# Second pass on review pages (after review_fix.py): a viewer who cannot comment through claude.ai (view-only link, or no
# comments UI) gets the page's own note box; notes are kept on their device, clearly labelled as NOT sent, with
# "Email my notes" / "Copy my notes" buttons. The claude.ai button checks the composer actually opened.
# usage: python3 -I review_fix2.py PAGE.html
import sys, re
p = sys.argv[1]; s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a)); s = s.replace(a, b)
rep('''      <form class="composer" id="composer">''', '''      <div class="cc" id="sendBox" hidden>
        <p class="cc-hint" id="sendWhy" style="color:var(--ink-2)"></p>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="btn primary" id="sendMail" type="button">Email my notes</button>
          <button class="btn" id="sendCopy" type="button">Copy my notes</button>
        </div>
      </div>
      <form class="composer" id="composer">''')
rep('function useClaudeComments(){ $("composer").hidden = true; $("ccBox").hidden = false; ccSync(); }\n',
'''function useClaudeComments(){ $("composer").hidden = true; $("sendBox").hidden = true; $("ccBox").hidden = false; ccSync(); }
const DKEY = "review-notes-" + MASTER;
function loadDrafts(){ try { return JSON.parse(localStorage.getItem(DKEY) || "[]"); } catch (e) { return []; } }
function saveDrafts(){ try { localStorage.setItem(DKEY, JSON.stringify(comments)); } catch (e) {} }
function useDrafts(why){
  mode = "local"; comments = loadDrafts(); canWrite = true;
  $("ccBox").hidden = true; $("composer").hidden = false; $("sendBox").hidden = false;
  $("noteText").disabled = false; $("noteText").placeholder = "Write your note for this frame…";
  $("sendWhy").textContent = (why ? why + " " : "") + "Your notes are pinned to the timecode and kept on this device. When you're done, press Email my notes (or Copy my notes and paste them to the editor): they are not sent until you do.";
  $("storeNote").textContent = "Notes not sent yet: use Email my notes";
  renderAll();
}
''')
# local add / patch / delete for drafts
rep('''  } else { useClaudeComments(); toast("Use \\u201cComment on this frame\\u201d to post your note."); return false; }''',
    '''  } else { c.id = "n" + Date.now(); comments.push(c); saveDrafts(); renderAll(); toast("Note saved here. Send it with Email my notes."); return true; }''')
rep('''  if (mode === "db") { try { await dbNs.doc("comments/" + id).update(p); } catch (e) { toast("That change didn't save."); } }''',
    '''  if (mode === "db") { try { await dbNs.doc("comments/" + id).update(p); } catch (e) { toast("That change didn't save."); } }
  else { const c = comments.find(x => x.id === id); if (c) Object.assign(c, p); saveDrafts(); renderAll(); }''')
rep('''  if (mode === "db") { try { await dbNs.doc("comments/" + id).delete(); } catch (e) { toast("Couldn't delete that comment."); } }''',
    '''  if (mode === "db") { try { await dbNs.doc("comments/" + id).delete(); } catch (e) { toast("Couldn't delete that comment."); } }
  else { comments = comments.filter(x => x.id !== id); saveDrafts(); renderAll(); }''')
# claude.ai button: check the result; fall back to the page's own note box
a0 = s.index('$("ccBtn").addEventListener("click", async () => {'); a1 = s.index('async function connectComments(){')
s = s[:a0] + '''$("ccBtn").addEventListener("click", async () => {
  vid.pause(); ccSync();
  if (!cmNs) { useDrafts("Commenting through Claude isn't available on your link."); return; }
  const el = $("ccStamp"), r = document.createRange(); r.selectNodeContents(el);
  try {
    const res = await cmNs.openComposer({range: r});
    if (res && res.opened === false) { toast("Click once on the page, then press the button again."); return; }
    toast("Type your note in the comment box: it is pinned to " + tc(vid.currentTime || 0, true));
  } catch (e) {
    if (e && e.code === "rate_limited") { toast("Wait a moment, then try again."); return; }
    useDrafts("Your link lets you view but not comment in Claude.");
  }
});
''' + s[a1:]
rep('''  if (!(window.claude && window.claude.use)) { useClaudeComments(); return; }''', '''  if (!(window.claude && window.claude.use)) { useDrafts(""); return; }''')
rep('''  if (!isOwner) { useClaudeComments(); $("storeNote").textContent = "Comment with \\u201cComment on this frame\\u201d"; }''',
    '''  if (!isOwner && cmNs) { useClaudeComments(); $("storeNote").textContent = "Comment with \\u201cComment on this frame\\u201d"; }
  else if (!isOwner) useDrafts("Commenting through Claude isn't available on your link.");''')
# send buttons
rep('/* ---------- keys ---------- */', '''/* ---------- send my notes (viewers without comment access) ---------- */
function notesText(){
  const lines = [document.title, ""];
  for (const c of CUTS) {
    const cs = comments.filter(x => x.cut === c.id).sort((a, b) => (a.t ?? -1) - (b.t ?? -1));
    if (!cs.length) continue;
    lines.push(`${c.hook} ${c.ar} ${c.ver}  (${c.file})`);
    for (const x of cs) lines.push(`  ${x.t == null ? "general " : tc(x.t)}  ${x.text.replace(/\\n/g, " / ")}`);
    lines.push("");
  }
  return lines.join("\\n").trim();
}
$("sendCopy").addEventListener("click", () => $("copyAll").click());
$("sendMail").addEventListener("click", () => {
  if (!comments.length) { toast("Write a note first."); return; }
  const a = document.createElement("a");
  a.href = "mailto:?subject=" + encodeURIComponent("Notes: " + document.title) + "&body=" + encodeURIComponent(notesText().slice(0, 6000));
  a.target = "_blank"; a.rel = "noopener"; document.body.appendChild(a); a.click(); a.remove();
  toast("If no email window opened, use Copy my notes and paste them.");
});

/* ---------- keys ---------- */''')
open(p, "w").write(s); print("patched", p)
