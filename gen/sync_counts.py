#!/usr/bin/env python3
"""部品の数を一か所から数え、文書のすべての記述をそろえる / Count components from one source and sync every mention.

数える元 / Sources:
- Web: components/bundle.js の 1 行目（@ds-bundle の components）＝見本のある部品。
  ほかに window.Fluent2 が公開している大文字始まりの部品（FormActions・ListItem など）とフック（use*）。
- Flutter: km1_widgets.dart の冒頭の「部品 / Widgets」の一覧。
結果を project/inventory.json に書き、README・platforms・PDF の表紙の数を書き換える。--check は書き換えずに食い違いを報告し、あれば終了コード 1。
coverage.md の部品名の一覧が数えた名前とずれていないか、どこかに古い部品数が残っていないかも見る。
"""
import json,re,sys,subprocess
import os as _os
_H=_os.path.dirname(_os.path.abspath(__file__))
P=_os.environ.get('KM1_PROJECT') or (_os.path.join(_H,'..','project') if _os.path.exists(_os.path.join(_H,'..','project','tokens.json')) else _os.path.join(_H,'..'))
P=_os.path.normpath(P)+'/'
js=open(P+'components/bundle.js').read()
cards=[c['name'] for c in json.loads(re.match(r'/\* @ds-bundle: (\{.*?\}) \*/',js).group(1))['components']]
keys=json.loads(subprocess.run(['node','-e',"global.window={React:require('"+(_os.environ.get('REACT_PATH') or 'react')+"')};global.React=window.React;require('"+P+"components/bundle.js');console.log(JSON.stringify(Object.keys(window.Fluent2)))"],capture_output=True,text=True).stdout)
comps=sorted(k for k in keys if k[0].isupper()); hooks=sorted(k for k in keys if k.startswith('use'))
dart=open(P+'km1_widgets.dart').read()
head=dart.split('// 部品 / Widgets:')[1].split('\n//\n')[0]
fl=[w.strip() for w in re.sub(r'//','',head).replace('\n',' ').split(',') if w.strip()]
# 見出しの一覧と、ファイルの中の公開している部品が一致するか / the header list must match the public widgets in the file
_pub=set(re.findall(r'^class (Km1\w+)(?:<\w+>)? extends (?:StatelessWidget|StatefulWidget)',dart,re.M))|set(re.findall(r'^Future<[^>]*> (showKm1\w+)',dart,re.M))
_hdr_bad=sorted(set(fl)^_pub)
inv={'web':{'cards':len(cards),'components':len(comps),'hooks':hooks,'cardNames':cards,'componentNames':comps},'flutter':{'widgets':len(fl),'names':fl}}
W,C,F=len(cards),len(comps),len(fl)
_IJ=json.load(open(P+'icons/build/km1-icons.json'))['icons']
IN=len(_IJ); IT=sum(1 for e in _IJ.values() if (e.get('b') or {}).get('tint'))
rules=[('README.md',r'KM1 専用の \d+ 部品',f'KM1 専用の {F} 部品',2),
 ('README.md',r'plus `km1_widgets\.dart` \(\d+ KM1 widgets\)',f'plus `km1_widgets.dart` ({F} KM1 widgets)',1),
 ('coverage.md',r'見本のある部品 \d+（公開 \d+）',f'見本のある部品 {W}（公開 {C}）',1),
 ('coverage.md',r'KM1 専用の \d+ 部品',f'KM1 専用の {F} 部品',1),
 ('coverage.md',r'Web: \d+ with previews, \d+ exported; Flutter: \d+ KM1 widgets',f'Web: {W} with previews, {C} exported; Flutter: {F} KM1 widgets',1),
 ('README.md',r'^(?:\d+ 個と|見本のある部品 \d+ 個（公開している部品は全部で \d+ 個）と)、[^\n]*?を `window\.Fluent2` に収録。',f'見本のある部品 {W} 個（公開している部品は全部で {C} 個）と、フォームの状態をまとめる `useForm`、選択の状態をまとめる `useSelection` を `window.Fluent2` に収録。',1),
 ('README.md',r'\*(?:Fifty|Forty|\d+ components)[^*]*?live in `window\.Fluent2`',f'*{W} components with previews ({C} exported in total) plus the `useForm` and `useSelection` hooks live in `window.Fluent2`',1),
 ('platforms.md',r'\| (?:見本のある部品 \d+（公開 \d+）|\d+ 部品)。自動検査',f'| 見本のある部品 {W}（公開 {C}）。自動検査',1),
 ('platforms.md',r'KM1 専用の \d+ 部品',f'KM1 専用の {F} 部品',1),
 ('../gen/pdf.py',r'Web \d+・Flutter 専用 \d+',f'Web {W}・Flutter 専用 {F}',1),
 # アイコンの数（km1-icons.json から）/ icon counts from km1-icons.json
 ('icons.md',r'全部のアイコンを KM1 B 案で描く（\d+ 個）',f'全部のアイコンを KM1 B 案で描く（{IN} 個）',1),
 ('icons.md',r'\*Every icon \(\d+\)',f'*Every icon ({IN})',1),
 ('icons.md',r'^全部で \d+ 個。',f'全部で {IN} 個。',1),
 ('icons.md',r'\*\d+ icons, all B',f'*{IN} icons, all B',1),
 ('icons.md',r'淡い面があるのは \d+ 個',f'淡い面があるのは {IT} 個',1),
 ('icons.md',r'; \d+ with the soft tint',f'; {IT} with the soft tint',1),
 ('icons.md',r'（いま \d+ 個: 予定の仲間',f'（いま {IT} 個: 予定の仲間',1),
 ('components/IconTrial/README.md',r'（いま \d+ 個。一覧',f'（いま {IT} 個。一覧',1),
 ('components/IconTrial/README.md',r'\(\d+ icons; see the tint column',f'({IT} icons; see the tint column',1),
 ('README.md',r'Fluent System Icons、Microsoft、MIT。\d+ 個）',f'Fluent System Icons、Microsoft、MIT。{IN} 個）',1),
 ('README.md',r'Microsoft, MIT; \d+ icons\)',f'Microsoft, MIT; {IN} icons)',1)]
