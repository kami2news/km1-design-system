複数選択や同意のためのチェックボックス。ラベルは必ず付け、ラベルをクリックしても切り替わる。
*A checkbox for multi-select or consent. Always provide a label; clicking the label toggles it.*

利用側が渡すもの: `children`（ラベル）、`checked` または `defaultChecked`、`onChange`。
*Consumer provides: `children` (label), `checked` or `defaultChecked`, `onChange`.*

- 枠は `stroke-strong`（3:1 以上）、選択時は `brand` の塗りに白いチェック。フォーカスは `focus-ring`。大きさは 20px。
  *Border `stroke-strong` (3:1 or more); checked is a `brand` fill with a white tick; focus uses `focus-ring`; 20px.*
- やらないこと: ラベルなしの使用、状態を色だけで示すこと（チェック記号が状態を示す）。
  *Don't: use without a label, or rely on color alone (the tick shows state).*
