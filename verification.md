# 検証の手順と記録 / Verification

KM1 の検証は「自動の検査（ここで実施）」と「実機・読み上げ・各 OS のビルド（手元の環境で実施）」に分かれる。自動の検査に合格しても、人が快適に使えることの確認にはならない。この章は、手元で行う検証の手順と、結果の記録欄。
*Automated checks run here; devices, screen readers and native builds must run locally. Passing automated checks does not prove comfortable use. This chapter holds the local procedures and the results log.*

## 1. 記録 / Results log

状態: **済**（合格）・**不合格**（課題を書く）・**未実施**。日付と、使った端末・OS・ソフトの版を書く。
*Status: done / failed (note the issue) / not run, with date and versions.*

| # | 対象 / Target | 内容 / What | 状態 | 日付・環境 | 課題 |
|---|---|---|---|---|---|
| W1 | Web（headless Chrome） | 部品の自動検査（axe、WCAG 2.2 A・AA の規則）・キーボード・320px・再発防止（自分で id を作る部品すべてを 2 つ置く、SortableList の Esc を含む）・利用シナリオ 3 つ・大量データ | 済 | 2026-11-18・Chrome（`gen/web_test.js`。clone から `bash gen/check_all.sh` で再現でき、GitHub の CI でも push のたびに流す） | axe 134 ページ・キーボード 67・320px 63（説明用の図 4 つは対象外）・再発防止 9（2026-11-19 に 4 つ追加。前の版の bundle.js では 3 つ不合格になることを確かめた）・シナリオ 42 項目、すべて合格。大量データは下の 4 章（2026-11-13） |
| W2 | Web（実際のブラウザ） | 利用シナリオ 3 つを Chrome・Edge・Safari・Firefox で | 未実施 | | |
| N1 | Windows | NVDA とナレーターで利用シナリオ 3 つ | 未実施 | | |
| N2 | Windows | WinUI 3 のビルドと表示（`KM1.xaml`） | 未実施 | | |
| M1 | macOS | VoiceOver で利用シナリオ、SwiftUI の表示 | 未実施 | | |
| I1 | iOS・iPadOS | VoiceOver、Dynamic Type、Safe Area | 未実施 | | |
| A1 | Android | TalkBack、戻るジェスチャー、Compose のビルド | 未実施 | | |
| F1 | Flutter（CI） | `flutter analyze`（エラー・警告で失敗）と `flutter test`（ギャラリーをスマホ 390・PC 1280 の幅、ライト・ダークで組み立て、例外とはみ出しがないか） | 済 | 2026-11-18・GitHub Actions の ubuntu-24.04・Flutter stable（`.github/workflows/check.yml`。push のたびに流す） | 情報（material.dart の非推奨）は失敗にしない。アイコンの一覧の画像比較は、承認済みの画像を入れるまで飛ばす（F2） |
| F2 | Flutter の画像比較 | アイコンの一覧 6 枚（と 2026-11-19 からギャラリー 4 枚: スマホ・PC × ライト・ダーク）を承認済みの画像と比べ、違えば CI を失敗にする | 済 | 2026-11-19・GitHub Actions の ubuntu-24.04・Flutter stable。goldens ワークフローで作り、6 枚を目で確認して登録（144 個の線と塗り、ライトとダーク、16・20・24px） | それまで CI が `--update-goldens` で毎回作り直しており違いを見逃していたのを、比べる形に直した。最初の候補では、テストで KM1Icons の書体が読み込まれず塗りのアイコンが □ になっていたので直した。画像には画面の背景色を入れる（透明だとダークの見え方を見誤る） |
| F3 | Flutter（実機） | Android・iOS・Windows・macOS でのビルドと実際の画面 | 未実施 | | |
| T1 | 書体 / Typefaces | Office（Windows・Mac）、iOS・Android・Windows の画面で、文字がゴシック体で描かれるか（明朝・セリフ体に落ちていないか）。日本語・英語・数字・記号（①・℃・〜）の混じった文で見る。手順は 5 章 | 未実施 | | 自動の検査（`fontcheck.py`・`fontcheck_render.js`）は 2026-11-14 に合格 |
| C1 | 文書の整合 / Docs consistency | `gen/sync_counts.py --check`（部品数・対応表の食い違い）と `gen/govcheck.py`（保留・提案の期限）を一緒に流す | 済 | 2026-11-18・`gen/check_all.sh` の中で流す（CI も同じ） | 2026-11-15 に追加。変更のたびに流す |

