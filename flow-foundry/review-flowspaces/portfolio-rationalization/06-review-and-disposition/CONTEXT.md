---
id: portfolio-rationalization-stage-06
title: "Stage 06 — Review & Disposition Capture"
type: stage-context
stage: 6
review-intensity: heavy
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
  - "[[close-score-model]]"
---

# Stage 06 — Review & Disposition Capture

> The human loop, and the flow's terminal stage. Everything upstream produced a
> recommendation; this stage records what people actually decided — which is
> frequently not the same thing, and that difference is the most valuable
> output of the whole cycle.

## Inputs

| Input | Source | Required |
|---|---|---|
| Per-item disposition packets | Stage 05 | Yes |
| Assignee-routed outreach list | Stage 05 | Yes |
| `Needs objective review` packets, alignment-framed | Stage 05 | Yes |
| Merge-candidate pairs | Stage 05 | Yes |
| Demotion record | Stage 05 | Yes |
| Cycle summary and framing statement | Stage 05 | Yes |
| Operator overrides from mapping | Stage 03 | Yes |
| Dictionary version used this cycle | Stage 03 | Yes |
| Calibration status | Stage 04 | Yes |
| Disposition taxonomy (below) | This contract | Yes |

## Process

`Layer-3: inline (one-off — the disposition taxonomy and capture protocol below
are specific to this flowspace; no reusable skill was identified, because the
capture is a human conversation with a recording discipline attached rather
than an agent capability)`

1. **Distribute per assignee**, not broadly. Each owner receives their own
   section of the outreach list plus the framing statement. The whole pack —
   assignee names paired with recommendations about their work — is the most
   sensitive artifact this flow produces and does not need general circulation.
2. **Lead with the framing, every time.** Before any owner sees a
   recommendation: these are triage recommendations based on observable signals,
   they do not prove an item lacks value, and nothing has been or will be closed
   by this process. An owner who believes the system has already decided will
   defend rather than inform, and the cycle produces nothing useful.
3. **Walk each packet with its owner.** Present the recommendation, the signals
   that fired, the evidence trail, and the suggested question. The owner's
   knowledge beats every signal in the model — the model sees a ticket, the
   owner sees the work.
4. **Capture a disposition per reviewed item** from this taxonomy:

   | Disposition | Meaning |
   |---|---|
   | **Close** | The work is no longer needed, or was completed elsewhere without the ticket being updated |
   | **Merge** | Real work, but duplicated or fragmented — fold into another item (name it) |
   | **Rewrite** | Real, needed work whose ticket does not describe it adequately — the signals were reading bad documentation, not bad work |
   | **Re-scope** | Real work whose scope has drifted or grown stale — narrow, split, or redefine it |
   | **Keep** | Active, aligned, and correctly represented — no action |
   | **Defer** | A decision cannot be made this cycle; name what is blocking it and who owns unblocking |

   `Defer` exists because forcing a decision produces a bad one. But a deferred
   item carries a blocker and an owner, or it is not a deferral — it is an
   item that quietly rolls forward every cycle forever.
5. **Record the rationale with every disposition.** One or two sentences from
   the owner in their own words. This is the cycle's audit trail and the input
   to next cycle's calibration.
6. **Record disagreements explicitly.** Where the owner's disposition diverges
   from the recommendation — a `Close (recommended)` item the owner keeps, a
   `Keep` item the owner closes — capture the divergence and its reason as a
   first-class output. **Divergences are the single most valuable signal for
   improving the model**, and a cycle that records only outcomes and not
   disagreements has thrown away its own feedback.
7. **Collect dictionary-revision notes.** For every `Needs objective review`
   item, record which of the three cases it turned out to be: poorly worded
   work, a dictionary gap, or genuine misalignment. Dictionary-gap cases yield
   concrete term additions for the next cycle — this feedback path is the main
   reason the dictionary improves rather than staling.
8. **Collect model-calibration feedback.** Note where scores felt clearly wrong
   and in which direction: dimensions that over- or under-fired, band
   thresholds producing too much or too little review volume, statuses whose
   adjustment did not match how the team actually uses them.
