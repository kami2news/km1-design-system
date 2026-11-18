# KM1 の検証セット（Windows 実機用）/ KM1 verification kit for Windows

Windows の実機（XP9 など）で、headless Chrome では確かめられないことを確かめるセット。2026-11-15 に別のリポジトリ（`km1-verify`）で作り、2026-11-18 にここへ移した。
*A kit for checks headless Chrome can't do, run on a real Windows machine. Moved here from the separate `km1-verify` repository on 2026-11-18.*

## 組み立て / Build

1. `cd gen && npm i`（見本の描画に使う / for rendering previews）
2. `python3 verify/make_kit.py` → `verify/build/KM1_verify/` と `KM1_verify.zip` ができる。本体の今のファイルから組み立てるので、KM1 を直したら組み立て直す。
   *Builds from the current KM1 files; rebuild after changing KM1.*

## 実行 / Run（Windows）

1. `KM1_verify.zip` を好きな場所に展開する（例: ドキュメント\KM1_verify）。
2. フォルダで PowerShell を開き、次を実行する:
   `powershell -ExecutionPolicy Bypass -File .\verify.ps1`
3. `results\` に log.txt・アイコンの画像（goldens）・Office から書き出した PDF・Edge の画像ができる。results フォルダごと Claude に渡すと、中身を読んで判定し、`verification.md` に記録する。

このセットが読み書きするのは自分のフォルダの中（results）だけ。Flutter・Word・PowerPoint・Edge を使う。
*The kit only writes inside its own results folder; it uses Flutter, Word, PowerPoint and Edge.*

## 確かめること / What it checks

1. **Flutter:** `flutter analyze`、部品の見本（`gallery.dart`）とアイコンの画像比較（`test/`）
2. **Office:** Word・PowerPoint でひな形と見本を開き、PDF に書き出す。使われた書体の一覧
3. **書体:** 端末に入っている日本語と英語の書体
4. **Edge:** 部品の見本 6 件を Edge で開いて画像にする
