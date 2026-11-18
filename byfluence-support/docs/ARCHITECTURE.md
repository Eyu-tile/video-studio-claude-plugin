# Architecture

## 1. Overview

```
Browser (React SPA)  ──HTTPS──▶  Express API (Node 22)  ──▶  SQLite (node:sqlite, WAL)
   Vite build in dist/             /api/*   session-cookie auth        data/byfluence-support.db
                                   /api/v1/* API-key auth (AI bot)     data/uploads/ (private files)
                                   in-memory MiniSearch index
```

The whole system is **one Node process and one database file**. That keeps it easy to run, back up and move. For a single support team it handles tens of thousands of tickets comfortably.

**Scaling path:** every table maps 1:1 to PostgreSQL. All database access goes through `server/db.js` (`all/get/run/tx`), so migrating means swapping that module and running the same schema. The search index rebuilds from the database, so several app instances can each keep their own copy.

| Layer | Choice | Why |
|---|---|---|
| Frontend | React 18, React Router, Tailwind CSS v4 | Fast, maintainable component architecture; desktop-first with mobile support; light and dark mode |
| Rich text | TipTap 3 | Headings, lists, checklists, tables, links, images, code blocks, and custom callouts (info, tip, warning, policy pending) |
| Charts | Recharts | Reports |
| Backend | Express 4 | Simple, well understood |
| Database | SQLite through `node:sqlite` | No native build and no separate server; ACID; WAL mode |
| Search | MiniSearch | BM25 relevance, fuzzy matching (typo tolerance), prefix matching, field boosts and synonym expansion |
| Auth | scrypt hashes, httpOnly SameSite=Strict session cookies | No third-party auth service needed |

## 2. Navigation

| Section | Route | Purpose |
|---|---|---|
| Dashboard | `/` | Live statistics from ticket data, urgent issues, recent issues, my follow-ups, announcements, recent docs, quick access, supervisor checks |
| Customer Issues | `/tickets`, `/tickets/:number` | Ticketing: 12 views, filters, table and Kanban, ticket detail with timeline |
| Escalation Center | `/escalations` | Levels 2–4; update progress, record decisions |
| Knowledge Base | `/kb`, `/kb/c/:category`, `/kb/:slug` | 16 categories → subcategories → articles |
| Customer FAQs | `/faqs` | Bilingual short answers, copy button |
| Response Templates | `/templates/:slug` | Fill placeholders, switch Amharic/English, copy, log to ticket |
| Troubleshooting Guides | `/troubleshooting` | Master diagnostic guides |
| Support SOPs | `/sops` | 23 procedures |
| Customer Communication | `/communication` | Tone, language, channel and difficult-conversation guides |
| Policies & Guidelines | `/policies` | Policies, Feature Status, Policy Pending tracker |
| Training Center | `/training` | 10 modules, quizzes, team progress |
| Announcements | `/announcements` | Priority, expiry, read tracking |
| Documentation Management | `/manage` | All content, templates, review queue, feedback, categories, knowledge gaps |
| Performance Reports | `/reports` | Metrics, charts, employee table, CSV export |
| Settings | `/settings` | Profile, team, service targets, departments, feature status, quick links, synonyms, integrations, backups, audit log |
| Search | `Ctrl/⌘ K` anywhere; `/search?q=` | Global search |

## 3. Data model

| Table | Holds |
|---|---|
| `users` | Employees: role (admin, supervisor, agent), department, active flag, temporary-password flag, preferences |
| `sessions` | Session tokens, stored only as SHA-256 hashes, with expiry |
| `categories` | One tree per scope (`kb`, `template`, `sop`, `policy`, `communication`); `parent_id` marks subcategories |
| `documents` | Articles, troubleshooting guides, FAQs, SOPs, policies and guides. See below. |
| `templates` | Response templates: channel, style, Amharic and English subject and message, usage notes, usage count |
| `versions` | A snapshot of a document, template or training module on every change, with change summary, author and time. Restore creates a new version. |
| `doc_feedback` | "Helpful?" votes, "outdated" reports and edit suggestions; open, done or dismissed |
| `tickets` | Customer, issue, category, priority, status, channel, references, assignee, reported time, due time, first response, escalation level, resolution fields, close reason, reopen count, CSAT, linked docs, `is_demo` |
| `ticket_events` | **The timeline.** Every action is a typed event with JSON data, author and time. |
| `escalations` | Level 2–4, department, reason, assignee, status, progress, expected follow-up, decision, decided by and when |
| `followups` | Due time, reason, assignee, status (pending, done, cancelled) |
| `attachments` | Private files: random stored name, checked MIME type and size |
| `announcements`, `announcement_reads` | Announcements with priority, type, status, pinned flag, expiry and per-user read state |
| `training_modules`, `training_progress` | Lesson sections, quiz (answers never sent to the browser) and best score per user |
| `settings` | JSON values: service targets, departments, features, quick links, search synonyms, support info, placeholders, training pass mark |
| `audit_log` | Who did what, to what, from which IP, and when |
| `search_log` | Search queries. Queries with no results drive the "knowledge gaps" report. |
| `doc_views` | Each user's recently viewed documents |
| `api_keys` | Integration keys, stored hashed, with scopes `kb:read` and `tickets:create` |

The fields of `documents`:

- **type:** `article`, `troubleshooting`, `faq`, `sop`, `policy` or `guide`
- **content:** title, summary, and `sections` (a JSON list of key, label and HTML)
- **links and handling:** tags, related docs, linked templates, feature dependencies, audience, default priority and escalation department
- **flags:** `policy_pending` and `ai_visible`
- **workflow:** `status` (draft, review, published, archived), version, view count and helpful votes

### Document sections

Every article uses the same keys, so the interface can treat them specially:

