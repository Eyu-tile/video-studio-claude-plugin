#!/usr/bin/env python3
"""Learn a client's footage library from wherever they keep it, without downloading all of it.

Sources: Google Drive, Frame.io, Dropbox, OneDrive, any page with videos, direct file links, a local folder.
Public share links work as they are. A saved API key (vs keys, per client) switches to the provider's API.

  vs learn source  <Library> <link-or-path> [--name N] [--provider auto|gdrive|frameio|dropbox|onedrive|web|direct|local]
  vs learn scan    <Library>                     list every file in every source  -> inventory.json
  vs learn sample  <Library> [--jobs 6]          probe + a few frames per clip over the network -> numbered contact sheets
  vs learn next    <Library> [--n 12]            the next sheet to look at and the template to fill
  vs learn tag     <Library> tags.json           save what was seen (kind, people, beats, status, best part, use)
  vs learn atlas   <Library>                     write ATLAS.md / atlas.json from everything learned
  vs learn find    <Library> "woman sneezing" [--status OK] [--unused] [--kind ugc]
  vs learn fetch   <Library> <id|name> -o DIR [--section 2-6]   fresh download of one clip when a project needs it
  vs learn use     <Library> <id> [<id>...] --project CODE      log usage (uniqueness rule)
  vs learn status  <Library>

Files: <workspace>/library/<Library>/resources/ (sources.json, inventory.json, atlas.json, ATLAS.md, sheets/).
Frames are cached in ~/.cache/video-studio/learn/<Library>/. Keys are never written here.
"""
import argparse
import base64
import concurrent.futures as cf
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, load_json, save_json  # noqa: E402

VIDEO = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".mts", ".mxf", ".mpg", ".mpeg", ".3gp"}
IMAGE = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff", ".gif"}
AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
UA = {"User-Agent": "Mozilla/5.0 (video-studio learn)"}
FIELDS = ["kind", "people", "product", "beats", "framing", "best", "status", "use", "tags", "notes"]


# ---------- paths ----------
def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    except OSError:
        root = ""
    return Path(root or os.getcwd()) / "video-studio"


def lib_dir(lib):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,60}", lib):
        die("library name: letters, digits, '.', '_' or '-' (e.g. CaptureCards)")
    return workspace() / "library" / lib / "resources"


def cache_dir(lib):
    return Path(os.environ.get("VS_LEARN_CACHE") or Path.home() / ".cache" / "video-studio" / "learn") / lib


def jload(p, default):
    return load_json(p) if Path(p).exists() else default


def kind_of(name, mime=""):
    ext = Path(name).suffix.lower()
    if ext in VIDEO or mime.startswith("video/"):
        return "video"
    if ext in IMAGE or mime.startswith("image/"):
        return "image"
    if ext in AUDIO or mime.startswith("audio/"):
        return "audio"
    return "other"


# ---------- keys (per client, from vs keys) ----------
def key(provider, lib):
    try:
        from keys import resolve
        v, _ = resolve(provider, lib)
        return v
    except Exception:
        return None


# ---------- http ----------
def http(url, data=None, headers=None, timeout=60):
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def http_json(url, data=None, headers=None):
    body = json.dumps(data).encode() if isinstance(data, (dict, list)) else data
    h = {"Content-Type": "application/json", **(headers or {})} if body else (headers or {})
    return json.loads(http(url, body, h))


# ---------- provider detection ----------
def detect(link):
    if Path(link).expanduser().exists():
        return "local"
    host = urllib.parse.urlsplit(link).netloc.lower()
    if "drive.google.com" in host or "docs.google.com" in host:
        return "gdrive"
    if "frame.io" in host or host == "f.io":
        return "frameio"
    if "dropbox.com" in host:
        return "dropbox"
    if "1drv.ms" in host or "onedrive" in host or "sharepoint.com" in host:
        return "onedrive"
    if kind_of(urllib.parse.urlsplit(link).path) != "other":
        return "direct"
    return "web"


