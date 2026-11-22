#!/usr/bin/env python3
"""Sound design: find every moment in an edit that wants a sound, and put a real recording on
the exact frame.

Moments come from (any combination):
  --edl work/edl.json        transitions, hard cuts, text pops, overlay entrances, image reveals
  --hyperframes <dir>        a HyperFrames project: every timed .clip element (titles, cards, logos, charts…)
  --video out/draft.mp4      a finished render with no EDL: scene changes
  --beats work/beats.json    downbeats (impacts on the drop) with --on-beats
Sounds come from a library of real recordings, matched by filename keywords:
  project assets/sfx, workspace library/assets/sfx, the media-use skill's bundled CC SFX, any --library DIR,
  and sounds you render from earshot's code-made bank (`vs sfx bank --from earshot`).

  vs sfx plan --edl work/edl.json -o work/sfx_plan.json            -> plan + report.md (edit it, then apply)
  vs sfx plan --hyperframes work/gfx/launch -o work/sfx_plan.json
  vs sfx apply out/draft.mp4 --plan work/sfx_plan.json -o out/draft_sfx.mp4 --stem out/sfx_stem.wav
  vs sfx merge work/edl.json --plan work/sfx_plan.json -o work/edl.sfx.json   (EDL `sfx` entries for vs render)
  vs sfx library                                                    what's available, by category
  vs sfx analyse <files|dirs>                                       onset, hit, crest, level, brightness of each sound
  vs sfx plan --edl work/edl.json --snap out/draft.mp4 --sheet ...  snap every cue to the frame the picture changes,
                                                                    and a frame per cue for Claude to judge
  vs sfx check --plan work/sfx_plan.json                            measured landing of every sound vs its frame
  vs sfx bank --from earshot                                        render earshot's sound bank into library/assets/sfx/earshot
"""
import argparse
import array
import hashlib
import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import (cut_points, die, fmt_ts, load_json, need, probe, run, save_json, sfx_chain,  # noqa: E402
                       timeline)
import sfx_sense  # noqa: E402

AUDIO_EXT = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".aiff", ".aif", ".ogg", ".opus"}
# category -> filename keywords (first match wins, so order specific -> generic)
CATEGORIES = {  # first match wins: specific before generic. Matched on the cue part of the name ("swipe__glass" -> swipe)
    "type": ["typing", "typewriter", "keyboard"],
    "camera": ["shutter", "camera", "flash", "photo"],
    "whoosh": ["whoosh", "swoosh", "swish", "woosh", "swipe", "whip", "pass-by", "passby", "transition", "slide",
               "open", "close", "maximize", "minimize", "expand", "collapse", "drag", "seek", "skip"],
    "riser": ["riser", "rise", "build", "uplifter", "sweep-up", "tension", "loading", "processing", "progress",
              "scanning", "connecting", "streaming", "charge"],
    "impact": ["impact", "hit", "boom", "thud", "slam", "punch", "drop", "kick", "braam", "snap", "lock", "stop", "stomp"],
    "glitch": ["glitch", "digital", "static", "zap", "error", "invalid", "warning", "blocked", "denied", "fail",
               "disconnect", "scratch", "cancel", "delete", "refund"],
    "chime": ["chime", "ding", "bell", "notification", "success", "sparkle", "shimmer", "magic", "complete",
              "confirmation", "achievement", "reward", "level-up", "bonus", "badge", "streak", "purchase", "checkout",
              "unlock", "receive", "send", "question", "bong", "ping", "glass", "wake", "connect", "coupon", "info", "mention"],
    "pop": ["pop", "bubble", "blip", "pluck", "hover", "focus", "reaction", "add-to-cart", "paste", "copy"],
    "click": ["click", "tap", "tick", "ui", "button", "toggle", "switch", "mouse", "key", "select", "press", "check",
              "back", "forward", "scroll", "play", "pause", "release", "deselect", "volume", "reorder", "start"],
    "swell": ["swell", "reverse", "reverse-cymbal", "suck", "inhale", "sleep", "whoom"],
    "paper": ["paper", "page", "flip", "rustle"],
}
# What each moment wants: (category preference list, level dB).
# level: dB relative to a normalised hit (the sound's loudest 50 ms brought to REF_HIT_DB), so 0 dB is about as loud as
# a dialogue peak, -10 dB sits clearly under it. Every file is measured, so a quiet chime and a slammed impact land
# at the level the cue asks for instead of differing by 30 dB.
# Which point of a sound lands on the frame depends on the sound:
#   "crest" = its loudest moment: a whoosh passes the cut there, a riser or swell tops out on the reveal;
#   "hit"   = where its loud part arrives (first 50 ms within 3 dB of the loudest): an impact with a pre-swell or a
#             silent lead-in hits on the frame, a sustained boom starts on it;
#   "onset" = where it starts sounding: clicks, pops, chimes, typing and glitches start on the action.
ANCHOR = {"whoosh": "crest", "swell": "crest", "riser": "crest", "impact": "hit"}
ANCHOR_KEY = {"onset": "onset", "hit": "hit_t", "crest": "crest_t"}
CUE = {
    "transition-fast": (["whoosh", "swell"], -8),
    "transition-soft": (["swell", "whoosh"], -14),
    "transition-dip": (["impact", "swell"], -10),
    "transition-glitch": (["glitch", "whoosh"], -12),
    "cut-section": (["whoosh", "impact"], -12),
    "cut": (["click", "pop"], -18),
    "text": (["pop", "click"], -12),
    "text-big": (["impact", "pop"], -10),
    "overlay": (["whoosh", "pop"], -12),
    "logo": (["chime", "impact"], -10),
    "chart": (["click", "pop"], -14),
    "image": (["swell", "whoosh"], -16),
    "scene": (["whoosh", "click"], -14),
    "beat": (["impact"], -9),
    "type": (["type", "click"], -16),
    "camera": (["camera", "click"], -12),
    "riser": (["riser", "swell"], -14),
}
REF_HIT_DB = -12.0      # a normalised sound's loudest 50 ms RMS, in dBFS
MAX_BOOST_DB = 18.0     # never lift a near-silent file more than this (it would lift its noise too)
PEAK_CEIL_DB = -1.0     # a placed sound's sample peak never exceeds this
# Taste presets: how dense, how loud, extra layers. Explicit flags win over the preset.
STYLES = {
    "talking-head": {"min_gap": 5.0, "every_cut": False, "gain_offset": -2, "risers": False, "speech_duck": 12,
                     "drop_over_speech": ["cut", "scene", "chart", "type"]},
    "tutorial": {"min_gap": 1.5, "every_cut": False, "gain_offset": -2, "risers": False, "speech_duck": 12,
                 "drop_over_speech": ["cut", "scene"]},
    "ugc-ad": {"min_gap": 0.8, "every_cut": True, "gain_offset": 0, "risers": False, "speech_duck": 10,
               "drop_over_speech": ["cut"]},
    "montage": {"min_gap": 0.5, "every_cut": True, "gain_offset": 0, "risers": True, "speech_duck": 10,
                "drop_over_speech": []},
    "launch": {"min_gap": 0.25, "every_cut": True, "gain_offset": 2, "risers": True, "speech_duck": 10,
               "drop_over_speech": []},
}
FAST_TR = {"whip", "whip-left", "whip-right", "slideleft", "slideright", "slideup", "slidedown", "smoothleft",
           "smoothright", "wipeleft", "wiperight", "wipeup", "wipedown", "zoomin", "hblur", "radial"}
