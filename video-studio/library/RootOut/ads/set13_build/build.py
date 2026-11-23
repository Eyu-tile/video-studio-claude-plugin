#!/usr/bin/env python3
"""Set 13 builder. python3 work/build.py h1|h2|h3
Each segment = one generated clip trimmed to its speech (whisper word times), at 1080x1920/30, with overlays cued on
spoken words. Speaker audio is the clip's own lip-synced track (never VO over b-roll). Then concat, music bed, captions."""
import json, os, subprocess, sys, wave
from pathlib import Path
import numpy as np
P = Path(__file__).resolve().parent.parent; C = P / "raw/gen/clips"; G = P / "work/gfx"; WEB = P / "raw/web"; T = P / "work/tmp"
T.mkdir(parents=True, exist_ok=True)
FIX = {"wort": "wart", "root out": "RootOut", "rootout": "RootOut", "kid's": "kids'", "4": "4", "14": "fourteen"}

def run(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)

_m = None
def words(clip):
    """Cached whisper word timings for a clip's own audio."""
    cache = T / f"{clip}.words.json"
    if cache.exists(): return json.loads(cache.read_text())
    global _m
    if _m is None:
        from faster_whisper import WhisperModel; _m = WhisperModel("small.en", device="cpu", compute_type="int8")
    wav = T / f"{clip}.wav"; run(["ffmpeg", "-v", "error", "-y", "-i", str(C / f"{clip}.mp4"), "-ar", "16000", "-ac", "1", str(wav)])
    w = wave.open(str(wav)); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    segs, _ = _m.transcribe(a, beam_size=5, word_timestamps=True)
    out = [{"w": x.word.strip(), "s": round(x.start, 3), "e": round(x.end, 3)} for s in segs for x in s.words]
    cache.write_text(json.dumps(out)); return out

def at(ws, key, nth=0, edge="s"):
    hits = [w for w in ws if w["w"].lower().strip(".,!?'\"").startswith(key.lower())]
    return hits[nth][edge] if hits else None

# ---------------------------------------------------------------- segments
# overlay: (kind, file, start_word|float, end_word|float|None, extra)
#   kind 'png' = full-canvas PNG; 'pip' = video window (x, y, w, h, mask)
def seg(clip, ov=(), pre=0.05, post=0.22, cut_after=None, tail=None, speed=None):
    kid = clip in ("c02", "c10", "h3a")
    return dict(clip=clip, ov=list(ov), pre=pre, post=post, cut_after=cut_after, tail=tail, speed=speed or (1.0 if kid else 1.07))

