---
id: sp-doc-evidence-gatherer
title: "Skill Primer Brief — Doc Evidence Gatherer"
type: skill-primer-brief
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
related: ["[[documentarian]]"]
---

# Skill Primer Brief — Doc Evidence Gatherer

## Purpose

Build the documentarian flowspace's Stage 02 **evidence dossier**: a cited,
job-type-steered sweep of Jira, Confluence, transcripts, and delivered-work
artifacts that downstream doc planning and drafting can trace every claim to.
Replaces the manual "open twenty tabs and reconstruct what happened" pass
that precedes any honest documentation effort.

## Triggering intent

- **Fires on:** documentarian Stage 02, in the mode the confirmed job type
  selects — `closeout` (walk closed items: fields, full comment thread,
  linked pages/issues), `modernize`/`tree-audit` (page-tree inventory with
  staleness signals), `sad-update` (delivered feature's items, design docs,
  repo context), `meeting` (distill a screened transcript into decisions /
  actions / discussed items, resolving mentioned Jira keys).
- **Does not fire on:** gathering one engineer's accomplishments evidence
  (that's `jira-accomplishments-gatherer` / `confluence-contribution-gatherer`
  — different scope, different quality bars; reusing them here would violate
  their declared boundaries); eliciting requirements from a human
  (`context-elicitation`, bound to the ai-refinement persona); writing or
  planning anything — this skill is read-only and stops at the dossier.

## Method sketch

- One skill, mode-conditioned — the `context-elicitation` eight-type-taxonomy
  precedent: shared gathering discipline (read-only; cite every entry with a
  resolvable source link; flag indirect evidence with a confidence note),
  mode-specific sweeps.
- Closeout mode distinguishes outcome statements from plan statements in
  comments ("we will" is not "we did").
- Tree modes collect the staleness signals `documentation-standards.md`
  defines (review-by lapses, dead links, orphan position).
- Meeting mode carries no attributions the Stage 01 screen did not approve,
  and confirms mentioned Jira keys exist.
- Gaps the evidence cannot answer are emitted as explicit **open evidence
  questions** — the input to the open-section plan. Failure mode to guard:
  silently absorbing a gap into fluent prose.

## Inputs and data boundary

Reads Jira projects and Confluence spaces scoped at Stage 01/02, plus
user-provided transcripts. Max data-class: `internal`; a sweep that surfaces
`confidential` content stops and re-scopes. Engine: **Rovo** for the
Atlassian sweep (data stays in Atlassian); Copilot contributes repo context
for `sad-update` via a mirroring-protocol §5 handoff.

## Demand source

Documentarian flowspace, Stage 02 (`02-evidence-gathering/CONTEXT.md`) —
Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

Against a seeded test set (one closed item with a mixed will-do/did comment
thread, one small page tree with two stale pages, one synthetic transcript
naming two real and one nonexistent Jira key): every dossier entry's source
link resolves; the will-do statement is not reported as an outcome; both
stale pages carry the right signals; the nonexistent key is flagged, not
listed; at least one open evidence question is emitted where the material is
silent; nothing was written to any platform.
