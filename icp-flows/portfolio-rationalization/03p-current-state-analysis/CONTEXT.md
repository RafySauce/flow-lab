---
id: portfolio-rationalization-stage-03p
title: "Stage 03P — Current State Analysis (Pivot)"
type: stage-context
stage: "3p"
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-29
updated: 2026-07-29
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[objective-dictionary-template]]"
  - "[[portfolio-rationalization-stage-03]]"
---

# Stage 03P — Current State Analysis (Pivot)

> Not a numbered stage in the main 1–6 sequence — a documented alternate
> terminal, reached only when Stage 03 ends without a confirmed dictionary
> (`03-objective-mapping/CONTEXT.md`, steps 3–5). A cycle either continues
> 3 → 4 → 5 → 6, or ends here. Never both.
>
> **Provenance-spec deviation, flagged not silently resolved:**
> `methodology/provenance-spec.md` requires `stage` to be an integer on
> `type: stage-context`. This stage's real position is "3-and-a-branch," not
> an integer, so this contract carries `stage: "3p"` as a deliberate
> exception. Recorded for the operator to ratify as a one-off, or resolve
> with a small spec amendment (e.g. allowing a string `stage` id for branch
> stages) — see the decision log
> (`flow-foundry/decision-log/2026-07-29-portfolio-rationalization-dictionary-inference-and-pivot.md`).

## Inputs

| Input | Source | Required |
|---|---|---|
| Normalized item set | Stage 01 | Yes |
| Field-availability report | Stage 01 | Yes |
| Degraded-signal list | Stage 01 | Yes |
| Cycle scope record | Stage 01 | Yes |
| Portfolio profile — status, assignee, priority, due-date distributions | Stage 02 | Yes |
| Age ranking (all items) + oldest-10 detail | Stage 02 | Yes |
| Per-item field-completion percentage with absolute counts | Stage 02 | Yes |
| Oldest-and-sparsest cross-cut | Stage 02 | Yes |
| Lens exploration record | Stage 02 | No |
| The pivot decision and its stated cause | Stage 03, step 5 | Yes |
| Rejected/unconfirmed candidate dictionary, if inference was attempted | Stage 03, steps 3–4 | No — present only if inference was attempted |

## Process

`Layer-3: inline (one-off — every section below is either a verbatim
carry-forward of Stage 01/02 output or a count aggregation; no matching or
scoring capability is exercised, so no skill gap exists here the way
Stages 01–05 each flagged one)`

1. **State the framing before anything else.** No objective dictionary —
   inferred or operator-authored — was confirmed this cycle, so the
   close-score model's objective-unrelatedness dimension (40 of ~100 points)
   cannot be computed responsibly. This is a *description* of the
   backlog's shape, not a judgment about what to do with it.
2. **Record the pivot's cause verbatim** — exactly which of Stage 03's three
   outcomes applies: no categorical structure to infer from, an inferred
   dictionary presented but not confirmed, or the operator declined to
   pursue either path.
3. **Carry the portfolio shape forward unchanged** — Stage 02's
   status/assignee/priority/due-date distributions, not recomputed.
4. **Carry age and staleness forward**, computing staleness independently
   (days since `Updated`, preferring the most recent human touch where
   comment timestamps are available) — these are observable facts with no
   alignment dependency, so they need no dictionary to be reported honestly.
5. **Carry field completion forward** — per-item percentage, absolute
   counts, and the oldest-and-sparsest cross-cut, taken directly from
   Stage 02's figures rather than recomputed.
6. **Build the descriptive structural-grouping section** — item counts per
   Component, Label, and Epic Link, with an explicit statement beside it
   that **these are not objective areas, carry no confidence band, and were
   never scored.** If Stage 03 produced an inferred-but-unconfirmed
   dictionary, its clusters may be reused here, but every weight, score, and
   confidence label must be stripped first — only the grouping and its item
   counts carry forward.
7. **State what this document does not do.** No close score. No
   recommendation band. No per-item disposition packet. No assignee-routed
   outreach list. No dictionary. Say this plainly, near the top, before any
   grouping is shown — a reader who skims past the framing statement should
   still hit this before mistaking a grouping for a recommendation.
