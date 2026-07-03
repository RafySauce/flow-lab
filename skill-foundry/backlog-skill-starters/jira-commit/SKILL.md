---
name: jira-commit
description: >
  Maps a validated, signed-off Jira work item payload to Jira fields per the
  selected type's schema in the work-item-schemas registry, resolves hierarchy
  and dependency links, applies stakeholder tags as labels, shows a mandatory
  dry-run preview, executes the commit through the engine's native Jira
  capabilities, and manages the session loop/close decision. Invoke at Stage 06
  of the ai-refinement flowspace with a signed-off Stage 05 payload in hand. Do
  NOT use to validate the payload (workitem-validation) or for bulk
  imports/edits of existing issues outside a refinement run.
# --- provenance (house layer) ---
id: jira-commit
type: skill
artifact-version: "1.2"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
generated-by: skill-foundry
generated-by-version: "1.1"
data-class: public
related: ["[[sp-jira-commit]]", "[[ai-refinement]]", "[[work-item-schemas]]"]
---

# Jira Commit

The commit boundary of the `ai-refinement` pipeline — the only skill in the
family that writes to an external system. It translates the signed-off payload
into a Jira create/update — field set driven by the selected type's schema in
the work-item-schemas registry — with hierarchy, dependency links, and
stakeholder labels resolved, always behind a dry-run preview and explicit
approval, then closes the loop: next item or session summary. The commit rides
the engine's native Jira capabilities first (Rovo's built-in Jira actions);
a sanctioned Jira connector is the fallback for engines without them.
Everything upstream drafts and gates; this skill acts.

## Flow Diagram

