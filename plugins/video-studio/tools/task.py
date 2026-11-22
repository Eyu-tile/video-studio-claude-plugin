#!/usr/bin/env python3
"""Task history by code: deliveries, client feedback, and picking up exactly where you left off.

Each client task (an ad, a cut, a version set) gets a code, e.g. TC0488. Its history lives in
<workspace>/history/<CODE>.json and <CODE>.md (small text, committed with the workspace, so it survives
cloud sessions and new machines). Every delivery snapshots the edit's inputs (script, shot list, EDLs,
builder, project.md) into history/<CODE>/vN/ so a later session can rebuild or change exactly that version.

  vs task new TC0488 --project capturecards-tc0488 --client TrueClean --title "Scale & awareness 1"
  vs task deliver TC0488 --file out/final/ad.mp4 [--file ...] [--link URL] --note "v2: real people"
  vs task feedback TC0488 "client: make the hook faster"       (or --file comments.txt; timestamps map via vs notes)
  vs task resume TC0488            briefing: brief, versions, open feedback, files, next step
  vs task done TC0488 3 --how "cut the first 2 shots"           mark feedback #3 handled
  vs task note TC0488 "decision: keep the 84% chip"             decisions and context worth keeping
  vs task restore TC0488 [--version v2]   put a version's snapshot back into the project (fresh machine)
  vs task list [--client X] [--open]
  vs task close TC0488 | reopen TC0488
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
from vs_common import die, load_json, save_json  # noqa: E402

CODE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,40}")
SNAP_GLOBS = ["project.md", "NOTES.md", "work/*.json", "work/*.py", "work/*.sh", "work/*.ass", "work/*.srt",
              "work/notes.json", "assets/credits.json", "assets/CREDITS.md"]
SNAP_MAX = 3_000_000  # bytes per file


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


def hist_dir():
    return workspace() / "history"


def tpath(code):
    if not CODE.fullmatch(code):
        die("task code: letters, digits, '.', '_' or '-' (e.g. TC0488)")
    return hist_dir() / f"{code.upper()}.json"


def load(code):
    p = tpath(code)
    if not p.exists():
        known = sorted(x.stem for x in hist_dir().glob("*.json")) if hist_dir().exists() else []
        die(f"no task {code.upper()}. Known: {', '.join(known) or 'none'} (start one: vs task new {code.upper()})")
    return load_json(p)


def proj_dir(t):
    return workspace() / "projects" / t["project"] if t.get("project") else None


def save(t):
    t["updated"] = now()
    save_json(tpath(t["code"]), t)
    (hist_dir() / f"{t['code']}.md").write_text(render_md(t))


def open_feedback(t):
    return [f for f in t["feedback"] if f["status"] == "open"]


def render_md(t):
    L = [f"# {t['code']}: {t.get('title') or ''}".rstrip(": "), "",
         f"- Client: {t.get('client') or '-'}", f"- Project folder: `projects/{t.get('project') or '-'}`",
         f"- Status: **{t['status']}**  (created {t['created']}, updated {t.get('updated', t['created'])})"]
    if t.get("brief"):
        L += ["", "## Brief", t["brief"]]
    L += ["", "## Versions"]
    for v in t["versions"] or []:
        L.append(f"- **{v['version']}** {v['date']}: {v.get('note') or ''}")
        for f in v["files"]:
            L.append(f"  - `{f['path']}` ({f.get('duration') or '?'} s, sha256 {f['sha256'][:12]})")
        if v.get("link"):
            L.append(f"  - link: {v['link']}")
        L.append(f"  - snapshot: `history/{t['code']}/{v['version']}/`")
    if not t["versions"]:
        L.append("- none yet")
    L += ["", "## Client feedback"]
    for f in t["feedback"] or []:
        mark = "x" if f["status"] == "done" else ("-" if f["status"] == "skipped" else " ")
        how = f" → {f['how']}" if f.get("how") else ""
        L.append(f"- [{mark}] #{f['id']} ({f['date']}, on {f.get('on') or '-'}) {f['text']}{how}")
    if not t["feedback"]:
        L.append("- none yet")
    if t["notes"]:
        L += ["", "## Notes and decisions"] + [f"- {n['date']}: {n['text']}" for n in t["notes"]]
    return "\n".join(L) + "\n"


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def duration(p):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        return round(float(out), 2)
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None


def snapshot(t, version):
    pd = proj_dir(t)
    dest = hist_dir() / t["code"] / version
    n = 0
    if pd and pd.exists():
        for g in SNAP_GLOBS:
            for f in pd.glob(g):
                if f.is_file() and f.stat().st_size <= SNAP_MAX:
                    rel = f.relative_to(pd)
                    (dest / rel).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, dest / rel)
                    n += 1
    return n


def cmd_new(a):
    p = tpath(a.code)
    if p.exists() and not a.force:
        die(f"{a.code.upper()} already exists: vs task resume {a.code.upper()}")
    brief = Path(a.brief).read_text() if a.brief and Path(a.brief).exists() else (a.brief or "")
    t = {"code": a.code.upper(), "title": a.title, "client": a.client, "project": a.project, "brief": brief.strip(),
         "status": "in progress", "created": now(), "versions": [], "feedback": [], "notes": []}
    save(t)
    pd = proj_dir(t)
    if pd and (pd / "project.md").exists() and t["code"] not in (pd / "project.md").read_text():
        with open(pd / "project.md", "a") as fh:
            fh.write(f"\n## Task\n- Code: {t['code']} (history: `vs task resume {t['code']}`)\n")
    print(f"task {t['code']} started -> {p}")


def cmd_deliver(a):
    t = load(a.code)
    files = []
    pd = proj_dir(t)
    for f in a.file or []:
        fp = Path(f)
        if not fp.exists() and pd and (pd / f).exists():
            fp = pd / f
        if not fp.exists():
            die(f"file not found: {f}")
        rel = os.path.relpath(fp.resolve(), pd.resolve()) if pd and pd.exists() else str(fp)
        files.append({"path": rel, "bytes": fp.stat().st_size, "sha256": sha256(fp), "duration": duration(fp)})
    if not files and not a.link:
        die("give the delivered --file(s) and/or a --link")
    version = a.version or f"v{len(t['versions']) + 1}"
    if any(v["version"] == version for v in t["versions"]):
        die(f"{version} already delivered; pick another --version")
    n = snapshot(t, version)
    t["versions"].append({"version": version, "date": now(), "note": a.note, "link": a.link, "files": files,
                          "snapshot_files": n})
    for f in open_feedback(t):  # feedback answered by this delivery stays open until marked done
        f.setdefault("seen_in", version)
    t["status"] = "delivered"
    save(t)
    print(f"{t['code']} {version} delivered: {len(files)} file(s), {n} edit files snapshotted -> "
          f"history/{t['code']}/{version}/")
    left = open_feedback(t)
    if left:
        print(f"still open: {len(left)} feedback item(s); mark handled ones: vs task done {t['code']} <#> --how ...")
    offers = []
    if files and pref("review_page") != "never":
        offers.append(f"a review page for comments (/video-review: vs present {files[0]['path']} "
                      f"--project {t.get('project') or '<P>'} --task {t['code']} --version {version})")
    if files and pref("social_post") != "never":
        offers.append("posting to social media (/social-post; nothing posts without approving the plan)")
    if offers:
        print("next: ask the person, in one question set, about " + " and ".join(offers))


def pref(key):
    f = workspace() / "settings.json"
    try:
        return load_json(f).get(key, "ask") if f.exists() else "ask"
    except (OSError, ValueError, SystemExit):
        return "ask"


def cmd_feedback(a):
    t = load(a.code)
    text = Path(a.file).read_text() if a.file else (a.text or sys.stdin.read())
    items = [x.strip() for x in (text.splitlines() if a.split else [text]) if x.strip()]
    if not items:
        die("empty feedback")
    on = a.on or (t["versions"][-1]["version"] if t["versions"] else None)
    start = len(t["feedback"])
    for i, x in enumerate(items):
        t["feedback"].append({"id": start + i + 1, "date": now(), "on": on, "from": a.who, "text": x,
                              "status": "open"})
    t["status"] = "revising"
    save(t)
    print(f"{t['code']}: {len(items)} feedback item(s) on {on or '-'} logged (#{start + 1}–#{start + len(items)})")
    if t.get("client"):
        import lessons
        new = [{"id": f["id"], "text": f["text"]} for f in t["feedback"][start:]]
        for n, les, scope in lessons.record_notes(t["client"], new, t.get("project"), f"task {t['code']}"):
            print(f"REPEAT: feedback #{n['id']} is something we already learned ({scope} {les['id']}: "
                  f"{les['rule']}). Fix it and tighten the lesson (a --check, or --must).")
    pd = proj_dir(t)
    edl = pd / "work" / "edl.json" if pd else None
    if any(re.search(r"\b\d{1,2}:\d{2}\b", x) for x in items):
        print("Timestamped notes: map them onto shots with "
              f"`vs notes add {pd / 'work' / 'notes.json' if pd else 'work/notes.json'} --edl "
              f"{edl if edl and edl.exists() else '<the EDL that version was rendered from>'} <notes>`")


def cmd_done(a):
    t = load(a.code)
    for f in t["feedback"]:
        if f["id"] == a.id:
            f["status"] = "skipped" if a.skip else "done"
            f["how"] = a.how or a.skip
            f["closed"] = now()
            break
    else:
        die(f"no feedback #{a.id} in {t['code']}")
    save(t)
    print(f"{t['code']} #{a.id} {'skipped' if a.skip else 'done'}; {len(open_feedback(t))} still open")


def cmd_note(a):
    t = load(a.code)
    t["notes"].append({"date": now(), "text": a.text})
    save(t)
    print(f"{t['code']}: note saved")


def cmd_resume(a):
    t = load(a.code)
    pd = proj_dir(t)
    last = t["versions"][-1] if t["versions"] else None
    print(f"=== {t['code']}: {t.get('title') or ''} | client {t.get('client') or '-'} | {t['status']} ===")
    if t.get("brief"):
        b = t["brief"]
        print("Brief:", b if len(b) < 700 else b[:700] + " … (full brief: history/" + t["code"] + ".md)")
    print(f"Versions: {', '.join(v['version'] + ' ' + v['date'][:10] for v in t['versions']) or 'none delivered'}")
    if last:
        print(f"Last delivered {last['version']} ({last['date']}): {last.get('note') or ''}")
        for f in last["files"]:
            here = pd and (pd / f["path"]).exists()
            print(f"  {f['path']} {'(on disk)' if here else '(not on this machine)'}")
    of = open_feedback(t)
    print(f"Open client feedback ({len(of)}):" if of else "Open client feedback: none")
    for f in of:
        print(f"  #{f['id']} on {f.get('on') or '-'} ({f['date']}): {f['text']}")
    if t["notes"]:
        print("Notes and decisions:")
        for n in t["notes"][-8:]:
            print(f"  {n['date'][:10]}: {n['text']}")
    if pd and (pd / "work" / "notes.json").exists():
        nn = load_json(pd / "work" / "notes.json")
        todo = [n for n in nn.get("notes", []) if n.get("status", "open") == "open"]
        if todo:
            print(f"Timestamped review notes still open: {len(todo)} (vs notes list {pd / 'work' / 'notes.json'})")
    print("Read first:", ", ".join(x for x in [
        f"history/{t['code']}.md",
        f"projects/{t['project']}/project.md" if pd and (pd / "project.md").exists() else None,
        f"projects/{t['project']}/NOTES.md" if pd and (pd / "NOTES.md").exists() else None] if x))
    if pd and not pd.exists():
        snap = f" --version {last['version']}" if last else ""
        print(f"Project folder is not on this machine: `vs task restore {t['code']}{snap}` brings back the edit files;"
              " re-fetch footage/renders listed in them.")
    nxt = ("work through the open feedback (newest version first), render the next version, then "
           f"`vs task deliver {t['code']} --file ... --note ...` and mark items with `vs task done`") if of else (
        "no open feedback: wait for the client, or log their comments with "
        f"`vs task feedback {t['code']} \"...\"`")
    print("Next:", nxt)


def cmd_restore(a):
    t = load(a.code)
    if not t["versions"]:
        die("nothing delivered yet, so there is no snapshot to restore")
    v = a.version or t["versions"][-1]["version"]
    src = hist_dir() / t["code"] / v
    if not src.exists():
        die(f"no snapshot for {v}")
    pd = proj_dir(t) or die("task has no project folder")
    n = 0
    for f in src.rglob("*"):
        if f.is_file():
            d = pd / f.relative_to(src)
            if d.exists() and not a.force:
                continue
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, d)
            n += 1
    print(f"restored {n} file(s) of {t['code']} {v} into {pd} (existing files kept; --force overwrites)")


def cmd_list(a):
    if not hist_dir().exists():
        print("no tasks yet: vs task new <CODE> --project <folder> --client <name> --title <title>")
        return
    rows = [load_json(p) for p in sorted(hist_dir().glob("*.json"))]
    for t in rows:
        if a.client and (t.get("client") or "").lower() != a.client.lower():
            continue
        if a.open and t["status"] == "closed":
            continue
        last = t["versions"][-1]["version"] if t["versions"] else "-"
        print(f"{t['code']:<10} {t['status']:<12} {last:<4} open fb {len(open_feedback(t)):<2} "
              f"{(t.get('client') or '-')[:14]:<14} {t.get('title') or ''}")


def cmd_status(a, status):
    t = load(a.code)
    t["status"] = status
    save(t)
    print(f"{t['code']}: {status}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("new")
    s.add_argument("code")
    s.add_argument("--project", help="folder name under projects/")
    s.add_argument("--client")
    s.add_argument("--title")
    s.add_argument("--brief", help="brief text or a file with it")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("deliver")
    s.add_argument("code")
    s.add_argument("--file", action="append")
    s.add_argument("--link", help="where the client got it (Drive, Frame.io, ...)")
    s.add_argument("--note", help="what this version changed")
    s.add_argument("--version")
    s = sub.add_parser("feedback")
    s.add_argument("code")
    s.add_argument("text", nargs="?")
    s.add_argument("--file")
    s.add_argument("--on", help="version it is about (default: last delivered)")
    s.add_argument("--who", help="who said it")
    s.add_argument("--split", action="store_true", help="one item per line")
    s = sub.add_parser("done")
    s.add_argument("code")
    s.add_argument("id", type=int)
    s.add_argument("--how")
    s.add_argument("--skip", help="not done, and why")
    s = sub.add_parser("note")
    s.add_argument("code")
    s.add_argument("text")
    for name in ("resume", "close", "reopen"):
        s = sub.add_parser(name)
        s.add_argument("code")
    s = sub.add_parser("restore")
    s.add_argument("code")
    s.add_argument("--version")
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("list")
    s.add_argument("--client")
    s.add_argument("--open", action="store_true")
    a = ap.parse_args()
    if a.cmd == "close":
        return cmd_status(a, "closed")
    if a.cmd == "reopen":
        return cmd_status(a, "in progress")
    {"new": cmd_new, "deliver": cmd_deliver, "feedback": cmd_feedback, "done": cmd_done, "note": cmd_note,
     "resume": cmd_resume, "restore": cmd_restore, "list": cmd_list}[a.cmd](a)


if __name__ == "__main__":
    main()
