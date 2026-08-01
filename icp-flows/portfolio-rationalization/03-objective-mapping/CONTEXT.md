---
id: portfolio-rationalization-stage-03
title: "Stage 03 — Objective Mapping"
type: stage-context
stage: 3
review-intensity: heavy
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
  - "[[close-score-model]]"
---

# Stage 03 — Objective Mapping

## Inputs

| Input | Source | Required |
|---|---|---|
| Normalized item set | Stage 01 | Yes |
| Field-availability report (which text fields exist and how many items populate them) | Stage 01 | Yes |
| Degraded-signal list | Stage 01 | Yes |
| **The instance's objective dictionary** — objective areas, keyword sets with weights, confidence thresholds | Instance `reference/` folder, authored from `../reference/objective-dictionary-template.md` | Yes — operator-authored, or produced via confirmed inference this cycle (steps 3–5) |
| Dictionary structure, scoring, tie-break, and secondary-match rules | `../reference/objective-dictionary-template.md` | Yes |
| Confidence-to-points mapping this stage's output must feed | `../reference/close-score-model.md` §3.2 | Yes |
| Prior cycle's dictionary-revision notes | Stage 06 of the prior cycle; instance `decision-log/` | No |
| Component/Label/Epic Link population counts (for inference grouping) | Stage 01 field-availability report | No — required only if inference is attempted |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-objective-keyword-mapper)`

1. **Load and confirm the dictionary.** Read the instance's objective
   dictionary and echo back to the operator: the objective areas by name, the
   term count and weight distribution per area, the dictionary's
   `artifact-version`, and its last-updated date. **The operator confirms the
   dictionary is current for this planning cycle before any matching runs.** A
   dictionary that lags an objective-area change maps every item against
   strategy that no longer exists, and nothing downstream can detect it.
2. **Apply the prior cycle's revision notes** if any exist — terms Stage 06
   identified as missing when a human resolved a `Needs objective review` item.
   Present them as proposed additions; the operator accepts or rejects each.
   Never fold them in silently: a dictionary change alters scores, and the
   change has to be visible in the record.
3. **If no confirmed dictionary exists, attempt inference before halting.**
   Objective areas are still organizational strategy content, and this stage
   still does not invent them from nothing — but a candidate set of objective
   areas *can* be surfaced from the portfolio's own vocabulary and existing
   categorical structure, transparently, and handed to the operator to confirm
   or reject. Build an **inferred dictionary** per
   `../reference/objective-dictionary-template.md` §9: group items by whatever
   categorical fields the field-availability report shows populated for a
   meaningful share of the portfolio — Component, Labels, Epic Link —
   cross-referenced with term frequency in Summary and Description within each
   group. Every inferred area carries `provenance: inferred` and a weight
   ceiling of 2 — **no inferred term may ever claim the weight-3 designation**
   the template reserves for organizational vocabulary a human wrote down. If
   the field-availability report shows too little categorical structure to
   cluster on at all (below the evidence floor in §9), say so and skip
   straight to step 5.
4. **Present the inferred dictionary for confirmation, with full
   transparency.** Show every candidate area's name (drawn from its dominant
   Component/Label/Epic value, never invented), its inferred keyword set with
   weights and the item-group evidence behind each term, and which items
   clustered nowhere. This is the same "transparent, arguable, owned" bar the
   template sets for a real dictionary (§1) — the operator must be able to
   point at the same evidence an authored dictionary's owner would point at.
   **The operator does one of three things:** confirms it as-is, confirms it
   with edits (rename an area, drop a spurious term, merge two candidates), or
   rejects it. A confirmed inferred dictionary is written to the instance's
   `reference/` folder like any other — its own `artifact-version`, the
   operator as confirming owner, `provenance: inferred` — and from this point
   in the cycle it *is* this cycle's dictionary, not a proxy for one.
5. **If the operator cannot confirm an inferred dictionary and has no
   dictionary of their own, do not halt — pivot.** A flat halt produces
   nothing, and the portfolio still has a shape worth reporting without
   objective alignment. Stop here and route the cycle to
   `../03p-current-state-analysis/CONTEXT.md` instead of continuing to
   Stage 04. State the reason plainly, verbatim, in the cycle record: which of
   "no categorical structure to infer from," "inferred dictionary presented
   but not confirmed," or "operator declined to pursue either path" applies.
   This is not this stage degrading — it is a different, complete deliverable
   with its own contract, not a partial run of this one.
6. **Declare the searchable field set for this cycle.** From the
   field-availability report, state which of the seven mapping fields (Summary,
   Description, Business Outcome, Scope, Acceptance Criteria, Dependencies,
   Risks) actually exist and are populated. If Business Outcome is absent, say
   so here — it is the highest-value mapping field and every mapping this cycle
   is weaker without it.
7. **Match each item against every area.** For each item, for each objective
   area: find the distinct terms that match, sum their weights, and record which
   field each hit came from. Distinct means a term appearing six times counts
   once — repetition is a writing style, not evidence.
8. **Assign confidence** per the dictionary's thresholds (default: High ≥ 8
   *and* at least one weight-3 term; Medium 4–7; Low/weak 1–3; `Needs objective
   review` 0). A score of 8 assembled entirely from weight-1 generic terms caps
   at Medium — that is a coincidence, not a match. If this cycle's dictionary
   carries `provenance: inferred`, no term in it can be weight 3 (§9 of the
   template) — High confidence is therefore structurally unreachable for an
   inferred dictionary, not merely discouraged.
9. **Assign the primary area** — highest-scoring. Record the **secondary
   possible match** when the runner-up scores ≥ 60% of the primary. On a true
   tie between two areas both above the Low threshold, **flag for human
   assignment rather than auto-assigning**; this stage carries heavy review
   precisely so these get looked at.
10. **Bucket the unmatched as `Needs objective review`** — items where no term in
    any area matched. State explicitly, in the output itself, that this means
    "a human must look at this" and covers three distinct situations the mapping
    cannot tell apart: poorly worded real work, a gap in the dictionary, or
    genuinely unaligned work. It is **not** a closure verdict and must never be
    presented as one.
11. **Degrade, don't fail, on thin items.** An item carrying only a Summary can
    still map — at correspondingly lower confidence, flagged as a Summary-only
    mapping in its output row. Do not promote a Summary-only match to High
    confidence regardless of score.
12. **Present the mapping distribution for operator review** — how many items
    landed in each area, how many in each confidence band, how many need
    objective review, how many carry secondary matches, how many are flagged
    for human assignment. A distribution that looks wrong (everything in one
    area, or half the portfolio needing review) is a dictionary problem, and
    this is where it gets caught.
13. **Operator reviews and adjudicates.** The operator resolves the
    human-assignment flags, spot-checks mappings by reading the matched-keyword
    evidence, and overrides any mapping they judge wrong. **Every override is
    recorded with its reason** — overrides are the richest source of dictionary
    improvements for the next cycle.
14. **Confirm before advancing.** Obtain explicit operator sign-off on the
    mapping set, including the adjudicated flags and any overrides.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Per-item mapping record | Stage 04 (unrelatedness dimension), Stage 05 (packet evidence) | Key → mapped area, confidence band, score, matched keywords with source field, secondary match (area + score) or none |
| `Needs objective review` bucket | Stages 04, 05, 06 | Item list with the explicit not-a-closure-verdict framing attached |
| Human-assignment flags and their adjudications | Stage 05; cycle decision log | Item → operator's assigned area + reason |
| Operator overrides | Stage 06; cycle decision log; next cycle's dictionary review | Item → original mapping, override, reason |
| Mapping distribution summary | Stage 05, Stage 06 | Counts per area, per confidence band, secondary-match count |
| Dictionary version used this cycle | Stage 04, Stage 06; cycle decision log | Dictionary id + `artifact-version` + last-updated date + provenance (`operator-authored` / `inferred-and-confirmed`) |
| Summary-only / degraded mapping flags | Stage 04, Stage 05 | Item list with the reason each is degraded |

## Verify

Cross-stage trace: every item in Stage 01's normalized item set appears exactly
once in Stage 03's mapping record — mapped to an area or bucketed as `Needs
objective review`, never both and never neither. Check additionally that every
confidence band Stage 03 emits has a corresponding row in
`../reference/close-score-model.md` §3.2's confidence-to-points table, and that
the dictionary's thresholds and that table agree. The failure this catches is
Stage 04 receiving a confidence value it has no points mapping for and silently
scoring it as zero unrelatedness — turning an unmappable item into a
well-aligned one. Running this check leaves a one-line result in the cycle's
decision log. This check applies only when Stage 03 reaches a
confirmed-dictionary resolution and proceeds to Stage 04; a cycle that pivots
to `../03p-current-state-analysis/` is checked under that stage's own Verify
instead. Additionally, if this cycle's dictionary carries `provenance:
inferred`, confirm no item's confidence band is recorded as High — a High
band anywhere in an inferred-and-confirmed cycle is a build defect, not a
judgment call.

- [ ] Dictionary loaded, its version and last-updated date echoed, and operator
      confirmed it is current for this planning cycle **before** matching ran
- [ ] Prior-cycle revision notes presented as proposals and individually
      accepted or rejected — never folded in silently
- [ ] Inference attempted before any halt when no dictionary was confirmed,
      with every inferred term capped at weight ≤2
- [ ] Inferred dictionary presented for operator confirmation with full
      evidence before use
- [ ] If inference could not be confirmed and no dictionary exists, the cycle
      routed to Current State Analysis rather than halting
- [ ] Dictionary provenance recorded and carried to Stage 04
- [ ] Searchable field set for this cycle declared, with Business Outcome's
      absence called out if applicable
- [ ] Distinct-term counting applied (repeats counted once)
- [ ] Every match records the source field of each keyword hit
- [ ] High confidence requires a weight-3 term, not score alone
- [ ] Secondary matches recorded at the ≥60% threshold
- [ ] True ties flagged for human assignment, not auto-assigned
- [ ] `Needs objective review` bucket carries the explicit not-a-closure-verdict
      framing in the output itself
- [ ] Summary-only mappings flagged and capped below High confidence
- [ ] Mapping distribution presented for review before advancing
- [ ] Every operator override recorded with its reason
- [ ] Operator signed off on the mapping set

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — deviating from the U-curve default with cause. This is
  the highest-judgment content in the flow and the only input that encodes
  organizational strategy rather than observable Jira facts. It feeds 40 of the
  model's ~100 points, and a mis-mapped item arrives at Stage 04 as a
  weak-alignment signal worth up to 40 closure points that no downstream stage
  can distinguish from genuine misalignment. The dictionary is also the one
  artifact that goes stale between planning cycles without any visible symptom.
- **Evidence:** operator sign-off on the mapping set, plus decision-log entries
  recording the dictionary version used, every human-assignment adjudication,
  and every override with its reason.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- The objective dictionary itself may carry a higher classification than the
  portfolio data — objective-area statements are often `internal` or
  `confidential` strategy content. Confirm the dictionary's own `data-class` at
  instantiation and route this stage to engines sanctioned for **that** class,
  not merely for the item set's class.
- The dictionary lives in the instance, never in this public repo
  (`AGENTS.md` rule 8). This design copy carries only the mold.
- An inferred dictionary is built entirely from this cycle's own portfolio
  text and existing tags — it introduces no new data-class question the item
  set doesn't already carry, unlike an operator-authored dictionary which may
  sit at a higher classification. Route an inferred dictionary at the item
  set's own ceiling.
- This stage performs no external queries — it reads Stage 01's normalized set
  and the instance's dictionary.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
