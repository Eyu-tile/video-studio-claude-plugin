---
description: Work a Hyperscale brief - show my briefs, or pull brief N into a project, find footage, edit, and upload the finished ads
argument-hint: "[brief number, e.g. 457]"
---

Use the `hyperscale-briefs` skill.

1. Check the Hyperscale connector responds (`mcp__Hyperscale__whoami`). If its tools aren't there, explain how to
   connect it (Claude app: Settings → Connectors → Hyperscale; Claude Code: /mcp) and stop.
2. No brief number ($ARGUMENTS empty): list the person's briefs (`list_briefs` with `mine: true`, plus stages
   `ready` and `revisions` filtered to their name), say which need them now, and ask which to work on.
3. With a number: `get_brief($ARGUMENTS)`, save it as JSON in the workspace, run
   `vs hyperscale pull <file> --brand "<brand from whoami>"`, read the project's BRIEF.md and any linked docs,
   and summarise in a few lines: what to make, the exports, open notes, and the first step. If a project for it
   already exists, run `vs hyperscale notes` and `vs hyperscale status` instead and continue from there.
