# Second reading of proofs/P-LB.md (md5 b769e8df079712aba31e21bf8c401639, 508 lines)

Verdict: CONFIRMED. All 15 findings of R-P-LB are resolved. The file holds together end to end, and I find no new Major
or minor issue. Four new nits are listed below; none of them blocks the merge.

Line numbers are those of P-LB.md unless a chapter is named. Chapter line numbers are those of the current tree
(HEAD 99cdddb7, with P-K.md modified in the working tree; no chapter is modified).

## The fifteen findings

- **m1** resolved, line 5 (lines 4–6). It now reads "a lower bound for d_acc, and so for d_NM and N_NM, and an upper
  bound for δ". This matches [[cor:ec-lb-delta]].
- **m2** resolved, line 373: "as z tends to 0 or γ_C to infinity". Text 6 is still six lines (369–374).
- **m3** resolved, lines 347–350. Line 343 now says "the six lines". The sentence states the bound at that point's z,
  and g is cited to [[eq:ec-lb-g]]. Read under the convention of [[sec:ec-gauge-gap]] ("Throughout, z = 4·10⁻⁶",
  chapter 71 line 1314), the sentence is now true at every point of the proved set. It is exactly
  [[thm:ec-lb-proved]]'s display [[eq:ec-lb-bound]]. γ_C is not fixed by the section's convention, so it is read as that
  point's damping parameter. The wording can be tightened (nit N1).
- **m4** resolved.
  - **B_g and B_η in P-LB.** They occur only in [[lem:ec-lb-rounds]] (124–162), [[thm:ec-lb-proved]] and its proof
    (169–202), [[rem:ec-lb-conditions]] (226, "6B_η") and the crosswalk rows (485, 486, 488). Every use is consistent:
    - B_g bounds ε_g, ε_K and the increments;
    - B_η bounds ε_K and η_2;
    - in the theorem, B_g = min(g(z), 40h/13) and B_η = 40h/13.
  - **δ̂ and δ̄.** δ̂ occurs once, at line 67 ("the number δ̂ of [[prop:ec-rounds]]"). That is correct: chapter 71
    line 1397 defines δ̂ := 1.46214·10⁻¹⁰ there. δ̄ does not occur.
  - **B_g and B_η in the chapters.** The answer to the check is no: they are used elsewhere with other meanings, though
    never in chapters 40, 41 or 71.
    - B_g is the Bianchi gauge operator div_g Gt in chapter 07 (lines 44, 46, 112, [[eq:data-bianchi]]), chapter 80
      (1099, 1122), chapter 81 (304, 307, 338, 1002), chapter 82 (1078) and chapter 84 (372).
    - B_g is a term of [Hin23a] in chapter 45 (617–618).
    - B_η is a subspace B^∞_η of [[thm:ii-g-2-1]] in chapter 46 (1540, 1557, 1568: "U ∈ B_η").
    - Each new use is bound explicitly in its own statement, and the old uses are different kinds of object in other
      chapters. So I grade this a nit (N3), with an optional rename.
- **m5** resolved.
  - Item 12 (457–470) gives the old and new texts.
  - Item 11 (line 453) now excepts [[rem:s14-eps-ind-scope]].
  - The crosswalk note is at lines 501–502.
  - The old text occurs once in the current chapter 33, at lines 3534–3535, followed by "defined.".
  - The merged remark reads correctly: "which is the smaller for h ≤ 6.309·10⁻⁹" is true, since the crossover is at
    6.30945·10⁻⁹.
- **n1** resolved, lines 91–92. The majorants hold for every e ∈ [0, 10⁻⁵]: recomputed, they are 1635.54, 2645.10,
  2855.08, 4141.03, 2358.03, 1654.76 and 848.59, against the printed 1636, 2646, 2856, 4142, 2359, 1655 and 849.
- **n2** resolved, lines 320–321: "and / 𝖧 ⊂ (0, h_*); so h = 10⁻⁶ is not in 𝖧". No line starts with ⊂.
- **n3** resolved, lines 322–324: "is not shown to lie below them." "not decided" occurs only once, at line 322.
- **n4** resolved, line 225: "through v = 1/2 and e in P_2 and [[eq:s14-f-two]]".
- **n5** resolved. Line 229 is the (C4) item. Line 237 reads "not (C2), (C3) or (C5), nor (C4) beyond the existence of
  ε_ind". The two agree, and (C1)–(C4) are row c3 and (C5) is row c4 (chapter 46).
