# Skill Foundry

The production line for **skills** — discrete, reusable AI capability definitions. Each skill is authored once as an **engine-neutral spec** and then adapted to the engine that will run it: an Atlassian Rovo agent, a GitHub Copilot custom agent, or a Copilot prompt file. This folder is the *where*; [`foundry-spec.md`](foundry-spec.md) is the *how*.

## Layout

```
skill-foundry/
├── CONTEXT.md                   # this file — read before working in this folder
├── foundry-spec.md              # the method: triage → vet → author → adapt → review
├── templates/
│   ├── skill-primer-brief-template.md  # intake path 1: crystallized intent
│   ├── skill-spec-template.md          # the engine-neutral core spec
│   ├── adapter-copilot.md              # emitting Copilot instructions/prompt files/agents
│   ├── adapter-rovo.md                 # emitting Rovo agent definitions
│   └── intake-vetting-checklist.md     # the foreign-material gate (shared with flow-foundry)
├── references/
│   └── flow-diagram-guide.md    # Flow Diagram syntax, palette, GitLab/Confluence rendering check
├── backlog-skill-starters/      # INBOX: primer-briefs + foreign starters (claimed / to-review)
└── decision-log/                # non-obvious foundry calls
```

The DONE queue lives at the repo top level: completed, human-verified skills
land in [`../produced-skills/`](../produced-skills/) (human-placed only).

## The queue model

```
skill-primer-brief (clean intent)        ┐
  ← from a person, or from the           │──>  backlog-skill-starters/
     flow-foundry's Layer-3 gap triage   ┘         │  [triage → vet (if foreign) → author → adapt → review]
foreign material (URL, prompt, repo)               ▼
                                              ../produced-skills/    (human gate; repo top level)
```

Truth-levels track the lifecycle exactly as in the flow-foundry: `claimed` → `to-review` → `verified`, human-promoted only.

## One skill = one spec + N adapters

The core spec ([`templates/skill-spec-template.md`](templates/skill-spec-template.md)) carries everything engine-independent: purpose, triggering intent, method, boundaries ("what this skill is not"), and review criteria. Adapters are thin, mechanical translations into engine configuration — if an adapter needs logic the spec doesn't have, the spec is incomplete, fix it there. This keeps capabilities portable across engines (and across employers' tool choices).

## The demand loop

Most skill demand arrives from the flow-foundry: a flowspace stage that needs a capability that doesn't exist files a `skill-primer-brief` here. The built skill then becomes that stage's Layer-3 reference, closing the loop.
