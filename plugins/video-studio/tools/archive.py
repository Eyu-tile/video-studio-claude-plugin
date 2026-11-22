#!/usr/bin/env python3
"""Internet Archive footage: brief-driven search, exact licence labels, item files, look-before-you-cut
inspection (scenes + keyframes read over HTTPS) and verified frame-accurate cuts with provenance.

Approach and numbers adapted from broll-mcp (MIT, https://github.com/edigeh/broll-mcp): two-stage query
(all terms, then any term) over title/subject/description/shotlist, collection trust tiers, exact licence URL
table, format ranking for the file to cut, rendition grouping by the `original` chain, scene normalising
(merge < 1.5 s, split takes > 20 s every 10 s, cap 120), cut verify (duration within 0.1 s, zero decode errors).

Used by `vs fetch search --provider archive`, `vs fetch inspect` and `vs fetch get`.
"""
import hashlib
import json
import math
import re
import shutil
import subprocess
import tempfile
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://archive.org"
# --- licences: exact URL table, nothing guessed -------------------------------------------------------------
_CC = {"by": ("CC BY", "allowed", "yes"), "by-sa": ("CC BY-SA", "allowed", "yes"),
       "by-nd": ("CC BY-ND", "allowed", "yes"), "by-nc": ("CC BY-NC", "not_allowed", "yes"),
       "by-nc-sa": ("CC BY-NC-SA", "not_allowed", "yes"), "by-nc-nd": ("CC BY-NC-ND", "not_allowed", "yes")}
LICENSES = {
    "creativecommons.org/licenses/publicdomain": ("Public domain (CC PD dedication)", "allowed", "no"),
    "creativecommons.org/publicdomain/zero/1.0": ("CC0 1.0", "allowed", "no"),
    "creativecommons.org/publicdomain/mark/1.0": ("Public Domain Mark 1.0", "allowed", "no"),
    **{f"creativecommons.org/licenses/{k}/{v}": (f"{n} {v}", c, at)
       for k, (n, c, at) in _CC.items() for v in ("1.0", "2.0", "2.5", "3.0", "4.0")},
}
# Lucene treats an unescaped "/" as a regex delimiter; archive.org answers BACKEND_ERROR to `*licenses/by/*`.
LICENSE_CLAUSE = {
    "commercial": r"licenseurl:(*publicdomain* OR *\/by\/* OR *\/by-sa\/*)",            # default: no NC, no ND
    "stated": "(licenseurl:* OR rights:*)",                                              # --allow-nc
}


def license_info(url, rights=None):
    url = url.strip() if isinstance(url, str) and url.strip() else None
    rights = " ".join(rights) if isinstance(rights, list) else rights
    if not url:
        return {"label": "unknown (rights statement only)" if rights else "unknown", "license_url": None,
                "commercial_use": "unknown", "attribution_required": "unknown", "rights_statement": rights}
    key = re.sub(r"^(https?://)?(www\.)?", "", url.lower()).rstrip("/")
    label, commercial, attrib = LICENSES.get(key, ("unrecognized", "unknown", "unknown"))
    return {"label": label, "license_url": url, "commercial_use": commercial, "attribution_required": attrib,
            "rights_statement": rights}


# --- search ---------------------------------------------------------------------------------------------------
TIERS = {"prelinger": 1, "nasa": 1, "stock_footage": 2, "feature_films": 2}
PLAYABLE = ("h.264", "h.264 IA", "512Kb MPEG4", "MPEG4")
STOP = set("""a an the of in on at to for with and or by from into onto over under is are be as its it this that some
very who while their his her them up down out off near about close closeup wide medium view look style vintage old
seconds sec b roll broll footage shot shots clip clips cinematic video film scene scenes stock angle slow motion hd 4k
""".split())
BW = re.compile(r"\b(black[\s-]*(and|&)[\s-]*white|b\s*&\s*w|b/w|monochrome)\b")
BW_VALUE = re.compile(r"black|\bb\s*&\s*w\b|\bb/w\b|\bbw\b|monochrome|\bp&b\b")
COLOR_CLAUSE = {"bw": 'color:(black OR "b&w" OR "b/w" OR bw OR "black&white" OR blackandwhite OR monochrome)',
                "color": "color:(color OR colour OR colored OR coloured OR colorized OR technicolor OR c)"}
DECADE = re.compile(r"^(1[89]\d0|20[0-2]0)s$")


