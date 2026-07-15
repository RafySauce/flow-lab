---
id: sp-doc-drafter
title: "Skill Primer Brief — Doc Drafter"
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
related: ["[[documentarian]]", "[[sp-sad-diagram-maintainer]]"]
---

# Skill Primer Brief — Doc Drafter

## Purpose

Draft or update one governed document against its registry template, filling
only what the evidence supports and emitting protocol-conformant open-section
markers for everything a human must supply. Serves all five documentarian job
types; the collaborative open-section discipline is the whole point — this is
the skill that must *not* write fluent, invented content into evidence gaps.

## Triggering intent

- **Fires on:** documentarian Stage 04, once per work-order line: `create`
  lines (instantiate the matched registry template, draft evidence-grounded
  sections, mark planned open sections) and `update` lines (section-by-section
  diffs against the existing page, preserving content the evidence doesn't
  contradict).
- **Does not fire on:** deciding *what* to draft (that's `doc-planner`'s
  confirmed work order); validating (that's `doc-standards-validator`);
  committing (that's `confluence-page-commit`); accomplishments narrative
  drafting (`accomplishments-drafter` — different document family, different
  voice contract); diagram-source edits (see `sp-sad-diagram-maintainer`,
  flagged as a merge candidate into this skill — the build decides).

## Method sketch

- Instantiate the registry template: all required sections, metadata block
  (owner, type, source-evidence links, review-by).
- Every substantive claim cites a dossier entry; indirect evidence is drafted
  as indirect ("the close-out comments indicate…"), not asserted.
- Planned open sections become `> [OPEN — <owner>: <what's needed>]` markers
  with surrounding scaffold — never generated content. **The defining failure
  mode: a planned open section quietly filled with plausible prose.** The
  build's quality bar should treat one such instance as a gate failure.
- Updates are diffs: unchanged sections declared unchanged, modifications
  shown old → new; no style rewrites outside `modernize` scope.
- Voice per `documentation-standards.md` (instructional, second person; no
  bold-as-structure, no emojis).

## Inputs and data boundary

Reads one work-order line, its cited dossier entries, the registry template,
the open-section protocol, and (updates) the existing page. Max data-class:
`internal`. Engines: Rovo or Copilot — Copilot for repo-adjacent `sad-update`
content, Rovo for Confluence-native material.

## Demand source

Documentarian flowspace, Stage 04 (`04-draft-and-update/CONTEXT.md`) —
Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

On a seeded runbook `create` line (evidence covering diagnosis and
remediation; escalation path planned open) and a seeded SOP `update` line
(evidence touching two of six sections): the runbook draft cites every
diagnosis/remediation claim, carries exactly one open-section marker (owned,
specific), and invents nothing for escalation; the SOP diff modifies only the
two evidenced sections and declares the rest unchanged. Section sets match
the registry templates exactly.
