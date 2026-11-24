操作を実行するボタン。1 画面にプライマリ（`appearance="primary"`）は 1 つだけ。
*A button that triggers an action. Only one primary (`appearance="primary"`) per screen.*

利用側が渡すもの: `children`（動詞のラベル）。アイコンのみの場合は `aria-label` が必須。
*Consumer provides: `children` (a verb label). Icon-only buttons require `aria-label`.*

- `primary`: 主要操作。`secondary`（既定）: 通常の操作。`outline`: 背景が不均一な面の上。`subtle`: ツールバー内。`transparent`: リンク的な操作。`danger`: 取り消せない操作の確認（赤の文字、形は `secondary`）。
  *`primary`: main action. `secondary` (default): ordinary action. `outline`: on uneven backgrounds. `subtle`: in toolbars. `transparent`: link-like action. `danger`: confirming an irreversible action (red text, secondary shape).*
- サイズは `small` / `medium`（標準）/ `large`。高さは PC で 24 / 32 / 40px、スマホで 44 / 44 / 48px に自動で切り替わる。
  *Sizes: `small`, `medium` (default), `large`: 24 / 32 / 40px on PC, 44 / 44 / 48px on touch, switched automatically.*
- 使い分け（デジタル庁デザインシステム）: `primary` は 1 画面に原則 1 つ。`outline` は同じ場面で同時に 3 つまで（4 つ以上なら流れを見直す）。「キャンセル」は 1 画面に 1 つの文字だけのボタン（`transparent`）。重要度の差は色だけで示さず、塗りと枠線などの形で示す。
  *Usage (Digital Agency DS): one `primary` per screen; at most three `outline` together (more means rethinking the flow); cancel is a single text-only button (`transparent`). Importance is shown by shape (fill vs outline), not color alone.*
- 配置: PC では「完了」「次へ」を右、「キャンセル」「戻る」を左。スマホでは縦に積み、主なボタンを一番上にする。
  *Placement: on desktop progress actions go right and cancel/back go left; on mobile stack vertically with the primary on top.*
- 無効化は極力避ける。押せない理由が分からないと、操作が止まる。どうしても無効にするときは、ボタンのすぐ近くに理由か有効にする条件を書き、`aria-describedby` で結ぶ。`disabled` は `aria-disabled` で実装してあり、Tab キーで届き、押しても何も起きない。
  *Avoid disabling. If unavoidable, write the reason or condition next to the button and link it with `aria-describedby`. `disabled` is implemented with `aria-disabled`: it stays reachable by Tab and does nothing when pressed.*
- やること: ラベルは 2〜4 文字の動詞。破壊的操作は確認ダイアログで受ける。
  *Do: short verb labels; confirm destructive actions in a dialog.*
- やらないこと: プライマリの並置、`disabled` の理由を示さないまま放置。
  *Don't: place several primaries together, or leave a disabled button unexplained.*
