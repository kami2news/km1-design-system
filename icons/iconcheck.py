"""KM1 のアイコンの検査 / Check the KM1 icon set (KM1-ICO-001 §7)
使い方 / Usage: python3 iconcheck.py km1-icons.json [KM1Icons.ttf]
FAIL があると終了コード 1。"""
import json, re, sys
from fontTools.svgLib.path import parse_path
from fontTools.pens.boundsPen import ControlBoundsPen, BoundsPen
res = []
def R(level, code, msg): res.append((level, code, msg))
d = json.load(open(sys.argv[1]))
icons = d['icons']
for n, e in icons.items():
    if not re.fullmatch(r'[a-z][a-z0-9]*(-[a-z0-9]+)*', n): R('FAIL', 'NAME', f'{n}: 名前は英小文字とハイフン / lowercase-hyphen names')
    if not e.get('ja') or not e.get('en'): R('FAIL', 'LABEL', f'{n}: 日本語と英語の名前がない / missing labels')
    if not (e.get('source') == 'km1' or str(e.get('source', '')).startswith('fluent:')): R('FAIL', 'SOURCE', f'{n}: 出典がない / missing source')
    if e.get('source') == 'km1' and not str(e.get('base', '')).startswith('fluent:'): R('FAIL', 'BASE', f'{n}: KM1 が描くアイコンは Fluent の絵を土台にする / KM1 drawings must build on a Fluent pictogram')
    for k in e.get('scaled', []): R('WARN', 'SCALED', f'{n} {k}: Fluent にその大きさがないので 20px の形を拡大・縮小した / scaled from 20px')
    for s in d['sizes']:
        for v in ('regular', 'filled'):
            p = e['paths'].get(f'{s}-{v}')
            if not p: R('FAIL', 'MISSING', f'{n}: {s}px {v} がない'); continue
            pen = ControlBoundsPen(None); parse_path(p, pen); b = pen.bounds
            if not b: R('FAIL', 'EMPTY', f'{n} {s}-{v}: 形が空 / empty'); continue
            tol = 0.05
            if b[0] < -tol or b[1] < -tol or b[2] > s + tol or b[3] > s + tol: R('FAIL', 'BOUNDS', f'{n} {s}-{v}: 枠の外にはみ出す {tuple(round(x, 2) for x in b)}')
            if e.get('style') == 'km1-b':
                # B 案は 20 の格子で余白 1（大きさに合わせて拡大・縮小）/ B: 1-unit margin on the 20 grid, scaled
                pen = BoundsPen(None); parse_path(p, pen); b = pen.bounds
                lo, hi = s / 20 - tol, s * 19 / 20 + tol
                if b[0] < lo or b[1] < lo or b[2] > hi or b[3] > hi: R('FAIL', 'LIVE', f'{n} {s}-{v}: B の余白を割る {tuple(round(x, 2) for x in b)}')
            elif e['source'] == 'km1':
                lo, hi = {16: (1, 15), 20: (2, 18), 24: (2, 22)}[s]; lo -= tol; hi += tol   # Fluent と同じ生きている範囲 / same live areas as Fluent
                if b[0] < lo or b[1] < lo or b[2] > hi or b[3] > hi: R('FAIL', 'LIVE', f'{n} {s}-{v}: 生きている範囲の外 {tuple(round(x, 2) for x in b)}')
    if e['paths'].get('20-regular') == e['paths'].get('20-filled') and e['source'] == 'km1':
        R('WARN', 'SAME', f'{n}: Regular と Filled が同じ形 / identical styles')
# KM1 B 案 / KM1 B icons
import os
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def cr(a, b):
    a, b = sorted((lum(a), lum(b)), reverse=True); return (a + 0.05) / (b + 0.05)
