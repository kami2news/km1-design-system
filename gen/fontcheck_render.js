// KM1 書体の検査（描画）/ Rendered-font check
// 見本ページを Chrome で開き、文字がある要素ごとに「実際に描かれた書体」を CDP で取り、
// セリフ体・明朝体・手書き風・筆文字が 1 つでもあれば FAIL にする。
// Opens each preview in Chrome and reads the fonts actually used for every text node (CDP
// CSS.getPlatformFontsForNode). Any serif, Mincho, script or brush font is a FAIL.
// OFFLINE=1 を付けると外部通信を止める（例: OFFLINE=1 ... node fontcheck_render.js gen 'fonttest\\.html$'） / OFFLINE=1 blocks network
// 使い方 / usage: PUPPETEER_CORE=<puppeteer-core のパス> CHROME=<chrome のパス> node fontcheck_render.js <dir with *.html> [pattern]
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER_CORE || 'puppeteer-core');
const BANNED = /(serif(?!.*sans)|mincho|明朝|times|georgia|garamond|didot|bodoni|playfair|cambria|century|courier|script|brush|gyosho|行書|草書|楷書|kaisho|教科書|kyokasho|毛筆|筆|pop|ポップ|handwrit|comic|cursive|fantasy|MV Boli)/i;
(async () => {
  const dir = process.argv[2], pat = new RegExp(process.argv[3] || '-light\\.html$');
  const files = fs.readdirSync(dir).filter(f => pat.test(f)).sort();
  const browser = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--disable-gpu'] });
  const page = await browser.newPage();
  // OFFLINE=1: 外部通信を止めて、読み込みに失敗したときの代替を見る / block http(s) to see the fallback when web fonts fail
  if (process.env.OFFLINE === '1') {
    await page.setRequestInterception(true);
    page.on('request', req => (/^https?:/.test(req.url()) ? req.abort() : req.continue()));
  }
  const cdp = await page.target().createCDPSession();
  const used = {}, bad = [];
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f), { waitUntil: 'load' });
    await new Promise(r => setTimeout(r, 900));
    await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
    const { root } = await cdp.send('DOM.getDocument', { depth: -1, pierce: true });
    const ids = [];
    (function walk(n, parent) {
      if (n.nodeType === 3 && n.nodeValue.trim() && parent && !/^(SCRIPT|STYLE|TITLE|NOSCRIPT)$/.test(parent.nodeName)) ids.push([parent.nodeId, parent.nodeName, n.nodeValue.trim().slice(0, 20)]);
      for (const c of (n.children || [])) walk(c, n);
      if (n.contentDocument) walk(n.contentDocument, null);
    })(root, null);
    const seen = new Set();
    for (const [id, name, text] of ids) {
      if (seen.has(id)) continue; seen.add(id);
      let r; try { r = await cdp.send('CSS.getPlatformFontsForNode', { nodeId: id }); } catch (e) { continue; }
      for (const pf of r.fonts) {
        used[pf.familyName] = (used[pf.familyName] || 0) + pf.glyphCount;
        if (BANNED.test(pf.familyName)) bad.push(`${f} <${name.toLowerCase()}> "${text}" → ${pf.familyName}`);
      }
    }
  }
  await browser.close();
  console.log('files', files.length);
  console.log('fonts used (glyphs):', Object.entries(used).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} ${v}`).join(' / '));
  for (const b of bad.slice(0, 40)) console.log('FAIL', b);
  console.log(`--- FAIL ${bad.length}`);
  process.exit(bad.length ? 1 : 0);
})();
