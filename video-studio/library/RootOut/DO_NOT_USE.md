# RootOut do-not-use rules (from the site; no client rules received yet)

> **Owner rule (23 Nov 2026, overrides the briefs and CLAIMS.md):** no disclaimer-type text in our videos or generations: no "AI illustration" / AI-generated labels, no footnotes or marks (`*`, `†`), no FDA / "not evaluated" / "results vary" lines, no photo-credit captions. Disclosures go in the platform AI label and the post description. House lesson L1 (`style/LESSONS.md`), checked by `vs qa`.

These come from what the site itself labels and from claim risk. Client rules, when they arrive, are added here and win.

## BANNED
1. **The "Real results" before/after photos** (`brand/images/samples_illustrative/`, atlas ids `we-79641c2cd5`… all
   `rootout-SAMPLE-*`). Each is stamped "CONCEPT ONLY · AI EXAMPLE · NOT A REAL RESULT". Never show them as results,
   never crop the stamp off, never pair them with names, ages or "nearly gone in N weeks". Style reference only.
2. **The named testimonials and the "4.8 from 1,316 reviews" rating.** The site labels them "illustrative reviews … for
   layout preview". Don't put them in an ad as real reviews, captions, or VO.
3. **Melt-Off Heel Kit assets** (`brand/images/sister_meltoff/`): a different product (cracked heels). RootOut is
   explicitly "not for dry, cracked heels".
4. **AI people presented as customers.** Any AI person (site renders or Higgsfield) may act out the routine but must not
   say "I"/"my wart" results or appear as a reviewer, unless the client signs off and it is disclosed.
5. Genital warts, moles, bleeding or colour-changing spots, infected/broken skin, diabetic feet: never shown as use cases.

## CAUTION (check before use)
- The 8x-deeper visuals (`pdp-02`, `rootout-1v1-root-v6.*`, `3062835a….mp4`): keep the † footnote on screen.
- Children (`pdp-04-no-tears`: AI boy asleep): kids are an angle the site pushes, but child-safety claims need sign-off;
  which formula (adult vs Kids 4+) does the bottle on screen contain?
- Comparison table (`pdp-06`): "No blisters or scars", "Gentle enough for kids" are absolute claims.
- Competitor references: show "a freeze spray" / "corn pads" generically; no competitor brand names or packaging.
- Results-timeline language ("That means it's working", "flakes off") and "so it stays gone".
- How-to video bottle (`rootout-how-to-v3.*`): a plain amber bottle with only "WilloMD" small, not the labelled
  RootOut bottle. Fine as a how-to; for a product moment use the labelled renders.
- Gore: warts/corns are close-ups of skin; keep them clean and mild (no bleeding, peeling flesh or pus).

## Client edit rules (from Set 19 review, 23 Nov 2026) — apply to every set
- **No "AI illustration" (or any "AI …") text on screen.** Keep the claim disclaimers (`*`, `†`).
- **Each b-roll clip once per ad.** No repeats of the same footage, real or generated (check with `ads/set19_build/qa_unique.py`).
- **No frozen b-roll.** Never hold a last frame; stretch ≤ 0.7x or add coverage (`ads/set19_build/qa_freeze.py`).
- **Lip sync:** a talking clip only ever plays with its own line; never reuse it as b-roll under other VO.
- **Kids look school-age (≈ 5+), never babies or toddlers.**
- Captions stay in the middle safe zone, including over screenshots.
