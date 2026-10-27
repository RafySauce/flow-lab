---
id: decision-2026-10-27-accomplishments-correlator-skill-build
title: "Decision Log — accomplishments-correlator Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-correlator]]"
  - "[[sp-accomplishments-correlator]]"
  - "[[accomplishments-digest]]"
---

# Decision Log — 2026-10-27 — accomplishments-correlator Skill Build

**What was decided:** build `accomplishments-correlator` from its primer brief
and stage it in `review-skills/accomplishments-correlator/` at
`truth-level: to-review`. **By whom:** agent, on the operator's explicit
go-ahead to build the five accomplishments-digest 2.0 skill briefs in
parallel. **Triage:** skill-primer-brief, clean path; the brief's decided
intent was transcribed, not re-opened.

## Build decisions

1. **Heavy confirmation is part of the contract.** Method step 6 requires an
   explicit confirmation of the full map and says silence or a skim is not
   confirmation, mirroring Stage 6's `heavy` review intensity (D6).
2. **Assigned-but-not-resolved ServiceNow list is not counted as evidence.**
   Stage 5 emits it as a separate list; it is carried whole as context so the
   coverage count (count in = count out) stays about evidence entries. Flagged
   for the operator to confirm.
3. **Transitive identifier matching** is allowed (A-B by Jira key, B-C by
   INC number gives one group), with the chain shown, so the engineer can
   split it if wrong.
4. **Step 6 loops back to matching** on requested changes (dashed edge in the
   diagram), since a split or re-theme can change identifier groups.
5. **Quotes default to paraphrase;** a named quote appears only if the
   engineer picks it, per the flow's data profile.
6. **Reduced-input path:** with no file access, digests are pasted; missing
   versus skipped digests are asked about, never assumed.
7. **No collision found** with `accomplishments-drafter`,
   `portfolio-rationalization`, or the gatherer skills; each boundary is
   stated in "What this skill is not."

## Owed for promotion (operator)

- Five-point gate (`foundry-spec.md` §4), including a live test on each
  sanctioned engine using the brief's two simulated runs (review criterion 8).
- Replace `Layer-3: TBD` in `accomplishments-digest` Stage 6 with a pointer to
  this skill; add the row to `produced-skills/CONTEXT.md` at promotion; move
  the primer brief to `completed-skill-starters/` at promotion.

Nothing here has run on-engine. Catalogs untouched by design (four sibling
builds ran in parallel).
