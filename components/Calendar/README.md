月の表から日付を 1 つ選ぶ。予定のある日に印を付けられる。
*A month grid for picking one date, with marks on days that have events.*

## 使い方 / Usage
- 日付は `'2026-11-12'` の形の文字列でやり取りする（`value`、`onChange`、`min`、`max`、`marks` のキー）。
  *Dates are `'2026-11-12'` strings (`value`, `onChange`, `min`, `max`, keys of `marks`).*
- 今日は枠の丸、選択中は塗りの丸で示す。予定のある日は数字の下に点が付き、読み上げでは「予定 2 件」と伝わる（`marks` に件数を渡す）。
  *Today is a ring, the selection a filled circle. Days with events get a dot, read out as "予定 2 件" (pass counts in `marks`).*
- 週の始まりは日曜（`weekStart={1}` で月曜）。土日の色分けはしない（色だけの区別になるため）。
  *Weeks start on Sunday (`weekStart={1}` for Monday). Weekends are not color-coded.*
- キーボード: 矢印で日を移動、Home・End で週の端、PageUp・PageDown で前後の月、Enter・Space で選ぶ（W3C APG の日付グリッド）。
  *Keyboard: arrows move by day, Home/End to week edges, PageUp/PageDown by month, Enter/Space selects (W3C APG date grid).*
- マスの大きさはスマホ 44px・PC 32px。フォームで日付だけ入れてもらうなら、`Input` の `type="date"` のほうが速い。
  *Cells are 44px on touch, 32px on PC. For a plain date in a form, `Input` with `type="date"` is quicker.*

## 利用側が渡すもの / You provide
`value`、`onChange`、必要なら `marks`（`{'2026-11-14': 2}`）・`min`・`max`・`weekStart`・`label`・`today`。
