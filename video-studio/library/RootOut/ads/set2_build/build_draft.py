#!/usr/bin/env python3
"""Set 2 draft timeline (no VO yet): reused WilloMd clips + the narrator take T1 + labelled cards for shots still to
generate. Timing = script words at 2.4 w/s (+0.25 s per phrase); T1 keeps its real length and native audio.
Guide captions show each phrase (the final cut uses word-by-word captions on the recorded voice).

Usage: python3 -I build_draft.py   ->  projects/rootout-set2/out/Set2_H1_draft_v1.mp4 + draft_report.md
"""
import json, subprocess, textwrap, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4] / "projects" / "rootout-set2"
RAW, WORK, OUT = ROOT / "raw", ROOT / "work" / "draft", ROOT / "out"
WORK.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 720, 1280, 30
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
WPS, GAP, MIN_SPEED = 2.4, 0.25, 0.75

# (shot, VO phrase, kind, source, in-point s, note)   kind: R reuse · T take · P to generate · C code card
SHOTS = [
 ("01", "We gave three kids with warts a different fix for two weeks.", "P", "N 5 s: three kids' bare feet side by side on a living-room rug, blue / yellow / green socks beside them, slow pan", 0, ""),
 ("03", "A freeze kit. Acid pads. And RootOut.", "R", "s4_P1_lineup", 0, "b5365ce0"),
 ("04", "Freezing, pads, acid, clippers. You've tried at least one. It grew back.", "T", "takes/T1_row2.mp4", 0, "ad56e80b narrator T1"),
 ("05", "Here's what we saw.", "C", "calendar", 0, "code: paper calendar flips to day 1"),
 ("06", "Night one. Kid one, a wart on his foot, got the freeze kit. He cried.", "P", "N 4 s: BLUE socks, boy's foot side-on on a parent's knee, freeze spray puff on the sole, his hand grips the chair", 0, ""),
 ("08", "Kid two got an acid pad.", "P", "S still: YELLOW socks, parent presses a round acid pad onto a girl's sole", 0, ""),
 ("09", "Kid three, a wart on her finger, got RootOut at bedtime. She didn't fight it.", "P", "N 4 s: GREEN socks on the bed, warm lamp, real bottle on the duvet, picture book, toes relax", 0, ""),
 ("11", "Week one. Kid one had a blister. The wart was still under it.", "P", "S still: BLUE sock pulled down, pale blister over the spot, wart edge showing", 0, ""),
 ("12", "Kid two's pad slid off by lunch, every day.", "P", "S still: YELLOW sock peeled off, the round pad stuck inside the sock", 0, ""),
 ("13", "Kid three's dot stayed on all night.", "P", "S still: GREEN sock, morning light, clear dot still on the sole", 0, ""),
 ("14", "Two weeks. Kid one's wart grew back.", "P", "S still: BLUE sock, the same rough wart back", 0, ""),
 ("15", "Kid two's skin went white. The wart stayed.", "P", "S still: YELLOW sock, macro, ring of soggy white skin around the wart", 0, ""),
 ("16", "Kid three's spot", "R", "s4_B18_smoothsole", 0, "0bd6fdf0 (stand-in until the green-sock still)"),
 ("17", "was gone.", "R", "s1_hallway", 0, "e73e0ad5"),
 ("18", "So why did only one work?", "P", "T 4 s: narrator to camera, RootOut bottle alone on the table", 0, ""),
 ("19", "Freezing, acid and shaving only snap off the top,", "R", "s4_D2_toponly", 0, "41c510bb"),
 ("20", "like picking a dandelion.", "R", "s1_dand_snap", 0.5, "3e99af22"),
 ("21", "The root stays under the hard skin,", "R", "s17_soil_cutaway", 0, "ee317059"),
 ("22", "so it grows back.", "R", "s1_dand_back", 0, "644d4a63"),
 ("23a", "Kid three used RootOut.", "R", "s4_P2_slidein", 0, "7df26a04"),
 ("23b", "It's an oil with four plants.", "R", "s4_P4_flatlay", 0, "c9a3a938"),
 ("24a", "The lemon softens that hard skin on top,", "R", "s4_B14_lemon", 0, "ad286b2b"),
 ("24b", "so the rest can get in.", "R", "s4_D4_lemon3d", 1.0, "f1cf23e1"),
 ("25a", "The tea tree is a thin oil.", "R", "s4_B15_teatree", 0, "e20edf28"),
 ("25b", "It sinks in,", "R", "s4_D5_sink", 0.8, "c8b506d4"),
 ("26", "up to 8x deeper than a regular cream,", "R", "s1_towels", 0, "ce962fe0 + code 8x gauge"),
 ("27", "and carries the pokeweed and white cedar down with it.", "R", "s4_D6_carry", 0, "e1c706fd"),
 ("28a", "Then those two", "R", "s4_B16_pokeweed", 0, "b6cdaa58"),
 ("28b", "break the wart down from the root,", "R", "s4_D7_crumble", 0, "3ca33dac"),
 ("28c", "so it can't grow back.", "R", "s17_x6_root", 2.5, "692c7031"),
 ("29a", "One alone can't do that.", "R", "s4_D3_rootstill", 0, "8f469553"),
 ("29b", "Together, they get all the way down.", "R", "s4_D8_together", 1.0, "d8d2be71"),
 ("30", "And the clear dot keeps them in all night.", "R", "s4_D9_clean", 0, "80da1c88 + code clock 9 pm to 5 am"),
 ("31a", "Deep doesn't mean harsh.", "R", "s4_P5_nightbook", 0, "2ca62c5c"),
 ("31b", "It's a kids' formula, ages 4 and up.", "R", "s20_socks_bed", 0, "5100f730"),
 ("32", "No acid, no freezing, no blister.", "R", "s4_B17_bin", 0, "cc05bcb3"),
 ("33", "Just a little cool tingle.", "R", "s17_b2_routine", 2.0, "13cd338e"),
 ("34", "Recommended by pediatricians.", "R", "s4_P3_hero", 0, "7a84c998"),
 ("35", "MOM 2: I tried it on my own hand first. Cool for a second. No sting at all.", "P", "T 6 s: MOM 2 (rust tee, kitchen) to camera holding the real bottle", 0, ""),
 ("36", "Here's what you do at bedtime.", "P", "N 4 s: GREEN-sock girl's bed at night, feet up, picture book", 0, ""),
 ("37", "Two light strokes with the file.", "R", "s20_file_kid", 0, "757ba2f9"),
 ("38", "Then you brush the oil on.", "P", "N 4 s: hand brushes oil from the real RootOut cap onto a kid's sole, bedroom", 0, ""),
 ("39", "The file only touches the hard top.", "R", "s4_B13_thumbrub", 0, "5ac712ad"),
 ("40", "Never the skin. So it doesn't hurt.", "R", "s19_dot_v2", 0, "686ace6f"),
 ("41", "MOM 1: I was scared to file his foot. Two light strokes. He didn't even look up from his show.", "P", "T 7 s: MOM 1 (sofa, plain hoodie) to camera, boy's foot on her lap, no kid face", 0, ""),
 ("42a", "When it looks gone,", "R", "s19_clear_sole", 0, "d24782f6"),
 ("42b", "keep going 14 more nights. That's the Root Rule.", "R", "s4_B20_plus14", 0, "e211dc9d"),
 ("43", "MOM 3: I kept going two more weeks after it looked gone. It hasn't come back.", "P", "T 6 s: MOM 3 (silver bob, hallway) to camera, green socks in her hand", 0, ""),
 ("44", "Warts spread. One can turn into fifteen.", "R", "s19_splash_v2", 0, "d0432c1f"),
 ("45", "Every fix that only gets the top means another round.", "P", "N 4 s: pharmacy checkout belt, freeze-kit box slides to the scanner, a hand takes it back", 0, ""),
 ("46", "You can get yours from the link below. Third bottle's on us. And if it's not gone, you get every penny back. You've got 90 days.", "P", "T 9 s: narrator slides the third real bottle into the row", 0, ""),
 ("48", "", "C", "endcard", 0, "Not the top. The root. · Buy 2, get 1 free"),
]
HOOK_TITLE = "3 kids. 3 wart fixes. 2 weeks."

