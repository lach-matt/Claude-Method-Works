# R-P-T49: independent reading of proofs/P-T49.md (md5 81f3f0edc4d7918bfe12c8c1fafe5c6b, 664 lines)

**Verdict: NOT CONFIRMED. 2 Major, 8 minor, 9 nits.**

The mathematics of the new section holds. I recomputed every displayed identity, both printed tables, every root
bracket and every numerical bound exactly, and all of them are correct (list at the end). The argument of
thm:t49-uniform covers the whole range 0 < h ≤ 10⁻⁶ and 0 < z ≤ ½: real intervals in s and y, and no grid points.

The two Majors are these:
- Placement text 6 inserts a false sentence into prop:is-mult.
- rem:t49-count states unproved results as facts.

The minors fall into three groups:
- Two placement texts (4 and 7) do not apply to the current chapters.
- Two remarks of chapter 71 become false after the merge, and no placement text covers them.
- Five are local imprecisions in the section.

The chapters changed while I read: HEAD went from ef06059e to 59de7926, and the uncommitted P-T78 merge is in the
working tree, touching chapters 32, 34, 35, 46, 71 and 90. Every line number below is in that working tree, at the
time of reading. Each old text in a replacement proposed below was checked to occur exactly once there.

---

## Major

### M1. Placement text 6 (P-T49.md line 600): the new sentence on hκ > 70 is false

Current text (new text 6, first sentence):

    strip −101 ≤ Re ≤ 5. No root of P_l with hκ > 70, κ = l(l + 2), has real part at most 51 ([[cor:t49-right]]). The

**What is wrong.**
- cor:t49-right proves that three roots have real part greater than 51 and three have real part *less than −5·10⁵*.
  So every P_l with hκ > 70 has three roots of real part at most 51. The sentence contradicts the corollary it cites,
  and [[prop:s14-scalar-every-h]] as well.
- What the corollary proves is "no root with real part in [2, 51]". Together with [[prop:np-10-54]], that also
  excludes every real part in [−100, 51].
- A second, smaller defect is in the last sentence of the new text. It cites thm:t49-point for "N(L̂_b(0), ·)⁻¹ has
  only simple poles". thm:t49-point does not state this. The pole statement follows from the theorem together with
  the "poles" paragraph of prop:is-mult's own proof.
- Chapter 71 writes 𝖹_exc (rem:ec-lb-conditions, rem:ec-point-outside), and in prop:is-mult's proof the letter Z
  already names a set of roots. The new text should therefore use 𝖹_exc.

**Replacement.** New text 6, the five lines replacing the four old lines (chapter 71, now lines 3123–3126; the old
text is unchanged and occurs once):

    strip −101 ≤ Re ≤ 5. No root of P_l with hκ > 70, κ = l(l + 2), has real part in [2, 51] ([[cor:t49-right]]). The
    roots of real part below −101 (the ι^C_(·,≪) − 1 and the gauge roots −l, 1 − l, 2 − l, 2 − ι^Υ of large degree) are
    simple as well: (C1)–(C4) of [[sec:iii-f1-1]] hold at h = 10⁻⁶ and 𝖹_exc is empty there, so every indicial root of
    L̂_b(0) is simple at each type and degree at which it occurs ([[thm:t49-point]]), and N(L̂_b(0), ·)⁻¹ has only simple
    poles, by the argument for the poles in the proof below.

Also change "New, the four lines:" (line 598) to "New, the five lines:". Update the line range "(lines 2846–2849)"
(line 591) to the current lines.

### M2. rem:t49-count (lines 319–361) states unproved results as facts; it should be removed

**What is wrong.**
- The remark asserts five exact results without proof:
  - that 𝖹 ∩ I is finite;
  - that there are 138863520426 discriminant pairs and 37085751 points of 𝖹₃;
  - that 𝖹₁ ∩ I = 𝖹₁′ ∩ I;
  - that there are about 2.7·10⁵ points with ε_ind = 0;
  - that 𝖹 ∩ (9.9999980542·10⁻⁷, 10⁻⁶] = ∅.
- It says itself that these rest on "exact evaluations … not written out here".
- The contract is that the paper states only what it proves.
- STYLE §1 allows two forms for such material. The first is a pending marker for the coordinator. The second, by the
  author's ruling (ii), is a one-paragraph "(Numerical observation.)" remark saying what was observed and that no
  proof uses it.