## 2. 利用シナリオ / Scenarios

部品を組み合わせた 3 つの画面（見本「画面の例」）で、最初から最後まで操作する。Web ではスクリプトで自動化済み（W1）。実機と読み上げソフトでは、同じ手順を手で行う。
*Three composed screens ("Screen patterns" cards), automated on the web (W1) and run by hand on devices.*

| シナリオ | 手順 / Steps | 合格の条件 / Pass when |
|---|---|---|
| S1 予定を追加する（ScreenAddEvent） | 「予定を追加」→ 何も入れずに「追加する」→ エラーの一覧のリンクで欄へ → 入力して「追加する」 | ドロワーが開くとフォーカスが中へ移る・エラーの一覧へフォーカスが移り件数が読まれる・追加後にドロワーが閉じ、「予定を追加」へフォーカスが戻り、追加が読み上げられる |
| S2 一覧から選んで編集する（ScreenListEdit） | 一覧で授業を開く → 「教室」を編集 → 空で保存（失敗）→ 直して保存 → 2 件を選んで削除 → 確認 → 「元に戻す」 | 今開いている行が分かる・失敗が読まれ入力が残る・保存後に見出しへ戻る・件数つきで確認される・元に戻る |
| S3 通信が切れた状態から戻る（ScreenOffline） | 機内モードにする → 予定を追加 → 機内モードを切る | 警告と「〜時点の内容」が出る・「未送信 1 件」が出る・つながると自動で送られ、お知らせが読まれる |

## 3. 各 OS の手順 / Per-OS procedures

### Windows（N1・N2）
- 自動で確かめられる部分（Flutter の解析とアイコンの画像比較、Word・PowerPoint での書き出し、入っている書体、Edge での見本の表示）は、検証セット `verify/`（`python3 verify/make_kit.py` で組み立て、Windows で `verify.ps1`）でまとめて走らせる。結果の `results` を 1 章に記録する。
  *Automatable parts run from the kit in `verify/`; record its `results` in section 1.*
- NVDA（最新版）とナレーターで S1〜S3。見出しで移動（H キー）、フォームのモードの切り替え、ダイアログの中に読み上げが閉じ込められるか、Tab の順が見た目と同じか。
  *NVDA and Narrator: S1–S3; heading navigation, focus mode, dialog containment, tab order = visual order.*
- キーボードだけで S1〜S3（Tab・Shift+Tab・Enter・Space・Esc・矢印）。フォーカスの枠が常に見えるか。
- WinUI 3: `KM1.xaml` を `App.xaml` の MergedDictionaries に入れてビルド。ライト・ダーク・ハイコントラスト（設定 › アクセシビリティ › コントラスト テーマ）で、主ボタン・入力欄・フォーカスの見え方を確認。
  *WinUI 3: merge `KM1.xaml`, build, and check light, dark and contrast themes.*

### macOS（M1）
- VoiceOver（⌘F5）で S1〜S3。ローター（VO+U）で見出しとフォームの部品が一覧に出るか。
- SwiftUI: `KM1Theme.swift` を入れたプレビューで、ライト・ダーク・「コントラストを上げる」を確認。

### iOS・iPadOS（I1）
- VoiceOver で S1〜S3。スワイプの順が見た目の順と同じか。
- Dynamic Type を最大（アクセシビリティサイズ AX5）にして、文字が切れない・重ならない・横にはみ出さないか（Web は 200% 拡大まで確認済み）。
- Safe Area: ノッチとホームインジケーターのある端末で、BottomSheet・下部のタブ・Toast が隠れないか。