- **n6** resolved, lines 238–239: "the data classes (rows d1–d2), the parameter set ℬ_* (rows b1–b4) or the smallness of
  row n1".
- **n7** resolved, lines 241–242: "which implies the bound 1.403 × 10²⁰ of [[thm:loss-d]] (ii)".
- **n8** resolved, line 451. See nit N4 for a remaining imprecision; it is merge-instruction text, not chapter text.
- **n9** resolved, line 67. The empty sentence is gone, and the paragraph ends at "[[prop:ec-rounds]]."
- **n10** resolved, lines 505–508. P-K.md as it now stands (md5 e38d85b60ed9a392d9f143d944a8ed06, lines 462–466)
  still appends notes to ch:explicit-constants (its text 2) and to sec:scope-constants (its texts 8–9). So the
  paragraph is accurate.

## New findings

### Major

None.

### minor

None.

### Nits

**N1. Lines 348–350 (text 4): "not 4·10⁻⁶" can be read as saying z ≠ 4·10⁻⁶, and R is not tied to the point.**
Whether (γ_Υ, e_Υ) = (1/100, 1/100), and so z = 4·10⁻⁶, is admissible is undecided ([[rem:ec-point-outside]],
[[rem:ec-lb-unbounded]]). So the text should not seem to exclude that value. Also, R in [[thm:loss-d]] (ii) is "the
number of rounds of [[prop:ec-rounds]]", which is the count at the computational point; here it is the count at the
point in question.

Old (lines 348–350):

    proved, d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²), where z = 4e_Υγ_Υ² is that point's gauge parameter, not
    4·10⁻⁶, and g is the function of [[eq:ec-lb-g]] ([[thm:ec-lb-proved]]). The bound (iii) is explicit in the numbers of
    steps, which

New (still three lines, 107, 114 and 82 characters; after resolution at most 107; text 4 stays "the six lines"):

    proved, d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²), where R is the number of rounds at that point,
    z = 4e_Υγ_Υ² its gauge parameter (not the value 4·10⁻⁶ fixed in this section) and g the function of [[eq:ec-lb-g]]
    ([[thm:ec-lb-proved]]). The bound (iii) is explicit in the numbers of steps, which

**N2. Lines 332–334 (text 3): "the lower bound" reads as the bound of [[thm:loss-d]].**
The sentence before says that "the lower bound of [[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at
every h". Then "At every point of the proved set the lower bound holds as an explicit function of z … and h" reads as
if that bound, 1.403 × 10²⁰, held on the proved set. It does not: it is a different bound. That bound also uses more
than the two properties just listed, namely ε_Υ < g(z) and ε_ind(h) < 40h/13, which the kept sentence "the theorems use
only 0 < ε_ind(h) ≤ δ_50" does not mention.

Old (lines 332–334):

    every h, ε_Υ being fixed by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). At every point of the proved set the
    lower bound holds as an explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated
    ([[thm:ec-lb-proved]]).

New (still three lines, 117, 118 and 110 characters; after resolution at most 118; text 3 stays "the seventeen lines"):

    every h, ε_Υ being fixed by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). At every point of the proved set a
    lower bound for d holds as an explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated, through bounds for
    ε_Υ and ε_ind(h) that hold at every such point ([[lem:ec-lb-gauge]], [[lem:ec-lb-ind]], [[thm:ec-lb-proved]]).

The crosswalk note for rem:ec-point-outside (line 496, "last sentence cites thm:ec-lb-proved") stays true.

**N3. B_g and B_η are used elsewhere in the paper with other meanings (see m4).** B_g is the Bianchi gauge operator of
chapters 07, 80, 81, 82 and 84 and a term of [Hin23a] in chapter 45. B_η is the Nash–Moser subspace written B_η in
chapter 46. None of these occur in chapters 40, 41 or 71, and the new symbols are numbers bound in their own statements.
The paper already reuses g and h in the same way. I recommend no change.

