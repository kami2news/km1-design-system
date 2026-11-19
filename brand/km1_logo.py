"""KM1 のロゴと表示バッジを作る / Build the KM1 logo and attribution badge (KM1-ICO-001 §9)

しるし（アプリアイコンと同じ絵）・横組み（しるし＋「KM1」）・表示バッジ（Designed with KM1 / KM1 で設計）を、
ライト・ダーク・単色で SVG と PNG（1・2・3 倍）に書き出す。文字は Noto Sans CJK JP の字形を輪郭にする（SIL OFL 1.1）。
Writes the mark, the horizontal lockup and the attribution badge in light, dark and mono, as SVG and PNG @1x/2x/3x.

使い方 / Usage:  python3 brand/km1_logo.py dist/logo
必要なもの / Needs: fonttools, rsvg-convert（librsvg）
"""
import os, sys, subprocess
from fontTools.ttLib import TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'icons'))
from km1_appicon import artwork, wordmark   # 形はアプリアイコンと同じ（色は白地に青）/ same drawing as the app icon, blue on white

NOTO = '/usr/share/fonts/opentype/noto/NotoSansCJK-{}.ttc'
_fonts = {}
def font(weight):
    if weight not in _fonts:
        _fonts[weight] = TTCollection(NOTO.format(weight)).fonts[0]   # 0 = JP
    return _fonts[weight]

# KM1 のトークンの値 / KM1 token values (tokens.json)
THEMES = {
    'light': dict(surface='FFFFFF', stroke='D1D1D1', ink='242424', ink2='424242', mark_bg='FFFFFF', mark_fg='10218B'),   # brand-700
    'dark':  dict(surface='292929', stroke='666666', ink='FFFFFF', ink2='D6D6D6', mark_bg='FFFFFF', mark_fg='10218B'),   # ダークでも白地に紺 / white tile on dark too
}
RADIUS = 0.125   # しるしの角: 32px で radius-md（4px）と同じ比 / mark corner = radius-md at 32px

def text_path(runs, size):
    """[(文字列, 太さ), ...] を 1 本のパスにする。原点は基線の左端。返す値 (d, 幅) / runs → outline path at font size"""
    pen_d, x = [], 0.0
    for s, w in runs:
        tt = font(w); gs = tt.getGlyphSet(); cmap = tt.getBestCmap(); k = size / tt['head'].unitsPerEm
        for ch in s:
            g = cmap[ord(ch)]
            pen = SVGPathPen(gs)
            gs[g].draw(TransformPen(pen, (k, 0, 0, -k, x, 0)))
            pen_d.append(pen.getCommands())
            x += gs[g].width * k
    return ' '.join(pen_d), x

def mark_svg(size, c, mono=False):
    """ロゴのしるし: 白地に青。§6 のアプリアイコン（紺地に白）の色を入れ替えたもの。白い面が明るい背景に溶けないよう、
    縁を青で囲む（太さはしるしの 1/32。32px で 1px）。48px 未満は帯を省く。単色は縁・文字・帯を ink 1 色で、地は透明。
    Logo mark: blue on white (the §6 app icon with colours swapped), framed by a blue border (size/32);
    under 48px the bar is dropped. Mono draws border, letters and bar in ink on a transparent ground."""
    small = size < 48
    fg = c['ink'] if mono else c['mark_fg']
    s = artwork(size, 'FFFFFF', fg, ('text', wordmark('KM1')), small=small)
    inner = s[s.index('>') + 1:s.rindex('</svg>')]
    body = inner.split('/>', 1)[1]          # 地の四角を外して文字と帯だけ / drop the ground rect
    sw = max(1.0, size / 32); r = size * RADIUS
    ground = 'none' if mono else f'#{c["mark_bg"]}'
    frame = f'<rect x="{sw / 2:g}" y="{sw / 2:g}" width="{size - sw:g}" height="{size - sw:g}" rx="{r - sw / 2:.2f}" fill="{ground}" stroke="#{fg}" stroke-width="{sw:g}"/>'
    return frame + body

def doc(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}">{body}</svg>'

def lockup(H, c, mono=False):
    """横組み: しるし＋間（しるしの 1/4）＋「KM1」（大文字の高さ＝しるしの 0.42）/ mark + gap (H/4) + wordmark (cap height 0.42 H)"""
    d, w, asc = wordmark('KM1')
    k = (H * 0.42) / asc
    gap = H * 0.25
    x = H + gap; y = (H - asc * k) / 2
    body = f'<g>{mark_svg(int(H), c, mono)}</g><path transform="translate({x:.2f} {y:.2f}) scale({k:.5f})" d="{d}" fill="#{c["ink"]}"/>'
    return doc(round(x + w * k, 2), H, body)

def badge(lang, c, H=24):
    """表示バッジ。高さ 24px（小さい部品の高さ）、縁 1px、角 radius-md（4px）、しるし 16px、文字 12px（caption-1）
    Badge: 24px tall, 1px border, radius-md, 16px mark, 12px text"""
    fs = 12
    runs = [('Designed with ', 'Regular'), ('KM1', 'Bold')] if lang == 'en' else [('KM1', 'Bold'), (' で設計', 'Regular')]
    pad, m, gap, padr = 4, 16, 6, 8
    parts, x = [], pad + m + gap
    base = H / 2 + fs * 0.37   # 大文字の中心を高さの中央に / centre the cap height
    for s, wt in runs:
        d, w = text_path([(s, wt)], fs)
        col = c['ink'] if wt == 'Bold' else c['ink2']
        parts.append(f'<path transform="translate({x:.2f} {base:.2f})" d="{d}" fill="#{col}"/>')
        x += w
    W = round(x + padr)
    body = (f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="4" fill="#{c["surface"]}" stroke="#{c["stroke"]}"/>'
            f'<g transform="translate({pad} {(H - m) / 2:g})">{mark_svg(m, c)}</g>' + ''.join(parts))
    label = 'Designed with KM1' if lang == 'en' else 'KM1 で設計'
    return doc(W, H, body).replace('>', f' role="img" aria-label="{label}"><title>{label}</title>', 1)

def png(svg, path, scale):
    import re
    w = float(re.search(r'width="([\d.]+)"', svg).group(1))
    out = subprocess.run(['rsvg-convert', '-w', str(round(w * scale))], input=svg.encode(), capture_output=True, check=True).stdout
    open(path, 'wb').write(out)

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else 'dist/logo'
    os.makedirs(out, exist_ok=True)
    L, D = THEMES['light'], THEMES['dark']
    files = {
        'km1-mark.svg': doc(64, 64, mark_svg(64, L)),
        'km1-mark-dark.svg': doc(64, 64, mark_svg(64, D)),
        'km1-mark-mono.svg': doc(64, 64, mark_svg(64, L, mono=True)),
        'km1-logo.svg': lockup(64, L),
        'km1-logo-dark.svg': lockup(64, D),
        'km1-logo-mono.svg': lockup(64, L, mono=True),
        'designed-with-km1.svg': badge('en', L),
        'designed-with-km1-dark.svg': badge('en', D),
        'km1-de-sekkei.svg': badge('ja', L),
        'km1-de-sekkei-dark.svg': badge('ja', D),
    }
    for name, svg in files.items():
        open(os.path.join(out, name), 'w').write(svg)
        for s in (1, 2, 3):
            png(svg, os.path.join(out, name[:-4] + ('' if s == 1 else f'@{s}x') + '.png'), s)
    print(f'{len(files)} 種を {out} に書き出した / wrote {len(files)} artworks (SVG + PNG @1x/2x/3x)')

if __name__ == '__main__':
    main()
