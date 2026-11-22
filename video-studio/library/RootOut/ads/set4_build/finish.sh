#!/bin/bash
# Light phone finish (fine luma grain, soft vignette, light sharpening) + burned-in captions + loudness -14 LUFS / TP -2.2.
set -e; h=$1; H=$(echo $h | tr a-z A-Z); P=/home/user/video-studio-claude-plugin/video-studio/projects/rootout-set4; cd $P
ffmpeg -y -v error -i out/raw_${h}.mp4 -vf "noise=c0s=5:c0f=t+u,vignette=angle=PI/6:mode=forward,unsharp=3:3:0.2,ass=work/captions_${h}.ass:fontsdir=assets/fonts" \
  -c:v libx264 -preset slow -crf 21 -maxrate 10M -bufsize 20M -pix_fmt yuv420p -af loudnorm=I=-14:TP=-2.2:LRA=11,alimiter=limit=0.75:level=false -ar 48000 -c:a aac -b:a 192k -movflags +faststart -map_metadata -1 \
  out/WilloMD_RootOut_Set4_${H}_9x16_${VER:-v1}.mp4
echo out/WilloMD_RootOut_Set4_${H}_9x16_${VER:-v1}.mp4
