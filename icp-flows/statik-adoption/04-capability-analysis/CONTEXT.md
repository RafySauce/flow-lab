---
id: statik-adoption-stage-04
title: "Stage 04 — Capability Analysis"
type: stage-context
stage: 4
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[statik-adoption]]"
  - "[[flow-capability-analyzer]]"
  - "[[board-evidence-requirements]]"
---

# Stage 04 — Capability Analysis

Covers **STATIK step 4**: what the service is actually capable of delivering,
from historical data — lead time, throughput, predictability, quality, and
conformance — measured per work item type and tested against the fitness
criteria the customers stated. This is where "we usually turn those around in a
couple of weeks" meets the record.

## Inputs

| Input | Source | Required |
|---|---|---|
| Work item type set, with `below floor` and `unmeasured` marks | `work/03-work-item-types.md` | Yes |
| Demand profile per type | `work/03-demand-profile.md` | Yes |
| Customer expectation per type | `work/03-expectations.md` | Yes |
| Amended fitness criteria | `work/01-fitness-criteria.md` + `work/02-criteria-amendments.md` | Yes |
| History-availability finding | `work/01-history-availability.md` | Yes |
| Bound item set | `work/01-bound-set.md` | Only in evidence-grounded mode |
| Mode declaration (step 4 row) | `work/01-mode-declaration.md` | Yes |

## Process

1. **Fix the measurement start point and declare it.** Lead time is measured
   from a stated point, and which point is chosen changes every number. Stage 05
   has not yet set the commitment point, so this stage measures from item
   creation, **declares that it did**, and flags itself for recomputation if
   Stage 05's ratified commitment point differs. This is the flow's most likely
   loop-back (5 → 4) and it is expected, not exceptional.
2. **Report lead time as a distribution, never as an average.** Report the 50th,
   85th, and 95th percentiles per type, with the observation count and window.
   An average lead time is the single most misleading number in flow analysis:
   knowledge-work lead times are right-skewed, so the mean sits above the median
   and describes no actual item, and a customer commitment made against an
   average is missed roughly half the time by construction. Where a type is
   marked `below floor` by Stage 03, report its individual observations as a
   list and label them observations — never percentiles over a handful of items.
3. **Report throughput per type** — items completed per unit time, same unit as
   the arrival rate in Stage 03 so the two are directly comparable. **Compare
   them explicitly**: a type whose arrival rate exceeds its throughput has a
   queue that grows without bound, and that comparison is often the single most
   actionable finding in the whole run.
4. **Report predictability as spread, not as a separate score.** The ratio of
   the 95th to the 50th percentile per type is the workable measure: a type
   delivering in 3 days at the median and 40 at the 95th is unpredictable
   regardless of how good the median looks. Predictability is what most
   customers actually mean when they say they want things faster, and separating
   it from raw speed is usually the finding that reframes the Stage 08
   conversation.
5. **Report due-date performance where due dates exist** — the proportion of
   items met, and the distribution of lateness for those missed. Where the field
   is absent or unpopulated, report `unavailable`, never "no due dates," which is
   a different and much stronger claim about the service.
6. **Report per-state residency where history allows.** Time spent in each state,
   per type, split into *working* and *waiting* wherever Stage 05's activity/
   queue distinction can be anticipated from state names. Flow efficiency —
   working time over total lead time — is reported when it can be computed and
   marked `unavailable` when it cannot. This is the input that makes a WIP limit
   at Stage 07 defensible rather than guessed, and it is exactly what is lost
   when history is unavailable.
7. **Take the stated degrade path when history is unavailable, and say what was
   lost.** With Created and Resolved only, end-to-end lead time, throughput, and
   due-date performance are all still computable; per-state residency, flow
   efficiency, and blocked-time analysis are not. Report the degrade explicitly
   in the output rather than silently omitting the sections — a missing section
   reads as "nothing to report," which is a different claim from "not
   measurable here."
8. **Test capability against the fitness criteria and against customer
   expectation, per type.** For each criterion: what does the record say, and
   does it meet the expectation Stage 03 recorded? Emit a `meets` / `misses` /
   `unmeasurable` verdict per criterion per type, with the figure behind it.
   This table is the evidentiary core of the Stage 08 conversation.
9. **Surface type-splitting candidates.** A type whose lead-time distribution is
   clearly bimodal is usually two types that Stage 03 merged. Report it as a
   candidate loop-back to Stage 03 with the evidence; do not split it here.
10. **Present the capability profile and the criterion verdicts, then stop.**

`Layer-3: flow-capability-analyzer`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Capability profile per type | Lead-time percentiles (50/85/95) or labelled observations; throughput; arrival-vs-throughput comparison; predictability ratio; due-date performance or `unavailable`; observation count and window | `work/04-capability-profile.md` |
| Per-state residency | Working/waiting time per state per type, and flow efficiency — or an explicit `unavailable` block naming what was lost and why | `work/04-state-residency.md` |
| Fitness verdict table | One row per fitness criterion per type: criterion, expectation, measured figure, `meets`/`misses`/`unmeasurable` | `work/04-fitness-verdicts.md` |
| Measurement-basis declaration | The start point used (creation), the window, and the flag for recomputation if Stage 05 sets a different commitment point | `work/04-measurement-basis.md` |
| Type-split candidates | Types with bimodal distributions, with the evidence, as candidate loop-backs to Stage 03 | `work/04-split-candidates.md` |

## Verify

Trace **Stage 02 → Stage 04**: every fitness criterion in the amended criteria
set must appear in `work/04-fitness-verdicts.md` with a verdict of `meets`,
`misses`, or `unmeasurable` — and every `unmeasurable` must name which specific
data was absent (the field, or the history), not merely be left blank.

The failure mode this catches: a criterion that mattered enough for a customer
to state it silently drops out of the analysis because no convenient metric
existed, and Stage 08 presents a design that never addressed the thing the
customer complained about. `unmeasurable` is an acceptable and honest verdict;
absence is not. Running this check leaves a one-line result in the run's
decision log.

## Review

- **Reviewer:** the service owner, with the delivery team confirming that the
  figures match their lived experience of the work.
- **Intensity:** `light` — constrained execution. The computation is determined
  by the bound set and the stated rules; the reviewer checks that the numbers
  are recognizable and that the degrade paths were declared, rather than setting
  direction. A figure the team says is unrecognizable is a signal that the bound
  scope or the type set is wrong — that is a loop-back to Stage 01 or 03, not a
  judgment to be made here.
- **Evidence:** a decision-log entry naming the reviewers, the date, the
  measurement basis used, every `unavailable` section with its cause, and any
  loop-back raised.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- **This stage produces no per-person metric of any kind.** Lead time, throughput,
  and residency are reported per work item type and per state, never per
  assignee, and the stage declines that framing explicitly when asked. This is a
  data-handling constraint, not a presentation preference: individual flow
  metrics turn a Kanban rollout into an instrument of performance management,
  which ends the honest reporting every later stage depends on — and Stage 02's
  elicitation in particular cannot survive it.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
