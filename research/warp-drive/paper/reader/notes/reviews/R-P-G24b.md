# R-P-G24b: independent reading of proofs/P-G24b.md

File read: `research/warp-drive/paper/reader/proofs/P-G24b.md`, md5 ad4e510f643b517a2513528c1da18acc, 1,559 lines.
The writer's report (`notes/reports/P-G24b.md`), the base chapter, chapters 20, 22 and 95 (Appendix A), proofs/P-G1.md
and the preprint text were read as needed. Nothing under method/, drive/, extracted/ or recovered/ was read. No chapter,
crosswalk or proof file was edited.

**Verdict: NOT CONFIRMED.** The new proofs are correct in substance: lem:iv5-2-symbols, lem:iv5-6-transport,
lem:iv5-6-core (both λ_* and C_* check out), the new proof of prop:iv5-6-1, thm:iv5-7-3 (b) through Appendix A's BGP
results, and def:iv6-0-2 with every use of it. The reported finding is right. Every old text still occurs exactly once,
also at the current HEAD. But there are 4 minor issues and 12 nits, and the relative-index step stays unproved. That
step is listed as Major below. The author flags it themselves, so it is an open item and not an error in the texts.

## Judgment of the finding (prop:iv5-6-1 (1), second estimate)

**The finding is correct.** Without a support condition at Σ^♯, the second estimate of prop:iv5-6-1 (1) is false.
Here is why.

- Σ^♯ is a final hypersurface for {r ≥ r_♯}: dr is future timelike on [½r_♯, r̂] (lem:iv5-0-3 (c)).
- So a solution of the backward problem for P_h* can take its data on Σ^♯.
- Such a solution can vanish on τ⁻¹([T_0/2, T_0]) and still be nonzero on τ⁻¹([0, T_0/2]).

The section 3.2 counterexample has the right idea, but two of its steps are not justified as written (finding m4).
Below is a version that I checked step by step.

1. Fix h ∈ (0, 1] and t_1 ∈ (0, ½T_0r_♯). Take p ∈ Σ^♯ with 0 < t(p) < t_1, so 0 < τ(p) < T_0/2.
2. Let F be a smoothed maximum of t − t_1 and r_♯ − r, with dF a convex combination of dt and −dr. Put
   S₀ := {F = 0} ∩ {r > ½r_♯}.
   - Both differentials are past timelike on {½r_♯ ≤ r ≤ r̂}, by lem:iv5-0-3 (a) and (c), so S₀ is spacelike.
   - S₀ coincides with Σ^♯ near p.
   - S₀ is acausal. After a future causal curve leaves S₀, either t > t_1 or r < r_♯, and r keeps decreasing inside
     {r ≤ r̂}. So F > 0 from then on.
3. Every inextendible causal curve through a point of {r ≥ r_♯} meets S₀. If F < 0 at the point, the future part of the
   curve reaches F = 0 while r > ½r_♯. If F > 0, the past part does.
   - So {r ≥ r_♯} lies in D(S₀).
   - By thm:std-bgp-development and thm:std-bgp-cauchy (5) there is a smooth ω on D(S₀) with P_h*ω = 0, whose Cauchy
     data on S₀ are supported in a small neighbourhood K of p in S₀ ∩ Σ^♯, and with ω(p) ≠ 0.
     P_h* is normally hyperbolic up to the factor h².
4. supp ω ⊂ J(K).
   - Future causal curves from K enter {r < r_♯} and stay there.
   - Past causal curves from K have t < t_1 < ½T_0r_♯ ≤ ½T_0r on {r ≥ r_♯}, so τ < T_0/2 there.
   - So on M^♭, ω vanishes on τ⁻¹([T_0/2, T_0]).
5. Multiply ω by a cut-off in t that equals 1 on {t ≥ 0} and 0 on {t ≤ −1}. The product:
   - has compact support in M^♭, so it lies in ρ_sf^(−α_sf−2)H²_(3b,h);
   - satisfies P_h* = 0 on τ⁻¹([0, T_0]) and vanishes on τ⁻¹([T_0/2, T_0]);
   - is nonzero near p.
   So the left side of the estimate is positive and the right side is 0, for every h.