- rem:t49-count is neither. It is five paragraphs long, it asserts its claims as results ("Hence 𝖹 ∩ I = 𝖹₁ ∩ I is
  finite"), and its marker would block assembly.
- Being unused does not cure an unproved statement. A remark that a reader cannot check from the text does not belong
  in an edition whose rule is that every claim is proved in it.

**Spot checks** (they do not change the recommendation; they tell the coordinator whether the numbers can be trusted):
- disc_ι P(·; κ, h) is a positive multiple of h⁶D̃(κ, h), where D̃ has integer coefficients and degree 9 in κ and 24
  in h.
- At h = h₁ its four positive roots are 17063.8228…, 9.375921…·10¹⁶, 4.756190…·10²¹ and 4.843977…·10²¹, as (i)
  states.
- The root of D̃(4959862·4959864, ·) below 10⁻⁶ is 9.9999980541988·10⁻⁷, as (iv) states.
- I did not check the counts.

**Recommendation: remove the remark, and say in rem:t49-scope what is not decided.** Exact changes:

(a) Delete lines 319–361 (from "**Remark {#rem:t49-count}**" through the blank line that follows (v)).

(b) In rem:t49-scope, add "whether 𝖹 ∩ I is finite is not decided here". This is part of the replacement in m8
below.

(c) In placement text 1 (lines 540–549), drop rem:t49-count from the label list and delete the last sentence
("[[rem:t49-count]] carries the pending marker computational-1: … as the coordinator decides."). n3 gives the full
replacement.

(d) Delete the crosswalk row "rem:t49-count …" (line 651), and renumber the later rows to the lines of the revised
file.

Nothing else cites rem:t49-count. I checked:
- No chapter cites it.
- No other proof file cites it.
- In P-T49.md it is named only in text 1 and in the crosswalk row.
- P-ADM (proofs/P-ADM.md:909) mentions its pending marker only as the one lint hit of a scratch merge.

**If the coordinator and the author decide to keep the observation**, the only form the contract allows is ruling (ii).
The replacement for lines 319–360 would then be the following four lines. They lint clean, and are at most 116
characters after label resolution:

    **Remark {#rem:t49-count}** (Numerical observation.) The discriminants and resultants of [[rem:t49-sets]] (a) were
    evaluated exactly in rational arithmetic as polynomials in h, of degree up to 393, and their roots in I isolated. In
    this computation 𝖹 ∩ I is finite, with at most 138900606177 points, its largest point is 9.99999805419…·10⁻⁷, and at
    about 2.7·10⁵ of its points ε_ind = 0. No proof of this paper uses these observations.

---

## minor

### m1. Placement text 4 (lines 570–579): the old text does not occur in chapter 33

The quoted old lines, "[[cor:s14-eps-ind-point]] shows that this upper bound is attained … / defined.", are not in the
chapter. The P-LB merge (a722cb42) rewrote the end of rem:s14-eps-ind-scope. The current last three lines (chapter 33,
lines 3538–3540) are:

    ε_ind(h) < 40h/13 of [[lem:ec-lb-ind]], which is the smaller for h ≤ 6.309·10⁻⁹. [[cor:s14-eps-ind-point]] shows that
    the upper bound δ_50 is attained at the end h = 10⁻⁶ of the interval on which ε_ind is
    defined.

**Replacement for text 4.** Old: the three lines above. New, the four lines:

    ε_ind(h) < 40h/13 of [[lem:ec-lb-ind]], which is the smaller for h ≤ 6.309·10⁻⁹. [[cor:s14-eps-ind-point]] shows that
    the upper bound δ_50 is attained at the end h = 10⁻⁶ of the interval on which ε_ind is defined; no positive lower
    bound for ε_ind holds on any subinterval of (0, 10⁻⁶] of length 2·10⁻⁹ with the countable set 𝖹 removed
    ([[prop:t49-vector]]), and the point h = 10⁻⁶ itself lies outside 𝖹 ([[thm:t49-point]]).

The heading becomes "*4. [[ch:s14]], [[rem:s14-eps-ind-scope]], its last three lines (lines 3538–3540).*". The added
clause is correct: prop:t49-vector (c), and thm:t49-point. It is consistent with the remark's "this paper does not
determine ε_ind(h) for h ∈ 𝖧 beyond …", because it adds a negative fact and not a value.

### m2. Placement text 7 (lines 607–622): the old text does not occur, and the fallback is not exact

The quoted old lines ("decided. So the computational point is … / … Every number of this chapter that depends on the
point is stated") are not in chapter 71. rem:ec-point-outside has been rewritten twice: by P-LB (merged), and now by
the P-T78 merge in the working tree. That merge also adds "the exclusion z_Υ ∉ 𝖹_exc of row u5 is a separate
condition".

The fallback paragraph (lines 619–622) asks for an insertion "and the lines rewrapped". That is not an exact text, and
the contract asks for one. The remark now writes 𝖹_exc, not Z_exc.

**Replacement for text 7** on the current text (chapter 71, lines 69–71). Old, the three lines:

    modification ([[sec:iii-d2-1]]). So the computational point is a point at which the formulas of the proof can be
    evaluated, not one at which the hypotheses of [[thm:settling]] are shown to hold. Every number of this chapter that
    depends on the point is stated at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)),

New, the five lines:

    modification ([[sec:iii-d2-1]]). So the computational point is a point at which the formulas of the proof can be
    evaluated, not one at which the hypotheses of [[thm:settling]] are shown to hold. Its damping and gauge parameters
    avoid the countable exclusions: h = 10⁻⁶ ∉ 𝖹, and the set 𝖹_exc of [[prop:iii-f1-2-3]] (e) is empty at h = 10⁻⁶
    ([[thm:t49-point]]). Every number of this chapter that depends on the point is stated at it. For h ∈ 𝖧 the theorems
    use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)),

