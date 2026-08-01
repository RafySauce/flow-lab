---
id: sp-flow-capability-analyzer
title: "Skill Primer Brief — Flow Capability Analyzer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[demand-profiler]]", "[[jira-portfolio-ingest]]"]
---

# Skill Primer Brief — Flow Capability Analyzer

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-flow-capability-analyzer.md`.

## Purpose

Measures what a service actually delivers, from its historical record (STATIK
step 4): lead time as a **distribution**, throughput, predictability, due-date
performance, and per-state residency — per work item type, tested against the
fitness criteria the customers stated.

It replaces "we usually turn those around in a couple of weeks" with the record,
and it exists because flow metrics are the one part of STATIK where a board can
answer definitively and where doing the arithmetic wrong is both easy and
invisible.

## Triggering intent

**Fires on** — Stage 04 of `statik-adoption`, and standalone on:

- "How long does this kind of work actually take?"
- "What's our lead time distribution?"
- "Are we predictable?"
- "Do we hit our due dates?"
- "Where does the time actually go in this workflow?"

**Does not fire on (near-misses):**

- **Measuring what arrives.** That is `demand-profiler` (STATIK step 3). Demand
  is arrival; capability is delivery. This skill consumes the type set that one
  produces and never derives its own.
- **Per-person productivity analysis.** Explicitly refused — see the data
  boundary. A request for individual throughput or cycle time is declined with a
  stated reason, not silently reframed.
- **Scoring items for closure or triage.** That is `closure-scorer` in
  `portfolio-rationalization`. This skill measures the *system*, not the worth of
  individual items.
- **Gathering one engineer's own closed work for a review period.** That is
  `jira-accomplishments-gatherer` — different unit (person), different intent
  (evidence for a review).
- **Setting WIP limits.** That is `kanban-system-designer`, which consumes this
  skill's residency output.

## Method sketch

1. **Fix and declare the measurement start point.** Lead time is measured from a
   stated point and the choice changes every number. When invoked before the
   commitment point is ratified, measure from creation and **declare it**, with a
   recomputation flag for when the commitment point lands.
2. **Report lead time as a distribution — 50th, 85th, 95th percentiles — never as
   an average.** This is the load-bearing quality rule. Knowledge-work lead times
   are right-skewed: the mean sits above the median and describes no actual item,
   and a customer commitment made against an average is missed roughly half the
   time by construction. Below the per-type floor, report individual observations
   as a labelled list — never percentiles over a handful of items.
3. **Report throughput per type**, in the same unit as the arrival rate so the two
   are directly comparable, and **make the comparison explicitly**. A type whose
   arrival exceeds its throughput has an unboundedly growing queue, and that is
   frequently the single most actionable finding in a run.
4. **Report predictability as the 95th/50th spread**, not as a separate score. A
   type delivering in 3 days at the median and 40 at the 95th is unpredictable
   however good the median looks — and predictability is usually what customers
   mean when they say they want things faster.
5. **Report due-date performance where due dates exist** — proportion met, and
   lateness distribution for those missed. Absent or unpopulated field reports
   `unavailable`, never "no due dates," which is a different and much stronger
   claim.
6. **Report per-state residency where history allows**, split working versus
   waiting, with flow efficiency where computable. This is what makes a WIP limit
   defensible rather than guessed.
7. **Take the stated degrade path when history is absent, and name what was
   lost.** With Created and Resolved only: lead time, throughput, and due-date
   performance still compute; residency, flow efficiency, and blocked-time
   analysis do not. Report the degrade as an explicit block rather than omitting
   the sections — a missing section reads as "nothing to report," a different
   claim from "not measurable here."
8. **Verdict every fitness criterion per type** — `meets` / `misses` /
   `unmeasurable`, with the figure behind it, and every `unmeasurable` naming the
   specific absent data. This table is the evidentiary core of the socialization
   conversation.
9. **Surface bimodal distributions as type-split candidates** for a loop-back to
   demand analysis. Report the evidence; never split the type here.

### Known failure modes to guard against

- **Reporting an average lead time.** The single most misleading number in flow
  analysis, and the one every stakeholder asks for by name.
- **Computing percentiles over too few items** because the type was ratified
  qualitatively.
- **Silently omitting a section** when its data is unavailable.
- **Carrying a stale measurement basis forward** after the commitment point moves
  — the flow's most consequential undetectable error.
- **Producing any per-person figure**, including when asked directly.
- **Reporting throughput without comparing it to arrival**, which discards the
  most actionable comparison available.
- **Dropping a fitness criterion** because no convenient metric existed.
  `unmeasurable` is honest; absence is not.

## Inputs and data boundary

Reads: the work item type set with floor marks; the demand profile (for the
arrival comparison); the fitness criteria and per-type expectations; the
history-availability finding; the normalized item set from
`jira-portfolio-ingest`; the mode declaration.

**Named input gap, carried from the flowspace:** `jira-portfolio-ingest` emits a
*point-in-time* item set and does not carry status-transition history. This skill
declares history as an input requirement with the §7 degrade path, so it runs
either way, but per-state residency requires an unresolved operator decision —
extend that skill, request history here, or accept the degrade permanently. Not
resolved by this brief.

Max data-class: `internal`. **No per-person metric at any point** — lead time,
throughput, and residency are per type and per state, never per assignee, and the
skill declines that framing explicitly when asked. This is a data-handling
constraint, not a presentation preference: individual flow metrics turn a Kanban
rollout into performance management, which ends the honest reporting the rest of
the method depends on.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01. Nothing in the house
toolkit computes flow metrics; `closure-scorer` and `portfolio-profiler` both
read Jira but neither measures delivery over time.

## Definition of done

1. Lead time is reported as percentiles in every sufficient case; a test
   requesting "the average" returns the distribution with a stated reason, not
   the mean.
2. A type below the completed-item floor yields labelled observations, never
   percentiles.
3. Arrival-versus-throughput is compared explicitly per type, and a type with
   arrival exceeding throughput is called out.
4. Predictability is reported as spread; a good-median/bad-tail type is correctly
   identified as unpredictable.
5. The no-history degrade path is exercised: residency and flow efficiency appear
   as an explicit `unavailable` block naming the cause, not as missing sections.
6. An absent due-date field yields `unavailable`, never "no due dates."
7. Every fitness criterion receives a verdict, and every `unmeasurable` names the
   specific missing data.
8. A commitment-point change triggers the recomputation flag rather than an
   in-place adjustment or a footnoted carry-forward.
9. A direct request for per-person cycle time is declined with a stated reason.
10. A bimodal type is surfaced as a split candidate with evidence, and is not
    split by this skill.
