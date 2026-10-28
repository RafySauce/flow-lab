---
id: decision-2026-10-28-accomplishments-digest-2-0-swap-and-deprecations
title: "Decision Log — Accomplishments Digest 2.0 Replaces 1.3; Finisher and Enricher Deprecated"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-28
updated: 2026-10-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-finisher]]"
  - "[[repo-context-enricher]]"
  - "[[decision-2026-10-27-accomplishments-digest-m365-servicenow-revision]]"
---

# Decision Log — 2026-10-28 — Accomplishments Digest 2.0 Swap and Deprecations

**What was decided:** the staged 2.0 copy of `accomplishments-digest` replaces
the 1.3 in `icp-flows/`, and the two proposed deprecations from the 2.0
revision log are applied. **By whom:** the operator, by approving this change;
the agent made the edits at the operator's direction and judged no readiness.

- **2.0 lands at `to-review`, the same truth-level the 1.3 carried.** No
  `verified` stamp is applied; the three validation gates and the skill gates
  stay with the operator. 1.3's decision-log history travels inside the 2.0
  copy; its Stage 6 handoff template is retired with that stage.
- **`accomplishments-docx-finisher`:** `status: replaced`, superseded by
  `accomplishments-digest` (Stage 9), `truth-level: deprecated`, banner added.
- **`repo-context-enricher`:** `status: dead` (no replacement),
  `truth-level: deprecated`, banner added; its `START-HERE.md` degrade line is
  replaced by the digest's Microsoft 365 / ServiceNow reduced-input path.
- **The five new and revised skills stay in `skill-foundry/review-skills/`**,
  with their briefs in the backlog, until each passes the five-point gate.
