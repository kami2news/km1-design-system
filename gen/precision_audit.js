// 精度の監査: 描画した見本の全要素から、実際に効いている値を取り出して KM1 の決まりと照らす。
// Precision audit: read computed values from every rendered preview element and compare them with KM1's rules.
//
//   node gen/precision_audit.js /tmp/rc [--json=out.json] [--only=Name,Name] [--width=1280,375]
//   既定は PC（1280）・タブレット（768）・スマホ（375）の 3 つの幅で測る / desktop, tablet and phone widths by default
//
// 見るもの / Checks
//   TYPE   文字の大きさ・行の高さの組が型の表にない / size + line-height pair not in the type ramp
//   WRAP   2 行以上に折り返した文（見出しを除く）の行の高さが 1.5 倍未満 / wrapped body text below 1.5x (D23)
//   SQUEEZE 12 字以下の短い文字が折り返す（入れ物が狭すぎる）/ short text wraps: the box is too narrow
//   SMALL  12 px 未満の文字 / text below 12px
//   WEIGHT 400・600 以外の太さ / weight other than 400 and 600
//   COLOR  文字色が色トークンにない / text colour not a token
//   SPACE  余白（padding・margin・gap）が余白の段にない / spacing value not on the spacing scale
//   MEASURE 折り返した文の 1 行が 40em を超える / wrapped text wider than 40em (D23)
//   RADIUS 角丸が角丸の段にない / corner radius not on the radius scale
//   BORDER 縁の太さが 1・2・4px 以外 / border width other than 1, 2, 4px
//   FONT   書体が KM1 の書体の並び（sans・mono）で始まらない / font stack not KM1's sans or mono
//   TARGET 押せるものが 24px 四方に満たない（WCAG 2.5.8。行の中の文のリンクは除く）/ pressable target under 24px
//   OVERLAP 押せる範囲どうしが重なる（親子は除く）/ pressable areas overlap
//   GAP    同じまとまりの中で、並ぶものの間隔が 0.5〜3px だけ違う（そろえそこない）/ near-equal gaps within one group
//   CLIP   文字が箱からはみ出して切れているのに「…」が出ない / text clipped without an ellipsis
//   EDGE   1 つの領域の中で、文字の左端が 2px 未満ずれて並ぶ（そろえそこない）/ near-miss left edges (<2px apart)
'use strict';
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER || 'puppeteer-core');
const ROOT = path.resolve(__dirname, '..');
const DIR = path.resolve(process.argv[2] || '/tmp/rc');
const arg = k => (process.argv.find(a => a.startsWith(`--${k}=`)) || '').slice(k.length + 3);
const ONLY = arg('only') ? arg('only').split(',') : null;
const tokens = JSON.parse(fs.readFileSync(path.join(ROOT, 'tokens.json'), 'utf8'));