def speech_end(clip):
    """Last moment of real speech (silencedetect), whisper word ends run long."""
    r = subprocess.run(["ffmpeg", "-i", str(C / f"{clip}.mp4"), "-af", "silencedetect=n=-38dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
    D = dur(C / f"{clip}.mp4"); last_start, open_ = None, False
    for l in r.splitlines():
        if "silence_start" in l: last_start = float(l.split("silence_start: ")[1]); open_ = True
        elif "silence_end" in l:
            e = float(l.split("silence_end: ")[1].split()[0]); open_ = e < D - 0.08
            if not open_: pass
    # trailing silence = the last one, if it reaches the end of the clip
    return last_start if (last_start is not None and (open_ or True) and last_start > D - 3.0 and _reaches_end(r, D)) else D
def _reaches_end(r, D):
    ends = [float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
    starts = [l for l in r.splitlines() if "silence_start" in l]
    return len(starts) > len(ends) or (ends and ends[-1] >= D - 0.1)

def web(name): return WEB / "cards" / f"{name}_card.png"
def pip_src(rel): return WEB / rel

BODY = [
    seg("c02", [("png", "w_freeze_card.png", "froze", "this", {})]),
    seg("c03"),
    seg("c04", [("png", "gal_1.png", "look", "dry", {}), ("png", "gal_2.png", "dry", "dark", {}), ("png", "gal_3.png", "dark", "smooth", {}),
                ("png", "gal_4.png", "smooth", None, {})]),
    seg("c05", [("png", "photo_cryo.png", "freezing", "like", {}), ("png", "w_comeback_card.png", "grows", None, {})]),
    seg("c06", [("pip", "../gen/clips/m1.mp4", 0.0, "pokeweed", {"x": 0, "y": 0, "w": 1080, "h": 1920, "r": 0, "fit": 1}),
                ("pip", "../gen/clips/m2.mp4", "pokeweed", 99, {"x": 0, "y": 0, "w": 1080, "h": 1920, "r": 0, "fit": 1}),
                ("png", "plant_lemon.png", "lemon", 99, {}), ("png", "plant_teatree.png", "tea", 99, {}),
                ("png", "plant_pokeweed.png", "pokeweed", 99, {}), ("png", "plant_cedar.png", "cedar", 99, {}),
                ("png", "p_8x.png", "eight", "and", {}),
                ("png", "photo_root.png", "root", None, {"nth": -1})], post=1.6),
    seg("c08", [("png", "w_kids4_card.png", "kid", None, {}), ("png", "p_kids.png", "kid", None, {"alt_for": "w_kids4_card.png"}),
]),
    seg("c09", [("png", "p_step1.png", "rub", "brush", {}), ("png", "p_step2.png", "brush", "clear", {}), ("png", "p_step3.png", "clear", None, {})], post=0.5),
    seg("c10", pre=0.25, post=0.45),
    seg("c11", [("png", "p_rootrule.png", "14", 3.7, {}),
                ("pip", "family/mixkit_48169_kids_running_grass_from_behind.mp4", "it", None, {"x": 140, "y": 150, "w": 800, "h": 560, "ss": 3, "nth": 1})]),
    seg("c12", [("png", "w_offer_card.png", "buy", None, {}), ("png", "p_offer.png", "buy", None, {"alt_for": "w_offer_card.png"})], post=0.6),
]
HOOKS = {
    "h1": [seg("c01", [("png", "t_h1.png", 0.0, "about", {}), ("png", "ba.png", "flaked", "about", {})])],
    "h2": [seg("h2", [("png", "t_h2.png", 0.0, "then", {}), ("png", "ba.png", "flaked", None, {})])],
    "h3": [seg("h3a", pre=0.2, post=0.35), seg("h3b")],
}

def render_seg(i, s, tag):
    clip = s["clip"]; src = C / f"{clip}.mp4"; ws = words(clip)
    t0 = max(0, ws[0]["s"] - s["pre"]); end_w = min(ws[-1]["e"], speech_end(clip))
    if s["cut_after"]: end_w = at(ws, s["cut_after"], edge="e")
    t1 = min(dur(src), end_w + s["post"]); L = t1 - t0
    inputs = ["-ss", f"{t0:.3f}", "-t", f"{L:.3f}", "-i", str(src)]
    fc = ["[0:v]scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuva420p[v0]"]; last = "v0"; n = 1
    have = {o[1] for o in s["ov"] if (G / o[1]).exists() or (o[0] == "pip" and pip_src(o[1]).exists())}
    for kind, f, a, b, ex in s["ov"]:
        if f not in have: continue
        if ex.get("alt_for") and ex["alt_for"] in have: continue   # pill is only the fallback for a missing screenshot
        ta = a if isinstance(a, float) else at(ws, a, ex.get("nth", 0)); tb = b if isinstance(b, (int, float)) and not isinstance(b, bool) else (at(ws, b) if b else None)
        if isinstance(b, float) and b < 99: tb = b + t0
        if ta is None: print("  ! cue not found", clip, a); continue
        ta = max(0.0, ta - t0); tb = (L if tb is None or tb >= 99 else max(ta + 0.4, tb - t0))
        if kind == "png":
            inputs += ["-loop", "1", "-t", f"{L:.3f}", "-i", str(G / f)]
            fc.append(f"[{n}:v]format=rgba,fade=in:st={ta:.2f}:d=0.15:alpha=1,fade=out:st={max(ta, tb - 0.12):.2f}:d=0.12:alpha=1[o{n}]")
            fc.append(f"[{last}][o{n}]overlay=0:0:enable='between(t,{ta:.2f},{tb:.2f})'[v{n}]")
        else:
            x, y, w, h = ex["x"], ex["y"], ex["w"], ex["h"]
            rr = ex.get("r", 44); mk = G / f"mask_{w}x{h}_r{rr}.png"
            if not mk.exists():
                from PIL import Image, ImageDraw
                mm = Image.new("L", (w, h), 0); ImageDraw.Draw(mm).rounded_rectangle((0, 0, w - 1, h - 1), rr, fill=255) if rr else mm.paste(255, (0, 0, w, h)); mm.save(mk)
            ss = ["-ss", str(ex["ss"])] if ex.get("ss") else []
            fit = ex.get("fit"); k = ((tb - ta) / dur(pip_src(f))) if fit else 1.0
            loop = [] if fit else ["-stream_loop", "-1"]
            inputs += [*loop, *ss, "-t", f"{L:.3f}", "-i", str(pip_src(f)), "-loop", "1", "-t", f"{L:.3f}", "-i", str(mk)]
            fc.append(f"[{n}:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setpts=(PTS-STARTPTS)*{k:.4f}+{ta:.2f}/TB,fps=30,format=rgba[p{n}]")
            fc.append(f"[{n+1}:v]scale={w}:{h},format=gray[m{n}]"); fc.append(f"[p{n}][m{n}]alphamerge[q{n}]")
            fc.append(f"[{last}][q{n}]overlay={x}:{y}:enable='between(t,{ta:.2f},{tb:.2f})':eof_action=repeat[v{n}]")
            last = f"v{n}"; n += 2; continue
        last = f"v{n}"; n += 1
    sp = s["speed"]
    fc.append(f"[{last}]setpts=PTS/{sp},fps=30,format=yuv420p[vout]")
    fc.append(f"[0:a]aresample=48000,aformat=channel_layouts=stereo,atempo={sp},afade=in:d=0.04,afade=out:st={L/sp-0.08:.3f}:d=0.08,loudnorm=I=-16:TP=-2:LRA=9[aout]")
    out = T / f"{tag}_{i:02d}_{clip}.mp4"
    import os
    if not (os.environ.get("REUSE") and out.exists()): run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "aac", "-b:a", "192k", "-t", f"{L/sp:.3f}", str(out)])
    shifted = [{"w": w["w"], "s": (w["s"] - t0) / sp, "e": (w["e"] - t0) / sp} for w in ws if t0 - 0.05 <= w["s"] < t1]
    if s["cut_after"]: shifted = [w for w in shifted if w["s"] < (end_w - t0) / sp - 0.05]
    for w in shifted: w["seg"] = i
    return out, L / sp, shifted

def endcard(tag, L=3.0):
    out = T / f"{tag}_99_end.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{L}", "-i", str(G / "endcard.png"), "-f", "lavfi", "-t", f"{L}", "-i", "anullsrc=r=48000:cl=stereo",
         "-vf", "scale=1080:1920,zoompan=z='1.0+0.012*on/90':d=1:s=1080x1920:fps=30,fade=in:d=0.2,format=yuv420p", "-c:v", "libx264", "-crf", "17",
         "-c:a", "aac", "-shortest", str(out)]); return out, L