9. **Confirm nothing was written to Jira.** State it plainly in the cycle
   record. Owners act on their own items outside this flow, on their own
   authority — that separation is the design, and stating it keeps the
   provenance of any subsequent Jira change unambiguous.
10. **Close the cycle.** Produce the cycle record: what was reviewed, what was
    decided, what diverged, what was deferred and why, what feedback was
    collected. Record it in the instance's `decision-log/`.
11. **Hand forward to the next cycle.** Dictionary-revision notes go to next
    cycle's Stage 03 step 2; calibration feedback goes to
    `../reference/close-score-model.md` §7; deferred items and their blockers
    go to next cycle's Stage 05 as prior context.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Per-item captured disposition + owner rationale | Cycle record; instance decision log | Item → disposition, rationale, deciding owner, date |
| Divergence record | Next cycle's Stage 04/05 calibration; instance decision log | Item → recommendation, actual disposition, owner's reason |
| Dictionary-revision notes | **Next cycle's Stage 03, step 2** | Per `Needs objective review` item: which of the three cases, and any concrete terms to add |
| Model-calibration feedback | `../reference/close-score-model.md` §7 review | Dimensions/thresholds that over- or under-fired, with the evidence |
| Deferred-item register | **Next cycle's Stage 05** | Item → blocker, owner of unblocking, cycle deferred |
| Merge decisions | Cycle record | Item pairs and which absorbed which |
| Cycle record | Instance `decision-log/` | Scope, counts, dispositions, divergences, deferrals, feedback, no-writes confirmation |

## Verify

Cross-stage trace: every item Stage 05 issued a packet for has a captured
disposition or an explicit deferral in Stage 06's output — none silently
dropped. Check additionally that every `Needs objective review` item from
Stage 03 has a dictionary-revision note classifying it into one of the three
cases, since that classification is the sole input to next cycle's dictionary
improvement. The failure this catches is the review conversation happening but
its results not being captured in a form the next cycle can consume — leaving
the dictionary and the model frozen at their initial guesses while the cycle
appears to have succeeded. Running this check leaves a one-line result in the
cycle's decision log.

- [ ] Pack distributed per assignee, not circulated broadly
- [ ] Framing statement led every owner conversation, before any recommendation
- [ ] Every packeted item has a captured disposition from the taxonomy, or an
      explicit deferral
- [ ] Every deferral names a blocker and an owner of unblocking
- [ ] Every disposition carries the owner's rationale in their own words
- [ ] Every divergence between recommendation and disposition recorded with its
      reason
- [ ] Every `Needs objective review` item classified into one of the three
      cases, with terms captured where the case was a dictionary gap
- [ ] Model-calibration feedback collected, with direction and evidence
- [ ] Merge decisions recorded, naming which item absorbed which
- [ ] No-Jira-writes confirmed and stated in the cycle record
- [ ] Cycle record written to the instance's `decision-log/`
- [ ] Dictionary notes, calibration feedback, and deferred items handed forward
      to their named next-cycle destinations

## Review

- **Reviewer:** operator, with the item owners as the substantive reviewers
- **Intensity:** heavy — the U-curve's terminal heavy stage, and the only point
  in the flow where a human with actual knowledge of the work meets the
  analysis. Every upstream signal is a proxy; this is where the proxies get
  tested. It is also the stage where the flow's feedback loops are either
  closed or lost, and a cycle that skips the capture discipline produces a
  review that felt productive and improved nothing.
- **Evidence:** the cycle record in the instance's `decision-log/` — dispositions
  with rationales, divergences, deferrals with blockers, and the feedback
  handed forward. An owner sign-off per assignee section confirms the
  conversation happened.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- This stage handles the flow's most sensitive combination: named individuals,
  their work, and recommendations about it. Per-assignee distribution (step 1)
  is a data-handling constraint, not a courtesy.
- Owner rationales are free text and may introduce content above `internal`
  (customer names, commercial detail, personnel context). Screen captured
  rationales before they enter the cycle record, and summarize rather than
  transcribe where a rationale carries sensitive specifics.
- **No writes to Jira, at this or any stage.** Owners act on their items
  outside this flow, on their own authority.
- Real portfolio content and cycle records live in the instance, never in this
  public design repo.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
