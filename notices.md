# 第三者表記と非公認 / Notices

KM1-LIC-001。KM1 が参考にしたもの、取り込んだもの、使っているものの権利と、KM1 を外に配るときに入れる表記。法的な助言ではない。配る前に、各出典の原文で確かめる。
*KM1-LIC-001. The rights attached to what KM1 references, adopts or uses, and the notices to include when KM1 is shared outside. Not legal advice; check the originals before distributing.*

## 1. KM1 の立場 / KM1's position

KM1 は個人が作ったデザイン標準で、Microsoft、セイコーエプソン、東京科学大学（Science Tokyo）、デジタル庁をはじめ、本文に名前が出る組織のいずれとも関係がない。どの組織も KM1 を作成・承認・推奨していない。名前は、考え方や出典を示すためだけに書いている。名称・ロゴ・商標は各権利者のもの。
*KM1 is a personal design standard with no affiliation to Microsoft, Seiko Epson, Institute of Science Tokyo, Japan's Digital Agency or any other organization named in the text. None of them created, approved or endorsed it. Names appear only to credit ideas and sources; names, logos and trademarks belong to their owners.*

**KM1 のライセンス / KM1's license:** KM1（コード・文書・アイコンの絵・PDF・Office のひな形）は MIT License で公開する。著作権表示と全文はリポジトリの `LICENSE`（名前はそこにだけ書く）。第三者の素材（Fluent System Icons の MIT など）は、それぞれの条件が別にかかる（3 章）。
*KM1 (code, docs, icon drawings, PDFs, Office templates) is released under the MIT License; the copyright notice and full text are in `LICENSE`, the only place the name appears. Third-party material keeps its own terms (section 3).*

## 2. 外に配る文書の固定の文言 / Fixed wording for shared documents

PDF の奥付、Office のひな形、素材集の README などに、必要な分をそのまま入れる。
*Paste what applies into a PDF colophon, Office template, asset-pack README and so on.*

### 2.1 非公認の表記（外に配るものすべて）/ Non-affiliation (everything shared)

> KM1 は個人が作ったデザイン標準です。Microsoft、セイコーエプソン、東京科学大学（Science Tokyo）、デジタル庁、そのほかの組織が作成・承認・推奨したものではなく、これらの組織とは関係がありません。名称・商標は各権利者のものです。
> *KM1 is a personal design standard. It was not created, approved or endorsed by Microsoft, Seiko Epson, Institute of Science Tokyo, Japan's Digital Agency or any other organization, and is not affiliated with them. All names and trademarks belong to their owners.*

### 2.2 デジタル庁の表記（部品の使い方の規則を含むもの）/ Digital Agency (when component-usage rules are included)

KM1 の部品の使い方の規則（ボタンの配置、無効にしない扱い、補足とエラーの位置、必須表示、Radio と Select の使い分け、通知の閉じ方）は、デジタル庁デザインシステムを読み、KM1 の言葉で書き直したもの。デジタル庁のルールでは、「デザインシステム本体」（ガイドライン・コンポーネントの文書）を利用するときは出典を書き、編集・加工したときはそのことも書く。加工した内容をデジタル庁が作ったように見せてはいけない。
*KM1's component-usage rules were rewritten in KM1's words from the Digital Agency design system. Its terms require a source line for the guidance itself, a note when it is edited or adapted, and forbid presenting adapted content as the Agency's own.*

> 出典：デジタル庁デザインシステムウェブサイト https://design.digital.go.jp/dads/ をもとに、KM1 作成者が編集・加工して作成。加工した内容はデジタル庁が作成したものではありません。
> *Source: Digital Agency Design System website https://design.digital.go.jp/dads/ , edited and adapted by the KM1 author. The adapted content was not created by the Digital Agency.*

根拠: デジタル庁デザインシステムの「利用ルール」（https://design.digital.go.jp/introduction/notices/ 、2026-11-15 に確認）。
*Basis: the Agency's usage rules page, checked 2026-11-15.*

### 2.3 アイコン（KM1 のアイコンを含むもの）/ Icons

> KM1 のアイコンは、Fluent System Icons（Microsoft、MIT License）をもとに描き直したものです。Copyright (c) 2020 Microsoft Corporation. ライセンスの全文は https://github.com/microsoft/fluentui-system-icons の LICENSE を参照してください。
> *KM1 icons are redrawn from Fluent System Icons (Microsoft, MIT License). Copyright (c) 2020 Microsoft Corporation. See the LICENSE in https://github.com/microsoft/fluentui-system-icons for the full text.*

