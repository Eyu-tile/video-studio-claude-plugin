#!/usr/bin/env python3
"""Set 4 v2 edit: one picture per spoken phrase (≤3 s), VO-led, cut times taken from the ElevenLabs word timings.
Mom clips are lip-synced to the same VO lines, so their picture is placed by cross-correlating their audio with the line.
build_v2.py h1 [h2 h3]  -> projects/rootout-set4/v2/edl/set4v2_<hook>.edl.json"""
import difflib, json, subprocess, sys
from pathlib import Path
import numpy as np
B = Path(__file__).resolve().parent; sys.path.insert(0, str(B.parent))
from check_script import norm
from check_clips import n2

P = Path("/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4")
V2, VO, TX = P / "v2", P / "raw/gen/vo", P / "work/tx"
C2, C1, G1, GX = V2 / "clips", P / "raw/gen/clips", P / "work/gfx", V2 / "gfx"
BREATH, LEAD = 0.22, 0.06
L = {l["id"]: l for l in json.loads((B.parent / "SCRIPT_LOCK.json").read_text())["lines"]}
BODY = ["v01a", "v01b", "v02a", "v02b", "v03a", "v03b", "v03c", "v03d", "v05a", "v05b", "v05c", "v06a", "v06b", "v06c",
        "v07a", "v07b", "v08a", "v08b", "v09", "v10a", "v10b"]
HOOKS = {"h1": ["h1"], "h2": ["h2a", "h2b"], "h3": ["h3"]}
MOMLINE = {"M1_h1": "h1", "M2_car": "v03c", "M3_nobody": "v05a", "M4r_fault": "v05c", "M5r_bottle": "v06a", "M6_safe": "v07a",
           "M7_cap": "v08b", "M8_sofa": "v10a", "M9_h2b": "h2b", "M10_h3": "h3"}

def c2(n, **o): return ("clip", C2 / f"{n}.mp4", o)
def c1(n, **o): return ("clip", C1 / f"{n}.mp4", o)
def g1(n, **o): return ("clip", G1 / f"{n}.mp4", o)
def gx(n, **o): return ("clip", GX / f"{n}.mp4", o)
def mom(n, **o): return ("mom", n, o)
PUSH, PULL = {"push": 1.07}, {"pull": 1.07}

