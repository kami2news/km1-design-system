# 変更履歴 / Changelog

## 2026-11-26 — RS1 との関係 / Relation to RS1

- **役割分担を明記:** 授業・研究のレポートは RS1、それ以外の文書・スライド・画面は KM1、と `documents.md` 冒頭と `README.md` に書いた。順位は「授業・提出先の指定 ＞ RS1 ＞ KM1」。値は変えていない。
  *Stated the split: coursework reports follow RS1, everything else KM1; precedence is course instructions > RS1 > KM1. No values changed.*

## 2026-11-19 — 外部レビューへの対応 / Review follow-ups

- **Flutter の画像比較を本当の検査に:** CI が `flutter test --update-goldens` で毎回画像を作り直しており、違いを見逃していた。通常の CI は承認済みの画像と比べて違えば失敗にし、作り直しは手で動かす「goldens」ワークフローだけにした（成果物を目で確かめてから commit）。承認済みの画像を入れるまでは比較を飛ばして警告を出す。手順は `verification.md` 6 章。
  *Golden tests now compare against approved images; regeneration only via the manual "goldens" workflow.*
- **SortableList:** id を渡さずに 2 つ置くと説明の id（`sort-help`）が重なっていたのを、ほかの部品と同じく自動で振るようにした。Esc は「移動を終える」だけで動かした並びが残っていたのを、説明どおり持ち上げる前の並びに戻して読み上げるようにした。
  *SortableList: generated help id; Esc now restores the original order and announces it.*
- **再発防止のテスト:** 自分で id を作る 14 部品を全部 2 つずつ置き、id が重ならないこと・aria の参照先がすべてあることを確かめるテストと、SortableList の Esc のテストを足した。前の版の `bundle.js` では 3 つ不合格になる。
  *Every id-generating component placed twice, plus the Esc test; the previous bundle fails three of them.*
- **検証の記録を実際に合わせた:** Flutter の解析とテストは CI で済み（F1）、画像比較（F2）と実機（F3）は未実施、と分けた。`platforms.md` に段階（安定〔パイロット〕・パイロット・実験的）を付け、ビルドしたことのない WinUI・Compose・SwiftUI は「実験的」にした。
  *Verification log matches CI; platforms labelled stable-pilot, pilot or experimental.*
- **色の組み合わせの検査:** 意味づけの色の 36 組（ライト・ダークで 72）を WCAG の比で調べる `gen/contrast_check.py` を足し、`check_all.sh` に入れた。すべて合格。
  *New semantic-pair contrast check (72 pairs, all pass).*
- **DTCG 形式のトークン:** `tokens.json` から W3C Design Tokens 形式のファイルをライト・ダーク 1 つずつ作る `gen/tokens_dtcg.py` を足した（`dist/tokens/`、生成物で差分を検査）。正本は `tokens.json` のまま。
  *DTCG export generated from tokens.json.*
- **文献紹介で使ってわかったこと（§4.3・4.4・4.6）:** 転載した図の決まりを「映して 14 pt」から「印刷の大きさの 2 倍以上で載せ、届かない文字は日本語のラベルで補う」に言い換え、切り出した画像には元の dpi を入れる約束にした（前の検査は画像の dpi で判定が変わり、高い解像度で切り出すと文字が小さくても素通りしていた）。検査は名前が `fig` の画像だけを調べる。表紙の下の欄を 12 列・3 行にして、文献紹介の書誌が入るようにした。書誌（表紙・区切り・参考文献のスライド・名前が `ref` の枠）は文字数に数えない。図を 2 枚並べるときの高さ 332 と縦横の比の表（6＋6 は 1.27 以上、縦長の図は 5＋7）を足した。図の説明は 1 行が基本で、何・どこ・いつ・単位が入らないときだけ 2 行まで、残りはノートで話す。
  *Lessons from a paper-review deck: reproduced figures at 2× print size with dpi embedded, a 12-column 3-line cover field, bibliography excluded from the character count, a two-figure size table, and captions of up to two lines.*
- **画像比較の登録と拡張:** 承認済みの画像を登録した（アイコンの一覧 6 枚）。最初の候補では、テストで KM1Icons の書体が読み込まれず塗りのアイコンが □ になっていたのを直し、画像に画面の背景色を入れた。部品を並べたギャラリーの画像 4 枚（スマホ・PC × ライト・ダーク）も比べるようにした。
  *Goldens approved (6 icon sheets) after fixing font loading and adding the surface colour; 4 gallery goldens added.*
- **Flutter の版を固定:** 必須の検査と画像の作成は同じ版に固定し、最新の stable は必須でない参考のジョブで試す（stable の更新だけで必須の検査が落ちないように）。
  *Flutter pinned for required jobs; latest stable runs as an advisory job.*
- **公開の手順:** タグは付け直さない（同じ日の 2 回目は `.2`）、タグごとに GitHub の Release を作り `dist/` を添付する、と決め、`CONTRIBUTING.md` に手順を書いた。`CODEOWNERS` と Dependabot（npm・pip・Actions を週 1 回）を足した。
  *Immutable tags plus GitHub Releases; CONTRIBUTING, CODEOWNERS and Dependabot added.*

## 2026-11-19 — スライドの文字の大きさと割り付け / Slide type sizes and layout grid

- **文字を大きく（KM1-DOC-003 §4.1）:** 投影して読む前提にし、題名 28→32pt、本文 20→24pt、補足・英語・表・グラフ 16→20pt、柱 12→14pt にした。内容の文字は 20pt 以上、14pt は柱の行だけ。どれも KM1 の型の表の値（title-1・title-3・subtitle-1・body-1）で、行送りもトークンの値。題名は 1 行（全角 27 字まで）、縮めて入れない。
  *Slides now read at projection size: titles 32, body 24, secondary 20, footer 14pt; content never below 20pt; one-line titles; no shrink-to-fit.*
- **空間の定義（§4.2〜4.3）:** 余白（左右 48・上 40・題名と本文の間 24・柱 20・下 24）、本文の領域 864 × 368、12 列のグリッド（列 50・溝 24）と縦の 2 段（172 ＋ 172）を決め、図・表・カードを領域に合わせる・文字だけのスライドは上から詰める・箇条書きは 6 項目まで・余白の役割の順、を決まりにした。
  *Defined margins, an 864 × 368 body area, a 12-column grid and two-row split, plus fill, density and spacing-hierarchy rules.*
- **レイアウト:** 「KM1 図と説明」（8 ＋ 4 列）を足して 6 つにした。見本はグリッドの説明のスライドを足し、カード・グラフ・表を本文の領域いっぱいに置き直した。
  *Added the Figure-and-text layout; the sample deck now shows the grid and fills the body area.*
- **グラフの模様:** Office の既定の模様（`dkHorz` など、8 × 8 画素の固定の柄）をやめ、Web の模様と同じ形の画像（繰り返し 12pt・線 4pt）を並べて塗るようにした。画像は `office/km1_patterns.py` で作り（アクセント 6 色 × 8 模様）、`dist/KM1_グラフの模様.zip` で配る。見本に模様の一覧のスライドを足した。グラフの棒は画像を「積み重ね」（`c:pictureOptions`）で並べる。並べる指定だけでは、Claude のプレビューと LibreOffice がグラフの中の画像を引き伸ばし、横線 1 本が棒いっぱいに広がったため。
  *Replaced Office preset patterns with tiled KM1 pattern images (12pt repeat, 4pt stripes), shipped as `KM1_グラフの模様.zip`; added a pattern overview slide.*
