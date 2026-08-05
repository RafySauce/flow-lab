---
id: decision-2026-08-05-progressive-disclosure-compaction
title: "Decision Log — Progressive-Disclosure Compaction (HUB.md + Stage 01)"
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
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[work-item-schemas]]"
---

# Decision Log — 2026-08-05 — Progressive-Disclosure Compaction

**What was decided:** compact `HUB.md`'s "Known gaps" section (309 of 616
lines) to the pointer-plus-citation discipline in
`methodology/governance-and-audit.md` §5a, and remove Stage 01's
transcribed persona (step 6) and schema (step 7) content in favor of
pointers to `reference/ai-refinement-hybrid.md` and
`reference/work-item-schemas.md`, matching Stage 06's existing delegation
pattern. **By whom:** operator, applying the Interpretable Context
Methodology (ICM) sibling project's routing-file discipline
(`RinDig/icm-architect`) — this flow was the stated trigger case, being
the largest and most-iterated in the repo. **Alternatives considered:**
leave as-is (rejected — context bloat was the reported problem). **Reason:**
§5a; no guardrail, schema, or behavior changed — every cited decision-log
link was preserved, only the surrounding narrative was removed. **What it
affects:** `HUB.md` (1.21 → 1.22, 616 → 466 lines, `verified` → `to-review`)
and `01-intake-and-guardrails/CONTEXT.md` (1.15 → 1.16, 521 → 511 lines,
`verified` → `to-review`). Re-promotion per §7 may be a lightweight
structural re-check (stage table / diagram / cross-reference integrity),
not a full five-point re-gate, since no Layer-3 skill or checklist item
changed.
