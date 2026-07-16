---
id: decision-2026-07-16-gitlab-sole-source-of-truth
title: "Decision Log — Architecture Correction: GitLab Is the Sole Source of Truth"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-16
updated: 2026-07-16
owner: operator
source: human+ai
data-class: public
related:
  - "[[mirroring-protocol]]"
  - "[[flow-foundry-spec]]"
  - "[[skill-foundry-spec]]"
---

# Decision Log — 2026-07-16 — GitLab Is the Sole Source of Truth

**What was decided:** the documented dual-surface architecture (Confluence as
system of record, an internal git repo as a regenerated Copilot mirror) is
retired. The actual architecture is a single surface: **an internal GitLab
repository is the sole source of truth for an ICP instance, and both
sanctioned engines (Rovo and Copilot) ground on it and operate against it.**
Confluence, Jira, and ServiceNow remain in the toolchain as *external systems*
— integration targets flows/skills read from and write to at declared data
boundaries — not as homes for the ICP structure. Consequences: nothing to
mirror, sync, or drift-check (repo history is the audit trail); engine
assignment can no longer be justified by "Rovo can't touch git" / "Copilot
can't touch Confluence" and must be re-derived per skill; the
`sp-mirror-drift-checker` starter is obsolete-by-architecture-change
(permanently, not pending). **By whom:** operator (confirmed facts), recorded
by agent. **Alternatives considered:** keeping the dual-surface docs as a
documented-but-optional deployment mode — rejected; it never matched the
actual deployment and 170+ files inherited the false premise. **What it
affects:** this pass corrected the core specs and templates —
`mirroring-protocol.md` (2.0, retitled "Source of Truth Protocol"),
`README.md`, `AGENTS.md`, `icp-primer.md` §4, `governance-and-audit.md` (1.2),
`provenance-spec.md` (1.2), both foundry specs (1.5), both flow-diagram
guides, `adapter-rovo.md`'s engine rule, `adapter-copilot.md`, the flowspace
scaffold/checklist/brief templates, and both capability catalogs. **Still
stale, deliberately:** per-flowspace `HUB.md` Surfaces sections, stage
`CONTEXT.md` files, individual `SKILL.md`/adapter designs (notably
`confluence-page-commit`, `doc-custodian`, `contract-reviewer`,
`provenance-stamper`, `repo-context-enricher`, `accomplishments-docx-stylizer`
engine reasoning), and backlog primer briefs — substantive flow/skill
revisions route through the foundries (AGENTS.md rule 2), not bulk edits.
Prior decision-log entries reference the old architecture by design — logs
are append-only records of what was true when written.
