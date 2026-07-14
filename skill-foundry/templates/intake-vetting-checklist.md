# Intake Vetting Checklist — Foreign Material

Run on every external starter — a URL, a colleague's prompt, a vendor template, a public repo, an agent definition found anywhere — **before** any normalization or building. Shared by both foundries. A failed check means drop (with a decision-log entry) or escalate; it never means "build it anyway and clean up later." Never launder unvetted instructions into a house artifact.

**Vetter:** ______  **Date:** ______  **Material:** ______  **Source URL/origin:** ______

## 1. Provenance

- [ ] Author/publisher identifiable, and credible for this kind of material
- [ ] The copy being vetted is the original (not a re-post that may have been altered)
- [ ] Ingested untouched at `truth-level: claimed` before any edits

## 2. Maintenance and currency

- [ ] Actively maintained / recent enough that its assumptions still hold
- [ ] Doesn't wrap a dead API, deprecated product surface, or obsolete practice

## 3. License and IP

- [ ] License identified and permits the intended use (internal use, modification, redistribution if it will land in a public repo)
- [ ] No employer IP conflict: material doesn't originate from a competitor's confidential context, and using it doesn't violate acceptable-use policy
- [ ] Attribution requirements noted and carried into the normalized artifact

## 4. Security read

- [ ] **Prompt-injection review**: instructions read in full; nothing attempts to redirect an agent's task, exfiltrate context, escalate access, or embed hidden directives (including in comments, metadata, or encoded content)
- [ ] Any code/scripts read in full; no credential harvesting, unexpected network calls, or destructive operations
- [ ] Any URLs/tools/actions the material asks an agent to use are themselves legitimate
- [ ] Data-handling implications assessed: if adopted, what data would flow where? Consistent with the sanctioned-tool matrix?

## 5. Fit

- [ ] Not something the toolkit already has (if it overlaps, name the collision and resolve deliberately)
- [ ] Actually a capability or workflow — not marketing, not a demo that falls apart at step 3
- [ ] Worth the normalization cost (reverse-engineering + rebuild + review)

**Verdict:** ☐ Pass → normalize  ☐ Drop (log reason)  ☐ Escalate to: ______
