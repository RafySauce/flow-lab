---
id: decision-2026-07-03-skill-review-queue-added
title: "Decision Log — Review Staging Queue Added (review-skills/)"
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
  - "[[decision-2026-07-03-flow-review-queue-added]]"
---

# Decision Log — 2026-07-03 — Review Staging Queue Added

**What was decided:** each foundry gains a staging queue for finished work —
here, `skill-foundry/review-skills/`. §4's stamp-and-stage step now moves the
built skill folder (`<slug>/SKILL.md` + `adapters/`) there from
`backlog-skill-starters/` at `truth-level: to-review`; the primer brief stays
in the backlog as the intake record; the operator runs the five-point gate and
either promotes the skill to `../produced-skills/` or returns it. **By whom:**
agent, on operator instruction (same instruction as the flow-foundry
companion entry). **Alternatives considered:** leaving finished builds in the
backlog (rejected — the five staged `ai-refinement` skills already showed
review-ready folders drowning among `sp-*` starters). **What it affects:**
`foundry-spec.md` §4–§5 (changelog 1.3), `CONTEXT.md`,
`backlog-skill-starters/CONTEXT.md`, `../produced-skills/CONTEXT.md`, repo
`AGENTS.md`, `README.md`. Promotion semantics unchanged — the staging move in
is the foundry's; every move out is the operator's. The five built
`ai-refinement` skill folders were not relocated in this change — they
predate the queue and move when next touched or at the operator's word.
