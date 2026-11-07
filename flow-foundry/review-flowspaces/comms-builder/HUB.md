---
id: comms-builder
title: "Comms Builder — Stakeholder Communications from Ask to Ready-to-Send Pack"
type: flowspace
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[fp-comms-builder]]"
  - "[[executive-slide-digest]]"
  - "[[sp-comms-context-linker]]"
  - "[[sp-audience-mapper]]"
  - "[[sp-comms-plan-builder]]"
  - "[[sp-comms-drafter]]"
  - "[[sp-deck-stylizer]]"
  - "[[comms-builder-commit-packet]]"
  - "[[design-system-binding]]"
---

# Comms Builder — Stakeholder Communications from Ask to Ready-to-Send Pack

This flowspace turns "we need to get communications out to <audience> about
<subject>" into a reviewed, ready-to-send pack for application owners,
technical owners, and business users. Subjects include changes to shared
services, platform changes, key projects, and CVE or incident response plans;
changes are the first use case. Stage 1 decides with the user whether the ask
is a **one-off** message or a **campaign**. A campaign adds a comms plan with
a timeline visual, a validation tracker, and implementation meeting
materials. The flow drafts and hands off; it never sends, posts, or messages
anyone. One run = one pack for one subject.

Its sibling `executive-slide-digest` reports where an initiative stands to
executives; this flow prepares people for something that is about to happen
to them. Exec status-deck asks route there. Both will style decks through
the same `deck-stylizer` once it is built.

## Stage Flow Diagram

