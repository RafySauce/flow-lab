---
id: decision-2026-08-01-statik-adoption-skill-batch-promotion
title: "Decision Log — STATIK Adoption Skill Batch Promoted to verified on a Full Agent-Run Gate, Including a Simulated End-to-End Run"
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
  - "[[decision-2026-08-01-statik-adoption-skill-batch]]"
  - "[[sp-fitness-and-dissatisfaction-profiler]]"
  - "[[sp-demand-profiler]]"
  - "[[sp-flow-capability-analyzer]]"
  - "[[sp-workflow-modeler]]"
  - "[[sp-class-of-service-designer]]"
  - "[[sp-kanban-system-designer]]"
  - "[[statik-adoption]]"
---

# Decision Log — 2026-08-01 — STATIK Adoption Skill Batch Promoted

**What was decided:** promote all six statik-adoption skills `to-review` →
`verified` and move them from `skill-foundry/review-skills/` to
`produced-skills/`: `fitness-and-dissatisfaction-profiler`,
`demand-profiler`, `flow-capability-analyzer`, `workflow-modeler`,
`class-of-service-designer`, `kanban-system-designer`. **By whom:** the
operator (Rafy) — explicit instruction this session to test whichever
skills had not had a dry run, ahead of opening a PR.

## Unlike the other 2026-08-01 batches: no pre-run existed

This batch's own build log
(`2026-08-01-statik-adoption-skill-batch.md`, §7) states plainly: "the
five-point gate has **not** been run... no agent-side gate pre-run was
performed here — no spec review pass, no simulated live test per adapter,
no trigger check, no boundary/collision check beyond the three resolutions
recorded [there]. All five gate points remain outstanding for all six
skills." This entry runs the full gate from scratch, not just the live-test
item.

## Gate item 1 — spec review — pass

All six specs: purpose sharp, triggering intent names misfires, boundaries
explicit and mutually naming (each spec's "What this skill is not" section
cross-references its nearest neighbor, e.g. `demand-profiler` ↔
`portfolio-profiler`, `workflow-modeler` ↔ `process-decomposition`,
`class-of-service-designer` ↔ `closure-scorer`/`disposition-packet-builder`).
No placeholder/TODO/template-remnant text found in any of the six specs or
their adapters. Each carries its required Mermaid Flow Diagram; all
decision/halt branches in each diagram trace to a numbered Method step.

## Gate item 2 — live test — simulated end-to-end run

One synthetic service ("Network Change Service," three board issue types:
Change Request, Standard Change, Emergency Change) was walked through all
six skills in STATIK order, checked against each skill's own numbered
Review criteria, deliberately constructed to exercise the flow's own
documented loop-backs rather than avoid them:

