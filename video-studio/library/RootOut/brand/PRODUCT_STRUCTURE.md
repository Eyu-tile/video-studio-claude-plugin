# RootOut product structure (for prompts and shot checks)

From the PDP images (site + the client's zip of 6 webp, 21 Nov: identical to `images/pdp/`, 1280 px) and the site's
how-to loop. Paste the **prompt block** into every generation that shows the product; check every frame against the list.

## The parts
| part | what it looks like | how it's used |
|---|---|---|
| **Bottle** | short round amber glass bottle (Boston-round shape), 11 ml; shoulders curve into a short neck | stands upright; never held by the glass to apply |
| **Cap = handle** | tall glossy **white** cylindrical screw cap, about as tall as the glass body; plain, no print | unscrewed and held like a nail-polish cap |
| **Brush** | a thin clear plastic stem fixed under the cap, small brush tip (dark bristles in the how-to loop) | comes out with the cap, paints a thin coat on the spot only, goes back in |
| **Label** | white wrap; top line "WilloMD" small navy; "RootOut™" large bold navy; "Advanced Wart, Corn & Callus Oil" in two lines; a royal-blue band "Brush-on · Natural oil" in white; "11 ml (0.37 fl oz)" at the bottom | label faces camera in product moments; never mirrored, never re-lettered |
| **Box** | tall white carton, "WilloMD" small, "RootOut™" large navy, "Advanced Wart, Corn & Callus Oil", blue band "File · Soak · Cover", "11 ml (0.37 fl oz)" | offer / end card, three in a row |
| **Night cover dots** | a sheet of ~20 clear round dots (hydrocolloid look) | one pressed over the spot at bedtime, peeled in the morning |
| **Single-use files** | 5 small white flat emery strips with rounded ends | two light strokes on the hard top, then binned |

## Routine as shown (File · Soak · Cover)
1. A fresh white file, two light strokes over the hard top only.
2. Unscrew the white cap; the brush comes out on its stem; paint the oil on the spot (no dropper, no cotton swab, no soaking in water).
3. Press a clear round dot over it.

## Prompt block (copy into product shots)
"a small round amber glass bottle with a tall glossy white screw cap; attached under the cap is a thin clear stem with a
small nail-polish-style brush; white label with 'RootOut' in large bold navy letters and a royal-blue band near the
bottom; the cap is unscrewed and the brush paints oil onto the skin like nail polish"

## Generation notes (tests, 21 Nov)
- **Soul does not keep the product.** With `A01-bottle-front-white.jpg` as its reference it drew a different bottle
  (garbled label "Advenenad, Wart, Cornt", invented logo, wrong shape, no scene). Don't rely on Soul for readable labels.
- For label-readable moments, composite the real packshot (`images/pdp/A12-duo-transparent.png`, `A01-…`) in the edit,
  or keep the bottle soft-focus/turned in generated shots. Test whether Seedance `image_references` holds the label
  before relying on it.
- Never: a dropper, a roller ball, a spray, a cotton swab (that is Amoils), a bottle with a printed cap.
