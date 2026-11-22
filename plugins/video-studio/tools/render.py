#!/usr/bin/env python3
"""Render an EDL to video with ffmpeg. Deterministic: same EDL, same output.

Stage 1 (shots): each segment is cut frame-accurately from its source, stabilised, framed
(static crop, or keyframed zoom / pan / rotation), graded, retimed (constant speed, speed
ramp, reverse, freeze) and joined (hard cuts or transitions) with its dialogue, including
J/L cuts. Stage 2 (finish): blur/pixelate regions, overlays (chroma key, keyframed
position, fades), texts, captions, voice clean-up, sound effects, audio tracks with volume
automation and ducking, and loudness normalisation.

Long edits render stage 1 in chunks (split at hard cuts) in parallel, cached by content, so
a change to one shot re-renders only its chunk.

EDL reference: skills/video-edit/references/edl.md. Summary:
{
  "source": "raw/a.mp4",
  "segments": [{
     "src": "...", "start": 1.2, "end": 6.8,    source seconds (images: start 0, end = duration)
     "speed": 1.0 | [[0, 1], [1.5, 0.3], [3, 1]], constant, or a ramp: [source s from start, speed]
     "reverse": false, "freeze": 1.5,            play backwards | hold the frame at `start` for 1.5 s
     "fit": "cover"|"contain"|"blur", "focus": [0.5, 0.4], "zoom": 1.0, "zoom_to": 1.15,
     "kf": {"zoom": [[0, 1], [2, 1.2]], "x": [[0, 0.3], [2, 0.7]], "y": [...], "rotate": [[0, 0], [1, 3]]},
     "grade": "punchy", "lut": "luts/x.cube", "stabilize": false | true | "strong",
     "volume_db": 0, "mute": false, "audio_lead": 0.5, "audio_tail": 0.8,   J-cut / L-cut seconds
     "transition_in": {"type": "fade", "dur": 0.4}
  }],
  "grade", "lut", "reframe", "fit",
  "overlays": [{"file", "start", "end", "in", "x", "y", "w", "fit", "focus", "opacity",
                "key": "green" | {"color": "#00FF00", "similarity": 0.12, "blend": 0.08},
                "fade_in": 0.3, "fade_out": 0.3, "kf": {"x": [[0, -400], [0.5, 60]], "y": [...]}}],
  "blurs": [{"start", "end", "x", "y", "w", "h", "mode": "blur"|"pixelate", "strength": 20, "kf": {"x", "y"}}],
  "texts": [...], "sfx": [...],
  "music": {"file", "gain_db", "duck", "start", "fade_out"},
  "tracks": [{"name": "ambience", "gain_db": -24, "gain": [[0, -30], [4, -18]], "duck": false,
              "clips": [{"file", "at", "in", "dur", "gain_db", "fade_in", "fade_out", "loop"}]}],
  "audio_track": {"src", "start", "gain_db", "follow", "offset"},
  "audio": {"enhance": true, "gain": [[t, dB], ...]}
}

Usage:
  vs render work/edl.json -o out/draft.mp4 --preview            (uses proxies from `vs proxy`)
  vs render work/edl.json -o out/final.mp4 --preset reels --captions work/captions.ass
  vs render work/edl.json -o out/part.mp4 --range 20-35 --preview
  vs render work/edl_v2.json -o out/final_v2.mp4 --since out/final_v1.mp4   revision: re-encode only the shots
        that changed (between the cuts around them), copy the rest of v1's picture, remix the audio in full
  vs render work/edl.json -o out/final.mov --codec prores --10bit
  vs render work/edl.json -o out/hdr.mp4 --codec h265 --hdr     (keep HDR10 / HLG)
  vs render work/edl.json -o out/long.mp4 --chunks 60 --jobs 4  (force chunking; default: auto)
"""
import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import shlex
import shutil
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import splice  # noqa: E402
from vs_common import (ASPECTS, GRADES, PRESETS, VOICE_ENHANCE, die, sfx_chain, fmt_ts, has_filter,  # noqa: E402
                       is_image, kf_expr, load_json, need, probe, ramp_points, ramp_setpts, run, safe_zone, save_json,
                       timeline)

RENDER_VERSION = "2.5.0"  # part of the chunk cache key: bump when stage-1 output changes
FADE = 0.025
JL_FADE = 0.02
AUTO_CHUNK_MIN = 180.0  # auto-chunk edits at least this long (seconds)
XFADE = {"fade": "fade", "crossfade": "fade", "dissolve": "dissolve", "dip-black": "fadeblack",
         "fadeblack": "fadeblack", "dip-white": "fadewhite", "fadewhite": "fadewhite",
         "wipeleft": "wipeleft", "wiperight": "wiperight", "wipeup": "wipeup", "wipedown": "wipedown",
         "slideleft": "slideleft", "slideright": "slideright", "slideup": "slideup", "slidedown": "slidedown",
         "whip": "slideleft", "whip-left": "slideleft", "whip-right": "slideright",
         "smoothleft": "smoothleft", "smoothright": "smoothright", "circleopen": "circleopen",
         "circleclose": "circleclose", "radial": "radial", "pixelize": "pixelize", "zoomin": "zoomin",
         "hblur": "hblur", "distance": "distance"}
TEXT_POS = {"top": (8, 0.10), "center": (5, 0.0), "bottom": (2, 0.12), "lower-third": (1, 0.16),
            "top-left": (7, 0.06), "top-right": (9, 0.06), "bottom-left": (1, 0.08), "bottom-right": (3, 0.08)}
HDR_TONEMAP = ("zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,"
               "zscale=t=bt709:m=bt709:r=tv,format=yuv420p")
KEY_COLORS = {"green": "0x00FF00", "blue": "0x0000FF"}
STAB = {True: (5, 15), "light": (4, 10), "strong": (8, 30)}  # (shakiness, smoothing)
DUCK = {"threshold": 0.03, "ratio": 8, "attack": 20, "release": 400}


def esc_path(p):
    return str(p).replace("\\", "/").replace(":", r"\:").replace("'", r"\'").replace(",", r"\,")


def atempo_chain(speed):
    parts, s = [], speed
    while s > 2.0:
        parts.append("atempo=2.0")
        s /= 2.0
    while s < 0.5:
        parts.append("atempo=0.5")
        s /= 0.5
    parts.append(f"atempo={s:.5f}")
    return ",".join(parts)


