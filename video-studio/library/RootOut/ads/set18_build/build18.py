#!/usr/bin/env python3
"""Set 18 H1 builder. VO lines (ElevenLabs, verbatim) laid on one clock; every shot starts on a word of the script;
talking shots are cut from the Seedance takes and retimed so the lips land on the VO we play (Set 17 lipwarp method,
word anchors from ElevenLabs STT of each take). Out: work/build/H1/{video_noaudio.mp4, vo.wav, timeline.json}.
Usage: python3 build18.py [H1]"""
import json, os, re, subprocess, sys, difflib
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent)); import timeline as TLm
P = TLm.P; VO = P / "raw/vo"; RE = P / "raw/reuse"; ST = P / "raw/stock"; GEN = P / "raw/gen"; G = P / "assets/graphics"
OUT = P / "work/build/H1"; SH = OUT / "shots"; SH.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
def sh(a): r = subprocess.run(a, capture_output=True, text=True); r.returncode and sys.exit(" ".join(map(str, a))[:400] + "\n" + r.stderr[-1500:])
def ff(*a): sh(["ffmpeg", "-v", "error", "-y", *map(str, a)])
dur = TLm.dur
COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
ENC = ["-an", "-c:v", "libx264", "-crf", "17", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]

# ---------------- VO clock ----------------
ORDER = ["r01", "r02", "r03", "r04", "r05", "r06", "r07", "r08", "r09", "r10", "r11", "r12", "r13", "r14", "r15",
         "r15b_dad", "r15b_girl", "r16", "r17", "r18", "r19"]
GAP = 0.32
HOLD = {"r02": 0.15, "r05": 1.0, "r06": 1.3, "r07": 0.1, "r08": 0.45, "r09": 0.2, "r10": 0.35, "r11": 0.35, "r12": 0.1,
        "r13": 0.25, "r14": 0.35, "r15": 0.45, "r15b_dad": 0.3, "r15b_girl": 0.45, "r16": 0.35, "r17": 0.4, "r18": 0.3, "r19": 0.8}
def vo_clock():
    t = 0.25; at = {}
    for ln in ORDER:
        at[ln] = t; t += dur(VO / f"{ln}.mp3") + GAP + HOLD.get(ln, 0)
    return at, t
AT, VO_END = vo_clock()
def T(line, phrase): return AT[line] + TLm.find(line, phrase)[0] - 0.06

