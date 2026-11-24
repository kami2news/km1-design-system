曜日 × 時限の時間割。授業やシフトのように、毎週同じ枠に入る予定を見せる。
*A weekday-by-period timetable for things that recur in fixed weekly slots, such as classes or shifts.*

## 使い方 / Usage
- 表の名前（`caption`）は必須。行は `periods`（`{label: '1限', time: '9:00〜9:50'}`）、列は `days`（既定は月〜金）。
  *`caption` is required. Rows come from `periods`, columns from `days` (Mon–Fri by default).*
- 予定は `items` に `{day, period, title, sub?, cat?}` で渡す（`day`・`period` は 0 始まりの位置）。`cat` は分類色の名前（`teal`、`pumpkin` など）で、左の帯と淡い塗りになる。文字は常に `ink`。
  *Items are `{day, period, title, sub?, cat?}` (zero-based positions). `cat` names a category color, shown as a left bar and tint; text stays `ink`.*
- 分類色だけで区別させない。授業名を `title` に、場所や種類を `sub` に必ず書く。
  *Never rely on the category color alone: put the name in `title` and the place or kind in `sub`.*
- `onSelect` を渡すと各コマがボタンになる。押したらプレビューを出す（いきなり編集にしない）。
  *With `onSelect` each slot becomes a button; open a preview, not the editor.*
- `today` に列の位置を渡すと、その曜日の見出しに線が付き、読み上げでも「今日」と伝わる。
  *`today` (a column index) underlines that weekday heading and announces it as today.*
- 狭い画面では横にスクロールする。スマホで 1 日ずつ見せたいときは、`Tabs` で曜日を切り替えて `Card` の一覧にする。
  *Scrolls horizontally when narrow. On phones, consider `Tabs` per weekday with a list of `Card`s instead.*

## 利用側が渡すもの / You provide
`caption`、`periods`、`items`、必要なら `days`・`today`・`onSelect`・`hideCaption`。
- 分類は色に加えて模様でも区別できる: 項目に `pattern`（`CategoryPattern`）を渡すと題名の前に分類のしるしが出る。凡例は `CategoryLegend` で添える（KM1-COL-001）。
  *Pass `pattern` to show a category mark before the title; add a `CategoryLegend` (KM1-COL-001).*

**理由 / Why:** 毎週同じ枠の予定（授業・シフト）を見る。曜日 × 時限の格子。毎週同じ場所にあるので探さない。
*Weekly fixed slots (classes, shifts): a weekday × period grid; the same place every week, no searching.*
