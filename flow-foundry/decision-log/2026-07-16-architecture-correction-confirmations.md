---
id: decision-2026-07-16-architecture-correction-confirmations
title: "Decision Log — Operator Confirmations on the Source-Repo Correction"
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
  - "[[decision-2026-07-16-gitlab-sole-source-of-truth]]"
  - "[[mirroring-protocol]]"
---

# Decision Log — 2026-07-16 — Operator Confirmations on the Source-Repo Correction

**What was decided:** three open questions from the architecture correction
(same-day sibling entry) were resolved by the operator. (1) **Terminology:**
the house term for the instance repository is the **source-repo** — adopted
across the corrected specs and templates ("single-surface model" /
"source-of-truth mapping" phrasing replaced). (2) **`confluence-page-commit`
and `doc-custodian` are kept, not retired:** they still function — their job
is building and maintaining items *in* Confluence or ServiceNow, i.e. they
are external-system publishing/maintenance skills. The pending foundry-routed
revision reframes their rationale (external-system write targets, not
"Confluence as system of record") rather than redesigning them into
GitLab-commit skills. (3) **Rovo's repo access has a named mechanism:** the
**Rovo GitLab connector** gives Rovo read access to the source-repo; cited
explicitly in `mirroring-protocol.md` §1, `adapter-rovo.md`, and README.
**By whom:** operator. **Alternatives considered:** retiring or
git-redesigning the two skills (rejected — their external-system purpose is
still valid); leaving the connector generic (rejected — naming it makes the
adapter template concrete). **What it affects:** the same files as the
sibling entry (terminology pass), plus it sets direction for the pending
foundry revision of Tier 3–9 artifacts.
