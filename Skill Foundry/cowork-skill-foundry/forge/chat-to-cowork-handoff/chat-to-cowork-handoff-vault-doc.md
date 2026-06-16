---
id: chat-to-cowork-handoff
title: "Chat-to-Cowork Handoff"
aliases: []
type: skill
artifact-version: "1.0"
created: 2026-06-14
updated: 2026-06-14
status: living
truth-level: to-review
domain: ai
phase: "Phase 1 — Personal Skills"
systems: []
tags:
  - homelab/ai
  - workflow
  - session-management
  - cowork
execution-tier: frontier
created-by: "Cincinnatus & Claude claude-sonnet-4-6"
generated-by: skill-foundry
skill-version: "0.2.2"
skill-build-version: "0.1"
source: human+ai
related: []
---

# Chat-to-Cowork Handoff

Session-handoff skill for transferring work from Claude chat to Cowork mode. Builds a structured markdown document — work-type-adaptive, depth-sized, Cowork-aware — that the receiving Cowork session can open and act on immediately: skills cued, workspace files identified, resumption instruction priming Cowork behaviors.

Normalized from foreign material: github.com/maaarcooo/claude-skills (`handoff/SKILL.md`, public, 2026).

---

## Connection Notes

*Un-verified hints for the vault-side connection skill. Not graph edges.*

- **Origin/attribution:** maaarcooo/claude-skills GitHub repo, `handoff/SKILL.md` (public, no explicit license; standard open sharing; vetted 2026-06-14). Selected from four candidates: ykdojo/claude-code-tips (minimal stub), BexTuychiev gist (Claude Code-only, wrong context), maaarcooo (chat-native, most complete — selected), thegeneralist01 (empty on fetch). Trace: `cowork-skill-foundry/traces/2026-06-14-chat-to-cowork-handoff-trace.md`.
- **Core structure from source:** work-type classification (6 types), depth-sizing tiers (Light/Standard/Deep/Extended), adaptive skeleton with "never include empty sections" discipline, quality checklist. These are the source's real contributions — preserved intact.
- **Cowork delta added by foundry:** `## Cowork Setup` section in the document skeleton (skills to invoke / workspace files to read / connectors needed), Cowork-priming resumption instruction block (replaces source's generic "confirm understanding"), Process Step 2 (environment mapping before writing), save-location guidance, three Cowork-specific "What This Skill Is Not" entries.
- **Potential complement:** a reverse skill (Cowork→chat) could be useful when a Cowork session needs a lightweight continuation without the full tool stack. Not built here; flag for the backlog if the pattern recurs.
- **Potential complement:** a generic chat→chat handoff (no Cowork target) is covered by the source material. If that use case surfaces, the source or a thin fork is the right path — not this skill, which has Cowork orientation baked in.
- **Execution-tier frontier:** work-type classification, depth judgment, skill-recommendation, and voice calibration all require model judgment. Not a candidate for Hermes-baseline.
- **Limits measured:** name 22, description 680, compatibility 174 — all under loader limits.
