// KM1 の Web の自動検査（W1）/ Automated web checks for KM1 (W1)
// 使い方 / usage: node web_test.js <見本のフォルダ（render_previews.py の出力）> [--only=axe,keyboard,reflow,regress,scenario]
// gen で `npm i`（puppeteer-core・axe-core・React）。Chrome の場所は CHROME で変えられる。
// 1. axe   : 全部の見本（ライト・ダーク）で axe-core の WCAG 2.2 A・AA の規則。違反 0 で合格。ページ単位の規則（main・h1・目印）は
//            見本が部品の断片なので対象外 / WCAG A/AA rules only; page-level best practices don't apply to fragments
// 2. keyboard: ライトの見本で Tab を 30 回まで押し、フォーカスが見える所にあり、枠（outline か box-shadow）が出るか
// 3. reflow: 幅 320px で、ページ全体が横にはみ出さないか（WCAG 1.4.10）
// 4. regress: 無効の ListItem・Button を押しても何も起きない。ErrorSummary・StepFlow を 2 つ置いても id が重ならない
// 5. scenario: 利用シナリオ S1〜S3（verification.md 2 章）を 360px・1366px のライトと 1024px のダークで
// 1 つでも落ちたら終了コード 1。/ Exits 1 on any failure.
const fs = require('fs'), path = require('path');
const puppeteer = require(process.env.PUPPETEER || 'puppeteer-core');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const DIR = path.resolve(process.argv[2] || '/tmp/rc');
const ONLY = ((process.argv.find(a => a.startsWith('--only=')) || '').slice(7) || 'axe,keyboard,reflow,regress,scenario').split(',');
const sleep = ms => new Promise(r => setTimeout(r, ms));
let fails = 0, passes = 0;
const ok = (cond, name, info) => { if (cond) passes++; else { fails++; console.log('FAIL', name, info || ''); } };
const url = f => 'file://' + path.join(DIR, f);

async function load(p, file, w, h) {
  await p.setViewport({ width: w || 1366, height: h || 900 });
  await p.goto(url(file), { waitUntil: 'load' }); await sleep(250);
}

async function axe(p, pages) {
  for (const f of pages) {
    await load(p, f);
    await p.evaluate(AXE);
    const v = await p.evaluate(async () => (await window.axe.run(document, { resultTypes: ['violations'], runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } })).violations
      .map(x => `${x.id}(${x.impact}) ×${x.nodes.length}: ${x.nodes[0].target.join(' ')}`));
    ok(v.length === 0, 'axe ' + f, v.join(' | '));
  }
}

async function keyboard(p, pages) {
  for (const f of pages) {
    await load(p, f);
    // 要素ごとに、フォーカスがある間に一度でも枠が出たか（日付の欄は中の年・月・日を Chrome が自分で描くため）
    // per element: a ring must show at least once while it has focus (Chrome draws date sub-fields itself)
    for (let i = 0; i < 30; i++) {
      await p.keyboard.press('Tab');
      const end = await p.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return true;
        const has = e => { const c = getComputedStyle(e); return (c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0) || c.boxShadow !== 'none'; };
        const ring = has(el) || (el.parentElement && has(el.parentElement)) || (el.parentElement && el.parentElement.parentElement && has(el.parentElement.parentElement));
        const cs = getComputedStyle(el), b = el.getBoundingClientRect();
        window.__kb = window.__kb || new Map(); const o = window.__kb.get(el) || { ring: false, visible: true };
        o.ring = o.ring || ring; o.visible = o.visible && b.width > 0 && b.height > 0 && cs.visibility !== 'hidden';
        o.tag = el.tagName + (el.className ? '.' + String(el.className).split(' ')[0] : ''); window.__kb.set(el, o); return false;
      });
      if (end) break;
    }
    const bad = await p.evaluate(() => [...(window.__kb || new Map()).values()].filter(o => !o.ring || !o.visible).map(o => o.tag + (o.visible ? '' : ' 見えない/hidden') + (o.ring ? '' : ' 枠なし/no ring')));
    ok(bad.length === 0, 'keyboard ' + f, [...new Set(bad)].join(', '));
  }
}

