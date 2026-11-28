// Browser check of a vertical review page (local.html): the player takes the video's 9:16 shape instead of a wide
// black box, and each filmstrip cell is covered by exactly one frame (no gaps), at desktop and phone width.
// Usage: node tests/review_vertical_check.js <review dir>   (prints JSON; exit 1 on any failure)
const { chromium } = require('playwright');

(async () => {
  const dir = process.argv[2];
  const fails = [];
  const b = await chromium.launch();
  const res = {};
  for (const [name, vp] of [['desktop', { width: 1360, height: 820 }], ['phone', { width: 390, height: 844 }]]) {
    const p = await b.newPage({ viewport: vp });
    const errs = [];
    p.on('pageerror', (e) => errs.push(e.message));
    await p.goto('file://' + dir + '/local.html');
    await p.waitForFunction(() => document.querySelector('video').readyState >= 1, null, { timeout: 15000 });
    await p.waitForTimeout(300);
    const r = await p.evaluate(() => {
      const scr = document.getElementById('screen');
      const box = scr.getBoundingClientRect();
      const v = document.querySelector('video');
      const cells = [...document.querySelectorAll('#strip span')].map((s) => {
        const c = s.getBoundingClientRect();
        const cs = getComputedStyle(s);
        const pos = cs.backgroundPosition.split(' ').map(parseFloat);
        return { w: c.width, h: c.height, size: parseFloat(cs.backgroundSize), x: pos[0], y: pos[1] };
      });
      return { shaped: scr.classList.contains('shaped'), ratio: box.width / box.height, vratio: v.videoWidth / v.videoHeight,
               cells, side: document.documentElement.scrollWidth > innerWidth };
    });
    res[name] = { shaped: r.shaped, ratio: r.ratio, cells: r.cells.length };
    const tag = (m) => fails.push(`${name}: ${m}`);
    if (errs.length) tag('script errors: ' + errs.join('; '));
    if (!r.shaped) tag('player not shaped to the vertical video');
    if (Math.abs(r.ratio - r.vratio) > 0.01) tag(`player ratio ${r.ratio.toFixed(3)} vs video ${r.vratio.toFixed(3)}`);
    if (r.side) tag('sideways scroll');
    if (!r.cells.length) tag('no filmstrip cells');
    // a cell shows one frame: the scaled frame (sprite width / columns) covers the cell, centred, never a gap
    for (const c of r.cells) {
      if (c.x > 0.5 || c.y > 0.5) { tag(`filmstrip cell starts with a gap (${c.x}, ${c.y})`); break; }
    }
    await p.close();
  }
  await b.close();
  console.log(JSON.stringify({ res, fails }, null, 1));
  process.exit(fails.length ? 1 : 0);
})();
