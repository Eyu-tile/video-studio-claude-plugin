# Patch a review page (review_*/index.html, shared template) so that:
# 1) seeking works: each cut's mp4 is fetched whole into a blob URL (the file host does not serve byte ranges, so the
#    browser snapped back to 0 on a seek into an unbuffered part);
# 2) client comments reach the owner: anyone who cannot write the page's own store (every outside-org invitee, Viewers,
#    Commenters) comments through claude.ai's comment composer, anchored to the cut + timecode stamp; no silent
#    browser-only fallback any more.
# usage: python3 -I review_fix.py PAGE.html
import sys, re
p = sys.argv[1]; s = open(p).read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:60], s.count(a)); s = s.replace(a, b)
# --- markup: loading note on the video, comment box always present, clearer hint
rep('<video id="vid" playsinline preload="auto"></video>',
    '<video id="vid" playsinline preload="auto"></video>\n        <div id="loadMsg" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:rgba(0,0,0,.72);color:#fff;padding:10px 16px;border-radius:10px;font:600 14px/1.3 system-ui,sans-serif;pointer-events:none" hidden>Loading video…</div>')
rep('<p class="cc-hint" id="ccHint">Pause where you want, then comment. Your note is saved in this page\'s Comments, where the owner sees it.</p>',
    '<p class="cc-hint" id="ccHint">Pause on the frame, then press the button: your comment is posted in this page\'s Comments with this cut and timecode, and the owner gets it. You need to be signed in to Claude with comment access.</p>')
# --- video loading through a blob so every timecode is seekable
rep('''    vid.pause();
    vid.src = "v/" + c.src + ".mp4"; vid.poster = "v/" + c.src + ".jpg";
    vid.playbackRate = parseFloat($("rate").value);''',
    '''    vid.pause(); vid.poster = "v/" + c.src + ".jpg"; loadVideo(c);''')
rep('/* ---------- player ---------- */', '''/* ---------- video loading: whole file into a blob URL so any timecode can be reached ---------- */
const blobs = {}; let loadSeq = 0, pendingT = null;
async function loadVideo(c){
  const my = ++loadSeq, msg = $("loadMsg");
  if (blobs[c.id]) { vid.src = blobs[c.id]; vid.playbackRate = parseFloat($("rate").value); msg.hidden = true; return; }
  msg.hidden = false; msg.textContent = "Loading video…";
  try {
    const r = await fetch("v/" + c.src + ".mp4"); if (!r.ok || !r.body) throw new Error("http " + r.status);
    const total = +r.headers.get("content-length") || 0, rd = r.body.getReader(), parts = []; let got = 0;
    for (;;) { const {done, value} = await rd.read(); if (done) break; parts.push(value); got += value.length;
      if (my === loadSeq && total) msg.textContent = "Loading video " + Math.round(got / total * 100) + "%"; }
    blobs[c.id] = URL.createObjectURL(new Blob(parts, {type: "video/mp4"}));
    if (my !== loadSeq) return;
    vid.src = blobs[c.id];
  } catch (e) { if (my !== loadSeq) return; vid.src = "v/" + c.src + ".mp4"; }
  vid.playbackRate = parseFloat($("rate").value); msg.hidden = true;
}
vid.addEventListener("loadedmetadata", () => { if (pendingT != null) { const t = pendingT; pendingT = null; seek(t); } });

/* ---------- player ---------- */''')
rep('function seek(t){ vid.currentTime = Math.max(0, Math.min(dur() - 0.001, t)); tick(); }',
    'function seek(t){ if (vid.readyState < 1) { pendingT = t; return; } vid.currentTime = Math.max(0, Math.min(dur() - 0.001, t)); tick(); }')
# --- storage: no silent browser-only comments
lk = re.search(r'const LKEY = "[^"]+";\n', s).group(0)
rep(lk, '')
rep('function loadLocal(){ try { comments = JSON.parse(localStorage.getItem(LKEY) || "[]"); } catch (e) { comments = []; } }\n', 'function loadLocal(){ comments = []; mode = "none"; }\n')
rep('function saveLocal(){ try { localStorage.setItem(LKEY, JSON.stringify(comments)); } catch (e) {} }\n', 'function useClaudeComments(){ $("composer").hidden = true; $("ccBox").hidden = false; ccSync(); }\n')
rep('''    catch (e) { if (cmNs) { $("composer").hidden = true; toast("Use \\u201cComment on this frame\\u201d to comment."); } else toast(e && e.code === "invalid_argument" ? "You can view this page but not comment on it." : "The comment didn't save. Try again."); return false; }
  } else { c.id = "l" + Date.now(); comments.push(c); saveLocal(); renderAll(); }''',
    '''    catch (e) { if (e && e.code === "invalid_argument") { useClaudeComments(); toast("Use \\u201cComment on this frame\\u201d: your note goes to the page's Comments."); } else toast("The comment didn't save. Try again."); return false; }
  } else { useClaudeComments(); toast("Use \\u201cComment on this frame\\u201d to post your note."); return false; }''')
rep('else { const c = comments.find(x => x.id === id); if (c) Object.assign(c, p); saveLocal(); renderAll(); }', '')
rep('else { comments = comments.filter(x => x.id !== id); saveLocal(); renderAll(); }', '')
s = s.replace('note.textContent = "Saved in this browser only. Open the page inside Claude to share comments.";', 'note.textContent = "Comment with \\u201cComment on this frame\\u201d";')
rep('''      if (!canWrite) { $("noteText").disabled = true; $("noteText").placeholder = "You have view access, so you can't comment here."; }''',
    '''      if (!canWrite && !isOwner) useClaudeComments();''')
# --- claude.ai comments: shown to everyone but the owner; anchored to the cut + timecode stamp
rep('''  if (!cmNs) return;
  const el = $("ccStamp"), r = document.createRange(); r.selectNodeContents(el);
  try { await cmNs.openComposer({range: r}); }''',
    '''  if (!cmNs) { $("ccHint").textContent = "Click Comment in Claude's top bar, then click the timecode above and write your note. It reaches the owner with this cut and timecode."; return; }
  const el = $("ccStamp"), r = document.createRange(); r.selectNodeContents(el);
  try { await cmNs.openComposer({range: r}); toast("Write your note in the comment box: it is pinned to " + tc(vid.currentTime || 0, true)); }''')
rep('''  try { cmNs = await window.claude.use("comments"); } catch (e) { cmNs = null; }
  if (!cmNs) return;
  $("ccBox").hidden = false; ccSync();
  // people who can't write the page's own comment store use claude.ai comments only
  const ownStore = !!dbNs && (isOwner || canWrite);
  if (!ownStore) { $("composer").hidden = true; $("storeNote").textContent = "Comment with \\u201cComment on this frame\\u201d"; }''',
    '''  try { cmNs = await window.claude.use("comments"); } catch (e) { cmNs = null; }
  // the owner uses the page's own list; everyone else posts claude.ai comments (they always reach the owner)
  if (!isOwner) { useClaudeComments(); $("storeNote").textContent = "Comment with \\u201cComment on this frame\\u201d"; }
  else if (cmNs) { $("ccBox").hidden = false; ccSync(); }''')
rep('''  if (!(window.claude && window.claude.use)) return;
  try { cmNs''', '''  if (!(window.claude && window.claude.use)) { useClaudeComments(); return; }
  try { cmNs''')
open(p, "w").write(s); print("patched", p)
