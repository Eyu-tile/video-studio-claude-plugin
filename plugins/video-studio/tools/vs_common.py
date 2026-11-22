"""Shared helpers for the video-studio tools. Stdlib only (numpy is imported lazily where needed)."""
import json
import shutil
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

FILLERS = {
    "um", "umm", "uh", "uhh", "erm", "er", "ah", "hmm", "mm", "mhm",
    "like,", "you know", "i mean", "sort of", "kind of",
}
# Single-token fillers that are safe to drop automatically. Multi-word ones
# above are only flagged; the planner decides.
HARD_FILLERS = {"um", "umm", "uh", "uhh", "erm", "er", "ah", "hmm", "mm", "mhm"}

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic"}

ASPECTS = {"16:9": (1920, 1080), "9:16": (1080, 1920), "1:1": (1080, 1080), "4:5": (1080, 1350),
           "4:3": (1440, 1080), "21:9": (2560, 1080)}

# Platform delivery presets: aspect, loudness target, max length (s), notes.
PRESETS = {
    "reels":     {"aspect": "9:16", "lufs": -14, "max": 90,   "fps": 30, "note": "Instagram Reels"},
    "tiktok":    {"aspect": "9:16", "lufs": -14, "max": 600,  "fps": 30, "note": "TikTok"},
    "shorts":    {"aspect": "9:16", "lufs": -14, "max": 180,  "fps": 30, "note": "YouTube Shorts"},
    "story":     {"aspect": "9:16", "lufs": -14, "max": 60,   "fps": 30, "note": "IG/FB story (60 s per card)"},
    "youtube":   {"aspect": "16:9", "lufs": -14, "max": None, "fps": None, "note": "YouTube long-form"},
    "youtube-4k": {"aspect": "16:9", "lufs": -14, "max": None, "fps": None, "scale": 2, "note": "YouTube 2160p"},
    "linkedin":  {"aspect": "1:1",  "lufs": -14, "max": 600,  "fps": 30, "note": "LinkedIn feed (1:1 or 4:5)"},
    "feed":      {"aspect": "4:5",  "lufs": -14, "max": 60,   "fps": 30, "note": "IG/FB feed"},
    "x":         {"aspect": "16:9", "lufs": -14, "max": 140,  "fps": 30, "note": "X / Twitter"},
    "podcast":   {"aspect": "16:9", "lufs": -16, "max": None, "fps": None, "note": "video podcast"},
    "broadcast": {"aspect": "16:9", "lufs": -23, "max": None, "fps": None, "note": "EBU R128 broadcast"},
}

# UI safe zones per platform, as fractions of the frame to keep free of text, logos and key action.
# Meta Reels ads: 14% top, 35% bottom, 6% sides (as restated by ad-spec guides; Meta's own spec page
# was not reachable when this was written). TikTok publishes templates, not numbers: these are
# conservative defaults with the right-side action rail. Check the platform template for new formats.
SAFE_ZONES = {
    "reels":   {"top": 0.14, "bottom": 0.35, "left": 0.06, "right": 0.06},
    "story":   {"top": 0.14, "bottom": 0.20, "left": 0.06, "right": 0.06},
    "tiktok":  {"top": 0.12, "bottom": 0.30, "left": 0.06, "right": 0.15},
    "shorts":  {"top": 0.12, "bottom": 0.25, "left": 0.06, "right": 0.15},
    "feed":    {"top": 0.05, "bottom": 0.12, "left": 0.05, "right": 0.05},
    "default_vertical": {"top": 0.12, "bottom": 0.30, "left": 0.06, "right": 0.15},
}


def safe_zone(preset=None, aspect=None):
    """Safe zone for a preset (or a generic one for vertical aspects); None for landscape."""
    if preset in SAFE_ZONES:
        return SAFE_ZONES[preset]
    a = PRESETS.get(preset, {}).get("aspect") or aspect
    if a == "9:16":
        return SAFE_ZONES["default_vertical"]
    return None


