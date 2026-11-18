// KM1-DOC-003 スライドのひな形と見本を作る / Build the KM1 slide template (.potx) and sample deck (.pptx)
// 使い方 / Usage: node km1_pptx.js <出力フォルダ / out dir>
// 寸法は 1pt ＝ KM1 の 1px として、KM1 のトークンの値をそのまま使う（16:9、960 × 540pt）。
// Sizes use KM1 token values with 1pt = 1px on a 960 × 540pt (16:9) slide.
const pptxgen = require('pptxgenjs');
const fs = require('fs'), path = require('path'), JSZip = require(require.resolve('jszip', {paths: [path.dirname(require.resolve('pptxgenjs'))]}));
const OUT = process.argv[2] || '.';
const PT = v => v / 72;                       // pt → inch
const FONT = '游ゴシック';                      // 和文・英数字とも / both scripts (office.md §2)
const T = {                                   // KM1 の型の表から / from the KM1 type ramp
  display: 68, largeTitle: 40, title2: 28, subtitle1: 20, body: 20, small: 16, caption: 12 };
const S = { xs: 4, sm: 8, md: 12, lg: 16, xl: 20, xxl: 24, xxxl: 32 };   // spacing tokens
const M = S.xxxl;                             // 外の余白 32pt / outer margin
const W = 960, H = 540;
const THEME = { name: 'KM1', headFontFace: FONT, bodyFontFace: FONT, colors: {
  dk1: '242424', lt1: 'FFFFFF', dk2: '10218B', lt2: 'F5F5F5',
  accent1: '10218B', accent2: '0F6CBD', accent3: '038387', accent4: 'BC4B09', accent5: '5C2E91', accent6: '107C10',
  hlink: '10218B', folHlink: '5C2E91' } };
const C = { ink: '242424', ink2: '424242', ink3: '616161', brand: '10218B', line: 'E0E0E0', tint: 'ECEFFC', muted: 'F5F5F5' };
const LANG = 'ja-JP';
// KM1 の表記（notices 2.1・2.6）。ひな形は本文に入れず、ノートかファイルの説明に入れる（使う人の文書に写らないように）
// KM1 notices 2.1 and 2.6; templates carry them in notes or file properties, never in the body
const KM1_NOTICE_JA = 'KM1 は個人が作ったデザイン標準です。Microsoft、セイコーエプソン、東京科学大学（Science Tokyo）、デジタル庁、そのほかの組織が作成・承認・推奨したものではなく、これらの組織とは関係がありません。名称・商標は各権利者のものです。KM1 は MIT License で公開しています。ライセンスの全文と著作権表示は https://github.com/kami2news/km1-design-system の LICENSE を参照してください。';
const KM1_NOTICE_EN = "KM1 is a personal design standard. It was not created, approved or endorsed by Microsoft, Seiko Epson, Institute of Science Tokyo, Japan's Digital Agency or any other organization, and is not affiliated with them. All names and trademarks belong to their owners. KM1 is released under the MIT License. See the LICENSE in https://github.com/kami2news/km1-design-system for the full text and copyright notice.";