// 部品ではなく説明用の図（表紙・アイコンの表・選び方の早見図）は 320px の対象外 / doc cards, not components
const REFLOW_EXEMPT = { 'Cover-light.html': '表紙 / cover', 'Icon-light.html': 'アイコンの一覧表 / icon table', 'IconTrial-light.html': 'アイコンの試作表 / icon trial table', 'SelectionGuide-light.html': '部品の選び方の早見図 / selection chart' };
async function reflow(p, pages) {
  for (const f of pages.filter(f => !REFLOW_EXEMPT[f])) {
    await load(p, f, 320, 640);
    const w = await p.evaluate(() => document.documentElement.scrollWidth);
    ok(w <= 321, 'reflow320 ' + f, `scrollWidth=${w}`);
  }
}

// 見本の HTML を一時的に作る（render_previews.py と同じ組み方）/ build an ad-hoc test page
function testPage(name, script, theme) {
  const f = `_test-${name}.html`;
  fs.writeFileSync(path.join(DIR, f), `<!doctype html><html lang="ja" data-theme="${theme || 'light'}"><head><meta charset="utf-8"><title>${name}</title>
<link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css"><script src="react.js"></script><script src="react-dom.js"></script><script src="bundle.js"></script>
</head><body><div id="r"></div><script>var h=React.createElement,F=window.Fluent2;window.hits=0;${script}</script></body></html>`);
  return f;
}

async function regress(p) {
  // 無効の ListItem と Button / disabled ListItem and Button
  await load(p, testPage('disabled', `ReactDOM.createRoot(document.getElementById('r')).render(h('div',null,
    h(F.List,{label:'t'},h(F.ListItem,{title:'無効の行',disabled:true,onClick:function(){window.hits++;}}),h(F.ListItem,{title:'無効のリンク',href:'#x',disabled:true,onClick:function(){window.hits++;}})),
    h(F.Button,{disabled:true,onClick:function(){window.hits++;}},'無効のボタン')));`));
  for (const sel of ['button.f2-li__primary', 'a.f2-li__primary', 'button.f2-btn']) {
    await p.click(sel); await p.focus(sel); await p.keyboard.press('Enter');
  }
  const r = await p.evaluate(() => ({ hits: window.hits, hash: location.hash, focusable: [...document.querySelectorAll('[aria-disabled="true"]')].every(e => e.tabIndex >= 0) }));
  ok(r.hits === 0 && r.hash === '', '無効の ListItem・Button は押しても動かない / disabled items are inert', JSON.stringify(r));
  ok(r.focusable, '無効でもフォーカスできる / disabled items stay focusable');
  // 2 つ置いても id が重ならない / no duplicate ids with two instances
  await load(p, testPage('multi', `var e=[{id:'a1',label:'名前',message:'入力してください'}],S=[{id:'s1',title:'一'},{id:'s2',title:'二'}];
    ReactDOM.createRoot(document.getElementById('r')).render(h('div',null,h('input',{id:'a1'}),
      h(F.ErrorSummary,{errors:e}),h(F.ErrorSummary,{errors:e,title:'二つ目'}),
      h(F.StepFlow,{steps:S,active:'s1',label:'流れ 1'},'a'),h(F.StepFlow,{steps:S,active:'s2',label:'流れ 2'},'b'),h(F.ErrorSummary,{errors:e,id:'mine'})));`));
  const d = await p.evaluate(() => {
    const ids = [...document.querySelectorAll('[id]')].map(e => e.id), dup = ids.filter((x, i) => ids.indexOf(x) !== i);
    const refs = [...document.querySelectorAll('[aria-labelledby]')].map(e => { const t = document.getElementById(e.getAttribute('aria-labelledby')); return !!t && e.contains(t); });
    return { dup, refs, mine: !!document.getElementById('mine-title') };
  });
  ok(d.dup.length === 0, '2 つ置いても id が重ならない / unique ids', JSON.stringify(d.dup));
  ok(d.refs.length >= 5 && d.refs.every(Boolean), '名前の参照先が自分の見出し / aria-labelledby points inside itself', JSON.stringify(d.refs));
  ok(d.mine, '外から決めた id を使う / caller id respected');
}

