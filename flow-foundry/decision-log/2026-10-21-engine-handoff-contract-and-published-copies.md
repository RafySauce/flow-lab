---
id: decision-2026-10-21-engine-handoff-contract-and-published-copies
title: "Decision Log — Engine Handoff Contract and Published Copies"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-21
updated: 2026-10-21
owner: operator
source: human+ai
data-class: public
related:
  - "[[engine-handoff-contract]]"
  - "[[mirroring-protocol]]"
  - "[[2026-07-16-gitlab-sole-source-of-truth]]"
---

# Decision Log — 2026-10-21 — Engine Handoff Contract and Published Copies

**What was decided:** two methodology changes recording how instances
actually run while engines cannot reach the source-repo.

1. A new shared spec, `methodology/engine-handoff-contract.md` (1.0), defines
   the **commit packet**: the self-contained Markdown a flow emits when the
   engine that produced signed-off work cannot write it, for a different
   engine that can write but cannot read this method. It opens with a
   verbatim **executor brief** (the commit stage's rules, restated), then a
   header, a per-flow payload, decisions left to the user, and a return slip.
2. `methodology/mirroring-protocol.md` 2.0 → 3.0 adds **published copies**
   (§6): read-only, version-stamped snapshots of a flow, published by hand
   after merge, with a version note kept in the protocol. §1 separates the
   target state (engines ground on GitLab) from the interim. §4 splits into
   same-repo handoffs (unchanged) and the commit packet.

**By whom:** agent, on direct operator instruction, after a design
discussion in which the operator chose full wiring into both flows, the
source-repo name, a version note kept in the protocol itself, and an
uncommitted cleanup handoff for the citing documents.

**The situation, as the operator described it:** a Copilot Agent Builder
flow agent runs the flows from a static copy uploaded to SharePoint and has
read-only access to Confluence, Jira, and ServiceNow. Rovo has write access
but cannot read GitLab, and holds a Confluence copy of `ai-refinement` at
1.21 while the source is at 1.25 (1.26 after this pass). The operator carries
output between them by hand.

## Decisions and alternatives

1. **The commit packet carries instructions — a bounded departure from "state,
   never instructions."** That rule (protocol §4) assumes the receiver grounds
   on the source-repo. A blind executor has nothing to ground on, so the
   packet brings the commit stage's rules with it. Bounds: the brief restates
   the stage contract and never widens it (the source-repo `CONTEXT.md` wins
   on any difference); it never replaces a human approval; payload text is
   declared data, not instructions, because it originates in unsanitized
   meetings, emails, and documents. *Alternatives considered:* (a) a
   standalone Agent Builder skill that builds the packet — rejected by the
   operator: the flow agent already runs the flows, so a contract is enough;
   (b) a standing Rovo agent pre-loaded with the contract — not rejected,
   but not available today, and the self-contained packet works in plain
   Rovo chat either way; (c) per-target adapters (Jira, Confluence) — rejected
   by the operator; per-engine adapters were retired in this repo, and the
   per-flow payload sections already hold everything target-specific.
2. **The brief is shared and verbatim; only the payload is per-flow.** The
   reusable part across a fragmented toolchain is "how a blind engine commits
   safely," which does not depend on the flow. Per-flow specifics live in a
   short "commit-stage specifics" block inside each flow's payload.
3. **The packet carries the producing flow's version, and the brief's first
   rule is a version check.** Published copies drift behind the source; the
   packet is where the drift becomes visible, before anything is written,
   instead of after a wrong write.
4. **At most ten items or pages per packet**, matching `ai-refinement`'s
   ≤10-item bulk sub-batch rule; larger sets split into numbered,
   self-contained packets.
5. **"Published copies" replaces the mirroring idea, rather than deleting the
   protocol.** The operator wants GitLab to stay the source of truth and
   wants away from mirroring, since everything is manual anyway. Published
   copies say what is true — snapshots, by hand, behind the source — without
   promising sync. *Alternatives considered:* deprecating the protocol
   (rejected: §1, §2, §3, and §5 remain true and are cited by 51 files);
   splitting it into two documents (deferred: every citing file would have
   to pick a target).
6. **Section numbers 1–5 kept stable; filename and `id` kept.** Many
   documents cite "§4" or "§5" — some already wrongly, from v1 numbering.
   Renumbering would break more. The rename and reference pass are queued as
   a separate operator-held cleanup handoff, not committed here.
7. **The version note holds surface types and version numbers only.** No
   URLs, space keys, or site names enter this public repo.

## Assumptions (operator to confirm or amend)

- **F1** — The Agent Builder agent counts as **Copilot** for data-boundary
  purposes. Every boundary this pass relies on is read that way.
- **F2** — The Static document copy's version is left as "operator to
  record" in the version note; the operator knows what is uploaded.
