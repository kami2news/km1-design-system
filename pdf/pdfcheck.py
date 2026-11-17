#!/usr/bin/env python3
"""KM1 PDF 検査 / KM1 PDF checker

使い方 / Usage:  python3 pdfcheck.py file.pdf [--json]
必要 / Requires: pypdf (pip install pypdf)

KM1「PDF の規定」のうち、機械で確かめられる項目を調べる。PDF/UA-1 の Matterhorn Protocol のうち
機械判定できる条件の一部（番号を併記）と、KM1 独自の項目（KM-）を扱う。
人の目で見る項目（読む順の正しさ、代替テキストの中身、色の使い方など）は調べない。
Checks the machine-testable part of the KM1 PDF rules: a subset of the PDF/UA-1 Matterhorn
machine-testable failure conditions (numbers given) plus KM1-specific items (KM-).
It does not check human-judgment items (reading order, alt-text quality, color use).
結果 / Result: FAIL があれば終了コード 1 / exit code 1 if any FAIL.
"""
import sys, json, re, os
from pypdf import PdfReader
from pypdf.generic import IndirectObject, ArrayObject, DictionaryObject

A4 = (595.28, 841.89)

def obj(x):
    return x.get_object() if isinstance(x, IndirectObject) else x

def walk(node, depth=0, out=None, parent=None):
    """構造木をたどる / walk the structure tree"""
    if out is None: out = []
    node = obj(node)
    if isinstance(node, DictionaryObject):
        s = node.get('/S')
        if s is not None:
            out.append((str(s), node, parent))
        k = node.get('/K')
        if k is not None:
            k = obj(k)
            kids = k if isinstance(k, ArrayObject) else [k]
            for c in kids:
                c = obj(c)
                if isinstance(c, DictionaryObject) and ('/S' in c or '/K' in c) and c.get('/Type') not in ('/MCR', '/OBJR'):
                    walk(c, depth + 1, out, node)
    return out

