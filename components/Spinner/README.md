短い待ち時間を示す回転する輪。保存や送信のように、出てくる中身の形がない 1〜10 秒の待ちに使う。
*A rotating ring for 1–10 second waits with no content shape to preview, such as saving or sending.*

**理由 / Why:** 待ちの部品は、形と時間で 1 つに決まる（「画面の組み立て › 待ち時間」）。形が分かれば Skeleton のほうが何が出るか伝わり、10 秒以上なら工程と時間が要るので、Spinner はその間の短い待ちだけに使う。
*Shape and duration pick exactly one waiting part. Skeleton tells more when the layout is known, and 10s or more needs steps and time, so Spinner covers only the short waits in between.*

## 使い方 / Usage
- 何を待っているかを文言で添える（「保存中」「読み込み中」）。場所がないときだけ `hideLabel` で文言を隠す（読み上げには残る）。
  *Say what is being waited for. Use `hideLabel` only when there is no room (it stays available to screen readers).*
- 使うのは 10 秒未満の待ちだけ。10 秒以上かかる処理には使わず、工程と時間の見込みを出す `Progress` を使う。
  *Only for waits under 10 seconds; for 10 seconds or more use `Progress` with steps and a time estimate.*
- `prefers-reduced-motion` では回転がゆっくりになる。
  *Rotation slows under `prefers-reduced-motion`.*

## 利用側が渡すもの / You provide
`label`（既定「読み込み中」）、必要なら `hideLabel`。
