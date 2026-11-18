// Role-based permissions. One source of truth used by the API and sent to the client
// (the client only uses it to hide controls; the server always enforces).

export const ROLES = {
  admin: 'Administrator',
  supervisor: 'Support Supervisor',
  agent: 'Support Agent',
};

const AGENT = [
  'docs.read',               // published documentation
  'templates.use',
  'tickets.create',
  'tickets.view_own',        // assigned to me, created by me, or unassigned queue
  'tickets.update_own',
  'tickets.note',
  'tickets.communicate',
  'tickets.escalate',
  'tickets.resolve_own',
  'followups.manage_own',
  'announcements.read',
  'training.take',
  'docs.feedback',
  'search.use',
];

const SUPERVISOR = [
  ...AGENT,
  'docs.read_unpublished',
  'docs.edit',               // create/edit drafts, send to review
  'docs.publish',            // publish non-policy content (FAQ, templates, articles, SOPs, guides)
  'templates.edit',
  'tickets.view_all',
  'tickets.update_all',
  'tickets.assign',
  'tickets.reopen',
  'escalations.manage',
  'announcements.manage',
  'reports.view',
  'training.view_team',
  'feedback.manage',
  'features.view',
];

const ADMIN = [
  ...SUPERVISOR,
  'policies.publish',        // publish/approve policy documents
  'categories.manage',
  'docs.delete',
  'users.manage',
  'settings.manage',
  'audit.view',
  'backup.download',
  'apikeys.manage',
  'training.edit',
  'tickets.delete_demo',
];

export const PERMISSIONS = {
  agent: new Set(AGENT),
  supervisor: new Set(SUPERVISOR),
  admin: new Set(ADMIN),
};

export function can(user, perm) {
  return !!user && PERMISSIONS[user.role]?.has(perm);
}

export function permissionsFor(role) {
  return [...(PERMISSIONS[role] || [])];
}

/** May this user see this ticket? */
export function canViewTicket(user, t) {
  if (can(user, 'tickets.view_all')) return true;
  return t.assignee_id === user.id || t.created_by === user.id || t.assignee_id == null;
}

/** May this user change this ticket? */
export function canUpdateTicket(user, t) {
  if (can(user, 'tickets.update_all')) return true;
  return t.assignee_id === user.id || (t.assignee_id == null && can(user, 'tickets.update_own'));
}

/** May this user publish (or approve) a document of this type? */
export function canPublishDoc(user, type) {
  if (type === 'policy') return can(user, 'policies.publish');
  return can(user, 'docs.publish');
}
