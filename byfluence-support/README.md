# Byfluence Support Operating System

An internal web application for the Byfluence customer support team. It combines:

- **Knowledge base**: 447 documents (282 issue articles, 13 troubleshooting guides, 101 FAQs, 23 SOPs, 15 policies, 13 communication guides), including bilingual responses
- **Response templates**: 86, in Amharic and English
- **Ticketing system**: table and Kanban views
- **Escalation center**
- **SOPs, communication guides and policies**: includes a *Policy Pending* tracker and a *Feature Status* page
- **Training center**: 10 modules with knowledge checks
- **Announcements**
- **Documentation management**: rich-text editor, review workflow, version history and restore
- **Performance reports**
- **Role-based access**, an **audit log**, **backups**, and a **read-only knowledge API** for the future Telegram AI assistant

> Internal use only. Customer information in this system is confidential.

---

## Quick start (development)

Requirements: **Node.js 22.13 or newer**. No external database is needed. The app uses Node's built-in SQLite.

```bash
cd byfluence-support
npm install
npm run seed          # creates data/byfluence-support.db, the admin account, all content and DEMO data
npm run dev           # API on :4000, web app on http://localhost:5173
```

`npm run seed` prints the administrator email (`admin@byfluence.local`) and a **temporary password**. You must change it at first sign-in.

These demo employee accounts are created only for evaluation. The password for all of them is `Demo-pass-2026`.

| Account | Role |
|---|---|
| supervisor@byfluence.local | Support Supervisor |
| dawit@byfluence.local, meron@byfluence.local, yonas@byfluence.local | Support Agents |
| payments@byfluence.local | Agent (Payments & Finance) |
| safety@byfluence.local | Agent (Trust & Safety) |

Before going live: deactivate demo accounts (Settings → Team) and delete demo tickets (Settings → Data & backup → *Delete demo data*).

### Seed options

```bash
npm run seed -- --no-demo     # production: admin + content only
npm run seed -- --content     # re-import Markdown content into an existing DB (never overwrites docs edited in the app)
npm run seed -- --reset       # ⚠ wipes the database and starts over
ADMIN_EMAIL=you@byfluence.com ADMIN_PASSWORD='…' ADMIN_NAME='Your Name' npm run seed -- --no-demo
```

## Production

```bash
npm ci
npm run build                          # builds the web app into dist/
npm run seed -- --no-demo              # first time only
PORT=4000 npm start                    # serves API + web app on one port
```

Run it behind HTTPS (nginx, Caddy or a cloud load balancer). Session cookies are `Secure` when `NODE_ENV=production`. If TLS ends at a proxy, also set `TRUST_PROXY=1`.

| Variable | Default | Purpose |
|---|---|---|
| `PORT` | 4000 | HTTP port |
| `DATA_DIR` | `./data` | Database, uploads and backups. Put this on a persistent, backed-up disk. |
| `NODE_ENV` | — | Set to `production` for secure cookies |
| `TRUST_PROXY` | — | Set to `1` when behind a reverse proxy |
| `COOKIE_SECURE` | — | Set to `false` only for HTTP testing |
| `SESSION_DAYS` | 7 | Login session length |
| `MAX_UPLOAD_MB` | 10 | Maximum attachment size |

A `Dockerfile` is included:

```bash
docker build -t byfluence-support .
```

```bash
docker run -p 4000:4000 -v byf-data:/app/data byfluence-support
```

The first run of the container seeds the database without demo data. Read the admin password from the container log.

### Backups

- **Database:** Settings → Data & backup → *Download database backup*. This is a consistent SQLite snapshot made with `VACUUM INTO`.
- **Uploads:** also back up the `DATA_DIR/uploads` folder.
- **Automating it:** schedule a copy of `DATA_DIR`, or call `GET /api/admin/backup` with an admin session.
- **Restoring:** stop the server, replace `data/byfluence-support.db` with the backup file, then start it again.

## Testing

```bash
npm test                 # 10 end-to-end API tests on a throwaway database
npm run check:content    # validates every Markdown content file
```

The tests cover:

- authentication and CSRF protection
- dashboard statistics calculated from real tickets
- the full ticket lifecycle, with its rules on resolution, closing and escalation
- agent visibility and permission limits
- document versioning, restore and HTML sanitization
- policy publishing rights
- search by customer wording, synonyms and typos
- the AI API privacy filter
- upload validation, including disguised files
- data persisting across restarts
- the audit log

## Project structure

```
byfluence-support/
├── client/                 React app (Vite + Tailwind CSS v4 + TipTap + Recharts)
│   └── src/{components,pages,lib}
├── server/
│   ├── index.js            Express app, security headers, CSRF, routing
│   ├── db.js               SQLite schema & helpers
│   ├── auth.js             scrypt password hashing, sessions, API keys, login throttling
│   ├── permissions.js      role → permission matrix (enforced server-side)
│   ├── search.js           MiniSearch index (BM25, fuzzy, prefix) + synonym expansion
│   ├── routes/             tickets, operations (escalations/follow-ups/files), content, insights, admin, api-v1
│   ├── content/            Markdown parser + content validator
│   └── seed/               seeder, Markdown→HTML, demo data
├── content/                Initial documentation as Markdown (see content/FORMAT.md)
├── docs/                   Architecture, admin guide, agent guide, policy decisions
└── tests/                  API test suite
```

## Documentation

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): architecture, database schema, ticket lifecycle, search, security and the AI integration
- [docs/ADMIN_GUIDE.md](docs/ADMIN_GUIDE.md): for administrators and supervisors
- [docs/AGENT_GUIDE.md](docs/AGENT_GUIDE.md): for support employees
- [docs/POLICY_DECISIONS.md](docs/POLICY_DECISIONS.md): **decisions Byfluence management must make** before the "Policy Pending Approval" markers can be removed
- [content/FORMAT.md](content/FORMAT.md): how the seed content is written