- **見づらさを規定で防ぐ（§4.1〜4.6、別のチャットの修正案 A〜C）:** 文字のカードは中身＋上下 24 の高さにし、説明は見出しのすぐ下（段の高さいっぱいは図と大きな数字のカードだけ）。カードの文字は 24pt、20pt は図の説明・表・グラフ・補足だけ。1 枚の文字は全角 100 字程度・説明のまとまりは 3 つまで・1 枚 45〜60 秒。転載した図は中の文字が 14pt 以上になる大きさで、数値の図は描き直す。紺の強調は 1 枚に 1 か所で、見出しは黒の太字。助数詞の前と、和文と数字の間には空白を入れず（「4回」「12月」）、数値と単位の間は pt・px・% も含めて半角の空白をあける（「4 m」「24 pt」、理系の標準）。大きな数字のカードも中身の高さにした（数字と説明を離さない）。横長の図の縦の分け方、図の説明の書き方、中身の 5 つの型、人の確認 4 項目を足した。
  *Rules from the readability review: content-height cards, 24pt card text, ~100 characters per slide, reproduced-figure sizing, one navy emphasis per slide, no space before counters, wide-figure split, caption format, five content types, four more human checks.*
- **見やすさの見直し（世の中の指針を参考に）:** 「題名で主張し、本文で根拠を見せる」（Penn State の assertion–evidence）を中身の型の基本にし、「文」は最後の手段にした。図と説明の分け方を 8＋4 列から 7＋5 列にし、24 pt の文が折り返す列は全角 12 字以上・行末に 1〜2 字だけ落とさない決まりにした。中身が本文の領域の 4 割未満のスライドは、まとめるか根拠の図を足す（東北大学の発表資料チェックリストの「空白が過度に多いスライド」）。英語の併記は話すスライドではノートに移す。見本の 3・5〜8 枚目を作り直した（3 枚目は模式図、6 枚目は大きな数字 1 つ）。
  *Readability pass against published guidance: assertion–evidence as the default content type, 7+5 figure split, line-length and orphan rules, near-empty slides merged, English moved to notes; sample slides rebuilt.*
- **検査:** `officecheck.py` に、14pt が柱の行の外にないか、本文の領域からのはみ出し（FAIL）、題名の行への食い込み・グリッドからのずれ・題名の長さ・箇条書きの数・図だけのスライドの下半分の空き（注意）、「自動調整」での縮小（FAIL）、1 枚の文字数・文字のカードの埋まり方・紺の強調の数・助数詞の前の空白・単位の前の空白がない・縮めた図・細い列の折り返し・行末の 1〜2 字・中身の少なさ（注意）を足した。前の見本はこの検査で FAIL 5・注意 13 になる。
  *`officecheck.py` now checks footer-only 14pt, overflow, grid alignment, title length, bullet count, empty lower half and shrink-to-fit.*

## 2026-11-18 — 正本を GitHub に移す / Source of truth moved to GitHub

- **正本:** このリポジトリ（`kami2news/km1-design-system`）を正本にし、claude.ai のデザインシステムは使わない。配布物は `dist/`。
  *This repository is now the source of truth; distributables live in `dist/`.*
- **構成:** 公開用の `.txt` と `project/` の前提を外した。名前・勤め先を消す表が入った PDF の道具は入れず、`gen/build_pdf.py` で PDF 2 冊を作り直した。
  *Dropped the `.txt` and `project/` assumptions; PDFs are rebuilt with `gen/build_pdf.py`.*
- **道具:** `km1_pptx.js` がテーマの色を自分で書く。`gen/render_previews.py` と `gen/package.json` で見本を描き、`sizecheck.py` が単独で動く（FAIL 0）。
  *`km1_pptx.js` writes its own theme colors; previews render from the repo so `sizecheck.py` runs on its own.*
- **M1 比較:** 再現図をファイルにした（Grid・List は元の PNG、ほか 5 つは出典の寸法から SVG で描き直し）。
  *M1 reconstructions are now files (two original PNGs, five redrawn as SVG).*
- **カタログと一覧:** `components/README.md`（16 のグループ別、ライトとダークの見本）、`icons/icon-list.svg`、トークンの図 `assets/tokens/`（`tokens.md` に掲載）を追加。claude.ai の閲覧画面が見せていたものをファイルにした。
  *Added the grouped light/dark catalog, the icon sheet and token sheets — what the claude.ai viewer used to show.*
- **PDF:** `gen/build_pdf.py` を「PDF の規定」どおりに作り直した: 表紙に全 2 冊の組、ページ番号つきの目次、2 冊で通しの章番号（本編の第 11 章は別冊の案内）、変更履歴、奥付、見本は等倍で空白の行で分割、Dialog などは開いた状態、作る前に寸法と件数の検査。本編 142 ページ・別冊 119 ページ、どちらも FAIL 0。
  *Rebuilt the PDF generator to the PDF rules: set cover, paged contents, chapter numbers across volumes, changelog, colophon, true-size previews split at gaps, open overlays, checks first.*
- **適用記録:** スケジュール確認アプリのアイコンの点検（KM1 の 144 個の版に取り込み直し）を台帳に記録し、KM1 に無いアイコン 5 つ（オンライン会議・端末・未完了の丸・空き時間を探す・毎週以外の繰り返し）を不足の台帳 A5〜A9 に足した。どれも見た製品は 1 つで、2 つ目の製品での確認待ち。
  *Logged the schedule-check icon audit and added five missing icons as gaps A5–A9 (one product so far).*
- **メインカラーの書き方（D13）:** `#10218B` を「EPSON ブルー」と断定するのをやめ、「EPSON の青を参考にして選んだ紺」と書くようにした。原典の確認待ちの扱い（principles・governance・notices）も外した。値は変えていない。
  *`#10218B` is now described as a navy chosen with Epson's blue as a reference, not as "EPSON blue"; the pending source check is dropped. The value is unchanged.*
- **第三者表記:** `bundle.js` に React と Fluent UI のコードが入っていないことを確かめ、未確認の項目から外した。
  *Confirmed `bundle.js` bundles neither React nor Fluent UI code.*
- **スライドのひな形:** テーマを書き込む処理を自前にしたとき、書体の組の名前が「KM1」から「Office」に戻っていた（書体は游ゴシックのまま）。「KM1」に直し、テーマが 2026-11-15 の版と同じになったことを確かめた。
  *Restored the font-scheme name "KM1" in the slide theme; the theme again matches the 2026-11-15 build.*
- **検証セット:** 別のリポジトリ `km1-verify`（2026-11-15）の Windows 実機用の検証セットを `verify/` に移した。中の KM1 のファイルは持たず、`make_kit.py` が本体の今のファイルから組み立てる。`km1-verify` は消す。
  *Moved the Windows verification kit from `km1-verify` into `verify/`; `make_kit.py` assembles it from current KM1 files.*
- **外部レビューへの対応:** ListItem は無効のとき押しても動かないようにした（ボタンとリンクの両方）。ErrorSummary・StepFlow は固定の id をやめ、自動で振るか `id` で決められるようにした（2 つ置いても重ならない）。TimeGrid の予定の読み上げの名前を、見えている文字の順のあとに日付にした（Web・Flutter、WCAG 2.5.3）。TagPicker の入力欄にフォーカスの枠を足した。スクリムを `--opacity-scrim` の参照にした。`bundle.css` の先頭に書体の土台（`html` の書体、フォーム部品の `font:inherit`）を足し、README に導入の約束として書いた。
  *Review fixes: inert disabled ListItem, generated ids for ErrorSummary/StepFlow, TimeGrid label-in-name, TagPicker focus ring, scrim token, base font contract.*
