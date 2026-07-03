# flow-lab

**A portable, engine-agnostic implementation of Interpretable Context Methodology (ICM) for workplace AI tooling — GitHub Copilot, Copilot agents, and Atlassian Rovo.**

This repository contains two *foundries* — repeatable production lines for AI-assisted work:

- **`flow-foundry/`** — builds *flowspaces*: multi-stage, human-reviewed AI workflows expressed as folder structure and markdown contracts.
- **`skill-foundry/`** — builds *skills*: discrete, reusable AI capability definitions, authored once in an engine-neutral spec and adapted to whichever engine will run them (Rovo agent, Copilot custom agent, Copilot prompt file).

The repository holds the **method, templates, and sanitized exemplars only**. Instantiated flowspaces containing real work content live inside your employer's tenancy (Confluence + an internal git mirror) — never here. See [Governance](#governance-your-work-is-your-responsibility).

---

## Table of contents

1. [The methodology: ICM in brief](#the-methodology-icm-in-brief)
2. [How I apply it (house practice)](#how-i-apply-it-house-practice)
3. [The two foundries](#the-two-foundries)
4. [The dual-surface model: Atlassian primary, Copilot mirror](#the-dual-surface-model-atlassian-primary-copilot-mirror)
5. [How to use this yourself](#how-to-use-this-yourself)
6. [Governance: your work is your responsibility](#governance-your-work-is-your-responsibility)
7. [Sources and citations](#sources-and-citations)

---

## The methodology: ICM in brief

**Interpretable Context Methodology (ICM)** is a published method for orchestrating AI agent workflows using folder structure, markdown files, and local scripts instead of framework-level orchestration code (Van Clief & McDermott, 2026 — see [Sources](#sources-and-citations)). Its central observation:

> If the prompts and context for each stage of a workflow already exist as files in a well-organized folder hierarchy, you do not need a coordination layer — the filesystem tracks what has been produced and what depends on it.

The core mechanics, all from the paper:

- **Numbered folders represent stages.** One agent, reading the right files at the right moment, does the work that would otherwise require a multi-agent framework.
- **Plain markdown carries the context.** Each stage's folder holds the prompt and context that tell the agent what role to play at that step.
- **A layered context hierarchy** separates stable *reference material* (rules, conventions, style guides — "Layer 3") from per-run *working artifacts* ("Layer 4"). Reference material persists across runs; working artifacts change every time. Keeping them structurally separate matters because the model should treat one as constraints and the other as content (ICM §3.2, Table 2).
- **Stage contracts and handoffs.** Each stage reads from the previous stage's output, processes it according to its own contract, and writes to its own output location. *At each boundary, the human can inspect and edit the output before the next stage runs* (ICM §3.3, Fig. 4).
- **Human attention follows a U-curve.** Practitioner experience shows human editing is heavy at stage 1 (direction-setting is creative judgment), light in the constrained middle stages, and heavy again at the final stage (aligning output with earlier decisions — "closer to debugging") (ICM Fig. 5).

The paper grounds this in a long software-engineering lineage: Unix pipeline design, Parnas's modular decomposition (1972), Dijkstra's separation of concerns, multi-pass compilation, and literate programming. It positions ICM within the practitioner discipline Andrej Karpathy named **context engineering** (June 2025): filling the context window with the right information — instructions, retrieved knowledge, prior outputs — structured so the model can use them effectively.

Throughout this repo, "ICP" refers to the practice of applying ICM — the protocol layer (folder shapes, contracts, naming) this lab has standardized on. ICM is the published methodology; ICP is how it's operationalized here.

---

## How I apply it (house practice)

Everything in this section is **my own practice layered on top of ICM**, developed and battle-tested in a private homelab implementation before being ported here. Where the paper is cited above, this section is not the paper — treat it as one practitioner's opinionated extension.

**1. A provenance and truth lifecycle on every artifact.**
Every document carries frontmatter declaring what it is, who/what made it, and how much to trust it. The load-bearing field is `truth-level`:

```
claimed → (external material, ingested untouched — separate branch)
draft → to-review → verified → deprecated   (linear progression)
```

`verified` means a human confirmed it against reality. See [`methodology/provenance-spec.md`](methodology/provenance-spec.md).

**2. The verified gate is always human.**
AI builds, normalizes, and recommends. A human approves. Nothing self-promotes to `verified`, and nothing moves into a `completed-*` folder without human review. This is not ceremony — it is the single control that keeps an AI-heavy pipeline auditable, and it aligns with the human-oversight expectations emerging in regulation (see the paper's own citations of the human-oversight literature, including EU AI Act Article 14 analysis).

**3. Two foundries, one demand loop.**
Workflows (flowspaces) and capabilities (skills) are built by separate production lines that feed each other: when the flow-foundry scaffolds a stage that needs a skill that doesn't exist, it drafts a *skill-primer-brief* into the skill-foundry's backlog. Flow demand drives skill supply.

**4. Triage is the front door.**
Every incoming starter is classified before anything is built: a *primer-brief* (clean, crystallized intent) takes the transcription path; *foreign material* (a URL, README, someone else's prompt, a vendor template) is **vetted first** — provenance, maintenance, license, security — then normalized; and some starters are *not worthy* — saying no is a legitimate, frequent triage outcome.

**5. Queues are the visible pipeline.**
Work-products physically sit in folders that encode their state: `backlog-*` (inbox) → in progress → `review-*` (built, staged for the human gate) → the top-level DONE queues (human-placed only). The folder move *is* the completion signal; `truth-level` is the provenance that travels with the document.

**6. Populated vs. present.**
A contract field is *populated* when its content is specific, not merely filled in. "Confirm the output is good" fails; "confirm Stage 3's categories match the list established in Stage 1's outputs" passes. The test: could the next stage's owner write their Inputs section from your Outputs section without a conversation?

**7. Boundary discipline.**
Every foundry and skill declares what it is *not*, explicitly. Overlapping tools drift into each other; a written non-goal list is the cheapest defense.

**8. Decision logging.**
Non-obvious calls — a triage drop, a security flag, a structural choice — get a short logged entry. An unlogged decision teaches the system nothing and leaves nothing for an audit to find.

---

## The two foundries

```
     primer-brief (crystallized intent)  ┐
     foreign material (vet first!)       ┘──>  backlog-*-starters/   (inbox)
                                                   │
                                               [TRIAGE]
                                                   │
                                              FOUNDRY BUILD          (scaffold / author / stamp)
                                                   │
                                 review-flowspaces/ | review-skills/  (staged; foundry-placed, to-review)
                                                   │
                                            [HUMAN REVIEW GATE]
                                                   ▼
                                     icp-flows/ | produced-skills/   (top level; verified, human-placed)

     flow-foundry ── "this stage needs a skill that doesn't exist" ──> skill-foundry backlog
     skill-foundry ── produces the skill ──> flowspace references it as Layer-3
```

- **[`flow-foundry/`](flow-foundry/)** scaffolds flowspaces: stage decomposition, per-stage contracts (Inputs / Process / Outputs / Verify, plus two workplace extensions — Review and Data boundary), a Mermaid Stage Flow Diagram rendered on both GitLab and Confluence, a review-intensity map, and validation gates. Read its [CONTEXT.md](flow-foundry/CONTEXT.md) and [foundry-spec](flow-foundry/foundry-spec.md).
- **[`skill-foundry/`](skill-foundry/)** authors skills as an **engine-neutral spec** plus per-engine adapters (Rovo agent definition, Copilot custom agent / prompt file). Read its [CONTEXT.md](skill-foundry/CONTEXT.md) and [foundry-spec](skill-foundry/foundry-spec.md).

Both foundries share the same intake/triage/review skeleton. Neither ever self-promotes its output.

---

## The dual-surface model: Atlassian primary, Copilot mirror

This edition of the foundries is built for a constraint common in enterprise environments: **the sanctioned AI tools are GitHub Copilot (and Copilot agents) and Atlassian Rovo**, and knowledge lives in Confluence/Jira while code lives in git.

The design response:

| Surface | Role | What lives there |
|---|---|---|
| **Confluence (Atlassian)** | **System of record.** The primary ICP instance. | Flowspace page trees, stage contracts as pages, decision logs, review sign-offs. Rovo agents operate here natively. |
| **Internal git repo** | **Copilot mirror.** | A markdown mirror of the Confluence structure so Copilot (chat, agents, coding agent) can read the same contracts. Handoffs between Rovo and Copilot travel through this mirror. |
| **This public repo (flow-lab)** | **Method only.** | Foundry specs, templates, sanitized exemplars. No employer content, ever. |

The mapping rules, handoff artifact, and drift checks are specified in [`methodology/mirroring-protocol.md`](methodology/mirroring-protocol.md). The short version: folder ↔ page tree, `HUB.md` ↔ parent page, stage `CONTEXT.md` ↔ child page, frontmatter ↔ page properties/labels; the git mirror is regenerated from Confluence (one direction of truth), and a periodic drift check compares the two.

---

## How to use this yourself

1. **Read the methodology folder** — [`icp-primer.md`](methodology/icp-primer.md) (the method, with citations), [`provenance-spec.md`](methodology/provenance-spec.md) (the frontmatter schema), [`governance-and-audit.md`](methodology/governance-and-audit.md) (the gates you must not skip).
2. **Stand up your surfaces.** Create a Confluence space (or section) for your primary ICP instance, and an internal repo for the Copilot mirror. Copy this repo's `flow-foundry/` and `skill-foundry/` trees into them as the starting structure.
3. **Run the flow-foundry on your first real workflow.** Pick a genuinely repeatable, multi-stage process with human review points (a report cycle, an intake process, a review pipeline). Fill in a [flow-primer-brief](flow-foundry/templates/flow-primer-brief-template.md), then follow [flow-foundry/foundry-spec.md](flow-foundry/foundry-spec.md) to scaffold it.
4. **Let flowspace gaps drive skill builds.** When a stage needs a capability that doesn't exist, file a [skill-primer-brief](skill-foundry/templates/skill-primer-brief-template.md) into the skill-foundry backlog and build it there — engine-neutral spec first, then the adapter for the engine that stage runs on.
5. **Hold the gates.** Data-classification check at intake. Human review before anything is `verified`. Decision log entries for non-obvious calls. Drift check on the mirror.
6. **Adapt the enums, keep the skeleton.** Your document types, data classes, and stage names will differ. The skeleton — triage front door, stage contracts, human gate, queues — is the part that transfers.

You do **not** need Copilot or Rovo specifically. The specs are engine-neutral by design; the adapters are the only engine-specific parts, and writing a new adapter (for Claude, Gemini Enterprise, a local model) is a template exercise.

---

## Governance: your work is your responsibility

Read this section before using anything in this repository.

- **All AI-generated work products are yours to quality-gate.** Every artifact an AI produces under these foundries — documents, code, agent definitions, summaries — must be reviewed by a qualified human before it is relied upon, shipped, or represented as complete. The `verified` truth-level exists precisely so that unreviewed output is visibly unreviewed. Do not skip the gate; do not automate it away.
- **Source-review everything AI hands you.** AI output can be wrong, outdated, fabricated, or subtly misaligned with your context. Check claims against primary sources. Check generated code for correctness, security, and license contamination. Check summaries against the documents they summarize. The foundries build review points into the structure; using them is on you.
- **Foreign material gets vetted, not laundered.** Prompts, templates, agent definitions, and repos from outside your control pass the [intake vetting checklist](skill-foundry/templates/intake-vetting-checklist.md) — provenance, maintenance, license, security read — before they are normalized into your toolkit. Never wrap unvetted third-party instructions in your own branding and call them yours.
- **Your employer's policies override this repo.** Data classification, acceptable-use, AI-tool sanctioning, IP, and disclosure policies at your workplace take precedence over anything written here. Nothing in this repository is legal, compliance, or security advice.
- **Keep work content out of public surfaces.** This repo is public by design and holds method only. Instantiated flowspaces, decision logs, and anything touching employer data stay inside employer tenancy.

---

## Sources and citations

**The methodology:**

- J. Van Clief and D. McDermott, *"Interpretable Context Methodology: Folder Structure as Agent Architecture,"* Eduba / University of Edinburgh, arXiv:2603.16021, 2026. The ICM paper — stages as folders, markdown as context, the layered context hierarchy, stage contracts with human-inspectable boundaries, and the U-curve of human editing attention. The protocol it describes is open source under the MIT license. Everything in [The methodology](#the-methodology-icm-in-brief) above derives from this paper.

**Intellectual lineage (as cited within the ICM paper):**

- D. L. Parnas, *"On the Criteria To Be Used in Decomposing Systems into Modules,"* CACM, 1972 — decomposition by information hiding.
- E. W. Dijkstra — "separation of concerns."
- Unix pipeline design; multi-pass compiler architecture; D. Knuth's literate programming.
- A. Karpathy, on "context engineering" as the successor framing to prompt engineering, June 2025; L. Martin (LangChain), context-engineering strategy taxonomy.
- Anthropic, *"Introducing the Model Context Protocol,"* November 2024.
- Human-oversight and automation literature: R. Parasuraman et al. on types and levels of human interaction with automation; M. Fink, *"Human Oversight under Article 14 of the EU AI Act,"* SSRN 5147196, 2025.

**Formats and tooling conventions:**

- The [agentskills.io](https://agentskills.io) skill format (`SKILL.md` with `name`/`description` frontmatter) — the neutral skill packaging convention the skill-foundry's spec template is shaped after.
- `AGENTS.md` as the cross-engine root-context convention recognized by GitHub Copilot and other coding agents.
- GitHub Copilot customization surfaces (repository instructions, prompt files, custom agents) and Atlassian Rovo agents — see the adapters in [`skill-foundry/templates/`](skill-foundry/templates/).

**House practice (my own):**

- The provenance/truth-level lifecycle, the dual-foundry demand loop, the triage front door with foreign-material vetting, the human-only verified gate, the queue-folder pipeline, the populated-vs-present contract discipline, boundary declarations, and decision logging are **my own practices**, developed in a private homelab ICM implementation and generalized here. They are opinionated extensions of ICM, not part of the published methodology — disagree with them freely.

---

*Maintained as a public method repo. Contributions and forks welcome; employer data is not.*
