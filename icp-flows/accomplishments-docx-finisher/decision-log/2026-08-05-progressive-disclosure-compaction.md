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
  - "[[fp-accomplishments-docx-finisher]]"
---

# Decision Log — 2026-08-05 — Progressive-Disclosure Compaction

**What was decided:** compact `HUB.md`'s "Known gaps" section (29 of 137
lines) to the pointer-plus-citation discipline in
`methodology/governance-and-audit.md` §5a. **By whom:** operator, as part
of a repo-wide pass triggered by `ai-refinement/HUB.md`'s bloat (see
`flow-foundry/decision-log/2026-08-05-pointer-section-discipline.md`).
**Alternatives considered:** pilot on `ai-refinement` only, leave this file
untouched (rejected — full repo-wide scope chosen). **Reason:** §5a; no
guardrail, schema, or behavior changed — every cited decision-log link was
preserved. **What it affects:** `HUB.md` (1.1 → 1.2, 137 → 135 lines,
`verified` → `to-review`). Re-promotion per §7 may be a lightweight
structural re-check, not a full re-gate.
