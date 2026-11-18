#!/usr/bin/env python3
"""KM1 の PDF 2 冊（本編「デザイン標準」と別冊「部品カタログ」）を作る / Build the two KM1 PDF volumes
使い方 / Usage: python3 build_pdf.py <出力フォルダ / out dir> [--skip-checks]
必要 / Requires: markdown, pypdf, Pillow, Google Chrome（headless）。見本の画像は先に
  `node gen/shoot_previews.js` で撮っておく（gen で npm i が要る）。
documents.md「PDF の規定」（KM1-DOC-001）どおりに作る:
- 表紙（題名・副題・版・作成者「KM1 作成者」・全 2 冊の組とファイル名・部品の数）。表紙に柱とページ番号を出さない
- 目次（章と節、ページ番号つき。2 回書き出してページ番号を入れる）とPDF のしおり
- 章の番号は 2 冊で通し。本編の第 11 章は別冊の案内。本編の最後に変更履歴。どちらも最後に奥付（notices.md §2）
- 図は <figure role="group"> に代替テキストと図の番号。英語の段落は lang="en"
- 部品の見本は等倍（画面の 1px ＝ 0.26mm）。縦に長い見本は行と行のあいだの空白（10px 以上）で切って等倍のまま分ける。
  ページの幅に入らないものだけ縮め、倍率を図の説明に書く。説明は見本の下に 3 段
- 作る前に sync_counts.py --check と sizecheck.py を通す（--skip-checks で省略。配布物では省略しない）
- 名前・勤め先など個人の情報は扱わない（見本は架空の名前だけ）
Builds both volumes per documents.md (KM1-DOC-001): cover with set info, paged contents, bookmarks, chapter numbers
across volumes, changelog and colophon, true-size previews split at blank gaps, checks before building.
"""
import os, re, sys, glob, html, json, shutil, subprocess, tempfile
import markdown
from PIL import Image
from pypdf import PdfReader

G = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(G)
sys.path.insert(0, G)
from catalog_md import groups as preview_groups  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = os.path.abspath(args[0] if args else '.')
SKIP = '--skip-checks' in sys.argv
DATE = os.environ.get('KM1_DATE') or __import__('datetime').date.today().isoformat()
CHROME = os.environ.get('CHROME') or shutil.which('google-chrome') or shutil.which('chromium') or 'google-chrome'
MAIN_FILE, CAT_FILE = 'KM1_デザイン標準.pdf', 'KM1_部品カタログ.pdf'
CAT_CHAPTER = 11
# 本編の章（ファイル）。None は別冊の案内の章 / main-volume chapters; None marks the pointer chapter
MAIN = ['README', 'principles', 'tokens', 'patterns', 'platforms', 'icons', 'documents', 'office', 'product', 'dataviz',
        None, 'governance', 'verification', 'coverage', 'adoption', 'proposals', 'm1', 'notices']
assert MAIN.index(None) + 1 == CAT_CHAPTER
PX_MM = 25.4 / 96                       # CSS 1px = 0.2646mm
FIG = [0]

# ---------- 検査 / checks ----------
def checks():
    subprocess.run([sys.executable, os.path.join(G, 'sync_counts.py'), '--check'], check=True)
    subprocess.run([sys.executable, os.path.join(G, 'sizecheck.py')], check=True)

# ---------- Markdown → HTML ----------
def escape_raw_html(s):
    """コードの外の生の HTML タグを文字にする（文書は HTML を書かない約束）/ escape raw HTML outside code"""
    out = []
    for i, block in enumerate(re.split(r'(```.*?```)', s, flags=re.S)):
        if i % 2: out.append(block); continue
        parts = re.split(r'(`[^`\n]*`)', block)
        out.append(''.join(x if j % 2 else re.sub(r'<(?=[A-Za-z/!])', '&lt;', x) for j, x in enumerate(parts)))
    return ''.join(out)

def english(h):
    """英語の段落（*...*）に lang="en" / mark English lines"""
    def rep(m):
        t = m.group(1); plain = re.sub('<[^>]+>', '', t)
        latin = sum(c.isascii() and c.isalpha() for c in plain); cjk = sum(ord(c) > 0x2e80 for c in plain)
        return f'<span class="en" lang="en">{t}</span>' if latin > 12 and latin > cjk * 3 else m.group(0)
    return re.sub(r'<em>(.*?)</em>', rep, h, flags=re.S)

