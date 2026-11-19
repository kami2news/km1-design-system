// KM1-DOC-003 スライドのひな形と見本を作る / Build the KM1 slide template (.potx) and sample deck (.pptx)
// 使い方 / Usage: node km1_pptx.js <出力フォルダ / out dir>
// 寸法は 1pt ＝ KM1 の 1px として、KM1 のトークンの値をそのまま使う（16:9、960 × 540pt）。
// Sizes use KM1 token values with 1pt = 1px on a 960 × 540pt (16:9) slide.
const pptxgen = require('pptxgenjs');
const fs = require('fs'), path = require('path'), JSZip = require(require.resolve('jszip', {paths: [path.dirname(require.resolve('pptxgenjs'))]}));
const OUT = process.argv[2] || '.';
const PT = v => v / 72;                       // pt → inch
const FONT = '游ゴシック';                      // 和文・英数字とも / both scripts (office.md §2)
// 文字の大きさと行送り（KM1 の型の表の値。行送りもトークンの lineHeight）/ sizes and line heights from the KM1 type ramp
const T = { display: 68, largeTitle: 40, title1: 32, body: 24, small: 20, caption: 14 };
const LH = { 68: 92, 40: 52, 32: 40, 24: 32, 20: 28, 14: 20 };
const S = { xs: 4, sm: 8, md: 12, lg: 16, xl: 20, xxl: 24, xxxl: 32 };   // spacing tokens
// 画面の割り付け（office.md §4.2）。1pt ＝ 1px、どれも 8 の倍数か KM1 の余白のトークン
// Slide grid (office.md §4.2); 1pt = 1px, every value is a multiple of 8 or a KM1 spacing token
const W = 960, H = 540;
const G = {
  side: 48,             // 左右の余白 / side margins = space-xxxl + space-lg
  top: 40,              // 上の余白 / top margin = space-xxxl + space-sm
  titleH: 40,           // 題名の行（32pt を 1 行）/ title row, one line of 32pt
  gap: S.xxl,           // 題名と本文、本文と柱の間、列の間 24 / title-body, body-footer and column gutter
  col: 50, cols: 12,    // 12 列。列 50 ＋ 溝 24 ＝ 74 / 12 columns of 50 with 24 gutters
  footH: 20, bottom: 24 // 柱の行（14pt を 1 行）と下の余白 / footer row and bottom margin
};
G.contentW = W - 2 * G.side;                       // 864
G.bodyTop = G.top + G.titleH + G.gap;              // 104
G.footTop = H - G.bottom - G.footH;                // 496
G.bodyBottom = G.footTop - G.gap;                  // 472
G.bodyH = G.bodyBottom - G.bodyTop;                // 368
G.rowH = (G.bodyH - G.gap) / 2;                    // 172（本文を上下 2 段にするとき / two body rows）
const colX = i => G.side + i * (G.col + G.gap);    // i 列目の左端 / left edge of column i (0-11)
const spanW = n => n * G.col + (n - 1) * G.gap;    // n 列ぶんの幅 / width of n columns
const M = G.side;
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
    { text: { text: docName, options: { x: PT(G.side), y: PT(G.footTop), w: PT(spanW(8)), h: PT(G.footH), fontSize: T.caption, color: C.ink3, fontFace: FONT, margin: 0, valign: 'middle', lang: LANG } } },
  ];
  const num = { x: PT(colX(10)), y: PT(G.footTop), w: PT(spanW(2)), h: PT(G.footH), fontSize: T.caption, color: C.ink3, fontFace: FONT, align: 'right', valign: 'middle' };
  const body = (name, x, w, text) => ({ placeholder: { options: { name, type: 'body', x: PT(x), y: PT(G.bodyTop), w: PT(w), h: PT(G.bodyH), fontSize: T.body, lineSpacing: LH[T.body], paraSpaceAfter: S.md, color: C.ink, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text } });
  // 表紙: しるし・題名・副題を本文の領域の中で上から置き、版の日付は柱の行の上 / cover blocks stack inside the body area
  pres.defineSlideMaster({ title: 'KM1 表紙 / Title', background: { color: 'FFFFFF' },
    objects: [
      { rect: { x: PT(G.side), y: PT(152), w: PT(62), h: PT(17), fill: { color: C.brand }, line: { type: 'none' } } },  // 表紙のしるし（PDF と同じ 22 × 6mm）
      { placeholder: { options: { name: 'title', type: 'title', x: PT(G.side), y: PT(184), w: PT(spanW(10)), h: PT(2 * LH[40]), fontSize: T.largeTitle, lineSpacing: LH[40], bold: true, color: C.brand, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG }, text: '題名 / Title' } },
      { placeholder: { options: { name: 'subtitle', type: 'body', x: PT(G.side), y: PT(184 + 2 * LH[40] + S.xxl), w: PT(spanW(10)), h: PT(2 * LH[24]), fontSize: T.body, lineSpacing: LH[24], color: C.ink2, fontFace: FONT, valign: 'top', margin: 0, lang: LANG }, text: '副題 / Subtitle' } },
      { placeholder: { options: { name: 'meta', type: 'body', x: PT(G.side), y: PT(G.bodyBottom - LH[20]), w: PT(spanW(8)), h: PT(LH[20]), fontSize: T.small, color: C.ink3, fontFace: FONT, valign: 'bottom', margin: 0, lang: LANG }, text: '版の日付・作成者 / Date, author' } },
    ] });
  pres.defineSlideMaster({ title: 'KM1 区切り / Section', background: { color: C.muted },
    objects: [
      { placeholder: { options: { name: 'number', type: 'body', x: PT(G.side), y: PT(184), w: PT(spanW(4)), h: PT(LH[24]), fontSize: T.body, bold: true, color: C.brand, fontFace: FONT, margin: 0, lang: LANG }, text: '01' } },
      { placeholder: { options: { name: 'title', type: 'title', x: PT(G.side), y: PT(184 + LH[24] + S.lg), w: PT(spanW(10)), h: PT(2 * LH[40]), fontSize: T.largeTitle, lineSpacing: LH[40], bold: true, color: C.ink, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG }, text: '章の題名 / Section title' } },
      ...foot ], slideNumber: num });
  const titleBox = { name: 'title', type: 'title', x: PT(G.side), y: PT(G.top), w: PT(G.contentW), h: PT(G.titleH), fontSize: T.title1, lineSpacing: LH[32], bold: true, color: C.ink, fontFace: FONT, valign: 'top', align: 'left', margin: 0, lang: LANG };
  const title = { placeholder: { options: titleBox, text: 'スライドの題名 / Slide title' } };
  pres.defineSlideMaster({ title: 'KM1 題名と本文 / Title and content', background: { color: 'FFFFFF' },
    objects: [ title, body('body', G.side, G.contentW, '本文 / Body'), ...foot ], slideNumber: num });
  pres.defineSlideMaster({ title: 'KM1 2 段 / Two columns', background: { color: 'FFFFFF' },
    objects: [ title, body('left', colX(0), spanW(6), '左 / Left'), body('right', colX(6), spanW(6), '右 / Right'), ...foot ], slideNumber: num });
  pres.defineSlideMaster({ title: 'KM1 図と説明 / Figure and text', background: { color: 'FFFFFF' },
    objects: [ title, body('text', colX(8), spanW(4), '説明 / Text'), ...foot ], slideNumber: num });
  pres.defineSlideMaster({ title: 'KM1 題名だけ / Title only', background: { color: 'FFFFFF' },
    objects: [ title, ...foot ], slideNumber: num });
  return G;
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
  const MAP = { 4400: 3200, 3200: 2400, 2800: 2000, 2400: 2000, 1800: 2000 };
  for (const n of Object.keys(z.files).filter(n => /slideMasters\/slideMaster\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    x = x.replace(/sz="(4400|3200|2800|2400|1800)"/g, (m, v) => `sz="${MAP[v]}"`);
    z.file(n, x);
  }
  // グラフの系列に模様を付ける（KM1-COL-001、office.md §4.5）。Office の既定の模様（pattFill）は細かすぎて映すと
  // にごった色にしか見えないので、km1_patterns.py で作った画像（間隔 12pt・線 4pt）を並べて塗る。
  // 系列 0 は塗り、1 は横線、2 は縦線、3 は斜線、4 は格子、5 は斜め格子、6 は点、7 は市松。
  // Pattern fills for chart series: picture tiles from km1_patterns.py instead of the tiny Office presets.
  const ORDER = ['solid', 'horizontal', 'vertical', 'diagonal', 'grid', 'crosshatch', 'dots', 'checker'];
  const PATDIR = path.join(__dirname, 'patterns');
  let ct = await z.file('[Content_Types].xml').async('string');
  if (!/Extension="png"/.test(ct)) { ct = ct.replace('<Default ', '<Default Extension="png" ContentType="image/png"/><Default '); z.file('[Content_Types].xml', ct); }
  for (const n of Object.keys(z.files).filter(n => /charts\/chart\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string');
    const sers = x.match(/<c:ser>[\s\S]*?<\/c:ser>/g) || [];
    if (sers.length < 2) continue;
    const relN = n.replace(/charts\/(chart\d+\.xml)$/, 'charts/_rels/$1.rels');
    let rels = z.file(relN) ? await z.file(relN).async('string')
      : '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"></Relationships>';
    sers.forEach((ser, i) => {
      const p = ORDER[i % ORDER.length]; if (p === 'solid') return;
      const m = ser.match(/<c:spPr><a:solidFill><a:srgbClr val="([0-9A-Fa-f]{6})"\/><\/a:solidFill>/); if (!m) return;
      const col = m[1].toUpperCase(), file = `km1-pattern-${ORDER.indexOf(p) + 1}-${p}-${col}.png`;
      const src = path.join(PATDIR, file);
      if (!fs.existsSync(src)) throw new Error(`模様の画像がない / missing tile ${file}（python3 km1_patterns.py patterns）`);
      z.file(`ppt/media/${file}`, fs.readFileSync(src));
      const rid = `rIdKm1Pat${i}`;
      if (!rels.includes(`Id="${rid}"`)) rels = rels.replace('</Relationships>', `<Relationship Id="${rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/${file}"/></Relationships>`);
      const fill = `<c:spPr><a:blipFill rotWithShape="0"><a:blip r:embed="${rid}"/><a:srcRect/><a:tile tx="0" ty="0" sx="100000" sy="100000" flip="none" algn="tl"/></a:blipFill><a:ln w="9525"><a:solidFill><a:srgbClr val="616161"/></a:solidFill></a:ln>`;
      x = x.replace(ser, ser.replace(m[0], fill));
    });
    z.file(n, x); z.file(relN, rels);
  }
  for (const n of Object.keys(z.files).filter(n => /charts\/chart\d+\.xml$/.test(n))) {   // 軸の線を KM1 の色に / axis lines in a KM1 color
    z.file(n, (await z.file(n).async('string')).replace(/val="888888"/g, 'val="616161"'));
  }
  // 見本の模様の図形（名前が km1pat-<模様>-<色>）を画像の並べ塗りにする / tile-fill shapes named km1pat-*
  for (const n of Object.keys(z.files).filter(n => /slides\/slide\d+\.xml$/.test(n))) {
    let x = await z.file(n).async('string'); if (!x.includes('name="km1pat-')) continue;
    const relN = n.replace(/slides\/(slide\d+\.xml)$/, 'slides/_rels/$1.rels'); let rels = await z.file(relN).async('string'); let k = 0;
    x = x.replace(/(<p:sp>(?:(?!<\/p:sp>)[\s\S])*?name="km1pat-([a-z]+)-([0-9A-F]{6})"[\s\S]*?)<a:solidFill><a:srgbClr val="[0-9A-Fa-f]{6}"\/><\/a:solidFill>/g, (m, head, p, col) => {
      if (p === 'solid') return m;
      const file = `km1-pattern-${ORDER.indexOf(p) + 1}-${p}-${col}.png`, rid = `rIdKm1Sw${k++}`;
      z.file(`ppt/media/${file}`, fs.readFileSync(path.join(PATDIR, file)));
      rels = rels.replace('</Relationships>', `<Relationship Id="${rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/${file}"/></Relationships>`);
      return `${head}<a:blipFill rotWithShape="0"><a:blip r:embed="${rid}"/><a:srcRect/><a:tile tx="0" ty="0" sx="100000" sy="100000" flip="none" algn="tl"/></a:blipFill>`;
    });
    z.file(n, x); z.file(relN, rels);
  }
  let p = await z.file('ppt/presentation.xml').async('string');
  z.file('ppt/presentation.xml', p.replace(/sz="1800"/g, 'sz="2400"'));
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
  layouts(pres, 'KM1 スライドの規定 見本');
  const t = (s, o = {}) => ({ text: s, options: Object.assign({ lang: LANG }, o) });
  const en = (s, o = {}) => t(s, Object.assign({ fontSize: T.small, lineSpacing: LH[20], color: C.ink3, breakLine: true }, o));
  const li = (s, o = {}) => t(s, Object.assign({ bullet: true, breakLine: true, paraSpaceBefore: S.lg, paraSpaceAfter: 0 }, o));
  const card = (s, x, y, w, h, fill, name) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: PT(x), y: PT(y), w: PT(w), h: PT(h), fill: { color: fill }, line: { type: 'none' }, rectRadius: PT(8), objectName: name });
  const box = (s, text, x, y, w, h, o) => s.addText(text, Object.assign({ x: PT(x), y: PT(y), w: PT(w), h: PT(h), margin: 0, isTextBox: true, valign: 'top', fontFace: FONT, lang: LANG }, o));
  const PAD = S.xxl;                                  // カードの内側（spacious）/ card padding

  pres.addSection({ title: '表紙 / Cover' });
  let s = pres.addSlide({ masterName: 'KM1 表紙 / Title', sectionTitle: '表紙 / Cover' });
  s.addText('KM1 スライドの規定', { placeholder: 'title' });
  s.addText('ひな形の使い方の見本 / How to use the KM1 slide template', { placeholder: 'subtitle' });
  s.addText('2026-11-19・KM1', { placeholder: 'meta' });
  s.addNotes('表紙。題名は 40pt・太字・ブランドの紺。しるしは PDF の表紙と同じ大きさ。');

  pres.addSection({ title: '決まり / Rules' });
  s = pres.addSlide({ masterName: 'KM1 区切り / Section', sectionTitle: '決まり / Rules' });
  s.addText('01', { placeholder: 'number' }); s.addText('文字と余白の決まり', { placeholder: 'title' });

  s = pres.addSlide({ masterName: 'KM1 題名と本文 / Title and content', sectionTitle: '決まり / Rules' });
  s.addText('文字は 20pt 以上、本文は 24pt', { placeholder: 'title' });
  s.addText([
    li('題名は 32pt・太字・1 行。題名だけ読めば話の筋がわかる文にする', { paraSpaceBefore: 0 }),
    en('Titles: 32pt bold, one line, so the titles alone tell the story'),
    li('本文は 24pt。補足・英語・表・グラフは 20pt'),
    en('Body 24pt; notes, English, tables and charts 20pt'),
    li('柱とスライド番号だけ 14pt。内容の文字は 20pt より小さくしない'),
    en('Only the footer and slide number are 14pt; no content below 20pt'),
  ], { placeholder: 'body' });

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: '決まり / Rules' });
  s.addText('余白と 12 列のグリッド', { placeholder: 'title' });
  for (let i = 0; i < G.cols; i++) card(s, colX(i), G.bodyTop, G.col, G.bodyH, C.tint, `col-${i + 1}`);
  const lh = 3 * LH[24], bh = lh + 2 * PAD, by = G.bodyTop + (G.bodyH - bh) / 2;   // 中の文字に合わせた白いカード / white card sized to its text
  card(s, colX(2), by, spanW(8), bh, 'FFFFFF', 'grid-card');
  box(s, [t('左右 48・上 40・題名 40・間 24', { breakLine: true, bold: true }), t('本文 864 × 368、列 50・溝 24', { breakLine: true }), t('下は柱 20・余白 24')],
    colX(2) + PAD, by + PAD, spanW(8) - 2 * PAD, lh, { fontSize: T.body, lineSpacing: LH[24], color: C.ink, objectName: 'grid-label' });
  s.addNotes('薄い紺の帯が 12 列。図・表・カードの左右の端は、どれかの列の端にそろえる。');

  s = pres.addSlide({ masterName: 'KM1 2 段 / Two columns', sectionTitle: '決まり / Rules' });
  s.addText('使う形・使わない形', { placeholder: 'title' });
  s.addText([ t('使う', { bold: true, color: C.brand, breakLine: true, paraSpaceAfter: 0 }),
    li('題名・本文はプレースホルダーに入れる'),
    li('グラフは PowerPoint のグラフで作る'),
    li('図・表・カードは列の端にそろえる', { breakLine: false }) ], { placeholder: 'left' });
  s.addText([ t('使わない', { bold: true, color: 'B10E1C', breakLine: true, paraSpaceAfter: 0 }),
    li('文字を画像にする'),
    li('色だけで区別する'),
    li('縮めて詰め込む（2 枚に分ける）', { breakLine: false }) ], { placeholder: 'right' });

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: '決まり / Rules' });
  s.addText('大きな数字は 68pt で 1 つだけ', { placeholder: 'title' });
  [['68pt', '数字 / Number', '1 枚に 1 つ'], ['32pt', '題名 / Title', '1 行で'], ['24pt', '本文 / Body', '6 項目まで']].forEach(([n, l, d], i) => {
    const x = colX(i * 4), w = spanW(4);
    card(s, x, G.bodyTop, w, G.bodyH, i === 0 ? C.tint : C.muted, `card-${i + 1}`);
    box(s, n, x + PAD, G.bodyTop + PAD, w - 2 * PAD, LH[i === 0 ? 68 : 40], { fontSize: i === 0 ? T.display : T.largeTitle, bold: true, color: i === 0 ? C.brand : C.ink, objectName: `num-${i + 1}` });
    box(s, [t(l, { breakLine: true, bold: true }), t(d, { color: C.ink2 })], x + PAD, G.bodyBottom - PAD - 2 * LH[24], w - 2 * PAD, 2 * LH[24],
      { fontSize: T.body, lineSpacing: LH[24], color: C.ink, valign: 'bottom', objectName: `label-${i + 1}` });
  });
  s.addNotes('カードは本文の領域の高さいっぱい（368）。数字は上、説明は下にそろえ、間を空ける。');

  pres.addSection({ title: 'グラフと表 / Charts and tables' });
  const chartOpt = { barDir: 'col', showValue: true, dataLabelPosition: 'outEnd', dataLabelColor: C.ink, dataLabelFontSize: T.small, dataLabelFontFace: '+mn-lt',
    catAxisLabelColor: C.ink2, valAxisLabelColor: C.ink2, catAxisLabelFontSize: T.small, valAxisLabelFontSize: T.small, catAxisLabelFontFace: '+mn-lt', valAxisLabelFontFace: '+mn-lt',
    valGridLine: { color: 'E0E0E0', size: 1 }, catGridLine: { style: 'none' }, showTitle: false };
  s = pres.addSlide({ masterName: 'KM1 図と説明 / Figure and text', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('4 月は 1 月の 2 倍近くに増えた', { placeholder: 'title' });
  s.addChart(pres.charts.BAR, [{ name: '件数', labels: ['1 月', '2 月', '3 月', '4 月'], values: [12, 18, 15, 22] }], Object.assign({}, chartOpt, {
    x: PT(colX(0)), y: PT(G.bodyTop), w: PT(spanW(8)), h: PT(G.bodyH), chartColors: ['10218B'], showLegend: false,
    altText: '月ごとの件数の棒グラフ。1 月 12 件、2 月 18 件、3 月 15 件、4 月 22 件。' }));
  s.addText([ t('値は棒の上に書き込む', { bullet: true, breakLine: true }), t('言いたいことは題名に書く', { bullet: true, breakLine: true }),
    t('図は左の 8 列、説明は右の 4 列', { bullet: true }) ], { placeholder: 'text' });

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('模様は 8 つ、系列の順にこの順で使う', { placeholder: 'title' });
  [['solid', '1 塗り'], ['horizontal', '2 横線'], ['vertical', '3 縦線'], ['diagonal', '4 斜線'], ['grid', '5 格子'], ['crosshatch', '6 斜め格子'], ['dots', '7 点'], ['checker', '8 市松']].forEach(([p, l], i) => {
    const x = colX((i % 4) * 3), y = G.bodyTop + Math.floor(i / 4) * (G.rowH + G.gap), w = spanW(3), sh = G.rowH - LH[20] - S.sm;
    s.addShape(pres.shapes.RECTANGLE, { x: PT(x), y: PT(y), w: PT(w), h: PT(sh), fill: { color: C.brand }, line: { color: C.ink3, width: 0.75 }, objectName: `km1pat-${p}-${C.brand}` });
    box(s, l, x, y + sh + S.sm, w, LH[20], { fontSize: T.small, color: C.ink, objectName: `patlabel-${i + 1}` });
  });
  s.addNotes('模様の画像は office/patterns（km1_patterns.py で作る）。グラフの系列は「塗りつぶし（図またはテクスチャ）› 画像をテクスチャとして並べる」で、拡大縮小 100%。');

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('系列は色と模様の両方で分ける', { placeholder: 'title' });
  s.addChart(pres.charts.BAR, [
    { name: '授業', labels: ['1 月', '2 月', '3 月'], values: [18, 16, 20] },
    { name: 'バイト', labels: ['1 月', '2 月', '3 月'], values: [12, 14, 10] },
    { name: 'サークル', labels: ['1 月', '2 月', '3 月'], values: [6, 8, 5] }], Object.assign({}, chartOpt, {
    x: PT(G.side), y: PT(G.bodyTop), w: PT(G.contentW), h: PT(G.bodyH), barGapWidthPct: 60,
    chartColors: ['10218B', 'BC4B09', '038387'], showLegend: true, legendPos: 'b', legendFontSize: T.small, legendColor: C.ink, legendFontFace: '+mn-lt',
    altText: '月ごとの時間の内訳の棒グラフ。授業は 1 月 18・2 月 16・3 月 20 時間、バイトは 12・14・10 時間、サークルは 6・8・5 時間。授業は塗り、バイトは横線、サークルは縦線の模様。' }));
  s.addNotes('系列の塗りは KM1-COL-001 の順: 塗り → 横線 → 縦線。白黒で印刷しても区別できる。');

  s = pres.addSlide({ masterName: 'KM1 題名だけ / Title only', sectionTitle: 'グラフと表 / Charts and tables' });
  s.addText('表は見出しの行を付け、セルを結合しない', { placeholder: 'title' });
  const hd = o => Object.assign({ bold: true, fill: { color: 'F0F0F0' }, color: C.ink, fontSize: T.small }, o || {});
  const cell = (v, o) => ({ text: v, options: Object.assign({ fontSize: T.small, color: C.ink }, o || {}) });
  const rows = [
    [cell('役割', hd()), cell('大きさ', hd()), cell('使う場所', hd())],
    [cell('大きな数字'), cell('68pt'), cell('1 枚に 1 つ')],
    [cell('表紙・区切りの題名'), cell('40pt'), cell('表紙と章の区切り')],
    [cell('スライドの題名'), cell('32pt'), cell('すべてのスライド、1 行')],
    [cell('本文'), cell('24pt'), cell('箇条書き・説明')],
    [cell('補足・英語・表・グラフ'), cell('20pt'), cell('内容の文字の最小')],
    [cell('柱・スライド番号'), cell('14pt'), cell('下の柱の行だけ')],
  ];
  const rh = G.bodyH / 8;                              // 46 ＝ 本文の高さを 8 行で割る / body height in 8 rows
  s.addTable(rows, { x: PT(G.side), y: PT(G.bodyTop), w: PT(G.contentW), colW: [PT(4 * (G.col + G.gap)), PT(2 * (G.col + G.gap)), PT(spanW(6))],   // 列の境目を列の頭にそろえる / boundaries on column starts
    border: { type: 'solid', pt: 1, color: 'D1D1D1' }, rowH: PT(rh), valign: 'middle', margin: [0, PT(S.lg), 0, PT(S.lg)], fontFace: FONT });

  pres.addSection({ title: 'まとめ / Summary' });
  s = pres.addSlide({ masterName: 'KM1 題名と本文 / Title and content', sectionTitle: 'まとめ / Summary' });
  s.addText('出す前に確かめること', { placeholder: 'title' });
  s.addText([
    li('officecheck.py で FAIL が 0（大きさ・グリッド・はみ出し・題名の長さ）', { paraSpaceBefore: 0 }),
    li('PowerPoint の「アクセシビリティ チェック」で問題が 0'),
    li('読み上げの順（オブジェクトの順）が見た目の順と同じ'),
    li('ファイルのプロパティに個人名が残っていない', { breakLine: false }),
  ], { placeholder: 'body' });
  s.addNotes(KM1_NOTICE_JA + '\n' + KM1_NOTICE_EN);

  const f = path.join(OUT, 'KM1_スライド見本.pptx');
  await pres.writeFile({ fileName: f }); await applyTheme(f, THEME); await fixTheme(f);
  console.log('ok', f);
}
build().catch(e => { console.error(e); process.exit(1); });