def ass_color(hex_rgb, alpha=0):
    h = hex_rgb.lstrip("#")
    return f"&H{alpha:02X}{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def ass_ts(t):
    t = max(t, 0)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def write_texts_ass(texts, path, W, H, font, safe=None):
    base = min(W, H)
    styles, events = [], []
    for i, t in enumerate(texts):
        align, mv = TEXT_POS.get(t.get("pos", "center"), TEXT_POS["center"])
        size = int(base * float(t.get("size", 0.075)))
        col = ass_color(t.get("color", "#FFFFFF"))
        box = t.get("box")
        border, outline, back = (3, max(size // 5, 6), ass_color(box, 0x30)) if box else (1, max(size // 14, 2), ass_color("#000000", 0x80))
        ml = mr = int(W * 0.08)
        if safe and not t.get("ignore_safe"):  # keep texts out of the platform UI
            if align in (1, 2, 3):
                mv = max(mv, safe["bottom"] + 0.02)
            elif align in (7, 8, 9):
                mv = max(mv, safe["top"] + 0.02)
            ml, mr = max(ml, int(W * (safe["left"] + 0.02))), max(mr, int(W * (safe["right"] + 0.02)))
        styles.append(f"Style: T{i},{t.get('font', font)},{size},{col},{col},{ass_color('#000000')},{back},"
                      f"{-1 if t.get('bold', True) else 0},0,0,0,100,100,0,0,{border},{outline},0,{align},{ml},{mr},{int(H * mv)},1")
        anim = t.get("anim", "fade")
        tag = {"pop": r"{\fad(60,120)\fscx70\fscy70\t(0,160,\fscx100\fscy100)}", "fade": r"{\fad(150,150)}",
               "none": ""}.get(anim, r"{\fad(150,150)}")
        text = str(t["text"]).replace("\\n", "\n").replace("\n", r"\N").replace("{", "(").replace("}", ")")
        events.append(f"Dialogue: 1,{ass_ts(float(t['start']))},{ass_ts(float(t['end']))},T{i},,0,0,0,,{tag}{text}")
    Path(path).write_text(
        f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, "
        "MarginL, MarginR, MarginV, Encoding\n" + "\n".join(styles) +
        "\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n" +
        "\n".join(events) + "\n", encoding="utf-8")


def proxy_for(src):
    """The proxy `vs proxy` made for a source (raw/.proxy/<name>.mkv), if any."""
    p = Path(src).parent / ".proxy" / (Path(src).name + ".mkv")
    return p if p.exists() and p.stat().st_mtime >= Path(src).stat().st_mtime else None


def file_sig(path):
    st = Path(path).stat()
    return [str(Path(path).resolve()), st.st_size, int(st.st_mtime)]


# --------------------------------------------------------------------------------------------
# Shots: timeline items grouped back into the segments the editor wrote.

def groups_of(tl):
    groups = []
    for it in tl:
        if it["first"]:
            seg = it["seg"]
            groups.append({"items": [it], "seg": seg, "src": it["src"], "start": it["start"],
                           "out_start": it["out_start"], "overlap": it["overlap"], "freeze": it["freeze"],
                           "index": it["index"]})
        else:
            groups[-1]["items"].append(it)
    for g in groups:
        g["end"] = g["items"][-1]["end"]
        g["out_end"] = g["items"][-1]["out_end"]
        g["len"] = g["out_end"] - g["out_start"]
        sp = g["seg"].get("speed", 1.0)
        g["ramp"] = ramp_points(g["seg"], g["end"] - g["start"]) if isinstance(sp, list) and not g["freeze"] else None
        g["speed"] = 1.0 if (g["freeze"] or g["ramp"]) else g["items"][0]["speed"]
    return groups


class Graph:
    """An ffmpeg input list plus filter graph under construction."""

    def __init__(self):
        self.inputs, self.filters, self.n = [], [], 0

    def add_input(self, *args):
        self.inputs += list(args)
        self.n += 1
        return self.n - 1

    def f(self, s):
        self.filters.append(s)


class Ctx:
    def __init__(self, args, edl, W, H, fps, pixfmt, keep_hdr, cache_dir, warnings):
        self.args, self.edl, self.W, self.H, self.fps = args, edl, W, H, fps
        self.pixfmt, self.keep_hdr, self.cache_dir, self.warnings = pixfmt, keep_hdr, cache_dir, warnings
        self.use_proxy = bool(args.proxy or args.preview)
        self.trf = {}
        self.t_in = {}       # shot index -> in-point time on its decoded branch (set where the branch is cut)
        self.only = None     # "video": picture only (a revision window); "audio": sound only (no frame decoded)

    def video_src(self, src):
        if self.use_proxy and not is_image(src):
            p = proxy_for(src)
            if p:
                return str(p)
        return src


def out_time_expr(g, var):
    """Expression for the segment's output time given its source-relative time variable."""
    if g["ramp"]:
        return ramp_setpts(g["ramp"], var)
    if g["speed"] != 1.0:
        return f"({var})/{g['speed']:.6g}"
    return f"({var})"


def shot_video(ctx, gr, vlab, k, g):
    W, H, fps, seg, edl = ctx.W, ctx.H, ctx.fps, g["seg"], ctx.edl
    pinfo = probe(ctx.video_src(g["src"]))
    chain = []
    if g["freeze"]:
        chain.append(f"trim=end_frame=1,setpts=PTS-STARTPTS,fps={fps},"
                     f"tpad=stop_mode=clone:stop_duration={g['freeze']:.3f},trim=duration={g['freeze']:.3f}")
    if seg.get("reverse") and not g["freeze"]:
        if g["end"] - g["start"] > 30:
            ctx.warnings.add(f"{Path(g['src']).name}: reversing {g['end'] - g['start']:.0f}s holds it all in memory")
        chain.append("reverse")
    stab = seg.get("stabilize")
    if stab and not g["freeze"] and not is_image(g["src"]):
        trf = ctx.trf.get(g["index"])
        if trf:
            _, smooth = STAB.get(stab, STAB[True])
            chain.append(f"vidstabtransform=input='{esc_path(trf)}':smoothing={smooth}:optzoom=1:interpol=bicubic,"
                         "unsharp=5:5:0.6:3:3:0.3")
        else:
            chain.append("deshake")
    if pinfo["hdr"] and not ctx.keep_hdr:
        if has_filter("zscale"):
            chain.append(HDR_TONEMAP)
        else:
            ctx.warnings.add(f"{Path(g['src']).name}: HDR source but ffmpeg lacks zscale; colours may look washed out")
    elif ctx.keep_hdr and not pinfo["hdr"] and not is_image(g["src"]):
        ctx.warnings.add(f"{Path(g['src']).name}: SDR shot in an HDR render will look dim/flat next to HDR shots")
    # Time 0 of the shot is its in-point. When the in-point falls between two source frames the first decoded frame
    # is a little after it; resetting to that frame (PTS-STARTPTS) shifted the whole shot by up to a frame.
    t_in = ctx.t_in.pop(k, None)
    t_in = t_in if not (g["freeze"] or seg.get("reverse") or stab) else None
    chain.append(f"setpts=PTS-{t_in:.6f}/TB" if t_in is not None else "setpts=PTS-STARTPTS")

    kf = dict(seg.get("kf") or {})
    fx, fy = seg.get("focus", [edl.get("reframe", 0.5), 0.5])
    z0 = float(seg.get("zoom", 1.0))
    z1 = seg.get("zoom_to")
    if z1 is None and is_image(g["src"]) and seg.get("ken_burns", True) and "zoom" not in kf:
        z1 = z0 * 1.08
    if z1 is not None and "zoom" not in kf:
        kf["zoom"] = [[0, z0, "linear"], [g["len"], float(z1), "linear"]]
    fit = seg.get("fit", edl.get("fit", "cover"))
    animated = "zoom" in kf
    if fit in ("contain", "blur") and not animated and z0 == 1.0:
        fg = f"scale={W}:{H}:force_original_aspect_ratio=decrease,setsar=1"
        if fit == "blur":
            bg = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                  f"boxblur=luma_radius=min(h\\,w)/20:luma_power=2,eq=brightness=-0.08")
            body = (f"split=2[b{k}][f{k}];[b{k}]{bg}[bb{k}];[f{k}]{fg}[ff{k}];"
                    f"[bb{k}][ff{k}]overlay=(W-w)/2:(H-h)/2")
        else:
            body = f"{fg},pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black"
    elif "zoom" in kf:
        # Animated framing: oversample 2x, then zoompan one output frame per input frame.
        tz = out_time_expr(g, f"on/{fps}")
        zx = kf_expr(kf["zoom"], tvar=tz) if "zoom" in kf else f"{z0}"
        xx = kf_expr(kf["x"], tvar=tz) if "x" in kf else f"{fx}"
        yy = kf_expr(kf["y"], tvar=tz) if "y" in kf else f"{fy}"
        body = (f"fps={fps},scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
                f"zoompan=z='max({zx},1)':x='(iw-iw/zoom)*({xx})':y='(ih-ih/zoom)*({yy})'"
                f":d=1:s={W}x{H}:fps={fps}")
    elif "x" not in kf and "y" not in kf and z0 >= 1.0:
        # Static framing: crop the source to the region that will be visible, THEN scale it to the frame.
        # Same picture as scale-to-cover-then-crop, but the scaler only works on output-sized frames: filling a
        # 1080x1920 Reel from 1920x1080 used to scale every frame to 3413x1920 first.
        zw, zh = int(W * z0) // 2 * 2, int(H * z0) // 2 * 2
        sc = f"max({zw}/iw\\,{zh}/ih)"
        body = (f"crop=w='min(iw\\,{W}/{sc})':h='min(ih\\,{H}/{sc})':x='(iw-ow)*({fx})':y='(ih-oh)*({fy})',"
                f"scale={W}:{H}")
    else:
        zw, zh = int(W * z0) // 2 * 2, int(H * z0) // 2 * 2
        tt = out_time_expr(g, "t")
        xx = kf_expr(kf["x"], tvar=tt) if "x" in kf else f"{fx}"
        yy = kf_expr(kf["y"], tvar=tt) if "y" in kf else f"{fy}"
        body = (f"scale={zw}:{zh}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H}:x='(iw-{W})*({xx})':y='(ih-{H})*({yy})'")
    chain.append(body)
    if "rotate" in kf:
        tt = out_time_expr(g, "t")
        chain.append(f"rotate=a='({kf_expr(kf['rotate'], tvar=tt)})*PI/180':c=black")
    grade = seg.get("grade", edl.get("grade"))
    if grade:
        gch = GRADES.get(grade)
        if gch is None:
            die(f"unknown grade '{grade}'. Options: {', '.join(GRADES)}")
        if gch:
            chain.append(gch)
    lut = seg.get("lut", edl.get("lut"))
    if lut:
        if not Path(lut).exists():
            die(f"LUT not found: {lut}")
        chain.append(f"lut3d='{esc_path(lut)}'")
    if g["ramp"]:
        chain.append(f"setpts='({ramp_setpts(g['ramp'], 'T')})/TB'")
    elif g["speed"] != 1.0:
        chain.append(f"setpts=PTS/{g['speed']}")
    # Place the shot on the video's absolute frame grid: output frame j (time j/fps) belongs to the shot whose
    # [out_start, out_end) holds it, and shows the source at in-point + (j/fps - out_start). Each shot used to be
    # cut to its own rounded length, so the rounding piled up differently depending on the shots before it: an
    # untouched shot moved by a frame whenever an earlier cut changed (and revision splices could not match).
    f0, f1 = frame_index(g["out_start"], fps), frame_index(g["out_end"], fps)
    phase = f0 / fps - g["out_start"]          # 0 <= phase < 1 frame: how far the shot's first frame is into it
    if phase > 1e-6:
        chain.append(f"setpts=PTS-{phase:.6f}/TB")
    # fps picks, for each output frame, the source frame on screen at that moment; frames before the shot's first
    # output frame (the margin kept before the in-point) are then dropped
    chain.append(f"fps={fps},trim=start=0,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop=1,setsar=1,"
                 f"format={ctx.pixfmt},trim=end_frame={max(f1 - f0, 1)},settb=AVTB")
    gr.f(f"[{vlab}]" + ",".join(chain) + f"[v{k}]")


def shot_audio(ctx, gr, ain, k, g):
    """Dialogue for one shot, exactly as long as its picture."""
    seg, L = g["seg"], g["len"]
    tail = [f"afade=t=in:d={FADE},afade=t=out:st={max(L - FADE, 0):.4f}:d={FADE}", f"apad,atrim=0:{L:.4f}"]
    head = f"[{ain}]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS"
    vol = float(seg.get("volume_db", 0))
    if g["ramp"]:
        parts = g["items"]
        labs = "".join(f"[r{k}_{i}]" for i in range(len(parts)))
        gr.f(f"{head},asplit={len(parts)}{labs}")
        for i, it in enumerate(parts):
            a0, a1 = it["start"] - g["start"], it["end"] - g["start"]
            pl = it["out_end"] - it["out_start"]
            gr.f(f"[r{k}_{i}]atrim={a0:.4f}:{a1:.4f},asetpts=PTS-STARTPTS,{atempo_chain(it['speed'])},"
                 f"apad,atrim=0:{pl:.4f}[rp{k}_{i}]")
        chain = ["".join(f"[rp{k}_{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1"]
    else:
        chain = [head]
        if seg.get("reverse"):
            chain.append("areverse")
        if g["speed"] != 1.0:
            chain.append(atempo_chain(g["speed"]))
    if vol:
        chain.append(f"volume={vol}dB")
    gr.f(",".join(chain + tail) + f"[a{k}]")


def silence(gr, label, length):
    gr.f(f"anullsrc=r=48000:cl=stereo,atrim=0:{length:.4f}[{label}]")


def jl_patches(ctx, groups, follow):
    """J/L cuts as audio patches over the joined dialogue: (src, src_in, dur, at, mute_from, mute_to)."""
    out = []
    for k in range(1, len(groups)):
        prev, cur = groups[k - 1], groups[k]
        lead, tail = float(cur["seg"].get("audio_lead", 0)), float(prev["seg"].get("audio_tail", 0))
        if not (lead or tail):
            continue
        cut = cur["out_start"]
        if cur["overlap"] > 0 or follow or ctx.edl.get("audio_track"):
            ctx.warnings.add(f"audio_lead/audio_tail at shot {k + 1} ignored (transition or shared audio track)")
            continue
        if lead:
            if cur["ramp"] or cur["seg"].get("reverse") or cur["freeze"] or is_image(cur["src"]) or cur["seg"].get("mute"):
                ctx.warnings.add(f"audio_lead on shot {k + 1} ignored (needs plain audio)")
            else:
                lead = min(lead, prev["len"] - 0.05, cur["start"] / cur["speed"])
                if lead > 0.02:
                    out.append((cur["src"], cur["start"] - lead * cur["speed"], lead, cut - lead, cur["speed"],
                                cur["seg"]))
        if tail:
            if prev["ramp"] or prev["seg"].get("reverse") or prev["freeze"] or is_image(prev["src"]) or prev["seg"].get("mute"):
                ctx.warnings.add(f"audio_tail on shot {k} ignored (needs plain audio)")
            else:
                d = probe(prev["src"])["duration"]
                tail = min(tail, cur["len"] - 0.05, (d - prev["end"]) / prev["speed"] if d else tail)
                if tail > 0.02:
                    out.append((prev["src"], prev["end"], tail, cut, prev["speed"], prev["seg"]))
    return out


SHARE_MAX_GAP = 2.0  # seconds of source between two shots that one decoder reads through instead of seeking


def shared_runs(ctx, gr, groups, follow, skip_audio=False):
    """Consecutive shots cut from one source, in order and close together (jump cuts): one decoder reads the run
    once and each shot is trimmed from it, instead of one seeking decoder per shot that decodes from the previous
    keyframe every time (2:35 talking-head Reel, 38 shots: filter graph 36.9 s -> 26.6 s). Adds one input per run
    and its split/trim branches to `gr`; returns {shot index: (video label, audio label)}."""
    def plain(g):
        seg = g["seg"]
        return (not is_image(g["src"]) and not g["freeze"] and not seg.get("reverse") and not seg.get("stabilize")
                and ctx.video_src(g["src"]) == g["src"] and not follow)
    if os.environ.get("VS_NO_SHARE"):  # debugging: one decoder per shot
        return {}
    runs, cur = [], []
    for k, g in enumerate(groups):
        if cur and plain(g) and g["src"] == groups[cur[-1]]["src"] \
                and -1e-3 <= g["start"] - groups[cur[-1]]["end"] <= SHARE_MAX_GAP:
            cur.append(k)
            continue
        if len(cur) > 1:
            runs.append(cur)
        cur = [k] if plain(g) else []
    if len(cur) > 1:
        runs.append(cur)
    out = {}
    for run_ in runs:
        g0, g1 = groups[run_[0]], groups[run_[-1]]
        r0, r1 = g0["start"], g1["end"]
        early = min(r0, 1.0)     # seek early (as single shots do) so the frame showing at r0 is decoded too
        r0 -= early
        ri = gr.add_input("-ss", f"{r0:.3f}", "-t", f"{r1 - r0 + 2.0 / ctx.fps:.3f}", "-i", g0["src"])
        n = len(run_)
        if ctx.only != "audio":
            gr.f(f"[{ri}:v]split={n}" + "".join(f"[rs{k}]" for k in run_))
        has_a = probe(g0["src"])["has_audio"]
        if has_a:
            gr.f(f"[{ri}:a]asplit={n}" + "".join(f"[ras{k}]" for k in run_))
        for k in run_:
            a, b = groups[k]["start"] - r0, groups[k]["end"] - r0
            m = min(a, 1.0 / ctx.fps)   # keep the frame on screen at the in-point (it starts just before it)
            if ctx.only != "audio":
                gr.f(f"[rs{k}]trim=start={a - m:.4f}:end={b + 1.0 / ctx.fps:.4f}[rv{k}]")
            ctx.t_in[k] = a          # the in-point's time on this branch's clock (input seeked to r0 = 0)
            used = has_a and not skip_audio and not groups[k]["seg"].get("mute")
            if has_a:  # every split branch must end somewhere: sound the shot won't use goes to a null sink
                gr.f(f"[ras{k}]atrim=start={a:.4f}:end={b:.4f}" + (f"[ra{k}]" if used else ",anullsink"))
            out[k] = (f"rv{k}", f"ra{k}" if used else None)
    return out


def build_shots(ctx, gr, groups, t0=0.0):
    """Stage 1 into graph `gr`. Returns (video label, audio label, length)."""
    edl = ctx.edl
    use_track = edl.get("audio_track")
    follow = bool(use_track and use_track.get("follow"))
    if follow:
        if not Path(use_track["src"]).exists():
            die(f"audio_track not found: {use_track['src']}")
        tinfo = probe(use_track["src"])
    vid, aud = ctx.only != "audio", ctx.only != "video"
    shared = shared_runs(ctx, gr, groups, follow, skip_audio=bool(use_track and not follow) or not aud)
    for k, g in enumerate(groups):
        src, a, b = g["src"], g["start"], g["end"]
        vsrc = ctx.video_src(src)
        if k in shared:
            vlab, alab = shared[k]
        elif is_image(src):
            vi = gr.add_input("-loop", "1", "-framerate", str(ctx.fps), "-t", f"{g['len']:.3f}", "-i", src)
            vlab, alab = f"{vi}:v", f"{vi}:a"
        elif g["freeze"]:
            vi = gr.add_input("-ss", f"{a:.3f}", "-t", "1", "-i", vsrc)
            vlab, alab = f"{vi}:v", f"{vi}:a"
        elif g["seg"].get("reverse") or g["seg"].get("stabilize"):
            vi = gr.add_input("-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", vsrc)
            vlab, alab = f"{vi}:v", f"{vi}:a"
        else:
            # Seek up to 1 s early, then trim to the in-point: shots land on the right source frame (frame-numbered
            # source: 97 % exact vs 82.5 % seeking straight to the in-point, which put 1 in 6 frames a frame early).
            # Costs nothing extra: a seek decodes from the previous keyframe anyway.
            pad = min(a, 1.0)
            vi = gr.add_input("-ss", f"{a - pad:.3f}", "-t", f"{b - a + pad + 2.0 / ctx.fps:.3f}", "-i", vsrc)
            m = min(pad, 1.0 / ctx.fps)  # keep the frame on screen at the in-point (it starts just before it)
            if vid:
                gr.f(f"[{vi}:v]trim=start={pad - m:.4f}:end={pad + b - a + 1.0 / ctx.fps:.4f}[pv{k}]")
            ctx.t_in[k] = pad
            vlab, alab = f"pv{k}", None
            if aud and probe(src)["has_audio"] and vsrc == src and not (use_track and not follow) \
                    and not g["seg"].get("mute"):
                gr.f(f"[{vi}:a]atrim=start={pad:.4f}:end={pad + b - a:.4f}[pa{k}]")
                alab = f"pa{k}"
        if vid:
            shot_video(ctx, gr, vlab, k, g)
        else:
            ctx.t_in.pop(k, None)
        if (use_track and not follow) or not aud:
            continue
        if follow and not g["freeze"]:
            ref0 = float(g["seg"].get("ref", [a])[0]) + float(use_track.get("offset", 0))
            ai = gr.add_input("-ss", f"{max(ref0, 0):.3f}", "-t", f"{b - a:.3f}", "-i", use_track["src"])
            has_a, ain = tinfo["has_audio"], f"{ai}:a"
        else:
            has_a = probe(src)["has_audio"] and not g["freeze"] and not is_image(src)
            ain = alab
            if has_a and vsrc != src:  # proxies keep audio, but the original is the reference
                ain = f"{gr.add_input('-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', src)}:a"
        if has_a and not g["seg"].get("mute"):
            shot_audio(ctx, gr, ain, k, g)
        else:
            silence(gr, f"a{k}", g["len"])

    skip_audio = bool(use_track and not follow) or not aud
    has_tr = any(g["overlap"] > 0 for g in groups[1:])
    G = len(groups)
    if not vid:   # sound only: join the shots' audio the way the picture would be joined
        al = "a0"
        for k in range(1, G):
            d = groups[k]["overlap"]
            gr.f(f"[{al}][a{k}]" + (f"acrossfade=d={d:.4f}:c1=tri:c2=tri" if d > 0 else "concat=n=2:v=0:a=1")
                 + f"[xa{k}]")
            al = f"xa{k}"
        gr.f(f"[{al}]anull[ca]")
        return None, "ca", groups[-1]["out_end"] - t0
    if not has_tr:
        if skip_audio:
            gr.f("".join(f"[v{k}]" for k in range(G)) + f"concat=n={G}:v=1:a=0[cvj]")
            gr.f(f"[cvj]setpts=N/({ctx.fps}*TB)[cv]")
        else:
            gr.f("".join(f"[v{k}][a{k}]" for k in range(G)) + f"concat=n={G}:v=1:a=1[cvj][ca]")
            gr.f(f"[cvj]setpts=N/({ctx.fps}*TB)[cv]")
    else:
        vl, al = "v0", "a0"
        for k in range(1, G):
            g = groups[k]
            if g["overlap"] > 0:
                tr = g["seg"]["transition_in"]
                ttype = tr.get("type", "fade") if isinstance(tr, dict) else "fade"
                xf = XFADE.get(ttype, ttype)
                d = g["overlap"]
                gr.f(f"[{vl}][v{k}]xfade=transition={xf}:duration={d:.4f}:offset={g['out_start'] - t0:.4f}[xv{k}]")
                if not skip_audio:
                    gr.f(f"[{al}][a{k}]acrossfade=d={d:.4f}:c1=tri:c2=tri[xa{k}]")
            else:
                gr.f(f"[{vl}][v{k}]concat=n=2:v=1:a=0[xv{k}]")
                if not skip_audio:
                    gr.f(f"[{al}][a{k}]concat=n=2:v=0:a=1[xa{k}]")
            vl, al = f"xv{k}", f"xa{k}"
        gr.f(f"[{vl}]setpts=N/({ctx.fps}*TB)[cv]")
        if not skip_audio:
            gr.f(f"[{al}]anull[ca]")
    total = groups[-1]["out_end"] - t0
    if skip_audio:
        silence(gr, "ca", total)
        return "cv", "ca", total

    patches = jl_patches(ctx, groups, follow)
    if patches:
        mutes, labs = [], []
        for j, (src, s_in, dur, at, sp, seg) in enumerate(patches):
            pi = gr.add_input("-ss", f"{s_in:.3f}", "-t", f"{dur * sp:.3f}", "-i", src)
            chain = [f"[{pi}:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS"]
            if sp != 1.0:
                chain.append(atempo_chain(sp))
            if float(seg.get("volume_db", 0)):
                chain.append(f"volume={float(seg['volume_db'])}dB")
            chain.append(f"apad,atrim=0:{dur:.4f},afade=t=in:d={JL_FADE},afade=t=out:st={dur - JL_FADE:.4f}:d={JL_FADE},"
                         f"adelay={int(round((at - t0) * 1000))}:all=1")
            gr.f(",".join(chain) + f"[jl{j}]")
            labs.append(f"[jl{j}]")
            mutes.append((at - t0, at - t0 + dur))
        pts = [[0, 1, "linear"]]
        for m0, m1 in sorted(mutes):
            pts += [[max(m0 - JL_FADE, 0), 1, "linear"], [m0, 0, "linear"], [m1, 0, "linear"], [m1 + JL_FADE, 1, "linear"]]
        gr.f(f"[ca]volume='{kf_expr(pts)}':eval=frame[cam]")
        gr.f(f"[cam]{''.join(labs)}amix=inputs={1 + len(labs)}:duration=first:normalize=0[cjl]")
        return "cv", "cjl", total
    return "cv", "ca", total


# --------------------------------------------------------------------------------------------
# Finish: everything that lives on the output timeline.

def finish(ctx, gr, vlab, alab, total, out):
    edl = ctx.edl
    use_track = edl.get("audio_track")
    follow = bool(use_track and use_track.get("follow"))
    if use_track and not follow:
        if not Path(use_track["src"]).exists():
            die(f"audio_track not found: {use_track['src']}")
        ti = gr.add_input("-i", use_track["src"])
        s0 = float(use_track.get("start", 0))
        g = float(use_track.get("gain_db", 0))
        gr.f(f"[{ti}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={s0:.3f}:{s0 + total:.3f},"
             f"asetpts=PTS-STARTPTS,volume={g}dB,apad,atrim=0:{total:.3f}[trk]")
        gr.f(f"[{alab}]anullsink")
        alab = "trk"
    ofmt = ":format=yuv420p10" if "10" in ctx.pixfmt else ""
    if ctx.only != "audio":
        finish_video(ctx, gr, vlab, ofmt, out)
    if ctx.only == "video":
        gr.f(f"[{alab}]anullsink")
        return
    finish_audio(ctx, gr, alab, total)


def finish_video(ctx, gr, vlab, ofmt, out):
    edl, W, H = ctx.edl, ctx.W, ctx.H
    for j, bl in enumerate(edl.get("blurs", [])):
        s, e = float(bl["start"]), float(bl["end"])
        cw = max(int(W * float(bl.get("w", 0.2))) // 2 * 2, 4)
        ch = max(int(H * float(bl.get("h", 0.2))) // 2 * 2, 4)
        kfb = bl.get("kf") or {}
        xx = kf_expr(kfb["x"]) if "x" in kfb else f"{float(bl.get('x', 0.4))}"
        yy = kf_expr(kfb["y"]) if "y" in kfb else f"{float(bl.get('y', 0.4))}"
        xe, ye = f"({xx})*{W}", f"({yy})*{H}"
        strength = int(bl.get("strength", 20))
        if bl.get("mode", "blur") == "pixelate":
            b = max(strength // 2, 4)
            fx = f"scale={max(cw // b, 1)}:{max(ch // b, 1)},scale={cw}:{ch}:flags=neighbor"
        else:
            r = max(min(strength, min(cw, ch) // 2 - 1), 1)
            fx = f"boxblur=luma_radius={r}:luma_power=2:chroma_radius={max(r // 2, 1)}"
        gr.f(f"[{vlab}]split=2[bm{j}][bs{j}]")
        gr.f(f"[bs{j}]crop={cw}:{ch}:x='min(max({xe},0),{W - cw})':y='min(max({ye},0),{H - ch})',{fx}[bb{j}]")
        gr.f(f"[bm{j}][bb{j}]overlay=x='min(max({xe},0),{W - cw})':y='min(max({ye},0),{H - ch})'"
             f":enable='between(t,{s},{e})'{ofmt}[bl{j}]")
        vlab = f"bl{j}"

    for j, ov in enumerate(edl.get("overlays", [])):
        if not Path(ov["file"]).exists():
            die(f"overlay not found: {ov['file']}")
        dec = ["-c:v", "libvpx-vp9"] if ov["file"].lower().endswith(".webm") else []
        loop = ["-loop", "1"] if is_image(ov["file"]) else []
        seek = ["-ss", f"{float(ov['in']):.3f}"] if ov.get("in") and not loop else []
        oi = gr.add_input(*loop, *seek, *dec, "-i", ov["file"])
        s, e = float(ov["start"]), float(ov["end"])
        chain = []
        key = ov.get("key")
        if key:
            kc = key if isinstance(key, dict) else {"color": key}
            col = KEY_COLORS.get(kc.get("color", "green"), str(kc.get("color", "green")).replace("#", "0x"))
            chain.append(f"chromakey=color={col}:similarity={float(kc.get('similarity', 0.12))}"
                         f":blend={float(kc.get('blend', 0.08))}")
            if kc.get("despill", True) and col in ("0x00FF00", "0x0000FF"):
                chain.append(f"format=yuva444p,despill=type={'blue' if col == '0x0000FF' else 'green'}")
        if ov.get("fit", "w" not in ov):
            fx, fy = ov.get("focus", [0.5, 0.5])
            chain.append(f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-{W})*{fx}:(ih-{H})*{fy}")
        elif "w" in ov:
            chain.append(f"scale={int(ov['w'])}:-2")
        chain.append("format=rgba")
        if "opacity" in ov:
            chain.append(f"colorchannelmixer=aa={float(ov['opacity'])}")
        if loop:
            chain.append(f"trim=0:{e - s:.3f}")
        chain.append("setpts=PTS-STARTPTS")
        if ov.get("fade_in"):
            chain.append(f"fade=t=in:st=0:d={float(ov['fade_in'])}:alpha=1")
        if ov.get("fade_out"):
            fo = float(ov["fade_out"])
            chain.append(f"fade=t=out:st={max(e - s - fo, 0):.3f}:d={fo}:alpha=1")
        chain.append(f"setpts=PTS+{s}/TB")
        gr.f(f"[{oi}:v]" + ",".join(chain) + f"[o{j}]")
        kfo = ov.get("kf") or {}
        lt = f"(t-{s})"
        x = f"'{kf_expr(kfo['x'], tvar=lt)}'" if "x" in kfo else ov.get("x", 0)
        y = f"'{kf_expr(kfo['y'], tvar=lt)}'" if "y" in kfo else ov.get("y", 0)
        gr.f(f"[{vlab}][o{j}]overlay=x={x}:y={y}:enable='between(t,{s},{e})':eof_action=pass{ofmt}[ov{j}]")
        vlab = f"ov{j}"

    # Custom fonts: project assets/fonts, then the workspace library, then style/fonts.
    fontsdir = ""
    edl_dir = Path(ctx.args.edl).resolve().parent
    ws = edl_dir.parents[2] if len(edl_dir.parents) > 2 else None
    for cand in (edl_dir.parent / "assets" / "fonts", ws and ws / "library" / "assets" / "fonts",
                 ws and ws / "style" / "fonts"):
        if cand and cand.is_dir() and any(cand.iterdir()):
            fontsdir = f":fontsdir='{esc_path(cand)}'"
            break
    if edl.get("texts"):
        tpath = out.with_suffix(".texts.ass")
        out.parent.mkdir(parents=True, exist_ok=True)
        aspect = ctx.args.aspect or PRESETS.get(ctx.args.preset, {}).get("aspect")
        write_texts_ass(edl["texts"], tpath, W, H, ctx.args.font,
                        safe_zone(ctx.args.preset, aspect if aspect else ("9:16" if H > W else None)))
        gr.f(f"[{vlab}]subtitles='{esc_path(tpath)}'{fontsdir}[tv]")
        vlab = "tv"
    if ctx.args.captions:
        if not Path(ctx.args.captions).exists():
            die(f"captions not found: {ctx.args.captions}")
        gr.f(f"[{vlab}]subtitles='{esc_path(ctx.args.captions)}'{fontsdir}[sv]")
        vlab = "sv"
    gr.f(f"[{vlab}]null[vout]")


def finish_audio(ctx, gr, alab, total):
    edl = ctx.edl
    use_track = edl.get("audio_track")
    # Audio: foreground (dialogue + sfx), then beds (music + tracks), ducked under the foreground.
    aud = edl.get("audio", {})
    if aud.get("enhance"):
        gr.f(f"[{alab}]{VOICE_ENHANCE}[ae]")
        alab = "ae"
    if aud.get("gain"):
        gr.f(f"[{alab}]volume='pow(10,({kf_expr(aud['gain'], default_ease='linear')})/20)':eval=frame[ag]")
        alab = "ag"
    sfx = edl.get("sfx", [])
    if sfx:
        labs = []
        for j, fx in enumerate(sfx):
            if not Path(fx["file"]).exists():
                die(f"sfx not found: {fx['file']}")
            si = gr.add_input("-i", fx["file"])
            gr.f(f"[{si}:a]{sfx_chain(fx)}[fx{j}]")
            labs.append(f"[fx{j}]")
        gr.f(f"[{alab}]{''.join(labs)}amix=inputs={1 + len(labs)}:duration=first:normalize=0[asx]")
        alab = "asx"

    tracks = list(edl.get("tracks", []))
    music = edl.get("music")
    if music:
        tracks.insert(0, {"name": "music", "duck": music.get("duck", True), "gain_db": float(music.get("gain_db", -18)),
                          "clips": [{"file": music["file"], "in": float(music.get("start", 0)), "loop": True,
                                     "fade_in": 0.3, "fade_out": float(music.get("fade_out", 1.5))}]})
    ducked, plain = [], []
    for j, tr in enumerate(tracks):
        lab = track_bus(gr, tr, j, total)
        if not lab:
            continue
        (ducked if tr.get("duck") and not use_track else plain).append((lab, tr))
    if ducked:
        if len(ducked) > 1:
            gr.f("".join(f"[{lab}]" for lab, _ in ducked) + f"amix=inputs={len(ducked)}:duration=first:normalize=0[dkin]")
            dk = "dkin"
        else:
            dk = ducked[0][0]
        dc = dict(DUCK)
        for _, tr in ducked:
            if isinstance(tr.get("duck"), dict):
                dc.update(tr["duck"])
        gr.f(f"[{alab}]asplit=2[fgo][sc]")
        gr.f(f"[{dk}][sc]sidechaincompress=threshold={dc['threshold']}:ratio={dc['ratio']}"
             f":attack={dc['attack']}:release={dc['release']}[dkd]")
        alab = "fgo"
        plain.insert(0, ("dkd", None))
    if plain:
        gr.f(f"[{alab}]" + "".join(f"[{lab}]" for lab, _ in plain) +
             f"amix=inputs={1 + len(plain)}:duration=first:normalize=0[am]")
        alab = "am"
    lufs = ctx.lufs
    if lufs is not None:
        gr.f(f"[{alab}]loudnorm=I={lufs}:TP=-1.5:LRA=11,aresample=48000[an]")
        alab = "an"
    gr.f(f"[{alab}]anull[aout]")


def track_bus(gr, tr, j, total):
    labs = []
    for c, clip in enumerate(tr.get("clips", [])):
        f = clip["file"]
        if not Path(f).exists():
            die(f"track '{tr.get('name', j)}' clip not found: {f}")
        at = float(clip.get("at", 0))
        if at >= total:
            continue
        dur = float(clip["dur"]) if clip.get("dur") else None
        loop = clip.get("loop", False)
        if dur is None:
            dur = total - at if loop else min(probe(f)["duration"] - float(clip.get("in", 0)), total - at)
        dur = min(dur, total - at)
        ci = gr.add_input(*(["-stream_loop", "-1"] if loop else []), "-ss", f"{float(clip.get('in', 0)):.3f}", "-i", f)
        chain = [f"[{ci}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS"]
        if float(clip.get("gain_db", 0)):
            chain.append(f"volume={float(clip['gain_db'])}dB")
        if clip.get("fade_in"):
            chain.append(f"afade=t=in:d={float(clip['fade_in'])}")
        if clip.get("fade_out"):
            fo = float(clip["fade_out"])
            chain.append(f"afade=t=out:st={max(dur - fo, 0):.3f}:d={fo}")
        chain.append(f"adelay={int(at * 1000)}:all=1")
        gr.f(",".join(chain) + f"[t{j}c{c}]")
        labs.append(f"[t{j}c{c}]")
    if not labs:
        return None
    mix = f"amix=inputs={len(labs)}:duration=longest:normalize=0," if len(labs) > 1 else ""
    if tr.get("gain"):
        gain = f"volume='pow(10,({kf_expr(tr['gain'], default_ease='linear')})/20)':eval=frame"
    else:
        gain = f"volume={float(tr.get('gain_db', 0))}dB"
    gr.f("".join(labs) + f"{mix}apad,atrim=0:{total:.3f},{gain}[tk{j}]")
    return f"tk{j}"


# --------------------------------------------------------------------------------------------
# Encoding, stabilisation pre-pass, chunks.

def encoder_args(args, pixfmt, hdr_transfer):
    if args.codec == "prores":
        return ["-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le"], ["-c:a", "pcm_s16le"]
    # x264 veryfast vs medium at CRF 18 on real 1080p footage: 2.0x faster, same SSIM (0.9476 vs 0.9480), 5 % smaller
    # file; on a 2:35 1080x1920 Reel the final render went from 88.6 s to the time below. `--speed best` for masters.
    speeds = {"h264": {"fast": "veryfast", "balanced": "medium", "best": "slow"},
              "h265": {"fast": "fast", "balanced": "medium", "best": "slow"}}
    preset_speed = "ultrafast" if args.preview else speeds.get(args.codec, speeds["h264"])[args.speed]
    crf = max(args.crf, 26) if args.preview else args.crf
    lib = "libx264" if args.codec == "h264" else "libx265"
    tag = ["-tag:v", "hvc1"] if args.codec == "h265" else []
    venc = ["-c:v", lib, "-preset", preset_speed, "-crf", str(crf), "-pix_fmt", pixfmt, *tag]
    if hdr_transfer:
        venc += ["-x265-params", f"colorprim=bt2020:transfer={hdr_transfer}:colormatrix=bt2020nc"
                 + (":hdr10=1:repeat-headers=1" if hdr_transfer == "smpte2084" else ""),
                 "-color_primaries", "bt2020", "-color_trc", hdr_transfer, "-colorspace", "bt2020nc"]
    return venc, ["-c:a", "aac", "-b:a", "192k"]


def frame_index(t, fps):
    """First output frame at or after time t (frame k shows time k/fps): where a cut at t really starts."""
    return int(math.ceil(t * fps - 1e-6))


def frame_at(t, fps):
    return frame_index(t, fps) / fps


def manifest_path(out):
    return Path(str(out) + ".render.json")


def splice_plan(since, new_manifest, out):
    """Can this render reuse `since`? Returns the plan (window / copy) or None for a full render, saying why."""
    old_file, old_m = Path(since), manifest_path(since)
    if not old_file.exists() or not old_m.exists():
        print(f"--since: {old_m.name} not found (renders before this version have none); rendering everything",
              file=sys.stderr)
        return None
    if old_file.resolve() == Path(out).resolve():
        die("--since must be a different file from -o (the old render is read while the new one is written)")
    plan = splice.plan(load_json(old_m), new_manifest)
    if plan.get("full"):
        print(f"--since: full render ({plan['full']})", file=sys.stderr)
        return None
    if not plan.get("copy"):
        keys = splice.keyframe_times(old_file)
        fps = new_manifest["settings"]["fps"]
        for t in (plan["a"], plan["b_old"]):
            # a cut between two frames starts on the next frame: that is where the encoder put the keyframe
            if 0 < t < load_json(old_m)["total"] - 1e-3 and not any(abs(k - frame_at(t, fps)) < 0.5 / fps for k in keys):
                print(f"--since: {old_file.name} has no keyframe at {t:.2f} s; rendering everything", file=sys.stderr)
                return None
    plan["old"] = str(old_file)
    return plan


def splice_render(ctx, groups, sp, venc, aenc, fps, total, out, new_manifest):
    """A revision: encode only the changed window's picture (built from the shots in it, nothing else decoded), mix
    the full sound in a sound-only pass (no frame decoded), copy the rest of the picture from the old file at its
    keyframes, then mux and check."""
    t_start = time.time()
    work = ctx.cache_dir / f"splice-{hashlib.sha1(str(out.resolve()).encode()).hexdigest()[:10]}"
    work.mkdir(parents=True, exist_ok=True)
    audio, win, old_v, joined = work / "audio.m4a", work / "window.mp4", work / "old_video.mp4", work / "video.mp4"
    old = Path(sp["old"])
    jobs = []
    # sound: every shot's audio, music, sfx, ducking and loudness, with no picture in the graph
    ctx.only = "audio"
    ga = Graph()
    _, al, _ = build_shots(ctx, ga, groups)
    finish(ctx, ga, None, al, total, out)
    jobs.append(["ffmpeg", "-y", "-hide_banner", "-v", "error", *ga.inputs, "-filter_complex", ";".join(ga.filters),
                 "-map", "[aout]", "-t", f"{total:.4f}", "-vn", *aenc, str(audio)])
    if not sp.get("copy"):
        a, b_new = sp["a"], sp["b_new"]
        fa = frame_at(a, fps)
        wgroups = [g for g in groups if g["out_start"] >= a - 1e-6 and g["out_end"] <= b_new + 1e-6]
        ctx.only = "video"
        gv = Graph()
        vl, al, _ = build_shots(ctx, gv, wgroups, t0=a)
        gv.f(f"[{vl}]setpts=PTS+{fa:.6f}/TB[cvabs]")    # back on the edit's clock: texts, captions, overlays line up
        finish(ctx, gv, "cvabs", al, total, out)
        gv.f("[vout]setpts=PTS-STARTPTS[vwin]")
        inner = [0.0] + [frame_at(c, fps) - fa for c in new_manifest["cuts"] if a + 1e-3 < c < b_new - 1e-3]
        wenc = list(venc)
        if "-force_key_frames" in wenc:
            wenc[wenc.index("-force_key_frames") + 1] = ",".join(f"{t:.4f}" for t in inner)
        n_win = frame_index(b_new, fps) - frame_index(a, fps)
        jobs.append(["ffmpeg", "-y", "-hide_banner", "-v", "error", *gv.inputs, "-filter_complex",
                     ";".join(gv.filters), "-map", "[vwin]", "-frames:v", str(n_win), *wenc, "-r", str(fps), "-an",
                     str(win)])
    ctx.only = None
    with ThreadPoolExecutor(max_workers=len(jobs)) as ex:      # the sound and the window encode side by side
        results = list(ex.map(lambda c: subprocess.run(c, capture_output=True, text=True), jobs))
    for r in results:
        if r.returncode != 0:
            print(f"revision render failed ({r.returncode}); rendering everything instead\n{(r.stderr or '')[-1500:]}",
                  file=sys.stderr)
            return False
    run(["ffmpeg", "-y", "-v", "error", "-i", str(old), "-map", "0:v:0", "-c", "copy", str(old_v)])
    if sp.get("copy"):
        video = old_v
        what = "picture unchanged: copied all of it, remixed the sound"
    else:
        old_total = load_json(manifest_path(old))["total"]
        listing = work / "concat.txt"
        # Split the old picture by frame number at the keyframes around the window (finals have an IDR at every cut,
        # closed GOPs): the segment muxer cuts exactly there, so no time-based seek can land a frame early or late.
        fa, fb = frame_index(sp["a"], fps), frame_index(sp["b_old"], fps)
        old_frames = round(old_total * fps)
        marks = ([fa] if fa > 0 else []) + ([fb] if fb < old_frames else [])
        parts = []
        for f in work.glob("old[0-9][0-9][0-9].mp4"):
            f.unlink()
        if marks:
            run(["ffmpeg", "-y", "-v", "error", "-i", str(old_v), "-map", "0:v:0", "-c", "copy", "-f", "segment",
                 "-segment_frames", ",".join(map(str, marks)), "-reset_timestamps", "1", str(work / "old%03d.mp4")])
            pieces = sorted(work.glob("old[0-9][0-9][0-9].mp4"))
            if fa > 0:
                parts.append(pieces[0])
            parts.append(win)
            if fb < old_frames:
                parts.append(pieces[-1])
        else:
            parts.append(win)
        listing.write_text("".join(f"file '{x.resolve()}'\n" for x in parts))
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(joined)])
        video = joined
        what = (f"re-encoded {fmt_ts(sp['a'])}-{fmt_ts(sp['b_new'])} ({sp['b_new'] - sp['a']:.1f} s of {total:.1f} s; "
                f"{'; '.join(sp['why'][:3])}), copied the rest from {old.name}, remixed the sound")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-i", str(audio), "-map", "0:v:0", "-map", "1:a:0", "-c", "copy",
         "-t", f"{total:.4f}", "-movflags", "+faststart", str(out)])
    o = probe(str(out))
    frames = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries",
                                 "stream=nb_read_packets", "-of", "csv=p=0", str(out)],
                                capture_output=True, text=True).stdout.strip() or 0)
    want = round(total * fps)
    seams = [] if sp.get("copy") else [t for t in (sp["a"], sp["b_new"]) if 0 < t < total]
    errs = ""
    for t in seams:  # decode a second either side of each seam: a broken splice shows up as decode errors
        d = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(0, t - 1):.3f}", "-i", str(out), "-t", "2", "-f", "null",
                            "-"], capture_output=True, text=True)
        errs += d.stderr
    if abs(frames - want) > 1 or abs(o["duration"] - total) > 2 / fps or errs.strip():
        print(f"revision splice check failed (frames {frames} vs {want}, duration {o['duration']:.3f} vs {total:.3f}"
              f"{', decode errors at a seam' if errs.strip() else ''}); rendering everything instead", file=sys.stderr)
        out.unlink(missing_ok=True)
        return False
    save_json(manifest_path(out), new_manifest)
    shutil.rmtree(work, ignore_errors=True)
    print(f"rendered {out}: {o['width']}x{o['height']} @ {o['fps']}fps, {fmt_ts(o['duration'])} "
          f"(revision: {what}; {time.time() - t_start:.1f} s)")
    return True