def figures(h, base):
    """画像を図にする（role="group"・代替テキスト・図の番号）/ wrap images as numbered figures"""
    def rep(m):
        alt, src = m.group(1), m.group(2)
        if not re.match(r'(https?|file|data):', src): src = 'file://' + os.path.join(base, src)
        FIG[0] += 1; cap = html.unescape(alt).split(' — ')[0]
        return f'<figure role="group"><img src="{src}" alt="{alt}"><figcaption>図 {FIG[0]} {html.escape(cap)}</figcaption></figure>'
    h = re.sub(r'<p>\s*((?:<img [^>]*>\s*)+)</p>', lambda m: m.group(1), h)   # 段落から出す / unwrap
    return re.sub(r'<img alt="([^"]*)" src="([^"]+)"\s*/?>', rep, h)

def md_html(path, shift=0, number=None):
    s = escape_raw_html(open(path, encoding='utf-8').read())
    h = markdown.markdown(s, extensions=['tables', 'fenced_code', 'sane_lists'])
    h = english(figures(h, os.path.dirname(os.path.abspath(path))))
    if shift:   # 見出しを下げる / demote headings
        h = re.sub(r'<(/?)h([1-5])\b', lambda m: f'<{m.group(1)}h{int(m.group(2)) + shift}', h)
    if number is not None:   # 章の番号 / chapter number on the first h1
        h = re.sub(r'<h1>', f'<h1>{number}. ', h, count=1)
    return h

# ---------- 見本の画像 / preview images ----------
def slices(png, tmp, first_max, max_h, page_w):
    """等倍で載せる。縦に長いものは空白の行で切る / true size; split tall images at blank rows"""
    im = Image.open(png).convert('RGB'); W, H = im.size     # 2 倍で撮っている / shot at 2x
    css_w = W / 2; scale = min(1.0, page_w / css_w)
    px = im.load(); bg = px[W - 1, H - 1]
    blank = [all(px[x, y] == bg for x in range(0, W, 3)) for y in range(H)]
    out, top, limit = [], 0, first_max
    while top < H:
        end = min(H, top + int(limit * 2 / scale))
        if end < H:   # 空白が 10px（2 倍で 20 行）以上続く所の真ん中で切る / cut mid-gap of ≥10px blank
            best = None; run = 0
            for y in range(end, top + 40, -1):
                run = run + 1 if blank[y] else 0
                if run >= 20: best = y + run // 2; break
            end = best or end
        f = os.path.join(tmp, f'{os.path.basename(os.path.dirname(png))}_{len(out)}.png')
        im.crop((0, top, W, end)).save(f); out.append((f, (end - top) / 2))
        top, limit = end, max_h
    return css_w, scale, out

def preview_section(name, tmp, page_w):
    png = os.path.join(ROOT, 'components', name, 'preview.png')
    readme = os.path.join(ROOT, 'components', name, 'README.md')
    body = md_html(readme, shift=2) if os.path.exists(readme) else ''
    parts = [f'<section class="comp"><h3>{html.escape(name)}</h3>']
    if os.path.exists(png):
        css_w, scale, sl = slices(png, tmp, 520, 600, page_w)
        FIG[0] += 1
        note = '等倍' if scale >= 0.999 else f'{scale * 100:.0f}% に縮小'
        for i, (f, h) in enumerate(sl):
            cap = f'図 {FIG[0]} {name} の見本（{note}' + (f'、{i + 1}/{len(sl)}' if len(sl) > 1 else '') + '）'
            parts.append(f'<figure role="group" class="pv"><img src="file://{f}" alt="{html.escape(name)} の見本 / {html.escape(name)} preview'
                         + (f' ({i + 1}/{len(sl)})' if len(sl) > 1 else '') + f'" style="width:{css_w * scale:.1f}px;height:{h * scale:.1f}px">'
                         f'<figcaption>{cap}</figcaption></figure>')
    parts.append(f'<div class="cols">{body}</div></section>')
    return ''.join(parts)

# ---------- 組み立て / assembly ----------
def colophon():
    s = open(os.path.join(ROOT, 'notices.md'), encoding='utf-8').read()
    sec = s.split('## 2.', 1)[1].split('\n## 3.', 1)[0]
    quotes = '\n\n'.join(re.findall(r'^(?:> .*\n?)+', sec, flags=re.M))
    h = english(markdown.markdown(escape_raw_html(quotes)))
    return (f'<section class="chapter colophon"><h1>奥付 / Colophon</h1>{h}'
            f'<p>版 / Edition: {DATE}<br>作成者 / Author: KM1 作成者</p>'
            f'<p>組 / Set: {MAIN_FILE}（本編）・{CAT_FILE}（別冊）</p></section>')