If a pair used nowhere else is wanted, replace every B_g by Θ_g and every B_η by Θ_η in P-LB.md: all 80 occurrences, on
lines 124–202, 226 and 485–488. Θ_g and Θ_η occur in no chapter, and Θ_ occurs nowhere in chapters 40, 41 or 71. Θ is
one code point, like B, so no line length changes.

**N4. Line 451 (item 11, merge instructions only): "follows from [[thm:ec-lb-proved]] at z = 4·10⁻⁶".**
The last sentence of [[prop:ec-rounds]] is about the point (γ_Υ, e_Υ) = (1/100, 1/100) at every h ∈ 𝖧. That point is not
known to satisfy the hypotheses of [[thm:ec-lb-proved]], which asks for all the conditions of [[sec:vi-c-1]]. The
sentence follows from the theorem's proof by the next-to-last sentence of [[rem:ec-lb-conditions]]: "It holds as well at
every (h, z) … at which the constructions … are run with constants satisfying the conditions listed". This text is not
merged into any chapter.

Old (lines 451–453):

    on every h ∈ 𝖧 with the same (γ_Υ, e_Υ), stays true and follows from [[thm:ec-lb-proved]] at z = 4·10⁻⁶), the statement
    of [[thm:loss-d]], [[cor:uc-two-offsets]], [[thm:uc-reduction]], [[thm:uc-integer]] with [[eq:uc-lower]], and every
    statement of [[ch:s14]] except [[rem:s14-eps-ind-scope]] (text 12) keep their texts. The numeric lower bound

New (four lines, at most 117 characters):

    on every h ∈ 𝖧 with the same (γ_Υ, e_Υ), stays true and, by [[rem:ec-lb-conditions]], follows from the proof of
    [[thm:ec-lb-proved]] at z = 4·10⁻⁶), the statement of [[thm:loss-d]], [[cor:uc-two-offsets]], [[thm:uc-reduction]],
    [[thm:uc-integer]] with [[eq:uc-lower]], and every statement of [[ch:s14]] except [[rem:s14-eps-ind-scope]] (text 12)
    keep their texts. The numeric lower bound

## What I checked and found correct

- **The proofs, re-read line by line.**
  - [[lem:ec-lb-gauge]] (a)–(d). The discriminant, s_± and 1 + 4s_± are as stated. The w-bounds are as stated, with
    the identity (z²/(2u))(u² − 1 − z/4). For d₂: 2uA = 240 and 4u²A³ = 864000. For d₁: 342 and 2222316, and
    6561·21600 = 141717600 < 142228224. Also 5/171 − 7/240 = 1/13680, c = 30031/16416000, and
    30031·544 = 16336864 < 16416000.
  - As a cross-check, (b), (c) and ½(d₁(8) − d₂(7)) ≤ g(z) hold at 229 points of (0, ½] (z = i/400 and z = 10⁻¹, …,
    10⁻²⁹), recomputed with mpmath at 120 digits.
  - [[lem:ec-lb-ind]]. I re-expanded f₀ + f₁(hξ) + … + f₆(hξ)⁶ of [[eq:s14-f-two]] (chapter 33 line 889) at κ = 8 with
    sympy. All nine p_j agree identically with lines 84–87, and f₀ and f₁ agree with line 89.
  - The tail is 0.0016360 < 0.0017.
  - p₂(40/13) = −(9280 + 59920e)/169 = −11879149/216320 = −54.9147. p₂(38/13) = −(9306 + 57346e)/169 = −55.0684.
  - p₂′ ≥ 152/13 − 11 − 159e = 0.69075 > 0.69. 6·10⁶e = 1875/32, and the margin is 3.522 > 3.5.
  - [[lem:ec-lb-rounds]]. Both counts follow from the stated bounds:
    - #{i ≥ 0 : 2 + (i + 1)B_g ≤ β − B_g} ≥ g_1(β)/B_g;
    - #{i ≥ 0 : 1 + B_η + iB_g ≤ β − 2} ≥ g_2(β)/B_g.
  - [[lem:ec-level-sum]] (chapter 71) applies as stated, with c = ε_K, both spans below 1, and g_1, g_2 vanishing below
    b_1 and c_1.
  - Both integrals and the final inequality recompute. The monotonicity in ε_K on (0, B_g] uses 5B_g + B_η < 1.
  - [[thm:ec-lb-proved]].
    - ε_g = min(ε_Υ, ε_ind) < min(g(z), 40h/13) = B_g.
    - ε_K < ε_g, ε_K < ε_ind < B_η and η_2 < ε_+ < ε_ind < B_η.
    - 5B_g + B_η ≤ 6B_η ≤ (240/13)·10⁻⁶ = 1.846·10⁻⁵.
    - 1/B_g² = max(g(z)⁻², (13γ_C/40)²).
    - The loss step does not depend on the point.
  - [[cor:ec-lb-delta]], [[rem:ec-lb-conditions]] and [[rem:ec-lb-unbounded]]: every step checks.
  - All 79 distinct labels cited in P-LB.md resolve in the merged tree.
