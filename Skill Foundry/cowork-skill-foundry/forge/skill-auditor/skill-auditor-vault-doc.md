---
id: skill-auditor
title: "Skill Auditor"
aliases: []
type: skill
artifact-version: "1.0"
created: 2026-06-04
updated: 2026-06-04
status: living
truth-level: to-review
domain: ai
phase: "Phase 1 — Skill Pipeline"
systems: []
tags:
  - homelab/ai
  - skill-pipeline
  - verification
  - security
execution-tier: frontier
created-by: "Cincinnatus & Claude claude-opus-4-8"
generated-by: skill-foundry
skill-version: "0.2.2"
skill-build-version: "0.1"
source: human+ai
related: []
---

# Skill Auditor

The verification mirror of skill-foundry — the fifth pipeline skill. The foundry
makes tools; the auditor judges them. It is *called* (not chained) at three
call-sites: foreign intake (vet source before the foundry normalizes), the
review-bench gate (full battery post-emit, binding verdict), and standalone
(Cincinnatus points it at any candidate). It orchestrates torres-rna, the
security-review command, and skill-creator's eval loop; its original muscle is the
security-read synthesis, boundary-collision against the corpus, foreign-source
vetting, and the block/clear verdict. See the SKILL.md in
`cowork-skill-foundry/forge/skill-auditor/` (moving to `completed-skills/` on
review).

---

## Connection Notes

*Un-verified hints for the vault-side connection skill. Not graph edges.*

- Mirror of: [[skill-foundry]] — deliberately a *separate* skill, not a foundry
  mode. The separation is the point: a maker that grades its own work grades it
  generously. When the foundry calls the auditor on a skill it just built, the
  auditor runs in a fresh subagent so the examiner isn't the author in disguise.
- Orchestrates (does not reimplement): [[torres-rna]] for schema validity, the
  `security-review` command for the safety pass, [[skill-creator]] for triggering
  and behavioral-quality eval. Each is an instrument the auditor plays. Coupling is
  live — if any of them moves or changes interface, the audit-battery reference
  needs updating.
- Load-bearing on: [[dna-spec]] — the verdict deliberately does **not** mint a
  `blocked` truth-level. A BLOCKED skill stays at `to-review` and the trace explains
  why. This was a standing decision (keep to-review, no schema extension). If a
  future need to express "blocked" in frontmatter is real, it's a flagged
  `dna-spec.md` proposal, not something the auditor invents.
- Severity model is the core design: block only on the objective (schema, install
  limits, security, true boundary duplicates), flag on the subjective (triggering,
  quality, voice). The asymmetry mirrors the schema's "default to the safer state"
  logic — a subjective concern reaches the human as a note, never as a locked door.
- Privacy-first weighting: the security read gives explicit, heavier weight to
  sovereignty / phone-home / undisclosed egress than a generic code review would —
  reflecting the household's data-sovereignty stance. This is a candidate house
  pattern for any future skill that vets external code.
- Origin: built from bare conversation intent in a single skill-foundry session
  (2026-06-04), no formal primer-brief. The shape was decided in a
  thinking-partner-style exchange inline (scope, automation posture, structure) and
  then forged. A trace is logged in `cowork-skill-foundry/traces/`.
- Schema-validation caveat: stamped against the foundry's `dna-spec-extract.md` and
  the verified travel-planner exemplar — canonical `dna-spec.md` was not reachable
  in the build environment. RNA should re-validate against canonical, and confirm
  the `phase` value ("Phase 1 — Skill Pipeline") against the canonical phase
  taxonomy.
- Forward-coupled to: the Hermes deployment session and the foundry's instrument
  module — the audit trace is exactly the kind of gate-decision record the future
  skill-foundry-agent (and an eventual auditor-agent) inherits. A scheduled sweep of
  the `to-review` queue that auto-runs the gate is a thin future add now that the
  auditor is callable.