### Android（A1）
- TalkBack で S1〜S3。戻るジェスチャーで、開いているドロワー・シート・ダイアログだけが閉じるか（画面ごと戻らないか）。
- Compose: `Km1Theme.kt` を入れてビルド。主ボタンの縁取り（ダーク）と 48dp の操作領域。

### Flutter（F1）
- `km1_theme.dart`・`km1_widgets.dart` で `flutter analyze` で警告 0。`flutter build`（使う OS ごと）。
- `Km1Density` と `Km1Table`・`Km1SortableList` の `density`、`Km1StepFlow`、`showKm1BottomSheet` を実際の画面で見る。
- 結果（解析の出力）を KM1 の会話に貼れば、こちらで直す。
  *Run `flutter analyze` and builds; paste the output into a KM1 conversation for fixes.*

## 4. 大量のデータ / Large data

headless Chrome で、選べる List と Table に 500〜5,000 行を表示して測った（2026-11-13、このセッションの環境。CPU を 4 倍遅くした値は、性能の低いスマホの目安）。
*Measured in headless Chrome; the 4× CPU slowdown approximates low-end phones.*

| 部品 | 行数 | 表示 | 1 件選ぶ | すべて選ぶ | 4 倍遅い CPU で 1 件選ぶ |
|---|---|---|---|---|---|
| List | 500 | 131ms | 61ms | 32ms | 225ms |
| List | 2,000 | 190ms | 74ms | 119ms | 326ms |
| List | 5,000 | 423ms | 225ms | 226ms | 787ms |
| Table | 500 | 67ms | 30ms | 36ms | 135ms |
| Table | 2,000 | 216ms | 110ms | 140ms | 385ms |
| Table | 5,000 | 666ms | 234ms | 283ms | 1,091ms |

- 結論: 1 件選ぶたびに全部の行を描き直しており、2,000 行を超えると反応が目に見えて遅れる（操作への反応は 200ms 以内が目安）。
  *Each selection re-renders every row; beyond ~2,000 rows the response visibly lags (target: under 200ms).*
- 規則: 1 画面に出す行は 500 行まで。それ以上は `Pagination`（1 ページ 50〜100 件）か、検索・絞り込みで減らす。
  *Rule: show at most 500 rows per screen; paginate (50–100 per page) or filter beyond that.*
- 今後: 見えている行だけを描く仕組み（仮想スクロール）と、選択の変化した行だけを描き直す改良（次の版の候補）。
  *Next: virtualization and re-rendering only changed rows.*

## 5. 書体の確認の手順（T1） / Typeface check procedure

自動の検査では、端末で実際に描かれる書体は分からない。手元の端末で次を行い、T1 に記録する。
*Automated checks cannot see what a device really draws. Do this locally and log it in T1.*

1. `gen/fonttest.html` を確認したい端末のブラウザで開く（`tokens.css` を同じフォルダに置く）。端末は Windows・macOS・iOS・Android のうち使うもの。
   *Open `gen/fonttest.html` in the browser on each target device, next to `tokens.css`.*
2. 「使える書体」の表示を見る。先頭の書体が WARN でも、並びのどれかが PASS ならゴシックで描かれる。FAIL は並びのどれも使えない状態。
3. 日本語・英語・数字・記号（①・℃・〜）の混じった文を目で見て、明朝・セリフ体に落ちていないかを確かめる。比べるための行は URL に `?controls=1` を付けると出る。
4. Office はひな形を開いて見出し・本文の書体名を確かめる。
5. 結果（日付・端末・OS とブラウザの版・返事）を T1 に書く。

## 6. Flutter の画像比較の手順（F2） / Flutter golden procedure

