---
id: sp-doc-planner
title: "Skill Primer Brief — Doc Planner"
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
related: ["[[documentarian]]", "[[sp-doc-evidence-gatherer]]"]
---

# Skill Primer Brief — Doc Planner

## Purpose

Turn a documentarian evidence dossier plus the doc-type registry into a
confirmed **doc work order**: per document, create/update/archive, the
matched doc type and template, the open-section plan, and the Jira-link plan
— agent proposes with rationale, human decides line by line. This is the
judgment core of the flow; the skill's job is to make the judgment
inspectable, not to make it.

## Triggering intent

- **Fires on:** documentarian Stage 03, once per job, on a Stage 02 dossier.
  Also produces the audit-report preamble for `tree-audit` jobs and the
  candidate work items for `meeting` jobs (shaped per
  `reference/ai-refinement-handoff-contract.md`).
- **Does not fire on:** drafting document content (that's `doc-drafter` —
  this skill plans, it never writes prose into documents); refining or
  creating work items (candidates go to ai-refinement; this skill never
  targets Jira creation); re-gathering evidence (a thin dossier is returned
  to Stage 02, not padded).

## Method sketch

- Propose documents only from citing evidence — a document with no dossier
  entries behind it doesn't get proposed.
- Match each to one of the six registry types with a stated rationale;
  redirect out-of-scope intents per the registry table.
- Map every open evidence question onto an open-section plan with an owner
  (ungrounded mode: ask the user); one question silently dropped is the
  defining defect.
- Per-line user confirm/edit/strike, recorded; the confirmed work order
  fixes downstream scope.
- Failure modes to guard: over-proposing (documentation for its own sake —
  the registry's out-of-scope table and the "no citing evidence" rule are
  the brake), and hedging with open sections (>50% open means the evidence
  isn't ready — finding, not plan).

## Inputs and data boundary

Reads the Stage 02 dossier, the doc-type registry, and (update lines) target
page metadata. Max data-class: `internal`. Engines: Rovo or Copilot —
planning works from already-gathered material; no platform writes.

## Demand source

Documentarian flowspace, Stage 03
(`03-doc-plan-and-template-match/CONTEXT.md`) — Layer-3 gap flagged at
scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

On a seeded closeout dossier (rich evidence for one runbook, partial evidence
for one SOP, one out-of-scope BRD-shaped ask, two open evidence questions):
proposes exactly the two in-scope documents with type rationale, redirects
the BRD ask to ai-refinement, maps both open questions to owned open
sections, and produces a work order the user can confirm line-by-line with
every decision captured. No document proposed without citations.
