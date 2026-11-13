# Brief for a chapter writer of the reader's edition

You write one or more chapters of the self-contained edition titled "Five-Dimensional Vaidya Black Holes as
High-Frequency Limits of Vacuum Spacetimes". Readers are mathematicians and physicists in general relativity with no
access to this repository. Read first, and follow exactly: `STYLE.md` and `OUTLINE.md` in this directory.

## Your sources

Your chapter's entry in the source map (`maps/outline-M.md` section 4, or `maps/outline-S.md`) names its source files and line
ranges, the composition instructions to follow (outline-M section 2) and the material to drop (section 3). Paths in
the map are relative to `research/warp-drive/` (P = `paper/RESPONSE-HL-5D.md`, NP = `docket68/n1star/N1STAR-PROOF.md`,
GD = `docket68/n1star/GAUGEDECAY5.md`, and so on, as the map's own legend says). Read every source line your entry
names. You may read more of a source to understand a step; you may not take mathematics from a text the map marks as
replaced by a later one.

## What to write

1. The chapter's final mathematics, complete: every definition, statement, proof, hypothesis and constant, composed
   from the latest form with every later amendment folded in. A proof the source gives in full is given in full.
   Copy formulas exactly; do not re-derive or simplify a formula unless the source's own amendment does. Keep each
   claim's scope exactly (a statement "for l ≤ 12, computed" stays that; a numerical result says "numerically").
2. In the edition's voice (STYLE.md section 3): no history, no process words, no record letters for results, no status
   tags. The epistemic content of a tag goes into prose: "Computation [[C:key]] verifies this identity exactly",
   "… with certified bounds (interval arithmetic)", "… numerically, on three grids", "by [Hin26, Proposition 6.9]".
3. Labels as in STYLE.md section 4. Export exactly the keys `OUTLINE.md` assigns to your chapter. Cite other
   chapters' results by their exported keys. Where you need a result of another chapter that has no exported key,
   write `[[pending:short-description]]` and list it in your report; never cite a source file or a record name.
4. Literature: cite `[KEY, Theorem n]` with the bibliography keys of the record's reference list (P section 10). When
   a proof uses a published result as a black box, state the result exactly once (with page), in the chapter or as a
   request for the standard-results appendix in your report.
5. Every computation keeps its citation: `[[C:key]]` (key rule in OUTLINE.md). Say what it decides and by which
   method; never give program names, label sets (X1–X8) or runtimes in the text.

## When the sources do not support a clean text

Do not repair mathematics. If the sources disagree, a step is missing, a cited result cannot be found, or a status is
weaker than the statement the chapter must make, write the chapter as far as the sources support, mark the place with
`[[pending:issue-N]]`, and describe issue N in your report with file:line evidence. The coordinator decides.

## Deliverables

- `chapters/NN-key.md` (file name from OUTLINE.md), lines of at most 121 characters, `python3 lint.py
  chapters/NN-key.md` reporting 0 hits other than `[[pending:…]]` markers.
- `crosswalk/NN-key.tsv`: one row per labelled item of your chapter: `label`, `source` (file:line of the final form
  you used), `source_name` (the record's name, e.g. "NP Theorem E", "GD Lemma R7.2 as corrected by (A76)"), `note`.
- A report at the path your prompt gives: the issues (with evidence), the `[[pending:…]]` list, the computations you
  cited (key → what it decides, method), the literature results you used as black boxes (key, number, page), and any
  notation you had to fix. At most 600 words.

Work in place: write the chapter file early and extend it, so nothing is lost if your context fills. Do not modify
any file outside `chapters/`, `crosswalk/` and your report.
