"""理由の確認（governance.md 7 章）の、機械で見られる部分 / Machine part of the reason review (Governance §7)

- FAIL: 浮いていない部品に外側の影（box-shadow）を付けている。浮く部品は ALLOW に理由つきで並べる
- FAIL: 見本（preview.html）の文言が、本物の内容ではなく部品自身や見本であることを説明している
- FAIL: 見本で削除のボタンを primary にしている（D26）
- FAIL: 見本の文言で、入力例をプレースホルダに入れている（D27）。数字と単位・助数詞の間があいていない（D27。ファイル名は除く）
- FAIL: 部品の README に「**理由 / Why:**」の行がない（全部品に書いた。-v で一覧）
使い方 / Usage: python3 gen/reasoncheck.py [-v]
"""
import glob, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
V = '-v' in sys.argv
res = []
def out(lv, code, msg): res.append((lv, code, msg))

# 浮いている（ほかの内容の上に重なる、または指で持ち上げている）ので影で高さを示してよいもの / parts that float
ALLOW = {
    '.f2-dialog': 'ダイアログは画面の上に重なる', '.f2-drawer': 'ドロワーは画面の上に重なる', '.f2-sheet': 'シートは画面の上に重なる',
    '.f2-psheet': '手元の操作シートは画面の上に重なる', '.f2-toast': 'トーストは内容の上に出る', '.f2-menu__list': 'メニューは内容の上に開く',
    '.f2-combo__list': '候補の一覧は内容の上に開く', '.f2-pop__panel': 'ポップオーバーは内容の上に開く', '.f2-tip__bubble': 'ツールチップは内容の上に出る',
    '.f2-sort__item--grabbed': '並べ替え中の行は指で持ち上げている', '.f2-slider__input::-webkit-slider-thumb': 'つまみは溝の上に乗っている',
    '.f2-igrid__check': '写真の上に重なるチェックを読めるようにする',
}
css = open(os.path.join(ROOT, 'components', 'bundle.css'), encoding='utf-8').read()
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
for sel, body in re.findall(r'([^{}]+)\{([^{}]*box-shadow:[^{}]*)\}', css):
    val = re.search(r'box-shadow:([^;}]*)', body).group(1).strip()
    if val.startswith('inset') or val == 'none': continue        # 内側の線は縁の代わり / inset lines act as borders
    for s1 in [x.strip() for x in sel.split(',')]:
        base = s1.split(':hover')[0].split(':focus')[0].strip()
        if base not in ALLOW: out('FAIL', 'SHADOW', f'{s1} に影（{val}）。浮いていない部品は縁で示す。浮くなら ALLOW に理由を書く / shadow on a non-floating part')

# 見本の文言 / preview copy
SELF = re.compile(r'クリックできる|操作対象です|ここに(?:本文|テキスト|説明)|サンプル(?:テキスト)?|ダミー|テキスト\s*[0-9０-９]|項目\s*[0-9０-９]|Lorem|placeholder text|Example (?:text|title)')
for f in sorted(glob.glob(os.path.join(ROOT, 'components', '*', 'preview.html'))):
    name = f.split(os.sep)[-2]
    if name.startswith('Compare'): continue      # M1 との比較カードは出典の説明が中身 / comparison cards describe their source
    t = re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
    for m in SELF.finditer(t):
        out('FAIL', 'COPY', f'{name} の見本の文言「{m.group(0)}」。本物の内容で書く（部品や見本を説明しない）/ self-describing preview copy')

# 入力例と数字の書き方（D27）/ examples in placeholders, digits next to Japanese
J = '[\u3040-\u30fa\u30fc-\u30ff\u4e00-\u9fff]'      # ・（U+30FB）は区切りなので除く / the middle dot is a separator
DIG = re.compile(rf"'[^'\n]*?(?:{J}\d|\d{J})[^'\n]*?'")
for f in sorted(glob.glob(os.path.join(ROOT, 'components', '*', 'preview.html'))):
    name = f.split(os.sep)[-2]
    t = re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
    for m in re.finditer(r"placeholder\s*[:=]\s*['\"]例", t):
        out('FAIL', 'EXAMPLE', f'{name}: 入力例をプレースホルダに入れている。hint に「例：」で書く / example in placeholder')
    for m in re.finditer(r"appearance\s*:\s*'primary'[^)]{0,80}?'[^']*削除[^']*'", t):
        out('FAIL', 'DANGER', f'{name}: 削除を primary にしている。取り消せない操作は danger（D26）/ delete as primary')
    for m in DIG.finditer(t):
        lit = m.group(0)
        if re.search(r'\.(?:csv|pdf|png|jpe?g|xlsx|docx)', lit): continue   # ファイル名はそのまま / file names
        out('FAIL', 'DIGIT', f'{name}: 数字と日本語の間に半角の空きがない {lit[:40]} / no space between number and counter')

# 理由の行 / the Why line
miss = []
for f in sorted(glob.glob(os.path.join(ROOT, 'components', '*', 'README.md'))):
    if '**理由 / Why:**' not in open(f, encoding='utf-8').read(): miss.append(f.split(os.sep)[-2])
total = len(glob.glob(os.path.join(ROOT, 'components', '*', 'README.md')))
if miss: out('FAIL', 'WHY', f'「理由 / Why」の行がない部品 {len(miss)} / {total}' + (': ' + '、'.join(miss) if V else '（-v で一覧）'))
else: out('PASS', 'WHY', f'全 {total} 部品に理由の行がある')

for lv, code, msg in res:
    if lv != 'PASS' or V: print(f'{lv:4} {code:7} {msg}')
nf = sum(1 for r in res if r[0] == 'FAIL'); nw = sum(1 for r in res if r[0] == 'WARN')
print(f'--- FAIL {nf} / WARN {nw}  （理由の確認のうち機械で見られる部分だけ。人の確認は governance.md 7 章）')
sys.exit(1 if nf else 0)
