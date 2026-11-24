// KM1-DOC-002 Word のひな形と見本を作る / Build the KM1 Word template (.dotx) and sample (.docx)
// 使い方 / Usage: node km1_docx.js <出力フォルダ / out dir>
// 文字・余白・色は「PDF の規定」（documents.md）と同じ値。Word から PDF に書き出しても同じ見た目になる。
// Type, margins and colors match documents.md, so a Word-exported PDF looks like a KM1 PDF.
const fs = require('fs'), path = require('path');
const d = require('docx');
const JSZip = require(require.resolve('jszip', { paths: [path.dirname(require.resolve('docx'))] }));
const OUT = process.argv[2] || '.';
const FONT = '游ゴシック';
const F = { ascii: FONT, eastAsia: FONT, hAnsi: FONT, cs: FONT };
const MM = v => Math.round(v * 56.6929);                 // mm → twip
const PT = v => v * 2;                                   // pt → half-points
const LINE = r => Math.round(240 * r);                   // 行送りの倍率 / line-height multiple
const C = { ink: '242424', ink2: '616161', ink3: '616161', brand: '10218B', head: 'F0F0F0', rule: 'D1D1D1' };
const LANG = { value: 'ja-JP', eastAsia: 'ja-JP' };

// KM1 の表記（notices 2.1・2.6）。ひな形は本文に入れず、ノートかファイルの説明に入れる（使う人の文書に写らないように）
// KM1 notices 2.1 and 2.6; templates carry them in notes or file properties, never in the body
const KM1_NOTICE_JA = 'KM1 は個人が作ったデザイン標準です。Microsoft、セイコーエプソン、東京科学大学（Science Tokyo）、デジタル庁、そのほかの組織が作成・承認・推奨したものではなく、これらの組織とは関係がありません。名称・商標は各権利者のものです。KM1 は MIT License で公開しています。ライセンスの全文と著作権表示は https://github.com/kami2news/km1-design-system の LICENSE を参照してください。';
const KM1_NOTICE_EN = "KM1 is a personal design standard. It was not created, approved or endorsed by Microsoft, Seiko Epson, Institute of Science Tokyo, Japan's Digital Agency or any other organization, and is not affiliated with them. All names and trademarks belong to their owners. KM1 is released under the MIT License. See the LICENSE in https://github.com/kami2news/km1-design-system for the full text and copyright notice.";

