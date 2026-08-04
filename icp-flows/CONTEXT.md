# ICP Flows (DONE)

## Available flowspaces

| Flow | What it does | Use it when |
|---|---|---|
| [`ai-refinement`](ai-refinement/HUB.md) | Turns a rough idea into a Jira-ready work item through disciplined, per-field refinement with the TPSO persona, stakeholder grounding, and explicit confirmation at every step — one run = one committed work item. Where you already hold the item set (a spreadsheet, an export, a list), bulk creation mode instead builds the whole set in one reviewed pass, behind a separate acknowledgment. | You need to refine and commit a new (or decomposed) Jira work item — or create many child items you've already decided on. |
| [`documentarian`](documentarian/HUB.md) | Produces, updates, and maintains operational documentation (SOPs, MOPs, runbooks, SADs, ServiceNow KB articles, meeting pages) from evidence in Jira, Confluence, transcripts, and delivered work; hands candidate work items back to `ai-refinement`. | You need to create, update, or hand over custody of a piece of operational documentation. |
| [`accomplishments-digest`](accomplishments-digest/HUB.md) | Turns a review period's Jira and Confluence activity into a single, outcome-framed accomplishments document grouped by theme, carrying the engineer's own read on impact. | You're prepping for a performance review and need a first-draft accomplishments document. |
| [`accomplishments-docx-finisher`](accomplishments-docx-finisher/HUB.md) | Companion to `accomplishments-digest`: turns an already human-approved accomplishments document into a final, house-branded `.docx`, adding supporting (not new) evidence via Copilot repo access. | You've approved an `accomplishments-digest` output and need it as a finished, styled Word file. |
| [`portfolio-rationalization`](portfolio-rationalization/HUB.md) | Turns a whole Jira project or space into a prioritized, evidence-carrying portfolio review pack — profiles the portfolio's shape, maps every item to strategic objective areas, scores closure risk across five corroborating dimensions, and builds a per-item disposition packet routed to owners. Writes nothing to Jira. *(`truth-level: to-review` — score calibration and the objective dictionary are still operator-gated; see the flow's Known gaps.)* | You need a hygiene and objective-alignment review of a Jira portfolio — what to close, merge, rewrite, or keep — with the evidence behind each call. |
| [`statik-adoption`](statik-adoption/HUB.md) | Designs a Kanban system for one named service by working through STATIK, using the service's Jira or ServiceNow board as evidence wherever it exists and structured conversation where it doesn't, ending in a system design socialized and agreed with stakeholders. *(`truth-level: to-review` — evidence-sufficiency floors are reasoned, not calibrated; see the flow's Known gaps.)* | You need to introduce or redesign a Kanban system for a specific service, grounded in real demand and capability data rather than a copied template. |

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
