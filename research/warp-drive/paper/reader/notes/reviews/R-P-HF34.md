# R-P-HF34: independent reading of proofs/P-HF34.md (the a priori estimate at level four, sec:tl5-hf4)

File read: proofs/P-HF34.md, md5 b06b3e6ccc316b68679ecaa9ea061242, 535 lines: chapter text 1-390, Placement 392-424,
Comparison 426-504, crosswalk rows 506-535. I read every line and every proof in full. Also read: the writer's report
notes/reports/P-HF34.md; sec:tl5-hf in full (chapters/87-ten-l5.md:3596-4609), sec:tl5-beyond (3488-3595) and the
statements and proofs of lem:tl5-xt-seed-jets and lem:tl5-xt-order (2803-2880); notes/reviews/R-P-HF.md (verdict, the
level question (a)-(e), M1, M2). Line numbers below are lines of P-HF34.md unless marked "87:".

Chapter 87 is byte-identical at the current HEAD 88ae2d77 (md5 ec7b5668bc80c2604dd99a3119203ac8) to the copy at
f99f4a13 and 60527421 that the Placement names, so its quotations and its line numbers 87:4608-4609 are current. At
this HEAD the assembly numbers sec:tl5-hf as Section 57.14 and thm:tl5-hf as Theorem 57.145 (not 57.132), and the new
section as Section 57.15 with thm:tl5-hf4 Theorem 57.155; the numbers the Comparison quotes are right.

## Verdict

**CONFIRMED** — 0 Major, 3 minor, 7 nits, and three errors in the Comparison table (not chapter text, for the author).

Every statement of the chapter text is true and every proof is complete, with every constant recomputed exactly
(below). The three minors are wording: a proof that reuses Step 1 without the paragraph Step 1 rests on (m1), a remark
that under-reports what the N₀ terms depend on (m2), and two sentences that say the section proves "the same
statement" or "[[thm:tl5-hf]]" at level four, where it proves a counterpart with three more constants (m3). Each has an
exact replacement, and all replacement texts of this review, applied together, pass the checks in the scratch merge
(last section). The minors should be applied in the merge.

## What was checked, and how

### 1. def:tl5-hf4-levels and lem:tl5-hf4-quadratic

- The low and high quantities are those of def:tl5-hf-levels with N = 4: 𝔰 has |Ψ_B| (|B| ≤ 2), |D̂Ψ_B| (|B| ≤ 1),
  |D̂²h|; 𝔧 has |Ψ_B|, |D̂Ψ_B| (|B| ≤ 4) and |D̂²Ψ_B| (|B| ≤ 3); Λ is for |B| ≤ 4; C⁶ = C^(N+2). Correct.
- (a). Letters go to one factor each, so solution factors carry disjoint letter sets. This holds once ℒ^B g = ℒ^B ĝ + Ψ_B
  is split, which the background count of the level-6 proof already does: (Λ + 1)^k is Λ for ℒ^B ĝ plus coefficient 1
  for Ψ_B, while g⁻¹ stays a background factor of norm at most 𝔤₀. Derivatives: H·D̂²h, H·h and D̂h·D̂h carry two, one
  and two, and (i)-(iv) never add one. So the orders sum to at most |I| + 2. Order |I| + 2 forces D̂²Ψ_I, which is the
  subtracted term. Correct, at every level.
- (b), exhaustive count. A high factor with d derivatives needs at least 3 − d letters (Ψ_B: |B| ≥ 3; D̂Ψ_B: |B| ≥ 2;
  D̂²Ψ_B: |B| ≥ 1). Two high factors need at least 6 − (d_X + d_Y) ≥ 4 letters, so none occur at |I| ≤ 3. At |I| = 4
  equality forces d_X + d_Y = 2 and all four letters on the pair: (d_X, d_Y) = (1, 1) gives D̂Ψ_2·D̂Ψ_2, and (2, 0)
  gives D̂²Ψ_1·Ψ_3. Three high factors would need at least 7 letters.
  - D̂Ψ_2·D̂Ψ_2 needs two first derivatives on different factors, so it comes only from 2𝔮.
  - D̂²Ψ_1·Ψ_3 needs D̂² on one factor, so it comes only from H^(λσ)D̂_λD̂_σh. Ψ_3 comes from ℒ³H, as the expansion of
    D̂²h gives a single solution factor. 2𝔠(H)h has no derivatives.
  - Both pairs occur. Every other monomial at |I| ≤ 4 has at most one high factor, so it has a factor bounded at the
    point.
  - The other factors of a monomial in 𝔑^M_I carry no letter and no derivative, so they are H or h. The bounds
    |𝔑^L_I| ≤ 𝔠_(|I|)𝔰𝔧 and |𝔑^M_I| ≤ 𝔠_(|I|)𝔭_M follow, since the background norms of the two parts together are at
    most 𝔠_(|I|). Correct.