CI の Flutter のテストは、`verify/flutter/test/goldens/` にある承認済みの画像（アイコンの一覧 6 枚、部品を並べたギャラリー 4 枚）と比べる。ギャラリーはテスト用の書体で文字が四角に描かれるので、文字の形ではなく、部品の位置・大きさ・色の変化を見つけるためのもの。Flutter の版は `check.yml` と `goldens.yml` で同じものに固定し、版を上げるときは画像も作り直す（最新の stable は参考のジョブで試す）。画像が違えば CI は失敗し、違った画像は成果物 `flutter-golden-failures` に出る。`--update-goldens`（画像を作り直す）は通常の CI では使わない。
*CI compares against approved images in `verify/flutter/test/goldens/`; any difference fails the build and the diffs are uploaded. `--update-goldens` is never used in the normal CI.*

1. 承認済みの画像を作る・作り直す: GitHub の Actions で「goldens」ワークフローを手で動かす（Run workflow）。CI と同じ ubuntu と Flutter で作るので、手元の OS の書体の違いが入らない。
   *Run the "goldens" workflow by hand; it renders on the same runner as CI.*
2. 成果物 `flutter-goldens-candidate` を落として、6 枚（16・20・24px × ライト・ダーク）を目で確かめる。アイコンが欠けていないか、線の太さ・色が KM1 の決まりどおりか。
3. よければ `verify/flutter/test/goldens/` に入れて commit する。変更の理由（アイコンを足した、など）を変更履歴に書く。
4. 以後、アイコンや Flutter のテーマを変えて画像が変わると CI が失敗する。意図した変更なら 1〜3 をやり直す。意図しない変更なら直す。
   *Afterwards any visual change fails CI; redo steps 1–3 only for intended changes.*

承認済みの画像がまだないあいだは、CI は画像比較を飛ばして警告を出す（ほかのテストは流す）。
*Until approved images exist, CI skips the comparison with a warning and runs the rest.*

## 7. 検査を自分で流す / Running the checks

clone したままの状態から、次の手順で全部の検査を流せる。GitHub の CI（`.github/workflows/check.yml`）も push のたびに同じものを流し、Flutter の解析とテストも別に流す。
*Every check runs from a clean clone as below; CI runs the same on each push, plus Flutter analyze and tests.*

1. 必要なもの: Python 3.10 以上、Node 22、Google Chrome、poppler-utils（`pdffonts`）、librsvg（`rsvg-convert`）、日本語のゴシック体（Noto Sans CJK など）。
2. `pip install -r requirements.txt`、`(cd gen && npm ci)`、`(cd office && npm ci)`
3. `bash gen/check_all.sh` → トークンの生成物の差分・トークンの別名・色の組み合わせのコントラスト・部品の数・保留の期限・理由の確認（`reasoncheck.py`）・アイコン・見本の描画・Web の自動検査（axe・キーボード・320px・再発防止・シナリオ）・精度の監査（PC・タブレット・スマホの幅で全要素の値を 16 項目、`precision_audit.js`）・寸法・Office・PDF・書体の 14 項目。1 つでも落ちれば終了コードが 0 以外になる。
*Requires Python 3.10+, Node 22, Chrome, poppler-utils, librsvg and a CJK sans font; install the pinned dependencies, then run `bash gen/check_all.sh` (14 checks; non-zero exit on any failure).*

実機・読み上げソフト（NVDA・ナレーター・VoiceOver・TalkBack）・各 OS のネイティブのビルドは、ここでは流せない。手順と記録はこの章の 1〜6、Windows 用の検証セットは `verify/`。
*Real devices, screen readers and native builds can't run here; see sections 1–6 and the Windows kit in `verify/`.*

## 8. これまでの点検 / Earlier checks

自動の検査（7 章）に入る前に、手で流して記録した点検。今は同じ内容を `check_all.sh` が毎回確かめている。
*Checks run by hand before they were folded into `check_all.sh` (section 7), which now repeats them on every run.*

