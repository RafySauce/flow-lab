---
id: documentarian-stage-02
title: "Stage 02 — Evidence Gathering"
type: stage-context
stage: 2
review-intensity: light
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
  - "[[sp-doc-evidence-gatherer]]"
---

# Stage 02 — Evidence Gathering

## Inputs

| Input | Source | Required |
|---|---|---|
| Selected job type + rationale | Stage 01 | Yes |
| Screened source material references (item keys, space/tree links, feature reference, transcript) | Stage 01 | Yes |
| Acknowledged responsibility flag | Stage 01 | Yes |
| Jira project(s) and Confluence space(s) to read | User (confirmed against Stage 01 source references) | Yes |
| Microsoft 365 sources to read — SharePoint/OneDrive files, Outlook mail, Teams meeting recaps/transcripts, Teams chats and channels | User (confirmed scope, step 0) | If the engine is Copilot with a live connector |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-evidence-gatherer)`

Build the **evidence dossier** in the mode the job type selects. One skill,
mode-steered — the gathering discipline is shared (read-only, cite
everything, flag confidence), only the sweep differs:

0. **Scope confirmation — before any read.** Propose a concrete sweep scope
   across the surfaces this engine can actually reach: the Jira items and
   Confluence spaces from Stage 01 and, on Copilot with a live connector,
   the Microsoft 365 sources tied to *this job* — the named meeting's recap
   or transcript, mail and chat threads about the named work, the team
   channel, SharePoint/OneDrive folders the user names — inside a date
   window around the work. Never a whole-mailbox, all-chats, or
   whole-site sweep. The user confirms, trims, or redirects before anything
   is read; each later widening is confirmed the same way. Record the
   confirmed scope in the dossier header.
1. **`closeout` mode** — walk the closed work item(s): all fields, the full
   comment thread, linked Confluence pages, linked issues (blocks/relates),
   and attachments' names (not contents, unless the user opens them). Record
   what was actually done and decided, distinguishing outcome statements from
   plan statements — a comment saying "we will" is not evidence that "we
   did."
2. **`modernize` / `tree-audit` mode** — inventory the target page tree: per
   page, title, parent, labels, last-updated date, contributors count, and a
   structure sketch (headings). Collect staleness signals per
   `../reference/documentation-standards.md` (age past the doc type's
   threshold, dead links, orphaned position). `tree-audit` sweeps the full
   tree; `modernize` sweeps the pages the user scoped.
3. **`sad-update` mode** — gather the delivered feature's evidence: the
   feature's Jira items, linked design docs or ADRs, and (where a repo is in
   scope and Copilot is the engine) the delivering change's repo context.
   Identify which existing SAD pages and diagram sources reference the
   touched components.
4. **`meeting` mode** — distill the screened transcript/summary into:
   decisions made, actions agreed, topics discussed, and Jira items
   explicitly mentioned (resolve mentioned keys against Jira to confirm they
   exist). Separate decisions from discussion; carry no attributions the
   Stage 01 screen did not approve.
4a. **Microsoft 365 sources (Copilot).** Read-only, inside the confirmed
   scope. What they add per mode:
   - `meeting`: a Teams recap or transcript can be the job's source material
     directly, in place of a pasted one — distilled exactly as step 4 says.
   - `closeout` / `sad-update`: decisions and outcomes recorded in mail,
     chat, or SharePoint design documents that never reached Jira or
     Confluence. The outcome-vs-plan distinction applies with extra force —
     chat is where "we will" is most often said.
   - `modernize` / `tree-audit`: rarely needed; the page tree is the
     evidence.

   **Mail and chat get the strictest screen of any source** — the same
   standard as a meeting transcript. Distill to decisions, outcomes, and
   facts about the work; never quote personal or off-topic content; carry no
   names or attributions the Stage 01 screen did not approve; cite by link
   or message reference rather than pasting. Anything `confidential` — HR or
   personnel matters, customer detail, credentials — stops the sweep per the
   data boundary below.
5. **Dossier assembly** — every entry carries its source link (Jira key,
   page URL, transcript line reference, mail/chat/file reference) and its
   source surface (Jira, Confluence, SharePoint/OneDrive, Outlook, Teams) and a confidence note where the
   evidence is indirect. Gaps the evidence cannot answer are listed
   explicitly as **open evidence questions** — Stage 3 turns these into open
   sections rather than letting them be silently guessed.

This stage is read-only on every platform it touches.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Evidence dossier (header: job type, confirmed scope, surfaces swept; body: cited entries in the job type's mode shape, each with its source surface) | Stage 03 | structured markdown |
| Open evidence questions list | Stage 03 | list, each with what's missing and why |
| Mentioned-Jira-items list with existence confirmed (meeting mode) | Stages 03, 06 | list of keys + summaries |

## Verify

Cross-stage trace: the dossier Stage 02 hands forward answers to the job type
Stage 01 confirmed. Check that the dossier header's job type equals Stage
01's confirmed selection, and that every dossier entry carries a resolvable
source link — an uncited entry is treated as an open evidence question, not
evidence. The failure this catches is Stage 03 planning documents from
unsourced or wrong-mode material. Running this check leaves a one-line result
in the run's decision log.

- [ ] Dossier header names Stage 01's job type
- [ ] Every dossier entry has a source link that resolves (spot-check at
      minimum the entries Stage 03 builds work-order lines from)
- [ ] Outcome vs. plan statements distinguished (closeout mode)
- [ ] Staleness signals collected per the standards baseline (modernize /
      tree-audit modes)
- [ ] Mentioned Jira keys resolved against Jira (meeting mode)
- [ ] Open evidence questions listed explicitly — none silently absorbed
- [ ] No write occurred on any platform touched
- [ ] The sweep scope was confirmed by the user before any read, and no
      source outside it was read
- [ ] Every entry names its source surface; mail and chat entries are
      distilled to work facts, with no unapproved names or verbatim
      personal content

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution against a confirmed job type;
  the dossier is inspected for coverage and citation, not re-derived.
- **Evidence:** the dossier itself (cited) and a one-line entry in the run's
  decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot — **read-only on
  every surface, for both.** Rovo reads Jira and Confluence natively.
  Copilot reads Jira and Confluence through read-only connectors, the
  repo side for `sad-update`, and — where a live connector exists —
  SharePoint/OneDrive, Outlook, and Teams. (Widened 2026-10-21 on operator
  decision; previously Rovo-only for the Atlassian sweep.)
- Evidence gathered from Microsoft 365 that later appears in a Confluence
  page crosses from one platform into another. The per-entry source surface
  is what lets Stage 05's PII and attribution check see where each fact came
  from.
- If gathered evidence surfaces `confidential` content (customer detail in an
  incident record, credentials in a comment), stop the sweep, flag it, and
  re-scope with the user before continuing.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
