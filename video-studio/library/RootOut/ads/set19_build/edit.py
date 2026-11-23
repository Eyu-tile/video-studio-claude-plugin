#!/usr/bin/env python3
"""RootOut Set 19 edit, row by row from SCRIPT.md (verbatim). Usage: python3 work/edit.py H1|H2|H3|H4"""
import json, sys, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import Build, w, P, CL, ST, GF, PH

TW = json.load(open(P / "work/talk_words.json"))  # whisper words of each talking clip


def tw(clip, word, occ=0, edge="start"):
    hits = [x for x in TW[clip] if x[2].lower().strip(".,!?'\"") == word.lower()]
    x = hits[occ if occ >= 0 else len(hits) + occ]; return x[0] if edge == "start" else x[1]


def speech(clip, pre=0.12, post=0.35):
    ws = TW[clip]; return max(0, ws[0][0] - pre), ws[-1][1] + post


C = lambda n: CL / f"{n}.mp4"
S = lambda n: next(ST.glob(f"mixkit_{n}_*.mp4"))
PHOTO_DAD = next(PH.glob("*painful-plantar-warts*"))
AI = {"label": "AI illustration"}

hook = sys.argv[1] if len(sys.argv) > 1 else "H1"
b = Build(hook)

# ---- Row 1: hook ----
if hook == "H1":
    a, e = speech("t01_h1_bleach", pre=0.9); b.talk("t01_h1_bleach.mp4", a, e)
elif hook == "H2":
    a, e = speech("t02_h2_door", pre=0.3); b.talk("t02_h2_door.mp4", a, e)
elif hook == "H4":
    a, e = speech("t03_h4_winter", pre=0.3); b.talk("t03_h4_winter.mp4", a, e)
elif hook == "H3":
    b.vo("vo_h3", 0.0, w("vo_h3", "my", 0, "end") - 0.05 + 0.6, [
        (C("b36_tub_line"), 0.0, w("vo_h3", "here")),
        (C("b21_mason_sole"), 0.3, w("vo_h3", "one", 0)),
        (C("b22_lily_heel"), 0.3, w("vo_h3", "then", 1, "start")),
        (PHOTO_DAD, 0, None)], gap=0.1)

# ---- Row 2: the chain ----
if hook == "H3":
    a, e = speech("t04_three_fingers", pre=0.05); b.talk("t04_three_fingers.mp4", a, e)
else:
    b.vo("vo_r2", 0.0, w("vo_r2", "one", 1, "end") + 0.05 if False else w("vo_r2", "three", 0, "start") - 0.05, [
        (C("b21_mason_sole"), 0.0, w("vo_r2", "then", 0, "start")),
        (C("b22_lily_heel"), 0.0, w("vo_r2", "then", 1, "start")),
        (PHOTO_DAD, 0, None)], gap=0.0)
    a = tw("t04_three_fingers", "three") - 0.25; b.talk("t04_three_fingers.mp4", a, speech("t04_three_fingers")[1])

# ---- Row 3: every fix, with its price ----
r = "vo_r3"
b.vo(r, 0.0, WORDS_END := json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (C("b23_towels"), 0.0, w(r, "flip", 0, "start") - 0.05, {"blur": (0.55, 0.75)}),
    (C("b24_flipflops_shower"), 0.0, w(r, "i", 1, "start")),
    (C("b50_scrub"), 0.0, w(r, "white", 0, "start")),
    (C("b25_socks"), 0.0, w(r, "a", 0, "start")),
    (C("b26_bandaid"), 0.0, w(r, "a", 1, "start")),
    (C("b27_kit_shelf"), 0.0, w(r, "one", 0, "start")),
    (S(5407), 8.0, w(r, "$250", 0, "start")),
    (GF / "g_receipt.mp4", 0.0, w(r, "and", 1, "start")),
    (C("b21_mason_sole"), 1.5, None)], gap=0.35)

# ---- Row 4: acceptance ----
a, e = speech("t05_towels", pre=0.2); b.talk("t05_towels.mp4", a, e)

# ---- Row 5: the peer with more kids ----
r = "vo_r5"
b.vo(r, 0.0, w(r, "kids") + 0.15, [
    (S(4434), 2.0, w(r, "our", 0, "start")),
    (S(5886), 3.0, w(r, "400", 0, "start")),
    (C("b29_sneakers_nurse"), 0.0, None)], gap=0.1)
