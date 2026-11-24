#!/usr/bin/env python3
"""Set 18 H1 v3 (client notes 24 Nov):
- New dad: Soul 2 base -> GPT Image 2.6 scene edits -> each locked as Seedance 2.5 720p start frame; he speaks his line
  natively from the prompt (no audio reference / lip-sync forcing) so he moves and talks naturally.
- Voice lock: the first take's (K1a) voice; every off-camera line is Seed Audio cloned from it (raw/vo4).
- Edit rules: 0-4 s only the dad; every b-roll ~3 s (2.6-4.2 s before the 1.1x speed-up); every dad segment >= 4 s
  final (>= 4.4 s here) with a slow push-in; one study card only; no infants (kids 4+), no kid faces.
Usage: python3 build18v3.py [--plan]   (--plan prints the shot list + rule check without rendering)"""
import json, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import build18v2 as V2
from build18v2 import ff, stt, find, dur, fr, W, H, FPS, COVER, ENC, P, RE, ST, GEN, G, PDP, SITE
V2.TLm.NUM.update({"4": "four", "1500": "fifteenhundred", "8": "eight", "90": "ninety", "14": "fourteen"})
C3 = GEN / "clips3"; VO4 = P / "raw/vo4"
OUT = P / "work/build/H1v3"; SH = OUT / "shots"; SH.mkdir(parents=True, exist_ok=True)
FINAL = P / "out/WilloMD_RootOut_Set18_H1_9x16_v3.mp4"
SPEED = float(os.environ.get("SPEED", "1.1")); MIN_M = 4.0 * SPEED; BR = (2.4 * SPEED, 3.8 * SPEED)
M = "M"
TK = lambda n: C3 / f"{n}.mp4"
VO = lambda n: VO4 / f"{n}.wav"