### 2. lem:tl5-hf4-face, derived independently

- Along γ_ω: τ₁ = t, dτ₂/dv = 1 − κκ′, and dμ dτ₂/(1 − κκ′) = R³ dω dv. φ is nondecreasing in v and at most φ(t, b) on
  Σ; φ ≥ 0. S_t ⊂ Σ, because τ₂ is smallest at v = 1/2 on {τ₁ = t}. So [·]_t, the supremum over Σ₁(t, v*), covers S_t.
- (a). ∂_γ(A_e) = (ℒ_(∂_γ)A)_e, since ∂_u and ∂_v commute with 𝒱 and κ′ is constant. Then
  - (d/dv)|A_e|² ≤ |A_e|² + |(ℒ_(∂_γ)A)_e|²;
  - |ℒ_(∂_γ)A| ≤ |∂_γ||D̂A| + r|D̂∂_γ||A|, as D̂ is torsion free;
  - |A_e|² + |(ℒA)_e|² ≤ 𝔳^(2r)((1 + 2r²|D̂∂_γ|²)|A|² + 2|∂_γ|²|D̂A|²).
  Integrate from 1/2, weight with e^(−φ(v)) ≤ e^(−φ(v′)) ≤ 1, and use dω dv = R⁻³ dμ dτ₂/(1 − κκ′). The value at
  v = 1/2 is ∫_(S_t)|A_e|² ≤ [𝔳^(2r)]_t ∫_(S_t)|A|² dω, and the bulk constant is 𝔱_r. Exactly (a).
- (b). 6C_(S³)² = 1/2 by lem:tl5-hf-sphere, with sup_ω Σ f² ≤ Σ sup f². Then
  - |K(B_e)| ≤ |(ℒ_K B)_e| + r|B_e|;
  - |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K B)_e| + r|(ℒ_K B)_e| + r|(ℒ_(K′)B)_e| + r²|B_e|, the index actions being constant;
  - squaring and summing over the 6 K and the 36 pairs gives the coefficient 1 + 6·2r² + 36·4r⁴ = 1 + 12r² + 144r⁴ on
    |A_e|², 2 + 6·4r² + 6·4r² = 2 + 48r² on each |(ℒ_K A)_e|², and 4 on each |(ℒ_(K′)ℒ_K A)_e|².
  For r ≥ 1 the first coefficient is the largest, so the factor is (1/2)𝔭_r 𝔵_r(t). See nit n2 for r = 0.
- (c). |X||Y| ≤ 𝔴^(r_X + r_Y)|X_e||Y_e| ≤ max(1, 𝔴)⁶|X_e||Y_e|, so 𝔪(t)² = [max(1, 𝔴)¹² R³]_t. Then
  e^(−φ) = e^φ e^(−φ) e^(−φ) with e^φ ≤ e^(φ(t,b)), and the L²_v L^∞_ω against L^∞_v L²_ω split. Exactly
  eq:tl5-hf4-holder.

### 3. lem:tl5-hf-linfty at N = 4, and eq:tl5-hf4-m2

I went through the proof of lem:tl5-hf-linfty step by step at N = 4.

- *Second derivatives* (|C| ≤ 3). Lemma G is needed only for |J| ≤ 3, where 𝔑^M = 0. 𝔧 ≤ 2𝒥₁ + M₂, with
  M₂ = max_(|C|≤3)|D̂²Ψ_C|. With k₃𝔰 ≤ 1/2 this gives M₂ ≤ 2(k₁ + 1)𝒥₁ + 2k₂ max_(|J|≤3)|ℒ^J(2R̂ic)| at every point of
  Q(a, b). That is eq:tl5-hf4-m2 with ϱ(p).
- *Zeroth order* (|B| ≤ 2). The words JB have length at most 4 = N, and |Ψ_(JB)| ≤ η₀ on S_a.
- *First order* (|B| ≤ 1). |JB| ≤ 3 = N − 1, and |D̂Ψ_(JB)| ≤ η₀ on S_a.
- *Last step* (B = ∅). Every factor of N(h) is low. L runs over the words of length at most 1, and 𝔐 = 8.

