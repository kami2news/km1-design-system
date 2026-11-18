# デザイン原則 / Design principles

Microsoft Fluent 2、Science Tokyo、EPSON の 3 つの考え方から、共通する部分を軸にして、食い違う部分は判断を決めた。公開されている説明から読み取った考え方であり、各社のガイドライン本体の転記ではない。
*Drawn from three sources (Microsoft Fluent 2, Science Tokyo, EPSON): the shared parts form the axes, and the parts that differ have a decision. These are readings of public descriptions, not copies of each company's guidelines.*

## 3 社に共通する 6 つの原則 / Six principles shared by all three

| 原則 | Microsoft Fluent 2 | Science Tokyo | EPSON |
| --- | --- | --- | --- |
| 1 人を中心に、迷わせない | Built for focus（流れを妨げない） | 情報にアクセスしやすい状態 | 分かりやすさ（FlipUI の「結果から選ぶ」） |
| 2 ノイズを減らす | 視覚的ノイズを減らす | 規定外のサイズを避ける | 画面は必要最小限の情報（FlipUI） |
| 3 全体で一貫する | Unmistakably Microsoft | ブランドから Web まで一つの体系 | 事業領域をまたぐ一貫したデザイン戦略 |
| 4 すべての人に | One for all, all for one | ウェブアクセシビリティ方針 | カラーユニバーサルデザイン（色だけに頼らない） |
| 5 個性は少しだけ | 少しの個性が印象を左右する | ブランドネイビー | ブランド色（青） |
| 6 長く使える | 利用者が既に知る体験を土台に | 段階的に改善を続ける | 長く使い続けられる体験 |

*Rows in English: (1) Put people first and never make them hesitate. (2) Reduce noise. (3) Stay consistent as a whole. (4) Design for everyone. (5) Add only a little personality. (6) Last long.*

### KM1 での適用 / Applied in KM1

**1 人を中心に、迷わせない / People first.** 1 画面にプライマリは原則 1 つ。ラベルは動詞で書く。本文は `body-1`（14px）以上、`ink` 系の文字は `surface` 系の上で 4.5:1 以上。
*One primary per screen by default; verb labels; body text at `body-1` (14px) or larger; `ink` text at 4.5:1 or more on `surface` tokens.*
- 1 つの `Card` は 1 つの作業にし、その作業に必要な情報だけを載せる（EPSON FlipUI） / *One `Card` = one task, with only the information that task needs (Epson FlipUI)*
- 設定は多数の項目を調整させず、求める結果（プリセット）から選ばせる。基本の設定は初期値として組み込む（EPSON FlipUI、Smart Panel） / *Let people pick the desired result (a preset) instead of tuning many settings; build basic settings in as defaults (Epson FlipUI, Smart Panel)*
- エラーは目立つアイコンで知らせる（EPSON Smart Panel。`Alert` に実装済み） / *Errors get a conspicuous icon (Epson Smart Panel; already in `Alert`)*

**2 ノイズを減らす / Reduce noise.** 操作の枠（ナビ、ツールバー、装飾）は最小に、利用者の内容と作業領域を最大にする。グラデーション・ガラス効果・過剰な影は使わず、中立の面にブランド色を 1 色だけ差す。規定外の文字サイズ・余白は使わない。余白は詰めすぎない（`space-lg` 以上を基本）。
*Minimal chrome, maximal content. No gradients, glass or heavy shadows; one brand color on neutral surfaces. No sizes or spacing outside the defined set; do not squeeze spacing (`space-lg` or more by default).*

**3 全体で一貫する / Consistency.** 値は意味づけトークンだけを参照し、原色（`gray-*`、`brand-*` など）は直接使わない。同じ部品は画面が変わっても同じ形・位置・挙動にし、違いは `appearance` で切り替える。状態（hover / pressed / focus / disabled）を全部品で定義する。
*Reference semantic tokens only; never use primitives directly. The same part keeps the same shape, place and behavior; differences are switched by `appearance`. Define all states on every part.*

**4 すべての人に / For everyone.** アクセシビリティを全コンポーネントの必須条件にする。
*Accessibility is a requirement of every component:*
- 見出しの順序を飛ばさない（`Card` は `headingLevel` で調整） / *keep heading order (`Card` uses `headingLevel`)*
- コントラスト（文字 4.5:1、操作要素の境界とフォーカスリング 3:1） / *contrast: 4.5:1 text; 3:1 control borders and focus ring*
- 色だけで伝えない（`Alert` はアイコンと文言、`Link` は下線、`Checkbox` はチェック記号） / *never color alone (`Alert` icon + word, `Link` underline, `Checkbox` tick)*
- リンクは行き先が分かるラベル（「こちら」を避ける） / *descriptive link labels*
- 画像には代替テキスト、装飾画像は空の alt / *alt text; empty alt for decorative images*
- キーボードだけで操作でき、フォーカスが見える / *keyboard operable, visible focus*
- 表は見出しセル、リストは本物のリスト要素 / *header cells in tables, real list elements*
- `prefers-reduced-motion` と強制カラーモード（`forced-colors`）に対応する / *support reduced motion and forced colors*
- 書体は `lang` で切り替える（`ja` は Noto Sans JP、`en` は Segoe UI → Hind） / *fonts switch by `lang`*

