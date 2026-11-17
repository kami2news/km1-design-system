#!/usr/bin/env python3
"""KM1 のアイコン一覧の図を作る / Build the KM1 icon list sheet
使い方 / Usage: python3 icon_sheet.py [出力 / out.svg]（既定は icons/icon-list.svg）
km1-icons.json の B 案（通常表示）を、名前・日本語名つきで格子に並べる。GitHub の icons.md と PDF から参照する。
Lays out every B icon (regular display) with its name and Japanese label; referenced from icons.md and the PDF."""
import json, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'icon-list.svg')
d = json.load(open(os.path.join(HERE, 'km1-icons.json'), encoding='utf-8'))['icons']
COLS, CW, CH, PAD = 8, 120, 92, 16
INK, SUB, LINE, T0, T1 = '#242424', '#616161', '#E0E0E0', '#F6F8FB', '#D3DCE7'
names = list(d)
rows = (len(names) + COLS - 1) // COLS
W, H = COLS * CW + PAD * 2, rows * CH + PAD * 2 + 40
F = 'font-family="Noto Sans JP,Noto Sans CJK JP,Segoe UI,sans-serif"'
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">',
     f'<title>KM1 アイコン一覧（{len(names)} 個、B 案・24px）/ KM1 icon list</title>',
     f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
     f'<text x="{PAD}" y="{PAD+18}" {F} font-size="16" font-weight="700" fill="#10218B">KM1 アイコン一覧 / Icon list — {len(names)}</text>', '<defs>']
for n in names:
    b = d[n]['b']
    if b['tint']:
        o.append(f'<linearGradient id="g-{n}" gradientUnits="userSpaceOnUse" x1="0" y1="{b["tintY"][0]}" x2="0" y2="{b["tintY"][1]}"><stop stop-color="{T0}"/><stop offset="1" stop-color="{T1}"/></linearGradient>')
o.append('</defs>')
for i, n in enumerate(names):
    e = d[n]; b = e['b']; x = PAD + (i % COLS) * CW; y = PAD + 40 + (i // COLS) * CH
    o.append(f'<rect x="{x+.5}" y="{y+.5}" width="{CW-1}" height="{CH-1}" fill="none" stroke="{LINE}"/>')
    o.append(f'<g transform="translate({x+CW/2-16} {y+10}) scale(1.6)">')   # 20 単位の形を 32px に / 20-unit art at 32px
    if b['tint']: o.append(f'<path fill="url(#g-{n})" d="{b["tint"]["24"]}"/>')
    o.append(f'<path fill="{INK}" d="{b["ink"]["24"]}"/></g>')
    o.append(f'<text x="{x+CW/2}" y="{y+60}" {F} font-size="11" fill="{INK}" text-anchor="middle">{html.escape(n)}</text>')
    o.append(f'<text x="{x+CW/2}" y="{y+76}" {F} font-size="10" fill="{SUB}" text-anchor="middle">{html.escape(e["ja"])}</text>')
o.append('</svg>')
open(OUT, 'w', encoding='utf-8').write('\n'.join(o))
print('icon list', len(names), OUT)
