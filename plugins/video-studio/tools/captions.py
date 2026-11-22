#!/usr/bin/env python3
"""Build captions on the EDITED timeline from a word transcript + EDL.

Writes an ASS file for burning in (render.py --captions) and an SRT for
platform upload. Words are remapped through the EDL, so captions stay in
sync after cuts. Positions respect platform safe zones.

Styles:
  bold-pop  1-3 words, uppercase, active word in accent colour (short-form / Reels / TikTok)
  clean     sentence chunks on a soft box, bottom third (YouTube, LinkedIn, explainers)
  minimal   small, lower-case-friendly, thin outline (calm/brand films)

Usage:
  vs captions work/transcript.json work/edl.json -o work/captions --style bold-pop --aspect 9:16 --accent "#FFD400"
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import ASPECTS, HARD_FILLERS, is_image, load_json, norm_word, save_json, timeline  # noqa: E402



def ass_color(hex_rgb, alpha=0):
    h = hex_rgb.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return f"&H{alpha:02X}{b}{g}{r}".upper()


def ass_ts(t):
    t = max(t, 0)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def srt_ts(t):
    t = max(t, 0)
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def remap(words, edl, tsrc, keep_fillers=False):
    """Map source word times onto the output timeline (speed and transitions included).
    Words outside kept segments are dropped; segments from other sources only advance the clock."""
    out = []
    track = edl.get("audio_track") or {}
    via_track = track.get("follow") and Path(track["src"]).resolve() == Path(tsrc).resolve()
    for it in timeline(edl):
        if via_track and "ref" in it["seg"]:
            # Multicam: the transcript is of the shared mix; map through each segment's reference range.
            off = float(track.get("offset", 0))
            a, b = it["seg"]["ref"][0] + off, it["seg"]["ref"][1] + off
        elif is_image(it["src"]) or Path(it["src"]).resolve() != Path(tsrc).resolve():
            continue
        else:
            a, b = it["start"], it["end"]
        sp, o = it["speed"], it["out_start"]
        for w in words:
            if w["s"] >= a - 0.02 and w["e"] <= b + 0.02 and (keep_fillers or norm_word(w["w"]) not in HARD_FILLERS):
                out.append({"w": w["w"], "s": o + max(w["s"] - a, 0) / sp, "e": o + (min(w["e"], b) - a) / sp,
                            "filler": norm_word(w["w"]) in HARD_FILLERS})
    out.sort(key=lambda w: w["s"])
    return out


def chunk(words, max_words, max_chars, pause=0.4):
    cur = []
    for i, w in enumerate(words):
        if cur:
            gap = w["s"] - cur[-1]["e"]
            text_len = sum(len(x["w"]) + 1 for x in cur) + len(w["w"])
            if (len(cur) >= max_words or text_len > max_chars or gap > pause
                    or cur[-1]["w"].endswith((".", "?", "!", ","))):
                yield cur
                cur = []
        cur.append(w)
    if cur:
        yield cur


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("transcript")
    ap.add_argument("edl", help="EDL the video is rendered from (use the same one!)")
    ap.add_argument("-o", "--out", required=True, help="output path without extension")
    ap.add_argument("--style", choices=["bold-pop", "clean", "minimal", "karaoke"], default="clean")
    ap.add_argument("--preset", help="platform preset name; sets --aspect (reels, shorts, youtube, ...)")
    ap.add_argument("--aspect", choices=list(ASPECTS), default="16:9", help="must match render.py --aspect")
    ap.add_argument("--font", default="Inter", help="font family (must be installed / fontconfig)")
    ap.add_argument("--accent", default="#FFD400", help="highlight colour (use your brand colour from style/brand.md)")
    ap.add_argument("--text-color", default="#FFFFFF")
    ap.add_argument("--max-words", type=int)
    args = ap.parse_args()

    if args.preset:
        from vs_common import PRESETS
        args.aspect = PRESETS[args.preset]["aspect"]
    W, H = ASPECTS[args.aspect]
    vertical = H > W
    t = load_json(args.transcript)
    words = remap(t["words"], load_json(args.edl), t["source"])
    base = min(W, H)

    if args.style == "bold-pop":
        size, mw, mc, bold, upper = int(base * 0.075), args.max_words or 3, 18, -1, True
        border, outline, shadow, back = 1, max(base // 160, 4), 0, ass_color("#000000", 0x00)
        margin_v = int(H * (0.30 if vertical else 0.14))
        align = 2
    elif args.style == "clean":
        size, mw, mc, bold, upper = int(base * 0.052), args.max_words or 8, 42, -1, False
        border, outline, shadow, back = 3, max(base // 90, 8), 0, ass_color("#000000", 0x60)
        margin_v = int(H * (0.22 if vertical else 0.07))
        align = 2
    elif args.style == "karaoke":
        size, mw, mc, bold, upper = int(base * 0.058), args.max_words or 6, 32, -1, False
        border, outline, shadow, back = 1, max(base // 150, 4), 0, ass_color("#000000", 0x00)
        margin_v = int(H * (0.24 if vertical else 0.08))
        align = 2
    else:
        size, mw, mc, bold, upper = int(base * 0.040), args.max_words or 7, 40, 0, False
        border, outline, shadow, back = 1, 2, 0, ass_color("#000000", 0x80)
        margin_v = int(H * (0.20 if vertical else 0.06))
        align = 2
    # Vertical: keep clear of right-rail icons and the caption/UI band at the bottom.
    margin_l = int(W * 0.08)
    margin_r = int(W * (0.16 if vertical else 0.08))
    from vs_common import safe_zone
    sz = safe_zone(args.preset, args.aspect)
    if sz:  # platform UI: never let captions sit under it
        margin_v = max(margin_v, int(H * (sz["bottom"] + 0.02)))
        margin_l = max(margin_l, int(W * (sz["left"] + 0.02)))
        margin_r = max(margin_r, int(W * (sz["right"] + 0.02)))

    txt, acc = ass_color(args.text_color), ass_color(args.accent)
    # Karaoke fills from SecondaryColour (not yet spoken) to PrimaryColour (spoken).
    prim, sec = (acc, txt) if args.style == "karaoke" else (txt, acc)
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{args.font},{size},{prim},{sec},{ass_color('#000000')},{back},{bold},0,0,0,100,100,0,0,{border},{outline},{shadow},{align},{margin_l},{margin_r},{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events, srt = [], []
    chunks = list(chunk(words, mw, mc))
    for ci, c in enumerate(chunks):
        start = c[0]["s"]
        # Hold until the next chunk starts (max +0.6s) so captions don't flicker off between words.
        nxt = chunks[ci + 1][0]["s"] if ci + 1 < len(chunks) else c[-1]["e"] + 0.6
        end = min(nxt, c[-1]["e"] + 0.6)
        end = max(end, min(start + 0.3, nxt))
        toks = [(w["w"].upper() if upper else w["w"]).replace("{", "(").replace("}", ")") for w in c]
        srt.append(f"{len(srt) + 1}\n{srt_ts(start)} --> {srt_ts(end)}\n{' '.join(t.strip() for t in toks)}\n")
        if args.style == "bold-pop":
            for k, w in enumerate(c):
                ws = w["s"] if k else start
                we = c[k + 1]["s"] if k + 1 < len(c) else end
                line = " ".join(
                    (f"{{\\c{acc}\\fscx108\\fscy108}}{t}{{\\c{txt}\\fscx100\\fscy100}}" if j == k else t)
                    for j, t in enumerate(toks))
                pop = "{\\fad(40,0)}" if k == 0 else ""
                events.append(f"Dialogue: 0,{ass_ts(ws)},{ass_ts(we)},Cap,,0,0,0,,{pop}{line}")
        elif args.style == "karaoke":
            # Words fill from text colour to accent as they are spoken (\\kf = smooth fill, centiseconds).
            parts, t = [], start
            for w, tok in zip(c, toks):
                lead = max(w["s"] - t, 0)
                if lead > 0.01:
                    parts.append(f"{{\\k{int(lead * 100)}}}")
                parts.append(f"{{\\kf{max(int((w['e'] - max(w['s'], t)) * 100), 1)}}}{tok} ")
                t = max(w["e"], t)
            events.append(f"Dialogue: 0,{ass_ts(start)},{ass_ts(end)},Cap,,0,0,0,,{''.join(parts).rstrip()}")
        else:
            events.append(f"Dialogue: 0,{ass_ts(start)},{ass_ts(end)},Cap,,0,0,0,,{{\\fad(80,80)}}{' '.join(toks)}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".ass").write_text(header + "\n".join(events) + "\n", encoding="utf-8")
    out.with_suffix(".srt").write_text("\n".join(srt), encoding="utf-8")
    # how these captions were made, so `vs fix --render` can remake them after an edit with the same look
    save_json(out.with_suffix(".captions.json"), {"argv": sys.argv[1:], "cwd": os.getcwd()})
    print(f"{len(chunks)} caption cards ({args.style}, {W}x{H}) -> {out.with_suffix('.ass')}, {out.with_suffix('.srt')}")


if __name__ == "__main__":
    main()
