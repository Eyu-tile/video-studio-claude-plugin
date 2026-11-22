#!/usr/bin/env python3
"""Revisions in two commands: find the exact place each note means, then render, check and show only that.

  vs fix <project> "1:12 cut this pause shorter" ["0:40 typo in the title" ...] [--video out/x.mp4] [--by client]
      Logs the notes against the render they were given on (the latest one unless --video), and prints for each
      timed note everything at that moment and nothing else: the shots there with their EDL index, every word with
      its time, every pause and filler with the exact `vs edl cut` command, texts/sfx there, and a frame sheet.
      Notes about the whole video are listed as such (no single window).

  (change only those EDL entries with `vs edl ...`)

  vs fix <project> --render [--how "shortened the pause at 1:12"]
      Remakes the captions with the same settings (if the render had them), re-renders with --since the reviewed
      version (only the shots around each change are re-encoded, the rest is copied, the sound remixed), checks the
      picture only around the notes plus the whole sound (and the client's lessons), and makes a before/after sheet
      per note. With --how the notes are marked done; otherwise look at the sheets and run `vs notes done`.

<project> is a folder or a name under <workspace>/projects/. Files: <project>/work/edl.json, work/notes.json.
"""
import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, fmt_ts, load_json  # noqa: E402

TOOLS = Path(__file__).parent
VS = TOOLS.parent / "bin" / "vs"


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    except OSError:
        root = ""
    return Path(root or os.getcwd()) / "video-studio"


def project_dir(p):
    cand = [Path(p), workspace() / "projects" / p]
    d = next((c for c in cand if (c / "work").is_dir()), None)
    if not d:
        die(f"no project {p!r} (a folder with work/, or a name under {workspace() / 'projects'})")
    return d.resolve()


def rel(p):
    """A path as short as it can be from here (output an agent reads, and copies into the next command)."""
    r = os.path.relpath(p)
    return r if not r.startswith("..") else str(p)


def latest_render(pd):
    ms = sorted((pd / "out").glob("**/*.mp4.render.json"), key=lambda m: m.stat().st_mtime)
    for m in reversed(ms):
        v = Path(str(m)[: -len(".render.json")])
        if v.exists():
            return v
    return None


def vs(*args, cwd=None, check=True):
    p = subprocess.run([str(VS), *map(str, args)], capture_output=True, text=True, cwd=cwd)
    if check and p.returncode != 0:
        die(f"vs {' '.join(map(str, args[:2]))} failed:\n{p.stdout[-1500:]}{p.stderr[-1500:]}")
    return p


def opt(argv, name):
    if name in argv:
        i = argv.index(name)
        return argv[i + 1] if i + 1 < len(argv) else None
    for x in argv:
        if x.startswith(name + "="):
            return x.split("=", 1)[1]
    return None


def without(argv, name):
    out, skip = [], False
    for x in argv:
        if skip:
            skip = False
            continue
        if x == name:
            skip = True
            continue
        if x.startswith(name + "="):
            continue
        out.append(x)
    return out


def next_name(video):
    v = Path(video)
    m = re.match(r"(.*)_v(\d+)$", v.stem)
    base, n = (m.group(1), int(m.group(2)) + 1) if m else (v.stem, 2)
    while (v.parent / f"{base}_v{n}{v.suffix}").exists():
        n += 1
    return v.parent / f"{base}_v{n}{v.suffix}"


def windows(note, pad=2.0):
    t0 = min(x for x, _ in note["at"])
    t1 = max((y if y is not None else x) for x, y in note["at"])
    return max(0.0, t0 - pad), t1 + pad


# --------------------------------------------------------------------------------------------

def cmd_notes(a, pd):
    edl = Path(rel(Path(a.edl).resolve() if a.edl else pd / "work" / "edl.json"))
    notes = Path(rel(pd / "work" / "notes.json"))
    video = Path(a.video).resolve() if a.video else latest_render(pd)
    if not video:
        die(f"no render with a .render.json in {pd / 'out'}: pass --video <the version that was reviewed>")
    before = load_json(notes)["notes"] if notes.exists() else []
    args = ["notes", "add", notes, "--edl", edl, "--video", video] + (["--by", a.by] if a.by else [])
    for t in a.notes:
        args += ["--text", t]
    out = vs(*args).stdout
    for line in out.splitlines():
        if line.startswith("REPEAT"):
            print(line)
    new = [n for n in load_json(notes)["notes"] if n["id"] > max((b["id"] for b in before), default=0)]
    print(f"Reviewed version: {video.name}. Fix ONLY what each note asks; change only the entries listed.\n")
    for n in new:
        if not n.get("at"):
            print(f"== note {n['id']}: {n['text']}\n   about the whole video (no single moment): handle it with the normal "
                  "steps (a global setting, music, grade...); `vs fix --render` still renders it.\n")
            continue
        vs("notes", "focus", notes, n["id"], "--video", video, "--edl", edl)
        md = (notes.parent / "focus" / f"note-{n['id']}" / "focus.md").read_text(encoding="utf-8")
        md = md.split("\n## Next", 1)[0].rstrip()
        md = md.replace("Fix only what this note asks. Do not re-plan, re-transcribe or re-review the whole video.\n", "")
        print(f"== {md.lstrip('# ')}\n")
    print(f"Next: change those entries with `vs edl ... {edl}`, then `vs fix {a.project} --render "
          "[--how \"what you changed\"]`.")


