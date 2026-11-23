import json, re, shutil
ads = [("h1", "h1-v4", "H1", "“Sorry to keep you waiting. It's wart season.”"),
       ("h2", "h2-v3", "H2", "“I'd get it down till the black dots were gone…”"),
       ("h3", "h3-v3", "H3", "“His wart is back. Again.”")]
cfgs = {}
for key, ver, label, hook in ads:
    c = json.load(open(f"{ver}/publish.json"))["config"]
    c.update({"id": f"rootout-set17-{ver}", "slug": f"rootout-set17-{key}", "title": f"RootOut Set 17 · {label}", "version": ver,
              "video": f"{key}.mp4", "poster": f"{key}_poster.jpg", "collection": f"comments_{key}", "label": label, "hook": hook})
    c["strip"]["src"] = f"{key}_strip.jpg"; cfgs[key] = c
src = open("h1-v4/index.html").read()
src = re.sub(r"<title>.*?</title>", lambda m: "<title>RootOut Set 17 Review</title>", src, count=1)
blob = json.dumps({"order": [a[0] for a in ads], "ads": cfgs}, ensure_ascii=False).replace("</", "<\\/")
src = re.sub(r'<script id="vs-config" type="application/json">.*?</script>',
             lambda m: '<script id="vs-configs" type="application/json">' + blob + "</script>", src, count=1, flags=re.S)
old = 'const cfg = JSON.parse(document.getElementById("vs-config").textContent);'
assert old in src
src = src.replace(old, '''const ALL = JSON.parse(document.getElementById("vs-configs").textContent);
  const pick = () => { const k = (location.hash || "").replace("#", ""); return ALL.ads[k] ? k : ALL.order[0]; };
  const AD = pick(); const cfg = ALL.ads[AD];
  // tab bar: one ad per tab; switching reloads the page on that ad (each ad has its own video and comment thread)
  (() => {
    const nav = document.getElementById("adTabs");
    for (const k of ALL.order) {
      const a = ALL.ads[k], b = document.createElement("button");
      b.type = "button"; b.className = "adtab" + (k === AD ? " on" : ""); b.setAttribute("aria-pressed", k === AD ? "true" : "false");
      const t = document.createElement("b"); t.textContent = a.label;
      const s = document.createElement("span"); s.textContent = `${a.version} · ${a.length}`;
      const h = document.createElement("i"); h.textContent = a.hook;
      b.append(t, s, h);
      b.addEventListener("click", () => { if (k === AD) return; location.hash = k; location.reload(); });
      nav.appendChild(b);
    }
    window.addEventListener("hashchange", () => { if (pick() !== AD) location.reload(); });
  })();''')
assert src.count('collection("comments")') == 2
src = src.replace('collection("comments")', 'collection(cfg.collection || "comments")')
assert '<div class="app">\n  <header>' in src
src = src.replace('<div class="app">\n  <header>', '<div class="app">\n  <nav class="adtabs" id="adTabs" aria-label="Ads in this set"></nav>\n  <header>', 1)
css = '''
.adtabs { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin: 14px 0 4px; }
.adtab { display: grid; gap: 2px; text-align: left; padding: 10px 12px; border-radius: 10px; border: 1px solid var(--line);
  background: var(--panel); color: var(--fg); min-width: 0; }
.adtab b { font-size: 15px; font-weight: 600; }
.adtab span { color: var(--muted); font: 12px var(--font-tc); }
.adtab i { font-style: normal; color: var(--muted); font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.adtab:hover { border-color: var(--muted); }
.adtab.on { border-color: var(--accent); background: var(--raised); box-shadow: inset 0 -2px 0 var(--accent); }
.adtab.on b { color: var(--accent); }
@media (max-width: 560px) { .adtab i { display: none; } .adtab { padding: 8px 10px; } }
</style>'''
src = src.replace("</style>", css, 1)
open("set17/index.html", "w").write(src); print("ok", len(src))
