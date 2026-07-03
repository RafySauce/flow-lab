---
id: decision-2026-07-03-source-input-taxonomy-expansion
title: "Decision Log — Source-Input Taxonomy Expanded to Eight Types (REC-05)"
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
  - "[[context-elicitation]]"
  - "[[decision-2026-07-03-input-taxonomy]]"
---

# Decision Log — 2026-07-03 — Source-Input Taxonomy Expanded

**What was decided:** broaden the HUB's "Common source inputs" taxonomy from
four types to eight, adding structured requirements documents (SOW/PRD/BRD),
incident/problem records, architecture/design artifacts, and a catch-all
"unclassified document" row — implementing drift-analysis recommendation
REC-05. **By whom:** agent, on operator instruction. **What it affects:**
`HUB.md` (taxonomy table + intro paragraph), Stage 01 (data-safety reminder
step, references the broadened list), Stage 02 (elicitation steering, step 1),
and `context-elicitation` (Method step 1, question-sequence steering).

## Relationship to the original taxonomy decision

This extends, not replaces,
`decision-log/2026-07-03-input-taxonomy.md`, which established the original
four types and their threading pattern (HUB table + Stage 01 screening +
Stage 02 steering, no new stage). The same pattern is reused for the four new
rows. That original log's "Flagged, not applied" section noted that steering
`context-elicitation`'s question sequence by input type was deferred to avoid
reopening a passed pre-gate — that skill revision has since happened (1.2,
per `decision-log/2026-07-03-input-taxonomy.md`'s own note being acted on),
so this pass edits the skill directly rather than deferring again.

## Decisions and alternatives

1. **Real intake documents don't fit the original four.** The drift analysis
   observed that architecture decision records, vendor SOWs, requirements
   spreadsheets, and Confluence pages arrive routinely and match none of the
   original rows cleanly. Rather than stretching an existing row's definition
   to cover them (which would blur its handling notes), three new specific
   rows were added plus a catch-all.
2. **Problem-shaped types get their own framing, not force-fit into
   "solution-shaped."** The original four rows are all request/solution-shaped
   by the taxonomy's own intro paragraph. Incident/problem records are
   already problem-shaped; the intro paragraph was revised to state this
   isn't true of all eight rows anymore, rather than silently letting the
   inaccurate generalization stand.
3. **Catch-all row is the safety net, not a shortcut.** "Unclassified
   document" gets the strictest data-safety screen and the full, unsteered
   question sequence — it exists so Stage 1/2 never have a document with
   nowhere to go, not to let ambiguous material skip screening.

## Assumption (operator to confirm or amend)

- **F1 — eight types are sufficient, not exhaustive.** This taxonomy is
  still a closed, named list plus a catch-all, not a claim that every
  possible intake document type has a dedicated row. Amendment path: if a
  ninth pattern recurs often enough to warrant its own handling notes,
  promote it out of the catch-all the same way this pass promoted three rows
  out of "unclassified."
