人や場所を、写真か頭文字で小さく示す丸。
*A small circle showing a person or place by photo or initials.*

## 使い方 / Usage
- 名前を `name` に渡すと、頭文字（日本語は 1 文字、英語は 2 文字）と色が自動で決まる。色は分類色の淡い塗りで、文字は常に `ink`。
  *`name` sets initials (one character for Japanese, two for English) and a color: a category tint with `ink` text.*
- 読み上げには名前が伝わる。すぐ横に名前の文字があるときは `decorative` にして二重に読ませない。
  *The name is announced; set `decorative` when the name is already written next to it.*
- 大きさは `sm` 24px・`md` 32px・`lg` 48px。押せる部品にはしない（押せるなら `Button` の中に入れる）。
  *Sizes 24/32/48px. Not interactive by itself; put it inside a `Button` if it must be pressed.*

## 利用側が渡すもの / You provide
`name`、必要なら `src`・`initials`・`size`・`color`（`cat-*` の名前）・`decorative`。
