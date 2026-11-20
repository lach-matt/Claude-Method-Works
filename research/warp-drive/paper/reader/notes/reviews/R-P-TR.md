# Review R-P-TR: proofs/P-TR.md (md5 fa60e463d8da76fe646853f4315db859, 706 lines)

**Verdict: NOT CONFIRMED — 1 Major, 10 minor, 15 nits.**

The transfer is sound in substance. Every symbolic identity holds, and every printed number checks against an exact
recomputation. The chain from the four inputs to every number of thm:uc-integer is complete, apart from two places
where the file files a step under the wrong heading or wrong label (minor 4–6). There is one real gap: a missing step
in lem:tr-large (c), case b ≥ 56. The missing step is true and closes in one sentence. Without it, the definition of ι_P
and prop:tr-eps (a) rest on an unproved claim.

Chapters changed while I was reading: commit f3e7d724 merged P-K, including sec:uc-data-order in chapter 71 and the
K sentence in chapter 90. Every placement check below was re-run against the chapters as they now stand, at that
commit.

Line numbers refer to P-TR.md.

---

## Major

**M1. lem:tr-large (c), lines 293–295: for b ≥ 56 the root in the disc is not shown to have real part > 19/10.**

Current text:

> Rouché's theorem gives exactly one root in the disc. The disc lies in Im ι > 0, as r < b, and is disjoint from the
> disc of (a), as d − r > 1/100; by symmetry its conjugate holds exactly one root; so, with ι_B(l, h), these are the
> three roots of real part greater than 19/10 ([[prop:np-10-54]] (i)), and the root in the upper disc is ι_P(l, h).

What is wrong:
- prop:np-10-54 (i) says each root has real part either > 19/10 or < −100. To place the root of the disc among the
  three of real part > 19/10, the disc must avoid {Re ι < −100}.
- For b ≤ 56 this holds: Re ι > a − 1/5 ≥ 2.3.
- For b ≥ 56 the radius is b/10, so the disc reaches Re ι = a − b/10. This is below −100 once b > 10(a + 100) ≥ 1025.
- Such b occur in the theorem's range. At h = h₁ and x = 70, 16b² = 24y − (2 + x)² − 16x with y = x/ϖ ≈ 1.44·10⁷,
  so b ≈ 4.6·10³. The lemma itself is stated for every h ∈ (0, 10⁻⁶], where b is unbounded.
