---
id: decision-2026-07-15-value-decomposition-brief-relocation
title: "Decision Log — Value-Decomposition Primer Brief Relocated to completed-skill-starters"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-value-decomposition]]"
  - "[[value-decomposition]]"
  - "[[decision-2026-07-15-value-decomposition-skill-gate-prerun]]"
---

# Decision Log — 2026-07-15 — Value-Decomposition Primer Brief Relocated

**What was decided:** move `sp-value-decomposition.md` from
`backlog-skill-starters/` to `completed-skill-starters/`, bumping its
`truth-level` to `verified` (artifact-version 1.0 → 1.1). **By whom:**
agent, on operator instruction ("make sure the completed ones have their
sp- files moved to completed skill starters"). **What it affects:** the one
brief file; the skill itself is untouched.

**Why this is a completion of an existing promotion, not a new one:** the
operator promoted the `value-decomposition` skill to
`../../produced-skills/` at `truth-level: verified` earlier today (repo
commit `c6f0672`, "Promoted skills", 2026-07-15 — the operator's own
commit, alongside the same session's `scope-dependency-mapper` and
`context-elicitation` stamps), following the agent-side pre-run recorded in
`2026-07-15-value-decomposition-skill-gate-prerun.md`. Per
`foundry-spec.md` §4/changelog 1.4, the primer brief moves to
`completed-skill-starters/` at the same moment as promotion; that
relocation was missed in the promotion commit. This entry, together with
the promotion commit it cites, is the review-evidence record (provenance
rule 5) behind the brief's `verified` stamp. All other promoted skills'
briefs were already in `completed-skill-starters/`; this was the only
straggler.
