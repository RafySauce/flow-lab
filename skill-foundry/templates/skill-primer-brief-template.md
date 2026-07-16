---
id: sp-<slug>
title: "Skill Primer Brief — <Skill Name>"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable human>
source: <human | human+ai>
generated-by: <flow-foundry, if this brief comes from a Layer-3 gap; omit if hand-raised>
data-class: <public | internal | confidential | restricted>
related: ["[[<flowspace-id>]] (if filed from a flowspace gap)"]
---

# Skill Primer Brief — <Skill Name>

> Intake path 1 for the skill-foundry: crystallized intent, written before authoring starts. File in `skill-foundry/backlog-skill-starters/` as `sp-<slug>.md`.

## Purpose

One or two sentences: what capability, for whom, replacing what manual work.

## Triggering intent

The situations that should invoke this skill — concrete phrasings and contexts. Then the near-misses: situations that *look* adjacent but should **not** trigger it (this is what keeps skills from colliding).

## Method sketch

Best current understanding of how the skill should work: steps, quality bar, known failure modes to guard against. Bullet-level is fine; the foundry develops it into the full spec.

## Inputs and data boundary

What context/sources the skill needs (pages, boards, repos, documents). Max `data-class` it will handle. Which engine(s) it should run on — and note if that's a constraint with its reason (e.g., "must be Rovo: the invoking users work in Atlassian chat," or "this data class isn't sanctioned for Copilot per the employer matrix"). Both engines ground on the GitLab source of truth, so repo access alone is never the constraint.

## Demand source

Where this need came from: a flowspace stage (name it and the gap), a recurring manual task, a request. If from a flowspace, the stage's `CONTEXT.md` gets this brief's id.

## Definition of done

How the operator will judge the built skill acceptable — this seeds the spec's review criteria and the live test at the gate.
