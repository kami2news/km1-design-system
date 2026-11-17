KM1 のアプリアイコンとファビコン（KM1-ICO-001 §6）。紺（`brand`）の正方形に白の「KM1」と表紙のしるし。`icons/km1_appicon.py` が 1 枚の元の絵から Web・Android・iOS・Windows の大きさを全部書き出す。
*KM1 app icon and favicons: navy square, white "KM1" and the cover bar. `icons/km1_appicon.py` writes every platform size from one master.*

利用側が渡すもの（道具に渡す）: 背景の色（`--bg`）、絵柄の色（`--fg`）、絵柄（KM1 のしるし、KM1 のアイコン 1 つ、または 3 文字までの文字）。
*Inputs to the tool: background, foreground, and a motif (the KM1 mark, one KM1 icon, or up to three characters).*

## 使い方 / Usage

- 絵柄は中央の直径 60% の円に収める。Android の円や PWA の maskable で切り抜かれても欠けない。
  *Keep the motif inside a 60% circle so platform masks never clip it.*
- 絵柄と背景のコントラストは 3:1 以上（道具が確かめ、足りなければ作らない）。
  *Motif contrast at least 3:1 (the tool refuses otherwise).*
- iOS・ストア用は透明を使わない。48px 以下のファビコンは角を丸め、絵柄を大きくする。
  *No transparency for iOS and stores; small favicons are pre-rounded with a larger motif.*
- ほかのアプリは同じ道具で色と絵柄だけ変える（例: ティールに `timetable`）。Flutter は書き出された `flutter_launcher_icons.yaml` を使う。
  *Other apps reuse the tool with their own color and motif; Flutter uses the generated `flutter_launcher_icons.yaml`.*
