#!/usr/bin/env python3
"""Hyperscale bridge: a brief in Hyperscale becomes a video-studio project, and the finished ads go back onto it.

Hyperscale (the team's ad studio: briefs, review notes, Library, swipes, kie.ai generation) is reached through
its MCP connector; Claude makes those calls. This tool does the local half: it turns a saved brief into a
project, plans the exports and the Library searches, keeps review notes in sync with `vs notes` / `vs task`,
and prepares, uploads and records the finished files.

  vs hyperscale pull <brief.json> [--project NAME] [--brand "Haven & Spool"]
        brief.json = the get_brief result saved as JSON. Creates projects/hs-<number>-<title>/ with BRIEF.md,
        work/brief.json (vs ads brief), work/hyperscale/{brief,exports,shots}.json, notes.txt, and task HS-<number>
  vs hyperscale notes <brief.json> --project P      refresh review notes (new ones -> notes.txt + vs task feedback)
  vs hyperscale shots --project P                   per script row: what to search in the Library (search_library args)
  vs hyperscale prep --project P [--file H1=out/a.mp4 ...] [--ending evergreen] [--version 3]
        strip metadata (-map_metadata -1, faststart), check size/aspect/codec/audio, name each file
        <number>_<hook>_<size>_v<N>[_<ending>].mp4 in out/hyperscale/, write work/hyperscale/upload.json
  vs hyperscale put --project P <name|hook> --url <upload_url> [--upload-id ID]   PUT the file to the one-time link
  vs hyperscale done --project P <name|hook> --upload-id ID                       mark it attached (finish_brief_upload)
  vs hyperscale status --project P                  exports planned / prepared / uploaded, open notes, next step
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, probe, save_json  # noqa: E402

BIN = Path(__file__).resolve().parents[1] / "bin" / "vs"
AWARE = {"unaware": "unaware", "problem": "problem", "solution": "solution", "product": "product", "most": "most"}
ACTIONS = [(r"\brol(l|ling|ls)\b|roller", "Rolling on"), (r"\bpour", "Pouring"), (r"\bhold", "Holding"),
           (r"\bappl(y|ying)|\brub|press(es|ing)? oil", "Applying"), (r"\bopen(s|ing)?\b(?! palm)", "Opening")]
SHOTS = [(r"close-?up|macro", "Close-up"), (r"selfie", "Selfie"), (r"top-?down|overhead", "Top-down"),
         (r"\bwide\b", "Wide"), (r"\bhands?\b(?! sweep)", "Hands only"), (r"mid shot", "Mid shot")]
NOT_LIBRARY = r"archive|papyrus|tomb|museum|collage|animation|diagram|end card|reenactment|vintage photo|calendar"


def now():
    return time.strftime("%Y-%m-%d %H:%M")


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    except OSError:
        root = ""
    return Path(root or os.getcwd()) / "video-studio"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:40] or "brief"


def proj(p):
    if not p:
        die("give --project (folder name under projects/ or a path)")
    d = Path(p)
    if not d.is_dir():
        d = workspace() / "projects" / p
    if not d.is_dir():
        die(f"project not found: {p}")
    return d


def hs_dir(d):
    return d / "work" / "hyperscale"


def state(d):
    f = hs_dir(d) / "state.json"
    return load_json(f) if f.exists() else {}


def save_state(d, s):
    save_json(hs_dir(d) / "state.json", s)


def vs(*args, ok=False):
    r = subprocess.run(["bash", str(BIN), *args], capture_output=True, text=True, env={**os.environ})
    if ok and r.returncode:
        die(f"vs {' '.join(args)} failed: {(r.stderr or r.stdout).strip()[-400:]}")
    return r


def who(email):
    return (email or "reviewer").split("@")[0]


# --- reading the brief -------------------------------------------------------------------------------------------

def all_text(b):
    rows = b.get("script") or []
    parts = [b.get("idea", ""), " ".join(b.get("editing_notes") or [])]
    parts += [" ".join(str(r.get(k, "")) for k in ("script", "visual", "on_screen_text")) for r in rows]
    return "\n".join(parts)


def awareness(b):
    a = (b.get("awareness") or "").lower()
    return next((v for k, v in AWARE.items() if a.startswith(k)), "problem")


def age_band(b):
    txt = all_text(b)
    m = re.search(r"\b(\d{2})\s*(?:-|–|to)\s*(\d{2})\b", txt)
    if m:
        mid = (int(m.group(1)) + int(m.group(2))) / 2
    else:
        m = re.search(r"\b(\d{2})\+", txt)
        mid = int(m.group(1)) if m else 40
    return "55+" if mid >= 55 else "35-54" if mid >= 35 else "18-34"


def endings(b):
    txt = all_text(b).lower()
    if "evergreen" in txt and ("two endings" in txt or "second export" in txt or "black friday" in txt):
        return ["bf", "evergreen"]
    return [""]


def offer(b):
    for r in reversed(b.get("script") or []):
        for k in ("on_screen_text", "script"):
            m = re.search(r"(buy\s*1[^\n]*?(?:free|guarantee)[^\n]*)|(buy one,? get one free[^.\n]*)",
                          str(r.get(k, "")), re.I)
            if m:
                return re.sub(r"^.*?END CARD:\s*", "", m.group(0)).strip(" .")
    return ""


def claims(b):
    out, seen = [], set()
    for r in b.get("script") or []:
        for m in re.finditer(r"Source:\s*([^\n.]+)", str(r.get("on_screen_text", ""))):
            src = m.group(1).strip()
            line = str(r.get("script", "")).strip().splitlines()
            key = (line[-1] if line else "", src)
            if key not in seen:
                seen.add(key)
                out.append({"claim": key[0][:200], "evidence": f"per {src}", "source": src})
    return out


def product(b):
    txt = all_text(b).lower()
    if "belly pack" in txt:
        return "Castor Oil Belly Pack" if "castor" in txt else "Belly Pack"
    if re.search(r"roller|roll-on|roll on|rolling it on", txt):
        return "Castor Oil Roll On" if "castor" in txt else "Roll-on"
    return ""


def ads_brief(b, brand, prod=None):
    ugc = "ugc" in (b.get("video_type") or "").lower()
    txt = all_text(b).lower()
    return {
        "client": brand or "", "product": prod or product(b), "offer": offer(b),
        "cta": "Tap the link below" if "link below" in txt else "Shop now",
        "format": "ugc" if ugc else "vsl", "platform": "reels", "length": None,
        "audience": {"who": next((n.split("\n")[0][8:].strip() for n in b.get("editing_notes") or []
                                  if n.startswith("Avatar:")), ""), "age": age_band(b), "gender": "female"
                     if re.search(r"\bwom[ae]n\b", txt) else "mixed"},
        "emotion": "relief from embarrassment" if "skin tag" in txt else "confidence",
        "awareness": awareness(b), "angles": [b.get("angle", "")], "variants": len(b.get("hooks") or []) or 1,
        "claims": claims(b),
        "creator": {"name": "", "paid": ugc, "disclosure": "Paid partnership label / #ad" if ugc else ""},
        "policy": {"category": "beauty", "before_after": bool(re.search(r"before\W+(and\W+)?after", txt))},
        "brand": {"font": "Montserrat", "accent": "#FFD400", "logo": ""},
        "footage": [], "references": [b["reference"]] if b.get("reference") else [],
        "notes": f"Hyperscale brief #{b.get('number')} ({b.get('title')}). Read BRIEF.md: the editing notes there win.",
    }


def brief_md(b):
    L = [f"# Hyperscale brief #{b.get('number')}: {b.get('title')}", "",
         f"- Stage: {b.get('stage')} (round {b.get('round')}) · Pod: {b.get('pod')} · Strategist: "
         f"{b.get('strategist')} · Editor: {b.get('editor')}",
         f"- Angle: {b.get('angle')} · Awareness: {b.get('awareness')} · Type: {b.get('video_type')} · "
         f"Format: {b.get('format')}",
         f"- Hooks: {', '.join(b.get('hooks') or [])} · Sizes: {', '.join(b.get('sizes') or [])}",
         f"- Reference: {b.get('reference') or '-'}", "", "## Idea", "", (b.get("idea") or "").strip(), "",
         "## Script", ""]
    for i, r in enumerate(b.get("script") or [], 1):
        L.append(f"### Row {i}: {r.get('module')}")
        for k, name in (("script", "VO / words"), ("visual", "Visual"), ("on_screen_text", "On screen")):
            v = str(r.get(k) or "").strip()
            if v:
                L += [f"**{name}:**", "", v, ""]
    L += ["## Editing notes", ""]
    for n in b.get("editing_notes") or []:
        L += ["- " + n.strip().replace("\n", "\n  "), ""]
    if b.get("ads"):
        L += ["## Uploaded so far", "", ", ".join(b["ads"]), ""]
    return "\n".join(L) + "\n"


def library_query(i, r, b):
    vis = str(r.get("visual") or "")
    low = vis.lower()
    q = {"heading": f"Row {i}: {r.get('module')} - {vis[:60].strip()}"}
    m = re.search(r"Library:\s*([^)]+)\)", vis)
    if m:
        for part in m.group(1).split(","):
            k, _, v = part.strip().partition(" ")
            if k in ("angle", "action", "shot", "style", "product", "folder", "age", "cap", "gender"):
                q[k] = v.strip()
        m2 = re.search(r'Library\s*"([^"]+)"', vis)
        if m2:
            q["query"] = m2.group(1)
    for pat, tag in ACTIONS:
        if "action" not in q and re.search(pat, low):
            q["action"] = tag
    for pat, tag in SHOTS:
        if "shot" not in q and re.search(pat, low):
            q["shot"] = tag
    if re.search(r"\bwom[ae]n\b", low):
        q.setdefault("gender", "Woman")
    if re.search(r"\b(5[5-9]|6\d)\b|55\+|50\s*-\s*6\d", low):
        q.setdefault("age", "55+")
    if "ugc" in low or "ugc" in (b.get("video_type") or "").lower():
        q.setdefault("style", "UGC")
    if re.search(r"roller|roll-on|our (real )?bottle|our oil", low):
        q.setdefault("product", "Roll On")
    elif "belly pack" in low:
        q.setdefault("product", "Belly Pack")
    return q


def shot_plan(b):
    out = []
    for i, r in enumerate(b.get("script") or [], 1):
        vis = str(r.get("visual") or "").strip()
        if not vis or (r.get("module", "").lower() == "hook" and vis[:1] in "\"“'‘"):
            # short hook rows whose "visual" is really the hook text
            out.append({"row": i, "module": r.get("module"), "visual": vis, "source": "text",
                        "note": "hook title text, not footage"})
            continue
        low = vis.lower()
        real = re.search(r"real (footage|woman|ugc)|our (real )?bottle|rolling|\bwom[ae]n\b|product", low)
        src = ("mixed" if real else "graphics-or-archive") if re.search(NOT_LIBRARY, low) else "library"
        out.append({"row": i, "module": r.get("module"), "visual": vis, "source": src,
                    "search_library": library_query(i, r, b)})
    return out


def exports_plan(b):
    sizes = b.get("sizes") or ["9x16"]
    hooks = b.get("hooks") or ["H1"]
    last = {}
    for a in b.get("ads") or []:
        m = re.match(r"(H\d+)\s+(\d+)[:x](\d+)\s+v(\d+)", a)
        if m:
            k = (m.group(1), f"{m.group(2)}x{m.group(3)}")
            last[k] = max(last.get(k, 0), int(m.group(4)))
    rows = []
    for h in hooks:
        for s in sizes:
            for e in endings(b):
                v = last.get((h, s), 0) + 1
                rows.append({"hook": h, "size": s, "ending": e, "version": v,
                             "label": f"{h} {s.replace('x', ':')} v{v}" + (f" ({e})" if e else ""),
                             "name": f"{b.get('number')}_{h}_{s}_v{v}" + (f"_{e}" if e else "") + ".mp4"})
    return rows


# --- commands ----------------------------------------------------------------------------------------------------

def sync_notes(d, b, s):
    seen = set(s.get("notes_seen", []))
    new = []
    for n in b.get("open_notes") or []:
        key = hashlib.sha1(f"{n.get('at')}|{n.get('note')}".encode()).hexdigest()[:12]
        if key not in seen:
            seen.add(key)
            new.append(n)
    s["notes_seen"] = sorted(seen)
    s["open_notes"] = b.get("open_notes") or []
    lines = [f"{n.get('at') or ''} {n.get('note')}".strip() for n in s["open_notes"]]
    (hs_dir(d) / "notes.txt").write_text("\n".join(lines) + ("\n" if lines else ""))
    if new and s.get("task"):
        txt = "\n".join(f"{n.get('at') or ''} {n.get('note')}".strip() for n in new)
        vs("task", "feedback", s["task"], txt, "--split", "--who", who(new[0].get("by")))
    docs = [u for n in new for u in re.findall(r"https://docs\.google\.com/\S+", n.get("note", ""))]
    return new, docs


def cmd_pull(a):
    b = load_json(a.brief)
    if "number" not in b:
        die("that file is not a get_brief result (no 'number')")
    ws = workspace()
    name = a.project or f"hs-{b['number']}-{slug(b.get('title'))}"
    d = ws / "projects" / name
    if not d.exists():
        vs("new", name, ok=True)
    h = hs_dir(d)
    save_json(h / "brief.json", b)
    (d / "BRIEF.md").write_text(brief_md(b))
    brand = a.brand or (load_json(ws / ".hyperscale.json").get("brand") if (ws / ".hyperscale.json").exists() else "")
    if a.brand:
        save_json(ws / ".hyperscale.json", {"brand": a.brand})
    ab = d / "work" / "brief.json"
    if not ab.exists() or a.force:
        save_json(ab, ads_brief(b, brand, a.product))
    save_json(h / "shots.json", shot_plan(b))
    save_json(h / "exports.json", exports_plan(b))
    s = state(d)
    s.update({"number": b["number"], "title": b.get("title"), "brand": brand, "pulled": now(),
              "stage": b.get("stage"), "round": b.get("round")})
    code = f"HS-{b['number']}"
    if not a.no_task:
        hist = ws / "history" / f"{code}.json"
        if not hist.exists():
            vs("task", "new", code, "--project", name, "--client", brand or "Hyperscale", "--title",
               f"#{b['number']} {b.get('title')} ({b.get('angle')})", "--brief", str(d / "BRIEF.md"), ok=True)
        s["task"] = code
    pm = d / "project.md"
    if pm.exists() and "Hyperscale brief" not in pm.read_text():
        with open(pm, "a") as fh:
            fh.write(f"\n## Hyperscale\n- Brief #{b['number']} \"{b.get('title')}\" ({b.get('pod')}, strategist "
                     f"{b.get('strategist')}). Full brief: BRIEF.md. Sync: `vs hyperscale status --project {name}`\n")
    new, docs = sync_notes(d, b, s)
    save_state(d, s)
    ex = exports_plan(b)
    sp = shot_plan(b)
    print(f"brief #{b['number']} \"{b.get('title')}\" -> {d}")
    print(f"  BRIEF.md, work/brief.json (vs ads brief: check it with `vs ads brief {ab}`)")
    print(f"  exports: {len(ex)} ({', '.join(e['name'] for e in ex[:6])}{' ...' if len(ex) > 6 else ''})")
    print(f"  shots: {sum(x['source'] == 'library' for x in sp)} rows to search in the Library, "
          f"{sum(x['source'] == 'mixed' for x in sp)} mixed, "
          f"{sum(x['source'] == 'graphics-or-archive' for x in sp)} graphics/archive only")
    if s.get("task"):
        print(f"  task {s['task']} (vs task resume {s['task']})")
    if new:
        print(f"  {len(new)} new review note(s) -> work/hyperscale/notes.txt")
    for u in docs:
        print(f"  a note links a doc: read it (Google Drive read_file_content, includeComments) before editing: {u}")
    print(f"next: vs hyperscale shots --project {name}  (then search_library once per row)")


def cmd_notes(a):
    d = proj(a.project)
    b = load_json(a.brief)
    save_json(hs_dir(d) / "brief.json", b)
    s = state(d)
    s.update({"stage": b.get("stage"), "round": b.get("round")})
    new, docs = sync_notes(d, b, s)
    save_state(d, s)
    print(f"{len(s['open_notes'])} open note(s), {len(new)} new -> {hs_dir(d) / 'notes.txt'}")
    for n in s["open_notes"]:
        print(f"  {n.get('at') or '--'}  {n.get('note')}  ({who(n.get('by'))})")
    for u in docs:
        print(f"  read the linked doc before editing: {u}")
    if s["open_notes"]:
        print(f"next: vs notes add {d}/work/notes.json --edl <the reviewed EDL> {hs_dir(d) / 'notes.txt'}")


def cmd_shots(a):
    d = proj(a.project)
    plan = load_json(hs_dir(d) / "shots.json")
    for x in plan:
        print(f"Row {x['row']} [{x['module']}] {x['source']}")
        print(f"   {x['visual'][:150]}{'...' if len(x['visual']) > 150 else ''}")
        if x.get("search_library"):
            q = {k: v for k, v in x["search_library"].items()}
            print("   search_library " + ", ".join(f"{k}={v!r}" for k, v in q.items()))
    print("library = search it; mixed = search the real-footage part, build the collage/archive part; "
          "graphics-or-archive = motion graphics (HyperFrames) or vs fetch (Commons, Met, Archive).")
    print("Rule: search the Library first; generate (quote + yes) only what nothing fits. Download picks with\n"
          f"  vs add <file url> --project {d.name} --as broll --credit \"Hyperscale Library\" --license \"brand-owned\"")


def parse_files(a, d, plan):
    pairs = []
    for f in a.file or []:
        hook, _, path = f.partition("=")
        if not path:
            die(f"--file wants HOOK=path, got {f}")
        pairs.append((hook.upper(), Path(path) if Path(path).is_absolute() else d / path))
    if not pairs:  # newest render per hook in out/
        for e in plan:
            c = [p for p in (d / "out").rglob("*.mp4") if "hyperscale" not in p.parts
                 and re.search(rf"(^|[^a-z0-9]){e['hook'].lower()}([^0-9]|$)", p.stem.lower())
                 and (not e["ending"] or e["ending"] in p.stem.lower())]
            if c:
                pairs.append((e["hook"], max(c, key=lambda p: p.stat().st_mtime)))
    return pairs


def check_file(p, size):
    info = probe(p)
    probs = []
    w, h = info["width"], info["height"]
    sw, _, sh = size.partition("x")
    if w and h and sw and sh and abs(w / h - int(sw) / int(sh)) > 0.01:
        probs.append(f"{w}x{h} is not {size}")
    if info["vcodec"] not in ("h264", "hevc"):
        probs.append(f"codec {info['vcodec']} (want h264)")
    if not info["has_audio"]:
        probs.append("no audio track")
    if info["duration"] < 3:
        probs.append(f"only {info['duration']:.1f}s long")
    return info, probs


def cmd_prep(a):
    d = proj(a.project)
    b = load_json(hs_dir(d) / "brief.json")
    plan = exports_plan(b)
    if a.version:
        for e in plan:
            e["version"] = a.version
            e["name"] = re.sub(r"_v\d+", f"_v{a.version}", e["name"])
            e["label"] = re.sub(r" v\d+", f" v{a.version}", e["label"])
    pairs = parse_files(a, d, plan)
    if not pairs:
        die("no finished renders found in out/ with H1/H2... in the name; pass --file H1=out/final_h1.mp4")
    outdir = d / "out" / "hyperscale"
    outdir.mkdir(parents=True, exist_ok=True)
    s = state(d)
    up = s.get("uploads", [])
    fails = 0
    for hook, src in pairs:
        if not src.exists():
            die(f"not found: {src}")
        cands = [e for e in plan if e["hook"] == hook and (e["ending"] == (a.ending or e["ending"]))]
        e = next((c for c in cands if not c["ending"] or c["ending"] in src.stem.lower()), cands[0] if cands else None)
        if not e:
            die(f"{hook} is not one of the brief's hooks ({', '.join(b.get('hooks') or [])})")
        dst = outdir / e["name"]
        r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-map", "0", "-map_metadata", "-1",
                            "-map_chapters", "-1", "-c", "copy", "-movflags", "+faststart", str(dst)],
                           capture_output=True, text=True)
        if r.returncode:
            die(f"ffmpeg could not prepare {src}: {r.stderr.strip()[-300:]}")
        info, probs = check_file(dst, e["size"])
        fails += bool(probs)
        up = [u for u in up if u["name"] != e["name"]]
        up.append({"name": e["name"], "hook": hook, "label": e["label"], "file": str(dst.relative_to(d)),
                   "source": str(src), "content_type": "video/mp4", "number": b["number"],
                   "seconds": round(info["duration"], 2), "problems": probs, "status": "prepared",
                   "prepared": now()})
        print(f"{'FAIL' if probs else 'ok  '} {e['name']}  {info['width']}x{info['height']} {info['duration']:.1f}s"
              + (f"  ({'; '.join(probs)})" if probs else ""))
    s["uploads"] = up
    save_state(d, s)
    save_json(hs_dir(d) / "upload.json", up)
    print("metadata stripped. Before uploading, run the QA: vs ads qa <file> --edl <edl> --brief work/brief.json")
    print(f"upload each: start_brief_upload(number={b['number']}, filename=<name>, hook=<H#>, "
          "content_type='video/mp4') -> vs hyperscale put --project " + d.name + " <name> --url <upload_url> "
          "--upload-id <upload_id> -> finish_brief_upload(upload_id, send_to_review on the last one)")
    if fails:
        sys.exit(1)


def find_upload(s, key):
    for u in s.get("uploads", []):
        if key in (u["name"], u["hook"], u["label"]):
            return u
    die(f"no prepared file '{key}' (vs hyperscale status shows them)")


def cmd_put(a):
    d = proj(a.project)
    s = state(d)
    u = find_upload(s, a.key)
    if u.get("problems") and not a.force:
        die(f"{u['name']} failed its checks ({'; '.join(u['problems'])}); fix it or pass --force")
    f = d / u["file"]
    if not re.match(r"^https://|^http://(127\.0\.0\.1|localhost)[:/]", a.url):
        die("the upload link must be https")
    r = subprocess.run(["curl", "-sS", "--fail-with-body", "-X", "PUT", "-H", f"Content-Type: {u['content_type']}",
                        "--data-binary", f"@{f}", a.url], capture_output=True, text=True)
    if r.returncode:
        die(f"upload failed: {(r.stdout + r.stderr).strip()[-400:]}")
    u.update({"status": "uploaded", "uploaded": now(), "sha256": hashlib.sha256(f.read_bytes()).hexdigest()})
    if a.upload_id:
        u["upload_id"] = a.upload_id
    save_state(d, s)
    print(f"uploaded {u['name']} ({f.stat().st_size // 1024} KB). Now: finish_brief_upload(upload_id="
          f"{a.upload_id or '<upload_id>'}) then vs hyperscale done --project {d.name} {u['name']} --upload-id ...")


def cmd_done(a):
    d = proj(a.project)
    s = state(d)
    u = find_upload(s, a.key)
    u.update({"status": "attached", "attached": now(), "upload_id": a.upload_id or u.get("upload_id")})
    save_state(d, s)
    left = [x for x in s["uploads"] if x["status"] != "attached"]
    print(f"{u['name']} is on brief #{s.get('number')}. {len(left)} still to attach.")
    if not left and s.get("task"):
        files = [x["file"] for x in s["uploads"]]
        args = ["task", "deliver", s["task"], "--note", a.note or f"uploaded to Hyperscale #{s.get('number')}",
                "--link", f"hyperscale brief #{s.get('number')}"]
        for f in files:
            args += ["--file", f]
        r = vs(*args)
        print((r.stdout or r.stderr).strip())


def cmd_status(a):
    d = proj(a.project)
    s = state(d)
    b = load_json(hs_dir(d) / "brief.json")
    print(f"#{s.get('number')} {s.get('title')}: {s.get('stage')} (round {s.get('round')}), task {s.get('task', '-')}")
    ups = {u["name"]: u for u in s.get("uploads", [])}
    for e in exports_plan(b):
        u = ups.get(e["name"])
        print(f"  {e['name']:<34} {u['status'] if u else 'to render'}"
              + (f"  ! {'; '.join(u['problems'])}" if u and u.get("problems") else ""))
    for n in s.get("open_notes", []):
        print(f"  note {n.get('at') or '--'}: {n.get('note')}")
    todo = [e for e in exports_plan(b) if e["name"] not in ups]
    if todo:
        print(f"next: render {todo[0]['label']}, then vs hyperscale prep --project {d.name}")
    elif any(u["status"] != "attached" for u in ups.values()):
        print("next: start_brief_upload / vs hyperscale put / finish_brief_upload for the rest")
    else:
        print("all exports are on the brief")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("pull")
    s.add_argument("brief")
    s.add_argument("--project")
    s.add_argument("--brand")
    s.add_argument("--product", help="product name for the ads brief (default: guessed from the script)")
    s.add_argument("--no-task", action="store_true")
    s.add_argument("--force", action="store_true", help="rewrite work/brief.json")
    s = sub.add_parser("notes")
    s.add_argument("brief")
    s.add_argument("--project", required=True)
    for name in ("shots", "status"):
        sub.add_parser(name).add_argument("--project", required=True)
    s = sub.add_parser("prep")
    s.add_argument("--project", required=True)
    s.add_argument("--file", action="append", help="HOOK=path, e.g. H1=out/final_h1.mp4")
    s.add_argument("--ending", help="bf or evergreen when the brief has two endings")
    s.add_argument("--version", type=int)
    s = sub.add_parser("put")
    s.add_argument("key")
    s.add_argument("--project", required=True)
    s.add_argument("--url", required=True)
    s.add_argument("--upload-id")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("done")
    s.add_argument("key")
    s.add_argument("--project", required=True)
    s.add_argument("--upload-id")
    s.add_argument("--note")
    a = ap.parse_args()
    if a.cmd == "pull" and not shutil.which("ffmpeg"):
        print("warning: ffmpeg not found (vs setup)", file=sys.stderr)
    {"pull": cmd_pull, "notes": cmd_notes, "shots": cmd_shots, "prep": cmd_prep, "put": cmd_put, "done": cmd_done,
     "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    main()