# (phrase, picture, overlays)  overlays: png names from v2/gfx (placed by OV), or ("text", ...) small disclaimers
HOOK_SHOTS = {
 "h1": [("There are only", mom("M1_h1"), []),
        ("four ways to get rid of a kid's wart,", c2("P1_lineup", in_=0.2), []),
        ("ranked from weakest", c2("B1_lineup", in_=0.3, **PUSH), []),
        ("to strongest.", c2("P2_slidein", in_=0.6), []),
        ("Most families never make it to number four.", mom("M1_h1"), [])],
 "h2": [("One wart turned into fifteen.", c1("i02_cluster", in_=0.3, **PUSH), []),
        ("So here's every fix we tried,", c1("i01_shelf", in_=0.3, **PULL), []),
        ("ranked from weakest", c2("B1_lineup", in_=0.3, **PUSH), []),
        ("to strongest.", c2("P2_slidein", in_=0.6), []),
        ("Only number four got the root.", mom("M9_h2b"), [])],
 "h3": [("R.I.P., my kid's wart.", gx("tombstone", in_=0.0), []),
        ("You will not be missed.", mom("M10_h3"), []),
        ("Here's every fix we tried,", c2("P1_lineup", in_=0.2), []),
        ("ranked from weakest", c2("B1_lineup", in_=0.3, **PUSH), []),
        ("to strongest.", c2("P2_slidein", in_=0.6), [])],
}
DAG = "†Based on our manufacturer's absorption testing against a regular cream."
HOMEO = "*Homeopathic claims are based on traditional homeopathic practice, not accepted medical evidence, and are not FDA evaluated. Results vary."
BODY_SHOTS = [
 ("Number one,", g1("s_tape"), ["rank1"]),
 ("duct tape.", c2("K_test_tape", in_=0.3), ["rank1"]),
 ("It sits on top of the wart for weeks.", c2("B3_tapefoot", in_=0.2, **PUSH), []),
 ("Rent free.", c2("B4_sock", in_=0.3), []),
 ("It never gets under the hard skin.", c2("D1_tape3d", in_=0.3), ["card:w_tape"]),
 ("Number two,", c2("B5_pads", in_=0.2, **PUSH), ["rank2"]),
 ("acid pads.", c2("B6_padpress", in_=0.2), ["rank2"]),
 ("A bit stronger.", c2("B6_padpress", in_=2.0), []),
 ("They peel it down", c1("i04_pad", in_=0.3), []),
 ("till the black dots are gone.", g1("s_acid"), []),
 ("And it always seems to come back.", c2("B5_pads", in_=2.0, **PULL), ["card:w_acid"]),
 ("Number three,", c2("B7_vapour", in_=0.2), ["rank3"]),
 ("freezing at the doctor's.", c1("i05_exam", in_=0.2, zoom=1.3, focus=[0.45, 0.75]), ["rank3"]),
 ("The strongest one most of us know.", g1("s_freeze"), ["card:w_freeze"]),
 ("Somebody held him still every time.", c2("B8_holdankle", in_=0.2, **PUSH), []),
 ("It was agonizing for all of us.", mom("M2_car"), []),
 ("And after every visit,", c2("B9_carpark", in_=0.2), []),
 ("there were two or three more.", c2("B10_threewarts", in_=0.2, **PUSH), ["card:w_cryo"]),
 ("Here's what nobody told me.", mom("M3_nobody"), []),
 ("Freezing,", c2("D2_toponly", in_=0.0), []),
 ("acid and shaving", c2("D2_toponly", in_=2.2), []),
 ("only snap off the top,", ("clip", P / "assets/broll/archive_deathtow1947_death-to-weeds_1146.00-1156.50.mp4", {"in_": 4.6, "fit": "blur"}), []),
 ("like picking a dandelion.", c2("B11_snap", in_=0.3), []),
 ("The root stays under the hard skin,", c2("B12_soilbox", in_=0.2, **PUSH), []),
 ("so it grows back.", g1("s_dand_back"), []),
 ("Every fix made it look done,", c2("B13_thumbrub", in_=0.2), []),
 ("but the root never left.", c2("D3_rootstill", in_=1.2, **PUSH), []),
 ("It was never our fault.", mom("M4r_fault"), []),
 ("Number four", c2("P3_hero", in_=0.2, **PUSH), ["rank4"]),
 ("gets the root.", g1("s_dand_root"), ["rank4"]),
 ("It's RootOut, an oil with four plants,", mom("M5r_bottle"), []),
 ("and each one takes it a little deeper.", c2("P4_flatlay", in_=0.3, **PUSH), []),
 ("Lemon goes first", c2("B14_lemon", in_=0.2), ["lab_lemon"]),
 ("and softens the hard top.", c2("D4_lemon3d", in_=0.6), []),
 ("Tea tree is a thin oil,", c2("B15_teatree", in_=0.2), ["lab_tea"]),
 ("so it sinks right in,", c2("D5_sink", in_=0.6), []),
 ("up to 8x deeper than a regular cream,", c1("i06_towels", in_=0.3), ["x8", "aiph", ("text", DAG)]),
 ("and it carries the last two plants", c2("D6_carry", in_=0.0), []),
 ("down with it.", c2("D6_carry", in_=2.0), []),
 ("Pokeweed and white cedar break the wart down from the", c2("B16_pokeweed", in_=0.2, **PUSH), ["lab_poke"]),
 ("root, so there's nothing left to grow back.", c2("D7_crumble", in_=0.6), [("text", HOMEO)]),
 ("Any one of them alone", c2("D8_together", in_=0.0), []),
 ("stops halfway.", c2("D8_together", in_=1.4), []),
 ("Together, they reach the root.", c2("D8_together", in_=2.4), []),
 ("And deep doesn't mean harsh.", mom("M6_safe"), []),
 ("It's a kids' formula,", c2("P5_nightbook", in_=0.4, **PUSH), []),
 ("for ages 4 and up.", mom("M6_safe"), []),
 ("No acid,", c2("B17_bin", in_=0.2), ["x_acid"]),
 ("no freezing,", c2("B17_bin", in_=2.0), ["x_freeze"]),
 ("no blister.", c2("B18_smoothsole", in_=0.2), ["x_blister"]),
 ("Just a little cool tingle.", c1("i10_toes", in_=0.2), []),
 ("And pediatricians recommend it.", c2("P6_clinicdesk", in_=0.6, **PUSH), []),
 ("At bedtime, it's three steps.", c2("P7_nightkit", in_=0.5), []),
 ("File:", g1("g_howto", in_=0.0, out=2.15), []),
 ("rub the little file over it twice,", c1("i11_file", in_=0.2), ["step1"]),
 ("just on the hard top.", g1("g_howto", in_=1.0, out=2.15), []),
 ("Soak: brush the oil on.", g1("g_howto", in_=2.15, out=4.7), []),
 ("Cover: a clear dot on top,", g1("g_howto", in_=4.7, out=7.1), []),
 ("so it soaks all night.", c2("P8_timelapse", in_=0.0), ["night"]),
 ("He's asleep before I put the cap back on.", mom("M7_cap"), []),
 ("Most spots, on a hand or a foot,", c2("B19r_handfoot", in_=0.2), []),
 ("are gone in about two weeks.", g1("g_calendar", in_=0.0), []),
 ("Then you do fourteen more nights,", c2("B20_plus14", in_=0.3), ["plus14"]),
 ("so the root is gone too.", c2("D9_clean", in_=2.4), []),
 ("Nobody gets held down,", c2("B21_hallway", in_=0.2), []),
 ("and there's nothing to book.", gx("phone_delete", in_=0.0), []),
 ("If your kid's wart keeps coming back,", mom("M8_sofa"), []),
 ("you've been stuck at number three.", c2("B23_drawer", in_=0.2), []),
 ("Skip to number four.", c2("P3_hero", in_=2.0, **PUSH), ["rank4"]),
 ("It's at the link below.", c2("R_pdp_scroll", in_=0.0), ["link"]),
 ("Three for the price of two.", c1("i16_bottles", in_=0.3), ["b2g1"]),
 ("And if it's not gone, you get your money back.", gx("offer", in_=0.0), []),
]
END = 3.2
# overlay placement (top-left on 1080x1920; every box sits inside x 65–918, y 230–1344)
OV = {"rank": (54, 214), "lab": "top", "x": "top", "step": "top", "night": "top", "plus14": "top", "b2g1": "top", "link": "top", "x8": "top", "aiph": (40, 1090)}