def brief_terms(brief):
    """'8 seconds of children eating bananas, black and white 1950s footage' -> terms, decade, wants_bw."""
    low = brief.lower()
    wants_bw = bool(BW.search(low))
    words = re.findall(r"[a-z0-9]+", BW.sub(" ", low).replace("b-roll", " "))
    terms, decade = [], None
    for w in words:
        if DECADE.match(w):
            decade = decade or int(w[:4])
        elif w not in STOP and len(w) > 1 and not (w.isdigit() and len(w) != 4) and w not in terms:
            terms.append(w)
    return terms[:6], decade, wants_bw


def build_query(terms, media, strict, licence="commercial", decade=None, color=None, collections=None):
    q = [f"mediatype:{media}"]
    if media == "movies":
        q.append("(" + " OR ".join(f'format:"{f}"' for f in PLAYABLE) + ")")
    if licence in LICENSE_CLAUSE:
        q.append(LICENSE_CLAUSE[licence])
    if color in COLOR_CLAUSE:
        q.append(COLOR_CLAUSE[color])
    if decade:
        q.append(f"year:[{decade} TO {decade + 9}]")
    if collections:
        q.append("collection:(" + " OR ".join(collections) + ")")
    if terms:
        if strict:
            q.append("(" + " AND ".join(f"(title:{t} OR subject:{t} OR description:{t} OR shotlist:{t})" for t in terms) + ")")
        else:
            any_ = " OR ".join(terms)
            q.append(f"(title:({any_}) OR subject:({any_}) OR description:({any_}) OR shotlist:({any_}))")
    return " AND ".join(q)


def _flat(v):
    return " ".join(map(str, v)) if isinstance(v, list) else str(v or "")


def score(doc, terms, tier, wants_bw, strict):
    """title 3 · subject 2 · shotlist 1 · description-only 1 (strict hits) + tier 3/1.5 + log10(downloads)/2
    + 1 for h.264 + 2 for black and white when asked. Returns (score, why)."""
    title, subj, shot = (_flat(doc.get(k)).lower() for k in ("title", "subject", "shotlist"))
    s, why = 0.0, []
    for t in terms:
        pat = re.compile(rf"\b{re.escape(t)}")
        for text, pts, where in ((title, 3, "title"), (subj, 2, "subject"), (shot, 1, "shotlist")):
            if pat.search(text):
                s += pts
                why.append(f"{where} '{t}'")
                break
        else:
            if strict:
                s += 1
                why.append(f"description '{t}'")
    s += {1: 3.0, 2: 1.5}.get(tier, 0.0)
    try:
        s += math.log10(max(1.0, float(doc.get("downloads") or 0))) / 2
    except (TypeError, ValueError):
        pass
    fmts = doc.get("format") or []
    fmts = fmts if isinstance(fmts, list) else [fmts]
    if any(f in ("h.264", "h.264 IA") for f in fmts):
        s += 1
    if wants_bw and BW_VALUE.search(_flat(doc.get("color")).lower()):
        s += 2
        why.append("black and white")
    return round(s, 2), why


FIELDS = ["identifier", "title", "creator", "year", "date", "licenseurl", "rights", "runtime", "subject", "color",
          "downloads", "format"]


def search(brief, media, n, http_json, licence="commercial", color=None, collections=None, log=None):
    """Two-stage search (all terms; then any term if that found fewer than n), ranked locally.
    Returns docs with _score, _why, _tier, _license, _strict."""
    terms, decade, wants_bw = brief_terms(brief)
    if not terms:
        raise RuntimeError(f"'{brief}' has no searchable words once shot words (footage, cinematic, b-roll...) are "
                           "removed; describe what is visible, e.g. 'aerial farmland'")
    color = color or ("bw" if wants_bw and media == "movies" else None)
    rows = max(n * 4, 40)
    docs, seen = [], set()
    for strict in (True, False):
        if not strict and len(docs) >= n:
            break
        q = build_query(terms, media, strict, licence, decade, color, collections)
        d = archive_json(http_json, "/advancedsearch.php", {"q": q, "fl[]": FIELDS + ([] if strict else ["shotlist"]),
                                                            "rows": rows, "output": "json",
                                                            "sort[]": ["downloads desc", "identifier asc"]})
        if "error" in d:
            raise RuntimeError(f"archive.org search error: {d['error']}")
        for doc in d.get("response", {}).get("docs", []):
            if doc["identifier"] not in seen:
                seen.add(doc["identifier"])
                docs.append(dict(doc, _strict=strict))
        if log:
            log(f"archive {'all' if strict else 'any'}-terms query: {d.get('response', {}).get('numFound', 0)} found")
    tiers = _tiers(http_json, [d["identifier"] for d in docs])
    for doc in docs:
        doc["_tier"] = tiers.get(doc["identifier"], 3)
        doc["_score"], doc["_why"] = score(doc, terms, doc["_tier"], wants_bw, doc["_strict"])
        doc["_license"] = license_info(doc.get("licenseurl"), doc.get("rights"))
    docs.sort(key=lambda d: (not d["_strict"], -d["_score"]))
    return docs[:n]


