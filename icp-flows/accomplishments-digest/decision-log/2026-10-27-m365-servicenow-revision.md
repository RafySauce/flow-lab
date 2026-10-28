---
id: decision-2026-10-27-accomplishments-digest-m365-servicenow-revision
title: "Decision Log — Microsoft 365 & ServiceNow Gather, Correlate, Word Output as Skill, 1.3 → 2.0"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[fp-accomplishments-digest-m365-servicenow]]"
  - "[[accomplishments-docx-finisher]]"
---

# Decision Log — 2026-10-27 — Accomplishments Digest 2.0

**What was decided:** this revision adds two gather stages (Microsoft 365, ServiceNow), a heavy
Correlate stage, runtime engine selection, and Word styling as a skill-backed
stage. It also retires the companion `accomplishments-docx-finisher` flow. The
version goes from 1.3 to 2.0 and stages are renumbered 01–09. **By whom:** the agent, on direct operator
instruction and with the operator's go-ahead to build ("let's implement this"). The intake record is
`flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.
**What it affects:** every stage contract, the HUB, the document shape, and the
default Word style (moved into this flow). It adds three skill briefs and two revision briefs, and
proposes two deprecations (below).

## Operator decisions (2026-10-27)

| # | Call | Alternative rejected |
|---|---|---|
| D1 | One new gather stage per source | Folding the new sources into Stages 2/3, which would put two engines in one stage contract |
| D2 | The engine is chosen at runtime by capability probe | A Copilot-first or Rovo-first fixed assignment |
| D3 | Correlation is its own stage | Correlation inside Draft, which would make a heavier, harder-to-verify drafter |
| D4 | An Operational load section plus counts as evidence in themes | Counts only inside themes, or a standalone section only |
| D5 | Word styling is a skill, not a flow ("a flow seems a bit heavy") | Keeping the companion flow without its Copilot lock |
| D6 | Correlate is heavy ("confirm it is correct so the report generates correctly") | Light, with the check at Stage 8 |

## Agent calls (operator took the brief's defaults)

1. **Correlate is a skill**, not inline. Matching on shared identifiers is
   reusable, so a brief was filed (`sp-accomplishments-correlator`).
2. **ServiceNow attribution is probed per tenant**, not fixed in the design.
   The probe is `reference/servicenow-attribution-capability-check.md`.
3. **Mail scope defaults to personal**, and shared mailboxes must be opted in by name at Stage 1.
4. **Renumber to 01–09**, not non-sequential, to keep the house convention.
5. **The existing skills are reused as patterns, not widened.**
   `doc-evidence-gatherer` declares itself "not an accomplishments gatherer."
   `servicenow-ticket-ingest` is aggregate-only by design, and that design
   protects `statik-adoption`. New per-person skills borrow their mechanics.
6. **The revision is staged as a full 2.0 copy in `review-flowspaces/`.**
   The verified 1.3 in `icp-flows/` is left untouched, because the foundry never
   writes into the done queues. On promotion, the operator replaces the 1.3
   copy with this one.
7. **Deviations from the U-curve.** Stage 6 is heavy mid-flow (D6). Stage 9
   stays light as an optional terminal stage, because Stage 8 is the content gate
   and Stage 9's Verify checks that styling changed nothing.

## Proposed deprecations (operator's act at promotion)

- **`icp-flows/accomplishments-docx-finisher`** (flowspace): replaced by Stage
  9. Its enrichment step (adding repo and file evidence to approved content)
  is not carried over, because evidence now enters through Stages 2–6 before
  the human gates rather than after them. Its J1 assumption ("enrichment never
  adds claims") becomes moot.
- **`produced-skills/repo-context-enricher`**: its only consumer was the
  finisher's Stage 1. Mark it deprecated rather than deleting it, so its
  record survives.

## Promotion checklist for the operator

- [ ] Run the three validation gates on this staged copy (`flow-foundry/templates/validation-checklist.md`).
- [ ] Replace `icp-flows/accomplishments-digest/` with this copy, and stamp `verified`.
- [ ] Apply the two deprecations above.
- [ ] Update `icp-flows/CONTEXT.md` (the accomplishments-digest row's inputs; remove or deprecate the finisher row) and `produced-skills/CONTEXT.md` (the enricher row).
- [ ] Decide when to send the five briefs in `skill-foundry/backlog-skill-starters/` through the skill-foundry.
