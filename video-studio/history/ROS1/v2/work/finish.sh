#!/bin/bash
# Phone-camera finish (luma grain, faint lens fringe, soft vignette, light sharpening) under burned-in captions.
set -e; h=$1; H=$(echo $h | tr a-z A-Z); cd "$(dirname "$0")/.."
ffmpeg -y -v error -i out/set1_${h}_v2raw.mp4 -vf "rgbashift=rh=1:bh=-1,noise=c0s=7:c0f=t+u,vignette=angle=PI/5:mode=forward,unsharp=3:3:0.25,ass=work/captions_${h}.ass:fontsdir=assets/fonts" \
  -c:v libx264 -preset slow -crf 23 -maxrate 9M -bufsize 18M -pix_fmt yuv420p -af loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false -ar 48000 -c:a aac -b:a 192k -movflags +faststart -map_metadata -1 \
  out/WilloMD_RootOut_Set1_${H}_9x16_v2.mp4
