# 変更の進め方 / Contributing

KM1 は個人が管理するデザイン標準です。変更の決め方（提案・保留・期限）は `governance.md`、変更の記録は `changelog.md`。
*KM1 is a personally maintained design standard. Decision rules live in `governance.md`, the record in `changelog.md`.*

## 1. 変更するとき / Making a change

1. `main` から枝（branch）を作り、pull request で `main` に入れる。`main` に直接 push しない。
   *Branch from `main` and merge through a pull request; never push to `main` directly.*
2. トークンを変えるときは `tokens.json`（正本）だけを直し、生成物は道具で作り直す: `python3 gen/tokens_css.py`、`gen/km1_dart.py`、`gen/native.py`、`gen/tokens_dtcg.py`。生成物を手で直さない。
   *Edit only `tokens.json`; regenerate every derived file with the scripts.*
3. 部品を変えたら、その部品の `README.md` と `changelog.md` を同じ pull request で直す。部品や画面を足す・変えるときは、`governance.md` 7 章の「理由の確認」を通し、`README.md` に「**理由 / Why:**」の行を書く。
4. `bash gen/check_all.sh` が通ること。CI（`.github/workflows/check.yml`）も同じものと Flutter の解析・テストを流す。
   *`bash gen/check_all.sh` must pass; CI runs the same plus Flutter analyze and tests.*
5. Flutter の画像が変わる変更は、`verification.md` 6 章の手順で承認済みの画像を作り直して同じ pull request に入れる。
   Flutter の版は `.github/workflows/check.yml` と `goldens.yml` で固定している。上げるときは 2 つを一緒に変え、画像を作り直す。「Flutter 最新の stable（参考）」のジョブが落ちたら、版を上げる前に直す。
   *Flutter is pinned in both workflows; bump them together and regenerate goldens. The advisory latest-stable job warns early.*
6. 公開リポジトリなので、個人の氏名・勤め先・メールアドレスを書かない。見本の名前は架空にする。
   *Public repository: no personal names, employers or e-mail addresses.*

## 2. 公開（リリース）/ Releasing

1. `changelog.md` に `## YYYY-MM-DD — 題名` の節を書く。
2. `KM1_DATE=YYYY-MM-DD python3 gen/build_pdf.py dist` で PDF を作り直し、`office/` の道具でひな形を作り直す（`office.md` §5）。
3. `bash gen/check_all.sh` が通ることを確かめて `main` に入れる。
4. タグを付ける: `git tag -a km1-YYYY-MM-DD -m "KM1 YYYY-MM-DD" && git push origin km1-YYYY-MM-DD`。付けたタグは動かさない。同じ日の 2 回目は `km1-YYYY-MM-DD.2`。
5. GitHub の Release をそのタグで作る: 本文は変更履歴のその日の節、添付は `dist/` の PDF 2 冊・`.potx`・`.dotx`・`KM1_表示バッジ.pptx`・`KM1_icons.zip`・`KM1_グラフの模様.zip`・`dist/tokens/*.json`。
   `gh release create km1-YYYY-MM-DD dist/*.pdf dist/*.potx dist/*.dotx dist/KM1_表示バッジ.pptx dist/*.zip dist/tokens/*.json --title "KM1 YYYY-MM-DD" --notes-file <その日の節>`
   *Tag `km1-YYYY-MM-DD` (immutable), then create a GitHub Release with the changelog section and the `dist/` files.*

## 3. 対応の段階 / Support levels

各プラットフォームの状態（安定〔パイロット〕・パイロット・実験的）は `platforms.md` の表。実験的なもの（WinUI・Compose・SwiftUI）は、実機での確認（`verification.md`）が済むまで製品に使わない。
*Platform status (stable-pilot, pilot, experimental) is in `platforms.md`; experimental targets stay out of products until verified.*