# ---------- adapters: list(source, lib) -> [item]; resolve(item, lib) -> url or local path ----------
def item(provider, sid, name, folder="", size=None, **extra):
    return {"id": f"{provider[:2]}-{hashlib.sha1(str(sid).encode()).hexdigest()[:10]}", "provider": provider,
            "pid": sid, "name": name, "folder": folder, "size": size, "kind": kind_of(name, extra.pop("mime", "")),
            **extra}


def list_local(src, lib):
    root = Path(src["link"]).expanduser()
    out = []
    for p in sorted(root.rglob("*")) if root.is_dir() else [root]:
        if p.is_file() and not p.name.startswith("."):
            out.append(item("local", str(p.resolve()), p.name, str(p.parent.relative_to(root)) if root.is_dir() else "",
                            p.stat().st_size))
    return out


def list_direct(src, lib):
    links = [src["link"]]
    if Path(src["link"]).is_file() and src["link"].endswith(".txt"):
        links = [x.strip() for x in Path(src["link"]).read_text().splitlines() if x.strip()]
    return [item("direct", u, urllib.parse.unquote(Path(urllib.parse.urlsplit(u).path).name) or u) for u in links]


GD_FOLDER = re.compile(r"/folders/([\w-]+)|[?&]id=([\w-]+)")
GD_FILE = re.compile(r"/file/d/([\w-]+)|[?&]id=([\w-]+)")


def gd_id(link, pat):
    m = pat.search(link)
    return (m.group(1) or m.group(2)) if m else None


def parse_gdrive_embedded(page):
    """Entries of https://drive.google.com/embeddedfolderview?id=FOLDER: [(id, name, is_folder)]."""
    out = []
    for m in re.finditer(r'<div class="flip-entry" id="entry-([\w-]+)".*?<a href="([^"]+)".*?'
                         r'<div class="flip-entry-title">(.*?)</div>', page, re.S):
        fid, href, title = m.group(1), m.group(2), html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).strip()
        out.append((fid, title, "/folders/" in href))
    return out


def list_gdrive(src, lib):
    k = key("gdrive", lib)
    root = gd_id(src["link"], GD_FOLDER) if "/folders/" in src["link"] else None
    if not root:
        fid = gd_id(src["link"], GD_FILE) or die(f"no Drive file or folder id in {src['link']}")
        return [item("gdrive", fid, src.get("name") or fid)]
    out, todo = [], [(root, "")]
    while todo:
        fid, path = todo.pop()
        if k:
            tok = None
            while True:
                q = urllib.parse.urlencode({"q": f"'{fid}' in parents and trashed=false", "pageSize": 1000, "key": k,
                                            "fields": "nextPageToken,files(id,name,mimeType,size,"
                                                      "videoMediaMetadata,imageMediaMetadata)",
                                            "supportsAllDrives": "true", "includeItemsFromAllDrives": "true",
                                            **({"pageToken": tok} if tok else {})})
                d = http_json(f"https://www.googleapis.com/drive/v3/files?{q}")
                for f in d.get("files", []):
                    if f["mimeType"] == "application/vnd.google-apps.folder":
                        todo.append((f["id"], f"{path}/{f['name']}".strip("/")))
                    else:
                        vm = f.get("videoMediaMetadata") or {}
                        out.append(item("gdrive", f["id"], f["name"], path, int(f["size"]) if f.get("size") else None,
                                        mime=f["mimeType"], duration=round(int(vm["durationMillis"]) / 1000, 2)
                                        if vm.get("durationMillis") else None,
                                        res=f"{vm['width']}x{vm['height']}" if vm.get("width") else None))
                tok = d.get("nextPageToken")
                if not tok:
                    break
        else:
            page = http(f"https://drive.google.com/embeddedfolderview?id={fid}").decode("utf-8", "replace")
            for cid, name, is_folder in parse_gdrive_embedded(page):
                if is_folder:
                    todo.append((cid, f"{path}/{name}".strip("/")))
                else:
                    out.append(item("gdrive", cid, name, path))
    return out


def resolve_gdrive(it, lib):
    k = key("gdrive", lib)
    if k:
        return f"https://www.googleapis.com/drive/v3/files/{it['pid']}?alt=media&key={k}&supportsAllDrives=true"
    return f"https://drive.usercontent.google.com/download?id={it['pid']}&export=download&confirm=t"


