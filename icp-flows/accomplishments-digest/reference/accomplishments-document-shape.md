---
id: accomplishments-document-shape
title: "Accomplishments Document Shape — House Template"
type: template
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related: ["[[accomplishments-digest]]"]
---

# Accomplishments Document Shape — House Template

The output shape Stage 7 (Draft) synthesizes into and Stage 8 (Align &
Publish) edits against. Themes/initiatives are the top-level structure —
never one section per source tool (Jira, Confluence, Microsoft 365,
ServiceNow); the reader shouldn't have to know which tool a given
accomplishment came from.

```markdown
# <Engineer Name> — Accomplishments, <Review Period>

_Prepared for: <audience>. Period: <start date> – <end date>._

## Summary

Two to four sentences in the engineer's own words: what they'd want a
manager to take away if they read nothing else.

## <Theme / Initiative 1>

One-sentence outcome framing, then 2–4 supporting bullets. Self-identified
top items (from Stage 1) get first placement or visible emphasis within
their theme, not folded in anonymously among tracker-sourced items.

- <outcome-framed bullet, ticket/doc reference kept out of the reader-facing
  line but traceable in the source digest>
- <bullet>

## <Theme / Initiative 2>

(repeat shape)

## Collaboration & scope beyond individual tickets

Cross-team work, mentoring, reviews given, docs that changed how others
work, and recognition from colleagues and other teams (paraphrased by
default: "recognized by the network team for the cutover"). This draws on
Stage 3's collaboration signal and Stage 4's recognition evidence. Omit this
section outright (not "collaboration signal unavailable") if Stage 3
explicitly flagged the signal as unavailable at this instance's
activity-history depth and Stage 4 found no recognition — a visible empty
section reads worse than no section.

## Operational load

Two to four sentences or bullets putting run-the-business work in context:
what kinds of records were resolved (incidents, change tasks, catalog tasks,
problem tasks), the priority mix, median time to resolve, and any problem
tasks that led to a permanent fix. Context, not a scoreboard. Omit this
section if ServiceNow was skipped or out of scope.

## Notes

Any coverage gaps carried forward from Stages 2–7, including sources that
were skipped or unreachable (e.g. "the migration
work spanned two quarters; only this period's slice is reflected here").
Omit this section if there are none — an empty caveats section undermines
the document's confidence.
```

## Authoring rules

- **Outcome first, ticket second.** "Shipped X, which cut Y by Z" beats "Closed
  14 tickets in the Foo epic." Ticket/doc counts are supporting evidence, never
  the headline.
- **Theme-grouped, not tool-grouped.** A reader should never need to know
  which tool something came from. Operational load is the one
  non-theme section, because volume needs its context in one place.
- **Volume is context, never a ranking.** No bare counts as headlines, and no
  comparison with peers or a team average.
- **Other people's words are paraphrased.** A verbatim quote appears only
  when the engineer chose it at Stage 6 or 8.
- **Audience-matched length and detail.** A manager-only doc can stay terse; a
  promo-committee doc typically needs more supporting detail per theme —
  Stage 1's audience answer sets this, not a fixed template length.
- **Gaps stay visible.** A thin-coverage flag or a skipped source from
  Stages 2–5 becomes a Notes-section line, not a smoothed-over silence.
