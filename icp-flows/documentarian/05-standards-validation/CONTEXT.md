---
id: documentarian-stage-05
title: "Stage 05 — Standards Validation"
type: stage-context
stage: 5
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[documentation-standards]]"
  - "[[doc-type-registry]]"
  - "[[sp-doc-standards-validator]]"
---

# Stage 05 — Standards Validation

## Inputs

| Input | Source | Required |
|---|---|---|
| Drafted document or section diff for the current work-order line | Stage 04 | Yes |
| Open-section marker list (filled/deferred status) | Stage 04 | Yes |
| Doc-type schema (required sections, metadata fields) for the line's type | `../reference/doc-type-registry.md` | Yes |
| Documentation standards baseline | `../reference/documentation-standards.md` | Yes |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-standards-validator).
provenance-stamper (verified, produced-skills/) is referenced for the
mirror-side pass: stamping/validating frontmatter on any artifact of this
run that lands in the git mirror.`

Validation reports; it never edits and never resolves an open section.

1. **Schema completeness** — every required section of the line's doc type is
   present and non-empty (an open-section marker counts as present-by-design,
   not missing). Metadata block complete: owner, doc type, source-evidence
   links, review-by date per the type's cadence.
2. **Open-section enumeration** — list every open-section marker still
   deferred, with owner and what's-needed. Markers are never resolved,
   softened, or hidden at this stage; the enumerated list is what Stage 6
   puts in front of the user at the waiver gate.
3. **Standards pass** — check the draft against
   `../reference/documentation-standards.md`: naming convention for the page
   title, heading structure, label set for the doc type, link hygiene (every
   internal link resolves; Jira keys well-formed), formatting rules, no
   attribution or PII that the Stage 01 screen did not approve.
4. **Diff safety (update lines)** — confirm the diff touches only the
   sections the work-order line scoped; out-of-scope drift is a finding, not
   a silent fix.
5. **Findings report** — emit pass/fail per check with a one-line finding per
   failure. Failures return the line to Stage 4 for correction; the loop
   repeats until the report is clean or the user explicitly accepts a listed
   finding as-is (recorded).

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Validation findings report (pass/fail per check, findings listed) | Stage 06, user | structured checklist |
| Enumerated deferred open-section list | Stage 06 (waiver gate) | list |
| Validated document/diff (unchanged content — validation never edits) | Stage 06 | as received from Stage 04 |

## Verify

Cross-stage trace: the document Stage 05 hands forward is byte-identical to
what Stage 04 produced (validation reports, never edits), and the deferred
open-section list Stage 05 enumerates matches the markers actually present in
the document one-for-one. The failure this catches is validation quietly
"fixing" content or under-reporting open sections so Stage 6's waiver gate
sees fewer than exist. Running this check leaves a one-line result in the
run's decision log.

- [ ] Document content unchanged by this stage
- [ ] Every required schema section present (open markers count as
      present-by-design); metadata block complete
- [ ] Enumerated open-section list matches in-document markers one-for-one
- [ ] Standards checks run per the baseline; every failure is a listed
      finding
- [ ] Update-line diffs confirmed in-scope
- [ ] Any user-accepted finding recorded as accepted, not deleted

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — largely mechanical checking against written schema
  and baseline; review confirms report accuracy, not the checks themselves.
- **Evidence:** the findings report in the session and a one-line entry in
  the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Validation reads the draft and the two reference specs; it introduces no
  new content and touches no platform.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
