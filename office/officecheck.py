"""KM1 の Word・PowerPoint の検査 / Check Word and PowerPoint files against KM1-DOC-002/003.
使い方 / Usage: python3 officecheck.py file.docx|file.pptx|.dotx|.potx ...
FAIL があると終了コード 1。機械で確かめられる項目だけで、人の確認（office.md §6）は別に要る。
Exits 1 on any FAIL. Machine checks only; the human checks in office.md §6 are still needed."""
import sys,zipfile,re
from lxml import etree
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main',
 'p':'http://schemas.openxmlformats.org/presentationml/2006/main','wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
 'dc':'http://purl.org/dc/elements/1.1/','cp':'http://schemas.openxmlformats.org/package/2006/metadata/core-properties','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
# KM1 の色（ライトテーマ）だけ / KM1 light-theme colors only
PALETTE={'242424','424242','616161','10218B','FFFFFF','F5F5F5','F0F0F0','ECEFFC','E0E0E0','D1D1D1','0F6CBD','038387','BC4B09','5C2E91','107C10','B10E1C','EBF3FC','FDF3F4','F1FAF1','FFF9F5','000000','AUTO'}
WORD_SIZES={8,8.5,9,10,11,13,20,28}          # documents.md の表と同じ / same as the PDF rules
SLIDE_SIZES={14,20,24,32,40,68}               # KM1 の型の表（office.md §4.1）/ KM1 type ramp
# スライドの割り付け（office.md §4.2）。単位は pt / slide grid in pt
EMU=12700; SIDE=48; TOP=40; GUT=24; COL=50; BODY_TOP=104; BODY_BOTTOM=472; FOOT_TOP=496; CONTENT_W=864
GRID_X={SIDE+i*(COL+GUT) for i in range(12)}; GRID_R={SIDE+i*(COL+GUT)+COL for i in range(12)}
TITLE_EM=CONTENT_W/32                          # 32pt の題名が 1 行に入る全角の字数（27）/ full-width chars per title line
FONT='游ゴシック'
res=[]
def out(level,code,msg): res.append((level,code,msg))
def x(z,n):
    try: return etree.fromstring(z.read(n))
    except KeyError: return None
def core(z,fname):
    c=x(z,'docProps/core.xml')
    t=c.findtext('dc:title',namespaces=NS) if c is not None else None
    if not t or not t.strip() or t.strip().lower() in ('untitled','無題') or t.strip()==fname: out('FAIL','TITLE','文書の題名がない / no document title')
    else: out('PASS','TITLE',t)
    a=c.findtext('dc:creator',namespaces=NS) if c is not None else ''
    lm=c.findtext('cp:lastModifiedBy',namespaces=NS) if c is not None else ''
    if (a or '').strip() or (lm or '').strip(): out('WARN','AUTHOR',f'作成者が入っている（外に出すなら消す）/ author set: {a or lm}')
NOTSANS=re.compile(r'明|Mincho|Times|Georgia|Garamond|Century|Cambria|Courier|Book Antiqua|Palatino|Angsana|Sylfaen|Plantagenet|MV Boli|Script|Comic|行書|草書|楷書|教科書|ポップ',re.I)
def theme(z):
    for n in z.namelist():
        if re.search(r'theme/theme\d*\.xml$',n):
            t=etree.fromstring(z.read(n))
            for k in ('majorFont','minorFont'):
                f=t.find(f'.//a:{k}',NS)
                if f is None: continue
                ea=f.find('a:ea',NS)
                if ea is None or ea.get('typeface')!=FONT: out('FAIL','THEMEFONT',f'{k} の和文書体が {FONT} でない / East Asian theme font is not {FONT}')
                la=f.find('a:latin',NS)
                if la is None or la.get('typeface')!=FONT: out('FAIL','THEMEFONT',f'{k} の欧文書体が {FONT} でない / Latin theme font is not {FONT}')
                for sf in f.findall('a:font',NS):   # 言語ごとの補助の書体もゴシック系（KM1-TYP-001）/ per-script fonts must be sans
                    if NOTSANS.search(sf.get('typeface','')): out('FAIL','SCRIPTFONT',f'{k} の {sf.get("script")} の書体 {sf.get("typeface")} はゴシック系でない / not sans')
            s=t.find('.//a:clrScheme',NS)
            if s is not None:
                for e in s:
                    v=e.find('a:srgbClr',NS)
                    if v is not None and v.get('val').upper() not in PALETTE: out('FAIL','THEMECOLOR',f'テーマの色 {etree.QName(e).localname}={v.get("val")} が KM1 にない')
