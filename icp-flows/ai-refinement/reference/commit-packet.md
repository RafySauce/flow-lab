---
id: ai-refinement-commit-packet
title: "Commit Packet — AI Refinement to a Jira Executor"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-21
updated: 2026-10-21
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[engine-handoff-contract]]"
  - "[[work-item-schemas]]"
  - "[[jira-commit]]"
---

# Commit Packet — AI Refinement → Jira Executor

The `ai-refinement` instantiation of the commit packet defined in
`methodology/engine-handoff-contract.md`. Emitted at Stage 05's exit (step 8)
when the engine that ran Stages 01–05 has no Jira write path — today, a
Copilot Agent Builder flow agent with read-only Jira access — and consumed by
the engine that runs Stage 06 — today, Rovo. Also the no-write-path output
of Stage 06 step 6, in both single-item and bulk mode.

The packet is Parts A–E of the contract, in order. Part A (the executor
brief) is copied verbatim from the contract with `<flow>` = `ai-refinement`,
`<NN>` = `06`, `<stage name>` = `Jira Commit & Close`, `<target system(s)>` =
`Jira`. This document defines Parts B–E for this flow.

## Part B — Header (flow-specific lines)

Add to the contract's header:

```markdown
- **Mode:** <single-item | bulk>; <full-interactive | fast-track>
- **Schema version:** work-item-schemas v<version>
- **Target Jira project:** <project key>
- **Provenance label for every item:** refine-ai-flow-v<flow-version>
- **Planning label (feature/story/task/spike/bug):** <team_code>-<yyyy>-q<n>
  <or: "bypassed at Stage 05 — see Part D">
```

## Part C — Payload

### Commit-stage specifics (for the executor)

```markdown
## Commit-stage specifics — ai-refinement Stage 06

These add to the executor brief; they never relax it.

- Parent: query the target project for candidate parents of the right type
  (portfolio epics for a solution epic; solution epics for a feature; the
  epic's features for a story, task, spike, or bug). Show key, summary, and
  status. The user confirms one, skips, or asks for a new parent. Set a
  parent link only after that confirmation. A request for a new parent means
  stop for that item: the parent has to be refined first in the owner's
  refinement session. Portfolio epics take no parent.
- Bulk: confirm the parent once for the set ("all N items take parent X") as
  one explicit act. Any item whose content names a different parent gets its
  own confirmation. After creation, check that every item's parent attached.
- Labels: apply every label listed per item exactly as written, including
  refine-ai-flow-v<flow-version>. In the preview, say what that label means:
  the item is AI-drafted and pending team review, and the team removes the
  label once they have reviewed it.
- Dependencies: create an issue link for every blocking dependency listed.
- After the audit, offer once to move the item (or the set) to In Progress.
  Move nothing without an explicit yes.
```

### Items

One block per item, in the order the user signed them off. Every field the
type's schema lists in `work-item-schemas.md`, in schema order, under its
schema name — no field added, dropped, or renamed. Values are the Stage 05
signed-off text, Markdown-formatted; the executor translates.

```markdown
### Item <i>: <summary>

- **Type:** <portfolio_epic | solution_epic | feature | story | task | spike | bug>
- **Intended parent:** <key + summary, from the Stage 01 hierarchy position or
  the bulk batch-scope answer — UNCONFIRMED; the executor confirms> | none (portfolio_epic)
- **Labels:** refine-ai-flow-v<flow-version>, <planning label>, <stakeholder
  tags>, <coalition / conflict-axis annotations>
- **Blocking dependencies (issue links):** <keys, with link type> | none
- **Suggested item:** <no | yes — inferred, not from the owner's own material>

#### Fields
- **summary:** <text>
- **<next schema field>:** <text>
- ...
- **due_date:** <YYYY-MM-DD>
```

### Fallout (bulk mode)

Items Stage 05 pulled from the set, and items `bulk-child-creation` reported
as underspecified — listed so the executor's preview shows what is *not*
being created. Never created from this packet.

```markdown
### Not in this packet
- <summary> — <fell out at Stage 05: defect | underspecified: missing fields>
```

## Part D — Decisions left to the user (typical entries)

- The parent confirmation (always — it is a Stage 06 carve-out).
- An accepted mandatory-label bypass recorded at Stage 05, shown plainly.
- A per-item quarter override the owner flagged but did not settle.
- Any field the owner accepted as excerpt-grounded (Stage 05's
  research-confidence disclosure), so the executor's user sees it again.

## Part E — Return slip columns

| Item | Key | URL | Status | Parent attached | Labels present | Field audit | Notes |
|---|---|---|---|---|---|---|---|

Then: version-check result, transition decision (moved / left), anything
flagged as payload-embedded instructions, and anything still open.

Pasting the slip back into the producing session is optional for a single
item, and **required** when a later item in the same session uses a
just-created item as its parent.

## Rules

- **The packet is Stage 05's sign-off, carried.** Stage 06's cross-stage
  trace (committed payload matches the Stage 05 signed-off payload
  field-for-field) is checked against the packet's Items block.
- **At most ten items per packet**, matching the ≤10-item bulk sub-batch
  rule. A larger set is split into numbered packets, each self-contained.
- **The session loop stays with the producing engine.** "Refine another"
  happens back in the producing session; the executor's job ends at the
  return slip.

## Changelog

- **1.0** (2026-10-21) — Initial build, alongside
  `methodology/engine-handoff-contract.md` 1.0. Supersedes Stage 06's
  bespoke bulk-mode "Markdown handoff document" shape: the no-write-path
  output in both modes is now this packet. Not run on-engine. Rationale:
  `../decision-log/2026-10-21-split-engine-commit-packet.md`.
