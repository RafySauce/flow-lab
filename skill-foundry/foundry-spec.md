---
id: skill-foundry-spec
title: "Skill Foundry — Method Spec"
type: specification
artifact-version: "1.2"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-03
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[provenance-spec]]", "[[flow-foundry-spec]]"]
---

# Skill Foundry — Method Spec

The method for turning skill intent — or foreign material — into a house-standard skill: an engine-neutral spec plus per-engine adapters, provenance-stamped and human-reviewed. Adapted from a private homelab implementation; work-context changes in the changelog.

---

## 1. Intake and triage (the front door)

**Step 0 — Confirm invocation.** The foundry runs only on a confirmed
operator instruction. Before any triage, build, or revision work: restate the
starter, its triage classification, and the intended outputs, and wait for the
operator's explicit go-ahead. A starter merely being mentioned — or sitting in
the backlog — is not an instruction to build it.

Classify every starter before building:

1. **Skill-primer-brief?** Crystallized intent per [`templates/skill-primer-brief-template.md`](templates/skill-primer-brief-template.md) — from a person, or from the flow-foundry's Layer-3 gap triage. → *Clean path*: transcribe the decided intent into a spec. Don't re-open settled exploration.
2. **Foreign material?** A URL, a colleague's prompt, a vendor agent template, a public repo. → *Normalize path*: run [`templates/intake-vetting-checklist.md`](templates/intake-vetting-checklist.md) **before any building** — provenance, maintenance, license/IP, security read including prompt-injection review. Pass → reverse-engineer the intent and rebuild to house standard. Fail → drop, with a logged reason. Never launder unvetted instructions into a house skill.
3. **Not skill-worthy?** Marketing dressed as a tool, an abandoned source, a capability the toolkit already has, or something too one-off to reuse. Say so plainly; recommend dropping or routing (a multi-stage workflow is a flowspace — hand to the flow-foundry). Dropping is a normal, logged outcome.
4. **Bare conversation?** Workable — but surface the primer-brief's questions (what is this *for*, when should it *fire*, what must it *never* do) rather than guessing.

## 2. Author the engine-neutral spec

Per [`templates/skill-spec-template.md`](templates/skill-spec-template.md). The spec carries everything engine-independent:

- **Flow Diagram** — a Mermaid `flowchart LR` per [`references/flow-diagram-guide.md`](references/flow-diagram-guide.md): trigger → steps → terminal output, flat chain, house node-role palette. A visual complement to Method, not a replacement.
- **Purpose and triggering intent** — what it does; the situations (and phrasings) that should invoke it, and the near-misses that shouldn't.
- **Method** — the steps, the quality bar, worked examples where behavior is easy to get wrong.
- **Inputs and grounding** — what context/sources the skill needs, and its **data boundary**: the max `data-class` it may handle and which engines are sanctioned to run it.
- **Boundaries — "what this skill is not"** — the explicit non-goals that keep skills from drifting into each other.
- **Review criteria** — how a human judges an output of this skill acceptable; this becomes the verification test at the gate.

Authoring standards: populated-vs-present applies to every section; the spec must be executable by an informed stranger; keep it consistent with workplace style/tone guidelines.

## 3. Emit adapters

For each engine the skill will run on, translate the spec mechanically:

- **Copilot** → [`templates/adapter-copilot.md`](templates/adapter-copilot.md): repository custom instructions, path-scoped instruction files, a prompt file, or a custom agent definition — the adapter doc maps which to choose.
- **Rovo** → [`templates/adapter-rovo.md`](templates/adapter-rovo.md): a Rovo agent definition (instructions, knowledge scoping, permitted actions).

Adapter rules: an adapter adds **format, not logic** — if the adapter needs behavior the spec lacks, fix the spec; every adapter states which spec version it was generated from; when the spec changes, all adapters regenerate (version skew between adapters is drift — flag it).

## 4. Stamp and stage

