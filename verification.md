# 検証の手順と記録 / Verification

KM1 の検証は「自動の検査（ここで実施）」と「実機・読み上げ・各 OS のビルド（手元の環境で実施）」に分かれる。自動の検査に合格しても、人が快適に使えることの確認にはならない。この章は、手元で行う検証の手順と、結果の記録欄。
*Automated checks run here; devices, screen readers and native builds must run locally. Passing automated checks does not prove comfortable use. This chapter holds the local procedures and the results log.*

## 1. 記録 / Results log

状態: **済**（合格）・**不合格**（課題を書く）・**未実施**。日付と、使った端末・OS・ソフトの版を書く。
*Status: done / failed (note the issue) / not run, with date and versions.*

| # | 対象 / Target | 内容 / What | 状態 | 日付・環境 | 課題 |
|---|---|---|---|---|---|
| W1 | Web（headless Chrome） | 部品の自動検査（axe）・キーボード・320px・密度・利用シナリオ 3 つ・大量データ | 済 | 2026-11-13・Chrome（このセッションの環境） | 大量データ（下の 4 章） |
| W2 | Web（実際のブラウザ） | 利用シナリオ 3 つを Chrome・Edge・Safari・Firefox で | 未実施 | | |
| N1 | Windows | NVDA とナレーターで利用シナリオ 3 つ | 未実施 | | |
| N2 | Windows | WinUI 3 のビルドと表示（`KM1.xaml`） | 未実施 | | |
| M1 | macOS | VoiceOver で利用シナリオ、SwiftUI の表示 | 未実施 | | |
| I1 | iOS・iPadOS | VoiceOver、Dynamic Type、Safe Area | 未実施 | | |
| A1 | Android | TalkBack、戻るジェスチャー、Compose のビルド | 未実施 | | |
| F1 | Flutter | `flutter analyze`、ビルド、実際の画面 | 未実施 | | |
| T1 | 書体 / Typefaces | Office（Windows・Mac）、iOS・Android・Windows の画面で、文字がゴシック体で描かれるか（明朝・セリフ体に落ちていないか）。日本語・英語・数字・記号（①・℃・〜）の混じった文で見る。手順は 5 章 | 未実施 | | 自動の検査（`fontcheck.py`・`fontcheck_render.js`）は 2026-11-14 に合格 |
| C1 | 文書の整合 / Docs consistency | `gen/sync_counts.py --check`（部品数・対応表の食い違い）と `gen/govcheck.py`（保留・提案の期限）を一緒に流す | 未実施 | | 2026-11-15 に追加。変更のたびに流す |

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