GLITCH_TR = {"pixelize", "glitch"}


def tr_pan(ttype):
    """Pan a transition whoosh the way the picture moves: content leaving to the left sounds on the left."""
    t = ttype.lower()
    if t in ("whip", "whip-left") or t.endswith("left"):
        return -0.4
    if t == "whip-right" or t.endswith("right"):
        return 0.4
    return 0.0


def plugin_root():
    return Path(__file__).resolve().parent.parent


def workspace():
    ws = os.environ.get("VS_WORKSPACE")
    if ws:
        return Path(ws)
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(top.stdout.strip() if top.returncode == 0 else os.getcwd()) / "video-studio"


def categorise(name):
    n = name.lower().split("__")[0]
    for cat, words in CATEGORIES.items():
        if any(re.search(rf"(^|[^a-z]){re.escape(w)}", n) for w in words):
            return cat
    return None


def library(extra, project=None, only=False):
    """Sound folders, most specific first. only=True: just the --library folders (a client's own brand pack)."""
    dirs = []
    if project and not only:
        dirs.append(Path(project) / "assets" / "sfx")
    if only:
        dirs += [Path(d) for d in extra or []]
    else:
        dirs += [workspace() / "library" / "assets" / "sfx", *(Path(d) for d in extra or []),
                 plugin_root() / "skills" / "media-use" / "audio" / "assets" / "sfx"]
    lib = {}
    for d in dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*")):
            if f.suffix.lower() in AUDIO_EXT and f.is_file():
                cat = categorise(f.stem) or categorise(f.parent.name)
                if cat:
                    lib.setdefault(cat, []).append(str(f))
    # Within a category, the most typical sounds first (keywords are listed best-first).
    def rank(path, cat):
        n = Path(path).stem.lower().split("__")[0]
        return next((i for i, w in enumerate(CATEGORIES[cat]) if re.search(rf"(^|[^a-z]){re.escape(w)}", n)), 99)
    for cat in lib:
        lib[cat].sort(key=lambda f, c=cat: rank(f, c))
    return lib


def moments_from_edl(edl, every_cut):
    out = []
    tl = cut_points(timeline(edl))
    for k, it in enumerate(tl[1:], 1):
        seg = it["seg"]
        tr = seg.get("transition_in")
        t = it["out_start"] + it["overlap"] / 2
        if tr:
            ttype = tr.get("type", "fade") if isinstance(tr, dict) else "fade"
            cue = ("transition-glitch" if ttype in GLITCH_TR else "transition-fast" if ttype in FAST_TR
                   else "transition-dip" if "dip" in ttype or ttype.startswith("fade") and "black" in ttype
                   else "transition-soft")
            out.append({"t": t, "cue": cue, "why": f"{ttype} into shot {k + 1}", "pan": tr_pan(ttype),
                        "ev_dur": it["overlap"] or None})
        elif it["src"] != tl[k - 1]["src"]:
            out.append({"t": t, "cue": "cut-section", "why": f"cut to {Path(it['src']).name} (shot {k + 1})"})
        elif every_cut:
            out.append({"t": t, "cue": "cut", "why": f"cut into shot {k + 1}"})
        if str(it["src"]).lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".heic")):
            out.append({"t": it["out_start"] + it["overlap"], "cue": "image", "why": "photo reveal"})
    for tx in edl.get("texts", []):
        big = float(tx.get("size", 0.075)) >= 0.09 or tx.get("pos") == "center"
        out.append({"t": float(tx["start"]), "cue": "text-big" if big else "text", "size": float(tx.get("size", 0.075)),
                    "why": f"text \"{str(tx['text'])[:30]}\" ({tx.get('anim', 'fade')})"})
    for ov in edl.get("overlays", []):
        name = Path(ov["file"]).stem.lower()
        cue = "logo" if "logo" in name or "end" in name else ("chart" if "chart" in name or "stat" in name else "overlay")
        out.append({"t": float(ov["start"]), "cue": cue, "why": f"overlay {Path(ov['file']).name}"})
    return out


TIMED_RE = re.compile(r"<([a-z0-9-]+)(\s[^>]*\bdata-start=\"[^\"]*\"[^>]*)>", re.I)


def attr(s, name):
    m = re.search(rf"\b{name}=\"([^\"]*)\"", s)
    return html.unescape(m.group(1)) if m else None


