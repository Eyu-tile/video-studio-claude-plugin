#!/usr/bin/env python3
"""Final pass: animated overlays at their line times (hook, plant list, routine steps, product callout, CTA),
phone-camera finish, loudnorm. No captions, no footnotes on b-roll. Usage: finish17.py h1 v2"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent; hook, ver = (sys.argv[1:] + ["h1", "v2"])[:2]
vo = dict(json.load(open(P / "work" / f"{hook}_vo_times.json")))
ov = [(f"hook_{hook}", 0.0), ("plants", vo["L14"]), ("steps", vo["L16fix"]), ("callout", vo["L17"] + 2.45), ("cta", vo["L18"] + 2.6)]
ins = [f"-i work/{hook}_video.mp4", f"-i work/{hook}_audio.wav"] + [f"-itsoffset {t:.3f} -i work/ov/{n}.mov" for n, t in ov]
fc = "[0]null[v0]"
for k, (n, t) in enumerate(ov):
    fc += f";[v{k}][{k+2}]overlay=0:0:eof_action=pass[v{k+1}]"
fc += f";[v{len(ov)}]scale=1080:1920:flags=lanczos,rgbashift=rh=1:bh=-1,noise=c0s=6:c0f=t+u,vignette=angle=PI/5:mode=forward,unsharp=3:3:0.25,format=yuv420p[v]"
fc += ";[1]loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false[a]"
out = P / f"out/WilloMD_RootOut_Set17_{hook.upper()}_9x16_{ver}.mp4"
cmd = (f"ffmpeg -v error -y {' '.join(ins)} -filter_complex \"{fc}\" -map [v] -map [a] -c:v libx264 -preset slow -crf 20 "
       f"-maxrate 9M -bufsize 18M -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart -map_metadata -1 -shortest {out}")
subprocess.run(cmd, shell=True, check=True, cwd=P); print(out)