- **検査を再現できる形に:** `gen/web_test.js`（axe・キーボード・320px・再発防止・利用シナリオ 3 つ）と `gen/check_all.sh`（全部の検査）を足し、GitHub の CI で push のたびに流す（Flutter の解析とテストも）。依存を `requirements.txt`・`gen/package.json`・`office/package.json` で固定し、`puppeteer-core` を 25 に上げて `npm audit` の指摘を 0 にした。`sync_counts.py` は管理外のファイルを読まないようにした。版ごとに Git のタグ `km1-YYYY-MM-DD` を付ける。
  *Reproducible checks: web tests and a check-all script run in CI; dependencies pinned (npm audit clean); edition tags.*
- **ライセンス（D14）:** KM1 本体を MIT License にした（`LICENSE`）。README と notices に書き、PDF の奥付とアイコンの zip にも入れた。PDF と Office には名前を書かず、ライセンスの一文（notices 2.6）だけを載せる。Microsoft の MIT の年（2020 年）を notices 2.3 に入れ、未確認から外した。
  *KM1 is now MIT-licensed (`LICENSE`); the line goes into PDFs, Office files and the icon zip without a personal name.*
- **Office の表記:** notices で決めていた非公認の表記（2.1）がひな形と見本に入っていなかったので、ライセンスの一文と一緒に入れた。見本は最後のページかノート、ひな形は本文に入れず、PowerPoint はノート、Word はファイルの説明に入れる。
  *Office samples and templates now carry the non-affiliation and license lines (templates only in notes or file properties).*
- **Flutter の CI:** 初回の CI で、最新の Flutter（3.50）では `km1_theme.dart` の画面切り替えの指定（`CupertinoPageTransitionsBuilder`）がエラーになると分かった。`material.dart` が含まなくなったため、`cupertino.dart` から読むように生成元を直した。`material.dart` の非推奨（`material_ui` への移行）は platforms に今後の課題として書き、CI ではその情報だけ落とさない。
  *First CI run found `CupertinoPageTransitionsBuilder` no longer comes via material.dart in Flutter 3.50; now imported from cupertino.dart. The material_ui migration is noted as pending.*

## 2026-11-15 — 点検への対応（実機検証とブランド色の命名を除く） / Review follow-ups

- **部品の対応表を追加:** `coverage.md`（KM1-COV-001）。Web 60・Flutter 30 の全名と、ネイティブはテーマだけであること、不足 G1〜G5（Flutter の Alert・Link の対応が無いことを含む）を記録。
  *Added the coverage matrix, including the unmapped Flutter Alert and Link.*
- **出典と帰属:** `notices.md`（KM1-LIC-001）。無関係の明記、デジタル庁の帰属と改変の断り、アイコン（MIT）と書体（OFL）の表記、出典の確認の表。README に位置づけを追記し、`documents.md` §5 と PDF ひな形に奥付を追加。
  *Added notices, a colophon rule and a template colophon.*
- **グラフ・不足領域:** `dataviz.md`（KM1-VIZ-001、提案）と `proposals.md`（期間入力・ツリー・グラフ・動きのトークン・連続色）。いずれも仕様案で、部品やトークンはまだ変えていない。
  *Spec proposals only; no components or tokens changed.*
- **導入の記録:** `adoption.md`（KM1-ADO-001）。スケジュール確認・kami2pos での使い方と、文書から読み取った穴 A1〜A4（実際の利用からの記録ではない）。`product.md` §6 から参照。
  *Adoption ledger; gaps derived from documents, not from product use.*
- **保留の期限:** `governance.md` に D10（書体の自前配信）・D11（仕様案）・D12（動きのトークン、D6 の代案）を追記し、§6 に開いている判断の確認日と「決まらないときの既定」を追加。日付は仮置きで、持ち主が変えてよい。`gen/govcheck.py` で期限を検査。
  *Deadlines table and checker; dates are provisional.*
- **書体:** `tokens.md` §7 に読み込みと代替の規則（KM1-TYP-002）、`gen/fonttest.html`（端末で使える書体を見るページ）、`fontcheck.py` の警告、`fontcheck_render.js` の `OFFLINE=1`、`verification.md` §5 と C1。
  *Font loading and fallback rules, test page, new checks.*
- **数の食い違いを直した:** README の英語の行が Flutter の部品を 28 と書いていたのを 30 に。`gen/sync_counts.py` に coverage.md の数・名前の照合と、古い部品数の走査を追加。
  *Fixed the README's English count (28 → 30) and extended sync_counts.*
- **いじらなかったもの:** 実機・Flutter・ネイティブの検証（点検の 1）と、ブランド色 `#10218B` の原典・命名（点検の 4）は意図して触っていない。
  *Items 1 (real-device verification) and 4 (brand color source and naming) are intentionally untouched.*
- **限り:** `gen/` のスクリプトは、KM1 のフォルダ全体に対してはまだ流していない。構文の確認と、合成データでの動作確認だけ。手元で `sync_counts.py --check`・`govcheck.py`・`fontcheck.py` を流すこと。
  *The gen/ scripts have not been run against the full KM1 folder; only syntax and synthetic-data checks were done.*

## 2026-11-14 — 部品カタログの無駄な空白 / Wasted blank space in the catalog

- **BottomSheet の不具合を直した:** 幅 640px 以上で中央のダイアログとして開くとき、中身が少なくても画面の高さの 80% まで伸び、選択肢とボタンのあいだに大きな空白ができていた（`position:fixed`・`inset:0`・`margin:auto` の組み合わせで高さが引き伸ばされていた）。高さを `fit-content` にして、中身の高さで開くようにした。実際の画面でも同じ空白が出ていた。
  *BottomSheet as a centered dialog (640px+) stretched to 80% of the viewport; it now fits its content. This affected real screens too.*
- **カタログの撮り方:** 中央寄せの見本（空の状態など）の左側の空白も切るようにした（中身から 16px だけ残す）。開いた状態で撮る Dialog・Drawer・BottomSheet は、内容に合わせた小さめの画面で撮り、暗い幕だけの部分を減らした。Toast は、ボタンのすぐ下に出す形で撮る（画面の中央に出るため、ボタンとのあいだが大きく空いていた）。カタログは 121 ページから 120 ページになった。
  *Catalog shots now trim left/top space, open overlays use smaller windows, and the Toast sits under its button; 121 → 120 pages.*
- Drawer の中の、選択肢と下のボタンのあいだの空白は、画面の高さいっぱいに出る横の引き出しの形どおりなので残す。
  *The gap inside the Drawer is its full-height design and stays.*

## 2026-11-14 — 部品カタログの改ページと、アイコンの説明の食い違い / Catalog page breaks and icon text

持ち主のレビュー（KM1 B 案（調整版）の採用の確認と、直すところ 3 点）に対応した。
*Follow-up to the owner's review (B style confirmed; three fixes).*

- **カタログの改ページ:** 1 ページに入らない見本を等間隔で切っていたため、アイコンの一覧（「状態の色」「お金〜添付」の行など）がページの境目で切れていた。切る位置を、行と行のあいだの空白（背景だけが 10px 以上続く所）にした。どの見本にも効く。
  *Tall previews are now cut only in blank gaps of 10px or more between rows, so icons stay with their labels.*