- As written, the claim "these are the three roots of real part greater than 19/10" is unproved for those (l, h).
  Three results depend on it:
  - the well-definedness of ι_P in def:tr-exceptional (b) ("ι_P(l, h) is the root of P_l with Re ι > 19/10 and
    Im ι > 0");
  - the conclusion of (c) that ι_B, ι_P and ι̅_P are all the roots of real part > 19/10;
  - through that conclusion, prop:tr-eps (a). There every root with |ι − 1| ≤ 50 must be one of those located.

The claim is true and closes in one line:
- b² ≤ 3y/2 = 3x/(2ϖ) ≤ 105/ϖ = 105e/h.
- So b/10 ≤ (1.05e/h)^(1/2), which is less than 1/(2h) because 4.2eh < 1.
- So the disc lies in {Re ι > a − b/10 > −1/(2h)}.
- prop:s14-scalar-every-h puts the three remote roots in {Re ι < −1/(2h)}.

Replacement, re-wrapped to 121 characters:

> Rouché's theorem gives exactly one root in the disc. The disc lies in Im ι > 0, as r < b, and is disjoint from the
> disc of (a), as d − r > 1/100. It lies in {Re ι > −1/(2h)}: for b ≤ 56, Re ι > a − 1/5 ≥ 2.3; for b ≥ 56, as
> b² ≤ 3y/2 = 3x/(2ϖ) ≤ 105e/h, Re ι > a − b/10 ≥ 5/2 − (1.05e/h)^(1/2) > −1/(2h), since 4.2eh < 1. So, by
> [[prop:s14-scalar-every-h]], its root is not one of the three roots of real part below −1/(2h), and by symmetry its
> conjugate holds exactly one root; so, with ι_B(l, h), these are the three roots of real part at least 2, which are
> those of real part greater than 19/10 ([[prop:np-10-54]] (i)), and the root in the upper disc is ι_P(l, h).

---

## minor

**m1. Printed constants whose leading digits are wrong (lines 23, 70, 505).**
- 13ε_Υ/40 = 13·1.4619·10⁻¹⁰/40 = 4.751175·10⁻¹¹ exactly. It is printed "4.7512…·10⁻¹¹" twice, at lines 23 and 70.
- h_c = 1/1001992 = 9.9801196…·10⁻⁷. It is printed "9.98012…·10⁻⁷" at line 505.
- The edition's "…" means truncation: 1/𝔡₁ = 3000002.583…, z/13680 = 2.92397…·10⁻¹⁰. Under that convention both
  printed values are false.
- No proof uses the decimals. The 0.19 % claim holds either way: 4.76/4.751175 = 1.001857.

Replacements:
- lines 23 and 70: "13ε_Υ/40 = 4.7512…·10⁻¹¹" → "13ε_Υ/40 = 4.751175·10⁻¹¹";
- line 505: "h_c := 1/1001992 = 9.98012…·10⁻⁷" → "h_c := 1/1001992 = 9.98011…·10⁻⁷".

**m2. prop:tr-eps, line 365: the inclusion "(a − 1/5, a + 1/5) ⊂ (2.3, 51.2)" is false.**
- Current text: "[[lem:tr-large]] (c), Re ι ∈ (a − 1/5, a + 1/5) ⊂ (2.3, 51.2), and Re ι lies within ε_Υ of an
  integer only if that integer lies in [3, 51], which h ∉ 𝖩 excludes."
- b ≤ 50.2 does not bound x below 70. For any x ≤ 70, b can be made arbitrarily large by taking h small, and
  b(70, ϖ = 0.1024) ≈ 25.1. So a runs up to 55, and a + 1/5 up to 55.2.
- The conclusion needs Re ι ≤ 51, which comes from |ι − 1| ≤ 50 and is not stated in this clause.
- Replacement: "[[lem:tr-large]] (c), Re ι ∈ (a − 1/5, a + 1/5) with a ≥ 5/2, so Re ι > 2.3, and Re ι ≤ 51 as
  |ι − 1| ≤ 50; so Re ι lies within ε_Υ of an integer only if that integer lies in [3, 51], which h ∉ 𝖩 excludes."

**m3. "Near the points of 𝖩, ε_ind is small and the bound fails" is said more widely than it is true (lines 19, 519;
placement texts 2, 4, 6, 7).**

The ι_P clause of 𝖩 asks only b ≤ 50.2. That is a sufficient condition for |ι_P − 1| ≤ 50, not an equivalent one.
For example, b = 50.1 and Re ι_P = 30 give |ι_P − 1| ≈ 57.8. At such a crossing the entry ι_P − 1 has modulus > 50,
so it does not enter ε_ind(h), and ε_ind(h) does not tend to 0 there. Also, a point of 𝖩 at distance ~ε_Υ/κ from a
crossing has ε_ind ≈ ε_Υ/2 nearby, not "arbitrarily small".

Replacements:
- **Line 519.**
  - Current: "The same argument applies near every point of 𝖩 at which some ι_B, Re ι_P or ι_v equals an integer
    n ∈ [3, 51]."
  - New: "The same argument applies near every point of 𝖩 at which ι_B or ι_v equals an integer n ∈ [3, 51], or Re ι_P
    equals such an n with |ι_P − 1| ≤ 50."
- **Line 19.**
  - Current: "cross the integers, at finitely many values of h for each degree, and near such a value ε_ind(h) tends to 0."
  - New: "cross the integers, at finitely many values of h for each degree, and near such a value, when the root has
    |ι − 1| ≤ 50, ε_ind(h) tends to 0."
- **Text 2.**
  - Current: "and they fail near the excluded values of h"
  - New: "and they fail near the values of h at which such a root crosses an integer"
- **Text 4.**
  - Current: "and near the points of 𝖩 the bound fails ([[prop:tr-fail]])"
  - New: "and near the points of 𝖩 at which a root of P_l or p_(v) with |ι − 1| ≤ 50 crosses an integer the bound fails
    ([[prop:tr-fail]])"
- **Text 6.**
  - Current: "and near the points of 𝖩 the bounds fail"
  - New: "and near the points of 𝖩 at which such a root crosses an integer the bounds fail"
- **Text 7.**
  - Current: "near whose points ε_ind(h) is arbitrarily small"
  - New: "which contains the values of h at which a root of P_l or p_(v) with |ι − 1| ≤ 50 crosses an integer, near each
    of which ε_ind(h) is arbitrarily small"

**m4. Proof of thm:tr-transfer (ii), lines 450–452: two results are filed as "fixed by (γ_Υ, e_Υ)" but use h.**
- thm:is-gap ends: "As μ_G < δ_50 = ε_ind and μ_G < ε_Υ …, every ε_K ∈ (0, μ_G) [is] available for a suitable
  ε_+, and ε_K = 1.6416·10⁻¹⁴ is admissible."
  - ε_ind = δ_50 holds only at h = 10⁻⁶ (cor:s14-eps-ind-point).
  - At h the step needs μ_G < ε_ind. This holds because the proof takes ε_ind ≥ ε_Υ > μ_G, but the file does not
    say so.
- prop:is-ci-pp (b) reads ℰ^ι_ind below 1.5099. At h this is prop:tr-inputs (a), not a gauge fact.
- Replacement for lines 450–452:
  - Current: "[[prop:gap-sums]], [[lem:ec-gauge-gap]], [[prop:is-ind]], [[prop:is-ci-pp]], [[thm:is-gap]], [[thm:is-d0]],
    [[cor:is-flat]] and [[lem:uc-two-offsets]] concern numbers fixed by (γ_Υ, e_Υ)."
  - New: "[[prop:gap-sums]], [[lem:ec-gauge-gap]], [[prop:is-ind]], [[thm:is-d0]], [[cor:is-flat]] and
    [[lem:uc-two-offsets]] concern numbers fixed by (γ_Υ, e_Υ); [[prop:is-ci-pp]] and [[thm:is-gap]] use besides
    ℰ^ι_ind below the real part 1.5099, which by [[prop:tr-inputs]] (a) is that of ℰ_ind with the exponent 1, and
    [[thm:is-gap]] uses μ_G < ε_ind, which holds as ε_ind ≥ ε_Υ > μ_G."

**m5. Line 456: wrong part cited.**
- Current: "ε_ind(h) ≥ ε_Υ ([[prop:tr-eps]] (b))".
- The lower bound is prop:tr-eps (a). Part (b) is the statement for h ≤ 13ε_Υ/40.
- Replacement: "ε_ind(h) ≥ ε_Υ ([[prop:tr-eps]] (a))".

**m6. Line 464: wrong label.**
- Current: "the step of the proof of [[lem:cs-elem]] that uses ε_ind uses ε_ind > ε_K".
- ε_ind appears nowhere in lem:cs-elem or its proof. The step is in the proof of lem:cs-fourier (b), the zf part:
  "those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K", chapter 71 line 4379.
- Replacement: "the step of the proof of [[lem:cs-fourier]] (b) that uses ε_ind uses ε_ind > ε_K".

**m7. prop:tr-fail, line 512: d_acc ≥ 3R at a general h is credited to a theorem stated at the computational point.**
- Current: "so by [[thm:loss-d]] (ii), d_NM ≥ d_acc ≥ 3R > …".
- thm:loss-d (ii) is stated "at the computational point". The fact that the inequality holds at every parameter point
  is proved in the proof of thm:ec-lb-proved.
- Replacement: "so by the argument of [[thm:loss-d]] (ii), which does not use the computational point (proof of
  [[thm:ec-lb-proved]]), d_NM ≥ d_acc ≥ 3R > …".

