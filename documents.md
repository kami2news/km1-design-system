# PDF の規定 / PDF documents

KM1-DOC-001。KM1 で作る PDF（報告書・資料・手順書・この標準そのもの）の決まり。画面の部品と同じトークンと考え方を、紙の大きさの文書に当てはめる。
*KM1-DOC-001. Rules for PDFs made with KM1 (reports, handouts, manuals, this standard itself). It applies the same tokens and thinking as the UI to page-sized documents.*

道具は `pdf/` にある: 見た目のひな形 `km1-print.css`、見本 `template.html`、仕上げ `km1_finish.py`、検査 `pdfcheck.py`。
*Tools live in `pdf/`: the `km1-print.css` template, a `template.html` sample, `km1_finish.py` for finishing and `pdfcheck.py` for checking.*

Word と PowerPoint のファイルそのものの決まりは「Word と PowerPoint の規定」（`office.md`）。
*Rules for Word and PowerPoint files are in `office.md`.*

**対象外 / Out of scope:** 大学の授業・ゼミ・卒業研究で提出・配布するレポート・レジュメ・論文は KM1 の対象外（別の標準 RS1 で扱う）。KM1 は RS1 の値や部品に頼らず、RS1 も KM1 に頼らない。研究発表のスライドは KM1-DOC-003 で扱う。
*Coursework reports, seminar handouts and theses are out of scope (handled by the separate RS1 standard); neither depends on the other. Research presentation slides are covered by KM1-DOC-003.*

## 1. PDF にするか / Should it be a PDF?

- PDF は「配る・残す・印刷する」ための形。画面で読むだけ、あとで直す、スマホで読むことが多いなら、Web ページか共有ドキュメントを先に考える。PDF は画面幅に合わせて折り返せないため。
  *PDF is for handing out, archiving and printing. If people mostly read on screen, edit later or read on phones, prefer a web page or a shared doc; PDF doesn't reflow to the screen.*
- 入力してもらう用紙を PDF のフォームにしない。KM1 のフォーム（「画面の組み立て › フォーム」）で Web にする。
  *Don't make fillable PDF forms; build a web form with KM1 Forms instead.*

## 2. 判型と余白 / Page size and margins

| 項目 / Item | 決まり / Rule |
|---|---|
| 大きさ / Size | A4 縦が基本。横長の図や表が中心なら A4 横。1 冊の中で、章ごとに向きを変えてよい。向きの違う部分が大きいときは別冊に分ける（§5「分冊」）。KM1 自身は本編（縦）と部品カタログ（横）の 2 冊。CSS の名前つきページ（`@page wide{size:A4 landscape}` と `page: wide`）で作る。スライドを PDF にするときはスライドの比率のまま（検査では注意として出る）/ A4 portrait by default; landscape for wide figures; orientation may change per chapter via CSS named pages; slides keep their own ratio |
| 余白 / Margins | 上下 20mm・左右 17mm。両面印刷して綴じるときは内側（綴じる側）を 25mm / 20mm top and bottom, 17mm sides; 25mm on the binding side when bound |
| 段組み / Columns | 1 段。2 段組みは読み上げの順が崩れやすいので使わない / Single column; two columns break reading order too easily |
| 1 行の長さ / Line length | 本文 10pt で約 50 字（A4・左右 17mm のとき）/ about 50 characters at 10pt |

## 3. 文字 / Type

| 役割 / Role | 大きさ・太さ / Size, weight | 行送り / Leading | 色（トークン）/ Color (token) |
|---|---|---|---|
| 本文 / Body | 10pt・標準 | 1.7 | `ink` #242424（15.5:1） |
| 英語の併記 / English line | 9pt・標準 | 1.55 | `ink-secondary` #616161（6.2:1） |
| 大見出し H1（章）/ Chapter | 20pt・太字、下に 2pt の線 | 1.3 | `brand-ink` #10218B（13.0:1） |
| 中見出し H2 / Section | 13pt・太字 | 1.4 | `ink` |
| 小見出し H3・H4 | 11pt・10pt・太字 | 1.7 | `ink` |
| 表 / Tables | 9pt | 1.55 | `ink`、見出しセルの背景 #f0f0f0（13.6:1） |
| 柱・ページ番号・図の説明 / Running heads, page numbers, captions | 8〜8.5pt | — | `ink-secondary` |

