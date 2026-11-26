# RootOut Set 1B preview builder: VO track + word-cued b-roll + captions + music -> out/ROS1B_<H>_preview_vN.mp4
# usage: python3 work/build.py H1 [H2 H3] [--version 1]
import json, os, re, subprocess, sys, difflib
from PIL import Image, ImageDraw, ImageFont

P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(P)
LIB = "../../library/RootOut/brand/images/pdp/"
W, H, FPS = 1080, 1920, 30
FONT_B = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FONT_S = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
NAVY, BLUE, ICE, ORANGE = (11, 42, 91), (23, 99, 184), (238, 244, 250), (224, 78, 24)

SCRIPT = {  # verbatim lines (caption text); cues use these words
 "k01": "I'm never letting them freeze my wart again.",
 "k02": "Last time, I cried the whole ride home.",
 "k03": "My wart feels like a pebble when I run.",
 "k04": "Mom's tried everything.",
 "k05": "Grown-ups said my wart would go away by itself.",
 "k06": "It didn't.",
 "k07": "I had it on the bottom of my foot for a whole year. The wart stuff from the store stung really bad.",
 "k08": "So the doctor froze it. Mom had to hold my foot still. The freezing spray burned. I cried. And it grew back anyway.",
 "k09": "Then my mom found out why.",
 "m01": "It wasn't his fault. Or mine. Here's what the freeze missed.",
 "m02": "Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back.",
 "k10": "So it's like a weed. You have to get the root.",
 "m03": "That's what RootOut does. It's an oil with four plants, and each one has a job. Lemon opens up the hard skin. Tea tree takes it down, up to 8x deeper than a regular cream.",
 "k11": "Then pokeweed and white cedar break the wart down. From the root!",
 "m04": "Deep doesn't mean harsh. It's a kids' formula, ages 4 and up. No blister. Recommended by pediatricians.",
 "m05": "At bedtime, two light strokes with the file. That opens up the hard top.",
 "k12": "It just scratches the hard part. It doesn't even hurt.",
 "m06": "Then you brush the oil on.",
 "k13": "It's cold for like one second. Kinda tingly. That's it.",
 "m07": "Then a clear dot seals it in, so it keeps soaking all night.",
 "k14": "Mom paints it on at bedtime. I just keep watching my show.",
 "k15": "No spray. No acid. Nobody holds me down.",
 "t01": "It's like Chapstick for my wart. Just a little cold.",
 "t02": "My daughter's six. She hated the freeze. Now she just sticks her foot out at bedtime.",
 "t03": "It was gone in like two weeks. Now I run at recess.",
 "k16": "Mom cancelled my freeze appointment.",
 "m08": "Get yours from the link below. Buy two, the third's free. And if it's not gone, you get your money back.",
}
SAY = {"8x": "eight times", "4": "four"}  # how a caption word was spoken

