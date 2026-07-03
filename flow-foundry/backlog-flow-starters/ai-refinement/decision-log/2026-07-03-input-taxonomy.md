---
id: decision-2026-07-03-input-taxonomy
title: "Decision Log — AI Refinement Common Source-Input Taxonomy"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[context-elicitation]]"
---

# Decision Log — 2026-07-03 — Common Source-Input Taxonomy

## Input

Operator-stated observation: the material that most often starts a refinement
run falls into four types — (1) emails with direct requests for support,
(2) vendor details on required actions to take, (3) meeting minutes/notes or
summaries, (4) directly stated requirements from an engineer in chat
("I need to go do x, y, z to help ABC (stakeholder)").

## Decision

Thread the taxonomy into the existing flowspace artifacts rather than adding a
new stage or document type:

| Artifact | Change | Version |
|---|---|---|
| `HUB.md` | New "Common source inputs" section: the four types, typical carriers, per-type handling notes | 1.2 → 1.3 |
| `01-intake-and-guardrails/CONTEXT.md` | Optional source-material input row; data-safety step extended to type and screen the material (strip names/addresses, vet third-party vendor content); screened material + type tag added as an output to Stage 02; verify item added | 1.1 → 1.2 |
| `02-context-and-problem-framing/CONTEXT.md` | Optional input row for the screened material + type tag; elicitation step steers by type (requester → sweep entry point; solution-shaped vendor/task lists → recover the problem first; minutes → split into one item per run); verify item added | 1.1 → 1.2 |

**Rationale**: All four types arrive request-shaped or solution-shaped, so they
change *how* Stage 1 screens and Stage 2 elicits — they do not add work the
existing stages don't already own. No topology change; no new stage.

## Data-safety note

Types 1 and 3 (emails, minutes) routinely carry names and addresses; type 2 is
third-party material. The screen belongs at Stage 01 — the session's trust
boundary — which is why the handling landed there rather than in Stage 02.

## Flagged, not applied

The `context-elicitation` skill spec (skill-foundry backlog, `to-review`,
pre-gate run passed 2026-07-03) currently reads "the user's conversational
input" only. Steering its question sequence by source-material type would be a
behavior change requiring a spec version bump, adapter re-stamps, and a re-run
of the five-point gate. Recommended for the operator's next skill revision
pass; not applied here to keep the passed pre-gate evidence valid.