**T19 fixes it.** The new proof (T20, "The second estimate of (1)") proves the estimate for ω smooth with compact
support in {r > r_♯}. These are dense among the ω supported at Σ^♯, and both sides of the estimate are continuous in
ρ_sf^(−α_sf−2)H²_(3b,h). I checked every step of that proof (below).

**The uses satisfy the condition.**
- prop:iv5-7-2 (x) applies the estimate to ω′ ∈ H(Ω)^(−,•), which is supported at Σ^♯.
- The extension and restriction for s′ > 1 ("as in prop:iv5-7-1") runs step (x) again on Ω̃. There ω̃′ lies in
  Ω̃^(−,•) and is supported at {r = ¾r_♯}. The new proof works with ¾r_♯ in place of r_♯, since N = {r > ½r_♯} and
  lem:iv5-0-3 (b), (c) hold there.
- thm:iv6-2-1 uses the analogue on M, eq:iv6-2-e2. It has no inner boundary, and compactly supported sections in
  ℝ_t × (ℝ⁴ ∖ 0) are dense, so it needs no condition.
- I found no other use. A grep of all chapters shows that prop:iv5-6-1 and "(5.67)" occur only in chapter 33.
- Chapter 62 cites lem:iv5-0-5, but only condition (6) off 𝗌𝖿, which T3 does not affect.

## Findings

### Major

**M1 (open item, flagged by the author; not an error in the texts). Lines 1409–1432, §6.1: the relative-index step of
prop:iv6-1-1, index 0, steps (i) and (iii).**
- The step applies thm:std-relative-index (Mel93, Thm 6.5), which is stated for a b-elliptic operator on a compact
  b-manifold, to an operator that is a scattering operator with radial sets at r = ∞.
- With P-G24b merged, the chapter therefore still contains a step that is not proved.
- The four-step sketch is sound. Step 4 follows from closed range and the density of 𝒴_β in 𝒴_(β₁).
- The "multiplicity count" may be less work than §6.1 suggests. Melrose's rank_j(z) at a root z of a sector's regular
  matrix indicial polynomial equals the order of vanishing of its determinant at z, since it is the sum of the partial
  multiplicities (Smith form). The determinants are the polynomials P_l and p_(v) of prop:np-10-12, and lem:iv4-1-3 (a)
  already counts their roots with real part ≥ 2 with multiplicity.
- So the lemma would need: (α) the localisation argument of §6.1 at r = 0, with formal solutions to enough orders that
  Pu ∈ 𝒴_β; (β) the identity rank = order of the zero of the determinant.
- Suggested replacement: add this lemma before prop:iv6-1-1 and cite it in place of "[Mel93, Theorem 6.5] … ([Hin26a,
  p. 91])" at chapter lines 2409–2410. The classification (c) and the coordinator note stay as they are.

### minor

**m1. Lines 332–336 (T4, the cut-off convention), with consequences at lines 45–47, 376, 509–510, 565–566, 606–607 and
432–433.**

Current text:

    *Commutants near o.* A *cut-off* below is a smooth function χ of one variable with values in [0, 1], equal to 1 on a
    closed interval J and to 0 outside a larger open interval, non-decreasing to the left of J and non-increasing to its
    right, such that (χχ′)^(1/2) is smooth to the left of J and (−χχ′)^(1/2) to its right. Such cut-offs exist: with
    φ(x) := e^(−1/x) for x > 0 and φ(x) := 0 for x ≤ 0, the function χ(x) := φ(β − x)/(φ(β − x) + φ(x − α)), α < β, is
    equal to 1 on (−∞, α] and to 0 on [β, ∞), and near α and near β the function −χχ′ is the square of a smooth positive

What is wrong. The definition does not ask a cut-off to be positive on the larger interval. So "equal to 1 on J,
supported in I" allows χ to vanish on part of I ∖ J. Several proofs need b_0 to be elliptic on WF′(B_0) at small
frequency at points where χ < 1 and no a priori operator E is available:

- prop:iv5-2-1 (2) (T5): ρ_K ≤ 2δ needs χ_K > 0 on [0, 2], but χ_K is only 1 on [0, 1].
- prop:iv5-3-1 (1) (T8): ρ_K ≤ (3/2)δ_r needs χ_K > 0 on ((5/4)δ_r, (3/2)δ_r]. Making b_0 elliptic there is the stated
  purpose of T8, at lines 45–47, and the wording does not achieve it.
