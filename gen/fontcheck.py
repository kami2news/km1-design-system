#!/usr/bin/env python3
"""KM1 書体の検査（ソース・Office・PDF）/ Typeface check over sources, Office files and PDFs.

KM1-TYP-001 の機械で確かめられる項目だけを見る。/ Machine-checkable parts of KM1-TYP-001 only.
 1. ソースに使わない書体の名前がない（セリフ・明朝・手書き風・筆文字・装飾）。
 2. CSS の font-family の並びは、最後が sans-serif / monospace / system-ui（または var(--font-*) / inherit）。
 3. Office のテーマ: 見出しと本文の和文・欧文が游ゴシック。言語ごとの補助の書体にもセリフ・明朝・手書き風がない。
 4. PDF に埋め込まれた書体がゴシック系と等幅だけ。
usage: fontcheck.py <project dir> <out dir>
"""
import os, re, sys, zipfile, subprocess, glob

PROJ, OUT = sys.argv[1], sys.argv[2]
BANNED = re.compile(r"(?<!sans-)(?<!Sans )\b(serif|Mincho|Times New Roman|Times|Georgia|Garamond|Didot|Bodoni|Playfair|Cambria|Century|Courier New|Courier|Book Antiqua|Palatino|Baskerville|Segoe Script|Brush Script|Lucida Handwriting|Comic Sans|MV Boli|Angsana New|Sylfaen|Plantagenet Cherokee|cursive|fantasy)\b|明朝|明體|行書|草書|楷書|教科書|毛筆|ポップ体|HG[^\"']*(行書|正楷書|教科書|創英角ﾎﾟｯﾌﾟ)", re.I)
SRC_EXT = ('.css', '.js', '.ts', '.dart', '.kt', '.swift', '.xaml', '.html')
# 文章の中で書体の名前に触れるのは問題ない（決まりの説明）。コードだけ見る / docs may name fonts; only code is checked
res = []
def out(level, msg): res.append((level, msg))

# 1・2 ソース / sources
for root, _, files in os.walk(PROJ):
    if 'node_modules' in root: continue
    for f in files:
        p = os.path.join(root, f)
        name = f[:-4] if f.endswith('.txt') else f
        if not name.endswith(SRC_EXT) or name.endswith('.md'): continue
        if 'Compare' in root: pass  # Material との比較見本も同じ決まり / comparison previews follow the same rule
        s = open(p, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r"(font-family\s*:\s*[^;}<>\n]+|--font-[a-z-]+\s*:\s*[^;}<>\n]+|font\s*:\s*\d{3}[^;}\"']+|fontFamily(?:Fallback)?\s*[:=]\s*[^;\n]+|typeface\s*=\s*\"[^\"]*\"|FontFamily[^>]*>[^<]*)", s):
            decl = m.group(0).rstrip('"\\\' ')
            b = BANNED.search(decl)
            if b: out('FAIL', f'{os.path.relpath(p, PROJ)}: 使わない書体 / banned family "{b.group(0)}" in `{decl.strip()[:90]}`')
            if decl.startswith(('font-family', '--font-')) and name.endswith(('.css', '.html', '.js')):
                stack = decl.split(':', 1)[1].strip().rstrip(',').strip()
                last = stack.split(',')[-1].strip().strip('"\'').lower()
                if not (last in ('sans-serif', 'monospace', 'system-ui', 'inherit') or stack.startswith('var(--font-')):
                    out('FAIL', f'{os.path.relpath(p, PROJ)}: 並びの最後がゴシック系でない / stack does not end in a sans generic: `{stack[:80]}`')
        # SVG の文字は書体を明示する（既定はセリフ）/ SVG <text> must name a family (the default is serif)
        for m in re.finditer(r"<text\b[^>]*>", s):
            if 'font-family' not in m.group(0) and 'class=' not in m.group(0):
                out('WARN', f'{os.path.relpath(p, PROJ)}: SVG の <text> に font-family がない / SVG <text> without font-family')

# 3 Office
for p in sorted(glob.glob(os.path.join(OUT, '*.docx')) + glob.glob(os.path.join(OUT, '*.dotx')) + glob.glob(os.path.join(OUT, '*.pptx')) + glob.glob(os.path.join(OUT, '*.potx'))):
    z = zipfile.ZipFile(p)
    for n in z.namelist():
        if not n.endswith('.xml'): continue
        x = z.read(n).decode('utf-8', 'ignore')
        for m in re.finditer(r'(?:typeface|w:ascii|w:hAnsi|w:eastAsia|w:cs)="([^"]+)"', x):
            if BANNED.search(m.group(1)): out('FAIL', f'{os.path.basename(p)} {n}: 使わない書体 / banned "{m.group(1)}"')
        if '/theme/' in n:
            for tag in ('majorFont', 'minorFont'):
                blk = re.search(rf'<a:{tag}>(.*?)</a:{tag}>', x, re.S)
                if not blk: continue
                for k in ('latin', 'ea'):
                    t = re.search(rf'<a:{k} typeface="([^"]*)"', blk.group(1))
                    if not t or t.group(1) != '游ゴシック': out('FAIL', f'{os.path.basename(p)} {tag}/{k} が游ゴシックでない / not 游ゴシック: {t.group(1) if t else None}')

# 4 PDF
for p in sorted(glob.glob(os.path.join(OUT, '*.pdf'))):
    if os.path.basename(p).startswith('pass'): continue
    r = subprocess.run(['pdffonts', p], capture_output=True, text=True).stdout.splitlines()[2:]
    for line in r:
        fam = line.split()[0].split('+')[-1]
        if BANNED.search(fam) or not re.search(r'Sans|Gothic|Mono|Hind|Segoe|Inter', fam, re.I):
            out('FAIL', f'{os.path.basename(p)}: 埋め込み書体 / embedded font {fam}')

# 5 基本の書体とフォーム部品 / base font on the root and inheritance on form controls (KM1-TYP-002)
for rel in ('components/bundle.css', 'pdf/km1-print.css'):
    p = os.path.join(PROJ, rel)
    if not os.path.exists(p): continue
    s = open(p, encoding='utf-8', errors='ignore').read()
    if not re.search(r'(?:^|[,}\s])(?:html|:root|body)\b[^{}]*\{[^{}]*font-family', s, re.M):
        out('WARN', f'{rel}: html / :root / body に基本の font-family がない / no base font-family on html, :root or body')
    if rel.endswith('bundle.css') and not re.search(r'(?:button|input|select|textarea)[^{}]*\{[^{}]*font(?:-family)?\s*:\s*inherit', s):
        out('WARN', f'{rel}: button / input / select / textarea に font の継承がない / form controls do not inherit the font')
# 6 書体テストページがトークンを読んでいるか / the font test page must read the font tokens
for rel in ('gen/fonttest.html', 'gen/fonttest.html.txt'):
    p = os.path.join(PROJ, rel)
    if os.path.exists(p):
        if '--font-sans' not in open(p, encoding='utf-8', errors='ignore').read():
            out('FAIL', f'{rel}: --font-sans を読んでいない / does not read --font-sans')
        break

for l, m in res: print(l, m)
nf = sum(1 for l, _ in res if l == 'FAIL'); nw = sum(1 for l, _ in res if l == 'WARN')
print(f'  --- FAIL {nf} / WARN {nw}  （機械で確かめられる項目だけ / machine checks only）')
sys.exit(1 if nf else 0)
