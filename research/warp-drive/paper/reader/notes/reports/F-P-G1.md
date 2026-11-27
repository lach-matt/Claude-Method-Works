# F-P-G1: fix round on proofs/P-G1.md (gap G1)

File: research/warp-drive/paper/reader/proofs/P-G1.md
- New md5 d7105443b0800ac5c3433179b5f4e285, 1224 lines. The read version was 1cd8f781545862cce8159aed13a34a31, 942 lines.
- Insertable section: lines 1–575. Placement, merge order and crosswalk: lines 577–1224.
- Nothing else in the repository was edited. No chapter, crosswalk, Appendix A, bibliography or P-G24b file was touched. Nothing was committed.

## M1: settled without the misprint and without an author decision

The reader was right, and my earlier report (P-G1 §3) was wrong on one point: the published Theorem 3.52 does not correct (3.38). Both versions print A_1 in the last place.

The disjoint-support lemma (lem:iv5-calc-disjoint, lines 160–233) is now proved from statements [Hin26d] actually prints. It no longer uses (3.38) or Lemma 3.28, and (S16) quotes neither. The proof runs as follows.

1. **Essential supports.** E_1 ∩ E_2 = ∅, by the argument as before, from Definition 3.25 and Lemma 3.24 (1).
2. **The operator.** X := Op(c_1)TOp(c_2) lies in the calculus by the composition statement of Theorem 3.51. It maps C_c^∞ to itself (p. 44, and Definition 3.34).
3. **Mapping property.** Microlocality, Proposition 3.55 (2), applied three times gives WF(Xu) ⊂ E_2 ∩ E_1 = ∅. Proposition 3.55 (1) then gives Xu ∈ ww′ρ̄^LH^L for every u ∈ w′ρ̄^(−L)H^(−L). Boundedness follows from the closed graph theorem, using Theorem 3.44 and (3.14).
4. **Adjoint.** The duality (3.19) of Proposition 3.22, with the density of Lemma 3.20, gives the bounds for X*.
5. **W-regularity.** On N_(P′) one has 𝒲 = ρ̄⁻¹𝒱. With the norm of p. 37 and Proposition 3.19, this gives wH^s ⊃ wH^(s;k) ⊃ wρ̄^kH^(s+k), so the k = 0 bounds imply all k.
6. **Conclusion.** X satisfies Definition 3.34, so X is a residual operator, and X ∈ wρ̄^LΨ^(−L) for every L by Definition 3.43.

Everything downstream is unchanged: microsupport, (c), (e), Lemma C, and C33-5, -9 and -11.

(S16) now quotes, verbatim from arXiv v1 with pages:
- Lemma 3.18 and the norm after it (p. 37);
- Lemma 3.20 (p. 38);
- Proposition 3.22 with (3.19) (p. 39);
- Lemma 3.24 (1) (p. 40);
- Definition 3.25 (p. 41);
- the sentence after Definition 3.31 (p. 44);
- Definition 3.34 with (3.30) (p. 46);
- Definition 3.43, including its first sentence (p. 51);
- the Poisson-bracket sentence of Theorem 3.51 (p. 55);
- Definition 3.54 and Proposition 3.55 (1), (2) (p. 57).

Checks against the published text:
- Definition 3.55 and Proposition 3.56 (1), (2): identical wording, read through the excerpt fetch.
- Definition 3.34: published wording "such that (1)" against v1 "with the following properties. (1)". (S16) quotes v1, as Appendix A does throughout.
- Definition 3.17, the p. 37 norm, Proposition 3.19 and Proposition 3.22: same text in the published partial copy.

For transparency: [Hin26d] proves Proposition 3.55 (2) by pointing to "standard applications of the principal symbol calculus". The edition cites the printed statement, which is correct as printed.

## Minor findings and nits

All are applied in the reader's words, with these exceptions.

