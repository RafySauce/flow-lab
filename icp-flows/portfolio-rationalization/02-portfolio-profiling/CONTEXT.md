---
id: portfolio-rationalization-stage-02
title: "Stage 02 — Portfolio Profiling"
type: stage-context
stage: 2
review-intensity: light
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-08-01
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[export-and-field-requirements]]"
  - "[[work-item-schemas]]"
---

# Stage 02 — Portfolio Profiling

> The diagnostic layer. Its job is **not** to decide what should be closed —
> it is to show the operator what they are looking at, from several angles,
> before anything is judged. Everything in this contract is arranged to keep
> that ordering intact.

## Inputs

| Input | Source | Required |
|---|---|---|
| Normalized item set | Stage 01 | Yes |
| Confirmed item count | Stage 01 | Yes |
| Completion denominator (this cycle's column count) | Stage 01 | Yes |
| Field-availability report | Stage 01 | Yes |
| Degraded-signal list | Stage 01 | Yes |
| Cycle scope record | Stage 01 | Yes |
| Denominator rule and degraded-signal handling | `../reference/export-and-field-requirements.md` §3–4 | Yes |
| Connected-space discovery outcome | Stage 01 | Yes |
| Connected-space hierarchy context, if Stage 01 resolved any candidates | Stage 01 | No — present only when discovery resolved candidates |
| Work item type hierarchy (Portfolio Epic → Solution Epic → Feature → Story/Task/Spike/Bug) | `../../ai-refinement/reference/work-item-schemas.md` | Yes — only for the hierarchy view; the rest of this stage does not depend on it |
| Prior cycle's profile, if this is not the first cycle | Instance `decision-log/` | No |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-portfolio-profiler)`

1. **State the frame.** Open with the portfolio's size and the denominator:
   "N items across M columns, scope `<project/filter>`." Both numbers, always
   together — a completion percentage without its denominator hides the thing
   that gives it meaning.
2. **Distribution by status.** Count items per status, and per Status Category
   where available. Report counts, not percentages alone: "14 In Progress, 12
   Backlog, 5 Analyzing, 3 Review, 1 On Hold, 1 Ready" is legible; "39%
   In Progress" is not.
3. **Distribution by assignee.** Count items per assignee, and report the
   unassigned count separately and explicitly — unassigned work is a finding,
   not a blank row. **Output a distribution, never a named ranking.** This
   stage profiles workload; it does not evaluate people, and a sorted list of
   humans by ticket count invites exactly that reading.
4. **Distribution by priority.** Count per priority level. A portfolio where
   every item carries the same priority (all Medium, say) is itself a finding —
   it means priority is not being used as a signal and no downstream stage
   should treat it as one. Say so when it happens.
5. **Due-date categorization.** Bucket into: overdue, due within 30 days, future
   (beyond 30 days), and no due date. Report all four counts. Where Due date is
   absent from the source entirely, report the category as unavailable rather
   than reporting every item as "no due date" — those are different facts.
6. **Age ranking.** Order items oldest to newest by `Created`, with the age in
   days. Surface the oldest 10 with key, summary, and age.
7. **Field completion per item.** Compute populated-fields ÷ denominator per
   item, per the rule in `../reference/export-and-field-requirements.md` §4.
   Report every percentage with its absolute counts (`44 of 216 — 20.4%`).
   Same denominator for every item in the cycle.
8. **The oldest-and-sparsest cross-cut.** Intersect the age ranking with the
   completion ranking: items that are both old and thinly populated. This is
   the cross-cut that matters most downstream — it is the shape that
   corroborates rather than any single ranking — and it is the one view a
   status-by-status read will never surface.
9. **Build the hierarchy view — Portfolio Epic → Solution Epic → Feature →
   child.** Using `Issue Type` and `Parent key` from the normalized item set
   — plus any connected-space hierarchy context Stage 01 resolved — trace
   every item's parent chain against the hierarchy
   `../../ai-refinement/reference/work-item-schemas.md` defines (Portfolio
   Epic → Solution Epic → Feature → Story/Task/Spike/Bug).
   - **Render a Mermaid `flowchart TD`**, one node per item, labeled with its
     **Summary** — this is a hierarchy of what the work *is*, not a bare key
     list. Truncate labels past ~60 characters for legibility and say so
     where the diagram is presented; the full Summary always stays available
     in an accompanying key/summary/type/parent table, never only inside the
     diagram. Edges run parent → child. Give any node Stage 01 resolved from
     a connected space a visibly distinct style (a separate `classDef`, per
     `flow-foundry/references/flow-diagram-guide.md`'s palette convention),
     so the operator can tell primary-scope work from imported hierarchy
     context at a glance.
   - **Call out orphans — two counts, never folded into one.** Per
     `work-item-schemas.md`, every refinable type except Portfolio Epic
     expects a parent. Report, separately: items with **no `Parent key`
     populated at all**, and items whose `Parent key` **is populated but does
     not resolve** to any item in the primary set or the connected-space
     context — a dangling reference, a different fact from "no parent
     stated" and one that points at a different problem (a broken link
     versus one never made). Break both counts out by `Issue Type` and list
     the affected items (key + summary) so the operator can act on them.
   - **Degrade explicitly — do not fabricate a hierarchy from partial data.**
     If `Issue Type` or `Parent key` is absent from the source entirely,
     state that the hierarchy view cannot be built, name the missing field,
     and skip the diagram — the same discipline step 11 (below) applies
     everywhere else in this stage.
   - This is a **first-class output**, produced whenever the fields support
     it — like the oldest-and-sparsest cross-cut, not something the operator
     has to request as a lens.
10. **Offer the exploration lenses, and stop.** Present the angles available for
    deeper inspection — status, assignee workload, due dates and risk, priority,
    labels, custom fields, or something else — and ask which the operator wants
    to explore first. **Do not proceed to Stage 03 until the operator has had
    this offer.** Jumping from distributions straight to objective mapping is
    the single most likely way this flow degrades into a scoring machine that
    nobody trusts, because nobody looked at the data first.
11. **Explore the chosen lens** in whatever depth the operator asks, and repeat
    the offer. The operator ends the exploration and advances, not the agent.
12. **Note degraded signals in the profile itself**, not only in a footnote:
    if Due date is absent, the due-date section says so where the counts would
    be; if Assignee is absent, the workload section says so; if the hierarchy
    view could not be built, step 9 already said so in place. A missing
    section reads as "nothing to report," which is a different claim.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Portfolio profile — status, assignee, priority, and due-date distributions | Stage 05 (packet context), Stage 06 (review framing) | Counts per category, with unavailable categories marked |
| Age ranking (all items) + oldest-10 detail | Stage 04 (sanity-check against age scores), Stage 05 | Ordered list: key, summary, days since Created |
| Per-item field-completion percentage with absolute counts | Stage 04 (completion dimension input) | Key → `X of Y — Z%` |
| Oldest-and-sparsest cross-cut | Stage 05 (packet context), Stage 06 | Item list with both rankings shown |
| Hierarchy view — Portfolio Epic → Solution Epic → Feature → child, by summary, plus orphan and dangling-reference counts by type | Stage 05 (packet context), Stage 06 (review framing) | Mermaid `flowchart TD` block + companion key/summary/type/parent table + two orphan-family counts broken out by `Issue Type` |
| Lens exploration record — which lenses the operator examined and what they observed | Stage 06; cycle decision log | Text |
| Degraded-signal annotations, in-place in the profile | Stages 03, 04, 05 | Inline notes per affected section |

## Verify

Cross-stage trace: the item count Stage 02 profiles equals the confirmed item
count Stage 01 emitted, and every status distribution's category sum equals
that same total. Check that the four due-date buckets (overdue, ≤30 days,
future, none) also sum to the total, with any item excluded for an unavailable
Due date field counted explicitly rather than dropped. The failure this catches
is items vanishing between stages — an item with a null status or an unparseable
date silently falling out of every bucket, so the distributions look complete
and describe a smaller portfolio than the one under review. Running this check
leaves a one-line result in the cycle's decision log. The hierarchy view's
orphan and dangling-reference accounting is checked separately, against the
same normalized set plus any resolved connected-space context — it does not
feed this trace and a hierarchy-view gap cannot by itself explain a count
mismatch here.

- [ ] Item count and denominator stated together, up front
- [ ] Status distribution counts sum to the confirmed item count
- [ ] Assignee distribution reports unassigned separately; output is a
      distribution, not a named ranking
- [ ] Priority distribution reported, with single-value uniformity called out
      as a finding if present
- [ ] All four due-date buckets reported and summing to the total, or the
      category marked unavailable
- [ ] Age ranking covers every item; oldest 10 shown with key, summary, age
- [ ] Every completion percentage carries its absolute counts
- [ ] Same denominator applied to every item
- [ ] Oldest-and-sparsest cross-cut produced
- [ ] Hierarchy view built from `Issue Type` and `Parent key` when both are
      available; explicitly marked unavailable, naming the missing field,
      when they are not
- [ ] Every item in the primary set (and any resolved connected-space
      context) is classified as exactly one of: has a resolving parent, no
      parent stated (orphan), or parent stated but unresolved (dangling) —
      none silently dropped from the accounting
- [ ] Orphan and dangling-reference counts reported separately and broken out
      by `Issue Type`
- [ ] Diagram nodes labeled with Summary, truncated past the stated limit
      with full text in the companion table; connected-space nodes visually
      distinguished from primary-scope nodes
- [ ] The exploration-lens offer was made and the operator responded **before**
      advancing to Stage 03
- [ ] Degraded signals annotated in-place in the affected profile sections, not
      only footnoted

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution. The counting is mechanical and
  checkable by arithmetic; the judgment in this stage belongs to the operator
  reading the profile, not to the agent producing it.
- **Evidence:** the lens exploration record — which lenses were examined and
  what the operator observed — as a decision-log line. An advance to Stage 03
  with no lens record means step 10 was skipped, which is a review failure
  even if every number is right. The hierarchy view's orphan and
  dangling-reference counts travel in the same decision-log line when the
  view was built.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Assignee names are handled here for workload distribution. They stay at
  `internal`, and the distribution-not-ranking rule in step 3 is a data-handling
  constraint, not a presentation preference.
- This stage performs no external queries — it reads Stage 01's normalized set,
  and any connected-space hierarchy context Stage 01 already resolved, only.
  No new data enters the cycle here; this stage does not itself reach outside
  the primary scope.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
