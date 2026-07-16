# Flow Foundry

The production line for **flowspaces** — ICM-structured, human-reviewed, multi-stage AI workflows. This folder is the *where* (the queue the work moves through); [`foundry-spec.md`](foundry-spec.md) is the *how*.

## Layout

```
flow-foundry/
├── CONTEXT.md                   # this file — read before working in this folder
├── foundry-spec.md              # the method: triage → setup → scaffold → validate
├── templates/
│   ├── flow-primer-brief-template.md   # intake path 1: crystallized intent
│   ├── flowspace-scaffold.md           # the output shape: HUB.md + stage folders
│   ├── stage-context-template.md       # the 6-field stage contract
│   └── validation-checklist.md         # the three promotion gates, as a checklist
├── references/
│   └── flow-diagram-guide.md    # Stage Flow Diagram syntax, palette, GitLab/Confluence rendering check
├── backlog-flow-starters/       # INBOX: primer-briefs + foreign starters (claimed / draft)
├── review-flowspaces/           # STAGED: finished builds awaiting the human gate (to-review)
└── decision-log/                # non-obvious foundry calls, one file per entry
```

Finished builds stage in [`review-flowspaces/`](review-flowspaces/) — the
foundry's last move. The DONE queue lives at the repo top level: completed,
human-verified flowspace designs land in [`../icp-flows/`](../icp-flows/)
(human-placed only).

## The queue model

```
flow-primer-brief (clean intent)   ┐
foreign workflow material (vetted) ┘──>  backlog-flow-starters/
                                              │  [triage → scaffold → pre-check]
                                              ▼
                                         review-flowspaces/    (foundry-staged, to-review)
                                              │  [HUMAN GATE: three validation gates]
                                              ▼
                                         ../icp-flows/    (human-placed; repo top level)
```

Truth-levels track the lifecycle: `claimed` (foreign, ingested untouched) → `draft`/`to-review` (primer-brief or post-scaffold) → `verified` (promoted by the operator after the three validation gates). Staging a finished build in `review-flowspaces/` is the foundry's last move; every move out of it is the operator's. **The foundry never self-promotes.**

## Where flowspaces actually run

This public repo holds the foundry itself and *sanitized exemplars only*. Real flowspaces are instantiated in employer tenancy — the source-repo, an internal GitLab repository that is the sole source of truth for the instance, which both engines ground on (Rovo via the GitLab connector, Copilot natively) — per [`methodology/mirroring-protocol.md`](../methodology/mirroring-protocol.md). A completed flowspace here means the *design* is done and generic; instances live where the work lives.

## The demand loop

Every Layer-3 gap found while scaffolding — a stage that needs a skill that doesn't exist — becomes a `skill-primer-brief` filed into [`../skill-foundry/backlog-skill-starters/`](../skill-foundry/backlog-skill-starters/). Flow demand feeds skill supply.