- prop:iv5-3-1 (2): ρ_sf ≤ (3/2)δ needs χ_sf > 0 on ((5/4), (3/2)].
- prop:iv5-4-1 (2) (T11, which has no E): χ_sf > 0 on [0, 3/2] and χ_R > 0 on [−(3/2)δ_sf, (3/2)δ_sf].
- prop:iv5-5-1 (2) (T13): χ_K > 0 on [0, t_2⁻¹], where T13 takes χ_K = 1 only on [0, t_3⁻¹]. The preprint takes it
  equal to 1 near [0, t_2⁻¹].
- The last sentence of T41 asserts the ellipticity in all of these cases.

The explicit construction is positive on (−∞, β), so one change to the definition repairs every case.

Replacement for lines 332–336, all lines ≤ 121 characters; line 337 then follows unchanged:

    *Commutants near o.* A *cut-off* below is a smooth function χ of one variable with values in [0, 1], equal to 1 on a
    closed interval J, positive on a larger interval I that is open in the range of the variable, and 0 outside I,
    non-decreasing to the left of J and non-increasing to its right, such that (χχ′)^(1/2) is smooth to the left of J and
    (−χχ′)^(1/2) to its right; "supported in I" refers to this I. Such cut-offs exist: with φ(x) := e^(−1/x) for x > 0
    and φ(x) := 0 for x ≤ 0, the function χ(x) := φ(β − x)/(φ(β − x) + φ(x − α)), α < β, is equal to 1 on (−∞, α],
    positive on (−∞, β) and 0 on [β, ∞), and near α and near β the function −χχ′ is the square of a smooth positive

T5, T8, T11 and T13 can then stay as they are. At lines 45–47, add "and positive there (section 5, the convention of
T4)" after "[0, 2δ_r)". Also note in §1 that T8 widens χ_sf from [0, 3/2) to [0, 2), and that T11 inherits this.

**m2. Lines 1042–1044 (T24) and 1129, 1133–1136 (T27): the strong sense is overclaimed.**

Current text, line 1042: `(for s_1 < −s + 2, ℓ_1 < −ℓ − 1 and β_1 < −β + 2, in the strong sense, the adjoint being
taken for the L² pairing of`. Line 1129 ends `This gives, for every M, in the strong sense,`.

What is wrong.
- Strong forms of the boundary-face estimates hold only with a priori orders that are above threshold (rem:i-a-7-3).
  - For eq:iv6-1-4, whose error term is in H^(−M,(−M,−M)), the a priori order at R_in is below the R_in threshold, so
    the strong form fails.
  - Chapter 22's eq:i-c-4-3, which T27 reruns, is stated only for w ∈ 𝒳_(tf,θ).
- For the dual estimate, prop:i-a-4-9 (2) needs an a priori order −𝗋₀ − 1 with 𝗋₀ below the R_out threshold. So in
  eq:iv6-1-3, ℓ_1 must satisfy ℓ_1 > −½ − h⁻¹(1 − e)(1 − v) near R_out.
- The later uses are unaffected. The independence of the annihilator from the orders uses only an admissible a priori
  order.

Replacement for lines 1042–1044:

    (for s_1 < −s + 2, β_1 < −β + 2 and ℓ_1 < −ℓ − 1 with ℓ_1 > −½ − h⁻¹(1 − e)(1 − v) near R_out, in the strong sense,
    the adjoint being taken for the L² pairing of these spaces; [Hin26a, (B.28)]) hold uniformly for σ in e^(i[0,π−δ]) near
    1 and in e^(i[δ,π]) near −1, for fixed orders admissible on that set ([[def:iv6-0-2]]).

