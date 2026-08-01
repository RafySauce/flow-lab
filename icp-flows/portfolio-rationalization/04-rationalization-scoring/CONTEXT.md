---
id: portfolio-rationalization-stage-04
title: "Stage 04 — Rationalization Scoring"
type: stage-context
stage: 4
review-intensity: light
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
  - "[[close-score-model]]"
---

# Stage 04 — Rationalization Scoring

## Inputs

| Input | Source | Required |
|---|---|---|
| Normalized item set (Created, Updated, Status, Status Category, Due date, Comments) | Stage 01 | Yes |
| Field-availability report and degraded-signal list | Stage 01 | Yes |
| Per-item field-completion percentage with absolute counts | Stage 02 | Yes |
| Age ranking (for the sanity cross-check) | Stage 02 | Yes |
| Per-item mapping record — area, confidence band, score, secondary match | Stage 03 | Yes |
| Summary-only / degraded mapping flags | Stage 03 | Yes |
| Dictionary provenance (`operator-authored` / `inferred-and-confirmed`) | Stage 03 | Yes |
| The scoring model — dimensions, ramps, ceilings, corroboration rule | `../reference/close-score-model.md` | Yes |
| Instance status→adjustment mapping (real workflow statuses onto the model's table) | Instance `decision-log/`, set at instantiation | Yes |
| Calibration ratification status | Instance `decision-log/` | Yes |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-closure-scorer)`

1. **State the calibration status up front.** If the model's ramps have not been
   ratified against a real cycle (`../reference/close-score-model.md` §7), say
   so before presenting any score: these are proposed numbers producing
   provisional rankings. An unratified model still ranks usefully — it just must
   not be presented as settled.
2. **Load the instance's status mapping.** The model's status table names the
   statuses of one portfolio; instances differ. Apply the instance's mapping,
   falling back to `Status Category` for any status not explicitly mapped. **An
   unmapped status with no category fallback scores 0 and is flagged in that
   item's breakdown** — never silently assigned a value.
3. **Score dimension 1 — Age.** Days since `Created`: 0 at ≤90, 35 at ≥400,
   linear between (`35 × (days − 90) ÷ 310`, rounded).
4. **Score dimension 2 — Objective unrelatedness.** Invert Stage 03's
   confidence into unrelatedness per §3.2: High 0–5, Medium 10–20, Low/weak
   30–35, `Needs objective review` 40. Position within the band comes from the
   mapping score. **Subtract 5 for a recorded secondary match, floored at the
   band minimum** — ambiguous alignment is not misalignment. For a Summary-only
   or otherwise degraded mapping, record the degradation alongside the score:
   the reviewer needs to know the 35 came from thin text rather than clear
   misalignment. **If this cycle's dictionary carries `provenance: inferred`,
   record that alongside the score as a caveat** — the same handling as a
   Summary-only mapping. Do not adjust the point value: adjusting the
   arithmetic for a provenance difference the model has never been calibrated
   against would be a second unratified number on top of the first.
5. **Score dimension 3 — Staleness.** Days since `Updated`: 0 at ≤30, 15 at
   ≥180, linear between. **Prefer the most recent human touch** (comment, status
   change, field edit) over raw `Updated` where comment timestamps are
   available — bulk edits, automation rules, and sprint rollovers all move
   `Updated` without anyone thinking about the work. Record which source was
   used per item; where only raw `Updated` is available, flag that item's
   staleness score low-confidence.
6. **Score dimension 4 — Low field completion.** From Stage 02's per-item
   percentage: 0 at ≥60%, 10 at ≤20%, linear between. Use Stage 02's figures
   directly — do not recompute against a different denominator.
7. **Score dimension 5 — Status/overdue adjustment.** Status component per the
   instance mapping (In Progress −10 through On Hold +8); overdue component +6
   when a Due date is set and has passed. **A missing Due date contributes 0 and
   is reported as unknown, not as "not overdue"** — those are different facts,
   and incompleteness is already counted in dimension 4.
8. **Sum to the total.** Dimensions 1–4 give a 0–100 base; dimension 5 adjusts
   it to a −10..114 range. **Do not clamp.** A negative total is a legitimate,
   informative result meaning actively delivered, well aligned, recently
   touched.
9. **Evaluate the corroboration rule.** Count how many of the five dimensions
   score above their midpoint (Age >17, Unrelatedness >20, Staleness >7,
   Completion >5, Status/overdue >+2). Record the count and which dimensions
   fired. This count travels with the score — Stage 05 cannot band without it.
10. **Emit the breakdown with every score.** A total without its per-dimension
    breakdown is an invalid output of this stage. The breakdown is what makes
    the score arguable, and a score nobody can argue with will not survive its
    first governance conversation.
11. **Rank the portfolio** by total, descending.
12. **Sanity-check against Stage 02.** Confirm the top of the age ranking and
    the top of the age-dimension scores agree, and that the
    oldest-and-sparsest cross-cut items appear in the upper half of the total
    ranking. A divergence means a date parse or a denominator mismatch, not an
    interesting finding.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Per-item close score | Stage 05 (banding), Stage 06 | Integer, −10 to 114, unclamped |
| Per-item dimension breakdown | Stage 05 (packet evidence), Stage 06 | Five named dimensions with their points and the inputs each was computed from |
| Corroboration count and firing dimensions | Stage 05 — **required for banding** | Integer 0–5 + the named dimensions above midpoint |
| Ranked portfolio | Stage 05, Stage 06 | Items ordered by total, descending |
| Per-item scoring caveats | Stage 05 (packet), Stage 06 | Low-confidence staleness, degraded mapping, unmapped status, unknown due date, inferred-dictionary provenance — per item |
| Calibration status declaration | Stage 05, Stage 06; cycle decision log | Ratified / unratified, with the model's `artifact-version` |
| Sanity-check result vs. Stage 02 | Cycle decision log | Pass, or the divergence found |

## Verify

Cross-stage trace: every item's objective-unrelatedness score traces back to the
confidence band Stage 03 assigned it, and every item's completion score traces
back to the percentage Stage 02 computed. Check a sample across all four
confidence bands that the unrelatedness points fall inside the band range
`../reference/close-score-model.md` §3.2 defines, and that a secondary match
where present reduced the score by exactly 5 without breaching the band floor.
The failure this catches is a confidence band drifting out of sync with the
points table — Stage 03 emitting a band the model has no row for, which scores
as zero unrelatedness and turns an unmappable item into an apparently
well-aligned one. Running this check leaves a one-line result in the cycle's
decision log.

- [ ] Calibration status stated before any score was presented
- [ ] Instance status mapping applied; unmapped statuses scored 0 and flagged,
      not silently valued
- [ ] All five dimensions scored for every item
- [ ] Secondary-match reduction of exactly 5 applied where recorded, floored at
      the band minimum
- [ ] Staleness used the most recent human touch where comments were available;
      raw-`Updated` items flagged low-confidence
- [ ] Completion scores taken from Stage 02's figures, not recomputed
- [ ] Missing Due date contributed 0 and is reported as unknown, not as
      "not overdue"
- [ ] Totals unclamped — negatives preserved
- [ ] Corroboration count computed and travelling with every score
- [ ] Every score carries its per-dimension breakdown
- [ ] Sanity cross-check against Stage 02's age ranking and
      oldest-and-sparsest cross-cut passed, or the divergence was investigated

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution. The model is fully specified in
  `../reference/close-score-model.md`; this stage applies it rather than
  exercising judgment about it. The judgment lives upstream in Stage 03's
  mapping and downstream in Stage 06's disposition. Note that light review
  here is only defensible *because* the model is written down and every score
  is emitted with its breakdown — an unexplained score would need heavy review.
- **Evidence:** a decision-log line recording the model's `artifact-version`,
  the calibration status, the sanity-check result, and the score distribution
  (how many items in each band's range) — enough for a later reviewer to tell
  whether this cycle's scores are comparable to another's.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Purely computational over Stages 01–03 outputs. No external queries, no new
  data entering the cycle.
- Comment content is read for timestamp extraction only (step 5). Comment
  *bodies* are not needed for scoring and should not be carried into this
  stage's outputs — they are the highest-risk content in a Jira export and
  there is no reason for them to travel further than Stage 01's screen.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
