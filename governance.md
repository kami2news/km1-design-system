# 運用の決まり / Governance

KM1 に何を入れ、何を入れないかを決める手続きと、変更・互換性・出典の扱い。判断を変えるときも、ここの手続きに従う。
*How KM1 decides what goes in, and how changes, compatibility and sources are handled—including reversing a decision.*

## 1. 判断の状態 / Decision states

| 状態 / State | 意味 / Meaning | 次に進む条件 / To move on |
|---|---|---|
| 提案 / Proposed | 案があるだけ | 目的・使う条件・既存との重複を書く |
| 保留 / On hold | 判断の材料が足りない | 足りない材料（比較・利用テスト・技術の制約）を書き、そろったら再検討 |
| 試行 / Trial | 条件つきで一部の画面だけに使う | 期間と、比べる指標を決める。終わったら採用か不採用 |
| 採用 / Adopted | 標準。部品・トークン・規則になっている | 変えるときは 3 章の手続き |
| 不採用 / Rejected | 理由を書いて入れない | 前提が変わったら「提案」から出し直す |
| 廃止予定 / Deprecated | まだ使えるが、次の版で外す | 代わりを書き、1 つの版のあいだは残す |

## 2. 判断の記録 / Decision log

| # | 対象 / Subject | 状態 | 日付 | 理由・条件 / Reason | 出典の章 |
|---|---|---|---|---|---|
| D1 | FAB（浮いた丸いボタン） | 不採用（2026-11-13 に再確認） | 2026-11-12 以前 | 内容と重なる・読む順と位置がずれる・アイコンだけでは意味が伝わらない。採るなら、今の配置と比べる利用テストを先にする | KM1 × M1 |
| D2 | Ripple（波紋） | 不採用 | 2026-11-12 以前 | 動かしてよいのは色・影・不透明度と 8px までの移動だけ。押した時は色の変化で伝える | 画面の組み立て › 動き |
| D3 | Carbon の Fluid スタイル・フォームの密度の切り替え | 不採用 | 2026-11-13 | 複雑なフォームに向かない。高さは入力方法で決まる | 画面の組み立て › フォーム |
| D4 | Card・Table・SortableList の密度 | 採用 | 2026-11-13 | コレクションとコンテナに限って余白だけを変える | トークン |
| D5 | ページ内のボタンの位置（Carbon の主ボタン左） | 不採用 | 2026-11-13 | KM1 の他の画面と揃える（PC は主ボタン右） | 画面の組み立て › フォーム |
| D6 | 動きのトークンを `tokens.json` に入れる | 保留 | 2026-11-13 | 保存の形式が動きの族を読まない。生成スクリプトの中に持つ案を検討。代案は D12（2026-11-15） | KM1 × M1 |
| D7 | Dialog・Drawer のボタンの並び（CSS で見た目だけ逆にする） | 廃止（直した） | 2026-11-13 | DOM の順＝見た目の順に統一。スマホでは DOM の順ごと入れ替える | 変更履歴 |
| D8 | 仮想スクロール（大量の行） | 提案 | 2026-11-13 | 2,000 行を超えると選択の反応が遅れる。当面は 500 行まで＋ページ送り | 検証 |
| D9 | 密度の spacious を Spectrum 2 と同じ「1 段上」にそろえるか | 保留 | 2026-11-13 | 今は依頼の値（2 段上）。持ち主の判断待ち | トークン |
| D10 | 書体（Noto Sans JP）の自前配信 | 提案 | 2026-11-15 | 外部配信に頼らず、オフライン・社内網でも同じ字形にする。ライセンス（OFL 1.1）と配信量の確認が先 | トークン 7 章 |
| D11 | 不足領域の仕様案（期間入力・ツリー・グラフ・連続色） | 提案 | 2026-11-15 | 部品にする前に、仕様だけ先に決める。使う画面が出てから試行へ | 仕様案 |
| D12 | 動きのトークンを `duration`・`easing` の族として `tokens.json` に入れる（D6 の代案） | 提案 | 2026-11-15 | 保存の形式は単一の値の族を読める。族の数（12 まで）の確認と試行が先 | 仕様案 P4 |
| D13 | メインカラー `#10218B` の扱い | 採用 | 2026-11-18 | EPSON の青を参考にして KM1 が選んだ色として書く。「EPSON ブルー」と断定せず、EPSON の指定色としても扱わない。原典の確認は要らない | デザイン原則 |

## 3. 判断を変える手続き / Changing a decision

1. **提案を書く:** 何を・なぜ変えるか、前の判断の理由のどれが変わったか。導入の記録（`adoption.md`）の穴 A1〜 から起こすときは、その番号を書く。
   *Write what changes and which earlier reason no longer holds.*
