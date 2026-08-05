---
id: decision-2026-08-05-progressive-disclosure-compaction
title: "Decision Log — Progressive-Disclosure Compaction (HUB.md)"
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
  - "[[fp-statik-adoption]]"
---

# Decision Log — 2026-08-05 — Progressive-Disclosure Compaction

**What was decided:** compact `HUB.md`'s "Known gaps" section (94 of 294
lines) to the pointer-plus-citation discipline in
`methodology/governance-and-audit.md` §5a. This flowspace's own
`decision-log/` folder held no dated entries before this one — its gap
citations point to `flow-foundry/decision-log/` and
`skill-foundry/decision-log/`, which were left unchanged. **By whom:**
operator, as part of a repo-wide pass triggered by `ai-refinement/HUB.md`'s
bloat (see
`flow-foundry/decision-log/2026-08-05-pointer-section-discipline.md`).
**Alternatives considered:** pilot on `ai-refinement` only (rejected — full
repo-wide scope chosen). **Reason:** §5a; no guardrail, schema, or
behavior changed. **What it affects:** `HUB.md` (1.2 → 1.3, 294 → 269
lines; stays `to-review`, no demotion needed).
