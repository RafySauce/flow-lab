---
id: decision-2026-07-07-completed-starters-queue-formalized
title: "Decision Log — Completed-Skill-Starters Queue Formalized; Promotion Evidence Recorded for Contract Reviewer + Provenance Stamper"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[skill-foundry-spec]]", "[[sp-contract-reviewer]]", "[[sp-provenance-stamper]]"]
---

# Decision Log — 2026-07-07 — Completed-Skill-Starters Queue Formalized; Promotion Evidence Recorded

**What was decided:** two things, together. (a) Formalized
`skill-foundry/completed-skill-starters/` as the documented terminal home for
a primer brief once its corresponding skill is promoted to
`../produced-skills/` — `foundry-spec.md` §4 (changelog 1.4), `CONTEXT.md`,
and `backlog-skill-starters/CONTEXT.md` updated to state the rule; the seven
primer briefs already relocated there by hand
(`sp-context-elicitation`, `sp-contract-reviewer`, `sp-field-refinement-cadence`,
`sp-jira-commit`, `sp-provenance-stamper`, `sp-scope-dependency-mapper`,
`sp-workitem-validation`) had their `truth-level` bumped `to-review` →
`verified` to match. (b) Recorded the missing review evidence for
`contract-reviewer` and `provenance-stamper`: both were already sitting
uncommitted in `../produced-skills/` with `truth-level: to-review` and no
decision-log entry — this entry supplies that evidence per §5's "Evidence
recorded" requirement and both `SKILL.md` files are bumped to
`truth-level: verified`.

**By whom:** agent, on operator instruction, confirming the promotion of
`contract-reviewer` and `provenance-stamper` as already reviewed (the
operator had already moved both to `produced-skills/` in a prior session).

**Alternatives considered:** leaving the primer-brief relocation undocumented
(rejected — the working tree already diverged from the written spec, and the
docs should describe what actually happens); reverting the two skills to
`review-skills/` pending a fresh review (rejected — operator confirmed the
existing move stands, review evidence just needed to be logged, not redone).

**Review evidence (§5, five-point gate) — `contract-reviewer` and
`provenance-stamper`:**
1. Spec review — both specs carry purpose, specific triggering intent with
   named near-misses, explicit boundaries, usable review criteria, and a
   Flow Diagram, per `2026-07-07-foundry-support-skill-gate-prerun.md`'s
   agent-side pre-check.
2. Live test — confirmed by operator at promotion time.
3. Trigger check — confirmed by operator at promotion time.
4. Boundary/collision check — first pass run pre-build against the five
   `ai-refinement` skills and the two dropped starters (no overlap), per
   `2026-07-07-foundry-support-skill-batch.md`; re-confirmed at promotion.
5. Evidence recorded — this entry.

**What it affects:** `foundry-spec.md` (§4, changelog 1.4), `CONTEXT.md`,
`backlog-skill-starters/CONTEXT.md`, new `completed-skill-starters/CONTEXT.md`,
`AGENTS.md`, root `README.md`; frontmatter on the seven relocated primer
briefs and on `produced-skills/contract-reviewer/SKILL.md` and
`produced-skills/provenance-stamper/SKILL.md`. No further file moves — the
backlog, review-skills, and produced-skills placements themselves were
already correct in the working tree; this entry documents and stamps them.
