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

A = P / "assets/sfx"
AMB = {"clinic": A / "openverse_ad1363e8-b3e3-4229-9dad-_kitchen-room-tone.mp3", "bath": A / "openverse_71f883c5-e1bd-4efd-b158-_bathroom-tone-drone.mp3",
       "yard": A / "openverse_579a2093-ffe1-461a-bf85-_backyard-birds-001-wav.mp3", "room": A / "openverse_b14d236c-2f0b-4058-a3b1-_room-tone.mp3"}
SCENE = {"b02_clinic": "clinic", "b04_clinic_a": "clinic", "b03_bathroom": "bath", "b05_wart_back": "bath", "b05_wart_back_v2": "bath",
         "b06_dand_snap": "yard", "b07_dand_back": "yard", "b08_dand_water": "yard", "b09_dand_root": "yard", "b10_towels": "room",
         "b11_nightstand": "room", "b12_file": "room", "b13_brush": "room", "b14_dot": "room", "b15_lamp": "room", "b17_hallway": "room", "b18_dad": "room"}
FOLEY = [("b02_clinic", A / "hf_spray.mp3", 0.2, -12), ("b04_clinic_a", A / "hf_spray.mp3", 0.3, -12), ("b04_clinic_a", A / "hf_paper_crinkle.mp3", 0.6, -16),
         ("b08_dand_water", A / "hf_water_pour.mp3", 0.0, -14), ("b10_towels", A / "openverse_ebb7fa8b-b886-42ca-abe9-_paper-rustling-02-wav.mp3", 0.3, -20),
         ("b12_file", A / "openverse_b1072884-7370-4c04-99c6-_filingnails-wav.mp3", 0.2, -18), ("b15_lamp", A / "hf_lamp_click.mp3", 0.9, -10),
         ("b17_hallway", A / "hf_footsteps.mp3", 0.0, -14), ("b18_dad", A / "openverse_eb8cdbf2-1614-4244-95d1-_turning-pages-wav.mp3", 0.6, -20)]

def sound_design(pos):
    """Room tone/ambience under every silent AI shot + foley on the action: silent AI footage reads fake."""
    amb, fol, off = [], [], {}
    for note, (st, ln) in sorted(pos.items(), key=lambda kv: kv[1][0]):
        sc = SCENE.get(note)
        if not sc: continue
        gain = {"clinic": -30, "bath": -28, "yard": -24, "room": -32}[sc]
        o = off.get(sc, 0.0); off[sc] = o + ln
        amb.append({"file": str(AMB[sc]), "at": round(st, 3), "in": round(o % 25, 3), "dur": round(ln, 3), "gain_db": gain, "fade_in": 0.08, "fade_out": 0.08})
    for note, f, d, g in FOLEY:
        if note in pos:
            st, ln = pos[note]
            fol.append({"file": str(f), "at": round(st + d, 3), "in": 0.0, "dur": round(max(0.5, min(ln - d, 3.0)), 3), "gain_db": g, "fade_out": 0.15})
    return [{"name": "ambience", "gain_db": 0, "clips": amb}, {"name": "foley", "gain_db": 0, "clips": fol}]

GR = P / "assets/graphics"
def web_cards(pos):
    """Real AAD treatment-page lines (raw/web, captured 22 Nov) as phone screenshots over the failed-fixes beats."""
    plan = [("b03_bathroom", "w1_acid_card.png"), ("b04_clinic_a", "w2_freeze_card.png"),
            (next((k for k in pos if k.startswith("b05_wart_back")), "b05_wart_back"), "w3_repeat_card.png")]
    ovs = []
    for note, card in plan:
        if note not in pos: continue
        st, ln = pos[note]; e = st + ln - 0.1; a = max(st + 0.25, e - 3.0)  # land on the line, not the whole shot
        if e - a < 1.0: continue
        top = 150 if card.startswith("w3") else 330  # keep the wart (lower middle of b05) clear
        ovs.append({"file": str(GR / card), "start": round(a, 3), "end": round(e, 3), "w": 780, "x": 150,
                    "kf": {"y": [[0, top + 90], [0.28, top]]}, "fade_in": 0.18, "fade_out": 0.15})
    return ovs

