import json,re
import os as _os
_H=_os.path.dirname(_os.path.abspath(__file__))
P=_os.environ.get('KM1_PROJECT') or (_os.path.join(_H,'..','project') if _os.path.exists(_os.path.join(_H,'..','project','tokens.json')) else _os.path.join(_H,'..'))
P=_os.path.normpath(P)+'/'
t=json.load(open(P+'tokens.json'))
def val(v,theme):
    v=v if isinstance(v,str) else v.get(theme,v['light'])
    m=re.fullmatch(r'\{(.+)\}',v)
    return f'var(--{m.group(1)})' if m else v
def colors(theme,indent='  '):
    return ''.join(f'{indent}--{x["name"]}:{val(x["value"],theme)};\n' for x in t['color']['tokens'])
o='/* KM1 tokens.css — tokens.json から自動生成。直接編集しない。 / Generated from tokens.json; do not edit by hand.\n'
o+=' 使い方 / Usage: <html lang="ja"> に読み込む。ダークは <html data-theme="dark">、固定しないときは OS の設定に従う。\n'
o+=' 部品のクラス（.f2-btn など）は components/bundle.css を併用する。 / Pair with components/bundle.css for component classes. */\n'
o+=':root{\n'+colors('light')
for fam in('spacing','radius','size','layer','opacity'):
    o+=''.join(f'  --{x["name"]}:{x["value"]};\n' for x in t[fam]['tokens'])
o+=''.join(f'  --{x["name"]}:{x["value"]};\n' for x in t['shadow']['tokens'])
# 用途別エイリアスと OS 別の操作領域は、基本トークンへの参照のまま出す / role aliases stay references
for fam in ('spacingRole','platformTarget'):
    o+=''.join(f'  --{x["name"]}:var(--{x["ref"]});\n' for x in t[fam]['tokens'])
o+=''.join(f'  --font-{k}:{v};\n' for k,v in t['type']['families'].items())
o+='}\n'
o+=':root:lang(en){--font-sans:var(--font-sans-en)}\n'
o+='[data-theme="dark"]{\n'+colors('dark')+'}\n'
o+='@media (prefers-color-scheme:dark){\n:root:not([data-theme="light"]){\n'+colors('dark')+'}\n}\n'
for g in t['type']['groups']:
    for s in g['styles']:
        o+=f'.f2-text-{s["name"]}{{font:{s["fontWeight"]} {s["fontSize"]}/{s["lineHeight"]} var(--font-sans)}}\n'
open(P+'tokens.css','w').write(o)
print(len(o),o.count('--'))