def _tiers(http_json, ids):
    """Collection tier per id from an id-only membership query (popular items list hundreds of fav-* collections,
    so `collection` is never fetched with the results)."""
    out = {}
    for tier in (1, 2):
        names = [c for c, t in TIERS.items() if t == tier]
        chunk = [i for i in ids if i not in out]
        if not chunk:
            break
        q = "identifier:(" + " OR ".join(f'"{i}"' for i in chunk) + ") AND collection:(" + " OR ".join(names) + ")"
        try:
            d = archive_json(http_json, "/advancedsearch.php", {"q": q, "fl[]": ["identifier"], "rows": len(chunk),
                                                                "output": "json"})
        except RuntimeError:
            continue
        for doc in d.get("response", {}).get("docs", []):
            out[doc["identifier"]] = tier
    return out


_last = [0.0]


def archive_json(http_json, path, params=None):
    """archive.org asks bots for at most about 1 request a second."""
    wait = 1.0 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    return http_json(BASE + path, params=params)


# --- items and files ---------------------------------------------------------------------------------------------
CUT_RANK = {"h.264": 1, "h.264 IA": 1, "h.264 MPEG4": 2, "MPEG4": 2, "512Kb MPEG4": 3}   # cut automatically
NAMED_ONLY = {"HiRes MPEG4": 4, "MPEG2": 4, "QuickTime": 4, "Matroska": 4}             # cut only when named
SCAN_FORMAT = "512Kb MPEG4"                                                              # cheap file to scan
TRANSCRIPTS = {"SubRip", "Web Video Text Tracks", "Whisper ASR JSON"}


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        m = re.fullmatch(r"(\d+):(\d{1,2})(?::(\d{1,2}))?(?:\.\d+)?", str(v or "").strip())
        if m:
            a, b, c = m.groups()
            return int(a) * 3600 + int(b) * 60 + int(c) if c else int(a) * 60 + int(b)
        return None


def _stem(name):
    base = name.rsplit("/", 1)[-1]
    return base.rsplit(".", 1)[0] if "." in base else base


def video_groups(files):
    """Renditions of one video grouped by following each derivative's `original` chain to its root file.
    Each group: {root, files: [...], best, scan}. Items with many groups are multi-clip (stock footage reels)."""
    by_name = {f.get("name"): f for f in files if f.get("name")}

    def root_of(name):
        seen = set()
        while name in by_name and by_name[name].get("original") and name not in seen:
            seen.add(name)
            name = by_name[name]["original"]
        return name

    groups = {}
    for f in files:
        fmt = f.get("format") or ""
        rank = CUT_RANK.get(fmt) or NAMED_ONLY.get(fmt)
        if not rank or not f.get("name"):
            continue
        vf = {"name": f["name"], "format": fmt, "rank": rank, "length": _num(f.get("length")),
              "width": int(_num(f.get("width")) or 0) or None, "height": int(_num(f.get("height")) or 0) or None,
              "size": int(_num(f.get("size")) or 0) or None, "md5": f.get("md5"), "source": f.get("source")}
        groups.setdefault(root_of(f["name"]), []).append(vf)
    groups = _merge_renditions(groups, by_name)
    out = []
    for root, fs in sorted(groups.items()):
        cuttable = [f for f in fs if f["rank"] <= 3]
        if not cuttable:
            continue
        best = min(cuttable, key=lambda f: (f["rank"], -(f["width"] or 0) * (f["height"] or 0)))
        scan = next((f for f in fs if f["format"] == SCAN_FORMAT and f["length"] and best["length"]
                     and abs(f["length"] - best["length"]) < 0.5), best)
        out.append({"root": root, "files": fs, "best": best, "scan": scan})
    return out