```mermaid
flowchart LR
    Start(["Trigger: signed-off payload<br/>from Stage 05"]):::start --> M["Step 1 — Map fields<br/>Registry schema for the type →<br/>standard + discovered custom IDs"]:::process
    M --> L["Step 2 — Resolve links<br/>Parent (epic/parent link),<br/>blocking deps, stakeholder labels"]:::process
    L --> P{"Parent + fields resolve<br/>in target instance?"}:::decision
    P -->|No| H["Halt — report unmapped<br/>field / missing parent"]:::halt
    P -->|Yes| DR["Step 3 — Dry-run preview<br/>Full payload, readable form"]:::process
    DR --> A{"User approves?"}:::decision
    A -->|No| H2["Stop — return payload<br/>for revision"]:::halt
    A -->|Yes| X["Step 4 — Commit<br/>Native Jira actions (or sanctioned<br/>connector); confirm key + URL"]:::process
    X --> SL["Step 5 — Session loop<br/>Refine another / done"]:::process
    SL --> Output(["Output: issue key + URL<br/>(+ session summary on close)"]):::output

    classDef start fill:#1e293b,stroke:#94a3b8,color:#f1f5f9
    classDef process fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef decision fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef output fill:#14532d,stroke:#4ade80,color:#dcfce7
    classDef halt fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Triggering intent

- **Fires on:** Stage 06 of `ai-refinement`, with a Stage 05 signed-off payload
  in hand; "commit this item to Jira."
- **Does not fire on (near-misses):** validating or formatting the payload
  (`workitem-validation`); creating issues from unrefined text ("just make a
  ticket that says…" — route through the pipeline); bulk imports, migrations,
  or edits to existing issues outside a refinement run.

## Method

1. **Field mapping, registry-driven.** Load the selected type's schema from
   the flowspace's `reference/work-item-schemas.md` — the registry is the
   authoritative required-field set per type; the payload's completeness was
   gated upstream against it. Map standard fields (`summary`, `description`,
   `duedate`, `issuetype`) directly. Map every remaining registry field for
   the type — problem_statement, business_outcomes, customer_business_value,
   in_scope, out_of_scope, type_of_work, work_category, acceptance_criteria,
   and for spikes question_to_answer and timebox — via per-instance
   custom-field-ID discovery, seeded by the registry's field names. A field
   the target instance lacks is a halt with a named field, never a silent
   drop.
2. **Linkage resolution.** Validate the parent exists — via the engine's
   native Jira lookup where available; set epic link (feature under solution
   epic) or parent link (story/task/spike under feature). Queue blocks /
   is-blocked-by links for every Stage 03 blocking dependency. Apply Stage
   02/03 stakeholder tags and coalition/conflict-axis annotations as Jira
   labels (or the instance's designated fields).
3. **Dry-run preview.** Present the complete payload — fields, links, labels —
   in readable form. Commit only on explicit approval; "looks fine, go" from
   an earlier stage does not carry forward.
4. **Commit and confirm.** Execute the commit through the engine's native
   Jira capabilities first: on Rovo, the built-in create issue / update issue
   / create issue link actions, with authentication and field resolution
   handled by the platform. On engines without native Jira actions (Copilot),
   fall back to the workspace's sanctioned Jira integration (e.g., Atlassian
   MCP/connector). Return the issue key and URL. On error (field not found,
   parent not found, permission denied): report precisely, roll nothing
   forward, and never leave a partial commit unreported.
5. **Session loop.** "Refine another" → retain session context (guardrails,
   persona, schemas) and return to Stage 02. "Done" → produce the session
   summary listing every created key/URL.

## Inputs and grounding

Reads: the Stage 05 signed-off payload, Stage 03's classified dependency list,
Stage 02's stakeholder tags, the hierarchy position from Stage 01, and the
selected type's schema from the flowspace's `reference/work-item-schemas.md`
(the authoritative required-field registry — for `solution_epic` and `feature`
the source clipping remains authoritative on divergence). Grounding rules:
commit exactly the signed-off payload — any mutation after sign-off invalidates
the run; the field set comes from the registry per type, never from memory;
discover custom-field IDs from the live instance rather than assuming them,
seeded by the registry's field names; report the platform's actual response,
never a presumed success.

## Data boundary

- Max data-class: internal. Payloads travel only over the platform's
  authenticated, encrypted channels; issue keys/URLs are internal-shareable.
- The skill never stores, logs, or requests API credentials — authentication
  is the platform's (Rovo/Copilot integration) concern.
- Sanctioned engines: Rovo (native Atlassian actions) and Copilot (via the
  sanctioned Jira integration), per the employer matrix.

## What this skill is not

- **Not a validator** — it assumes a signed-off payload; unvalidated input is
  refused and routed to `workitem-validation`.
- **Not a drafting tool** — content questions reopen the upstream stages.
- **Not a bulk-import or migration tool** — one signed-off item per commit.
- **Not autonomous** — no commit without the dry-run preview and explicit
  approval, ever; this mirrors the flowspace's human-at-every-boundary method.

## Review criteria

A single output of this skill is acceptable when:

1. Every field in the selected type's registry schema maps to a resolved Jira
   field ID (spike runs include question_to_answer and timebox), or the run
   halted naming the unmapped field.
2. The parent link is correct for the hierarchy level, and the parent was
   validated to exist before commit.
3. Every Stage 03 blocking dependency appears as an issue link; stakeholder
   tags appear as labels.
4. The transcript shows the dry-run preview and the user's explicit approval
   *after* it.
5. The committed issue (fetched back by key) matches the signed-off payload
   field-for-field.
6. Any API error was reported verbatim with no partial state left silent.

## Adapters

| Engine | Artifact | Generated from spec version |
|---|---|---|
| Rovo | adapters/rovo-agent.md | 1.2 |
| Copilot | adapters/copilot-prompt.md | 1.2 |

## Changelog

- **1.2** (2026-07-03) — Field mapping grounded in the work-item-schemas
  registry: the required-field set is read per selected type (adding the spike
  fields `question_to_answer` and `timebox` the 1.1 list omitted), with
  per-instance ID discovery retained as the mechanism, seeded by registry
  names. Commit path made engine-native-first: Rovo's built-in Jira actions
  are the primary path, sanctioned connector the fallback (operator
  instruction, 2026-07-03 — supersedes the "after ratification" deferral in
  the flowspace's work-item-schema-extension log; the schemas themselves
  remain `to-review`). Both adapters regenerated. Content change: pre-gate
  evidence re-run required — see
  `decision-log/2026-07-03-ai-refinement-skill-revision-pass.md`.
- **1.1** (2026-07-03) — Flow Diagram brought to one-for-one with the Method
  prose: the session-loop decision (Method step 5) added as its own node instead
  of being folded into the terminal output (pre-gate spec-review finding; no
  behavior change). Adapters re-stamped — content unchanged by a diagram-only
  revision.
- **1.0** (2026-07-03) — Initial build from `sp-jira-commit`.
