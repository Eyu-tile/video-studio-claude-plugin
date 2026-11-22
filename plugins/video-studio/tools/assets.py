#!/usr/bin/env python3
"""Get media into a project: stock search on the internet, any URL, or the editor's own files.
Every file brought in is logged with its source and licence in <project>/assets/credits.json
and CREDITS.md.

Search stock (results + a numbered contact sheet to choose from):
  vs fetch search "city night traffic" --type video --orientation portrait --project launch
  vs fetch search "upbeat corporate" --type music --project launch
  vs fetch search "whoosh" --type sfx --project launch
  vs fetch search "handshake" --type photo --provider unsplash,pexels --project launch
Download chosen results (numbers from the sheet / table):
  vs fetch get video-studio/projects/launch/work/assets/city-night-traffic.video.json 2 5 7
Internet Archive films: look inside before cutting, then cut only the seconds you need (verified, with provenance):
  vs fetch search "children eating bananas black and white" --provider archive --project launch
  vs fetch inspect <results.json> 3 --project launch          (scenes + keyframe sheet; multi-clip items: clip list)
  vs fetch get <results.json> 3 --section 5:00-5:08 --project launch
  vs fetch inspect archive:AboutBan1935 --window 4:00-9:00    (any item by identifier)
Bring in anything the editor gives (files, folders, zips, links):
  vs add ~/Desktop/shoot/ --project launch                  (footage -> raw/, by type)
  vs add logo.png font.otf look.cube --project launch       (-> assets/logos, fonts, luts)
  vs add "https://drive.google.com/drive/folders/..." --project launch
  vs add "https://www.dropbox.com/s/.../clip.mp4?dl=0" --as broll --project launch
  vs add "https://youtu.be/..." --as ref --project launch   (pages via yt-dlp; rights are on you)
  vs add brand-kit.zip --library                            (shared across projects)
API keys (free): vs keys set pexels | pixabay | unsplash | freesound | jamendo    vs keys list
No-key providers: openverse (800M+ CC images and audio: music and sound effects), wikimedia (images + video),
wikipedia (the images illustrating articles on a topic), archive (Internet Archive: public-domain films, newsreels,
home movies, audio), nasa (public domain), youtube (Creative Commons videos only unless --allow-any-license; needs yt-dlp).

Providers' terms: Pexels / Pixabay / Unsplash licences allow free commercial use without attribution
(Unsplash asks for credit); Openverse / Wikimedia / Freesound items carry per-item Creative Commons
licences: the ledger records each one, and NC/ND licences are excluded by default.
"""
import argparse
import getpass
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import IMAGE_EXT, die, fmt_ts, load_json, need, probe, run, save_json  # noqa: E402
import archive as ia  # noqa: E402

UA = "video-studio-claude-plugin/2.0 (+https://claude.com/claude-code)"
KEYS_FILE = Path(os.environ.get("VS_KEYS_FILE", Path.home() / ".config" / "video-studio" / "keys.env"))
KEY_ENV = {"pexels": "PEXELS_API_KEY", "pixabay": "PIXABAY_API_KEY", "unsplash": "UNSPLASH_ACCESS_KEY",
           "freesound": "FREESOUND_API_KEY", "jamendo": "JAMENDO_CLIENT_ID"}
BASE = {  # override with VS_<PROVIDER>_BASE (self-hosted mirrors, proxies, tests)
    "pexels": "https://api.pexels.com", "pixabay": "https://pixabay.com/api", "unsplash": "https://api.unsplash.com",
    "openverse": "https://api.openverse.org/v1", "wikimedia": "https://commons.wikimedia.org/w/api.php",
    "freesound": "https://freesound.org/apiv2", "nasa": "https://images-api.nasa.gov",
    "archive": "https://archive.org", "wikipedia": "https://{lang}.wikipedia.org/w/api.php",
    "jamendo": "https://api.jamendo.com/v3.0", "ccmixter": "http://ccmixter.org/api",
    "incompetech": "https://incompetech.com/music/royalty-free",
}
PROVIDERS = {  # type -> providers tried in this order by --provider auto
    "video": ["pexels", "pixabay", "archive", "wikimedia", "nasa", "youtube"],
    "photo": ["pexels", "unsplash", "pixabay", "openverse", "wikipedia", "wikimedia", "nasa", "archive"],
    "music": ["jamendo", "openverse", "incompetech", "ccmixter", "archive", "freesound"],
    "sfx": ["openverse", "freesound", "archive"],
}
VIDEO_EXT = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".mts", ".m2ts", ".mxf", ".mpg", ".mpeg"}
AUDIO_EXT = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".aiff", ".aif", ".ogg", ".opus"}
KIND_DIR = {"raw": "raw", "broll": "assets/broll", "image": "assets/images", "photo": "assets/images",
            "logo": "assets/logos", "music": "assets/music", "sfx": "assets/sfx", "font": "assets/fonts",
            "lut": "assets/luts", "ref": "refs", "graphic": "assets/graphics", "video": "assets/broll"}
OK_LICENSES = ("cc0", "pdm", "by", "by-sa", "public domain", "pexels", "pixabay", "unsplash", "nasa")


# ---------- small helpers ----------
def base(p):
    return os.environ.get(f"VS_{p.upper()}_BASE", BASE[p]).rstrip("/")


def load_keys():
    keys = {}
    if KEYS_FILE.exists():
        for line in KEYS_FILE.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                keys[k.strip()] = v.strip().strip('"')
    return {p: os.environ.get(env) or keys.get(env) for p, env in KEY_ENV.items()}


def http_json(url, headers=None, params=None):
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(
            {k: v for k, v in params.items() if v is not None}, doseq=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json", **(headers or {})})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503) and attempt < 2:
                ra = e.headers.get("Retry-After") if e.headers else None
                time.sleep(min(float(ra), 60) if ra and ra.strip().isdigit() else 2 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}: {e.read()[:200]!r}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"cannot reach {urllib.parse.urlsplit(url).netloc}: {e.reason}")


def download(url, dest, headers=None, max_mb=4096):
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(req, timeout=60) as r, open(tmp, "wb") as f:
        ctype = r.headers.get("Content-Type", "")
        size = 0
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            size += len(chunk)
            if size > max_mb * (1 << 20):
                tmp.unlink(missing_ok=True)
                raise RuntimeError(f"{url} is larger than {max_mb} MB; download it manually")
            f.write(chunk)
    tmp.rename(dest)
    return dest, ctype


def slug(s, n=40):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n] or "item"


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(top.stdout.strip() if top.returncode == 0 else os.getcwd()) / "video-studio"


def project_dir(args, hint=None):
    if getattr(args, "library", False):
        return workspace() / "library"
    if getattr(args, "to", None):
        return None
    if getattr(args, "project", None):
        p = workspace() / "projects" / args.project
        if not p.exists():
            die(f"project {args.project} not found (vs new {args.project})")
        return p
    if hint:
        parts = Path(hint).resolve().parts
        if "projects" in parts:
            i = parts.index("projects")
            if len(parts) > i + 1:
                return Path(*parts[: i + 2])
    die("say where it goes: --project <name>, --library, or --to <dir>")


def target_dir(args, kind, hint=None):
    if getattr(args, "to", None):
        return Path(args.to)
    return project_dir(args, hint) / KIND_DIR.get(kind, "assets/misc")