- **`fitness-and-dissatisfaction-profiler`** — all 8 criteria met.
  Recipient and dependant criteria elicited separately; the "what did you
  stop asking for" question surfaced demand later picked up by
  `demand-profiler` as an unmeasured type; one dissatisfaction item routed
  to the out-of-scope list (a scheduling complaint, not about flow); a
  board-signal discrepancy (near-zero reopen rate contradicting a "redone
  twice" complaint) was reported for human resolution rather than used to
  overrule the stated complaint; no individual was named anywhere.
- **`demand-profiler`** — all 10 criteria met. Two of three issue types
  merged on the discrimination test (identical distributions, workflow, and
  expectation); the third stayed distinct on all three dimensions; three
  abstraction levels were shown; arrival was reported as a number per
  window with two time-granularity framings surfacing a month-end spike
  invisible at the weekly grain; a below-floor type was correctly flagged
  ahead of the capability stage; an unmeasured type (surfaced by the
  profiler above) was recorded rather than dropped.
- **`flow-capability-analyzer`** — all 10 criteria met, including a
  supplementary micro-test of the no-history degrade path (confirmed an
  explicit `unavailable` block naming what was lost, sections not omitted).
  Lead time reported as percentiles with a declared, not-yet-ratified
  measurement start point; a bimodal distribution was correctly surfaced as
  a split candidate rather than split in place — feeding the flow's own
  documented Stage 4→3 loop-back; arrival-vs-throughput and the 95/50
  predictability spread were both computed and compared explicitly; a
  simulated request for individual cycle time was declined with a stated
  reason.
- **`workflow-modeler`** — all 10 criteria met, including a supplementary
  micro-test confirming the skill declines to run without delivery-team
  input. All four board/account disagreement types were exercised (a queue
  masquerading as an activity, an activity with no status, an unused
  status, and a status meaning different things per type); the commitment
  point was set later than item creation, correctly triggering the
  **recomputation directive** — the flow's single most consequential
  check — rather than silently adjusting prior figures; one shared model
  with typed exceptions was chosen over a forced merge, reasoned.
- **`class-of-service-designer`** — all 10 criteria met. Invoked first
  against a deliberately stale capability basis (the recomputation
  directive above still outstanding): correctly **stopped** rather than
  deriving classes from stale figures. Re-invoked after the simulated
  loop-back resolved: three classes derived (no fixed-date class, omission
  recorded and reasoned); the independence rule was satisfied by design
  (Expedite carries two types, and one type appears in two classes) rather
  than collapsing into one-class-per-type; the intangible case was
  cross-checked against a real deferred-maintenance complaint; expedite
  carried a hard concurrent limit and a role-based (never individual)
  invocation policy; capacity allocation was proposed only for the class
  with a measured mix, explicitly withheld for the other, with conventional
  figures kept in a separately labelled block.
- **`kanban-system-designer`** — all 10 criteria met, including a
  supplementary micro-test confirming a bare "just build me a board"
  request with no upstream analysis is declined with the missing inputs
  named. All seven canvas elements were produced; one WIP limit was
  correctly marked `derived` and shown binding (below observed
  concurrency), a second was correctly flagged non-binding with a stated
  reason, and a third (no residency data) was correctly marked
  `starting point` only; every cadence named the decision it is empowered
  to make; the per-person exclusion was written into the metric set itself;
  one design element (a swimlane convention) was correctly flagged
  `convention — no evidence trace` rather than silently justified or
  dropped; both dissatisfaction sets were checked, with the one
  process/tooling complaint outside Kanban scope stated as still
  unaddressed rather than silently absorbed.

No defects were found in any of the six specs.

## Gate item 3 — trigger check — pass

Each spec's fires-on was walked against its five siblings' and the (then)
twenty-six produced skills' near-miss lists. The closest pairs —
`demand-profiler` vs `portfolio-profiler` (unit and time-dimension split),
`fitness-and-dissatisfaction-profiler` vs `context-elicitation` (service vs.
one work item), `workflow-modeler` vs `process-decomposition` (states of a
type vs. steps within one item's execution) — are each disambiguated in
both directions, consistent with the three collision resolutions already
recorded in the batch-build entry.

## Gate item 4 — boundary/collision check — pass

The six are disjoint by stage and artifact (criteria/dissatisfaction →
demand → capability → workflow model → classes → system design), each
naming its neighbors explicitly. One unresolved boundary, inherited and not
closed here: `workflow-modeler` ↔ `process-decomposition` is stated on both
sides but untested, because `process-decomposition` (built for a different
flowspace) is itself still `to-review` and out of this batch's scope — left
open, not silently assumed fine.

## Gate item 5 — evidence

This entry, plus the companion flow-side edit to
`icp-flows/statik-adoption/HUB.md` (stage table, diagram colors, and
Known-gaps skill table corrected from "to-review — gate pending" to the
built/verified status — the flowspace's own `truth-level` unchanged).

**What remains open, explicitly:** no on-engine invocation for any of the
six. The flowspace design itself is **not** promoted by this entry — it
carries real unresolved operator items its own Known Gaps section already
lists (ServiceNow ingest not yet built, the ingest history delta with three
undecided options, two unreachable source articles, unratified
evidence-sufficiency floors) that a simulated skill-level test does not
touch.

## What it affects

Six skill folders moved `skill-foundry/review-skills/` →
`produced-skills/`, `truth-level` flipped to `verified` in each `SKILL.md`
(no spec content changed).
