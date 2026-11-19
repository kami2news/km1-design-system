#!/usr/bin/env python3
"""KM1 のグラフの模様（KM1-COL-001）を、Office で並べて使う画像にする / Build KM1 chart pattern tiles for Office
使い方 / Usage: python3 km1_patterns.py <出力フォルダ / out dir>

Office の既定の模様（pattFill の dkHorz など）は 8 × 8 画素の固定の細かい柄で、映すと色がにごって見えるだけになり、
大きさも変えられない。KM1 では、Web の模様（bundle.css の .f2-pat）と同じ形を、スライドで見分けられる大きさの
画像にして「図を並べて塗る」で使う。
Office preset patterns are fixed 8 × 8-pixel tiles that read as a muddy tint when projected. KM1 uses picture tiles
with the same shapes as the web patterns (.f2-pat), sized to be distinguishable on slides.

寸法（1pt ＝ KM1 の 1px、office.md §4.5）/ Sizes (1pt = 1 KM1 px):
  繰り返しの間隔 12pt（space-md）、線の太さ 4pt（space-xs）、格子と斜め格子の線 2pt、点の直径 6pt、市松の 1 マス 12pt
  repeat 12pt, stripe 4pt, grid lines 2pt, dot diameter 6pt, checker square 12pt
色は前景が系列の色、背景が白。画像は 4 倍の解像度（288dpi）で書き、Office では等倍（100%）で並べる。
"""
import os, sys
from PIL import Image, ImageDraw

P = 12            # 繰り返し（pt）/ repeat
SCALE = 4         # 1pt あたりの画素（288dpi）/ pixels per pt
DPI = 72 * SCALE
STRIPE, LINE, DOT = 4, 2, 6
ORDER = ['solid', 'horizontal', 'vertical', 'diagonal', 'grid', 'crosshatch', 'dots', 'checker']   # KM1-COL-001 の順
NAMES_JA = {'solid': '塗り', 'horizontal': '横線', 'vertical': '縦線', 'diagonal': '斜線', 'grid': '格子', 'crosshatch': '斜め格子', 'dots': '点', 'checker': '市松'}
# テーマのアクセントの順（office.md §2）/ theme accent order
ACCENTS = {'accent1': '10218B', 'accent2': '0F6CBD', 'accent3': '038387', 'accent4': 'BC4B09', 'accent5': '5C2E91', 'accent6': '107C10'}


def rgb(h): return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tile(pattern, color):
    """1 枚の模様の画像（つなぎ目が出ないように 3 × 3 に描いて真ん中を切る）/ one seamless tile"""
    n = 2 * P if pattern == 'checker' else P
    s = n * SCALE
    big = Image.new('RGB', (3 * s, 3 * s), (255, 255, 255))
    d = ImageDraw.Draw(big)
    c = rgb(color)
    u = SCALE
    if pattern == 'solid':
        d.rectangle([0, 0, 3 * s, 3 * s], fill=c)
    elif pattern == 'horizontal':
        for k in range(9):
            y = k * P * u
            d.rectangle([0, y, 3 * s, y + STRIPE * u - 1], fill=c)
    elif pattern == 'vertical':
        for k in range(9):
            x = k * P * u
            d.rectangle([x, 0, x + STRIPE * u - 1, 3 * s], fill=c)
    elif pattern in ('diagonal', 'crosshatch'):
        w = (STRIPE if pattern == 'diagonal' else LINE) * u * 1.41421   # 水平に測った幅 / horizontal width of a 45° band
        dirs = [1] if pattern == 'diagonal' else [1, -1]
        for sg in dirs:                                                  # 1: 右下がり（Web の 45deg と同じ向き）/ falling
            for k in range(-9, 18):
                x0 = k * P * u
                if sg == 1:
                    poly = [(x0, 0), (x0 + w, 0), (x0 + w + 3 * s, 3 * s), (x0 + 3 * s, 3 * s)]
                else:
                    poly = [(x0, 3 * s), (x0 + w, 3 * s), (x0 + w + 3 * s, 0), (x0 + 3 * s, 0)]
                d.polygon(poly, fill=c)
    elif pattern == 'grid':
        for k in range(9):
            v = k * P * u
            d.rectangle([0, v, 3 * s, v + LINE * u - 1], fill=c)
            d.rectangle([v, 0, v + LINE * u - 1, 3 * s], fill=c)
    elif pattern == 'dots':
        r = DOT * u / 2
        for i in range(9):
            for j in range(9):
                cx, cy = (i + 0.5) * P * u, (j + 0.5) * P * u
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    elif pattern == 'checker':
        for i in range(6):
            for j in range(6):
                if (i + j) % 2 == 0:
                    d.rectangle([i * P * u, j * P * u, (i + 1) * P * u - 1, (j + 1) * P * u - 1], fill=c)
    return big.crop((s, s, 2 * s, 2 * s))


def build(out):
    os.makedirs(out, exist_ok=True)
    files = []
    for an, col in ACCENTS.items():
        for i, p in enumerate(ORDER, 1):
            f = os.path.join(out, f'km1-pattern-{i}-{p}-{col}.png')
            tile(p, col).save(f, dpi=(DPI, DPI), optimize=True)
            files.append(f)
    return files


if __name__ == '__main__':
    fs = build(sys.argv[1] if len(sys.argv) > 1 else 'patterns')
    print('ok', len(fs), 'tiles')
