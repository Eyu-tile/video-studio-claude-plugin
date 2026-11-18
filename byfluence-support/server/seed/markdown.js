import { marked } from 'marked';

marked.setOptions({ gfm: true, breaks: false });

const CALLOUT = { NOTE: 'note', TIP: 'tip', WARNING: 'warning', POLICY: 'policy', IMPORTANT: 'warning', CAUTION: 'warning' };

/** Markdown → HTML compatible with the TipTap editor (callouts + task lists). */
export function md(text) {
  if (!text || !text.trim()) return '';
  let html = marked.parse(text);
  // Callouts: <blockquote><p>[!WARNING] ...</p>...</blockquote>
  html = html.replace(/<blockquote>\s*<p>\[!(NOTE|TIP|WARNING|POLICY|IMPORTANT|CAUTION)\]\s*([\s\S]*?)<\/blockquote>/g,
    (_m, kind, rest) => `<div class="callout callout-${CALLOUT[kind]}" data-callout="${CALLOUT[kind]}"><p>${rest.trim()}</div>`);
  // Task lists
  html = html.replace(/<li><input (checked="" )?disabled="" type="checkbox">\s*([\s\S]*?)<\/li>/g,
    (_m, checked, body) => `<li data-type="taskItem" data-checked="${checked ? 'true' : 'false'}"><p>${body.trim()}</p></li>`);
  html = html.replace(/<ul>\s*(<li data-type="taskItem")/g, '<ul data-type="taskList">$1');
  return html.trim();
}

/** Markdown bullet list → array of strings */
export function mdList(text) {
  return (text || '').split('\n').map((l) => l.trim()).filter((l) => /^([-*]|\d+\.)\s+/.test(l)).map((l) => l.replace(/^([-*]|\d+\.)\s+/, '').replace(/\*\*/g, ''));
}

/** Markdown → plain text (for summaries & templates) */
export function plain(text) {
  return (text || '').replace(/\*\*(.+?)\*\*/g, '$1').replace(/(^|\s)\*(.+?)\*/g, '$1$2').replace(/`([^`]+)`/g, '$1').trim();
}
