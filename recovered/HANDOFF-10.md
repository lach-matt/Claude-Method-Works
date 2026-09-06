# THE METHOD 1.6 — HANDOFF (chat 8 → chat 9), 2026-08-24

## THE BRIDGE — read this before anything else
1. **Current state of every volume** = the two BUILD-9 bundles in project knowledge (`The_Method_1_6_BUILD9_main_and_register.md`, `The_Method_1_6_BUILD9_compendia_papers_audits.md`). Split on `<<<FILE: name>>>` … `<<<END FILE: name>>>` into `/home/claude/build/` (`split.py`). **Figures:** `The_Method_1_6_figures_BUILD9.zip` (output of chat 8; upload to Drive and put the id here). It holds `figures/` (49; 16.1, 24.1, 12.3, 25.2 are chat 8's re-renders), `figures-compendia/` (12), `figures-pre-crop/` (15, chat 7's originals), `figures-pre-rerender/` (4, chat 7's renders of the four). If only BUILD8's zip is available (Drive id `1l-176jSS0yKyeV3sqWh4iGxyGr4p-grG`; nested JSON, base64 in `json.loads(d[0]['text'])['content']`), re-run `fig_rerender.py` (bundle 2) to regenerate the four.
2. **Every finding, prior state and ruling**: `MAIN_AUDIT.md` V1–V48 (bundle 2). Reasoning: project-scoped `conversation_search`, chats "Rebuild 1"–"Rebuild 5", chat 6, chat 7, chat 8. Read at the hit; do not page.
3. **Standing directives, rulings 1–4**: HANDOFF-2 (`The_Method_1_6_BUILD_handoff_and_audits.md`); 5–14 HANDOFF-4; 15–17 HANDOFF-5; 18–20 HANDOFF-7; 21–22 register 1751. All kept in bundle 2. Carry verbatim. No new rulings in chat 8.
4. Retire BUILD-8 bundles from project knowledge once BUILD-9 is in.
5. Tools (bundle 2, run from `/home/claude/build/`): `build.py` as HANDOFF-8 §5 — now stamps "Build 9" and drops the image alt line at press (1754); `ref.docx` recipe unchanged (HANDOFF-8 §5). Font: docx in Georgia, container PDFs in Caladea — accepted, do not flag. Also `register_cites.py`, `dclose.py`, `index_gen.py`, `split.py`, `trueres.py`, `crop_titles.py`, `qgraph.py`, **`fig_rerender.py`** (chat 8: redraws 16.1, 12.3, 25.2, 24.1 from `fig241_data.json` and the constants in the script).
Rule: anything a chat produces goes into the next bundle; nothing lives only in outputs.

## State
Phase 4 in progress. Register 1,548 entries (165–1755); 15 prose + 2 numeric counts in main track it. Chat 8 registers 1753–1755. Main and Register re-pressed (270 pp, 423 pp) with Build 9 and the new renders, sampled and holding; the six other volumes' presses are chat 7's and are unchanged by chat 8 (no source edit). No render carries a stale title.

## Open — carry, in order
- **24.1's two flags (1753), author's:** (a) caption says "monotone in all of them"; the Spectra Compendium's table has Al I (d→f), Al II (f→g), He I (d→i) rising — ruling needed on the caption; (b) §24.4's He II series 7.6×10⁻⁵ → 1.6×10⁻⁶ is in the record as endpoints only, and the compendium's He II rows (−0.0003 → −0.0005) are the uncorrected series — five interior values (or levels + limit) needed, then the compendium rows. The render draws He II as the two endpoints, dashed, labelled.
- §34.4 "The rule": heading, no body (1755) — body or removal, author's.
- §32.4.1 `[N — pair count to be confirmed]`: no count or script in the record (1755).
- Item F (stale generators) unchanged. Carried: V14 paper side; Register kinds table / F.1 995/2,433 not recomputable; §32.1.1's 58/138 not recomputable; Main Index is §-locators.

## Method notes
- Plots: no generator for the archived set; chat 8's four have one (`fig_rerender.py`). 16.1's Z = 2 values were digitised from the archived render (the compendium tabulates only δ̄ and σ per channel).
- Register entries are the record — never edit their bodies; build.py enforces form. Counts: the Register's two "N entries, 165 to M" lines, main's 15 "one thousand five hundred and …" sentences and its two numerics move together.
- Zeno: fetch → read → analyse → close flags → report; close each segment; handoff at 90%.