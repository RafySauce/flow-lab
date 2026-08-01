---
id: sp-workflow-modeler
title: "Skill Primer Brief — Workflow Modeler"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[flow-capability-analyzer]]", "[[sad-diagram-maintainer]]"]
---

# Skill Primer Brief — Workflow Modeler

> Intake path 1 for the skill-foundry, from the `statik-adoption` flow-foundry
> Layer-3 gap triage. Filed as
> `skill-foundry/backlog-skill-starters/sp-workflow-modeler.md`.

## Purpose

Models the workflow each work item type actually passes through as a sequence of
**knowledge-discovery activities**, separates activities from queues, and sets
the **commitment point** and **delivery point** (STATIK step 5).

It replaces transcribing the board's status list into a "workflow." The board's
statuses are one team's historical guess, usually inherited from a project
template, and they routinely name organisational handoffs rather than activities
that discover knowledge. STATIK is explicit that what is modelled is the flow of
work, not the organisation chart.

The commitment point is this skill's highest-stakes output: it silently redefines
every lead-time figure measured before it was set, and nothing downstream can
detect that it was set wrong.

## Triggering intent

**Fires on** — Stage 05 of `statik-adoption`, and standalone on:

- "Model how work actually flows through this service."
- "Our board columns don't match how we really work."
- "Where's the commitment point for this service?"
- "Which of our statuses are actually just queues?"

**Does not fire on (near-misses):**

- **Documenting a procedure or runbook.** That is the `documentarian` flowspace.
  This models the *shape* of a delivery workflow for system design; it does not
  author operational procedure.
- **Decomposing a work item into ordered children.** That is
  `process-decomposition` — sequencing *within* one item's execution, not the
  states every item of a type passes through. Superficially similar vocabulary
  (phases, sequence, dependencies), entirely different unit.
- **Maintaining architecture diagrams.** That is `sad-diagram-maintainer`. This
  skill produces a workflow model, not a systems diagram, and does not touch
  architecture artifacts.
- **Designing the board.** That is `kanban-system-designer`, which consumes this
  model. Modelling and designing are deliberately separate steps: the model says
  what is true, the design says what to build.
- **Configuring Jira workflows.** No write path, ever.

## Method sketch

1. **Ask what is learned, not what is done.** Per type, walk the item's life with
   the delivery team asking at each step: *what do we know after this that we did
   not know before?* Steps that answer become the model's states. A step that
   answers "nothing — it moved to someone else's queue" is a handoff, not an
   activity.
2. **Derive candidate states from the board and present the disagreements.**
   Propose from observed status sequence and residency, set beside the activity
   list, and report the four common disagreements explicitly:
   - a status where items sit but nothing is learned (a queue masquerading as an
     activity — most often one containing "ready" or "pending");
   - an activity the team describes with no status at all (invisible work, which
     is why it never gets capacity);
   - statuses never used, or used by a handful of items;
   - a status meaning different things for different types.
3. **Mark every state `activity` or `queue`.** No state left unmarked. This
   distinction makes flow efficiency meaningful and determines how a WIP limit on
   that state will behave.
4. **Set the commitment point with the team, deliberately.** Ask directly: at what
   moment does this become something we have promised? Upstream of it, items are
   *options* the service may decline; downstream, they are work in progress the
   customer is owed. The answer is frequently later than the board implies and
   frequently has no status of its own.
5. **Emit a recomputation directive.** If the ratified commitment point differs
   from the basis the capability analysis declared, every lead-time figure is
   measured from the wrong start: emit an explicit loop-back instruction. Do not
   adjust numbers in place, and do not carry old figures forward with a footnote —
   a silently mismatched basis is undetectable downstream. If it matches, say so
   explicitly rather than staying silent.
6. **Set the delivery point**, and note whether the service retains obligation
   past it (validation in the customer's hands, a warranty period) — which
   determines whether the last column ends the system or is a state still needing
   management.
7. **Model per type, then look for a shared model.** Types usually share most
   states and differ in one or two. One model with typed exceptions is easier to
   operate; several genuine models beat one model fitting none. State which was
   chosen and why — a forced merge produces a board the team quietly works around.

### Known failure modes to guard against

- **Transcribing board statuses as the model** — the failure the method's first
  half exists to prevent.
- **Modelling the org chart** — states named for the team or person performing
  them rather than for the activity.
- **Leaving the commitment point implicit**, or setting it at creation by default
  because that is where the board starts.
- **Failing to emit the recomputation directive** when the commitment point moved.
  The flow's most consequential silent error.
- **Folding a queue into an adjacent activity**, hiding waiting time.
- **Forcing one shared model** onto types that genuinely flow differently.

## Inputs and data boundary

Reads: the work item type set; per-state residency and the capability profile;
the declared measurement basis; the board's status list and transition
configuration; the internal dissatisfaction set (which routinely names the
queues); and the delivery team's own account, which is required — this skill
cannot run from the board alone and says so rather than producing a
board-transcribed model.

Max data-class: `internal`. Workflow modelling makes organisational handoffs
visible, which makes it easy to slide into naming teams and individuals as
bottlenecks. States are named for the **activity** ("technical review"), never
for the performer ("waiting on Priya", "with the architects") — the same
attribution rule the dissatisfaction elicitation sets, applied to the model.

Engines: Rovo and Copilot, per the employer matrix.

## Demand source

`statik-adoption` flowspace Layer-3 triage, 2026-08-01. No existing house skill
models a delivery workflow; the nearest neighbours (`process-decomposition`,
`sad-diagram-maintainer`, `documentarian`) each operate on a different artifact
at a different altitude, and the boundaries are stated above in both directions.

## Definition of done

1. A test where board statuses and the team's account diverge produces a model
   from the account plus an explicit disagreement list — not a transcription.
2. A status named "Ready for X" containing items with long residency and no
   knowledge discovery is correctly marked `queue`.
3. Every state carries an `activity` or `queue` mark; an unmarked state fails.
4. An activity the team describes with no corresponding status appears in the
   model, marked `no current status`.
5. A commitment point ratified later than creation emits a recomputation
   directive naming the new basis; a matching one emits an explicit confirmation
   rather than silence.
6. A state named for a team or individual is caught and renamed for its activity.
7. A two-type test where the types genuinely differ produces either two models or
   one model with stated typed exceptions — never a forced merge presented as a
   shared model.
8. Run without delivery-team input, the skill declines to produce a ratified
   model and says why, rather than emitting a board transcription.