def stab_prepass(ctx, groups):
    if not any(g["seg"].get("stabilize") for g in groups):
        return
    if not (has_filter("vidstabdetect") and has_filter("vidstabtransform")):
        ctx.warnings.add("ffmpeg has no vid.stab; using deshake (weaker). Install an ffmpeg built with libvidstab")
        return
    ctx.cache_dir.mkdir(parents=True, exist_ok=True)
    for g in groups:
        stab = g["seg"].get("stabilize")
        if not stab or g["freeze"] or is_image(g["src"]):
            continue
        vsrc = ctx.video_src(g["src"])
        shak, _ = STAB.get(stab, STAB[True])
        key = hashlib.sha256(json.dumps([file_sig(vsrc), g["start"], g["end"], shak, bool(g["seg"].get("reverse"))])
                             .encode()).hexdigest()[:20]
        trf = ctx.cache_dir / f"stab-{key}.trf"
        if not trf.exists():
            print(f"stabilise: analysing {Path(g['src']).name} {g['start']:.2f}-{g['end']:.2f}s", file=sys.stderr)
            pre = "reverse," if g["seg"].get("reverse") else ""
            tmp = trf.with_suffix(".part")
            run(["ffmpeg", "-y", "-hide_banner", "-v", "error", "-ss", f"{g['start']:.3f}", "-t",
                 f"{g['end'] - g['start']:.3f}", "-i", vsrc, "-vf",
                 f"{pre}vidstabdetect=shakiness={shak}:accuracy=15:result='{esc_path(tmp)}'", "-f", "null", "-"])
            tmp.rename(trf)
        ctx.trf[g["index"]] = trf


