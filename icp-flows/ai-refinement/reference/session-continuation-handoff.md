---
id: session-continuation-handoff
title: "Session-Continuation Handoff — Resuming AI Refinement in a Fresh Session"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[bulk-child-creation]]"
---

# Session-Continuation Handoff — Resuming AI Refinement in a Fresh Session

How `ai-refinement` hands its own progress from a session running low on
context budget (per the `context_budget_awareness` house amendment,
`reference/ai-refinement-hybrid.md`) into a fresh session that continues the
same flow. This is a different problem from
`icp-flows/documentarian/reference/ai-refinement-handoff-contract.md`, which
carries *candidate work items* from one flow into another's intake. This
document carries *this flow's own progress* — items already committed, items
mid-draft, and what the agent already knows about the ones not yet started —
so a fresh session can pick up without re-deriving anything, following the
same mirroring-protocol §5 handoff shape (state, never instructions).

## When this fires

The `context_budget_awareness` amendment's highest threshold (context usage
past 80%): the agent stops proposing further work in the current session,
states a concrete split of what can still be finished reliably here versus
what should move to a fresh session, and produces this document. It may also
be requested directly by the user at any point below that threshold ("give me
a handoff now") — the document shape is identical either way; only the
trigger differs.

## Package shape

One file per handoff, `handoffs/YYYY-MM-DD-ai-refinement-session-<n>.md` at
instantiation (mirroring-protocol §5 naming):

```markdown
---
id: ai-refinement-session-handoff-<date>
type: clipping            # records state; not itself reviewed work
truth-level: claimed
source: human+ai
owner: <human driving the session>
data-class: internal
---

# Handoff: ai-refinement — session continuation

**From:** <stage the session stopped at> (Rovo | Copilot, <engine session
context, e.g. Confluence space / chat>)
**Context usage at handoff:** ~<percent>% (self-reported at the stop point)

## State

**Session mode:** <full-interactive | fast-track | bulk creation>. Work-item
type(s) in play: <type(s)>. Stakeholder register loaded: <yes/no, domain>.

**Completed this session** — one line per item already committed:
- <work-item type> <key> — <one-line summary> — <URL>

**In progress — the item or batch the session stopped mid-way through:**
- **Stage reached:** <stage number and name>
- **Fields already confirmed:** <field: value, cited to source, for every
  field settled before the stop>
- **Fields still open:** <field names with whatever partial context exists —
  never fabricated to look more complete than it is>
- **For a bulk-creation pass specifically:** which sub-batches (per
  `bulk-child-creation` step 10) completed, which sub-batch was in flight,
  and the running result table as of the stop point.

**Not yet started** — items named or implied but not yet reached, in the
priority order the agent recommends for the fresh session:
1. <item description> — <why this ordering: dependency, size, risk, or
   the user's own stated priority>

## Open questions / operator decisions pending

<anything the receiving session must not decide on its own — an ambiguous
set-versus-item reading left unresolved, a parent not yet confirmed, a due
date not yet elicited>
```

## Rules

- **The handoff carries state, never instructions** (mirroring-protocol §5) —
  the receiving session re-enters at the named stage using that stage's own
  `CONTEXT.md` as its contract; this document is not a substitute
  instruction set.
- **Nothing here is re-derived by the fresh session as if new.** Completed
  items are restated from their actual committed content (keys, URLs),
  never redrafted. Confirmed fields are carried forward as confirmed, not
  re-elicited. Open fields stay open — the fresh session resumes the
  pipeline's existing elicitation for them, it does not invent values to
  close the gap.
- **The priority recommendation is a proposal, not a decision.** The fresh
  session states it plainly and lets the user confirm, reorder, or drop
  items, the same way every other agent-proposed ordering in this pipeline
  works.
- **A bulk-creation in-flight sub-batch is never silently resumed into the
  next sub-batch.** Per `bulk-child-creation` step 10, a resume picks up
  exactly at the point of failure or stop — this document records that point
  precisely rather than approximately.
- **The package names its human owner**, the person carrying it into the
  fresh session — delivery is to the user, never an automated session
  hand-off.
- **Data-class stays internal**, matching the rest of the pipeline; the same
  screening that applied to the source material at intake still governs what
  can appear in this document.

## Changelog

- **1.0** (2026-08-05) — Initial build, alongside the
  `context_budget_awareness` house amendment it serves as the handoff target
  for. Modeled structurally on `ai-refinement-handoff-contract.md` (frontmatter
  + package shape + rules) but resumption-shaped rather than
  transfer-shaped: that contract carries candidate items *between* flows,
  this one carries *this flow's own progress* across a session boundary.
  `truth-level: to-review` — house-authored, pending operator sign-off; not
  run on-engine. See
  `decision-log/2026-08-05-bulk-batch-chunking-and-context-budget-awareness.md`.