### 8.1 利用シナリオと見直し（2026-11-13）/ Scenarios and review fixes

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| 利用シナリオ 3 つ / scenarios | 予定を追加する・一覧から選んで編集する・通信が切れて戻る、をスクリプトで最初から最後まで操作（360・1366px のライト、1024px のダーク） | 18 項目すべて合格 |
| ボタンの並び / action order | Dialog・Drawer・BottomSheet を 360px と 1366px で開き、DOM の順と見た目の順を比較 | どれも一致（以前は 360px で不一致） |
| 表の行の種類 / table rows | compact で、表示専用の行・リンクのある行・選べる行の高さを PC とタッチで測定 | 表示専用だけ 25px に詰まり、ほかは 32・44px を保つ |
| 大量のデータ / large data | List・Table に 500〜5,000 行（「検証」の 4 章） | 2,000 行を超えると選択の反応が 200ms を超える。1 画面 500 行までの規則を追加 |
| 部品の数 / counts | `gen/sync_counts.py --check`（`inventory.json` から数える） | 文書の記述がすべて一致 |
| 手元で行う検証 / local checks | 手順と記録欄を「検証」にまとめた | 実機・読み上げ・各 OS のビルドは未実施 |

### 8.2 書体の点検（KM1-TYP-001、2026-11-14）/ Typeface check

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| ソースの書体の指定 / source declarations | `gen/fontcheck.py`（CSS・JS・Dart・Kotlin・Swift・XAML・HTML） | 使わない書体 0。等幅の並びにあった Courier New（タイプライター風のセリフ体）を外した |
| Office のテーマ / Office themes | `gen/fontcheck.py`・`office/officecheck.py` | ひな形と見本の 4 つで、言語ごとの補助の書体に残っていた Office 既定の明朝・セリフ体・手書き風（新細明體・Times New Roman・Angsana New・MV Boli など）をゴシック系に置き換え、FAIL 0 |
| PDF の埋め込み書体 / PDF fonts | `gen/fontcheck.py`（`pdffonts`） | 2 冊ともゴシック系と等幅だけ |
| 描かれた書体 / rendered fonts | `gen/fontcheck_render.js`（Chrome、見本 175 ページ（ライト・ダーク）、文字ごとに実際の書体） | セリフ体・明朝・手書き風 0。ただしこの環境に日本語の明朝体がないため、和文が明朝に落ちることはここでは見つけられない |
| 道具 / tools | 検査と生成の道具を `gen/` に置いた（`KM1_PROJECT` でフォルダを指定できる） | — |

### 8.3 トークンと密度（KM1-TOK-001）の点検（2026-11-13）/ Token and density check

headless Chrome だけで実施。実機・読み上げソフト・各 OS のビルドは未確認。
*Headless Chrome only; devices, screen readers and native builds not yet checked.*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| トークンの解決 / resolution | `tokens_check.py` で値と参照先を照合。見本で Card の余白・表の行の余白・並べ替えの間を実測 | 14 個すべて一致。密度ごとに 12/2/2・16/4/4・24/8/8px |
| ライト・ダーク / themes | 見本「Density」を両テーマで axe と目視 | 違反 0 |
| 操作領域 / targets | 3 つの密度で、ボタン・チェック・つまみの大きさと選べる行の高さを PC とタッチで測定 | すべて PC 32px・タッチ 44px 以上 |
| キーボード / keyboard | Tab で届く 42 個のフォーカスの見え方と大きさ（PC・タッチ） | 問題なし |
| 文字の拡大 / text resize | 200% 拡大（683px 相当）、文字の間隔の上書き（WCAG 1.4.12）、両方、320px | はみ出し・切れなし（視覚的に隠した読み上げ用の文字を除く） |
| 意図しない変化 / regression | 既定（regular）で全 65 の見本を、変更前後で画素比較（PC とタッチ） | 同じ。差が出た 5 つは動きのある部品で、アニメーションを止めると同じ |
| 回帰の自動検査 / axe | 60 の見本 × ライト・ダーク（120 ページ） | 違反 0 |
| 生成物 / generated | Flutter（構文と API 名）、Kotlin・Swift（構文）、XAML（xmllint） | 問題なし（ビルドは未実施） |

