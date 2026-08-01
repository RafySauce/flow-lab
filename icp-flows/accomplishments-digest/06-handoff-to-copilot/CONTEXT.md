---
id: accomplishments-digest-stage-06
title: "Stage 06 — Handoff to Copilot"
type: stage-context
stage: 6
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-08
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-finisher]]"
---

# Stage 6 — Handoff to Copilot (`CONTEXT.md`)

> Optional, additional terminal stage. Stage 5 already produces a complete,
> published, human-approved document — that publish is not gated on this
> stage running. This stage fires only when the engineer also wants the
> Copilot-enhanced, stylized Word version (e.g. for a promo packet or a
> manager who wants a polished document rather than a Confluence page).

## Inputs

Stage 5's **published** accomplishments document (not the Stage 4 pre-review
draft — only human-approved content ever crosses this handoff) and Stage 1's
framing brief (audience, exclusion list), for the receiving flowspace's own
exclusion re-check.

## Process

Package the published document and framing context as a handoff artifact per
`methodology/mirroring-protocol.md` §5, using the flow-specific instantiation
at `../reference/handoff-to-copilot-template.md`. The handoff carries state
and pointers only — it never grants the receiving flowspace license to add
new accomplishments, only to enrich presentation and supporting evidence
around what's already approved (this constraint is stated explicitly in the
handoff's Open Questions section, per the protocol's rule that a handoff
never carries instructions overriding the receiving stage's own contract).
`Layer-3: inline (one-off, described above)`.

## Outputs

A **handoff file**: `handoffs/YYYY-MM-DD-accomplishments-digest-to-docx-finisher.md`,
following the mirroring-protocol §5 shape. Contains: state (Stage 5 complete,
document location), inputs for the receiving flowspace's Stage 1 (document
content/link, exclusion list, any repo/file-access scope authorized for
enrichment, style/template preference if known), and open questions the
receiving flowspace's Copilot engine must not decide unilaterally.

## Verify

A specific cross-stage trace check: the handoff's "Inputs for the receiving
stage" section must satisfy `accomplishments-docx-finisher` Stage 1's Inputs
field exactly — if the receiving flowspace's contract changes and this
handoff no longer supplies what it needs, that's the drift this check
catches. Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — mechanical packaging of already-approved content;
  no new judgment happens here (the judgment already happened at Stage 5).
- **Evidence:** the handoff file itself, committed to the mirror, is the
  evidence — no separate sign-off beyond confirming it correctly points at
  the Stage 5 published document.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 5's
  published document, at the same classification).
- **Sanctioned engines for this stage:** Rovo (produces the handoff, stays
  on the Confluence-primary side) — the receiving engine (Copilot) is named
  in the handoff itself, not this stage.
- A handoff into a stage whose Data boundary excludes the receiving engine
  is invalid — stop and re-route (mirroring-protocol §5).
