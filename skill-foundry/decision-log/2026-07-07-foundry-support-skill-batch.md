---
id: decision-2026-07-07-foundry-support-skill-batch
title: "Decision Log — Foundry-Support Skill Batch Build: Contract Reviewer + Provenance Stamper"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[sp-contract-reviewer]]", "[[sp-provenance-stamper]]"]
---

# Decision Log — 2026-07-07 — Foundry-Support Skill Batch Build

**What was decided:** author the two backlog starters the operator confirmed
as worth building after rationalizing the skill-foundry backlog —
`contract-reviewer` and `provenance-stamper` — each as an engine-neutral
`SKILL.md` plus adapters, staged in `review-skills/` at `truth-level:
to-review`. **By whom:** agent, on operator instruction ("that works,
proceed" — confirming the build/drop split proposed after backlog
rationalization). **What it affects:** `review-skills/contract-reviewer/` and
`review-skills/provenance-stamper/` (new); the two `sp-*` primer briefs stay
unchanged in the backlog as intake records. Nothing promoted, nothing moved
to `../../produced-skills/`, nothing deployed.

**Intake path:** clean — both arrive from `sp-*` primer briefs already sitting
`to-review` in the backlog; no foreign material, no vetting checklist run.

**Companion decision:** the other two starters seeded alongside these four
(`sp-intake-triage-assistant`, `sp-mirror-drift-checker`) were triage-dropped
in the same rationalization pass, not built — see
`2026-07-07-skill-starter-triage-drop.md`.

**Notable calls:**
- `contract-reviewer`'s Copilot adapter is a **custom agent** definition
  (`.github/agents/contract-reviewer.md`), not a prompt file — its triggering
  intent is a standing role reused across every flowspace reaching
  `to-review`, not a one-off command, per the adapter's own rule of thumb.
  Its Rovo adapter is deliberately **not built**: the brief marked it
  optional, and no Confluence-native point of use exists yet — this mirrors
  the same "don't build ahead of demand" call applied to the two dropped
  starters, at adapter granularity instead of skill granularity.
- `provenance-stamper` gets both adapters (prompt file for Copilot, agent for
  Rovo) per its brief's explicit "both" — it is invoked from both surfaces on
  every artifact either foundry produces.
- Boundary/collision first pass against the five already-produced
  `ai-refinement` skills and the two dropped starters: no territory overlap —
  these two serve the foundries' own pipeline (contract quality,
  frontmatter), not a work-item refinement run. Formal collision check
  re-runs at the five-point promotion gate; pre-run evidence in the
  companion entry, `2026-07-07-foundry-support-skill-gate-prerun.md`.

**Next:** operator review per `foundry-spec.md` §5 (see the companion
gate-pre-run entry for what's already checked agent-side and what remains).
