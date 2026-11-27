# F-P-LB: fix report for proofs/P-LB.md

- **Review:** R-P-LB, on md5 c2b4ef1da757cd54c18364b535c839e2.
- **New md5 of proofs/P-LB.md:** b769e8df079712aba31e21bf8c401639 (508 lines).
- **Files changed:** only P-LB.md. No chapter and no P-K.md was edited, and nothing was committed. The other chapters
  showing as modified in git status were changed by other agents.
- **Line numbers** below are those of the new file.

## Minor

**m1** (the opening says δ gets a lower bound). Applied the reviewer's text: "d_NM and N_NM, and an upper bound for δ,
… in terms of the gauge parameter z = 4e_Υγ_Υ² and of h = γ_C⁻¹". I kept "of" before h, and the paragraph is rewrapped.

**m2** (text 6, "as they tend to 0"). Applied verbatim: "as z tends to 0 or γ_C to infinity". Text 6 is still six lines.

**m3** (text 4 states a general-z bound inside sec:ec-gauge-gap, where z = 4·10⁻⁶, and uses g undefined). Applied
verbatim. The text now says z is that point's gauge parameter, "not 4·10⁻⁶", and that g is the function of eq:ec-lb-g.
Text 4 is now "the six lines".

**m4** (δ̂ and δ̄ are rebound against prop:ec-rounds and def:ec-point). Resolved by renaming, as the coordinator
preferred, not by the reviewer's clarifying sentence.

- **New names:** the abstract bounds are B_g (it bounds ε_g, ε_K and the increments) and B_η (it bounds η_2 and ε_K).
- **Where renamed:** in lem:ec-lb-rounds and eq:ec-lb-rounds, thm:ec-lb-proved and its proof, the bound 6B_η in
  rem:ec-lb-conditions, and the three crosswalk notes.
- **Why these names:**
  - B_g and B_η occur nowhere in chapters 40, 41 or 71.
  - Fraktur 𝔞 and 𝔟 were rejected because 𝔟 is the parameter space in chapter 40.
  - The symbol Δ was rejected because Δτ_0 is a lower bound on the increments.
- **Every use checked:**
  - One δ̂ is kept, after lem:ec-lb-gauge: "the number δ̂ of [[prop:ec-rounds]]". It refers to that proposition's value
    1.46214·10⁻¹⁰, which is correct.
  - No δ̄ remains.
  - ε_K δ̂ became "ε_K B_g", with a space, so that it does not read as a subscript.
  - The two longest displays were re-split: eq:ec-lb-rounds re-padded, and the first Σ display set on two lines.
  - Three paragraphs of lem:ec-lb-rounds were rewrapped so that no line starts with a relation.

**m5** (chapter 33's rem:s14-eps-ind-scope becomes false). Added placement item 12, with old and new texts.

- **The old text** was copied from the current chapter 33 (after 003371f6, at today's tree) and occurs exactly once,
  at lines 3534–3535.
- **The new text** is the reviewer's, three lines: "… beyond 0 < ε_ind(h) ≤ δ_50 and the bound ε_ind(h) < 40h/13 of
  [[lem:ec-lb-ind]], which is the smaller for h ≤ 6.309·10⁻⁹ …", with "the upper bound δ_50 is attained".
- **The next line**, "defined.", is unchanged. Item 12 also notes that the kept sentence of rem:ec-point-outside stays
  true, and that the old text must be checked again at merge.
- **Item 11** now reads "every statement of [[ch:s14]] except [[rem:s14-eps-ind-scope]] (text 12)".
- **Crosswalk note added** for the chapter 33 row rem:s14-eps-ind-scope.

## Nits

- **n1** (majorants in e). Applied verbatim: "each coefficient taken at its largest modulus for 0 ≤ e ≤ 10⁻⁵ and each power
  of ξ at ξ = 40/13". The printed bounds stand.
- **n2** ("open at h_*"). Applied: "and 𝖧 ⊂ (0, h_*); so h = 10⁻⁶ is not in 𝖧". The break is moved before "𝖧" so that
  no line starts with ⊂. Text 3 is still seventeen lines.
- **n3** ("not decided" twice in one sentence). Applied verbatim: "… and (γ_Υ, e_Υ) = (1/100, 1/100) is not shown to lie
  below them."
- **n4** (v also enters). Applied verbatim: "through v = 1/2 and e in P_2 and [[eq:s14-f-two]]".
- **n5** ((C4) missing from the list). Added the reviewer's list item for (C4). The following paragraph now reads "not
  (C2), (C3) or (C5), nor (C4) beyond the existence of ε_ind", so the list and the exclusions agree.
- **n6** (row groups mixed). Applied: "the data classes (rows d1–d2), the parameter set ℬ_* (rows b1–b4) or the smallness
  of row n1". The paragraph is rewrapped.
- **n7** ("is the bound"). Applied: "which implies the bound 1.403 × 10²⁰ of [[thm:loss-d]] (ii)".
- **n8** ("is the case z = 4·10⁻⁶"). Applied verbatim: "stays true and follows from [[thm:ec-lb-proved]] at
  z = 4·10⁻⁶".
- **n9** (empty sentence). Deleted. The paragraph ends at "the number δ̂ of [[prop:ec-rounds]]."
- **n10** (crosswalk coordination with P-K). Added a paragraph to the crosswalk section. Both proposals append notes to
  ch:explicit-constants (chapter 71) and sec:scope-constants (chapter 90). The one merged second appends after the
  other's note, separated by "; ", and no other row is shared. P-K.md was not touched.

## Checks (re-run)

- **Lines:** every line of P-LB.md is at most 121 characters. No backslash. No wrapped line starts with a forbidden
  marker; the only lines starting with "- " are the intended list items.
- **Labels:** all 16 new labels are lowercase and undefined elsewhere. Every [[…]] reference resolves to a chapter label
  or to one defined in the file.
- **Lint:**
  - On the proof part together with the eleven new texts, lint gives only undefined-label hits, and all of those labels
    exist in the chapters.
  - On the whole file, lint gives the expected hits only: file paths in the crosswalk rows, and rem:ec-point-outside
    appearing in both the old and the new text.
- **Stated line counts:** all old and new line counts in the Placement match.
- **Trial merge** in a fresh scratch copy of today's chapters:
  - all ten replacements (texts 2–10 and 12) were found exactly once and applied, and the section was inserted after
    sec:ec-delta;
  - lint --chapters gives 0 hits on 62 files;
  - assemble --check gives 0 problems;
  - no assembled line is over 121 characters after label resolution;
  - assembled-paper lint gives 0 hits;
  - the labels resolve, for example thm:ec-lb-proved → Theorem 49.38.
- **Crosswalk rows:** line numbers updated to the new file (lem:ec-lb-ind 69, …, rem:ec-lb-unbounded 244).