def cover(title, subtitle, vol, counts):
    return (f'<section class="cover"><div class="mark"></div><div class="title">{html.escape(title)}</div>'
            f'<div class="subtitle">{html.escape(subtitle)}</div>'
            f'<div class="meta"><p>全 2 冊・{vol} / Volume {1 if vol == "本編" else 2} of 2</p>'
            f'<p>組のファイル / Set: {MAIN_FILE}（本編）・{CAT_FILE}（別冊）</p><p>{counts}</p>'
            f'<p>版 / Edition: {DATE}</p><p>作成者 / Author: KM1 作成者</p></div></section>')

def toc(heads, pages=None):
    items = []
    for k, (lvl, text, hid) in enumerate(heads):
        pg = pages[k] if pages else '000'
        items.append(f'<li class="l{lvl}"><a href="#{hid}">{html.escape(text)}</a><span class="pg">{pg}</span></li>')
    return f'<section class="toc"><h1>目次 / Contents</h1><ol>{"".join(items)}</ol></section>'

def ids(body):
    """h1・h2 に id を振り、目次の項目を集める / id headings and collect contents entries"""
    heads = []; n = [0]
    def rep(m):
        lvl, inner = int(m.group(1)), m.group(2); n[0] += 1; hid = f'h{n[0]}'
        heads.append((lvl, html.unescape(re.sub('<[^>]+>', '', inner)).strip(), hid))
        return f'<h{lvl} id="{hid}">{inner}</h{lvl}>'
    return re.sub(r'<h([12])>(.*?)</h\1>', rep, body, flags=re.S), heads

def outline_pages(pdf):
    r = PdfReader(pdf); out = []
    def walk(o):
        for x in o:
            if isinstance(x, list): walk(x)
            else: out.append((re.sub(r'\s+', ' ', x.title).strip(), r.get_destination_page_number(x) + 1))
    walk(r.outline); return out

def render(title, body_html, pdf, landscape):
    css = open(os.path.join(ROOT, 'pdf', 'km1-print.css'), encoding='utf-8').read()
    css = css.replace('content:"文書名 / Document name"', f'content:"{title}"').replace('content:"YYYY-MM-DD"', f'content:"{DATE}"')
    if landscape: css = css.replace('@page{size:A4;', '@page{size:A4 landscape;') + '.cover{height:160mm}'
    else: css += '.cover{height:245mm}'
    css += ('.cover{overflow:hidden;break-after:page}.cover .meta p{margin:0 0 1mm}'
            'figure img{max-width:100%;height:auto}.pv img{max-width:none;border:1px solid #d1d1d1}.pv{margin:2mm 0 3mm}'
            '.toc li.l2{padding-left:5mm;font-size:9pt}.toc li.l1{font-weight:700;margin-top:2mm}'
            '.comp{break-before:page}.comp>h3{font-size:13pt;margin:0 0 2mm}.cols{columns:3;column-gap:6mm;font-size:8.6pt;line-height:1.55}'
            '.cols h4,.cols h5,.cols h6{break-after:avoid;font-size:9.5pt;margin:2mm 0 1mm}.cols table{font-size:7.6pt}.cols pre{font-size:7.4pt}'
            '.colophon blockquote{margin:2mm 0 4mm;padding-left:3mm;border-left:3px solid #d1d1d1}')
    d = tempfile.mkdtemp(prefix='km1-pdf-'); hp = os.path.join(d, 'index.html')
    open(os.path.join(d, 'km1-print.css'), 'w', encoding='utf-8').write(css)
    open(hp, 'w', encoding='utf-8').write(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
                                          f'<link rel="stylesheet" href="km1-print.css"></head><body>{body_html}</body></html>')
    raw = os.path.join(d, 'raw.pdf')
    subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--allow-file-access-from-files', '--no-pdf-header-footer',
                    '--generate-pdf-document-outline', '--export-tagged-pdf', f'--print-to-pdf={raw}', 'file://' + hp],
                   check=True, stderr=subprocess.DEVNULL)
    return raw

