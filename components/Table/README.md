行と列でデータを見比べる表。
*A table for comparing data in rows and columns.*

## 使い方 / Usage
- 表の名前（`caption`）は必須。見た目に出したくないときは `hideCaption`（読み上げには残る）。
  *`caption` is required; `hideCaption` hides it visually but keeps it for screen readers.*
- 1 列目は行の見出しになる（`rowHeader={false}` で外せる）。数値の列は `align: 'end'` で右にそろえ、桁がそろう数字にする。
  *The first column is the row header (`rowHeader={false}` to opt out). Numeric columns use `align: 'end'` with tabular figures.*
- 並べ替えできる列は `sortable`。今の並びは矢印のアイコンと `aria-sort` の両方で示す。並べ替えそのものは利用側で行い、`sort` と `onSort` でつなぐ。
  *`sortable` columns show the current order by arrow icon and `aria-sort`; sorting itself is done by the consumer via `sort` and `onSort`.*
- 行の高さはスマホ 44px・PC 32px。列が多いときは横にスクロールする（枠にフォーカスして矢印キーで動かせる）。5 列を超えるならスマホでは `Card` の一覧に組み替える。
  *Rows are 44px on touch, 32px on PC. Wide tables scroll horizontally (the frame is focusable). Past five columns, switch to a list of `Card`s on phones.*
- セルの中身を作り替えるときは列に `render` を渡す（`Badge` や `Menu` を置ける）。
  *Use a column `render` for custom cells (`Badge`, `Menu`).*

## 行の選択と一括操作 / Row selection and bulk actions
- `selectable` を付けると左にチェックボックスの列が出る。見出しのチェックボックスは「すべて選択」で、一部だけ選ぶと「−」（一部選択）になる。行のチェックボックスの読み上げ名は「（1 列目の値）を選択」。1 列目が文字でないときは列に `text` を渡す。
  *`selectable` adds a checkbox column; the header box selects all and shows a dash when partial. Row boxes are named from the first column (pass `text` on it if it renders non-text).*
- 1 件以上選ぶと、表の上に「3 件を選択中」と `bulkActions` のボタン、「選択を解除」が出る。件数は読み上げにも伝わる。
  *With a selection, a bar shows the count, `bulkActions` and "選択を解除"; the count is announced.*
- 削除のような取り消せない一括操作は `danger: true` にして、押したあと `Dialog` で「3 件を削除しますか」と件数つきで確認する。
  *Irreversible bulk actions use `danger: true` and confirm with the count in a `Dialog`.*
- 選んだ状態は利用側が持つ（`selected` と `onSelectionChange`）。並べ替えやページを変えても選択は消さない。
  *The caller owns `selected`; sorting or paging keeps the selection.*

## 密度 / Density

`density="compact"`・`"regular"`（既定、今までと同じ）・`"spacious"`。行の上下の余白は `collection-item-gap-*` の半分（2・4・8px）、行の最小の高さは compact で中身まで、regular で `--control-height`、spacious で `--control-height` + 8px。表示専用の行（文字だけ）は compact で中身の高さまで詰まる。選択のチェックがある行、中にリンク・ボタン・入力がある行は、どの密度でも PC 32px・タッチ 44px（Flutter は OS ごとの値）を下回らない。行全体を押す操作はないので、行を開く表は先頭のセルにリンクを置く。どの密度を選ぶかは「トークン › 密度」の作業ごとの表。入れ物の `data-density` にも従う。Flutter は `Km1Table(density: Km1Density.compact)`。
*Row padding is half of `collection-item-gap-*` (2/4/8px); minimum row height is content (compact), `--control-height` (regular) or +8px (spacious). Display-only rows shrink in compact; rows with checkboxes, links, buttons or inputs never drop below the control height. Choose density by task (Tokens › Density). Flutter: `Km1Table(density:)`.*

## 利用側が渡すもの / You provide
`caption`、`columns`（`{key, label, align?, sortable?, render?, text?}`）、`rows`（`id` があると安定する）、必要なら `sort`・`onSort`・`striped`・`empty`、行選択には `selectable`・`selected`・`onSelectionChange`・`bulkActions`（`{label, onClick(ids), icon?, danger?}`）、密度に `density`。
