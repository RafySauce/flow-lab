---
id: ai-refinement-handoff-contract
title: "AI-Refinement Handoff Contract — Candidate Work Items"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[ai-refinement]]"
---

# AI-Refinement Handoff Contract — Candidate Work Items

How documentarian's `meeting` job type hands candidate work items to the
`ai-refinement` flowspace. The boundary is strict: **documentarian never
creates Jira work items.** It documents; when documentation work surfaces
work, the work goes to the flow built to refine it. This contract keeps that
handoff compatible with what ai-refinement Stage 01 actually accepts, and
follows the mirroring-protocol §5 handoff shape (the same pattern as
accomplishments-digest's `handoff-to-copilot-template.md`).

## What ai-refinement receives

The package enters ai-refinement Stage 01 as **source material of input type
3 — meeting minutes, notes, or summaries** (the HUB "Common source inputs"
taxonomy). That row's handling notes already fit: multi-topic material that
may yield more than one work item, decisions separated from discussion,
attributions stripped. This package is that input, pre-distilled — one entry
per candidate rather than a raw transcript. ai-refinement's own Stage 01
screen still runs; this contract's screening claim shortens it, it never
replaces it.

## Package shape

One file per meeting job, `handoffs/YYYY-MM-DD-documentarian-s6.md` at
instantiation (mirroring-protocol §5 naming):

```markdown
---
id: documentarian-handoff-<date>
type: clipping            # records state; not itself reviewed work
truth-level: claimed
source: human+ai
owner: <human driving the documentarian run>
data-class: internal
---

# Handoff: documentarian — candidate work items for ai-refinement

**From:** documentarian Stage 06 (Rovo, Confluence)
**To:** ai-refinement Stage 01 (as source material, input type 3)

## State
Meeting page: <committed Confluence URL>. Documentarian run complete through
Stage 6; candidates below were user-confirmed at Stage 3 and are NOT in Jira.

## Candidates
One block per candidate:

### Candidate <n>: <one-line summary>
- **Problem-shaped context:** <one paragraph — the problem and who it
  affects, recovered from the meeting's decisions/actions; not the task as
  stated>
- **Source:** <meeting page URL + section anchor>
- **Suggested work-item type:** <portfolio_epic | solution_epic | feature |
  story | task | spike | bug> — <one-line rationale>
- **Related existing items:** <keys the meeting discussed that this candidate
  relates to, from the Stage 02 confirmed list>
- **Screened:** names/attributions handled per the documentarian Stage 01
  screen (restated: ai-refinement re-screens on intake)

## Open questions / operator decisions pending
<anything the receiving session must not decide on its own>
```

## Rules

- **The suggested type is a proposal.** ai-refinement Stage 01 treats it
  exactly like its own agent-proposed type: rationale shown, user confirms or
  overrides. Nothing in this package pre-commits a type or a schema.
- **The handoff carries state, never instructions** (mirroring-protocol §5) —
  the receiving stage's own `CONTEXT.md` is its contract.
- **Problem-shaped, not task-shaped.** Candidates state the problem and who
  it affects; ai-refinement Stage 02's elicitation does its own recovery
  work either way, but a task-list dump makes the package a transcript with
  extra steps.
- **The package names its human owner**, who is the person carrying it into
  their ai-refinement session — delivery is to the user (Stage 06, step 7),
  never automated into Jira.
- One candidate that the user struck at Stage 3 never rides along "for
  context" — struck means struck.