- **説明の食い違い:** 淡い面のあるアイコンを「60 個」としていたのを、実物どおり 63 個に（8 個を足したときに 3 個増えていた）。部品カタログの「Alert の状態の記号は今までどおり」を「4 種とも B 案。Alert の中では状態の色の塗りの形」に。`sync_counts.py` がアイコンの総数と淡い面の数も `km1-icons.json` から合わせ、ずれを検査で見つけるようにした。
  *Tint count corrected to 63; the Alert note updated; `sync_counts.py` now keeps icon totals and tint counts in step with the JSON.*
- **線の太さの書き方:** 「アイコン」1 章の大きさの表にあった「線 1px」「線 1.5px」を外し、線の太さは 8 章の描き方の決まり（16px は実寸 約 1.3px、20px は 1.45px、24px は 約 1.55px）だけで決めることにした。
  *Stroke widths now live only in §8; the size table lists use and display size.*
- 変更の記録にある「137 個」は、その時点の数なので残す。
  *The 137 in older changelog entries is historical and stays.*

## 2026-11-14 — アイコンを全部 B 案に（塗りの形・状態の記号）と 8 個の追加 / All icons in B, plus eight new ones

- **Alert の状態の記号 4 個を B 案で描いた:** お知らせ（丸に i）・完了（丸にチェック）・注意（三角に !）・エラー（丸に !）。形で区別でき、色は状態の色のまま。
  *The four Alert status symbols are now B drawings.*
- **塗りの形（Filled）も B 案から作るようにした:** Fluent の塗りの形を B 案の通常表示と並べて比べたところ、別の絵になるものが多かった（並べ替えが矢印 1 本になる、砂時計・ログアウト・整理券・密度・元に戻すの形が違う など）。そのため、同じ原図から決まり（閉じた形は塗る、中の記号はくり抜く、外の線は 1.2 倍）で作るようにした（「アイコン」8.6）。Fluent の形は、比べるための 20px だけ残す。
  *Fluent Filled did not match the B drawings, so Filled is now derived from the same drawings (Icons §8.6); Fluent shapes stay only for comparison.*
- これで Flutter のアイコンフォント（`Km1Icons.*`）の字形も B 案の形（1 色）になった。`Icon(Km1Icons.deadline)` でも B 案の形が出る。
  *Flutter font glyphs are B shapes too.*
- **利用先の調査から 8 個を足した:** `task-list`（タスク）・`notification-off`（通知オフ）・`lock-open`（ロック解除）・`timer`（タイマー）・`sparkle`（自動処理）・`view-month`（月の表示）・`text-size`（文字の大きさ）・`filter-dismiss`（絞り込みを解除）。調べた範囲と足さなかったものは「アイコン」9 章。全部で 144 個。
  *Eight icons added from a usage survey (Icons §9); 144 in total.*
- Alert の「閉じる」ボタンが × を直接描いていたので、`dismiss` に直した。
  *Alert close now uses `dismiss`.*
- `iconcheck.py`: B 案の形は 20 の格子の余白 1 で調べるようにした（Fluent の生きている範囲ではなく）。
  *`iconcheck.py` checks B shapes against the 1-unit margin.*

## 2026-11-14 — 整合性の点検 / Consistency check

点検した範囲: 公開している `.txt` と元のファイル、アイコン（一覧・Web・Flutter・型定義・部品の中の参照）、部品の数（`inventory.json`・文書・Flutter の一覧）、トークン（`tokens.json` と生成物、文書に書いた色の値、`var()` の参照）、文書のリンクとファイル名、文書に出てくる Flutter・Kotlin・Swift・Web の名前、決まりの番号、書体、PDF・Office。
*Checked: published copies vs sources, icon names across web/Flutter/types, component counts, tokens vs generated files and documented hex values, links and file names, API names in docs, rule IDs, typefaces, PDF and Office.*

- Flutter の部品の一覧（`km1_widgets.dart` の見出し）に `Km1CategoryMark`・`Km1CategoryLegend` が抜けていた。足して、Flutter 専用の部品は 30 個（文書・PDF の数も 28 → 30）。`sync_counts.py` が、見出しの一覧とファイルの中の公開している部品の一致も調べるようにした。
  *The Flutter widget list missed the two category widgets: now 30, and `sync_counts.py` checks the list against the file.*
- `km1_widgets.dart` の前提と README の Flutter の入れ方に `km1_icons_b.dart` がなかった。足した。
  *Added `km1_icons_b.dart` to the Flutter requirements.*
- IconTrial の説明に、淡い面が「予定・フォルダ・通知だけ」という古い決まりが残っていた。今の決まり（面が形の理解を助けるもの、60 個）に直した。
  *IconTrial still described the old tint scope; updated.*
- 公開している全部のファイルを、手元の正本と同じ内容で出し直した。
  *Republished every file so the artifact matches the source.*
- 問題なし: `.txt` と元のファイル、アイコンの名前（136 個・別名 1）、トークンと生成物、文書に書いた色の値（163 個のトークン）、リンク、決まりの番号（8 つ、すべて見出しで定義）、書体、PDF（2 冊）、寸法。`var()` で見つからない名前は、どれも部品が実行時に入れる値だった。
  *No other mismatches found.*

## 2026-11-14 — Flutter のアイコンのファイルを単独で組み込めるように / Flutter icon file builds on its own

- `km1_icons_b.dart` が、`km1_widgets.dart` にある `context.km1` を使っていたため、アイコンのファイルだけを組み込むとコンパイルできなかった（アプリ側からの報告）。色を `Theme.of(context).extension<Km1Colors>()`（なければ `Km1Colors.light`）で `km1_theme.dart` から直接読むように、生成の道具（`km1_bdart.py`）を直した。組み込みに要るのは `km1_icons_b.dart`・`km1_icons.dart`・`KM1Icons.ttf`・`km1_theme.dart` だけ。アプリ側の補助ファイル（`km1_context.dart` など）は要らなくなる。
  *`km1_icons_b.dart` used `context.km1` from `km1_widgets.dart`, so it failed to compile on its own. It now reads `Km1Colors` straight from the theme; only the theme file is needed.*
- `iconcheck.py` に、Flutter のアイコンのファイルが `km1_theme.dart`・`km1_icons.dart` だけで組み込めるか（ほかの KM1 のファイルの名前や `context.km1…` を使っていないか）を調べる項目を足した。古い形のファイルで FAIL になることも確かめた。
  *`iconcheck.py` now fails if the icon files depend on anything beyond the theme and font files.*

## 2026-11-14 — 書体の決まり（KM1-TYP-001）と保守 / Typeface rule and maintenance

- 書体の決まりを `tokens.md` 7 章に書いた。KM1 はゴシック体だけ。華美なセリフ体、行書・草書・楷書・筆文字、手書き風・装飾書体は使わない。明朝体とふつうのセリフ体も、ゴシックの 1 系統で揃えるため使わない（例外は他者のロゴだけ）。太さは 400 と 600、和文に斜体を使わない、並びの最後は `sans-serif`、SVG の文字は書体を明示する。
  *Typeface rule (tokens §7): sans-serif only; no ornate serifs, brush/calligraphic, script or display faces; no Mincho or plain serifs either. Weights 400/600, no Japanese italics, stacks end in `sans-serif`.*
- 等幅の並びから Courier New を外し、Cascadia Mono → Consolas → Noto Sans Mono CJK JP → Menlo にした。日本語の並びに Hiragino Sans を足した（Flutter の並びと揃えた）。
  *Mono stack drops Courier New; Hiragino Sans added to the Japanese stack.*
