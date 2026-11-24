関係の強い短い欄を、広い画面でだけ 2 列に並べる。基本は 1 列。
*Puts short, closely related fields side by side, but only on wide screens. One column by default.*

利用側が渡すもの: 子の欄、`columns={2}`（2 列を許すとき）。全幅にしたい子には `span="full"`。
*Consumer provides: the fields, `columns={2}` to allow two columns, and `span="full"` on children that should span the row.*

- 2 列になる条件: 画面幅 1024px 以上（メディアクエリ）かつ、フォームの幅 560px 以上（コンテナクエリ、`.f2-form` が入れ物）。どちらかを満たさなければ 1 列。だからダイアログの中では PC でも 1 列のまま。
  *Two columns need both a viewport of at least 1024px (media query) and a form at least 560px wide (container query on `.f2-form`). Otherwise it's one column, so it stays single-column inside dialogs even on PC.*
- 向いている組: 姓・名、開始・終了、郵便番号・都道府県。向いていない: メール、住所、メモ（`span="full"` にする）。
  *Good pairs: family/given name, start/end, postcode/prefecture. Not suited: email, address, notes (use `span="full"`).*
- 並び: 子の順に左→右、上→下。DOM の順＝見た目の順＝Tab の順。CSS で並べ替えない。
  *Order: children flow left to right, top to bottom. DOM order = visual order = Tab order; never reorder with CSS.*
- 間隔: 縦 `space-xxl` 24px・横 `space-lg` 16px。`.f2-form--contained` の中では縦横 16px。
  *Gaps: 24px vertical (`space-xxl`), 16px horizontal (`space-lg`); 16px both ways inside `.f2-form--contained`.*
- 状態・キーボード・テーマ: 自分では持たない。中の欄に従う。
  *States, keyboard, themes: none of its own; the fields handle them.*

```jsx
<FormGrid columns={2}>
  <Input label="姓" required autoComplete="family-name" />
  <Input label="名" required autoComplete="given-name" />
  <Input label="メールアドレス" type="email" span="full" />
</FormGrid>
```

してはいけないこと / Don't:

- 関係のない欄を幅を埋めるために並べる。 *Pair unrelated fields just to fill the width.*
- 3 列以上にする。 *Use three or more columns.*
- 左列を下まで読んでから右列、という縦の流れにする（読む順が崩れる）。 *Flow down the left column then the right; it breaks reading order.*

**理由 / Why:** 短い欄の多いフォームが縦に長くなりすぎる。関係の強い欄だけ広い画面で 2 列。基本は 1 列で読む順を崩さない。
*Forms of many short fields grow too tall: only closely related fields share two columns on wide screens; one column keeps reading order.*
