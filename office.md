# Word と PowerPoint の規定 / Word and PowerPoint

KM1-DOC-002（Word）と KM1-DOC-003（PowerPoint）。KM1 で作る Word の文書と PowerPoint のスライドの決まり。色・文字の大きさ・余白は KM1 のトークンと「PDF の規定」（KM1-DOC-001）から取り、新しい値は作らない。
*KM1-DOC-002 (Word) and KM1-DOC-003 (PowerPoint). Colors, type sizes and spacing come from KM1 tokens and the PDF rules (KM1-DOC-001); no new values.*

道具は `office/` にある: ひな形と見本を作る `km1_docx.js`・`km1_pptx.js`、検査 `officecheck.py`、グラフの模様の画像を作る `km1_patterns.py`（出力は `office/patterns/` と `KM1_グラフの模様.zip`）。できあがったひな形は `KM1_文書.dotx`・`KM1_スライド.potx`、見本は `KM1_文書見本.docx`・`KM1_スライド見本.pptx`。
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
| 本文・箇条書き・カードの見出しと説明 / Body, card text | 24pt・標準（見出しは太字）、行送り 32、項目の間 12〜16 | title-3 の大きさ |
| 図の説明・表・グラフ・補足・英語の併記 / Captions, tables, charts, notes, English | 20pt・行送り 28 | subtitle-1 の大きさ |
| 柱・スライド番号 / Footer, slide number | 14pt・#616161、行送り 20 | body-1 |

- **内容の文字は 20pt 以上。** 14pt は下の柱の行（柱とスライド番号）だけ。Microsoft は 18pt 以上、投影するときの多くの指針は 24pt 以上を求めるので、本文を 24pt、それ以外の内容を 20pt にした。
  *Content text 20pt or more; 14pt only in the footer row. Microsoft asks for 18pt or more; most projection guidelines ask for 24pt, so body is 24pt.*
- 入りきらないときは文字を縮めない。言葉を削るか 2 枚に分ける（PowerPoint の「自動調整」で縮んだ文字は検査で FAIL になる）。
  *Never shrink to fit; cut words or split the slide.*
- 題名は 1 行。32pt で 1 行に入るのは全角 27 字（半角は 0.55 字に数える）まで。
  *Titles fit on one line: 27 full-width characters at 32pt.*
- 本文は左寄せ。中央寄せは使わない（題名も左寄せ）。
  *Left-aligned text, titles included.*
- **英語の併記は話すスライドに載せない:** 映しながら話すスライドでは、英語はノートに書く。日本語の下に英語の行を重ねると読む量が倍になり、目が行き来するため。英語を併記するのは、配って読んでもらう資料（PDF にして配るもの）だけ。詳しいことはノートに書き、あとで資料と一緒に共有するという考え方（ウェールズ政府の指針など）と同じ。
  *Spoken slides put English in the notes; only handout decks carry English under the Japanese.*
- 20pt は図の説明・表・グラフ・補足・英語の併記だけに使う。カードの中の文字は本文と同じ 24pt（大きなカードに 20pt の文字を置くと中身が貧弱に見える）。
  *20pt only for captions, tables, charts, notes and English; card text is 24pt like the body.*
- **数字のあとの空白（スライドの文字）:** 数値と単位の間は半角の空白をあける（SI の書き方。理系の標準）。単位には `pt`・`px`・`%` も含める。例: 「水深 4 m」「25 °C」「24 pt」「25 %」。助数詞（年・月・日・回・本・個・枚・か所・件・人・時間・列・行・字・項目・つ など）の前には空白を入れず、和文と数字の間にも入れない。例: 「4回」「12月」「1枚に1つ」。日本語の中に空白が多いと間延びして読みにくくなるため。単位の前の空白がない・助数詞の前に空白がある、はどちらも検査で注意。
  *A space between a number and its unit, pt, px and % included ("4 m", "24 pt", "25 %"); no space before Japanese counters or between Japanese and numbers ("4回", "12月").*
  - 注意: LibreOffice とそれを使うプレビューは、和文と英数字の間に自動で少し間をあける表示をするので、空白を入れていなくても間があいて見えることがある。ファイルの文字そのもので確かめる（`officecheck.py` が空白を調べる）。

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
| 7 ＋ 5 | 494 ＋ 346 | 図と説明（図が左）。説明の列は 24 pt で 1 行 13 字ほど |
| 4 ＋ 4 ＋ 4 | 272 × 3 | カード 3 枚 |
| 3 × 4 | 198 × 4 | カード 4 枚・手順 |

