# F-P-RI: fix round for proofs/P-RI.md

**Output.** research/warp-drive/paper/reader/proofs/P-RI.md. It was aadbb3f1b0fd5ffdc68824940c96c1d2 (465 lines) and
is now **a5756b0fec1a33885fcd3987fae1b51c, 586 lines**. It is not committed. No other file in the repository was
edited: no chapter, no crosswalk file, no other proof file. The plain assemble.py was run only in scratch copies.

**Base.** Chapter 33 at HEAD has md5 d2184d75289047ef76ee866214fda5d0 (after the P-ADM and P-G1 merges; P-G1 added
sec:iv5-calc). Chapter 34 has md5 5dbbf88718c43171095a90cf0a4009c8. The crosswalk files are 33: 5b4e25fe…, 34:
6995e64a…. The working tree equals HEAD (ecd1a428) for all four. I re-copied every old text from these files with a
script. Each occurs exactly once, as whole lines:
- P-RI-1 at chapter 33 lines 2791–2792;
- P-RI-2 at lines 3017–3049;
- P-RI-3, which is new, at chapter 34 lines 595–596.

## Findings

- **m1, n1, n2, n3, n4: applied as given.** I checked the reader's consolidated 64-line P-RI-2 text myself, against
  each finding and against the chapters. A diff with the earlier new text shows only these changes:
  - the R_in clause is attached to θ ∈ {0, π}, with "where only R_out enters ([[def:iv6-0-2]])" for θ ∈ (0, π);
  - "whose (H1)–(H2) part", which is right, because the (H3) part of the proof of lem:iv4-1-6 is lem:iv4-1-5 and needs
    h small;
  - γ_* replaces X (four places); this is lem:iii-f1-2-4 with its X taken as γ_* = C_0 + 2;
  - "([[lem:s14-tf-inputs]] (i))" after ρ²Diff¹_b;
  - G(0, 1). The weight 1 lies in (0, 2) and in [−γ_*, γ_*], and it is root-free for I_0, whose roots are −d and d + 2.

  I found nothing wrong. The text is used byte for byte: its md5 without the final newline is the reader's
  3ff2456e854726636c603698c5441504. I kept the short source line "(H1)–(H2) part does not use the value of γ_C. Its
  transition", as the reader did, so that the verified block stays unchanged; it does not show in the rendering.
  Section 2 is the same text. The notes (3.1, 3.3) are updated to match: (H3), the evaluation at 1, γ_* against the
  manifold X, and the R_in clause listed as a third repair.
- **n5: applied, with an addition.** Section 6 now states the change as an append to the fourth field of the
  prop:iv6-1-1 row, the text starting with "; P-RI: …". The interplay section says that both files append to that row
  and that the two appends compose in either order. Scratch copies B and C confirm this: the row keeps four fields and
  both notes in full, and only the order of the notes differs. The note also gained "and its R_in clause restricted to
  theta in {0, pi}", which the reader offered as optional. A second note is added for P-RI-3: it goes into the empty
  fourth field of the lem:iii-f1-3-1 row of crosswalk/34, or after "; " if a note has been added there first.
- **n6: applied with a change.** The reader's replacement says that the chapter-33 results resting on prop:iv6-1-1
  "enter chapter 34 only at Step 4 of prop:iii-f1-3-3 (ii)". That is not quite true. There is a second route:
  - h_tf of thm:iv6-3-1 is part of h_* := min(10⁻⁶, h_0, h_tf) in eq:iv4-0-1 (chapter 33, line 112);
  - chapter 34 fixes the constraint damping data "in sec:iv4-0" (its lines 75–77).

  The new bullet names both routes. Neither reaches the four pieces the new text uses: lem:iii-f1-2-4, lem:iii-f1-3-1,
  *Types and representations* and the *Weights* paragraph. These cite no chapter-33 result and use none of chapter
  34's fixed data. prop:iv6-1-1 holds for every h ∈ (0, 10⁻⁶] (sec:iv6-0). So there is no cycle. The bullet also
  lists the other citations of thm:iii-e-1-1 in chapter 34:
  - its setting: lines 77, 212, 275, 281 and 1935;
  - its clauses (1)–(3): lines 285, 1148, 1500 and 1937.

  For the coordinator: the same overstrong sentence is still in the earlier report, notes/reports/P-RI.md line 51
  ("uses chapter 33 only in prop:iii-f1-3-3"). I did not edit that file, as I was asked to edit only P-RI.md.