def check(path):
    R = []
    def res(code, ok, msg, level='FAIL'):
        R.append({'code': code, 'result': 'PASS' if ok else level, 'msg': msg})
    r = PdfReader(path)
    root = obj(r.trailer['/Root'])
    info = r.metadata or {}

    # 暗号化 / encryption
    res('KM-SEC', not r.is_encrypted, '暗号化・パスワードなし / not encrypted (支援技術を妨げない / no barrier for assistive tech)')

    # タグ / tagged
    mi = obj(root.get('/MarkInfo', {})) or {}
    res('01-005', bool(mi.get('/Marked')), 'タグ付き PDF（MarkInfo /Marked true）/ tagged PDF')
    res('KM-TREE', '/StructTreeRoot' in root, '構造木がある / has a structure tree')

    # 言語 / language
    lang = str(root.get('/Lang', '') or '')
    res('11-001', bool(lang), f'文書の言語 /Lang = "{lang}" / document language')

    # 題名 / title
    title = str(info.get('/Title', '') or '').strip()
    res('KM-TITLE', bool(title) and not re.search(r'\.(docx?|pptx?|html?|pdf)$|^untitled|^無題', title, re.I),
        f'題名が入っている（ファイル名ではない）"{title}" / meaningful title')
    vp = obj(root.get('/ViewerPreferences', {})) or {}
    res('07-001', bool(vp.get('/DisplayDocTitle')), 'ウィンドウに題名を表示（DisplayDocTitle）/ DisplayDocTitle true')

    # XMP
    xmp = root.get('/Metadata')
    xs = obj(xmp).get_data().decode('utf-8', 'ignore') if xmp else ''
    res('06-001', bool(xs), 'XMP メタデータがある / XMP metadata present')
    if xs:
        res('06-003', 'dc:title' in xs, 'XMP に dc:title / dc:title in XMP')
    res('06-002', 'pdfuaid' in xs, 'PDF/UA の識別子（PDF/UA 準拠を名乗るときだけ必要）/ PDF/UA identifier (only if claiming PDF/UA)', 'INFO')

    # しおり / outline
    n = len(r.pages)
    has_outline = '/Outlines' in root and obj(root['/Outlines']).get('/First') is not None
    res('KM-OUTLINE', has_outline or n < 9, f'{n} ページ。9 ページ以上ならしおり（目次）が必要 / bookmarks required at 9+ pages', 'FAIL')

    # 判型 / page size
    bad = []
    for i, p in enumerate(r.pages):
        w, h = float(p.mediabox.width), float(p.mediabox.height)
        a, b = sorted((w, h))
        if not (abs(a - A4[0]) < 3 and abs(b - A4[1]) < 3): bad.append((i + 1, round(w), round(h)))
    res('KM-SIZE', not bad, 'すべて A4（縦か横）/ all A4' + (f' 例外 {bad[:3]}' if bad else ''), 'WARN')

    # フォント埋め込み / font embedding
    notemb = set()
    for p in r.pages:
        rs = obj(p.get('/Resources', {})) or {}
        fd = obj(rs.get('/Font', {})) or {}
        for k, f in fd.items():
            f = obj(f)
            if f.get('/Subtype') == '/Type3': continue
            d = f.get('/FontDescriptor')
            if d is None and '/DescendantFonts' in f: d = obj(obj(f['/DescendantFonts'])[0]).get('/FontDescriptor')
            d = obj(d) if d is not None else {}
            if not any(x in d for x in ('/FontFile', '/FontFile2', '/FontFile3')): notemb.add(str(f.get('/BaseFont')))
    res('31-009', not notemb, 'フォントをすべて埋め込み / all fonts embedded' + (f' 未埋め込み {sorted(notemb)}' if notemb else ''))

    # 文字のないページ / pages without text (scanned?)
    empty = []
    for i, p in enumerate(r.pages):
        try: t = (p.extract_text() or '').strip()
        except Exception: t = 'x'
        if len(t) < 5: empty.append(i + 1)
    res('KM-TEXT', not empty, '全ページに文字がある（画像だけのページなし）/ every page has real text' + (f' 文字なし p.{empty[:10]}' if empty else ''), 'WARN')

    # 構造の中身 / structure contents
    if '/StructTreeRoot' in root:
        st = obj(root['/StructTreeRoot'])
        rm = obj(st.get('/RoleMap', {})) or {}
        els = walk(st)
        def std(s):
            seen = 0
            while s in rm and seen < 10: s = str(rm[s]); seen += 1
            return s
        types = [std(s) for s, _, _ in els]
        figs = [(s, d) for (s0, d, _), s in zip(els, types) if s == '/Figure']
        noalt = [1 for s, d in figs if not (d.get('/Alt') or d.get('/ActualText'))]
        res('13-004', not noalt, f'図 {len(figs)} 個すべてに代替テキスト / alt text on all {len(figs)} figures' + (f'（なし {len(noalt)}）' if noalt else ''))
        hs = [int(s[2]) for s in types if re.fullmatch(r'/H[1-6]', s)]
        res('14-002', bool(hs) or n < 3, f'見出しタグ {len(hs)} 個 / heading tags: {len(hs)}', 'FAIL')
        if hs:
            res('14-001', hs[0] == 1, f'最初の見出しが H1（実際は H{hs[0]}）/ first heading is H1')
            skip = [(a, b) for a, b in zip(hs, hs[1:]) if b > a + 1]
            res('14-003', not skip, '見出しの段を飛ばさない / no skipped heading levels' + (f' 例 H{skip[0][0]}→H{skip[0][1]}（{len(skip)} か所）' if skip else ''))
        res('14-007', not ('/H' in types and hs), 'H と H1〜H6 を混ぜない / no mix of H and Hn')
        tables = [d for (s0, d, _), s in zip(els, types) if s == '/Table']
        th = types.count('/TH')
        res('15-KM', not tables or th > 0, f'表 {len(tables)} 個、見出しセル TH {th} 個 / tables: {len(tables)}, TH cells: {th}')
        res('KM-LIST', False, f'リスト L {types.count("/L")}、段落 P {types.count("/P")}、リンク Link {types.count("/Link")} / structure counts', 'INFO')

    # リンク注釈 / link annotations
    links = nocont = 0
    for p in r.pages:
        for a in obj(p.get('/Annots', [])) or []:
            a = obj(a)
            if a.get('/Subtype') == '/Link':
                links += 1
                if not a.get('/Contents'): nocont += 1
    res('28-KM', False, f'リンク {links} 個（うち /Contents なし {nocont}。PDF/UA-1 では Link 構造要素に入っていれば足りるが、PDF/UA-2 では Contents が要る）/ links', 'INFO')

    # 大きさ / size
    mb = os.path.getsize(path) / 1048576
    res('KM-SIZEMB', mb <= 10 or mb / max(n, 1) <= 0.3, f'{mb:.1f} MB（{n} ページ、1 ページ {mb / max(n, 1) * 1024:.0f} KB）。目安: 10 MB 以下か 1 ページ 300 KB 以下 / size budget', 'WARN')
    return R

if __name__ == '__main__':
    p = sys.argv[1]
    R = check(p)
    if '--json' in sys.argv:
        print(json.dumps(R, ensure_ascii=False, indent=1))
    else:
        for x in R: print(f"{x['result']:5} {x['code']:10} {x['msg']}")
        f = sum(x['result'] == 'FAIL' for x in R); w = sum(x['result'] == 'WARN' for x in R)
        print(f'--- FAIL {f} / WARN {w}  （機械で確かめられる項目だけ。人の確認が別に要る / machine checks only）')
    sys.exit(1 if any(x['result'] == 'FAIL' for x in R) else 0)
