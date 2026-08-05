---
id: sp-export-log
title: "Skill Primer Brief — Export Log"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
data-class: public
related: ["[[ai-refinement]]"]
---

# Skill Primer Brief — Export Log

> Intake path 1 for the skill-foundry: crystallized intent, written before
> authoring starts. Filed in `skill-foundry/backlog-skill-starters/` as
> `sp-export-log.md`.

## Purpose

Captures a sanitized, standardized record of what happened in a working
session against any flow or skill in this repo — what ran, what friction
came up, what decisions got made, what came out of it — so a human can feed
it back into this repo's own improvement loop. Not scoped to
`ai-refinement`: any flow or skill session can be exported. Replaces the
current practice of feedback existing only as whatever the user happens to
remember and retype later, or not surfacing at all.

This is deliberately **not** an in-flow session summary. `ai-refinement`
Stage 06 already produces one of those (its own "session summary" output,
step 9) — unscrubbed, scoped to what was created, meant for the user and the
run's own decision log. This skill produces a different artifact: sanitized
for a public repo, scoped to what would help someone improve the *method*
itself, and never committed anywhere by the skill — a human decides where it
lands.

## Triggering intent

**Fires on** — an explicit, direct request from the user, at any point in a
session:

- "Export log," "export learnings," "export this session," "give me a
  feedback export," "log this for the repo."
- Typically at session end, or right after a friction point the user wants
  captured while it's fresh — either is a valid trigger, not just close-out.

Never fires unprompted. This skill does not run automatically at the end of
every session or flow pass — that would mean deciding on the user's behalf
that their session is worth writing up.

**Does not fire on (near-misses):**

- **A flow's own in-flow session summary** (e.g., `ai-refinement` Stage 06
  step 9, "Done → close session, produce session summary"). That summary is
  unscrubbed, scoped to what was created, and belongs to the run's own
  decision trail — this skill is a separate, sanitized, repo-facing export
  the user asks for on top of it, never a replacement.
- **A raw transcript dump.** This skill summarizes and screens; it never
  offers to paste the conversation verbatim as the "export."
- **Filing the export into the repo.** This skill produces a document; it
  never creates a decision-log entry, edits a `HUB.md` gap log, or files a
  new primer brief itself — see "What this skill is not."

## Method sketch

1. **Recognize the trigger and confirm scope.** The whole session, or a
   named portion of it ("just the batch-creation part"). State back what's
   being exported before drafting anything.
2. **Identify what ran.** Which flow(s), skill(s), and stage(s) were invoked
   this session — read from the session's own context, never guessed.
3. **Capture friction and decisions.** What didn't work as specified, what
   the user or agent had to work around, any deviation from a stage/skill's
   stated method and why. Cite the specific stage or skill each point
   traces to.
4. **Capture outcomes**, referenced rather than re-listed in full — "created
   12 Jira items via `bulk-child-creation`," not a re-drafted copy of the
   items themselves.
5. **Screen before drafting further.** Reuse the data-safety screening
   pattern already established in this repo (`bulk-child-creation` step 4,
   Stage 01's data-safety guardrail): strip personal names, customer
   references, hostnames, credentials, and any employer-identifying detail.
   Content that can't be confidently scrubbed is named as withheld, never
   guessed-and-included. Target ceiling: `public` — safe for this repo,
   which holds sanitized method only.
6. **Present the draft for review before finalizing.** The user can edit,
   drop a section, or decline the whole export — nothing is produced
   silently, matching the confirm-before-output pattern every other skill in
   this repo already uses.
7. **Output as a standalone Markdown document**, valid frontmatter per
   `methodology/provenance-spec.md`, handed to the user directly (in-session
   or as a file). The skill states plainly, in the document itself, that
   placement is a human decision: it may become a decision-log entry, a new
   `sp-<slug>.md` primer brief, or a flowspace `HUB.md` gap-log entry — the
   skill does not choose or write to any of those itself.

### Known failure modes to guard against

- **Filing itself.** The single most likely overreach: writing directly into
  a `decision-log/` or a `HUB.md` gap log because the shape looks close
  enough. That crosses the operator-only placement rule (`AGENTS.md` rule 5)
  that governs every other output in this repo.
- **Fabricating friction that didn't happen**, to make the export feel more
  complete. Anti-fabrication applies here exactly as it does in
  `bulk-child-creation`: say "not observed" rather than invent a plausible
  gap.
- **Under-scrubbing.** A session transcript is the highest-risk carrier this
  skill touches — worse than an exported spreadsheet, because it can carry
  anything the user typed. Screen before drafting, not after.
- **Treating this as the flow's own close-out.** It supplements a stage's
  existing session summary; it is never a substitute for one.

## Inputs and data boundary

Reads: only the current session's own conversation and context — which
flow/skill/stage ran, what was said, what was produced. Never fetches
external data, never reads other sessions.

Max data-class of the **produced output**: `public` — this repo holds
sanitized method and exemplars only, and this skill's whole purpose is
producing something safe to land here. The **source session** content may be
`internal` or higher; step 5's screen is what bridges the two, and it halts
rather than guesses when it can't confidently scrub something.

Engines: Rovo and Copilot, and also a bare chat session referencing this
repo directly (`START-HERE.md`'s degrade-path pattern) — nothing in the
method needs a live connector, since it only reads the session's own
context.

## Demand source

Raised directly by the operator, 2026-08-05, alongside the
`context_budget_awareness` house amendment: a general, repo-wide way for
anyone to export sanitized session learnings so they can feed back into
improving the flows and skills themselves, standardized rather than ad hoc.

The chat discussion that produced this brief did not settle exactly where an
export lands once produced — this brief resolves it toward "the skill hands
off a document, a human places it," the option most consistent with this
repo's existing operator-only placement rule (`AGENTS.md` rule 5) and its
default "propose, don't mint" practice (rule 7). Flagged for the operator to
confirm or redirect at review.

## Definition of done

1. Fires only on an explicit user request, never unprompted at session close
   or on a schedule.
2. Correctly identifies which flow(s)/skill(s)/stage(s) ran this session,
   citing the session's own context rather than assuming.
3. Every friction point or decision captured traces to something that
   actually happened in the session — nothing invented to round out the
   export.
4. The data-safety screen ran before the draft was presented, and anything
   that couldn't be confidently scrubbed is named as withheld, not guessed.
5. The user reviewed and could edit or decline the draft before it was
   finalized.
6. The output is a standalone, provenance-stamped Markdown document that
   explicitly states placement is a human decision — the skill itself wrote
   to no repo location.
7. Given a session with nothing notable to report, the skill says so plainly
   rather than padding the export to look substantive.
