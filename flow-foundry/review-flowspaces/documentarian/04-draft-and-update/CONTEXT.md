---
id: documentarian-stage-04
title: "Stage 04 — Draft & Update"
type: stage-context
stage: 4
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[doc-type-registry]]"
  - "[[collaborative-sections-protocol]]"
  - "[[sp-doc-drafter]]"
  - "[[sp-sad-diagram-maintainer]]"
---

# Stage 04 — Draft & Update

## Inputs

| Input | Source | Required |
|---|---|---|
| One work-order line (the current document: action, doc type, template ref, target page, open-section plan, Jira-link plan) | Stage 03 | Yes |
| Evidence dossier entries the line cites | Stage 02 (via the line's citations) | Yes |
| Doc-type template for the matched type | `../reference/doc-type-registry.md` | Yes |
| Open-section marker protocol | `../reference/collaborative-sections-protocol.md` | Yes |
| Existing page content (update lines) | Confluence (read) | If applicable |
| Existing diagram source (sad-update lines) | Confluence page / mirror repo | If applicable |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-drafter); for sad-update
lines that touch diagram sources, additionally sp-sad-diagram-maintainer
(flagged merge candidate — the skill-foundry decides whether it folds into
the drafter)`

One pass = one work-order line. Band ③ loops this stage per line.

1. **Template instantiation** — for `create` lines, instantiate the matched
   doc type's template from the registry: all required sections present,
   metadata block populated (owner, doc type, source-evidence links,
   review-by per the type's cadence).
2. **Evidence-grounded drafting** — fill each section only from the line's
   cited dossier entries. Every substantive claim in the draft traces to a
   citation; where the evidence is indirect, the draft says so rather than
   asserting confidently.
3. **Open sections, never guesses** — sections the open-section plan assigns
   to the human are emitted as open-section markers per the protocol
   (`> [OPEN — <owner>: <what's needed>]`), with enough surrounding scaffold
   that the owner can fill them without re-deriving context. The drafter
   never fills a planned open section with plausible content — an
   invented-but-fluent section is this stage's defining failure mode.
4. **Updates as diffs** — for `update` lines, read the existing page and
   present changes as a section-by-section diff: unchanged sections stated as
   unchanged, modified sections shown old → new, additions marked. Existing
   content that the evidence does not contradict is preserved, not rewritten
   for style (style-only changes belong to `modernize` lines where the work
   order says so).
5. **Diagram maintenance (sad-update lines)** — update text-editable diagram
   sources (Mermaid, PlantUML, drawio XML) to reflect the delivered change,
   with the same diff discipline. Non-text-editable diagrams (images, screen
   captures) are flagged for human redraw as an open section — never traced
   over or re-generated lossily.
6. **Per-document presentation** — present the draft (or diff) with its open
   sections enumerated. The user may fill open sections now, defer them, or
   adjust the draft; deferred sections stay marked and travel to Stage 5.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Drafted document (create lines) or section diff (update lines), template-shaped, citations attached | Stage 05 | markdown against the registry template |
| Open-section marker list (id, owner, what's needed, status: filled/deferred) | Stages 05, 06 | list |
| Updated diagram source + human-redraw flags (sad-update lines) | Stage 05 | diagram source + list |

## Verify

Cross-stage trace: the draft's section set matches the registry template for
the line's doc type, and the draft's open-section markers match Stage 03's
open-section plan for this line — every planned open section is present
(filled or deferred, never silently resolved by invented content), and no
unplanned section was dropped. The failure this catches is a fluent draft
that quietly guessed what Stage 03 said the human must supply. Running this
check leaves a one-line result in the run's decision log.

- [ ] Section set matches the registry template for the doc type
- [ ] Metadata block populated (owner, type, evidence links, review-by)
- [ ] Every substantive claim carries a citation to a dossier entry
- [ ] Every Stage 03 planned open section appears as a marker (filled or
      deferred) — none replaced by generated content
- [ ] Update lines presented as diffs; unchanged content preserved
- [ ] Diagram changes limited to text-editable sources; non-text diagrams
      flagged for human redraw
- [ ] User saw the draft and open-section list for this line

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution against a confirmed work-order
  line and template; the user already inspects each draft inline, so review
  is a consistency scan, not a re-read.
- **Evidence:** the presented draft/diff in the session and a one-line entry
  in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot — drafting works from
  the dossier's cited content; Copilot may drive when the evidence is
  repo-adjacent (sad-update), Rovo when it is Confluence/Jira-native.
- Drafts contain only content already screened at Stages 01–02; new material
  the user types into an open section is theirs and enters at their call.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
