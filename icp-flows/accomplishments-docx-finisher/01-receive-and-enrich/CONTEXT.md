---
id: accomplishments-docx-finisher-stage-01
title: "Stage 01 — Receive & Enrich"
type: stage-context
stage: 1
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
  - "[[accomplishments-docx-finisher]]"
  - "[[repo-context-enricher]]"
---

# Stage 1 — Receive & Enrich (`CONTEXT.md`)

## Inputs

The handoff file from `accomplishments-digest` Stage 6
(`handoffs/YYYY-MM-DD-accomplishments-digest-to-docx-finisher.md`), per
`../../accomplishments-digest/reference/handoff-to-copilot-template.md` —
specifically: the published document content/link, the exclusion list, the
authorized repo/file-access scope, and any stated style preference.

## Process

Parse the handoff and confirm the authorized repo/file-access scope before
touching anything — a blank or ambiguous scope means **no access**, per the
handoff template's rule; ask rather than assume a broader scope. Within the
authorized scope, pull supporting evidence (relevant PRs, commits, linked
docs, code ownership) that reinforces what the published document already
claims. This is enrichment of presentation and evidence, never new
accomplishments — if the repo context surfaces something noteworthy that
isn't already in the published document, it does not get added here; it gets
flagged as a note for the engineer to decide whether it belongs in a future
`accomplishments-digest` run, not smuggled into this one. Every addition made
must be flagged distinctly (e.g. an inline marker or a separate "Added by
Stage 1" list) so Stage 3 can scrutinize exactly what changed.
`Layer-3: repo-context-enricher` (skill spec in
`produced-skills/repo-context-enricher/`, `verified`).

## Outputs

An **enriched content set**: the original published document plus a
distinctly-flagged list of supporting evidence additions (each tied to the
theme/section it supports), and a separate note of any out-of-scope findings
surfaced but deliberately not added. Lands as `work/01-enriched-content.md`.

## Verify

A specific cross-stage trace check: every flagged addition in this stage's
output must trace to a specific item within the authorized repo/file-access
scope from the handoff — an addition that can't be traced to an authorized
source is the failure mode this catches, and it must be removed before
Stage 2 runs. Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — a documented deviation from the U-curve's "first
  stage heavy" default (see `../HUB.md`'s diagram note and the primer
  brief): the framing judgment already happened upstream, at
  `accomplishments-digest` Stage 5. This stage adds evidence within a
  pre-authorized scope, not open judgment.
- **Evidence:** the flagged-additions list itself is the review surface;
  formal sign-off is deferred to Stage 3, which re-checks these additions
  alongside the exclusion list.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits the handoff's
  classification; repo/file content pulled stays within the same or lower
  classification — never escalate by pulling something more sensitive than
  the handoff authorized).
- **Sanctioned engines for this stage:** Copilot (named as the receiving
  engine in the handoff) — this stage requires repository/file access,
  which is the reason it's Copilot-side rather than Rovo-side.
- A handoff into this stage from an engine outside this boundary, or with no
  stated authorized scope, is invalid — stop and ask, don't infer.
