---
id: decision-2026-07-03-fast-track-mode
title: "Decision Log — Fast-Track Mode (REC-08)"
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
  - "[[ai-refinement-hybrid]]"
  - "[[context-elicitation]]"
  - "[[scope-dependency-mapper]]"
  - "[[field-refinement-cadence]]"
  - "[[jira-commit]]"
---

# Decision Log — 2026-07-03 — Fast-Track Mode

**What was decided:** add an optional fast-track mode, selected at Stage 01,
that lets Stages 02–05 draft fields directly from structured source material
(with citation) instead of eliciting everything one field at a time —
implementing drift-analysis recommendation REC-08, at a design the operator
negotiated and approved before implementation (see "Design negotiation,"
below). **By whom:** agent, on operator instruction, after an explicit design
discussion resolving how fast-track interacts with the flowspace's existing
"non-negotiable" one-field-at-a-time cadence. **What it affects:** every
stage `CONTEXT.md` (01 through 06), `HUB.md` (stage table footnotes, taxonomy
intro, run procedure), and three skills — `context-elicitation`,
`scope-dependency-mapper` (carve-out only), and `field-refinement-cadence`
(the skill whose entire premise — "walks fields one at a time" — required a
description-level rewrite to "conditionally scoped").

## The gap this closes

REC-08 in the drift analysis: the flow requires six explicit stage boundaries
with heavy review at Stages 1, 2, and 6, plus per-field confirmation within
Stage 04 — proportional to risk for a vague idea, but disproportionate
ceremony when a user hands over a detailed, structured document that already
answers most fields. The stated end-state goal ("any user hands an intake
document to Rovo, and the flow produces a committed work item end-to-end")
is achievable but slower and more repetitive than it needs to be for
well-formed inputs.

## Design negotiation (recorded because it shaped every downstream edit)

Before implementation, the operator and the agent worked through how
fast-track mode could coexist with two already-hard-won constraints:
`field-refinement-cadence`'s description of `confirm_each_step: true` as
"non-negotiable," and the NEADD-1827-driven rule that due dates and parent
mappings are never silently assigned. The resolved design, confirmed by the
operator before any file was touched:

1. Stage 01 assesses fast-track eligibility and proposes it with a stated
   rationale (which fields look extractable, from where); the user always
   makes the final mode choice and can force full-interactive regardless of
   the agent's assessment.
2. Stages 02–04 in fast-track draft every field they can from source
   material, with a citation to where it came from; anything not
   confidently draftable falls back to one-at-a-time elicitation — never
   left blank or guessed.
3. Four hard carve-outs never fast-track, in any mode: `due_date` elicitation
   (Stage 04), Stage 06's parent-mapping confirmation, Stage 02's
   stakeholder sweep, and Stage 03's coalition/conflict-axis annotation. The
   first two were already-established rules from the NEADD-1827 revision;
   the latter two were added at the operator's explicit request during
   design negotiation, reasoning that misidentifying a stakeholder or a
   conflict costs more downstream than a wording tweak would.
4. Stages 03–05's review consolidates into one draft-and-review checkpoint
   in fast-track mode. Stages 01 and 02 (heavy) and Stage 06 (heavy) never
   compress, in any mode.

This negotiation is recorded here in more depth than a typical decision-log
entry because the resulting design was implemented literally as agreed,
across every touched file — a future reader auditing why, say, Stage 02's
stakeholder sweep is marked "hard carve-out" should find the reasoning here,
not have to reverse-engineer it from the stage contract alone.

## Decisions and alternatives

1. **Cadence reframed as conditionally scoped, not replaced.**
   `field-refinement-cadence`'s description and Method were rewritten so the
   one-at-a-time cadence and fast-track's consolidated presentation are two
   modes of the same accountability mechanism (an explicit confirmation per
   field), not a cadence skill plus a separate bypass. *Alternative
   considered:* leave the skill's one-at-a-time framing untouched and treat
   fast-track purely as a Stage 01–04 CONTEXT.md-level behavior invisible to
   the skill spec — rejected, since the skill's own description
   ("non-negotiable") would then directly contradict what Stage 04 actually
   does in fast-track mode, reintroducing exactly the kind of contract/skill
   drift the NEADD-1827 revision fixed for Stage 06.
2. **Consolidation is Stages 03–05 only, anchored at Stage 05.** Rather than
   each of Stages 03, 04, 05 independently deciding what "consolidated"
   means, Stage 05's Review section is the single canonical definition all
   three stages point back to — avoiding three slightly different
   descriptions of the same checkpoint drifting apart over future edits.
3. **Type auto-detection bundled into the same Stage 01 step as mode
   selection**, since both are assessments of the same source material,
   done at the same point in the flow, and both end in a user
   confirm/override — splitting them into separate steps would have doubled
   a very similar interaction pattern.

## Assumptions (operator to confirm or amend)

- **H1 — heavy-stays-heavy, light-consolidates is the correct read of
  REC-08.** REC-08's original text protected Stage 1 and Stage 6's review
  intensity explicitly but didn't mention Stage 2. This implementation
  infers Stage 2 also stays independently heavy (it's heavy, not light) and
  is not folded into the Stage 03–05 consolidation — confirmed with the
  operator during design negotiation, but flagged here since it required an
  inference beyond the recommendation's literal text.
- **H2 — fast-track's confidence assessment is qualitative, not a scored
  threshold.** Stage 01 "assesses whether the intake document is
  detailed enough" — this is deliberately left as a judgment call for the
  agent to make and state a rationale for, not a numeric confidence score
  with a cutoff. Amendment path: if this proves inconsistent across runs,
  a more mechanical rubric could be added as a follow-up revision.
