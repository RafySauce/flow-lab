# Verdict Format — the audit trace

Every audit ends in one artifact: a **verdict trace**, written to the project's
`traces/` as `YYYY-MM-DD-<skill>-audit-trace.md`. It is the auditor's output and,
because the foundry project is instrumented, it is also what Hermes inherits — a
worked record of a gate decision and why it went the way it did.

The trace does two jobs at once: it tells Cincinnatus the outcome and the fixes, and
it teaches the future auditor-agent what a good audit looks like. Write it for both
readers.

---

## Frontmatter

```yaml
---
date: YYYY-MM-DD
skill: <skill-name>
auditor-version: "<skill-auditor version at audit time>"
mode: intake | gate | standalone
independence: subagent | inline-self-audit   # inline lowers confidence; say why
verdict: BLOCKED | CLEAR
blocking-failures: <count>
flags: <count>
---
```

---

## Body structure

```markdown
# Audit — <skill-name>

## Verdict: BLOCKED | CLEAR

<One or two sentences: the outcome and what it means. If BLOCKED, the headline is
the block(s). If CLEAR, state that promotion is unlocked and awaits Cincinnatus's
release — the auditor did not promote.>

## Battery results

| Check | Severity | Result | Note |
|---|---|---|---|
| Schema / DNA validity | blocking | pass/FAIL | <torres-rna result; canonical or extract-validated> |
| Install limits | blocking | pass/FAIL | <measured char counts> |
| Security / safety | blocking | pass/FAIL | <findings or clean> |
| Boundary collision | blocking/flag | pass/FLAG/FAIL | <sibling + overlap, or clean> |
| Triggering accuracy | flag | pass/FLAG | <score or manual assessment> |
| Behavioral quality | flag | pass/FLAG | <concrete weaknesses or clean> |
| Voice coherence | flag | pass/FLAG | <rubric result> |

## Blocks (if any) — each with its fix path

<For every blocking FAIL: the exact file/line, what's wrong, and the specific fix.
A block without a fix path is an incomplete verdict.>

## Flags — notes for the human, not blockers

<Advisory findings. These ride along to Cincinnatus; they do not hold the skill.>

## Consequence

- **BLOCKED** → stays at `truth-level: to-review`. No `blocked` truth-level is
  minted (the schema has none and the auditor never extends it); this trace is the
  record of why it's parked. Re-audit after the fix.
- **CLEAR** → promotion unlocked, not performed. The skill stays at `to-review`
  with this clean verdict attached, awaiting Cincinnatus's release to `verified` and
  the move to `completed-skills/`.

## Capability this audit embodies

<Stamped like the foundry's build traces — the reusable capability the future
auditor-agent should carry forward. E.g. "sovereignty-first egress detection in
foreign scripts," or "boundary-collision caught by corpus diff that triggering
eval would have missed.">
```

---

## Discipline

- **Lead with the verdict.** BLOCKED or CLEAR in the first line — never bury it.
- **Every block carries a fix.** The auditor's job isn't to stop skills; it's to
  make sure only sound ones move. A block that doesn't say how to unblock is a
  failure of the verdict, not a stricter verdict.
- **Flags are notes, not penalties.** Keep the line between "the human should see
  this" and "the machine won't allow this" bright. The severity table in
  `audit-battery.md` is the contract.
- **Never claim the promotion.** The trace records that the way is clear; it never
  says "promoted." That word is Cincinnatus's.
- **Don't copy sensitive material into the trace.** If the audit surfaced PII or
  credentials, describe the finding without reproducing the data.
