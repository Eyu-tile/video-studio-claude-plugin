// Usage: node hl.js URL OUT "phrase1" ["phrase2" ...]  -> highlights phrases, centres the first, phone-size screenshot
const { chromium } = require('playwright');
(async () => {
  const [,, url, out, ...phrases] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 430, height: 760 }, deviceScaleFactor: 2.5,
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }); await p.waitForTimeout(2500);
  const ok = await p.evaluate((phrases) => {
    document.querySelectorAll('header, nav, [class*=cookie], [id*=cookie], [class*=banner], [class*=Banner], .usa-banner, #onetrust-banner-sdk, [class*=sticky], [class*=Sticky]').forEach(e => e.style.display = 'none');
    let first = null, found = 0;
    for (const ph of phrases) {
      const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let n; while ((n = w.nextNode())) {
        const i = n.nodeValue.indexOf(ph); if (i < 0) continue;
        const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + ph.length);
        const m = document.createElement('mark'); m.style.cssText = 'background:#FFE45C;color:inherit;padding:1px 2px;border-radius:3px';
        r.surroundContents(m); if (!first) first = m; found++; break;
      }
    }
    if (first) first.scrollIntoView({ block: 'center' });
    return found;
  }, phrases);
  await p.waitForTimeout(600); await p.screenshot({ path: out }); console.log(out, 'highlighted', ok, 'of', phrases.length); await b.close();
})();
