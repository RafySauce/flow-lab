# Stage <N> — <Stage Name> (`CONTEXT.md`)

> The six-field stage contract: the ICM four (Inputs / Process / Outputs / Verify) plus two workplace extensions (Review / Data boundary). Every field must be **populated, not merely present** — the test throughout: could the next stage's owner write their Inputs from your Outputs without a conversation?

## Inputs

What this stage receives. Concrete scope: named artifacts, specific fields, or defined outputs of the preceding stage — with their locations (instance repo path, or an external-system link where the artifact lives there). "Whatever the previous stage produces" fails this field.

## Process

What happens in this stage — actionable, not a description of the output. "Synthesize the gathered material into a taxonomy" is process; "a taxonomy is produced" is not. If a skill drives this stage, reference it here:

`Layer-3: <skill-id>` · or `Layer-3: inline (one-off, described above)` · or `Layer-3: TBD — skill-primer-brief filed (<brief-id>)`

## Outputs

What this stage produces — named artifacts with their shape (e.g., "a priority-ordered list of 5–7 items, each with a one-sentence rationale") and where they land.

## Verify

A specific cross-stage trace check — name the two stages, the artifact, and the property being traced. The failure mode this catches: stage N assumes something stage N−1 no longer outputs. "Confirm the output is good" fails this field. **Running this check leaves a one-line result in the run's decision log.**

## Review

- **Reviewer:** the human accountable for this stage's output.
- **Intensity:** `heavy` (judgment stage — direction-setting or final alignment) or `light` (constrained execution). Default per the U-curve: first and last stages heavy.
- **Evidence:** what the review leaves behind (sign-off comment, decision-log line, page property update).

## Data boundary

- **Max data-class this stage handles:** `<public | internal | confidential | restricted>`
- **Sanctioned engines for this stage:** which tools may see this stage's content, per the employer's sanctioned-tool matrix.
- A handoff into this stage from an engine outside this boundary is invalid — stop and re-route.
