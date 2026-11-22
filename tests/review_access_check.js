// Browser check of who can post on the published review page (index.html), with a stub of the claude.ai runtime:
// owner and invited editor post to the shared list; a view-only viewer and an account claude.ai doesn't link to the
// invite keep notes on the device, marked NOT sent, with the access check in Copy notes; a refused note is not lost.
// Usage: node tests/review_access_check.js <review dir>   (prints JSON; exit 1 on any failure)
const { chromium } = require('playwright');

function stub(kind) {
  return `(() => {
    const kind = ${JSON.stringify(kind)};
    const docs = window.__docs = [], listeners = [];
    const emit = () => listeners.forEach((f) => f({ metadata: { fromCache: false }, docs: docs.map((d) => ({ id: d.id, data: () => d.data })) }));
    const refuse = (code) => { const e = new Error(code); e.code = code; throw e; };
    const col = {
      add: async (c) => { if (kind === 'viewer' || kind === 'unlinked') refuse('invalid_argument'); docs.push({ id: 'd' + docs.length, data: c }); emit(); },
      doc: () => ({ update: async () => {}, delete: async () => {} }),
      onSnapshot: (f) => { listeners.push(f); setTimeout(emit, 30); return () => {}; },
    };
    const user = { me: async () => ({ id: 'u1' }), can: async () => kind !== 'viewer', isOwner: async () => kind === 'owner', profiles: async () => ({}) };
    window.claude = { use: async (n) => {
      if (n === 'db') return { collection: () => col };
      if (n === 'user' && kind !== 'unlinked') return user;
      refuse('not_granted');
    } };
  })();`;
}

(async () => {
  const dir = process.argv[2];
  const fails = [], out = {};
  const ok = (cond, msg) => { if (!cond) fails.push(msg); };
  const b = await chromium.launch();
  for (const kind of ['owner', 'editor', 'viewer', 'unlinked']) {
    const ctx = await b.newContext({ viewport: { width: 1360, height: 820 } });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', (e) => errs.push(e.message));
    await p.addInitScript(stub(kind));
    await p.goto('file://' + dir + '/index.html');
    await p.waitForTimeout(500);
    await p.evaluate(() => { navigator.clipboard.writeText = (t) => { window.__c = t; return Promise.resolve(); }; });
    try { await p.fill('#text', 'Note from ' + kind, { timeout: 3000 }); await p.press('#text', 'Enter'); }
    catch { ok(false, `${kind}: can type a note`); }
    await p.waitForTimeout(300);
    const r = {
      mode: await p.textContent('#mode'), status: await p.textContent('#status'),
      shared: await p.evaluate(() => window.__docs.length),
      shown: await p.$$eval('.list .c .body', (e) => e.map((x) => x.textContent)),
      red: await p.evaluate(() => document.getElementById('mode').classList.contains('warn')),
    };
    if (await p.$('#refresh')) { await p.click('#refresh'); await p.waitForTimeout(200); } else ok(false, `${kind}: Refresh button`);
    await p.click('#copyNotes'); await p.waitForTimeout(100);
    r.copied = await p.evaluate(() => window.__c || '');
    const shared = kind === 'owner' || kind === 'editor';
    ok(!errs.length, `${kind}: no script errors (${errs.join('; ')})`);
    ok(r.shown.includes('Note from ' + kind), `${kind}: the note is shown`);
    if (shared) {
      ok(r.shared === 1 && r.mode.startsWith('Shared'), `${kind}: posted to the shared list`);
      ok(!r.red && !r.copied.includes('Access check'), `${kind}: no NOT-sent warning`);
    } else {
      ok(r.shared === 0 && /NOT sent/.test(r.mode) && r.red, `${kind}: kept on the device, marked NOT sent in red`);
      ok(r.copied.includes('Note from ' + kind) && r.copied.includes('Access check:'), `${kind}: Copy notes has the note and the access check`);
    }
    if (kind === 'unlinked') ok(r.copied.includes('user=false') && r.copied.includes('error=invalid_argument'), 'unlinked: access check says user=false and why the write failed');
    if (kind === 'viewer') ok(r.copied.includes('write=false'), 'viewer: access check says write=false');
    out[kind] = r;
    await ctx.close();
  }
  await b.close();
  console.log(JSON.stringify({ ok: !fails.length, fails, out }, null, 1));
  process.exit(fails.length ? 1 : 0);
})();
