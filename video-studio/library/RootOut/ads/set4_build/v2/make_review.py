#!/usr/bin/env python3
"""One client review page for all three hooks, in the same format as the other RootOut sets (Set 20):
`vs present` builds each hook's proxy, filmstrip and poster; this joins them into one page with H1/H2/H3 tabs,
one shared comment list per hook (collections comments_H1, comments_H2, comments_H3).
make_review.py   (after: vs present out/v2/..._H1_9x16_v3.mp4 -o out/review_set4/H1, same for H2/H3)"""
import json
from pathlib import Path

R = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4/out/review_set4")
HOOKS = ["H1", "H2", "H3"]
CSS = """.hooktabs { display: inline-flex; gap: 4px; padding: 3px; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; }
.hooktab { display: inline-flex; align-items: baseline; gap: 6px; padding: 4px 10px; border-radius: 7px; color: var(--muted); text-decoration: none; font-weight: 600; }
.hooktab span { font: 11px var(--font-tc); font-weight: 400; }
.hooktab:hover { color: var(--fg); }
.hooktab[aria-current="page"] { background: var(--accent); color: var(--accent-ink); }
"""
cfgs = {}
for h in HOOKS:
    c = json.loads((R / h / "publish.json").read_text())["config"]
    c["video"], c["poster"] = f"{h}/video.mp4", f"{h}/poster.jpg"
    c["strip"]["src"] = f"{h}/strip.jpg"
    cfgs[h] = c
page = (R / "H1/index.html").read_text()
start = page.index('<script id="vs-config" type="application/json">') + len('<script id="vs-config" type="application/json">')
end = page.index("</script>", start)
page = page[:start] + json.dumps(cfgs) + page[end:]
tabs = "".join(f'<a class="hooktab" href="#{h.lower()}" data-hook="{h}">{h}<span>v3 · {cfgs[h]["length"]}</span></a>' for h in HOOKS)
reps = [
    ("</style>", CSS + "</style>"),
    ('<h1 id="title"></h1>', f'<h1 id="title"></h1>\n    <nav class="hooktabs" aria-label="Hook">{tabs}</nav>'),
    ('  const cfg = JSON.parse(document.getElementById("vs-config").textContent);',
     '  const ALL = JSON.parse(document.getElementById("vs-config").textContent);\n'
     '  const HOOKS = Object.keys(ALL);\n'
     '  const HOOK = HOOKS.find(k => "#" + k.toLowerCase() === location.hash) || HOOKS[0];\n'
     '  const cfg = ALL[HOOK];\n'
     '  document.querySelectorAll(".hooktab").forEach(a => a.setAttribute("aria-current", a.dataset.hook === HOOK ? "page" : "false"));\n'
     '  addEventListener("hashchange", () => location.reload());'),
    ('dbRef.collection("comments")', 'dbRef.collection("comments_" + HOOK)'),
    ('db.collection("comments")', 'db.collection("comments_" + HOOK)'),
]
for a, b in reps:
    assert page.count(a) == 1, a
    page = page.replace(a, b)
import re
page = re.sub(r"<title>[^<]*</title>", "<title>RootOut Set 4 Review</title>", page, count=1)
(R / "index.html").write_text(page)
files = {f"{h}/{n}": str(R / h / n) for h in HOOKS for n in ("video.mp4", "strip.jpg", "poster.jpg")}
(R / "publish.json").write_text(json.dumps({"file_path": str(R / "index.html"), "files": files,
    "capabilities": {"db": {}, "user": {"scopes": ["profile"]}, "downloads": {}}}, indent=1))
print(R / "index.html", "title ok" if "<title>RootOut Set 4 Review</title>" in page else "CHECK TITLE")
