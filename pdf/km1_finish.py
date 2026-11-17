#!/usr/bin/env python3
"""KM1 PDF 仕上げ / KM1 PDF finishing

使い方 / Usage:  python3 km1_finish.py in.pdf out.pdf [--title "題名"] [--lang ja]
必要 / Requires: pypdf

Chrome で書き出した PDF に、KM1「PDF の規定」で必要な文書情報を足す。
Adds the document information the KM1 PDF rules need to a PDF exported from Chrome.
- XMP メタデータ（dc:title・dc:language）/ XMP with dc:title and dc:language
- 題名をウィンドウに表示（DisplayDocTitle）/ DisplayDocTitle
- リンク注釈の説明（/Contents）/ /Contents on link annotations
- Chrome のしおりで題名が 2 回つながる不具合を直す / fixes Chrome's doubled bookmark titles
- しおりがあれば、開いたときにしおりを表示 / opens with bookmarks shown when present
PDF/UA の識別子は入れない（準拠を確かめる検査器が要るため）。
It never adds a PDF/UA identifier; claiming conformance needs a real validator.
"""
import sys, argparse
from xml.sax.saxutils import escape
from pypdf import PdfReader, PdfWriter
from pypdf.generic import StreamObject, NameObject, TextStringObject, BooleanObject, DictionaryObject

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('dst')
ap.add_argument('--title'); ap.add_argument('--lang')
a = ap.parse_args()

w = PdfWriter(clone_from=a.src)
root = w._root_object
title = a.title or str((w.metadata or {}).get('/Title', '') or '')
lang = a.lang or str(root.get('/Lang', '') or 'ja')
if a.title: w.add_metadata({'/Title': title})
root[NameObject('/Lang')] = TextStringObject(lang)

vp = root.get('/ViewerPreferences')
vp = vp.get_object() if vp is not None else DictionaryObject()
vp[NameObject('/DisplayDocTitle')] = BooleanObject(True)
root[NameObject('/ViewerPreferences')] = vp

xmp = f'''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title><rdf:Alt><rdf:li xml:lang="x-default">{escape(title)}</rdf:li></rdf:Alt></dc:title><dc:language><rdf:Bag><rdf:li>{escape(lang)}</rdf:li></rdf:Bag></dc:language><dc:format>application/pdf</dc:format></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''
ms = StreamObject(); ms.set_data(xmp.encode('utf-8'))
ms[NameObject('/Type')] = NameObject('/Metadata'); ms[NameObject('/Subtype')] = NameObject('/XML')
root[NameObject('/Metadata')] = w._add_object(ms)

n = 0
for pg in w.pages:
    for an in pg.get('/Annots', []) or []:
        an = an.get_object()
        if an.get('/Subtype') == '/Link' and not an.get('/Contents'):
            act = an.get('/A'); act = act.get_object() if act is not None else {}
            u = act.get('/URI') if act else None
            an[NameObject('/Contents')] = TextStringObject(f'外部リンク / External link: {u}' if u else '文書内のリンク / Link within this document')
            n += 1

def fix(node):
    while node is not None:
        node = node.get_object(); t = str(node.get('/Title', ''))
        h = len(t) // 2
        if len(t) % 2 == 0 and h and t[:h] == t[h:]: node[NameObject('/Title')] = TextStringObject(t[:h])
        if '/First' in node: fix(node['/First'])
        node = node.get('/Next')
if '/Outlines' in root and root['/Outlines'].get_object().get('/First') is not None:
    fix(root['/Outlines'].get_object()['/First'])
    w.page_mode = '/UseOutlines'

w.write(a.dst)
print(f'done: title="{title}" lang={lang} links={n}')
