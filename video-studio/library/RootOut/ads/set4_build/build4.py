#!/usr/bin/env python3
"""Build RootOut Set 4 (H1/H2/H3): cut-away scenes timed to the spoken words, mom keyed over them, inserts,
real b-roll, web cards, VO, sound bed, captions -> EDL for `vs render`.
build4.py prep            transcribe every clip (word times) into work/tx_clips/
build4.py scenes h1 [..]  render the cut-away scenes + mom composites needed
build4.py edl h1 [..]     write work/ads/set4_<hook>.edl.json"""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cutaway

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
B = Path(__file__).resolve().parent
VS = "/home/user/video-studio-claude-plugin/plugins/video-studio/bin/vs"
C, V, G, CW, CMP = P / "raw/gen/clips", P / "raw/gen/vo", P / "work/gfx", P / "work/cutaway", P / "work/comp"
BR = P / "raw/broll"  # real internet footage picked for this set (see library BROLL_PICKS.md)
BREATH = 0.22
MOM = {"m01": ("m01_h1b", "h1"), "m02": ("m02_h2", "h2b"), "m03": ("m03_h3", "h3"), "m04": ("m04_tape", "v01a"),
       "m05": ("m05_pad", "v02a"), "m06": ("m06_can", "v03a"), "m07": ("m07_agon", "v03c"), "m08": ("m08_nobody", "v05a"),
       "m09": ("m09_fault", "v05c"), "m10": ("m10_bottle", "v06a"), "m11": ("m11_together", "v06c"), "m12": ("m12_safe", "v07a"),
       "m13": ("m13_cap", "v08b"), "m14": ("m14_skip", "v10a")}
PL = {"1": {"slot": 1, "present": 1}, "2": {"slot": 2, "present": 1}, "3": {"slot": 3, "present": 1}, "4": {"slot": 4, "present": 1}}

def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)

def words(f):
    tx = P / "work/tx_clips" / f"{Path(f).stem}.json"
    if not tx.exists():
        tx.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([VS, "transcribe", str(f), "-o", str(tx.with_suffix("")), "--model", "small.en"], capture_output=True)
    return json.loads(tx.read_text())["words"]

def window(f):
    w = words(f); return max(0.0, w[0]["s"] - 0.10), min(dur(f), w[-1]["e"] + 0.22)

def at(f, text, nth=1, edge="s"):
    """time (s, from the clip start) of the nth word that starts with `text` (case-insensitive)."""
    k = 0
    for w in words(f):
        if w["w"].lower().strip(",.!?'\"").startswith(text.lower()):
            k += 1
            if k == nth: return w[edge]
    raise KeyError(f"{text} not in {f}")

def pins(*ks, **over):
    d = {k: dict(PL[k]) for k in ks}; d.update(over); return d