def moments_from_hyperframes(root):
    """Read a HyperFrames project: timed .clip elements in index.html and compositions/*.html.
    Sub-composition hosts offset their children by the host's data-start."""
    root = Path(root)
    index = root / "index.html"
    if not index.exists():
        die(f"{index} not found (pass the HyperFrames project folder)")
    out = []

    def scan(path, offset, depth=0):
        txt = path.read_text(encoding="utf-8", errors="ignore")
        for m in TIMED_RE.finditer(txt):
            tag, attrs = m.group(1), m.group(2)
            start = attr(attrs, "data-start")
            src = attr(attrs, "data-composition-src")
            is_clip = re.search(r"\bclass=\"[^\"]*\bclip\b", attrs) is not None
            if not src and not is_clip:
                continue  # the root composition or an untimed wrapper
            if start is None:
                continue
            try:
                t = offset + float(start)
            except ValueError:
                continue
            ident = (attr(attrs, "id") or "") + " " + (attr(attrs, "data-composition-id") or "")
            comp = src
            kind = (attr(attrs, "data-track-kind") or "").lower()
            low = ident.lower()
            if tag in ("audio",):
                continue
            if comp and comp.endswith(".html") and depth < 3 and (root / comp).exists():
                out.append({"t": t, "cue": "transition-fast" if t > 0 else "overlay", "why": f"scene {ident.strip()}"})
                scan(root / comp, t, depth + 1)
                continue
            if kind == "captions" or "caption" in low:
                continue
            cue = ("logo" if "logo" in low else "chart" if re.search(r"chart|graph|stat|number|counter", low)
                   else "text-big" if re.search(r"title|headline|hero|hook", low)
                   else "type" if "typ" in low else "camera" if "photo" in low or "flash" in low
                   else "overlay" if tag in ("video", "img") else "text")
            out.append({"t": t, "cue": cue, "why": f"<{tag}> {ident.strip() or '(no id)'} in {path.name}"})
    scan(index, 0.0)
    comp_dir = root / "compositions"
    if comp_dir.is_dir() and not any("scene" in m["why"] for m in out):
        for f in sorted(comp_dir.glob("*.html")):  # hosts not resolvable: still list their clips at local time
            scan(f, 0.0, 3)
    return out


def scene_scores(video):
    """ffmpeg's per-frame scene score (0..1) for every frame."""
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", video, "-an", "-vf",
             "scale=320:-2,select='gte(scene,0)',metadata=print:key=lavfi.scene_score", "-f", "null", "-"])
    t = [float(x) for x in re.findall(r"pts_time:([\d.]+)", p.stderr)]
    v = [float(x) for x in re.findall(r"lavfi\.scene_score=([\d.]+)", p.stderr)]
    return list(zip(t, v))


def moments_from_video(video, threshold, adaptive=3.0, min_len=15, window=2, floor=None):
    """Hard cuts in a finished video. Adaptive, like PySceneDetect's AdaptiveDetector (adaptive_threshold 3.0,
    window 2 frames, min_scene_len 15 frames): a frame is a cut when its scene score is >= `adaptive` x the mean of
    its neighbours and above a small floor, or simply above `threshold`. Grainy film flickers everywhere, so a
    fixed threshold either misses cuts or finds grain."""
    sc = scene_scores(video)
    if floor is None:  # the clip's own noise: grainy film scores ~0.09 at its 95th percentile, real cuts >= 0.15
        vals = sorted(v for _, v in sc)
        floor = max(0.10, 1.5 * vals[int(0.95 * (len(vals) - 1))]) if vals else 0.10
    cuts, last = [], -10 ** 9
    for i, (t, v) in enumerate(sc):
        nb = [x for _, x in sc[max(0, i - window):i] + sc[i + 1:i + 1 + window]]
        ratio = v / max(sum(nb) / len(nb), 1e-3) if nb else 0
        if (v >= threshold or (v >= floor and ratio >= adaptive)) and i - last >= min_len:
            cuts.append({"t": t, "cue": "scene", "why": f"cut (scene score {v:.2f}, {ratio:.1f}x its neighbours)"})
            last = i
    return cuts


def cache_path():
    return Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "video-studio" / "sfx_analysis_v4.json"


def _measure(path):
    """Decode to 16 kHz mono and read the envelope in 10 ms windows."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = array.array("h", raw)
    if sys.byteorder == "big":
        a.byteswap()
    win = 160
    rms = [math.sqrt(sum(x * x for x in a[i:i + win]) / max(len(a[i:i + win]), 1)) for i in range(0, len(a), win)]
    if not rms or max(rms) == 0:
        return None
    peak = max(abs(x) for x in a)
    hit = [math.sqrt(sum(r * r for r in rms[i:i + 5]) / len(rms[i:i + 5])) for i in range(len(rms))]  # 50 ms RMS
    hi = max(range(len(hit)), key=hit.__getitem__)
    arrive = next(i for i, h in enumerate(hit) if h >= hit[hi] * 0.708)  # first 50 ms within 3 dB of the loudest
    top = max(rms)
    onset = next(i for i, r in enumerate(rms) if r >= top * 0.1)  # first window within 20 dB of the loudest
    db = lambda v: round(20 * math.log10(max(v, 1) / 32768), 1)  # noqa: E731
    return {"duration": round(len(a) / 16000, 3), "onset": round(onset * 0.01, 3),
            "hit_t": round(min(arrive + 2, len(rms) - 1) * 0.01, 3),   # where the loud part arrives
            "crest_t": round(min(hi + 2, len(rms) - 1) * 0.01, 3),     # centre of the loudest 50 ms
            "hit_db": db(hit[hi]), "peak_db": db(peak), "centroid_hz": sfx_sense.centroid_hz(path)}


def analyse(paths):
    """Onset, peak time, loudest-50 ms level and sample peak for each sound (cached by path, size and mtime)."""
    cp = cache_path()
    try:
        cache = json.loads(cp.read_text())
    except (OSError, ValueError):
        cache = {}
    out, dirty = {}, False
    for f in paths:
        try:
            st = os.stat(f)
        except OSError:
            continue
        key = hashlib.sha1(f"{Path(f).resolve()}|{st.st_size}|{int(st.st_mtime)}".encode()).hexdigest()
        if key not in cache:
            cache[key], dirty = _measure(f), True
        out[f] = cache[key]
    if dirty:
        cp.parent.mkdir(parents=True, exist_ok=True)
        cp.write_text(json.dumps(cache))
    return out


def norm_gain(m):
    """dB that brings a sound's loudest 50 ms to REF_HIT_DB, without lifting noise too far or clipping."""
    if not m:
        return 0.0
    return round(min(max(REF_HIT_DB - m["hit_db"], -30.0), MAX_BOOST_DB), 1)


