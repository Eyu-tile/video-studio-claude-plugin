#!/usr/bin/env python3
"""Set 18 finish: overlays (hook box, chips, plants, 8x gauge, offer, seal), captions = the script text word for word
timed from the VO, sound (VO + room tone + foley/whoosh + ducked music bed), light phone finish, -14 LUFS / TP -2.
Usage: python3 finish18.py  -> out/WilloMD_RootOut_Set18_H1_9x16_v1.mp4"""
import json, re, subprocess, sys, difflib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import timeline as TLm
P = TLm.P; B = P / "work/build/H1"; G = P / "assets/graphics"; VO = P / "raw/vo"
SFX = Path("/home/user/video-studio-claude-plugin/plugins/video-studio/skills/media-use/audio/assets/sfx")
MUSIC = P / "assets/music/Investigations.mp3"
TL = json.load(open(B / "timeline.json")); AT = TL["at"]; TOTAL = TL["total"]; SHOTS = TL["shots"]
LINES = {l[0]: l[2] for l in json.load(open(P / "work/lines.json"))["lines"]}
OUTF = P / "out/WilloMD_RootOut_Set18_H1_9x16_v1.mp4"; OUTF.parent.mkdir(exist_ok=True)
def ff(*a):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *map(str, a)], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-2500:])
def wt(line, phrase): return AT[line] + TLm.find(line, phrase)[0]
def shot(n): return next(s for s in SHOTS if s["n"] == n)
def shot_of(src_stem, kind=None): return [s for s in SHOTS if Path(s["src"]).stem == src_stem and (kind is None or s["kind"] == kind)]

# ---------------- overlays: (png, t0, t1, x, y) ; x "c" = centred ----------------
ov = [(G / "hook_h1.png", 0.15, 3.2, "c", 150)]
w1 = shot_of("w1_card")[0]; ov.append((G / "chip_x2.png", wt("r06", "twice as likely"), w1["t1"], "c", 1440))
s47 = [s for s in SHOTS if s["kind"] == "talk" and "plants" in s["opts"].get("ov", "")][0]; ov.append((G / "plants.png", s47["t0"] + 0.25, s47["t1"], "c", 980))
for name, ph in (("chip_kids4", "A kids' formula"), ("chip_noacid", "No acid"), ("chip_nofreeze", "no freezing"), ("chip_noblister", "no blister")):
    t0 = wt("r14", ph); end = wt("r14", "Just a little cool tingle")
    y = {"chip_kids4": 780, "chip_noacid": 900, "chip_nofreeze": 900, "chip_noblister": 900}[name]
    x = {"chip_kids4": "c", "chip_noacid": 70, "chip_nofreeze": 360, "chip_noblister": 720}[name]
    ov.append((G / f"{name}.png", t0, end + 1.2, x, y))
ov.append((G / "chip_plus14.png", wt("r16", "fourteen more nights"), shot_of("N10")[0]["t1"] + 3.0, "c", 980))
x10 = shot_of("14_S17_x10_three_bottles")[0]; ov.append((G / "chip_offer.png", x10["t0"] + 0.35, x10["t1"], "c", 300))
seal_t = wt("r18", "ninety days"); ov.append((G / "seal90.png", seal_t, wt("r19", "Or you know"), 640, 900))
gauge = [s for s in SHOTS if "gauge" in s["opts"]][0]

# ---------------- captions: script text, VO word times ----------------
SCRIPT_FORMS = [(("fifteen", "hundred"), "1,500"), (("eight", "times"), "8x"), (("four", "and"), None)]
def cap_tokens():
    toks = []
    for ln in TL["at"]:
        txt = LINES[ln]; W = TLm.words(ln); spoken = txt.replace("'Leave", "‘Leave").split()
        A = [TLm.NUM.get(TLm.norm(x), TLm.norm(x)) for x in spoken]; Bn = [w[0] for w in W]
        sm = difflib.SequenceMatcher(None, A, Bn, autojunk=False); times = [None] * len(A)
        for a, b, n in sm.get_matching_blocks():
            for k in range(n): times[a + k] = (W[b + k][1], W[b + k][2])
        for i in range(len(A)):  # fill gaps (joined/split words)
            if times[i] is None:
                p = next((times[j] for j in range(i - 1, -1, -1) if times[j]), (0, 0)); times[i] = (p[1], p[1] + 0.2)
        i = 0
        while i < len(spoken):
            w = spoken[i]; s, e = times[i]
            nxt = spoken[i + 1] if i + 1 < len(spoken) else ""
            if TLm.norm(w) == "fifteen" and TLm.norm(nxt) == "hundred": w, e = "1,500", times[i + 1][1]; i += 1
            elif TLm.norm(w) == "eight" and TLm.norm(nxt) == "times": w, e = "8x", times[i + 1][1]; i += 1
            elif TLm.norm(w) == "four" and TLm.norm(nxt) == "and": w = "4"
            elif TLm.norm(w) == "fourteen": w = "14"
            elif TLm.norm(w) == "ninety": w = "90"
            toks.append([w.replace("‘", "'"), AT[ln] + s, AT[ln] + e, ln]); i += 1
    return toks
def groups(toks):
    out, cur = [], []
    for t in toks:
        if cur and (t[3] != cur[-1][3] or t[1] - cur[-1][2] > 0.6): out.append(cur); cur = []
        cur.append(t); end = t[0][-1:] in ".,?!"
        if len(cur) >= 4 or (end and len(cur) >= 2) or sum(len(x[0]) for x in cur) > 22: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
