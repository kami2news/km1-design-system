KM1 のアイコン（KM1-ICO-001）。KM1 の名前で引く 1 つのセットで、通常表示（線と淡い面）も選択・強調の塗りの形（Filled）も KM1 B 案で KM1 が描いた形（もとにした絵は Fluent System Icons、Microsoft、MIT）。描き方と一覧は本編「アイコン」の章。
*KM1 icons (KM1-ICO-001): one set addressed by KM1 names, Regular and Filled are both drawn by KM1 in the B style (based on Fluent pictograms, MIT). Rules and the full list are in the Icons chapter.*

利用側が渡すもの: `name`（KM1 の名前）、`size`（16・20・24・32、標準 20）、`filled`（選択中・強調のとき）、`label`（アイコンだけで意味を持つときの読み上げの名前）。名前の一覧は `ICONS`（名前 → 日本語の名前）。
*Consumer provides: `name`, `size` (16/20/24/32, default 20), `filled` (selected or emphasized), `label` (only when the icon stands alone). `ICONS` maps names to Japanese labels.*

## 使い方 / Usage

- 標準は 20px の Regular。小さな場所は 16px、ナビと上部バーは 24px、空の状態だけ 32px。
  *20px Regular by default; 16px small, 24px navigation, 32px only in empty states.*
- 通常表示の色は `icon-ink`。押す・選ぶ・無効・強い背景の上では親の文字色に従う。部品の中のアイコン（`icon16`・`icon20`）は部品の文字色に従う。状態の記号だけ状態の色（`info-ink` など）にしてよい。
  *Rest color `icon-ink`; states and icons inside parts follow the text color; only status symbols take a status color.*
- 文字の横に置くときは `label` を付けない。アイコンだけのボタンはボタン側に `aria-label` とツールチップを付ける。
  *No `label` next to text; icon-only buttons put `aria-label` and a tooltip on the button.*
- Flutter は `Km1BIcon(Km1BIconName.deadline)`（`size`・`filled`・`inherit`・`color`）。`Icon(Km1Icons.deadline)` はフォントの字形（B 案の形、1 色で淡い面なし）なので、通常表示は `Km1BIcon` を使う。
  *Flutter: `Km1BIcon(Km1BIconName.deadline)`; `Icon(Km1Icons.deadline)` is the single-color B glyph without the tint; use `Km1BIcon` for regular display.*

**理由 / Why:** 言葉の横で、意味を速く見分ける。KM1 の線と淡い面の形。必ず言葉と組み、アイコンだけで意味を伝えない。
*Recognise meaning quickly beside words: KM1 line-and-tint shapes, always with a word, never alone.*