def check_docx(z,fname):
    core(z,fname); theme(z)
    doc=x(z,'word/document.xml'); st=x(z,'word/styles.xml')
    w='{%s}'%NS['w']
    # 既定の言語 / default language
    lang=st.find('.//w:docDefaults//w:lang',NS)
    if lang is None or 'ja' not in (lang.get(w+'eastAsia') or '')+(lang.get(w+'val') or ''): out('FAIL','LANG','既定の言語が日本語でない / default language is not ja-JP')
    else: out('PASS','LANG','ja-JP')
    # 見出しの段 / heading levels
    sid={s.get(w+'styleId'):s for s in st.findall('w:style',NS)}
    def outline(pid):
        s=sid.get(pid); 
        while s is not None:
            o=s.find('.//w:outlineLvl',NS)
            if o is not None: return int(o.get(w+'val'))+1
            m=re.match(r'Heading(\d)$',s.get(w+'styleId') or '')
            if m: return int(m.group(1))
            b=s.find('w:basedOn',NS); s=sid.get(b.get(w+'val')) if b is not None else None
        return None
    prev=0; n=0
    for p in doc.iter(w+'p'):
        ps=p.find('w:pPr/w:pStyle',NS)
        lv=outline(ps.get(w+'val')) if ps is not None else None
        if lv:
            n+=1
            if lv>prev+1: out('FAIL','HEAD',f'見出しの段が飛んでいる H{prev}→H{lv}: {"".join(p.itertext())[:30]}')
            prev=lv
        txt=''.join(p.itertext()).strip()
        # 太字だけの短い段落は見出しの代わりかもしれない / bold-only short paragraph may be a fake heading
        rs=p.findall('w:r',NS)
        if txt and len(txt)<40 and not lv and rs and all(r.find('w:rPr/w:b',NS) is not None for r in rs) and p.getparent().tag!=w+'tc':
            out('WARN','FAKEHEAD',f'太字だけの段落（見出しスタイルを使う）/ bold-only paragraph: {txt[:30]}')
        if re.match(r'^[・•●■◆]\s?',txt) and p.find('w:pPr/w:numPr',NS) is None: out('FAIL','LIST',f'手で打った箇条書き / typed bullet: {txt[:30]}')
    if n==0: out('FAIL','HEAD','見出しがない / no headings')
    # 文字の大きさと色 / sizes and colors
    sizes=set(); bad=set()
    for tree in (doc,st):
        for e in tree.iter(w+'sz'):
            sizes.add(int(e.get(w+'val'))/2)
        for e in tree.iter(w+'color'):
            v=(e.get(w+'val') or '').upper()
            if v not in PALETTE: bad.add(v)
    for s in sorted(sizes-WORD_SIZES): out('FAIL','SIZE',f'{s}pt は KM1 の Word の大きさにない / not a KM1 size')
    for v in sorted(sizes):
        if v<8: out('FAIL','MIN','8pt より小さい文字 / below 8pt')
    for v in bad: out('FAIL','COLOR',f'#{v} は KM1 の色にない / not a KM1 color')
    # 図の代替テキスト / alt text
    for dp in doc.iter('{%s}docPr'%NS['wp']):
        dec=dp.find('.//{http://schemas.microsoft.com/office/drawing/2017/decorative}decorative')
        if not (dp.get('descr') or '').strip() and dec is None: out('FAIL','ALT',f'図に代替テキストがない / image without alt text: {dp.get("name")}')
    # 表 / tables
    for i,t in enumerate(doc.iter(w+'tbl'),1):
        fr=t.find('w:tr',NS)
        if fr is None or fr.find('w:trPr/w:tblHeader',NS) is None: out('FAIL','TABLEHEAD',f'表 {i} の見出し行が「繰り返す」になっていない / header row not repeated')
        if t.find('.//w:gridSpan',NS) is not None or t.find('.//w:vMerge',NS) is not None: out('FAIL','MERGE',f'表 {i} に結合したセル / merged cells')
    # リンクの文字 / link text
    for h in doc.iter(w+'hyperlink'):
        t=''.join(h.itertext()).strip()
        if t in ('こちら','ここ','click here','here','リンク'): out('FAIL','LINK',f'行き先のわからないリンクの文字 / vague link text: {t}')
    sec=doc.find('.//w:sectPr/w:pgSz',NS)
    if sec is not None and not (abs(int(sec.get(w+'w'))-11906)<30 and abs(int(sec.get(w+'h'))-16838)<30) and not (abs(int(sec.get(w+'h'))-11906)<30): out('WARN','A4','A4 でない / not A4')