a, e = speech("t06_car", pre=0.1); b.talk("t06_car.mp4", a, e)

# ---- Row 6: the study (real page) ----
r = "vo_r6"
b.vo(r, w(r, "first") + 0.15, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (GF / "g_study.mp4", 0.0, w(r, "twice", 0, "start") - 0.2, {"captop": True}),
    (GF / "g_house.mp4", 0.0, w(r, "they", 0, "start")),
    (GF / "g_study_pool.mp4", 0.0, None, {"captop": True})], gap=0.35)

# ---- Row 7: the Dandelion ----
r = "vo_r7"
b.vo(r, 0.0, w(r, "bathroom") + 0.1, [
    (C("b27_kit_shelf"), 0.5, w(r, "freezing", 0, "start")),
    (S(34699), 1.0, w(r, "like", 0, "start")),
    (C("b30_dand_snap"), 0.0, w(r, "the", 1, "start")),
    (C("b31_dand_back"), 0.0, w(r, "so", 1, "start")),
    (S(36242), 2.0, w(r, "all", 0, "start")),
    (C("b32_footprints"), 0.0, None)], gap=0.1)
a, e = speech("t07_awful", pre=0.1, post=0.6); b.talk("t07_awful.mp4", a, e)

# ---- Row 8: product + four plants ----
a, e = speech("t08_rootout", pre=0.1, post=0.2); b.talk("t08_rootout.mp4", a, e)
r = "vo_r8"
b.vo(r, w(r, "out") + 0.1, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (C("b33_skin_lemon"), 0.0, w(r, "tea", 0, "start") - 0.1, AI),
    (C("b34_skin_teatree"), 0.0, w(r, "those", 0, "start") - 0.1, {"overlay": ("o_gauge", 0.0), "label": "AI illustration"}),
    (C("b34_skin_teatree"), 2.0, None, AI)], gap=0.35)

# ---- Row 9: safe for her ----
a, e = speech("t09_couch", pre=0.1, post=0.1); b.talk("t09_couch.mp4", a, e)
r = "vo_r9"
b.vo(r, w(r, "up") + 0.1, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (C("b52_socks_bed_v2"), 0.0, w(r, "and", 1, "start")),
    (C("b40_three_bottles"), 0.3, w(r, "another", 0, "start")),
    (S(5886), 8.0, None)], gap=0.15)
a, e = speech("t10_mom2", pre=0.1); b.talk("t10_mom2.mp4", a, e)

# ---- Row 10: bedtime routine ----
r = "vo_r10"
b.vo(r, 0.0, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (C("b36_tub_line"), 0.0, w(r, "two", 1, "start")),
    (C("b37_file"), 0.0, w(r, "brush", 0, "start")),
    (ST / "brand_howto_brush.mp4", 0.0, w(r, "a", 0, "start"), {"push": True}),
    (ST / "brand_howto_cover.mp4", 0.0, w(r, "everybody", 0, "start"), {"push": True}),
    (C("b40_three_bottles"), 0.0, None)], gap=0.35)

# ---- Row 11: result + Root Rule ----
r = "vo_r11"
b.vo(r, 0.0, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (S(38501), 1.0, w(r, "lily", 0, "start"), {"overlay": ("o_calendar", 0.0), "speed": 1.3, "push": True}),
    (C("b36_tub_line"), 1.0, None)], gap=0.35)

# ---- Row 12: life back ----
r = "vo_r12"
b.vo(r, 0.0, json.load(open(P / "work/vo_words.json"))[r][-1][1] + 0.05, [
    (C("b53_splash_v2"), 0.0, w(r, "no", 1, "start")),
    (S(47057), 1.0, w(r, "all", 0, "start")),
    (S(48264), 0.5, w(r, "and", 0, "start")),
    (S(48169), 4.0, None)], gap=0.35)

# ---- Row 13: close ----
r = "vo_r13"
b.vo(r, 0.0, w(r, "link") + 0.1, [
    (C("b36_tub_line"), 0.0, w(r, "then", 0, "start")),
    (C("b40_three_bottles"), 1.0, None)], gap=0.1)
a = max(0.0, tw("t11_offer", "one") - 0.15); e = speech("t11_offer", post=0.5)[1]; b.talk("t11_offer.mp4", a, e)

# ---- End card ----
b.card(GF / "g_end.mp4", 3.5)
b.finish()
