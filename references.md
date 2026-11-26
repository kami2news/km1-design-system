# 参考文献 / References

KM1 の決まりの根拠と、参考にした資料の一覧。各章の出典は、ここの節を指す。KM1 の決まりは、どれもそれ自体の理由で書いてあり、ここの資料は理由を確かめるための根拠として使う。参照日は、書いていないものは 2026-11 に確かめた。
*Everything KM1's rules rest on or drew from. Each chapter's sources point here. KM1's rules carry their own reasons; these are for checking them. Accessed November 2026 unless noted.*

## 1. 土台とライセンス / Base and licenses

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| [Fluent 2 Design System](https://fluent2.microsoft.design/)（Microsoft） | 部品の振る舞い・状態・トークンの構造と値の出発点 | 原則 4、基礎 |
| [Fluent System Icons](https://github.com/microsoft/fluentui-system-icons)（Microsoft、MIT） | KM1 のアイコンのもとの絵。配るときは MIT の表記を付ける | アイコン、表記とライセンス |
| [Noto Sans JP・Noto Sans CJK JP](https://fonts.google.com/noto/specimen/Noto+Sans+JP)（SIL OFL 1.1） | 日本語の書体。Web で読み込み、PDF に埋め込み、Flutter に同梱 | 基礎 3.4、表記とライセンス |
| [Hind](https://fonts.google.com/specimen/Hind)（SIL OFL 1.1） | 英語の書体の候補 | 基礎 3.4 |

## 2. アクセシビリティの規格 / Accessibility standards

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | コントラスト、押せる大きさ（2.5.5・2.5.8）、リフロー（1.4.10）、文字の間隔（1.4.12）、フォーカス | 原則 1・5、基礎、検証 |
| [W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Tabs・Dialog・Menu などのキーボード操作と役割 | 原則 5、部品 |
| [W3C WAI Forms Tutorial: Grouping](https://www.w3.org/WAI/tutorials/forms/grouping/) | フォームのまとまり（fieldset と legend） | 画面の組み立て › フォーム |
| [W3C WCAG 2.2 Techniques H71](https://www.w3.org/WAI/WCAG22/Techniques/html/H71) | まとまりの見出し（PDF・HTML） | PDF |

## 3. 使いやすさと設計の進め方 / Usability and process

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| ISO 9241-210:2019 "Human-centred design for interactive systems" | 4 つの活動（7.2〜7.5）の順番だけ。本文は読んでおらず、公開の目次と解説から確認 | プロダクトデザイン |
| [Jakob Nielsen: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)（Nielsen Norman Group） | 作ったものを点検する 10 項目。趣旨を KM1 の言葉で書き直した | プロダクトデザイン |
| [Jakob Nielsen: Response Times, the 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) | 待ち時間の区切り（0.1・1・10 秒） | 画面の組み立て › 待ち時間 |

## 4. プラットフォーム / Platforms

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| [Android Developers: Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps) | 操作領域 48 × 48dp | プラットフォーム |
| [Apple: Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | 操作領域 44 × 44pt、iOS・iPadOS の作法 | プラットフォーム |
| [Microsoft Learn: Guidelines for touch targets](https://learn.microsoft.com/windows/apps/design/input/guidelines-for-targeting) | Windows のタッチの操作領域 44 × 44 epx | プラットフォーム |
| [Android Developers: Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) | アプリアイコンの欠けない範囲（108dp の中の 66dp） | アイコン 6 |
| [MDN: Define your app icons](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons) | maskable のアイコンの安全な円（80%） | アイコン 6 |

端末ごとの作法（戻る、安全領域、iPad の分割表示など）は、各社の公式資料の一般的な決まりを KM1 の言葉でまとめたもので、細部は実機で確かめていない。
*Per-platform conventions summarize each vendor's general guidance; details are not verified on devices.*

## 5. 考え方を参考にしたデザインシステム / Design systems consulted

見た目・コード・文章は取り込んでいない。KM1 の決まりにするときは、理由を KM1 の言葉で書き直した。
*Ideas only; no look, code or text was taken. Rules were restated with KM1's own reasons.*

| 文献 / Source | 参考にした考え方 / Idea | 章 |
|---|---|---|
| [IBM Carbon: Forms](https://carbondesignsystem.com/patterns/forms-pattern/)・[Fluid styles](https://carbondesignsystem.com/patterns/fluid-styles/) | フォームの 1 列・確かめる時機・グループの間隔。Fluid の形は採らない | 画面の組み立て › フォーム |
| [GOV.UK: Error summary](https://design-system.service.gov.uk/components/error-summary/) | 送信後の誤りの一覧と、各欄へのリンク | 画面の組み立て › フォーム |
| Adobe Spectrum: [Design tokens](https://spectrum.adobe.com/page/design-tokens)・[Spacing](https://spectrum.adobe.com/page/spacing)・[Layout spacing](https://spectrum.adobe.com/foundations/layout-and-structure/spacing/layout-spacing)・[Component spacing](https://spectrum.adobe.com/foundations/layout-and-structure/spacing/component-spacing)（2026-11-13 参照） | トークンの三段、余白をレイアウトと部品に分ける、密度は並ぶものと入れ物だけ | 基礎 1・4・7 |
| Material Design 1（m1.material.io）: [Lists](https://m1.material.io/components/lists.html)・[Lists: Controls](https://m1.material.io/components/lists-controls.html)・[Expansion panels](https://m1.material.io/components/expansion-panels.html)・[Steppers](https://m1.material.io/components/steppers.html)・[Bottom sheets](https://m1.material.io/components/bottom-sheets.html)・[Grid lists](https://m1.material.io/components/grid-lists.html)・[Subheaders](https://m1.material.io/components/subheaders.html)・[Selection](https://m1.material.io/patterns/selection.html)・[Toolbars](https://m1.material.io/components/toolbars.html)・[Data tables](https://m1.material.io/components/data-tables.html)・[Bottom navigation](https://m1.material.io/components/bottom-navigation.html)・[Cards](https://m1.material.io/components/cards.html)・[FAB](https://m1.material.io/components/buttons-floating-action-button.html)・[Offline states](https://m1.material.io/patterns/offline-states.html)・[Permissions](https://m1.material.io/patterns/permissions.html)（2026-11-13 参照） | 「用途と目的がはっきりした UI」（1 部品 1 目的、識別は左・補助は右）。見た目は採らない | 記録（KM1 × M1） |

## 6. PDF / PDF documents

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| [PDF Association: ISO 14289-2（PDF/UA-2）](https://pdfa.org/iso-14289-2-pdf-ua-2-the-gold-standard-for-accessibility-in-pdf-2-0-has-arrived/) | タグつき PDF の決まり | PDF |
| [Matterhorn Protocol 1.02](https://pdfa.org/download-area/accessibility/MatterhornProtocol_1-02.pdf) | PDF のアクセシビリティの検査項目 | PDF 9 |
| [axes4: Matterhorn Protocol と PAC](https://support.axes4.com/hc/en-us/articles/7371943734930) | 手元での検査（PAC） | PDF 9 |

## 7. スライドと Word / Slides and Word

| 文献 / Source | 使っているところ / Used for | 章 |
|---|---|---|
| [Penn State: Assertion–Evidence の研究](https://writing.engr.psu.edu/research.html)・[Alley ほか: Assertion–Evidence Slides Instruction Set](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/7/13153/files/2008/10/Assertion-Evidence-Slides-Instruction_Set.pdf) | 見出しを主張の 1 文にし、本文を図で示す形 | Word と PowerPoint 4.7 |
| [東北大学: 発表資料チェックリスト](https://web.tohoku.ac.jp/yusa/wp-content/uploads/2026/03/checklist_presen_0204.docx) | 研究発表の中身の順番と点検 | Word と PowerPoint 4.7 |
| [NYC MOPD: Accessible Slidedecks Guide](https://www.nyc.gov/site/mopd/publications/guides/accessible-slidedecks-guide.page)・[Indiana University: PowerPoint](https://accessibility.iu.edu/creating-content/documents/powerpoint/index.html)・[ウェールズ政府: アクセシブルな PowerPoint](https://www.gov.wales/node/30039) | 投影する文字は 24pt 以上 | Word と PowerPoint 4.1 |
| Microsoft サポート: [PowerPoint をアクセシビリティ対応にする](https://support.microsoft.com/ja-jp/Accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities)・[アクセシビリティ チェックのルール](https://support.microsoft.com/ja-jp/Accessibility/office-accessibility/rules-for-the-accessibility-checker)・[閲覧順序ウィンドウ](https://support.microsoft.com/ja-jp/powerpoint/make-slides-easier-to-read-by-using-the-reading-order-pane) | Office の道具の使い方（読み上げの順番、代替テキスト、検査） | Word と PowerPoint 6 |

## 8. 道具 / Tools

| 文献 / Source | 使っているところ / Used for |
|---|---|
| [axe-core](https://github.com/dequelabs/axe-core)（Deque、MPL-2.0） | Web の自動検査。配布物には含めない |
| [React](https://react.dev/)（Meta、MIT） | Web の部品の実行。`bundle.js` には同梱しない |