- 書体は KM1 の `Noto Sans JP`（なければ Noto Sans CJK JP）。英数字も同じ書体で揃え、等幅は `code` だけ。フォントは必ず埋め込む（PDF/UA-1、Matterhorn 31-009）。
  *Use KM1's `Noto Sans JP` (or Noto Sans CJK JP) for both scripts; monospace only for code. Always embed fonts (PDF/UA-1, Matterhorn 31-009).*
- 8pt より小さい文字を使わない。8pt を使うのは柱・ページ番号・注記だけ。
  *Nothing below 8pt; 8pt only for running heads, page numbers and notes.*
- 文字の色はすべて白地で 4.5:1 以上（上の表の比はすべて計算済み）。斜体は日本語に使わない。
  *All text is at least 4.5:1 on white (ratios above are computed). No italics for Japanese.*

## 4. 色と印刷 / Color and printing

- KM1 のライトテーマのトークンだけを使う。PDF にダークテーマは使わない（印刷するとインクが多く、紙では読みにくい）。
  *Light-theme tokens only; no dark theme in PDFs (heavy ink, hard to read on paper).*
- 色だけで意味を伝えない。白黒で印刷しても、文字・記号・模様で区別できるようにする（WCAG 1.4.1）。状態の色を使うときは「意味の色の使い分け」と同じく、アイコンか言葉を添える。
  *Never rely on color alone; a grayscale print must still distinguish everything (WCAG 1.4.1). Status colors come with an icon or a word, as in "Status colors in practice".*
- 背景色を印刷させる指定（`print-color-adjust: exact`）を入れる。ただし広い面の塗りは表紙のしるしと見出しセルだけにする。
  *Force background printing (`print-color-adjust: exact`), but keep large fills to the cover mark and table header cells.*
- 印刷会社に入稿する PDF（CMYK・トンボ・PDF/X）はこの規定の範囲外。必要になったら印刷会社の指定に従う。
  *Press-ready PDFs (CMYK, crop marks, PDF/X) are out of scope; follow the printer's spec when needed.*

## 5. 文書の組み立て / Document structure

1. **表紙 / Cover:** 題名、副題、版（日付 `YYYY-MM-DD`）、作成者または組織。表紙には柱とページ番号を出さない。
   *Title, subtitle, edition date, author or organization; no running heads or page number.*
2. **目次 / Contents:** 9 ページ以上の文書に付ける。章と節、ページ番号付き。PDF の「しおり」も同じ構成で付ける。
   *Required at 9+ pages: chapters and sections with page numbers, mirrored as PDF bookmarks.*
3. **本文 / Body:** 章は新しいページから始める。見出しの段は飛ばさない（H1 の次は H2）。
   *Chapters start on a new page; heading levels never skip.*
4. **柱とページ番号 / Running heads:** 上に文書名（左）と版の日付（右）、下中央にページ番号。
   *Document name top-left, edition date top-right, page number bottom center.*
5. **変更履歴 / Changelog:** 改訂する文書は最後に変更履歴を付ける。
   *Documents that get revised end with a changelog.*
6. **分冊 / Volumes:** 1 冊が 150 ページを超えるとき、または性質の違う部分（読む決まりと、見て比べる見本など）が大きいときは分ける。分けた冊はどれも表紙に「全 N 冊・本編／別冊」と組のファイル名を書き、同じ版の日付にして、いつも一緒に作って一緒に配る。章の番号は冊をまたいで通し、本編には別冊に移した章の場所を残して中身の案内を書く。
   *Split when a volume exceeds 150 pages or a large part differs in nature (rules to read vs. previews to compare). Every volume states "Volume N of M" and the set's file names on its cover, shares the edition date, and is built and shared together. Chapter numbers run across volumes; the main volume keeps a pointer chapter.*
7. **奥付 / Colophon:** 外部に共有する文書の最後に、`notices.md` §2 の文言（無関係の旨・デジタル庁の帰属と改変の断り・アイコンと書体のライセンス）を入れる。作成者の行は実名を入れず、既定の「KM1 作成者」を使う（§7 との調整は持ち主の判断）。ひな形には奥付の領域がある。
   *Shared documents end with the `notices.md` §2 wording (non-affiliation, Digital Agency credit and adaptation note, icon and font licenses). The author line defaults to "KM1 作成者", no real name; reconciling with §7 is the owner's call. The template has a colophon section.*