# Colour grades as ffmpeg filter chains (applied after scaling, before overlays).
GRADES = {
    "none": "",
    "natural": "eq=contrast=1.04:saturation=1.08",
    "punchy": "eq=contrast=1.12:saturation=1.28:gamma=0.98,unsharp=5:5:0.4",
    "bright": "eq=brightness=0.04:contrast=1.03:gamma=1.06:saturation=1.08",
    "warm": "colortemperature=temperature=5200,eq=saturation=1.08",
    "cool": "colortemperature=temperature=7600,eq=saturation=1.04",
    "cinematic": "colorbalance=rs=-0.06:bs=0.08:rh=0.08:bh=-0.07,eq=contrast=1.08:saturation=0.92,vignette=PI/5",
    "teal-orange": "colorbalance=rs=-0.1:gs=-0.02:bs=0.12:rh=0.12:gh=0.02:bh=-0.1,eq=contrast=1.06",
    "moody": "eq=contrast=1.1:brightness=-0.03:saturation=0.8,vignette=PI/4",
    "vintage": "curves=preset=vintage,eq=saturation=0.85",
    "film": "curves=preset=medium_contrast,eq=saturation=0.9,noise=alls=6:allf=t",
    "bw": "hue=s=0,eq=contrast=1.15",
    "bw-contrast": "hue=s=0,curves=preset=strong_contrast",
    "vibrant": "vibrance=intensity=0.35,eq=contrast=1.05",
    "auto": "normalize=blackpt=black:whitept=white:smoothing=24:independence=0.4",
}

# Voice clean-up chain: rumble cut, broadband denoise, de-ess, gentle compression.
VOICE_ENHANCE = ("highpass=f=80,afftdn=nf=-25:tn=1,deesser=i=0.4,"
                 "acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2")


def sfx_chain(fx):
    """ffmpeg filter chain (no labels) that places one sound effect: optional trim (`in`, `dur`), fades
    (`fade_in`, `fade_out`), stereo `pan` (-1 left .. 1 right), `gain_db`, then a delay to `at` seconds."""
    f = ["aresample=48000", "aformat=channel_layouts=stereo"]
    rate = float(fx.get("rate", 1) or 1)
    if abs(rate - 1) > 1e-4:  # pitch/speed variation; in/dur/fades below are in the varied file's time
        f.append(f"asetrate={48000 * rate:.0f},aresample=48000")
    start, dur = float(fx.get("in", 0) or 0), fx.get("dur")
    if start > 0 or dur:
        f.append(f"atrim=start={start:.3f}" + (f":duration={float(dur):.3f}" if dur else "") + ",asetpts=PTS-STARTPTS")
    if fx.get("fade_in"):
        f.append(f"afade=t=in:d={float(fx['fade_in']):.3f}")
    if fx.get("fade_out") and dur:
        fo = min(float(fx["fade_out"]), float(dur))
        f.append(f"afade=t=out:st={float(dur) - fo:.3f}:d={fo:.3f}")
    pan = max(-1.0, min(1.0, float(fx.get("pan", 0) or 0)))
    if pan:
        f.append(f"pan=stereo|c0={min(1, 1 - pan):.3f}*c0|c1={min(1, 1 + pan):.3f}*c1")
    f.append(f"volume={float(fx.get('gain_db', -6))}dB")
    f.append(f"adelay={int(max(float(fx['at']), 0) * 1000)}:all=1")
    return ",".join(f)


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def need(binary):
    if shutil.which(binary) is None:
        die(f"'{binary}' not found on PATH. Run: vs setup")


def need_numpy():
    try:
        import numpy
        return numpy
    except ImportError:
        die("numpy is required for this command. Run: vs setup")


def run(cmd, capture=True):
    """Run a command, return CompletedProcess. Exits with the stderr tail on failure."""
    p = subprocess.run(cmd, capture_output=capture, text=True)
    if p.returncode != 0:
        tail = (p.stderr or "")[-2500:]
        die(f"command failed ({p.returncode}): {' '.join(map(str, cmd))}\n{tail}")
    return p


