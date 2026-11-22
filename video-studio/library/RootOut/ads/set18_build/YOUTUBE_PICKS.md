# Set 18 · real b-roll found on YouTube (22 Nov)

Searched YouTube by beat (18 queries, 144 results), checked each pick by its frames at 0 / 25 / 50 / 75 %.
**Not downloaded here:** YouTube asks this cloud server to sign in ("confirm you're not a bot"). Download on a normal
computer with the command at the bottom, then drop the files in `video-studio/projects/rootout-set18/raw/stock/youtube/`
(or a Drive folder and send the link).

**Rights:** these are ordinary YouTube uploads, not checked as Creative Commons. Using them in a paid ad needs the
uploader's OK or a licence (or a CC licence on the video page: "Creative Commons Attribution licence (reuse allowed)"
under the description). Check each before the ad ships; keep the link in CREDITS.

| beat | video | length | what's in it (by frame) | use | caution |
|---|---|---|---|---|---|
| 11 dandelion snap / root | [ryLeRKaUKbc](https://www.youtube.com/watch?v=ryLeRKaUKbc) "How To Dig Up Dandelions" | 20 s | hand (pink sleeve, garden glove) pulls dandelions in a lawn, close, phone look | **USE** snap + pull | talking head ~25 %: skip |
| 11 whole root | [ehFNXzM04HQ](https://www.youtube.com/watch?v=ehFNXzM04HQ) "How to properly remove a dandelion" | 1:43 | bare hands work a dandelion out; ~75 % a hand holds the plant with its long root | **USE** root to lens | title card at start; a bag with text |
| 11 backup | [gI--Hy4XNh8](https://www.youtube.com/watch?v=gI--Hy4XNh8) "Weed Puller… Whole Root Every Time" | 54 s | stand-up weed puller lifts dandelions out whole | BACKUP | it's a tool demo (possible brand) |
| 11 backup | [thI_ZYJsZw0](https://www.youtube.com/watch?v=thI_ZYJsZw0) "How to Pull Dandelions" | 1:09 | ~75 %: macro of fingers at a dandelion base | BACKUP | man's face in the rest |
| 17 sprinkler | [N8x-w0hWxSE](https://www.youtube.com/watch?v=N8x-w0hWxSE) "Summer fun running through a sprinkler" | 28 s | small boy runs through a lawn sprinkler, backyard, home video | **USE** crop to legs/feet | face small but visible: crop |
| 17 sprinkler | [ydDVsE5QfSA](https://www.youtube.com/watch?v=ydDVsE5QfSA) "Kids and Water Sprinkler" | 40 s | several kids in a backyard sprinkler, sunny | **USE** (two kids) crop to feet | faces at distance: crop |
| 17 sprinkler | [hSgfgFm8Ofw](https://www.youtube.com/watch?v=hSgfgFm8Ofw) "Slow-Motion Sprinkler Encounter" | 14 s | girl runs through a sprinkler, slow motion | BACKUP | face at distance |
| 08 freezing | [SQeGts3bDW0](https://www.youtube.com/watch?v=SQeGts3bDW0) "Cryotherapy of Wart" | 1:06 | real cryo gun spraying a finger wart, macro, no faces | **USE** 1–2 s on "Freezing." | adult hand; brass gun, no brand seen |
| 08 freezing backup | [A-DAS3xPul8](https://www.youtube.com/watch?v=A-DAS3xPul8) "Wart Removal Using Liquid Nitrogen" | 1:13 | clinic, gloved hands, nitrogen can | BACKUP crop chest-down | doctor's face: crop |
| 10 duct tape | [WmPJ4xjrMjU](https://www.youtube.com/watch?v=WmPJ4xjrMjU) "How To Rip Duct Tape" | 24 s | ~75 %: hands rip grey tape | **USE** last seconds | "Duck Tape" brand in thumbnail/title cards: use only the rip |
| 06c school | [LUsTvmzuXCs](https://www.youtube.com/watch?v=LUsTvmzuXCs) "School Backpack And Students Walking" | 15 s | kids from behind with backpacks on school steps | **USE** | stock-style, check licence |
| 06c school | [KuFYG90ddqk](https://www.youtube.com/watch?v=KuFYG90ddqk) "Elementary School Kids Walking With Backpacks" | 7 s | three kids from behind walking into school | **USE** | |
Rejected: AaWsjFD4rIQ (FillerStock watermark), sAWLCr9Pw2A (teen face, not a milkshake shot), Dzy8A_H77ow (kid face +
captions), DBvM3ulpB5E / X63whpCvuns / WkRBXPr8uCU / zbEPuSqCKK0 (talking heads, cartoons), uKvLA63FbaE (Froot-Loops
colours, not a Cheerio look).
Not found on YouTube: milkshake in a car back seat, a lamp switched off by a hand, kids' feet on a bath mat, a kitchen drawer at night.

## Download (on a computer where YouTube works)
```
pip install -U yt-dlp
mkdir -p set18_youtube && cd set18_youtube
yt-dlp -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 -o "%(id)s_%(title).40s.%(ext)s" \
  ryLeRKaUKbc ehFNXzM04HQ gI--Hy4XNh8 thI_ZYJsZw0 N8x-w0hWxSE ydDVsE5QfSA hSgfgFm8Ofw \
  SQeGts3bDW0 A-DAS3xPul8 WmPJ4xjrMjU LUsTvmzuXCs KuFYG90ddqk
```
