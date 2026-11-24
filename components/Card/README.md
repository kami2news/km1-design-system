関連する情報をまとめる面。`surface` 上に `stroke` の 1px の縁、`radius-lg`、内側は `container-card-padding-regular`（= `space-lg`）。影は付けない。
*A surface that groups related content: a 1px `stroke` border, `radius-lg`, `container-card-padding-regular` (= `space-lg`) padding on `surface`. No shadow.*

**理由 / Why:** カードは画面の上で動かず、浮いてもいないので、高さを示す影には意味がない。まとまりは縁 1 本で示す。押せるカードは、ホバーで面の色と縁を濃くして知らせる。
*Cards neither move nor float, so an elevation shadow says nothing; one border marks the group. Interactive cards darken the surface and border on hover.*

- 密度 / Density: `density="compact"`（内側 12px）・`"regular"`（16px、既定）・`"spacious"`（24px）。入れ物の `data-density` にも従う。中の文字の大きさとボタンの高さは変わらない。Flutter は `Padding(padding: EdgeInsets.all(Km1Density.compact.containerPadding))`（「トークン › 密度」）。
  *`density` compact (12px) / regular (16px, default) / spacious (24px); also follows a container's `data-density`. Text size and button height never change.*

利用側が渡すもの: `children`、任意で `title` と `headingLevel`（既定 3。ページの見出し順を飛ばさないよう設定する）。`onClick` を渡すとカード全体が操作対象になり、Enter / Space とフォーカスリングに対応する。
*Consumer provides: `children`, optional `title` and `headingLevel` (default 3; set it so heading order is never skipped). With `onClick` the whole card is interactive, with Enter / Space and a focus ring.*

- やること: カード内に操作が複数ある場合は `onClick` を使わず、内部に `Button` を置く。
  *Do: when a card holds several actions, skip `onClick` and place `Button`s inside.*
- やらないこと: カードの入れ子、色付きの左罫線によるアクセント。
  *Don't: nest cards or add a colored left-border accent.*
