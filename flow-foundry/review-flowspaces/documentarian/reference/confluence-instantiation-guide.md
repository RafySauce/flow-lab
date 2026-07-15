---
id: documentarian-confluence-instantiation-guide
title: "Confluence Instantiation Guide — Documentarian"
type: specification
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
  - "[[custody-model]]"
---

# Confluence Instantiation Guide — Documentarian

Operator checklist for deploying this flowspace design into employer tenancy.
**Prepared, not executed** — every step here is the operator's act, per
mirroring-protocol. This public copy stays sanitized; tenant names, space
keys, and agent configurations exist only on the internal side.

## Page-tree structure (mirroring-protocol §2 mapping)

```
Documentarian (parent page ⇄ HUB.md)
├── 01 — Intake & Routing        (⇄ 01-intake-and-routing/CONTEXT.md)
├── 02 — Evidence Gathering      (⇄ 02-evidence-gathering/CONTEXT.md)
├── 03 — Doc Plan & Template Match
├── 04 — Draft & Update
├── 05 — Standards Validation
├── 06 — Commit & Link
├── 07 — Custody & Close
├── Reference                    (⇄ reference/, one child page per file)
├── Decision Log                 (⇄ decision-log/, one child page per entry)
└── Doc Registry                 (the custody-model index page — instance
                                  artifact; no design-copy equivalent)
```

Frontmatter ⇄ page properties + labels per mirroring-protocol §2
(`truth-level` label, `src-human-ai`, `dc-internal`; Status macro for
`status`). At instantiation, add the per-stage `work/` folders and the
`handoffs/` folder on the mirror side — absent from this design copy by
convention.

## Operator checklist

**Space setup**
- [ ] Target documentation space chosen; flowspace page tree created per the
      mapping above
- [ ] Mermaid-rendering macro confirmed installed in the space — else the HUB
      page notes "diagram: see mirror" (setup-questionnaire item; do not ship
      a dead code block)
- [ ] Doc-registry index page created per `custody-model.md`, empty
- [ ] Label set from `documentation-standards.md` agreed (doc-type labels,
      `servicenow-pending`, `archive-candidate`, `archived`)
- [ ] Archive mechanism fixed for this tenant (archive space / archive label /
      native archiving) and recorded in the instantiated custody model
- [ ] Open-section marker rendering decided (canonical blockquote vs. a
      confirmed task/status macro) and recorded in the instantiated protocol

**Governance**
- [ ] Sanctioned-tool matrix consulted: Rovo confirmed for `internal`
      Confluence/Jira read+write; Copilot's repo-side role for `sad-update`
      confirmed; any Copilot-side Atlassian connector status recorded
- [ ] Internal policy link inserted at Stage 01, step 2 (redacted in this
      public copy)
- [ ] ServiceNow question answered for this tenant: is any integration
      sanctioned? Record the answer on the deferred
      `sp-servicenow-kb-commit` brief either way
- [ ] Documentation-owners register: instantiate from
      `icp-flows/ai-refinement/reference/platform-stakeholder-register-template.md`
      when ready; until then Stage 01 flags ungrounded mode

**Agent deployment (once skills exist)**
- [ ] Skills promoted through the skill-foundry's five-point gate before any
      adapter deploys — this guide does not shortcut the gate
- [ ] Rovo agents deployed per each skill's `adapters/rovo-agent.md`; Copilot
      surfaces per `adapters/copilot-prompt.md`
- [ ] First on-engine run per adapter observed and recorded (the gate's
      simulated tests are not engine runs)

**Mirror**
- [ ] Internal repo path `flows/documentarian/` created; sync procedure and
      `MIRROR-STATE.md` per mirroring-protocol §3
