候補から複数を選ぶ欄。選んだものはタグとして並び、1 つずつ外せる。
*Pick several options; choices appear as removable tags.*

## 使い方 / Usage
- 選択肢が少ない（5 個以下）なら `Checkbox` を並べるほうが早い。多い、または名前で探したいときに `TagPicker`。
  *For five or fewer options use `Checkbox`es; `TagPicker` is for many options or searching by name.*
- 入力すると候補が絞られ、↓↑で選んで Enter で追加。空の欄で Backspace を押すと最後のタグが外れる。追加・削除は読み上げにも伝わる。
  *Type to filter, arrows and Enter to add; Backspace in an empty field removes the last tag; changes are announced.*
- タグの「×」の読み上げ名は「（タグ名）を外す」。スマホでは押せる範囲を 44px に広げてある。
  *Each × is named "(tag) を外す" and gets a 44px hit area on touch.*
- 数に上限があるなら `max` を渡す。超えたときは入力を止めず、「選べるのは 3 個までです」と知らせる。
  *`max` sets a limit; exceeding it is announced, not silently blocked.*
- 自由入力のタグ（新しいタグを作る）は、このバージョンでは受け付けない。
  *Free-text tag creation is not supported in this version.*

## 利用側が渡すもの / You provide
`label`、`options`（`{value, label}`）、`value`（選んだ value の配列）、`onChange`、必要なら `placeholder`・`hint`・`error`・`required`・`max`。

**理由 / Why:** 候補から複数を選ぶ。選んだものがタグで並び、何を選んだか一目で分かる。
*Pick several from suggestions: choices line up as tags, so what you picked is visible at a glance.*
