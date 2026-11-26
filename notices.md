# 表記とライセンス / Notices

KM1-LIC-001。KM1 が使っている第三者の素材の権利と、KM1 を外に配るときに入れる表記。法的な助言ではない。配る前に、各素材の原文で確かめる。
*KM1-LIC-001. Rights attached to third-party material KM1 uses, and the notices to include when KM1 is shared. Not legal advice; check the originals before distributing.*

## 1. KM1 の位置づけ / KM1's status

KM1 は個人が作ったデザイン標準で、どの企業・団体とも関係がなく、作成・承認・推奨も受けていない。文書に出てくる名前は、素材の出典と、従っている規格を示すためだけに使う。
*KM1 is a personal design standard, unaffiliated with and not created, approved or endorsed by any company or organization. Names appear only to credit material and cite standards.*

**KM1 のライセンス / KM1's license:** KM1（コード・文書・アイコンの絵・PDF・Office のひな形）は MIT License で公開する。著作権表示と全文はリポジトリの `LICENSE`（名前はそこにだけ書く）。第三者の素材は、それぞれの条件に従う（3 章）。
*KM1 (code, docs, icon drawings, PDFs, Office templates) is MIT-licensed; the notice and full text are in `LICENSE`, the only place the name appears. Third-party material keeps its own terms (section 3).*

## 2. 外に配るときの固定の文言 / Fixed wording for shared material

PDF の奥付、Office のひな形、素材集の README などに、必要な分をそのまま入れる。
*Paste what applies into a PDF colophon, Office template, asset-pack README and so on.*

### 2.1 位置づけ（外に配るものすべて）/ Status (everything shared)

> KM1 は個人が作ったデザイン標準です。どの企業・団体が作成・承認・推奨したものでもありません。製品名と商標は、それぞれの持ち主のものです。
> *KM1 is a personal design standard, not created, approved or endorsed by any company or organization. Product names and trademarks belong to their owners.*

### 2.2 アイコン（KM1 のアイコンを含むもの）/ Icons

> KM1 のアイコンは、Fluent System Icons（Microsoft、MIT License）をもとに描き直したものです。Copyright (c) 2020 Microsoft Corporation. ライセンスの全文は https://github.com/microsoft/fluentui-system-icons の LICENSE を参照してください。
> *KM1 icons are redrawn from Fluent System Icons (Microsoft, MIT License). Copyright (c) 2020 Microsoft Corporation. See the LICENSE in https://github.com/microsoft/fluentui-system-icons for the full text.*

素材集（SVG・PNG）を配るときは、LICENSE の全文を同梱する。MIT は、複製や大部分の使用に著作権表示と許諾文を付けることを条件にしている。著作権表示の年は原文で確かめて転記する。
*When shipping the SVG/PNG pack, include the full LICENSE text. MIT requires the copyright and permission notice with copies or substantial portions; copy the exact year from the original.*

### 2.3 書体 / Typefaces

> 本文の書体は Noto Sans JP・Noto Sans CJK JP（SIL Open Font License 1.1）。
> *Body type is Noto Sans JP / Noto Sans CJK JP (SIL Open Font License 1.1).*

フォントのファイルを配るとき(Flutter アプリへの同梱、自前配信)は、配布元の `OFL.txt` を同梱する。PDF への埋め込みは OFL で認められている。
*Ship the font's own `OFL.txt` when distributing font files (Flutter bundle, self-hosting). Embedding in PDFs is permitted by the OFL.*

### 2.4 作成者の表記 / Author line

既定は「KM1 作成者」。実名を書くかどうかは持ち主が決める。「PDF」の 7 章は、外に配る PDF に個人名を残さない決まりなので、実名を書くなら、その決まりとの食い違いを先に直す。
*The default is "KM1 author". Whether to print a real name is the owner's call; `documents.md` ch. 7 keeps personal names out of shared PDFs, so resolve that conflict first.*

### 2.5 KM1 のライセンス / KM1 license

> KM1 は MIT License で公開しています。ライセンスの全文と著作権表示は https://github.com/kami2news/km1-design-system の LICENSE を参照してください。
> *KM1 is released under the MIT License. See the LICENSE in https://github.com/kami2news/km1-design-system for the full text and copyright notice.*

