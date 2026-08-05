---
name: export-log
description: >
  Captures a sanitized, standardized record of what happened in a working
  session against any flow or skill in this repo — what ran, what friction
  came up, what decisions got made, what came out of it — for a human to feed
  back into the repo's own improvement loop. Fires only on an explicit user
  request ("export log," "export learnings," "export this session"), never
  automatically. Screens for PII/employer-identifying content before
  drafting, presents the draft for review before finalizing, and hands off a
  standalone Markdown document — it never files itself into a decision log,
  gap log, or backlog starter; placement is a human decision. Do NOT use for
  a flow's own in-flow session summary (already produced by that flow, e.g.
  ai-refinement Stage 06), for a raw transcript dump, or to file the export
  into the repo on the skill's own initiative.
# --- provenance (house layer) ---
id: export-log
type: skill
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
generated-by: skill-foundry
generated-by-version: "1.5"
data-class: public
related: ["[[sp-export-log]]", "[[ai-refinement]]"]
---

# Export Log

A general-purpose, repo-wide skill — not scoped to any one flow — that turns
a working session into a sanitized, standardized feedback artifact a human
can use to improve this repo's own methods. It sits outside every flow's own
close-out: a flow's Stage 06-equivalent session summary (where one exists)
records what was created, for the run's own audit trail; this skill records
what the *method itself* could do better, screened for public-repo safety,
and never commits itself anywhere — the operator-only placement rule
(`AGENTS.md` rule 5) applies to its output exactly as it does to every other
skill's.

## Flow Diagram

