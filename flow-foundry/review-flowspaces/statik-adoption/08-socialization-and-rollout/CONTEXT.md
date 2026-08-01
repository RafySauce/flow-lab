---
id: statik-adoption-stage-08
title: "Stage 08 — Socialization & Rollout"
type: stage-context
stage: 8
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
  - "[[rollout-and-socialization-guide]]"
---

# Stage 08 — Socialization & Rollout

Covers **STATIK step 8**: socialize the design and negotiate its implementation.
Walk each stakeholder group through how the system will work *from their point
of view*, listen, absorb objections as design inputs, rework, and return for
agreement.

This stage is routinely treated as a communications exercise appended to a
finished design. It is not: it is a negotiation with real design authority, and
objections raised here legitimately change classes of service, capacity
allocations, WIP limits, board structure, and reporting. A design that reaches
this stage and emerges unchanged has usually not been socialized — it has been
announced.

A run does not end when the design is drawn. It ends when the stakeholders
agree.

## Inputs

| Input | Source | Required |
|---|---|---|
| Full system design | `work/07-*.md` (board, limits, ticket, policies, cadences, metrics) | Yes |
| Evidence trace table | `work/07-evidence-trace.md` | Yes |
| Both dissatisfaction sets, with sources | `work/02-dissatisfaction-*.md` | Yes |
| Fitness verdicts | `work/04-fitness-verdicts.md` | Yes |
| Unaddressed dissatisfaction lists | `work/06-unaddressed.md`, `work/07-unaddressed.md` | Yes |
| Service frame with customer groups | `work/01-service-frame.md` | Yes |
| Mode declaration | `work/01-mode-declaration.md` | Yes |

## Process

Structure and templates in `reference/rollout-and-socialization-guide.md`.

1. **Build one view of the design per stakeholder group,** from the service
   frame's customer list plus the delivery team and any governance stakeholder.
   Each view leads with the dissatisfaction *that group* reported and the design
   element that addresses it. A single generic walkthrough is what produces
   polite agreement followed by non-adoption: people assent to a design they
   have not seen implications of, and object months later in the form of working
   around it.
2. **Lead with their dissatisfaction, not with the board.** The board is the
   least interesting part of the design to everyone except the team operating
   it. Open each session with "you told us X was the problem; here is what
   changes about X, and here is the evidence" — the trace table exists for
   exactly this.
3. **State the evidence basis honestly, per the mode declaration.** Where a
   finding was measured, say measured and show the figure. Where it was elicited,
   say elicited. Where a WIP limit is a starting point rather than a derived
   figure, say so. A stakeholder who later discovers that a confident number was
   an estimate stops trusting all the others, and the whole design with them.
4. **Present what the design does *not* fix.** The unaddressed lists and Stage
   02's out-of-scope list, stated plainly. A design that appears to promise
   everything will be judged against everything.
5. **Capture objections as structured design inputs, not as feedback.** For each
   objection, record: the group, what they object to, what they predict will
   happen, and which design element it bears on. The guide's objection map gives
   the common objections and the design element each properly bears on —
   "expedite will be abused" bears on the expedite invocation policy and its
   authoriser, not on whether to have an expedite class; "the limits are too
   low" bears on the residency evidence behind them, which is either there or
   is not.
6. **Distinguish the three kinds of objection, and treat them differently.**
   - **Evidence objections** ("that number is wrong") — check the evidence. If
     the objection is right, take the loop-back to whichever stage produced it.
     This is the stage's most valuable output and the reason it has design
     authority.
   - **Design objections** ("that limit will not work for us") — rework the
     design element. Normal and expected.
   - **Interest objections** ("this reduces my ability to jump the queue") —
     these are legitimate to surface and are *not* resolved by reworking the
     design. Name them as interests, and escalate to the service owner as a
     decision rather than absorbing them silently. A capacity allocation quietly
     bent to accommodate one group's interest is how a class system dies.
