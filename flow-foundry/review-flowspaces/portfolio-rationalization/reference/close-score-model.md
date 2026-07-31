---
id: close-score-model
title: "Close-Score Model & Recommendation Taxonomy"
type: specification
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-29
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[objective-dictionary-template]]"
  - "[[export-and-field-requirements]]"
---

# Close-Score Model & Recommendation Taxonomy

The scoring rubric Stage 04 applies and the recommendation bands Stage 05 uses.
One file, because a score is meaningless without the band it lands in and a band
is unjustifiable without the score behind it.

> **Every number in this document is a proposal.** The ramps were inferred from
> five data points the operator described from an existing analysis workbook,
> not derived from its formulas. They have never been run against a full cycle
> of real portfolio data. Calibration against one real cycle — and confirming
> the bands produce a review volume the governance process can absorb — is an
> operator gate before the first live run. See "Calibration status" below.

---

## 1. What the score is, and is not

The close score is a **composite triage indicator**. It combines strategic
alignment, age, inactivity, data quality, and workflow state into one number
whose only job is to rank items for human attention.

It is **not** a measure of business value. A high close score says the
observable data around an item is weak — not that the work is worthless. An
item can be genuinely critical and score 95 because nobody has touched its
ticket in eight months and its description is three words. That is exactly the
item a governance review should look at, which is the point.

Every score is invalid without its per-dimension breakdown. Stage 04 emits
both or neither.

## 2. The governing principle

**Do not close work simply because it is old.**

Age is the most available signal and the most misleading one. A long-lived item
in active delivery, well-aligned to an objective and updated last week, is
healthy — age alone tells you nothing. The model encodes this structurally in
two ways:

1. Age is capped at 35 of ~100 points — it cannot reach a closure band alone.
2. The **corroboration rule** (§5) blocks the two closure bands outright unless
   at least three of the five dimensions fire.

Neither is advice. Both are checks Stage 04 runs and Stage 05 enforces.

## 3. The five dimensions

| # | Dimension | Range | Signal source |
|---|---|---|---|
| 1 | Age | 0 → 35 | Days since `Created` |
| 2 | Objective unrelatedness | 0 → 40 | Stage 03 mapping confidence + score |
| 3 | Staleness | 0 → 15 | Days since `Updated` |
| 4 | Low field completion | 0 → 10 | Populated fields ÷ available columns |
| 5 | Status / overdue adjustment | −10 → +14 | `Status` / `Status Category` + `Due date` |

Dimensions 1–4 sum to a 0–100 base. Dimension 5 is an adjustment, not a
component — it is why a total can exceed 100 (max 114) or fall below the base
(min −10). Totals are not clamped: a −4 total is a legitimate, informative
result meaning "actively being delivered, well aligned, recently touched."

### 3.1 Age — 0 to 35

Linear ramp on days since `Created`:

- ≤ 90 days → 0
- ≥ 400 days → 35
- Between → `35 × (days − 90) ÷ 310`, rounded to the nearest integer.

*Why 90 and 400:* below a quarter, age carries no signal — the item has not had
time to go stale. Above roughly 13 months an item has survived a full planning
cycle plus a quarter without completing, which is where age starts meaning
something on its own.

### 3.2 Objective unrelatedness — 0 to 40

The largest single dimension, and the only one that is not an observable Jira
fact. It reads Stage 03's output, inverting alignment into unrelatedness:

| Stage 03 result | Points |
|---|---|
| High confidence | 0 – 5 |
| Medium confidence | 10 – 20 |
| Low confidence / weak match (mapping score 1–3) | 30 – 35 |
| `Needs objective review` (no match) | 40 |

Within a band, position is set by the mapping score: a high-confidence item
with a mapping score of 14 takes 0; one scraping the top of the medium
threshold takes 5. Stage 03's dictionary defines the confidence thresholds
(`objective-dictionary-template.md` §4).

**A secondary possible match reduces this dimension by 5 points, floored at the
band minimum.** An item that plausibly supports two objectives is not
unaligned — it is ambiguously aligned, which is a different and much weaker
closure signal.

*Caution:* `Needs objective review` at 40 points is the heaviest single push in
the model, and it fires on items whose *wording* failed to match, not
necessarily whose *work* is unaligned. This is deliberate — such items need
human attention — but it is also why Stage 03 carries heavy review and why the
corroboration rule exists. An item that is merely badly worded will typically
fail to corroborate on the other dimensions and stay out of the closure bands.