No other step uses N ≥ 5, so the lemma's claims are correct.

### 4. lem:tl5-hf4-mixed, every constant recomputed exactly

- On faces, |Ψ|² + |D̂Ψ|² ≤ 𝔨₂(e_o + κ′e_i): the e_o coefficient is 1/z̲ + 1/c ≤ 1/z̲ + max(1/c, 1/κ′), and the e_i
  coefficient is 1 ≤ κ′ max(1/c, 1/κ′). This gives the second line of eq:tl5-hf4-mixed. With eq:tl5-hf4-m2 at the
  points of Σ, ‖M₂‖_Σ ≤ λ_t𝔍 + ς_tϱ.
- Ranks: (D̂Ψ_B, D̂Ψ_(B′)) is (3, 3) and (D̂²Ψ_Z, Ψ_B) is (4, 2), both with sum 6. Summing over ordered pairs gives
  X₁²Y₁² + X₂²Y₂².
- X₁: m′₀, m′₁, m′₂ = 0, 2, 6 (m′_k ≤ 2m′_(k−1) + 2). Σ_(|J|≤2) m′² = 6·4 + 36·36 = 1320 and 49·1320 = 64,680. The words
  JB are distinct, since |B| = 2 fixes the split, so X₁² ≤ 𝔭₃𝔵₃(1 + 64680[Λ]²)𝔍².
- X₂: m₁ = 7 and m₂ = 35 (m_k ≤ 4m_(k−1) + 7 = (7/3)(4^k − 1)). Each monomial of R has at most two background factors,
  and Λ ≥ 1 gives |R| ≤ m Λ²𝒥₁. Then 2·7·43 = 602, Σ m² = 6·49 + 36·1225 = 44,394, 2·7·44394 = 621,516, and
  789² = 622,521 > 621,516.
- Y₁ and Y₂: 49·2π² = 98π² and 343·2π² = 686π². Also Σ_(|B|=2)|D̂²Ψ_B|² ≤ 49M₂², and the |B| = 2 and |B| = 3 sums are at
  most 𝒥₁².
- 𝔭₂ = 2353, 𝔭₃ = 11,773, 𝔭₄ = 37,057; √602 = 24.54, π√98 = 31.10, π√686 = 82.28. The final max-bounds of X_i and Y_i
  follow from √(a² + b²) ≤ a + b, and the first line of eq:tl5-hf4-mixed from (X₁²Y₁² + X₂²Y₂²)^(1/2) ≤ X₁Y₁ + X₂Y₂.
  Correct.

### 5. prop:tl5-hf4-bootstrap and the constants

- *Step 1* holds at N = 4, with ℰ⁰_4 ≤ μ^(−4)e^φ Y² and the μ^(−2) of 𝔰_*. It rests on the opening paragraph of the
  level-6 proof (m1).
- *Step 2*.
  - For |J| ≤ 3, ℒ^J N(h) has no 𝔑^M part. 𝔔_IJ vanishes for |J| = |I| with J ≠ I (by the construction in
    def:tl5-hf-coupling, ℒ^J𝔤 with J ≠ I enters only through L̂Ψ_J with |J| < |I|), so 𝔑^M_I enters only with
    coefficient 1.
  - The 𝔑^M term is bounded by the second inequality of lem:tl5-hf-pointwise and by √e_o + √c√e_i ≤
    (1 + c/κ′)^(1/2)((1 − κκ′)ε₁)^(1/2). Then Cauchy–Schwarz on each face Σ₁(t, b′) and over I, (Σ_I ‖𝔑^M_I‖²)^(1/2) ≤
    49[𝔠₄]_t‖𝔭_M‖_Σ, the last factor at most μ^(−2)Y_s, and 𝔍 ≤ [𝔨₂]^(1/2)μ^(−2)Y_s.
  - The product is 98 e^(φ(t,b′)/2)[…]_t[𝔠₄]_t𝔪𝔵𝔶 μ²(𝔍 + ϱ)(𝔍 + ϱ + η₀)Y_s ≤ m_t(…). The expansion
    μ²(𝔍 + ϱ)(𝔍 + ϱ + η₀) ≤ [𝔨₂]μ^(−2)Y² + [𝔨₂]^(1/2)(2ϱ + η₀)Y + μ²ϱ(ϱ + η₀) gives exactly S_M, 𝔯_M and ε_M.
