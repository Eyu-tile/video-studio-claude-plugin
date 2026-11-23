#!/usr/bin/env python3
"""Captions for Set 17 (client 23 Nov: captions throughout). Text = the locked script (BRIEF.md spelling), timed with the
VO word timestamps of each line at its place in the cut. 2-4 words per card, bold pop, spoken word in brand orange.
Off the web cards (moved to the bottom edge) and off the CTA (hidden) so product/offer stay clean. -> work/captions_<hook>.ass"""
import json, re, sys, difflib
from pathlib import Path
P = Path(__file__).resolve().parent.parent; hook = (sys.argv[1:] or ["h1"])[0]
S = {  # exact script text per VO line (BRIEF.md)
 "L01": "Sorry to keep you waiting. It's wart season. So, what's going on?", "L02": "We froze his wart twice, and it came back.",
 "L03": "That sounds like the root. Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back.",
 "L03b": "Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back.",
 "L04": "But the skin on top is so hard. Nothing gets in.", "L05": "That sounds like a hard-top problem. Lemon softens that skin, so the rest can get in.",
 "L06": "The cream from the store just sits on top.", "L07": "That sounds like a thick cream. You need a thin oil. Tea tree sinks in, up to 8x deeper than a regular cream, and carries the rest down with it.",
 "L08": "And it hurts him to step on.", "L09": "That sounds like it's growing inward. Pokeweed and white cedar break it down from the root, so it can't grow back.",
 "L10": "Now his sister has one.", "L11": "That sounds like it's spreading at home. A study of almost 1,500 schoolkids found someone at home with a wart makes the other kids about twice as likely to get one. So don't wait.",
 "L12": "He screams if anyone touches it.", "L13": "That sounds like he's been hurt before. So, nothing that stings. No acid, no freezing. A kids' formula, ages 4 and up. Just a little cool tingle.",
 "L14": "So I need lemon, tea tree, pokeweed, white cedar… four different bottles? That's going to get expensive.",
 "L15": "You could. But RootOut has all four plants in one little oil.",
 "L16fix": "At bedtime, two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top, so it soaks all night. Two minutes.",
 "L17": "Most spots are gone in about two weeks. Then keep going fourteen more nights, so the root is gone too.",
 "L18": "I'd grab a couple, one for each kid. Buy two, and the third one's free. And you've got 90 days to ask for your money back.",
 "Lh2a": "I'd get it down till the black dots were gone, and it always came back.", "Lh2b": "That sounds like the root.",
 "Lh3a": "His wart is back. Again.", "Lh3b": "Then let's talk about the root.",
}
VO = json.load(open(P / f"work/{hook}_vo_times.json")); VW = json.load(open(P / "work/vo_words.json"))
def nz(w): return re.sub(r"[^a-z0-9]", "", w.lower())
EXP = {"8x": ["eight", "times"], "1500": ["1", "500"], "rootout": ["root", "out"], "pokeweed": ["poke", "weed"], "schoolkids": ["school", "kids"],
       "fourteen": ["14"], "90": ["90"], "hardtop": ["hardtop"]}
def timed(line, t0):
    toks = S[line].split(); ww = VW[line]["words"]; wn = [nz(w[0]) for w in ww]
    out, j = [], 0
    for tok in toks:
        k = nz(tok); parts = EXP.get(k, [k]); hit = None
        for jj in range(j, min(j + 4, len(wn))):
            if wn[jj] == parts[0] or wn[jj].startswith(parts[0][:4]) or parts[0].startswith(wn[jj][:4] or "#"):
                hit = jj; break
        if hit is None: out.append([tok, None, None]); continue
        end = min(hit + len(parts) - 1, len(ww) - 1); out.append([tok, t0 + ww[hit][1], t0 + ww[end][2]]); j = end + 1
    for i, w in enumerate(out):  # fill any unmatched word between its neighbours
        if w[1] is None:
            a = next((out[k][2] for k in range(i - 1, -1, -1) if out[k][2] is not None), t0)
            b = next((out[k][1] for k in range(i + 1, len(out)) if out[k][1] is not None), a + 0.3)
            w[1], w[2] = a, max(a + 0.08, b)
    return out
lines = dict(VO); dur = lambda n: VW[n]["dur"]
cards = [(lines["L08"], lines["L08"] + dur("L08")), (lines["L11"] + 2.0, lines["L11"] + 9.0)]
cta = lines["L18"] + 2.6
def ts(t): t = max(0, t); return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00221A0B,&H64000000,-1,0,0,0,100,100,0,0,1,6,3,2,70,70,600,1
Style: CapLow,Inter ExtraBold,62,&H00FFFFFF,&H00FFFFFF,&H00221A0B,&H64000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ORANGE = r"{\c&H184EE0&}"; WHITE = r"{\c&HFFFFFF&}"
ev = []
for line, t0 in VO:
    if line not in S: continue
    w = timed(line, t0); chunks, cur = [], []
    for x in w:  # 2-4 words, break after punctuation
        cur.append(x)
        if len(cur) >= 4 or re.search(r"[.,?!…]$", x[0]): chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    for ci, ch in enumerate(chunks):
        st, en = ch[0][1], (chunks[ci + 1][0][1] if ci + 1 < len(chunks) else ch[-1][2] + 0.25)
        if st >= cta: continue
        en = min(en, cta)
        style = "CapLow" if any(a <= st < b for a, b in cards) else "Cap"
        for wi, x in enumerate(ch):  # one event per spoken word: that word orange
            a = x[1] if wi else st; b = ch[wi + 1][1] if wi + 1 < len(ch) else en
            if b - a < 0.02: continue
            txt = " ".join((ORANGE + y[0].upper() + WHITE) if k == wi else y[0].upper() for k, y in enumerate(ch))
            pop = r"{\fscx112\fscy112\t(0,90,\fscx100\fscy100)}" if wi == 0 else ""
            ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{pop}{txt}")
(P / f"work/captions_{hook}.ass").write_text(hdr + "\n".join(ev) + "\n"); print(hook, len(ev), "caption events")
