// トークンの見本の図を作る / Render visual token sheets
// 使い方 / usage: node token_sheets.js [出力フォルダ / out dir]（既定 assets/tokens）
// tokens.json の名前を tokens.css で実際に描き、色（ライト・ダーク）・文字・余白・角丸・影・大きさの PNG を作る。
// tokens.md の「見本の図」と PDF から参照する。値は描いたあとの計算値なので、生成物の確認にもなる。
// Draws every token through tokens.css and writes PNG sheets referenced from tokens.md and the PDF.
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER || 'puppeteer-core');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.resolve(process.argv[2] || path.join(ROOT, 'assets', 'tokens'));
const T = JSON.parse(fs.readFileSync(path.join(ROOT, 'tokens.json'), 'utf8'));
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const ja = u => esc(String(u || '').split(' / ')[0]);
const PRIM = /^(gray|brand|blue|teal|orange|purple|green|red|yellow|pink|cat)-\d/;
const page = (title, body) => `<!doctype html><html lang="ja" data-theme="light"><head><meta charset="utf-8">
<link rel="stylesheet" href="file://${ROOT}/tokens.css"><style>
body{margin:0;padding:24px;background:#fff;color:#242424;font:400 13px/18px var(--font-sans);width:1100px}
h1{font:700 18px/24px var(--font-sans);color:#10218B;margin:0 0 16px}
table{border-collapse:collapse;width:100%} th,td{border-bottom:1px solid #e0e0e0;padding:6px 8px;white-space:nowrap;text-align:left;vertical-align:middle}
th{font-weight:600;color:#424242;background:#fafafa} code{font:12px/16px var(--font-mono)} .u{color:#616161;font-size:12px;white-space:normal}
.sw{display:flex;align-items:center;gap:8px}.chip{width:56px;height:28px;border:1px solid rgba(0,0,0,.15);border-radius:4px}
.dk{background:#1f1f1f;color:#f5f5f5}.dk .chip{border-color:rgba(255,255,255,.25)}
.grid{display:grid;grid-template-columns:repeat(8,1fr);gap:8px}.cell{font-size:11px;line-height:14px}.cell .chip{width:100%;height:36px}
</style></head><body><h1>${title}</h1>${body}</body></html>`;
function colorSheets() {
  const all = T.color.tokens, prim = all.filter(t => PRIM.test(t.name)), sem = all.filter(t => !PRIM.test(t.name));
  const row = t => `<tr><td><code>${t.name}</code></td>
    <td><div class="sw" data-theme="light"><div class="chip" style="background:var(--${t.name})"></div><code class="hex" data-v="${t.name}"></code></div></td>
    <td class="dk"><div class="sw" data-theme="dark"><div class="chip" style="background:var(--${t.name})"></div><code class="hex" data-v="${t.name}"></code></div></td>
    <td class="u">${ja(t.usage)}</td></tr>`;
  const half = Math.ceil(sem.length / 2);
  return {
    'color-semantic-1': page(`色（意味づけ）1 / Semantic colors 1 — ${sem.length}`, `<table><tr><th>名前</th><th>ライト</th><th>ダーク</th><th>用途</th></tr>${sem.slice(0, half).map(row).join('')}</table>`),
    'color-semantic-2': page('色（意味づけ）2 / Semantic colors 2', `<table><tr><th>名前</th><th>ライト</th><th>ダーク</th><th>用途</th></tr>${sem.slice(half).map(row).join('')}</table>`),
    'color-primitive': page(`色（原色）/ Primitive colors — ${prim.length}`, `<div class="grid">${prim.map(t => `<div class="cell" data-theme="light"><div class="chip" style="background:var(--${t.name})"></div><code>${t.name}</code><br><code class="hex" data-v="${t.name}"></code></div>`).join('')}</div>`),
  };
}
function typeSheet() {
  const fam = T.type.families;
  const rows = T.type.groups.flatMap(g => g.styles.map(s => `<tr><td><code>${s.name}</code><div class="u">${s.fontSize} / ${s.lineHeight} / ${s.fontWeight}</div></td>
    <td style="font-family:var(--font-${g.family === 'mono' ? 'mono' : 'sans'});font-size:${s.fontSize};line-height:${s.lineHeight};font-weight:${s.fontWeight};white-space:nowrap;overflow:hidden;max-width:620px">予定 Schedule 12</td>
    <td class="u">${ja(s.usage)}</td></tr>`)).join('');
  const fams = Object.entries(fam).map(([k, v]) => `<tr><td><code>${k}</code></td><td colspan="2"><code>${esc(v)}</code></td></tr>`).join('');
  return { 'type': page('文字 / Type ramp', `<table><tr><th>名前</th><th>見本</th><th>用途</th></tr>${rows}${fams}</table>`) };
}
function boxSheet(key, title, toks, draw) {
  return { [key]: page(title, `<table><tr><th>名前</th><th>値</th><th>見本</th><th>用途</th></tr>${toks.map(t => `<tr><td><code>${t.name}</code></td><td><code>${esc(t.value)}</code></td><td>${draw(t)}</td><td class="u">${ja(t.usage)}</td></tr>`).join('')}</table>`) };
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const sheets = Object.assign({}, colorSheets(), typeSheet(),
    boxSheet('spacing', '余白 / Spacing', T.spacing.tokens, t => `<div style="height:16px;width:var(--${t.name});background:#10218B;min-width:1px"></div>`),
    boxSheet('radius', '角丸 / Radius', T.radius.tokens, t => `<div style="width:64px;height:40px;border:2px solid #10218B;border-radius:var(--${t.name})"></div>`),
    boxSheet('shadow', '影 / Shadow', T.shadow.tokens, t => `<div style="width:96px;height:48px;margin:12px;background:#fff;border-radius:4px;box-shadow:var(--${t.name})"></div>`),
    boxSheet('size', '大きさ / Size', T.size.tokens, t => `<div style="height:var(--${t.name});width:var(--${t.name});max-width:200px;max-height:80px;background:#ECEFFC;border:1px solid #10218B"></div>`));
  const b = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage(); await p.setViewport({ width: 1148, height: 600, deviceScaleFactor: 2 });
  for (const [name, html] of Object.entries(sheets)) {
    const f = path.join(OUT, name + '.html'); fs.writeFileSync(f, html);
    await p.goto('file://' + f, { waitUntil: 'load' });
    await p.evaluate(() => document.querySelectorAll('.hex').forEach(el => {
      const c = getComputedStyle(el.closest('[data-theme]')).getPropertyValue('--' + el.dataset.v).trim();
      const d = document.createElement('div'); d.style.color = c; el.closest('[data-theme]').appendChild(d);
      const m = getComputedStyle(d).color.match(/[\d.]+/g); d.remove();
      el.textContent = m ? '#' + m.slice(0, 3).map(x => (+x).toString(16).padStart(2, '0')).join('') + (m[3] !== undefined && +m[3] < 1 ? ` ${Math.round(m[3] * 100)}%` : '') : c;
    }));
    const h = await p.evaluate(() => document.body.scrollHeight);
    await p.screenshot({ path: path.join(OUT, name + '.png'), clip: { x: 0, y: 0, width: 1148, height: h } });
    fs.unlinkSync(f);
  }
  await b.close(); console.log('token sheets', Object.keys(sheets).length, OUT);
})();
