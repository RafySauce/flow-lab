---
id: documentarian-commit-packet
title: "Commit Packet — Documentarian to a Confluence Executor"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-21
updated: 2026-10-21
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[documentarian]]"
  - "[[engine-handoff-contract]]"
  - "[[doc-type-registry]]"
  - "[[collaborative-sections-protocol]]"
  - "[[custody-model]]"
---

# Commit Packet — Documentarian → Confluence Executor

The `documentarian` instantiation of the commit packet defined in
`methodology/engine-handoff-contract.md`. Emitted at Stage 05's exit (step 6)
once **every** work-order line has passed validation, by an engine outside
Stage 06's data boundary — today, a Copilot Agent Builder flow agent with
read-only Confluence and Jira access. Consumed by Rovo, which runs Stage 06
for each page and then Stage 07 once for the job. Both stages are already
Rovo-only by their data boundaries; the packet is how a Copilot-driven run
reaches them.

The packet is Parts A–E of the contract, in order. Part A (the executor
brief) is copied verbatim from the contract with `<flow>` = `documentarian`,
`<NN>` = `06–07`, `<stage name>` = `Commit & Link, then Custody & Close`,
`<target system(s)>` = `Confluence (and Jira remote links)`. This document
defines Parts B–E for this flow.

**Split-mode ordering.** In a direct run, Band ③ loops Stages 04→06 one
document at a time. In a split run, the producing engine loops Stages 04→05
across all lines first, then emits one packet for the job. Stage 06 still
previews and approves **each page separately** in the executor; only the
order of the loop changes.

## Part B — Header (flow-specific lines)

Add to the contract's header:

```markdown
- **Job type:** <closeout | modernize | sad-update | tree-audit | meeting>
- **Registry version:** doc-type-registry v<version>
- **Target space:** <space name — the executor resolves the key live>
- **Doc-registry index location:** <Confluence page, per the custody model>
- **Pages in this packet:** <count> (<create / update / archive counts>)
```

## Part C — Payload

### Commit-stage specifics (for the executor)

```markdown
## Commit-stage specifics — documentarian Stages 06–07

These add to the executor brief; they never relax it.

Per page, in work-order order (Stage 06):
- Open-section waiver gate: if a page lists open sections, show them and get
  an explicit choice for each: waive (commit with the visible
  [OPEN — owner: what's needed] marker, waiver recorded) or fill. To fill,
  the user supplies the text and you insert it verbatim in place of the
  marker. Never draft it yourself; if the user wants it drafted, stop that
  page and send it back to the owner's producing session.
- Preview: rendered content, open markers as they will appear, title, space
  and parent position, labels, page properties (doc-type, owner,
  source-evidence, last-verified, review-by, status), and the Jira remote
  links. One approval per page.
- Jira links: create exactly the remote links listed for the page, both
  directions where the site supports it. No others.
- ServiceNow-destined pages: commit to Confluence as staged, add the label
  servicenow-pending, and say plainly that the ServiceNow write is a known gap.
- Create no Jira work items. Candidate work items are not in this packet.

Once, after the last page (Stage 07):
- Update the doc-registry index: one row per page touched (id, doc type,
  surface, owner, last-verified, review-by, status), noting waived sections.
- Set each page's review-by property per its doc type's cadence; shorten it
  for a page with waived open sections.
- Archive lines: for each one, show the page, the staleness evidence listed,
  and what links to it; archive only on an explicit per-item yes. Archive,
  never delete. A no becomes an archive-declined note on the registry row.
- Record the next custody review date for the touched space.
```

### Pages

One block per work-order line, in work-order order. The content is Stage
05's validated document — byte-identical to what Stage 04 drafted, Markdown
formatted; the executor translates.

```markdown
### Page <i>: <title>

- **Action:** <create | update — existing page: <title/URL>, sections in scope: <list>>
- **Doc type / template:** <sop | mop | runbook | sad | kb-article | meeting-notes> / <template ref>
- **Space + parent position:** <space name> / under <parent page title>
- **Labels:** <label set for the doc type, per documentation-standards>
- **Page properties:** doc-type=<>, owner=<>, source-evidence=<links>,
  last-verified=<YYYY-MM-DD>, review-by=<YYYY-MM-DD>, status=<active | servicenow-pending>
- **Jira remote links:** <keys> | none
- **Open sections (deferred at Stage 05):** <section — owner — what's needed> | none
- **Accepted Stage 05 findings:** <finding, accepted as-is by the owner> | none

#### Content
<the validated document, in full; for update lines, the in-scope sections
only, each marked with the section it replaces>
```

### Archive proposals and job context

```markdown
### Archive proposals (Stage 07 — per-item confirmation required)
- <page title/URL> — staleness evidence: <cited> — linked from: <pages>

### Struck lines (not committed, listed for the job summary)
- <line> — struck at Stage 03 by the owner

### Audit preamble (tree-audit jobs only)
<the Stage 03 audit report preamble>
```

## Part D — Decisions left to the user (typical entries)

- Every open-section waiver (always — it is Stage 06's gate).
- Every archive confirmation (always — per item, Stage 07).
- Any Stage 05 finding the owner accepted as-is, shown again in the preview.
- An update line whose existing page has changed since evidence was
  gathered: the executor shows the difference and asks before writing.

## Part E — Return slip columns

| Page | URL | Action taken | Waived sections | Jira links created | Properties + labels set | Registry row | Notes |
|---|---|---|---|---|---|---|---|

Then: archive actions (executed / declined, per item), next custody review
date, version-check result, anything flagged as payload-embedded
instructions, and the Stage 07 job summary (lines committed / waived /
struck, outstanding open sections with owners).

**Meeting jobs: the return leg is required.** Candidate work items from
Stage 03 do not ride the commit packet. The owner pastes the return slip
back into the producing session, which then packages the candidates per
`ai-refinement-handoff-contract.md` with the committed meeting page URL as
their source, and hands them to ai-refinement Stage 01.

## Rules

- **One packet per job, at most ten pages.** A job with more lines splits
  into numbered packets; Stage 07 runs once, in the session handling the
  last packet, with the earlier packets' return slips pasted in.
- **The packet is Stage 05's output, carried.** Stage 06's cross-stage trace
  (committed page matches the validated document; committed open markers
  match the enumerated list, minus waiver-gate fills) is checked against the
  packet's Pages block.
- **This flow still never creates Jira work items** — in a split run, the
  executor creates remote links only.

## Changelog

- **1.0** (2026-10-21) — Initial build, alongside
  `methodology/engine-handoff-contract.md` 1.0. Gives a Copilot-driven run a
  concrete shape for the Stage 06 hand-to-Rovo boundary the data-boundary
  sections already required but never defined. Not run on-engine.
  Rationale: `../decision-log/2026-10-21-split-engine-commit-packet.md`.