- **n4.** The sentence now reads "the Q-terms add at most (9C₂ + 2)𝔛⁻² + C′_𝔛h to the coefficient −c_0 of ‖Aω‖², where C₂ does not depend on 𝔛 and C′_𝔛 does not depend on h". I used this rather than "−¾c_0" because the Cauchy–Schwarz step is written out only in P-G24b's T41. The two lines that variant A of T41 anchors on are unchanged.
- **n9.** No change, as the reader advised.
- **m8.** Every placement is now given as whole chapter lines between fences, so no rewrapping is needed in context.
- **m7.** C33-11 is fenced and rewrapped. No line of it starts with "|".
- **m4.** The numbering note now covers Sections 1–4. Sections 2 and 4 were checked in the published text:
  - Prop. 2.3 → 2.4, with (2.5) → (2.6);
  - Prop. 4.2 and Def. 4.6 keep their numbers;
  - Defs 4.11, 4.14, 4.20 → 4.12, 4.15, 4.21;
  - Props 4.15, 4.17, 4.18, 4.22 → 4.16, 4.18, 4.19, 4.23;
  - every display (4.n) → (4.n + 1).

  In Section 3 the shift runs from Lemma 3.36 (n13). The note also lists Def. 3.54 → 3.55 and Theorem 3.52 → 3.53.

Additions of my own:
- C33-6 now says the regularised estimate follows "by the argument below with prop:np-10-65-a (e) and the same iteration" (the reader's open point 3).
- The disjoint lemma reduces to scalar symbols through (S14).
- C95-1 now lists Lemma 3.18, (3.19) and (3.30), and no longer lists Lemma 3.28 or (3.38).

**Crosswalk (m5, n15).**
- The prop:np-10-65-a row after def:iv5-0-1 is deleted.
- Fourteen rows go after lem:iv5-0-5, as paper/reader/proofs/P-G1.md@PIN:a-b with line ranges. PIN is pinned at merge.
- Twelve "G1:" notes are given for the changed rows.
- Every row is at most 121 characters.

## Old texts and the merge with P-G24b

**Source of the old texts.** Every old text was re-copied from HEAD fb87f2fc as whole lines and located by content. The chapter md5s at HEAD:
- chapter 33: 9571426c…, which includes the M-T49 merge;
- chapter 95: 66591dd9…;
- chapter 23: 58661f32…;
- chapter 98: 63661326….

Each old text occurs exactly once.

**Line numbers.** P-G24b's old texts come from 007858d8…. Its line numbers are one less than HEAD's from line 116 on, but all 43 still occur exactly once at HEAD.

**Merge order: P-G1 first, then P-G24b.**
- **C33-11 and T41.** After C33-11, use variant A of T41. Its old text, the last two lines of C33-11, is found exactly once.
- **C33-12 and T7.** They share "[[lem:iv5-0-5]] (6) on supp ψ′." at the start of line 1534. C33-12 keeps those words at the start of its first line, so T7's old text is still found exactly once.
- **C33-20 and T34.** C33-20 inserts a paragraph before T34's old text without changing it.
- **Adjacent but not overlapping:** T42/C33-9 (lines 1463/1464) and T5/C33-10 (lines 1505/1506).
- No other old texts share a character.

## Checks on a scratch copy

**P-G1 applied** (the copy is in scratchpad/fg1/merge):
- the chapter lint run reports 0 hits (62 files, 4662 labels);
- the assembly check reports 0 problems;
- no line over 121 characters, raw or after label resolution, in chapters 23, 33, 95 or 98;
- crosswalk 33 has 213 rows for 213 labels, in chapter order;
- C23-1 applied in a separate copy: lint 0 hits.

**P-G1 then all of P-G24b** (T41 by variant A): lint 0 hits, assembly 0 problems (4678 labels), and no line over 121 characters in any chapter, raw or resolved.

**The proof file itself.** Lines 1–575 have:
- 8 proofs and 8 ∎;
- no backslash and lowercase labels;
- no lint hits except cross-chapter labels.

The placement part of the file has the expected hits (fences, file paths, md5s).

## Incident

Early in this round I ran assemble.py with --help in the repository to read its options. It does not parse --help, so it assembled and wrote PAPER.md. I restored PAPER.md from HEAD with git checkout about ten seconds later. No snapshot commit captured the rewritten file; the last commit touching PAPER.md is a6e37e7d, 13:30.

## Not closed

1. Published page numbers of [Hin26d] remain unknown, because the proxy refuses ams.org. Appendix A keeps the v1 pages, with the numbering note.
2. C23-1 stays optional. Applying it needs a check of 27:460 (lem:ii-f-2-2 (c), uniform in h) and 37:824, which relied on the old words "the above holds uniformly in p". That is outside G1.