Replacement for the end of line 1129 and the line after the display:

    part in (−2, 100], and β − 2 ∈ (−2, C_0] is not the real part of a root. This gives, for every M and every ω in the
    domain of [[eq:iv6-1-1]],

    ([Hin26a, (B.19)–(B.20)]), which implies [[eq:iv6-1-2]]; its strong sense is that of the pieces ([[rem:i-a-7-3]]) and
    of [[lem:i-c-2-5]]. The adjoint chain of the same proof (the estimates (2) of

At the end of line 1136, replace `‖ω‖_(H^(−M,(−M,−M))_(sc,b)), which is smaller.` with:

    ‖ω‖_(H^(−M,(−M,−M))_(sc,b)), which is smaller, for ω in the domain, and in the strong sense with the a priori orders of
    [[eq:iv6-1-3]] ([[rem:i-a-7-3]]).

**m3. Lines 1259–1260 (T33) and 1307 (T35), with §6.3 at lines 1441–1444: the cone-face cut-off does not match item (a)
and the combination.**

Current text: `…, with χ_cf a cut-off equal to 1 on [0, 1] and` / `supported in [0, 3), and χ₁ := χ_(τ,0) of
[[sec:iv5-1]] at T. By`. T35: `(a) The forward and backward cone estimates hold on {ρ_cf ≤ 4δ_r} ∩ {τ ≥ T/40},
globally in t, with a priori sets in`.

What is wrong.

1. With χ_cf(𝔛ρ_cf), equal to 1 on [0, 1] and supported in [0, 3), the backward cone estimate has its a priori set in
   {𝔛⁻¹ ≤ ρ_cf ≤ 3𝔛⁻¹}. Item (a) says that set is {(5/2)δ_r ≤ ρ_cf ≤ 4δ_r}, a ratio of 8/5 against 3. Two
   requirements then conflict:
   - b_0 is positive only on {ρ_cf ≤ 4δ_r}, so the commutant needs 3𝔛⁻¹ ≤ 4δ_r;
   - the adjoint combination covers that set by (c) (2), which reaches only {ρ_cf ≥ 2δ_r}, so it needs 𝔛⁻¹ ≥ 2δ_r.

   No 𝔛 meets both. T33 makes the preprint's cut-off explicit, and that brings out a mismatch the citation used to hide.
2. T35 keeps the claim that the backward estimate holds on {τ ≥ T/40}. With χ̃ := χ_(τ,2) (T37), b_0 vanishes for
   τ ≤ (2.25/10)T. §6.3 acknowledges this and leaves it standing. The combination uses the backward estimate only for
   τ ≥ T/2, so a correct statement costs nothing.

Replacement for T33's first two new lines:

    a = w⁻¹χ_cf(𝔛ρ_cf)χ_0(𝔛|ζ|)χ₁(t/r), w := ρ_sf^(α_sf+1)ρ_cf^(α_cf−1), with 𝔛 := δ_r⁻¹, χ_cf a cut-off equal to 1 on
    [0, 5/2] and supported in [0, 4), and χ₁ := χ_(τ,0) of [[sec:iv5-1]] at T, δ_r being fixed below so small that 𝔛 is
    large enough. By

Replacement for T35's new line, two lines; the old line 2497 then follows unchanged:

    (a) The forward cone estimate holds on {ρ_cf < 4δ_r} ∩ {τ ≥ T/40} and the backward one on
    {ρ_cf < 4δ_r} ∩ {τ ≥ (2.75/10)T}, globally in t, with a priori sets in

A new placement text is also needed, at chapter line 2494 (2495 at HEAD), which no text touches. The old line is:

    the dilations), and that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}. Then:

Its replacement:

    the dilations), that (6) holds on 𝗌𝖿 ∩ {s ∈ [δ_r, v(1 − δ_sf)]}, and that 𝔛 = δ_r⁻¹ is as large as the cone-face
    symbols need. Then:

With these changes the forward estimate controls ρ_cf < 4δ_r, which covers (c) (1)'s a priori set
{δ_r ≤ ρ_cf ≤ 2δ_r} and s ∈ [2δ_r, 3δ_r] near 𝗌𝖿. The backward estimate's a priori set
{(5/2)δ_r ≤ ρ_cf ≤ 4δ_r} lies in the reach of (c) (2). Delete the first bullet of §6.3.

**m4. Lines 148–157 (§3.2, the counterexample; it is a coordinator note, but it is the evidence that goes to the
author).**

Two steps fail as written.
- Step 2 says ω "is a solution of the Cauchy problem on ℝ_t × {r > ½r_♯}". The backward problem from {t = t_1} is not
  posed on all of that set, because future causal curves can leave through r = ½r_♯ before t = t_1.
- Step 5 says "Choose f so that the past light cone of q carries ω across Σ^♯. Then ω ≠ 0 on τ⁻¹([0, T_0/2]) ∩
  {r ≥ r_♯}". Nothing shows that ω is nonzero there. For a smooth source behind Σ^♯ this would need unique continuation
  or propagation of singularities.

