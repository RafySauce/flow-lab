# tasks/ — Context

## What this room is for

Scheduled task definitions. The two tiers of automated work are defined here as markdown files. Each definition specifies what the task reads, what it writes (if anything), its cadence, and its done-condition. The actual scheduling is wired via the `schedule` skill.

## Decision: pulse.md

**Resolved:** The lightweight tally DOES append a dated one-liner to `review/pulse.md` on each run. Format: `YYYY-MM-DD: [intake count] intake | [corpus count] corpus | [traces count] traces | [flags if any]`. This makes trends in what is accumulating visible over time without proliferating files. Appended, not rewritten. One line per run.

---

## Task definitions

### Task 1: Lightweight Tally

**File:** `tasks/tally-task.md`

**Purpose:** Keep Cincinnatus oriented between synthesis runs. Surface what is accumulating and flag anything that warrants attention.

**Reads:**
- `intake/` — count items, note topics
- `corpus/` — count new items since last run
- `traces/` — count new items since last run, note capability distribution

**Writes:**
- One dated line appended to `review/pulse.md` (the rolling tally log)
- Nothing else durable — no new files, no changes to existing files

**Cadence:** Daily (or every session, whichever is more natural once usage patterns emerge). Start time-based; revisit if quiet periods produce meaningless lines.

**Done-condition:** `review/pulse.md` has a new dated entry reflecting current counts and any flags. If nothing has changed, the line says so — silence is not the right output.

**Flags to surface:**
- Intake cluster: 3+ items that share a topic not yet served by a project room
- Trace cluster: 3+ traces with the same capability since the last synthesis run
- Stale Active card: a board card has been Active for 14+ days with no logged movement

---

### Task 2: Heavyweight Synthesis

**File:** `tasks/synthesis-task.md`

**Purpose:** Read the full trace and corpus set, write one synthesis finding, and advance the design intelligence for the Hermes stack.

**Reads:**
- `traces/` — full set
- `corpus/` — full set
- `review/board.md` — for project state context

**Writes:**
- One synthesis finding to `synthesis/` (named `synthesis-YYYY-MM-DD-[topic-cluster].md`)
- Nothing else — does not update board, does not mint rooms

**Cadence:** Weekly. Start time-based (e.g., Sunday evening). Revisit threshold-based if quiet periods produce empty findings — a synthesis run over fewer than 5 traces is probably premature.

**Done-condition:** A new dated synthesis finding exists in `synthesis/` that (a) clusters the trace set by capability, (b) names the dominant life-domains generating signal, (c) proposes at least one migration target, and (d) proposes any new project rooms warranted by intake clustering. Cincinnatus reviews and approves/rejects proposals.

**Constraints:**
- Does not mint project rooms (proposes only)
- Does not stamp migration targets on individual traces (asserts them in the finding only)
- Does not add a usefulness field to anything, ever
- Any proposal that would route sensitive data toward a cloud API is flagged explicitly in the finding

---

## What lives in this room

- `tally-task.md` — the lightweight tally definition (expanded from above)
- `synthesis-task.md` — the heavyweight synthesis definition (expanded from above)
- Any future task definitions as the harness evolves

## Skills

`schedule` — for wiring task cadence once definitions are finalised.