# ------------------------------------------------------------------ the plan
def plan(hook):
    """List of beats. ("mom", key, scene) | ("vo", vo_id, [shots]) | ("gfx", file, seconds)
    shot = (kind, src_or_scene, weight[, opts]); kind in clip|broll|cut|gfx. Scene times are from the beat start."""
    m = lambda k: C / f"{MOM[k][0]}.mp4"
    def rel(k, word, nth=1):  # word time relative to the speech window start
        f = m(k)
        if not f.exists(): return 0.5
        try: return at(f, word, nth) - window(f)[0]
        except KeyError: return 0.5
    beats = []
    if hook == "h1":
        beats.append(("mom", "m01", {"slots_glow": rel("m01", "four"), "blink_slot4": rel("m01", "number"), "pins": {}}))
    elif hook == "h2":
        beats.append(("vo", "h2a", [("clip", C / "i01_shelf.mp4", 1), ("clip", C / "i02_cluster.mp4", 1)]))
        # m02's hand shows three fingers on "four": keep her for "Only number", then the cut-away with slot 4 blinking
        cut = rel("m02", "four") - 0.05
        mom_comp("m02", {"slots_glow": 0.0, "pins": {}})
        beats.append(("vo", "h2b", [("clip", CMP / "m02_h2.mp4", cut, {"in": 0.0}),
                                    ("cut", {"slots_glow": -1, "blink_slot4": 0.0, "pins": {}, "board": 1}, 2.41 - cut)]))
    else:
        beats.append(("mom", "m03", {"tomb_at": 0.15, "tomb_x": 770, "pins": {}}))
    beats += [
        ("mom", "m04", {"chip": "#1  Duct tape", "chip_in": 0, "pins": {"1": {"slot": 1, "drop_at": rel("m04", "sits")}}}),
        ("vo", "v01b", [("cut", {"chip": "#1  Duct tape", "pins": pins("1"), "tape_at": 0.1}, 1.7, {"card": "w_tape"}),
                        ("gfx", G / "s_tape.mp4", 1.0)]),
        ("mom", "m05", {"chip": "#2  Acid pads", "chip_in": 0, "pins": {**pins("1"), "2": {"slot": 2, "drop_at": rel("m05", "stronger")}}}),
        ("vo", "v02b", [("clip", C / "i04_pad.mp4", 1.0), ("gfx", G / "s_acid.mp4", 0.8), ("cut", {"chip": "#2  Acid pads", "pins": pins("1", "2"), "dots_fade": 0.0, "regrow": [0.05, 1.3]}, 1.1, {"card": "w_acid"})]),
        ("mom", "m06", {"chip": "#3  Freezing", "chip_in": 0, "pins": {**pins("1", "2"), "3": {"slot": 3, "drop_at": rel("m06", "strongest")}}}),
        ("vo", "v03b", [("clip", C / "i05_exam.mp4", 1.0, {"in": 0.2, "card": "w_freeze", "seg": {"zoom": 1.3, "focus": [0.45, 0.75]}}), ("gfx", G / "s_freeze.mp4", 0.8)]),
        ("mom", "m07", {"chip": "#3  Freezing", "pins": pins("1", "2", "3")}),
        ("vo", "v03d", [("cut", {"chip": "#3  Freezing", "pins": pins("1", "2", "3"), "bumps3_at": 1.6}, 1.0, {"card": "w_cryo"})]),
        ("mom", "m08", {"pins": pins("1", "2", "3"), "bumps3": 1}),
        ("vo", "v05b", [("cut", {"pins": pins("1", "2", "3"), "bumps3": 1, "zoom": [0.05, 0.8, 2.6], "board": 1}, 0.9),
                        ("gfx", G / "s_dand_dry.mp4", 1.4), ("broll", "dand_snap", 1.8), ("gfx", G / "s_stem.mp4", 1.2),
                        ("gfx", G / "s_dand_root.mp4", 2.0), ("gfx", G / "s_dand_back.mp4", 1.5),
                        ("cut", {"pins": pins("1", "2", "3"), "bumps3": 1, "root_glow": 0.0, "board": 1}, 1.2)]),
        ("mom", "m09", {"pins": pins("1", "2", "3"), "bumps3": 1, "root_glow": 0.0}),
        ("mom", "m10", {"chip": "#4  RootOut", "chip_in": 0, "pins": pins("1", "2", "3"), "bumps3": 1, "slots_glow": 0.0, "blink_slot4": 0.4}),
        ("vo", "v06b", [("clip", C / "i07_clay_lemon.mp4", 1.25), ("clip", C / "i08_clay_tea.mp4", 1.0),
                        ("cut", {"chip": "#4  RootOut", "pins": pins("1", "2", "3"), "bumps3": 1, "cream_at": 0.0, "fill8x": [0.1, 1.5], "board": 1}, 0.85, {"dagger": 1}),
                        ("clip", C / "i06_towels.mp4", 0.6, {"in": 2.2, "label": "AI placeholder"}), ("clip", C / "i09_clay_root.mp4", 1.25, {"homeo": 1})]),
        ("mom", "m11", {"chip": "#4  RootOut", "pins": {**pins("1", "2", "3"), "4": {"slot": 4, "drop_at": rel("m11", "together"), "drop_dur": 0.9}}, "bumps3": 1, "fill8x": [-2, -1]}),
        ("mom", "m12", {"pins": pins("1", "2", "3", "4"), "bumps3": 1, "fill8x": [-2, -1]}),
        ("vo", "v07b", [("clip", C / "i10_toes.mp4", 1.0, {"in": 0.2}), ("cut", {"pins": pins("1", "2", "3", "4"), "bumps3": 1, "board": 1}, 1.0)]),
        # File / Soak / Cover = the brand's own how-to macro (real footage, site video), cut to the words
        ("vo", "v08a", [("clip", C / "i11_file.mp4", 2.7, {"in": 0.2}), ("gfx", G / "g_howto.mp4", 4.8, {"in": 0.0, "out": 2.15}),
                        ("gfx", G / "g_howto.mp4", 2.45, {"in": 2.15, "out": 4.7}), ("gfx", G / "g_howto.mp4", 2.55, {"in": 4.7, "out": 7.1}),
                        ("clip", C / "i14_lamp.mp4", 1.75, {"in": 0.6})]),
        ("mom", "m13", {"pins": pins("1", "2", "3", "4"), "bumps3": 1, "clock": [0.0, 2.6]}),
        ("vo", "v09", [("gfx", G / "g_calendar.mp4", 1.0), ("cut", {"pins": pins("4"), "bumps3": 1, "smooth_at": 0.4, "board": 1, "board_all": 1}, 1.0)]),
        ("mom", "m14", {"pins": {**{k: {"slot": int(k), "drop_at": rel("m14", "stuck") + 0.1 * i, "flick_at": rel("m14", "skip") + 0.12 * i} for i, k in enumerate("123")}, "4": dict(PL["4"])},
                        "smooth_at": -5}),
        ("vo", "v10b", [("clip", C / "i16_bottles.mp4", 1.0), ("gfx", G / "g_offer.mp4", 1.4)]),
        ("gfx", G / "g_end.mp4", 3.2),
    ]
    return beats

