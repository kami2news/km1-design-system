フォームの中の 1 つのまとまりに見出しを付ける。間隔は「欄の間 < グループの間」になるよう決めてあり、枠や背景は付けない。全体の決まりは「画面の組み立て › フォーム」。
*Gives one cluster of a form its heading. Spacing is set so field gaps are smaller than group gaps, with no border or background. Overall rules: Patterns › Forms.*

利用側が渡すもの: `title`、子の欄。必要なら `description`、`as="fieldset"`、`headingLevel`。
*Consumer provides: `title` and the fields. Optionally `description`, `as="fieldset"`, `headingLevel`.*

- 目的: 長いフォームを意味のある塊に分け、見出しで飛べるようにする。
  *Purpose: split a long form into meaningful chunks that screen-reader users can jump between by heading.*
- 構造: 通常は `<section aria-labelledby>` + `<h2>`。1 つの問いに答える組（ラジオの組、生年月日の 3 欄）は `as="fieldset"` にして `<legend>` で問いを読ませる（WCAG 1.3.1、W3C H71）。fieldset を入れ子にしない。
  *Structure: a `<section aria-labelledby>` with an `<h2>` by default. For controls that answer one question, use `as="fieldset"` so the `<legend>` is read (WCAG 1.3.1, W3C H71). Don't nest fieldsets.*
- 状態: 持たない。中の欄がそれぞれ通常・エラー・無効を持つ。
  *States: none of its own; each field has its own default, error and disabled states.*
- キーボード: フォーカスを受けない。Tab は中の欄を DOM の順にたどる。
  *Keyboard: not focusable itself; Tab walks the fields in DOM order.*
- 幅: 親の `.f2-form`（最大 720px）に従う。スマホでも見た目は同じ。
  *Width: follows the parent `.f2-form` (max 720px); looks the same on phones.*
- ライト・ダーク: 見出しは `ink`、説明は `ink-secondary`。どちらのテーマでも 4.5:1 以上。
  *Light/dark: title uses `ink`, description `ink-secondary`; both meet 4.5:1 in either theme.*

```jsx
<form className="f2-form" noValidate onSubmit={submit}>
  <ErrorSummary errors={f.errors} focusKey={tries} />
  <FormGroup title="予定の内容" description="時間割に表示されます。">
    <Input label="タイトル" required {...f.field('title')} />
  </FormGroup>
  <FormActions>
    <Button>キャンセル</Button>
    <Button appearance="primary" type="submit">登録する</Button>
  </FormActions>
</form>
```

`FormActions`: 子を PC の並び（左から: キャンセル … 主ボタン）で渡す。PC は右寄せで横並び、幅 479px 以下は縦に積み、DOM の順ごと逆にして主ボタンを上にする（Tab の順と見た目が一致する）。
*`FormActions`: pass children in PC order (Cancel … primary). On PC they sit right-aligned in a row; at 479px and below they stack and the DOM order is reversed so the primary is on top and Tab order still matches.*

`.f2-form--contained` を付けると、ダイアログやドロワー向けの詰めた間隔（欄 16px・グループ 32px）になる。
*Add `.f2-form--contained` for the tighter spacing used in dialogs and drawers (16px fields, 32px groups).*

してはいけないこと / Don't:

- グループごとにカードや枠で囲む。 *Box each group in a card or border.*
- 見出しだけ大きくして `<h2>` を使わない（見出しで飛べなくなる）。 *Fake a heading with large text instead of a real heading element.*
- 1 項目しかないのにグループにする。 *Make a group for a single field.*

**理由 / Why:** 長いフォームを区切る。枠ではなく見出しと余白で区切る（欄の間 < グループの間）。
*Break up long forms: headings and space, not boxes (gap inside < gap between).*
