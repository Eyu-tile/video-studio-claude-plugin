import { useEffect, useRef } from 'react';
import { useEditor, EditorContent, Node, mergeAttributes } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import { Table, TableRow, TableCell, TableHeader } from '@tiptap/extension-table';
import Image from '@tiptap/extension-image';
import { TaskList, TaskItem } from '@tiptap/extension-list';
import { Placeholder } from '@tiptap/extensions';
import {
  Bold, Italic, Underline, Strikethrough, Heading2, Heading3, List, ListOrdered, ListTodo, Quote, Link2, ImagePlus, Table as TableIcon,
  Code2, Minus, Undo2, Redo2, Info, AlertTriangle, Lightbulb, Scale, Rows3, Columns3, Trash2, Pilcrow,
} from 'lucide-react';
import { api } from '../lib/api.js';
import { cx, useToast } from './ui.jsx';

const Callout = Node.create({
  name: 'callout',
  group: 'block',
  content: 'block+',
  defining: true,
  addAttributes() {
    return { type: { default: 'note', parseHTML: (el) => el.getAttribute('data-callout') || (el.className.match(/callout-(\w+)/) || [])[1] || 'note' } };
  },
  parseHTML() { return [{ tag: 'div[data-callout]' }, { tag: 'div.callout' }]; },
  renderHTML({ node, HTMLAttributes }) {
    return ['div', mergeAttributes(HTMLAttributes, { 'data-callout': node.attrs.type, class: `callout callout-${node.attrs.type}` }), 0];
  },
  addCommands() {
    return {
      toggleCallout: (type) => ({ commands, editor }) => {
        if (editor.isActive('callout', { type })) return commands.lift('callout');
        if (editor.isActive('callout')) return commands.updateAttributes('callout', { type });
        return commands.wrapIn('callout', { type });
      },
    };
  },
});

function Tb({ icon: Icon, label, active, onClick, disabled }) {
  return (
    <button type="button" title={label} aria-label={label} disabled={disabled} onMouseDown={(e) => e.preventDefault()} onClick={onClick}
      className={cx('size-7 grid place-items-center rounded-md transition-colors disabled:opacity-30', active ? 'bg-brand-100 text-brand-700 dark:bg-brand-900/60 dark:text-brand-200' : 'text-muted hover:bg-[var(--surface-2)] hover:text-[var(--text)]')}>
      <Icon className="size-4" />
    </button>
  );
}
const Sep = () => <span className="w-px h-5 bg-[var(--border)] mx-0.5" />;

