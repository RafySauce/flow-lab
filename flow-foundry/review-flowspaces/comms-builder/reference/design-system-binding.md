---
id: design-system-binding
title: "Design-System Binding"
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
---

# Design-System Binding

How a design system plugs into this flow's visual outputs without being
written into the flow. flow-lab ships only the **brand-neutral default**
below; an instance binds its own system in its source-repo. This contract
lives here until `deck-stylizer` is built (`sp-deck-stylizer`), then moves
into that skill so `executive-slide-digest` can share it.

## What a design system styles here — and what it does not

| Output | Styled by the binding? | Why |
|---|---|---|
| Timeline (Mermaid gantt) | Yes — color roles | Read at a glance; color carries status |
| Confluence plan page | Structure and voice; color only where page panels allow | Confluence styling is limited |
| Implementation meeting deck | Yes — full | Presented, so it benefits most |
| Jira comment | No | Plain table and a link |
| Emails and Teams posts | Voice rules only, never visual styling | Recipients' clients strip styling, and the messages must read as the employer's own internal comms |

## The contract — roles a binding fills

A binding is one file in the instance's source-repo,
`reference/design-system-binding.local.md` (or wherever the config points),
with this frontmatter block:

```yaml
design-system: <name, or "neutral-default">
template-path: <folder the agent can read for message and deck templates, or empty>
deck-template: <path to a .pptx template, or empty>
themes:
  present: <theme for decks and screen-shared frames>
  read: <theme for pages and printed handouts>
type-family: <font stack>
timeline-colors:          # fill / border / text per role (see timeline-and-validation-tracker.md)
  upcoming:   [<fill>, <border>, <text>]
  sent:       [<fill>, <border>, <text>]
  validating: [<fill>, <border>, <text>]
  key-window: [<fill>, <border>, <text>]
status-words: [On track, At risk, Blocked, Note]   # color always paired with a word
voice-rules:              # short list applied to every draft and page
  - <rule>
```

Every text-on-fill pair must hold 4.5:1 contrast. Colors that must be told
apart differ in lightness, not hue alone.

## Neutral default (what this repo ships)

```yaml
design-system: neutral-default
template-path: ""
deck-template: ""
themes: { present: light, read: light }
type-family: "Calibri, Arial, sans-serif"
timeline-colors:
  upcoming:   ["#ffffff", "#6b7280", "#111827"]
  sent:       ["#e3efe5", "#2e6b3a", "#111827"]
  validating: ["#e6f0fa", "#1f5f8b", "#111827"]
  key-window: ["#fdeee6", "#b4441e", "#111827"]
status-words: [On track, At risk, Blocked, Note]
voice-rules:
  - Lead with the answer or the action.
  - Sentence case; no hype words; no emoji.
  - One ask per message, with a date.
  - Every date carries a timezone when a time is given.
```

## Rules

- A binding is instance configuration, never committed to this public repo.
  An operator's own design system stays in their tenancy or private
  workspace unless they decide otherwise (see this flow's decision log §4).
- When `template-path` is set, its templates win over
  `default-message-templates.md` for every touchpoint kind they cover.
- A missing binding is not an error: the run says "neutral default" at
  Stage 1 and continues.
