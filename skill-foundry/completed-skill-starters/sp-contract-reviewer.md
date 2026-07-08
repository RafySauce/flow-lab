---
id: sp-contract-reviewer
title: "Skill Primer Brief — Stage-Contract Reviewer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-02
updated: 2026-07-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.0"
data-class: public
related: ["[[flow-foundry-spec]]"]
---

# Skill Primer Brief — Stage-Contract Reviewer

## Purpose

Pre-review a flowspace's stage contracts against the populated-vs-present standard before the human dry-run (validation gate 3), so the operator's review time goes to judgment instead of catching placeholder text.

## Triggering intent

- **Fires on:** "pre-review these contracts," a flowspace reaching `to-review`, and re-validation passes.
- **Does not fire on:** the dry-run itself or promotion (gate 3 is explicitly human — this skill is the *warm-up act*, and its report must say so), or authoring/fixing contracts (that's the flow-foundry with the operator).

## Method sketch

Per `CONTEXT.md`, test each of the six fields:

1. Inputs: names artifacts and locations? ("whatever the previous stage produces" → flag)
2. Process: verbs or output-descriptions? Layer-3 line present and resolvable?
3. Outputs: could the next stage's Inputs be drafted from this? (Attempt the draft; if it requires guessing, flag with the specific gap.)
4. Verify: names two stages, an artifact, and a property? ("confirm it's good" → flag)
5. Review: a real named human, an intensity, an evidence form?
6. Data boundary: class + engines stated; consistent with `HUB.md`'s stage table?

Emit a findings report per stage, severity-ranked, quoting the failing text.

## Inputs and data boundary

Reads flowspace trees (mirror or Confluence). Max data-class: internal. Engine: **Copilot** (custom agent on the mirror) primary; Rovo adapter optional.

## Demand source

Flow-foundry validation gate 1/3 prep — every scaffolded flowspace passes this bottleneck, and contract quality is the load-bearing discipline of the whole method.

## Definition of done

On a seeded flowspace with one deliberately weak field of each of the six kinds, flags all six with quoted text and drafts no false "next-stage Inputs" for the passing stages.