- Office のテーマで、言語ごとの補助の書体に残っていた既定の明朝・セリフ体・手書き風をゴシック系に置き換えた（繁体字・アラビア文字・ヘブライ文字・ベトナム語・タイ文字・インドの文字など）。`officecheck.py` が見出し・本文の欧文の書体と、補助の書体も調べるようにした。
  *Office per-script theme fonts switched to sans; `officecheck.py` checks them.*
- 書体の検査 `gen/fontcheck.py`（ソース・Office・PDF）と `gen/fontcheck_render.js`（Chrome で実際に描かれた書体）を足した。手元の検証に T1（Office と各 OS の書体）を足した。
- 保守: 文書が名前を出していた道具（`sizecheck.py`・`tokens_check.py`・`sync_counts.py`・`native.py` など）を `gen/` に置き、決め打ちのフォルダの場所をやめて `KM1_PROJECT` で指定できるようにした。
  *Maintenance: tools named in the docs now ship in `gen/`, with the project folder taken from `KM1_PROJECT`.*

## 2026-11-14 — 使う側が意図したアイコンを出せるように / Making the intended icon come out

- 「予定」と「空の予定」は通常表示で同じ絵柄だった。意味も同じ（予定の絵。「ない」ことは文言で伝える）なので `calendar` に 1 つにまとめ、`calendar-empty` は別名として残した（Web は `calendar` を出し、Flutter の `Km1Icons.calendarEmpty…` は非推奨）。空の状態の見本と Flutter の `Km1EmptyState` は `calendar` の B 案を出す（`bIcon`）。全部で 136 個（B 案 132・Alert の記号 4）。
  *`calendar-empty` merged into `calendar` (kept as an alias). EmptyState samples and `Km1EmptyState` now show the B calendar. 136 icons.*
- Flutter の標準の書き方を `Km1BIcon(Km1BIconName.deadline)` に直した。`Icon(Km1Icons.deadline)` はフォントの字形なので Fluent の形が出る（Filled 用）。
  *Flutter standard usage is now `Km1BIcon(...)`; the `Km1Icons` font is for Filled.*
- 淡い面の決まりを実際に合わせた（「閉じたもののうち、面が形の理解を助けるもの」、§4 の表に面の有無の列）。配布の zip を作る前に古い SVG を消すようにし、外したアイコン（`all-day`・`time-now`・`calendar-empty`）の SVG が残らないようにした。
  *Tint rule updated to match the drawings (tint column in §4). Stale SVGs are cleared before packing.*

## 2026-11-14 — アイコンを 137 個に、Flutter の部品も B 案に / 137 icons; Flutter parts use B icons

- 配布用の zip を `KM1_icons.zip` 1 つにまとめた（中は `icons/`・`office/`・`appicon/`、ライセンスと説明は一番上に 1 つ）。
  *Distribution is now a single `KM1_icons.zip` with `icons/`, `office/` and `appicon/` folders.*

- B 案のアイコンを 58 個足した（全部で 137 個、うち B 案 133 個）。お店・会計（カート・レシート・店・商品・割引・お金・財布・カード払い・QR コード・整理券・待ち・電卓・バーコード）、予定（予定を追加・リマインダー・メモ）、やりとりと共通の操作（添付・送信・電話・ログイン／ログアウト・再読み込み・リスト／グリッド／表・グラフ・しおり・クラウド・Wi-Fi・ライト／ダーク・拡大／縮小・再生・マイク・音量・地図・建物・学校・本・鍵・保護・アーカイブ・連絡先・交通・天気など）。Filled はそれぞれ Fluent の形。
  *Added 58 B-style icons (137 total, 133 in B) for shop and checkout, scheduling and common actions; Filled from Fluent.*
- Flutter の部品（`km1_widgets.dart`）の中のアイコン 18 か所を `Km1BIcon` に切り替えた。部品の中では `inherit: true` でまわりの色に従う。状態の記号（エラー）と、塗りの旗はそのまま。
  *Flutter parts now draw 18 icons with `Km1BIcon` (inheriting IconTheme color inside parts).*

## 2026-11-13 — KM1 B 案を全アイコンに / KM1 B style for all icons

- 持ち主の指示で、B 案（調整版）を基準に残りのアイコンも描き直した。通常表示（Regular）は 75 個すべて KM1 が描いた B 案（線 1.45、`icon-ink`、閉じた「もの」の形にだけ淡い面）。選択・強調の Filled は Fluent の形、Alert の状態の記号 4 個は Fluent のまま。
  *Per the owner, all 75 Regular icons are now drawn in the B style; Filled stays Fluent, and the four Alert status symbols are unchanged.*
- 予定の仲間（締め切り・今日が期限・仮・中止・毎週・日／週／一覧・時間割）は、右下の丸い印をやめ、予定の枠の中に記号を置く形にした。オフラインと非表示は斜線の周りをくり抜く。
  *Calendar variants put their mark inside the body; slashed icons knock out around the slash.*
- 描画データを線から輪郭に変えた（大きさごとに輪郭を計算し、Web・Flutter・SVG・Office が同じ形を塗る）。原図は `icons/km1_bdefs.py`。
  *Drawing data is now per-size outlines shared by every platform; drawings in `icons/km1_bdefs.py`.*
- 部品の中のアイコン（閉じる・矢印・チェック・並べ替えなど）も B 案になった。色は部品の文字色に従うので、チェックボックスの白いチェックなどは今までどおり。
  *Icons inside parts are B too and follow the part's text color (e.g. white checkbox ticks are unchanged).*

## 2026-11-13 — KM1 B 案（調整版）のアイコンを試験導入 / Trial of KM1 B icons

- 「KM1 アイコン作成指示書」の B 案（調整版）で、検索・予定・フォルダ・削除・警告・通知の 6 種の通常表示を KM1 が描いた形にした。線は 20px で 1.45（検索 1.35）、予定・フォルダ・通知に淡い縦のグラデーション。選択・強調の Filled と、Alert の中の状態の記号は今までどおり。
  *Six icons now use the KM1 B (adjusted) drawings at rest; Filled and Alert status symbols are unchanged.*
- 色のトークンを 3 つ足した: `icon-ink`（ライト #657283・ダーク #9AA7B8）、`icon-tint-start`、`icon-tint-end`。コントラストはどれも 3:1 以上（`iconcheck.py` で確認）。
  *Added `icon-ink`, `icon-tint-start` and `icon-tint-end` (all pairs ≥3:1).*
- Web: `Icon` と、部品の中の `icon16`・`icon20` が B 案で描く。グラデーションの ID はアイコンごとに一意。状態（ホバー・押下・選択・無効・強い背景）では親の文字色に従い、選択は Filled、強制カラーでは面を描かない。比べる用に `variant:'fluent'`、全体を戻す `setIconStyle('fluent')`。検索欄の虫めがねも B 案になった。
  *Web `Icon`, `icon16` and `icon20` render B; unique gradient IDs; state, Filled, forced-colors handling; `variant:'fluent'` and `setIconStyle('fluent')` for comparison and rollback. The SearchBox glass is now B.*
- Flutter: 同じ原図から `Km1BIcon` を作る `icons/km1_bdart.py` と `km1_icons_b.dart`。配布用の SVG・スプライト・Office の素材も B 案に。16px の通知は振り子を小さく下げる光学調整をした。
  *Flutter `Km1BIcon` generated from the same paths; SVG, sprite and Office files updated; 16px bell optically adjusted.*
- カタログに「IconTrial」（導入前と導入後、16・20・24px、状態、今ある部品の中）を足した。
  *Added the IconTrial catalog card.*

