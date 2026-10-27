---
id: decision-2026-10-27-accomplishments-drafter-2-revision
title: "Decision Log — Accomplishments Drafter 1.0 → 2.0 Revision Build"
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
  - "[[sp-accomplishments-drafter-revision]]"
  - "[[accomplishments-drafter]]"
  - "[[decision-2026-10-27-accomplishments-digest-m365-servicenow-revision]]"
---

# Decision Log — 2026-10-27 — Accomplishments Drafter 2.0 Revision Build

**What was decided:** revise `accomplishments-drafter` to 2.0 (confirmed correlation map in place of two digests; Operational load section; recognition handling), staged as `review-skills/accomplishments-drafter/SKILL.md` at `to-review`. **By whom:** agent, on the operator's go-ahead to build the five digest-2.0 skills. **What it affects:** one new folder in `review-skills/`; the verified 1.0 in `produced-skills/` is untouched (the foundry never writes to the done queues), and the operator replaces it at promotion.

- **Halts on an unconfirmed map** (review criterion 10), not drafting best-effort — Stage 6 is a heavy gate precisely so prose is never built on unconfirmed groups.
- **Never regroups:** a wrong-looking group goes back to Stage 6 rather than being fixed in the drafter, keeping the correlator/drafter boundary clean.
- **Operational load uses only figures the load summary states**, never recomputed, and excludes assigned-but-not-resolved records, so the section cannot become a scoreboard.
- **Diagram and Method kept one-for-one;** Mermaid compilation not run this session (see report); GitLab rendering unconfirmed.