Replacement: the five-step construction in the judgment above, with data on the spacelike hypersurface S₀ that
coincides with Σ^♯ near p.

### nit

**n1. Lines 4–7, 61, 224 and the line numbers throughout: the base has moved.**
- HEAD changed during this reading. Chapter 33 is now md5 9571426c902bea231329690543c17455 (commit b238c1fd, the P-T49
  merge). One line was inserted at line 113 and a section was appended at line 3537.
- I re-ran the placement check at HEAD. All 43 old texts occur exactly once, none overlap, and variant A still
  applies.
- Line numbers from 113 on are now one higher.
- HEAD has 248 bracketed citations. The new one is [Hin26, (8.13)] at line 3580, class (b).
- The crosswalk at HEAD has 216 rows. With the 16 new rows inserted it matches the chapter's label order.

Replacement for "md5 007858d84d3f7b2ba03c0c84d0338749": "md5 007858d84d3f7b2ba03c0c84d0338749 (at HEAD, after the P-T49
merge, 9571426c902bea231329690543c17455: the old texts are unchanged, and line numbers from 113 on are one higher)".

**n2. Line 113: the classification table misses chapter line 2107.** That line has [Hin26a, (5.18)] ("the bound
[Hin26a, (5.18)]"), class (b). Replacement for the row's first cell: `| 1977–2089, 2107 |`.

**n3. Line 288 (T42).** Current text: `Let Λ⁻ be a microlocal parametrix of Λ near supp a. By [Hin26a, (5.25)], (5.26) and
the split of the`. For |⟨AP_hω, Aω⟩| ≤ (4c_0)⁻¹‖Λ⁻AP_hω‖² + c_0‖ΛAω‖², Λ⁻ must be a parametrix of Λ*. Also, "(5.26)"
appears without its citation. Replacement:

    *Conclusion.* Let Λ⁻ be a microlocal parametrix of Λ* near supp a. By [Hin26a, (5.25)–(5.26)] and the split of the

**n4. Lines 415 and 432–433 (T41, and the same lines in variant A).**
- B_0 and E denote two different operators in one proof: the quantisations of b_0 and e, and the operators of the
  statement.
- Two routine steps from eq:iv5-2-iter to the statement are not written out.

Replacement for lines 432–433, with the same change at lines 464–465:

    wave front set of the B_0 of the statement, b_0 is elliptic where the fibre variable has length at most 𝔛⁻¹, and
    [[prop:iv5-1-2]] applies where it has length at least 𝔛⁻¹. The quantisation of e is bounded by the E of the statement,
    whose elliptic set contains supp e, and B̃_0𝓛_hω by B_1P_hω, B̃_0 being microsupported in Ell(B_1), each up to
    h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h)). This gives [Hin26a, (5.33)], with δ := 𝔛⁻¹.

**n5. Lines 436–437 and 1481–1483 (merge order with P-G1).** If T41 is merged first, C33-11's old text no longer exists,
because it contains T41's old sentence. Replacement for lines 1482–1483: "T41 is therefore given in two variants. Merge
C33-11 first and then use variant A. If T41 is merged on the current text, C33-11 must end before its last paragraph,
and that paragraph's first clause must be put into T41's first sentence." That clause is "the coefficient of ‖Aω‖² is
at most −c_0 + (9C₂ + 2)𝔛⁻² + C′_𝔛h, with C₂ independent of 𝔛".

**n6. T20, lines 909–910, 921 and 935–936: the 𝔛 thresholds are given as "𝔛 large".** The paper's rule is explicit
constants, and the first estimate already gives its threshold. Replacements:
- Lines 909–910: `… with κ = ⅛ and λ := ¾𝔛r_♯, for` / `𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ), (4/3)λ_*). There
  w²r⁻⁴ and w² lie between positive multiples of ρ_K^(−2α_K), so`.
- Line 921: `… ∩ {r > r_♯} for` / `𝔛 ≥ max(6(|α_sf| + 1) max(1, 5Γ/3), (4/3)λ_*), with λ := ¾𝔛. There`.
- Lines 935–936: `… By (∗) the hypotheses hold, with λ := ¾𝔛r_♯,` / `for 𝔛 ≥ r_♯⁻¹ max(6(3|α_K| + 1) max(1, 2Γ),
  (4/3)λ_*), and as there w²r⁻⁴ and w² lie between positive multiples of` / `ρ_K^(2α_K), [[eq:iv5-6-core]] gives the`.