def od_token(link):
    return "u!" + base64.urlsafe_b64encode(link.encode()).decode().rstrip("=")


def list_onedrive(src, lib):
    tok = od_token(src["link"])
    base = f"https://api.onedrive.com/v1.0/shares/{tok}"
    out, todo = [], [(f"{base}/root?expand=children", "")]
    while todo:
        url, path = todo.pop()
        d = http_json(url)
        kids = d.get("children", d.get("value", []))
        if not kids and "file" in d:
            kids = [d]
        for c in kids:
            if "folder" in c:
                todo.append((f"{base}/items/{c['id']}/children", f"{path}/{c['name']}".strip("/")))
            else:
                out.append(item("onedrive", c["id"], c["name"], path, c.get("size"),
                                mime=(c.get("file") or {}).get("mimeType", ""), share=tok))
        nxt = d.get("@odata.nextLink")
        if nxt:
            todo.append((nxt, path))
    return out


def resolve_onedrive(it, lib):
    d = http_json(f"https://api.onedrive.com/v1.0/shares/{it['share']}/items/{it['pid']}")
    return d.get("@content.downloadUrl") or die(f"OneDrive gave no download link for {it['name']}")


def list_dropbox(src, lib):
    link = src["link"]
    tok = key("dropbox", lib)
    if not tok:
        if "/scl/fi/" in link or "/s/" in link:  # a single shared file
            return [item("dropbox", link, urllib.parse.unquote(Path(urllib.parse.urlsplit(link).path).name))]
        die("a Dropbox shared folder needs a Dropbox access token to list it without downloading the whole zip: "
            f"vs keys ask dropbox --project {lib}  (or download it once with: vs add '{link}' --library)")
    out, todo = [], [("", "")]
    h = {"Authorization": f"Bearer {tok}"}
    while todo:
        path, rel = todo.pop()
        d = http_json("https://api.dropboxapi.com/2/files/list_folder", {"path": path, "shared_link": {"url": link}},
                      h)
        while True:
            for e in d["entries"]:
                if e[".tag"] == "folder":
                    todo.append((f"{path}/{e['name']}", f"{rel}/{e['name']}".strip("/")))
                else:
                    out.append(item("dropbox", f"{path}/{e['name']}", e["name"], rel, e.get("size"), link=link))
            if not d.get("has_more"):
                break
            d = http_json("https://api.dropboxapi.com/2/files/list_folder/continue", {"cursor": d["cursor"]}, h)
    return out


def resolve_dropbox(it, lib):
    if "link" not in it:  # single public file
        u = urllib.parse.urlsplit(it["pid"])
        q = urllib.parse.parse_qs(u.query)
        q["dl"] = ["1"]
        return urllib.parse.urlunsplit(u._replace(query=urllib.parse.urlencode(q, doseq=True)))
    tok = key("dropbox", lib) or die("Dropbox token missing: vs keys ask dropbox --project " + lib)
    dest = cache_dir(lib) / "files" / f"{it['id']}{Path(it['name']).suffix}"
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        data = http("https://content.dropboxapi.com/2/sharing/get_shared_link_file", b"",
                    {"Authorization": f"Bearer {tok}", "Dropbox-API-Arg": json.dumps({"url": it["link"],
                                                                                       "path": it["pid"]})},
                    timeout=600)
        dest.write_bytes(data)
    return str(dest)


BROWSER_JS = Path(__file__).with_name("learn_browser.mjs")


