---
id: mirroring-protocol
title: "Source-Repo Protocol — GitLab as the Sole Source of Truth"
type: specification
artifact-version: "3.0"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-10-21
owner: operator
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[provenance-spec]]", "[[governance-and-audit]]", "[[engine-handoff-contract]]"]
---

# Source-Repo Protocol

**GitLab is the sole source of truth for an ICP instance.** One instance = one internal GitLab repository — the **source-repo**, the house term the rest of this repository uses for it. Every flowspace, stage contract, decision log, and sign-off lives there as markdown with literal YAML frontmatter, in exactly the folder shapes this repo's templates define. There is no Confluence system-of-record, no sync, and no dual-surface split. Where engines cannot yet reach the source-repo, they read **published copies** — read-only, version-stamped snapshots made by hand after a merge (§6). A published copy is never a second source.

This protocol governs the *employer-internal* instance. This public repo is not an instance; it holds method only.

> **Supersession note (v2.0).** Versions 1.x of this document specified a dual-surface architecture — Confluence as primary, an internal git repo as a regenerated Copilot mirror — with a structure mapping, a manual sync procedure, a drift check, and Confluence-native mechanics. That architecture is retired. Downstream documents that still cite the old §2 (structure mapping), §3 (sync), §4 (drift check), or §7 (Confluence-native mechanics) describe machinery that no longer exists; they are queued for foundry-routed revision. The decision is logged in `flow-foundry/decision-log/2026-07-16-gitlab-sole-source-of-truth.md`.
>
> **Interim note (v3.0).** The filename keeps the old "mirroring" name only so that existing references resolve; nothing here mirrors or syncs. v3.0 records the operating reality while engines are blocked from the source-repo: published copies (§6) and the commit packet for blind executors (§4, `engine-handoff-contract.md`). A rename and a pass over the citing documents are queued separately.

---

## 1. The single surface

| Surface | Role | Writes |
|---|---|---|
| **The source-repo (internal GitLab repository)** | The ICP instance. The authoritative copy of every flowspace, contract, decision log, and sign-off. **Target state:** both sanctioned engines ground on it directly — Rovo through the **Rovo GitLab connector**, Copilot natively. **Until then:** engines read published copies (§6). | Humans write directly or via merge request. Agents propose changes as branches/MRs; direct silent edits to `verified` content are never sanctioned. |
| **This public repo (flow-lab)** | Method, templates, and sanitized exemplars only. | Not an instance surface; employer content never enters it. |

With one source there is nothing to sync: **the repository history is the audit trail.** Published copies can drift *behind* the source, never away from it; §6 makes that visible.

## 2. External systems — Confluence, Jira, ServiceNow

Confluence, Jira, and ServiceNow remain in the toolchain, but as **external systems** — the applications flows and skills most often read from or write to, subject to each stage's Data boundary and the employer's sanctioned-tool matrix. They are integration targets, not homes for the ICP structure:

- A skill may *write* to them (`jira-commit` creating work items; the `documentarian` flow targeting ServiceNow KB articles or Confluence pages as deliverable destinations).
- A skill may *read* from them (`confluence-contribution-gatherer`, `jira-accomplishments-gatherer`).
- Content fetched from them into the instance enters as `type: clipping`, `truth-level: claimed`, per `provenance-spec.md` — external material is never treated as reviewed work by virtue of where it came from.

The ICP methodology's own documents — contracts, hubs, decision logs, skills — are never *authored or kept* in these systems. The one exception is a read-only published copy (§6), which is a snapshot for an engine to read, not a home. A deliverable *published* to one of them is an output crossing the boundary, carrying its AI-contribution disclosure with it (`governance-and-audit.md` §6).

## 3. Change discipline (git-native mechanics)

The machinery the old dual-surface model implemented by hand, git provides natively:

- **Commit messages are the change log.** House rule: non-trivial edits to a stage contract, hub, or spec get a commit message describing *why* it changed, not just what. Diffs are free; "compare versions" is `git diff`.
- **Merge requests are the review surface.** Promotions (`to-review` → `verified`) and any edit to `verified` content ride an MR a human approves. MR approval is *supplementary* review evidence; the decision-log entry naming who/when/what-was-checked remains the requirement (`governance-and-audit.md` §4).
- **Branch protection is boundary enforcement.** Protecting the default branch (and `icp-flows/` / `produced-skills/` paths, where the GitLab tier supports path rules) enforces the human-only gate structurally, not just by convention.
- **Folder moves stay the queue mechanism.** `backlog-*` → `review-*` → DONE-queue transitions are `git mv` commits; history follows the file.
- **Decision-log entries are still required.** A diff shows what changed; only the log captures rationale and alternatives considered. Append-only, per `governance-and-audit.md` §7.

## 4. Engine handoffs

