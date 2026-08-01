---
id: statik-adoption-stage-03
title: "Stage 03 — Demand Analysis"
type: stage-context
stage: 3
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
  - "[[demand-profiler]]"
  - "[[board-evidence-requirements]]"
---

# Stage 03 — Demand Analysis

Covers **STATIK step 3**: the nature of demand. Who asks, what they ask for, how
often, in what pattern, and with what expectation. Work item type discovery
happens here, and it is the single most consequential output of the stage —
every subsequent stage analyses, models, and designs *per work item type*.

## Inputs

| Input | Source | Required |
|---|---|---|
| Service frame with customer groups | `work/01-service-frame.md` | Yes |
| Bound item set + field-availability report | `work/01-bound-set.md` | Only in evidence-grounded mode |
| Mode declaration (step 3 row) | `work/01-mode-declaration.md` | Yes |
| External dissatisfaction set | `work/02-dissatisfaction-external.md` | Yes |
| Amended fitness criteria | `work/01-fitness-criteria.md` + `work/02-criteria-amendments.md` | Yes |
| Known unmeasured demand — requests handled outside the board | Operator / delivery team | Yes |

## Process

1. **Propose candidate work item types, and do not start from the issue-type
   field.** The board's issue types are an administrative artifact — often a
   Jira project template nobody chose, often three types doing the work of
   eight, often eight doing the work of two. Derive candidates from what the
   request *is and what it takes to serve it*: cluster the bound set on summary
   text, requesting group, and the shape of the work, then compare the clusters
   against the issue-type field and report where they disagree. The
   disagreements are findings for the reviewer, not noise to reconcile silently.
2. **Set the abstraction level deliberately, and show the alternatives.** Type
   discovery is the hard part of this step, and the failure is in both
   directions: too abstract ("requests") gives every type the same policy and
   the system distinguishes nothing; too granular (one type per menu item)
   gives types with three items a year and no measurable distribution. Propose a
   level, state the count it yields, and show one level coarser and one level
   finer with their counts so the reviewer chooses against real alternatives
   rather than approving the only option offered.
3. **Apply the discrimination test to each proposed type.** A work item type
   earns its place only if it is expected to differ from its siblings in at
   least one of: the workflow it passes through, its lead-time distribution, or
   the customer expectation attached to it. A type that differs in none of these
   is a *label*, not a type — merge it and say so. This is the test that keeps
   type sets honest; without it, type discovery drifts back into mirroring the
   issue-type field.
4. **Measure arrival rate per type.** Requests per unit time — always a number
   per unit, never "a lot" or "steady." State the unit and the observation
   window explicitly. Where the mode declaration says conversation-only, elicit
   an estimate and label it an estimate in the output; never present an elicited
   figure in the same column as a measured one.
5. **Measure the arrival pattern, not just the rate.** The same average hides
   very different systems: smooth arrival, weekly or monthly spikes,
   quarter-end clustering, or burst-driven arrival tied to an external event.
   Report the pattern per type across at least two time framings (e.g. by week
   and by month) — a pattern invisible at one granularity is usually obvious at
   another. Arrival *variability* is what drives WIP limits and capacity
   allocation at Stage 07; an average alone cannot support either.
6. **Record demand that the board never saw.** Requests taken by chat, by
   corridor conversation, or by a queue this service does not track are still
   demand on the system, and they are systematically invisible to an
   evidence-grounded analysis. Ask for them explicitly, record them as a named
   type where they form one, and mark them `unmeasured` — an unmeasured type is
   a finding about the board as much as about the demand.
7. **Attach customer expectation per type.** From the fitness criteria and the
   external dissatisfaction set: what does the requesting group expect of *this
   type* — how fast, how predictable, by when. This is the input Stage 06 turns
   into classes of service, and a type with no attached expectation will produce
   a class of service nobody asked for.
8. **Present the type set with its counts, rates, patterns, expectations, and
   the disagreements against the issue-type field — then stop for
   ratification.**

`Layer-3: demand-profiler`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Work item type set | 3–8 types, each with: name, one-line definition, which discrimination test(s) it passes, item count in the bound set, and the issue-type value(s) it maps to (or `unmeasured`) | `work/03-work-item-types.md` |
| Demand profile per type | Arrival rate with its unit and window; pattern across two time framings; variability characterization; each figure tagged `measured` or `estimated` | `work/03-demand-profile.md` |
| Customer expectation per type | Expectation statement, the customer group holding it, and the fitness criterion it derives from | `work/03-expectations.md` |
| Abstraction-level record | The chosen level with the coarser and finer alternatives that were shown, their type counts, and the reviewer's rationale for the choice | `work/03-abstraction-record.md` |
| Issue-type disagreement list | Where derived clusters and the board's issue-type field disagree, with the item counts involved | `work/03-issue-type-disagreements.md` |

## Verify

Trace **Stage 03 → Stage 04**: every work item type in
`work/03-work-item-types.md` must carry an item count from the bound set, and
each count must be checked against the per-type sufficiency floor in
`reference/board-evidence-requirements.md` §3. Types below the floor are marked
`below floor` in the type set itself — before Stage 04 begins — so that Stage 04
reports observations for them rather than a distribution.

The failure mode this catches: a type set ratified on qualitative grounds (these
really are different kinds of work) where one or more types have too few
completed items to support any capability claim, and Stage 04 computes a
"distribution" over seven items that then justifies a WIP limit. Running this
check leaves a one-line result in the run's decision log.

## Review

- **Reviewer:** the delivery team, jointly — not the service owner alone. Work
  item type discovery is the one judgment the people doing the work are best
  placed to make, and a type set ratified only by the owner reliably mirrors how
  work is *reported* rather than how it is *done*.
- **Intensity:** `light` — constrained execution. The analysis is bounded by the
  bound set and the stated tests, and the reviewer's job is to accept, merge, or
  split proposed types against the discrimination test rather than to set
  direction. The judgment that would make this heavy (the abstraction level) is
  handled by forcing the alternatives into the open at step 2, so the reviewer
  chooses rather than ratifies.
- **Evidence:** a decision-log entry naming the reviewers, the date, the ratified
  type count, the abstraction level chosen over which alternatives, and every
  type marked `below floor` or `unmeasured`.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- Clustering reads issue summary and description text, which carries customer
  references and hostnames. Cluster *labels* are house-authored abstractions and
  must not quote identifying content from the items they were derived from.
- Assignee data is used only in aggregate, and only where it bears on demand
  routing. This stage produces no per-person figure of any kind and declines
  that framing explicitly.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