def build(title, front, body, pdf, landscape=False):
    body, heads = ids(body)
    raw = render(title, front + toc(heads) + body, pdf, landscape)          # 1 回目 / pass 1
    fixed = raw + '.fixed.pdf'                                               # Chrome のしおりの題名の重複を直してから読む
    subprocess.run([sys.executable, os.path.join(ROOT, 'pdf', 'km1_finish.py'), raw, fixed], check=True, stdout=subprocess.DEVNULL)
    ol = outline_pages(fixed); pages = []; i = 0
    for lvl, text, _ in heads:                                              # しおりと順に照らす / match in order
        while i < len(ol) and ol[i][0] != re.sub(r'\s+', ' ', text): i += 1
        pages.append(ol[i][1] if i < len(ol) else ''); i += 1
    raw = render(title, front + toc(heads, pages) + body, pdf, landscape)  # 2 回目 / pass 2
    subprocess.run([sys.executable, os.path.join(ROOT, 'pdf', 'km1_finish.py'), raw, pdf, '--title', title, '--lang', 'ja'], check=True)
    print('pdf', pdf, len(PdfReader(pdf).pages), 'pages')

def main():
    if not SKIP: checks()
    os.makedirs(OUT, exist_ok=True)
    inv = json.load(open(os.path.join(ROOT, 'inventory.json'), encoding='utf-8'))
    counts = f'部品 Web {inv["web"]["components"]}・Flutter 専用 {inv["flutter"]["widgets"]} / Components: Web {inv["web"]["components"]}, Flutter-only {inv["flutter"]["widgets"]}'
    gs = [(g, lab, [n for n in ns if n != 'Cover']) for g, lab, ns in preview_groups()]
    gs = [x for x in gs if x[2]]
    # 本編 / main volume
    FIG[0] = 0; chapters = []
    for k, n in enumerate(MAIN, 1):
        if n is None:
            lst = ''.join(f'<li><strong>{html.escape(lab)}</strong>: {"・".join(ns)}</li>' for _, lab, ns in gs)
            chapters.append(f'<section class="chapter"><h1>{k}. 部品 / Components</h1>'
                            f'<p>部品の見本と説明は別冊「KM1 部品カタログ」（{CAT_FILE}、横向き）の第 {k} 章に載せている。'
                            f'寸法の決まりは第 3 章「トークン」の「部品の寸法」、部品とプラットフォームの対応は第 {MAIN.index("coverage") + 1} 章。</p>'
                            f'<span class="en" lang="en">Component previews and guidance are in the companion volume, chapter {k}. Sizes are in chapter 3; platform coverage in chapter {MAIN.index("coverage") + 1}.</span>'
                            f'<h2>別冊に載せている部品 / In the catalog</h2><ul>{lst}</ul></section>')
        else:
            chapters.append(f'<section class="chapter">{md_html(os.path.join(ROOT, n + ".md"), number=k)}</section>')
    chapters.append(f'<section class="chapter">{md_html(os.path.join(ROOT, "changelog.md"))}</section>')
    build('KM1 デザイン標準', cover('KM1 デザイン標準', 'Design standard', '本編', counts), ''.join(chapters) + colophon(),
          os.path.join(OUT, MAIN_FILE))
    # 別冊 / catalog volume
    FIG[0] = 0; tmp = tempfile.mkdtemp(prefix='km1-cat-'); page_w = (297 - 34) / PX_MM - 4
    body = [f'<section class="chapter"><h1>{CAT_CHAPTER}. 部品 / Components</h1>'
            '<p>見本はすべて等倍（画面の 1px ＝ 0.26mm）。縦に長い見本は、行と行のあいだの空白で切って等倍のまま分けて載せる。'
            'ページの幅に入らない見本だけ縮め、図の説明に倍率を書く。Dialog・Drawer・BottomSheet・Menu・Popover・Toast は開いた状態。</p>'
            '<span class="en" lang="en">Previews are true size (1px = 0.26mm); tall ones are split at blank gaps, and only those wider than the page are scaled, with the ratio in the caption. Overlays are shown open.</span></section>']
    for g, lab, ns in gs:
        body.append(f'<section class="chapter"><h2>{html.escape(lab)}</h2><p>{"・".join(ns)}</p></section>')
        body += [preview_section(n, tmp, page_w) for n in ns]
    build('KM1 部品カタログ', cover('KM1 部品カタログ', 'Component catalog', '別冊', counts), ''.join(body) + colophon(),
          os.path.join(OUT, CAT_FILE), landscape=True)

if __name__ == '__main__':
    main()
