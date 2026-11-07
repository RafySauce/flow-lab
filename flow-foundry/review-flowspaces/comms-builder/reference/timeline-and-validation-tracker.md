---
id: timeline-and-validation-tracker
title: "Timeline and Validation Tracker"
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

# Timeline and Validation Tracker

Stage 4 builds the campaign timeline as a Mermaid `gantt`, delivered as a
**rendered image plus the raw Mermaid**, with colors that carry meaning and
a legend. Colors come from the instance's design-system binding
(`design-system-binding.md`); the values below are the brand-neutral
default.

## Color roles

Mermaid gantt colors tasks by state, so each role maps to a state tag.
Color never stands alone: each label also carries the word.

| Role | Gantt tag | Meaning | Neutral default (fill / border) |
|---|---|---|---|
| Upcoming | *(none)* | Touchpoint not yet sent | `#ffffff` / `#6b7280` |
| Sent | `done` | Touchpoint sent | `#e3efe5` / `#2e6b3a` |
| Awaiting validation | `active` | A validation window is open | `#e6f0fa` / `#1f5f8b` |
| Key window | `crit` | The change window or response period itself | `#fdeee6` / `#b4441e` |
| Milestone | `milestone` | Go/no-go, all-clear, deadline | drawn as a diamond in the task colors |

Text is `#111827` on every fill (all pairs above 4.5:1).

## Example (neutral default)

```mermaid
%%{init: {'theme':'base','themeVariables': {
  'taskBkgColor':'#ffffff','taskBorderColor':'#6b7280','taskTextColor':'#111827','taskTextDarkColor':'#111827','taskTextOutsideColor':'#111827',
  'doneTaskBkgColor':'#e3efe5','doneTaskBorderColor':'#2e6b3a',
  'activeTaskBkgColor':'#e6f0fa','activeTaskBorderColor':'#1f5f8b',
  'critBkgColor':'#fdeee6','critBorderColor':'#b4441e'}}}%%
gantt
    title Platform upgrade — comms plan
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Announce
    T-14 announce (all segments) — SENT      :done, a1, 2026-01-05, 1d
    section Validate
    Validation window (app owners) — OPEN    :active, v1, 2026-01-12, 5d
    section Remind
    T-2 reminder + bridge invite — UPCOMING  :r1, 2026-01-17, 1d
    section Implement
    Change window — KEY WINDOW               :crit, w1, 2026-01-19, 1d
    Go/no-go — MILESTONE                     :milestone, m1, 2026-01-19, 0d
    All-clear — UPCOMING                     :c1, 2026-01-20, 1d
```

Legend line to print under every rendered image:
`Upcoming · Sent · Awaiting validation · Key window · Milestone` — each in
its color.

## Rendering

- **Image:** render with the engine's own capability where it has one.
  Never paste plan content into an unsanctioned external renderer.
- **Raw Mermaid:** always delivered in a fenced block, so it can be pasted
  into a Confluence Mermaid macro or edited later.
- **Table fallback:** used for Jira comments (no Mermaid rendering), and
  anywhere the image cannot be produced:

| Date | Touchpoint | Segments | Channel | Status |
|---|---|---|---|---|

## Validation tracker

One row per validation ask from Stage 3. Status values: not started · in
progress · confirmed · issue raised.

| Validates | Team (group) | What is confirmed | Due | Status | Evidence link |
|---|---|---|---|---|---|
