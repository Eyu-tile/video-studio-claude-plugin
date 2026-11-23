#!/usr/bin/env python3
"""Watch any video from a link (or a file) and write what Claude needs to understand it.

Gets the video (YouTube, Instagram, TikTok, X, Vimeo, Facebook and ~1,800 other sites via yt-dlp;
direct .mp4/.mov links; Google Drive; Dropbox; local files), then:
  meta.json     title, author, caption/description, duration, link
  breakdown/    shots, camera moves, look, pacing, tempo, hits (vs breakdown)
  frames_NN.png contact sheets: a frame every --every seconds, timestamped (Read these)
  transcript    words with timestamps when a Whisper backend is installed (vs setup)
  watch.md      one page tying it together: read it first, then the frame sheets

  vs watch "https://www.instagram.com/reel/XXXX/" -o work/watch/reel
  vs watch "https://youtu.be/XXXX" -o work/watch/talk --every 5 --no-transcript
  vs watch raw/ref.mp4 -o work/watch/ref
  vs watch "<url>" -o work/watch/x --cookies-from-browser chrome     (logged-in or private posts)

Instagram often answers 429 to tools that aren't logged in; vs watch then falls back to the public
embed page (caption + video). Only watch what you may study; downloading doesn't clear rights.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, fmt_ts, need, probe, save_json  # noqa: E402

HERE = Path(__file__).parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) "
      "Version/17.0 Safari/605.1.15")
MEDIA_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi", ".mp3", ".wav", ".m4a"}


def http_get(url, dest=None, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if dest is None:
            return r.read().decode("utf-8", "replace")
        with open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
    return dest


def instagram_embed(url, folder):
    """Caption, author and video of a public Instagram post from its embed page. Returns (file, meta)."""
    m = re.search(r"instagram\.com/(?:[^/]+/)?(reel|reels|p|tv)/([A-Za-z0-9_-]+)", url)
    if not m:
        return None, {}
    kind = "reel" if m.group(1) in ("reel", "reels") else "p"
    page = http_get(f"https://www.instagram.com/{kind}/{m.group(2)}/embed/captioned/")
    meta = {"id": m.group(2), "url": url, "source": "instagram embed"}
    cap = re.search(r'class="Caption"[^>]*>(.*?)</div>', page, re.S)
    if cap:
        import html as h
        meta["description"] = re.sub(r"\s+", " ", h.unescape(re.sub(r"<[^>]+>", " ", cap.group(1)))).strip()
    user = re.search(r'class="UsernameText"[^>]*>([^<]+)<', page)
    if user:
        meta["uploader"] = user.group(1)
    i = page.find("video_url")
    if i < 0:
        return None, meta
    vm = re.search(r'(https?:[^"]*?)\\+"', page[i:i + 4000])
    if not vm:
        return None, meta
    vurl = vm.group(1).replace("\\", "").replace("u0026", "&")
    dest = Path(folder) / f"instagram_{m.group(2)}.mp4"
    http_get(vurl, dest, timeout=120)
    return dest, meta


def fetch(src, folder, cookies=None, max_height=1080):
    """Download src into folder. Returns (path, meta)."""
    p = Path(src)
    if p.exists():
        return p, {"title": p.stem, "source": "local file"}
    url = src
    host = urllib.parse.urlsplit(url).netloc.lower()
    if not host:
        die(f"not a file or a link: {src}")
    path_ext = Path(urllib.parse.urlsplit(url).path).suffix.lower()
    if path_ext in MEDIA_EXT:
        dest = Path(folder) / Path(urllib.parse.urlsplit(url).path).name
        http_get(url, dest, timeout=600)
        return dest, {"url": url, "title": dest.stem, "source": "direct link"}
    if "drive.google.com" in host or "docs.google.com" in host:
        import importlib.util
        if not importlib.util.find_spec("gdown"):
            die("Google Drive links need gdown: vs setup")
        from vs_common import gdrive_download
        out = gdrive_download(url, folder)
        if not out:
            die("Google Drive refused the download (is the file shared as 'anyone with the link'?)")
        return Path(out), {"url": url, "title": Path(out).stem, "source": "google drive"}
    if "dropbox.com" in host:
        u = re.sub(r"([?&])dl=0", r"\1dl=1", url)
        u = u if "dl=1" in u else u + ("&" if "?" in u else "?") + "dl=1"
        dest = Path(folder) / (Path(urllib.parse.urlsplit(url).path).name or "dropbox.mp4")
        http_get(u, dest, timeout=600)
        return dest, {"url": url, "title": dest.stem, "source": "dropbox"}
    # A page: yt-dlp, with an embed fallback for Instagram.
    import importlib.util
    ytdlp = [sys.executable, "-m", "yt_dlp"] if importlib.util.find_spec("yt_dlp") else (
        ["yt-dlp"] if shutil.which("yt-dlp") else None)
    err = "yt-dlp is not installed (vs setup)"
    if ytdlp:
        cmd = ytdlp + ["--no-warnings", "--no-playlist", "-f",
                       f"bv*[height<={max_height}]+ba/b[height<={max_height}]/b", "--merge-output-format", "mp4",
                       "--write-info-json", "-o", str(Path(folder) / "video.%(ext)s")]
        if cookies:
            cmd += ["--cookies-from-browser", cookies]
        r = subprocess.run(cmd + [url], capture_output=True, text=True)
        vids = [f for f in Path(folder).glob("video.*") if f.suffix != ".json" and not f.name.endswith(".part")]
        if r.returncode == 0 and vids:
            meta = {"url": url, "source": "yt-dlp"}
            info = Path(folder) / "video.info.json"
            if info.exists():
                j = json.loads(info.read_text())
                for k in ("title", "uploader", "channel", "description", "duration", "upload_date", "view_count",
                          "like_count", "webpage_url", "extractor"):
                    if j.get(k) is not None:
                        meta[k] = j[k]
                info.unlink()
            return vids[0], meta
        err = (r.stderr.strip().splitlines() or ["yt-dlp failed"])[-1]
    if "instagram.com" in host:
        print(f"yt-dlp: {err[:160]}; trying Instagram's public embed page", file=sys.stderr)
        f, meta = instagram_embed(url, folder)
        if f:
            return f, meta
        die("Instagram didn't serve this post publicly. Log in to Instagram in your browser and add "
            "--cookies-from-browser chrome (or safari/firefox), or save the video and pass the file")
    die(f"could not get a video from {url}: {err[:300]}\nLogged-in or private posts: --cookies-from-browser chrome")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="link or file")
    ap.add_argument("-o", "--out", required=True, help="output folder")
    ap.add_argument("--every", type=float, help="seconds between sheet frames (default: ~24 frames per minute, "
                                                "at least every 0.5 s)")
    ap.add_argument("--no-transcript", action="store_true")
    ap.add_argument("--model", default="small", help="Whisper model for the transcript")
    ap.add_argument("--cookies-from-browser", help="chrome | safari | firefox: for logged-in or private posts")
    ap.add_argument("--max-height", type=int, default=1080)
    args = ap.parse_args()
    need("ffmpeg")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="vs-watch-"))
    try:
        path, meta = fetch(args.source, tmp, args.cookies_from_browser, args.max_height)
        if path.parent == tmp:
            dest = out / ("video" + path.suffix)
            shutil.move(str(path), dest)
            path = dest
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    info = probe(str(path))
    if not info["has_video"] and not info["has_audio"]:
        die(f"{path} has no audio or video")
    meta.update({"file": str(path), "duration": round(info["duration"], 2), "width": info["width"],
                 "height": info["height"], "fps": info["fps"]})
    save_json(out / "meta.json", meta)
    dur = info["duration"] or 0
    print(f"got {path.name}: {info['width']}x{info['height']}, {fmt_ts(dur)}", file=sys.stderr)

    sheets, bd_ok = [], False
    if info["has_video"]:
        r = subprocess.run([sys.executable, str(HERE / "breakdown.py"), str(path), "-o", str(out / "breakdown")],
                           capture_output=True, text=True)
        bd_ok = r.returncode == 0
        every = args.every or max(0.5, round(dur / 24 * (1 if dur <= 60 else 2.5), 1))
        times = [round(t * every, 2) for t in range(int(dur / every) + 1) if t * every < dur - 0.05]
        for i in range(0, len(times), 12):
            sheet = out / f"frames_{i // 12 + 1:02d}.png"
            subprocess.run([sys.executable, str(HERE / "filmstrip.py"), str(path), "-o", str(sheet), "--at",
                            ",".join(map(str, times[i:i + 12])), "--cols", "6", "--width", "300"],
                           capture_output=True, text=True)
            if sheet.exists():
                sheets.append((sheet, times[i], times[min(i + 11, len(times) - 1)]))
            if len(sheets) >= 12:
                break
    transcript, tnote = None, ""
    if info["has_audio"] and not args.no_transcript:
        r = subprocess.run([sys.executable, str(HERE / "transcribe.py"), str(path), "-o", str(out / "transcript"),
                            "--model", args.model], capture_output=True, text=True)
        if r.returncode == 0 and (out / "transcript.json").exists():
            transcript = json.loads((out / "transcript.json").read_text())
        else:
            tnote = (r.stderr.strip().splitlines() or ["transcription failed"])[-1][:200]

    title = meta.get("title") or (f"@{meta['uploader']}: " + meta.get("description", "")[:70].strip()
                                  if meta.get("uploader") else path.name)
    lines = [f"# Watched: {title}", ""]
    for k, label in (("uploader", "By"), ("url", "Link"), ("upload_date", "Posted"), ("view_count", "Views")):
        if meta.get(k):
            lines.append(f"- {label}: {meta[k]}")
    lines.append(f"- {info['width']}x{info['height']} @ {info['fps']} fps, {fmt_ts(dur)}; file `{path}`")
    if meta.get("description"):
        lines += ["", "## Caption / description", "", meta["description"][:3000]]
    if bd_ok and (out / "breakdown" / "report.md").exists():
        rep = (out / "breakdown" / "report.md").read_text().splitlines()
        lines += ["", "## How it's cut (vs breakdown)", ""] + rep[2:] + [""]
    if transcript:
        lines += ["## What's said", ""]
        for seg in transcript.get("segments", []):
            lines.append(f"- [{fmt_ts(seg['s'])[1:]}] {seg['text'].strip()}")
        lines.append("")
    elif info["has_audio"]:
        lines += ["## What's said", "", f"No transcript ({'skipped' if args.no_transcript else tnote or 'no Whisper backend: vs setup'}).", ""]
    if sheets:
        lines += ["## Look at (Read each, in order)", ""]
        lines += [f"- `{s}`: {fmt_ts(a)[1:]}-{fmt_ts(b)[1:]}" for s, a, b in sheets]
        lines += ["", "Read the sheets, then describe what happens shot by shot (on-screen text, effects, framing, "
                      "who/what is shown). Zoom in on any moment: `vs filmstrip <file> -o x.png --at t1,t2`."]
    (out / "watch.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"watched -> {out}/watch.md ({len(sheets)} frame sheet(s){', transcript' if transcript else ''}"
          f"{', breakdown' if bd_ok else ''})")


if __name__ == "__main__":
    main()
