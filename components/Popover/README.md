ボタンの近くに出る、小さな作業用のパネル。表示の設定、短い補足、2〜3 項目の入力に使う。
*A small working panel next to a button for view settings, short details or two or three fields.*

## 使い方 / Usage
- `Tooltip` は読むだけの 1 行、`Menu` は操作の一覧、`Popover` は中で操作できる小さなパネル、`Dialog` は画面を止めて答えてもらうもの。
  *`Tooltip` is one read-only line, `Menu` a list of actions, `Popover` a small interactive panel, `Dialog` a blocking question.*
- 見出しは必須（読み上げの名前になる）。開くと中の最初の操作にフォーカスが移り、Esc・「×」・外側を押すと閉じて、開いたボタンに戻る。
  *A title is required. Focus moves inside on open; Esc, × or an outside click close it and return focus to the trigger.*
- 背後の画面は止めない（`aria-modal="false"`）。取り消せない操作や長い入力は `Dialog` か `Drawer` にする。
  *Non-modal; irreversible actions or long forms belong in `Dialog` or `Drawer`.*
- 幅は 320px まで。画面の右端に近いボタンでは `align="end"`。
  *Up to 320px wide; use `align="end"` near the right edge.*

## 利用側が渡すもの / You provide
`title`、`trigger`（`{label, icon?, iconOnly?, appearance?}`）、中身、必要なら `open` + `onOpenChange`・`align`。
