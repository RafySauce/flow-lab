# Skill Foundry

instrumented: true

The workshop where Torres-Core skills get built, normalized to house standard, and reviewed — and the larval form of the Hermes skill-foundry agent that will eventually inherit this whole process. Serves Cincinnatus as the toolmaker's bench; serves future-Hermes as a worked, traced specification of how skill-building is done.

## Workspaces
- /00-intake — raw captures with no room yet (a half-formed skill idea, a link to revisit, a "we should build something for X")
- /intake-triage — classify and vet every starter: primer-brief vs. foreign material vs. not-skill-worthy
- /forge — the build: reverse-engineer intent, author to house standard, stamp the two artifacts
- /review-bench — the human gate: Cincinnatus reviews, eval confirms, the skill graduates
- /corpus — work products: finished skills accumulate here (mirrors completed-skills/)
- /traces — flagged foundry decisions, stamped with capability (the signal that feeds Hermes)
- /synthesis — scheduled-task findings: source ai, the carry-across into the Hermes skill-foundry agent spec
- /tasks — the two scheduled-task definitions (tally + synthesis)
- /harness — emergent Hermes design material: the skill-foundry-agent prompt, gateway routing, MCP wiring

## Queue folders (the visible pipeline, distinct from rooms)
- /backlog-skill-starters — INBOX: starters land here (truth-level: claimed)
- /completed-skills — DONE: house-standard, reviewed skills (truth-level: verified)

Rooms are *modes of work*; queue folders are *where the work-product physically sits as it moves*. A starter lives in backlog-skill-starters/ while the intake-triage and forge rooms act on it, then moves to completed-skills/ when review-bench passes it.

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Capture a half-formed skill idea | /00-intake *(not yet created)* | CONTEXT.md | — |
| Classify or vet a new starter | /intake-triage *(not yet created)* | CONTEXT.md | skill-foundry |
| Build or normalize a skill | /cowork-skill-foundry/forge | CONTEXT.md | skill-foundry |
| Review a normalized skill | /cowork-skill-foundry/review-bench | CONTEXT.md | skill-foundry |
| Log a foundry decision as a trace | /cowork-skill-foundry/traces | CONTEXT.md | — |
| Run the weekly tally | /cowork-skill-foundry/tasks | CONTEXT.md | — |
| Run the synthesis pass | /cowork-skill-foundry/tasks + /cowork-skill-foundry/synthesis | CONTEXT.md | — |
| Work on the Hermes agent design | /cowork-skill-foundry/harness | CONTEXT.md | — |
| File pipeline-wiring / exec briefs | /cowork-skill-foundry/harness | CONTEXT.md | — |

## Naming conventions
- Skill starters: `starter_<short-name>.md` (in backlog-skill-starters/)
- Completed skills: the skill folder itself, `<skill-name>/` (in completed-skills/)
- Traces: `YYYY-MM-DD-<short-name>-trace.md`
- Synthesis findings: `YYYY-MM-DD-synthesis.md`
- Companion DNA vault-docs: `<skill-name>.md` (the type: skill entity-doc)

## Rules
- Read this file first on every task.
- The skill-foundry skill is the authority on *how* to build — this project is *where*. When they seem to disagree, the skill wins on method; flag the gap.
- DNA is canonical. Every artifact stamps against dna-spec.md. The foundry never extends the schema — it flags needed changes.
- Two artifacts per skill: a clean SKILL.md (agentskills.io headers only) and a companion DNA vault-doc. Never fuse them.
- verified is a human gate. The foundry normalizes and recommends; Cincinnatus approves. Nothing self-promotes to completed-skills/.
- Foreign material is vetted before it is built — maintenance, provenance, security read. No laundering unvetted or sovereignty-violating behavior into a house skill.
- Every meaningful foundry decision earns a trace. The trace is what Hermes inherits — an un-traced build teaches the future agent nothing.
- New rooms are proposed, not minted silently. The weekly tally proposes rooms from intake clusters; Cincinnatus approves before a folder is created.
- This project is instrumented because Hermes will inherit this responsibility and process. The instrument module is not decoration — it is the agent spec being written in slow motion.
