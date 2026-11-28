# review_fix4.py PAGE.html [PAGE.html ...]
# Review-page comment routing fix (2026-11-21):
#  - a viewer who can write the page's shared comments (owner, outside Editor, org members) posts there; never forced to drafts
#  - a viewer who can only read (outside Viewer/Commenter) posts with "Comment on this frame" when Claude offers it,
#    and is always told about Claude's own Comment button
#  - signed-out viewers keep notes on the device, told plainly they are NOT sent, warned before leaving, Email/Copy to send
#  - Refresh button: re-reads the shared comments (owner sees new ones at once; the list is also live)
#  - NOTES_TO constant: the Email my notes address (empty until the user names one)
import sys, re

STORAGE = r'''/* ---------- storage: shared comments when this viewer can write, Claude's comments otherwise, this device last ---------- */
let cmNs = null, unsub = null, unsent = false;
const NOTES_TO = "";   // inbox for "Email my notes" (empty: the viewer types it)
function loadLocal(){ if (mode === "local") return; comments = []; mode = "none"; }
function useClaudeComments(){ $("composer").hidden = true; $("sendBox").hidden = true; $("ccBox").hidden = false; $("ccBtn").hidden = false; $("storeNote").textContent = "Comment with \u201cComment on this frame\u201d"; ccSync(); }
const DKEY = "review-notes-" + MASTER;
function loadDrafts(){ try { return JSON.parse(localStorage.getItem(DKEY) || "[]"); } catch (e) { return []; } }
function saveDrafts(){ try { localStorage.setItem(DKEY, JSON.stringify(comments)); } catch (e) {} }
const SHELL_TIP = "Signed in to Claude? You can also use Claude's own Comment button at the top of this page: click it, click the video and type your note with the timecode, and it reaches the editor directly.";
function draftsNote(){ $("storeNote").textContent = comments.length ? "Notes NOT sent yet: press Email my notes" : "Notes stay on this device until you send them"; }
function useDrafts(why){
  mode = "local"; comments = loadDrafts(); canWrite = true; unsent = comments.length > 0;
  $("ccBox").hidden = true; $("composer").hidden = false; $("sendBox").hidden = false;
  $("noteText").disabled = false; $("noteText").placeholder = "Write your note for this frame…";
  $("sendWhy").textContent = (why ? why + " " : "") + "Your notes are NOT sent yet: they are kept on this device only. When you're done, press Email my notes (or Copy my notes and send them to the editor). " + SHELL_TIP;
  draftsNote(); renderAll();
}
window.addEventListener("beforeunload", e => { if (mode === "local" && unsent) { e.preventDefault(); e.returnValue = ""; } });
function cannotWrite(){
  canWrite = false;
  if (cmNs) { useClaudeComments(); return "claude"; }
  useDrafts("Your access lets you view this page but not post to its comment list."); return "local";
}
async function add(c){
  if (mode === "db") {
    try { await dbNs.collection("comments").doc().set(c); return true; }
    catch (e) {
      if (e && (e.code === "invalid_argument" || e.code === "not_granted" || e.code === "permission_denied")) {
        if (cannotWrite() === "claude") { toast("Use “Comment on this frame”: your note goes to the page's Comments."); return false; }
        c.id = "n" + Date.now(); comments.push(c); saveDrafts(); unsent = true; draftsNote(); renderAll(); return true;
      }
      toast("The comment didn't save. Try again."); return false; }
  }
  c.id = "n" + Date.now(); comments.push(c); saveDrafts(); unsent = true; draftsNote(); renderAll(); return true;
}
async function patch(id, p){
  if (mode === "db") { try { await dbNs.doc("comments/" + id).update(p); } catch (e) { toast("That change didn't save."); } }
  else { const c = comments.find(x => x.id === id); if (c) Object.assign(c, p); saveDrafts(); renderAll(); }
}
async function remove(id){
  if (mode === "db") { try { await dbNs.doc("comments/" + id).delete(); } catch (e) { toast("Couldn't delete that comment."); } }
  else { comments = comments.filter(x => x.id !== id); saveDrafts(); unsent = comments.length > 0; draftsNote(); renderAll(); }
}
function stamp(){ return new Date().toLocaleTimeString([], {hour: "2-digit", minute: "2-digit"}); }
function subscribe(){
  const note = $("storeNote");
  if (unsub) { try { unsub(); } catch (e) {} unsub = null; }
  return new Promise(resolve => {
    let first = true;
    const t = setTimeout(() => { if (first) { first = false; resolve(false); } }, 10000);
    try {
      unsub = dbNs.collection("comments").onSnapshot(snap => {
        if (mode === "local") return;
        mode = "db";
        comments = snap.docs.map(d => Object.assign({id: d.id}, d.data()));
        if (canWrite || isOwner) note.textContent = "Comments are shared and live · updated " + stamp();
        renderAll();
        if (first) { first = false; clearTimeout(t); resolve(true); }
      }, err => {
        note.textContent = "Comments couldn't connect. Press Refresh to try again.";
        if (first) { first = false; clearTimeout(t); resolve(false); }
      });
    } catch (e) { if (first) { first = false; clearTimeout(t); resolve(false); } }
  });
}
async function connect(){
  const note = $("storeNote");
  mode = "none";   // the page starts in "local"; shared comments must be able to take over (the old pages never left "local")
  if (!(window.claude && window.claude.use)) { useDrafts(""); return; }
  let db = null, u = null;
  try { [db, u, cmNs] = await Promise.all([window.claude.use("db"), window.claude.use("user"), window.claude.use("comments")]); } catch (e) {}
  userNs = u;
  let w = null;
  if (u) {
    try { const me = await u.me(); myId = me && me.id; } catch (e) {}
    try { isOwner = !!(await u.isOwner()); } catch (e) {}
    try { w = await u.can("data.write"); } catch (e) {}
  }
  if (db) {
    dbNs = db; canWrite = isOwner || w !== false;
    const ok = await subscribe();
    if (isOwner) {
      $("composer").hidden = false; $("sendBox").hidden = true; $("ccBox").hidden = false; $("ccBtn").hidden = !cmNs;
      $("ccHint").textContent = "Clients who can't post here use Claude's Comment button: those comments are in Claude's comment panel (the speech-bubble icon at the top), not in this list. Press Refresh to reload this list.";
      ccSync(); return;
    }
    if (!ok) { if (cmNs) useClaudeComments(); else useDrafts("Comments couldn't connect."); return; }
    if (!canWrite) { if (cmNs) useClaudeComments(); else useDrafts("Your access lets you view this page but not post to its comment list."); return; }
    $("composer").hidden = false; $("sendBox").hidden = true; $("ccBox").hidden = true; return;
  }
  if (cmNs) { useClaudeComments(); note.textContent = "Comment with “Comment on this frame”"; return; }
  useDrafts(u ? "" : "You're not signed in to Claude, so your notes can't be shared from here.");
}
$("refresh").addEventListener("click", async () => {
  if (mode === "local") { comments = loadDrafts(); renderAll(); toast("Notes on this device reloaded"); return; }
  if (!dbNs) { location.reload(); return; }
  const ok = await subscribe(); toast(ok ? "Comments refreshed · " + stamp() : "Couldn't reach the comments. Try again.");
});

'''

