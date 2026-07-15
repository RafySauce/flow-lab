# Stage 5 — Align & Publish (`CONTEXT.md`)

## Inputs

Stage 4's draft accomplishments document (`work/04-draft.md`) and Stage 1's
original framing brief (`work/01-framing-brief.md`), for direct comparison —
this stage's whole job is checking the draft against the framing, not reading
the draft fresh.

## Process

The engineer reads the draft against their own Stage 1 framing: does it
represent what they actually think mattered, in their own voice, at the right
level of detail for the stated audience? This is closer to debugging than
composing — line edits, re-ordering emphasis, cutting anything that reads as
generic tracker output, adding color the tools couldn't surface. Confirm the
Stage 1 exclusion-list check (already run mechanically at Stage 4) with a
human read, since exclusion is exactly the kind of judgment call that
shouldn't rely solely on an automated check. Once satisfied, the engineer
publishes — sharing the document with their manager or the stated audience.
`Layer-3: inline (one-off, described above)`.

## Outputs

The **final accomplishments document**, published to the primary surface
(the engineer's Confluence `Accomplishments` page tree, this cycle's page)
and shared with the stated audience. This is the flow's terminal artifact —
nothing downstream consumes it within this flowspace.

## Verify

A specific cross-stage trace check: the published document's audience and
period match Stage 1's framing brief exactly (no silent scope creep to a
different cycle or a wider audience than the engineer originally set).
Result recorded as a one-line entry in the run's decision log — this is also
the run's closing entry.

## Review

- **Reviewer:** the engineer (this is their own document, shared under their
  own name).
- **Intensity:** `heavy` — final alignment against the Stage 1 framing;
  this is the "closer to debugging" end of the U-curve, and the last point
  before the document leaves the flow entirely.
- **Evidence:** the engineer's explicit confirmation before sharing ("this
  reads as mine, this is what I want my manager to see"), plus the
  publication itself as the record.

## Data boundary

- **Max data-class this stage handles:** `internal` (the finished document
  may be shared beyond the immediate team once published — confirm the
  audience matches what Stage 1 authorized before that happens).
- **Sanctioned engines for this stage:** Rovo or Copilot for the edit pass;
  publication itself happens on whichever surface the employer's sanctioned-
  tool matrix designates for performance-review material (may be stricter
  than the gather stages' matrix).
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