- **n7: applied.** The pins now name the HEAD md5s of both chapters and both crosswalk files, with the line numbers
  above and the crosswalk row at line 127. "43" is now "45". P-G1 is recorded as merged into the base. Every claim
  about P-G24b (md5 a44f9f97…, 45 texts) was re-checked against that file and against both chapter bases:
  - its numbering is that of md5 147ca162…;
  - T41 is used in variant A (its §8);
  - P-RI-1 lies between T21 and T23: 2752–2754 and 2937–2939 at HEAD, 2135–2137 and 2316–2318 in its numbering, where
    P-RI-1 is at 2170–2171;
  - P-RI-2 lies between T29 and T30: 3005–3008 and 3080–3082 at HEAD, 2384–2387 and 2458–2460 in its numbering, where
    P-RI-2 is at 2396–2428. T29's old text ends inside line 3008;
  - its §6.1 is at lines 1475–1499, its table row for [Mel93]/[Hin26a, p. 91] at line 127, its summary item (c) at
    lines 16–17, and its §9 note "; P-G24b: …";
  - T23 keeps "where only R_out enters" true;
  - T39 removes the word "sector" at line 3169.

  Other stale items were also updated: "sector" at line 3169 (it was 2541), lem:s14-tf-inputs (v) at lines 2823–2824,
  and its only citation at line 3043.
- **n8: applied as given** (section 3.2).
- **s ≥ 2 (new item P-RI-3).** In chapter 34, lem:iii-f1-3-1's "and s ∈ ℤ." becomes "and s ∈ ℤ, s ≥ 2.". It is one
  line, 120 characters, with no label. Steps 1 and 2 both take Mellin transforms of elements of H^(s−2)_b. The paper
  defines these (sec:i-c-2-3) only for weighted L² functions, and only for those does eq:i-c-2-1 hold. The notes say
  so (section 3.1).

## Uses of lem:iii-f1-3-1

I searched every chapter source for "lem:iii-f1-3-1" at HEAD. It finds the label (chapter 34, line 595) and one use.
No other proof file cites the lemma.
- **Chapter 34, line 760** (prop:iii-f1-3-3 (iii)). It uses the s fixed at line 716, "Fix α_+, s ∈ ℤ large", so
  s ≥ 2 holds: s is taken large, and nothing bounds it above.
- **After P-RI, chapter 33, the P-RI-2 new text** (paragraph "G(λ, γ) does not depend on γ"). It uses s := 2, fixed
  in its first sentence, so s ≥ 2 holds.
- **After P-RI, chapter 33, the P-RI-1 overview.** It only names the formula; the formula is applied with s = 2 in
  P-RI-2.

## Scratch merges

The copies are in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/fpri/.
Each is a git archive of the reader directory at HEAD. The scripts are in tools/ there. The final runs used the
installed proofs/P-RI.md.

| copy | content | lint --chapters | assemble --check | assemble, then lint --paper |
|---|---|---|---|---|
| base | HEAD | 4665 labels, 0 hits | 0 problems | (not run) |
| A | P-RI alone, both crosswalk notes included | 4665 labels, 0 hits | 0 problems | PAPER.md 0 hits |
| B | P-G24b's 45 texts (T41 variant A) and its prop:iv6-1-1 note, then P-RI | 4681 labels, 0 hits | 0 problems | PAPER.md 0 hits |
| C | P-RI, then P-G24b as in B | 4681 labels, 0 hits | 0 problems | PAPER.md 0 hits |

- **Old texts.** Every old text was found exactly once at its turn, in all orders. P-G24b's old texts are exact
  substrings: T7, T16, T29 and T45 end inside a line, and T15 starts and ends inside one. P-G24b applies cleanly at
  HEAD.
- **Orders.** B and C give byte-identical chapters 33 and 34. Their crosswalk files differ only in the order of the two
  notes on row 127.
- **Line lengths.** No line exceeds 121 characters, counted in characters, in chapters 33 and 34 or in PAPER.md, in A,
  B or C. In the assembled paper:
  - the index-0 text is at most 117 characters per line;
  - the overview is at most 113;
  - the lemma line is 120.

  With every label replaced by "Proposition 33.123", the new texts reach at most 121.
- **Typography.** No new line starts with "+ ", "- ", "* ", "> ", "#", "=", "|" or "<". There is no backslash, and no
  label is added or changed.
- **Citations after the change.** "[Mel93" and "[Hin26a, p. 91]" are gone from chapter 33. thm:std-relative-index is
  cited once, in P-RI-1. lem:s14-tf-inputs (v) is cited nowhere.
- **The proof file.** The only lines over 121 characters in P-RI.md are the two one-line crosswalk notes inside
  fences.
