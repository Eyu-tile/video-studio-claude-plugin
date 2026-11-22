# review_fix5.py PAGE.html [...]  (run after review_fix4.py)
# - each claude.use() call is caught on its own: one capability failing for an outside viewer no longer drops the others
# - an access check line (what the platform reported for this viewer) is shown with device-only notes and included in
#   Copy my notes / Email my notes, so a failed route can be diagnosed from what the client sends
import sys

def fix(p):
    s = open(p, encoding="utf-8").read()
    if "review_fix5" in s:
        return "already fixed"
    if "review_fix4" not in s:
        return "SKIPPED: run review_fix4.py first"
    a = s.index("async function connect(){")
    b = s.index('$("refresh").addEventListener', a)
    old = s[a:b]
    tail = old[old.index("  if (db) {"):]          # keep the routing that follows unchanged
    new = '''let diag = {}, lastErr = null;
function diagText(){ return "Access check: " + Object.entries(diag).map(([k, v]) => k + "=" + v).join(" · ") + (lastErr ? " · error=" + lastErr : ""); }
async function connect(){
  const note = $("storeNote");
  mode = "none";   // the page starts in "local"; shared comments must be able to take over (the old pages never left "local")
  diag.claude = !!(window.claude && window.claude.use);
  if (!diag.claude) { useDrafts(""); return; }
  const safe = n => Promise.resolve().then(() => window.claude.use(n)).catch(e => { diag[n + "Err"] = (e && e.code) || "error"; return null; });
  const [db, u, cm] = await Promise.all([safe("db"), safe("user"), safe("comments")]);
  cmNs = cm; userNs = u;
  let w = null;
  if (u) {
    try { const me = await u.me(); myId = me && me.id; } catch (e) {}
    try { isOwner = !!(await u.isOwner()); } catch (e) {}
    try { w = await u.can("data.write"); } catch (e) {}
    try { diag.editor = await u.canEdit(); } catch (e) {}
  }
  Object.assign(diag, {db: !!db, user: !!u, comments: !!cm, owner: isOwner, write: w});
''' + tail
    s = s[:a] + new + s[b:]
    # remember error codes
    o = 'note.textContent = "Comments couldn\'t connect. Press Refresh to try again.";'
    assert s.count(o) == 1, "subscribe error"
    s = s.replace(o, 'lastErr = (err && err.code) || "connect"; ' + o)
    o = '    catch (e) {\n      if (e && (e.code === "invalid_argument"'
    assert s.count(o) == 1, "add error"
    s = s.replace(o, '    catch (e) {\n      lastErr = (e && e.code) || "write";\n      if (e && (e.code === "invalid_argument"')
    # show the check with device-only notes
    o = '"Your notes are NOT sent yet: they are kept on this device only. When you\'re done, press Email my notes (or Copy my notes and send them to the editor). " + SHELL_TIP;'
    assert s.count(o) == 1, "sendWhy"
    s = s.replace(o, o[:-1] + ' + " (" + diagText() + ")";')
    # include it in what the client sends
    o = 'const txt = lines.join("\\n").trim() || "No comments yet.";'
    assert s.count(o) == 1, "copy text"
    s = s.replace(o, 'const txt = (lines.join("\\n").trim() || "No comments yet.") + (mode === "local" ? "\\n\\n" + diagText() : "");')
    o = '  return lines.join("\\n").trim();\n}'
    assert s.count(o) == 1, "email text"
    s = s.replace(o, '  return lines.join("\\n").trim() + (mode === "local" ? "\\n\\n" + diagText() : "");\n}')
    s = s.replace("/* review_fix4 */", "/* review_fix4 */ /* review_fix5 */", 1)
    assert "review_fix5" in s
    open(p, "w", encoding="utf-8").write(s)
    return "fixed"

for p in sys.argv[1:]:
    try: print(p, fix(p))
    except (ValueError, AssertionError) as e: print(p, "SKIPPED:", e)
