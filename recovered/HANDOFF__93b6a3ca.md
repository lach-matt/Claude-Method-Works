# THE METHOD 1.6 — HANDOFF (chat 1 → chat 2), 2026-08-23

## Standing directives (carry forward verbatim)
Prime Handoff at 90% context. Prime Zeno: segment every action; order fetch → read → analyse → close flags → report; close each step before the next. Review project knowledge first; review chats/artefacts before any restore. Project is construction of publishable drafts; reader-perspective audits essential; compendium gold standard (scope, taxonomy, consistent form, unified voice, fact-check, cross-reference, dual-purpose, hierarchy). The set of books is a self-referencing, self-defending closed index: every claim a volume makes about itself must be true of the file that carries it; corrections keep both states; form changes are register entries.

## Rulings received
1. .md files canonical; JPEG bundles (mis-named .pdf) visual reference only; `theory_of_everything_*` deferred (later, separate).
2. Löwdin arc = Chapter 35, registers 1701–1712; three-body arc = Chapter 36, registers 1713–1724 (timestamp order).
3. Register form: **ruling C** — full normalisation to the settled form (caps headline, italic body); evolution recorded as entry 1725.
4. Spectra totals paragraph: restate from the table (done in Spectra Part IV and main Appendix B.2).

## Outputs (all in /mnt/user-data/outputs; "-2" = merged + audited)
The_Method_1_6-2.md · The_Register-2.md · Mathematical_Compendium-2.md · Physics_Compendium-2.md · Index_of_Indices-2.md · Spectra_Compendium-2.md · THE-LOWDIN-SOLUTION-2.md · Three_Body…Lach-2.md · figures/ (15 PNG) · MANIFEST.md · REGISTER_AUDIT.md · MATH_AUDIT.md · PHYS_AUDIT.md · IOI_SPEC_AUDIT.md · MAIN_AUDIT.md · this file.
Build scripts (not outputs, reproducible from Register-1 etc.): merge_math.py, merge_phys.py, merge_ioi.py, merge_main.py, normalise_register.py.

## Phase status
- Phase 0 ✔  Phase 1 ✔ (six volumes + two papers merged; figures placed)
- Phase 2: Register ✔ · Math ✔ · Physics ✔ · IOI ✔ · Spectra ✔ · Main: mechanical ✔, **sampled read pending (V9)**
- Phase 3 (cross-volume) not started · Phase 4 (production) not started

## Open items needing the author
A. Main V6 — Part VII subsection style (numbered vs unnumbered).
B. Main V7 — Chapter 34 closing aside vs Chapter 36 (forward pointer or leave).
C. `FIG5spectraindex3D.png` unplaced (candidate: second panel to Löwdin paper Fig 1, or Chapter 35).
D. Löwdin paper refs 6, 7, 9, 12 carry bracketed placeholders — complete before production.
E. Missing assets: 8 host compendium figures (`figures-compendia/fig-supply, fig-channel-map, fig-index-final, fig-spectra-lattice, fig-i1-tower … fig-i4-crossing`); all main-volume figures (1–25); nothing embedded in main yet.
F. Generators stale and stated so: `register_gen.py` (Register front matter + entry 1725), `spectra.py` (Spectra Part IV + main App B.2). Rebuilds owed.

## Phase 3 plan (cross-volume), in segments
1. Chapter-shift (+2) test across every volume for `§` refs (Math had 8; others clean; main clean) — done for all; confirm in one pass.
2. Register cited-by recount: parse every "register NNN" across all -2 volumes → regenerate load-bearing table (376 figure and top ten) → set "225 cited in chapters" from data.
3. Compendium object ↔ register: every `X.y` object's `source *R nnn*` / `register nnn` resolves; every LS/3B object's depth confirmed against chains (M8); Λ_phys "objects rest on it" for the five new parameters (P6).
4. Main-volume Index closure re-run (V8) and Index of Indices "book's own indexes" counts.
5. Bibliography ↔ References: every compendium bibliography work appears in main References or is scoped to a companion.

## Phase 4 plan (production)
docx/pdf per volume from the -2 .md (read docx SKILL.md first); front matter, contents, index; figures from `figures/` + the missing assets above; papers formatted separately.

## Method notes for the next instance
- All -2 volumes are UTF-8/LF; code spans must be excluded from any text normalisation.
- Register entry regex: `^### \d+` (single) and `^### \d+(, \d+)+` (grouped fault entries after 361).
- Section headings in main: `^#{2,4} N(.N)*`; the contents block (lines ~109–170) duplicates headings — skip it when counting.
- Do not trust any "generated … cannot drift" sentence; test it against the file.