def chunk_groups(groups, target):
    """Split shots into chunks of about `target` seconds, only at plain hard cuts."""
    chunks, cur = [], []
    for k, g in enumerate(groups):
        if cur:
            prev = groups[k - 1]
            clean = (g["overlap"] == 0 and not g["seg"].get("audio_lead") and not prev["seg"].get("audio_tail"))
            if clean and g["out_start"] - cur[0]["out_start"] >= target:
                chunks.append(cur)
                cur = []
        cur.append(g)
    if cur:
        chunks.append(cur)
    return chunks


def chunk_key(ctx, chunk):
    data = {"v": RENDER_VERSION, "W": ctx.W, "H": ctx.H, "fps": ctx.fps, "pix": ctx.pixfmt, "hdr": ctx.keep_hdr,
            "proxy": ctx.use_proxy, "preview": bool(ctx.args.preview),
            "edl": {k: ctx.edl.get(k) for k in ("grade", "lut", "reframe", "fit", "audio_track")},
            "shots": [[g["src"], g["start"], g["end"], g["out_start"] - chunk[0]["out_start"], g["seg"],
                       file_sig(ctx.video_src(g["src"])), file_sig(g["src"])] for g in chunk]}
    luts = {g["seg"].get("lut") for g in chunk} | {ctx.edl.get("lut")}
    data["luts"] = [file_sig(lp) for lp in sorted(x for x in luts if x) if Path(lp).exists()]
    return hashlib.sha256(json.dumps(data, sort_keys=True, default=str).encode()).hexdigest()[:24]


