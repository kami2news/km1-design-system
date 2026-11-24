長い一覧をページに分けたときの、ページの移動。
*Moves between pages of a long list.*

## 使い方 / Usage
- 今のページは、枠・色・文字の太さで示し、読み上げには `aria-current="page"` で伝わる。前後のボタンは端のページでも消さず、押せない状態にする。
  *The current page shows an edge, color and bold text, exposed via `aria-current="page"`. Prev/next stay visible at the ends, just inactive.*
- 7 ページを超えると、最初・最後・今の前後だけを出し、間は「…」にする。480px 未満ではページ番号を隠し、「3 / 12」の表示と前後のボタンだけにする。
  *Past seven pages only first, last and neighbors show, with "…" between. Below 480px page numbers collapse to "3 / 12" plus prev/next.*
- 1 ページに収まるなら出さない。件数が少ない一覧は「もっと見る」ボタンのほうが簡単。
  *Omit it for a single page; for short lists a "show more" button is simpler.*
- ページを変えたら、一覧の先頭にスクロールとフォーカスを戻す（利用側で行う）。
  *After a page change, return scroll and focus to the top of the list (consumer's job).*

## 利用側が渡すもの / You provide
`page`（1 始まり）、`count`（総ページ数）、`onChange`、必要なら `label`。

**理由 / Why:** 長い一覧を区切る。500 行を超えない決まりと組で使う。何ページ中のどこかが分かる。
*Split long lists: paired with the 500-row limit; shows where you are among the pages.*
