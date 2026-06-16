# Tasks

## What this room is for
The two scheduled tasks that keep the instrument alive: a frequent lightweight tally and a less-frequent heavyweight synthesis. These are the automated heartbeat that turns ambient work into carried-across signal.

## What lives here
The two task definitions below. When Cowork scheduled tasks run, they read these.

---

## Task 1 — Weekly Tally (lightweight, frequent)

**Cadence:** weekly.

**What it does:**
- Counts what is accumulating: starters in /backlog-skill-starters by state, skills completed this week, traces logged by capability.
- Surfaces stalls: starters sitting in claimed too long, anything stuck in /forge.
- Proposes new rooms from /00-intake clusters — if several captures point at the same mode of work, propose a room (Cincinnatus approves before any folder is minted).
- Writes a short tally note; does NOT synthesize or propose Hermes targets (that is Task 2's job).

**Output:** a brief status surfaced to Cincinnatus. Cheap, frequent, low-judgment.

---

## Task 2 — Synthesis Pass (heavyweight, infrequent)

**Cadence:** monthly (or on-demand when corpus has grown meaningfully).

**What it does:**
- Reads /traces + /corpus together.
- Finds patterns across many builds — recurring capability clusters, repeated triage outcomes, execution-tier calls that proved wrong on reflection, foreign-intake failure modes.
- Writes a dated finding to /synthesis with source: ai.
- For each pattern cluster, proposes a Hermes migration target — because Hermes inherits this process, the target is concrete:
  - agent: a behavior the skill-foundry-agent should encode
  - gateway: an execution-tier routing rule
  - mcp-skill: a capability worth wrapping for the council
- Adds emergent design material to /harness when a finding implies agent-prompt or wiring decisions.

**Output:** a synthesis finding + Hermes-target proposals. This is the carry-across — the slow-motion writing of the agent spec.

---

## What good looks like
The tally is boring and reliable (it should never require thought). The synthesis is insightful and destination-oriented (every finding points somewhere in Hermes). The anti-pattern: a synthesis that summarizes without proposing a target, or a tally that tries to do synthesis's job.

## Skills
None directly — these are scheduled-task definitions, not skill invocations.
