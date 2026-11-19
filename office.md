# Word と PowerPoint の規定 / Word and PowerPoint

KM1-DOC-002（Word）と KM1-DOC-003（PowerPoint）。KM1 で作る Word の文書と PowerPoint のスライドの決まり。色・文字の大きさ・余白は KM1 のトークンと「PDF の規定」（KM1-DOC-001）から取り、新しい値は作らない。
*KM1-DOC-002 (Word) and KM1-DOC-003 (PowerPoint). Colors, type sizes and spacing come from KM1 tokens and the PDF rules (KM1-DOC-001); no new values.*

道具は `office/` にある: ひな形と見本を作る `km1_docx.js`・`km1_pptx.js`、検査 `officecheck.py`。できあがったひな形は `KM1_文書.dotx`・`KM1_スライド.potx`、見本は `KM1_文書見本.docx`・`KM1_スライド見本.pptx`。
*Tools are in `office/`: generators `km1_docx.js` and `km1_pptx.js`, checker `officecheck.py`. Outputs: the `KM1_文書.dotx` and `KM1_スライド.potx` templates and two sample files.*

## 1. どれで作るか / Which format

| 用途 / Use | 形 / Format |
|---|---|
| 配る・残す・印刷する完成した文書 / Final documents to hand out or keep | PDF（「PDF の規定」）。Word で書いたものも PDF にして配る |
| 人と一緒に直す文書、提出先が Word を求める文書 / Documents edited together, or required as Word | Word（.docx） |
| 人の前で話すときの資料 / Slides for a talk | PowerPoint（.pptx）。配るときは PDF にする |
| 画面で読むもの・あとで直すもの / Read on screen, edited later | Web ページか共有ドキュメント |

## 2. 共通の決まり / Common rules

| 項目 / Item | 決まり / Rule |
|---|---|
| 書体 / Font | **游ゴシック**（和文も英数字も同じ書体）。Windows と macOS の両方に入っていて、Office でそのまま表示できる。KM1 の画面の第一候補の Noto Sans JP は Office にも OS にも入っていないため、Office では使わない。テーマの書体（見出し・本文とも）を游ゴシックにし、文字ごとに書体を指定しない / Yu Gothic for both scripts, set as the theme font。言語ごとの補助の書体（テーマの `<a:font script=…>`）も、Office の既定に入っている明朝・セリフ体・手書き風（新細明體・Times New Roman・Angsana New・MV Boli など）をゴシック系に置き換える（`tokens.md` 7 章）。明朝体・游明朝は使わない |
| 色 / Colors | テーマの色を KM1 にする: 文字 `ink` #242424、濃い 2 `brand` #10218B、淡い 2 #F5F5F5、アクセント 1〜6 は #10218B・#0F6CBD・#038387・#BC4B09・#5C2E91・#107C10（どれも白地で 3:1 以上）、リンク #10218B。この表と `officecheck.py` の色の一覧にない色は使わない / KM1 theme colors only |
| 文字のコントラスト / Contrast | 文字は背景と 4.5:1 以上。薄い灰色の文字は #616161（`ink-tertiary`）まで / text 4.5:1 or more |
| 色だけで伝えない / Not color alone | グラフは値を書き込み、凡例の代わりに系列の名前を線や棒の横に書く。状態は言葉かアイコンを添える（WCAG 1.4.1） |
| 言語 / Language | 文書の言語を日本語（ja-JP）にする。英語の段落には英語を指定する |
| 個人情報 / Personal data | 外に出すファイルは作成者・最終更新者を空にする（「ファイル › 情報 › 問題のチェック › ドキュメント検査」）。見本の名前は架空にする |
| 暗号化 / Protection | パスワードや編集の制限をかけない（読み上げソフトが読めなくなることがある） |
| ファイル名 / File name | `<文書名>_<YYYY-MM-DD>.docx`・`.pptx`。空白を入れない |

## 3. Word / KM1-DOC-002

**ページ / Page:** A4 縦、余白は上下 20mm・左右 17mm（「PDF の規定」と同じ）。1 段組み。表紙は柱とページ番号を出さない。2 ページ目から、上に文書名（左）と版の日付（右）、下中央にページ番号。
*A4 portrait, 20mm top and bottom, 17mm sides, single column; no header or page number on the cover.*

**文字 / Type**（スタイルの名前で使う / apply as styles）