## 2026-11-13 — アイコンをこれまでの部品になじむ形に / Icons that match existing parts

- 最初に KM1 が描いた 22 個は、これまでの部品と並べると塗りが重く、形が記号的すぎて浮いた（持ち主の確認）。Fluent System Icons に同じ意味のものがあるものはすべて Fluent の形に替えた（締め切り＝`calendar_clock`、今日が期限＝`calendar_error`、仮＝`calendar_question_mark`、中止＝`calendar_cancel`、毎週＝`calendar_arrow_repeat_all`、日／週／一覧＝`calendar_day`／`calendar_work_week`／`calendar_agenda`、勤務＝`shifts`、教室の変更＝`door_arrow_right`、提出＝`document_arrow_up`、試験＝`clipboard_task`、状態＝`info`／`checkmark_circle`／`warning`／`error_circle`、密度＝`line_horizontal_5`／`4`／`3`）。KM1 の名前はそのまま。
  *The first 22 KM1 drawings looked heavy and too symbolic next to existing parts; every one with a Fluent equivalent now uses the Fluent shape, keeping the KM1 names.*
- KM1 が描くのは Fluent にないものだけにし、描くときは Fluent の絵を土台にする決まりにした。いま KM1 が描いているのは時間割（Fluent の `calendar_empty` に曜日 × 時限のマス）だけ。`time-now` と `all-day` はアイコンから外した。状態の記号を形で分ける決まり（八角形など）はやめた。全部で 78 個。
  *KM1 now draws only what Fluent lacks, on a Fluent base (currently just the timetable). `time-now` and `all-day` were removed; status shapes follow Fluent again. 78 icons.*
- Fluent にその大きさがない 4 つ（`room-change` の 24px、`density-compact` の 16・24px、`density-regular` の 24px）は 20px の形を拡大・縮小して補い、検査で注意として出す。
  *Missing Fluent sizes are scaled from 20px and flagged by the checker.*

## 2026-11-13 — KM1 のアイコン / KM1 icons (KM1-ICO-001)

- アイコンを **KM1 の名前で引く 1 つのセット**にした（80 個）。KM1 が描いたもの 22 個（予定・時間割・締め切りの仲間 15、状態の記号 4、密度 3）と、Fluent System Icons（MIT）から形をそのまま取り込んだもの 58 個。各アイコンに 16・20・24px の Regular と Filled がある。
  *Icons are now one set addressed by KM1 names (80): 22 drawn by KM1 and 58 imported unchanged from Fluent System Icons (MIT), each in 16/20/24px Regular and Filled.*
- 描き方の決まり（20px の格子、1px の線、生きている範囲、塗りのくり抜き、予定の枠の仲間、状態は形でも分ける）を「アイコン」の章（`icons.md`）にした。本編の章を 1 つ足し、部品は第 12 章、変更履歴は第 13 章になった。
  *Drawing rules are in the new Icons chapter; components move to chapter 12 and the changelog to 13.*
- **状態の記号を形でも分けた:** お知らせ＝角丸の四角、完了＝円、注意＝三角、エラー＝八角形。`Alert` と入力欄のエラーの記号が新しい形になった。
  *Status symbols differ by shape; `Alert` and field errors use them.*
- Web: `Icon` 部品と `ICONS`。部品の中の矢印・閉じる・チェックなども KM1 のアイコンに置き換えた（見た目は同じ形）。Flutter: アイコンフォント `KM1Icons.ttf` と `Km1Icons`。`km1_widgets.dart` は `fluentui_system_icons` を使わなくなった（pubspec にフォントを登録する）。Office: SVG と PNG の素材集。ネイティブ（Windows・iOS）は SVG を取り込む決まりにした。
  *Web `Icon`; built-in component icons now come from the set. Flutter icon font and `Km1Icons` replace `fluentui_system_icons`. Office SVG/PNG pack. Native apps import the SVGs.*
- **アプリアイコン:** KM1 のしるし（紺に白の「KM1」と表紙の帯）を決め、Web・Android・iOS・Windows の大きさを全部書き出す `km1_appicon.py` を作った。絵柄は直径 60% の円に収め、コントラスト 3:1 未満なら作らない。ほかのアプリは色と絵柄を変えるだけで使える。
  *App icon: the KM1 mark plus a generator for every platform size; motifs fit a 60% circle and need 3:1 contrast.*
- 検査 `iconcheck.py`（16・20・24px の両方の種類があるか、枠からのはみ出し、生きている範囲、名前、出典、Flutter のフォントの字形の数）。カタログに「Icon」「AppIcon」のカードを足した。
  *Added `iconcheck.py` and the Icon and AppIcon catalog cards.*
- 見本の個人情報を減らした: 入力欄の見本の部署名を一般的なものに、時間割の見本の勤務先を「駅前店」にした。
  *Replaced a real department and workplace in previews with neutral samples.*

## 2026-11-13 — 分類を色 × 模様に / Categories as color × pattern (KM1-COL-001)

- 分類の区別に模様を足した。8 つの模様（塗り・横線・縦線・斜線・格子・斜め格子・点・市松）と 18 色で 144 通り。色が見分けにくい人、白黒の印刷、ハイコントラスト表示でも区別が残る。
  *Added 8 patterns to the 18 category colors: 144 combinations that survive color-vision differences, grayscale and forced colors.*
- 模様は文字の下に描かない決まりにし、使う場所を分類のしるし・凡例・グラフの塗りに限った。予定のブロックは淡い塗りと帯のままで、題名の前にしるしを出す。
  *Patterns never go under text: marks, legends and chart fills only.*
- 部品: `CategoryMark`・`CategoryLegend`・`categoryStyle(i)`・`PATTERNS`。`Timetable`・`TimeGrid` の項目に `pattern` を足した（省けば今までどおり）。Flutter は `Km1Pattern`・`Km1PatternPainter`・`Km1CategoryMark`・`Km1CategoryLegend`・`km1CategoryStyleAt`、`Km1Slot`・`Km1TimeGridEvent` に `pattern`。
  *New components and a `pattern` prop on Timetable and TimeGrid items (optional; existing use unchanged), mirrored in Flutter.*
- 見本カード「CategoryPattern」（144 通りの表、既定の割り当て、白黒での見え方、グラフの塗り）を足し、時間割と週の予定の見本に模様と凡例を付けた。週の予定の見本の 1 時間の高さを、README の決まりどおり 56px に直した（48px になっていた）。
  *Added the CategoryPattern card; timetable and week previews now show marks and legends; fixed the week preview's hour height to the documented 56px.*
- Office: グラフの系列が 2 つ以上なら模様も付ける決まりと、PowerPoint の模様の対応（`dkHorz` など）を足した。スライド見本に模様つきのグラフを足し、グラフの軸の線を KM1 の色（#616161）にした。`officecheck.py` はグラフの色も調べる。
  *Office rule for patterned chart series, sample slide added, axis lines in a KM1 color; `officecheck.py` now checks chart colors.*

## 2026-11-13 — 本編と部品カタログの 2 冊に / Two-volume set

- 部品の章を別冊「KM1 部品カタログ」（`KM1_部品カタログ.pdf`、全ページ横向き）に分け、本編「KM1 デザイン標準」（縦）と 2 冊で 1 組にした。表紙に「全 2 冊・本編／別冊」と組のファイル名を書き、版の日付をそろえ、`gen/pdf.py` が 1 回で 2 冊とも作って両方を検査する。本編の第 11 章は別冊の案内（載せている部品の一覧と寸法の決まりの場所）。章の番号は 2 冊で通し。
  *Split the Components chapter into a landscape companion volume; both volumes share the edition, cross-reference each other on the cover, and are built and checked together. Chapter 11 in the main volume points to the catalog.*
