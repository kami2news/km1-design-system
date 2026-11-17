"""KM1 のアイコン一式を作り直す / Rebuild everything for KM1 icons
使い方 / Usage: python3 build_all.py <Fluent の svg-icons の icons フォルダ> <配布物の出力フォルダ>
1. 形（km1_icons.py）→ 2. Flutter のフォント（km1_font.py）→ 3. Web の bundle.js に埋め込む
→ 4. Office 用の素材集 → 5. KM1 のアプリアイコン → 6. 検査（iconcheck.py）→ 7. 配布用の zip
"""
import json, os, re, subprocess, sys, shutil, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
BUILD = os.path.join(HERE, 'build')
MIT = """MIT License

Copyright (c) 2020 Microsoft Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
NOTE = """KM1 のアイコン / KM1 icons (KM1-ICO-001)

- 通常（regular）も塗り（filled）も、すべて KM1 が B 案で描いたもの（KM1-ICO-001 §8）。
- km1-icons.json の fluent の欄だけ、導入前と比べるための Fluent System Icons（Microsoft、MIT。LICENSE-Fluent.txt）の形（20px）を残している。
- 名前: km1_<名前>_<大きさ>_<regular|filled>.svg
All regular and filled shapes are KM1 B drawings; only the "fluent" field in km1-icons.json keeps Fluent System Icons (MIT, LICENSE-Fluent.txt) at 20px for before/after comparison.
"""

def run(*a):
    print('$', ' '.join(a)); subprocess.run(a, check=True)

def embed_bundle():
    d = json.load(open(os.path.join(BUILD, 'km1-icons.json')))
    ki = '{' + ','.join(json.dumps(n) + ':[' + ','.join(json.dumps(e['paths'][f'{s}-{v}']) for s in (16, 20, 24) for v in ('regular', 'filled')) + ']' for n, e in d['icons'].items()) + '}'
    ja = '{' + ','.join(json.dumps(n) + ':' + json.dumps(e['ja']) for n, e in d['icons'].items()) + '}'
    kb = '{' + ','.join(json.dumps(n) + ':' + json.dumps(e['b'], separators=(',', ':')) for n, e in d['icons'].items() if 'b' in e) + '}'
    p = os.path.join(PROJ, 'components', 'bundle.js'); s = open(p).read()
    s = re.sub(r'^var KB=\{.*?\};', lambda m: 'var KB=' + kb + ';', s, count=1, flags=re.M)
    s = re.sub(r'^var KI=\{.*?\};$', lambda m: 'var KI=' + ki + ';', s, count=1, flags=re.M)
    s = re.sub(r'^var KI_JA=\{.*?\};$', lambda m: 'var KI_JA=' + ja + ';', s, count=1, flags=re.M)
    s = re.sub(r'^var KI_ALIAS=\{.*?\};$', lambda m: 'var KI_ALIAS=' + json.dumps(d.get('aliases', {})) + ';', s, count=1, flags=re.M)
    kf = '{' + ','.join(json.dumps(n) + ':' + json.dumps([e['fluent']['20-regular'], e['fluent']['20-filled']]) for n, e in d['icons'].items() if 'fluent' in e) + '}'
    s = re.sub(r'^var KF=\{.*?\};$', lambda m: 'var KF=' + kf + ';', s, count=1, flags=re.M)
    open(p, 'w').write(s); print('bundle.js: icons embedded')

def b_svg(n, e, size, ink='currentColor', t0='#F6F8FB', t1='#D3DCE7', title=True):
    """KM1 B 案の SVG（1 ファイルに 1 つなので ID は名前つきで衝突しない）/ standalone B-icon SVG"""
    b = e['b']; k = '16' if size <= 16 else '20' if size <= 20 else '24'; gid = f'km1-{n}-fill'
    out = f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 20 20" color="{ink}">'
    if title: out += f'<title>{e["ja"]} / {e["en"]}</title>'
    if b['tint']:
        out += f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{b["tintY"][0]}" x2="0" y2="{b["tintY"][1]}"><stop stop-color="{t0}"/><stop offset="1" stop-color="{t1}"/></linearGradient></defs>'
        out += f'<path fill="url(#{gid})" d="{b["tint"][k]}"/>'
    out += f'<path fill="currentColor" d="{b["ink"][k]}"/>'
    return out + '</svg>'

def write_b_svgs():
    d = json.load(open(os.path.join(BUILD, 'km1-icons.json')))
    sp = open(os.path.join(BUILD, 'sprite-20.svg')).read()
    for n, e in d['icons'].items():
        if 'b' in e:
            for s in (16, 20, 24):
                open(os.path.join(BUILD, 'svg', f'km1_{n}_{s}-regular.svg'), 'w').write(b_svg(n, e, s) + '\n')
            # スプライトの Regular も B 案に。色は CSS の変数から（なければライトの値）/ sprite symbols use CSS variables
            inner = re.sub(r'^<svg[^>]*>|</svg>$', '', b_svg(n, e, 20, t0='var(--icon-tint-start,#F6F8FB)', t1='var(--icon-tint-end,#D3DCE7)', title=False))
            inner = inner.replace('stop-color="var(', 'style="stop-color:var(').replace(')"/>', ')"/>')
            sp = re.sub(rf'<symbol id="km1-{n}-regular" viewBox="0 0 20 20">.*?</symbol>', lambda m: f'<symbol id="km1-{n}-regular" viewBox="0 0 20 20">{inner}</symbol>', sp, flags=re.S)
    open(os.path.join(BUILD, 'sprite-20.svg'), 'w').write(sp)

def office(out):
    d = json.load(open(os.path.join(BUILD, 'km1-icons.json')))
    root = os.path.join(out, 'KM1_icons_office'); shutil.rmtree(root, ignore_errors=True)
    for sub in ('svg', 'png'): os.makedirs(os.path.join(root, sub))
    for n, e in d['icons'].items():
        for s in (20, 24):
            for v in ('regular', 'filled'):
                if 'b' in e and v == 'regular':
                    svg = b_svg(n, e, s, ink='#657283')
                else:
                    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}"><title>{e["ja"]} / {e["en"]}</title><path fill="#242424" d="{e["paths"][f"{s}-{v}"]}"/></svg>'
                open(os.path.join(root, 'svg', f'km1_{n}_{s}_{v}.svg'), 'w').write(svg)
                if s == 20:
                    png = subprocess.run(['rsvg-convert', '-w', '256', '-h', '256'], input=svg.encode(), capture_output=True, check=True).stdout
                    open(os.path.join(root, 'png', f'km1_{n}_{v}_256.png'), 'wb').write(png)
    open(os.path.join(root, 'LICENSE-Fluent.txt'), 'w').write(MIT)
    open(os.path.join(root, 'README.txt'), 'w').write(NOTE + '\nPowerPoint・Word: 「挿入 › 画像」で SVG を入れ、「グラフィックの塗りつぶし」で色を変える（文字の色 #242424 が標準）。\nInsert SVG via Insert › Pictures; recolor with Graphics Fill (default #242424).\n')
    return root

def zipdir(src, dst):
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(src):
            for f in sorted(files):
                full = os.path.join(base, f); z.write(full, os.path.relpath(full, os.path.dirname(src)))
    print('zip', dst)

def main(fluent, out):
    os.makedirs(out, exist_ok=True)
    shutil.rmtree(os.path.join(BUILD, 'svg'), ignore_errors=True)   # 消えたアイコンの古い SVG を残さない / no stale SVGs
    run(sys.executable, os.path.join(HERE, 'km1_icons.py'), fluent, BUILD)
    run(sys.executable, os.path.join(HERE, 'km1_font.py'), os.path.join(BUILD, 'km1-icons.json'), BUILD)
    embed_bundle()
    write_b_svgs()
    run(sys.executable, os.path.join(HERE, 'km1_bdart.py'), os.path.join(BUILD, 'km1-icons.json'), BUILD)
    off = office(out)
    app = os.path.join(out, 'KM1_appicon'); shutil.rmtree(app, ignore_errors=True)
    run(sys.executable, os.path.join(HERE, 'km1_appicon.py'), app)
    run(sys.executable, os.path.join(HERE, 'iconcheck.py'), os.path.join(BUILD, 'km1-icons.json'), os.path.join(BUILD, 'KM1Icons.ttf'))
    # 配布用 / distribution
    web = os.path.join(out, 'KM1_icons'); shutil.rmtree(web, ignore_errors=True); os.makedirs(web)
    shutil.copytree(os.path.join(BUILD, 'svg'), os.path.join(web, 'svg'))
    for f in ('km1-icons.json', 'sprite-20.svg', 'KM1Icons.ttf', 'km1_icons.dart', 'km1_icons_b.dart'): shutil.copy(os.path.join(BUILD, f), web)
    open(os.path.join(web, 'LICENSE-Fluent.txt'), 'w').write(MIT); open(os.path.join(web, 'README.txt'), 'w').write(NOTE)
    # 配布は 1 つの zip にまとめる / ship everything as one zip
    bundle = os.path.join(out, 'KM1_icons_pack'); shutil.rmtree(bundle, ignore_errors=True); os.makedirs(bundle)
    shutil.copytree(web, os.path.join(bundle, 'icons'))          # SVG・JSON・スプライト・Flutter
    shutil.copytree(off, os.path.join(bundle, 'office'))         # PowerPoint・Word 用
    shutil.copytree(app, os.path.join(bundle, 'appicon'))        # アプリアイコン・ファビコン
    for sub in ('icons', 'office'):
        for f in ('LICENSE-Fluent.txt', 'README.txt'):
            q = os.path.join(bundle, sub, f)
            if os.path.exists(q): os.remove(q)
    open(os.path.join(bundle, 'LICENSE-Fluent.txt'), 'w').write(MIT)
    open(os.path.join(bundle, 'README.txt'), 'w').write(NOTE + """
