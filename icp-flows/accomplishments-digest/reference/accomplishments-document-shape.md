---
id: accomplishments-document-shape
title: "Accomplishments Document Shape — House Template"
type: template
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related: ["[[accomplishments-digest]]"]
---

# Accomplishments Document Shape — House Template

The output shape Stage 4 (Draft) synthesizes into and Stage 5 (Align &
Publish) edits against. Themes/initiatives are the top-level structure —
never "Jira" and "Confluence" as sections; the reader shouldn't have to know
which tool a given accomplishment came from.

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
work — anything Stage 3's collaboration-signal slice surfaced. Omit this
section outright (not "collaboration signal unavailable") if Stage 3
explicitly flagged the signal as unavailable at this instance's
activity-history depth — a visible empty section reads worse than no
section.

## Notes

Any coverage gaps carried forward from Stages 2–4 (e.g. "the migration
work spanned two quarters; only this period's slice is reflected here").
Omit this section if there are none — an empty caveats section undermines
the document's confidence.
```

## Authoring rules

- **Outcome first, ticket second.** "Shipped X, which cut Y by Z" beats "Closed
  14 tickets in the Foo epic." Ticket/doc counts are supporting evidence, never
  the headline.
- **Theme-grouped, not tool-grouped.** A reader should never need to know
  whether something came from Jira or Confluence.
- **Audience-matched length and detail.** A manager-only doc can stay terse; a
  promo-committee doc typically needs more supporting detail per theme —
  Stage 1's audience answer sets this, not a fixed template length.
- **Gaps stay visible.** A thin-coverage flag from Stage 2 or 3 becomes a
  Notes-section line, not a smoothed-over silence.
