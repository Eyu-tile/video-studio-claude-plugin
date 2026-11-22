const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ ...devices['iPhone 13'] });
  const p = await ctx.newPage();
  await p.goto(process.argv[2], { waitUntil: 'domcontentloaded', timeout: 60000 });
  try { await p.waitForFunction(() => document.body.innerText.includes('were not related to the presence of warts'), null, { timeout: 45000 }); } catch (e) { console.log('text not found'); }
  await p.waitForTimeout(4000);
  for (const t of ['Accept', 'Got it', 'I agree', 'Close']) { const btn = p.getByRole('button', { name: t }); if (await btn.count()) { try { await btn.first().click({ timeout: 2000 }); } catch (e) {} } }
  await p.evaluate(() => {
    const marks = ['were not related to the presence of warts', 'children with a family member with warts', '1465 children aged 4-12'];
    const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const nodes = []; while (tw.nextNode()) nodes.push(tw.currentNode);
    for (const m of marks) for (const c of nodes) { const i = c.data.indexOf(m); if (i >= 0) { const r = document.createRange(); r.setStart(c, i); r.setEnd(c, i + m.length); const s = document.createElement('mark'); s.style.background = '#FFE066'; s.style.color = 'inherit'; r.surroundContents(s); break; } }
  });
  await p.screenshot({ path: process.argv[3], fullPage: true });
  console.log(await p.title());
  await b.close();
})();