**m8. The symbol h₁ collides with other uses.**
- P-TR defines h₁ := 4.76·10⁻¹¹ at lines 5 and 28, and it appears again in text 3. P-T49, the companion file on the
  same polynomials, defines h₁ := 5·10⁻¹¹ (its line 8).
- In chapter 71, the newly merged sec:uc-data-order uses (h₀, h₁) for initial data (lines 5019–5020). sec:tr will be
  inserted right after it. The threshold h_0 of h_* = min(10⁻⁶, h_0, h_tf) appears in rem:tr-scope itself.
- Replacement: rename P-TR's constant throughout lines 1–522 and in text 3, for example "h_m := 4.76·10⁻¹¹". Or agree a
  single value and symbol with P-T49.

**m9. Placement texts use notation not defined where they land.**
- Text 2, the opening of chapter 71: 𝖧 appears there for the first time.
- Text 5, chapter 3: there are no occurrences of 𝖧 in chapter 3.
- Text 6, chapter 90: neither 𝖧 nor h_* occurs in chapter 90.
- Text 7, chapter 33: ε_Υ occurs nowhere in chapter 33.

Replacements:
- **Text 2.** "for every h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶)" → "for every h in the set 𝖧 of [[eq:iv4-0-1]] with
  4.76·10⁻¹¹ ≤ h < 10⁻⁶"; and "outside an explicit set" → "outside a set".
