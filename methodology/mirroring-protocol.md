---
id: mirroring-protocol
title: "Mirroring Protocol — Atlassian Primary ⇄ Copilot Git Mirror"
type: specification
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-03
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[provenance-spec]]", "[[governance-and-audit]]"]
---

# Mirroring Protocol

How one ICP instance lives on two surfaces — **Confluence as the system of record** and **an internal git repository as the Copilot-readable mirror** — without the two drifting apart, and how work hands off between Rovo and Copilot.

This protocol governs the *employer-internal* instance. This public repo is not a mirror surface; it holds method only.

---

## 1. Roles

| Surface | Role | Writes |
|---|---|---|
| **Confluence** | Primary. The authoritative copy of every flowspace, contract, decision log, and sign-off. Rovo agents read and act here natively. | Humans and Rovo agents write here. |
| **Internal git repo (GitLab)** | Mirror. A markdown rendering of the Confluence structure so Copilot (chat, custom agents, coding agent) can ground on the same contracts. | Regenerated from Confluence. Copilot writes **proposals** here (branches/PRs), never direct edits to mirrored content. |

**One direction of truth.** Content flows Confluence → git. Changes originating on the git side (e.g., Copilot drafts a revised stage contract) go back as a *proposal* that a human applies to Confluence; the mirror then picks it up on the next sync. Two-way silent sync is explicitly rejected — it is how mirrors diverge and audits fail.

---

## 2. Structure mapping

| ICP structure | Confluence | Git mirror |
|---|---|---|
| Flowspace | Parent page (the hub) with a child-page tree | Folder with `HUB.md` |
| Stage | Child page per stage, numbered (`01 — Intake`, `02 — Draft`, …) | Numbered folder with `CONTEXT.md` (`01-intake/CONTEXT.md`) |
| Stage contract fields | Page sections (Inputs / Process / Outputs / Verify / Review / Data boundary) | Same headings in `CONTEXT.md` |
| Stage Flow Diagram | Mermaid diagram rendered by the space's Mermaid macro (if installed), else a "diagram: see mirror" note | Mermaid `flowchart LR` in `HUB.md`, rendered natively by GitLab's markdown viewer |
| Provenance frontmatter | Page properties macro + labels (`truth-verified`, `src-human-ai`, `dc-internal`) + Status macro | Literal YAML frontmatter |
| Decision log | Child pages under a `Decision Log` page, one per entry | `decision-log/YYYY-MM-DD-<slug>.md` |
| Working artifacts (Layer 4) | Attachments or child pages under the stage | `NN-<stage>/work/` (may be `.gitignore`d if transient) |
| Reference material (Layer 3) | A `Reference` page tree, linked from stage pages | `reference/` folder, pointed at from `CONTEXT.md` |

Naming rule: the Confluence page title and the git path both derive from the artifact `id`. If you can't compute one from the other, the mapping is broken.

---

## 3. Sync procedure

Until a sync automation exists (a flagged skill gap — see the skill-foundry backlog), the mirror is maintained manually at defined moments:

1. **Sync on state change, not on schedule alone.** Mirror after any of: a stage contract edited, a truth-level promotion, a decision-log entry added, a flowspace created or retired.
2. **Sync is a copy, not a rewrite.** Transcribe Confluence content to markdown faithfully; do not "improve" during sync. Improvements are edits to the primary, which then sync.
3. **Stamp the sync.** The mirror root carries a `MIRROR-STATE.md`: last-sync date, syncing human/agent, and the list of paths touched.

## 4. Drift check

A periodic (weekly, or pre-audit) comparison of the two surfaces:

- Every flowspace hub in Confluence has a corresponding `HUB.md`, and vice versa.
- Stage count and stage names match per flowspace.
- `truth-level` and `updated` match per artifact (page properties vs. frontmatter).
- No mirror file is newer than its `MIRROR-STATE.md` entry implies.
- Stage Flow Diagram renders correctly on both surfaces: GitLab (view the rendered `.md`, not the diff) and Confluence (macro installed and displaying, or the page carries the "diagram: see mirror" fallback note — not a dead code block).