- *Step 3* and the closing. 4A_(w,4)B_(w,4) = 8(√2δ_w + 2ε_w + 2ε_M)(S_F + S_M). The smallness conditions are those of
  the level-6 proposition with 𝔯_(w,4) in place of 𝔯_w. The case A_(w,4) = 0 forces δ_w = ε_w = 0, as at level 6.
  Correct.

### 6. lem:tl5-hf4-persistence

- *Order counts.* P(4) holds. In the step m ≥ 5, the factors of order ≤ m − 3 are bounded at a point, and those of order
  ≤ m are bounded in ‖·‖_(Σ,0). Two factors of order ≥ m − 2 force m ≤ 6 and orders ≤ 4. At most one of them is D̂²Ψ,
  so the ranks sum to at most 6.
- *Mixed products and the weight.* In (i), the weight sits on one side only, with no factor e^(φ(t,b)), so no constant
  depends on Ã. Order-(m + 1) factors can occur only on the X side, and only at m = 5 (o_Y + 1 ≤ 5 ≤ m). So a mixed
  product never has two unknown factors.
- *Step (ii).* The second case occurs only at m = 5 with orders 3 and 3, and both sides are then known.
- *Step (iii).* Constant rates A + Ã, A′. The part with A, A′ absorbs ñᵀ𝔅_mñ, and (1 − ϑ)Ã(e_o + κ′e_i) absorbs the
  linear-in-energy terms. lem:tl5-hf-identity is applied directly, so the fluxes on N₀ and N₁ (order ≤ m + 1) enter as
  constants. The traces on S_t and S_a are data of order ≤ m. The linear estimate is never used under a vanishing
  hypothesis on N₀, so the level-6 reading's M2 is respected.
- *Step (iv)* and the final paragraph use only bounds at a point.

Correct.

### 7. thm:tl5-hf4 and rem:tl5-hf4-level

- Hypothesis (a) has the merged form: η₀ < 𝔰₁, with derivatives of order ≤ 4 on N₀, and the N₀ fluxes in δ_w.
- (H1) is eq:tl5-hf4-h1, (H2) is lem:tl5-hf4-persistence, (H4) comes from |h|_k̂ < κ_m/2, and (H3) is
  eq:tl5-hf4-closing. ε ≤ ε_𝔰𝔰_* holds because |h|, |D̂h| and |D̂²h| are low at N = 4.
- lem:tl5-xt-order (c) with m = 5 gives vanishing of G^♯ − ĝ to order 4 on N₀⁺ under (X). lem:tl5-xt-seed-jets (a) and
  (b) are quoted correctly: orders ≤ 3 are the seed's, and the fourth v-derivatives of the leaf metric differ off at
  most one torus. The remark states only the sufficient condition and its failure for seed-jet backgrounds. Correct,
  except m2 and nit n5.

### 8. Citations of sec:tl5-hf results at N = 4

- def:tl5-hf-levels (N ≥ 5) is cited for its formulas. lem:tl5-hf-quadratic (N ≥ 5) is cited for its expansion, its
  majorant 𝔠_n and its items (ii) and (iii), none of which use N ≥ 5.
- lem:tl5-hf-linfty (N ≥ 5) is re-proved at N = 4 by lem:tl5-hf4-linfty. def:tl5-hf-norm and def:tl5-hf-constants
  (N ≥ 5) are cited for formulas that do not use it.
- lem:tl5-hf-persistence (N ≥ 6) is cited only for its last paragraph, which uses bounds at a point. thm:tl5-hf (N ≥ 6)
  is cited for its proof, with the replacements named; that proof's only level use, "low quantities for N ≥ 4", holds.
- The rest (sphere, components, Sobolev, eq:tl5-hf-cs-r, recovery, allocation, identity, linear estimates,
  def:tl5-hf-coupling with N ≥ 1, prop:tl5-hf-linear-n, quasilinear, conversions) is level-free.

No result is cited outside its range. The section's "N := 4 throughout" covers the two places that point to the level-6
lemma for N-dependent quantities (nit n3).

### 9. Overclaim

