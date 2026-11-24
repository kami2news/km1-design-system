前の答えによって必要になる欄を、その答えのすぐ下に出す。
*Shows fields that an earlier answer makes necessary, right below that answer.*

利用側が渡すもの: `show`（出すかどうか）、子の欄、`announce`（出たときに読ませる文）。必要なら `announceHide`。
*Consumer provides: `show`, the fields, and `announce` (what to read out when they appear). Optionally `announceHide`.*

- 出たとき: フォーカスは動かさない。`role="status"`（polite）で `announce` を読ませる。既定は「入力項目が追加されました」。具体的に「『教室』の入力欄が追加されました」と書く。
  *On show: focus stays put; `announce` is read through a polite `role="status"`. The default is generic, so name the field.*
- 消えたとき: 既定では何も読ませない。`announceHide` を渡したときだけ読む。
  *On hide: silent by default; reads `announceHide` only if given.*
- 値: 部品は値を持たない。`useForm` の `when` に同じ条件を書くと、隠れた欄は検証も送信もされない。値は残るので、答えを戻すと元に戻る。消したいときだけ `resetOnHide`。
  *Values: the component holds none. Put the same condition in `useForm`'s `when` and hidden fields are skipped by validation and submission. Values are kept and come back when the answer is switched back; use `resetOnHide` only when they must be cleared.*
- 見た目: 左に `stroke-subtle` 2px の線と `space-lg` の字下げ。出るときは `duration-normal` で入る（動きを減らす設定では動かない）。強制カラーでは線を `CanvasText` にする。
  *Look: a 2px `stroke-subtle` rule with `space-lg` indent. Enters over `duration-normal` (no motion with reduced-motion). In forced colors the rule becomes `CanvasText`.*
- キーボード: 出た欄は、次の Tab でそのまま届く位置（答えの直後）にある。
  *Keyboard: the new fields sit right after the answer, so the next Tab reaches them.*

```jsx
<RadioGroup legend="種類" {...f.field('kind', { kind: 'radio' })} options={kinds} />
<ConditionalField show={f.visible('room')} announce="「教室」の入力欄が追加されました">
  <Input label="教室" required {...f.field('room')} />
</ConditionalField>
```

してはいけないこと / Don't:

- 出た欄へ自動でフォーカスを移す。 *Move focus to the new field automatically.*
- フォームの別の場所（ずっと下など）に出す。 *Reveal fields somewhere else in the form.*
- 隠した欄の値を送る、または黙って消す。 *Submit hidden values, or silently wipe them.*

**理由 / Why:** 答えによって必要な欄が変わる。必要になった欄を、その答えのすぐ下に出す。関係が位置で分かる。
*Needed fields depend on an answer: the new field appears right under that answer, so position shows the link.*