# `<shot>.mts-mp430-272` and `<shot>.mts-mp430-360` are two encodes of one shot uploaded as separate originals.
RENDITION = re.compile(r"^(?P<shot>.+?)(?:[-_][A-Za-z]+\d*)?[-_](?P<height>\d{3,4})p?$")
RENDITION_TOLERANCE = 1.5  # largest length gap seen between encodes of one shot: 1.34 s


def _merge_renditions(groups, by_name):
    """Merge groups whose root names differ only by a height suffix that is the file's real height, when every
    length in the merged group agrees within 1.5 s. Anything else stays a separate clip."""
    clusters, out = {}, {}
    for root, fs in groups.items():
        folder, _, base = root.rpartition("/")
        m = RENDITION.match(_stem(base))
        h = _num((by_name.get(root) or {}).get("height"))
        if m and h and int(h) == int(m.group("height")):
            clusters.setdefault(f"{folder}/{m.group('shot')}", []).append(root)
        else:
            out[root] = fs
    for roots in clusters.values():
        lengths = [f["length"] for r in roots for f in groups[r]]
        if len(roots) < 2 or None in lengths or max(lengths) - min(lengths) > RENDITION_TOLERANCE:
            out.update({r: groups[r] for r in roots})
        else:
            out[roots[0]] = [f for r in roots for f in groups[r]]
    return out


def thumbs_for(ident, files, group):
    """Archive-made thumbnails `{id}.thumbs/{stem}_{NNNNNN}.jpg` (NNNNNN = seconds) for one group."""
    stems = {_stem(f["name"]) for f in group["files"]} | {_stem(group["root"])}
    out = []
    for f in files:
        name = f.get("name") or ""
        m = re.fullmatch(re.escape(ident) + r"\.thumbs/(.+)_(\d{6})\.jpg", name)
        if m and m.group(1) in stems:
            out.append((int(m.group(2)), name))
    return sorted(out)


def item(http_json, ident):
    raw = archive_json(http_json, f"/metadata/{urllib.parse.quote(ident)}")
    if not raw or "metadata" not in raw:
        raise RuntimeError(f"archive.org item '{ident}' not found")
    if raw.get("is_dark"):
        raise RuntimeError(f"archive.org item '{ident}' is restricted (dark)")
    meta = raw["metadata"]
    files = [f for f in raw.get("files", []) if isinstance(f, dict)]
    cols = meta.get("collection") or []
    cols = [c for c in (cols if isinstance(cols, list) else [cols]) if not str(c).startswith("fav-")]
    return {"identifier": ident, "title": _flat(meta.get("title")) or ident, "creator": _flat(meta.get("creator")) or None,
            "date": _flat(meta.get("date")) or _flat(meta.get("year")) or None, "collections": cols,
            "tier": min((TIERS.get(c, 3) for c in cols), default=3), "color": _flat(meta.get("color")) or None,
            "sound": _flat(meta.get("sound")) or None, "shotlist": _flat(meta.get("shotlist"))[:2000] or None,
            "description": re.sub(r"<[^>]+>|\s+", " ", _flat(meta.get("description")))[:300].strip() or None,
            "license": license_info(meta.get("licenseurl"), meta.get("rights")),
            "server": raw.get("server") or raw.get("d1"), "files": files, "groups": video_groups(files),
            "transcripts": [f["name"] for f in files if f.get("format") in TRANSCRIPTS and str(f.get("size") or "0") != "0"],
            "page_url": f"{BASE}/details/{ident}"}


def file_url(ident, name):
    return f"{BASE}/download/{urllib.parse.quote(ident)}/{urllib.parse.quote(name)}"


def pick_file(it, name=None):
    """The file to cut: the named one, else the best rendition of the longest video."""
    if name:
        for g in it["groups"]:
            for f in g["files"]:
                if f["name"] == name:
                    return g, f
        names = [g["best"]["name"] for g in it["groups"]][:5]
        raise RuntimeError(f"no video file '{name}' in {it['identifier']}; playable: {names}")
    if not it["groups"]:
        raise RuntimeError(f"{it['identifier']} has no playable video (h.264 / MPEG4)")
    g = max(it["groups"], key=lambda g: g["best"]["length"] or 0)
    return g, g["best"]


