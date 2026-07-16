---
id: icp-primer
title: "ICP Primer — Interpretable Context Methodology, Applied"
type: specification
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-16
source: human+ai
data-class: public
related: ["[[provenance-spec]]", "[[mirroring-protocol]]", "[[governance-and-audit]]"]
---

# ICP Primer

What ICM is, what this lab adds to it, and the vocabulary the rest of this repository assumes. Citations for every borrowed idea; the additions are labeled as additions.

---

## 1. ICM — the published methodology

**Interpretable Context Methodology** (Van Clief & McDermott, arXiv:2603.16021, 2026) replaces framework-level agent orchestration with filesystem structure for sequential, human-reviewed workflows. Its claims, in the paper's own arc:

**Folders are the orchestration layer.** Numbered folders represent stages. Plain markdown files carry the prompts and context that tell a single agent what role to play at each step. Local scripts handle mechanical work that doesn't need AI. Files are simultaneously the artifacts of work *and* the coordination mechanism between stages — no separate orchestration layer is needed when the filesystem tracks what has been produced and what depends on it.

**Context lives in a layered hierarchy** (ICM §3.2, Fig. 1). The layers that matter most in practice:

- **Layer 3 — reference material**: stable rules and conventions that persist across runs (`voice.md`, `design-system.md`, style guides, contracts). The model should internalize these as constraints.
- **Layer 4 — working artifacts**: per-run content that changes every time. The model should treat these as the material being worked.

Keeping the two structurally separate matters because they require different kinds of attention (ICM Table 2). In this lab's usage, "a Layer-3 skill" means: a stable, reusable capability definition a stage points at rather than inlines.

**Stage contracts and human-inspectable handoffs** (ICM §3.3, Fig. 4). Each stage reads the previous stage's output, processes it per its own contract, and writes to its own output location. At each boundary, the human can inspect and edit before the next stage runs. This is the methodology's human-in-the-loop mechanism — review is *architectural*, not procedural.

**The U-curve of human attention** (ICM Fig. 5). Practitioner experience: human editing is heavy at the first stage (direction-setting — creative judgment), light through the constrained middle, heavy again at the final stage (aligning output with earlier decisions — "closer to debugging"). The paper notes these values are practitioner self-report, not instrumented measurement.

**Lineage.** The paper grounds ICM in Unix pipeline design, Parnas's decomposition-by-information-hiding (1972), Dijkstra's separation of concerns, multi-pass compilation, and literate programming — and situates it within *context engineering* as articulated by Karpathy (2025) and taxonomized by Martin (LangChain).

"ICP" in this lab = the protocol layer of applying ICM: the standardized folder shapes, contract formats, and naming conventions defined in this repository.

---

## 2. Vocabulary

| Term | Meaning here |
|---|---|
| **Flowspace** | An ICM-structured workspace for one repeatable workflow: a hub document, numbered stage folders, per-stage contracts, a review-intensity map. Built by the flow-foundry. |
| **Skill** | A discrete, reusable AI capability definition: an engine-neutral spec plus per-engine adapters. Built by the skill-foundry. |
| **Foundry** | A production line that turns intent (or foreign material) into a house-standard artifact through triage → build → human review. |
| **Primer-brief** | The clean-path intake artifact: crystallized intent, written down before building starts. `flow-primer-brief` feeds the flow-foundry; `skill-primer-brief` feeds the skill-foundry. |
| **Foreign material** | Any starter not authored under this method — a vendor template, a colleague's prompt, a public repo, a README. Vetted before it is normalized. |
| **Stage contract** | A stage's `CONTEXT.md`: Inputs / Process / Outputs / Verify, plus the two workplace extensions (Review, Data boundary). |
| **Truth-level** | The epistemic lifecycle field: `claimed`, `draft`, `to-review`, `verified`, `deprecated`. See `provenance-spec.md`. |
| **The demand loop** | Flow-foundry finds a stage needing a nonexistent skill → files a skill-primer-brief into the skill-foundry backlog → the built skill becomes the stage's Layer-3 reference. |

---

## 3. What this lab adds to ICM (the house layer)

These are practitioner extensions, not part of the published methodology:

1. **Provenance frontmatter with a truth lifecycle** — every artifact declares its type, origin, AI involvement, and epistemic state. The retrieval-and-trust problem ICM leaves implicit is made explicit. (`provenance-spec.md`)
2. **The human-only verified gate** — `verified` is a promotion only a human performs, with evidence. ICM makes review *possible* at each boundary; the house layer makes it *required* before anything is treated as done.
3. **The dual-foundry pattern with a demand loop** — workflows and capabilities are built by separate, mutually-feeding production lines, so neither is improvised inline.
4. **Triage as the front door, with foreign-material vetting** — provenance, maintenance, license, and security review before normalization. Saying no is a designed outcome.
5. **Queue folders as visible state** — `backlog-*` → in-progress → `completed-*`, where the folder move is the completion signal and only a human moves things to completed.
6. **Populated-vs-present** — the contract-quality test: could the next stage's owner write their Inputs from your Outputs without a conversation?
7. **Boundary declarations** — every foundry and skill carries an explicit "what this is not" list.
8. **Decision logging and audit surface** — non-obvious calls are logged; reviews leave evidence. (`governance-and-audit.md`)
9. **The review-intensity map** — the U-curve (ICM Fig. 5) restored to its original meaning and made operational: each stage in a flowspace is marked `heavy` or `light` for expected human review intensity, so reviewers budget attention where the methodology says it is actually needed. (A prior private implementation repurposed the U-curve for model-tier routing; this edition deliberately returns it to human-attention planning, which is what the paper measured.)
10. **The data-boundary field** — each stage declares what classification of data may enter which AI tool at that stage. This replaces the "sovereignty routing" of self-hosted implementations with the control that matters in an enterprise: sanctioned-tool and data-classification compliance.

---

## 4. Design constraints of this edition

This edition is shaped by three constraints, worth naming because they explain the structure:

1. **The sanctioned engines are Copilot and Rovo.** No self-hosted models, no arbitrary agent frameworks, no control over model routing. Therefore: engine-neutral specs + thin adapters, and no execution-tier machinery.
2. **The source of truth is GitLab.** An ICP instance lives in a single internal GitLab repository that both engines ground on and operate against. Confluence, Jira, and ServiceNow stay in the toolchain as *external systems* — integration targets flows and skills read from and write to at declared data boundaries, not where the methodology's own documents live. Therefore: the single-surface model and the source-of-truth protocol (`mirroring-protocol.md`).
3. **The method must be public; the work must not be.** Therefore: this repo carries method and templates only, and the governance doc draws the line explicitly.
