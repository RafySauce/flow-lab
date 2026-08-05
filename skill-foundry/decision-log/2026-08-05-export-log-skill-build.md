---
id: decision-2026-08-05-export-log-skill-build
title: "Decision Log — export-log Skill Build"
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
  - "[[export-log]]"
  - "[[sp-export-log]]"
  - "[[ai-refinement]]"
---

# Decision Log — 2026-08-05 — export-log Skill Build

**What was decided:** build `export-log` from the primer brief filed the
same day, and stage it in `review-skills/export-log/` at
`truth-level: to-review`, per `foundry-spec.md` §§2–4. **By whom:** agent,
following an operator-approved plan that named this skill explicitly as one
of four deliverables from a chat discussion of two ai-refinement improvement
ideas — the operator instruction chain (rule 2's confirmation) runs through
that plan approval rather than a separate in-repo request. **Triage
classification:** skill-primer-brief — clean path. The brief
(`backlog-skill-starters/sp-export-log.md`) carries crystallized Purpose,
Triggering intent, a seven-step Method sketch, known failure modes,
inputs/data boundary, and a Definition of done; this build transcribes it
into the engine-neutral spec and adapters without re-opening the
exploration.

The brief stays in `backlog-skill-starters/` as the intake record, per
`foundry-spec.md` §4 — it moves to `completed-skill-starters/` only at
promotion, alongside the skill itself.

## Build decisions

1. **The open placement question is resolved toward "hand off, don't
   file"** — the primer brief's own Demand-source section already flags this
   as unsettled from the chat that produced it. Rather than guess at an
   automatic destination (e.g., writing straight into a decision-log or
   `HUB.md` gap log), the skill is built to produce a standalone document and
   say plainly that placement is a human decision. This is the option most
   consistent with two rules already governing every other skill in this
   repo — `AGENTS.md` rule 5 (the verified/placement gate is human) and rule
   7 (propose structure, don't mint it) — rather than a novel exception
   carved out for this one skill. Flagged explicitly for the operator to
   confirm or redirect at review; this is the single largest assumption in
   the build.
2. **Scoped repo-wide, not folded into `ai-refinement`.** The demand was
   explicitly for something "invoked by anyone who wants to provide
   feedback," on any flow — building it as an `ai-refinement`-only skill
   would have contradicted the brief's own stated scope. It is staged
   without wiring into any flow's Stage 01 (there is no natural single
   flow to wire it into), reachable directly by its own trigger phrases
   instead, the same access pattern `START-HERE.md` already uses for
   flow/skill discovery in a bare chat session.
3. **No repo cataloging yet.** Not added to `produced-skills/CONTEXT.md` or
   `AGENTS.md`'s routing tables — both list only promoted, `verified` work,
   matching how `bulk-child-creation` and `process-decomposition` were
   likewise absent from those surfaces while staged. Cataloging is a
   promotion-time act, not a build-time one.
4. **Anti-fabrication carried over as the skill's own load-bearing rule**,
   the same house pattern `bulk-child-creation` established for batch
   drafting: an uneventful or unremarkable session must produce a short,
   honest export ("not observed") rather than a padded one invented to look
   substantive. Review criterion 3 is the gate this fails outright if
   violated, mirroring `bulk-child-creation`'s review criterion 5.
5. **No collision found.** Checked against every skill with an
   session-summary-shaped output (`ai-refinement` Stage 06's session
   summary) and against `documentarian` (which produces committed
   Confluence documentation, a different artifact entirely). Both boundaries
   are stated explicitly in the spec's "What this skill is not" rather than
   left implicit, since a session-summary-shaped output is the nearest
   plausible overlap. No existing skill or stage needed a cross-reference
   added — this skill only ever reads a session that already happened; it
   writes into nothing another skill owns.
6. **Adapters add format, not logic.** Both are mechanical translations of
   the seven Method steps; the refusal set (decline to replace a flow's own
   session summary, decline to dump a raw transcript, decline to file the
   export itself) is identical across both, matching the pattern
   `bulk-child-creation`'s and `process-decomposition`'s adapters already
   use.

## Five-point gate — status

Not run. Per `foundry-spec.md` §5 the gate is the operator's, and this build
stops at staging. Owed for promotion:

1. **Spec review** — purpose, triggering intent (including the near-misses
   against a flow's own session summary and a raw transcript dump),
   boundaries, review criteria, and Flow Diagram one-for-one with Method
   prose.
2. **Live test per adapter** — a session with genuine friction to export
   (exercises steps 3–5 meaningfully) and a second, uneventful session
   (exercises the "not observed" anti-fabrication path) would together cover
   the skill's main behavior.
3. **Trigger check** — fires only on explicit request; does not fire
   automatically at session close, and does not activate in place of a
   flow's own session summary when one exists.
4. **Boundary/collision check** — re-verify against any flow gaining its own
   session-summary-shaped output after this build.
5. **Promotion, and the placement question.** Moving the folder to
   `produced-skills/`, the primer brief to `completed-skill-starters/`, and
   both to `verified` — plus the operator's explicit ruling on build
   decision 1 above, since it was resolved by inference rather than direct
   instruction and is the one design choice in this build most likely to be
   overturned at review.

Nothing here has run on-engine.
