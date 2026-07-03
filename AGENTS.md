# flow-lab — Agent Briefing

> Read this first, every session, before opening any other file. This is the routing table for the repository.

## What this is

flow-lab is a public method repository: an engine-agnostic implementation of Interpretable Context Methodology (ICM) packaged as two foundries — production lines for AI-assisted work — targeted at workplace toolchains (GitHub Copilot, Copilot agents, Atlassian Rovo).

It holds **method, templates, and sanitized exemplars only**. No employer content, no personal data, no credentials — ever. Instantiated flowspaces live in the operator's employer tenancy (Confluence + internal git mirror), not here.

## Directory map

| Path | What it is |
|---|---|
| `README.md` | The full orientation: methodology, house practice, foundry model, governance. Read it once per session. |
| `methodology/icp-primer.md` | The methodology explainer with citations. The "why" behind every structure here. |
| `methodology/provenance-spec.md` | The canonical frontmatter schema. Every artifact produced in this system is stamped against it. When a template and this spec disagree, the spec wins. |
| `methodology/mirroring-protocol.md` | Confluence ⇄ git mapping rules, the handoff artifact, drift checks. |
| `methodology/governance-and-audit.md` | The gates: data classification at intake, human-only verified promotion, decision logging, review evidence. |
| `flow-foundry/` | Builds flowspaces. `foundry-spec.md` is the method; `templates/` are the molds; `backlog-flow-starters/` → `completed-flowspaces/` is the queue. |
| `skill-foundry/` | Builds skills. `foundry-spec.md` is the method; `templates/` include the engine-neutral skill spec plus Copilot and Rovo adapters; `backlog-skill-starters/` → `completed-skills/` is the queue. |

## How agents operate here

0. **`CONTEXT.md` is the folder's entry point.** Every working folder carries a `CONTEXT.md` — read it before operating in that folder. `README.md` exists only at the repo root, as the public landing page. (Inside a scaffolded flowspace, a stage's `CONTEXT.md` is additionally its six-field stage contract.)
1. **Route through the foundry specs.** Building or normalizing a flowspace → `flow-foundry/foundry-spec.md`. Building or normalizing a skill → `skill-foundry/foundry-spec.md`. Don't re-derive method the spec already defines.
2. **Triage before building.** Classify every starter: primer-brief (clean path), foreign material (vet first — provenance, license, security), or not-worthy (recommend dropping, plainly).
3. **Stamp everything.** Every artifact carries valid frontmatter per `methodology/provenance-spec.md`. New artifacts emit at `truth-level: draft` or `to-review`, never `verified`.
4. **The verified gate is human.** Never promote `truth-level: verified`, never move anything into a `completed-*` folder, never mark a review passed. Build, recommend, and present; the operator approves.
5. **Log non-obvious decisions.** Triage drops, security flags, structural choices — one short entry in the relevant foundry's decision log (see `methodology/governance-and-audit.md`).
6. **Propose structure, don't mint it.** New folders, new stages, new document types get proposed to the operator before creation.
7. **Keep this repo public-safe.** If content arriving in a session looks like employer material, personal data, or credentials, stop and flag it instead of committing it.
