# KM1 の検証（XP9 / Windows）/ KM1 verification on Windows
# 使い方: このフォルダで PowerShell を開き  powershell -ExecutionPolicy Bypass -File .\verify.ps1
# 結果は results\ に出る（log.txt・画像・PDF）。ほかの場所は変更しない。
$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$out = Join-Path $root 'results'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$log = Join-Path $out 'log.txt'
function Log($m) { $m | Tee-Object -FilePath $log -Append }
"KM1 verify $(Get-Date -Format s) on $env:COMPUTERNAME" | Set-Content $log -Encoding utf8

# 1. Flutter
Log '=== 1. Flutter ==='
Push-Location (Join-Path $root 'flutter')
try {
  Log (flutter --version 2>&1 | Out-String)
  Log (flutter pub get 2>&1 | Out-String)
  Log '--- flutter analyze'
  Log (flutter analyze 2>&1 | Out-String)
  Log "analyze exit: $LASTEXITCODE"
  Log '--- flutter test --update-goldens (画像を作る / write golden images)'
  Log (flutter test --update-goldens 2>&1 | Out-String)
  Log "test(update) exit: $LASTEXITCODE"
  Log '--- flutter test (作った画像と比べる / compare)'
  Log (flutter test 2>&1 | Out-String)
  Log "test exit: $LASTEXITCODE"
  Copy-Item -Recurse -Force (Join-Path 'test' 'goldens') (Join-Path $out 'goldens') -ErrorAction SilentlyContinue
} catch { Log "Flutter error: $_" }
Pop-Location

# 2. Office（Word・PowerPoint で開いて PDF に書き出す）/ open in Office and export PDF
Log '=== 2. Office ==='
$off = Join-Path $root 'office'
try {
  $w = New-Object -ComObject Word.Application; $w.Visible = $false
  foreach ($f in @('KM1_文書見本.docx', 'KM1_文書.dotx')) {
    $p = Join-Path $off $f
    $d = $w.Documents.Open($p, $false, $true)
    $pdf = Join-Path $out ($f + '.pdf')
    $d.ExportAsFixedFormat($pdf, 17)
    Log "Word OK: $f pages=$($d.ComputeStatistics(2))"
    $d.Close($false)
  }
  $w.Quit()
} catch { Log "Word error: $_" }
try {
  $pp = New-Object -ComObject PowerPoint.Application
  foreach ($f in @('KM1_スライド見本.pptx', 'KM1_スライド.potx')) {
    $p = Join-Path $off $f
    $pr = $pp.Presentations.Open($p, $true, $false, $false)
    $pdf = Join-Path $out ($f + '.pdf')
    $pr.SaveAs($pdf, 32)
    Log "PowerPoint OK: $f slides=$($pr.Slides.Count)"
    # 置き換えられた書体の一覧 / fonts used and whether they are installed
    foreach ($ft in $pr.Fonts) { Log ("  font: {0}  embedded-able={1}" -f $ft.Name, $ft.Embeddable) }
    $pr.Close()
  }
  $pp.Quit()
} catch { Log "PowerPoint error: $_" }

# 3. 書体（入っている日本語のゴシック体）/ installed fonts
Log '=== 3. Fonts ==='
Add-Type -AssemblyName System.Drawing
$fams = (New-Object System.Drawing.Text.InstalledFontCollection).Families | ForEach-Object Name
foreach ($n in @('Noto Sans JP', 'Yu Gothic UI', 'Yu Gothic', '游ゴシック', 'Meiryo UI', 'Segoe UI', 'Segoe UI Variable Text', 'Cascadia Mono', 'Consolas', 'Microsoft JhengHei', 'Leelawadee UI', 'Nirmala UI', 'Hind')) {
  Log ("  {0}: {1}" -f $n, ($(if ($fams -contains $n) { 'あり / installed' } else { 'なし / missing' })))
}

# 4. Web（Edge で見本を開いて画像にする）/ render previews in Edge
Log '=== 4. Edge ==='
$edge = @("${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe", "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($edge) {
  Get-ChildItem (Join-Path $root 'web') -Filter *.html | ForEach-Object {
    $png = Join-Path $out ('edge-' + $_.BaseName + '.png')
    & $edge --headless=new --disable-gpu --hide-scrollbars --window-size=1000,900 "--screenshot=$png" $_.FullName 2>$null
    Start-Sleep -Seconds 3
    Log "  $($_.Name): $(Test-Path $png)"
  }
} else { Log '  Edge が見つからない / Edge not found' }
Log '=== done ==='