function layouts(pres, docName) {
  const foot = [
    { text: { text: docName, options: { x: PT(M), y: PT(H - M + 6), w: PT(600), h: PT(20), fontSize: T.caption, color: C.ink3, fontFace: FONT, margin: 0, lang: LANG } } },
  ];
  const num = { x: PT(W - M - 80), y: PT(H - M + 6), w: PT(80), h: PT(20), fontSize: T.caption, color: C.ink3, fontFace: FONT, align: 'right' };
  pres.defineSlideMaster({ title: 'KM1 表紙 / Title', background: { color: 'FFFFFF' },
    objects: [
      { rect: { x: PT(M + 16), y: PT(120), w: PT(62), h: PT(17), fill: { color: C.brand }, line: { type: 'none' } } },  // 表紙のしるし（PDF と同じ 22 × 6mm）
      { placeholder: { options: { name: 'title', type: 'title', x: PT(M + 16), y: PT(152), w: PT(W - 2 * M - 32), h: PT(120), fontSize: T.largeTitle, bold: true, color: C.brand, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG }, text: '題名 / Title' } },
      { placeholder: { options: { name: 'subtitle', type: 'body', x: PT(M + 16), y: PT(288), w: PT(W - 2 * M - 32), h: PT(64), fontSize: T.subtitle1, color: C.ink2, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text: '副題 / Subtitle' } },
      { placeholder: { options: { name: 'meta', type: 'body', x: PT(M + 16), y: PT(H - M - 48), w: PT(600), h: PT(40), fontSize: T.small, color: C.ink3, fontFace: FONT, valign: 'bottom', margin: 0, lang: LANG }, text: '版の日付・作成者 / Date, author' } },
    ] });
  pres.defineSlideMaster({ title: 'KM1 区切り / Section', background: { color: C.muted },
    objects: [
      { placeholder: { options: { name: 'number', type: 'body', x: PT(M + 16), y: PT(176), w: PT(200), h: PT(40), fontSize: T.subtitle1, bold: true, color: C.brand, fontFace: FONT, margin: 0, lang: LANG }, text: '01' } },
      { placeholder: { options: { name: 'title', type: 'title', x: PT(M + 16), y: PT(224), w: PT(W - 2 * M - 32), h: PT(120), fontSize: T.largeTitle, bold: true, color: C.ink, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG }, text: '章の題名 / Section title' } },
      ...foot ], slideNumber: num });
  const titleBox = { name: 'title', type: 'title', x: PT(M), y: PT(M), w: PT(W - 2 * M), h: PT(44), fontSize: T.title2, bold: true, color: C.ink, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG };
  const bodyTop = M + 44 + S.xxl;              // 100pt
  const bodyH = H - bodyTop - M - S.xxl;       // 本文の下端は柱の上 24pt / ends 24pt above the footer
  pres.defineSlideMaster({ title: 'KM1 題名と本文 / Title and content', background: { color: 'FFFFFF' },
    objects: [ { placeholder: { options: titleBox, text: 'スライドの題名 / Slide title' } },
      { placeholder: { options: { name: 'body', type: 'body', x: PT(M), y: PT(bodyTop), w: PT(W - 2 * M), h: PT(bodyH), fontSize: T.body, color: C.ink, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text: '本文 / Body' } },
      ...foot ], slideNumber: num });
  const colW = (W - 2 * M - S.xxxl) / 2;
  pres.defineSlideMaster({ title: 'KM1 2 段 / Two columns', background: { color: 'FFFFFF' },
    objects: [ { placeholder: { options: titleBox, text: 'スライドの題名 / Slide title' } },
      { placeholder: { options: { name: 'left', type: 'body', x: PT(M), y: PT(bodyTop), w: PT(colW), h: PT(bodyH), fontSize: T.body, color: C.ink, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text: '左 / Left' } },
      { placeholder: { options: { name: 'right', type: 'body', x: PT(M + colW + S.xxxl), y: PT(bodyTop), w: PT(colW), h: PT(bodyH), fontSize: T.body, color: C.ink, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text: '右 / Right' } },
      ...foot ], slideNumber: num });
  pres.defineSlideMaster({ title: 'KM1 題名だけ / Title only', background: { color: 'FFFFFF' },
    objects: [ { placeholder: { options: titleBox, text: 'スライドの題名 / Slide title' } }, ...foot ], slideNumber: num });
  return { bodyTop, bodyH, colW };
}

async function save(z, file) {                    // フォルダの項目を入れずに書く / write without folder entries
  const o = new JSZip();
  for (const [n, f] of Object.entries(z.files)) if (!f.dir) o.file(n, await f.async('nodebuffer'), { createFolders: false });
  fs.writeFileSync(file, await o.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}
async function toTemplate(file, potx) {             // .pptx → .potx（中身の種類を書き換える）/ change the main content type
  const z = await JSZip.loadAsync(fs.readFileSync(file));
  let ct = await z.file('[Content_Types].xml').async('string');
  ct = ct.replace('presentationml.presentation.main+xml', 'presentationml.template.main+xml');
  z.file('[Content_Types].xml', ct);
  await save(z, potx);
}
// 言語ごとの補助の書体もゴシック系にする（KM1-TYP-001）/ make the per-script theme fonts sans too
const SCRIPT_SANS = { Hant: 'Microsoft JhengHei', Arab: 'Segoe UI', Hebr: 'Segoe UI', Viet: 'Segoe UI', Thai: 'Leelawadee UI', Khmr: 'Leelawadee UI', Laoo: 'Leelawadee UI',
  Geor: 'Segoe UI', Armn: 'Segoe UI', Cher: 'Gadugi', Cans: 'Gadugi', Ethi: 'Ebrima', Thaa: 'Nirmala UI', Uigh: 'Segoe UI',
  Syrc: 'Segoe UI Historic', Syre: 'Segoe UI Historic', Syrj: 'Segoe UI Historic', Syrn: 'Segoe UI Historic',
  Deva: 'Nirmala UI', Beng: 'Nirmala UI', Gujr: 'Nirmala UI', Guru: 'Nirmala UI', Knda: 'Nirmala UI', Mlym: 'Nirmala UI', Orya: 'Nirmala UI', Taml: 'Nirmala UI', Telu: 'Nirmala UI', Sinh: 'Nirmala UI' };
function sansScripts(x) {
  return x.replace(/<a:font script="([A-Za-z]+)" typeface="[^"]*"\/>/g, (m, s) => SCRIPT_SANS[s] ? `<a:font script="${s}" typeface="${SCRIPT_SANS[s]}"/>` : m);
}
async function fixTheme(file) {                     // 和文の書体と言語を足す / add East Asian theme font and language
  const z = await JSZip.loadAsync(fs.readFileSync(file));
  for (const n of Object.keys(z.files).filter(n => /theme\/theme\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    x = sansScripts(x.replace(/<a:ea typeface="[^"]*"\/>/g, `<a:ea typeface="${FONT}"/>`));
    z.file(n, x);
  }
  // 既定の文字の大きさを KM1 の型の表に合わせる / map pptxgenjs default sizes to the KM1 ramp
  const MAP = { 4400: 2800, 3200: 2000, 2800: 2000, 2400: 2000, 1800: 1600 };
  for (const n of Object.keys(z.files).filter(n => /slideMasters\/slideMaster\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    x = x.replace(/sz="(4400|3200|2800|2400|1800)"/g, (m, v) => `sz="${MAP[v]}"`);
    z.file(n, x);
  }
  // グラフの系列に模様を付ける（KM1-COL-001）。系列 0 は塗り、1 は横線、2 は縦線…
  // Pattern fills for chart series (KM1-COL-001): series 0 solid, 1 horizontal, 2 vertical, ...
  const PRST = [null, 'dkHorz', 'dkVert', 'wdDnDiag', 'smGrid', 'diagCross', 'dotGrid', 'lgCheck'];
  for (const n of Object.keys(z.files).filter(n => /charts\/chart\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    const sers = x.match(/<c:ser>[\s\S]*?<\/c:ser>/g) || [];
    if (sers.length < 2) continue;
    sers.forEach((ser, i) => {
      const prst = PRST[i % PRST.length]; if (!prst) return;
      const out = ser.replace(/(<c:spPr>)<a:solidFill><a:srgbClr val="([0-9A-Fa-f]{6})"\/><\/a:solidFill>/,
        (m, a, v) => `${a}<a:pattFill prst="${prst}"><a:fgClr><a:srgbClr val="${v}"/></a:fgClr><a:bgClr><a:srgbClr val="FFFFFF"/></a:bgClr></a:pattFill>`);
      x = x.replace(ser, out.replace(/(<\/a:pattFill>)(<a:ln)/, '$1$2').replace(/<c:spPr><a:pattFill([\s\S]*?)<\/a:pattFill>(?!<a:ln)/, (m) => m + `<a:ln w="9525"><a:solidFill><a:srgbClr val="616161"/></a:solidFill></a:ln>`));
    });
    z.file(n, x);
  }
  for (const n of Object.keys(z.files).filter(n => /charts\/chart\d+\.xml$/.test(n))) {   // 軸の線を KM1 の色に / axis lines in a KM1 color
    z.file(n, (await z.file(n).async('string')).replace(/val="888888"/g, 'val="616161"'));
  }
  let p = await z.file('ppt/presentation.xml').async('string');
  z.file('ppt/presentation.xml', p.replace(/sz="1800"/g, 'sz="2000"'));
  // 表の 1 行目を見出しの行にする（読み上げで見出しとして扱われる）/ mark the first table row as header
  for (const n of Object.keys(z.files).filter(n => /slides\/slide\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    x = x.replace(/<a:tblPr\/>/g, '<a:tblPr firstRow="1"/>').replace(/<a:tblPr(?![^>]*firstRow)([^>\/]*)>/g, '<a:tblPr firstRow="1"$1>');
    z.file(n, x);
  }
  await save(z, file);
}

function props(pres, title) {
  pres.layout = 'LAYOUT_WIDE';
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT, lang: LANG };
  pres.title = title; pres.subject = 'KM1-DOC-003'; pres.author = ''; pres.company = '';
}

async function build() {
  // テーマの色と名前を書き込む（外部の道具は要らない）/ write theme colors and name (no external tool needed)
  const applyTheme = async (file, th) => {
    const z = await JSZip.loadAsync(fs.readFileSync(file));
    for (const n of Object.keys(z.files).filter(n => /theme\/theme\d+\.xml$/.test(n))) {
      let x = await z.file(n).async('string');
      x = x.replace(/(<a:theme\b[^>]*\bname=")[^"]*"/, `$1${th.name}"`).replace(/(<a:clrScheme\b[^>]*\bname=")[^"]*"/, `$1${th.name}"`).replace(/(<a:fontScheme\b[^>]*\bname=")[^"]*"/, `$1${th.name}"`);
      for (const [k, v] of Object.entries(th.colors)) {
        x = x.replace(new RegExp(`<a:${k}>[\\s\\S]*?</a:${k}>`), `<a:${k}><a:srgbClr val="${v}"/></a:${k}>`);
      }
      z.file(n, x);
    }
    fs.writeFileSync(file, await z.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
  };
  // 1) ひな形 / template
  {
    const pres = new pptxgen(); props(pres, 'KM1 スライドのひな形 / KM1 slide template'); layouts(pres, '文書名 / Document name');
    const f = path.join(OUT, 'KM1_slides_template.pptx');
    pres.addSlide({ masterName: 'KM1 表紙 / Title' }).addText('KM1 スライドのひな形', { placeholder: 'title' }).addNotes(KM1_NOTICE_JA + '\n' + KM1_NOTICE_EN);
    await pres.writeFile({ fileName: f }); await applyTheme(f, THEME); await fixTheme(f);
    await toTemplate(f, path.join(OUT, 'KM1_スライド.potx')); fs.unlinkSync(f);
  }
  // 2) 見本 / sample deck
  const pres = new pptxgen(); props(pres, 'KM1 スライドの規定 見本 / KM1 slide rules sample');
  const L = layouts(pres, 'KM1 スライドの規定 見本');
  const sc = pres.SchemeColor;
  const t = (s, o = {}) => ({ text: s, options: Object.assign({ lang: LANG }, o) });
  const en = (s) => t(s, { fontSize: T.small, color: C.ink3, breakLine: true });

  pres.addSection({ title: '表紙 / Cover' });
  let s = pres.addSlide({ masterName: 'KM1 表紙 / Title', sectionTitle: '表紙 / Cover' });
  s.addText('KM1 スライドの規定', { placeholder: 'title' });
  s.addText('ひな形の使い方の見本 / How to use the KM1 slide template', { placeholder: 'subtitle' });
  s.addText('2026-11-13・KM1', { placeholder: 'meta' });
  s.addNotes('表紙。題名は 40pt・太字・ブランドの紺。しるしは PDF の表紙と同じ大きさ。');

  pres.addSection({ title: '決まり / Rules' });
  s = pres.addSlide({ masterName: 'KM1 区切り / Section', sectionTitle: '決まり / Rules' });
  s.addText('01', { placeholder: 'number' }); s.addText('文字と色の決まり', { placeholder: 'title' });

  s = pres.addSlide({ masterName: 'KM1 題名と本文 / Title and content', sectionTitle: '決まり / Rules' });
  s.addText('1 枚に伝えることは 1 つ', { placeholder: 'title' });
  s.addText([
    t('題名は 28pt・太字。題名だけ読めば話の筋がわかる文にする', { bullet: true, breakLine: true }),
    en('Titles are 28pt bold, written so the titles alone tell the story'),
    t('本文は 20pt。補足と英語は 16pt。柱とページ番号だけ 12pt', { bullet: true, breakLine: true, paraSpaceBefore: S.lg }),
    en('Body 20pt; notes and English 16pt; only footers use 12pt'),
    t('大きさは KM1 の型の表の値だけ（68・40・28・20・16・12pt）', { bullet: true, breakLine: true, paraSpaceBefore: S.lg }),
    en('Only KM1 type-ramp sizes: 68, 40, 28, 20, 16 and 12pt'),
  ], { placeholder: 'body' });

  s = pres.addSlide({ masterName: 'KM1 2 段 / Two columns', sectionTitle: '決まり / Rules' });
  s.addText('使う形・使わない形', { placeholder: 'title' });
  s.addText([ t('使う', { bold: true, color: C.brand, breakLine: true }),
    t('題名・本文はプレースホルダーに入れる', { bullet: true, breakLine: true }),
    t('グラフは PowerPoint のグラフで作る', { bullet: true, breakLine: true }),
    t('図には代替テキストを付ける', { bullet: true }) ], { placeholder: 'left' });
  s.addText([ t('使わない', { bold: true, color: 'B10E1C', breakLine: true }),
    t('文字を画像にする', { bullet: true, breakLine: true }),
    t('色だけで区別する', { bullet: true, breakLine: true }),
    t('アニメーション・画面切り替えの効果', { bullet: true }) ], { placeholder: 'right' });

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: '決まり / Rules' });
  s.addText('大きな数字は 68pt で 1 つだけ', { placeholder: 'title' });
  const cw = (W - 2 * M - 2 * S.xxl) / 3;
  [['68pt', '数字 / Number'], ['28pt', '題名 / Title'], ['20pt', '本文 / Body']].forEach(([n, l], i) => {
    const x = M + i * (cw + S.xxl);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: PT(x), y: PT(L.bodyTop), w: PT(cw), h: PT(220), fill: { color: i === 0 ? C.tint : C.muted }, line: { type: 'none' }, rectRadius: PT(8), objectName: `card-${i + 1}` });
    s.addText(n, { x: PT(x + S.xxl), y: PT(L.bodyTop + S.xxl), w: PT(cw - 2 * S.xxl), h: PT(100), fontSize: i === 0 ? T.display : T.largeTitle, bold: true, color: i === 0 ? C.brand : C.ink, margin: 0, isTextBox: true, valign: 'top', lang: LANG, objectName: `num-${i + 1}` });
    s.addText(l, { x: PT(x + S.xxl), y: PT(L.bodyTop + 140), w: PT(cw - 2 * S.xxl), h: PT(56), fontSize: T.body, color: C.ink2, margin: 0, isTextBox: true, valign: 'top', lang: LANG, objectName: `label-${i + 1}` });
  });

  pres.addSection({ title: 'グラフと表 / Charts and tables' });
  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('グラフは値を書き込み、色だけに頼らない', { placeholder: 'title' });
  s.addChart(pres.charts.BAR, [{ name: '件数', labels: ['1 月', '2 月', '3 月', '4 月'], values: [12, 18, 15, 22] }], {
    x: PT(M), y: PT(L.bodyTop), w: PT(W - 2 * M), h: PT(L.bodyH), barDir: 'col',
    chartColors: ['10218B'], showValue: true, dataLabelPosition: 'outEnd', dataLabelColor: C.ink, dataLabelFontSize: T.small, dataLabelFontFace: '+mn-lt',
    catAxisLabelColor: C.ink2, valAxisLabelColor: C.ink2, catAxisLabelFontSize: T.small, valAxisLabelFontSize: T.small, catAxisLabelFontFace: '+mn-lt', valAxisLabelFontFace: '+mn-lt',
    valGridLine: { color: 'E0E0E0', size: 1 }, catGridLine: { style: 'none' }, showLegend: false,
    showTitle: false, altText: '月ごとの件数の棒グラフ。1 月 12 件、2 月 18 件、3 月 15 件、4 月 22 件。' });

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('系列は色と模様の両方で分ける', { placeholder: 'title' });
  s.addChart(pres.charts.BAR, [
    { name: '授業', labels: ['1 月', '2 月', '3 月'], values: [18, 16, 20] },
    { name: 'バイト', labels: ['1 月', '2 月', '3 月'], values: [12, 14, 10] },
    { name: 'サークル', labels: ['1 月', '2 月', '3 月'], values: [6, 8, 5] }], {
    x: PT(M), y: PT(L.bodyTop), w: PT(W - 2 * M), h: PT(L.bodyH), barDir: 'col', barGapWidthPct: 60,
    chartColors: ['10218B', 'BC4B09', '038387'], showValue: true, dataLabelPosition: 'outEnd', dataLabelColor: C.ink, dataLabelFontSize: T.small, dataLabelFontFace: '+mn-lt',
    catAxisLabelColor: C.ink2, valAxisLabelColor: C.ink2, catAxisLabelFontSize: T.small, valAxisLabelFontSize: T.small, catAxisLabelFontFace: '+mn-lt', valAxisLabelFontFace: '+mn-lt',
    valGridLine: { color: 'E0E0E0', size: 1 }, catGridLine: { style: 'none' }, showLegend: true, legendPos: 'b', legendFontSize: T.small, legendColor: C.ink, legendFontFace: '+mn-lt',
    showTitle: false, altText: '月ごとの時間の内訳の棒グラフ。授業は 1 月 18・2 月 16・3 月 20 時間、バイトは 12・14・10 時間、サークルは 6・8・5 時間。授業は塗り、バイトは横線、サークルは縦線の模様。' });
  s.addNotes('系列の塗りは KM1-COL-001 の順: 塗り → 横線 → 縦線。白黒で印刷しても区別できる。');

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('表は見出しの行を付け、セルを結合しない', { placeholder: 'title' });
  const hd = o => Object.assign({ bold: true, fill: { color: 'F0F0F0' }, color: C.ink, fontSize: T.small }, o || {});
  const cell = (v, o) => ({ text: v, options: Object.assign({ fontSize: T.small, color: C.ink }, o || {}) });
  s.addTable([
    [cell('項目', hd()), cell('大きさ', hd()), cell('使う場所', hd())],
    [cell('数字'), cell('68pt'), cell('1 枚に 1 つの大きな数字')],
    [cell('表紙・区切りの題名'), cell('40pt'), cell('表紙と章の区切り')],
    [cell('スライドの題名'), cell('28pt'), cell('すべてのスライド')],
    [cell('本文'), cell('20pt'), cell('箇条書き・説明')],
    [cell('補足・英語・表'), cell('16pt'), cell('英語の併記、表の中')],
    [cell('柱・ページ番号'), cell('12pt'), cell('下の端だけ')],
  ], { x: PT(M), y: PT(L.bodyTop), w: PT(W - 2 * M), colW: [PT(260), PT(160), PT(W - 2 * M - 420)], border: { type: 'solid', pt: 1, color: 'D1D1D1' }, rowH: PT(36), valign: 'middle', margin: [0, PT(S.md), 0, PT(S.md)], fontFace: FONT });

  pres.addSection({ title: 'まとめ / Summary' });
  s = pres.addSlide({ masterName: 'KM1 題名と本文 / Title and content', sectionTitle: 'まとめ / Summary' });
  s.addText('出す前に確かめること', { placeholder: 'title' });
  s.addText([
    t('officecheck.py で FAIL が 0（題名・大きさ・色・代替テキスト・言語）', { bullet: true, breakLine: true }),
    t('PowerPoint の「アクセシビリティ チェック」で問題が 0', { bullet: true, breakLine: true }),
    t('読み上げの順（オブジェクトの順）が見た目の順と同じ', { bullet: true, breakLine: true }),
    t('ファイルのプロパティに個人名が残っていない', { bullet: true }),
  ], { placeholder: 'body' });
  s.addNotes(KM1_NOTICE_JA + '\n' + KM1_NOTICE_EN);

  const f = path.join(OUT, 'KM1_スライド見本.pptx');
  await pres.writeFile({ fileName: f }); await applyTheme(f, THEME); await fixTheme(f);
  console.log('ok', f);
}
build().catch(e => { console.error(e); process.exit(1); });
