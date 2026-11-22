#!/usr/bin/env python3
"""Present a finished video for review in a Frame.io-style page: player with frame-accurate timecode, a filmstrip
timeline with comment pins, and a comment thread (pinned to a frame or a range, replies, resolve). Comments come
back as `vs notes` lines, so review feedback flows straight into the revision checklist.

  vs present out/final.mp4 --project launch [--task TC0488] [--version v2] [--title "Launch reel"]
        -> out/review/<version>/: index.html (the page), video.mp4 (browser proxy, <= 14 MB), strip.jpg, poster.jpg,
           local.html (open in any browser; comments stay in that browser, Export CSV sends them), publish.json
           (what Claude passes to the Artifact tool: published on claude.ai, comments are shared and live, and
           Claude reads them back)
  vs present notes <comments.json|comments.csv> [--all] [-o notes.txt]   comments -> "0:12.40 text" lines (vs notes)
  vs present link <review dir> <url>          remember the published link (and on the task's latest version)
  vs present pref [ask|always|never]          whether Claude offers the review page after each finished task
"""
import argparse
import csv
import hashlib
import html
import io
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, need, probe, run, save_json  # noqa: E402

TEMPLATE = Path(__file__).parent / "templates" / "review.html"
PUBLISH_FILE_LIMIT_MB = 15     # Artifact tool: each binary file published beside the page
CAPABILITIES = {"db": {}, "user": {"scopes": ["profile"]}, "downloads": True}


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(top.stdout.strip() if top.returncode == 0 else os.getcwd()) / "video-studio"


def slug(s, n=40):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n] or "review"


def mmss(t):
    m, s = divmod(int(round(t)), 60)
    return f"{m}:{s:02d}"


def proxy(src, dest, dur, max_mb, has_audio):
    """H.264/AAC MP4 every browser plays, long side <= 1280, keyframe every second (quick, exact seeking), moov first.
    Bitrate sized so the file stays under max_mb; one smaller retry if the encoder overshoots."""
    audio_k = 128 if has_audio else 0
    for attempt, factor in enumerate((0.92, 0.75)):
        total_k = max_mb * 8 * 1024 * factor / max(dur, 1)
        v_k = int(max(250, min(5000, total_k - audio_k)))
        long_side = 1280 if v_k >= 1200 else 960 if v_k >= 600 else 640
        vf = (f"scale='if(gt(iw,ih),min({long_side},iw),-2)':'if(gt(iw,ih),-2,min({long_side},ih))',"
              "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p")
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(src), "-map", "0:v:0", "-vf", vf, "-c:v", "libx264", "-preset",
               "veryfast",  # a review copy: veryfast halves the wait; the bitrate cap still holds the size "-b:v", f"{v_k}k", "-maxrate", f"{int(v_k * 1.5)}k", "-bufsize", f"{v_k * 2}k",
               "-force_key_frames", "expr:gte(t,n_forced*1)", "-movflags", "+faststart"]
        cmd += ["-map", "0:a:0", "-c:a", "aac", "-b:a", f"{audio_k}k", "-ac", "2"] if has_audio else ["-an"]
        run(cmd + [str(dest)])
        mb = dest.stat().st_size / 1048576
        if mb <= max_mb:
            return {"video_kbps": v_k, "long_side": long_side, "mb": round(mb, 2)}
    die(f"could not fit the review video under {max_mb} MB ({mb:.1f} MB at {v_k} kbps); "
        "for long videos present a shorter part (--section a-b) or several parts")


def strip(src, dest, dur, width, height):
    """Timeline filmstrip: up to 60 thumbnails, 90 px high, in a 10-column sprite."""
    count = int(max(8, min(60, round(dur * 2))))
    interval = dur / count
    th = 90
    tw = max(2, int(round(th * width / height / 2)) * 2)
    cols = min(10, count)
    rows = math.ceil(count / cols)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf",
         f"fps=1/{interval:.4f},scale={tw}:{th},tile={cols}x{rows}", "-frames:v", "1", "-q:v", "5", str(dest)])
    return {"src": dest.name, "w": tw, "h": th, "cols": cols, "count": count, "interval": round(interval, 4)}


