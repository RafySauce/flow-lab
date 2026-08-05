# ICP Flows (DONE)

## Workflow catalog

| Flow | Inputs | Outputs | Users |
|---|---|---|---|
| [`ai-refinement`](ai-refinement/HUB.md) | A rough idea, or a decided item set for bulk mode | One committed Jira work item, or a reviewed batch of child items | Anyone raising or decomposing a work item (TPSO lens) |
| [`documentarian`](documentarian/HUB.md) | Evidence from Jira, Confluence, transcripts, delivered work | A created, updated, or archived SOP, MOP, runbook, SAD, KB article, or meeting page | Engineering team leads and platform owners maintaining operational docs |
| [`accomplishments-digest`](accomplishments-digest/HUB.md) | A review period and the engineer's own framing of what mattered | A theme-grouped draft accomplishments document | Engineers prepping for a performance review |
| [`accomplishments-docx-finisher`](accomplishments-docx-finisher/HUB.md) | An approved `accomplishments-digest` document | A finished, house-branded `.docx` | The same engineer, once their draft is approved |
| [`portfolio-rationalization`](portfolio-rationalization/HUB.md) *(to-review)* | A live Jira project/space, or an export | A prioritized disposition packet — close/merge/rewrite/keep recommendations with evidence | Portfolio and delivery managers running a backlog hygiene review |
| [`statik-adoption`](statik-adoption/HUB.md) *(to-review)* | One named service's Jira/ServiceNow board, or conversation where no board exists | A socialized, agreed Kanban system design | Service owners, delivery managers, or coaches |

> **Before you invoke one:** these are complete, engine-neutral designs — you can run one directly in a chat session referencing this repo. Point your agent at [`START-HERE.md`](../START-HERE.md) first: it checks what your session actually has access to (Jira, Confluence, a connected repo, or none of it) and runs the flow within those limits, producing chat/markdown output wherever a live system isn't connected. For full, persistent, audited execution — real Jira/Confluence writes, git history as the audit trail, human-gated promotion — each flow assumes an employer-side source-repo (the GitLab instance that is the sole source of truth for that flow); see [`README.md`'s "Using what's already built"](../README.md#using-whats-already-built) for that deeper path.

Each flow's `HUB.md` frontmatter and opening paragraph are the source of truth for the summaries above; if they ever disagree, the `HUB.md` wins.

---

The repo's top-level landing zone for **completed flowspaces**: designs that
passed all three validation gates (structural completeness, Layer-3 status
declared, human dry-run) and were promoted to `truth-level: verified` **by the
operator** — the foundry never places anything here itself.

Fed from `flow-foundry/review-flowspaces/`, where the foundry stages finished
builds for the gate; the method that gets a design here is
`flow-foundry/foundry-spec.md`, and the promotion is recorded as a
decision-log entry per `methodology/governance-and-audit.md`.

In this public repo, only sanitized, generic flowspace *designs*
(`data-class: public`) live here. Instantiated flowspaces carrying real work
content live in employer tenancy per `../methodology/mirroring-protocol.md`.