// ---------- シナリオ / scenarios ----------
const byLabel = (p, text) => p.evaluateHandle(t => { const l = [...document.querySelectorAll('label')].find(x => x.textContent.replace(/\s|必須|\*/g, '').startsWith(t)); return l && (l.control || document.getElementById(l.htmlFor)); }, text);
const btnByText = (p, text, scope) => p.evaluateHandle((t, s) => [...(s ? document.querySelector(s) : document).querySelectorAll('button')].find(b => b.textContent.trim() === t), text, scope || null);
const active = p => p.evaluate(() => { const a = document.activeElement; return { tag: a.tagName, id: a.id, cls: String(a.className), text: a.textContent.trim().slice(0, 40) }; });
const live = (p, re) => p.evaluate(r => [...document.querySelectorAll('[role=status],[role=alert],[aria-live]')].some(e => new RegExp(r).test(e.textContent)), re);
// React が受け取る形で値を入れる（全選択して消すのは日付・時刻の欄で効かないため）/ set a value the way React sees it
async function type(p, handle, text) {
  await handle.focus();
  await handle.evaluate((el, v) => { const d = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(el), 'value'); d.set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }, text);
}

async function s1(p, tag) {
  const open = await btnByText(p, '予定を追加'); await open.click(); await sleep(300);
  ok(await p.evaluate(() => !!document.activeElement.closest('.f2-drawer')), `S1 ${tag} ドロワーが開くとフォーカスが中へ / focus moves into drawer`);
  await (await btnByText(p, '追加する')).click(); await sleep(300);
  const a = await active(p);
  ok(/f2-errsum/.test(a.cls) && /2 件/.test(a.text), `S1 ${tag} エラーの一覧へフォーカスが移り件数が出る / error summary focused with count`, JSON.stringify(a));
  await p.click('.f2-errsum a'); await sleep(150);
  const target = await p.evaluate(() => document.querySelector('.f2-errsum a').getAttribute('href').slice(1));
  ok((await active(p)).id === target, `S1 ${tag} エラーのリンクで欄へ / link moves focus to the field`);
  await type(p, await byLabel(p, 'タイトル'), '読書会');
  await type(p, await byLabel(p, '開始'), '10:30'); await sleep(100);
  await (await btnByText(p, '追加する')).click(); await sleep(900);
  const after = await active(p);
  ok(!(await p.evaluate(() => { const d = document.querySelector('dialog.f2-drawer'); return d && d.open; })), `S1 ${tag} 追加後にドロワーが閉じる / drawer closes`);
  ok(after.text === '予定を追加', `S1 ${tag} 「予定を追加」へフォーカスが戻る / focus returns to opener`, JSON.stringify(after));
  ok(await live(p, '「読書会」を追加しました'), `S1 ${tag} 追加が読み上げの領域に出る / addition announced`);
}

