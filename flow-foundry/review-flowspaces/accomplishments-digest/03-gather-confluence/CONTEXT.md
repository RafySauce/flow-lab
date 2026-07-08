# Stage 3 — Gather — Confluence & Collaboration (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`) — period and self-
identified top items. Independent of Stage 2's output (no dependency between
the two gather stages; either can run first, or in parallel).

## Process

Query Confluence for pages the engineer authored or substantially co-authored
within the period — design docs, RFCs, postmortems, process docs, runbooks —
and separately, wherever the platform surfaces it, collaboration signal:
review comments given, page mentions, cross-team page contributions. Group by
initiative the same way Stage 2 groups by theme, and frame each as scope or
leadership evidence ("drove the design for X," "wrote the postmortem that
changed Y's on-call process") rather than a page-title list. Before relying on
the collaboration-signal slice, check whether the target Confluence instance
actually exposes comment/mention history at the needed granularity — if not,
narrow to authored-pages-only and say so explicitly rather than presenting a
thin result as complete. `Layer-3: TBD — skill-primer-brief filed
(sp-confluence-contribution-gatherer)`.

## Outputs

A **Confluence & collaboration digest**: an initiative-grouped list of
authored/co-authored docs (framed as scope/leadership evidence) plus a
collaboration-signal section (or an explicit "collaboration signal
unavailable at this instance's activity-history depth" note). Lands as
`work/03-confluence-digest.md`.

## Verify

A specific cross-stage trace check: every self-identified top item from
Stage 1's framing brief that plausibly maps to a doc or initiative must
appear (explicitly, or explicitly flagged "not found in Confluence — narrative
only") in this stage's digest, mirroring Stage 2's check. Result recorded as
a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — constrained execution against a defined query and
  grouping method; no framing judgment happens here.
- **Evidence:** the digest is available for the engineer to skim before
  Stage 4 drafts from it; no formal sign-off required at this boundary.

## Data boundary

- **Max data-class this stage handles:** `internal` (page content; may
  reference other people as co-authors or reviewers — do not expand scope to
  their individual performance, and do not quote review comments in ways
  that read as evaluating a colleague rather than the engineer's own work).
- **Sanctioned engines for this stage:** Rovo, if the employer's matrix
  requires Confluence-native access to stay inside Atlassian; note at
  instantiation if a Copilot-side integration is also sanctioned.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