**縦の分け方 / Vertical:** 本文の領域は 1 段（368）か、上下 2 段（172 ＋ 間 24 ＋ 172）。横長の図（時系列など）にだけ、もう 1 つの分け方を認める: 上から「図の高さ ＋ 図の説明 1 行（28）＋ 間 24 ＋ 残り」。図は 12 列の全幅に置き、図の高さは図の縦横の比で決め、残りに説明か箇条書きを置く。
*Body area: one row of 368 or two rows of 172. Wide figures only may use figure height + one caption line (28) + 24 gap + the rest, at full width.*
*The body area is one row of 368 or two rows of 172 with a 24 gap.*

### 4.3 空間の使い方 / Using the space

- **はみ出さない:** 本文の領域の外（題名の行・柱の行・余白）に図や文字を置かない。柱に重なるものは検査で FAIL。
  *Nothing outside the body area; overlapping the footer is a FAIL.*
- **図とグラフは領域に合わせる:** グラフと図は列の幅（12・8・6 列）と段の高さ（368 か 172）いっぱいに置く。表は行の高さを 368 ÷ 8 ＝ 46 か 40 にして上から詰める。図やグラフの下に本文の領域の半分以上の空きがあれば、大きさか分け方を見直す（検査で注意）。
  *Charts and figures fill their columns and row; tables use 46 or 40 rows from the top.*
- **カードは中身に合わせる:** 文字のカードの高さは「上の余白 24 ＋ 中身 ＋ 下の余白 24」（`container-card-padding-spacious`）。説明は見出しのすぐ下に間 12（`space-md`）で置き、見出しと説明を上下に離さない。横に並べたカードは一番高いものに高さをそろえ、余った高さは本文の領域の下に残す。大きな数字（68pt）のカードも同じで、数字のすぐ下（間 12）に見出しと説明を置く（数字を上・説明を下に離して、間に空白を作らない）。段の高さ（368 か 172）いっぱいにするのは、図やグラフが入るカードだけ。文字のカードで文字が高さの半分に届かなければ検査で注意。
  *Text cards are content height plus 24 padding top and bottom, with the description 12 below the heading; side-by-side cards share the tallest height and leftover space stays below. Hero-number cards too; only figure cards fill the row.*
  - カードは区切りのために使わない。区切りは見出しと間隔で示す（「画面の組み立て」の「グループごとにカードや枠で囲まない」と同じ）。カードは並べて比べる単位にだけ使う。
    *Cards are units to compare, not separators.*
- **文字だけのスライドは上から詰める:** 本文は本文の領域の上にそろえる（縦の中央にしない）。下の空きは読みやすさのための余白としてそのまま残し、文字を大きくしたり間を広げたりして埋めない。
  *Text slides start at the top of the body area; leftover space stays empty.*
- **量の上限:**
  - 1 枚の文字は全角 100 字程度まで（半角は 0.5 字）。数えないもの: 題名・図の説明（名前が `caption`）・英語の併記・書誌（表紙と区切り、題名が「参考文献」「文献」「出典」「References」のスライド、名前が `ref` で始まる枠）。書誌は削れないので量の上限から外す。
  - 説明のまとまり（見出しと文の組、カード、段落）は 3 つまで、1 つは 2 行まで。箇条書きは 6 項目まで、1 項目は 2 行まで。
  - 超えたら 2 枚に分け、題名に「（2/2）」を付ける。上限は箇条書きだけでなく、見出しと文の組を並べたスライドにも効く。
  - 枚数の目安は 1 枚 45〜60 秒（10 分の発表なら 10〜12 枚）。
  *About 100 full-width characters per slide (titles, captions and English excluded); at most three text groups of two lines; six bullets of two lines; 45–60 seconds per slide.*
