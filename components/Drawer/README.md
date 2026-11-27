画面の端から出る大きめのパネル。絞り込みの条件、詳細、少し長い設定に使う。
*A panel that slides in from the edge for filters, details or longer settings.*

## 使い方 / Usage
- 短い確認や 1 つの質問は `Dialog`。項目が多く、背後の画面を見ながら操作したいときは `Drawer`。
  *Use `Dialog` for short confirmations; `Drawer` for longer content people work on next to the page.*
- 既定は右から出る。ナビゲーションのように左が自然なものは `position="start"`。幅は 400px、480px 未満では画面いっぱい。
  *Slides from the right by default; `position="start"` for navigation-like panels. 400px wide; full width below 480px.*
- 見出しは必須。右上の「×」、Esc、暗幕を押すと閉じる。フォーカスはパネルの中に閉じ込められ、閉じると開いたボタンに戻る（標準の `dialog` 要素）。
  *A title is required. ×, Esc and the scrim close it; focus is trapped inside and returns to the opener (native `dialog`).*
- 下部の `actions` は `Dialog` と同じく、右にプライマリ、左に「キャンセル」。
  *`actions` follow `Dialog`: primary right, "キャンセル" left.*

## 利用側が渡すもの / You provide
`open`、`onClose`、`title`、中身、必要なら `actions`・`position`。

**理由 / Why:** 今の画面を見ながら詳しい条件や詳細を扱う。画面の端から出し、元の画面が横に残る。
*Detailed filters or details while keeping the screen: slides from the edge, the screen stays beside it.*
