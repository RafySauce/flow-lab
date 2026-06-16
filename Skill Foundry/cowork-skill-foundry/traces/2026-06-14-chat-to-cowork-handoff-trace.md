---
type: trace
created: 2026-06-14
capability: foreign-intake-normalization
artifact: chat-to-cowork-handoff
---

# Trace: maaarcooo handoff → chat-to-cowork-handoff (foreign intake)

## Input

User directive: build a handoff skill to go from chat to Cowork. Search for pre-made skills first, run the best source through the foundry. Prefer GitHub repos.

Four candidates evaluated via GitHub/web search:

1. **ykdojo/claude-code-tips** — 6-line stub. Correct spirit (HANDOFF.md with Goal/Progress/What Worked/What Didn't/Next Steps), no substance.
2. **BexTuychiev gist** (`/transfer-context`) — Claude Code-only: CLAUDE.md, file line ranges, project-root paths, "wait for instructions" framing. Wrong context for chat→Cowork.
3. **maaarcooo/claude-skills** — chat-native, work-type classification (6 types), depth sizing (4 tiers), adaptive skeleton, quality checklist. No Code assumptions. **Selected.**
4. **thegeneralist01/claude-handoff-skills** — empty on fetch (gated or removed content).

REMvisual/claude-handoff was in search results but README was also empty on fetch.

## Triage and vetting

**Classified:** foreign-skill-starter (GitHub repo, single file).

**Source vet:**
- Maintenance: active — surfaced at top of 2026 skill searches with substantive, well-structured content.
- Provenance: public GitHub, no explicit license; standard open sharing posture. No concerning attribution chain.
- Security read: pure text-generation skill. Reads conversation context, writes a markdown file to disk. No external API calls, no data exfil, no tool invocations, no runtime dependencies. Clean.
- Sovereignty: no PII leaves the session. Work-type classification and depth judgment happen entirely within the model. Clean.

**Verdict:** pass — normalize with Cowork extension.

## Core preservation decisions

The source's real contribution is structure, not prose:
- Work-type classification (6 types with section suggestions) — preserved intact; categories are well-chosen and non-overlapping
- Depth-sizing tiers (Light/Standard/Deep/Extended with word-count calibration) — preserved; the calibration logic is the valuable part, not the specific counts
- Adaptive skeleton with "never include empty sections" discipline — preserved
- Quality checklist — preserved; restructured to front-load Cowork-specific checks

Table-formatted the work-type classification (source used prose lists — harder to scan at a glance).

## Cowork delta (additions by the foundry)

The source was chat-native but unaware of the Cowork receiving environment. Four targeted additions:

1. **Process Step 2 (Map the Cowork Environment)** — explicit pre-writing step to identify: skills to invoke, workspace files to reference, connectors in use, bash/terminal work flagging. This is the key structural addition; without it the handoff is just a general summary.
2. **`## Cowork Setup` section in the document skeleton** — structured block (skills to invoke / workspace files to read first / connectors needed) at the top of the handoff, after the resumption instruction. Explicitly omittable if nothing applies to avoid padding.
3. **Cowork-priming resumption instruction block** — replaced the source's generic "confirm understanding in 2–3 sentences" with specific Cowork priming: Read tool for workspace files, invoke listed skills, then confirm. The source's generic instruction lands in the wrong environment.
4. **Save-location guidance** — handoff file should land where Cowork can reach it (workspace folder or desktop). A handoff that saves to a chat-inaccessible temp path is useless to the receiving session.

## Dropped from source

- The source's verbatim instruction examples in content guidelines — kept the rules, dropped the illustrative prose (body bloat in a reference section).
- Mild reordering: clarify-ambiguities step moved before environment-mapping step (Step 4 before Step 2 in the source) — catching scope ambiguity before doing the Cowork mapping avoids mapping the wrong work.

## What This Skill Is Not entries (Cowork-specific, not in source)

Three entries added beyond the source's implicit scope:
- Not a Claude Code handoff (separate environment, separate file and command patterns)
- Not a substitute for `productivity:memory-management` (complements it)
- Not a thinking-partner output (if exploration is still live, the handoff is premature — say so)

## Limits measured

- name: `chat-to-cowork-handoff` = 22 chars ✓ (limit: 64)
- description: 680 chars ✓ (limit: 1024)
- compatibility: 174 chars ✓ (limit: 500)

## Open questions for review bench

1. **Skill list in Step 2** — the enumerated Cowork skills (homelab-architect, execution-partner, etc.) will drift as the skill catalog grows. Should Step 2 say "check the installed skill list" rather than naming them? Or is the enumeration useful as a triggering prompt even if stale? Recommend: keep the list but note it's illustrative, not exhaustive.
2. **Save location** — "Cowork workspace folder or desktop" is vague. Should the skill ask for or infer the workspace path? Current approach: leave it to judgment (consistent with the source's non-prescriptive file handling).

## Status

Emitted at `truth-level: to-review`, `execution-tier: frontier`. Eval not yet run. Awaiting Cincinnatus review at the bench.