# --- inspect: scenes + keyframes over HTTPS ------------------------------------------------------------------
MIN_SCENE, LONG_TAKE, SPLIT_STEP, MAX_SCENES, MAX_WINDOW = 1.5, 20.0, 10.0, 120, 900.0
NET = ["-reconnect", "1", "-reconnect_on_network_error", "1", "-reconnect_delay_max", "10", "-rw_timeout", "20000000"]


def net(url, ua):
    """Input options for reading over HTTP(S): our User-Agent, reconnects, a read timeout. None for local files."""
    return ["-user_agent", ua, *NET] if str(url).startswith(("http://", "https://")) else []


def normalize_scenes(cuts, start, end):
    """Merge scenes < 1.5 s, split takes > 20 s every 10 s (marked synthetic), cap at 120."""
    bounds = [start] + sorted({round(c, 3) for c in cuts if start < c < end}) + [end]
    merged = []
    for a, b in zip(bounds, bounds[1:]):
        if b <= a:
            continue
        if merged and (b - a < MIN_SCENE or merged[-1][1] - merged[-1][0] < MIN_SCENE):
            merged[-1][1] = b
        else:
            merged.append([a, b])
    out = []
    for a, b in merged:
        if b - a > LONG_TAKE:
            t = a
            while b - t > SPLIT_STEP + MIN_SCENE:
                out.append((t, t + SPLIT_STEP, True))
                t += SPLIT_STEP
            out.append((t, b, True))
        else:
            out.append((a, b, not cuts))
    return [{"scene": i + 1, "start": round(a, 3), "end": round(b, 3), "keyframe": round((a + b) / 2, 3),
             "synthetic": syn} for i, (a, b, syn) in enumerate(out[:MAX_SCENES])]


def detect_cuts(url, start, end, ua, threshold=0.3):
    p = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "info", *net(url, ua),
                        "-ss", f"{start:.3f}", "-t", f"{end - start:.3f}", "-i", url, "-an", "-vf",
                        f"scale=320:-2,select='gt(scene,{threshold})',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True, timeout=900)
    if p.returncode != 0:
        raise RuntimeError("scene scan failed: " + (p.stderr.strip().splitlines() or ["ffmpeg error"])[-1][:200])
    return [start + float(t) for t in re.findall(r"pts_time:([0-9.]+)", p.stderr)]