Delete the fallback paragraph (lines 619–622). If P-ADM merges together with P-T49, P-ADM's item 31 already contains
this sentence and replaces text 7 (proofs/P-ADM.md:938–951). In that case text 7 lapses, and the note should say so.

### m3. Two remarks of chapter 71 become false after the merge; no placement text covers them, and text 8 says they stay

Text 8 (lines 624–626) says that everything in chapter 71 other than texts 6 and 7 keeps its text. Two remarks then
contradict what the merged section proves:

- **rem:is-summary**, chapter 71 line 3462: "…and their exact multiplicities, which this paper does not decide, are
  not needed." After the merge, thm:t49-point decides them: all are 1.
- **rem:sp-scope**, chapter 71 lines 4073–4079: "for x > 70 this paper locates the roots of P_l only in {Re ι > 2}
  with no real root in (2, 5], … but leaves the largest l contributing a pole below real part 5 unevaluated. This
  section does not determine the multiplicities … at most 7 everywhere". After the merge, cor:t49-right places those
  roots in Re ι > 51, and thm:t49-point makes every root simple.

Both remarks were in chapter 71 before P-T49 was written: rem:sp-scope since 74074c98.

**New text 9** (chapter 71, rem:is-summary, line 3462). Old, the line:

    these the bound 7 serves, and their exact multiplicities, which this paper does not decide, are not needed. So the

New, the line:

    these the bound 7 serves, and their exact multiplicities, which are 1 ([[thm:t49-point]]), are not needed. So the

**New text 10** (chapter 71, rem:sp-scope, lines 4073–4079). Old, the seven lines:

    x ≤ 70 the roots are enclosed by [[lem:s14-sextic-small]] and [[lem:s14-sextic-large]]; for x > 70 this paper locates
    the roots of P_l only in {Re ι > 2} with no real root in (2, 5], and shows those of real part at most 5 simple, which
    suffices for every statement above but leaves the largest l contributing a pole below real part 5 unevaluated. This
    section does not determine the multiplicities of the indicial roots of real part at most 0 or in (4, 5]: they are 1
    at real part in [−101, 5] ([[prop:is-mult]]) and at most 7 everywhere ([[prop:iii-f1-2-3]] (b)). Nor does it
    determine L of [[cor:sp-lstar]] (a), which lies in [39, 50] ([[prop:is-logs]]); l_* = 50 is admissible for every
    value of L in that range.

New, the five lines:

    x ≤ 70 the roots are enclosed by [[lem:s14-sextic-small]] and [[lem:s14-sextic-large]]; for x > 70 no root of P_l has
    real part in [2, 51] ([[cor:t49-right]]), so every pole of real part at most 5 comes from a degree with x ≤ 70. Every
    indicial root of L̂_b(0) is simple at each type and degree at which it occurs ([[thm:t49-point]]). This section does
    not determine L of [[cor:sp-lstar]] (a), which lies in [39, 50] ([[prop:is-logs]]); l_* = 50 is admissible for every
    value of L in that range.

No number changes. M ≤ 7 remains true, and max(1, L, M) = L still holds. The new text 10 does not claim that the
largest such l is evaluated. Text 8 becomes:

    *8. Unchanged.* Every statement and proof of [[ch:s14]] other than texts 3 and 4, the statement of
    [[prop:iii-f1-2-3]], the rows of [[sec:vi-c-1]] and [[thm:vi-c-2-1]], and every text of [[ch:explicit-constants]]
    other than texts 6, 7, 9 and 10 keep their texts. Row u5 of [[sec:vi-c-1]] stays true as written: 𝖹_exc is
    countable, being empty wherever (C2) holds.

Add to the crosswalk notes for chapter 71: rem:is-summary, "multiplicities below −101 are 1 (P-T49 text 9)";
rem:sp-scope, "x > 70 and multiplicities by cor:t49-right and thm:t49-point (P-T49 text 10)".