def render_chunk(ctx, chunk, path, threads):
    gr = Graph()
    vl, al, total = build_shots(ctx, gr, chunk, t0=chunk[0]["out_start"])
    gr.f(f"[{vl}]null[vout]")
    gr.f(f"[{al}]anull[aout]")
    vcodec = ["-c:v", "libx264", "-preset", "ultrafast" if ctx.args.preview else "veryfast", "-crf", "10",
              "-pix_fmt", ctx.pixfmt]
    tmp = path.with_suffix(".part.mkv")
    run(["ffmpeg", "-y", "-hide_banner", "-v", "error", *gr.inputs, "-filter_complex", ";".join(gr.filters),
         "-map", "[vout]", "-map", "[aout]", "-t", f"{total:.4f}", *vcodec, "-r", str(ctx.fps),
         "-c:a", "pcm_s16le", "-threads", str(threads), str(tmp)])
    tmp.rename(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edl")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--preset", choices=list(PRESETS), help="platform preset: sets aspect, fps, loudness")
    ap.add_argument("--aspect", choices=list(ASPECTS), help="output aspect (default: preset, else first source)")
    ap.add_argument("--fps", type=float)
    ap.add_argument("--captions", help="ASS or SRT file to burn in (from `vs captions`)")
    ap.add_argument("--loudnorm", type=float, nargs="?", const=-14.0, help="LUFS target (preset sets it)")
    ap.add_argument("--no-loudnorm", action="store_true")
    ap.add_argument("--font", default="Inter", help="font for EDL texts")
    ap.add_argument("--codec", choices=["h264", "h265", "prores"], default="h264")
    ap.add_argument("--crf", type=int, default=18)
    ap.add_argument("--speed", choices=["fast", "balanced", "best"], default="fast",
                    help="encoder effort: fast (x264 veryfast, default), balanced (medium), best (slow, for masters)")
    ap.add_argument("--10bit", dest="ten_bit", action="store_true", help="10-bit output (h265/prores): no banding")
    ap.add_argument("--hdr", action="store_true", help="keep HDR (HDR10/HLG) instead of tone-mapping to SDR (h265)")
    ap.add_argument("--range", help="render only this output window, e.g. 20-35")
    ap.add_argument("--since", help="a previous render of this edit (with its .render.json): re-encode only the "
                                    "changed window and copy the rest; falls back to a full render when needed")
    ap.add_argument("--preview", action="store_true", help="half resolution, ultrafast, proxies: for review drafts")
    ap.add_argument("--proxy", action="store_true", help="use proxies from `vs proxy` (on by default with --preview)")
    ap.add_argument("--chunks", default="auto", help="auto | off | seconds per chunk (stage 1 in parallel, cached)")
    ap.add_argument("--jobs", type=int, default=0, help="parallel chunk renders (default: cores/2, max 4)")
    ap.add_argument("--no-cache", action="store_true", help="re-render every chunk")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    need("ffmpeg")
    edl = load_json(args.edl)
    tl = timeline(edl)
    if not tl:
        die("EDL has no segments")
    probes = {}
    for it in tl:
        if not Path(it["src"]).exists():
            die(f"source not found: {it['src']} (paths are relative to the current directory)")
        probes.setdefault(it["src"], probe(it["src"]))
        if it["end"] <= it["start"]:
            die(f"segment {it['src']} {it['start']}..{it['end']}: end must be after start")
        d = probes[it["src"]]["duration"]
        if d and it["end"] > d + 0.05 and not it["freeze"]:
            die(f"segment {Path(it['src']).name} ends at {it['end']:.2f}s but the source is {d:.2f}s")
        if it["freeze"] and (is_image(it["src"]) or (d and it["start"] >= d)):
            die(f"freeze on {Path(it['src']).name} @ {it['start']}s: needs a video and a time inside it")
    groups = groups_of(tl)

    preset = PRESETS.get(args.preset, {})
    first = next((probes[i["src"]] for i in tl if not is_image(i["src"])), probes[tl[0]["src"]])
    aspect = args.aspect or preset.get("aspect")
    if aspect:
        W, H = ASPECTS[aspect]
        W, H = W * preset.get("scale", 1), H * preset.get("scale", 1)
    else:
        W, H = first["width"] - first["width"] % 2, first["height"] - first["height"] % 2
    fps = round(args.fps or preset.get("fps") or first["fps"] or 30, 3)
    if args.preview:
        W, H = (W // 2) - (W // 2) % 2, (H // 2) - (H // 2) % 2

    warnings = set()
    keep_hdr, hdr_transfer = False, None
    if args.hdr:
        if args.codec != "h265":
            die("--hdr needs --codec h265")
        hdr_src = next((p for p in probes.values() if p["hdr"]), None)
        if not hdr_src:
            warnings.add("--hdr: no HDR source found; rendering 10-bit SDR")
        else:
            keep_hdr, hdr_transfer = True, hdr_src.get("transfer") or "smpte2084"
    ten = args.ten_bit or args.hdr
    if ten and args.codec == "h264":
        warnings.add("--10bit ignored for h264 (players rarely support it); use --codec h265 or prores")
        ten = False
    pixfmt = "yuv420p10le" if ten or args.codec == "prores" else "yuv420p"
    for src, p in probes.items():
        if p["vfr"]:
            warnings.add(f"{Path(src).name}: variable frame rate (phone footage); conformed to {fps} fps")

    out = Path(args.out)
    cache_dir = Path(os.environ.get("VS_CACHE") or out.parent / ".vs-cache")
    ctx = Ctx(args, edl, W, H, fps, pixfmt, keep_hdr, cache_dir, warnings)
    ctx.lufs = None if args.no_loudnorm else (args.loudnorm if args.loudnorm is not None else preset.get("lufs"))
    if ctx.use_proxy:
        missing = [s for s in probes if not is_image(s) and not proxy_for(s)]
        if args.proxy and missing:
            warnings.add(f"no proxy for {len(missing)} source(s); using originals (make them: vs proxy <files>)")
    total = groups[-1]["out_end"]

    if args.chunks == "off" or args.range or args.dry_run:
        target = None
    elif args.chunks == "auto":
        target = 60.0 if total >= AUTO_CHUNK_MIN else None
    else:
        target = float(args.chunks)
    chunks = chunk_groups(groups, target) if target else [groups]
    if len(chunks) < 2:
        chunks = [groups]

    if not args.dry_run:
        stab_prepass(ctx, groups)
    venc, aenc = encoder_args(args, pixfmt, hdr_transfer)
    settings = {"render": RENDER_VERSION, "W": W, "H": H, "fps": fps, "pixfmt": pixfmt, "codec": args.codec,
                "crf": args.crf, "speed": args.speed, "preview": bool(args.preview), "proxy": bool(ctx.use_proxy), "font": args.font,
                "preset": args.preset, "hdr": bool(keep_hdr)}
    new_manifest = splice.manifest(edl, groups, total, settings, args.captions)
    new_manifest["args"] = {"argv": sys.argv[1:], "cwd": os.getcwd()}   # how it was rendered (for `vs fix --render`)
    cut_times = new_manifest["cuts"][1:-1]
    if args.codec == "h264":  # an IDR frame at every hard cut: a later revision can splice there without re-encoding
        venc += ["-force_key_frames", ",".join(f"{t:.4f}" for t in [0.0] + cut_times), "-x264-params", "forced-idr=1"]
    sp = None
    if args.since:
        sp = splice_plan(args.since, new_manifest, out)

    if sp and not args.dry_run and not args.range:
        if splice_render(ctx, groups, sp, venc, aenc, fps, total, out, new_manifest):
            return

    gr = Graph()
    if len(chunks) == 1:
        vl, al, total = build_shots(ctx, gr, groups)
    else:
        cache_dir.mkdir(parents=True, exist_ok=True)
        jobs = args.jobs or max(1, min(4, (os.cpu_count() or 2) // 2))
        threads = max(1, (os.cpu_count() or 2) // jobs)
        todo, paths = [], []
        for c in chunks:
            p = cache_dir / f"chunk-{chunk_key(ctx, c)}.mkv"
            paths.append(p)
            if (args.no_cache or not p.exists()) and p not in {q for _, q in todo}:
                todo.append((c, p))
        print(f"stage 1: {len(chunks)} chunks, {len(chunks) - len(todo)} cached, rendering {len(todo)} "
              f"with {jobs} job(s)", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=jobs) as ex:
            for f in [ex.submit(render_chunk, ctx, c, p, threads) for c, p in todo]:
                f.result()
        listing = Path(tempfile.mkstemp(suffix=".txt", dir=cache_dir)[1])
        listing.write_text("".join(f"file '{p.resolve()}'\n" for p in paths))
        ci = gr.add_input("-f", "concat", "-safe", "0", "-i", str(listing))
        vl, al = f"{ci}:v", f"{ci}:a"
        gr.f(f"[{vl}]setpts=PTS-STARTPTS[cv]")
        gr.f(f"[{al}]asetpts=PTS-STARTPTS,apad,atrim=0:{total:.4f}[ca]")
        vl, al = "cv", "ca"
    finish(ctx, gr, vl, al, total, out)

    out.parent.mkdir(parents=True, exist_ok=True)
    vmap, amap, length = "[vout]", "[aout]", total
    if args.range:  # trim inside the graph (output seeking used to drop the wrong -t and still decode everything)
        r0, _, r1 = args.range.partition("-")
        r0, r1 = float(r0), min(float(r1), total)
        gr.f(f"[vout]trim=start={r0:.4f}:end={r1:.4f},setpts=PTS-STARTPTS[vrange]")
        gr.f(f"[aout]atrim=start={r0:.4f}:end={r1:.4f},asetpts=PTS-STARTPTS[arange]")
        vmap, amap, length = "[vrange]", "[arange]", r1 - r0
        if "-force_key_frames" in venc:
            i = venc.index("-force_key_frames")
            venc[i + 1] = "0"
    cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error", "-stats", *gr.inputs,
           "-filter_complex", ";".join(gr.filters), "-map", vmap, "-map", amap,
           "-t", f"{length:.4f}", *venc, "-r", str(fps), *aenc, "-movflags", "+faststart", str(out)]
    for w in sorted(warnings):
        print(f"warning: {w}", file=sys.stderr)
    if preset.get("max") and total > preset["max"]:
        print(f"warning: {total:.1f}s is over the {args.preset} limit of {preset['max']}s", file=sys.stderr)
    if args.dry_run:
        print(shlex.join(cmd))  # copy-paste safe: the graph itself contains quotes
        return
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        tail = (p.stderr or "")[-2500:]
        die(f"render failed ({p.returncode}). Re-run with --dry-run to see the ffmpeg command.\n{tail}")
    o = probe(str(out))
    if not args.range:
        save_json(manifest_path(out), new_manifest)
    has_tr = any(g["overlap"] > 0 for g in groups[1:])
    print(f"rendered {out}: {o['width']}x{o['height']} @ {o['fps']}fps, {fmt_ts(o['duration'])} "
          f"({len(groups)} segments{', transitions' if has_tr else ''}"
          f"{f', {len(chunks)} chunks' if len(chunks) > 1 else ''})")


if __name__ == "__main__":
    main()