R, G = "raw/reuse/", "raw/gen/"
# shots: (line, cue word index in SCRIPT line, source, options). Each shot runs until the next cue.
BODY = [
 ("k07", 0, R+"b21_sole.mp4", {}),
 ("k07", 13, R+"b03_bath.mp4", {"in": 0.5}),            # "The wart stuff from the store"
 ("k08", 0, R+"b04_clinic.mp4", {}),                     # doctor froze it / hold my foot still
 ("k08", 12, R+"s4_vapour.mp4", {}),                     # "The freezing spray burned. I cried."
 ("k08", 18, R+"b60_back.mp4", {"in": 1.2}),             # "And it grew back anyway"
 ("k09", 0, R+"g12_feetup.mp4", {}),
 ("m01", 0, G+"g03.png", {"temp": "N03 mom lifts the bottle"}),
 ("m02", 0, R+"m1_frost.mp4", {}),                       # Freezing, acid and shaving
 ("m02", 4, R+"b06_snap.mp4", {}),                       # only snap off the top, like picking a dandelion
 ("m02", 13, R+"b09_root.mp4", {}),                      # The root stays under the hard skin
 ("m02", 20, R+"b07_back.mp4", {}),                      # so it grows back
 ("k10", 0, G+"g04.png", {"temp": "N04 boy wiggles the dandelion"}),
 ("m03", 0, LIB+"A01-bottle-front-white.jpg", {"fit": "pad", "bg": "white"}),   # That's what RootOut does
 ("m03", 8, R+"s13_door.mp4", {}),                       # four plants ... Lemon opens up the hard skin
 ("m03", 22, R+"m2_soak.mp4", {"in": 1.0}),              # Tea tree takes it down
 ("m03", 27, R+"b10_towels.mp4", {}),                    # up to 8x deeper than a regular cream
 ("k11", 0, R+"x6_root.mp4", {}),                        # pokeweed and white cedar break the wart down
 ("k11", 9, R+"s13_root.mp4", {"in": 1.5}),              # From the root!
 ("m04", 0, R+"b11_night.mp4", {}),                      # Deep doesn't mean harsh. kids' formula, 4 and up
 ("m04", 12, LIB+"RootOut-30-flatlay-v3.jpg", {"fit": "pad", "bg": (238, 244, 250)}),  # No blister. Recommended by pediatricians
 ("m05", 0, R+"b37_file.mp4", {}),
 ("k12", 0, R+"b35_pillow.mp4", {}),
 ("m06", 0, R+"b2_routine.mp4", {"in": 3.0, "zoom": 1.25}),
 ("k13", 0, G+"g05.png", {"temp": "N05 thumbs-up"}),
 ("m07", 0, R+"b55_dot.mp4", {}),
 ("m07", 7, R+"m4_night.mp4", {}),                       # so it keeps soaking all night
 ("k14", 0, R+"dot_pillow.mp4", {}),
 ("k15", 0, G+"g06.png", {"temp": "N06 bin lid shuts"}),
 ("k15", 4, R+"b17_hall.mp4", {}),                       # Nobody holds me down
 ("t01", 0, G+"g07.png", {"temp": "N07 girl with the bottle"}),
 ("t02", 0, G+"g08.png", {"temp": "N08 Mom 2 talking take"}),
 ("t03", 0, G+"g09.png", {"temp": "N09 school yard"}),
 ("k16", 0, "GFX:calendar", {}),
 ("m08", 0, R+"x10_bottles.mp4", {"cap_top": True}),
 ("m08", 11, LIB+"RootOut-90-flatlay-v3.jpg", {"fit": "pad", "bg": (238, 244, 250)}),   # money back
]
HOOK = {
 "H1": [("k01", 0, "SLATE:N01 boy on his bed, holding his foot", {"temp": "N01"}), ("k02", 0, G+"g02.png", {"temp": "N02 car back seat"})],
 "H2": [("k03", 0, G+"g10.png", {"temp": "N10 boy runs, foot on its edge"}), ("k04", 0, R+"b61_shelf.mp4", {})],
 "H3": [("k05", 0, "SLATE:N01 boy on his bed, holding his foot", {"temp": "N01"}), ("k06", 0, R+"b05_back.mp4", {"in": 0.5})],
}
TITLE = {"H1": "Never again.", "H2": "Like a pebble when I run.", "H3": "They said it would go away."}
END = 2.6

def sh(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())

def align(h):
    """script words -> times, using the whisper transcript of the VO track."""
    lines = json.load(open(f"work/lines_{h}.json")); ww = json.load(open(f"work/tr_{h}.json"))["words"]
    out = {}
    for L in lines["lines"]:
        sw = SCRIPT[L["id"]].split()
        spoken = []  # (script index, normalized spoken token)
        for i, w in enumerate(sw):
            for t in SAY.get(norm(w), norm(w)).split(): spoken.append((i, norm(t)))
        tw = [x for x in ww if L["s"] - 0.35 <= (x["s"] + x["e"]) / 2 <= L["e"] + 0.1]
        sm = difflib.SequenceMatcher(None, [s for _, s in spoken], [norm(x["w"]) for x in tw], autojunk=False)
        st = [None] * len(sw); en = [None] * len(sw)
        for a, b, n in sm.get_matching_blocks():
            for k in range(n):
                i = spoken[a + k][0]; x = tw[b + k]
                st[i] = x["s"] if st[i] is None else st[i]; en[i] = x["e"]
        st[0] = L["s"] if st[0] is None else max(st[0], L["s"]); en[-1] = L["e"] if en[-1] is None else en[-1]
        # interpolate gaps
        known = [i for i in range(len(sw)) if st[i] is not None]
        for i in range(len(sw)):
            if st[i] is None:
                a = max(k for k in known if k < i); b = min([k for k in known if k > i] or [len(sw)])
                t0 = en[a] or st[a]; t1 = st[b] if b < len(sw) else L["e"]
                st[i] = t0 + (t1 - t0) * (i - a) / (b - a); en[i] = st[i] + (t1 - t0) / (b - a) * 0.9
            if en[i] is None: en[i] = st[i] + 0.25
        out[L["id"]] = {"s": L["s"], "e": L["e"], "words": [{"w": sw[i], "s": round(st[i], 3), "e": round(en[i], 3)} for i in range(len(sw))]}
    return lines["total"], out

