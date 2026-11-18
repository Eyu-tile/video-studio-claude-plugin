import crypto from 'node:crypto';
import { get, run, nowIso, parseJson } from './db.js';
import { can, permissionsFor } from './permissions.js';

const SESSION_DAYS = Number(process.env.SESSION_DAYS || 7);
export const COOKIE = 'byf_session';

export function hashPassword(password) {
  const salt = crypto.randomBytes(16);
  const hash = crypto.scryptSync(password, salt, 64, { N: 16384, r: 8, p: 1 });
  return `scrypt$${salt.toString('base64')}$${hash.toString('base64')}`;
}

export function verifyPassword(password, stored) {
  const [alg, saltB64, hashB64] = String(stored).split('$');
  if (alg !== 'scrypt' || !saltB64 || !hashB64) return false;
  const expected = Buffer.from(hashB64, 'base64');
  const actual = crypto.scryptSync(password, Buffer.from(saltB64, 'base64'), expected.length, { N: 16384, r: 8, p: 1 });
  return crypto.timingSafeEqual(expected, actual);
}

export function validatePassword(pw) {
  if (typeof pw !== 'string' || pw.length < 10) return 'Password must be at least 10 characters.';
  if (!/[A-Za-z]/.test(pw) || !/\d/.test(pw)) return 'Password must contain letters and numbers.';
  return null;
}

const sha256 = (s) => crypto.createHash('sha256').update(s).digest('hex');

export function createSession(userId, req) {
  const token = crypto.randomBytes(32).toString('base64url');
  const expires = new Date(Date.now() + SESSION_DAYS * 864e5).toISOString();
  run('INSERT INTO sessions(token_hash,user_id,created_at,expires_at,ip,user_agent) VALUES (?,?,?,?,?,?)',
    sha256(token), userId, nowIso(), expires, req.ip, String(req.headers['user-agent'] || '').slice(0, 200));
  return { token, expires };
}

export function destroySession(token) {
  if (token) run('DELETE FROM sessions WHERE token_hash = ?', sha256(token));
}

export function publicUser(u) {
  if (!u) return null;
  return {
    id: u.id, name: u.name, email: u.email, role: u.role, department: u.department, title: u.title,
    active: !!u.active, must_change_password: !!u.must_change_password,
    preferences: parseJson(u.preferences, {}), created_at: u.created_at, last_login_at: u.last_login_at,
    permissions: permissionsFor(u.role),
  };
}

/** Express middleware: attaches req.user if a valid session cookie is present. */
export function loadUser(req, _res, next) {
  const token = req.cookies?.[COOKIE];
  if (token) {
    const row = get(`SELECT u.* FROM sessions s JOIN users u ON u.id = s.user_id
                     WHERE s.token_hash = ? AND s.expires_at > ? AND u.active = 1`, sha256(token), nowIso());
    if (row) req.user = row;
  }
  next();
}

export function requireAuth(req, res, next) {
  if (!req.user) return res.status(401).json({ error: 'Please sign in.' });
  next();
}

export function requirePerm(...perms) {
  return (req, res, next) => {
    if (!req.user) return res.status(401).json({ error: 'Please sign in.' });
    if (!perms.some((p) => can(req.user, p))) return res.status(403).json({ error: 'You do not have permission to do this.' });
    next();
  };
}

// --- API keys (for the future AI assistant / integrations) ---
export function createApiKey() {
  const raw = `byf_${crypto.randomBytes(24).toString('base64url')}`;
  return { raw, hash: sha256(raw), prefix: raw.slice(0, 10) };
}
export function apiKeyAuth(scope) {
  return (req, res, next) => {
    const header = req.headers.authorization || '';
    const raw = header.startsWith('Bearer ') ? header.slice(7) : req.headers['x-api-key'];
    if (!raw) return res.status(401).json({ error: 'API key required' });
    const key = get('SELECT * FROM api_keys WHERE key_hash = ? AND revoked_at IS NULL', sha256(String(raw)));
    if (!key || !parseJson(key.scopes, []).includes(scope)) return res.status(403).json({ error: 'Invalid API key or scope' });
    run('UPDATE api_keys SET last_used_at = ? WHERE id = ?', nowIso(), key.id);
    req.apiKey = key;
    next();
  };
}

// Simple in-memory login throttle (per email + IP)
const attempts = new Map();
export function loginThrottle(key) {
  const now = Date.now();
  const a = attempts.get(key) || { n: 0, until: 0, first: now };
  if (a.until > now) return Math.ceil((a.until - now) / 1000);
  return 0;
}
export function loginFailed(key) {
  const now = Date.now();
  const a = attempts.get(key) || { n: 0, until: 0, first: now };
  if (now - a.first > 15 * 60e3) { a.n = 0; a.first = now; }
  a.n += 1;
  if (a.n >= 5) a.until = now + Math.min(15 * 60e3, 30e3 * 2 ** (a.n - 5));
  attempts.set(key, a);
}
export function loginSucceeded(key) { attempts.delete(key); }

export { can };