# ---------------- shot list (start anchor, source, options) ----------------
END_CARD = 3.2
S = [  # (start_time, kind, src, opts)
 (0.0, "talk", "K1", {"line": "r01"}),
 (T("r01", "Ask me how I know"), "talk", "K1", {"line": "r01", "zoom": 1.15}),
 (T("r02", "This is how"), "talk", "K1", {"line": "r02"}),
 (T("r02", "Root and all"), "clip", RE / "03_S1_b09_dand_root.mp4", {"in": 0.6}),
 (T("r03", "My son had"), "clip", RE / "37_S20_g12_feetup.mp4", {"in": 0.5}),
 (T("r03", "on his heel"), "clip", RE / "27_S19_b21_mason_sole.mp4", {"in": 0.0, "push": 1.12}),
 (T("r03", "The doctor took"), "clip", RE / "16_S17_b1_glove_wart.mp4", {"in": 0.0}),
 (T("r03", "and said"), "clip", ST / "b03_doctor/mixkit_32176_doctor-putting-on-a-stethoscope.mp4", {"in": 6.4}),
 (T("r03", "So we left it"), "talk", "K1", {"line": "r03"}),
 (T("r04", "Every week"), "talk", "K1", {"line": "r04"}),
 (T("r04", "I started checking"), "still", GEN / "stills/N1.png", {"push": (1.0, 1.1)}),
 (T("r04", "By week six"), "still", GEN / "stills/N2.png", {"push": (1.05, 1.12)}),
 (T("r04", "By week six") + 0.75, "still", GEN / "stills/N3.png", {"push": (1.05, 1.18)}),
 (T("r05", "Then a second"), "still", GEN / "stills/N4.png", {"push": (1.0, 1.12)}),
 (T("r05", "Then my daughter"), "clip", RE / "33_S20_g07_sister.mp4", {"in": 0.3}),
 (T("r05", "on her finger"), "still", GEN / "stills/N5.png", {"push": (1.05, 1.2), "fy": 0.62}),
 (T("r05", "She's wanted"), "talk", "K1", {"line": "r05"}),
 (T("r05", "This she got"), "talk", "K1", {"line": "r05", "zoom": 1.18}),
 (T("r06", "Turns out"), "talk", "K1", {"line": "r06"}),
 (T("r06", "Almost fifteen hundred"), "clip", RE / "41_S19_b29_sneakers.mp4", {"in": 0.3}),
 (T("r06", "If someone at home"), "card", G / "w1_card.png", {"bg": GEN / "frames/F_K1.png", "chip": (G / "chip_x2.png", "twice")}),
 (T("r06", "And the it'll go away part"), "card", G / "w3_card.png", {"bg": GEN / "frames/F_K1.png"}),
 (T("r06", "About half of kids'"), "card", G / "w2_card.png", {"bg": GEN / "frames/F_K1.png"}),
 (T("r06", "Half don't"), "anim", G / "c_split.mp4", {}),
 (T("r06", "We got the other half"), "talk", "K1", {"line": "r06"}),
 (AT["r06"] + dur(VO / "r06.mp3") + 0.1, "clip", RE / "25_S1_b17_hallway.mp4", {"in": 0.4}),
 (T("r07", "So let me save"), "talk", "K1", {"line": "r07"}),
 (T("r07", "Here's what you'll"), "clip", GEN / "clips/G1.mp4", {"in": 0.0}),
 (T("r08", "Freezing"), "clip", RE / "24_S1_b04_clinic.mp4", {"in": 0.3, "whoosh": True}),
 (T("r08", "a milkshake"), "still", GEN / "stills/N6.png", {"push": (1.0, 1.1)}),
 (T("r08", "then you book"), "anim", G / "c_freezecal.mp4", {}),
 (T("r08", "Congratulations"), "talk", "K2a", {"line": "r08", "zoom": 1.12}),
 (T("r09", "Acid from"), "talk", "K2a", {"line": "r09", "whoosh": True}),
 (T("r09", "It turns the skin"), "still", GEN / "stills/N7.png", {"push": (1.05, 1.2)}),
 (T("r09", "The wart doesn't"), "talk", "K2a", {"line": "r09"}),
 (T("r10", "Duct tape"), "still", ST / "b07_ducttape/ov_ducttape_bandage_Conklin.jpg", {"push": (1.0, 1.08), "whoosh": True}),
 (T("r10", "A week of sticky"), "clip", RE / "40_S19_b25_socks.mp4", {"in": 1.6}),
 (T("r10", "Same wart"), "talk", "K2a", {"line": "r10", "zoom": 1.15}),
 (T("r11", "Every one of those"), "clip", RE / "21_S19_b61_shelf_sweep.mp4", {"in": 0.4}),
 (T("r11", "Freezing acid and shaving"), "talk", "Y1", {"line": "r11"}),
 (T("r11", "like picking a dandelion"), "clip", RE / "00_S1_b06_dand_snap.mp4", {"in": 1.2}),
 (T("r11", "The root stays"), "clip", RE / "07_S17_x3_soil_cutaway.mp4", {"in": 0.0}),
 (T("r11", "so it grows back"), "anim", G / "c_sidecut.mp4", {}),
 (T("r12", "You have to get under"), "talk", "K2b", {"line": "r12"}),
 (T("r12", "That's what RootOut does"), "talk", "K2b", {"line": "r12", "zoom": 1.1, "whoosh": True}),
 (T("r12", "It's an oil with four"), "talk", "K2b", {"line": "r12", "ov": [(G / "plants.png", 0.25, None, 90, 1180)]}),
 (T("r13", "Lemon softens"), "clip", RE / "08_S13_m1_skin_door.mp4", {"in": 0.0}),
 (T("r13", "Tea tree is a thin oil"), "talk", "K2b", {"line": "r13"}),
 (T("r13", "It sinks in"), "clip", RE / "46_S1_b10_towels.mp4", {"in": 0.3, "gauge": True}),
 (T("r13", "and it carries"), "talk", "K2b", {"line": "r13"}),
 (T("r13", "Pokeweed and white cedar"), "clip", RE / "15_S17_x6_root_3d.mp4", {"in": 0.0}),
 (T("r13", "so it can't grow back"), "clip", RE / "09_S13_m2_skin_root.mp4", {"in": 2.0}),
 (T("r14", "And it's made for kids"), "talk", "K2b", {"line": "r14", "chips": [("chip_kids4", "A kids' formula"), ("chip_noacid", "No acid"),
                                                                                  ("chip_nofreeze", "no freezing"), ("chip_noblister", "no blister")]}),
 (T("r15", "At bedtime"), "clip", RE / "30_S19_b52_socks_bed.mp4", {"in": 0.5}),
 (T("r15", "two light rubs"), "clip", RE / "17_S19_b37_file_kid.mp4", {"in": 0.6}),
 (T("r15", "Brush the oil on"), "clip", RE / "12_S17_b2_routine.mp4", {"in": 3.6, "fy": 0.45, "zoom": 1.25}),
 (T("r15", "A clear dot on top"), "clip", RE / "19_S19_b55_dot_v2.mp4", {"in": 1.0}),
 (T("r15", "Two minutes"), "clip", RE / "23_S1_b11_nightstand.mp4", {"in": 5.0, "lamp_off": True}),
 (T("r15b_dad", "Does it hurt"), "clip", RE / "38_S19_b35_pillow.mp4", {"in": 0.0}),
 (T("r16", "About two weeks later"), "anim", G / "c_nights.mp4", {}),
 (T("r16", "his were gone"), "still", GEN / "stills/N9.png", {"push": (1.0, 1.1)}),
 (T("r16", "Hers too"), "still", GEN / "stills/N10.png", {"push": (1.05, 1.15), "fy": 0.62}),
 (T("r16", "We kept going"), "talk", "K3", {"line": "r16", "ov": [(G / "chip_plus14.png", 0.9, None, "c", 1200)]}),
 (T("r17", "Last Saturday"), "clip", RE / "34_S20_g14_run.mp4", {"in": 0.2}),
 (T("r17", "through the sprinkler"), "clip", ST / "b17_sprinkler/mixkit_19551_sprinkler-watering-the-grass.mp4", {"in": 9.0}),
 (T("r17", "and I didn't check"), "talk", "Y2", {"line": "r17"}),
 (T("r18", "Link's below"), "clip", RE / "14_S17_x10_three_bottles.mp4", {"in": 0.8, "ov": [(G / "chip_offer.png", 0.4, None, "c", 380)]}),
 (T("r18", "so every kid"), "talk", "K3", {"line": "r18"}),
 (T("r18", "And you've got ninety"), "talk", "K3", {"line": "r18", "ov": [(G / "seal90.png", 0.5, None, 680, 1180)]}),
 (T("r19", "Or you know"), "talk", "K3", {"line": "r19", "zoom": 1.08}),
 (VO_END - 0.2, "anim", G / "c_end.mp4", {}),
]
TOTAL = VO_END - 0.2 + END_CARD
fr = lambda t: int(round(t * FPS))