**Provenance caveat.** Stage 03's dictionary may carry `provenance: inferred`
rather than `operator-authored` (`objective-dictionary-template.md` §9). This
dimension's arithmetic does not change based on provenance — an
inferred-and-confirmed mapping scores exactly as an authored one would. What
changes is that every score built on an inferred dictionary carries a caveat
through Stage 04 and Stage 05, because it has not been through the same
organizational-accountability test an authored dictionary's owner provides.
Treat the caveat as trust information for the reader, not a scoring
adjustment.

### 3.3 Staleness — 0 to 15

Linear ramp on days since `Updated`:

- ≤ 30 days → 0
- ≥ 180 days → 15
- Between → `15 × (days − 30) ÷ 150`, rounded to the nearest integer.

*Known distortion:* bulk edits, automation rules, and sprint rollovers all
touch `Updated` without anyone thinking about the work. Where the export
carries comment timestamps, Stage 04 should prefer the most recent *human*
touch (comment, status change, field edit) over the raw `Updated` value, and
record which it used. Where it cannot tell, it uses `Updated` and flags the
item's staleness score as low-confidence in the breakdown.

### 3.4 Low field completion — 0 to 10

Ramp on the item's populated-field percentage, per the denominator rule in
`export-and-field-requirements.md` §4:

- ≥ 60% populated → 0
- ≤ 20% populated → 10
- Between → `10 × (60 − pct) ÷ 40`, rounded to the nearest integer.

*Why the ceiling is low:* sparse metadata is weak evidence on its own. Plenty
of well-understood work carries thin tickets, and plenty of doomed work is
documented beautifully. It earns 10 points as a corroborating signal, not more.

### 3.5 Status / overdue adjustment — −10 to +14

Two independent components, summed:

**Status component:**

| Status | Adjustment | Reasoning |
|---|---|---|
| On Hold | +8 | Explicitly parked — the strongest workflow-state closure signal |
| Backlog | +6 | Never started |
| Analyzing | +4 | Started but pre-commitment |
| Ready | +2 | Committed, not started |
| Review | 0 | Nearly delivered — neutral |
| In Progress | −10 | Actively being delivered — pushes *away* from closure |

**Overdue component:** `+6` when a `Due date` is set and has passed. No
adjustment when the due date is future or absent — a missing due date is a
completeness signal already counted in §3.4, not a second penalty here.

**Status names are instance-specific.** The table above uses the statuses the
operator's portfolio actually carries. At instantiation, map the instance's
real workflow statuses onto this table via `Status Category` (To Do /
In Progress / Done) as the fallback for any status not listed, and record the
mapping in the instance's `decision-log/`. An unmapped status defaults to 0
and is flagged in the breakdown, never silently scored.

## 4. Recommendation bands

| Band | Score | Meaning |
|---|---|---|
| `Close (recommended)` | ≥ 95 | Multiple strong signals agree the item is stale, weakly aligned, underdeveloped, and not in delivery. Recommend closure to the owner. |
| `Strong close candidate` | 80 – 94 | High-priority governance review. Likely close, merge, or re-scope — the owner decides which. |
| `Review for closure` | 65 – 79 | Needs owner review before any decision. The signals are real but not conclusive. |
| `Keep / not closure-priority` | < 65 | Appears active, aligned, recent, or strategically relevant. No action this cycle. |

> **Naming note.** The source taxonomy's top band was `Closed`. Renamed here to
> `Close (recommended)`: `Closed` reads as a Jira status and invites the reading
> that the flow already closed something, which it cannot do — this flow has no
> write path to Jira at any stage. Proposed per `AGENTS.md` rule 7, awaiting
> operator ratification.

Every band label is a **triage recommendation, not an action.** Nothing in this
flow closes, merges, or edits anything. Stage 06 captures what the humans
decide, which may differ from every recommendation in the pack.

## 5. The corroboration rule

**No item may be banded `Close (recommended)` or `Strong close candidate`
unless at least three of the five dimensions score above their midpoint.**

Midpoints:

| Dimension | Midpoint | Fires above |
|---|---|---|
| Age | 17.5 | > 17 |
| Objective unrelatedness | 20 | > 20 |
| Staleness | 7.5 | > 7 |
| Low field completion | 5 | > 5 |
| Status / overdue | +2 | > +2 |

An item scoring ≥ 80 on fewer than three firing dimensions is **demoted to
`Review for closure`**, and Stage 05's packet states the demotion and its cause
explicitly: "scored 88 but only 2 of 5 dimensions corroborate — reviewing, not
recommending closure."

This is the model's central guard. Without it, a 500-day-old item with a
`Needs objective review` flag reaches 75+ on two dimensions alone, and the
"don't close work simply because it is old" principle becomes a slogan rather
than a rule. The demotion path — rather than an outright block — keeps the item
visible for review instead of hiding it.

## 6. Worked examples (synthetic)

