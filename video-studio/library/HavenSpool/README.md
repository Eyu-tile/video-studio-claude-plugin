# Haven & Spool library

Everything video-studio has learned about Haven & Spool's ads. Standalone: built only from Haven & Spool's own
Hyperscale briefs; no other brand's folder applies here.

Start with:
1. `AD_PLAYBOOK.md`: product, offer, audience, angles, formats, hooks, mechanism, editing defaults.
2. `WINNING_ADS.md`: the winners and what to reuse from each (with the briefs' own evidence).
3. `DO_NOT_USE.md`: what reviewers keep sending back, ranked.
4. `LESSONS.md` / `lessons.json`: the same mistakes as checks (`vs lessons brief --brand HavenSpool`).

Generated from the briefs (`vs hyperscale learn`; don't edit by hand):
- `ads/briefs/<number>.json`: raw `get_brief` results (139 briefs)
- `ads/briefs_index.json`, `ads/CATALOGUE.md`, `ads/HOOK_BANK.md`, `ads/WINNER_SIGNALS.md`,
  `ads/REVIEW_NOTES.md`, `ads/EDITING_RULES.md`, `ads/STATS.md`

Refresh after new briefs launch: save their `get_brief` JSON into `ads/briefs/`, then
`vs hyperscale learn video-studio/library/HavenSpool/ads/briefs --brand "Haven & Spool"`, then update the three
hand-written files above.