# ---------------- talking shots: line time -> take time (lip warp) ----------------
MAP = json.load(open(P / "work/lipsync_map.json"))
def clip_words(take):
    f = GEN / f"clips/{take}.stt.json"
    if not f.exists():
        sh(["curl", "-s", "-m", "180", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text", "-H", "xi-api-key: dummy",
            "-F", "model_id=scribe_v1", "-F", "timestamps_granularity=word", "-F", f"file=@{GEN / f'clips/{take}.mp4'}", "-o", str(f)])
    d = json.load(open(f)); out = []
    for w in d["words"]:
        if w.get("type") != "word": continue
        for p in w["text"].replace("-", " ").split(): out.append((TLm.NUM.get(TLm.norm(p), TLm.norm(p)), w["start"], w["end"]))
    return out
def ls_words(take):
    out = []
    for m in MAP[take]:
        for n, s, e in TLm.words(m["line"]):
            if m["src_in"] - 0.01 <= s and e <= m["src_out"] + 0.01:
                o = m["take_in"] - m["src_in"]; out.append((n, s + o, e + o))
    return out
_anch = {}
def anchors(take):
    if take in _anch: return _anch[take]
    l, c = ls_words(take), clip_words(take)
    sm = difflib.SequenceMatcher(None, [x[0] for x in l], [x[0] for x in c], autojunk=False); pts = [(0.0, 0.0)]
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): pts += [(l[a + k][1], c[b + k][1]), (l[a + k][2], c[b + k][2])]
    pts = sorted(set(pts)); mono = [pts[0]]
    for p in pts[1:]:
        if p[0] > mono[-1][0] + 0.02 and p[1] > mono[-1][1] + 0.02: mono.append(p)
    _anch[take] = mono; matched = sum(n for *_, n in sm.get_matching_blocks())
    print(f"  {take}: {matched}/{len(l)} words matched in the take")
    return mono