中身 / Contents
- icons/    SVG（16・20・24px の Regular と Filled）、km1-icons.json、sprite-20.svg、Flutter 用の KM1Icons.ttf・km1_icons.dart・km1_icons_b.dart
          （Flutter に組み込むときは KM1 本体の km1_theme.dart（同じ版）も同じフォルダに置く。km1_widgets.dart は要らない）
          (Flutter also needs km1_theme.dart from the same KM1 version; km1_widgets.dart is not required)
- office/   PowerPoint・Word 用の SVG（20・24px）と PNG（256px）。「挿入 › 画像」で入れ、「グラフィックの塗りつぶし」で色を変える
- appicon/  KM1 のアプリアイコンとファビコン（web・android・ios・windows、flutter_launcher_icons.yaml）
""")
    for old_zip in ('KM1_icons.zip', 'KM1_icons_office.zip', 'KM1_appicon.zip'):
        q = os.path.join(out, old_zip)
        if os.path.exists(q): os.remove(q)
    with zipfile.ZipFile(os.path.join(out, 'KM1_icons.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(bundle):
            for f in sorted(files):
                full = os.path.join(base, f); z.write(full, os.path.join('KM1_icons', os.path.relpath(full, bundle)))
    print('zip', os.path.join(out, 'KM1_icons.zip'))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
