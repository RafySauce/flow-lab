---
id: sp-portfolio-profiler
title: "Skill Primer Brief — Portfolio Profiler"
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
  - "[[export-and-field-requirements]]"
---

# Skill Primer Brief — Portfolio Profiler

## Purpose

Profile a normalized Jira portfolio — distributions by status, assignee,
priority, and due-date category; age ranking; per-item field completion; and
the oldest-and-sparsest cross-cut — and offer the operator exploration lenses
*before* any judgment is applied. Replaces the hand-built pivot tables that
currently answer "what are we even looking at?" once, in a spreadsheet nobody
can re-run.

## Triggering intent

**Fires on:** Stage 02 of `portfolio-rationalization`. Also standalone on
"profile this portfolio," "what does our backlog look like," "show me the
shape of this project," "how complete are these tickets."

**Does not fire on:**

- "Which of these should we close" / "score these for closure" — that is
  `closure-scorer`, downstream. This skill deliberately stops short of
  judgment, and blurring that line destroys its whole value.
- Mapping items to objectives — that is `objective-keyword-mapper`.
- Individual performance questions ("who is behind on their tickets"). The
  assignee output is a workload distribution and must not be repurposed into a
  named ranking; the skill should decline this framing explicitly.

## Method sketch

1. State the frame: item count **and** completion denominator together, up
   front.
2. Distributions — status (and Status Category), assignee (unassigned counted
   separately and explicitly), priority, due-date buckets (overdue / ≤30 days /
   future / none).
3. Age ranking by `Created`, oldest 10 surfaced with key, summary, days.
4. Per-item field completion, same denominator for every item, **every
   percentage reported with its absolute counts** (`44 of 216 — 20.4%`).
5. The oldest-and-sparsest cross-cut — intersect age and completion rankings.
   This is the highest-value view and the one no single-axis read surfaces.
6. **Offer the exploration lenses and stop.** Status, assignee workload, due
   dates and risk, priority, labels, custom fields, something else. Wait for
   the operator.
7. Explore the chosen lens to whatever depth is asked; repeat the offer. The
   operator ends exploration, not the skill.
8. Annotate degraded signals **in place** in the affected section, not only in
   a footnote.

**Quality bar:** every distribution's categories sum to the confirmed item
count. An item with a null status or unparseable date must appear in an
explicit "uncategorized" count, never fall silently out of every bucket.

**Failure modes to guard against:**

- Advancing past the lens offer without operator response — the single most
  likely way the flow degrades into a scoring machine nobody trusts.
- Reporting percentages without denominators.
- Emitting an assignee ranking rather than a distribution.
- Reporting "no due date" for every item when the Due date field is absent
  entirely — those are different facts.
- A missing section reading as "nothing to report" when it means "field
  unavailable."

## Inputs and data boundary

**Needs:** the normalized item set, confirmed item count, completion
denominator, field-availability report, and degraded-signal list — all from
`jira-portfolio-ingest`. No external access; this skill computes over what it
is handed.

**Max data-class:** `internal` — it handles assignee names for the workload
distribution. The distribution-not-ranking rule is a data-handling constraint,
not a presentation preference.

**Engines:** Rovo and Copilot both. No constraint.

## Demand source

Layer-3 gap at Stage 02 of the `portfolio-rationalization` flowspace, filed
during its scaffold. The stage contract carries this brief's id.

## Definition of done

- Distributions sum to the item count in every dimension, with uncategorized
  items surfaced rather than dropped.
- Never advances without the lens offer being made and answered.
- Percentages never appear without their absolute counts.
- Declines to produce a named performance ranking from the assignee data, and
  says why.
- The oldest-and-sparsest cross-cut is produced as a first-class output, not
  derivable-on-request.
- Degraded signals appear in the profile body, where the missing numbers would
  have been.