def keyframes(url, times, out_dir, ua):
    """One 320 px JPEG per time (input seeking, so only the bytes around each time are read)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    got = []
    for t in times:
        out = out_dir / f"kf_{t:09.3f}.jpg"
        if not out.exists():
            subprocess.run(["ffmpeg", "-y", "-nostdin", "-v", "error", *net(url, ua), "-ss", f"{t:.3f}",
                            "-i", url, "-frames:v", "1", "-vf", "scale=320:-2", "-q:v", "4", str(out)],
                           capture_output=True, timeout=120)
        got.append(out if out.exists() else None)
    return got


def sheet(images, labels, out_png, cols=4):
    """Numbered contact sheet of keyframes/thumbnails with a label on each tile."""
    td = Path(tempfile.mkdtemp())
    try:
        tiles = []
        for img, label in zip(images, labels):
            if not img:
                continue
            fr = td / f"f{len(tiles):03d}.png"
            lab = label.replace("'", "").replace(":", r"\:")
            p = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(img), "-frames:v", "1", "-vf",
                                "scale=320:180:force_original_aspect_ratio=decrease,pad=320:204:(ow-iw)/2:24:0x222222,"
                                f"drawtext=text='{lab}':x=6:y=4:fontsize=15:fontcolor=white", str(fr)], capture_output=True)
            if p.returncode == 0:
                tiles.append(fr)
        if not tiles:
            return None
        cols = min(cols, len(tiles))
        out_png.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "1", "-i", str(td / "f%03d.png"), "-vf",
                        f"tile={cols}x{-(-len(tiles) // cols)}:padding=4:margin=4:color=0x111111", "-frames:v", "1",
                        str(out_png)], check=True, capture_output=True)
        return out_png
    finally:
        shutil.rmtree(td, ignore_errors=True)


def fmt(t):
    m, s = divmod(max(t, 0), 60)
    return f"{int(m)}:{s:04.1f}"


CLIP_PAGE = 60


def inspect(http_json, download, ident, out_base, ua, name=None, window=None, page=1):
    """Write <out_base>.json/.md/.png: scenes with timings and a keyframe sheet for one video, or, for an item
    that holds many separate clips, a clip list with the archive's own thumbnails."""
    it = item(http_json, ident)
    out_base = Path(out_base)
    lic = it["license"]
    head = [f"# {it['title']} ({it['date'] or 'n.d.'})", "",
            f"{it['page_url']} · collections: {', '.join(it['collections'][:4]) or '-'} (tier {it['tier']}) · "
            f"licence: {lic['label']} (commercial use {lic['commercial_use']}) · colour: {it['color'] or '?'} · "
            f"sound: {it['sound'] or '?'}", ""]
    if lic.get("rights_statement"):
        head += [f"Rights statement: {lic['rights_statement'][:300]}", ""]
    if it["shotlist"]:
        head += ["Shotlist (from the archive):", "", it["shotlist"][:1200], ""]
    if it["transcripts"]:
        head += [f"Transcripts in the item: {', '.join(it['transcripts'][:3])}", ""]
    if name is None and len(it["groups"]) > 3:  # multi-clip item: list clips with archive thumbnails
        clips, imgs, labels = [], [], []
        td = out_base.parent / (out_base.name + "_thumbs")
        first = (page - 1) * CLIP_PAGE
        for i, g in enumerate(it["groups"][first:first + CLIP_PAGE], first + 1):
            b = g["best"]
            clips.append({"clip": i, "file": b["name"], "length": b["length"], "format": b["format"],
                          "size": f"{b['width']}x{b['height']}" if b["width"] else None})
            th = thumbs_for(ident, it["files"], g)
            if th:
                dest = td / f"c{i:03d}.jpg"
                if not dest.exists():
                    try:
                        download(file_url(ident, th[0][1]), dest, max_mb=5)
                    except Exception:
                        dest = None
                imgs.append(dest)
                labels.append(f"#{i}  {b['length'] or 0:.0f}s")
        png = sheet(imgs, labels, out_base.with_suffix(".png"))
        pages = -(-len(it["groups"]) // CLIP_PAGE)
        rows = head + [f"{len(it['groups'])} separate clips; page {page} of {pages} (clips {first + 1}-"
                       f"{min(first + CLIP_PAGE, len(it['groups']))}" + (f", next: --page {page + 1}" if page < pages else "")
                       + f"). Inspect one with `vs fetch inspect archive:{ident} --file <file>`.", "",
                       "| # | file | length | format | size |", "|---|---|---|---|---|"]
        rows += [f"| {c['clip']} | {c['file']} | {c['length'] or '?'} s | {c['format']} | {c['size'] or ''} |" for c in clips]
        data = {"mode": "clip_list", **{k: it[k] for k in ("identifier", "title", "date", "collections", "tier",
                                                         "license", "page_url")}, "clips": clips}
    else:
        g, f = pick_file(it, name)
        length = f["length"] or g["best"]["length"]
        if not length:
            raise RuntimeError(f"archive.org lists no length for {f['name']}; name another file with --file")
        start, end = (window or (0.0, min(length, MAX_WINDOW)))
        end = min(end, length, start + MAX_WINDOW)
        scan = g["scan"]
        scan_url = file_url(ident, scan["name"])
        try:
            cuts = detect_cuts(scan_url, start, end, ua)
        except (RuntimeError, subprocess.TimeoutExpired) as e:
            cuts, head = [], head + [f"(scene scan failed: {e}; showing fixed 10 s steps)", ""]
        scenes = normalize_scenes(cuts, start, end)
        kdir = out_base.parent / (out_base.name + "_frames")
        imgs = keyframes(scan_url, [s["keyframe"] for s in scenes], kdir, ua)
        for s, img in zip(scenes, imgs):
            s["image"] = str(img) if img else None
        png = sheet(imgs, [f"#{s['scene']}  {fmt(s['start'])}-{fmt(s['end'])}" for s in scenes], out_base.with_suffix(".png"))
        rows = head + [f"File to cut: {f['name']} ({f['format']}, {f['width']}x{f['height']}, {length:.0f} s); scanned "
                       f"{scan['name']} from {fmt(start)} to {fmt(end)}" + (" (the first 15 min; pass --window for later "
                                                                             "parts)" if not window and end < length else "") + ".",
                       "", "| scene | from | to | length | note |", "|---|---|---|---|---|"]
        rows += [f"| {s['scene']} | {fmt(s['start'])} | {fmt(s['end'])} | {s['end'] - s['start']:.1f} s | "
                 f"{'long take, split' if s['synthetic'] else ''} |" for s in scenes]
        rows += ["", f"Cut one: `vs fetch get <results.json> <n> --section <from>-<to>` (or `vs fetch get archive:{ident} "
                 f"--file {f['name']} --section <from>-<to>`)."]
        data = {"mode": "scenes", **{k: it[k] for k in ("identifier", "title", "date", "collections", "tier", "license",
                                                       "page_url", "shotlist")},
                "file": f["name"], "scan_file": scan["name"], "length": length, "window": [start, end], "scenes": scenes}
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_base.with_suffix(".json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    out_base.with_suffix(".md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    return data, png


# --- verified cut + provenance ------------------------------------------------------------------------------
TOLERANCE = 0.1


def verify(path):
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,codec_name,width,height",
                        "-of", "json", str(path)], capture_output=True, text=True)
    info = json.loads(p.stdout or "{}") if p.returncode == 0 else {}
    d = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", str(path), "-f", "null", "-"], capture_output=True, text=True)
    errors = len([ln for ln in d.stderr.splitlines() if ln.strip()]) + (d.returncode != 0)
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    return {"duration": round(float(info.get("format", {}).get("duration") or 0), 3), "decode_errors": errors,
            "video_codec": v.get("codec_name"), "size": f"{v.get('width')}x{v.get('height')}" if v else None,
            "has_audio": any(s.get("codec_type") == "audio" for s in info.get("streams", []))}