BROLL = json.loads((B / "broll_map.json").read_text()) if (B / "broll_map.json").exists() else {}

# ------------------------------------------------------------------ rendering scenes + composites
HITS = []
def scene_hits(sc, t0):
    """Sound hits for the events in a cut-away scene that starts at t0 on the edit clock."""
    for k, p in sc.get("pins", {}).items():
        if p.get("drop_at") is not None: HITS.append(("gold" if k == "4" else "pin", t0 + p["drop_at"] + p.get("drop_dur", 0.55) * 0.92, -8))
        if p.get("flick_at") is not None: HITS.append(("flick", t0 + p["flick_at"], -10))
    for ev, nm, g in (("tomb_at", "pop", -8), ("bumps3_at", "pop", -10), ("tape_at", "tape", -12), ("chip_in", "chip", -16), ("cream_at", "pop", -14)):
        if sc.get(ev) is not None and sc[ev] >= 0: HITS.append((nm, t0 + sc[ev], g))
    if sc.get("fill8x") and sc["fill8x"][0] >= 0: HITS.append(("rise", t0 + sc["fill8x"][0], -14))
    if sc.get("smooth_at") is not None and sc["smooth_at"] >= 0: HITS.append(("shine", t0 + sc["smooth_at"], -12))
    if sc.get("zoom"): HITS.append(("whoosh", t0 + sc["zoom"][0], -10))
CLIP_FOLEY = {"i05_exam": [("spray", 0.6, -10)], "i14_lamp": [("lamp", 0.8, -8)], "i11_file": [("file", 0.3, -14)], "i03_tape": [("tape", 0.4, -12)],
              "i04_pad": [("peel", 0.3, -14)], "g_calendar": [("marker", 0.5, -16)], "g_offer": [("pop", 0.3, -12)], "i12_brush": [("brush", 0.3, -16)]}

def scene_file(name, sc, d):
    out = CW / f"{name}.mp4"; sc = dict(sc, dur=round(d, 3))
    key = CW / f"{name}.json"
    if out.exists() and key.exists() and json.loads(key.read_text()) == sc: return out
    cutaway.render(sc, out); key.write_text(json.dumps(sc)); return out

