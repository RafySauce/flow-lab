# Stage 4 — Draft (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`), Stage 2's Jira digest
(`work/02-jira-digest.md`), and Stage 3's Confluence & collaboration digest
(`work/03-confluence-digest.md`) — all three, named explicitly; a draft built
from only the two gather digests and not the framing brief loses the
engineer's own narrative and reads as a tracker export.

## Process

Synthesize the three inputs into the house accomplishments-document shape
defined in `../reference/accomplishments-document-shape.md`:
themes/initiatives as the top-level structure (not "Jira" and "Confluence" as
separate sections — the reader shouldn't have to know which tool a given
accomplishment came from), each theme opening with the outcome framing, then
supporting detail, with Stage 1's self-identified top items given first
placement or visible emphasis within their themes rather than folded in
anonymously among tracker-sourced items. Match tone and detail level to
Stage 1's stated audience. Carry forward every thin-coverage or unavailable-
signal flag from Stages 2–3 as an explicit note rather than silently smoothing
over the gap. `Layer-3: skill built, staged in
skill-foundry/review-skills/accomplishments-drafter/ —
sp-accomplishments-drafter` awaiting operator promotion.

## Outputs

A **draft accomplishments document**: theme-structured, outcome-framed,
audience-matched, with Stage 1's top items visibly represented and any
coverage gaps noted rather than hidden. Lands as `work/04-draft.md`.

## Verify

A specific cross-stage trace check: every item in Stage 1's exclusion list is
absent from this draft (the check Stage 1's own Verify field defines) — this
is the stage where that check actually gets run, since it's the first stage
producing reader-facing prose. Also confirm every theme in the draft traces
to at least one Stage 2 or Stage 3 digest entry (no fabricated content).
Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — synthesis against a defined shape and three
  concrete source documents; not a new judgment call, so it doesn't carry
  Stage 1/5's weight, but the exclusion-list check above is non-negotiable
  regardless of intensity label.
- **Evidence:** the draft is handed to the engineer for Stage 5's review; no
  separate sign-off at this boundary.

## Data boundary

- **Max data-class this stage handles:** `internal` (synthesized content
  carries forward whatever Stages 2–3 gathered, at the same classification).
- **Sanctioned engines for this stage:** Rovo or Copilot — this stage is pure
  synthesis of already-gathered material, no new external query, so either
  engine sanctioned for `internal` content is fine.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