All of these lines are ≤ 121 characters.

**n7. T20, lines 899–901 and 904–905.**
- The density argument mollifies near Σ^♯ without first extending across it.
- ρ_K := r/(t + r) is defined only on {t > −r}, while lem:iv5-6-core needs ψ ∈ C^∞(N). Its relation to the ρ_K of the
  statement is not stated.

Replacements:

    vanishing for t < 0 with compact support (extend across Σ^♯, translate in t, mollify and cut off at large r), and both
    sides are continuous in its norm.

and

    and ω′ := χω, with ω smooth, vanishing for t < 0 and with compact support. On {t > −r} put ρ_K := r/(t + r), extended
    smoothly and positively to N; on r⁻¹([r_♯, r̂]) ∩ {t ≥ 0} it is ρ_K′/(1 + ρ_K′), ρ_K′ the ρ_K of [[def:iv5-0-1]] near K⁺,
    so the weights are equivalent. Take R := {r ≥ r_1}, f_1 := r_1 − r, I_+ := {1}, Y := 0 and

**n8. Line 1157 (T28).** Current text: `([[lem:iv6-0-1]] (c)). So the estimate at R_out holds with constants`. lem:iv6-0-1 (c)
gives the b-principal symbol near r = 0. R_out is at ρ = 0, where the claim comes from (H2). Replacement:

    near ρ = 0 ((H2) of [[sec:i-a-1-3]], which (□^C)^(σ) satisfies, as above). So the estimate at R_out holds with constants

**n9. Lines 1240–1243 (T32).** Chapter line 2465, which follows T32's new text unchanged, ends "dτ being past timelike
on supp χ₁′". After T33's "χ₁ := χ_(τ,0)", that symbol is ambiguous; the cut-off meant is χ_(τ,1). Extend T32's old
and new texts by that line. Replacement for it:

    future, resp. past, lightlike covectors, dτ being past timelike on supp χ′_(τ,1).

**n10. Lines 676–677 (T17).** Current text: `…be such that at each point at most two of them vanish, and those with
linearly independent differentials, and let R := …`. Replacement for line 677:

    most two of them vanish, and those that vanish there have linearly independent differentials, and let

The current line 678 then starts with "R := {f_1 ≤ 0, …".

**n11. T4, lines 339–343.**
- "w a positive function on M^♭ (a product of powers of ρ_sf and ρ_K)" does not cover T33, which applies the lemma on M
  with ρ_cf. A suggested reading is "(a product of powers of boundary defining functions)".
- prop:iv5-5-3 (2) has a factor named f, which clashes with the lemma's f. The proposition does not invoke the lemma,
  but "Every commutant in [[sec:iv5-2]]–[[sec:iv5-5]] has the form" includes it.

**n12. Proof-file layout.**
- A blank line is missing before "## 7." (line 1447) and before "## 9." (line 1491).
- Line 119, "the ambiguity of item 3", refers to something the file does not contain.
- T22, lines 976–977 ("for the data extended smoothly to S"): a clause is suggested, "(on S, (ω, r𝓛_(∂_t)ω) and
  (ω, ∇_nω) determine each other)", because thm:std-bgp-cauchy (5) takes the data u|_S and ∇_nu|_S.
- prop:iv5-7-1 (chapter lines 2032–2034) says (5.68)–(5.69) "need only lem:iv5-0-3 (c) and lem:iv5-0-4". The new
  proof also uses lem:iv5-0-3 (a) and the bounds of its hypothesis paragraph. They hold on {r ≥ ½r_♯} too, so the
  conclusion stands.

## What I checked and found correct

**Placement**
- On the base 007858d8, which is the chapter at 19059be4:
  - every old text occurs exactly once, and no two overlap;
  - T7, T15, T16 and T29 are partial-line old texts, and they match once the newline the fence adds is dropped;
  - applying all 43 texts reproduces the writer's scratch chapter byte for byte (md5 bacd1122…).
