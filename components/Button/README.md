操作を実行するボタン。1 画面にプライマリ（`appearance="primary"`）は 1 つだけ。
*A button that triggers an action. Only one primary (`appearance="primary"`) per screen.*

利用側が渡すもの: `children`（動詞のラベル）。アイコンのみの場合は `aria-label` が必須。
*Consumer provides: `children` (a verb label). Icon-only buttons require `aria-label`.*

- 種類は 4 つ。`primary`（紺の塗り）: その画面で次にすること、1 画面に 1 つ。`secondary`（既定、枠）: ふつうの操作と「キャンセル」。`subtle`（枠なし）: ツールバーや行の中など、同じ形のボタンが何度も並ぶところ。`danger`（赤の文字、枠）: 取り消せない操作。古い `outline` は `secondary`、`transparent` は `subtle` として描く（D28）。
  *Four kinds. `primary` (navy fill): the next step, one per screen. `secondary` (default, outlined): ordinary actions and Cancel. `subtle` (no border): repeated buttons in toolbars and rows. `danger` (red text, outlined): irreversible actions. Old `outline` renders as `secondary`, `transparent` as `subtle` (D28).*
- サイズは `small` / `medium`（標準）/ `large`。高さは PC で 24 / 32 / 40px、スマホで 44 / 44 / 48px に自動で切り替わる。
  *Sizes: `small`, `medium` (default), `large`: 24 / 32 / 40px on PC, 44 / 44 / 48px on touch, switched automatically.*
- 使い分け: `primary` は 1 画面に原則 1 つ。枠のボタンは同じ場面で同時に 3 つまで（4 つ以上なら流れを見直す）。「キャンセル」は `secondary`。重要度の差は色だけで示さず、塗り・枠・枠なしの形で示す（デジタル庁デザインシステムの考え方）。
  *Usage: one `primary` per screen; at most three outlined buttons together (more means rethinking the flow); Cancel is `secondary`. Importance is shown by shape (fill, outline, none), not color alone (after the Digital Agency DS).*
- 配置: PC では「完了」「次へ」を右、「キャンセル」「戻る」を左。スマホでは縦に積み、主なボタンを一番上にする。
  *Placement: on desktop progress actions go right and cancel/back go left; on mobile stack vertically with the primary on top.*
- 無効化は極力避ける。押せない理由が分からないと、操作が止まる。どうしても無効にするときは、ボタンのすぐ近くに理由か有効にする条件を書き、`aria-describedby` で結ぶ。`disabled` は `aria-disabled` で実装してあり、Tab キーで届き、押しても何も起きない。
  *Avoid disabling. If unavoidable, write the reason or condition next to the button and link it with `aria-describedby`. `disabled` is implemented with `aria-disabled`: it stays reachable by Tab and does nothing when pressed.*
- やること: ラベルは 2〜4 文字の動詞。破壊的操作は確認ダイアログで受ける。
  *Do: short verb labels; confirm destructive actions in a dialog.*
- やらないこと: プライマリの並置、`disabled` の理由を示さないまま放置。
  *Don't: place several primaries together, or leave a disabled button unexplained.*

**理由 / Why:** 前は 6 種類あり、`secondary` と `outline`（面の色だけが違う）、`subtle` と `transparent`（文字の色だけが違う）の差は、見ても使い分けの理由が言えなかった。形（塗り・枠・枠なし）が重要度にそのまま対応する 3 つと、取り消せない操作の 1 つに絞った。「キャンセル」を紺の文字にすると、やめる操作がいちばん目立ってしまうので枠にした。
*Six kinds had two pairs that differed only in fill or text colour, with no reason to choose. Three shapes map to importance, plus one for irreversible actions; Cancel is outlined so that quitting is not the most eye-catching action.*
