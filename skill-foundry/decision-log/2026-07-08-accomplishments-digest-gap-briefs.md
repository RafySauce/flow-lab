---
id: decision-2026-07-08-accomplishments-digest-gap-briefs
title: "Decision Log — Three Skill-Primer-Briefs Filed from Accomplishments Digest Layer-3 Triage"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-jira-accomplishments-gatherer]]"
  - "[[sp-confluence-contribution-gatherer]]"
  - "[[sp-accomplishments-drafter]]"
  - "[[accomplishments-digest]]"
---

# Decision Log — 2026-07-08 — Accomplishments Digest Gap Briefs

**What was decided:** file three skill-primer-briefs to
`backlog-skill-starters/` — `sp-jira-accomplishments-gatherer`,
`sp-confluence-contribution-gatherer`, `sp-accomplishments-drafter` —
matching the three Layer-3 gaps flagged during the flow-foundry's scaffold of
the `accomplishments-digest` flowspace (Stages 2, 3, and 4 respectively).
**By whom:** agent, as part of the flowspace scaffold, per `foundry-spec.md`
§4's Layer-3 triage rule (gap → draft a primer brief, mark the contract
`TBD`, note it in `HUB.md`). **What it affects:** three new briefs at
`truth-level: to-review`; no skills authored yet — this is the demand-loop
handoff (flow-foundry flags, skill-foundry builds later), not a build.

## Why three separate briefs, not one combined skill

Each targets a different data source or operation with its own contract:
the two gatherers hit different platforms (Jira vs. Confluence) with
different native-access constraints, and the drafter is pure synthesis with
no external query at all — bundling any two would blur a boundary the
skill-foundry's own discipline (declared non-goals, no overlapping tools)
argues against. This mirrors the existing `ai-refinement` flowspace's pattern
of one skill per pipeline stage rather than one skill per flowspace.

## Assumption (operator to confirm or amend)

- **J1 — these three are worth building, not dropping.** Unlike the
  `sp-intake-triage-assistant` drop (`2026-07-07-skill-starter-triage-drop.md`),
  no volume/necessity concern applies here — the flowspace cannot run its
  gather/draft stages without them, so the presumption is build, not drop.
  Amendment path: if instantiation reveals the underlying Jira/Confluence
  queries are simple enough to stay inline in the flowspace contracts rather
  than warranting standalone reusable skills, drop these with a logged
  reason and fold the logic into the stage `CONTEXT.md` files instead.
