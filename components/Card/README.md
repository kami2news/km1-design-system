関連する情報をまとめる面。`surface` 上に `shadow-2`、`radius-lg`、内側は `container-card-padding-regular`（= `space-lg`）。
*A surface that groups related content: `shadow-2`, `radius-lg`, `container-card-padding-regular` (= `space-lg`) padding on `surface`.*

- 密度 / Density: `density="compact"`（内側 12px）・`"regular"`（16px、既定）・`"spacious"`（24px）。入れ物の `data-density` にも従う。中の文字の大きさとボタンの高さは変わらない。Flutter は `Padding(padding: EdgeInsets.all(Km1Density.compact.containerPadding))`（「トークン › 密度」）。
  *`density` compact (12px) / regular (16px, default) / spacious (24px); also follows a container's `data-density`. Text size and button height never change.*

利用側が渡すもの: `children`、任意で `title` と `headingLevel`（既定 3。ページの見出し順を飛ばさないよう設定する）。`onClick` を渡すとカード全体が操作対象になり、Enter / Space とフォーカスリングに対応する。
*Consumer provides: `children`, optional `title` and `headingLevel` (default 3; set it so heading order is never skipped). With `onClick` the whole card is interactive, with Enter / Space and a focus ring.*

- やること: カード内に操作が複数ある場合は `onClick` を使わず、内部に `Button` を置く。
  *Do: when a card holds several actions, skip `onClick` and place `Button`s inside.*
- やらないこと: カードの入れ子、色付きの左罫線によるアクセント。
  *Don't: nest cards or add a colored left-border accent.*
