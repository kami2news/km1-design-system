"""KM1 B 案の原図 / Source drawings for KM1 B icons (KM1-ICO-001 §8)

基準: 「KM1 アイコン作成指示書」の B 案（調整版）。20 の格子、線 1.45（検索 1.35）、端と角は丸、
淡い面は閉じた「もの」の形（予定の仲間・書類・入れ物・建物など）だけ。操作の記号（矢印・×・＋など）には面を付けない。
Basis: the B (adjusted) sheet. 20 grid, 1.45 strokes (search 1.35), round caps/joins; soft tint only on closed
"object" shapes (calendar family, documents, containers, buildings), never on action marks.

各アイコンは ink（線と点）、tint（淡い面、なしもあり）、knock（線も面もくり抜く場所）で書く。
大きさごとに線の幅を変えて輪郭にし、Web も Flutter も同じ輪郭を塗る。
Each icon has ink ops, an optional tint shape and knock-outs; outlines are computed per size and filled everywhere.
"""
import math
import pathops
from fontTools.svgLib.path import parse_path

SW_STD = {16: 1.625, 20: 1.45, 24: 1.3}       # 実寸で約 1.3・1.45・1.55px / ≈1.3, 1.45, 1.55px actual
SW_SEARCH = {16: 1.5, 20: 1.35, 24: 1.2}
TINT_Y = (4, 17)

# ------------------------------------------------------------------ 形 / shapes
def P(d):
    p = pathops.Path(); parse_path(d, p.getPen()); return p
def rr(x, y, w, h, r):
    return P(f'M{x+r} {y}h{w-2*r}a{r} {r} 0 0 1 {r} {r}v{h-2*r}a{r} {r} 0 0 1 {-r} {r}h{-(w-2*r)}a{r} {r} 0 0 1 {-r} {-r}v{-(h-2*r)}a{r} {r} 0 0 1 {r} {-r}z')
def circ(cx, cy, r):
    return P(f'M{cx-r} {cy}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0z')
def pl(*pts, close=False):
    return P('M' + 'L'.join(f'{x:.3f} {y:.3f}' for x, y in pts) + ('Z' if close else ''))
