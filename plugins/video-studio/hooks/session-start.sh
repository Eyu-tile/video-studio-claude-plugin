#!/usr/bin/env bash
# Put the plugin's `vs` CLI on PATH for every Bash command in the session, and mention open client tasks
# (vs task) so a returning session can pick up where it left off.
[ -n "${CLAUDE_ENV_FILE:-}" ] && [ -n "${CLAUDE_PLUGIN_ROOT:-}" ] || exit 0
printf 'export PATH="%s/bin:$PATH"\nexport VS_ROOT="%s"\n' "$CLAUDE_PLUGIN_ROOT" "$CLAUDE_PLUGIN_ROOT" >> "$CLAUDE_ENV_FILE"
hist="${VS_WORKSPACE:-${CLAUDE_PROJECT_DIR:-$PWD}/video-studio}/history"
if [ -d "$hist" ] && command -v python3 >/dev/null 2>&1; then
  python3 - "$hist" <<'PY' 2>/dev/null || true
import json, sys
from pathlib import Path
rows = []
for p in sorted(Path(sys.argv[1]).glob("*.json")):
    try:
        t = json.loads(p.read_text())
    except Exception:
        continue
    if t.get("status") == "closed":
        continue
    fb = sum(f.get("status") == "open" for f in t.get("feedback", []))
    last = t["versions"][-1]["version"] if t.get("versions") else "no delivery"
    rows.append((t.get("updated", ""), f"{t['code']} ({t.get('client') or '-'}: {t.get('title') or ''}) "
                 f"{t.get('status')}, last {last}, {fb} open feedback"))
if rows:
    rows.sort(reverse=True)
    print("video-studio open client tasks (newest first). When the person names a code or says continue, run "
          "`vs task resume <CODE>` before anything else:")
    for _, r in rows[:8]:
        print(" -", r)
PY
fi
exit 0
