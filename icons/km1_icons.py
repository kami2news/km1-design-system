"""KM1 のアイコンを作る / Build the KM1 icon set (KM1-ICO-001)

独自のアイコンは「線と面の組み立て」で書き、ここで塗りの輪郭（1 本のパス）にする。
Fluent System Icons（MIT）から取り込むものは、KM1 の名前を付けてそのまま使う。

使い方 / Usage:
  python3 km1_icons.py <Fluent の svg-icons の icons フォルダ> <出力フォルダ>
出力 / Output: km1-icons.json（全部の形）、svg/（1 つずつ）、sprite-20.svg
必要なもの / Needs: skia-pathops, fonttools
"""
import json, math, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

# ---------------------------------------------------------------- 形 / shapes (20px の格子 / on the 20px grid)
def P(d):
    p = pathops.Path(); parse_path(d, p.getPen()); return p
def rect(x, y, w, h, r=0):
    if r <= 0: return P(f'M{x} {y}h{w}v{h}h{-w}z')
    return P(f'M{x+r} {y}h{w-2*r}a{r} {r} 0 0 1 {r} {r}v{h-2*r}a{r} {r} 0 0 1 {-r} {r}h{-(w-2*r)}a{r} {r} 0 0 1 {-r} {-r}v{-(h-2*r)}a{r} {r} 0 0 1 {r} {-r}z')
def circle(cx, cy, r):
    return P(f'M{cx-r} {cy}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0z')
def line(*pts):
    return P('M' + 'L'.join(f'{x} {y}' for x, y in pts))
def poly(*pts):
    return P('M' + 'L'.join(f'{x} {y}' for x, y in pts) + 'Z')
def octagon(cx, cy, r):
    pts = [(cx + r * math.cos(math.radians(22.5 + 45 * i)), cy + r * math.sin(math.radians(22.5 + 45 * i))) for i in range(8)]
    return poly(*[(round(x, 3), round(y, 3)) for x, y in pts])
def arc(cx, cy, r, a0, a1):
    """a0 から a1 まで（度、時計回り）/ clockwise arc in degrees"""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return P(f'M{x0:.3f} {y0:.3f}A{r} {r} 0 {large} 1 {x1:.3f} {y1:.3f}')

def stroked(p, w):
    q = pathops.Path(p); q.stroke(w, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4); q.convertConicsToQuads(); return q
def op(a, b, kind):
    return pathops.op(a, b, kind, fix_winding=True, keep_starting_points=False)
def build(ops, sw):
    """ops: [('+'|'-', shape, 'line'|'fill', clip?)] を順に合成 / combine in order"""
    acc = pathops.Path()
    for o in ops:
        sign, shape, mode = o[0], o[1], o[2]
        s = stroked(shape, sw) if mode == 'line' else pathops.Path(shape)
        if mode == 'fill':
            s = op(s, pathops.Path(), pathops.PathOp.UNION)
        if len(o) > 3 and o[3] is not None:
            s = op(s, o[3], pathops.PathOp.INTERSECTION)
        acc = op(acc, s, pathops.PathOp.UNION if sign == '+' else pathops.PathOp.DIFFERENCE)
    return acc

# ---------------------------------------------------------------- 独自のアイコン / Original KM1 icons
# 線の中心は .5 の位置（1px の線が画素にそろう）。生きている範囲は 2〜18、枠は 3〜17。
# Stroke centres sit on .5 so 1px lines align to pixels. Live area 2–18; frames 3–17.
ORIG = {}
def define(name, ja, en, reg, fil):
    ORIG[name] = {'ja': ja, 'en': en, 'regular': reg, 'filled': fil}

# KM1 が描くのは Fluent に同じ意味のものがないときだけ。描くときは Fluent の絵（ここでは予定の枠）を土台にし、
# 中身を Fluent と同じ細さ・同じ密度で足す。記号だけの新しい形は作らない。
# KM1 draws only where Fluent has no equivalent, building on a Fluent pictogram with details at Fluent's weight.
FL = None   # Fluent の icons フォルダ（main で設定）/ set in main
def fluent(name, size=20, v='regular'):
    return P(' '.join(re.findall(r' d="([^"]+)"', open(f'{FL}/{name}_{size}_{v}.svg').read())))

