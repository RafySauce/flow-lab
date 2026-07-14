---
id: decision-2026-07-03-stakeholder-register-domain-split
title: "Decision Log — Stakeholder Register Split Into Template + Instance (REC-06)"
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
  - "[[platform-stakeholder-register]]"
  - "[[context-elicitation]]"
  - "[[scope-dependency-mapper]]"
---

# Decision Log — 2026-07-03 — Stakeholder Register Domain Split

**What was decided:** split the stakeholder register into a domain-neutral
template (`reference/platform-stakeholder-register-template.md`, new) and the
existing 17-entry register, explicitly relabeled as the network-engineering
instance of that template — implementing drift-analysis recommendation
REC-06 at the "full split" depth the operator selected. **By whom:** agent,
on operator instruction. **What it affects:** new
`reference/platform-stakeholder-register-template.md` (1.0, `to-review`),
`reference/platform-stakeholder-register.md`'s ingest note (1.0 → 1.1,
relabeled, content below the note untouched), Stage 01 (new grounding-check
step), Stage 02 and Stage 03 (ungrounded-mode conditionals), and
`context-elicitation` and `scope-dependency-mapper` (matching ungrounded-mode
conditionals in their Method sections), plus `flow-foundry/foundry-spec.md`
(new setup-questionnaire question).

## The gap this closes

DRIFT-03 in the drift analysis: the source document says nothing about
stakeholders, but the flow's entire stakeholder-register integration
(Stages 02, 03, 06) is hardcoded to a 17-entry, network-engineering-specific
register. For the stated goal ("any user hands an intake document to Rovo"),
a user outside network engineering would get irrelevant register entries
with no fallback.

## Decisions and alternatives

1. **Template + instance, not a single generalized register.** The template
   holds structure only (role-types, a placeholder stakeholder table,
   placeholder alignment/conflict sections, the same escalation-rule shape);
   the network-engineering register becomes one instance of it, explicitly
   labeled as such. *Alternative considered:* generalize the existing
   register's entries into abstract categories usable across domains —
   rejected, since abstracting real entries into placeholders loses the
   worked-example value the current register provides, and a new domain
   still needs its own concrete entries either way.
2. **Ungrounded mode, not a hard block.** When no register is loaded for a
   domain, Stages 02/03 (and the skills that implement them) ask the user
   directly instead of walking a register, rather than refusing to proceed.
   This is a degraded but functional path, matching the operator's stated
   goal that "any user" should be able to run the flow, including in domains
   with no register authored yet.
3. **Skill-level conditionals added alongside the stage-level ones.** The
   register-walking logic lives in `context-elicitation` (Stage 02) and
   `scope-dependency-mapper` (Stage 03), not just their stage contracts —
   so both layers needed the same conditional for the fallback to actually
   take effect, not just be documented at the contract level with no
   matching skill behavior.
4. **Foundry-level generalization.** `flow-foundry/foundry-spec.md`'s setup
   questionnaire gained a ninth question (stakeholder register availability)
   so future flowspaces with a similar dependency inherit this pattern by
   default, rather than each one rediscovering the same gap independently.

## Assumption (operator to confirm or amend)

- **G1 — the template's placeholder shape is domain-agnostic enough.** The
  template assumes every domain's register will want the same six sections
  (role-types, stakeholder table, alignment, conflict, escalation-path
  definition, usage rules). Amendment path: if a domain's real structure
  needs a section this template doesn't anticipate, extend the template
  itself rather than diverging in a one-off instance.
