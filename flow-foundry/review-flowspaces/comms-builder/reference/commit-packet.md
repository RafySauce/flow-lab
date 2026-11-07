---
id: comms-builder-commit-packet
title: "Commit Packet — Comms Builder to a Rovo Executor"
type: specification
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
  - "[[comms-builder]]"
  - "[[engine-handoff-contract]]"
  - "[[confluence-page-commit]]"
---

# Commit Packet — Comms Builder → Rovo Executor

The `comms-builder` instantiation of the commit packet defined in
`methodology/engine-handoff-contract.md`. This flow runs entirely in
Copilot. Anything bound for Confluence or Jira leaves Stage 8 as a `.md`
packet the requester pastes into Rovo by hand; Copilot never writes to
either system.

The packet is Parts A–E of the contract, in order. Part A (the executor
brief) is copied verbatim from the contract with `<flow>` =
`comms-builder`, `<NN>` = `08`, `<stage name>` = `Publish & Hand Off`,
`<target system(s)>` = `Confluence (plan page) and/or Jira (plan-summary
comment)`. This document defines Parts B–E for this flow.

A packet carries at most **two items**: one Confluence page and one Jira
comment. A run that targets neither emits no packet.

## Part B — Header (flow-specific lines)

```markdown
- **Comms type / lane:** <awareness | action required | change implementation | response plan> / <one-off | campaign>
- **Subject:** <one sentence from the framing brief>
- **Key date:** <YYYY-MM-DD, timezone>
- **Approved:** <YYYY-MM-DD> by <requester> (and <house comms approver> if any)
- **Provenance label:** comms-builder-flow-v<flow-version>
- **Items in this packet:** <page: yes/no> · <jira comment: yes/no>
```

## Part C — Payload

### Commit-stage specifics (for the executor)

```markdown
## Commit-stage specifics — comms-builder Stage 08

These add to the executor brief; they never relax it.

Confluence plan page (if present):
- Run confluence-page-commit: show a rendered preview (title, space, parent,
  labels, content) and get one explicit approval before writing.
- Content is the approved plan as given. If the space has a Mermaid macro,
  place the raw Mermaid block in it; otherwise attach the timeline image
  the user supplies and keep the table fallback in the page body.
- Labels: comms-plan and comms-builder-flow-v<flow-version>.

Jira comment (if present):
- Add exactly one comment to the named existing item. Show the comment text
  and the item key first; post only on an explicit yes.
- Content is the table fallback plus the Confluence page link (if the page
  was created in this run, use the URL you just created). No Mermaid.
- Create no work items, change no fields, transition nothing.

Never send email or Teams messages; those are the requester's to send.
```

### Items

```markdown
### Item 1: Confluence plan page
- **Action:** create | update — existing page: <title/URL>
- **Space + parent position:** <space name> / under <parent page title>
- **Title:** Comms plan — <subject> — <key date>
- **Labels:** comms-plan, comms-builder-flow-v<flow-version>

#### Content
<approved plan: framing summary, segment table, touchpoint table,
validation tracker, legend, raw Mermaid block, table fallback>

### Item 2: Jira plan-summary comment
- **Item key:** <KEY-123>
- **Link to plan page:** <URL | "use Item 1's URL">

#### Content
<approved table fallback and one-line summary>
```

## Part D — Decisions left to the user (typical entries)

- Whether to create or update the plan page when a page with the same title
  already exists.
- Placement of the timeline (Mermaid macro vs. attached image).
- "None" when nothing was left open.

## Part E — Return slip columns

| Item | Created as (URL / comment link) | Status (created / updated / not created / halted) | Labels set | Notes |
|---|---|---|---|---|

Then: version-check result, anything flagged as payload-embedded
instructions, and anything still open for the requester. The return leg is
optional; pasting the slip back lets the run record the page URL in its
decision log.
