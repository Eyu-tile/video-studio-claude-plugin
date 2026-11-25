#!/usr/bin/env python3
"""Shared catalogue of every Higgsfield (WilloMd) generation, so every RootOut session reuses what the others made.

  python3 -I catalog.py build <show_generations page JSON files...>   rebuild catalog.jsonl + CATALOG.md from raw pages
  python3 -I catalog.py search "dandelion root"  [--type video] [--since 2026-11-21]   find clips by words in name/prompt/notes
  python3 -I catalog.py add <job_id> --type video --name s5_snap --set "Set 5" --notes "hand snaps dandelion" [--prompt "..."] [--verdict use|backup|reject]
  python3 -I catalog.py get <job_id or 8-char prefix>                 one entry

Download a clip: call mcp__WilloMd__jobs_wait with its job id (returns result_url), then curl it into the project.
No URLs are stored here: they carry the account id.
Reuse costs 0 credits; pass a job id as a Seedance/Soul media value to use it as a reference.
"""
import json, re, sys, datetime, glob
from pathlib import Path
HERE = Path(__file__).resolve().parent; LIB = HERE.parent
CAT, MD = HERE / "catalog.jsonl", HERE / "CATALOG.md"
ROOTOUT_START = datetime.datetime(2026, 11, 21, tzinfo=datetime.UTC).timestamp()

def load():
    return [json.loads(l) for l in CAT.read_text().splitlines() if l.strip()] if CAT.exists() else []

def save(rows):
    rows.sort(key=lambda r: -r.get("ts", 0))
    CAT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)); write_md(rows)

def known_names():
    """job id -> (name, set) from every build kit's jobs.json / GEN_LOG in the library."""
    out = {}
    for f in list(LIB.glob("ads/*/jobs.json")) + list(LIB.glob("ads/**/jobs*.json")):
        st = f.parent.name.replace("_build", "").replace("set", "Set ")
        def walk(o, path=""):
            if isinstance(o, dict):
                for k, v in o.items(): walk(v, k if not path else f"{path}.{k}")
            elif isinstance(o, list):
                for x in o: walk(x, path)
            elif isinstance(o, str) and re.fullmatch(r"[0-9a-f]{8}-[0-9a-f-]{27}", o):
                out.setdefault(o, (path.split(".")[-1], st))
        try: walk(json.loads(f.read_text()))
        except Exception: pass
    reuse = LIB / "ads/set18_build/REUSE.md"
    if reuse.exists():
        for line in reuse.read_text().splitlines():
            m = re.search(r"(S\d+) (\w+) · ([0-9a-f]{8})", line)
            if m:
                cells = [c.strip() for c in line.split("|")]
                out.setdefault("prefix:" + m.group(3), (m.group(2), "Set " + m.group(1)[1:], cells[4] if len(cells) > 4 else ""))
    return out

def build(files):
    old = {r["id"]: r for r in load()}; names = known_names(); rows = {}
    for f in files:
        for it in json.load(open(f)).get("items", []):
            p = it.get("params") or {}; meds = p.get("medias") or []
            refs = [{"role": m.get("role"), "id": (m.get("data") or {}).get("id") or m.get("value")} for m in meds if isinstance(m, dict)]
            res = it.get("results") or {}
            r = {"id": it["id"], "type": it.get("type"), "model": it.get("model"), "ts": it.get("createdAt", 0),
                 "date": datetime.datetime.fromtimestamp(it.get("createdAt", 0), datetime.UTC).strftime("%Y-%m-%d"),
                 "rootout_era": it.get("createdAt", 0) >= ROOTOUT_START, "status": it.get("status"),
                 "duration": p.get("duration"), "aspect": p.get("aspect_ratio"), "prompt": str(p.get("prompt") or "")[:700],
                 "refs": refs}  # no download URLs here (they carry the account id): get one with jobs_wait on the id
            n = names.get(it["id"]) or names.get("prefix:" + it["id"][:8])
            if n: r["name"], r["set"] = n[0], n[1]; r["notes"] = n[2] if len(n) > 2 else ""
            keep = old.get(it["id"], {})
            for k in ("name", "set", "notes", "verdict"):
                if keep.get(k): r[k] = keep[k]
            rows[it["id"]] = r
    for k, v in old.items(): rows.setdefault(k, v)
    save(list(rows.values())); print(f"{len(rows)} generations in {CAT.name}")