**5 個性は少しだけ / A little personality.** 個性はメインカラー（`brand`、EPSON の青を参考にした紺）のアクセントだけにする。測れない「小さなディテール」は設けない。
*Personality is the main-color accent (`brand`, a navy inspired by Epson's blue) only. No unmeasurable "small detail".*

**6 長く使える / Built to last.** 標準のコンポーネントの挙動（キーボード、フォーカス、ラベルの位置）には利用者が既に知っている形を使う。流行を追わず、改良は tokens.json と本文を更新して積み上げる。
*Use the familiar behavior of standard components (keyboard, focus, label position). Do not chase trends; improve by updating tokens.json and this text.*

## 食い違う点と KM1 の判断 / Where they differ, and KM1's call

| 食い違い | KM1 の判断 |
| --- | --- |
| Fluent「プラットフォーム標準を約 8 割再利用」と、Science Tokyo・EPSON の「独自の一貫性」 | 操作の挙動は標準に従い、個性は色・書体・余白の使い方だけで出す |
| 簡潔さと、説明を足すアクセシビリティ | アクセシビリティを優先し、その上で最小限に近づける |
| 書体: Fluent の Segoe UI と、Science Tokyo の Noto Sans JP | `lang` で切り替える |
| ブランド色: Fluent の青、Science Tokyo のネイビー、EPSON の青 | EPSON の青を参考にした紺 `#10218B`（KM1 のメインカラー） |
| 操作領域: デジタル庁は Small ボタンでも 44px を確保、Fluent 2 は 32px が標準 | 端末で切り替える。スマホは small も含めて 44px（デジタル庁）、PC は 32px・small 24px（Fluent 2、WCAG の AA を満たす） |

*Conflicts: (1) Fluent's reuse of platform patterns versus the others' own consistency: follow standard behavior, express personality only through color, type and spacing. (2) Minimalism versus accessibility: accessibility wins. (3) Typeface: switch by `lang`. (4) Brand color: `#10218B`, a navy inspired by Epson's blue (KM1's main color).*

判断の基準：実装できる規則（値、条件、検査できる手順）になるものだけ採用し、ふんわりしたものは、Fluent と Science Tokyo の規則に従う。
*Rule: adopt only what becomes an implementable rule (a value, a condition, a checkable step). Vague ideas fall back to the rules already set by Fluent and Science Tokyo.*

## 実際に実装に使った情報 / What is actually used

| 出典 | 実装に使ったもの |
| --- | --- |
| Microsoft Fluent 2 | トークンの構造、コンポーネントの挙動、状態の定義、余白 4px 刻み |
| Fluent System Icons（Microsoft、MIT） | アイコン（Material 系は混ぜない） |
| Science Tokyo | アクセシビリティの条件（コントラスト、見出し順、色だけで伝えない、キーボード操作）、Noto Sans JP |
| EPSON | メインカラーの参考（`#10218B` は EPSON の青を参考にした色）。FlipUI の「1 カード 1 作業」「結果から選ぶ」、Smart Panel の初期値の組み込み、色だけで伝えない |
| デジタル庁デザインシステム（β v2.18.2） | 部品の使い方：ボタンの使い分けと配置、無効化の扱い、補足とエラーの位置、必須表示、選択肢の数と Radio/Select の使い分け、通知の閉じ方 |
| ISO 9241-210:2019（人間中心設計） | プロダクトデザインの 4 つの活動の順番。本文は未読で、公開の目次と解説から確認 |
| Jakob Nielsen の応答時間の 3 つの目安（0.1・1・10 秒） | 待ち時間の表示の区切り（10 秒以上は工程と時間の見込み） |
| Jakob Nielsen の 10 のユーザビリティ原則（Nielsen Norman Group） | 作ったものを点検する 10 項目（KM1 の部品に当てはめて書き直した） |
| Android・Apple HIG・Windows の公式資料 | 端末ごとの操作領域（Android 48dp、iOS 44pt、Windows のタッチ 44epx）と作法（「プラットフォーム」セクション） |
| WCAG 2.2 | 操作領域（スマホ 44px = AAA 2.5.5、PC 32px = AA 2.5.8 を満たす） |
| W3C ARIA Authoring Practices Guide | Tabs・Dialog などの操作とキーボード挙動 |

