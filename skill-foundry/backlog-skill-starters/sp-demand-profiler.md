---
id: sp-demand-profiler
title: "Skill Primer Brief — Demand Profiler"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[portfolio-profiler]]", "[[jira-portfolio-ingest]]"]
---

# Skill Primer Brief — Demand Profiler

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-demand-profiler.md`.

## Purpose

Discovers a service's **work item types** at a usable level of abstraction and
measures the **arrival rate, pattern, and variability** of each (STATIK step 3),
from a bound Jira set where one exists and from structured elicitation where it
does not.

Work item type discovery is the consequential half: every downstream STATIK step
analyses, models, and designs *per type*, so a bad type set propagates into the
capability analysis, the workflow model, the classes of service, and the board.
It replaces the two standard failures — adopting the board's issue-type field as
the type set, and answering arrival rate from memory in a workshop.

## Triggering intent

**Fires on** — Stage 03 of `statik-adoption`, and standalone on:

- "What kinds of work actually arrive here?"
- "What are our work item types?"
- "How much demand do we get, and how bumpy is it?"
- "Is our demand steady or spiky?"

**Does not fire on (near-misses):**

- **Profiling a backlog's current state for triage.** That is
  `portfolio-profiler`: status/assignee/priority distributions, age ranking,
  field completion. Its unit is the *item*, its purpose is triage, and it is
  point-in-time. This skill's unit is the *type*, its purpose is system design,
  and it is inherently longitudinal — arrival over time is the whole point.
  Neither substitutes for the other; both briefs state this in both directions.
- **Binding or normalizing the source.** That is `jira-portfolio-ingest`, which
  this skill consumes the output of. This skill never queries or normalizes.
- **Measuring how well work is delivered.** That is `flow-capability-analyzer`
  (STATIK step 4). Demand is what arrives; capability is what gets out.
- **Deciding urgency treatment.** Classes of service are
  `class-of-service-designer`. Type is what the work is, not how urgent it is.

## Method sketch

1. **Do not start from the issue-type field.** It is an administrative artifact —
   often a project template nobody chose, often three types doing the work of
   eight. Derive candidate types from what the request *is and what it takes to
   serve it*: cluster on summary text, requesting group, and work shape.
2. **Compare clusters against the issue-type field and report disagreements**
   with item counts. Disagreements are findings for the reviewer, never
   reconciled silently.
3. **Propose an abstraction level and show one coarser and one finer**, each with
   the type count it yields. The failure is in both directions — too abstract and
   every type gets the same policy; too granular and types carry three items a
   year. Showing alternatives makes the reviewer choose rather than ratify.
4. **Apply the discrimination test to every proposed type.** A type earns its
   place only if it is expected to differ from siblings in at least one of: the
   workflow it passes through, its lead-time distribution, or the customer
   expectation attached to it. Differing in none makes it a *label* — merge it and
   say so. This test is what keeps type discovery from drifting back into
   mirroring the issue-type field.
5. **Measure arrival rate per type** — always a number per stated unit over a
   stated window. Never "a lot" or "steady."
6. **Measure the arrival pattern across at least two time framings** (e.g. weekly
   and monthly). The same average hides very different systems, and a pattern
   invisible at one granularity is usually obvious at another. Characterize
   variability — this is what drives WIP limits and capacity allocation
   downstream, and an average alone supports neither.
7. **Ask for demand the board never saw** — chat requests, corridor asks, work
   taken through an untracked queue. Record it as a named type where it forms
   one, marked `unmeasured`. An unmeasured type is a finding about the board as
   much as about the demand.
8. **Attach customer expectation per type**, from the fitness criteria and
   external dissatisfaction sets. A type with no attached expectation produces a
   class of service nobody asked for.
9. **Tag every figure `measured` or `estimated`**, in every mode including
   all-estimated runs, and never place the two in the same column.
10. **Check each type against the sufficiency floor** and mark those below it, so
    the capability analysis reports observations rather than a distribution.

### Known failure modes to guard against

- **Adopting the issue-type field as the type set** — the failure the whole first
  half of the method exists to prevent.
- **Presenting one abstraction level as the only option**, which converts the
  reviewer's choice into a rubber stamp.
- **Skipping the discrimination test** for a type that "obviously" belongs.
- **Reporting an average arrival rate with no pattern**, which supports no WIP
  limit and no allocation.
- **Silently omitting unmeasured demand** because it is not on the board.
- **Mixing estimated and measured figures in one column.**
- **Producing any per-person figure.** Assignee data is aggregate-only here.

## Inputs and data boundary

Reads: the normalized item set and field-availability report from
`jira-portfolio-ingest`; the service frame with customer groups; the fitness
criteria and external dissatisfaction sets; the mode declaration.

Max data-class: `internal`. Clustering reads summary and description text
carrying customer references and hostnames — cluster *labels* are house-authored
abstractions and must not quote identifying content from the items behind them.
Assignee data is used only in aggregate and only where it bears on demand
routing; no per-person figure of any kind, and the skill declines that framing
explicitly.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01. `portfolio-profiler` was
examined and rejected for reuse on unit-of-analysis grounds — the collision
analysis is recorded in
`flow-foundry/decision-log/2026-08-01-statik-adoption-triage-and-scaffold.md` §8.

## Definition of done

1. A test board whose issue-type field disagrees with the work's actual shape
   produces a derived type set plus an explicit disagreement list — not a mirror
   of the field.
2. Three abstraction levels are always shown with their type counts; a run that
   presents only the chosen level fails.
3. A proposed type that differs from a sibling in none of the three
   discrimination dimensions is merged, with the merge stated.
4. Arrival rate is always a number per stated unit over a stated window; a test
   feeding vague input produces an elicited number tagged `estimated`, never a
   qualitative phrase.
5. Pattern is reported across at least two time framings, and a spiky demand
   whose spikes are invisible weekly is caught monthly.
6. Unmeasured demand raised in conversation appears in the type set marked
   `unmeasured`.
7. Every type carries an item count checked against the floor, with `below floor`
   marks applied before the capability analysis begins.
8. Measured and estimated figures never share a column, in any mode.
9. A collision test against `portfolio-profiler` confirms the boundary in both
   directions: "what does our backlog look like" routes there, "what kinds of
   work arrive and how often" routes here.
