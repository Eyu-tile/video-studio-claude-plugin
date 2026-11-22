#!/usr/bin/env python3
"""Captions for Set 19 = the locked script text, word for word, timed from the edit's audio.
Timing comes from word stamps of each piece (ElevenLabs VO or the talking clip); text comes from SCRIPT (aligned with difflib,
so whisper spellings like "route", "Rude out", "$15" never reach the screen). Then `vs captions` (bold-pop) builds the ASS,
and captions are kept off the end card. Usage: python3 work/captions.py H1"""
import json, re, subprocess, sys, difflib
from pathlib import Path

P = Path(__file__).resolve().parent.parent
VS = P.parents[2] / "plugins/video-studio/bin/vs"
h = sys.argv[1]
TL = json.load(open(P / f"work/build/{h}/timeline.json"))
VOW = json.load(open(P / "work/vo_words.json")); TW = json.load(open(P / "work/talk_words.json"))

ROW1 = {"H1": "I was bleaching the tub after every bath, until our school nurse told me what she tells every mom.",
        "H2": "I was sure my kids caught their warts at the town pool. Then our school nurse told me to check my own bathroom.",
        "H3": "He only goes barefoot at home, never outside. So he got it here. Then his sister got one. Then my husband.",
        "H4": "The whole family's home for winter break. One bathroom, five feet, two weeks. That's how one wart turns into four. So this year, I did this first."}
ROW2 = {"H3": "That's my son, Mason. Three warts, one bathroom."}
ROW2_DEFAULT = ("It started with a hard little spot on Mason's foot, with tiny black dots. Then Lily got one on her heel. "
                "Then my husband got one. Three warts, one bathroom.")
BODY = """So I made rules. Everybody gets their own towel. Flip-flops in the shower. I bleached the tub after every single bath. White socks to bed. A Band-Aid on every foot before school. A whole shelf of freezing kits, fifteen dollars each. One doctor visit, two hundred fifty dollars and a morning off work. And Mason's came right back.
I figured warts were just part of having kids. They had to be catching it at the town pool.
Then I noticed something weird. Our school nurse sees four hundred kids. She has three of her own, same as me. And nobody in her house has a wart. So I asked her what she does.
She said, 'Check your house first.' A study of almost 1,500 schoolkids found that when someone at home has a wart, the other kids are about twice as likely to get one. They found no link to the pool.
Then I told her about my shelf of kits. She said, 'Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back.' So the root stayed. All my rules cleaned the bathroom. None of them touched the root. I felt awful.
Then she told me what she tells every mom. RootOut. It's an oil with four plants. Lemon softens the hard skin on top, so the oil can get in. Tea tree is a thin oil. It sinks in up to 8x deeper than a regular cream, and carries pokeweed and white cedar down with it. Those two break the wart down from the root, so it can't grow back.
I asked if it was safe for Lily. She's six. The nurse said it's a kids' formula, ages 4 and up. No acid, no freezing, no blister. Just a little cool tingle. And it's recommended by pediatricians. Another mom at pickup told me, 'My son fell asleep with the dot on. He didn't even notice.'
So now it's part of bedtime. Two kids and one husband, lined up on the edge of the tub. Two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top. Everybody has their own bottle.
In about two weeks, Mason's spot was gone. We kept going fourteen more nights, so the root is gone too. Lily and my husband are right behind him.
Last night was bath time with no rules. No flip-flops in the shower. No bleach. All three kids barefoot, running down the hall. And Theo, my four-year-old, never got one.
So if one person in your house has a wart, check every foot tonight. Then tap the link. One bottle for each kid: buy two, the third is free. My husband counts as a kid. And you've got 90 days to ask for your money back."""
script = " ".join([ROW1[h], ROW2.get(h, ROW2_DEFAULT), BODY.replace("\n", " ")])
stoks = script.split()

# ---- timed words from the pieces ----
timed = []
for kind, src, a, b, t0 in TL["pieces"]:
    ws = VOW[src] if kind == "vo" else TW[Path(src).stem]
    for s, e, txt in ws:
        mid = (s + e) / 2
        if a - 0.02 <= mid <= b + 0.02:
            timed.append([t0 + s - a, t0 + e - a, txt])

norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
A = [norm(x[2]) for x in timed]; B = [norm(x) for x in stoks]
out = []
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        for k in range(i2 - i1): out.append({"w": stoks[j1 + k], "s": timed[i1 + k][0], "e": timed[i1 + k][1]})
    elif op in ("replace", "insert"):
        if j2 == j1: continue
        if i2 > i1: s, e = timed[i1][0], timed[i2 - 1][1]
        else:  # script words with no timed match: squeeze between neighbours
            s = timed[i1 - 1][1] if i1 > 0 else 0.0; e = timed[i1][0] if i1 < len(timed) else s + 0.3
        n = j2 - j1; step = max(0.05, (e - s) / n)
        for k in range(n): out.append({"w": stoks[j1 + k], "s": s + k * step, "e": s + (k + 1) * step})
    # 'delete' (whisper extras) dropped
miss = sum(1 for op in sm.get_opcodes() if op[0] != "equal")
print(h, "script words", len(stoks), "timed", len(timed), "non-equal blocks", miss)
out.sort(key=lambda x: x["s"])
assert [x["w"] for x in out] == stoks, "caption words differ from script"
tx = P / f"work/build/{h}/script_words.json"
json.dump({"source": str(P / f"work/build/{h}/video.mp4"), "words": out, "duration": TL["length"]}, open(tx, "w"), indent=0)
raw = P / f"work/build/{h}/video.mp4"
ide = P / f"work/build/{h}/identity.edl.json"
ide.write_text(json.dumps({"source": str(raw), "segments": [{"src": str(raw), "start": 0, "end": round(TL["length"], 3)}]}))
cap = P / f"work/build/{h}/captions"
subprocess.run([str(VS), "captions", str(tx), str(ide), "-o", str(cap), "--style", "bold-pop", "--aspect", "9:16",
                "--accent", "#FFD400", "--font", "Inter"], check=True)
# drop captions on the end card
ass = Path(str(cap) + ".ass")
def ts(v): hh, mm, ss = v.split(":"); return int(hh) * 3600 + int(mm) * 60 + float(ss)
keep = []
for ln in ass.read_text().splitlines():
    if ln.startswith("Dialogue:"):
        st = ts(ln.split(",", 9)[1])
        if any(a - 0.05 <= st < bb for a, bb in TL["nocap"]): continue
        if any(a - 0.05 <= st < bb for a, bb in TL.get("captop", [])):
            f = ln.split(",", 9); f[9] = "{\\an8\\pos(540,24)}" + f[9]; ln = ",".join(f)
    keep.append(ln)
ass.write_text("\n".join(keep) + "\n"); print("captions ->", ass)
