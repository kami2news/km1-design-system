const puppeteer=require(process.env.PUPPETEER||'/tmp/perf/node_modules/puppeteer-core');
const fs=require('fs');
(async()=>{
 const mode=process.argv[2]||'pc';
 const b=await puppeteer.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
 const files=fs.readdirSync('/tmp/rc').filter(f=>f.endsWith('-light.html'));
 const out={};
 for(const f of files){
  const p=await b.newPage(); await p.setViewport(mode==='touch'?{width:390,height:844,hasTouch:true,isMobile:true}:{width:1000,height:900});
  await p.goto('file:///tmp/rc/'+f); await new Promise(r=>setTimeout(r,500));
  out[f.replace('-light.html','')]=await p.evaluate(()=>{
   const r={h:{},fs:{},rad:{},ic:{}};
   const add=(o,k,el)=>{(o[k]=o[k]||[]).push(el.tagName.toLowerCase()+'.'+String(el.className&&el.className.baseVal!==undefined?el.className.baseVal:el.className).split(' ')[0]);};
   document.querySelectorAll('#r *').forEach(el=>{
     const cs=getComputedStyle(el); if(cs.display==='none'||el.closest('img'))return;
     const bb=el.getBoundingClientRect(); if(!bb.width)return;
     if(el.matches('button,input:not([type=checkbox]):not([type=radio]):not([type=range]),select,[role=tab],[role=combobox],.f2-btn')) add(r.h,Math.round(bb.height),el);
     if(el.childNodes&&[...el.childNodes].some(n=>n.nodeType==3&&n.textContent.trim())) add(r.fs,cs.fontSize+'/'+cs.lineHeight,el);
     if(cs.borderTopLeftRadius!=='0px') add(r.rad,cs.borderTopLeftRadius,el);
     if(el.tagName==='svg') add(r.ic,Math.round(bb.width)+'x'+Math.round(bb.height),el);
   });
   for(const o of Object.values(r))for(const k in o)o[k]=[...new Set(o[k])].slice(0,4).join(',')+' ×'+o[k].length;
   return r;});
  await p.close();
 }
 fs.writeFileSync('/tmp/aud/'+mode+'.json',JSON.stringify(out,null,1));
 await b.close();
})();
