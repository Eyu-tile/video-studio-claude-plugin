#!/usr/bin/env python3
"""Set 6 graphics (code, free). Reuses the Set 18 helpers. Out: projects/rootout-set6/assets/graphics/.
Hook boxes (H1/H2/H3), citation card (van Haalen 2009, script row 4: shown as a citation card, no added claims),
8x gauge frames, offer card with the 90-day seal, end card ("Start before it spreads."). No disclaimer text (house L1)."""
import math, os, sys
from pathlib import Path
os.environ["S18"] = "/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set6"
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "set18_build"))
import render_gfx18 as g
from render_gfx18 import W, H, NAVY, BLUE, ICE, ORANGE, WHITE, F, ease, centered, anim, hook_box, seal, gauge_frames, DUO

G = g.G  # projects/rootout-set6/assets/graphics

def citation(d, img, t):  # card slides up; "≈ 2× as likely" stamps in at 0.9 s
    y = 520 + int(120 * (1 - ease(t / 0.45)))
    d.rounded_rectangle((70, y, W - 70, y + 860), 44, fill=WHITE, outline=(214, 222, 232), width=4)
    f, fb = F("Medium", 40), F("ExtraBold", 50)
    d.text((130, y + 70), "British Journal of Dermatology · 2009", font=f, fill=(110, 118, 130))
    for i, line in enumerate(("Warts in primary schoolchildren:", "prevalence and relation", "with environmental factors")):
        d.text((130, y + 150 + i * 66), line, font=fb, fill=NAVY)
    d.text((130, y + 370), "van Haalen et al.", font=F("Medium", 40), fill=(110, 118, 130))
    d.line((130, y + 450, W - 130, y + 450), fill=(226, 230, 236), width=3)
    d.text((130, y + 490), "1,465 schoolkids, ages 4–12", font=F("Bold", 48), fill=NAVY)
    d.rounded_rectangle((118, y + 572, W - 118, y + 650), 14, fill=(255, 224, 102))
    d.text((130, y + 584), "family member with warts", font=F("Bold", 48), fill=NAVY)
    if t > 0.9:
        s = 1 + 0.35 * (1 - ease((t - 0.9) / 0.3)); f2 = F("Black", int(96 * s)); txt = "≈ 2× as likely"
        tw = d.textlength(txt, font=f2); d.text(((W - tw) / 2, y + 690), txt, font=f2, fill=ORANGE)

def offer(d, img, t):
    d.rectangle((0, 0, W, H), fill=ICE)
    bw = 760; b = DUO.resize((bw, int(DUO.height * bw / DUO.width))); img.paste(b, ((W - bw) // 2, 330 + int(10 * math.sin(t * 2.2))), b)
    k = ease((t - 0.2) / 0.4); centered(d, 1180, "Buy 2, get 1 free", F("Black", int(84 * (0.9 + 0.1 * k))), ORANGE)
    if t > 0.7:
        s = g.Image.open(G / "seal90.png").convert("RGBA"); sz = int(320 * ease((t - 0.7) / 0.3)) or 1
        s = s.resize((sz, sz)); img.paste(s, ((W - sz) // 2, 1330), s)

def end_card(d, img, t):
    d.rectangle((0, 0, W, H), fill=ICE); centered(d, 250, "Start before", F("Black", 96)); centered(d, 365, "it spreads.", F("Black", 96), ORANGE)
    bw = 720; b = DUO.resize((bw, int(DUO.height * bw / DUO.width))); img.paste(b, ((W - bw) // 2, 560 + int(12 * math.sin(t * 2.2))), b)
    for x, whole in ((130, False), (950, True)):
        d.line((x - 70, 1150, x + 70, 1150), fill=(140, 110, 70), width=8)
        d.line((x, 1150, x, 1000), fill=(80, 140, 60), width=12); d.ellipse((x - 55, 930, x + 55, 1040), fill=(246, 196, 40))
        if whole:
            d.line((x, 1150, x - 12, 1260, x + 10, 1340), fill=(250, 246, 236), width=16); d.line((x - 4, 1220, x - 40, 1270), fill=(250, 246, 236), width=8)
    centered(d, 1440, "Buy 2, get 1 free", F("ExtraBold", 58)); centered(d, 1550, "90-day money-back", F("Bold", 48), BLUE)
    pr = 1 + 0.04 * math.sin(t * 5); bw2, bh2 = int(480 * pr), int(120 * pr); x0, y0 = (W - bw2) // 2, 1680
    d.rounded_rectangle((x0, y0, x0 + bw2, y0 + bh2), bh2 // 2, fill=ORANGE); f = F("ExtraBold", 60); tw = d.textlength("Shop now", font=f)
    d.text(((W - tw) / 2, y0 + (bh2 - 60) / 2 - 8), "Shop now", font=f, fill=WHITE)

if __name__ == "__main__":
    hook_box("It started with a limp.", G / "hook_h1.png")
    hook_box("\"It hurts to step on.\"", G / "hook_h2.png")
    hook_box("Turn his foot over tonight", G / "hook_h3.png")
    seal(G / "seal90.png"); gauge_frames(G / "gauge")
    anim("c_citation", 3.4, citation); anim("c_offer", 3.6, offer); anim("c_end", 3.2, end_card)
    print("ok", sorted(p.name for p in G.iterdir()))
