#!/usr/bin/env python3
"""Mix + finish one hook: voice + ambience bed + music (Carefree, Kevin MacLeod, CC BY 4.0) ducked under the voice,
hook text (On screen, from the brief) for the first seconds, bold-pop captions, phone-camera finish, loudnorm.
Usage: python3 work/finish.py H1 [version]"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent
h = sys.argv[1]; ver = sys.argv[2] if len(sys.argv) > 2 else "v1"
B = P / f"work/build/{h}"; TL = json.load(open(B / "timeline.json")); L = TL["length"]
HOOK = {"H1": "I was bleaching the tub\nafter every bath…", "H2": "I was sure they caught it\nat the pool.",
        "H3": "He only goes barefoot\nat home.", "H4": ""}[h]
HOOK_END = TL["pieces"][0][4] + (TL["pieces"][0][3] - TL["pieces"][0][2])  # end of row-1 piece
out = P / f"out/WilloMD_RootOut_Set19_{h}_9x16_{ver}.mp4"; out.parent.mkdir(exist_ok=True)
font = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
hookf = B / "hook.txt"; hookf.write_text(HOOK)
vf = ("rgbashift=rh=1:bh=-1,noise=c0s=6:c0f=t+u,vignette=angle=PI/5:mode=forward,unsharp=3:3:0.25,"
      f"ass={B / 'captions.ass'}:fontsdir={P / 'assets/fonts'}")
if HOOK:
    vf += (f",drawtext=fontfile={font}:textfile={hookf}:fontsize=62:line_spacing=14:fontcolor=black:x=(w-tw)/2:y=250:"
           f"box=1:boxcolor=white@0.96:boxborderw=26:enable='lt(t,{min(HOOK_END, 4.5):.2f})'")
music = P / "assets/music/Carefree.mp3"
fc = ("[1:a]volume=0.18[amb];"
      f"[2:a]aloop=loop=-1:size=2e9,atrim=0:{L:.3f},volume=0.33,afade=t=in:d=1.5,afade=t=out:st={L - 2.5:.3f}:d=2.5[mus];"
      "[0:a]asplit=2[v1][v2];[mus][v2]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[duck];"
      "[v1][amb][duck]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(B / "voice.wav"), "-i", str(B / "amb.wav"), "-i", str(music), "-i", str(B / "video.mp4"),
                "-filter_complex", fc + f";[3:v]{vf}[v]", "-map", "[v]", "-map", "[a]", "-t", f"{L:.3f}",
                "-c:v", "libx264", "-preset", "slow", "-crf", "21", "-maxrate", "10M", "-bufsize", "20M", "-pix_fmt", "yuv420p",
                "-ar", "48000", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-map_metadata", "-1", str(out)], check=True)
print("->", out)
