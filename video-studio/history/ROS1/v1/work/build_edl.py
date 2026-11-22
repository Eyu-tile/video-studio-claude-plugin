#!/usr/bin/env python3
"""Build the Set 1 EDLs (H1/H2/H3) from the generated clips, VO lines and code-made graphics.
Talking clips keep their own (lip-synced) audio, trimmed to the speech; every other line is an ElevenLabs VO file
placed on a VO track over muted b-roll. Picture length of each beat = its voice length + a short breath."""
import json, subprocess, sys
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent.parent
C, V, G = P / "raw/gen/clips", P / "raw/gen/vo", P / "work/gfx"
BREATH = 0.28

def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout)

def speech_window(clip):
    """First and last speech in a talking clip (energy-based), so the cut starts on the first word."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(clip), "-ac", "1", "-ar", "8000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    x = np.abs(np.frombuffer(raw, np.int16).astype(float)); win = 160
    e = x[: len(x) // win * win].reshape(-1, win).mean(1); thr = max(e.max() * 0.12, 200)
    idx = np.where(e > thr)[0]
    if not len(idx): return 0.0, dur(clip)
    return max(0.0, idx[0] * win / 8000 - 0.12), min(dur(clip), (idx[-1] + 1) * win / 8000 + 0.25)

def seg(src, start, end, **kw):
    return {"src": str(src), "start": round(start, 3), "end": round(end, 3), **kw}

def build(hook):
    segs, vo, t = [], [], 0.0
    def talk(name):  # lip-synced clip with its own audio
        nonlocal t
        s0, s1 = speech_window(C / f"{name}.mp4"); segs.append(seg(C / f"{name}.mp4", s0, s1, note=name)); t += s1 - s0
    def voiced(vofile, shots):  # VO over muted shots; shots = [(file, start, weight)], stretched to fill the VO
        nonlocal t
        L = dur(V / vofile) + BREATH; vo.append({"file": str(V / vofile), "at": round(t + 0.08, 3)})
        tot = sum(w for _, _, w in shots); out = 0
        for k, (f, s, w) in enumerate(shots):
            d = L * w / tot if k < len(shots) - 1 else L - out
            avail = dur(f) - s
            if d > avail:  # slow it down slightly rather than freeze (max 25%)
                segs.append(seg(f, s, s + avail, mute=True, speed=round(avail / d, 3), note=f.stem))
            else:
                segs.append(seg(f, s, s + d, mute=True, note=f.stem))
            out += d
        t += L
    # ---- hook + bridge ----
    if hook == "h1":
        talk("c01_hook_h1"); voiced("vo01.mp3", [(C / "b02_clinic.mp4", 0.3, 1)])
    elif hook == "h2":
        talk("c12_hook_h2"); voiced("vo13.mp3", [(C / "b02_clinic.mp4", 0.0, 1)])
    else:
        talk("c14_hook_h3"); voiced("vo15.mp3", [(C / "b02_clinic.mp4", 0.3, 1)])
    hook_end = t
    # ---- body ----
    voiced("vo02.mp3", [(C / "b03_bathroom.mp4", 0.4, 1)])
    voiced("vo03.mp3", [(C / "b04_clinic_a.mp4", 0.0, 1), (C / "b05_wart_back.mp4", 0.2, 1)])
    talk("c04_reframe")
    voiced("vo05.mp3", [(C / "b06_dand_snap.mp4", 0.3, 2.2), (C / "b07_dand_back.mp4", 0.5, 1.6), (G / "g11_frost.mp4", 0, 2.6),
                        (C / "b08_dand_water.mp4", 0.6, 1.4), (C / "b09_dand_root.mp4", 0.3, 2.0)])
    plants_at = t
    voiced("vo06.mp3", [(G / "g12a_team.mp4", 0, 7.0), (C / "b10_towels.mp4", 0.2, 3.6), (G / "g12b_team.mp4", 0, 4.5)])
    towels_at = plants_at + (dur(V / "vo06.mp3") + BREATH) * 7.0 / 15.1
    voiced("vo07.mp3", [(C / "b11_nightstand.mp4", 0.0, 1)])
    voiced("vo08.mp3", [(C / "b12_file.mp4", 0.1, 3.6), (C / "b13_brush.mp4", 0.2, 4.6), (C / "b14_dot.mp4", 0.2, 3.5),
                        (C / "b15_lamp.mp4", 0.3, 3.0), (G / "g19_clock.mp4", 0, 2.4)])
    voiced("vo09.mp3", [(C / "b17_hallway.mp4", 0.0, 1)])
    testi_at = t
    talk("c16_mom1"); talk("c17_mom2")
    segs.append(seg(C / "b18_dad.mp4", 0.3, 3.0, mute=True, note="b18_dad")); t += 2.7
    talk("c18_mom3"); testi_end = t
    voiced("vo10.mp3", [(G / "g26_stakes.mp4", 0, 1)])
    voiced("vo11.mp3", [(G / "g27_offer.mp4", 0, 1)])
    segs.append(seg(G / "g28_end.mp4", 0, 2.5, mute=True, note="end card")); t += 2.5

    hook_txt = {"h1": "Never again.", "h2": "Cancelled 4 times.", "h3": "His wart hurts.\nI can't fix it."}[hook]
    small = {"pos": "bottom", "size": 0.026, "color": "#FFFFFF", "box": "#00000080", "anim": "none"}
    edl = {
        "segments": segs, "grade": "natural",
        "texts": [
            {"text": hook_txt, "start": 0.0, "end": round(min(hook_end, 3.2), 2), "pos": "top", "size": 0.072, "anim": "pop",
             "color": "#FFFFFF", "box": "#0B2A5B", "font": "Inter", "bold": True},
            {"text": "†Based on our manufacturer's absorption testing against a regular cream.", "start": round(towels_at, 2),
             "end": round(towels_at + 3.6, 2), **small},
            {"text": "*Homeopathic claims are based on traditional homeopathic practice, not accepted medical evidence,\nand are not FDA evaluated. Results vary.",
             "start": round(plants_at, 2), "end": round(towels_at, 2), **small},
            {"text": "AI-generated people. Not real customers.", "start": round(testi_at, 2), "end": round(testi_end, 2), **small},
        ],
        "blurs": [{"start": round(hook_end - (dur(V / ('vo01.mp3' if hook == 'h1' else 'vo13.mp3' if hook == 'h2' else 'vo15.mp3')) + BREATH), 2),
                   "end": round(hook_end, 2), "x": 0.33, "y": 0.22, "w": 0.4, "h": 0.2, "mode": "blur", "strength": 30}],
        "tracks": [{"name": "vo", "gain_db": 0, "clips": vo}],
        "audio": {"enhance": False},
    }
    out = P / "work/ads" / f"set1_{hook}.edl.json"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(edl, indent=1)); print(out.name, f"{t:.1f} s, {len(segs)} shots")

if __name__ == "__main__":
    for h in sys.argv[1:] or ["h1", "h2", "h3"]: build(h)
