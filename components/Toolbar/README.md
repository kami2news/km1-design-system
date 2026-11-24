一覧や編集画面の上に、よく使う操作を横に並べる帯。
*A strip of frequent actions above a list or editor.*

## 使い方 / Usage
- 並べるのは、その画面でよく使う操作だけ。主な操作（「予定を追加」）はツールバーに入れず、プライマリボタンとして外に置く。
  *Only frequent actions; keep the main action as a primary button outside the toolbar.*
- ツールバー全体で Tab は 1 回止まるだけで、中は左右の矢印・Home・End で移動する（W3C APG の Toolbar）。
  *One Tab stop for the whole toolbar; arrows, Home and End move inside (W3C APG Toolbar).*
- オン・オフを切り替える操作は `pressed` を渡すと、押された状態が見た目と `aria-pressed` で伝わる。
  *Toggles use `pressed`, shown visually and via `aria-pressed`.*
- アイコンだけのボタンは `iconOnly` と `label` を渡す（`label` が読み上げ名とツールチップになる）。
  *Icon-only buttons need `iconOnly` and `label`.*
- 640px 未満では `priority: 'low'` の項目が「⋯」のメニューにまとまる。消えるのではなく、メニューから同じ操作ができる。
  *Below 640px, `priority: 'low'` items move into a "⋯" menu; the same actions stay available.*
- 区切りは `{separator: true}`。
  *Separators are `{separator: true}`.*

## 利用側が渡すもの / You provide
`label`、`items`（`{label, icon?, onClick?, iconOnly?, pressed?, disabled?, priority?}` か `{separator: true}`）。

**理由 / Why:** よく使う操作をすぐ押したい。操作の対象（一覧・編集画面）の真上に、いつも同じ並びで置く。
*Frequent actions within reach: directly above what they act on, always in the same order.*
