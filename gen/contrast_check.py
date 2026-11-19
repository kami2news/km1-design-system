#!/usr/bin/env python3
"""意味づけの色の組み合わせのコントラストを、ライトとダークの両方で調べる / Contrast check for semantic color pairs
使い方 / Usage: python3 gen/contrast_check.py [tokens.json]
文字は 4.5:1 以上（WCAG 2.2 1.4.3）、枠・アイコン・フォーカスの線は 3:1 以上（1.4.11）。
無効の文字（ink-disabled）は WCAG の対象外なので調べない。FAIL があると終了コード 1。
Text pairs need 4.5:1 (WCAG 1.4.3), UI strokes, icons and focus rings 3:1 (1.4.11); disabled text is exempt. Exits 1 on any FAIL."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURFACES = ['surface', 'surface-subtle', 'surface-muted', 'surface-sunken']
# (前景, 背景の一覧, 必要な比, 種類) / (foreground, backgrounds, ratio, kind)
PAIRS = [
    ('ink', SURFACES + ['surface-hover', 'surface-pressed'], 4.5, '文字'),
    ('ink-secondary', SURFACES, 4.5, '文字'),
    ('ink-tertiary', ['surface', 'surface-subtle'], 4.5, '文字'),
    ('on-brand', ['brand'], 4.5, '文字'),
    ('brand-ink', ['surface', 'surface-subtle'], 4.5, '文字（リンク）'),
    ('info-ink', ['surface', 'info-tint'], 4.5, '文字'),
    ('danger-ink', ['surface', 'danger-tint'], 4.5, '文字'),
    ('success-ink', ['surface', 'success-tint'], 4.5, '文字'),
    ('warning-ink', ['surface', 'warning-tint'], 4.5, '文字'),
    ('stroke-strong', SURFACES, 3.0, '枠'),
    ('focus-ring', SURFACES, 3.0, 'フォーカス'),
    ('icon-ink', SURFACES, 3.0, 'アイコン'),
    ('brand-stroke', ['surface'], 3.0, '枠（主ボタン）'),
]


def lum(hx):
    hx = hx.lstrip('#')
    c = [int(hx[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main():
    d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'tokens.json'), encoding='utf-8'))
    tok = {t['name']: t['value'] for t in d['color']['tokens']}

    def resolve(name, mode, depth=0):
        v = tok[name]
        v = v[mode] if isinstance(v, dict) else v
        m = re.fullmatch(r'\{([a-z0-9-]+)\}', v.strip())
        if m and depth < 8:
            return resolve(m.group(1), mode, depth + 1)
        return v.strip()

    fails = n = 0
    for fg, bgs, need, kind in PAIRS:
        if fg not in tok:
            print(f'WARN {fg} がトークンにない / missing token'); continue
        for bg in bgs:
            if bg not in tok:
                print(f'WARN {bg} がトークンにない / missing token'); continue
            for mode in ('light', 'dark'):
                a, b = resolve(fg, mode), resolve(bg, mode)
                if not (a.startswith('#') and b.startswith('#')):
                    continue
                r = ratio(a, b); n += 1
                if r + 1e-9 < need:
                    fails += 1
                    print(f'FAIL {mode:5} {kind}: {fg} {a} / {bg} {b} = {r:.2f}:1（{need}:1 以上が要る）')
    print(f'--- 組み合わせ {n}（ライト・ダーク）/ FAIL {fails}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