### 8.4 フォーム（KM1-PAT-001）の点検（2026-11-13）/ Forms check

headless Chrome だけで実施。実機・スクリーンリーダーは未確認。
*Headless Chrome only; real devices and screen readers not yet checked.*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| 動き方 26 項目 / behavior | 見本フォームをスクリプトで操作（離れたら確かめる、直すと消える、送信で一覧とフォーカス、リンクで欄へ、条件表示でフォーカスを奪わない、読み上げ文、隠れた欄は検証しない・送らない、値が残る、相関チェック、送信中の表示、横スクロールなし、DOM 順＝見た目の順）/ scripted | 320・360・640・1023・1024・1366px（ライト）、360・1366px（ダーク）ですべて合格 / all pass |
| 2 列の条件 / two-column rule | 画面 500・1023・1024・1366px、入れ物 420px | 2 列になるのは 1024px 以上かつ入れ物 560px 以上のときだけ / only ≥1024px and container ≥560px |
| 自動検査 / axe-core 4.10 | 新しい 4 部品、送信後・条件表示後の状態も含む。1366px と 360px / incl. after-submit and revealed states | 違反 0 / 0 violations |
| 既存部品の回帰 / regression | 全 45 プレビュー × ライト・ダーク（90 ページ）を axe で再検査 / all 45 previews re-run | 違反 0、はみ出し 0 / 0 violations, no overflow |
| フォーカス表示と押せる大きさ / focus and target | Tab で届く全要素、PC とタッチ / every tabbable, PC and touch | 問題なし / no issues |
| 強制カラー / forced colors | CSS に `CanvasText` の規則を追加 | 表示の確認は未実施 / rendering not verified |

### 8.5 アクセシビリティ点検（2026-11-12）/ Accessibility check

当時の全 40 部品のプレビューを、ライトとダークの両方で点検した（2026-11-12 時点の記録、追加した部品も同じ方法で点検。追加分では、パンくずのリンクの幅、ファイル選択のフォーカス表示、予定表の締め切りの重なりと高さ、終日の行の読み上げ名、ポップオーバーの属性、タグ欄の押せる範囲を直した）。
*All 40 component previews were checked in light and dark with the same method; additions needed fixes (breadcrumb width, file picker focus, timeline deadline overlap and height, all-day row naming, popover attribute, tag field hit area).*

| 点検 / Check | 方法 / Method | 結果 / Result |
|---|---|---|
| WCAG 2.2 A・AA の自動検査 / automated | axe-core 4.10（WCAG 2.0〜2.2 の A・AA と推奨ルール）。メニュー・ダイアログ・ツールチップ・カレンダーは開いた状態でも実施 / incl. open states | 違反 0。判定保留 3 種は、背景色をツールが読めないもの（色は計算で合格済み）/ 0 violations |
| リフロー 1.4.10 / reflow | 320px 幅で横にはみ出す要素を数えた / overflow at 320px | 0（表と時間割は決まりどおり枠内で横スクロール）|
| 文字の間隔 1.4.12 / text spacing | 行間 1.5・字間 0.12em・語間 0.16em を強制 / forced spacing | 切れていた時間割のコマとナビの文字を、折り返しに直した / truncation fixed |
| フォーカス / focus | 操作できる全要素に順にフォーカスし、届くか・2px 以上の枠が出るかを確認 / every focusable element | 全部品で届き、枠が出る / all pass |
| 操作領域 2.5.8・2.5.5 / target size | PC は 24px 以上、タッチ表示は 44px 以上か / 24px PC, 44px touch | タッチ表示の small ボタンの幅が 37〜38px だったので、最小幅を高さと同じにした / fixed |
| 強制カラー / forced colors | Windows のハイコントラスト相当で表示 / high-contrast emulation | カレンダーの選択日・タブ・ページ送り・ナビの選択中が見分けにくかったので、強調色で示すように直した / fixed |

