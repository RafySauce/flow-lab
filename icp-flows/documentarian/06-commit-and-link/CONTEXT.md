---
id: documentarian-stage-06
title: "Stage 06 — Commit & Link"
type: stage-context
stage: 6
review-intensity: heavy
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-10-21
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[collaborative-sections-protocol]]"
  - "[[ai-refinement-handoff-contract]]"
  - "[[sp-confluence-page-commit]]"
  - "[[sp-servicenow-kb-commit]]"
  - "[[documentarian-commit-packet]]"
---

# Stage 06 — Commit & Link

## Inputs

| Input | Source | Required |
|---|---|---|
| Validated document/diff for the current work-order line | Stage 05 | Yes |
| Clean findings report (or user-accepted findings, recorded) | Stage 05 | Yes |
| Enumerated deferred open-section list | Stage 05 | Yes |
| Work-order line (target page/space, position, Jira-link plan) | Stage 03 | Yes |
| Target surface + ServiceNow staged-path acceptance (if applicable) | Stage 01 | Yes |
| Candidate work items for ai-refinement (meeting jobs) | Stage 03 | If applicable |
| User commit approval (per document) | User | Yes |
| Commit packet — stands in for the Stage 01/03/05 rows above | Producing engine, carried by the user (Stage 05 step 6) | If split-engine run |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-confluence-page-commit).
ServiceNow write path: deferred gap, sp-servicenow-kb-commit filed — see
step 6. The ai-refinement handoff packaging (step 7) is inline per
../reference/ai-refinement-handoff-contract.md.`

This is the commit boundary. Nothing writes to a shared platform before the
rendered preview is explicitly approved.

**Entering from a commit packet (split-engine run).** When Stages 01–05 ran
on an engine outside this boundary, this stage starts from the commit packet
(`../reference/commit-packet.md`): each Pages block supplies the validated
document, its work-order line, its deferred open-section list, and its
accepted findings. Steps 1–6 and 8 run per page, unchanged — the packet's
executor brief restates them for an engine that cannot read this file. At
the waiver gate (step 1), a "fill" means the user supplies the text, inserted
verbatim; drafting it returns that page to the producing session. Step 7
does not run here: candidate work items stay with the producing engine,
which packages them once the return slip brings back the meeting page URL.
Step 9's loop walks the packet's pages, then advances to Stage 07.

1. **Open-section waiver gate** — if the deferred open-section list is
   non-empty, present it and obtain an explicit waiver before any commit: the
   user either fills the sections now (returning briefly to Stage 4's
   presentation), or waives them — committing the document with visible open
   markers — with the waiver recorded per
   `../reference/collaborative-sections-protocol.md`. No silent commit of
   open sections.
2. **Format translation** — convert the validated Markdown into the target
   platform's native format (Confluence storage format / rendered editor
   content) before any write. Raw Markdown syntax landing in a Confluence
   page is a defect, the same `format_translation_gate` discipline as
   ai-refinement Stage 06.
3. **Dry-run preview** — present the document in rendered form: content, the
   open-section markers as they will appear, page title, target space and
   parent position, labels and page properties (doc type, owner, review-by),
   and the Jira remote links to be created. Obtain explicit approval.
4. **Commit** — create or update the Confluence page through the engine's
   native Confluence capabilities (Rovo actions first; the sanctioned
   Atlassian integration is the fallback for engines without them). Set
   labels, page properties, and parent position per the work-order line.
5. **Jira linkage** — create the remote links per the line's Jira-link plan
   (page ↔ item, both directions where the tenant supports it). Every link
   traces to the plan; no discovered-along-the-way links without user
   confirmation.
6. **ServiceNow-destined documents** — the write path is a **known gap**
   (`sp-servicenow-kb-commit`, deferred: no sanctioned ServiceNow integration
   exists). The document — already shaped by the `kb-article` registry schema
   with its ServiceNow field mapping — commits to Confluence as staged,
   labeled `servicenow-pending`, and the gap is stated to the user rather
   than worked around.
7. **ai-refinement handoff (meeting jobs)** — package the confirmed candidate
   work items per `../reference/ai-refinement-handoff-contract.md` and hand
   the package to the user for their ai-refinement session. This flow never
   creates Jira work items itself.
8. **Confirm success** — return the page URL(s), created links, and (if
   applicable) the handoff package location.
9. **Loop decision** — work-order lines remaining → loop back to Stage 4 with
   the next line; work order drained → advance to Stage 7.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Committed page URL + applied labels/properties | Stage 07, user | link + list |
| Created Jira remote links | Stage 07, run decision log | list |
| Recorded open-section waiver (if any) | Stage 07, run decision log | text |
| ai-refinement handoff package (meeting jobs) | User → ai-refinement Stage 01 | per the handoff contract |
| Loop/advance decision | Band ③ / Stage 07 | text |
| Filled return slip, Stage 06 columns (split-engine run) | User → producing session; run decision log | table, per `../reference/commit-packet.md` Part E |

## Verify

Cross-stage trace: the committed page matches Stage 05's validated document
content-for-content (only markup translated, nothing of substance altered
after validation), and the open-section markers visible on the committed page
match Stage 05's enumerated list exactly (minus any the user filled at the
waiver gate, plus none). Additionally, every link created matches Stage 03's
Jira-link plan for this line. The failures these catch are post-validation
content mutation, silently dropped or invented open sections, and unplanned
links. Running these checks leaves a one-line result in the run's decision
log.

- [ ] Open-section waiver obtained (or sections filled) before commit —
      recorded
- [ ] No raw Markdown syntax in the committed page
- [ ] Rendered dry-run preview shown (content, markers, position, labels,
      properties, planned links) and explicitly approved
- [ ] Committed content matches the Stage 05 validated document
      (markup-translation aside)
- [ ] Committed open-section markers match the enumerated list (accounting
      only for waiver-gate fills)
- [ ] Every created Jira link is in the Stage 03 plan; none invented
- [ ] ServiceNow-destined documents staged with `servicenow-pending`, gap
      stated
- [ ] Handoff package (meeting jobs) shaped per the contract and delivered to
      the user, not to Jira
- [ ] Page URL returned; loop/advance decision recorded
- [ ] When entered from a commit packet, the version check (executor brief
      rule 1) ran first, every page got its own preview and approval, and no
      waived or filled section text was drafted by the executor

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy, unconditionally — this is the commit boundary. An
  incorrect write creates or corrupts real pages on shared platforms that
  colleagues rely on.
- **Evidence:** the approved dry-run preview, the committed page URL, and the
  link list captured in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo — the write path uses native
  Atlassian actions and the content stays in Atlassian. A Copilot-driven run
  hands off to Rovo (or to the human) at this boundary through the commit
  packet (`../reference/commit-packet.md`,
  `methodology/engine-handoff-contract.md`); Copilot does not hold
  Confluence write credentials.
- Page URLs and links are `internal` — shareable within the organization.
- API credentials are handled by the platform — never included in flowspace
  artifacts.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
