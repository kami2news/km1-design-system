順序のある複数の工程を、利用者が入力しながら進める。工程の一覧（完了・現在・エラー・未完了）、今の工程の見出しと中身、「戻る」「次へ」。M1 の Steppers を KM1 に合わせたもの。システムの処理を待つ工程は `Progress`（`steps`）。
*A user-driven multi-step flow: the step list (done, current, error, to do), the current step's heading and content, Back and Next. Adapts M1 Steppers. Waiting on system work is `Progress` (`steps`).*

## 使う条件 / When to use

- 3 工程以上で、各工程の中身がはっきり違うとき（申し込み、初期設定）。前の答えで次の内容が変わるときにも向く（M1 Steppers）。
  *Three or more clearly different steps; good when earlier answers shape later steps.*
- 使わない: 1 画面で済むフォーム（`FormGroup` で区切る）、2 工程以下、同じ階層の表示の切り替え（`Tabs`）。StepFlow の中に StepFlow を入れない・1 画面に 2 つ置かない（M1 Steppers）。
  *Not for single-page forms, two steps or view switching (`Tabs`). Never nest flows or put two on one screen.*

## 型 / Modes

| 型 / Mode | 進み方 / Navigation | 例 / Example |
|---|---|---|
| 順番どおり `linear`（既定） | 前の工程を終えないと次へ進めない。終えた工程には戻れる（`editable: false` の工程は戻れない） | 申し込み |
| 自由 `nonlinear` | どの工程にも移れる | 設定の見直し |

- 任意の工程は `optional: true`（「任意」と表示）。工程の途中の入力は、`useForm` の値を工程をまたいで持ち、利用側で下書き保存する（再読み込み・画面の回転・戻る操作で消えないよう、`sessionStorage` かサーバーに保存）。
  *`optional` steps are labeled. Keep values across steps (e.g. `useForm`) and save drafts so reloads, rotation and Back don't lose them.*
- 「次へ」で確かめる。誤りがあれば進まず、その工程を `errors` に入れ、フォームの規則どおり `ErrorSummary` と欄のエラーを出す。
  *Validate on Next; on errors stay, mark the step in `errors` and show ErrorSummary plus inline errors.*

## 状態 / States

番号の丸（未完了・枠だけ）、現在（`brand` の丸に白い番号・太字）、完了（チェックのアイコン）、エラー（エラーのアイコン・`danger-tint`）、任意（「任意」の文字）。色だけでなく、アイコン・番号・読み上げの言葉で区別する。
*Numbered ring (to do), filled brand circle (current), check icon (done), error icon (error), "任意" text (optional) — never color alone.*

## キーボード・読み上げ / Keyboard and screen readers

- 工程の一覧は `nav`（名前は `label`）の中の `ol`。今の工程に `aria-current="step"`。各工程に「（2 / 4、完了）」のような状態を読み上げ用に付ける。移れる工程だけ button、移れない工程は文字。
  *An `ol` inside a named `nav`; `aria-current="step"`; each step carries "(2 / 4, done)" for screen readers; only reachable steps are buttons.*
- 工程が変わったら、新しい工程の見出し（`h2`、`tabIndex=-1`）へフォーカスを移す。見出しは「手順 2 / 4」と工程名。
  *On step change, focus moves to the new step heading ("手順 2 / 4" + name).*

## 幅 / Responsive

本体の幅が 560px 以上なら横並び、未満なら縦並び（M1 も狭い画面は縦）。M1 のスマホ用の「点」だけの表示は使わない（工程名が分からないため）。
*Horizontal at 560px+ (container), vertical below. No dots-only mobile stepper (step names would be lost).*

## トークン / Tokens

丸 24px（`radius-circular`）、`brand`・`on-brand`、`brand-ink`、`danger-ink`・`danger-tint`、`stroke`（つなぐ線）、見出し `subtitle-1`（20/28）、`space-xxl`（一覧と本体の間）。
*24px circles, brand/on-brand, brand-ink, danger tokens, `stroke` connectors, `subtitle-1` heading, `space-xxl`.*

## API

```jsx
<StepFlow label="見学の申し込み" steps={[{id:'who',title:'参加者'},{id:'when',title:'日時'},{id:'opt',title:'持ち物',optional:true},{id:'ok',title:'確認'}]}
  active={step} completed={done} errors={errs} onStepChange={setStep}
  onBack={back} onNext={next} onFinish={submit} finishLabel="申し込む">{content}</StepFlow>
```

`steps`（`{id, title, optional?, editable?, description?}`）、`active`、`completed`、`errors`、`mode`（`linear`・`nonlinear`）、`onStepChange`、`onBack`・`onNext`・`onFinish`、`nextLabel`・`backLabel`・`finishLabel`、`busy`、`label`。
Flutter: `Km1StepFlow`（`steps`（`Km1Step`）・`active`・`completed`・`errors`・`linear`・`onStepChange`・`onBack`・`onNext`・`onFinish`）。Flutter 標準の `Stepper` は Material の見た目のため使わない。

## してはいけないこと / Don't

- 工程の名前を長くする（4〜8 文字程度）。 *Long step names.*
- 「次へ」を押せなくして理由を言わない。 *Disable Next without saying why.*
- 工程を移るたびに入力を消す。 *Clear input when switching steps.*

## テスト / Tests

`aria-current` が 1 つ、状態の読み上げ、順番どおり型で未着手は押せない、任意の表示、誤りで進まずエラー表示、次の工程の見出しへフォーカス、完了した工程へ戻れる、幅での縦横（8 項目、320〜1366px・ダークで合格）。
*8 checks pass at 320–1366px and dark.*