tj = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tokens.json')
if os.path.exists(tj):
    T = {t['name']: t['value'] for t in json.load(open(tj))['color']['tokens']}
    def res_(v, th):
        v = v[th] if isinstance(v, dict) else v
        while v.startswith('{'): v = T[v.strip('{}')][th] if isinstance(T[v.strip('{}')], dict) else T[v.strip('{}')]
        return v
    for th in ('light', 'dark'):
        ink = res_(T['icon-ink'], th)
        for other in ('surface', 'icon-tint-end', 'icon-tint-start'):
            r = cr(ink, res_(T[other], th))
            R('FAIL' if r < 3 else 'PASS', 'CONTRAST', f'{th}: icon-ink と {other} が {r:.2f}:1（3:1 以上）')
for n, e in icons.items():
    b = e.get('b')
    if not b: continue
    for k in ('16', '20', '24'):
        for part in ('ink', 'tint'):
            dd = b['ink'][k] if part == 'ink' else (b['tint'][k] if b.get('tint') else None)
            if part == 'ink' and not dd: R('FAIL', 'B', f'{n}: {k}px の線がない'); continue
            if not dd: continue
            pen = BoundsPen(None); parse_path(dd, pen); bb = pen.bounds
            if bb[0] < 1.0 or bb[1] < 1.0 or bb[2] > 19.0 or bb[3] > 19.0: R('FAIL', 'B-BOUNDS', f'{n} {k}px {part}: 20 の枠の余白 1 を割る {tuple(round(x, 2) for x in bb)}')
# Flutter のアイコンのファイルが、km1_theme.dart と km1_icons.dart だけで組み込めるか（km1_widgets.dart に頼らない）
# The Flutter icon files must build with only km1_theme.dart and km1_icons.dart (no dependency on km1_widgets.dart)
_B = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
_T = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'km1_theme.dart')
if os.path.exists(os.path.join(_B, 'km1_icons_b.dart')) and os.path.exists(_T):
    defs = set()
    for f in (_T, os.path.join(_B, 'km1_icons.dart')):
        defs |= set(re.findall(r'\b(?:class|enum|extension|mixin|typedef)\s+(\w+)', open(f, encoding='utf-8').read()))
    for f in ('km1_icons_b.dart', 'km1_icons.dart'):
        src = open(os.path.join(_B, f), encoding='utf-8').read()
        defs_self = defs | set(re.findall(r'\b(?:class|enum)\s+(\w+)', src))
        imps = re.findall(r"^import '([^']+)'", src, re.M)
        local = [i for i in imps if not i.startswith(('package:flutter/', 'dart:'))]
        bad_imp = [i for i in local if i not in ('km1_theme.dart', 'km1_icons.dart')]
        miss = sorted({u for u in re.findall(r'\b(Km1\w*)\b', src) if u not in defs_self})
        ext = re.findall(r'context\.(km1\w*)\b', src)
        if bad_imp or miss or ext: R('FAIL', 'DART', f'{f}: km1_theme.dart・km1_icons.dart だけでは組み込めない / not self-contained: imports {bad_imp} missing {miss} extensions {sorted(set(ext))}')
        else: R('PASS', 'DART', f'{f}: 自立して組み込める / self-contained')
if len(sys.argv) > 2:
    from fontTools.ttLib import TTFont
    f = TTFont(sys.argv[2]); cmap = f.getBestCmap()
    need = len(icons) * 2 * 3
    if len(cmap) != need: R('FAIL', 'FONT', f'フォントの字形の数 {len(cmap)}（要るのは {need}）/ font glyph count')
    else: R('PASS', 'FONT', f'{len(cmap)} 字形')
for l, c, m in res:
    if l != 'PASS' or '-v' in sys.argv: print(f'{l:4} {c:7} {m}')
nf = sum(1 for r in res if r[0] == 'FAIL'); nw = sum(1 for r in res if r[0] == 'WARN')
print(f'--- アイコン {len(icons)} 個（KM1 {sum(1 for e in icons.values() if e["source"] == "km1")}・Fluent {sum(1 for e in icons.values() if e["source"] != "km1")}）FAIL {nf} / WARN {nw}')
sys.exit(1 if nf else 0)
