---
id: job-search-partner
title: "Job Search Partner"
aliases: []
type: skill
artifact-version: "1.0"
created: 2026-06-10
updated: 2026-06-10
status: living
truth-level: to-review
domain: ai
phase: "Phase 1 — Personal Skills"
systems: []
tags:
  - homelab/ai
  - career
  - personal
  - household
execution-tier: frontier
created-by: "Cincinnatus & Claude claude-fable-5"
generated-by: skill-foundry
skill-version: "0.2.2"
skill-build-version: "0.1"
source: human+ai
related: []
---

# Job Search Partner

Two-mode job-search skill for M1 and F1: Scout (Nimble-backed live discovery with
dedupe) and Apply (five-dimension fit evaluation → drafter-reviewer document
pipeline in docx/pdf → interview prep), built against standing per-person career
profiles. See the SKILL.md in `cowork-skill-foundry/forge/job-search-partner/`
(moving to `completed-skills/` on review).

Normalized from foreign material: github.com/MadsLorentzen/ai-job-search (MIT).

---

## Connection Notes

*Un-verified hints for the vault-side connection skill. Not graph edges.*

- **Origin/attribution:** MadsLorentzen/ai-job-search (MIT, vetted 2026-06-10);
  job-portal CLI pattern within it credited to Mikkel Krogholm
  (mikkelkrogsholm/skills). Companion LinkedIn article by the author was not
  fetchable (LinkedIn blocks automated access); README carried the substance.
  Starter doc: `backlog-skill-starters/starter_ai-job-search.md`.
- **Hard dependency:** `career-profile-M1.md` / `career-profile-F1.md` (Skill
  Foundry workspace) — neither exists yet; the skill's profile interview creates
  them on first run. Until then every run starts with profile-building.
- **Sibling pattern:** second household skill after [[travel-planner]] using the
  external-standing-profile-read-at-invocation pattern (M1/F1 pseudonyms). Two
  instances now — the pattern is starting to earn formalization as a house
  contract.
- **Privacy posture:** profile PII never enters web queries; deep profile
  authoring recommended local-first. This is the first skill where the
  sovereignty boundary shaped the *workflow* (not just storage) — relevant
  precedent for future personal-data skills (health, finance).
- **Execution-tier frontier:** voice load (application prose), judgment-heavy
  evaluation, and the reviewer sub-agent pattern. Scout mode's
  search-dedupe-triage loop is the one baseline-able fragment if ever split.
- **Runtime couplings:** nimble researcher sub-agent / nimble-web-expert
  (discovery; WebSearch fallback wired), house docx/pdf skills (document
  output), Agent tool (reviewer).
- **Eval status:** not yet run — promotion to `verified` requires eval pass +
  Cincinnatus review.
