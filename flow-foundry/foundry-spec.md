---
id: flow-foundry-spec
title: "Flow Foundry — Method Spec"
type: specification
artifact-version: "1.4"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-03
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[provenance-spec]]", "[[skill-foundry-spec]]"]
---

# Flow Foundry — Method Spec

The method for turning a crystallized workflow intent (or a foreign workflow artifact) into a house-standard flowspace. Engine-agnostic: the same method runs whether the session driver is Copilot, Rovo, or a human with a text editor. Adapted from a private homelab implementation; changes for the work context are listed in the changelog.

---

## 1. Intake and triage (the front door)

**Step 0 — Confirm invocation.** The foundry runs only on a confirmed
operator instruction. Before any triage, scaffold, or revision work: restate
the starter, its triage classification, and the intended outputs, and wait for
the operator's explicit go-ahead. A starter merely being mentioned — or
sitting in the backlog — is not an instruction to build it.

The first move on any starter is to classify it:

1. **Flow-primer-brief?** Crystallized intent with a purpose statement, stage estimate, and Layer-3 inventory (per [`templates/flow-primer-brief-template.md`](templates/flow-primer-brief-template.md)). → *Clean path*: transcribe the decided intent into structure. The exploration is done; don't re-open it.
2. **Foreign workflow material?** An existing process doc, a vendor "AI workflow" template, someone else's folder structure. → *Normalize path*: run the [intake vetting checklist](../skill-foundry/templates/intake-vetting-checklist.md) (provenance, maintenance, license, security) first, then assess and rebuild to house standard.
3. **Not flowspace-worthy?** Single-session tasks aren't flowspaces; a capability is a skill (route to the skill-foundry); a one-off project doesn't need a reusable structure. Say so plainly and recommend the right tool. Dropping is a normal outcome — log it.
4. **Bare conversation, no formal starter?** Workable — but say so, and run the setup questionnaire below to backfill the missing structure.

Every triage call that isn't obvious earns a `decision-log/` entry.

## 2. Setup questionnaire

Nine questions, answered (or consciously deferred, with a note) before authoring a single stage:

1. **Name + slug** — kebab-case; drives the `id`, folder name, and Confluence page title.
2. **Purpose statement** — one sentence: what problem, for whom.
3. **Stage count and names** — known, or designed together now?
4. **Primary surface mapping** — which Confluence space/page tree is the primary instance; which GitLab repo is the mirror. If the target Confluence space doesn't have a Mermaid-rendering macro installed, note that now — it changes how the Stage Flow Diagram ships (see `references/flow-diagram-guide.md`).
5. **Review-intensity per stage** — apply the U-curve default (heavy / light / heavy — ICM Fig. 5) and adjust: which stages carry judgment, which are constrained execution?
6. **Data boundary per stage** — what `data-class` does each stage handle, and which engines are sanctioned for it?
7. **Layer-3 status per stage** — existing skill to reference, inline one-off, or gap?
8. **Intake path** — clean design from a primer-brief, or normalization of foreign material?
9. **Stakeholder register availability** — is a stakeholder register available for this domain (whether a house register or a template instantiation)? If not, note that stakeholder-dependent stages will run in ungrounded mode — asking the user directly rather than walking a register — until one is authored.

## 3. Scaffold

Produce the structure per [`templates/flowspace-scaffold.md`](templates/flowspace-scaffold.md):

- **`HUB.md`** (maps to the Confluence parent page): provenance frontmatter (`type: flowspace`), purpose, the **Stage Flow Diagram** (a Mermaid `flowchart LR`, one node per stage — per `references/flow-diagram-guide.md`), the stage table (number, name, review-intensity, data boundary, Layer-3 status), and links.
- **One numbered folder per stage** (`01-<slug>/` …), each with a `CONTEXT.md` per [`templates/stage-context-template.md`](templates/stage-context-template.md) — the six-field contract:
  - **Inputs / Process / Outputs / Verify** — the ICM stage contract (§3.3).
  - **Review** — who reviews this stage's output, at what intensity (from the U-curve mapping), and what evidence the review leaves.
  - **Data boundary** — the max `data-class` this stage handles and the engines sanctioned to touch it.
- **`reference/`** for Layer-3 material and pointers; **`decision-log/`** for the instance's logged calls.

**Populated vs. present** is the authoring standard for every field: could the next stage's owner write their Inputs from your Outputs without a conversation? "Confirm the output is good" fails Verify; naming the two stages, the artifact, and the property being traced passes.

## 4. Layer-3 triage per stage

For each stage, in order:

1. **Reference an existing skill** — pointer in the contract (`Layer-3: <skill-id>`), don't inline what's already canonical.
2. **Inline a one-off** — logic genuinely specific to this flowspace goes directly in the Process field.
3. **Flag a gap** — reusable logic with no existing skill: draft a `skill-primer-brief` into `../skill-foundry/backlog-skill-starters/`, mark the contract `Layer-3: TBD — brief filed (<brief-id>)`, and note the gap in `HUB.md`.

## 5. Staging, validation, and promotion

When the scaffold, Layer-3 triage, and agent-side pre-checks are complete, the foundry moves the flowspace from `backlog-flow-starters/` to **`review-flowspaces/`** — the staging queue for quick human review, at `truth-level: to-review`. This staging move is the foundry's last act on a build; everything after it is the operator's.