def arc(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return P(f'M{x0:.3f} {y0:.3f}A{r} {r} 0 {large} 1 {x1:.3f} {y1:.3f}')
def head(x, y, ang, s=2.6):
    """矢じり（ang の向きに進む先端 x,y）/ arrowhead at (x,y) pointing to ang degrees"""
    a1, a2 = math.radians(ang + 180 - 45), math.radians(ang + 180 + 45)
    return pl((x + s * math.cos(a1), y + s * math.sin(a1)), (x, y), (x + s * math.cos(a2), y + s * math.sin(a2)))
def L(d): return ('+', P(d) if isinstance(d, str) else d, 'line')
def F(shape): return ('+', shape, 'fill')
def DOT(x, y, r=0.85): return ('dot', x, y, r)

# 共通の形 / shared shapes
CAL = 'M4 4.25h12a1.25 1.25 0 0 1 1.25 1.25v10.25a1.25 1.25 0 0 1-1.25 1.25H4a1.25 1.25 0 0 1-1.25-1.25V5.5A1.25 1.25 0 0 1 4 4.25Z'
CAL_TOP = 'M3 8h14M6.5 2.75v3m7-3v3'
FOLDER = 'M3.5 4.25h4l2 2h7A1.25 1.25 0 0 1 17.75 7.5v7.75a1.25 1.25 0 0 1-1.25 1.25h-13a1.25 1.25 0 0 1-1.25-1.25V5.5A1.25 1.25 0 0 1 3.5 4.25Z'
BELL = 'M5.25 9a4.75 4.75 0 0 1 9.5 0v2.1l1.75 3.05a.55.55 0 0 1-.48.85H3.98a.55.55 0 0 1-.48-.85l1.75-3.05V9Z'
DOC = 'M5.25 2.75h6.25l4.25 4.25v9a1.25 1.25 0 0 1-1.25 1.25H5.25A1.25 1.25 0 0 1 4 16V4a1.25 1.25 0 0 1 1.25-1.25Z'
DOC_FOLD = 'M11.25 3v4.25h4.25'

def cal(*extra, tint=True):
    return {'tint': P(CAL) if tint else None, 'ink': [L(CAL), L(CAL_TOP), *extra]}

def gear(cx=10, cy=10, ro=7.0, ri=5.4, n=8):
    pts = []
    for i in range(n):
        a = 360 / n * i
        for da, r in ((-12, ri), (-7, ro), (7, ro), (12, ri)):
            t = math.radians(a + da - 90); pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return pl(*pts, close=True)

def star(cx=10, cy=10.6, ro=7.4, ri=3.3):
    pts = []
    for i in range(10):
        r = ro if i % 2 == 0 else ri; t = math.radians(-90 + 36 * i)
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return pl(*pts, close=True)

# ------------------------------------------------------------------ 原図 / drawings
B = {}
def d(name, ink, tint=None, knock=None, sw=None, ink16=None, solid=None, hollow=False):
    # solid: 塗りの形（Filled）で、閉じていない線でも塗りつぶす場所 / extra areas filled in the Filled form
    B[name] = {'ink': ink, 'tint': tint, 'knock': knock or [], 'sw': sw or SW_STD, 'ink16': ink16, 'solid': solid or [], 'hollow': hollow}

# 指示書の 6 種（原図どおり）/ the six from the sheet, as drawn
d('search', [L('M3.25 8.5a5.25 5.25 0 1 0 10.5 0a5.25 5.25 0 1 0-10.5 0Z'), L('M12.3 12.3l4 4')], sw=SW_SEARCH, hollow=True)   # 塗りの形でもレンズは輪のまま / lens stays a ring when filled
d('calendar', **cal())
d('folder', [L(FOLDER)], tint=P(FOLDER))
d('delete', [L('M2.75 5h14.5M7.5 5V2.75h5V5M4.75 5l.75 10.6a1.5 1.5 0 0 0 1.5 1.4h6a1.5 1.5 0 0 0 1.5-1.4L15.25 5')],
  solid=[P('M4.75 5l.75 10.6a1.5 1.5 0 0 0 1.5 1.4h6a1.5 1.5 0 0 0 1.5-1.4L15.25 5Z')])
d('warning', [L('M9.1 3.6a1.03 1.03 0 0 1 1.8 0l6.55 11.5a1.13 1.13 0 0 1-.98 1.65H3.53a1.13 1.13 0 0 1-.98-1.65L9.1 3.6Z'), L('M10 7.5v3.25'), DOT(10, 13.75)])
d('notification', [L('M8 15.75a2 2 0 0 0 4 0M10 3v1.25'), L(BELL)], tint=P(BELL),
  ink16=[L('M8.4 16.35a1.6 1.6 0 0 0 3.2 0M10 3v1.25'), L(BELL)])   # 16px は振り子を小さく下げる / smaller clapper at 16px

# 予定の仲間: 予定の枠の中（見出しの下、y 8〜17）に記号を置く / calendar family: mark inside the body
d('timetable', **cal(L('M3 12.5h14'), L('M7.75 8v9M12.25 8v9')))
d('deadline', **cal(L('M10 10v2.75l1.6 1'), L('M7 12.5a3 3 0 1 0 6 0a3 3 0 1 0-6 0Z')))
d('due-today', **cal(L('M10 10v2.6'), DOT(10, 14.75)))
d('tentative', **cal(L('M8.55 11.1a1.5 1.5 0 1 1 2.2 1.35c-.5.25-.75.6-.75 1.05'), DOT(10, 15.15, 0.8)))
d('canceled', **cal(L('M8.1 10.6l3.8 3.8M11.9 10.6l-3.8 3.8')))
d('repeat-weekly', **cal(L(arc(10, 12.6, 2.6, 300, 570)), L(head(10 + 2.6 * math.cos(math.radians(210)), 12.6 + 2.6 * math.sin(math.radians(210)), 120, 1.6))))
d('view-day', **cal(L('M6 11h8'), L('M6 14h5')))
d('view-week', **cal(L('M7.75 8v9M12.25 8v9')))
d('view-agenda', **cal(L('M6 10.75h1M9 10.75h5M6 14h1M9 14h5')))

# 書類・入れ物 / documents and containers
d('document', [L(DOC), L(DOC_FOLD)], tint=P(DOC))
d('submit', [L(DOC), L(DOC_FOLD), L('M9.75 15v-5.25'), L('M7.5 12l2.25-2.25L12 12')], tint=P(DOC))
d('exam', [L('M6.75 4.25H5A1.25 1.25 0 0 0 3.75 5.5V16A1.25 1.25 0 0 0 5 17.25h10A1.25 1.25 0 0 0 16.25 16V5.5A1.25 1.25 0 0 0 15 4.25h-1.75'),
           L(rr(6.75, 2.75, 6.5, 3, 0.9)), L('M6.75 11.25l2.25 2.25 4.25-4.5')],
  tint=P('M5 4.25h10a1.25 1.25 0 0 1 1.25 1.25V16A1.25 1.25 0 0 1 15 17.25H5A1.25 1.25 0 0 1 3.75 16V5.5A1.25 1.25 0 0 1 5 4.25Z'))
d('copy', [L(rr(6.75, 6.25, 10.5, 11, 1.25)), L('M3.25 13.5V4.25A1.25 1.25 0 0 1 4.5 3h8.75')], tint=rr(6.75, 6.25, 10.5, 11, 1.25))
d('mail', [L(rr(2.75, 4.25, 14.5, 11.5, 1.25)), L('M3.5 5.5L10 10.5l6.5-5')], tint=rr(2.75, 4.25, 14.5, 11.5, 1.25))
CHAT = 'M5 3.75h10a2 2 0 0 1 2 2v6.25a2 2 0 0 1-2 2H9.75l-3.5 3v-3H5a2 2 0 0 1-2-2V5.75a2 2 0 0 1 2-2Z'
d('chat', [L(CHAT)], tint=P(CHAT))
d('image', [L(rr(2.75, 3.75, 14.5, 12.5, 1.25)), L('M3.25 14.25l4.25-4.25 4 4 1.75-1.75 3.5 3.5'), L(circ(13.25, 7.5, 1.25))], tint=rr(2.75, 3.75, 14.5, 12.5, 1.25))
TAG = pl((10.6, 2.75), (16, 2.75), (17.25, 4), (17.25, 9.4), (9.75, 16.9), (8.9, 17.25), (8.05, 16.9), (3.1, 11.95), (2.75, 11.1), (3.1, 10.25), close=True)
d('tag', [L(TAG), L(circ(13.6, 6.4, 1.15))], tint=TAG)
d('save', [L('M4 2.75h9.25L17.25 6.75V16A1.25 1.25 0 0 1 16 17.25H4A1.25 1.25 0 0 1 2.75 16V4A1.25 1.25 0 0 1 4 2.75Z'), L('M6.25 17v-4.75h7.5V17'), L('M6.25 3v3.5h5.5V3')],
  tint=P('M4 2.75h9.25L17.25 6.75V16A1.25 1.25 0 0 1 16 17.25H4A1.25 1.25 0 0 1 2.75 16V4A1.25 1.25 0 0 1 4 2.75Z'))
PRINT_BODY = 'M6 14H4A1.25 1.25 0 0 1 2.75 12.75v-4.5A1.25 1.25 0 0 1 4 7h12a1.25 1.25 0 0 1 1.25 1.25v4.5A1.25 1.25 0 0 1 16 14h-2'
d('print', [L(PRINT_BODY), L('M6 7V3.75h8V7'), L(rr(6, 11.25, 8, 6, 0.75)), DOT(14.25, 9.5, 0.7)],
  tint=pathops.op(rr(2.75, 7, 14.5, 7, 1.25), rr(6, 11.25, 8, 6, 0.75), pathops.PathOp.DIFFERENCE, fix_winding=True))
d('briefcase', [L(rr(2.75, 6.25, 14.5, 10.75, 1.25)), L('M7.25 6.25V4.5a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1v1.75'), L('M3 10.75h14')], tint=rr(2.75, 6.25, 14.5, 10.75, 1.25))
d('shift-work', [L(rr(3, 3, 14, 14, 2.5)), L('M10 6.25V10l2.75 1.75')], tint=rr(3, 3, 14, 14, 2.5))
d('room-change', [L(rr(3.25, 2.75, 7.75, 14.5, 1.25)), DOT(8.75, 10.25, 0.8), L('M12.75 10h4.5'), L(head(17.25, 10, 0, 2.4))], tint=rr(3.25, 2.75, 7.75, 14.5, 1.25))
HOUSE = 'M4.5 8.25L10 3.5l5.5 4.75v7.75a1.25 1.25 0 0 1-1.25 1.25H5.75A1.25 1.25 0 0 1 4.5 16Z'
d('home', [L(HOUSE), L('M8.25 17.25v-4.5h3.5v4.5')], tint=P(HOUSE))
d('lock', [L(rr(4.25, 8.75, 11.5, 8.5, 1.25)), L('M6.75 8.75v-2.5a3.25 3.25 0 0 1 6.5 0v2.5'), DOT(10, 13, 1.0)], tint=rr(4.25, 8.75, 11.5, 8.5, 1.25))
FLAG = 'M4.75 3.75h10.5l-2.25 3.75 2.25 3.75H4.75Z'
d('flag', [L('M4.75 17.25V3.25'), L(FLAG)], tint=P(FLAG))
PIN_ = 'M10 17.25s5.5-4.9 5.5-9.25a5.5 5.5 0 0 0-11 0c0 4.35 5.5 9.25 5.5 9.25Z'
d('location', [L(PIN_), L(circ(10, 8, 2))], tint=P(PIN_))
CLOUD = 'M6 15.25h8.25a3.25 3.25 0 0 0 .35-6.48A4.75 4.75 0 0 0 5.6 8.1 3.6 3.6 0 0 0 6 15.25Z'
d('offline', [L(CLOUD), L('M3.5 3.5l13 13')], tint=P(CLOUD), knock=[pl((3.5, 3.5), (16.5, 16.5))])

# 人 / people
d('person', [L(circ(10, 6.5, 3.25)), L('M4.25 17c0-3 2.55-5 5.75-5s5.75 2 5.75 5')], solid=[P('M4.25 17c0-3 2.55-5 5.75-5s5.75 2 5.75 5Z')])
d('people', [L(circ(7.5, 7, 2.6)), L('M2.75 16.75c0-2.5 2.1-4.25 4.75-4.25s4.75 1.75 4.75 4.25'), L(circ(14, 6.25, 2.1)), L('M13.75 11.5c2.1 0 3.5 1.35 3.5 3.4')],
  solid=[P('M2.75 16.75c0-2.5 2.1-4.25 4.75-4.25s4.75 1.75 4.75 4.25Z')])

# 操作の記号（面なし）/ action marks, no tint
d('add', [L('M10 4v12M4 10h12')])
d('subtract', [L('M4 10h12')])
d('dismiss', [L('M5 5l10 10M15 5L5 15')])
d('check', [L('M4 10.5l4 4 8-9')])
d('chevron-down', [L('M5 7.5l5 5 5-5')])
d('chevron-up', [L('M5 12.5l5-5 5 5')])
d('chevron-left', [L('M12.5 5l-5 5 5 5')])
d('chevron-right', [L('M7.5 5l5 5-5 5')])
d('arrow-up', [L('M10 16.5v-13M5 8.5l5-5 5 5')])
d('arrow-down', [L('M10 3.5v13M5 11.5l5 5 5-5')])
d('arrow-left', [L('M16.5 10h-13M8.5 5l-5 5 5 5')])
d('arrow-right', [L('M3.5 10h13M11.5 5l5 5-5 5')])
d('sort', [L('M6.5 16V4M3.5 7l3-3 3 3'), L('M13.5 4v12M10.5 13l3 3 3-3')])
d('sort-up', [L('M6.25 16V4M3.25 7l3-3 3 3'), L('M11 14.5h2.5M11 10h4M11 5.5h5.5')])
d('sort-down', [L('M6.25 4v12M3.25 13l3 3 3-3'), L('M11 5.5h2.5M11 10h4M11 14.5h5.5')])
d('edit', [L('M13.1 3.6a1.65 1.65 0 0 1 2.35 0l.95.95a1.65 1.65 0 0 1 0 2.35L7.1 16.2l-3.6.85.85-3.6Z'), L('M11.75 5l3.25 3.25')])
d('filter', [L('M3.5 5.5h13M6 10h8M8.5 14.5h3')])
d('settings', [L(gear()), L(circ(10, 10, 2.4))])
d('more', [DOT(4.75, 10, 1.15), DOT(10, 10, 1.15), DOT(15.25, 10, 1.15)])
d('more-vertical', [DOT(10, 4.75, 1.15), DOT(10, 10, 1.15), DOT(10, 15.25, 1.15)])
d('drag', [DOT(7.5, 5, 1.05), DOT(12.5, 5, 1.05), DOT(7.5, 10, 1.05), DOT(12.5, 10, 1.05), DOT(7.5, 15, 1.05), DOT(12.5, 15, 1.05)])
d('menu', [L('M3.5 5.5h13M3.5 10h13M3.5 14.5h13')])
d('open-external', [L('M9 4.25H5.5A1.25 1.25 0 0 0 4.25 5.5v9a1.25 1.25 0 0 0 1.25 1.25h9a1.25 1.25 0 0 0 1.25-1.25V11'), L('M11.5 3.75h4.75V8.5M16 4l-6.25 6.25')])
d('link', [L('M8.25 6.5H6.5a3.5 3.5 0 0 0 0 7h1.75M11.75 6.5h1.75a3.5 3.5 0 0 1 0 7h-1.75M7 10h6')])
d('share', [L('M12.75 3.75l3.5 3.25-3.5 3.25'), L('M16 7h-5.25a4 4 0 0 0-4 4v1'), L('M4.25 8.5v6.75a1.25 1.25 0 0 0 1.25 1.25h9.25a1.25 1.25 0 0 0 1.25-1.25v-2')])
d('download', [L('M10 3.5v9.25M6 9l4 4 4-4'), L('M4 16.5h12')])
d('upload', [L('M10 13.25V4M6 7.75l4-4 4 4'), L('M4 16.5h12')])
d('star', [L(star())])
d('eye', [L('M2.5 10c1.8-3.6 4.4-5.5 7.5-5.5s5.7 1.9 7.5 5.5c-1.8 3.6-4.4 5.5-7.5 5.5S4.3 13.6 2.5 10Z'), L(circ(10, 10, 2.5))])
d('eye-off', [L('M2.5 10c1.8-3.6 4.4-5.5 7.5-5.5s5.7 1.9 7.5 5.5c-1.8 3.6-4.4 5.5-7.5 5.5S4.3 13.6 2.5 10Z'), L(circ(10, 10, 2.5)), L('M3.5 3.5l13 13')],
  knock=[pl((3.5, 3.5), (16.5, 16.5))])
d('help', [L(circ(10, 10, 7.25)), L('M8.1 8.1a1.95 1.95 0 1 1 2.85 1.75c-.6.3-.95.75-.95 1.4v.35'), DOT(10, 14.1)])
d('clock', [L(circ(10, 10, 7.25)), L('M10 6v4.25l2.75 1.75')])
d('sync', [L(arc(10, 10, 6.25, 200, 340)), L(head(10 + 6.25 * math.cos(math.radians(340)), 10 + 6.25 * math.sin(math.radians(340)), 70, 2.4)),
           L(arc(10, 10, 6.25, 20, 160)), L(head(10 + 6.25 * math.cos(math.radians(160)), 10 + 6.25 * math.sin(math.radians(160)), 250, 2.4))])
d('undo', [L('M7 4.5L3.75 7.75 7 11'), L('M4 7.75h7.5a4.75 4.75 0 0 1 0 9.5H8.5')])
d('history', [L(arc(10, 10, 7, 215, 505)), L(head(10 + 7 * math.cos(math.radians(215)), 10 + 7 * math.sin(math.radians(215)), 125, 2.4)), L('M10 6.5v3.75l2.5 1.5')])
PIN = pl((11.75, 3.25), (16.75, 8.25), (13.9, 9.35), (11, 12.25), (10.85, 15.15), (4.85, 9.15), (7.75, 9), (10.65, 6.1), close=True)
d('pin', [L(PIN), L('M7.85 12.15l-4.6 4.6')])
d('density-compact', [L('M3.5 3.5h13M3.5 6.75h13M3.5 10h13M3.5 13.25h13M3.5 16.5h13')])
d('density-regular', [L('M3.5 4.5h13M3.5 8.17h13M3.5 11.83h13M3.5 15.5h13')])
d('density-spacious', [L('M3.5 4h13M3.5 10h13M3.5 16h13')])

# ------------------------------------------------------------------ 輪郭にする / to outlines
def _op(a, b, k):
    return pathops.op(a, b, k, fix_winding=True, keep_starting_points=False)
def _stroke(p, w):
    q = pathops.Path(p); q.stroke(w, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4); q.convertConicsToQuads(); return q
def _union(ps):
    acc = pathops.Path()
    for p in ps: acc = _op(acc, p, pathops.PathOp.UNION)
    return acc

def outline(name, size):
    """(ink, tint) の pathops.Path を返す（20 の格子）/ ink and tint outlines on the 20 grid"""
    b = B[name]; w = b['sw'][size]
    ops = b['ink16'] if size == 16 and b.get('ink16') else b['ink']
    parts = []
    for o in ops:
        if o[0] == 'dot':
            r = o[3] + (0.15 if size == 16 else 0)      # 16px は点を少し大きく / slightly larger dots at 16px
            parts.append(circ(o[1], o[2], r))
        elif o[2] == 'line':
            parts.append(_stroke(o[1], w))
        else:
            parts.append(_op(o[1], pathops.Path(), pathops.PathOp.UNION))
    ink = _union(parts)
    tint = _op(b['tint'], pathops.Path(), pathops.PathOp.UNION) if b['tint'] is not None else None
    if b['knock']:
        # くり抜きは線 1 本分＋すき間（線の幅の 2.4 倍）/ knock-out = stroke width × 2.4
        k = _union([_stroke(s, w * 2.4) if not _closed(s) else s for s in b['knock']])
        ink = _op(ink, k, pathops.PathOp.DIFFERENCE)
        if tint is not None: tint = _op(tint, k, pathops.PathOp.DIFFERENCE)
        # くり抜いた後に、くり抜きに使った線そのもの（斜線など）を戻す / put the slash itself back
        back = [_stroke(s, w) for s in b['knock'] if not _closed(s) and _is_slash(name)]
        if back: ink = _union([ink] + back)
    return ink, tint

FILLED_K = 1.2   # 塗りの形では、外に出る線を 1.2 倍の太さにする / outer strokes 1.2x heavier in the Filled form

def _contours(shape):
    return list(shape.contours) if len(list(shape.contours)) > 1 else [shape]

def outline_filled(name, size):
    """B 案の塗りの形（Filled）。KM1-ICO-001 §8.6 / the B Filled form.
    1. 閉じた形（線の輪郭・淡い面・solid）は中まで塗る。
    2. ほかの閉じた形の中に収まる線と点は、通常の太さでくり抜く（白い線になる）。
    3. それ以外の線（外に出る線・操作の記号）は 1.2 倍の太さで塗る。
    4. 斜線のくり抜き（offline・eye-off）は通常の形と同じ。"""
    b = B[name]; w = b['sw'][size]
    ops = b['ink16'] if size == 16 and b.get('ink16') else b['ink']
    items = []   # (shape_for_inside_test, region_or_None, kind, payload)
    for o in ops:
        if o[0] == 'dot':
            r = o[3] + (0.15 if size == 16 else 0)
            c = circ(o[1], o[2], r)
            items.append({'test': c, 'region': None, 'draw': circ(o[1], o[2], r * FILLED_K), 'knock': c})   # 外の点は少し大きく / outer dots slightly larger
        elif o[2] == 'line':
            for c in _contours(o[1]):
                closed = _closed(c) and not b.get('hollow')
                reg = _union([_op(c, pathops.Path(), pathops.PathOp.UNION), _stroke(c, w * FILLED_K)]) if closed else None
                items.append({'test': _stroke(c, w), 'region': reg, 'draw': _stroke(c, w * FILLED_K), 'knock': _stroke(c, w)})
        else:
            sh = _op(o[1], pathops.Path(), pathops.PathOp.UNION)
            items.append({'test': sh, 'region': sh, 'draw': sh, 'knock': sh})
    extra = []
    if b['tint'] is not None: extra.append(_op(b['tint'], pathops.Path(), pathops.PathOp.UNION))
    for sv in b.get('solid', []): extra.append(_op(sv, pathops.Path(), pathops.PathOp.UNION))
    def inside(i):
        others = [it['region'] for j, it in enumerate(items) if j != i and it['region'] is not None] + extra
        if not others: return False
        # 自分の囲む範囲より大きい「ほかの形」の中にあるか / within a region other than its own
        own = items[i]['region']
        cands = [r for r in others if own is None or _area(r) > _area(own) * 1.05]
        if not cands: return False
        rest = _op(items[i]['test'], _union(cands), pathops.PathOp.DIFFERENCE)
        return _area(rest) < 0.02
    inner = [inside(i) for i in range(len(items))]
    base = _union([it['region'] for it in items if it['region'] is not None] + extra +
                  [it['draw'] for it, inn in zip(items, inner) if not inn])
    kn = [it['knock'] for it, inn in zip(items, inner) if inn]
    ink = _op(base, _union(kn), pathops.PathOp.DIFFERENCE) if kn else base
    # 内側の閉じた形の中身は塗ったまま戻す（輪だけ白く残す）/ refill inner closed shapes inside their ring
    for it, inn in zip(items, inner):
        if inn and it['region'] is not None:
            core = _op(it['region'], _stroke_outline_band(it, w), pathops.PathOp.DIFFERENCE)
            # 中にさらにくり抜く線があれば、それも保つ / keep knock-outs nested inside it
            nested = [x['knock'] for x, n2 in zip(items, inner) if n2 and x is not it and _area(_op(x['test'], it['region'], pathops.PathOp.DIFFERENCE)) < 0.02]
            if nested: core = _op(core, _union(nested), pathops.PathOp.DIFFERENCE)
            ink = _union([ink, core])
    if b['knock']:
        k = _union([_stroke(s_, w * 2.4) if not _closed(s_) else s_ for s_ in b['knock']])
        ink = _op(ink, k, pathops.PathOp.DIFFERENCE)
        back = [_stroke(s_, w * FILLED_K) for s_ in b['knock'] if not _closed(s_) and _is_slash(name)]
        if back: ink = _union([ink] + back)
    return ink

def _stroke_outline_band(it, w):
    return it['knock']

def _area(p):
    try: return abs(p.area)
    except Exception: return 0.0

def _closed(p):
    return any(v == 'closePath' for v, _ in p.segments)
def _is_slash(name):
    return name in ('offline', 'eye-off', 'notification-off')

# ------------------------------------------------------------------ 追加 1（2026-11-14）/ additions 1
# お店・会計（kami2pos）/ shop and checkout
CART_BASKET = pl((5.4, 6.25), (16.5, 6.25), (14.6, 12.75), (6.7, 12.75), close=True)
d('cart', [L('M2.75 3.5h1.9l2.05 9.25h7.9'), L(CART_BASKET), L(circ(7.75, 15.75, 1.2)), L(circ(13.75, 15.75, 1.2))], tint=CART_BASKET)
RECEIPT = 'M5 2.75h10v14.5l-1.65-1.1-1.65 1.1-1.7-1.1-1.65 1.1-1.65-1.1L5 17.25Z'
d('receipt', [L(RECEIPT), L('M7.5 6.5h5M7.5 9.5h5M7.5 12.5h3')], tint=P(RECEIPT))
STORE_BODY = 'M4.25 9.25v8h11.5v-8'
d('store', [L('M3 7.25L4.25 3.25h11.5L17 7.25'), L('M3 7.25a2.33 2.33 0 0 0 4.67 0a2.33 2.33 0 0 0 4.66 0a2.33 2.33 0 0 0 4.67 0'), L(STORE_BODY), L('M8.25 17.25v-4h3.5v4')],
  tint=P('M4.25 9.25h11.5v8H4.25Z'))
BOX = pl((10, 2.75), (16.5, 6), (16.5, 14), (10, 17.25), (3.5, 14), (3.5, 6), close=True)
d('product', [L(BOX), L('M3.75 6.15L10 9.25l6.25-3.1'), L('M10 9.25v7.75')], tint=BOX)
d('discount', [L(TAG), L(circ(13.6, 6.4, 1.15)), L('M7.6 13.4l4.3-4.3'), DOT(8.1, 9.6, 0.9), DOT(11.6, 13.1, 0.9)], tint=TAG)
d('money', [L(rr(2.75, 5, 14.5, 10, 1.25)), L(circ(10, 10, 2.25)), DOT(5.6, 10, 0.75), DOT(14.4, 10, 0.75)], tint=rr(2.75, 5, 14.5, 10, 1.25))
d('wallet', [L(rr(2.75, 5.25, 14.5, 11.5, 1.5)), L('M4 5.4l9.3-2.3a1 1 0 0 1 1.2.95v1.2'), L(rr(12, 9, 5.25, 3.75, 1)), DOT(14.25, 10.875, 0.65)], tint=rr(2.75, 5.25, 14.5, 11.5, 1.5))
d('payment-card', [L(rr(2.75, 4.75, 14.5, 10.5, 1.25)), L('M3 8h14'), L('M5.5 12.25h3')], tint=rr(2.75, 4.75, 14.5, 10.5, 1.25))
d('qr-code', [L(rr(3, 3, 5, 5, 1)), L(rr(12, 3, 5, 5, 1)), L(rr(3, 12, 5, 5, 1)), DOT(5.5, 5.5, 0.9), DOT(14.5, 5.5, 0.9), DOT(5.5, 14.5, 0.9),
              DOT(12.7, 12.7, 0.8), DOT(16.3, 12.7, 0.8), DOT(12.7, 16.3, 0.8), DOT(16.3, 16.3, 0.8), DOT(14.5, 14.5, 0.8)])
TICKET = 'M3 5.25h14v3a1.75 1.75 0 0 0 0 3.5v3H3v-3a1.75 1.75 0 0 0 0-3.5Z'
d('ticket', [L(TICKET), L('M7.5 8.75h5M7.5 11.25h5')], tint=P(TICKET))
d('waiting', [L('M5.5 2.75h9M5.5 17.25h9'), L('M6.5 2.75v2.5c0 1.75 3.5 3.25 3.5 4.75s-3.5 3-3.5 4.75v2.5M13.5 2.75v2.5c0 1.75-3.5 3.25-3.5 4.75s3.5 3 3.5 4.75v2.5'),
              F(pl((8.1, 16.3), (11.9, 16.3), (10, 14.4), close=True))])
d('calculator', [L(rr(4, 2.75, 12, 14.5, 1.5)), L(rr(6.25, 5, 7.5, 3, 0.6))] + [DOT(x, y, 0.85) for y in (11, 14.25) for x in (7, 10, 13)], tint=rr(4, 2.75, 12, 14.5, 1.5))
d('barcode-scan', [L('M3 6.5V4.25A1.25 1.25 0 0 1 4.25 3H6.5M13.5 3h2.25A1.25 1.25 0 0 1 17 4.25V6.5M17 13.5v2.25A1.25 1.25 0 0 1 15.75 17H13.5M6.5 17H4.25A1.25 1.25 0 0 1 3 15.75V13.5'),
                   L('M7 6.75v6.5M10 6.75v6.5M13 6.75v6.5')])
# 予定 / schedule
d('calendar-add', **cal(L('M10 10v5M7.5 12.5h5')))
d('reminder', [L(circ(10, 10.75, 6)), L('M10 7.75v3l2 1.25'), L('M3.25 5.25l2.5-2.25M16.75 5.25l-2.5-2.25')])
NOTE = 'M4.25 3h11.5A1.25 1.25 0 0 1 17 4.25V12l-5 5H4.25A1.25 1.25 0 0 1 3 15.75V4.25A1.25 1.25 0 0 1 4.25 3Z'
d('note', [L(NOTE), L('M12 17v-3.75A1.25 1.25 0 0 1 13.25 12H17'), L('M6 7h8M6 10h5')], tint=P(NOTE))
# やりとり・共通 / communication and common
d('attach', [L('M15.5 9.25l-5.6 5.6a3.25 3.25 0 0 1-4.6-4.6l6.1-6.1a2.15 2.15 0 0 1 3.05 3.05l-5.85 5.85a1.05 1.05 0 0 1-1.5-1.5l5.15-5.15')])
PLANE = pl((3, 3.25), (17.25, 10), (3, 16.75), (5.25, 10), close=True)
d('send', [L(PLANE), L('M5.25 10h5.5')], tint=PLANE)
d('phone', [L('M6.4 3h-2a1.25 1.25 0 0 0-1.25 1.35C3.8 11.3 8.7 16.2 15.65 16.85A1.25 1.25 0 0 0 17 15.6v-2l-3.4-1.4-1.75 1.75a10 10 0 0 1-5.7-5.7L7.9 6.5Z')])
d('globe', [L(circ(10, 10, 7.25)), L('M10 2.75c-2 2-3 4.5-3 7.25s1 5.25 3 7.25M10 2.75c2 2 3 4.5 3 7.25s-1 5.25-3 7.25'), L('M3 10h14')])
CAM = 'M7.25 4.25h5.5l1.25 2h2A1.25 1.25 0 0 1 17.25 7.5v7.25A1.25 1.25 0 0 1 16 16H4a1.25 1.25 0 0 1-1.25-1.25V7.5A1.25 1.25 0 0 1 4 6.25h2Z'
d('camera', [L(CAM), L(circ(10, 11, 2.75))], tint=P(CAM))
d('person-add', [L(circ(8.5, 6.5, 3)), L('M3 17c0-2.9 2.45-4.75 5.5-4.75 1.1 0 2.1.25 2.95.7'), L('M15 11.5v5.5M12.25 14.25h5.5')],
  solid=[P('M3 17c0-2.9 2.45-4.75 5.5-4.75 1.1 0 2.1.25 2.95.7V17Z')])
d('sign-out', [L('M8.5 3H5A1.25 1.25 0 0 0 3.75 4.25v11.5A1.25 1.25 0 0 0 5 17h3.5'), L('M8 10h9M13.75 6.5L17.25 10l-3.5 3.5')])
d('sign-in', [L('M11.5 3H15a1.25 1.25 0 0 1 1.25 1.25v11.5A1.25 1.25 0 0 1 15 17h-3.5'), L('M3 10h9M8.75 6.5L12.25 10 8.75 13.5')])
d('refresh', [L(arc(10, 10, 6.5, 330, 600)), L(head(10 + 6.5 * math.cos(math.radians(600)), 10 + 6.5 * math.sin(math.radians(600)), 690, 2.4))])
d('list', [DOT(4.25, 5.5, 1.1), DOT(4.25, 10, 1.1), DOT(4.25, 14.5, 1.1), L('M7.5 5.5h9M7.5 10h9M7.5 14.5h9')])
d('grid', [L(rr(3, 3, 5.75, 5.75, 1.25)), L(rr(11.25, 3, 5.75, 5.75, 1.25)), L(rr(3, 11.25, 5.75, 5.75, 1.25)), L(rr(11.25, 11.25, 5.75, 5.75, 1.25))])
d('table', [L(rr(2.75, 3.5, 14.5, 13, 1.25)), L('M3 8h14M3 12.25h14M8 8v8.25')])
BARS = [rr(3.5, 10, 3, 7, 0.75), rr(8.5, 3.5, 3, 13.5, 0.75), rr(13.5, 7.5, 3, 9.5, 0.75)]
d('chart', [L(b_) for b_ in BARS])
BOOKMARK = 'M5.5 2.75h9a1.25 1.25 0 0 1 1.25 1.25v13l-5.75-3.75L4.25 17V4A1.25 1.25 0 0 1 5.5 2.75Z'
d('bookmark', [L(BOOKMARK)], tint=P(BOOKMARK))
d('heart', [L('M10 16.5S3 12.4 3 7.6A3.6 3.6 0 0 1 10 6.4a3.6 3.6 0 0 1 7 1.2c0 4.8-7 8.9-7 8.9Z')])
d('cloud', [L(CLOUD)], tint=P(CLOUD))
d('wifi', [L('M3 8.25a10 10 0 0 1 14 0M5.6 10.9a6.3 6.3 0 0 1 8.8 0M8.2 13.5a2.6 2.6 0 0 1 3.6 0'), DOT(10, 16, 1.05)])
d('light-mode', [L(circ(10, 10, 3.25))] + [L(pl((10 + 5.25 * math.cos(math.radians(a)), 10 + 5.25 * math.sin(math.radians(a))), (10 + 7 * math.cos(math.radians(a)), 10 + 7 * math.sin(math.radians(a))))) for a in range(0, 360, 45)])
d('dark-mode', [L('M16.25 12.25A6.75 6.75 0 0 1 7.75 3.75a6.75 6.75 0 1 0 8.5 8.5Z')])
d('keyboard', [L(rr(2.75, 5, 14.5, 10, 1.25)), L('M7 12.5h6')] + [DOT(x, 8.25, 0.75) for x in (5.75, 8.75, 11.25, 14.25)], tint=rr(2.75, 5, 14.5, 10, 1.25))
d('zoom-in', [L('M3.25 8.5a5.25 5.25 0 1 0 10.5 0a5.25 5.25 0 1 0-10.5 0Z'), L('M12.3 12.3l4 4'), L('M8.5 6.25v4.5M6.25 8.5h4.5')], sw=SW_SEARCH)
d('zoom-out', [L('M3.25 8.5a5.25 5.25 0 1 0 10.5 0a5.25 5.25 0 1 0-10.5 0Z'), L('M12.3 12.3l4 4'), L('M6.25 8.5h4.5')], sw=SW_SEARCH)
d('expand', [L('M11.5 3h5.5v5.5M17 3l-5.5 5.5'), L('M8.5 17H3v-5.5M3 17l5.5-5.5')])
d('collapse', [L('M3.25 16.75l5-5M4.75 11.75h3.5v3.5'), L('M16.75 3.25l-5 5M11.75 4.75v3.5h3.5')])
d('play', [L(pl((6, 3.75), (16.25, 10), (6, 16.25), close=True))])
d('pause', [L(rr(5, 3.75, 3, 12.5, 0.75)), L(rr(12, 3.75, 3, 12.5, 0.75))])
d('mic', [L(rr(7.25, 2.75, 5.5, 9.25, 2.75)), L('M4.75 9.25a5.25 5.25 0 0 0 10.5 0'), L('M10 14.5v2.75M7.25 17.25h5.5')], tint=rr(7.25, 2.75, 5.5, 9.25, 2.75))
SPK = 'M3 7.75h2.75L9.75 4.25v11.5l-4-3.5H3Z'
d('volume', [L(SPK), L('M12.75 7.25a3.75 3.75 0 0 1 0 5.5M14.75 5a7 7 0 0 1 0 10')], tint=P(SPK))
MAP = pl((2.75, 4.75), (7.25, 3), (12.75, 4.75), (17.25, 3), (17.25, 15.25), (12.75, 17), (7.25, 15.25), (2.75, 17), close=True)
d('map', [L(MAP), L('M7.25 3v12.25M12.75 4.75V17')], tint=MAP)
d('building', [L(rr(4.25, 2.75, 11.5, 14.5, 1.25)), L('M8.5 17.25v-3.5h3v3.5')] + [DOT(x, y, 0.75) for y in (6, 9.25) for x in (7.25, 10, 12.75)], tint=rr(4.25, 2.75, 11.5, 14.5, 1.25))
CAP = pl((10, 4), (17.5, 7.75), (10, 11.5), (2.5, 7.75), close=True)
d('school', [L(CAP), L('M5.5 9.5v3.5c1.5 1.4 2.9 2 4.5 2s3-.6 4.5-2V9.5'), L('M17.5 7.75v4.75')], tint=CAP)
BOOK = 'M5.5 2.75H16v11.5H5.25A1.25 1.25 0 0 0 4 15.5V4.25A1.5 1.5 0 0 1 5.5 2.75Z'
d('book', [L(BOOK), L('M4 15.5a1.75 1.75 0 0 0 1.75 1.75H16'), L('M7.5 6.25h5')], tint=P(BOOK))
d('redo', [L('M13 4.5l3.25 3.25L13 11'), L('M16 7.75H8.5a4.75 4.75 0 0 0 0 9.5h3')])
CLIP_BODY = 'M5 4.25h10a1.25 1.25 0 0 1 1.25 1.25V16A1.25 1.25 0 0 1 15 17.25H5A1.25 1.25 0 0 1 3.75 16V5.5A1.25 1.25 0 0 1 5 4.25Z'
d('paste', [L('M6.75 4.25H5A1.25 1.25 0 0 0 3.75 5.5V16A1.25 1.25 0 0 0 5 17.25h10A1.25 1.25 0 0 0 16.25 16V5.5A1.25 1.25 0 0 0 15 4.25h-1.75'),
            L(rr(6.75, 2.75, 6.5, 3, 0.9)), L('M7 10.25h6M7 13.5h4')], tint=P(CLIP_BODY))
d('select-all', [L(rr(3, 3, 14, 14, 2)), L('M6.75 10.25l2.25 2.25 4.25-4.5')])
d('key', [L(circ(6.75, 13.25, 3.5)), L('M9.25 10.75l7-7'), L('M14.25 5.75l2 2M12.25 7.75l1.5 1.5')])
SHIELD = 'M10 2.75l6.25 2.25v4.5c0 3.9-2.6 6.6-6.25 7.75C6.35 16.1 3.75 13.4 3.75 9.5V5Z'
d('shield', [L(SHIELD)], tint=P(SHIELD))
FOPEN = 'M2.75 15.5l2.45-6.2a1.25 1.25 0 0 1 1.15-.8h10.9a.75.75 0 0 1 .7 1.02l-2.2 5.68a1.25 1.25 0 0 1-1.15.8H3.5a.75.75 0 0 1-.75-.5Z'
d('folder-open', [L('M2.75 15V5.5A1.25 1.25 0 0 1 4 4.25h3.5l2 2H15A1.25 1.25 0 0 1 16.25 7.5v1'), L(FOPEN)], tint=P(FOPEN))
ARCH = 'M4 7v8.75A1.25 1.25 0 0 0 5.25 17h9.5A1.25 1.25 0 0 0 16 15.75V7Z'
d('archive', [L(rr(2.75, 3.5, 14.5, 3.5, 1)), L(ARCH), L('M8 10.5h4')], tint=P(ARCH))
d('contact-card', [L(rr(2.75, 4, 14.5, 12, 1.25)), L(circ(7.25, 8.75, 1.75)), L('M4.75 13.5c.4-1.4 1.3-2.1 2.5-2.1s2.1.7 2.5 2.1'), L('M11.5 8.5h3.5M11.5 11.5h3.5')],
  tint=rr(2.75, 4, 14.5, 12, 1.25))
d('bus', [L(rr(4, 2.75, 12, 12.5, 2)), L('M4.25 9h11.5'), L('M6.5 15.25v2M13.5 15.25v2'), DOT(7, 12.25, 0.8), DOT(13, 12.25, 0.8)], tint=rr(4, 2.75, 12, 12.5, 2))
WCLOUD = 'M7.75 16.25h6.5a2.75 2.75 0 0 0 .3-5.48A3.75 3.75 0 0 0 7.5 11.25a2.5 2.5 0 0 0 .25 5Z'
d('weather', [L(circ(7, 6.75, 2.5)), L(WCLOUD)] + [L(pl((7 + 3.75 * math.cos(math.radians(a)), 6.75 + 3.75 * math.sin(math.radians(a))), (7 + 4.75 * math.cos(math.radians(a)), 6.75 + 4.75 * math.sin(math.radians(a))))) for a in (180, 225, 270, 315)],
  tint=P(WCLOUD))

# ------------------------------------------------------------------ Alert の状態の記号（2026-11-14）/ Alert status symbols
# 円の記号なので淡い面は付けない。形で区別する（お知らせ i・完了 ✓・注意 三角・エラー !）。色は使う側（info-ink など）。
# Circle symbols, no tint; told apart by shape (i, check, triangle, !); color comes from the status ink.
RING = circ(10, 10, 7.25)
d('status-info', [L(RING), L('M10 9.25v4.75'), DOT(10, 6.6, 0.95)])
d('status-success', [L(RING), L('M6.75 10.25l2.25 2.25 4.25-4.5')])
d('status-warning', [L('M9.1 3.6a1.03 1.03 0 0 1 1.8 0l6.55 11.5a1.13 1.13 0 0 1-.98 1.65H3.53a1.13 1.13 0 0 1-.98-1.65L9.1 3.6Z'), L('M10 7.5v3.25'), DOT(10, 13.75)])
d('status-error', [L(RING), L('M10 6.25v4.5'), DOT(10, 13.6, 0.95)])

# ------------------------------------------------------------------ 追加 2（2026-11-14、利用先の調査から）/ additions 2
d('task-list', [L('M3 5.1l1.5 1.5 2.75-3'), L(circ(5, 10.25, 1.6)), L(circ(5, 15.25, 1.6)), L('M9.75 5h7.25M9.75 10.25h7.25M9.75 15.25h7.25')])
d('notification-off', [L('M8 15.75a2 2 0 0 0 4 0M10 3v1.25'), L(BELL), L('M3.5 3.5l13 13')], tint=P(BELL), knock=[pl((3.5, 3.5), (16.5, 16.5))])
d('lock-open', [L(rr(4.25, 8.75, 11.5, 8.5, 1.25)), L('M6.75 8.75v-2.5a3.25 3.25 0 0 1 6.3-1.1'), DOT(10, 13, 1.0)], tint=rr(4.25, 8.75, 11.5, 8.5, 1.25))
d('timer', [L(circ(10, 11, 6)), L('M10 11V7.75'), L('M8.25 2.75h3.5M10 2.75V5'), L('M15 5.75l1.25-1.25')])
d('sparkle', [L('M8.5 4.5c.6 3 1.9 4.4 5 5-3.1.6-4.4 2-5 5-.6-3-1.9-4.4-5-5 3.1-.6 4.4-2 5-5Z'),
              L('M15 2.75c.25 1.1.75 1.6 1.85 1.85-1.1.25-1.6.75-1.85 1.85-.25-1.1-.75-1.6-1.85-1.85 1.1-.25 1.6-.75 1.85-1.85Z')])
d('view-month', **cal(*[DOT(x, y, 0.8) for y in (11, 14.25) for x in (6.5, 10, 13.5)]))
d('text-size', [L('M2.75 16l4.5-12 4.5 12M4.4 11.75h5.7'), L('M12 16l2.6-7 2.6 7M13 13.6h3.2')])
d('filter-dismiss', [L('M3.5 5.5h13M6 10h4.5M8.5 14.5h1.5'), L('M12.75 10.75l4 4M16.75 10.75l-4 4')])
