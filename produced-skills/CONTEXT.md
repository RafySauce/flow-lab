# Produced Skills (DONE)

## Available skills

| Skill | What it does | Invoke when |
|---|---|---|
| [`context-elicitation`](context-elicitation/SKILL.md) | Extracts structured problem context (problem statement, business outcomes, customer value, stakeholder tags) through a guided question sequence. | Stage 02 of `ai-refinement`, or a vague idea needs framing into schema-ready statements. |
| [`scope-dependency-mapper`](scope-dependency-mapper/SKILL.md) | Turns a confirmed problem statement into scope, dependency, and risk outputs with stakeholder/conflict annotations. | Stage 03 of `ai-refinement`. |
| [`field-refinement-cadence`](field-refinement-cadence/SKILL.md) | Drives per-field drafting of the remaining Jira schema fields with confirmation, conflict detection, and acceptance-criteria reframing. | Stage 04 of `ai-refinement`. |
| [`value-decomposition`](value-decomposition/SKILL.md) | Proposes candidate child work items one hierarchy level down from a parent item, grounded in the value-delivery deck. | Stage 01 of `ai-refinement`, when the user asks to decompose/break down a parent-level item. |
| [`workitem-validation`](workitem-validation/SKILL.md) | Runs the completeness/constraint gate on a refined work item — schema, labels, formatting, acceptance criteria — with a pass/fail report. | Stage 05 of `ai-refinement`. |
| [`jira-commit`](jira-commit/SKILL.md) | Maps a signed-off payload to Jira fields, resolves hierarchy/dependency links and labels, shows a dry-run preview, and executes the commit. | Stage 06 of `ai-refinement`, with a signed-off Stage 05 payload. |
| [`jira-accomplishments-gatherer`](jira-accomplishments-gatherer/SKILL.md) | Queries an engineer's own closed Jira work in a date range, clusters it by theme, and reframes it in outcome language. | Stage 2 of `accomplishments-digest`, or standalone on "pull my closed work for \<period\>." |
| [`confluence-contribution-gatherer`](confluence-contribution-gatherer/SKILL.md) | Queries an engineer's authored Confluence pages and available collaboration signal in a date range, framed as scope/leadership evidence. | Stage 3 of `accomplishments-digest`, or standalone on "what docs did I write this quarter." |
| [`accomplishments-drafter`](accomplishments-drafter/SKILL.md) | Synthesizes the framing brief plus Jira and Confluence digests into the house accomplishments-document shape, theme-structured and outcome-framed. | Stage 4 of `accomplishments-digest`, once all three upstream inputs exist. |
| [`repo-context-enricher`](repo-context-enricher/SKILL.md) | Pulls supporting (never new) evidence from an authorized repo/file scope to reinforce an already-approved accomplishments document, flagging every addition. | Stage 1 of `accomplishments-docx-finisher`, with a handoff file in hand. |
| [`accomplishments-docx-stylizer`](accomplishments-docx-stylizer/SKILL.md) | Applies the house Word template/branding to enriched accomplishments content and produces the final `.docx`. | Stage 2 of `accomplishments-docx-finisher`, with Stage 1's enriched content set. |
| [`contract-reviewer`](contract-reviewer/SKILL.md) | Pre-reviews a flowspace's stage contracts against the populated-vs-present standard, emitting a severity-ranked findings report. | A flowspace reaches `to-review`, on "pre-review these contracts," or a re-validation pass. |
| [`provenance-stamper`](provenance-stamper/SKILL.md) | Stamps and validates provenance frontmatter against `methodology/provenance-spec.md`, inferring what it can and asking for owner/data-class. | On "stamp this," "is this schema-compliant," creating any new ICP artifact, or a batch check across a folder/page tree. |

> **Before you invoke one:** everything above is a sanitized *design*, not a live agent. Each skill assumes an employer-side source-repo (the GitLab instance that is the sole source of truth for that skill) and, for the adapter you want, an actually deployed Rovo agent or Copilot custom agent/prompt file — none of which exist in this public repo. Opening a `SKILL.md` shows the design and its adapters; deploying one is the operator's act (see the note at the bottom of this page). See [`README.md`'s "Using what's already built"](../README.md#using-whats-already-built) for the path from design to running instance.

Each skill's `SKILL.md` `description` frontmatter is the source of truth for the summaries above (it also states what each skill is *not* for) — if they ever disagree, the `SKILL.md` wins.

---

The repo's top-level landing zone for **completed skills**: skills that passed
the five-point review gate (spec review, live test per adapter, trigger check,
collision check, evidence recorded) and were promoted to
`truth-level: verified` **by the operator** — the foundry never places
anything here itself.

Fed from `skill-foundry/review-skills/`, where the foundry stages finished
builds for the gate; the method that gets a skill here is
`skill-foundry/foundry-spec.md`, and the promotion is recorded as a
decision-log entry per `methodology/governance-and-audit.md`.

Each entry is a skill folder: `<skill-slug>/SKILL.md` + `adapters/`.
Deployment of adapters to live engines (publishing the Rovo agent, merging
Copilot files) is also the operator's act, recorded in the skill card.