A flowspace promotes `to-review` → `verified` when three gates pass (checklist form in [`templates/validation-checklist.md`](templates/validation-checklist.md)):

1. **Structural completeness** — every `CONTEXT.md` fully populated (no placeholders), `HUB.md` frontmatter valid with the stage table matching the folders one-for-one, surface mapping declared, Stage Flow Diagram present and matching the stage table (per the checklist in `references/flow-diagram-guide.md`) with rendering confirmed on both GitLab and Confluence (or the Confluence fallback note if no macro is installed).
2. **Layer-3 status declared** — every stage explicitly: referenced skill (with id), inlined one-off, or flagged gap (with brief id).
3. **Human dry-run** — the operator walks the contracts in order and confirms: Inputs concretely scoped, Process actionable, Outputs specific enough to write the next Inputs from, Verify a real cross-stage check, Review and Data boundary consistent with the sanctioned-tool matrix.

Promotion is recorded as a decision-log entry (reviewer, date, what was checked), and the operator — never the foundry — moves the flowspace from `review-flowspaces/` to `../icp-flows/`. **The foundry never self-promotes.** At the same time, the operator adds or updates the flowspace's row in the "Available flowspaces" table in `../icp-flows/CONTEXT.md`, so the capability catalog never drifts out of sync with what's actually promoted.

## 6. Standalone re-validation (drift check)

On demand or on a schedule, gate 1 re-runs against any existing flowspace — plus the mirror drift check (`methodology/mirroring-protocol.md` §4) if the flowspace is instantiated. Output is a **report, not a re-promotion**: findings go to the operator, who decides whether drift warrants a re-scaffold. Re-validation never changes `truth-level`.

## 7. What this foundry is not

- **Not an explorer.** It receives crystallized intent; it doesn't decide whether a workflow should exist. If that question reopens mid-scaffold, stop and hand back to a thinking session.
- **Not the skill-foundry.** It flags skill gaps with a brief and hands off; it never authors the skill inline.
- **Not an executor.** It builds workspaces; it doesn't run the workflows inside them.
- **Not a self-promoter.** Verified is the operator's call, every time.
- **Not a data handler.** It builds structure; employer content enters only the internal instance, never this repo.

---

## Changelog

- **1.4** (2026-07-03) — Setup questionnaire gains a ninth question: stakeholder
  register availability for the target domain, with the ungrounded-mode
  fallback noted as the consequence of deferring it. Operator-instructed,
  generalizing the `ai-refinement` flowspace's domain-configurable register
  split (`platform-stakeholder-register-template.md`) into the foundry's
  standard intake for any future flowspace with a register dependency.
- **1.3** (2026-07-03) — Operator-instructed: added the review staging queue. Finished builds now move from `backlog-flow-starters/` to `review-flowspaces/` (foundry-placed, `to-review`) to await quick human review — §5 gains the staging step. Promotion semantics unchanged: `../icp-flows/` remains human-placed, `verified` only; the staging move is the foundry's last act on a build.
- **1.2** (2026-07-03) — Two operator-instructed changes. (a) **Invocation gate:** §1 gains Step 0 — the foundry runs only on a confirmed operator instruction; restate starter, classification, and intended outputs and get the go-ahead before building. (b) **DONE queue relocated:** completed flowspace designs now land in the repo's top-level `../icp-flows/` (was `completed-flowspaces/` inside this foundry); promotion semantics unchanged — human-placed, `verified` only. Frontmatter version also realigned with this changelog (the 1.1 entry had not been reflected in `artifact-version`).
- **1.1** (2026-07-03) — Reinstated the Stage Flow Diagram requirement dropped in 1.0. Every `HUB.md` now carries a Mermaid `flowchart LR` per `references/flow-diagram-guide.md` (review-intensity palette, ported from the homelab node-role palette), checked at validation Gate 1. The 1.0 rationale ("Confluence rendering varies") is now a checked setup-questionnaire item and validation condition instead of a reason to skip diagrams: GitLab renders Mermaid natively, Confluence renders it only with a macro installed — both are confirmed per flowspace, and a space without the macro gets a "diagram: see mirror" note rather than a dropped diagram.
- **1.0** (2026-07-02) — Work edition, adapted from the homelab flowspace-foundry v0.5. Kept: dual-path intake with triage, setup questionnaire, ICM 4-field stage contract with populated-vs-present, Layer-3 triage and the demand loop, 3-gate validation, standalone re-validation, human-only promotion. Changed: execution-tier map → **review-intensity map** (U-curve restored to its published human-attention meaning) + **data-boundary field** (sovereignty routing → sanctioned-tool compliance); root context file `AGENTS.md` → `HUB.md` (maps to a Confluence parent page; repo root keeps a single AGENTS.md); added surface-mapping question and mirror drift check to re-validation; contract extended 4 → 6 fields (Review, Data boundary). Dropped: Hermes runtime-router seam, Obsidian/vault graph wiring, Cowork room structure, house-voice enforcement (replaced by "consistent with workplace style guides"), mermaid palette requirements (diagrams optional — Confluence rendering varies).