def text_png(path, txt, size=54, box=True):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img); f = ImageFont.truetype(FONT_S, size)
    tw = d.textlength(txt, font=f); x, y = 40, 40
    if box: d.rounded_rectangle([x - 16, y - 10, x + tw + 16, y + size + 16], 14, fill=(0, 0, 0, 150))
    d.text((x, y), txt, font=f, fill=(255, 220, 80)); img.save(path)

def calendar_frames(path, n):
    """split frame: phone calendar 'Wart freeze 3:15' deleted (left) + bottle and dot (right)."""
    bottle = Image.open(LIB + "A12-duo-transparent.png").convert("RGBA")
    os.makedirs(path, exist_ok=True)
    fb = ImageFont.truetype(FONT_B, 54); fs = ImageFont.truetype(FONT_S, 40)
    for k in range(n):
        p = k / max(1, n - 1)
        img = Image.new("RGB", (W, H), (24, 26, 33)); d = ImageDraw.Draw(img)
        # left half: phone calendar
        d.rounded_rectangle([40, 360, 520, 1560], 50, fill=(250, 250, 252))
        d.text((90, 430), "Thursday", font=fs, fill=(200, 60, 50)); d.text((90, 480), "14", font=ImageFont.truetype(FONT_B, 120), fill=(20, 20, 25))
        for i, hh in enumerate(["2 PM", "3 PM", "4 PM", "5 PM"]):
            d.text((80, 720 + i * 190), hh, font=ImageFont.truetype(FONT_S, 28), fill=(150, 150, 160)); d.line([170, 735 + i * 190, 500, 735 + i * 190], fill=(225, 225, 230), width=2)
        a = 1 - min(1, max(0, (p - 0.45) / 0.3))   # event fades out after the swipe
        if a > 0:
            off = int(-400 * max(0, (p - 0.35) / 0.3)) if p > 0.35 else 0
            ev = Image.new("RGBA", (330, 150), (90, 140, 230, int(255 * a))); de = ImageDraw.Draw(ev)
            de.text((18, 22), "Wart freeze", font=ImageFont.truetype(FONT_B, 36), fill=(255, 255, 255, int(255 * a)))
            de.text((18, 80), "3:15", font=ImageFont.truetype(FONT_S, 32), fill=(255, 255, 255, int(255 * a)))
            img.paste(ev, (175 + off, 930), ev)
        if 0.25 < p < 0.6:  # thumb
            tx = int(440 - 380 * (p - 0.25) / 0.35); d.ellipse([tx, 960, tx + 110, 1100], fill=(226, 180, 150))
        # right half: bottle under lamp light + clear dot
        glow = Image.new("RGB", (520, 1200), (60, 45, 30)); img.paste(glow, (560, 360))
        b = bottle.copy(); b.thumbnail((470, 900)); img.paste(b, (560 + (520 - b.width) // 2, 520), b)
        d.ellipse([760, 1420, 880, 1540], outline=(230, 235, 240), width=6)
        img.save(f"{path}/{k:04d}.png")

def end_frames(path, n):
    bottle = Image.open(LIB + "A01-bottle-front-white.jpg").convert("RGB")
    os.makedirs(path, exist_ok=True)
    for k in range(n):
        p = k / max(1, n - 1)
        img = Image.new("RGB", (W, H), (250, 244, 236)); d = ImageDraw.Draw(img)
        b = bottle.copy(); s = 1.0 + 0.04 * p; bw = int(620 * s); b = b.resize((bw, int(bw * bottle.height / bottle.width)))
        img.paste(b, ((W - bw) // 2, 430))
        f = ImageFont.truetype(FONT_B, 92); t = "Not the top."; d.text(((W - d.textlength(t, font=f)) / 2, 150), t, font=f, fill=NAVY)
        t = "The root."; d.text(((W - d.textlength(t, font=f)) / 2, 260), t, font=f, fill=BLUE)
        # snapped vs whole dandelion icon
        cx = W // 2; y = 1500
        for dx, whole in ((-170, False), (170, True)):
            x = cx + dx; d.ellipse([x - 34, y - 34, x + 34, y + 34], fill=(240, 190, 30)); d.line([x, y + 34, x, y + 150], fill=(90, 150, 60), width=8)
            d.line([x - 80, y + 150, x + 80, y + 150], fill=(150, 110, 70), width=6)
            if whole: d.line([x, y + 150, x, y + 290], fill=(235, 230, 215), width=10); d.line([x, y + 220, x - 30, y + 280], fill=(235, 230, 215), width=6)
            else: d.line([x - 22, y + 82, x + 22, y + 70], fill=(200, 60, 50), width=6)
        f2 = ImageFont.truetype(FONT_B, 54); t = "Buy 2, get 1 free"
        bw2 = d.textlength(t, font=f2); d.rounded_rectangle([(W - bw2) / 2 - 40, 1810 - 70, (W + bw2) / 2 + 40, 1810 + 10], 40, fill=ORANGE)
        d.text(((W - bw2) / 2, 1810 - 62), t, font=f2, fill=(255, 255, 255))
        img.save(f"{path}/{k:04d}.png")

def seg(i, src, o, L, out):
    vf_fit = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
    z = o.get("zoom", 1.0)
    if z != 1.0: vf_fit = f"scale={int(W*z)}:{int(H*z)}:force_original_aspect_ratio=increase,crop={W}:{H}"
    if src.startswith("SLATE:"):
        t = src[6:]; img = Image.new("RGB", (W, H), (30, 32, 40)); d = ImageDraw.Draw(img); f = ImageFont.truetype(FONT_S, 50)
        y = 820
        for line in ["TO GENERATE", t]:
            d.text(((W - d.textlength(line, font=f)) / 2, y), line, font=f, fill=(200, 200, 210)); y += 80
        img.save(f"work/seg/slate{i}.png"); src = f"work/seg/slate{i}.png"
    if src.startswith("GFX:calendar"):
        n = int(L * FPS) + 1; calendar_frames(f"work/seg/cal{i}", n)
        sh(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i",f"work/seg/cal{i}/%04d.png","-t",f"{L:.3f}","-pix_fmt","yuv420p","-c:v","libx264","-crf","18","-r",str(FPS),out]); return
    if src.lower().endswith((".png", ".jpg")):
        if o.get("fit") == "pad":
            bg = o.get("bg", "white"); bg = "#%02x%02x%02x" % bg if isinstance(bg, tuple) else bg
            pre = f"scale={W-120}:-2,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={bg}"
        else: pre = vf_fit
        frames = int(L * FPS) + 1
        vf = f"{pre},scale={W*2}:{H*2},zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}"
        sh(["ffmpeg","-v","error","-y","-loop","1","-i",src,"-vf",vf,"-t",f"{L:.3f}","-pix_fmt","yuv420p","-c:v","libx264","-crf","18","-r",str(FPS),out]); return
    inn = o.get("in", 0.0); avail = dur(src) - inn - 0.05
    speed = 1.0
    if avail < L: speed = max(0.75, avail / L)      # slow to fit, never below 0.75x (L4)
    pts = f"setpts={1/speed:.4f}*(PTS-STARTPTS)"
    vf = f"trim=start={inn},{pts},{vf_fit},fps={FPS},tpad=stop_mode=clone:stop_duration=2"   # clone pad only if still short (flagged)
    sh(["ffmpeg","-v","error","-y","-i",src,"-vf",vf,"-an","-t",f"{L:.3f}","-pix_fmt","yuv420p","-c:v","libx264","-crf","18","-r",str(FPS),out])
    if avail / 0.75 < L - 0.05: print(f"  ! {os.path.basename(src)} short by {L - avail/0.75:.2f}s (freeze pad)")

def ass_time(t): h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60; return f"{h}:{m:02d}:{s:05.2f}"

def captions(words_by_line, shots_cap_top, total, path):
    """bold word-by-word captions, 2-4 word groups, active word highlighted (L5)."""
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter Black,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,70,70,560,1
Style: CapTop,Inter Black,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,8,70,70,300,1
Style: Title,Inter Black,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,3,18,0,8,60,60,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    for lid, L in words_by_line.items():
        ws = L["words"]; groups = []; cur = []
        for w in ws:
            cur.append(w)
            if len(cur) >= 3 or w["w"][-1] in ".,!?" and len(cur) >= 1: groups.append(cur); cur = []
        if cur: groups.append(cur)
        for gi, g in enumerate(groups):
            g_end = groups[gi + 1][0]["s"] if gi + 1 < len(groups) else g[-1]["e"] + 0.15
            for k, w in enumerate(g):
                s = w["s"]; e = g[k + 1]["s"] if k + 1 < len(g) else g_end
                txt = " ".join(("{\\c&H2FD4FF&}" + x["w"].upper() + "{\\c&HFFFFFF&}") if j == k else x["w"].upper() for j, x in enumerate(g))
                style = "CapTop" if any(a <= s < b for a, b in shots_cap_top) else "Cap"
                ev.append(f"Dialogue: 1,{ass_time(s)},{ass_time(max(e, s + 0.05))},{style},,0,0,0,,{txt}")
    open(path, "w").write(head + "\n".join(ev) + "\n")

def build(h, ver):
    total, A = align(h); os.makedirs("work/seg", exist_ok=True); os.makedirs("out", exist_ok=True)
    shots = HOOK[h] + BODY
    cues = [A[l]["words"][wi]["s"] if (l, wi) != (shots[0][0], 0) else 0.0 for l, wi, _, _ in shots]
    cues[0] = 0.0
    ends = cues[1:] + [total + 0.25]
    files = []; temps = []; cap_top = []; edl = []
    for i, ((l, wi, src, o), s, e) in enumerate(zip(shots, cues, ends)):
        L = e - s; out = f"work/seg/{h}_{i:02d}.mp4"; seg(i, src, o, L, out); files.append(out)
        if "temp" in o: temps.append((s, e, "TEMP " + o["temp"]))
        if o.get("cap_top") or o.get("fit") == "pad": cap_top.append((s, e))
        edl.append({"i": i, "t": round(s, 2), "len": round(L, 2), "line": l, "cue": SCRIPT[l].split()[wi], "src": os.path.basename(src)})
        if not (1.4 <= L <= 4.6): print(f"  ~ shot {i} {os.path.basename(src)} is {L:.2f}s")
    # end card
    n = int(END * FPS); end_frames("work/seg/end", n)
    sh(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i","work/seg/end/%04d.png","-t",f"{END}","-pix_fmt","yuv420p","-c:v","libx264","-crf","18","-r",str(FPS),f"work/seg/{h}_end.mp4"])
    files.append(f"work/seg/{h}_end.mp4")
    open(f"work/seg/{h}_list.txt", "w").write("".join(f"file '{os.path.basename(f)}'\n" for f in files))
    sh(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"work/seg/{h}_list.txt","-c","copy",f"work/{h}_video.mp4"])
    vlen = dur(f"work/{h}_video.mp4")
    captions(A, cap_top, total, f"work/{h}.ass")
    # temp tags + hook title overlays
    ov = []; inputs = ["-i", f"work/{h}_video.mp4"]
    for k, (s, e, t) in enumerate(temps):
        p = f"work/seg/tag_{h}_{k}.png"; text_png(p, t, 40); inputs += ["-i", p]; ov.append((s, e))
    hook_end = A[shots[1][0]]["s"]  # title over the hook line
    fc = f"[0:v]ass=work/{h}.ass:fontsdir=/usr/share/fonts/opentype/inter[v0];"
    last = "v0"
    for k, (s, e) in enumerate(ov):
        fc += f"[{last}][{k+1}:v]overlay=0:0:enable='between(t,{s:.2f},{e:.2f})'[v{k+1}];"; last = f"v{k+1}"
    # title as drawtext box (Title style via a separate ass event)
    open(f"work/{h}_title.ass", "w").write(open(f"work/{h}.ass").read().split("[Events]")[0] + "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n" +
        f"Dialogue: 2,{ass_time(0)},{ass_time(hook_end)},Title,,0,0,0,,{TITLE[h]}\n")
    fc += f"[{last}]ass=work/{h}_title.ass:fontsdir=/usr/share/fonts/opentype/inter[vout];"
    # audio: VO + music bed, ducked under voice, lifted on the end card, short fade on the last frame (L6)
    vo = f"work/vo_{h}.wav"; inputs += ["-i", vo, "-i", "raw/music/bed.mp3"]
    ia, im = len(ov) + 1, len(ov) + 2
    fc += (f"[{ia}:a]apad=whole_dur={vlen},loudnorm=I=-16:TP=-2:LRA=7,asplit=2[vo][sc];"
           f"[{im}:a]atrim=0:{vlen},asetpts=PTS-STARTPTS,volume=0.32,volume='if(gt(t,{total:.2f}),1.8,1)':eval=frame[mu];"
           f"[mu][sc]sidechaincompress=threshold=0.04:ratio=5:attack=20:release=350[mud];"
           f"[vo][mud]amix=inputs=2:normalize=0,afade=t=out:st={vlen-0.6:.2f}:d=0.6,alimiter=limit=0.89[aout]")
    out = f"out/ROS1B_{h}_preview_v{ver}.mp4"
    sh(["ffmpeg","-v","error","-y"] + inputs + ["-filter_complex", fc, "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-crf", "26", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "160k", "-t", f"{vlen:.3f}", "-movflags", "+faststart", out])
    json.dump(edl, open(f"work/edl_{h}.json", "w"), indent=1)
    print(h, "->", out, f"{vlen:.1f}s")

if __name__ == "__main__":
    a = sys.argv[1:]; ver = a[a.index("--version") + 1] if "--version" in a else "1"
    for h in [x for x in a if x.startswith("H")]: build(h, ver)
