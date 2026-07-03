---
id: decision-2026-07-03-structure-correction
title: "Decision Log — AI Refinement Structure Correction"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
---

# Decision Log — 2026-07-03 — Structure Correction

**What was decided:** rebuild the `ai-refinement` flowspace to house standard and
author its five demanded skills. **By whom:** agent, on operator instruction;
all artifacts emitted at `to-review` — nothing promoted. **What it affects:**
the flowspace tree, the skill-foundry backlog, and both foundries' queues.

## Deviations corrected (each was a validation-gate failure)

1. **Location** — the flowspace sat at the repo root (`ai-refinement/`), outside
   any foundry queue. Moved to `flow-foundry/backlog-flow-starters/ai-refinement/`.
   *Alternative considered:* `completed-flowspaces/` — rejected: that folder is
   human-placed only and the flowspace is `to-review`. The backlog is where
   in-progress foundry output stages (mirroring the skill-foundry's "land it in
   the backlog at to-review" rule).
2. **Stage shape** — stages were flat files (`01-…--CONTEXT.md`); the scaffold and
   mirroring protocol §2 require numbered folders (`01-<slug>/CONTEXT.md`). Rebuilt.
3. **Queue hygiene** — five `skill-*-brief.md` files lived inside the flowspace and
   stage contracts pointed at a nonexistent `skill-demand/` folder. Refiled as
   `sp-<slug>.md` primer briefs in `skill-foundry/backlog-skill-starters/` per the
   demand loop; stage contracts now point at the built skills.
4. **Folder conventions** — `decision-log--<date>-<slug>.md` and `reference--….md`
   flat files became `decision-log/YYYY-MM-DD-<slug>.md` and `reference/` per the
   scaffold and governance §5.
5. **Public-repo compliance** — artifacts carried `data-class: internal`
   frontmatter, invalid here (provenance rule 6), and Stage 01 embedded an internal
   Confluence URL. Frontmatter set to `public` (the *documents* are sanitized
   design; the *instance* data boundary stays `internal` inside the contracts) and
   the URL redacted with a restore-at-instantiation note. Named owner replaced
   with `operator` per the repo's no-personal-data rule.
6. **Contract quality** — Verify fields were completeness checklists, not the
   required cross-stage trace checks. Each now names the stages, artifact, and
   property traced, and logs its result.

## Assumptions (operator to confirm or amend)

- **A1 — Staging location.** In-progress flowspaces live in
  `backlog-flow-starters/` until the operator promotes them; the foundry never
  creates a third "in-progress" folder without operator ratification.
- **A2 — Built skills land in the skill-foundry backlog** (spec §4) as
  `<slug>/SKILL.md` + `adapters/`, beside their `sp-` briefs, which are kept as
  the demand record.
- **A3 — `work/` and `handoffs/` folders are instantiation-time artifacts.**
  They hold only per-run content, so the sanitized public design omits them
  (noted in `HUB.md` § Surfaces).
- **A4 — Stakeholder register is public-safe and in-scope.** It self-declares
  generic team names; ingested as a `claimed` clipping and woven into the design:
  Stage 02 tags stakeholders (register usage rule 1), Stage 03 annotates
  coalition/conflict-axis with decision-owner or escalation routing (rules 2–4),
  Stage 06 commits the tags as Jira labels. The Jira schemas from the source doc
  stay authoritative — no new required fields were invented.
- **A5 — Schema extension flag.** `type: stage-context` (with `stage` and
  `review-intensity` fields) is used by stage contracts but absent from the
  provenance spec's type enum. Foundries don't extend the schema — flagged here
  for the operator to ratify a `stage-context` row in `provenance-spec.md`.
- **A6 — Decision-log truth-level.** The type enum defaults decision logs to
  `verified` (they record events), but agents never emit `verified`; these are
  stamped `to-review` for the operator to promote.
- **A7 — Skill naming.** Skill ids drop the redundant `skill-` prefix
  (`context-elicitation`, not `skill-context-elicitation`) to match the house
  pattern of `sp-<slug>` briefs producing `<slug>/SKILL.md` folders.
- **A8 — Diagram colors.** Stages 2–6 now render true review-intensity colors
  rather than `gap` rose: the guide defines `gap` as "the stage's skill doesn't
  exist yet," and the skills now exist (at `to-review`).
