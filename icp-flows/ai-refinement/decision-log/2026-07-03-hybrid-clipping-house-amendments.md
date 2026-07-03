---
id: decision-2026-07-03-hybrid-clipping-house-amendments
title: "Decision Log — House Amendments Backported Into ai-refinement-hybrid.md"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
---

# Decision Log — 2026-07-03 — House Amendments Backported Into the Clipping

**What was decided:** append five house-proven rules (due-date elicitation,
post-commit transition offer, parent-mapping confirmation, format-translation
gate, communication_style enforcement) directly into
`reference/ai-refinement-hybrid.md`, as a new `## House Amendments` section
below the unchanged source material, rather than in a separate addendum
document. **By whom:** agent, on operator instruction, as part of implementing
the drift-analysis recommendations (REC-07). **What it affects:**
`reference/ai-refinement-hybrid.md` (1.0 → 1.1, `truth-level: claimed` →
`to-review`), and every stage/skill that now cites a specific amendment by
name (Stages 01, 04, 05, 06; `context-elicitation`, `field-refinement-cadence`,
`jira-commit`).

## Reconciling this against prior precedent

`decision-log/2026-07-03-work-item-schema-extension.md` (decision 1)
deliberately kept the schema extension in a separate registry file rather
than editing this same clipping, reasoning that "editing it would destroy its
evidentiary value." This decision reverses that instinct for a narrower
class of change: the five rules being backported here are not new fields or
new scope — they are behavior the flowspace already proved necessary through
on-engine operation (four from NEADD-1827) and a drift analysis (the fifth,
communication_style). The operator explicitly chose "edit the clipping
directly" over a separate addendum-only file when asked. To preserve the
evidentiary distinction the prior precedent was protecting, the amendments
are appended below the original text, under their own heading, each labeled
house-authored with its origin — the unmodified source material remains
diffable against the real external document; only the new section is house
content.

## Truth-level change

`ai-refinement-hybrid.md` moves from `claimed` to `to-review`. The source
material itself is still unreviewed foreign content (`claimed` would still
be accurate for that portion alone), but the file as a whole now carries
substantive house-authored content pending the same operator sign-off as the
rest of the flowspace — `to-review` is the more honest single status for the
combined file, matching how `work-item-schemas.md` already handles mixed
clipping-plus-house-extension provenance. **This reverses the file's
truth-level for the first time since ingest — flagged here explicitly for
the operator to confirm or override.**

## Assumption (operator to confirm or amend)

- **D1 — amendment-vs-clipping boundary is durable.** This assumes future
  edits to this file will maintain the same discipline: new source material
  (if the real external document is ever re-ingested) replaces the top
  section; new house-proven rules get appended to the amendments section.
  Amendment path: if this boundary blurs in practice, split the amendments
  into their own file after all, following the original schema-extension
  precedent.
