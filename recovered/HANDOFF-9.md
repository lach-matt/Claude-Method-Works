# THE METHOD 1.6 — HANDOFF (chat 7 → chat 8), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-8 bundles in project knowledge (`The_Method_1_6_BUILD8_main_and_register.md`, `The_Method_1_6_BUILD8_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures:** `The_Method_1_6_figures_complete.zip` in Google Drive (id `1jcoJrEKFh4FfWAdKfXWgbMasDpr4OYvp`; nested JSON, base64 in `json.loads(d[0]['text'])['content']`) is now **superseded for fourteen files**: chat 7 cropped the stale title line from figure-6.1, 6.2, 7.1, 8.2, 10.1, 15.1, 19.1, 23.1, 23.2, 24.1, 24.2, 24.3, 25.1, 26.1 (register 1747). The cropped set is `The_Method_1_6_figures_BUILD8.zip` (outputs of chat 7; upload it to Drive and replace the id here). If only the old zip is available, re-crop with `crop_titles.py` (bundle 2). Originals kept as `figures-pre-crop/` in the zip.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V47 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5", chat 6, chat 7. Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2 (`The_Method_1_6_BUILD_handoff_and_audits.md`); 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7. All kept in bundle 2. Carry verbatim. **No new rulings in chat 7**; one is requested (below).
4. Retire BUILD-7 bundles from project knowledge once BUILD-8 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `build.py` as HANDOFF-8 §5; `ref.docx` recipe unchanged (note: the container has no Georgia; soffice substitutes Caladea, so PDF page counts are ~13% below chat 6's — the docx is unaffected). Also `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`, `trueres.py`, `crop_titles.py`, `qgraph.py` (walks the Math Compendium's dependency lines; reproduces 1749's 15 = 6 + 9).
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## Ruling requested
- **Λ_phys rule and supersession (1749).** The printed rule counts provenance-transitive dependence, so `Q.final` and its eight Löwdin objects count as resting on the withdrawn exchange coefficient (15) though `Q.final`'s statement carries no s. Readings: 15 (as printed) or 6 (built on the superseded form). The Physics Compendium prints the split beneath the count; the count itself is unchanged pending the ruling.

## State
Phase 4 in progress. Register 1,542 entries (165–1749); 15 prose + 2 numeric counts in main track it. Chat 7 registers 1746–1749. **All eight volumes pressed** (main 229 pp, Register 348, Math 83, Physics 22, IOI 39, Spectra 20, Löwdin 13, Three-Body 8), sampled and holding. Segment 3 (plots) ✔: all 32 read; 14 titles cropped; item D ✔ (Löwdin refs 6/7/9/12 filled, both papers pressed); Q.delta ✔ (1749).

## Open — carry, in order
- **Four plots owed a re-render from the book's data** (no source survives; 1747): 16.1 (4/4 → 56/56, stale title), 24.1 (He II series, monotone claim; title already cropped), 12.3 ("§7.8.1" in subtitle), 25.2 (bar labels §14.4/§17.6). 16.1 is the only stale title still in a render.
- **Caption 25.1** says 1,105 cells; plot and §25.5 say 1,061. Author's call (not edited, 1746).
- **Chapter 28 orphan "Figure 15.3"**: 1746 located its origin — 24.3's baked pre-V16 title. Resolve as a text edit to "Figure 24.3" once confirmed.
- Three-Body paper: byline "Matthew LachIndependent researcher" lacks a break; inline equations are plain text with literal underscores (1748). build.py stamps "Build 6" — advance the string.
- Main figure captions print twice (alt line + caption): decide whether build.py drops the alt line.
- Q family: whether `Q.bridge`/`Q.region` should be re-stated against `Q.final` (cannot re-point; would cycle).
- Item F (stale generators) unchanged. Carried: §34.4 heading without body; §32.4.1 `[N — pair count]`; "Chapter 27 said…"; §32.1 loose examples; V14 paper side; Register kinds table / F.1 995/2,433 not recomputable; Main Index is §-locators.

## Method notes
- Plots: restore-point-2_13 holds fig00–fig27 as PNGs only; every archived plot matches one byte for byte (map in 1747). Do not look for a generator again.
- Register entries are the record — never edit their bodies; build.py enforces form. Counts: the Register's two "N entries, 165 to M" lines, main's 15 "one thousand five hundred and …" sentences and its two numerics move together.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.