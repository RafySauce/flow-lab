---
id: sp-sad-diagram-maintainer
title: "Skill Primer Brief — SAD Diagram Maintainer"
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

# Skill Primer Brief — SAD Diagram Maintainer

> **Merge candidate.** Filed separately because diagram-source editing has
> its own quality bars and failure modes, but the skill-foundry should
> explicitly decide at build time whether this folds into `doc-drafter` as a
> mode rather than standing alone. If merged, `doc-drafter`'s spec absorbs
> this brief's method and quality bars, and this brief is closed with a
> pointer.

## Purpose

Update **text-editable** architecture-diagram sources (Mermaid, PlantUML,
drawio XML) inside SAD documents to reflect a delivered feature, with the
same diff-and-cite discipline as prose updates — and flag everything else
(images, screenshots, lost-source diagrams) for human redraw instead of
regenerating it lossily.

## Triggering intent

- **Fires on:** documentarian Stage 04, `sad-update` work-order lines whose
  target sections include diagram sources.
- **Does not fire on:** prose sections of the same SAD (that's
  `doc-drafter`); creating architecture from scratch with no delivered-change
  evidence (that's design work, not documentation maintenance); flowspace
  Stage Flow Diagrams (those belong to the foundries and
  `flow-diagram-guide.md`); non-text diagram formats — those are flagged as
  open sections for human redraw, never traced over or re-drawn from
  inference.

## Method sketch

- Parse the existing diagram source; identify the elements the delivered
  change touches (from the dossier's feature evidence: new component, changed
  interface, removed flow).
- Apply the minimal edit: add/rename/remove exactly the evidenced elements;
  preserve layout hints, styling, and untouched elements byte-for-byte where
  the format allows.
- Present as source diff plus a rendered before/after where the surface can
  render it.
- Every diagram edit cites the evidence entry that justifies it — an
  unevidenced "tidy-up" of someone's diagram is a defect.
- Failure modes to guard: silent re-layout that makes the diff unreviewable;
  inventing intermediate components to make the picture "complete";
  editing a rendered image's underlying source when the two have drifted
  (check for drift first; drifted pairs get flagged, not edited).

## Inputs and data boundary

Reads the SAD page's diagram sources (Confluence attachment/macro body or
mirror file) and the `sad-update` dossier. Max data-class: `internal`.
Engines: Copilot for mirror-side source edits, Rovo where the source lives in
Confluence macros — the build confirms which surface holds sources per
tenant.

## Demand source

Documentarian flowspace, Stage 04 (`04-draft-and-update/CONTEXT.md`),
`sad-update` job type — Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

On a seeded Mermaid component diagram plus a dossier evidencing one added
service and one changed interface: the edit adds exactly one node and
relabels exactly one edge, the rest of the source is unchanged, both edits
carry citations, and a companion PNG-only diagram in the same document is
flagged for human redraw rather than touched. If the merge into `doc-drafter`
is chosen instead, these same checks run as that skill's diagram-mode tests.
