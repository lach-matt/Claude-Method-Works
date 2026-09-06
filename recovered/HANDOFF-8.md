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