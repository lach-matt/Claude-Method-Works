# Addendum for writers of the stability-theory chapters (files 20–48 and 60)

Read `WRITER-BRIEF.md` first; everything there applies. This addendum adds what is particular to the stability
theory, whose sources are the files of `docket68/n1star/proof5/` (outline-S's section 1.8 maps the part names I.A,
II.F1, III.I(15), IV(4), VI.C, … to file names and kept line ranges).

1. **Your entry.** Your chapter's entry is in `maps/outline-S.md` section 3 (S1–S30). Section 2 lists what is dropped
   in every part (status paragraphs, closing "findings/sources" sections, amendment records, in-body tags); Appendix A
   lists the in-body lines to edit. Read the whole kept range your entry names.
2. **Keys.** Define every result you carry under its canonical key (OUTLINE.md, "Canonical keys"): III.K Theorem 4.3
   is `**Theorem {#thm:iii-k-4-3}**`. Cite results of other parts by their canonical keys, even if their chapter is not
   written yet. A section you cite is `[[sec:<part>-<n>]]`.
3. **The companion papers.** Each part writes out a result of [Hin26c], [Hin26], [Hin26a], [Hin23a] or [CD03] in
   dimension 4 + 1. In the edition each result has its own statement and proof, and may say once "This is
   [Hin26c, Theorem 9.5] in dimension 4 + 1, with …". The dimensional changes are mathematics and stay. Results of the
   literature used as black boxes (outline-S's "BB") are stated exactly with page, or listed in your report for the
   standard-results appendix.
4. **The inner radius.** `docket68/n1star/BEYOND5-R0-PROOF.md` re-proves every part with a lowered inner radius
   r_flat ∈ (0, R₁/2]. Read its section for your parts and state each result with the inner radius as a parameter
   where that file shows it holds so; then no separate re-proof is needed later.
5. **Base points.** Chapters S20–S24 are written at a general base point b near b₀ from the start, folding in the
   sections of III.I(15) their entries name.
6. **Inputs from the main proof's section 10.** Where your entry lists "MAIN: N1STAR 10.x" items, read those
   sections of `docket68/n1star/N1STAR-PROOF.md` (they are headed "### 10.x"). If yours is the lowest-numbered
   chapter whose entry lists an item, carry it: state it as a lemma or proposition under the key `np-10-x[-item]`
   and prove it in writing (the source's proof is usually a program; write the derivation, checking it privately).
   Otherwise cite it by that key.
7. **Arguments about the text.** Where the source justifies a step by counting or listing lines of its own text
   (a census, a ledger keyed by file:line, an admissibility enumeration), replace it by the mathematics it stood
   for: state the hypothesis each use needs at the place it is used, or give the table of results with what supplies
   each one. Never cite a line number.
8. **Bibliography.** `maps/bibliography-notes.md` records keys that the sources use in two senses ([Hin26b], one site
   of [Hin23b], the supplement's text for [HV16]); use the work the cited content belongs to, and say which in your
   report.
9. **Size.** Your entry gives an estimate. Write the complete mathematics even if it runs longer; never abbreviate a
   proof to "as in the source".
