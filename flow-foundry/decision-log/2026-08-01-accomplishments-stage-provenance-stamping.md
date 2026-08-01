---
id: decision-2026-08-01-accomplishments-stage-provenance-stamping
title: "Decision Log — Retroactive Provenance Stamping for accomplishments-digest / accomplishments-docx-finisher Stage CONTEXT.md Files"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-finisher]]"
  - "[[decision-2026-07-15-accomplishments-flowspaces-promotion]]"
---

# Decision Log — 2026-08-01 — Accomplishments Stage Provenance Stamping

**What was decided:** add provenance frontmatter (`id`, `type:
stage-context`, `stage`, `review-intensity`, `artifact-version`, `status`,
`truth-level: verified`, dates, `owner`, `source`, `generated-by`,
`data-class`, `related`) to all nine stage `CONTEXT.md` files across
`accomplishments-digest` (6 stages) and `accomplishments-docx-finisher` (3
stages), which carried none at all. **By whom:** agent, found during this
session's broader review of `icp-flows/` for gaps and inconsistencies.

**What was checked:** both flowspaces' `HUB.md` are already `truth-level:
verified` with recorded review evidence
(`flow-foundry/decision-log/2026-07-15-accomplishments-flowspaces-promotion.md`),
whose Gate 1 (structural completeness) explicitly requires "every stage has
a `CONTEXT.md` with all six fields populated." The stage content itself was
already complete and populated — only the frontmatter block was absent.
Both flowspaces were scaffolded 2026-07-08, before `provenance-spec.md`
1.1 (2026-07-15) documented the `stage-context` type and its `stage`/
`review-intensity` fields as a schema the other flowspaces (`ai-refinement`,
`documentarian`) had already been stamped with; these two were simply never
retrofitted when the spec caught up to house practice.

**This is not a new promotion decision.** `truth-level: verified` is
applied here to match the parent flow's own already-evidenced verified
status, not as an independent Gate 3 human dry-run of these nine stages
individually — the original promotion entry above is the review evidence
this stamping inherits. `created`/`updated` dates are backdated to match
each flow's `HUB.md` (2026-07-08 / 2026-07-15) rather than stamped with
today's date, since no stage content changed.

**What it affects:** nine `CONTEXT.md` files gain frontmatter only; no
prose content was edited. `review-intensity` per stage is taken directly
from each `HUB.md`'s existing Stage table.