*Fluent 2: token structure, component behavior, states, 4px spacing. Fluent System Icons: icons. Science Tokyo: accessibility conditions and Noto Sans JP. EPSON: reference for the main color, and FlipUI/Smart Panel rules. Digital Agency design system: how components are used (button roles and placement, disabling, hint/error position, required marks, Radio vs Select, dismissing notices). WCAG 2.2: hit areas. W3C APG: widget behavior.*

## 情報源の確度 / Source reliability

| 対象 | 確認できたこと | 確認できていないこと |
| --- | --- | --- |
| EPSON | FlipUI・Smart Panel・ユニバーサルデザインの各公式ページ。いずれも数値の基準は掲載なし。「省・小・精」の各文字の定義は公式にはない | —（メインカラーは参考にした色なので、原典の確認は要らない） |
| デジタル庁デザインシステム | 部品の概要・使い方・アクセシビリティの各公式ページ（Button、Select、Radio、Checkbox、通知バナー）。Button の寸法（Large 56px、Medium 48px、Small 36px、X-Small 28px）は例示画像の記載で、Small と X-Small も 44px の操作領域を確保する決まり。Textarea、Header、Drawer などは読んでいない | 色・書体・余白などの基本デザインのページ、リンクテキスト、フォーカス表示（Button のページに規定なし） |
| Science Tokyo | デザイントークン（色・書体・余白・角丸）のページ | 文字サイズ・行間・余白の表と影（画像のため読み取れなかった） |

*Digital Agency DS: official overview/usage/accessibility pages for Button, Select, Radio, Checkbox and Notification Banner; button sizes come from example images; Small and X-Small must still keep a 44px target. Textarea, Header, Drawer, etc. and the foundation pages are not read. EPSON: official FlipUI, Smart Panel and universal design pages; none gives numeric standards; Epson does not define each character of 省・小・精. Not confirmed: the logo guideline original. Science Tokyo: design token pages; the type-size, spacing and elevation tables are in images and could not be read.*

**メインカラー `#10218B` について / About the main color `#10218B`:** EPSON の青を参考にして選んだ紺で、KM1 のメインカラー（`brand`）として使う。EPSON の指定色や公式の UI 色として扱うものではなく、色の値は KM1 が決めたもの。値を変えるときは `tokens.json` を直し、コントラスト（白地で 4.5:1 以上）を確かめる。
*A navy chosen with Epson's blue as a reference and used as KM1's main color (`brand`). It is not an Epson-specified or official UI color; the value is KM1's own. To change it, edit `tokens.json` and recheck contrast (4.5:1 or more on white).*

## 初代 Material Design（M1）から取り込んだもの / What KM1 takes from M1

M1（2014〜2017、m1.material.io）からは「用途と目的がはっきりした UI」の考え方だけを取り込む: 1 つの部品は 1 つの目的、主操作が面の大半、識別は左・補助は右、状態は形と言葉でも示す、身ぶりは近道だけ。見た目（Roboto、紙の影、Ripple、FAB、色）は取り込まない。M2・M3 とは混ぜない。詳しくは「KM1 × M1」。
*From M1 KM1 takes only the purpose-clear principles (one purpose per component, primary action fills the surface, identity at start and secondary at end, states shown by shape and words, gestures as shortcuts). Not its look. Details in "KM1 × M1".*

## 取り込んでいないもの / Not adopted

各社の色（Science Tokyo の配色など）、ロゴ、形状。ブランド色はメインカラー `#10218B`（EPSON の青を参考にした紺）1 色。
*Other companies' colors (e.g. Science Tokyo's palette), logos and shapes are not adopted. The brand color is the single main color `#10218B` (inspired by Epson's blue).*

## 出典 / Sources

- Microsoft Fluent 2: fluent2.microsoft.design（Design principles ほか）
- Science Tokyo デザインシステム: design-system.isct.ac.jp（デザイントークン、ウェブアクセシビリティ）
- EPSON: corporate.epson/ja/technology/design/works/works-flip-ui.html、works-smart-panel.html、corporate.epson/ja/sustainability/customer-commitment/universal-design.html、corporate.epson/ja/news/2026/260519.html
- デジタル庁デザインシステム: design.digital.go.jp/dads/components/（button、select、radio、checkbox、notification-banner の概要・usage・accessibility）
- Fluent System Icons: github.com/microsoft/fluentui-system-icons（MIT）
- WCAG 2.2: w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- W3C ARIA Authoring Practices Guide: w3.org/WAI/ARIA/apg/