def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)

def pcm(f, sr=8000, ss=0, t=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(ss)] + (["-t", str(t)] if t else []) + ["-i", str(f), "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32)

def env(x, sr=8000, hop=80):
    n = len(x) // hop; e = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)); return (e - e.mean()) / (e.std() + 1e-9)

_off = {}
def mom_offset(clip, t0, t1):
    """seconds to add to a VO-line time to land on the same moment in the mom clip: median over the words spoken
    between t0 and t1 (line-relative), matched by whisper in both files (Seedance drifts a little inside a clip)."""
    import statistics
    a = json.loads((V2 / "tx" / f"{clip}.json").read_text())["words"]; b = json.loads((TX / f"{MOMLINE[clip]}.json").read_text())["words"]
    k = lambda w: w["w"].lower().strip(".,!?")
    sm = difflib.SequenceMatcher(a=[k(w) for w in a], b=[k(w) for w in b], autojunk=False)
    pairs = [(a[i]["s"] - b[j]["s"], b[j]["s"]) for o, a0, a1, b0, b1 in sm.get_opcodes() if o == "equal" for i, j in zip(range(a0, a1), range(b0, b1))]
    pairs = [p for p in pairs if p[1] > 0.05] or pairs  # whisper pins the first word to 0.0
    inside = [d for d, t in pairs if t0 - 0.05 <= t <= t1] or [d for d, t in pairs]
    off = statistics.median(inside); _off.setdefault(clip, []).append(round(off, 2)); return off

def word_times(lines):
    """script tokens of the given lines with absolute start times on the edit clock (lines laid end to end + BREATH)."""
    toks, t = [], 0.0; starts = {}
    for lid in lines:
        starts[lid] = t
        W = json.loads((TX / f"{lid}.json").read_text())["words"]; st = L[lid]["text"].split()
        key = lambda s: "".join(n2(norm(s))) or s.lower()
        sm = difflib.SequenceMatcher(a=[key(w["w"]) for w in W], b=[key(s) for s in st], autojunk=False)
        tt = [None] * len(st)
        for op, a0, a1, b0, b1 in sm.get_opcodes():
            if op == "equal":
                for i, j in zip(range(a0, a1), range(b0, b1)): tt[j] = W[i]["s"]
            elif op == "replace":
                for k, j in enumerate(range(b0, b1)): tt[j] = W[a0]["s"] + (W[a1 - 1]["e"] - W[a0]["s"]) * k / (b1 - b0)
        for j in range(len(st)):
            if tt[j] is None: tt[j] = tt[j - 1] + 0.2 if j else 0.0
            toks.append((st[j], t + LEAD + tt[j], lid))
        t += dur(VO / f"{lid}.mp3") + BREATH
    return toks, starts, t

def ov_png(name, a, b):
    from PIL import Image
    w, h = Image.open(GX / f"{name}.png").size
    kind = next((k for k in OV if name.startswith(k)), None); pos = OV.get(kind, "top")
    if pos == "top": x, y = 491 - w // 2, 236
    elif pos == "low": x, y = 491 - w // 2, 1150
    else: x, y = pos
    if kind in ("rank",) : y = 214
    return {"file": str(GX / f"{name}.png"), "start": round(a + 0.04, 3), "end": round(b, 3), "w": w, "x": x,
            "kf": {"y": [[0, y + 26], [0.22, y]]}, "fade_in": 0.16, "fade_out": 0.1}

def card(name, a, b):
    from PIL import Image
    f = GX / f"src_{name}.png"; w, h = Image.open(f).size
    return {"file": str(f), "start": round(a + 0.12, 3), "end": round(b - 0.04, 3), "w": w, "x": 491 - w // 2, "kf": {"y": [[0, 470], [0.3, 410]]}, "fade_in": 0.16, "fade_out": 0.12}

def small(text, a, b): return {"text": text, "start": round(a, 2), "end": round(b, 2), "pos": "center", "size": 0.025, "color": "#FFFFFF", "box": "#00000080", "anim": "none"}

def build(hook):
    lines = HOOKS[hook] + BODY; toks, starts, t_end = word_times(lines)
    shots = HOOK_SHOTS[hook] + BODY_SHOTS
    # map each phrase to its first token
    k, cuts = 0, []
    key = lambda s: "".join(n2(norm(s)))
    for ph, pic, ovs in shots:
        pt = ph.split()
        got = [key(x[0]) for x in toks[k:k + len(pt)]]
        assert got == [key(x) for x in pt], f"phrase mismatch at '{ph}': script has {' '.join(x[0] for x in toks[k:k + len(pt)])}"
        cuts.append(toks[k][1] - LEAD - 0.04 if k else 0.0); k += len(pt)
    assert k == len(toks), f"{len(toks) - k} script words not covered by shots"
    vo_end = t_end
    bounds = cuts + [vo_end]
    segs, ovl, texts, pos = [], [], [], []
    for i, (ph, pic, ovs) in enumerate(shots):
        a, b = bounds[i], bounds[i + 1]; d = b - a
        kind, src, o = pic; o = dict(o)
        if kind == "mom":
            lid = MOMLINE[src]; f = C2 / f"{src}.mp4"
            off = mom_offset(src, a - starts[lid], b - starts[lid] - LEAD)
            s0 = a - starts[lid] - LEAD + off
            if s0 < 0: s0 = 0.0
            s1 = min(s0 + d, dur(f)); seg = {"src": str(f), "start": round(s0, 3), "end": round(s1, 3), "mute": True, "note": f"{src} ({ph[:24]})"}
            if s1 - s0 < d - 0.02: seg["speed"] = round((s1 - s0) / d, 3)
        else:
            f = src; s0 = float(o.pop("in_", 0.3)); end = float(o.pop("out", dur(f)))
            push, pull = o.pop("push", None), o.pop("pull", None)
            avail = end - s0
            seg = {"src": str(f), "start": round(s0, 3), "end": round(min(end, s0 + d), 3), "mute": True, "note": f"{Path(f).stem} ({ph[:24]})", **o}
            if avail < d: seg["speed"] = round(max(avail / d, 0.5), 3); seg["end"] = round(s0 + min(avail, d * seg["speed"]), 3)
            z0 = float(o.get("zoom", 1.0))
            if push: seg["kf"] = {"zoom": [[0, z0], [round(d, 3), round(z0 * push, 3)]]}
            if pull: seg["kf"] = {"zoom": [[0, round(z0 * pull, 3)], [round(d, 3), z0]]}
        segs.append(seg); pos.append((kind, Path(str(src)).stem, round(a, 3), round(d, 3), ph))
        for ov in ovs:
            if isinstance(ov, tuple): texts.append(small(ov[1], a, b))
            elif ov.startswith("card:"): ovl.append(card(ov[5:], a, b))
            else:
                # a rank card / label that spans consecutive shots is laid once
                if ovl and ovl[-1]["file"].endswith(f"/{ov}.png") and abs(ovl[-1]["end"] - a) < 0.01: ovl[-1]["end"] = round(b, 3)
                else: ovl.append(ov_png(ov, a, b))
    segs.append({"src": str(GX / "endcard.mp4"), "start": 0.0, "end": END, "mute": True, "note": "end card"}); pos.append(("end", "endcard", round(vo_end, 3), END, ""))
    total = vo_end + END
    ovl.insert(0, {"file": str(GX / "banner.png"), "start": 0.0, "end": round(bounds[5] if hook == "h1" else bounds[4], 3), "w": 978, "x": 2, "y": 196,
                   "fade_in": 0.0, "fade_out": 0.15})
    # banner sits above the frame top band: shift y into the safe zone
    ovl[0]["y"] = 214; ovl[0]["x"] = 491 - 978 // 2
    vo = [{"file": str(VO / f"{lid}.mp3"), "at": round(starts[lid] + LEAD, 3)} for lid in lines]
    mus = V2 / f"edl/music_{hook}.wav"; mus.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", str(P / "assets/music/Life_of_Riley.mp3"), "-t", f"{total:.3f}",
                    "-af", f"afade=t=in:d=0.4,volume=1.0,afade=t=out:st={max(total - 2.0, 0):.3f}:d=2.0", "-ar", "48000", str(mus)], check=True)
    edl = {"segments": segs, "grade": "natural", "texts": texts, "overlays": ovl,
           "tracks": [{"name": "vo", "gain_db": 0, "clips": vo}] + sound_bed(pos),
           "music": {"file": str(mus), "gain_db": -22, "duck": True, "start": 0, "fade_out": 0.01}, "audio": {"enhance": False}}
    out = V2 / f"edl/set4v2_{hook}.edl.json"; out.write_text(json.dumps(edl, indent=1))
    (V2 / f"edl/set4v2_{hook}.pos.json").write_text(json.dumps(pos, indent=0))
    lens = [p[3] for p in pos[:-1]]
    print(f"{out.name}: {total:.1f} s, {len(segs)} shots, median {sorted(lens)[len(lens)//2]:.2f} s, longest {max(lens):.2f} s "
          f"({pos[lens.index(max(lens))][4][:40]})")
    for c, v in _off.items(): print(f"  sync {c}: offsets {v}")