def check_pptx(z,fname):
    core(z,fname); theme(z)
    pres=x(z,'ppt/presentation.xml'); sz=pres.find('p:sldSz',NS)
    if abs(int(sz.get('cx'))/int(sz.get('cy'))-16/9)>0.01: out('WARN','RATIO','16:9 でない / not 16:9')
    slides=sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n)],key=lambda n:int(re.findall(r'\d+',n)[-1]))
    titles={}
    parts=slides+[n for n in z.namelist() if re.match(r'ppt/slide(Layout|Master)s/slide(Layout|Master)\d+\.xml$',n) or re.match(r'ppt/charts/chart\d+\.xml$',n)]
    sizes=set(); bad=set(); nolang=0
    for n in parts:
        s=x(z,n)
        for r in s.iter('{%s}rPr'%NS['a'],'{%s}defRPr'%NS['a'],'{%s}endParaRPr'%NS['a']):
            if r.get('sz'): sizes.add(int(r.get('sz'))/100)
        for c in s.iter('{%s}srgbClr'%NS['a']):
            if c.get('val').upper() not in PALETTE: bad.add(c.get('val').upper())
    for i,n in enumerate(slides,1):
        s=x(z,n)
        tt=None
        for sp in s.iter('{%s}sp'%NS['p']):
            ph=sp.find('.//p:nvPr/p:ph',NS)
            if ph is not None and ph.get('type') in ('title','ctrTitle'): tt=''.join(sp.find('.//p:txBody',NS).itertext()).strip() if sp.find('.//p:txBody',NS) is not None else ''
        if not tt: out('FAIL','SLIDETITLE',f'スライド {i} に題名がない / slide {i} has no title')
        else: titles.setdefault(tt,[]).append(i)
        for pic in s.iter('{%s}pic'%NS['p'],'{%s}graphicFrame'%NS['p']):
            c=pic.find('.//p:cNvPr',NS)
            dec=pic.find('.//{http://schemas.microsoft.com/office/drawing/2017/decorative}decorative')
            if c is not None and not (c.get('descr') or '').strip() and dec is None and pic.find('.//a:tbl',NS) is None:
                out('FAIL','ALT',f'スライド {i} の図・グラフに代替テキストがない / no alt text: {c.get("name")}')
        for t in s.iter('{%s}tbl'%NS['a']):
            pr=t.find('a:tblPr',NS)
            if pr is None or pr.get('firstRow')!='1': out('WARN','TABLEHEAD',f'スライド {i} の表で「タイトル行」が入っていない / header row option off')
            if t.find('.//a:tc[@gridSpan]',NS) is not None or t.find('.//a:tc[@rowSpan]',NS) is not None: out('FAIL','MERGE',f'スライド {i} の表に結合したセル')
        if s.find('.//p:transition',NS) is not None or s.find('.//p:timing',NS) is not None: out('WARN','MOTION',f'スライド {i} に画面切り替え・アニメーション')
        for r in s.iter('{%s}rPr'%NS['a']):
            if r.getparent().find('a:t',NS) is not None and not r.get('lang'): nolang+=1
    for t,ii in titles.items():
        if len(ii)>1: out('FAIL','DUPTITLE',f'同じ題名のスライド {ii}: {t[:30]}（続きなら「（2/2）」を付ける）')
    for s in sorted(sizes-SLIDE_SIZES): out('FAIL','SIZE',f'{s:g}pt は KM1 のスライドの大きさにない / not a KM1 slide size')
    for v in sorted(bad): out('FAIL','COLOR',f'#{v} は KM1 の色にない / not a KM1 color')
    if nolang: out('WARN','LANG',f'言語の指定がない文字 {nolang} か所 / runs without lang')
    layout_checks(z,slides)
    if slides: out('PASS','SLIDES',f'{len(slides)} 枚')
def xfrm(e):
    o=e.find('.//a:off',NS); s=e.find('.//a:ext',NS)
    if o is None or s is None: return None
    return [int(o.get(k))/EMU for k in ('x','y')]+[int(s.get(k))/EMU for k in ('cx','cy')]
