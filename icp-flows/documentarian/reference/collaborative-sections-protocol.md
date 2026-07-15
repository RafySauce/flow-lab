---
id: collaborative-sections-protocol
title: "Collaborative Sections Protocol — Open-Section Markers"
type: specification
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[doc-type-registry]]"
---

# Collaborative Sections Protocol — Open-Section Markers

The mechanism that makes documentarian drafting *collaborative by
construction*: the flow builds the parts of a document the evidence supports
and marks the parts a human must supply — visibly, with an owner, instead of
guessing. This is the flow's answer to the defining failure mode of
AI-drafted documentation: fluent, plausible, invented content in exactly the
places nobody had evidence.

## Marker syntax

An open section is a blockquote marker in place of (or inside) the section's
content:

```markdown
> [OPEN — <owner>: <what's needed, one line>]
```

- `<owner>` — the accountable human by name or role (ungrounded mode: asked
  of the user at Stage 03; never guessed).
- `<what's needed>` — specific enough to fill without re-deriving context
  ("the escalation rotation for sev-1, and who owns the pager Tuesday
  handoff" — not "escalation info").
- A marker may be preceded by scaffold: the agent writes the section's frame
  and any evidence-supported fragments, and the marker covers exactly the
  missing part.

On the Confluence primary, the marker renders as the same blockquote (or the
tenant's task/status macro where one is confirmed at instantiation — the
custody model records the choice); the text form above is canonical in the
mirror.

## Lifecycle

1. **Planned** — Stage 03 maps each open evidence question onto a document's
   open-section plan, with owner.
2. **Emitted** — Stage 04 writes the marker into the draft. Filling a planned
   open section with generated content is a defect, full stop.
3. **Enumerated** — Stage 05 lists every deferred marker; the list must match
   the in-document markers one-for-one. Validation never resolves, softens,
   or hides a marker.
4. **Gated** — Stage 06's waiver gate: before commit, the user either fills
   each open section or explicitly waives it. A commit carrying open markers
   happens only on a recorded waiver — never silently.
5. **Tracked** — Stage 07 notes waived sections on the document's registry
   row and shortens its review-by, so open sections resurface on a clock
   instead of fossilizing.
6. **Resolved** — the owner fills the section in place (directly on the page,
   or via a later documentarian update line); the next custody touch clears
   the row's note.

## Rules

- Every marker has exactly one owner. "Team to fill" fails the protocol.
- Markers are never nested and never used for agent-to-agent notes — they are
  human-facing asks only.
- The count of markers is honest workload signal: Stage 03 chooses fewer,
  well-scoped open sections over sprinkling markers to hedge. If more than
  half a document would be open sections, the evidence isn't ready — that's a
  Stage 03 finding (gather more, or defer the document), not a marker
  problem.
- A marker outside this syntax (bare TODO/TBD, empty heading) is a Stage 05
  finding — either it becomes a protocol marker with an owner, or it gets
  filled.