@lru_cache(maxsize=1)
def ffmpeg_filters():
    need("ffmpeg")
    out = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True).stdout
    names = set()
    for line in out.splitlines():
        parts = line.split()
        # Filter rows look like " T.C xfade  VV->V  description"; flags are 3 chars of T/S/C/.
        if len(parts) > 2 and len(parts[0]) == 3 and set(parts[0]) <= set("TSC.") and "->" in parts[2]:
            names.add(parts[1])
    return names


def has_filter(name):
    return name in ffmpeg_filters()


def is_image(path):
    return Path(path).suffix.lower() in IMAGE_EXT


@lru_cache(maxsize=256)
def probe(path):
    """Duration, display size (rotation applied), fps, audio/video presence, HDR flag."""
    need("ffprobe")
    p = run(["ffprobe", "-v", "error", "-print_format", "json",
             "-show_format", "-show_streams", str(path)])
    info = json.loads(p.stdout)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    fps, w, h, rot, hdr, vfr, transfer = 30.0, 0, 0, 0, False, False, None
    if v:
        w, h = int(v.get("width", 0)), int(v.get("height", 0))
        for key in ("avg_frame_rate", "r_frame_rate"):
            n, _, d = v.get(key, "0/0").partition("/")
            if d and float(d) and float(n):
                fps = float(n) / float(d)
                break
        n1, _, d1 = v.get("avg_frame_rate", "0/0").partition("/")
        n2, _, d2 = v.get("r_frame_rate", "0/0").partition("/")
        if d1 and d2 and float(d1) and float(d2) and float(n1):
            vfr = abs(float(n1) / float(d1) - float(n2) / float(d2)) > 0.5
        rot = int(float(v.get("tags", {}).get("rotate", 0)))
        for sd in v.get("side_data_list", []):
            if "rotation" in sd:
                rot = int(sd["rotation"])
        if abs(rot) % 180 == 90:
            w, h = h, w
        hdr = v.get("color_transfer") in ("arib-std-b67", "smpte2084")
        transfer = v.get("color_transfer") if hdr else None
    dur = float(info["format"].get("duration", 0.0) or 0.0)
    if is_image(path):
        dur = 0.0
    return {
        "duration": dur, "width": w, "height": h, "fps": round(fps, 3), "rotation": rot,
        "has_video": v is not None, "has_audio": a is not None, "hdr": hdr, "transfer": transfer, "vfr": vfr,
        "vcodec": v.get("codec_name") if v else None,
        "channels": int(a.get("channels", 0)) if a else 0,
    }


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def fmt_ts(t):
    """Seconds -> MM:SS.mmm"""
    m, s = divmod(max(t, 0.0), 60)
    return f"{int(m):02d}:{s:06.3f}"


def norm_word(w):
    return w.strip().lower().strip(".,!?;:\"'()[]")


def edl_segments(edl):
    """Yield (src, start, end, seg) with defaults resolved. Image segments start at 0.
    A freeze segment ({"start": t, "freeze": 1.5}) may omit `end`."""
    default_src = edl.get("source")
    for seg in edl["segments"]:
        src = seg.get("src", default_src)
        if src is None:
            die("segment has no 'src' and EDL has no 'source'")
        a = float(seg.get("start", 0.0))
        if "end" not in seg and not seg.get("freeze"):
            die(f"segment {src} @ {a}: missing 'end'")
        b = float(seg["end"]) if "end" in seg else a + 0.04
        yield src, a, b, seg


def seg_speed(seg):
    s = seg.get("speed", 1.0)
    if isinstance(s, list):  # speed ramp: average for callers that only need a number
        return max(sum(float(p[1]) for p in s) / len(s), 0.05)
    return max(float(s), 0.05)


def transition_dur(seg):
    t = seg.get("transition_in")
    if not t:
        return 0.0
    return float(t.get("dur", 0.4)) if isinstance(t, dict) else 0.4


