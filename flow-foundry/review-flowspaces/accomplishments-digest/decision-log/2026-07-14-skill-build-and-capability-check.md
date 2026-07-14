---
id: decision-2026-07-14-accomplishments-digest-skill-build-and-capability-check
title: "Decision Log — Three Layer-3 Skills Built; Confluence Capability Check Operationalized"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-14
updated: 2026-07-14
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[sp-jira-accomplishments-gatherer]]"
  - "[[sp-confluence-contribution-gatherer]]"
  - "[[sp-accomplishments-drafter]]"
---

# Decision Log — 2026-07-14 — Three Layer-3 Skills Built; Confluence Capability Check Operationalized

**What was decided:** two follow-ups to this flowspace's outstanding Layer-3
gaps, on direct operator instruction ("let's build the skills then test.
then work through the open items"). **By whom:** agent. **What it affects:**
Stages 2, 3, and 4's `CONTEXT.md` Layer-3 lines (updated from "TBD — brief
filed" to "skill built, staged... awaiting operator promotion"); `HUB.md`'s
Known gaps table and Reference material table; a new reference doc,
`reference/confluence-activity-history-capability-check.md`; the flow
primer brief's first open question, annotated as operationalized.

## 1. The three Layer-3 skill gaps

`jira-accomplishments-gatherer`, `confluence-contribution-gatherer`, and
`accomplishments-drafter` were authored as full specs plus adapters by the
skill-foundry and staged in `skill-foundry/review-skills/`, at
`truth-level: to-review`. Full build record, spec-review findings, and
simulated live-test evidence: `skill-foundry/decision-log/2026-07-14-
accomplishments-digest-skill-batch.md` and its companion gate-pre-run entry.
This flowspace's own `CONTEXT.md` files and `HUB.md` are updated here only to
reflect that state accurately — build status, not promotion status. No
skill was promoted, moved to `../../../produced-skills/`, or deployed; that
remains the operator's call.

## 2. The Confluence activity-history open question

The flow primer brief's open question ("does the target org's instance
expose enough activity history to make the collaboration-signal slice
reliable?") was a standing unknown with no concrete procedure attached
beyond "resolve at instantiation." This session turned it into a one-time-
per-tenant probe: `reference/confluence-activity-history-capability-check.md`
— a 5-step probe plus a 3-row decision table (Full / Partial /
Authored-pages-only depth) that tells an operator which of the
`confluence-contribution-gatherer` skill's three already-designed fallback
behaviors applies to their tenant.

**Why this counts as progress, not resolution:** this public repo cannot
answer "what does *your* Confluence instance expose" — that's inherently
per-tenant and only knowable at instantiation. What it *can* do is turn a
vague "check this later" into a runnable procedure with a decision table, so
instantiation doesn't start from a blank page. The skill's own behavior in
every depth scenario was already correct in the 2026-07-14 build (per its
Review criterion 2) — this checklist doesn't change the skill, it tells the
operator which of its existing branches their tenant will exercise.

## Assumption (operator to confirm or amend)

- **J1 — a one-time-per-tenant probe is the right cadence**, not a per-run
  check. Amendment path: if a tenant's retention settings turn out to change
  more often than a platform upgrade (e.g., an admin-configurable retention
  window IT can lower at will), this should become a periodic re-check
  folded into the quarterly audit pass instead of a one-time instantiation
  step.