| スタイル / Style | 大きさ・太さ・色 | 行送り | 用途 |
|---|---|---|---|
| 表題 / Title | 28pt・太字・#10218B | 1.3 | 表紙の題名。上に 22 × 6mm の紺のしるし（塗りの段落）|
| 副題 / Subtitle | 13pt・#424242 | 1.7 | 表紙の副題 |
| 見出し 1 / Heading 1 | 20pt・太字・#10218B、下に 2pt の線、改ページして始める | 1.3 | 章 |
| 見出し 2 / Heading 2 | 13pt・太字 | 1.4 | 節 |
| 見出し 3・4 | 11pt・10pt・太字 | 1.7 | 小見出し |
| 標準 / Normal | 10pt | 1.7 | 本文 |
| KM1 英語 / English | 9pt・#616161、言語は英語 | 1.55 | 英語の併記 |
| KM1 表の文字 / Table text | 9pt | 1.55 | 表の中 |
| 図表番号 / caption | 8.5pt・#424242 | 1.55 | 図と表の説明 |
| 柱・ページ番号 | 8pt・#616161 | — | ヘッダーとフッター |

- 使う大きさは 8・8.5・9・10・11・13・20・28pt だけ。8pt より小さくしない。
  *Only these sizes; nothing below 8pt.*
- 見出しは「見出し 1〜4」のスタイルだけで作り、段を飛ばさない（見出し 1 の次は見出し 2）。太字にしただけの段落を見出しの代わりにしない。目次とナビゲーション ウィンドウは見出しのスタイルから作られる。
  *Headings use Heading 1–4 only, never skipping a level; no bold paragraphs as fake headings.*
- 箇条書きと番号は Word の機能で付ける。「・」や「1.」を手で打たない。
  *Use list formatting; never type bullets or numbers.*
- 表は 1 行目を見出しにして「タイトル行の繰り返し」をオンにし、行の途中で改ページしない。セルを結合しない。見出しのセルは #F0F0F0、罫線は #D1D1D1 の 0.5pt。
  *First row is a repeating header row; no merged cells.*
- 図には代替テキストを付ける。飾りの図は「装飾用にする」にチェックする。文字を図にしない。図と表の下に図表番号を付ける。
  *Alt text on every figure; mark decorative ones as decorative; captions below.*
- 空の段落を重ねて間をあけない。間はスタイルの段落前後の間隔で取る。
  *No empty paragraphs for spacing.*
- 英語の併記は日本語の段落のすぐ下に「KM1 英語」のスタイルで置く（画面と PDF と同じ並び）。

**PDF にするとき / To PDF:** 「PDF の規定」§8 の「Word から」の手順で書き出し、`pdfcheck.py` にかける。

## 4. PowerPoint / KM1-DOC-003

**スライド / Slide:** 16:9（33.867 × 19.05cm、960 × 540pt）。**1pt を KM1 の 1px として、トークンの値をそのまま使う。** 大きさと余白は、少し離れた画面に映して読む前提で決める（2026-11-19 に引き上げ。出典はこの文書の末尾）。
*16:9, 960 × 540pt; 1pt = 1 KM1 px. Sizes and spacing assume a projected screen read from a distance (raised 2026-11-19; sources at the end).*

### 4.1 文字 / Type

KM1 の型の表の大きさと行送りだけを使う / only KM1 type-ramp sizes and line heights

| 役割 / Role | 大きさ・行送り / Size, line | KM1 の型 |
|---|---|---|
| 大きな数字（1 枚に 1 つ）/ Hero number | 68pt・太字、行送り 92 | display |
| 表紙・章の区切りの題名 / Cover, section title | 40pt・太字、行送り 52、2 行まで | large-title |
| スライドの題名 / Slide title | 32pt・太字、行送り 40、**1 行**・左寄せ | title-1 |
| 本文・箇条書き / Body | 24pt・標準、行送り 32、項目の間 12〜16 | title-3 の大きさ・標準の太さ |
| 補足・英語・表・グラフ・カードの説明 / Notes, English, tables, charts | 20pt・行送り 28 | subtitle-1 の大きさ |
| 柱・スライド番号 / Footer, slide number | 14pt・#616161、行送り 20 | body-1 |