- **Text 5.** "for h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶) outside a set of length below 1.7·10⁻¹¹" → "for damping parameters
  h = 1/γ_C ∈ [4.76·10⁻¹¹, 10⁻⁶) of the proved set outside a set of total length below 1.7·10⁻¹¹".
- **Text 6.**
  - "with h ∈ 𝖧 ∩ [4.76·10⁻¹¹, 10⁻⁶)" → "with h in the set 𝖧 of [[eq:iv4-0-1]] and 4.76·10⁻¹¹ ≤ h < 10⁻⁶";
  - "as h_* and the gauge thresholds are not determined" → "as the supremum of 𝖧 and the gauge thresholds are not
    determined".
- **Text 7.** "ε_ind(h) ≥ ε_Υ = 1.4619·10⁻¹⁰" → "ε_ind(h) ≥ 1.4619·10⁻¹⁰, the value of ε_Υ in [[def:uc-choice]],".

**m10. Text 6 (chapter 90) reads ambiguously now that P-K is merged.**
- The paragraph now carries the K sentence between the d/N_NM bounds and the inserted sentence: chapter 90 lines 77–79,
  "… at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The computational point is …".
- "The upper bounds hold with the same numbers" can therefore be read as including the bound for K. thm:tr-transfer does
  not state that bound.
- Replacement: "The upper bounds hold with the same numbers" → "The upper bounds for d and N_NM hold with the same
  numbers".
- Alternatively, add a line to thm:tr-transfer (ii) that K is then at most an integer below 3.45745·10⁵¹ at
  (h, 1/100, 1/100). This follows, as prop:uc-data-order's count holds at every parameter choice, but it should be
  said.

---

## nits

Statement and proof:
1. **Line 5.** "In this chapter h enters through four inputs only" → "In the proof of [[thm:uc-integer]] h enters through
   four inputs only". sec:ec-lb-proved also depends on h.
   - Likewise, line 12: "every other number of the chapter" → "every other number that proof uses".
2. **Lines 10–11.** lem:ec-theta-in-zero needs γ_Υ{1, 2, 1 − e_Υ} and (1 + v_C)γ_C{1, 2, 1 − e_C} disjoint, which holds
   for γ_C ≥ 10⁶, not "for every γ_C". Replace "and so do [[lem:ec-theta-in-zero]]" by "and so does
   [[lem:ec-theta-in-zero]] at every γ_C = 1/h ≥ 10⁶, the two sets of that lemma being disjoint, and so do".
3. **Line 23.** "no h satisfies the hypothesis" → "no h satisfies (H_ε) ([[prop:tr-eps]] (b))". The hypothesis
   h ≥ h₁ makes the original wording trivial.
4. **Line 34.** "except the root 2 of P_0 and of P_1" → "except the root 2 of P_1". The list names C, and 2 is not a
   root of C.
