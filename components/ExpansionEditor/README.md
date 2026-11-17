一覧の中の 1 項目を、その場で開いて直す。閉じているときは項目名と今の値、開くと入力欄と「キャンセル」「保存」。M1 の Expansion panels の「軽い編集」を取り込んだもの。閲覧だけの開閉は `Accordion`。
*Opens one item in place to edit it: collapsed shows the name and current value; open shows fields with Cancel and Save. Brings in M1 Expansion panels' "lightweight editing". View-only disclosure stays `Accordion`.*

## 使う条件 / When to use

- 設定画面やプロフィールなどで、1 項目ずつ値を見ながら直すとき。入力欄は 1〜3 個まで。
  *Settings or profile items edited one at a time, 1–3 fields each.*
- 使わない: 説明を開いて読むだけ → `Accordion`。入力欄が 4 個以上、またはスマホで画面の半分を超える → 別画面か `Drawer`。何段階もある入力 → `StepFlow`。
  *Not for read-only disclosure (`Accordion`), 4+ fields or more than half a phone screen (separate page or `Drawer`), or multi-step input (`StepFlow`).*

## 状態と動き / States and behavior

| 状態 / State | 表示 / Shows |
|---|---|
| 閉じている / collapsed | 項目名、今の値（なければ「未設定」）、「編集」 |
| 開いている / open | 入力欄、キャンセル、保存 |
| 保存中 / saving | 保存ボタンに `aria-disabled` と Spinner、文言「保存中…」 |
| 失敗 / error | パネルの中に `role="alert"` で理由。開いたまま、入力は消さない |
| 未保存で閉じようとした / dirty close | 閉じずに「変更が保存されていません…」を表示 |
| 読み取り専用 / read-only | ボタンにせず、変更できない理由を書く（`readOnlyReason`） |

- 保存に成功したら閉じて、要約を新しい値にし、見出しのボタンへフォーカスを戻し、「（項目名）を保存しました」と読み上げる。ほかの場所に結果を残す必要があるときだけ `Toast` を足す。
  *On success: collapse, update the summary, return focus to the header button and announce the save; add a Toast only if needed elsewhere.*
- `onSave` は `true`・`false`・Promise を返せる。Promise が失敗したら、そのメッセージを表示する（「何がだめか」と「どう直すか」）。
  *`onSave` may return true/false or a Promise; a rejection's message is shown.*
- 同時に開くのは原則 1 つ。別の項目を開く前に、今の項目を保存かキャンセルさせる（利用側で `open` を管理する）。
  *Keep one open at a time; the caller controls `open`.*

## キーボード・読み上げ / Keyboard and screen readers

見出し（既定 `h3`）の中の button に `aria-expanded` と `aria-controls`。開いた中身は見出しで名付けた `region`、その中の `form` なので Enter で保存できる。Esc で閉じる動きは持たない（入力中の Esc を奪わないため）。
*A button inside a heading with `aria-expanded`/`aria-controls`; the panel is a named region holding a form (Enter saves). No Esc-to-close, so Esc stays with the fields.*

## 幅 / Responsive

PC: 項目名・値・「編集」を 1 行に。479px 以下: 値を項目名の下に回す。ボタンは `FormActions` に従う（PC は保存が右、スマホは縦に積んで保存が上）。
*PC: one row; ≤479px: the value wraps under the name. Buttons follow `FormActions`.*

## トークン / Tokens

`stroke-subtle`（閉じているとき）・`stroke`（開いているとき）の 1px 枠、`radius-md`、`space-lg`、`brand-ink`（「編集」）、`danger-tint`（失敗）。
*1px `stroke-subtle`/`stroke` border, `radius-md`, `space-lg`, `brand-ink`, `danger-tint`.*

## API

```jsx
<ExpansionEditor title="表示名" summary={name} open={open} onOpenChange={setOpen}
  dirty={draft !== name} onSave={() => api.save(draft)} onCancel={() => setDraft(name)}>
  <Input label="表示名" value={draft} onChange={e => setDraft(e.target.value)} />
</ExpansionEditor>
```

`title`、`summary`、`children`、`onSave`、`onCancel`、`dirty`、`open`・`defaultOpen`・`onOpenChange`、`readOnly`・`readOnlyReason`、`saveLabel`、`savedMessage`、`headingLevel`。
Flutter: `Km1ExpansionEditor`（`title`・`summary`・`child`・`onSave`（`Future<bool>`）・`onCancel`・`dirty`・`readOnlyReason`）。

## してはいけないこと / Don't

- 中にさらに ExpansionEditor や重いフォームを入れる。 *Nest editors or heavy forms inside.*
- 保存しないまま黙って閉じる。 *Silently discard edits on collapse.*
- 外側の `<form>` の中に置く（form の入れ子になる）。 *Place it inside another `<form>`.*

## テスト / Tests

開閉の状態、未保存で閉じない、失敗の `role="alert"`、保存中、保存後に閉じて要約が変わる、フォーカスの復帰、読み上げ、読み取り専用、2 つ目の開閉、キャンセル（10 項目、320〜1366px・ダークで合格）。
*10 checks pass at 320–1366px and dark.*
