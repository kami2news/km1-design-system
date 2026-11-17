"""KM1 のアプリアイコン・ファビコンを作る / Build app icons and favicons (KM1-ICO-001 §6)

1 枚の絵（正方形・全面の塗り＋中央の絵柄）から、各 OS の大きさを全部書き出す。
From one artwork (full-bleed square + centred motif) it writes every size each platform needs.

使い方 / Usage:
  python3 km1_appicon.py <出力フォルダ> [--bg 10218B] [--fg FFFFFF]
                         [--mark km1 | --icon <KM1 のアイコン名> --icons km1-icons.json] [--name KM1]
  例 / e.g.  python3 km1_appicon.py out/km1                       # KM1 そのもの
            python3 km1_appicon.py out/schedule --bg 038387 --icon timetable --icons build/km1-icons.json --name 予定
必要なもの / Needs: fonttools, Pillow, rsvg-convert（librsvg）
"""
import argparse, os, subprocess, json, io
from fontTools.ttLib import TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image

FONT = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'   # SIL OFL 1.1。字形を輪郭にして使う / outlines only

def wordmark(text):
    """文字を輪郭のパスにする。返す値は (d, 幅, 高さ)。原点は左上 / text → outline path"""
    tt = TTCollection(FONT).fonts[0]
    gs = tt.getGlyphSet(); cmap = tt.getBestCmap(); upm = tt['head'].unitsPerEm
    pen = SVGPathPen(gs); x = 0; asc = 0.74 * upm   # 大文字と数字の高さの上端 / cap height top
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (1, 0, 0, -1, x, asc)))
        x += gs[g].width - (0.02 * upm if ch != text[-1] else 0)
    return pen.getCommands(), x, asc

def artwork(size, bg, fg, motif, small=False):
    """正方形の SVG。絵柄は直径 60% の円に収める（Android の安全な円 66/108＝61%、PWA の maskable 80% の両方に入る）。
    小さいファビコン（48px 以下）は角を丸めて書き出すので、絵柄を幅 80% まで広げる。
    Motif fits a circle of 60% diameter (inside Android's 61% and PWA's 80% safe circles); small favicons widen it to 80%."""
    import math
    body = ''
    if motif[0] == 'text':
        d, w, h = motif[1]
        bar = 0 if small else 3.2 * (0.30 * w * 6 / 22)          # 帯と間の高さ / bar + gap height (in text units)
        H = h + bar
        k = (size * 0.80 / w) if small else size * min(0.56 / w, 0.58 / math.hypot(w, H))
        tw, th = w * k, h * k
        x0 = (size - tw) / 2
        y0 = (size - H * k) / 2 + bar * k                           # 帯と文字のまとまりを中央に / centre bar + text together
        body += f'<path transform="translate({x0:.2f} {y0:.2f}) scale({k:.5f})" d="{d}" fill="#{fg}"/>'
        if not small:   # 表紙のしるし（22:6 の帯）を文字の上に / the cover bar above the wordmark
            bw, bh = tw * 0.30, tw * 0.30 * 6 / 22
            body += f'<rect x="{x0:.2f}" y="{y0 - bh * 3.2:.2f}" width="{bw:.2f}" height="{bh:.2f}" fill="#{fg}"/>'
    else:
        d = motif[1]
        box = size * (0.80 if small else 0.53)   # アイコンの絵は 20 の格子の 2〜18。対角線が 60% に収まる / live area diagonal ≤ 60%
        k = box / 20
        body += f'<path transform="translate({(size - box) / 2:.2f} {(size - box) / 2:.2f}) scale({k:.5f})" d="{d}" fill="#{fg}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}"><rect width="{size}" height="{size}" fill="#{bg}"/>{body}</svg>'

def rounded(svg, size, r):
    """ファビコンなど OS が角を丸めない場所用に、角を丸めた版 / rounded version where the OS does not mask"""
    return svg.replace(f'<rect width="{size}" height="{size}"', f'<rect width="{size}" height="{size}" rx="{size * r:.2f}"', 1)

def png(svg, path, size, alpha=True):
    out = subprocess.run(['rsvg-convert', '-w', str(size), '-h', str(size)], input=svg.encode(), capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(out)).convert('RGBA')
    if not alpha:
        bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[3]); im = bg
    im.save(path); return im

