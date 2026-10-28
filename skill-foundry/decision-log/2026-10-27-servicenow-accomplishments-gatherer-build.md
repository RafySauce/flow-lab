---
id: decision-2026-10-27-servicenow-accomplishments-gatherer-build
title: "Decision Log — ServiceNow Accomplishments Gatherer Built and Staged"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-servicenow-accomplishments-gatherer]]"
  - "[[servicenow-accomplishments-gatherer]]"
  - "[[servicenow-ticket-ingest]]"
---

# Decision Log — 2026-10-27 — ServiceNow Accomplishments Gatherer Built and Staged

**What was decided:** `sp-servicenow-accomplishments-gatherer` (primer-brief, clean path) was built as `review-skills/servicenow-accomplishments-gatherer/` at `to-review`, with a synthetic test fixture in `reference/`. **By whom:** the agent, on the operator's explicit go-ahead to build the five 2.0 skills. **Alternatives considered:** widening `servicenow-ticket-ingest` with a per-person mode (rejected: its aggregate-only guarantee protects `statik-adoption`); pointing to the flow's attribution probe only (rejected: the skill must run standalone, so the probe is inline in Method step 2 and the flow reference stays canonical). **What it affects:** nothing in the done queues. The primer brief stays in the backlog as the intake record; the operator still owns the five-point gate and the catalog rows (`produced-skills/CONTEXT.md`, `review-skills/CONTEXT.md`), and Stage 5's `Layer-3: TBD` line becomes a pointer on promotion.
