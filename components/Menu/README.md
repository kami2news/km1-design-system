ボタンを押すと開く操作の一覧。場所を取らずに、頻度の低い操作をまとめる。
*A list of actions that opens from a button, grouping less frequent actions compactly.*

## 使い方 / Usage
- 項目は動詞で書く（「編集」「複製」「削除」）。7 個以内にする。取り消せない操作は `danger` にして最後に置き、押したあと `Dialog` で確認する。
  *Verb labels, seven items at most. Irreversible actions are `danger`, placed last, and confirmed in a `Dialog`.*
- 主な操作はメニューに隠さず、ボタンとして外に出す。
  *Never hide the main action in a menu; keep it as a visible button.*
- アイコンだけのボタン（「⋯」）にするときは `iconOnly` と `label` を渡す。`label` が読み上げ名になる。
  *For an icon-only trigger pass `iconOnly` and `label`; `label` becomes the accessible name.*
- キーボード: ↓・Enter・Space で開く、↑↓ で移動、Home・End、Esc で閉じてボタンに戻る（W3C APG の Menu Button）。
  *Keyboard: Down/Enter/Space opens; Up/Down move; Home/End; Esc closes and returns focus (W3C APG Menu Button).*
- 値を選ぶ用途（都道府県など）には使わない。`Select` を使う。
  *Not for choosing a value: use `Select`.*

## 利用側が渡すもの / You provide
`label`、`items`（`{label, onSelect, icon?, danger?, disabled?}` の配列）、必要なら `icon`・`iconOnly`・`align`（`start`・`end`）・`appearance`。

**理由 / Why:** 頻度の低い操作で画面を埋めたくない。ボタンの近くに開き、選んだら閉じる。場所を取らない。
*Rare actions should not fill the screen: opens by its button and closes after a choice.*