const styles = {

  default: {
    document: { run: { font: F, size: PT(10), color: C.ink, language: LANG }, paragraph: { spacing: { line: LINE(1.7), before: 0, after: 120 } } },
    title: { run: { font: F, size: PT(28), bold: true, color: C.brand }, paragraph: { spacing: { before: 0, after: 240, line: LINE(1.3) }, keepNext: true } },
    heading1: { run: { font: F, size: PT(20), bold: true, color: C.brand }, paragraph: { pageBreakBefore: true, keepNext: true, spacing: { before: 0, after: 240, line: LINE(1.3) }, border: { bottom: { style: d.BorderStyle.SINGLE, size: 16, color: C.brand, space: 4 } } } },
    heading2: { run: { font: F, size: PT(13), bold: true, color: C.ink }, paragraph: { keepNext: true, spacing: { before: 360, after: 120, line: LINE(1.4) } } },
    heading3: { run: { font: F, size: PT(11), bold: true, color: C.ink }, paragraph: { keepNext: true, spacing: { before: 240, after: 80, line: LINE(1.7) } } },
    heading4: { run: { font: F, size: PT(10), bold: true, color: C.ink }, paragraph: { keepNext: true, spacing: { before: 200, after: 60, line: LINE(1.7) } } },
  },
  paragraphStyles: [
    { id: 'Subtitle', name: 'Subtitle', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: PT(13), color: C.ink2 }, paragraph: { spacing: { after: 480 } } },
    { id: 'KM1English', name: 'KM1 英語 / English', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: PT(9), color: C.ink3, language: { value: 'en-US' } }, paragraph: { spacing: { line: LINE(1.55), before: 0, after: 160 } } },
    { id: 'Caption', name: 'caption', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: PT(8.5), color: C.ink2 }, paragraph: { spacing: { before: 60, after: 240, line: LINE(1.55) } } },
    { id: 'KM1Table', name: 'KM1 表の文字 / Table text', basedOn: 'Normal', quickFormat: true, run: { size: PT(9) }, paragraph: { spacing: { before: 40, after: 40, line: LINE(1.55) } } },
    { id: 'KM1Meta', name: 'KM1 版と作成者 / Edition', basedOn: 'Normal', quickFormat: true, run: { size: PT(10), color: C.ink3 }, paragraph: { spacing: { after: 0 } } },
  ],
};
const numbering = { config: [
  { reference: 'km1-bullet', levels: [0, 1].map(l => ({ level: l, format: d.LevelFormat.BULLET, text: l ? '–' : '•', alignment: d.AlignmentType.LEFT, style: { paragraph: { indent: { left: 360 * (l + 1), hanging: 240 } } } })) },
  { reference: 'km1-num', levels: [{ level: 0, format: d.LevelFormat.DECIMAL, text: '%1.', alignment: d.AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
] };

// 表紙のしるし: PDF と同じ 22 × 6mm の紺の帯。文字を使わない塗りの段落なので読み上げに出ない
// Cover mark: the same 22 × 6mm navy bar as the PDF, drawn as paragraph shading (no text, nothing read aloud)
const MARK = () => new d.Paragraph({ spacing: { before: MM(30), after: MM(6), line: MM(6), lineRule: d.LineRuleType.EXACT },
  indent: { right: MM(210 - 34 - 22) }, shading: { type: d.ShadingType.CLEAR, color: 'auto', fill: C.brand }, children: [] });
const P = (text, o = {}) => new d.Paragraph(Object.assign({ children: [new d.TextRun(text)] }, o));
const EN = text => new d.Paragraph({ style: 'KM1English', children: [new d.TextRun(text)] });
const LI = (text, ref = 'km1-bullet') => new d.Paragraph({ numbering: { reference: ref, level: 0 }, children: [new d.TextRun(text)] });

function page(docName, date, children) {
  const W = MM(210 - 34);                                 // 本文の幅 / text width
  return {
    properties: { page: { size: { width: MM(210), height: MM(297) }, margin: { top: MM(20), bottom: MM(20), left: MM(17), right: MM(17), header: MM(10), footer: MM(10) } }, titlePage: true },
    headers: { default: new d.Header({ children: [new d.Paragraph({ style: 'KM1Meta', tabStops: [{ type: d.TabStopType.RIGHT, position: W }],
      children: [new d.TextRun({ text: docName, size: PT(8) }), new d.TextRun({ text: '\t' + date, size: PT(8) })] })] }),
      first: new d.Header({ children: [new d.Paragraph('')] }) },
    footers: { default: new d.Footer({ children: [new d.Paragraph({ alignment: d.AlignmentType.CENTER, children: [new d.TextRun({ children: [d.PageNumber.CURRENT], size: PT(8), color: C.ink3 })] })] }),
      first: new d.Footer({ children: [new d.Paragraph('')] }) },
    children };
}
function table(rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const b = { style: d.BorderStyle.SINGLE, size: 4, color: C.rule };
  return new d.Table({ width: { size: total, type: d.WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new d.TableRow({ tableHeader: i === 0, cantSplit: true, children: r.map((c, j) => new d.TableCell({
      width: { size: widths[j], type: d.WidthType.DXA }, borders: { top: b, bottom: b, left: b, right: b },
      shading: i === 0 ? { type: d.ShadingType.CLEAR, color: 'auto', fill: C.head } : undefined,
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      children: [new d.Paragraph({ style: 'KM1Table', children: [new d.TextRun({ text: c, bold: i === 0 })] })] })) })) });
}
// 言語ごとの補助の書体もゴシック系にする（KM1-TYP-001）/ make the per-script theme fonts sans too
const SCRIPT_SANS = { Hant: 'Microsoft JhengHei', Arab: 'Segoe UI', Hebr: 'Segoe UI', Viet: 'Segoe UI', Thai: 'Leelawadee UI', Khmr: 'Leelawadee UI', Laoo: 'Leelawadee UI',
  Geor: 'Segoe UI', Armn: 'Segoe UI', Cher: 'Gadugi', Cans: 'Gadugi', Ethi: 'Ebrima', Thaa: 'Nirmala UI', Uigh: 'Segoe UI',
  Syrc: 'Segoe UI Historic', Syre: 'Segoe UI Historic', Syrj: 'Segoe UI Historic', Syrn: 'Segoe UI Historic',
  Deva: 'Nirmala UI', Beng: 'Nirmala UI', Gujr: 'Nirmala UI', Guru: 'Nirmala UI', Knda: 'Nirmala UI', Mlym: 'Nirmala UI', Orya: 'Nirmala UI', Taml: 'Nirmala UI', Telu: 'Nirmala UI', Sinh: 'Nirmala UI' };
function sansScripts(x) {
  return x.replace(/<a:font script="([A-Za-z]+)" typeface="[^"]*"\/>/g, (m, s) => SCRIPT_SANS[s] ? `<a:font script="${s}" typeface="${SCRIPT_SANS[s]}"/>` : m);
}
// テーマを KM1 にする（色・書体）/ Make the Office theme KM1 (colors and fonts)
const THEME = { dk1: '242424', lt1: 'FFFFFF', dk2: '10218B', lt2: 'F5F5F5', accent1: '10218B', accent2: '0F6CBD', accent3: '038387', accent4: 'BC4B09', accent5: '5C2E91', accent6: '107C10', hlink: '10218B', folHlink: '5C2E91' };
function km1Theme(x) {
  for (const [k, v] of Object.entries(THEME)) x = x.replace(new RegExp(`(<a:${k}>)[\\s\\S]*?(</a:${k}>)`), `$1<a:srgbClr val="${v}"/>$2`);
  x = x.replace(/<a:latin typeface="[^"]*"( panose="[^"]*")?\/>/g, `<a:latin typeface="${FONT}"/>`)
       .replace(/<a:ea typeface="[^"]*"\/>/g, `<a:ea typeface="${FONT}"/>`)
       .replace(/<a:font script="Jpan" typeface="[^"]*"\/>/g, `<a:font script="Jpan" typeface="${FONT}"/>`)
       .replace(/<a:clrScheme name="[^"]*"/, '<a:clrScheme name="KM1"').replace(/<a:fontScheme name="[^"]*"/, '<a:fontScheme name="KM1"');
  return sansScripts(x);
}
async function finish(doc, file, template) {
  const buf = await d.Packer.toBuffer(doc);
  const z = await JSZip.loadAsync(buf), o = new JSZip();
  for (const [n, f] of Object.entries(z.files)) {
    if (f.dir) continue;
    let data = await f.async('nodebuffer');
    if (template && n === '[Content_Types].xml') data = Buffer.from(data.toString().replace('wordprocessingml.document.main+xml', 'wordprocessingml.template.main+xml'));
    if (/theme\/theme\d+\.xml$/.test(n)) data = Buffer.from(km1Theme(data.toString()));
    if (n === 'word/styles.xml') data = Buffer.from(data.toString().replace(/w:val="0563C1"/g, `w:val="${C.brand}"`).replace(/w:val="(2E74B5|1F4D78)"/g, `w:val="${C.ink}"`));
    if (n === 'word/settings.xml') data = Buffer.from(data.toString().replace('</w:settings>', '<w:themeFontLang w:val="ja-JP" w:eastAsia="ja-JP"/></w:settings>'));
    o.file(n, data, { createFolders: false });
  }
  fs.writeFileSync(file, await o.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}
function makeDoc(title, sections, description) {
  return new d.Document({ title, subject: 'KM1-DOC-002', creator: '', lastModifiedBy: '', description: description || '', styles, numbering, features: { updateFields: false }, sections });
}

(async () => {
  const W = MM(210 - 34);
  // 1) ひな形 / template
  await finish(makeDoc('KM1 文書のひな形 / KM1 document template', [page('文書名 / Document name', 'YYYY-MM-DD', [
    MARK(),
    new d.Paragraph({ heading: d.HeadingLevel.TITLE, children: [new d.TextRun('文書の題名 / Title')] }),
    new d.Paragraph({ style: 'Subtitle', children: [new d.TextRun('副題 / Subtitle')] }),
    new d.Paragraph({ style: 'KM1Meta', children: [new d.TextRun('YYYY-MM-DD・作成者 / Author')] }),
    new d.Paragraph({ heading: d.HeadingLevel.HEADING_1, children: [new d.TextRun('1. 章の題名 / Chapter')] }),
    P('本文 / Body'), EN('English line'),
  ])], KM1_NOTICE_JA + ' ' + KM1_NOTICE_EN), path.join(OUT, 'KM1_文書.dotx'), true);

  // 2) 見本 / sample
  const date = '2026-11-13', name = 'KM1 文書の規定 見本';
  const kids = [
    MARK(),
    new d.Paragraph({ heading: d.HeadingLevel.TITLE, children: [new d.TextRun('KM1 文書の規定')] }),
    new d.Paragraph({ style: 'Subtitle', children: [new d.TextRun('Word のひな形の使い方の見本 / How to use the KM1 Word template')] }),
    new d.Paragraph({ style: 'KM1Meta', children: [new d.TextRun(date + '・KM1')] }),

    new d.Paragraph({ heading: d.HeadingLevel.HEADING_1, children: [new d.TextRun('1. 文字 / Type')] }),
    P('本文は 10pt、行送り 1.7。見出しは Word の「見出し 1」〜「見出し 4」のスタイルだけを使い、文字を太くして見出しの代わりにしない。'),
    EN('Body is 10pt with 1.7 leading. Use only the built-in Heading 1–4 styles; never fake headings with bold text.'),
    new d.Paragraph({ heading: d.HeadingLevel.HEADING_2, children: [new d.TextRun('1.1 大きさの表 / Size table')] }),
    table([['役割 / Role', '大きさ / Size', 'スタイル / Style'],
      ['表紙の題名', '28pt・太字・紺', '表題 / Title'],
      ['章（大見出し）', '20pt・太字・紺、下に 2pt の線', '見出し 1 / Heading 1'],
      ['節（中見出し）', '13pt・太字', '見出し 2 / Heading 2'],
      ['小見出し', '11pt・10pt・太字', '見出し 3・4'],
      ['本文', '10pt', '標準 / Normal'],
      ['英語の併記', '9pt・#616161', 'KM1 英語 / English'],
      ['表の中', '9pt', 'KM1 表の文字'],
      ['図の説明・柱・ページ番号', '8〜8.5pt', '図表番号 / caption']], [MM(56), MM(60), W - MM(116)]),
    new d.Paragraph({ style: 'Caption', children: [new d.TextRun('表 1　KM1 の Word の文字の大きさ / Table 1. Type sizes in KM1 Word documents')] }),
    new d.Paragraph({ heading: d.HeadingLevel.HEADING_2, children: [new d.TextRun('1.2 箇条書き / Lists')] }),
    LI('箇条書きは Word の箇条書きの機能で作る。「・」を手で打たない。'),
    LI('手順は番号付きの箇条書きにする。'),
    EN('Make lists with Word list formatting, never typed bullets; use numbered lists for procedures.'),

    new d.Paragraph({ heading: d.HeadingLevel.HEADING_1, children: [new d.TextRun('2. 出す前に / Before sharing')] }),
    LI('officecheck.py で FAIL が 0 になるまで直す。', 'km1-num'),
    LI('Word の「アクセシビリティ チェック」で問題を 0 にする。', 'km1-num'),
    LI('ファイルのプロパティ（作成者・題名）を確かめる。', 'km1-num'),
    LI('PDF にするときは「名前を付けて保存」で PDF を選ぶ（PDF の規定 §8）。', 'km1-num'),
    EN('Run officecheck.py to zero FAILs, clear Word\'s Accessibility Checker, check file properties, and export PDFs with Save As (PDF rules §8).'),
    new d.Paragraph({ heading: d.HeadingLevel.HEADING_1, children: [new d.TextRun('KM1 について / About KM1')] }),
    P(KM1_NOTICE_JA),
    EN(KM1_NOTICE_EN),
  ];
  await finish(makeDoc('KM1 文書の規定 見本 / KM1 document rules sample', [page(name, date, kids)], KM1_NOTICE_JA + ' ' + KM1_NOTICE_EN), path.join(OUT, 'KM1_文書見本.docx'), false);
  console.log('ok');
})().catch(e => { console.error(e); process.exit(1); });