CELLS = [rect(x, y, 2.25, 1.75, 0.5) for y in (8.75, 12.25) for x in (5.25, 8.875, 12.5)]   # 曜日 × 時限のマス / weekday × period cells
def scaled(p, k):
    q = pathops.Path(); p.draw(TransformPen(q.getPen(), (k, 0, 0, k, 0, 0))); return q
def timetable(v, size=20):
    base = scaled(fluent('calendar_empty', size, v), 20 / size)   # その大きさの Fluent の枠を 20 の格子に / Fluent frame of that size, on the 20 grid
    if v == 'regular':
        return [('+', base, 'fill')] + [('+', c_, 'fill') for c_ in CELLS]
    return [('+', base, 'fill')] + [('-', c_, 'fill') for c_ in CELLS]
LAZY = {'timetable': ('時間割', 'Timetable', timetable)}

# ---------------------------------------------------------------- 取り込み / Imported from Fluent System Icons (MIT)
IMPORT = {  # KM1 の名前: (Fluent の名前, 日本語, English)
 'add': ('add', '追加', 'Add'), 'subtract': ('subtract', '減らす', 'Subtract'), 'dismiss': ('dismiss', '閉じる', 'Dismiss'),
 'check': ('checkmark', 'チェック', 'Check'), 'chevron-down': ('chevron_down', '下へ', 'Chevron down'), 'chevron-up': ('chevron_up', '上へ', 'Chevron up'),
 'chevron-left': ('chevron_left', '前へ', 'Chevron left'), 'chevron-right': ('chevron_right', '次へ', 'Chevron right'),
 'arrow-up': ('arrow_up', '上向きの矢印', 'Arrow up'), 'arrow-down': ('arrow_down', '下向きの矢印', 'Arrow down'),
 'arrow-left': ('arrow_left', '戻る', 'Arrow left'), 'arrow-right': ('arrow_right', '進む', 'Arrow right'),
 'sort': ('arrow_sort', '並べ替え', 'Sort'), 'sort-up': ('arrow_sort_up', '昇順', 'Sort ascending'), 'sort-down': ('arrow_sort_down', '降順', 'Sort descending'),
 'edit': ('edit', '編集', 'Edit'), 'delete': ('delete', '削除', 'Delete'), 'copy': ('copy', '複製', 'Copy'), 'search': ('search', '検索', 'Search'),
 'filter': ('filter', '絞り込み', 'Filter'), 'settings': ('settings', '設定', 'Settings'), 'more': ('more_horizontal', 'その他の操作', 'More'),
 'more-vertical': ('more_vertical', 'その他の操作（縦）', 'More (vertical)'), 'drag': ('re_order_dots_vertical', '並べ替えのつまみ', 'Drag handle'),
 'menu': ('navigation', 'メニュー', 'Menu'), 'home': ('home', 'ホーム', 'Home'), 'open-external': ('open', '別のタブで開く', 'Open externally'),
 'link': ('link', 'リンク', 'Link'), 'share': ('share', '共有', 'Share'), 'save': ('save', '保存', 'Save'), 'download': ('arrow_download', 'ダウンロード', 'Download'),
 'upload': ('arrow_upload', 'アップロード', 'Upload'), 'document': ('document', '文書', 'Document'), 'folder': ('folder', 'フォルダー', 'Folder'),
 'image': ('image', '画像', 'Image'), 'tag': ('tag', 'タグ', 'Tag'), 'person': ('person', '人', 'Person'), 'people': ('people', '人たち', 'People'),
 'mail': ('mail', 'メール', 'Mail'), 'chat': ('chat', 'チャット', 'Chat'), 'notification': ('alert', '通知', 'Notification'), 'star': ('star', 'お気に入り', 'Favorite'),
 'eye': ('eye', '表示', 'Show'), 'eye-off': ('eye_off', '非表示', 'Hide'), 'lock': ('lock_closed', 'ロック', 'Locked'),
 'help': ('question_circle', 'ヘルプ', 'Help'), 'warning': ('warning', '警告', 'Warning'), 'calendar': ('calendar_ltr', '予定', 'Calendar'),
 'clock': ('clock', '時刻', 'Time'), 'flag': ('flag', '旗', 'Flag'), 'location': ('location', '場所', 'Location'), 'offline': ('cloud_off', 'オフライン', 'Offline'),
 'sync': ('arrow_sync', '同期', 'Sync'), 'undo': ('arrow_undo', '元に戻す', 'Undo'), 'history': ('history', '履歴', 'History'), 'print': ('print', '印刷', 'Print'),
 'pin': ('pin', 'ピン留め', 'Pin'), 'briefcase': ('briefcase', '仕事', 'Work'),
 # 予定・時間割・締め切り / schedule
 'deadline': ('calendar_clock', '締め切り', 'Deadline'), 'due-today': ('calendar_error', '今日が期限', 'Due today'),
 'tentative': ('calendar_question_mark', '仮の予定', 'Tentative'), 'canceled': ('calendar_cancel', '休講・中止', 'Canceled'),
 'repeat-weekly': ('calendar_arrow_repeat_all', '毎週くり返す', 'Repeats weekly'), 'view-day': ('calendar_day', '日の表示', 'Day view'),
 'view-week': ('calendar_work_week', '週の表示', 'Week view'), 'view-agenda': ('calendar_agenda', '予定の一覧', 'Agenda view'),
 'shift-work': ('shifts', '勤務・バイト', 'Shift work'), 'room-change': ('door_arrow_right', '教室の変更', 'Room change'),
 'submit': ('document_arrow_up', '提出', 'Submit'), 'exam': ('clipboard_task', '試験', 'Exam'),
 # 状態の記号 / status
 'status-info': ('info', 'お知らせ', 'Information'), 'status-success': ('checkmark_circle', '完了', 'Success'),
 'status-warning': ('warning', '注意', 'Warning'), 'status-error': ('error_circle', 'エラー', 'Error'),
 # 密度 / density
 'density-compact': ('line_horizontal_5', '密度: 詰める', 'Density: compact'), 'density-regular': ('line_horizontal_4', '密度: 標準', 'Density: regular'),
 'density-spacious': ('line_horizontal_3', '密度: ゆったり', 'Density: spacious'),
 # 追加 1（2026-11-14）/ additions 1
 'cart': ('cart', 'カート', 'Cart'), 'receipt': ('receipt', 'レシート', 'Receipt'), 'store': ('building_shop', '店', 'Store'),
 'product': ('box', '商品', 'Product'), 'discount': ('tag_percent', '割引', 'Discount'), 'money': ('money', 'お金', 'Money'),
 'wallet': ('wallet', '財布', 'Wallet'), 'payment-card': ('payment', 'カード払い', 'Card payment'), 'qr-code': ('qr_code', 'QR コード', 'QR code'),
 'ticket': ('ticket_diagonal', '整理券', 'Ticket'), 'waiting': ('hourglass_half', '待ち', 'Waiting'), 'calculator': ('calculator', '電卓', 'Calculator'),
 'barcode-scan': ('barcode_scanner', 'バーコードを読む', 'Scan barcode'), 'calendar-add': ('calendar_add', '予定を追加', 'Add event'),
 'reminder': ('clock_alarm', 'リマインダー', 'Reminder'), 'note': ('note', 'メモ', 'Note'), 'attach': ('attach', '添付', 'Attach'),
 'send': ('send', '送信', 'Send'), 'phone': ('call', '電話', 'Phone'), 'globe': ('globe', 'Web・言語', 'Globe'), 'camera': ('camera', 'カメラ', 'Camera'),
 'person-add': ('person_add', '人を追加', 'Add person'), 'sign-out': ('sign_out', 'ログアウト', 'Sign out'), 'sign-in': ('arrow_enter', 'ログイン', 'Sign in'),
 'refresh': ('arrow_clockwise', '再読み込み', 'Refresh'), 'list': ('list', 'リスト', 'List'), 'grid': ('grid', 'グリッド', 'Grid'), 'table': ('table', '表', 'Table'),
 'chart': ('data_bar_vertical', 'グラフ', 'Chart'), 'bookmark': ('bookmark', 'しおり', 'Bookmark'), 'heart': ('heart', 'いいね', 'Like'),
 'cloud': ('cloud', 'クラウド', 'Cloud'), 'wifi': ('wifi_1', 'Wi-Fi', 'Wi-Fi'), 'light-mode': ('weather_sunny', 'ライト', 'Light mode'),
 'dark-mode': ('weather_moon', 'ダーク', 'Dark mode'), 'keyboard': ('keyboard', 'キーボード', 'Keyboard'), 'zoom-in': ('zoom_in', '拡大', 'Zoom in'),
 'zoom-out': ('zoom_out', '縮小', 'Zoom out'), 'expand': ('arrow_maximize', '広げる', 'Expand'), 'collapse': ('arrow_minimize', '縮める', 'Collapse'),
 'play': ('play', '再生', 'Play'), 'pause': ('pause', '一時停止', 'Pause'), 'mic': ('mic', 'マイク', 'Microphone'), 'volume': ('speaker_2', '音量', 'Volume'),
 'map': ('map', '地図', 'Map'), 'building': ('building', '建物', 'Building'), 'school': ('hat_graduation', '学校', 'School'), 'book': ('book', '本', 'Book'),
 'redo': ('arrow_redo', 'やり直す', 'Redo'), 'paste': ('clipboard_paste', '貼り付け', 'Paste'), 'select-all': ('select_all_on', 'すべて選択', 'Select all'),
 'key': ('key', '鍵・パスワード', 'Key'), 'shield': ('shield', '保護', 'Shield'), 'folder-open': ('folder_open', '開いたフォルダー', 'Open folder'),
 'archive': ('archive', 'アーカイブ', 'Archive'), 'contact-card': ('contact_card', '連絡先', 'Contact'), 'bus': ('vehicle_bus', '交通', 'Transit'),
 'weather': ('weather_partly_cloudy_day', '天気', 'Weather'),
 # 追加 2（2026-11-14、利用先の調査から）/ additions 2, from the usage survey
 'task-list': ('task_list_ltr', 'タスク', 'Tasks'), 'notification-off': ('alert_off', '通知オフ', 'Notifications off'),
 'lock-open': ('lock_open', 'ロック解除', 'Unlocked'), 'timer': ('timer', 'タイマー', 'Timer'),
 'sparkle': ('sparkle', '自動処理', 'Automatic'), 'view-month': ('calendar_month', '月の表示', 'Month view'),
 'text-size': ('text_font_size', '文字の大きさ', 'Text size'), 'filter-dismiss': ('filter_dismiss', '絞り込みを解除', 'Clear filters'),
}
# KM1 B 案（調整版）の原図は km1_bdefs.py / KM1 B drawings live in km1_bdefs.py
import km1_bdefs