- **内容の文字は 20pt 以上。** 14pt は下の柱の行（柱とスライド番号）だけ。Microsoft は 18pt 以上、投影するときの多くの指針は 24pt 以上を求めるので、本文を 24pt、それ以外の内容を 20pt にした。
  *Content text 20pt or more; 14pt only in the footer row. Microsoft asks for 18pt or more; most projection guidelines ask for 24pt, so body is 24pt.*
- 入りきらないときは文字を縮めない。言葉を削るか 2 枚に分ける（PowerPoint の「自動調整」で縮んだ文字は検査で FAIL になる）。
  *Never shrink to fit; cut words or split the slide.*
- 題名は 1 行。32pt で 1 行に入るのは全角 27 字（半角は 0.55 字に数える）まで。
  *Titles fit on one line: 27 full-width characters at 32pt.*
- 本文は左寄せ。中央寄せは使わない（題名も左寄せ）。
  *Left-aligned text, titles included.*

### 4.2 余白とグリッド / Spacing and grid

どの値も 4 の倍数で、KM1 の余白のトークン（`space-*`）か、その和。
*All values are multiples of 4 built from KM1 spacing tokens.*

| 場所 / Zone | 値（pt） / Value | 内訳 |
|---|---|---|
| 左右の余白 / Side margins | 48 | `space-xxxl` 32 ＋ `space-lg` 16 |
| 上の余白 / Top margin | 40 | `space-xxxl` ＋ `space-sm` |
| 題名の行 / Title row | 40（y 40〜80） | 32pt の 1 行 |
| 題名と本文の間 / Title–body gap | 24 | `space-xxl`（`layout-section-gap`） |
| **本文の領域 / Body area** | **x 48・y 104、864 × 368** | 図・表・カード・本文はここに入れる |
| 本文と柱の間 / Body–footer gap | 24 | `space-xxl` |
| 柱の行 / Footer row | 20（y 496〜516） | 14pt の 1 行 |
| 下の余白 / Bottom margin | 24 | `space-xxl` |

**12 列のグリッド / 12-column grid:** 本文の領域の幅 864 を、列 50・溝 24 の 12 列に分ける（列の左端は x ＝ 48 ＋ 74 × n）。図・表・カード・テキスト ボックスの左右の端は列の端にそろえる。よく使う分け方:
*864pt split into 12 columns of 50 with 24 gutters; left and right edges of every object sit on column edges.*

| 分け方 / Split | 幅 / Widths | 使う場面 |
|---|---|---|
| 12 | 864 | グラフ・表・大きな図 |
| 6 ＋ 6 | 420 ＋ 420 | 2 段（比べる・並べる） |
| 8 ＋ 4 | 568 ＋ 272 | 図と説明（図が左） |
| 4 ＋ 4 ＋ 4 | 272 × 3 | カード 3 枚 |
| 3 × 4 | 198 × 4 | カード 4 枚・手順 |

**縦の分け方 / Vertical:** 本文の領域は 1 段（368）か、上下 2 段（172 ＋ 間 24 ＋ 172）。
*The body area is one row of 368 or two rows of 172 with a 24 gap.*

### 4.3 空間の使い方 / Using the space

- **はみ出さない:** 本文の領域の外（題名の行・柱の行・余白）に図や文字を置かない。柱に重なるものは検査で FAIL。
  *Nothing outside the body area; overlapping the footer is a FAIL.*
- **図・表・カードは領域に合わせる:** グラフと図は列の幅（12・8・6 列）と段の高さ（368 か 172）いっぱいに置く。カードは段の高さに合わせ、内側の余白は 24（`container-card-padding-spacious`）、数字や見出しは上、説明は下にそろえる。表は行の高さを 368 ÷ 8 ＝ 46 か 40 にして上から詰める。図・表・カードだけのスライドで本文の領域の下半分が空いていたら、大きさか分け方を見直す（検査で注意）。
  *Charts and figures fill their columns and row; cards match the row height with 24 padding, top/bottom aligned content; tables use 46 or 40 rows from the top.*
- **文字だけのスライドは上から詰める:** 本文は本文の領域の上にそろえる（縦の中央にしない）。下の空きは読みやすさのための余白としてそのまま残し、文字を大きくしたり間を広げたりして埋めない。
  *Text slides start at the top of the body area; leftover space stays empty.*
- **量の上限:** 箇条書きは 1 枚に 6 項目まで（1 項目は 2 行まで）。超えたら 2 枚に分け、題名に「（2/2）」を付ける。
  *At most six bullet items, each up to two lines; split beyond that.*