```mermaid
flowchart LR
    S1["1. Frame &amp; Triage<br/>review: heavy"]:::heavy --> S2["2. Link Source Records<br/>review: light"]:::gap
    S2 --> S3["3. Audience Design<br/>review: heavy"]:::gap
    S3 --> S4["4. Comms Plan &amp; Timeline<br/>review: light"]:::gap
    S4 --> S5["5. Draft Messages<br/>review: light"]:::gap
    S5 --> S6["6. Meeting Materials<br/>review: light"]:::gap
    S6 --> S7["7. Align &amp; Approve<br/>review: heavy"]:::heavy
    S7 --> S8["8. Publish &amp; Hand Off<br/>review: heavy"]:::heavy

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

> Stages 2–6 carry the `gap` color: each depends on a skill whose primer
> brief is filed but not yet built. The Stage table carries their real
> review intensity. Lanes (below) decide which stages a run executes; the
> diagram shows the full campaign path.

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | Frame & Triage | heavy | internal | Copilot | inline — human judgment, lane and type proposal per `reference/comms-types-and-lanes.md` |
| 2 | Link Source Records | light | confidential (read) / internal (output) | Copilot | TBD — brief filed (`sp-comms-context-linker`) |
| 3 | Audience Design | heavy | internal | Copilot | TBD — brief filed (`sp-audience-mapper`) |
| 4 | Comms Plan & Timeline | light | internal | Copilot | TBD — brief filed (`sp-comms-plan-builder`) |
| 5 | Draft Messages | light | internal | Copilot | TBD — brief filed (`sp-comms-drafter`) |
| 6 | Meeting Materials | light | internal | Copilot | TBD — brief filed (`sp-deck-stylizer`) for the deck; agenda and run-of-show inline |
| 7 | Align & Approve | heavy | internal | Copilot | inline — human judgment |
| 8 | Publish & Hand Off | heavy | internal | Copilot (producer); Rovo (executor of packets) | inline — packet emission per `reference/commit-packet.md`; executor runs `confluence-page-commit` |

### Lanes

| Lane | Stages run | Suggested when |
|---|---|---|
| One-off | 1 → 2 (only if records are linked) → 3 (lite: one or two segments) → 5 → 7 → 8 | A single message to one or two audiences, no validation asks, no implementation event |
| Campaign | 1 → 2 → 3 → 4 → 5 → 6 (only with an implementation event) → 7 → 8 | A large-scale change touching many stakeholders; a change that needs specific validation from application teams; a project with many different stakeholders |

The flow proposes the lane with its reasons; the user decides. A one-off can
upgrade to a campaign at Stage 7 without restarting — the run re-enters at
Stage 4 with Stages 1–3 outputs intact.

## Source-repo

- **Source-repo:** the operator's internal GitLab instance repo,
  `flowspaces/comms-builder/` — set at instantiation, sole source of truth
  for the instance.
- **External systems read:** ServiceNow (change, incident, and
  vulnerability records) and Jira, read-only, at Stage 2 only, by Copilot.
  Paste fallback when a source is not reachable.
- **External systems written:** Confluence (comms plan page) and Jira (a
  plan-summary comment on a named item), written **only** by a Rovo executor
  from Stage 8's commit packet, which the user carries by hand. Outlook and
  Teams drafts are created by the user. No stage sends a message.

## Run procedure

A run starts when someone asks for comms about a subject. Stage 1 captures
the subject, the audience in plain words, the key date, and any linked
records, then proposes a comms type and lane with reasons; the user confirms
or steers. Stage 2 pulls the linked records into a cited context sheet under
the response-plan data rule. Stage 3 designs segments and what each needs
to know and do. On a campaign, Stage 4 lays touchpoints against the key date
and produces the validation tracker and the timeline (rendered image plus
raw Mermaid). Stage 5 drafts every message from the operator's templates or
the plain defaults. Stage 6 builds meeting materials when an implementation
event exists. Stage 7 is the user's review of the whole pack against Stage
1's framing. Stage 8 delivers the pack in chat and emits a commit packet for
anything bound for Rovo. Each boundary is a human check — that is the
method, not an inconvenience. Visual outputs follow the instance's
design-system binding (`reference/design-system-binding.md`).

## Known gaps

> Per `methodology/governance-and-audit.md` §5a: each entry is a pointer —
> 1–3 sentences plus the decision-log citation.

Five Layer-3 skills are filed as primer briefs in
`skill-foundry/backlog-skill-starters/` and not built; until they are, a
direct run follows each stage's Process field inline. Building them is a
separate operator go-ahead. See `decision-log/2026-11-07-scaffold-triage.md`.

| Skill | Primer brief | Target stage | Status |
|---|---|---|---|
| `comms-context-linker` | `sp-comms-context-linker` | 2 | brief filed |
| `audience-mapper` | `sp-audience-mapper` | 3 | brief filed |
| `comms-plan-builder` | `sp-comms-plan-builder` | 4 | brief filed |
| `comms-drafter` | `sp-comms-drafter` | 5 | brief filed |
| `deck-stylizer` | `sp-deck-stylizer` | 6 | brief filed; would later replace `executive-slide-pptx-stylizer` (separate decision) |

Second gap: the design-system binding contract lives in this flow's
`reference/` until `deck-stylizer` is built, then moves into that skill.
This repo ships only the brand-neutral default; an instance binds its own
system. See `decision-log/2026-11-07-scaffold-triage.md` §4.

Third gap: whether the instance's Copilot can render Mermaid to an image,
and whether its Confluence has a Mermaid macro, are open; the table fallback
in `reference/timeline-and-validation-tracker.md` covers both until
confirmed.

## Reference material (Layer-3)

| Artifact | Location | Covers |
|---|---|---|
| Flow Primer Brief | `flow-foundry/backlog-flow-starters/fp-comms-builder.md` | The crystallized intent this flowspace was built from |
| Comms Types and Lanes | `reference/comms-types-and-lanes.md` | Comms types, lane rule, default touchpoint set per type, response-plan data rule |
| Audience Segment View | `reference/audience-segment-view.md` | Default segments and the per-segment view shape |
| Timeline and Validation Tracker | `reference/timeline-and-validation-tracker.md` | Gantt conventions, color roles, legend, table fallback, tracker shape |
| Default Message Templates | `reference/default-message-templates.md` | Plain defaults used when no operator template folder is set |
| Design-System Binding | `reference/design-system-binding.md` | The contract a design system fills, the config keys, and the neutral default |
| Commit Packet | `reference/commit-packet.md` | Rovo handoff for the Confluence plan page and the Jira comment |
| Engine Handoff Contract | `methodology/engine-handoff-contract.md` | Packet Parts A–E |
| Sibling flowspace | `../executive-slide-digest/HUB.md` | Exec status decks |
| Provenance spec | `methodology/provenance-spec.md` | Frontmatter rules |
| Governance & Audit | `methodology/governance-and-audit.md` | Gate requirements |
