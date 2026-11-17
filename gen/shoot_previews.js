// 部品の見本を画像にする / Screenshot every component preview
// 使い方 / usage: node shoot_previews.js <見本のフォルダ（render_previews.py の出力）> <components フォルダ>
// 各部品フォルダに preview.png（ライト、幅 1000px）を書く。GitHub の部品カタログと PDF で使う。
// Writes components/<Name>/preview.png (light, 1000px wide) for the GitHub catalog and the PDF.
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER || 'puppeteer-core');
(async () => {
  const [dir, comps] = process.argv.slice(2);
  const b = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage(); await p.setViewport({ width: 1000, height: 600, deviceScaleFactor: 1 });
  let n = 0;
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('-light.html')).sort()) {
    const name = f.replace('-light.html', '');
    await p.goto('file://' + path.resolve(dir, f), { waitUntil: 'load' }); await new Promise(r => setTimeout(r, 700));
    const h = await p.evaluate(() => Math.ceil(document.body.scrollHeight));
    await p.screenshot({ path: path.join(comps, name, 'preview.png'), clip: { x: 0, y: 0, width: 1000, height: Math.min(Math.max(h, 80), 2400) } });
    n++;
  }
  await b.close(); console.log('screenshots', n);
})();
