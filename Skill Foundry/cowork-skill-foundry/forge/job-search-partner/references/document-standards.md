# Document Standards — docx/pdf build rules and verification

Replaces the source's LaTeX chain (moderncv + cover.cls + compiled-PDF
inspection) with the house docx/pdf skills. The source's core insight survives
the translation: **the rendered document is the truth, not the source content** —
page breaks and layout misbehave, so inspect the output before presenting.

## Build route

- Default: **.docx** via the house docx skill (employers expect editable or
  PDF-exported Word-class documents; user can export to PDF themselves).
- On request: **.pdf** via the house pdf skill.
- Output location: `applications/<company>/` in the workspace —
  `cv-<person>-<company>.docx`, `cover-<person>-<company>-<role>.docx`.
- Read the relevant house skill's SKILL.md before building; this reference
  governs *content and verification*, not docx mechanics.

## CV format

- **Exactly 2 pages.** Not 1, not 3.
- Clean professional single-column layout; name + contact header; sections:
  profile statement, experience, skills, education, then
  certifications/publications/awards as the profile warrants.
- Tailoring lives in: the profile statement, bullet emphasis and order, skills
  selection, section order. Substance never changes (writing-style.md rule 6).
- No entry title orphaned at a page bottom with its bullets on the next page —
  adjust spacing or content order to keep entries whole.

## Cover letter format

- **Exactly 1 page**, signature block included — never spills.
- Date, addressee block (named person when the posting gives one), headline per
  the writing-style formula, body per the writing-style structure, signature.
- Same font family throughout, bullets included.

## Verification checklist (run once, Phase D, against the rendered files)

### Factual accuracy
- [ ] Every claim matches the career profile — no fabricated skills, experience,
      or achievements
- [ ] Titles, dates, companies, locations correct
- [ ] Contact details correct (this is the one place real PII belongs)
- [ ] All company-specific claims independently verified — reviewer research
      not taken on faith

### Targeting
- [ ] Profile statement / opening tailored to this role, not generic
- [ ] Bullets reframed toward the job's requirements
- [ ] Key requirements addressed; gaps acknowledged where material
- [ ] Nice-to-haves highlighted where genuinely matched

### Consistency
- [ ] CV and letter agree with each other (no contradictions)
- [ ] Tone consistent and matched to the person's register

### Quality
- [ ] No spelling/grammar errors
- [ ] Letter addressed correctly ("Dear Hiring Manager" only when no name exists)
- [ ] Stretch-flagged bullets resolved by explicit user decision (keep/soften/drop)

### Rendered-output verification (never skip)
- [ ] Open and inspect the generated files (or render to PDF and view)
- [ ] CV is exactly 2 pages; letter exactly 1
- [ ] No orphaned entry titles; no clipped or overflowing blocks
- [ ] Fonts and spacing uniform

Present results as a pass/fail list alongside the documents.