5. **Lines 41–43.** Make the domain explicit: "for which there are l and an integer n with 3 ≤ n ≤ 51 such that" →
   "for which there are l and an integer n with 3 ≤ n ≤ 51 such that ι_B(l, h), resp. ι_P(l, h), is defined (x ≤ 70)
   and".
6. **Line 63.** "whether or not h ∉ 𝖩 and h ≥ h₁" → "whether or not h ∈ 𝖩 and whether or not h ≥ h₁".
7. **Line 137.** "For an integer n ≥ 4, ι_v(l, h) = n exactly when h = …" → "For an integer n ≥ 4 with n < l + 2,
   ι_v(l, h) = n exactly when h = …". For n ≥ l + 2 there is no positive solution.
8. **Line 156.** "are real, simple and lie in (2, 3)" → "are real, simple and lie in [2, 3), the root 2 occurring only
   at l = 1".
9. **Lines 206–207, (a).** The proof gives one root in |s| < x/2 and one in |s| < 1/100. That they coincide follows
   because one disc contains the other, but it is not said. Add after "≥ 0.3885" (line 225): "; as one of the two discs
   |s| < x/2 and |s| < 1/100 contains the other, they hold the same root".
10. **Line 280, box [1/2, 5] × [20, 40].**
    - ϖ̄ is printed 0.0188. With 0.0188, N = 6.6505 > 6.644.
    - With the defined value 3x_b/(2b_a²) = 0.01875, N = 6.6425 < 6.644, so the printed N is correct.
    - Print "0.01875" in place of "0.0188".
11. **Line 323.** "evaluating 𝒬 from below at the left end and A, B from above at the right end" → "… and A, B from
    above, with the majorants at the right end and the factor 1/x of 10⁻⁶F̄^ϖ/x at the left end".
    - The printed A values (0.04152, …, 5.997) are exactly those with 1/x_a. With 1/x_b they would be smaller.
12. **Lines 467–468.** "which use only ε_K < ε_Υ < 1.46214·10⁻¹⁰ and ε_ind(h) ≤ δ_50" → "which use only
    ε_K < 1.6417·10⁻¹⁴ ((G) for the index sets as constructed), ε_Υ < 1.46214·10⁻¹⁰ and ε_ind(h) ≤ δ_50".
13. **Line 520.** "ε_g ≤ ε_ind(h) < 40h/13 < ε_Υ" → "ε_g ≤ ε_ind(h) < 40h/13 ≤ ε_Υ". Equality holds at
    h = 13ε_Υ/40.

Placement and crosswalk:

14. **Stale line references in the placement items.**
    - Line numbers now:
      - text 3 is at chapter 71 lines 69–71, not 66–68;
      - text 4 at 1798–1800, not 1795–1797;
      - text 5 at chapter 3 lines 361–363, not 354–356;
      - text 6 at chapter 90 line 80, not 78.
    - The parenthetical of item 6, "an item that inserts the order of the approximant after line 76 leaves this line as
      it is", is stale: that item (P-K text 8) is merged.
    - Item 1's "(after the section sec:uc-data-order, if that section has been inserted before it)" can now read "after
      the section sec:uc-data-order".
15. **Crosswalk row 2 note.** "𝖩 collects the h at which ι_B, Re ι_P or ι_v is within ε_Υ of an integer n ∈ [3, 51]"
    → "… ι_B, Re ι_P (with b ≤ 50.2) or ι_v (n ≥ 4) is within ε_Υ of an integer n ∈ [3, 51]".

---

## Placement and crosswalk checks

- Each Old text (items 2–7) occurs exactly once in the current chapters, at commit f3e7d724: chapter 71 lines 26–28,
  69–71 and 1798–1800; chapter 3 lines 361–363; chapter 90 line 80; chapter 33 lines 3536–3540.
- Item 6 does not overlap P-K's item 8, which is now merged at chapter 90 lines 76–79. The two edits compose; see m10
  for the reading of the result.
