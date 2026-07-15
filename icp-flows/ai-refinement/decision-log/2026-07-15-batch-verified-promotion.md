---
id: decision-2026-07-15-batch-verified-promotion
title: "Decision Log — Batch truth-level Promotion to verified across icp-flows/ and produced-skills/"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[documentarian]]"
  - "[[jira-commit]]"
  - "[[workitem-validation]]"
  - "[[field-refinement-cadence]]"
---

# Decision Log — 2026-07-15 — Batch verified Promotion

**What was decided:** promote every non-log, non-`claimed` artifact still at
`truth-level: to-review` under `icp-flows/` and `produced-skills/` to
`truth-level: verified`, and stamp `updated: 2026-07-15`. **By whom:** the
operator (Rafy) — explicit instruction this
session to "update the truth-level validation status for any items that have
been promoted to icp-flows and produced-skills to show verified." The operator
is the reviewer of record; the agent executed the frontmatter edits. This entry
is the promotion's review evidence per governance §4 and provenance rule 5.

**Reviewer:** operator  **Date:** 2026-07-15  **What was checked:** the operator
confirmed these artifacts against reality as of this session. Promotion covers
items already resident in the two landing zones (residency there being the
completed-gate signal per `icp-flows/CONTEXT.md` and
`produced-skills/CONTEXT.md`) whose frontmatter had not yet been flipped.

**Scope — 31 artifacts flipped `to-review` → `verified`:**

- **produced-skills/** — `field-refinement-cadence`, `jira-commit`,
  `workitem-validation` (SKILL.md).
- **icp-flows/ai-refinement/** — stage CONTEXTs 01–06; references
  `ai-refinement-hybrid`, `confluence-instantiation-guide`,
  `on-engine-validation-checklist`, `platform-stakeholder-register-template`,
  `work-item-schemas`.
- **icp-flows/documentarian/** — stage CONTEXTs 01–07; HUB.md; references
  `ai-refinement-handoff-contract`, `collaborative-sections-protocol`,
  `confluence-instantiation-guide`, `custody-model`, `doc-type-registry`,
  `documentation-standards`.
- **icp-flows/accomplishments-digest/** — references
  `accomplishments-document-shape`, `confluence-activity-history-capability-check`,
  `handoff-to-copilot-template`.
- **icp-flows/accomplishments-docx-finisher/** — reference
  `docx-minimal-default-style`.

**Explicitly excluded (unchanged):** all `decision-log` entries (they record
events, not claims — verified by nature); the `claimed` clipping
`ai-refinement/reference/platform-stakeholder-register.md` (provenance rules 4
and 8 forbid a claimed artifact being verified). Artifacts already `verified`
(HUBs, prior-promoted skills) were not touched.

**Mirroring:** per `methodology/mirroring-protocol.md` §5, a truth-level
promotion is a sync trigger. The Confluence mirror's page-properties `truth-level`
and Status macros for these artifacts should be updated to `VERIFIED` on the next
sync.
