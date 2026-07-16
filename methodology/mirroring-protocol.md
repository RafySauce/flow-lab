---
id: mirroring-protocol
title: "Source of Truth Protocol — GitLab Single Surface"
type: specification
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-16
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[provenance-spec]]", "[[governance-and-audit]]"]
---

# Source of Truth Protocol

**GitLab is the sole source of truth for an ICP instance.** One instance = one internal GitLab repository. Every flowspace, stage contract, decision log, and sign-off lives there as markdown with literal YAML frontmatter, in exactly the folder shapes this repo's templates define. There is no Confluence system-of-record, no regenerated mirror, and no dual-surface split.

This protocol governs the *employer-internal* instance. This public repo is not an instance; it holds method only.

> **Supersession note (v2.0).** Versions 1.x of this document specified a dual-surface architecture — Confluence as primary, an internal git repo as a regenerated Copilot mirror — with a structure mapping, a manual sync procedure, a drift check, and Confluence-native mechanics. That architecture is retired. Downstream documents that still cite the old §2 (structure mapping), §3 (sync), §4 (drift check), or §7 (Confluence-native mechanics) describe machinery that no longer exists; they are queued for foundry-routed revision. The decision is logged in `flow-foundry/decision-log/2026-07-16-gitlab-sole-source-of-truth.md`.

---

## 1. The single surface

| Surface | Role | Writes |
|---|---|---|
| **Internal GitLab repository** | The ICP instance. The authoritative copy of every flowspace, contract, decision log, and sign-off. Both sanctioned engines — Rovo and Copilot — ground on it and operate against it. | Humans write directly or via merge request. Agents propose changes as branches/MRs; direct silent edits to `verified` content are never sanctioned. |
| **This public repo (flow-lab)** | Method, templates, and sanitized exemplars only. | Not an instance surface; employer content never enters it. |

With one surface there is nothing to mirror, nothing to sync, and no cross-surface drift to check: **the repository history is the audit trail.**

## 2. External systems — Confluence, Jira, ServiceNow

Confluence, Jira, and ServiceNow remain in the toolchain, but as **external systems** — the applications flows and skills most often read from or write to, subject to each stage's Data boundary and the employer's sanctioned-tool matrix. They are integration targets, not homes for the ICP structure:

- A skill may *write* to them (`jira-commit` creating work items; the `documentarian` flow targeting ServiceNow KB articles or Confluence pages as deliverable destinations).
- A skill may *read* from them (`confluence-contribution-gatherer`, `jira-accomplishments-gatherer`).
- Content fetched from them into the instance enters as `type: clipping`, `truth-level: claimed`, per `provenance-spec.md` — external material is never treated as reviewed work by virtue of where it came from.

The ICP methodology's own documents — contracts, hubs, decision logs, skills — never live in these systems. A deliverable *published* to one of them is an output crossing the boundary, carrying its AI-contribution disclosure with it (`governance-and-audit.md` §6).

## 3. Change discipline (git-native mechanics)

The machinery the old dual-surface model implemented by hand, git provides natively:

- **Commit messages are the change log.** House rule: non-trivial edits to a stage contract, hub, or spec get a commit message describing *why* it changed, not just what. Diffs are free; "compare versions" is `git diff`.
- **Merge requests are the review surface.** Promotions (`to-review` → `verified`) and any edit to `verified` content ride an MR a human approves. MR approval is *supplementary* review evidence; the decision-log entry naming who/when/what-was-checked remains the requirement (`governance-and-audit.md` §4).
- **Branch protection is boundary enforcement.** Protecting the default branch (and `icp-flows/` / `produced-skills/` paths, where the GitLab tier supports path rules) enforces the human-only gate structurally, not just by convention.
- **Folder moves stay the queue mechanism.** `backlog-*` → `review-*` → DONE-queue transitions are `git mv` commits; history follows the file.
- **Decision-log entries are still required.** A diff shows what changed; only the log captures rationale and alternatives considered. Append-only, per `governance-and-audit.md` §7.

## 4. The handoff artifact (Rovo ⇄ Copilot)

Both engines operate against the same repository, so a handoff no longer crosses surfaces — but work still crosses *engines* mid-flow, and the handoff record keeps that legible. It travels as a file in the instance repo, `handoffs/YYYY-MM-DD-<flowspace>-s<N>.md`:

```markdown
---
id: <flowspace>-handoff-<date>
type: clipping            # it records state; it is not itself reviewed work
truth-level: claimed
source: human+ai
owner: <human driving the flow>
data-class: <highest class of referenced content>
---

# Handoff: <flowspace> — into Stage <N>

**From:** <engine that produced current state>
**To:** <engine picking up>

## State
What stages are complete, at what truth-level, with repo paths.

## Inputs for the receiving stage
Exactly what the receiving stage's contract lists as Inputs, with locations.

## Open questions / operator decisions pending
Anything the receiving engine must not decide on its own.
```

Rules unchanged from v1: the handoff **names its human owner**; the receiving engine treats the receiving stage's `CONTEXT.md` as its contract (the handoff carries state, never new instructions that override the contract); and a handoff into a stage whose Data boundary excludes the receiving engine is invalid — stop and re-route.

## 5. What deliberately does not enter the instance

- Employer content never enters any public surface, including this repo.
- Rovo/Copilot conversation transcripts are not committed — only their *artifacts* (documents, decisions, code) enter the structure.
- Credentials, tokens, and personal data never enter the ICP tree.

---

## Changelog

- **2.0** (2026-07-16) — **Architecture correction: GitLab is the sole source of truth.** Retitled from "Mirroring Protocol — Atlassian Primary ⇄ Copilot Git Mirror" (filename and `id` kept stable so existing references resolve). Removed the Confluence-primary/git-mirror split and everything that existed to serve it: the structure mapping (old §2), the sync procedure and `MIRROR-STATE.md` (old §3), the drift check (old §4), and Confluence-native mechanics (old §7). Added: external-systems section (Confluence/Jira/ServiceNow as integration targets), git-native change discipline. Kept: the Rovo⇄Copilot handoff artifact (simplified to single-surface paths) and the what-does-not-enter rules. Rationale and impact: `flow-foundry/decision-log/2026-07-16-gitlab-sole-source-of-truth.md`.
- **1.1** (2026-07-03) — Added §7, Confluence-native mechanics. *(Superseded by 2.0.)*
- **1.0** (2026-07-02) — Initial dual-surface protocol. *(Superseded by 2.0.)*