# (kind, file, text, hold_after, events[(phrase|None, source|M, opts)])
ITEMS = [
 ("take", TK("K1a"), "If your kid's doctor said, 'Leave the wart, it'll go away,' I'd bet money there's a second one coming. Ask me how I know.", 0.15,
   [(None, M, {"hook": 1})]),
 ("tts", VO("v01"), "This is how we finally got rid of it.", 0.05, [(None, RE / "03_S1_b09_dand_root.mp4", {"in": 0.4})]),
 ("tts", VO("t02"), "Root and all.", 0.12, []),
 ("tts", VO("t03"), "My son had one wart on his heel. One. The doctor took a look and said, 'Leave it, it'll go away.'", 0.1,
   [(None, RE / "27_S19_b21_mason_sole.mp4", {"push": 1.1}), ("The doctor took", ST / "b03_doctor/mixkit_32176_doctor-putting-on-a-stethoscope.mp4", {"in": 6.0})]),
 ("take", TK("K1b"), "So we left it. Every week it got a little bigger. I started checking it against a Cheerio.", 0.1, [(None, M, {})]),
 ("tts", VO("t04b"), "By week six, the wart was winning.", 0.05, [(None, "WEEKS", {})]),
 ("tts", VO("t05"), "Then a second one showed up right next to it. Then my daughter got one, on her finger. She's six.", 0.05,
   [(None, GEN / "stills/N4.png", {"push": (1.0, 1.1)}), ("Then my daughter", GEN / "stills/N5.png", {"push": (1.05, 1.18), "fy": 0.62})]),
 ("tts", VO("v05"), "She's wanted everything her brother had since she could walk.", 0.1, [(None, RE / "33_S20_g07_sister.mp4", {"in": 0.2})]),
 ("take", TK("K1c"), "This, she got. Turns out there's a real study on this.", 0.1, [(None, M, {})]),
 ("tts", VO("t06"), "Almost 1,500 schoolkids. If someone at home has a wart, the other kids are about twice as likely to get one. And the 'it'll go away' part is half right. About half of kids' warts go on their own within a year. Half don't.", 0.1,
   [(None, ST / "b06_school/mixkit_24970_american-children-boarding-a-school-bus.mp4", {"in": 0.5}),
    ("If someone at home", G / "w1_card.png", {"card": 1, "chip_at": ("twice as likely", "x2")}),
    ("And the", RE / "41_S19_b29_sneakers.mp4", {"in": 0.3}), ("About half of", RE / "26_S19_b60_wart_back.mp4", {"in": 1.0})]),
 ("take", TK("K1d"), "We got the other half. So let me save you some time and money.", 0.05, [(None, M, {})]),
 ("tts", VO("t07"), "Here's what you'll try next.", 0.05, [(None, GEN / "clips/G1.mp4", {})]),
 ("tts", VO("t08"), "Freezing. Ten seconds of screaming, a milkshake on the way home, then you book the next one.", 0.1,
   [("Ten seconds", RE / "24_S1_b04_clinic.mp4", {"in": 0.3}), ("then you book", G / "c_freezecal.mp4", {"anim": 1})]),
 ("take", TK("K2a"), "Congratulations. You've got a wart subscription. Acid from the drugstore. It turns the skin around it white. The wart doesn't even notice. Duct tape. A week of sticky socks. Same wart.", 0.15,
   [(None, M, {}), ("It turns the skin", GEN / "stills/N7.png", {"push": (1.05, 1.18)}), ("Duct tape", M, {})]),
 ("take", TK("Y1"), "Every one of those has the same problem. Freezing, acid and shaving only snap off the top,", 0.03, [(None, M, {})]),
 ("tts", VO("t11b"), "like picking a dandelion. The root stays under the hard skin, so it grows back.", 0.1,
   [(None, RE / "00_S1_b06_dand_snap.mp4", {"in": 1.0}), ("The root stays", RE / "07_S17_x3_soil_cutaway.mp4", {})]),
 ("take", TK("K2b1"), "You have to get under that hard skin, down to the root. That's what RootOut does. It's an oil with four plants, and each one has a job.", 0.05,
   [(None, M, {}), ("It's an oil with four", RE / "13_S17_x9_bottle_counter.mp4", {"in": 0.5, "plants": 1})]),
 ("tts", VO("t13a"), "Lemon softens the hard skin on top, so the oil can get in.", 0.05, [(None, RE / "08_S13_m1_skin_door.mp4", {})]),
 ("take", TK("K2b2"), "Tea tree is a thin oil. It sinks in up to 8x deeper than a regular cream, and it carries the last two plants down with it.", 0.05,
   [(None, M, {"gauge": 1})]),
 ("tts", VO("t13c"), "Pokeweed and white cedar break the wart down from the root, so it can't grow back.", 0.1,
   [(None, RE / "15_S17_x6_root_3d.mp4", {}), ("so it can't", RE / "09_S13_m2_skin_root.mp4", {"in": 1.5})]),
 ("take", TK("K2b3"), "And it's made for kids. A kids' formula, ages 4 and up. No acid, no freezing, no blister. Just a little cool tingle. Recommended by pediatricians.", 0.1,
   [(None, M, {"chip_at": ("A kids", "kids4")}), ("Just a little", ST / "b03_doctor/mixkit_17475_doctor-writing-a-prescription.mp4", {"in": 1.5})]),
 ("tts", VO("t15"), "At bedtime, two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top. Two minutes, and they're asleep.", 0.1,
   [(None, RE / "12_S17_b2_routine.mp4", {"in": 0.0}), ("Brush the oil on", SITE / "shopify-ff701bf4.mp4", {"in": 2.3, "crop": "1080:900:0:150"}),
    ("Two minutes", RE / "23_S1_b11_nightstand.mp4", {"in": 0.3})]),
 ("tts", VO("t15d"), "Does it hurt?", 0.1, [(None, RE / "30_S19_b52_socks_bed.mp4", {"in": 0.3})]),
 ("girl", P / "raw/vo/r15b_girl.mp3", "Nope. It's cold and tingly.", 0.2, []),
 ("tts", VO("t16"), "About two weeks later, his were gone. Hers too.", 0.05, [(None, GEN / "stills/N9.png", {"push": (1.0, 1.1)})]),
 ("tts", VO("v16b"), "We kept going 14 more nights to get the roots.", 0.1, [(None, G / "c_nights.mp4", {"anim": 1, "chip": "plus14"})]),
 ("take", TK("Y2"), "Last Saturday they both ran barefoot through the sprinkler, and I didn't check a single foot.", 0.1, [(None, M, {})]),
 ("take", TK("K3"), "Link's below. Get two and the third one's on us, so every kid has their own. And you've got 90 days. If it's not gone, every penny comes back. Or, you know, leave it. See how that goes.", 0.4,
   [(None, M, {"chip_at": ("Get two", "offer")}), ("And you've got", PDP / "pdp-09-offer-guarantee-v11.jpg", {"card": 1}), ("every penny", M, {})]),
]
END = 3.0

def piece(kind, f, text):
    w = stt(f); a, b = w[0][1], w[-1][2]
    if kind == "take":  # a native take may add words before/after: span = first 3 words .. last 3 words of the line
        a = find(w, " ".join(text.split()[:3]))[0]; b = find(w, " ".join(text.split()[-3:]), a)[1]
    return max(0, a - 0.06), b + 0.12, w

def layout():
    t = 0.15; L = []
    for k, (kind, f, text, hold, ev) in enumerate(ITEMS):
        a, b, w = piece(kind, f, text)
        L.append(dict(k=k, kind=kind, f=str(f), text=text, a=a, b=b, t0=t, t1=t + b - a, words=w, ev=ev, src=Path(f).stem)); t += b - a + hold
    return L, t

def at(it, ph):
    a, _ = find(it["words"], ph, it["a"]); return it["t0"] + (a - it["a"]) - 0.05

