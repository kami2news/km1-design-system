一覧や画面の中を探すための検索欄。
*A search field for finding things in a list or screen.*

## 使い方 / Usage
- ラベルは必ず付ける。見た目に出さないときは `hideLabel`（読み上げには残る）。プレースホルダーに例を書く（「授業名・場所で検索」）。
  *Always label it; `hideLabel` hides it visually only. Put an example in the placeholder.*
- 入力中に絞り込むなら `onChange`、決定してから探すなら Enter の `onSearch` を使う。入力があるときだけ「×」（検索語を消す）が出て、Esc でも消せる。
  *Use `onChange` for live filtering or `onSearch` (Enter) for submit-style search. "×" appears only with text; Esc also clears.*
- 結果が 0 件のときは、一覧側に `EmptyState`（「条件に合う予定はありません」）を出す。
  *For zero results, show an `EmptyState` in the list.*
- 欄は `role="search"` の領域に入るので、読み上げで検索の場所として見つけられる。
  *It sits in a `role="search"` landmark.*

## 利用側が渡すもの / You provide
`label`、必要なら `placeholder`・`value` + `onChange`・`onSearch`・`hint`・`hideLabel`。

**理由 / Why:** 画面の中から探したい。いつも同じ場所に置き、消すボタンと Esc で戻せる。
*Find things on the screen: always in the same place, with a clear button and Esc to return.*
