送信して誤りがあったとき、フォームの上に件数と誤りの一覧を出す。各行は該当の欄へのリンク。
*After a failed submit, shows the count and a list of problems above the form; each line links to its field.*

利用側が渡すもの: `errors`（`{id, label, message}` の配列。`useForm` の `errors` をそのまま渡せる）、`focusKey`（送信のたびに増える数）。
*Consumer provides: `errors` (`{id, label, message}` items; `useForm().errors` fits as-is) and `focusKey` (a number that increases on each submit).*

- 出し方: `errors` が空なら何も描かない。`focusKey` が変わるたびに一覧そのものへフォーカスを移す（`tabindex="-1"`）。見出しは「入力内容を確認してください（N 件）」（GOV.UK Error summary）。
  *Behavior: renders nothing when empty. Each time `focusKey` changes, focus moves to the summary (`tabindex="-1"`). The heading reads "Check your entries (N)" (GOV.UK Error summary).*
- リンク: 押すと該当の欄までスクロールしてフォーカスする。ラジオの組（`fieldset`）なら最初の選択肢へ。
  *Links: scroll to and focus the field; for a radio group (`fieldset`) the first option.*
- 文言: 欄の横のエラーと同じ文を使う。「何がだめか」と「どう直すか」。
  *Wording: the same message as next to the field — what's wrong and how to fix it.*
- 見た目: `danger-tint` の背景、`danger-ink` の枠（左 4px）。色だけでなく見出しとアイコンでも伝える。強制カラーでは枠を `CanvasText` に。スマホではリンクの高さを 44px にする。
  *Look: `danger-tint` fill with a `danger-ink` border (4px on the left); the heading and icon carry the meaning too. Forced colors use `CanvasText`. On touch, links get a 44px target.*
- キーボード: 一覧にフォーカスが来たら、Tab でリンクを順にたどれる。
  *Keyboard: once focused, Tab walks through the links.*

```jsx
const [tries, setTries] = useState(0);
<form onSubmit={e => { setTries(t => t + 1); f.handleSubmit(save)(e); }}>
  <ErrorSummary errors={f.errors} focusKey={tries} />
  ...
</form>
```

`useForm(config)`: フォームの状態をまとめる。
*`useForm(config)`: holds the form's state.*
- `initial`・`labels`・`validate`（名前ごとに `(値, 全体) => エラー文 | null`）・`when`（名前ごとに表示条件）・`resetOnHide`。
  *`initial`, `labels`, `validate` (per name: `(value, all) => message | null`), `when` (per name: show condition), `resetOnHide`.*
- 確かめる時: 欄を離れたとき・送信時。一度触った欄は入力のたびに確かめ直す。ラジオとチェックボックスは選んだ時点で触ったことにする。
  *When it validates: on blur and on submit; a touched field re-validates on every change. Radios and checkboxes count as touched once changed.*
- `field(name, {kind})` が `id`・`name`・`value`・`onChange`・`onBlur`・`error` を返す。`kind` は `text`（既定）・`checkbox`・`radio`・`value`。
  *`field(name, {kind})` returns `id`, `name`, `value`, `onChange`, `onBlur`, `error`; `kind` is `text` (default), `checkbox`, `radio` or `value`.*
- `handleSubmit(onValid)`: 誤りがなければ、表示中の欄だけを入れた値で `onValid` を呼ぶ。`payload()` でも同じものが取れる。
  *`handleSubmit(onValid)` calls `onValid` with only the visible fields when there are no errors; `payload()` returns the same.*

してはいけないこと / Don't:

- 一覧だけ出して、欄の横にエラーを出さない。 *Show the summary without the inline errors.*
- 打っている途中に一覧を出す。 *Show the summary while the user is typing.*
- エラーのあとで入力を消す。 *Clear the user's input after an error.*
