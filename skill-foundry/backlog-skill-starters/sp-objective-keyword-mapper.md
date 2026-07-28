---
id: sp-objective-keyword-mapper
title: "Skill Primer Brief — Objective Keyword Mapper"
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
  - "[[objective-dictionary-template]]"
---

# Skill Primer Brief — Objective Keyword Mapper

## Purpose

Map every item in a normalized Jira portfolio to the organization's strategic
objective areas using a transparent, versioned keyword dictionary — emitting
mapped area, confidence, score, the keywords that matched and where, and any
secondary possible match. Replaces the manual, unrecorded judgment that
currently decides whether a ticket "supports the strategy," and makes each
decision arguable by pointing at its evidence.

## Triggering intent

**Fires on:** Stage 03 of `portfolio-rationalization`. Also standalone on "map
these items to our objectives," "which OKR does this work support," "how much
of the portfolio is aligned to <area>," "find the unaligned work."

**Does not fire on:**

- "Should we close this" — that is `closure-scorer` and
  `disposition-packet-builder` downstream. This skill produces alignment
  evidence, never a closure verdict, and `Needs objective review` must never be
  presented as one.
- Refining a single item's business-outcome wording — that is
  `context-elicitation` in the `ai-refinement` flow.
- Authoring the objective dictionary itself. The dictionary is a human
  artifact; this skill consumes it and proposes additions from feedback, but
  never invents objective areas.

## Method sketch

1. Load the instance dictionary; echo back its areas, term counts, weight
   distribution, `artifact-version`, and last-updated date. **Operator confirms
   it is current for the planning cycle before any matching runs.**
2. Present prior-cycle revision notes as proposed term additions, accepted or
   rejected individually. Never fold in silently — a dictionary change alters
   scores and must be visible.
3. **Halt if no dictionary exists.** This is the hard dependency. Objective
   areas cannot be inferred from the portfolio; an agent that invents them
   produces confident, plausible, worthless mappings.
4. Declare the searchable field set for this cycle from the field-availability
   report; call out an absent Business Outcome explicitly.
5. Match each item against every area: **distinct** terms only (six
   occurrences count once — repetition is style, not evidence), summing
   weights, recording the source field of every hit.
6. Assign confidence per the dictionary's thresholds. **High requires at least
   one weight-3 term, not score alone** — 8 points of weight-1 generics is a
   coincidence.
7. Primary = highest-scoring area. Secondary recorded when the runner-up scores
   ≥60% of the primary. **True ties flag for human assignment, never
   auto-assign.**
8. Bucket zero-match items as `Needs objective review`, with the
   three-cases framing attached in the output itself (poorly worded work /
   dictionary gap / genuine misalignment — indistinguishable to the mapping).
9. Degrade rather than fail on thin items: a Summary-only match is valid but
   flagged and **capped below High** regardless of score.
10. Present the mapping distribution for operator review; support spot-checks
    against matched-keyword evidence; record every override with its reason.

**Quality bar:** every mapping is explainable by pointing at the keywords that
fired and the fields they fired in. A mapping nobody can argue with will not
survive its first governance meeting.

**Failure modes to guard against:**

- Running against a stale dictionary — maps the whole portfolio against
  strategy that no longer exists, with no visible symptom.
- Inventing objective areas when none are supplied.
- Counting repeated terms multiple times, inflating scores for verbose tickets.
- Promoting a Summary-only match to High confidence.
- Emitting a confidence band the downstream scoring model has no points row for
   — it scores as zero unrelatedness and turns an unmappable item into an
  apparently well-aligned one.
- Presenting `Needs objective review` as a closure signal.

## Inputs and data boundary

**Needs:** the normalized item set and field-availability report from
`jira-portfolio-ingest`; the instance's objective dictionary (authored from
`objective-dictionary-template.md`); the confidence-to-points table in the
flowspace's `reference/close-score-model.md` §3.2, which its output must agree
with.

**Max data-class:** `internal` for the item set — **but the dictionary itself
may be higher.** Objective-area statements are often `internal` or
`confidential` strategy content. Confirm the dictionary's own `data-class` at
instantiation and route this skill to engines sanctioned for *that* class, not
merely for the portfolio's. This is a real constraint and the main reason this
skill's engine routing may end up narrower than the rest of the flow's.

**Engines:** Rovo and Copilot both, subject to the dictionary's classification.

## Demand source

Layer-3 gap at Stage 03 of the `portfolio-rationalization` flowspace, filed
during its scaffold. The stage contract carries this brief's id. Stage 03
carries heavy review specifically because of this skill's failure modes.

## Definition of done

- Every item maps to exactly one primary area or the review bucket — never
  both, never neither.
- Every mapping carries its matched keywords with their source fields.
- Confidence bands agree exactly with the scoring model's points table; a
  mismatch is a build failure, not a warning.
- Halts cleanly and explains itself when no dictionary is present.
- Ties and overrides are surfaced to the human, never resolved silently.
- Runs against a dictionary of at least three areas and 30+ terms and produces
  a distribution the operator recognizes as plausible.
