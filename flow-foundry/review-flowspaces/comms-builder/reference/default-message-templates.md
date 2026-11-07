---
id: default-message-templates
title: "Default Message Templates"
type: template
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

# Default Message Templates

Stage 5 uses these only when the instance's `template-path` is unset or has
no template for a touchpoint kind. They are deliberately plain, so the
requester can review and tweak them fast. Placeholders in `<angle
brackets>` are filled from cited inputs; anything the inputs lack becomes
`[NEEDS INPUT: …]`.

Every template follows four rules: the subject leads with the action or the
date; the first line says what is happening and whether the reader must act;
one ask per message; a named place for questions.

## Announce (awareness or change)

```text
Subject: <What> on <date> — <no action needed | action needed by <date>>

<One sentence: what is changing and when.>

What this means for you: <segment-specific impact>.
What you need to do: <action and date, or "Nothing.">
Reference: <record number / page link>
Questions: <group or channel>
```

## Action request / validation request

```text
Subject: Action needed by <date>: <the action>

<One sentence: why we are asking.>

Please <action> by <date>. <How to do it, or where the steps are.>
When done: <how to confirm — reply, form, tracker row>.
If you can't make the date: <who to tell>.
Questions: <group or channel>
```

## Reminder

```text
Subject: Reminder — <action or event> on <date>

<One sentence restating what is happening and when.>
<If action: "If you have already <done it>, thank you — no need to reply.">
Questions: <group or channel>
```

## Day-of start notice

```text
Subject: Starting now: <change> (<window>)

<Change> has started and is planned to finish by <time, timezone>.
During the window: <what people will notice>.
Next update: <time or "at completion">.
Report problems to: <channel>
```

## All-clear

```text
Subject: Complete: <change>

<Change> finished at <time>. <Services> are available.
<If validation: "Validation status: <summary from tracker>.">
If something looks wrong: <channel>
```

## Delay or rollback notice

```text
Subject: <Delayed | Rolled back>: <change>

<Change> has been <delayed to <new date> | rolled back>. <Services> are
<available as before | status>.
What this means for you: <impact>.
Next update: <when>.
Questions: <group or channel>
```

## Response plan — initial, update, resolved

```text
Subject: <Initial notice | Update <n> | Resolved>: <short name>, <record number>

What's happening: <impact in plain terms — no technical detail>.
Who is affected: <segments or services>.
What you need to do now: <action, or "Nothing at this time.">
Next update: <time | "none — this is resolved">.
Questions: <group or channel>
```

Response-plan drafts never carry exploit details, configurations, IP
addresses, or control descriptions (`comms-types-and-lanes.md`).