- **1 行の長さと改行の位置:** 24 pt の文が折り返す列は、1 行に全角 12 字以上入る幅にする（5 列以上。4 列〔272〕は 24 pt で 11 字しか入らない）。1 行のラベルや見出しだけなら細い列でもよい。行末に 1〜2 字だけ次の行に落ちる文は、言葉を削るか言い換える（PowerPoint は日本語を文字の単位で折り返すため）。どちらも検査で注意（目安の計算で、実際の折り返しは人が見る）。
  *Wrapping 24 pt text needs columns of 12+ full-width characters; reword lines that leave one or two characters on the last line.*
- **中身が少なすぎるスライドは作らない:** 中身（文字・図・カード）が本文の領域の 4 割に届かないスライドは、前後のスライドとまとめるか、根拠の図を足す。下の空きを文字の拡大や間の広げで埋めない（それは前の決まりのまま）。大きな数字のスライド、表紙・区切りは除く。検査で注意。空白が多すぎるスライドがないかは、大学の発表資料のチェックリストにもある確認。
  *Slides whose content fills under 40% of the body area are merged or given evidence; never padded. Hero-number, cover and section slides are exempt.*
- **余白の役割を混ぜない:** 項目の間 12〜16（`space-md`〜`space-lg`）＜ まとまりの間 24（`space-xxl`）＜ 領域の間 32 以上。近いものほど間を狭くする。空の段落や空白の文字で間をあけない。
  *Item gaps < group gaps < region gaps; never space with empty paragraphs.*

### 4.4 レイアウト / Layouts

ひな形に 6 つある。スライドは必ずこのどれかから作る。
*Six layouts in the template; every slide uses one.*

| レイアウト / Layout | 使う場面 |
|---|---|
| KM1 表紙 / Title | 1 枚目。題名・副題と、下の欄（12 列・20 pt・3 行まで）。下の欄には発表者と日付、文献紹介では紹介する論文の著者・題名・誌名・年を書く。左上に表紙のしるし（PDF と同じ大きさ）|
| KM1 区切り / Section | 章の始め。背景 #F5F5F5、章の番号と題名 |
| KM1 題名と本文 / Title and content | 箇条書き・説明（12 列） |
| KM1 2 段 / Two columns | 比べる・並べる（6 ＋ 6 列） |
| KM1 図と説明 / Figure and text | 左 7 列に図・グラフ、右 5 列に説明 |
| KM1 題名だけ / Title only | グラフ・表・図・数字のカード |

**中身の型 / Content types:** 本文は「題名で主張し、本文で根拠を見せる」形を基本にする（assertion–evidence。Penn State の Alley らの研究で、題名を主張の文にして図で支えるスライドの方が、話題名と箇条書きのスライドより理解が深まると報告されている）。そのため型は上から優先し、「文」は図にできないときの最後の手段にする。レイアウトの中に置く中身は次の 5 つの型にする。同じ役割のスライドは同じ型にそろえる（例: 結果のスライドは全部「図と説明」）。1 つの資料の中で組み方を増やさない。
*Five content types; slides with the same role use the same type.*

| 型 / Type | 中身 | レイアウト |
|---|---|---|
| 図と説明 | 図・グラフ（7 列）と説明（5 列）、または横長の図と下の説明（§4.2） | 図と説明・題名だけ |
| グラフ | PowerPoint のグラフ 1 つを全幅 | 題名だけ |
| カード | 比べる単位を 2〜4 枚（§4.3） | 題名だけ |
| 文 | 箇条書きか短い段落（§4.3 の量の上限） | 題名と本文・2 段 |
| 大きな数字 | 68pt の数字 1 つと説明 | 題名だけ |

### 4.5 そのほか / Other rules

