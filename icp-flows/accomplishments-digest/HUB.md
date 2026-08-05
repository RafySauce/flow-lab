---
id: accomplishments-digest
title: "Accomplishments Digest — Jira & Confluence Performance-Review Prep"
type: flowspace
artifact-version: "1.3"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-08-05
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[fp-accomplishments-digest]]"
  - "[[sp-jira-accomplishments-gatherer]]"
  - "[[sp-confluence-contribution-gatherer]]"
  - "[[sp-accomplishments-drafter]]"
  - "[[accomplishments-docx-finisher]]"
---

# Accomplishments Digest — Jira & Confluence Performance-Review Prep

This flowspace turns a review period's worth of Jira and Confluence activity into
a single, readable accomplishments document an engineer can hand to their
manager. It exists because the raw material — closed tickets, authored docs,
review comments — is scattered, ticket-shaped, and easy to under-sell; the
flow's job is to gather it faithfully, reframe it in outcome terms grouped by
theme, and carry the engineer's own read on impact rather than substitute an
agent's guess for it. One run = one finished document for one review cycle.

## Stage Flow Diagram

```mermaid
flowchart LR
    S1["1. Frame<br/>review: heavy"]:::heavy --> S2["2. Gather — Jira<br/>review: light"]:::light
    S2 --> S3["3. Gather — Confluence &amp; Collaboration<br/>review: light"]:::light
    S3 --> S4["4. Draft<br/>review: light"]:::light
    S4 --> S5["5. Align &amp; Publish<br/>review: heavy"]:::heavy
    S5 --> S6["6. Handoff to Copilot<br/>review: light"]:::light

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

> Stages 2, 3, and 4 are colored by their intended `light` review intensity, not
> `gap` — the skills they lean on now are `truth-level: verified` and live in
> `produced-skills/` (operator promotion 2026-07-15, accepting the five-point
> gate's agent pre-run and its simulated live tests as the review record;
> evidence in
> `skill-foundry/decision-log/2026-07-15-accomplishments-digest-skill-batch-promotion.md`).
> The simulated live tests are not engine runs — the first on-engine
> invocation per adapter happens at deployment, which remains the operator's
> act at instantiation. See Known gaps. The diagram keeps the flat-chain
> convention (`references/flow-diagram-guide.md` — no branching without a
> documented topology split) even though Stage 6 is optional in practice:
> Stage 5's publish is already the flow's complete, terminal artifact, and
> Stage 6 only runs when the engineer also wants the Copilot-produced,
> stylized Word version. Optionality is documented in the Stage table and
> Stage 6's own `CONTEXT.md`, not encoded as a diagram branch.

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | Frame | heavy | internal | Rovo, Copilot | inline — human judgment, no skill |
| 2 | Gather — Jira | light | internal | Rovo | `jira-accomplishments-gatherer` (verified, `produced-skills/`) |
| 3 | Gather — Confluence & Collaboration | light | internal | Rovo | `confluence-contribution-gatherer` (verified, `produced-skills/`) |
| 4 | Draft | light | internal | Rovo, Copilot | `accomplishments-drafter` (verified, `produced-skills/`) |
| 5 | Align & Publish | heavy | internal | Rovo, Copilot | inline — human judgment, no skill |
| 6 | Handoff to Copilot (optional) | light | internal | Rovo | inline — see `reference/handoff-to-copilot-template.md` |

## Surfaces

- **Primary:** `<Confluence space set at instantiation>` — an `Accomplishments`
  page tree, one page per review cycle per engineer. Confirm the Mermaid macro
  is installed in the target space before this diagram ships to the Confluence
  primary; absent that, the page notes "diagram: see mirror."
- **Mirror:** `<internal repo>` → `flows/accomplishments-digest/`.

This public copy is the sanitized *design*; instantiation happens in employer
tenancy per `methodology/mirroring-protocol.md`. At instantiation, add the
per-stage `work/` folders (Layer-4, transient, one set per review cycle) and
the `handoffs/` folder — deliberately absent here since they only ever hold
per-run content.

## Run procedure

The engineer starts a run ahead of a scheduled review. Stage 1 sets the period,
audience, and the engineer's own framing of what mattered — this is the
heaviest-judgment stage and the one place the agent should ask more than it
tells. Stages 2 and 3 gather in parallel or in sequence (no dependency between
them) against the period Stage 1 set, each landing a theme-grouped, outcome-
framed digest rather than a raw activity list. Stage 4 synthesizes the two
digests with Stage 1's narrative into the house document shape. Stage 5 is the
engineer's own edit pass against their Stage 1 framing before anything is
shared — human inspects at every stage boundary, and this boundary in
particular is the one that keeps the document from reading as AI-generated
ticket-listing rather than the engineer's own account of their work. Stage 5's
published document is the flow's complete, terminal artifact. If the engineer
also wants a stylized Word version — for a promo packet, or a manager who
wants a polished document rather than a Confluence page — Stage 6 packages
that same published, approved document as a handoff (never the pre-review
Stage 4 draft) and hands it to the companion `accomplishments-docx-finisher`
flowspace, which enriches presentation only and ends with its own heavy
human-review stage before that version is shared.

## Known gaps

> Per `methodology/governance-and-audit.md` §5a: each entry below is a
> pointer, not an archive — 1–3 sentences plus the decision-log citation
> that carries the full rationale.

All three skills demanded by Stages 2–4 are `truth-level: verified` —
promoted 2026-07-15, evidence in
`skill-foundry/decision-log/2026-07-15-accomplishments-digest-skill-batch-promotion.md`
(pre-run:
`skill-foundry/decision-log/2026-07-14-accomplishments-digest-skill-gate-prerun.md`).
Remaining gap: no adapter is published to a live engine yet — first
on-engine invocation and Copilot-connector sanctioning both happen at
deployment, the operator's act.

| Skill | Primer brief | Target stage | Status |
|---|---|---|---|
| `jira-accomplishments-gatherer` | `sp-jira-accomplishments-gatherer` | 2 | verified — promoted 2026-07-15; deployment pending |
| `confluence-contribution-gatherer` | `sp-confluence-contribution-gatherer` | 3 | verified — promoted 2026-07-15; deployment pending |
| `accomplishments-drafter` | `sp-accomplishments-drafter` | 4 | verified — promoted 2026-07-15; deployment pending |

Second gap: the primer brief's open question on per-tenant activity-history
depth is operationalized as a one-time-per-tenant probe at
`reference/confluence-activity-history-capability-check.md` — Stage 3 and
the gatherer skill already implement all three fallback modes; the
checklist just tells the operator which mode a tenant is in.

Third gap (2026-07-08, 1.0 → 1.1): Stage 6 (Handoff to Copilot) added on
operator instruction — a second output artifact handed off to the
companion `accomplishments-docx-finisher` flowspace, which adds
repo/file-context enrichment and produces a final, stylized Word document.
Stage 6 is `Layer-3: inline`, not a skill gap. Rationale:
`decision-log/2026-07-08-copilot-handoff-revision.md`.

## Reference material (Layer-3)

| Artifact | Location | Covers |
|---|---|---|
| Flow Primer Brief | `flow-foundry/backlog-flow-starters/fp-accomplishments-digest.md` | Original crystallized intent this flowspace was built from |
| Handoff Template | `reference/handoff-to-copilot-template.md` | Flow-specific instantiation of the mirroring-protocol §5 handoff shape, for Stage 6 |
| Confluence Activity-History Capability Check | `reference/confluence-activity-history-capability-check.md` | One-time-per-tenant probe resolving Stage 3's flagged capability check |
| Companion flowspace | `../accomplishments-docx-finisher/HUB.md` | Receives Stage 6's handoff; produces the stylized Word document |
| Provenance spec | `methodology/provenance-spec.md` | Frontmatter rules for all artifacts |
| Governance & Audit | `methodology/governance-and-audit.md` | Gate requirements |
| Mirroring Protocol | `methodology/mirroring-protocol.md` | Handoff artifact shape (§5) this flowspace's Stage 6 follows |