- At HEAD, with the 16 crosswalk rows inserted after their anchors:
  - `lint.py --chapters` reports 4,665 labels and 0 hits, and `assemble.py --check` reports 0 problems;
  - `lint.py --paper` reports 0 hits;
  - the longest line of PAPER.md is 121 characters;
  - the crosswalk has 216 rows in chapter order;
  - the only wrapped-line starts are the two genuine list items of T9 and T25;
  - all labels are lowercase.
- Overlap with P-G1:
  - variant A's old text occurs once in C33-11's new text, and it applies after C33-11;
  - C33-20's anchor is T34's first old line, handled as the file says;
  - C33-10 and T5, and C33-12 and T7, are adjacent and do not overlap;
  - C33-1, 2, 5–10 and 12–19 share nothing with T1–T43;
  - no other proof file contains these old texts.

**Classification**
- The 247 citations on the base split exactly as the file says: 208, 28, 4, 3, 2, 1, 1.
- Every (a) row matches its line.
- I checked every (b) citation in lines 1220–2665. Each is a name of a displayed or proved statement, a definition
  written out, or a remark. The only omission is line 2107 (n2).
- I found no used-and-unproved step missed beyond M1. The pairing (5.37)–(5.38) at line 1505 is displayed and
  verifies directly, as T7 does for the adjoint.

**T1, T2 and T3**
- T1: r⁻¹ = ρ_sf on charts 2–3, and r ≥ r_♯.
- T2: ρ_sf⁻¹V(ρ_sf) = −∂_(z^μ)r, the class of ∇, and □_g = −g^(μν)(∇∇)_(μν).
- T3: prop:np-10-14 (v) holds for every δ_r > 0, and the sets in (4) and (5) only shrink. prop:iv5-7-2 (iii) needs
  2δ_r ≤ v(1 − δ_sf), which T3 now guarantees.
- T8 and the uses of prop:iv5-3-1 in prop:iv5-7-1 (viii)–(ix) and prop:iv5-7-2 (iii)–(iv) are consistent, given m1.

**lem:iv5-2-symbols and the symbol texts**
- lem:iv5-2-symbols: the Leibniz identity is exact for both signs, including wH_(−ℓ+j)(w⁻¹) = ℓ(dw/w) + wH_j(w⁻¹),
  a·a_k = a_k²φ_k, and supp f.
- The existence formula is right: −χχ′ = (smooth positive)·(φ^(1/2)(x − α)⁻¹)² near α, and (smooth
  positive)·(φ(β − x)(β − x)⁻¹)² near β.
- For T6, T7, T8, T10, T11, T12, T13 and T14 I re-derived every b_0, b_R, b_K, b_sf, e, e₁, e₂, e_R, e_T and b_T from
  the lemma. In each I checked the weight bracket (ℓ(dw/w) and wH_j(w⁻¹) for w = ρ_K^(±α_K), w, w⁻¹ and w′), the
  sign of ±φφ′ against the sign of −ℓ(dφ) given by lem:iv5-0-5 (3)–(6) or by causality, and the square root.
- T13 uses b_0's −1 and the factor χ₁′/χ₁ = 𝔛(r − r_1)⁻².

**The pairings**
- T7's eq:iv5-2-adj, derived from Im X = (X − X*)/2i: Im(−L_h*) = Im L_h = hS, and
  ½{A², Q} = AQA + ½[A, [A, Q]].
- T42 and T43: ∓Im⟨P_h*ω, A²ω⟩ = ⟨(∓(Re L_h − Im □_h)A² ∓ (i/2)[P_h*, A²])ω, ω⟩, and the cancellation of
  c_0‖ΛAω‖².
- T41: the pairing bound, F handled by prop:iv5-1-2 (or prop:np-10-65-a (e) in variant A), and the 2N-step iteration
  inside the slack of the supports.

**lem:iv5-6-transport**
- (i): M^μ = −½ℓ^μ.
- (ii): the pointwise identity 2φB(Aω, ω) = ∇_μ(φB(M^μω, ω)) + ½B(ℓ(dφ)ω, ω) + φB(Sω, ω), and the signs of the
  boundary terms.
- (iii): K = r⁻²(…) and the count of c-factors against G(c)⁻¹-factors in eq:s14-s.

**lem:iv5-6-core**
- Every inequality: the three products, eq:iv5-6-core-1 (using h ≤ 1), the transport step, eq:iv5-6-core-2, and the
  conclusion.
