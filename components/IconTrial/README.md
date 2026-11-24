KM1 B 案（調整版）の導入前と導入後の比較（KM1-ICO-001 §8）。試験導入した 6 種（検索・予定・フォルダ・削除・警告・通知）で見比べる。いまは全アイコンの通常表示が B 案。通常の `Icon` の呼び出し（`h(Icon,{name:'calendar'})`）でそのまま出る。
*Before/after comparison for the KM1 B (adjusted) icons, now the standard; compared on six: search, calendar, folder, delete, warning and notification, drawn by KM1 with strokes and a soft tint. They render through the normal `Icon` call.*

**理由 / Why:** 部品ではなく判断の記録。アイコンの B 案を選んだときの導入前と導入後の比べで、見直すときの根拠になるので保管する。部品の数には数えない（D21）。
*A record of the before/after comparison behind icon style B, kept as evidence; not counted as a part (D21).*

利用側が渡すもの: いつもの `Icon` と同じ（`name`・`size`・`filled`・`label`）。導入前の形と比べるときだけ `variant:'fluent'`。アプリ全体で元に戻すときは `setIconStyle('fluent')`。
*Same props as `Icon`; `variant:'fluent'` shows the previous shape; `setIconStyle('fluent')` reverts app-wide.*

## 使い方 / Usage

- 通常表示の線と記号は `icon-ink`（ライト #657283・ダーク #9AA7B8）、閉じた「もの」の形のうち面が形の理解を助けるもの（いま 63 個。一覧は「アイコン」4 章の「面」の列）の淡い面は `icon-tint-start` → `icon-tint-end` の縦のグラデーション。
  *Strokes in `icon-ink`, soft tint from `icon-tint-start` to `icon-tint-end` on closed object shapes where a fill helps recognition (63 icons; see the tint column in icons §4).*
- 押した・選んだ・今いる場所（`aria-pressed`・`aria-selected`・`aria-current`）は、B 案の塗りの形（`filled`、「アイコン」8.6）に切り替える。ホバー・押下・無効・強い背景（主ボタン）の上では、線は親の文字色に従い、強い背景の上では面を描かない。
  *Selected states switch to the B Filled form; hover, pressed, disabled and strong fills follow the parent text color, with no tint on strong fills.*
- ハイコントラスト（forced colors）では面を描かず、線は文字色。輪郭だけで区別できる形にしてある。
  *Forced colors drop the tint; shapes are recognisable by outline alone.*
- グラデーションの ID はアイコンごとに一意にする（`Icon` が自動で付ける）。同じ画面に何個並べても衝突しない。
  *Gradient IDs are unique per instance.*
- `Alert` の状態の記号（`status-info`・`status-success`・`status-warning`・`status-error`）も 4 種とも B 案。`Alert` の中では状態の色の塗りの形（Filled）を使う。ここでの「警告」は一般の警告アイコン `warning`。
  *All four Alert status symbols are B too; inside `Alert` they use the Filled form in the status color. The `warning` here is the general warning icon.*
- Flutter は `Km1BIcon(Km1BIconName.calendar)`（`icons/km1_icons_b.dart`、同じ原図から生成）。
  *Flutter: `Km1BIcon` generated from the same drawings.*
