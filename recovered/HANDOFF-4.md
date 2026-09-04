# THE METHOD 1.6 — HANDOFF (chat 2 → chat 3), 2026-08-24

## THE BRIDGE — read this before anything else
The next chat does not need files transferred. Everything is reachable from inside the project:
1. **The current state of every volume** is in the two BUILD-3 bundles in project knowledge (`The_Method_1_6_BUILD3_main_and_register.md`, `The_Method_1_6_BUILD3_compendia_papers_audits.md`). Split them on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (15 files + this handoff, MAIN_AUDIT, FIGURE_MAP, D59_DRAFT, MANIFEST). Figures: `cp /mnt/project/*.png figures/`.
2. **Every finding, prior state and ruling** is in `MAIN_AUDIT.md` (inside bundle 2): V1–V35 with what was closed, what is open, and the text before each edit.
3. **How each ruling was reached** is in this project's past chats — use `conversation_search` (project-scoped) with content words, e.g. "D.5.9 re-closure", "figure renumbering", "Q domain constraint", "COORDINATES-2.13". Chat titles: "Rebuild 1" (chat 1), and chat 2 (this one). Read at the hit; do not page.
4. **The author's standing directives, rulings 1–4 and the compendium gold standard** are in HANDOFF-2 (bundle `The_Method_1_6_BUILD_handoff_and_audits.md`, still in project knowledge) — carry verbatim.
5. Retire BUILD-2 bundles and the -1 volumes from project knowledge once BUILD-3 is in, so `project_knowledge_search` returns only current text. (Not yet done by the author as of this handoff.)
Rule: anything a chat produces goes into the next bundle; nothing lives only in an outputs folder.

## Rulings received in chat 2 (add to 1–4)
5. Register count = the Register's contents (V24). 6. A.9 proof replaced (V22). 7. D re-closure: test both placements, comparison decides (V27 → derivations; E = 0 at 65/22). 8. Audit count: current = twenty-five; historical stays (V10). 9. V16 figure/proposition renumbering — go. 10. V6/V7 — number Part VII subsections; add the pointer. 11. V12, V14, V15, V9.4b, V33 — as proposed (V14: register-cited). 12. V32 — timestamp decides. 13. Coordinates file gets a place in the book (COORDINATES-2.13, COORD(Z, charge, ℓ, 2S+1)). 14. Q: R = one claim; the E.4.1 constraint dropped (refuted by R).

## State
Phase 0–2 ✔ (all six volumes, incl. main sampled read V9). Register at 1,522 entries (165–1729). Appendix D at 65 elements / 22 fibres, E = 0. Q at fourteen, E = 0 fibred, domain column printed. Figures renumbered (chapter · sequence), map in FIGURE_MAP.md.
Phase 3 not started. Phase 4 not started.

## Open (carry)
- V21: bare "§3" at line ~2232 (§11.6) — target unlocated. "Theorem 9.1 / 10.1 / 11.1 / 11.2" in D.5.2/D.5.4 are old-scheme names — sweep.
- Orphan "Figure 15.3" in Chapter 28's withdrawal (no caption under any scheme).
- §34.4 "The rule" — heading with no body before §34.5; lost paragraph or spare heading.
- §32.4.1: `[N — pair count to be confirmed]` placeholder (unrecoverable pair count).
- Withdrawal ratio (F.4.1) needs redefining now the Register is its own volume; current Ch 28 vs chapters reads 0.061.
- D: the Löwdin *challenge* mathematics (Ch 34, registers 1249–1357) never entered — next re-closure owed.
- Chat-1 items: C (FIG5 3D figure placement), D (Löwdin paper refs 6/7/9/12 placeholders), E (missing assets — author: figures are in Google Drive under another name; ask for the link), F (generators `register_gen.py`, `spectra.py` stale; now also Q/E(G)/withdrawal-ratio readouts).
- V14 paper side: three-body paper labels only checks A, B, E.

## Phase 3 plan (segments, in order)
1. Content-matched sweep: every bare §N, every "Theorem a.b", "Chapter N" in tables (D.5.2's locators: §16.1, §6.1, Ch. 10/15/17/18 are old-scheme), across all -2 volumes. Map → apply → register entry.
2. Register cited-by recount; load-bearing table (376 / top ten); "225 cited in chapters" from data; all press-recomputed prose numbers listed and either dated or generated.
3. Compendium object ↔ register resolution; LS/3B depths (M8); Λ_phys objects for the five new parameters (P6); D.5.10 for Chapter 34's mathematics.
4. Index closure re-run (V8); Index of Indices counts.
5. Bibliography ↔ References.
6. Heading levels (V11): appendices/Index/References `#`→`##`; `X.n` labels → `###`. Do at the start of Phase 4.

## Method notes
- Anchor edits on body headings; the contents block (lines ~109–172) duplicates them at a different level.
- Chapter material is sometimes copied verbatim into appendices (A.10's equation line was in §10) — edit both.
- Three numbering generations coexist (+5 / +7 / +13 chapters; +1 appendix letters; +1 Part numbers). A reference that resolves is not a reference that is right.
- Every "recomputed by the press / cannot drift" sentence: test it against the file.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.