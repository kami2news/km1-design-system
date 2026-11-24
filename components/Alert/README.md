状態をユーザーに知らせるバナー。色に加えて、アイコンと「情報」「成功」「注意」「エラー」の文言を必ず併記する。
*A banner that informs users of a state. Besides color it always carries an icon and a word (Info, Success, Warning, Error).*

**理由 / Why:** 状態は、色が見分けられない人にも、形（アイコン）と言葉の 2 つで伝わる。色は面の 1 か所だけにし、色の縁や色の文字を重ねない。同じことを 4 回言うと、どれも目立たなくなるため。
*Shape (icon) and word carry the state for everyone; colour appears once, on the surface. Repeating it in border and text too makes nothing stand out.*

利用側が渡すもの: `status`（`info` / `success` / `warning` / `danger`）、`title`（何が起きたか）、任意で `children`（どうすればよいか）。
*Consumer provides: `status`, `title` (what happened), optional `children` (what to do).*

- `danger` と `warning` は `role="alert"`、`info` と `success` は `role="status"` で読み上げられる。
  *`danger` and `warning` use `role="alert"`; `info` and `success` use `role="status"`.*
- 閉じられるようにするときは `onClose` を渡す。×の閉じるボタン（スマホ 44px・PC 32px、読み上げは「閉じる」）が付く。「閉じる」を普通のアクションボタンで作らない。画面に固定して出す場合は必ず `onClose` を付け、閉じたことを覚えて再表示しないようにし、あとから見直せる手段も用意する（デジタル庁デザインシステム）。
  *Pass `onClose` to make it dismissible: an × button (44px on touch, 32px on PC, announced as "閉じる"). Don't build "close" as an ordinary action button. A pinned alert must be dismissible, remember the dismissal, and offer a way to see it again (Digital Agency DS).*
- 背景は各 `-tint`、アイコンは各 `-ink`、文字（「情報：」などの種類の言葉も）は `ink`。縁は付けない（強制カラーモードでだけ縁が出る）。
  *Background is the `-tint` token, the icon uses the `-ink` token, all text including the kind word is `ink`. No border except in forced-colors mode.*
- やらないこと: 文言なしのアイコンだけ、1 画面に複数の `danger` を並べること。
  *Don't: show an icon without a word, or stack several `danger` alerts on one screen.*
