# Administrator & Supervisor Guide

## First-day setup (administrator)

1. **Sign in** with the admin account printed by `npm run seed` and set a new password.
2. **Settings → Feature Status:** set each feature and payment method to *Live*, *Planned*, *Unconfirmed*… and tick **Verified** once you've checked it in production. Agents rely on this page, so it matters more than any other setting.
3. **Settings → Quick links & channels:** enter the official Telegram handle, support email, phone number and hours. Leave a field empty until it is officially confirmed.
4. **Settings → Service targets:** set the internal first-response and resolution targets for each priority, then tick *approved by management*. The defaults are placeholders.
5. **Settings → Departments:** adjust the escalation departments if your organisation is different.
6. **Settings → Team & roles:** add employees. Each gets a temporary password, shown once; share it securely. Deactivate the demo accounts.
7. **Settings → Data & backup:** delete the demo data when you go live, and set up regular backups (see the README).
8. **Policies & Guidelines → Policy Pending Tracker:** work through the decisions with management (see `docs/POLICY_DECISIONS.md`).

## Roles

| Role | Can |
|---|---|
| **Support Agent** | Read published content; search; copy templates; create tickets; work tickets assigned to them or unassigned; notes; communication log; follow-ups; attachments; escalate; resolve and close their own tickets; take training |
| **Support Supervisor** | Everything agents can do, plus: see and assign all tickets; reopen; decide or reassign escalations; create and edit content; publish non-policy content; announcements; reports; team training progress; review feedback |
| **Administrator** | Everything, plus: publish and approve **policies**; manage categories, employees, settings and API keys; audit log; backups; permanently delete archived content; delete demo data |

The server enforces every permission. Hiding a button is never the only protection.

## Managing documentation (Documentation Management)

- **Create:** click **Create** and pick a type. New articles start with the standard structure, from Issue Description through Internal Notes. Add or remove sections, reorder them, and use the toolbar for headings, lists, checklists, tables, links, images and callouts (info, tip, warning, **policy pending**).
- **Workflow:** Draft → **Submit for review** → **Publish** → Archive. Agents see published content only. Policies need administrator approval. When a supervisor edits a published policy, it goes back to *Under Review*.
- **Edits:** every save needs a short change summary and creates a version. **History** shows a line-by-line comparison with the previous version, and **Restore** brings an old version back as a new one.
- **Conflicts:** if two people edit the same article, the second save is rejected with a "newer version" warning instead of silently overwriting.
- **Feature dependencies:** tick the features an article depends on. While one of them is not *Live and verified*, the article shows a warning banner.
- **Policy pending:** if you write a *Policy Pending Approval* section, the article is flagged automatically. When a policy is approved, update the policy document, then remove the pending sections from the affected articles. The tracker lists them.
- **AI visibility:** untick *Available to AI assistant* for anything the future bot must not use. Internal notes are always excluded.
- **Review queue:** articles waiting for approval.
- **Feedback:** "outdated" reports and edit suggestions from agents. Click **Edit article**, then mark the item **Done**.
- **Categories:** add, rename or reorder categories and subcategories (administrator only). Only empty categories can be deleted.
- **Knowledge gaps:** searches that returned nothing. Write an article, add tags to an existing one, or add a synonym (Settings → Search synonyms).
- **Templates:** use `{{placeholders}}` from the list on the right of the editor. Unknown placeholders are flagged.

## Supervising tickets

- **Assigning:** the dashboard's *Urgent issues* and the tickets list's *Unassigned* and *Overdue* views show what needs an owner. Assign from the ticket's Details panel.
- **Escalation Center:** filter by level and department. Use **Update** to record progress or reassign, and **Decide** to record the final decision, which moves the ticket back to *In Progress*. Escalations past their expected follow-up time are flagged in red.
- **Reports:** choose a period (today, this week, this month, 30 days or custom). You can exclude demo tickets and export CSV. All numbers come from real ticket events.

## Announcements

Use announcements for new payment methods, policy changes, feature launches, known technical issues, service interruptions and new instructions.

- **Critical:** unread critical announcements appear as a red banner on everyone's dashboard.
- **Read status:** you can see how many employees have read each announcement.
- **Big edits:** use "mark unread for everyone" when an announcement changes significantly.

## Training

- **Team progress:** Training Center → *Team progress* shows each employee's module scores.
- **Editing:** administrators can edit any module, including its quiz questions and correct answers. Click **Edit module**.
- **Pass mark:** 80% by default.

## Integrations (the future AI assistant)

Settings → Integrations → create an API key with scope `kb:read`. Add `tickets:create` only if the bot should open tickets when it hands off to a human. The key is shown once; store it in the bot's secret settings. The endpoints are listed on that page and in `docs/ARCHITECTURE.md`. Revoke a key immediately if it is exposed.

## Audit log

Settings → Audit log records:

- every login and failed login
- every ticket action
- every content and settings change
- file uploads and views
- backups, API key changes and demo-data deletion

You can filter by action, employee and date.