- **余白の役割を混ぜない:** 項目の間 12〜16（`space-md`〜`space-lg`）＜ まとまりの間 24（`space-xxl`）＜ 領域の間 32 以上。近いものほど間を狭くする。空の段落や空白の文字で間をあけない。
  *Item gaps < group gaps < region gaps; never space with empty paragraphs.*

### 4.4 レイアウト / Layouts

ひな形に 6 つある。スライドは必ずこのどれかから作る。
*Six layouts in the template; every slide uses one.*

| レイアウト / Layout | 使う場面 |
|---|---|
| KM1 表紙 / Title | 1 枚目。題名・副題・版の日付と作成者。左上に表紙のしるし（PDF と同じ大きさ）|
| KM1 区切り / Section | 章の始め。背景 #F5F5F5、章の番号と題名 |
| KM1 題名と本文 / Title and content | 箇条書き・説明（12 列） |
| KM1 2 段 / Two columns | 比べる・並べる（6 ＋ 6 列） |
| KM1 図と説明 / Figure and text | 左 8 列に図・グラフ、右 4 列に説明 |
| KM1 題名だけ / Title only | グラフ・表・図・数字のカード |

### 4.5 そのほか / Other rules

- 題名は全部のスライドに付け、題名のプレースホルダーに入れる。同じ題名を 2 枚に使わない（続きは「（2/2）」を付ける）。題名だけを読んで話の筋がわかるようにする。
  *Every slide has a unique title in the title placeholder.*
- 1 枚に伝えることは 1 つ。
- 文字はプレースホルダーに入れる。自分で置いたテキスト ボックスは読み上げの順が崩れやすいので、使ったら「校閲 › アクセシビリティ チェック」から開く［閲覧順序］ウィンドウで、見た目の順に直す。
  *Prefer placeholders; fix reading order when adding text boxes.*
- グラフは PowerPoint のグラフで作り（画像にしない）、色はテーマのアクセントの順、値を書き込む。軸と値の文字は 20pt・#424242、目盛りの線は #E0E0E0。
  *Native charts with theme accents and data labels.*
- グラフの系列が 2 つ以上あるときは、色に加えて模様で分ける（KM1-COL-001）。系列の「塗りつぶし › パターン」で、1 つ目は塗りつぶし、2 つ目から横線（太）`dkHorz`・縦線（太）`dkVert`・右下がり対角線（太）`wdDnDiag`・格子（小）`smGrid`・斜め格子 `diagCross`・点線: 格子 `dotGrid`・市松模様（大）`lgCheck` の順。前景色は系列の色、背景色は白、枠線は #616161 の 0.75pt。見本の `km1_pptx.js` はこの順で書き込む。
  *With two or more series, add patterns (KM1-COL-001) in this order; foreground = series color, background = white, outline #616161.*
- 表は「タイトル行」をオンにし、見出しの行は #F0F0F0 と太字、罫線は #D1D1D1。セルを結合しない。
- カードの角丸は 8pt（`radius-xl`）、塗りは #F5F5F5 か #ECEFFC。影や帯・縁の色の線は付けない（KM1 は大きな面の塗りを避ける）。
  *Cards use 8pt corners and flat tints; no shadows, stripes or edge bars.*
- アニメーションと画面切り替えの効果は使わない（KM1 の動きの決まり: 動かしてよいのは色・不透明度・8px までの移動だけ。スライドでは使う理由がない）。
  *No animations or transitions.*
- 話す内容はノートに書く。スライドに長い文を載せない。

**配るとき / Handing out:** PDF にして配る。「名前を付けて保存 › PDF › オプション」で「アクセシビリティ用のドキュメント構造タグ」をオンにし、`pdfcheck.py` にかける（スライドの比率のままなので A4 の項目は注意として出る）。

## 5. 作り方 / How to make one

1. ひな形から始める: Word は `KM1_文書.dotx`、PowerPoint は `KM1_スライド.potx` を開いて（ダブルクリックで新しいファイルになる）書く。
   *Start from the templates.*
2. ひな形を作り直すとき: `node km1_docx.js <出力先>`、`node km1_pptx.js <出力先>`（`docx`・`pptxgenjs` が必要。テーマの色は `km1_pptx.js` が自分で書き込む）。トークンを変えたら、ここの値も合わせて変える。
   *Regenerate with the scripts; keep values in step with tokens.*
