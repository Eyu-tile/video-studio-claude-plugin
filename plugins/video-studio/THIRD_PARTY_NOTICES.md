# Third-party skills

The following skill folders are copied from
[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) and are licensed under the
Apache License 2.0 (https://www.apache.org/licenses/LICENSE-2.0). Copyright HeyGen and the
HyperFrames contributors. Versions and content hashes are pinned in `skills-lock.json` (upstream release v0.9.19).

- `hyperframes/`
- `hyperframes-cli/`
- `hyperframes-registry/`
- `reverse-any-video/`
- `style-sampling/`
- `media-use/` (its sound effects under `media-use/audio/assets/sfx/` are Pixabay Content License, see `CREDITS.md` there).
  Local change: the riser timing note in `audio/references/sfx.md` and `audio/assets/sfx/manifest.json` (the file
  crests at about 3.0 s, not at its 10.03 s length); the other folders are unmodified.

Refresh (maintainers): in a scratch folder run `npx skills add heygen-com/hyperframes --skill hyperframes --skill hyperframes-cli --skill hyperframes-registry --skill media-use --agent claude-code -y`, then replace the four folders under `skills/` with the new copies and update `skills-lock.json`.

All other skills in this plugin (`video-*`, `motion-graphics`) are original to this plugin (MIT).

Telemetry: the HyperFrames CLI sends usage telemetry, and the `hyperframes` skill runs a usage beacon
(`npx hyperframes events`) when it starts. Opt out with `npx hyperframes telemetry disable`.

# Adapted code

- **broll-mcp** ([edigeh/broll-mcp](https://github.com/edigeh/broll-mcp), MIT, Copyright (c) 2026 edigeh): the
  Internet Archive search, licence table, file grouping, scene normalising and cut verification in
  `tools/archive.py` follow its approach and numbers (reimplemented, not copied verbatim). The archive.org metadata
  fixtures in `tests/fixtures/archive/` come from its `research/raw/meta/` captures.

# Optional external tools (installed on request, not bundled)

- **rea-video** ([JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video), Apache-2.0): installed by
  `vs setup --rea` into its own venv, pinned to commit `e3d2805ee1e6188a640b62149eb055474f6bf982`; no code is copied
  into this plugin. `vs breakdown` is an independent implementation (numpy + ffmpeg).
- **earshot** ([Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), MIT): installed by `vs setup --earshot`.
- **Composio skill** ([ComposioHQ/composio](https://github.com/ComposioHQ/composio) `skills/composio`, MIT, Copyright
  (c) 2025 Sampark Inc.): installed for Claude Code by `vs setup --social` (`npx skills add ComposioHQ/composio
  --skill composio --agent claude-code --global`); nothing is copied into this plugin. Posting runs through the
  person's own Composio account (CLI or MCP).