CARD = [(s["t0"], s["t1"]) for s in SHOTS if s["kind"] == "card"]
NO_CAP = [(TOTAL - 3.2, TOTAL)]
def write_ass(path):
    L = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "", "[V4+ Styles]",
         "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         "Style: Cap,Inter ExtraBold,66,&H00201814,&H00201814,&H00FFFFFF,&H50000000,0,0,0,0,100,100,0,0,3,16,0,2,90,90,560,1",
         "Style: CapTop,Inter ExtraBold,62,&H00201814,&H00201814,&H00FFFFFF,&H50000000,0,0,0,0,100,100,0,0,3,16,0,8,90,90,250,1",
         "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    gs = groups(cap_tokens()); n = 0
    for i, g in enumerate(gs):
        s = g[0][1] - 0.04; e = min(g[-1][2] + 0.25, gs[i + 1][0][1] - 0.04 if i + 1 < len(gs) else g[-1][2] + 0.25)
        if any(a <= s < b for a, b in NO_CAP): continue
        st = "CapTop" if any(a - 0.05 <= s < b for a, b in CARD) else "Cap"
        txt = " ".join(t[0] for t in g); txt = txt[0].upper() + txt[1:] if g[0][0][:1].islower() and i and gs[i - 1][-1][0][-1:] in ".?!" else txt
        L.append(f"Dialogue: 0,{ts(s)},{ts(e)},{st},,0,0,0,,{{\\fad(60,40)}}{txt}"); n += 1
    Path(path).write_text("\n".join(L) + "\n"); return gs

def main():
    T = P / "work/finish"; T.mkdir(parents=True, exist_ok=True)
    gs = write_ass(T / "captions.ass")
    words = [t[0] for g in gs for t in g]; json.dump(words, open(T / "caption_words.json", "w"))
    # ---- picture: overlays + gauge + captions + finish ----
    ins = ["-i", B / "picture.mp4"]; fl = ["[0]setpts=PTS-STARTPTS[v0]"]; last = "v0"
    for k, (png, t0, t1, x, y) in enumerate(ov):
        d = t1 - t0; ins += ["-loop", "1", "-framerate", "30", "-t", f"{d:.2f}", "-i", png]; j = k + 1
        X = "(W-w)/2" if x == "c" else str(x)
        fl.append(f"[{j}]format=rgba,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st={d - 0.15:.2f}:d=0.15:alpha=1,setpts=PTS+{t0:.3f}/TB[o{j}]")
        fl.append(f"[{last}][o{j}]overlay=x={X}:y='{y}+max(0,40*(1-(t-{t0:.2f})/0.18))':eof_action=pass[v{j}]"); last = f"v{j}"
    j = len(ov) + 1
    ins += ["-framerate", "30", "-i", G / "gauge/g%03d.png"]
    fl.append(f"[{j}]setpts=PTS-STARTPTS+{gauge['t0'] + 0.2:.2f}/TB,tpad=stop_mode=clone:stop_duration=6[g]")
    fl.append(f"[{last}][g]overlay=x=770:y=520:enable='between(t,{gauge['t0'] + 0.2:.2f},{gauge['t1']:.2f})'[vg]")
    fl.append(f"[vg]subtitles={T / 'captions.ass'}:fontsdir=/usr/share/fonts/opentype/inter,"
              "noise=alls=7:allf=t,vignette=PI/5.5,unsharp=5:5:0.35,format=yuv420p[vout]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vout]", "-t", f"{TOTAL:.3f}", "-c:v", "libx264", "-crf", "21", "-maxrate", "9M", "-bufsize", "18M", "-preset", "medium", "-r", "30", T / "picture_fin.mp4")
    # ---- sound ----
    sfx = []
    for s in SHOTS:
        o = s["opts"]
        if "whoosh" in o: sfx.append((SFX / "whoosh-short.mp3", s["t0"] - 0.12, -10))
        if "lamp_off" in o: sfx.append((SFX / "click-soft.mp3", s["t1"] - 0.6, -6))
        if s["kind"] in ("card",): sfx.append((SFX / "whoosh.mp3", s["t0"] - 0.05, -16))
    for png, t0, t1, x, y in ov[1:]: sfx.append((SFX / "pop.mp3", t0, -14))
    sfx.append((SFX / "whoosh-cinematic.mp3", TOTAL - 3.3, -12))
    ins = ["-i", B / "vo.wav", "-stream_loop", "-1", "-i", MUSIC]
    fl = [f"anoisesrc=color=brown:amplitude=0.02:d={TOTAL:.2f},lowpass=f=420,volume=-12dB[room]",
          "[0]aresample=48000,aformat=channel_layouts=stereo,asplit=2[vo][vok]",
          f"[1]atrim=0:{TOTAL:.2f},volume=-23dB,aformat=channel_layouts=stereo[mus]",
          "[mus][vok]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[duck]"]
    mix = ["[vo]", "[duck]", "[room]"]
    for k, (f, t, db) in enumerate(sfx):
        j = k + 2; ins += ["-i", f]; fl.append(f"[{j}]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={max(0, int(t * 1000))}:all=1[x{j}]"); mix.append(f"[x{j}]")
    fl.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=0:{TOTAL:.3f},loudnorm=I=-14:TP=-2.0:LRA=9[aout]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[aout]", "-ar", "48000", T / "mix.wav")
    ff("-i", T / "picture_fin.mp4", "-i", T / "mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-shortest", "-movflags", "+faststart", OUTF)
    print("out", OUTF, round(TOTAL, 2), "s")
if __name__ == "__main__": main()
