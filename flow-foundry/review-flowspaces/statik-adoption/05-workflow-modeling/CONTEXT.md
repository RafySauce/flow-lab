---
id: statik-adoption-stage-05
title: "Stage 05 — Workflow Modeling"
type: stage-context
stage: 5
review-intensity: heavy
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
  - "[[workflow-modeler]]"
  - "[[statik-method-reference]]"
---

# Stage 05 — Workflow Modeling

Covers **STATIK step 5**: model the workflow each work item type actually passes
through, as a sequence of knowledge-discovery activities, and set the commitment
and delivery points. The flow's highest-judgment stage.

The board's configured statuses are not the workflow. They are one team's
historical guess at it, usually inherited from a project template, and they
routinely name organisational handoffs rather than activities that discover
knowledge. STATIK is explicit that what is modelled is the flow of work, not the
organisation chart.

## Inputs

| Input | Source | Required |
|---|---|---|
| Work item type set | `work/03-work-item-types.md` | Yes |
| Per-state residency (working/waiting per state) | `work/04-state-residency.md` | Yes — or its `unavailable` block |
| Capability profile per type | `work/04-capability-profile.md` | Yes |
| Measurement-basis declaration | `work/04-measurement-basis.md` | Yes |
| Board status list and transition configuration | `work/01-bound-set.md` | Only in evidence-grounded mode |
| Internal dissatisfaction set | `work/02-dissatisfaction-internal.md` | Yes |
| Access to the delivery team | Operator arranges | Yes — this stage cannot be run from the board alone |

## Process

1. **Ask what is learned, not what is done.** For each work item type, walk the
   item's life with the delivery team and ask at each step: what do we *know
   after this step that we did not know before*? The steps that answer that
   question are the knowledge-discovery activities and they become the model's
   states. A step that answers it with "nothing — it just moved to another
   person's queue" is a handoff, not an activity.
2. **Derive candidate states from the board and present the disagreements.**
   Where a board is bound, propose states from the observed status sequence and
   residency data, then set them beside the activity list from step 1 and report
   where they disagree. The four disagreements worth naming explicitly, because
   they are the common ones:
   - a status where items sit but nothing is learned (a queue masquerading as an
     activity — most often a status containing the word "ready" or "pending");
   - an activity the team describes that has no status at all (invisible work,
     which is why it never gets capacity);
   - statuses that are never used, or used by fewer than a handful of items;
   - a status that means different things for different work item types.
3. **Separate activities from queues, and mark every state as one or the
   other.** This is the distinction that makes the rest of the design possible:
   flow efficiency at Stage 04 is meaningless without it, and a WIP limit placed
   on a queue behaves entirely differently from one placed on an activity. Every
   state gets an explicit `activity` or `queue` mark — no state is left
   unmarked.
4. **Set the commitment point, deliberately and with the team.** This is the
   point at which the service commits to delivering an item — before it, items
   are *options* the service may decline; after it, they are work in progress
   the customer is owed. Ask directly: at what moment does this become something
   we have promised? The answer is frequently later than the board implies, and
   frequently a moment with no status of its own.
5. **Recompute Stage 04 if the commitment point moved.** If the ratified
   commitment point differs from item creation — the basis Stage 04 declared —
   then every lead-time figure is measured from the wrong start and must be
   recomputed. Take the 5 → 4 loop-back. Do not adjust the numbers in place and
   do not carry the old figures forward with a footnote: Stage 06's classes of
   service and Stage 07's WIP limits both derive from these figures, and a
   silently mismatched basis is undetectable downstream. This is the single
   most consequential check in the flow.
6. **Set the delivery point** — where the item leaves this service's control and
   reaches the customer. Note explicitly whether the service retains any
   obligation past it (validation of usefulness in the customer's hands, a
   warranty period), because that determines whether the board's last column is
   the end of the system or a state that still needs managing.
7. **Model per work item type, then look for a shared model.** Types often share
   most of their workflow and differ in a step or two. A single model with typed
   exceptions is easier to operate than several parallel models; several genuine
   models are better than one model that fits none. State which was chosen and
   why — a forced merge here produces a board the team will quietly work around.
8. **Present the model(s), the activity/queue marks, the commitment and delivery
   points, and the board disagreements — then stop for ratification.**

`Layer-3: workflow-modeler`

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Workflow model per type (or shared model with typed exceptions) | Ordered states, each with: name, the knowledge discovered there, `activity` or `queue`, and the board status(es) it maps to or `no current status` | `work/05-workflow-model.md` |
| Commitment point declaration | The state or moment, what changes at it, and whether it differs from Stage 04's measurement basis | `work/05-commitment-point.md` |
| Delivery point declaration | The state or moment, and any obligation retained past it | `work/05-delivery-point.md` |
| Board disagreement list | Queues masquerading as activities, activities with no status, unused statuses, and statuses meaning different things per type — with item counts | `work/05-board-disagreements.md` |
| Recomputation directive | Either `commitment point = creation, Stage 04 stands` or a loop-back instruction naming the new basis | `work/05-recomputation-directive.md` |

## Verify

Trace **Stage 04 → Stage 05 → Stage 04**: compare the ratified commitment point
in `work/05-commitment-point.md` against the declared measurement basis in
`work/04-measurement-basis.md`. If they differ, `work/05-recomputation-directive.md`
must carry a loop-back instruction and Stage 06 must not open until Stage 04 has
been re-run from the new basis. If they match, the directive must say so
explicitly.

Additionally, trace **Stage 05 → Stage 04** on the activity/queue marks: every
state marked `activity` or `queue` here must be consistent with how Stage 04's
residency analysis split working from waiting time. Where they conflict, Stage
04's split was a guess from state names and this stage's mark is authoritative —
record the correction.

The failure mode this catches: the commitment point is ratified as "when the
work is scheduled into a sprint," three weeks after creation on average, and
nobody re-runs Stage 04 — so every lead-time percentile, every predictability
ratio, and every WIP limit derived from them describes a system that does not
exist. Running these checks leaves a one-line result each in the run's decision
log.

## Review

- **Reviewer:** the delivery team, jointly with the service owner. The team owns
  the activity model (they are the only ones who know what is learned where);
  the owner owns the commitment point (it is a commitment the service makes, not
  a technical fact).
- **Intensity:** `heavy` — **breaks the U-curve default with cause.** The
  commitment point silently redefines every lead-time number Stage 04 produced,
  and no downstream stage can detect that it was set wrong: Stage 06 and Stage 07
  will both consume the resulting figures without any way to tell they are
  measured from the wrong start. The activity-versus-queue judgment is equally
  load-bearing and equally invisible downstream.
- **Evidence:** a decision-log entry naming both reviewers, the date, the
  ratified commitment and delivery points, whether a recomputation loop-back was
  triggered, and every board disagreement accepted or rejected.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- Workflow modelling makes organisational handoffs visible, which makes it easy
  to slide into naming teams and individuals as bottlenecks. States are named
  for the *activity* ("technical review"), never for the person or team that
  performs it ("waiting on Priya", "with the architects") — the same attribution
  rule Stage 02 set, applied to the model.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
