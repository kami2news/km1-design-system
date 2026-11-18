// 部品の見本を画像にする / Screenshot every component preview
// 使い方 / usage: node shoot_previews.js <見本のフォルダ（render_previews.py の出力）> <components フォルダ>
// 各部品フォルダに preview.png（ライト）と preview-dark.png（ダーク）を書く。2 倍の解像度で撮り、
// 中身の大きさで切り抜く（中身から 16px 残す）。画像の幅の半分が画面の CSS px（PDF で等倍に戻す）。
// Writes preview.png / preview-dark.png at 2x, cropped to content plus 16px; half the pixel width is the CSS size.
// 開いた状態で撮る / shot open: Dialog・Drawer・BottomSheet（小さめの画面全体）、Menu・Popover（押してから）、
// Toast（ボタンのすぐ下に置く）、Tooltip（フォーカスで出す。見本が自分で出す）。
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER || 'puppeteer-core');
const OVERLAY = { Dialog: 1, Drawer: 1, BottomSheet: 1 };          // 画面全体を撮る / capture the whole (small) window
const CLICK = { Drawer: '#r button', BottomSheet: '#r button', Menu: '#r button', Popover: '#r button' };
(async () => {
  const [dir, comps] = process.argv.slice(2);
  const b = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage();
  let n = 0;
  for (const f of fs.readdirSync(dir).filter(f => /-(light|dark)\.html$/.test(f)).sort()) {
    const [, name, theme] = f.match(/^(.*)-(light|dark)\.html$/);
    const ov = OVERLAY[name];
    await p.setViewport(ov ? { width: 720, height: 480, deviceScaleFactor: 2 } : { width: 960, height: 800, deviceScaleFactor: 2 });
    await p.goto('file://' + path.resolve(dir, f), { waitUntil: 'load' }); await new Promise(r => setTimeout(r, 600));
    if (CLICK[name]) { const el = await p.$(CLICK[name]); if (el) { await el.click(); await new Promise(r => setTimeout(r, 500)); } }
    if (name === 'Toast') await p.evaluate(() => {                  // 画面の中央ではなくボタンのすぐ下に / place under its button
      const btn = document.querySelector('#r button'), t = document.querySelector('.f2-toast'), reg = document.querySelector('.f2-toast-region');
      if (!btn || !t) return; const r = btn.getBoundingClientRect();
      const host = reg || t; host.style.position = 'absolute'; host.style.inset = 'auto'; host.style.left = r.left + 'px'; host.style.top = (r.bottom + 8) + 'px';
      host.style.transform = 'none'; host.style.width = 'auto'; t.style.animation = 'none';
    });
    await p.evaluate(() => document.getAnimations().forEach(a => { try { a.finish(); } catch (e) {} }));
    let clip;
    if (ov) clip = { x: 0, y: 0, width: 720, height: 480 };
    else {
      clip = await p.evaluate(() => {                              // 見える中身の外接矩形 / bounding box of visible content
        let x0 = 1e9, y0 = 1e9, x1 = 0, y1 = 0;
        for (const el of document.body.querySelectorAll('*')) {
          if (/^(SCRIPT|STYLE|LINK|META)$/.test(el.tagName)) continue;
          const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
          const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
          const own = [...el.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
          const painted = own || /^(svg|img|input|select|textarea|button|canvas|hr)$/i.test(el.tagName) ||
            cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.borderTopWidth !== '0px' || cs.borderLeftWidth !== '0px' || cs.boxShadow !== 'none';
          if (!painted || el === document.body || el === document.documentElement) continue;
          x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom);
        }
        const W = document.documentElement.scrollWidth, H = document.documentElement.scrollHeight;
        if (x1 <= x0) return { x: 0, y: 0, width: Math.min(W, 960), height: 80 };
        x0 = Math.max(0, Math.floor(x0 - 16)); y0 = Math.max(0, Math.floor(y0 - 16));
        x1 = Math.min(W, Math.ceil(x1 + 16)); y1 = Math.min(H, Math.ceil(y1 + 16));
        return { x: x0, y: y0, width: x1 - x0, height: y1 - y0 };
      });
      const H = await p.evaluate(() => document.documentElement.scrollHeight);
      if (clip.y + clip.height > 800) await p.setViewport({ width: 960, height: Math.min(H, 6000), deviceScaleFactor: 2 });
    }
    const out = path.join(comps, name, theme === 'light' ? 'preview.png' : 'preview-dark.png');
    await p.screenshot({ path: out, clip, captureBeyondViewport: true });
    n++;
  }
  await b.close(); console.log('screenshots', n);
})();