FOLEY = {"K_test_tape": ("tape", 0.3, -12), "i05_exam": ("spray", 0.5, -10), "B7_vapour": ("spray", 0.2, -14), "i11_file": ("file", 0.2, -14),
         "B6_padpress": ("peel", 0.3, -14), "B11_snap": ("pop", 0.6, -14), "g_calendar": ("marker", 0.5, -16), "B20_plus14": ("marker", 0.4, -16),
         "B17_bin": ("pop", 0.6, -14), "phone_delete": ("chip", 0.6, -14), "B23_drawer": ("pop", 0.9, -12), "offer": ("pop", 0.95, -12),
         "R_pdp_scroll": ("chip", 1.6, -14), "P8_timelapse": ("shine", 0.3, -16), "endcard": ("shine", 0.2, -12)}
def sound_bed(pos):
    mp = json.loads((P / "work/sfx_map.json").read_text())
    amb, fol = [], []
    for kind, name, st, ln, ph in pos:
        if kind in ("clip", "mom") and mp.get("room") and not name.startswith(("s_", "g_", "offer", "R_")):
            amb.append({"file": mp["room"], "at": st, "in": round(st % 20, 3), "dur": ln, "gain_db": -32, "fade_in": 0.04, "fade_out": 0.04})
        if ph.startswith("Number") and mp.get("whoosh"): fol.append({"file": mp["whoosh"], "at": max(st - 0.05, 0), "in": 0, "dur": 1.2, "gain_db": -14, "fade_out": 0.1})
        if name in FOLEY and mp.get(FOLEY[name][0]):
            nm, off, g = FOLEY[name]; fol.append({"file": mp[nm], "at": round(st + off, 3), "in": 0, "dur": 1.5, "gain_db": g, "fade_out": 0.1})
    return [{"name": "ambience", "gain_db": 0, "clips": amb}, {"name": "foley", "gain_db": 0, "clips": fol}]

if __name__ == "__main__":
    for h in sys.argv[1:] or ["h1", "h2", "h3"]: build(h)
