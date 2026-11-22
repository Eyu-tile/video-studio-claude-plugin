#!/usr/bin/env python3
"""Get a finished video ready to post on social platforms, check every post against its platform's limits, and log
where it went. The posting itself goes through Composio (`vs setup --social`: the composio skill, then its CLI or
MCP), always after the person approves the exact plan: platform, account, caption, privacy.

  vs social prep out/final.mp4 --project launch --platforms tiktok,reels,shorts [--task TC0488] [--version v2]
        -> out/social/<version>/: one file per platform (H.264/AAC, faststart; re-encoded only when needed),
           cover.jpg, post.json (captions to write, limits, checks) and post_plan.md
  vs social check out/social/v2/post.json     validate captions, hashtags, length, size, aspect; rewrite post_plan.md
  vs social log out/social/v2/post.json tiktok --url https://... [--id 123]   record a published post (and on the task)
  vs social pref [ask|never]                  whether Claude offers posting after each finished task

Limits below are the platforms' published numbers as of 2026-11 (Composio tool docs for Instagram); a platform can
change them, so the live tool schema or error wins.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, need, probe, run, save_json  # noqa: E402

# aspect: what the platform shows best (others are allowed but letterboxed/cropped); dur: seconds (min, max);
# mb: upload size cap we keep under; caption: characters; title: characters; tags: hashtag cap;
# public_url: the API takes a public direct URL, not a file; privacy: our default until the person says otherwise.
PLATFORMS = {
    "tiktok": {"name": "TikTok", "toolkit": "tiktok", "aspect": "9:16", "dur": (3, 600), "mb": 4000, "caption": 2200,
               "title": None, "tags": None, "privacy": "SELF_ONLY",
               "note": "max length per account comes from the creator info query; poll publish status, never re-post"},
    "reels": {"name": "Instagram Reels", "toolkit": "instagram", "aspect": "9:16", "dur": (3, 900), "mb": 100,
              "caption": 2200, "title": None, "tags": 30, "mentions": 20, "public_url": True, "privacy": None,
              "note": "Business or Creator account; the video must be at a public direct URL (not Drive, not a private page)"},
    "shorts": {"name": "YouTube Shorts", "toolkit": "youtube", "aspect": "9:16", "dur": (1, 180), "mb": 256000,
               "caption": 5000, "title": 100, "tags": None, "privacy": "private",
               "note": "title <= 100 characters; privacy private until the person says unlisted or public"},
    "youtube": {"name": "YouTube", "toolkit": "youtube", "aspect": "16:9", "dur": (1, 43200), "mb": 256000,
                "caption": 5000, "title": 100, "tags": None, "privacy": "private",
                "note": "unverified channels are limited to 15 minutes"},
    "linkedin": {"name": "LinkedIn", "toolkit": "linkedin", "aspect": "1:1", "dur": (3, 1800), "mb": 500,
                 "caption": 3000, "title": None, "tags": None, "privacy": "PUBLIC",
                 "note": "upload, wait until the video is AVAILABLE, then post with commentary"},
    "x": {"name": "X", "toolkit": "twitter", "aspect": "16:9", "dur": (1, 140), "mb": 512, "caption": 280,
          "title": None, "tags": None, "privacy": None, "url_len": 23,
          "note": "140 s for standard accounts; every link counts as 23 characters"},
}
ASPECTS = {"9:16": 9 / 16, "16:9": 16 / 9, "1:1": 1.0, "4:5": 0.8}


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(top.stdout.strip() if top.returncode == 0 else os.getcwd()) / "video-studio"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def aspect_name(w, h):
    r = w / h
    return min(ASPECTS, key=lambda k: abs(ASPECTS[k] - r)), r


def needs_encode(info, path):
    """Upload-safe already? H.264 + AAC (or no audio) in an MP4."""
    if path.suffix.lower() != ".mp4":
        return True
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name,pix_fmt", "-of", "json",
                        str(path)], capture_output=True, text=True)
    streams = json.loads(p.stdout or "{}").get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), {})
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)
    return v.get("codec_name") != "h264" or v.get("pix_fmt") not in ("yuv420p", None) or (a and a.get("codec_name") != "aac")


def file_checks(spec, info, path):
    out = []
    dur = float(info["duration"] or 0)
    lo, hi = spec["dur"]
    if dur < lo:
        out.append(f"too short: {dur:.1f} s (min {lo} s)")
    if dur > hi:
        out.append(f"too long: {dur:.0f} s (max {hi} s): cut a version for {spec['name']}")
    got, r = aspect_name(info["width"], info["height"])
    if abs(r - ASPECTS[spec["aspect"]]) > 0.03:
        out.append(f"aspect {info['width']}x{info['height']} ({got}); {spec['name']} shows {spec['aspect']} best: "
                   f"render a {spec['aspect']} version (vs render ... --preset), or set \"accept_aspect\": true "
                   "for this platform in post.json if the person accepts letterboxing")
    mb = path.stat().st_size / 1048576
    if mb > spec["mb"]:
        out.append(f"file {mb:.0f} MB > {spec['mb']} MB")
    return out


def problems(spec, post):
    """File problems (an accepted aspect is not one) plus caption/title/account problems."""
    fp = [x for x in post.get("file_problems") or [] if not (post.get("accept_aspect") and x.startswith("aspect"))]
    return fp + text_checks(spec, post)


def text_checks(spec, post):
    out = []
    cap = post.get("caption") or ""
    if not cap.strip() and spec.get("caption"):
        out.append("caption not written yet")
    n = len(re.sub(r"https?://\S+", "x" * spec["url_len"], cap)) if spec.get("url_len") else len(cap)
    if spec.get("caption") and n > spec["caption"]:
        out.append(f"caption {n} characters > {spec['caption']}")
    tags = re.findall(r"(?<!\w)#\w+", cap)
    if spec.get("tags") and len(tags) > spec["tags"]:
        out.append(f"{len(tags)} hashtags > {spec['tags']}")
    if spec.get("mentions") and len(re.findall(r"(?<!\w)@\w+", cap)) > spec["mentions"]:
        out.append(f"more than {spec['mentions']} @mentions")
    if spec.get("title"):
        t = post.get("title") or ""
        if not t.strip():
            out.append("title not written yet")
        elif len(t) > spec["title"]:
            out.append(f"title {len(t)} characters > {spec['title']}")
    if spec.get("public_url") and not post.get("public_url"):
        out.append("needs a public direct URL to the MP4 (the person's own hosting: S3, R2, Cloudinary...)")
    if not post.get("account"):
        out.append("account to post as not confirmed")
    return out


def write_plan(d, data):
    rows = [f"# Social posts: {data['title']} {data['version']}", "",
            "Nothing is posted until the person approves this table. Composio posts it (vs setup --social).", "",
            "| platform | account | file | length | privacy | caption | checks |", "|---|---|---|---|---|---|---|"]
    for key, p in data["posts"].items():
        spec = PLATFORMS[key]
        cap = (p.get("title") + " / " if p.get("title") else "") + (p.get("caption") or "")
        cap = cap.replace("|", "/").replace("\n", " ")
        cap = cap[:90] + ("…" if len(cap) > 90 else "")
        checks = "; ".join(p.get("problems") or []) or "ok"
        state = f" (posted: {p['posted']['url']})" if p.get("posted") else ""
        rows.append(f"| {spec['name']}{state} | {p.get('account') or '?'} | {Path(p['file']).name} | {p['duration']:.1f} s "
                    f"| {p.get('privacy') or '-'} | {cap or '(to write)'} | {checks} |")
    rows += ["", "Platform notes:"] + [f"- {PLATFORMS[k]['name']}: {PLATFORMS[k]['note']}" for k in data["posts"]]
    (d / "post_plan.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def cmd_prep(a):
    need("ffmpeg")
    src = Path(a.video)
    if not src.exists():
        die(f"video not found: {src}")
    keys = [k.strip().lower() for k in a.platforms.split(",") if k.strip()]
    bad = [k for k in keys if k not in PLATFORMS]
    if bad:
        die(f"unknown platform(s) {', '.join(bad)}; choose from {', '.join(PLATFORMS)}")
    proj = workspace() / "projects" / a.project if a.project else None
    if proj and not proj.exists():
        die(f"project {a.project} not found")
    version = a.version or "v1"
    d = Path(a.out) if a.out else ((proj / "out" / "social" / version) if proj else src.with_name(f"{src.stem}_social"))
    d.mkdir(parents=True, exist_ok=True)
    info = probe(str(src))
    upload = d / f"{src.stem}.mp4"
    if needs_encode(info, src):
        print(f"re-encoding {src.name} to H.264/AAC MP4 for upload...")
        run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-map", "0:v:0", "-map", "0:a:0?", "-c:v", "libx264", "-crf", "18",
             "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(upload)])
    else:
        shutil.copy2(src, upload)
    info = probe(str(upload))
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{min(1.0, float(info['duration']) / 4):.2f}", "-i", str(upload),
         "-frames:v", "1", "-q:v", "3", str(d / "cover.jpg")])
    old = load_json(d / "post.json") if (d / "post.json").exists() else {}
    posts = {}
    for k in keys:
        spec = PLATFORMS[k]
        prev = (old.get("posts") or {}).get(k, {})
        posts[k] = {"platform": spec["name"], "toolkit": spec["toolkit"], "file": str(upload.resolve()),
                    "duration": round(float(info["duration"]), 2), "size": f"{info['width']}x{info['height']}",
                    "caption": prev.get("caption", a.caption or ""), "title": prev.get("title", a.title_text or "")
                    if spec.get("title") else None,
                    "privacy": prev.get("privacy", spec.get("privacy")), "account": prev.get("account"),
                    "public_url": prev.get("public_url"), "posted": prev.get("posted"),
                    "limits": {k2: spec[k2] for k2 in ("dur", "mb", "caption", "title", "tags") if spec.get(k2)}}
        posts[k]["file_problems"] = file_checks(spec, info, upload)
        posts[k]["accept_aspect"] = prev.get("accept_aspect", False)
        posts[k]["problems"] = problems(spec, posts[k])
    data = {"title": a.title or (a.project or src.stem), "version": version, "project": a.project, "task": a.task,
            "source": str(src.resolve()), "cover": str((d / "cover.jpg").resolve()), "posts": posts}
    save_json(d / "post.json", data)
    write_plan(d, data)
    print(f"{len(posts)} post(s) prepared -> {d / 'post.json'}, {d / 'post_plan.md'}")
    for k, p in posts.items():
        fp = [x for x in p["file_problems"] if not (p["accept_aspect"] and x.startswith("aspect"))]
        if fp:
            print(f"  {PLATFORMS[k]['name']}: {'; '.join(fp)}")
    print("next: write captions (and titles) into post.json, confirm the account per platform, vs social check, "
          "then show post_plan.md for approval")


def cmd_check(a):
    f = Path(a.post)
    data = load_json(f)
    total = 0
    for k, p in data["posts"].items():
        spec = PLATFORMS[k]
        p["problems"] = problems(spec, p)
        total += len(p["problems"])
        print(f"{spec['name']}: " + ("; ".join(p["problems"]) if p["problems"] else "ready"))
    save_json(f, data)
    write_plan(f.parent, data)
    print(f"-> {f.parent / 'post_plan.md'}")
    if total:
        sys.exit(1)


def cmd_log(a):
    f = Path(a.post)
    data = load_json(f)
    if a.platform not in data["posts"]:
        die(f"{a.platform} is not in {f} (has: {', '.join(data['posts'])})")
    p = data["posts"][a.platform]
    p["posted"] = {"url": a.url, "id": a.id, "at": now(), "account": p.get("account")}
    save_json(f, data)
    write_plan(f.parent, data)
    if data.get("task"):
        import task  # noqa: E402
        t = task.load(data["task"])
        v = next((x for x in t["versions"] if x["version"] == data["version"]), t["versions"][-1] if t["versions"] else None)
        if v is not None:
            v.setdefault("posts", []).append({"platform": PLATFORMS[a.platform]["name"], "url": a.url, "at": now()})
            task.save(t)
    print(f"{PLATFORMS[a.platform]['name']} post logged: {a.url}")


def cmd_pref(a):
    f = workspace() / "settings.json"
    data = load_json(f) if f.exists() else {}
    if a.value:
        data["social_post"] = a.value
        save_json(f, data)
    print(data.get("social_post", "ask"))


def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ("prep", "check", "log", "pref", "-h", "--help"):
        die("usage: vs social prep|check|log|pref ... (vs social --help)")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prep")
    p.add_argument("video")
    p.add_argument("--platforms", required=True, help="comma list: " + ",".join(PLATFORMS))
    p.add_argument("--project")
    p.add_argument("--task")
    p.add_argument("--version")
    p.add_argument("--title", help="name of the piece (for the plan)")
    p.add_argument("--caption", help="a starting caption for every platform (edit per platform in post.json)")
    p.add_argument("--title-text", help="YouTube title")
    p.add_argument("-o", "--out")
    c = sub.add_parser("check")
    c.add_argument("post")
    lg = sub.add_parser("log")
    lg.add_argument("post")
    lg.add_argument("platform", choices=sorted(PLATFORMS))
    lg.add_argument("--url", required=True)
    lg.add_argument("--id")
    pr = sub.add_parser("pref")
    pr.add_argument("value", nargs="?", choices=["ask", "never"])
    a = ap.parse_args()
    {"prep": cmd_prep, "check": cmd_check, "log": cmd_log, "pref": cmd_pref}[a.cmd](a)


if __name__ == "__main__":
    main()