- **The constants**, recomputed in exact rational arithmetic (fractions), with mpmath for the square roots.
  - 3·27360²(1 − 2·10⁻⁵) = 2245663885.8 > 2.24566·10⁹ > 2.2456·10⁹, and 27360/1088 = 25.1471 < 25.15.
  - 3(13/40)²(1 − 2·10⁻⁵) = 0.31686866 > 0.31686 > 0.3168.
  - 21·2.24566·10⁹ = 4.715886·10¹⁰ > 4.7158·10¹⁰, and 21·0.31686 = 6.65406 > 6.654.
  - 2.24566·10⁹/16 = 1.4035375·10⁸ > 1.4035·10⁸, and 25.15·4 = 100.6 exactly.
  - (59/196)·32 = 472/49. (472/49)·2.24566·10⁹ = 2.16317·10¹⁰ > 2.163·10¹⁰, and (472/49)·0.31686 = 3.052202 > 3.052.
  - 0.3168/(4.48·10⁻²⁶)² = 1.57844·10⁵⁰ > 1.57157·10⁵⁰, with the crossover at 4.48979·10⁻²⁶.
  - 3(1 − 2·10⁻⁵)g(4·10⁻⁶)⁻² = 1.4032576·10²⁰ > 1.4032·10²⁰, and g(4·10⁻⁶) = 1.4621354·10⁻¹⁰ < 1.46214·10⁻¹⁰.
  - The crossover of 0.3168h⁻² with 1.4032·10²⁰ is at 4.7515·10⁻¹¹, so "h < 4.75·10⁻¹¹" is right.
  - (c) at z = 4·10⁻⁶ gives 2.9239692·10⁻¹⁰ and 2.9242707·10⁻¹⁰, consistent with line 66 and [[eq:ec-gauge-gap]].
  - (40/13)·6.309·10⁻⁹ = 1.941231·10⁻⁸ < δ_50.
- **The placements.**
  - Every old text occurs exactly once in the current chapters, as whole lines, at the stated lines:
    - chapter 71: 16, 49, 1462, 1512 and 4693;
    - chapter 00: 32; chapter 01: 150; chapter 03: 351; chapter 90: 66; chapter 33: 3534.
  - "stop." is line 1527 of chapter 71, a blank line follows, and the heading of [[sec:ec-upper]] is at line 1529.
  - All stated line counts of old and new texts are right, and the crosswalk line numbers (1, 12, 29, 69, 72, 80, 98, 117,
    124, 133, 164, 175, 180, 210, 222, 244) match the file.
  - The existing rows that the notes annotate exist: rem:s14-eps-ind-scope (chapter 33), sec:scope-constants,
    sec:introduction-scope and sec:further-results. The front-matter crosswalk has no rows.
- **The trial merge.** I applied texts 2–10 and 12 and inserted the section in a scratch copy of chapters/, crosswalk/,
  assemble.py and lint.py. The results:
  - lint --chapters: 62 files, 4609 labels (4593 + 16), 0 hits, including chapter 20;
  - assemble --check: 0 problems;
  - assembled lint --paper: 0 hits;
  - no line of the assembled paper is over 121 characters (code points) after label resolution (the new section is at
    most 120);
  - every source line of P-LB.md is at most 121 characters;
  - every merged text reads correctly in its context, including text 12 before "defined." and text 10 before "These are
    lower bounds …";
  - thm:ec-lb-proved resolves to Theorem 49.38.
- **Typography.** No wrapped line of P-LB.md starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The only such lines
  are the three headings and the intended list items (225–233, 415, 425). All labels are lowercase. The 16 new labels
  are defined nowhere else.