- 題名は全部のスライドに付け、題名のプレースホルダーに入れる。同じ題名を 2 枚に使わない（続きは「（2/2）」を付ける）。題名だけを読んで話の筋がわかるようにする。
  *Every slide has a unique title in the title placeholder.*
- 1 枚に伝えることは 1 つ。
- **強調の色:** ブランドの紺（#10218B）で強調するのは 1 枚に 1 か所（主張・結論・大きな数字）だけ。見出しやラベル（「使う」「使わない」など）は黒（`ink` #242424）の太字にする。全部の見出しが紺だと、どこが大事か分からなくなるため。表紙の題名・章の番号は 1 か所として数える。
  *Brand navy marks one thing per slide (claim, conclusion or hero number); headings and labels are bold ink.*
- 文字はプレースホルダーに入れる。自分で置いたテキスト ボックスは読み上げの順が崩れやすいので、使ったら「校閲 › アクセシビリティ チェック」から開く［閲覧順序］ウィンドウで、見た目の順に直す。
  *Prefer placeholders; fix reading order when adding text boxes.*
- グラフは PowerPoint のグラフで作り（画像にしない）、色はテーマのアクセントの順、値を書き込む。軸と値の文字は 20pt・#424242、目盛りの線は #E0E0E0。
  *Native charts with theme accents and data labels.*
- グラフの系列が 2 つ以上あるときは、色に加えて模様で分ける（KM1-COL-001）。順は 1 塗り・2 横線・3 縦線・4 斜線（右下がり）・5 格子・6 斜め格子・7 点・8 市松（Web の `.f2-pat` と同じ形）。
  *With two or more series, add patterns (KM1-COL-001) in this order, same shapes as the web.*
  - **Office の既定の模様（「塗りつぶし › パターン」の `dkHorz` など）は使わない。** 8 × 8 画素の決まった細かい柄で、映すと色がにごって見えるだけになり、大きさも変えられないため（2026-11-19 にやめた）。
    *Do not use Office's preset patterns: fixed 8 × 8-pixel tiles that read as a muddy tint when projected.*
  - 代わりに KM1 の模様の画像（`KM1_グラフの模様.zip`、`office/km1_patterns.py` で作る）を、系列の「塗りつぶし › 塗りつぶし（図またはテクスチャ）› 挿入する › ファイルから」で選ぶ。グラフの棒では画像の並べ方を「積み重ね」にする（「引き伸ばし」にしない。「画像をテクスチャとして並べる」だけだと、グラフの中では画像を引き伸ばして表示するアプリがある）。グラフ以外の図形では「画像をテクスチャとして並べる」をオンにし、拡大縮小は 100%、配置は左上にする。ファイル名は `km1-pattern-<番号>-<模様>-<色>.png`。
    *Use the KM1 pattern images as a tiled picture fill at 100% scale.*
  - 寸法は 1pt ＝ 1px で、繰り返し 12pt（`space-md`）、横線・縦線・斜線の太さ 4pt（`space-xs`）、格子・斜め格子の線 2pt、点の直径 6pt、市松の 1 マス 12pt。前景は系列の色、背景は白、枠線は #616161 の 0.75pt。画面の模様（間隔 8px）より大きいのは、スライドを離れて見るため。
    *Repeat 12pt, stripes 4pt, grid lines 2pt, dots 6pt, checker squares 12pt; foreground = series color, background white, outline #616161 0.75pt.*
  - 画像はテーマのアクセント 6 色 × 8 模様の 48 枚。見本の `km1_pptx.js` はこの画像を書き込み、見本の 9 枚目に一覧がある。
- 表は「タイトル行」をオンにし、見出しの行は #F0F0F0 と太字、罫線は #D1D1D1。セルを結合しない。
- カードの角丸は 8pt（`radius-xl`）、塗りは #F5F5F5 か #ECEFFC。影や帯・縁の色の線は付けない（KM1 は大きな面の塗りを避ける）。
  *Cards use 8pt corners and flat tints; no shadows, stripes or edge bars.*
