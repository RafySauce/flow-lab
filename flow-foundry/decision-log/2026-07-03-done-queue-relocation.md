---
id: decision-2026-07-03-flow-done-queue-relocation
title: "Decision Log — DONE Queue Relocated to icp-flows/; Invocation Gate Added"
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
  - "[[decision-2026-07-03-skill-done-queue-relocation]]"
---

# Decision Log — 2026-07-03 — DONE Queue Relocation + Invocation Gate

**What was decided:** (a) the flow-foundry's DONE queue moved from
`flow-foundry/completed-flowspaces/` to the repo's top-level `icp-flows/`, so
finished, operator-verified flow designs are findable without entering the
foundry; (b) both foundries gained an invocation gate (foundry-spec §1
Step 0 + AGENTS.md rule 2): foundry work runs only after restating the starter
and intended outputs and receiving the operator's explicit go-ahead.
**By whom:** agent, on operator instruction. **What it affects:**
`foundry-spec.md` (1.2), `CONTEXT.md`, `backlog-flow-starters/CONTEXT.md`,
repo `AGENTS.md` (directory map, "Find it fast" table, rules), `README.md`
diagram, and the `ai-refinement` HUB (1.6, path wording only). Promotion
semantics are unchanged — `icp-flows/` remains human-placed, `verified` only.
The queue was empty at the moment of the move, so nothing was relocated.
Decision-log entries written before this date reference the old path by
design — logs are append-only records of what was true when written.
