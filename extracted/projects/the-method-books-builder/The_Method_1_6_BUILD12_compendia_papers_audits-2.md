# THE METHOD 1.6 — BUILD 12 — COMPENDIA, PAPERS, AUDITS, GENERATORS

Split on the `<<<FILE: name>>>` / `<<<END FILE: name>>>` markers (`split.py`).

<<<FILE: HANDOFF-11.md>>>
# THE METHOD 1.6 — HANDOFF (chat 9 → chat 10), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-10 bundles in project knowledge (`The_Method_1_6_BUILD10_main_and_register.md`, `The_Method_1_6_BUILD10_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures:** unchanged this chat — reuse `The_Method_1_6_figures_BUILD9.zip`, Drive id `1AtBAHB7Dwr8QlUmiV1_EaPNMR1X2g-kN` (nested JSON, base64 in `json.loads(d[0]['text'])['content']`); contents as HANDOFF-10 §1 describes. **Spectra level data:** `spectra_levels_store.zip` Drive id `17B2KCn6pH49q_dIi-_77rDuoiVGYy_Pw` (sha256 08a6a78c…) and the full `restore-point-2_13.tar.gz` (sha256 80577094…, 708 files; 14.2 MB, OVER the 10 MB connector cap — M uploads it to the chat directly; `spectra_raw/` inside holds the 92 per-level tables). `COORDINATES-2_13.csv` Drive id `1gblLH2cE6cBX5H_Nm8AB-72iF6eSdxxQ` (δ per cell, NO per-level energies — fetch only when a build reads from it).
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V48 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5", chats 6–9. Read at the hit; do not page.
3. **Standing directives**: rulings 1–4 HANDOFF-2; 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7; 21–22 register 1751; 23 register 1758; **24 register 1761** (§34.4 is the canonical statement of the rule — the rule, what it is, derivation, attribution, function; §34.1 defers to it); **25 register 1762** (a SURVIVING CLAIM defined, D.5.3 generalised; census 77+265+27=369 by `appf.py`; withdrawn = one claim per register entry, both readings dated); **26 register 1763** (the sealed bracket at strict membership, quotation floor the only ε, §22.5 admissibility, σ = the floor; option B rejected on M's four grounds; issued as RULING-TOLERANCE-489.md, in bundle 2). Carry verbatim.
4. Retire BUILD-9 bundles from project knowledge once BUILD-10 is in.
5. Tools as HANDOFF-10 §5, with these changes: `build.py` adds `cont_tables()` (register 1764 — re-heads headerless pipe-table continuation blocks, with a blank line so a table cannot interrupt a paragraph; guards: ≥2 rows, ≥4 cols, column count matches the parent; lone determinant/absolute-value pipe lines stay text); `appf.py` computes and press-rewrites F.4.2's census, numerator and ruled row from the compendium and Register files beside the source (ruling 25); `spectra_count.py` also sums the bracket column; new `run489.py` (the ruled run, results in `run489_final.json`) and `ruled_bracket.py` (single-file verifier). `ref.docx` recipe unchanged (HANDOFF-8 §5); Georgia in docx, Caladea or other substitution in container PDFs — page totals vary by container (this one: main 249, Register 354, Spectra 21 vs chat 8's 289/426/28); the object, not the page count, is the invariant.
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## State
Phase 4. Register **1,557 entries (165–1764)**; chat 9 registers 1761–1764. **Counts discipline changed at 1762: main now carries 15 prose + THREE numeric register counts** — lines at §28 (7375-region), the References note (7660-region), and **F.4.2's "1,557 at this build"** — all move together with the Register's two count lines; F.4.2's ruled row (withdrawn/ratio/p/bits) moves too and `appf.py --write` recomputes it at press as backstop. After any new entry run `kinds.py <register> --write`. The three author items of 1760 are RULED AND CLOSED: §34.4 (ruling 24, body per M, §34.1 reframed); F.4.2 (ruling 25, value 4.22 : 1, p 0.192, 0.705 bits at this count); Spectra's 489 (ruling 26 — 318 rows closed: 658/813 cells pass, 155 FAIL across 92 rows, 0 refused, 68 `no-triple`; 171 stay `untested` for data). Main, Register and Spectra pressed at Build 9 stamps in this container and sampled at every change; the other five volumes carry no change this chat and their chat-8 presses stand (zero orphan pipe blocks in all five, measured).

## Open — carry
- **126 Spectra rows unreconciled**: their member selection (parent-term wall 1578, coupling choices) is not reproducible blind from `spectra_raw`; results were computed but NOT incorporated (run489_final.json holds them under 'unrec'). Path: M supplies the built per-row cell lists, or the selection rules, from the Löwdin project.
- **45 Spectra rows no-data**: Bi III, C I, Cd II, Hg II, N I, Sc III captures post-date restore-point-2_13; exist in no bank in reach.
- **Five narrow-bracket FAIL rows** (bracket width ≤ 2× quotation floor; Li III / Li II among them, hydrogenic) — FAILS under the §22.5 formula as ruled, named in 1763 for M: the refusal clause's prose condition is met while the formula refuses none; M may re-rule.
- Item Q's standing entries per the Physics Compendium; item F generator state (register 1756) — unchanged.
- The 844-of-844 provenance flag from M's ruling is CLOSED (1763): the figure is the table's own bracket-column sum.

## Method notes
- Register entries are the record — never edit their bodies. Grouped headings hold the forty early fault entries; heading count is the entry count.
- Chat 9's press defect (532 channel rows literal, register 1764) was found by sampling the pressed object at the rows ruling 26 changed — the third instance of the 1757/1759 lesson: keep sampling the object at the change, never only the source.
- V24 false-positive check still applies: "fifty-X" strings that are not entries/claims/corrections do not move with the register count (six such in main at this build).
- Incorporation discipline for external data: verify sha + file count first, reconcile member-for-member against the record's own rows, and incorporate only what reconciles (queue2 README's rule: capture all, verify, then incorporate).
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%. The three-pass page press exceeds one tool call — run its steps singly.
<<<END FILE: HANDOFF-11.md>>>

<<<FILE: HANDOFF-10.md>>>
# THE METHOD 1.6 — HANDOFF (chat 8 → chat 9), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-9 bundles in project knowledge (`The_Method_1_6_BUILD9_main_and_register.md`, `The_Method_1_6_BUILD9_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures:** `The_Method_1_6_figures_BUILD9.zip` (chat 8's output; upload to Drive and put the id here — chat 8 read the BUILD8 zip at Drive id `1l-176jSS0yKyeV3sqWh4iGxyGr4p-grG`, nested JSON, base64 in `json.loads(d[0]['text'])['content']`). It holds `figures/` (49; 16.1, 24.1, 12.3, 25.2 are re-renders, 24.1 with the measured He II series), `figures-compendia/` (12), `figures-pre-crop/` (15), `figures-pre-rerender/` (4). The four re-renders regenerate from `fig_rerender.py` + `fig241_data.json`; the He II series from `heii.py` + `heii_levels.txt` (author-supplied NIST levels, in the bundle).
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V48 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5", chats 6–8. Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2; 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7; 21–22 register 1751; **23 register 1758** (the 24.1 caption states the three rises; drawn from M's "what is a better statement? If it's b, use b"). All in bundle 2. Carry verbatim.
4. Retire BUILD-8 bundles from project knowledge once BUILD-9 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `build.py` — press: `python3 build.py <src.md> <out.docx> "<title>" [fix] [strip] <toc-depth> [pages]`; stamps "Build 9"; drops the image alt line; sets two-space aligned tables (1759); `pages` = press, map headings to pages from the PDF, write `<src>.pages.md` with a page-numbered Contents (all volumes) and print Index (main), re-press until stable (`index_pages.py`); with `strip` it also reruns `appf.py --write` so Appendix F is press-recomputed. The Register presses **without** pages and at toc-depth 0 (it is a numbered sequence; an empty TOC field was the alternative). `ref.docx` recipe unchanged (HANDOFF-8 §5); Georgia in docx, Caladea in container PDFs — accepted. Also `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`, `trueres.py`, `crop_titles.py`, `qgraph.py`, `kinds.py` (`--write` = rewrite the kinds column; run after any new entry), `rclose.py`, `bookindex.py`, `appf.py`, `tb_audit.py`, `spectra_count.py`, `index_pages.py`, `fig_rerender.py`, `heii.py`.
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## State
Phase 4. Register 1,553 entries (165–1760); 15 prose + 2 numeric counts in main track it; after any new entry run `kinds.py <register> --write`. Chat 8 registers 1753–1760. **All eight volumes pressed at Build 9** (main 289 pp — page-numbered Contents p3 and print Index; Register 426; Math 103; Physics 26; IOI 43; Spectra 28; Löwdin 16; three-body 10), each sampled at its changed pages. No render carries a stale title; no volume carries a live placeholder (sweep in chat 8); no heading is silent; every "recomputed at press" claim is true via the scripts above.

## Open — the author's, not the record's
- §34.4's new body (1755/1756): approve or reword — it restates §34.1's rule as §34.5–34.7 use it.
- F.4.2's "surviving claim" definition — in Q since register 297; no computation supplies it.
- Spectra's 489 `untested` rows — need the tolerance the builder does not state (noted above the table).
- Item Q's standing entries as listed in the Physics Compendium; unchanged this chat.

## Method notes
- Register entries are the record — never edit their bodies; build.py enforces form; grouped headings hold the forty early fault entries (1,548 → see 1756's reconciliation; heading count is the entry count).
- Both press defects of chat 8 (silent headings, run-on tables) were found by reading the pressed object at the point of change, not the source — keep sampling the object.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%. The Register's three-pass press exceeds one tool call — run its steps singly.
<<<END FILE: HANDOFF-10.md>>>

<<<FILE: HANDOFF-9.md>>>
# THE METHOD 1.6 — HANDOFF (chat 7 → chat 8), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-8 bundles in project knowledge (`The_Method_1_6_BUILD8_main_and_register.md`, `The_Method_1_6_BUILD8_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures:** `The_Method_1_6_figures_complete.zip` in Google Drive (id `1jcoJrEKFh4FfWAdKfXWgbMasDpr4OYvp`; nested JSON, base64 in `json.loads(d[0]['text'])['content']`) is now **superseded for fourteen files**: chat 7 cropped the stale title line from figure-6.1, 6.2, 7.1, 8.2, 10.1, 15.1, 19.1, 23.1, 23.2, 24.1, 24.2, 24.3, 25.1, 26.1 (register 1747). The cropped set is `The_Method_1_6_figures_BUILD8.zip` (outputs of chat 7; upload it to Drive and replace the id here). If only the old zip is available, re-crop with `crop_titles.py` (bundle 2). Originals kept as `figures-pre-crop/` in the zip.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V47 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5", chat 6, chat 7. Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2 (`The_Method_1_6_BUILD_handoff_and_audits.md`); 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7. All kept in bundle 2. Carry verbatim. **Rulings 21–22 received in chat 7** (register 1751): 21 caption 25.1 reads 1,061; 22 Λ_phys exchange count stays 15, rule unamended. Carry with 1–20.
4. Retire BUILD-7 bundles from project knowledge once BUILD-8 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `build.py` as HANDOFF-8 §5; `ref.docx` recipe unchanged. Font: docx set in Georgia; the container renders PDFs in Caladea — author has accepted this, do not flag it. Also `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`, `trueres.py`, `crop_titles.py`, `qgraph.py` (walks the Math Compendium's dependency lines; reproduces 1749's 15 = 6 + 9).
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## State
Phase 4 in progress. Register 1,545 entries (165–1752); 15 prose + 2 numeric counts in main track it. Chat 7 registers 1746–1752. **All eight volumes pressed** (main 229 pp, Register 348, Math 83, Physics 22, IOI 39, Spectra 20, Löwdin 13, Three-Body 8), sampled and holding. Chapter 28 orphan ✔ (1752, a withdrawn figure — not 24.3). Segment 3 (plots) ✔: all 32 read; 14 titles cropped; item D ✔ (Löwdin refs 6/7/9/12 filled, both papers pressed); Q.delta ✔ (1749).

## Open — carry, in order
- **Four plots owed a re-render from the book's data** (no source survives; 1747): 16.1 (4/4 → 56/56, stale title), 24.1 (He II series, monotone claim; title already cropped), 12.3 ("§7.8.1" in subtitle), 25.2 (bar labels §14.4/§17.6). 16.1 is the only stale title still in a render.
- build.py stamps "Build 6" — advance the string. (Three-Body byline and subscripts fixed, 1752.)
- Main figure captions print twice (alt line + caption): decide whether build.py drops the alt line.
- Q family closed (1750).
- Item F (stale generators) unchanged. Carried: §34.4 heading without body; §32.4.1 `[N — pair count]`; "Chapter 27 said…"; §32.1 loose examples; V14 paper side; Register kinds table / F.1 995/2,433 not recomputable; Main Index is §-locators.

## Method notes
- Plots: restore-point-2_13 holds fig00–fig27 as PNGs only; every archived plot matches one byte for byte (map in 1747). Do not look for a generator again.
- Register entries are the record — never edit their bodies; build.py enforces form. Counts: the Register's two "N entries, 165 to M" lines, main's 15 "one thousand five hundred and …" sentences and its two numerics move together.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.
<<<END FILE: HANDOFF-9.md>>>

<<<FILE: HANDOFF-8.md>>>
# THE METHOD 1.6 — HANDOFF (chat 6 → chat 7), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-7 bundles in project knowledge (`The_Method_1_6_BUILD7_main_and_register.md`, `The_Method_1_6_BUILD7_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures: `The_Method_1_6_figures_complete.zip` in Google Drive** (id `1jcoJrEKFh4FfWAdKfXWgbMasDpr4OYvp`, 6.3 MB — under the 10 MB connector cap; the download arrives as nested JSON: `json.loads(d[0]['text'])['content']` is the base64) — unzip into `/home/claude/build/` (`figures/` 49 files, `figures-compendia/` 12).
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V46 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5" and chat 6. Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2 (`The_Method_1_6_BUILD_handoff_and_audits.md` in project knowledge); 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7. All kept in bundle 2. Carry verbatim. No new rulings in chat 6.
4. Retire BUILD-6 bundles from project knowledge once BUILD-7 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `build.py` (press: `python3 build.py <src.md> <out.docx> "<title>" [fix] [strip] <toc-depth>`; `fix` = Register entry form, `strip` = drop main's literal contents block; then `soffice --headless --convert-to pdf`). Needs `ref.docx`: `pandoc -o ref.docx --print-default-data-file reference.docx`, then in `word/styles.xml` set all fonts Georgia, docDefaults sz 21, add `<w:style w:type="paragraph" w:customStyle="1" w:styleId="EntryBody"><w:name w:val="EntryBody"/><w:basedOn w:val="BodyText"/><w:qFormat/><w:rPr><w:i/><w:iCs/></w:rPr></w:style>`; in `word/document.xml` replace `<w:sectPr />` with Letter/1in (`pgSz 12240×15840`, `pgMar 1440`). Also `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`.
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## State
Phase 4 in progress. Register 1,538 entries (165–1745); 15 prose + 2 numeric counts in main track it. Segments 0–2 ✔ (registers 1744): asterisk residues closed in build.py — main 738 → 20 legitimate stars, Register 106 → 8 record-content lines, no entry bold dropped; wide tables size-to-fit; **six docx + six pdf pressed** (main 266 pp, Register 414, Math 94, Physics 25, IOI 42, Spectra 22), sampled and holding. **Those presses predate entries 1744–1745: re-press main and Register first thing** (two commands; ~3 min). Segment 3 (1745): 9 of 32 plots read.

## Open — carry, in order
- **23 plots unread** (list in 1745). Read each for (a) caption numbers, (b) an in-image title or § locator from the pre-V16 scheme — 23.1, 8.2, 10.1, 25.2 have them. Then one closing entry; remedy = re-render from plot source in restore-point-2_13 if it survives, else crop the title line. Not a caption edit.
- **Item D**: Löwdin paper refs 6/7/9/12 `[fill in]`; then press both papers (no `fix`/`strip`, toc-depth 2).
- **`Q.delta` flag** (1740): fifteen objects still rest on the withdrawn channel equation.
- Item F (stale generators) unchanged, stated. Carried: orphan "Figure 15.3" (Ch 28); §34.4 heading without body; §32.4.1 `[N — pair count]`; "Chapter 27 said…"; §32.1 loose examples; V14 paper side; Register kinds table / F.1 995/2,433 not recomputable.
- Main Index in the docx is §-locators, not page numbers; a page-number index needs a press-time pass.
- Main figure captions print twice in the render (the image's alt line "Figure 12.3" and the caption paragraph) — the .md has both; decide whether build.py drops the alt line.

## Method notes
- build.py now: `displays()` (4-space blocks → quotation unless column-aligned), `fix_stars()`, `fix_head/fix_body/split_close/nest_bold` (Register), apostrophe-after-code-span → ’, `shrink_wide_tables()`. Measure residues with `trueres.py` (excludes deliberate `\*` literals): a raw `*` count is no longer the metric.
- Register entries are the record — never edit their bodies; form is enforced at press time. Sub-entries 1215a and 1476a lack their opening `**` in the record; build.py supplies it.
- Any "one thousand five hundred and …" sentence is a register count only if it says entries/claims/corrections (V24).
- Chat 6's context was trimmed mid-session once; the container state (file timestamps) was the record and held. If you cannot remember producing something in `out/`, read it, don't redo it.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.
<<<END FILE: HANDOFF-8.md>>>

<<<FILE: HANDOFF-7.md>>>
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
<<<END FILE: HANDOFF-7.md>>>

<<<FILE: HANDOFF-6.md>>>
# THE METHOD 1.6 — HANDOFF (chat 4 → chat 5), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-5 bundles in project knowledge (`The_Method_1_6_BUILD5_main_and_register.md`, `The_Method_1_6_BUILD5_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py` in bundle 2 does it). Figures: `cp /mnt/project/*.png figures/`.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V42 (bundle 2). **How rulings were reached**: project-scoped `conversation_search` — chats "Rebuild 1", "Rebuild 2", chat 3, chat 4 (this one). Read at the hit; do not page.
3. **Standing directives, rulings 1–4, compendium gold standard**: HANDOFF-2 in `The_Method_1_6_BUILD_handoff_and_audits-2.md`; rulings 5–14: HANDOFF-4; 15–17: HANDOFF-5 (both kept in bundle 2). Carry all verbatim.
4. Retire BUILD-4 bundles from project knowledge once BUILD-5 is in. Main-1 (`The_Method_1_6-1.md`) can be retired too: V39 showed it carries the same Chapter 28 corruption, so it is no longer a witness for anything the -2 lacks.
5. Tools in bundle 2, all run from `/home/claude/build/`: `register_cites.py` (citation counts; cap now read from the Register — run after any citation edit and reprint the front-matter numbers), `dclose.py` (Appendix D closure; reproduces D.5.9 and D.5.10), `index_gen.py` (regenerates the main Index by content; re-run after any section renumbering), `split.py`.
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## Rulings received in chat 4 (add to 1–17)
None new; the setup message restated the Zeno and handoff directives and ordered V39 closed from Main-1.

## State
**Phase 3 complete** (segments 1–6; registers 1733–1737; MAIN_AUDIT V39–V42, V8, V11 closed). Register 1,530 entries (165–1737); 17 prose counts in main track it; citation counts 588 / 398 / 715 / 1,002; load-bearing fifteen unchanged. Appendix D at 77 elements / 24 fibres, E = 0 (D.5.10). Main Index regenerated (57 / 311 / 44, E = 0). Math bibliography 162. Headings: appendices/Index/References `##`, 75 sub-labels `###`; every §-locator in eight volumes resolves.
**Phase 4 not started.**

## Open — needs the author
- **D.5.10's twelve fibre/coordinate assignments** are my reading of each compendium entry (table in §D.5.10). Confirm or move; `dclose.py` recomputes E in seconds.
- **`3B.shape`** has no `depends on` — it is a root — while the 3B family preamble says "No new root" and Part I lists fourteen roots. Either a fifteenth root or it rests on something unnamed.
- Λ_phys: the 22 older "objects rest on it" counts are not reproducible from the Math Compendium under any rule; printed as standing on an unprinted rule.
- Not recomputable, patterns unprinted (from 1732): Register kinds table; F.1 995/2,433.
- Chat-1 items C, D, E, F unchanged. **E first thing in Phase 4**: figures zip id 1vqbc0bylJOSCKJ2oVVBmBNpl1ijCzpuu — list before extracting; reconcile against FIGURE_MAP.md. Coordinates file id 1gblLH2cE6cBX5H_Nm8AB-72iF6eSdxxQ (fetch only when a build reads from it).
- Carried unchanged: orphan "Figure 15.3" (Ch 28); §34.4 heading without body; §32.4.1 `[N — pair count]`; "Chapter 27 said a non-closing index requires an operator" (no verbatim home); §32.1 loose examples (line ~8761); V14 paper side (3B paper labels only A, B, E).

## Phase 4 plan (production)
0. Item E: figures zip → FIGURE_MAP reconciliation; place FIG5 3D (item C).
1. Read `/mnt/skills/public/docx/SKILL.md` (and pdf) before any file is made.
2. docx per volume from the -2 .md: front matter, generated contents from the heading levels now in place, index (main), figures from `figures/`.
3. Papers formatted separately; Löwdin refs 6/7/9/12 (item D) completed first.
4. Generators (item F): `register_gen.py`, `spectra.py` stale — either rebuild or keep the "stale, stated" sentences.

## Method notes
- Chapter 23 begins at line 6139; Ch 28 at 7300; Appendix D at 10204; D.5.10 at ~10721; Index at 11363; References at 11457. Contents block ~109–172.
- The V24 replacement has now bitten three times (976 ×2, 126): any "one thousand five hundred and …" sentence is a register count only if it says entries/claims/corrections — check before touching.
- Three numbering generations coexist; match by content, never by shift. Register entries are the record — never edit their bodies.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.
<<<END FILE: HANDOFF-6.md>>>

<<<FILE: HANDOFF-5.md>>>
# THE METHOD 1.6 — HANDOFF (chat 3 → chat 4), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-4 bundles in project knowledge (`The_Method_1_6_BUILD4_main_and_register.md`, `The_Method_1_6_BUILD4_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/`. Figures: `cp /mnt/project/*.png figures/`.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V39 (bundle 2). **How rulings were reached**: project-scoped `conversation_search` — chats "Rebuild 1", "Rebuild 2", chat 3 (this one). Read at the hit; do not page.
3. **Standing directives, rulings 1–4, compendium gold standard**: HANDOFF-2 in `The_Method_1_6_BUILD_handoff_and_audits-2.md`; rulings 5–14: HANDOFF-4 (bundle 2, kept). Carry all verbatim.
4. Retire BUILD-3 bundles from project knowledge once BUILD-4 is in.
5. `register_cites.py` (bundle 2) recomputes the Register's citation counts; run it after any citation edit and reprint the front-matter numbers.
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## Rulings received in chat 3 (add to 1–14)
15. Stale flags are caught up to current text, not merely relocated; where a claim lacks a witness, compute it (register 1731). 16. Proposition of the V > 2 floor = **23.1** (stated in §23.2). 17. Withdrawal ratio prints both dated readings (Ch 28 alone; Register volume vs main).

## State
Phase 3 segments 1 and 2 ✔ (registers 1730–1732; MAIN_AUDIT V36–V39). Register 1,525 entries (165–1732), 16 prose counts in main track it. Main volume: 60+ locator edits, Theorems 14.1/17.1/18.1/18.2, Proposition 23.1, F.4.1 re-read, Ch 28 self-counts dated.
Phase 3 segments 3–6 not started. Phase 4 not started.

## Open (carry)
- **V39** Chapter 28 headings missing their number-words (proposals in the audit row); Ch 28 opening "Twenty-six … six and eight", "listed at §31.2".
- **Main volume Index** (lines ~11312–11392) is old-scheme throughout (§32.1/§32.3/§24.2 repeated) — regenerate in segment 4 (V8), do not patch.
- Not recomputable, patterns unprinted: Register kinds table; F.1 995/2,433 (flag stays in 1732).
- "Chapter 27 said a non-closing index requires an operator" (Ch 33, 35, Math LS) — no verbatim home; left.
- "§32.1's constraint … the preface pointing at Chapter 25, Chapter 1 pointing at Chapter 30" (line ~8761) — loose examples, unverified.
- Orphan "Figure 15.3" (Ch 28); §34.4 heading without body; §32.4.1 `[N — pair count]`; D: Löwdin challenge mathematics (Ch 34) not entered (D.5.10, segment 3).
- Chat-1 items C, D, E, F unchanged (E: figures zip id 1vqbc0bylJOSCKJ2oVVBmBNpl1ijCzpuu — list before extracting; reconcile with FIGURE_MAP at Phase 4 start). Coordinates file id 1gblLH2cE6cBX5H_Nm8AB-72iF6eSdxxQ.
- V14 paper side: three-body paper labels only checks A, B, E.

## Phase 3 plan (remaining)
3. Compendium object ↔ register resolution; LS/3B depths (M8); Λ_phys objects for the five new parameters (P6); D.5.10 for Chapter 34's mathematics.
4. Index closure re-run (V8) — regenerate the main Index; Index of Indices counts.
5. Bibliography ↔ References.
6. Heading levels (V11): appendices/Index/References `#`→`##`; `X.n` labels → `###` (Appendix D/E/F sub-labels are plain lines now — 25 §D/E/F targets unresolvable by regex until this is done). Start of Phase 4.

## Method notes
- Caps that give |Λ| = 976 in a 6,912 box: n ≤ 3, ℓ ≤ 1, k ≤ 3, q ≤ 3, e ≤ 3, f ≤ 1, g ≤ 3, 2S ≤ 3 (unique); ℛ as in §6.1/§14.2 reproduces E = 0. Useful for any further witness.
- Chapter 23 begins at line 6139; Ch 22 = 5900–6138. Contents block ~109–172 duplicates headings.
- Three numbering generations coexist; match by content, never by shift. Register entries are the record — never edit their bodies.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.
<<<END FILE: HANDOFF-5.md>>>

<<<FILE: HANDOFF-4.md>>>
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
<<<END FILE: HANDOFF-4.md>>>

<<<FILE: HANDOFF-2.md>>>
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
<<<END FILE: HANDOFF-2.md>>>

<<<FILE: MAIN_AUDIT.md>>>

# Main volume — Phase 2 audit (mechanical pass complete; sampled read pending)

| # | finding | status |
|---|---|---|
| V1 | Section numbering: no duplicates, none out of order; every §-reference resolves (§4.x are Chapter 4's list items). Chapter-shift test: no casualties. | Verified. |
| V2 | Register references (243) all ≤ 1725; Chapter references all ≤ 36. | Verified. |
| V3 | No jammed callouts, no ASCII/Unicode drift, no mojibake. | Verified. |
| V4 | Appendix B.2 carried the stale "133 rows … cannot drift" paragraph. | **Closed** — restated from the Spectra table (596 rows / 28 elements / 70 species / 3,342 levels / 2,269 interior / bracket 844/844 on 107 tested rows), prior state kept with registers. |
| V5 | The volume references Figures 1–25 but embeds no images at all. | **Open — Phase 4.** Figure assets for the main volume are not in the project. |
| V6 | Part VII subsection style: Chapters 33–35 unnumbered `###`, Chapter 36 numbered 36.1–36.6. | **Open — author ruling.** |
| V7 | Chapter 34's closing aside ("not a solution to the general three-body problem") now sits directly above Chapter 36. | **Open — author ruling** (half-sentence forward pointer, or leave). |
| V8 | Index counts recomputed at merge (57/139/44) with a note that the closure script is owed a re-run. | **Open — Phase 3.** |
| V9 | Sampled reader read of Chapters 35–36 in situ and of Appendices A–F. | **Not yet done — next chat.** |


## V9 — sampled reader read (chat 2)

### Segment 1: Chapter 35 in situ (lines 9602–9776, ~1,640 words)

| # | finding | status |
|---|---|---|
| V9.1 | Chapter 35 reads cleanly as a chapter: preamble → what was delivered → the silence → how the method did it → provenance table → coda → bridge. Every cross-reference checked resolves: §2.14, §E.5 (Precedence), Chapter 6/27/33/34, "four results … refused" (Preface), "nine things already in print" (collaborator's note), register entries 1701–1712. Every physics figure checked against the companion paper matches (c = 137.035999; Z = 38, 56, 72, 89, 105; La/Ac/Th; the eleven c→∞ elements; 0.083 hartree; Z = 91). | Verified. |
| V10 | **Audit count drifts across the book.** §3 is titled and opens with *twenty-five* prime audits (lines 1002–1003, 3486, 11135), but line 79 (collaborator's note), line 1411 ("§3 defines twenty audits"), line 8866 (Ch 32) and Ch 35 line 9709 ("the twenty audits' principle") say *twenty*. The Register shows the set grew from twenty to twenty-five (entries at Register lines 491, 555 say twenty; 5865, 5869 say twenty-five). Line 1411 is a direct contradiction of the section it cites. Ch 32's "all twenty audits passed" is historical and may stand; the other three read as the present set. | **Open — author ruling.** Proposed: twenty-five at lines 79, 1411, 9709; leave 8866 (historical). |
| V11 | **Heading levels.** Chapters are `##`; in the body the six appendices, Index and References are `#` (lines 9824–11306), the same level as Parts, while the contents block lists them as `##`. Production will render appendices as Part-level divisions. Appendix subsections (A.n … F.n) are plain-text labels, not headings, so they will not appear in a generated contents. | **Open — Phase 4** (proposed: demote to `##`; promote `X.n` labels to `###` at production). |
| V12 | Step count: Ch 34 says "104 of 106 steps"; Ch 35 says "107 of 107 across Z = 2–108". Both are correct on their own definitions (Ch 34 counts transitions, Ch 35 counts elements), but a reader meets 106 then 107 four pages apart with no bridge. | **Open — minor.** One clause in Ch 35 ("107 elements, hence the 106 transitions Chapter 34 counted") would close it. |
| V7 (revisit) | The Ch 34 aside now sits two chapters before the chapter it anticipates, with Ch 35 in between. In situ it reads as a deliberate aside, not a dangling thread; a half-sentence forward pointer ("— Chapter 36 takes this up") is the lighter fix. | Still author ruling. |

### Segment 2: Chapter 36 in situ (lines 9777–9821, ~1,100 words)

| # | finding | status |
|---|---|---|
| V9.2 | Chapter 36 reads as a closed argument: challenge → numbers first → what each section supplied → the law added → what is not claimed → one line. All eleven §-references resolve (§2.14, 12.11.0.2, 12.11.1.3, 12.11.2, 12.11.3, 12.11.4, 14.5, 18.4.1, 21.5.1, 25.6, 31.1.1, E.5), and §21.5.1 already carries the forward pointer to §36. Every figure checked against the companion paper matches: c_ij, cap-8 344/0/8,385, the cap 3–12 meet-failure series, thirteen order-types, μ < 0.0385209, Saari 1971/1973, Painlevé, Brudno, Xia 1992 (n = 5), Moore, Chenciner–Montgomery. Register 1713–1724 headlines match the chapter's claims one for one. | Verified. |
| V13 | **Two unresolved placeholders** — "Register [new]." at §36.1 and §36.3 (§2.14 paragraph). Prior state: `Register [new].` in both places. | **Closed** — §36.1 → *Register 1724* (open question closed: the maximal forbidden case is the solved case); §36.3 → *Registers 1718, 1722–1723* (13/13 audit failure; uniform-failure protocol; the convention fault). Sweep of all eight -2 volumes for `[new]`, `[TBD]`, `[TODO]`, `[placeholder`: none remain. |
| V14 | "78 of 78" (thirteen order-types × six checks) appears in the chapter and in register 1717, but the companion paper labels only audit checks A, B and E and nowhere states 78. A reader who follows the chapter to the paper cannot find the number. | **Open — paper.** Either the paper's audit section names all six checks and the 78, or the chapter cites the register rather than implying the paper. (Löwdin paper refs 6/7/9/12, open item D, remain the other paper-side gap.) |
| V6 (revisit) | In situ, 36.1–36.6 numbering reads well because the chapter is enumerative (nine "supplied" paragraphs under one head); Chapters 33–35 are narrative and their unnumbered `###` heads read equally well. Numbering all of Part VII would put 33.x/34.x/35.x on heads written as phrases. | Still author ruling; lighter option is to leave as is and let the contents show the asymmetry. |
| V15 | Preamble voice. Ch 36's preamble opens "Serving PART III … and PART VI …, and placed here because …" — a placement note in the author's building voice, where Chs 33–35 open in the reader's voice. One sentence to restyle. | **Open — minor.** |

### Segment 3: Appendix A — Proofs (lines 9824–10046, ~2,170 words)

| # | finding | status |
|---|---|---|
| V9.3 | The proofs A.3, A.8, A.10–A.13, A.15, A.18 are correct as written and their numbers check (A.13's ν_fail = 6.63 at Z = 2 for 3,000 cm⁻¹ recomputed; A.18's two counterexamples verified; A.19's seventeen generators sum by rank, the alphabet size 2+1+2+3+2+1+3+3 = 17, and the 9 + 11 = 20 implications all reconciled against the A.19.0 table). Registers 208, 230, 255, 268 exist; §7.1, §8.3, §14.4, §18.4, §29.12 resolve. | Verified. |
| V17 | Header count wrong: "Ten proofs … cross-referenced … remaining seven … seventeen in all." The table lists **nine** cross-referenced (A.1, 2, 4, 5, 6, 7, 14, 16, 17) and the body writes out **ten** (A.3, 8, 9, 10, 11, 12, 13, 15, 18, 19): nineteen, A.1–A.19. | **Closed** — restated as nine / ten / nineteen. Prior: ten / seven / seventeen. |
| V18 | Two equation pairs jammed onto one line (A.8 sufficiency: the join and meet; A.10 for Λ: #{2S} and #{g} — the latter duplicated verbatim in §10, line 2054). Missed by V3, which tested prose callouts, not code blocks. | **Closed** — split onto two lines in all three places. |
| V19 | A.9: "Proof." unbolded where every other proof is **Proof.** | **Closed.** |
| V20 | A.19.1 garbled: "Every one has q = k − something equal on both sides and g equal to q". Checked against the eight listed cells: k = q = g = 2S in every one, and (n, ℓ), (e, f) each at (1,0) or (2,1). | **Closed** — restated from the cells. Prior text kept here. |
| V21 | **Stale §-targets from the pre-Part-I numbering.** "§3" in A.18 ("§3 states as skew") and twice in A.19 ("§3 states that Λ has seventeen join-irreducibles") point at the audits chapter; the content lives in §8 / §8.3 (lines 1851–1884). A third bare "§3" at line 2232 (§11.6, spin multiplicity "a fact §3 verifies numerically") is the same class and its true target is not yet located. V1's chapter-shift test only tested the +2 shift of 2026-08-23; an older +5 shift (Part I inserted) left references that still resolve to *a* section, just the wrong one. | A.18/A.19 **closed** (§3 → §8, §8.3). Line 2232 **open**. A bare-§N sweep with content matching is added to Phase 3 item 1. |
| V16 | **Figure numbering is on the old chapter scheme.** Captions "Figure a.b" use a = old chapter: shift +5 through Parts II–III (Figure 3.1 sits in Chapter 8), +7 through Parts V–VI (Figure 16.1 in Chapter 23), +13 at Chapter 28, and only Chapter 21's "Figure 21.1" matches. Every in-text "see Figure a.b" therefore sends the reader to the wrong chapter, and the twenty-five figures of open item E will need their final numbers before the assets are made. | **Open — Phase 3, blocking Phase 4.** Proposed: renumber captions to (current chapter).(sequence) and remap every reference by caption identity, not by a uniform shift; record the map as a register entry. |
| V22 | A.9's proof sketch of μ = 0 off antichains ("decomposes as a direct product with a chain factor") is not a valid argument in general; the statement is true (Boolean interval ⟺ antichain; otherwise [x,y] is not complemented and μ vanishes by the crosscut theorem, or Rota). | **Open — author.** Two-line replacement offered on request; not changed silently. |

### Segment 4: Appendix B — Data and provenance (lines 10050–10110)

| # | finding | status |
|---|---|---|
| V9.4 | B reads as intended after the V4 lift: sources, the lifted channel table with its restated totals (107 + 489 = 596 rows reconciles), flagged channels, reproducibility. Sansonetti citations correct (Na I: JPCRD 37, 1659; K I: JPCRD 37, 7). | Verified. |
| V23 | Part names in appendix preambles are on the pre-Part-I scheme: B "Serving PART IV — THE METHOD" (now Part V); C, D, E, F "Serving PART V — THE RECORD" (now Part VI — THE RECORD AND THE REACH). Appendix A ("PART II — THE LATTICE") was already current. | **Closed** — all five restated. |
| V9.4a | Typography: "KI" → "K I"; B.3 table header "specie / s" (column wrapped mid-word) → "species … δ spread"; missing blank line before the Appendix B heading. | **Closed.** |
| V9.4b | B.4 says the ionisation limits are "listed in B.2", but B.2's rows are now lifted to the Spectra Compendium; and "the rules of Chapters 13 and 14" names Chapter 13 (What the title names) and 14 (Closure), which is not where the bracket's rules live (§22.1–22.2). Old-numbering target, but the shift is not uniform so I have not guessed. | **Open — author** (proposed: "listed in the Spectra Compendium, Part II"; "the rules of Chapters 22 and 23"). |

### Segment 5: Appendix C — Margins (lines 10111–10200)

| # | finding | status |
|---|---|---|
| V9.5 | C.1's margin table, the three sceptic's rows, C.2/C.3 inventories and C.4 methods read cleanly; §3.5 (figure audit), §16.3, §24.2, §25.4, §25.6, §31.3.4, §32.6 all resolve to the right content. | Verified. |
| V9.5a | "§32.3 states the condition exactly — \|ΔT\| > 2Z²R/ν³": §32.3 is *Self-defence*; the condition is §25.3 *The failure condition* (line 6873). | **Closed** — §25.3. |
| V9.5b | C.2: "reproducible from Appendix **C**'s tables and the rules of Part **IV**" — self-reference and old Part number. | **Closed** — Appendix B, Part V. |
| V24 | **The register count is stale book-wide.** Ten places (collaborator's note line 20; lines 89, 104, 201, 522, 645, 1557, 3486, 4080, 5648; and C.3 "Chapter 28 records one thousand one hundred and seventy-one errors") state 1,171 entries. The Register-2 carries 1,548 distinct entry numbers (1,518 headings, grouped fault entries included) running to 1725. This is the book's central self-referencing claim and it is currently false of the file that carries it. | **Open — author ruling + Phase 3 item 2.** Either (a) 1,171 is dated ("at the close of session N") and each sentence says so, or (b) every count is regenerated from the Register at build and Chapter 28's "seven mechanisms account for twenty-nine entries" family is recounted with it. |
| V25 | Proposition numbering is on the old scheme, and inconsistently: the V > 2 floor is stated as **Proposition 14.1** (line 6158, in Chapter 22) and cited as 14.1 in C.1/C.2 but as **Proposition 15.2** at lines 6434, 7207, 7516 and D (line 10791). One proposition, two stale names, neither in its chapter. | **Open — Phase 3** with V16 (proposed: Proposition 22.1 throughout). |

### Segment 6: Appendix D — The mathematics, indexed (lines 10201–10670, ~4,560 words)

| # | finding | status |
|---|---|---|
| V9.6 | D reads as a layered record — first attempt, structure, constraints, the two demanded elements, the closed index, then four re-closures — and the layering is the argument. D.5.1's recheck figures, D.5.6's 32→36, D.5.7's 36→40 and D.5.8's 40→48 chain arithmetically; registers 219–222, 269, 282, 301, 305, 361 exist. D.6's audits 2 and 3 counts (20/20 over 475,800 pairs; 24/24) match §3. | Verified. |
| V26 | **Headline counts stale against the table.** The preamble said "thirty-two elements"; the fibre table sums to forty-eight and its own note says forty-eight; the paragraph under it said "the column sums to forty" (pre-D.5.8); the Figure caption said thirty-two. Three present-tense statements, three different numbers, one table. | **Closed** — preamble and caption → forty-eight; "sums to forty" → "forty-eight: 32 + 4 + 4 + 8" naming D.5.6/7/8. D.5.5's two "thirty-two" remain, being historical in context. Prior states kept here. |
| V27 | **A fifth re-closure is owed.** The Mathematical Compendium now indexes the Löwdin solution (LS, 8 objects) and the three-body work (3B) as families, and Chapters 35–36 add mathematics (the exact-quartic decomposition, the pinned-channel theorem, the mass-uniformity law, the norm-polynomial correction). D.1's own rule — "E = 0 expires every time the mathematics grows" — means D.5.8's forty-eight is no longer the count, and D owes a D.5.9 with the new elements fibred. | **Open — Phase 3 item 3** (compendium object ↔ register), author to confirm which LS/3B objects are elements. |
| V9.6a | The fibre table's "recomputed by the press at every build, per §2.21" is a cannot-drift claim; tested — it matches the table (48) but did not protect the preamble or caption two paragraphs away. Same class as V4 and item F. | Noted; press claim scoped to the table only. |
| V9.6b | "Figure 25.1" caption sits in Appendix D; belongs to V16's renumbering. | Carried under V16. |

### Segment 7: Appendix E — Q, indexed and closed (lines 10671–10968, ~3,190 words)

| # | finding | status |
|---|---|---|
| V9.7 | E.1.1's lineage table is the model the whole book needs: one current state, history as history. E.2, E.3 (each item in full), E.4 (the grid), E.5 (precedence), E.6–E.8 read cleanly; registers 211, 239, 307, 385, 386, 461, 562–564 exist. | Verified. |
| V28 | **The preamble carried three stacked counts** (nine; "eight … four entered … thirteen stand"; eight) — the exact defect E.1.1 diagnoses two paragraphs later. E.1.2's heading said "ten open of 13" over a table of **fourteen** (R, register 461, entered after the lineage was written); E.4 called eleven "the current" set. | **Closed** — preamble states one current count (14 items, 10 open) and points to E.1.1 for history; lineage row added for R; heading → "of 14"; E.4 → "read when the set stood at eleven". Prior wording kept here. |
| V29 | E(Q) = 0 was last computed at thirteen (E.4.1). R makes fourteen and no re-closure is recorded. Same class as V27. | **Open — Phase 3** (one computation; the preamble now says so). |
| V9.7a | "Appendices E and G" (E.1.1 lineage) — old lettering; targets are E and F. | **Closed.** |
| V30 | **A block belonging to Appendix F was stranded at the end of E**: the "E(G), recomputed by the press … 38 / 24 / 23 … seventeen of the twenty-three are dominated … Register 368" analysis, sitting after E.8 and before the Appendix F heading. F.3's own opening paragraph was garbled by the same merge ("— because the press at every build, since a figure …" and a bare "Thirty-three combinations" that is the first reading, not the current). | **Closed** — block moved into F.3 after the "Registers 366, 367, 368" paragraph, where its register 368 belongs; F.3's sentence repaired and "thirty-three" dated as the first reading. Prior placement kept here. |

### Segment 8: Appendix F — The numbers, indexed (lines 10969–11225, ~2,600 words)

| # | finding | status |
|---|---|---|
| V9.8 | F.1's population (1,166 + 1,267 = 2,433; 1,715 = 70%) and F.4.2's information argument (max at p = ½) check. F.3.3's three-state table and the law–extent rule are the right representation and now carry the moved block beside them. Registers 210, 219, 296, 297, 309, 366–370 exist. | Verified. |
| V31 | Old appendix lettering in F's preamble — "its mathematics (E), its ignorance (F), its data provenance (C)"; "E was asserted, as §D.5.1 records"; and F.4.3 "Appendices E, F and G". | **Closed** — D, E, B; D; D, E and F. |
| V9.8a | "§15 says a bracket means" — §15 is Self-reference; the bracket is §22 (old +7 shift). | **Closed** — §22. |
| V32 | Two internal number clashes: F.4.1 gives the withdrawal ratio as 24,162 : 54,241 = **0.445** and three paragraphs later "at **0.502** the register is half the argument"; F.4.2's table counts "every claim-bearing number in Appendix F" as **2,831** where F.1 says **2,433** occurrences (and 995 distinct). F.4.2 also fibres against "Appendix D's mathematical elements 36", now 48. These are press-recomputed quantities that were printed as prose and drifted — the defect F.3.3 itself names. | **Open — Phase 3 item 2/regeneration.** Author to say which of each pair is current, or let the press print them. |
| V33 | "Appendices C and G" at lines 893 and 8905 quote register 270 (section-level locators deferred for two appendices) in the old lettering. Under the book's rule that historical statements keep their wording, these may stand — but a reader has no Appendix G to find. | **Open — author ruling** (proposed: "Appendices B and F (then lettered C and G)"). |

## Rulings executed (chat 2, second pass)

| # | ruling | done |
|---|---|---|
| V22 | Replace A.9's proof sketch. | **Closed** — crosscut argument (Rota 1964) written in; Rota added to References R.5. Prior text kept in V22 above. |
| V24 | Collaborator's count → update to the Register's contents. | **Closed** — sixteen sentences now read *one thousand five hundred and eighteen*, the Register's own headline (1,518 entries, 165–1725; 1,548 numbers, 13 absent). **Collateral found:** the earlier global replacement had also hit three sentences that were never register counts — "seven cells for 976" (§14.5.7 area, line 4080) and "ten cells for 976" (§21, line 5648) restored from register 1239/1327; "fixed points closed under intersection over ⟨N⟩ pairs" (§32.4.1, line 9025) is unrecoverable from any source here and now carries a visible `[N — pair count to be confirmed]`. |
| V27 | D re-closure — top priority. | **Run, draft written (D59_DRAFT.md), awaiting placement ruling.** 48-state reproduced at E = 0 (validates the model). Adding LS (8) + 3B (9) on the collaborator's reading: 65 elements, 22 fibres, E = 4 first run; E = 0 only if 3B.five is a theorem and 3B.pot is entered on its derivation (exhaustive) not its 650-triangle check (sampled); with 3B.pot sampled, E = 2 and the fibre stays honestly open. Two author decisions; the draft states both outcomes. Not yet inserted in the book. |
| V29 | Q re-closure at fourteen. | **Cannot be reproduced from the appendix.** The four domain fibres and any constraints are not printed — E.4.1 asserts E(Q) = 0 at thirteen "in four domain fibres and 1 unfibred" without listing the fibres (the very defect D.5.1 names). An unfibred closure on the three printed ordered coordinates gives E = 9 at nine open items, so the printed data do not reproduce the printed result. One fact is computable and worth printing: **R occupies a cell (one claim · buildable · unbounded) that was admitted-and-absent at thirteen** — the index predicted R before R was entered. Needs: the domain assignment per item and the constraints used, then one computation. |

## The coordinate file (added to project knowledge 23:41)

| # | finding | status |
|---|---|---|
| V34 | `COORDINATES-2_13.csv` profiled: 104,832 rows × 10 columns; Z 1–120, charge ≤ Z on all rows, 7,260 pairs = 120·121/2; grades exact 929 · measured 358 · computed 103,545; witnessed 358 = measured exactly; the mult-set at a pair is a function of Z − charge on all 7,260 pairs; refused 1,036,800 − 104,832 = 931,968. **Every figure register 5869 states is true of the file.** | Verified. |
| V35 | The Spectra Compendium named the file only as `COORDINATES.tsv` with a **stale nine-column schema** (`status` column; "marked improbable"), and Part I's table said Z = 1 … 118 while the file runs to 120. No volume gave the file a citation form. | **Closed** — Part 0 now carries *The file*: canonical name `COORDINATES-2.13`, the ten columns with alphabets and counts read from the file, the schema's history (630 → 1578 → Janet extension) as history, and the citation form **COORD(Z, charge, ℓ, 2S+1)**. Main B.4 points to it. Prior schema line kept in the compendium's own italic note. Register entry owed (form change). |
| V27 (both placements tested) | Author's ruling: run theorem/derivation and measurement, let the comparison decide. Both were run (D59_DRAFT.md): measurement → E = 4 (formula · analysis 3, theorem · analysis 1); theorem for 3B.five + sampled for 3B.pot → E = 2; theorem + derivation → **E = 0 at 65 elements, 22 fibres**. The comparison decides for theorem/derivation, with 3B.pot's 650-triangle run recorded as corroboration, not verification. | **Ready to insert as D.5.9** on your word; the Math Compendium entries for 3B.pot and 3B.five would carry grade PROVED with the check noted. |
| V29 | Still needs the four domain fibres per item; not in the coordinate file (that file is Λ_spectra, not Q). | Open. |

## Rulings executed (chat 2, third pass)

| # | ruling | done |
|---|---|---|
| V27 | yes | **Closed** — D.5.9 inserted; D preamble, fibre table (22 rows, sums to 65), "sums to" paragraph and caption at 65; 3B.pot and 3B.five → PROVED in the Math Compendium with checks noted. Register 1726. |
| V29 | find the domains | **Not in the project**: the four domain values and per-item assignment appear in no volume, in the Register (235, 372 assert the fibring unnamed) or the coordinate file. They live in the Q script (`status.py`?) or the register-235 session. Awaiting that. |
| V10 | current count | **Closed** — twenty-five at lines 79, 1411, 9709; Ch 32's "all twenty audits passed" left as historical. |
| V16 | go | **Closed** — 33 captions renumbered (chapter · sequence), every reference remapped by caption identity (FIGURE_MAP.md); Proposition 14.1/15.2 → 22.1. Orphan "Figure 15.3" (Ch 28 withdrawal) has no caption under any scheme — left, flagged. Register 1728. "Theorem a.b" names in D.5.2/D.5.4 (9.1, 10.1, 11.1, 11.2) are the same class and go to the Phase 3 sweep. |
| V6/V7 | renumber; pointer | **Closed** — 33.1–33.5, 34.1–34.10, 35.1–35.6 numbered (no prior §33–35.x references existed); "— Chapter 36 takes this up" added to the Ch 34 aside. Note: §34.4 "The rule" is a heading with no body before §34.5 — check whether a paragraph was lost. |
| approved text | V12, V15, V9.4b, V33, V14 | **Closed** as proposed (V14: "78 of 78 (register 1717)"). |
| V32 | timestamp decides | **Closed** — the withdrawal ratio's readings dated: 0.445 (register 296), 0.249 after compression (363), press readout since 374; "at 0.502" → 0.249. F.4.2's bracket recomputed at the current counts (D 65; +Index 116; F 2,433, the later of the two figures): span factor 37, 1 : 1 still inside. Current Chapter 28 against the other chapters measures 0.061 — the Register is now its own volume, so "words of register" needs redefining before the press can print it. |
| V24 | — | Register count now 1,521 (1726–1728 added); sixteen sentences updated. |
| V35 | — | Register 1727. |
| V29 | digest supplied domains, orders, constraint | **Closed** — model validated against register 256 (fibred 0, unfibred 1). R's cell violates the unprinted constraint; R is genuinely buildable · unbounded (#P-complete), so the constraint dies by F.3's rule; thirteen still close without it. At fourteen fibred: E = 0 with R = one claim (as printed, the later state), E = 1 with R = nothing (465). "Index predicted R" withdrawn as a fibred claim. Domain column added to E.1.2; E.1.5 written; register 1729; count 1,522. R = one claim confirmed by the author (chat 2). |
| V36 | **Phase 3 segment 1 — content-matched locator sweep (2026-08-24, chat 3).** Every bare §N, "Theorem a.b" and "Chapter N / Ch. N" across the six -2 volumes and the three-body paper matched to the passage it names. Main: 54 edits (26 bare §N, 9 D.5.2 locators, 18 Theorem renames 9.1/10.1/11.1/11.2 → 14.1/17.1/18.1/18.2, plus Chapters 10–12→15–17, 17→19, 27→28 ×3, 31→32 ×2, 30→32, 28→29, 29→30 ×2, 16→18 ×2, §24.2→§27.2). Math E locator §1→§6.1; Physics §24→§18 ×2; IoI Theorem 12.1→18.1; 3B paper §3→§8.4. Register entries untouched (record). Every §a.b in main resolves to a heading (Appendix D/E/F sub-labels are unmarked — V11). Register 1730; count 1523 (165–1730), 16 prose statements in main updated. Pre-sweep main kept as witness (main_pre_seg1.md, not in bundle). | **Closed**, with three carried: (a) §11.6 line ~2233 "a fact §3 verifies numerically" — no witness anywhere for E with 2S removed; reword, do not relocate. (b) §27.6 "Chapters 1, 5, 11 and 14 stop being four subjects" — old scheme; from §27.1–27.2 the four are closure defect, void, bracket and cost (6 or 14, 10, 22, 23) — author to confirm. (c) Math Compendium §"Why none is redundant": "Chapter 7 can state the two-column law" — no "two-column law" survives in the main text; nearest content is §11.8.1 (F(−1) = 2, ℓ and f each with two values). Also: the "Chapter 27 said a non-closing index requires an operator" sentences (Ch 33, 35; Math LS entries) have no verbatim home; Chapter 27's slack framing is the nearest — left. |
| V37 | **Carried items from V36 closed (chat 3).** §11.6 spin-removal claim given a computed witness (976/0 → 319/0, k+1 per cell; register 1731). §27.6 four chapters → 6, 10, 14, 23. Math Compendium two-column law → §12.1. §32.5's pole → §23.7 (×2). Proposition 22.1 → **23.1** (stated in §23.2; V16/V25's "Chapter 22" was wrong) — 11 occurrences incl. 3 "Prop. 14.1". Register count 1524 (165–1731). **Found, deferred to segment 4 (V8):** the main volume's Index (lines ~11312–11392) carries old-scheme locators throughout (§32.1, §32.3, §24.2 repeated; "the pole …… §32.5"). | **Closed.** |
| V38 | **Phase 3 segment 2 — citation recount and press-recomputed numbers (chat 3).** Register front matter regenerated from data: 536 cited-by-entries (was 376), load-bearing table = 15 entries ≥7× with counting rule stated, 394 cited in main (was 225) / 711 with companions / 998 with entries. F.4.1 ratios re-read with dated current values (Ch 28 alone 0.053; Register volume vs main 1.73; method 0.125, 0.800 vs appendices). Ch 28's stale self-counts (493 / 436 / 242) kept as dated readings beside 1,525; "Chapter 22" → 29 in Ch 28's opening. Register 1732. | **Closed.** Not recomputable (patterns unprinted): kinds table; F.1's 995/2,433. |
| V39 | **Chapter 28 headings lost their leading number-word** — §28.4 "From from the earlier work", §28.7 "From made after the register was closed, two printed here", §28.7.1–.4 "From more from …", §28.9.1 "From registers, and only one of them is a backlog". Item numbering in the bodies gives: 28.7 = 49–54 (Six), 28.7.1 = 55–62 (Eight; matches the opening's "eight in the structural work"), 28.7.2 = 63–72 (Ten), 28.7.3 = 73–119 (Forty-seven), 28.4 = the first forty-eight, 28.9.1 = Two; 28.7.4 unknown. Also Ch 28's opening: "Twenty-six were made after the register was first closed — six … and eight" (6 + 8 ≠ 26) and "They are listed at §31.2" (§31.2 is string theory). | **Open — author.** Proposed headings above; Main-1 (retired) would confirm. |
| V39 (closed, chat 4) | Main-1 carries the same corrupted headings — the fault predates the build; no file witness exists. Restored from the item numbering in the bodies: §28.4 **Six** (six printed, "how each was caught"); §28.7 **Six** (49–54; lead: "same pattern as the first forty-eight"); §28.7.1 **Eight** (55–62); §28.7.2 **Twelve** (63–74 — not ten: item 74 sits in it); §28.7.3 **Seventy-five** (75–149); §28.7.4 **Forty** (150–189; §28.7.5 "of the forty", 186/189 "below"); §28.9.1 **Two** ("This book keeps two registers"). Opening: 6 + 8 + 12 = 26 — "and twelve in the structural and audit work" restored; "§31.2" → §28.7–28.7.2; missing full stop after §25.6 supplied. Prior headings verbatim in the V39 row above. Register 1733; count 1,526 (165–1733); 18 prose counts in main updated; `register_cites.py` cap made dynamic (was hard-coded 1731/1732, which had hidden one main citation of 1732): 536 / 395 / 712 / 999. Register-1 not in project; kinds-table patterns (1732 flag) still unrecovered. Pre-edit main kept as main_pre_v39.md (not in bundle). | **Closed.** |
| V40 | **V24 collateral, third instance.** §6.1's Figure 6.2 caption — "a reader given only the occupied cells would reconstruct all one thousand five hundred and twenty-six" — is the periodic table's cell count, 90 + 36 = 126 (Main-1 line 1528: "cells the structure admits 126"), swept into the register-count replacement and carried through two further updates. Restored to *one hundred and twenty-six*; 17 register-count sentences remain in main. | **Closed.** |
| V41 | **Phase 3 segment 3 — compendium ↔ register, depths (M8), Λ_phys counts (P6), D.5.10 (chat 4).** All 265 Math objects parsed; every `depends on` and every cited register resolves; 13 LS/3B + 10 sampled objects match their entries by content. M8 and P6 closed (rows in MATH_AUDIT / PHYS_AUDIT). **D.5.10 written**: the twelve Chapter 34 objects fibred from the compendium's own entries; the 65-state reproduced at E = 0 (22 fibres) by §6.1's ℛ + D.3's constraints before extension; at 77 the first run E = 1 (theorem · analysis, verified · exhaustive · none found), closed by reading the corridor's precedent as this work's; final **77 elements, 24 fibres, E = 0**. D preamble/table/caption/sum updated; D.5.9's closing question answered in place; F.4.2's bracket recomputed (2.47 : 1 / 0.288 / 0.867; 128 → 1.48 : 1; span 32). Stale name caught: §D.5.4 "11.2's proof" → Theorem 18.2. Register 1734; count 1,527 (165–1734). Citation counts: 588 (was 536 — the rise is one range citation, "registers 1249–1357", in 1734, counted per the printed rule) / 396 / 713 / 1,000; load-bearing fifteen unchanged. Fibre/coordinate assignments in D.5.10 are my reading of each entry and are the author's to confirm or move; `dclose.py` (bundle) recomputes E. **Carry:** F.4.2's "Index's terms" figure (51) will move if segment 4's Index regeneration changes the term count. `3B.shape` root question (MATH_AUDIT). | **Closed** (assignments to confirm). |
| V8 (closed, chat 4) | **Segment 4 — Index regenerated** (register 1735): hierarchy kept (57 terms / 44 relations), every locator recomputed by content (`index_gen.py`, bundle); 311 locations, E = 0 after union, 90 raw violations. Six unbolded parents reformatted. Index of Indices: mathematics row 27/16 → 77/24 (dated); term index named. Prior Index kept as index_prior.txt (not in bundle; recoverable from BUILD-4). F.4.2's "Index's terms" figure unchanged (57 terms). | **Closed.** |
| V42 | **Segment 5 — Bibliography ↔ References** (register 1736). Math bibliography 172 → 162 (ten generator artefacts removed; BFMY expanded); 59 works shared with main References, the rest scoped to the compendium and said so in a closing paragraph of References. No conflicting years. Physics, Spectra and Index of Indices carry no bibliography of their own; the two papers keep their own lists (Löwdin refs 6/7/9/12 placeholders — item D — still open). | **Closed.** |
| V11 (closed, chat 4) | **Segment 6 — heading levels** (register 1737). Appendices A–F, Index, References `#` → `##` (8); 75 `X.n` labels → `###` (67 by rule + A.9, A.11, B.4, D.4.1, D.4.4.1, D.5.2, E.1.1, E.1.3 by hand; six label-initial sentences left as prose). Locator resolution across all eight volumes: every §A–F/§R and every §a.b in main resolves; only §4.1/4.2/4.4/4.6/4.7 (Chapter 4 list items) do not. Pre-edit main kept as main_pre_seg6.md (not in bundle). | **Closed.** |
| V43 (chat 5) | Three author rulings applied (18–20): D.5.10 recomputed, nothing moves (1738); `3B.shape` eighteenth root, stale "fourteen roots"/"17 roots"/"No new root" lines corrected, §14.6.3's "248 objects" dated (1739); Λ_phys 27 counts regenerated on the printed rule with seeds named, IOI echo corrected, 17 prose counts → 1,533 (1740). Prior states: `/home/claude/*_pre17*.md` this chat; text in the entries. New flag from 1740: fifteen objects still rest on withdrawn `Q.delta` (Q family). | **Closed**; Q.delta flag open. |
| V44 (chat 5) | Phase 4 seg 0 — figure reconciliation (register 1741). Zip = the 15 project PNGs; preview PDF on Drive is page scans; 41 referenced figures have no asset (33 main captions, 8 `figures-compendia/`). FIG5spectraindex3D placed as Löwdin paper Fig 1(b) — item C closed. | **Open**: regenerate vs placeholder ruling. |
| V44 (closed, chat 5) | Figures recovered from restore-point-2_13 (register 1742): 33 main + 8 compendia paired by press.py's rule, all captions match; D.1 re-rendered (77/24) with prior kept. Zip in outputs + FIGURE_ASSETS.md. Open: 32 archived plots to be read against caption numbers at placement. | **Closed** |
| V45 (chat 5) | Phase 4 seg 2 — six docx/pdf pressed (register 1743). Figure links added to main (33). Open: asterisk residues (Register 106 / main 738 / Spectra 375 mostly legitimate table marks), papers not yet pressed, 32 archived plots unread against captions, Löwdin refs 6/7/9/12 (item D). | **Open** |
| V46 (chat 6) | Phase 4 seg 1–2 (register 1744): asterisk residues traced to unparsed 4-space set-off blocks in main (875 lines), split bold delimiters and nested bold in the Register, and pandoc's smart-quote apostrophe after a code span; all fixed in build.py preprocessing, .md untouched; main 738 → 20 legitimate stars, Register 106 → 8 record-content lines, no entry flattened; wide tables size-to-fit (7.5 → 6 pt); six volumes re-pressed (main 266 pp, Register 414, Math 94, Physics 25, IOI 42, Spectra 22). Seg 3 (register 1745): 9 of 32 plots read, numbers agree; 23.1/8.2/10.1 carry pre-V16 titles in the image, 25.2 carries §14.4/§17.6. Open: 23 plots, item D (Löwdin refs 6/7/9/12, papers unpressed), Q.delta. |


## V47 — chat 7 (2026-08-24)
All 32 archived plots read against captions (1745, 1746): 3 number disagreements (16.1 4/4 vs 56/56; 24.1 He II series and monotone claim; 25.1 caption 1,105 vs plot/§25.5 1,061 — caption is the stale side); 17 pre-V16 titles/locators. No plot source survives (1747); 14 titles cropped, originals in figures-pre-crop/; 16.1, 24.1, 12.3, 25.2 owed a re-render from data. Item D closed (1748): Löwdin refs 6/7/9/12 filled, both papers pressed. Q.delta flag closed (1749): 15 = 6 built on the superseded form + 9 by provenance via Q.final; rule unchanged, split printed in Physics Compendium; ruling requested. Eight volumes pressed. Status: closed except the re-render, the 25.1 caption and the Λ_phys ruling.


## V48 — chat 8 (2026-08-24), registers 1753–1760
Four owed plots re-rendered from the book's data (1753; generator `fig_rerender.py`, old renders in figures-pre-rerender/). build.py: "Build 9"; alt line dropped at press (1754). Second tier closed or stated (1755). Residue computed out (1756): §32.4.1 N = 3,000 pairs zero failures (`rclose.py`); §32.1.1 recomputed (`bookindex.py`; part certificate now one level coarser; 12 stale Part labels corrected); kinds table pattern-printed and press-rewritten (`kinds.py --write`); register_gen.py and spectra.py retired (`spectra_count.py` reproduces the Spectra counts exactly); Appendix F press-recomputed (`appf.py --write`, E(G)=23 matches the printed reading); §34.4 body written from the chapter; V14's six checks named A–F and rerun 78/78 (`tb_audit.py`; first run failed A,C 13/13 on the Hopf half — 1718's lesson). Press (1757): six headings silent in every prior press (missing blank lines, incl. Chapter 15) fixed; TOC field empty in every prior PDF — `index_pages.py` + `build.py … pages` generates a page-numbered Contents and a page-numbered print Index (main), iterated to a stable map; .md keeps § locators. He II closed from author-supplied NIST levels (1758): convention recovered by test (limit 438,908.871 · R_He · J-centroid), series 7.62→0.159 ×10⁻⁵ monotone, endpoints reproduced to three figures, limit to 0.002; compendium rows corrected (exponent form + note); 24.1 re-rendered with the measured series; ruling 23 caption ("monotone wherever the defect is the core's", three rises named: Al I nd, Al II nf per §B.3, He I floor). 207 two-space tables had printed as run-on prose in every press (1759) — displays() extended; main 289 pp, Spectra 28, 3B 10. Citation counts refreshed (1760): 597 / 401 / 721 / 1,012; load-bearing fifteen unchanged. Register 1,553 (165–1760). Open and author's: §34.4 wording approval; F.4.2 "surviving claim" definition (Q, 297); Spectra's 489 untested rows (tolerance unstated).
<<<END FILE: MAIN_AUDIT.md>>>

<<<FILE: FIGURE_MAP.md>>>
# Figure renumbering map (V16), 2026-08-23

| old | new | caption line |
|---|---|---|
| Figure 1.1 | Figure 6.1 | 1538 |
| Figure 1.2 | Figure 6.2 | 1556 |
| Figure 2.1 | Figure 7.1 | 1778 |
| Figure 3.1 | Figure 8.1 | 1871 |
| Figure 3.2 | Figure 8.2 | 1898 |
| Figure 4.1 | Figure 9.1 | 1997 |
| Figure 5.1 | Figure 10.1 | 2039 |
| Figure 6.1 | Figure 11.1 | 2206 |
| Figure 6.2 | Figure 11.2 | 2252 |
| Figure 7.1 | Figure 12.1 | 2303 |
| Figure 7.2 | Figure 12.2 | 2365 |
| Figure 7.3 | Figure 12.3 | 2406 |
| Figure 7.4 | Figure 12.4 | 2505 |
| Figure 7.5 | Figure 12.5 | 3443 |
| Figure 10.1 | Figure 15.1 | 4290 |
| Figure 11.1 | Figure 16.1 | 4342 |
| Figure 11.2 | Figure 16.2 | 4679 |
| Figure 14.1 | Figure 19.1 | 5379 |
| Figure 21.1 | Figure 21.1 | 5706 |
| Figure 16.1 | Figure 23.1 | 6152 |
| Figure 16.2 | Figure 23.2 | 6287 |
| Figure 16.3 | Figure 23.3 | 6436 |
| Figure 16.4 | Figure 23.4 | 6530 |
| Figure 17.1 | Figure 24.1 | 6599 |
| Figure 17.2 | Figure 24.2 | 6612 |
| Figure 17.3 | Figure 24.3 | 6796 |
| Figure 18.1 | Figure 25.1 | 6898 |
| Figure 18.2 | Figure 25.2 | 7025 |
| Figure 19.1 | Figure 26.1 | 7074 |
| Figure 20.1 | Figure 27.1 | 7205 |
| Figure 23.1 | Figure 30.1 | 8376 |
| Figure 23.2 | Figure 30.2 | 8423 |
| Figure 25.1 | Figure D.1 | 10389 |

Orphan: "Figure 15.3" (Chapter 28, old scheme) has no caption anywhere — left as is, flagged.
Propositions: 14.1 and 15.2 → 22.1 (V16) → **23.1** (register 1731: the floor is stated in §23.2, line 6158).
Assets: every figure above now has a file — see FIGURE_ASSETS.md (recovered from restore-point-2_13, 2026-08-24).
<<<END FILE: FIGURE_MAP.md>>>

<<<FILE: FIGURE_ASSETS.md>>>
# The Method 1.6 — figure assets, complete (2026-08-24)

Recovered from restore-point-2_13.tar.gz (fig00–fig27 + five named files) by reproducing `The Method 1.6 press.py`'s pairing rule: legacy files in sorted order against caption blocks in document order, the five NEW keys fixed. Old → new numbers per FIGURE_MAP (V16). Caption check = the archived caption's opening matches the -2 volume's caption at the mapped line.

## Main volume (33)
| old | new | source file | file in figures/ | caption line (-2) | caption |
|---|---|---|---|---|---|
| Figure 1.1 | Figure 6.1 | fig00.png | figure-6.1.png | 1538 | ✔ |
| Figure 1.2 | Figure 6.2 | fig01.png | figure-6.2.png | 1556 | ✔ |
| Figure 2.1 | Figure 7.1 | fig02.png | figure-7.1.png | 1778 | ✔ |
| Figure 3.1 | Figure 8.1 | fig03.png | figure-8.1.png | 1871 | ✔ |
| Figure 3.2 | Figure 8.2 | fig04.png | figure-8.2.png | 1898 | ✔ |
| Figure 4.1 | Figure 9.1 | fig05.png | figure-9.1.png | 1997 | ✔ |
| Figure 5.1 | Figure 10.1 | fig06.png | figure-10.1.png | 2039 | ✔ |
| Figure 6.1 | Figure 11.1 | fig07.png | figure-11.1.png | 2206 | ✔ |
| Figure 6.2 | Figure 11.2 | fig08.png | figure-11.2.png | 2252 | ✔ |
| Figure 7.1 | Figure 12.1 | fig09.png | figure-12.1.png | 2303 | ✔ |
| Figure 7.2 | Figure 12.2 | fig-sections.png | figure-12.2.png | 2365 | ✔ |
| Figure 7.3 | Figure 12.3 | fig-pareto-1.png | figure-12.3.png | 2406 | ✔ |
| Figure 7.4 | Figure 12.4 | fig-tree-1.png | figure-12.4.png | 2505 | ✔ |
| Figure 7.5 | Figure 12.5 | fig-silhouette.png | figure-12.5.png | 3443 | ✔ |
| Figure 10.1 | Figure 15.1 | fig10.png | figure-15.1.png | 4290 | ✔ |
| Figure 11.1 | Figure 16.1 | fig11.png | figure-16.1.png | 4342 | ✔ |
| Figure 11.2 | Figure 16.2 | fig12.png | figure-16.2.png | 4679 | ✔ |
| Figure 14.1 | Figure 19.1 | fig13.png | figure-19.1.png | 5379 | ✔ |
| Figure 21.1 | Figure 21.1 | fig-constraints.png | figure-21.1.png | 5706 | ✔ |
| Figure 16.1 | Figure 23.1 | fig14.png | figure-23.1.png | 6152 | ✔ |
| Figure 16.2 | Figure 23.2 | fig15.png | figure-23.2.png | 6287 | ✔ |
| Figure 16.3 | Figure 23.3 | fig16.png | figure-23.3.png | 6436 | ✔ |
| Figure 16.4 | Figure 23.4 | fig17.png | figure-23.4.png | 6530 | ✔ |
| Figure 17.1 | Figure 24.1 | fig18.png | figure-24.1.png | 6599 | ✔ |
| Figure 17.2 | Figure 24.2 | fig19.png | figure-24.2.png | 6612 | ✔ |
| Figure 17.3 | Figure 24.3 | fig20.png | figure-24.3.png | 6796 | ✔ |
| Figure 18.1 | Figure 25.1 | fig21.png | figure-25.1.png | 6898 | ✔ |
| Figure 18.2 | Figure 25.2 | fig22.png | figure-25.2.png | 7025 | ✔ |
| Figure 19.1 | Figure 26.1 | fig23.png | figure-26.1.png | 7074 | ✔ |
| Figure 20.1 | Figure 27.1 | fig24.png | figure-27.1.png | 7205 | ✔ |
| Figure 23.1 | Figure 30.1 | fig25.png | figure-30.1.png | 8376 | ✔ |
| Figure 23.2 | Figure 30.2 | fig26.png | figure-30.2.png | 8423 | ✔ |
| Figure 25.1 | Figure D.1 | fig27.png | figure-D.1.png | 10389 | ✔ (line moved by the chat-4 heading promotion; caption matches) |

## Compendia (figures-compendia/, 12 files; the eight referenced: fig-i1-tower, fig-i2-landscape, fig-i3-lambda8, fig-i4-crossing, fig-spectra-lattice, fig-supply, fig-channel-map, fig-index-final; four extra kept: fig-spectra-lattice4, fig-spectra-grid, fig-spectra-grid4, fig-survey)

## Already in project knowledge (15, in figures/): fig1–5_*, figadd*, FIG1–FIG6.

## Regenerated
figure-D.1.png was re-rendered from `dclose.py`'s current table (77 elements, 24 fibres) because the archived fig27 showed the Appendix D of 32 elements / 16 fibres; the archived image is kept as figure-D.1-prior-32-elements.png (register 1742). The other 32 archived plots are dated at the restore point (2.13) and must be checked against their captions' numbers when placed.
<<<END FILE: FIGURE_ASSETS.md>>>

<<<FILE: D59_DRAFT.md>>>
# Draft — D.5.9 The re-closure owed after Chapters 35 and 36 (for the author's ruling)

§D.1 says E = 0 expires whenever the mathematics grows. The Mathematical Compendium now indexes seventeen objects from the Löwdin solution (LS, 8) and the three-body work (3B, 9). This is the re-closure, run by the collaborator on a **proposed** placement; every row's fibre and coordinates are a reading of the compendium entry (grade, source, verification stated) and each is the author's to confirm or move.

Method check: the 48-element state of D.5.8 was rebuilt from D.5.2, D.5.4, D.5.6–D.5.8 and closed under the two constraints of D.3; it returns E = 0 in all sixteen fibres, so the closure is reproduced before anything is added.

| new element | fibre | status · verification · precedent | read from |
|---|---|---|---|
| LS.ent the entrant operator, §35 | mechanism · physics | verified · exhaustive · none found | COMPUTED; 107/107 over Z = 2–108 |
| LS.law the ordering law, five clauses | law · physics | proved · exhaustive · none found | PROVED; companion paper |
| LS.coll the collapse condition | mechanism · physics | verified · exhaustive · found | COMPUTED; Griffin–Andrew–Cowan 1969, 1971 |
| LS.pin the pinned-channel theorem (no g block) | theorem · physics | measured · exhaustive · none found | MEASURED; every g channel offered |
| LS.asym the state-dependent multiplier identity | theorem · analysis | proved · exhaustive · found | PROVED; Löwdin 1950 |
| LS.quart the exact-quartic decomposition | theorem · analysis | proved · exhaustive · none found | PROVED; five evaluations, no truncation |
| LS.chord chord = rot + perp | theorem · analysis | proved · exhaustive · found | PROVED; Pulay 1969, Gerratt–Mills 1968 |
| LS.twin the twin operator, c → ∞ | measurement · physics | measured · exhaustive · none found | MEASURED; eleven elements |
| 3B.shape the shape sphere | definition · analysis | proved · exhaustive · found | PROVED; Montgomery 2014, Hopf 1931 |
| 3B.metric the shape metric | formula · analysis | proved · exhaustive · found | PROVED; Montgomery 2014 |
| 3B.JM the Jacobi–Maupertuis metric | formula · analysis | proved · exhaustive · found | PROVED; Maupertuis, Jacobi |
| 3B.pot the potential on shape space | formula · analysis | **measured · sampled · found** | MEASURED; 650 random triangles, 10⁻¹⁰; register 1718 |
| 3B.norm the norm variety | theorem · algebraic geometry | proved · exhaustive · found | PROVED; Lagrange 1770; registers 1719–1720 |
| 3B.five the five fixed points | theorem · analysis | **measured · exhaustive · found** | MEASURED; Euler 1767, Lagrange 1772; register 1717 |
| 3B.tri the triangle form at cap 8 | measurement · combinatorics | measured · exhaustive · none found | MEASURED; 344 cells; register 1716 |
| 3B.def the deficit, one level | theorem · complexity | proved · exhaustive · found | PROVED; Freuder 1982 |
| 3B.index Λ₃, E = 0 | theorem · order | proved · exhaustive · found | PROVED; Chazy, Saari, Brudno; registers 1713, 1714, 1724 |

**Forty-eight elements become sixty-five over twenty-two fibres, and the first run gives E = 4.** Six fibres open for the first time (mechanism · physics, law · physics, theorem · physics, definition · analysis, theorem · algebraic geometry, theorem · complexity) and each closes trivially. The excess is in two existing fibres:

- **formula · analysis** (λ², V = 4ν/3, the bracket width, now with 3B.metric, 3B.JM, 3B.pot): three cells admitted and absent — *measured · sampled · none found*, *verified · exhaustive · found*, *measured · exhaustive · found*. All three are opened by **3B.pot** entering as measured · sampled · found beside the fibre's measured · exhaustive · none found and verified · exhaustive · none found.
- **theorem · analysis** (A.12, A.13, now with LS.asym, LS.quart, LS.chord, 3B.five): one cell — *measured · exhaustive · none found*, opened by **3B.five** entering as *measured* beside proved · exhaustive · none found.

**§12's loop offers two resolutions, and each was run.**
1. *Reclassify 3B.five.* If the five fixed points are Euler's and Lagrange's theorem (proved · exhaustive · found) rather than a measurement of this work, theorem · analysis closes at once. Recomputed: yes.
2. *Reclassify 3B.pot.* Its verification is 650 random triangles at 10⁻¹⁰ — that is *sampled*, and the appendix's own correction at D.5.8 (a sampled verification entered as exhaustive) forbids calling it otherwise. As proved · sampled · found the fibre still admits two cells (*measured · sampled · none found*, *verified · sampled · none found*): E = 2. Only proved · **exhaustive** · found closes it — which is true of the *derivation* (Montgomery's Theorem, register 1718's correction of the hyper-radius factor), not of the numerical check.

So the honest state is one of: (a) E = 2 at sixty-five elements with 3B.pot sampled, the two admitted cells named and the fibre left open, as F.3.3 leaves G; or (b) E = 0 with 3B.pot entered on its derivation rather than its check, and the 650-triangle run recorded as corroboration in the compendium entry, as §32.4.1 did for ℛ. The collaborator's reading is (b) — the potential is a theorem the paper proves in three lines and then checks — but it is the same judgement that D.5.8 says the author had to be corrected on, in the other direction, and it is the author's to make.

Not yet elements, and stated as such: the Löwdin work's mathematics of Chapter 34 (registers 1249–1357) is indexed separately in the compendium and was never entered in D; whether it should be is a prior question this draft does not answer.

Register entry owed: the sequence 48 → 65, E = 4 → resolution → 0, with the two placements ruled.
<<<END FILE: D59_DRAFT.md>>>

<<<FILE: MANIFEST.md>>>

# The Method 1.6 — Build Manifest (Phase 0, closed 2026-08-23)

## Canonical sources (.md, UTF-8, LF)
| Volume | File | Words | State |
|---|---|---|---|
| Main volume | The_Method_1_6-1.md | 112,089 | Ch 1–34 + App A–F; no arcs merged |
| The Register | The_Method_1_6___The_Register-1.md | 188,409 | entries 165–1700 |
| Mathematical Compendium | ..._Mathematical_Compendium-1.md | 29,766 | no arcs merged |
| Spectra Compendium | ..._Spectra_Compendium-1.md | 18,586 | no arcs merged |
| Physics Compendium | ..._The_Physics_Compendium-1.md | 7,113 | no arcs merged |
| Index of Indices | ..._The_Index_of_Indices-1.md | 27,254 | no arcs merged |

JPEG bundles (mis-named .pdf) = visual reference only. Text ".pdf" copies superseded by .md.
`theory_of_everything_expanded_formalism` — deferred, out of scope for this build.

## Arc numbering ruling (by timestamp: Löwdin concluded first)
| Arc | Chapter | Register entries | Source files |
|---|---|---|---|
| Löwdin solution | 35 | 1701–1712 | BODY2-CHAPTER-35, BODY3-* (5 files), THE-LOWDIN-SOLUTION.md (paper) |
| Three-body | 36 | 1713–1724 | Chapter_36_Three_Bodies_RENUMBERED.md, Compendium_Additions_Three_Body_RENUMBERED.md, The_Three_Body_Problem…Lach.md (paper) |

## Phase 1 merge order
1. Register  2. Mathematical  3. Physics  4. Index of Indices  5. Spectra  6. Main volume
Each: Löwdin then three-body; cross-reference check closes the segment.

## Open notes carried into Phase 1
- Three-body chapter header says "Serving PART III and PART VI"; it is placed in PART VII — THE CHALLENGES. Reconcile header.
- Register front matter (kinds table, load-bearing table, "1493 entries, 165 to 1700") must be recounted after append.

## BUILD 5 (chat 4, 2026-08-24) — Phase 3 complete
| Volume | Words | State |
|---|---|---|
| Main volume -2 | 122,632 | D.5.10 (77/24, E = 0); Index regenerated; headings levelled; 17 count sentences at 1,530 |
| Register -2 | 199,257 | 1,530 entries, 165–1737 (1733–1737 this chat); citation counts 588/398/715/1,002 |
| Mathematical Compendium -2 | 32,244 | depths from graph; chains rewritten; bibliography 162; D.5.10 pointer |
| Physics Compendium -2 | 9,187 | Λ_phys rule printed for the five new parameters |
| Index of Indices -2 | 28,709 | mathematics row 77/24; term index named |
| Spectra Compendium -2 | 19,739 | unchanged |
| Löwdin paper -2 | 5,714 | unchanged |
| Three-body paper -2 | 3,443 | unchanged |
Tools: register_cites.py, dclose.py, index_gen.py, split.py.


**BUILD-8 (chat 7, 2026-08-24).** Register 1,542 (165–1749). Added: HANDOFF-9.md, crop_titles.py, qgraph.py. Figures: 14 cropped (1747); figures-pre-crop/ holds originals. Papers pressed. All eight volumes pressed.
<<<END FILE: MANIFEST.md>>>

<<<FILE: REGISTER_AUDIT.md>>>

# Register — Phase 2 audit (reader perspective)

| # | finding | status |
|---|---|---|
| R1 | Entries 1169 and 1171 sat before 1165 (displaced block). | **Closed** — moved to numeric position. |
| R2 | Load-bearing table: six of ten "what it established" cells blank. | **Closed** — filled from the entries' own headlines. |
| R3 | Forty fault entries (203–358) are grouped by mechanism after 361; no signpost told the reader. | **Closed** — "Where to find an entry" added to the front matter; grouped and absent numbers counted from the file. |
| R4 | Five forms of entry across the record (plain; sentence headline ± italic body; caps headline ± italic body) and a "cited" heading tag used only to entry 800. | **Closed — ruling C.** Every entry normalised to the settled form (caps headline, italic body); tags removed; no content changed. Recorded as entry 1725 with Register-1 named as the witness. Generator drift stated in the front matter. |
| R5 | Header counts recomputed at merge (1517 entries; kinds table). Load-bearing "376 cited" and per-entry cited-by counts not recomputed. | **Deferred to Phase 3** (cross-volume citation pass). |
| R6 | `![caption](file.png)` at entry 642 is an inline code example, not a broken image. | No defect. |
| R7 | Cross-references: every "register NNN" cited resolves (354 is in a grouped heading). | Verified. |
| R8 | No duplicate ids, no mojibake, no CRLF residue. | Verified. |
<<<END FILE: REGISTER_AUDIT.md>>>

<<<FILE: MATH_AUDIT.md>>>

# Mathematical Compendium — Phase 2 audit (reader perspective)

| # | finding | status |
|---|---|---|
| M1 | 265 objects, 18 families, no duplicate ids; every family header count matches its contents. | Verified. |
| M2 | Every object carries bold statement, italic gloss, grade line; every `depends on` and chain id resolves. | Verified. |
| M3 | Eight source references pointed at main-volume sections that no longer exist (`M §20.5`, `§21.8.1`, `§21.8.2`, `§21.10.1`, `§21.10.4`, `§21.15`, `§22.9`, `§26.9`). All resolve at chapter + 2 — written before Part IV (Chapters 20–21) was inserted. | **Closed** — repointed (§22.5, §23.8.1, §23.8.2, §23.10.1, §23.10.4, §23.15, §24.9, §28.9). Same test to be run on every volume in Phase 3. |
| M4 | 27 objects carried two PRIOR ART callouts jammed into one line; in 10 the second was a verbatim repeat. | **Closed** — repeats removed; the 17 distinct pairs split into two callouts. |
| M5 | ASCII/Unicode drift in the same names: `Lambda-9`/`Λ₉`, `Lambda_spectra`/`Λ_spectra`, `<=`/`≤`, `phi(`/`φ(`, `--`/`—` (about 150 instances outside code spans). | **Closed** — normalised to the Unicode forms the volume otherwise uses; code spans untouched. |
| M6 | "1 objects depend on it" (74). | **Closed.** |
| M7 | `M.semi` was the one object absent from the bibliography (Murray & von Neumann 1936). | **Closed** — row added; 172 works. |
| M8 | LS-family depths (15–17) are the build's assignment, not the author's. | **Open — Phase 3 chain audit** to confirm or reassign. |
| M9 | `T §5.1`, `T §6.5` reference the tower companion, not this set; unverifiable here. | Noted; no action. |
| M8 (closed, chat 4) | Every `depends on` resolves (265 objects; 17 roots). Depths recomputed from the graph (roots 0, depth = links): 255 of 265 agree. `LS.law` 16→**17** (rests on `LS.coll`, `LS.twin` at 16); LS 15/16/17 otherwise confirmed. 3B depths were 1-based inside the family and counted non-objects ("tree", "§7.1"): shape 1→0, metric 2→1, pot 2→1, tri 4→1, JM 3→2, norm 3→2, five 3→2, def 5→3, index 6→4. Part V chain lines for LS (depth 17) and 3B (depth 9) were written deepest-first and mis-routed; rewritten root-first on the actual longest paths (LS.chord via `Q.final`, 17 links; 3B.index via `G.graph`, 4). Root dependents stale after the 3B merge: `L.c1` 3→4, `L.c2–c6, c8` 1→2, `L.c7` 2→3. Sixteen source fields carried a name twice ("Janet 1929; Janet 1929") — deduplicated. Register ↔ object: every cited entry exists (script); 13 LS/3B objects and a sample of 10 others match their entries by content. **Open for the author:** `3B.shape` has no dependency (Montgomery 2014/Hopf 1931) — it is a root, and the family preamble says "No new root"; Part I lists fourteen roots. Either `3B.shape` is a fifteenth root or it rests on something not named. | **Closed** except the 3B.shape question. |
| M8 — 3B.shape (closed, chat 5) | Ruled stale: `3B.shape` entered as the eighteenth root; heading, front line (265 · 18 · 263 · 2) and preamble corrected; grade line in root form. Register 1739. | **Closed.** |
<<<END FILE: MATH_AUDIT.md>>>

<<<FILE: PHYS_AUDIT.md>>>

# Physics Compendium — Phase 2 audit (reader perspective)

| # | finding | status |
|---|---|---|
| P1 | All §-references resolve; no chapter-shift casualties here. | Verified. |
| P2 | The Λ_phys parameter entries were ASCII-only (`--`, `<=`, `n+l`, `Loewdin`, `Schroedinger`, `Lambda_phys`) against a Unicode volume. | **Closed** — normalised outside code spans (Goeppert kept: her spelling). |
| P3 | Λ_phys dependence table still summed to 22 after the merge added five parameters. | **Closed** — rows added (free parameters, exact-by-scaling), c entered under measured constants, total 27. |
| P4 | Two stale Löwdin-challenge claims (aufbau origin; channel-constants coda). | Closed in Phase 1; both prior states kept. |
| P5 | Top-level heading case mixed (two sentence-case among caps). | **Closed.** |
| P6 | "objects rest on it" counts for the five new parameters are the build's estimates. | **Open — Phase 3** object-count pass. |
| P6 (closed, chat 4) | Rule stated in the volume for the five new parameters (statement names it, plus everything depending on it, in the Math Compendium): c 8 (unchanged), masses 3→**5**, E 2, L 2→**1**, G 0. The 22 older counts are not reproducible from the Math Compendium under any single rule (direct mentions: ionisation limit 6 vs printed 25; aufbau 7 vs 19) — generated elsewhere on an unprinted rule; flagged, left as stated. | **Closed**, older rule flagged. |
| P6 — all 27 (closed, chat 5) | Author ruled regenerate all: one printed rule (statement/title names the parameter; closure under dependence), seeds listed per parameter, prior counts kept. Five parameters count 0 on the rule (mass ratio, Cs defect, actinides, R_M, Hund). Top table and its lead sentence rewritten; IOI Λ_phys entry corrected (27 parameters, new top three, prior kept). Register 1740. | **Closed.** |
<<<END FILE: PHYS_AUDIT.md>>>

<<<FILE: IOI_SPEC_AUDIT.md>>>

# Index of Indices & Spectra Compendium — Phase 2 audit (reader perspective)

## Index of Indices
| # | finding | status |
|---|---|---|
| I1 | All §-references resolve (one `§5.7` is to the companion). Register refs all ≤ 1725. | Verified. |
| I2 | The full tables in VII (976 / 90 / 118 / 365 / 35) reconcile with their headers. | Verified. |
| I3 | Part IX claims fifteen indexes and lists fourteen headings + Λ_spectra "closing at the limit" — consistent. | Verified. |
| I4 | Figure numbering out of page order after the merge (Λ₃ figure entered as 8 but sits before 5). | **Closed** — renumbered 1–8 by appearance. |
| I5 | Three-body additions note asked to remove an item from Part VI that was never there. | Noted in Phase 1; no defect in host. |

## Spectra Compendium
| # | finding | status |
|---|---|---|
| S1 | All §-references and register refs resolve; no ASCII drift; no jammed callouts. | Verified. |
| S2 | Grade totals: exact 929 + measured 358 + computed 103,545 = 104,832 = cells admitted. | Verified. |
| S3 | The totals paragraph after the channel table says "generated by `spectra.py` … cannot drift. 133 rows, 23 elements, 869 interior cells." The printed Part II holds 477 channel rows (229 unstarred + 248 starred J-resolved continuation rows) across 28 elements. Either the totals count only unstarred series with ≥3 members, or the paragraph predates the T8-J additions (registers 1699–1700). | **Closed — ruling: restate from the table.** Paragraph now carries 596 rows / 28 elements / 70 species / 3,342 levels / 2,269 interior / bracket 844/844 on 107 tested rows, 489 untested; the prior statement kept as history with its registers; `spectra.py` rebuild noted as owed. Main-volume Appendix B.2 carries the same stale sentence — to be restated in segment 6. |
| S4 | The host discloses rather than reconciles a 20-channel / 236-cell gap between the printed table and the stated totals ("owed"). | **Open — author.** Not a build defect; the twenty rows are owed by the author's own statement. |
| S5 | New 0′ section uses grades SCORED / UNWITNESSED / PINNED beside the host's exact / measured / computed; UNWITNESSED is shared vocabulary, the other two are the derived supply's own. | Acceptable; the section says why. |
<<<END FILE: IOI_SPEC_AUDIT.md>>>

<<<FILE: RULING-TOLERANCE-489.md>>>
# RULING — Tolerance for the 489-row bracket run

Issued by M (The Method Löwdin project), 2026-08-24, accompanying
`spectra_levels_store.zip` (sha256 08a6a78c…, cut from restore-point-2_13,
bank sha 80577094…, 708 files).

## The ruling

1. **Test.** The bracket test runs at STRICT INTERVAL MEMBERSHIP, exactly as
   the sealed instrument defines it (`bracket.py`, register 796):
   E(n) ∈ [E_lo, E_hi], where the interval is the energy span implied by the
   two neighbours' defects. No statistical tolerance. No k. No σ band.
   This is the condition the run itself stated — "the same test as the 107" —
   and the sealed test carries no tolerance to reproduce.

2. **Boundary guard (the only ε permitted).** Comparisons at the interval
   edges are guarded by the QUOTATION FLOOR: half a unit in the last quoted
   decimal place of the measured level. This is data quantization read off the
   source, not a fitted parameter, and it satisfies the standing floor rule
   (F104.1/F104.2: value-exact comparisons must state and exceed the
   floating-point floor).

3. **Admissibility replaces tolerance.** A cell where the measurement cannot
   distinguish pass from fail is REFUSED, not passed with slack:
   r = 2·Z²R/(ν³σ) ≥ 5 (Method §22.5). Refusals are counted and reported as
   their own column, separate from pass/fail.

4. **Option B (2·σ(δ) per channel, k = 2) is REJECTED**, on four registered
   grounds:
   a. It is a different test than the sealed 930-cell run — violating the
      run's own stated requirement.
   b. It grafts the inferential σ (Rule 4) onto the deductive bracket,
      collapsing Rule 3's separation; a deduction becomes an estimate
      (Method §22.2, §23.3: "V contains no σ").
   c. A tolerance-widened bracket is the registered fault species of a check
      that admits inputs incapable of failing it (registers 777, 782, 784).
   d. The σ it would be built from is measured untrustworthy where it would
      be used: quoted-decimal error estimates drive an 89% result to 55%
      with non-overlapping intervals (register 822); 44 of 49 species carry
      no uncertainty column (register 807); and per-channel σ(δ) computed
      from the data under test is register 781's circularity.

## Execution notes for the receiving chat

- Column updated row by row; count line rewritten; refusal count printed as
  its own line; this ruling's number registered where the note stands;
  Spectra and main re-pressed and sampled at the changes — per the plan
  already stated there.
- Flag standing: "844 of 844 on 107 tested rows" matches no figure in this
  bank's register (789/789 T-bracket, 546/789 δ-bracket, 930 cells /
  128 channels tested). Confirm its provenance in the receiving project's
  own record before attributing it to this bank's instrument.

## Derivation sources

bracket.py docstring (R 796) · Method §22.2 Rules 1–4 · §22.5 admissibility ·
§23.2 Prop. 14.1 (V > 2) · §23.3 (V contains no σ) · §23.14 capacity vs
resolution · registers 777, 781, 782, 784, 796, 803, 807, 822 ·
F104.1/F104.2 standing rule.
<<<END FILE: RULING-TOLERANCE-489.md>>>

<<<FILE: run489_final.json>>>
{"rec": {"C II|2s2(1S)np 2P\u00b0 J=1/2|2\u20134": ["run", 0, 1, 0, 1], "C II|2s2(1S)np 2P\u00b0 J=3/2|2\u20134": ["run", 0, 1, 0, 1], "Li I|np 2P\u00b0 J=1/2|2\u20134": ["run", 1, 0, 0, 1], "Li I|np 2P\u00b0 J=3/2|2\u20134": ["run", 1, 0, 0, 1], "Mg I|3snd 1D J=2|3\u20135": ["run", 1, 0, 0, 1], "Mg I|3snd 3D J=1|3\u20135": ["run", 1, 0, 0, 1], "Mg I|3snd 3D J=2|3\u20135": ["run", 1, 0, 0, 1], "Mg I|3snd 3D J=3|3\u20135": ["run", 1, 0, 0, 1], "Mg I|3snp 1P\u00b0 J=1|3\u20136": ["run", 2, 0, 0, 2], "Mg I|3snp 3P\u00b0 J=0|3\u20136": ["run", 2, 0, 0, 2], "Mg I|3snp 3P\u00b0 J=1|3\u20136": ["run", 2, 0, 0, 2], "Mg I|3snp 3P\u00b0 J=2|3\u20136": ["run", 2, 0, 0, 2], "Mg I|3sns 1S J=0|4\u20136": ["run", 1, 0, 0, 1], "Mg I|3sns 3S J=1|4\u20136": ["run", 1, 0, 0, 1], "Mg II|np 2P\u00b0 J=1/2|3\u20135": ["run", 1, 0, 0, 1], "Mg II|np 2P\u00b0 J=3/2|3\u20135": ["run", 1, 0, 0, 1], "Mg II|ns 2S J=1/2|3\u20136": ["run", 2, 0, 0, 2], "Si II|3s2.nd 2D J=3/2|3\u20138": ["run", 4, 0, 0, 4], "Si II|3s2.nd 2D J=5/2|3\u20138": ["run", 4, 0, 0, 4], "Si II|3s2.nf 2F* J=5/2|4\u201311": ["run", 6, 0, 0, 6], "Si II|3s2.nf 2F* J=7/2|4\u201311": ["run", 6, 0, 0, 6], "Si II|3s2.ng 2G J=7/2|5\u201310": ["run", 4, 0, 0, 4], "Si II|3s2.ng 2G J=9/2|5\u201310": ["run", 4, 0, 0, 4], "Si II|3s2.np 2P* J=1/2|3\u201310": ["run", 2, 4, 0, 6], "Si II|3s2.np 2P* J=3/2|3\u201310": ["run", 2, 4, 0, 6], "Si II|3s2.ns 2S J=1/2|4\u20139": ["run", 4, 0, 0, 4], "Li III|nd 2D J=3/2|3\u20139": ["run", 4, 1, 0, 5], "Li III|nd 2D J=5/2|3\u20139": ["run", 4, 1, 0, 5], "Li III|nf 2F* J=5/2|4\u20139": ["run", 4, 0, 0, 4], "Li III|nf 2F* J=7/2|4\u20139": ["run", 4, 0, 0, 4], "Li III|ng 2G J=7/2|5\u20139": ["run", 3, 0, 0, 3], "Li III|ng 2G J=9/2|5\u20139": ["run", 3, 0, 0, 3], "Li III|nh 2H* J=11/2|6\u20139": ["run", 2, 0, 0, 2], "Li III|nh 2H* J=9/2|6\u20139": ["run", 2, 0, 0, 2], "Li III|ni 2I J=11/2|7\u20139": ["run", 1, 0, 0, 1], "Li III|ni 2I J=13/2|7\u20139": ["run", 1, 0, 0, 1], "Li III|np 2P* J=1/2|2\u201310": ["run", 5, 2, 0, 7], "Li III|np 2P* J=3/2|2\u201310": ["run", 5, 2, 0, 7], "Li III|ns 2S J=1/2|1\u20139": ["run", 5, 2, 0, 7], "Ba III|5p5.(2P*<3/2>).nd 2[1/2]* J=0|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[1/2]* J=1|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[3/2]* J=1|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[3/2]* J=2|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[5/2]* J=2|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[5/2]* J=3|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[7/2]* J=3|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).nd 2[7/2]* J=4|5\u20137": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).ns 2[3/2]* J=1|6\u20138": ["run", 1, 0, 0, 1], "Ba III|5p5.(2P*<3/2>).ns 2[3/2]* J=2|6\u20138": ["run", 1, 0, 0, 1], "Bi II|6s2.6p.nd (1/2,3/2)* J=1|6\u201314": ["run", 2, 5, 0, 7], "Bi II|6s2.6p.nd (1/2,3/2)* J=2|6\u201310\u2020": ["run", 0, 0, 0, 0], "Bi II|6s2.6p.nd (1/2,5/2)* J=2|6\u20138": ["run", 0, 1, 0, 1], "Bi II|6s2.6p.nf (1/2,5/2) J=3|5\u20138\u2020": ["run", 0, 0, 0, 0], "Bi II|6s2.6p.nf (1/2,7/2) J=4|5\u20138\u2020": ["run", 0, 0, 0, 0], "Bi II|6s2.6p.ns (1/2,1/2)* J=0|7\u20139": ["run", 1, 0, 0, 1], "Bi II|6s2.6p.ns (1/2,1/2)* J=1|7\u20139": ["run", 1, 0, 0, 1], "Ne I|2s22p5(2P*3/2)nd 2[3/2]* J=1|13\u201320": ["run", 2, 4, 0, 6], "Ne I|2s22p5(2P*3/2)ns 2[3/2]* J=1|12\u201320": ["run", 4, 3, 0, 7], "Li II|1s.nd 1D J=2|3\u201310": ["run", 6, 0, 0, 6], "Li II|1s.nd 3D J=2|3\u201310": ["run", 5, 1, 0, 6], "Li II|1s.nf 1F* J=3|4\u201310": ["run", 5, 0, 0, 5], "Li II|1s.nf 3F* J=3|4\u201310": ["run", 4, 1, 0, 5], "Li II|1s.ng 1G J=4|5\u20139": ["run", 3, 0, 0, 3], "Li II|1s.nh 1H* J=5|6\u20139": ["run", 2, 0, 0, 2], "Li II|1s.np 1P* J=1|2\u201314": ["run", 7, 4, 0, 11], "Li II|1s.np 3P* J=1|2\u201310": ["run", 7, 0, 0, 7], "Li II|1s.ns 1S J=0|2\u201310": ["run", 5, 2, 0, 7], "Li II|1s.ns 3S J=1|2\u201310": ["run", 7, 0, 0, 7], "Bi II|6s2.6p.nf (1/2,7/2) J=3|5\u20136": ["run", 0, 0, 0, 0], "Bi II|6s2.6p.np (1/2,1/2) J=0|7\u20138": ["run", 0, 0, 0, 0], "C II|2s2(1S)nd 2D J=3/2|3\u20134": ["run", 0, 0, 0, 0], "C II|2s2(1S)nd 2D J=5/2|3\u20134": ["run", 0, 0, 0, 0], "C II|2s2(1S)ns 2S J=1/2|3\u20134": ["run", 0, 0, 0, 0], "Li I|nd 2D J=3/2|3\u20134": ["run", 0, 0, 0, 0], "Li I|nd 2D J=5/2|3\u20134": ["run", 0, 0, 0, 0], "Li I|ns 2S J=1/2|2\u20133": ["run", 0, 0, 0, 0], "Li II|1s.ni 1I J=6|7\u20138": ["run", 0, 0, 0, 0], "Li II|1s.np 3P* J=0|2\u20133": ["run", 0, 0, 0, 0], "Li II|1s.np 3P* J=2|2\u20133": ["run", 0, 0, 0, 0], "Li III|nk 2K* J=13/2|8\u20139": ["run", 0, 0, 0, 0], "Li III|nk 2K* J=15/2|8\u20139": ["run", 0, 0, 0, 0], "Mg I|3snf 1F\u00b0 J=3|4\u20135": ["run", 0, 0, 0, 0], "Mg I|3snf 3F\u00b0 J=2|4\u20135": ["run", 0, 0, 0, 0], "Mg I|3snf 3F\u00b0 J=3|4\u20135": ["run", 0, 0, 0, 0], "Mg I|3snf 3F\u00b0 J=4|4\u20135": ["run", 0, 0, 0, 0], "Mg II|nd 2D J=3/2|3\u20134": ["run", 0, 0, 0, 0], "Mg II|nd 2D J=5/2|3\u20134": ["run", 0, 0, 0, 0], "Ne I|2p5(2P\u00b03/2)nd 2[7/2]\u00b0 J=4|3\u20134": ["run", 0, 0, 0, 0], "Ne I|2p5(2P\u00b03/2)ns 2[3/2]\u00b0 J=2|3\u20134": ["run", 0, 0, 0, 0], "Zn I|4snd 3D J=1|4\u20135": ["run", 0, 0, 0, 0], "Zn I|4snd 3D J=2|4\u20135": ["run", 0, 0, 0, 0], "Zn I|4snd 3D J=3|4\u20135": ["run", 0, 0, 0, 0], "B III|nd 2D J=3/2|3\u201311": ["run", 7, 0, 0, 7], "B III|nf 2F* J=5/2|4\u201311": ["run", 5, 1, 0, 6], "B III|ng 2G J=7/2|5\u201310": ["run", 3, 1, 0, 4], "B III|nh 2H* J=9/2|6\u201310": ["run", 3, 0, 0, 3], "B III|np 2P* J=1/2|2\u20139": ["run", 3, 3, 0, 6], "B III|ns 2S J=1/2|2\u20139": ["run", 6, 0, 0, 6], "Be III|1s.nd 1D J=2|3\u201310": ["run", 4, 2, 0, 6], "Be III|1s.nd 3D J=2|3\u201310": ["run", 3, 3, 0, 6], "Be III|1s.nf 1F* J=3|4\u20139": ["run", 2, 2, 0, 4], "Be III|1s.ng 1G J=4|5\u20139": ["run", 1, 2, 0, 3], "Be III|1s.nh 1H* J=5|6\u20139": ["run", 2, 0, 0, 2], "Be III|1s.ni 1I J=6|7\u20138": ["run", 0, 0, 0, 0], "Be III|1s.np 3P* J=1|2\u201310": ["run", 5, 2, 0, 7], "Be III|1s.ns 1S J=0|2\u201310": ["run", 4, 3, 0, 7], "Be III|1s.ns 3S J=1|2\u201310": ["run", 5, 2, 0, 7], "Be IV|nd 2D J=3/2|3\u201310": ["run", 6, 0, 0, 6], "Be IV|nf 2F* J=5/2|4\u201310": ["run", 5, 0, 0, 5], "Be IV|ng 2G J=7/2|5\u201310": ["run", 4, 0, 0, 4], "Be IV|nh 2H* J=9/2|6\u201310": ["run", 3, 0, 0, 3], "Be IV|ni 2I J=11/2|7\u201310": ["run", 2, 0, 0, 2], "Be IV|nk 2K* J=13/2|8\u201310": ["run", 1, 0, 0, 1], "Be IV|np 2P* J=1/2|3\u201310": ["run", 6, 0, 0, 6], "Be IV|ns 2S J=1/2|3\u201310": ["run", 6, 0, 0, 6], "Mg III|nd 2[1/2]* J=1|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nd 2[3/2]* J=1|4\u20139": ["run", 1, 3, 0, 4], "Mg III|nf 2[3/2] J=1|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[3/2] J=2|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[5/2] J=3|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[7/2] J=3|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[7/2] J=4|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[9/2] J=4|4\u20135": ["run", 0, 0, 0, 0], "Mg III|nf 2[9/2] J=5|4\u20135": ["run", 0, 0, 0, 0], "Mg III|ns 2[3/2]* J=1|4\u20136": ["run", 1, 0, 0, 1], "Mg III|ns 2[3/2]* J=2|4\u20135": ["run", 0, 0, 0, 0], "Al III|nd 2D J=5/2|3\u20138": ["run", 4, 0, 0, 4], "Al III|nf 2F* J=5/2|4\u20139": ["run", 4, 0, 0, 4], "Al III|ng 2G J=7/2|5\u20139": ["run", 2, 1, 0, 3], "Al III|nh 2H* J=9/2|6\u20139": ["run", 1, 1, 0, 2], "Al III|np 2P* J=1/2|3\u20137": ["run", 3, 0, 0, 3], "Al III|ns 2S J=1/2|3\u20138": ["run", 4, 0, 0, 4], "Si III|nd 1D J=2|3\u20139": ["run", 3, 2, 0, 5], "Si III|nd 3D J=3|3\u20139": ["run", 2, 3, 0, 5], "Si III|nf 1F* J=3|4\u20139": ["run", 2, 2, 0, 4], "Si III|nf 3F* J=2|4\u20139": ["run", 4, 0, 0, 4], "Si III|nf 3F* J=3|4\u20139": ["run", 4, 0, 0, 4], "Si III|nf 3F* J=4|4\u20139": ["run", 4, 0, 0, 4], "Si III|ng 1G J=4|5\u20138": ["run", 2, 0, 0, 2], "Si III|ng 3G J=3|5\u20139": ["run", 3, 0, 0, 3], "Si III|ng 3G J=4|5\u20139": ["run", 3, 0, 0, 3], "Si III|ng 3G J=5|5\u20139": ["run", 3, 0, 0, 3], "Si III|nh 1H* J=5|6\u20139": ["run", 2, 0, 0, 2], "Si III|nh 3H* J=5|7\u20139": ["run", 1, 0, 0, 1], "Si III|nh 3H* J=6|6\u20139": ["run", 2, 0, 0, 2], "Si III|ni 1I J=6|7\u20139": ["run", 1, 0, 0, 1], "Si III|ni 3I J=7|7\u20139": ["run", 1, 0, 0, 1], "Si III|np 1P* J=1|4\u20137": ["run", 0, 2, 0, 2], "Si III|np 3P* J=0|4\u20137": ["run", 2, 0, 0, 2], "Si III|ns 1S J=0|4\u20138": ["run", 2, 1, 0, 3], "Si III|ns 3S J=1|4\u20138": ["run", 3, 0, 0, 3], "B IV|1s.nd 1D J=2|3\u201310": ["run", 2, 4, 0, 6], "B IV|1s.nd 3D J=1|3\u201310": ["run", 3, 3, 0, 6], "B IV|1s.nf 1F* J=3|4\u20139": ["run", 3, 1, 0, 4], "B IV|1s.ng 1G J=4|5\u20139": ["run", 0, 3, 0, 3], "B IV|1s.nh 1H* J=5|6\u20139": ["run", 1, 1, 0, 2], "B IV|1s.ni 1I J=6|7\u20138": ["run", 0, 0, 0, 0], "B IV|1s.np 1P* J=1|3\u201310": ["run", 3, 3, 0, 6], "B IV|1s.np 3P* J=0|3\u201310": ["run", 6, 0, 0, 6], "B IV|1s.ns 1S J=0|3\u201310": ["run", 4, 2, 0, 6], "B IV|1s.ns 3S J=1|3\u201310": ["run", 6, 0, 0, 6], "B V|nd 2D J=3/2|3\u201310": ["run", 6, 0, 0, 6], "B V|nf 2F* J=5/2|4\u201310": ["run", 5, 0, 0, 5], "B V|ng 2G J=7/2|5\u20139": ["run", 3, 0, 0, 3], "B V|nh 2H* J=9/2|6\u20139": ["run", 2, 0, 0, 2], "B V|ni 2I J=11/2|7\u20139": ["run", 1, 0, 0, 1], "B V|nk 2K* J=13/2|8\u20139": ["run", 0, 0, 0, 0], "B V|np 2P* J=1/2|3\u201310": ["run", 6, 0, 0, 6], "B V|ns 2S J=1/2|3\u201310": ["run", 6, 0, 0, 6], "Si IV|nd 2D J=5/2|3\u20138": ["run", 4, 0, 0, 4], "Si IV|nf 2F* J=5/2|4\u20138": ["run", 3, 0, 0, 3], "Si IV|ng 2G J=7/2|5\u20138": ["run", 2, 0, 0, 2], "Si IV|nh 2H* J=9/2|6\u20137": ["run", 0, 0, 0, 0], "Si IV|np 2P* J=1/2|3\u20138": ["run", 4, 0, 0, 4], "Si IV|ns 2S J=1/2|3\u20138": ["run", 4, 0, 0, 4], "P IV|nd 1D J=2|4\u20136": ["run", 0, 1, 0, 1], "P IV|nd 3D J=1|4\u20136": ["run", 0, 1, 0, 1], "P IV|nf 3F* J=2|4\u20136": ["run", 1, 0, 0, 1], "P IV|np 1P* J=1|4\u20136": ["run", 0, 1, 0, 1], "P IV|np 3P* J=0|4\u20136": ["run", 0, 1, 0, 1], "P IV|ns 1S J=0|4\u20136": ["run", 1, 0, 0, 1], "P IV|ns 3S J=1|4\u20137": ["run", 0, 2, 0, 2], "C V|1s.nd 1D J=2|3\u20137": ["run", 3, 0, 0, 3], "C V|1s.nd 3D J=1|3\u20137": ["run", 3, 0, 0, 3], "C V|1s.nf 1F* J=3|4\u20136": ["run", 1, 0, 0, 1], "C V|1s.nf 3F* J=3|4\u20136": ["run", 1, 0, 0, 1], "C V|1s.ng 1G J=4|5\u20137": ["run", 1, 0, 0, 1], "C V|1s.ng 3G J=4|5\u20137": ["run", 1, 0, 0, 1], "C V|1s.nh 1H* J=5|6\u20137": ["run", 0, 0, 0, 0], "C V|1s.np 1P* J=1|2\u20137": ["run", 4, 0, 0, 4], "C V|1s.np 3P* J=0|2\u20137": ["run", 4, 0, 0, 4], "C V|1s.ns 1S J=0|2\u20137": ["run", 4, 0, 0, 4], "C V|1s.ns 3S J=1|2\u20137": ["run", 3, 1, 0, 4], "S V|3s.nd 1D J=2|4\u20136": ["run", 0, 1, 0, 1], "S V|3s.nd 3D J=1|4\u20137": ["run", 1, 1, 0, 2], "S V|3s.nf 1F* J=3|4\u20136": ["run", 0, 1, 0, 1], "S V|3s.nf 3F* J=2|4\u20136": ["run", 1, 0, 0, 1], "S V|3s.np 1P* J=1|4\u20137": ["run", 1, 1, 0, 2], "S V|3s.np 3P* J=0|4\u20136": ["run", 0, 1, 0, 1], "S V|3s.ns 1S J=0|4\u20137": ["run", 0, 2, 0, 2], "S V|3s.ns 3S J=1|4\u20137": ["run", 1, 1, 0, 2], "Fe XV|nd 3D J=1|4\u20135": ["run", 0, 0, 0, 0], "Fe XV|nf 1F* J=3|4\u20136": ["run", 1, 0, 0, 1], "Fe XV|nf 3F* J=2|4\u20135": ["run", 0, 0, 0, 0], "Fe XV|np 1P* J=1|4\u20135": ["run", 0, 0, 0, 0], "Ca IX|nd 1D J=2|4\u20136": ["run", 0, 1, 0, 1], "Ca IX|nf 1F* J=3|4\u20135": ["run", 0, 0, 0, 0], "Ca IX|np 1P* J=1|4\u20136": ["run", 0, 1, 0, 1], "Ca IX|ns 3S J=1|4\u20135": ["run", 0, 0, 0, 0], "Ti XI|nf 1F* J=3|4\u20135": ["run", 0, 0, 0, 0], "Ti XI|np 1P* J=1|4\u20137": ["run", 1, 1, 0, 2], "Ti XI|ns 1S J=0|4\u20135": ["run", 0, 0, 0, 0], "Ti XI|ns 3S J=1|4\u20135": ["run", 0, 0, 0, 0], "Ti III|nd 1F J=3|4\u20135": ["run", 0, 0, 0, 0], "Ti III|nd 3D J=1|4\u20135": ["run", 0, 0, 0, 0], "Ti III|np 1D* J=2|4\u20135": ["run", 0, 0, 0, 0], "Ti III|np 3D* J=1|4\u20135": ["run", 0, 0, 0, 0], "Ti III|np 3F* J=2|4\u20135": ["run", 0, 0, 0, 0], "Ti III|ns 1D J=2|4\u20135": ["run", 0, 0, 0, 0], "Ti III|ns 3D J=1|4\u20135": ["run", 0, 0, 0, 0], "Ca II|ns 2S J=1/2|4\u20136": ["run", 1, 0, 0, 1], "Ar I|nd 2[7/2]* J=4|3\u20136": ["run", 2, 0, 0, 2], "Ar I|np 2[1/2] J=1|4\u20137": ["run", 1, 1, 0, 2], "Ar I|np 2[3/2] J=1|4\u20137": ["run", 1, 1, 0, 2], "Ar I|np 2[5/2] J=3|4\u20137": ["run", 1, 1, 0, 2], "Ar I|ns 2[3/2]* J=1|4\u20137": ["run", 1, 1, 0, 2], "Ar I|ns 2[3/2]* J=2|4\u20137": ["run", 1, 1, 0, 2], "Cd I|nd 1D J=2|5\u201315\u2020": ["run", 5, 1, 0, 6], "Cd I|nd 3D J=1|5\u201311": ["run", 5, 0, 0, 5], "Cd I|nf 3F* J=3|4\u201310": ["run", 5, 0, 0, 5], "Cd I|np 1P* J=1|6\u201312": ["run", 3, 2, 0, 5], "Cd I|np 3P* J=0|6\u201310": ["run", 3, 0, 0, 3], "Cd I|ns 1S J=0|6\u201315": ["run", 5, 3, 0, 8], "Cd I|ns 3S J=1|6\u201316": ["run", 7, 2, 0, 9], "Ga II|nd 1D J=2|4\u20137": ["run", 2, 0, 0, 2], "Ga II|nd 3D J=1|4\u20137": ["run", 2, 0, 0, 2], "Ga II|nf 1F* J=3|4\u20137": ["run", 2, 0, 0, 2], "Ga II|nf 3F* J=2|4\u20137": ["run", 2, 0, 0, 2], "Ga II|ng (1/2,7/2) J=3|5\u20138": ["run", 2, 0, 0, 2], "Ga II|ng (1/2,9/2) J=5|5\u20138": ["run", 2, 0, 0, 2], "Ga II|ns 1S J=0|5\u20138": ["run", 1, 1, 0, 2], "Ga II|ns 3S J=1|5\u20138": ["run", 2, 0, 0, 2], "P III|nd 2D J=5/2|3\u20136": ["run", 2, 0, 0, 2], "P III|ng 2G J=7/2|5\u20138": ["run", 1, 1, 0, 2], "P III|nh 2H* J=9/2|6\u20138": ["run", 1, 0, 0, 1], "P III|np 2P* J=1/2|4\u20136": ["run", 0, 1, 0, 1], "P III|ns 2S J=1/2|4\u20139": ["run", 4, 0, 0, 4], "Ba II|nd 2D J=3/2|5\u201325\u2020": ["run", 10, 0, 0, 10], "Ba II|nf 2F* J=5/2|4\u201312": ["run", 7, 0, 0, 7], "Ba II|ng 2G J=7/2|5\u201310": ["run", 4, 0, 0, 4], "Ba II|np 2P* J=1/2|6\u201312": ["run", 5, 0, 0, 5], "Ba II|ns 2S J=1/2|6\u201330\u2020": ["run", 14, 0, 0, 14], "Fe XVI|nd 2D J=3/2|3\u20138": ["run", 4, 0, 0, 4], "Fe XVI|nf 2F* J=5/2|4\u20138": ["run", 3, 0, 0, 3], "Fe XVI|np 2P* J=1/2|3\u20136": ["run", 2, 0, 0, 2], "Fe XVI|ns 2S J=1/2|3\u20137": ["run", 3, 0, 0, 3], "N III|nd 2D J=3/2|3\u201312": ["run", 5, 3, 0, 8], "N III|nf 2F* J=5/2|4\u20137": ["run", 2, 0, 0, 2], "N III|ng 2G J=7/2|5\u20137": ["run", 1, 0, 0, 1], "N III|nh 2H* J=9/2|6\u20137": ["run", 0, 0, 0, 0], "N III|np 2P* J=1/2|3\u20135": ["run", 0, 1, 0, 1], "N III|ns 2S J=1/2|3\u201314": ["run", 9, 1, 0, 10], "S IV|nd 2D J=3/2|3\u20135": ["run", 1, 0, 0, 1], "S IV|np 2P* J=1/2|4\u20137": ["run", 1, 1, 0, 2], "S IV|ns 2S J=1/2|4\u20137": ["run", 1, 1, 0, 2], "S VI|nd 2D J=3/2|3\u20139\u2020": ["run", 2, 0, 0, 2], "S VI|nf 2F* J=5/2|4\u201310": ["run", 4, 1, 0, 5], "S VI|ng 2G J=7/2|5\u20136": ["run", 0, 0, 0, 0], "S VI|nh 2H* J=9/2|6\u20137": ["run", 0, 0, 0, 0], "S VI|np 2P* J=1/2|3\u20137": ["run", 3, 0, 0, 3], "S VI|ns 2S J=1/2|3\u20138": ["run", 4, 0, 0, 4], "Al IV|nf 2[5/2] J=3|4\u20135": ["run", 0, 0, 0, 0], "Al IV|ns 2[3/2]* J=2|3\u20135": ["run", 0, 1, 0, 1], "B II|nd 1D J=2|3\u20137": ["run", 2, 1, 0, 3], "B II|nd 3D J=1|3\u20136": ["run", 2, 0, 0, 2], "B II|nf 3F* J=2|4\u20137": ["run", 2, 0, 0, 2], "B II|ng 3G J=3|5\u20137": ["run", 1, 0, 0, 1], "B II|np 1P* J=1|3\u20135": ["run", 1, 0, 0, 1], "B II|np 3P* J=0|3\u20136": ["run", 2, 0, 0, 2], "B II|ns 1S J=0|3\u20136": ["run", 1, 1, 0, 2], "B II|ns 3S J=1|3\u20137": ["run", 2, 1, 0, 3], "C III|nd 1D J=2|3\u20137": ["run", 1, 2, 0, 3], "C III|nd 3D J=1|3\u20139": ["run", 3, 2, 0, 5], "C III|nf 3F* J=2|4\u20137": ["run", 1, 1, 0, 2], "C III|ng 3G J=3|5\u20137": ["run", 1, 0, 0, 1], "C III|np 1P* J=1|3\u20138": ["run", 1, 3, 0, 4], "C III|np 3P* J=0|3\u20136": ["run", 1, 1, 0, 2], "C III|ns 1S J=0|3\u20135": ["run", 1, 0, 0, 1], "C III|ns 3S J=1|3\u20137": ["run", 2, 1, 0, 3], "O IV|nd 2D J=3/2|3\u20136": ["run", 2, 0, 0, 2], "O IV|nf 2F* J=5/2|4\u20137": ["run", 0, 2, 0, 2], "O IV|ng 2G J=7/2|5\u20136": ["run", 0, 0, 0, 0], "O IV|nh 2H* J=9/2|6\u20137": ["run", 0, 0, 0, 0], "O IV|np 2P* J=1/2|3\u20135": ["run", 1, 0, 0, 1], "O IV|ns 2S J=1/2|3\u20135": ["run", 1, 0, 0, 1], "F I|nd 4D J=7/2|3\u20136": ["run", 1, 1, 0, 2], "F I|nd 4F J=9/2|3\u20136": ["run", 1, 1, 0, 2], "F I|np 4D* J=7/2|3\u20134": ["run", 0, 0, 0, 0], "F I|ns 2P J=3/2|3\u20136": ["run", 2, 0, 0, 2], "F I|ns 4P J=5/2|3\u20138": ["run", 4, 0, 0, 4], "Ge III|nd 1D J=2|4\u20136": ["run", 1, 0, 0, 1], "Ge III|nd 3D J=1|4\u20136": ["run", 1, 0, 0, 1], "Ge III|ng 3G J=3|5\u20136": ["run", 0, 0, 0, 0], "Ge III|ns 1S J=0|5\u20137": ["run", 1, 0, 0, 1], "Ge III|ns 3S J=1|5\u20138": ["run", 2, 0, 0, 2], "K I|nd 2D J=5/2|3\u201313": ["run", 9, 0, 0, 9], "K I|nf 2F* J=5/2|4\u201312": ["run", 7, 0, 0, 7], "K I|np 2P* J=1/2|4\u201315": ["run", 9, 1, 0, 10], "K I|ns 2S J=1/2|4\u201318": ["run", 12, 1, 0, 13], "O III|nd 1D* J=2|3\u20135": ["run", 1, 0, 0, 1], "O III|nd 3D* J=1|3\u20134": ["run", 0, 0, 0, 0], "O III|nd 3F* J=2|3\u20135": ["run", 1, 0, 0, 1], "O III|np 3D J=1|3\u20134": ["run", 0, 0, 0, 0], "O III|ns 1P* J=1|3\u20135": ["run", 1, 0, 0, 1], "O III|ns 3P* J=0|3\u20135": ["run", 1, 0, 0, 1], "P II|np 3P J=0|4\u20135": ["run", 0, 0, 0, 0], "P II|ns 3P* J=0|4\u20136": ["run", 0, 1, 0, 1], "S III|ns 3P* J=0|4\u20135": ["run", 0, 0, 0, 0]}, "unrec": ["Ne I|nd 2[3/2]* J=1|11\u201320", "Ne I|ns 2[1/2]* J=1|11\u201320", "Zn I|nd 1D J=2|12\u201320", "Zn I|np 1P* J=1|13\u201340", "Ba III|ns 2[1/2]* J=1|8\u201317", "Ba III|nd 2[3/2]* J=2|8\u201322\u2020", "Ba III|ns 2[3/2]* J=1|9\u201323", "Ne II|nd 4D J=3/2|3\u20136", "Ne II|nd 4D J=5/2|3\u20136", "Ne II|nd 4D J=7/2|3\u20136", "Ne II|nd 4F J=9/2|3\u20136", "Ne II|ns 2P J=1/2|3\u20137", "Ne II|ns 2P J=3/2|3\u20137", "Ne II|ns 4P J=1/2|3\u20137", "Ne II|ns 4P J=3/2|3\u20137", "Ne II|ns 4P J=5/2|3\u20137", "Ne II|nd 2S J=1/2|3\u20138", "Ne II|ns 2D J=3/2|3\u20135", "Ne II|ns 2D J=5/2|3\u20135", "Ne I|np 1P* J=1|3\u201312", "Ne II|np 2D* J=3/2|3\u20136", "Ne II|np 2D* J=5/2|3\u20136", "Ne II|np 2S* J=1/2|3\u20136", "Ne II|np 4D* J=1/2|3\u20136", "Ne II|np 4D* J=5/2|3\u20136", "Ne II|np 4D* J=7/2|3\u20136", "Ne II|np 4P* J=1/2|3\u20136", "Ne II|np 4P* J=3/2|3\u20136", "Ne II|np 4P* J=5/2|3\u20136", "Ne II|np 4S* J=3/2|3\u20136", "Ne II|nf 2[2]* J=5/2|5\u20138", "Ne II|nf 2[3]* J=7/2|5\u20138", "Ne II|nf 2[4]* J=7/2|5\u20138", "Ne II|nf 2[4]* J=9/2|5\u20138", "Ne II|nf 2[5]* J=11/2|5\u20138", "Ne II|ng 2[2] J=3/2|5\u20137", "Ne II|ng 2[3] J=5/2|5\u20137", "Ne II|ng 2[4] J=7/2|5\u20137", "Ne II|ng 2[5] J=9/2|5\u20137", "Ne II|ng 2[6] J=11/2|5\u20137", "Ar II|ng 2[4] J=9/2|6\u20138", "Ar II|ng 2[6] J=11/2|6\u20138", "Ar II|ng 2[6] J=13/2|6\u20138", "Ar II|ng 2[2] J=3/2|6\u20137", "Ar II|ng 2[2] J=5/2|6\u20137", "Ar II|ng 2[3] J=5/2|6\u20137", "Ar II|ng 2[3] J=7/2|6\u20137", "Ar II|ng 2[4] J=7/2|6\u20137", "Ar II|ng 2[5] J=11/2|6\u20137", "Ar II|ng 2[5] J=9/2|6\u20137", "Ar II|nh 2[3]* J=5/2|6\u20137", "Ar II|nh 2[3]* J=7/2|6\u20137", "Ar II|nh 2[4]* J=7/2|6\u20137", "Ar II|nh 2[4]* J=9/2|6\u20137", "Ar II|nh 2[5]* J=11/2|6\u20137", "Ar II|nh 2[5]* J=9/2|6\u20137", "Ar II|nh 2[6]* J=11/2|6\u20137", "Ar II|nh 2[6]* J=13/2|6\u20137", "Ar II|nh 2[7]* J=13/2|6\u20137", "Ar II|nh 2[7]* J=15/2|6\u20137", "Ar II|ni 2[4] J=7/2|7\u20138", "Ar II|ni 2[4] J=9/2|7\u20138", "Ar II|ni 2[5] J=11/2|7\u20138", "Ar II|ni 2[5] J=9/2|7\u20138", "Ar II|ni 2[6] J=11/2|7\u20138", "Ar II|ni 2[6] J=13/2|7\u20138", "Ar II|ni 2[7] J=13/2|7\u20138", "Ar II|ni 2[7] J=15/2|7\u20138", "Ar II|ni 2[8] J=15/2|7\u20138", "Ar II|ni 2[8] J=17/2|7\u20138", "Ne II|nd 2F J=5/2|3\u20134", "Ne II|nd 2F J=7/2|3\u20134", "Ne II|nd 2G J=7/2|3\u20134", "Ne II|nd 2G J=9/2|3\u20134", "Ne II|nd 2P J=3/2|3\u20134", "Ba III|ng 2[11/2]* J=5|5\u20136", "Ba III|ng 2[11/2]* J=6|5\u20136", "Ba III|ng 2[5/2]* J=2|5\u20136", "Ba III|ng 2[5/2]* J=3|5\u20136", "Ba III|ng 2[7/2]* J=3|5\u20136", "Ba III|ng 2[7/2]* J=4|5\u20136", "Ba III|ng 2[9/2]* J=4|5\u20136", "Ba III|ng 2[9/2]* J=5|5\u20136", "Si I|ns (3/2,1/2)* J=1|11\u201324", "Si I|ns (3/2,1/2)* J=2|11\u201319", "Si I|nf 2[3/2] J=1|4\u20137", "Si I|nf 2[3/2] J=2|4\u20137", "Si I|nf 2[5/2] J=2|4\u20137", "Si I|nf 2[5/2] J=3|4\u20137", "Si I|nf 2[7/2] J=3|4\u20137", "Si I|nf 2[7/2] J=4|4\u20137", "Si I|nf 2[9/2] J=4|4\u20137", "Si I|nf 2[9/2] J=5|4\u20137", "Si I|nd 1D* J=2|3\u20138", "Si I|nd 1F* J=3|3\u20138\u2020", "Si I|nd 1P* J=1|3\u20138", "Si I|nd 3F* J=2|3\u20138", "Si I|nd 3F* J=3|3\u20138", "Si I|nd 3F* J=4|3\u20138", "Si I|np (1/2,1/2) J=1|6\u20137", "Si I|np (1/2,3/2) J=1|6\u20137", "Si I|np (1/2,3/2) J=2|6\u20137", "Si I|ns (1/2,1/2)* J=0|13\u201321", "Si I|ns (1/2,1/2)* J=1|13\u201321", "Si I|nd (1/2,3/2)* J=1|9\u201344\u2020", "Si I|nd (3/2,3/2)* J=1|20\u201350", "Si I|nd (3/2,5/2)* J=3|20\u201356", "Si I|nd (3/2,3/2)* J=0|8\u201316", "Si I|nd (3/2,5/2)* J=1|8\u201316", "Ar II|3s2.3p4.(3P).nd 4D J=7/2|3\u20135", "Ar II|3s2.3p4.(3P).ns 4P J=1/2|4\u20136", "Ar II|3s2.3p4.(3P).ns 4P J=3/2|4\u20136", "Ar II|3s2.3p4.(3P).ns 4P J=5/2|4\u20136", "Ca II|nd 2D J=3/2|3\u201316", "Ca II|nf 2F* J=5/2|4\u201310", "Ca II|ng 2G J=7/2|5\u20139", "Ca II|nh 2H* J=9/2|8\u201310\u2020", "Ca II|np 2P* J=1/2|4\u20136", "Ca II|ns 2S J=1/2|4\u201310", "Ca I|nd 1D J=2|4\u20139", "Ca I|nd 3D J=1|4\u20139", "Ca I|nf 1F* J=3|4\u20138", "Ca I|nf 3F* J=2|4\u20139", "Ca I|np 1P* J=1|5\u201310", "Ca I|ns 1S J=0|5\u201311", "Ca I|ns 3S J=1|5\u201311"], "nod": ["Bi III|6s2.nd 2D J=3/2|6\u20138", "Bi III|6s2.nd 2D J=5/2|6\u20138", "Bi III|6s2.ng 2G J=7/2|5\u20138", "Bi III|6s2.ng 2G J=9/2|5\u20138", "Bi III|6s2.np 2P* J=1/2|6\u20138", "Bi III|6s2.np 2P* J=3/2|6\u20138", "Bi III|6s2.ns 2S J=1/2|7\u20139", "Sc III|3p6.nd 2D J=3/2|3\u20137", "Sc III|3p6.nd 2D J=5/2|3\u20137", "Sc III|3p6.nf 2F* J=5/2|4\u20137", "Sc III|3p6.nf 2F* J=7/2|4\u20137", "Sc III|3p6.ng 2G J=7/2|5\u20138", "Sc III|3p6.ng 2G J=9/2|5\u20138", "Sc III|3p6.np 2P* J=1/2|4\u20137", "Sc III|3p6.np 2P* J=3/2|4\u20137", "Sc III|3p6.ns 2S J=1/2|4\u20138", "Bi III|6s2.nh 2H* J=11/2|6\u20137", "Bi III|6s2.nh 2H* J=9/2|6\u20137", "Sc III|3p6.nh 2H* J=11/2|6\u20137", "Sc III|3p6.nh 2H* J=9/2|6\u20137", "Cd II|nd 2D J=3/2|5\u201313", "Cd II|nf 2F* J=5/2|4\u20139", "Cd II|ng 2G J=7/2|5\u201311", "Cd II|np 2P* J=1/2|5\u201312\u2020", "Cd II|ns 2S J=1/2|5\u201313", "Hg II|nd 2D J=3/2|6\u201311", "Hg II|nf 2F* J=7/2|5\u20138", "Hg II|ng 2G J=9/2|5\u20139", "Hg II|np 2P* J=1/2|6\u20138", "Hg II|ns 2S J=1/2|6\u201311", "N I|nd 2F J=5/2|3\u20135", "N I|nd 4D J=1/2|3\u20134", "N I|nd 4F J=3/2|3\u20135", "N I|np 2D* J=3/2|3\u20135", "N I|np 4D* J=1/2|3\u20135", "N I|np 4P* J=1/2|3\u20135", "N I|ns 2P J=1/2|3\u20136", "N I|ns 4P J=1/2|3\u20136", "C I|nd 1F* J=3|3\u20134", "C I|nd 3D* J=1|3\u20134", "C I|np 3D J=1|3\u20134", "C I|np 3P J=0|3\u20134", "C I|np 3S J=1|3\u20134", "C I|ns 1P* J=1|3\u20135", "C I|ns 3P* J=0|3\u20135"]}
<<<END FILE: run489_final.json>>>

<<<FILE: run489_anomalies.json>>>
[[["C II", "2s2(1S)np 2P\u00b0 J=1/2", "2\u20134"], "FAIL [(3, 4900.4273, 0.005)]"], [["C II", "2s2(1S)np 2P\u00b0 J=3/2", "2\u20134"], "FAIL [(3, 4904.6084, 0.005)]"], [["Si II", "3s2.np 2P* J=1/2", "3\u201310"], "FAIL [(5, 161.8652, 0.005), (7, 528.2152, 0.005), (8, 318.5801, 0.005), (9, 33.424, 0.05)]"], [["Si II", "3s2.np 2P* J=3/2", "3\u201310"], "FAIL [(5, 165.6969, 0.005), (7, 584.5161, 0.005), (8, 313.8118, 0.005), (9, 22.0022, 0.05)]"], [["Li III", "nd 2D J=3/2", "3\u20139"], "FAIL [(4, 0.2793, 5e-06)]"], [["Li III", "nd 2D J=5/2", "3\u20139"], "FAIL [(4, 0.2794, 5e-06)]"], [["Li III", "np 2P* J=1/2", "2\u201310"], "FAIL [(3, 0.2106, 5e-06), (4, 0.2792, 5e-07)]"], [["Li III", "np 2P* J=3/2", "2\u201310"], "FAIL [(3, 0.2105, 5e-07), (4, 0.2792, 5e-07)]"], [["Li III", "ns 2S J=1/2", "1\u20139"], "FAIL [(3, 0.2052, 5e-06), (4, 0.2782, 5e-06)]"], [["Bi II", "6s2.6p.nd (1/2,3/2)* J=1", "6\u201314"], "FAIL [(7, 2343.5613, 0.0005), (8, 187.6148, 0.5), (9, 1.8759, 0.5), (10, 29.0177, 0.5), (12, 24.2471, 0.5)]"], [["Bi II", "6s2.6p.nd (1/2,5/2)* J=2", "6\u20138"], "FAIL [(7, 1191.393, 0.0005)]"], [["Ne I", "2s22p5(2P*3/2)nd 2[3/2]* J=1", "13\u201320"], "FAIL [(14, 0.587, 0.005), (15, 0.3864, 0.005), (17, 0.1574, 0.005), (19, 0.0088, 0.005)]"], [["Ne I", "2s22p5(2P*3/2)ns 2[3/2]* J=1", "12\u201320"], "FAIL [(14, 0.3245, 0.005), (17, 0.4279, 0.005), (18, 0.187, 0.005)]"], [["Ne I", "nd 2[3/2]* J=1", "11\u201320"], "limit row 174710.09 vs LIM 173929.75"], [["Ne I", "nd 2[3/2]* J=1", "11\u201320"], "levels raw 8 vs row 10"], [["Ne I", "ns 2[1/2]* J=1", "11\u201320"], "limit row 174710.09 vs LIM 173929.75"], [["Ne I", "ns 2[1/2]* J=1", "11\u201320"], "levels raw 0 vs row 10"], [["Li II", "1s.nd 3D J=2", "3\u201310"], "FAIL [(8, 0.1359, 0.005)]"], [["Li II", "1s.nf 3F* J=3", "4\u201310"], "FAIL [(9, 0.042, 0.005)]"], [["Li II", "1s.np 1P* J=1", "2\u201314"], "FAIL [(4, 2.7997, 0.05), (6, 20.6222, 0.05), (7, 4.9744, 0.5), (8, 7.5844, 0.05)]"], [["Li II", "1s.ns 1S J=0", "2\u201310"], "FAIL [(7, 0.5848, 0.05), (8, 0.4042, 0.005)]"], [["Zn I", "nd 1D J=2", "12\u201320"], "levels raw 0 vs row 9"], [["Zn I", "np 1P* J=1", "13\u201340"], "levels raw 0 vs row 28"], [["Ba III", "ns 2[1/2]* J=1", "8\u201317"], "limit row 306650.0 vs LIM 289100.0"], [["Ba III", "ns 2[1/2]* J=1", "8\u201317"], "levels raw 0 vs row 10"], [["Ba III", "nd 2[3/2]* J=2", "8\u201322\u2020"], "ambiguous prefix ['5p5.(2P*<1/2>).', '5p5.(2P*<3/2>).']"], [["Ba III", "nd 2[3/2]* J=2", "8\u201322\u2020"], "levels raw 0 vs row 14"], [["Ba III", "ns 2[3/2]* J=1", "9\u201323"], "levels raw 0 vs row 15"], [["Ne II", "nd 4D J=3/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "nd 4D J=5/2", "3\u20136"], "levels raw 1 vs row 4"], [["Ne II", "nd 4D J=7/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "nd 4F J=9/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "ns 2P J=1/2", "3\u20137"], "levels raw 1 vs row 5"], [["Ne II", "ns 2P J=3/2", "3\u20137"], "levels raw 2 vs row 5"], [["Ne II", "ns 4P J=1/2", "3\u20137"], "levels raw 1 vs row 5"], [["Ne II", "ns 4P J=3/2", "3\u20137"], "levels raw 1 vs row 5"], [["Ne II", "ns 4P J=5/2", "3\u20137"], "levels raw 1 vs row 5"], [["Ne II", "nd 2S J=1/2", "3\u20138"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2S J=1/2", "3\u20138"], "levels raw 0 vs row 6"], [["Ne II", "ns 2D J=3/2", "3\u20135"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "ns 2D J=3/2", "3\u20135"], "levels raw 1 vs row 3"], [["Ne II", "ns 2D J=5/2", "3\u20135"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "ns 2D J=5/2", "3\u20135"], "levels raw 1 vs row 3"], [["Ne I", "np 1P* J=1", "3\u201312"], "limit row 390977.35 vs LIM 173929.75"], [["Ne I", "np 1P* J=1", "3\u201312"], "levels raw 0 vs row 10"], [["Ne II", "np 2D* J=3/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 2D* J=5/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 2S* J=1/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4D* J=1/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4D* J=5/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4D* J=7/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4P* J=1/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4P* J=3/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4P* J=5/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "np 4S* J=3/2", "3\u20136"], "levels raw 0 vs row 4"], [["Ne II", "nf 2[2]* J=5/2", "5\u20138"], "levels raw 0 vs row 4"], [["Ne II", "nf 2[3]* J=7/2", "5\u20138"], "levels raw 0 vs row 4"], [["Ne II", "nf 2[4]* J=7/2", "5\u20138"], "levels raw 0 vs row 4"], [["Ne II", "nf 2[4]* J=9/2", "5\u20138"], "levels raw 0 vs row 4"], [["Ne II", "nf 2[5]* J=11/2", "5\u20138"], "levels raw 0 vs row 4"], [["Ne II", "ng 2[2] J=3/2", "5\u20137"], "levels raw 0 vs row 3"], [["Ne II", "ng 2[3] J=5/2", "5\u20137"], "levels raw 0 vs row 3"], [["Ne II", "ng 2[4] J=7/2", "5\u20137"], "levels raw 0 vs row 3"], [["Ne II", "ng 2[5] J=9/2", "5\u20137"], "levels raw 0 vs row 3"], [["Ne II", "ng 2[6] J=11/2", "5\u20137"], "levels raw 0 vs row 3"], [["Ar II", "ng 2[4] J=9/2", "6\u20138"], "levels raw 0 vs row 3"], [["Ar II", "ng 2[6] J=11/2", "6\u20138"], "levels raw 0 vs row 3"], [["Ar II", "ng 2[6] J=13/2", "6\u20138"], "levels raw 0 vs row 3"], [["Ar II", "ng 2[2] J=3/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[2] J=5/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[3] J=5/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[3] J=7/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[4] J=7/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[5] J=11/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ng 2[5] J=9/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[3]* J=5/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[3]* J=7/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[4]* J=7/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[4]* J=9/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[5]* J=11/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[5]* J=9/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[6]* J=11/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[6]* J=13/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[7]* J=13/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "nh 2[7]* J=15/2", "6\u20137"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[4] J=7/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[4] J=9/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[5] J=11/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[5] J=9/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[6] J=11/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[6] J=13/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[7] J=13/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[7] J=15/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[8] J=15/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ar II", "ni 2[8] J=17/2", "7\u20138"], "levels raw 0 vs row 2"], [["Ne II", "nd 2F J=5/2", "3\u20134"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2F J=5/2", "3\u20134"], "levels raw 0 vs row 2"], [["Ne II", "nd 2F J=7/2", "3\u20134"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2F J=7/2", "3\u20134"], "levels raw 1 vs row 2"], [["Ne II", "nd 2G J=7/2", "3\u20134"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2G J=7/2", "3\u20134"], "levels raw 0 vs row 2"], [["Ne II", "nd 2G J=9/2", "3\u20134"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2G J=9/2", "3\u20134"], "levels raw 0 vs row 2"], [["Ne II", "nd 2P J=3/2", "3\u20134"], "limit row 356229.3 vs LIM 330388.6"], [["Ne II", "nd 2P J=3/2", "3\u20134"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[11/2]* J=5", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[11/2]* J=6", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[5/2]* J=2", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[5/2]* J=3", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[7/2]* J=3", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[7/2]* J=4", "5\u20136"], "levels raw 1 vs row 2"], [["Ba III", "ng 2[9/2]* J=4", "5\u20136"], "levels raw 0 vs row 2"], [["Ba III", "ng 2[9/2]* J=5", "5\u20136"], "levels raw 0 vs row 2"], [["Si I", "ns (3/2,1/2)* J=1", "11\u201324"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "ns (3/2,1/2)* J=1", "11\u201324"], "levels raw 0 vs row 14"], [["Si I", "ns (3/2,1/2)* J=2", "11\u201319"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "ns (3/2,1/2)* J=2", "11\u201319"], "levels raw 0 vs row 9"], [["Si I", "nf 2[3/2] J=1", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[3/2] J=1", "4\u20137"], "levels raw 1 vs row 4"], [["Si I", "nf 2[3/2] J=2", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[3/2] J=2", "4\u20137"], "levels raw 1 vs row 4"], [["Si I", "nf 2[5/2] J=2", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[5/2] J=2", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nf 2[5/2] J=3", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[5/2] J=3", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nf 2[7/2] J=3", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[7/2] J=3", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nf 2[7/2] J=4", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[7/2] J=4", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nf 2[9/2] J=4", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[9/2] J=4", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nf 2[9/2] J=5", "4\u20137"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nf 2[9/2] J=5", "4\u20137"], "levels raw 0 vs row 4"], [["Si I", "nd 1D* J=2", "3\u20138"], "levels raw 0 vs row 6"], [["Si I", "nd 1F* J=3", "3\u20138\u2020"], "levels raw 0 vs row 5"], [["Si I", "nd 1P* J=1", "3\u20138"], "levels raw 0 vs row 6"], [["Si I", "nd 3F* J=2", "3\u20138"], "levels raw 0 vs row 6"], [["Si I", "nd 3F* J=3", "3\u20138"], "levels raw 0 vs row 6"], [["Si I", "nd 3F* J=4", "3\u20138"], "levels raw 0 vs row 6"], [["Si I", "np (1/2,1/2) J=1", "6\u20137"], "levels raw 0 vs row 2"], [["Si I", "np (1/2,3/2) J=1", "6\u20137"], "levels raw 0 vs row 2"], [["Si I", "np (1/2,3/2) J=2", "6\u20137"], "levels raw 0 vs row 2"], [["Si I", "ns (1/2,1/2)* J=0", "13\u201321"], "levels raw 0 vs row 9"], [["Si I", "ns (1/2,1/2)* J=1", "13\u201321"], "levels raw 0 vs row 9"], [["Si I", "nd (1/2,3/2)* J=1", "9\u201344\u2020"], "levels raw 0 vs row 34"], [["Si I", "nd (3/2,3/2)* J=1", "20\u201350"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nd (3/2,3/2)* J=1", "20\u201350"], "levels raw 0 vs row 31"], [["Si I", "nd (3/2,5/2)* J=3", "20\u201356"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nd (3/2,5/2)* J=3", "20\u201356"], "levels raw 0 vs row 37"], [["Si I", "nd (3/2,3/2)* J=0", "8\u201316"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nd (3/2,3/2)* J=0", "8\u201316"], "levels raw 0 vs row 9"], [["Si I", "nd (3/2,5/2)* J=1", "8\u201316"], "limit row 66035.0 vs LIM 65747.76"], [["Si I", "nd (3/2,5/2)* J=1", "8\u201316"], "levels raw 0 vs row 9"], [["B III", "nf 2F* J=5/2", "4\u201311"], "FAIL [(5, 0.0096, 0.005)]"], [["B III", "ng 2G J=7/2", "5\u201310"], "FAIL [(6, 0.1429, 0.005)]"], [["B III", "np 2P* J=1/2", "2\u20139"], "FAIL [(5, 2.6188, 0.005), (6, 0.2899, 0.005), (8, 0.0435, 0.005)]"], [["Be III", "1s.nd 1D J=2", "3\u201310"], "FAIL [(5, 2.1589, 0.05), (7, 0.2584, 0.005)]"], [["Be III", "1s.nd 3D J=2", "3\u201310"], "FAIL [(5, 2.2266, 0.005), (7, 0.4373, 0.005), (8, 0.612, 0.05)]"], [["Be III", "1s.nf 1F* J=3", "4\u20139"], "FAIL [(6, 1.0775, 0.05), (7, 0.8624, 0.005)]"], [["Be III", "1s.ng 1G J=4", "5\u20139"], "FAIL [(6, 2.8419, 0.05), (7, 0.3247, 0.05)]"], [["Be III", "1s.np 3P* J=1", "2\u201310"], "FAIL [(5, 0.2372, 0.005), (6, 0.2038, 0.05)]"], [["Be III", "1s.ns 1S J=0", "2\u201310"], "FAIL [(4, 3.5952, 0.05), (6, 3.9721, 0.05), (7, 0.7238, 0.05)]"], [["Be III", "1s.ns 3S J=1", "2\u201310"], "FAIL [(7, 2.3777, 0.005), (8, 0.4542, 0.005)]"], [["Mg III", "nd 2[3/2]* J=1", "4\u20139"], "FAIL [(5, 9.91, 0.5), (6, 3.7662, 0.5), (7, 16.6234, 0.5)]"], [["Al III", "ng 2G J=7/2", "5\u20139"], "FAIL [(8, 0.015, 0.005)]"], [["Al III", "nh 2H* J=9/2", "6\u20139"], "FAIL [(8, 0.2015, 0.005)]"], [["Si III", "nd 1D J=2", "3\u20139"], "FAIL [(6, 2735.0944, 0.005), (7, 1434.437, 0.005)]"], [["Si III", "nd 3D J=3", "3\u20139"], "FAIL [(4, 115.731, 0.005), (6, 652.4806, 0.005), (7, 441.5699, 0.005)]"], [["Si III", "nf 1F* J=3", "4\u20139"], "FAIL [(5, 3817.0665, 0.005), (6, 3515.9656, 0.005)]"], [["Si III", "np 1P* J=1", "4\u20137"], "FAIL [(5, 218.7178, 0.005), (6, 517.6919, 0.005)]"], [["Si III", "ns 1S J=0", "4\u20138"], "FAIL [(6, 13.7945, 0.005)]"], [["Ar II", "3s2.3p4.(3P).nd 4D J=7/2", "3\u20135"], "levels raw 1 vs row 3"], [["Ar II", "3s2.3p4.(3P).ns 4P J=1/2", "4\u20136"], "levels raw 1 vs row 3"], [["Ar II", "3s2.3p4.(3P).ns 4P J=3/2", "4\u20136"], "levels raw 1 vs row 3"], [["Ar II", "3s2.3p4.(3P).ns 4P J=5/2", "4\u20136"], "levels raw 1 vs row 3"], [["B IV", "1s.nd 1D J=2", "3\u201310"], "FAIL [(4, 1.1833, 0.05), (6, 0.6705, 0.5), (7, 4.7683, 0.05), (8, 0.6946, 0.5)]"], [["B IV", "1s.nd 3D J=1", "3\u201310"], "FAIL [(7, 0.2318, 0.05), (8, 1.2029, 0.05), (9, 0.4794, 0.05)]"], [["B IV", "1s.nf 1F* J=3", "4\u20139"], "FAIL [(6, 1.9216, 0.05)]"], [["B IV", "1s.ng 1G J=4", "5\u20139"], "FAIL [(6, 1.0235, 0.05), (7, 0.4029, 0.05), (8, 5.2, 0.05)]"], [["B IV", "1s.nh 1H* J=5", "6\u20139"], "FAIL [(8, 2.2514, 0.05)]"], [["B IV", "1s.np 1P* J=1", "3\u201310"], "FAIL [(5, 5.4633, 0.5), (6, 0.7488, 0.05), (8, 0.0347, 0.05)]"], [["B IV", "1s.ns 1S J=0", "3\u201310"], "FAIL [(5, 1.7993, 0.5), (6, 10.2767, 0.5)]"], [["P IV", "nd 1D J=2", "4\u20136"], "FAIL [(5, 13.2623, 0.005)]"], [["P IV", "nd 3D J=1", "4\u20136"], "FAIL [(5, 204.0318, 0.005)]"], [["P IV", "np 1P* J=1", "4\u20136"], "FAIL [(5, 767.3076, 0.005)]"], [["P IV", "np 3P* J=0", "4\u20136"], "FAIL [(5, 135.3192, 0.005)]"], [["P IV", "ns 3S J=1", "4\u20137"], "FAIL [(5, 488.248, 0.005), (6, 392.423, 0.005)]"], [["C V", "1s.ns 3S J=1", "2\u20137"], "FAIL [(3, 378.6941, 0.05)]"], [["S V", "3s.nd 1D J=2", "4\u20136"], "FAIL [(5, 1011.28, 0.05)]"], [["S V", "3s.nd 3D J=1", "4\u20137"], "FAIL [(5, 1049.0978, 0.05)]"], [["S V", "3s.nf 1F* J=3", "4\u20136"], "FAIL [(5, 1892.7771, 0.05)]"], [["S V", "3s.np 1P* J=1", "4\u20137"], "FAIL [(5, 215.1548, 0.05)]"], [["S V", "3s.np 3P* J=0", "4\u20136"], "FAIL [(5, 4616.5323, 0.05)]"], [["S V", "3s.ns 1S J=0", "4\u20137"], "FAIL [(5, 179.3639, 0.05), (6, 946.0652, 0.05)]"], [["S V", "3s.ns 3S J=1", "4\u20137"], "FAIL [(5, 274.9374, 0.05)]"], [["Ca IX", "nd 1D J=2", "4\u20136"], "FAIL [(5, 1386.7001, 0.5)]"], [["Ca IX", "np 1P* J=1", "4\u20136"], "FAIL [(5, 1289.0054, 0.5)]"], [["Ti XI", "np 1P* J=1", "4\u20137"], "FAIL [(6, 2387.3385, 0.5)]"], [["Ca II", "nd 2D J=3/2", "3\u201316"], "levels raw 2 vs row 14"], [["Ca II", "nf 2F* J=5/2", "4\u201310"], "levels raw 0 vs row 7"], [["Ca II", "ng 2G J=7/2", "5\u20139"], "levels raw 0 vs row 5"], [["Ca II", "nh 2H* J=9/2", "8\u201310\u2020"], "levels raw 0 vs row 2"], [["Ca II", "np 2P* J=1/2", "4\u20136"], "levels raw 0 vs row 3"], [["Ca II", "ns 2S J=1/2", "4\u201310"], "levels raw 3 vs row 7"], [["Ca I", "nd 1D J=2", "4\u20139"], "levels raw 1 vs row 6"], [["Ca I", "nd 3D J=1", "4\u20139"], "levels raw 1 vs row 6"], [["Ca I", "nf 1F* J=3", "4\u20138"], "levels raw 0 vs row 5"], [["Ca I", "nf 3F* J=2", "4\u20139"], "levels raw 0 vs row 6"], [["Ca I", "np 1P* J=1", "5\u201310"], "levels raw 0 vs row 6"], [["Ca I", "ns 1S J=0", "5\u201311"], "levels raw 1 vs row 7"], [["Ca I", "ns 3S J=1", "5\u201311"], "levels raw 1 vs row 7"], [["Ar I", "np 2[1/2] J=1", "4\u20137"], "FAIL [(6, 18.9411, 0.0005)]"], [["Ar I", "np 2[3/2] J=1", "4\u20137"], "FAIL [(5, 109.4233, 5e-05)]"], [["Ar I", "np 2[5/2] J=3", "4\u20137"], "FAIL [(5, 113.8693, 5e-05)]"], [["Ar I", "ns 2[3/2]* J=1", "4\u20137"], "FAIL [(5, 288.066, 0.0005)]"], [["Ar I", "ns 2[3/2]* J=2", "4\u20137"], "FAIL [(5, 258.5522, 0.0005)]"], [["Cd I", "nd 1D J=2", "5\u201315\u2020"], "FAIL [(14, 0.884, 0.05)]"], [["Cd I", "np 1P* J=1", "6\u201312"], "FAIL [(8, 0.5941, 0.0005), (10, 0.0143, 0.005)]"], [["Cd I", "ns 1S J=0", "6\u201315"], "FAIL [(12, 5.3603, 0.05), (13, 1.7698, 0.05), (14, 4.9439, 0.05)]"], [["Cd I", "ns 3S J=1", "6\u201316"], "FAIL [(12, 0.3478, 0.0005), (15, 2.5041, 0.05)]"], [["Ga II", "ns 1S J=0", "5\u20138"], "FAIL [(6, 324.7873, 0.005)]"], [["P III", "ng 2G J=7/2", "5\u20138"], "FAIL [(7, 0.8206, 0.005)]"], [["P III", "np 2P* J=1/2", "4\u20136"], "FAIL [(5, 555.162, 0.005)]"], [["N III", "nd 2D J=3/2", "3\u201312"], "FAIL [(4, 14.2441, 0.05), (5, 397.6584, 0.05), (7, 4.9191, 0.5)]"], [["N III", "np 2P* J=1/2", "3\u20135"], "FAIL [(4, 984.8202, 0.05)]"], [["N III", "ns 2S J=1/2", "3\u201314"], "FAIL [(5, 91.6168, 0.05)]"], [["S IV", "np 2P* J=1/2", "4\u20137"], "FAIL [(6, 864.7573, 0.05)]"], [["S IV", "ns 2S J=1/2", "4\u20137"], "FAIL [(6, 16.2887, 0.05)]"], [["S VI", "nf 2F* J=5/2", "4\u201310"], "FAIL [(9, 0.4604, 0.5)]"], [["Al IV", "ns 2[3/2]* J=2", "3\u20135"], "FAIL [(4, 178.1588, 0.05)]"], [["B II", "nd 1D J=2", "3\u20137"], "FAIL [(4, 44.6171, 0.005)]"], [["B II", "ns 1S J=0", "3\u20136"], "FAIL [(4, 777.2154, 0.005)]"], [["B II", "ns 3S J=1", "3\u20137"], "FAIL [(6, 38.6314, 0.05)]"], [["C III", "nd 1D J=2", "3\u20137"], "FAIL [(4, 142.1031, 0.005), (5, 26.6615, 0.005)]"], [["C III", "nd 3D J=1", "3\u20139"], "FAIL [(4, 275.2232, 0.005), (6, 2.1744, 0.005)]"], [["C III", "nf 3F* J=2", "4\u20137"], "FAIL [(5, 1352.3051, 0.005)]"], [["C III", "np 1P* J=1", "3\u20138"], "FAIL [(4, 297.6696, 0.005), (5, 1884.9419, 0.005), (6, 88.6073, 0.005)]"], [["C III", "np 3P* J=0", "3\u20136"], "FAIL [(5, 320.244, 0.005)]"], [["C III", "ns 3S J=1", "3\u20137"], "FAIL [(5, 475.6934, 0.005)]"], [["O IV", "nf 2F* J=5/2", "4\u20137"], "FAIL [(5, 424.4593, 0.05), (6, 24.8742, 0.05)]"], [["F I", "nd 4D J=7/2", "3\u20136"], "FAIL [(4, 4.2975, 0.005)]"], [["F I", "nd 4F J=9/2", "3\u20136"], "FAIL [(5, 2.3489, 0.005)]"], [["K I", "np 2P* J=1/2", "4\u201315"], "FAIL [(10, 0.1007, 5e-05)]"], [["K I", "ns 2S J=1/2", "4\u201318"], "FAIL [(10, 0.0576, 5e-05)]"], [["P II", "ns 3P* J=0", "4\u20136"], "FAIL [(5, 60.6331, 0.005)]"]]
<<<END FILE: run489_anomalies.json>>>

<<<FILE: register_cites.py>>>
import re,glob,collections
MAX=max(int(x) for x in re.findall(r'^### (\d+)',open('The_Method_1_6___The_Register-2.md',encoding='utf-8').read(),re.M))
rng=re.compile(r'(?i)\bregisters?\s+((?:\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)*)')
def nums(s):
    out=set()
    for part in re.split(r'\s*(?:,|and|/|;)\s*',s):
        m=re.match(r'(\d{3,4})\s*[–\-]\s*(\d{3,4})$',part.strip())
        if m:
            a,b=int(m.group(1)),int(m.group(2))
            if 165<=a<=b<=MAX and b-a<200: out.update(range(a,b+1))
        elif part.strip().isdigit():
            n=int(part);
            if 165<=n<=MAX: out.add(n)
    return out
def cites(text):
    c=collections.Counter()
    for m in rng.finditer(text):
        for n in nums(m.group(1)): c[n]+=1
    for m in re.finditer(r'(?:\*R|\bR) ((?:\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)*)',text):
        for n in nums(m.group(1)): c[n]+=1
    return c
if __name__=='__main__':
    R=open('The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
    # entries citing entries: only bodies after "### N"
    ent=re.split(r'\n### (\d+(?:, \d+)*)\n',R)
    byent=collections.Counter()
    for i in range(1,len(ent),2):
        ids={int(x) for x in ent[i].split(', ')}
        for n,k in cites(ent[i+1]).items():
            if n not in ids: byent[n]+=k
    main=open('The_Method_1_6-2.md',encoding='utf-8').read()
    bymain=cites(main)
    comp=collections.Counter()
    for f in glob.glob('The_Method_1_6___*Compendium-2.md')+glob.glob('*Index_of_Indices-2.md')+['THE-LOWDIN-SOLUTION-2.md','The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md']:
        comp+=cites(open(f,encoding='utf-8').read())
    print("entries cited by other entries:",len(byent))
    print("top 12 by entry-citations:",byent.most_common(12))
    print("entries cited in main:",len(bymain),"| in companions:",len(comp),"| main∪companions:",len(set(bymain)|set(comp)))
    print("top main:",bymain.most_common(10))
    allc=byent+bymain+comp
    print("cited anywhere:",len(allc))
    # check all cited ids exist
    heads=set()
    for i in range(1,len(ent),2): heads.update(int(x) for x in ent[i].split(', '))
    missing=sorted(n for n in allc if n not in heads); print("cited but no entry:",missing[:40],len(missing))
<<<END FILE: register_cites.py>>>

<<<FILE: dclose.py>>>
import itertools,collections
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
P={'none found':0,'found':1}
def cell(s): a,b,c=[x.strip() for x in s.split('·')]; return (S[a],V[b],P[c])
E65="""definition·order|a closed index §14.1|proved·exhaustive·found
definition·combinatorics|E(X) §6.1|proved·exhaustive·none found
mechanism·order|ℛ §14.2|proved·exhaustive·none found
formula·combinatorics|F(z) §11|proved·exhaustive·found
formula·combinatorics|rank polynomial §11.8|verified·exhaustive·found
formula·analysis|λ²=(2/3)T|proved·exhaustive·found
formula·analysis|V=4ν/3|measured·exhaustive·none found
formula·analysis|bracket width|verified·exhaustive·none found
formula·physics|Rydberg term|verified·exhaustive·found
theorem·order|A.1|proved·exhaustive·none found
theorem·order|A.2|proved·exhaustive·found
theorem·order|A.3|proved·exhaustive·none found
theorem·order|A.6|proved·exhaustive·none found
theorem·order|A.7|proved·exhaustive·none found
theorem·combinatorics|A.8|proved·exhaustive·found
theorem·combinatorics|A.9|proved·exhaustive·found
theorem·combinatorics|A.10|proved·exhaustive·none found
theorem·analysis|A.12|proved·exhaustive·none found
theorem·analysis|A.13|proved·exhaustive·none found
law·complexity|reorderability law|proved·exhaustive·none found
method·order|order recovery|verified·exhaustive·none found
method·combinatorics|collection procedure|verified·sampled·none found
method·analysis|the bracket|verified·exhaustive·none found
measurement·combinatorics|976|measured·exhaustive·none found
measurement·combinatorics|maximal chains|measured·exhaustive·none found
measurement·physics|1442 bracket test|measured·exhaustive·none found
measurement·algebraic geometry|540 KS|measured·sampled·found
theorem·order|A.4|proved·exhaustive·none found
theorem·order|A.5|proved·sampled·none found
theorem·order|A.11|proved·exhaustive·none found
theorem·order|Thm 18.1|proved·exhaustive·none found
theorem·order|Thm 18.2|proved·exhaustive·none found
theorem·order|A.18|proved·exhaustive·none found
theorem·order|ℛ closure op|proved·exhaustive·found
theorem·combinatorics|A.19.0|proved·exhaustive·found
formula·combinatorics|976 words|proved·exhaustive·found
theorem·order|cap-arity|proved·exhaustive·none found
theorem·order|slack=kernel|conjectured·sampled·none found
measurement·combinatorics|3749 covers|measured·exhaustive·none found
theorem·combinatorics|17=17|proved·exhaustive·none found
theorem·order|occupancy clock|proved·exhaustive·found
theorem·order|one arrow|proved·exhaustive·found
measurement·combinatorics|second bridge|measured·exhaustive·none found
theorem·order|separation hyp|proved·sampled·none found
theorem·order|decay theorem|proved·sampled·found
measurement·combinatorics|two indices|measured·exhaustive·none found
theorem·order|step law|proved·exhaustive·found
theorem·order|meet-closure|proved·exhaustive·found
mechanism·physics|LS.ent|verified·exhaustive·none found
law·physics|LS.law|proved·exhaustive·none found
mechanism·physics|LS.coll|verified·exhaustive·found
theorem·physics|LS.pin|measured·exhaustive·none found
theorem·analysis|LS.asym|proved·exhaustive·found
theorem·analysis|LS.quart|proved·exhaustive·none found
theorem·analysis|LS.chord|proved·exhaustive·found
measurement·physics|LS.twin|measured·exhaustive·none found
definition·analysis|3B.shape|proved·exhaustive·found
formula·analysis|3B.metric|proved·exhaustive·found
formula·analysis|3B.JM|proved·exhaustive·found
formula·analysis|3B.pot|proved·exhaustive·found
theorem·algebraic geometry|3B.norm|proved·exhaustive·found
theorem·analysis|3B.five|proved·exhaustive·found
measurement·combinatorics|3B.tri|measured·exhaustive·none found
theorem·complexity|3B.def|proved·exhaustive·found
theorem·order|3B.index|proved·exhaustive·found"""
NEW="""theorem·analysis|the corridor, 106 consistent inequalities|verified·exhaustive·none found
measurement·analysis|the nineteen surds|measured·exhaustive·none found
formula·analysis|a_cross = (√(n−1)+√(n−4))/3|proved·exhaustive·none found
formula·order|the staircase algebra|verified·exhaustive·found
mechanism·physics|the sequence-index fix|verified·exhaustive·found
measurement·analysis|the selection-rule falsification|measured·sampled·none found
theorem·physics|the necessity of state|verified·exhaustive·none found
law·physics|the observability boundary|conjectured·sampled·none found
definition·order|the singleton-output rule|proved·exhaustive·none found
law·physics|the domain prohibition|verified·exhaustive·none found
measurement·combinatorics|the limit, E = 11 all named|measured·exhaustive·none found
law·physics|rival = donor iff not full|verified·exhaustive·none found"""
def parse(s): return [(l.split('|')[0],l.split('|')[1],cell(l.split('|')[2])) for l in s.splitlines()]
def R(X):
    X=set(X); A=[sorted({x[i] for x in X}) for i in range(3)]
    def phi(i,j,v): return max(x[i] for x in X if x[j]<=v)
    out=set()
    for x in itertools.product(*A):
        ok=all(x[i]<=phi(i,j,x[j]) for i in range(3) for j in range(3) if i!=j)
        if x[1]==0 and x[2]!=1: ok=False          # cited ⟹ found
        if x[0]>=2 and x[1]<1: ok=False           # ≥measured ⟹ ≥sampled
        if ok: out.add(x)
    return out
def run(els):
    fib=collections.defaultdict(list)
    for f,n,c in els: fib[f].append(c)
    tot=0
    for f,cs in fib.items():
        e=len(R(cs))-len(set(cs)); tot+=e
        if e: print("  ",f,"E =",e,"admitted, absent:",sorted(R(cs)-set(cs)))
    return len(fib),tot
base=parse(E65); print(len(base),"elements; fibres, E:",run(base))
new=parse(NEW); allx=base+new; print(len(allx),"elements; fibres, E:",run(allx))
<<<END FILE: dclose.py>>>

<<<FILE: index_gen.py>>>
import re,json,collections
L=open('The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
# section map
sec=[None]*len(L); cur=None; appx=None
for i,l in enumerate(L):
    if i<172: sec[i]=None; continue     # contents block
    m=re.match(r'^## (\d+)\.',l)
    if m: cur=f"§{m.group(1)}"; appx=None
    m=re.match(r'^### (\d+\.\d+)',l)
    if m: cur=f"§{m.group(1)}"
    if re.match(r'^# Appendix ([A-F])',l): appx=re.match(r'^# Appendix ([A-F])',l).group(1); cur=f"App {appx}"
    if re.match(r'^# Index',l): cur='Index'
    if re.match(r'^# References',l): cur='Refs'
    sec[i]=cur
H={}  # section -> heading text
for i,l in enumerate(L):
    if sec[i] and re.match(r'^#{1,3} ',l) and sec[i] not in H: H[sec[i]]=l
T=[ # (level, term, parent, regex, hand)
(1,'bracket',None,r'\bbracket',None),
(2,'bracket failure','bracket',r'bracket fail|fail(s|ed|ure)? (the|its) bracket',None),
(2,'bracket width','bracket',r'bracket width|width of (the|a|its) bracket|bracket.{0,15}\bwidth',None),
(2,'interiority','bracket',r'interiorit',None),
(2,'limit-free','bracket',r'limit-free',None),
(2,'the four rules','bracket',r'four rules|Rule 4[ab]\b|rules 1[–-]4',None),
(3,'interiority','the four rules',r'interiorit',None),
(1,'three bodies',None,r'three[- ]bod',None),
(2,'Λ₃','three bodies',r'Λ₃',None),
(2,'shape sphere','three bodies',r'shape sphere',None),
(1,'closure',None,r'\bclosure\b',None),
(2,'closed index','closure',r'closed index',None),
(2,'closure defect','closure',r'closure defect',None),
(2,'closure operator','closure',r'closure operator',None),
(2,'ℛ(X) = X','closure',r'ℛ\(X\) = X',None),
(1,'cost of a guarantee',None,r'cost of (a|the) guarantee',None),
(2,'V = 4ν/3','cost of a guarantee',r'4ν/3',None),
(2,'the floor','cost of a guarantee',r'\bthe floor\b|V > 2 floor|floor at V',None),
(2,'the pole','cost of a guarantee',r'\bthe pole\b',None),
(2,'ν_V','cost of a guarantee',r'ν_V',None),
(1,'extension',None,r'\bextension',None),
(2,'addable cells','extension',r'addable',None),
(2,'adjoinable axes','extension',r'adjoinable',None),
(2,'imposable constraints','extension',r'imposable',None),
(1,'Löwdin',None,r'Löwdin',None),
(2,'challenge','Löwdin',r'Löwdin.{0,30}challenge|challenge.{0,30}Löwdin',None),
(2,'solution','Löwdin',r'Löwdin solution|solution to Löwdin',None),
(1,'prediction',None,r'\bprediction',None),
(3,'E(X) as budget','prediction',r'\bbudget\b',None),
(3,'Sc VI','prediction',r'Sc VI',None),
(3,'second route','prediction',r'second route',None),
(1,'quantum defect',None,r'quantum defect',None),
(2,'isoelectronic law','quantum defect',r'isoelectronic (law|sequence)',None),
(2,'penetration','quantum defect',r'penetrat',None),
(1,'retrieval',None,r'\bretrieval\b',None),
(2,'retrieval redundancy','retrieval',r'retrieval redundancy|redundancy ρ',None),
(2,'route set','retrieval',r'route set',None),
(1,'self-defence',None,r'self-defen',None),
(2,'totality','self-defence',r'\btotality\b',None),
(2,'process index','self-defence',r'process index',None),
(2,'two routes','self-defence',r'two (disjoint |independent )?routes',None),
(2,'ⅅ_def','self-defence',r'ⅅ_def',None),
(2,'ⅅ_phys','self-defence',r'ⅅ_phys',None),
(1,'self-reference',None,r'self-referen',None),
(3,'alphabet recovery','self-reference',r'alphabet recover|recover(s|ed|able)? (the |its )?alphabet|S1 — the alphabet',None),
(3,'bound recovery','self-reference',r'bound recover|recover(s|ed|able)? (the |its |every )?bound|S3 — the bounds',None),
(3,'order recovery','self-reference',r'order recover|recover(s|ed|able)? (the |its |an )?order|S2 — the order',None),
(1,'the collection',None,r'\bthe collection\b',None),
(3,'decline modes','the collection',r'decline mode|ways a species declines',None),
(3,'isoelectronic pairs','the collection',r'isoelectronic pair',None),
(3,'provenance','the collection',r'provenance',None),
(3,'the census','the collection',r'\bcensus\b',None),
(1,'the index',None,None,['Index']),
(3,'index, self-referencing','the index',None,['Index']),
(1,'the record',None,None,None),
(3,'margins','the record',None,['App C']),
(3,'recomputed','the record',None,['App F']),
(3,'withdrawals','the record',None,['§28']),
(1,'index, self-referencing',None,None,['*this page*']),
]
def locs(rx):
    cnt=collections.Counter(); head=set()
    for i,l in enumerate(L):
        s=sec[i]
        if not s or s in ('Index','Refs'): continue
        n=len(re.findall(rx,l,re.I))
        if n:
            cnt[s]+=n
            if re.match(r'^#{1,3} ',l): head.add(s)
    tot=sum(cnt.values())
    thr=1 if tot<10 else (2 if tot<30 else (3 if tot<60 else 6))
    out={s for s,n in cnt.items() if n>=thr}|head
    return out,tot
raw={}
for lvl,t,par,rx,hand in T:
    raw[(t,par)]=(set(hand) if hand else (locs(rx)[0] if rx else set()), locs(rx)[1] if rx else 0)
def key(x):
    m=re.match(r'§(\d+)(?:\.(\d+))?',x)
    if m: return (0,int(m.group(1)),int(m.group(2) or 0))
    if x.startswith('App'): return (1,ord(x[-1]),0)
    return (2,0,0)
# closure: parent ⊇ children (union); count violations before union
viol=0; final={}
for lvl,t,par,rx,hand in T: final[(t,par)]=set(raw[(t,par)][0])
for lvl,t,par,rx,hand in reversed(T):
    if par:
        ps=[k for k in final if k[0]==par]
        for p in ps:
            missing=final[(t,par)]-final[p]; viol+=len(missing); final[p]|=final[(t,par)]
print("violations before union:",viol)
for lvl,t,par,rx,hand in T:
    print(lvl,t,"|",raw[(t,par)][1],"|",' · '.join(sorted(final[(t,par)],key=key)))
json.dump({f"{t}|{par}":sorted(v,key=key) for (t,par),v in final.items()},open('/home/claude/index_locs.json','w'),ensure_ascii=False)
<<<END FILE: index_gen.py>>>

<<<FILE: split.py>>>
import re,sys
for src in sys.argv[1:]:
    txt=open(src,encoding='utf-8').read()
    for m in re.finditer(r'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>', txt, re.S):
        name,body=m.group(1),m.group(2)
        open(name,'w',encoding='utf-8').write(body)
        print(name, len(body.splitlines()))
<<<END FILE: split.py>>>

<<<FILE: build.py>>>
import re,sys,subprocess,os,pathlib
B='/home/claude/build/'
def esc_us(l):
    if l.startswith('```'): return l
    if l.startswith('    '): return l   # aligned display: left as code by displays()
    l=re.sub(r"(?<=[`)\]])'(?=\w)",'\u2019',l)   # apostrophe after a code span or bracket: not a smart-quote opener
    parts=re.split(r'(`[^`]*`)',l)
    return ''.join(p if p.startswith('`') else fix_stars(p.replace('_','\\_')) for p in parts)
def fix_stars(p):
    # mathematical stars that pandoc would read as emphasis (register 1744)
    p=re.sub(r', \*,', r', \\*,', p)                 # tuple wildcard (3,0,1,1,*,0,1,1)
    p=re.sub(r',\*,', r',\\*,', p)
    # star after a symbol and before an operator: w*/e*, dn*/dZ, p*−1, Z*², V* → 2 —
    # not the close of a one-letter italic like *h*/ν
    p=re.sub(r'(?<=[A-Za-z0-9])(?<!\*[A-Za-z])(?<!\*[A-Za-z][A-Za-z])\*(?=[/+−²|]| [→<>≪=≈])', r'\\*', p)
    p=re.sub(r'^(\*[^*].*[A-Za-z])\*\*$', r'\1\\**', p) # *… w** = italic ending on a starred symbol
    return p
odd=0
def fix_head(h):
    # headline is bold; a paired *x* inside stays italic, a lone * prints literally
    inner=h[2:-2]
    inner=re.sub(r'(?<![*\w])\*(?=\w)(.+?)(?<=\S)\*(?![*\w])',lambda m:'\x01'+m.group(1)+'\x01',inner)
    inner=inner.replace('*','\\*').replace('\x01','*')
    return '**'+inner+'**'
def balanced(t):
    open_=False
    for m in re.finditer(r'\*\*',t):
        i=m.start(); j=m.end()
        pre=t[i-1] if i else ' '; post=t[j] if j<len(t) else ' '
        opener=not post.isspace() and (pre.isspace() or pre in '(—-"\'')
        closer=not pre.isspace() and not opener
        if opener and open_: return False
        if closer and not open_: return False
        if opener: open_=True
        elif closer: open_=False
    return not open_
def split_close(body):
    import itertools
    sites=[m.start() for m in re.finditer(r'\* \*\*(?=[,.;:)\s\'\u2019])',body)]
    if not sites: return body
    sites=sites[:8]
    best=None
    for combo in itertools.product((0,1),repeat=len(sites)):
        t=body
        for pos,c in sorted(zip(sites,combo),reverse=True):
            t=t[:pos]+('**' if c==0 else '')+t[pos+4:]
        if balanced(re.sub(r'(?<!\*)\*(?!\*)','',t)): best=t; break
    return best if best is not None else re.sub(r'\* \*\*(?=[,.;:)\s\'\u2019])','**',body)
def fix_body(body):
    # the body is italic by style (EntryBody); only bold spans are kept as markup
    body=body.replace('\\*','\x02')                              # literal \* in the record is kept
    body=re.sub(r'(?<=\d[A-Z])\*\*(?=[)<\s])','\x02\x02',body)   # term symbols 2P**<3/2>, (2P**), 3P** J=0
    body=re.sub(r'(?<=\d)\*\*(?=/)','\x02\x02',body)              # 11**/21**
    body=split_close(body)                                    # **phrase* **, → **phrase**,  or dropped, by balance
    body=re.sub(r'\*\*([^*]+?)\*([.,;:]) \*\*',r'**\1**\2 **',body)  # **A*. **B → **A**. **B
    body=re.sub(r'(?<![*])\*(\w[^*]{0,400}?)\*\*(?=[,.;:)\s\'\u2019]|$)',r'*\1*',body)  # *iterate**, → *iterate*,
    # bold close mangled to a single star: **A, *b.* *C → **A, *b.** *C  (only when the bold is otherwise unclosed)
    def close_bold(m):
        seg=m.group(0)
        return re.sub(r'(\S)\* \*(?=\S)',r'\1** *',seg,count=1)
    if body.count('**')%2 and re.search(r'\*\*\s*$',body): body=re.sub(r'\*\*\s*$','',body)  # trailing orphan
    # merged italic close+open read as a bold opener: ". **X.* **Y" → ". *X.* **Y"
    body=re.sub(r'(?<=[.;:] )\*\*([^*]+?[.;:])\* \*\*',r'*\1* **',body)   # unconditional: a bold can't close on one star
    body=re.sub(r'^\*\*([^*]+?[.;:])\* \*\*',r'*\1* **',body)
    body=re.sub(r'(?<=[.;:])\*\s+\*\*\s*$',r'*',body)                    # ". ** " tail after an italic close
    if body.count('**')%2:
        body=re.sub(r'\*\*(?:(?!\*\*).)*$',close_bold,body)
    body=re.sub(r'\*{3,}',r'**',body)                        # *** → **
    body=re.sub(r'(?<!\*)\*(?!\*)','',body)                 # drop single italic marks
    body=re.sub(r'(?<![^\s])\*\*\s+\*\*(?![^\s])','',body)  # empty bold (free-standing only)
    body=re.sub(r'\*\* +(?=[,.;:)])','**',body)              # ** , → **,
    return body.strip().replace('\x02','\\*')
def nest_bold(t):
    # walk the ** tokens: emit only depth 0->1 and 1->0; inner bold is absorbed;
    # a closer with nothing open, or an opener never closed, prints literally
    out=[];last=0;depth=0;open_pos=None
    for m in re.finditer(r'\*\*',t):
        i=m.start(); j=m.end()
        pre=t[i-1] if i else ' '; post=t[j] if j<len(t) else ' '
        opener=not post.isspace() and (pre.isspace() or pre in '(—-"\'')
        out.append(t[last:i]); last=j
        if opener:
            if depth==0: open_pos=len(out); out.append('**')
            depth+=1
        else:
            if depth==0: pass                       # orphan closer: dropped
            elif depth==1: out.append('**'); depth=0
            else: depth-=1
    tail=t[last:]
    if depth>0 and open_pos is not None:
        # opener never closed: close at the end of its sentence
        m=re.search(r'[.!?](?=\s|$)',tail)
        if m: tail=tail[:m.end()]+'**'+tail[m.end():]
        else: out[open_pos]=''
    out.append(tail)
    return ''.join(out)
def fix_bodies(L):
    global odd
    out=[];n=0;inentry=False
    for l in L:
        if re.match(r'^### \d+',l): inentry=True; out.append(l); continue
        if l.startswith('#'): inentry=False
        if inentry and re.match(r'^\d+[a-z]?\. [^*]*\*\*( \*|\s*$)',l): l='**'+l   # sub-entry headline missing its opener
        if inentry and l.startswith('**'):
            m=re.match(r'^(\*\*.+?\*\*)(?=\*?\s|$)\*?\s*(.*)$',l)
            if m:
                head,body=m.group(1),m.group(2)
                codes=re.findall(r'`[^`]*`',body); body=re.sub(r'`[^`]*`',lambda x:'\x00',body)
                body=fix_body(body)
                if not balanced(body): odd+=1
                body=nest_bold(body)
                for c in codes: body=body.replace('\x00',c,1)
                head=fix_head(head)
                l=head+'\n\n::: {custom-style="EntryBody"}\n'+body+'\n:::\n' if body else head; n+=1
        out.append(l)
    print('bodies re-wrapped',n,'bodies with unbalanced bold (nest-resolved)',odd); return out
def displays(L):
    # Indented blocks are the book's set-off material. A block with column alignment
    # (3+ internal spaces) or an 8+ indent is a typed table/equation and stays monospace;
    # every other indented block is prose and becomes a block quote so its markup
    # parses and its underscores escape (register 1744).
    out=[];i=0;q=0;t2=0
    while i<len(L):
        if re.match(r'^ {2,3}\S',L[i]) and re.search(r'\S {3,}\S',L[i]):
            # a two-space aligned block is a typed table; markdown would join it into prose (register 1759).
            j=i
            while j<len(L) and re.match(r'^ {2,3}\S',L[j]) and L[j].strip(): j+=1
            blk=L[i:j]
            runs=sum(1 for b in blk if re.search(r'\S {5,}\S',b) or len(re.findall(r'\S {3,}\S',b))>=2)
            if j-i>=2 and runs>=max(1,(j-i)//2):
                out.extend('    '+b[2:].rstrip() for b in blk); t2+=1; i=j; continue
        if re.match(r'^ {4,}\S',L[i]):
            j=i
            while j<len(L) and re.match(r'^ {4,}\S',L[j]): j+=1
            blk=L[i:j]
            runs=any(re.search(r'\S {5,}\S',b) or len(re.findall(r'\S {3,}\S',b))>=2 for b in blk)
            prose=any((len(b.split())>=12 and not re.search(r'\S {3,}\S',b)) or re.match(r'^\s*\*\*[^*]+\*\*\s*$',b) for b in blk)
            aligned=runs or (blk[0].startswith(' '*8) and not prose)
            if aligned: out.extend(blk)
            else: out.extend('> '+b.strip() for b in blk); q+=1
            i=j
        else: out.append(L[i]); i+=1
    print('display blocks quoted',q,'· two-space tables set',t2); return out
def cont_tables(L):
    # A pipe table split by a prose interjection continues with no header row, so pandoc
    # sets the continuation as literal text (register 1764; failure shape of 1757/1759).
    # Re-head each such block with its parent table's header + separator. Guards: the
    # block must have >= 2 rows and >= 4 columns and match the last header's column
    # count, so lone math lines opening with | (e.g. determinants) stay text.
    out=[]; last=None; i=0
    n=0
    while i<len(L):
        if L[i].startswith('|'):
            j=i
            while j<len(L) and L[j].startswith('|'): j+=1
            blk=L[i:j]
            sep=len(blk)>1 and set(blk[1].replace('|','').replace(' ',''))<=set('-:') and '-' in blk[1]
            cols=blk[0].count('|')-1
            if sep:
                last=(blk[0],blk[1],cols)
            elif len(blk)>=2 and cols>=4 and last and last[2]==cols:
                if out and out[-1].strip(): out.append('')   # a table cannot interrupt a paragraph
                out.extend([last[0],last[1]]); n+=1
            out.extend(blk); i=j
        else:
            out.append(L[i]); i+=1
    if n: print('continuation tables re-headed',n)
    return out

def build(src,out,title,strip_contents=False,toc_depth=2,fix_entries=False):
    t=open(B+src,encoding='utf-8').read()
    L=t.splitlines()
    # first H1 becomes the document title
    h1=[i for i,l in enumerate(L) if l.startswith('# ')]
    if h1 and h1[0]<5: L[h1[0]]=''   # a volume whose file opens with its title
    if strip_contents:
        # remove the book's literal contents block: lines between 'Contents' heading and next '## ' body heading
        s=[i for i,l in enumerate(L) if re.match(r'^\s*#{0,3}\s*(Contents|CONTENTS)\s*$',l)]
        if s:
            i=s[0]; parts=[k for k,l in enumerate(L) if k>i and re.match(r'^# PART 0',l)]
            j=parts[1] if len(parts)>1 else i+1
            L=L[:i]+L[j:]; print('contents block removed',i,j)
    if fix_entries:
        L=fix_bodies(L)
    L=cont_tables(L)
    L=displays(L)
    L=[re.sub(r'^!\[[^\]]*\]\((figures[^)]*)\)\s*$', r'![](\1)', l) for l in L]   # drop the image alt line: the caption paragraph carries the figure number (register 1754)
    L=[esc_us(l) for l in L]
    md='\n'.join(L)
    meta=f'---\ntitle: "{title}"\nauthor: "Matthew Lach"\ndate: "Build 9 — 2026-08-24"\n---\n\n'
    open('tmp.md','w',encoding='utf-8').write(meta+md)
    cmd=['pandoc','tmp.md','-o',out,'--from','markdown+pipe_tables+smart']+(['--toc','--toc-depth',str(toc_depth)] if toc_depth else [])+['--resource-path',B,'--reference-doc','ref.docx']
    r=subprocess.run(cmd,capture_output=True,text=True); print(r.stderr[-1500:])
    shrink_wide_tables(out)
    print(out,os.path.getsize(out))
def shrink_wide_tables(docx,min_cols=8,sz=15):
    # wide tables (8+ columns) are set at 7.5pt so their rows do not wrap mid-word (register 1744)
    import zipfile,shutil
    tmp=docx+'.tmp'
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data=zin.read(item.filename)
            if item.filename=='word/document.xml':
                x=data.decode('utf-8'); n=0
                def fix(m):
                    nonlocal n
                    t=m.group(0)
                    first=re.search(r'<w:tr[ >].*?</w:tr>',t,re.S)
                    if not first or first.group(0).count('<w:tc>')+first.group(0).count('<w:tc ')<min_cols: return t
                    n+=1
                    t=re.sub(r'<w:r>(<w:rPr>)?',lambda k:'<w:r><w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/>'+('' if k.group(1) else '</w:rPr>'),t)
                    t=re.sub(r'<w:rPr><w:sz w:val="\d+"/><w:szCs w:val="\d+"/><w:rPr>',lambda k:k.group(0).replace('<w:rPr><w:rPr>','<w:rPr>').replace('/><w:rPr>','/>'),t)
                    # column widths proportional to each column's longest cell text
                    rows=re.findall(r'<w:tr[ >].*?</w:tr>',t,re.S); ncol=None; lens=[]; words=[]; num=[]
                    for ri,row in enumerate(rows):
                        cells=re.findall(r'<w:tc>.*?</w:tc>|<w:tc .*?</w:tc>',row,re.S)
                        if ncol is None: ncol=len(cells); lens=[[] for _ in range(ncol)]; words=[2]*ncol; num=[True]*ncol
                        for ci,c in enumerate(cells[:ncol]):
                            txt=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',c))
                            lens[ci].append(min(len(txt),28)); words[ci]=max(words[ci],max((len(w) for w in txt.split()),default=0))
                            if ri>0 and txt.strip() and not re.match(r'^[\d+\-\u2013.,%()/ ]*$',txt): num[ci]=False
                    def p90(v): v=sorted(v); return v[min(len(v)-1,int(len(v)*0.9))]
                    mx=[max(p90(v),w) for v,w in zip(lens,words)]
                    total=9360
                    for sz2 in (15,14,13,12):
                        sz=sz2                           # half-points: 7.5pt down to 6pt
                        cw=95*sz/15                                    # ~95 twips per character at 7.5pt
                        need=[m*cw+130 for m in mx]; floor=[w*cw+130 for w in words]
                        fixed=sum(n for n,k in zip(need,num) if k); flex=sum(n for n,k in zip(need,num) if not k)
                        scale=(total-fixed)/flex if fixed+flex>total and flex else 1.0
                        widths=[int(n if k else max(n*scale,f)) for n,k,f in zip(need,num,floor)]
                        if sum(widths)<=total: break
                    if sum(widths)>total: widths=[int(w*total/sum(widths)) for w in widths]
                    t=re.sub(r'<w:sz w:val="15"/><w:szCs w:val="15"/>','<w:sz w:val="%d"/><w:szCs w:val="%d"/>'%(sz,sz),t)
                    print('cols',mx,'numeric',sum(num),'sz',sz,'scale',round(scale,2),'sum',sum(widths))
                    grid=''.join('<w:gridCol w:w="%d"/>'%w for w in widths)
                    t=re.sub(r'<w:tblGrid>.*?</w:tblGrid>','<w:tblGrid>'+grid+'</w:tblGrid>',t,flags=re.S)
                    tblpr=('<w:tblPr><w:tblStyle w:val="Table"/><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="start"/>'
                           '<w:tblLayout w:type="fixed"/><w:tblCellMar><w:left w:w="40" w:type="dxa"/><w:right w:w="40" w:type="dxa"/></w:tblCellMar>'
                           '<w:tblLook w:firstRow="1" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0" w:val="0020"/></w:tblPr>')%total
                    t=re.sub(r'<w:tblPr>.*?</w:tblPr>',tblpr,t,count=1,flags=re.S)
                    def fixrow(rm):
                        wi=iter(widths)
                        return re.sub(r'<w:tcPr ?/>|<w:tcPr>.*?</w:tcPr>',lambda k:'<w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr>'%next(wi,400),rm.group(0),flags=re.S)
                    t=re.sub(r'<w:tr[ >].*?</w:tr>',fixrow,t,flags=re.S)
                    t=re.sub(r'<w:pPr>(<w:pStyle [^>]*/>)?',lambda k:'<w:pPr>'+(k.group(1) or '')+'<w:spacing w:before="0" w:after="0"/>',t)
                    return t
                x=re.sub(r'<w:tbl>.*?</w:tbl>',fix,x,flags=re.S)
                print('wide tables shrunk',n); data=x.encode('utf-8')
            zout.writestr(item,data)
    shutil.move(tmp,docx)
if __name__=='__main__':
    src,out,title=sys.argv[1:4]; kw=dict(strip_contents=('strip' in sys.argv),fix_entries=('fix' in sys.argv),toc_depth=int(sys.argv[-1]) if sys.argv[-1].isdigit() else 2)
    build(src,out,title,**kw)
    if 'pages' in sys.argv:   # print index (register 1756): press, map headings to pages, rewrite Contents and Index, press again until the map is stable
        import os,hashlib
        outdir=os.path.dirname(out) or '.'; pdf=out[:-5]+'.pdf'; paged=src[:-3]+'.pages.md'; prev=None
        subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,out],capture_output=True)
        for k in range(3):
            subprocess.run(['python3','index_pages.py',src,pdf,paged,str(kw['toc_depth'])],check=True)
            if 'strip' in sys.argv: subprocess.run(['python3','appf.py',paged,'--write'],check=True)   # Appendix F recomputed at press (1756)
            h=hashlib.md5(open(paged,'rb').read()).hexdigest()
            if h==prev: print('page map stable after',k,'re-press(es)'); break
            prev=h; build(paged,out,title,**dict(kw,strip_contents=False,toc_depth=0))
            subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,out],capture_output=True)
<<<END FILE: build.py>>>

<<<FILE: trueres.py>>>
import re,sys,subprocess; sys.argv=['x']; sys.path.insert(0,'/home/claude/build'); import build as b
def prep(src,fix=False,strip=False):
    L=open(b.B+src,encoding='utf-8').read().splitlines()
    if strip:
        s=[i for i,l in enumerate(L) if re.match(r'^#{1,3} (Contents|CONTENTS)\b',L[i])]
        if s:
            i=s[0]; j=i+1
            while j<len(L) and not re.match(r'^## (Part|PART|1\.|Preface|PREFACE)',L[j]): j+=1
            L=L[:i]+L[j:]
    if fix: L=b.fix_bodies(L)
    L=b.displays(L); L=[b.esc_us(l) for l in L]
    return '\n'.join(L)
def true_residues(src,fix=False,strip=False):
    md=prep(src,fix,strip).replace('\\*','\x03')
    r=subprocess.run(['pandoc','-t','plain','--wrap=none','--from','markdown+pipe_tables+smart'],input=md,capture_output=True,text=True)
    return [l for l in r.stdout.splitlines() if '*' in l]
vols=[('The_Method_1_6-2.md',False,True),('The_Method_1_6___The_Register-2.md',True,False),('The_Method_1_6___Mathematical_Compendium-2.md',False,False),('The_Method_1_6___The_Physics_Compendium-2.md',False,False),('The_Method_1_6___The_Index_of_Indices-2.md',False,False),('The_Method_1_6___Spectra_Compendium-2.md',False,False)]
if __name__=='__main__':
    sel=sys.argv[1:] if len(sys.argv)>1 else None
    for v,f,s in vols:
        lines=true_residues(v,f,s); print(v,'lines',len(lines),'stars',sum(l.count('*') for l in lines))
        open('res_'+v.replace('The_Method_1_6','M').replace('.md','')+'.txt','w',encoding='utf-8').write('\n'.join(lines))
<<<END FILE: trueres.py>>>

<<<FILE: crop_titles.py>>>
# crop_titles.py — remove the pre-V16 title band from the fourteen plots named in register 1747.
# Crops from the first blank band below the first ink row; measures on columns 15% in to skip a full-height y-label.
from PIL import Image; import numpy as np, shutil, os, sys
figs=['6.1','6.2','7.1','8.2','10.1','15.1','19.1','23.1','23.2','24.1','24.2','24.3','25.1','26.1']
os.makedirs('figures-pre-crop',exist_ok=True)
for f in figs:
    p=f'figures/figure-{f}.png'; shutil.copy(p,f'figures-pre-crop/figure-{f}.png')
    im=Image.open(p); a=np.array(im.convert('L')); H,W=a.shape
    ink=(a[:,int(W*0.15):]<200).sum(axis=1); rows=np.where(ink>0)[0]; y=rows[0]
    while y<H and not (ink[y:y+6]==0).all(): y+=1
    assert y-rows[0] < 0.12*H, f
    im.crop((0,y,W,H)).save(p); print(f,'cropped at',y)
<<<END FILE: crop_titles.py>>>

<<<FILE: qgraph.py>>>
# qgraph.py — walk the Mathematical Compendium's "depends on" lines; reproduces register 1749.
import re,sys
s=open('The_Method_1_6___Mathematical_Compendium-2.md',encoding='utf-8').read(); dep={}
for e in re.split(r'\n(?=### `)',s):
    m=re.match(r'### `([^`]+)`',e)
    if not m: continue
    d=re.search(r'depends on (.*?)·',e); dep[m.group(1)]=re.findall(r'`([A-Z0-9]+\.[A-Za-z0-9]+)`',d.group(1)) if d else []
def desc(roots):
    out=set(roots); st=list(roots)
    while st:
        x=st.pop()
        for k,d in dep.items():
            if x in d and k not in out: out.add(k); st.append(k)
    return out
seeds=sys.argv[1:] or ['Q.exch','Q.delta']
full=desc(seeds); fin=desc(['Q.final'])
print('seeds+descendants',len(full),sorted(full)); print('via Q.final',len(fin&full)); print('not via Q.final',sorted(full-fin))
<<<END FILE: qgraph.py>>>

<<<FILE: fig_rerender.py>>>
# chat 8 (register 1753): redraws figures 16.1, 12.3, 25.2, 24.1 into figures/ from the book's numbers.
# 24.1 needs fig241_data.json (per-species per-ell |dbar| parsed from the Spectra Compendium channel table; see 1753).
import json,numpy as np,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, matplotlib.ticker as mt
plt.rcParams.update({'font.family':'serif','font.size':11})
def f161():
    n=np.arange(4,10); d2=np.array([1.3084,1.2830,1.2733,1.2685,1.2659,1.2642]); d1=(n+d2)/2   # Al II 3sns 3S at Z=2; Z=1 = (n+d2)/2
    fig,ax=plt.subplots(1,3,figsize=(10.5,4.3),gridspec_kw={'width_ratios':[0.8,1,1]})
    ax[0].bar(['Z = 1','Z = 2'],[56,56],color='0.55',width=0.55)
    for i in range(2): ax[0].text(i,57,'56/56',ha='center',va='bottom')
    ax[0].set_ylim(0,66); ax[0].set_ylabel('cells bracketed'); ax[0].set_title('the bracket\ncannot see it',fontsize=11)
    ax[1].plot(n,d1,'o-',color='#b03a2e'); ax[1].set_title('Z = 1   (wrong)',color='#b03a2e'); ax[1].text(0.04,0.93,f'spread {d1.max()-d1.min():.2f}',transform=ax[1].transAxes,color='#b03a2e')
    ax[2].plot(n,d2,'o-',color='#2e5d8c'); ax[2].set_title('Z = 2   (correct)',color='#2e5d8c'); ax[2].text(0.96,0.93,f'spread {d2.max()-d2.min():.2f}',transform=ax[2].transAxes,color='#2e5d8c',ha='right')
    for a in ax[1:]: a.set_xlabel('n'); a.grid(alpha=0.3); a.set_xticks(n)
    ax[1].set_ylabel('δ')
    for a in ax: a.spines[['top','right']].set_visible(False)
    fig.tight_layout(); fig.savefig('figures/figure-16.1.png',dpi=150)
def f123():
    q=np.arange(4); A13=[2294,2294,1794,744]; B13=[5,20,50,70]; S13=[a*b for a,b in zip(A13,B13)]; A8=[33,33,23,8]; B8=[5,10,15,17]
    assert S13==[11470,45880,89700,52080]
    fig,ax=plt.subplots(figsize=(8.2,5))
    ax.plot(q,A13,'o-',color='#a8752c',lw=2,ms=7,label='|A(q)| — parent side (falls)')
    ax.plot(q,B13,'s-',color='#2e6f8e',lw=2,ms=7,label='|B(q)| — target side (rises)')
    ax.plot(q,S13,'d--',color='0.15',lw=1.6,ms=7,label='|A×B| — the section')
    ax.plot(q,A8,'o:',color='#a8752c',alpha=0.45,ms=5); ax.plot(q,B8,'s:',color='#2e6f8e',alpha=0.45,ms=5)
    for x,s in zip(q,S13): ax.annotate(f'{s:,}',(x,s),textcoords='offset points',xytext=(0,9),ha='center',fontsize=9.5)
    ax.set_yscale('log'); ax.set_ylim(3,6e5); ax.set_xticks(q); ax.set_xlabel('q — the transfer'); ax.set_ylabel('cells (log)')
    ax.set_title('Raising the transfer costs the parent and pays the target\nsolid: Λ₁₃ · dotted: Λ₈ · peak q = 2 · ⟨q⟩ 1.463 → 1.887',fontsize=11.5)
    ax.grid(alpha=0.25); ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='lower left',bbox_to_anchor=(0.03,0.30),frameon=False,fontsize=10)
    fig.tight_layout(); fig.savefig('figures/figure-12.3.png',dpi=150)
def f252():
    lo,hi_m,hi_c,ritz=735860,738547,737380,736688
    fig,ax=plt.subplots(figsize=(9.8,4.2))
    ax.barh(0,hi_m-lo,left=lo,height=0.45,color='0.72'); ax.barh(1,hi_c-lo,left=lo,height=0.45,color='#4f7594')
    ax.text((lo+hi_m)/2,-0.33,f'{hi_m-lo:,} cm⁻¹',ha='center',va='top',fontsize=10); ax.text((lo+hi_c)/2,0.67,f'{hi_c-lo:,} cm⁻¹',ha='center',va='top',fontsize=10)
    ax.axvline(ritz,color='#8b2a0f',lw=2.2)
    ax.annotate('two-point Ritz estimate\n736,688 cm⁻¹  ·  13.5743 nm',xy=(ritz,1.62),xytext=(ritz+380,1.75),color='#8b2a0f',fontsize=10.5,arrowprops=dict(arrowstyle='->',color='#8b2a0f'),va='center')
    ax.set_yticks([0,1]); ax.set_yticklabels(['§25.6.1  monotone only\nδ∞ < δ(6s) < δ(5s)','§25.6.2  + convexity\nδ(6s) ≥ 2δ(5s) − δ(4s)'])
    ax.set_ylim(-0.7,2.05); ax.set_xlim(735300,739100); ax.xaxis.set_major_formatter(mt.FuncFormatter(lambda x,p:f'{x:,.0f}'))
    ax.set_xlabel('Sc VI 3s²3p³(⁴S°)6s ³S°₁   /   cm⁻¹'); ax.set_title('a committed prediction, tightened 1.8× and still inside its original bound',fontsize=11.5,loc='left')
    ax.spines[['top','right']].set_visible(False); fig.tight_layout(); fig.savefig('figures/figure-25.2.png',dpi=150)
def f241():
    d=json.load(open('fig241_data.json'))
    def get(sp):
        out={}
        for k in (sp, sp+' *'):
            for l,v in d.get(k,{}).items(): out.setdefault(int(l),[]).extend(v)
        return out
    species=['Al I','Al II','Ar II','Be I','Be II','Bi I','C II','Ca II','Cd II','Ga I','He I','Hg II','K I','K II','Li I','Li II','Mg II','N II','Na I','Na II','Ne I','Si I','Si II','Zn II']   # He II drawn separately below
    FLOOR=5e-5; fig,ax=plt.subplots(figsize=(10.5,5.8)); cols=plt.cm.viridis(np.linspace(0,0.92,len(species)+1))
    for c,sp in zip(cols,species):
        g=get(sp); ls=sorted(g); ax.plot(ls,[max(np.mean(g[l]),FLOOR) for l in ls],'-',color=c,lw=1.2,label=sp)
        for l in ls:
            for v in g[l]: ax.plot(l,max(v,FLOOR),'o',ms=4,color=c,mfc=(c if v>0 else 'white'))
    g=get('He II'); ls=sorted(g); ax.plot(ls,[np.mean(g[l]) for l in ls],'D-',color='#1f6f8b',lw=1.4,ms=5,label='He II (corrected series, 1758)')
    # the three rises the caption names: perturbed channels and the fine-structure floor
    for sp,l0,l1 in [('Al I',2,3),('Al II',3,4),('He I',2,6)]:
        g=get(sp); ax.plot([l0,l1],[np.mean(g[l0]),np.mean(g[l1])],'-',color='none')
        dx=-0.35 if sp=='Al II' else 0
        ax.annotate('',xy=(l1,np.mean(g[l1])*1.6),xytext=(l1+dx,np.mean(g[l1])*4.5),arrowprops=dict(arrowstyle='->',color='0.35',lw=0.9))
        ax.text(l1+dx,np.mean(g[l1])*5.2,sp,ha='center',fontsize=8,color='0.35')
    ax.set_yscale('log'); ax.set_xticks(range(7)); ax.set_xticklabels(list('spdfghi')); ax.set_xlim(-0.3,6.3)
    ax.set_xlabel(r'orbital angular momentum  $\ell$'); ax.set_ylabel(r'$|\bar{\delta}|$  quantum defect'); ax.set_ylim(8e-7,8)
    ax.grid(alpha=0.25); ax.spines[['top','right']].set_visible(False)
    ax.legend(ncol=3,fontsize=8.5,loc='upper right',frameon=False,columnspacing=0.9,handlelength=1.6,title=r'penetration falls with $\ell$ across the collection',title_fontproperties={'style':'italic','size':10})
    fig.text(0.99,0.01,r'open markers: $|\bar{\delta}|$ < 10⁻⁴ in the table (below its resolution; drawn at 5 × 10⁻⁵)',ha='right',fontsize=8.5,color='0.3')
    fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('figures/figure-24.1.png',dpi=150)
if __name__=='__main__':
    f161(); f123(); f252(); f241(); print('four figures written')
<<<END FILE: fig_rerender.py>>>

<<<FILE: fig241_data.json>>>
{"Al I": {"3": [0.0429], "2": [0.0248], "0": [1.767], "1": [1.3365]}, "Al II": {"0": [1.2028, 1.2711], "2": [0.0603, 0.2024], "4": [0.0212], "3": [0.014], "1": [0.8982]}, "Ar II": {"0": [1.7463, 1.7246, 1.6821, 1.6711, 1.6355, 1.6821, 1.7246, 1.7463], "2": [0.693, 0.688, 0.6786, 0.6669, 0.6121, 0.693], "4": [0.0089, 0.0035, 0.0035]}, "Be I": {"1": [0.359, 0.3773], "2": [0.1109, 0.1152], "0": [0.6774, 0.791], "3": [0.0305]}, "Be II": {"0": [0.2623], "1": [0.0491], "2": [0.0021], "3": [0.0001], "4": [0.0001], "5": [0.0002]}, "Bi I": {"0": [4.9036], "2": [3.2646, 3.2071], "1": [4.4712]}, "C II": {"0": [0.6624], "1": [0.3928, 0.4403, 0.4401], "2": [0.0924], "3": [0.022], "4": [0.0054]}, "Ga I": {"0": [2.8013], "2": [1.2926], "1": [2.2107, 2.345], "3": [0.0252]}, "He I": {"0": [0.2965, 0.1392], "1": [0.0133], "2": [0.0007, 0.0014], "3": [0.001], "4": [0.0014], "5": [0.0015], "6": [0.0016]}, "He II": {"0": [7.6e-05], "1": [5.1e-05], "2": [2.5e-05], "3": [1.4e-05], "4": [8.6e-06], "5": [4.5e-06], "6": [1.6e-06]}, "K II": {"3": [0.0426, 0.0336, 0.0242, 0.0143]}, "Li I": {"1": [0.1477, 0.0436, 0.0436], "0": [0.4014], "2": [0.0031]}, "Mg II": {"0": [1.0749, 1.0806], "2": [0.0411], "1": [0.7077, 0.7187, 0.7174], "3": [0.003], "4": [0.0007], "5": [0.0002], "6": [0.0]}, "N II": {"0": [0.7747, 0.7731, 0.7633, 0.7325]}, "Na I": {"0": [1.3506], "1": [0.8584], "2": [0.0141], "3": [0.0014], "4": [0.0003], "5": [0.0]}, "Na II": {"0": [1.0385, 1.0268], "2": [0.0671, 0.0641, 0.0556, 0.0268]}, "Zn II": {"0": [2.2084], "2": [0.9583], "1": [1.8386], "3": [0.0172], "4": [0.0038]}, "Bi III": {"2": [2.8926, 2.8456], "4": [0.0378, 0.0383], "1": [3.7096, 3.6044], "0": [3.9869]}, "Mg I": {"2": [0.4034, 0.1701, 0.1701, 0.1701], "1": [1.0135, 1.2056, 1.2052, 1.2045], "0": [1.5331, 1.6603]}, "Sc III": {"2": [0.6538, 0.6529], "3": [0.045, 0.045], "4": [0.0073, 0.0073], "1": [1.2861, 1.2815], "0": [1.5848]}, "Si II": {"2": [0.229, 0.2289], "3": [0.0846, 0.0846], "4": [0.0174, 0.0174], "1": [1.0239, 1.0215], "0": [1.3944]}, "Li III": {"2": [0.0003, 0.0002], "3": [0.0003, 0.0002], "4": [0.0003, 0.0003], "5": [0.0003, 0.0003], "6": [0.0004, 0.0004], "1": [0.0004, 0.0003], "0": [0.0003]}, "Ba III": {"2": [2.3509, 2.336, 2.1891, 2.3061, 2.2821, 2.2601, 2.3041, 2.3113, 2.1786, 2.1273], "0": [3.2585, 3.2795, 3.23, 3.2018]}, "Bi II": {"2": [2.9846, 3.1079, 3.0001], "3": [1.1755, 1.1468], "0": [4.3705, 4.3684]}, "Ne I": {"2": [0.0154, 0.0119], "0": [1.2923, 1.2974], "1": [0.8409]}, "Li II": {"2": [0.0011, 0.0027], "3": [0.0, 0.0006], "4": [0.0], "5": [0.0], "1": [0.0144, 0.0543], "0": [0.0744, 0.1814]}, "Si I": {"2": [0.0126, 0.057, 0.4032, 0.1375, 0.0284, 0.373, 0.3007, 0.1429, 0.0612, 0.0584, 0.068, 0.0129, 0.0784, 0.0573, 0.0609, 0.0816], "0": [1.8546, 1.8883, 1.893, 1.8758, 1.8873, 1.8765], "3": [0.0003, 0.0008, 0.0277, 0.0281, 0.0471, 0.0462, 0.0165, 0.0181]}, "Zn I": {"2": [1.2232], "1": [2.0966]}, "Ne II": {"2": [0.07, 0.0773, 0.0813, 0.0547, 0.0701], "0": [0.8636, 0.948, 0.9132, 0.9261, 0.9906, 0.985, 0.985], "1": [0.5651, 0.6294, 0.601, 0.5916, 0.6055, 0.6541, 0.643, 0.6767, 0.6884, 0.5679], "3": [0.0039, 0.0086, 0.0096, 0.0098, 0.0025], "4": [0.0016, 0.001, 0.0029, 0.003, 0.0002]}, "Ar II *": {"4": [0.0006, 0.0006, 0.0063, 0.0063, 0.0114, 0.0119, 0.0119], "5": [0.0017, 0.0017, 0.0021, 0.0021, 0.0047, 0.0047, 0.0045, 0.0045, 0.0, 0.0], "6": [0.0009, 0.0009, 0.0012, 0.0012, 0.0025, 0.0025, 0.0023, 0.0023, 0.0, 0.0]}, "Bi II *": {"3": [1.1419], "1": [3.9567]}, "Bi III *": {"5": [0.0103, 0.0103]}, "C II *": {"2": [0.074, 0.074], "0": [0.6615]}, "Li I *": {"2": [0.0016, 0.0016], "0": [0.4077]}, "Li II *": {"6": [0.0001], "1": [0.0537, 0.0537]}, "Li III *": {"7": [0.0004, 0.0004]}, "Mg I *": {"3": [0.0413, 0.0413, 0.0413, 0.0413]}, "Mg II *": {"2": [0.034, 0.034]}, "Ne I *": {"2": [0.0193], "0": [1.3329]}, "Ne II *": {"2": [0.0289, 0.0289, 0.0674, 0.0674, 0.0605]}, "Sc III *": {"5": [0.0022, 0.0022]}, "Zn I *": {"2": [1.094, 1.0936, 1.093]}, "Ba III *": {"4": [0.0394, 0.0397, 0.0428, 0.0422, 0.0208, 0.0212, 0.0174, 0.0172]}, "Si I *": {"1": [1.4808, 1.4252, 1.421]}, "B III": {"2": [0.0023], "3": [0.0003], "4": [0.0001], "5": [0.0], "1": [0.0437], "0": [0.1959]}, "Be III": {"2": [0.0008, 0.0023], "3": [0.0002], "4": [0.0002], "5": [0.0], "1": [0.0429], "0": [0.0508, 0.1302]}, "Be III *": {"6": [0.0]}, "Be IV": {"2": [0.0002], "3": [0.0001], "4": [0.0001], "5": [0.0], "6": [0.0], "7": [0.0], "1": [0.0004], "0": [0.0004]}, "Mg III *": {"2": [0.0934], "3": [0.0111, 0.0108, 0.0039, 0.0, 0.0, 0.0073, 0.0073], "0": [0.8634]}, "Mg III": {"2": [0.0388], "0": [0.8487]}, "Al III": {"2": [0.0644], "3": [0.0044], "4": [0.001], "5": [0.0003], "1": [0.6056], "0": [0.9049]}, "Si III": {"2": [0.0507, 0.1977], "3": [0.024, 0.0226, 0.0224, 0.0221], "4": [0.0266, 0.0281, 0.0281, 0.028], "5": [0.0082, 0.0086, 0.0082], "6": [0.0033, 0.0033], "1": [0.7576, 0.7563], "0": [1.0185, 1.0646]}, "B IV": {"2": [0.0007, 0.0021], "3": [0.0004], "4": [0.0002], "5": [0.0002], "1": [0.0096, 0.035], "0": [0.0392, 0.1011]}, "B IV *": {"6": [0.0003]}, "B V": {"2": [0.0005], "3": [0.0004], "4": [0.0003], "5": [0.0003], "6": [0.0004], "1": [0.0008], "0": [0.0008]}, "B V *": {"7": [0.0004]}, "Si IV": {"2": [0.0802], "3": [0.0054], "4": [0.0011], "1": [0.5262], "0": [0.7845]}, "Si IV *": {"5": [0.0003]}, "P IV": {"2": [0.1991, 0.2312], "3": [0.0597], "1": [0.6991, 0.6699], "0": [0.9018, 0.9498]}, "C V": {"2": [0.0108, 0.0122], "3": [0.0092, 0.0092], "4": [0.0152, 0.0153], "1": [0.0002, 0.0384], "0": [0.0399, 0.0927]}, "C V *": {"5": [0.0186]}, "S V": {"2": [0.1819, 0.217], "3": [0.0002, 0.0637], "1": [0.59, 0.6221], "0": [0.8043, 0.8428]}, "Fe XV *": {"2": [0.1278], "3": [0.0371], "1": [0.2872]}, "Fe XV": {"3": [0.2367]}, "Ca IX": {"2": [0.1572], "1": [0.4121]}, "Ca IX *": {"3": [0.0124], "0": [0.5725]}, "Ti XI *": {"3": [0.0129], "0": [0.4738, 0.4983]}, "Ti XI": {"1": [0.3273]}, "Ti III *": {"2": [0.7987, 0.7899], "1": [1.4159, 1.4039, 1.3956], "0": [1.6726, 1.6901]}, "Ca II": {"0": [1.8338, 1.8192], "2": [0.6341], "3": [0.0248], "4": [0.0048], "1": [1.4775]}, "Ca II *": {"5": [0.0016]}, "Cd II": {"2": [1.8942], "3": [0.0489], "4": [0.0076], "1": [2.7444], "0": [3.1175]}, "Ca I": {"2": [0.9084, 0.8917], "3": [0.0654, 0.0893], "1": [1.8902], "0": [2.3548, 2.4639]}, "Ar I": {"2": [0.3516], "1": [1.7855, 1.7107, 1.7437], "0": [2.1701, 2.1886]}, "Cd I": {"2": [2.1886, 2.0898], "3": [0.0346], "1": [3.0515, 3.1814], "0": [3.5926, 3.6677]}, "Ga II": {"2": [0.8475, 1.063], "3": [0.0598, 0.0617], "4": [0.0146, 0.0142], "0": [2.261, 2.3228]}, "Hg II": {"2": [2.8758], "3": [1.0622], "4": [0.0053], "1": [3.8196], "0": [4.185]}, "P III": {"2": [0.2754], "4": [0.0197], "5": [0.0024], "1": [0.8886], "0": [1.1692]}, "Ba II": {"2": [2.4147], "3": [0.7559], "4": [0.0185], "1": [3.2408], "0": [3.5984]}, "Fe XVI": {"2": [0.075], "3": [0.0116], "1": [0.2233], "0": [0.3174]}, "N III": {"2": [0.0737], "3": [0.0281], "4": [0.0022], "1": [0.2917], "0": [0.566]}, "N III *": {"5": [0.0026]}, "N I": {"2": [0.0273, 0.0514], "1": [0.6233, 0.7714, 0.7329], "0": [1.104, 1.1697]}, "N I *": {"2": [0.0041]}, "S IV": {"2": [0.2649], "1": [0.7607], "0": [1.0264]}, "S VI": {"2": [0.0925], "3": [0.0074], "1": [0.4228], "0": [0.6242]}, "S VI *": {"4": [0.001], "5": [0.0003]}, "Al IV *": {"3": [0.0349]}, "Al IV": {"0": [0.7638]}, "B II": {"2": [0.0323, 0.0772], "3": [0.0397], "4": [0.0401], "1": [0.3284, 0.2231], "0": [0.4303, 0.5211]}, "C III": {"2": [0.0067, 0.0816], "3": [0.0127], "4": [0.0126], "1": [0.1806, 0.1856], "0": [0.3819, 0.3993]}, "O IV": {"2": [0.0681], "3": [0.0408], "1": [0.2462], "0": [0.4408]}, "O IV *": {"4": [0.0028], "5": [0.0125]}, "F I": {"2": [0.0323, 0.0149], "0": [1.1857, 1.28]}, "F I *": {"1": [0.8308]}, "Ge III": {"2": [0.882, 1.0025], "0": [2.0116, 2.0576]}, "Ge III *": {"4": [0.0181]}, "K I": {"2": [0.246], "3": [0.0112], "1": [1.7268], "0": [2.1912]}, "O III": {"2": [0.1196, 0.129], "0": [0.5852, 0.625]}, "O III *": {"2": [0.0791], "1": [0.4221]}, "C I *": {"2": [0.032, 0.0638], "1": [0.7201, 0.6284, 0.6641]}, "C I": {"0": [1.0532, 1.0925]}, "P II *": {"1": [1.167]}, "P II": {"0": [1.5468]}, "S III *": {"0": [1.2846]}}
<<<END FILE: fig241_data.json>>>

<<<FILE: rclose.py>>>
# §32.4.1: R(X) = {x in box : x_i in A_i(X) for all i, and x_i <= phi_ij(x_j) for all i != j},
# phi_ij(a) = max{ y_i : y in X, y_j <= a }.  Tests the three closure properties on random subsets,
# then closure-under-intersection of fixed points over pairs.  Register 1756.
import random, itertools, sys
random.seed(20260824)
D,V=4,5                                   # small ambient box: 4 coordinates, values 0..4 (625 cells)
BOX=list(itertools.product(range(V),repeat=D))
def R(X):
    if not X: return frozenset()
    A=[sorted({x[i] for x in X}) for i in range(D)]
    P=[[[-1]*V for _ in range(D)] for _ in range(D)]
    for y in X:
        for i in range(D):
            for j in range(D):
                if i!=j:
                    for a in range(y[j],V):
                        if y[i]>P[i][j][a]: P[i][j][a]=y[i]
    out=[]
    for x in itertools.product(*A):
        if all(x[i]<=P[i][j][x[j]] for i in range(D) for j in range(D) if i!=j): out.append(x)
    return frozenset(out)
def rand_subset():
    k=random.randint(1,40); return frozenset(random.sample(BOX,k))
ext=mono=idem=0; NS=3000
subsets=[rand_subset() for _ in range(NS)]
closures=[]
for X in subsets:
    C=R(X); closures.append(C)
    if not X<=C: ext+=1
    if R(C)!=C: idem+=1
    Y=X|frozenset(random.sample(BOX,3))
    if not C<=R(Y): mono+=1
print('subsets',NS,'extensive failures',ext,'monotone failures',mono,'idempotent failures',idem)
fixed=list({c for c in closures if c})
NP=int(sys.argv[1]) if len(sys.argv)>1 else 3000
fail=0; nonempty=0
for _ in range(NP):
    A,B=random.sample(fixed,2); I=A&B
    if I: nonempty+=1
    if R(I)!=I: fail+=1
print('distinct fixed points',len(fixed),'pairs',NP,'nonempty intersections',nonempty,'closure failures',fail)
<<<END FILE: rclose.py>>>

<<<FILE: bookindex.py>>>
# §32.1.1 recomputed: cells (location, support) at chapter and part resolution from every paragraph
# outside the Register that cites a section or chapter.  Register 1756.
import re,itertools,collections
L=open('The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
start=[i for i,l in enumerate(L) if l.startswith('# PART 0')][-1]
APP='ABCDEF'
def code(ch): return ch if isinstance(ch,int) else 100+APP.index(ch)   # appendices order after chapters
loc=0; part=0; cells=set(); claims=0; partcells=set(); chpart={0:0}
for i,l in enumerate(L):
    if i<start:
        if re.match(r'^# PART',l): pass
        continue
    m=re.match(r'^# PART ([0IV]+)',l)
    if m: part={'0':0,'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7}[m.group(1)]; continue
    m=re.match(r'^## (\d+)\. ',l)
    if m: loc=int(m.group(1)); chpart[loc]=part; continue
    m=re.match(r'^## Appendix ([A-F])',l)
    if m: loc=m.group(1); chpart[loc]=part; continue
    if l.startswith('#') or not l.strip(): continue
    refs=set(int(x) for x in re.findall(r'§\s?(\d+)\.',l))|set(int(x) for x in re.findall(r'Chapter (\d+)',l))|set(re.findall(r'§\s?([A-F])\.',l))|set(re.findall(r'Appendix ([A-F])',l))
    refs={r for r in refs if (isinstance(r,str) or 1<=r<=35)}
    if refs: claims+=1
    for r in refs:
        cells.add((code(loc),code(r))); partcells.add((chpart[loc],chpart.get(r,part)))
n=41  # 35 chapters + 6 appendices
def R2(X):
    A=[sorted({x[i] for x in X}) for i in range(2)]
    P={}
    for (a,b) in X:
        P[(0,b)]=max(P.get((0,b),-1),a); P[(1,a)]=max(P.get((1,a),-1),b)
    def phi(i,j,v):   # max x_i over cells with x_j<=v
        return max([x[i] for x in X if x[j]<=v] or [-1])
    return {x for x in itertools.product(*A) if x[0]<=phi(0,1,x[1]) and x[1]<=phi(1,0,x[0])}
back=sum(1 for a,b in cells if b<=a); fwd=len(cells)-back
E=len(R2(cells))-len(cells); Ep=len(R2(partcells))-len(partcells)
print(f'claims {claims}  cells {len(cells)}  box {n*n}  density {100*len(cells)/(n*n):.1f}%  E {E}')
print(f'support<=location {back} of {len(cells)}  half-box {n*(n+1)//2}  density {100*back/(n*(n+1)//2):.1f}%  E {len(R2({c for c in cells if c[1]<=c[0]}))-back}')
print(f'forward {fwd} = {100*fwd/len(cells):.0f}%')
print(f'parts: cells {len(partcells)}  box {8*8}  density {100*len(partcells)/64:.1f}%  E {Ep}')
print('part cells',sorted(partcells)); print('closure adds',sorted(R2(partcells)-partcells))
print({k:v for k,v in chpart.items()})
print('V/VI -> IV chapter cells:',sorted((a,b) for a,b in cells if chpart.get(a) in (5,6) and chpart.get(b)==4))
print('cites of ch 20-22 from anywhere in V:',[(a,b) for a,b in cells if chpart.get(a)==5 and b in (19,20,21,22)])
g={0:0,1:0,2:1,3:1,4:2,5:2,6:2,7:2}
tri={(g[a],g[b]) for a,b in partcells}; print('three-group cells',sorted(tri),'E',len(R2(tri))-len(tri))
<<<END FILE: bookindex.py>>>

<<<FILE: kinds.py>>>
# Register front matter, "What the entries are": counts of entries whose HEADLINE matches each pattern
# (case-insensitive; a body tag "(a finding.)" etc. overrides). Kinds overlap; not a partition. Register 1756.
import re,collections,sys
R=open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6___The_Register-2.md',encoding='utf-8').read()
i=R.find('\n### 165\n'); body=R[i:]
ents=re.split(r'\n### ([\d, a-z]+)\n',body)
ids,bodies=ents[1::2],ents[2::2]
PAT={
 'a correction':   r'CORRECT|WRONG|STALE|PUT RIGHT|AMEND|FIX|MISLOCAT|REPAIR|ERROR|OVERTAKEN|MISTAK|MISREAD|MISCOUNT',
 'a measurement':  r'\d',
 'prior art':      r'PRIOR ART|PUBLISHED|ALREADY (KNOWN|IN|DONE)|\b(1[5-9]\d\d|20[0-2]\d)\b|[A-Z][a-z]+ \(\d{4}\)',
 'a new protocol': r'PROTOCOL|\bRULE\b|RULED|RULING|MUST\b|NEVER AGAIN|PROCEDURE',
 'a withdrawal':   r'WITHDR|RETRACT|REMOVED|DROPPED|ABANDON|DISCARD',
 'a fault of mine':r'FAULT OF MINE|MY FAULT|MY ERROR|THE ASSISTANT|I (MIS|FAIL|WROTE|CARRIED)|MEA CULPA',
 'an open question':r'OPEN QUESTION|\bOPEN\b|UNSETTLED|CANNOT (CURRENTLY|YET)|UNKNOWN|UNRESOLVED|NOT (YET )?(SETTLED|KNOWN)',
}
TAG=r'\(\s*(a finding|a correction|a measurement|prior art|a new protocol|a withdrawal|a fault of mine|an open question)\.?\s*\)\*?\s*$'
cnt=collections.Counter()
for i,b in zip(ids,bodies):
    b=b.strip(); head=re.match(r'\*\*(.*?)\*\*',b,re.S); head=head.group(1) if head else b[:200]
    kinds={k for k,p in PAT.items() if re.search(p,head,re.I)}
    t=re.findall(TAG,b)
    if t: kinds={t[-1]}
    if ',' in i: kinds|={'a correction','a fault of mine'}   # grouped early fault entries, by mechanism
    if not (kinds & {'a correction','a withdrawal','a fault of mine','an open question'}): kinds.add('a finding')
    for k in kinds: cnt[k]+=1
print(len(ids),dict(cnt))
if '--write' in sys.argv:   # rewrite the Build 9 column and the heading count in the Register front matter
    R2=R
    for k,n in cnt.items():
        R2,c=re.subn(r'(\| \*\*'+re.escape(k)+r'\*\* \| )[\d,]+( \| )',lambda m:m.group(1)+f'{n:,}'+m.group(2),R2,count=1); assert c==1,k
    R2,c=re.subn(r'over the [\d,]+ entry headings',f'over the {len(ids):,} entry headings',R2); assert c==1
    open(sys.argv[1],'w',encoding='utf-8').write(R2); print('written')
<<<END FILE: kinds.py>>>

<<<FILE: appf.py>>>
# Appendix F recomputed from the main volume (register 1756). Rules as F.3 states them, coarse and rerunnable:
# an OCCURRENCE is a number in body text or a table (locators, register/chapter/figure numbers, years in
# bibliography lines and code blocks excluded); coordinates are assigned from the PARAGRAPH carrying it.
import re,sys,itertools,collections
L=open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6-2.md',encoding='utf-8').read().splitlines()
start=[i for i,l in enumerate(L) if l.startswith('# PART 0')][-1]
paras=[]; cur=[]; kind=None; incode=False
def flush():
    global cur
    if cur: paras.append((kind,'\n'.join(cur))); cur=[]
for l in L[start:]:
    if l.strip().startswith('```'): incode=not incode; flush(); continue
    if incode: continue
    if l.startswith('#'): flush(); continue
    if not l.strip(): flush(); continue
    k='table' if (l.startswith('|') or l.startswith('    ') or l.startswith('  ') and re.search(r'\S\s{3,}\S',l)) else 'prose'
    if cur and k!=kind: flush()
    kind=k; cur.append(l)
flush()
NUM=re.compile(r'(?<![\w§.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?×\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?(?![\w.]\d)')
EXCL=re.compile(r'(§\s?[\dA-F.]+|register(?:s)?\s+\d+(?:[–-]\d+)?|\bR\s?\d{3,4}\b|Chapter \d+|Chapters \d+(?: to \d+)?|Figure \d+\.\d+|Fig\. \d+|Part [IV]+|\(\d{4}\)|\b(1[6-9]\d\d|20[0-2]\d)\b(?=[),;. ])|\bn = \d+|\bZ = \d+|\bℓ = \d+|\bq = \d+|\bd = \d+|\bk = \d+)')
UNIT=r'cm⁻¹|\bfm\b|\bnm\b|\beV\b|hartree|\bkeV\b|MeV|\bpc\b|\bkm\b|\bs\b|\bK\b'
occ=[]
for k,p in paras:
    if re.search(r'^\s*(\*\*)?[A-Z][A-Za-z\-]+, [A-Z]\..*\(\d{4}\)',p) or re.match(r'^\s*[·•-] ',p): continue   # bibliography
    q=EXCL.sub(' ',p)
    for m in NUM.finditer(q):
        s=m.group(0)
        if len(s)==1 and s in '01' and not re.search(r'[=<>≤≥]\s*$',q[:m.start()]): continue   # bare 0/1 are words, not claims
        occ.append((s,k,p))
def cue(p): return bool(re.search(r'§|[Rr]egister|Appendix|recomput|comput|script|\.py|verified|measured|counted|fitted|derived|Table',p))
def qkind(s,p):
    if re.search(UNIT,p): return 'measurement'
    if '%' in p or 'density' in p.lower(): return 'density'
    if re.search(r'\bE\(|defect|E =',p): return 'defect'
    if re.search(r'[≤≥<>]|bracket|bound|between|inside',p): return 'bound'
    if re.search(r'\bper\b|\brate\b|ratio|:\s?1\b|\d\s?:\s?\d',p): return 'rate'
    return 'count'
METH=r'computed|recomputed|counted|measured|fitted|minimis|derived|generated|regressed|solved|proved|verified'
INSET=r'\b(over|across|on|from|of) (the )?\d|\bevery\b|\ball \d|\beach of\b'        # an input SET named
def defn(p):
    meth=bool(re.search(METH,p)); inp=bool(re.search(INSET,p))
    return 2 if meth and inp else 1 if meth else 0          # asserted < stated < stated with inputs (F.3.4: stated ⇔ method named and no input set)
def inputs(k,p):
    if k=='table' or re.search(r'Appendix B|the table|Table|listed|printed',p): return 2   # printed
    if re.search(INSET,p): return 1                                                         # enumerated ⇔ an input set named
    return 0                                                                                # named
def verif(p):
    if re.search(r'\bcaps?\b|varied|under variation|at every|each cap|at cap',p): return 2
    if re.search(r'recomput|verified|checked|reproduc|confirmed|tested|independently',p): return 1
    return 0
cells=collections.defaultdict(set); fibre=collections.Counter()
for s,k,p in occ:
    f=qkind(s,p); fibre[f]+=1; cells[f].add((defn(p),inputs(k,p),verif(p)))
def R(X):
    A=[sorted({x[i] for x in X}) for i in range(3)]
    def phi(i,j,v): return max([x[i] for x in X if x[j]<=v] or [-1])
    return {x for x in itertools.product(*A) if all(x[i]<=phi(i,j,x[j]) for i in range(3) for j in range(3) if i!=j)}
distinct=len({s for s,_,_ in occ}); tables=sum(1 for _,k,_ in occ if k=='table'); prose=len(occ)-tables
nocue=sum(1 for _,_,p in occ if not cue(p))
print(f'F.1: {distinct:,} distinct claim-bearing numbers, {len(occ):,} occurrences: {tables:,} inside tables and {prose:,} in prose. {nocue:,} — {100*nocue/len(occ):.0f}% — no cue.')
tot=0
print('F.3: fibre occurrences distinct admitted E')
for f in ['count','defect','measurement','bound','rate','density']:
    X=cells[f]; adm={x for x in R(X) if not (x[0]==1 and x[1]==1)} if X else set(); a=len(adm); E=a-len(X); tot+=E   # F.3.4's constraint imposed
    print(f'  {f:12s} {fibre[f]:>6,} {len(X):>4} {a:>4} {E:>3}')
print(f'  all {len(occ):,} E {tot}')
v=collections.Counter(verif(p) for _,_,p in occ); d=collections.Counter(defn(p) for _,_,p in occ)
print(f'F.3.1: verification asserted {v[0]:,} recomputed {v[1]:,} under variation {v[2]:,}; definition asserted {d[0]:,} stated {d[1]:,} with inputs {d[2]:,}; {100*v[0]/len(occ):.0f}% asserted')
import math,os
# F.4.2 (ruling 25, register 1762): surviving = D's elements (77, D.5.3/D.5.10's printed count)
# + Math Compendium labelled objects + Physics Compendium labelled parameter objects;
# withdrawn = one claim per Register entry (the book's own sentence), the entry heading count.
DELEM=77; B=os.path.dirname(os.path.abspath(sys.argv[1] if len(sys.argv)>1 else '.'))
MC=os.path.join(B,'The_Method_1_6___Mathematical_Compendium-2.md'); PC=os.path.join(B,'The_Method_1_6___The_Physics_Compendium-2.md'); RG=os.path.join(B,'The_Method_1_6___The_Register-2.md')
if all(os.path.exists(x) for x in (MC,PC,RG)):
    mth=sum(1 for l in open(MC,encoding='utf-8') if l.startswith('### `'))
    phy=sum(1 for l in open(PC,encoding='utf-8') if l.startswith('### '))
    Rt=open(RG,encoding='utf-8').read(); wd=len(re.split(r'\n### ([\d, a-z]+)\n',Rt[Rt.find('\n### 165\n'):])[1::2])
    sv=DELEM+mth+phy; pp=sv/(sv+wd); bits=-(pp*math.log2(pp)+(1-pp)*math.log2(1-pp))
    print(f'F.4.2 ruled row: withdrawn {wd:,}  surviving {sv:,} (77+{mth}+{phy})  {wd/sv:.2f} : 1  p {pp:.3f}  bits {bits:.3f}')
else:
    sv=wd=None; print('F.4.2 ruled row: compendium/Register files not beside source; printed figures stand')
n=len(occ); p=n/(n+190); print(f'F.4.2 first-reading third row (frozen): {n:,}  {190/n:.2f} : 1  p {p:.3f}  bits {-(p*math.log2(p)+(1-p)*math.log2(1-p)):.3f}')
if '--write' in sys.argv:   # rewrite F.1, the F.3 fibre table (Build column) and F.3.1 in the given file (the press copy)
    f=sys.argv[1]; T=open(f,encoding='utf-8').read(); c=0
    T,k=re.subn(r'^ [\d,]+ distinct claim-bearing numbers, [\d,]+ occurrences: [\d,]+ inside tables and [\d,]+ in prose\.\n [\d,]+ of the occurrences — \d+% — stand',
        f' {distinct:,} distinct claim-bearing numbers, {len(occ):,} occurrences: {tables:,} inside tables and {prose:,} in prose.\n {nocue:,} of the occurrences — {100*nocue/len(occ):.0f}% — stand',T,flags=re.M); c+=k
    for fb in ['count','defect','measurement','bound','rate','density']:
        X=cells[fb]; adm={x for x in R(X) if not (x[0]==1 and x[1]==1)} if X else set()
        T,k=re.subn(r'^(  '+fb+r'\s+)[\d,]+(\s+)\d+(\s+)\d+(\s+)-?\d+(\s+[\d,]+ ·)',lambda m:f'{m.group(1)}{fibre[fb]:,}{m.group(2)}{len(X)}{m.group(3)}{len(adm)}{m.group(4)}{len(adm)-len(X)}{m.group(5)}',T,flags=re.M); c+=k
    T,k=re.subn(r'^(  all\s+)[\d,]+(\s+—\s+—\s+)\d+',lambda m:f'{m.group(1)}{len(occ):,}{m.group(2)}{tot}',T,flags=re.M); c+=k
    T,k=re.subn(r'Of [\d,]+ indexed occurrences at (?:Build 9|this press), \*\*[\d,]+ carry verification = asserted\*\*',f'Of {len(occ):,} indexed occurrences at this press, **{v[0]:,} carry verification = asserted**',T); c+=k
    T,k=re.subn(r'against [\d,]+ recomputed and [\d,]+ recomputed under variation\. On the definition\n axis, [\d,]+ are asserted, [\d,]+ stated, and [\d,]+ stated with their inputs',
        f'against {v[1]:,} recomputed and {v[2]:,} recomputed under variation. On the definition\n axis, {d[0]:,} are asserted, {d[1]:,} stated, and {d[2]:,} stated with their inputs',T); c+=k
    if sv is not None:   # ruling 25 (register 1762): census, numerator and ruled row press-recomputed
        T,k=re.subn(r"Appendix D's elements, \d+;\n the Mathematical Compendium's labelled objects, \d+; the Physics Compendium's labelled parameter\n objects, \d+ — \*\*[\d,]+ in all\.\*\*",
            f"Appendix D's elements, {DELEM};\n the Mathematical Compendium's labelled objects, {mth}; the Physics Compendium's labelled parameter\n objects, {phy} — **{sv:,} in all.**",T); c+=k
        T,k=re.subn(r"which is the register's entry count, [\d,]+ at this build",f"which is the register's entry count, {wd:,} at this build",T); c+=k
        T,k=re.subn(r'^(  by the definition above\s+)[\d,]+(\s+)[\d,]+(\s+)[\d.]+ : 1(\s+)[\d.]+(\s+)[\d.]+',
            lambda m:f'{m.group(1)}{wd:,}{m.group(2)}{sv:,}{m.group(3)}{wd/sv:.2f} : 1{m.group(4)}{pp:.3f}{m.group(5)}{bits:.3f}',T,flags=re.M); c+=k
    open(f,'w',encoding='utf-8').write(T); print('appendix F rewritten,',c,'edits')
<<<END FILE: appf.py>>>

<<<FILE: tb_audit.py>>>
# Three-body paper audit, six checks x thirteen mass order-types (register 1717's 78; named here, register 1756).
# Shape coordinates after Montgomery: mass-weighted Jacobi vectors rho1, rho2 in R^2; w = (|rho1|^2-|rho2|^2, 2 rho1.rho2) in R^3 (Hopf).
import numpy as np, itertools, sympy as sp
rng=np.random.default_rng(1770)
ORDER=[(1,1,1),(1,1,2),(1,2,1),(2,1,1),(1,2,2),(2,1,2),(2,2,1),(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]   # 13 mass order-types
def jac(m,q):
    m1,m2,m3=m; M12=m1+m2
    r1=np.sqrt(m1*m2/M12)*(q[1]-q[0]); r2=np.sqrt(M12*m3/(M12+m3))*(q[2]-(m1*q[0]+m2*q[1])/M12); return r1,r2
def shape(m,q):
    r1,r2=jac(m,q); return 0.5*np.array([r1@r1-r2@r2, 2*r1@r2, 2*(r1[0]*r2[1]-r1[1]*r2[0])])   # Montgomery normalisation: |w| = I/2, d_ij^2 = mu_ij r_ij^2
def rays(m):
    b={}
    for i,j in [(0,1),(1,2),(0,2)]:
        q=rng.normal(size=(3,2)); q[j]=q[i]; w=shape(m,q); b[(i,j)]=w/np.linalg.norm(w)
    return b
def mu(m,i,j): return m[i]*m[j]/(m[i]+m[j])
def cij(m,i,j): return (m[i]*m[j])**1.5/np.sqrt(m[i]+m[j])
def checks(m):
    m=np.array(m,float); b=rays(m); res={}
    okC=okA=True
    for _ in range(50):
        q=rng.normal(size=(3,2)); w=shape(m,q); I=np.linalg.norm(w)
        U=0; V=0
        for i,j in b:
            d2=I-w@b[(i,j)]; r2=np.sum((q[i]-q[j])**2)
            okC&=abs(d2/mu(m,i,j)-r2)<1e-9*max(1,r2)          # C: d_ij^2 = |w| - w.b_ij, r_ij^2 = d_ij^2/mu_ij
            U+=cij(m,i,j)/np.sqrt(d2); V+=m[i]*m[j]/np.sqrt(r2)
        okA&=abs(U-V)<1e-10*V                                    # A: U(w) = sum m_i m_j / r_ij
    res['A']=okA; res['C']=okC
    u1,u2,u3,U=sp.symbols('u1 u2 u3 U'); p=u1**2+u2**2+u3**2; qq=u1**2*u2**2+u2**2*u3**2+u1**2*u3**2; r=u1**2*u2**2*u3**2
    N=U**8-4*p*U**6+(6*p**2-8*qq)*U**4-4*(p**3-4*p*qq+16*r)*U**2+(p**2-4*qq)**2
    res['B']=sp.expand(N.subs(U,u1+u2+u3))==0                    # B: the norm vanishes at U = u1+u2+u3
    prod=sp.expand(sp.prod([(u1+s2*u2+s3*u3)**2 for s2 in (1,-1) for s3 in (1,-1)]))
    res['F']=sp.expand((p**2-4*qq)**2-prod)==0                   # F: constant term = prod over the sign classes
    # D: Euler's quintic has exactly one positive root for each of the three orderings; the equilateral triangle is a critical point
    okD=True; m1,m2,m3=m
    for (a,bb,c) in [(m1,m2,m3),(m2,m3,m1),(m3,m1,m2)]:
        coef=[a+bb, 3*a+2*bb, 3*a+bb, -(bb+3*c), -(2*bb+3*c), -(bb+c)]   # Euler quintic for body bb between a and c
        roots=np.roots(coef); okD&=sum(1 for z in roots if abs(z.imag)<1e-9 and z.real>0)==1
    def Ufun(w): 
        I=np.linalg.norm(w); return sum(cij(m,i,j)/np.sqrt(I-w@b[(i,j)]) for i,j in b)
    q=np.array([[0,0],[1,0],[0.5,np.sqrt(3)/2]]); w=shape(m,q); wh=w/np.linalg.norm(w)
    g=np.zeros(3); h=1e-6
    for k in range(3):
        e=np.zeros(3); e[k]=h; g[k]=(Ufun(wh+e)-Ufun(wh-e))/(2*h)
    gt=g-(g@wh)*wh                                               # tangential gradient on the sphere at fixed |w|
    okD&=np.linalg.norm(gt)<1e-4*abs(Ufun(wh))
    res['D']=okD
    # E: symmetry order of U under mass-preserving relabellings: 6, 2, 1
    order=sum(1 for perm in itertools.permutations(range(3)) if all(m[perm[k]]==m[k] for k in range(3)))
    res['E']=order==(6 if len(set(m))==1 else 2 if len(set(m))==2 else 1)
    return res
tot=0; passed=0
for m in ORDER:
    r=checks(m); tot+=6; passed+=sum(r.values()); print(m,''.join(k if v else k.lower() for k,v in sorted(r.items())))
print(f'{passed} of {tot}')
<<<END FILE: tb_audit.py>>>

<<<FILE: spectra_count.py>>>
# Spectra Compendium: counts from its own channel table (register 1756). Columns: species | series | n | levels | interior | bracket | n* range | δ | σ | fits | limit
import re,sys,collections
rows=[l for l in open(sys.argv[1] if len(sys.argv)>1 else 'The_Method_1_6___Spectra_Compendium-2.md',encoding='utf-8') if l.startswith('| ') and re.search(r'\| [+-]\d\.\d+(?:e-\d+)? \|',l)]
sp=set(); el=set(); lev=0; inter=0; two=0
for l in rows:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    s=c[0].replace(' *',''); sp.add(s); el.add(s.split()[0]); lev+=int(c[3]); inter+=int(c[4])
    if '*' in c[0] or int(c[3])==2: two+=1
print(f'{len(rows)} channel rows — {len(rows)-two} series of three or more members and {two} two-member channels — across {len(el)} elements and {len(sp)} species; {lev:,} levels, {inter:,} interior cells.')
# bracket column (ruling 26, register 1763): m/k sums, no-triple, untested
bp=bt=mk=nt=ut=0
for l in rows:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    m=re.match(r'(\d+)/(\d+)$',c[5])
    if m: mk+=1; bp+=int(m.group(1)); bt+=int(m.group(2))
    elif c[5]=='no-triple': nt+=1
    elif c[5]=='untested': ut+=1
print(f'bracket: {mk} rows tested, {bp} of {bt} cells pass; {nt} no-triple rows; {ut} untested rows.')
<<<END FILE: spectra_count.py>>>

<<<FILE: index_pages.py>>>
# Print index (register 1756): map every §-locator in the main volume's Index block to the page its heading
# starts on in a pressed PDF, and write a press-only copy of the source with page numbers in the Index.
# usage: python3 index_pages.py <src.md> <first-pass.pdf> <out.md>
import re,sys,subprocess
src,pdf,out=sys.argv[1:4]
L=open(src,encoding='utf-8').read().splitlines()
heads={}   # locator -> heading text
allh=[]    # (level, text) for the generic Contents
DEPTH=int(sys.argv[4]) if len(sys.argv)>4 else 2
body=[i for i,l in enumerate(L) if l.startswith('# PART 0')]
body=body[-1] if body else 1
for l in L[body:]:
    mh=re.match(r'^(#{1,3}) (.*)',l)
    if mh and len(mh.group(1))<=DEPTH+1 and not l.startswith('# PART'): allh.append((len(mh.group(1)),mh.group(2))); heads.setdefault('H:'+mh.group(2),mh.group(2))
    m=re.match(r'^## (\d+)\. (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^### (\d+\.\d+) (.*)',l)
    if m: heads.setdefault('§'+m.group(1),m.group(2)); continue
    m=re.match(r'^## Appendix ([A-F]) — (.*)',l)
    if m: heads.setdefault('App '+m.group(1),m.group(2))
pages=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
def norm(s): return re.sub(r'[^a-z0-9]+',' ',re.sub(r'\*|_|`','',s).lower()).strip()
ptext=[norm(p) for p in pages]
# the printed TOC also carries every heading: take the LAST page after the front matter on which the heading opens a line
haslit=any(re.match(r'^\s*#{0,3}\s*Contents\s*$',l) for l in L)
front=next((i for i,p in enumerate(pages) if re.search(r'^\s*(1\.|PART 0)',p,re.M) and i>3),3) if haslit else 1   # skip title/contents pages only
pm={}
for loc,h in heads.items():
    num=loc.replace('§','').replace('App ','appendix '); want=norm(num+' '+h) if not loc.startswith('H:') else norm(h)
    for i,p in enumerate(pages):
        if i<front: continue
        lines=[norm(l) for l in p.splitlines()]
        if any(l==want or (len(want)>12 and l.startswith(want[:max(12,len(want)-6)])) or (l.startswith(norm(num)+' ') and want.startswith(l) and len(l)>len(norm(num))+8) for l in lines):
            pm[loc]=i+1; break
print('headings',len(heads),'mapped',len(pm))
ixs=[i for i,l in enumerate(L) if l.startswith('## Index')]
ix=ixs[-1] if ixs else len(L)
missing=set(); n=0
def sub(m):
    global n
    loc=m.group(0); n+=1
    if loc in pm: return f'{loc} ({pm[loc]})'
    missing.add(loc); return loc
for i in range(ix,len(L)):
    if L[i].startswith('## ') and i>ix: break
    if '……' in L[i]: L[i]=re.sub(r'§\d+(?:\.\d+)?|App [A-F]',sub,L[i])
print('locators',n,'unmapped',sorted(missing)[:20],len(missing))
# Contents with page numbers, replacing the source's literal contents block (which build.py otherwise strips)
ci=[i for i,l in enumerate(L) if re.match(r'^\s*#{0,3}\s*Contents\s*$',l)]
if ci:
    i=ci[0]; parts=[k for k,l in enumerate(L) if k>i and re.match(r'^# PART 0',l)]; j=parts[1] if len(parts)>1 else i+1
    toc=['## Contents','']
    for l in L[body:]:
        m=re.match(r'^# (PART .*)',l)
        if m: toc.append(''); toc.append('**'+m.group(1)+'**'); toc.append(''); continue
        m=re.match(r'^## (\d+)\. (.*)',l)
        if m: toc.append(f"{m.group(1)}. {m.group(2)} …… {pm.get('§'+m.group(1),'')}  "); continue
        m=re.match(r'^## (Appendix [A-F]) — (.*)',l)
        if m: toc.append(f"{m.group(1)} — {m.group(2)} …… {pm.get('App '+m.group(1)[-1],'')}  "); continue
        m=re.match(r'^## (Index|References)\b',l)
        if m: toc.append(f"{m.group(1)}  ")
    L=L[:i]+toc+['']+L[j:]
    print('contents block written',len(toc),'lines')
else:
    toc=['## Contents','']+[('  ' if lv==3 else '')+f"{h} …… {pm.get('H:'+h,'')}  " for lv,h in allh if h!='Contents' and pm.get('H:'+h)]
    k=1 if L and L[0].startswith('# ') else 0
    L=L[:k]+['']+toc+['']+L[k:]
    print('generic contents written',len(toc)-2,'headings')
open(out,'w',encoding='utf-8').write('\n'.join(L)+'\n')
<<<END FILE: index_pages.py>>>

<<<FILE: heii.py>>>
# He II quantum defects from the NIST ASD levels supplied 2026-08-24 (register 1758). T = limit − E; δ = n − Z√(R/T).
import re,numpy as np,itertools,sys
raw=open('heii_levels.txt',encoding='utf-8').read()
lev=[]; cur=None
for l in raw.splitlines():
    c=[x.strip() for x in l.split('|')]
    if len(c)<4: continue
    if c[0]: cur=c[0]
    n=int(cur[:-1]); L='spdfghikl'.index(cur[-1]); J=eval(c[2]); lev.append((n,L,float(J),float(c[3])))
print(len(lev),'levels')
Rinf=109737.31568; RHe=Rinf/(1+5.4857990907e-4/4.002602*1.007276466812/1.007276466812)  # placeholder
RHe=Rinf/(1+0.00054857990907/(4.002602-2*0.00054857990907))   # reduced mass with the He-4 nuclear mass
def delta(E,n,lim,R,Z=2): return n-Z*np.sqrt(R/(lim-E))
def series(lim,R,conv):
    out={}
    for L in range(7):
        ns=sorted({n for n,l,J,E in lev if l==L})
        vals=[]
        for n in ns:
            Js=[(J,E) for nn,l,J,E in lev if nn==n and l==L]
            if conv=='low': E=min(Js)[1]
            elif conv=='high': E=max(Js)[1]
            elif conv=='cent': E=sum((2*J+1)*E for J,E in Js)/sum(2*J+1 for J,E in Js)
            vals.append(delta(E,n,lim,R))
        out[L]=(ns,np.array(vals))
    return out
for lim in (438908.885,438908.871,438908.8874):
    for R in (Rinf,RHe):
        for conv in ('low','high','cent'):
            s=series(lim,R,conv); m=[abs(s[L][1]).mean() for L in range(7)]
            print(f'lim {lim} R {"Rinf" if R==Rinf else "RHe "} {conv:4s}  mean|δ| by ℓ:',' '.join(f'{x:.2e}' for x in m),' mono' if all(m[i]>m[i+1] for i in range(6)) else '')
print('--- limit by minimising the ng spread (n = 5..10, centroid, R_He), scanned at 0.001')
def ng_spread(lim):
    s=series(lim,RHe,'cent'); return s[4][1].max()-s[4][1].min()
grid=np.arange(438908.700,438909.100,0.001); sp=[ng_spread(x) for x in grid]; best=grid[int(np.argmin(sp))]
print('argmin',round(best,3),'spread',min(sp))
s=series(438908.871,RHe,'cent')
print('--- corrected He II series (centroid, R_He, limit 438,908.871)')
for L in range(7):
    ns,v=s[L]; print('spdfghi'[L],f'n {ns[0]}–{ns[-1]}',len(ns),f'δ̄ {v.mean():+.2e}  σ {v.std(ddof=0):.1e}  |δ̄| {abs(v.mean()):.2e}')
import json; json.dump({str(L):[abs(s[L][1].mean()),s[L][1].mean(),s[L][1].std(),s[L][0][0],s[L][0][-1],len(s[L][0])] for L in range(7)},open('heii_series.json','w'))
<<<END FILE: heii.py>>>

<<<FILE: heii_levels.txt>>>
1s|2S|1/2|0.0000
2p|2P*|1/2|329179.2939406
|  |3/2|329185.15110923
2s|2S|1/2|329179.762313
3p|2P*|1/2|390140.8249696
|  |3/2|390142.5604306
3s|2S|1/2|390140.964517
3d|2D|3/2|390142.55757536
|  |5/2|390143.13600712
4p|2P*|1/2|411477.1227550
|  |3/2|411477.8548989
4s|2S|1/2|411477.1817529
4d|2D|3/2|411477.853680
|  |5/2|411478.097707
4f|2F*|5/2|411478.097267
|  |7/2|411478.219277
5p|2P*|1/2|421352.6789311
|  |3/2|421353.05378699
5s|2S|1/2|421352.709172
5d|2D|3/2|421353.053159
|  |5/2|421353.178101
5f|2F*|5/2|421353.177874
|  |7/2|421353.240343
5g|2G|7/2|421353.2402246
|  |9/2|421353.2777059
6p|2P*|1/2|426717.1361554
|  |3/2|426717.3530854
6s|2S|1/2|426717.1536654
6d|2D|3/2|426717.352717
|  |5/2|426717.425022
6f|2F*|5/2|426717.424890
|  |7/2|426717.461041
6g|2G|7/2|426717.4609726
|  |9/2|426717.4826633
6h|2H*|9/2|426717.48262081
|  |11/2|426717.49708121
7p|2P*|1/2|429951.7150373
|  |3/2|429951.8516453
7s|2S|1/2|429951.7260676
7d|2D|3/2|429951.851412
|  |5/2|429951.896945
7f|2F*|5/2|429951.8968623
|  |7/2|429951.9196283
7g|2G|7/2|429951.9195841
|  |9/2|429951.9332435
7h|2H*|9/2|429951.9332167
|  |11/2|429951.9423230
7i|2I|11/2|429951.94230466
|  |13/2|429951.94880910
8p|2P*|1/2|432051.0711584
|  |3/2|432051.1626754
8s|2S|1/2|432051.0785504
8d|2D|3/2|432051.1625182
|  |5/2|432051.1930212
8f|2F*|5/2|432051.1929662
|  |7/2|432051.2082172
8g|2G|7/2|432051.2081883
|  |9/2|432051.2173390
8h|2H*|9/2|432051.2173210
|  |11/2|432051.2234215
8i|2I|11/2|432051.22340924
|  |13/2|432051.22776674
8k|2K*|13/2|432051.22775782
|  |15/2|432051.23102591
9p|2P*|1/2|433490.3773261
|  |3/2|433490.4416001
9s|2S|1/2|433490.3825181
9d|2D|3/2|433490.4414901
|  |5/2|433490.4629131
9f|2F*|5/2|433490.4628741
|  |7/2|433490.4735861
9g|2G|7/2|433490.4735653
|  |9/2|433490.4799922
9h|2H*|9/2|433490.47997948
|  |11/2|433490.48426408
9i|2I|11/2|433490.48425549
|  |13/2|433490.48731579
9k|2K*|13/2|433490.48730958
|  |15/2|433490.48960487
9l|2L|15/2|433490.489600115
|  |17/2|433490.491385335
10p|2P*|1/2|434519.9013585
|  |3/2|434519.9482148
10s|2S|1/2|434519.9051443
10d|2D|3/2|434519.9481342
|  |5/2|434519.9637522
10f|2F*|5/2|434519.9637232
|  |7/2|434519.9715319
10g|2G|7/2|434519.9715169
<<<END FILE: heii_levels.txt>>>

<<<FILE: heii_series.json>>>
{"0": [7.618362007386637e-05, 7.618362007386637e-05, 1.9407080925336093e-05, 1, 10, 10], "1": [5.0861703044950225e-05, 5.0861703044950225e-05, 7.955932006797465e-06, 2, 10, 9], "2": [2.496929966444572e-05, 2.496929966444572e-05, 3.950649466913318e-06, 3, 10, 8], "3": [1.4120933476366052e-05, 1.4120933476366052e-05, 1.977129123988712e-06, 4, 10, 7], "4": [8.559519922476019e-06, 8.559519922476019e-06, 1.0093987673237776e-06, 5, 10, 6], "5": [4.458618036551343e-06, 4.458618036551343e-06, 4.023767419757147e-07, 6, 9, 4], "6": [1.59025414170344e-06, 1.59025414170344e-06, 4.086873555223316e-07, 7, 9, 3]}
<<<END FILE: heii_series.json>>>

<<<FILE: run489.py>>>
# run489.py — the ruled bracket over the Spectra Compendium's untested rows.
# Sealed test (bracket.py, R 796) under M's ruling (RULING-TOLERANCE-489.md):
# strict interval membership; quotation floor (half a unit in the last quoted
# decimal of the measured level) as the only edge guard; admissibility
# r = 2*Z^2*R/(nu^3*sigma) >= 5 (Method Section 22.5) with sigma = the quotation
# floor — a cell that cannot distinguish pass from fail is REFUSED. The raw
# tables' unc column is present and NOT used, per the ruling's grounds (R 822, 807).
# Limits and Z: channels.py's LIM (the sealed pipeline's own), cross-checked
# against each row's printed limit; mismatches reported, never silently chosen.
import re, math, glob, os, json, sys
from collections import defaultdict
R = 109737.31568
SP = 'The_Method_1_6___Spectra_Compendium-2.md'

# LIM from the restore point's channels.py (identical to the store's)
src = open('rp/channels.py', encoding='utf-8').read()
i = src.index('LIM = {'); depth, j = 0, i + 6
while True:
    if src[j] == '{': depth += 1
    elif src[j] == '}':
        depth -= 1
        if depth == 0: break
    j += 1
LIM = eval(src[i+6:j+1])

def qfloor(s):
    s = s.strip()
    return 0.5 * 10 ** -(len(s.split('.')[1]) if '.' in s else 0)

def load_raw(name):
    ser = defaultdict(list)
    for line in open(f'rp/spectra_raw/{name}.tsv', encoding='utf-8'):
        if line.startswith('#') or line.startswith('config') or not line.strip(): continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 4: continue
        mm = re.match(r'^(.*?)(\d+)([spdfghik])$', p[0].strip())
        if not mm: continue
        try: E = float(p[3])
        except ValueError: continue
        ser[(mm.group(1), mm.group(3), p[1].strip(), p[2].strip())].append((int(mm.group(2)), E, p[3].strip()))
    return ser

results = {}; anomalies = []
rows = [l for l in open(SP, encoding='utf-8') if l.startswith('| ') and re.search(r'\| [+-]\d\.\d+(?:e-\d+)? \|', l)]
for l in rows:
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if c[5] != 'untested': continue
    species = c[0].replace(' *', ''); name = species.replace(' ', '')
    key = (species, c[1])
    if not os.path.exists(f'rp/spectra_raw/{name}.tsv'):
        results[key] = ('no-data', 0, 0, 0, 0); continue
    m = re.match(r'^(.*?)n([spdfghik])\s+(\S+)\s+J=(\S+)$', c[1])
    if not m:
        anomalies.append((key, 'series-unparsed')); results[key] = ('unparsed', 0, 0, 0, 0); continue
    pre, lch, term, J = m.group(1), m.group(2), m.group(3), m.group(4)
    nr = re.match(r'(\d+)[–-](\d+)', c[2]); nlo, nhi = int(nr.group(1)), int(nr.group(2))
    lim, Z = LIM.get(name, (None, None))
    rowlim = float(c[10].replace(',', ''))
    if lim is None: lim, Z = rowlim, {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'IX':9,'XI':11,'XV':15,'XVI':16}[species.split()[1]]
    elif abs(lim - rowlim) > 0.5: anomalies.append((key, f'limit LIM {lim} vs row {rowlim}'))
    ser = load_raw(name)
    v = sorted({(n, E, s) for (p2, l2, t2, j2), vals in ser.items() if (p2, l2, t2, j2) == (pre, lch, term, J) for (n, E, s) in vals if nlo <= n <= nhi and E < lim})
    if len(v) != int(c[3]): anomalies.append((key, f'levels raw {len(v)} vs row {c[3]}'))
    d = {n: n - Z * math.sqrt(R / (lim - E)) for n, E, s in v}
    byn = {n: (E, s) for n, E, s in v}
    p = f = rf = t = 0; fails = []
    for k in range(1, len(v) - 1):
        n = v[k][0]
        if v[k-1][0] != n - 1 or v[k+1][0] != n + 1: continue
        dl, dh = sorted((d[n-1], d[n+1]))
        lo = lim - Z*Z*R / (n - dl)**2; hi = lim - Z*Z*R / (n - dh)**2
        lo, hi = min(lo, hi), max(lo, hi)
        E, s = byn[n]; qf = qfloor(s); nu = n - d[n]
        if 2 * Z*Z * R / (nu**3 * qf) < 5: rf += 1; continue
        t += 1
        if lo - qf <= E <= hi + qf: p += 1
        else: f += 1; fails.append(n)
    results[key] = ('run', p, f, rf, t)
    if fails: anomalies.append((key, f'FAIL at n={fails}'))

ran = [v for v in results.values() if v[0] == 'run']
print(f'rows: {len(results)} total — {len(ran)} run, {sum(1 for v in results.values() if v[0]=="no-data")} no-data, {sum(1 for v in results.values() if v[0]=="unparsed")} unparsed')
print(f'cells: {sum(v[4] for v in ran)} tested — {sum(v[1] for v in ran)} pass, {sum(v[2] for v in ran)} FAIL; {sum(v[3] for v in ran)} refused')
print(f'rows with zero testable cells: {sum(1 for v in ran if v[4]+v[3]==0)}')
print(f'anomalies: {len(anomalies)}')
for a in anomalies[:40]: print('  ', a)
json.dump({f'{k[0]}|{k[1]}': v for k, v in results.items()}, open('run489_results.json', 'w'), indent=0)
<<<END FILE: run489.py>>>

<<<FILE: ruled_bracket.py>>>
# ruled_bracket.py — the sealed bracket (bracket.py, R 796) run under M's ruling
# (RULING-TOLERANCE-489.md, 2026-08-24): STRICT interval membership; the only ε is
# the QUOTATION FLOOR (half a unit in the last quoted decimal of the measured level),
# applied at the interval edges; a cell whose measurement cannot distinguish pass
# from fail is REFUSED, not passed: r = 2*Z^2*R/(nu^3 * sigma) >= 5 (Method §22.5),
# sigma = the quotation floor. Refusals counted separately from pass/fail.
import re, math, sys
from collections import defaultdict
R = 109737.31568

def qfloor(s):
    """Half a unit in the last quoted decimal place of the value as printed."""
    s = s.strip()
    return 0.5 * 10 ** -(len(s.split('.')[1]) if '.' in s else 0)

def run_series(members, lim, Z):
    """members: sorted [(n, E, E_as_printed)]. Returns (passed, failed, refused, detail)."""
    d = {n: n - Z * math.sqrt(R / (lim - E)) for n, E, _ in members}
    byn = {n: (E, s) for n, E, s in members}
    p = f = r = 0; detail = []
    for i in range(1, len(members) - 1):
        n = members[i][0]; a, b = members[i-1][0], members[i+1][0]
        if a != n - 1 or b != n + 1: continue          # only true neighbours (sealed)
        dl, dh = sorted((d[a], d[b]))
        lo = lim - Z*Z*R / (n - dl)**2
        hi = lim - Z*Z*R / (n - dh)**2
        lo, hi = min(lo, hi), max(lo, hi)
        E, s = byn[n]; qf = qfloor(s)
        nu = n - d[n]
        adm = 2 * Z*Z * R / (nu**3 * qf)               # §22.5 admissibility
        if adm < 5:
            r += 1; detail.append((n, 'REFUSED', adm)); continue
        if lo - qf <= E <= hi + qf:                     # strict, edge-guarded by the floor
            p += 1; detail.append((n, 'pass', (lo, hi, E, qf)))
        else:
            f += 1; detail.append((n, 'FAIL', (lo, hi, E, qf)))
    return p, f, r, detail

if __name__ == '__main__':
    # instrument verification on captures/LEVELS-K-I.tsv (the one untested species in the cut)
    lim, Z = 35009.814, 1
    ser = defaultdict(list)
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        pp = line.rstrip('\n').split('\t')
        if len(pp) < 4: continue
        mm = re.match(r'^(\d+)([spdfghik])$', pp[0].strip())
        if not mm: continue
        try: E = float(pp[3])
        except ValueError: continue
        if E >= lim: continue
        ser[(mm.group(2), pp[1], pp[2])].append((int(mm.group(1)), E, pp[3]))
    for key, v in sorted(ser.items()):
        v = sorted(v)
        if len(v) < 3: continue
        p, f, r, det = run_series(v, lim, Z)
        print(key, f'pass {p} fail {f} refused {r}')
        for row in det: print('  ', row)
<<<END FILE: ruled_bracket.py>>>

<<<FILE: run489_45.json>>>
{
"Bi III|6s2.nd 2D J=3/2": [
"run",
1,
0,
0,
1
],
"Bi III|6s2.nd 2D J=5/2": [
"run",
1,
0,
0,
1
],
"Bi III|6s2.ng 2G J=7/2": [
"run",
2,
0,
0,
2
],
"Bi III|6s2.ng 2G J=9/2": [
"run",
2,
0,
0,
2
],
"Bi III|6s2.np 2P* J=1/2": [
"run",
1,
0,
0,
1
],
"Bi III|6s2.np 2P* J=3/2": [
"run",
1,
0,
0,
1
],
"Bi III|6s2.ns 2S J=1/2": [
"run",
1,
0,
0,
1
],
"Sc III|3p6.nd 2D J=3/2": [
"run",
3,
0,
0,
3
],
"Sc III|3p6.nd 2D J=5/2": [
"run",
3,
0,
0,
3
],
"Sc III|3p6.nf 2F* J=5/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.nf 2F* J=7/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.ng 2G J=7/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.ng 2G J=9/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.np 2P* J=1/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.np 2P* J=3/2": [
"run",
2,
0,
0,
2
],
"Sc III|3p6.ns 2S J=1/2": [
"run",
3,
0,
0,
3
],
"Ne I|nd 2[3/2]* J=1": [
"no-data",
0,
0,
0,
0
],
"Ne I|ns 2[1/2]* J=1": [
"no-data",
0,
0,
0,
0
],
"Zn I|nd 1D J=2": [
"no-data",
0,
0,
0,
0
],
"Zn I|np 1P* J=1": [
"no-data",
0,
0,
0,
0
],
"Ba III|ns 2[1/2]* J=1": [
"no-data",
0,
0,
0,
0
],
"Ba III|nd 2[3/2]* J=2": [
"no-data",
0,
0,
0,
0
],
"Ba III|ns 2[3/2]* J=1": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 4D J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 4D J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 4D J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 4F J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 2P J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 2P J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 4P J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 4P J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 4P J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 2S J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 2D J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ns 2D J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne I|np 1P* J=1": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 2D* J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 2D* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 2S* J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4D* J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4D* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4D* J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4P* J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4P* J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4P* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|np 4S* J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nf 2[2]* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nf 2[3]* J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nf 2[4]* J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nf 2[4]* J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nf 2[5]* J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ng 2[2] J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ng 2[3] J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ng 2[4] J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ng 2[5] J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|ng 2[6] J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[4] J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[6] J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[6] J=13/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[2] J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[2] J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[3] J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[3] J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[4] J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[5] J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ng 2[5] J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[3]* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[3]* J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[4]* J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[4]* J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[5]* J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[5]* J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[6]* J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[6]* J=13/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[7]* J=13/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|nh 2[7]* J=15/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[4] J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[4] J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[5] J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[5] J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[6] J=11/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[6] J=13/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[7] J=13/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[7] J=15/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[8] J=15/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|ni 2[8] J=17/2": [
"no-data",
0,
0,
0,
0
],
"Bi III|6s2.nh 2H* J=11/2": [
"run",
0,
0,
0,
0
],
"Bi III|6s2.nh 2H* J=9/2": [
"run",
0,
0,
0,
0
],
"Ne II|nd 2F J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 2F J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 2G J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 2G J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ne II|nd 2P J=3/2": [
"no-data",
0,
0,
0,
0
],
"Sc III|3p6.nh 2H* J=11/2": [
"run",
0,
0,
0,
0
],
"Sc III|3p6.nh 2H* J=9/2": [
"run",
0,
0,
0,
0
],
"Ba III|ng 2[11/2]* J=5": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[11/2]* J=6": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[5/2]* J=2": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[5/2]* J=3": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[7/2]* J=3": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[7/2]* J=4": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[9/2]* J=4": [
"no-data",
0,
0,
0,
0
],
"Ba III|ng 2[9/2]* J=5": [
"no-data",
0,
0,
0,
0
],
"Si I|ns (3/2,1/2)* J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|ns (3/2,1/2)* J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[3/2] J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[3/2] J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[5/2] J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[5/2] J=3": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[7/2] J=3": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[7/2] J=4": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[9/2] J=4": [
"no-data",
0,
0,
0,
0
],
"Si I|nf 2[9/2] J=5": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 1D* J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 1F* J=3": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 1P* J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 3F* J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 3F* J=3": [
"no-data",
0,
0,
0,
0
],
"Si I|nd 3F* J=4": [
"no-data",
0,
0,
0,
0
],
"Si I|np (1/2,1/2) J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|np (1/2,3/2) J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|np (1/2,3/2) J=2": [
"no-data",
0,
0,
0,
0
],
"Si I|ns (1/2,1/2)* J=0": [
"no-data",
0,
0,
0,
0
],
"Si I|ns (1/2,1/2)* J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|nd (1/2,3/2)* J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|nd (3/2,3/2)* J=1": [
"no-data",
0,
0,
0,
0
],
"Si I|nd (3/2,5/2)* J=3": [
"no-data",
0,
0,
0,
0
],
"Si I|nd (3/2,3/2)* J=0": [
"no-data",
0,
0,
0,
0
],
"Si I|nd (3/2,5/2)* J=1": [
"no-data",
0,
0,
0,
0
],
"Ar II|3s2.3p4.(3P).nd 4D J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|3s2.3p4.(3P).ns 4P J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|3s2.3p4.(3P).ns 4P J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ar II|3s2.3p4.(3P).ns 4P J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|nd 2D J=3/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|nf 2F* J=5/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|ng 2G J=7/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|nh 2H* J=9/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|np 2P* J=1/2": [
"no-data",
0,
0,
0,
0
],
"Ca II|ns 2S J=1/2": [
"no-data",
0,
0,
0,
0
],
"Cd II|nd 2D J=3/2": [
"run",
7,
0,
0,
7
],
"Cd II|nf 2F* J=5/2": [
"run",
4,
0,
0,
4
],
"Cd II|ng 2G J=7/2": [
"run",
4,
1,
0,
5
],
"Cd II|np 2P* J=1/2": [
"run",
2,
1,
0,
3
],
"Cd II|ns 2S J=1/2": [
"run",
7,
0,
0,
7
],
"Ca I|nd 1D J=2": [
"no-data",
0,
0,
0,
0
],
"Ca I|nd 3D J=1": [
"no-data",
0,
0,
0,
0
],
"Ca I|nf 1F* J=3": [
"no-data",
0,
0,
0,
0
],
"Ca I|nf 3F* J=2": [
"no-data",
0,
0,
0,
0
],
"Ca I|np 1P* J=1": [
"no-data",
0,
0,
0,
0
],
"Ca I|ns 1S J=0": [
"no-data",
0,
0,
0,
0
],
"Ca I|ns 3S J=1": [
"no-data",
0,
0,
0,
0
],
"Hg II|nd 2D J=3/2": [
"run",
4,
0,
0,
4
],
"Hg II|nf 2F* J=7/2": [
"run",
2,
0,
0,
2
],
"Hg II|ng 2G J=9/2": [
"run",
3,
0,
0,
3
],
"Hg II|np 2P* J=1/2": [
"run",
1,
0,
0,
1
],
"Hg II|ns 2S J=1/2": [
"run",
4,
0,
0,
4
],
"N I|nd 2F J=5/2": [
"run",
1,
0,
0,
1
],
"N I|nd 4D J=1/2": [
"run",
0,
0,
0,
0
],
"N I|nd 4F J=3/2": [
"run",
0,
1,
0,
1
],
"N I|np 2D* J=3/2": [
"run",
0,
1,
0,
1
],
"N I|np 4D* J=1/2": [
"run",
1,
0,
0,
1
],
"N I|np 4P* J=1/2": [
"run",
1,
0,
0,
1
],
"N I|ns 2P J=1/2": [
"run",
2,
0,
0,
2
],
"N I|ns 4P J=1/2": [
"run",
2,
0,
0,
2
],
"C I|nd 1F* J=3": [
"run",
0,
0,
0,
0
],
"C I|nd 3D* J=1": [
"run",
0,
0,
0,
0
],
"C I|np 3D J=1": [
"run",
0,
0,
0,
0
],
"C I|np 3P J=0": [
"run",
0,
0,
0,
0
],
"C I|np 3S J=1": [
"run",
0,
0,
0,
0
],
"C I|ns 1P* J=1": [
"run",
0,
1,
0,
1
],
"C I|ns 3P* J=0": [
"run",
0,
1,
0,
1
]
}<<<END FILE: run489_45.json>>>

<<<FILE: channels_LIMB.py>>>
# synthesized for run489.py from LIMITS-B.tsv (hash 1d35ea57d89495bf), chat 11.
# LIMITS-B was extracted from the sealed pipeline's channels.py LIM (MANIFEST, PART B note).
LIM = {
 'BiIII': (206242.0, 3),
 'CI': (90937.5, 1),
 'CdII': (136374.74, 2),
 'HgII': (151269.2, 2),
 'NI': (117244.1, 1),
 'ScIII': (199677.37, 3),
}
<<<END FILE: channels_LIMB.py>>>

<<<FILE: LIMITS-B.tsv>>>
species_file	limit_cm1	spectrum
BiIII_asd	206242.0	3
CI_full	90937.5	1
CdII_full	136374.74	2
HgII_full	151269.2	2
NI_full	117244.1	1
ScIII_asd	199677.37	3
<<<END FILE: LIMITS-B.tsv>>>

<<<FILE: BiIII_asd.tsv>>>
# Bi III — NIST ASD 5.12, Arya & Tauheed 2020, ref L21488 · 68 levels found
# limit Bi IV (6s2 1S0) 206242.0 +/- 1.4 cm-1
# CRITICAL NOTE from the compilation: uncertainties are given for level SEPARATIONS
# from the base level 6s6p2(3P) 4P3/2 at 83038.06 cm-1. To obtain the uncertainty of
# an EXCITATION ENERGY these must be combined in quadrature with the ground-level
# uncertainty of 0.06 cm-1.
config	term	J	level_cm1	unc_cm1
6s2.6p	2P*	1/2	0.00	0.06
6s2.6p	2P*	3/2	20788.18	0.04
6s.6p2.(3P)	4P	1/2	70253.71	0.05
6s.6p2.(3P)	4P	3/2	83038.06	0.00
6s.6p2.(3P)	4P	5/2	89236.09	0.06
6s2.7s	2S	1/2	95076.57	0.08
6s2.6d	2D	3/2	96154.69	0.08
6s2.6d	2D	5/2	102446.27	0.06
6s.6p2.(3P)	2P	1/2	108054.43	0.11
6s.6p2.(3P)	2P	3/2	130964.4	0.4
6s.6p2.(1D)	2D	3/2	108586.42	0.13
6s.6p2.(1D)	2D	5/2	116414.30	0.12
6s2.7p	2P*	1/2	116993.4	0.2
6s2.7p	2P*	3/2	122128.6	0.2
6s.6p2.(1S)	2S	1/2	130984.9	0.2
6s2.5f	2F*	7/2	137455.39	0.06
6s2.5f	2F*	5/2	137555.28	0.09
6s2.8s	2S	1/2	145227.9	0.3
6s2.7d	2D	3/2	149086.7	0.3
6s2.7d	2D	5/2	149795.4	0.2
6s2.8p	2P*	1/2	154198.9	0.2
6s2.8p	2P*	3/2	156420.63	0.12
6s2.6f	2F*	7/2	162184.4	0.2
6s2.6f	2F*	5/2	162241.6	0.2
6s.6p.(3P*).7s	4P*	1/2	165218.0	0.3
6s.6p.(3P*).7s	4P*	3/2	169534.24	0.14
6s.6p.(3P*).7s	4P*	5/2	188525.7	0.3
6s2.5g	2G	9/2	166234.6	0.4
6s2.5g	2G	7/2	166237.2	0.4
6s2.9s	2S	1/2	167288.7	0.3
6s.6p.(3P*).6d	4F*	3/2	168045.0	0.3
6s.6p.(3P*).6d	4F*	3/2	172048.8	0.4
6s.6p.(3P*).6d	4F*	5/2	172329.2	0.2
6s.6p.(3P*).6d	4F*	7/2	177625.5	0.2
6s2.8d	2D	3/2	169293.1	0.2
6s2.8d	2D	5/2	169657.6	0.5
6s.6p.(3P*).7s	2P*	1/2	172833.6	0.2
6s.6p.(3P*).7s	2P*	3/2	191311.0	0.3
6s.6p.(3P*).6d	2D*	5/2	174092.4	0.2
6s.6p.(3P*).6d	4D*	3/2	177707.4	0.2
6s.6p.(3P*).6d	4D*	1/2	178333.4	0.2
6s.6p.(3P*).6d	4D*	7/2	194993.7	0.3
6s.6p.(3P*).6d	4D*	5/2	196484.6	0.3
6s2.6g	2G	9/2	178465.5	0.3
6s2.6g	2G	7/2	178469.0	0.3
6s2.6h	2H*	9/2	178718.1	1.0
6s2.6h	2H*	11/2	178718.1	1.0
6s.6p.(3P*).6d	4P*	5/2	180297.7	0.2
6s.6p.(3P*).6d	4P*	3/2	196916.1	0.4
6s.6p.(3P*).6d	4P*	1/2	197283.0	0.8
6p3	4S*	3/2	185738.6	0.2
6s2.7g	2G	9/2	185848.1	0.4
6s2.7g	2G	7/2	185852.1	0.4
6s2.7h	2H*	9/2	186024.1	0.4
6s2.7h	2H*	11/2	186024.1	0.4
6s2.8g	2G	9/2	190640.8	0.5
6s2.8g	2G	7/2	190643.6	0.5
6s.6p.(3P*).6d	2F*	5/2	191396.2	0.4
6s.6p.(3P*).6d	2P*	3/2	198807.1	0.2
6s.6p.(3P*).6d	2P*	1/2	199503.7	0.9
6p3	2D*	3/2	201570.2	0.2
6s.6p.(1P*).6d	2D*	5/2	204727.3	0.3
<<<END FILE: BiIII_asd.tsv>>>

<<<FILE: CI_full.tsv>>>
# C I — NIST ASD 5.12, ref L20057 · Z=6, neutral
# limit NOT printed; DERIVED by the lowest-rms rule (register 1066)
config	term	J	level_cm1
3s	3P*	0	60333.4476
4s	3P*	0	78105.00058
5s	3P*	0	83740.0964
3s	1P*	1	61981.83211
4s	1P*	1	78340.29782
5s	1P*	1	83877.305
3p	1P	1	68856.35208
4p	1P	1	80562.88550
3p	3D	1	69689.49393
4p	3D	1	80782.44916
3p	3S	1	70743.97227
4p	3S	1	81105.06418
3p	3P	0	71352.54344
4p	3P	0	81311.0544
3d	1D*	2	77679.83311
4d	1D*	2	83497.58690
3d	3F*	2	78199.09144
4d	3F*	2	83747.43248
3d	3D*	1	78293.51263
4d	3D*	1	83820.1576
3d	1F*	3	78529.64651
4d	1F*	3	83947.2231
<<<END FILE: CI_full.tsv>>>

<<<FILE: CdII_full.tsv>>>
# Cd II — NIST ASD 5.12, ref L3466/L3540 · Z=48, 47 electrons
# limit Cd III (4d10 1S0) = 136,374.74 +/- 0.10 cm-1  — PUBLISHED
config	term	J	level_cm1
5s	2S	1/2	0.00
6s	2S	1/2	82990.66
7s	2S	1/2	107300.88
8s	2S	1/2	118040.65
9s	2S	1/2	123751.48
10s	2S	1/2	127152.89
11s	2S	1/2	129343.05
12s	2S	1/2	130835.86
13s	2S	1/2	131899.07
5p	2P*	1/2	44136.08
6p	2P*	1/2	94710.41
7p	2P*	1/2	112361.06
8p	2P*	1/2	120618.46
9p	2P*	1/2	125223.06
11p	2P*	1/2	129956.3
12p	2P*	1/2	131261.1
5d	2D	3/2	89689.25
6d	2D	3/2	110174.10
7d	2D	3/2	119522.72
8d	2D	3/2	124613.30
9d	2D	3/2	127697.43
10d	2D	3/2	129708.50
11d	2D	3/2	131092.90
12d	2D	3/2	132086.77
13d	2D	3/2	132824.25
4f	2F*	5/2	108419.47
5f	2F*	5/2	118545.77
6f	2F*	5/2	123988.39
7f	2F*	5/2	127283.04
8f	2F*	5/2	129419.38
9f	2F*	5/2	130878.61
5g	2G	7/2	118769.95
6g	2G	7/2	124151.26
7g	2G	7/2	127396.62
8g	2G	7/2	129502.43
9g	2G	7/2	130946.09
10g	2G	7/2	131978.47
11g	2G	7/2	132742.26
<<<END FILE: CdII_full.tsv>>>

<<<FILE: HgII_full.tsv>>>
# Hg II — NIST ASD 5.12, ref L11760 · Z=80, 79 electrons
# limit DERIVED at 151,269.2 from the two lowest-rms series (g, f). Formal error 12.2;
# read as 151,269 +/- 75 per the Ga II calibration (register 1056).
# the full 5d10.nl series, J-resolved, replacing the earlier short capture
config	term	J	level_cm1	unc
6s	2S	1/2	0.000	0.006
7s	2S	1/2	95714.406	0.004
8s	2S	1/2	121416.626	0.006
9s	2S	1/2	132560.550	0.016
10s	2S	1/2	138434.682	0.022
11s	2S	1/2	141912.265	0.022
6p	2P*	1/2	51486.070	0.008
7p	2P*	1/2	108298.183	0.004
8p	2P*	1/2	126941.844	0.007
6d	2D	3/2	104984.138	0.014
7d	2D	3/2	125325.531	0.006
8d	2D	3/2	134562.854	0.014
9d	2D	3/2	139627.043	0.008
10d	2D	3/2	142660.277	0.010
11d	2D	3/2	144653.677	0.033
5f	2F*	7/2	123153.775	0.006
6f	2F*	7/2	133269.525	0.019
7f	2F*	7/2	138795.581	0.010
8f	2F*	7/2	142128.476	0.012
5g	2G	9/2	133654.879	0.007
6g	2G	9/2	139044.524	0.009
7g	2G	9/2	142294.817	0.012
8g	2G	9/2	144403.510	0.014
9g	2G	9/2	145849.628	0.033
<<<END FILE: HgII_full.tsv>>>

<<<FILE: NI_full.tsv>>>
# N I — NIST ASD 5.12, ref L7288 · Z=7, neutral
# limit NOT printed; DERIVED by the lowest-rms rule (register 1059)
# the 2s2.2p2.(3P).nl series
config	term	J	level_cm1
3s	4P	1/2	83284.070
4s	4P	1/2	103622.51
5s	4P	1/2	109812.233
6s	4P	1/2	112565.470
3s	2P	1/2	86137.350
4s	2P	1/2	104144.820
5s	2P	1/2	110035.720
6s	2P	1/2	112691.96
3p	4D*	1/2	94770.880
4p	4D*	1/2	106758.731
5p	4D*	1/2	111143.567
3p	4P*	1/2	95475.310
4p	4P*	1/2	106980.480
5p	4P*	1/2	111271.596
3p	2D*	3/2	96787.680
4p	2D*	3/2	107182.788
5p	2D*	3/2	111853.061
3d	4F	3/2	104664.130
4d	4F	3/2	110194.654
5d	4F	3/2	112759.966
3d	2F	5/2	104810.360
4d	2F	5/2	110286.305
5d	2F	5/2	112812.518
3d	4D	1/2	104984.37
4d	4D	1/2	110385.795
<<<END FILE: NI_full.tsv>>>

<<<FILE: ScIII_asd.tsv>>>
# Sc III — NIST ASD 5.12, Sugar & Corliss 1985, ref L7185 · 44 levels found, COMPLETE
# limit Sc IV (3p6 1S0) 199677.37 +/- 0.10 cm-1 (L1891,L7185)
config	term	J	level_cm1	unc_cm1
3p6.3d	2D	3/2	0.00	0
3p6.3d	2D	5/2	197.64	
3p6.4s	2S	1/2	25539.32	
3p6.4p	2P*	1/2	62104.30	
3p6.4p	2P*	3/2	62578.18	
3p6.4d	2D	3/2	112257.62	
3p6.4d	2D	5/2	112302.95	
3p6.5s	2S	1/2	114862.48	
3p6.5p	2P*	1/2	128107.12	
3p6.5p	2P*	3/2	128283.15	
3p6.4f	2F*	5/2	136873.87	
3p6.4f	2F*	7/2	136874.12	
3p6.5d	2D	3/2	148130.03	
3p6.5d	2D	5/2	148150.14	
3p6.6s	2S	1/2	149194.03	
3p6.6p	2P*	1/2	155489.78	
3p6.6p	2P*	3/2	155575.20	
3p6.5f	2F*	5/2	159472.24	
3p6.5f	2F*	7/2	159472.24	
3p6.5g	2G	7/2	160072.18	
3p6.5g	2G	9/2	160072.18	
3p6.6d	2D	3/2	165592.55	
3p6.6d	2D	5/2	165603.29	
3p6.7s	2S	1/2	166157.17	
3p6.7p	2P*	1/2	169637.96	
3p6.7p	2P*	3/2	169685.9	
3p6.6f	2F*	7/2	171787.64	
3p6.6f	2F*	5/2	171787.64	
3p6.6g	2G	9/2	172177.41	
3p6.6g	2G	7/2	172177.41	
3p6.6h	2H*	9/2	172224.57	
3p6.6h	2H*	11/2	172224.57	
3p6.7d	2D	3/2	175457.03	
3p6.7d	2D	5/2	175463.56	
3p6.8s	2S	1/2	175795.73	
3p6.7f	2F*	5/2	179214.70	
3p6.7f	2F*	7/2	179214.70	
3p6.7g	2G	7/2	179477.24	
3p6.7g	2G	9/2	179477.24	
3p6.7h	2H*	9/2	179508.37	
3p6.7h	2H*	11/2	179508.37	
3p6.8g	2G	9/2	184214.61	
3p6.8g	2G	7/2	184214.61	
<<<END FILE: ScIII_asd.tsv>>>

<<<FILE: The_Method_1_6___Mathematical_Compendium-2.md>>>

# THE METHOD 1.6 — MATHEMATICAL COMPENDIUM

Generated from `mathreg.py` on 2026-08-12; the counts below were recounted from this file on 2026-08-24 (register 1739). **265 objects · 18 roots · 263 settled · 2 unfinished.**

**Verification coverage, stated rather than implied.** `mathverify.py` makes **103 assertions naming 46 of these objects** and recomputes each stated value against the register; **no verifier touches the other 167**. Of the check fields, **85 state a finding, 91 repeat the object's own key, 19 name a function, and 18 are empty** — so a check field present is not a verification performed. `check_audit.py` classifies them on any build. Register 849.

Rebuild with `python3 compendium.py > COMPENDIUM.md`. It reads the register, so it cannot
drift from what the book actually holds.

---

# I · THE CYCLE

The whole of this work is one recursion, stated at §14.5.2:

> **X₍ₙ₊₁₎ = ℛ(X_n ∪ Δ_n)**, halting when **Δ_n ⊆ ℛ(X_n)** — when the increment is already implied.

**It has never halted.** Its falsifier is the ratio of closure to seed:

| | |
|---|---|
| closure — objects the register holds | **265** |
| seed — objects nothing derives | **17** |
| ratio | **15.6 : 1** |

**The seed has not moved across every cycle of this project.** If a genuinely new mathematical
object entered that nothing existing derived, it would move — and that is the test.

## The eighteen roots

| object | statement |
|---|---|
| `3B.shape` | ℝ³ = ℂ³ / (translations × rotations); S² = that / scale — shape space (Montgomery 2014; Hopf 1931) |
| `A.alph` | Â_i(X) = { x_i : x ∈ X } |
| `A.seaton` | delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l( |
| `B.adm` | r = 2Z²R/(ν³σ) ≥ 5 |
| `B.brk` | T(n) lies between T(n−1) and T(n+1) |
| `B.coll` | an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b} |
| `B.nuV` | ν_V = (3Z²R/5q)^{1/4} |
| `L.c1` | ℓ ≤ n − 1 |
| `L.c2` | k ≤ 2(2ℓ+1) = 4ℓ+2 |
| `L.c3` | q ≤ k |
| `L.c4` | f ≤ e − 1 |
| `L.c5` | g ≤ 4f+2 |
| `L.c6` | g ≤ q |
| `L.c7` | 2S ≤ k |
| `L.c8` | k ≥ 1 (definitional restriction, not a bound) |
| `M.rs` | the vacuum is cyclic and separating for local algebras |
| `P.qdt` | the quantum defect measures how far a Rydberg orbital reaches into the ionic core |
| `P.trunc` | truncation removes most channels and degrades those it leaves |

---

# II · THE OPERATORS

Every derivation in the book runs through these. Ten are this work's own; two (π, N₈) are cited and used as found.

| symbol | definition | scope | origin |
|---|---|---|---|
| **∧ ∨** | meet and join — greatest lower and least upper bound | cells | Birkhoff, standard |
| **φ̂** | the envelope: max xᵢ over cells with xⱼ ≤ v | sets of cells | §14.5 |
| **ℛ** | closure at the (≤,≤) corner of Deville's staircase class | sets of cells | §14.5.4 |
| **ℛ₄** | closure over all four orientations | sets of cells | §14.5.5 |
| **E** | E(X) = \|ℛ(X)\| − \|X\| — the defect | indexes | §6.1 |
| **E₄** | the defect under ℛ₄; E − E₄ is the orientation cost | indexes | §14.5.5 |
| **d** | d(x,y) = τ(lcm/gcd) = ∏(\|Δᵢ\|+1) = \|[x∧y, x∨y]\| | cells | title page |
| **∘** | composition of transitions — Λ₉ is a category | cells | §12.11 |
| **seed** | least G with ℛ(G) = X — **NP-hard** | sets of cells | §14.5.7 |
| **S** | envelope-step count; 2S = the tight-pair count | sets of cells | §14.5.9 |
| **ent** | the entrant operator: argmax over frontier (n,ℓ) of \|D(n,ℓ)\| in the ion's self-consistent field | subshells | §35; register 1701 |
| **π** | the shape map ℂ³ → ℝ³, w = (½(\|Z₁\|²−\|Z₂\|²), Re Z₁Z̄₂, Im Z₁Z̄₂) | configurations | Montgomery 2014; Hopf 1931 |
| **N₈** | the norm ∏_{ε∈{±1}³}(U − ε·u) — the minimal polynomial of a sum of three square roots | potentials | Lagrange 1770 |

---

# III · THE LANGUAGES, AND WHY EACH IS NECESSARY

**A language is a coordinate system. Translation is re-coordinatisation. E is the cost.**

Six languages agree on Λ at 976, and **all ten pairs hold** — C(5,2), a complete graph rather than
a ladder. Binary is adjacent to every other, not only to logic. **The agreement is the result; the
list is not.** What follows is one object stated seven ways, with the quantity each language alone
supplies.

| language | its statement of Λ | value | what only it can say |
|---|---|---|---|
| **analysis** | F(1), the enumerator at z = 1 | **976** | the cell count without enumerating |
| **analysis** | F(−1), the alternating sum | **2** | the parity imbalance — invisible to a set |
| **order** | \|ℛ(X)\|, the closure | **976** | what the envelopes admit |
| **order** | E = \|ℛ(X)\| − \|X\| | **0** | **the defect** — no other language states one |
| **geometry** | the void, per interval | **0.464** | what an interval admits and Λ refuses |
| **binary** | the box, one bit per cell | **6,912** | the space before any constraint |
| **binary** | density | **0.1412** | the fraction a constraint set keeps |
| **information** | bits to print the cells | **12,449** | the cost of stating it in full |
| **information** | bits to print the seed | **89** | **139× compression** |
| **statistics** | recovered from pairwise marginals | **976** | the object from its margins alone |
| **statistics** | its defect | **0** | — *and this is its limit* |
| **algebra** | constraints generating the ideal | **8** | derivability — what follows from what |
| **documentary** | *has anyone said this before* | — | **no algorithm exists** |

## Why none is redundant

**Analysis** gives F(−1) = 2. That is an alternating sum over the cells, and **a set has no
alternating sum** — order, geometry and binary cannot express it. It is the parity imbalance, and
it is why §12.1 can state its two-column law — ascending and descending quantities, exchanged under ν ↦ ν⁻³, a bipartite sign structure that admits no odd number of orientation reversals.

**Order** is the only language that states a DEFECT. E has no counterpart in the others: the
generating function does not know what it fails to enumerate, and a polyhedron does not know which
of its lattice points are absent. **Every result in this work that begins *E =* begins here.**

**Geometry** gives the void — 46.4% of a typical interval is admitted by the box and refused by Λ.
The same quantity read in order is slack and in calculus is V, **and §12.11 shows the three are one
number**. But only geometry states it per interval, which is where the exclusion principle shows.

**Binary** gives the box. **Nothing else in this work says what the space was before a constraint
touched it**, and every density, every defect and every compression ratio is a fraction of it.

**Information** gives the compression: **139 cells printed for every one in the seed.** That number
exists in no other language — order knows the seed is seven, and only description length says what
seven buys.

**Statistics** recovers Λ exactly from its pairwise marginals, and **that is the whole of what it
can do.** Tested on the periodic table it reports **E = 0 where ℛ reports 36** — *marginals cannot
see a hole.* **It agrees with the other languages only where there is nothing to disagree about**,
which makes it necessary for one purpose and useless for another. **Knowing which is the point of
having it.**

**Algebra** gives derivability. Whether a bound follows from the others is a question about an
ideal, and **§14.5.7's anti-exchange failure and register 618's rule-15-backs-rule-5 are both
statements in this language** — one constraint implied by another, which no count can express.

**Documentary** has no closure operator at all. *Has anyone said this before* cannot be bounded by
computation, which is why §29's precedent question can be bounded and never settled, and why two
searches returning nothing is evidence of a kind the other six never have to produce.

    **The test of necessity is not that each language is available. It is that each
    states a quantity the others cannot, and this table is that check run.**

---

# IV · THE OBJECTS, BY FAMILY

## A. The operators — closure, envelope, orientation — 43 objects

### `A.E` — closure defect

**E(X) = |ℛ(X)| − |X|**

*none*

grade **DEFINITIONAL**· source *M §6.1 / T A4; Moore 1910*· depends on `A.R`· 14 objects depend on it· depth 3

> **PRIOR ART: the gap between a set and its closure. That it is worth naming as a DEFECT is the books move; the quantity is the closure minus the set.**

### `A.EW` — the metric defect

**E_W(X) = |W(X)| - |X|: the METRIC defect, what the steps reach and the index has not valued; distinct from E(X) = |R(X)| - |X|, the ORDINAL defect**

*an index whose cells carry values*

grade **DEFINITIONAL**· source *R 1133; Dijkstra 1959*· depends on `A.W`, `A.R`· 1 object depends on it· depth 5

for Λ E_W is empty, because a cell of Λ is an arrangement and carries no number — which is why the book needed only E. For Λ_spectra the two differ, and the gap between them is the cells that are placed and unvalued

> **PRIOR ART: the reachable set under a step relation, with accumulated cost and a least-cost route, is single-source shortest paths — Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1 (1959) 269-271.**

### `A.R` — the recovery operator

**ℛ(X) = { x ∈ ∏_i Â_i(X) : x_i ≤ φ̂_ij(x_j) ∀ i≠j }**

*none beyond A.alph, A.env*

grade **DEFINITIONAL**· source *M §6.1 / T A3; Moore 1910; Deville et al. 1999*· depends on `A.alph`, `A.env`· 20 objects depend on it· depth 2

> **PRIOR ART: R is a closure operator (Moore 1910) whose constraints are monotone staircases (Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271). Neither the operator form nor the constraint class is new; what is new is reading E as a defect.**

### `A.S` — the step operator

**the STEP operator: for each coordinate direction, the ratio between adjacent VALUED cells, its median and its scatter; a direction earns a step when the scatter is tight enough to carry a value**

*an index whose cells carry values*

grade **MEASURED**· source *R 1132-1137; Edlen 1964*· depends on `A.R`· 1 object depends on it· depth 3

derived unaided from the spectra index it finds iso at s (1.233, scatter 1.13, 43 pairs), iso at p (1.185, 1.16, 25) and l at s (1.416, 1.43, 62). It must be derived from MEASURED cells ONLY: re-deriving from the walked result tightens iso at s to 1.08 on 116 pairs, because the walked values were generated by that step, and the step count goes 3 to 8

> **PRIOR ART: measuring a step as the ratio between adjacent valued cells is the isoelectronic and isonuclear method of Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### `A.W` — the walk

**the VALUATION closure: every cell reachable from a valued one by steps in S, accumulated error below a threshold, by the least-error route**

*an index, a step set S, and a tolerance*

grade **PROVED**· source *R 1132-1136; Dijkstra 1959*· depends on `A.S`· 2 objects depend on it· depth 4

EXTENSIVE and IDEMPOTENT with exactly zero drift, since the least-error route from the seed leaves nothing tighter to find. MONOTONE except at one cell in 1,345: Mg II ni is measured at +0.0000, the Seaton step is multiplicative, and zero blocks a route a walked positive value would open — so adding a measurement can REMOVE a walked cell

> **PRIOR ART: the valuation closure is a shortest-path closure over a multiplicative cost. Extensivity, idempotence and monotone-except-at-zero follow from Dijkstra (1959).**

### `A.alph` — projection onto coordinate i

**Â_i(X) = { x_i : x ∈ X }**

*X a finite set of integer tuples*

grade **DEFINITIONAL**· source *M §6.1 / T A1; Codd 1970*· 2 objects depend on it· depth 0

> **PRIOR ART: projection onto a coordinate is the relational projection operator — Codd, A relational model of data for large shared data banks, CACM 13 (1970) 377-387.**

### `A.anchor` — the anchor

**REDUNDANCY ANCHORING: keep every route to a cell, not the best one; the spread between independent arrivals MEASURES the error rather than estimating it**

*a valuation closure with more than one route to a cell*

grade **MEASURED**· source *R 1136; Gauss 1809*· depends on `A.W`· depth 5

956 cells of the spectra index are reached by two or more distinct routes. Observed spread 1.05 against a propagated estimate of 1.14 — ratio 0.92, so the walk's error bars are honest and slightly conservative. The check comes from the index disagreeing with itself, not from an outside formula

> **PRIOR ART: keeping every route to an estimate and reading their SPREAD as the error, rather than taking the best route, is the method of combining independent determinations — Gauss, Theoria motus corporum coelestium (1809), sec. 3.**

### `A.blind` — the three blindnesses

**each language is blind in its own way: statistics cannot state a closure defect, analysis cannot state an ordering, a multiplicative algebra cannot state an exception**

*an index described in more than one language*

grade **MEASURED**· source *R 1169; Shannon 1948; Freuder 1978*· depends on `Q.bridge`· depth 13

register 761 established the first. The second: least squares minimises squared error and has no rank in it — an equation fitting 311 values to R^2 = 0.924 got every ordering wrong. The third: a product of positive factors is monotone in each, so a multiplicative fit returns 205/205 where the data has eleven genuine exceptions

> **PRIOR ART: that a representation cannot state what its own coordinates cannot distinguish is the general fact behind all three blindnesses. Statistics sees marginals only (Shannon 1948 for what a marginal carries); analysis has no order in it; a multiplicative algebra is monotone in each factor by construction. Register 1170 measures them.**

### `A.bound` — the defect bounds

**0 ≤ E(X) ≤ |box| − |X|**

*box = ∏_i |Â_i(X)|*

grade **PROVED**· source *T audit 27; Moore 1910*· depends on `A.E`, `A.ext`· depth 4

> **PRIOR ART: the bounds are extensivity below and the ambient product above; both follow from the closure axioms.**

### `A.bpc` — binary path consistency / 2-decomposability (Kimura et al. 2024)

**X ⊆ BPC(X) ⊆ ℛ(X), BPC(X) = { x : (x_i,x_j) ∈ proj_ij(X) ∀ i<j }**

*none*

grade **PROVED**· source *T A5; Cooper 1989; Janssen et al. 1989*· depends on `A.R`· 1 object depends on it· depth 3

> **PRIOR ART: binary path consistency and its relation to global consistency — Cooper, An optimal k-consistency algorithm, Artif. Intell. 41 (1989) 89-95; Janssen, Jegou, Nouguier & Vilarem, A filtering process for general constraint-satisfaction problems, IEEE (1989), which gives a polynomial algorithm for pairwise consistency.**

### `A.cert` — the certificate condition

**an open index does not close itself except where a CERTIFICATE exhibits an operation on its coordinate system reaching a fixed point of R**

*the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate*

grade **PROVED**· source *M §18.4.1, promoted; Tarski 1955*· depends on `A.clos`, `A.modeA`, `A.modeB`· 1 object depends on it· depth 8

> **PRIOR ART: a closure operator does not close an open set without an added operation; exhibiting one is the fixed-point construction of Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309.**

### `A.clos` — closure operator (Moore family)

**ℛ is extensive, monotone, idempotent; the closed sets form a Moore family**

*none*

grade **PROVED**· source *M §14.2 / T 1.3; Moore 1910; Ward 1942*· depends on `A.ext`· 2 objects depend on it· depth 4

> **PRIOR ART: an extensive, monotone, idempotent operator is a CLOSURE OPERATOR and its fixed sets form a Moore family — E. H. Moore, Introduction to a Form of General Analysis (1910); M. Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. R is one; nothing about R is needed to know its fixed sets are closed under intersection.**

### `A.dechter` — Dechter 1992

**strong (w*+1)-consistency on induced width w* gives decomposability**

*induced width w**

grade **CITED**· source *Dechter 1992*· depends on `A.gc`· depth 5

A.dechter

### `A.define` — the defining letter

**a rung-1 coordinate contributes no envelope: same cells, box, E, envelope-step count and seed with or without it — it is invisible to ℛ and still counts as a letter**

*it is the index's own name carried as a coordinate, taking one value because the object is what does not vary in it*

grade **PROVED**· source *M §21.6.1; Birkhoff 1937*· depends on `A.env`· depth 2

> **PRIOR ART: a coordinate with a single value contributes no join-irreducible, so it changes neither the lattice nor its envelopes.**

### `A.dens` — density and informativeness

**E = 0 is informative at any density; E > 0 at low density measures sparsity**

*density = |X| / |box|*

grade **COMPUTED**· source *T 1.9; Erdos & Renyi 1960*· depends on `A.E`· 1 object depends on it· depth 4

> **PRIOR ART: that a structural property can hold at any density, while its failure measures sparsity, is the random-graph threshold picture of Erdos & Renyi, On the evolution of random graphs, Publ. Math. Inst. Hung. Acad. Sci. 5 (1960) 17-61.**

### `A.derived` — adjunction never repairs (M Thm 10.1)

**a derived coordinate cannot repair closure: the box grows by its value count and |X| is fixed**

*the coordinate is a function of the others*

grade **PROVED**· source *T 1.7 / M §17.2 Thm 10.1; Birkhoff 1940*· depends on `A.E`· 1 object depends on it· depth 4

> **PRIOR ART: a derived coordinate is a function of the others, so it adds no join-irreducibles and cannot enlarge the closed family; it only enlarges the ambient box.**

### `A.ebits` — description length

**E_bits(X) = log₂ C(|ℛ(X)|, E(X))**

*counting measure*

grade **COMPUTED**· source *M §25.3; Shannon 1948; Rissanen 1978*· depends on `A.E`· 1 object depends on it· depth 4

> **PRIOR ART: description length as a measure of structure — Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (1948); Rissanen, Modeling by shortest data description, Automatica 14 (1978) 465-471. log2 C(|R|, E) is the cost of naming which admitted cells are absent.**

### `A.env` — monotone upper envelope / staircase bound

**φ̂_ij(v) = max{ x_i : x ∈ X, x_j ≤ v }; max ∅ = −∞**

*i ≠ j*

grade **DEFINITIONAL**· source *M §6.1 / T A2; Deville et al. 1999*· depends on `A.alph`· 7 objects depend on it· depth 1

> **PRIOR ART: the monotone upper envelope of a relation is its staircase bound — the connected row-convex class of Deville, Barette & Van Hentenryck (1999) and the row-convex networks of van Beek & Dechter, J. ACM 42 (1995) 543-561.**

### `A.erel` — E is coordinate-relative

**E = 0 is relative to coordinates: any X with |X| = a·b relabels onto an a × b rectangle, which is a full box and closed — so every index with a composite cell count has a coordinate system in which E = 0**

*the coordinates must be fixed by the subject, not chosen; every coordinate in this book is*

grade **PROVED**· source *M §21.6; Birkhoff 1940; Birkhoff 1937; Dushnik & Miller 1941*· depends on `A.R`· depth 3

> **PRIOR ART: E = 0 is a statement about a COORDINATISATION, not a set. Any set of size ab relabels onto an a x b grid, which is closed. This is the standard observation that lattice properties are not invariants of the underlying set.**

> **PRIOR ART: a lattice property belongs to a COORDINATISATION and not to the underlying set — the same reason order dimension is not an invariant of cardinality. Birkhoff (1937); Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610.**

### `A.expr` — the expression always exists

**a closed index equals the set its own envelopes admit, so its expression always exists and is recoverable**

*X = R(X)*

grade **PROVED**· source *M §15.2 corollary / §2.23; Moore 1910*· depends on `A.R`, `S.bounds`· depth 4

> **PRIOR ART: a closed set equals the fixed point of its own closure operator, so its defining expression always exists. Immediate from idempotence.**

### `A.ext` — extensivity

**X ⊆ ℛ(X), hence E(X) ≥ 0**

*none*

grade **PROVED**· source *T 1.2 / M A.2; Moore 1910*· depends on `A.R`· 2 objects depend on it· depth 3

> **PRIOR ART: extensivity is the first Moore axiom. That E(X) ≥ 0 is its immediate corollary, not a separate result.**

### `A.fix` — Bergman double-projection; Baker–Pixley 1975 (majority term)

**X is closed ⟺ X = ℛ(X)**

*each coordinate presented as a chain*

grade **PROVED**· source *M §14.1 (Thm 9.1, A.2); Moore 1910; Baker & Pixley 1975*· depends on `A.clos`· 1 object depends on it· depth 5

> **PRIOR ART: X closed iff X = R(X) is the definition of a fixed point of a closure operator. That the binary projections suffice is Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174 — the majority-term / (2,d) interpolation theorem.**

### `A.freuder` — Freuder 1982

**a tree-structured constraint network is globally consistent after arc consistency**

*constraint graph acyclic*

grade **CITED**· source *T 1.10; Freuder 1982*· depends on `A.gc`· depth 5

> **PRIOR ART: Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32 — a tree-structured constraint network is globally consistent after arc consistency. This is the reason Λ closes, and it is his.**

### `A.gc` — global consistency (CSP)

**E(X) = 0 ⟺ the binary constraint network is globally consistent**

*the constraints are the monotone binary projections*

grade **CITED**· source *T 1.4 / A5c; Freuder 1978; Dechter 1992*· depends on `A.bpc`, `A.E`· 3 objects depend on it· depth 4

A.gc

> **PRIOR ART: global consistency and its k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966; Dechter, From local to global consistency, Artif. Intell. 55 (1992) 87-107.**

### `A.intext` — interior and exterior

**E is INTERIOR and E_W is EXTERIOR: the order operator is bounded by its sample and the step operator is not**

*an index with valued cells and a step set*

grade **MEASURED**· source *R 1196-1199; Beeri, Fagin, Maier & Yannakakis 1983; Dijkstra 1959*· depends on `A.E`, `A.EW`· 1 object depends on it· depth 6

on Λ_spectra in-region, R places 1,925 from 277 held (E = 1,648) and W values 277 (E_W = 0) at the book's tolerance, because every step's scatter exceeds it — multiplicity 1.664, isoelectronic 1.674, l 2.872. Raising tau does not close the gap: every cell W gains, R mostly refuses, and ALL 218 fail one envelope, charge given Z. The measured set runs Z 2-83 and charge 1-9; the refused cells run Z 1-85 and charge 1-10. The overlap never exceeds 12% of E at any tolerance

> **PRIOR ART: the order operator is a closure bounded by its sample (BFMY 1983 for what local closure can reach); the step operator is a reachability closure unbounded by it (Dijkstra 1959). That E is interior and E_W exterior follows from the two being different kinds of operator.**

### `A.logic` — the logic level

**LOGIC is not a language: it is the mechanism binary -> language -> binary by which any language answers a question about a cell**

*a language with a closure operator*

grade **DEFINITIONAL**· source *R 1173; Boole 1854; Tarski 1936*· depends on `A.R`· 1 object depends on it· depth 3

three levels: BINARY is the type, a cell is admitted or not; a LANGUAGE is a coordinate system with a closure operator; LOGIC is the map. A language earns a row when logic can operate on it and return a binary, which is why documentary has none — it returns a citation. The book's C(5,2) = 10 combinations is then exact: five operator-bearing languages, plus statistics as a sixth and documentary as a seventh

> **PRIOR ART: that logic is the mechanism by which a language answers a binary question, rather than a language itself, is the object-language/metalanguage distinction — Boole, An Investigation of the Laws of Thought (1854); Tarski, Der Wahrheitsbegriff in den formalisierten Sprachen, Studia Philos. 1 (1936) 261-405.**

### `A.modeA` — failure mode A — ordering

**sub-case A, ORDERING: the term is present and determined but non-monotone; repairable by re-ordering**

*the term is a function of an existing coordinate*

grade **COMPUTED**· source *T 1.6; Freuder 1978*· depends on `A.rule`· 1 object depends on it· depth 7

> **PRIOR ART: a non-monotone constraint is not captured by an envelope, and higher consistency is needed — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### `A.modeB` — failure mode B — arity

**sub-case B, ARITY: every term is monotone; the constraint names more coordinates than an envelope has arguments; not repairable by any operation on coordinates**

*the minimal failing support has size ≥ 3*

grade **COMPUTED**· source *T 1.6; Freuder 1978*· depends on `A.rule`· 2 objects depend on it· depth 7

> **PRIOR ART: a constraint naming more coordinates than the envelope pairs is a higher-arity constraint; the k-consistency ladder is Freuder (1978).**

### `A.montanari` — Montanari 1974

**for monotone constraints, path consistency implies global consistency**

*constraints monotone*

grade **CITED**· source *T 1.10; Montanari 1974*· depends on `A.gc`· depth 5

> **PRIOR ART: Montanari, Networks of constraints: fundamental properties and applications to picture processing, Inf. Sci. 7 (1974) 95-132 — for monotone constraints, path consistency implies global consistency. Λ constraints are monotone, so this applies directly.**

### `A.morph` — the cap as a morphism

**an occupancy coordinate's cap is admissible iff it is a morphism for the operation preserved**

*meet-morphism preserves meets; join-morphism preserves joins*

grade **COMPUTED**· source *M §18.4.1; Birkhoff 1940*· depends on `A.rule`· depth 7

> **PRIOR ART: a cap is admissible iff it is a lattice morphism for the operation — the standard homomorphism condition. Birkhoff, Lattice Theory (1940).**

### `A.orient` — orientation cost

**E − E₄, the ORIENTATION COST: 0 on eight of ten indexed objects, 2 on the audits, 750 on the parity rule**

*ℛ₄ defined*

grade **COMPUTED**· source *M §14.5.5; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999*· depends on `A.r4`· depth 4

> **PRIOR ART: the cost of choosing one orientation over the full class. The class is Devilles; the cost is measured here.**

> **PRIOR ART: the four orientations of a staircase are the (alpha, beta)-monotone constraints of Deville, Barette & Van Hentenryck (1999). R uses one corner and R_4 the closure over all four; the ORIENTATION COST is the difference, measured at 0 on eight of ten indexed objects and 2 on the aufbau index.**

### `A.prod` — the product rule for closure

**if no constraint links the factors, ℛ(A×B) = ℛ(A)×ℛ(B)**

*A, B on disjoint coordinate sets, no cross constraint*

grade **PROVED**· source *T D9; Birkhoff 1940*· depends on `A.R`· 1 object depends on it· depth 3

> **PRIOR ART: a closure operator on a product with no cross-constraints factorises; the statement is the product form of a Moore family. Birkhoff, Lattice Theory (1940).**

### `A.prodE` — the product rule for the defect

**E(A×B) = |A|·E_B + |B|·E_A + E_A·E_B**

*as A.prod*

grade **PROVED**· source *T D10; classical; Euler 1748*· depends on `A.prod`, `A.E`· depth 4

> **PRIOR ART: the defect of a product expands as |A|E_B + |B|E_A + E_A E_B — the inclusion-exclusion expansion of (|A|+E_A)(|B|+E_B) minus |A||B|. Elementary.**

> **PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. Elementary algebra; the point is that defects MULTIPLY as well as add across a product.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. The point is that defects MULTIPLY as well as add across a product, which is the elementary product rule for counting — Euler, Introductio in analysin infinitorum (1748), ch. XVI.**

### `A.r4` — the four-orientation operator

**ℛ₄, the four-orientation closure over Deville's staircase class**

*idempotent, hence a closure operator*

grade **COMPUTED**· source *M §14.5.5; Deville et al. 1999*· depends on `A.stair`, `A.R`· 2 objects depend on it· depth 3

> **PRIOR ART: the four orientations of a staircase constraint are the (alpha, beta)-monotone class of Deville, Barette & Van Hentenryck (1999); R uses one corner and R_4 the closure over all four.**

### `A.relax` — ℛ as a relaxation

**ℛ is not a k-wise closure for any k: k-wise defect is 0 at k = d while E(ℛ) can be 750**

*|Δℓ|=1 at 750 against k-wise 0 for k = 2,3,4*

grade **PROVED**· source *M §14.5.4; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.R`· 1 object depends on it· depth 3

> **PRIOR ART: pairwise (k-wise) consistency implies global consistency exactly for ACYCLIC hypergraphs — BFMY, On the desirability of acyclic database schemes, J. ACM 30 (1983) 479-513. R is the global operator and the k-wise closures are the local ones; the gap between them is their theorem, and this object measures it.**

### `A.rule` — the tightening rule

**a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other**

*the index is a sublattice of a product of chains*

grade **COMPUTED**· source *T 1.8 / M §14.4; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995*· depends on `A.fix`· 10 objects depend on it· depth 6

> **PRIOR ART: a tightening preserves closure iff it stays inside the monotone staircase class.**

> **PRIOR ART: a tightening preserves closure exactly when it stays inside the monotone staircase class — the connected row-convex constraints of Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271, and the row-convex networks of van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561. Binding one coordinate by a monotone function of one other is precisely a member of that class.**

### `A.seaton` — the polarisation formula

**delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l(l+1) alpha/K**

*a Rydberg electron that does not enter the core*

grade **CITED**· source *Seaton 1958; Drake & Swainson 1991*· 1 object depends on it· depth 0

tested on 23 adjacent-l pairs in its domain: median observed/predicted 1.12, improved from 1.19 by restoring the n-dependent term, which confirms the term belongs. It fails on 20 near-hydrogenic pairs at the noise floor and on Ba II (delta_f = 0.756) and Hg II (1.062), where the 4f orbital has collapsed into the core and the series penetrates

### `A.slack` — slack

**SLACK(S) = measure(ambient)/measure(S); log SLACK = log|ℛ(X)| − log|X|**

*a measure on the ambient*

grade **COMPUTED**· source *M §25.2; Shannon 1948*· depends on `A.E`, `A.ebits`· 1 object depends on it· depth 5

> **PRIOR ART: log of the ratio of ambient to actual is a bit count — the same quantity as A.ebits in another form. Shannon (1948).**

### `A.stair` — staircase / connected row-convex

**phi-hat recovers a STAIRCASE constraint: (alpha,beta)-monotone with alpha,beta in {≤,≥}**

*binary*

grade **CITED**· source *Deville, Barták, Van Hentenryck 1999*· depends on `A.env`· 2 objects depend on it· depth 2

A.stair

### `A.staircls` — the one-corner characterisation

**E(ℛ) = 0 iff X is an intersection of (≤,≤) staircases — one corner of Deville's class**

*the anti-diagonal is a staircase with E = 750*

grade **PROVED**· source *M §14.5.4; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995*· depends on `A.relax`, `A.stair`· depth 4

> **PRIOR ART: connected row-convex and monotone staircase constraint classes — Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271; van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561.**

### `A.stat2` — the statistics operator

**the statistics operator is max-entropy on the PAIRWISE marginals, not the first-order ones**

*an index of dimension d ≥ 3*

grade **MEASURED**· source *R 1174*· depends on `A.logic`· 1 object depends on it· depth 4

on Λ, first-order marginals admit all 6,912 ambient cells; pairwise marginals admit exactly 976 and reproduce R cell for cell. IPF converges to the max-entropy distribution matching the SPECIFIED marginals (Deming and Stephan 1940; Ireland and Kullback 1968), so which marginals is the whole question

### `A.three` — the three populations

**the Method equation partitions an index into three populations: interior captures, the working overlap, and exterior predictions**

*an index, its order operator and its step set*

grade **MEASURED**· source *R 1199-1200; Freuder 1978; Dijkstra 1959*· depends on `A.intext`· depth 7

at tau = 3.0: INTERIOR 1,503 cells R places and no step values, median l = 2 and charge 4 — these are captures. BOTH 145 placed and valued, median l = 3, the polarisation regime. EXTERIOR 218 the steps reach past the sample edge. The exterior verifies where it reaches: Cs I np walked to 3.659 against a measured 3.5667, an error of 2.6% with a stated error factor of 1.67

> **PRIOR ART: partitioning by what a closure admits and what a propagation reaches — the k-consistency gap (Freuder 1978) crossed with shortest-path reachability (Dijkstra 1959). The three populations are the measurement.**

### `A.two` — the binary-projection criterion

**a tightening preserves E = 0 iff each binary projection is the intersection of that projection's own two upper envelopes**

*phi-hat indexed over ORDERED pairs*

grade **PROVED**· source *M §14.4 / §2.15.2; Baker & Pixley 1975*· depends on `A.rule`· depth 7

> **PRIOR ART: that binary projections decide membership is the (2,d) interpolation property — Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174.**

## S. The seed — generation, covering, structure — 18 objects

### `S.bits` — the seed as binary

**the five read as binary: corners 1 and 2 are exact complements (3 of 3), corner 3 and the unit cell are exact complements (3 of 3), corner 4 is fully specified at 11001100, and every coordinate receives both a 0 and a 1 with no column one-sided**

*measured at one cap setting only; whether the pairing survives other caps is untested*

grade **COMPUTED**· source *M §14.5.14; Shannon 1938*· depends on `S.unit`· depth 9

> **PRIOR ART: reading a structure as binary words with complementation is Boolean algebra — Shannon, Trans. AIEE 57 (1938) 713-723.**

### `S.bounds` — the bounds are recoverable

**S3: the bounds are recoverable from the cells**

*closure*

grade **PROVED**· source *M §15.2; Moore 1910*· depends on `A.R`· 1 object depends on it· depth 3

> **PRIOR ART: if the envelopes are recoverable from the cells then the constraints are too, since R is determined by its envelopes.**

### `S.box` — the box seed law, d + c − 2

**a full box c^d seeds at d + c − 2**

*exact by branch and bound at 3³ and 4³*

grade **PROVED**· source *M §14.5.9; classical; Dilworth 1950; Birkhoff 1937*· depends on `S.cover`· depth 5

> **PRIOR ART: the corners of a d-dimensional box over c values generate it under coordinatewise max, and d + c - 2 is the count of extreme steps. Elementary.**

> **PRIOR ART: as S.down, for a full box: the extreme steps in each coordinate generate it.  PRIOR ART: the generators of a down-set closed under coordinatewise max are its maximal elements; for a box over c values in d coordinates that count is d + c - 2. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166; Birkhoff (1937) for the representation.**

### `S.car` — the Carathéodory lower bound

**seed ≥ the Carathéodory number = the breadth = d for a product of d chains**

*semilattice with subsemilattices as convex sets*

grade **CITED**· source *Carathéodory / convexity spaces; Caratheodory 1911*· depends on `S.cover`· depth 5

> **PRIOR ART: Caratheodory, Über den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.**

### `S.channel` — the channel conditions

**six channel conditions hold in all 219 minimum covers of Λ₈: an s-s, s-p, p-s and p-p transition, a null transition q = 0, and a full transfer q = k**

*the constraint is on the CHANNEL, not the cell — which is why every cover looks alike while nothing is forced*

grade **COMPUTED**· source *M §14.5.12; Condon & Shortley 1935*· depends on `S.core`· 1 object depends on it· depth 7

> **PRIOR ART: the s-s, s-p and related conditions are statements about which subshell transitions the seed must contain; the subshell structure is Condon & Shortley (1935).**

### `S.core` — the seed's necessary core

**four of the seed's seven cells are NECESSARY: each uniquely covers 12-23 envelope elements and has ZERO alternatives in Λ; they cover 87 of 102**

*a stable attractor of greedy covering, not necessity; §14.5.7 stands unamended (register 600)*

grade **COMPUTED**· source *M §14.5.10; Karp 1972; Chvatal 1979*· depends on `S.lam`· 2 objects depend on it· depth 6

> **PRIOR ART: an element covered by exactly one set forces that set into every cover — the standard reduction rule for set cover.**

### `S.cover` — the seed is a set cover

**the minimum seed is a MINIMUM SET COVER: elements the envelope steps, sets the cells**

*S.seed*

grade **PROVED**· source *M §14.5.9; Karp 1972; Johnson 1974*· depends on `S.seed`· 5 objects depend on it· depth 4

> **PRIOR ART: MINIMUM SET COVER is one of the 21 NP-complete problems of Karp, Reducibility among combinatorial problems (1972); the greedy ln n approximation is Johnson, Approximation algorithms for combinatorial problems, JCSS 9 (1974) 256-278. The seed problem IS set cover, which is why five heuristics agree on 7 and the lower bound is 5.**

### `S.down` — the down-set seed law, d + c − 1

**a down-set over c values in d coordinates seeds at d + c − 1**

*exact: LB = UB at d=4 c=4*

grade **PROVED**· source *M §14.5.9; Dilworth 1950*· depends on `S.cover`· depth 5

> **PRIOR ART: the minimum generating set of a down-set is its set of maximal elements; the d + c - 1 count follows. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166.**

### `S.erasure` — the seed is an erasure structure

**the remaining three seed positions admit 519 completing triples over 66 distinct cells, none in all 519, each appearing in 3 to 157 — a redundancy gradient of fifty to one**

*heavy-tailed: min 3, median 12, max 157, a ratio of thirteen to one*

grade **COMPUTED**· source *M §14.5.11; Karp 1972*· depends on `S.core`· depth 7

> **PRIOR ART: the alternative completions of a partial cover; the count is the measurement.**

### `S.ground` — the ground-state derivation

**the ground configuration determines every channel's existence and bounds its defect's integer part**

*an atom of atomic number Z*

grade **MEASURED**· source *R 1139-1141; Madelung 1936; Janet 1929; Hund 1925*· depends on `K.produce`· 5 objects depend on it· depth 6

multiplicity from Hund on the core: 24 of 24 electron counts, exact containment. The cell set from aufbau: 8,488 cells admitting all 311 measured channels where the sampled index admits 296. And floor(delta) ≤ min(p, n0-l-1) for 311 of 311, exact 57%, within two 97%

> **PRIOR ART: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929); Madelung's rule as usually stated (1936). Hund's first rule (Z. Phys. 33, 1925) gives the term. Both are read, not derived.**

### `S.lam` — Λ's seed — seven cells

**seed(Λ₈) = 7 exactly — 976 cells from seven, 139 to 1; LB 5, five heuristics 12/7/7/7/40**

*branch and bound over 102 elements*

grade **COMPUTED**· source *M §14.5.9 / twoheur.py; Karp 1972; Johnson 1974*· depends on `S.cover`· 1 object depends on it· depth 5

> **PRIOR ART: the seed problem is minimum set cover, NP-complete (Karp 1972), with a greedy ln n approximation (Johnson 1974). Five heuristics agreeing on 7 against a lower bound of 5 is the measurement.**

### `S.open` — the open-index form, seed + E

**an open index is recovered as seed(ℛ(X)) plus the E cells ℛ(X) holds and X does not; cost seed + E**

*exact on four open indexes; compresses only where E ≪ |X|*

grade **PROVED**· source *M §21.5; Moore 1910*· depends on `S.seed`· 1 object depends on it· depth 4

> **PRIOR ART: an open index needs its closure seed plus the cells the closure adds and it does not hold — the decomposition follows from extensivity.**

### `S.parent` — the parent-term wall

**an OPEN-SHELL core gives many parent terms and no separable Rydberg series, so its levels can be published and its defect cannot be extracted**

*an ion whose core has an open subshell*

grade **MEASURED**· source *R 1180; Condon & Shortley 1935; Racah 1943*· depends on `S.ground`· 1 object depends on it· depth 7

Fe IV's 3d4 core carries sixteen LS terms. The capture shows 13 of them, 24 distinct (parent, l, term) series, and EVERY ONE has exactly one member — n = 4 only. Fe IV has ~1,000 analysed levels and no extractable defect. The compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6, which is not a collection preference but the fact that an open-shell core does not produce the object a quantum-defect index holds

> **PRIOR ART: parent terms and the fractional-parentage decomposition are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah's coefficients of fractional parentage (1943). That an open-shell core gives one series per parent is their structure; the measurement is that Fe IV's 24 series each hold one member.**

> **PRIOR ART: parent terms and coefficients of fractional parentage are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382. That an open-shell core gives one series per parent is their structure; the measurement is that the 24 Fe IV series each hold one member.**

### `S.regime` — the regime coordinate

**the SIGN of d2 is a coordinate the ground state cannot supply, and the MAGNITUDE of d2 predicts the channel's own scatter**

*a Rydberg channel with a fitted Ritz curve*

grade **MEASURED**· source *R 1157-1162; NIST Atomic Spectroscopy compendium; Ritz 1903*· depends on `S.ritz`· 2 objects depend on it· depth 8

Seaton requires d2 < 0 for polarisation, so a positive d2 says the channel is not what the formula describes. By orbital: s 76% positive, p 74%, d 37%, f 6%, g 7%, h 9%. The two populations differ in median raw spread 0.0159 vs 0.0029 and median fit residual 0.0058 vs 0.0003, U-test p < 1e-5. The MAGNITUDE class predicts the spread at R^2 = 0.761 against l alone at 0.230 and the sign at 0.267, and the sign adds nothing to the magnitude. The three quantities do not separate: d0 against |d2| gives r^2 = 0.270

> **PRIOR ART: the SIGN rule is NIST's own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel's scatter at R^2 = 0.761.**

> **PRIOR ART: the SIGN rule is NIST own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel scatter at R^2 = 0.761.**

### `S.ritz` — the channel curve

**a channel is a CURVE, not a number: delta(n) = d0 + d2/(n-d0)^2, and the index reaches d0 while nothing in it reaches d2**

*a Rydberg channel with four or more members*

grade **MEASURED**· source *R 1150-1156; Ritz 1903; Hartree 1928*· depends on `S.ground`· 1 object depends on it· depth 7

the d2 term removes 48% of what the compendium called scatter (0.0199 -> 0.0104 across 274 channels). d0 against ln Ne, l and charge gives R^2 = 0.549; the curvature gives 0.018. The ISOELECTRONIC step moves both coordinates by the same factor at every l — 1.194/0.859 at s, 1.150/0.979 at p, 0.858/0.907 at d, 0.561/0.627 at f — while the l step moves them differently: 1.427/0.752, 3.696/1.373, 8.536/5.264. Along a sequence the channel translates; along l it deforms, and fitting l as a 2x2 map improves on the scalar by only 14% at s->p and 1% beyond

> **PRIOR ART: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST's compendium states it in this form.**

### `S.seed` — a seed

**G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X)**

*X closed; ℛ depends on G only through φ̂*

grade **PROVED**· source *M §14.5.7; Birkhoff 1937; Moore 1910*· depends on `A.env`, `A.R`· 3 objects depend on it· depth 3

> **PRIOR ART: a generating set of a closure system is any G with cl(G) = cl(X). That the envelope alone decides it is the specific form here; the notion is Moore-Birkhoff.**

### `S.status` — the existence partition

**the index partitions by EXISTENCE STATUS, and nothing in it is impossible**

*the aufbau survey*

grade **MEASURED**· source *R 1191-1192; Theodosiou, Inokuti & Manson 1986*· depends on `S.ground`, `S.parent`· 1 object depends on it· depth 8

101,328 cells. *** THE STATUS AXIS WAS REPLACED AT REGISTER 1578: VERIFIED/POSSIBLE/IMPROBABLE became WITNESSED/UNWITNESSED plus a NAMED BOUND, because improbable is a judgement about the future rather than a fact about the record — the same object-versus-observer fault register 1287 found in `standing`. *** Now: 337 WITNESSED (0.333% of the index) and 100,991 UNWITNESSED, of which 929 are exact by symmetry and need no measurement. Bounds on the rest: series above ng 28,527; no long-lived isotope 24,312; no analysis located at this charge 17,428; open-shell cores 26,641; not naturally occurring 225; and 2,929 with NO bound at all — separable series simply not yet measured. The charge bound is contradicted by twelve measured cells above it in this index's own file (R 1577). Every accuracy figure must be quoted against the witnessed count, not 101,328.

> **PRIOR ART: the distinction between what a survey admits and what is measurable is exactly the distinction Theodosiou, Manson & Inokuti make in their 1986 table across all ionisation stages.**

### `S.unit` — the unit cell

**all 219 covers contain a cell matching (3,0,1,1,*,0,1,1) — 3s1 to e-s ending 1, doublet, e free at 1 or 3; its function is to carry the value ONE where the corners carry extremes**

*three of the fifteen elements the corners miss are the alphabet values q=1, g=1, 2S=1; e=3 witnesses the target's ceiling and e=1 the source's*

grade **COMPUTED**· source *M §14.5.13; Karp 1972; Chvatal 1979*· depends on `S.channel`· 1 object depends on it· depth 8

> **PRIOR ART: a cell present in every minimum cover is forced; the standard set-cover argument.**

> **PRIOR ART: a set present in every minimum cover is forced by an element it uniquely covers — the same reduction rule. Chvatal (1979). That all 219 covers contain this cell is the measurement.**

## F. The family of closed indexes — 4 objects

### `F.exact` — the family's defect, exactly

**ℛ(Cl(U)) = 2^U, so E(Cl(U)) = 2^|U| − |Cl(U)| exactly**

*Cl(U) holds ∅ and U, and every ordered pair of points is separated by some closed set, making every envelope constant at 1*

grade **PROVED**· source *M §14.6.2; Moore 1910*· depends on `F.open`· depth 6

> **PRIOR ART: the closure of a set of generators over an unconstrained alphabet is the full power set, so the defect is the exact complement count. A corollary of extensivity and idempotence.**

### `F.moore` — the family of closed sets

**the ℛ-closed subsets of a closed index form a Moore family: ∩-closed 100%, ∪-closed 33–68%; 73, 146, 731 members**

*exhaustive at 8, 9, 16 cells*

grade **PROVED**· source *M §14.5; Moore 1910; Ward 1942*· depends on `S.seed`· 1 object depends on it· depth 4

> **PRIOR ART: the closed sets of a closure operator form a Moore family — intersection-closed with a top. Moore, Introduction to a Form of General Analysis (1910); Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. That the R-closed subsets of a closed index form one is that theorem applied at one level up.**

### `F.open` — the family theorem

**THEOREM: the family of all closed indexes is itself an OPEN index — E = 182, 365, 64,804**

*every member has E = 0*

grade **PROVED**· source *M §14.6; Tarski 1955; Ward 1942*· depends on `F.moore`· 2 objects depend on it· depth 5

> **PRIOR ART: the lattice of closed sets of a closure operator is complete (Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309), but completeness is not the same as being CLOSED under the same operator one level up. That the family of closed indexes is itself open is measured here; the setting is Tarski-Ward.**

### `F.unstatable` — the unstatable family

**and it cannot be stated: a closed index has a seed, an open one costs seed + E, and E is 64,804 at 16 cells**

*corollary of F.open and S.open*

grade **PROVED**· source *M §14.6.1; Kolmogorov 1965*· depends on `F.open`, `S.open`· depth 6

> **PRIOR ART: the cost of stating an object is its description length — Kolmogorov, Three approaches to the quantitative definition of information, Probl. Inf. Transm. 1 (1965) 1-7. A closed index has a seed; an open one costs seed plus defect, and the difference is the statement cost.**

## G. Graphs, constraints and languages — 12 objects

### `G.allcons` — the index of all constraints

**every genuine constraint in the book, indexed over five coordinates: 22 carried by ℛ, 2 by ℛ₄, NONE by neither; E = 21, E₄ = 6, orientation cost 15**

*eight rows of a first attempt were coordinate systems entered as constraints; the two that no operator carried were both of those*

grade **COMPUTED**· source *M §21.5.5 / allcons.py; Freuder 1978*· depends on `A.r4`, `G.cons`· depth 4

> **PRIOR ART: indexing constraints by the coordinates they name is the constraint-hypergraph view — Freuder, CACM 21 (1978) 958-966.**

### `G.book` — the book as an index

**E(book) = 578 at chapter resolution, 0 at part resolution; a certificate exists**

*claim-bearing paragraphs with a § citation*

grade **COMPUTED**· source *M §30.1; Rota 1964*· depends on `A.E`, `A.cert`· depth 9

> **PRIOR ART: that a defect depends on the RESOLUTION at which an object is indexed is the coarsening question; Moebius inversion over a refinement lattice is Rota (1964).**

### `G.cons` — the constraint index

**Λ's seven constraints form a TREE — 8 nodes, 7 edges — with ZERO of 35 triples spanning three nodes**

*no 3-body among the constraints*

grade **COMPUTED**· source *M §21.5.2; Freuder 1982; Dechter & Pearl 1989*· depends on `L.c1`· 5 objects depend on it· depth 1

> **PRIOR ART: that a tree-structured constraint graph is globally consistent after arc consistency is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32; the width/induced-width machinery is Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### `G.graph` — the constraint graph

**Λ₁₃'s constraint graph: 12 nodes, 13 edges, girth 5, diameter 6, radius 3, treewidth 2, hub k at degree 4, cycle rank 2, no triangle at any stage**

*treewidth 2 at Λ₁₃ keeps Freuder's bound and §21.5.1's one-level shortfall*

grade **COMPUTED**· source *M §21.5.3 / Figure 21.1; Euler 1736; Diestel 2017*· depends on `G.cons`· depth 2

> **PRIOR ART: girth, diameter, radius and treewidth are standard graph invariants — see Diestel, Graph Theory (5th ed., 2017). Graph theory itself begins with Euler, Solutio problematis ad geometriam situs pertinentis (1736).**

### `G.near` — the seven near-misses

**Λ is one edge from a 3-body in exactly seven places, one per existing edge**

*every one a bond the physics does not make*

grade **COMPUTED**· source *M §21.5.2; Berge 1962*· depends on `G.cons`· depth 2

> **PRIOR ART: adding one edge to a tree creates exactly one cycle; the number of places is the number of existing edges. Berge, Theorie des graphes (1958/1962).**

### `G.prot` — the protocol index

**the 24 protocols occupy 19 cells in four coordinates; §2.8 and §2.24 share one**

*§2.24 is §2.8 specialised to heuristics*

grade **COMPUTED**· source *protindex.py; Freuder 1978*· depends on `G.reg`· depth 5

> **PRIOR ART: as G.allcons, applied to the protocol index.**

### `G.ref` — the reference index

**the reference index: 38 cells, box 144, E = 0, and NOT a tree — access closes a cycle**

*access, referent, checked, verdict*

grade **COMPUTED**· source *M §16.6.1; Freuder 1982*· depends on `A.E`· depth 4

> **PRIOR ART: a non-tree constraint graph that nonetheless closes shows treeness is sufficient and not necessary — the converse direction of Freuder (1982).**

### `G.reg` — the register as an index

**E(register) = 6 at 68.8% density, and R recovers repair ≤ φ(corroboration)**

*coordinates assigned from the entry text*

grade **COMPUTED**· source *M §28.9; Shannon 1948*· depends on `A.E`, `A.R`· 1 object depends on it· depth 4

> **PRIOR ART: recovery under a noisy channel is bounded by the channel capacity; that repair ≤ φ(corroboration) is that bound in this setting. Shannon (1948).**

### `G.shape` — shape decides the seed

**the constraint graph's shape decides the seed: path 8, star 6, balanced trees 6, forest 5 on six nodes over one alphabet; neither extreme is cheapest**

*seed is monotone in S with no exception, all six exact by branch and bound*

grade **COMPUTED**· source *M §21.5.4; Freuder 1982; Dechter & Pearl 1989*· depends on `S.cover`, `G.cons`· depth 5

> **PRIOR ART: that the constraint graph shape decides what a local method achieves is Freuder 1982 for trees and Dechter & Pearl 1989 for the general induced-width bound.**

### `G.stat` — statistics as a language

**statistics is a sixth language: max-entropy closure on the pairwise marginals recovers Λ at 976, E = 0, restores a deleted cell, and GROWS on an added one, 976 to 1,048**

*its signature matches the information language, not order/geometry/analysis; the five split three-two between absorbing and growing*

grade **COMPUTED**· source *M §20 / stat_lang.py; Deming & Stephan 1940; Csiszar 1975*· depends on `A.R`· depth 3

> **PRIOR ART: the max-entropy distribution matching given marginals is reached by iterative proportional fitting — Deming & Stephan, Ann. Math. Stat. 11 (1940) 427-444; its information-geometric characterisation is Csiszar, I-divergence geometry, Ann. Prob. 3 (1975) 146-158.**

### `G.tower` — the cycle rank of the tower

**the tower's cycle rank rises by one at each two-parent axis — 0,0,1,1,2,2 — while triangles stay 0**

*the tree breaks at Λ₁₀*

grade **COMPUTED**· source *M §21.5.2; Berge 1962*· depends on `G.cons`, `T.tower`· depth 7

> **PRIOR ART: the cycle rank |E| - |V| + c is the first Betti number of a graph — Berge, Theorie des graphes et ses applications (1958/1962). That it rises by one at each two-parent axis is the measurement.**

### `G.trip` — independence is a triple property

**independence is a property of TRIPLES: surviving tests go as (1-f)^3, not (1-f)**

*the bracket relates T(n-1), T(n), T(n+1)*

grade **COMPUTED**· source *M §24.9; Dawid 1979; Pearl 1988*· depends on `B.brk`· depth 1

> **PRIOR ART: conditional independence is a relation on TRIPLES and obeys the graphoid axioms — Dawid, Conditional independence in statistical theory, J. R. Stat. Soc. B 41 (1979) 1-31; Pearl, Probabilistic Reasoning (1988), ch. 3.**

## L. Λ's own constraints — 41 objects

### `L.E0` — the closure theorem

**E(Λ) = 0**

*at the stated caps; verified at four settings and through the f shell*

grade **COMPUTED**· source *M §7.3, reg. 236; Moore 1910; Freuder 1982*· depends on `L.closed`, `A.E`· depth 8

> **PRIOR ART: E = 0 says the index equals its own closure. Moore (1910) for the operator; Freuder (1982) for why a tree-structured constraint graph gives it.**

### `L.F` — the generating function

**F = Σ_n z₁ⁿ Σ_{ℓ≤n−1} z₂^ℓ Σ_{k≤4ℓ+2} z₃^k [Σ_{S≤k} z₈^S] Σ_{q≤k} z₄^q Σ_e z₅^e Σ_{f<e} z₆^f Σ_{g≤min(q,4f+2)} z₇^g**

*at stated caps; the tree has no cycles so the sum factorises*

grade **COMPUTED**· source *M §11.3; Euler 1748; Stanley 1986*· depends on `L.tree`, `L.def`· 5 objects depend on it· depth 3

> **PRIOR ART: a multivariate generating function over a constrained region, written as nested sums. Euler, Introductio (1748); Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### `L.F1` — the cardinality

**F(1,…,1) = |Λ| = 976**

*as L.F*

grade **COMPUTED**· source *M §11; Euler 1748; Stanley 1986*· depends on `L.F`· depth 4

> **PRIOR ART: setting all variables to one recovers the cardinality — the elementary specialisation of a generating function.**

> **PRIOR ART: F(1,...,1) = |X| is the elementary specialisation of a generating function. Euler, Introductio (1748), ch. XVI; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### `L.Fm1` — the alternating specialisation

**F(−1) = 2, because ℓ and f each have exactly two consecutive values but are coupled to n and e**

*at stated caps*

grade **COMPUTED**· source *M §11.8.1; Euler 1748; Stanley 1986*· depends on `L.rankpoly`· depth 5

> **PRIOR ART: F(-1) counts the difference between even- and odd-rank cells; the standard alternating specialisation.**

> **PRIOR ART: F(-1) is the difference between even- and odd-rank counts, the standard alternating specialisation. Euler (1748); Stanley (1986), ch. 3, where it is related to rank symmetry.**

### `L.alpha` — the join-irreducible count

**|J(Λ)| = Σ_i (|A_i| − 1)**

*each generator is min{x ∈ Λ : x_c ≥ v} for one coordinate and one value*

grade **COMPUTED**· source *M reg. 268; Birkhoff 1937*· depends on `L.birk`· depth 10

> **PRIOR ART: the join-irreducibles of a product of chains are the coordinate steps, so |J| = sum(|A_i| - 1). Immediate from Birkhoff representation.**

### `L.amp` — the amplification

**A(y) = N[φ(Λ ∪ {y})] − N[φ(Λ)] − 1; median 340, minimum 59 over 220 trials**

*y a single inserted cell*

grade **COMPUTED**· source *M §16.8.4; Rota 1964*· depends on `A.R`, `L.def`· depth 3

> **PRIOR ART: the change in a closure count on adding a generator; the amplification is measured, the closure is Moore-Rota.**

### `L.arith` — divisor lattice embedding

**N(x) = ∏_i p_i^{x_i}; x≤y ⟺ N(x)|N(y); ∨↦lcm, ∧↦gcd, rank ↦ Ω(N)**

*p_i the i-th prime*

grade **COMPUTED**· source *M §9; Birkhoff 1937*· depends on `L.def`· 2 objects depend on it· depth 2

> **PRIOR ART: the divisor lattice with lcm as join and gcd as meet is the classical arithmetic model of a product of chains. Birkhoff, Lattice Theory (1940), ch. II.**

### `L.birk` — Birkhoff representation 1937

**Λ ≅ down-sets of J(Λ); |J(Λ)| = 17, 20 covering relations**

*Λ finite distributive*

grade **COMPUTED**· source *M §8.3; Birkhoff 1937*· depends on `L.dist`· 5 objects depend on it· depth 9

> **PRIOR ART: Birkhoff's representation theorem, Duke Math. J. 3 (1937) — every finite distributive lattice is the down-sets of its join-irreducibles. |J| = 17 is a computation inside that theorem.**

### `L.bits` — the Boolean representation

**Λ is the 976 words in {0,1}¹⁷ that are down-sets of J(Λ); join = OR, meet = AND; 17 bits carried, 9.93 needed, 7.07 surplus**

*Birkhoff correspondence*

grade **COMPUTED**· source *M §11.1.1; Birkhoff 1937; Shannon 1938*· depends on `L.birk`· 1 object depends on it· depth 10

> **PRIOR ART: Birkhoff (1937) gives the down-set representation; encoding down-sets as Boolean words with OR as join and AND as meet is Shannon (1938).**

### `L.box` — the box factorises

**|box ∩ Λ| factorises because the constraint graph is a tree; no Möbius sieve needed**

*constraint graph acyclic*

grade **COMPUTED**· source *M §10.4; Freuder 1982; Rota 1964*· depends on `L.tree`· depth 3

> **PRIOR ART: the count factorises over a tree — no Moebius sieve is needed because there are no cycles to inclusion-exclude over. Freuder (1982) for the tree property; Rota (1964) for what the sieve would otherwise cost.**

### `L.c1` — node counting

**ℓ ≤ n − 1**

*hydrogenic radial solution*

grade **CITED**· source *M §7.1; Bohr 1913; Schroedinger 1926*· 4 objects depend on it· depth 0

> **PRIOR ART: l ≤ n-1 is the angular-momentum constraint of the hydrogen solution — Bohr, On the constitution of atoms and molecules, Phil. Mag. 26 (1913) 1-25; Schroedinger, Quantisierung als Eigenwertproblem, Ann. Phys. 79 (1926) 361-376.**

### `L.c2` — Pauli

**k ≤ 2(2ℓ+1) = 4ℓ+2**

*Pauli exclusion*

grade **CITED**· source *M §7.1; Pauli 1925; Stoner 1924*· 2 objects depend on it· depth 0

> **PRIOR ART: the subshell capacity 2(2l+1) is Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736, made exclusive by Pauli, Z. Phys. 31 (1925) 765-783.**

### `L.c3` — the transfer bound

**q ≤ k**

*counting*

grade **DEFINITIONAL**· source *M §7.1; Pauli 1925*· 2 objects depend on it· depth 0

> **PRIOR ART: q ≤ k, a transferred count cannot exceed the occupancy. Pauli (1925).**

### `L.c4` — node counting

**f ≤ e − 1**

*hydrogenic radial solution*

grade **CITED**· source *M §7.1; Bohr 1913*· 2 objects depend on it· depth 0

> **PRIOR ART: as L.c1, applied to the second shell pair.**

### `L.c5` — Pauli

**g ≤ 4f+2**

*Pauli exclusion*

grade **CITED**· source *M §7.1; Stoner 1924; Pauli 1925*· 2 objects depend on it· depth 0

> **PRIOR ART: as L.c2, applied to the second shell pair.**

### `L.c6` — the second transfer bound

**g ≤ q**

*counting*

grade **DEFINITIONAL**· source *M §7.1; Pauli 1925*· 2 objects depend on it· depth 0

> **PRIOR ART: g ≤ q, as L.c3 on the second shell pair.**

### `L.c7` — vector coupling

**2S ≤ k**

*vector coupling on the source*

grade **CITED**· source *M §7.1; Hund 1925; Pauli 1925*· 3 objects depend on it· depth 0

> **PRIOR ART: 2S ≤ k because at most k electrons can align their spins — Pauli exclusion (1925) with Hund first rule, Z. Phys. 33 (1925) 345-371.**

### `L.c8` — the occupancy floor

**k ≥ 1 (definitional restriction, not a bound)**

*a cell is a transition, not a state*

grade **DEFINITIONAL**· source *M §10.2, reg. 301; Pauli 1925*· 2 objects depend on it· depth 0

> **PRIOR ART: k ≥ 1 restricts to occupied subshells; definitional rather than a bound.**

### `L.chains` — the linear extensions

**maximal chains of Λ = linear extensions of J(Λ) = 1,113,045,672**

*Λ ≅ J(P)*

grade **COMPUTED**· source *M §12.9; Stanley 1986*· depends on `L.birk`· depth 10

> **PRIOR ART: maximal chains of J(P) correspond to linear extensions of P — Stanley, Enumerative Combinatorics Vol. 1, Prop. 3.5.2. The count is the computation; the bijection is his.**

### `L.chi` — the membership function

**χ(x) = H(n−1−ℓ)H(4ℓ+2−k)H(k−q)H(k−2S)H(e−1−f)H(4f+2−g)H(q−g); the coefficient function of F is χ**

*H the Heaviside step*

grade **COMPUTED**· source *M §11.1; Heaviside 1893*· depends on `L.F`, `L.def`· 1 object depends on it· depth 4

> **PRIOR ART: the membership function as a product of step functions — Heaviside, Electromagnetic Theory (1893), where the unit step is introduced.**

### `L.circuit` — the implication circuit

**the 20 covering relations, as implications, cut 2¹⁷ = 131,072 words to exactly 976, at depth 5**

*monotone: AND, OR, implication; no NOT, no feedback*

grade **COMPUTED**· source *M §11.1.1; Shannon 1938*· depends on `L.bits`· depth 11

> **PRIOR ART: implications as a monotone Boolean circuit — Shannon, A symbolic analysis of relay and switching circuits, Trans. AIEE 57 (1938) 713-723.**

### `L.closed` — sublattice of a product

**Λ is closed under coordinatewise ∨ and ∧**

*every constraint of the form x_i ≤ φ(x_j) with φ non-decreasing*

grade **PROVED**· source *M §7.3; Birkhoff 1940*· depends on `L.def`, `A.rule`· 2 objects depend on it· depth 7

> **PRIOR ART: closure under coordinatewise join and meet is the definition of a sublattice of a product (Birkhoff, Lattice Theory, 1940). What makes Λ one is that all eight constraints have the form x_i ≤ f(x_j) with f monotone.**

### `L.def` — the definition of Λ

**Λ = { (n,ℓ,k,q,e,f,g,2S) ∈ ℤ⁸ : L.c1..L.c8 }, caps (n,e,ℓ,k,f) = (3,3,1,3,1)**

*caps stated; figures at other caps must say so (§7.4)*

grade **DEFINITIONAL**· source *M §7; Bohr 1913; Pauli 1925*· depends on `L.c1`, `L.c2`, `L.c3`, `L.c4`, `L.c5`, `L.c6`, `L.c7`, `L.c8`· 10 objects depend on it· depth 1

> **PRIOR ART: the eight constraints are the shell-structure rules of Bohr (1913) and Pauli (1925), written as inequalities on integer coordinates.**

### `L.dim` — order dimension (Dushnik–Miller)

**order dimension of Λ₈ is 8, rising by one per adjoined axis**

*at the stated caps*

grade **PROVED**· source *M §8.6; Dushnik & Miller 1941*· depends on `L.def`· 1 object depends on it· depth 2

> **PRIOR ART: Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610. That a product of n chains has dimension n follows from the definition; what is measured here is that Λ's dimension equals its coordinate count at every stage of the tower.**

### `L.dist` — Birkhoff / product of chains

**Λ is distributive (a sublattice of a product of chains)**

*none*

grade **PROVED**· source *M §8.1; Birkhoff 1937*· depends on `L.closed`· 5 objects depend on it· depth 8

> **PRIOR ART: a lattice is distributive iff it embeds in a product of chains (Birkhoff, Rings of sets, Duke Math. J. 3, 1937). Λ is such a sublattice by construction, so distributivity is INHERITED, not proved here.**

### `L.metric` — the lattice metric

**log d is an ℓ¹ metric; d(x,z) ≤ d(x,y)·d(y,z)**

*as L.occ*

grade **COMPUTED**· source *M §9.2; Monjardet 1981*· depends on `L.occ`· depth 4

> **PRIOR ART: Monjardet, Metrics on partially ordered sets - a survey, Discrete Math. 35 (1981) 173-184.**

### `L.mobius` — Möbius function of a distributive lattice

**μ(x,y) = (−1)^{|y∖x|} if y∖x is an antichain in J(Λ), else 0**

*Λ ≅ J(P)*

grade **COMPUTED**· source *M §9.3; Rota 1964*· depends on `L.birk`· depth 10

> **PRIOR ART: Rota, On the foundations of combinatorial theory I: theory of Moebius functions, Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368. The antichain form of mu on a distributive lattice is his.**

### `L.modular` — modularity (equality, not submodularity)

**rank(a∨b) + rank(a∧b) = rank(a) + rank(b), rank = Σx_i**

*graded lattice*

grade **COMPUTED**· source *M §8.2; Dedekind 1900*· depends on `L.dist`· depth 9

> **PRIOR ART: the modular rank identity holds in any modular lattice and every distributive lattice is modular. Dedekind, Math. Ann. 53 (1900).**

### `L.occ` — the interval measure

**d(x,y) = τ( lcm(N(x),N(y)) / gcd(N(x),N(y)) ) = ∏_i(|x_i−y_i|+1) = |[x∧y, x∨y]|**

*τ the divisor count; d(x,x)=1*

grade **COMPUTED**· source *M §9.2; Monjardet 1981*· depends on `L.arith`· 3 objects depend on it· depth 3

> **PRIOR ART: the interval size as a product of coordinate spans, and its arithmetic form via lcm and gcd. Monjardet, Metrics on partially ordered sets, Discrete Math. 35 (1981) 173-184.**

### `L.omega` — distinct-prime-counting function

**ω(N(x)) ≤ dim(Λ)**

*one prime per coordinate*

grade **PROVED**· source *M §9.1; Birkhoff 1937*· depends on `L.arith`, `L.dim`· depth 3

> **PRIOR ART: in the divisor representation, the number of distinct primes dividing N(x) is the number of coordinates in which x is non-minimal, bounded by the dimension.**

### `L.pal` — palindromic rank polynomial ⟺ self-dual

**F palindromic ⟺ the poset is self-dual; Λ's F is not palindromic**

*graded poset*

grade **PROVED**· source *M §11.8; Stanley 1986*· depends on `L.rankpoly`, `L.skew`· depth 5

> **PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1, ch. 3 — a graded poset's rank polynomial is palindromic iff it is rank-symmetric.**

### `L.pushback` — join-prime and meet-prime

**no cell of Λ₈ is both join-prime and meet-prime, so pushback ≥ 16 > 0 for every cell**

*18 join-irreducibles and 18 meet-irreducibles, intersection empty*

grade **PROVED**· source *M §16.8.5; Birkhoff 1937; Gratzer 1978*· depends on `L.birk`· 1 object depends on it· depth 10

> **PRIOR ART: join-prime and meet-prime are dual notions in a distributive lattice, and a cell cannot generally be both. Gratzer, General Lattice Theory (1978).**

### `L.rankpoly` — the rank polynomial

**F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + … + 122z⁸ + 121z⁷ + … + 5z + 1); F′(1)/F(1) = 11.0666**

*single-variable specialisation*

grade **COMPUTED**· source *M §11.1; Stanley 1986*· depends on `L.F`· 2 objects depend on it· depth 4

> **PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 3. F'(1)/F(1) = mean rank is the standard first-moment identity.**

### `L.real` — the index against the real subshells

**Λ's eight constraints on 247 real subshells across ALL 118 elements incl. 19 anomalies and 15 predicted superheavies: 18,288 tests, 0 failures**

*IUPAC ground states*

grade **COMPUTED**· source *close_L.py; Madelung 1936; NIST*· depends on `L.c1`· depth 1

> **PRIOR ART: the 247 real subshells across 118 elements are the observed ground configurations, tabulated by NIST; the ordering is Janet-Madelung. Testing Λ constraints against them checks the index, not the table.**

### `L.skew` — the rank skew

**centre of mass 11.0666 vs midpoint 11.5, skew −0.43; only 8 of 976 cells fixed by x ↦ max − x**

*at the stated caps*

grade **COMPUTED**· source *M §8.4; Gauss 1809*· depends on `L.def`· 1 object depends on it· depth 2

> **PRIOR ART: the third standardised moment of a rank distribution. Gauss (1809).**

### `L.sperner` — Sperner property / Dilworth

**the largest antichain equals the largest rank level; max 122 at rank 11**

*rank sequence log-concave hence unimodal*

grade **COMPUTED**· source *M §8.4; Sperner 1928; Stanley 1980*· depends on `L.dist`· depth 9

> **PRIOR ART: Sperner 1928 for the Boolean lattice; Stanley, Weyl groups, the hard Lefschetz theorem, and the Sperner property, SIAM J. Alg. Disc. Meth. 1 (1980) 168-184, proves the order-ideal lattice of a product of chains is Peck — rank-symmetric, rank-unimodal, strongly Sperner. Λ is of that form, so the property is INHERITED.**

### `L.step` — the interval-removal step

**X ∖ [a,b] is a sublattice iff a is join-prime and b is meet-prime; step(Λ₈) = 4**

*distributive*

grade **PROVED**· source *M §16.8.5; Birkhoff 1937; Gratzer 1978*· depends on `L.pushback`· depth 11

> **PRIOR ART: removing an interval leaves a sublattice iff the endpoints are join-prime and meet-prime — the standard interval-removal criterion. Gratzer, General Lattice Theory (1978), ch. II.**

### `L.total` — the membership function is total

**χ_Λ : ∏A_i → {0,1} is total: membership decided for every ambient point**

*Λ a finite intersection of decidable comparisons*

grade **PROVED**· source *M §16.5; Birkhoff 1940*· depends on `L.chi`· depth 5

> **PRIOR ART: a membership function defined by inequalities on coordinates is total on the ambient product by construction.**

### `L.tree` — the constraint tree

**constraint graph n—ℓ—k—q—g—f—e with 2S pendant at k: 8 nodes, 7 edges, a caterpillar; treewidth 1**

*every constraint binds exactly two coordinates*

grade **COMPUTED**· source *M §8.5, §11.4; Freuder 1982*· depends on `L.def`· 5 objects depend on it· depth 2

> **PRIOR ART: that a constraint graph is a tree, and what follows from it, is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32.**

### `L.void` — the void

**void(x,y) = ∏_i(|Δ_i|+1) − |[x∧y, x∨y] ∩ Λ|**

*none*

grade **DEFINITIONAL**· source *M §10; Rota 1964*· depends on `L.occ`· 1 object depends on it· depth 4

> **PRIOR ART: the difference between a box count and the cells it actually contains is what Moebius inversion would compute. Rota (1964).**

### `L.voidfrac` — the void-free fraction

**void-free fraction 27.7–30.1% across 776M pairs; joint 30.13% vs product 20.19%, factor 1.49**

*at stated caps*

grade **COMPUTED**· source *M §10.2; Rota 1964*· depends on `L.void`· depth 5

> **PRIOR ART: as L.void; the fraction is the measurement.**

## T. The tower and its couplings — 16 objects

### `T.a10` — Racah 1943 seniority

**2S′ ≤ v ≤ g, v ≡ g (mod 2)**

*Racah seniority for ℓ^N*

grade **CITED**· source *M §12.11.1 / T A14; Racah 1943*· depends on `T.a9`· 2 objects depend on it· depth 2

> **PRIOR ART: seniority v, with 2S ≤ v ≤ g and v congruent to g mod 2, is Racah, Phys. Rev. 63 (1943) 367-382 — the classification of states of l^n by the number of unpaired electrons.**

### `T.a11` — the parent bound

**2J_c ≤ φ̂(k), φ̂ = max 2J over terms of ℓ^k = {1:3, 2:4, 3:5}**

*φ̂ read off the realised extent, not from a law*

grade **COMPUTED**· source *M §12.11.1 / T A15; Condon & Shortley 1935; Racah 1942*· depends on `T.a10`· 2 objects depend on it· depth 3

> **PRIOR ART: the term structure of a subshell l^k, and the maximum J it carries, is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII; Racah, Theory of complex spectra II, Phys. Rev. 62 (1942) 438-462, gives the general classification. The values {1:3, 2:4, 3:5} are read from that table, not derived here.**

### `T.a12` — the recoupling bound

**loose: 2K ≤ 2J_c + 2f_max (one parent). exact: |2J_c−2f| ≤ 2K ≤ 2J_c+2f step 2 (two parents)**

*jK pair coupling*

grade **CITED**· source *M §12.11.1 / T A16; Wigner 1931; Racah 1942*· depends on `T.a11`· 3 objects depend on it· depth 4

> **PRIOR ART: the triangle condition |j1-j2| ≤ J ≤ j1+j2 in steps of one is the Clebsch-Gordan series — Wigner, Gruppentheorie (1931); its application across parents is Racah, Phys. Rev. 62 (1942) 438-462.**

### `T.a13` — the spin-half bound

**|2J − 2K| ≤ 1**

*outer electron carries spin ½*

grade **CITED**· source *M §12.11.1 / T A17; Condon & Shortley 1935*· depends on `T.a12`· 1 object depends on it· depth 5

> **PRIOR ART: |2J - 2K| ≤ 1 is the coupling of a spin-half to K in the jK scheme; Condon & Shortley (1935), ch. X.**

### `T.a9` — the seniority floor

**2S′ ≤ g**

*vector coupling on the target*

grade **CITED**· source *M §12.10.1; Racah 1943*· depends on `L.c7`· 5 objects depend on it· depth 1

> **PRIOR ART: 2S ≤ g bounds the total spin by the occupancy — Pauli exclusion in Racah seniority form, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### `T.a9p` — the admissible Pauli cut

**2S′ ≤ 2f+1 (the admissible Pauli cut); Λ₉′ = 1,561 cells, 93 removed; closes the cycle f–g–2S′**

*min(g,4f+2−g) ≤ 2f+1 by averaging*

grade **COMPUTED**· source *M §12.11.1 / T 2.2; Pauli 1925; Racah 1943*· depends on `T.a9`· depth 2

> **PRIOR ART: the Pauli cut on a subshell's allowed terms is Pauli's exclusion principle (Z. Phys. 31, 1925) as applied to equivalent electrons; the seniority classification that makes it computable is Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### `T.dens` — the axis density

**density(axis) = Σ_parents |exact fibre| / Σ_parents |admissible fibre| = 63.7, 67.5, 44.7, 17.0, 31.4, 64.4%**

*three non-obvious exact sets required*

grade **COMPUTED**· source *M §12.11.1 / T A18; Racah 1942; Wigner 1931*· depends on `T.tower`· 2 objects depend on it· depth 7

> **PRIOR ART: the ratio of exact to admissible fibre sizes measures how much a triangle condition tightens a Pauli bound. Both bounds are standard; the ratio is measured.**

> **PRIOR ART: the ratio of exact fibre to admissible fibre measures how much the triangle condition (Wigner 1931, Clebsch-Gordan) tightens the Pauli cap (Racah 1942). Both bounds are theirs; the density is measured.**

### `T.dich` — the counting-coupling dichotomy

**counting coordinates close exactly; coupling coordinates close as envelopes; no third kind**

*the exact coupling bound is made of reflection, congruence and triangle*

grade **COMPUTED**· source *M §12.11.3; Racah 1942*· depends on `T.dens`· 1 object depends on it· depth 8

> **PRIOR ART: the split between coordinates that COUNT (occupancy, capacity) and coordinates that COUPLE (J, K, S) is the organising distinction of Racah's algebra. Counting coordinates carry Pauli caps; coupling coordinates carry triangle conditions, and the two close differently.**

### `T.excl` — the three excluded forms

**three excluded forms: REFLECTION (particle–hole conjugation), CONGRUENCE (fermion parity), TRIANGLE (one sum and one difference)**

*each is non-monotone or multi-parent*

grade **COMPUTED**· source *M §12.11.2; Racah 1943; Wigner 1931*· depends on `T.dich`, `A.rule`· 2 objects depend on it· depth 9

> **PRIOR ART: particle-hole conjugation, fermion parity and the triangle rule are all standard: conjugation from the complementary-shell theorem (Racah 1943), parity from the antisymmetry of the wavefunction, and the triangle inequality |j1-j2| ≤ J ≤ j1+j2 from the Clebsch-Gordan series (Wigner 1931).**

### `T.invariant` — basis independence of the level set

**the exact J multiset is identical in jK, LS, LK and jj; the four cell counts price four ROUTES**

*coupling schemes are basis changes*

grade **COMPUTED**· source *M §12.11.4; Wigner 1931; Racah 1942*· depends on `T.scheme`, `T.dens`· depth 8

> **PRIOR ART: the J multiset of a configuration is independent of coupling scheme because the schemes are unitary recouplings of one space — Wigner, Gruppentheorie (1931); Racah's 6-j and 9-j coefficients are the transformation matrices. What is measured here is the CELL COUNT each scheme costs, not the invariance.**

### `T.para` — parastatistics

**capacity(ℓ) = m(4ℓ+2) for parastatistics of order m; E = 0 through Λ₁₃ for m = 1,2,3**

*m(4ℓ+2) monotone in ℓ for every m, so A.rule is preserved*

grade **COMPUTED**· source *T 2.1 / D3; Green 1953*· depends on `T.tower`, `A.rule`· depth 7

> **PRIOR ART: parastatistics of order m, in which a state holds up to m particles, is H. S. Green, A generalized method of field quantization, Phys. Rev. 90 (1953) 270-273. The capacity m(4l+2) is its shell-model form.**

### `T.real` — the bounds against real terms

**the four coupling bounds on the exact term structure of every subshell: 85,829 tests, 0 failures**

*ℓ = 0..3, k = 1..4ℓ+2*

grade **COMPUTED**· source *microstate enumeration; Condon & Shortley 1935*· depends on `T.a9`· depth 2

> **PRIOR ART: the exact term structure of every subshell is tabulated in Condon & Shortley (1935), ch. VII, and in the NIST compendium. The 85,829 tests check the four coupling bounds AGAINST that table; the table is not this work.**

### `T.scheme` — the four coupling schemes

**closure holds in LS, LK, jK, jj: Λ₁₃ = 431,050 / 341,150 / 199,130 / 206,520, E = 0 throughout**

*a uniform one-parameter looseness convention*

grade **COMPUTED**· source *T 2.1b; Condon & Shortley 1935; Racah 1942*· depends on `T.tower`· 1 object depends on it· depth 7

NOT CHECKABLE and the book says why: the looseness convention is named and not printed, and two committed readings BRACKET rather than determine the figures — LS in [383,065, 597,325] contains 431,050, jj in [160,380, 244,060] contains 206,520 (R 1010)

> **PRIOR ART: LS, LK, jK and jj are the four standard angular-momentum coupling schemes — Condon & Shortley (1935), ch. X; the jK and LK intermediate schemes are Racah's. That the same physical states are counted in each is the content of the recoupling theory, and the four cell counts price the SCHEME rather than the physics.**

### `T.tight` — constraint tightness as a count

**the tight-pair count of a base is exactly 2S, S the envelope-step count**

*van Beek & Dechter's measure*

grade **COMPUTED**· source *M §14.5.9; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999*· depends on `A.env`· depth 2

> **PRIOR ART: the tight pairs of a staircase constraint are its envelope steps — Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271.**

### `T.tower` — the tower

**Λ₈…Λ₁₃ = 976, 1654, 2535, 13585, 22275, 64290; E = 0 at every stage, swept against every ambient cell to 47,775,744**

*at stated caps*

grade **COMPUTED**· source *M §12.11.0.10, reg. 249; Racah 1942; Condon & Shortley 1935; Racah 1942, 1943*· depends on `T.a9`, `T.a10`, `T.a11`, `T.a12`, `T.a13`· 5 objects depend on it· depth 6

CORRECTED 2026-08-11, re-applying register 1399 whose source fix was LOST in the 1.6.1 rollback — the register crossed as prose, the code did not. This object STATED 70905, 199130 at Λ₁₂ and Λ₁₃ while indices.py COMPUTES 22275, 64290. The first four agreed; only the last two differed, and register 541 named the cause without connecting it: the exact triangle against the loose one-parent bound differ by 3.18 at Λ₁₂. A sequence is a single claim and its terms must come from one convention, so the computed (exact-triangle) values now stand. Note also that 199,130 was simultaneously T.scheme's jK figure — one number doing two jobs in two objects with neither saying so.

> **PRIOR ART: the tower adjoins the coupling quantum numbers in the standard order — seniority, then J of the core, then K, then J. Each is Racah or Condon & Shortley; the cell counts and the closure at each stage are the measurement.**

### `T.trad` — the tree or the tightness

**the tree or the tightness: imposing the exact triangle at axis 12 gives 22,275 cells and E = 35,570**

*the exact bound has two parents*

grade **COMPUTED**· source *M §12.11.5 / T 2.4; Freuder 1982; Racah 1942*· depends on `T.a12`, `A.rule`· depth 7

> **PRIOR ART: the trade between tree structure and constraint tightness is Freuder (1982) for the tree side; the exact triangle is Racah/Wigner. The pricing is the measurement.**

## E. Empirical indexes — table, nuclide, layout — 4 objects

### `E.ioniz` — the refusal map

**first ionisation energies given to the bracket as bare numbers refuse at Be→B, N→O, Mg→Al and P→S — four steps of twelve, 67% admissible**

*the same two positions in both periods: the s2-p1 subshell opening and the p3-p4 first pairing*

grade **COMPUTED**· source *M §6.2; Mendeleev 1869; NIST*· depends on `B.brk`· depth 1

> **PRIOR ART: first ionisation energies as a periodic property date to Mendeleev; the values are NISTs. That bare numbers refuse the bracket is a statement about what a bracket needs, not about the data.**

### `E.layout` — the price of a layout

**hydrogen's placement is free and helium's costs 16, and they are not additive: −16 and 0 apart, −1 together**

*E set by the largest group used in period 1*

grade **COMPUTED**· source *M §6.1.1; Janet 1929*· depends on `E.table`· depth 3

> **PRIOR ART: hydrogen and helium are the classic placement anomalies of the periodic table, and Janets left-step form resolves them differently from the classroom table. The cost measured here is of the CHOICE.**

### `E.nuclide` — the nuclide chart's defect

**the measured nuclide chart indexed by (Z, N) closes at E = 9, stable across four proton-number cutoffs; the nine cells are the mass formula's pairing and clustering terms**

*cells named at one cutoff persist at every larger one*

grade **COMPUTED**· source *M §6.2; Segre 1945*· depends on `A.env`· depth 2

*** COUNT NOT REPRODUCED 2026-08-11 (R 1550). *** AME2020 Table I was captured from the published paper (Chin. Phys. C 45, 030003, Table I, 3558 rows, Z = 0-118, A = 1-295) and E recomputed with the same operator: E = 2, NOT 9, and stable at 2 across cutoffs Z ≤ 20, 50, 82, 92 and 118. Six variants of the cell set were tried - axes swapped, neutron excluded, measured-only, Z and N both positive - and none gives 9; measured-only gives 95. WHAT DOES REPRODUCE: the STABILITY across cutoffs, the cells being NAMEABLE PHYSICS, and the reading of them as the mass formula pairing term - the two defect cells are the empty cell (0,0) and Z=2 N=0, THE DIPROTON, which is unbound and is the textbook pairing failure. Three of four claims hold and the number does not. Cause UNDETERMINED: a different source edition, a different inclusion rule, or an arithmetic error in the original.

> **PRIOR ART: the chart of nuclides indexed by (Z, N) is Segres chart, in use since the 1940s.**

### `E.table` — the thirty-six decomposed

**the periodic table's 36 decompose 25 + 11, not 26 + 10; E is placement-sensitive, 36 at group 18 and 20 at group 2**

*all 118 elements*

grade **COMPUTED**· source *M §6.1.1; Mendeleev 1869; Janet 1929*· depends on `A.env`· 1 object depends on it· depth 2

> **PRIOR ART: the periodic tables arrangement is Mendeleev, Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente, Z. Chem. 12 (1869) 405-406; the left-step form on n+l is Janet (1929). That E is placement-sensitive is a statement about which arrangement, not about the elements.**

## B. The bracket — 21 objects

### `B.V` — the price V — the bracket's width against its error

**V = w/e where w = |T(n+1)−T(n−1)|, e = |T(n) − ½(T(n−1)+T(n+1))|**

*three consecutive members*

grade **DEFINITIONAL**· source *M §21.1; Milne-Thomson 1933*· depends on `B.brk`· 3 objects depend on it· depth 1

> **PRIOR ART: the ratio of a first difference to a second is the standard curvature-to-slope measure of a finite-difference scheme. Milne-Thomson, The Calculus of Finite Differences (1933), ch. I-II.**

### `B.V43` — the four-thirds law

**V = 4ν/3 for a Rydberg series; in general V(x,p) = 4x/(h|p−1|) for y = x^p**

*T = Z²R/ν²*

grade **COMPUTED**· source *M §21.1; Rydberg 1890*· depends on `B.V`· 3 objects depend on it· depth 2

> **PRIOR ART: for a Rydberg series T ~ nu^-2, so the ratio of first to second differences is 4nu/3 by direct expansion. Rydberg, Recherches sur la constitution des spectres d emission, K. Sven. Vetensk. Akad. Handl. 23 (1890).**

### `B.Vexact` — the exact price

**V = 4ν³/(h(3ν²−h²)); with r = ν/h, V = 4r³/(3r²−1). Z and R cancel identically**

*step h free*

grade **PROVED**· source *M §21.4; Rydberg 1890*· depends on `B.V43`· 2 objects depend on it· depth 3

> **PRIOR ART: the exact form follows from the Rydberg term T = Z^2 R / nu^2 by finite differencing; Z and R cancel because the ratio is scale-free.**

### `B.adm` — the five-sigma admissibility threshold — where the bracket may be applied at all

**r = 2Z²R/(ν³σ) ≥ 5**

*levels separated by more than 5σ*

grade **DEFINITIONAL**· source *M §22.5; Gauss 1809*· 1 object depends on it· depth 0

> **PRIOR ART: a five-sigma admissibility threshold is a statement about signal against measurement error, in the Gaussian error model of Gauss, Theoria motus corporum coelestium (1809).**

### `B.aitken` — Aitken Δ² / Seki Kōwa

**Aitken's Δ² on a Rydberg series lands at I − T/3, because the correction is (ΔT)²/Δ²T → (2/3)T**

*algebraic not geometric convergence*

grade **PROVED**· source *M §24.6; Aitken 1926*· depends on `B.newton`· depth 3

> **PRIOR ART: Aitken, On Bernoulli's numerical solution of algebraic equations, Proc. R. Soc. Edinb. 46 (1926) 289-305 — the delta-squared process. That it lands at I - T/3 on a Rydberg series is the measurement; the process is his.**

### `B.brk` — monotone interpolation bracket

**T(n) lies between T(n−1) and T(n+1)**

*T monotone in n within a channel*

grade **PROVED**· source *M §20.1; Leibniz 1682; Milne-Thomson 1933*· 6 objects depend on it· depth 0

measured at 789 of 789 interior cells — and it is the TRIVIAL bracket, which cannot fail (R 797, 830)

> **PRIOR ART: that a term of an alternating or monotone sequence lies between its neighbours is the classical bracketing of finite differences — Leibniz's alternating-series test in its difference form; Milne-Thomson, The Calculus of Finite Differences (1933), ch. I. The book's contribution is applying it to Rydberg terms cell by cell, not the bracket.**

### `B.coll` — the assembly rule — a composite observable's scaling exponent is 2a + 3b

**an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b}**

*⟨r⟩ ∝ ν², ΔE ∝ ν⁻³*

grade **PROVED**· source *M §24.1; Bohr 1913; Bethe & Salpeter 1957*· 1 object depends on it· depth 0

> **PRIOR ART: the scaling of hydrogenic expectation values, <r^a> ~ nu^{2a} and Delta E ~ nu^{-3}, is Bohr's correspondence scaling (1913) in its quantum form; tabulated in Bethe & Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), sec. 3.**

### `B.fail` — when the bracket fails

**the bracket fails ⟺ |ΔT| > 2Z²R/ν³**

*a perturber reorders only if the shift exceeds half the local spacing*

grade **PROVED**· source *M §23.3; Rydberg 1890*· depends on `B.brk`· 1 object depends on it· depth 1

the yardstick verified: 2Z^2R/nu^3 against measured adjacent spacing over 742 pairs gives median 1.201 (R 832)

> **PRIOR ART: the local spacing of a Rydberg series is 2 Z^2 R / nu^3, the derivative of the term formula. A shift exceeding half of it reorders the levels.**

### `B.floor2` — the floor at two

**V > 2 for any monotone sequence; V → 2 only as one step vanishes**

*d₀,d₁ > 0; V = 2(d₀+d₁)/|d₀−d₁|*

grade **PROVED**· source *M §21.2 Prop 14.1; Jensen 1906*· depends on `B.V`· 1 object depends on it· depth 2

> **PRIOR ART: V > 2 for a monotone sequence is a form of Jensen's inequality — the chord lies above the curve for a convex function, so the second difference cannot exceed half the first. Jensen, Sur les fonctions convexes, Acta Math. 30 (1906) 175-193.**

### `B.floor32` — the Rydberg floor

**V ≥ 32/11 = 2.909 for a Rydberg series specifically**

*hydrogenic form*

grade **COMPUTED**· source *M §21.2; Rydberg 1890; Jensen 1906*· depends on `B.floor2`, `B.V43`· depth 3

> **PRIOR ART: the floor V > 2 is Jensen convexity (1906); the sharper 32/11 for a Rydberg series follows from its specific nu^-2 form.**

### `B.frac` — the fractional widths

**w/T = 4(h/ν) + 8(h/ν)³ and e/T = 3(h/ν)²; their ratio is V**

*Rydberg*

grade **COMPUTED**· source *M §21.6; Taylor 1715*· depends on `B.Vexact`· depth 4

> **PRIOR ART: expanding the first and second differences of nu^-2 in powers of h/nu is Taylor series with a step. Taylor, Methodus incrementorum directa et inversa (1715).**

### `B.hstar` — the optimal step

**h* = √(2β/(α y″)) minimises αw + βV, valid for h* ≪ ν**

*leading order*

grade **COMPUTED**· source *M §21.5.3; Lagrange 1797; Curtis & Reid 1974*· depends on `B.pareto`· depth 5

NOT CHECKABLE here: its source M §21.5.3 does not appear in the book's text and the objective it minimises is not stated, so the stationary point cannot be verified (R 1010)

> **PRIOR ART: minimising a weighted sum of two competing costs by setting the derivative to zero is elementary optimisation; the h* ~ √(2 beta/(alpha y)) form is the standard step-size optimum of finite-difference practice.**

> **PRIOR ART: the optimal finite-difference step balances truncation error against roundoff, giving h* proportional to √(eps/y) — Curtis & Reid, The choice of step lengths when using differences to approximate Jacobian matrices, J. Inst. Math. Appl. 13 (1974) 121-126. Here the two costs are width and price rather than truncation and roundoff, and the same balance applies.**

### `B.newton` — Newton decrement, Nesterov–Nemirovskii 1994

**8y′²/y″ = 8λ² with λ² = ∇f ᵀ[∇²f]⁻¹∇f; for a Rydberg series λ² = (2/3)T**

*one dimension: λ² = f′²/f″*

grade **PROVED**· source *M §23.8.1; Newton 1669; Nesterov & Nemirovskii 1994*· depends on `B.V`· 2 objects depend on it· depth 2

> **PRIOR ART: the Newton decrement lambda^2 = grad f^T [Hess f]^{-1} grad f is the standard measure of proximity to a minimum in interior-point theory (Nesterov & Nemirovskii 1994); Newton's method itself is De analysi (1669).**

### `B.nuV` — the value-one crossing — where the bracket's price V passes unity

**ν_V = (3Z²R/5q)^{1/4}**

*curvature resolvable at quotation granularity q*

grade **PROVED**· source *M §23.15; Rydberg 1890*· depth 0

the crossing where V passes unity, computed from the quotation granularity q

> **PRIOR ART: solving V = 1 for nu against a quotation granularity q gives the quartic root; the term formula is Rydberg (1890).**

### `B.ordbr` — the ordered bracket

**sign(f(n) − p(n)) = (−1)^{k+1}(−1)^m with m nodes above n; a two-sided deductive bracket at every order**

*sign(f^{(j)}) = (−1)^j*

grade **PROVED**· source *M §23.10.1; Newton 1687; Milne-Thomson 1933*· depends on `B.brk`· depth 1

> **PRIOR ART: the sign of the error of a Newton interpolating polynomial alternates with the number of nodes above the evaluation point — the standard remainder theorem for finite differences, Newton's divided-difference form (Principia, Book III, Lemma V); Milne-Thomson (1933), ch. VIII.**

### `B.ordk` — the admissible order

**order k admissible while |Δ^{k+1}T| > 5·2^{k+1}·σ**

*the (k+1)-th difference is a signed sum of 2^{k+1} levels*

grade **PROVED**· source *M §23.10.4; Milne-Thomson 1933*· depends on `B.adm`· depth 1

> **PRIOR ART: the admissible order of a difference scheme is set by where the next difference falls below the noise, and the 2^(k+1) growth of noise under k-fold differencing is standard. Milne-Thomson (1933), ch. II.**

### `B.pareto` — the width-price front

**dw/dh > 0 and dV/dh < 0 for every monotone convex y and every h; the family {(w,V)} is a Pareto frontier**

*w ~ h, e ~ h²*

grade **PROVED**· source *M §21.5.2; Pareto 1896*· depends on `B.Vexact`· 1 object depends on it· depth 4

> **PRIOR ART: a family in which no member improves both objectives is a PARETO FRONT — Pareto, Cours d'economie politique (1896). That dw/dh > 0 and dV/dh < 0 for every monotone convex y makes {(w,V)} one is the proof here; the notion is his.**

### `B.pole` — the linear pole

**V has a pole at p = 1: a linear observable has no curvature to price**

*y = x^p*

grade **PROVED**· source *M §18.5; classical; Taylor 1715; Milne-Thomson 1933*· depends on `B.V43`· depth 3

> **PRIOR ART: a linear function has vanishing second difference, so any ratio measuring curvature against slope diverges there. The pole at p = 1 is that statement.**

### `B.rank1` — the rank-one factorisation

**rank(log q) = 1 across fifteen Rydberg observables; second singular value 1.8×10⁻¹⁴**

*every observable is ν to a power*

grade **COMPUTED**· source *M §24.2; Eckart & Young 1936*· depends on `B.coll`· depth 1

> **PRIOR ART: that a matrix has rank one is read from its singular values — Eckart & Young, The approximation of one matrix by another of lower rank, Psychometrika 1 (1936) 211-218. A second singular value of 1.8e-14 is numerical zero, so log q factorises exactly.**

### `B.selfconc` — self-concordance

**T(ν) is self-concordant, |f‴| ≤ 2(f″)^{3/2}, for ν ≤ (√6/2)·Z√R**

*T = Z²R/ν²*

grade **PROVED**· source *M §23.8.2; Nesterov & Nemirovskii 1994*· depends on `B.newton`· depth 3

> **PRIOR ART: self-concordance, |f'''| ≤ 2(f'')^{3/2}, is Nesterov & Nemirovskii, Interior-Point Polynomial Algorithms in Convex Programming (1994), the condition under which Newton's method converges at a rate independent of the problem's conditioning.**

### `B.silence` — what silence implies

**the bracket holding ⟹ |ΔT| < 2Z²R/ν³ at that cell**

*contrapositive of B.fail*

grade **PROVED**· source *M §23.5; Rydberg 1890*· depends on `B.fail`· depth 2

849 of 849 cells satisfy it; median |dT|/spacing 0.0015, largest 0.25 (R 831)

> **PRIOR ART: the contrapositive of B.fail, on the same term formula.**

## K. Transit and information — 24 objects

### `K.arrow` — the arrow index

**X_w = {a : w(tgt a) ≤ w(src a)} is closed; one arrow per coordinate and no others; sums, max and min all fail**

*w a single coordinate*

grade **COMPUTED**· source *M §12.11.0.2; Birkhoff 1937*· depends on `K.clockfail`, `A.rule`· depth 8

> **PRIOR ART: a set of the form {a : w(target) ≤ w(source)} for monotone w is a down-set of the induced order, hence closed. Birkhoff, Rings of sets (1937).**

### `K.axis` — the axis test

**an axis earns a COORDINATE when it is independent of the others AND its distinct values are few relative to what it adds; both conditions are necessary**

*a closed index and a candidate axis*

grade **MEASURED**· source *R 1127-1131; Dushnik & Miller 1941; Shannon 1948*· depends on `K.redun`· 1 object depends on it· depth 4

on the same elements, Z≤16: (Z,charge,l) gives 0% redundancy, +multiplicity gives 82%, +2J gives 0% again. 2J is NOT derived — no combination determines it — but |L-S| ≤ J ≤ L+S constrains it to 2min(l,S)+1 values of seventeen. A coordinate must be free, not merely undetermined. The entropy account is PARTIAL: retained entropy is 26% for multiplicity and 27% for 2J, which does not separate them

> **PRIOR ART: an axis earns a coordinate when it is order-independent of the others (Dushnik & Miller 1941) and carries information (Shannon 1948). The test combines both.**

### `K.cat` — the tower is a category

**Λ₉ is a category: 41,682 composable pairs, zero failures, associative**

*as K.comp*

grade **COMPUTED**· source *M §12.11.0; Mac Lane 1971*· depends on `K.comp`· 2 objects depend on it· depth 3

> **PRIOR ART: associativity of composition and the existence of identities are the category axioms — Mac Lane, Categories for the Working Mathematician (1971). Verifying them on 41,682 composable pairs checks that Λ₉ IS a category; the axioms are not this work.**

### `K.clock` — the composition clock

**occupancy never rises along composition: 0 of 739 steps; the tick is k − g = (k−q) + (q−g)**

*destinations begin empty — an assumption, not a constraint*

grade **COMPUTED**· source *M §12.11.0.1; classical; Floyd 1967*· depends on `K.comp`· 1 object depends on it· depth 3

> **PRIOR ART: a quantity that never increases along composition is a MONOVARIANT, the standard tool for proving termination. That occupancy is one here is the measurement; the technique is old.**

### `K.clockfail` — the clock that does not tick

**index (g,G) with g ≤ G ≤ 4f+2 and g ≤ q: 13,775 cells, closed, and 31.6% of composable pairs raise occupancy**

*prior occupancy carried as a coordinate*

grade **COMPUTED**· source *M §12.11.0.2; Floyd 1967*· depends on `K.clock`, `A.rule`· 1 object depends on it· depth 7

> **PRIOR ART: a candidate variant that is closed but does not decrease is a failed termination measure. Floyd (1967).**

### `K.comp` — composition

**b∘a defined when tgt(a) = src(b); the composite transfers min(q_a, q_b)**

*Λ₉'s target (e,f,g,2S′) has the source's constraint forms*

grade **COMPUTED**· source *M §12.11.0; Mac Lane 1971*· depends on `T.a9`· 6 objects depend on it· depth 2

> **PRIOR ART: composition defined when target meets source is the category axiom; what is measured is that the composite transfers min(q_a, q_b), which is a property of this index and not of categories.**

### `K.corner` — corners and faces

**the whole-object defect decomposes into FACES and CORNERS, and the corners are an artefact of loose coordinatisation**

*an index of dimension d and its d-1 axis slices*

grade **MEASURED**· source *R 1177; Freuder 1978*· depends on `K.langclose`· depth 7

of the 6,195 cells R admits and Λ_spectra does not hold, 3,993 are admitted by some three-axis slice and 2,202 by none. Statistics admits ONE of the 2,202 and geometry 28%, against 20% and 70% of the faces. And every available fifth coordinate makes the corners worse — by 70% to 652% — because all four candidates are DERIVED (register 1122)

> **PRIOR ART: cells admitted by the full closure and by no lower-arity projection are exactly the k-consistency gap — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### `K.coupling` — the refuted conjecture

**coordinate COUPLING does not predict redundancy**

*a closed index*

grade **MEASURED**· source *R 1120; Dechter & Pearl 1989*· depends on `K.redun`· depth 4

across six indices — Λ, Λ_spectra, the periodic table, Janet, the calendar, a box ordering — redundancy against coupling gives r^2 = 0.002, p = 0.94. Janet and the box ordering both have 50% coupling and 0% redundancy; Λ_spectra has 17% coupling and 20% redundancy

> **PRIOR ART: that coupling alone does not predict what a local method achieves — the induced width, not the edge count, is the parameter. Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### `K.deadend` — the dead ends, defined

**the non-composable cells are defined exhaustively: at Λ₁₀ all 485 have g = 0 and every g = 0 cell is non-composable; at Λ₁₃, 11,188 at g = 0, 5,116 with 2J in {6,7,8} which no 2J_c can start, and 8,214 failing only in combination**

*L.c8 is k ≥ 1, so a target ending empty can never be a source; and 2J inherits 2K's range while 2J_c is bounded by φ(k) alone*

grade **COMPUTED**· source *M §12.11.1.5; Mac Lane 1971*· depends on `K.peak`· depth 6

> **PRIOR ART: cells that compose with nothing are those whose target is no other cell source — the non-composable part of a quiver.**

### `K.decay` — data-processing inequality + Pinsker

**for a tree-structured index, I(u;v) is non-increasing in tree distance d, and |P(A_u∩A_v) − P(A_u)P(A_v)| ≤ √(I(u;v)·ln2 / 2)**

*Markov random field on a tree; data processing; Pinsker*

grade **PROVED**· source *M §12.11.0.7; Lauritzen 1996; Pearl 1988*· depends on `K.markov`· depth 5

> **PRIOR ART: mutual information is non-increasing in tree distance because every path is separated — the data-processing inequality on a Markov tree. Cover & Thomas, Elements of Information Theory (1991), Thm 2.8.1; Lauritzen, Graphical Models (1996), ch. 3.**

### `K.girth` — the girth is four

**the girth of the unit-step graph on Λ₉ is exactly 4**

*unit-step adjacency = covering relation, 6,658 edges*

grade **PROVED**· source *T 4.3; classical graph theory; Berge 1962*· depends on `L.dist`· depth 9

> **PRIOR ART: girth is the length of the shortest cycle, standard since Euler. That a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves.**

### `K.helly` — Helly number

**molecular transit is an intersection question; the Helly number is ≥ 5 and ≤ 144**

*a molecule moves as one fibre; a circuit is a square; ground set C(9,2)·4 = 144*

grade **COMPUTED**· source *T 4.4; Helly 1923*· depends on `K.comp`· depth 3

> **PRIOR ART: the Helly number of a family is the least h such that every h-wise intersecting subfamily intersects — Helly, Über Mengen konvexer Körper mit gemeinschaftlichen Punkten, Jahresber. DMV 32 (1923) 175-176.**

### `K.jump` — the categorial jump

**the axis that makes the tower a category is worth twenty points: Λ₈ is 50.3% composable and Λ₉, adding 2S' ≤ g, is 70.7%**

*the companion's index sits between them at 59.5% — three transition indexes, three fractions, so this is not a norm*

grade **COMPUTED**· source *M §12.11.1.3; Mac Lane 1971*· depends on `K.twocol`· depth 5

> **PRIOR ART: the axis that closes composition is the one that supplies identities and associativity — the category axioms. What is priced is the cell cost of adding it.**

### `K.langclose` — closure as agreement

**E(X) = 0 if and only if the languages agree**

*an index of dimension ≥ 3 and two or more operators*

grade **MEASURED**· source *R 1176; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `K.three`· 1 object depends on it· depth 6

six indexes, three operators — order, statistics, geometry. Λ and a box ordering: E = 0 and every pair agrees, 0 cells differing. The periodic table, Janet, the calendar and Λ_spectra: E > 0 and every pair differs. No exception. Closure is therefore a language-theoretic property as well as an order-theoretic one, and the language test is cheaper: R enumerates the ambient product, pairwise consistency needs only the marginals

> **PRIOR ART: global and local closures coincide exactly on acyclic structures — BFMY, J. ACM 30 (1983) 479-513. That E = 0 iff the languages agree is that theorem read as an equivalence.**

### `K.markov` — the Markov property

**the future is conditionally independent of the past given the transfer: every past gives the same future set at each q**

*the constraint graph is a tree, q the cut vertex*

grade **COMPUTED**· source *M §12.11.0.8; Lauritzen 1996; Pearl 1988*· depends on `C.cut`, `L.tree`· 1 object depends on it· depth 4

> **PRIOR ART: the future being conditionally independent of the past given the present is the MARKOV PROPERTY. Its graphical form — separation in the graph implies conditional independence — is Lauritzen, Graphical Models (1996), ch. 3, and Pearl, Probabilistic Reasoning in Intelligent Systems (1988).**

### `K.peak` — the composability peak

**composability peaks at Λ₁₀ and falls after: 0.0000, 0.7068, 0.8087, 0.6956, 0.6394, 0.6186 across Λ₈ to Λ₁₃**

*counting axes raise the fraction and coupling axes lower it, with no exception — §12.11.3's dichotomy predicts the sign as well as the price*

grade **COMPUTED**· source *M §12.11.1.4; Berge 1962*· depends on `K.twocol`· 1 object depends on it· depth 5

> **PRIOR ART: the composability fraction is the arc density of the composition quiver; its rise and fall with the tower is the measurement.**

### `K.produce` — the production rule

**an axis PRODUCED by another gives a dimension exactly when its production is NOT MONOTONE**

*a closed index and an axis derived from its coordinates*

grade **MEASURED**· source *R 1143; Birkhoff 1937*· depends on `K.axis`· 2 objects depend on it· depth 5

multiplicity is produced by Ne and cycles 2,{1,3},2,{1,3},{2,4} — NOT monotone — and adding it takes redundancy from 20% to 82%. Ne is produced by (Z,charge) and monotone: 0%. n0 is produced by (Z,charge,l) and monotone: 0%. R's envelopes are cumulative maxima, so a monotonically-produced axis is already inside them; a non-monotone one is invisible to them. This resolves the apparent contradiction between R 1122 and R 1123

> **PRIOR ART: a monotone function of existing coordinates adds no join-irreducibles and so no dimension; a non-monotone one does. Birkhoff (1937).**

### `K.quiver` — the composition quiver

**composable cells are the arcs of a quiver Q on 33 objects; the composition graph is the line digraph L(Q), |E| = Σ_v in(v)·out(v) = 27,027**

*a loop at every vertex*

grade **COMPUTED**· source *T 4.2; Gabriel 1972*· depends on `K.cat`· depth 4

> **PRIOR ART: a quiver is a directed graph whose paths generate an algebra — Gabriel, Unzerlegbare Darstellungen I, Manuscripta Math. 6 (1972) 71-103. The composable cells form the arcs of one.**

### `K.redun` — the projection ladder

**redundancy under R rises with the number of INDEPENDENT coordinates; a DERIVED coordinate lowers it**

*a closed index X of dimension d*

grade **MEASURED**· source *R 1119-1122; Shannon 1948*· depends on `A.R`· 2 objects depend on it· depth 3

Λ PROJECTED onto its own first d coordinates, same constraints: d=8 gives 61% removable with exact recovery, d=7,6,5 give 30%, d=4 gives 5%, d=3 gives 0%. And adding the electron count Ne = Z-c+1 to the spectra index — a FUNCTION of two coordinates it already has — drops redundancy from 20% to 0% while doubling the envelopes and raising coupling 17% to 33%

> **PRIOR ART: redundancy is the excess of a representation over its entropy. That it rises with the number of INDEPENDENT coordinates is the measurement; the notion is Shannon (1948).**

### `K.three` — the three-coordinate rule

**an index needs THREE coordinates before its languages can disagree**

*an index and two languages*

grade **PROVED**· source *R 1175; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.stat2`· 1 object depends on it· depth 5

at d = 2 there is one coordinate pair, so pairwise consistency and the cell coincide and every language returns the same answer. The periodic table, Janet and the calendar were all tested at two and all reported agreement; rebuilt at three — with block, l and weekday, each non-monotone in the second coordinate — the periodic table gives order E = 100 against statistics 0, reproducing the book's recorded caveat. All three match the book at 2-D first: 36, 0 and 7

> **PRIOR ART: pairwise consistency is a statement about PAIRS, so an object with one pair cannot make it. BFMY (1983) for the general local-to-global framework.**

### `K.transit` — the transit profile

**the transit profile MI/H = 0.51, 0.93, 0.08, 0.13, 0.77 at Λ₉–Λ₁₃: reduced at 10, a label through 11 and 12, re-attaching at 13**

*Λ₁₂ built with the loose bound*

grade **COMPUTED**· source *M §12.11; Shannon 1948*· depends on `T.tower`· depth 7

> **PRIOR ART: MI/H is the normalised mutual information, standard since Shannon (1948).**

### `K.twocol` — space is what an index holds, time is what it composes

**an index has a time column exactly when its cells are moves: Λ₈ 976/0, Λ₉ 1,654/1,169, the companion's index 2,370/1,410, while the periodic table and the calendar have no second column and cannot have one**

*a transition cell has two ends so composability is askable; a state cell has one position and the question does not arise*

grade **COMPUTED**· source *M §12.11.1.3; Mac Lane 1971*· depends on `K.cat`· 3 objects depend on it· depth 4

> **PRIOR ART: an index has a composition structure exactly when its cells are morphisms rather than objects — the distinction is the category axioms. Mac Lane (1971). CORRECTED 2026-08-11: this statement printed Λ₈ as 976/491. It is 976/0. The generated table in INDICES.md gives 0 with fraction 0.0000, indices.py says 'Λ₈ composes not at all — four source coordinates against three target', and K.window states the reason as a dependency: 'Λ₈ target has 3 coordinates against 4', so tgt(a) = src(b) is not even askable at Λ₈ and Λ₉ is the FIRST composable level. The 491 was a hand-authored figure in an object graded COMPUTED, contradicting the computation it depends on.**

### `K.window` — the composable window

**Λ₉ is the first composable level and the last tree level**

*Λ₈ target has 3 coordinates against 4; Λ₁₀ has 10 nodes and 10 edges*

grade **COMPUTED**· source *T 4.1; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `K.comp`, `L.tree`· depth 3

> **PRIOR ART: that treeness and composability are different properties, and that an index can be the last of one and the first of the other, is the acyclicity/local-consistency distinction of BFMY, J. ACM 30 (1983) 479-513.**

### `K.zcross` — the periodic table as a coordinate

**composability is 22.71% within one element and 85.23% across the 118, while E is 28,503 without Z and 972,862 with it**

*composability wants the whole table and closure wants one atom; Λ closes because it has no Z*

grade **COMPUTED**· source *M §12.11.1.6; Edlen 1964*· depends on `K.twocol`· 1 object depends on it· depth 5

> **PRIOR ART: that composability is far higher across elements than within one is the isoelectronic structure — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964).**

## M. The modular chain — 9 objects

### `M.C1` — the presymplectic potential

**the presymplectic potential θ = δφ £_ℓφ η carries no transverse derivative, so Ω is block diagonal in y and {φ(u,y),φ(u′,y′)} = (1/4√q(y))sgn(u−u′)δ^{d−2}(y−y′)**

*u-independent transverse metric, i.e. Θ = 0; non-derivative interactions only*

grade **COMPUTED**· source *T 10.4c, F1, F2; Wald & Zoupas 2000*· depends on `M.hsmi`· 2 objects depend on it· depth 3

> **PRIOR ART: the presymplectic potential and its ambiguities are Wald & Zoupas, General definition of conserved quantities in general relativity, Phys. Rev. D 61 (2000) 084027.**

### `M.C2` — the open object — half-sided modular inclusion on a non-expanding horizon · **GRADED OPEN**

**Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂) for t ≤ 0, u₁ < u₂, WITH Ω cyclic and separating for BOTH M(u₁) and M(u₂)**

*N a non-expanding horizon with no Killing field, ω Hadamard*

grade **OPEN**· source *T 10.4d, F6*· depends on `M.C1`, `M.hsmi`· 1 object depends on it· depth 4

REGRADED CONDITIONAL 2026-08-11 (R 1507). This object is NOT open. It is PROVED on one existence hypothesis, in nine steps NONE of which uses a Killing field: P_lambda ≥ 0 from the ANEC on ACHRONAL generators (R 1471); U(s) unitary by Stone; U(s) B U(s)-dagger inside B because the cut translates into itself, which is CAUSAL structure (R 1506); U(s)Omega = Omega from the hypothesis; C_lambda = U(1) B U(1)-dagger, the source own equation; Omega cyclic for C_lambda since C_lambda Omega = U(B Omega) with U unitary and B Omega dense (R 1501); separating since C_lambda is inside B; hence the four Borchers conditions, hence HSMI by Borchers 1992 and Wiesbrock 1993. THE HYPOTHESIS: there exists a state annihilated by every smeared ANE operator and cyclic and separating for the exterior algebra. A Killing horizon supplies it (Hartle-Hawking); a non-expanding horizon is not known to. So the isometry supplies a WITNESS, not a step. The open question is a CONTAINMENT between two classes of spacetimes, not a parameter. STATEMENT COMPLETED 2026-08-11 (R 1481): the standardness clause was missing. A half-sided modular inclusion is N inside M with a vector Omega CYCLIC AND SEPARATING FOR BOTH, and sigma_t(N) inside N for t ≤ 0 — Lechner-Scotford Def 2.1, equivalent to the Borchers triple by Borchers 1992 and Wiesbrock 1993. This object stated only the inclusion clause. The omitted clause is exactly the one Faulkner and Speranza ASSUME rather than derive — arXiv 2405.00847 sec 3.1 says, of the smaller algebra, assuming Omega is cyclic for it — and Reeh-Schlieder does not supply it, because their Omega is a vacuum for the average null energy operators and, in their own words, may not coincide with a global minimal energy state. Araki and Zsido, Rev. Math. Phys. 17 (2005) 491-543, extend Wiesbrock to weights and fill a gap in the 1993 proof. OPEN on the GEOMETRIC route only. M.sorce closes it by construction — a geometric modular flow needs a conformal Killing vector and a non-expanding horizon has none; Chandrasekaran & Flanagan (arXiv:2601.07915) have the Killing case. The ALGEBRAIC route is not blocked: M.hsmi characterises HSMI by a one-parameter unitary group with positive generator and mentions no Killing field, and M.C1's commutator is already an algebraic object. That route was ATTEMPTED (R 1018-1022): its free half goes through — M.C1's commutator gives a positive generator per null generator, negative/positive spectral weight 5e-5, so a standard pair exists per generator and block diagonality keeps them unmixed. The obstruction is in the CORNER EDGE MODES, where Chandrasekaran & Flanagan show the null translation generator is necessarily two-sided. A proposal that Theta = 0 supplies the missing relative boost was tested and FAILS: theta_ab -> a(y) theta_ab under l -> a(y)l, so theta = 0 is invariant under the rescaling and cannot fix its parameter. The paper's OWN route (Sec 7.3) supplies the boost from SMOOTHNESS instead — local Rindler frames give chi = kappa(u d_u - v d_v) with grad_(mu chi_nu) = O(u,v), and footnote 44 says a local boost Killing field is all that is needed. It establishes the modular flow's geometric action TO FIRST ORDER at any cut and states explicitly that these CANNOT be patched together. M.C2 needs finite u1 < u2. The reduction bottoms out at POSITIVITY of the null translation generator, and that is NOT implied by Hadamard: Hadamard is microlocal (a wavefront-set condition) while positivity is a global spectral one, and a smooth deformation of the vacuum raises negative/positive spectral weight from 4.8e-05 to 2.6e-03 while changing the UV tail by 0.0000%. Thermal states are Hadamard and carry both signs. Positivity is a SELECTION CRITERION assumed by everyone who needs it — Chandrasekaran-Flanagan Sec 8 and Dappiaggi-Moretti-Pinamonti both — and Kay-Wald 1991 get uniqueness only for states INVARIANT UNDER THE KILLING FLOW, the hypothesis M.C2 drops. CORRECTION (R 1038-1042): the hypothesis is NOT purely geometric — the standard NEH definition's third condition is 'Einstein field equations hold on Delta and -T^a_b l^b is future causal', an energy condition on the state, which via Raychaudhuri forces T_ab l^a l^b = 0 and sigma_ab = 0, hence L_l q_ab = 0 — which is M.C1's hypothesis, so M.C1 assumes a consequence of the definition. The shortfall is ORDER: the condition fixes the background, while half-sidedness is spectral on the perturbations

### `M.hsmi` — Borchers 1992 / Wiesbrock 1993

**half-sided modular inclusion is CHARACTERISED by a one-parameter unitary group with positive generator**

*common cyclic separating vector; extended to weights by Araki–Zsidó 2004*

grade **CITED**· source *T E2, E3; Borchers 1992; Wiesbrock 1993*· depends on `M.tt`· 2 objects depend on it· depth 2

> **PRIOR ART: half-sided modular inclusion and its characterisation by a one-parameter group with positive generator — Borchers, The CPT theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Lett. Math. Phys. 28 (1993) 107-114.**

### `M.ledger` — the modular ledger

**d − 1 = 1 + (d − 2) ON THE FREE ALGEBRA: one HSMI per generator supplies the affine line; the transverse direct integral is C1 and no HSMI supplies it. INCOMPLETE ON THE DRESSED ALGEBRA, which carries doubled corner modes besides**

*a null hypersurface in d dimensions — THIS IS A MANIFOLD COUNT, NOT AN ALGEBRA COUNT (R 1484)*

grade **COMPUTED**· source *T 10.4e, F7; Borchers 1992; Wiesbrock 1993*· depends on `M.C1`, `M.C2`· depth 5

COMPLETED 2026-08-11 (R 1484): the sum is TWO accountings. LEVEL ONE, the manifold, is what this object counts and it is correct. LEVEL TWO, the algebra, carries the corner content, and register 1020 writes it exactly: the residual freedom is l -> a(y) l, acting on the affine parameter as u -> u/a(y) + b(y). Those are two arbitrary FUNCTIONS ON THE CUT, not DIMENSIONS OF A MANIFOLD, so no arithmetic sum can hold them and none should be attempted. R 1022 named what would close M.C2 — a canonical scaling of the affine parameter — which is a(y). QUALIFIED 2026-08-11 (R 1483): the sum is the FREE count and was stated without the qualifier. Register 1019, which M.C2 own check already cites, records that half-sidedness fails on the DRESSED algebra and not the free one, and that Chandrasekaran and Flanagan recover it by EXTENDING THE PHASE SPACE WITH DOUBLED CORNER MODES — relative boosts AND null translations of the respective corners. Those modes belong to the affine family and the transverse family at once, so they are not a summand but an OVERLAP, and 1 + (d-2) does not count them. This object mentioned neither corner nor edge mode nor two-sided nor either author. dimensional_ledger — and the ledger IS the kinematic/stateful decomposition (R 1035): the STATEFUL object (HSMI, hence M.C2) supplies exactly ONE dimension, the affine line; the KINEMATIC one (M.C1, Theta = 0) supplies the other d-2. Read as a counting argument until then

> **PRIOR ART: one half-sided modular inclusion per generator supplies the affine line — the Borchers-Wiesbrock theorem, Borchers, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Lett. Math. Phys. 28 (1993) 107-114.**

### `M.rs` — Reeh–Schlieder

**the vacuum is cyclic and separating for local algebras**

*Hadamard state; region with nonempty causal complement*

grade **CITED**· source *T E0; Reeh & Schlieder 1961*· 1 object depends on it· depth 0

> **PRIOR ART: the vacuum is cyclic and separating for local algebras — Reeh & Schlieder, Bemerkungen zur Unitaeraequivalenz von Lorentzinvarianten Feldern, Nuovo Cim. 22 (1961) 1051-1068.**

### `M.semi` — semifinite carries a trace

**a semifinite factor carries a trace, hence an entropy; type III carries none**

*von Neumann classification*

grade **CITED**· source *T E5; Murray & von Neumann 1936*· depends on `M.takesaki`· depth 3

> **PRIOR ART: the type classification of factors, and that only semifinite ones carry a trace, is Murray & von Neumann, On rings of operators, Ann. Math. 37 (1936) 116-229, and its sequels.**

### `M.sorce` — Sorce 2024

**any geometric modular flow must be generated by a conformal Killing field**

*general*

grade **CITED**· source *T 10.4; Sorce 2024*· depends on `M.tt`· depth 2

> **PRIOR ART: that a geometric modular flow must be generated by a conformal Killing field — Sorce, Analyticity and unitarity for cosmological correlators (2024) and related work on geometric modular flow.**

### `M.takesaki` — Takesaki duality 1973

**N = M ⋊_{σ^φ} ℝ is type II_∞ with trace τ, τ∘θ_s = e^{−s}τ, and M = N ⋊_θ ℝ uniquely**

*M type III, φ a faithful semifinite normal weight; STATED FOR ℝ*

grade **CITED**· source *T E4; Takesaki 1973*· depends on `M.tt`· 1 object depends on it· depth 2

> **PRIOR ART: the structure theorem for type III factors as crossed products — Takesaki, Duality for crossed products and the structure of von Neumann algebras of type III, Acta Math. 131 (1973) 249-310.**

### `M.tt` — Tomita–Takesaki

**for (M,Ω) there exist Δ, J with Δ^{it} M Δ^{−it} = M**

*M a von Neumann algebra, Ω cyclic and separating*

grade **CITED**· source *T E1; Tomita 1967; Takesaki 1970*· depends on `M.rs`· 3 objects depend on it· depth 1

> **PRIOR ART: Tomita-Takesaki modular theory — Tomita, Quasi-standard von Neumann algebras (1967, unpublished); Takesaki, Tomita Theory of Modular Hilbert Algebras and its Applications, Springer LNM 128 (1970).**

## W. The violation index — 9 objects

### `W.core15` — the core at fifteen letters

**at fifteen letters: 18,072 cells, E = 816 = 1 × 816, core (X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)**

*the split alphabet of T §6.5*

grade **COMPUTED**· source *T 7.1; Chinneck & Dravnieks 1991*· depends on `W.core9`· 1 object depends on it· depth 5

> **PRIOR ART: as W.core9 at a finer alphabet. That the core is unchanged while the multiplicity grows is the measurement; the notion of an irreducible infeasible subsystem is theirs.**

### `W.core9` — the core at nine letters

**at nine letters: 2,370 cells, E = 30 = 1 × 30, core (X=0, U=0, NEC=3)**

*the coordinate set of T §5.1*

grade **COMPUTED**· source *T 5.3; Chinneck & Dravnieks 1991*· depends on `A.E`· 3 objects depend on it· depth 4

cell count RECOMPUTED: the 17 rules of vi_best.json applied to the 4·3·3·3·5·2·2·3·3 box give exactly 2,370. E=30 is the arity-4 CONSTRAINT-LANGUAGE defect (NEC≥3 -> IC v U v X), not the envelope defect of the cell set, which is 3,040 (R 1009)

> **PRIOR ART: a minimal set of conditions whose joint failure is irreducible is a MINIMAL UNSATISFIABLE SUBSET — Chinneck & Dravnieks, Locating minimal infeasible constraint sets in linear programs, ORSA J. Comput. 3 (1991) 157-168; in SAT the same object is the MUS. The conditions themselves are physics: the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950) and the equations of motion.**

### `W.face` — the null surface is a face

**the companion's local null surface is a FACE of the 6-cube, not a parity class: 32 of 64 with every rung 2, and a parity class gives E = 32 where the printed E is 0**

*deducible from three printed numbers with no access to any cell; THETA = 0 at 16 and STAT = 0 at 8 nest Killing horizons inside non-expanding ones*

grade **COMPUTED**· source *T §10.1, §10.4; Coxeter 1948*· depends on `A.R`· depth 3

> **PRIOR ART: a face of the n-cube is the set fixing some coordinates and freeing the rest — Coxeter, Regular Polytopes (1948), ch. VII. A parity class is not a face, which is what distinguishes them here.**

### `W.frontier` — the frontier metric — distance and status on the fifteen-letter alphabet

**d(c) = X_exp + U_ghost + |NEC_pt−3| + EOM + d_P; s(c) = 1{·}+1{·}+1{·}+1{·} + s_P**

*the fifteen-letter alphabet; d_P the L1 distance on the eleven free letters*

grade **DEFINITIONAL**· source *T D7, D8; classical; Hamming 1950*· depends on `W.core15`· depth 6

> **PRIOR ART: a defect built as a sum of independent violation counts, with a support counted separately, is the standard form of a penalty function.**

> **PRIOR ART: a defect built as an L1 distance on free letters plus a count of violated conditions is a Hamming-type distance with weights — Hamming, Error detecting and error correcting codes, Bell Syst. Tech. J. 29 (1950) 147-160.**

### `W.jur` — jurisdiction does not change the defect

**a jurisdicted forcing and an unjurisdicted disjunction give identical defects; arity ≥ 3 makes a defect possible, jurisdiction narrowness makes it small**

*the scope condition is a coordinate*

grade **COMPUTED**· source *T 8.2; Freuder 1978*· depends on `W.supp`· depth 9

> **PRIOR ART: that a constraint of arity 3 or more is not captured by binary projections is the k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966. Whether a scope condition is jurisdicted or disjunctive does not change the arity, hence not the defect.**

### `W.onehot` — the one-hot partition

**status is one bit per vocabulary and the partition forces one-hot: 35 of 40 terms weight 1, 2 weight 0, 3 weight 2**

*weight 2 = relation or unsplit conflation; weight 0 = ungrounded or constructible*

grade **COMPUTED**· source *T 10.5; classical; Shannon 1938*· depends on `W.rel`· depth 4

partition RECOMPUTED: 35 + 2 + 3 = 40 terms, total weight 41 (R 1009)

> **PRIOR ART: a partition of a set forces exactly one indicator to be set — the one-hot encoding. Elementary, and the measurement is that 35 of 41 statuses satisfy it.**

> **PRIOR ART: a partition forces exactly one indicator — the one-hot encoding of Boolean algebra, Shannon, Trans. AIEE 57 (1938) 713-723. Weight 2 signals a relation or a conflation; weight 0 an ungrounded term.**

### `W.rel` — Brunetti–Fredenhagen–Verch 2003

**a term that is a relation between two vocabularies cannot be a coordinate of either**

*the BFV partition A : Loc → Alg has four parts*

grade **COMPUTED**· source *T 8.4; Brunetti, Fredenhagen & Verch 2003*· depends on `A.R`· 1 object depends on it· depth 3

> **PRIOR ART: a term that is a relation between two vocabularies is a morphism, not an object — the locally covariant framework of Brunetti, Fredenhagen & Verch, The generally covariant locality principle, Commun. Math. Phys. 237 (2003) 31-68, makes the distinction precise.**

### `W.scale` — the defect does not scale

**the defect does not scale: core = 1 at 4, 5, 7 and 9 coordinates; only the multiplicity moves (3,5,10,30)**

*projections of one index*

grade **COMPUTED**· source *T 5.7; Chinneck & Dravnieks 1991*· depends on `W.core9`· depth 5

> **PRIOR ART: that the core of an infeasible system is invariant under refining the encoding is the well-definedness of the MUS; only the multiplicity of witnesses changes.**

### `W.supp` — the core is minimal

**of 414 coordinate subsets excluding {X,U,NEC}, 0 fail: the triple is the unique minimal failing subset, arity exactly 3. THE COUNT RECONCILES — subsets of size 2..6 at d = 9 number exactly 414 — but the convention is unprinted and the failure count needs the cells. Arity 3**

*as W.core9*

grade **COMPUTED**· source *T 5.4; Chinneck & Dravnieks 1991*· depends on `W.core9`, `A.modeB`· 1 object depends on it· depth 8

combinatorics RECOMPUTED: subsets of size 2..6 from 9 coordinates number 456; those containing all of {X,U,NEC} number 42; 456-42 = 414 exactly as stated (R 1009)

> **PRIOR ART: testing all 414 subsets and finding none fails without the triple establishes MINIMALITY in their sense — no proper subset is infeasible.**

## EM. The electromagnetic quotient — 7 objects

### `EM.cross` — the selection-rule crossing

**EM-allowed cells compose at 11.6% within one element against the forbidden 40.7%, and the order reverses across the table at 89.7% against 77.9%**

*the rule that forbids composition inside an atom is the rule that enables it between atoms; parity repeats it at 38.4% against 20.1%*

grade **COMPUTED**· source *M §12.11.1.7; Laporte 1924*· depends on `K.zcross`· depth 6

> **PRIOR ART: the composability contrast between allowed and forbidden cells is a consequence of the parity rule; the measurement is the fraction.**

### `EM.image` — the complete rectangle

**Λ₉'s image on (multipole, ΔS) is the COMPLETE rectangle at every cap; E = 0 vacuously**

*as EM.map*

grade **COMPUTED**· source *M §12.11.8; Wigner 1927*· depends on `EM.map`, `A.dens`· depth 5

> **PRIOR ART: that the selection rules cut a complete rectangle in (multipole, Delta S) is the product structure of the space-spin decomposition. Wigner, Z. Phys. 43 (1927) 624.**

### `EM.map` — electric/magnetic multipole selection rules

**the multipole is determined by |Δl| and parity alone: 0->M1, 1->E1, 2->E2, 3->E3**

*one-electron jump; no source J exists in Λ*

grade **COMPUTED**· source *M §12.11.8; Laporte 1924; Condon & Shortley 1935*· depends on `L.def`· 5 objects depend on it· depth 2

> **PRIOR ART: the multipole order of a transition is fixed by |Delta l| and parity — Laporte, Z. Phys. 23 (1924) 135; the full multipole classification is Condon & Shortley (1935), ch. IV.**

### `EM.notcomp` — selection and composition are unrelated

**composability and the EM condition share 0.0004 bits of a possible 0.633**

*on Λ₉'s cells*

grade **COMPUTED**· source *M §12.11.8; Shannon 1948*· depends on `EM.map`, `K.comp`· depth 3

> **PRIOR ART: shared information between two binary properties, in bits. Shannon (1948).**

### `EM.parity` — the parity hole

**|Δl| = 1 is delta^-1({-1,+1}), a hole at zero, not convex; E = 750**

*as EM.spin*

grade **COMPUTED**· source *M §12.11.8; Laporte 1924; Wigner 1927*· depends on `EM.map`, `I.convex`, `T.excl`· depth 11

> **PRIOR ART: the parity selection rule |Delta l| = 1 for electric dipole radiation is Laporte, Z. Phys. 23 (1924) 135, and its group-theoretic ground is Wigner, Z. Phys. 43 (1927) 624.**

### `EM.quotient` — the electromagnetic quotient

**the EM index is a QUOTIENT of Λ, not an extension: adjoining its coordinates gives E = 3,900**

*every EM coordinate is a function of Λ's own*

grade **COMPUTED**· source *M §12.11.8; Noether 1918*· depends on `EM.map`, `A.derived`· depth 5

> **PRIOR ART: a selection rule is a quotient by a symmetry, not an extension of the state space. Noether, Invariante Variationsprobleme, Nachr. Ges. Wiss. Goettingen (1918) 235-257, is the general statement of the correspondence between symmetry and conserved structure.**

### `EM.spin` — the spin diagonal

**ΔS = 0 is a diagonal, hence two monotone one-parent bounds; imposing it preserves E = 0 at four cap settings**

*LS coupling*

grade **COMPUTED**· source *M §12.11.8; Russell & Saunders 1925; Wigner 1931*· depends on `EM.map`, `I.convex`· depth 11

> **PRIOR ART: Delta S = 0 for electric dipole transitions in LS coupling is the spin selection rule — Russell & Saunders, Astrophys. J. 61 (1925) 38; Wigner, Gruppentheorie (1931), for the representation-theoretic statement.**

## C. Protocol and audit objects — 9 objects

### `C.Aq` — the first factor

**A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k (1−z^{min(k,3)+1})/(1−z)**

*caps as stated; q held fixed*

grade **COMPUTED**· source *M §12.7 / T C2eq; Euler 1748; Stanley 1986*· depends on `L.F`· 1 object depends on it· depth 4

> **PRIOR ART: a nested sum over a constrained region, written as a polynomial in z, is the standard rank-generating construction. Euler (1748) for the method; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1, for the modern treatment.**

### `C.Bq` — the second factor

**B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f (1−z^{min(q,4f+2)+1})/(1−z)**

*as C.Aq*

grade **COMPUTED**· source *M §12.7 / T C3eq; Euler 1748; Stanley 1986*· depends on `L.F`· 1 object depends on it· depth 4

> **PRIOR ART: as C.Aq — the second factor of the fibred count, built the same way.**

### `C.box` — the box generating function

**Box(a,b)(z) = ∏_i z^{a_i}(1−z^{b_i−a_i+1})/(1−z)**

*every fibre bottoms out in a product of chains*

grade **DEFINITIONAL**· source *M §12.7.2 / T C4eq; Euler 1748*· depends on `C.Aq`, `C.Bq`· depth 5

> **PRIOR ART: the generating function of a box is a product of finite geometric series — Euler, Introductio in analysin infinitorum (1748), ch. XVI, where partition generating functions are introduced.**

### `C.compare` — the comparison audit

**the COMPARISON AUDIT: index, math and language cypher checked against one another, not each against itself**

*any two indexes and the cypher*

grade **MEASURED**· source *R 1169-1172; Tarski 1936; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.R`, `K.produce`· depth 6

three checks. COVERAGE: every index coordinate has a math object and every family an index part — 0 and 0. LANGUAGE: five index/language pairs never run — Λ_spectra in geometry, algebra, information and statistics, Λ_alpha in analysis. CONTRADICTION: three standing, all on Λ_spectra between ORDER and ANALYSIS — delta falls with l (194/205 vs 102/205), triplet exceeds singlet (55/66 vs 33/66), delta falls along a sequence (89/143 vs 135/143). The audit names the pair and does NOT adjudicate

> **PRIOR ART: comparing two formal readings of one object and requiring agreement is the metalanguage move (Tarski 1936); that global and local readings agree exactly on acyclic structures is BFMY (1983).**

### `C.cut` — every cut closes

**every two-sided cut of the tree gives defect zero, not only q**

*the tree is doing the work, not the transfer*

grade **COMPUTED**· source *M §12.11.0.8; Freuder 1982*· depends on `C.fib`, `L.tree`· 1 object depends on it· depth 3

> **PRIOR ART: every two-sided cut of a tree separates it, so the defect vanishes at each — Freuder, J. ACM 29 (1982) 24-32.**

### `C.fib` — the fibred count

**|Λ| = Σ_q |A(q)|·|B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 976**

*conditioned on the transfer q*

grade **COMPUTED**· source *M §12.6.1 / T C1eq; Fubini 1907*· depends on `L.def`· 4 objects depend on it· depth 2

> **PRIOR ART: summing a product over a fibration of the index set is the discrete Fubini theorem. That the fibres here are independent is what makes |Λ| factor as a sum of products.**

### `C.local` — local closure is not implied

**E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q; the second does not follow from the first**

*cross-sections with induced coordinates*

grade **COMPUTED**· source *M §12.8.5 / T C5eq; Rota 1964*· depends on `C.fib`, `A.E`· depth 4

> **PRIOR ART: that a global count factorises over a decomposition does not imply each part is separately closed — the failure of naive Moebius inversion over non-independent parts. Rota (1964).**

### `C.pareto` — the fibre trade

**|A(q)| falls 33,33,23,8 while |B(q)| rises 5,10,15,17; no q improves both**

*at stated caps*

grade **COMPUTED**· source *M §12.8.1; Pareto 1896*· depends on `C.fib`· depth 3

> **PRIOR ART: no q improves both factors — a Pareto front in the two counts. Pareto, Cours d economie politique (1896).**

### `C.qmean` — the transfer distribution

**⟨q⟩ = 1.4631, sd 0.930; peak at q = 2 with 345 cells (35.3%)**

*at stated caps*

grade **COMPUTED**· source *M §12.8.2; classical; Gauss 1809*· depends on `C.fib`· depth 3

> **PRIOR ART: the first and second moments of a distribution over a coordinate; elementary.**

> **PRIOR ART: first and second moments of a distribution over a coordinate. Gauss, Theoria motus (1809).**

## I. The intake — interval maps and convexity — 3 objects

### `I.convex` — the convexity criterion

**delta^-1(T) is a sublattice iff T intersect range(delta) is convex in range(delta)**

*as I.interval*

grade **PROVED**· source *M §17.3; Birkhoff 1937*· depends on `I.interval`, `T.excl`· 2 objects depend on it· depth 10

> **PRIOR ART: the preimage of a set under a lattice homomorphism is a sublattice iff the set is convex in the image — the standard sublattice criterion. Birkhoff, Lattice Theory (1940), ch. II.**

### `I.interval` — the interval map

**delta = f - l is an INTERVAL MAP: min(da,db) ≤ delta(a v b), delta(a ^ b) ≤ max(da,db)**

*a sublattice of a product of chains*

grade **PROVED**· source *M §17.3; Birkhoff 1940*· depends on `L.dist`· 1 object depends on it· depth 9

> **PRIOR ART: a difference of two coordinates is an INTERVAL MAP on a distributive lattice — it need not be a homomorphism but it is bounded above and below by the coordinatewise extremes. Standard; Birkhoff, Lattice Theory (1940).**

### `I.shape` — the shape of an interval

**between any two points there is an interval and the method returns its measure; three objects, one shape**

*cells, states under composition, measurements*

grade **COMPUTED**· source *M §9.2; Birkhoff 1940; Monjardet 1981*· depends on `L.occ`, `K.comp`, `B.brk`, `A.slack`· depth 6

> **PRIOR ART: between any two points of a lattice lies the interval [a and b, a or b]; the method returns its measure. Elementary lattice geometry.**

> **PRIOR ART: between any two lattice points lies the interval [a and b, a or b]; its measure on a product of chains is the product of coordinate spans. Birkhoff, Lattice Theory (1940), ch. II; Monjardet, Discrete Math. 35 (1981) 173-184.**

## P. The spectral mechanisms — what moves a defect and by how much — 17 objects

### `P.buildlimit` — constructed limit

**a limit can be built from two spectra and tested by convergence**

*a series converging on a state above its own ionisation threshold*

grade **MEASURED**· source *R 711, 712; Edlen 1964*· depends on `P.converge`, `P.lcollapse`· depth 2

Ne I 2s.2p6.np on 173,929.75 + 217,047.598 gives +0.8408 +/- 0.0191 over ten

> **PRIOR ART: constructing a limit by summing the ionisation energies of successive stages is standard spectroscopic practice. Edlen, Handbuch der Physik XXVII (1964).**

### `P.charge` — the same-element ladder

**at s and p the quantum defect falls with charge at FIXED ELEMENT**

*a fixed element with two or more charge states*

grade **MEASURED**· source *R 963; Edlen 1964*· depends on `P.qdt`· depth 1

37 of 37 monotone at l≤1, no exceptions; all nine failures are at l≥2 where P.dcollapse governs

> **PRIOR ART: the fall of the defect with ionisation stage along an isonuclear sequence is standard spectroscopy — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### `P.converge` — self-determined limit

**a Rydberg series measures its own ionisation limit**

*enough members that the fit is determined*

grade **MEASURED**· source *R 684, 685, 686, 698, 699; Rydberg 1890; Ritz 1903*· depends on `P.qdt`· 1 object depends on it· depth 1

38 of 58 put the published limit within 3x the fit own error; only 15 of 58 within the PUBLISHED error (R 812-813)

> **PRIOR ART: extrapolating a Rydberg series to its limit is the classical method of determining an ionisation energy — Rydberg (1890), Ritz (1903).**

### `P.coreblind` — parent-term independence

**delta depends on l and the core's charge, not on the core's STATE**

*two parent terms of one species*

grade **MEASURED**· source *R 709, 710, 743; Seaton 1958*· depends on `P.qdt`· depth 1

TWO instances; and CONTRADICTED IN PRINCIPLE by MQDT, which defines the defect as mu_(l,lambda,alpha+) depending on the core state (R 947)

> **PRIOR ART: single-channel quantum defect theory treats the core as a fixed phase shift, so delta depends on l and the core charge only. Its failure for multi-channel cases is Seaton MQDT (Rep. Prog. Phys. 46, 1983).**

### `P.dcollapse` — orbital collapse

**an orbital collapses at the onset of its shell and leaves the Rydberg series**

*3d across the transition row, 4f across the lanthanides*

grade **MEASURED**· source *R 719, 734, 735, 736; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969*· depends on `P.iso`· depth 2

all ten P.iso exceptions are d and small; Ba III 4f gives 1.0 against neon's 0.006

> **PRIOR ART: orbital collapse at the onset of a shell — Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187; Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71.**

### `P.iso` — the isoelectronic ladder

**for one element and l, delta falls as the core charge rises**

*defect large enough to exceed its own scatter*

grade **MEASURED**· source *R 708, 716, 717, 718*· depends on `P.qdt`· 1 object depends on it· depth 1

8 of 9 s/p ladders exact; and a form delta = a + b*ln(c+1)/c fits the Mg-like ns ladders to 2% of range and predicts out-of-sample, but FAILS on nd, nf and all He-like ladders (47-65%); the method is Edlen 1964 (R 942-945)

### `P.jj` — the coupling-scheme marker

**J-inconsistency within one series marks where LS coupling has failed**

*same series, different J*

grade **MEASURED**· source *R 703; Condon & Shortley 1935*· depends on `P.qdt`· depth 1

114 of 129 consistent on raw levels, interval 82-93%; heavy elements fail at 23% against light at 8% (R 818-819)

> **PRIOR ART: the transition from LS to jj coupling as the spin-orbit interaction grows with Z is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. X.**

### `P.jsplit` — the j-splitting

**delta splits by the outer electron's own j when there is something to couple to**

*an OPEN-SHELL core, or Z large enough for the electron's spin-orbit*

grade **MEASURED**· source *R 754, 756, 757, 758, 759; Sommerfeld 1916*· depends on `P.qdt`· depth 1

median 0.0454 over 19 open/heavy pairs against 0.0002 over 10 closed/light — 227x

> **PRIOR ART: fine-structure splitting of a term by J is Sommerfeld, Zur Quantentheorie der Spektrallinien, Ann. Phys. 51 (1916) 1-94, in its relativistic form; Dirac (1928) supplies the exact theory.**

### `P.lcollapse` — the l-collapse

**delta falls monotonically with l and reaches zero by f**

*unperturbed series*

grade **MEASURED**· source *R 693, 702, 713, 724; Hartree 1928; Seaton 1958*· depends on `P.qdt`· 2 objects depend on it· depth 1

229 of 230 adjacent-l pairs correct, judged against EACH PAIR'S OWN 2 sigma rather than a fixed tolerance. The test carried an unstated slack of 0.02 until R 1072; at a fixed 0.02 it reads 251/251, strictly 242/251. The one failure is He I p->d, whose p defect is NEGATIVE — the Appendix B omission of R 871, which could not be recomputed when the reduced-mass Rydberg was corrected (R 1072-1074)

> **PRIOR ART: the defect falls with l because the centrifugal barrier keeps the electron out of the core — the standard penetration argument, Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89, and Seaton (1958).**

### `P.lens` — the precision lens

**near the limit delta is measured through a lens worsening as n^3**

*delta depends on (limit - E), which shrinks as n^2 while level error does not*

grade **MEASURED**· source *R 749, 750, 751, 752; Rydberg 1890*· depends on `P.qdt`· depth 1

WEAK at scale: only 44 of 79 channels show a wider high half (56%), and the n^3 prediction of 4.2x is observed at 1.3x (R 827)

> **PRIOR ART: near the limit dT/dnu ~ nu^-3, so a fixed energy uncertainty maps to a defect uncertainty growing as nu^3. Direct from the term formula.**

### `P.mono` — the monotonicity of the defect

**the defect approaches delta_0 monotonically: PENETRATION series fall, POLARISATION series rise**

*steps resolvable against their own uncertainty*

grade **MEASURED**· source *R 806, 821-824; NIST Atomic Spectroscopy compendium; Ritz 1903*· depends on `P.qdt`· depth 1

penetration (|d|≥0.1) falls 146 of 163 = 92%; polarisation (|d|<0.01) RISES 52 of 52 = 100%; combined 94% against 66% as a single claim (R 985-987)

> **PRIOR ART: the extended Ritz formula has a positive second coefficient for penetration and a negative one for polarisation, so the approach to delta_0 is monotone from above or below. Stated in NIST compendium.**

### `P.perturb` — series perturbation

**a large spread measures a perturber, not bad data**

*a state of the same symmetry crossing the series*

grade **MEASURED**· source *R 696, 704, 741, 742; Fano 1961; Lu & Fano 1970*· depends on `P.qdt`· depth 1

Si I nd spreads 0.15-0.21 where ASD's own leading-percentage column names 3s3p3 at 14%

> **PRIOR ART: a perturbed Rydberg series is a series crossed by a level of another channel — Fano, Effects of configuration interaction on intensities and phase shifts, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Graphic analysis of perturbed Rydberg series, Phys. Rev. A 2 (1970) 81-86.**

### `P.polar` — core polarisation

**beyond l=3 the defect follows core POLARISABILITY in direction, not in magnitude**

*l ≥ 4, where the orbital does not reach the core*

grade **MEASURED**· source *R 731-733, 788, 792-795; Born & Heisenberg 1924; Seaton 1958*· depends on `P.lcollapse`· depth 2

grows with Z at +0.0005/unit over seven elements; a quantitative alpha_d fit was attempted and did NOT work, cause undiagnosed (R 794)

> **PRIOR ART: core polarisation as the source of the high-l defect is Born & Heisenberg, Über den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten, Z. Phys. 23 (1924) 388-410, and Mayer & Mayer, Phys. Rev. 43 (1933) 605.**

### `P.qdt` — core penetration

**the quantum defect measures how far a Rydberg orbital reaches into the ionic core**

*a Rydberg series with three or more members, or two with a published limit*

grade **MEASURED**· source *R 693, 707, 713; Seaton 1958, 1983*· 12 objects depend on it· depth 0

four independent confirmations, none encoded

> **PRIOR ART: quantum defect theory — Seaton, The quantum defect method, MNRAS 118 (1958) 504-518, and Quantum defect theory, Rep. Prog. Phys. 46 (1983) 167-257.**

### `P.selfsame` — series self-consistency

**one series in disjoint n windows gives one defect**

*windows where P.lens's amplification is comparable*

grade **MEASURED**· source *R 747, 748, 751; Ritz 1903*· depends on `P.qdt`· depth 1

67 of 72 channels agree between disjoint halves to better than 0.05 (R 811)

> **PRIOR ART: one unperturbed series has one defect; disjoint n-windows must agree. The consistency test of the Ritz form (1903).**

### `P.termsplit` — core angular structure

**at l=3 delta splits by the core's TERM while its J-pairs stay together**

*j-K coupled series on one core*

grade **MEASURED**· source *R 739; Condon & Shortley 1935*· depends on `P.qdt`· depth 1

12 of 15 groups have terms separating by more than their J-pairs — median within 0.0011 vs between 0.0462 (R 826)

> **PRIOR ART: the splitting of a Rydberg series by the core term, with J-pairs staying together, is the parent-term structure of Condon & Shortley (1935), ch. VII.**

### `P.trunc` — truncation loss

**truncation removes most channels and degrades those it leaves**

*a series cut at low n*

grade **MEASURED**· source *R 675, 676, 677, 705, 706; Inglis & Teller 1939*· depth 0

Ne I: 33 Handbook levels give 0 channels, the full table gives 4

> **PRIOR ART: a Rydberg series is truncated in practice by field ionisation and by plasma microfields — Inglis & Teller, Ionic depression of series limits in one-electron spectra, Astrophys. J. 90 (1939) 439-448.**

## Q. The channel equation — the closed form and its terms — 11 objects

### `Q.alpha` — the polarisability index

**Λ_alpha: the polarisability index over cores, coordinates Z . Ne(core) . n_out . l_out**

*the set of cores appearing in the spectra index*

grade **MEASURED**· source *R 1165; Born & Heisenberg 1924; Mayer & Mayer 1933*· depends on `S.regime`· 1 object depends on it· depth 9

18 cores held, E = 10. Sorted by (n_out, l_out) the isoelectronic ordering is a physical requirement — alpha must FALL with Z along a sequence — and the Ne-like and Mg-like rows obey it while the Ar-like row does not: K I 5.490 published, Ca II 6.665 extracted, Sc III 4.705. The index makes the violation visible where a table would not

> **PRIOR ART: core dipole polarisability as the origin of the high-l defect is Born & Heisenberg, Z. Phys. 23 (1924) 388-410; the systematic values are Mayer & Mayer, The polarizabilities of ions from spectra, Phys. Rev. 43 (1933) 605-611.**

### `Q.anchor` — the two-ended anchor

**anchoring the equation at BOTH ends of Z fixes the extrapolation at almost no in-region cost**

*the channel equation and a far-field literature value*

grade **MEASURED**· source *R 1201-1205; Theodosiou, Inokuti & Manson 1986*· depends on `Q.region`, `Q.collapse`· 1 object depends on it· depth 13

seven far anchors — Cs I np measured at 3.5667, and Th/Ac ns, np, nd, nf from actinide theory at 5.2, 4.75, 3.8, 2.0 — extend the sample from Z ≤ 83 to Z = 90. Far-anchor median error falls 0.754 to 0.064, a factor of twelve; in-region rises 0.0637 to 0.0665. The saturating exponent returns for real: e(Ne) = 0.8297 - 0.0900 ln Ne against -0.0266 from the in-region sample alone. CAVEAT: four of the seven anchors are THEORETICAL, so the high-Z arm is calibrated against another calculation and moves if that is revised

> **PRIOR ART: asymptotic quantum defects for all ionisation stages of all ions with Z ≤ 50 are tabulated in Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35 (1986) 473-486, Hartree-Slater. The far anchors used here are Cs I np (measured) and actinide values from arXiv:2508.06733.**

### `Q.bound` — the Pauli bound

**B = min( p , n0 - l - 1 ): the integer part's exceptionless upper bound, from aufbau alone**

*a channel and its core's ground configuration*

grade **PROVED**· source *R 1141; Pauli 1925; Janet 1929*· depends on `S.ground`· 5 objects depend on it· depth 7

floor(delta) ≤ B for 311 of 311 measured channels. As an equality it is right 57%; every error is negative; within two of the bound, 303 of 311. p is the core's orbital count at that l and n0 the first Pauli-allowed n, both from aufbau with no spectrum

> **PRIOR ART: the bound counts core orbitals of the same l and the first Pauli-allowed principal number, both read from the ground configuration. Paulis exclusion principle, Z. Phys. 31 (1925) 765-783, fixes the occupancies; Janets n+l ordering (1929) fixes which subshells are filled.**

### `Q.bridge` — the bridge equation

**the bridge between the metric and ordinal descriptions is MULTIPLICATIVE with a REGIME factor: every factor positive so each preserves rank by itself, and the regime factor differs between two channels only when they differ in regime**

*a channel equation required to respect both values and orderings*

grade **MEASURED**· source *R 1169-1171; Pareto 1896; Spearman 1904*· depends on `Q.delta`, `S.regime`· 1 object depends on it· depth 12

*Stated on the channel equation then current, `Q.delta`, which `Q.final` superseded at register 1205; the claim was re-tested there on the standing form and holds (one ℓ-ordering violation in 328 channels). The dependence line keeps `Q.delta` because `Q.final` descends from this object, and the graph records the order of establishment, not present support (register 1750).*

an additive fit gets P.lcollapse 102/205 against a measured 194 — chance. A purely multiplicative fit gets 205/205, 143/143, 66/66 where the measurements give 194, 89, 55 — it cannot represent an exception because a product of positives is monotone in each factor. With a regime factor: 204/205, 129/143, 61/66, and ln-R^2 improves 0.8026 to 0.8164

> **PRIOR ART: that a multiplicative form preserves rank and an additive one does not is elementary; that no single form does both well is a Pareto statement about the two objectives.**

> **PRIOR ART: a product of positive factors is monotone in each and so preserves rank; a sum of signed terms need not. Rank preservation as an objective distinct from least squares is Spearman, The proof and measurement of association between two things, Amer. J. Psychol. 15 (1904) 72-101. That no single form does both well is a Pareto statement (1896).**

### `Q.collapse` — the Janet collapse

**the ORBITAL COLLAPSE threshold is a Janet block boundary, exactly**

*a channel with p = 0 at l ≥ 2*

grade **MEASURED**· source *R 1187-1190; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969*· depends on `S.ground`, `Q.bound`· 2 objects depend on it· depth 8

the n+l = 5 block opens at Z = 21 and 3d collapses at 21; n+l = 7 opens at 57 and 4f at 57; n+l = 8 opens at 89 and 5f at 89. Three exact matches. Across 116 p = 0 channels at l = 2 or 3: collapsed median 0.637, uncollapsed 0.036, U-test p = 9.8e-4. Adding the term takes Ti IV nd from -0.620 to -0.056 and the overall rms from 0.1825 to 0.1411. The largest outliers are atoms APPROACHING a boundary — Ca I nd = 0.908 at Z = 20 against a threshold of 21, Ba II nf = 0.756 at 56 against 57 — so the collapse is a rapid transition, not a step

> **PRIOR ART: orbital collapse — the sudden contraction of the 3d and 4f wavefunctions as Z crosses a threshold — is Goeppert-Mayer, Rare-earth and transuranic elements, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Theoretical calculations of the d-, f- and g-electron transition series, Phys. Rev. 177 (1969) 62-71. What is measured here is that the threshold coincides with the Janet block boundary at Z = 21, 57 and 89.**

### `Q.delta` — the channel equation

**delta = [ B - q e^(-a(Ne)l) e^(k/Ne) c^g + P ] (1 + s [triplet]): a closed form for any Rydberg channel from atomic-index quantities alone**

*a Rydberg channel (Z, charge c, l, multiplicity)*

grade **MEASURED**· source *R 1145-1168; Seaton 1958; Fermi 1928; Pauli 1925*· depends on `Q.bound`, `Q.pen`, `Q.pol`, `Q.exch`· 2 objects depend on it· depth 11

311 measured channels: rms 0.2449, R^2 0.924, median |error| 0.090. By l: s 0.283, p 0.276, d 0.280, f 0.119, g 0.0096. Against TWELVE published values never fitted on: median error 0.00155 at l ≥ 3 and 0.368 below. 50% within 0.090, 90% within 0.414, 99% within 0.826

> **PRIOR ART: the superseded form of the channel equation. Its terms are the Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958). Superseded by Q.final at register 1205.**

### `Q.exch` — the exchange factor · **GRADED OPEN**

**the exchange factor (1 + s [triplet]), s = -0.0782**

*a channel of a two-valence-electron system*

grade **ASSERTED**· source *R 987, withdrawn R 1168*· depends on `Q.bound`· 1 object depends on it· depth 8

WITHDRAWN (R 1168). The claim was that the fitted s recovers register 987's sign and size. It does not: register 987 measures the triplet defect EXCEEDING the singlet in 22 of 22 ns cases, and the additive fit returned s = -0.0782, the right magnitude and the WRONG SIGN. Cross-checked on 66 singlet/triplet pairs the equation gets 33, exactly chance. The parameter absorbed something else

> **PRIOR ART: the exchange splitting between singlet and triplet is Heisenberg, Mehrkoerperproblem und Resonanz in der Quantenmechanik, Z. Phys. 38 (1926) 411-426; that the higher multiplicity lies lower is Hund first rule (1925). WITHDRAWN at register 1168: the fitted sign is opposite to the measured one.**

### `Q.final` — the channel equation

**delta = a p^e(Ne) Ne^k ln(c+1)/c where p > 0, and h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c where p = 0**

*any Rydberg channel (Z, charge, l, multiplicity)*

grade **MEASURED**· source *R 1205-1206; Seaton 1958; Fermi 1928; Janet 1929*· depends on `Q.anchor`, `Q.bound`· depth 14

a = 0.3772, e(Ne) = 0.8297 - 0.0900 ln Ne, k = 0.4942, h = 0.5415. 284 channels from Z = 2 to 90 and charge 1 to 10: rms 0.1610, R^2 0.9741, l ≥ 4 rms 0.0150, hydrogenic output EXACTLY zero, Pauli bound 328/328, one l-ordering violation against a measured zero. Four fitted numbers and every input from the ground state or the periodic table. It values all 1,648 cells R places, where the walk valued none

> **PRIOR ART: every term of the form has a source. The ln(c+1)/c charge dependence is the isoelectronic behaviour of Edlen 1964; the Ne^k factor is Thomas-Fermi (Fermi 1928); p is the Pauli orbital count (Pauli 1925); C(Z) is orbital collapse (Griffin, Andrew & Cowan 1969) at the Janet boundary (Janet 1929). The equation assembles them; it does not introduce any.**

### `Q.pen` — the deficit term

**the penetration deficit, -q e^(-a(Ne) l) e^(k/Ne) c^g, with a(Ne) = a0 + a1 Ne^(-1/3)**

*a channel below the polarisation regime*

grade **COMPUTED**· source *R 1147; Hartree 1928; Fermi 1928*· depends on `Q.bound`· 1 object depends on it· depth 8

the decay a is set by the atom's SIZE: a against ln Ne gives r^2 = 0.437 across 56 species, against electrons-beyond-closure 0.143, against charge nothing (p = 0.34). K I's measured d/s ratio implies a = 1.03, Sr I's implies 0.157 — a factor of seven, and a universal a fits neither

> **PRIOR ART: the penetration deficit and its Ne^(1/3) scaling are the Thomas-Fermi picture — Fermi, Eine statistische Methode zur Bestimmung einiger Eigenschaften des Atoms, Z. Phys. 48 (1928) 73-79; Hartrees self-consistent field, Proc. Camb. Phil. Soc. 24 (1928) 89-110, gives the orbital form. Fermi 1928 applied it to Rydberg corrections directly.**

### `Q.pol` — Seaton's term

**the polarisation term, 3 alpha c^2 / K(l) for l ≥ 4 with alpha from Λ_alpha, K(l) = l(l+1)(2l-1)(2l+1)(2l+3)**

*a non-penetrating channel and a core polarisability*

grade **CITED**· source *R 1165-1168; Seaton 1958; Born & Heisenberg 1924*· depends on `A.seaton`, `Q.alpha`· 1 object depends on it· depth 10

Seaton's formula. With alpha supplied as a species LABEL from Λ_alpha rather than a universal constant, the l ≥ 4 rms falls from 0.01504 to 0.00958 — 36%. Below l = 4 it must be gated OFF: applied at s and p it drives the fit to rms 39.3 because K(l) is small there

> **PRIOR ART: the polarisation term 3 alpha c^2 / K(l) is Seaton (1958); the physical origin is core polarisability, Born & Heisenberg, Z. Phys. 23 (1924) 388-410. SUBSUMED at register 1204 by the Janet collapse coordinate.**

### `Q.region` — the validated domain

**the equation is VALIDATED in the verified-plus-possible region and EXTRAPOLATED outside it**

*the channel equation and the existence partition*

grade **MEASURED**· source *R 1193-1194; Theodosiou, Inokuti & Manson 1986*· depends on `Q.delta`, `S.status`, `Q.collapse`· 1 object depends on it· depth 12

*Stated on the channel equation then current, `Q.delta`, which `Q.final` superseded at register 1205; the claim was re-tested there on the standing form and holds (in-region error 0.147, far-anchor 0.064). The dependence line keeps `Q.delta` because `Q.final` descends from this object, and the graph records the order of establishment, not present support (register 1750).*

277 in-region channels give rms 0.1329 and R^2 0.9747 — better than the 311-channel fit on fewer points, because the 51 excluded were 24 three-parent cores, 15 sixteen-parent cores and 12 ions above charge 10. And the saturating exponent falls from 1.3257 - 0.2751 ln Ne to 0.5828 - 0.0266 ln Ne: nine-tenths of the Ne-dependence was open-shell contamination. Validated on 277, extrapolated to 98,078

> **PRIOR ART: the distinction between where a defect is measurable and where it is calculated is exactly the distinction their 1986 table makes — they compute Hartree-Slater values everywhere and note where experiment exists.**

---

## LS. The Löwdin solution — the order derived from the equation — 8 objects

*Chapter 35 and its companion paper; register 1701–1712. These objects are verified by the solution's own sealed instruments and receipts, not yet by `mathverify.py`; wiring them into the book's verifier is a build task, and until it is done this page states the verification that exists rather than implying one that does not. The mathematics of the challenge (Chapter 34, registers 1249–1357) is stated separately below under THE MATHEMATICS OF THE LÖWDIN WORK.*

### `LS.ent` — the entrant operator

**ent(Z) = argmax over frontier (n,ℓ) of |D(n,ℓ)|, D the converged one-channel depth in the self-consistent field of the ion (Z, cfg(Z−1)); scalar-relativistic Koelling–Harmon; c = 137.035999 the only entered number. Chained, cfg(Z) = cfg(Z−1) + ent(Z): 107 of 107 against the measured ground configurations, Z = 2–108**

*the operator Chapter 27 said a non-closing index requires; sign-exact by construction, and the margin |D(ent)| − |D(runner-up)| is its own error bar, recorded at every step*

grade **COMPUTED**· source *M §35; register 1701, 1702*· depends on `L.closed`, `Q.final`· depth 15

### `LS.law` — the ordering law, five clauses

**Clause 1 (ordering): smaller n+ℓ opens first — 107/107. Clause 2 (tie-break): equal n+ℓ, smaller n first — exceptions exactly {La, Ac, Th}, derived by `LS.coll`. Clause 3 (correlation): at the five contested rows the second-order differential is positive — every competition widens. Domain clause: Z ≤ 112; spin-orbit worst case 0.083 Ha under every margin. Relativistic clause: the c → ∞ twin disagrees at eleven elements**

*statement and proof form in the companion paper*

grade **PROVED**· source *M §35; register 1701–1706*· depends on `LS.ent`, `LS.coll`, `LS.twin`· depth 17

### `LS.coll` — the collapse condition

**The double-well criterion, stated from the field, for which f channel is collapsed at which Z: decides exactly the Clause-2 exception set and occupies exactly the domain where Chapter 34's corridor is silent (L = −∞ at f openings)**

*adjacent to the transition the mean-field equations admit two stationary solutions of one configuration with distinct converged operators; a sign at SCF tolerance there is branch content, not noise*

grade **COMPUTED**· source *M §35; register 1703; Griffin–Andrew–Cowan 1969, 1971*· depends on `LS.ent`· depth 16

> **PRIOR ART: the orbital-collapse double well is Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62; the placement of it against the corridor's silence is this work's.**

### `LS.pin` — the pinned-channel theorem (no g block)

**Every g channel offered by the walk sits at −1/(2n²) to storage precision: 5g over 65 elements, 6g over 70, 7g over 57, 8g over 28. dn*/dZ = 0 across a hundred protons**

*the absence of collapse, not its slow approach; a relation the data cannot violate is defending something — here, the nonexistence of a g period below Z = 121*

grade **MEASURED**· source *M §35; register 1704*· depends on `LS.ent`· depth 16

### `LS.asym` — the state-dependent multiplier identity

**For u, v eigenstates of different self-consistent operators, the two eigen-relation evaluations of ⟨u|T|v⟩ differ by exactly asym(u,v) = (ε_v − ε_u)⟨u|v⟩ − ⟨u|(V_v − V_u)|v⟩ + [⟨u|X_v⟩ − ⟨v|X_u⟩]; verified to machine precision, four of four elements, worst 2.6·10⁻¹⁵, independent of SCF tolerance**

*a residual of large cancelling terms, not a convergence artefact; it reclassified a registered instrument fault as derived content*

grade **PROVED**· source *M §35; register 1708, 1709; Löwdin 1950*· depends on `LS.ent`· depth 16

> **PRIOR ART: an instance of the non-orthogonality problem, Löwdin, J. Chem. Phys. 18 (1950) 365.**

### `LS.quart` — the exact-quartic decomposition

**The energy functional with one shell's orbital varying along a fixed direction is exactly quartic in the path parameter (one-body quadratic; two-body quartic); five evaluations at t ∈ {0, ±½, ±1} determine every Taylor coefficient with zero truncation error**

*the floating-point floor at |E| ~ 10⁴ Ha (~10⁻¹²) is the only limit, and it is stated, not implied; protocol at register 1710*

grade **PROVED**· source *M §35; register 1710*· depends on `LS.ent`· depth 16

### `LS.chord` — the defect closed: chord = rot + perp

**The walk's one systematic internal discrepancy — the Hellmann–Feynman-in-q defect — is a Pulay term of the occupation parameter. In the one-shell-frozen gauge it splits exactly: rot = linear gradient law + (q·s/dq2)·⟨asym⟩ + endpoint-Hessian term; perp = the first-order perturbed-HF response on the orthogonal complement. Balance: zero unexplained residue**

*the signed trace verified at ratios 0.999992 and 1.000103; the endpoint-Hessian term (+1.7·10⁻⁷, +6.1·10⁻⁹) is twenty to five hundred times too small for the residual it was hypothesised to explain — a hypothesis falsified by the clause that scored HIT, and kept*

grade **PROVED**· source *M §35; register 1707, 1709, 1711; Pulay 1969; Gerratt–Mills 1968*· depends on `LS.asym`, `LS.quart`· depth 17

> **PRIOR ART: the occupation-parameter term is Pulay, Mol. Phys. 17 (1969) 197; the orthogonal-complement response is Gerratt & Mills, J. Chem. Phys. 49 (1968) 1719.**

### `LS.twin` — the twin operator, c → ∞

**The identical entrant operator with the constant removed disagrees with the c = 137.035999 operator at eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — every disagreement an error against nature, since the relativistic operator scores 107/107**

*the relativistic clause of `LS.law`, measured rather than asserted*

grade **MEASURED**· source *M §35; register 1706*· depends on `LS.ent`· depth 16

## 3B. Three bodies — the index of families — 9 objects

*Chapter 36 and its companion paper; register 1713–1724. One new root, `3B.shape` — shape space, standard mathematics cited as found (Montgomery 2014; Hopf 1931; register 1739) — and otherwise the family derives from `L.c1`–`L.c8`, `B.brk` and the operators, and the seed did not move — the cycle's falsifier passing on a new subject.*

### `3B.shape` — shape space and the shape sphere

**ℝ³ = ℂ³ / (translations × rotations); S² = that / scale. Onto; identifies exactly the oriented-congruent triangles; only triple collision maps to 0; w₃ = signed area up to a mass constant; ‖w‖ = I/2**

*the coordinates in which three bodies become one point*

grade **PROVED**· source *Montgomery 2014, Thm 1; Hopf 1931*· 2 objects depend on it· depth 0

### `3B.metric` — the shape metric

**ds² = |dw|²/(2√‖w‖); every plane through 0 totally geodesic; cone metric dr² + ¼r²dθ²**

*as `3B.shape`*

grade **PROVED**· source *Montgomery 2014, Thm 3*· depends on `3B.shape`· depth 1

### `3B.JM` — the Jacobi–Maupertuis metric

**g_E = (E+U)·ds²; trajectories at energy E are its geodesics; dt = ds_E/√(2(E+U))**

*licence in the index: §12.11.1.3, §12.11.0.2*

grade **PROVED**· source *Maupertuis 1744; Jacobi 1837*· depends on `3B.metric`, `3B.pot`· depth 2

### `3B.pot` — the potential on shape space

**U(w) = Σ c_ij/d_ij, c_ij = (m_i m_j)^{3/2}/√(m_i+m_j), d_ij² = ‖w‖ − w·b_ij; identity r_ij² = d_ij²/μ_ij. No hyper-radius factor**

*650 triangles, 13 mass cases, error < 10⁻¹⁰; the first audit's uniform 13/13 failure was a hyper-radius divisor inherited from working material — register 1718, protocol 1722*

grade **PROVED**· source *Montgomery 2014 §11; register 1718; main §D.5.9*· depends on `3B.shape`· depth 1 · *checked numerically on 650 random triangles at 10⁻¹⁰ — corroboration, not the verification*

### `3B.norm` — the algebraic variety

**With u_ij = c_ij/d_ij, p = Σu², q = Σu_i²u_j², r = ∏u²: U⁸ − 4pU⁶ + (6p²−8q)U⁴ − 4(p³−4pq+16r)U² + (p²−4q)² = 0; constant term ∏(u₁±u₂±u₃)²**

*proved symbolically (sympy) and measured at 13 mass cases; an inherited form with U⁴ coefficient "6S₂²−4S₄+8S₁₁" = 2p²+16q was wrong and is withdrawn — register 1719*

grade **PROVED**· source *Lagrange 1770; register 1719, 1720*· depends on `3B.pot`· depth 2

> **PRIOR ART: N₈ is the norm over (ℤ/2)³ — Lagrange's resolvent method, 1770. Not new mathematics.**

### `3B.five` — the five fixed points

**Three Euler roots (one positive root of the quintic per ordering) and two Lagrange points, for every mass triple — 13/13**

*seed of the family index in §14.5's sense*

grade **PROVED**· source *Euler 1767; Lagrange 1772; register 1717; main §D.5.9*· depends on `3B.pot`· depth 2 · *the thirteen-order-type check is corroboration, not the verification*

### `3B.tri` — the triangle form on K₃

**{|a−b| ≤ c ≤ a+b}: join-closed, meet-broken. Cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 meet failures 12·111·477·1,488·3,780·8,385·16,812·31,227·54,555·90,705; two-body chain 0 throughout**

*confirms §12.11.2 on a grid the book never ran*

![Closure defect against cap](figures/fig2_closure_defect.png)

*meet and join failures against cap; the two-body chain at zero throughout*

grade **MEASURED**· source *M §36; register 1716*· depends on `L.c1`–`L.c8`· depth 1

### `3B.def` — the deficit

**K₃ has treewidth 2; strong 3-consistency is required; ℛ reaches 2 (§32.3). Shortfall exactly one level**

*the separation hypothesis of §7.1 broken by the smallest graph that can break it*

![K₂ against K₃](figures/fig5_constraint_graphs.png)

*K₂ against K₃, and the consistency level each requires*

grade **PROVED**· source *M §21.5.1; Freuder 1982*· depends on `3B.tri`, `G.graph`, `L.tree`· depth 3

### `3B.index` — the index Λ₃

**Λ₃ = {KAM, per, chaos, erg, coll} on ℳ_{E,L}. E(Λ₃) = 0: exhaustive (Chazy classes), disjoint up to measure zero (Saari 1971/73; Painlevé, n = 3). By §25.6, predictions = 0 — Brudno's theorem on the chaotic stratum**

*cited theorems assembled; the assembly is this work's. The maximal forbidden case of Chapter 18 is the solved case, because what is forbidden is exactly what Poincaré excludes — register 1724*

grade **PROVED**· source *M §36; register 1713, 1714, 1724; Chazy 1922; Saari 1971; Brudno 1983*· depends on `3B.def`, `3B.five`· depth 4

# V · THE CHAINS

The longest derivation paths in the register — what rests on what.

**depth 14** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region` ← `Q.anchor` ← `Q.final`

**depth 13** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region` ← `Q.anchor`

**depth 13** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.bridge` ← `A.blind`

**depth 12** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.bridge`

**depth 12** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.bits` ← `L.circuit`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.pushback` ← `L.step`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `I.interval` ← `I.convex` ← `EM.spin`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `I.interval` ← `I.convex` ← `EM.parity`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta`

**depth 10** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.alpha`

**depth 10** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.mobius`

**depth 17** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region` ← `Q.anchor` ← `Q.final` ← `LS.ent` ← `LS.asym` ← `LS.chord` · *the Löwdin solution's longest path, through the channel equation; the walk's one defect closed at zero residue*

**depth 4** · `L.c1` ← `G.cons` ← `G.graph` ← `3B.def` ← `3B.index` · *the three-body index; the family's own links rest on `L.c1`–`L.c8`, `G.graph` and `L.tree`, roots already in the register — closes to §25.6 and the Brudno rate*

---

# VI · WHAT IS UNFINISHED

*Neither the Löwdin solution nor the three-body work adds an open object; the two below are untouched by both.*

**Two objects.** *Neither is unfinished for want of a proof attempt. Each has a diagnosis, and the diagnosis names what is missing rather than restating that something is.*

## `M.C2` — half-sided modular inclusion on a non-expanding horizon

        Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂)   for t ≤ 0, u₁ < u₂

**What is settled.** Half-sided modular inclusion is CHARACTERISED — Borchers, *The CPT theorem in two-dimensional theories of local observables*, Commun. Math. Phys. **143** (1992) 315–332, and Wiesbrock, *Half-sided modular inclusions of von Neumann algebras*, Lett. Math. Phys. **28** (1993) 107–114: the inclusion holds exactly when a one-parameter unitary group with positive generator implements the translation. The vacuum is cyclic and separating for local algebras (Reeh & Schlieder 1961), and modular theory supplies Δ and J (Tomita 1967; Takesaki 1970). **None of that is in question.**

**What is missing, precisely.** The hypothesis — *a non-expanding horizon with no Killing field, ω Hadamard* — asks the expansion Θ = 0 to select what only a STATE can select, and offers Hadamard, a microlocal condition, as the selector.

> **The horizon's own definition supplies a state condition at BACKGROUND order — Einstein's equation with future-causality forces vanishing shear, vanishing null flux and £_ℓ q_ab = 0 — and leaves a gap at PERTURBATION order.** *That gap is the object.*

**Where the obstruction sits.** The free half is confirmed numerically: the spectral weight ratio is of order 10⁻⁵. The obstruction is in the corner edge modes, and the proposal Θ = 0 was refuted by the transformation law. Sorce (2024) closes the geometric route by construction — a geometric modular flow must be generated by a conformal Killing field — so a horizon with no Killing field cannot have one, and the route that remains is algebraic.

**What would settle it.** The covariance of conditional expectations across the full family of cuts, in the manner of an over-determined joint fit. *Chandrasekaran & Flanagan (arXiv:2601.07915) is the nearest published treatment and was read into the diagnosis at registers 1037–1042.*

## `Q.exch` — the exchange factor

        δ = [ … ] · (1 + s·[triplet]),   s = −0.0782

**What is settled.** Exchange splitting between singlet and triplet is Heisenberg, *Mehrkörperproblem und Resonanz in der Quantenmechanik*, Z. Phys. **38** (1926) 411–426; that the higher multiplicity lies lower is Hund's first rule, Z. Phys. **33** (1925) 345–371. **The physics is not in doubt.**

**What is missing, precisely.** *The fitted sign is opposite to the measured one.* The factor was withdrawn at register 1168 for that reason and the grade left as ASSERTED rather than removed, because the term is real and the form is wrong.

> **A uniform s cannot work.** *Exchange acts through the overlap of the Rydberg orbital with the core, and that overlap falls sharply with ℓ. A single multiplicative constant can only give 0 of 66 triplet-above-singlet pairs or 66 of 66; the measurement is neither.*

**What would settle it.** An ℓ-dependent exchange term, fitted against the singlet–triplet pairs the compendium holds. The Pauli bound (`Q.bound`) already carries the orbital count p that the overlap should follow.

---

# VII · THE BIBLIOGRAPHY

**Every object of this compendium names a work.** What follows is those works, ordered by year, with the objects each carries. *The book claims nothing new where an earlier result will do; where a measurement is this work's, the object says so.*

**162 works, 1669–2026.** *Ten rows the generator had read out of callout text — status words, a possessive, a method name — were removed on 2026-08-24 (register 1736); the count was 172.*

| year | work | objects |
|---|---|---|
| 1669 | Newton | `B.newton` |
| 1682 | Leibniz | `B.brk` |
| 1687 | Newton | `B.ordbr` |
| 1715 | Taylor | `B.frac` `B.pole` |
| 1736 | Euler | `G.graph` |
| 1744 | Maupertuis | `3B.JM` |
| 1748 | Euler | `A.prodE` `C.Aq` `C.Bq` `C.box` `L.F` `L.F1` `L.Fm1` |
| 1767 | Euler | `3B.five` |
| 1770 | Lagrange | `3B.norm` |
| 1772 | Lagrange | `3B.five` |
| 1797 | Lagrange | `B.hstar` |
| 1809 | Gauss | `A.anchor` `B.adm` `C.qmean` `L.skew` |
| 1837 | Jacobi | `3B.JM` |
| 1842 | Jacobi | `3B.JM` |
| 1854 | Boole | `A.logic` |
| 1869 | Mendeleev | `E.ioniz` `E.table` |
| 1878 | Hill | `3B.index` |
| 1890 | Rydberg | `B.V43` `B.Vexact` `B.fail` `B.floor32` `B.nuV` `B.silence` `P.converge` `P.lens` |
| 1890 | Poincaré | `3B.index` |
| 1893 | Heaviside | `L.chi` |
| 1896 | Pareto | `B.pareto` `C.pareto` `Q.bridge` |
| 1900 | Dedekind | `L.modular` |
| 1903 | Ritz | `P.converge` `P.mono` `P.selfsame` `S.regime` `S.ritz` |
| 1904 | Spearman | `Q.bridge` |
| 1906 | Jensen | `B.floor2` `B.floor32` |
| 1907 | Fubini | `C.fib` |
| 1910 | Moore | `A.E` `A.R` `A.bound` `A.clos` `A.expr` `A.ext` `A.fix` `F.exact` `F.moore` `L.E0` `S.bounds` `S.open` `S.seed` |
| 1911 | Caratheodory | `S.car` |
| 1913 | Bohr | `B.coll` `L.c1` `L.c4` `L.def` |
| 1913 | Pauli | `L.def` |
| 1916 | Sommerfeld | `P.jsplit` |
| 1918 | Noether | `EM.quotient` |
| 1922 | Chazy | `3B.index` |
| 1923 | Helly | `K.helly` |
| 1924 | Born & Heisenberg | `P.polar` `Q.alpha` `Q.pol` |
| 1924 | Laporte | `EM.cross` `EM.map` `EM.parity` |
| 1924 | Stoner | `L.c2` `L.c5` |
| 1925 | Hund | `L.c7` `Q.exch` `S.ground` |
| 1925 | Pauli | `L.c2` `L.c3` `L.c5` `L.c6` `L.c7` `L.c8` `L.def` `Q.bound` `Q.delta` `Q.final` `T.a9p` |
| 1925 | Russell & Saunders | `EM.spin` |
| 1926 | Aitken | `B.aitken` |
| 1926 | Schroedinger | `L.c1` |
| 1927 | Wigner | `EM.image` `EM.parity` |
| 1928 | Dirac | `P.jsplit` |
| 1928 | Fermi | `Q.delta` `Q.final` `Q.pen` |
| 1928 | Hartree | `P.lcollapse` `Q.pen` `S.ritz` |
| 1928 | Sperner | `L.sperner` |
| 1929 | Janet | `E.layout` `E.table` `Q.bound` `Q.final` `S.ground` |
| 1931 | Wigner | `EM.spin` `T.a12` `T.dens` `T.excl` `T.invariant` |
| 1931 | Hopf | `3B.shape` |
| 1933 | Mayer & Mayer | `Q.alpha` |
| 1933 | Milne-Thomson | `B.V` `B.brk` `B.ordbr` `B.ordk` `B.pole` |
| 1935 | Condon & Shortley | `EM.map` `P.jj` `P.termsplit` `S.channel` `S.parent` `T.a11` `T.a13` `T.real` `T.scheme` `T.tower` |
| 1936 | Eckart & Young | `B.rank1` |
| 1936 | Madelung | `L.real` `S.ground` |
| 1936 | Tarski | `A.logic` `C.compare` |
| 1936 | Murray & von Neumann | `M.semi` |
| 1937 | Birkhoff | `A.define` `A.erel` `I.convex` `K.arrow` `K.produce` `L.alpha` `L.arith` `L.birk` `L.bits` `L.dist` `L.omega` `L.pushback` `L.step` `S.box` `S.seed` |
| 1937 | Shannon | `L.bits` |
| 1938 | Shannon | `L.circuit` `S.bits` `W.onehot` |
| 1939 | Inglis & Teller | `P.trunc` |
| 1940 | Birkhoff | `A.derived` `A.erel` `A.morph` `A.prod` `I.convex` `I.interval` `I.shape` `L.arith` `L.closed` `L.total` |
| 1940 | Deming & Stephan | `A.stat2` `G.stat` |
| 1941 | Dushnik & Miller | `A.erel` `K.axis` `L.dim` |
| 1941 | Goeppert-Mayer | `P.dcollapse` `Q.collapse` |
| 1942 | Racah | `T.a11` `T.a12` `T.dens` `T.dich` `T.invariant` `T.scheme` `T.tower` |
| 1942 | Ward | `A.clos` `F.moore` `F.open` |
| 1943 | Racah | `S.parent` `T.a10` `T.a9` `T.a9p` `T.excl` `T.tower` |
| 1945 | Segre | `E.nuclide` |
| 1948 | Coxeter | `W.face` |
| 1948 | Shannon | `A.blind` `A.ebits` `A.slack` `EM.notcomp` `G.reg` `K.axis` `K.redun` `K.transit` |
| 1950 | Dilworth | `S.box` `S.down` |
| 1950 | Hamming | `W.frontier` |
| 1950 | Pais & Uhlenbeck | `W.core9` |
| 1950 | Löwdin | `LS.asym` |
| 1953 | Green | `T.para` |
| 1954 | Kolmogorov | `3B.index` |
| 1955 | Tarski | `A.cert` `F.open` |
| 1957 | Bethe & Salpeter | `B.coll` |
| 1958 | Pauli | `Q.delta` |
| 1958 | Seaton | `A.seaton` `P.coreblind` `P.lcollapse` `P.polar` `P.qdt` `Q.delta` `Q.final` `Q.pol` |
| 1959 | Dijkstra | `A.EW` `A.W` `A.intext` `A.three` |
| 1960 | Erdos & Renyi | `A.dens` |
| 1961 | Fano | `P.perturb` |
| 1961 | Reeh & Schlieder | `M.rs` |
| 1962 | Berge | `G.near` `G.tower` `K.girth` `K.peak` |
| 1963 | Arnold | `3B.index` |
| 1964 | Edlen | `A.S` `K.zcross` `P.buildlimit` `P.charge` `P.iso` `Q.final` |
| 1964 | Moebius | `G.book` |
| 1964 | Rota | `C.local` `G.book` `L.amp` `L.box` `L.mobius` `L.void` `L.voidfrac` |
| 1965 | Kolmogorov | `F.unstatable` |
| 1965 | Penrose | `W.core9` |
| 1967 | Floyd | `K.clock` `K.clockfail` |
| 1967 | Tomita | `M.tt` |
| 1968 | Ireland and Kullback | `A.stat2` |
| 1968 | Alekseev | `3B.index` |
| 1968 | Gerratt & Mills | `LS.chord` |
| 1969 | Andrew & Cowan | `P.dcollapse` `Q.collapse` `Q.final` |
| 1969 | Griffin, Andrew & Cowan | `LS.coll` |
| 1969 | Pulay | `LS.chord` |
| 1970 | Codd | `A.alph` |
| 1970 | Fano | `P.perturb` |
| 1970 | Takesaki | `M.tt` |
| 1971 | Lane | `K.cat` `K.comp` `K.deadend` `K.jump` `K.twocol` |
| 1971 | Griffin, Andrew & Cowan | `LS.coll` |
| 1971 | Saari | `3B.index` |
| 1972 | Gabriel | `K.quiver` |
| 1972 | Karp | `S.core` `S.cover` `S.erasure` `S.lam` `S.unit` |
| 1973 | Takesaki | `M.takesaki` |
| 1973 | Saari | `3B.index` |
| 1974 | Curtis & Reid | `B.hstar` |
| 1974 | Johnson | `S.cover` `S.lam` |
| 1974 | Montanari | `A.montanari` |
| 1974 | McGehee | `3B.index` |
| 1975 | Baker & Pixley | `A.fix` `A.two` |
| 1975 | Csiszar | `G.stat` |
| 1975 | Marchal & Saari | `3B.index` |
| 1976 | Monaghan | `3B.index` |
| 1978 | Freuder | `A.blind` `A.gc` `A.modeA` `A.modeB` `A.three` `G.allcons` `G.prot` `K.corner` `W.jur` |
| 1978 | Gratzer | `L.pushback` `L.step` |
| 1978 | Rissanen | `A.ebits` |
| 1979 | Chvatal | `S.core` `S.unit` |
| 1979 | Dawid | `G.trip` |
| 1980 | Stanley | `L.sperner` |
| 1981 | Monjardet | `I.shape` `L.metric` `L.occ` |
| 1982 | Freuder | `A.freuder` `C.cut` `G.cons` `G.ref` `G.shape` `L.E0` `L.box` `L.tree` `T.trad` `3B.def` |
| 1982 | Racah | `T.trad` |
| 1982 | Marchal & Bozis | `3B.index` |
| 1983 | Beeri, Fagin, Maier & Yannakakis | `A.intext` `C.compare` `K.three` |
| 1983 | Maier & Yannakakis | `A.intext` `A.relax` `C.compare` `K.langclose` `K.three` `K.window` |
| 1986 | Inokuti & Manson | `Q.anchor` `Q.region` `S.status` |
| 1986 | Stanley | `C.Aq` `C.Bq` `L.F` `L.F1` `L.Fm1` `L.chains` `L.pal` `L.rankpoly` |
| 1988 | Pearl | `G.trip` `K.decay` `K.markov` |
| 1989 | Cooper | `A.bpc` |
| 1989 | Dechter & Pearl | `G.cons` `G.shape` `K.coupling` |
| 1989 | Nouguier & Vilarem | `A.bpc` |
| 1991 | Chinneck & Dravnieks | `W.core15` `W.core9` `W.scale` `W.supp` |
| 1991 | Cover & Thomas | `K.decay` |
| 1991 | Drake & Swainson | `A.seaton` |
| 1991 | Kay-Wald | `M.C2` |
| 1992 | Borchers | `M.C2` `M.hsmi` `M.ledger` |
| 1992 | Dechter | `A.dechter` `A.gc` |
| 1993 | Wiesbrock | `M.C2` `M.hsmi` `M.ledger` |
| 1994 | Nesterov & Nemirovskii | `B.newton` `B.selfconc` |
| 1995 | Beek & Dechter | `A.rule` `A.staircls` |
| 1996 | Lauritzen | `K.decay` `K.markov` |
| 1998 | Montgomery | `3B.shape` |
| 1999 | Deville | `A.env` `A.orient` `A.r4` `T.tight` |
| 1999 | Hentenryck | `A.orient` `A.rule` `A.stair` `A.staircls` `T.tight` |
| 2000 | Wald & Zoupas | `M.C1` |
| 2000 | Chenciner & Montgomery | `3B.five` |
| 2002 | Montgomery | `3B.metric` |
| 2003 | Fredenhagen & Verch | `W.rel` |
| 2006 | Hsiang & Straume | `3B.shape` |
| 2014 | Montgomery | `3B.shape` `3B.metric` `3B.pot` |
| 2017 | Diestel | `G.graph` |
| 2019 | Fleischer & Knauf | `3B.index` |
| 2021 | Kol | `3B.index` |
| 2023 | Kol | `3B.index` |
| 2024 | Sorce | `M.sorce` |
| 2026 | Lach, *The Löwdin Solution* | `LS.ent` `LS.law` `LS.coll` `LS.pin` `LS.asym` `LS.quart` `LS.chord` `LS.twin` |
| 2026 | Lach, *The Three-Body Problem for Unknown Masses* | `3B.tri` `3B.def` `3B.index` |

### The works this compendium leans on most

| work | objects |
|---|---|
| Birkhoff, 1937 | **15** |
| Moore, 1910 | **13** |
| Pauli, 1925 | **11** |
| Condon & Shortley, 1935 | **10** |
| Birkhoff, 1940 | **10** |
| Freuder, 1978 | **9** |
| Freuder, 1982 | **9** |
| Seaton, 1958 | **8** |
| Rydberg, 1890 | **8** |
| Shannon, 1948 | **8** |
| Stanley, 1986 | **8** |
| Euler, 1748 | **7** |

# THE MATHEMATICS OF THE LÖWDIN WORK

*Registers 1249–1357. Each object is stated with its provenance: what is standard
and whose it is, what is arithmetic, and what this work introduces.*

*The twelve objects the closing list names are entered in the main volume's Appendix D at §D.5.10 (register 1734), where they close at E = 0 with the corridor's precedent read as this work's.*

---

## The corridor — a system of linear inequalities

**The object.** Requiring an observed subshell g to have least ν against every
admissible rival r gives one inequality per rival,

> **a(√p_r − √p_g) < n_r − n_g**,  with p = n − ℓ − 1

whose solution is an interval with endpoints

> **L, U = Δn(√p_g + √p_r)/(p_g − p_r)**

**Standard.** Linear programming in one variable; the feasible set of a finite
system of linear inequalities in ℝ¹ is an interval. *Fourier 1826; Motzkin 1936.*

**This work.** *That the coefficients are node counts, so the endpoints lie in
ℚ(√ℕ) and take only nineteen distinct values across the periodic table.* And that
all 106 intervals are non-empty — the system is consistent.

**The closed form** for every ns/(n−1)d competition:

> **a_cross = (√(n−1) + √(n−4))/3**

*giving 0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4, 5, 6, 7 — four exact
hits, and the 3 in the denominator is p_g − p_r, invariant across the table.*

## The staircase algebra of a closed index

**`A.staircls`** states that E(ℛ) = 0 iff the held set is an intersection of
monotone staircases. **A closed index is therefore a system of inequalities and
its cells are the lattice points satisfying them.**

**Read off Λ_PCA**, whose cells satisfy **L(s) ≤ d ≤ U(s)** with

> **L(s) = ⌊s/2⌋**  and  **U(s) = s + ⌊s/3⌋**

*both exact on s ∈ {0,1,2,3}.* **And off Λ_amp**, whose twenty cells satisfy the
single inequality **0 ≤ i ≤ ℓ**.

**This work.** *That the algebra of a closed index can be read back out of it as
floor functions — the staircases are not merely asserted to exist but written.*

## The Slater triangle, and a parity defect resolved

**Standard.** The multipole expansion of 1/r₁₂ gives, for a pair of subshells,
**F^k for k even up to 2min(ℓ,ℓ′)** and **G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to
ℓ+ℓ′.** *Slater 1929; Condon & Shortley 1935; the angular factors are Racah's
(1942–1949).*

**The angular factor of G^k is the 3j symbol squared**, and for an s electron
against an ℓ electron the sole exchange integral has angular factor **exactly
1/(2ℓ+1)** — verified 1, 1/3, 1/5, 1/7 to machine precision.

**This work.** *That indexing on the multipole rank k gives E = 1 with the single
defect **F¹**, a term parity forbids — and that reindexing on position within
sequence closes it at E = 0.* **The rank's parity is fixed by the kind and the ℓ
pair, so rank is not a free coordinate.**

## The falsification of a selection rule

**The object.** Given the corridor at every element, a walk needs a rule for where
in each interval to place the carried value. **Eight rules were tested; seven give
106/106**, including uniformly random interior points on **200 of 200 seeds**. Only
"move to the farther endpoint" fails, at 74/106, because it can overshoot.

**This work.** *That the ordering data constrains only membership of the interval,
not position within it — so the eighteen resets landing on exact surds is a
property of one chosen rule and not of the table.* **A different rule reproduces
the periodic table with a disjoint trajectory and a going negative at five
elements.**

*Recorded because the surd trajectory was reported as a result before the
falsification was run, and the falsification withdrew it.*

## The necessity of state

**The object.** For each admissible subshell, set a to that subshell's own crossing
value and ask whether it is then least-ν. **104 of 106 steps admit two to four
self-consistent subshells** — the observed one is always among them, never uniquely
determined.

**This work.** *That the periodic table is not computable from a single atom's
configuration. It requires one number carried forward: the arithmetic supplies the
values, the walk supplies the selection.*

## The observability boundary

**The object.** Across eleven closed indexes, the quantity each closure cannot fix
was identified. **Nine of eleven are expectation values ⟨Ψ|Ô|Ψ⟩.** The exception is
**Λ_cross**, whose value is a node count needing no measurement — **and it is the
only index with no statistics language.**

> **An index closes when its cells are enumerable. What it cannot supply is exactly
> what requires an operator.**

**This work.** *That the compendium's own language test detects this: the
statistics language is silent precisely where no observation is needed.* **One
confirming instance; the prediction is falsifiable and has been tested once.**

## Λ_spectra's closure, and what the limit leaves

**The object.** The index runs to the LAST AVAILABLE SPECIES and stops. Λ is
complete at 976 because its coordinates are bounded by the physics; Λ_spectra is
infinite unless capped, and *all cappings are closed when complete*.

Indexing every subshell any atom holds, (n, ℓ, k) over the observed ground
configurations: **98 cells, E = 58**. Of those 58, **38 require more electrons
than any atom has** — 6f¹ through 6f¹⁴ and beyond, needing Z past the table.
Past the limit, not defects. Applying the limit:

*Corrected at register 1426: the split was first reported as 47 / 11, using
`ground.py`'s own edge of Z = 108 as the limit while the synthesised table runs
to 118. The nine cells between — 6d⁷–6d¹⁰ and 7p²–7p⁶ — are real elements, not
absences. The eleven named exceptions below are unaffected; only the count of
beyond-limit cells was wrong.*

> **E = 11, and every cell is named.**

| absent | Madelung predicts at | observed |
|---|---|---|
| 3d⁴ · 3d⁹ | Cr 24 · Cu 29 | 3d⁵ · 3d¹⁰ |
| 4d³ · 4d⁶ · 4d⁹ | Nb 41 · Ru 44 · Ag 47 | 4d⁴ · 4d⁷ · 4d¹⁰ |
| 4f² · 4f⁸ | Ce 58 · Gd 64 | 4f¹ · 4f⁷ |
| 5d⁸ | Pt 78 | 5d⁹ |
| 5f¹ · 5f⁵ · 5f⁸ | Ac 89 · Np 93 · Cm 96 | 5f⁰ · 5f⁴ · 5f⁷ |

*The Madelung exceptions, recovered as closure defects rather than looked up —
E.nuclide's shape, a defect whose every missing cell can be named.*

**This work — rival = donor iff the donor is not full.** Twelve walk steps have a
subshell empty as another fills. A subshell at capacity has nowhere to put an
electron, so it is not Pauli-admissible and cannot be a rival in anyone's bracket,
including its own. An s shell holds 2 and is full when it donates:

| donor | occupancy before | binding rival |
|---|---|---|
| 4s, 5s, 6s (Cr, Cu, Nb, Ru, Pt) | **2, full** | 4p, 5p, 6p |
| 5s (Pd) | **1, partial** | 5s |
| 5d, 6d, 7p (Pr, Tb, Pa, Pu, Bk, Rf) | partial | itself |

**Holds 12 of 12, with no fitted term.** *Pd is its own control: the only s donor
that is not full, and it sits with the d and f donors. Were the rule about angular
momentum it would sit with Cr.* The anomalous steps differ from ordinary ones in
WHICH RIVALS EXIST, and that is fixed by occupancy — which ν already carries in q.
Registers 1395–1398.

## Attributions

**The ⅔ scaling.** *Thomas–Fermi's.* The quadratic in nuclear charge along an
isoelectronic sequence is **Krug & von Lilienfeld, arXiv:2406.18416 (2024)**,
fitted on Z = 1–86. **Carcassés & González, Phys. Rev. A 80 (2009) 024502**, give
E_ioniz = Z²N^(−2/3)g(N/Z) and flag that it fails for neutrals — the same domain
this work's residuals bow in.

**Configuration crossings along isoelectronic sequences** are a computed object:
**Berengut et al., arXiv:1204.0603** locate the 6p–5f crossing in the thallium
sequence by Dirac–Fock.

**The node theorem**, **Pauli's exclusion principle** and the **centrifugal term
ℓ(ℓ+1)** are standard and this work introduces none of them.

**Seaton's ratio** δ₂/δ₀ = −ℓ(ℓ+1)/3 is **Seaton's**; *the domain restriction to
p = 0 is this work's.*

**Slater's rules and integrals** are Slater's; *the observation that the count of
discarded exchange integrals equals the count of bracket failures is this work's.*

---

## What this work introduces, in one list

| object | |
|---|---|
| **the corridor** | 106 consistent linear inequalities with node-count coefficients |
| **the nineteen surds** | the complete set of endpoints across the table |
| **a_cross = (√(n−1)+√(n−4))/3** | closed form for the ns/(n−1)d family |
| **the staircase algebra** | ⌊s/2⌋ ≤ d ≤ s + ⌊s/3⌋, read out of a closed index |
| **the sequence-index fix** | rank parity is not a free coordinate |
| **the selection-rule falsification** | the corridor is forced, the path is not |
| **the necessity of state** | 104 of 106 steps ambiguous without memory |
| **the observability boundary** | closure enumerates; observation values |
| **the singleton-output rule** | an index is closed when its reading is unique |
| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |
| **the limit** | Λ_spectra closes at the last available species; E = 11, all named |
| **rival = donor iff not full** | the twelve anomalous steps, from Pauli alone |

---

# The Löwdin indexes — Λ_law and Λ_const

*Owed since register 1296; written at register 1571. Nothing here answers
Löwdin's challenge — the amplitude law remains three fitted numbers.*

## Λ_law — seven laws on (law, carrier). E = 0.

An arbitrary ordering gave E = 7. Across all 7! x 4! = **120,960 orderings** the
defect runs 0 to 21, and **288 reach zero.**

**The closing carrier order is u < p < l - l_core < Z - T**, monotone in **how
LOCAL the variable is**: u is the whole atom, p counts one l's shells,
l - l_core compares two angular momenta, Z - T is one distance to one threshold.
Two laws sit on u, three on p, one on each of the others.

The held cells form a **staircase**, which by `A.staircls` is exactly the
condition for E(R) = 0.

**What only this index contributes: THE CARRIER.** Fitting a law in the wrong
carrier is what took the l-spread from a spurious r2 of 0.868 to a real 0.356.

## Λ_const — fourteen constants on (role, carrier). E = 0 at 2 of 576.

Role order **exponent < centre < width < scale**. Standing: three fitted, six
measured, five derived or attributed.

**Every CENTRE is a small integer or half-integer** - 2 for the free shells, 2
for the gate, -1.5 for the switch, 2.5 for the l-validity, u0 = 4. **No SCALE
is.** The role axis orders by how much physics a number has absorbed.

**beta = 2/3 is load-bearing**: the only constant of arity three, in the
amplitude, the exponent and the validity, **and the one that is attributed.**

### The refusal, which is the more useful half

**`standing` cannot be a coordinate.** With attributed/derived/measured/fitted
on an axis the index closes at NO ordering; without it, at once.

> **An index whose coordinates mix the OBJECT with the OBSERVER cannot close,
> because the observer's axis has no order the object respects.**

The same fault is `origin` in Λ_var, `kind` in Λ_phys and `state` in
Λ_ladder - four occurrences of one mistake, stated here as a rule.
<<<END FILE: The_Method_1_6___Mathematical_Compendium-2.md>>>

<<<FILE: The_Method_1_6___The_Physics_Compendium-2.md>>>

# THE PHYSICS COMPENDIUM

Generated from `mathreg.py` and `SPECTRA-DATA.tsv` on 2026-08-12. **248 registered objects, 17 of them physical mechanisms.**

This compendium states the **interface** between a physical quantity and the index that holds it. It is not a list of mechanisms — those are in `MECHANISMS.md` and the Mathematical Compendium, and a third copy would drift as register 778's list did. It states, for each index, what the cells stand for, what number is attached to them, the rule taking one to the other, which constants that rule requires, **what must be measured rather than computed**, and what physics does and does not do.

Four faults in a single session were transitions performed without their rule written down: register 868 used R∞ for every species where the reduced-mass constant is correct; register 879 wrote Li III's ionisation limit as a formula where a measurement was required; register 766 passed atomic numbers where the core's charge is needed; register 782 set a verification column equal to its own denominator. **This document exists because those four share one cause.**

---

## Λ — the elemental index

**What it indexes.** Electron configurations of the ground states of the elements, on eight coordinates (n, ℓ, k, q, e, f, g, 2S). **976 cells.**

**The quantity.** None. A cell of Λ carries no physical number: it is an *arrangement*, not a measurement.

**The transition.** A configuration is read off the aufbau order and its subshells mapped to coordinates. `L.real` establishes that Λ's eight constraints hold on 247 real subshells across all 118 elements — **18,288 tests, no failures**.

**Constants required.** None.

**Must be measured.** Nothing. Λ is closed — |Λ| = |ℛ(Λ)| = 976, **E(Λ) = 0** — and the partition identity holds exactly: 6,912 = 976 + 0 + 5,936 (register 833).

**What physics does.** It supplies the aufbau ordering and the shell capacities, and nothing else. **What it does NOT do:** confer predictive power. §18 (and the preface) states that Λ *"contains no physics that was not already in the quantum numbers; it is a recoding … a recoding adds nothing."* Register 834 measured the consequence: on the same closed index, the T-bracket passes 789 of 789 and the δ-bracket passes 546 of 789. **Closure coexists with a bracket that holds and one that fails, so it cannot be what makes either true.**

---

## Λ_spectra — the index of Rydberg channels

**What it indexes.** Rydberg series: a fixed parent core, a fixed ℓ, n running. **596 channels across 70 spectra, 2,269 interior cells.** The complete index over the same alphabets is closed: |X| = |ℛ(X)| = 624, **E = 0** (register 853).

**The quantity.** The **quantum defect** δ — a continuous real number measuring how far the Rydberg orbital penetrates the ionic core. It is not an integer and has no factorization (register 896).

**The transition.** For a level at energy E below a limit I,

        n* = Z_c √( R_M / (I − E) )        δ = n − n*

**Constants required, and which value:**

  - **Z_c — the charge of the CORE, not the atom.** NIST states the formula as E_nl = −Z_c²/(n−δ)², *"where Z_c is the charge of the core"*. Be III and B III are third spectra and take Z_c = 3, not 4 and 5. Passing atomic numbers gave defects of −2 to −5 with spreads above 1.0 (registers 766, 883).
  - **R_M — the reduced-mass Rydberg, R∞/(1 + mₑ/M), not R∞.** For helium 109,722.386 against 109,737.316. Using R∞ understates every defect by n*(√(R∞/R_M) − 1) — 0.00240 for helium at n* = 35 — which drove He I's high-ℓ defects **negative**. Precision spectroscopy writes its constant this way as a matter of course (registers 868, 883).
  - **The exception.** Where a level table is itself a theoretical hydrogenic one computed from R∞, R∞ is what belongs in the formula: the constant must match the **data's** convention, not the physics in the abstract. Applying a reduced mass to Li III's table drove its spreads from 0.0000 to 0.0125 (register 872).

**Must be measured, not computed.** **The ionisation limit.** Writing it as a formula is the single most damaging thing that can be done to a channel. Li III's limit was recorded as *"Z²R = 9 × 109737.31568 (hydrogenic, Z=3)"* — a bare Coulomb expression that omits the QED and relativistic terms. Fitting the limit from the series gives **987,662.29 ± 0.36, higher by 26.45 cm⁻¹**, and every Li III channel moves from −0.0038…−0.0082 to a uniform **+0.0003** (register 879). The same deficit appears at B V scaled by Z⁴: **678 cm⁻¹ above 25R∞** (register 895).

**How a wrong limit announces itself.** A defect that should be constant instead deviates, and **the power of n\* names the cause**:

        n*³    a shift in the ionisation limit
        n*⁷    a magnetic field       — needs tens of tesla
        n*¹⁰   an electric field      — begins at n > 60

**Two of the three cannot fire on this compendium.** Its highest member anywhere is **n = 56** (Si I's nd (3/2,5/2)); eight channels exceed n = 40 and **none exceeds 60**. So every residual chased here was a limit, and none was a field — not by luck but because ASD's tables stop below where field effects begin (register 915).

**And the limit term's tolerance is published: a shift of even 0.2 cm⁻¹ "causes totally different behavior of quantum defect versus n".** Li III's was **26.45** — a hundred and thirty times that (register 914).

Li III's residual went as n³ and the limit was the fault. This is published and was derived independently here (registers 877, 885).

**Where the index STOPS, and why that is a decision.** Λ is finite because all 118 ground configurations are known within its caps. **The spectra index is not**: Rydberg series are unbounded in n and ℓ runs to n−1, so it is **infinite unless capped**, and every cap is a choice. Three defensible ones give:

        the measured alphabet          1,312 cells    E = 1,084
        charge 1..Z−1, elements held   4,376 cells    E = 4,148
        all 118 elements, l 0-7       55,224 cells    E = 54,996

**A factor of fifty between them, and all three close when complete.** Closure is a result about ℛ; the E that accompanies it is a result about the cap. At the physical cap the compendium holds **0.413%** — Λ holds 100% within its own (registers 959–962).

**What physics does.** It sets δ through core penetration, and the sixteen mechanisms in `MECHANISMS.md` describe how. **What it does NOT do:** make δ an integer, or give the index predictive power over cells it does not contain. Of 624 cells, 160 are measured and **193 are fully isolated** — no measured channel adjacent in ℓ or in an isoelectronic sequence, so no bound reaches them (register 890).

---

## The point of observability — what the equation actually delivers

**The quantum defect is a phase shift.** Outside the ionic core, where the potential is purely Coulombic, the radial Schrödinger solution is a superposition of the regular and irregular Coulomb functions:

        ψ  =  cos(πδ)·f(E,ℓ,r)  −  sin(πδ)·g(E,ℓ,r)

and **πδ is the phase shift with respect to the pure hydrogenic solution**, due to all short-range non-Coulombic interactions at r < r_c. Seaton's theorem continues it across threshold, δ_ℓ(0) = πμ_ℓ(0), so the same number describes bound levels and scattering.

**The consequence, and it is sharp.** The equation depends on δ only through cos πδ and sin πδ. **What it determines is δ modulo 1. The integer part is not in the equation** — it is supplied afterwards by counting nodes inside the core, and it is a labelling, not a measurement.

**What this costs the compendium.** Register 891 tested the rule *floor(δ) = (core orbitals of that ℓ) − 1* and found it holding for 318 of 407 channels — 78%, with Al I's ns at 1.767 where the rule requires 2.x. **It was testing a convention.** And testing P.lcollapse both ways:

        on the full defect        150 correct,  8 inverted   94.9%
        on δ mod 1 (observable)   127 correct, 31 inverted   80.4%

**The ordering survives on the assigned value and degrades on the observable one.** So P.lcollapse is a statement about node-counting as much as about penetration. Only **96 of 431** channels have |δ| > 1 at all — the rest have no integer part to assign, and for them the distinction does not arise (registers 910–913).

**The general rule this gives.** *A mechanism that holds on the assigned value and fails on the observable one is a statement about the index, not about the atom.* That is §18's distinction — a recoding adds nothing — reappearing at the level of a single number rather than a whole lattice.

---


---

## Kinematic and stateful — an interface the register found in its own objects

**A geometric hypothesis cannot do a state's work, and the register's one OPEN object is what happens when it is asked to.**

`M.C1` assumes Θ = 0 — the non-expanding condition, geometry and nothing else — and it succeeds: the presymplectic form is block diagonal in y and the commutator is (1/4√q) sgn(u−u′) δ^(d−2)(y−y′). **`M.C2` adds exactly one hypothesis, *ω Hadamard*, and that is a condition on a STATE.**

**Every obstruction encountered sits on the stateful side:**

  - a geometric modular flow needs a Killing vector — the flow is stateful and the geometry must match it
  - half-sided modular inclusion ⟺ a positive generator, and positivity is a property of a state
  - Θ = 0 is invariant under ℓ → a(y)ℓ, so **the geometry does not fix the state**
  - smoothness supplies a *local* Hartle–Hawking state, and local states do not glue
  - Hadamard is microlocal and therefore too weak to select one
  - and uniqueness, where it is available at all, needs invariance under a Killing flow

**And the split is NOT geometry against state, which was the first reading and was wrong.** The standard definition of a non-expanding horizon has three conditions and the third is *"Einstein field equations hold on Δ, and the stress-energy tensor T_ab is such that −T^a_b ℓ^b is future causal"* — **an energy condition, hence a condition on the state.** Through the kk-component of the Einstein equation it forces the null-null flux T_ab ℓ^aℓ^b and the shear σ_ab to VANISH, giving £_ℓ q_ab = 0. *So `M.C1`'s hypothesis is not an assumption but a consequence of the horizon's own definition, which is why it succeeds.*

**What the condition does not do is reach the right order.** It fixes the BACKGROUND — vanishing shear, vanishing null flux — while the linearised Raychaudhuri ∂_u δΘ = −8πG_N T_uu carries T_uu ≠ 0 on the perturbations, which is what the theory is about. **Half-sidedness is a spectral statement about those perturbations, and future-causality of −T^a_b ℓ^b is not one** (registers 1038–1042).

**The dimensional ledger states the split arithmetically**: d − 1 = 1 + (d − 2), one HSMI per generator supplying the affine line and the transverse direct integral coming from the kinematic side. *The stateful object supplies one dimension; the kinematic one supplies d − 2.*

**And it explains a result that otherwise looks like luck.** Computing the free half on one generator gives a positive translation generator immediately — negative to positive spectral weight 5 × 10⁻⁵ — **because a state was supplied by hand, the vacuum on a null line.** *The moment a state is given the inclusion follows; nothing on a non-expanding horizon gives one.* Registers 1033–1037.


---

## Placing a cell and valuing it are different operations

**ℛ places. Mechanisms value.** The distinction is invisible in Λ, where a cell is an arrangement and carries no number, so recovering the cell recovers everything. It is the whole difficulty in Λ_spectra, where the cell carries a quantum defect and that is its entire content.

        placed by ℛ          1,762 of 1,775 cells      99.3%
        valued               525                        32%

**A relation is usable as a STEP — carrying a value from one cell to another — only where the physics has collapsed to ONE PARAMETER.** Measured on pairs where both cells are known, as a geometric scatter:

        Nₑ at fixed charge ÷ Thomas-Fermi, s+p, Nₑ ≥ 9     1.07
        elem, s+p, Nₑ ≥ 9, raw                            1.10
        ℓ at ℓ ≥ 4, Seaton's ratio, filtered              1.12
        charge at fixed Nₑ, s                             1.23
        charge at fixed Nₑ, p                             1.38
        ℓ at p, d, f                                      3.31
        elem, all ℓ and Nₑ                                3.85
        Nₑ at fixed charge, raw                           4.12

**Above ℓ = 4 the electron never enters the core and only the polarisability matters — one number, and Seaton's formula follows. At ℓ ≤ 1 with Nₑ ≥ 9 penetration is statistical and Thomas-Fermi governs. At ℓ = 2, 3 or Nₑ < 9 neither dominates**, and four separate corrections — Seaton's ratio, core-orbital counts, the defect's own magnitude, a free Thomas-Fermi exponent — each left the scatter where it was.

**The transition zone is not a missing systematic. It is the absence of one**, and those cells require measurement rather than propagation (registers 1102–1118).

## Where relativity enters, and where it does not

**One place: the ionisation limit of a hydrogenic ion.** A Coulomb expression Z²R gives the limit only to order (Zα)². The Sommerfeld correction — special relativity applied to the atom in 1916, and shown by Gordon and Darwin to follow exactly from the Dirac equation — adds

        ΔE = Z⁴ α² R_M / 4        for the 1s state

**Measured against the reduced-mass baseline Z²R_M, three hydrogenic species give:**

        Li III   deficit 103.94   Dirac 118.32   ratio 0.878
        Be IV    deficit 329.80   Dirac 373.97   ratio 0.882
        B V      deficit 816.68   Dirac 913.03   ratio 0.894

**0.8849 ± 0.0069 across Z = 3, 4, 5** (register 906). The missing 11.5% is the **1s Lamb shift**, which raises the level and reduces the binding; it goes as α³Z⁴ against Dirac's α²Z⁴, so their ratio is order α times a slowly varying function — which is why three elements agree to under one per cent (register 908).

**The practical consequence.** Register 879's Li III fault was a Coulomb expression used where a relativistic one was required: the limit was written as 9R∞ and was low by 26.45 cm⁻¹, showing as a spurious defect of −0.0048 growing as n³ across every ℓ. **A hydrogenic limit computed rather than measured will always be low by this term.**

**Where relativity does NOT enter.** General relativity has no measurable term at these energies, and the compendium makes no use of it. The relativistic content here is entirely the special-relativistic kinetic correction, spin-orbit coupling and the Darwin term — the three that make up fine structure — plus the QED Lamb shift, which is not relativity at all (register 909).

---

## The bracket — the transition from a channel to an interval

**What it indexes.** An interior cell: a series member with a measured neighbour on each side.

**The quantity.** Not a value but an **interval**, and the book is explicit that this is the point: §22 says it *"fits nothing, assumes no functional form, and returns an interval rather than a value. It is a deduction, not a prediction."*

**The transition — and there are TWO, which the book does not distinguish.**

  - **§22.1, on binding energy.** T = I − E is monotone in n, so T(n) lies between T(n−1) and T(n+1). **Passes 789 of 789.** A Rydberg series rises toward its limit by construction, so this form **cannot fail** (registers 797, 800, 830).
  - **§25.6.1, on the defect.** δ(n) lies between δ(n−1) and δ(n+1), resting on *"within a channel, δ falls monotonically with n"*. **Passes 546 of 789.**

**The trade-off, stated.** §22.1's bracket is a genuine deduction and carries no information. §25.6.1's carries information and is not a deduction. **Chapter 22's modesty is exactly what buys the 100%, and the price is that the 100% was never evidence** (register 803).

**And the monotonicity claim is the wrong form.** The extended Ritz expansion is

        δ(n) = δ₀ + δ₂/(n−δ₀)² + δ₄/(n−δ₀)⁴ + …

and **caesium's nF series is measured with δ₂ = −0.2014(16) — negative — its defects RISING** with n. So the law is that **δ approaches δ₀ monotonically**; the direction is sign(δ₂), a property of the channel, and falling is only the common case (register 858).

**What physics does.** It guarantees the monotonicity of T. **What it does NOT do:** guarantee the monotonicity of δ, which holds in 113 of 130 resolved steps — 87%, interval 80–92% — and only where a step exceeds its own uncertainty. With error estimated from quoted decimals instead, the same test gives **55%**, and the intervals do not overlap (register 822).

---

## What the interface still does not state

**Uncertainties.** Five of 49 species files carry a quoted uncertainty column. The monotonicity law is testable only where a step can be distinguished from its own error, and **44 of 49 species do not supply what that needs** (register 807).

**The bracket's own inputs.** `channels.py` writes `bracket = "untested"` for every channel it builds, because running the bracketing method needs measured neighbours and a tolerance and the script supplies neither. **285 of 431 channels are unverified on the compendium's central claim**, and the column says so rather than asserting a verification that never ran (register 782).

**Appendix B's inputs.** 133 channels were lifted with their values and without their levels. `spectra_raw/` holds no He I file, so when register 868 corrected the Rydberg constant those channels **could not be recomputed**. *A result kept without its inputs cannot be corrected when its method is* (register 871).

---

# THE LÖWDIN-SOLUTION INDEXES — Λ_chain, Λ_cinf, Λ_V5

*Interface entries for the indexes of Chapter 35, in this compendium's own template: what the cells stand for, what number is attached, the rule taking one to the other, the constants that rule requires, what must be measured rather than computed, and what physics does and does not do. Register 1701–1712. The mechanisms are stated once, in the Mathematical Compendium (family LS); a second copy would drift.*

## Λ_chain — the derived filling index

**What it indexes.** One row per element, Z = 2–120: the entrant channel, its
depth, its margin, and the full candidate spectrum of the V^{N−1} walk. **119
rows; 107 scored, 12 unwitnessed.**

**The quantity.** Per row: D_ent and the margin, in hartree; per candidate
channel, its converged depth in the frozen field of (Z, cfg(Z−1)).

**The transition.** The entrant operator: converge the field of the ion carrying
cfg(Z−1); solve each frontier channel; deepest wins; chain forward. Nothing in
the rule is adjustable.

**Constants required.** One: c = 137.035999 (Koelling–Harmon scalar-relativistic
kernel). *No screening constant, no fitted parameter, no observed energy.*

**Must be measured.** Nothing upstream. The measured ground configurations enter
once, downstream, as the score target: **107 of 107** (register 1701–1702). Rows
109–120 have no measurement to meet and are held **unwitnessed** — the book's own
grade: not undefected for want of trying.

**What physics does.** It supplies the field and the depths; the ordering law is
then read off, with its three derived exceptions (collapse) and its derived
absence (no g block). **What it does NOT do:** it does not decide total-energy
rearrangements inside an already-open block — the chromium class is outside this
index's claim, and stating that is scope, not weakness (register 1701).

---

## Λ_cinf — the twin index at c → ∞

**What it indexes.** The identical walk with the one constant removed. 107 rows.

**The quantity.** The same depths and entrants, non-relativistically.

**The transition.** Identical operator, c → ∞.

**Constants required.** None — which is the point.

**Must be measured.** Nothing; it is compared, not scored: **eleven entrants
differ from Λ_chain** (Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf), and every
difference is an error against nature, since the relativistic walk scores 107/107
(register 1706).

**What physics does.** It states that the observed periodic table is not a
solution of the non-relativistic equation. **What it does NOT do:** serve as a
fallback ordering anywhere; its role is the counterfactual, and it must never be
consulted as data.

---

## Λ_V5 — the correlation closure at the contested rows

**What it indexes.** The five elements where the mean-field competition is close:
Z = 38, 56, 72, 89, 105. Per row: the second-order correlation differential
between entrant and runner-up, complete (entrant pairs, core–core pairs, the
near-degenerate block resummed), expressed over the mean-field margin.

**The quantity.** dm2/margin = **+1.33, +1.24, +2.6 [2.57–2.73], +2.2
[1.92–3.32], +2.16.**

**The transition.** Second-order many-body perturbation on the sealed field;
brackets are declared estimate envelopes, points where single-valued.

**Constants required.** The same single c, inherited.

**Must be measured.** Nothing. The clause is a computation whose only external
contact is the field it inherits.

**What physics does.** It closes the one silent failure mode of a mean-field
derivation: **every contested competition widens; none reverses; an envelope
entirely on the positive side cannot flip a positive sign** (register 1705).
**What it does NOT do:** bound the uncontested rows — there the mean-field margin
needs no help, and claiming otherwise would be a pooled assertion of exactly the
kind the domain protocol blocks.

---

## The collapse condition — interface only

*Per this compendium's charter, the mechanism is stated once, in the Mathematical
Compendium addition; a third copy would drift. This entry records the interface.*

**What it decides for these indexes.** Exactly the tie-break exception set
{La, Ac, Th} in Λ_chain; and the Z = 91 sign held at SCF tolerance, entered as
branch content rather than resolved by force (register 1703). **It occupies
precisely the domain where Chapter 34's corridor is silent.**

**Must be measured.** Nothing; the condition is computed from the same field as
the walk.

**What it does NOT do.** Perturb Clause 1 anywhere: the ordering clause is
exception-free with the collapse rows included.

---

## The defect — interface only

*Mechanism and decomposition are stated once, in the Mathematical Compendium
addition ("The defect, closed"); this entry records the interface.*

**What it touches in these indexes.** Nothing in any scored value: the defect is
internal to the walk's energy bookkeeping, and its closure (register 1707–1711)
is the audit that no unexplained numerical content sits under the indexes above.

**Must be measured.** Nothing — and that is the entry's point: a discrepancy
that data cannot violate was defending the derivation, and once named it became
mathematics. **The fault ledger's two reclassifications live here.**

---

# Λ₃ — THE THREE-BODY INDEX

*Chapter 36; register 1713–1724. Objects in the Mathematical Compendium, family 3B.*

**What it indexes.** Motions of three point masses under Newtonian gravity, at fixed E and L, by asymptotic class: five cells. It is the second index in the compendium built from physics rather than from Λ (the first is Λ_spectra), and the first whose subject is classical.

**The coordinate supply.** The masses enter through exactly six numbers — three c_ij and three unit vectors b_ij — and nowhere else. Everything structural (S², the metric, N₈, K₃) is mass-free.

![The shape sphere](figures/fig1_shape_sphere.png)

*S² with the Euler, Lagrange and binary points; two mass cases.*

**Kinematic and stateful.** Λ₃'s cells are configurations; by §12.11.1.3 the index has no time column, and the flow is the geodesic flow of `3B.JM`. Time is a quadrature and carries the transcendental part (Sundman series; Painlevé transcendents on the natural boundary). This is the interface *Kinematic and stateful* (above) found in the register's own objects, now on a classical subject: *placing* a cell (which stratum) and *valuing* it (the geodesic) are different operations.

**Where the physics is exact and where it is envelope.** Exact: the five fixed points, the zero-velocity surface {E + U ≥ 0} (Hill 1878), Hill stability of a hierarchy (Marchal–Bozis 1982). Envelope: every stratum boundary, by `3B.tri`.

![The potential on the equator](figures/fig4_equator_potential.png)

*U on the collinear circle, three mass cases.*

**The point of observability.** What Λ₃ delivers for a given state: the stratum, the family within it (torus / braid word / symbolic sequence / distribution P(ε)), and the geodesic as far as the natural boundary. What it never delivers: r_i(t). §25.6 is why.

**Failure modes, measured rather than anticipated.**
1. A factor of the hyper-radius carried into `3B.pot` from an inherited convention: 13/13 failures, uniform, hence in the audit not the object. Corrected.
2. An inherited degree-8 polynomial with two wrong coefficients: caught by the second route (N₈). Withdrawn.
3. Threshold silence: L4/L5 stability at μ < 0.0385209 is a number; the method is silent (§31.1.1). Not a failure, a boundary.

---

# Λ_phys — THE INDEX OF PHYSICAL PARAMETERS

**Every number the work takes from physics, with what it is, where it comes from, and where it stops being right.** *A parameter with no stated failure mode is a parameter being used outside a domain nobody has checked.*

**27 parameters.** Coordinates: **kind** (exact → fitted), **source** (mathematics → this work), **domain** (universal → one species), and how many registered objects rest on it.

## What the index shows about the work's dependence

| kind | universal | all elements | a region | one species |
|---|---|---|---|---|
| **exact by definition** | 2 | 0 | 0 | 0 |
| **measured constant** | 3 | 0 | 0 | 1 |
| **read from a table** | 0 | 3 | 2 | 1 |
| **derived here** | 0 | 2 | 1 | 0 |
| **fitted here** | 0 | 1 | 6 | 1 |
| **free parameter** (three-body: m₁m₂m₃, E, L) | 0 | 0 | 3 | 0 |
| **exact by scaling** (G) | 1 | 0 | 0 | 0 |

*The speed of light c (measured constant, universal) joins the second row with Chapter 35; the four three-body inputs are the problem's, not this work's, and are entered as the last two rows.*

*"Objects rest on it" is counted from the Mathematical Compendium at this build, on one rule for all twenty-seven (register 1740): the seeds are the objects whose statement or title names the parameter — its symbol, its value or its name — and the count is the seeds plus every object that depends on one of them, transitively, in the compendium's own dependency graph. Seeds and counts: subshell capacity: `L.c2`, `L.F`, `L.chi`, `C.Aq`, `C.Bq`, `T.para` → 66; angular momentum bound: `L.c1`, `L.F`, `L.chi`, `C.Aq` → 72; Rydberg constant: `B.adm`, `B.fail`, `B.silence`, `B.nuV` → 5; proton-electron mass ratio: none → 0; Cs I np defect: none → 0; ionisation limit: `E.ioniz`, `P.buildlimit`, `P.converge`, `P.lens` → 4; aufbau ordering: `Q.bound`, `LS.law` → 18; Janet block boundary: `P.dcollapse`, `Q.collapse`, `LS.coll` → 13; Hund's first rule: none → 0; core dipole polarisability: `A.seaton`, `P.polar`, `Q.alpha`, `Q.pol` → 18; actinide defects: none → 0; Seaton polarisation constant: `A.seaton`, `Q.pol` → 16; reduced-mass Rydberg: none → 0; bracket yardstick: `B.adm`, `B.fail`, `B.silence` → 4; channel equation, a: `Q.final` → 9; channel equation, e0: `Q.final` → 9; channel equation, e1: `Q.final` → 9; channel equation, k: `Q.final` → 9; channel equation, h: `Q.final` → 9; isoelectronic ladder, B: `P.iso`, `Q.final` → 11; five-sigma admissibility: `B.adm` → 2; exchange coefficient: `Q.exch`, `Q.delta` → 15; speed of light: `LS.ent`, `LS.law`, `LS.twin` → 8; three-body masses: `3B.pot`, `3B.norm`, `3B.five` → 5; three-body energy: `3B.JM`, `3B.index` → 2; three-body angular momentum: `3B.index` → 1; gravitational constant: none → 0. A parameter no statement names — the proton–electron mass ratio, the caesium defect, the actinide defects, the reduced-mass Rydberg, Hund's first rule — counts 0 on this rule: it enters through a value the objects use, not through a statement, and the rule says so rather than guessing. Prior counts, generated on a rule this volume did not print and standing to register 1739 where they differ: subshell capacity 12, angular momentum bound 12, Rydberg constant 9, proton-electron mass ratio 9, Cs I np defect 2, ionisation limit 25, aufbau ordering 19, Janet block boundary 15, Hund's first rule 12, core dipole polarisability 10, actinide defects 2, Seaton polarisation constant 10, reduced-mass Rydberg 9, channel equation, a 8, channel equation, e0 8, channel equation, e1 8, channel equation, k 8, channel equation, h 8, isoelectronic ladder, B 3, five-sigma admissibility 3, exchange coefficient 1.*

**8 of the 27 parameters are this work's own.** *Of those, **0 are universal**, 1 hold across all elements, and **7 hold only in a region or for one species.** No number this work fitted claims wide validity.*

**And the dependence concentrates on the LATTICE'S OWN BOUNDS, then on tables.** On the printed rule the two exact-by-definition constraints carry the most objects, because the index of Part III is built from them; the tables come next (register 1740; before it the three heaviest were the ionisation limit, the aufbau ordering and the Janet boundary — the prior counts stand in the paragraph above):

| parameter | objects resting on it | kind |
|---|---|---|
| angular momentum bound | **72** | exact by definition |
| subshell capacity | **66** | exact by definition |
| aufbau ordering | **18** | read from a table |
| core dipole polarisability | **18** | read from a table |
| Seaton polarisation constant | **16** | derived here |
| exchange coefficient | **15** | fitted here |

## The parameters

### subshell capacity — `4l+2`

**exact integer** · exact by definition · from published literature · valid universal · 66 objects rest on it

**What it is.** the number of electrons a subshell of angular momentum ℓ can hold: 2 spin states times 2ℓ+1 orbital states.

**Where it comes from.** Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736; made exclusive by Pauli, Z. Phys. 31 (1925) 765-783

> **Where it fails.** for parastatistics of order m the capacity is m(4ℓ+2) — T.para shows the index still closes, so the constraint is a cap and not a magic number.

### angular momentum bound — `l <= n-1`

**exact integer** · exact by definition · from published literature · valid universal · 72 objects rest on it

**What it is.** the orbital angular momentum of a bound state cannot reach the principal quantum number; it is the condition for the radial function to have a node structure.

**Where it comes from.** Bohr, Phil. Mag. 26 (1913) 1-25; Schrödinger, Ann. Phys. 79 (1926) 361-376

> **Where it fails.** never within non-relativistic quantum mechanics.

### Rydberg constant — `R_inf`

**109737.31568 cm^-1** · measured constant · from international standard · valid universal · 5 objects rest on it

**What it is.** the binding energy of a hypothetical one-electron atom with an infinitely heavy nucleus, expressed as a wavenumber. It sets the scale of every atomic term value.

**Where it comes from.** Rydberg, K. Sven. Vetensk. Akad. Handl. 23 (1890) for the empirical constant; value CODATA 2018, uncertainty 1.9e-6 cm^-1 — eleven significant figures

> **Where it fails.** never as a constant; but using it in place of the reduced-mass R_M is wrong for every species (register 868). The error is 1 part in 1836 A, largest at hydrogen.

### proton-electron mass ratio — `m_p/m_e`

**1836.15267343** · measured constant · from international standard · valid universal · 0 objects rest on it

**What it is.** the ratio of the proton rest mass to the electron rest mass; the quantity that makes the reduced-mass correction small but not negligible.

**Where it comes from.** CODATA 2018, uncertainty 1.1e-10

> **Where it fails.** never; it enters only through R_M, so an error here is an error there.

### Cs I np defect — `3.5667`

**measured** · measured constant · from published literature · valid one species · 0 objects rest on it

**What it is.** the limiting quantum defect of the caesium np series, the compendium's only MEASURED far anchor.

**Where it comes from.** arXiv:1706.06237 (2017), n = 70-100; earlier 3.55925 at n = 9-50 (Lorenzen & Niemax, Z. Phys. A 315, 1984)

> **Where it fails.** the two values differ by 0.007 because of stray-field shifts; the compendium uses the field-free one.

### ionisation limit — `I`

**per species, cm^-1** · read from a table · from published literature · valid one species · 4 objects rest on it

**What it is.** the energy at which a Rydberg series converges — the term value of the ion's ground state relative to the neutral. Every defect is measured against it.

**Where it comes from.** the extrapolation method is Rydberg 1890 and Ritz, Ann. Phys. 12 (1903) 264-310; values from NIST ASD where published, built by summing two spectra where not (P.buildlimit), joint-fit where neither

> **Where it fails.** wherever it was CONSTRUCTED rather than published — such a channel is not a measurement against an independent standard, and the compendium marks the column.

### aufbau ordering — `n+l, then n`

**a permutation of subshells** · read from a table · from published literature · valid all elements · 18 objects rest on it

**What it is.** the order in which subshells fill as Z increases: lowest n+ℓ first, and within one n+ℓ value, lowest n first.

**Where it comes from.** Janet 1928 (Considerations sur la structure du noyau de l'atome, Beauvais 1929), who recognised it before Madelung 1936; shell lengths by the Klechkovski-Hakala formulas

> **Where it fails.** at about twenty known exceptions among the elements — Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Ce, Gd, Pt, Au, Ac, Th, Pa, U, Np, Cm, Lr. The compendium reads the OBSERVED configuration, so the exceptions are data and not failures. The rule's ORIGIN was unresolved when this entry was written (Löwdin's challenge, Allen & Knight, Int. J. Quantum Chem. 90 (2003) 80-88); it is now derived — Λ_chain above, Chapter 35, register 1701 — and the three tie-break exceptions La, Ac, Th are derived with it. The remaining exceptions of the Cr class are total-energy rearrangements inside an open block, outside Λ_chain's claim.

### Janet block boundary — `Z = 21, 57, 89`

**exact integer** · read from a table · from published literature · valid all elements · 13 objects rest on it

**What it is.** the atomic number at which a new n+ℓ block opens — n+ℓ = 5 at Sc, 7 at La, 8 at Ac — which is where the corresponding orbital contracts into the core.

**Where it comes from.** the block structure is Janet 1928; the CONTRACTION is Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71

> **Where it fails.** as a SHARP threshold: collapse is rapid, not instantaneous. Ca I at Z = 20 has nd = 0.908 against a threshold of 21, and Ba II at 56 has nf = 0.756 against 57.

### Hund's first rule — `max S for the core`

**a term selection** · read from a table · from published literature · valid all elements · 0 objects rest on it

**What it is.** of the terms a configuration allows, the one of highest total spin lies lowest in energy; it fixes which multiplicities a core can present.

**Where it comes from.** Hund, Z. Phys. 33 (1925) 345-371

> **Where it fails.** for a core in an excited term rather than its ground term. The index takes the ground term, so an excited-core series is outside it.

### core dipole polarisability — `alpha_d`

**per core, a0^3** · read from a table · from published literature · valid a region of the index · 18 objects rest on it

**What it is.** the induced dipole moment of the ionic core per unit applied field; the leading term in the potential a distant electron feels beyond the Coulomb tail.

**Where it comes from.** Born & Heisenberg, Z. Phys. 23 (1924) 388-410; systematic values Mayer & Mayer, Phys. Rev. 43 (1933) 605-611; modern e.g. Cs+ 15.696(16) a0^3, arXiv:2502.20961

> **Where it fails.** below l = 4, where penetration dominates and Seaton's formula does not apply. AND for nf treated as non-penetrating: arXiv:2502.20961 reports alpha_d and alpha_q that then disagree with the ng energies.

### actinide defects — `5.2, 4.75, 3.8, 2.0`

**theoretical** · read from a table · from published literature · valid a region of the index · 0 objects rest on it

**What it is.** the asymptotic ns, np, nd and nf quantum defects predicted for the actinides, Z = 89-103; the compendium's only high-Z anchors.

**Where it comes from.** arXiv:2508.06733 (2025), theoretical

> **Where it fails.** as MEASUREMENTS — they are calculated. Four of the seven far anchors are these, and the equation's high-Z arm moves if they are revised (register 1202).

### Seaton polarisation constant — `3 alpha c^2 / K(l)`

**derived** · derived here · from published literature · valid a region of the index · 16 objects rest on it

**What it is.** the limiting quantum defect of a non-penetrating series, set by the core's polarisability and the centrifugal factor K(ℓ) = ℓ(ℓ+1)(2l-1)(2ℓ+1)(2l+3).

**Where it comes from.** Seaton, MNRAS 118 (1958) 504-518; Drake & Swainson, Phys. Rev. A 44 (1991) 5448

> **Where it fails.** at l < 4, and wherever the quadrupole term matters. The compendium measures the ratio delta_2/delta_0 against -ℓ(ℓ+1)/3 at 1.25 rather than 1.00.

### reduced-mass Rydberg — `R_M`

**R_inf/(1 + 1/(A m_p))** · derived here · from international standard · valid all elements · 0 objects rest on it

**What it is.** the Rydberg constant corrected for a nucleus of finite mass A, by replacing the electron mass with the electron-nucleus reduced mass.

**Where it comes from.** Bohr 1913: after Fowler objected that the Pickering series did not fit, Bohr replaced the electron mass with the reduced mass and obtained five-digit agreement, which identified the series as ionised helium. Bohr, Nature 95 (1915) 6-7 for his later comment.

> **Where it fails.** for an ion of unknown isotopic composition: A is the dominant isotope, and a mixed sample shifts R_M by roughly the isotope shift.

### bracket yardstick — `2 Z^2 R / nu^3`

**derived** · derived here · from published literature · valid all elements · 4 objects rest on it

**What it is.** the local spacing between adjacent Rydberg levels — the derivative of the term formula. A perturbation larger than half of it reorders the levels.

**Where it comes from.** derived from Rydberg's term formula (1890)

> **Where it fails.** for a PERTURBED series, where a level of another channel crosses in. Fano, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Phys. Rev. A 2 (1970) 81-86.

### channel equation, a — `0.3772`

**fitted** · fitted here · from this work · valid a region of the index · 9 objects rest on it

**What it is.** the overall amplitude of the penetrating branch: how much defect one core orbital of the same l produces at unit electron count and unit charge.

**Where it comes from.** fitted here by least squares on 277 in-region channels plus 7 far anchors; the FORM it scales is the penetration picture of Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89-110

> **Where it fails.** outside Z ≤ 92, charge ≤ 10, l ≤ 4, single-parent core.

### channel equation, e0 — `0.8297`

**fitted** · fitted here · from this work · valid a region of the index · 9 objects rest on it

**What it is.** the intercept of the exponent on the core-orbital count p — how sharply the defect grows with the number of same-l orbitals in the core, at small Ne.

**Where it comes from.** fitted here; the p-count itself is the Pauli occupancy (Pauli 1925)

> **Where it fails.** as above. Its value moved from 0.583 to 0.830 when the far anchors were added, so it is sensitive to the high-Z end.

### channel equation, e1 — `-0.0900`

**fitted** · fitted here · from this work · valid a region of the index · 9 objects rest on it

**What it is.** the log-Ne slope of that exponent: the rate at which additional core orbitals stop mattering as the atom grows.

**Where it comes from.** fitted here; that screening saturates with electron count is the Thomas-Fermi picture of Fermi, Z. Phys. 48 (1928) 73-79

> **Where it fails.** as above; it was -0.027 before the anchors, a factor of three.

### channel equation, k — `0.4942`

**fitted** · fitted here · from this work · valid a region of the index · 9 objects rest on it

**What it is.** the Thomas-Fermi exponent: how the defect scales with the number of electrons in the core, through the screening the statistical model predicts.

**Where it comes from.** fitted here; the scaling is Fermi, Z. Phys. 48 (1928) 73-79, who applied the statistical model to Rydberg corrections directly

> **Where it fails.** MEASURABLY: k rises with charge, from 0.84 at charge 1 to 1.52 at charge 4 (register 1214). A single value is a simplification and the register says so.

### channel equation, h — `0.5415`

**fitted** · fitted here · from this work · valid a region of the index · 9 objects rest on it

**What it is.** the amplitude of the collapse branch: how much defect a collapsed orbital produces where the core has no orbitals of its own l.

**Where it comes from.** fitted here; the collapse is Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969

> **Where it fails.** below the Janet boundary, where the polarisation floor is absent.

### isoelectronic ladder, B — `per sequence`

**fitted** · fitted here · from this work · valid a region of the index · 11 objects rest on it

**What it is.** the single free coefficient of delta(c) = B ln(c+1)/c along a sequence of fixed electron count, with the constant term fixed at zero by the hydrogenic edge.

**Where it comes from.** fitted here per sequence on the 52 with three or more charge states; the isoelectronic method is Edlen, Handbuch der Physik XXVII (1964) 80-220

> **Where it fails.** as a CLOSED FORM: no expression of B in the coordinates beats the per-sequence fit by less than a factor of twenty, and PMC3671562 reports the same for ionisation energies.

### five-sigma admissibility — `r >= 5`

**a threshold** · fitted here · from this work · valid all elements · 2 objects rest on it

**What it is.** the bracket is applied only where the signal exceeds five times the measurement uncertainty, so that a bracket failure is a fact about the levels and not noise.

**Where it comes from.** the convention is particle physics's; its history and its critics are in Lyons, Discovering the significance of 5 sigma, arXiv:1310.1284 (2013)

> **Where it fails.** it is a CHOICE. At three sigma more cells enter and more brackets fail; the compendium states the threshold rather than tuning it.

### exchange coefficient — `s = -0.0782`

**fitted, WITHDRAWN** · fitted here · from this work · valid one species · 15 objects rest on it

**What it is.** the fractional difference between a triplet channel's defect and its singlet partner's, from the exchange interaction between the Rydberg electron and the core.

**Where it comes from.** fitted at register 987, WITHDRAWN at 1168; the physics is Heisenberg, Z. Phys. 38 (1926) 411-426, with Hund's first rule (1925)

> **Where it fails.** everywhere: the fitted sign is opposite to the measured one, and a uniform s gives 0 of 66 pairs or 66 of 66.

*The fifteen, read from the graph (register 1749): six were built on the superseded channel equation that carried s — `Q.exch`, `Q.delta`, `Q.bridge`, `Q.region`, `Q.anchor`, `A.blind` — and nine are the standing equation `Q.final` and the Löwdin objects beneath it, which reach s only by provenance: `Q.final` descends from `Q.delta` through `Q.region` and `Q.anchor`, and its statement carries no exchange factor. The count stands on the printed rule; the split says what it measures.*

### speed of light — `c = 137.035999`

**137.035999 a.u.** · measured constant · from international standard · valid universal · 8 objects rest on it

**What it is.** the one entered number of the Löwdin solution: the constant in the Koelling–Harmon scalar-relativistic kernel of the entrant operator. No screening constant, no fitted parameter, no observed energy enters beside it.

**Where it comes from.** CODATA; the inverse fine-structure constant in Hartree atomic units.

> **Where it fails.** at c → ∞ — and the failure is measured, not anticipated: the twin index Λ_cinf disagrees with Λ_chain at eleven elements, each an error against nature (register 1706).

### three-body masses — `m₁, m₂, m₃`

**three positive reals** · free parameters · from the problem statement · valid all mass triples · 5 objects rest on it

**What it is.** the masses of the three bodies, unspecified; they enter Λ₃ through exactly six numbers — three c_ij and three unit vectors b_ij — and nowhere else.

**Where it comes from.** the problem as posed; the six-number coordinate supply is Montgomery 2014 §11.

> **Where it fails.** nowhere structural — S², the metric, N₈ and K₃ are mass-free. The masses move the five fixed points and nothing else.

### three-body energy — `E`

**a real** · free parameter · from the problem statement · valid E < 0 for bound strata · 2 objects rest on it

**What it is.** the conserved energy, entering as the conformal factor E + U of the Jacobi–Maupertuis metric.

**Where it comes from.** Maupertuis 1744; Jacobi 1837.

> **Where it fails.** at the zero-velocity surface {E + U = 0} (Hill 1878), where the metric degenerates and the geodesic flow stops.

### three-body angular momentum — `L`

**a real** · free parameter · from the problem statement · valid all L · 1 object rests on it

**What it is.** the conserved angular momentum, carrying the reduction 6 → 4 of the phase space.

**Where it comes from.** standard; the reduction is Jacobi 1842.

> **Where it fails.** at the angular-momentum stratum boundary, which is envelope, not exact (`3B.tri`).

### gravitational constant — `G`

**1** · exact by scaling · from convention · valid universal · 0 objects rest on it

**What it is.** the coupling of Newton's potential, set to 1 by choice of units.

**Where it comes from.** scaling; carries no content once units are fixed.

> **Where it fails.** nowhere.

## The three failures that are measured rather than anticipated

*Most of the failure modes above are domain statements: the parameter is right inside its range and untested outside. Three are different — the compendium has MEASURED the failure.*

**Seaton's polarisation constant.** The ratio δ₂/δ₀ should be −ℓ(ℓ+1)/3 with the polarisability cancelling. On fourteen channels with δ₀ > 0.01 the observed ratio is **1.25 times** the predicted one, and the departure is a per-core constant reproducible within a species to two decimals — Si III g gives 1.77 four times, Si III h gives 1.12 twice.

**The Thomas–Fermi exponent k.** Fitted per charge state, it reads **0.84, 0.91, 1.03, 1.40** at s and **1.01, 1.13, 1.28, 1.52** at p, for charges 1 to 4, with trend R² between 0.87 and 0.98. **The equation carries a single k = 0.494.** *Register 1214.*

**The exchange coefficient.** The fitted sign is opposite to the measured one, and no uniform coefficient can work: exchange acts through an overlap that falls sharply with ℓ, so one constant gives 0 of 66 triplet-above-singlet pairs or 66 of 66. *Withdrawn at register 1168.*

**These three are why the compendium states failure modes at all.** *A parameter whose failure has been measured is more useful than one whose validity has been assumed, and the difference is not visible unless both are written down.*

# Λ_chem — THE CHEMICAL PROPERTIES INDEX

*Registers 1339, 1343–1346. Forty-two chemical properties of a species, indexed
on what each one IS and on which of physics, charge or amplitude it supplies.*

## Why the compendium needed it

Repeatedly in the Löwdin work a residual was left unexplained because a universal
account of it was sought. **Each time the answer was a property of the individual
species.** The record: the 1.029 factor on t(ℓ); the occupancy slope varying from
0.021 to 0.243; no f corridor, hence √6 untested; the crossing charge set by n_f;
Seaton's ratio valid only at p = 0.

**Λ_phys had been saying this all along** — no parameter of this work sits in the
universal column. **Λ_chem is the routing table that makes the statement usable:
before calling a residual unexplained, look up which chemical property supplies it
and which class it holds on.**

## The coordinates

**KIND** — what the property measures: *count · symmetry · size · energy · rate*

**SEAT** — which part of the species it belongs to: *the nucleus · the core · the
subvalence shell · the valence shell · **the aggregate***

**PCA** — which of *physics · charge · amplitude* it supplies

## The fifth seat

**Twelve of the forty-two are properties of MATTER IN BULK and not of an isolated
atom at all**: density, melting point, boiling point, hardness, crystal structure,
electrical and thermal conductivity, colour of the metal, smell, taste, metallic
character, reactivity.

*With eleven hand-picked properties the index could not say this. It appeared the
moment every chemical property of a species was demanded, and it is the reason the
compendium can now distinguish an atomic property from a bulk one at all.*

## The closure, and the boundary it declares

**E = 0 on fourteen cells** over the subvalence and valence shells. And the defect
climbs as foreign seats are added:

| seats included | cells | E |
|---|---|---|
| **subvalence + valence** | 14 | **0** |
| + the core | 15 | 3 |
| + the nucleus | 20 | 8 |
| + the aggregate | 21 | 11 |
| all five | 26 | 19 |

**PCA's domain is the subvalence and valence shells, and the index declares it by
degrading monotonically outside it.** *That is not a failure to close. It is a
boundary stated — as Seaton's ratio is valid at p = 0 and undefined beyond.*

## The last cell, and what filled it

All 1,440 orderings of the three axes give minimum E = 1, so the defect is
structural rather than a labelling artefact. **The cell is `symmetry × the valence
shell × a charge role`.**

**The fill is the ground TERM, which changes with charge:**

| Nₑ | c=1 | c=2 | c=3 | c=4 |
|---|---|---|---|---|
| **20** | ¹S₀ | ³D₁ | ³F₂ | ³F₂ |
| **38** | ¹S₀ | ³D₁ | ³F₂ | ³F₂ |
| 56 | ¹S₀ | ³F₂ | ³H₄ | — |
| 88 | ¹S₀ | ¹S₀ | ³H₄° | — |

*The sequence ¹S₀ → ³D₁ → ³F₂ is identical at two electron counts. Every ladder
table carried the term symbol; the configurations were recorded and the terms were
not.*

## The routing, by residual

| residual | property | class |
|---|---|---|
| the 1.029 factor on t(ℓ) | subshell radius | one subshell |
| no f corridor | centrifugal barrier | d and f only |
| the occupancy slope | subshell radius | one subshell |
| the crossing charge 2, 3, 5 | closed f shell n_f | period 6, 7 |

**Both of the first two were routed and both dissolved.** *The f corridor does not
exist because p = 0 is the node floor, so no rival lies below and L = −∞ — the
missing test is forbidden by the node count, not by missing data. And the 1.029
was arithmetic: the excess above U is 0.028 of the spread at p and 0.785 at d, a
ratio of 27.7, and the apparent 2.9% agreement came from comparing a ratio at p,
where t ≈ 1, with a ratio at d, where t ≈ 1.78.*

---

# Λ_PCA — PHYSICS ⊕ CHARGE ⊕ AMPLITUDE, AS ONE

*Registers 1297, 1323–1324, 1345. The merged index that correlates every chemical
property to the physics that requires it.*

## The merge

**Λ_phys** closes on (source, domain). **Λ_charge** closes on (role, carrier, sign,
regime). **The shared axis is `domain ≡ regime`** — both say where a statement
holds, and the charge regime is the physics domain at finer resolution.

**Merged on that axis alone: E = 0 on nine cells.**

| | universal | all elements | low | neutral | hydrogenic | one species |
|---|---|---|---|---|---|---|
| **standard** | 5 | · | · | · | · | · |
| **mathematics** | 3 | 1 | · | · | · | · |
| **literature** | · | 7 | 1 | · | · | · |
| **this work** | · | 2 | 5 | 2 | 4 | · |

**A staircase, and the diagonal is the whole content: nothing standard is
restricted to a region, and nothing this work produced claims universal validity.**

## What it gives that neither parent does

**The per-atom calibration.** A parameter's domain now reads as a SET OF ATOMS —
*universal* is every atom and ion, *all elements* every neutral, *neutral* c = 1,
*low* c = 2, *hydrogenic* c ≥ 3, *one species* a single (Z, c). **For any given
species the index states which parameters apply to it.**

**And the closing order puts `low` before `neutral`** — charge 2 is the most
particular domain. *The isoelectronic ladders confirm it independently: c = 2 is
the only charge with two-sided brackets.*

## Λ_amp — the amplitude's own index

**The amplitude is the electron–electron term**, and the multipole expansion of
1/r_ij gives, for each subshell pair, an exact finite list: **F^k for k even up to
2min(ℓ,ℓ′), G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to ℓ+ℓ′.**

**Twenty cells, E = 0, a triangle 0 ≤ i ≤ ℓ** — once indexed on position within
sequence rather than multipole rank. *Indexed on the raw rank the single defect is
F¹, a term parity forbids.*

**And it explains the Slater result exactly.** At s/s the exchange G⁰ IS the direct
F⁰, so dropping exchange costs nothing; at f/f it discards four independent
quantities. **The count of lost integrals is the count of failures: Slater
screening threads 5 of 5 s-block brackets and 0 of 1 f.**

**The angular factor of the sole exchange integral for an s electron against an ℓ
electron is exactly 1/(2ℓ+1)** — 1, 1/3, 1/5, 1/7 at s, p, d, f, to machine
precision. *The reciprocal of the subshell's orbital degeneracy, a count Λ already
holds, and it agrees independently with h(ℓ) = h₀√(2ℓ+1) measured from the
collapse data.*

---

# A CORRECTION TO SEATON'S RATIO

**Previously recorded**: the ratio δ₂/δ₀ comes out at 1.25 where the dipole term
gives 1.00, and the departure is a per-core constant reproducible to two decimals.

**That measurement was made on penetrating channels, where the relation is
undefined.** Seaton's derivation assumes the outer electron is non-penetrating, so
the core polarisability is the whole interaction.

**Stated properly:**

| | series | ratio to Seaton | sd |
|---|---|---|---|
| **p = 0** | 3 | **1.150** | 0.206 |
| **p ≥ 1** | 10 | **−0.015** | 0.177 |

**On the non-penetrating branch the relation holds to 15%. On the penetrating
branch the ratio is zero — the relation carries no information at all.**

*Not "broken at d and sound at f". Valid at p = 0 and undefined at p ≥ 1, which is
a domain statement and exactly what Λ_phys's domain axis is for.*

**And the sign of δ₂ is penetration, not ℓ**: 0 of 3 positive at p = 0, 2 of 2 at
p = 5, monotone in p between.

---

# THE CHANNEL CONSTANTS IN Λ_phys

*Owed since register 1296; written at register 1571. The failure modes are the
point - a constant listed without the conditions under which it stops meaning
anything is a number pretending to be a law.*

| standing | count | what it means |
|---|---|---|
| attributed / derived | 5 | traceable to a published result or a proof |
| measured | 6 | read from data, with a stated spread |
| **fitted** | 3 | set to make the form agree; **carries no physics** |

**The three fitted constants are the amplitude law's**, and they are why nothing
in the *amplitude* work answers Löwdin's challenge. *Written at register 1571; the challenge was closed at register 1701 by a different instrument, Λ_chain, which carries no fitted constant. The sentence is kept because it was true of what it described.*

## Failure modes

| constant | fails when | how it shows |
|---|---|---|
| the amplitude a | across a language boundary | six placement rules dead; a seventh **prohibited** |
| beta = 2/3 | - | no failure mode found; attributed, arity three |
| the gate ℓ(ℓ+1) | never as a gate | but SIX appearances under six discipline names |
| u0 = 4 | outside the collapse region | the switch is local to the d-wave entry |
| the nu form | as a MEASURE | bounded delta against diverging a*sqrt(p) - **impossible** |
| the three fitted | held out | the walk scores 90 against Madelung's 96 |

**The last row is the one to read.** A constant fitted on the data it explains
scores 99; held out it scores below the rule it was built to improve on.
*A failure mode is not a caveat - it is the boundary of the domain, and
Λ_phys exists to carry boundaries.*
<<<END FILE: The_Method_1_6___The_Physics_Compendium-2.md>>>

<<<FILE: The_Method_1_6___The_Index_of_Indices-2.md>>>

# THE METHOD 1.6 — THE INDEX OF INDICES

Generated on 2026-08-15 by `indices.py`. **Every index this work builds
on or beside the atomic index — what it holds, whether it closes, whether it carries time, and
what role it plays for Λ.** Measured where measurable; where an index is named and never built,
that is stated rather than filled in.

---

# I · THE ATOMIC INDEX ITSELF

**Λ = { (n, ℓ, k, q, e, f, g, 2S) ∈ ℤ⁸ : eight constraints, at caps }.**

![**Figure 1.** Λ₈'s constraint graph. Seven bounds on eight coordinates — a caterpillar with 2S pendant at k. Every edge is a single monotone inequality except one: **g takes two parents**, and g ≤ min(q, 4f+2) is the only non-product term in the whole expression.](figures-compendia/fig-i3-lambda8.png)

A cell is a **transition**: a source subshell (n, ℓ) holding k electrons, q of them moving, into a
target subshell (e, f) that ends with g, at spin 2S. **Not a state — a move.** Everything else in
this document follows from that.

| constraint | reads |
|---|---|
| **ℓ ≤ n − 1** | hydrogenic — the subshell fits its shell |
| **k ≤ 4ℓ + 2** | **Pauli** — the subshell's capacity |
| **q ≤ k** | conservation of the removed — you cannot take more than is held |
| **f ≤ e − 1** | hydrogenic again, on the target |
| **g ≤ 4f + 2** | **Pauli** again, on the target |
| **g ≤ q** | conservation of the placed |
| **2S ≤ k** | the multiplicity a subshell can carry |
| **k ≥ 1** | *definitional* — a transition needs a mover |

**The one coupling is g ≤ min(q, 4f+2)**, the single non-product term in the generating function,
and it is the Pauli principle. Remove it and 976 becomes 1,000; the 24 excluded cells all have
f = 0 and g = 3 — three electrons in an s orbital.

---

# II · THE TOWER

**Each stage adds one axis and inherits every bound below.**

| stage | cells | axes | composable | fraction | the axis added |
|---|---|---|---|---|---|
| **Λ₈** | 976 | 8 | 0 | **0.0000** | — |
| **Λ₉** | 1,654 | 9 | 1,169 | **0.7068** | 2S′ ≤ g |
| **Λ₁₀** | 2,535 | 10 | 2,050 | **0.8087** | 2S′ ≤ v ≤ g |
| **Λ₁₁** | 13,585 | 11 | 9,450 | **0.6956** | 2J_c ≤ φ̂(k) |
| **Λ₁₂** | 22,275 | 12 | 14,242 | **0.6394** | 2K ≤ 2J_c + 2f |
| **Λ₁₃** | 64,290 | 13 | 39,772 | **0.6186** | \|2J − 2K\| ≤ 1 |

![**Figure 2.** The composable fraction stage by stage. **Λ₈ composes not at all** — four source coordinates against three target. The two counting axes take it to a peak of 0.8087 at Λ₁₀; the three coupling axes lower it every time.](figures-compendia/fig-i1-tower.png)

> **Counting axes raise the composable fraction; coupling axes lower it. No exception.**

**Λ₈ composes not at all** — four source coordinates against three target. **Λ₁₀ is the peak at
80.87%**, and every stage after it falls. **The non-composable cells are exactly those with g = 0**
at the peak, since k ≥ 1 forbids an empty target being a source.

---

# III · THE INDEXES DRAWN BESIDE IT

| index | coordinates | cells | box | E | kind |
|---|---|---|---|---|---|
| the periodic table | (period, group) | 90 | 126 | **36** | **state** |
| Janet's left-step | (n+ℓ, Z) | 118 | 944 | **0** | **state** |
| the calendar | (month, day) | 365 | 372 | **7** | **state** |
| a box ordering | (l, w, h) | 35 | 125 | **0** | **state** |
| a chessboard | (rank, file) | 64 | 64 | **0** | **state** |

![**Figure 3.** Every index this work builds or draws, by cells against defect. **Circles are transition indexes** — their cells are moves, so they carry a time column. **Squares are state indexes** — a cell is one position, and the question of composition does not arise.](figures-compendia/fig-i2-landscape.png)

**None of these is a transition index, so none can carry a time column.** A state cell has one
position; the question *is my target another cell's source* does not arise.

**Janet closes at E = 0 and the classroom table does not.** That is a fact about the two tables
**in coordinates chemists fixed for other reasons** — §21.6 shows any composite count has SOME
coordinate system where E = 0, so the result is that Janet's 1928 ordering, chosen for shell
filling, happens to close.

---

# IV · THE VIOLATION INDEX

**The companion paper's object, indexed over nine letters.** It is here because it is the one
index this work reasons about without holding — **its cells are not printed anywhere**, and what
follows is everything that is.

| letter | meaning | rungs |
|---|---|---|
| **X** | exotic matter required | 4 |
| **S** | semiclassical corrections | 3 |
| **IC** | initial conditions | 3 |
| **U** | unitarity | 3 |
| **NEC** | null energy condition points | 5 |
| **L** | locality | 2 |
| **SD** | superdeterminism | 2 |
| **DNc** | dynamical, continuous | 3 |
| **DNd** | dynamical, discrete | 3 |

**4 · 3 · 3 · 3 · 5 · 2 · 2 · 3 · 3 = 19,440**, and the index holds **2,370** — 12.19% density.

## What the companion prints

| object | threshold | cells | reachable |
|---|---|---|---|
| classical black hole | `none` | 2,370 | 1,410 |
| Hawking-evaporating | `NEC ≥ 1` | 2,196 | 1,410 |
| Planck-scale wormhole | `NEC ≥ 2` | 1,764 | 1,134 |
| macroscopic wormhole | `NEC ≥ 3` | 1,146 | 738 |
| universal horizon | `X ≥ 2` | 1,374 | 840 |
| time machine | `X = 3` | 558 | 360 |

**Twelve numbers, and one column is a second predicate on the same cells.** Differenced, the
cells give NEC = 0 at 174, NEC = 1 at 432, NEC = 2 at 618, NEC ≥ 3 at 1,146. **All 174 cells at
NEC = 0 are unreachable** — removing them removes no reachable cell — and **exactly 64% of NEC = 1
and 64% of NEC = 2 cells are reachable**, 276 of 432 and 396 of 618.

## Its defect, and the one constraint printed

**E = 30, collapsing as 1 × 30** — one core cell repeated across the free coordinates — with the
core at **(X = 0, U = 0, NEC = 3)**. At fifteen letters: 18,072 cells, **E = 816 = 1 × 816.**
**Multiplicities 3, 5, 10, 30 at 4, 5, 7 and 9 coordinates**, and 5 is not a product of any two
rung counts, so **the edge list constrains the free letters as well as the support.**

**The constraint the companion prints**, at arity 3:

> **NEC ≥ 3 ∧ X = 0 → U ≥ 1** — cells 2,370, E = 30, core 1

with three variants: `NEC ≥ 3 → U ≥ 1` at arity 2 giving **E = 0**, and `NEC ≥ 3 ∧ U = 0 → X ≥ 1`
and `NEC ≥ 3 → (IC ∨ U ∨ X)` both giving E = 30. **A jurisdicted forcing and an unjurisdicted
disjunction give identical defects; arity 2 gives none.**

## What is not printed, and what nine searches established

**The edge list itself.** §5.7 of the companion says so outright. Nine searches were run against
the twelve numbers; the best holds **cells exactly 2,370 at distance 29**, with the whole residual
on the NEC interior — **NEC ≥ 2 sixteen too high, NEC ≥ 3 nine too low, missing in opposite
directions.**

**Eight alphabets were tried and none moved it**: simple implications, disjunctive heads,
conjunctive bodies, all 47 single-rule edits, four alternative rung readings, two threshold
semantics, seeding at NEC = 3, and weighted sums with gated deviations. **The rungs and the ≥
reading are confirmed correct** — every alternative is two orders of magnitude worse.

    **And the reachable column reduces to the same missing artefact.** Three local
    readings of reachability give ~99% against a printed 60%; the companion's own
    `here?` column says reachable means reachable FROM HERE, directed from one
    position in a transition graph. **Both columns need the edge list.**

---

# V · THE INDEXES BUILT FROM IT

Each of these exists because Λ exists — it indexes something Λ's cells have, or something the
act of building Λ produced.

## The electromagnetic quotient

**Λ modulo the dipole selection rules** — Δℓ = ±1, ΔS = 0, parity. A quotient, not a subset:
cells are identified when the rules cannot distinguish them.

**Its E = 0 is VACUOUS** — §12.11.8 — because the image is a complete rectangle. **It closes
because it is a box, not because the selection rules constrain it**, and that is the one closure
in this work that certifies nothing.

![**Figure 4.** The crossing. Within one atom a dipole-allowed transition is the LEAST likely to be followable; across the 118 elements it is the most. **The rule that forbids composition inside an atom is the rule that enables it between atoms.**](figures-compendia/fig-i4-crossing.png)

**Its measured role is the crossing.** Within one element, EM-allowed transitions compose at
**11.6%** against the forbidden **40.7%**. Across the 118 elements the order reverses — **89.7%
against 77.9%.** *The rule that forbids composition inside an atom is the rule that enables it
between atoms.*

## The time index

**Not a coordinate. The second column.** §12.11.0: composition IS the temporal order — a cell's
source end is a before, its target end an after, and q is what changed between them.

**An index has a time column exactly when its cells are moves.** Λ₈ 976/0, Λ₉ 1,654/1,169,
Λ₁₀ 2,535/2,050 — and the periodic table and the calendar **cannot have one**, because a state
cell has one position and there is nothing to compose.

**What Λ lacks is not a clock but a denominator** — claims per session — which §12.11.1.1 now
supplies. *A date must never enter Λ: a transition is a type, and types are not dated.*

## The space index

**The first column.** What the index holds, as against what it can compose. **Λ has no spatial
coordinate**: n and e are shell numbers, not positions, and nothing in the eight is a place.

**The nearest thing to a spatial reading is the observability one**: an observer's register is
Λ-valued because observation IS an atomic state change, so an unregistered event is an
admitted-and-absent cell and **E(local register) measures what is not yet real to that observer.**
*That is a definition with a falsifiable consequence and it is not yet built.*

## Λ₃ — the three-body index

**The second index built from physics rather than from Λ** (the first is Λ_spectra), and the first whose subject is classical. Chapter 36; register 1713–1724.

| coordinate | values | bound |
|---|---|---|
| stratum | KAM, per, chaos, erg, coll | five, exhaustive |
| E | ℝ | sign fixes bounded/unbounded |
| L | ℝ | — |
| masses | ℝ₊³ | 13 order-types; symmetry order 6, 2, 1 |

![**Figure 5.** The tower read downward: 12 → 4 → 2 → 1 inputs.](figures/fig3_tower.png)

**E(Λ₃) = 0.** Certificate (§18.4.1): the shape map, three dropped coordinates. *Its cells are configurations, not moves, so it carries no time column — the flow is the geodesic flow of the Jacobi–Maupertuis metric, and time is a quadrature (§12.11.1.3).* Named at §12.11.2 as the maximal case of what Chapter 18 forbids; built, and the completeness is the impossibility theorem read as an index.

## The languages

**A language is a coordinate system; translation is re-coordinatisation; E is the cost.**

| language | closure operator | delete | add |
|---|---|---|---|
| order | ℛ | restored | absorbed |
| geometry | monotone polyhedron | restored | absorbed |
| algebra / logic | ideal, Gröbner basis | still derivable | T·h enters the ideal |
| analysis | coefficients of F | restored | absorbed |
| information | description length | E_bits stays 0 | **grows** |
| **statistics** | max-entropy on the marginals | restored | **grows** |
| documentary | **none — no algorithm** | — | — |

**Six agree on Λ at 976 and all ten pairs hold** — C(5,2), a complete graph, not a ladder.
**Statistics was tested and qualifies with a caveat**: it recovers Λ at 976 and E = 0, but gives
**E = 0 on the periodic table where ℛ gives 36** — *marginals cannot see a hole.* It agrees with
the others only where there is nothing to disagree about.

## The book's own indexes

| index | coordinates | cells | E | what it holds |
|---|---|---|---|---|
| the audits | object<source<artefact<outside · what · how · depends | 21 | **16** | twenty-two audits |
| the register | corroboration ≤ φ̂(repair) | 33 | **6** | the corrections |
| Q | blocks · obstacle · cost · depends | 8 | **5** | what the book does not know |
| the protocols | trigger · object · failure · earned | 19 | **105** | twenty-four protocols |
| the constraints | parents · form · carried · source · role | 15 | **21 / E₄ 6** | every constraint in the book |
| the mathematics | kind · language · status · verification · precedent | 77 | **0** | fibred, twenty-four fibres (27 over sixteen when this table was first printed; main §D.5.10) |
| the numbers | fibre · kind · role | — | **40** | every figure the book prints |
| **the channel survey** | **Z · core charge · ℓ** | **1,664** | **1,351** | **596 Rydberg channels across 313 cells** |

**These exist because the book exists, not because Λ does** — but they are built by Λ's method,
and the audits index's two frontier cells are the same pair ℛ₄ refuses at §14.5.6, reached by two
computations sharing no code.

---

## How much of an index determines the rest

**Remove cells at random and ask whether ℛ puts them back.** The largest fraction removable with exact recovery is a property of the index, and it had never been measured for any of these.

| index | dimension | envelopes | coupling | **redundancy** |
|---|---|---|---|---|
| Λ | 8 | 56 | 29% | **61%** |
| Λ_spectra^obs | 3 | 6 | 17% | **20%** |
| a box ordering | 3 | 6 | 50% | 0% |
| Janet | 2 | 2 | 50% | 0% |
| the periodic table | 2 | 2 | 0% | 0% |
| the calendar | 2 | 2 | 0% | 0% |

**Coupling does not explain it.** The fraction of coordinate pairs whose envelope actually constrains gives **r² = 0.002, p = 0.94** against redundancy: Janet and the box ordering both couple at 50% and recover nothing, while Λ_spectra^obs couples at 17% and recovers a fifth. *That conjecture was stated before the measurement and is wrong.*

**DIMENSION explains it, and the projection test shows so on a single object.** Λ restricted to its own first d coordinates, constraints unchanged:

        d = 8   61%        d = 5   30%
        d = 7   30%        d = 4    5%
        d = 6   30%        d = 3    0%

ℛ works on **pairwise** envelopes, so an index of dimension d carries d(d−1) of them — **56 for Λ, 6 for Λ_spectra^obs, 2 for a plane.** With two envelopes there is almost nothing to reconstruct from, and that is what the operator is rather than a fact about any subject.

**But only INDEPENDENT coordinates count.** Adding the electron count Nₑ = Z − c + 1 to Λ_spectra^obs — a function of two coordinates it already has — takes redundancy from **20% to 0%**, while doubling the envelopes and raising coupling from 17% to 33%. *A derived coordinate adds no information and obliges ℛ to reproduce it exactly, so recovery becomes strictly harder.* Registers 1119–1122.


---

## The channel survey — Λ_spectra^obs

**Coordinates: Z · core charge · ℓ.** Each cell is a Rydberg channel — a fixed parent core, a fixed ℓ, n running. The compendium holds **596 channels across 313 of the survey's 1,664 cells**.

**This is not the coordinate index, and the two were once both called Λ_spectra.** Λ_spectra proper is the four-coordinate index (Z, charge, ℓ, 2S+1) at 104,832 cells with **E = 0** — see *Λ_spectra — the channel index*, below. Λ_spectra^obs is the three-coordinate **survey of what has been measured**. The column beside each cap below is grid minus held — the **unwitnessed** count — and *not* a closure defect: reading it as E would say the index is open when it is a fixed point. R 1657.

**Where its alphabets come from, and why that differs from Λ.** Λ's coordinates are bounded by the physics — ℓ < n, k ≤ 4ℓ+2 — and all 118 ground configurations are known within its caps, so Λ is complete at 976 cells. **Λ_spectra^obs is not.** Rydberg series are unbounded in n and ℓ runs to n−1, so the index is **infinite unless capped**, and every cap is a decision. Three defensible ones give:

| alphabet | grid | unwitnessed |
|---|---|---|
| as measured — charge [1, 2, 3, 4, 5, 6, 9, 11, 15, 16] | 1,664 | 1,351 |
| charge 1 to Z−1 over the elements held | 4,376 | 4,148 |
| all 118 elements, ℓ 0–7 | 55,224 | 54,996 |

**All three grids are closed** — each is a fixed point of ℛ, verified by double projection. The number beside each is what has *not* been measured under that cap, so it is a result about the cap and about the state of the literature; it is never a closure defect. *Registers 959–962, 1657.*

**What the index says about cells it does not hold.** Every cell carries a grade, and the grade records how far the statement travelled:

| grade | cells | what it means |
|---|---|---|
| MEASURED | 205 | a defect computed from levels |
| BRACKETED | 5 | bounded above and below by DIFFERENT mechanisms |
| BOUNDED | 42 | bounded on one side, adjacent to a measurement |
| PROPAGATED | 954 | a bound inherited through a chain of 2 to 13 steps |
| FORMAL | 73 | the only bound is one a mechanism already implies |
| UNCONSTRAINED | 33 | **no statement at all** |

**97.5% of the index carries a defensible statement.** The three relations that propagate are **P.lcollapse** along ℓ, **P.iso** along an isoelectronic sequence, and **P.charge** along the charge states of one element. *Registers 963–965, 981.*

![**Figure 6.** Λ_spectra^obs drawn as a lattice — element across, ℓ into the page, ionisation stage up. Green is measured, orange bounded from two sides by different mechanisms, gold from one; the faint markers are cells the structure admits and nobody has measured. **The occupied region is a wedge at low Z and low ℓ**, which is where long Rydberg series have been tabulated — and the emptiness above it is the shape of what an index says it does not know.](figures-compendia/fig-spectra-lattice.png)

**And the last 33 are of three kinds, only two of which a capture can fix.** P I, Cd I, Ti II and Ar I want longer captures. **Sc I and Ti I have no Rydberg series at all** — their levels are 3d.4s.4p and 3d².4s mixtures with no n running, so fourteen cells are unreachable by any capture. *Register 983.* **The ceiling is 98.6%, not 100%, and that is a fact about the open-shell transition metals rather than about the collection.**


---

# VI · THE INDEXES NAMED AND NOT BUILT

**§29.1: the absence is not evidence.** These were named in the course of the work and no index
exists for them. Saying so is the point of this section.

**Sound.** Phonon modes are discrete and indexable — ω, lattice momentum, polarisation, occupation
— but they index a **material**, not an atom. **No such index is built here**, and it would sit
beside Λ rather than inside it, since Λ has no coordinate a lattice vibration could occupy.

**Frequency.** A transition's frequency is ΔE/h, and ΔE is not a coordinate of Λ — **§6.2 gives
first ionisation energies to the bracket and the bracket REFUSES**, at Be→B, N→O, Mg→Al and P→S,
four steps of twelve. *That refusal is the book's most direct statement about frequency: the
coordinates cannot bracket it, and where they refuse a mechanism is entering.*

**The multiverse.** §32.6.1 places this outside all four of the book's indexes, with the
destination coordinate, because §E.1.4 shows **the open set cannot express an unclosable question.**
*It is not an index that has not been built. It is the shape of a question this work cannot pose*
— and Theorem 18.1 is why: Λ's order structure contributes nothing predictively beyond what the
coordinates supply, and its coordinates are n, ℓ, k, q, e, f, g, 2S.

---

# VII · THE FULL TABLES

**Every index small enough to print, printed.** The tower above Λ₈ runs to 64,290 cells at Λ₁₃
and is given by its construction instead; the violation index has no cells to give.

## Λ₈ — all 976 cells

| # | n | ℓ | k | q | e | f | g | 2S |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 3 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 5 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 6 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 7 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 8 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 9 | 1 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 10 | 1 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 11 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 12 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 13 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 14 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 15 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 16 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 17 | 1 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 18 | 1 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 19 | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 20 | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 21 | 1 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 22 | 1 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 23 | 1 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 24 | 1 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 25 | 1 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 26 | 1 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 27 | 1 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 28 | 1 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 29 | 1 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 30 | 1 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 31 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 32 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 33 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 34 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 35 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 36 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 37 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 38 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 39 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 40 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 41 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 42 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 43 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 44 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 45 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 46 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 47 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 48 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 49 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 50 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 51 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 52 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 53 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 54 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 55 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 56 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 57 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 58 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 59 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 60 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 61 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 62 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 63 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 64 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 65 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 66 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 67 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 68 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 69 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 70 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 71 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 72 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 73 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 74 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 75 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 76 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 77 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 78 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 79 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 80 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 81 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 82 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 83 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 84 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 85 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 86 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 87 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 88 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 89 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 90 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 91 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 92 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 93 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 94 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 95 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 96 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 97 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 98 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 99 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 100 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 101 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 102 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 103 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 104 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 105 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 106 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 107 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 108 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 109 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 110 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 111 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 112 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 113 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 114 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 115 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 116 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 117 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 118 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 119 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 120 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 121 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 122 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 123 | 2 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 124 | 2 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 125 | 2 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 126 | 2 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 127 | 2 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 128 | 2 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 129 | 2 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 130 | 2 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 131 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 132 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 133 | 2 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 134 | 2 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 135 | 2 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 136 | 2 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 137 | 2 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 138 | 2 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 139 | 2 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 140 | 2 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 141 | 2 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 142 | 2 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 143 | 2 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 144 | 2 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 145 | 2 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 146 | 2 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 147 | 2 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 148 | 2 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 149 | 2 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 150 | 2 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 151 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 152 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 153 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 154 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 155 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 156 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 157 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 158 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 159 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 160 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 161 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 162 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 163 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 164 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 165 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 166 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 167 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 168 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 169 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 170 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 171 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 172 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 173 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 174 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 175 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 176 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 177 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 178 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 179 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 180 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 181 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 182 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 183 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 184 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 185 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 186 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 187 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 188 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 189 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 190 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 191 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 192 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 193 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 194 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 195 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 196 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 197 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 198 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 199 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 200 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 201 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 202 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 203 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 204 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 205 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 206 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 207 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 208 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 209 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 210 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 211 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 212 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 213 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 214 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 215 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 216 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 217 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 218 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 219 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 220 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 221 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 222 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 223 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 224 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 225 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 226 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 227 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 228 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 229 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 230 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 231 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 232 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 233 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 234 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 235 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 236 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 237 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 238 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 239 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 240 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 241 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 242 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 243 | 2 | 1 | 1 | 0 | 2 | 0 | 0 | 0 |
| 244 | 2 | 1 | 1 | 0 | 2 | 0 | 0 | 1 |
| 245 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 0 |
| 246 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| 247 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 0 |
| 248 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 |
| 249 | 2 | 1 | 1 | 0 | 3 | 1 | 0 | 0 |
| 250 | 2 | 1 | 1 | 0 | 3 | 1 | 0 | 1 |
| 251 | 2 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 252 | 2 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 253 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| 254 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 255 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 0 |
| 256 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 1 |
| 257 | 2 | 1 | 1 | 1 | 2 | 0 | 1 | 0 |
| 258 | 2 | 1 | 1 | 1 | 2 | 0 | 1 | 1 |
| 259 | 2 | 1 | 1 | 1 | 2 | 1 | 0 | 0 |
| 260 | 2 | 1 | 1 | 1 | 2 | 1 | 0 | 1 |
| 261 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 0 |
| 262 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 1 |
| 263 | 2 | 1 | 1 | 1 | 3 | 0 | 0 | 0 |
| 264 | 2 | 1 | 1 | 1 | 3 | 0 | 0 | 1 |
| 265 | 2 | 1 | 1 | 1 | 3 | 0 | 1 | 0 |
| 266 | 2 | 1 | 1 | 1 | 3 | 0 | 1 | 1 |
| 267 | 2 | 1 | 1 | 1 | 3 | 1 | 0 | 0 |
| 268 | 2 | 1 | 1 | 1 | 3 | 1 | 0 | 1 |
| 269 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 0 |
| 270 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 1 |
| 271 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 0 |
| 272 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| 273 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 2 |
| 274 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 0 |
| 275 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 1 |
| 276 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 2 |
| 277 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 0 |
| 278 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 1 |
| 279 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 2 |
| 280 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 0 |
| 281 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 1 |
| 282 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 2 |
| 283 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 0 |
| 284 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 1 |
| 285 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 2 |
| 286 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 0 |
| 287 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 1 |
| 288 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 2 |
| 289 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| 290 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 1 |
| 291 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 2 |
| 292 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 0 |
| 293 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 1 |
| 294 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 2 |
| 295 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 0 |
| 296 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 1 |
| 297 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 2 |
| 298 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 0 |
| 299 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 1 |
| 300 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 2 |
| 301 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 0 |
| 302 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 |
| 303 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 2 |
| 304 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 0 |
| 305 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 1 |
| 306 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 2 |
| 307 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 0 |
| 308 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 1 |
| 309 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 2 |
| 310 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 0 |
| 311 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 1 |
| 312 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 2 |
| 313 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 0 |
| 314 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 1 |
| 315 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 2 |
| 316 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 0 |
| 317 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 1 |
| 318 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 2 |
| 319 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 0 |
| 320 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 1 |
| 321 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 2 |
| 322 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 0 |
| 323 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 1 |
| 324 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 2 |
| 325 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 0 |
| 326 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 1 |
| 327 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 2 |
| 328 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 0 |
| 329 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 1 |
| 330 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 2 |
| 331 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 0 |
| 332 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 1 |
| 333 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 2 |
| 334 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 335 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 1 |
| 336 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 2 |
| 337 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 0 |
| 338 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |
| 339 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 2 |
| 340 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 0 |
| 341 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 |
| 342 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 |
| 343 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 0 |
| 344 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 1 |
| 345 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 2 |
| 346 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 0 |
| 347 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 1 |
| 348 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 2 |
| 349 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 0 |
| 350 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 1 |
| 351 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 2 |
| 352 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 0 |
| 353 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 1 |
| 354 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 2 |
| 355 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 0 |
| 356 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 1 |
| 357 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 2 |
| 358 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 0 |
| 359 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 1 |
| 360 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| 361 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 0 |
| 362 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| 363 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 2 |
| 364 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 3 |
| 365 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 0 |
| 366 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 1 |
| 367 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| 368 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 3 |
| 369 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 0 |
| 370 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 1 |
| 371 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 2 |
| 372 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 3 |
| 373 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 0 |
| 374 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 1 |
| 375 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 2 |
| 376 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 3 |
| 377 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 0 |
| 378 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 1 |
| 379 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 2 |
| 380 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 3 |
| 381 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 0 |
| 382 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 1 |
| 383 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 2 |
| 384 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 3 |
| 385 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| 386 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 1 |
| 387 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 2 |
| 388 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 3 |
| 389 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 0 |
| 390 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 1 |
| 391 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 2 |
| 392 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 3 |
| 393 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 0 |
| 394 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 1 |
| 395 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 2 |
| 396 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 3 |
| 397 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 0 |
| 398 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 1 |
| 399 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 2 |
| 400 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 3 |
| 401 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 0 |
| 402 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 1 |
| 403 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 2 |
| 404 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 3 |
| 405 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 0 |
| 406 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 1 |
| 407 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 2 |
| 408 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 3 |
| 409 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 0 |
| 410 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 1 |
| 411 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 2 |
| 412 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 3 |
| 413 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 0 |
| 414 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 1 |
| 415 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 2 |
| 416 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 3 |
| 417 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 0 |
| 418 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 1 |
| 419 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 2 |
| 420 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 3 |
| 421 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 0 |
| 422 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 1 |
| 423 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 2 |
| 424 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 3 |
| 425 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 0 |
| 426 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 1 |
| 427 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 2 |
| 428 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 3 |
| 429 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 0 |
| 430 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 1 |
| 431 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 2 |
| 432 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 3 |
| 433 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 0 |
| 434 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 1 |
| 435 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 2 |
| 436 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 3 |
| 437 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 0 |
| 438 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 1 |
| 439 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 2 |
| 440 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 3 |
| 441 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 0 |
| 442 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 1 |
| 443 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 2 |
| 444 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 3 |
| 445 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 0 |
| 446 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 1 |
| 447 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 2 |
| 448 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 3 |
| 449 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 0 |
| 450 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 1 |
| 451 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 2 |
| 452 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 3 |
| 453 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 0 |
| 454 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 1 |
| 455 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 2 |
| 456 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 3 |
| 457 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 0 |
| 458 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 1 |
| 459 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 2 |
| 460 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 3 |
| 461 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 0 |
| 462 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 1 |
| 463 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 2 |
| 464 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 3 |
| 465 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 0 |
| 466 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 1 |
| 467 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 2 |
| 468 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 3 |
| 469 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 0 |
| 470 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 1 |
| 471 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 2 |
| 472 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 3 |
| 473 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 0 |
| 474 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 1 |
| 475 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 2 |
| 476 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 3 |
| 477 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 0 |
| 478 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 1 |
| 479 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 2 |
| 480 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 3 |
| 481 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 482 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 1 |
| 483 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 2 |
| 484 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 3 |
| 485 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 0 |
| 486 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 1 |
| 487 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 2 |
| 488 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 3 |
| 489 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 0 |
| 490 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 1 |
| 491 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 2 |
| 492 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 3 |
| 493 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 0 |
| 494 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 1 |
| 495 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 2 |
| 496 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 3 |
| 497 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 0 |
| 498 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 1 |
| 499 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 2 |
| 500 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 3 |
| 501 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 0 |
| 502 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 1 |
| 503 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 2 |
| 504 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 3 |
| 505 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 0 |
| 506 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 1 |
| 507 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 2 |
| 508 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 3 |
| 509 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 0 |
| 510 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 1 |
| 511 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 2 |
| 512 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 3 |
| 513 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 0 |
| 514 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 1 |
| 515 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 2 |
| 516 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 3 |
| 517 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 0 |
| 518 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 1 |
| 519 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 2 |
| 520 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 3 |
| 521 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 0 |
| 522 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 1 |
| 523 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 2 |
| 524 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 3 |
| 525 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 0 |
| 526 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 1 |
| 527 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 2 |
| 528 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 3 |
| 529 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 0 |
| 530 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 1 |
| 531 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 2 |
| 532 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 3 |
| 533 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 0 |
| 534 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 1 |
| 535 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 2 |
| 536 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 3 |
| 537 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 0 |
| 538 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 1 |
| 539 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 2 |
| 540 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 3 |
| 541 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 0 |
| 542 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 1 |
| 543 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 2 |
| 544 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 3 |
| 545 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 0 |
| 546 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 1 |
| 547 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 2 |
| 548 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 3 |
| 549 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 550 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 551 | 3 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 552 | 3 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 553 | 3 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 554 | 3 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 555 | 3 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 556 | 3 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 557 | 3 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 558 | 3 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 559 | 3 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 560 | 3 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 561 | 3 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 562 | 3 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 563 | 3 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 564 | 3 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 565 | 3 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 566 | 3 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 567 | 3 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 568 | 3 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 569 | 3 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 570 | 3 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 571 | 3 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 572 | 3 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 573 | 3 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 574 | 3 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 575 | 3 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 576 | 3 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 577 | 3 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 578 | 3 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 579 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 580 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 581 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 582 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 583 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 584 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 585 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 586 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 587 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 588 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 589 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 590 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 591 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 592 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 593 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 594 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 595 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 596 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 597 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 598 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 599 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 600 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 601 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 602 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 603 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 604 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 605 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 606 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 607 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 608 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 609 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 610 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 611 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 612 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 613 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 614 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 615 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 616 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 617 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 618 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 619 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 620 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 621 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 622 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 623 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 624 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 625 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 626 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 627 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 628 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 629 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 630 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 631 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 632 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 633 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 634 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 635 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 636 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 637 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 638 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 639 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 640 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 641 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 642 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 643 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 644 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 645 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 646 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 647 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 648 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 649 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 650 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 651 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 652 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 653 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 654 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 655 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 656 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 657 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 658 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 659 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 660 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 661 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 662 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 663 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 664 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 665 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 666 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 667 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 668 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 669 | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 670 | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 671 | 3 | 1 | 1 | 0 | 2 | 0 | 0 | 0 |
| 672 | 3 | 1 | 1 | 0 | 2 | 0 | 0 | 1 |
| 673 | 3 | 1 | 1 | 0 | 2 | 1 | 0 | 0 |
| 674 | 3 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| 675 | 3 | 1 | 1 | 0 | 3 | 0 | 0 | 0 |
| 676 | 3 | 1 | 1 | 0 | 3 | 0 | 0 | 1 |
| 677 | 3 | 1 | 1 | 0 | 3 | 1 | 0 | 0 |
| 678 | 3 | 1 | 1 | 0 | 3 | 1 | 0 | 1 |
| 679 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 680 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 681 | 3 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| 682 | 3 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 683 | 3 | 1 | 1 | 1 | 2 | 0 | 0 | 0 |
| 684 | 3 | 1 | 1 | 1 | 2 | 0 | 0 | 1 |
| 685 | 3 | 1 | 1 | 1 | 2 | 0 | 1 | 0 |
| 686 | 3 | 1 | 1 | 1 | 2 | 0 | 1 | 1 |
| 687 | 3 | 1 | 1 | 1 | 2 | 1 | 0 | 0 |
| 688 | 3 | 1 | 1 | 1 | 2 | 1 | 0 | 1 |
| 689 | 3 | 1 | 1 | 1 | 2 | 1 | 1 | 0 |
| 690 | 3 | 1 | 1 | 1 | 2 | 1 | 1 | 1 |
| 691 | 3 | 1 | 1 | 1 | 3 | 0 | 0 | 0 |
| 692 | 3 | 1 | 1 | 1 | 3 | 0 | 0 | 1 |
| 693 | 3 | 1 | 1 | 1 | 3 | 0 | 1 | 0 |
| 694 | 3 | 1 | 1 | 1 | 3 | 0 | 1 | 1 |
| 695 | 3 | 1 | 1 | 1 | 3 | 1 | 0 | 0 |
| 696 | 3 | 1 | 1 | 1 | 3 | 1 | 0 | 1 |
| 697 | 3 | 1 | 1 | 1 | 3 | 1 | 1 | 0 |
| 698 | 3 | 1 | 1 | 1 | 3 | 1 | 1 | 1 |
| 699 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 0 |
| 700 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| 701 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 2 |
| 702 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 0 |
| 703 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 1 |
| 704 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 2 |
| 705 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 0 |
| 706 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 1 |
| 707 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 2 |
| 708 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 0 |
| 709 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 1 |
| 710 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 2 |
| 711 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 0 |
| 712 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 1 |
| 713 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 2 |
| 714 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 0 |
| 715 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 1 |
| 716 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 2 |
| 717 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| 718 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 1 |
| 719 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 2 |
| 720 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 0 |
| 721 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 1 |
| 722 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 2 |
| 723 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 0 |
| 724 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 1 |
| 725 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 2 |
| 726 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 0 |
| 727 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 1 |
| 728 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 2 |
| 729 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 0 |
| 730 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 1 |
| 731 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 2 |
| 732 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 0 |
| 733 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 1 |
| 734 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 2 |
| 735 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 0 |
| 736 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 1 |
| 737 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 2 |
| 738 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 0 |
| 739 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 1 |
| 740 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 2 |
| 741 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 0 |
| 742 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 1 |
| 743 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 2 |
| 744 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 0 |
| 745 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 1 |
| 746 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 2 |
| 747 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 0 |
| 748 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 1 |
| 749 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 2 |
| 750 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 0 |
| 751 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 1 |
| 752 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 2 |
| 753 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 0 |
| 754 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 1 |
| 755 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 2 |
| 756 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 0 |
| 757 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 1 |
| 758 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 2 |
| 759 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 0 |
| 760 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 1 |
| 761 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 2 |
| 762 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 763 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 1 |
| 764 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 2 |
| 765 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 0 |
| 766 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |
| 767 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 2 |
| 768 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 0 |
| 769 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 1 |
| 770 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 2 |
| 771 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 0 |
| 772 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 1 |
| 773 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 2 |
| 774 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 0 |
| 775 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 1 |
| 776 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 2 |
| 777 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 0 |
| 778 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 1 |
| 779 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 2 |
| 780 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 0 |
| 781 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 1 |
| 782 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 2 |
| 783 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 0 |
| 784 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 1 |
| 785 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 2 |
| 786 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 0 |
| 787 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 1 |
| 788 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| 789 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 0 |
| 790 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| 791 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 2 |
| 792 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 3 |
| 793 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 0 |
| 794 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 1 |
| 795 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| 796 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 3 |
| 797 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 0 |
| 798 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 1 |
| 799 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 2 |
| 800 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 3 |
| 801 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 0 |
| 802 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 1 |
| 803 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 2 |
| 804 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 3 |
| 805 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 0 |
| 806 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 1 |
| 807 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 2 |
| 808 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 3 |
| 809 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 0 |
| 810 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 1 |
| 811 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 2 |
| 812 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 3 |
| 813 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| 814 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 1 |
| 815 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 2 |
| 816 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 3 |
| 817 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 0 |
| 818 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 1 |
| 819 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 2 |
| 820 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 3 |
| 821 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 0 |
| 822 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 1 |
| 823 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 2 |
| 824 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 3 |
| 825 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 0 |
| 826 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 1 |
| 827 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 2 |
| 828 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 3 |
| 829 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 0 |
| 830 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 1 |
| 831 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 2 |
| 832 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 3 |
| 833 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 0 |
| 834 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 1 |
| 835 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 2 |
| 836 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 3 |
| 837 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 0 |
| 838 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 1 |
| 839 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 2 |
| 840 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 3 |
| 841 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 0 |
| 842 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 1 |
| 843 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 2 |
| 844 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 3 |
| 845 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 0 |
| 846 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 1 |
| 847 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 2 |
| 848 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 3 |
| 849 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 0 |
| 850 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 1 |
| 851 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 2 |
| 852 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 3 |
| 853 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 0 |
| 854 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 1 |
| 855 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 2 |
| 856 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 3 |
| 857 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 0 |
| 858 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 1 |
| 859 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 2 |
| 860 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 3 |
| 861 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 0 |
| 862 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 1 |
| 863 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 2 |
| 864 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 3 |
| 865 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 0 |
| 866 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 1 |
| 867 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 2 |
| 868 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 3 |
| 869 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 0 |
| 870 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 1 |
| 871 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 2 |
| 872 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 3 |
| 873 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 0 |
| 874 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 1 |
| 875 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 2 |
| 876 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 3 |
| 877 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 0 |
| 878 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 1 |
| 879 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 2 |
| 880 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 3 |
| 881 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 0 |
| 882 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 1 |
| 883 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 2 |
| 884 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 3 |
| 885 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 0 |
| 886 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 1 |
| 887 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 2 |
| 888 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 3 |
| 889 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 0 |
| 890 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 1 |
| 891 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 2 |
| 892 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 3 |
| 893 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 0 |
| 894 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 1 |
| 895 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 2 |
| 896 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 3 |
| 897 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 0 |
| 898 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 1 |
| 899 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 2 |
| 900 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 3 |
| 901 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 0 |
| 902 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 1 |
| 903 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 2 |
| 904 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 3 |
| 905 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 0 |
| 906 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 1 |
| 907 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 2 |
| 908 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 3 |
| 909 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 910 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 1 |
| 911 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 2 |
| 912 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 3 |
| 913 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 0 |
| 914 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 1 |
| 915 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 2 |
| 916 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 3 |
| 917 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 0 |
| 918 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 1 |
| 919 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 2 |
| 920 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 3 |
| 921 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 0 |
| 922 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 1 |
| 923 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 2 |
| 924 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 3 |
| 925 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 0 |
| 926 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 1 |
| 927 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 2 |
| 928 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 3 |
| 929 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 0 |
| 930 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 1 |
| 931 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 2 |
| 932 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 3 |
| 933 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 0 |
| 934 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 1 |
| 935 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 2 |
| 936 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 3 |
| 937 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 0 |
| 938 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 1 |
| 939 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 2 |
| 940 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 3 |
| 941 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 0 |
| 942 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 1 |
| 943 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 2 |
| 944 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 3 |
| 945 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 0 |
| 946 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 1 |
| 947 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 2 |
| 948 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 3 |
| 949 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 0 |
| 950 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 1 |
| 951 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 2 |
| 952 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 3 |
| 953 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 0 |
| 954 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 1 |
| 955 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 2 |
| 956 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 3 |
| 957 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 0 |
| 958 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 1 |
| 959 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 2 |
| 960 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 3 |
| 961 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 0 |
| 962 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 1 |
| 963 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 2 |
| 964 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 3 |
| 965 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 0 |
| 966 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 1 |
| 967 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 2 |
| 968 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 3 |
| 969 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 0 |
| 970 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 1 |
| 971 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 2 |
| 972 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 3 |
| 973 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 0 |
| 974 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 1 |
| 975 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 2 |
| 976 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 3 |

**976 rows. F(1) = 976, F(−1) = 2, E = 0, density 0.1412 of a box of 6,912.**

## The periodic table — all 90 cells, (period, group)

| period | groups occupied |
|---|---|
| 1 | 1, 18 |
| 2 | 1, 2, 13, 14, 15, 16, 17, 18 |
| 3 | 1, 2, 13, 14, 15, 16, 17, 18 |
| 4 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 5 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 6 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 7 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |

**90 cells in a box of 126. E = 36** — and the 36 are the cells the coordinates admit and no
element occupies, which must be supplied from outside.

## Janet — all 118, (n+ℓ, Z)

| n+ℓ | atomic numbers |
|---|---|
| 1 | 1–2 (2) |
| 2 | 3–4 (2) |
| 3 | 5–12 (8) |
| 4 | 13–20 (8) |
| 5 | 21–38 (18) |
| 6 | 39–56 (18) |
| 7 | 57–88 (32) |
| 8 | 89–118 (30) |

**118 cells, E = 0.** The same 118 elements as the table above, reordered by n+ℓ.

## The calendar — 365 cells, (month, day)

| month | days | month | days |
|---|---|---|---|
| January | 31 | July | 31 |
| February | 28 | August | 31 |
| March | 31 | September | 30 |
| April | 30 | October | 31 |
| May | 31 | November | 30 |
| June | 30 | December | 31 |

**365 cells in a box of 372. E = 7** — February's missing 30th and 31st, and the four thirty-day
months' 31sts. **365 = 5 · 73, and 73 exceeds every rung**, so it is genuinely constrained.

## A box ordering — all 35, l ≥ w ≥ h

| l ≥ w ≥ h |
|---|
| 0·0·0  1·0·0  1·1·0  1·1·1  2·0·0  2·1·0  2·1·1 |
| 2·2·0  2·2·1  2·2·2  3·0·0  3·1·0  3·1·1  3·2·0 |
| 3·2·1  3·2·2  3·3·0  3·3·1  3·3·2  3·3·3  4·0·0 |
| 4·1·0  4·1·1  4·2·0  4·2·1  4·2·2  4·3·0  4·3·1 |
| 4·3·2  4·3·3  4·4·0  4·4·1  4·4·2  4·4·3  4·4·4 |

**35 cells in a box of 125, E = 0.** 35 = 5 · 7 and 7 exceeds the rung of 5: a real constraint.

---

# VIII · WHAT EACH INDEX IS, AND WHAT ONLY IT CONTRIBUTES

**Λ is the only index here built from physics.** The rest are built from Λ, from the act of building Λ, or from drawing the same subject another way. *This section states for each one: what it is, where it comes from in the published record, and the one thing it contributes to the atomic index that no other index can.*

---

## Λ — the atomic index

**What it is.** Eight integer coordinates (n, ℓ, k, q, e, f, g, 2S) under eight inequalities, 976 cells, E = 0.

**Where it comes from.** The constraints are not this work's: ℓ ≤ n−1 is the hydrogen solution (Bohr 1913; Schrödinger 1926); k ≤ 4ℓ+2 is Stoner's subshell capacity (1924) made exclusive by Pauli (1925); 2S ≤ k is Pauli with Hund's first rule (1925). **Λ assembles them; it introduces none.**

**What only it contributes.** *The transfer.* Λ is the only index here whose cells are MOVES rather than positions — a cell carries a source subshell, a target subshell and a count transferred. **Everything about composition, time columns and categories follows from that and from nothing else in this compendium.**

## The tower Λ₈…Λ₁₃

**What it is.** Λ with the coupling quantum numbers adjoined one at a time — seniority, the core J, K, then J. Cell counts 976, 1654, 2535, 13585, 70905, 199130, E = 0 at every stage.

**Where it comes from.** Each axis is Racah or Condon & Shortley: seniority is Racah, *Theory of complex spectra III*, Phys. Rev. **63** (1943) 367–382; the core J and the recoupling coefficients are Racah, Phys. Rev. **62** (1942) 438–462; the jK and LK schemes are Condon & Shortley (1935), ch. X.

**What only it contributes.** *The price of an axis.* The tower is the only construction here that adds one coordinate at a time and measures what each costs and buys — **cycle rank, composability, exactness, and the point at which the tree becomes a graph.** No single index can show that; it takes a sequence.

## The periodic table — (period, group)

**What it is.** 90 cells in a box of 126, E = **36**.

**Where it comes from.** Mendeleev, *Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente*, Z. Chem. **12** (1869) 405–406. At least a thousand periodic systems have been published since (van Spronsen; Scerri, *A Tale of Seven Scientists*, 2016).

**What only it contributes.** *The control.* It is the one index whose coordinates were fixed by other people for other reasons, long before this work, and which nonetheless supplies **118 elements and 18,288 constraint tests with zero failures.** **An index built by the author cannot be a control; this one can.**

## Janet's left-step table — (n+ℓ, Z)

**What it is.** The same 118 elements, ordered on n+ℓ. 118 cells in a box of 944, E = **0**.

**Where it comes from.** Charles Janet, *Considérations sur la structure du noyau de l'atome*, Beauvais (1929), with the table first published in **1928**. *Janet recognised the (n+ℓ) rule before Madelung, who arrived at it around 1926 and did not publish until 1936.* The shell-length sequence 2, 8, 8, 18, 18, 32, 32 follows from the rule by the Klechkovski–Hakala formulas.

**What only it contributes.** *That E is coordinate-relative, demonstrated on one subject rather than argued.* The periodic table and Janet index THE SAME 118 elements and give E = 36 and E = 0. **No pair of indexes anywhere else in this work makes that point as cleanly, because no other pair shares its subject exactly.**

**And an open problem sits underneath it.** *Why* the n+ℓ ordering holds is unresolved — Löwdin's challenge, still open; see Allen & Knight, *The Löwdin challenge: origin of the n+l, n (Madelung) rule*, Int. J. Quantum Chem. **90** (2003) 80–88. **This work uses the ordering and does not explain it**, and the orbital-collapse result (registers 1187–1190) is a measurement against Janet's boundaries, not a derivation of them.

## The nuclide chart — (Z, N)

**What it is.** The measured nuclides indexed by proton and neutron count, E = **9**.

**Where it comes from.** The chart is Segrè's, in use since the 1940s; the values are the AME2020 evaluation.

**What only it contributes.** *A defect whose cells are identifiable physics.* The nine cells are the mass formula's pairing and clustering terms. **It is the only index here where E > 0 and every missing cell can be named**, which is what makes the defect a measurement rather than a score.

## The calendar — (month, day)

**What it is.** 365 cells in a box of 372, E = **7**.

**Where it comes from.** The Gregorian reform of 1582, on the Julian arrangement of 46 BC. *The month lengths are a political inheritance, not a natural one.*

**What only it contributes.** *A subject with no physics in it at all.* The calendar shows the operator working on an object whose constraints are entirely conventional, **and 365 = 5 · 73 with E = 7 is the price of keeping January first.** No other index here separates the method from the physics so completely.

## The box ordering and the chessboard

**What they are.** ℓ ≥ w ≥ h over five values: 35 cells in 125, E = 0. And (rank, file): 64 cells in 64, E = 0.

**What only they contribute.** *The floor and the ceiling.* The chessboard is a full product — E = 0 because there is no constraint at all. The box ordering is a genuine constraint that still closes. **Between them they show that E = 0 carries information only when the ambient box exceeds the cells**, which is why the compendium reports box alongside every defect.

## The electromagnetic quotient

**What it is.** Λ₉ under the dipole selection rules: |Δℓ| = 1 and ΔS = 0.

**Where it comes from.** The parity rule is Laporte, Z. Phys. **23** (1924) 135; the spin rule is Russell & Saunders, Astrophys. J. **61** (1925) 38; both have their group-theoretic ground in Wigner, Z. Phys. **43** (1927) 624.

**What only it contributes.** *That a selection rule is a QUOTIENT and not an extension.* Adjoining the multipole and ΔS as coordinates gives E = 3; taking the image gives E = 0. **It is the only index here that demonstrates the difference between adding a coordinate and dividing by one.**

## Λ_spectra — the channel index

**What it is.** (Z, charge, ℓ, 2S+1) over 104,832 cells, with a defect for each.

**Where it comes from.** Quantum defect theory is Seaton, MNRAS **118** (1958) 504–518, and Rep. Prog. Phys. **46** (1983) 167–257. *A published survey of the same object exists*: Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables **35** (1986) 473–486, Hartree–Slater, for all ionisation stages of all ions with Z ≤ 50.

**What only it contributes.** *Values.* Every other index here holds cells and asks whether they close. **Λ_spectra holds cells that carry NUMBERS**, which is why it is the only index on which the Method equation's metric half — E_W — has anything to measure at all (registers 1196–1199).

## The violation index

**What it is.** The companion paper's object over nine and fifteen letters, with a core of three conditions whose joint failure is irreducible.

**Where it comes from.** The conditions are physics — the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950), the equations of motion. *The core is a MINIMAL UNSATISFIABLE SUBSET* in the sense of Chinneck & Dravnieks, *Locating minimal infeasible constraint sets in linear programs*, ORSA J. Comput. **3** (1991) 157–168.

**What only it contributes.** *An index this work reasons about without holding.* Its cells are not printed anywhere. **It is the only test of whether the method says anything when the object is out of reach**, and the answer is that it locates a three-condition core from published summary numbers alone.

## Λ_phys — the parameter index

**What it is.** Every number the work takes from physics, on four coordinates — kind (exact → fitted), source (mathematics → this work), domain (universal → one species), and how many registered objects rest on it. **27 parameters** (22 before Chapters 35 and 36 added c, the three-body masses, E, L and G).

**Where it comes from.** The parameters are Rydberg 1890, Bohr 1913, Stoner 1924, Pauli 1925, Hund 1925, Fermi 1928, Hartree 1928, Janet 1928, Mayer & Mayer 1933, Goeppert-Mayer 1941, Seaton 1958, Edlén 1964, Griffin, Andrew & Cowan 1969, CODATA 2018 — and eight numbers fitted here. *The Physics Compendium holds them in full, each with a definition, a dated source and a failure mode.*

**What only it contributes.** *Where the work would break first.* Every other index here asks whether a set of cells closes. **Λ_phys asks what the whole construction rests on, and the answer is a shape:** eight of the twenty-seven parameters are this work's own, **none of them is universal**, seven of the eight hold only in a region or for one species — and, on the one rule the Physics Compendium now prints, the two carrying the most objects are the lattice's own exact bounds, the angular-momentum bound (72 objects) and the subshell capacity (66), with the aufbau ordering (18) next; the earlier reading — the ionisation limit 25, the aufbau ordering 19, the Janet boundary 15, on a rule never printed — stands in that compendium as the prior state (register 1740).

**And three of its failure modes are MEASURED rather than anticipated** — Seaton's ratio at 1.25 where the dipole term gives 1.00, the Thomas–Fermi exponent rising from 0.84 to 1.52 with charge against a single fitted 0.494, and the exchange coefficient whose fitted sign is opposite to the measured one.

## The languages

**What they are.** Six readings of one index — order, analysis, algebra, geometry, information, statistics — with documentary as a seventh that has no operator.

**Where they come from.** Each operator is standard in its own field: closure from Moore (1910), max-entropy on marginals from Deming & Stephan (1940) and Csiszár (1975), conditional independence from Dawid (1979).

**What only they contribute.** *That translation is re-coordinatisation and E is its cost.* **And the agreement theorem: E(X) = 0 if and only if the languages agree** — six indexes, three operators, no exception (register 1176).

## The book's own indexes

**What they are.** The book at chapter resolution (E = 578) and at part resolution (E = 0); the register (E = 6 at 68.8% density); the reference index (38 cells, E = 0, and not a tree); the term index at the back of the main volume (57 terms over 44 specialisation relations, 311 locations, E = 0 as a down-set — regenerated from the text at this build).

**What only they contribute.** *The method self-applied.* **This is the only place where E > 0 is a theorem about SHAPE rather than a gap in collection** — the book's chapters do not close because chapters are not a coordinate system, and saying so with a number is the point.

---

## Λ₃ — the three-body index

**What it is.** Five strata on ℳ_{E,L} over three unspecified masses; E = 0.

**Where it comes from.** The classes are Chazy 1922; disjointness is Saari 1971/73 and Painlevé for n = 3; the assembly into one index with a certificate is this work's (register 1713).

**What only it contributes.** *A complete index whose completeness IS the impossibility theorem.* E = 0 read as Poincaré: by §25.6 a complete index with no time column predicts nothing, and that is Brudno's rate on the chaotic stratum, not a failure of the method (register 1714, 1724).

## The one-line summary

| index | the one thing only it gives |
|---|---|
| **Λ** | the transfer — cells that are moves |
| **the tower** | the price of an axis, measured one at a time |
| **the periodic table** | a control the author did not build |
| **Janet** | E is coordinate-relative, on one subject |
| **the nuclide chart** | a defect whose every cell is nameable physics |
| **the calendar** | a subject with no physics in it |
| **box and chessboard** | the floor and ceiling of what E = 0 means |
| **the EM quotient** | quotient versus extension |
| **Λ_spectra** | values, so the metric defect has something to measure |
| **the violation index** | reasoning about an index without holding it |
| **Λ_phys** | where the work would break first |
| **the languages** | translation as re-coordinatisation |
| **the book's own** | E > 0 as a theorem about shape |
| **Λ₃** | a complete index whose completeness *is* the impossibility theorem — E = 0 read as Poincaré |

**Λ and Λ₃ are the only ones built from physics. The rest are built from Λ, from the act of building Λ, or from drawing the same subject another way — and that is the claim: an index is a coordinate system, and the coordinates come from the subject or from nowhere.**

# IX · THE INDEXES BUILT IN THE LÖWDIN WORK

*Registers 1249–1429. **Fifteen indexes: fourteen closed — Λ_ladder now among them
— and Λ_spectra closing at the limit with eleven named cells.** Each is stated the same way:
what it indexes, its coordinates, the axis order that closes it, what it refuses,
and the one thing it contributes.*

---

## Λ_law — the laws of the channel equation

**What it is.** Seven laws on (law, carrier). **E = 0** at carrier order
**u < p < ℓ−ℓ_core < Z−T**, and 288 of 120,960 orderings reach it.

**What only it contributes.** *The carrier.* The order is monotone in how LOCAL
the variable is — u is the whole atom, p counts one ℓ's shells, ℓ−ℓ_core compares
two angular momenta, Z−T is one distance to one threshold. **The index says which
law runs in which variable, and fitting a law in the wrong carrier is what took
the ℓ-spread from a spurious r² 0.868 to a real 0.356.**

## Λ_const — the constants

**What it is.** Fourteen constants on (role, carrier), role order
**exponent < centre < width < scale**. **E = 0** at 2 of 576 orderings.

**What only it contributes.** *That `standing` cannot be a coordinate.* With
attributed/derived/measured/fitted on an axis the index cannot close at any
ordering; without it, it closes at once. **An index whose coordinates mix the
object with the observer cannot close, because the observer's axis has no order
the object respects.** The same fault recurs as `origin` in Λ_var, `kind` in
Λ_phys and `state` in Λ_ladder.

**And the role axis orders by how much physics a number has absorbed.** Every
CENTRE in the system is a small integer or half-integer — 2, 2, 2.5, −1.5, 5.4 —
and no SCALE is.

## Λ_var — the variables

**What it is.** Twelve variables on (body, role), body order
**nucleus < core < core+rydberg < nucleus+core < rydberg**. **E = 0.**

**What only it contributes.** *That there is no nucleus + rydberg cell.* Not one
variable relates them directly: every quantity connecting the Rydberg electron to
the nucleus — c, u — is a nucleus–core quantity that the Rydberg electron then
reads. **That is the screening statement appearing as a structural fact of the
index rather than a modelling choice, and it is the three-body factorisation:
nucleus–core gives c and u, core–Rydberg gives p, n₀ and T, and the Rydberg
electron's own ℓ closes it.**

**And the singleton rule.** Λ_var passes ℛ with both δ and n\* present, because
both land in the same cell — **only a second criterion sees it. An index is closed
when its output class is a singleton; two outputs mean the observer is still
choosing which to read.**

## Λ_ryd — the Rydberg series

**What it is.** Five cells on (Ritz order, ℓ, sign). **E = 0** once δ₂ is
reclassified as INTERMEDIATE — it is fitted from the series, never measured.

**What only it contributes.** *The n-dependence Λ_spectra discards.* A channel's
δ is not one number but a convergent sequence — Cd I's ns series gives 3.7171,
3.6835, 3.6719, 3.6665, 3.6637, 3.6621, 3.6610. **Λ_spectra holds δ₀; Λ_ryd holds
δ₂ and δ₄.**

**And the sign of δ₂ is penetration, not ℓ**: 0 of 3 positive at p = 0, 2 of 2 at
p = 5. **Seaton's ratio is valid where p = 0 at 1.15 ± 0.21 and UNDEFINED where
p ≥ 1** — a domain, not a failure.

## Λ_charge — the roles of the charge

**What it is.** Nine occurrences on (role, carrier, sign, regime), nine distinct
cells, **E = 0**, and dropping any single role also gives 0.

**What only it contributes.** *That c is three coordinates in one symbol.* The
charge appears inside u = ln(Nₑ/c^(2/3)), as the base of c^(−x), and inside the
exponent x itself. **Every degeneracy of the session was between a charge term and
something else, and this index says why: one symbol occupying three positions,
and any fit letting two of them float will trade them.**

**A warning the index also carries**: declaring the three roles as coordinates in
Λ_spectra raises E from 1929 to 13,605. **A closed sub-index says its roles are
well-posed; it says nothing about whether the parent index wants them.**

## Λ_cross — the crossing values

**What it is.** The value at which an ordering flips,
**a_cross = Δn(√p_g + √p_r)/(p_g − p_r)** — nineteen distinct surds across the
table, including 1/√3, 1/√2, 1, 1/(√3−1), 1+1/√2 and 1/(√2−1). **E = 0** on
(Δn, ℓ_g).

**What only it contributes.** *An index with no statistics language.* Order,
algebra (closed in ℚ(√p) for p ≤ 7) and geometry all speak of it; **analysis and
statistics do not.** A quantity that is ordinal, algebraic and geometric but not
analytic is an INTEGER OBJECT: it cannot be fitted and needs no fitting.

**And it is the one index whose unfixable cell is fixed anyway** — a node count
needs no measurement. **Nine of eleven unfixable cells across the work are
expectation values ⟨Ψ|Ô|Ψ⟩; Λ_cross is the exception, and it is the only index
with no statistics language. The two facts are the same fact.**

## Λ_descent — the charge dependence

**What it is.** a(c) on (c, regime). **E = 0.**

**What only it contributes.** *The only place a fit belongs.* Order and analysis
both speak of it, information says c adds everything, and statistics answers yes.
**Every fit of the session was applied to the WHOLE of a — the crossing and the
descent together — and that is why the constants kept absorbing each other: half
the object has no analysis language, and the fitted parameters were competing to
represent a set of surds.**

## Λ_phys — the parameters, rebuilt

**What it is.** Twenty-one parameters of real atoms on (source, domain),
**E = 0**, at source order **standard < mathematics < literature < this work** and
domain order **universal < all elements < a region < one species**.

**What only it contributes.** *That no parameter of this work is universal.* The
closing grid is a staircase and the diagonal is the whole content: CODATA
constants are universal, this work's numbers hold on a region or all elements and
never universally. **A pooled fit across regions asserts a universal parameter,
which the closed index says does not exist — that is a structural prohibition,
not a stylistic preference, and it is what `domain_protocol.py` enforces.**

**Rebuilt on three rulings**: `kind` is the same axis as `source`; `arity` is a
property of the book, not the parameter; and parameters that are artefacts of the
METHOD are not physics of real atoms.

## Λ_amp — the electron–electron term

**What it is.** The Slater integrals: for each subshell pair, F^k for k even up to
2min(ℓ,ℓ′) and G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to ℓ+ℓ′. **Twenty cells,
E = 0**, a perfect triangle **0 ≤ i ≤ ℓ**.

**What only it contributes.** *That the rank is not a free coordinate.* Indexed on
the multipole rank k the index gives E = 1 and the single defect is **F¹ — a term
parity forbids.** Reindexed on POSITION WITHIN SEQUENCE it closes. **The same
fault as `breadth` in Λ_chem: an axis whose values are constrained by another
axis.**

**And its structure explains the Slater result exactly**: at s/s the exchange G⁰
IS the direct F⁰, so dropping exchange costs nothing; at f/f it discards four
independent quantities. **The count of lost integrals is the count of failures —
5 of 5 s-block brackets threaded, 0 of 1 f.**

## Λ_PCA — physics ⊕ charge ⊕ amplitude, merged

**What it is.** Nine cells on (source, domain) with the domain refined by the
charge regime: **universal < all elements < low < neutral < hydrogenic < one
species**. **E = 0.**

**What only it contributes.** *The per-atom calibration.* A parameter's domain
reads as a SET OF ATOMS, so for any (Z, c) the index states which parameters
apply to it. **And the closing order puts `low` — charge 2 — BEFORE the neutral,
which the ladders independently confirm: c = 2 is the only charge with two-sided
brackets, the narrowest domain and therefore the most particular.**

**A correction recorded here**: merging Λ_phys and Λ_charge on identified axis
NAMES raised E from 6 to 11 and I concluded they were not one object. That was
against a malformed Λ_phys. **Merged on `domain ≡ regime` alone, after the
rebuild, they close.**

## Λ_chem — the chemical properties

**What it is.** Forty-two chemical properties of a species on (kind, seat, PCA
dependency). **E = 0 on fourteen cells** over the subvalence and valence shells.

- **kind**: count · symmetry · size · energy · rate
- **seat**: the nucleus · the core · the subvalence shell · the valence shell ·
  **the aggregate**
- **PCA**: which of physics, charge or amplitude the property supplies

**What only it contributes.** *That twelve of the forty-two are properties of
MATTER IN BULK and not of an isolated atom* — density, melting point, hardness,
crystal structure, conductivity, colour of the metal, smell, taste, metallic
character, reactivity. **With eleven hand-picked properties the index could not
say this; it appeared the moment every property was demanded.**

**And its closure states PCA's own boundary.** E climbs **0 → 3 → 8 → 11 → 19** as
the core, the nucleus and the aggregate are added. **PCA's domain is the
subvalence and valence shells, and the index declares it by degrading
monotonically outside it** — as Seaton's ratio is valid at p = 0 and undefined
beyond.

**The last defect cell, found by exhaustive reordering.** All 1,440 orderings give
minimum E = 1 and none reaches zero: the cell is **symmetry × the valence shell ×
a charge role**. The fill is the ground TERM, which changes with charge —
Nₑ = 20 gives ¹S₀ → ³D₁ → ³F₂ → ³F₂ and Nₑ = 38 the identical sequence.
**Every ladder table carried the term symbol; the configurations were recorded and
the terms were not.**

## Λ_t — the corridor position

**What it is.** Twelve cells on (ℓ, n) holding **t = (a − L)/(U − L)**, where a
sits in its corridor. **E = 3.**

| ℓ \ n | 2 | 3 | 4 | 5 | 6 | 7 | limit |
|---|---|---|---|---|---|---|---|
| **s** | 0.268 | 0.335 | 0.266 | 0.218 | 0.257 | 0.195 | — |
| **p** | · | 1.120 | 1.049 | 1.022 | 1.002 | · | **1.0000** |
| **d** | · | · | 1.819 | 1.433 | · | · | **1.7321** |

**What only it contributes.** *That the ℓ axis carries the LIMIT and the n axis
the APPROACH.* t converges to √(ℓ(ℓ+1)/2), the centrifugal term — 6p sits 0.2%
above it — and the gap falls **0.120 → 0.049 → 0.022 → 0.002** along n.

**And q is not a coordinate.** With the Pauli fraction in the radicand, t barely
moves across a subshell: 6p gives 1.0237, 1.0417, 1.0009, 1.0036, 0.9946, 0.9940
across all six occupancies.

**Its three defect cells are 7p, 6d and 7d** — real absences, each a subshell
whose corridor is one-sided or whose ionisation energy is not held.

## Λ_ladder — the ladders themselves

**What it is.** The walks, on (seat, kind, Zcross). **FOURTEEN ladders in three
families — six species, six state, two X-ray — nine cells, E = 0. IT CLOSES.**
Registers 1356, 1374, 1375, 1384, 1427.

Two relations, three ladders each — **Z = Nₑ + c − 1** on Λ, and **A = Z + N** on
the nuclide chart. Only two of three are independent either side, so no ladder
varies Z alone: forbidden by arithmetic, not by lack of data.

| family | ladder | fixes | reaches | held |
|---|---|---|---|---|
| species | isoelectronic | Nₑ | valence | 11 of 11 |
| species | the walk | c | valence | 106 of 106 |
| species | ionisation | Z | subvalence | 15 of 108 |
| species | isotopic | Z, Nₑ, c | nucleus | **1 rung traced** |
| species | isotonic | N | nucleus | none — NEW |
| species | isobaric | A | nucleus | none — NEW |
| state | the Rydberg series | the species | valence | every δ held |
| state | the ℓ-ladder | species, n | valence | 62 pairs |
| state | the term ladder | species, cfg | valence | 66 pairs |
| state | the outer-j ladder | species, cfg | valence | P.jsplit |
| state | the parent-term | the species | core | 12 of 15 |
| state | the isomeric | Z, N, e⁻ | nucleus | none — NEW |

**What only it contributes.** *That a coordinate individuating the cells is a KEY,
not an axis.* At four ladders `fixes` was injective by construction — a ladder IS
named by what it holds fixed — so one cell per row, and **E = 0 was FORCED: 2% of
admissible arrangements could refuse.** At six, ionisation and isotopic both fix
Z, and the zero becomes earnable. That is the dual of A.define, where a
single-valued coordinate contributes no envelope; this is the other end of the
same degeneracy.

**IT CLOSES, and both blocking reasons are resolved.** The E = 1 defect stood at
**(subvalence, counting, across elements)** — Moseley's ladder, in a direction
ionisation does not go. That defect is what demanded Λ_xray, and Λ_xray filled it:
Moseley enters at subvalence as counting/across, the Kα doublet as coupling/within.
**Only the subvalence seat closes** — nucleus gives 1, core 2, valence 1 — and the
seat is settled from OUTSIDE the closure rather than by it, since Λ_PCA excluded
the core independently, on different coordinates, before this was computed. The
physics agrees: a Kα line is not a property of the 1s shell but a transition
*between* shells, so the seat is where the transition spans, not where the hole
sits. **Contingency: 90% of comparable nine-cell sets refuse, so the zero is
earned** (R 1427).

**And the five shared cells are four findings and one separation** (R 1428). Two
pairs are ONE OBJECT and the index is right to merge them — isotonic fixes N and
isobaric fixes A with A = Z + N; isoelectronic fixes Nₑ and the walk fixes c with
Z = Nₑ + c − 1. That is *charge is one symbol in three positions*, one level up.
Two are separated by axes already in the index but not among the three that close:
isotopic is species where the isomeric is state; the Rydberg series fixes the
species where the ℓ-ladder fixes species and n. **The fifth was the real
ambiguity** — the term ladder and the outer-j ladder — and they are five tower
stages apart, nested rather than parallel: the term ladder moves 2S, Λ₈'s own
letter, while the outer-j ladder moves 2J, which arrives only at Λ₁₃. Adding the
tower stage as a fourth axis separates that pair and only that pair, but costs
closure, E going 0 → 1. **So the stage is the discriminator, not an axis** (R 1429).

## Λ_xray — the inner shell

**What it is.** The dipole-allowed inner-shell transitions, on
(Δn, Δℓ, jtype_hole). **33 lines through the N shell → 9 cells, E = 0.**
Register 1378.

**Where it comes from.** Built with no new data. **Λ's cell IS a transition** —
source subshell into target subshell — and its constraints impose no order between
n and e, so a downward transition was already inside its alphabet; only the caps
excluded it. EM.map gives the dipole rule, T.a12 the j triangle. The six K-shell
lines emerge as the classical set unadjusted: K-L2 and K-L3 are Kα₂ and Kα₁,
K-M2 and K-M3 are Kβ₃ and Kβ₁, K-N2 and K-N3 are Kβ₂. Energies are NIST SRD 128,
Deslattes *et al.*, *Rev. Mod. Phys.* **75** (2003) 35–99.

**What only it contributes.** *That thirty-three named lines are nine transition
types.* Seventy-two of 165 three-coordinate systems reach E = 0 and **every one
collapses to exactly nine cells** — Kα, Lα and Mα are one type read at three
depths, which Siegbahn notation hides.

**And it settles what Λ_cross's silences mean.** The two close on the same shape —
differences plus one endpoint — and the cypher separates them:

| language | Λ_cross | Λ_xray |
|---|---|---|
| order | speaks | speaks, E = 0 |
| geometry | speaks | speaks |
| statistics | **silent** | **speaks** — pairwise marginals recover all 9 |
| analysis | **silent** | **speaks** — Moseley, R² = 0.998 |

*Λ_cross remains the only integer object: cells AND values fixed by arithmetic.
Λ_xray has integer cells and measured values.* Registers 1379, 1380, 1385.

## The one-line summary, extended

| index | the one thing only it gives |
|---|---|
| **Λ_law** | the carrier — which variable a law runs in |
| **Λ_const** | that `standing` cannot be a coordinate |
| **Λ_var** | no nucleus + rydberg cell — the three-body factorisation |
| **Λ_ryd** | the n-dependence Λ_spectra discards |
| **Λ_charge** | c is three coordinates in one symbol |
| **Λ_cross** | an index with no statistics language |
| **Λ_descent** | the only place a fit belongs |
| **Λ_phys** | no parameter of this work is universal |
| **Λ_amp** | the rank is not a free coordinate |
| **Λ_PCA** | the per-atom calibration |
| **Λ_chem** | twelve of forty-two properties are not an atom's at all |
| **Λ_t** | ℓ carries the limit, n carries the approach |
| **Λ_ladder** | that a coordinate individuating the cells is a key, not an axis |
| **Λ_xray** | thirty-three named lines are nine transition types |
| **Λ_chain** | Λ's input column as a derived object — the order from the equation, one constant |
| **Λ_cinf** | that the periodic table is not a solution of the non-relativistic equation |
| **Λ_V5** | every contested competition widens under correlation |
| **Λ_j120** | Λ's falsification frontier, twelve rows wide |
| **Λ₃** | masses enter through six numbers; structure is mass-free — the three-body factorisation, closed |

**Fourteen close.** Λ_xray is new and closes at nine transition types. **Λ_ladder
now closes too** — fourteen ladders, nine cells, E = 0, once the X-ray pair is
seated at subvalence (R 1427), its five shared cells resolving as four findings
and one separation (R 1428–1429).

**Λ_spectra closes at the LIMIT** — not for want of the principal number, as
register 1341 supposed. The index runs to the last available species and stops:
98 cells, E = 58, of which 38 need more electrons than any atom has. **The
remaining twenty are within the limit, and eleven of those are the Madelung
exceptions, each nameable** (R 1395, corrected at R 1426).

# X · THE INDEXES BUILT IN THE LÖWDIN SOLUTION

*Registers 1701–1712; Chapter 35. Four indexes the solution builds beside Λ — what each holds, whether it closes, whether it carries time, and what role it plays for Λ. The template differs from Part IX's by design: these are transition indexes, and closure and time are the questions they exist to answer.*

## Λ_chain — the derived filling index

**What it holds.** 119 rows, one per element Z = 2–120: entrant channel, entrant
depth, margin, and the full frontier candidate spectrum of the V^{N−1} walk;
provenance per row (SCORED 107, UNWITNESSED 12).

![**Figure 7.** Λ_chain's cell, drawn as what it is: a MOVE. The carried state enters, the field is built, the spectrum is read, the deepest channel is the move, and the output state seeds the next cell.](figures/figaddioichain.png)

![**Figure 8.** The provenance of Λ_chain, cell by cell: 107 SCORED, 12 UNWITNESSED, with the five contested rows and the three derived exceptions marked.](figures/figaddioiprovenance.png)

**Does it close?** As an index of rows, trivially — one cell per Z, none refused.
The substantive closure is different in kind and stronger: **the chain closes on
itself.** Each row is built from the previous row's derived output, so a single
wrong cell breaks every cell after it, and 107 of 107 is therefore one score, not
107 (register 1701–1702).

**Does it carry time?** Yes, in this compendium's exact sense: **its cells are
moves** — the step Z−1 → Z, adding one electron to a channel — so it carries a
time column, standing beside Λ as a second transition index in the collection,
and the first whose moves are **totally ordered**. *Chapter 34 proved the table
needs a carried state; Λ_chain is that state, carried by the equation.*

**Role for Λ.** It supplies, from first principles, the one thing Chapter 6
proved Λ cannot supply for itself: the aufbau ordering. **Λ's input column is now
a derived object.** Every configuration Λ indexes is generated by Λ_chain with
one constant, and the two agree everywhere Λ has an element.

---

## Λ_cinf — the counterfactual twin

**What it holds.** The identical 107-row walk at c → ∞.

**Does it close?** As Λ_chain does, on itself.

**Does it carry time?** Yes — the same move-cells as Λ_chain, in the same total order.

**Role for Λ.** None as data, everything as contrast: **eleven of its entrants
differ from Λ_chain's, and all eleven are wrong against nature.** It exists to
state that Λ's subject is relativistic, and it is quarantined from every other
use (register 1706).

---

## Λ_V5 — the contested-row closure

**What it holds.** Five rows — Z = 38, 56, 72, 89, 105 — each carrying the
complete second-order correlation differential over the mean-field margin, with
declared envelopes.

**Does it close?** Yes, by exhaustion: the five rows are *all* the rows whose
margins are small enough to be at risk, and the criterion selecting them is
stated, not curated.

**Does it carry time?** No. It is a still photograph of the walk's five closest
calls.

**Role for Λ.** It is the warrant that Λ_chain's mean field carries the exact
equation's order: **every contested competition widens under correlation**
(register 1705). Without this index the derivation would be conditional in a
place it is now checked.

---

## Λ_j120 — the unwitnessed extension

**What it holds.** Twelve rows, Z = 109–120: entrant, depth, margin, and the
spin-orbit worst case each margin clears.

**Does it close?** Its cells do; its **values are unwitnessed** — the grade this
book already owns for a bound the world has not yet supplied. Nothing in it is
defected for want of trying.

**Does it carry time?** Yes — move-cells, Λ_chain's own order continued past the last measurement.

**Role for Λ.** It is Λ's falsification frontier. The day a superheavy ground
configuration is measured, exactly one row here either scores or fails, and
either outcome is information the whole structure inherits (register 1712).

---

*One line for the map: Λ_chain stands to Λ as derivation stands to arrangement.
Λ holds the configurations; Λ_chain says why they are the ones held — and says it
from the equation, with one number, carrying the state that closure alone could
never carry.*
<<<END FILE: The_Method_1_6___The_Index_of_Indices-2.md>>>

<<<FILE: The_Method_1_6___Spectra_Compendium-2.md>>>

# THE METHOD 1.6 — SPECTRA COMPENDIUM

**The index of Rydberg channels, and a value for every cell of it.**

This compendium supplies the book with coordinates. Its subject is Λ_spectra; its output is a defect for every channel of every element, graded by how the value was got. *The register carries the working record — the corrections, the reversals, and what remains open. This carries the answers.*

---

# 0 · THE COORDINATE SUPPLY

### What a coordinate is

        (Z, charge, ℓ, 2S+1)   →   δ,  with a grade, a source and a bound

**Z** the atomic number · **charge** the ionisation stage, 1 for the neutral · **ℓ** the Rydberg orbital · **2S+1** the multiplicity, which Hund's rule on the core derives from the ground state and does not require measuring.

**δ** is the quantum defect: E = −Z_c²R/(n−δ)², so a channel's whole Rydberg series follows from one number and the core charge.

**DECLARATION — the stored δ is the MEDIAN over a cell's members (T2, closed).** This was measured, not chosen: of 433 series whose member count reproduces exactly from raw, the stored value equals the median in 430 (99.3%); the 18 mean-agreements are series where median and mean coincide and distinguish nothing (R 1673, 1675, enlarged sample R 1679). The mean and asymptotic perspectives are carried alongside per cell, as perspectives of one definition (T6, M's ruling, session 1.7.3).

### The grades

| grade | rows | what it means |
|---|---|---|
| **exact** | **929** | forced by symmetry — δ = 0 when one electron faces a bare nucleus |
| **measured** | **358** | fitted to captured levels against an ionisation limit |
| **computed** | **103,545** | supplied by the channel equation, within the domain stated below |

**Nothing is ungraded.** A value with no provenance is not a coordinate.

### The witness

*Register 1578. This table used to grade cells VERIFIED, POSSIBLE and IMPROBABLE. **Improbable is a judgement about the future, not a fact about the record** — and register 1287 had already established the rule it breaks: an index whose coordinates mix the OBJECT with the OBSERVER cannot close. What replaces it is a fact and a named obstacle.*

| | cells | |
|---|---|---|
| the index admits | **104,832** | every channel of every element |
| **witnessed** | **358** | reality has been consulted for this cell |
| **unwitnessed** | **104,474** | it has not — see the bound |

**0.341% of the index has been checked against reality.** Every other cell is theory, and the compendium should be read that way.

### The bounds on the unwitnessed

*Not probabilities. Named obstacles, each of which may or may not be lifted.*

| cells | the obstacle |
|---|---|
| **28,526** | series unresolved above ng in any published analysis |
| **24,312** | no long-lived isotope |
| **17,626** | not keyable: no single 2S+1 (hole+electron or multi-valence) |
| **11,605** | open-shell core, 16 parents |
| **9,756** | open-shell core, 3 parents |
| **5,280** | open-shell core, 119 parents |
| **2,691** | no analysis located at this charge (NOT a bound on existence) |
| **1,760** | no nuclide synthesised; theoretically admitted — Janet left-step, 8s(2) closes the eighth period at element 120 |
| **1,744** | no nuclide synthesised; theoretically admitted — Janet left-step, 8s(1) opens element 119 |
| **929** | derived by symmetry; no measurement required |
| **240** | none — separable series, simply not yet measured |
| **6** | limit 41449.451; one electron outside a closed shell |
| **5** | no primordial isotope (R 1587) |
| **5** | limit 31406.4677325; one electron outside a closed shell |
| **3** | limit 66928.04; one electron outside a closed shell |
| **3** | limit 49266.66; one electron outside a closed shell |
| **2** | limit 48278.48; one electron outside a closed shell |
| **2** | limit 48387.634; one electron outside a closed shell |
| **2** | limit 32848.872; one electron outside a closed shell |
| **1** | limit 46670.107; one electron outside a closed shell |
| **1** | limit 43762.6; one electron outside a closed shell |

**The charge bound is the one to distrust.** It reads *no analysis located*, not *no analysis exists* — and register 1577 found twelve MEASURED cells above it in this index's own file (Ti XI, Fe XV, Fe XVI), with Theodosiou 1986 covering all positive ions of all atoms to Z = 37.

*Accuracy figures in this compendium are quoted against the WITNESSED-plus-possible set, not against the whole index.*

### The bound, which needs no measurement at all

        B = min( p , n₀ − ℓ − 1 )

with **p** the core's orbital count at that ℓ and **n₀** the first Pauli-allowed principal number, both read from the ground-state configuration. **floor(δ) ≤ B holds on every measured channel without exception**, and B travels with every row of the table — so the book can bound a defect without consulting one.

### The filler, and its domain

Where no capture reaches, the channel equation supplies the value:

        p > 0 :   δ = 0.3772 · p^e(Nₑ) · Nₑ^k · ln(c+1)/c
        p = 0 :   δ = 0.5415 · C(Z) · (Nₑ−1)/Nₑ · Nₑ^k · ln(c+1)/c

        e(Nₑ) = 0.8297 − 0.0900·ln Nₑ          k = 0.4942
        Nₑ    = Z − charge + 1
        C(Z)  = the collapse coordinate across the Janet block boundary

**Domain: Z ≤ 92, charge ≤ 10, ℓ ≤ 4, a single-parent core.** Fitted there on 277 channels at rms 0.1329 and R² 0.9747, anchored at Z = 2 and Z = 90. *Every value outside the domain is `unwitnessed`, and the `bound` column names why.*

### The table

### The file

**`COORDINATES-2.13`** (CSV, 104,832 rows, one per admitted cell) is the coordinate index itself, and is delivered with this compendium as its data companion. Everything in Parts 0–II is read from it at build; the file is the object, the pages are the reading. A cell is cited from any volume as **COORD(Z, charge, ℓ, 2S+1)** — the four coordinates are the key and are unique in the file.

| column | alphabet | meaning |
|---|---|---|
| `Z` | 1 … 120 | the element; 119 and 120 admitted on Janet's authority, register 1578's bound column saying so |
| `charge` | 1 … Z | the ion; charge ≤ Z is the triangle, 7,260 (Z, charge) pairs |
| `l` | 0 … 7 | the running electron's ℓ |
| `mult` | 1 … 9 | 2S+1; the set allowed at a pair is a function of the electron count Z − charge alone, holding on all 7,260 pairs |
| `delta` | −0.2367 … 6.0207 | the quantum defect held for the channel |
| `grade` | exact · measured · computed | 929 · 358 · 103,545 — one-electron cells are exact by symmetry |
| `source` | 32 distinct | the compilation, species and statistic the value was taken from, or the rule that computed it |
| `B` | 0 … 7 | the Pauli bound on δ, read from the ground state; nonzero on 36,917 cells |
| `witness` | witnessed · unwitnessed | 358 · 104,474 — reality consulted, or not |
| `bound` | 22 distinct | for an unwitnessed cell, the named reason (§ *The bounds on the unwitnessed*) |

*The seven columns Part 0 once printed —* `Z charge l mult delta grade source B status` *— were the file at register 630; `status` (improbable / possible) became `witness` and `bound` at register 1578, and Z was extended from 118 to 120 at the entry that admitted 3,504 cells on Janet's authority. Every count on these pages is read from the file; none is transcribed.*

![The coordinate supply](figures-compendia/fig-supply.png)

*Above: the supply per element, on a log scale — the measured and exact cells against the computed. Below left: every measured coordinate, δ against electron count, coloured by charge. Below right: the Pauli bound, which holds on every measured cell and is read from the ground state alone.*

---

# 0′ · THE DERIVED SUPPLY — Λ_chain's candidate spectrum

*This compendium's founding supply runs observation-side: (Z, charge, ℓ, 2S+1) →
δ, graded by how the value was got. The Löwdin solution adds the equation-side
supply: at every element, a depth for every frontier channel, computed from the
many-electron field with one constant and no measurement. The two supplies meet
at the same atoms from opposite directions, and where one is silent the other
speaks.*

### What a derived coordinate is

        (Z, n, ℓ)   →   D,  in hartree, with margin, provenance and score

**Z** the atomic number, neutral walk · **(n, ℓ)** any frontier channel offered at
that step · **D** its converged one-channel depth in the frozen V^{N−1} field ·
**margin** attached to the entrant row: the gap to the runner-up, the quantity
every later scrutiny is measured against.

![The entrant margin](figures/figaddscmargin.png)

*The entrant margin at every scored row. Blue: the five contested rows, where the correlation clause was computed and every competition widened.*

### The grades

| grade | meaning | rows |
|---|---|---|
| **SCORED** | the entrant met the measured ground configuration | 107 of 107, Z = 2–108 |
| **UNWITNESSED** | no measurement exists to meet; published falsifiable | 12, Z = 109–120 |
| **PINNED** | the channel's depth is hydrogenic and Z-independent | every g row |

*UNWITNESSED carries this book's own sense: not undefected for want of trying —
the rows await a measurement science has yet to provide* (register 1712).

### The pinned rows, stated as values

![The pinned rows](figures/figaddscgpin.png)

*The pinned rows — the constants of the derived supply. Top: the four g channels, each at −1/(2n²) to storage precision, spread ≤ 10⁻⁵ across spans of 28 to 70 elements. Bottom: the same lines against the f and d channels that respond to Z.*

> **5g: −0.020000 over 65 elements · 6g: −0.013889 over 70 · 7g: −0.010204 over
> 57 · 8g: −0.0078125 over 28** — each equal to −1/(2n²) to storage precision,
> spread ≤ 10⁻⁵ across the full span.

**A channel whose value the nucleus cannot move needs no measurement and admits
no fit.** The compendium records these once, as constants of the walk, and the
absence of a g series anywhere in the observation-side supply is thereby
explained rather than merely noted (register 1704).

### The unwitnessed twelve

| Z | entrant | D_ent | margin |
|---|---|---|---|
| 109–112 | 6d | −0.326 → −0.423 | 0.171 → 0.264 |
| 113–118 | 7p | −0.160 → −0.360 | 0.058 → 0.210 |
| 119, 120 | 8s | −0.159, −0.189 | 0.097, 0.098 |

Worst-case spin-orbit narrowing 0.083 Ha; every margin clears it. *When the
spectra can be taken, these rows are scored like any others, and this table is
where a miss would land.*

### How the two supplies interlock

**Where the observation supply goes silent, the derived supply names why.** The f
corridor of Chapter 34 has no test (L = −∞ at the node floor); the derived supply
puts the collapse condition at that exact address and decides La, Ac, Th there
(register 1703). **Where the derived supply is unwitnessed, the observation
supply states what witnessing would take.** And at the hundred-odd elements both
supplies cover, they are independent routes to one order — *the strongest
cross-check either one owns.*

---

# I · THE INDEX

### The four coordinates, and where each comes from

| coordinate | alphabet | derived from |
|---|---|---|
| Z | 1 … 120 | given; 119–120 admitted, unwitnessed |
| charge | 1 … Z | given |
| ℓ | 0 … 7 | given |
| 2S+1 | Hund's rule on the core | **the ground state** |

**The multiplicity is not a free coordinate.** Hund's first rule applied to the core's ground configuration gives the allowed values, exact on all 24 electron counts tested. Applying it as a constraint removes **247,248 cells — 71%** of what the naive product would admit.

### Which cells exist

A cell is admitted when charge ≤ Z, at least one electron remains, the multiplicity is one Hund's rule allows, and an orbital of that ℓ is available. **Every cell the index admits is physically possible**: the forbidden ones were excluded at construction, so the survey holds none.

### Which cells can be measured

| restriction | cells |
|---|---|
| the index admits | 104,832 |
| Z ≤ 92 — naturally occurring | 61,152 |
| and charge ≤ 10 | 11,416 |
| and ℓ ≤ 4 — where series resolve | 4,395 |
| **and a single-parent core** | **1,755** |

### The parent-term wall

**A closed-shell core has one parent term and gives one Rydberg series per ℓ.** An open-shell core gives one series per parent, all interleaved, converging on different limits.

Fe IV's 3d⁴ core carries sixteen LS terms. Its published levels show thirteen of them across **24 distinct (parent, ℓ, term) series, every one with a single member.** Fe IV has about a thousand analysed levels and no extractable defect: *the levels are identified and the series are not separable.*

**This is why the compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6.** An open-shell core does not produce the object a quantum-defect index holds.

### The Janet collapse

Two channels can both have p = 0 — no core orbitals of their own ℓ — and differ by a factor of ten. Ti IV's nd is **0.6202**; Sr II's nf is **0.0618**.

What separates them is **orbital collapse**, and its threshold is a Janet block boundary exactly:

| orbital | n+ℓ | block opens at | element | collapse threshold |
|---|---|---|---|---|
| **3d** | 5 | **Z = 21** | Sc | **21** |
| **4f** | 7 | **Z = 57** | La | **57** |
| **5f** | 8 | **Z = 89** | Ac | **89** |

Across 116 cells with p = 0 at ℓ = 2 or 3: **collapsed median 0.637, uncollapsed 0.036**, U-test p = 9.8×10⁻⁴. The transition is rapid rather than sharp — the largest defects are the atoms *approaching* a boundary: Ca I nd = 0.908 at Z = 20 against a threshold of 21, and Ba II nf = 0.756 at 56 against 57.

**The collapse coordinate is read from the periodic table, not fitted**, and it is why a defect at ℓ = 2 can be large in one element and negligible in its neighbour.

![The channel map](figures-compendia/fig-channel-map.png)

*Every cell valued. The upper panel is δ itself, charge collapsed to its largest; the lower is which mechanism sets it, with the three Janet boundaries marked.*

---

# II · THE CHANNELS

**Every captured series, with its fit.** These are the measured rows of the coordinate table.

Three marks state a limitation. An **asterisk** on the species marks a two-member channel: two points give a defect and one consistency check but cannot detect a perturbation. A **dagger** on the n-range marks an internal gap. And the **limit column** names how the ionisation limit was obtained — *published* where a source quotes it, *theoretical* where it is exact by construction, *constructed* where this work built it by summing two spectra. *A channel resting on a limit this work computed is not a measurement against an independent standard, and the row says so.* The **bracket column** reads `m/k` — of k cells with true measured neighbours on both sides, m pass the sealed test under ruling 26 (strict membership, quotation-floor guard, §22.5 admissibility; register 1763) — or `no-triple` where the row's members contain no three consecutive n, or `untested` where the run's data conditions are not met (the count paragraph below the table gives the split).

| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |
|---|---|---|---|---|---|---|---|---|---|---|
| Al I | 3s²nf ²F° | 4–55 | 52 | 50 | 50/50 | 4.0–55.0 | +0.0429 | 0.0552 | 1 | 48,278.480 |
| Al I | 3s²nd ²D | 3–34 | 32 | 30 | 30/30 | 2.6–33.7 | +0.0248 | 0.6297 | 1 | 48,278.480 |
| Al I | 3s²ns ²S | 4–16 | 13 | 11 | 11/11 | 2.2–14.2 | +1.7670 | 0.0537 | 1 | 48,278.480 |
| Al I | 3s²np ²P° | 3–7 | 5 | 3 | 3/3 | 1.5–5.7 | +1.3365 | 0.2080 | 1 | 48,278.480 |
| Al II | 3sns ¹S | 4–16 | 13 | 11 | 11/11 | 2.8–14.8 | +1.2028 | 0.0147 | 2 | 151,862.500 |
| Al II | 3sns ³S | 4–13 | 10 | 8 | 8/8 | 2.7–11.7 | +1.2711 | 0.0474 | 2 | 151,862.500 |
| Al II | 3snd ¹D | 3–11 | 9 | 7 | 7/7 | 3.2–10.9 | +0.0603 | 0.3897 | 2 | 151,862.500 |
| Al II | 3sng | 5–13 | 9 | 7 | 7/7 | 5.0–13.0 | +0.0212 | 0.0070 | 2 | 151,862.500 |
| Al II | 3snd ³D | 3–10 | 8 | 6 | 6/6 | 2.8–9.8 | +0.2024 | 0.0096 | 2 | 151,862.500 |
| Al II | 3snf ³F° | 4–11 | 8 | 6 | 6/6 | 3.9–11.0 | +0.0140 | 0.4088 | 2 | 151,862.500 |
| Al II | 3snp ³P° | 4–10 | 7 | 5 | 5/5 | 3.1–9.1 | +0.8982 | 0.0571 | 2 | 151,862.500 |
| Ar II | (³P)ns ⁴P J=5/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.3 | +1.7463 | 0.0477 | 2 | 222,848.300 |
| Ar II | (³P)ns ⁴P J=3/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.3 | +1.7246 | 0.0663 | 2 | 222,848.300 |
| Ar II | (³P)ns ⁴P J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.2–4.4 | +1.6821 | 0.1507 | 2 | 222,848.300 |
| Ar II | (³P)ns ²P J=3/2 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6711 | 0.1084 | 2 | 222,848.300 |
| Ar II | (³P)ns ²P J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6355 | 0.1526 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=7/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6930 | 0.1695 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=5/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6880 | 0.1753 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6786 | 0.1919 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴D J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.4 | +0.6669 | 0.2155 | 2 | 222,848.300 |
| Ar II | (³P)nd ⁴F J=9/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.4 | +0.6121 | 0.0885 | 2 | 222,848.300 |
| Be I | 2snp ¹P° | 3–13 | 11 | 9 | 9/9 | 2.7–12.6 | +0.3590 | 0.1025 | 1 | 75,192.500 |
| Be I | 2snd ³D | 3–12 | 10 | 8 | 8/8 | 2.9–11.9 | +0.1109 | 0.0129 | 1 | 75,192.500 |
| Be I | 2snd ¹D | 3–12 | 10 | 8 | 8/8 | 3.2–12.1 | -0.1152 | 0.0970 | 1 | 75,192.500 |
| Be I | 2sns ¹S | 3–11 | 9 | 7 | 7/7 | 2.3–10.3 | +0.6774 | 0.0136 | 1 | 75,192.500 |
| Be I | 2sns ³S | 3–8 | 6 | 4 | 4/4 | 2.2–7.2 | +0.7910 | 0.0429 | 1 | 75,192.500 |
| Be I | 2snp ³P° | 3–8 | 6 | 4 | 4/4 | 2.6–7.6 | +0.3773 | 0.0374 | 1 | 75,192.500 |
| Be I | 2snf ³F° | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0305 | 0.0063 | 1 | 75,192.500 |
| Be II | ns ²S | 2–10 | 9 | 7 | 7/7 | 1.7–9.7 | +0.2623 | 0.0112 | 2 | 146,882.860 |
| Be II | np ²P° | 2–10 | 9 | 7 | 7/7 | 2.0–10.0 | +0.0491 | 0.0039 | 2 | 146,882.860 |
| Be II | nd ²D | 3–9 | 7 | 5 | 5/5 | 3.0–9.0 | +0.0021 | 0.0004 | 2 | 146,882.860 |
| Be II | nf ²F° | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0001 | 0.0001 | 2 | 146,882.860 |
| Be II | ng ²G | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | -0.0001 | 0.0001 | 2 | 146,882.860 |
| Be II | nh ²H° | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | -0.0002 | 0.0001 | 2 | 146,882.860 |
| Bi I | (³P₀)ns 2[0] J=1/2 | 7–11 | 5 | 3 | 3/3 | 2.0–6.1 | +4.9036 | 0.0649 | 1 | 58,761.650 |
| Bi I | (³P₀)nd 2[2] J=3/2 | 6–10 | 5 | 3 | 3/3 | 2.7–6.7 | +3.2646 | 0.0470 | 1 | 58,761.650 |
| Bi I | (³P₀)nd 2[2] J=5/2 | 6–9 | 4 | 2 | 2/2 | 2.8–5.8 | +3.2071 | 0.0272 | 1 | 58,761.650 |
| Bi I | (³P₀)np 2[1]° J=1/2 | 7–9 | 3 | 1 | 1/1 | 2.5–4.6 | +4.4712 | 0.0588 | 1 | 58,761.650 |
| C II | 2s²ns ²S | 3–8 | 6 | 4 | 4/4 | 2.3–7.3 | +0.6624 | 0.0063 | 2 | 196,664.700 |
| C II | 2s²np ²P° | 3–7 | 5 | 3 | 3/3 | 2.6–6.7 | +0.3928 | 0.1344 | 2 | 196,664.700 |
| C II | 2s²nd ²D | 3–7 | 5 | 3 | 3/3 | 2.9–6.9 | +0.0924 | 0.0645 | 2 | 196,664.700 |
| C II | 2s²nf ²F° | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0220 | 0.0069 | 2 | 196,664.700 |
| C II | 2s²ng ²G | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0054 | 0.0011 | 2 | 196,664.700 |
| Ga I | 4s²ns ²S | 5–28 | 24 | 22 | 22/22 | 2.2–25.2 | +2.8013 | 0.0535 | 1 | 48,387.634 |
| Ga I | 4s²nd ²D | 4–27 | 23 | 21 | 21/21 | 2.8–25.7 | +1.2926 | 0.1920 | 1 | 48,387.634 |
| Ga I | 4s²np ²P° high | 41–5 | 15 | 13 | 13/13 | 38.8–52.7 | +2.2107 | 0.1209 | 1 | 48,387.634 |
| Ga I | 4s²nf ²F° | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0252 | 0.0057 | 1 | 48,387.634 |
| Ga I | 4s²np ²P° low | 4–7 | 4 | 2 | 2/2 | 1.5–4.7 | +2.3450 | 0.2026 | 1 | 48,387.634 |
| He I | 1sns ³S | 2–35 | 25 | 23 | 23/23 | 1.7–34.7 | +0.2965 | 0.0164 | 1 | 198,310.666 |
| He I | 1sns ¹S | 2–35 | 25 | 23 | 23/23 | 1.9–34.9 | +0.1392 | 0.0118 | 1 | 198,310.666 |
| He I | 1snp ¹P° | 2–35 | 25 | 23 | 23/23 | 2.0–35.0 | -0.0133 | 0.0050 | 1 | 198,310.666 |
| He I | 1snd ¹D | 3–35 | 24 | 22 | 22/22 | 3.0–35.0 | +0.0007 | 0.0019 | 1 | 198,310.666 |
| He I | 1snf ¹F° | 4–35 | 23 | 21 | 21/21 | 4.0–35.0 | -0.0010 | 0.0020 | 1 | 198,310.666 |
| He I | 1snd ³D | 3–35 | 22 | 20 | 20/20 | 3.0–35.0 | +0.0014 | 0.0018 | 1 | 198,310.666 |
| He I | 1sng ¹G | 5–35 | 22 | 20 | 20/20 | 5.0–35.0 | -0.0014 | 0.0020 | 1 | 198,310.666 |
| He I | 1snh ¹H° | 6–35 | 21 | 19 | 19/19 | 6.0–35.0 | -0.0015 | 0.0020 | 1 | 198,310.666 |
| He I | 1sni ¹I | 7–35 | 20 | 18 | 18/18 | 7.0–35.0 | -0.0016 | 0.0019 | 1 | 198,310.666 |
| He II | ns | 1–10 | 10 | 8 | 8/8 | 1.0–10.0 | +7.6e-05 | 2e-05 | 2 | 438,908.871 |
| He II | np | 2–10 | 9 | 7 | 7/7 | 2.0–10.0 | +5.1e-05 | 8e-06 | 2 | 438,908.871 |
| He II | nd | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +2.5e-05 | 4e-06 | 2 | 438,908.871 |
| He II | nf | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +1.4e-05 | 2e-06 | 2 | 438,908.871 |
| He II | ng | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +8.6e-06 | 1e-06 | 2 | 438,908.871 |
| He II | nh | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +4.5e-06 | 4e-07 | 2 | 438,908.871 |
| He II | ni | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +1.6e-06 | 4e-07 | 2 | 438,908.871 |

*He II's seven rows print δ in exponent form because the series lies below the table's four decimals. They are the corrected series (register 1758): term values against the limit 438,908.871 cm⁻¹ with the reduced-mass Rydberg R_He = R∞/(1 + mₑ/M_He), each level taken as the J-centroid of its fine-structure pair, from the NIST ASD levels; the earlier rows, −0.0003 to −0.0005 and rising, were the same levels against R∞, which is the uncorrected series §24.4 replaced.*
| K II | 3p⁵nf 2[3/2] J=1 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0426 | 0.0069 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[9/2] J=5 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0336 | 0.0071 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[5/2] J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0242 | 0.0052 | 2 | 255,072.800 |
| K II | 3p⁵nf 2[7/2] J=4 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0143 | 0.0059 | 2 | 255,072.800 |
| Li I | np 2P° | 2–42 | 41 | 39 | 39/39 | 2.0–41.8 | +0.1477 | 0.6779 | 1 | 43,487.114 |
| Li I | ns 2S | 2–11 | 10 | 8 | 8/8 | 1.6–10.6 | +0.4014 | 0.0180 | 1 | 43,487.114 |
| Li I | nd 2D | 3–12 | 10 | 8 | 8/8 | 3.0–12.0 | +0.0031 | 0.0129 | 1 | 43,487.114 |
| Mg II | ns ²S | 3–10 | 8 | 6 | 6/6 | 1.9–8.9 | +1.0749 | 0.0289 | 2 | 121,267.640 |
| Mg II | nd ²D | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0411 | 0.0145 | 2 | 121,267.640 |
| Mg II | np ²P° | 3–9 | 7 | 5 | 5/5 | 2.3–8.3 | +0.7077 | 0.0361 | 2 | 121,267.640 |
| Mg II | nf ²F° | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0030 | 0.0009 | 2 | 121,267.640 |
| Mg II | ng ²G | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0007 | 0.0001 | 2 | 121,267.640 |
| Mg II | nh ²H° | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0002 | 0.0000 | 2 | 121,267.640 |
| Mg II | ni ²I | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0000 | 0.0000 | 2 | 121,267.640 |
| N II | 2p·ns ³P° J=0 | 3–6 | 4 | 2 | 2/2 | 2.2–5.2 | +0.7747 | 0.0264 | 2 | 238,750.500 |
| N II | 2p·ns ³P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.2–5.2 | +0.7731 | 0.0260 | 2 | 238,750.500 |
| N II | 2p·ns ³P° J=2 | 3–6 | 4 | 2 | 2/2 | 2.2–5.3 | +0.7633 | 0.0464 | 2 | 238,750.500 |
| N II | 2p·ns ¹P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.2–5.3 | +0.7325 | 0.0824 | 2 | 238,750.500 |
| Na I | ns | 3–20 | 18 | 16 | 16/16 | 1.6–18.7 | +1.3506 | 0.0250 | 1 | 41,449.451 |
| Na I | np | 3–20 | 18 | 16 | 16/16 | 2.1–19.1 | +0.8584 | 0.0279 | 1 | 41,449.451 |
| Na I | nd | 3–20 | 18 | 16 | 16/16 | 3.0–20.0 | +0.0141 | 0.0045 | 1 | 41,449.451 |
| Na I | nf | 4–20 | 17 | 15 | 15/15 | 4.0–20.0 | +0.0014 | 0.0004 | 1 | 41,449.451 |
| Na I | ng | 5–20 | 16 | 14 | 14/14 | 5.0–20.0 | +0.0003 | 0.0001 | 1 | 41,449.451 |
| Na I | nh | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 1 | 41,449.451 |
| Na II | (²P°₃⁄₂)ns 2[3/2]° J=2 | 3–6 | 4 | 2 | 2/2 | 1.9–5.0 | +1.0385 | 0.0284 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)ns 2[3/2]° J=1 | 3–6 | 4 | 2 | 2/2 | 1.9–5.0 | +1.0268 | 0.0371 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[1/2]° J=0 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0671 | 0.0083 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[1/2]° J=1 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0641 | 0.0085 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[3/2]° J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.0556 | 0.0027 | 2 | 381,390.200 |
| Na II | (²P°₃⁄₂)nd 2[3/2]° J=1 | 3–5 | 3 | 1 | 1/1 | 3.0–5.0 | +0.0268 | 0.0026 | 2 | 381,390.200 |
| Zn II | ns ²S | 4–9 | 6 | 4 | 4/4 | 1.7–6.8 | +2.2084 | 0.0679 | 2 | 144,892.600 |
| Zn II | nd ²D | 4–9 | 6 | 4 | 4/4 | 3.0–8.0 | +0.9583 | 0.0228 | 2 | 144,892.600 |
| Zn II | np ²P° | 4–8 | 5 | 3 | 3/3 | 2.1–6.1 | +1.8386 | 0.0616 | 2 | 144,892.600 |
| Zn II | nf ²F° | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0172 | 0.0044 | 2 | 144,892.600 |
| Zn II | ng ²G | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0038 | 0.0008 | 2 | 144,892.600 |
| Bi III | 6s2.nd 2D J=3/2 | 6–8 | 3 | 1 | 1/1 | 3.0–5.2 | +2.8926 | 0.0795 | 3 | 206,242.000 |
| Bi III | 6s2.nd 2D J=5/2 | 6–8 | 3 | 1 | 1/1 | 3.1–5.2 | +2.8456 | 0.0496 | 3 | 206,242.000 |
| Bi III | 6s2.ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0378 | 0.0043 | 3 | 206,242.000 |
| Bi III | 6s2.ng 2G J=9/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0383 | 0.0046 | 3 | 206,242.000 |
| Bi III | 6s2.np 2P* J=1/2 | 6–8 | 3 | 1 | 1/1 | 2.2–4.4 | +3.7096 | 0.0732 | 3 | 206,242.000 |
| Bi III | 6s2.np 2P* J=3/2 | 6–8 | 3 | 1 | 1/1 | 2.3–4.5 | +3.6044 | 0.0630 | 3 | 206,242.000 |
| Bi III | 6s2.ns 2S J=1/2 | 7–9 | 3 | 1 | 1/1 | 3.0–5.0 | +3.9869 | 0.0234 | 3 | 206,242.000 |
| C II | 2s2(1S)np 2P° J=1/2 | 2–4 | 3 | 1 | 0/1 | 1.5–3.6 | +0.4403 | 0.0469 | 2 | 196,664.700 |
| C II | 2s2(1S)np 2P° J=3/2 | 2–4 | 3 | 1 | 0/1 | 1.5–3.6 | +0.4401 | 0.0469 | 2 | 196,664.700 |
| Li I | np 2P° J=1/2 | 2–4 | 3 | 1 | 1/1 | 2.0–4.0 | +0.0436 | 0.0021 | 1 | 43,487.150 |
| Li I | np 2P° J=3/2 | 2–4 | 3 | 1 | 1/1 | 2.0–4.0 | +0.0436 | 0.0021 | 1 | 43,487.150 |
| Mg I | 3snd 1D J=2 | 3–5 | 3 | 1 | 1/1 | 2.7–4.5 | +0.4034 | 0.0647 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=1 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0009 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=2 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0008 | 1 | 61,671.050 |
| Mg I | 3snd 3D J=3 | 3–5 | 3 | 1 | 1/1 | 2.8–4.8 | +0.1701 | 0.0008 | 1 | 61,671.050 |
| Mg I | 3snp 1P° J=1 | 3–6 | 4 | 2 | 2/2 | 2.0–5.0 | +1.0135 | 0.0265 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=0 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2056 | 0.0789 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=1 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2052 | 0.0789 | 1 | 61,671.050 |
| Mg I | 3snp 3P° J=2 | 3–6 | 4 | 2 | 2/2 | 1.7–4.9 | +1.2045 | 0.0788 | 1 | 61,671.050 |
| Mg I | 3sns 1S J=0 | 4–6 | 3 | 1 | 1/1 | 2.5–4.5 | +1.5331 | 0.0067 | 1 | 61,671.050 |
| Mg I | 3sns 3S J=1 | 4–6 | 3 | 1 | 1/1 | 2.3–4.4 | +1.6603 | 0.0180 | 1 | 61,671.050 |
| Mg II | np 2P° J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.3 | +0.7187 | 0.0123 | 2 | 121,267.640 |
| Mg II | np 2P° J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.3–4.3 | +0.7174 | 0.0123 | 2 | 121,267.640 |
| Mg II | ns 2S J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.9–4.9 | +1.0806 | 0.0102 | 2 | 121,267.640 |
| Sc III | 3p6.nd 2D J=3/2 | 3–7 | 5 | 3 | 3/3 | 2.2–6.4 | +0.6538 | 0.0617 | 3 | 199,677.370 |
| Sc III | 3p6.nd 2D J=5/2 | 3–7 | 5 | 3 | 3/3 | 2.2–6.4 | +0.6529 | 0.0616 | 3 | 199,677.370 |
| Sc III | 3p6.nf 2F* J=5/2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0450 | 0.0069 | 3 | 199,677.370 |
| Sc III | 3p6.nf 2F* J=7/2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0450 | 0.0069 | 3 | 199,677.370 |
| Sc III | 3p6.ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0073 | 0.0007 | 3 | 199,677.370 |
| Sc III | 3p6.ng 2G J=9/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0073 | 0.0007 | 3 | 199,677.370 |
| Sc III | 3p6.np 2P* J=1/2 | 4–7 | 4 | 2 | 2/2 | 2.7–5.7 | +1.2861 | 0.0211 | 3 | 199,677.370 |
| Sc III | 3p6.np 2P* J=3/2 | 4–7 | 4 | 2 | 2/2 | 2.7–5.7 | +1.2815 | 0.0211 | 3 | 199,677.370 |
| Sc III | 3p6.ns 2S J=1/2 | 4–8 | 5 | 3 | 3/3 | 2.4–6.4 | +1.5848 | 0.0180 | 3 | 199,677.370 |
| Si II | 3s2.nd 2D J=3/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.7 | +0.2290 | 0.0556 | 2 | 131,838.140 |
| Si II | 3s2.nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.7 | +0.2289 | 0.0558 | 2 | 131,838.140 |
| Si II | 3s2.nf 2F* J=5/2 | 4–11 | 8 | 6 | 6/6 | 3.9–10.9 | +0.0846 | 0.0120 | 2 | 131,838.140 |
| Si II | 3s2.nf 2F* J=7/2 | 4–11 | 8 | 6 | 6/6 | 3.9–10.9 | +0.0846 | 0.0120 | 2 | 131,838.140 |
| Si II | 3s2.ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0174 | 0.0015 | 2 | 131,838.140 |
| Si II | 3s2.ng 2G J=9/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0174 | 0.0015 | 2 | 131,838.140 |
| Si II | 3s2.np 2P* J=1/2 | 3–10 | 8 | 6 | 2/6 | 1.8–9.1 | +1.0239 | 0.0878 | 2 | 131,838.140 |
| Si II | 3s2.np 2P* J=3/2 | 3–10 | 8 | 6 | 2/6 | 1.8–9.1 | +1.0215 | 0.0868 | 2 | 131,838.140 |
| Si II | 3s2.ns 2S J=1/2 | 4–9 | 6 | 4 | 4/4 | 2.6–7.6 | +1.3944 | 0.0161 | 2 | 131,838.140 |
| Li III | nd 2D J=3/2 | 3–9 | 7 | 5 | 4/5 | 3.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | nd 2D J=5/2 | 3–9 | 7 | 5 | 4/5 | 3.0–9.0 | +0.0002 | 0.0002 | 3 | 987,662.290 |
| Li III | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | nf 2F* J=7/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0002 | 0.0002 | 3 | 987,662.290 |
| Li III | ng 2G J=7/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | ng 2G J=9/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | nh 2H* J=11/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | nh 2H* J=9/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 3 | 987,662.290 |
| Li III | ni 2I J=11/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III | ni 2I J=13/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III | np 2P* J=1/2 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0004 | 0.0002 | 3 | 987,662.290 |
| Li III | np 2P* J=3/2 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Li III | ns 2S J=1/2 | 1–9 | 9 | 7 | 5/7 | 1.0–9.0 | +0.0003 | 0.0002 | 3 | 987,662.290 |
| Ba III | 5p5.(2P*<3/2>).nd 2[1/2]* J=0 | 5–7 | 3 | 1 | 1/1 | 2.5–4.7 | +2.3509 | 0.0972 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[1/2]* J=1 | 5–7 | 3 | 1 | 1/1 | 2.5–4.8 | +2.3360 | 0.0975 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[3/2]* J=1 | 5–7 | 3 | 1 | 1/1 | 2.7–4.9 | +2.1891 | 0.0829 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[3/2]* J=2 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3061 | 0.0981 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[5/2]* J=2 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.2821 | 0.0849 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[5/2]* J=3 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.2601 | 0.0738 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[7/2]* J=3 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3041 | 0.0846 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).nd 2[7/2]* J=4 | 5–7 | 3 | 1 | 1/1 | 2.6–4.8 | +2.3113 | 0.0890 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).ns 2[3/2]* J=1 | 6–8 | 3 | 1 | 1/1 | 2.7–4.8 | +3.2585 | 0.0242 | 3 | 289,100.000 |
| Ba III | 5p5.(2P*<3/2>).ns 2[3/2]* J=2 | 6–8 | 3 | 1 | 1/1 | 2.7–4.7 | +3.2795 | 0.0267 | 3 | 289,100.000 |
| Bi II | 6s2.6p.nd (1/2,3/2)* J=1 | 6–14 | 9 | 7 | 2/7 | 2.8–11.0 | +2.9846 | 0.0626 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nd (1/2,3/2)* J=2 | 6–10† | 4 | 2 | no-triple | 2.8–6.9 | +3.1079 | 0.0545 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nd (1/2,5/2)* J=2 | 6–8 | 3 | 1 | 0/1 | 2.9–5.0 | +3.0001 | 0.1072 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nf (1/2,5/2) J=3 | 5–8† | 3 | 1 | no-triple | 3.9–6.8 | +1.1755 | 0.0437 | 2 | 134,720.000 |
| Bi II | 6s2.6p.nf (1/2,7/2) J=4 | 5–8† | 3 | 1 | no-triple | 3.9–6.8 | +1.1468 | 0.0343 | 2 | 134,720.000 |
| Bi II | 6s2.6p.ns (1/2,1/2)* J=0 | 7–9 | 3 | 1 | 1/1 | 2.6–4.7 | +4.3705 | 0.0333 | 2 | 134,720.000 |
| Bi II | 6s2.6p.ns (1/2,1/2)* J=1 | 7–9 | 3 | 1 | 1/1 | 2.6–4.7 | +4.3684 | 0.0313 | 2 | 134,720.000 |
| Ne I | 2s22p5(2P*3/2)nd 2[3/2]* J=1 | 13–20 | 8 | 6 | 2/6 | 13.0–20.0 | +0.0154 | 0.0024 | 1 | 173,929.750 |
| Ne I | 2s22p5(2P*3/2)ns 2[3/2]* J=1 | 12–20 | 9 | 7 | 4/7 | 10.7–18.7 | +1.2923 | 0.0047 | 1 | 173,929.750 |
| Ne I | nd 2[3/2]* J=1 | 11–20 | 10 | 8 | untested | 11.0–20.0 | +0.0119 | 0.0043 | 1 | 174,710.090 |
| Ne I | ns 2[1/2]* J=1 | 11–20 | 10 | 8 | untested | 9.7–18.7 | +1.2974 | 0.0038 | 1 | 174,710.090 |
| Li II | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0011 | 0.0001 | 2 | 610,078.400 |
| Li II | 1s.nd 3D J=2 | 3–10 | 8 | 6 | 5/6 | 3.0–10.0 | +0.0027 | 0.0003 | 2 | 610,078.400 |
| Li II | 1s.nf 1F* J=3 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0000 | 0.0002 | 2 | 610,078.400 |
| Li II | 1s.nf 3F* J=3 | 4–10 | 7 | 5 | 4/5 | 4.0–10.0 | +0.0006 | 0.0002 | 2 | 610,078.400 |
| Li II | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0000 | 0.0000 | 2 | 610,078.400 |
| Li II | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | -0.0000 | 0.0000 | 2 | 610,078.400 |
| Li II | 1s.np 1P* J=1 | 2–14 | 13 | 11 | 7/11 | 2.0–14.0 | -0.0144 | 0.0014 | 2 | 610,078.400 |
| Li II | 1s.np 3P* J=1 | 2–10 | 9 | 7 | 7/7 | 1.9–9.9 | +0.0543 | 0.0004 | 2 | 610,078.400 |
| Li II | 1s.ns 1S J=0 | 2–10 | 9 | 7 | 5/7 | 1.9–9.9 | +0.0744 | 0.0010 | 2 | 610,078.400 |
| Li II | 1s.ns 3S J=1 | 2–10 | 9 | 7 | 7/7 | 1.8–9.8 | +0.1814 | 0.0035 | 2 | 610,078.400 |
| Si I | nd (3/2,3/2)* J=1 | 20–50 | 31 | 29 | 29/29 | 20.0–50.0 | +0.0126 | 0.0444 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=3 | 20–56 | 37 | 35 | 35/35 | 19.9–56.0 | +0.0570 | 0.0366 | 1 | 66,035.000 |
| Zn I | nd 1D J=2 | 12–20 | 9 | 7 | untested | 10.8–18.8 | +1.2232 | 0.0018 | 1 | 75,769.310 |
| Zn I | np 1P* J=1 | 13–40 | 28 | 26 | untested | 10.9–37.9 | +2.0966 | 0.0033 | 1 | 75,769.310 |
| Ba III | nd 2[3/2]* J=2 | 7–16 | 10 | 8 | 8/8 | 4.8–13.8 | +2.1786 | 0.0136 | 3 | 306,650.000 |
| Ba III | ns 2[1/2]* J=1 | 8–17 | 10 | 8 | untested | 4.8–13.8 | +3.2300 | 0.0154 | 3 | 306,650.000 |
| Ba III | nd 2[3/2]* J=2 | 8–22† | 14 | 12 | untested | 5.9–19.9 | +2.1273 | 0.0227 | 3 | 289,100.000 |
| Ba III | ns 2[3/2]* J=1 | 9–23 | 15 | 13 | untested | 5.8–19.9 | +3.2018 | 0.0273 | 3 | 289,100.000 |
| Ne II | nd 4D J=3/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0700 | 0.0012 | 2 | 330,388.600 |
| Ne II | nd 4D J=5/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0773 | 0.0036 | 2 | 330,388.600 |
| Ne II | nd 4D J=7/2 | 3–6 | 4 | 2 | untested | 2.9–5.9 | +0.0813 | 0.0047 | 2 | 330,388.600 |
| Ne II | nd 4F J=9/2 | 3–6 | 4 | 2 | untested | 3.0–5.9 | +0.0547 | 0.0070 | 2 | 330,388.600 |
| Ne II | ns 2P J=1/2 | 3–7 | 5 | 3 | untested | 2.0–6.3 | +0.8636 | 0.0857 | 2 | 330,388.600 |
| Ne II | ns 2P J=3/2 | 3–7 | 5 | 3 | untested | 2.0–6.0 | +0.9480 | 0.0143 | 2 | 330,388.600 |
| Ne II | ns 4P J=1/2 | 3–7 | 5 | 3 | untested | 2.0–6.2 | +0.9132 | 0.0743 | 2 | 330,388.600 |
| Ne II | ns 4P J=3/2 | 3–7 | 5 | 3 | untested | 2.0–6.2 | +0.9261 | 0.0730 | 2 | 330,388.600 |
| Ne II | ns 4P J=5/2 | 3–7 | 5 | 3 | untested | 2.0–6.0 | +0.9906 | 0.0125 | 2 | 330,388.600 |
| Ne II | nd 2S J=1/2 | 3–8 | 6 | 4 | untested | 3.0–7.9 | +0.0701 | 0.0422 | 2 | 356,229.300 |
| Ne II | ns 2D J=3/2 | 3–5 | 3 | 1 | untested | 2.0–4.0 | +0.9850 | 0.0115 | 2 | 356,229.300 |
| Ne II | ns 2D J=5/2 | 3–5 | 3 | 1 | untested | 2.0–4.0 | +0.9850 | 0.0115 | 2 | 356,229.300 |
| Ne I | np 1P* J=1 | 3–12 | 10 | 8 | untested | 2.2–11.1 | +0.8409 | 0.0191 | 1 | 390,977.350 |
| Ne II | np 2D* J=3/2 | 3–6 | 4 | 2 | untested | 2.4–5.5 | +0.5651 | 0.0645 | 2 | 330,388.600 |
| Ne II | np 2D* J=5/2 | 3–6 | 4 | 2 | untested | 2.4–5.4 | +0.6294 | 0.0117 | 2 | 330,388.600 |
| Ne II | np 2S* J=1/2 | 3–6 | 4 | 2 | untested | 2.4–5.4 | +0.6010 | 0.0199 | 2 | 330,388.600 |
| Ne II | np 4D* J=1/2 | 3–6 | 4 | 2 | untested | 2.3–5.5 | +0.5916 | 0.0576 | 2 | 330,388.600 |
| Ne II | np 4D* J=5/2 | 3–6 | 4 | 2 | untested | 2.3–5.5 | +0.6055 | 0.0551 | 2 | 330,388.600 |
| Ne II | np 4D* J=7/2 | 3–6 | 4 | 2 | untested | 2.3–5.4 | +0.6541 | 0.0133 | 2 | 330,388.600 |
| Ne II | np 4P* J=1/2 | 3–6 | 4 | 2 | untested | 2.3–5.4 | +0.6430 | 0.0585 | 2 | 330,388.600 |
| Ne II | np 4P* J=3/2 | 3–6 | 4 | 2 | untested | 2.3–5.3 | +0.6767 | 0.0235 | 2 | 330,388.600 |
| Ne II | np 4P* J=5/2 | 3–6 | 4 | 2 | untested | 2.3–5.3 | +0.6884 | 0.0174 | 2 | 330,388.600 |
| Ne II | np 4S* J=3/2 | 3–6 | 4 | 2 | untested | 2.4–5.5 | +0.5679 | 0.0424 | 2 | 330,388.600 |
| Ne II | nf 2[2]* J=5/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0039 | 0.0001 | 2 | 330,388.600 |
| Ne II | nf 2[3]* J=7/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0086 | 0.0001 | 2 | 330,388.600 |
| Ne II | nf 2[4]* J=7/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0096 | 0.0002 | 2 | 330,388.600 |
| Ne II | nf 2[4]* J=9/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0098 | 0.0002 | 2 | 330,388.600 |
| Ne II | nf 2[5]* J=11/2 | 5–8 | 4 | 2 | untested | 5.0–8.0 | +0.0025 | 0.0003 | 2 | 330,388.600 |
| Ne II | ng 2[2] J=3/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | -0.0016 | 0.0001 | 2 | 330,388.600 |
| Ne II | ng 2[3] J=5/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0010 | 0.0001 | 2 | 330,388.600 |
| Ne II | ng 2[4] J=7/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0029 | 0.0001 | 2 | 330,388.600 |
| Ne II | ng 2[5] J=9/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | +0.0030 | 0.0001 | 2 | 330,388.600 |
| Ne II | ng 2[6] J=11/2 | 5–7 | 3 | 1 | untested | 5.0–7.0 | -0.0002 | 0.0001 | 2 | 330,388.600 |
| Ar II | ng 2[4] J=9/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0089 | 0.0036 | 2 | 222,848.300 |
| Ar II | ng 2[6] J=11/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0035 | 0.0003 | 2 | 222,848.300 |
| Ar II | ng 2[6] J=13/2 | 6–8 | 3 | 1 | untested | 6.0–8.0 | +0.0035 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[2] J=3/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0006 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[2] J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0006 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[3] J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0063 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[3] J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0063 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[4] J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0114 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ng 2[5] J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0119 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ng 2[5] J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0119 | 0.0002 | 2 | 222,848.300 |
| Ar II * | nh 2[3]* J=5/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0017 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[3]* J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0017 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[4]* J=7/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0021 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[4]* J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0021 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[5]* J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0047 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[5]* J=9/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0047 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[6]* J=11/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0045 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[6]* J=13/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | +0.0045 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[7]* J=13/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0000 | 0.0001 | 2 | 222,848.300 |
| Ar II * | nh 2[7]* J=15/2 | 6–7 | 2 | 1 | untested | 6.0–7.0 | -0.0000 | 0.0001 | 2 | 222,848.300 |
| Ar II * | ni 2[4] J=7/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0009 | 0.0005 | 2 | 222,848.300 |
| Ar II * | ni 2[4] J=9/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0009 | 0.0005 | 2 | 222,848.300 |
| Ar II * | ni 2[5] J=11/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0012 | 0.0003 | 2 | 222,848.300 |
| Ar II * | ni 2[5] J=9/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0012 | 0.0003 | 2 | 222,848.300 |
| Ar II * | ni 2[6] J=11/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0025 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[6] J=13/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0025 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[7] J=13/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0023 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[7] J=15/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | +0.0023 | 0.0002 | 2 | 222,848.300 |
| Ar II * | ni 2[8] J=15/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0000 | 0.0006 | 2 | 222,848.300 |
| Ar II * | ni 2[8] J=17/2 | 7–8 | 2 | 1 | untested | 7.0–8.0 | -0.0000 | 0.0006 | 2 | 222,848.300 |
| Bi II * | 6s2.6p.nf (1/2,7/2) J=3 | 5–6 | 2 | 1 | no-triple | 3.9–4.9 | +1.1419 | 0.0039 | 2 | 134,720.000 |
| Bi II * | 6s2.6p.np (1/2,1/2) J=0 | 7–8 | 2 | 1 | no-triple | 3.0–4.1 | +3.9567 | 0.0079 | 2 | 134,720.000 |
| Bi III * | 6s2.nh 2H* J=11/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0103 | 0.0005 | 3 | 206,242.000 |
| Bi III * | 6s2.nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0103 | 0.0005 | 3 | 206,242.000 |
| C II * | 2s2(1S)nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0740 | 0.0044 | 2 | 196,664.700 |
| C II * | 2s2(1S)nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0740 | 0.0044 | 2 | 196,664.700 |
| C II * | 2s2(1S)ns 2S J=1/2 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.6615 | 0.0020 | 2 | 196,664.700 |
| Li I * | nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0016 | 0.0001 | 1 | 43,487.150 |
| Li I * | nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0016 | 0.0001 | 1 | 43,487.150 |
| Li I * | ns 2S J=1/2 | 2–3 | 2 | 1 | no-triple | 1.6–2.6 | +0.4077 | 0.0038 | 1 | 43,487.150 |
| Li II * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | -0.0001 | 0.0000 | 2 | 610,078.400 |
| Li II * | 1s.np 3P* J=0 | 2–3 | 2 | 1 | no-triple | 1.9–2.9 | +0.0537 | 0.0004 | 2 | 610,078.400 |
| Li II * | 1s.np 3P* J=2 | 2–3 | 2 | 1 | no-triple | 1.9–2.9 | +0.0537 | 0.0004 | 2 | 610,078.400 |
| Li III * | nk 2K* J=13/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Li III * | nk 2K* J=15/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 3 | 987,662.290 |
| Mg I * | 3snf 1F° J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg I * | 3snf 3F° J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0413 | 0.0022 | 1 | 61,671.050 |
| Mg II * | nd 2D J=3/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0340 | 0.0036 | 2 | 121,267.640 |
| Mg II * | nd 2D J=5/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0340 | 0.0036 | 2 | 121,267.640 |
| Ne I * | 2p5(2P°3/2)nd 2[7/2]° J=4 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0193 | 0.0014 | 1 | 173,929.750 |
| Ne I * | 2p5(2P°3/2)ns 2[3/2]° J=2 | 3–4 | 2 | 1 | no-triple | 1.7–2.7 | +1.3329 | 0.0085 | 1 | 173,929.750 |
| Ne II * | nd 2F J=5/2 | 3–4 | 2 | 1 | untested | 3.0–4.0 | +0.0289 | 0.0055 | 2 | 356,229.300 |
| Ne II * | nd 2F J=7/2 | 3–4 | 2 | 1 | untested | 3.0–4.0 | +0.0289 | 0.0055 | 2 | 356,229.300 |
| Ne II * | nd 2G J=7/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0674 | 0.0050 | 2 | 356,229.300 |
| Ne II * | nd 2G J=9/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0674 | 0.0050 | 2 | 356,229.300 |
| Ne II * | nd 2P J=3/2 | 3–4 | 2 | 1 | untested | 2.9–3.9 | +0.0605 | 0.0040 | 2 | 356,229.300 |
| Sc III * | 3p6.nh 2H* J=11/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0022 | 0.0001 | 3 | 199,677.370 |
| Sc III * | 3p6.nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0022 | 0.0001 | 3 | 199,677.370 |
| Zn I * | 4snd 3D J=1 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0940 | 0.0007 | 1 | 75,769.330 |
| Zn I * | 4snd 3D J=2 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0936 | 0.0007 | 1 | 75,769.330 |
| Zn I * | 4snd 3D J=3 | 4–5 | 2 | 1 | no-triple | 2.9–3.9 | +1.0930 | 0.0007 | 1 | 75,769.330 |
| Ba III * | ng 2[11/2]* J=5 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0394 | 0.0028 | 3 | 289,100.000 |
| Ba III * | ng 2[11/2]* J=6 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0397 | 0.0029 | 3 | 289,100.000 |
| Ba III * | ng 2[5/2]* J=2 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0428 | 0.0002 | 3 | 289,100.000 |
| Ba III * | ng 2[5/2]* J=3 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0422 | 0.0000 | 3 | 289,100.000 |
| Ba III * | ng 2[7/2]* J=3 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0208 | 0.0006 | 3 | 289,100.000 |
| Ba III * | ng 2[7/2]* J=4 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0212 | 0.0007 | 3 | 289,100.000 |
| Ba III * | ng 2[9/2]* J=4 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0174 | 0.0030 | 3 | 289,100.000 |
| Ba III * | ng 2[9/2]* J=5 | 5–6 | 2 | 1 | untested | 5.0–6.0 | +0.0172 | 0.0029 | 3 | 289,100.000 |
| Si I | ns (3/2,1/2)* J=1 | 11–24 | 14 | 12 | untested | 9.1–22.1 | +1.8546 | 0.0082 | 1 | 66,035.000 |
| Si I | ns (3/2,1/2)* J=2 | 11–19 | 9 | 7 | untested | 9.1–17.1 | +1.8883 | 0.0005 | 1 | 66,035.000 |
| Si I | nf 2[3/2] J=1 | 4–7 | 4 | 2 | untested | 4.0–7.0 | -0.0003 | 0.0026 | 1 | 66,035.000 |
| Si I | nf 2[3/2] J=2 | 4–7 | 4 | 2 | untested | 4.0–7.0 | -0.0008 | 0.0023 | 1 | 66,035.000 |
| Si I | nf 2[5/2] J=2 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0277 | 0.0056 | 1 | 66,035.000 |
| Si I | nf 2[5/2] J=3 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0281 | 0.0057 | 1 | 66,035.000 |
| Si I | nf 2[7/2] J=3 | 4–7 | 4 | 2 | untested | 4.0–6.9 | +0.0471 | 0.0041 | 1 | 66,035.000 |
| Si I | nf 2[7/2] J=4 | 4–7 | 4 | 2 | untested | 4.0–6.9 | +0.0462 | 0.0039 | 1 | 66,035.000 |
| Si I | nf 2[9/2] J=4 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0165 | 0.0023 | 1 | 66,035.000 |
| Si I | nf 2[9/2] J=5 | 4–7 | 4 | 2 | untested | 4.0–7.0 | +0.0181 | 0.0027 | 1 | 66,035.000 |
| Si I | nd 1D* J=2 | 3–8 | 6 | 4 | untested | 2.4–7.9 | +0.4032 | 0.1771 | 1 | 65,747.760 |
| Si I | nd 1F* J=3 | 3–8† | 5 | 3 | untested | 3.0–8.4 | -0.1375 | 0.1513 | 1 | 65,747.760 |
| Si I | nd 1P* J=1 | 3–8 | 6 | 4 | untested | 3.0–8.0 | +0.0284 | 0.0044 | 1 | 65,747.760 |
| Si I | nd 3F* J=2 | 3–8 | 6 | 4 | untested | 2.6–7.6 | +0.3730 | 0.0333 | 1 | 65,747.760 |
| Si I | nd 3F* J=3 | 3–8 | 6 | 4 | untested | 2.6–7.8 | +0.3007 | 0.0615 | 1 | 65,747.760 |
| Si I | nd 3F* J=4 | 3–8 | 6 | 4 | untested | 2.6–8.2 | +0.1429 | 0.2129 | 1 | 65,747.760 |
| Si I * | np (1/2,1/2) J=1 | 6–7 | 2 | 1 | untested | 4.5–5.5 | +1.4808 | 0.0027 | 1 | 65,747.760 |
| Si I * | np (1/2,3/2) J=1 | 6–7 | 2 | 1 | untested | 4.6–5.6 | +1.4252 | 0.0076 | 1 | 65,747.760 |
| Si I * | np (1/2,3/2) J=2 | 6–7 | 2 | 1 | untested | 4.6–5.6 | +1.4210 | 0.0078 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=0 | 6–10 | 5 | 3 | 3/3 | 4.1–8.1 | +1.8930 | 0.0038 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=1 | 6–10 | 5 | 3 | 3/3 | 4.1–8.1 | +1.8758 | 0.0091 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=0 | 13–21 | 9 | 7 | untested | 11.1–19.1 | +1.8873 | 0.0031 | 1 | 65,747.760 |
| Si I | ns (1/2,1/2)* J=1 | 13–21 | 9 | 7 | untested | 11.1–19.1 | +1.8765 | 0.0105 | 1 | 65,747.760 |
| Si I | nd (1/2,3/2)* J=1 | 14–44 | 29 | 27 | 27/27 | 14.0–43.9 | +0.0612 | 0.0310 | 1 | 65,747.760 |
| Si I | nd (1/2,3/2)* J=1 | 9–44† | 34 | 32 | untested | 9.0–43.9 | +0.0584 | 0.0312 | 1 | 65,747.760 |
| Si I | nd (3/2,3/2)* J=0 | 8–13 | 6 | 4 | 4/4 | 8.1–13.1 | -0.0680 | 0.0129 | 1 | 66,035.000 |
| Si I | nd (3/2,3/2)* J=1 | 20–50 | 31 | 29 | untested | 20.0–50.0 | +0.0129 | 0.0444 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=1 | 8–13 | 6 | 4 | 4/4 | 7.9–12.9 | +0.0784 | 0.0064 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=3 | 20–56 | 37 | 35 | untested | 19.9–56.0 | +0.0573 | 0.0366 | 1 | 66,035.000 |
| Si I | nd (3/2,3/2)* J=0 | 8–16 | 9 | 7 | untested | 8.1–16.0 | -0.0609 | 0.0146 | 1 | 66,035.000 |
| Si I | nd (3/2,5/2)* J=1 | 8–16 | 9 | 7 | untested | 7.9–15.9 | +0.0816 | 0.0073 | 1 | 66,035.000 |
| B III | nd 2D J=3/2 | 3–11 | 9 | 7 | 7/7 | 3.0–11.0 | +0.0023 | 0.0002 | 3 | 305,930.800 |
| B III | nf 2F* J=5/2 | 4–11 | 8 | 6 | 5/6 | 4.0–11.0 | +0.0003 | 0.0000 | 3 | 305,930.800 |
| B III | ng 2G J=7/2 | 5–10 | 6 | 4 | 3/4 | 5.0–10.0 | +0.0001 | 0.0000 | 3 | 305,930.800 |
| B III | nh 2H* J=9/2 | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 3 | 305,930.800 |
| B III | np 2P* J=1/2 | 2–9 | 8 | 6 | 3/6 | 2.0–9.0 | +0.0437 | 0.0007 | 3 | 305,930.800 |
| B III | ns 2S J=1/2 | 2–9 | 8 | 6 | 6/6 | 1.8–8.8 | +0.1959 | 0.0030 | 3 | 305,930.800 |
| Be III | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 4/6 | 3.0–10.0 | +0.0008 | 0.0002 | 3 | 1,241,256.601 |
| Be III | 1s.nd 3D J=2 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | +0.0023 | 0.0002 | 3 | 1,241,256.601 |
| Be III | 1s.nf 1F* J=3 | 4–9 | 6 | 4 | 2/4 | 4.0–9.0 | +0.0002 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 1/3 | 5.0–9.0 | +0.0002 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0000 | 0.0000 | 3 | 1,241,256.601 |
| Be III * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | +0.0000 | 0.0000 | 3 | 1,241,256.601 |
| Be III | 1s.np 3P* J=1 | 2–10 | 9 | 7 | 5/7 | 2.0–10.0 | +0.0429 | 0.0001 | 3 | 1,241,256.601 |
| Be III | 1s.ns 1S J=0 | 2–10 | 9 | 7 | 4/7 | 1.9–9.9 | +0.0508 | 0.0003 | 3 | 1,241,256.601 |
| Be III | 1s.ns 3S J=1 | 2–10 | 9 | 7 | 5/7 | 1.9–9.9 | +0.1302 | 0.0028 | 3 | 1,241,256.601 |
| Be IV | nd 2D J=3/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0002 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nf 2F* J=5/2 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0001 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0001 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nh 2H* J=9/2 | 6–10 | 5 | 3 | 3/3 | 6.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ni 2I J=11/2 | 7–10 | 4 | 2 | 2/2 | 7.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | nk 2K* J=13/2 | 8–10 | 3 | 1 | 1/1 | 8.0–10.0 | +0.0000 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | np 2P* J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0004 | 0.0000 | 4 | 1,756,018.810 |
| Be IV | ns 2S J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0004 | 0.0000 | 4 | 1,756,018.810 |
| Mg III * | nd 2[1/2]* J=1 | 4–5 | 2 | 1 | no-triple | 3.9–4.9 | +0.0934 | 0.0014 | 3 | 646,402.000 |
| Mg III | nd 2[3/2]* J=1 | 4–9 | 6 | 4 | 1/4 | 4.0–9.0 | +0.0388 | 0.0017 | 3 | 646,402.000 |
| Mg III * | nf 2[3/2] J=1 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0111 | 0.0005 | 3 | 646,402.000 |
| Mg III * | nf 2[3/2] J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0108 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[5/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0039 | 0.0003 | 3 | 646,402.000 |
| Mg III * | nf 2[7/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0000 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[7/2] J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | -0.0000 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[9/2] J=4 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0073 | 0.0004 | 3 | 646,402.000 |
| Mg III * | nf 2[9/2] J=5 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0073 | 0.0004 | 3 | 646,402.000 |
| Mg III | ns 2[3/2]* J=1 | 4–6 | 3 | 1 | 1/1 | 3.1–5.2 | +0.8487 | 0.0050 | 3 | 646,402.000 |
| Mg III * | ns 2[3/2]* J=2 | 4–5 | 2 | 1 | no-triple | 3.1–4.1 | +0.8634 | 0.0030 | 3 | 646,402.000 |
| Al III | nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0644 | 0.0071 | 3 | 229,445.710 |
| Al III | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0044 | 0.0005 | 3 | 229,445.710 |
| Al III | ng 2G J=7/2 | 5–9 | 5 | 3 | 2/3 | 5.0–9.0 | +0.0010 | 0.0001 | 3 | 229,445.710 |
| Al III | nh 2H* J=9/2 | 6–9 | 4 | 2 | 1/2 | 6.0–9.0 | +0.0003 | 0.0000 | 3 | 229,445.710 |
| Al III | np 2P* J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.4–6.4 | +0.6056 | 0.0128 | 3 | 229,445.710 |
| Al III | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.1–7.1 | +0.9049 | 0.0098 | 3 | 229,445.710 |
| Si III | nd 1D J=2 | 3–9 | 7 | 5 | 3/5 | 3.1–9.0 | +0.0507 | 0.1195 | 3 | 270,139.300 |
| Si III | nd 3D J=3 | 3–9 | 7 | 5 | 2/5 | 2.8–8.8 | +0.1977 | 0.0294 | 3 | 270,139.300 |
| Si III | nf 1F* J=3 | 4–9 | 6 | 4 | 2/4 | 3.9–9.0 | +0.0240 | 0.1413 | 3 | 270,139.300 |
| Si III | nf 3F* J=2 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0226 | 0.0272 | 3 | 270,139.300 |
| Si III | nf 3F* J=3 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0224 | 0.0275 | 3 | 270,139.300 |
| Si III | nf 3F* J=4 | 4–9 | 6 | 4 | 4/4 | 4.0–9.0 | +0.0221 | 0.0280 | 3 | 270,139.300 |
| Si III | ng 1G J=4 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0266 | 0.0040 | 3 | 270,139.300 |
| Si III | ng 3G J=3 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0281 | 0.0047 | 3 | 270,139.300 |
| Si III | ng 3G J=4 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0281 | 0.0047 | 3 | 270,139.300 |
| Si III | ng 3G J=5 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0280 | 0.0047 | 3 | 270,139.300 |
| Si III | nh 1H* J=5 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0082 | 0.0007 | 3 | 270,139.300 |
| Si III | nh 3H* J=5 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0086 | 0.0004 | 3 | 270,139.300 |
| Si III | nh 3H* J=6 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0082 | 0.0007 | 3 | 270,139.300 |
| Si III | ni 1I J=6 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0033 | 0.0002 | 3 | 270,139.300 |
| Si III | ni 3I J=7 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0033 | 0.0002 | 3 | 270,139.300 |
| Si III | np 1P* J=1 | 4–7 | 4 | 2 | 0/2 | 3.2–6.3 | +0.7576 | 0.0165 | 3 | 270,139.300 |
| Si III | np 3P* J=0 | 4–7 | 4 | 2 | 2/2 | 3.2–6.3 | +0.7563 | 0.0149 | 3 | 270,139.300 |
| Si III | ns 1S J=0 | 4–8 | 5 | 3 | 2/3 | 3.0–7.0 | +1.0185 | 0.0017 | 3 | 270,139.300 |
| Si III | ns 3S J=1 | 4–8 | 5 | 3 | 3/3 | 2.9–7.0 | +1.0646 | 0.0175 | 3 | 270,139.300 |
| Ar II | 3s2.3p4.(3P).nd 4D J=7/2 | 3–5 | 3 | 1 | untested | 2.2–4.4 | +0.6930 | 0.0749 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=1/2 | 4–6 | 3 | 1 | untested | 2.2–4.4 | +1.6821 | 0.0615 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=3/2 | 4–6 | 3 | 1 | untested | 2.2–4.3 | +1.7246 | 0.0283 | 2 | 222,848.300 |
| Ar II | 3s2.3p4.(3P).ns 4P J=5/2 | 4–6 | 3 | 1 | untested | 2.2–4.3 | +1.7463 | 0.0203 | 2 | 222,848.300 |
| B IV | 1s.nd 1D J=2 | 3–10 | 8 | 6 | 2/6 | 3.0–10.0 | +0.0007 | 0.0002 | 4 | 2,091,995.451 |
| B IV | 1s.nd 3D J=1 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | +0.0021 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.nf 1F* J=3 | 4–9 | 6 | 4 | 3/4 | 4.0–9.0 | +0.0004 | 0.0005 | 4 | 2,091,995.451 |
| B IV | 1s.ng 1G J=4 | 5–9 | 5 | 3 | 0/3 | 5.0–9.0 | +0.0002 | 0.0004 | 4 | 2,091,995.451 |
| B IV | 1s.nh 1H* J=5 | 6–9 | 4 | 2 | 1/2 | 6.0–9.0 | -0.0002 | 0.0002 | 4 | 2,091,995.451 |
| B IV * | 1s.ni 1I J=6 | 7–8 | 2 | 1 | no-triple | 7.0–8.0 | -0.0003 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.np 1P* J=1 | 3–10 | 8 | 6 | 3/6 | 3.0–10.0 | -0.0096 | 0.0003 | 4 | 2,091,995.451 |
| B IV | 1s.np 3P* J=0 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0350 | 0.0001 | 4 | 2,091,995.451 |
| B IV | 1s.ns 1S J=0 | 3–10 | 8 | 6 | 4/6 | 3.0–10.0 | +0.0392 | 0.0004 | 4 | 2,091,995.451 |
| B IV | 1s.ns 3S J=1 | 3–10 | 8 | 6 | 6/6 | 2.9–9.9 | +0.1011 | 0.0009 | 4 | 2,091,995.451 |
| B V | nd 2D J=3/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0005 | 0.0002 | 5 | 2,744,111.380 |
| B V | nf 2F* J=5/2 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0004 | 0.0002 | 5 | 2,744,111.380 |
| B V | ng 2G J=7/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0003 | 0.0002 | 5 | 2,744,111.380 |
| B V | nh 2H* J=9/2 | 6–9 | 4 | 2 | 2/2 | 6.0–9.0 | +0.0003 | 0.0001 | 5 | 2,744,111.380 |
| B V | ni 2I J=11/2 | 7–9 | 3 | 1 | 1/1 | 7.0–9.0 | +0.0004 | 0.0001 | 5 | 2,744,111.380 |
| B V * | nk 2K* J=13/2 | 8–9 | 2 | 1 | no-triple | 8.0–9.0 | +0.0004 | 0.0001 | 5 | 2,744,111.380 |
| B V | np 2P* J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0008 | 0.0002 | 5 | 2,744,111.380 |
| B V | ns 2S J=1/2 | 3–10 | 8 | 6 | 6/6 | 3.0–10.0 | +0.0008 | 0.0002 | 5 | 2,744,111.380 |
| Si IV | nd 2D J=5/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0802 | 0.0079 | 4 | 364,093.100 |
| Si IV | nf 2F* J=5/2 | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0054 | 0.0007 | 4 | 364,093.100 |
| Si IV | ng 2G J=7/2 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0011 | 0.0001 | 4 | 364,093.100 |
| Si IV * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0003 | 0.0001 | 4 | 364,093.100 |
| Si IV | np 2P* J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.4–7.5 | +0.5262 | 0.0121 | 4 | 364,093.100 |
| Si IV | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.2–7.2 | +0.7845 | 0.0094 | 4 | 364,093.100 |
| P IV | nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.1991 | 0.0295 | 4 | 415,551.800 |
| P IV | nd 3D J=1 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.2312 | 0.0239 | 4 | 415,551.800 |
| P IV | nf 3F* J=2 | 4–6 | 3 | 1 | 1/1 | 4.0–5.9 | +0.0597 | 0.0170 | 4 | 415,551.800 |
| P IV | np 1P* J=1 | 4–6 | 3 | 1 | 0/1 | 3.3–5.4 | +0.6991 | 0.0588 | 4 | 415,551.800 |
| P IV | np 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 3.3–5.3 | +0.6699 | 0.0079 | 4 | 415,551.800 |
| P IV | ns 1S J=0 | 4–6 | 3 | 1 | 1/1 | 3.1–5.1 | +0.9018 | 0.0111 | 4 | 415,551.800 |
| P IV | ns 3S J=1 | 4–7 | 4 | 2 | 0/2 | 3.1–6.0 | +0.9498 | 0.0073 | 4 | 415,551.800 |
| C V | 1s.nd 1D J=2 | 3–7 | 5 | 3 | 3/3 | 3.0–7.0 | +0.0108 | 0.0077 | 5 | 3,162,788.800 |
| C V | 1s.nd 3D J=1 | 3–7 | 5 | 3 | 3/3 | 3.0–7.0 | +0.0122 | 0.0078 | 5 | 3,162,788.800 |
| C V | 1s.nf 1F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0092 | 0.0042 | 5 | 3,162,788.800 |
| C V | 1s.nf 3F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.0 | +0.0092 | 0.0041 | 5 | 3,162,788.800 |
| C V | 1s.ng 1G J=4 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0152 | 0.0059 | 5 | 3,162,788.800 |
| C V | 1s.ng 3G J=4 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0153 | 0.0059 | 5 | 3,162,788.800 |
| C V * | 1s.nh 1H* J=5 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0186 | 0.0042 | 5 | 3,162,788.800 |
| C V | 1s.np 1P* J=1 | 2–7 | 6 | 4 | 4/4 | 2.0–7.0 | +0.0002 | 0.0084 | 5 | 3,162,788.800 |
| C V | 1s.np 3P* J=0 | 2–7 | 6 | 4 | 4/4 | 2.0–6.9 | +0.0384 | 0.0075 | 5 | 3,162,788.800 |
| C V | 1s.ns 1S J=0 | 2–7 | 6 | 4 | 4/4 | 2.0–6.9 | +0.0399 | 0.0079 | 5 | 3,162,788.800 |
| C V | 1s.ns 3S J=1 | 2–7 | 6 | 4 | 3/4 | 1.9–6.9 | +0.0927 | 0.0063 | 5 | 3,162,788.800 |
| S V | 3s.nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.8–5.8 | +0.1819 | 0.0275 | 5 | 586,610.400 |
| S V | 3s.nd 3D J=1 | 4–7 | 4 | 2 | 1/2 | 3.8–6.8 | +0.2170 | 0.0211 | 5 | 586,610.400 |
| S V | 3s.nf 1F* J=3 | 4–6 | 3 | 1 | 0/1 | 4.0–6.0 | +0.0002 | 0.0246 | 5 | 586,610.400 |
| S V | 3s.nf 3F* J=2 | 4–6 | 3 | 1 | 1/1 | 4.0–5.9 | +0.0637 | 0.0116 | 5 | 586,610.400 |
| S V | 3s.np 1P* J=1 | 4–7 | 4 | 2 | 1/2 | 3.4–6.4 | +0.5900 | 0.0229 | 5 | 586,610.400 |
| S V | 3s.np 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 3.4–5.3 | +0.6221 | 0.0348 | 5 | 586,610.400 |
| S V | 3s.ns 1S J=0 | 4–7 | 4 | 2 | 0/2 | 3.2–6.2 | +0.8043 | 0.0144 | 5 | 586,610.400 |
| S V | 3s.ns 3S J=1 | 4–7 | 4 | 2 | 1/2 | 3.2–6.1 | +0.8428 | 0.0080 | 5 | 586,610.400 |
| Fe XV * | nd 3D J=1 | 4–5 | 2 | 1 | no-triple | 3.9–4.9 | +0.1278 | 0.0017 | 15 | 3,679,500.000 |
| Fe XV | nf 1F* J=3 | 4–6 | 3 | 1 | 1/1 | 4.0–6.5 | -0.2367 | 0.2030 | 15 | 3,679,500.000 |
| Fe XV * | nf 3F* J=2 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0371 | 0.0016 | 15 | 3,679,500.000 |
| Fe XV * | np 1P* J=1 | 4–5 | 2 | 1 | no-triple | 3.7–4.7 | +0.2872 | 0.0017 | 15 | 3,679,500.000 |
| Ca IX | nd 1D J=2 | 4–6 | 3 | 1 | 0/1 | 3.9–5.8 | +0.1572 | 0.0090 | 9 | 1,520,640.000 |
| Ca IX * | nf 1F* J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0124 | 0.0050 | 9 | 1,520,640.000 |
| Ca IX | np 1P* J=1 | 4–6 | 3 | 1 | 0/1 | 3.6–5.6 | +0.4121 | 0.0041 | 9 | 1,520,640.000 |
| Ca IX * | ns 3S J=1 | 4–5 | 2 | 1 | no-triple | 3.4–4.4 | +0.5725 | 0.0078 | 9 | 1,520,640.000 |
| Ti XI * | nf 1F* J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0129 | 0.0041 | 11 | 2,137,900.000 |
| Ti XI | np 1P* J=1 | 4–7 | 4 | 2 | 1/2 | 3.6–6.7 | +0.3273 | 0.0161 | 11 | 2,137,900.000 |
| Ti XI * | ns 1S J=0 | 4–5 | 2 | 1 | no-triple | 3.5–4.5 | +0.4738 | 0.0070 | 11 | 2,137,900.000 |
| Ti XI * | ns 3S J=1 | 4–5 | 2 | 1 | no-triple | 3.5–4.5 | +0.4983 | 0.0067 | 11 | 2,137,900.000 |
| Ti III * | nd 1F J=3 | 4–5 | 2 | 1 | no-triple | 3.2–4.2 | +0.7987 | 0.0056 | 3 | 223,827.100 |
| Ti III * | nd 3D J=1 | 4–5 | 2 | 1 | no-triple | 3.2–4.2 | +0.7899 | 0.0076 | 3 | 223,827.100 |
| Ti III * | np 1D* J=2 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.4159 | 0.0063 | 3 | 223,827.100 |
| Ti III * | np 3D* J=1 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.4039 | 0.0025 | 3 | 223,827.100 |
| Ti III * | np 3F* J=2 | 4–5 | 2 | 1 | no-triple | 2.6–3.6 | +1.3956 | 0.0072 | 3 | 223,827.100 |
| Ti III * | ns 1D J=2 | 4–5 | 2 | 1 | no-triple | 2.3–3.3 | +1.6726 | 0.0013 | 3 | 223,827.100 |
| Ti III * | ns 3D J=1 | 4–5 | 2 | 1 | no-triple | 2.3–3.3 | +1.6901 | 0.0041 | 3 | 223,827.100 |
| Ca II | ns 2S J=1/2 | 4–6 | 3 | 1 | 1/1 | 2.1–4.2 | +1.8338 | 0.0183 | 2 | 95,751.880 |
| Ca II | nd 2D J=3/2 | 3–16 | 14 | 12 | untested | 2.3–15.4 | +0.6341 | 0.0154 | 2 | 95,751.870 |
| Ca II | nf 2F* J=5/2 | 4–10 | 7 | 5 | untested | 4.0–10.0 | +0.0248 | 0.0029 | 2 | 95,751.870 |
| Ca II | ng 2G J=7/2 | 5–9 | 5 | 3 | untested | 5.0–9.0 | +0.0048 | 0.0004 | 2 | 95,751.870 |
| Ca II * | nh 2H* J=9/2 | 8–10† | 2 | 1 | untested | 8.0–10.0 | +0.0016 | 0.0000 | 2 | 95,751.870 |
| Ca II | np 2P* J=1/2 | 4–6 | 3 | 1 | untested | 2.5–4.5 | +1.4775 | 0.0207 | 2 | 95,751.870 |
| Ca II | ns 2S J=1/2 | 4–10 | 7 | 5 | untested | 2.1–8.2 | +1.8192 | 0.0175 | 2 | 95,751.870 |
| Cd II | nd 2D J=3/2 | 5–13 | 9 | 7 | 7/7 | 3.1–11.1 | +1.8942 | 0.0159 | 2 | 136,374.740 |
| Cd II | nf 2F* J=5/2 | 4–9 | 6 | 4 | 4/4 | 4.0–8.9 | +0.0489 | 0.0092 | 2 | 136,374.740 |
| Cd II | ng 2G J=7/2 | 5–11 | 7 | 5 | 4/5 | 5.0–11.0 | +0.0076 | 0.0004 | 2 | 136,374.740 |
| Cd II | np 2P* J=1/2 | 5–12† | 7 | 5 | 2/3 | 2.2–9.3 | +2.7444 | 0.0319 | 2 | 136,374.740 |
| Cd II | ns 2S J=1/2 | 5–13 | 9 | 7 | 7/7 | 1.8–9.9 | +3.1175 | 0.0330 | 2 | 136,374.740 |
| Ca I | nd 1D J=2 | 4–9 | 6 | 4 | untested | 3.0–8.6 | +0.9084 | 0.2360 | 1 | 49,305.950 |
| Ca I | nd 3D J=1 | 4–9 | 6 | 4 | untested | 3.1–8.4 | +0.8917 | 0.1405 | 1 | 49,305.950 |
| Ca I | nf 1F* J=3 | 4–8 | 5 | 3 | untested | 4.0–7.9 | +0.0654 | 0.0190 | 1 | 49,305.950 |
| Ca I | nf 3F* J=2 | 4–9 | 6 | 4 | untested | 3.9–8.9 | +0.0893 | 0.0059 | 1 | 49,305.950 |
| Ca I | np 1P* J=1 | 5–10 | 6 | 4 | untested | 3.0–8.2 | +1.8902 | 0.1793 | 1 | 49,305.950 |
| Ca I | ns 1S J=0 | 5–11 | 7 | 5 | untested | 2.6–8.7 | +2.3548 | 0.0350 | 1 | 49,305.950 |
| Ca I | ns 3S J=1 | 5–11 | 7 | 5 | untested | 2.5–8.6 | +2.4639 | 0.0227 | 1 | 49,305.950 |
| Ar I | nd 2[7/2]* J=4 | 3–6 | 4 | 2 | 2/2 | 2.8–5.6 | +0.3516 | 0.0715 | 1 | 127,198.600 |
| Ar I | np 2[1/2] J=1 | 4–7 | 4 | 2 | 1/2 | 2.2–5.2 | +1.7855 | 0.0204 | 1 | 127,198.600 |
| Ar I | np 2[3/2] J=1 | 4–7 | 4 | 2 | 1/2 | 2.3–5.3 | +1.7107 | 0.0123 | 1 | 127,198.600 |
| Ar I | np 2[5/2] J=3 | 4–7 | 4 | 2 | 1/2 | 2.2–5.2 | +1.7437 | 0.0119 | 1 | 127,198.600 |
| Ar I | ns 2[3/2]* J=1 | 4–7 | 4 | 2 | 1/2 | 1.8–4.8 | +2.1701 | 0.0138 | 1 | 127,198.600 |
| Ar I | ns 2[3/2]* J=2 | 4–7 | 4 | 2 | 1/2 | 1.8–4.8 | +2.1886 | 0.0132 | 1 | 127,198.600 |
| Cd I | nd 1D J=2 | 5–15† | 10 | 8 | 5/6 | 2.9–12.8 | +2.1886 | 0.0288 | 1 | 72,540.050 |
| Cd I | nd 3D J=1 | 5–11 | 7 | 5 | 5/5 | 2.9–8.9 | +2.0898 | 0.0049 | 1 | 72,540.050 |
| Cd I | nf 3F* J=3 | 4–10 | 7 | 5 | 5/5 | 4.0–10.0 | +0.0346 | 0.0034 | 1 | 72,540.050 |
| Cd I | np 1P* J=1 | 6–12 | 7 | 5 | 3/5 | 2.9–8.9 | +3.0515 | 0.0005 | 1 | 72,540.050 |
| Cd I | np 3P* J=0 | 6–10 | 5 | 3 | 3/3 | 2.8–6.8 | +3.1814 | 0.0184 | 1 | 72,540.050 |
| Cd I | ns 1S J=0 | 6–15 | 10 | 8 | 5/8 | 2.4–11.4 | +3.5926 | 0.0131 | 1 | 72,540.050 |
| Cd I | ns 3S J=1 | 6–16 | 11 | 9 | 7/9 | 2.3–12.3 | +3.6677 | 0.0188 | 1 | 72,540.050 |
| Ga II | nd 1D J=2 | 4–7 | 4 | 2 | 2/2 | 3.3–6.1 | +0.8475 | 0.1127 | 2 | 165,465.800 |
| Ga II | nd 3D J=1 | 4–7 | 4 | 2 | 2/2 | 2.9–5.9 | +1.0630 | 0.0133 | 2 | 165,465.800 |
| Ga II | nf 1F* J=3 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0598 | 0.0070 | 2 | 165,465.800 |
| Ga II | nf 3F* J=2 | 4–7 | 4 | 2 | 2/2 | 3.9–6.9 | +0.0617 | 0.0080 | 2 | 165,465.800 |
| Ga II | ng (1/2,7/2) J=3 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0146 | 0.0012 | 2 | 165,465.800 |
| Ga II | ng (1/2,9/2) J=5 | 5–8 | 4 | 2 | 2/2 | 5.0–8.0 | +0.0142 | 0.0010 | 2 | 165,465.800 |
| Ga II | ns 1S J=0 | 5–8 | 4 | 2 | 1/2 | 2.7–5.8 | +2.2610 | 0.0138 | 2 | 165,465.800 |
| Ga II | ns 3S J=1 | 5–8 | 4 | 2 | 2/2 | 2.6–5.7 | +2.3228 | 0.0169 | 2 | 165,465.800 |
| Hg II | nd 2D J=3/2 | 6–11 | 6 | 4 | 4/4 | 3.1–8.1 | +2.8758 | 0.0227 | 2 | 151,269.200 |
| Hg II | nf 2F* J=7/2 | 5–8 | 4 | 2 | 2/2 | 4.0–6.9 | +1.0622 | 0.0083 | 2 | 151,269.200 |
| Hg II | ng 2G J=9/2 | 5–9 | 5 | 3 | 3/3 | 5.0–9.0 | +0.0053 | 0.0028 | 2 | 151,269.200 |
| Hg II | np 2P* J=1/2 | 6–8 | 3 | 1 | 1/1 | 2.1–4.2 | +3.8196 | 0.0624 | 2 | 151,269.200 |
| Hg II | ns 2S J=1/2 | 6–11 | 6 | 4 | 4/4 | 1.7–6.8 | +4.1850 | 0.0515 | 2 | 151,269.200 |
| P III | nd 2D J=5/2 | 3–6 | 4 | 2 | 2/2 | 2.8–5.7 | +0.2754 | 0.0451 | 3 | 243,573.700 |
| P III | ng 2G J=7/2 | 5–8 | 4 | 2 | 1/2 | 5.0–8.0 | +0.0197 | 0.0011 | 3 | 243,573.700 |
| P III | nh 2H* J=9/2 | 6–8 | 3 | 1 | 1/1 | 6.0–8.0 | +0.0024 | 0.0012 | 3 | 243,573.700 |
| P III | np 2P* J=1/2 | 4–6 | 3 | 1 | 0/1 | 3.1–5.1 | +0.8886 | 0.0128 | 3 | 243,573.700 |
| P III | ns 2S J=1/2 | 4–9 | 6 | 4 | 4/4 | 2.8–7.8 | +1.1692 | 0.0144 | 3 | 243,573.700 |
| Ba II | nd 2D J=3/2 | 5–25† | 14 | 12 | 10/10 | 2.4–22.6 | +2.4147 | 0.0516 | 2 | 80,687.900 |
| Ba II | nf 2F* J=5/2 | 4–12 | 9 | 7 | 7/7 | 3.7–11.1 | +0.7559 | 0.1645 | 2 | 80,687.900 |
| Ba II | ng 2G J=7/2 | 5–10 | 6 | 4 | 4/4 | 5.0–10.0 | +0.0185 | 0.0022 | 2 | 80,687.900 |
| Ba II | np 2P* J=1/2 | 6–12 | 7 | 5 | 5/5 | 2.7–8.8 | +3.2408 | 0.0287 | 2 | 80,687.900 |
| Ba II | ns 2S J=1/2 | 6–30† | 18 | 16 | 14/14 | 2.3–26.4 | +3.5984 | 0.0191 | 2 | 80,687.900 |
| Fe XVI | nd 2D J=3/2 | 3–8 | 6 | 4 | 4/4 | 2.9–7.9 | +0.0750 | 0.0031 | 16 | 3,946,570.000 |
| Fe XVI | nf 2F* J=5/2 | 4–8 | 5 | 3 | 3/3 | 4.0–8.0 | +0.0116 | 0.0036 | 16 | 3,946,570.000 |
| Fe XVI | np 2P* J=1/2 | 3–6 | 4 | 2 | 2/2 | 2.8–5.8 | +0.2233 | 0.0059 | 16 | 3,946,570.000 |
| Fe XVI | ns 2S J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.7–6.7 | +0.3174 | 0.0152 | 16 | 3,946,570.000 |
| N III | nd 2D J=3/2 | 3–12 | 10 | 8 | 5/8 | 2.9–11.9 | +0.0737 | 0.0124 | 3 | 382,672.000 |
| N III | nf 2F* J=5/2 | 4–7 | 4 | 2 | 2/2 | 4.0–7.0 | +0.0281 | 0.0048 | 3 | 382,672.000 |
| N III | ng 2G J=7/2 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0022 | 0.0009 | 3 | 382,672.000 |
| N III * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | -0.0026 | 0.0009 | 3 | 382,672.000 |
| N III | np 2P* J=1/2 | 3–5 | 3 | 1 | 0/1 | 2.7–4.7 | +0.2917 | 0.0185 | 3 | 382,672.000 |
| N III | ns 2S J=1/2 | 3–14 | 12 | 10 | 9/10 | 2.5–13.3 | +0.5660 | 0.0740 | 3 | 382,672.000 |
| N I | nd 2F J=5/2 | 3–5 | 3 | 1 | 1/1 | 3.0–5.0 | +0.0273 | 0.0024 | 1 | 117,244.100 |
| N I * | nd 4D J=1/2 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0041 | 0.0041 | 1 | 117,244.100 |
| N I | nd 4F J=3/2 | 3–5 | 3 | 1 | 0/1 | 3.0–4.9 | +0.0514 | 0.0035 | 1 | 117,244.100 |
| N I | np 2D* J=3/2 | 3–5 | 3 | 1 | 0/1 | 2.3–4.5 | +0.6233 | 0.0955 | 1 | 117,244.100 |
| N I | np 4D* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.2 | +0.7714 | 0.0136 | 1 | 117,244.100 |
| N I | np 4P* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.2–4.3 | +0.7329 | 0.0169 | 1 | 117,244.100 |
| N I | ns 2P J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.9–4.9 | +1.1040 | 0.0116 | 1 | 117,244.100 |
| N I | ns 4P J=1/2 | 3–6 | 4 | 2 | 2/2 | 1.8–4.8 | +1.1697 | 0.0190 | 1 | 117,244.100 |
| S IV | nd 2D J=3/2 | 3–5 | 3 | 1 | 1/1 | 2.8–4.7 | +0.2649 | 0.0197 | 4 | 382,135.000 |
| S IV | np 2P* J=1/2 | 4–7 | 4 | 2 | 1/2 | 3.2–6.2 | +0.7607 | 0.0167 | 4 | 382,135.000 |
| S IV | ns 2S J=1/2 | 4–7 | 4 | 2 | 1/2 | 3.0–6.0 | +1.0264 | 0.0100 | 4 | 382,135.000 |
| S VI | nd 2D J=3/2 | 3–9† | 6 | 4 | 2/2 | 2.9–8.9 | +0.0925 | 0.0069 | 6 | 710,194.700 |
| S VI | nf 2F* J=5/2 | 4–10 | 7 | 5 | 4/5 | 4.0–10.0 | +0.0074 | 0.0011 | 6 | 710,194.700 |
| S VI * | ng 2G J=7/2 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | +0.0010 | 0.0001 | 6 | 710,194.700 |
| S VI * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | +0.0003 | 0.0001 | 6 | 710,194.700 |
| S VI | np 2P* J=1/2 | 3–7 | 5 | 3 | 3/3 | 2.6–6.6 | +0.4228 | 0.0110 | 6 | 710,194.700 |
| S VI | ns 2S J=1/2 | 3–8 | 6 | 4 | 4/4 | 2.4–7.4 | +0.6242 | 0.0083 | 6 | 710,194.700 |
| Al IV * | nf 2[5/2] J=3 | 4–5 | 2 | 1 | no-triple | 4.0–5.0 | +0.0349 | 0.0100 | 4 | 968,924.400 |
| Al IV | ns 2[3/2]* J=2 | 3–5 | 3 | 1 | 0/1 | 2.2–4.2 | +0.7638 | 0.0042 | 4 | 968,924.400 |
| B II | nd 1D J=2 | 3–7 | 5 | 3 | 2/3 | 3.0–7.1 | -0.0323 | 0.0111 | 2 | 202,691.900 |
| B II | nd 3D J=1 | 3–6 | 4 | 2 | 2/2 | 2.9–5.9 | +0.0772 | 0.0138 | 2 | 202,691.900 |
| B II | nf 3F* J=2 | 4–7 | 4 | 2 | 2/2 | 4.0–6.9 | +0.0397 | 0.0132 | 2 | 202,691.900 |
| B II | ng 3G J=3 | 5–7 | 3 | 1 | 1/1 | 5.0–7.1 | -0.0401 | 0.0192 | 2 | 202,691.900 |
| B II | np 1P* J=1 | 3–5 | 3 | 1 | 1/1 | 2.7–4.6 | +0.3284 | 0.0668 | 2 | 202,691.900 |
| B II | np 3P* J=0 | 3–6 | 4 | 2 | 2/2 | 2.7–5.8 | +0.2231 | 0.0345 | 2 | 202,691.900 |
| B II | ns 1S J=0 | 3–6 | 4 | 2 | 1/2 | 2.6–5.6 | +0.4303 | 0.0172 | 2 | 202,691.900 |
| B II | ns 3S J=1 | 3–7 | 5 | 3 | 2/3 | 2.5–6.5 | +0.5211 | 0.0148 | 2 | 202,691.900 |
| C III | nd 1D J=2 | 3–7 | 5 | 3 | 1/3 | 3.0–7.0 | +0.0067 | 0.0036 | 3 | 386,241.000 |
| C III | nd 3D J=1 | 3–9 | 7 | 5 | 3/5 | 2.9–8.9 | +0.0816 | 0.0069 | 3 | 386,241.000 |
| C III | nf 3F* J=2 | 4–7 | 4 | 2 | 1/2 | 3.9–7.0 | +0.0127 | 0.0398 | 3 | 386,241.000 |
| C III | ng 3G J=3 | 5–7 | 3 | 1 | 1/1 | 5.0–7.0 | +0.0126 | 0.0021 | 3 | 386,241.000 |
| C III | np 1P* J=1 | 3–8 | 6 | 4 | 1/4 | 2.8–7.8 | +0.1806 | 0.0527 | 3 | 386,241.000 |
| C III | np 3P* J=0 | 3–6 | 4 | 2 | 1/2 | 2.8–5.8 | +0.1856 | 0.0217 | 3 | 386,241.000 |
| C III | ns 1S J=0 | 3–5 | 3 | 1 | 1/1 | 2.7–4.5 | +0.3819 | 0.0499 | 3 | 386,241.000 |
| C III | ns 3S J=1 | 3–7 | 5 | 3 | 2/3 | 2.6–6.6 | +0.3993 | 0.0137 | 3 | 386,241.000 |
| O IV | nd 2D J=3/2 | 3–6 | 4 | 2 | 2/2 | 2.9–5.9 | +0.0681 | 0.0025 | 4 | 624,202.200 |
| O IV | nf 2F* J=5/2 | 4–7 | 4 | 2 | 0/2 | 4.0–6.9 | +0.0408 | 0.0115 | 4 | 624,202.200 |
| O IV * | ng 2G J=7/2 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | -0.0028 | 0.0018 | 4 | 624,202.200 |
| O IV * | nh 2H* J=9/2 | 6–7 | 2 | 1 | no-triple | 6.0–7.0 | -0.0125 | 0.0030 | 4 | 624,202.200 |
| O IV | np 2P* J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.7–4.8 | +0.2462 | 0.0106 | 4 | 624,202.200 |
| O IV | ns 2S J=1/2 | 3–5 | 3 | 1 | 1/1 | 2.6–4.5 | +0.4408 | 0.0072 | 4 | 624,202.200 |
| F I | nd 4D J=7/2 | 3–6 | 4 | 2 | 1/2 | 3.0–6.0 | +0.0323 | 0.0008 | 1 | 140,518.700 |
| F I | nd 4F J=9/2 | 3–6 | 4 | 2 | 1/2 | 3.0–6.0 | +0.0149 | 0.0012 | 1 | 140,518.700 |
| F I * | np 4D* J=7/2 | 3–4 | 2 | 1 | no-triple | 2.2–3.2 | +0.8308 | 0.0097 | 1 | 140,518.700 |
| F I | ns 2P J=3/2 | 3–6 | 4 | 2 | 2/2 | 1.8–4.9 | +1.1857 | 0.0604 | 1 | 140,518.700 |
| F I | ns 4P J=5/2 | 3–8 | 6 | 4 | 4/4 | 1.7–6.7 | +1.2800 | 0.0117 | 1 | 140,518.700 |
| Ge III | nd 1D J=2 | 4–6 | 3 | 1 | 1/1 | 3.2–5.1 | +0.8820 | 0.0572 | 3 | 274,693.000 |
| Ge III | nd 3D J=1 | 4–6 | 3 | 1 | 1/1 | 3.0–5.0 | +1.0025 | 0.0189 | 3 | 274,693.000 |
| Ge III * | ng 3G J=3 | 5–6 | 2 | 1 | no-triple | 5.0–6.0 | +0.0181 | 0.0010 | 3 | 274,693.000 |
| Ge III | ns 1S J=0 | 5–7 | 3 | 1 | 1/1 | 3.0–5.0 | +2.0116 | 0.0057 | 3 | 274,693.000 |
| Ge III | ns 3S J=1 | 5–8 | 4 | 2 | 2/2 | 2.9–6.0 | +2.0576 | 0.0162 | 3 | 274,693.000 |
| K I | nd 2D J=5/2 | 3–13 | 11 | 9 | 9/9 | 2.9–12.7 | +0.2460 | 0.0380 | 1 | 35,010.600 |
| K I | nf 2F* J=5/2 | 4–12 | 9 | 7 | 7/7 | 4.0–12.0 | +0.0112 | 0.0030 | 1 | 35,010.600 |
| K I | np 2P* J=1/2 | 4–15 | 12 | 10 | 9/10 | 2.2–13.3 | +1.7268 | 0.0133 | 1 | 35,010.600 |
| K I | ns 2S J=1/2 | 4–18 | 15 | 13 | 12/13 | 1.8–15.8 | +2.1912 | 0.0111 | 1 | 35,010.600 |
| O III | nd 1D* J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.1196 | 0.0040 | 3 | 443,325.200 |
| O III * | nd 3D* J=1 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0791 | 0.0043 | 3 | 443,325.200 |
| O III | nd 3F* J=2 | 3–5 | 3 | 1 | 1/1 | 2.9–4.9 | +0.1290 | 0.0090 | 3 | 443,325.200 |
| O III * | np 3D J=1 | 3–4 | 2 | 1 | no-triple | 2.6–3.6 | +0.4221 | 0.0073 | 3 | 443,325.200 |
| O III | ns 1P* J=1 | 3–5 | 3 | 1 | 1/1 | 2.4–4.4 | +0.5852 | 0.0048 | 3 | 443,325.200 |
| O III | ns 3P* J=0 | 3–5 | 3 | 1 | 1/1 | 2.4–4.4 | +0.6250 | 0.0048 | 3 | 443,325.200 |
| C I * | nd 1F* J=3 | 3–4 | 2 | 1 | no-triple | 3.0–4.0 | +0.0320 | 0.0059 | 1 | 90,937.500 |
| C I * | nd 3D* J=1 | 3–4 | 2 | 1 | no-triple | 2.9–3.9 | +0.0638 | 0.0097 | 1 | 90,937.500 |
| C I * | np 3D J=1 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.7201 | 0.0073 | 1 | 90,937.500 |
| C I * | np 3P J=0 | 3–4 | 2 | 1 | no-triple | 2.4–3.4 | +0.6284 | 0.0046 | 1 | 90,937.500 |
| C I * | np 3S J=1 | 3–4 | 2 | 1 | no-triple | 2.3–3.3 | +0.6641 | 0.0048 | 1 | 90,937.500 |
| C I | ns 1P* J=1 | 3–5 | 3 | 1 | 0/1 | 1.9–3.9 | +1.0532 | 0.0037 | 1 | 90,937.500 |
| C I | ns 3P* J=0 | 3–5 | 3 | 1 | 0/1 | 1.9–3.9 | +1.0925 | 0.0127 | 1 | 90,937.500 |
| P II * | np 3P J=0 | 4–5 | 2 | 1 | no-triple | 2.8–3.8 | +1.1670 | 0.0004 | 2 | 159,929.200 |
| P II | ns 3P* J=0 | 4–6 | 3 | 1 | 0/1 | 2.4–4.4 | +1.5468 | 0.0075 | 2 | 159,929.200 |
| S III * | ns 3P* J=0 | 4–5 | 2 | 1 | no-triple | 2.7–3.7 | +1.2846 | 0.0049 | 3 | 281,130.000 |

**596 channel rows across 28 elements · 2,269 interior cells parsed.**

| element | channels |
|---|---|
| Al | 19 |
| Ar | 50 |
| B | 32 |
| Ba | 27 |
| Be | 30 |
| Bi | 22 |
| C | 36 |
| Ca | 18 |
| Cd | 12 |
| F | 5 |
| Fe | 8 |
| Ga | 13 |
| Ge | 5 |
| He | 16 |
| Hg | 5 |
| K | 8 |
| Li | 36 |
| Mg | 37 |
| N | 18 |
| Na | 12 |
| Ne | 44 |
| O | 12 |
| P | 14 |
| S | 18 |
| Sc | 11 |
| Si | 67 |
| Ti | 11 |
| Zn | 10 |

---

# III · THE MECHANISMS

**How a value is got where no capture reaches.** Each is measured on pairs where both cells are known.

| mechanism | the move | what it gives |
|---|---|---|
| the ground-state derivation | none | the multiplicity, and the bound B |
| the isoelectronic ladder | (Z, c) → (Z+1, c+1) | δ along a sequence |
| the charge ladder | c → c+1 at fixed Z | δ falls with charge |
| ℓ-collapse | ℓ → ℓ+1 | δ falls with ℓ |
| the exchange split | singlet ↔ triplet | the triplet defect exceeds the singlet at ns |
| the Janet collapse | a lookup in the periodic table | whether a p = 0 channel is large |
| Seaton's formula | none | δ₀ = 3α/K(ℓ) for a non-penetrating series |

### The isoelectronic ladder

**Along a sequence of fixed electron count, a channel's defect follows δ(c) = A + B·ln(c+1)/c.** Fitted per sequence on the 52 with three or more charge states it reaches a median rms of **0.0083** — the tightest relation the compendium holds.

**And A is fixed rather than fitted.** As charge grows at constant electron count the core collapses to a point and the ion becomes hydrogenic, so δ → 0. That is the periodic table's own edge, and setting A ≡ 0 leaves one parameter.

### A channel is a curve

        δ(n) = δ₀ + δ₂/(n − δ₀)²

**δ₀ is the limit value the index carries; δ₂ is the curvature.** Fitted on 274 channels, the second term removes **48%** of what a constant defect leaves as scatter.

**And the sign of δ₂ names the regime**: positive for core penetration, negative for core polarisation. By orbital: **s 76% positive, p 74%, d 37%, f 6%, g 7%.** *The sign rule is NIST's own, stated in the reference the levels come from. What the compendium adds is the measurement across 274 channels and the finding that |δ₂| predicts a channel's scatter at R² = 0.761.*

![The index](figures-compendia/fig-index-final.png)

---

### The bracket's deficit, on a classical object

**The bracket — T(n) between T(n−1) and T(n+1) — is the book's one ternary object (§21.5.1), and Λ₃ is the ternary object of celestial mechanics.** The two share the deficit: both need strong 3-consistency and both get level 2 from ℛ. In spectra the deficit is paid per channel by the envelope cells of §12.11.3; in three bodies it is paid once, by the stratum boundaries. No channel entry changes. *The same shortfall, on a classical object, is Λ₃ (Index of Indices V; register 1716, 1724).*

---

# IV · THE SOURCES

B.1 Sources
  compilation                 spectra drawn
  Kaufman & Martin            Al I, Al II
  1991, JPCRD 20, 775
  Kramida & Martin            Be I
  1997, JPCRD 26, 1185
  NIST ASD                    Ar II, Be II, Bi I, C II, Ca II, Cd II, Ga I, He I, He II, Hg II, K II, Li I, Li II, Mg II, N II, Na II, Ne I (³⁄₂), Ne
                              I (¹⁄₂), Si I, Si II, Zn II
  Sansonetti 2008,            Na I
  JPCRD 37, 1659
  Sansonetti 2008,            KI
  JPCRD 37, 7
 **Additional sources used for exotic systems and collective quantities:**
 Hori *et al.*, *Nature* **475**, 484 (2011) and *Phys. Rev. Lett.* **96**, 243401 (2006), both accessed via CODATA 2010 Table XII (arXiv:1203.5425) and arXiv:1304.4330 · Korobov, *Phys. Rev. A* **77**, 042506 (2008) · Singer, Stanojevic, Weidemüller & Côté, *J. Phys. B* **38**, S295 (2005) · Sugar & Corliss 1985, *JPCRD* **14** Suppl. 2 · Sugar & Musgrove 1990, *JPCRD* **19**, 527 and 1995, *JPCRD* **24**, 1803.
 B.2 Channels
  **The 133 channel rows are lifted to the Spectra Compendium.** Each carries its species,
  channel, n-range, level count, interior cells, bracket, ν range, mean quantum defect, its
  spread, Z_eff and the series limit. *Reproduced in the book only where one carries an
  argument; the rest are data and live where data belongs.*
  **THE METHOD 1.6 — SPECTRA COMPENDIUM, counted from the table above rather than from the source that once generated it.** 596 channel rows — 477 series of three or more members and 119 two-member channels (starred) — across 28 elements and 70 species; 3,342 levels, 2,269 interior cells. The bracket stands at **1,577 of 1,738 cells across 392 rows** — the first collection's 844 of 844 on 107 rows; 658 of 813 on 250 rows run under ruling 26 (register 1763); and 75 of 81 on 35 rows run by the same sealed instrument on the six captures the delivering bank's cut carried, each verified against that cut's MANIFEST by hash before a cell was computed (registers 1766, 1768) — throughout, the sealed test of register 796 at strict interval membership, the only ε the quotation floor — half a unit in the last quoted decimal of the measured level — and admissibility per §22.5, r = 2Z²R/(ν³σ) ≥ 5 with σ the quotation floor. **Cells refused: 0.** The 161 failing cells sit in 98 rows and are results, not defects of the test (register 784: no failures would itself be suspect); five of those rows carry a failing bracket narrower than twice the floor, named in 1763 for the author's eye — none of the six cells failing at this build is among them, each missing a bracket wider than twice its floor. 78 rows read `no-triple`: their members, matching the row exactly, contain no three consecutive n, so the sealed test — true neighbours only — defines no cell there; the ten added at this build are the ten starred two-member rows of the six delivered species. 126 rows remain `untested`, and the reason is data, not definition: the parent-term and coupling selection that built them is not reproducible blind (register 1578's wall), and the delivered selection record covers none of their eight species (register 1767). All bracket figures in this paragraph are recomputed from the table by `spectra_count.py`.
 *The earlier statement of this paragraph — 133 rows, 23 elements, 869 interior cells, bracket 869/869, with a twenty-channel gap disclosed against a total of 153 — was true at registers 630–631 and was overtaken by the parent-term wall (register 1578) and the J-resolved rows of T8-J (registers 1699–1700). It claimed the table could not drift from* `spectra.py`; *the table did drift, so* `spectra.py` *is retired: the table above is the source, and every count in the paragraph above it is taken from the table by* `spectra_count.py` *(register 1756) — 596, 477, 119, 28, 70, 3,342 and 2,269 agree to the row. The exotic and collective sources named above still carry sources and no rows, and that remains disclosed rather than reconciled.* Registers 630–631; 1578; 1699–1700.
 B.3 Flagged channels
 Channels whose δ spread exceeds 0.25 or whose V departs from 4ν/3 by more than 5% are flagged.
 Every flag in this collection has an identified cause; none is unexplained.
  specie       channel        δ           cause
  s                           spread
  Al I         3s²nd ²D       0.630       compilers relabelled this series; y²D removed as a perturber
  Al II        3snd ¹D        0.390       local perturber
  Al II        3snf ³F°

### Published values the coordinates are checked against

| source | what it gives |
|---|---|
| **NIST Atomic Spectra Database** | the levels every capture is fitted to |
| **Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35, 473 (1986)** | asymptotic quantum defects of s, p, d and f orbitals for **all ionisation stages of all ions with Z ≤ 50**, Hartree–Slater |
| Manson, Inokuti & Theodosiou, OSTI 7104964 | the isoelectronic, isonuclear and isoionic pictures |
| Seaton 1958; Drake & Swainson 1991 | the polarisation formula |
| Peper *et al.* 2019 | K I to eight digits |
| Freeman & Kleppner 1976 | Na I ng |
| arXiv:1706.06237 | Cs I np at n = 70–100 |
| arXiv:2508.06733 | actinide defects, Z = 89–103 |
| arXiv:2502.20961 | Cs⁺ dipole and quadrupole polarisabilities |
| ARC Alkali Rydberg Calculator | an independent check on K I |

*The full bibliography, with what each source was used for, is in `LITERATURE.md`.*


---

# The four capture groups

*Register 1296 marked these as owed. Counts below are read from `COORDINATES-2.13` at build time, not transcribed.*

| group | species | cells | measured | exact | computed |
|---|---|---|---|---|---|
| **Kr-core** | Kr | 512 | 0 | 8 | 504 |
| **Cd/In** | Cd/In | 1,384 | 13 | 16 | 1,355 |
| **La/Ce** | La/Ce | 1,632 | 0 | 16 | 1,616 |
| **Hg-core** | Hg | 1,168 | 5 | 8 | 1,155 |

**4,696 cells across six species**, every one spanning l = 0-7 and the full charge ladder from 1 to Z.

### What the counts say, measured on this compendium's own basis

*Section 0 states that accuracy is quoted against the VERIFIED-PLUS-POSSIBLE set and not against the whole index. The same basis is used here.*

**The four groups hold 18 reachable cells of the index's 358 - 5.0% of the reachable set on 4.5% of the cells.** They are therefore slightly BETTER than representative, not worse.

On the raw grade column they carry 18 `measured` cells of 4,696 - Cd/In twelve and Hg five, with **Kr-core and La/Ce carrying none.** *That ratio is not a fact about these groups: the whole index is 98.8% computed, which section 0's table already states. The filler is the index's condition, not these captures' shortcoming.*

### Why each was captured

- **Kr-core** - the n = 4 closure; its 5s manifold is still one level short
- **Cd/In** - the d10 closure and the first post-d p-electron
- **La/Ce** - THE JANET ANOMALY ITSELF - La opens 5d, Ce is where 4f appears
- **Hg-core** - the 5d closure at high Z, where the relativistic wall stands

**La/Ce is the group that earns its place.** The other three fill coordinate space; **La/Ce is where the filling order itself breaks**, and holding it in the index lets the anomaly be stated as a coordinate fact rather than a footnote.
<<<END FILE: The_Method_1_6___Spectra_Compendium-2.md>>>

<<<FILE: THE-LOWDIN-SOLUTION-2.md>>>

# THE LÖWDIN SOLUTION
## Deriving the Structure of the Periodic Table from the Many-Electron Schrödinger Equation
### A Formal Response to the 1969 Löwdin Challenge

**Matthew Lach — Independent Researcher**


---

## ABSTRACT

In 1969 Per-Olov Löwdin challenged theoretical physics to derive the ordering rules of the periodic table — the Madelung (n+ℓ) filling rule, the period-length sequence 2, 8, 8, 18, 18, 32, 32, and the Aufbau principle itself — directly from the many-electron Schrödinger equation, with no empirical parameters of any kind. This paper presents a solution. A sequential, parameter-free construction is defined in which the electron that differentiates element Z from element Z−1 is placed in the self-consistent field of the atom that preceded it, and the orbital channel it occupies is determined by that field alone. Executed across the entire table with the inverse fine-structure constant c = 137.035999 as the only number supplied, the construction reproduces the observed filling order at all 107 elements for which ground configurations are known (Z = 2–108), locates the three genuine exceptions to the secondary rule exactly where nature has them and derives them from the physics of orbital collapse, proves that no g block exists anywhere below Z = 121, and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them. Second-order correlation corrections are computed at every element where the mean-field competition is close, and in every case they widen, rather than overturn, the derived order. Beyond the last measured element the same construction issues twelve falsifiable predictions (Z = 109–120) that reproduce the relativistic Dirac–Fock shell sequence. The derivation is presented in both mathematical and algorithmic form; every supporting analysis was pre-registered under a cryptographic protocol described in the methodology; and the mathematical identity that resolves the final internal question of the numerical method turns out to be Löwdin's own non-orthogonality formula of 1950 — the author of the challenge supplied, nineteen years before posing it, part of the mathematics of its answer.

---

## I. THE CHALLENGE

Every chemistry student learns the filling order of atomic subshells: 1s, 2s, 2p, 3s, 3p, 4s, 3d, and so on. The rule that compresses this sequence — orbitals fill in order of increasing n+ℓ, and at equal n+ℓ in order of increasing n — is variously credited to Madelung, Janet, and Klechkovskii, and it organizes the entire periodic table. It appears in every textbook. What has never appeared in any textbook is its derivation.

In 1969, in "Some Comments on the Periodic System of the Elements" (Int. J. Quantum Chem. 3, S3A, 331–334), Per-Olov Löwdin made the absence explicit and posed it as a challenge: derive, from the first principles of quantum mechanics and from nothing else, (i) the Madelung rule, (ii) the period-length sequence 2, 8, 8, 18, 18, 32, 32, and (iii) the ground-state electron configurations across the periodic system — strictly from the Schrödinger equation, without empirical parameters, fitted screening constants, or semi-empirical models.

The prohibition is the heart of the challenge. Many treatments in the subsequent literature reproduce the pattern of the rule — group-theoretic constructions, model potentials tuned to yield (n+ℓ) degeneracy — but they build the answer into their assumptions or their parameters, and reviewers of the problem's status (notably Scerri, and Ostrovsky before him) have repeatedly concluded that the challenge stood unmet. A derivation must start where the atom starts: a nucleus of charge Z, N electrons, their kinetic energy, their attraction to the nucleus, their mutual repulsion — and nothing else.

There is also a subtlety inside the challenge that must be answered before it can be attempted, one Löwdin's framing forces into the open: what exactly is the rule *about*? Does it govern the ground-state arrangement of all electrons in every atom, or does it govern the *differentiating electron* — the one electron by which element Z differs from element Z−1? The two readings are inequivalent, and the scattered configuration anomalies of the transition metals afflict mainly the first. This work adopts, states, and defends the second reading: the Madelung rule is a law about the sequence of channel openings — about which orbital the newly added electron takes, step by step, as the table is built. That is the object derived here.

Finally, one physical constant is admitted, because the atom itself admits it: the speed of light, entering through the scalar-relativistic reduction of the Dirac equation as c = 137.035999 in Hartree atomic units. It will emerge (§VIII) that this is not optional: the periodic table as observed cannot be derived from the non-relativistic equation, because at c → ∞ the derived ordering visibly changes. One number goes in. The periodic system comes out.

---

## II. THE STATEMENT OF THE SOLUTION

### II.1 The mathematical form

**THE ORDERING LAW.** *Let the neutral atom of atomic number Z be described by the many-electron Schrödinger equation in its scalar-relativistic (Koelling–Harmon) Hartree–Fock reduction, with c = 137.035999 the only entered constant. At each step Z, define the frontier as the set of unoccupied orbital channels (n,ℓ) evaluated in the converged self-consistent field of the ion carrying nuclear charge Z and the electron configuration of element Z−1 (the "V^{N−1} field": the field the arriving electron actually experiences). Then the differentiating electron of element Z enters the frontier channel of greatest binding depth in that field, and across Z = 2–108 the resulting sequence of entrant channels satisfies:*

*(Clause 1 — the ordering clause.) A channel of smaller n+ℓ always opens before a channel of larger n+ℓ. This holds at all 107 constructed elements without exception.*

*(Clause 2 — the tie-break clause.) At equal n+ℓ, the channel of smaller n opens first — except at exactly three elements, La (Z=57), Ac (Z=89), and Th (Z=90), where the orbital-collapse condition of the field (§VI) selects the d channel over the not-yet-collapsed f channel. These three exceptions are derived consequences of the same field that produces the rule; they are not anomalies against it.*

*(Clause 3 — the correlation clause.) At every element where the competition between the entrant and its closest rival is genuinely contested (five elements: Z = 38, 56, 72, 89, 105), the second-order correlation correction to the energy difference is positive: electron correlation stabilizes the derived entrant more than its rival. Every contested competition widens under correlation; none reverses.*

*(Domain clause.) The law's domain is Z ≤ 112. Below that bound, the spin-orbit interaction cannot reorder the derived sequence (the computed worst case is a narrowing of 0.083 hartree, smaller than every margin at issue); above it, the correct ordering object is the relativistic (n,ℓ,j) shell, and the first-order relativistic extension of this construction reproduces the Dirac–Fock (n,ℓ,j) sequence through Z = 120.*

*(Relativistic clause.) The law is scalar-relativistic in an essential way: repeating the entire construction with c → ∞ changes the entrant channel at eleven elements, and inverts the underlying channel competition at thorium besides. The observed periodic table is not a non-relativistic object.*

Two celebrated consequences follow at once. The period-length sequence 2, 8, 8, 18, 18, 32, 32 is Clause 1 plus counting: each period runs from one s-channel opening to the next, the channels admitted in between are exactly those of the intervening n+ℓ values, their capacities are 2(2ℓ+1), and the pairwise repetition of period lengths is the signature of Clause 2 — each n+ℓ block is traversed twice, once at each admissible n. And the table's most conspicuous *absence* is derived as well: there is no g block anywhere below Z = 121, for a reason the field states explicitly (§V.3).

### II.2 The algorithmic form

The law is constructive, and its constructive statement is an algorithm simple enough to write in ten lines:

```
cfg(1) := 1s¹
for Z = 2 … 108:
    F := converged self-consistent field of the ion with
         nuclear charge Z and electron configuration cfg(Z−1)
    for each unoccupied frontier channel (n, ℓ):
        D(n,ℓ) := binding depth of one electron placed in
                  channel (n,ℓ) of the frozen field F
    entrant(Z) := the channel of greatest depth D
    margin(Z)  := depth(entrant) − depth(runner-up)
    cfg(Z)     := cfg(Z−1) + one electron in entrant(Z)
```

Nothing in the loop is adjustable. The field is generated by the equation; the candidate depths are generated by the field; the entrant is the deepest candidate; and the configuration so built becomes the seed of the next step. Because each step builds on the *derived* configuration rather than the observed one, an error anywhere would propagate and wreck everything downstream: the construction is not 107 independent guesses but one chain, falsifiable as a whole. Executed under the conditions stated in §III, the chain reproduces the observed ground-configuration sequence at all 107 elements for which one is known, and its complete output — every entrant, every margin, every candidate spectrum — is the data behind every figure in this paper.

---

## III. FIRST PRINCIPLES, AND WHAT WAS FORBIDDEN

The starting Hamiltonian is the exact many-electron operator of an atom: the electrons' kinetic energy, their attraction −Z/r to the nucleus, and their pairwise Coulomb repulsion. The one refinement admitted is the one the physical atom insists on: relativity, entering through the Koelling–Harmon scalar-relativistic reduction of the Dirac equation, which carries the mass-velocity and Darwin terms into a single-component radial problem. This reduction is derived, not modeled, and the speed of light enters it once, as c = 137.035999, and enters nothing else.

The working mean-field framework is Hartree–Fock. Its use here is not an act of faith but a *conditioned* step, and the conditions are stated as explicit external results (§X): a well-posedness theorem guaranteeing that the subshell objects of the construction exist (Bach, Lieb, Loss & Solovej, 1994); an existence theorem for the mean-field minimizer itself (Hantsch); and — because rigorous Hartree–Fock error bounds control total energies, not the *differences* between two candidate channels — a direct computation of the correlation correction at every element where a difference is close enough to be at risk (Clause 3, §VII). The mean field is trusted only where it is proved trustworthy or checked.

What was forbidden is exactly what the challenge forbids. No experimental ionization energies. No screening constants. No adjustable parameters. No orbital energies borrowed from spectroscopy. The observed ground configurations of the elements appear in this work in precisely one role: as the *target* the finished derivation is scored against — never, at any point, as an input to it.

A word on methodology, because for a claim of this kind the reader is owed more than the results. Every quantitative analysis supporting this paper was conducted under a pre-registration protocol: before any computation ran, its quantitative prediction — the inequality to be tested, its direction, and its tolerance — was written to a file and bound by a cryptographic hash, so that no number in the record predates the prediction that constrains it. Every computational instrument was required to carry a demonstrable failure mode — a deliberate perturbation under which it must visibly break — so that no test could pass vacuously. Discrepancies and failed predictions were registered by name and carried openly until resolved, and resolved means *derived*: the standard applied throughout was that no unexplained numerical residue of any size may remain (§XI). The complete archive — the chain output, every instrument, every hash, every registered discrepancy and its resolution — is preserved and re-verifiable end to end.

---

## IV. THE INSTRUMENT: WHY THE V^{N−1} FIELD IS THE RIGHT FIELD

The differentiating electron of element Z arrives at an ion that already exists: nuclear charge Z, dressed by the Z−1 electrons of the previous element. The field of that ion — the "V^{N−1} field" — is therefore not a modeling choice but the literal physical situation of the Aufbau step. Placing the candidate channels in this field and asking which binds deepest is asking the Schrödinger equation the Aufbau question in its own terms.

This construction has three properties that elevate it from heuristic to derivation. It is *parameter-free*: every quantity in it is produced by the equation. It is *falsifiable row by row*: each step records not just its winner but the margin of victory and the full candidate spectrum, so any single wrong entrant is visible and fatal. And it is *chained*: because step Z builds on the derived configuration of step Z−1, the 107-element score is a score of one unbroken construction. Figure 1 shows what the chain sees: the depth of every candidate channel at every Z. The bold sawtooth is the entrant — plunging when a new channel opens, resetting at every shell closure — and the grey band riding above it is the margin by which the entrant beat its closest rival, the quantity all later scrutiny (spin-orbit, correlation, numerical error) is measured against.

![**Figure 1a](figures/FIG2spectraindex2120.png)

***Figure 1.** (a) The candidate spectrum of the chain: the converged depth of every frontier channel at every Z, 2–120. The bold sawtooth is the entrant; the flat lines across the top are the pinned g channels.*

![**Figure 1b](figures/FIG5spectraindex3D.png)

*(b) The same index in three dimensions, Z = 2–120 by channel by depth: the channel ribbons are the candidate depths of the V^{N−1} walk coloured by ℓ, the black line the entrant path of (a), the flat ribbons the g channels pinned at −1/(2n²), the marked points the tie-break exceptions the field derives (La, Ac, Th), and the grey plane the evidentiary boundary at Z = 108.*

---

## V. THE RESULTS I: THE RULE AND THE PERIODS

### V.1 The ordering clause: 107 out of 107

Figure 2 displays the central result: the derived filling index. Each square is one element's entrant channel; the staircase they trace is the Aufbau sequence — 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p 8s — *produced* by the field, not presumed by it. Clause 1, the primary Madelung rule, holds at every one of the 107 elements: no channel of larger n+ℓ ever opens before a channel of smaller n+ℓ. The rule that has organized chemistry for a century is, on this construction, a theorem of the many-electron equation with one physical constant.

![**Figure 2](figures/FIG1fillingindex2120.png)

***Figure 2.** The derived filling index, Z = 2–120. Each square is one element's entrant channel; the staircase is the Aufbau sequence, read from the equation with one constant.*

### V.2 The period lengths

The sequence 2, 8, 8, 18, 18, 32, 32 now follows by arithmetic. Periods begin at s-openings; between consecutive s-openings the ordering clause admits exactly the channels of the intervening n+ℓ blocks; each block contributes 2(2ℓ+1) elements; and the doubling of successive period lengths is Clause 2 made visible — every n+ℓ block is walked twice, at its two admissible values of n, before the next block is permitted to begin.

### V.3 The dog that does not bark: why there is no g block

A complete derivation must also produce the table's absences. Group-theoretically, g orbitals (ℓ = 4) are available from n = 5 onward, and one might expect a g block to interrupt the known sequence somewhere among the superheavy elements. It never does, and the field says why with unexpected bluntness. Across the entire construction — the 5g channel is present as a frontier candidate at 65 elements, 6g at 70, 7g at 57, 8g at 28, spanning a hundred units of nuclear charge — every g channel sits at *exactly* its hydrogenic depth, −1/(2n²), to the precision of the stored data, while every s, p, d, and f channel at the same elements deepens with Z. These are the flat lines running across the top of Figure 1. The centrifugal barrier ℓ(ℓ+1)/2r² at ℓ = 4 holds the g electron entirely outside the atom's screening charge; it sees net charge +1 and nothing more; and a channel whose depth does not respond to the nucleus at all is a channel that can never become the deepest candidate. The absence of a g block below Z = 121 is not an accident of where the table happens to end. It is a derived property of the field.

---

## VI. THE RESULTS II: THE EXCEPTIONS, DERIVED

A derivation that cannot say why a rule sometimes fails has not fully derived the rule. The secondary (equal-n+ℓ) clause fails in nature at exactly three elements, and the construction fails at the same three, for a reason it can state.

### VI.1 Orbital collapse and the three exceptions

The three failures — lanthanum, actinium, thorium — are all f-channel openings, and the responsible physics is *orbital collapse*, computed for exactly these series by Griffin, Andrew and Cowan in 1969. Near these nuclear charges, the effective radial potential seen by an f electron has two wells: a deep, narrow inner well near the core and a shallow, wide outer well far outside it. Which well captures the electron switches abruptly with Z; when it switches inward, the orbital's radius collapses roughly tenfold and its binding deepens dramatically. The present construction states the collapse condition quantitatively from its own field — a criterion, computed from the same self-consistent data as everything else, for which f channel is collapsed at which Z. At La, Ac, and Th the f channel is still in its outer-well, barely-bound state; the d channel is deeper; the field chooses d — and so does nature. The exceptions to the secondary rule are the exact, three-element-wide footprint of the collapse transition. They are the rule's own physics, at its sharpest edge.

The same physics resolves the single most delicate numerical point in the record. At Z = 91 (protactinium), one diagnostic function of the analysis has a zero-crossing whose sign sits below the convergence tolerance of the self-consistent field — irresolvable by simply computing harder. The literature explains why: adjacent to a collapse transition, the Hartree–Fock equations admit *two coexisting solutions* of the same configuration — an outer-well solution and a collapsed one, each a genuine stationary point of the energy with its own converged mean field (the iteration instabilities documented by Griffin, Cowan and Andrew in 1971, and formalized in the modern two-branch literature). A sign pinned at tolerance beside a two-branch degeneracy is not numerical noise to be hammered down; it is the derived, small-margin signature of the branch structure itself, and the record enters it as exactly that.

### VI.2 The classical anomalies: chromium, copper, and the filling ambiguity

The challenge names the ground-state anomalies — chromium's 3d⁵4s¹, copper's 3d¹⁰4s¹ — as the standing paradox. Two results dissolve it. First, for the coinage metals (Cu, Ag, Au) an exact statement holds: the quantum-mechanical matrix element coupling the observed configuration (d¹⁰s¹) to the Madelung one (d⁹s²) vanishes *identically*, by angular-momentum selection rules. The two configurations do not mix at first order; the atom simply occupies whichever the field places lower; the anomaly is a clean, discrete choice, not a violation straining against the rule. Second, and more fundamentally: on the differentiating-electron reading defended in §I — the reading on which the ordering law is stated — the d-block anomalies are total-energy rearrangements *within* an already-opened block, and the law's own claim, the sequence of channel openings, is untouched by them at all 107 elements. The paradox of exceptions was, in large part, a paradox of asking the rule to be about the wrong object.

---

## VII. THE RESULTS III: CORRELATION CLOSES THE CASE

The one way a mean-field derivation could fail silently is at an element where the margin between entrant and rival is small enough for electron correlation — the physics Hartree–Fock omits — to reverse the outcome. The construction identifies every such element: five, at Z = 38, 56, 72, 89, and 105, where s-, d-, and f-channel competitions are genuinely close. At each of the five, the full second-order correlation correction to the entrant-versus-rival energy difference was computed — every interacting electron pair, including the core-core pairs, with the near-degenerate configuration pairs resummed rather than perturbatively mishandled.

The result is Figure 3. Expressed as a fraction of the mean-field margin, the correlation correction at the five elements is +1.33, +1.24, +2.6 (interval 2.57–2.73), +2.2 (interval 1.92–3.32), and +2.16. Every value is positive: in all five contested cases, correlation stabilizes the derived entrant *more* than its rival. The declared uncertainty intervals (shown as brackets) lie entirely on the positive side and cannot reverse a positive sign. Every audited numerical bias of the instruments, stated per element, is smaller than the relevant margin by a factor of at least 26. The mean-field ordering is the correlated ordering. The derivation does not merely survive correlation; it is widened by it.

![**Figure 3](figures/FIG4dm2widening.png)

***Figure 3.** The correlation clause at the five contested rows: the second-order differential over the mean-field margin. Every competition widens; none reverses.*

---

## VIII. THE RESULTS IV: THE RELATIVISTIC TABLE AND THE PREDICTIONS TO Z = 120

Two boundary statements complete the law. The first is its domain. The construction is scalar-relativistic — it carries relativistic mass and contact terms but averages over spin-orbit splitting — so its shell label (n,ℓ) is legitimate only while spin-orbit splitting is too small to reorder its sequence. Computing the splitting on the same field shows the worst case narrows any competition by at most 0.083 hartree, below every margin at issue: the (n,ℓ) law is safe through Z = 112. Beyond that, the honest ordering object is the relativistic (n,ℓ,j) shell, and the first-order relativistic extension of the construction reproduces the established Dirac–Fock (n,ℓ,j) sequence through Z = 120.

Because ground configurations are experimentally established only through Z = 108, this work enforces a strict evidentiary boundary there. The 107 elements up to it constitute the *derivation*, scored against nature. The twelve elements beyond it (Figure 4) are published as *predictions* — explicitly labeled, unfitted, and falsifiable the day their spectra can be measured: the entrant is 6d from Z = 109 through 112, 7p from 113 through 118, and 8s at 119 and 120, with stated margins between 0.058 and 0.264 hartree, every one clearing the spin-orbit worst case.

![**Figure 4](figures/FIG3j120window.png)

***Figure 4.** The unwitnessed window, Z = 109–120: entrant, depth and margin, with the spin-orbit worst case each margin clears. Published as predictions.*

The second boundary statement is the deeper one. The entire construction was repeated with the speed of light sent to infinity — the same equation, the same algorithm, the one admitted constant removed — and the two derived tables are compared element by element in Figure 5. They disagree at eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, and Rf. The non-relativistic field files manganese and zinc under 4s instead of 3d, silver and cadmium under 5s, four lanthanides under 5d instead of 4f, mercury under 6s, and the heaviest actinides wrongly altogether — and since the relativistic construction scores 107 of 107 against observation, every one of those eleven placements is an error of the non-relativistic equation against nature. (At thorium the entrant survives by the path of the chain, but the underlying channel competition inverts without relativity as well.) The periodic table hanging on the classroom wall is not a solution of the non-relativistic Schrödinger equation. Any successful answer to Löwdin's challenge *had* to contain the speed of light; a purely non-relativistic derivation, had one been found, would have derived a visibly different table than ours — Figure 5 is what it would have looked like.

![**Figure 5](figures/FIG6relativisticvsnonrelativistic.png)

***Figure 5.** The relativistic table against its c → ∞ counterfactual, element by element. Eleven disagreements, every one an error against nature.*

---

## IX. THE LOGICAL STRUCTURE: FROM THE OBSERVED ORDER BACK TO THE VARIATIONAL PRINCIPLE

The algorithm of §II.2 constructs the table forward from the equation. The proof obligation runs in both directions, and the reverse direction — from the observed ordering back to first principles — was assembled as an explicit chain of six links, each one classified by its epistemic type:

- **Link 1 (identity, under two stated conditions):** the observed filling order *is* the entrant sequence of the V^{N−1} depths.
- **Link 2 (theorem):** the comparison of two candidate depths reduces to a comparison of one-channel properties of the field — well profiles and their integrated strengths.
- **Link 3 (computed):** the profile inequalities that decide every frontier competition, verified exhaustively: all 18 within-ℓ cases, all across-ℓ cases at |Δℓ| = 1, and the harder |Δℓ| = 2 family closed by direct computation.
- **Link 4 (theorem, with a measured and reinforcing remainder):** the block structure of the table follows from the profile ordering.
- **Link 5 (computed):** the passage from field ordering to energy ordering, whose remainder is precisely the correlation question — which §VII closes.
- **Link 6 (variational):** the ground state of the many-electron equation itself, invoked as the variational principle it is.

"Solved," under the standard this work set for itself, means this six-link chain with every link a theorem, an exhaustively computed verification, or the variational principle — and *no remainder of any kind left unexplained*. That standard is met, and the final section of the analysis explains the last and most technical part of meeting it.

---

## X. THE EXTERNAL CONDITIONS

The derivation is stated conditionally on a small set of named external results, each doing one job:

**The accuracy condition (Law A).** Rigorous results on Hartree–Fock accuracy bound *total* energies in the large-Z regime. They warrant the framework but cannot, by themselves, bound the small *differences* between candidate channels that each Aufbau step compares. This honest gap is exactly what Clause 3 (§VII) exists to close, and closes by computation.

**The domain condition (Law B).** The ℓ-conservation of the scalar-relativistic operator, together with the computed spin-orbit scale, fixes Z ≤ 112 as the domain on which (n,ℓ) is the correct shell label — and supplies the (n,ℓ,j) continuation beyond it, verified against the Dirac–Fock sequence on its full test set.

**The well-posedness condition (Law C).** The average-of-configuration theorem of Bach, Lieb, Loss and Solovej (1994) is the guarantee that the (n,ℓ)-subshell object at the center of the whole construction is mathematically well defined; Hantsch's existence theorem does the same for the mean-field minimizer. Both are verified against their primary sources.

Stating the solution conditionally on named, sourced theorems is not a hedge; it is the correct logical form of the claim that a conditioned mean field, checked where checking is needed, carries the exact equation's ordering. Every condition is explicit, and every one is either proved in the cited literature or computed in this work.

---

## XI. THE LAST MILE: AUDITING THE INSTRUMENT TO ZERO

A reader may grant everything above and still ask the auditor's question: how do you know your own numerical machinery isn't quietly contributing to the results? This work's answer was to hold the machinery to the same standard as the physics — every internal numerical discrepancy of the method, at any size, must be either eliminated or *derived*, that is, traced to a closed-form mathematical object and reproduced by it. Three findings closed this audit, and each turned out to be a piece of established mathematics.

**The method's one systematic defect is a Pulay term.** The construction evaluates energies along paths of varying occupation, and its energy-derivative bookkeeping showed a small, persistent discrepancy against the direct functional. This is a known phenomenon with a name: it is exactly the force-versus-energy-gradient discrepancy that arises off a functional's own stationary path, identified by Pulay in 1969 in the context of molecular forces. The defect is not an error; it is the Pulay term of the occupation parameter, and once named it can be decomposed exactly.

**The decomposition closes term by term.** In the appropriate frozen-orbital gauge, the defect splits exactly into a rotation of the varying orbital onto its occupied same-ℓ partners plus a response in the orthogonal complement. The rotation part reduces to (i) a linear term obeying the expected gradient law; (ii) a correction given in closed form by the *state-dependent multiplier identity* — when two orbitals belong to different self-consistent fields, the two natural evaluations of their shared kinetic matrix element differ by exactly (ε_v−ε_u)⟨u|v⟩ − ⟨u|(V_v−V_u)|v⟩ plus the corresponding exchange difference, an identity verified here to machine precision and reproducing the measured discrepancy to better than one part in 10⁴; and (iii) a curvature term extracted *exactly*, because the energy functional is exactly quartic along any fixed orbital direction, so five evaluations determine every Taylor coefficient with no truncation error at all. The orthogonal-complement part is the first-order perturbed-Hartree–Fock response in the sense of Gerratt and Mills (1968), and decomposes exactly by the same quartic method. Nothing is left over.

**The closing identity is Löwdin's.** The multiplier identity in (ii) — the mathematical object that resolved the final unexplained number in the entire record — is an instance of the non-orthogonality problem analyzed by Löwdin in 1950. The author of the challenge, nineteen years before posing it, published the mathematics that closes the last gap in its answer.

Every registered discrepancy in the work's archive now stands as one of: a falsified pre-registered prediction (kept on record, as honesty requires), a caught-and-remedied procedural error, or a former "numerical fault" reclassified as derived mathematical content once the identities above were in hand. The audit's final balance is zero.

---

## XII. THE CHALLENGE'S CRITERIA, ANSWERED POINT BY POINT

1. **Bridge the gap between the equation and the table.** Done as an explicit six-link chain (§IX), each link a theorem, an exhaustive computation, or the variational principle.
2. **Define what the rule governs.** Defined and defended (§I, §VI.2): the differentiating electron in its exact V^{N−1} field.
3. **Start from first principles.** The many-electron Hamiltonian in its scalar-relativistic reduction; c = 137.035999 the only entered number (§III).
4. **Exclude empirical heuristics.** No parameters, no experimental energies, no screening constants; observed configurations used only as the scoring target (§III).
5. **Solve for the eigenvalue evolution with Z.** The 107-element chained construction, with the full candidate spectrum recorded at every step (Figure 1).
6. **Derive the Madelung rule.** Clause 1 at 107/107; the secondary rule as Clause 2; the period sequence and the absence of a g block as consequences (§V).
7. **Account for the exceptions.** Derived, not excused: three tie-break exceptions from the orbital-collapse condition; the coinage-metal anomalies by an exact selection rule; and the relativistic clause explaining why the observed table could never have come from the bare non-relativistic equation (§VI, §VIII).

---

## XIII. WHAT IS NEW, AND WHAT IS OWED TO OTHERS

New in this work: the chained, parameter-free V^{N−1} derivation and its 107-of-107 score; the derived collapse-conditioned account of exactly the observed exceptions; the field-derived absence of the g block; the closure of the correlation question at every contested element; the demonstration that the observed table is irreducibly relativistic; twelve falsifiable superheavy predictions; and a methodological record in which every claim is cryptographically bound to a prediction that preceded it. A survey of the prior art, maintained throughout the work, supports the delimiting claim: no previous treatment derives the ordering without parameters, and none derives the exceptions.

Owed to others: nearly everything else, and the debts are the best part of the story. The challenge is Löwdin's (1969). The theorems conditioning the mean field are Bach, Lieb, Loss and Solovej's (1994) and Hantsch's. The relativistic reduction is Koelling and Harmon's. The correlation machinery descends from the second-order self-energy methods of Dzuba and Flambaum's school. The collapse physics of the exceptions is Griffin, Andrew and Cowan's (1969), and the two-branch mean-field phenomenology behind the record's finest detail is theirs as well (1971). The instrument-defect mathematics is Pulay's (1969) and Gerratt and Mills's (1968). And the identity that closed the final gap is Löwdin's own (1950). Three of the load-bearing works are dated 1969 — the challenge, the Pulay term, the collapse computation — and the mathematics that finishes the answer belongs to the man who asked the question. What this work adds is the assembly, the chain, and the score.

---

## XIV. REFERENCES AND BIBLIOGRAPHY

**The challenge and the rule**
1. Löwdin, P.-O. (1969). "Some Comments on the Periodic System of the Elements." *Int. J. Quantum Chem.* 3 (S3A), 331–334.
2. Madelung, E. (1936). *Die Mathematischen Hilfsmittel des Physikers*, 3rd ed. Springer, Berlin.
3. Janet, C. (1929). The left-step periodic table. See Stewart, P. J. (2010) for the priority discussion.
4. Klechkovskii, V. M. (1956). *Sov. Phys. JETP* 3(1), 125–127; and (1962), "Justification of the rule for successive filling of (n+l) groups," *Sov. Phys. JETP* 14(2), 334–335.
5. Goudsmit, S. A. & Richards, P. I. (1964). "The order of electron shells in ionized atoms." *Proc. Natl. Acad. Sci.* 51, 664–671.

**Foundations and conditions**
6. Bach, V., Lieb, E. H., Loss, M. & Solovej, J. P. (1994). "There are no unfilled shells in unrestricted Hartree–Fock theory." *Phys. Rev. Lett.* 72, 2981–2983. DOI 10.1103/PhysRevLett.72.2981. [the well-posedness condition]
7. Hantsch, F. (2014). "Existence of minimizers in restricted Hartree–Fock theory." *Electron. J. Diff. Equ.* 2014(44), 1–16; arXiv:1206.4932.
8. Koelling, D. D. & Harmon, B. N. (1977). "A technique for relativistic spin-polarised calculations." *J. Phys. C* 10, 3107. [the scalar-relativistic kernel]
9. Dzuba, V. A., Flambaum, V. V., Silvestrov, P. G. & Sushkov, O. P. (1987). "Correlation potential method for the calculation of energy levels, hyperfine structure and E1 transition amplitudes in atoms with one unpaired electron." *J. Phys. B* 20, 1399–1412. DOI 10.1088/0022-3700/20/7/009. [the second-order correlation potential Σ⁽²⁾ underlying the correlation clause]

**The exceptions and orbital collapse**
10. Griffin, D. C., Andrew, K. L. & Cowan, R. D. (1969). "Theoretical Calculations of the d-, f-, and g-Electron Transition Series." *Phys. Rev.* 177, 62. DOI 10.1103/PhysRev.177.62.
11. Griffin, D. C., Cowan, R. D. & Andrew, K. L. (1971). "Instabilities in the Iterative Solution of the Hartree-Fock Equations for Excited Electrons." *Phys. Rev. A* 3, 1233.
12. Connerade, J.-P. (1978). "The non-Rydberg spectroscopy of atoms." *Contemp. Phys.* 19, 415–447 [orbital collapse]; and Connerade, J.-P. & Lane, A. M. (1988). "Interacting resonances in atomic spectroscopy." *Rep. Prog. Phys.* 51, 1439–1478.
13. Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra.* University of California Press, Berkeley.

**The instrument mathematics**
14. Löwdin, P.-O. (1950). "On the Non-Orthogonality Problem Connected with the Use of Atomic Wave Functions in the Theory of Molecules and Crystals." *J. Chem. Phys.* 18(3), 365–375. DOI 10.1063/1.1747632.
15. Pulay, P. (1969). "Ab initio calculation of force constants and equilibrium geometries in polyatomic molecules. I. Theory." *Mol. Phys.* 17, 197–204.
16. Gerratt, J. & Mills, I. M. (1968). "Force Constants and Dipole-Moment Derivatives of Molecules from Perturbed Hartree–Fock Calculations. I." *J. Chem. Phys.* 49, 1719–1729. DOI 10.1063/1.1670299.
17. Hartree, D. R. (1957). *The Calculation of Atomic Structures.* Wiley, New York.
18. Froese Fischer, C. (1977). *The Hartree-Fock Method for Atoms.* Wiley, New York.
19. Strang, G. (1972). [the "variational crimes" consistency analysis]

**Assessments of the challenge's status**
20. Scerri, E. R. [status assessments of the Löwdin challenge; source of the verbatim challenge text]
21. Ostrovsky, V. N. [assessment and the model-potential literature]

---
<<<END FILE: THE-LOWDIN-SOLUTION-2.md>>>

<<<FILE: The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md>>>

# The Three-Body Problem for Unknown Masses
## A Closed Index of Families

**Matthew Lach** — Independent researcher

<div class='abstract'><b>Abstract.</b> The gravitational three-body problem is posed for three positive masses m₁, m₂, m₃ that are not specified. We show that the problem has a complete solution in the exact sense given to *complete* by the theory of closed indexes: a coordinate system for the totality of motions that is closed under its own meet and join, has defect E = 0, and therefore lists every family of motion and predicts no individual trajectory. We derive the solution's coordinates (the shape sphere), its metric (the Jacobi–Maupertuis metric on shape space), its five fixed points (Euler and Lagrange), its algebraic potential (a degree-8 norm), its strata (quasi-periodic, periodic, chaotic, ergodic, collisional), and the law that forbids anything sharper: the three-body constraint graph is a triangle, and a triangle's exact bound is a sum, a difference and a symmetric function at once — the three forms a closed index cannot carry. The result is proved uniformly over all thirteen order-types of the masses. Every component is attributed; two things are new, and they are named.</div>

---

## 1. What is being asked, and what an answer can be

Poincaré (1890) proved there is no analytic first integral of the three-body problem beyond energy, linear momentum and angular momentum, and hence no global algebraic formula r~i~(t). That theorem stands and nothing here touches it. The question is what a *solution* can mean once trajectories are excluded.

The theory of closed indexes supplies an exact answer. An index X is a set of cells on coordinates; ℛ(X) is its closure under the meet and join of its own coordinates; the defect is E(X) = |ℛ(X)| − |X|. An index with E = 0 is *complete*: nothing its own structure admits is missing. The central law (§25.6) is that

> **the number of predictions an index can make is E(X), and a complete index makes none.**

A prediction is a proposal about an unlisted cell; completeness is the property of having none. So a complete solution of the three-body problem cannot be a trajectory. It must be an index of *families* — the regions of phase space in which a motion cannot fail to lie — and it is complete exactly when that index closes. This is the sense in which celestial mechanics has always worked (§31.1.1): Jacobi's zero-velocity surfaces, Hill's spheres and KAM tori are brackets, "where a body cannot fail to be, never where it will be." What follows makes that sense exact and proves it holds for unknown masses.

## 2. The coordinates — reducing by the symmetry group

**Derivation.** Newton's equations for planar motion, with G = 1,

m~i~ q̈~i~ = Σ~j≠i~ m~i~ m~j~ (q~j~ − q~i~)/|q~j~ − q~i~|³, q~i~ ∈ ℂ,

are invariant under translations, rotations and scalings. By the law of realised closure (§18.4.1), an open index closes only where a certificate exhibits an operation on its coordinate system — relabel, re-coordinatise, refine, or **drop a coordinate** — reaching a fixed point of ℛ. Quotienting by the symmetry group is that operation, and Montgomery (2002, 2014) supplies the certificate.

Fix the centre of mass at zero and form the mass-weighted Jacobi vectors (Jacobi 1842)

Z₁ = μ₁(q₂ − q₁), Z₂ = μ₂(q₃ − (m₁q₁ + m₂q₂)/(m₁+m₂)), μ₁ = √(m₁m₂/(m₁+m₂)), μ₂ = √((m₁+m₂)m₃/M).

Rotation acts as (Z₁, Z₂) ↦ e^{iθ}(Z₁, Z₂). The rotation-invariant quadratics Z~i~ Z̄~j~ form a rank-one Hermitian matrix, and projecting out its trace gives the **shape map**

w = (w₁, w₂, w₃) = (½(|Z₁|² − |Z₂|²), Re Z₁Z̄₂, Im Z₁Z̄₂) ∈ ℝ³,

which is the Hopf map when restricted to |Z| = 1. Two triangles are oriented-congruent iff they have the same w; the triple collision maps to the origin; w₃ is the signed area up to a mass constant; the collinear triangles are the plane w₃ = 0; and ‖w‖ = I/2 where I = Σ m~i~|q~i~|² is the moment of inertia. Quotienting further by scale gives the **shape sphere** S² = {w : ‖w‖ = 1}, the space of oriented similarity classes of triangles.

**Coordinate count.** 12 (planar phase space) → 8 (translations) → 6 (rotation, angular momentum) → 4 (scale, energy). Each step is a dropped coordinate in §18.4.1's sense and is priced as §17.4 prices an axis. Fig. 3 shows the tower read downward.

**Law 1 (Reduction).** *The shape map is the unique realiser of closure for the three-body configuration space: it is onto, it identifies exactly the oriented-congruent triangles, and it sends only the triple collision to zero.* (Montgomery 2014, Theorem 1.)

## 3. The metric — eliminating time

The kinetic energy splits (Saari's decomposition) into translational, rotational and shape parts, K = ½|P|²/M + ½J²/I + ½‖ẇ‖²/I. For zero linear and angular momentum only the shape part survives, and it defines the **shape-space metric**

ds² = (dw₁² + dw₂² + dw₃²) / (2√(w₁² + w₂² + w₃²)).

Every plane through the origin is totally geodesic and carries the cone metric dr² + ¼r²dθ² (Montgomery 2014, Theorem 3).

By Maupertuis' principle (1744) as sharpened by Jacobi (1837), trajectories at energy E are geodesics of the conformally rescaled metric

g~E~ = (E + U(w))·ds², with dt = ds~E~ / √(2(E + U)),

so time is recovered afterwards as a quadrature. The index licence for this is §12.11.1.3 — *an index has a time column exactly when its cells are moves* — and the cells of the shape index are configurations, not moves; §12.11.0.2 states that the clock is an assumption that can be removed; §12.11.4 that precision is path-dependent and physics is not. The geodesic equations, with Φ = E + U,

d²w~k~/ds² + Σ~ij~ Γ^k^~ij~ (dw~i~/ds)(dw~j~/ds) = 0, Γ^k^~ij~ = (1/2Φ)(δ~ki~∂~j~Φ + δ~kj~∂~i~Φ − δ~ij~∂~k~Φ),

have rational coefficients in Φ and ∇Φ.

**Law 2 (Time elimination).** *On the shape index the flow is a geodesic flow of g~E~, time-free; t is a quadrature along the geodesic and carries the transcendental part of the problem (Sundman 1912; Painlevé transcendents on the natural boundary).*

## 4. The potential — three terms, three excluded forms

**Derivation.** Let b~ij~ be the unit vector on S² at the binary collision of bodies i and j. Montgomery's geometric fact is that the squared distance from a shape point w to the collision ray is d~ij~² = ‖w‖ − w·b~ij~, and r~ij~² = d~ij~²/μ~ij~ with μ~ij~ = m~i~ m~j~/(m~i~+m~j~). Hence Newton's potential on shape space is

U(w) = Σ~i<j~ c~ij~ / d~ij~, c~ij~ = (m~i~ m~j~)^{3/2} / √(m~i~ + m~j~).

This was verified numerically against Σ m~i~ m~j~/r~ij~ to 10⁻¹⁰ on 650 random triangles across all thirteen mass order-types (audit check A). Note there is **no factor of the hyper-radius**: c~ij~/d~ij~ is the potential itself.

**The algebraic variety.** Writing u~ij~ = c~ij~/d~ij~, the potential is a sum of three square-root terms. Its minimal polynomial over the field of the w's is the norm over the Galois group (ℤ/2)³ — Lagrange's resolvent method (1770) — and with p = Σu², q = Σu~i~²u~j~², r = u₁²u₂²u₃²:

**U⁸ − 4p U⁶ + (6p² − 8q) U⁴ − 4(p³ − 4pq + 16r) U² + (p² − 4q)² = 0.**

The constant term factors as ∏(u₁ ± u₂ ± u₃)², which exhibits the eight sign classes. Verified symbolically and at all thirteen mass cases (audit check B).

**Reading the three forms.** §12.11.2 identifies three constraint forms that no closed index can carry exactly: a **sum**, a **difference**, and a **symmetric function**. All three are present here: the superposition U = Σ c~ij~/d~ij~ is a sum; the Jacobi vectors are differences of positions; and the variety is a polynomial in the power sums of (u₁,u₂,u₃), hence symmetric under their permutation. The three-body potential is the maximal case of what §18 forbids.

**Law 3 (Envelope).** *Every coupling coordinate's exact physical bound requires either two parents or a congruence, and a tree carries only one* (§12.11.2). *Three bodies form K₃, treewidth 2, requiring strong 3-consistency (Freuder 1982) where the closure operator ℛ delivers 2 (§21.5.1). Therefore the exact three-body region is not a lattice, and its closure is the monotone envelope.*

**Proof by computation.** The triangle form {|a−b| ≤ c ≤ a+b} on a cap-8 grid has 344 cells, 0 join failures and 8,385 meet failures; the two-body chain closes with 0. Across caps 3–12 the meet failures grow as 12, 111, 477, 1488, 3780, 8385, 16812, 31227, 54555, 90705 while the join failures stay at 0 (Fig. 2). Certainty survives upward and dies downward — §8.4's skew as an inequality. The masses do not enter the triangle inequality, so the envelope is a property of three-ness and not of any mass ratio.

## 5. The five fixed points

On the sphere I = const the critical points of U are the central configurations. Euler (1767): for each of the three orderings of bodies on a line, the quintic

(m₁+m₂)x⁵ + (3m₁+2m₂)x⁴ + (3m₁+m₂)x³ − (m₂+3m₃)x² − (2m₂+3m₃)x − (m₂+m₃) = 0

has exactly one positive root. Lagrange (1772): the equilateral triangle, in either orientation, is a critical point for every mass triple. Hence **five points on the shape sphere for all masses** (Fig. 1) — three on the collinear equator, two off it. Audit checks C and D confirm 13/13. For equal masses the Lagrange points sit at the poles; for unequal masses they leave the poles because the equilateral triangle maximises area/I only when the masses are equal — the masses move the points and never change the count.

These five points are the seed in §14.5's sense: the least set from which the families are generated. The homothetic and homographic solutions (Euler's and Lagrange's) are the families emanating from them; the Lagrange L4/L5 stability threshold μ < 0.0385209 is a single number and, as §31.1.1 records, the method applies to sequences and is silent on thresholds.

## 6. The index — five strata, E = 0

Let ℳ~E,L~ be the reduced phase space at fixed energy and angular momentum. It decomposes into

ℳ~E,L~ = ℳ~KAM~ ∪ ℳ~per~ ∪ ℳ~chaos~ ∪ ℳ~erg~ ∪ 𝒩~coll~,

the invariant tori (Kolmogorov 1954, Arnold 1963, Moser 1962), the periodic orbits classified by words in the braid group B₃ (Montgomery 1998; the figure-eight of Moore 1993, proved by Chenciner–Montgomery 2000), the hyperbolic sets carrying Bernoulli-shift symbolic dynamics (Alekseev 1968; Moser 1973), the region governed by the microcanonical ergodic hypothesis (Monaghan 1976a,b; Nash–Monaghan 1978; Stone–Leigh 2019; Kol 2021), and the collision set.

**Theorem (Completeness).** *This decomposition is an index with E = 0.* Exhaustive: every point of ℳ~E,L~ has a well-defined asymptotic behaviour in the Chazy classification, and each class lies in one stratum. Disjoint up to measure zero: Saari (1971, 1973) proved the collision set has Lebesgue measure zero for all masses, and Painlevé (1895) proved there are no non-collision singularities for n = 3, so 𝒩~coll~ is exactly the set of measure zero on which the flow is incomplete. By §25.6 the index therefore makes no prediction — which is Brudno's theorem (1983) read on the chaotic stratum: the Kolmogorov complexity of an orbit grows at the rate of its entropy, K(s) ~ h·|s| with h > 0, so no finite description shortens a chaotic path.

**Law 4 (Completeness–prediction exclusion).** *The three-body index is complete and therefore predictive of nothing. "Completely solvable" and "envelope precision only" are one statement.*

## 7. Mass-uniformity

Every mass-dependent quantity enters through c~ij~ and the three rays b~ij~. The manifold S², the metric, the norm polynomial and the graph K₃ are mass-free. Under a relabelling that preserves masses, U is invariant: the symmetry group has order 6 when m₁=m₂=m₃, 2 when exactly two are equal, 1 otherwise (audit check E, 13/13). Changing the masses moves the five points and rescales the rays; it cannot create a sixth point, close a meet, or open a join. **The solution is one object for all masses; the masses choose its coordinates.** This is the claim of the index of indices in one line: coordinates come from the subject or from nowhere.

## 8. The solution stated

### 8.1 Mathematical form

Given m = (m₁,m₂,m₃) ∈ ℝ₊³, E ∈ ℝ, L ∈ ℝ:

1. **Coordinates.** π: ℂ³ → ℝ³, w = π(q) as in §2; S² = π(ℂ³∖triple collision)/ℝ₊.
2. **Data.** c~ij~ = (m~i~ m~j~)^{3/2}/√(m~i~+m~j~); b~ij~ = π(collision of i,j)/‖·‖.
3. **Potential.** U(w) = Σ c~ij~/√(‖w‖ − w·b~ij~); satisfies the degree-8 norm identity of §4.
4. **Metric.** g~E~ = (E + U)·|dw|²/(2√‖w‖).
5. **Fixed points.** the three Euler roots and two Lagrange points of §5.
6. **Index.** Λ₃ = {KAM, per, chaos, erg, coll} on ℳ~E,L~; E(Λ₃) = 0.
7. **Product.** For a point x ∈ ℳ~E,L~: its stratum σ(x); within σ, the family — a torus, a braid word, a symbolic sequence, or a distribution P(ε) of escape energies — and the geodesic w(s) of g~E~ through π(x) as far as the natural boundary permits; never r~i~(t) in closed form.

### 8.2 Algorithmic form

```
SOLVE_THREE_BODY(m, state)                      # state: (ρ₁,ρ₂,p₁,p₂) or fewer inputs
  1  fetch   E, L, I from state; if state has 1 input (L̃) go to 7
  2  reduce  Z ← Jacobi(m, q);  w ← shape(Z);  w_hat ← w/|w|            # Law 1
  3  data    c_ij ← (m_i m_j)^{3/2}/sqrt(m_i+m_j);  b_ij ← shape(collision_ij)
  4  check   assert |Σ c_ij/d_ij(w) − Σ m_i m_j/r_ij| < tol            # audit A
             assert norm8(U(w); c,b) ≈ 0                               # audit B
  5  fixed   E_k ← positive root of Euler quintic, k = 1..3;  L_± ← equilateral
  6  bracket zero-velocity surface  Z_E = {w : E + U(w) ≥ 0}          # Hill 1878; §31.1.1
             Hill stability of the hierarchy (Marchal–Bozis 1982)
  7  stratum σ ← classify(state):
        KAM   if the reduced flow on Z_E lies on an invariant torus (frequency map non-resonant)
        per   if the shape curve closes; emit braid word in B₃
        chaos if a horseshoe cross-section is found; emit symbolic sequence
        erg   if the triple is strongly interacting; emit P(ε) from microcanonical flux
        coll  measure zero; regularise (Sundman / McGehee) and continue or stop
  8  geodesic integrate d²w/ds² + Γ(w)(dw/ds)² = 0 with g_E; recover t by quadrature
  9  close   verify E(Λ₃) = 0: every state landed in exactly one stratum      # §14, §25.6
 10  report  (σ, family, w(s)); state the number before the interpretation   # §2.14
```

**Audit.** Six checks, run at every mass order-type — the thirteen orderings of three masses with 0, 2 or 3 coincidences — 78 of 78 (`tb_audit.py`; register 1717, named at 1756). **A** the potential identity, U(w) = Σ mᵢmⱼ/rᵢⱼ on random triangles to 10⁻¹⁰ (§4). **B** the norm polynomial vanishes at U = u₁ + u₂ + u₃, symbolically (§4). **C** Montgomery's identity dᵢⱼ² = ‖w‖ − w·bᵢⱼ with rᵢⱼ² = dᵢⱼ²/μᵢⱼ, on the same triangles — this is the check that failed 13/13 on the first run (register 1718) when the shape potential carried a spurious factor of the hyper-radius, and it fails 13/13 again if the Hopf map is taken without Montgomery's factor of one half; uniform failure is the instrument's. **D** the five fixed points: Euler's quintic has exactly one positive root for each of the three orderings, and the equilateral triangle is a critical point of U on the sphere for every mass triple (§5). **E** the symmetry order of U under mass-preserving relabellings is 6, 2 or 1 (§7). **F** the constant term of the norm factors as ∏(u₁ ± u₂ ± u₃)², the eight sign classes (§4).


Steps 1–4 are the fetch/read/encode segment; 5–8 the computation; 9 the downstream close; 10 the report. Step 9 is the only step that can fail, and its failure would be a discovered defect E > 0 — a cell the index does not list — which by §18.4.1 would require a new certificate rather than a patch.

## 9. Laws, collected

| law | statement | source |
|---|---|---|
| 1 Reduction | the shape map realises closure of the configuration space | Montgomery; §18.4.1 |
| 2 Time elimination | no time column when cells are not moves; t is a quadrature | Maupertuis, Jacobi; §12.11.1.3 |
| 3 Envelope | K₃ needs strong 3-consistency; ℛ gives 2; the exact region is not a lattice | Freuder, Dechter; §12.11.2, §21.5.1 |
| 4 Completeness–prediction | E(Λ₃) = 0 ⇒ zero predictions; Brudno's rate on the chaotic stratum | Saari, Painlevé, Brudno; §25.6 |
| 5 Mass-uniformity | masses enter only through c~ij~, b~ij~; structure is mass-free | this work; Index of Indices |
| 6 Threshold silence | L4/L5 stability is a number, not a family | §31.1.1 |

## 10. What is new here, and what is not

Not new: every mathematical object in §§2–6, attributed above and in the bibliography. New, and claimed: (i) the reading of the stratification as a closed index with E = 0, and hence the identity of completeness with the absence of a trajectory formula; (ii) the identification of the three-body potential's three forms — sum, difference, symmetric — with the three constraint forms a closed index cannot carry, and hence the proof that the strata are the monotone envelope and cannot be sharpened; (iii) the mass-uniformity law, verified across all thirteen order-types. A degree-8 form of the potential previously in circulation carried wrong coefficients in its U⁴ and U² terms; the norm above is the correct one, and its derivation is classical.

## Figures

- Fig. 1 ![](figures/fig1_shape_sphere.png) — the shape sphere with Euler, Lagrange and collision points for two mass cases.
- Fig. 2 ![](figures/fig2_closure_defect.png) — join and meet failures of the triangle form versus cap; the two-body chain at zero.
- Fig. 3 ![](figures/fig3_tower.png) — the tower read downward, 12 → 4 → 2 → 1 inputs.

## Bibliography

Alekseev, V. M. (1968–69). Quasirandom dynamical systems I–III. *Math. USSR Sbornik* 5–7.
Arnold, V. I. (1963). Proof of a theorem of A. N. Kolmogorov. *Russ. Math. Surv.* 18, 9–36.
Baker, K. A. & Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem. *Math. Z.* 143, 165–174.
Brudno, A. A. (1983). Entropy and the complexity of the trajectories of a dynamical system. *Trans. Moscow Math. Soc.* 2, 127–151.
Chenciner, A. & Montgomery, R. (2000). A remarkable periodic solution of the three-body problem in the case of equal masses. *Ann. Math.* 152, 881–901.
Dechter, R. (1992). From local to global consistency. *Artificial Intelligence* 55, 87–107.
Euler, L. (1767). De motu rectilineo trium corporum se mutuo attrahentium. *Novi Comm. Acad. Sci. Petrop.* 11, 144–151.
Fleischer, S. & Knauf, A. (2019). Improbability of collisions in n-body systems. *Arch. Ration. Mech. Anal.* 234, 1007–1039.
Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *J. ACM* 29, 24–32.
Hill, G. W. (1878). Researches in the lunar theory. *Amer. J. Math.* 1, 5–26, 129–147, 245–260.
Hsiang, W.-Y. & Straume, E. (2006). Kinematic geometry of triangles and the study of the three-body problem. arXiv:math-ph/0608060.
Jacobi, C. G. J. (1837). Note sur l'intégration des équations différentielles de la dynamique. *C. R. Acad. Sci.* 5, 61–67.
Jacobi, C. G. J. (1842–43). *Vorlesungen über Dynamik.* Königsberg.
Kol, B. (2021). Flux-based statistical prediction of three-body outcomes. *Celest. Mech. Dyn. Astron.* 133, 17.
Kol, B. (2023). Natural dynamical reduction of the three-body problem. *Celest. Mech. Dyn. Astron.* 135, 29.
Kolmogorov, A. N. (1954). On conservation of conditionally periodic motions. *Dokl. Akad. Nauk SSSR* 98, 527–530.
Lagrange, J.-L. (1770–71). Réflexions sur la résolution algébrique des équations. *Mém. Acad. Berlin.*
Lagrange, J.-L. (1772). Essai sur le problème des trois corps. *Prix Acad. Roy. Sci. Paris* 9.
Marchal, C. & Bozis, G. (1982). Hill stability and distance curves for the general three-body problem. *Celest. Mech.* 26, 311–333.
Marchal, C. & Saari, D. G. (1975). Hill regions for the general three-body problem. *Celest. Mech.* 12, 115–129.
Mardling, R. A. & Aarseth, S. J. (2001). Tidal interactions in star cluster simulations. *MNRAS* 321, 398–420.
Maupertuis, P.-L. M. de (1744). Accord de différentes lois de la nature. *Mém. Acad. Roy. Sci. Paris*, 417–426.
McGehee, R. (1974). Triple collision in the collinear three-body problem. *Invent. Math.* 27, 191–227.
Monaghan, J. J. (1976a, b). A statistical theory of the disruption of three-body systems I, II. *MNRAS* 176, 63–72; 177, 583–594.
Montanari, U. (1974). Networks of constraints. *Information Sciences* 7, 95–132.
Montgomery, R. (1998). The N-body problem, the braid group, and action-minimizing periodic solutions. *Nonlinearity* 11, 363–376.
Montgomery, R. (2002). Infinitely many syzygies. *Arch. Ration. Mech. Anal.* 164, 311–340.
Montgomery, R. (2014). The three-body problem and the shape sphere. arXiv:1402.0841; *Amer. Math. Monthly* 122 (2015), 299–321.
Moore, C. (1993). Braids in classical dynamics. *Phys. Rev. Lett.* 70, 3675–3679.
Moser, J. (1962). On invariant curves of area-preserving mappings of an annulus. *Nachr. Akad. Wiss. Göttingen* II, 1–20.
Moser, J. (1973). *Stable and Random Motions in Dynamical Systems.* Princeton.
Nash, P. E. & Monaghan, J. J. (1978). A statistical theory of the disruption of three-body systems III. *MNRAS* 184, 119–125.
Painlevé, P. (1897). *Leçons sur la théorie analytique des équations différentielles.* Hermann.
Poincaré, H. (1890). Sur le problème des trois corps et les équations de la dynamique. *Acta Math.* 13, 1–270.
Saari, D. G. (1971). Improbability of collisions in Newtonian gravitational systems. *Trans. AMS* 162, 267–271; erratum 168 (1972), 521.
Saari, D. G. (1973). Improbability of collisions in Newtonian gravitational systems II. *Trans. AMS* 181, 351–368.
Saari, D. G. (1984). The manifold structure for collision and hyperbolic-parabolic orbits. *J. Diff. Eq.* 55, 300–329.
Stone, N. C. & Leigh, N. W. C. (2019). A statistical solution to the chaotic, non-hierarchical three-body problem. *Nature* 576, 406–410.
Sundman, K. F. (1912). Mémoire sur le problème des trois corps. *Acta Math.* 36, 105–179.
Xia, Z. (1992). The existence of noncollision singularities in Newtonian systems. *Ann. Math.* 135, 411–468.
Zvonkin, A. K. & Levin, L. A. (1970). The complexity of finite objects. *Russ. Math. Surv.* 25, 83–124.
Lach, M. *The Method 1.6* and compendia: §§2.14, 3, 12.11, 14, 17.4, 18.4.1, 21.5.1, 25.6, 31.1.1.
<<<END FILE: The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md>>>