- 表は見出し行を付け、ページをまたぐときは見出し行を繰り返す。表の中で行や列を結合しない（読み上げで対応が崩れる）。
  *Tables have a header row that repeats across pages; don't merge cells (it breaks header association when read aloud).*
- 図には代替テキストを付ける。飾りだけの画像は代替テキストを空にし、読み上げの対象から外す。文字を画像にしない。スキャンしただけのページを入れない（やむをえないときは OCR で文字を入れる）。
  *Figures get alt text; decorative images get none and are excluded. Never set text as an image; no scan-only pages (OCR if unavoidable).*
- リンクの文字は行き先がわかる言葉にする（「こちら」にしない）。印刷して使う文書では URL も見える形で書く。
  *Link text names the destination (never "click here"); in documents meant for print, show the URL too.*

## 6. 文書情報 / Document properties

| 項目 / Item | 決まり / Rule | 検査番号 / Check |
|---|---|---|
| 題名 / Title | 中身がわかる題名。ファイル名や「無題」にしない。開いたときにウィンドウに題名を出す（DisplayDocTitle） | KM-TITLE・07-001 |
| 言語 / Language | 文書の言語を `ja` にする。英語の段落は可能なら `en` を付ける | 11-001 |
| XMP | `dc:title`・`dc:language` を入れる（`km1_finish.py` が入れる） | 06-001・06-003 |
| タグ / Tags | タグ付き PDF にする（見出し・段落・リスト・表・図・リンクの構造） | 01-005・KM-TREE |
| 暗号化 / Encryption | パスワードや「コピー禁止」をかけない。読み上げソフトが中身を読めなくなるため | KM-SEC |
| ファイル名 / File name | `<文書名>_<YYYY-MM-DD>.pdf`。空白を入れない / no spaces | — |
| 大きさ / File size | 10MB 以下、または 1 ページ 300KB 以下（目安） | KM-SIZEMB |

## 7. 個人情報 / Personal information

- 外に配る PDF では、作成者欄・見本の名前・画面の写しに、実在の個人名・勤務先・連絡先を残さない。見本は架空の名前（例: 山田 花子）にする。
  *In PDFs shared outside, don't leave real names, workplaces or contacts in properties, samples or screenshots; use fictional names.*
- 書き出したあと、PDF の文書のプロパティ（作成者・題名・キーワード）を開いて確かめる。
  *After exporting, open the document properties and check author, title and keywords.*

## 8. 作り方 / How to make one