- Item 7 (chapter 33) still matches its Old text. See m3 and m9 for its New text.
- The section was simulated in place, inserted before sec:ec-linear and after sec:uc-data-order. With labels resolved by
  the edition's assembler:
  - no undefined reference;
  - none of the 23 tr- labels is defined elsewhere;
  - the longest resolved line is ≤ 121 characters. In the simulation sec:tr is Section 49.15, thm:tr-transfer is
    Theorem 49.123 and eq:tr-split is (49.64).
- The New texts of items 2–7 were applied in a simulation and resolved: every line is ≤ 121 characters, and no
  reference is undefined.
- The raw file has at most 121 characters per line. No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or
  "|"; the only "|" lines are the two tables. All labels are lowercase.
- The style lint flags only two things: the crosswalk rows, whose file locations follow the P-K and P-LB convention,
  and the references to labels in other files.

## Consistency with P-T49

- Same polynomials and conventions:
  - p_(v)(ι) = −hι² + (2h − 1)ι + hκ + 3;
  - P-TR's crossing h = (n − 3)/((l + 1)² − (n − 1)²) equals P-T49's h^v_(n,l) = (n − 3)/(κ − n² + 2n);
  - P-TR's h_c = 1/1001992 is P-T49's h^v_(4,1000), "the largest of these values".
- P-TR's slope bound ∂_hι_v ≤ (l + 1)² is the cruder form of P-T49's prop:t49-vector (b), and the two agree.
- prop:t49-vector (c): ε_ind has no positive lower bound on any subinterval of length 2·10⁻⁹ with 𝖹 removed. This agrees
  with P-TR: 𝖩 has small measure but meets every such subinterval.
- P-T49's rem:t49-count (v) counts about 6.3·10⁷ ι_B and vector crossings in [5·10⁻¹¹, 10⁻⁶], plus the ι_P crossings.
  This fits the writer's "about 10⁸ crossings".
- The only clash is the symbol h₁ (m8).

## What I recomputed and found correct

Method:
- sympy for exact identities.
- Exact rationals for every majorant, with ϖ → 0.1024 or the stated ϖ̄, h → 10⁻⁶ and e → 1/102400.
- mpmath at 40 digits for the sums.
- Scripts are in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rptr/.

lem:tr-split:
- P_l = det(hN_l) at v = 1/2 equals U + eF, with h = eϖ and κ = x/h, identically in (ι, x, ϖ, e).
- eq:tr-dh holds identically. The 1/ϖ terms cancel as stated.
- 𝒬 = 2(ι − a)² − Δ/8.
- 𝒬(2 + x + s) = 3(1 − ϖ)y + (x − 2)s + 2s².
- F(2 + x) = −x g_B, with g_B as printed.
- F₁(a + s) = Σ A_j s^j, with A₀–A₄ as printed.
- F₂(2, x, ϖ) = −3x(1 + ϖ).
- F(2) = −x(9 − x − 3ϖ + 2ϖx + 3h + 3ϖh).
- U(2 + y), F₁(2 + y)/y, U(3 − y/2) and F₁(3 − y/2) all match their printed closed forms.

lem:tr-c-v:
- C₀ and C_h at 2 + 7·10⁻⁵ and at 5/2.
- The closed form, monotonicity, MVT bound, integer crossings and slope eq:tr-vslope of ι_v.
- ι_v(2, h) − 3 ≥ 5h/(1 + 6h).

lem:tr-small:

| quantity | computed | printed |
|---|---|---|
| positive terms of F₁(2 + y)/y | 1.65140 | ≤ 1.652 |
| majorant of (F₂ + hF₃)(2 + y)/y | 15.7979 | ≤ 15.8 |
| Ā₀(0.01536, 0.1024) | 4.83119 | ≤ 4.832 |
| h- and h²-terms at a | 0.000884 | ≤ 0.0009 |
| U(a) | — | ≥ 0.0248 |
| U(3 − y/2) | — | ≤ −1.4466y |
| y-coefficient in the bound for F₁(3 − y/2) | 13.8819 | ≤ 13.89 |
| h- and h²-terms at 3 − y/2 | 0.0015973 | < 0.0016 |
| \|F(2)\| ≤ c·x, c | 9.32571 | 9.326 |
| \|∂_ιF\| on [2, 2 + 3.1h] | 15.6318 | ≤ 15.64 |
| polynomial at κ = 15 | 310.563 | 310.56… |