- λ_* = max(1, 2(2C_Y² + C_R)/c₀, 8C_N/c₁, 4C₂^(1/2)/c₁) gives exactly the three absorptions used.
- C_* bounds both coefficients. Two factors 2 of slack are harmless: 4c₀⁻¹ where 2c₀⁻¹ suffices, and 4c₁⁻² where
  2c₁⁻² suffices.
- c₁ comes from lem:iv4-1-causal (d), and it holds for null ζ as well.

**The new proof of prop:iv5-6-1**
- P_h = h²□_g + 2hA, using lem:s14-box-c (the metric is Ricci-flat).
- A* = S − A, □_g* = Θ⁻¹□_gΘ = □_g + Z, and the bound on Y.
- (∗): 13/6 ≤ 9/4, −(5/8)γq² ≤ −(γ/4)(5q/4)², and |𝔛u + v| ≥ 5q/6.
- For all four estimates: the regions, the boundary functions and their I_± signs, κ = ⅛, the weights w and the norm
  equivalences, the commutators [P_h, χ] and [P_h*, χ] (including −2h²Θ⁻¹(∇^μΘ)(∂_μχ)), the cut-off arguments and the
  density arguments.
- eq:iv5-6-1 with f_3 = −τ in I_−, and β⁰_3 + β¹_3 bounded by ℋ_data.
- T21's bound on {τ = T}, uniform in T.

**thm:iv5-7-3 (b), T22**
- thm:std-bgp-development's statement and its Cauchy-development definition.
- S = N ∩ {t = 0} is acausal.
- Ω ∖ (K⁺ ∪ 𝗌𝖿) ⊂ D(S). The past parts of curves stay in {r ≥ min(r(p), r̂)}.
- BGP's σ_P(ξ) = −⟨ξ, ξ⟩ matches □_g = −∇^a∇_a.
- The solution does not depend on how the data are extended, since J⁺(S ∩ {r ≤ r_♯}) meets {r ≥ r_♯} only in S.
- Data compact in X_0 ∖ 𝗌𝖿 and f ∈ C_c^∞(Ω°) are dense in their spaces.

**def:iv6-0-2, T23**
- It agrees with chapter 20's (O2)/(O3) under ξ ↦ −ξ: the location of R_(σ₀,in), 𝖧_p = 𝖵_p, and σ𝖧 against
  sgn(σ₀)𝖧_(σ₀).
- The thresholds do not depend on σ₀, since p_in is linear (sec:i-a-4-3).
- Its uses:
  - prop:iv6-1-1, at real and at complex σ;
  - the uniformity: the constancy and margins on the connected union of the R_(σ₀,in), as T29 says;
  - index 0: the free orders are still admissible at every h⁻¹;
  - thm:iv6-3-1: ℓ = −½ is admissible at every σ;
  - thm:iv6-4-1: 𝗋_± are admissible on Θ_±, and the constant orders at e^(iθ);
  - no other chapter.

**prop:iv6-1-1, T25–T29**
- The shift: its sign and its power ρ^(−2ℓ).
- Pieces (C)–(F) of the proof of thm:i-a-7-2 (1) exist as cited.
- prop:i-a-4-9's threshold ½ inf min spec(S + S^(*h)) and prop:i-a-4-6's (−1 + ϑ_in)/2 are identified with eq:s14-theta-in.
- Chapter 22's thm:i-c-4-3 needs −q + 2 in the gap; with q = β, 2 − β ∈ [−C_0, 2) ⊂ (β_−, 2).
- lem:i-c-2-5 and lem:i-c-2-6 apply to r²(□^C)^(σ), with no root at β − 2.
- The complex σ case goes through prop:i-a-4-9 and thm:i-c-4-3 (2).

**thm:iv6-2-1, T30–T38**
- The weights of eq:iv6-2-e1 and eq:iv6-2-e2 come from w²r⁻⁴ and w², with r⁻² = ρ_sf²ρ_cf⁻².
- The bulk covectors.
- The cone-face symbols and their signs, including the backward commutant with χ̃.
- χ̃ = χ_(τ,2) vanishes for τ ≤ (2.25/10)T, and (2.25/10)·½ > 1/9.
- The renamings in the combination.
- eq:iv6-2-ap.
