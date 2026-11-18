// End-to-end API tests: seeds a throwaway database, starts the real server, and exercises the
// operational safety rules. Run with:  npm test
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { spawn, execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DATA_DIR = fs.mkdtempSync(path.join(os.tmpdir(), 'byf-test-'));
const PORT = 4600 + Math.floor(Math.random() * 300);
const BASE = `http://localhost:${PORT}/api`;
const ENV = { ...process.env, DATA_DIR, PORT: String(PORT), ADMIN_PASSWORD: 'Admin-pass-2026', NODE_ENV: 'test' };
let server;

function startServer() {
  return new Promise((resolve, reject) => {
    server = spawn(process.execPath, ['--no-warnings=ExperimentalWarning', 'server/index.js'], { cwd: ROOT, env: ENV });
    let out = '';
    server.stdout.on('data', (d) => { out += d; if (out.includes('listening')) resolve(); });
    server.stderr.on('data', (d) => { out += d; });
    server.on('exit', (c) => reject(new Error(`server exited ${c}: ${out}`)));
  });
}
async function stopServer() { if (server) { server.removeAllListeners('exit'); server.kill(); await new Promise((r) => server.once('close', r)); } }

class Client {
  constructor() { this.cookie = ''; }
  async req(method, url, body, { form, headers = {} } = {}) {
    const h = { 'X-Requested-With': 'byfluence-support', ...headers };
    if (this.cookie) h.cookie = this.cookie;
    let payload;
    if (form) payload = form; else if (body !== undefined) { h['content-type'] = 'application/json'; payload = JSON.stringify(body); }
    const res = await fetch(BASE + url, { method, headers: h, body: payload });
    const set = res.headers.get('set-cookie');
    if (set) this.cookie = set.split(';')[0];
    const data = (res.headers.get('content-type') || '').includes('json') ? await res.json() : await res.text();
    return { status: res.status, data };
  }
  get(u) { return this.req('GET', u); }
  post(u, b, o) { return this.req('POST', u, b, o); }
  patch(u, b) { return this.req('PATCH', u, b); }
  put(u, b) { return this.req('PUT', u, b); }
  async login(email, password = 'Demo-pass-2026') { const r = await this.post('/auth/login', { email, password }); assert.equal(r.status, 200, JSON.stringify(r.data)); return r.data.user; }
}
const admin = new Client();
const sup = new Client();
const agent = new Client();
const agent2 = new Client();

before(async () => {
  execFileSync(process.execPath, ['--no-warnings=ExperimentalWarning', 'server/seed/seed.js'], { cwd: ROOT, env: ENV, stdio: 'pipe' });
  await startServer();
  await admin.login('admin@byfluence.local', 'Admin-pass-2026');
  await sup.login('supervisor@byfluence.local');
  await agent.login('dawit@byfluence.local');
  await agent2.login('meron@byfluence.local');
});
after(async () => { await stopServer(); fs.rmSync(DATA_DIR, { recursive: true, force: true }); });

const newTicket = (c, extra = {}) => c.post('/tickets', {
  title: 'Paid but no meeting link received', description: 'Customer paid for a consultation; no Google Meet link.', customer_name: 'Test Customer',
  customer_phone: '0911000000', category_id: extra.category_id, priority: 'medium', channel: 'telegram', ...extra,
});

test('authentication and CSRF protection', async () => {
  const anon = new Client();
  assert.equal((await anon.get('/dashboard')).status, 401);
  const r = await fetch(`${BASE}/tickets`, { method: 'POST', headers: { cookie: agent.cookie, 'content-type': 'application/json' }, body: '{}' });
  assert.equal(r.status, 403, 'mutations without the app header are rejected');
  assert.equal((await anon.post('/auth/login', { email: 'dawit@byfluence.local', password: 'wrong-password-1' })).status, 400);
});

test('dashboard statistics come from stored tickets', async () => {
  const before = (await agent.get('/dashboard')).data.stats;
  const cats = (await agent.get('/categories?scope=kb')).data;
  const t = await newTicket(agent, { category_id: cats[0].id });
  assert.equal(t.status, 201);
  const afterStats = (await agent.get('/dashboard')).data.stats;
  assert.equal(afterStats.total, before.total + 1);
  assert.equal(afterStats.open, before.open + 1);
});

test('ticket lifecycle enforces documented resolution', async () => {
  const cats = (await agent.get('/categories?scope=kb')).data;
  const { data: t } = await newTicket(agent, { category_id: cats[5].id, subcategory_id: cats[5].subcategories[1].id });
  assert.match(t.number, /^BYF-\d{5}$/);
  assert.equal((await agent.post(`/tickets/${t.id}/status`, { status: 'resolved' })).status, 400, 'cannot set resolved via plain status');
  assert.equal((await agent.post(`/tickets/${t.id}/resolve`, { root_cause: 'x' })).status, 400, 'resolve needs all fields');
  assert.equal((await agent.post(`/tickets/${t.id}/close`, { close_type: 'resolved' })).status, 400, 'cannot close unresolved as resolved');
  assert.equal((await agent.post(`/tickets/${t.id}/close`, { close_type: 'other', note: 'short' })).status, 400, 'unresolved close needs explanation');
  // escalation blocks resolution until decided
  const esc = await agent.post(`/tickets/${t.id}/escalations`, { level: 3, department: 'technical', reason: 'Meet link generation failed for paid booking.' });
  assert.equal(esc.status, 201);
  const full = { root_cause: 'API timeout', actions_taken: 'Regenerated link', resolution: 'Customer has link', customer_notified: true };
  assert.equal((await agent.post(`/tickets/${t.id}/resolve`, full)).status, 400, 'open escalation blocks resolve');
  assert.equal((await agent.post(`/escalations/${esc.data.id}/decide`, { decision: 'Link regenerated by engineering.' })).status, 403, 'agent cannot decide others\' escalation');
  assert.equal((await sup.post(`/escalations/${esc.data.id}/decide`, { decision: 'Link regenerated by engineering.' })).status, 200);
  assert.equal((await agent.get(`/tickets/${t.id}`)).data.ticket.status, 'in_progress');
  assert.equal((await agent.post(`/tickets/${t.id}/resolve`, full)).status, 200);
  assert.equal((await agent.post(`/tickets/${t.id}/close`, { close_type: 'resolved' })).status, 200);
  assert.equal((await agent.post(`/tickets/${t.id}/reopen`, { reason: 'Customer says link still broken.' })).status, 200);
  const d = (await agent.get(`/tickets/${t.id}`)).data;
  assert.equal(d.ticket.status, 'reopened');
  assert.equal(d.ticket.reopen_count, 1);
  const types = d.events.map((e) => e.type);
  for (const ty of ['reported', 'created', 'escalated', 'escalation_decided', 'resolved', 'closed', 'reopened']) assert.ok(types.includes(ty), `timeline has ${ty}`);
  assert.equal(d.events.find((e) => e.type === 'resolved').data.resolution, 'Customer has link', 'original resolution preserved');
});

test('first response is recorded from outbound communication', async () => {
  const cats = (await agent.get('/categories?scope=kb')).data;
  const { data: t } = await newTicket(agent, { category_id: cats[0].id });
  await agent.post(`/tickets/${t.id}/communications`, { direction: 'outbound', channel: 'telegram', summary: 'Sent greeting' });
  const d = (await agent.get(`/tickets/${t.id}`)).data.ticket;
  assert.ok(d.first_response_at);
  assert.equal(d.status, 'open');
});

test('agents only see and change their own or unassigned tickets', async () => {
  const cats = (await agent.get('/categories?scope=kb')).data;
  const { data: t } = await newTicket(agent, { category_id: cats[0].id });
  assert.equal((await agent2.get(`/tickets/${t.id}`)).status, 403);
  assert.equal((await agent2.patch(`/tickets/${t.id}`, { priority: 'high' })).status, 403);
  assert.equal((await sup.get(`/tickets/${t.id}`)).status, 200, 'supervisor sees all');
  const meron = (await agent.get('/users')).data.find((u) => u.email === 'meron@byfluence.local');
  assert.equal((await agent.patch(`/tickets/${t.id}`, { assignee_id: meron.id })).status, 403, 'agent cannot assign to others');
  assert.equal((await agent.req('DELETE', `/tickets/${t.id}`)).status, 403);
  assert.equal((await admin.req('DELETE', `/tickets/${t.id}`)).status, 400, 'real tickets can never be deleted');
});

test('documentation versioning, review workflow and policy permissions', async () => {
  const { data: d } = await sup.get('/docs/con-missing-meet-link?view=0');
  const sections = d.doc.sections.map((s) => (s.key === 'description' ? { ...s, html: '<p>Updated description</p><script>alert(1)</script>' } : s));
  assert.equal((await sup.put('/docs/con-missing-meet-link', { sections })).status, 400, 'change summary required');
  const up = await sup.put('/docs/con-missing-meet-link', { sections, change_summary: 'Test edit', expected_version: d.doc.version });
  assert.equal(up.status, 200);
  assert.equal(up.data.version, d.doc.version + 1);
  assert.ok(!JSON.stringify(up.data.sections).includes('<script'), 'HTML is sanitized');
  assert.equal((await sup.put('/docs/con-missing-meet-link', { sections, change_summary: 'stale', expected_version: d.doc.version })).status, 409, 'stale edit rejected');
  const versions = (await sup.get('/docs/con-missing-meet-link/versions')).data;
  assert.ok(versions.length >= 2);
  assert.equal((await sup.post(`/docs/con-missing-meet-link/restore/${versions[1].id}`)).status, 200);
  assert.ok(!(await sup.get('/docs/con-missing-meet-link?view=0')).data.doc.sections.some((s) => s.html.includes('Updated description')), 'restored');
  // agents cannot edit; supervisors cannot publish policies
  assert.equal((await agent.put('/docs/con-missing-meet-link', { change_summary: 'x' })).status, 403);
  const draft = await sup.post('/docs', { type: 'policy', title: 'Test policy draft', sections: [], status: 'published' });
  assert.equal(draft.status, 201);
  assert.equal(draft.data.status, 'review', 'supervisor policy goes to review');
  assert.equal((await sup.post(`/docs/${draft.data.slug}/status`, { status: 'published' })).status, 403);
  assert.equal((await admin.post(`/docs/${draft.data.slug}/status`, { status: 'published' })).status, 200);
  assert.equal((await agent.get(`/docs?status=review`)).data.every((x) => x.status === 'published'), true, 'agents only see published');
});

test('search finds articles from customer wording', async () => {
  const r = (await agent.get('/search?q=' + encodeURIComponent("seller didn't join meeting"))).data;
  assert.ok(r.results.slice(0, 5).some((x) => x.slug === 'con-seller-no-show'), JSON.stringify(r.results.slice(0, 5).map((x) => x.slug)));
  const r2 = (await agent.get('/search?q=' + encodeURIComponent('payment successful but booking missing'))).data;
  assert.ok(r2.results.slice(0, 5).some((x) => x.slug === 'pay-paid-booking-not-confirmed'));
  const r3 = (await agent.get('/search?q=' + encodeURIComponent('forgot pasword'))).data; // typo
  assert.ok(r3.results.slice(0, 5).some((x) => x.slug === 'acc-forgot-password'));
});

test('AI knowledge API never exposes internal notes or drafts', async () => {
  const k = await admin.post('/admin/api-keys', { name: 'test bot', scopes: ['kb:read'] });
  assert.equal(k.status, 201);
  const auth = { Authorization: `Bearer ${k.data.key}` };
  const noKey = await fetch(`${BASE}/v1/kb/search?q=refund`);
  assert.equal(noKey.status, 401);
  const res = await (await fetch(`${BASE}/v1/kb/search?q=seller+did+not+join&full=1`, { headers: auth })).json();
  assert.ok(res.results.length > 0);
  for (const d of res.results) assert.ok(!d.sections.some((s) => s.key === 'internal'), 'internal notes stripped');
  const doc = await (await fetch(`${BASE}/v1/kb/docs/con-seller-no-show`, { headers: auth })).json();
  assert.equal(doc.policy_pending, true);
  const tick = await fetch(`${BASE}/v1/tickets`, { method: 'POST', headers: { ...auth, 'content-type': 'application/json' }, body: '{}' });
  assert.equal(tick.status, 403, 'kb:read key cannot create tickets');
});

test('uploads reject disguised files and are private', async () => {
  const cats = (await agent.get('/categories?scope=kb')).data;
  const { data: t } = await newTicket(agent, { category_id: cats[0].id });
  const fake = new FormData();
  fake.append('files', new Blob(['MZ this is an exe'], { type: 'image/png' }), 'receipt.png');
  assert.equal((await agent.post(`/tickets/${t.id}/attachments`, undefined, { form: fake })).status, 400);
  const png = Buffer.from('89504E470D0A1A0A0000000D4948445200000001000000010806000000', 'hex');
  const ok = new FormData();
  ok.append('files', new Blob([png], { type: 'image/png' }), 'receipt.png');
  const up = await agent.post(`/tickets/${t.id}/attachments`, undefined, { form: ok });
  assert.equal(up.status, 201);
  assert.equal((await agent2.get(`/files/${up.data[0].id}`)).status, 403, 'other agents cannot download');
  assert.equal((await new Client().get(`/files/${up.data[0].id}`)).status, 401);
});

test('data persists across server restarts and actions are audited', async () => {
  const cats = (await agent.get('/categories?scope=kb')).data;
  const { data: t } = await newTicket(agent, { category_id: cats[0].id, title: 'Persistence check ticket' });
  await stopServer();
  await startServer();
  const c = new Client();
  await c.login('dawit@byfluence.local');
  assert.equal((await c.get(`/tickets/${t.number}`)).data.ticket.title, 'Persistence check ticket');
  const audit = (await admin.get('/audit?action=ticket')).data;
  assert.ok(audit.rows.some((r) => r.entity_id === t.number && r.action === 'ticket.create'));
  assert.equal((await agent.get('/audit')).status, 403);
});