未確認 / Not checked: スクリーンリーダー（NVDA・VoiceOver・TalkBack）での実際の読み上げ、スマホ実機、ブラウザの 200% 拡大での実操作、Flutter 版。自動検査で見つかるのは問題の一部だけなので、読み上げの確認は人が行う必要がある。
*Screen readers (NVDA, VoiceOver, TalkBack), real phones, real 200% browser zoom and the Flutter side. Automated tools catch only part of the problems; screen-reader behavior still needs a human check.*

- 部品が使う色の組み合わせ（最初の 12 部品の 30 組と、追加した部品の 18 組、時間割の分類色の淡い塗りの上の文字 18 色分）を、ライトとダークの両方で計算し、文字 4.5:1 と枠・アイコン 3:1 を満たす（不合格 0）。分類色 `cat-*` はこの確認の対象外で、3:1 に満たない色がある（「画面の組み立て」に一覧）。この確認でダークの選択表示が 2.23:1 だったため、上の「選択時の縁」を決めた。
  *The color pairs used by components (30 for the first 12 components, 18 for the added ones, plus text on the timetable tint for all 18 category colors) were computed in light and dark: 4.5:1 for text, 3:1 for borders and icons (0 failures; the `cat-*` category colors are outside this check and some are below 3:1, as listed in Patterns). The check found selection marks at 2.23:1 in dark, which led to the "Selected edges" rule above.*
- Tabs の矢印キー・Home・End、Dialog の Esc、無効ボタンの Tab 到達、Alert の閉じるボタンの大きさ、Menu のキー操作（開く・移動・端で折り返し・Esc でボタンに戻る・外側クリックで閉じる）、Table の並べ替えと `aria-sort`、Toast の閉じる、Chip の `aria-pressed`、Nav の `aria-current`、Calendar のキー操作（矢印・Home・PageUp/PageDown・`min` で止まる）、Tooltip（フォーカスで出る・Esc で消える・マウスで出る）、Pagination の省略と端の動きは、ブラウザで動作を確認した。
  *Exercised in a browser: Tabs arrow/Home/End keys, Dialog Esc, Tab reach of disabled buttons, the Alert close button, Menu keys (open, move, wrap, Esc returns focus, outside click closes), Table sorting with `aria-sort`, Toast dismissal, Chip `aria-pressed`, Nav `aria-current`, Calendar keys (arrows, Home, PageUp/PageDown, stopping at `min`), Tooltip (focus shows, Esc hides, hover shows), Pagination truncation and end behavior.*
- ネイティブ用の `KM1.xaml`（WinUI 3）・`Km1Theme.kt`（Jetpack Compose）・`KM1Theme.swift`（SwiftUI）は、文法チェックを通した。WinUI と Compose は、使ったキー・関数・引数が公式のソース（2026-11-12 時点）に実在することも照合した。SwiftUI はソースが非公開のため照合していない。どれも**ビルドは未実施**。
  *Native files passed syntax checks; WinUI and Compose names were matched against official sources (SwiftUI is closed source). None has been built.*
- Flutter の `km1_theme.dart` と `km1_widgets.dart` は、(1) Dart の文法チェック（構文エラー 0）と、(2) 使っているクラス・名前付き引数・メンバー・アイコン名が Flutter の安定版（2026-11-09 時点）のソースと `fluentui_system_icons` 1.1.294 に実在するかの照合（問題 0）を通した。この照合は、わざと入れた間違い 6 件のうち 5 件を見つけ、列挙型の値の間違い 1 件は見逃した。**型の確認とコンパイル（`flutter analyze`）は、この環境では Flutter を入れられないため未実施。**
  *Flutter files passed (1) a Dart syntax check and (2) a check that every class, named argument, member and icon name exists in Flutter stable (2026-11-09) and fluentui_system_icons 1.1.294. The check caught 5 of 6 planted mistakes (missing a wrong enum value). **Type checking and compilation were not possible here.***
- 未確認: スクリーンリーダーでの読み上げ、実機のスマホ、Flutter での実際の見た目。
  *Not checked: screen-reader output, real mobile devices, and how it actually looks in Flutter.*