def run(cmd): subprocess.run(cmd, check=True)
def dur(p): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]))
def esc(s): return s.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%").replace(",", "\\,")
def words(s): return len(s.replace("MOM 1:", "").replace("MOM 2:", "").replace("MOM 3:", "").split())

def txtfile(name, text, width):
    p = WORK / f"{name}.txt"; p.write_text("\n".join(textwrap.wrap(text, width))); return str(p)

def caption_filter(sid, text, t0):
    if not text: return ""
    f = txtfile(f"cap_{sid}", text.split(": ", 1)[-1], 24)
    return (f",drawtext=fontfile={BOLD}:textfile={f}:fontsize=40:fontcolor=black:line_spacing=8:box=1:boxcolor=white@0.94:"
            f"boxborderw=16:x=(w-text_w)/2:y=h*0.66")

def card(sid, lines, sec, bg="0x0B2A5B"):
    vf = []
    y = 380
    for txt, size, color, font in lines:
        f = txtfile(f"card_{sid}_{y}", txt, 26 if size < 50 else 16)
        vf.append(f"drawtext=fontfile={font}:textfile={f}:fontsize={size}:fontcolor={color}:line_spacing=10:x=(w-text_w)/2:y={y}")
        y += size * (txt.count(" ") // (2 if size < 50 else 1) + 3) // 2 + 60
    return f"color=c={bg}:s={W}x{H}:r={FPS}:d={sec:.3f}", ",".join(vf)

segs, report, t = [], [], 0.0
for i, (sid, text, kind, src, inpt, note) in enumerate(SHOTS):
    out = WORK / f"seg_{i:02d}_{sid}.mp4"
    flag = ""
    if kind == "T":
        p = RAW / src; sec = dur(p)
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}" + caption_filter(sid, text, t)
        run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
             "-c:a", "aac", "-ar", "48000", "-ac", "2", str(out)])
    else:
        sec = round(words(text) / WPS + GAP, 2) if text else 3.0
        if kind == "R":
            p = RAW / "reuse" / f"{src}.mp4"; avail = dur(p) - inpt; speed = 1.0
            if avail < sec:
                speed = avail / sec
                if speed < MIN_SPEED: speed = MIN_SPEED; flag = f"clip short: {avail:.1f}s at 0.75x = {avail/0.75:.1f}s < slot {sec:.1f}s, slot trimmed"; sec = round(avail / MIN_SPEED, 2)
            vf = (f"trim=start={inpt},setpts=(PTS-STARTPTS)/{speed},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                  f"fps={FPS},trim=duration={sec}") + caption_filter(sid, text, t)
            if speed < 1: flag = flag or f"slowed to {speed:.2f}x"
            run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-filter_complex",
                 f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a", "-t", f"{sec}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                 "-c:a", "aac", str(out)])
        else:
            if kind == "P":
                src_lines = [("TO GENERATE", 34, "0xE04E18", BOLD), (src, 30, "white", SEMI)]  # NB: >4 s lines get split into 2 shots once generated
            elif src == "calendar":
                src_lines = [("DAY 1", 120, "0x0B2A5B", BOLD)]
            else:
                src_lines = [("Not the top. The root.", 56, "0x0B2A5B", BOLD), ("Buy 2, get 1 free", 40, "0xE04E18", BOLD),
                             ("(end card: bottle + snapped-vs-whole dandelion icon)", 26, "0x0B2A5B", SEMI)]
            bg = "0xEEF4FA" if kind == "C" else "0x0B2A5B"
            lav, vf = card(sid, src_lines, sec, bg)
            vf += caption_filter(sid, text, t)
            run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", lav, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                 "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a", "-t", f"{sec}", "-c:v", "libx264", "-preset",
                 "veryfast", "-crf", "23", "-c:a", "aac", str(out)])
    segs.append(out)
    report.append((sid, round(t, 2), round(t + sec, 2), kind, src if kind != "P" else "TO GENERATE", note, flag, text))
    t += sec

