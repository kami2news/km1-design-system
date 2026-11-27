#!/usr/bin/env python3
"""KM1 トークンの照合と影響範囲 / KM1 token check and impact map (KM1-TOK-001)

1. spacingRole・platformTarget の各トークンの value が ref の値と同じか確かめる（違えば直す: --fix）。
   Checks every alias's value equals its ref (fixes with --fix).
2. 基本トークン → 用途トークン → 使っている CSS の場所 / 部品 の対応表を作る（--md で Markdown）。
   Builds the primitive → role → usage map (--md prints Markdown).
"""
import json,re,sys
import os as _os
_H=_os.path.dirname(_os.path.abspath(__file__))
P=_os.environ.get('KM1_PROJECT') or (_os.path.join(_H,'..','project') if _os.path.exists(_os.path.join(_H,'..','project','tokens.json')) else _os.path.join(_H,'..'))
P=_os.path.normpath(P)+'/'
t=json.load(open(P+'tokens.json'))
base={}
for fam in ('spacing','size','radius'):
    for x in t[fam]['tokens']: base[x['name']]=x['value']
bad=[]
for fam in ('spacingRole','platformTarget'):
    for x in t[fam]['tokens']:
        want=base.get(x['ref'])
        if want is None: bad.append((x['name'],'ref なし / missing ref '+x['ref']))
        elif x['value']!=want:
            bad.append((x['name'],f"{x['value']} ≠ {x['ref']}={want}"))
            if '--fix' in sys.argv: x['value']=want
if '--fix' in sys.argv and bad: json.dump(t,open(P+'tokens.json','w'),ensure_ascii=False,indent=2)
css=re.sub(r'/\*.*?\*/','',open(P+'components/bundle.css').read(),flags=re.S)
js=open(P+'components/bundle.js').read()
def users(var):
    sels=set()
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',css):
        if f'var(--{var}' in m.group(2): sels.add(m.group(1).strip()[:60])
    return sorted(sels)
roles=t['spacingRole']['tokens']
rows=[]
for x in roles:
    direct=users(x['name'])
    via=[]
    for m in re.finditer(r'--(km1-density-[a-z-]+):var\(--([a-z0-9-]+)',css):
        if m.group(2)==x['name']:
            dv=m.group(1); via.append(f'{dv} → '+', '.join(users(dv)))
    via=sorted(set(via))
    rows.append((x['ref'],x['name'],x['value'],direct,via))
if '--md' in sys.argv or '--write-doc' in sys.argv:
    import io
    buf=io.StringIO()
    _print=print
    def print(*a,**k): _print(*a,file=buf,**k)
    print('| 基本トークン / Primitive | 用途トークン / Role token | 値 | 状態 / Status | 使っている場所 / Used by |')
    print('|---|---|---|---|---|')
    for ref,n,v,d,via in rows:
        u='; '.join(via) if via else ('`'+'`, `'.join(d)+'`' if d else '画面の規則（「画面の組み立て」）で使う。部品のコードではまだ使っていない / page rules only')
        st='適用済 / applied' if (via or d) else '定義済 / defined'
        print(f'| `{ref}` | `{n}` | {v} | {st} | {u} |')
    print()
    print('| 基本トークンを変えると / If you change | 変わる用途トークン / Role tokens that follow |')
    print('|---|---|')
    by={}
    for ref,n,v,d,via in rows: by.setdefault(ref,[]).append(n)
    for ref,ns in by.items(): print(f'| `{ref}` | '+'、'.join(f'`{n}`' for n in ns)+' |')
    print=_print
    out=buf.getvalue()
    if '--write-doc' in sys.argv:
        d=open(P+'tokens.md').read()
        a=d.index('`python3 gen/tokens_check.py --md`'); a=d.index('\n\n',a)+2; b=d.index('\n## 5. ',a)+1
        open(P+'tokens.md','w').write(d[:a]+out+'\n'+d[b:])
    else: print(out)
else:
    print('mismatch' if bad else 'all aliases match', bad)
    for r in rows: print(r[0],'->',r[1],r[2],r[3][:3],r[4])
sys.exit(1 if bad and '--fix' not in sys.argv else 0)