def interp(points, x):
    """Linear interpolation over [[x, y], ...] (clamped at the ends)."""
    pts = sorted((float(p[0]), float(p[1])) for p in points)
    if x <= pts[0][0]:
        return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
    return pts[-1][1]


RAMP_PIECES = 6  # constant-speed pieces per keyframe interval (audio, captions); video is exact


def ramp_points(seg, length):
    """Speed keyframes [[t, speed], ...] (t: source seconds from the segment start), clamped
    to the segment and extended flat to both ends."""
    pts = sorted((min(max(float(p[0]), 0.0), length), max(float(p[1]), 0.05)) for p in seg["speed"])
    if pts[0][0] > 0:
        pts.insert(0, (0.0, pts[0][1]))
    if pts[-1][0] < length:
        pts.append((length, pts[-1][1]))
    return pts


def ramp_intervals(pts):
    """[(t0, t1, s0, k, out0)]: speed s0 + k*(t - t0) on [t0, t1]; out0 = output time at t0."""
    out, acc = [], 0.0
    for (t0, s0), (t1, s1) in zip(pts, pts[1:]):
        if t1 <= t0:
            continue
        k = (s1 - s0) / (t1 - t0)
        out.append((t0, t1, s0, k, acc))
        acc += _ramp_int(t1 - t0, s0, k)
    return out


def _ramp_int(d, s0, k):
    """Output seconds for d source seconds when speed goes linearly s0 -> s0 + k*d."""
    import math
    if abs(k) < 1e-9:
        return d / s0
    return math.log((s0 + k * d) / s0) / k


def ramp_out(pts, x):
    """Output seconds after x source seconds of a ramped segment."""
    for t0, t1, s0, k, o in ramp_intervals(pts):
        if x <= t1:
            return o + _ramp_int(max(x - t0, 0.0), s0, k)
    return ramp_out(pts, pts[-1][0])


def ramp_setpts(pts, var="T"):
    """setpts expression (output seconds) for source-relative time `var` of a ramped segment."""
    expr = None
    for t0, t1, s0, k, o in reversed(ramp_intervals(pts)):
        d = f"(({var})-{t0:.6g})"
        piece = f"{o:.6g}+{d}/{s0:.6g}" if abs(k) < 1e-9 else f"{o:.6g}+log(({s0:.6g}+({k:.6g})*{d})/{s0:.6g})/({k:.6g})"
        expr = piece if expr is None else f"if(lt({var},{t1:.6g}),{piece},{expr})"
    return expr


def expand_ramp(a, b, seg):
    """Split a speed-ramped segment into constant-average-speed pieces.

    `speed` is [[t, speed], ...] with t in seconds from the segment's source start. Returns
    [(a_i, b_i, speed_i, out_offset_i)], where out_offset is the piece's output time inside
    the original segment. Piece lengths follow the exact ramp, so the pieces add up to the
    length the renderer produces."""
    pts = ramp_points(seg, b - a)
    marks = []
    for (t0, _), (t1, _) in zip(pts, pts[1:]):
        if t1 > t0:
            marks += [t0 + (t1 - t0) * i / RAMP_PIECES for i in range(RAMP_PIECES)]
    marks.append(b - a)
    out = []
    for x0, x1 in zip(marks, marks[1:]):
        o0, o1 = ramp_out(pts, x0), ramp_out(pts, x1)
        out.append((a + x0, a + x1, (x1 - x0) / max(o1 - o0, 1e-6), o0))
    return out