def plan():
    L, VEND = layout(); cuts = []
    for it in L:
        for ph, src, o in it["ev"]:
            cuts.append((max(0.0, it["t0"] if ph is None else at(it, ph)), src, o, it))
    cuts.sort(key=lambda c: c[0]); TOTAL = VEND + END
    shots = []
    for k, (t0, src, o, it) in enumerate(cuts):
        t1 = cuts[k + 1][0] if k + 1 < len(cuts) else VEND
        shots.append(dict(n=k + 1, t0=t0, t1=t1, src=src, o=o, it=it))
    shots.append(dict(n=len(shots) + 1, t0=VEND, t1=TOTAL, src=G / "c_end.mp4", o={"anim": 1}, it=None))
    bad = []
    for s in shots[:-1]:
        d = s["t1"] - s["t0"]
        if s["src"] == M and d < MIN_M: bad.append((s["n"], "dad", round(d / SPEED, 2)))
        if s["src"] != M and not (BR[0] <= d <= BR[1]): bad.append((s["n"], Path(str(s["src"])).name, round(d / SPEED, 2)))
    return L, shots, TOTAL, bad

def render(out, s):
    src, o, n = s["src"], s["o"], fr(s["t1"]) - fr(s["t0"])
    if src == M:  # dad: continuous slow push-in over the whole segment
        it = s["it"]; cin = it["a"] + (s["t0"] - it["t0"])
        vf = (f"{COVER},fps={FPS},tpad=stop_mode=clone:stop_duration=2,"
              f"zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},setsar=1")
        return ff("-ss", f"{cin:.3f}", "-i", it["f"], "-vf", vf, "-frames:v", n, *ENC, out)
    if src == "WEEKS":  # one 3 s growth shot: week 1 -> 3 -> 6 dissolving, slow push
        k = n // 3
        fl = ";".join(f"[{i}]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS},trim=end_frame={k + 8},setpts=PTS-STARTPTS[s{i}]" for i in range(3))
        fl += f";[s0][s1]xfade=transition=fade:duration=0.25:offset={k / FPS - 0.12:.3f}[x1];[x1][s2]xfade=transition=fade:duration=0.25:offset={2 * k / FPS - 0.25:.3f},tpad=stop_mode=clone:stop_duration=1,"
        fl += f"zoompan=z='1+0.1*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}[v]"
        return ff(*sum((["-loop", "1", "-i", GEN / f"stills/N{i}.png"] for i in (1, 2, 3)), []), "-filter_complex", fl, "-map", "[v]", "-frames:v", n, *ENC, out)
    V2.render(out, src, o, n)

def build():
    L, shots, TOTAL, bad = plan()
    for s in shots:
        print(f"{s['n']:3d} {s['t0']/SPEED:7.2f} {(s['t1']-s['t0'])/SPEED:5.2f}  {'DAD ' + s['it']['src'] if s['src'] == M else Path(str(s['src'])).name}")
    print("total", round(TOTAL / SPEED, 1), "s;", "rule breaks:", bad or "none")
    if "--plan" in sys.argv: return
    for s in shots:
        out = SH / f"s{s['n']:03d}.mp4"
        if not out.exists() or os.environ.get("REBUILD"): render(out, s)
    (SH / "l.txt").write_text("".join(f"file 's{s['n']:03d}.mp4'\n" for s in shots))
    ff("-f", "concat", "-safe", "0", "-i", SH / "l.txt", "-c", "copy", OUT / "picture.mp4")
    ins, fl, mix = [], [], []
    for j, it in enumerate(L):
        ins += ["-i", it["f"]]
        fl.append(f"[{j}]atrim={it['a']:.3f}:{it['b']:.3f},asetpts=N/SR/TB,aresample=48000,aformat=channel_layouts=mono,highpass=f=80,"
                  f"loudnorm=I=-18:TP=-3:LRA=7,afade=t=in:d=0.02,afade=t=out:st={it['b'] - it['a'] - 0.05:.3f}:d=0.05,adelay={int(it['t0'] * 1000)}[a{j}]")
        mix.append(f"[a{j}]")
    fl.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,acompressor=threshold=-22dB:ratio=3:attack=5:release=120,apad=whole_dur={TOTAL:.3f}[vo]")
    ff(*ins, "-filter_complex", ";".join(fl), "-map", "[vo]", "-t", f"{TOTAL:.3f}", "-c:a", "pcm_s16le", OUT / "vo.wav")
    # hand the shot list to v2's finisher (captions, chips, gauge, music, 1.1x)
    sh2 = []
    for s in shots:
        o = dict(s["o"])
        if "chip_at" in o: ph, name = o.pop("chip_at"); o["chip"] = name; o["chip_t"] = round(at(s["it"], ph), 3)
        sh2.append(dict(n=s["n"], t0=round(s["t0"], 3), t1=round(s["t1"], 3), src="TAKE" if s["src"] == M else str(s["src"]),
                        opts={a: str(b) for a, b in o.items()}))
    json.dump(dict(total=TOTAL, items=[{k: v for k, v in i.items() if k != "words"} for i in L], shots=sh2), open(OUT / "timeline.json", "w"), indent=1, default=str)
    V2.OUT, V2.FINAL = OUT, FINAL
    V2.finish(L, sh2, TOTAL)

if __name__ == "__main__": build()