def fmap(take, x):
    a = anchors(take); xs, ys = [p[0] for p in a], [p[1] for p in a]
    return float(np.interp(x, xs, ys)) if x <= xs[-1] else ys[-1] + (x - xs[-1])
def line_to_ls(take, line, t):
    """VO time inside a line -> lip-sync track time (pieces of that line); outside a piece: nearest piece edge + offset."""
    ms = [m for m in MAP[take] if m["line"] == line]
    for m in ms:
        if m["src_in"] - 0.6 <= t <= m["src_out"] + 2.0: return m["take_in"] + t - m["src_in"]
    m = min(ms, key=lambda m: abs(t - m["src_in"])); return m["take_in"] + t - m["src_in"]
def render_talk(out, take, line, t0, t1, zoom=1.0):
    """Output interval [t0,t1] on the VO clock -> chunks of the take, each retimed to its word anchors."""
    clip = GEN / f"clips/{take}.mp4"; cd = dur(clip)
    x0 = line_to_ls(take, line, t0 - AT[line]); x1 = x0 + (t1 - t0)
    a = anchors(take); cuts = [x0] + [p[0] for p in a if x0 + 0.3 < p[0] < x1 - 0.3] + [x1]; keep = [cuts[0]]
    for c in cuts[1:-1]:
        if c - keep[-1] >= 0.4: keep.append(c)
    keep.append(x1); parts = []; tmp = Path(str(out) + "_p"); tmp.mkdir(exist_ok=True); s_prev = None
    for i in range(len(keep) - 1):
        a0, a1 = keep[i], keep[i + 1]; dd = a1 - a0
        s0 = fmap(take, a0) if s_prev is None else s_prev; want = fmap(take, a1) - fmap(take, a0)
        s1 = s0 + min(max(want, dd * 0.65), dd * 1.6); s1 = min(s1, cd - 0.04); s0 = min(s0, cd - 0.3); s_prev = s1
        sd = max(s1 - s0, 0.1); pp = tmp / f"{i:03d}.mp4"
        zf = f",scale=iw*{zoom}:ih*{zoom},crop={W}:{H}" if zoom != 1 else ""
        ff("-ss", f"{s0:.3f}", "-t", f"{sd:.3f}", "-i", clip, "-vf", f"setpts=PTS*{dd / sd:.5f},{COVER}{zf},fps={FPS},setsar=1",
           "-frames:v", max(1, fr(a1 - x0) - fr(a0 - x0)), *ENC, pp); parts.append(pp)
    (tmp / "l.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    ff("-f", "concat", "-safe", "0", "-i", tmp / "l.txt", "-frames:v", fr(t1) - fr(t0), *ENC, out)

def render_clip(out, src, n, o):
    d = dur(src); i0 = o.get("in", 0.0); avail = min(d, o.get("out", d)) - i0; need = n / FPS
    sp = min(1.0, avail / need) if avail > 0 else 1.0
    if sp < 0.7: sp = 0.7  # never slower than 0.7x; tail frames clone below if still short
    z = o.get("zoom", 1.0); fy = o.get("fy", 0.5)
    vf = f"setpts=PTS/{sp:.4f},scale={W*z:.0f}:{H*z:.0f}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-{W})/2:(ih-{H})*{fy}"
    if o.get("push"):
        p = o["push"]; vf += f",zoompan=z='1+({p-1:.3f})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}"
    if o.get("lamp_off"): vf += f",fade=t=out:st={need - 0.55:.2f}:d=0.35"
    vf += f",fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration=2"
    ff("-ss", f"{i0:.3f}", "-i", src, "-vf", vf, "-frames:v", n, *ENC, out)

def render_still(out, src, n, o):
    z0, z1 = o.get("push", (1.0, 1.1)); fy = o.get("fy", 0.5)
    vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2}:(iw-{W*2})/2:(ih-{H*2})*{fy},"
          f"zoompan=z='{z0}+({z1-z0:.3f})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},setsar=1")
    ff("-loop", "1", "-i", src, "-vf", vf, "-frames:v", n, *ENC, out)