def place(m, frame_t, anchor, level, max_tail, max_head=None, rate=1.0):
    """Timing fields for one cue: the anchor point of the sound lands on frame_t; head and tail are capped.
    With a playback `rate` (pitch variation), every time in the file is divided by it."""
    if m and rate != 1.0:
        m = dict(m, **{k: m[k] / rate for k in ("duration", "onset", "hit_t", "crest_t")})
    off = m[ANCHOR_KEY[anchor]] if m else 0.0
    start = max(off - max_head, 0.0) if max_head is not None else 0.0  # a long build-up starts part-way in
    at = frame_t - (off - start)
    if at < 0:  # the sound would start before the video: drop more of its head instead of sliding it late
        start, at = start - at, 0.0
    cue = {"at": round(at, 3), "in": round(start, 3) if start else 0}
    if start and off - start > 0.05:
        cue["fade_in"] = round(min(0.15, (off - start) / 2), 3)
    if m:
        dur = min(m["duration"] - start, off - start + max_tail)
        if dur < m["duration"] - start - 0.01:
            cue.update(dur=round(dur, 3), fade_out=round(min(0.25, dur / 3), 3))
        norm = norm_gain(m)
        gain = min(norm + level, PEAK_CEIL_DB - m["peak_db"])
        cue.update(norm_db=norm, gain_db=round(gain, 1))
    else:
        cue["gain_db"] = level
    return cue


def speech_spans(path):
    """Word spans [(s, e)] from a vs transcribe JSON of the edit itself (output time, e.g. of out/draft.mp4)."""
    words = load_json(path).get("words", [])
    return [(float(w["s"]), float(w["e"])) for w in words if "s" in w and "e" in w]


def over_speech(t, spans, pad=0.08):
    return any(s - pad <= t <= e + pad for s, e in spans)


# What a moment wants from a sound (Soundify: the sound should cover the event; size sets weight).
HEAVY = {"text-big", "logo", "transition-dip", "beat", "cut-section"}      # big events: low, heavy sounds
LIGHT = {"text", "chart", "cut", "type", "camera", "overlay", "scene"}     # small UI events: short, bright sounds
REPEAT_WINDOW = 3                                                          # never reuse one of the last 3 files


def fit_score(m, cue, ev_dur):
    """How well a measured sound suits a moment; higher is better. Explainable parts, no model."""
    if not m:
        return 0.0, ""
    s, why = 0.0, []
    c = m.get("centroid_hz")
    if c:
        if cue in HEAVY:
            s += max(0.0, 1 - c / 4000)
            why.append(f"{c / 1000:.1f} kHz")
        elif cue in LIGHT:
            s += min(1.0, c / 4000)
            why.append(f"{c / 1000:.1f} kHz")
    if cue in LIGHT and m["duration"] > 1.2:
        s -= 0.5  # a UI pop should be short
    if ev_dur:  # a whoosh's build-up should match the move it covers (within 0.5x..2x)
        build = max(m["crest_t"] - m["onset"], 0.01)
        ratio = build / ev_dur
        s += 1.0 if 0.5 <= ratio <= 2 else max(0.0, 1 - abs(ratio - 1) / 3)
        why.append(f"build {build:.2f} s for a {ev_dur:.2f} s move")
    return round(s, 3), ", ".join(why)


def pick(lib, cats, recent, prefer, meas=None, cue=None, ev_dur=None):
    """Best-fitting sound of the first category that has any, skipping the last REPEAT_WINDOW files used
    (a shuffle bag, as in Wwise/FMOD/Unity random containers). Returns (category, file, why)."""
    for c in cats:
        files = lib.get(c)
        if not files:
            continue
        if prefer:  # e.g. --prefer cinematic,studio: those styles/packs first
            pref = [w.strip().lower() for w in prefer.split(",")]
            files = [f for f in files if any(w in f.lower() for w in pref)] or files
        fresh = [f for f in files if f not in recent[-REPEAT_WINDOW:]] or files
        order = {f: i for i, f in enumerate(files)}  # library order = keyword typicality, breaks ties
        scored = [(fit_score((meas or {}).get(f), cue, ev_dur), f) for f in fresh]
        (score, why), best = max(scored, key=lambda x: (x[0][0], -order[x[1]]))
        recent.append(best)
        return c, best, why
    return cats[0], None, ""


def variation(file, recent, seed):
    """A reused file plays slightly different each time (game-audio practice): pitch +-0.5 semitone,
    level 0 to -2 dB, seeded so the plan is reproducible. None the first time a file is used."""
    if recent.count(file) < 2:
        return None
    h = int(hashlib.sha1(f"{file}|{seed}".encode()).hexdigest()[:8], 16)
    semis = ((h % 1000) / 1000 - 0.5)            # -0.5 .. +0.5
    return {"rate": round(2 ** (semis / 12), 4), "jitter_db": -round(((h >> 10) % 1000) / 500, 1)}


def salience_db(m_):
    """Level from what is on screen (Soundify/MoSound: size and motion set intensity), clamped to +-6 dB because
    intensity predicted from video is rough (Video-Foley: half of frames within 6 dB)."""
    d = 0.0
    if m_.get("size"):
        d += 6 * math.log2(max(m_["size"], 0.01) / 0.075) / 2       # +3 dB per doubling of text size
    if m_.get("strength") is not None:
        d += (m_["strength"] - 0.5) * 6                              # strong visual change louder, weak quieter
    return round(max(-6.0, min(6.0, d)), 1)


def resolve_style(a):
    st = STYLES.get(a.style or "", {})
    defaults = {"min_gap": 0.35, "every_cut": False, "gain_offset": 0.0, "risers": False, "speech_duck": 10.0,
                "drop_over_speech": []}
    for k, v in defaults.items():
        if getattr(a, k, None) is None:
            setattr(a, k, st.get(k, v))


