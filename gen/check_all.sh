#!/usr/bin/env bash
# KM1 の検査をまとめて流す / Run every KM1 check from a clean clone
# 使い方 / Usage: bash gen/check_all.sh   （CI も同じものを流す / CI runs the same script）
# 前もって / Prerequisites:
#   pip install -r requirements.txt
#   (cd gen && npm ci) && (cd office && npm ci)
#   Google Chrome（CHROME で場所を指定できる）、poppler-utils（pdffonts）、librsvg（rsvg-convert）
# 1 つでも落ちたら終了コード 1。最後に結果の一覧を出す。/ Exits 1 if any step fails; prints a summary.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
WORK="$(mktemp -d)"; RESULTS=(); FAIL=0
step() { local name="$1"; shift; echo; echo "=== $name"; if "$@"; then RESULTS+=("OK   $name"); else RESULTS+=("FAIL $name"); FAIL=1; fi; }

# 1. トークンから作る生成物が、入っているものと同じか / generated files match tokens.json
regen() {
  python3 gen/tokens_css.py && python3 gen/km1_dart.py && python3 gen/native.py >/dev/null && python3 gen/tokens_dtcg.py >/dev/null &&
  git diff --exit-code -- tokens.css km1_theme.dart KM1.xaml Km1Theme.kt KM1Theme.swift dist/tokens
}
step "トークンの生成物 / generated token files" regen
step "トークンの別名 / token roles" python3 gen/tokens_check.py
step "色の組み合わせのコントラスト / contrast pairs" python3 gen/contrast_check.py
step "部品の数と文書 / counts" python3 gen/sync_counts.py --check
step "保留と提案の期限 / governance dates" python3 gen/govcheck.py
step "理由の確認（機械の部分）/ reason review" python3 gen/reasoncheck.py
step "アイコン / icons" python3 icons/iconcheck.py icons/km1-icons.json icons/KM1Icons.ttf
# 2. Web の見本 / web previews
step "見本の描画 / render previews" python3 gen/render_previews.py "$WORK/rc"
step "Web の自動検査（axe・キーボード・320px・再発防止・シナリオ）/ web tests" node gen/web_test.js "$WORK/rc"
step "精度の監査（PC とスマホの幅で全要素の値）/ precision audit" node gen/precision_audit.js "$WORK/rc"
step "部品の寸法 / sizes" python3 gen/sizecheck.py
# 3. Office と PDF / Office and PDF
office() { mkdir -p "$WORK/office" && (cd office && node km1_docx.js "$WORK/office" && node km1_pptx.js "$WORK/office") >/dev/null && python3 office/officecheck.py "$WORK"/office/*; }
step "Office のひな形 / Office templates" office
pdfs() { local r=0; for f in dist/*.pdf; do python3 pdf/pdfcheck.py "$f" | tail -1; python3 pdf/pdfcheck.py "$f" >/dev/null || r=1; done; return $r; }
step "PDF（dist）/ PDFs" pdfs
step "書体 / fonts" python3 gen/fontcheck.py . dist

echo; echo "=== 結果 / Summary"; printf '%s\n' "${RESULTS[@]}"
rm -rf "$WORK"; exit $FAIL