3. 検査: `python3 officecheck.py <ファイル>`。FAIL が 0 になるまで直す。
   *Run `officecheck.py` until there are no FAILs.*

## 6. 検査 / Checking

**機械の検査 / Machine checks** — `officecheck.py` が調べる:

| 対象 | 項目 |
|---|---|
| 両方 | 文書の題名、作成者が空か（注意）、テーマの和文・欧文の書体が游ゴシック、言語ごとの補助の書体に明朝・セリフ体・手書き風がない、テーマの色が KM1 の色 |
| Word | 既定の言語が日本語、見出しのスタイルがある・段が飛ばない、太字だけの見出しもどき（注意）、手で打った「・」、文字の大きさが §3 の値、8pt 未満、文字の色が KM1 の色、図の代替テキスト、表の見出し行の繰り返し、セルの結合、「こちら」のようなリンクの文字、A4 |
| PowerPoint | 16:9、全部のスライドに題名、題名の重複、図・グラフの代替テキスト、表のタイトル行（注意）とセルの結合、文字の大きさが §4.1 の値、14pt が柱の行の外にない、文字と図形の色が KM1 の色、言語の指定（注意）、アニメーション・画面切り替え（注意）。§4.2〜4.3 の割り付け: 本文の領域の下へのはみ出し（FAIL）、題名の行への食い込み・12 列のグリッドからのずれ・題名が 1 行に入らない・箇条書きが 7 項目以上・図だけのスライドの下半分の空き（どれも注意） |

FAIL があると終了コード 1 を返す。
*Exits 1 on any FAIL.*

**Office の検査 / Office's checker:** Word と PowerPoint の「校閲 › アクセシビリティ チェック」で、エラーと警告を 0 にする。`officecheck.py` は読み上げの順やコントラストの全部は見ない。
*Clear Office's Accessibility Checker too.*

**人の目の検査 / Human checks**

- [ ] 読み上げの順（PowerPoint の［閲覧順序］ウィンドウ）が見た目の順と同じ / reading order matches visual order
- [ ] 代替テキストが図の中身を伝えている / alt text conveys the figure
- [ ] 白黒で印刷しても区別できる / distinguishable in grayscale
- [ ] スライドの題名だけで話の筋がわかる / slide titles alone tell the story
- [ ] ファイルのプロパティに個人情報が残っていない / no personal data in properties

**確かめたこと / Verified (2026-11-19)** — 文字の大きさと割り付けを改めた版のひな形と見本が `officecheck.py` で FAIL 0・注意 0、LibreOffice で PDF にして全ページを目で見た。以前（2026-11-13） — ひな形 2 つと見本 2 つが `officecheck.py` で FAIL 0、Office Open XML の形式の検査（XSD・関係・中身の種類）に合格。LibreOffice で PDF にして全ページを目で見た（游ゴシックがないので Noto Sans CJK JP で表示。文字の幅は Office と少し違う）。**まだ確かめていないこと:** Microsoft Word・PowerPoint で開くこと、Office のアクセシビリティ チェック、PowerPoint で書き出した PDF のタグ。
*Templates and samples pass `officecheck.py` and OOXML validation, and were rendered with LibreOffice (Noto Sans CJK JP substituted for Yu Gothic). Not yet checked in Microsoft Office itself.*

出典 / Sources: [Microsoft: PowerPoint のプレゼンテーションをアクセシビリティ対応にする（18pt 以上）](https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25)・[NYC MOPD: Accessible Slidedecks Guide（24pt 以上）](https://www.nyc.gov/site/mopd/publications/guides/accessible-slidedecks-guide.page)・[Indiana University: PowerPoint（24pt 以上）](https://accessibility.iu.edu/creating-content/documents/powerpoint/index.html)・[Microsoft: アクセシビリティ チェックのルール](https://support.microsoft.com/ja-jp/Accessibility/office-accessibility/rules-for-the-accessibility-checker)・[Microsoft: PowerPoint のプレゼンテーションをアクセシビリティ対応にする](https://support.microsoft.com/ja-jp/Accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities)・[Microsoft: 閲覧順序ウィンドウ](https://support.microsoft.com/ja-jp/powerpoint/make-slides-easier-to-read-by-using-the-reading-order-pane)・[W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
