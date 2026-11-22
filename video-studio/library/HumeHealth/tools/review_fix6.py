# review_fix6.py PAGE.html [...]  (after review_fix5.py): when Claude doesn't recognise the viewer as invited
# (user capability absent) say so plainly: sign in with the invited email and open the invitation link.
import sys
NOTINV = ("Claude doesn’t recognise you as invited to this page: you may be signed in with a different email than the "
          "invitation, or you opened the plain link. Sign in to Claude with the invited email and open the link in the "
          "invitation email, then reload.")
def fix(p):
    s = open(p, encoding="utf-8").read()
    if "review_fix6" in s: return "already fixed"
    if "review_fix5" not in s: return "SKIPPED: run review_fix5.py first"
    o = 'useDrafts("Your access lets you view this page but not post to its comment list."); return "local";'
    assert s.count(o) == 1, "cannotWrite"
    s = s.replace(o, 'useDrafts(userNs ? "Your access lets you view this page but not post to its comment list." : NOT_INVITED); return "local";')
    o = 'if (!canWrite) { if (cmNs) useClaudeComments(); else useDrafts("Your access lets you view this page but not post to its comment list."); return; }'
    assert s.count(o) == 1, "connect branch"
    s = s.replace(o, 'if (!canWrite) { if (cmNs) useClaudeComments(); else useDrafts(u ? "Your access lets you view this page but not post to its comment list." : NOT_INVITED); return; }')
    o = 'let diag = {}, lastErr = null;'
    assert s.count(o) == 1, "diag"
    s = s.replace(o, o + '\nconst NOT_INVITED = ' + repr(NOTINV).replace("'", '"') + ';')
    s = s.replace("/* review_fix5 */", "/* review_fix5 */ /* review_fix6 */", 1)
    open(p, "w", encoding="utf-8").write(s); return "fixed"
for p in sys.argv[1:]:
    try: print(p.split("/")[-1], fix(p))
    except (ValueError, AssertionError) as e: print(p, "SKIPPED:", e)