def cmd_make(a):
    need("ffmpeg")
    src = Path(a.video)
    if not src.exists():
        die(f"video not found: {src}")
    info = probe(str(src))
    dur = float(info["duration"] or 0)
    if dur <= 0:
        die(f"{src} has no duration")
    if a.section:
        t0, _, t1 = a.section.partition("-")
        t0, t1 = float(t0), float(t1)
        cut = Path(a.out or ".") / "_section.mp4" if a.out else src.with_name(src.stem + "_section.mp4")
        run(["ffmpeg", "-y", "-v", "error", "-ss", str(t0), "-i", str(src), "-t", str(t1 - t0), "-c:v", "libx264",
             "-crf", "18", "-c:a", "aac", str(cut)])
        src, dur = cut, t1 - t0
    proj = workspace() / "projects" / a.project if a.project else None
    if proj and not proj.exists():
        die(f"project {a.project} not found")
    version = a.version or "v1"
    out = Path(a.out) if a.out else (proj / "out" / "review" / version if proj else src.with_name(f"{src.stem}_review"))
    out.mkdir(parents=True, exist_ok=True)
    print(f"encoding review copy of {src.name} ({dur:.1f} s)...")
    enc = proxy(src, out / "video.mp4", dur, a.max_mb, info.get("has_audio"))
    vi = probe(str(out / "video.mp4"))
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{min(1.0, dur / 4):.2f}", "-i", str(out / "video.mp4"), "-frames:v", "1",
         "-q:v", "4", str(out / "poster.jpg")])
    st = strip(out / "video.mp4", out / "strip.jpg", dur, vi["width"], vi["height"])
    title = a.title or (a.project.replace("-", " ").title() if a.project else src.stem.replace("_", " "))
    cfg = {"id": f"{slug(title)}-{version}-{hashlib.sha1(str(src.resolve()).encode()).hexdigest()[:8]}",
           "slug": slug(title), "title": title, "version": version, "client": a.client, "task": a.task,
           "fps": round(float(info.get("fps") or 25), 3), "duration": round(dur, 3), "length": mmss(dur),
           "video": "video.mp4", "poster": "poster.jpg", "strip": st}
    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("__TITLE__", html.escape(f"{title} {version}"), 1)
    page = page.replace("__CONFIG__", json.dumps(cfg).replace("</", "<\\/"), 1)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "local.html").write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
                                    'content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
                                    + page + "</body></html>\n", encoding="utf-8")
    publish = {"file_path": str((out / "index.html").resolve()),
               "files": {n: str((out / n).resolve()) for n in ("video.mp4", "strip.jpg", "poster.jpg")},
               "capabilities": CAPABILITIES, "icon": "video",
               "description": f"Review {title} {version}: play it frame by frame and leave comments pinned to a moment.",
               "title": f"{title} {version}", "config": cfg, "url": None}
    save_json(out / "publish.json", publish)
    print(f"review page -> {out}/ (video {enc['mb']} MB at {enc['video_kbps']} kbps, {vi['width']}x{vi['height']}, "
          f"{st['count']} filmstrip frames)")
    print(f"  on claude.ai: publish index.html with the Artifact tool using {out / 'publish.json'} "
          "(file_path, files, capabilities, icon, description): comments are shared, live, and readable by Claude")
    print(f"  anywhere else: open {out / 'local.html'} in a browser; comments stay in that browser, Export CSV sends them")