Every sentence of 1-390 and of the placement text was read for this. Apart from m3 (and n5's "excluded"), nothing
states more than is proved.

### 10. The writer's bookkeeping

The file bounds every level by the top one (S_F ~ μ^(−4), S_M ~ μ^(−2)). Its statements are right as they stand. The
graded count is not claimed in the chapter text.

## Major

None.

## minor

### m1. prop:tl5-hf4-bootstrap reuses Step 1 without the paragraph it rests on (lines 226-228)

*Why.* The proof says "Step 1 of the proof of [[prop:tl5-hf-bootstrap]] holds as written". That Step 1 starts from the
level-6 proof's opening paragraph. There, by thm:tl5-wg (F4_W), g is vacuum with the derivatives of G^♯ on N, so
𝔰 ≤ η₀ < 𝔰₁ on N₀ ("It contains 1/2, as D^κ_(1/2) = S ⊂ N₀"). Step 2 needs the same fact to apply lem:tl5-hf4-mixed with
the η₀ of def:tl5-hf4-constants: that lemma needs η₀ to bound g's quantities on N₀. The paragraph should be named.

Old:

    *Proof.* Step 1 of the proof of [[prop:tl5-hf-bootstrap]] holds as written with N = 4, A_(w,4) in place of A_w and
    [[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]]: it gives 𝔰 ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, |h|_k̂ < κ_m/2 and
    θ_H ≤ ϑ.

New:

    *Proof.* The first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]] hold as written with N = 4, A_(w,4)
    in place of A_w and [[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]]: g is vacuum and has on N ∩ D^κ_s the
    derivatives of G^♯, so that the quantities on N₀ bounded by η₀ are those of g; and 𝔰 ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, so
    that |h|_k̂ < κ_m/2 and θ_H ≤ ϑ.

### m2. rem:tl5-hf4-level under-reports the derivatives on N₀ (lines 380-382)

*Why.* The remark says the constants "on N₀ … involve the derivatives of G^♯ − ĝ of order at most 4, through η₀ and the
fluxes in δ_w". The terms 2Ω̂²|dv(𝔟[Ψ_I])|, |I| = 4, of δ_w contain D̂_TΨ_I, a transverse derivative of order 5. The
file's own def:tl5-hf4-constants says so (line 213: "and of order 5 in the terms 𝔟, which vanish where H does"). The
vanishing statement is right; the list of what is involved is not.

Old:

    factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2). On N₀ they involve the derivatives of
    G^♯ − ĝ of order at most 4, through η₀ and the fluxes in δ_w, which vanish when G^♯ − ĝ vanishes together with its
    partial derivatives of order at most 4 at the points of N₀. At the first stage of the problem at 10 l5, by

New:

    factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2). On N₀ they involve the derivatives of
    G^♯ − ĝ of order at most 4, through η₀ and the fluxes in δ_w, and of order 5 in the terms 𝔟 of δ_w, which carry the
    factor H; all of these vanish when G^♯ − ĝ vanishes together with its partial derivatives of order at most 4 at the
    points of N₀. At the first stage of the problem at 10 l5, by

### m3. "the same statement" and "proves [[thm:tl5-hf]] at level four" (line 3, and Placement item 2 New, lines 418-420)

*Why.* thm:tl5-hf assumes N ≥ 6. With N = 4, its closing condition 8(√2δ_w + 2ε_w)S_F < 1 is not what is proved. The
section proves thm:tl5-hf4, whose constants carry S_M, 𝔯_M and ε_M as well. So "This section proves the same statement
at level four" and the new sentence of rem:tl5-hf-level, "[[sec:tl5-hf4]] proves [[thm:tl5-hf]] at level four", say
more than is proved. In rem:tl5-hf-level the new sentence also follows "the estimate (H1) itself needs N ≥ 5", which
refers to that remark's way of bounding the products. The replacement says so, so that the two sentences do not read as
a contradiction.

Line 3, old:

    order N. This section proves the same statement at level four, with N := 4 throughout. The results of [[sec:tl5-hf]]

New:

    order N. This section proves its counterpart at level four, with N := 4 throughout. The results of [[sec:tl5-hf]]

Placement item 2, New text (lines 417-420): keep line 417 and replace lines 418-420, so the new text of
rem:tl5-hf-level is:

    [[lem:tl5-hf-conversions]] (b). The face energies of level 3 control D̂²h only in H² of the four-dimensional faces, and
    H² of a four-dimensional manifold does not embed in L^∞; so they give no bound of |D̂²h| at a point. With another
    bound of the products, [[sec:tl5-hf4]] proves the counterpart [[thm:tl5-hf4]] of [[thm:tl5-hf]] at level four, where two
    kinds of products have no factor bounded at a point; it bounds them on the faces by a Hölder inequality in mixed norms.

