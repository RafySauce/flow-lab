# Adapter — Atlassian Rovo

How to translate an engine-neutral skill spec into a Rovo agent definition. Same rule as every adapter: **format, not logic** — if the agent needs behavior the spec lacks, fix the spec first. Rovo's agent-builder surface evolves — verify current fields against Atlassian's docs when emitting; the mapping below is the stable part.

## When Rovo is the right engine

- The skill's inputs live in Confluence/Jira and its **data boundary says the content shouldn't leave Atlassian**.
- The skill acts *on* Atlassian objects (creates pages, updates issues, comments).
- The users who invoke it work in Atlassian, not in an IDE.

If the skill is code-shaped or repo-grounded, it's a Copilot skill; if it's both, emit both adapters from the same spec.

## Mapping the spec

| Spec section | Rovo agent field |
|---|---|
| `name` + `description` | Agent name + description — keep the fire / don't-fire cases in the description; users and Rovo routing both read it |
| Method | Agent instructions, near-verbatim. Lead with the role sentence, then the steps |
| Inputs and grounding | Knowledge scoping: the specific Confluence spaces / Jira projects the agent may read. Scope **narrowly** — grounding scope is a data-boundary control, not a convenience setting |
| Data boundary | Enforced structurally: knowledge scope + permitted actions define what the agent can touch. Instructions restate the boundary as a stop rule |
| What this skill is not | Instructions, kept intact, phrased as refusals-with-redirects ("if asked to X, decline and point to Y") |
| Review criteria | Instructions footer: self-check before responding — and unchanged as the human reviewer's checklist |
| Actions (if the skill writes) | Permitted actions, minimum set. A skill whose spec doesn't state it writes gets **no** write actions |

## Emit rules

1. The agent definition text is kept as `adapters/rovo-agent.md` in the skill folder (the copy of record), then configured in Rovo by a human — record the agent's live name/location in the skill card when deployed.
2. Header line in the definition: `Generated from <skill-slug>/SKILL.md v<version> — edit the spec, not the live agent.` Live-agent edits that bypass the spec are drift; the quarterly audit compares live instructions to the spec.
3. Test on synthetic/`public` content before pointing the agent at real spaces (the live-test promotion gate).
