#!/usr/bin/env python3
"""One review page for all Set 20 hooks: takes the per-ad `vs present` outputs and joins them into a tabbed page.
Each hook keeps its own comment list (db collection comments_H1, comments_H2, ...). Tabs route on #h1/#h2/#h3.
Usage: make_review.py <review_dir> <out_dir> H1=H1_v4 H2=H2_v1 H3=H3_v1"""
import json, re, sys
from pathlib import Path

src, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
hooks = dict(a.split("=") for a in sys.argv[3:])
cfgs, files = {}, {}
for h, d in hooks.items():
    pj = json.load(open(src / d / "publish.json")); c = pj["config"]
    c["title"] = "RootOut Set 20"; c["slug"] = f"rootout-set-20-{h.lower()}"
    for k in ("video", "poster"): files[f"{h}/{c[k]}"] = pj["files"][c[k]]; c[k] = f"{h}/{c[k]}"
    files[f"{h}/{c['strip']['src']}"] = pj["files"][c["strip"]["src"]]; c["strip"]["src"] = f"{h}/{c['strip']['src']}"
    cfgs[h] = c
first = next(iter(hooks)); html = (src / hooks[first] / "index.html").read_text()
html = re.sub(r"<title>.*?</title>", "<title>RootOut Set 20 Review</title>", html, count=1)
html = re.sub(r'(<script id="vs-config" type="application/json">).*?(</script>)',
              lambda m: m.group(1) + json.dumps(cfgs).replace("<", "\\u003c") + m.group(2), html, count=1, flags=re.S)
pick = ('const ALL = JSON.parse(document.getElementById("vs-config").textContent);\n'
        '  const HOOKS = Object.keys(ALL);\n'
        '  const HOOK = HOOKS.find(k => "#" + k.toLowerCase() === location.hash) || HOOKS[0];\n'
        '  const cfg = ALL[HOOK];\n'
        '  document.querySelectorAll(".hooktab").forEach(a => a.setAttribute("aria-current", a.dataset.hook === HOOK ? "page" : "false"));\n'
        '  addEventListener("hashchange", () => location.reload());')
html = html.replace('const cfg = JSON.parse(document.getElementById("vs-config").textContent);', pick, 1)
assert "const HOOK =" in html
n = html.count('collection("comments")'); assert n == 2, n
html = html.replace('collection("comments")', 'collection("comments_" + HOOK)')
tabs = '<nav class="hooktabs" aria-label="Hook">' + "".join(
    f'<a class="hooktab" href="#{h.lower()}" data-hook="{h}">{h}<span>{cfgs[h]["version"].split("_")[-1]} · {cfgs[h]["length"]}</span></a>'
    for h in hooks) + "</nav>"
html = html.replace('<h1 id="title"></h1>', '<h1 id="title"></h1>\n    ' + tabs, 1)
css = (".hooktabs { display: inline-flex; gap: 4px; padding: 3px; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; }\n"
       ".hooktab { display: inline-flex; align-items: baseline; gap: 6px; padding: 4px 10px; border-radius: 7px; color: var(--muted); text-decoration: none; font-weight: 600; }\n"
       ".hooktab span { font: 11px var(--font-tc); font-weight: 400; }\n"
       ".hooktab:hover { color: var(--fg); }\n"
       '.hooktab[aria-current="page"] { background: var(--accent); color: var(--accent-ink); }\n</style>')
html = html.replace("</style>", css, 1)
(out / "index.html").write_text(html)
json.dump({"file_path": str(out / "index.html"), "files": files}, open(out / "publish.json", "w"), indent=1)
print(out / "index.html", len(html), "bytes;", len(files), "media files")
