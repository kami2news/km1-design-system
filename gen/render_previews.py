#!/usr/bin/env python3
"""部品の見本を単独の HTML にする / Render component previews as standalone HTML pages
使い方 / Usage: python3 render_previews.py <出力フォルダ / out dir>
components/*/preview.html を tokens.css・bundle.css・React 18・bundle.js と組み合わせ、
<名前>-light.html と <名前>-dark.html を作る。React は gen/node_modules（`npm i` で入る）から読む。
Combines each preview with tokens.css, bundle.css, React 18 and bundle.js into <name>-light/-dark.html.
React comes from gen/node_modules (run `npm i` in gen/)."""
import os, sys, glob, shutil
G = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(G)
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '/tmp/rc')
NM = os.environ.get('KM1_NODE_MODULES', os.path.join(G, 'node_modules'))
os.makedirs(OUT, exist_ok=True)
assets = {
    'tokens.css': os.path.join(ROOT, 'tokens.css'),
    'bundle.css': os.path.join(ROOT, 'components', 'bundle.css'),
    'bundle.js': os.path.join(ROOT, 'components', 'bundle.js'),
    'react.js': os.path.join(NM, 'react', 'umd', 'react.production.min.js'),
    'react-dom.js': os.path.join(NM, 'react-dom', 'umd', 'react-dom.production.min.js'),
}
for name, src in assets.items():
    if not os.path.exists(src): sys.exit(f'見つからない / missing: {src}（gen で npm i / run npm i in gen/）')
    shutil.copy(src, os.path.join(OUT, name))
n = 0
for p in sorted(glob.glob(os.path.join(ROOT, 'components', '*', 'preview.html'))):
    comp = os.path.basename(os.path.dirname(p)); body = open(p, encoding='utf-8').read()
    for theme in ('light', 'dark'):
        html = (f'<!doctype html><html lang="ja" data-theme="{theme}"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{comp}</title>'
                '<link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css">'
                '<script src="react.js"></script><script src="react-dom.js"></script><script src="bundle.js"></script>'
                '<style>body{margin:0;background:var(--surface);color:var(--ink);font-family:var(--font-sans)}</style>'
                f'</head><body>{body}</body></html>')
        open(os.path.join(OUT, f'{comp}-{theme}.html'), 'w', encoding='utf-8').write(html)
        n += 1
print(f'{n} ページ / pages → {OUT}')
