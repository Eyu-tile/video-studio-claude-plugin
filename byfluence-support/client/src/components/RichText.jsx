import { useMemo } from 'react';
import { cx } from './ui.jsx';

/** Render sanitized (server-side) HTML. Highlights {{placeholders}}; task lists can be ticked locally. */
export default function RichText({ html, className, interactive = false, highlight = true }) {
  const out = useMemo(() => {
    let h = html || '';
    if (highlight) h = h.replace(/{{\s*([a-z_]+)\s*}}/g, '<span class="ph">{{$1}}</span>');
    return h;
  }, [html, highlight]);
  return (
    <div
      className={cx('prose-byf', interactive && 'interactive', className)}
      onClick={interactive ? (e) => {
        const li = e.target.closest('li[data-type="taskItem"]');
        if (li) li.setAttribute('data-checked', li.getAttribute('data-checked') === 'true' ? 'false' : 'true');
      } : undefined}
      // eslint-disable-next-line react/no-danger
      dangerouslySetInnerHTML={{ __html: out }}
    />
  );
}

/** Convert rendered HTML to clean plain text for copying (keeps paragraphs & list numbering). */
export function htmlToPlain(html) {
  const div = document.createElement('div');
  div.innerHTML = html || '';
  const lines = [];
  const walk = (node, listCtx) => {
    for (const el of node.childNodes) {
      if (el.nodeType === 3) { if (el.textContent.trim()) lines.push(el.textContent); continue; }
      const tag = el.tagName;
      if (tag === 'P' || /^H\d$/.test(tag) || tag === 'DIV' || tag === 'BLOCKQUOTE') {
        if (el.querySelector('p,ul,ol')) walk(el, listCtx);
        else lines.push(el.innerText ?? el.textContent);
        lines.push('');
      } else if (tag === 'UL' || tag === 'OL') {
        let i = 1;
        for (const li of el.children) {
          const prefix = tag === 'OL' ? `${i++}. ` : '• ';
          lines.push(prefix + (li.innerText ?? li.textContent).trim().replace(/\n+/g, ' '));
        }
        lines.push('');
      } else if (tag === 'BR') lines.push('');
      else if (tag === 'TABLE') { lines.push((el.innerText ?? el.textContent).trim()); lines.push(''); }
      else lines.push(el.innerText ?? el.textContent);
    }
  };
  walk(div);
  return lines.join('\n').replace(/\n{3,}/g, '\n\n').replace(/[ \t]+\n/g, '\n').trim();
}