def render_card(out, card, n, o):
    """Web card slides up over the dad frame, blurred and dimmed (slow push)."""
    vf = (f"[0]scale={W*1.1:.0f}:{H*1.1:.0f}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=18:2,eq=brightness=-0.12,setsar=1[bg];"
          f"[1]scale=1000:-1[c];[bg][c]overlay=x=(W-w)/2:y='(H-h)/2-120+max(0,260*(1-t/0.35))':shortest=0,fps={FPS}")
    ff("-loop", "1", "-i", o["bg"], "-loop", "1", "-i", card, "-filter_complex", vf, "-frames:v", n, *ENC, out)

def render_anim(out, src, n, o):
    d = dur(src); sp = min(1.25, max(0.6, d / (n / FPS)))
    ff("-i", src, "-vf", f"setpts=PTS/{sp:.4f},{COVER},fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration=3", "-frames:v", n, *ENC, out)

def build():
    shots = []; bounds = [s[0] for s in S] + [TOTAL]
    for k, (t0, kind, src, o) in enumerate(S):
        t1 = bounds[k + 1]; n = fr(t1) - fr(t0); out = SH / f"s{k + 1:02d}.mp4"
        if not out.exists() or os.environ.get("REBUILD"):
            if kind == "talk" and not (GEN / f"clips/{src}.mp4").exists():
                ff("-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}", "-frames:v", n, *ENC, str(out) + ".ph.mp4"); os.replace(str(out) + ".ph.mp4", SH / f"ph_s{k + 1:02d}.mp4")
                out = SH / f"ph_s{k + 1:02d}.mp4"
            elif kind == "talk": render_talk(out, src, o["line"], t0, t1, o.get("zoom", 1.0))
            elif kind == "clip": render_clip(out, src, n, o)
            elif kind == "still": render_still(out, src, n, o)
            elif kind == "card": render_card(out, src, n, o)
            elif kind == "anim": render_anim(out, src, n, o)
        shots.append({"n": k + 1, "t0": round(t0, 3), "t1": round(t1, 3), "kind": kind, "src": str(src), "opts": {k: str(v) for k, v in o.items()}})
        print(f"s{k + 1:02d} {t0:6.2f}-{t1:6.2f} {kind:5s} {Path(str(src)).stem}")
    (SH / "l.txt").write_text("".join(f"file '{('s' if (SH / f's{s[chr(110)]:02d}.mp4').exists() else 'ph_s')}{s['n']:02d}.mp4'\n" for s in shots))
    ff("-f", "concat", "-safe", "0", "-i", SH / "l.txt", "-c", "copy", OUT / "picture.mp4")
    # VO track
    ins = []; fl = []
    for i, ln in enumerate(ORDER):
        ins += ["-i", VO / f"{ln}.mp3"]; fl.append(f"[{i}]aresample=48000,aformat=channel_layouts=mono,adelay={int(AT[ln]*1000)}[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(ORDER))) + f"amix=inputs={len(ORDER)}:normalize=0,apad=whole_dur={TOTAL:.3f}[vo]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vo]", "-t", f"{TOTAL:.3f}", "-c:a", "pcm_s16le", OUT / "vo.wav")
    json.dump({"at": AT, "total": TOTAL, "shots": shots}, open(OUT / "timeline.json", "w"), indent=1)
    print("total", round(TOTAL, 2), "s,", len(shots), "shots")

if __name__ == "__main__": build()