素材集（SVG・PNG）を配るときは、LICENSE の全文を同梱する。MIT は、複製や大部分の使用に著作権表示と許諾文を付けることを条件にしている。著作権表示の年は原文で確かめて転記する。
*When shipping the SVG/PNG pack, include the full LICENSE text. MIT requires the copyright and permission notice with copies or substantial portions; copy the exact year from the original.*

### 2.4 書体 / Typefaces

> 本文の書体は Noto Sans JP・Noto Sans CJK JP（SIL Open Font License 1.1）。
> *Body type is Noto Sans JP / Noto Sans CJK JP (SIL Open Font License 1.1).*

フォントのファイルを配るとき(Flutter アプリへの同梱、自前配信)は、配布元の `OFL.txt` を同梱する。PDF への埋め込みは OFL で認められている。
*Ship the font's own `OFL.txt` when distributing font files (Flutter bundle, self-hosting). Embedding in PDFs is permitted by the OFL.*

### 2.5 作成者の表記 / Author line

既定は「KM1 作成者」。実名を書くかどうかは持ち主が決める。`documents.md` 7 章は、外に配る PDF に個人名を残さない決まりなので、実名を書くなら、その決まりとの食い違いを先に直す。
*The default is "KM1 author". Whether to print a real name is the owner's call; `documents.md` ch. 7 keeps personal names out of shared PDFs, so resolve that conflict first.*

### 2.6 KM1 のライセンス / KM1 license

> KM1 は MIT License で公開しています。ライセンスの全文と著作権表示は https://github.com/kami2news/km1-design-system の LICENSE を参照してください。
> *KM1 is released under the MIT License. See the LICENSE in https://github.com/kami2news/km1-design-system for the full text and copyright notice.*

PDF と Office のひな形にはこの文だけを載せ、個人名は書かない（`documents.md` 7 章）。名前は `LICENSE` の著作権表示にだけ書く。コードや素材集を配るときは `LICENSE` の全文を同梱する。
*PDFs and Office templates carry only this line, no personal name (documents.md §7); the name appears only in the `LICENSE` notice. Ship the full `LICENSE` with code and asset packs.*

## 3. 出典ごとの扱い / Source by source

確認の状態: **済**（公式のページで確認）、**一般**（広く知られる条件で、配る前に原文で確認する）、**要確認**（条件を読んでいない）。
*Status: confirmed (official page read), general (widely known terms; verify before distributing), to verify (terms not read).*

| 出典 / Source | 権利者と条件 / Owner and terms | KM1 の使い方 / How KM1 uses it | 配るときの表記 / Notice | 状態 |
|---|---|---|---|---|
| Fluent 2（原則・トークンの構造・部品の作法）| Microsoft。Fluent UI のコードは MIT。デザイン文書の利用条件は読んでいない | 構造と、公開されているトークンの値を土台にした | 2.1。取り込んだコードの有無は未確認 | 要確認 |
| Fluent System Icons | Microsoft、MIT | 原図をもとに KM1 のアイコンを描き直した | 2.3 | 一般 |
| Noto Sans JP・Noto Sans CJK JP・Noto Sans Mono CJK JP | SIL OFL 1.1 | Web は Google Fonts から読み込み、PDF に埋め込み、Flutter に同梱 | 2.4 | 一般 |
| Hind | SIL OFL 1.1（Indian Type Foundry） | 英語の書体の候補 | 2.4 | 一般 |
| Segoe UI・游ゴシック・Meiryo UI・ヒラギノ角ゴ | 各 OS・Office の書体 | 書体名を並びに書くだけ。ファイルは同梱も再配布もしない。Office 文書にも埋め込まない | 不要 | — |
| デジタル庁デザインシステム | デジタル庁。本体は出典と加工の記載が条件。Figma は CC BY 4.0、コードは MIT、ロゴは別 | 部品の使い方の考え方を KM1 の言葉で書き直した。Figma・コード・ロゴは取り込んでいない | 2.2 | 済 |
| Science Tokyo デザインシステム | 東京科学大学。利用条件のページは読んでいない | アクセシビリティの条件と書体の考え方を読み取った。配色・ロゴ・形状・文章は取り込んでいない | 2.1 | 要確認 |
| EPSON（FlipUI・Smart Panel・ユニバーサルデザインの公開説明）| セイコーエプソン。「EPSON」は同社の商標 | 考え方を読み取った。ロゴ・文章・画像は取り込んでいない。メインカラー `#10218B` は EPSON の青を参考にして KM1 が選んだ色で、EPSON の色として示さない（`principles.md`） | 2.1 | 要確認（商標の使い方） |
| IBM Carbon（フォームほか）| IBM。コードは Apache-2.0 で公開 | 考え方だけ。コードと CSS は取り込んでいない | 2.1。出典は本文に書いてある | 一般 |
| Material Design 1 | Google | 「用途と目的がはっきりした UI」の考え方だけ。見た目・コード・アイコンは取り込まない | 2.1 | 一般 |
| Adobe Spectrum 2 | Adobe | トークンの考え方（三段・余白の二系統）だけ | 2.1 | 一般 |
| WCAG 2.2・WAI-ARIA APG | W3C | 達成基準の番号と、部品のキーボード挙動を実装の根拠にした。文章は転記していない | 出典の表示 | 一般 |
| Nielsen の 10 のユーザビリティ原則 | Nielsen Norman Group | 趣旨を KM1 の言葉で書き直した | 出典（`product.md`） | 一般 |
| ISO 9241-210 | ISO | 4 つの活動の順番だけ。規格の文章は転記していない | 出典（`product.md`） | 一般 |
| axe-core | Deque、MPL-2.0 | 検査の道具として使うだけ。配布物に含めない | 不要 | 一般 |
| React 18 | Meta、MIT | 部品の実行に使う。`bundle.js` には同梱せず、外で読み込んだ React（`window.React`）を使う。見本の描画では `gen/package.json` で入れる（2026-11-18 に確認） | 同梱しないので不要。同梱するなら MIT の表記 | 済 |

