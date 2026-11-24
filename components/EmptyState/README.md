まだ何も無い場所に出す案内。何が入る場所かと、最初の一歩を伝える。中身が入るはずの場所に、左寄せの文で置く。
*Guidance for a place that has nothing yet: what belongs here and the first step, set left-aligned where the content would be.*

**理由 / Why:** 空の状態は、一覧が入るはずの位置で、一覧と同じ読み始めの線から読ませる。真ん中に大きなアイコンを置く型は、何も伝えない飾りなので使わない。次の予定のような、本物の次の一歩を書く。
*Read from the same left edge as the list it replaces. The centred big-icon template says nothing, so it is not used; state the real next step.*

## 使い方 / Usage
- 見出しは「何が無いか」を事実で書く（「今日の予定はありません」）。「データがありません」のような一般的な文言にしない。
  *The title states what is missing ("今日の予定はありません"), not a generic "no data".*
- 本文は 1〜2 文で、次に何があるか、どうすれば入るかを本物の内容で書く（「明日は 9:00 から気象学です」）。
  *One or two sentences with the real next step ("明日は 9:00 から気象学です").*
- 最初の一歩になる操作を 1 つだけ `action` に置く。その画面のプライマリにしてよい。
  *Put exactly one first-step action in `action`; it may be the screen's primary button.*
- アイコンは既定で付けない。画面に見出しがなく、何の場所か文だけでは分かりにくいときだけ、KM1 のアイコンの 32px（`icon-xl`）を 1 つ付ける。飾りなので読み上げない。イラストや絵文字は使わない。
  *No icon by default. Only when the place has no heading and the words alone leave it unclear, add one 32px KM1 icon (`icon-xl`), not announced. No illustrations or emoji.*
- 絞り込みの結果が 0 件のときは、「条件に合う予定はありません」と書き、`action` は「絞り込みを解除」にする。
  *For zero filter results, say so and make the action "clear filters".*
- エラーで表示できないときには使わない。`Alert` を使う。
  *Not for load failures: use `Alert`.*

## 利用側が渡すもの / You provide
`title`、本文、必要なら `icon`・`action`・`headingLevel`（既定 3）。
