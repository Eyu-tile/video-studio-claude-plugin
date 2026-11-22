# Splice L16's article, then join only the on-camera part of each line into one lip-sync track per take.
# Offsets go to work/lipsync_map.json so the edit can cut each line back out of the take.
import subprocess, json
R="raw/vo"; W="work/ls"; import os; os.makedirs(W,exist_ok=True)
def sh(c): subprocess.run(c,shell=True,check=True)
# L16: "with a little" -> "with the little" (the 'the' from "on the hard top", same take)
sh(f"ffmpeg -v error -y -i {R}/L16.mp3 -filter_complex "
   "\"[0]atrim=0:2.16,asetpts=N/SR/TB[a];[0]atrim=3.53:3.68,asetpts=N/SR/TB[b];"
   f"[0]atrim=2.27,asetpts=N/SR/TB[c];[a][b][c]concat=n=3:v=0:a=1\" -ar 44100 {R}/L16fix.wav")
GAP=0.35
takes={
 "D1":[("L01",0,4.45),("L03",0,1.35),("L05",0,2.0),("L07",0,3.4),("L09",0,1.9),("L11",0,2.0),("L11",10.3,11.65),("L13",0,4.1)],
 "D2":[("L15",0,4.6),("L16fix",9.15,9.75),("L17",0,2.4),("L18",0,7.5)],
 "M1":[("L02",0,3.0),("L04",0,4.05),("L06",0,2.75),("L10",0,1.85),("L12",0,2.7),("L14",0,8.3)],
}
mp={}
for t,segs in takes.items():
    parts=[];pos=0.0;mp[t]=[]
    for i,(n,a,b) in enumerate(segs):
        src=f"{R}/{n}.wav" if n=="L16fix" else f"{R}/{n}.mp3"
        if b==0: b=float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {src}",shell=True))-0.15
        p=f"{W}/{t}_{i:02d}.wav"
        sh(f"ffmpeg -v error -y -i {src} -af atrim={a}:{b},asetpts=N/SR/TB,afade=t=out:st={b-a-0.04}:d=0.04,apad=pad_dur={GAP} -ar 44100 -ac 1 {p}")
        mp[t].append({"line":n,"src_in":a,"src_out":b,"take_in":round(pos,3),"take_out":round(pos+b-a,3)})
        pos+=b-a+GAP; parts.append(p)
    open(f"{W}/{t}.txt","w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
    sh(f"cd {W} && ffmpeg -v error -y -f concat -safe 0 -i {t}.txt -c:a pcm_s16le {t}_lipsync.wav")
    print(t, round(pos,2))
json.dump(mp,open("work/lipsync_map.json","w"),indent=1)