- アニメーションと画面切り替えの効果は使わない（KM1 の動きの決まり: 動かしてよいのは色・不透明度・8px までの移動だけ。スライドでは使う理由がない）。
  *No animations or transitions.*
- 話す内容はノートに書く。スライドに長い文を載せない。
- **表示バッジ:** KM1 で作ったスライドには、最後のスライドの本文の領域の右下（右の余白 48pt、柱の行の上 24pt）に表示バッジ「Designed with KM1」（日本語のスライドは「KM1 で設計」）を置いてよい。GitHub の KM1 へのリンクと代替テキストが付いた画像を `KM1_表示バッジ.pptx` に用意してあるので、コピーして貼る（リンクも一緒に移る）。大きさは変えない（バッジは高さ 24pt、しるしだけのボタンは 32pt）。決まった大きさなので 12 列のグリッドにそろえなくてよい（`officecheck.py` は名前が `km1-badge` で始まるものを除く）。形と文言の決まりは「アイコン」§10。
  *Slides may carry the "Designed with KM1" badge bottom-right of the body area on the last slide. Copy it from `KM1_表示バッジ.pptx` — the GitHub link and alt text come with it. Do not resize (badge 24pt tall, mark button 32pt); fixed sizes are exempt from the grid.*

### 4.6 図の転載と図の説明 / Reproduced figures and captions

- **描き直すのが基本:** 数値が分かる図（棒・線・散布図など）は、PowerPoint のグラフで描き直す。論文の図をそのまま縮めると、検査は通っても肝心の中身が見えない。
  *Redraw figures whose values are known as native charts.*
- **転載する大きさ:** 論文の図の文字は印刷で 6〜7 pt なので、映して読める大きさ（14 pt 前後）にするには **印刷の大きさの 2 倍以上** で載せる。全体を 2 倍にできないときは、必要な部分だけを切り出す。それでも届かない文字（目盛りの数字・日付など）は、日本語のラベルを重ねて補う。1 枚に載せるパネルは 2 つまでを目安にする。
  *Paper figures print at 6–7 pt, so place them at 2× print size or more; crop if needed, and cover text that still falls short with Japanese labels. About two panels per slide.*
  - **切り出した画像には元の解像度（dpi）を入れる。** PDF から 600 dpi で切り出したなら、画像にも 600 dpi と書き込む（`pdftoppm -r 600` はそのまま入る。スクリーンショットは入らないので、書き出すときに指定する）。dpi が分かれば画像の画素数から印刷の大きさが決まり、検査で 2 倍に届いているかが分かる。
    *Embed the extraction dpi in cropped images so the print size, and the 2× rule, can be checked.*
  - 転載した図の画像の名前は `fig` で始める（例 `fig-2a`）。検査はこの名前の画像だけを調べ、dpi が無い・2 倍未満なら注意を出す。写真や自作の図は対象外。
    *Name reproduced-figure images `fig…`; the checker warns when dpi is missing or the scale is under 2×.*
- **図を 2 枚並べる:** 図の説明を 1 行（28）と間 8 を下に置くと、図の高さは 368 − 28 − 8 ＝ **332** まで。列の幅と合わせると、上下を切らずに入る図の縦横の比（幅 ÷ 高さ）は次のとおり。満たさない図は、別の分け方にするか 1 枚ずつのスライドにする。図の上下を切るのは最後の手段で、切った情報は日本語のラベルで補う。
  *With a one-line caption, figures can be 332 high; the minimum width/height ratio per split is below.*

| 分け方 / Split | 図の幅 | 縦横の比（幅 ÷ 高さ）が次以上なら切らずに入る |
|---|---|---|
| 12 列（1 枚） | 864 | 2.60（それより縦長なら「図と説明」の 7 列か、高さ 332 で幅を縮める） |
| 6 ＋ 6 | 420 ＋ 420 | 両方 1.27 |
| 5 ＋ 7 | 346 ＋ 494 | 5 列の図は 1.04（ほぼ正方形まで）、7 列の図は 1.49。縦長の図と横長の図を並べるとき |
| 7（図）＋ 5（説明） | 494 | 1.49 |

  説明が 2 行のときは図の高さが 304 になり、比は 6 ＋ 6 で 1.38、5 列で 1.14、7 列で 1.63 になる。
  *With a two-line caption the height drops to 304: 1.38 for 6+6, 1.14 for 5 columns, 1.63 for 7.*
