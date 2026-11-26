#!/usr/bin/env python3
"""Set 6 body takes (owner 26 Nov: whole body on camera, her real voice, the K1 vibe). Writes takes.json (requests)."""
import json
START, BOTTLE, VOICE = "e5b43ab6-bfdb-4cf9-96d6-f369ef258287", "2c52c56e-9f2f-4f40-9fda-4caa813e7578", "260e1746-252f-4938-b69d-fcffe8fb4de6"
BASE = ("Real vertical phone video, the phone propped against the fruit bowl on the kitchen counter, still camera with a tiny natural wobble, "
        "plain morning daylight; the same woman, same olive fleece, same kitchen as the start image; one continuous take, never cut. "
        "She talks straight to the lens like she's telling a close friend what happened: relaxed, honest, a little tired, natural small pauses "
        "between sentences, small shrugs, normal blinking, she glances away while remembering and comes back to the lens; not performing, not salesy. "
        "Voice: the same warm American female voice as the reference audio (use the audio only for her voice and tone, never its words), "
        "conversational, unhurried. She says exactly: \"{line}\" {act} "
        "The RootOut bottle is always exactly the reference bottle: white label with navy 'RootOut', blue band, tall glossy white cap, label unchanged and readable, never mirrored. "
        "No music, no captions, no on-screen text.")
REST = "The small amber RootOut bottle stands on the counter beside the fruit bowl, label facing the camera."
T = [  # (name, seconds, line, action)
 ("T02_limp", 15, "It started with a limp. He walked on the side of his foot. Every school morning was a fight over socks. He said it hurt to step on. I thought it was a splinter. I shook out his shoes. I tried tweezers. Nothing.", REST + " On 'Nothing.' she gives a small helpless shrug."),
 ("T03_found", 9, "Then one night at bath time, I turned his foot over. A hard little spot, with tiny black dots. A plantar wart.", REST + " She goes quiet and serious on 'A plantar wart.'"),
 ("T04a_two", 8, "And it didn't stay one. A month later there were two. Then his little sister had one on her heel.", REST + " She holds up two fingers on 'there were two'."),
 ("T04b_study", 12, "I looked it up. A study of almost fifteen hundred schoolkids found that someone at home with a wart makes the other kids about twice as likely to get one.", REST + " She picks up her phone from the counter, glances at it, then back to the lens."),
 ("T05_soccer", 7, "He sat out his soccer games. He wouldn't take his shoes off at a friend's house.", REST + " A sad little smile."),
 ("T06_freeze", 13, "So we did what the doctor said. We froze it. Somebody had to hold him still. It blistered, and he limped worse for a week. Three weeks later, it was back. Same spot.", REST + " She shakes her head slightly on 'Same spot.'"),
 ("T07_next", 5, "And now his sister was next in line for the freeze.", REST + " She exhales and pauses after the line."),
 ("T08a_tip", 10, "Then a mom from his team told me why it keeps coming back. Freezing, acid and shaving only snap off the top, like picking a dandelion.", REST + " On 'snap off the top' she mimes a little snap with her fingers."),
 ("T08b_rootout", 11, "The root stays under the hard skin, so it grows back. She used RootOut. It's an oil with four plants, and you brush it on at bedtime.", "On 'She used RootOut' she picks the small amber RootOut bottle up from the counter and holds it up beside her face, label toward the lens."),
 ("T09a_honest", 8, "Honestly, I didn't think it would work. But it was two minutes at bedtime, and nobody had to hold anybody down.", REST + " A small honest laugh at 'Honestly'."),
 ("T09b_routine", 14, "Two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top. He said it felt cool. In about two weeks, it was gone. His sister's too.", "She holds the small amber RootOut bottle in one hand and counts the three steps on her fingers; she smiles on 'His sister's too.'"),
 ("T10a_wish", 8, "Here's what I wish I'd known sooner. The lemon softens that hard skin on top. The tea tree is a thin oil.", REST + " She leans in a little, explaining."),
 ("T10b_root", 14, "It sinks in, up to eight times deeper than a regular cream, and carries the pokeweed and white cedar down to the root. Then those two break the wart down from there, so it can't grow back.", REST + " Calm explaining hand gestures, pointing down on 'down to the root'."),
 ("T11_safe", 8, "It's a kids' formula, for ages 4 and up, and pediatricians recommend it. No freezing, no acid, no blister.", "She holds the small amber RootOut bottle up to the lens, label facing the camera."),
 ("T12_after", 9, "We did fourteen more nights after it was gone, so the root was gone too. He's back at soccer. Running, not limping.", REST + " A relieved, proud smile on 'Running, not limping.'"),
 ("T13a_wait", 8, "If your kid's limping and you find a hard spot under his foot, don't wait for it to spread.", REST + " Sincere, direct to the lens."),
 ("T13b_offer", 9, "It's at the link below. Buy two, we'll add a third. And if it's not gone, you've got 90 days to get your money back.", "She holds the small amber RootOut bottle beside her face, label toward the lens, and points down once on 'link below'."),
]
req = []
for i, (n, s, line, act) in enumerate(T, start=2):
    req.append({"index": i, "params": {"model": "seedance_2_5", "duration": s, "aspect_ratio": "9:16", "resolution": "720p",
        "medias": [{"value": START, "role": "start_image"}, {"value": BOTTLE, "role": "image"}, {"value": VOICE, "role": "audio"}],
        "prompt": BASE.format(line=line, act=act)}, "name": n})
json.dump(req, open("takes.json", "w"), indent=1)
print(len(req), "takes", sum(t[1] for t in T), "s")