7. **Rework, and record what changed and why.** Every change traces to the
   objection that caused it. The changed design goes back through the affected
   Stage 07 outputs, not into a side document.
8. **Return to each group whose objection changed the design** and confirm the
   change addresses it. This is the step most often skipped, and skipping it
   converts socialization into consultation — the group raised something, the
   design changed, and they find out at go-live whether it was what they meant.
9. **Run the agreement test and record the result.** Per group: do they
   understand how work will now be selected, sequenced, and reported; do they
   accept the policies that constrain them; and do they know which cadence to
   bring a future concern to. Anything short of yes on all three is recorded as
   a named risk with an owner — not smoothed into agreement.
10. **Produce the rollout plan.** What changes on day one versus later, who
    configures the board, what the first operations review will examine, and
    when the system will be reviewed against these same fitness criteria.
    STATIK is iterative: name the re-run trigger explicitly rather than leaving
    the system to decay until someone notices.

`Layer-3: inline (one-off)` — the structure is specific to socializing *this*
design and is not a capability another flowspace would invoke; the reusable
material lives in `reference/rollout-and-socialization-guide.md`.

## Outputs

| Artifact | Shape | Lands in |
|---|---|---|
| Per-group design views | One per stakeholder group: their dissatisfaction, the elements addressing it, what changes for them, evidence basis stated per finding | `work/08-group-views/` |
| Objection register | Per objection: group, objection, predicted consequence, design element it bears on, classification (evidence / design / interest), and resolution | `work/08-objection-register.md` |
| Design change record | Every change made, the objection that caused it, and the Stage 07 artifact updated | `work/08-change-record.md` |
| Agreement record | Per group: the three-part agreement test result, and any named risk with its owner | `work/08-agreement-record.md` |
| Rollout plan | Day-one scope, configuration owner, first operations review agenda, and the named re-run trigger | `work/08-rollout-plan.md` |
| Final system design | The Stage 07 artifact set as amended, marked as the agreed version | `work/07-*.md` (updated in place, with the change record as the audit trail) |

## Verify

Trace **Stage 02 → Stage 08**: every source group that reported a
dissatisfaction must appear in `work/08-agreement-record.md` with a test result,
or be explicitly recorded as unreachable with the reason. A group whose
complaint shaped the design and who never saw the result is the specific failure
this catches — and it is the failure that produces a technically sound system
nobody adopts.

Trace **Stage 07 → Stage 08**: every entry in `work/08-change-record.md` must
name the Stage 07 artifact it updated, and those artifacts must actually carry
the change. The failure mode: objections are absorbed into meeting notes, the
design is verbally agreed to be different, and the written design still says
what it said before — so whoever configures the board builds the pre-objection
version. Running these checks leaves a one-line result each in the run's
decision log.

## Review

- **Reviewer:** the service owner, as the accountable human for the agreed
  system, with the delivery team confirming operability of the final amended
  design.
- **Intensity:** `heavy` — U-curve default for a final stage, and independently
  warranted: this is the flow's only alignment boundary, it holds real design
  authority, and everything downstream of it is human action outside the flow.
- **Evidence:** a decision-log entry naming the reviewer, the date, each group's
  agreement-test result, every interest objection escalated and how the owner
  decided it, every named risk with its owner, and the agreed re-run trigger.

## Data boundary

- **Max data-class this stage handles:** `internal`
- **Sanctioned engines for this stage:** Rovo, Copilot — per the employer
  sanctioned-tool matrix.
- The objection register carries candid statements from named *groups* and
  inherits Stage 02's attribution rule unchanged: objections are recorded against
  the group, never the individual who voiced them. Interest objections in
  particular are politically sensitive and must be written so they can be read by
  the group that raised them without misrepresenting anyone.
- **No stage of this flow writes to Jira, including this one.** Board
  configuration is a human act after the rollout plan is agreed. This boundary is
  deliberate: the flow's authority ends at a design people have agreed to.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
