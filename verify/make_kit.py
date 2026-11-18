#!/usr/bin/env python3
"""KM1 の検証セット（Windows 実機用）を組み立てる / Assemble the KM1 verification kit for Windows
使い方 / Usage: python3 make_kit.py [出力フォルダ / out dir]（既定 verify/build/KM1_verify。同じ名前の zip も作る）
本体の今のファイルから組み立てるので、本体を直したら組み立て直すだけで版がそろう。
- flutter/: verify/flutter の検証アプリに、km1_theme.dart・km1_widgets.dart・icons/km1_icons*.dart・KM1Icons.ttf を入れる
- office/: dist/ の Word・PowerPoint のひな形と見本
- web/: 部品の見本（Alert・Button・Icon・Input・Table・Toast のライト）。gen/render_previews.py で作る（gen で npm i が要る）
Builds from the current repo files so the kit always matches KM1; rerun after changing KM1."""
import os, sys, shutil, subprocess, tempfile, zipfile
V = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(V)
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(V, 'build', 'KM1_verify'))
WEB = ['Alert', 'Button', 'Icon', 'Input', 'Table', 'Toast']
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
shutil.copy(os.path.join(V, 'verify.ps1'), OUT)
shutil.copy(os.path.join(V, 'README.md'), os.path.join(OUT, 'README.txt'))
shutil.copytree(os.path.join(V, 'flutter'), os.path.join(OUT, 'flutter'))
lib = os.path.join(OUT, 'flutter', 'lib'); os.makedirs(os.path.join(OUT, 'flutter', 'fonts'))
for src in ('km1_theme.dart', 'km1_widgets.dart', 'icons/km1_icons.dart', 'icons/km1_icons_b.dart'):
    shutil.copy(os.path.join(ROOT, src), lib)
shutil.copy(os.path.join(ROOT, 'icons', 'KM1Icons.ttf'), os.path.join(OUT, 'flutter', 'fonts'))
os.makedirs(os.path.join(OUT, 'office'))
for f in ('KM1_文書.dotx', 'KM1_文書見本.docx', 'KM1_スライド.potx', 'KM1_スライド見本.pptx'):
    shutil.copy(os.path.join(ROOT, 'dist', f), os.path.join(OUT, 'office'))
tmp = tempfile.mkdtemp(prefix='km1-kit-')
subprocess.run([sys.executable, os.path.join(ROOT, 'gen', 'render_previews.py'), tmp], check=True, stdout=subprocess.DEVNULL)
web = os.path.join(OUT, 'web'); os.makedirs(web)
for f in ('tokens.css', 'bundle.css', 'bundle.js', 'react.js', 'react-dom.js'): shutil.copy(os.path.join(tmp, f), web)
for n in WEB: shutil.copy(os.path.join(tmp, f'{n}-light.html'), web)
z = OUT + '.zip'
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    for base, _, files in os.walk(OUT):
        for f in sorted(files):
            p = os.path.join(base, f); zf.write(p, os.path.join(os.path.basename(OUT), os.path.relpath(p, OUT)))
print('kit', OUT, z)
