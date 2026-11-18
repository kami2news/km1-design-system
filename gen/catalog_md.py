#!/usr/bin/env python3
"""部品カタログ（components/README.md）を作る / Build the GitHub component catalog
使い方 / Usage: python3 catalog_md.py（先に shoot_previews.js で画像を撮る / shoot screenshots first）
見本の @dsCard の group ごとに並べ、ライトとダークの画像を並べる。PDF の部品カタログも同じ順。
Groups previews by their @dsCard group and shows light and dark screenshots side by side."""
import os, re, glob, sys
G = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(G); C = os.path.join(ROOT, 'components')
ORDER = ['表紙 / Cover', 'Actions', 'Forms', 'Lists and selection', 'Data', 'Date and time', 'Navigation', 'Containers', 'Surfaces',
         'Overlays', 'Feedback', 'Status', 'Icons', '密度 / Density', '画面の例 / Screen patterns', 'M1 比較 / M1 comparison']
JA = {'Actions': '操作', 'Forms': '入力', 'Lists and selection': '一覧と選択', 'Data': 'データ', 'Date and time': '日付と時間',
      'Navigation': 'ナビゲーション', 'Containers': '入れ物', 'Surfaces': '面', 'Overlays': '重ねて出すもの', 'Feedback': '知らせ',
      'Status': '状態', 'Icons': 'アイコン'}
def label(g): return f'{JA[g]} / {g}' if g in JA else g

def groups():
    out = {}
    for p in sorted(glob.glob(os.path.join(C, '*', 'preview.html'))):
        n = os.path.basename(os.path.dirname(p))
        m = re.search(r'@dsCard group="([^"]+)"', open(p, encoding='utf-8').read())
        out.setdefault(m.group(1) if m else ('表紙 / Cover' if n == 'Cover' else 'Other'), []).append(n)
    keys = [g for g in ORDER if g in out] + sorted(g for g in out if g not in ORDER)
    return [(g, label(g), out[g]) for g in keys]

def summary(n):
    p = os.path.join(C, n, 'README.md')
    if not os.path.exists(p): return ''
    for line in open(p, encoding='utf-8'):
        line = line.strip()
        if line and not line.startswith(('#', '*', '|', '>', '-')): return re.sub(r'\s+', ' ', line)
    return ''

if __name__ == '__main__':
    gs = groups(); total = sum(len(x) for _, _, x in gs)
    o = ['# KM1 部品カタログ / Component catalog', '',
         f'見本 {total} 件を {len(gs)} のグループに分けて載せる。各部品の説明は部品フォルダの `README.md`、動く見本は `preview.html`。'
         '画像は `gen/shoot_previews.js` で撮ったもの（左がライト、右がダーク）。PDF 版は `dist/KM1_部品カタログ.pdf`。',
         f'*{total} previews in {len(gs)} groups. Each folder has a README and a live `preview.html`; light on the left, dark on the right. PDF: `dist/KM1_部品カタログ.pdf`.*', '',
         '## 目次 / Contents', '']
    for g, lab, ns in gs:
        a = re.sub(r'[^\w\- ]', '', lab.lower()).strip().replace(' ', '-')
        o.append(f'- **{lab}**: ' + '・'.join(f'[{n}](#{n.lower()})' for n in ns))
    for g, lab, ns in gs:
        o += ['', f'## {lab}', '']
        for n in ns:
            o += [f'### {n}', '', summary(n) + f' → [{n}/]({n}/)', '',
                  '<table><tr>'
                  f'<td valign="top"><img src="{n}/preview.png" alt="{n} の見本（ライト）/ {n} preview, light" width="420"></td>'
                  f'<td valign="top"><img src="{n}/preview-dark.png" alt="{n} の見本（ダーク）/ {n} preview, dark" width="420"></td>'
                  '</tr></table>', '']
    open(os.path.join(C, 'README.md'), 'w', encoding='utf-8').write('\n'.join(o).rstrip() + '\n')
    print('catalog', total, 'previews,', len(gs), 'groups')