def run_browser(mode, link):
    if not shutil.which("node"):
        die("this source is read with a headless browser: install Node.js, then `npm i -g playwright && "
            "npx playwright install chromium`")
    p = subprocess.run(["node", str(BROWSER_JS), mode, link], capture_output=True, text=True, timeout=1800,
                       env={**os.environ, "NODE_PATH": os.environ.get("NODE_PATH") or subprocess.run(
                           ["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()})
    if p.returncode != 0:
        die(f"browser read failed: {(p.stderr or p.stdout).strip()[-400:]}")
    return json.loads(p.stdout)


def list_frameio(src, lib):
    items = run_browser("frameio", src["link"])
    return [item("frameio", a["id"], a["name"], a.get("path", ""), a.get("size"), url=a.get("dl"),
                 fetched=time.time()) for a in items if a.get("name") and a.get("dl")]


def resolve_frameio(it, lib):
    # signed links expire (about a day): re-read the share when the cached one is old
    if it.get("url") and time.time() - it.get("fetched", 0) < 6 * 3600:
        return it["url"]
    src = next((s for s in jload(lib_dir(lib) / "sources.json", []) if s["provider"] == "frameio"), None)
    fresh = {a["id"]: a for a in run_browser("frameio", src["link"])} if src else {}
    a = fresh.get(it["pid"]) or die(f"{it['name']} is no longer in the Frame.io share (removed or moved)")
    return a["dl"]


def list_web(src, lib):
    found = run_browser("web", src["link"])
    return [item("web", a["url"], a.get("name") or Path(urllib.parse.urlsplit(a["url"]).path).name or a["url"],
                 "", a.get("size"), url=a["url"]) for a in found]


ADAPTERS = {
    "local": (list_local, lambda it, lib: it["pid"]),
    "direct": (list_direct, lambda it, lib: it["pid"]),
    "gdrive": (list_gdrive, resolve_gdrive),
    "onedrive": (list_onedrive, resolve_onedrive),
    "dropbox": (list_dropbox, resolve_dropbox),
    "frameio": (list_frameio, resolve_frameio),
    "web": (list_web, lambda it, lib: it["url"]),
}


def resolve(it, lib):
    return ADAPTERS[it["provider"]][1](it, lib)


# ---------- media probing over the network ----------
def net(src):
    """ffmpeg/ffprobe input options for a URL: timeout, and the proxy ffmpeg doesn't pick up by itself."""
    if not str(src).startswith(("http://", "https://")):
        return []
    px = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or os.environ.get("HTTP_PROXY") \
        or os.environ.get("http_proxy")
    return ["-rw_timeout", "30000000"] + (["-http_proxy", px] if px else [])


def probe(src):
    p = subprocess.run(["ffprobe", "-v", "error", *net(src), "-show_entries",
                        "format=duration,size:stream=codec_type,width,height,avg_frame_rate", "-of", "json", src],
                       capture_output=True, text=True, timeout=180)
    d = json.loads(p.stdout or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    fr = v.get("avg_frame_rate", "0/1").split("/")
    fps = round(int(fr[0]) / int(fr[1]), 2) if len(fr) == 2 and fr[1] not in ("0", "") else None
    w, h = v.get("width"), v.get("height")
    return {"duration": round(float(d["format"]["duration"]), 2) if d.get("format", {}).get("duration") else None,
            "res": f"{w}x{h}" if w else None, "orient": None if not w else
            ("vertical" if h > w else "horizontal" if w > h else "square"), "fps": fps,
            "has_audio": any(s.get("codec_type") == "audio" for s in d.get("streams", []))}


def frames(src, dur, n, out):
    out.mkdir(parents=True, exist_ok=True)
    ts = [dur * (i + 0.5) / n for i in range(n)] if dur else [0.0]
    got = []
    for i, t in enumerate(ts):
        f = out / f"{i:02d}.jpg"
        if not f.exists():
            subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{t:.2f}", *net(src),
                            "-i", src, "-frames:v", "1", "-vf", "scale=-2:300", "-q:v", "4", str(f)],
                           capture_output=True, timeout=180)
        if f.exists():
            got.append(f)
    return got, ts


def sample_one(it, lib, n):
    try:
        src = resolve(it, lib)
        meta = {} if it["kind"] == "image" else probe(src)
        fdir = cache_dir(lib) / "frames" / it["id"]
        fr, ts = frames(src, meta.get("duration"), 1 if it["kind"] == "image" else n, fdir)
        if not fr:
            return it["id"], {"sample_error": "no frames could be read"}
        return it["id"], {**{k: v for k, v in meta.items() if v is not None}, "frame_times": [round(t, 1) for t in ts],
                          "sampled": time.strftime("%Y-%m-%d %H:%M")}
    except SystemExit as e:
        return it["id"], {"sample_error": str(e)}
    except Exception as e:  # keep going: one bad file must not stop a 5,000-file library
        return it["id"], {"sample_error": f"{type(e).__name__}: {e}"[:300]}


def strip(lib, it, label, n, out):
    fdir = cache_dir(lib) / "frames" / it["id"]
    fr = sorted(fdir.glob("*.jpg"))
    if not fr:
        return None
    out.parent.mkdir(parents=True, exist_ok=True)
    args = ["ffmpeg", "-nostdin", "-v", "error", "-y"]
    for f in fr:
        args += ["-i", str(f)]
    k = len(fr)
    flt = "".join(f"[{i}]scale=300:300:force_original_aspect_ratio=decrease,pad=300:300:(ow-iw)/2:(oh-ih)/2:black[s{i}];"
                  for i in range(k))
    flt += "".join(f"[s{i}]" for i in range(k)) + (f"hstack=inputs={k}" if k > 1 else "null")
    flt += f",pad={300 * n}:336:0:36:black,drawtext=text='{label}':x=8:y=6:fontsize=24:fontcolor=yellow"
    p = subprocess.run(args + ["-filter_complex", flt, str(out)], capture_output=True)
    if p.returncode:  # no drawtext (fontconfig) available: same strip without the label
        flt = flt.rsplit(",drawtext", 1)[0]
        subprocess.run(args + ["-filter_complex", flt, str(out)], capture_output=True)
    return out if out.exists() else None


# ---------- commands ----------
def cmd_source(a):
    d = lib_dir(a.library)
    srcs = jload(d / "sources.json", [])
    prov = detect(a.link) if a.provider == "auto" else a.provider
    if prov not in ADAPTERS:
        die(f"provider must be one of: {', '.join(ADAPTERS)}")
    if any(s["link"] == a.link for s in srcs):
        print("already added")
        return
    srcs.append({"name": a.name or f"{prov}-{len(srcs) + 1}", "provider": prov, "link": a.link,
                 "added": time.strftime("%Y-%m-%d")})
    save_json(d / "sources.json", srcs)
    k = {"gdrive": "gdrive", "dropbox": "dropbox", "frameio": "frameio"}.get(prov)
    hint = f" (an API key makes it faster/complete: vs keys ask {k} --project {a.library})" \
        if k and not key(k, a.library) else ""
    print(f"source added: {prov} {a.link}{hint}\nnext: vs learn scan {a.library}")


def cmd_scan(a):
    d = lib_dir(a.library)
    srcs = jload(d / "sources.json", []) or die(f"no sources yet: vs learn source {a.library} <link>")
    inv = {x["id"]: x for x in jload(d / "inventory.json", [])}
    seen = set()
    for s in srcs:
        try:
            items = ADAPTERS[s["provider"]][0](s, a.library)
        except SystemExit:
            raise
        except Exception as e:
            print(f"  {s['name']}: could not list ({type(e).__name__}: {e})", file=sys.stderr)
            continue
        new = 0
        for it in items:
            it["source"] = s["name"]
            old = inv.get(it["id"], {})
            if not old:
                new += 1
            inv[it["id"]] = {**old, **it}
            seen.add(it["id"])
        print(f"  {s['name']} ({s['provider']}): {len(items)} files, {new} new")
    for i, x in inv.items():
        x["missing"] = i not in seen
    by_key = {}
    for x in inv.values():  # same name and size in two places = duplicate
        if x.get("size"):
            k2 = (x["name"].lower(), x["size"])
            if k2 in by_key and by_key[k2] != x["id"]:
                x["duplicate_of"] = by_key[k2]
            by_key.setdefault(k2, x["id"])
    rows = sorted(inv.values(), key=lambda x: (x.get("folder", ""), x["name"]))
    save_json(d / "inventory.json", rows)
    kinds = {}
    for x in rows:
        kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
    gone = sum(x["missing"] for x in rows)
    print(f"inventory: {len(rows)} files ({', '.join(f'{v} {k}' for k, v in sorted(kinds.items()))})"
          f"{f'; {gone} no longer in their source' if gone else ''}\nnext: vs learn sample {a.library}")


def todo_items(d, redo=False):
    return [x for x in jload(d / "inventory.json", []) if x["kind"] in ("video", "image") and not x.get("missing")
            and not x.get("duplicate_of") and (redo or not x.get("sampled"))]


def cmd_sample(a):
    d = lib_dir(a.library)
    inv = {x["id"]: x for x in jload(d / "inventory.json", [])} or die(f"run vs learn scan {a.library} first")
    todo = todo_items(d, a.redo)[: a.limit or None]
    if a.folder:
        todo = [x for x in todo if x.get("folder", "").startswith(a.folder)]
    print(f"sampling {len(todo)} files with {a.jobs} parallel jobs ({a.frames} frames each, read over the network)")
    t0, done = time.time(), 0
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for fid, res in ex.map(lambda it: sample_one(it, a.library, a.frames), todo):
            if "sample_error" not in res:
                inv[fid].pop("sample_error", None)
            inv[fid].update(res)
            done += 1
            if done % 25 == 0 or done == len(todo):
                save_json(d / "inventory.json", list(inv.values()))
                print(f"  {done}/{len(todo)}  {time.time() - t0:.0f}s")
    save_json(d / "inventory.json", list(inv.values()))
    build_sheets(a.library, a.frames)
    errs = sum(1 for x in inv.values() if x.get("sample_error"))
    print(f"done in {time.time() - t0:.0f}s{f'; {errs} could not be read (see sample_error)' if errs else ''}"
          f"\nnext: vs learn next {a.library}")


def build_sheets(lib, n, per=12):
    d = lib_dir(lib)
    inv = jload(d / "inventory.json", [])
    atlas = jload(d / "atlas.json", {})
    pending = [x for x in inv if x.get("sampled") and x["id"] not in atlas and not x.get("sheet")]
    sdir = d / "sheets"
    sdir.mkdir(parents=True, exist_ok=True)
    start = len(list(sdir.glob("sheet_*.jpg")))
    byid = {x["id"]: x for x in inv}
    for k in range(0, len(pending), per):
        group = pending[k:k + per]
        num = start + k // per + 1
        strips = []
        for j, it in enumerate(group, 1):
            s = strip(lib, it, f"{j}  {it['name'][:60]}".replace("'", "").replace(":", " "), n,
                      cache_dir(lib) / "strips" / f"{it['id']}.jpg")
            if s:
                strips.append(s)
                byid[it["id"]]["sheet"] = f"sheet_{num:04d}.jpg#{j}"
        if strips:
            out = sdir / f"sheet_{num:04d}.jpg"
            args = ["ffmpeg", "-nostdin", "-v", "error", "-y"]
            for s in strips:
                args += ["-i", str(s)]
            flt = "".join(f"[{i}]" for i in range(len(strips))) + (
                f"vstack=inputs={len(strips)}" if len(strips) > 1 else "null")
            subprocess.run(args + ["-filter_complex", flt, "-q:v", "5", str(out)], capture_output=True)
    save_json(d / "inventory.json", list(byid.values()))


def cmd_next(a):
    d = lib_dir(a.library)
    inv = jload(d / "inventory.json", [])
    atlas = jload(d / "atlas.json", {})
    waiting = {}
    for x in inv:
        if x.get("sheet") and x["id"] not in atlas:
            waiting.setdefault(x["sheet"].split("#")[0], []).append(x)
    if not waiting:
        left = len(todo_items(d))
        print("nothing waiting to be described." + (f" {left} files not sampled yet: vs learn sample {a.library}"
                                                    if left else f" All learned: vs learn atlas {a.library}"))
        return
    sheet = sorted(waiting)[0]
    rows = sorted(waiting[sheet], key=lambda x: int(x["sheet"].split("#")[1]))
    print(f"Look at: {d / 'sheets' / sheet}   ({len(waiting)} sheets waiting, {sum(map(len, waiting.values()))} clips)")
    print("Each row is one clip, frames left to right at the listed times. Then save a JSON list with vs learn tag:")
    tmpl = []
    for x in rows:
        times = ", ".join(f"{t}s" for t in x.get("frame_times", []))
        print(f"  #{x['sheet'].split('#')[1]:>2} {x['id']}  {x['name'][:50]:50} {x.get('duration', '-')}s "
              f"{x.get('res') or ''} {'audio' if x.get('has_audio') else 'no audio'}  frames at {times}")
        tmpl.append({"id": x["id"], "kind": "", "people": "", "product": "", "beats": "0-2: ...; 2-5: ...",
                     "framing": "", "best": "0-3", "status": "OK|CAUTION|BANNED", "use": "", "tags": {}})
    print(json.dumps(tmpl[:1], indent=1))


def cmd_tag(a):
    d = lib_dir(a.library)
    rows = json.loads(Path(a.file).read_text() if a.file != "-" else sys.stdin.read())
    inv = {x["id"]: x for x in jload(d / "inventory.json", [])}
    atlas = jload(d / "atlas.json", {})
    n = 0
    for r in rows if isinstance(rows, list) else [rows]:
        if r.get("id") not in inv:
            print(f"  skipped unknown id {r.get('id')}", file=sys.stderr)
            continue
        atlas[r["id"]] = {**atlas.get(r["id"], {}), **{k: r[k] for k in FIELDS if k in r},
                          "learned": time.strftime("%Y-%m-%d")}
        n += 1
    save_json(d / "atlas.json", atlas)
    left = sum(1 for x in inv.values() if x.get("sheet") and x["id"] not in atlas)
    print(f"saved {n} clip(s); {left} sampled clips still to describe" + ("" if left else
                                                                          f"; vs learn atlas {a.library}"))


def merged(d):
    inv = jload(d / "inventory.json", [])
    atlas = jload(d / "atlas.json", {})
    usage = jload(d / "usage.json", {})
    return [{**x, **atlas.get(x["id"], {}), "used_in": usage.get(x["id"], [])} for x in inv]


def cmd_atlas(a):
    d = lib_dir(a.library)
    rows = merged(d)
    learned = [r for r in rows if r.get("learned")]
    save_json(d / "atlas_full.json", rows)
    L = [f"# {a.library} footage atlas", "",
         f"{len(rows)} files, {len(learned)} described. Status: OK = usable, CAUTION = check before use, "
         "BANNED = never use. Generated by `vs learn atlas`; search with `vs learn find`.", ""]
    for folder in sorted({r.get("folder", "") for r in learned}):
        L += [f"## {folder or '(top level)'}", "", "| id | file | dur | res | status | kind | people | beats | best | use |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for r in sorted((r for r in learned if r.get("folder", "") == folder), key=lambda r: r["name"]):
            cell = [r["id"], r["name"], r.get("duration", ""), r.get("res", ""), r.get("status", ""), r.get("kind", ""),
                    r.get("people", ""), r.get("beats", ""), r.get("best", ""), r.get("use", "")]
            L.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in cell) + " |")
        L.append("")
    (d / "ATLAS.md").write_text("\n".join(L))
    print(f"ATLAS.md: {len(learned)} described clips (of {len(rows)} files) -> {d / 'ATLAS.md'}")


def cmd_find(a):
    d = lib_dir(a.library)
    words = [w for w in re.split(r"\W+", a.query.lower()) if w]
    hits = []
    for r in merged(d):
        if not r.get("learned") or r.get("missing"):
            continue
        if a.status and r.get("status", "").upper() != a.status.upper():
            continue
        if a.unused and r["used_in"]:
            continue
        if a.kind and a.kind.lower() not in str(r.get("kind", "")).lower():
            continue
        text = " ".join(str(r.get(k, "")) for k in ["name", "folder", "kind", "people", "product", "beats", "use",
                                                     "tags", "notes", "framing"]).lower()
        score = sum(text.count(w) for w in words)
        if score:
            hits.append((score, r))
    hits.sort(key=lambda h: -h[0])
    for score, r in hits[: a.n]:
        print(f"{r['id']}  {r.get('status', ''):7} {r.get('duration', '-'):>6}s {r.get('orient') or '':10} "
              f"{r['name'][:40]:40} best {r.get('best', '-'):8} used {','.join(r['used_in']) or '-'}\n"
              f"      {str(r.get('beats', ''))[:160]}")
    if not hits:
        print("no matches (only described clips are searched: vs learn next to describe more)")


def cmd_fetch(a):
    d = lib_dir(a.library)
    inv = jload(d / "inventory.json", [])
    it = next((x for x in inv if x["id"] == a.clip), None) or next(
        (x for x in inv if x["name"] == a.clip or Path(x["name"]).stem == a.clip), None) or die(f"no clip {a.clip}")
    src = resolve(it, a.library)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    dest = out / re.sub(r"[^A-Za-z0-9._-]", "_", it["name"])
    if a.section:
        s, e = (float(x) for x in a.section.split("-"))
        dest = dest.with_name(f"{dest.stem}_{s:g}-{e:g}{dest.suffix or '.mp4'}")
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(s), *net(src), "-i", src, "-t", str(e - s),
                        "-c", "copy", str(dest)], check=True)
    elif Path(src).exists():
        shutil.copy2(src, dest)
    else:
        subprocess.run(["curl", "-sSfL", "--retry", "3", "-o", str(dest), src], check=True)
    print(dest)