- **日本語の発表:** 英語の図には、要になるラベルだけでも日本語を重ねる（20pt、図の上の白い面に黒い文字）。
  *In Japanese talks, overlay Japanese on at least the key labels.*
- **図の説明:** 図の下に 20 pt で「図番号　内容。[n] Fig. ○ を転載」と書く（例「図2　湖の水深の変化（1975〜2020 年、m）。[3] Fig. 4 を転載」）。図番号と内容の間は全角の空白。テキスト ボックスの名前を `caption` で始めると、検査の文字数から外れる。
  - **1 行が基本、2 行まで。** 「何・どこ・いつ・単位」が 1 行に入らないときだけ 2 行にする（図の高さはその分 28 減る）。2 行にも入らない分（方法の細かい条件など）はノートに書いて口で話す。単位は軸の目盛りか説明のどちらかに必ず見える形で残し、ノートだけに回さない（聞き手はノートを読めないため）。3 行以上は検査で注意。
  *Captions: one line, two at most when what/where/when/unit need it; the rest goes in the notes and is spoken. Units must stay visible on the slide.*
- ライセンスと「一部を切り出した」などの断り書きは、最後の参考文献のスライドにまとめてよい。
  *Licence and cropping notes may be gathered on the references slide.*

### 4.7 研究発表の中身の順番 / Research talks

ゼミ・中間発表・文献紹介のスライドは、次の順番で組む。枚数の目安は発表時間 1 分に 1 枚（1 枚 45〜60 秒、§4.3）。配る資料（レジュメ）の書き方は KM1 の対象外。
*Seminar, progress and paper-review talks use the orders below; about one slide per minute. Handouts are out of scope.*

**文献の紹介 / Paper review**

| スライド | 中身 |
|---|---|
| 1 枚目（表紙）| 文献の書誌情報（著者・年・題名・誌名・巻（号）・頁または論文番号・DOI）、ゼミ名・発表日・発表者 |
| 2 枚目 | 文献の問いと結論。2〜3 行ずつ |
| 3 枚目〜 | 要約。1 枚に図 1 つと要点 1〜3 行。図には元の図番号・出典・ライセンスを付ける（§4.6）|
| 任意 | 発表者のコメント。要約のスライドに混ぜず、別のスライドにする |
| 最後 | 議論したいこと 1〜3 個 |
| 予備 | 参考文献（要約で引いた別の文献があるとき）|

*Cover with full citation; question and conclusion; one figure per summary slide; own comments on separate slides; 1–3 discussion points; references as a backup slide.*

**研究の進捗 / Progress report**

| スライド | 中身 |
|---|---|
| 1 枚目（表紙）| 表題、ゼミ名・発表日・発表者 |
| 2 枚目 | 要約 3 行（目的・いま分かったこと・次にすること）|
| 3 枚目 | 前回からの進み |
| 4 枚目〜 | 途中結果。1 枚に図 1 つ。暫定の値は「暫定」と書く |
| 次 | 分かったこと・言えないこと |
| 次 | 相談したいこと 1〜3 個 |
| 最後 | 今後の予定（表。状態は「未着手・進行中・完了」の言葉で）|