Findings are a **report, not an auto-fix** — a human decides which surface is right, corrects the primary, and re-syncs. (Automating the comparison is the `mirror-drift-checker` skill gap in the backlog.)

---

## 5. The handoff artifact (Rovo ⇄ Copilot)

When work crosses engines mid-flow — e.g., Rovo has driven stages 1–2 in Confluence and stage 3 is code work for Copilot — the handoff travels as a file in the mirror, `handoffs/YYYY-MM-DD-<flowspace>-s<N>.md`:

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

**From:** <engine + surface that produced current state>
**To:** <engine + surface picking up>

## State
What stages are complete, at what truth-level, with links (Confluence URL + mirror path).

## Inputs for the receiving stage
Exactly what the receiving stage's contract lists as Inputs, with locations.

## Open questions / operator decisions pending
Anything the receiving engine must not decide on its own.
```

Rules: the handoff **names its human owner**; the receiving engine treats the receiving stage's `CONTEXT.md` as its contract (the handoff carries state, never new instructions that override the contract); and a handoff into a stage whose Data boundary excludes the receiving engine is invalid — stop and re-route.

---

## 6. What deliberately does not sync

- Employer content never syncs to any public surface, including this repo.
- Rovo/Copilot conversation transcripts are not mirrored — only their *artifacts* (documents, decisions, code) enter the structure.
- Credentials, tokens, and personal data never enter either surface's ICP tree.

---

## 7. Confluence-native mechanics

Confluence being the primary surface is not just a constraint to mirror around — it has native machinery worth using deliberately.

- **Version history as lightweight commit log.** Every save can carry a change comment — the closest native analog to a git commit message. House rule: non-trivial edits to a stage contract, hub page, or decision-log page get a change comment describing *why* it changed, not just that it changed. "Compare versions" gives a diff view for free, useful for the drift check (§4) and for reviewing what moved between `to-review` and `verified`.
- **Boundary: this is not a git-mirror replacement.** Version history is linear, per-page, and can be purged by a space admin — it is evidence of change, not immutable audit proof. It does not replace the git mirror's branch/PR mechanism (§1's "one direction of truth" still governs cross-engine proposals), and it does not replace decision-log entries, which capture *rationale and alternatives considered* — something a version diff cannot reconstruct.
- **CQL for audit queries.** Confluence Query Language can drive the governance audit pass instead of manual page-by-page review — e.g. `label = "truth-verified" AND lastmodified < now("-90d")` to find stale verified pages due for re-check, or `space = "<flowspace>" AND label != "dc-public" AND label != "dc-internal" AND label != "dc-confidential" AND label != "dc-restricted"` to find pages missing a data-class label. See `governance-and-audit.md` §8.
- **Page Properties Report macro.** Renders a live dashboard of stage-contract frontmatter (truth-level, owner, data-class) pulled from every page carrying the properties macro, placed on the flowspace hub or a Reference page. Replaces manually walking pages during drift checks and audits.
- **Page moves stay the queue mechanism.** `backlog-*` → `completed-*` queue transitions are modeled as moving the page in the Confluence tree, mirroring the git-mirror folder move (§2). Page moves do not break version history continuity — the version log follows the page — so this is fully compatible with treating version history as an audit trail. No change from existing practice; noted here because it's worth confirming explicitly rather than assuming.
- **Status macro for truth-level.** A native colored-lozenge Status macro (`DRAFT`, `TO REVIEW`, `VERIFIED`, `DEPRECATED`) at the top of each stage-contract and hub page mirrors the `truth-level` frontmatter field, giving at-a-glance state on the page itself. Only a human sets it to `VERIFIED` — the same human-only gate rule (`governance-and-audit.md` §4), now visible inline rather than only in page properties.
- **Restrictions as boundary enforcement.** A stage contract's Data boundary field can be enforced literally via Confluence page/space view-restrictions, not just documented as convention.

---

## Changelog

- **1.1** (2026-07-03) — Added §7, Confluence-native mechanics: version history as change log, CQL-driven audits, Page Properties Report macro, Status macro for truth-level, restrictions as boundary enforcement. Confirmed page moves remain the queue mechanism.
- **1.0** (2026-07-02) — Initial protocol.
