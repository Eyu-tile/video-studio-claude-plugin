# Third pass: once a viewer is on the page's own note box (drafts), the shared-store listener and the 10 s timer never
# take it back; a refused shared-store write moves the note into drafts instead of dropping it.
import sys
p = sys.argv[1]; s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a)); s = s.replace(a, b)
rep('function loadLocal(){ comments = []; mode = "none"; }', 'function loadLocal(){ if (mode === "local") return; comments = []; mode = "none"; }')
rep('''    db.collection("comments").onSnapshot(snap => {
      if (!settled) { settled = true; clearTimeout(timer); }''', '''    db.collection("comments").onSnapshot(snap => {
      if (!settled) { settled = true; clearTimeout(timer); }
      if (mode === "local") return;   // this viewer writes notes on the page's own note box''')
rep('''    catch (e) { if (e && e.code === "invalid_argument") { useClaudeComments(); toast("Use \\u201cComment on this frame\\u201d: your note goes to the page's Comments."); } else toast("The comment didn't save. Try again."); return false; }''',
    '''    catch (e) {
      if (e && e.code === "invalid_argument") {
        if (cmNs) { useClaudeComments(); toast("Use \\u201cComment on this frame\\u201d: your note goes to the page's Comments."); return false; }
        useDrafts("Your link lets you view but not comment in Claude."); c.id = "n" + Date.now(); comments.push(c); saveDrafts(); renderAll(); return true;
      }
      toast("The comment didn't save. Try again."); return false; }''')
open(p, "w").write(s); print("patched", p)
