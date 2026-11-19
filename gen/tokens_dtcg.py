#!/usr/bin/env python3
"""tokens.json（正本）から W3C Design Tokens（DTCG 形式）のファイルを作る / Export tokens.json to the W3C DTCG format
使い方 / Usage: python3 gen/tokens_dtcg.py [出力フォルダ / out dir（既定 dist/tokens）]
出力: km1.light.tokens.json と km1.dark.tokens.json（DTCG にはライト・ダークの決まった書き方がないので、テーマごとに 1 ファイル）。
正本は tokens.json のまま。このファイルは生成物で、check_all.sh が差分を調べる。
Writes one DTCG file per theme (the format has no standard for modes). tokens.json stays the source of truth;
these are generated and diff-checked by check_all.sh."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = re.compile(r'^\{([a-z0-9-]+)\}$')


def dim(v):
    """'24px' → {"value": 24, "unit": "px"}、'0' → 0px"""
    v = str(v).strip()
    m = re.fullmatch(r'(-?\d+(?:\.\d+)?)(px|rem)?', v)
    if not m:
        raise ValueError(f'寸法でない / not a dimension: {v}')
    n = float(m.group(1))
    return {'value': int(n) if n.is_integer() else n, 'unit': m.group(2) or 'px'}


def shadow(v):
    out = []
    for part in re.split(r',\s*(?![^()]*\))', v):
        m = re.fullmatch(r'\s*(-?\d+)(?:px)?\s+(-?\d+)(?:px)?\s+(\d+)(?:px)?(?:\s+(-?\d+)(?:px)?)?\s+(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})\s*', part)
        if not m:
            raise ValueError(f'影の形が読めない / unparsable shadow: {part}')
        out.append({'color': m.group(5), 'offsetX': dim(m.group(1) + 'px'), 'offsetY': dim(m.group(2) + 'px'),
                    'blur': dim(m.group(3) + 'px'), 'spread': dim((m.group(4) or '0') + 'px')})
    return out if len(out) > 1 else out[0]


def build(d, mode):
    out = {'$description': f'KM1 design tokens ({mode}). Generated from tokens.json by gen/tokens_dtcg.py. Do not edit.'}
    col = out['color'] = {'$type': 'color'}
    for t in d['color']['tokens']:
        v = t['value'][mode] if isinstance(t['value'], dict) else t['value']
        m = REF.match(v.strip())
        col[t['name']] = {'$value': '{color.%s}' % m.group(1) if m else v.strip(), '$description': t.get('usage', '')}
    names = {}
    for g in ('spacing', 'radius', 'size'):
        grp = out[g] = {'$type': 'dimension'}
        for t in d[g]['tokens']:
            grp[t['name']] = {'$value': dim(t['value']), '$description': t.get('usage', '')}
            names[t['name']] = g
    for g in ('spacingRole', 'platformTarget'):
        grp = out[g] = {'$type': 'dimension'}
        for t in d[g]['tokens']:
            r = t.get('ref')
            grp[t['name']] = {'$value': '{%s.%s}' % (names[r], r) if r in names else dim(t['value']), '$description': t.get('usage', '')}
    grp = out['shadow'] = {'$type': 'shadow'}
    for t in d['shadow']['tokens']:
        grp[t['name']] = {'$value': shadow(t['value']), '$description': t.get('usage', '')}
    grp = out['layer'] = {'$type': 'number'}
    for t in d['layer']['tokens']:
        grp[t['name']] = {'$value': float(t['value']) if '.' in str(t['value']) else int(t['value']), '$description': t.get('usage', '')}
    grp = out['opacity'] = {'$type': 'number'}
    for t in d['opacity']['tokens']:
        grp[t['name']] = {'$value': float(str(t['value']).rstrip('%')) / 100, '$description': t.get('usage', '')}
    fam = out['fontFamily'] = {'$type': 'fontFamily'}
    for k, v in d['type']['families'].items():
        fam[k] = {'$value': [x.strip().strip('"') for x in v.split(',')]}
    typ = out['typography'] = {'$type': 'typography'}
    for g in d['type']['groups']:
        for st in g['styles']:
            typ[st['name']] = {'$value': {'fontFamily': '{fontFamily.%s}' % g.get('family', 'sans'), 'fontSize': dim(st['fontSize']),
                                          'fontWeight': st['fontWeight'], 'lineHeight': round(float(st['lineHeight'].rstrip('px')) / float(st['fontSize'].rstrip('px')), 4),
                                          'letterSpacing': dim('0px')}, '$description': st.get('usage', '')}
    return out


def main():
    d = json.load(open(os.path.join(ROOT, 'tokens.json'), encoding='utf-8'))
    od = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'dist', 'tokens')
    os.makedirs(od, exist_ok=True)
    for mode in ('light', 'dark'):
        f = os.path.join(od, f'km1.{mode}.tokens.json')
        with open(f, 'w', encoding='utf-8') as fh:
            json.dump(build(d, mode), fh, ensure_ascii=False, indent=2)
            fh.write('\n')
        print('ok', f)


if __name__ == '__main__':
    main()