// 型の表の組 / allowed size/line-height pairs
const PAIRS = new Set();
for (const g of tokens.type.groups) for (const s of g.styles) PAIRS.add(`${parseFloat(s.fontSize)}/${parseFloat(s.lineHeight)}`);
PAIRS.add('12/16');                 // 高さの決まった箱の中の 1 行（tokens.md 8.2「部品の寸法」）/ one line in a fixed-height box
const SIZES = new Set([...PAIRS].map(p => +p.split('/')[0]));
// 入力欄の文字は 16px（iOS の拡大を防ぐ）。中の値は 1 行 / inputs use 16px; single line
const INPUT_OK = new Set(['16/20', '16/22', '16/24']);
// 余白の段 / spacing scale (+ 1px の境界の打ち消し / 1px border compensation)
const SPACE = new Set(tokens.spacing.tokens.map(t => parseFloat(t.value) || 0));
for (const v of [...SPACE]) { SPACE.add(v - 1); SPACE.add(v + 1); }  // 1px の縁を引いた値 / minus or plus a 1px border
SPACE.add(1);
// 決まった足し算の値 / composed values with a stated formula
const COMPOSED = new Set([
  36,   // 入力欄の中のアイコンの場所 = space-md-nudge 10 + icon-sm 16 + space-md-nudge 10 / room for an icon inside a field
  48,   // フォームの組の間 = space-xxxl 32 + space-lg 16（.f2-form）/ gap between form groups
]);
// 文字色 / text colours from the colour tokens
function hex2rgb(h) { const n = parseInt(h.slice(1), 16); return `rgb(${n >> 16 & 255}, ${n >> 8 & 255}, ${n & 255})`; }
const tok = Object.fromEntries(tokens.color.tokens.map(t => [t.name, t.value]));
function res(v, m) { v = typeof v === 'object' ? v[m] : v; while (typeof v === 'string' && v.startsWith('{')) { v = tok[v.slice(1, -1)]; v = typeof v === 'object' ? v[m] : v; } return v; }
const RADII = new Set(tokens.radius.tokens.map(t => parseFloat(t.value) || 0));
const BORDERS = new Set(tokens.size.tokens.filter(t => /^stroke/.test(t.name)).map(t => parseFloat(t.value)));
const css = fs.readFileSync(path.join(ROOT, 'tokens.css'), 'utf8');
const FIRST = new Set([...css.matchAll(/--font-(?:sans|sans-en|mono):\s*"?([^",;]+)/g)].map(m => m[1].trim().toLowerCase()));
const COLORS = { light: new Set(), dark: new Set() };
for (const m of ['light', 'dark']) for (const n of Object.keys(tok)) {
  if (/^(gray|brand|blue|red|green|orange|yellow|purple|teal|pink|cat)-\d/.test(n)) continue;   // 原色は除く / skip primitives
  const v = res(tok[n], m); if (/^#[0-9a-f]{6}$/i.test(v)) COLORS[m].add(hex2rgb(v.toLowerCase()));
}

function inPage() {
  const out = [], hits = [], gaps = [];
  const vis = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 1 && r.height > 1 && !e.closest('.f2-sr') && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity !== 0; };
  const label = e => (e.tagName.toLowerCase() + ([...e.classList].slice(0, 2).map(c => '.' + c).join(''))) + (e.id ? '#' + e.id : '');
  const pathOf = e => { const a = []; for (let x = e; x && x !== document.body && a.length < 3; x = x.parentElement) a.unshift(label(x)); return a.join(' > '); };
  for (const e of document.body.querySelectorAll('*')) {
    if (['SCRIPT', 'STYLE', 'svg', 'SVG', 'path', 'TEMPLATE'].includes(e.tagName) || e.closest('svg')) continue;
    if (!vis(e)) continue;
    const cs = getComputedStyle(e);
    // 余白 / spacing
    const sp = {};
    for (const k of ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'marginTop', 'marginRight', 'marginBottom', 'marginLeft', 'rowGap', 'columnGap']) {
      const v = cs[k]; if (v && v.endsWith('px')) { const n = parseFloat(v); if (n !== 0) {
        if (/^margin/.test(k)) { const css = k.replace(/[A-Z]/g, m => '-' + m.toLowerCase()); const old = e.style.getPropertyValue(css); e.style.setProperty(css, 'auto'); const same = getComputedStyle(e)[k] === v; old ? e.style.setProperty(css, old) : e.style.removeProperty(css); if (same) continue; }   // margin: auto の結果は除く / skip margin:auto
        sp[k] = n; } }
    }
    // 自分の直下の文字 / own text
    const own = [...e.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' ');
    const isField = ['INPUT', 'TEXTAREA', 'SELECT'].includes(e.tagName);
    let lines = 0, width = 0;
    if (own) {
      const r = document.createRange(); let tops = new Set();
      for (const n of e.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { r.selectNodeContents(n); for (const q of r.getClientRects()) { if (q.width > 1) { tops.add(Math.round(q.top)); width = Math.max(width, q.width); } } }
      lines = tops.size;
    }
    const rect = e.getBoundingClientRect();
    // 切れた文字: 箱より中身が広く、はみ出しを隠していて、「…」を出していない / clipped text without ellipsis
    const clip = !!own && e.scrollWidth > e.clientWidth + 1 && /hidden|clip/.test(cs.overflowX + cs.overflow) && cs.textOverflow !== 'ellipsis';
    const clipByParent = !!own && !clip && (() => {
      // 文字の実際の右端と、はみ出しを隠す一番近い祖先の右端を比べる / compare the text's right edge with the nearest clipping ancestor
      const r = document.createRange(); let right = 0;
      for (const n of e.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { r.selectNodeContents(n); for (const q of r.getClientRects()) right = Math.max(right, q.right); }
      for (let a = e.parentElement, k = 0; a && k < 6; a = a.parentElement, k++) {
        const ac = getComputedStyle(a);
        if (/auto|scroll/.test(ac.overflowX)) return false;   // 横に送れる箱の中は切れていない / inside a scroll box nothing is lost
        if (!/hidden|clip/.test(ac.overflowX + ac.overflow)) continue;
        // 自分の「…」が効くのは自分の箱の中だけ。箱ごと祖先に切られていれば「…」は見えない / own ellipsis only works inside its own box
        const ar = a.getBoundingClientRect(); return Math.min(right, rect.right) > ar.right - parseFloat(ac.borderRightWidth) + 1 && ac.textOverflow !== 'ellipsis';
      }
      return false; })();
    const rad = [cs.borderTopLeftRadius, cs.borderTopRightRadius, cs.borderBottomLeftRadius, cs.borderBottomRightRadius].map(v => v.includes('%') ? -1 : parseFloat(v) || 0);
    const bw = ['Top', 'Right', 'Bottom', 'Left'].filter(k => cs['border' + k + 'Style'] !== 'none').map(k => parseFloat(cs['border' + k + 'Width']) || 0).filter(v => v > 0);
    const ff = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim().toLowerCase();
    const half = Math.min(rect.width, rect.height) / 2;
    out.push({ clip: clip || clipByParent, rad, bw, ff, half, path: pathOf(e), text: own.slice(0, 30), field: isField, fs: parseFloat(cs.fontSize), lh: cs.lineHeight, fw: cs.fontWeight, color: cs.color,
      lines, width, blockW: rect.width, align: cs.textAlign, heading: /^H[1-6]$/.test(e.tagName) || e.getAttribute('role') === 'heading' || /title|heading|__name|__h\b/.test(e.className) || !!e.closest('h1,h2,h3,h4,h5,h6,caption,legend'), centered: /flex|grid/.test(cs.display) && /center/.test(cs.justifyContent + cs.justifyItems), textLeft: (() => { if (!own) return null; const r = document.createRange(); for (const n of e.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { r.selectNodeContents(n); const q = r.getClientRects()[0]; if (q) return Math.round(q.left * 2) / 2; } return null; })(), selfAlign: (() => { const pcs = e.parentElement ? getComputedStyle(e.parentElement) : null; return pcs && /flex|grid/.test(pcs.display) ? (cs.justifySelf + ' ' + cs.alignSelf + ' ' + cs.marginLeft) : ''; })(), left: Math.round(rect.left * 2) / 2, sp, region: (e.closest('section,article,[role=dialog],dialog,form,.f2-card,ul,ol,table') ? pathOf(e.closest('section,article,[role=dialog],dialog,form,.f2-card,ul,ol,table')) : 'body') });
  }
  // 押せるもの / pressable things
  const SEL = 'button,a[href],input:not([type=hidden]),select,textarea,[role=button],[role=tab],[role=menuitem],[role=option],[role=switch],[role=checkbox],[role=radio],summary,[tabindex]:not([tabindex="-1"])';
  for (const e of document.querySelectorAll(SEL)) {
    if (!vis(e) || e.closest('[aria-hidden=true]') || e.disabled) continue;
    let r = e.getBoundingClientRect();
    // 見た目が小さいチェック・ラジオは、ラベルごと押せればラベルの範囲で測る / small boxes are measured with their label
    const lab = e.closest('label') || (e.id && document.querySelector(`label[for="${e.id}"]`));
    if (lab && ['checkbox', 'radio'].includes(e.type)) r = lab.getBoundingClientRect();
    const inline = e.tagName === 'A' && getComputedStyle(e).display === 'inline' && e.parentElement && e.parentElement.textContent.trim().length > e.textContent.trim().length + 4;
    hits.push({ path: pathOf(e), text: (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 20), x: r.left, y: r.top, w: r.width, h: r.height, inline, el: null });
    hits[hits.length - 1].el = e;
  }
  const hitOut = hits.map((h, i) => ({ ...h, el: undefined, i, anc: hits.filter(o => o !== h && (o.el.contains(h.el) || h.el.contains(o.el) || (o.el.closest('label') && o.el.closest('label').contains(h.el)) || (h.el.closest('label') && h.el.closest('label').contains(o.el)))).map(o => hits.indexOf(o)) }));
  // 並ぶものの間隔 / gaps between stacked or rowed siblings
  for (const c of document.body.querySelectorAll('*')) {
    if (c.closest('svg') || !vis(c)) continue;
    const kids = [...c.children].filter(k => vis(k) && getComputedStyle(k).position !== 'absolute' && getComputedStyle(k).position !== 'fixed');
    if (kids.length < 3) continue;
    const rs = kids.map(k => k.getBoundingClientRect());
    const col = rs.every((r, i) => i === 0 || r.top >= rs[i - 1].bottom - 0.5);
    const row = !col && rs.every((r, i) => i === 0 || (Math.abs(r.top - rs[0].top) < 1 && r.left >= rs[i - 1].right - 0.5));
    if (!col && !row) continue;
    let g = rs.slice(1).map((r, i) => Math.round((col ? r.top - rs[i].bottom : r.left - rs[i].right) * 2) / 2);
    // 見出し・ラベルと中身の間は、中身どうしとは別の関係 / heading-to-items is a different relation from item-to-item
    const k0 = kids[0]; if (/^(LEGEND|LABEL|H[1-6])$/.test(k0.tagName) || /legend|label|title|head/.test(k0.className)) g = g.slice(1);
    if (g.length < 2) continue;
    const mx = Math.max(...g), mn = Math.min(...g);
    if (mx - mn >= 0.5 && mx - mn <= 3 && mn >= 0) gaps.push({ path: pathOf(c), dir: col ? '縦' : '横', g });
  }
  return { out, hits: hitOut, gaps };
}

(async () => {
  const b = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage();
  const WIDTHS = (arg('width') || '1280,768,375').split(',').map(Number);
  const files = fs.readdirSync(DIR).filter(f => /-(light|dark)\.html$/.test(f)).sort();
  const found = []; let pages = 0, elements = 0;
  for (const W of WIDTHS) { await p.setViewport({ width: W, height: 900 });
  for (const f of files) {
    const [, name, theme] = f.match(/^(.*)-(light|dark)\.html$/);
    if (ONLY && !ONLY.includes(name)) continue;
    await p.goto('file://' + path.join(DIR, f), { waitUntil: 'load' }); await new Promise(r => setTimeout(r, 300));
    const res = await p.evaluate(inPage); const els = res.out; pages++; elements += els.length;
    if (theme === 'light') {
      const addH = (code, h, msg) => found.push({ code, name, theme, where: h.path, text: h.text, msg: msg + (W !== 1280 ? `（幅 ${W}）` : '') });
      for (const h of res.hits) {
        if (!h.inline && (h.w < 23.5 || h.h < 23.5)) addH('TARGET', h, `${Math.round(h.w)}×${Math.round(h.h)}px`);
        for (const o of res.hits) {
          if (o.i <= h.i || h.anc.includes(o.i)) continue;
          // 入力欄の中の消すボタン（検索欄）は、欄の文字の範囲の外に置いてある / a clear button sits inside the field's padding, outside its text area
          if (/f2-search__/.test(h.path + o.path)) continue;
          const ix = Math.min(h.x + h.w, o.x + o.w) - Math.max(h.x, o.x), iy = Math.min(h.y + h.h, o.y + o.h) - Math.max(h.y, o.y);
          if (ix > 1 && iy > 1) addH('OVERLAP', h, `「${o.text}」と ${Math.round(ix)}×${Math.round(iy)}px 重なる`);
        }
      }
      for (const g of res.gaps) found.push({ code: 'GAP', name, theme, where: g.path, text: '', msg: `${g.dir}の間隔 ${g.g.join('・')}px` + (W !== 1280 ? `（幅 ${W}）` : '') });
    }
    const add = (code, e, msg) => found.push({ code, name, theme, where: e.path, text: e.text, msg: msg + (W !== 1280 ? `（幅 ${W}）` : '') });
    const edges = {};
    for (const e of els) {
      const hasText = !!e.text || e.field;
      if (theme === 'light') {
        // AppIcon は OS の切り抜きの形を写したもの（KM1 の角丸ではない）/ AppIcon mimics OS masks
        if (name !== 'AppIcon') for (const r of new Set(e.rad)) if (r > 0 && !RADII.has(r) && Math.abs(r - e.half) > 0.5 && r < 9999) add('RADIUS', e, `${r}px`);
        // ラジオの選んだ印は太い縁で描く（部品の作り）/ the radio's checked dot is drawn with a thick border
        if (!/f2-radio__dot/.test(e.path)) for (const w of new Set(e.bw)) if (!BORDERS.has(w)) add('BORDER', e, `${w}px`);
        for (const [k, v] of Object.entries(e.sp)) {
          if (!SPACE.has(Math.abs(v)) && !COMPOSED.has(Math.abs(v))) add('SPACE', e, `${k} ${v}px`);
        }
      }
      if (!hasText) continue;
      if (theme === 'light' && !FIRST.has(e.ff)) add('FONT', e, e.ff);
      if (theme === 'light' && e.clip) add('CLIP', e, '「…」なしで切れている');
      const lhN = e.lh === 'normal' ? null : parseFloat(e.lh), pair = `${e.fs}/${lhN}`;
      if (theme === 'light') {
        if (e.fs < 12) add('SMALL', e, `${e.fs}px`);
        if (name === 'Cover' && /h1\.name$/.test(e.path)) { /* 表紙の KM1 はロゴの字（型の表の外）/ the cover wordmark is a logo, not type */ }
        else if (!e.field && !SIZES.has(e.fs)) add('TYPE', e, `大きさ ${e.fs}px`);
        else if (!e.field && lhN && !PAIRS.has(pair)) add('TYPE', e, `組 ${pair}`);
        else if (e.field && lhN && !PAIRS.has(pair) && !INPUT_OK.has(pair)) add('TYPE', e, `入力欄 ${pair}`);
        if (!['400', '600'].includes(e.fw)) add('WEIGHT', e, `太さ ${e.fw}`);
        // 短い文字（12 字以下）が折り返すのは入れ物が狭すぎる / short text wrapping means the box is too narrow
        if (e.lines >= 2 && e.text.replace(/\s/g, '').length <= 12) add('SQUEEZE', e, `${e.text.replace(/\s/g, '').length} 字が ${e.lines} 行に折り返す（幅 ${Math.round(e.blockW)}px）`);
        // 見出しは見出しの行の高さ（1.25〜1.4 倍）でよい。読ませる文は 1.5 倍以上（WCAG 1.4.12 は文の段落が対象）/ headings keep heading line height; body text needs 1.5x
        else if (e.lines >= 2 && lhN && lhN / e.fs < 1.5 && !e.heading) add('WRAP', e, `${e.lines} 行で ${pair}（${(lhN / e.fs).toFixed(2)} 倍）`);
        if (e.lines >= 2 && e.width > 40 * e.fs + 1) add('MEASURE', e, `1 行 ${Math.round(e.width / e.fs)}em`);
        // 左寄せの文字だけ比べる（右寄せ・中央・margin-left:auto の数字は対象外）/ only start-aligned text
        if (e.text && !e.centered && e.textLeft != null && ['start', 'left'].includes(e.align) && !/auto|end|right|center/.test(e.selfAlign) && e.blockW - e.width < 1 + 0 || (e.text && !e.centered && e.textLeft != null && ['start', 'left'].includes(e.align) && e.width < e.blockW - 1)) {
          (edges[e.region] = edges[e.region] || []).push({ ...e, left: e.textLeft });
        }
      }
      if (e.text && !COLORS[theme].has(e.color) && !/rgba\(0, 0, 0, 0\)/.test(e.color)) add('COLOR', e, e.color);
    }
    // そろえそこない: 同じ領域の左端が 0.5〜2px ずれる / near-miss edges within a region
    for (const [reg, list] of Object.entries(edges)) {
      const xs = [...new Set(list.map(e => e.left))].sort((a, b) => a - b);
      for (let i = 1; i < xs.length; i++) { const d = xs[i] - xs[i - 1]; if (d > 0 && d < 2) {
        const a = list.find(e => e.left === xs[i - 1]), c = list.find(e => e.left === xs[i]);
        found.push({ code: 'EDGE', name, theme, where: reg, text: '', msg: `幅 ${W}・左端 ${xs[i - 1]}「${a.text.slice(0, 10)}」${a.path.split(' > ').pop()} と ${xs[i]}「${c.text.slice(0, 10)}」${c.path.split(' > ').pop()}（${d}px）` }); } }
    }
  }
  }
  await b.close();
  const by = {}; for (const x of found) (by[x.code] = by[x.code] || []).push(x);
  const uniq = arr => { const m = new Map(); for (const x of arr) { const k = `${x.name}|${x.where}|${x.msg}`; if (!m.has(k)) m.set(k, { ...x, n: 0 }); m.get(k).n++; } return [...m.values()]; };
  console.log(`見本 ${pages} 枚・要素 ${elements} 個 / ${pages} previews, ${elements} elements`);
  for (const code of ['TYPE', 'WRAP', 'SQUEEZE', 'SMALL', 'WEIGHT', 'COLOR', 'SPACE', 'RADIUS', 'BORDER', 'FONT', 'MEASURE', 'CLIP', 'EDGE', 'TARGET', 'OVERLAP', 'GAP']) {
    const u = uniq(by[code] || []);
    console.log(`\n${code} ${u.length}`);
    for (const x of u.slice(0, +(arg('max') || 400))) console.log(`  ${x.name}${x.theme === 'dark' ? '(dark)' : ''}  ${x.msg}  ${x.where}${x.text ? '  「' + x.text + '」' : ''}${x.n > 1 ? '  ×' + x.n : ''}`);
  }
  if (arg('json')) fs.writeFileSync(arg('json'), JSON.stringify(found, null, 1));
  console.log(`\n--- 外れ ${found.length} 件 / ${found.length} findings`);
  process.exit(found.length ? 1 : 0);
})();
