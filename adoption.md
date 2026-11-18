# 適用記録 / Adoption log

KM1-ADO-001。KM1 を製品に適用した記録と、見つかった不足を、KM1 の判断に戻すための台帳。標準が机の上で終わらないようにする。`product.md` 6 章「KM1 に戻す」の実行場所。
*KM1-ADO-001. A ledger of where KM1 is applied and the gaps found, feeding them back into KM1's decisions, so the standard does not stay on paper. It is where `product.md` ch. 6 is carried out.*

## 1. 流れ / Flow

1. **適用する:** 製品に KM1 を当てる。範囲（色だけ・全面）と、そのときの KM1 の版（`KM1 YYYY-MM-DD`）を 2 章の台帳に 1 行書く。
2. **不足を書く:** KM1 に足りないもの、曖昧な規則、合わない規則に出会ったら、すぐ 3 章に 1 行書く。製品側で先に作ってよい（`product.md` 6 章）。
3. **数える:** 同じ不足が **2 つ目の製品**でも出たら、KM1 に入れる合図。1 回きりのものは入れない。
4. **提案にする:** 合図が出た不足は、`proposals.md` か `governance.md` の判断記録に提案として書き、台帳の「判断」の欄に番号（P1・D11 など）を書く。
5. **戻す:** 決まったら KM1 を直し、変更履歴に書く。次に製品へ適用するとき、台帳の「状態」を更新する。

*Apply → log gaps as they appear → a gap seen in a second product is the signal → write it up as a proposal or decision → fix KM1 and record it → update the ledger.*

KM1 の決まりを破る必要が出たら、破る前に決まりのほうを直す。製品ごとの例外は作らない。
*If a rule must be broken, change the rule first; no per-product exceptions.*

## 2. 適用の台帳 / Adoption register

| 製品 | 種類 | 適用の範囲 | KM1 の版 | 最後に確かめた日 | 外した原則 | 備考 |
|---|---|---|---|---|---|---|
| スケジュール確認アプリ（`schedule-check`） | Flutter（Web・スマホ） | 最初は色だけ（ブランド色と、高さ・レイアウトは据え置き）。2026-11-14 に、色以外も KM1 に合わせる方向。2026-11-18 にアイコンを KM1 の 144 個の版に取り込み直し、意味と絵のずれ 6 か所と、大きさ 14・18px の 21 か所（16・20・24・32px へ）を直した | アイコン: 144 個の版（2026-11-18 の GitHub 版と同じ形） | 2026-11-18（アプリ側の自動テスト 173 件、広い画面とスマホ幅の画面写し） | 未記録 | 専用の入力部品を作って「下辺だけ強調」を補っている（G2）。KM1 に無いアイコン 5 つは Fluent のまま（A5〜A9）。部品の中の小さな印（チェックボックスの中のチェックなど）は大きさの決まりの対象外として残した |
| `kami2pos`（イベント向け POS） | Flutter Web | 全面適用の方針（テーマ・色・アイコン・部品の高さ・文言）。店舗ごとのテーマカラーは分類色として残す | 未記録 | 未実施 | 未記録 | 実装フェーズ。適用の状況はまだ記録していない |

「未記録」「未実施」は、記録をまだ取っていないという意味。適用のたびに埋める。
*"Unrecorded" and "not run" mean no record has been taken yet; fill in on each application.*

## 3. 不足の台帳 / Gap ledger

| # | 見つけた日 | 製品・場所 | 内容 | 種類 | 見た製品の数 | 状態 | 判断 |
|---|---|---|---|---|---|---|---|
| A1 | 2026-11-15 | KM1 の文書の点検（`coverage.md`） | Flutter の `Alert`・`Link` の対応が決まっていない | 部品の不足 | 0（文書上の不足。製品での確認は未実施） | 未判断 | `coverage.md` G1 |
| A2 | 2026-11-15 | KM1 の文書の点検 | Flutter の `Input` で「下辺だけ強調」を再現できない。スケジュール確認アプリは専用の部品で補った | 部品の不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | `coverage.md` G2 |
| A3 | 2026-11-15 | KM1 の文書の点検（`verification.md` 4 章） | 一覧・表が 500 行を超える画面（`kami2pos` の注文一覧など）で、選択の反応が遅れうる | 規則の限界 | 0（実測は headless Chrome のみ） | 未判断 | D8 |
| A4 | 2026-11-15 | KM1 の文書の点検 | 期間を選ぶ・階層を選ぶ・グラフを出す部品がない | 部品の不足 | 0 | 提案あり | P1・P2・P3（D11） |
| A5 | 2026-11-18 | `schedule-check`・予定の場所 | オンライン会議（動画）のアイコンがない。Fluent のまま | アイコンの不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | — |
| A6 | 2026-11-18 | `schedule-check`・設定 | 端末（PC とスマホ、「システムに合わせる」）のアイコンがない。Fluent のまま。KM1 の `phone` は電話（通話）の絵 | アイコンの不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | — |
| A7 | 2026-11-18 | `schedule-check`・To Do | 未完了の丸（タスクのチェックの丸）がない。Fluent のまま | アイコンの不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | — |
| A8 | 2026-11-18 | `schedule-check`・空き時間を探す | 「空き時間を探す」がない。いまは `clock`（時刻）で代用しており、時刻の欄と同じ絵になる | アイコンの不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | — |
| A9 | 2026-11-18 | `schedule-check`・繰り返し | 毎週以外の繰り返し（毎日・毎月など）がない。いまは `repeat-weekly` で代用 | アイコンの不足 | 1（`schedule-check`） | 2 つ目の製品での確認待ち | — |

種類: **部品の不足** / **アイコンの不足** / **規則の曖昧さ** / **規則の限界** / **製品側の都合**（KM1 に入れない）。
*Kinds: missing component / missing icon / ambiguous rule / rule limit / product-specific (stays out of KM1).*

この表の A1〜A4 は、製品を使って見つけたものではなく、KM1 の文書を点検して見つけたもの。製品での確認は、これから埋める。A5〜A9 は `schedule-check` のアイコンの点検（2026-11-18）で見つけたもの。
*A1–A4 come from reviewing KM1's documents, not from using a product; confirmation in products is still to be filled in. A5–A9 come from the schedule-check icon audit on 2026-11-18.*

## 4. 続け方 / Routine

- 製品に KM1 を当てた日、または製品で KM1 に無いものを作った日に、2〜3 章へ 1 行ずつ書く。5 分で済む量にする。
  *Add one line to chapters 2–3 on the day KM1 is applied or something KM1 lacks is built; five minutes' work.*
- 月に 1 度、3 章の「見た製品の数」が 2 以上で「未判断」のものを、`governance.md` の判断記録に出す。
  *Monthly, move gaps seen in two or more products and still "undecided" into the decision log.*
- 製品側の都合は、KM1 に入れずに「製品側の都合」として残し、理由を 1 行書く。
  *Product-specific items stay out of KM1 with a one-line reason.*
