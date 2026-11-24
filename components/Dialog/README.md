確認や短い入力のために、画面の上に重ねて出す。元の操作を止めてでも判断してほしいときだけ使う。
*Overlay for a confirmation or short input. Use only when a decision must interrupt the task.*

利用側が渡すもの: `open`、`title`、`onClose`、`actions`（ボタン）、`children`。
*Consumer provides: `open`, `title`, `onClose`, `actions`, `children`.*

- 標準の `<dialog>` を `showModal()` で開くので、フォーカスは中に閉じ込められ、Esc で閉じ、閉じたら元のボタンに戻る。背景は操作できない。
  *Opened with native `<dialog>.showModal()`: focus is trapped, Esc closes, focus returns to the opener, and the background is inert.*
- 見出し（`title`）は必須。操作の文言は、実行する側を動詞で書き（「削除」）、実行しない側は「キャンセル」にそろえる。アクションは 2 つまでにし、主な 1 つを `primary` にする。右にプライマリ、左に「キャンセル」。幅 480px 未満では縦に積み、プライマリが上になる。アクションが 1 つだけのときは中央に置く（デジタル庁デザインシステムのボタン配置）。
  *`title` is required. The confirming label is a verb ("削除"); the declining one is always "キャンセル". At most two actions, one `primary`: primary on the right, cancel on the left; below 480px they stack with the primary on top; a single action is centered (Digital Agency DS button placement).*
- 取り消せない操作（削除など）の確認は、見出しに対象の名前を入れ（「『環境化学 第 8 回』を削除しますか？」）、本文で何が消えるかを 1 文で書く。実行する側のボタンは `primary` にせず `danger`（赤の文字）にし、「キャンセル」は `transparent` にする。`primary` の紺は「こちらを選んでほしい」という合図なので、消す操作には付けない（D26）。
  *For irreversible actions, name the object in the title, say what will be lost in one sentence, and use `danger` (red text), not `primary`, for the confirming button: navy primary says "choose this", which a deletion should not.*
- やらないこと: ダイアログの中にダイアログを出す、長いフォームを入れる。
  *Don't: nest dialogs or place long forms inside.*
