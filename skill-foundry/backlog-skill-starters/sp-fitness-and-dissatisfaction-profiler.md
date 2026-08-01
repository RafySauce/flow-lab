---
id: sp-fitness-and-dissatisfaction-profiler
title: "Skill Primer Brief — Fitness and Dissatisfaction Profiler"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[context-elicitation]]"]
---

# Skill Primer Brief — Fitness and Dissatisfaction Profiler

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-fitness-and-dissatisfaction-profiler.md`.

## Purpose

Elicits, for one named service, the **fitness criteria** its customers judge it
by (STATIK step 1) and the **sources of dissatisfaction** with it today (STATIK
step 2) — keeping internal and external dissatisfaction separate, attributing
every item to a source group rather than to a person, and connecting each
dissatisfaction to the fitness criterion it threatens.

It replaces the STATIK workshop's most commonly botched opening: a single
round-the-room "what's not working?" that merges customer and delivery
perspectives, produces complaints about named colleagues, and yields a list
nothing downstream can measure against.

## Triggering intent

**Fires on** — Stages 01–02 of `statik-adoption`, and standalone on:

- "What do our customers actually judge this service on?"
- "Run a dissatisfaction analysis for this service."
- "Why are people unhappy with how we deliver X?"
- "We need fitness criteria before we can measure anything."

**Does not fire on (near-misses):**

- **Framing one work item's problem context.** That is `context-elicitation`,
  whose unit is a *work item* and whose output is schema-ready fields for
  `ai-refinement`. This skill's unit is a *service*, and its output is criteria
  and dissatisfaction sets for a system design. The two ask superficially
  similar questions at completely different altitudes; the boundary is the unit
  of analysis and it is stated in both directions.
- **Stakeholder-register work.** `ai-refinement`'s register maps role-types,
  coalitions, and conflict axes for work-item tagging. This skill elicits what
  customer groups judge a service by. It reads a register where one exists but
  does not author or maintain one.
- **Retrospectives.** A retrospective examines a team's recent work; this
  examines a service's standing fitness. Adjacent, different.
- **Deciding what to do about the dissatisfaction.** That is the rest of the
  flowspace. This skill surfaces and structures; it proposes no remedy.

## Method sketch

1. **State the attribution rule before asking anything** — dissatisfaction is
   recorded against a source group, never a named person, and no artifact will
   carry individual attributions. Stated first, to participants, always. An
   unstated rule produces either sanitized non-answers or complaints about
   colleagues.
2. **Separate customer groups into recipients and dependants.** Dependants
   (downstream teams, on-call, auditors) are affected without asking, are
   routinely skipped, and routinely have the sharpest complaints.
3. **Elicit fitness criteria per group.** Drive toward the standard axes — lead
   time, predictability, quality, safety, regulatory conformance — without
   leading. Each criterion ends stated as something measurable *in principle*,
   with the group holding it. A criterion with no conceivable measure is recorded
   `unmeasurable` rather than dropped.
4. **Elicit external dissatisfaction.** Including the highest-yield question:
   *what do you not ask us for any more because it isn't worth it?* — which
   surfaces demand that has stopped arriving, invisible to any board.
5. **Elicit internal dissatisfaction separately, in different words** — what
   prevents you doing a good, professional job; where does work sit; what do you
   get interrupted for; what do you do twice. Not the same question pointed
   inward: delivery people are dissatisfied by different things than recipients,
   and one merged question loses that.
6. **Attribute and connect.** Each item names its source group and the fitness
   criterion it threatens. Two explicit exception paths: dissatisfaction with no
   matching criterion means step 3 missed one — add it and say so; dissatisfaction
   not about flow at all goes to a separate out-of-scope list.
7. **Corroborate with board signal where available, and label it corroboration.**
   Aged items, blocked counts, reopen rates support a stated dissatisfaction;
   they never discover one. Contradicting signal is reported as a discrepancy for
   a human, never used to overrule the person who said it.
8. **Emit the four artifacts separately** — external set, internal set, criteria
   amendments, out-of-scope list — and stop.

### Known failure modes to guard against

- **Merging internal and external into one ranked list.** The distinction is
  load-bearing at socialization: external dissatisfaction justifies the change to
  stakeholders, internal is what the team judges it by.
- **Inventing fitness criteria from the standard axes** because a group was hard
  to reach. A criterion nobody stated is one the team assumed, and it will drive
  design decisions that address nothing.
- **Letting board data lead.** The board records the work that arrived, never the
  frustration of the person who stopped sending it.
- **Recording individual names** at the point of capture rather than at the point
  of publishing.
- **Accepting an unmeasurable criterion silently** rather than marking it — Stage
  04 needs to know it cannot verdict on it.

## Inputs and data boundary

Reads: the service frame (service, customer groups); an existing stakeholder
register where one is loaded; SLA/OLA or service-definition documents where they
exist; and, for corroboration only, the bound Jira item set.

Max data-class: `internal`. This is the flowspace's most sensitive conversational
surface — elicitation routinely surfaces named individuals and inter-team
friction. Name removal happens **at the point of recording**, not at publishing.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01 — Stages 01–02 have no
existing skill covering service-level fitness and dissatisfaction elicitation.
`context-elicitation` is the nearest neighbour and operates at the wrong unit of
analysis. Gap rationale:
`flow-foundry/decision-log/2026-08-01-statik-adoption-triage-and-scaffold.md`.

## Definition of done

1. A test with both recipient and dependant groups produces criteria from both —
   a run that only asks recipients is caught.
2. Internal and external sets are emitted separately and are never merged, even
   when a run has few items in one of them.
3. Every dissatisfaction names a source group and a fitness criterion, or appears
   on the out-of-scope list with a reason. Nothing is unattributed.
4. A dissatisfaction with no matching criterion correctly produces a criteria
   amendment rather than being dropped or force-fitted.
5. A named individual in an elicited statement is removed at recording; a test
   feeding in "Priya never reviews anything" yields a source-attributed statement
   about review latency.
6. Board signal contradicting a stated dissatisfaction produces a discrepancy
   entry, not an overruled human.
7. The unmeasurable-criterion path is exercised: the criterion survives into the
   output, marked, rather than being dropped for lack of a metric.
8. A collision test against `context-elicitation` confirms the boundary holds in
   both directions — a work-item framing request routes there, a service-level
   fitness request routes here.
