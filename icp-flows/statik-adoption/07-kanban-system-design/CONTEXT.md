---
id: statik-adoption-stage-07
title: "Stage 07 — Kanban System Design"
type: stage-context
stage: 7
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
  - "[[kanban-system-designer]]"
  - "[[kanban-system-design-canvas]]"
---

# Stage 07 — Kanban System Design

Covers **STATIK step 7**: assemble the actual system. A Kanban system is not a
board — it is the board, the cards, the limits, the explicit policies, the
cadences, and the metrics, together. Designing the columns and stopping there is
the most common failed rollout, and it fails quietly: the board looks right for
months while nothing about the way work flows has changed.

Every element of the design must trace to the evidence that motivated it. An
element with no trace is a convention someone imported, and Stage 08 will not be
able to defend it when challenged.

## Inputs

| Input | Source | Required |
|---|---|---|
| Workflow model, activity/queue marks, commitment and delivery points | `work/05-workflow-model.md`, `work/05-commitment-point.md`, `work/05-delivery-point.md` | Yes |
| Class of service set and per-class policies | `work/06-classes-of-service.md`, `work/06-class-policies.md` | Yes |
| Capacity allocation proposal | `work/06-capacity-allocation.md` | Yes |
| Capability profile and per-state residency | `work/04-capability-profile.md`, `work/04-state-residency.md` | Yes |
| Demand profile per type, incl. arrival variability | `work/03-demand-profile.md` | Yes |
| Both dissatisfaction sets | `work/02-dissatisfaction-*.md` | Yes |
| Fitness verdicts | `work/04-fitness-verdicts.md` | Yes |

## Process

1. **Design the board columns from the workflow model, not from the current
   board.** Columns follow the ratified activity states. Queue states become
   explicit waiting columns or buffer columns rather than being folded into the
   adjacent activity — a queue hidden inside an activity column is invisible
   waiting time, which is precisely what Stage 04's residency analysis exists to
   expose. Mark the commitment point and the delivery point on the board
   explicitly; everything upstream of commitment is an options queue and is
   drawn as such.
