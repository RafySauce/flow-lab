---
id: audience-segment-view
title: "Audience Segment View"
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

# Audience Segment View

Stage 3 fills one view per segment. The shape descends from
`icp-flows/statik-adoption/reference/rollout-and-socialization-guide.md`'s
per-group view: people act on what changes *for them*, not on a generic
announcement.

## Default segments

| Segment | Usually cares about | Usually asked to |
|---|---|---|
| Application owners | Whether their application is affected, downtime, what they must confirm | Validate their application; approve a window; tell their own users |
| Technical owners | Technical impact on their components, dependencies, timing, backout | Make a change on their side; join the bridge; validate technically |
| Business users | Whether their work is interrupted, when, and what to do differently | Plan around a window; take a simple action; report problems |

Keep, drop, split, or add segments per run. Identify every segment by role,
group, or distribution list — never by a person's name.

## The view (one per segment)

```markdown
### <Segment> — identified by <group or distribution list>

- **What changes for you:** <one or two sentences, in their terms>
- **What you need to do:** <action> by <date>, or "nothing"
- **What you can ignore:** <the parts of the change that do not touch them>
- **You validate:** <what, by when> — or "no validation"
- **Channel:** <email | Teams post | meeting | Confluence page>
- **Questions go to:** <group or channel>
```

## The segment table (Stage 3 output)

| Segment | Identified by | What changes | Action and due date | Validates? | Channel | Questions go to |
|---|---|---|---|---|---|---|