*Cover; three-line summary; progress since last time; one result figure per slide (mark provisional values); findings and limits; 1–3 questions; schedule table with status in words.*

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
| PowerPoint | 16:9、全部のスライドに題名、題名の重複、図・グラフの代替テキスト、表のタイトル行（注意）とセルの結合、文字の大きさが §4.1 の値、14pt が柱の行の外にない、文字と図形の色が KM1 の色、言語の指定（注意）、アニメーション・画面切り替え（注意）。§4.2〜4.3 の割り付け: 本文の領域の下へのはみ出し（FAIL）、題名の行への食い込み・12 列のグリッドからのずれ・題名が 1 行に入らない・箇条書きが 7 項目以上・図・グラフの下の大きな空き・細い列で折り返す文・行末に 1〜2 字だけ落ちる文・中身が本文の領域の 4 割未満・図の説明が 3 行以上・転載した図（名前が `fig`）の dpi が無い・印刷の大きさの 2 倍未満（どれも注意）。§4.1・4.3・4.5・4.6 の中身: 1 枚の文字数が全角 100 字を超える・文字のカードで文字が高さの半分未満・紺の文字が 1 枚に 2 か所以上・助数詞の前の空白・単位の前の空白がない（どれも注意。書誌は文字数に数えない） |

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
- [ ] スライド一覧を 25% で表示しても、題名と一番大事なものが読める / titles and the key element read at 25% zoom
- [ ] 1 枚を 5 秒見て、言いたいことが分かる / the point is clear in five seconds
- [ ] 図の中の文字が、映したときに読める大きさになっている / text inside figures is readable when projected
- [ ] 同じ組み方が続きすぎず、形がばらばらでもない / layouts neither repeat too long nor scatter

- [ ] 説明の文の改行の位置が自然で、行末に 1〜2 字だけ落ちていない / natural line breaks, no stranded characters
- [ ] 中身が少なく下が大きく空いたスライドがない / no near-empty slides

検査に通ることと見やすいことは別。`officecheck.py` が FAIL 0・注意 0 でも、上の人の確認を省かない。
*Passing the checker is not the same as being readable; never skip the human checks.*

**確かめたこと / Verified (2026-11-19)** — 文字の大きさと割り付けを改めた版のひな形と見本が `officecheck.py` で FAIL 0・注意 0、LibreOffice で PDF にして全ページを目で見た。以前（2026-11-13） — ひな形 2 つと見本 2 つが `officecheck.py` で FAIL 0、Office Open XML の形式の検査（XSD・関係・中身の種類）に合格。LibreOffice で PDF にして全ページを目で見た（游ゴシックがないので Noto Sans CJK JP で表示。文字の幅は Office と少し違う）。**まだ確かめていないこと:** Microsoft Word・PowerPoint で開くこと、Office のアクセシビリティ チェック、PowerPoint で書き出した PDF のタグ。
*Templates and samples pass `officecheck.py` and OOXML validation, and were rendered with LibreOffice (Noto Sans CJK JP substituted for Yu Gothic). Not yet checked in Microsoft Office itself.*

出典 / Sources: [Penn State: Assertion–Evidence の研究](https://writing.engr.psu.edu/research.html)・[Alley ほか: Assertion–Evidence Slides Instruction Set](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/7/13153/files/2008/10/Assertion-Evidence-Slides-Instruction_Set.pdf)・[東北大学: 発表資料チェックリスト](https://web.tohoku.ac.jp/yusa/wp-content/uploads/2026/03/checklist_presen_0204.docx)・[ウェールズ政府: アクセシブルな PowerPoint の作り方](https://www.gov.wales/node/30039)・[Microsoft: PowerPoint のプレゼンテーションをアクセシビリティ対応にする（18pt 以上）](https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25)・[NYC MOPD: Accessible Slidedecks Guide（24pt 以上）](https://www.nyc.gov/site/mopd/publications/guides/accessible-slidedecks-guide.page)・[Indiana University: PowerPoint（24pt 以上）](https://accessibility.iu.edu/creating-content/documents/powerpoint/index.html)・[Microsoft: アクセシビリティ チェックのルール](https://support.microsoft.com/ja-jp/Accessibility/office-accessibility/rules-for-the-accessibility-checker)・[Microsoft: PowerPoint のプレゼンテーションをアクセシビリティ対応にする](https://support.microsoft.com/ja-jp/Accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities)・[Microsoft: 閲覧順序ウィンドウ](https://support.microsoft.com/ja-jp/powerpoint/make-slides-easier-to-read-by-using-the-reading-order-pane)・[W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