2. **Set WIP limits from measured residency and arrival variability, and show
   the derivation.** Per column, state the limit and the figures behind it —
   current average concurrent items in that state, its residency, and the
   arrival variability feeding it. Where residency data was unavailable (Stage
   04's degrade path), say so and propose a limit from current observed
   concurrency instead, explicitly labelled as a **starting point to be tuned at
   the operations review** rather than as a derived figure. Never present an
   underived limit as though it were computed.
3. **Set the limits to be felt.** A WIP limit set at or above current
   concurrency changes nothing and teaches the team that limits are decorative.
   The limit should bind sometimes — that is the mechanism by which a pull
   system creates the slack that shortens lead time. Say this out loud in the
   design, because the first instinct at review is always to raise the limits to
   where nothing blocks.
4. **Design the ticket.** For each state, ask what information a person needs in
   order to decide which item to pull next — that is what the card must carry.
   The baseline set: work item type, class of service, commitment date, due date
   where the class requires one, and blocked status. Add per-state signals the
   model calls for, and elapsed-time or blocked-time markers where the class
   policies depend on them. A card that does not support the pull decision at
   each state forces people back into the ticket, and the board stops working.
5. **Write the explicit policies.** Definition of done per column, pull criteria
   per column, the blocked-item policy (what marks it, who escalates, when),
   the class policies from Stage 06, and the capacity allocation. "Explicit
   policies" is one of the Kanban Method's core practices and the one most often
   skipped: a policy that lives in someone's head is not a policy, it is a habit,
   and it will not survive that person's absence.
6. **Design the cadences.** At minimum a replenishment cadence (how items pass
   the commitment point, how often, who decides) and an operations or flow
   review (where the metrics are read and the limits and allocations tuned).
   Add a delivery cadence where the delivery point requires one. Each cadence
   gets a purpose, a frequency, the roles attending, and — critically — the
   decision it is empowered to make. A cadence with no decision rights is a
   status meeting and will be cancelled within a quarter.
7. **Choose the metrics, and tie each to a fitness criterion.** The default set
   — cumulative flow, lead-time distribution, throughput, flow efficiency where
   measurable, due-date performance where a fixed-date class exists. Each
   selected metric names the fitness criterion it tracks; a metric tracking no
   criterion is dropped. Restate the no-per-person-metrics constraint here as a
   property of the *designed system*, not just of this analysis: the system must
   not be configured to produce individual throughput or lead-time reporting.
8. **Trace every element to its evidence.** Produce the trace table: each design
   element, and the specific finding (dissatisfaction, demand figure, capability
   figure, workflow judgment) that motivated it. Elements with no trace are
   flagged in the table rather than removed — some are legitimate conventions,
   and the point is that Stage 08 knows which ones it will have to defend on
   grounds other than evidence.
9. **Check the design against the dissatisfaction sets, both of them.** For each
   recorded dissatisfaction, which design element addresses it? Anything
   unaddressed is stated plainly in the output — a design that silently drops a
   complaint fails at Stage 08 in a way nobody can articulate, which is the
   worst kind of failure to debug.
10. **Present the full system design and the trace table, then stop.**

`Layer-3: kanban-system-designer`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Board design | Columns in order, each marked activity/queue/buffer, with the commitment and delivery points marked and the options queue upstream | `work/07-board-design.md` |
| WIP limits | Per column: limit, derivation figures, and `derived` or `starting point — to be tuned` | `work/07-wip-limits.md` |
| Ticket design | Card fields with the per-state pull decision each supports | `work/07-ticket-design.md` |
| Explicit policies | Per-column definition of done and pull criteria; blocked-item policy; class policies; capacity allocation | `work/07-policies.md` |
| Cadence design | Per cadence: purpose, frequency, roles, and the decision it is empowered to make | `work/07-cadences.md` |
| Metric set | Per metric: what it shows, the fitness criterion it tracks, and where it is reviewed | `work/07-metrics.md` |
| Evidence trace table | Every design element with the specific finding motivating it, or flagged `convention — no evidence trace` | `work/07-evidence-trace.md` |
| Unaddressed dissatisfaction list | Recorded dissatisfactions no design element addresses | `work/07-unaddressed.md` |

## Verify

Trace **Stage 02 → Stage 07**: every dissatisfaction in both sets must either
appear against a design element in `work/07-evidence-trace.md`, or appear in
`work/07-unaddressed.md` with a reason, or already sit on Stage 02's
out-of-scope list. Nothing may simply be absent from all three.

Trace **Stage 05 → Stage 07** on structure: every state in the ratified workflow
model must appear as a column, a buffer, or an explicitly merged element with a
stated reason — and every column must map back to a modelled state. A column
with no modelled state behind it is an imported convention and gets flagged as
one.

The failure mode these catch: the design drifts toward a familiar-looking board
during assembly — the columns everyone has seen before, the limits from the last
team — and the dissatisfactions that motivated the entire exercise are addressed
by nothing. The board looks professional and changes nothing. Running these
checks leaves a one-line result each in the run's decision log.

## Review

- **Reviewer:** the delivery team, jointly with the service owner. The team must
  confirm they can actually operate the design — the pull criteria, the card, the
  cadences — because a design only the owner endorses is one the team routes
  around.
- **Intensity:** `light` — constrained execution. Every element derives from
  ratified upstream outputs against the canvas in
  `reference/kanban-system-design-canvas.md`; the reviewer checks derivation and
  operability rather than setting direction. Direction was set at Stages 02, 05,
  and 06.
- **Evidence:** a decision-log entry naming both reviewers, the date, every WIP
  limit marked `starting point` rather than derived, every element flagged
  `convention — no evidence trace`, and every unaddressed dissatisfaction
  accepted as such.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- The metric set is a **data-boundary artifact, not only a design one**: it
  specifies what the operating system will report on an ongoing basis. Per-person
  throughput, lead time, and cycle-time reporting are excluded by design, and the
  exclusion is written into `work/07-metrics.md` so that whoever configures the
  board later inherits the constraint rather than re-deciding it.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