async function s2(p, tag) {
  ok(await p.evaluate(() => { const c = document.querySelector('[aria-current="true"]'); return !!c && /地球化学/.test(c.textContent); }), `S2 ${tag} 今開いている行が分かる / current row marked`);
  await p.click('.f2-xe__btn'); await sleep(200);
  await type(p, await byLabel(p, '教室'), '');
  await (await btnByText(p, '保存', '.f2-xe')).click(); await sleep(300);
  const err = await p.evaluate(() => { const e = document.querySelector('.f2-xe__err[role=alert]'); return { msg: !!e && /教室を入力/.test(e.textContent), keep: !!document.querySelector('.f2-xe__panel:not([hidden])') }; });
  ok(err.msg && err.keep, `S2 ${tag} 失敗が読まれ入力が残る / failure announced, editor stays open`, JSON.stringify(err));
  await type(p, await byLabel(p, '教室'), 'W9-100');
  await (await btnByText(p, '保存', '.f2-xe')).click(); await sleep(400);
  const back = await p.evaluate(() => ({ focus: document.activeElement.classList.contains('f2-xe__btn'), sum: document.querySelector('.f2-xe__summary').textContent }));
  ok(back.focus && back.sum === 'W9-100', `S2 ${tag} 保存後に見出しへ戻る / focus back on header, value saved`, JSON.stringify(back));
  const boxes = await p.$$('.f2-li__check input'); await boxes[1].click(); await boxes[2].click(); await sleep(150);
  await (await btnByText(p, '削除', '.f2-bulk')).click(); await sleep(300);
  ok(await p.evaluate(() => { const d = document.querySelector('dialog[open]'); return !!d && /2 件の授業を削除しますか/.test(d.textContent); }), `S2 ${tag} 件数つきで確認される / confirm shows count`);
  await (await btnByText(p, '削除する')).click(); await sleep(300);
  const n1 = await p.$$eval('.f2-li', x => x.length);
  const undo = await btnByText(p, '元に戻す'); await undo.click(); await sleep(300);
  const n2 = await p.$$eval('.f2-li', x => x.length);
  ok(n1 === 2 && n2 === 4, `S2 ${tag} 削除して元に戻せる / delete then undo`, `${n1}→${n2}`);
}

async function s3(p, tag) {
  await p.setOfflineMode(true); await sleep(300);
  ok(await p.evaluate(() => /インターネットに接続されていません/.test(document.body.textContent) && /時点の内容/.test(document.body.textContent)), `S3 ${tag} 警告と「〜時点の内容」が出る / warning and timestamp`);
  await type(p, await byLabel(p, '予定を追加'), 'ゼミ'); await p.keyboard.press('Enter'); await sleep(200);
  ok(await p.evaluate(() => /未送信 1 件/.test(document.body.textContent)), `S3 ${tag} 「未送信 1 件」が出る / pending count shown`);
  await p.setOfflineMode(false); await sleep(800);
  ok(await live(p, '1 件を送信しました'), `S3 ${tag} つながると送られ、お知らせが読まれる / sent and announced`);
}

async function scenarios(p) {
  for (const [w, theme] of [[360, 'light'], [1366, 'light'], [1024, 'dark']]) {
    const tag = `${w}px ${theme}`;
    for (const [n, fn] of [['ScreenAddEvent', s1], ['ScreenListEdit', s2], ['ScreenOffline', s3]]) {
      await load(p, `${n}-${theme}.html`, w, 800);
      try { await fn(p, tag); } catch (e) { ok(false, `${n} ${tag}`, e.message); }
      await p.setOfflineMode(false);
    }
  }
}

(async () => {
  const b = await puppeteer.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage();
  const all = fs.readdirSync(DIR).filter(f => /-(light|dark)\.html$/.test(f)).sort(), light = all.filter(f => f.endsWith('-light.html'));
  const t0 = Date.now(); const before = () => [passes, fails];
  for (const [k, run] of [['axe', () => axe(p, all)], ['keyboard', () => keyboard(p, light)], ['reflow', () => reflow(p, light)], ['regress', () => regress(p)], ['scenario', () => scenarios(p)]]) {
    if (!ONLY.includes(k)) continue;
    const [a0, f0] = before(); await run(); console.log(`${k}: 合格 ${passes - a0} / 不合格 ${fails - f0}`);
  }
  for (const f of fs.readdirSync(DIR).filter(f => f.startsWith('_test-'))) fs.unlinkSync(path.join(DIR, f));
  await b.close();
  console.log(`--- 合格 ${passes} / 不合格 ${fails}（${Math.round((Date.now() - t0) / 1000)} 秒）/ pass ${passes}, fail ${fails}`);
  process.exit(fails ? 1 : 0);
})();