8. **State the path back, once.** Authoring a dictionary, or successfully
   confirming an inferred one, before the next cycle is what unlocks
   Stages 04–06. This document doesn't shortcut that — it names it as the
   next step and stops.
9. **Present to the operator for sign-off** before the cycle closes.
10. **Confirm nothing was written to Jira and close the cycle** in the
    instance's `decision-log/`. **This ends the cycle standalone — it does
    not hand off into Stage 06.** Stage 06's disposition taxonomy
    (Close/Merge/Rewrite/Re-scope/Keep/Defer) presumes a recommendation for
    an owner to react to, and this stage deliberately produces none; forcing
    a handoff would either smuggle an implicit closure question back in
    through an owner conversation or produce an empty pass against inputs
    Stage 06 doesn't have. This stage's own steps 9–10 reuse Stage 06's
    sign-off and no-Jira-writes discipline directly, as its own terminal
    step, instead.

## Outputs

| Output | Format |
|---|---|
| Framing statement | Text, heads the document — why no score is possible this cycle |
| Pivot-cause record | Text — which of Stage 03's three outcomes applied, verbatim |
| Portfolio shape | Carried from Stage 02, unchanged |
| Age & staleness profile | Age ranking + oldest-10; independent staleness figures, no score attached |
| Field-completion profile | Per-item %, absolute counts, oldest-and-sparsest cross-cut |
| Descriptive structural groupings | Item counts per Component/Label/Epic, explicitly flagged as non-objective and non-scored |
| Candidate-dictionary residue (conditional) | The rejected/unconfirmed inferred dictionary plus the operator's stated reason, carried forward as raw material for next cycle's authoring effort |
| Data-quality flags | Degraded-signal list, carried from Stage 01 |
| "What this analysis does not do" | Text |
| Suggested next step | Text — author or confirm a dictionary before the next cycle |
| Operator sign-off record | Cycle decision log |
| No-Jira-writes confirmation | Text, cycle decision log |

## Verify

Cross-stage trace: every item in Stage 01's normalized item set appears in at
least one of the portfolio-shape, age/staleness, or field-completion
sections — the same no-item-silently-drops discipline Stage 02's own Verify
applies. Additionally, run a content check unique to this stage's purpose:
confirm the document contains no close score, no recommendation band, and no
phrase presenting a grouping as an alignment judgment. This is a directly
checkable property, and it is what structurally enforces "descriptive, not
judgment-bearing" rather than leaving it to the reader's trust. Running this
check leaves a one-line result in the cycle's decision log.

- [ ] Framing statement states plainly, up front, why no score is possible
      this cycle
- [ ] Pivot-cause record names exactly which of Stage 03's three outcomes
      applied
- [ ] Portfolio shape, age/staleness, and field-completion figures carried
      from Stage 01/02 without recomputation
- [ ] Every item from Stage 01's normalized set appears in at least one
      section
- [ ] Structural groupings explicitly flagged as non-objective and
      non-scored, with no weight/score/confidence label carried over from
      any unconfirmed inferred dictionary
- [ ] "What this analysis does not do" stated before any grouping is shown
- [ ] No close score, band, packet, or outreach list appears anywhere in the
      document
- [ ] Suggested next step names authoring or confirming a dictionary
- [ ] Operator signed off before the cycle closed
- [ ] No-Jira-writes confirmed and stated in the cycle record
- [ ] Cycle recorded in the instance's `decision-log/`; no handoff to
      Stage 06 attempted

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the cycle's terminal artifact in the
  absence of the flow's primary judgment input, and it is also where a
  reviewer checks the pivot itself was warranted: that Stage 03 didn't route
  here when a usable dictionary actually existed. A stage that closes a
  cycle without the flow's central judgment mechanism earns the same
  attention as the stages that open and close a normal cycle.
- **Evidence:** operator sign-off, plus the pivot-cause record and cycle
  summary in the instance's `decision-log/`.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- This stage classifies strictly less than Stage 03 does, since no
  dictionary of any kind — operator-authored or inferred — is in scope
  here.
- This stage performs no external queries — it reads Stage 01 and Stage 02
  outputs, and Stage 03's pivot record, only.
- **No writes to Jira**, consistent with every other stage in this
  flowspace.
- A handoff into this stage from an engine outside this boundary is invalid
  — stop and re-route.
