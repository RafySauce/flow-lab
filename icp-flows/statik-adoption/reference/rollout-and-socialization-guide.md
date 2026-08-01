---
id: rollout-and-socialization-guide
title: "Rollout and Socialization Guide — Stage 08's Inline Structure"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[statik-method-reference]]"]
---

# Rollout and Socialization Guide

Stage 08's structure. Layer-3 stable reference: Stage 08 is deliberately an
inline one-off rather than a skill (the negotiation is specific to *this* design
being socialized; no other flowspace would invoke it), so the reusable structure
lives here.

## The stance

Socialization is a **negotiation with real design authority**, not a
communications exercise appended to a finished design. Objections raised here
legitimately change classes of service, capacity allocations, WIP limits, board
structure, and reporting.

A design that reaches Stage 08 and emerges unchanged has usually not been
socialized — it has been announced. That is the single most reliable predictor
of a technically sound Kanban system nobody adopts.

## Per-group view template

One per stakeholder group — every customer group from the service frame
(recipients *and* dependants), the delivery team, and any governance
stakeholder. A single generic walkthrough produces polite agreement followed by
non-adoption: people assent to a design whose implications they have not seen,
and object months later in the form of working around it.

```markdown
# <Service> Kanban System — what changes for <group>

## What you told us
<their dissatisfaction, in their words, from work/02-dissatisfaction-*.md>

## What the evidence showed
<the relevant capability/demand findings, each tagged measured or estimated>

## What changes for you
<the design elements addressing their dissatisfaction, in their terms —
 not in board vocabulary>

## What you will be asked to do differently
<new obligations: how to request, what a class of service means for them,
 which cadence they attend>

## What this does not fix
<from the unaddressed lists and Stage 02's out-of-scope list>

## Where to raise a concern later
<the cadence, and what it is empowered to decide>
```

**Lead with their dissatisfaction, not with the board.** The board is the least
interesting part of the design to everyone except the team operating it.

**State the evidence basis honestly, per the mode declaration.** Measured means
measured, with the figure. Elicited means elicited. A WIP limit that is a
starting point rather than a derived figure says so. A stakeholder who later
discovers that a confident number was an estimate stops trusting all the others,
and the design with them.

## The objection map

Common objections and the design element each *properly* bears on. The point of
the map is to stop an objection being answered by changing the wrong thing.

| Objection | Bears on | Does *not* bear on |
|---|---|---|
| "Expedite will be abused" | The invocation policy: who may invoke, on what grounds, and the concurrent limit | Whether to have an expedite class at all |
| "The WIP limits are too low" | The residency evidence behind them — which either exists or does not | The principle of limiting WIP |
| "My work will never get done" | Capacity allocation, and whether their demand type is represented in the class set | The sequencing policy in general |
| "This is more process than we had" | Which policies were previously implicit and are now written down — usually most of them | Whether to have explicit policies |
| "We can't fit our work into these types" | The Stage 03 type set — a genuine loop-back to 3 | The board design |
| "That number doesn't match my experience" | The evidence — check it; if right, loop back to the stage that produced it | The design conclusions drawn from it, until the number is settled |
| "We need to report on individuals" | The metric set's exclusion, which is a stated constraint to be escalated as a decision — not quietly amended | Any other element |

## The three kinds of objection

Treat them differently. Conflating them is how socialization degrades into
either stubbornness or capitulation.

1. **Evidence objections** — "that number is wrong." Check the evidence. If the
   objection is right, take the loop-back to whichever stage produced it. This is
   Stage 08's most valuable output and the reason it holds design authority.
2. **Design objections** — "that limit will not work for us." Rework the element.
   Normal, expected, and the ordinary business of this stage.
3. **Interest objections** — "this reduces my ability to jump the queue."
   Legitimate to surface, and **not resolved by reworking the design.** Name it
   as an interest, and escalate to the service owner as a decision. A capacity
   allocation quietly bent to accommodate one group's interest is how a class
   system dies — slowly, and with no single moment anyone can point at.

## Rework discipline

- Every change traces to the objection that caused it, in
  `work/08-change-record.md`.
- Changes go into the **Stage 07 artifacts themselves**, not into a side
  document. The failure this prevents: objections absorbed into meeting notes,
  the design verbally agreed to be different, and the written design still saying
  what it said before — so whoever configures the board builds the pre-objection
  version.
- **Return to each group whose objection changed the design.** This is the step
  most often skipped, and skipping it converts socialization into consultation:
  the group raised something, the design changed, and they find out at go-live
  whether it was what they meant.

## The agreement test

Per group, three questions. Anything short of yes on all three is recorded as a
named risk with an owner — not smoothed into agreement.

1. Do they understand how work will now be **selected, sequenced, and reported**?
2. Do they **accept the policies that constrain them** — not merely the ones that
   benefit them?
3. Do they know **which cadence to bring a future concern to**?

## Rollout plan shape

```markdown
## Day one
<what changes immediately — usually board structure, classes, and the
 replenishment cadence>

## Deferred
<what waits, and for what — usually WIP limits pending a tuning period,
 and metrics pending data>

## Configuration
<who configures the board; note that no stage of this flow writes to Jira>

## First operations review
<date, attendees, and specifically what will be examined — the starting-point
 WIP limits and the capacity allocation are the usual first agenda>

## Re-run trigger
<the named condition that brings the service back through STATIK: a demand-mix
 shift, a fitness criterion consistently missed, or a fixed review date>
```

The re-run trigger matters more than it looks. STATIK is iterative by design,
and a system with no named re-run condition decays until someone happens to
notice — usually long after the demand it was designed for has changed.
