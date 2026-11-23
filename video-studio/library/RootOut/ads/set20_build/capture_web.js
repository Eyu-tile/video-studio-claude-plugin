// Capture real public pages on a phone viewport, highlight one verbatim sentence, crop around it.
const { chromium, devices } = require('playwright');
const out = process.argv[2];
const only = process.argv[3] ? process.argv[3].split(',') : null;
const jobs0 = [
  { n: 'w1_dots_nhs',   url: 'https://www.nhs.uk/conditions/warts-and-verrucas/', text: 'They have tiny black dots under the hard skin.' },
  { n: 'w2_pebbles_aad', url: 'https://www.aad.org/public/diseases/a-z/warts-overview', text: "Some people say it feels like they’re walking on pebbles." },
  { n: 'w3_nopick_aad', url: 'https://www.aad.org/public/diseases/a-z/warts-self-care', text: 'Do not pick or scratch at warts.' },
  { n: 'w4_spread_aad', url: 'https://www.aad.org/public/diseases/a-z/warts-overview', text: 'If you have a wart, you can spread the virus that causes it to other people and to other parts of your body.' },
  { n: 'w5_study_pubmed', url: 'https://pubmed.ncbi.nlm.nih.gov/19438464/', wait: 8000, text: 'An increased risk of the presence of warts was found in children with a family member with warts' },
  { n: 'w6_nhs_spread', url: 'https://www.nhs.uk/conditions/warts-and-verrucas/', text: 'do not scratch or pick a wart' },
];
const jobs = only ? jobs0.filter(j => only.includes(j.n)) : jobs0;
(async () => {
  const b = await chromium.launch();
  for (const j of jobs) {
    const ctx = await b.newContext({ ...devices['iPhone 13'], deviceScaleFactor: 3 });
    const p = await ctx.newPage();
    try {
      await p.goto(j.url, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(j.wait || 4000);
      for (const sel of ['#nhsuk-cookie-banner__link_accept_analytics', 'button:has-text("Accept")', 'button:has-text("I agree")', 'button:has-text("Got it")', 'button:has-text("Close")'])
        { const e = await p.$(sel); if (e) { await e.click().catch(()=>{}); await p.waitForTimeout(500); } }
      const box = await p.evaluate((t) => {
        // hide sticky/fixed overlays
        for (const el of document.querySelectorAll('*')) { const s = getComputedStyle(el); if ((s.position === 'fixed' || s.position === 'sticky') && el.tagName !== 'HTML') el.style.visibility = 'hidden'; }
        const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        const esc = x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); const rx = new RegExp(esc(t).replace(/[’']/g, "['’]").replace(/\s+/g, '\\s+'));
        while (w.nextNode()) { const nd = w.currentNode; const mm = rx.exec(nd.textContent); const i = mm ? mm.index : -1;
          if (i >= 0) { const r = document.createRange(); r.setStart(nd, i); r.setEnd(nd, i + mm[0].length);
            const m = document.createElement('mark'); m.style.background = '#FFE45C'; m.style.color = 'inherit'; m.style.padding = '0 2px';
            try { r.surroundContents(m); } catch (e) {}
            const blk = m.isConnected ? m : nd.parentElement; blk.scrollIntoView({ block: 'center' });
            const q = blk.getBoundingClientRect(); return { x: q.x, y: q.y, w: q.width, h: q.height }; } }
        return null; }, j.text);
      if (!box) { console.log(j.n, 'TEXT NOT FOUND'); await p.screenshot({ path: `${out}/${j.n}_FULL.png` }); continue; }
      await p.waitForTimeout(600);
      const vp = p.viewportSize(); const top = Math.max(0, box.y - 260), h = Math.min(vp.height - top, box.h + 520);
      await p.screenshot({ path: `${out}/${j.n}.png`, clip: { x: 0, y: top, width: vp.width, height: h } });
      console.log(j.n, 'ok', JSON.stringify(box));
    } catch (e) { console.log(j.n, 'ERR', e.message); }
    await ctx.close();
  }
  await b.close();
})();