Work crosses *engines* mid-flow. Which shape it travels in depends on whether the receiving engine can read the source-repo:

- **The receiving engine grounds on the source-repo** → the same-repo handoff below: state only, never instructions.
- **The receiving engine is blind** — it cannot read the source-repo and knows only what it is handed (today: Rovo committing what a Copilot Agent Builder agent produced) → the **commit packet**, `engine-handoff-contract.md`. It carries the commit stage's own rules restated, because the receiver has no other copy of them.

### Same-repo handoff

It travels as a file in the source-repo, `handoffs/YYYY-MM-DD-<flowspace>-s<N>.md`:

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

Rules unchanged from v1, for the same-repo handoff: the handoff **names its human owner**; the receiving engine treats the receiving stage's `CONTEXT.md` as its contract (the handoff carries state, never new instructions that override the contract); and a handoff into a stage whose Data boundary excludes the receiving engine is invalid — stop and re-route.

## 5. What deliberately does not enter the instance

- Employer content never enters any public surface, including this repo.
- Rovo/Copilot conversation transcripts are not committed — only their *artifacts* (documents, decisions, code) enter the structure.
- Credentials, tokens, and personal data never enter the ICP tree.

## 6. Published copies (interim operating mode)

While engines cannot reach the source-repo, a flow runs from a **published copy**: a snapshot of the flow's files placed where an engine can read it.

| Surface | Reader | Typical carrier |
|---|---|---|
| The source-repo | Humans; agents with repo access | GitLab — the only editable copy |
| Static document copy | Copilot (e.g. an Agent Builder agent's knowledge source) | Files uploaded to a SharePoint/OneDrive location |
| Confluence page copy | Rovo | A page tree reproducing a flow's HUB, stages, and references |

Rules:

- **Read-only.** A published copy is never edited in place. A fix found while running from a copy goes back to the source-repo as a change, then is republished.
- **Version-stamped.** Every published copy shows the `artifact-version` of the flow's `HUB.md` it was made from, at the top, where the reading engine and the human both see it.
- **Published by hand, after merge.** Publishing is a manual step the operator takes once a change merges in the source-repo. Nothing syncs automatically, and nothing here pretends to.
- **Stale is visible, not silent.** Compare each copy's stamped version with the source `HUB.md` when publishing, and keep the note below current. At run time, the commit packet's version check (`engine-handoff-contract.md`, executor brief rule 1) catches a copy that is behind before anything is written.

**Version note** — the operator updates this by hand on each publish. Surface types and versions only: no URLs, space keys, site names, or anything else that identifies a tenant belongs in this public repository.

| Flow | Source-repo | Static document copy (Copilot) | Confluence copy (Rovo) | Last checked |
|---|---|---|---|---|
| `ai-refinement` | 1.26 | *(operator to record)* | 1.21 — behind | 2026-10-21 |
| `documentarian` | 1.3 | *(operator to record)* | none | 2026-10-21 |

---

## Changelog

- **3.0** (2026-10-21) — **Interim operating mode recorded.** Engines cannot yet reach the source-repo; flows run from hand-published copies, and Rovo commits work produced by a Copilot Agent Builder agent. §1 now separates the target state (engines ground on GitLab) from the interim (published copies); §4 splits into same-repo handoffs (state only, unchanged) and the **commit packet** for blind executors (new `engine-handoff-contract.md`); new §6 defines published copies — read-only, version-stamped, published by hand after merge — with a version note. Section numbers 1–5 kept stable for existing citations; filename and `id` kept, rename queued. Raised by the operator. Rationale: `flow-foundry/decision-log/2026-10-21-engine-handoff-contract-and-published-copies.md`.
- **2.0** (2026-07-16) — **Architecture correction: GitLab is the sole source of truth.** Retitled from "Mirroring Protocol — Atlassian Primary ⇄ Copilot Git Mirror" to "Source-Repo Protocol" (filename and `id` kept stable so existing references resolve); operator confirmed **source-repo** as the house term for the instance repository, and that Rovo's read access to it is via the Rovo GitLab connector. Removed the Confluence-primary/git-mirror split and everything that existed to serve it: the structure mapping (old §2), the sync procedure and `MIRROR-STATE.md` (old §3), the drift check (old §4), and Confluence-native mechanics (old §7). Added: external-systems section (Confluence/Jira/ServiceNow as integration targets), git-native change discipline. Kept: the Rovo⇄Copilot handoff artifact (simplified to single-surface paths) and the what-does-not-enter rules. Rationale and impact: `flow-foundry/decision-log/2026-07-16-gitlab-sole-source-of-truth.md`.
- **1.1** (2026-07-03) — Added §7, Confluence-native mechanics. *(Superseded by 2.0.)*
- **1.0** (2026-07-02) — Initial dual-surface protocol. *(Superseded by 2.0.)*
