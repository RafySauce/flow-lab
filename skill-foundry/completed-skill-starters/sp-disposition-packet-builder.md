---
id: sp-disposition-packet-builder
title: "Skill Primer Brief — Disposition Packet Builder"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[close-score-model]]"
---

# Skill Primer Brief — Disposition Packet Builder

## Purpose

Turn a ranked, scored portfolio into something a named human can act on: band
each item into the recommendation taxonomy, enforce the corroboration rule,
build a per-item disposition packet (recommendation, signals that fired,
evidence trail, caveats, and a question worth asking the owner), and route the
packets by assignee. This is the step the source analysis never had — it is
what converts a ranking nobody reviews into four items each person will
actually look at.

## Triggering intent

**Fires on:** Stage 05 of `portfolio-rationalization`. Also standalone on
"build the review pack," "turn these scores into recommendations," "who needs
to look at what," "route these findings to owners."

**Does not fire on:**

- Computing scores — that is `closure-scorer`, upstream. This skill bands and
  packages; it never rescores.
- Closing, merging, labeling, or commenting on Jira items. There is no write
  path anywhere in this flow, and this skill should decline rather than route
  such a request — including to `jira-commit`, whose job is creating refined
  items, not bulk portfolio actions.
- Capturing what humans decided — that is Stage 06's inline capture protocol.

## Method sketch

1. Band per `close-score-model.md` §4: `Close (recommended)` ≥95, `Strong close
   candidate` 80–94, `Review for closure` 65–79, `Keep / not closure-priority`
   <65.
2. **Enforce the corroboration rule.** Any item in the top two bands with fewer
   than three firing dimensions is **demoted to `Review for closure`**, and the
   demotion is stated in the packet in plain language, not footnoted. This is
   the flow's governing principle made operational — a silent demotion teaches
   nobody anything.
3. Build packets for the three review-worthy bands (the keep band gets a
   summary line). Each carries: identity; the recommendation framed as a
   recommendation; **the signals that fired in plain language** ("434 days old,
   no update in 212 days, 21% of fields populated, sits in Backlog, weak
   objective alignment") rather than a bare number; the full evidence trail
   including matched keywords and dictionary version; every applicable caveat;
   and a **suggested question specific to that item's signal pattern**.
4. Handle `Needs objective review` items as **alignment questions, not closure
   questions**, whatever their score. The bucket covers three situations the
   mapping cannot distinguish, and collapsing them into a closure framing is
   the most likely way this flow produces a wrong recommendation.
5. Identify merge candidates — shared parents, heavily overlapping summaries
   and matched keywords — and note them in both packets of each pair. Merge is
   often right for real-but-fragmented work and is invisible to a per-item
   score.
6. Route by assignee, one section each, score-ordered; unassigned routes to the
   operator.
7. Build the cycle summary (band counts, demotions, needs-review count, merge
   candidates, calibration status).
8. Head the pack with the framing statement: triage recommendations from
   observable signals, not proof an item lacks value, nothing closed by this
   process.

**Quality bar:** an owner reading their section can tell, without asking
anyone, why each item is in front of them and what specifically they are being
asked.

**Failure modes to guard against:**

- Computing the corroboration rule upstream and then not enforcing it here —
  produces exactly the outcome the flow exists to prevent.
- Generic suggested questions. "Is this still needed?" on every packet wastes
  the owner's time and produces generic answers.
- Packets that hide their own weak evidence by omitting caveats.
- Presenting a band label as a decision rather than a recommendation.
- Circulating the whole pack broadly — assignee names paired with
  recommendations about their work is the most sensitive artifact the flow
  produces.

## Inputs and data boundary

**Needs:** scores, dimension breakdowns, corroboration counts, ranked
portfolio, and caveats from `closure-scorer`; mapping records and the
`Needs objective review` bucket from `objective-keyword-mapper`; the assignee
distribution and oldest-and-sparsest cross-cut from `portfolio-profiler`;
parent keys from the normalized set; band thresholds and label semantics from
`close-score-model.md` §4–5.

**Max data-class:** `internal`. The outreach list pairs named individuals with
recommendations about their work — more sensitive than either part alone.
**Per-assignee distribution is a data-handling constraint, not a courtesy.**

**Engines:** Rovo and Copilot both. No constraint.

## Demand source

Layer-3 gap at Stage 05 of the `portfolio-rationalization` flowspace, filed
during its scaffold. Stage 05 is the "Recommend" step the operator identified
as missing from the source analysis and asked to have built out.

## Definition of done

- Banding matches the thresholds exactly, and no item in the top two bands has
  a corroboration count below 3 — checked both directions against the demotion
  record.
- Every packet's suggested question is item-specific; a reviewer sampling ten
  packets finds ten different questions.
- Every caveat from upstream appears in its item's packet.
- `Needs objective review` items are never framed as closure candidates.
- The pack is routable — an owner's section stands alone and is
  self-explanatory without the rest of the pack.
- Declines any request to act on Jira, and says what it produces instead.
