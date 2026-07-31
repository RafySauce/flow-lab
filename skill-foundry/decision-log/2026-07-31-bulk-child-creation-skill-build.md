---
id: decision-2026-07-31-bulk-child-creation-skill-build
title: "Decision Log — bulk-child-creation Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-31
updated: 2026-07-31
owner: operator
source: human+ai
data-class: public
related:
  - "[[bulk-child-creation]]"
  - "[[sp-bulk-child-creation]]"
  - "[[ai-refinement]]"
  - "[[jira-commit]]"
  - "[[value-decomposition]]"
---

# Decision Log — 2026-07-31 — bulk-child-creation Skill Build

**What was decided:** build `bulk-child-creation` from a primer brief written
the same day, and stage it in `review-skills/` at `truth-level: to-review`.
**By whom:** agent, on direct operator instruction (the operator described the
capability and answered the four design questions before authoring began).
**Triage classification:** skill-primer-brief — clean path. The intent was
crystallized by the operator in conversation, captured as
`backlog-skill-starters/sp-bulk-child-creation.md`, and transcribed into the
spec without re-opening settled exploration.

The flowspace-side rationale — why the capability exists, the two carve-out
narrowings, and the anti-fabrication reasoning — lives in
`icp-flows/ai-refinement/decision-log/2026-07-31-bulk-creation-mode.md`. This
log records the build decisions only.

## Build decisions

1. **A skill, not a mode flag on the existing pipeline.** The deciding factor
   was step 5's stop-at-the-evidence rule. In single-item refinement, a field
   the agent cannot draft enters the elicitation queue and the user answers
   it; there is no analogue for "stop generating, report the item as
   underspecified, and let the user drop it." That behavior — plus set
   ingestion, batch review vocabulary, and the halt-on-failure creation
   loop — is enough distinct method to carry its own spec, its own review
   criteria, and its own boundary list.

2. **The spec carries the near-miss it is most likely to fail.** Standard
   house practice puts near-misses in Triggering intent; here the
   set-versus-item test also appears in Method step 2 with a worked example,
   because it is a *behavior* the skill executes rather than only a routing
   condition. The worked example (three switch upgrades versus one upgrade's
   four scope lines) is drawn from the network-engineering domain the
   flowspace's stakeholder register already assumes.

3. **Review criterion 5 is written as a run-failing criterion.** Most review
   criteria describe an acceptable output. Criterion 5 — no item padded past
   its evidence — is phrased to fail a run outright if violated, because a
   batch that looks complete and is partly invented passes every other
   criterion on the list.

4. **Suggested items modelled as a second, labelled set rather than flagged
   items in one set.** Structural separation survives review, validation, and
   creation; a per-item flag does not survive a user copying the list into
   something else. Stage 05 and Stage 06 both carry the separation forward
   explicitly.

5. **The degrade path produces a document, not a stalled run.** Extends the
   existing pattern (`jira-commit` 1.8's preview-only terminal output,
   `START-HERE.md`'s capability probe) rather than inventing a new one. The
   handoff document is specified with enough structure — one section per item,
   fields under their schema names, labels, intended parent, underspecified
   rows, suggested set kept separate — that a fresh session can finish the job
   without re-deriving anything.

6. **Adapters add format, not logic.** Both are mechanical translations of the
   twelve Method steps. Rovo is the primary target per the operator's stated
   requirement that native MCP tooling be reached for first, and its
   Permitted-actions section explicitly denies bulk edit, transition, close,
   and delete on existing issues — the boundary that keeps this skill from
   drifting into the portfolio-operations space. Copilot runs the same method
   through the sanctioned Jira integration.

7. **Collision check, run at authoring time.** Three neighbors, each named in
   the spec's boundary list with the line drawn:
   - `value-decomposition` decides *what* the children should be (vertical
     slices, MVP bounding); this skill takes a settled set and builds it. A
     spreadsheet of tasks reaches this skill directly.
   - `jira-commit` remains the only writer and the commit boundary; this skill
     drives it per item rather than replacing it. Its boundary was amended
     the same day (1.9 → 1.10) so the two specs agree on where bulk import
     stops and bulk creation starts.
   - `jira-portfolio-ingest` reads portfolios and writes nothing; this skill
     creates and never edits existing issues. No overlap, but both touch
     CSV/XLSX parsing, so the parsing contract is cited from one place rather
     than restated differently in two.

8. **Parsing rules cited, not duplicated.** The quote-honoring parse, header
   capture, repeated-column collapse, and item-count confirmation come from
   `review-flowspaces/portfolio-rationalization/reference/export-and-field-requirements.md`
   §6 and `review-skills/jira-portfolio-ingest/SKILL.md`. Both are unpromoted
   `to-review` artifacts, which the spec notes — this cites a design, not a
   verified capability. If `portfolio-rationalization` is never promoted, the
   rules need a permanent home; flagged to the operator in the flowspace log.

## Five-point gate — status

Not run. Per `foundry-spec.md` §5 the gate is the operator's, and this build
stops at staging. Owed for promotion:

1. **Spec review** — purpose, triggering intent (including the near-misses),
   boundaries, review criteria, and Flow Diagram one-for-one with Method
   prose, with Mermaid rendering confirmed on GitLab.
2. **Live test per adapter** on `public`/synthetic data — a synthetic sheet
   with a deliberately ambiguous row, a row naming a different parent, and a
   row missing a required field would exercise the criteria that matter most.
3. **Trigger check** — fires on set-shaped input; does *not* fire on one
   complex item with many scope bullets, a two-item meeting-minutes set, a
   bulk-edit request, or a single item wanting real refinement.
4. **Collision check** — as above, re-verified against the amended
   `jira-commit` 1.10 and `value-decomposition` 1.1.
5. **Promotion** — moving the folder to `produced-skills/`, moving the primer
   brief to `completed-skill-starters/`, and bumping both to `verified`.

Nothing here has run on-engine.