2. **影響を調べる:** 使っている部品と画面（`gen/tokens_check.py` の影響の表、`inventory.json`）、各 OS への影響。
   *Map the impact with the impact table and inventory.*
3. **比べる:** 今の形と新しい形を同じ画面で並べる見本を作る。操作に関わるものは利用テストか、少なくとも利用シナリオ（「検証」）で確かめる。
   *Compare side by side; for interaction changes, test with users or at least the scenarios.*
4. **決める:** 持ち主が決める。決めたら 2 章に記録し、変更履歴に書く。
   *The owner decides; record it here and in the changelog.*
5. **移す:** 互換性の規則（4 章）に従って、廃止予定の期間をおく。
   *Migrate per the compatibility rules.*

## 4. 互換性 / Compatibility

- **壊さない変更（いつでも可）:** 部品に任意の属性を足す、トークンを足す、文書を直す、見た目の不具合を直す。
  *Non-breaking: optional props, new tokens, doc fixes, visual bug fixes.*
- **壊す変更（廃止予定を経る）:** 属性やトークンの名前を変える・消す、既定の見た目を変える、DOM の構造を変えて利用側の CSS が効かなくなる。1 つの版で「廃止予定」と書き、次の版で外す。
  *Breaking changes (renaming/removing props or tokens, changing defaults or DOM) go through one edition as deprecated.*
- **確かめ方:** 既定の見た目は、全部の見本を変更の前後で画素ごとに比べる（動きは止める）。操作は利用シナリオと部品ごとの検査を流す。
  *Verify with before/after pixel comparison of all previews (animations frozen) plus scenario and component checks.*
- **版の名前:** `KM1 YYYY-MM-DD`（その日の最後の公開）。変更履歴の見出しと同じ。
  *Editions are named by date, matching changelog headings.*

## 5. 出典の扱い / Sources

| 出典 / Source | 状態 / Status | 扱い / How it is used |
|---|---|---|
| Fluent 2・Fluent System Icons | 確認済み（公式サイト・リポジトリ） | 基盤 |
| デジタル庁デザインシステム・WCAG 2.2・W3C APG | 確認済み | 規則の根拠 |
| Carbon・M1・Spectrum 2 | 確認済み（2026-11-13 に公式ページを参照） | 考え方だけを取り込む。見た目は取り込まない |
| EPSON の考え方 | 公開されている説明を参照 | デザイン原則の柱の 1 つ |
| メインカラー `#10218B` | 参考にした色（2026-11-18 に決定） | EPSON の青を参考にして KM1 が選んだ色として使う。EPSON の指定色とは書かず、原典の確認も要らない |
| Science Tokyo（ISCT） | 公開されている説明を参照 | デザイン原則の 3 つの柱の 1 つ（考え方の読み取り。ガイドラインの転記ではない） |

- 出典を足すときは、参照した日付と URL を本文の出典の欄に書く。原典を見ていないものは「未確認」と書き、根拠として使わない。
  *Record date and URL; mark unseen originals as unverified and don't rely on them.*

## 6. 保留と提案の期限 / Deadlines (KM1-GOV-002)

開いている判断（提案・保留・試行）には、次の確認日と「決まらないときの既定」を置く。放っておいても、既定の側に倒れるだけで、壊れない。確認は `gen/govcheck.py` で流す。日付は仮置きで、持ち主が変えてよい。
*Every open decision (proposed, on hold, trial) has a next review date and a default if nothing is decided. Dates are provisional; the owner may change them. Run `gen/govcheck.py`.*

| 判断 | 状態 | 次の確認日 | 担当 | 決まらないときの既定 | 決める条件 |
|---|---|---|---|---|---|
| D6 | 保留 | 2026-11-22 | 持ち主 | D12 に統合して閉じる | D12 の試行が先に進むなら不要 |
| D9 | 保留 | 2026-11-22 | 持ち主 | 今の値（2 段上）を続ける | Spectrum 2 との揃えを優先するなら変える |
| D12 | 提案 | 2026-11-30 | 持ち主 | `bundle.css` に持ったままにする | 族の数が 12 以内で、1 画面で試して問題がない |
| D10 | 提案 | 2026-12-06 | 持ち主 | Google Fonts のままにする | OFL の表記と配信量が確認でき、検査 `fontcheck` が通る |
| D11 | 提案 | 2026-12-13 | 持ち主 | 仕様案のままにする | 使う画面が 1 つ出る |
| D8 | 提案 | 2026-12-15 | 持ち主 | 500 行の規則を続ける | 導入の記録で 300 行超の画面が 2 つ出る |
