---
id: decision-2026-07-03-flow-review-queue-added
title: "Decision Log — Review Staging Queue Added (review-flowspaces/)"
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
  - "[[flow-foundry-spec]]"
  - "[[decision-2026-07-03-skill-review-queue-added]]"
---

# Decision Log — 2026-07-03 — Review Staging Queue Added

**What was decided:** each foundry gains a staging queue for finished work —
here, `flow-foundry/review-flowspaces/`. When a build and its agent-side
pre-checks are complete, the foundry moves it there from
`backlog-flow-starters/` at `truth-level: to-review`; the operator reviews
and either promotes it to `../icp-flows/` or returns it. **By whom:** agent,
on operator instruction ("each foundry needs a space for their work to be put
for quick human review and promotion"). **Alternatives considered:** leaving
finished builds in the backlog (rejected — review-ready work was
indistinguishable from raw starters, hiding exactly the items the operator
must act on). **What it affects:** `foundry-spec.md` §5 (now
staging + validation + promotion, changelog 1.3), `CONTEXT.md` (layout, queue
model), `backlog-flow-starters/CONTEXT.md`, `../icp-flows/CONTEXT.md` ("fed
from"), repo `AGENTS.md` (directory map, find-it-fast, rule 5), `README.md`
(diagram, house practice 5). Promotion semantics unchanged — the staging move
in is the foundry's; every move out is the operator's.