lem:tr-large (a):
- The constants 0.40392 and 26.296875.
- The root distances 0.449 and 0.27: x ≤ 0.01866 and Δ ≤ 0.774.
- The x/2 circle: |𝒬| ≥ 0.38856, ḡ_B(1/2) = 30.1340, F̄_ι(11/4, 1/2)/2 = 222.681, so e|F| ≤ 0.002469x < 0.194x.
- All 6 x-pieces. Each printed ḡ_B, F̄_ι, upper and lower entry is a valid outward rounding of the exact values, and the
  upper entry is below the lower one in every row. The tightest piece is [55, 70]: 11.814 < 14.4565.

lem:tr-large (b):
- Δ ∈ [−0.8, 0.7075] under x ≤ 0.1024y.
- Ā₀, …, Ā₄ = 4.9525, 1.72632, 18.6941, 6.75548, 0.512.
- |F| ≤ 9.08098, so e|F| = 8.87·10⁻⁵ < |U| ≥ 0.0058114.

lem:tr-large (c):
- b ≥ 0.1561, and b ≥ 2.5364, 8.0734, 15.5794, 21.8202 for x ≥ 1/2, 5, 20, 45.
- All 23 boxes: with ϖ̄ as defined, every N ≤ printed N, every D ≥ printed D, and N < D (display nit 10 aside).
- The b ≥ 56 bound: the largest power of b is 3, and the coefficient after b^k → b³56^(k−3) is 68.7665 ≤ 68.77.
- The condition d − r > 1/100 and the final b > 50.2 step.

lem:tr-large (d):
- c₀ = 4,646,945.96, c₁ = 141,542.62, c₂ = 882.5664, all below the printed bounds.
- e(c₀/4900 + c₁/70 + c₂) = 0.037627 < 0.0377.
- 0.001959x³ ≤ |U| for x ≥ 70.

lem:tr-slopes (a):
- The derivative formula.
- On each of the six intervals, 𝒬, A and B are reproduced to the printed digits, using 1/x_a for the F̄^ϖ term (nit 11).
- Quotients 0.99756, 0.99677, 0.99643, 0.99326, 0.98802, 0.98466; all ≥ 0.98.

lem:tr-slopes (b):
- The expansions of ∂_hP_l/κ and ∂_ιP_l about ζ.
- Re(−A₂c₀/(4ibA₂)) = 3/4.
- The deviation bound, with all 13 dev entries recomputed. My bound is smaller than the printed one in every box
  (largest 0.2096 against the printed 0.2923).

lem:tr-slopes (c):
- 0.99κ holds for κ ≥ 252,500, so it holds for l ≥ 999.

prop:tr-eps:
- (40/13)h₁(1 − 5·10⁴h₁) = 1.46461·10⁻¹⁰ > ε_Υ.
- 3.1h₁ = 1.4756·10⁻¹⁰.
- 5h₁/(1 + 6h₁) > 4.99h₁.
- 7687h and 10240h.
- The degree ranges: l = 122/123 ↔ y = 3/20, and l = 142/143 ↔ y = 1/5.

prop:tr-measure:
- The interval structure of 𝖩_B, 𝖩_P and 𝖩_v, and the slopes used. The x_n windows avoid the jump of ϱ at 20.
- The least degrees: 993.94 → 994, 631.38 → 631, 999.
- Factors 1.001006, 1.001584, 1.001001, all ≤ 1.0011 or 1.0016.
- Integral bounds 13.01377, 12.67020, 12.85641.
- Coefficients 0.0265884, 0.0634564, 0.0260023; sum 0.11606 < 0.1161.
- 0.1161ε_Υ = 1.69727·10⁻¹¹ < 1.698·10⁻¹¹, and 1.698·10⁻¹¹/(10⁻⁶ − h₁) = 1.69808·10⁻⁵ < 1.7·10⁻⁵.
- κ ≤ 70/h₁ in each case, so only finitely many l occur.