def timeline(edl):
    """Output-timeline placement of every segment, accounting for speed and transitions.

    Returns a list of dicts: {src, start, end, speed, out_start, out_end, seg, overlap, ...}.
    A transition on segment k overlaps it with segment k-1 by its duration, so out_start moves
    earlier. Speed-ramped segments become several constant-speed pieces: every piece after the
    first has `join` True (a seamless continuation, not a cut). `kf_off` is the piece's output
    time inside its original segment; `freeze` is the hold length of a freeze frame.
    """
    out, t = [], 0.0
    for k, (src, a, b, seg) in enumerate(edl_segments(edl)):
        if isinstance(seg.get("speed"), list) and not seg.get("freeze"):
            pieces = expand_ramp(a, b, seg)
        else:
            pieces = [(a, b, seg_speed(seg), 0.0)]
        for i, (pa, pb, sp, off) in enumerate(pieces):
            freeze = float(seg["freeze"]) if seg.get("freeze") else 0.0
            length = freeze if freeze else (pb - pa) / sp
            td = 0.0
            if k and i == 0:
                td = transition_dur(seg)
                td = min(td, length / 2, (out[-1]["out_end"] - out[-1]["out_start"]) / 2 if out else 0)
            start = t - td
            out.append({"src": src, "start": pa, "end": pb, "speed": 1.0 if freeze else sp,
                        "out_start": start, "out_end": start + length, "seg": seg, "overlap": td,
                        "join": i > 0, "first": i == 0, "last": i == len(pieces) - 1,
                        "kf_off": off, "freeze": freeze, "index": k})
            t = start + length
    return out


def cut_points(tl):
    """Timeline items that start a new shot (ramp continuations excluded)."""
    return [it for it in tl if not it["join"]]


EASE = {
    "linear": "{u}",
    "in": "({u})*({u})",
    "out": "(1-(1-{u})*(1-{u}))",
    "inout": "(3*({u})*({u})-2*({u})*({u})*({u}))",
}


def kf_expr(points, tvar="t", default_ease="inout"):
    """ffmpeg expression for keyframes [[t, v], [t, v, "ease"], ...] in the variable `tvar`.

    Holds the first value before the first key and the last value after the last; the ease on a
    key shapes the move INTO that key (linear, in, out, inout). Commas are safe inside the
    single-quoted option values the callers write."""
    pts = sorted(points, key=lambda p: float(p[0]))
    if not pts:
        raise ValueError("empty keyframe list")
    if len(pts) == 1:
        return f"({float(pts[0][1]):.6g})"
    expr = f"({float(pts[-1][1]):.6g})"
    for i in range(len(pts) - 1, 0, -1):
        t0, v0 = float(pts[i - 1][0]), float(pts[i - 1][1])
        t1, v1 = float(pts[i][0]), float(pts[i][1])
        ease = pts[i][2] if len(pts[i]) > 2 else default_ease
        if t1 <= t0:
            continue
        u = f"(({tvar})-{t0:.6g})/{t1 - t0:.6g}"
        shaped = EASE.get(ease, EASE["linear"]).format(u=u)
        expr = f"if(lt({tvar},{t1:.6g}),({v0:.6g})+({v1 - v0:.6g})*{shaped},{expr})"
    return f"if(lt({tvar},{float(pts[0][0]):.6g}),({float(pts[0][1]):.6g}),{expr})"


def total_duration(edl):
    tl = timeline(edl)
    return tl[-1]["out_end"] if tl else 0.0


def resolve(base, p):
    p = Path(p)
    return p if p.is_absolute() else (Path(base) / p)


def detect_cuts(path, threshold=0.3):
    """Hard-cut times (s). PySceneDetect's adaptive detector when installed (vs setup --ai), else
    ffmpeg's scene score. `threshold` is the ffmpeg scale (0.2 sensitive .. 0.5 hard cuts only)."""
    import importlib.util
    import re
    if importlib.util.find_spec("scenedetect") and not __import__("os").environ.get("VS_NO_AI"):
        try:
            from scenedetect import AdaptiveDetector, detect
            scenes = detect(str(path), AdaptiveDetector(adaptive_threshold=1.5 + 10 * threshold))
            return [s[0].get_seconds() for s in scenes[1:]]
        except Exception as e:  # noqa: BLE001 - fall back to ffmpeg on any detector problem
            print(f"warning: PySceneDetect failed ({e}); using ffmpeg", file=sys.stderr)
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-an", "-vf",
             f"scale=320:-2,select='gt(scene,{threshold})',showinfo", "-f", "null", "-"])
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", p.stderr)]