def write_md(rows):
    ro = [r for r in rows if r.get("rootout_era")]
    by = lambda t: [r for r in ro if r["type"] == t]
    L = ["# Higgsfield (WilloMd) generation catalogue", "",
         "Every generation on the WilloMd account, so each RootOut session can reuse what the others made (0 credits).",
         "Full data (prompt, references) is in `catalog.jsonl`; get a download link with jobs_wait on the id; search it with",
         "`python3 -I video-studio/library/RootOut/higgsfield/catalog.py search \"<words>\"`.",
         "**Before generating anything, search here. After every generation, add it** (`catalog.py add <job_id> --name ... --set ... --notes ...`) and push.", "",
         f"Totals: {len(rows)} generations ({sum(r['type']=='video' for r in rows)} video, {sum(r['type']=='image' for r in rows)} image, "
         f"{sum(r['type']=='audio' for r in rows)} audio). RootOut era (from 21 Nov 2026): {len(ro)}.", ""]
    for t in ("video", "image", "audio"):
        rs = by(t); named = [r for r in rs if r.get("name")]
        L += [f"## RootOut-era {t} ({len(rs)}; {len(named)} named by a set)", "", "| date | id (8) | set · name | model | what it is (prompt start) |", "|---|---|---|---|---|"]
        for r in rs:
            what = (r.get("notes") or r.get("prompt") or "").replace("|", "/").replace("\n", " ")[:110]
            L.append(f"| {r['date']} | `{r['id'][:8]}` | {(r.get('set','') + ' · ' + r.get('name','')).strip(' ·')} | {r['model']} | {what} |")
        L.append("")
    L += ["## Before 21 Nov (other WilloMd products)", "", f"{sum(1 for r in rows if not r.get('rootout_era'))} generations, listed only in `catalog.jsonl` (`search --before 2026-11-21`).", ""]
    MD.write_text("\n".join(L))

def search(words, typ=None, since=None):
    ws = [w.lower() for w in words.split()]
    for r in load():
        if typ and r["type"] != typ: continue
        if since and r["date"] < since: continue
        hay = " ".join(str(r.get(k, "")) for k in ("name", "set", "notes", "prompt")).lower()
        if all(w in hay for w in ws):
            print(f"{r['date']} {r['id']} {r['type']:5} {r['model']:14} {(r.get('set','')+' '+r.get('name','')).strip():24} {(r.get('notes') or r['prompt'])[:120]}")

def add(job, **kw):
    rows = {r["id"]: r for r in load()}; r = rows.get(job, {"id": job, "ts": datetime.datetime.now(datetime.UTC).timestamp(),
             "date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"), "rootout_era": True, "model": kw.get("model") or "", "refs": []})
    for k, v in kw.items():
        if v: r[k] = v
    rows[job] = r; save(list(rows.values())); print("added", job[:8], r.get("name", ""))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit()
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    if a[0] == "build": build(a[1:])
    elif a[0] == "search": search(a[1], opt("--type"), opt("--since"))
    elif a[0] == "get":
        for r in load():
            if r["id"].startswith(a[1]): print(json.dumps(r, indent=1, ensure_ascii=False))
    elif a[0] == "add":
        add(a[1], type=opt("--type"), name=opt("--name"), set=opt("--set"), notes=opt("--notes"), prompt=opt("--prompt"), verdict=opt("--verdict"), model=opt("--model"))