- 「PDF の規定」§5 に「分冊」の決まりを足した。
  *Added a Volumes rule to the PDF rules.*

## 2026-11-13 — 部品の寸法を定義どおりに、Word と PowerPoint の規定 / Component sizes, Word and PowerPoint

**部品の寸法 / Component sizes**
- 全部の見本を PC とスマホの幅で開いて測り、定義からずれていた部品を直した: アコーディオンの見出し・一覧の行・ExpansionEditor が 36px（上下の余白 8px）→ 32px（6px）、Alert などの閉じるボタンが親の高さで 37px に伸びていた → 32 × 32px、タグを外す × が 28px → 24px（`control-sm`）、2 行の一覧の行が 54px → 52px（題名と説明の間 4px）、StepFlow の番号の行の高さを型の表の 16px に。Flutter の `Km1ListItem`・`Km1ExpansionEditor` も同じ余白に。
  *Measured every preview on PC and phone and fixed drifted sizes (36→32px rows, 37→32px close buttons, 28→24px tag remove, 54→52px two-line rows).*
- 「トークン › 部品の寸法」の表を足し、`gen/sizecheck.py` が全部の見本をこの表と照らす。表にない値があれば PDF を作らない。
  *Added the Component sizes table; `gen/sizecheck.py` enforces it before every PDF build.*
- PDF の部品の章: 見本はすべて等倍。縦に長い見本は縮めずに等倍のまま分けて載せる。PDF の上で実際の倍率が 99.8〜100.2% であることを測って確かめた。
  *All previews are true size in the PDF (measured 99.8–100.2%); tall ones are split, never scaled.*

**Word と PowerPoint / Word and PowerPoint**
- KM1-DOC-002（Word）と KM1-DOC-003（PowerPoint）を `office.md` に足した。書体は游ゴシック、色はテーマを KM1 に、文字の大きさは Word は PDF の規定と同じ、スライドは 1pt＝1px で KM1 の型の表の値だけ。
  *Added the Word and PowerPoint rules: Yu Gothic, KM1 theme colors, PDF-rule sizes in Word and type-ramp sizes on slides (1pt = 1px).*
- ひな形 `KM1_文書.dotx`・`KM1_スライド.potx` と見本、それを作る `office/km1_docx.js`・`km1_pptx.js`、検査 `office/officecheck.py` を足した。
  *Added templates, samples, generators and `officecheck.py`.*
- PDF に「8. Word と PowerPoint の規定」の章を足し、後ろの章の番号を詰めた（抜けていた 10・11 もなくした）。

## 2026-11-13 — デザイン標準とビジュアルカタログを 1 冊に / One PDF

- 別に作っていた「KM1 ビジュアルカタログ」をやめ、デザイン標準の「部品」の章を横向きのページにした。
  *Dropped the separate visual catalog; the Components chapter is now landscape.*
- 部品の見本は**等倍**（画面の 1px ＝ 0.26mm、96dpi 相当）で載せる。ボタンは 32px の高さのまま紙に出るので、部品どうしの大きさを比べられる。縦が 1 ページに入らない画面の例・比較などだけ縮め、縮めたときは見本の下に倍率を書く。見本は中身の大きさで切り抜き、説明は見本の下に 3 段で詰める。メニュー・ポップオーバーは開いた状態で撮る。
  *Previews are printed at true size (1px = 0.26mm); only previews taller than a page are scaled, with the ratio in the caption. Previews are cropped to content, text flows in three columns below, and Menu/Popover are shown open.*
- 「PDF の規定」: 1 冊の中で章ごとに向きを変えてよいこと、その作り方（CSS の名前つきページ）を足した。

## 2026-11-13 — 設計レビューへの対応 / Review fixes

**直したこと / Fixed**
- Dialog・Drawer・BottomSheet のボタンの並び: 幅 479px 以下で CSS が見た目だけを逆にしていたのをやめ、`FormActions` と同じく DOM の順ごと入れ替えるようにした。Tab の順と見た目の順がいつも一致する（WCAG 1.3.2・2.4.3）。公開 API は変わらない。
- 余白の規則の食い違い: 12px（`space-md`）を「コントロールの内側・カードの中の小さなまとまり・compact 密度のコンテナの内側」に使えると明記した（基本値は変えない）。
- 古い部品数: `gen/sync_counts.py` が `inventory.json` に数をまとめ、README・プラットフォーム・PDF の表紙の数を書き換える。PDF を作るときに食い違いがあれば止まる。
- Table の compact: 中にリンク・ボタン・入力がある行も、操作領域の高さを保つ（`:has()`）。表示専用の行と、選べる行・操作がある行の違いを明記した。
- List: 今開いている行（一覧・詳細の画面）に印を付ける（`current` を button の行にも）。

**追加 / Added**
- 「検証」（`verification.md`）: 記録欄、利用シナリオ 3 つ、OS ごとの手順、大量データの測定と「1 画面 500 行まで」の規則。
- 「運用の決まり」（`governance.md`）: 判断の 6 つの状態、判断の記録 9 件、判断を変える手続き、互換性、出典の確認の状態（`#10218B` の原典は未確認）。
- 「画面の組み立て › 画面の型」と見本「画面の例」3 つ（ScreenAddEvent・ScreenListEdit・ScreenOffline）。
- 「トークン」: 用途トークンの状態（定義済・適用済）、作業の目的による密度の選び方。`layout-section-gap` を StepFlow で使い始めた。
- `Button` に `form`（外にある form を送るとき）。
- 「KM1 ビジュアルカタログ」（横向き A4・見本ごとに 1 ページ）を仕様書とは別に作る（`gen/catalog.py`）。→ 同じ日に、デザイン標準の「部品」の章へ統合した（上の項）。

**点検 / Checked** — README の「利用シナリオと見直し」。未確認: 実機、読み上げソフト、各 OS のビルド。

## 2026-11-13 — トークンの構造と密度（KM1-TOK-001）/ Token structure and density

**追加 / Added**
- 「トークン」（`tokens.md`）: 三つの段、用途別の余白、影響の範囲の表、密度、OS ごとの操作領域、Spectrum 2 から取り込んだもの・取り込まなかったもの。
- `tokens.json` に `spacingRole`（用途別の余白 8 個）と `platformTarget`（OS ごとの操作領域 6 個）。どちらも新しい基本値ではなく、`ref` の基本トークンを指す。
- 密度: Card・Table・SortableList の `density`（compact・regular・spacious）と、入れ物の `data-density`。Flutter は `Km1Density`、`Km1Table`・`Km1SortableList` の `density`。
- 生成物: tokens.css・Flutter（`Km1SpaceRole`・`Km1Density`・`Km1PlatformTarget`）・WinUI・Compose・SwiftUI に用途別の余白と操作領域。
- 道具: `gen/tokens_check.py`（値と参照先の照合、影響の範囲の表）。見本「Density」（3 つの密度を並べて比べる）。

**変更（今までの書き方のまま動く）/ Changed (backward compatible)**
- Flutter の `Km1Theme.targetFor()` と SwiftUI の `hitTarget` が、直接書いていた 48・44 の代わりにトークンから生成した値を使う（値は同じ）。
- Flutter の `Km1Table` の選択のチェックの欄に、操作領域の最小の高さを明示した（密度で行が詰まっても下回らない）。