def cut(url, start, duration, dest, ua, audio=True, source_length=None):
    """Re-encoded, frame-accurate H.264 cut (a stream copy snaps to keyframes: 8 s came back as 11.35 s), checked
    to be within 0.1 s of the asked length with zero decode errors; one retry. Returns the verify result."""
    want = min(duration, source_length - start) if source_length else duration
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.stem + ".part" + dest.suffix)
    last = None
    for attempt in range(2):
        cmd = ["ffmpeg", "-y", "-nostdin", "-v", "error", *net(url, ua), "-ss", f"{start:.3f}", "-i", url,
               "-t", f"{want:.3f}", "-map", "0:v:0"] + (["-map", "0:a:0?"] if audio else []) + \
              ["-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p"] + \
              (["-c:a", "aac", "-b:a", "192k"] if audio else ["-an"]) + ["-movflags", "+faststart", "-f", "mp4", str(tmp)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode == 0:
            last = verify(tmp)
            if abs(last["duration"] - want) <= TOLERANCE and last["decode_errors"] == 0:
                tmp.replace(dest)
                return dict(last, asked=round(want, 3))
        else:
            last = {"error": (p.stderr.strip().splitlines() or ["ffmpeg error"])[-1][:200]}
    tmp.unlink(missing_ok=True)
    raise RuntimeError(f"cut failed verification after 2 tries: {last}")


def provenance(it, f, start, dur, dest, ua, checked):
    """Record kept with the clip (and in the credits ledger): exactly which seconds of which file, under what licence."""
    lic = it["license"]
    year = (re.search(r"\b(1[89]\d\d|20\d\d)\b", it["date"] or "") or [None])[0]
    coll = {"prelinger": "Prelinger Archives", "nasa": "NASA"}.get((it["collections"] or [""])[0], "")
    attribution = (f"\"{it['title']}\"" + (f" ({year})" if year else "") + (f", {coll}" if coll else "") +
                   f" via Internet Archive, {it['page_url']}. License: {lic['label']}.")
    h = hashlib.sha256(Path(dest).read_bytes()).hexdigest()
    return {"schema": "video-studio/archive-provenance/1", "clip_sha256": h,
            "source": {"identifier": it["identifier"], "title": it["title"], "file": f["name"], "file_md5": f.get("md5"),
                       "format": f["format"], "collections": it["collections"], "tier": it["tier"], "date": it["date"],
                       "creator": it["creator"]},
            "license": lic, "segment": {"start_s": round(start, 3), "duration_s": round(dur, 3),
                                        "verified_duration_s": checked["duration"]},
            "retrieval": {"retrieved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                          "data_node": it.get("server"), "user_agent": ua},
            "processing": {"reencoded": True, "audio": checked.get("has_audio"), "decode_errors": checked["decode_errors"]},
            "attribution_text": attribution}