Optional: the opening of the section at chapter 71 line 2819 ("every multiplicity is at most 7, and every root of real
part in [−101, 5] is simple") stays true and can be left as it is.

### m4. rem:t49-sets (a), lines 25–26: "two distinct real roots" leaves out non-conjugate complex pairs

Current text:

    of the h at which (C2), (C3) or (C4) fails, and a point of 𝖹₁ ∖ 𝖹₁′ is one at which two distinct real roots of some
    P_l, or of C, have sum 2k for an integer k ∈ [3, 51].

**What is wrong.**
- At such a point, a resultant vanishes because 𝒜_k and ℬ_k share a root t. The proof of [[lem:iv4-1-3]] (b) treats
  only real t.
- A non-real t gives two non-real roots k ± i t^(1/2) that are not conjugates of each other, and their sum is 2k.
- For C (a cubic) this cannot happen, since it would need four roots k ± w, k ± w̄.
- For P_l, nothing in the paper excludes it. It would need two right roots of real part above 5·10⁵ + 2k, and the
  paper does not rule that out.
- What (C2) and (C4) do exclude is a double root and a conjugate pair with real part k.

**Replacement:**

    of the h at which (C2), (C3) or (C4) fails, and a point of 𝖹₁ ∖ 𝖹₁′ is one at which two distinct roots of some P_l,
    or of C, that are not complex conjugates of each other, have sum 2k for an integer k ∈ [3, 51].

### m5. Lines 4–5 and 14–15: 𝖹₃ and Z_exc are not unions of zero sets

**What is wrong.**
- "Each is a union of zero sets of explicit polynomials" (line 4) and "Each set below is a union, over the types and
  degrees, of the zero sets of finitely many polynomials" (line 14) hold for 𝖹₁ and 𝖹₂.
- 𝖹₃ is defined (in (c) and in [[prop:np-10-52]] (iii)) as the h at which a *non-real* root has integer real part.
  That is a subset of the zero sets of the resultants, which also vanish at real pairs with sum 2k.
- Z_exc is likewise a subset of the zero sets in z of the linear polynomials Q_l(μ − 3), resp. (μ − 5/2)² − 9/4 − z.

**Replacement for lines 4–6:**

    leaves out a countable set Z_exc of values of the gauge parameter z = 4e_Υγ_Υ². Each is contained in a union of zero
    sets of explicit polynomials. This section decides them at the damping point h = 10⁻⁶ of [[sec:s14-pa]], with
    z = 4·10⁻⁶, and describes 𝖹 on the interval

**Replacement for lines 14–15:**

    **Remark {#rem:t49-sets}** (The four sets.) Each set below is contained in a union, over the types and degrees, of
    the zero sets of finitely many polynomials, none of which vanishes identically; 𝖹₁ and 𝖹₂ are such unions.

### m6. lem:t49-shifted, line 85: a wrong value

The text says "2(s − 2)(3s − 8) is −4.56 at s = 7/5". At s = 7/5 the value is 2(−3/5)(−19/5) = 114/25 = **+4.56**.
The bound 22.54 is unaffected.

**Replacement in line 85:** "2(s − 2)(3s − 8) is −4.56 at" → "2(s − 2)(3s − 8) is 4.56 at".

### m7. prop:t49-six, lines 264–265: the stated method does not give |R₃ᵉ| < 43 and |R₃⁰| < 38

Current text:

    lies in [−6.96, −1.6] and the second in [3.2, 25.3], so |R₁⁰| < 7.1; and the sums of the moduli of the terms at
    ι = 59/20, x = 0.0185 give |R₂ᵉ| < 1070, |R₂⁰| < 4310, |R₃ᵉ| < 43, |R₃⁰| < 38. Hence

**What is wrong.**
- Expanded in ι, the sums of the moduli of the terms at ι = 59/20 are 508.3 for R₃ᵉ = ι⁵ − 3ι⁴ + ι³ + 3ι² − 2ι, and
  2870.3 for R₃⁰.
- For R₂ the sums are 1068.0 and 4307.5, which are correct.
- The bounds 43 and 38 are true: the maxima on 𝒥 are 42.09 and 6.06. They follow from the factored form.
- The conclusion |hW| < 5.7·10⁻⁵ is unaffected: these terms carry eh² and h³.

**Replacement:**

    lies in [−6.96, −1.6] and the second in [3.2, 25.3], so |R₁⁰| < 7.1; the sums of the moduli of the terms at
    ι = 59/20, x = 0.0185 give |R₂ᵉ| < 1070 and |R₂⁰| < 4310; the factors of R₃ᵉ = ι(ι − 2)(ι − 1)²(ι + 1) and of
    R₃⁰ = (3 − ι)R₃ᵉ are positive on 𝒥, so |R₃ᵉ| ≤ (59/20)(19/20)(39/20)²(79/20) < 42.1 and |R₃⁰| < (9/10)·42.1 < 38.
    Hence

(42.0932 < 42.1 and 0.9·42.1 = 37.89 < 38.) The line after "Hence" is the blank line before the display, as now.

### m8. rem:t49-scope, lines 362–370: three imprecise statements

**What is wrong.**
- "Away from the point, 𝖹₂ and Z_exc are empty and (C3) holds at every h ∈ (0, 10⁻⁶]" says Z_exc is empty at every h.
  thm:t49-uniform (iii) proves this only where (C2) holds, and (d) defines Z_exc only there.
- "𝖧 is open at h_*" does not give the reason. The reason is 𝖧 ⊂ (0, h_*) and h_* ≤ 10⁻⁶.
- The last sentence, "A statement made for every h ∈ 𝖧 ∩ I … fails on a set that meets every subinterval of I", is
  garbled. 𝖧 ∩ I may be empty, since h_* is not determined. What prop:t49-vector (c) gives is this: ε_ind has no
  positive lower bound on J ∖ 𝖹 for any interval J of length 2·10⁻⁹. Within (0, h_*), J ∖ 𝖹 = J ∩ 𝖧.

The replacement also carries M2 (b).

**Replacement for lines 362–370:**

    **Remark {#rem:t49-scope}** (What this decides.) At the damping point, the parts of rows c2, c3 and u5 of
    [[sec:vi-c-1]] that concern the indicial roots hold: h = 10⁻⁶ ∉ 𝖹, (C1)–(C4) hold, and Z_exc = ∅ at h = 10⁻⁶, so
    z = 4·10⁻⁶ ∉ Z_exc ([[thm:t49-point]]); every indicial root of L̂_b(0) at the computational point is simple. The
    computational point is not in 𝖧, because 𝖧 ⊂ (0, h_*) and h_* ≤ 10⁻⁶ ([[rem:ec-point-outside]]), and the thresholds
    h_0, h_tf of row c2 and those of rows u2–u4 are not determined. Away from the point, 𝖹₂ is empty and (C3) holds at
    every h ∈ (0, 10⁻⁶], and Z_exc is empty at every h at which (C2) holds ([[thm:t49-uniform]]); so 𝖹 = 𝖹₁ ∪ 𝖹₃, and,
    as (C2) holds at every h ∈ 𝖧, the order of choices in [[thm:vi-c-2-1]] meets no exclusion in z. The set 𝖹 meets I
    ([[prop:t49-six]]); whether 𝖹 ∩ I is finite is not decided here. For every interval J ⊂ (0, h_*) of length 2·10⁻⁹,
    ε_ind has no positive lower bound on J ∖ 𝖹 ([[prop:t49-vector]]); [[prop:np-10-52]] (iii) gives only ε_ind(h) > 0
    for h ∈ 𝖧.

P-ADM (proofs/P-ADM.md:966–978) proposes its own replacement for the first four sentences of this remark, because it
removes rows u2–u5. Whichever file merges second must rebase on the other's text.

---

## nits

### n1. cor:t49-right, lines 228–229 and 232–233

**What is wrong.**
- [[lem:s14-half-plane-count]] takes Ω ⊂ ℝ², but the proof applies it with Ω = [κ₀, ∞).
- The statement is for every *real* κ ≥ κ₀. [[prop:s14-scalar-every-h]] is stated only for κ = l(l + 2); its proof
  counts the roots on Ω₁ = [3, ∞) × (0, 10⁻⁶].

**Replacement for lines 228–229** (three lines):

    κ ≥ κ₀. By [[lem:s14-half-plane-count]] with Ω = [κ₀, ∞) × {10⁻⁶} the number of roots with real part greater than 51
    is the same for every κ ≥ κ₀. At κ = κ₀, x = hκ₀ = 69.989955 ∈ [35, 70], and [[lem:s14-sextic-large]] (a), (c) with
    the last

**Replacement for line 233:**

    [[prop:s14-scalar-every-h]], whose proof counts the roots for every real κ ≥ 3. ∎

### n2. prop:t49-pairs, lines 185–186: (C4) also needs the roots of C and of p_(v) to be real

**What is wrong.** The proposition concludes "(C4) holds at h = 10⁻⁶" from the statement about P_l alone. (C4)
concerns every type: scalar type 0 (P_0 = −(ι − 2)C) and the vector types (p_(v)). The reality of those roots is in
the proof of prop:t49-simple.

**Replacement for lines 185–186:**

    particular every root of P_l whose real part is an integer in [3, 51] is real, and so, the roots of C and of p_(v)
    being real (proof of [[prop:t49-simple]]), (C4) holds at h = 10⁻⁶; and none of the resultants of the third group of
    [[rem:t49-sets]] (a) vanishes at h = 10⁻⁶.

### n3. Placement text 1, lines 540–549: the anchor line

**What is wrong.**
- "defined." is line 3540 of chapter 33, not 3539.
- Text 4 rewrites that line. After text 4, the anchor "defined." no longer exists.

**Replacement for lines 540–549** (this also carries M2 (c)):

    *1. Where the section goes.* The section above, from its heading through [[rem:t49-scope]], is appended to [[ch:s14]]
    after its last line, the last line of [[rem:s14-eps-ind-scope]] as text 4 leaves it ("([[prop:t49-vector]]), and the
    point h = 10⁻⁶ itself lies outside 𝖹 ([[thm:t49-point]])."), with one blank line between. It defines
    sec:s14-exceptional, rem:t49-sets, sec:s14-exc-shifted, eq:t49-coeffs, eq:t49-shift, lem:t49-shifted,
    thm:t49-uniform, sec:s14-exc-point, eq:t49-disc, eq:t49-res, prop:t49-simple, prop:t49-pairs, thm:t49-point,
    cor:t49-right, sec:s14-exc-interval, eq:t49-delta, prop:t49-six, prop:t49-vector and rem:t49-scope, none of which is
    defined elsewhere, and cites only labels that the chapters define. It changes no statement of [[ch:s14]]:
    [[lem:iv4-1-3]], [[prop:np-10-52]], [[prop:s14-damping-distance]] and [[cor:s14-eps-ind-point]] stand as they are.

### n4. Stale line numbers in the placement headings

- Text 4: "(lines 3538–3539)". The current lines are 3538–3540.
- Text 6: "(lines 2846–2849)". The current lines are 3123–3126.
- Text 7: "(lines 53–54)". The current lines are 69–71.

The old texts of 3, 5 and 6 are exact and unique, so this is cosmetic.

### n5. Crosswalk rows, lines 633–658: the source column

The source column reads "paper/reader/proofs/P-T49.md:N", a single line and no commit. The existing rows pin a commit
and give a range, for example "paper/reader/proofs/P-A-indicial.md@0a8a4fa:349-381". Pin the rows to the commit of
confirmation and give line ranges, as the M-LB and M-K merges did.

### n6. eq:t49-disc, lines 152–153: "up to sign"

**What is wrong.** "…divided by the leading coefficient, up to sign" leaves the sign of 𝔇 open. The printed 𝔇 is
exactly 1/144 of the standard discriminant (−1)^15 Res_ι(𝒫, ∂_ι𝒫)/π₆. I checked this.

**Replacement:** "Its discriminant in ι is (−1)^15 times the resultant of 𝒫 and ∂_ι𝒫 divided by the leading
coefficient π₆, a polynomial in κ with integer coefficients; expanding it,".

### n7. Notation clash: c₀, …, c₃

In eq:t49-shift (lines 66–75), c₀, …, c₃ are polynomials in s. In the same chapter, [[lem:s14-sextic-split]] (ii)
writes c = c⁰ + hc₁ + h²c₂, and cor:t49-right (line 230) uses that c ("h·5155"). Renaming the shift coefficients, for
example to q₀, …, q₃, in lines 66–75 and 83–97, would avoid the clash. Optional.

### n8. 𝖹_exc in the chapter 71 texts

Chapter 71 writes 𝖹_exc (rem:ec-lb-conditions, rem:ec-point-outside). The replacements in M1 and m2 already use it.

### n9. sec:tab-t49-res, lines 476–530: optional leading digits

The table gives only the signs of 𝔖(k, l_k(l_k + 2)), 𝔖(k, (l_k + 1)(l_k + 3)) and the discriminants. The 𝔇 table
gives leading digits. Printing leading digits here too would make the 49 rows checkable at a glance. Optional.

---

## Placement and crosswalk: what was checked

- **Texts 3, 5 and 6.** Each old text occurs exactly once: chapter 33 line 114, chapter 34 line 490, chapter 71 line
  3123.
- **Texts 4 and 7.** The old texts occur nowhere (m1, m2).
- **Text 2.** Both anchors are unique: chapter 96 line 258 "*Used in* [[lem:s14-vector-distance]]." and line 260, the
  heading of sec:tab-s14-numerators.
- **The new texts in context.**
  - Text 3: correct (𝖹₂ = ∅, 10⁻⁶ ∉ 𝖹, and 𝖹 meets I are all proved).
  - Text 5: correct (thm:t49-uniform (ii) covers every z and every h ≤ 10⁻⁶; Z_exc at the constants is empty because
    (C2) holds on 𝖧).
  - Texts 4 and 7: correct in substance, once rebased.
  - Text 6: false in its first sentence (M1).
- **Scratch merge.**
  - I built a scratch copy of the current chapters with all texts applied: 1, 2, 3, 5 as written; 4, 6, 7 as
    corrected above; 9 and 10; and the section with the fixes above and rem:t49-count removed.
  - assemble.py's numbering and resolution report 0 problems. lint.py's assembled-mode scan of the result reports
    0 hits. With rem:t49-count kept, there is 1 hit, the pending marker.
  - No line exceeds 121 characters before or after label resolution, in the section, the tables, or any of the
    proposed texts.
- **Crosswalk.**
  - The 23 rows have four tab-separated columns, and the line numbers match the labels in P-T49.md as it stands.
  - The five existing rows named in "Notes to add" exist (eq:iv4-0-1 and rem:s14-eps-ind-scope in chapter 33,
    prop:iii-f1-2-3 in chapter 34, prop:is-mult and rem:ec-point-outside in chapter 71).
- **Typography of P-T49.md.**
  - Every line is at most 121 characters.
  - No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
  - Every label and reference is lowercase.
  - No label of the section is defined anywhere else.
- **Interaction.** P-ADM (unmerged) requires P-T49 to be merged first and cites thm:t49-point. Its item 31 supersedes
  text 7, and it rewrites rem:t49-sets (d) and rem:t49-scope (proofs/P-ADM.md:938–979).

---

## Recomputed and found correct

All of this was done with exact rational and integer arithmetic (python3 with sympy 1.14; fractions). Floating point
was used only to locate brackets, which were then confirmed exactly.

### The definitions (rem:t49-sets)

- 𝖹₁ matches the proof of [[lem:iv4-1-3]] (b) term for term: discriminants, C(2), the excluded points per type, and
  the resultants for k ∈ [3, 51].
- 𝖹₂ matches the proof of [[prop:np-10-52]] (ii): the eight points are 1 − l, 3 − l, l + 3, l + 5 and the roots of
  Q_l(ι − 1) plus 1; the vector points are p_(v) at 1 − l, 2 − l, l + 3, l + 4.
- 𝖹₃ matches [[prop:np-10-52]] (iii).
- Z_exc matches the proof of [[prop:iii-f1-2-3]] (e).
- (C1)–(C4) match sec:iii-f1-1, including the l = 1 set {0, 4, 6} and the l = 0 set {1, 3, 5}.
- d₁, d₂ ∈ (0, ¼) by eq:iii-d-4-2.
- The four numbers ι^Υ + 2 and 3 − ι^Υ are as stated.

### eq:t49-coeffs, eq:t49-shift and sec:tab-a-sextic

- All seven a_j(κ, h) equal the coefficients of det(hN_l) of eq:s14-nl at v = ½, e = 1/102400.
- 64·10¹⁸·a_j(κ, 10⁻⁶) = π_j of sec:tab-a-sextic.
- eq:t49-shift is an identity in (K, s, h, e) for both signs, with c₃, …, c₀ as printed.

### lem:t49-shifted

- The maxima on [7/5, 43/10] are 11.8, 22.54 and 13.754, then 37.6, 110.35 and 79.24, then 175.85, 325.23 and 194.96,
  each at s = 43/10.
- The 12 factors of the eh, h² and h³ terms are at most 1656 < 2000.
- |c₃| ≥ 1.99998. The bounds |c₂| < 11.8006, |c₁| < 22.5415 and |c₀| < 13.755 follow, and the sampled maxima are
  11.80081, 22.53925 and 13.75342.
- g(7.6) = 11.235, and g′ > 0 for K ≥ 7.6. √63 ≥ 7.6 > √48.
- For l ≤ 6: the perturbation sum is exactly 0.181816… < 0.19, and (2 − 14e)(1.7)²(0.7) = 4.0457 > 4.04.
- The y-ranges are [37/10, 113/10], and δ_l ≤ 2 − √3.

### thm:t49-uniform

- C(1), C(3), C(4) and C(5) are exactly as printed, and P_0 = −(ι − 2)C.
- The p_(v) values at l + 3, l + 4, 1 − l and 2 − l are as printed.
- The intervals for y ∓ (l + 1) and y ∓ K fall in [2, 43/10], resp. [7/5, 4], for every z ∈ (0, ½] and every l ≥ 1.
- The (iii) logic, with prop:iii-f1-2-3 (e) and (C1), is sound.

### eq:t49-disc and sec:tab-t49-disc

- disc_ι 𝒫 = 144·𝔇 exactly. I parsed all ten 𝔡_j from the file, and the digit groups are tens from the right.
- disc P = 9·2⁻⁵⁶·10⁻¹⁸⁰·𝔇.
- The signs are + − + + + + − + + + (four changes).
- The eight values 𝔇(n), 𝔇(n + 1) are integers with the printed signs and the printed leading digits, all correct
  truncations. For example 𝔇(214373185) = 1.00047834…·10¹⁵⁵.
- The roots are 18656.920380…, 214373184.714794…, 2354423533873.695235… and 24600231683951.517859…. The other five
  are real and negative.
- 𝔇 is squarefree (and irreducible).

### eq:t49-res and sec:tab-t49-res

- 𝒫(k + iy) = 𝒜_k(y²) + iyℬ_k(y²), with leading coefficients 64 and φ₅ = −384k − 255998991.
- Res_s(𝒜_k, ℬ_k) = 4𝔖 exactly. All 52 printed s_(a,b) were parsed and match; no non-zero coefficient is omitted.
  The degrees are 15 in k and 3 in κ.
- In the table of cubics, all 49 rows match: the coefficient signs, l_k, the signs of the two values, the sign of the
  discriminant, and the positive root to ten digits. For k = 3 the other two roots are −2443357.4 and −272837.4.

### prop:t49-simple, prop:t49-pairs and thm:t49-point

- At h = 10⁻⁶: C(−3·10⁶) = 5999945.4, C(−1.5·10⁶) = −375051.8, C(−10⁶) = −39.06, C(−100) = 203.96.
- The roots of C are −2000029.3, −999960.94 and 2.0000747.
- The proof structure of all three results is sound, apart from n2.

### cor:t49-right

- 𝒫(51; κ) is exactly as printed.
- Its derivative has discriminant −5.63·10¹⁹ < 0. The root is 49002580.7016.
- The root of 𝔖(51, ·) is 64667629.125 ∈ (8040·8042, 8041·8043) = (64657680, 64673763).
- κ₀ = 69989955, and hκ₀ = 69.989955 < 70 (8364·8366·10⁻⁶ = 69.973).
- With the last rows of sec:tab-a-pieces (max c = 5155, e_B/h = 29, e_P/h = 72), ι_B > 71.98 and Re ι_P > 54.991.

### prop:t49-six

- The split P = U + h(R₁ + hR₂ + h²R₃) with e = ε₀h holds as an identity in (ι, x, h, ε₀), and the decompositions of
  R₁ᵉ and R₁⁰ are as printed.
- On 𝒥, [−6.954, −1.620] ⊂ [−6.96, −1.6], [3.268, 25.249] ⊂ [3.2, 25.3], and (ι − 2)(3 − ι)(ι + 1) ≤ 0.8794.
- |hW| < 5.6920·10⁻⁵ (sampled maximum 4.81·10⁻⁵).
- Δ₁₃₀(10⁻⁶) = 0.321619, and the 𝒬, U and U(a) bounds hold (6.19·10⁻⁵ and 6.11·10⁻⁵ > 5.7·10⁻⁵).
- h⁻_l, h⁺_l for l = 130, …, 135 are (4.6254, 6.6648)·10⁻⁸, (2.2241, 2.4249)·10⁻⁷, (3.9455, 4.1432)·10⁻⁷,
  (5.6280, 5.8227)·10⁻⁷, (7.2727, 7.4645)·10⁻⁷ and (8.8807, 9.0696)·10⁻⁷. Each lies in its printed window, and the
  windows are disjoint and lie in I.
- Δ_l(h₁) ≤ −0.02186 and Δ_l(10⁻⁶) ≥ 0.035476. h⁻_l > 0 because κ ≥ 17160 > 17092.3.
- Independently, from sign changes of the full discriminant D̃(l(l + 2), h) in exact arithmetic, the double-root
  values are h = 6.5742·10⁻⁸, 2.4164·10⁻⁷, 4.1353·10⁻⁷, 5.8153·10⁻⁷, 7.4575·10⁻⁷ and 9.0632·10⁻⁷, each inside its
  (h⁻_l, h⁺_l).
- The counting and continuity argument is sound.

### prop:t49-vector

- p_(v)(n) = (κ − n² + 2n)(h − h^v_(n,l)), and ∂_ιp_(v) ∈ [−1.0001, −1] on [3, 51].
- h^v_(4,l) = 1/((l + 4)(l − 2)), which is below 10⁻⁶ exactly for l ≥ 1000 (999·1001: 1/999991 > 10⁻⁶).
- 1/1001992 = 9.98012·10⁻⁷ > 9.98·10⁻⁷, and the gap at l = 1000 is 1.99106·10⁻⁹ < 2·10⁻⁹.
- Over 4 ≤ n ≤ 50, the largest h^v_(n,l) below 10⁻⁶ is 32/32000493 = 9.9998459·10⁻⁷, at n = 35, l = 5656,
  κ = 32001648.
- No h^v_(n,l) equals 10⁻⁶.