**変えなかったこと / Kept**
- 基本トークンの値、色、書体、文字の階層、アイコン、角丸、ライト・ダーク、部品の公開 API（`density` を足しただけ）。既定（regular）の見た目は、全 65 の見本で画素単位で同じ（動きのある部品はアニメーションを止めて比較）。

**点検 / Checked** — 「トークン」と README を参照。未確認: 実機・読み上げソフト、Flutter と各 OS のビルド。

## 2026-11-13 — KM1 × M1（KM1-M1-001）/ Material Design 1 integration

**追加 / Added**
- 「KM1 × M1」（`m1.md`）: 取り込む原則、M1 の 26 部品・20 パターンとの対応表、添付の案の訂正 16 件、部品の選び方、見た目の比較、判断を仰ぐ事項、テスト、差分。
  *"KM1 × M1": principles, mapping of M1's 26 components and 20 patterns, 16 corrections to the proposal, selection guide, comparison, open decisions, tests and diff.*
- Web: `List`・`ListItem`・`ListSection`・`ListSectionHeader`、`ContextualActionBar`・`useSelection`、`ExpansionEditor`、`StepFlow`、`BottomSheet`、`ImageGrid`。
- Flutter: `Km1ListItem`・`Km1ListSectionHeader`・`Km1ContextualActionBar`・`Km1ExpansionEditor`・`Km1StepFlow`（`Km1Step`）・`showKm1BottomSheet`・`Km1ImageGrid`（`Km1ImageItem`）。
- 見本 / Cards: 「M1 比較」7 枚（原型の再現と KM1 案の並置）と部品の選び方の早見図。
- パターン / Patterns: 「通信できないとき」「権限を求めるとき」。
- アイコン / Icons: image、cloud off、edit、chevron up（Fluent System Icons 16 regular）。

**変更（今までの書き方のまま動く）/ Changed (backward compatible)**
- `Table` の一括操作を `ContextualActionBar` で描くようにした。見た目と文言は同じ。「選択を解除」のあとフォーカスが消える不具合を直した。
  *Table bulk actions render through ContextualActionBar; same look and text; fixed focus loss after "clear selection".*
- フォームの章: 3 工程以上は `StepFlow`、1 項目ずつの設定は `ExpansionEditor` へ案内。
- デザイン原則: M1 から取り込むものを明記。

**変えなかったこと / Kept**
- トークン、FAB と Ripple の禁止、ブランド色、入力方法で決まる高さ。

**点検 / Checked** — 新しい部品の動き 50 項目（320・360・1366px、ダーク 1024px）、axe 回帰 118 ページで違反 0。未確認: 実機、読み上げソフト、強制カラーの実表示、Flutter のビルド。
*50 scripted checks; axe regression over 118 pages with 0 violations. Not verified: devices, screen readers, forced-colors rendering, Flutter builds.*

## 2026-11-13 — PDF の規定（KM1-DOC-001）/ PDF documents

**追加 / Added**
- 「PDF の規定」（`documents.md`）: PDF にするかの判断、判型と余白、文字、色と印刷、文書の組み立て、文書情報、個人情報、作り方（HTML・Word・Google ドキュメント）、検査、長期保存。
  *"PDF documents": when to use PDF, page setup, type, color and print, structure, properties, personal data, how to export, checks, archiving.*
- 道具 / Tools（`pdf/`）: `km1-print.css`（ひな形）、`template.html`（見本）、`km1_finish.py`（XMP・リンクの説明・しおりの修正）、`pdfcheck.py`（機械の検査。PDF/UA-1 の Matterhorn Protocol の一部と KM1 独自の項目）。
  *`km1-print.css`, `template.html`, `km1_finish.py` and `pdfcheck.py` (a subset of PDF/UA-1 Matterhorn machine checks plus KM1 items).*

**変更 / Changed**
- KM1 自身の PDF を規定に合わせた: 図に代替テキスト、XMP、リンクの説明を追加。柱と英語の行の色をトークン（`ink-tertiary`）に揃えた。`pdfcheck.py` で FAIL 0。PDF/UA への準拠はまだ名乗らない（PAC・veraPDF で未検査）。
  *KM1's own PDF now follows the rules: figure alt text, XMP, link descriptions; running-head and English-line colors aligned to `ink-tertiary`. `pdfcheck.py` reports 0 FAILs. No PDF/UA claim yet (not run through PAC or veraPDF).*

## 2026-11-13 — フォームの組み立て（KM1-PAT-001）/ Form layout

**追加 / Added**
- 「画面の組み立て › フォーム」: 1 列が基本、2 列の条件、間隔、グループ、条件で出る欄、入力の確認とエラー、ボタン、密度、Flutter での対応。
  *Patterns › Forms: one column by default, the two-column rule, spacing, groups, conditional fields, validation and errors, buttons, density, Flutter mapping.*
- 部品 / Components: `FormGroup`、`FormActions`、`FormGrid`（と `FormItem`）、`ConditionalField`、`ErrorSummary`、フック `useForm`。
- Flutter: `Km1Form`、`Km1FormGroup`、`Km1FormGrid`、`Km1FullSpan`、`Km1ConditionalField`、`Km1ErrorSummary`（`Km1FormError`）、`Km1FormActions`。
- アイコン `errorCircle`（Fluent System Icons の error_circle_16_regular）。
  *Icon `errorCircle` (Fluent System Icons error_circle_16_regular).*

**変更（今までの書き方はそのまま動く）/ Changed (backward compatible)**
- `Input`・`Select`・`Textarea`・`Checkbox` が `name`・`onBlur` を受け取る。`Input` は `autoComplete`・`inputMode` も。
  *`Input`, `Select`, `Textarea` and `Checkbox` accept `name` and `onBlur`; `Input` also takes `autoComplete` and `inputMode`.*
- `RadioGroup` が `id`・`hint`・`error` を受け取る。エラーは `aria-invalid` と `aria-describedby` で組に結ぶ。
  *`RadioGroup` accepts `id`, `hint` and `error`; errors are tied to the group with `aria-invalid` and `aria-describedby`.*
- `Input` の見本の名前を架空の名前に変えた。 *The `Input` preview now uses a fictional name.*

**変えなかったこと（Carbon と違う所）/ Kept as is (differs from Carbon)**
- ボタンの位置（PC は主ボタンが右、スマホは主ボタンが上）、「※必須」の印、送信ボタンを無効にしないこと。理由は「画面の組み立て › フォーム」。
  *Button placement (primary right on PC, on top on phones), the "※必須" marker, and never disabling submit. Reasons are in Patterns › Forms.*
- Carbon の Fluid スタイルと密度の切り替えは採らない。 *Carbon's Fluid style and a density switch are not adopted.*
- 新しいトークンは足していない。 *No new tokens.*

**点検 / Checked** — README の「フォーム（KM1-PAT-001）の点検」。未確認: 実機、スクリーンリーダー、強制カラーの実表示、Flutter のビルド。
*See "Forms check" in README. Not yet checked: real devices, screen readers, actual forced-colors rendering, Flutter builds.*

## 2026-11-12 — 各 OS 向けのテーマ / Native themes

- WinUI 3（`KM1.xaml`）、Jetpack Compose（`Km1Theme.kt`）、SwiftUI（`KM1Theme.swift`）を `tokens.json` から生成。
  *Generated WinUI 3, Jetpack Compose and SwiftUI themes from `tokens.json`.*
- 部品を 40 個に増やし、Flutter の KM1 専用部品を 14 個にした。
  *Components grew to 40; Flutter gained 14 KM1 widgets.*