PDF と Office のひな形にはこの文だけを載せ、個人名は書かない（「PDF」の 7 章）。名前は `LICENSE` の著作権表示にだけ書く。コードや素材集を配るときは `LICENSE` の全文を同梱する。
*PDFs and Office templates carry only this line, no personal name (documents.md §7); the name appears only in the `LICENSE` notice. Ship the full `LICENSE` with code and asset packs.*

## 3. 使っている素材と参考 / Material used and referenced

確認の状態: **済**（公式のページで確認）、**一般**（広く知られる条件で、配る前に原文で確認する）、**要確認**（条件を読んでいない）。
*Status: confirmed, general (verify before distributing), to verify.*

| 出典 / Source | 権利者と条件 / Owner and terms | KM1 の使い方 / How KM1 uses it | 配るときの表記 / Notice | 状態 |
| Fluent 2（原則・トークンの構造・部品の作法）| Microsoft。Fluent UI のコードは MIT。デザイン文書の利用条件は読んでいない | 構造と、公開されているトークンの値を土台にした | 2.1。取り込んだコードの有無は未確認 | 要確認 |
| Fluent System Icons | Microsoft、MIT | 原図をもとに KM1 のアイコンを描き直した | 2.2 | 一般 |
| Noto Sans JP・Noto Sans CJK JP・Noto Sans Mono CJK JP | SIL OFL 1.1 | Web は Google Fonts から読み込み、PDF に埋め込み、Flutter に同梱 | 2.3 | 一般 |
| Hind | SIL OFL 1.1（Indian Type Foundry） | 英語の書体の候補 | 2.3 | 一般 |
| Segoe UI・游ゴシック・Meiryo UI・ヒラギノ角ゴ | 各 OS・Office の書体 | 書体名を並びに書くだけ。ファイルは同梱も再配布もしない。Office 文書にも埋め込まない | 不要 | — |
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
| KM1 の PDF（本編・部品カタログ）| 奥付に 2.1・2.2・2.3・2.5。作成者は 2.4 |
| Office のひな形と見本（`.dotx`・`.potx`・`.docx`・`.pptx`）| 2.1 と 2.5。見本は最後のページかノートに。ひな形は本文に入れず、PowerPoint はノート、Word はファイルの説明に |
| アイコンの素材集（SVG・PNG）| 2.2、KM1 の `LICENSE` と `LICENSE-Fluent.txt` の全文 |
| Flutter のコード・パッケージ | README に 2.1・2.2、KM1 の `LICENSE` の全文。フォントを同梱するなら `OFL.txt`（2.3） |
| Web の部品（`bundle.js`・`bundle.css`）| README に 2.1、KM1 の `LICENSE` の全文。React を同梱するなら MIT の表記 |
| 外に見せる画面の写し | 他社のロゴ・商標をそのまま写さない |

## 5. 言葉の使い方 / Wording rules

- 他の組織の名前は「出典」「参考」の範囲で書く。「公式」「認定」「承認」「推奨」「提携」は、他の組織の名前と一緒に書かない。
  *Name other organizations only as sources or references; never with "official", "certified", "approved", "endorsed" or "partner".*
- 「Fluent 2 を土台にした」は「部品の振る舞いとトークンの構造・値を Fluent 2 から始めた」という意味でだけ使い、認定を受けたように読める文にしない。
  *"Built on Fluent 2" only means behaviour, token structure and values started from Fluent 2, never certification.*
- ロゴ・マーク・商標を画像として使わない。使う必要があるときは、各社の利用規約に従う。
  *No logos, marks or trademarks as images; if needed, follow each owner's terms.*
- 他の文章の引用は短く、出典を付ける。長い転記はしない。
  *Quote briefly with a source; no long transcriptions.*

## 6. 未確認 / Open items

- Fluent 2 のデザイン文書の利用条件。
- 作成者の表記（2.4）。

`bundle.js` に React と Fluent UI のコードが入っていないこと、アイコンの MIT の年（2020 年、`LICENSE-Fluent.txt`）は 2026-11-18 に確かめた。
*Open: Fluent 2 design-doc terms and the author line. Verified 2026-11-18: `bundle.js` bundles neither React nor Fluent UI code; the icon MIT year (2020) is from `LICENSE-Fluent.txt`.*
