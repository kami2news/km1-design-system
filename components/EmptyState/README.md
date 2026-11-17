まだ何も無い場所に出す案内。何が入る場所かと、最初の一歩を伝える。
*Guidance for a place that has nothing yet: what belongs here and the first step.*

## 使い方 / Usage
- 見出しは「何が無いか」を事実で書く（「今日の予定はありません」）。「データがありません」のような一般的な文言にしない。
  *The title states what is missing ("今日の予定はありません"), not a generic "no data".*
- 本文は 1〜2 文で、ここに何が入るか、どうすれば入るかを書く。
  *One or two sentences on what goes here and how to add it.*
- 最初の一歩になる操作を 1 つだけ `action` に置く。その画面のプライマリにしてよい。
  *Put exactly one first-step action in `action`; it may be the screen's primary button.*
- アイコンは KM1 のアイコンの 32px（`h(Icon,{name:'calendar',size:32})`。24px の形を拡大）（`icon-xl`、KM1 で 32px を使うのはここだけ）を 1 つ。飾りなので読み上げない。イラストや絵文字は使わない。
  *One 32px Regular Fluent System Icon (`icon-xl`, the only 32px use in KM1), decorative (not announced). No illustrations or emoji.*
- 絞り込みの結果が 0 件のときは、「条件に合う予定はありません」と書き、`action` は「絞り込みを解除」にする。
  *For zero filter results, say so and make the action "clear filters".*
- エラーで表示できないときには使わない。`Alert` を使う。
  *Not for load failures: use `Alert`.*

## 利用側が渡すもの / You provide
`title`、本文、必要なら `icon`・`action`・`headingLevel`（既定 3）。
