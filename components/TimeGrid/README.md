1 日または 1 週間の予定を、時刻の縦軸に並べる予定表。
*A day or week schedule laid out on a vertical time axis.*

## 使い方 / Usage
- `days` に 1 日分（1 日表示）か 7 日分（週表示）を渡す。見出しは日付の書き方の決まりどおり「11/12（木）」。
  *Pass one day or seven in `days`, labeled per KM1's date format.*
- 予定は `events` に `{day, start, end, title, sub?, cat?}` で渡す。時刻は 24 時間制の「9:00」。重なる予定は自動で横に並ぶ。分類色 `cat` は左の帯と淡い塗りになり、文字は常に `ink`。
  *Events are `{day, start, end, title, sub?, cat?}` with 24-hour times; overlaps sit side by side; `cat` sets the bar and tint, text stays `ink`.*
- 終日の予定は `allDay: true` で上の「終日」行に入る。0:00 ちょうどの締め切りは、前日の終日として渡す（KM1 の日付の決まり）。
  *`allDay: true` goes to the all-day row; a 0:00 deadline is passed as all-day on the previous day.*
- 時刻つきの締め切りは `kind: 'deadline'` と `start` だけを渡す。1 分の枠として、旗のアイコン + 時刻で警告色に描く（赤にしない）。
  *Timed deadlines use `kind: 'deadline'` and `start` only: a one-minute slot with a flag icon in the warning color (never red).*
- 仮の予定は `tentative: true` で斜線になる（色だけに頼らない状態の示し方）。
  *`tentative: true` adds hatching.*
- 現在時刻は `now`（`'2026-11-12T10:20'`）で、その日の列に `danger-ink` の線が出る。
  *`now` draws the current-time line in `danger-ink`.*
- **`onSelect` を渡すことを強く勧める。** 短い予定は枠が小さく、文字が「…」で切れる。押したらプレビューカードで全文を見せる（「画面の組み立て」の決まり）。読み上げには、切れていない全文（「11/12（木） 9:00〜9:50 地球化学、3 号館 201」）が伝わる。
  ***Strongly prefer passing `onSelect`.** Short events truncate visually; open a preview card with the full text. Screen readers always get the full label.*
- **押せる範囲について**: 予定の枠の高さは時間の長さそのもので、押しやすさのために伸ばすと時刻がずれて見える。そこで、1 時間の高さはスマホで 64px（50 分の予定が 53px）、PC で 56px、締め切りの枠は 24px にしてある。それでも 30 分以下の予定は 44px に届かないので、**スマホでは同じ予定を `Card` の一覧（アジェンダ）でも押せるようにする**（WCAG 2.2 の 2.5.8 にある「同じ操作が別の部品でもできる」例外）。
  ***Hit areas**: block height is the duration, so it is not inflated. An hour is 64px on touch (a 50-minute event is 53px) and 56px on PC; deadlines are 24px. Short events still fall below 44px, so **on phones the same events must also be pressable in an agenda list of `Card`s** (the WCAG 2.2 2.5.8 equivalent-control exception).*
- 読み上げとキーボードの順番は、日ごと・時刻順。時刻の目盛りは読み上げない。
  *Reading and Tab order follow day, then time; the hour scale is not announced.*
- 予定ごとの読み上げの名前は、見えている文字の順（題名・時刻・補足）のあとに日付（例:「地球化学 10:00〜10:50 3 号館 201、11/9（月）」）。見えている言葉をそのまま名前に含め、声で操作する人が見えている言葉で呼べるようにする（WCAG 2.5.3）。
  *Each event's accessible name is its visible text in order (title, time, details), then the day (WCAG 2.5.3, label in name).*
- 週表示は 1 列 96px を下回ると横にスクロールする。スマホでは 1 日表示を基本にし、日の切り替えは `Tabs` か前後のボタンで行う。
  *The week view scrolls horizontally below 96px per day; phones should default to the day view.*

## Flutter
`km1_widgets.dart` の `Km1TimeGrid`。時刻は 0:00 からの分（9:00 なら 540）で渡す。親で高さを決める（`SizedBox` や `Expanded` の中に置く）。
*`Km1TimeGrid` in `km1_widgets.dart`; times are minutes from midnight; give it a bounded height.*

## 利用側が渡すもの / You provide
`label`、`days`（`{date, label}`）、`events`、必要なら `startHour`（既定 8）・`endHour`（既定 22）・`hourHeight`（既定はスマホ 64、PC 56）・`height`・`now`・`onSelect`。
- 分類は色に加えて模様でも区別できる: 項目に `pattern`（`CategoryPattern`）を渡すと題名の前に分類のしるしが出る。凡例は `CategoryLegend` で添える（KM1-COL-001）。
  *Pass `pattern` to show a category mark before the title; add a `CategoryLegend` (KM1-COL-001).*

**理由 / Why:** 1 日・1 週の予定の重なりを見る。時刻の縦軸に長さで置き、空き時間が見える。
*See overlaps in a day or week: events placed by length on a time axis, free time visible.*