## 4. 配布物ごとの確認 / Checklist per deliverable

| 配布物 / Deliverable | 入れるもの / Include |
|---|---|
| KM1 の PDF（本編・部品カタログ）| 奥付に 2.1・2.2・2.3・2.4・2.6。作成者は 2.5 |
| Office のひな形と見本（`.dotx`・`.potx`・`.docx`・`.pptx`）| 2.1 と 2.6。見本は最後のページかノートに。ひな形は本文に入れず、PowerPoint はノート、Word はファイルの説明（使う人の文書に写らないように）。游ゴシックは埋め込まない |
| アイコンの素材集（SVG・PNG）| 2.3、KM1 の `LICENSE` と `LICENSE-Fluent.txt` の全文 |
| Flutter のコード・パッケージ | README に 2.1・2.3、KM1 の `LICENSE` の全文。フォントを同梱するなら `OFL.txt`（2.4） |
| Web の部品（`bundle.js`・`bundle.css`）| README に 2.1、KM1 の `LICENSE` の全文。React を同梱するなら MIT の表記 |
| 社外に見せる画面の写し | 他社のロゴ・商標をそのまま写さない |

## 5. 言葉の使い方 / Wording rules

- 他の組織の名前は「参考にした」「考え方を読み取った」「出典」の範囲で書く。「公式」「認定」「承認」「推奨」「提携」は、他の組織の名前と一緒に書かない。
  *Name other organizations only to say "referenced", "read the thinking of" or "source". Never pair them with "official", "certified", "approved", "endorsed" or "partner".*
- 「Fluent 2 準拠」は「Fluent 2 の構造・値に従う」という意味でだけ使い、Microsoft の認定を受けたように読める文にしない。例: ×「Microsoft 認定の Fluent 2 準拠デザイン」 ◯「Fluent 2 の構造に従う個人のデザイン標準」。
  *"Fluent 2-based" means "follows Fluent 2's structure and values", never "certified by Microsoft".*
- ロゴ・マーク・商標を画像として使わない。使う必要があるときは、各社の利用規約に従う。
  *Do not use logos, marks or trademarks as images; if needed, follow each owner's terms.*
- 他の文章の引用は短く、出典を付ける。長い転記はしない。
  *Quote briefly with a source; no long transcriptions.*

## 6. 未確認 / Open items

- Fluent 2 のデザイン文書の利用条件、Science Tokyo の利用条件、セイコーエプソンの商標の使い方。
- 作成者の表記（2.5）。

`bundle.js` に React と Fluent UI のコードが入っていないこと、Microsoft の MIT の年（2020 年、`LICENSE-Fluent.txt`）は 2026-11-18 に確かめた。

*Open: Fluent 2 design-doc terms, Science Tokyo terms, Seiko Epson trademark use, and the author line. (Microsoft's MIT year, 2020, was taken from `LICENSE-Fluent.txt` on 2026-11-18.) (`bundle.js` was checked on 2026-11-18: it bundles neither React nor Fluent UI code.)*