- Provenance frontmatter on the skill card (`type: skill`, `generated-by: skill-foundry`, `source`, `data-class`), per `methodology/provenance-spec.md`.
- The skill folder: `<skill-slug>/` containing `SKILL.md` (the spec — shaped after the agentskills.io convention: `name` + `description` frontmatter, method in the body), `adapters/`, and optional `reference/`.
- Land it in the backlog at `truth-level: to-review` and present it for review.

## 5. Review and promotion (human gate)

The operator promotes `to-review` → `verified` when:

1. **Spec review** — purpose sharp, triggering intent specific (name the misfire cases), boundaries explicit, review criteria usable, Flow Diagram present and matching the Method prose one-for-one (per `references/flow-diagram-guide.md`), with rendering confirmed on GitLab and on Confluence (or the macro-missing fallback noted).
2. **Live test on the target engine** — at least one real invocation per adapter, on `public`/synthetic data, judged against the spec's review criteria.
3. **Trigger check** — the skill fires on its intended situations and *not* on its near-misses.
4. **Boundary/collision check** — no overlap with an existing skill's declared territory; if overlap exists, resolve it (merge, split, or redraw boundaries) before promotion.
5. **Evidence recorded** — the review leaves a decision-log entry (reviewer, date, what was tested).

Then the operator — never the foundry — moves the skill to `../produced-skills/` (the repo's top-level DONE queue) and deploys the adapters to their engines (Rovo agent published; Copilot files merged to the internal repo).

## 6. Maintenance

- A deployed skill that changes engines, changes behavior, or goes stale gets re-reviewed; superseded versions go `status: replaced` + `superseded-by`.
- A periodic collision/coverage audit (fold into the quarterly audit pass, `governance-and-audit.md` §8) reads all skill boundaries against each other.

## 7. What this foundry is not

- **Not an explorer.** It doesn't decide whether a capability should exist; a reopened "what is this for" goes back to a thinking session.
- **Not the flow-foundry.** Multi-stage workflows are flowspaces; it hands them off.
- **Not a code launderer.** Foreign material is vetted or dropped — never quietly rebranded.
- **Not an engine partisan.** The spec is the asset; engines are deployment targets.
- **Not a self-promoter.** Verified, completed, deployed — all human calls.

---

## Changelog

- **1.2** (2026-07-03) — Two operator-instructed changes. (a) **Invocation gate:** §1 gains Step 0 — the foundry runs only on a confirmed operator instruction; restate starter, classification, and intended outputs and get the go-ahead before building. (b) **DONE queue relocated:** completed skills now land in the repo's top-level `../produced-skills/` (was `completed-skills/` inside this foundry); promotion semantics unchanged — human-placed, `verified` only. Frontmatter version also realigned with this changelog (the 1.1 entry had not been reflected in `artifact-version`).
- **1.1** (2026-07-03) — Reinstated the Flow Diagram requirement dropped in 1.0. Every skill spec now carries a Mermaid `flowchart LR` per `references/flow-diagram-guide.md` (node-role palette, ported unchanged from the homelab skill-foundry), checked at the spec-review gate. Reinstated alongside the matching flow-foundry change: GitLab renders Mermaid natively, Confluence needs a macro — both confirmed per skill rather than skipping diagrams outright.
- **1.0** (2026-07-02) — Work edition, adapted from the homelab skill-foundry v0.2.6. Kept: dual-path intake with triage front door, foreign-material vetting, boundary discipline, human-only promotion, queue folders, provenance stamping, collision checking. Changed: the Claude skill-creator "engine room" (eval loop, benchmark scripts, `.skill` packaging) → **engine-neutral spec + per-engine adapters** with a live-test review gate, since the workplace engines (Copilot, Rovo) each have their own definition formats and no shared eval harness; execution-tier field → data-boundary section; house-voice enforcement → workplace-style consistency; graduation checklist (symlinks, slash-command index) → adapter deployment by the operator. Dropped: Hermes-baseline seam, Cowork rooms/instrumentation, traces→synthesis→agent-spec loop (decision log + quarterly synthesis remain as the audit/improvement mechanism), Obsidian vault companion docs and Connection Notes.