# concat + hook title (first 3 s) + DRAFT corner tag
lst = WORK / "list.txt"; lst.write_text("".join(f"file '{s}'\n" for s in segs))
joined = WORK / "joined.mp4"
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(joined)])
hf = txtfile("hook", HOOK_TITLE, 20); tag = txtfile("tag", "DRAFT v1 · no VO yet", 30)
vf = (f"drawtext=fontfile={BOLD}:textfile={hf}:fontsize=46:fontcolor=white:box=1:boxcolor=0xE04E18:boxborderw=18:"
      f"x=(w-text_w)/2:y=h*0.12:enable='lt(t,3)',"
      f"drawtext=fontfile={SEMI}:textfile={tag}:fontsize=22:fontcolor=white@0.85:box=1:boxcolor=black@0.45:boxborderw=8:x=16:y=16")
final = OUT / "Set2_H1_draft_v1.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(joined), "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
     "-c:a", "aac", "-movflags", "+faststart", str(final)])

used = [r[4] for r in report if r[3] == "R"]
dups = sorted({u for u in used if used.count(u) > 1})
md = ["# Set 2 · H1 draft v1 timeline", "", f"Total {t:.1f} s · {len(report)} shots · "
      f"{sum(r[3]=='R' for r in report)} reused · {sum(r[3]=='T' for r in report)} take · "
      f"{sum(r[3]=='P' for r in report)} to generate · {sum(r[3]=='C' for r in report)} code cards · duplicate sources: {dups or 'none'}", "",
      "| # | in | out | kind | source | note | flag | VO |", "|---|---|---|---|---|---|---|---|"]
md += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |" for r in report]
(pathlib.Path(__file__).parent / "DRAFT_TIMELINE.md").write_text("\n".join(md) + "\n")
print(final, f"{t:.1f}s", "dups:", dups)