GEOM = {"m07_agon": (0.46, 292, 1090), "m08_nobody": (0.46, 292, 1090)}  # Seedance zoomed in on these: shrink to match the others
def mom_comp(k, sc):
    f = C / f"{MOM[k][0]}.mp4"; s0, s1 = window(f); name = f"{MOM[k][0]}"
    sc_, gx, gy = GEOM.get(name, (0.78, 119, 740))
    bg = scene_file(f"bg_{name}", sc, s1 - s0)
    out = CMP / f"{name}.mp4"; CMP.mkdir(parents=True, exist_ok=True)
    stamp = CMP / f"{name}.stamp"; sig = json.dumps([sc, s0, s1, bg.stat().st_mtime, GEOM.get(name)])
    if not out.exists() or not stamp.exists() or stamp.read_text() != sig:
        subprocess.run([sys.executable, str(B / "composite.py"), str(f), str(bg), str(out), "--ss", f"{s0:.3f}", "--to", f"{s1:.3f}",
                        "--y", str(gy), "--x", str(gx), "--scale", str(sc_)], check=True)
        stamp.write_text(sig)
    return out, s1 - s0

# ------------------------------------------------------------------ EDL
def seg(src, start, end, **kw): return {"src": str(src), "start": round(start, 3), "end": round(end, 3), **kw}

def build(hook, render_only=False):
    segs, vo, ovs, texts, t = [], [], [], [], 0.0
    HITS.clear()
    pos = []  # (kind, name, start, length)
    for bi, beat in enumerate(plan(hook)):
        kind = beat[0]
        if kind == "mom" and render_only and not (C / f"{MOM[beat[1]][0]}.mp4").exists():
            continue
        if kind == "mom":
            out, L = mom_comp(beat[1], beat[2]); scene_hits(beat[2], t)
            segs.append(seg(out, 0, L, note=beat[1])); pos.append(("mom", beat[1], t, L)); t += L
        elif kind == "gfx":
            for nm, off, g in CLIP_FOLEY.get(Path(beat[1]).stem, []): HITS.append((nm, t + off, g))
            segs.append(seg(beat[1], 0, beat[2], mute=True, note=beat[1].stem)); pos.append(("gfx", beat[1].stem, t, beat[2])); t += beat[2]
        else:
            vid, shots = beat[1], beat[2]
            L = dur(V / f"{vid}.mp3") + BREATH; vo.append({"file": str(V / f"{vid}.mp3"), "at": round(t + 0.06, 3)})
            if not render_only: shots = [s for s in shots if s[0] != "broll" or s[1] in BROLL] or [("cut", {"pins": {}}, 1)]
            tot = sum(s[2] for s in shots); used = 0.0
            for j, s in enumerate(shots):
                d = L * s[2] / tot if j < len(shots) - 1 else L - used
                opts = s[3] if len(s) > 3 else {}
                if s[0] == "cut":
                    f = scene_file(f"vo_{hook}_{vid}_{j}", s[1], d); segs.append(seg(f, 0, d, mute=True, note=f"cut {vid}")); scene_hits(s[1], t + used)
                    if opts.get("card"): ovs.append(card_overlay(opts["card"], t + used, d))
                    if opts.get("dagger"): texts.append(small("†Based on our manufacturer's absorption testing against a regular cream.", t + used, t + used + d, pos="center"))
                else:
                    if render_only:
                        used += d; continue
                    if s[0] == "broll":
                        b = BROLL[s[1]]; f, a = P / b["file"], float(b.get("in", 0))
                    elif s[0] == "gfx":
                        f, a = s[1], float(opts.get("in", 0.0))
                    else:
                        f, a = s[1], float(opts.get("in", 0.3))
                    avail = (float(opts["out"]) if "out" in opts else dur(f)) - a
                    ex = {**(BROLL[s[1]].get("seg", {}) if s[0] == "broll" else {}), **opts.get("seg", {})}
                    if d > avail: segs.append(seg(f, a, a + avail, mute=True, speed=round(max(avail / d, 0.42), 3), note=f.stem, **ex))
                    else: segs.append(seg(f, a, a + d, mute=True, note=f.stem, **ex))
                    if opts.get("card"): ovs.append(card_overlay(opts["card"], t + used, d))
                    if opts.get("label"): texts.append(small(opts["label"], t + used, t + used + d, pos="top"))
                    if opts.get("homeo"): texts.append(small("*Homeopathic claims are based on traditional homeopathic practice, not accepted medical evidence,\nand are not FDA evaluated. Results vary.", t + used, t + used + d, pos="center"))
                    for nm, off, g in CLIP_FOLEY.get(Path(f).stem, []): HITS.append((nm, t + used + off, g))
                pos.append((s[0], f"{vid}:{j}", t + used, d)); used += d
            t += L
    if render_only: return
    hook_txt = {"h1": "Every wart fix, ranked", "h2": "One wart turned into fifteen.", "h3": "R.I.P. your kid's wart"}[hook]
    texts.insert(0, {"text": hook_txt, "start": 0.0, "end": 3.4, "pos": "top", "size": 0.058, "anim": "pop", "color": "#FFFFFF",
                     "box": "#0B2A5B", "font": "Inter", "bold": True})
    edl = {"segments": segs, "grade": "natural", "texts": texts, "overlays": ovs,
           "tracks": [{"name": "vo", "gain_db": 0, "clips": vo}] + sound_bed(pos),
           "music": {"file": str(P / f"work/music_fit_{hook}.wav"), "gain_db": -23, "duck": True, "start": 0, "fade_out": 0.01},
           "audio": {"enhance": False}}
    mus = P / f"work/music_fit_{hook}.wav"  # "Life of Riley" (Kevin MacLeod, CC BY 4.0) trimmed to the edit, fades under the end card
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", str(P / "assets/music/Life_of_Riley.mp3"), "-t", f"{t:.3f}",
                    "-af", f"afade=t=in:d=0.4,afade=t=out:st={max(t - 2.2, 0):.3f}:d=2.2", "-ar", "48000", str(mus)], check=True)
    out = P / "work/ads" / f"set4_{hook}.edl.json"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(edl, indent=1)); (P / "work/ads" / f"set4_{hook}.pos.json").write_text(json.dumps(pos))
    print(out.name, f"{t:.1f} s, {len(segs)} shots")

