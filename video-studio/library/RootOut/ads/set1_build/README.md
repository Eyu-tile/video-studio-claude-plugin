# Set 1 build kit (ROS1, delivered v5, 22 Nov)

How the RootOut Set 1 ad (H1/H2/H3, 9:16, ~1:57) was made, to reuse for the other sets. The project itself
(`video-studio/projects/rootout-set1/`, media, renders) is git-ignored and stays on the machine that made it.

| file | what |
|---|---|
| `SHOT_PLAN.md` | beat-by-beat plan, sources and credit quote |
| `GEN_LOG.md` | every Higgsfield (WilloMd) job: Soul frames, Seedance clips, ElevenLabs VO, rerolls, spend per pass |
| `jobs.json` | job ids: voices (Emily, Maya, Nora, Sloane), start frames, clips (reuse as references) |
| `build_edl.py` | builds the EDLs: talking clips keep their lip-synced audio, VO over muted b-roll, sound bed (ambience + foley), web cards, CTA |
| `render_gfx.py` | code-made motion cards (stakes, offer with 90-day seal, end card with Shop now), PIL -> ffmpeg |
| `make_captions.py` | whisper transcript of the render -> spelling fixes -> bold-pop captions kept off disclaimers/products |
| `make_web_cards.py` + `WEB_SOURCES.md` | real AAD page lines framed as phone screenshots; sources and exact quotes |
| `finish.sh` | phone-camera finish (grain, fringe, vignette, sharpen), captions burn-in, loudnorm TP -2.2 |

Lessons from the client's notes: the product must always be the real RootOut bottle (Seedance with the bottle as
`image_references` holds the label; Soul does not); no "AI-generated" text on testimonials (client's call: use the
platform AI label); captions throughout; sound under every AI shot; motion 3D skin cross-sections like Amoils #004.