- Response sections are grouped into the bilingual **Customer responses** card with copy buttons: `response_en/am`, `short_en/am`, `followup_en/am` and `answer_en/am`.
- `escalation` is shown as an orange box.
- `policy_pending` is shown as an amber "do not present as rules" box.
- `internal` is shown as an "employees only" box and is **never** sent to the AI API.

Custom sections are allowed.

## 4. Ticket lifecycle

```
new ──▶ open ──▶ under_review ──▶ waiting_customer / waiting_seller ──▶ in_progress ──▶ resolved ──▶ closed
                       │                                                    ▲            │            │
                       └──────────── escalated (via Escalate only) ─────────┘            └── reopened ◀┘
```

- **Changing status:** `new`, `open`, `under_review`, `waiting_*` and `in_progress` can be set directly.
- **Escalated:** a ticket only becomes `escalated` by creating an escalation, which records level, department, reason, owner and expected follow-up. Recording the decision moves it to `in_progress`.
- **Resolved:** requires root cause, actions taken, final resolution and whether the customer was notified. It is **blocked while an escalation is open**.
- **Closed:** if the ticket wasn't resolved first, closing needs a reason (duplicate, no response, withdrawn, spam, out of scope, other) and a written explanation.
- **Reopened:** requires a reason. History and the previous resolution stay in the timeline.
- **Due time:** `reported_at` plus the resolution target for the ticket's priority (Settings → Service targets). A ticket is overdue when it is open and past its due time.
- **First response:** the first outbound customer contact logged on the ticket. The first contact also moves `new` to `open`.
- **Logging only:** nothing is sent to customers automatically. Agents log what they sent. The template screen's "I sent it — log on ticket" does this in one click.
- **Deletion:** real tickets can never be deleted; only `is_demo` tickets can.

## 5. Search

- **One index:** an in-memory MiniSearch index covers documents, templates, announcements and training. Field boosts are title 4, tags 3, summary 2, body 1. Internal notes are never indexed.
- **Typo tolerance:** fuzzy matching (edit distance about 20% for longer words) plus prefix matching on the last word.
- **Synonyms:** about 25 default groups, editable in Settings. If a query contains any phrase in a group, the other phrases are searched as well at a lower weight. Examples: *didn't join ↔ no-show*, *money ↔ payment ↔ ክፍያ*, *link ↔ google meet*.
- **Ranking:** a bonus when every query word is in the title, and a small bonus for articles and guides.
- **Tickets:** searched with SQL by number, name, email, phone, order, transaction or consultation reference, or title. Results respect visibility rules.
- **Index updates:** the index is marked out of date on every write and rebuilt lazily.
- **Tracking:** every search is logged. Searches with no results show up as **knowledge gaps** for supervisors.

## 6. Security

- **Passwords:** scrypt with a per-password salt; at least 10 characters with letters and numbers. Temporary passwords force a change at first sign-in.
- **Sessions:** random 256-bit tokens, stored as hashes, in httpOnly cookies with SameSite=Strict (Secure in production). Sessions expire, and changing your password signs out your other sessions.
- **CSRF:** every request that changes data needs the `X-Requested-With: byfluence-support` header and a SameSite=Strict cookie.
- **Login throttling:** after 5 failed attempts per email and IP, waits increase exponentially.
- **Authorization:** every API route checks permissions from `server/permissions.js`. The browser only hides controls; the server enforces the rules.
  - Agents see tickets assigned to them, created by them, or unassigned.
  - Supervisors see all tickets.
  - Only admins publish policies.
- **Sanitization:** all rich-text HTML is sanitized on the server against an allow-list, so no scripts, event handlers or unsafe links get through.
- **Uploads:**
  - allow-listed types only (PNG, JPG, WEBP, GIF, PDF, TXT), with a size limit
  - **magic-byte check**, so a renamed `.exe` is rejected
  - stored under a random name outside the web root, served only to employees who can see the ticket, with `nosniff`
  - every download of a ticket file is audited
- **Security headers:** Helmet with a Content Security Policy (no inline scripts).
- **Sensitive-data warnings:** the ticket form and composer warn when text looks like an OTP, PIN or card number.
- **Audit log:** covers logins (including failures), every ticket action, escalations, document and template changes, settings changes, uploads, file views, backups, API key changes and demo-data deletion.

## 7. AI assistant integration (future Telegram bot)

`/api/v1/*` uses API keys created in Settings → Integrations.

| Endpoint | Returns |
|---|---|
| `GET /kb/search?q=&limit=&full=1` | Best matching published, AI-visible documents |
| `GET /kb/docs/:id` | One document. Internal-notes sections are removed. |
| `GET /kb/faqs`, `GET /kb/templates` | FAQs and published templates (Amharic and English) |
| `GET /kb/escalation` | Departments, feature status, and the rules for handing off to a human |
| `POST /tickets` (scope `tickets:create`) | Creates a ticket when the bot hands off to a human. Priority can be at most high. Logged as created via integration. |

What the API guarantees:

- It never returns drafts, archived content, internal notes, tickets, customer data or the audit log.
- Each document includes `policy_pending`, `requires_human_if`, `features` (live status) and `escalation_department`. The bot can then refuse to state unapproved rules and hand off to a human.
- Administrators can untick *Available to AI assistant* on any document.

## 8. Content pipeline

The initial content lives in `content/*.md`, following `content/FORMAT.md`.

- **Checking:** `npm run check:content` checks structure, categories, departments, feature keys and placeholders, and warns about concrete numbers or timelines in customer-facing text (to catch invented policies).
- **Loading:** `npm run seed` converts it to HTML (callouts and checklists included) and loads it into the database.
- **After seeding:** content is edited in the app. `npm run seed -- --content` re-imports Markdown changes without overwriting anything edited in the app.
