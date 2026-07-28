---
id: sp-closure-scorer
title: "Skill Primer Brief — Closure Scorer"
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

# Skill Primer Brief — Closure Scorer

## Purpose

Apply the close-score model to a mapped, profiled portfolio: five weighted
dimensions (age, objective unrelatedness, staleness, field completion,
status/overdue) combined into one composite triage score per item, each emitted
with the per-dimension breakdown that makes it arguable. Replaces an
unrecorded, unrepeatable ranking with a written model anyone can check.

## Triggering intent

**Fires on:** Stage 04 of `portfolio-rationalization`. Also standalone on
"score these items for closure risk," "rank the backlog by staleness and
alignment," "which items have the weakest signals."

**Does not fire on:**

- "Close these items" / "recommend dispositions" — banding into
  recommendations is `disposition-packet-builder`, and closing is nothing in
  this flow. This skill produces numbers and breakdowns, not verdicts.
- Estimating business value or priority. The score is a triage indicator over
  observable ticket data, and must decline framings that treat it as a value
  measure — a high score says the data around an item is weak, not that the
  work is worthless.
- Profiling distributions — that is `portfolio-profiler`, upstream.

## Method sketch

1. **State calibration status before presenting any score.** If the model's
   ramps are unratified, say so: provisional numbers, provisional ranking.
2. Load the instance's status→adjustment mapping; fall back to `Status
   Category`; **an unmapped status with no fallback scores 0 and is flagged**,
   never silently valued.
3. Score the five dimensions per `close-score-model.md` §3 — age (0–35),
   objective unrelatedness (0–40, minus 5 for a recorded secondary match,
   floored at the band minimum), staleness (0–15), low field completion (0–10),
   status/overdue (−10..+14).
4. Prefer the **most recent human touch** over raw `Updated` for staleness
   where comment timestamps exist; flag raw-`Updated` items low-confidence.
   Bulk edits, automation, and sprint rollovers move `Updated` without anyone
   thinking about the work.
5. Take completion figures from the profiler; **do not recompute** against a
   different denominator.
6. Sum. **Do not clamp** — a negative total is legitimate and informative.
7. Compute the **corroboration count**: how many dimensions score above their
   midpoint, and which. This travels with every score; the downstream bander
   cannot run without it.
8. Emit breakdown with every total. A total without its breakdown is an invalid
   output.
9. Rank descending; sanity-check the top of the age ranking and the
   oldest-and-sparsest cross-cut against the totals — divergence means a date
   parse or denominator mismatch, not a finding.

**Quality bar:** the arithmetic is reproducible from the breakdown alone. Hand
someone the breakdown and the model file, and they can rederive the total.

**Failure modes to guard against:**

- Presenting provisional scores as settled.
- Clamping negatives — hides the healthiest items' signal.
- Recomputing completion against a different denominator than the profiler
  used.
- Treating a missing Due date as "not overdue" rather than unknown.
- Emitting a total without its breakdown — the score becomes unarguable and
  the governance conversation stalls.
- Letting a confidence band with no points row silently score as zero
  unrelatedness.
- Scoring an item as more closeable because its export lacked a column. A
  missing signal scores zero, never a penalty.

## Inputs and data boundary

**Needs:** the normalized item set (Created, Updated, Status, Status Category,
Due date, comment timestamps) from `jira-portfolio-ingest`; per-item completion
from `portfolio-profiler`; the mapping record with confidence, score, and
secondary matches from `objective-keyword-mapper`; the model itself
(`close-score-model.md`); and the instance's status mapping and calibration
status from the instance decision log.

**Max data-class:** `internal`. Purely computational — no external access, no
new data enters here. **Comment bodies must not travel into this skill's
outputs**: it reads comment *timestamps* only, and comment text is the
highest-risk content in a Jira export with no reason to propagate.

**Engines:** Rovo and Copilot both. No constraint.

## Demand source

Layer-3 gap at Stage 04 of the `portfolio-rationalization` flowspace, filed
during its scaffold. The stage contract carries this brief's id.

## Definition of done

- Reproduces the model's three worked synthetic examples
  (`close-score-model.md` §6) exactly, including the negative-adjustment case
  and the demotion case.
- Every score carries a complete five-dimension breakdown and a corroboration
  count.
- Refuses to emit a score without its breakdown.
- States calibration status unprompted, every run.
- Declines to be used as a value or priority measure, and says what it is
  instead.
- Passes the Stage 02 sanity cross-check on a real portfolio.