def main():
    a = argparse.ArgumentParser()
    a.add_argument('out'); a.add_argument('--bg', default='10218B'); a.add_argument('--fg', default='FFFFFF')
    a.add_argument('--mark', default='km1'); a.add_argument('--icon'); a.add_argument('--icons'); a.add_argument('--name', default='KM1')
    o = a.parse_args()
    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    l1, l2 = sorted((lum(o.bg), lum(o.fg)), reverse=True); ratio = (l1 + 0.05) / (l2 + 0.05)
    if ratio < 3: raise SystemExit(f'絵柄と背景のコントラストが {ratio:.2f}:1。3:1 以上にする / contrast {ratio:.2f}:1 is below 3:1')
    print(f'contrast {ratio:.2f}:1')
    for sub in ('', 'web', 'android', 'ios', 'windows'): os.makedirs(os.path.join(o.out, sub), exist_ok=True)
    if o.icon:
        motif = ('icon', json.load(open(o.icons))['icons'][o.icon]['paths']['20-filled'])
    else:
        motif = ('text', wordmark('KM1' if o.mark == 'km1' else o.mark))
    big = lambda s: artwork(s, o.bg, o.fg, motif)
    small = lambda s: artwork(s, o.bg, o.fg, motif, small=True)
    W = lambda *p: os.path.join(o.out, *p)
    # 元の絵 / master artwork
    open(W('icon-master.svg'), 'w').write(big(1024))
    # Web: ファビコンは角を丸める（ブラウザは丸めない）/ favicons are pre-rounded
    open(W('web', 'favicon.svg'), 'w').write(rounded(small(32), 32, 0.2))
    ims = [png(rounded(small(s), s, 0.2), W('web', f'favicon-{s}.png'), s) for s in (16, 32, 48)]
    ims[2].save(W('web', 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
    png(big(180), W('web', 'apple-touch-icon.png'), 180, alpha=False)
    png(rounded(big(192), 192, 0.2), W('web', 'icon-192.png'), 192)
    png(rounded(big(512), 512, 0.2), W('web', 'icon-512.png'), 512)
    png(big(512), W('web', 'icon-maskable-512.png'), 512, alpha=False)
    # Android: アダプティブアイコン（108dp、表 432px）/ adaptive icon layers at 432px
    fg_only = big(432).replace(f'<rect width="432" height="432" fill="#{o.bg}"/>', '')
    png(fg_only, W('android', 'ic_launcher_foreground.png'), 432)
    png(f'<svg xmlns="http://www.w3.org/2000/svg" width="432" height="432"><rect width="432" height="432" fill="#{o.bg}"/></svg>', W('android', 'ic_launcher_background.png'), 432)
    png(fg_only.replace(f'fill="#{o.fg}"', 'fill="#000000"'), W('android', 'ic_launcher_monochrome.png'), 432)
    png(big(512), W('android', 'play-store-512.png'), 512, alpha=False)
    # iOS・macOS: 1024px、透明なし、角は OS が丸める / 1024px, no alpha, OS masks corners
    png(big(1024), W('ios', 'AppIcon-1024.png'), 1024, alpha=False)
    # Windows
    for s in (44, 150, 310): png(big(s), W('windows', f'Square{s}x{s}Logo.png'), s, alpha=False)
    # 設定の例 / config snippets
    open(W('web', 'manifest-icons.json'), 'w').write(json.dumps({'name': o.name, 'theme_color': '#' + o.bg, 'background_color': '#' + o.bg, 'icons': [
        {'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
        {'src': 'icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]}, ensure_ascii=False, indent=2))
    open(W('web', 'head.html'), 'w').write('<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<link rel="manifest" href="/manifest.webmanifest">\n')
    open(W('flutter_launcher_icons.yaml'), 'w').write(f'''# flutter_launcher_icons の設定 / config for flutter_launcher_icons
flutter_launcher_icons:
  image_path: "{o.out}/ios/AppIcon-1024.png"
  android: true
  ios: true
  remove_alpha_ios: true
  adaptive_icon_background: "#{o.bg}"
  adaptive_icon_foreground: "{o.out}/android/ic_launcher_foreground.png"
  adaptive_icon_monochrome: "{o.out}/android/ic_launcher_monochrome.png"
  web:
    generate: true
    image_path: "{o.out}/web/icon-512.png"
    background_color: "#{o.bg}"
    theme_color: "#{o.bg}"
  windows:
    generate: true
    image_path: "{o.out}/ios/AppIcon-1024.png"
''')
    print('done', o.out)

if __name__ == '__main__':
    main()
