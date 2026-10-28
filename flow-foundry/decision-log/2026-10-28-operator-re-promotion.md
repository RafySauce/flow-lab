---
id: decision-2026-10-28-operator-re-promotion
title: "Decision Log — Operator Re-Promotion of Twelve Demoted Items and Brief Stamps"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-28
updated: 2026-10-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[2026-10-28-truth-level-sync-sweep]]"
  - "[[2026-10-21-source-repo-protocol-rename-and-citation-sweep]]"
  - "[[governance-and-audit]]"
---

# Decision Log — 2026-10-28 — Operator Re-Promotion

**What was decided:** twelve items demoted to `to-review` by content changes
(2026-07-27 chat-session degrade paths; 2026-10-21 citation sweep) return to
`truth-level: verified`, and skill-primer briefs are stamped to match their
skills per `skill-foundry/foundry-spec.md` §4.

**By whom:** the operator, item by item, on a yes/no validation list that
named each item's version and what changed since its last promotion. The agent
applied the stamps on that instruction; it promoted nothing on its own.

## Promoted (operator answered yes to each)

| Item | Version | Change since last `verified` |
|---|---|---|
| `jira-accomplishments-gatherer` | 1.1 | Chat-session degrade path (2026-07-27) |
| `confluence-contribution-gatherer` | 1.1 | Chat-session degrade path (2026-07-27) |
| `bulk-child-creation` | 1.2 | Citation sweep (2026-10-21) |
| `servicenow-ticket-ingest` | 1.1 | Citation sweep (2026-10-21) |
| `confluence-page-commit` | 1.1 | `<flow>-flow-v<version>` provenance label on create/update (2026-10-21) |
| `provenance-stamper` | 1.1 | Engines narrowed to Copilot; Confluence batch-check trigger removed (2026-10-21) |
| documentarian `reference/doc-type-registry.md` | 1.1 | Source-repo model rewrite (2026-10-21) |
| documentarian `reference/documentation-standards.md` | 1.1 | Source-repo model rewrite; Confluence provenance label |
| documentarian `reference/collaborative-sections-protocol.md` | 1.1 | Source-repo model rewrite |
| documentarian `reference/custody-model.md` | 1.1 | Source-repo model rewrite |
| documentarian `reference/confluence-instantiation-guide.md` | 1.1 | Source-repo model rewrite |
| ai-refinement `reference/confluence-instantiation-guide.md` | 1.2 | Source-repo model rewrite |

**Evidence:** operator review and confirmation, 2026-10-28. No new on-engine
run backs this promotion: `confluence-page-commit` 1.1's label behavior has
not yet run on Rovo, and the on-engine and Copilot live tests the HUBs list as
pending stay pending. *Alternative considered:* hold `confluence-page-commit`
until a Rovo run (the operator chose to promote).

## Brief stamps

- Nineteen briefs in `completed-skill-starters/` move `to-review` →
  `verified` to match their now-`verified` skills: the sixteen whose skills
  were already `verified`, plus `sp-bulk-child-creation`,
  `sp-confluence-page-commit`, and `sp-servicenow-ticket-ingest`, promoted
  above.
- `sp-jira-accomplishments-gatherer`, `sp-confluence-contribution-gatherer`,
  and `sp-provenance-stamper` stay `verified`: the operator chose that briefs
  follow their skill, and those skills are `verified` again.

## Not covered

`doc-evidence-gatherer` 1.1 (Copilot sanctioned for read-only sweeps,
2026-10-21) and its brief stay `to-review`. It was not on the list because its
HUB already reported it correctly.

**What it affects:** six `SKILL.md` and six reference stamps, nineteen brief
stamps, four HUBs, `produced-skills/CONTEXT.md`.