def cmd_plan(a):
    resolve_style(a)
    moments = []
    if a.edl:
        moments += moments_from_edl(load_json(a.edl), a.every_cut)
    if a.hyperframes:
        moments += [dict(m, t=m["t"] + a.hyperframes_offset) for m in moments_from_hyperframes(a.hyperframes)]
    if a.video:
        moments += moments_from_video(a.video, a.threshold)
    if a.beats and a.on_beats:
        moments += [{"t": t, "cue": "beat", "why": "downbeat"} for t in load_json(a.beats).get("downbeats", [])[:: a.on_beats]]
    if not (a.edl or a.hyperframes or a.video or (a.beats and a.on_beats)):
        die("no moments to look at: pass --edl, --hyperframes, --video and/or --beats")
    if not moments:  # a plain jump-cut talking head often has nothing that wants a sound: that's an answer, not an error
        save_json(a.out, {"plan": [], "style": a.style, "missing_categories": []})
        Path(a.out).with_suffix(".md").write_text(
            "# Sound design plan\n\nNo moments that want a sound: no transitions, source changes, texts, overlays or "
            "beats in this edit (jump cuts within one shot get no SFX). Nothing to apply.\n", encoding="utf-8")
        print(f"0 cues: nothing in this edit wants a sound effect -> {a.out}")
        return
    moments.sort(key=lambda m: m["t"])
    spans = speech_spans(a.words) if a.words else []
    if spans and a.drop_over_speech:
        moments = [m for m in moments if not (m["cue"] in a.drop_over_speech and over_speech(m["t"], spans))]
    # De-clutter: keep the more important cue when two land within min-gap.
    rank = ["logo", "text-big", "transition-fast", "transition-glitch", "transition-dip", "beat", "cut-section",
            "overlay", "chart", "transition-soft", "image", "camera", "type", "text", "scene", "cut"]
    kept = []
    for m in moments:
        if kept and m["t"] - kept[-1]["t"] < a.min_gap:
            if rank.index(m["cue"]) < rank.index(kept[-1]["cue"]):
                kept[-1] = m
            continue
        kept.append(m)
    if a.library_only and not a.library:
        die("--library-only needs --library <folder>")
    lib = library(a.library, a.project_dir, a.library_only)
    meas = analyse([f for fs in lib.values() for f in fs]) if shutil.which("ffmpeg") else {}
    # Visual evidence: snap each moment to the frame where the picture really changes (never to a model's guess).
    evidence = a.snap or a.video
    env = cx = None
    if evidence:
        env, cx, fps = sfx_sense.envelope(evidence)
        pk = sfx_sense.peaks(env, fps)
        for m in kept:
            hit = sfx_sense.snap(m["t"], m["cue"], pk, fps, env)
            if hit:
                m["planned_t"], m["t"], m["strength"], m["vframe"] = m["t"], hit[0], hit[1], hit[2]
            else:
                m["unsnapped"] = m["cue"] not in sfx_sense.NO_SNAP
    bias = a.sync_bias / 1000.0
    recent, plan = [], []
    for i, m in enumerate(kept):
        cats, level = CUE[m["cue"]]
        cat, choice, fit_why = pick(lib, cats, recent, a.prefer, meas, m["cue"], m.get("ev_dur"))
        anchor = ANCHOR.get(cat, "onset")
        level += a.gain_offset + salience_db(m)
        speech = bool(spans) and over_speech(m["t"], spans)
        if speech:
            level -= a.speech_duck
        var = variation(choice, recent, i) if choice else None
        if var:
            level += var["jitter_db"]
        land = m["t"] + bias  # hits on the frame or just after it: early sound is noticed 2-3x sooner than late
        cue = {"frame_t": round(m["t"], 3), "cue": m["cue"], "category": cat, "file": choice, "anchor": anchor,
               "level_db": round(level, 1)}
        cue.update(place(meas.get(choice), land, anchor, round(level, 1), a.max_tail, a.max_head,
                         var["rate"] if var else 1.0) if choice else {"at": land, "gain_db": level})
        if var:
            cue["rate"] = var["rate"]
        pan = m.get("pan") or 0.0
        if not pan and cx is not None and m["cue"] in ("transition-fast", "transition-soft", "overlay", "image"):
            pan = sfx_sense.pan_at(cx, m.get("vframe"))  # follows where the motion is; hits stay centred
        if pan:
            cue["pan"] = pan
        if speech:
            cue["over_speech"] = True
        if "planned_t" in m:
            cue["planned_t"], cue["visual_strength"] = round(m["planned_t"], 3), round(m["strength"], 2)
        elif m.get("unsnapped"):
            cue["unsnapped"] = True
        cue["why"] = m["why"] + (f"; picks {fit_why}" if fit_why else "") + (" (over speech: lowered)" if speech else "")
        plan.append(cue)
        # A riser builds into the big reveals when there is room before them.
        if a.risers and m["cue"] in ("logo", "text-big"):
            prev = kept[i - 1]["t"] + 0.3 if i else 0.0
            last_riser = max((p["frame_t"] for p in plan if p["cue"] == "riser"), default=-99)
            room = min(m["t"] - prev, 4.0)
            if room >= 1.0 and m["t"] - last_riser >= 6.0:
                rcat, rfile, _ = pick(lib, CUE["riser"][0], recent, a.prefer, meas, "riser", room)
                if rfile:
                    rm = meas.get(rfile)
                    ranchor = ANCHOR.get(rcat, "crest")
                    crest = rm[ANCHOR_KEY[ranchor]] if rm else room
                    build = min(room, crest)
                    r = {"frame_t": round(m["t"], 3), "cue": "riser", "category": rcat, "file": rfile, "anchor": ranchor,
                         "level_db": CUE["riser"][1] + a.gain_offset}
                    r.update(place(rm, m["t"], ranchor, r["level_db"], 0.12, build))
                    if rm and crest > build:  # start part-way into the build so it fits the room
                        r["in"] = round(crest - build, 3)
                        r["at"] = round(m["t"] - build, 3)
                        r["dur"] = round(build + 0.12, 3)
                        r["fade_out"] = 0.08
                    r["fade_in"] = round(min(0.4, build / 3), 3)
                    r["why"] = f"builds {build:.1f} s into {m['cue']} at {fmt_ts(m['t'])}"
                    plan.append(r)
    plan.sort(key=lambda p: p["at"])
    # A tail gets out of the way of the next hit: it fades out as the next cue's frame arrives (risers overlap on purpose).
    hits = [p for p in plan if p["cue"] != "riser" and p.get("file")]
    for cur, nxt in zip(hits, hits[1:]):
        m = meas.get(cur["file"])
        if not m or nxt["frame_t"] <= cur["frame_t"]:
            continue
        rest = cur.get("dur") or m["duration"] - cur.get("in", 0)
        room = nxt["frame_t"] + 0.05 - cur["at"]
        if room < rest - 0.01:
            cur["dur"] = round(max(room, 0.1), 3)
            cur["fade_out"] = round(min(0.2, cur["dur"] / 3), 3)
    plan = cap_layers(plan, meas, rank, a.max_layers)
    missing = sorted({p["category"] for p in plan if not p["file"]})
    save_json(a.out, {"plan": plan, "style": a.style, "library_dirs": sorted({str(Path(f).parent) for fs in lib.values() for f in fs}),
                      "missing_categories": missing})
    rows = ["# Sound design plan", "", f"Style: {a.style or 'default'} · min gap {a.min_gap} s · "
            f"levels are dB under a normalised hit (0 ≈ a dialogue peak)", "",
            "| # | frame | starts | cue | sound | anchor | level | gain | why |", "|---|---|---|---|---|---|---|---|---|"]
    if evidence:
        n_snap = sum(1 for p in plan if "planned_t" in p)
        rows[2:2] = [f"Snapped to the picture ({Path(evidence).name}): {n_snap} of "
                     f"{sum(1 for p in plan if p['cue'] not in sfx_sense.NO_SNAP)} cues moved to the frame the image "
                     f"changes; sync bias +{a.sync_bias:.0f} ms (never early).", ""]
    for i, p in enumerate(plan, 1):
        snd = Path(p["file"]).name if p["file"] else "— (missing " + p["category"] + ")"
        if p.get("in"):
            snd += f" from {p['in']:.2f} s"
        fr = fmt_ts(p["frame_t"]) + (f" (planned {fmt_ts(p['planned_t'])})" if "planned_t" in p and
                                     abs(p["planned_t"] - p["frame_t"]) >= 0.005 else " (no visual change found)"
                                     if p.get("unsnapped") else "")
        rows.append(f"| {i} | {fr} | {fmt_ts(p['at'])} | {p['cue']} | {snd} | {p.get('anchor', '')} "
                    f"| {p.get('level_db', '')} dB | {p['gain_db']} dB | {p['why']} |")
    if missing:
        rows += ["", f"Missing categories: {', '.join(missing)}. Add recordings (`vs fetch search \"<category>\" --type sfx`, "
                     "`vs add <files> --as sfx`) or render earshot's bank (`vs sfx bank --from earshot`), then re-plan."]
    Path(a.out).with_suffix(".md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    if a.sheet:
        cue_sheet(plan, a.sheet if isinstance(a.sheet, str) else (evidence or ""), Path(a.out).with_suffix(".png"))
    print(f"{len(plan)} cues ({sum(1 for p in plan if p['file'])} with sounds) -> {a.out}, {Path(a.out).with_suffix('.md')}")
    if missing:
        print(f"missing sounds for: {', '.join(missing)}", file=sys.stderr)


def cap_layers(plan, meas, rank, limit):
    """Murch: listeners follow about 2.5 layers of similar sound; at 3+ they blur into one. Keep at most `limit`
    sounds ringing at once (a riser and its hit count as two); drop the least important extra."""
    def end(p):
        m = meas.get(p["file"]) or {}
        return p["at"] + (p.get("dur") or (m.get("duration", 0.5) / p.get("rate", 1.0)) - p.get("in", 0))
    prio = lambda p: rank.index(p["cue"]) if p["cue"] in rank else len(rank)  # noqa: E731
    kept = []
    for p in sorted(plan, key=lambda p: p["at"]):
        if not p.get("file"):
            kept.append(p)
            continue
        active = [q for q in kept if q.get("file") and end(q) > p["at"] + 0.02]
        if len(active) >= limit:
            worst = max(active + [p], key=prio)
            if worst is p:
                continue
            kept.remove(worst)
        kept.append(p)
    return kept


def cue_sheet(plan, video, out_png):
    """One frame per cue (the frame the sound lands on), numbered like sfx_plan.md, for Claude to judge meaning:
    does this moment deserve a sound, and is it the right kind? (Vision models judge meaning well, timing badly.)"""
    if not video:
        print("--sheet needs a render: pass --snap out/draft.mp4 (or --sheet <video>)", file=sys.stderr)
        return None
    import archive  # noqa: E402  (shared keyframe + contact-sheet helpers)
    td = out_png.with_name(out_png.stem + "_frames")
    imgs = archive.keyframes(video, [p["frame_t"] + 0.02 for p in plan], td, "vs")
    labels = [f"#{i} {fmt_ts(p['frame_t'])[3:]} {p['cue']} {Path(p['file']).stem[:14] if p['file'] else '-'}"
              for i, p in enumerate(plan, 1)]
    png = archive.sheet(imgs, labels, out_png)
    if png:
        print(f"cue sheet -> {png}")
    return png


def build_mix(plan, total):
    inputs, filt, labs = [], [], []
    for j, p in enumerate(x for x in plan if x.get("file")):
        inputs += ["-i", p["file"]]
        filt.append(f"[{j}:a]{sfx_chain(p)}[s{j}]")
        labs.append(f"[s{j}]")
    if not labs:
        die("plan has no sounds to place")
    filt.append(f"{''.join(labs)}amix=inputs={len(labs)}:normalize=0:duration=longest,apad,atrim=0:{total:.3f}[sfx]")
    return inputs, filt


def landing(fx, total=None):
    """Render one placed cue alone through the same filter chain as apply/render and measure where its anchor lands."""
    meas_ = analyse([fx["file"]]).get(fx["file"])
    if not meas_:
        return None
    at = float(fx["at"])
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", fx["file"], "-filter_complex", sfx_chain(dict(fx, at=0)),
                        "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True)
    a_ = array.array("h", p.stdout)
    win = 160
    rms = [math.sqrt(sum(x * x for x in a_[i:i + win]) / win) for i in range(0, len(a_) - win, win)]
    if not rms or max(rms) == 0:
        return None
    seg = rms
    top = max(seg)
    if fx.get("anchor") == "onset":
        k = next(i for i, r in enumerate(seg) if r >= top * 0.1)
    else:
        hit = [math.sqrt(sum(r * r for r in seg[i:i + 5]) / len(seg[i:i + 5])) for i in range(len(seg))]
        hi = max(range(len(hit)), key=hit.__getitem__)
        k = (hi if fx.get("anchor") == "crest" else next(i for i, h in enumerate(hit) if h >= hit[hi] * 0.708)) + 2
    return round(at + k / 100, 3)


def cmd_check(a):
    """Where each sound really lands vs the frame it belongs to. EBU R37: sound may lead the picture by at most 40 ms
    and lag by at most 60 ms; ITU-R BT.1359 detectability +45 / -125 ms. Early is the error viewers notice."""
    need("ffmpeg")
    plan = [p for p in load_json(a.plan)["plan"] if p.get("file")]
    rows = ["| # | cue | frame | lands | offset | verdict |", "|---|---|---|---|---|---|"]
    offs, bad = [], 0
    for i, p in enumerate(plan, 1):
        t = landing(p)
        if t is None:
            continue
        off = round((t - p["frame_t"]) * 1000)
        offs.append(off)
        verdict = "EARLY" if off < -a.max_lead else "LATE" if off > a.max_lag else "ok"
        bad += verdict != "ok"
        rows.append(f"| {i} | {p['cue']} | {fmt_ts(p['frame_t'])} | {fmt_ts(t)} | {off:+d} ms | {verdict} |")
    if not offs:
        die("nothing to check")
    within = lambda ms: sum(abs(o) <= ms for o in offs) / len(offs) * 100  # noqa: E731
    summary = (f"{len(offs)} sounds: {within(20):.0f} % within 20 ms, {within(40):.0f} % within one 25 fps frame (40 ms), "
               f"{bad} outside -{a.max_lead}/+{a.max_lag} ms (EBU R37). Mean offset {sum(offs) / len(offs):+.0f} ms.")
    out = Path(a.plan).with_name(Path(a.plan).stem + "_check.md")
    out.write_text("# Sync check\n\n" + summary + "\n\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(summary)
    print(f"-> {out}")
    if bad:
        sys.exit(1)


def cmd_apply(a):
    need("ffmpeg")
    plan = load_json(a.plan)["plan"]
    if not any(p_.get("file") for p_ in plan):
        print(f"plan has no sounds to place: {a.out} not written (use {a.video} as it is)")
        return
    info = probe(a.video)
    inputs, filt = build_mix(plan, info["duration"])
    n = len([p for p in plan if p.get("file")])
    if a.stem:
        Path(a.stem).parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[sfx]",
             "-c:a", "pcm_s24le", a.stem])
        print(f"SFX stem -> {a.stem}")
    vin = ["-i", a.video]
    if info["has_audio"]:
        mix = f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo[orig];[orig][sfx]amix=inputs=2:normalize=0:duration=first"
    else:
        mix = "[sfx]anull"
    if a.loudnorm is not None:
        mix += f",loudnorm=I={a.loudnorm}:TP=-1.5:LRA=11"
    run(["ffmpeg", "-y", "-v", "error", *inputs, *vin, "-filter_complex", ";".join(filt) + f";{mix}[out]",
         "-map", f"{n}:v", "-map", "[out]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.out])
    print(f"{n} sounds placed -> {a.out} (picture untouched, original audio kept)")


def cmd_merge(a):
    edl = load_json(a.edl)
    plan = load_json(a.plan)["plan"]
    edl["sfx"] = [s for s in edl.get("sfx", []) if not s.get("auto")] + \
        [dict({k: p[k] for k in ("file", "at", "gain_db", "in", "dur", "fade_in", "fade_out", "pan", "rate") if p.get(k)},
              at=p["at"], gain_db=p["gain_db"], auto=True, cue=p["cue"]) for p in plan if p.get("file")]
    save_json(a.out, edl)
    print(f"{sum(1 for s in edl['sfx'] if s.get('auto'))} sfx entries -> {a.out} (render it with vs render)")


def cmd_library(a):
    lib = library(a.library, a.project_dir)
    if not lib:
        print("no categorised sounds found. Add some: vs add <files> --as sfx --library | vs fetch search whoosh --type sfx")
    for cat in CATEGORIES:
        fs = lib.get(cat, [])
        print(f"{cat:8} {len(fs):3}  " + ", ".join(Path(f).name for f in fs[:4]) + (" …" if len(fs) > 4 else ""))


def cmd_analyse(a):
    files = []
    for x in a.paths:
        pth = Path(x)
        files += sorted(str(f) for f in pth.rglob("*") if f.suffix.lower() in AUDIO_EXT) if pth.is_dir() else [str(pth)]
    need("ffmpeg")
    meas = analyse(files)
    print(f"{'sound':34} {'cat':7} {'len':>6} {'onset':>6} {'hit':>6} {'crest':>6} {'hit dB':>7} {'peak dB':>8} {'norm':>6}")
    for f in files:
        m = meas.get(f)
        if not m:
            print(f"{Path(f).name[:34]:34} (silent or unreadable)")
            continue
        print(f"{Path(f).name[:34]:34} {categorise(Path(f).stem) or '-':7} {m['duration']:6.2f} {m['onset']:6.2f} "
              f"{m['hit_t']:6.2f} {m['crest_t']:6.2f} {m['hit_db']:7.1f} {m['peak_db']:8.1f} {norm_gain(m):+6.1f}")


def earshot_cmd():
    home = Path(os.environ.get("VS_EARSHOT_HOME", Path.home() / ".cache" / "video-studio" / "earshot"))
    py = home / ".venv" / "bin" / "python"
    if not py.exists():
        die("earshot is not installed. Run: vs setup --earshot")
    return [str(py), "-m", "earshot"]


def cmd_bank(a):
    """Render earshot's code-made sound bank into the library, named by category so `plan` can use them."""
    if a.source != "earshot":
        die("only --from earshot is supported")
    out = workspace() / "library" / "assets" / "sfx" / "earshot"
    out.mkdir(parents=True, exist_ok=True)
    p = subprocess.run([*earshot_cmd(), "sfx", "list", "--json"], capture_output=True, text=True)
    if p.returncode != 0:
        die(f"earshot sfx list failed: {p.stderr[-300:]}")
    try:
        data = json.loads(p.stdout)
    except json.JSONDecodeError:
        data = p.stdout.split()
    items = data.get("sounds", data.get("items", data)) if isinstance(data, dict) else data
    ids = [i.get("id") or i.get("name") if isinstance(i, dict) else str(i) for i in items]
    ids = [i for i in ids if i and categorise(i)]
    if a.limit:
        ids = ids[: a.limit]
    made = 0
    for i in ids:
        dest = out / f"{slug_id(i)}.wav"
        if dest.exists():
            continue
        r = subprocess.run([*earshot_cmd(), "sfx", "render", i, "-o", str(dest)], capture_output=True, text=True)
        made += r.returncode == 0
    led = workspace() / "library" / "assets" / "credits.json"
    data = load_json(led) if led.exists() else {"assets": []}
    data["assets"] = [x for x in data["assets"] if x.get("provider") != "earshot"] + [{
        "file": str(out), "kind": "sfx", "provider": "earshot", "title": "earshot sound bank (code-generated)",
        "license": "MIT (generated by earshot, no recordings)", "page_url": "https://github.com/Leonxlnx/earshot",
        "attribution_required": False}]
    save_json(led, data)
    print(f"rendered {made} new sounds ({len(ids)} matching categories) -> {out}")


def slug_id(s):
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--edl")
    p.add_argument("--hyperframes", help="HyperFrames project folder (index.html + compositions/)")
    p.add_argument("--hyperframes-offset", type=float, default=0.0, help="where the composition starts in the edit (s)")
    p.add_argument("--video", help="a finished render: place sounds on scene changes")
    p.add_argument("--threshold", type=float, default=0.3,
                   help="--video: a scene score that is always a cut; weaker cuts are found adaptively")
    p.add_argument("--beats")
    p.add_argument("--on-beats", type=int, default=0, help="add an impact every Nth downbeat")
    p.add_argument("--style", choices=sorted(STYLES), help="density/level preset; explicit flags override it")
    p.add_argument("--every-cut", action="store_true", default=None,
                   help="soft tick on every hard cut (montages); off for talking heads")
    p.add_argument("--min-gap", type=float, help="minimum seconds between sounds (default 0.35, or the style's)")
    p.add_argument("--gain-offset", type=float, help="raise/lower every cue (dB)")
    p.add_argument("--risers", action="store_true", default=None, help="build a riser into logo / big-title reveals")
    p.add_argument("--words", help="vs transcribe JSON of the edit itself (output time): cues over speech are "
                                   "lowered, and the style's minor cues are dropped there")
    p.add_argument("--speech-duck", type=float, help="dB lower for a cue that lands on a word (default 6)")
    p.add_argument("--max-tail", type=float, default=2.0, help="seconds a sound may ring after its anchor (faded)")
    p.add_argument("--snap", help="a render of the edit (out/draft.mp4): move every cue to the frame the picture "
                                  "actually changes (cuts, appearances, motion peaks)")
    p.add_argument("--sync-bias", type=float, default=10.0,
                   help="ms after the frame that hits land (0..40; never negative: early sound is noticed first)")
    p.add_argument("--max-layers", type=int, default=2, help="sounds ringing at once, at most (Murch: ~2.5)")
    p.add_argument("--sheet", nargs="?", const=True, default=None,
                   help="write <plan>.png with the frame at every cue (uses --snap/--video or the given video)")
    p.add_argument("--max-head", type=float, default=0.8,
                   help="seconds of build-up a sound may play before its anchor; a longer one starts part-way in")
    p.add_argument("--library", action="append", help="extra folder of SFX (repeatable)")
    p.add_argument("--prefer", help="prefer sounds whose path contains these words, e.g. cinematic,studio or kenney")
    p.add_argument("--library-only", action="store_true",
                   help="use only the --library folders (a client's brand pack), not the project/shared/bundled sounds")
    p.add_argument("--project-dir", help="project folder (uses its assets/sfx)")
    p.add_argument("-o", "--out", required=True)
    ap_ = sub.add_parser("apply")
    ap_.add_argument("video")
    ap_.add_argument("--plan", required=True)
    ap_.add_argument("-o", "--out", required=True)
    ap_.add_argument("--stem", help="also write the SFX alone as a WAV (for Premiere / After Effects / Resolve)")
    ap_.add_argument("--loudnorm", type=float, nargs="?", const=-14.0)
    m = sub.add_parser("merge")
    m.add_argument("edl")
    m.add_argument("--plan", required=True)
    m.add_argument("-o", "--out", required=True)
    lb = sub.add_parser("library")
    lb.add_argument("--library", action="append")
    lb.add_argument("--project-dir")
    ck = sub.add_parser("check")
    ck.add_argument("--plan", required=True)
    ck.add_argument("--max-lead", type=int, default=40, help="ms a sound may come before its frame (EBU R37: 40)")
    ck.add_argument("--max-lag", type=int, default=60, help="ms a sound may come after its frame (EBU R37: 60)")
    an = sub.add_parser("analyse", aliases=["analyze"])
    an.add_argument("paths", nargs="+")
    b = sub.add_parser("bank")
    b.add_argument("--from", dest="source", default="earshot")
    b.add_argument("--limit", type=int)
    a = ap.parse_args()
    if getattr(a, "project_dir", None) is None and getattr(a, "edl", None):
        parts = Path(a.edl).resolve().parts
        if "projects" in parts and len(parts) > parts.index("projects") + 1:
            a.project_dir = str(Path(*parts[: parts.index("projects") + 2]))
    {"plan": cmd_plan, "apply": cmd_apply, "merge": cmd_merge, "library": cmd_library, "bank": cmd_bank,
     "analyse": cmd_analyse, "analyze": cmd_analyse, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    main()