export default function Editor({ value, onChange, placeholder = 'Write here…', minHeight = 140, compact = false }) {
  const fileRef = useRef(null);
  const toast = useToast();
  const editor = useEditor({
    extensions: [
      StarterKit.configure({ heading: { levels: [2, 3, 4] }, link: { openOnClick: false, autolink: true, HTMLAttributes: { rel: 'noopener noreferrer', target: '_blank' } } }),
      Table.configure({ resizable: false }), TableRow, TableHeader, TableCell,
      Image.configure({ inline: false }),
      TaskList, TaskItem.configure({ nested: true }),
      Placeholder.configure({ placeholder }),
      Callout,
    ],
    content: value || '',
    onUpdate: ({ editor: e }) => onChange?.(e.isEmpty ? '' : e.getHTML()),
    editorProps: { attributes: { class: 'prose-byf tiptap px-3.5 py-3', style: `min-height:${minHeight}px` } },
  });

  // Sync external value changes (e.g. restoring a version)
  useEffect(() => {
    if (editor && value !== undefined && value !== editor.getHTML() && !editor.isFocused) editor.commands.setContent(value || '', { emitUpdate: false });
  }, [value, editor]);

  if (!editor) return <div className="rounded-lg border border-base surface" style={{ minHeight }} />;

  const setLink = () => {
    const prev = editor.getAttributes('link').href;
    // eslint-disable-next-line no-alert
    const url = window.prompt('Link URL (https://… or /kb/article-slug)', prev || 'https://');
    if (url === null) return;
    if (!url) editor.chain().focus().extendMarkRange('link').unsetLink().run();
    else if (/^(https?:\/\/|\/|mailto:|tel:)/.test(url)) editor.chain().focus().extendMarkRange('link').setLink({ href: url }).run();
    else toast.error('Links must start with https://, / , mailto: or tel:');
  };
  const uploadImage = async (file) => {
    const fd = new FormData();
    fd.append('files', file);
    try {
      const [img] = await api('/docs/images', { method: 'POST', form: fd });
      editor.chain().focus().setImage({ src: img.url, alt: file.name }).run();
    } catch (e) { toast.error(e); }
  };
  const inTable = editor.isActive('table');
  const c = () => editor.chain().focus();

  return (
    <div className="rounded-lg border border-base surface focus-within:border-brand-400 focus-within:ring-2 focus-within:ring-brand-500/20 transition">
      <div className="flex flex-wrap items-center gap-0.5 px-1.5 py-1 border-b border-base surface-2 rounded-t-lg sticky top-14 z-10">
        {!compact && <><Tb icon={Pilcrow} label="Paragraph" active={editor.isActive('paragraph')} onClick={() => c().setParagraph().run()} />
          <Tb icon={Heading2} label="Heading" active={editor.isActive('heading', { level: 2 })} onClick={() => c().toggleHeading({ level: 2 }).run()} />
          <Tb icon={Heading3} label="Subheading" active={editor.isActive('heading', { level: 3 })} onClick={() => c().toggleHeading({ level: 3 }).run()} /><Sep /></>}
        <Tb icon={Bold} label="Bold (Ctrl+B)" active={editor.isActive('bold')} onClick={() => c().toggleBold().run()} />
        <Tb icon={Italic} label="Italic (Ctrl+I)" active={editor.isActive('italic')} onClick={() => c().toggleItalic().run()} />
        <Tb icon={Underline} label="Underline" active={editor.isActive('underline')} onClick={() => c().toggleUnderline().run()} />
        <Tb icon={Strikethrough} label="Strikethrough" active={editor.isActive('strike')} onClick={() => c().toggleStrike().run()} />
        <Sep />
        <Tb icon={List} label="Bullet list" active={editor.isActive('bulletList')} onClick={() => c().toggleBulletList().run()} />
        <Tb icon={ListOrdered} label="Numbered list" active={editor.isActive('orderedList')} onClick={() => c().toggleOrderedList().run()} />
        <Tb icon={ListTodo} label="Checklist" active={editor.isActive('taskList')} onClick={() => c().toggleTaskList().run()} />
        <Sep />
        <Tb icon={Info} label="Info callout" active={editor.isActive('callout', { type: 'note' })} onClick={() => c().toggleCallout('note').run()} />
        <Tb icon={Lightbulb} label="Tip callout" active={editor.isActive('callout', { type: 'tip' })} onClick={() => c().toggleCallout('tip').run()} />
        <Tb icon={AlertTriangle} label="Warning callout" active={editor.isActive('callout', { type: 'warning' })} onClick={() => c().toggleCallout('warning').run()} />
        <Tb icon={Scale} label="Policy pending callout" active={editor.isActive('callout', { type: 'policy' })} onClick={() => c().toggleCallout('policy').run()} />
        {!compact && <Tb icon={Quote} label="Quote" active={editor.isActive('blockquote')} onClick={() => c().toggleBlockquote().run()} />}
        <Sep />
        <Tb icon={Link2} label="Link" active={editor.isActive('link')} onClick={setLink} />
        {!compact && <>
          <Tb icon={ImagePlus} label="Upload image" onClick={() => fileRef.current?.click()} />
          <Tb icon={TableIcon} label="Insert table" onClick={() => c().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()} />
          {inTable && <>
            <Tb icon={Rows3} label="Add row" onClick={() => c().addRowAfter().run()} />
            <Tb icon={Columns3} label="Add column" onClick={() => c().addColumnAfter().run()} />
            <Tb icon={Trash2} label="Delete table" onClick={() => c().deleteTable().run()} />
          </>}
          <Tb icon={Code2} label="Code block" active={editor.isActive('codeBlock')} onClick={() => c().toggleCodeBlock().run()} />
          <Tb icon={Minus} label="Divider" onClick={() => c().setHorizontalRule().run()} />
        </>}
        <span className="flex-1" />
        <Tb icon={Undo2} label="Undo" disabled={!editor.can().undo()} onClick={() => c().undo().run()} />
        <Tb icon={Redo2} label="Redo" disabled={!editor.can().redo()} onClick={() => c().redo().run()} />
        <input ref={fileRef} type="file" accept="image/png,image/jpeg,image/webp,image/gif" className="hidden" onChange={(e) => { if (e.target.files?.[0]) uploadImage(e.target.files[0]); e.target.value = ''; }} />
      </div>
      <EditorContent editor={editor} />
    </div>
  );
}
