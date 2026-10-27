---
id: accomplishments-digest-stage-06
title: "Stage 06 — Correlate"
type: stage-context
stage: 6
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[sp-accomplishments-correlator]]"
---

# Stage 6 — Correlate (`CONTEXT.md`)

> A deliberate mid-flow heavy gate, which deviates from the U-curve default.
> The reason: this is the point where all gathered context is loaded together
> and turned into the units the report is built from. A wrong merge (two
> different incidents treated as one) or an over-merge (one fix inflated into a
> theme) locks in here, and every later stage inherits it. The operator's call
> (2026-10-27): "once the context is loaded up, we need to confirm it is
> correct so the report generates correctly." Logged in
> `../decision-log/2026-10-27-m365-servicenow-revision.md`.

## Inputs

Stage 1's framing brief and every gather digest that ran:
`work/02-jira-digest.md`, `work/03-confluence-digest.md`,
`work/04-m365-digest.md`, and `work/05-servicenow-digest.md`. A digest that
declared its stage skipped or unreachable counts as present, so its gap is
carried forward. A digest that is simply missing is not acceptable: stop and
run or explicitly skip that stage.

## Process

Build **accomplishment groups**. Each group is one piece of work, with every
piece of evidence about it from every source.

1. **Match on hard identifiers first.** These are INC/CHG/PRB/PTASK numbers,
   Jira keys, Confluence page links, and SharePoint file references that appear in
   more than one digest. For example, an INC record, the thank-you email
   that names it, and the Teams recap where its root-cause fix was decided
   become one group.
2. **Then match on themes.** Group remaining entries under Stage 1's themes
   and top items when the link is clear. Mark each theme-based match
   `inferred` so it is visibly weaker than an identifier match.
3. **Keep the rest as singletons.** Unmatched evidence stays visible as its
   own group. Nothing is dropped.
4. **Don't merge by similarity alone.** Two records with similar
   descriptions but no shared identifier or clear theme link stay separate,
   and are flagged as "possible duplicate — engineer to decide."
5. **Attach load context.** ServiceNow volume attaches to the groups and
   themes it supports, as evidence only. The load summary is carried
   whole for the Operational load section.

Then present the groups to the engineer for confirmation, ordered with
Stage 1 top items first. The engineer can merge, split, re-theme, drop, or
promote groups, choose any verbatim recognition quote they want used, and
confirm that each top item has a group (or accept a "narrative only" flag).
`Layer-3: TBD — brief filed (sp-accomplishments-correlator)`.

## Outputs

A **confirmed correlation map**. Each accomplishment group has a working title, its
theme, its evidence entries with source and citation, its match basis
(identifier / inferred / singleton), and the engineer's disposition (keep /
merged / split / dropped). It also lists the gaps carried forward from each
digest, the load summary, and any verbatim quotes the engineer approved. Lands as
`work/06-correlation-map.md`.

## Verify

Two cross-stage trace checks:

- **Coverage:** every entry in every gather digest appears in exactly one
  group or is listed as dropped by the engineer. Count in equals count out.
- **Top items:** every Stage 1 top item maps to at least one confirmed group,
  or carries a "narrative only" flag the engineer accepted.

Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `heavy`. This is a judgment boundary: deciding what counts as
  one accomplishment, and whether the loaded context is right, before any
  prose exists.
- **Evidence:** the engineer's explicit confirmation of the map ("these groups
  are right, draft from these"), recorded in the run's decision log with any
  merges, splits, or drops they made.

## Data boundary

- **Max data-class this stage handles:** `internal`, carried from the
  digests. There is no new external query here.
- **Sanctioned engines for this stage:** any engine sanctioned for
  `internal` content. This stage is pure synthesis of already-gathered
  material.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
