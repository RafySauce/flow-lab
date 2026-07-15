# Stage 2 — Gather — Jira (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`) — specifically the period
(start/end dates) and the engineer's self-identified top items, used to check
completeness later, not to pre-filter the query. Also the engineer's Jira
identity/account and the project(s)/board(s) they work in.

## Process

Query Jira for work items the engineer closed, resolved, or was the primary
assignee/driver on within the period. Group results by theme (feature area,
initiative, or problem domain — not by issue type or sprint), and for each
theme reframe from ticket titles to outcomes: "shipped X, which enabled Y" or
"resolved Z, cutting <impact>" rather than a bare list of ticket keys and
summaries. Ticket counts are supporting evidence, not the headline. Flag any
theme where the tracker data looks thin relative to what the engineer's Stage
1 framing implied — that's a signal for Stage 4 to lean more on the narrative,
not a gap to silently paper over. `Layer-3: jira-accomplishments-gatherer`
(skill spec in `produced-skills/jira-accomplishments-gatherer/`, `verified`).

## Outputs

A **Jira digest**: a theme-grouped list, each theme carrying 2–5 outcome-framed
bullets with the underlying ticket keys cited (for traceability, not display),
plus a short flag list of any thin-coverage themes. Lands as
`work/02-jira-digest.md`.

## Verify

A specific cross-stage trace check: every self-identified top item from
Stage 1's framing brief that plausibly maps to Jira work must appear
(explicitly, or explicitly flagged as "not found in Jira — narrative only")
in this stage's digest. Silently dropping a Stage-1 item because the tracker
query missed it is the failure mode this catches. Result recorded as a
one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — constrained execution against a defined query and
  grouping method; no framing judgment happens here.
- **Evidence:** the digest is available for the engineer to skim before
  Stage 4 drafts from it; no formal sign-off required at this boundary (that
  weight sits at Stage 5).

## Data boundary

- **Max data-class this stage handles:** `internal` (project/ticket content;
  may include other engineers' names as collaborators — do not expand scope
  to their individual performance).
- **Sanctioned engines for this stage:** Rovo, if the employer's matrix
  requires Jira-native access to stay inside Atlassian; note at instantiation
  if a Copilot-side integration is also sanctioned.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