THREADS = r'''/* ---------- claude.ai comment threads: how viewers who can't post here comment ---------- */
function ccText(){ return `${cur.hook} · ${cur.ar} ${cur.ver} · ${tc(vid.currentTime || 0)}`; }
function ccSync(){ const el = $("ccStamp"); if (el && !$("ccBox").hidden) el.textContent = ccText(); }
vid.addEventListener("timeupdate", ccSync); vid.addEventListener("seeked", ccSync);
$("ccBtn").addEventListener("click", async () => {
  vid.pause(); ccSync();
  if (!cmNs) { useDrafts("Commenting through Claude isn't available on your link."); return; }
  const el = $("ccStamp"), r = document.createRange(); r.selectNodeContents(el);
  try {
    const res = await cmNs.openComposer({range: r});
    if (res && res.opened === false) { toast("Click once on the page, then press the button again."); return; }
    toast("Type your note in the comment box and post it: it is pinned to " + tc(vid.currentTime || 0, true));
  } catch (e) {
    if (e && e.code === "rate_limited") { toast("Wait a moment, then try again."); return; }
    useDrafts("Your link lets you view but not comment in Claude.");
  }
});
connect();
setInterval(renderNotes, 60000);
'''

OLD_CC = 'function useClaudeComments(){ $("composer").hidden = true; $("sendBox").hidden = true; $("ccBox").hidden = false; $("ccBtn").hidden = false; ccSync(); }'
NEW_CC = 'function useClaudeComments(){ $("composer").hidden = true; $("sendBox").hidden = true; $("ccBox").hidden = false; $("ccBtn").hidden = false; $("storeNote").textContent = "Comment with \\u201cComment on this frame\\u201d"; ccSync(); }'

def fix(p):
    s = open(p, encoding="utf-8").read()
    if "review_fix4" in s:
        if OLD_CC in s:
            open(p, "w", encoding="utf-8").write(s.replace(OLD_CC, NEW_CC)); return "updated (status line for commenters)"
        return "already fixed"
    a = s.index("/* ---------- storage: shared db when available, this browser otherwise ---------- */")
    b = s.index("/* ---------- composer ---------- */")
    s = s[:a] + STORAGE + s[b:]
    a = s.index("/* ---------- claude.ai comment threads: how shared viewers comment ---------- */")
    b = s.index("setInterval(renderNotes, 60000);", a) + len("setInterval(renderNotes, 60000);\n")
    s = s[:a] + THREADS + s[b:]
    old = '<button class="btn" id="copyAll" type="button">Copy all notes</button>'
    assert s.count(old) == 1, "copyAll button"
    s = s.replace(old, '<button class="btn" id="refresh" type="button" title="Reload the comments">Refresh</button>\n      ' + old)
    old = 'a.href = "mailto:?subject="'
    assert s.count(old) == 1, "mailto"
    s = s.replace(old, 'unsent = false; a.href = "mailto:" + encodeURIComponent(NOTES_TO) + "?subject="')
    old = '$("sendCopy").addEventListener("click", () => $("copyAll").click());'
    assert s.count(old) == 1, "sendCopy"
    s = s.replace(old, '$("sendCopy").addEventListener("click", () => { unsent = false; $("copyAll").click(); });')
    s = s.replace("</script>", "/* review_fix4 */\n</script>", 1) if s.count("</script>") == 1 else s.replace("})();\n</script>", "})();\n/* review_fix4 */\n</script>")
    assert "review_fix4" in s
    open(p, "w", encoding="utf-8").write(s)
    return "fixed"

for p in sys.argv[1:]:
    try: print(p, fix(p))
    except (ValueError, AssertionError) as e: print(p, "SKIPPED:", e)