```mermaid
flowchart LR
    Start(["Trigger: explicit user request<br/>\"export log\" / \"export learnings\""]):::start --> R["Step 1 — Recognize and<br/>confirm scope"]:::process
    R --> I["Step 2 — Identify what ran<br/>flow(s), skill(s), stage(s)"]:::process
    I --> C["Step 3 — Capture friction<br/>and decisions, cited"]:::process
    C --> O["Step 4 — Capture outcomes,<br/>referenced not re-listed"]:::process
    O --> S{"Step 5 — Data-safety screen<br/>public-safe?"}:::decision
    S -->|"can't confidently scrub"| W["Name it withheld —<br/>never guess and include"]:::halt
    W -.-> S
    S -->|"clean"| P["Step 6 — Present draft<br/>for review"]:::process
    P --> V{"User verdict"}:::decision
    V -->|"decline / edit further"| P
    V -->|"approve"| D["Step 7 — Output standalone<br/>Markdown document,<br/>placement left to a human"]:::process
    D --> Output(["Output: provenance-stamped<br/>Markdown export"]):::output

    classDef start fill:#1e293b,stroke:#94a3b8,color:#f1f5f9
    classDef process fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef decision fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef output fill:#14532d,stroke:#4ade80,color:#dcfce7
    classDef halt fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Triggering intent

- **Fires on:** an explicit, direct user request at any point in a
  session — "export log," "export learnings," "export this session," "give
  me a feedback export," "log this for the repo." Valid at session end or
  right after a friction point the user wants captured while it's fresh.
  Never inferred or run on a schedule; the user always asks for it by name.
- **Does not fire on (near-misses):**
  - **A flow's own in-flow session summary** — e.g. `ai-refinement` Stage 06
    step 9's "session summary" on close. That record is unscrubbed, scoped
    to what was created, and belongs to the run's own decision trail. This
    skill is a separate export the user asks for *in addition to* that, not
    instead of it.
  - **A raw transcript dump.** This skill summarizes and screens; offering
    to paste the conversation verbatim is not a valid output.
  - **Filing the export anywhere.** However close a produced document's
    shape looks to a decision-log entry or a `HUB.md` gap, this skill never
    writes to either — see "What this skill is not."

## Method

1. **Recognize the trigger and confirm scope.** State back exactly what's
   being exported — the whole session, or a named portion of it (e.g., "just
   the batch-creation part") — before drafting anything.
2. **Identify what ran.** Read the session's own context to name which
   flow(s), skill(s), and stage(s) were invoked. Never guess or assume a
   flow ran based on the user's stated intent alone if the transcript
   doesn't actually show it.
3. **Capture friction and decisions.** What didn't go as the relevant
   stage/skill spec describes, what had to be worked around, and any
   mid-session decision that deviated from the written method — each point
   cited to the specific stage or skill it traces to. Nothing here is
   invented to round out the export: an uneventful session gets a short,
   honest export, not a padded one.
4. **Capture outcomes, by reference.** State what was produced without
   re-drafting it — "created 12 Jira items via `bulk-child-creation`," with
   keys/URLs where available, not a re-listing of the items' own content.
5. **Run the data-safety screen before drafting further.** Reuse the
   screening pattern already established in this repo
   (`produced-skills/bulk-child-creation/SKILL.md` step 4; Stage 01's
   data-safety guardrail in `icp-flows/ai-refinement/reference/
   ai-refinement-hybrid.md`): strip personal names, customer references,
   hostnames, credentials, and any employer-identifying detail. This repo
   holds sanitized method and exemplars only (`AGENTS.md`) — the target
   ceiling for the produced document is `data-class: public`. Content that
   cannot be confidently scrubbed is named as withheld in the draft, never
   guessed at and included; a session transcript is the highest-risk carrier
   this skill touches, since it can carry anything typed into it.
6. **Present the draft for review before finalizing.** The user may approve,
   edit, drop a section, or decline the export entirely — nothing is
   produced or shared silently, the same confirm-before-output discipline
   every other skill in this repo already applies to its terminal output.
7. **Output as a standalone Markdown document.** Valid frontmatter per
   `methodology/provenance-spec.md`, `data-class: public`, handed to the
   user directly (in-session or as a file) rather than written to any repo
   path by the skill itself. The document states plainly, near the top, that
   placement is a human decision — it may become a decision-log entry, a new
   `sp-<slug>.md` primer brief, or a flowspace `HUB.md` gap-log entry,
   whichever the reviewing human judges fits, per `AGENTS.md` rule 5.

## Inputs and grounding

Reads: only the current session's own conversation and context — which
flow/skill/stage ran, what was said, what was produced. Never fetches
external data and never reads another session.

Grounding rules, in force order:

- **Cite, never invent.** Every friction point, decision, or outcome traces
  to something that actually happened in the session under review, cited to
  the specific stage or skill.
- **"Not observed" over fabrication.** An uneventful session, or one with
  nothing worth flagging, is reported as such rather than padded to look
  substantive — the same anti-fabrication principle
  `bulk-child-creation` applies to thin rows, applied here to thin sessions.
- **Withheld over guessed.** Anything the screen can't confidently clear is
  named as withheld with a one-line reason, never silently dropped and never
  included on a guess.

## Data boundary

- Max data-class of the **produced output**: `public`.
- The **source session** may carry `internal` or higher content; the step 5
  screen is what bridges the two — it halts on content it cannot confidently
  scrub rather than guessing.
- Reads only the current session's own context — no external fetch, no
  cross-session reads, no write actions of any kind (this skill never
  creates, edits, or files anything into Jira, Confluence, or this repo).
- Sanctioned engines: Rovo, Copilot, and a bare chat session referencing this
  repo directly (`START-HERE.md`'s degrade-path pattern) — the method needs
  no live connector.

## What this skill is not

- **Not a flow's own session summary** — where a flow already produces one
  (e.g., `ai-refinement` Stage 06), that record stays unscrubbed and scoped
  to what was created, for the run's own audit trail. This skill is an
  additional, sanitized, repo-facing export the user asks for on top of it.
- **Not a filer.** It never creates or edits a decision-log entry, a
  `HUB.md` gap-log entry, or a new `sp-<slug>.md` primer brief itself — it
  hands off a document and says placement is a human decision, per
  `AGENTS.md` rule 5 (the verified/placement gate is human) and rule 7
  (propose structure, don't mint it).
- **Not a transcript dump.** It summarizes and screens; the raw conversation
  is never offered as the output.
- **Not scoped to `ai-refinement`.** Invocable from any flow or skill
  session in this repo.
- **Not autonomous.** Never triggers itself, and never finalizes a draft the
  user hasn't reviewed.

## Review criteria

A single output of this skill is acceptable when:

1. It fired only on an **explicit user request**, never inferred or
   scheduled.
2. The flow(s)/skill(s)/stage(s) named as having run are **read from the
   session's own context**, not assumed.
3. Every friction point, decision, or outcome in the draft **traces to
   something that actually happened**, cited to its specific stage or skill —
   an uneventful session produced a short, honest export, not a padded one.
4. The **data-safety screen ran before the draft was presented**, and
   anything not confidently scrubbable is named as **withheld**, not
   silently dropped or guessed at.
5. The user **reviewed the draft and could edit, trim, or decline it**
   before anything was finalized.
6. The output is a **standalone, provenance-stamped Markdown document**
   (`data-class: public`) that **states placement is a human decision** —
   the skill itself wrote to no decision-log, gap log, or backlog location.
7. The output **never duplicates or replaces** a flow's own in-flow session
   summary where one already exists.

## Adapters

| Engine | Artifact | Generated from spec version |
|---|---|---|
| Rovo | adapters/rovo-agent.md | 1.0 |
| Copilot | adapters/copilot-prompt.md | 1.0 |

## Changelog

- **1.0** (2026-08-05) — Initial build from `sp-export-log`. Staged at
  `truth-level: to-review` in `skill-foundry/review-skills/export-log/`; the
  five-point gate and promotion (including the operator's decision on where
  a produced export lands — flagged open in the primer brief) are the
  operator's. Not run on-engine. See
  `skill-foundry/decision-log/2026-08-05-export-log-skill-build.md`.