def cmd_use(a):
    d = lib_dir(a.library)
    usage = jload(d / "usage.json", {})
    for i in a.ids:
        usage.setdefault(i, [])
        if a.project not in usage[i]:
            usage[i].append(a.project)
    save_json(d / "usage.json", usage)
    print(f"logged {len(a.ids)} clip(s) as used in {a.project}")


def cmd_status(a):
    d = lib_dir(a.library)
    inv = jload(d / "inventory.json", [])
    atlas = jload(d / "atlas.json", {})
    srcs = jload(d / "sources.json", [])
    media = [x for x in inv if x["kind"] in ("video", "image") and not x.get("missing") and not x.get("duplicate_of")]
    print(f"{a.library}: {len(srcs)} source(s), {len(inv)} files, {len(media)} usable media; "
          f"sampled {sum(1 for x in media if x.get('sampled'))}, described {sum(1 for x in media if x['id'] in atlas)}, "
          f"errors {sum(1 for x in media if x.get('sample_error'))}")
    for s in srcs:
        print(f"  {s['name']:<14} {s['provider']:<9} {s['link']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("source")
    s.add_argument("library")
    s.add_argument("link")
    s.add_argument("--name")
    s.add_argument("--provider", default="auto")
    for name in ("scan", "status", "atlas"):
        sub.add_parser(name).add_argument("library")
    s = sub.add_parser("sample")
    s.add_argument("library")
    s.add_argument("--jobs", type=int, default=6)
    s.add_argument("--frames", type=int, default=6)
    s.add_argument("--limit", type=int)
    s.add_argument("--folder", help="only files under this folder")
    s.add_argument("--redo", action="store_true")
    s = sub.add_parser("next")
    s.add_argument("library")
    s.add_argument("--n", type=int, default=12)
    s = sub.add_parser("tag")
    s.add_argument("library")
    s.add_argument("file", help="JSON list (or - for stdin)")
    s = sub.add_parser("find")
    s.add_argument("library")
    s.add_argument("query")
    s.add_argument("--status")
    s.add_argument("--kind")
    s.add_argument("--unused", action="store_true")
    s.add_argument("--n", type=int, default=15)
    s = sub.add_parser("fetch")
    s.add_argument("library")
    s.add_argument("clip")
    s.add_argument("-o", "--out", required=True)
    s.add_argument("--section", help="seconds, e.g. 2-6")
    s = sub.add_parser("use")
    s.add_argument("library")
    s.add_argument("ids", nargs="+")
    s.add_argument("--project", required=True)
    a = ap.parse_args()
    {"source": cmd_source, "scan": cmd_scan, "sample": cmd_sample, "next": cmd_next, "tag": cmd_tag,
     "atlas": cmd_atlas, "find": cmd_find, "fetch": cmd_fetch, "use": cmd_use, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    main()
