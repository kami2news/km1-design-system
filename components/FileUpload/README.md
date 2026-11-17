ファイルを選ぶ、またはドラッグして渡す欄。
*Choose a file, or drag one in.*

## 使い方 / Usage
- ラベルと、受け付ける形式・大きさをヒントに必ず書く（「PDF・画像、10 MB まで」）。`accept` でも絞る。
  *Always state accepted formats and size in the hint; also set `accept`.*
- ドラッグはおまけで、「ファイルを選ぶ」ボタンだけで必ず完結させる（キーボード、スマホ）。スマホではドラッグの案内文を隠す。
  *Dragging is optional; the "ファイルを選ぶ" button always works alone (keyboard, phones). Phones hide the drag text.*
- 選んだファイルは名前と大きさの一覧で見せ、1 つずつ「×」で外せる。
  *Chosen files are listed with name and size, each removable with ×.*
- 10 秒以上かかる送信は、送信後に `Progress`（工程と時間の見込み）で進み具合を出す。
  *Uploads of 10s or more show `Progress` afterwards.*

## 利用側が渡すもの / You provide
`label`、`onChange`（選ばれた `File` の配列）、必要なら `accept`・`multiple`・`hint`・`error`・`required`・`files`。
