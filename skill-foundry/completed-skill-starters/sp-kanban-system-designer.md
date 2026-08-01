---
id: sp-kanban-system-designer
title: "Skill Primer Brief — Kanban System Designer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[kanban-system-design-canvas]]", "[[workflow-modeler]]"]
---

# Skill Primer Brief — Kanban System Designer

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-kanban-system-designer.md`.

## Purpose

Assembles the complete Kanban system (STATIK step 7) from the ratified workflow
model, classes of service, and measured demand and capability: board columns, WIP
limits, ticket design, explicit policies, cadences, and metrics — **seven
elements, each traced to the evidence that motivated it.**

It replaces the board-only rollout, which is the most common failure mode of
Kanban adoption and the quietest: the board looks right for months while nothing
about how work flows has changed, because the limits are decorative, the policies
were never written down, and no cadence exists to tune anything.

## Triggering intent

**Fires on** — Stage 07 of `statik-adoption`, and standalone on:

- "Design the board for this service."
- "What should our WIP limits be?"
- "We have classes of service — now build the system."
- "What should be on the card?"
- "What cadences do we need?"

**Does not fire on (near-misses):**

- **Modelling the workflow.** That is `workflow-modeler`, whose output this
  consumes. Modelling says what is true; design says what to build. Keeping them
  separate is what stops the design from quietly rewriting the model to suit
  itself.
- **Deriving classes of service.** That is `class-of-service-designer`. Classes
  are carried through here unchanged; re-deriving them signals the upstream
  output was unusable and calls for a loop-back instead.
- **Configuring a Jira board.** No write path, ever. This skill produces a
  design; a human configures the tool. The boundary is deliberate.
- **Socializing or negotiating the design.** That is the flowspace's Stage 08,
  inline. This skill produces the artifact that stage negotiates over.
- **Generic "make me a Kanban board" requests with no upstream analysis.** The
  skill declines and names what it needs — a workflow model, classes, and demand
  or capability figures. Producing a template board on request is exactly what it
  exists to prevent.

## Method sketch

Structure and the completeness checklist live in the flowspace's
`reference/kanban-system-design-canvas.md`.

1. **Columns from the workflow model, not the current board.** Queue states
   become explicit waiting or buffer columns rather than being folded into the
   adjacent activity — a hidden queue is invisible waiting time. Mark the
   commitment and delivery points; everything upstream of commitment is an
   options queue and is drawn as one.
2. **WIP limits from measured residency and arrival variability, derivation
   shown.** Per column: the limit plus current concurrency, residency, and the
   arrival variability feeding it. Where residency was unavailable, propose from
   observed concurrency and label it `starting point — to be tuned at the
   operations review`. **Never present an underived limit as computed.**
3. **Set limits to be felt.** A limit at or above current concurrency changes
   nothing and teaches the team that limits are decorative. The limit should bind
   sometimes — that is the mechanism by which a pull system creates the slack that
   shortens lead time. State this in the design, because the first instinct at
   review is always to raise limits until nothing blocks.
4. **Ticket design from the pull decision.** Per state, ask what a person needs to
   know to decide which item to pull next; that is what the card carries.
   Baseline: type, class of service, commitment date, due date where the class
   requires one, blocked status. A card that does not support the pull decision
   forces people back into the ticket and the board stops working.
5. **Write the explicit policies** — per-column definition of done and pull
   criteria, blocked-item policy, class policies, capacity allocation. A policy
   living in someone's head is a habit, and it will not survive that person's
   absence.
6. **Design cadences with decision rights.** Replenishment (how items pass the
   commitment point, how often, who decides) and operations/flow review (where
   metrics are read and limits and allocations tuned) at minimum. Each names its
   purpose, frequency, roles, and **the decision it is empowered to make** — a
   cadence with no decision rights is a status meeting and will be cancelled
   within a quarter, taking the feedback loop with it.
7. **Metrics tied to fitness criteria.** Each selected metric names the criterion
   it tracks; a metric tracking none is dropped, because it will be reported,
   misread, and eventually acted on. **Per-person throughput, lead time, and cycle
   time are excluded by design**, written into the metric set itself so whoever
   configures the board inherits the constraint rather than re-deciding it.
8. **Produce the evidence trace table** — every element with the specific finding
   motivating it. Untraced elements are **flagged, not removed**: some are
   legitimate conventions, and the point is that socialization knows which
   elements it will have to defend on grounds other than evidence.
9. **Check the design against both dissatisfaction sets** and state plainly
   anything unaddressed. A design that silently drops a complaint fails at
   socialization in a way nobody can articulate.

### Known failure modes to guard against

- **Producing a board and calling it a system** — the six other elements missing.
- **Familiar-board drift**: the columns everyone has seen, the limits from the
  last team, and none of the motivating dissatisfactions addressed. The design
  looks professional and changes nothing.
- **Presenting a starting-point WIP limit as derived.**
- **Setting limits above current concurrency** so nothing ever blocks.
- **Cadences with no decision rights.**
- **Metrics with no fitness criterion**, or per-person metrics reaching the
  designed system.
- **Silently dropping a dissatisfaction** rather than listing it as unaddressed.

## Inputs and data boundary

Reads: the workflow model with activity/queue marks and commitment/delivery
points; classes of service and their policies; the capacity allocation proposal;
the capability profile and per-state residency; the demand profile including
arrival variability; both dissatisfaction sets; the fitness verdicts.

Refuses to run on a subset: without a workflow model and classes of service it
declines and names what is missing.

Max data-class: `internal`. **The metric set is a data-boundary artifact, not
only a design one** — it specifies what the operating system will report on an
ongoing basis, and the per-person exclusion is written into it so it propagates
to whoever configures the board.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01. Nothing in the house
toolkit designs an operating system for a service; the closest artifacts
(`documentarian`'s outputs) document procedures rather than designing flow.

## Definition of done

1. All seven canvas elements are present in every output; a board-only result
   fails.
2. Every column maps to a modelled state or is flagged `convention — no evidence
   trace`; every modelled state appears as a column, buffer, or explicitly merged
   element with a reason.
3. Every WIP limit is marked `derived` or `starting point`, and a no-residency run
   produces only the latter, correctly labelled.
4. A proposed limit at or above observed concurrency is flagged as
   non-binding with the reason stated.
5. Every card field names the per-state pull decision it supports.
6. Every cadence names the decision it is empowered to make; one without decision
   rights fails.
7. Every metric names its fitness criterion, and the per-person exclusion appears
   in the metric set itself, not only in commentary.
8. The evidence trace table covers every element; untraced elements are flagged
   rather than dropped.
9. Every recorded dissatisfaction is traced, listed as unaddressed with a reason,
   or already out of scope — nothing simply absent.
10. A bare "design me a Kanban board" request with no upstream analysis is
    declined with the missing inputs named.
