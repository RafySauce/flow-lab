---
date: 2026-06-04
skill: skill-auditor
foundry-version: "0.2.2"
triage-outcome: built
intake-type: bare-conversation-intent
---

# Trace — skill-auditor build

## Triage decision

Bare conversation intent — no formal primer-brief. The exploration happened inline
across the session: the shape was worked out in a thinking-partner-style exchange
(what already exists, where the real gaps are, the build-vs-verify boundary) and
three decisions were taken explicitly via multiple-choice before the forge opened:

- **Scope:** full gate (orchestrate all dimensions), not a narrow security-only tool.
- **Automation posture:** the gate *blocks*, the human *releases* (CI-style), not
  advisory-only and not auto-promote.
- **Structure:** the user first chose "extend skill-foundry," then on reflection
  steered to a distinct, callable **skill-auditor** that serves both internal builds
  and foreign-material intake. The pivot is the key decision — see below.

Noted to user that this was bare-conversation intake; proceeded.

## Key design decisions

- **Separate skill, not a foundry mode.** The decisive argument: a maker that grades
  its own work grades it generously. Pulling verification into its own skill makes the
  check independent of the build. The earlier "extend" instinct was about avoiding a
  redundant tester; the auditor isn't redundant because it adds a capability the
  foundry never had an instrument for — foreign-material safety vetting at intake.
- **Three call-sites, one battery.** Foreign intake (go/no-go before forge effort),
  review-bench gate (binding post-emit verdict), standalone (Cincinnatus on any
  candidate). The intake call-site is where "not a code launderer" stops being a
  promise and becomes an enforced gate.
- **Orchestrate, never reimplement.** The auditor wraps torres-rna (schema),
  security-review (safety), and skill-creator's eval (triggering/quality). Its only
  original muscle is security-read synthesis, boundary-collision against the corpus,
  foreign-source vetting, and the block/clear verdict. This keeps it from re-grading
  what skill-creator already grades — the same wrap-don't-rebuild rule the foundry
  applies to skill-creator, one layer down.
- **Severity asymmetry is the core design.** Block only on the objective (schema,
  install limits, security, true boundary duplicates); flag on the subjective
  (triggering, quality, voice). Mirrors the schema's "default to the safer state"
  logic — a subjective concern reaches the human as a note, never a locked door.
  This is what makes "the gate blocks, the human releases" actually workable.
- **BLOCKED keeps `to-review`; no schema extension.** Standing decision: do not mint
  a `blocked` truth-level. A blocked skill stays at `to-review` and the audit trace
  is the record of why it's parked. If expressing "blocked" in frontmatter ever
  becomes load-bearing, it's a flagged `dna-spec.md` proposal — the auditor (like the
  foundry) never extends the schema.
- **Privacy-first weighting in the security read.** Sovereignty / phone-home /
  undisclosed egress gets explicit, heavier weight than a generic code review would —
  reflecting the household's data-sovereignty stance.
- **Foundry edited to call it (v0.3).** Triage step 2 now calls the auditor on
  foreign material before normalizing; emit gains step 8 (hand to auditor for the
  gate); a "Not the auditor" boundary line and a diagram update were added. Edits made
  to the working copy (`skill-foundry-v1/`), left for review — the installed foundry
  was not overwritten.

## Self-audit (dogfooding — the auditor's first run was on itself)

- **Install-limit check caught a real block:** the auditor's own `description` came in
  at 1127 chars (limit 1024) — un-installable. Trimmed to 982 and re-measured to pass.
  The `measure_frontmatter.py` helper worked as intended. Good omen: the gate's first
  act was to block the gate.
- **Boundary-collision (vs. skill-foundry):** FLAG, not block. Shared "foreign
  material" surface, but distinct verbs (build/normalize vs. audit/vet/gate) and the
  auditor names the foundry as its boundary. Recommend a future disambiguating tweak
  to the *foundry's* description when there's headroom (it's at 1000/1024 now) —
  collisions are mutual and the foundry side doesn't yet name the auditor.
- **Schema:** stamped against `dna-spec-extract.md` + the verified travel-planner
  exemplar; canonical `dna-spec.md` was unreachable in this environment. RNA should
  re-validate against canonical and confirm the `phase` value.

## Capability this skill embodies

**Independent verification as a gate, not a vibe:** a callable examiner that
orchestrates the lab's existing instruments into one block/clear verdict, separates
objective failure (blocks) from subjective concern (flags), and refuses to let the
maker grade its own work. The foreign-intake call-site makes data-sovereignty
vetting an enforced precondition of corpus entry rather than a hopeful promise.
This is the verification half of "evaluate before promote," built as its own tool so
the future Hermes pipeline inherits a judge distinct from the builder.