bad=[]
if _hdr_bad: bad.append(f'km1_widgets.dart の見出しの部品一覧とファイルの中身が違う / header list differs: {_hdr_bad}')
for f,pat,rep,n in rules:
    if not _os.path.exists(P+f): continue  # 公開しないファイル（gen/pdf.py）は飛ばす / skip files intentionally not published
    s=open(P+f).read(); found=re.findall(pat,s,flags=re.M)
    if len(found)!=n: bad.append(f'{f}: {pat} が {len(found)} か所（{n} か所のはず）')
    stale=[x for x in found if x!=rep]
    if stale and '--check' in sys.argv: bad.append(f'{f}: 古い数 {stale}')
    if '--check' not in sys.argv: open(P+f,'w').write(re.sub(pat,lambda m:rep,s,flags=re.M))
# coverage.md の部品名の一覧が数えた名前とずれていないか / names listed in coverage.md must match the counted names
_cov=open(P+'coverage.md').read()
_miss=[n for n in comps+fl if '`'+n+'`' not in _cov]
if _miss: bad.append(f'coverage.md に載っていない部品 / missing from coverage.md: {_miss}')
# 古い部品数が残っていないか（*.md と部品の README）/ stray widget counts in docs
import glob as _g
for _f in sorted(_g.glob(P+'*.md'))+sorted(_g.glob(P+'components/*/README.md')):
    if _os.path.basename(_f)=='changelog.md': continue  # 変更履歴は当時の数を残す / history keeps past counts
    for _m in re.finditer(r'KM1 専用の (\d+) 部品|(\d+) KM1 widgets',open(_f).read()):
        _n=int(_m.group(1) or _m.group(2))
        if _n!=F: bad.append(f'{_os.path.relpath(_f,P)}: 古い Flutter 部品数 {_n}（{F} のはず）')
if '--check' not in sys.argv: json.dump(inv,open(P+'inventory.json','w'),ensure_ascii=False,indent=2)
print(f'Web 見本 {W}・公開 {C}・フック {len(hooks)}・Flutter {F}'); [print('NG',b) for b in bad]
sys.exit(1 if bad else 0)
