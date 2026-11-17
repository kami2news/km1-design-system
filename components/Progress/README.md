進み具合や量を横棒で示す。処理の進行、達成度、ゲームのゲージに使う。
*A horizontal bar for progress or amount: task progress, completion, game meters.*

## 使い方 / Usage
- ラベルと数値を必ず棒の上に出す。棒の長さや色だけで伝えない。数値の書き方は `valueText` で変えられる（「3 / 5 件」「残り 2 日」）。
  *Label and value always appear above the bar; never rely on length or color alone. `valueText` customizes the wording.*
- `value` を省くと、終わりの分からない処理（不確定）の表示になる。
  *Omit `value` for indeterminate work.*
- **10 秒以上かかる処理では、`steps` と時間の見込みを必ず渡す**（見積もれるなら `remaining`、見積もれないなら `elapsed` と理由。下の項目）（「画面の組み立て」の「待ち時間」）。棒の上に「工程 2 / 4・60%・残り約 30 秒」と出て、下に工程の一覧（済み・実行中・まだ）が並ぶ。工程が変わると読み上げにも伝わる。
  ***For work of 10 seconds or more, always pass `steps` and a time estimate** (`remaining` when estimable, otherwise `elapsed` with a reason; see below) (see "Waiting" in Patterns). The head reads "工程 2 / 4・60%・残り約 30 秒", with a step list (done, current, to do) below; step changes are announced.*
- `remaining` は秒数。`null` にすると「残り時間を計算中」。見積もれない処理では `remaining` を渡さず、`elapsed`（経過秒数）と、`valueText` に見積もれない理由か「通常 1〜3 分」のような実績の幅を渡す。根拠のない残り時間は出さない。見込みを超えたら `overdue` にして「予定より時間がかかっています」と出す（0 秒のまま止めない）。表記は自動で丸める（5 秒刻み、60 秒からは分）。
  *`remaining` is in seconds; `null` shows "estimating". When it cannot be estimated, omit `remaining` and pass `elapsed` (seconds) plus a reason or a past range ("通常 1〜3 分") in `valueText`; never show an invented time left. Past the estimate set `overdue` (never sit at zero). Values are rounded automatically (5-second steps, minutes from 60s).*
- 途中で止められる処理なら `onCancel` を渡す。「キャンセル」ボタンが付く。
  *Pass `onCancel` when the work can be stopped; a "キャンセル" button appears.*
- `status` は `success`・`warning`・`danger`。色を変えるときは、理由が `valueText` かラベルで読めるようにする。
  *`status` is `success`, `warning` or `danger`; when the color changes, the reason must be readable in the text.*
- 短い待ち時間で場所が小さいときは `Spinner` を使う。
  *For short waits in small places, use `Spinner`.*

## 利用側が渡すもの / You provide
`label`、`value`（0〜`max`、既定 100）、10 秒以上なら `steps`・`step` と、`remaining` か `elapsed`、必要なら `valueText`・`status`・`overdue`・`onCancel`。