**HTML から（KM1 の標準の作り方）/ From HTML (KM1's default)**

1. `pdf/template.html` をもとに書き、`km1-print.css` を読み込む。`<html lang="ja">` と `<title>` を必ず入れる。
   *Start from `template.html` with `km1-print.css`; always set `<html lang="ja">` and `<title>`.*
2. 図は `<figure role="group">` の中に `<img alt="…">` と `<figcaption>` を置く。`role` を付けない `<figure>` は、Chrome が代替テキストのない図として書き出す（2026-11-13 に KM1 で確認）。
   *Put `<img alt>` and `<figcaption>` inside `<figure role="group">`. A plain `<figure>` is exported by Chrome as a figure without alt text (confirmed in KM1 on 2026-11-13).*
3. Chrome で書き出す: `google-chrome --headless=new --no-pdf-header-footer --generate-pdf-document-outline --print-to-pdf=out.pdf file.html`。タグ付き PDF になり、見出しからしおりができる。
   *Export with headless Chrome as above: the result is tagged and bookmarks come from headings.*
4. 仕上げ: `python3 km1_finish.py out.pdf final.pdf`（XMP、リンクの説明、しおりの重複の修正）。
   *Finish with `km1_finish.py` (XMP, link descriptions, fixes doubled bookmark titles).*
5. 検査: `python3 pdfcheck.py final.pdf`。FAIL が 0 になるまで直す。
   *Check with `pdfcheck.py` and fix until there are no FAILs.*

**Word から / From Word**
- 見出しスタイル（見出し 1・2…）と代替テキストを付けてから、「名前を付けて保存」で PDF を選び、「オプション」で文書のプロパティ、アクセシビリティ用の構造タグ、見出しからのしおり作成を有効にする。印刷ダイアログの「PDF として印刷」は使わない（構造が消える）。
  *Use heading styles and alt text, then Save As PDF with Options for document properties, structure tags for accessibility and bookmarks from headings. Don't "print to PDF" from the print dialog; it drops the structure.*

**Google ドキュメントから / From Google Docs**
- 「ファイル › ダウンロード › PDF」で書き出したあと、必ず `pdfcheck.py` にかける。タグが残るかどうかは資料によって説明が食い違うため、FAIL が出たら .docx で落として Word から書き出す。
  *Download as PDF, then always run `pdfcheck.py`. Sources disagree on whether tags survive, so if it fails, download .docx and export from Word.*

## 9. 検査 / Checking

**機械の検査 / Machine checks** — `pdfcheck.py` が次を調べる（番号は PDF/UA-1 の Matterhorn Protocol、KM- は KM1 独自）:
タグ・構造木、言語、題名と DisplayDocTitle、XMP と dc:title、9 ページ以上のしおり、A4、フォントの埋め込み、文字のないページ、図の代替テキスト、見出しの有無・最初が H1・段の飛び・H と Hn の混在、表の見出しセル、暗号化、ファイルの大きさ。FAIL があると終了コード 1 を返すので、書き出しの手順に組み込める。
*`pdfcheck.py` checks tags, language, title, XMP, bookmarks, A4, embedded fonts, text-less pages, figure alt text, heading order, table headers, encryption and size. It exits with 1 on any FAIL, so it can gate an export script.*

**Windows での追加の検査 / Extra check on Windows** — 無料の PDF Accessibility Checker（PAC）で PDF/UA の機械判定をほぼすべて確かめる。`pdfcheck.py` はその一部しか見ない。
*Run the free PDF Accessibility Checker (PAC) on Windows for nearly all PDF/UA machine checks; `pdfcheck.py` covers only part of them.*

**人の目の検査 / Human checks**（機械では判定できない）
- [ ] 読む順（タグの順）が見た目の順と同じ / tag order matches visual order
- [ ] 代替テキストが図の中身を伝えている / alt text conveys the figure
- [ ] 飾りの画像・柱・ページ番号が読み上げの対象から外れている / decorations and running heads are artifacts
- [ ] 白黒で印刷しても区別できる / distinguishable in grayscale
- [ ] 表の見出しセルと結合のない形になっている / table headers present, no merged cells
- [ ] 文書のプロパティに個人情報が残っていない / no personal data in properties
- [ ] リンクが正しい場所に飛ぶ / links go to the right place

**PDF/UA を名乗る条件 / Claiming PDF/UA** — PDF/UA（ISO 14289）に準拠すると書いてよいのは、PAC か veraPDF で合格し、人の目の検査も済ませたときだけ。それまでは PDF/UA の識別子を入れない。KM1 自身の PDF もまだ名乗っていない。
*Only say a PDF conforms to PDF/UA (ISO 14289) after it passes PAC or veraPDF and the human checks; until then, add no PDF/UA identifier. KM1's own PDF doesn't claim it yet.*

## 10. 長期保存 / Archiving

- 提出先が PDF/A を求めるときだけ PDF/A にする。KM1 の手順（Chrome）では PDF/A は作れないので、その場合は Word の「PDF/A 準拠」などを使い、提出先の検証に通す。
  *Use PDF/A only when a recipient requires it. KM1's Chrome route can't produce PDF/A; use Word's PDF/A option or similar and pass the recipient's validator.*

出典 / Sources: [PDF Association: ISO 14289-2（PDF/UA-2）](https://pdfa.org/iso-14289-2-pdf-ua-2-the-gold-standard-for-accessibility-in-pdf-2-0-has-arrived/)・[Matterhorn Protocol 1.02](https://pdfa.org/download-area/accessibility/MatterhornProtocol_1-02.pdf)・[axes4: Matterhorn Protocol と PAC](https://support.axes4.com/hc/en-us/articles/7371943734930)・[W3C WCAG 2.2 Techniques H71](https://www.w3.org/WAI/WCAG22/Techniques/html/H71)・[デジタル庁 ウェブアクセシビリティ導入ガイドブック](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook)
