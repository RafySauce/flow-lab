---
id: decision-2026-08-05-bulk-batch-chunking-and-context-budget-awareness
title: "Decision Log — Bulk Batch Chunking and Context-Budget Awareness"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[bulk-child-creation]]"
  - "[[session-continuation-handoff]]"
---

# Decision Log — 2026-08-05 — Bulk Batch Chunking and Context-Budget Awareness

**What was decided:** two related additions to the `ai-refinement` flowspace,
both raised directly by the operator from a real Rovo run. First,
**sub-batch chunking** in `bulk-child-creation`: sets larger than ten items
are split into sequential sub-batches of at most ten before creation starts,
each sub-batch's create actions assembled and issued as one consolidated
pass. Second, a revision-in-place of the eleventh house amendment,
**`session_budget_checkpoint`**: the agent self-reports its context-window
usage at every stage boundary and after every bulk sub-batch, with
escalating advisories at 50/60/70% used and a stop-and-handoff response past
80%, backed by a new reference artifact,
`reference/session-continuation-handoff.md`. **By whom:** agent, on direct
operator instruction. **What it affects:** `bulk-child-creation` (1.0 → 1.1,
both adapters regenerated), `reference/ai-refinement-hybrid.md` (1.7 → 1.8),
a new `reference/session-continuation-handoff.md` (1.0), all six stage
`CONTEXT.md` files (light touch — one Process step and one Verify item
each), and `HUB.md` (1.22 → 1.23).

## Merge reconciliation with PR #47

This work was built on a branch cut from `main` before PR #47
("Incorporate Rovo session friction report into ai-refinement flow") merged.
That PR turned out to draw from an **independent operator report of the
same 2026-08-04 Rovo session incident**, and had already added a
`session_budget_checkpoint` house amendment (eleventh, ninth-through-eleventh
batch) covering much of the same ground as the `context_budget_awareness`
amendment originally designed here — a single 70%-usage warn-and-offer with
an inline-specified handoff document. Bringing this branch up to date against
`main` surfaced the collision as a real merge conflict, not just a line-level
one.