def ledger_add(folder, entry):
    """Record an asset in the nearest assets/credits.json (project or library)."""
    root = Path(folder).resolve()
    while root.name not in ("assets", "raw", "refs") and root.parent != root:
        root = root.parent
    proj = root.parent if root.name in ("assets", "raw", "refs") else Path(folder).resolve()
    led = proj / "assets" / "credits.json"
    data = load_json(led) if led.exists() else {"assets": []}
    data["assets"] = [a for a in data["assets"] if a.get("file") != entry["file"]] + [entry]
    save_json(led, data)
    write_credits_md(led)


def write_credits_md(led):
    data = load_json(led)
    rows = ["# Credits", "", "Assets used in this project, with source and licence. Keep this file with the project;",
            "paste the 'credit line' entries into the video description where attribution is required.", "",
            "| file | kind | source | author | licence | credit line needed |", "|---|---|---|---|---|---|"]
    lines = []
    for a in sorted(data["assets"], key=lambda a: a["file"]):
        need_credit = a.get("attribution_required")
        rows.append(f"| {Path(a['file']).name} | {a.get('kind', '')} | {a.get('page_url') or a.get('source', '')} | "
                    f"{a.get('author') or ''} | {a.get('license') or 'unknown'} | {'yes' if need_credit else 'no'} |")
        if need_credit:
            lines.append(f"- {a['credit_line']}" if a.get("credit_line") else
                         f"- \"{a.get('title') or Path(a['file']).stem}\" by {a.get('author') or 'unknown'} "
                         f"({a.get('license')}) {a.get('page_url') or ''}".rstrip())
    if lines:
        rows += ["", "## Credit lines", *lines]
    Path(led).with_name("CREDITS.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------- providers: each returns a list of normalised results ----------
def r_(**kw):
    kw.setdefault("duration", None)
    kw.setdefault("width", None)
    kw.setdefault("height", None)
    return kw


def pick_size(files, target, orient_portrait):
    """files: [(w, h, url)] -> url whose short side is closest to target, preferring >= target."""
    files = [f for f in files if f[0] and f[1] and f[2]]
    if not files:
        return None
    def score(f):
        short = min(f[0], f[1])
        return (short < target, abs(short - target))
    return sorted(files, key=score)[0]


def s_pexels(q, kind, a, key):
    hdr = {"Authorization": key}
    orient = {"landscape": "landscape", "portrait": "portrait", "square": "square"}.get(a.orientation)
    if kind == "video":
        d = http_json(f"{base('pexels')}/videos/search", hdr,
                      {"query": q, "per_page": a.n, "orientation": orient, "size": "medium"})
        out = []
        for v in d.get("videos", []):
            files = [(f.get("width"), f.get("height"), f.get("link")) for f in v.get("video_files", [])
                     if f.get("file_type") == "video/mp4"]
            out.append(r_(provider="pexels", id=str(v["id"]), title=q, kind="video", duration=v.get("duration"),
                          width=v.get("width"), height=v.get("height"), thumb=v.get("image"), page_url=v.get("url"),
                          author=(v.get("user") or {}).get("name"), author_url=(v.get("user") or {}).get("url"),
                          license="Pexels License", license_url="https://www.pexels.com/license/",
                          attribution_required=False, files=files))
        return out
    d = http_json(f"{base('pexels')}/v1/search", hdr, {"query": q, "per_page": a.n, "orientation": orient})
    return [r_(provider="pexels", id=str(p["id"]), title=p.get("alt") or q, kind="photo", width=p.get("width"),
               height=p.get("height"), thumb=p["src"].get("medium"), page_url=p.get("url"),
               author=p.get("photographer"), author_url=p.get("photographer_url"), license="Pexels License",
               license_url="https://www.pexels.com/license/", attribution_required=False,
               files=[(p.get("width"), p.get("height"), p["src"].get("original")),
                      (int(p.get("width", 0) * 0.5) or None, int(p.get("height", 0) * 0.5) or None, p["src"].get("large2x"))])
            for p in d.get("photos", [])]


def s_pixabay(q, kind, a, key):
    orient = {"landscape": "horizontal", "portrait": "vertical"}.get(a.orientation)
    common = {"key": key, "q": q[:100], "per_page": max(3, min(a.n, 200)), "safesearch": "true"}
    if kind == "video":
        d = http_json(f"{base('pixabay')}/videos/", params=common)
        out = []
        for h in d.get("hits", []):
            vids = h.get("videos", {})
            files = [(v.get("width"), v.get("height"), v.get("url")) for v in vids.values()]
            thumb = next((v.get("thumbnail") for v in vids.values() if v.get("thumbnail")), None)
            out.append(r_(provider="pixabay", id=str(h["id"]), title=h.get("tags") or q, kind="video",
                          duration=h.get("duration"), width=(vids.get("large") or {}).get("width"),
                          height=(vids.get("large") or {}).get("height"), thumb=thumb, page_url=h.get("pageURL"),
                          author=h.get("user"), license="Pixabay Content License",
                          license_url="https://pixabay.com/service/license-summary/", attribution_required=False,
                          files=files))
        return out
    d = http_json(f"{base('pixabay')}/", params={**common, "image_type": "photo", "orientation": orient})
    return [r_(provider="pixabay", id=str(h["id"]), title=h.get("tags") or q, kind="photo",
               width=h.get("imageWidth"), height=h.get("imageHeight"), thumb=h.get("webformatURL"),
               page_url=h.get("pageURL"), author=h.get("user"), license="Pixabay Content License",
               license_url="https://pixabay.com/service/license-summary/", attribution_required=False,
               files=[(h.get("imageWidth"), h.get("imageHeight"), h.get("largeImageURL"))])
            for h in d.get("hits", [])]


def s_unsplash(q, kind, a, key):
    if kind != "photo":
        return []
    orient = {"landscape": "landscape", "portrait": "portrait", "square": "squarish"}.get(a.orientation)
    d = http_json(f"{base('unsplash')}/search/photos", {"Authorization": f"Client-ID {key}"},
                  {"query": q, "per_page": min(a.n, 30), "orientation": orient})
    return [r_(provider="unsplash", id=p["id"], title=p.get("alt_description") or q, kind="photo",
               width=p.get("width"), height=p.get("height"), thumb=p["urls"].get("small"),
               page_url=p["links"].get("html"), author=p["user"].get("name"),
               author_url=p["user"]["links"].get("html"), license="Unsplash License",
               license_url="https://unsplash.com/license", attribution_required=True,
               download_location=p["links"].get("download_location"),
               files=[(p.get("width"), p.get("height"), p["urls"].get("full"))])
            for p in d.get("results", [])]


def s_openverse(q, kind, a, key):
    lic = "commercial,modification" if not a.allow_nc else None
    only = "cc0,pdm" if getattr(a, "cc0", False) else None
    if kind in ("music", "sfx"):
        # Openverse no longer fills "category" for most sound effects, so category=sound_effect matches
        # nothing: search sfx without it and keep them short instead.
        params = {"q": q, "page_size": a.n, "license_type": None if only else lic, "license": only,
                  "category": "music" if kind == "music" else None}
        if a.max_dur:
            params["length"] = "short" if a.max_dur <= 30 else ("medium" if a.max_dur <= 120 else None)
        elif kind == "sfx":
            params["length"] = "short"
        d = http_json(f"{base('openverse')}/audio/", params=params)
        kind_out = kind
    else:
        d = http_json(f"{base('openverse')}/images/", params={"q": q, "page_size": a.n, "license_type": None if only else lic,
                                                              "license": only})
        kind_out = "photo"
    out = []
    for it in d.get("results", []):
        licname = f"CC {it.get('license', '').upper()} {it.get('license_version') or ''}".strip()
        if it.get("license") in ("cc0", "pdm"):
            licname = "CC0 / public domain"
        dur = it.get("duration")
        out.append(r_(provider="openverse", id=it["id"], title=it.get("title") or q, kind=kind_out,
                      duration=(dur / 1000) if dur else None, width=it.get("width"), height=it.get("height"),
                      thumb=it.get("thumbnail") if kind_out == "photo" else None,
                      page_url=it.get("foreign_landing_url"), author=it.get("creator"), author_url=it.get("creator_url"),
                      license=licname, license_url=it.get("license_url"),
                      attribution_required=it.get("license") not in ("cc0", "pdm"),
                      source_site=it.get("source"), files=[(it.get("width") or 1, it.get("height") or 1, it.get("url"))]))
    return out


def s_wikimedia(q, kind, a, key):
    ft = "filetype:video" if kind == "video" else "filetype:bitmap"
    d = http_json(base("wikimedia"), params={
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": a.n,
        "gsrsearch": f"{ft} {q}", "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 320})
    out = []
    for pg in (d.get("query") or {}).get("pages", {}).values():
        ii = (pg.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata") or {}
        lic = (em.get("LicenseShortName") or {}).get("value", "")
        if not a.allow_nc and re.search(r"\bNC\b|\bND\b|non-?commercial", lic, re.I):
            continue
        artist = re.sub(r"<[^>]+>", "", (em.get("Artist") or {}).get("value", "")).strip()
        out.append(r_(provider="wikimedia", id=str(pg.get("pageid")), title=pg.get("title", "").replace("File:", ""),
                      kind=kind, duration=float(ii["duration"]) if ii.get("duration") else None,
                      width=ii.get("width"), height=ii.get("height"), thumb=ii.get("thumburl"),
                      page_url=ii.get("descriptionurl"), author=artist or None, license=lic or "see page",
                      license_url=(em.get("LicenseUrl") or {}).get("value"),
                      attribution_required=not re.search(r"public domain|cc0|pd", lic, re.I),
                      files=[(ii.get("width"), ii.get("height"), ii.get("url"))]))
    return out


def s_freesound(q, kind, a, key):
    flt = 'license:"Creative Commons 0" OR license:"Attribution"' if not a.allow_nc else None
    if a.max_dur or a.min_dur:
        dur = f"duration:[{a.min_dur or 0} TO {a.max_dur or '*'}]"
        flt = f"({flt}) AND {dur}" if flt else dur
    d = http_json(f"{base('freesound')}/search/text/", params={
        "query": q, "token": key, "page_size": a.n, "filter": flt,
        "fields": "id,name,duration,license,username,previews,url,tags"})
    out = []
    for s in d.get("results", []):
        lic = s.get("license", "")
        short = "CC0" if "zero" in lic or "publicdomain" in lic else ("CC BY" if "/by/" in lic else lic)
        out.append(r_(provider="freesound", id=str(s["id"]), title=s.get("name") or q, kind=kind,
                      duration=s.get("duration"), thumb=None, page_url=s.get("url"), author=s.get("username"),
                      license=short, license_url=lic, attribution_required=short != "CC0",
                      tags=", ".join((s.get("tags") or [])[:8]),
                      files=[(1, 1, (s.get("previews") or {}).get("preview-hq-mp3"))]))
    return out


def s_nasa(q, kind, a, key):
    media = "video" if kind == "video" else "image"
    d = http_json(f"{base('nasa')}/search", params={"q": q, "media_type": media})
    out = []
    for it in (d.get("collection") or {}).get("items", [])[: a.n]:
        meta = (it.get("data") or [{}])[0]
        thumb = next((l.get("href") for l in it.get("links", []) if l.get("rel") == "preview"), None)
        out.append(r_(provider="nasa", id=meta.get("nasa_id"), title=meta.get("title") or q, kind=kind,
                      thumb=thumb, page_url=f"https://images.nasa.gov/details/{meta.get('nasa_id')}",
                      author=meta.get("center"), license="NASA media (public domain, no endorsement)",
                      license_url="https://www.nasa.gov/nasa-brand-center/images-and-media/",
                      attribution_required=False, asset_manifest=it.get("href"), files=[]))
    return out


def s_archive(q, kind, a, key):
    """Internet Archive: public-domain and CC films (Prelinger, NASA, newsreels, stock footage), audio, images.
    Two-stage brief search ranked by where the words matched, collection tier and popularity (see archive.py)."""
    media = {"video": "movies", "photo": "image", "music": "audio", "sfx": "audio"}[kind]
    docs = ia.search(q, media, a.n, http_json, licence="stated" if a.allow_nc else "commercial",
                     collections=[c.strip() for c in a.collection.split(",")] if getattr(a, "collection", None) else None)
    out = []
    for doc in docs:
        ident, lic = doc["identifier"], doc["_license"]
        creator = doc.get("creator")
        why = "; ".join(doc["_why"][:3])
        out.append(r_(provider="archive", id=ident, title=doc.get("title") or ident, kind=kind,
                      thumb=f"{base('archive')}/services/img/{ident}", page_url=f"https://archive.org/details/{ident}",
                      author=", ".join(creator) if isinstance(creator, list) else creator, license=lic["label"],
                      license_url=lic["license_url"], commercial_use=lic["commercial_use"],
                      attribution_required=lic["attribution_required"] != "no",
                      duration=ia._num(doc.get("runtime")), year=doc.get("year"), color=ia._flat(doc.get("color")) or None,
                      tier=doc["_tier"], score=doc["_score"],
                      tags=f"tier {doc['_tier']}" + (f"; matched {why}" if why else "") + ("" if doc["_strict"] else " (some words)"),
                      files=[]))
    return out


def archive_file(r, target):
    """Pick the best media file of an archive.org item (closest to target height for video)."""
    meta = http_json(f"{base('archive')}/metadata/{r['id']}")
    files = meta.get("files", [])
    if r["kind"] == "video":
        cands = [f for f in files if f.get("name", "").lower().endswith((".mp4", ".mov", ".m4v", ".ogv", ".webm"))]
        def score(f):
            h = int(f.get("height") or 0) or (480 if "512kb" in f["name"].lower() else 720)
            return (h < min(target, 720), abs(h - target), -int(f.get("size") or 0))
    elif r["kind"] == "photo":
        cands = [f for f in files if f.get("name", "").lower().endswith((".jpg", ".jpeg", ".png", ".tif"))]
        score = lambda f: -int(f.get("size") or 0)  # noqa: E731
    else:
        cands = [f for f in files if f.get("name", "").lower().endswith((".mp3", ".wav", ".flac", ".ogg"))]
        score = lambda f: (not f["name"].lower().endswith((".wav", ".flac")), -int(f.get("size") or 0))  # noqa: E731
    if not cands:
        return None, None
    f = sorted(cands, key=score)[0]
    dur = float(f["length"]) if str(f.get("length", "")).replace(".", "", 1).isdigit() else None
    return f"{base('archive')}/download/{r['id']}/{urllib.parse.quote(f['name'])}", dur


def s_wikipedia(q, kind, a, key):
    """Wikipedia: the images that illustrate articles about the topic (people, places, events, products).
    Licences come from Wikimedia Commons per file."""
    if kind != "photo":
        return []
    api = base("wikipedia").format(lang=a.lang)
    d = http_json(api, params={"action": "query", "format": "json", "generator": "search", "gsrsearch": q,
                               "gsrlimit": 3, "prop": "images", "imlimit": 20})
    titles = []
    for pg in sorted((d.get("query") or {}).get("pages", {}).values(), key=lambda p: p.get("index", 99)):
        for im in pg.get("images", []):
            t = im["title"]
            if re.search(r"\.(jpe?g|png|tiff?|webp)$", t, re.I) and not re.search(r"icon|logo|flag of|symbol|edit-|commons-", t, re.I):
                titles.append(t.split(":", 1)[1])
    titles = list(dict.fromkeys(titles))[: a.n]
    if not titles:
        return []
    info = http_json(base("wikimedia"), params={"action": "query", "format": "json", "prop": "imageinfo",
                                                "titles": "|".join("File:" + t for t in titles),
                                                "iiprop": "url|size|extmetadata", "iiurlwidth": 320})
    out = []
    for pg in (info.get("query") or {}).get("pages", {}).values():
        ii = (pg.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata") or {}
        lic = (em.get("LicenseShortName") or {}).get("value", "")
        if not ii.get("url") or (not a.allow_nc and re.search(r"\bNC\b|\bND\b|non-?commercial|fair use", lic, re.I)):
            continue
        artist = re.sub(r"<[^>]+>", "", (em.get("Artist") or {}).get("value", "")).strip()
        out.append(r_(provider="wikipedia", id=str(pg.get("pageid") or pg.get("title")),
                      title=pg.get("title", "").replace("File:", ""), kind="photo", width=ii.get("width"),
                      height=ii.get("height"), thumb=ii.get("thumburl"), page_url=ii.get("descriptionurl"),
                      author=artist or None, license=lic or "see page", license_url=(em.get("LicenseUrl") or {}).get("value"),
                      attribution_required=not re.search(r"public domain|cc0|pd", lic, re.I),
                      files=[(ii.get("width"), ii.get("height"), ii.get("url"))]))
    return out


def ytdlp_cmd():
    custom = os.environ.get("VS_YTDLP_CMD")  # alternate binary (tests, pinned installs)
    return custom.split() if custom else [sys.executable, "-m", "yt_dlp"]


def s_youtube(q, kind, a, key):
    """YouTube search. Default: only videos the uploader licensed Creative Commons (CC BY, reuse allowed).
    --allow-any-license lists everything, marked 'rights not cleared' (references, commentary, your own uploads)."""
    if kind != "video":
        return []
    if a.allow_any_license:
        target = f"ytsearch{a.n}:{q}"
    else:  # YouTube's own Creative Commons filter
        target = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q) + "&sp=EgIwAQ%253D%253D"
    p = subprocess.run([*ytdlp_cmd(), "--dump-json", "--skip-download", "--no-warnings", "--playlist-end", str(a.n),
                        target], capture_output=True, text=True, timeout=300)
    if p.returncode != 0 and not p.stdout.strip():
        raise RuntimeError(f"yt-dlp search failed: {p.stderr.strip()[-200:]}")
    out = []
    for line in p.stdout.splitlines():
        try:
            v = json.loads(line)
        except json.JSONDecodeError:
            continue
        lic = v.get("license") or ""
        cc = "creative commons" in lic.lower()
        if not cc and not a.allow_any_license:
            continue
        out.append(r_(provider="youtube", id=v.get("id"), title=v.get("title") or q, kind="video",
                      duration=v.get("duration"), width=v.get("width"), height=v.get("height"),
                      thumb=v.get("thumbnail"), page_url=v.get("webpage_url") or f"https://www.youtube.com/watch?v={v.get('id')}",
                      author=v.get("channel") or v.get("uploader"), author_url=v.get("channel_url"),
                      license="CC BY (YouTube)" if cc else "rights not cleared (standard YouTube licence)",
                      license_url="https://creativecommons.org/licenses/by/3.0/" if cc else None,
                      attribution_required=True, rights_cleared=cc, files=[]))
    return out


def music_ok(r, a):
    if a.instrumental and r.get("vocal") is True:
        return False
    if r.get("bpm") and ((a.bpm_min and r["bpm"] < a.bpm_min) or (a.bpm_max and r["bpm"] > a.bpm_max)):
        return False
    return True


def s_jamendo(q, kind, a, key):
    """Jamendo: 500k+ Creative Commons tracks with mood/genre/instrument tags (free client_id)."""
    if kind != "music":
        return []
    params = {"client_id": key, "format": "json", "limit": min(a.n * 2, 200), "search": q,
              "include": "musicinfo licenses", "audioformat": "mp32", "audiodlformat": "mp32"}
    if a.instrumental:
        params["vocalinstrumental"] = "instrumental"
    if not a.allow_nc:
        params.update(ccnc="false", ccnd="false")
    d = http_json(f"{base('jamendo')}/tracks/", params=params)
    out = []
    for t in d.get("results", []):
        lic = t.get("license_ccurl") or ""
        if not a.allow_nc and re.search(r"/by-n[cd]|-nc|-nd", lic):
            continue
        dl = t.get("audiodownload") if t.get("audiodownload_allowed", True) else None
        mi = t.get("musicinfo") or {}
        tags = mi.get("tags") or {}
        out.append(r_(provider="jamendo", id=str(t.get("id")), title=f"{t.get('name')} - {t.get('artist_name')}",
                      kind="music", duration=t.get("duration"), thumb=t.get("image"), page_url=t.get("shareurl"),
                      author=t.get("artist_name"), license=lic_name(lic), license_url=lic,
                      attribution_required="publicdomain" not in lic, vocal=mi.get("vocalinstrumental") == "vocal",
                      tags=", ".join((tags.get("genres") or []) + (tags.get("vartags") or []) + (tags.get("instruments") or []))[:120],
                      speed=mi.get("speed"), files=[(1, 1, dl or t.get("audio"))]))
    return out


def lic_name(url):
    if not url:
        return "unknown"
    if "publicdomain" in url:
        return "Public domain"
    parts = [x for x in url.split("/licenses/")[-1].split("/")[:2] if x]
    return "CC " + " ".join([parts[0].upper(), *parts[1:]]) if parts else url


def mmss(v):
    m = re.match(r"^(\d+):(\d{2})$", str(v or ""))
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


def s_ccmixter(q, kind, a, key):
    """ccMixter: CC-licensed remixes, beds and instrumentals (no key)."""
    if kind != "music":
        return []
    tags = ",".join(t for t in [*q.lower().split(), "instrumental" if a.instrumental else ""] if t)
    params = {"f": "json", "tags": tags, "limit": a.n * 2, "sort": "rank", "type": "any"}
    if not a.allow_nc:
        params["lic"] = "by,sa,s,splus,pd,zero"
    d = http_json(f"{base('ccmixter')}/query", params=params)
    out = []
    for u in d if isinstance(d, list) else d.get("results", []):
        files = u.get("files") or []
        mp3 = next((f for f in files if str(f.get("download_url", "")).lower().endswith(".mp3")), files[0] if files else {})
        lic = u.get("license_url") or ""
        if not a.allow_nc and re.search(r"-nc|-nd|nc-|sampling\+?$", lic):
            continue
        out.append(r_(provider="ccmixter", id=str(u.get("upload_id")), title=f"{u.get('upload_name')} - {u.get('user_name')}",
                      kind="music", duration=mmss((mp3.get("file_format_info") or {}).get("ps")),
                      page_url=u.get("file_page_url"), author=u.get("user_real_name") or u.get("user_name"),
                      license=u.get("license_name") or lic_name(lic), license_url=lic,
                      attribution_required="publicdomain" not in lic and "zero" not in lic,
                      vocal=None if "instrumental" not in (u.get("upload_tags") or "") else False,
                      tags=(u.get("upload_tags") or "").strip(",")[:120], files=[(1, 1, mp3.get("download_url"))]))
    return out


def s_incompetech(q, kind, a, key):
    """Incompetech (Kevin MacLeod): 2,000+ production tracks, CC BY 4.0, searchable by feel/genre/BPM (no key)."""
    if kind != "music":
        return []
    cache = Path.home() / ".cache" / "video-studio" / "incompetech_pieces.json"
    pieces = None
    if cache.exists() and time.time() - cache.stat().st_mtime < 7 * 86400:
        pieces = load_json(cache)
    if pieces is None:
        pieces = http_json(f"{base('incompetech')}/pieces.json")
        save_json(cache, pieces)
    words = [w for w in re.split(r"\W+", q.lower()) if w]
    scored = []
    for pc in pieces:
        hay = " ".join(str(pc.get(k, "")) for k in ("title", "feel", "genre", "instruments", "description")).lower()
        score = sum(hay.count(w) for w in words)
        if score:
            scored.append((score, pc))
    out = []
    for _, pc in sorted(scored, key=lambda x: -x[0]):
        length = str(pc.get("length") or "")
        dur = None
        if re.match(r"^\d+:\d{2}$", length):
            m_, s_ = length.split(":")
            dur = int(m_) * 60 + int(s_)
        try:
            bpm = float(pc.get("bpm")) if pc.get("bpm") else None
        except ValueError:
            bpm = None
        fname = pc.get("filename") or f"{pc.get('title')}.mp3"
        title = pc.get("title") or fname
        out.append(r_(provider="incompetech", id=str(pc.get("uuid") or title), title=f"{title} - Kevin MacLeod",
                      kind="music", duration=dur, page_url="https://incompetech.com/music/royalty-free/music.html",
                      author="Kevin MacLeod", license="CC BY 4.0", license_url="https://creativecommons.org/licenses/by/4.0/",
                      attribution_required=True, bpm=bpm, vocal=False,
                      tags=", ".join(str(pc.get(k)) for k in ("feel", "genre", "instruments") if pc.get(k))[:120],
                      credit_line=f"\"{title}\" Kevin MacLeod (incompetech.com) Licensed under Creative Commons: "
                                  "By Attribution 4.0 License http://creativecommons.org/licenses/by/4.0/",
                      files=[(1, 1, f"{base('incompetech')}/mp3-royaltyfree/{urllib.parse.quote(fname)}")]))
        if len(out) >= a.n * 2:
            break
    return out


SEARCH = {"pexels": s_pexels, "pixabay": s_pixabay, "unsplash": s_unsplash, "openverse": s_openverse,
          "wikimedia": s_wikimedia, "freesound": s_freesound, "nasa": s_nasa, "archive": s_archive,
          "wikipedia": s_wikipedia, "youtube": s_youtube, "jamendo": s_jamendo, "ccmixter": s_ccmixter,
          "incompetech": s_incompetech}


def contact_sheet(results, out_png):
    need("ffmpeg")
    td = Path(tempfile.mkdtemp())
    frames = []
    try:
        for r in results:
            if not r.get("thumb"):
                continue
            try:
                src, _ = download(r["thumb"], td / f"t{r['n']:03d}.img", max_mb=20)
            except Exception:
                continue
            label = f"#{r['n']}  {r['provider']}"
            if r.get("duration"):
                label += f"  {r['duration']:.0f}s"
            if r.get("width"):
                label += f"  {r['width']}x{r['height']}"
            fr = td / f"f{len(frames):03d}.png"
            p = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-frames:v", "1", "-vf",
                                "scale=320:180:force_original_aspect_ratio=decrease,pad=320:200:(ow-iw)/2:20:0x222222,"
                                f"drawtext=text='{label}':x=6:y=3:fontsize=14:fontcolor=white", str(fr)],
                               capture_output=True)
            if p.returncode == 0:
                frames.append(fr)
        if not frames:
            return None
        cols = min(4, len(frames))
        rows = -(-len(frames) // cols)
        Path(out_png).parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-v", "error", "-framerate", "1", "-i", str(td / "f%03d.png"), "-vf",
             f"tile={cols}x{rows}:padding=4:margin=4:color=0x111111", "-frames:v", "1", str(out_png)])
        return out_png
    finally:
        shutil.rmtree(td, ignore_errors=True)


# ---------- commands ----------
def cmd_search(a):
    keys = load_keys()
    kind = a.type
    provs = PROVIDERS[kind] if a.provider == "auto" else a.provider.split(",")
    results, notes = [], []
    for p in provs:
        if p not in SEARCH:
            die(f"unknown provider {p}. Options: {', '.join(SEARCH)}")
        if p in KEY_ENV and not keys.get(p):
            notes.append(f"{p}: no API key (free: `vs keys set {p}`)")
            continue
        try:
            got = SEARCH[p](a.query, kind, a, keys.get(p))
        except RuntimeError as e:
            notes.append(f"{p}: {e}")
            continue
        for r in got:
            if getattr(a, "cc0", False) and r.get("attribution_required", True):
                continue  # --cc0: no credit line, no conditions
            if kind == "music" and not music_ok(r, a):
                continue
            if a.min_dur and r.get("duration") and r["duration"] < a.min_dur:
                continue
            if a.max_dur and r.get("duration") and r["duration"] > a.max_dur:
                continue
            if a.orientation and r.get("width") and r.get("height") and kind in ("video", "photo"):
                o = "portrait" if r["height"] > r["width"] * 1.05 else ("landscape" if r["width"] > r["height"] * 1.05 else "square")
                if o != a.orientation and not a.any_orientation_fallback:
                    continue
            results.append(r)
        if len(results) >= a.n and a.provider == "auto":
            break
    results = results[: a.n * 2]
    for i, r in enumerate(results, 1):
        r["n"] = i
    if a.out:
        out = Path(a.out)
    elif a.project or a.library:
        out = project_dir(a) / "work" / "assets" / f"{slug(a.query)}_{kind}"
    else:
        out = workspace() / "searches" / f"{slug(a.query)}_{kind}"
    save_json(out.with_suffix(".json"), {"query": a.query, "type": kind, "searched": now(), "results": results})
    has_notes = kind in ("video", "photo") and any(r["provider"] == "archive" for r in results)
    lines = [f"# {kind} results for \"{a.query}\"", "",
             "| # | provider | title | dur | size | licence | credit |" + (" why |" if has_notes else ""),
             "|---|---|---|---|---|---|---|" + ("---|" if has_notes else "")]
    if kind in ("music", "sfx"):
        lines[2:4] = ["| # | provider | title | dur | bpm/speed | tags | licence | credit |",
                      "|---|---|---|---|---|---|---|---|"]
    for r in results:
        size = f"{r['width']}x{r['height']}" if r.get("width") and kind in ("video", "photo") else ""
        dur = fmt_ts(r["duration"]) if r.get("duration") else ""
        title = (r.get("title") or "")[:48].replace("|", "/")
        credit = 'yes' if r.get('attribution_required') else 'no'
        if kind in ("music", "sfx"):
            tempo = f"{r['bpm']:.0f}" if r.get("bpm") else (r.get("speed") or "")
            tags = (r.get("tags") or "")[:60].replace("|", "/")
            lines.append(f"| {r['n']} | {r['provider']} | {title} | {dur} | {tempo} | {tags} | {r.get('license')} | {credit} |")
        else:
            notes_ = (r.get("tags") or "")[:70].replace("|", "/") if r["provider"] == "archive" else ""
            lines.append(f"| {r['n']} | {r['provider']} | {title} | {dur} | {size} | {r.get('license')} | {credit} |"
                         + (f" {notes_} |" if has_notes else ""))
    out.with_suffix(".md").write_text("\n".join(lines + ([""] + [f"- {n}" for n in notes] if notes else [])) + "\n",
                                      encoding="utf-8")
    sheet = contact_sheet(results, out.with_suffix(".png")) if kind in ("video", "photo") and results else None
    for n_ in notes:
        print(f"note: {n_}", file=sys.stderr)
    print(f"{len(results)} {kind} results -> {out.with_suffix('.md')}" + (f", sheet {sheet}" if sheet else ""))
    print(f"next: vs fetch get {out.with_suffix('.json')} <numbers>")


def nasa_files(r):
    try:
        urls = http_json(r["asset_manifest"])
    except Exception:
        return []
    want = (".mp4",) if r["kind"] == "video" else (".jpg", ".png")
    good = [u for u in urls if u.lower().endswith(want)]
    rank = ["~orig", "~large", "~medium"] if r["kind"] != "video" else ["~orig", "~large", "~medium", "~mobile"]
    return sorted(good, key=lambda u: next((i for i, t in enumerate(rank) if t in u), 9))[:1]


def archive_result(ident, kind="video"):
    """A result entry for any archive.org item named as archive:<identifier>."""
    return {"n": 1, "provider": "archive", "id": ident, "kind": kind, "title": ident,
            "page_url": f"https://archive.org/details/{ident}"}


def load_results(spec, numbers):
    if spec.startswith("archive:"):
        return {"query": spec, "results": [archive_result(spec.split(":", 1)[1])]}, numbers or [1]
    if not Path(spec).exists():
        die(f"results file not found: {spec} (run vs fetch search first, or pass archive:<identifier>)")
    return load_json(spec), numbers


def archive_get(n_, r, folder, a, data):
    """Archive video: the best rendition (or --file), and with --section a verified re-encoded cut + provenance."""
    it = ia.item(http_json, r["id"])
    g, f = ia.pick_file(it, a.file)
    url = ia.file_url(r["id"], f["name"])
    lic = it["license"]
    r.update(title=it["title"], author=it["creator"], license=lic["label"], license_url=lic["license_url"],
             commercial_use=lic["commercial_use"], attribution_required=lic["attribution_required"] != "no")
    stem = f"archive_{slug(r['id'], 24)}_{slug(it['title'], 30)}"
    if not a.section:
        dest = folder / f"{stem}{Path(f['name']).suffix.lower() or '.mp4'}"
        download(url, dest)
        return dest, url, None
    need("ffmpeg")
    t0, t1 = parse_section(a.section)
    length = f["length"] or g["best"]["length"]
    if length and t0 >= length:
        raise RuntimeError(f"section starts at {t0:.1f} s but {f['name']} is {length:.1f} s long")
    dest = folder / f"{stem}_{t0:07.2f}-{t1:07.2f}.mp4"
    checked = ia.cut(url, t0, t1 - t0, dest, UA, audio=not a.no_audio, source_length=length)
    prov = ia.provenance(it, f, t0, checked["asked"], dest, UA, checked)
    dest.with_suffix(".provenance.json").write_text(json.dumps(prov, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    r["credit_line"] = prov["attribution_text"]
    print(f"#{n_}: cut {checked['duration']:.3f} s (asked {checked['asked']:.3f} s, 0 decode errors) from {f['name']}")
    return dest, url, prov


def cmd_get(a):
    data, a.numbers = load_results(a.results, a.numbers)
    if not a.numbers:
        die("which results? e.g. vs fetch get <results.json> 2 5")
    by_n = {r["n"]: r for r in data["results"]}
    keys = load_keys()
    target = {"sd": 720, "hd": 1080, "4k": 2160}[a.quality]
    for n_ in a.numbers:
        r = by_n.get(n_)
        if not r:
            print(f"#{n_}: not in results", file=sys.stderr)
            continue
        kind = a.kind or {"video": "broll", "photo": "image", "music": "music", "sfx": "sfx"}[r["kind"]]
        folder = target_dir(a, kind, hint=a.results)
        if r["provider"] == "youtube":
            if not r.get("rights_cleared") and not a.i_have_rights:
                print(f"#{n_}: not Creative Commons. Re-run with --i-have-rights only if the person owns or licensed it "
                      "(or use --as ref to keep it as a reference)", file=sys.stderr)
                if kind != "ref":
                    continue
            dest = yt_get(r, folder, a, data)
            if not dest:
                continue
            log_and_report(n_, r, dest, kind, r["page_url"], data)
            continue
        if r["provider"] == "archive" and r["kind"] == "video":
            try:
                dest, url, prov = archive_get(n_, r, folder, a, data)
            except Exception as e:
                print(f"#{n_}: {e}", file=sys.stderr)
                continue
            log_and_report(n_, r, dest, kind, url, data, prov)
            continue
        if r["provider"] == "nasa":
            urls = nasa_files(r)
            url = urls[0] if urls else None
        elif r["provider"] == "archive":
            try:
                url, _ = archive_file(r, target)
            except RuntimeError as e:
                print(f"#{n_}: {e}", file=sys.stderr)
                continue
        else:
            best = pick_size(r.get("files", []), target, False)
            url = best[2] if best else None
        if not url:
            print(f"#{n_}: no downloadable file", file=sys.stderr)
            continue
        ext = Path(urllib.parse.urlsplit(url).path).suffix.lower() or (".mp4" if r["kind"] == "video" else ".jpg")
        if ext not in VIDEO_EXT | AUDIO_EXT | IMAGE_EXT:
            ext = {"video": ".mp4", "photo": ".jpg"}.get(r["kind"], ".mp3")
        dest = folder / f"{r['provider']}_{slug(str(r['id']), 24)}_{slug(r.get('title') or data['query'], 30)}{ext}"
        try:
            if r["provider"] == "unsplash" and r.get("download_location") and keys.get("unsplash"):
                http_json(r["download_location"], {"Authorization": f"Client-ID {keys['unsplash']}"})  # API terms
            if a.section and ext in VIDEO_EXT | AUDIO_EXT:
                dest = section_get(url, dest, a.section)
            else:
                download(url, dest)
        except Exception as e:
            print(f"#{n_}: download failed: {e}", file=sys.stderr)
            continue
        log_and_report(n_, r, dest, kind, url, data)


def log_and_report(n_, r, dest, kind, url, data, prov=None):
    entry = {k: r.get(k) for k in ("provider", "id", "title", "author", "author_url", "page_url", "license",
                                    "license_url", "attribution_required", "commercial_use", "credit_line")}
    entry.update(file=str(dest), kind=kind, source=url, downloaded=now(), query=data["query"])
    if prov:
        entry.update(segment=prov["segment"], source_file=prov["source"]["file"], source_md5=prov["source"]["file_md5"],
                     clip_sha256=prov["clip_sha256"], provenance=str(dest.with_suffix(".provenance.json")))
    ledger_add(dest.parent, entry)
    info = probe(str(dest)) if dest.suffix.lower() not in IMAGE_EXT else {}
    extra = (f" {fmt_ts(info['duration'])}" + (f" {info['width']}x{info['height']}" if info.get("width") else "")) \
        if info.get("duration") else ""
    print(f"#{n_} -> {dest}{extra}  [{r.get('license')}]")


def cmd_inspect(a):
    """Look inside an archive.org film before cutting: scenes with timings + a keyframe sheet (or a clip list)."""
    need("ffmpeg")
    if a.results.startswith("archive:"):
        ident = a.results.split(":", 1)[1]
    else:
        data, _ = load_results(a.results, [])
        r = {x["n"]: x for x in data["results"]}.get(a.number)
        if not r:
            die(f"#{a.number} is not in {a.results}")
        if r["provider"] != "archive" or r["kind"] != "video":
            die(f"#{a.number} is a {r['provider']} {r['kind']} result; inspect works on Internet Archive videos")
        ident = r["id"]
    hint = None if a.results.startswith("archive:") else a.results
    if a.out:
        out = Path(a.out)
    else:
        where_ = (Path(a.to) if a.to else project_dir(a, hint) / "work" / "assets" if (a.project or a.library or hint)
                  else workspace() / "searches")
        out = where_ / f"inspect_{slug(ident, 40)}"
    window = parse_section(a.window) if a.window else None
    data, png = ia.inspect(http_json, download, ident, out, UA, name=a.file, window=window, page=a.page)
    n = len(data.get("scenes") or data.get("clips") or [])
    print(f"{data['mode']}: {n} {'scenes' if data['mode'] == 'scenes' else 'clips'} -> {out.with_suffix('.md')}"
          + (f", sheet {png}" if png else ""))
    print(f"licence: {data['license']['label']} (commercial use {data['license']['commercial_use']})")


def parse_section(sec):
    a_, _, b_ = sec.partition("-")
    def secs(x):
        parts = [float(p) for p in x.split(":")]
        return sum(v * 60 ** i for i, v in enumerate(reversed(parts)))
    return secs(a_), secs(b_)


def section_get(url, dest, section):
    """Grab only [a, b] of a remote video/audio (HTTP range reads; the whole film never downloads)."""
    need("ffmpeg")
    t0, t1 = parse_section(section)
    dest = dest.with_name(f"{dest.stem}_{int(t0)}-{int(t1)}{dest.suffix}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-v", "error", "-user_agent", UA, "-ss", f"{t0:.3f}", "-i", url, "-t", f"{t1 - t0:.3f}",
         "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", str(dest)])
    return dest


def yt_get(r, folder, a, data):
    folder.mkdir(parents=True, exist_ok=True)
    h = {"sd": 720, "hd": 1080, "4k": 2160}[a.quality]
    stem = f"youtube_{slug(str(r['id']), 16)}_{slug(r.get('title') or data['query'], 30)}"
    cmd = [*ytdlp_cmd(), "-f", f"bv*[height<={h}]+ba/b[height<={h}]/b", "--merge-output-format", "mp4",
           "--no-playlist", "-o", str(folder / f"{stem}.%(ext)s")]
    if a.section:
        t0, t1 = parse_section(a.section)
        cmd += ["--download-sections", f"*{t0}-{t1}", "--force-keyframes-at-cuts"]
    p = subprocess.run(cmd + [r["page_url"]], text=True)
    if p.returncode != 0:
        print(f"youtube {r['id']}: download failed", file=sys.stderr)
        return None
    got = sorted(folder.glob(f"{stem}.*"), key=lambda f: f.stat().st_mtime)
    return got[-1] if got else None


def classify(path):
    ext = path.suffix.lower()
    name = path.name.lower()
    if ext in {".ttf", ".otf", ".woff", ".woff2"}:
        return "font"
    if ext in {".cube", ".3dl"}:
        return "lut"
    if ext in IMAGE_EXT or ext in {".svg", ".gif"}:
        return "logo" if "logo" in name else "image"
    if ext in AUDIO_EXT:
        try:
            return "sfx" if probe(str(path))["duration"] < 12 else "music"
        except SystemExit:
            return "music"
    if ext in VIDEO_EXT:
        return "raw"
    return None


def place(src, folder, mode):
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / src.name
    i = 1
    while dest.exists() and not dest.samefile(src):
        dest = folder / f"{src.stem}_{i}{src.suffix}"
        i += 1
    if dest.exists():
        return dest
    if mode == "link":
        dest.symlink_to(src.resolve())
    else:
        shutil.copy2(src, dest)
    return dest


def safe_extract(zpath, into):
    with zipfile.ZipFile(zpath) as z:
        for m in z.infolist():
            target = (into / m.filename).resolve()
            if not str(target).startswith(str(into.resolve())):
                die(f"refusing unsafe path in zip: {m.filename}")
        z.extractall(into)


def add_local(path, a, origin, added):
    if path.is_dir():
        for f in sorted(path.rglob("*")):
            if f.is_file() and not f.name.startswith("."):
                add_local(f, a, origin, added)
        return
    if path.suffix.lower() == ".zip":
        td = Path(tempfile.mkdtemp(prefix="vs-zip-"))
        try:
            safe_extract(path, td)
            add_local(td, a, origin or str(path), added)
        finally:
            shutil.rmtree(td, ignore_errors=True)
        return
    kind = a.kind or classify(path)
    if not kind:
        return
    folder = target_dir(a, kind)
    # Downloads/zip contents are copied out of temp; local footage is linked (no duplicate GBs) unless --copy.
    is_video = path.suffix.lower() in VIDEO_EXT
    mode = "copy" if (a.copy or origin) else ("link" if (a.link or is_video) else "copy")
    dest = place(path, folder, mode)
    ledger_add(folder, {"file": str(dest), "kind": kind, "source": origin or str(path.resolve()),
                        "license": a.license or ("provided by editor" if not origin or not origin.startswith("http")
                                                 else "unknown: provided by editor, confirm rights"),
                        "author": a.credit, "attribution_required": bool(a.credit), "downloaded": now(),
                        "title": path.stem})
    added.append((kind, dest))


def fetch_url(url, a, added):
    td = Path(tempfile.mkdtemp(prefix="vs-dl-"))
    host = urllib.parse.urlsplit(url).netloc.lower()
    try:
        if "drive.google.com" in host or "docs.google.com" in host:
            try:
                import gdown
            except ImportError:
                die("Google Drive links need gdown. Run: vs setup")
            if "/folders/" in url:
                gdown.download_folder(url, output=str(td), quiet=False, use_cookies=False)
            else:
                gdown.download(url, output=str(td) + "/", quiet=False, fuzzy=True)
        elif "dropbox.com" in host:
            u = re.sub(r"([?&])dl=0", r"\1dl=1", url)
            u = u if "dl=1" in u else u + ("&" if "?" in u else "?") + "dl=1"
            name = Path(urllib.parse.urlsplit(url).path).name or "dropbox_download"
            download(u, td / name)
        elif Path(urllib.parse.urlsplit(url).path).suffix.lower() in VIDEO_EXT | AUDIO_EXT | IMAGE_EXT | {".zip", ".cube", ".ttf", ".otf"}:
            download(url, td / Path(urllib.parse.urlsplit(url).path).name)
        else:
            # A page (YouTube, Vimeo, Instagram, TikTok, X, news sites ...): yt-dlp.
            cmd = [sys.executable, "-m", "yt_dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
                   "--merge-output-format", "mp4", "-o", str(td / "%(title).60s [%(id)s].%(ext)s", ), "--no-playlist"]
            if a.cookies_from_browser:
                cmd += ["--cookies-from-browser", a.cookies_from_browser]
            p = subprocess.run(cmd + [url], text=True)
            if p.returncode != 0 and "instagram.com" in host:
                from watch import instagram_embed  # public embed page: caption + video, no login
                f, _ = instagram_embed(url, td)
                if f:
                    p = subprocess.CompletedProcess(cmd, 0)
            if p.returncode != 0:
                die("yt-dlp could not fetch that page. Logged-in content (Instagram, TikTok, private videos) needs "
                    "--cookies-from-browser chrome|safari|firefox, or save the file and `vs add` it.")
        files = [f for f in td.rglob("*") if f.is_file() and not f.name.endswith(".part")]
        if not files:
            die(f"nothing downloaded from {url}")
        for f in files:
            add_local(f, a, url, added)
    finally:
        shutil.rmtree(td, ignore_errors=True)


def cmd_add(a):
    added = []
    for item in a.inputs:
        if re.match(r"^https?://", item):
            fetch_url(item, a, added)
        else:
            p = Path(item).expanduser()
            if not p.exists():
                die(f"not found: {item}")
            add_local(p, a, None, added)
    if not added:
        die("nothing importable found (media, images, fonts, LUTs, zips)")
    by_kind = {}
    for k, d in added:
        by_kind.setdefault(k, []).append(d)
    for k, ds in by_kind.items():
        print(f"{k}: {len(ds)} -> {ds[0].parent}")
        for d in ds[:12]:
            print(f"   {d.name}")
        if len(ds) > 12:
            print(f"   ... +{len(ds) - 12} more")
    if any(k in ("raw", "broll") for k, _ in added):
        print("next: vs ingest <project>/raw -o <project>/work/media   (or assets/broll)")


def cmd_keys(a):
    KEYS_FILE.parent.mkdir(parents=True, exist_ok=True)
    cur = {}
    if KEYS_FILE.exists():
        for line in KEYS_FILE.read_text().splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                cur[k.strip()] = v.strip()
    if a.action == "list":
        env_keys = load_keys()
        for p, env in KEY_ENV.items():
            v = env_keys.get(p)
            print(f"{p:10} {'set (' + v[:4] + '…)' if v else 'not set'}   {env}")
        print("no key needed: openverse, archive, wikipedia, wikimedia, youtube (CC), incompetech, ccmixter, nasa")
        return
    if a.provider not in KEY_ENV:
        die(f"provider must be one of {', '.join(KEY_ENV)}")
    env = KEY_ENV[a.provider]
    if a.action == "unset":
        cur.pop(env, None)
    else:
        val = a.value or (sys.stdin.readline().strip() if not sys.stdin.isatty() else getpass.getpass(f"{env}: "))
        if not val:
            die("empty key")
        cur[env] = val
    KEYS_FILE.write_text("".join(f"{k}={v}\n" for k, v in cur.items()))
    os.chmod(KEYS_FILE, 0o600)
    print(f"{a.provider}: {'removed' if a.action == 'unset' else 'saved'} in {KEYS_FILE}")


def cmd_credits(a):
    led = project_dir(a) / "assets" / "credits.json"
    if not led.exists():
        die(f"no assets logged yet ({led})")
    write_credits_md(led)
    print(led.with_name("CREDITS.md").read_text())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def where(p):
        p.add_argument("--project")
        p.add_argument("--library", action="store_true", help="workspace-wide library (logos, fonts, music beds)")
        p.add_argument("--to", help="explicit destination folder")

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--type", choices=["video", "photo", "music", "sfx"], default="video")
    s.add_argument("--provider", default="auto", help="auto or comma list: " + ",".join(SEARCH))
    s.add_argument("--orientation", choices=["landscape", "portrait", "square"])
    s.add_argument("--any-orientation-fallback", action="store_true", help="keep other orientations too")
    s.add_argument("--min-dur", type=float)
    s.add_argument("--max-dur", type=float)
    s.add_argument("--n", type=int, default=12)
    s.add_argument("--allow-nc", action="store_true", help="include NonCommercial/NoDerivs licences (personal projects)")
    s.add_argument("--cc0", action="store_true",
                   help="only CC0 / public domain: free to use anywhere, no credit needed (client ads)")
    s.add_argument("--allow-any-license", action="store_true",
                   help="YouTube: list all results, not only Creative Commons (references; rights not cleared)")
    s.add_argument("--lang", default="en", help="Wikipedia language edition (en, de, fr, ...)")
    s.add_argument("--instrumental", action="store_true", help="music: no vocals (background beds under speech)")
    s.add_argument("--bpm-min", type=float)
    s.add_argument("--bpm-max", type=float)
    s.add_argument("--collection", help="archive.org: only these collections, e.g. prelinger,nasa")
    s.add_argument("-o", "--out", help="output path without extension")
    where(s)
    g = sub.add_parser("get")
    g.add_argument("results")
    g.add_argument("numbers", nargs="*", type=int)
    g.add_argument("--quality", choices=["sd", "hd", "4k"], default="hd")
    g.add_argument("--as", dest="kind", choices=sorted(KIND_DIR))
    g.add_argument("--section", help="only this part of a long video/audio, source time: 95-110 or 1:35-1:50")
    g.add_argument("--i-have-rights", action="store_true",
                   help="download a non-CC YouTube result because the person owns/licensed it")
    g.add_argument("--file", help="archive.org: which video file of the item (from vs fetch inspect)")
    g.add_argument("--no-audio", action="store_true", help="archive.org cuts: picture only")
    where(g)
    i = sub.add_parser("inspect", help="scenes + keyframes of an Internet Archive film before cutting")
    i.add_argument("results", help="results JSON from vs fetch search, or archive:<identifier>")
    i.add_argument("number", nargs="?", type=int, default=1)
    i.add_argument("--file", help="a video file of the item (multi-clip items list them)")
    i.add_argument("--window", help="source range to scan, max 15 min: 4:00-9:00 (default: the first 15 min)")
    i.add_argument("--page", type=int, default=1, help="multi-clip items: which page of 60 clips")
    i.add_argument("-o", "--out", help="output path without extension")
    where(i)
    d = sub.add_parser("add")
    d.add_argument("inputs", nargs="+")
    d.add_argument("--as", dest="kind", choices=sorted(KIND_DIR))
    d.add_argument("--copy", action="store_true", help="copy local footage instead of linking it")
    d.add_argument("--link", action="store_true", help="symlink instead of copying")
    d.add_argument("--license", help="licence/rights note to record")
    d.add_argument("--credit", help="credit line (author) to record")
    d.add_argument("--cookies-from-browser", help="for logged-in pages via yt-dlp: chrome, safari, firefox")
    where(d)
    k = sub.add_parser("keys")
    k.add_argument("action", choices=["set", "unset", "list"])
    k.add_argument("provider", nargs="?")
    k.add_argument("value", nargs="?", help="omit to be prompted (keeps it out of shell history)")
    c = sub.add_parser("credits")
    where(c)
    a = ap.parse_args()
    {"search": cmd_search, "get": cmd_get, "inspect": cmd_inspect, "add": cmd_add, "keys": cmd_keys,
     "credits": cmd_credits}[a.cmd](a)


if __name__ == "__main__":
    main()