def pick(new, old):  # use the Seedance 3D motion version when it has been downloaded
    return new if new.exists() else old

def build(hook):
    segs, vo, t = [], [], 0.0
    pos = {}  # note -> (output start, output length)
    def talk(name):  # lip-synced clip with its own audio
        nonlocal t
        s0, s1 = speech_window(C / f"{name}.mp4"); segs.append(seg(C / f"{name}.mp4", s0, s1, note=name)); pos[name] = (t, s1 - s0); t += s1 - s0
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
            pos[f.stem] = (t + out, d); out += d
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
    voiced("vo03.mp3", [(C / "b04_clinic_a.mp4", 0.0, 1), (C / ("b05_wart_back_v2.mp4" if (C / "b05_wart_back_v2.mp4").exists() else "b05_wart_back.mp4"), 0.2, 1)])
    talk("c04_reframe")
    voiced("vo05.mp3", [(C / "b06_dand_snap.mp4", 0.3, 2.2), (C / "b07_dand_back.mp4", 0.5, 1.6), (pick(C / "m1_frost.mp4", G / "g11_frost.mp4"), 0, 2.6),
                        (C / "b08_dand_water.mp4", 0.6, 1.4), (C / "b09_dand_root.mp4", 0.3, 2.0)])
    plants_at = t
    voiced("vo06.mp3", [(pick(C / "m2_soak.mp4", G / "g12a_team.mp4"), 0, 7.0), (C / "b10_towels.mp4", 0.2, 3.6), (pick(C / "m3_root.mp4", G / "g12b_team.mp4"), 0, 4.5)])
    towels_at = plants_at + (dur(V / "vo06.mp3") + BREATH) * 7.0 / 15.1
    voiced("vo07.mp3", [(C / "b11_nightstand.mp4", 0.0, 1)])
    voiced("vo08.mp3", [(C / "b12_file.mp4", 0.1, 3.6), (C / "b13_brush.mp4", 0.2, 4.6), (C / "b14_dot.mp4", 0.2, 3.5),
                        (C / "b15_lamp.mp4", 0.3, 3.0), (pick(C / "m4_night.mp4", G / "g19_clock.mp4"), 0, 2.4)])
    voiced("vo09.mp3", [(C / "b17_hallway.mp4", 0.0, 1)])
    testi_at = t
    talk("c16_mom1"); talk("c17_mom2")
    segs.append(seg(C / "b18_dad.mp4", 0.3, 3.0, mute=True, note="b18_dad")); pos["b18_dad"] = (t, 2.7); t += 2.7
    talk("c18_mom3"); testi_end = t
    voiced("vo10.mp3", [(G / "g26_stakes.mp4", 0, 1)])
    # urgency CTA (v3): mom to camera with the bottle, then the moving offer card and end card under music
    talk("c19_cta")
    segs.append(seg(G / "g27b_offer_cta.mp4", 0, 4.2, mute=True, note="offer card")); pos["offer card"] = (t, 4.2); t += 4.2
    segs.append(seg(G / "g28b_end_cta.mp4", 0, 3.0, mute=True, note="end card")); t += 3.0

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
        ],
        "blurs": [{"start": round(hook_end - (dur(V / ('vo01.mp3' if hook == 'h1' else 'vo13.mp3' if hook == 'h2' else 'vo15.mp3')) + BREATH), 2),
                   "end": round(hook_end, 2), "x": 0.33, "y": 0.22, "w": 0.4, "h": 0.2, "mode": "blur", "strength": 30}],
        "overlays": web_cards(pos),
        "tracks": [{"name": "vo", "gain_db": 0, "clips": vo}] + sound_design(pos),
        "music": {"file": str(P / f"work/music_fit_{hook}.wav"), "gain_db": -22, "duck": True, "start": 0, "fade_out": 0.01},
        "audio": {"enhance": False},
    }
    out = P / "work/ads" / f"set1_{hook}.edl.json"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(edl, indent=1)); print(out.name, f"{t:.1f} s, {len(segs)} shots")

if __name__ == "__main__":
    for h in sys.argv[1:] or ["h1", "h2", "h3"]: build(h)
