---
id: decision-2026-10-09-production-promotion
title: "Decision Log — ai-refinement and documentarian Declared Production-Ready"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-10-09
updated: 2026-10-09
owner: operator
source: human+ai
data-class: public
related: ["[[ai-refinement]]", "[[documentarian]]"]
---

# ai-refinement and documentarian Declared Production-Ready

## Decision
The operator declared both flowspaces production-ready and instructed their
promotion to `truth-level: verified`. This is an operator-instructed
promotion (Gate 3, `methodology/governance-and-audit.md`); the foundry
applied the stamps at the operator's direction and did not judge readiness.

## Scope
- **`icp-flows/ai-refinement/`** — HUB, all six stage contracts, and the
  reference documents that were still `to-review`.
- **`icp-flows/documentarian/`** — HUB.
- **Dependent skills** that were `to-review` and sit on the ai-refinement
  path: `field-refinement-cadence`, `workitem-validation`, `jira-commit`,
  `bulk-child-creation`. A production flow cannot depend on unverified
  skills, so they move with it. Reverting is a one-line frontmatter change
  per file if the operator wants the skills held back.
- Decision-log entries are records and keep their original stamps.

## Reason
The operator's judgment that both flows are ready for use. This supersedes
the `to-review` demotions of 2026-08-05 and 2026-08-21 recorded in the
ai-refinement HUB.

## Related change
Per-engine adapters were retired the same day (`skill-foundry/foundry-spec.md`
1.6); skills are now their engine-neutral `SKILL.md` alone.

**Reviewed by:** operator
**Date:** 2026-10-09
