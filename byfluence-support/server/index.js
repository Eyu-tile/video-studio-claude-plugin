import express from 'express';
import cookieParser from 'cookie-parser';
import helmet from 'helmet';
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, get } from './db.js';
import { loadUser, requireAuth } from './auth.js';
import { HttpError } from './util.js';
import ticketRoutes from './routes/tickets.js';
import opsRoutes from './routes/operations.js';
import contentRoutes from './routes/content.js';
import insightRoutes from './routes/insights.js';
import adminRoutes, { pub as publicRoutes } from './routes/admin.js';
import apiV1 from './routes/api-v1.js';
import { ensureIndex } from './search.js';

const PORT = Number(process.env.PORT || 4000);
const app = express();
app.disable('x-powered-by');
app.set('trust proxy', process.env.TRUST_PROXY === '1' ? 1 : false);

app.use(helmet({
  contentSecurityPolicy: {
    useDefaults: true,
    directives: {
      'img-src': ["'self'", 'data:', 'blob:'],
      'style-src': ["'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'],
      'font-src': ["'self'", 'https://fonts.gstatic.com', 'data:'],
      'connect-src': ["'self'"],
    },
  },
  crossOriginEmbedderPolicy: false,
}));
app.use(express.json({ limit: '2mb' }));
app.use(cookieParser());

// CSRF defence: state-changing requests must come from our own frontend (custom header + SameSite=Strict cookie).
app.use('/api', (req, res, next) => {
  if (['GET', 'HEAD', 'OPTIONS'].includes(req.method) || req.path.startsWith('/v1/')) return next();
  if (req.get('X-Requested-With') !== 'byfluence-support') return res.status(403).json({ error: 'Missing request header.' });
  next();
});

app.get('/api/health', (_req, res) => res.json({ ok: true, users: get('SELECT COUNT(*) n FROM users').n }));
app.use('/api/v1', apiV1);
app.use('/api', loadUser, publicRoutes);
app.use('/api', requireAuth);
app.use('/api', (req, res, next) => {
  // Users with a temporary password may only change it.
  if (req.user.must_change_password && !['/auth/me', '/me/password', '/auth/logout', '/settings'].includes(req.path)) {
    return res.status(428).json({ error: 'Please set a new password first.', code: 'PASSWORD_CHANGE_REQUIRED' });
  }
  next();
});
app.use('/api', adminRoutes);
app.use('/api/tickets', ticketRoutes);
app.use('/api', opsRoutes);
app.use('/api', contentRoutes);
app.use('/api', insightRoutes);
app.use('/api', (_req, res) => res.status(404).json({ error: 'Not found.' }));

// Serve the built frontend in production
const dist = path.join(ROOT, 'dist');
if (fs.existsSync(dist)) {
  app.use(express.static(dist, { index: false, maxAge: '1h' }));
  app.get('*', (_req, res) => res.sendFile(path.join(dist, 'index.html')));
}

// eslint-disable-next-line no-unused-vars
app.use((err, req, res, _next) => {
  if (err instanceof HttpError || err.status) return res.status(err.status || 400).json({ error: err.message });
  if (err.type === 'entity.parse.failed') return res.status(400).json({ error: 'Invalid JSON.' });
  console.error(err);
  res.status(500).json({ error: 'Something went wrong on the server. The error has been logged.' });
});

const users = get('SELECT COUNT(*) n FROM users').n;
if (!users) {
  console.warn('\n⚠  The database is empty. Run `npm run seed` to create the admin account and initial content.\n');
}
ensureIndex();
app.listen(PORT, () => console.log(`Byfluence Support API listening on http://localhost:${PORT}`));
