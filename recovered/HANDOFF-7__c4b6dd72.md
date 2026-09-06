# THE METHOD 1.6 — HANDOFF (chat 5 → chat 6), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-6 bundles in project knowledge (`The_Method_1_6_BUILD6_main_and_register.md`, `The_Method_1_6_BUILD6_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures: the complete set is `The_Method_1_6_figures_complete.zip` in Google Drive** (author uploaded, 2026-08-24) — unzip into `/home/claude/build/` (gives `figures/` 48 files and `figures-compendia/` 12); `FIGURE_ASSETS.md` is its manifest. Project-knowledge PNGs are a 15-file subset.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V45 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 4" and this one ("Rebuild 5"/chat 5). Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2 (`The_Method_1_6_BUILD_handoff_and_audits-2.md`); 5–14 HANDOFF-4; 15–17 HANDOFF-5; **18–20 below**. Carry all verbatim.
4. Retire BUILD-5 bundles from project knowledge once BUILD-6 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`, **`build.py`** (press: `python3 build.py <src.md> <out.docx> "<title>" [fix] [strip] <toc-depth>`; `fix` = Register entry-body form, `strip` = drop the main volume's literal contents block; needs `ref.docx` — regenerate with `pandoc -o ref.docx --print-default-data-file reference.docx`, then set Georgia 10.5pt, Letter, 1in margins, and add paragraph style `EntryBody` (italic) as chat 5 did; then `soffice --convert-to pdf`).
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## Rulings received in chat 5 (add to 1–17)
18. D.5.10: the computation decides — `dclose.py` E = 0, nothing moves (register 1738). 19. `3B.shape` = eighteenth root; stale root lines corrected from the file (1739). 20. Λ_phys: regenerate all 27 counts on the printed rule (1740). General: stale statements are corrected from current information; read the timestamps.

## State
Phase 3 complete. **Phase 4 in progress.** Register 1,536 entries (165–1743); 17 prose counts in main track it; citations 593 / 399 / 717 / 1,006; load-bearing top list unchanged. Appendix D 77/24 E = 0 (confirmed 1738). Math Compendium 265 objects · 18 roots. Λ_phys 27 counts on one printed rule.
Segment 0 ✔ (1741, 1742: all 41 figures recovered from restore-point-2_13; D.1 re-rendered at 77/24, prior kept; FIG5 placed as Löwdin Fig 1(b), item C closed). Segment 1 ✔. Segment 2: **six docx + six pdf pressed** (outputs; Register 414 pp, Math 96, Physics 25, IOI 56, Spectra 55, main 282 with 33 figures embedded) — each opened and sampled, form/tables/figures hold. Papers not pressed (item D still open: Löwdin refs 6/7/9/12).

## Open — carry
- **Asterisk residues in the renders** (1743): Register 106 (165 entries where bold-in-italic was flattened); main 738 — mostly `.** ` / `. **` bold closes before/after punctuation that pandoc's flanking rule refuses, plus literal `\|` in code-styled table lines; Spectra 375 mostly legitimate `*` species marks (check). Fix in `build.py` preprocessing (e.g. move the closing `**` before the punctuation), not in the .md.
- **32 archived plots** unread against their captions' numbers (D.1 was stale; others may be). Read each at placement; disagreement → entry.
- **`Q.delta` flag** (1740): fifteen objects still rest on the withdrawn channel equation.
- Papers: press separately after item D. Item F (stale generators) unchanged, stated.
- Carried: orphan "Figure 15.3" (Ch 28); §34.4 heading without body; §32.4.1 `[N — pair count]`; "Chapter 27 said…" (no verbatim home); §32.1 loose examples; V14 paper side; Register kinds table / F.1 995/2,433 not recomputable.
- Main Index in the docx is the .md's regenerated Index (1735) with §-locators, not page numbers; a page-number index needs a press-time pass.

## Method notes
- Any "one thousand five hundred and …" sentence is a register count only if it says entries/claims/corrections (V24; 15 sentences + 2 numeric in main).
- Register entries are the record — never edit their bodies; form is enforced at press time.
- Underscores outside code spans must be escaped for pandoc; `∂_y` swallowed an italic body (1743).
- Google Drive connector caps downloads at 10 MB; the container has no network — ask for an upload to the chat for anything larger.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.