prop:tr-fail:
- 3(1 − 2.1·10⁻⁸)/(1.38·10⁻²⁵)² = 1.575299·10⁵⁰ > 1.5752·10⁵⁰ > D_acc. The exact threshold is ε < 1.38164·10⁻²⁵.
- h_c gives ι_v(1000, h_c) = 4, and h_c ∈ 𝖩_v(1000, 4).
- 1002001·1.377·10⁻³¹ = 1.37976·10⁻²⁵ < 1.38·10⁻²⁵.
- The hypotheses of lem:ec-lb-rounds with Θ_g = ε_ind(h) and Θ_η = δ̄.

h₁ and the 0.19 % claim:
- 13ε_Υ/40 = 4.751175·10⁻¹¹ and h₁/(13ε_Υ/40) = 1.001857.
- Remark after prop:tr-fail: 0.3168h⁻² > D_acc for h ≤ 4.4898·10⁻²⁶.

The chain in thm:tr-transfer (ii). I traced every step of thm:uc-integer, prop:uc-d-small and sec:cs for h-dependence:
- **Input (a), ε_ind.** It enters only through:
  - ε_g and eq:iii-i9-1-1 (lem:uc-admissible);
  - prop:ec-rounds, through ε_ind ≤ δ_50;
  - lem:cs-fourier (b), through ε_ind > ε_K;
  - thm:is-gap's last sentence (m4).
- **Window counts.** W, T_2 and I_lev use 𝔡₁ and 0.999ε_Υ, and are unchanged once lem:uc-gaps holds at h, which it does
  by prop:tr-inputs (a).
- **Λ ∩ {Re < 3 + ε_+}, N_Λ, k̄_0, J_*.** These see ℰ^ι_ind only below 1.5099, where the h-dependent exponents (> 3) do
  not enter.
- **ι⁺ losses.** d^max_ι ≤ 12 and l′ = 30 are bounds over a strip and do not depend on where the poles are. The poles
  enter only through their orders (≤ 1): l_* = 50, K_ι ≤ 2, m_ι ≤ 1.
- **Visibility.** The upper bound on the pole order of N_ι⁺⁻¹ is the last sentence of the proof of prop:sp-visible,
  valid without its hypothesis. So no bound needs lem:sp-exceptional at h.
- **γ_C directly.** It enters only through ϑ_L < 2 and the disjointness in lem:ec-theta-in-zero, both of which hold for
  γ_C ≥ 10⁶.
- **The lower bounds.** They use only the gauge (cor:uc-two-offsets, prop:ec-rounds), so the closing claim of
  thm:tr-transfer is right.
- I found no use of h = 10⁻⁶ beyond those listed above.

prop:tr-inputs:
- (a): the bound 3 and the general bound 50 of prop:is-logs (c). The file correctly drops is-logs' refinement to
  order 1, which needs distance > 1.34·10⁻⁶ from ℤ.
- (b): the coincidence analysis with the □^Υ entries in (1, 5]: l + 2 + d₂ for l ≤ 2 and l + 3 + d₁ for l = 1, plus
  3 + 𝔡₀ at s0. Simplicity follows from h ∉ 𝖹₁.
- (c): the 𝒮_τ lists and the integer differences, and the conditions of lem:sp-two-roots (c).
- (d): cor:sp-lstar (a)–(c).

Honesty of the statement. rem:tr-scope states that the hypothesis may be empty, through h_* ≤ h₁ or the gauge, and
the placement texts all carry this condition. "h ∉ 𝖩" is decidable in principle. For a given h it is finitely many
root-location questions for explicit polynomials:
- ι_B and ι_P for the l with hκ ≤ 70;
- ι_v for the l with ι_v ≤ 51 + ε_Υ.

𝖩 is a superset of the set where (H_ε) fails, because of the b ≤ 50.2 proxy. That is harmless for the theorem, but it
is behind m3.

A remark on the writer's report, not on the file: the report says 701 lines; the file has 706.
