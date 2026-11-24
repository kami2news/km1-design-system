"""部品の寸法を KM1 の定義と照らす / Check rendered component sizes against KM1 definitions.
見本（render_previews.py で作る）を PC（1000px、マウス）とスマホ（390px、タッチ）で開き、押せる部品の高さ・文字の大きさと行の高さ・角丸・アイコンの大きさを測る。
定義（tokens.json と tokens.md「部品の寸法」）にない値が出たら FAIL。決まった例外は EXC に理由つきで書く。
使い方 / Usage: gen で npm i をしてから python3 sizecheck.py（Chrome が要る。CHROME で場所を指定できる）
Run `npm i` in gen/ first; needs Chrome (set CHROME to override the path)."""
import json,subprocess,sys,os,tempfile
G=os.path.dirname(os.path.abspath(__file__))
WORK=tempfile.mkdtemp(prefix='km1-size-'); RC=os.path.join(WORK,'rc')
subprocess.run([sys.executable,os.path.join(G,'render_previews.py'),RC],check=True)
T=json.load(open(os.path.join(G,'..','tokens.json')))
px=lambda v:str(v)
FS=set();LH={'normal','16px'}  # 16px: 高さの決まった箱の中の 12px の 1 行（バッジ・小ボタン・目盛り。tokens.md 5 章）/ one 12px line in a fixed-height box
for g in T['type']['groups']:
  for st in g['styles']: FS.add(st['fontSize']);LH.add(st['lineHeight'])
RAD={t['value'] if isinstance(t,dict) else t for t in []}
RAD={x['value'] for x in T['radius']['tokens']}|{'50%'}
RAD.discard('0')
IC={f"{v}x{v}" for v in (12,16,20,24,32,48)}
HPC={'24','32','40'}; MIN_TOUCH=44
# 決まった例外（理由つき）/ Documented exceptions
EXC={
 ('ImageGrid','button.f2-igrid__open'):'写真のタイルは列幅で決まる / tile size follows the column width',
 ('TimeGrid','button.f2-tg__ev'):'予定の枠の高さは時間の長さ（TimeGrid README）/ block height is the duration',
 ('Nav','button.f2-nav__item'):'下のナビの項目は 56px（tokens.md 部品の寸法）/ bottom-nav item is 56px',
 ('FileUpload','input.f2-sr'):'見えない input（label が押す範囲）/ visually hidden input',
 ('TagPicker','input.f2-tags__input'):'入力欄の内側の入力。欄の高さが定義どおり / inner input; the field itself has the defined height',
 ('Timetable','button.f2-tt__item'):'時間割のマスは 2 行（科目と教室）で 48px（tokens.md 部品の寸法）/ two-line cell, 48px',
 ('Chip','button.f2-chip'):'タッチでは ::after で上下 6px 広げ 44px（tokens.md）/ ::after extends the target to 44px on touch',
}
LIST2={'52'}  # 2 行の一覧の行 / two-line list row
def run(mode):
  o=os.path.join(WORK,mode+'.json')
  subprocess.run(['timeout','300','node',os.path.join(G,'sizeprobe.js'),mode,RC,o],check=True,env=dict(os.environ,NODE_PATH=os.path.join(G,'node_modules')))
  return json.load(open(o))
def exc(c,v):
  return all((c,s.split(' ×')[0]) in EXC for s in v.split(',')) or all(any((c2,x) in EXC for c2 in [c]) for x in v.split(' ×')[0].split(','))
fails=[]
pc=run('pc')
for c,r in sorted(pc.items()):
  for k,v in r['h'].items():
    if k in HPC: continue
    if k in LIST2 and 'f2-li__primary' in v: continue
    if exc(c,v): continue
    fails.append(f'{c}: 高さ {k}px / height ({v})')
  for k,v in r['fs'].items():
    a,b=k.split('/')
    if a not in FS or b not in LH: fails.append(f'{c}: 文字 {k} / type ({v})')
  for k,v in r['rad'].items():
    if k not in RAD: fails.append(f'{c}: 角丸 {k} / radius ({v})')
  for k,v in r['ic'].items():
    if k not in IC: fails.append(f'{c}: アイコン {k} / icon ({v})')
tc=run('touch')
for c,r in sorted(tc.items()):
  for k,v in r['h'].items():
    if int(k)<MIN_TOUCH and not exc(c,v): fails.append(f'{c}: タッチで {k}px（44 未満）/ below 44 on touch ({v})')
for f in fails: print('FAIL',f)
print(f'--- 寸法 FAIL {len(fails)}（見本 {len(pc)} 件、PC とタッチ）/ size check')
sys.exit(1 if fails else 0)
