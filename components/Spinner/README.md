短い待ち時間を示す回転する輪。ボタンの横や一覧の読み込み中に使う。
*A rotating ring for short waits, beside a button or while a list loads.*

## 使い方 / Usage
- 何を待っているかを文言で添える（「保存中」「読み込み中」）。場所がないときだけ `hideLabel` で文言を隠す（読み上げには残る）。
  *Say what is being waited for. Use `hideLabel` only when there is no room (it stays available to screen readers).*
- 使うのは 10 秒未満の待ちだけ。10 秒以上かかる処理には使わず、工程と時間の見込みを出す `Progress` を使う。
  *Only for waits under 10 seconds; for 10 seconds or more use `Progress` with steps and a time estimate.*
- `prefers-reduced-motion` では回転がゆっくりになる。
  *Rotation slows under `prefers-reduced-motion`.*

## 利用側が渡すもの / You provide
`label`（既定「読み込み中」）、必要なら `hideLabel`。
