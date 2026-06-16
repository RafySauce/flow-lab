---
id: travel-planner
title: "Travel Planner"
aliases: []
type: skill
artifact-version: "1.1"
created: 2026-06-04
updated: 2026-06-04
status: living
truth-level: to-review
domain: ai
phase: "Phase 1 — Personal Skills"
systems: []
tags:
  - homelab/ai
  - travel
  - personal
  - lifestyle
execution-tier: frontier
created-by: "Cincinnatus & Claude claude-sonnet-4-6"
generated-by: skill-foundry
skill-version: "0.2.2"
skill-build-version: "0.2"
source: human+ai
related: []
---

# Travel Planner

Personalized travel planning skill for M1 and F1. Builds complete trip packages (itinerary,
packing list, logistics brief, combined trip document) against a standing traveler profile.
Two modes: Ideation (destination open) and Plan (destination confirmed). See the SKILL.md
in `cowork-skill-foundry/forge/travel-planner/` (moving to `completed-skills/` on review).

---

## Connection Notes

*Un-verified hints for the vault-side connection skill. Not graph edges.*

- Hard dependency on: `traveler-profile.md` (Skill Foundry workspace) — this file must exist
  and be current for the skill to produce accurate output. Profile changes don't require
  skill reinstall; they're picked up on the next invocation.
- F1 nut allergy is load-bearing across every output type — any future skill that generates
  restaurant or food recommendations for this household should reference or link this pattern.
- Execution-tier frontier: driven by voice load, cultural judgment, allergy-aware restaurant
  research, and multi-mode personalization. Not a candidate for Hermes-baseline until the
  profile-reading step can be made fully deterministic.
- Origin: built from bare conversation intent in a single skill-foundry session (2026-06-04).
  No formal primer-brief was produced; the exploration phase happened inline. A trace is
  logged in `cowork-skill-foundry/traces/`.
- Forward: as more personal skills are built for this household (meal planning, health
  logistics, home management), the traveler-profile.md pattern — external standing context
  read at invocation — may become a reusable house pattern worth formalizing.
