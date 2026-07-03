---
id: decision-2026-07-03-skill-done-queue-relocation
title: "Decision Log — DONE Queue Relocated to produced-skills/; Invocation Gate Added"
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
  - "[[skill-foundry-spec]]"
  - "[[decision-2026-07-03-flow-done-queue-relocation]]"
---

# Decision Log — 2026-07-03 — DONE Queue Relocation + Invocation Gate

**What was decided:** (a) the skill-foundry's DONE queue moved from
`skill-foundry/completed-skills/` to the repo's top-level `produced-skills/`,
so finished, operator-verified skills are findable without entering the
foundry; (b) both foundries gained an invocation gate (foundry-spec §1
Step 0 + AGENTS.md rule 2): foundry work runs only after restating the starter
and intended outputs and receiving the operator's explicit go-ahead.
**By whom:** agent, on operator instruction. **What it affects:**
`foundry-spec.md` (1.2), `CONTEXT.md`, `backlog-skill-starters/CONTEXT.md`,
repo `AGENTS.md`, and `README.md` — see the companion flow-foundry entry for
the full shared list. Promotion semantics are unchanged — `produced-skills/`
remains human-placed, `verified` only. The queue was empty at the moment of
the move, so nothing was relocated. The three 2026-07-03 entries in this log
that mention `completed-skills/` predate the move and keep their wording —
logs are append-only records of what was true when written.
