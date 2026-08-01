---
id: kanban-system-design-canvas
title: "Kanban System Design Canvas — The Seven Elements and Their Evidence"
type: template
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[classes-of-service-model]]"]
---

# Kanban System Design Canvas

The mold Stage 07 fills. A Kanban system is **seven elements, not one** — the
board alone is the most common failed rollout, and it fails quietly: the board
looks right for months while nothing about how work flows has changed.

Every element carries an evidence trace. An element with no trace is a
convention someone imported, which is allowed — but it is flagged, so Stage 08
knows which elements it will have to defend on grounds other than evidence.

## The seven elements

| # | Element | Derived from | Evidence trace must name |
|---|---|---|---|
| 1 | **Board columns** | Stage 05 workflow model | The modelled state each column represents; activity/queue/buffer mark; commitment and delivery points |
| 2 | **WIP limits** | Stage 04 residency + Stage 03 arrival variability | Per column: current concurrency, residency, arrival variability — or `starting point` where residency was unavailable |
| 3 | **Ticket design** | Stage 05 states + Stage 06 class policies | Per field: the per-state pull decision it supports |
| 4 | **Explicit policies** | Stages 05 and 06 | Per policy: the state or class it governs, and the dissatisfaction or judgment behind it |
| 5 | **Classes of service** | Stage 06 (carried through unchanged) | Already traced at Stage 06 |
| 6 | **Cadences** | Stage 05 commitment/delivery points + Stage 06 allocation | Per cadence: the decision it is empowered to make |
| 7 | **Metrics** | Stage 01/02 fitness criteria | Per metric: the fitness criterion it tracks |

## Element notes

### 1 — Board columns

Columns follow the ratified activity states, not the current board. **Queue
states become explicit waiting or buffer columns** rather than being folded into
the adjacent activity — a queue hidden inside an activity column is invisible
waiting time, which is exactly what Stage 04's residency analysis exists to
expose. Mark the commitment and delivery points on the board itself; everything
upstream of commitment is an options queue and is drawn as one.

### 2 — WIP limits

State the limit and the figures behind it. Where Stage 04 took the no-history
degrade path, propose from currently observed concurrency and label the result
`starting point — to be tuned at the operations review`, never presenting an
underived limit as computed.

**Set the limits to be felt.** A limit at or above current concurrency changes
nothing and teaches the team that limits are decorative. The limit should bind
sometimes — that is the mechanism by which a pull system creates the slack that
shortens lead time. Say this in the design, because the first instinct at review
is always to raise the limits until nothing blocks.

### 3 — Ticket design

Driven by one question, asked per state: *what does a person need to know here in
order to decide which item to pull next?* That is what the card must carry.

Baseline set: work item type, class of service, commitment date, due date where
the class requires one, blocked status. Add elapsed-time or blocked-time markers
where class policies depend on them, and per-state signals the workflow model
calls for. A card that does not support the pull decision forces people back into
the ticket, and the board stops functioning as a board.

### 4 — Explicit policies

Definition of done per column; pull criteria per column; the blocked-item policy
(what marks it, who escalates, when); class policies from Stage 06; capacity
allocation.

Making policies explicit is one of the Kanban Method's core practices and the one
most often skipped. A policy that lives in someone's head is not a policy — it is
a habit, and it does not survive that person's absence.

### 5 — Classes of service

Carried through from Stage 06 unchanged. Re-deriving them here is a sign the
Stage 06 output was not usable; take the loop-back instead.

### 6 — Cadences

At minimum:

- **Replenishment** — how items pass the commitment point, how often, who
  decides. This is the cadence that makes the commitment point real rather than
  notional.
- **Operations / flow review** — where the metrics are read and the limits and
  allocations tuned. This is where the system evolves; without it the design is
  frozen at its least-informed moment.
- **Delivery** — where the delivery point requires one.

Each cadence names its purpose, frequency, attending roles, and **the decision it
is empowered to make**. A cadence with no decision rights is a status meeting and
will be cancelled within a quarter — taking the system's feedback loop with it.

### 7 — Metrics

Default set: cumulative flow, lead-time distribution, throughput, flow efficiency
where measurable, due-date performance where a fixed-date class exists.

**Each metric names the fitness criterion it tracks. A metric tracking no
criterion is dropped** — it will be reported, misread, and eventually acted on.

**Per-person throughput, lead time, and cycle time are excluded by design.** This
is written into the metric set itself, not left as an analysis-time convention,
so whoever configures the board inherits the constraint rather than re-deciding
it. See `board-evidence-requirements.md` §5 for why.

## The completeness check

Before Stage 07 presents:

- [ ] All seven elements present — not just the board
- [ ] Every column maps to a modelled state, or is flagged as an imported convention
- [ ] Every modelled state appears as a column, buffer, or explicitly merged element with a reason
- [ ] Every WIP limit marked `derived` or `starting point`
- [ ] Every cadence names the decision it may make
- [ ] Every metric names its fitness criterion
- [ ] Per-person metrics explicitly excluded in the metric set
- [ ] Every recorded dissatisfaction either traced to an element, listed as unaddressed with a reason, or already on Stage 02's out-of-scope list
