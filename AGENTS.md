# flow-lab — Agent Briefing

> Read this first, every session, before opening any other file. This is the routing table for the repository.

## What this is

flow-lab is a public method repository: an engine-agnostic implementation of Interpretable Context Methodology (ICM) packaged as two foundries — production lines for AI-assisted work — targeted at workplace toolchains (GitHub Copilot, Copilot agents, Atlassian Rovo).

It holds **method, templates, and sanitized exemplars only**. No employer content, no personal data, no credentials — ever. Instantiated flowspaces live in the operator's employer tenancy (an internal GitLab repository — the sole source of truth for an instance), not here.

## Start here: using vs. building

- **"What can I use right now?"** → `icp-flows/CONTEXT.md` and `produced-skills/CONTEXT.md` — catalog tables of every promoted flow and skill, one line each on what it does and when to reach for it. Read the note at the top of each table first: **everything in `icp-flows/` and `produced-skills/` is a sanitized design, not a live agent.** Adding this public repo to a Rovo or Copilot chat lets you read the designs; it does not make any of them executable — each one assumes a private, employer-side GitLab instance (the sole source of truth) that only exists after a human instantiates it there.
- **"I want to build a new flow or skill, or stand up my own instance of this methodology"** → keep reading below (directory map, then rule 2 — confirm before invoking a foundry).

## Directory map

| Path | What it is |
|---|---|
| `README.md` | The full orientation: methodology, house practice, foundry model, governance. Read it once per session. |
| `methodology/icp-primer.md` | The methodology explainer with citations. The "why" behind every structure here. |
| `methodology/provenance-spec.md` | The canonical frontmatter schema. Every artifact produced in this system is stamped against it. When a template and this spec disagree, the spec wins. |
| `methodology/mirroring-protocol.md` | The source-of-truth protocol: GitLab as the single surface, external-system integrations (Confluence/Jira/ServiceNow), the Rovo⇄Copilot handoff artifact. |
| `methodology/governance-and-audit.md` | The gates: data classification at intake, human-only verified promotion, decision logging, review evidence. |
| `flow-foundry/` | Builds flowspaces. `foundry-spec.md` is the method; `templates/` are the molds; `backlog-flow-starters/` is the WIP queue; finished builds stage in `review-flowspaces/` for the human gate — promoted designs land in `icp-flows/`. |
| `skill-foundry/` | Builds skills. `foundry-spec.md` is the method; `templates/` include the engine-neutral skill spec plus Copilot and Rovo adapters; `backlog-skill-starters/` is the WIP queue; finished builds stage in `review-skills/` for the human gate — promoted skills land in `produced-skills/`, and their primer brief moves to `completed-skill-starters/` at the same time. |
| `icp-flows/` | DONE queue for flowspaces: designs that passed the three gates and were promoted `verified` by the operator. Human-placed only. |
| `produced-skills/` | DONE queue for skills: specs + adapters that passed the five-point gate and were promoted `verified` by the operator. Human-placed only. |

## Find it fast

| You need to… | Go to |
|---|---|
| See what flows/skills are available and what they do | `icp-flows/CONTEXT.md` and `produced-skills/CONTEXT.md` (capability tables) |
| Use a **completed** flowspace | `icp-flows/` |
| Use a **completed** skill | `produced-skills/` |
| Build or normalize a flowspace | `flow-foundry/foundry-spec.md` (confirm invocation first — rule 2) |
| Build or revise a skill | `skill-foundry/foundry-spec.md` (confirm invocation first — rule 2) |
| See flowspaces in progress | `flow-foundry/backlog-flow-starters/` |
| See skills in progress | `skill-foundry/backlog-skill-starters/` |
| Review a **finished** flowspace awaiting promotion | `flow-foundry/review-flowspaces/` |
| Review a **finished** skill awaiting promotion | `skill-foundry/review-skills/` |
| See a completed skill's intake record | `skill-foundry/completed-skill-starters/` |
| Stamp or check frontmatter | `methodology/provenance-spec.md` |
| Understand the source-of-truth model / engine handoffs | `methodology/mirroring-protocol.md` |
| Know which gate applies | `methodology/governance-and-audit.md` |
| Understand why any of this exists | `methodology/icp-primer.md` |
| See why a past call was made | The relevant foundry's `decision-log/` (or the flowspace's own `decision-log/`) |

## How agents operate here

0. **`CONTEXT.md` is the folder's entry point.** Every working folder carries a `CONTEXT.md` — read it before operating in that folder. `README.md` exists only at the repo root, as the public landing page. (Inside a scaffolded flowspace, a stage's `CONTEXT.md` is additionally its six-field stage contract.)
1. **Route through the foundry specs.** Building or normalizing a flowspace → `flow-foundry/foundry-spec.md`. Building or normalizing a skill → `skill-foundry/foundry-spec.md`. Don't re-derive method the spec already defines.
2. **Confirm before invoking a foundry.** Foundry work — triage, scaffold, author, adapt, revise — runs only on a confirmed operator instruction. Before starting, restate the starter, its triage classification, and the intended outputs, and get the operator's explicit go-ahead. A starter merely being mentioned, or sitting in a backlog, is not an instruction to build it.
3. **Triage before building.** Classify every starter: primer-brief (clean path), foreign material (vet first — provenance, license, security), or not-worthy (recommend dropping, plainly).
4. **Stamp everything.** Every artifact carries valid frontmatter per `methodology/provenance-spec.md`. New artifacts emit at `truth-level: draft` or `to-review`, never `verified`.
5. **The verified gate is human.** Never promote `truth-level: verified`, never move anything into `icp-flows/` or `produced-skills/`, never mark a review passed. Staging a finished, pre-checked build into the foundry's `review-*` queue (at `to-review`) is the foundry's last move; everything out of that queue — promotion, placement, return — is the operator's. Build, recommend, and present; the operator approves.
6. **Log non-obvious decisions.** Triage drops, security flags, structural choices — one short entry in the relevant foundry's decision log (see `methodology/governance-and-audit.md`).
7. **Propose structure, don't mint it.** New folders, new stages, new document types get proposed to the operator before creation.
8. **Keep this repo public-safe.** If content arriving in a session looks like employer material, personal data, or credentials, stop and flag it instead of committing it.