Three synthetic items, `PORT-nn` keys, exercising the model's edges. These are
illustrations of the arithmetic, not real portfolio data.

### PORT-01 — old, sparse, unaligned, parked

Created 434 days ago · Updated 212 days ago · 21% fields populated · Backlog ·
no due date · Stage 03: weak match, mapping score 1, no secondary match.

| Dimension | Score | Fires? |
|---|---|---|
| Age | 35 (≥400d cap) | ✓ |
| Objective unrelatedness | 35 (weak, no secondary) | ✓ |
| Staleness | 15 (≥180d cap) | ✓ |
| Field completion | 10 (≤20%… 21% → 10) | ✓ |
| Status / overdue | +6 (Backlog, not overdue) | ✓ |
| **Total** | **101** | 5 of 5 |

→ `Close (recommended)`. Five of five corroborate. This is the shape of a
genuine top-ranked closure candidate: every available signal points the same
direction.

### PORT-02 — old, but in delivery and well aligned

Created 480 days ago · Updated 9 days ago · 68% fields populated ·
In Progress · due date future · Stage 03: high confidence, mapping score 14.

| Dimension | Score | Fires? |
|---|---|---|
| Age | 35 | ✓ |
| Objective unrelatedness | 0 | ✗ |
| Staleness | 0 | ✗ |
| Field completion | 0 | ✗ |
| Status / overdue | −10 (In Progress) | ✗ |
| **Total** | **25** | 1 of 5 |

→ `Keep / not closure-priority`. Older than PORT-01 and nowhere near a closure
band. This is the case the model exists to get right: age is maxed and
irrelevant, because nothing corroborates it.

### PORT-03 — recent, thin, ambiguously aligned, overdue

Created 150 days ago · Updated 95 days ago · 34% fields populated ·
Analyzing · overdue · Stage 03: medium confidence, score 6, secondary match
present.

| Dimension | Score | Fires? |
|---|---|---|
| Age | 7 (`35 × 60 ÷ 310`) | ✗ |
| Objective unrelatedness | 10 (medium 15, −5 secondary) | ✗ |
| Staleness | 7 (`15 × 65 ÷ 150`) | ✗ |
| Field completion | 7 (`10 × 26 ÷ 40`) | ✓ |
| Status / overdue | +10 (Analyzing +4, overdue +6) | ✓ |
| **Total** | **41** | 2 of 5 |

→ `Keep / not closure-priority` on score alone. The overdue-and-thin
combination is worth surfacing in Stage 02's due-date lens, but it is not a
closure signal — the item is young and plausibly aligned. Had it scored into a
closure band, the corroboration rule would have demoted it anyway at 2 of 5.

### Demotion example

An item scoring 87 with only Age (35) and Objective unrelatedness (40) firing —
staleness 6, completion 4, status +2 (Ready, not overdue) — is **demoted to
`Review for closure`**. None of the last three clears its midpoint (7, 5, +2
are all *at or below* the thresholds, and the rule is strictly greater-than),
so two dimensions are carrying an 87, and two dimensions cannot carry a closure
recommendation regardless of total.

This is the archetype the corroboration rule exists for: an old item nobody
managed to map to an objective. Age and unrelatedness together reach 75 before
any other evidence, and both are the least reliable signals in the model — age
because it says nothing on its own, unrelatedness because it fires on wording
failures as readily as on genuine misalignment.

## 7. Calibration status

Unratified. What the operator must confirm before the first live run:

1. **The five ramps.** Anchors 90/400 (age), 30/180 (staleness), 60/20
   (completion) are inferred, not measured. Run one real cycle and check the
   score distribution has usable spread rather than clustering.
2. **The band thresholds.** 95 / 80 / 65 should produce a review volume the
   governance process can absorb. If a cycle yields 40 strong close candidates
   out of 60 items, the thresholds are wrong, not the portfolio.
3. **The status adjustment table**, mapped to the instance's real workflow
   statuses (§3.5).
4. **The confidence-to-points mapping in §3.2**, against the instance's actual
   objective dictionary once authored — the confidence thresholds live there,
   and this table has to agree with them.
5. **Whether `Needs objective review` at 40 is too heavy** in practice. It is
   the single largest push in the model and fires on a wording failure. One
   real cycle will show whether the corroboration rule is sufficient protection
   or whether the ceiling needs lowering.
6. **Whether inferred-and-confirmed dictionaries need materially different
   treatment** once real cycles run with them — an open question, deliberately
   not resolved by adding an untested point adjustment now (§3.2's provenance
   caveat).

Record the calibration decision in the instance's `decision-log/` and bump this
file's `artifact-version` when any number changes.