(The item's Old text is unchanged and still occurs exactly once, as whole lines, at 87:4608-4609.)

## nits

### n1. lem:tl5-hf4-face: v_Σ is undefined, and ∂_γ enters 𝔱_r before it is defined (lines 72-73)

Old:

    such that Σ := Σ₁(t, b) is not empty, and let γ_ω(v) := (t − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_Σ, ω ∈ S³, be the curves
    of the proof of [[lem:tl5-hf-sobolev]] that fill Σ, starting on the leaf S_t := {t} × {1/2} × S³ of N₀. Let φ be as in

New:

    such that Σ := Σ₁(t, b) is not empty, and let γ_ω(v) := (t − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_Σ, ω ∈ S³, with v_Σ the
    largest value of v on Σ, be the curves of the proof of [[lem:tl5-hf-sobolev]] that fill Σ, with velocity
    ∂_γ := ∂_v − κ′∂_u, starting on the leaf S_t := {t} × {1/2} × S³ of N₀. Let φ be as in

### n2. lem:tl5-hf4-face for r = 0 (line 86)

*Why.* For r = 0, the proof's squaring gives the coefficients 1, 2 and 4, which exceed 𝔭₀ = 1. The statement is still
true for scalars, by the sphere lemma directly, but the proof as written needs r ≥ 1. Only r = 2, 3, 4 are used.

Old:

    Then for every smooth covariant tensor field A of rank r ≤ 4 on Q(t, b):

New:

    Then for every smooth covariant tensor field A of rank r with 1 ≤ r ≤ 4 on Q(t, b):

### n3. Two pointers to the level-6 lemma for N-dependent quantities (lines 145 and 198)

The convention "N := 4 throughout" (line 3) makes these correct. Pointing at the level-4 lemma is exact, and it costs one
character on each line (both lines stay ≤ 121).

- Line 145: "𝒥₁, k₁ and k₂ as in [[lem:tl5-hf-linfty]] and 𝔨₂" becomes "𝒥₁, k₁ and k₂ as in [[lem:tl5-hf4-linfty]] and
  𝔨₂".
- Line 198: "ϱ and η₀ being those of [[lem:tl5-hf-linfty]] for a" becomes "ϱ and η₀ being those of [[lem:tl5-hf4-linfty]]
  for a" (the line break as in the file, after "for a").

### n4. 𝔵_t and 𝔶_t against 𝔵_r(t) (lines 149, 151, 155, 189, 202)

𝔵_t is defined from 𝔵₃(t) and 𝔵₄(t), so "𝔵₃" can be read as 𝔵_t at t = 3. This is optional: rename 𝔵_t to 𝔛_t and 𝔶_t to
𝔜_t at the 8 places in the chapter text (lines 149 and 151 once each; 155, 189 and 202 twice each), and correspondingly
in the Comparison section.

### n5. "Level three is excluded by the count of [[rem:tl5-hf-level]]" (lines 388-390)

*Why.* The relevant part of rem:tl5-hf-level is not its count, which concerns this method's N ≥ 5 and N ≥ 6. It is its
observation that level-3 energies give no pointwise bound of |D̂²h|. "Excluded" is stronger than a remark carries.

Old:

    5 on N₀⁺, and a background with the seed's jets there does not satisfy it. Level three is excluded by the count of
    [[rem:tl5-hf-level]]: its face energies give no bound of |D̂²h| at a point, which the passage to the double-null gauge
    needs.

New, with the two last lines being n7 (optional):

    5 on N₀⁺, and a background with the seed's jets there does not satisfy it. At level three the face energies give no
    bound of |D̂²h| at a point ([[rem:tl5-hf-level]]), which the passage to the double-null gauge needs. As for
    [[thm:tl5-hf]] ([[rem:tl5-beyond]]), the hypotheses of [[thm:tl5-hf4]] are established in this paper for no background
    at 10 l5.

Without n7, the second line ends "…which the passage to the double-null gauge needs."

### n6. "Λ now bounding" (line 268)

"Now" is on STYLE's narration list. Here it is mathematical, and lint does not flag it. Optional: "Λ here bounding the
quantities of".

### n7. The status of thm:tl5-hf4's hypotheses (optional; text in n5)

rem:tl5-beyond and the paragraph after thm:tl5-hf say that no numerical value of the constants is used and that the
hypotheses of thm:tl5-hf are established for no background at 10 l5. Nothing says so of thm:tl5-hf4, and the Placement
leaves rem:tl5-beyond unchanged. The sentence in n5 closes this without touching rem:tl5-beyond. It is not an
overclaim as written; it only prevents a reader from taking the level-4 theorem to change that status.

## The Comparison section (not chapter text; for the author)

The formulas, the μ-powers, the word counts, F₄ = 75, F₆ = 4683, 𝔐 = 8 and 400, the coupling counts (20 and 28 rows;
15 and 28 level pairs) and the level-4 constants are all right. So is the whole 𝔠_n row, recomputed from eq:tl5-hf-cn:
104, 1.82e3, 4.14e4, 1.22e6, 4.44e7, 1.93e9, 9.75e10 at Λ = 1; 4.44e7 and 9.64e8 for 𝔠₄, 9.75e10 and 8.54e12 for 𝔠₆. The
floating-point 𝔠_n table agrees with an exact re-evaluation to the digits shown. Three errors:

- C1 (lines 483-484). "built from the face suprema of … 𝔳⁴ and 𝔳⁶ on the leaf S_t". [𝔳⁴]_t and [𝔳⁶]_t are suprema over
  the face Σ₁(t, v*), by the definition of [·]_t, not over S_t (a supremum over S_t would suffice for the proof).
- C2 (line 495). "the background must carry g′'s v-jets of orders 4, …, N + 1". That is the sufficient condition of
  lem:tl5-xt-order (c), as the chapter text correctly says, not a necessary one; "must" overstates it.
- C3 (line 479). "𝔠_n enters 𝔤_N and k₃ (so 𝔰₀) for n ≤ N". k₃ uses 𝔠_n only for n ≤ N − 1.

The deduced graded count (μ^(−3/2)) is labelled as not part of any proof, and I have not checked it; it is separate
work.

## Crosswalk rows

The 22 rows are complete (one per label of 1-390), in chapter order, with 4 tab-separated fields each, and their
PENDING line numbers match the file. The note for the existing rem:tl5-hf-level row is fine. If the replacements above
are applied, the labels after line 71 move. The new PENDING lines are:

- unchanged: sec:tl5-hf4 1, sec:tl5-hf4-products 14, def:tl5-hf4-levels 16, eq:tl5-hf4-pm 26,
  lem:tl5-hf4-quadratic 30, eq:tl5-hf4-g 40, lem:tl5-hf4-face 71;
- eq:tl5-hf4-holder 96, lem:tl5-hf4-linfty 130, eq:tl5-hf4-m2 135, lem:tl5-hf4-mixed 143, eq:tl5-hf4-mixed 157;
- sec:tl5-hf4-bootstrap 193, def:tl5-hf4-constants 195, eq:tl5-hf4-constants 207, prop:tl5-hf4-bootstrap 217,
  eq:tl5-hf4-smallness 220, eq:tl5-hf4-h1 225;
- lem:tl5-hf4-persistence 263, thm:tl5-hf4 352, eq:tl5-hf4-closing 364, rem:tl5-hf4-level 378.

These numbers are for all of m1-m3 and n1-n7 applied. Without n7, nothing changes before line 391.

## Scratch merge

Trees: git archive of HEAD 88ae2d77, chapter 87 md5 ec7b5668bc80c2604dd99a3119203ac8.

- /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rphf34/ holds the file
  as written.
- /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rphf34b/ holds the file
  with every replacement of this review applied (m1-m3, n1-n7, n4's renaming).

In each tree:

- Item 1 inserts lines 1-390 after the last line of rem:tl5-hf-level, with one blank line before.
- Item 2's Old text occurs exactly once as whole lines (87:4608-4609) and is replaced.
- The 22 rows are appended to the crosswalk of chapter 87, and the rem:tl5-hf-level row is amended.

Results, identical for both trees:

- lint.py --chapters: "chapters: 62 file(s), 5101 label(s) defined, 0 hit(s)" (clean HEAD: 5079; +22);
- assemble.py --check: "labels 5101, computations cited 0, problems 0";
- in-memory assembly and lint of PAPER.md: "[] 0";
- no assembled line over 121 characters, and no source line of the chapter text or the placement over 121;
- no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "=" or "|" (the only "#" starts are the three headings).

Plain assemble.py was not run. No repository file was edited, and nothing was committed.

Verdict: CONFIRMED
