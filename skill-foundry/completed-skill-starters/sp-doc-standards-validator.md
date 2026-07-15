---
id: sp-doc-standards-validator
title: "Skill Primer Brief — Doc Standards Validator"
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
related: ["[[documentarian]]", "[[sp-doc-drafter]]"]
---

# Skill Primer Brief — Doc Standards Validator

## Purpose

Validate one drafted document (or diff) against its doc-type schema and the
documentation-standards baseline, and emit a findings report — the
documentarian analog of `workitem-validation`. Reports only: it never edits
content and never resolves an open section.

## Triggering intent

- **Fires on:** documentarian Stage 05, once per work-order line, on the
  Stage 04 draft/diff.
- **Does not fire on:** work-item validation (`workitem-validation` — Jira
  payloads, different schema family); fixing what it finds (failures return
  to Stage 04); provenance frontmatter checks on mirror artifacts (that's
  `provenance-stamper`, referenced separately by the stage); judging content
  quality or correctness — evidence fidelity is Stage 04's citation
  discipline; this skill checks shape, standards, and honesty of the
  open-section accounting.

## Method sketch

- Schema completeness per the registry type: required sections present
  (protocol-conformant open markers count as present-by-design), metadata
  block complete.
- **Open-section enumeration:** list every deferred marker; the list must
  match in-document markers one-for-one — under-reporting markers starves
  Stage 06's waiver gate, the check that matters most.
- Standards pass per `documentation-standards.md`: title pattern, heading
  nesting, numbered-procedure shape, label set, link hygiene (links resolve,
  Jira keys exist), voice/formatting rules, no unapproved
  names/attributions, no bare TODO/TBD outside marker syntax.
- Diff safety on update lines: only work-order-scoped sections touched.
- Pass/fail per check, one-line finding per failure; user-accepted findings
  recorded as accepted, never deleted.

## Inputs and data boundary

Reads the Stage 04 draft/diff, the doc-type registry schema, and the
standards baseline. Max data-class: `internal`. Engines: Rovo or Copilot —
pure read-and-report against written specs.

## Demand source

Documentarian flowspace, Stage 05 (`05-standards-validation/CONTEXT.md`) —
Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

On a seeded draft carrying five planted defects (one missing required
section, one dead link, one bare TODO, one heading skip, one marker missing
from a doctored enumeration list): all five are findings with correct
one-line descriptions, zero false positives on the clean sections, the
document content is byte-identical after the run, and the corrected
enumeration matches in-document markers one-for-one.