def em(t): return sum(1 if ord(ch)>0x2E7F else 0.55 for ch in t)
def layout_checks(z,slides):
    """余白・グリッド・はみ出し・題名の長さ・項目の数・空き（office.md §4.2〜4.3）/ spacing rules"""
    for i,n in enumerate(slides,1):
        s=x(z,n); boxes=[]
        for a in s.iter('{%s}normAutofit'%NS['a']):
            if a.get('fontScale') and a.get('fontScale')!='100000': out('FAIL','SHRINK',f'スライド {i} の文字が「自動調整」で縮んでいる（{int(a.get("fontScale"))/1000:g}%）。削るか 2 枚に分ける')
        for e in list(s.iter('{%s}sp'%NS['p']))+list(s.iter('{%s}graphicFrame'%NS['p']))+list(s.iter('{%s}pic'%NS['p'])):
            ph=e.find('.//p:nvPr/p:ph',NS)
            if ph is not None:
                body=e.find('.//p:txBody',NS)
                if ph.get('type') in ('title','ctrTitle') and body is not None:
                    tt=''.join(body.itertext()).strip()
                    if em(tt)>TITLE_EM: out('WARN','TITLELEN',f'スライド {i} の題名が 1 行に入らない（全角 {TITLE_EM:.0f} 字まで）: {tt[:30]}')
                elif body is not None:
                    lv1=[p for p in body.findall('a:p',NS) if p.find('a:pPr/a:buChar',NS) is not None or (p.find('a:pPr',NS) is not None and p.find('a:pPr',NS).get('indent'))]
                    if len(lv1)>6: out('WARN','BULLETS',f'スライド {i} の箇条書きが {len(lv1)} 項目（6 つまで。2 枚に分ける）')
                continue
            b=xfrm(e)
            trs=e.findall('.//a:tbl/a:tr',NS)
            if b and trs: b[3]=sum(int(r.get('h'))/EMU for r in trs)   # 表の高さは行の合計 / table height = sum of rows
            if b: boxes.append((b,e.find('.//p:cNvPr',NS).get('name')))
        def inside(a,b): return a is not b and b[0]-1<=a[0] and b[1]-1<=a[1] and a[0]+a[2]<=b[0]+b[2]+1 and a[1]+a[3]<=b[1]+b[3]+1
        top=[(b,nm) for b,nm in boxes if not any(inside(b,o) for o,_ in boxes)]
        for (bx,by,bw,bh),nm in top:
            if by+bh>BODY_BOTTOM+1: out('FAIL','OVERFLOW',f'スライド {i} の {nm} が本文の領域の下（{BODY_BOTTOM}pt）を越えて柱に重なる')
            if by<BODY_TOP-1: out('WARN','OVERFLOW',f'スライド {i} の {nm} が題名の行に入っている')
            if min(abs(bx-g) for g in GRID_X)>1 or min(abs(bx+bw-g) for g in GRID_R)>1: out('WARN','GRID',f'スライド {i} の {nm} の左右の端が 12 列のグリッドにそろっていない（x={bx:g}, w={bw:g}）')
        # 図・表・カードだけのスライドで、本文の領域の下半分が空いている / lower half empty on a visual slide
        if top and not any(e.find('.//p:nvPr/p:ph[@type="body"]',NS) is not None for e in s.iter('{%s}sp'%NS['p'])):
            low=max(b[1]+b[3] for b,_ in top)
            if low<(BODY_TOP+BODY_BOTTOM)/2: out('WARN','EMPTY',f'スライド {i} の本文の領域の下半分が空いている（図・表・カードを本文の領域に合わせる）')
    # 14pt は柱の行だけ / 14pt only in the footer row
    for n in slides+[m for m in z.namelist() if re.match(r'ppt/slide(Layout|Master)s/slide(Layout|Master)\d+\.xml$',m)]:
        s=x(z,n)
        for e in s.iter('{%s}sp'%NS['p']):
            if any(r.get('sz')=='1400' for r in e.iter('{%s}rPr'%NS['a'],'{%s}defRPr'%NS['a'])):
                b=xfrm(e)
                if b and b[1]<FOOT_TOP-1: out('FAIL','MIN',f'{n.split("/")[-1]}: 14pt は柱とスライド番号だけ。内容の文字は 20pt 以上')
rc=0
for f in sys.argv[1:]:
    res.clear(); z=zipfile.ZipFile(f); name=f.rsplit('/',1)[-1]
    (check_docx if f.lower().endswith(('.docx','.dotx')) else check_pptx)(z,name)
    print('==',name)
    for l,c,m in res:
        if l!='PASS' or '-v' in sys.argv: print(f'{l:4} {c:10} {m}')
    nf=sum(1 for r in res if r[0]=='FAIL'); nw=sum(1 for r in res if r[0]=='WARN')
    print(f'--- FAIL {nf} / WARN {nw}（機械で確かめられる項目だけ。人の確認が別に要る / machine checks only）')
    rc|=nf>0
sys.exit(1 if rc else 0)