# 別名 / aliases: 同じ意味の古い名前。新しく使わない（同じ絵柄を出す）
# Old names with the same meaning; do not use in new code (they render the same icon)
ALIASES = {'calendar-empty': 'calendar'}

SIZES = {16: 0.8, 20: 1.0, 24: 1.2}
SW = {16: 1.25, 20: 1.0, 24: 1.25}   # 20 の格子での線の幅 → 実寸で 16:1px・20:1px・24:1.5px

def to_d(path, scale):
    pen = SVGPathPen(None, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.') if '.' in ('%.2f' % v) else '%.2f' % v)
    path.draw(TransformPen(pen, (scale, 0, 0, scale, 0, 0)))
    return pen.getCommands()

def main(fluent_dir, out):
    os.makedirs(out + '/svg', exist_ok=True)
    global FL; FL = fluent_dir
    for n, (ja, en, fn) in LAZY.items(): define(n, ja, en, fn('regular'), fn('filled'))
    data = {'version': 3, 'rule': 'KM1-ICO-001', 'sizes': list(SIZES), 'aliases': ALIASES, 'icons': {}}
    for name, d in ORIG.items():
        e = {'ja': d['ja'], 'en': d['en'], 'source': 'km1', 'base': 'fluent:calendar_empty', 'paths': {}}
        for s, k in SIZES.items():
            for v in ('regular', 'filled'):
                ops = LAZY[name][2](v, s) if name in LAZY else d[v]
                e['paths'][f'{s}-{v}'] = to_d(build(ops, SW[s]), k)
        data['icons'][name] = e
    for name, (fl, ja, en) in IMPORT.items():
        e = {'ja': ja, 'en': en, 'source': f'fluent:{fl}', 'paths': {}}
        for s in SIZES:
            for v in ('regular', 'filled'):
                f = f'{fluent_dir}/{fl}_{s}_{v}.svg'
                if os.path.exists(f):
                    e['paths'][f'{s}-{v}'] = ' '.join(re.findall(r'<path[^>]* d="([^"]+)"', open(f).read()))
                else:   # Fluent にその大きさがないときは 20px の形を拡大・縮小 / scale the 20px drawing when Fluent lacks the size
                    e['paths'][f'{s}-{v}'] = to_d(P(' '.join(re.findall(r'<path[^>]* d="([^"]+)"', open(f'{fluent_dir}/{fl}_20_{v}.svg').read()))), s / 20)
                    e.setdefault('scaled', []).append(f'{s}-{v}')
        data['icons'][name] = e
    for n in km1_bdefs.B:
        if n not in data['icons']: continue
        ink, tint = {}, {}
        for s in (16, 20, 24):
            a, t = km1_bdefs.outline(n, s)
            ink[str(s)] = to_d(a, 1); tint[str(s)] = to_d(t, 1) if t is not None else None
        e = data['icons'][n]
        e['b'] = {'ink': ink, 'tint': tint if tint['20'] else None, 'tintY': km1_bdefs.TINT_Y}
        e['style'] = 'km1-b'
        # 通常（線だけ、1 色）と塗り（Filled）も B 案で作る。Fluent の形は比べるために 20px だけ残す。
        # Regular (single color, no tint) and Filled are B too; the Fluent shapes stay at 20px for comparison only.
        e['fluent'] = {'20-regular': e['paths']['20-regular'], '20-filled': e['paths']['20-filled']}
        for s in (16, 20, 24):
            a, _t = km1_bdefs.outline(n, s)
            e['paths'][f'{s}-regular'] = to_d(a, s / 20)
            e['paths'][f'{s}-filled'] = to_d(km1_bdefs.outline_filled(n, s), s / 20)
        e.pop('scaled', None)
        if str(e.get('source', '')).startswith('fluent:'):
            e['base'] = e['source']; e['source'] = 'km1'
    json.dump(data, open(out + '/km1-icons.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    sym = []
    for name, e in data['icons'].items():
        for key, dd in e['paths'].items():
            s = key.split('-')[0]
            open(f'{out}/svg/km1_{name}_{key}.svg', 'w').write(
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}"><title>{e["ja"]} / {e["en"]}</title><path fill="currentColor" d="{dd}"/></svg>\n')
            if s == '20':
                sym.append(f'<symbol id="km1-{name}-{key.split("-")[1]}" viewBox="0 0 20 20"><path fill="currentColor" d="{dd}"/></symbol>')
    open(out + '/sprite-20.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" style="display:none">' + ''.join(sym) + '</svg>\n')
    print('icons', len(data['icons']), '(km1', len(ORIG), '+ fluent', len(IMPORT), ')')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
