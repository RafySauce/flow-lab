---
id: decision-2026-08-05-pointer-section-discipline
title: "Decision Log — Pointer-Section Discipline (Governance + Template)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
data-class: public
related:
  - "[[governance-and-audit]]"
  - "[[flowspace-scaffold]]"
---

# Decision Log — 2026-08-05 — Pointer-Section Discipline

**What was decided:** add `methodology/governance-and-audit.md` §5a
("Pointer-section discipline" — Changelog and Known-gaps sections are
pointers, not archives: 1–3 sentences per entry, full rationale stays only
in the cited decision-log entry) and a §7 bullet on editorial-only passes
over `verified` artifacts (version bump + decision-log entry required;
re-promotion may be a lightweight check, not a full re-gate). Also updated
`flow-foundry/templates/flowspace-scaffold.md`'s HUB.md skeleton to state
the rule at the point of authorship. **By whom:** operator, applying the
Interpretable Context Methodology (ICM) sibling project's routing-file
discipline (`RinDig/icm-architect`) — user-raised, triggered by
`ai-refinement/HUB.md`'s Known-gaps section reaching 309 of 616 lines.
**Alternatives considered:** leave the convention as unwritten practice
(rejected — it had already drifted inconsistently across all six
flowspace HUB.md files). **Reason:** close the gap between the scaffold
template's original one-line "with ids and status" instruction and what
every flowspace actually accreted, so future flow-foundry builds don't
regress. **What it affects:** `governance-and-audit.md` (1.2 → 1.3);
`flowspace-scaffold.md` (unstamped, no version); triggered a compaction
pass across all six existing `icp-flows/*/HUB.md` files and
`ai-refinement`'s Stage 01, logged separately in each flowspace's own
decision-log.
