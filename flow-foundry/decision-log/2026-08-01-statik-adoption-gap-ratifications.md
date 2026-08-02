---
id: decision-2026-08-01-statik-adoption-gap-ratifications
title: "Decision Log — STATIK Adoption: Ingest History-Delta Resolution"
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
  - "[[statik-adoption]]"
  - "[[board-evidence-requirements]]"
  - "[[flow-capability-analyzer]]"
  - "[[jira-portfolio-ingest]]"
  - "[[decision-2026-08-01-statik-adoption-triage-and-scaffold]]"
---

# Decision Log — 2026-08-01 — STATIK Adoption: Ingest History-Delta Resolution

**What was decided:** the open "ingest history delta" question in `HUB.md`
and `reference/board-evidence-requirements.md` §4 — closed by taking option
(c), accepting the point-in-time-only degrade path permanently. **By whom:**
the operator, answering directly against the three options the original
triage-and-scaffold decision left open (§7 of
`2026-08-01-statik-adoption-triage-and-scaffold.md`).

## The question

`jira-portfolio-ingest` emits a point-in-time normalized item set. Stage 04's
capability analysis wants status-transition history — when each item entered
and left each state — to report per-state residency, flow efficiency, and
blocked-time analysis, and to let Stage 07 *derive* WIP limits from measured
concurrency rather than propose them as starting points. Three options were on
the table, none taken at scaffold time:

(a) Extend `jira-portfolio-ingest` with an optional history mode.
(b) Have `flow-capability-analyzer` request history itself, splitting ingest
    across two paths.
(c) Accept the degrade path permanently.

## Answer

**(c).** No build follows from this decision.

## Why this needed no build work

`flow-capability-analyzer` already implements the degrade path as designed:
end-to-end lead time, throughput, arrival-versus-throughput comparison, and
due-date performance, all computed from `Created`/`Resolved` alone, with the
degrade stated explicitly in its output rather than omitted. It already
declares history as a desired-not-required input carrying this exact degrade
path. Taking option (c) confirms the skill's existing behavior as final rather
than provisional — nothing in its `SKILL.md`, adapters, or Stage 04
`CONTEXT.md` needed to change.

## What's foreclosed by this decision

Options (a) and (b) are not merely deferred — they are the paths *not* taken.
In particular, (a) would have changed `jira-portfolio-ingest`'s behavior for
every consumer, including `portfolio-rationalization`'s promoted dependency on
it; (c) means that coordination cost is avoided, not postponed. If a future
need for per-state residency emerges (a real Stage 04 run where tuned WIP
limits prove materially wrong), that reopens this decision — it does not
silently reappear as an implicit assumption.

## What's lost, unchanged from the original framing

- No per-state residency, no flow efficiency, no blocked-time analysis at
  Stage 04.
- Stage 07's WIP limits stay tuned starting points, not derived figures —
  already labelled as such wherever they appear in Stage 07's design.

## Changes made

- `reference/board-evidence-requirements.md` §4 — the "open (operator call)"
  paragraph reworded to record the resolution and its rationale.
  `artifact-version` 1.0 → 1.1.
- `HUB.md` Known gaps — "ingest history delta (open, operator call)" reworded
  to "resolved 2026-08-01," citing this entry.
- `decision-log/CONTEXT.md` — dropped the history resolution from the
  "instantiation-time decisions" list (item 2); it's resolved at design time
  now, not a per-instance call. Renumbered the remaining list to two items.

## Notes

- This is a design-time decision on public design copy — no instance exists,
  no run happened.
- The other two statik-adoption gaps this session addressed operator input on
  are recorded separately: ServiceNow ingest (build authorized — see the
  servicenow-ticket-ingest skill-build decision log once filed) is a build
  decision, not a design-copy edit, and is tracked through the skill-foundry
  pipeline rather than here.
