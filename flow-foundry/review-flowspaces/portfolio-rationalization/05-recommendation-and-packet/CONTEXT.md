---
id: portfolio-rationalization-stage-05
title: "Stage 05 — Recommendation & Disposition Packet"
type: stage-context
stage: 5
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

# Stage 05 — Recommendation & Disposition Packet

> The step the source workbook did not have. Scoring ranks items; this stage
> turns a rank into something a named human can act on — a recommendation, the
> evidence behind it, and a question worth asking the person who owns the work.

## Inputs

| Input | Source | Required |
|---|---|---|
| Per-item close score | Stage 04 | Yes |
| Per-item dimension breakdown | Stage 04 | Yes |
| Corroboration count and firing dimensions | Stage 04 | Yes — banding cannot run without it |
| Ranked portfolio | Stage 04 | Yes |
| Per-item scoring caveats | Stage 04 | Yes |
| Calibration status declaration | Stage 04 | Yes |
| Per-item mapping record + `Needs objective review` bucket | Stage 03 | Yes |
| Portfolio profile, oldest-and-sparsest cross-cut, lens exploration record | Stage 02 | Yes |
| Assignee distribution (for routing) | Stage 02 | Yes |
| Parent key (merge-candidate context) | Stage 01 normalized set | No |
| Cycle scope record | Stage 01 | Yes |
| Band thresholds, corroboration rule, label semantics | `../reference/close-score-model.md` §4–5 | Yes |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-disposition-packet-builder)`

1. **Band each item** per `../reference/close-score-model.md` §4:
   `Close (recommended)` ≥95, `Strong close candidate` 80–94, `Review for
   closure` 65–79, `Keep / not closure-priority` <65.
2. **Apply the corroboration rule.** Any item banded `Close (recommended)` or
   `Strong close candidate` with **fewer than three firing dimensions is
   demoted to `Review for closure`**. The demotion and its cause go in the
   packet in plain language — "scored 88 but only 2 of 5 dimensions
   corroborate: reviewing, not recommending closure" — not in a footnote. This
   rule is the flow's governing principle made operational; a silent demotion
   teaches nobody anything.
3. **Build a disposition packet per item** in the three review-worthy bands
   (`Keep / not closure-priority` items get a line in the summary, not a
   packet). Each packet carries:
   - **Identity** — key, summary, status, assignee, age, last human touch.
   - **Recommendation** — the band, stated as a recommendation for review, never
     as a decision. `Close (recommended)` means *recommend closure to the
     owner*; nothing in this flow closes anything.
   - **Why — the signals that fired.** The named dimensions above midpoint with
     their points, in plain language: "434 days old, no update in 212 days,
     21% of fields populated, sits in Backlog, weak objective alignment." Not a
     bare number.
   - **The evidence trail** — the full dimension breakdown, the mapped
     objective area with its matched keywords, and the dictionary version used.
     This is what lets an owner disagree specifically rather than generally.
   - **Caveats** — every scoring caveat from Stage 04 that applies: degraded
     mapping, low-confidence staleness, unmapped status, unknown due date,
     and whether this cycle's objective mapping rests on an
     `inferred-and-confirmed` dictionary rather than an operator-authored
     one. A packet that hides its own weak evidence is worse than no packet.
   - **A suggested question for the owner** — one specific question this item's
     signal pattern actually raises. An old, sparse, unaligned Backlog item
     asks "is this still needed, and if so what changed since it was written?"
     An item in the `Needs objective review` bucket asks "which objective does
     this support, and does its wording say so?" A high-scoring item with a
     parent asks "should this merge into its parent?" Generic questions produce
     generic answers and waste the owner's time.
4. **Handle the `Needs objective review` bucket separately.** These items get
   packets framed as *alignment questions*, not closure questions, whatever
   their score. The bucket means a human must look, and covers three
   situations the mapping cannot distinguish — poorly worded real work, a
   dictionary gap, or genuine misalignment. A packet that presents an
   unmatched item as a closure candidate collapses that distinction and is the
   most likely way this flow produces a wrong recommendation.
5. **Identify merge candidates.** Where two high-scoring items share a parent,
   or their summaries and matched keywords overlap heavily, note them as
   possible merges in both packets. Merge is often the right disposition for
   work that is real but fragmented, and it is invisible to a per-item score.
6. **Route packets by assignee** into an outreach list — one section per
   assignee, their items ordered by score. Unassigned items route to the
   operator as their own section. This is what makes the pack usable: nobody
   reviews a 36-item ranked list, but everybody will look at their own four.
7. **Build the cycle summary** — total items reviewed, counts per band,
   demotion count, `Needs objective review` count, merge candidates
   identified, and the calibration status carried forward from Stage 04.
8. **Restate the framing at the top of the pack.** These are triage
   recommendations based on observable signals — age, staleness, field
   completion, objective alignment, workflow status. They do not prove an item
   lacks business value. They identify work whose *data* suggests it needs
   governance attention. Every reader of the pack sees this before they see a
   single recommendation.
9. **Present to the operator for review** before it goes to owners. The
   operator can pull items from the pack, adjust framing, or send it back to
   Stage 03 if the mapping distribution looks wrong.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Per-item disposition packet | Stage 06 — the artifact owners actually review | Identity, recommendation, signals that fired, evidence trail, caveats, suggested question |
| Demotion record | Stage 06; cycle decision log | Items demoted by the corroboration rule, with score and firing count |
| Assignee-routed outreach list | Stage 06 — drives who is asked what | One section per assignee (plus an operator section for unassigned), items score-ordered |
| Merge-candidate pairs | Stage 06 | Item pairs with the reason they look related |
| `Needs objective review` packets, alignment-framed | Stage 06 | As above, framed as alignment questions |
| Cycle summary | Stage 06; cycle decision log | Counts per band, demotions, needs-review, merge candidates, calibration status |
| Framing statement | Stage 06 — heads the pack | Text |

## Verify

Cross-stage trace: every item Stage 05 bands into `Close (recommended)` or
`Strong close candidate` has a corroboration count of 3 or more in Stage 04's
output, and every item with a count below 3 that scored ≥80 appears in the
demotion record. Check the arithmetic both directions — no undemoted item below
the threshold, no demoted item above it. The failure this catches is the
corroboration rule being computed in Stage 04 and then not enforced in Stage 05
— which produces exactly the outcome the flow exists to prevent: an old item
closed on age and one other signal. Running this check leaves a one-line result
in the cycle's decision log.

- [ ] Every item banded per the §4 thresholds
- [ ] Corroboration rule enforced; every sub-3 item scoring ≥80 demoted
- [ ] Every demotion stated in the packet in plain language, not footnoted
- [ ] Packets built for all three review-worthy bands
- [ ] Every packet carries signals-that-fired in plain language, the full
      evidence trail, and the dictionary version
- [ ] Every applicable Stage 04 caveat surfaced in its item's packet
- [ ] Every packet's suggested question is specific to that item's signal
      pattern, not generic
- [ ] `Needs objective review` items framed as alignment questions, not closure
      questions, regardless of score
- [ ] Merge candidates identified and noted in both packets of each pair
- [ ] Packets routed by assignee; unassigned routed to the operator
- [ ] Calibration status carried into the cycle summary
- [ ] Framing statement heads the pack, before any recommendation
- [ ] Operator reviewed the pack before it went to owners

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution against a written taxonomy. The
  banding is arithmetic and the packet shape is specified here; the judgment
  this stage's output *invites* belongs to Stage 06's owners. The one thing
  that would make this heavy — deciding what a recommendation means — is
  settled in `../reference/close-score-model.md` §4 rather than decided per
  cycle.
- **Evidence:** operator sign-off on the pack before distribution, plus a
  decision-log line recording the band counts, the demotion count, and the
  number of packets routed per assignee.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Packets pair assignee names with recommendations about their work. That
  combination is more sensitive than either part alone — treat the outreach
  list as the most sensitive artifact this flow produces, and distribute it
  per-assignee rather than circulating the whole pack broadly.
- The pack contains no closure actions and no Jira writes. It is a review
  document.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