def cmd_render(a, pd):
    t_start = time.time()
    notes_p = pd / "work" / "notes.json"
    if not notes_p.exists():
        die("no notes: `vs fix <project> \"<time> <note>\"` first")
    book = load_json(notes_p)
    open_ = [n for n in book["notes"] if n["status"] == "open"]
    if a.ids:
        want = {int(x) for x in a.ids.split(",")}
        open_ = [n for n in book["notes"] if n["id"] in want]
    if not open_:
        die("no open notes (vs notes list --all to see them)")
    prev = Path(open_[-1].get("video") or "")
    if not prev.exists():
        prev = latest_render(pd)
    man_p = Path(str(prev) + ".render.json")
    if not prev or not man_p.exists():
        die(f"the reviewed render {prev} has no .render.json; render it once with `vs render` first")
    man = load_json(man_p)
    rargs = man.get("args")
    if not rargs:
        die(f"{man_p.name} predates `vs fix`: run the render command once more by hand with --since {prev}")
    argv, cwd = list(rargs["argv"]), rargs["cwd"]
    edl = Path(cwd, argv[0]).resolve()
    steps = []
    # 1. captions, same look, new timing
    cap = opt(argv, "--captions")
    if cap:
        side = Path(cwd, cap).with_suffix(".captions.json")
        if side.exists():
            c = load_json(side)
            t = time.time()
            vs("captions", *c["argv"], cwd=c["cwd"])
            steps.append(f"captions remade ({time.time() - t:.1f} s)")
        else:
            steps.append("captions kept as they are (made before `vs fix`; remake them by hand if timing changed)")
    # 2. render only what changed
    nxt = next_name(prev)
    argv = without(without(without(argv, "-o"), "--out"), "--since")
    t = time.time()
    p = vs("render", *argv, "-o", nxt, "--since", prev, cwd=cwd)
    msg = next((ln for ln in p.stdout.splitlines() if ln.startswith("rendered")), p.stdout.strip()[-300:])
    fell = [ln for ln in p.stderr.splitlines() if ln.startswith("--since") or "splice check failed" in ln]
    steps.append(f"render {time.time() - t:.1f} s: {msg.split(': ', 1)[-1]}" + (f" [{fell[0]}]" if fell else ""))
    # 3. check: picture around the notes, sound whole, lessons
    timed = [n for n in open_ if n.get("at")]
    qargs = ["qa", nxt, "--edl", edl]
    preset = opt(argv, "--preset")
    if preset:
        qargs += ["--preset", preset]
    if cap:
        qargs += ["--captions", Path(cwd, cap).resolve()]
    if timed and not any(not n.get("at") for n in open_):
        for n in timed:
            lo, hi = windows(n)
            qargs += ["--window", f"{lo:.2f}-{hi:.2f}"]
    t = time.time()
    q = vs(*qargs, check=False)
    bad = [ln for ln in q.stdout.splitlines() if ln.startswith(("FAIL", "WARN"))]
    steps.append(f"QA {time.time() - t:.1f} s: " + ("all pass" if not bad else f"{len(bad)} to look at"))
    # 4. before/after per note
    sheets = []
    for n in timed:
        vs("notes", "focus", notes_p, n["id"], "--video", nxt, "--before", prev, "--edl", edl)
        sheets.append((n, notes_p.parent / "focus" / f"note-{n['id']}" / "frames.png"))
    if a.how:
        vs("notes", "done", notes_p, *[n["id"] for n in open_], "--how", a.how)
    print(f"{rel(nxt)} ({time.time() - t_start:.1f} s in all)")
    for s_ in steps:
        print(f"  - {s_}")
    for ln in bad:
        print(f"  {ln}")
    for n, sh in sheets:
        lo, hi = windows(n)
        print(f"  note {n['id']} ({fmt_ts(lo)[1:]}-{fmt_ts(hi)[1:]}): before/after {rel(sh)}")
    if a.how:
        print(f"  notes {', '.join(str(n['id']) for n in open_)} marked done")
    else:
        print(f"Look at each sheet (top row before, bottom after), then `vs notes done {notes_p} <ids> --how \"...\"`.")
    if q.returncode != 0:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project")
    ap.add_argument("notes", nargs="*", help="notes with times, e.g. \"1:12 cut this pause shorter\"")
    ap.add_argument("--video", help="the version that was reviewed (default: the latest render)")
    ap.add_argument("--edl", help="default: <project>/work/edl.json")
    ap.add_argument("--by", help="who gave the notes")
    ap.add_argument("--render", action="store_true", help="render, check and show the fixes")
    ap.add_argument("--how", help="with --render: mark the notes done with this")
    ap.add_argument("--ids", help="with --render: only these notes (default: every open one)")
    a = ap.parse_args()
    pd = project_dir(a.project)
    if a.render:
        cmd_render(a, pd)
    elif a.notes:
        cmd_notes(a, pd)
    else:
        os.execv(str(VS), [str(VS), "notes", "list", str(pd / "work" / "notes.json")])


if __name__ == "__main__":
    main()
