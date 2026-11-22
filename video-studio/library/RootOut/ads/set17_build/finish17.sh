#!/bin/bash
# Hook text (0.3-7.6 s), phone-camera finish (grain, faint fringe, vignette, light sharpen), loudnorm. No captions (owner: hook + end card only).
set -e; cd "$(dirname "$0")/.."; HOOK=${1:-h1}; VER=${VER:-v1}; H=$(echo $HOOK | tr a-z A-Z)
ffmpeg -v error -y -i work/${HOOK}_video.mp4 -i work/${HOOK}_audio.wav -loop 1 -i assets/graphics/hook_${HOOK}.png -filter_complex \
 "[0][2]overlay=0:0:enable='between(t,0.3,7.6)':shortest=1,scale=1080:1920:flags=lanczos,rgbashift=rh=1:bh=-1,noise=c0s=6:c0f=t+u,vignette=angle=PI/5:mode=forward,unsharp=3:3:0.25,format=yuv420p[v];[1]loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -preset slow -crf 21 -maxrate 9M -bufsize 18M -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart -map_metadata -1 -shortest \
 out/WilloMD_RootOut_Set17_${H}_9x16_${VER}.mp4