def ass_time(t): h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60; return f"{h}:{m:02d}:{s:05.2f}"
def captions(all_words, total, tag):
    """Chunks of up to 3 words, white Inter ExtraBold with a black edge, the spoken word popping yellow."""
    hdr = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, "
           "SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
           "Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Cap,Inter ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,70,70,520,1\n\n"
           "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    def clean(t):
        t = t.strip(); low = t.lower().strip(".,!?")
        if low in ("wort",): t = t.lower().replace("wort", "wart")
        return t.replace("kid's", "kids'")
    W = [dict(w, w=clean(w["w"])) for w in all_words]
    # merge "Root" + "out" -> RootOut
    m = []
    for w in W:
        if m and m[-1]["w"].lower() == "root" and w["w"].lower().startswith("out") and m[-1].get("seg") == w.get("seg"): m[-1]["w"] = "RootOut" + w["w"][3:]; m[-1]["e"] = w["e"]
        else: m.append(w)
    lines, cur = [], []
    for w in m:
        cur.append(w)
        nxt = m[m.index(w) + 1] if m.index(w) + 1 < len(m) else None
        if len(cur) == 3 or w["w"][-1:] in ".,!?" or (len(" ".join(x["w"] for x in cur)) > 16) or (nxt and nxt.get("seg") != w.get("seg")):
            lines.append(cur); cur = []
    if cur: lines.append(cur)
    ev = []
    for li, ln in enumerate(lines):
        nxt_start = lines[li + 1][0]["s"] if li + 1 < len(lines) else total
        for j, w in enumerate(ln):
            a = w["s"]; b = ln[j + 1]["s"] if j + 1 < len(ln) else min(ln[-1]["e"] + 0.15, nxt_start - 0.02)
            txt = " ".join(("{\\c&H00D4FF&}" + x["w"].upper() + "{\\c&HFFFFFF&}") if k == j else x["w"].upper() for k, x in enumerate(ln))
            ev.append(f"Dialogue: 0,{ass_time(a)},{ass_time(min(b, total - 3.0))},Cap,,0,0,0,,{txt}")
    p = T / f"captions_{tag}.ass"; p.write_text(hdr + "\n".join(ev) + "\n"); return p

