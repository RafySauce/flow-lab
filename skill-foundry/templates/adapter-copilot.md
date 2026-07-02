# Adapter — GitHub Copilot

How to translate an engine-neutral skill spec into Copilot configuration. An adapter adds **format, not logic**: every behavior below must trace to a section of the spec. Copilot's customization surfaces evolve — verify current syntax against GitHub's docs when emitting; this adapter maps *which surface to choose and what goes where*, which is the stable part.

## Choosing the surface

| Spec shape | Copilot surface |
|---|---|
| Always-on conventions for a whole repo (style, structure, provenance stamping) | Repository custom instructions — `.github/copilot-instructions.md` |
| Conventions scoped to certain paths/file types | Path-scoped instruction files — `.github/instructions/*.instructions.md` (with an `applyTo` glob) |
| An on-demand, invocable capability ("run the X procedure now") | Prompt file — `.github/prompts/<skill-slug>.prompt.md` |
| A persistent role with its own method and boundaries, used across sessions | Custom agent definition — `.github/agents/<skill-slug>.md` |
| Repo-level orientation any coding agent should read | `AGENTS.md` at the repo root (cross-engine convention) |

Most foundry skills land as a **prompt file** (capability) or a **custom agent** (role). Rule of thumb: if the spec's "Triggering intent" reads like a command, prompt file; if it reads like a job description, custom agent.

## Mapping the spec

| Spec section | Goes to |
|---|---|
| `description` frontmatter | The prompt file / agent description — Copilot routes on it, keep the fire / don't-fire cases in it |
| Method | The body, near-verbatim; tighten prose, don't add steps |
| Inputs and grounding | Body: name the repo paths/mirror folders to read; state the no-fabrication rules |
| Data boundary | A header line in the body: max data-class and a hard stop instruction if content exceeds it. **Also enforced by humans** — Copilot seeing the instruction is not the control, the sanctioned-tool matrix is |
| What this skill is not | Body, kept intact — this is what prevents scope creep in long sessions |
| Review criteria | Body footer: "before presenting output, self-check against: …" — and unchanged as the human's checklist |

## Emit rules

1. Header comment in the emitted file: `Generated from <skill-slug>/SKILL.md v<version> — do not edit here; edit the spec.`
2. Emitted files go to the **internal** mirror repo (or the product repo the skill serves), through normal PR review — the foundry emits, a human merges.
3. On spec change, regenerate every Copilot artifact and note the version bump; skew between spec and adapter is drift.
