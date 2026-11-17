#!/usr/bin/env python3
"""KM1 の PDF（デザイン標準・部品カタログ）を Markdown から作る / Build the KM1 PDFs from the Markdown docs
使い方 / Usage: python3 build_pdf.py <出力フォルダ / out dir>
必要 / Requires: markdown, pypdf, Google Chrome（headless）
pdf/km1-print.css を使い、pdf/km1_finish.py で文書情報を足す。名前・勤め先などの個人情報は扱わない。
Uses pdf/km1-print.css and finishes with pdf/km1_finish.py. Handles no personal information.
"""
import os, re, sys, subprocess, tempfile, shutil, glob, html
import markdown
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
DATE = os.environ.get('KM1_DATE', '2026-11-18')
CHROME = shutil.which('google-chrome') or shutil.which('chromium') or 'google-chrome'
STANDARD = ['README','principles','tokens','patterns','platforms','icons','dataviz','documents','office','product',
            'governance','verification','coverage','adoption','proposals','m1','notices']

def md(path):
    s = open(path, encoding='utf-8').read()
    return markdown.markdown(s, extensions=['tables', 'fenced_code', 'sane_lists'])

def build(name, title, subtitle, sections, pdf):
    css = open(os.path.join(ROOT, 'pdf', 'km1-print.css'), encoding='utf-8').read()
    css = css.replace('content:"文書名 / Document name"', f'content:"{title}"').replace('content:"YYYY-MM-DD"', f'content:"{DATE}"')
    toc = ''.join(f'<li>{html.escape(t)}</li>' for t, _ in sections)
    body = (f'<section class="cover"><div class="mark"></div><div class="title">{html.escape(title)}</div>'
            f'<div class="subtitle">{html.escape(subtitle)}</div><div class="meta"><p>版 / Edition: {DATE}</p>'
            f'<p>作成者 / Author: KM1 作成者</p></div></section>'
            f'<section class="toc chapter"><h1>目次 / Contents</h1><ol>{toc}</ol></section>'
            + ''.join(f'<section class="chapter">{h}</section>' for _, h in sections))
    d = tempfile.mkdtemp()
    open(os.path.join(d, 'km1-print.css'), 'w', encoding='utf-8').write(css)
    hp = os.path.join(d, 'index.html')
    open(hp, 'w', encoding='utf-8').write(f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
        f'<link rel="stylesheet" href="km1-print.css"></head><body>{body}</body></html>')
    raw = os.path.join(d, 'raw.pdf')
    subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer', '--generate-pdf-document-outline', '--export-tagged-pdf',
                    f'--print-to-pdf={raw}', 'file://' + hp], check=True, stderr=subprocess.DEVNULL)
    subprocess.run([sys.executable, os.path.join(ROOT, 'pdf', 'km1_finish.py'), raw, pdf, '--title', title, '--lang', 'ja'], check=True)
    print('pdf', pdf)

def title_of(h, fallback):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
    return re.sub('<[^>]+>', '', m.group(1)) if m else fallback

os.makedirs(OUT, exist_ok=True)
std = []
for n in STANDARD:
    p = os.path.join(ROOT, n + '.md')
    if os.path.exists(p): h = md(p); std.append((title_of(h, n), h))
build('standard', 'KM1 デザイン標準', 'Design standard', std, os.path.join(OUT, 'KM1_デザイン標準.pdf'))
cat = []
for p in sorted(glob.glob(os.path.join(ROOT, 'components', '*', 'README.md'))):
    n = os.path.basename(os.path.dirname(p)); h = md(p)
    cat.append((n, f'<h1>{html.escape(n)}</h1>' + h))
build('catalog', 'KM1 部品カタログ', 'Component catalog', cat, os.path.join(OUT, 'KM1_部品カタログ.pdf'))
