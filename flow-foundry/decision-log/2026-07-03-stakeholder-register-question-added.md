---
id: decision-2026-07-03-flow-stakeholder-register-question-added
title: "Decision Log — Stakeholder Register Availability Question Added to Setup Questionnaire"
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
  - "[[flow-foundry-spec]]"
  - "[[ai-refinement]]"
---

# Decision Log — 2026-07-03 — Stakeholder Register Question Added

**What was decided:** add a ninth setup-questionnaire question to
`flow-foundry/foundry-spec.md` §2 — "is a stakeholder register available for
this domain?" — with the ungrounded-mode fallback noted as the consequence
of deferring it. **By whom:** agent, on operator instruction, generalizing a
pattern from the `ai-refinement` flowspace's REC-06 implementation
(`icp-flows/ai-refinement/decision-log/2026-07-03-stakeholder-register-domain-split.md`)
into the foundry's standard intake. **What it affects:** `foundry-spec.md`
(1.3 → 1.4, changelog entry, questionnaire renumbered eight → nine
questions).

## Why this generalizes rather than staying flowspace-specific

`ai-refinement` is not the only flowspace likely to depend on a stakeholder
or requirements-source register — any flowspace grounding elicitation in a
"whose needs define this" register faces the same question `ai-refinement`
faced: what happens when no register exists yet for the target domain. Since
the foundry's setup questionnaire is exactly the mechanism for surfacing
this kind of dependency before scaffolding begins (per `foundry-spec.md` §2's
existing framing — "answered, or consciously deferred, with a note"), adding
the question here means future flowspaces inherit the ungrounded-mode
fallback pattern by default instead of each one rediscovering the gap
`ai-refinement`'s drift analysis found.

## Decisions and alternatives

1. **Question, not a mandatory gate.** The new question can be "consciously
   deferred, with a note," consistent with how the other eight questions
   already work — it does not block scaffolding a flowspace that doesn't
   have a register ready yet. *Alternative considered:* make register
   availability a hard prerequisite for any flowspace design involving
   stakeholder elicitation — rejected, since ungrounded mode is a legitimate,
   documented fallback, not a failure state to gate against.
2. **Referenced the consequence, not just the question.** The question's
   text explicitly names the fallback ("stakeholder-dependent stages will
   run in ungrounded mode") rather than leaving the implication for the
   flowspace designer to work out — matching how question 4 (Confluence
   Mermaid macro) already states its own fallback ("diagram: see mirror")
   inline.

## Assumption (operator to confirm or amend)

- **J1 — this question applies narrowly to register-dependent flowspaces.**
  Most flowspaces won't need a stakeholder register at all; this question is
  answered "not applicable" for those, the same way question 7 (Layer-3
  status per stage) can be answered per-stage with "not applicable" stages
  mixed in. Amendment path: if in practice this question causes confusion
  for non-register flowspaces, reword it to make the "not applicable" answer
  more prominent.