def rows_from(path):
    """Comment rows from the page's db (ArtifactData list output, any common shape) or its exported CSV."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if p.suffix.lower() == ".csv" or text.lstrip().startswith("#,"):
        out = []
        for r in csv.DictReader(io.StringIO(text)):
            t = r.get("Time") or r.get("Timecode") or ""
            out.append({"t_text": t, "te_text": r.get("End") or "", "text": r.get("Comment") or "",
                        "resolved": (r.get("Status") or "").lower() in ("completed", "resolved", "done"),
                        "who": r.get("Commenter") or "", "replies": r.get("Replies") or ""})
        return out
    data = json.loads(text)
    if isinstance(data, dict):
        data = data.get("documents") or data.get("docs") or data.get("items") or data.get("results") or list(data.values())
    docs = []
    for d in data if isinstance(data, list) else []:
        body = d.get("data") if isinstance(d.get("data"), dict) else d
        doc_id = d.get("id") or (d.get("path") or "").rsplit("/", 1)[-1] or body.get("id")
        docs.append(dict(body, id=doc_id))
    tops = [d for d in docs if not d.get("parent")]
    out = []
    for c in sorted(tops, key=lambda c: (c.get("t") is None, c.get("t") or 0)):
        reps = [r.get("text", "") for r in sorted((r for r in docs if r.get("parent") == c["id"]),
                                                 key=lambda r: r.get("created") or 0)]
        out.append({"t": c.get("t"), "te": c.get("te"), "text": c.get("text", ""), "resolved": bool(c.get("resolved")),
                    "who": c.get("byName") or "", "replies": " / ".join(reps)})
    return out


def short(t):
    m = int(t // 60)
    return f"{m}:{t - m * 60:05.2f}"


def cmd_notes(a):
    lines = []
    for r in rows_from(a.comments):
        if r["resolved"] and not a.all:
            continue
        if "t" in r:
            at = (short(r["t"]) + (f"-{short(r['te'])}" if isinstance(r.get("te"), (int, float)) else "") + " ") \
                if isinstance(r.get("t"), (int, float)) else ""
        else:
            at = (r["t_text"] + (f"-{r['te_text']}" if r["te_text"] else "") + " ") if r["t_text"] else ""
        extra = f" [replies: {r['replies']}]" if r["replies"] else ""
        lines.append(f"{at}{' '.join(r['text'].split())}{extra}")
    text = "\n".join(lines) + ("\n" if lines else "")
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"{len(lines)} comment(s) -> {a.out}  (next: vs notes add work/notes.json --edl work/edl.json {a.out})")
    else:
        sys.stdout.write(text)


def cmd_link(a):
    d = Path(a.dir)
    pub = d / "publish.json"
    if not pub.exists():
        die(f"{pub} not found (run vs present <video> first)")
    data = load_json(pub)
    data["url"] = a.url
    save_json(pub, data)
    code = (data.get("config") or {}).get("task")
    if code:
        import task  # noqa: E402
        t = task.load(code)
        if t["versions"]:
            t["versions"][-1]["review"] = a.url
            task.save(t)
            print(f"{code} {t['versions'][-1]['version']}: review page {a.url}")
    print(f"review link saved in {pub}")


PREF_KEY = "review_page"


def cmd_pref(a):
    f = workspace() / "settings.json"
    data = load_json(f) if f.exists() else {}
    if a.value:
        data[PREF_KEY] = a.value
        save_json(f, data)
    print(data.get(PREF_KEY, "ask"))


def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ("notes", "link", "pref", "-h", "--help"):
        sys.argv.insert(1, "make")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("video")
    m.add_argument("--project")
    m.add_argument("--task", help="client task code (vs task): shown on the page; vs present link records the URL")
    m.add_argument("--version", help="v1, v2 ... (default v1; use the delivered version)")
    m.add_argument("--title")
    m.add_argument("--client")
    m.add_argument("--section", help="only part of a long video, seconds: 0-90")
    m.add_argument("--max-mb", type=float, default=14.0, help=f"review copy size cap (publish limit {PUBLISH_FILE_LIMIT_MB} MB)")
    m.add_argument("-o", "--out", help="output folder")
    n = sub.add_parser("notes")
    n.add_argument("comments", help="the page's comments: ArtifactData list JSON, or the CSV from Export")
    n.add_argument("--all", action="store_true", help="include resolved comments")
    n.add_argument("-o", "--out")
    li = sub.add_parser("link")
    li.add_argument("dir")
    li.add_argument("url")
    pr = sub.add_parser("pref")
    pr.add_argument("value", nargs="?", choices=["ask", "always", "never"])
    a = ap.parse_args()
    if a.cmd == "make" and a.max_mb > PUBLISH_FILE_LIMIT_MB:
        die(f"--max-mb must be <= {PUBLISH_FILE_LIMIT_MB} (the Artifact tool's limit per published file)")
    {"make": cmd_make, "notes": cmd_notes, "link": cmd_link, "pref": cmd_pref}[a.cmd](a)


if __name__ == "__main__":
    main()
