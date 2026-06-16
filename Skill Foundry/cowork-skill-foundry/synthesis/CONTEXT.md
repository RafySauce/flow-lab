# Synthesis

## What this room is for
The wall the signal is carried across. The heavyweight scheduled task reads /traces + /corpus and writes findings here — patterns across many builds, distilled into something that shapes the future Hermes skill-foundry agent. This is the carry-across product: the place where "we did this 30 times" becomes "here is how the agent should do it."

## Process
The synthesis task (see /tasks) runs less frequently than the tally. It reads the accumulated traces and corpus, looks for patterns, and writes a dated finding with source: ai. Each finding proposes a migration target for what it found — because Hermes inherits this process, the target is usually concrete:
- An agent behavior (a rule the skill-foundry-agent should encode)
- A gateway routing rule (which execution-tier patterns should route where)
- An MCP-skill (a capability worth wrapping for the council)

## What lives here
Dated synthesis findings (YYYY-MM-DD-synthesis.md), each stamped source: ai, each proposing a Hermes-side destination.

## What good looks like
A finding that changes how the future agent behaves. "Foreign intake from GitHub fails vetting 60% of the time on maintenance grounds -> the agent should pre-filter on last-commit-date before fetching" is a real carry-across. A finding that just summarizes the traces without proposing a destination is half-done.

## Skills
None directly. The synthesis task definition lives in /tasks.