Resolved by reconciling rather than duplicating: `context_budget_awareness`
was withdrawn as a would-be ninth amendment, and its escalating-threshold
design (50/60/70/80%, per-stage self-report marker) was merged into
`session_budget_checkpoint` as an in-place revision instead — the same
pattern this flowspace already uses when a later operator ask refines an
existing amendment rather than justifying a new one (e.g.
`supporting_context_research`'s 1.6 revision). The handoff document's shape
moved out of the amendment's inline prose into the dedicated
`reference/session-continuation-handoff.md` this branch had already built,
which is additive to PR #47's design rather than competing with it. The
`bulk-child-creation` sub-batch chunking fix is unrelated to anything PR #47
touched and merged without incident. `HUB.md`'s gap log entry for this work
is renumbered Fourteenth (PR #47's is Thirteenth, and merged first) and
rescoped to describe only what PR #47's fixes didn't already cover, rather
than re-describing the shared incident from scratch.

## The gap this closes

The operator ran `bulk-child-creation` live in Rovo and hit two problems in
the same session, both traced to the same underlying cause: nothing in the
pipeline anticipated the limits of a single Rovo context window.

1. **Batch creation had no size ceiling.** `bulk-child-creation` step 10
   created an approved set sequentially in one unbounded pass. Past roughly
   ten items, Rovo lost track mid-batch and self-corrected — in the
   operator's words, "I've lost the context, let me re-read and pass the ask
   as a single code block" — recovering only after manual, trial-and-error
   chunking assisted by a task-tracker agent. The failure mode was real and
   reproducible (the operator saw it complete at both 10 and 15 items,
   inconsistently), but nothing in the spec told the agent to expect it.
2. **Nothing surfaced context-window usage to the user.** Rovo runs on a
   200k-token Claude backend and can self-report usage when asked directly —
   the operator got "140/200" on request — but the pipeline never asked on a
   schedule, so a user had no way to tell a session was degrading until
   output quality had already started to suffer. There was also no way to
   hand a session's progress to a fresh one; the only existing handoff
   pattern (`documentarian`'s `ai-refinement-handoff-contract.md`) is shaped
   for passing candidate work items *between* flows, not for resuming *this*
   flow's own progress across a session boundary.

## Design decisions

1. **Chunk upfront rather than let the engine discover the limit mid-run.**
   The operator's own recovery — re-reading the set and re-issuing it as a
   single consolidated block — is exactly what step 10 now does by default,
   before creation starts rather than as an emergency correction partway
   through. This turns an ad hoc recovery into a designed behavior.
2. **Ten is a starting point, not a derived ceiling.** The operator's
   observation (sometimes 10 succeeded, sometimes 15) means this is a
   practical safe default, not a measured hard limit. The spec says so
   explicitly and allows a smaller chunk for unusually large per-item
   content, the same judgment call already applied to an unusually detailed
   single row.
3. **A sub-batch failure halts at the point of failure, not at the
   sub-batch or the whole set.** This mirrors the existing halt-on-failure
   rule exactly, just restated to be explicit that chunking doesn't change
   what "halt" means: no continuation into the rest of the current
   sub-batch, no silent advance into the next one, resume picks up exactly
   where it stopped.
4. **Session-budget awareness stays advisory, not a new gate.** The revision
   adds no creation or commit gate and narrows no other amendment — it only
   adds information (the usage marker) and, past the highest threshold, a
   firmer proposal (the handoff) that the user can still decline. This keeps
   it consistent with the existing amendments' pattern of stating a fact or
   requiring a confirmation, never silently blocking — and with
   `session_budget_checkpoint`'s own original design, which this revision
   sharpens rather than overrides.
5. **The usage marker is a direct self-report, not a heuristic.** The
   operator's own test — asking Rovo directly and getting "140/200" — showed
   the engine can already answer this question. The revised amendment asks
   it on a schedule (every stage boundary, every bulk sub-batch) rather than
   inventing a proxy signal (turn count, item count) that would need
   separate calibration and could drift from what the engine actually knows —
   consistent with the original `session_budget_checkpoint`'s own note that
   estimation is an agent-side judgment call, not a fixed formula.
6. **Three escalating thresholds, not one.** 50% is informational only —
   the marker itself is the signal. 60% and 70% add an explicit advisory
   that quality may be starting to degrade, recommending the user finish
   what's in progress before opening new scope. Past 80%, the agent stops
   proposing further work and produces a handoff instead. This graduated
   response avoids two failure modes: nagging the user from the first stage
   of every session, and saying nothing until the session is already
   unusable.
7. **The session-continuation handoff is a new artifact, not a reuse of the
   cross-flow contract.** `ai-refinement-handoff-contract.md` carries
   candidate work items *into* Stage 01 from another flow — its package
   shape (one block per candidate, problem-shaped) doesn't fit "resume this
   flow's own progress," which needs to carry completed items (with keys),
   an in-progress item's confirmed and open fields, a not-yet-started
   priority list, and — specifically for a bulk pass — exactly which
   sub-batch was in flight. Reusing the *pattern* (mirroring-protocol §5
   shape: frontmatter + package shape + rules) while giving it
   resumption-specific content avoided distorting the existing contract to
   serve two different purposes.
8. **Every touched stage gets the same one-line treatment.** Rather than
   rewriting each stage's Process section, the marker is added as a single
   short paragraph (or a numbered step, where the stage's Process is
   step-numbered) at the stage's exit, plus one Verify checklist item. This
   keeps the change auditable across all six files without restructuring
   stage contracts that didn't otherwise need to change.

## Truth-level movements

- `bulk-child-creation` drops `verified` → `to-review` (behavior change to
  step 10; re-gate owed alongside the existing Copilot-adapter live-test
  gap).
- `ai-refinement-hybrid.md` stays `to-review` (already dropped by PR #47's
  1.7; this pass's 1.8 revision doesn't change the truth-level, only the
  content of one amendment already pending sign-off).
- All six stage `CONTEXT.md` files stay `to-review` (already dropped by PR
  #47 for Stage 01/05/06's content changes; Stages 02–04 drop here for the
  first time, for the new Process step + Verify item this pass adds).
- `HUB.md` stays `to-review` (already dropped by PR #47; this pass adds the
  Fourteenth gap entry, reference-table, and footnote changes on top).
- `session-continuation-handoff.md` is new, staged at `to-review` —
  house-authored, pending the same operator sign-off as every other
  reference artifact in this flowspace.

## Remaining for the operator (the human gate)

1. **Confirm the ten-item default.** The operator's own observation was that
   the failure point wasn't a hard wall (10 sometimes succeeded, 15
   sometimes did too) — ten is a conservative starting point picked from
   "10 seems like a safe spot," not a derived ceiling. A live re-run at this
   chunk size is the way to confirm it holds.
2. **Confirm the 50/60/70/80% thresholds and their wording.** These were
   proposed to match the operator's own stated bands (50/60/70) plus a
   stop-and-handoff point (80%) that wasn't itself specified in
   conversation — the operator should confirm 80% is the right place to stop
   proposing new work rather than continuing with only an advisory.
3. **Run the five-point gate on the revised `bulk-child-creation`** (spec
   review, per-adapter live test, trigger check, collision check) — the
   chunking behavior has not been exercised on-engine.
4. **Run a live session past the 80% threshold** to confirm the handoff
   document (`reference/session-continuation-handoff.md`) actually contains
   what a fresh session needs to resume without re-deriving anything — this
   was designed from the existing cross-flow contract's pattern, not proven
   against a real degraded session.
5. **Decide whether the context-remaining marker's display cadence is too
   frequent.** Six stages plus every bulk sub-batch is a lot of visible
   status lines in a full-interactive run; the operator may want it
   condensed (e.g., shown only when it changes meaningfully) once it's been
   seen live.