def build(tag):
    segs = HOOKS[tag] + ([dict(BODY[0], cut_after="cried", post=0.35)] + BODY[1:] if tag == "h3" else BODY)
    parts, allw, t = [], [], 0.0
    for i, s in enumerate(segs):
        if not (C / f"{s['clip']}.mp4").exists(): print("  missing clip", s["clip"]); continue
        out, L, ws = render_seg(i, s, tag); parts.append(out); allw += [dict(w, s=w["s"] + t, e=w["e"] + t, seg=i) for w in ws]; t += L
        print(f"  {s['clip']:5s} {L:5.2f}s  -> {t:6.2f}")
    e, L = endcard(tag); parts.append(e); t += L
    lst = T / f"{tag}_list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
    raw = T / f"{tag}_raw.mp4"; run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(raw)])
    total = dur(raw); ass = captions(allw, total, tag)
    music = P / "assets/music/wholesome.mp3"
    out = P / f"out/WilloMD_RootOut_Set13_{tag.upper()}_9x16_{os.environ.get("VER", "v2")}.mp4"; out.parent.mkdir(exist_ok=True)
    fc = (f"[0:v]rgbashift=rh=1:bh=-1,noise=c0s=6:c0f=t+u,vignette=angle=PI/8,eq=brightness=0.02:saturation=1.06,unsharp=3:3:0.25,"
          f"ass={ass}:fontsdir=/usr/share/fonts/opentype/inter[v];"
          f"[1:a]atrim=0:{total:.2f},volume=0.11,afade=in:d=1.2,afade=out:st={total-1.6:.2f}:d=1.6[m];"
          f"[0:a][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false[a]")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-stream_loop", "-1", "-i", str(music), "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "slow", "-crf", "21", "-maxrate", "9M", "-bufsize", "18M", "-pix_fmt", "yuv420p", "-ar", "48000",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-map_metadata", "-1", "-t", f"{total:.2f}", str(out)])
    print(tag, "->", out.name, f"{total:.1f}s")

if __name__ == "__main__":
    for tag in sys.argv[1:] or ["h1"]: build(tag)