def small(text, a, b, pos="bottom"):
    return {"text": text, "start": round(a, 2), "end": round(b, 2), "pos": pos, "size": 0.022, "color": "#FFFFFF", "box": "#00000080", "anim": "none"}

def card_overlay(name, start, d):
    f = P / "assets/graphics" / f"{name}_card.png"
    if not f.exists(): return {"file": str(P / "assets/graphics/blank.png"), "start": round(start, 3), "end": round(start + 0.01, 3), "w": 1, "x": 0, "y": 0}
    a = start + 0.15; e = start + d - 0.05
    return {"file": str(f), "start": round(a, 3), "end": round(e, 3), "w": 860, "x": 110, "kf": {"y": [[0, 1200], [0.3, 1110]]}, "fade_in": 0.18, "fade_out": 0.12}

SFX = P / "assets/sfx"
def sound_bed(pos):
    """Room tone under every scene + pin-drop ticks; files from work/sfx_map.json (name -> file, gain)."""
    mp = json.loads((P / "work/sfx_map.json").read_text()) if (P / "work/sfx_map.json").exists() else {}
    amb, fol = [], []
    for kind, name, st, ln in pos:
        if kind in ("clip", "broll", "mom") and mp.get("room"):
            amb.append({"file": mp["room"], "at": round(st, 3), "in": round(st % 20, 3), "dur": round(ln, 3), "gain_db": -30, "fade_in": 0.05, "fade_out": 0.05})
    for name, at_s, g in HITS:
        if mp.get(name): fol.append({"file": mp[name], "at": round(at_s, 3), "in": 0, "dur": 2.0, "gain_db": g, "fade_out": 0.1})
    return [{"name": "ambience", "gain_db": 0, "clips": amb}, {"name": "foley", "gain_db": 0, "clips": fol}]

if __name__ == "__main__":
    cmd, hooks = sys.argv[1], sys.argv[2:] or ["h1", "h2", "h3"]
    if cmd == "prep":
        for k, (n, _) in MOM.items():
            if (C / f"{n}.mp4").exists(): print(n, window(C / f"{n}.mp4"))
    elif cmd == "scenes":
        for h in hooks: build(h, render_only=True)
    else:
        for h in hooks: build(h)
