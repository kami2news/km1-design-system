今いる画面が、全体のどこにあるかを示す道しるべ。3 階層以上ある画面で使う。
*Shows where the current screen sits in a hierarchy of three or more levels.*

## 使い方 / Usage
- 左から上位の階層、最後が今の画面。今の画面はリンクにせず、太字で示す（読み上げには `aria-current="page"`）。
  *Top level on the left, current screen last; the current item is bold text, not a link.*
- 2 階層以下なら使わず、「戻る」ボタンで足りる。スマホでは途中の階層を「…」に縮める。
  *Skip it for two levels or fewer; on phones the middle levels collapse to "…".*
- `nav` の領域（既定の名前「パンくずリスト」）に入る。
  *Lives in a `nav` landmark named "パンくずリスト" by default.*

## 利用側が渡すもの / You provide
`items`（`{label, href?, onClick?}`）、必要なら `label`。
