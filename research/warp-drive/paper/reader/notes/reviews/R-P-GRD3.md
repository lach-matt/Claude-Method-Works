# R-P-GRD3: independent reading of proofs/P-GRD3.md (the constants sharpened a third time, sec:tl5-hft)

**File read:** proofs/P-GRD3.md, md5 fce4240ddc681ad32a8368735c51d9b4, 339 lines:
- chapter text 1–213 (sec:tl5-hft, 19 labels);
- Placement 215–241;
- Comparison 243–312;
- crosswalk rows 314–339.

I read every line and every proof in full.

**Also read:**
- notes/reports/P-GRD3.md;
- sec:tl5-hfs as merged (87:5426–5758), which is byte-identical to the P-GRD2.fixed.md I confirmed;
- sec:tl5-hfg, sec:tl5-hf4 and sec:tl5-hf, for every step reused.

Line numbers are lines of P-GRD3.md unless marked "87:". Repository state:
- HEAD is 46fc10fc.
- Chapter 87 (md5 e5fbd541…) last changed at 53bd18fb, so the Placement's quotations are current.
- I edited no repository file and committed nothing.

## Verdict

**NOT CONFIRMED** — 0 Major, 2 minor (one of them in the Comparison), 4 nits (one in the Comparison).

**The mathematics is right.** Every proof is complete except one justification in lem:tl5-hft-leaf (m1, a gap in the argument, not in the result):
- both options of the smallness lemma;
- the products and mixed lemmas under the weighted absorption;
- the intrinsic Sobolev inequality;
- the norm comparison;
- the bootstrap and both theorems.

Every constant I could recompute agrees, except that the Comparison's C_(E,r)² are partial sums with no tail bound (m2).

**The two minors:**
- **m1** (chapter text). The Casimir eigenvalue c_π = 2j₁(j₁+1) + 2j₂(j₂+1) is asserted. It is true; I checked it numerically. But the two checks given in parentheses both have j₁ = j₂, so they fix only the sum of the two coefficients. They cannot show that Σ K_ab² is twice the sum of the two su(2) Casimirs. A three-line decomposition proves it (R1).
- **m2** (Comparison, used by the evaluation). "C_(E,2)² ≈ 0.894, C_(E,3)² ≈ 3.635, C_(E,4)² ≈ 15.70" are the sums truncated at 2j₁ < 3000. No tail bound is given. The true values are 0.89416, 3.63744 and 15.7096, so the quoted 3.635 and 15.70 lie below them beyond rounding. A constant in a sufficient condition must be an upper bound. With the tail bound proved below, C_(E,2)² ≤ 0.8942, C_(E,3)² ≤ 3.6375 and C_(E,4)² ≤ 15.710 (C1).

**Fixed copy:** scratchpad/reader/rpgrd3/P-GRD3.fixed.md, md5 88c8d48fa7ae99695c536c90a17ad66c, 345 lines. It has all replacements applied, the Comparison's included, and the crosswalk line numbers updated. It is checked in the last section.

## Checks on the file as submitted (scratch merge)

**Scratch tree:** git archive of HEAD 46fc10fc in scratchpad/reader/rpgrd3/tree. Item 2's old text occurs exactly once, at 87:5757–5758. After item 2 it ends the chapter, and the section is appended there with one blank line.

**Results:**
- lint.py --chapters: 62 files, 5207 labels (5188 + 19), 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: prints `[] 0`.
- Lines: at most 121 characters, in the source and after labels resolve.
- Wrapped lines: none starts with a forbidden marker ("- " checked by hand).
- Numbering: no printed number of the 5188 old labels changes. The section is Section 57.18; thm:tl5-hft is Theorem 57.183, thm:tl5-hf4t is Theorem 57.184, rem:tl5-hft-what is Remark 57.185.
- Crosswalk: 19 rows, complete, in chapter order, with matching lines. Appended, the 363 rows equal the 363 labels in order.
- Format: no file or program names, code or AI language in the chapter text. Labels are lowercase.

## The points briefed, checked

### 1. lem:tl5-hft-small

**Option (a).** I checked every low quantity; the ϱ and η₀ parts stay apart throughout.
- **Ψ_B (|B| ≤ N − 2):** μ^(|B|+2) ≤ μ^(|JB|) gives μ^(−(|B|+2)/2) C_S ℰ_g^(1/2) + C_(0,0) η₀. |H| ≤ 2|h|.
- **D̂Ψ_B (|B| ≤ N − 3), the remainder:** a coefficient with a ≤ 2 letters times Ψ_C, |C| ≤ |B| + 2 − a, gives Λ_a μ^(−|C|/2) 𝒥_g ≤ μ^(−(|B|+3)/2) Λ₂^μ 𝒥_g. So |ℒ^J D̂Ψ_B| ≤ μ^(−(|B|+3)/2) (1 + 6Λ₂^μ) 𝒥_g.
- **D̂Ψ_B, the derivative:** eq:tl5-hfs-m2 gives |D̂ℒ^J D̂Ψ_B| ≤ μ^(−(|B|+3)/2)(2(k₁^μ+1) + 6√2Λ₂^μ)𝒥_g + 2k₂ϱ, with ϱ unweighted. On S_a the bound (1 + 6Λ₂)η₀ is unweighted.
- **D̂Ψ_B, the result:** the merged C₁ algebra gives μ^(−(|B|+3)/2) C₁^♮ ℰ_g^(1/2) + C_(1,ϱ) ϱ + C_(1,0)^g η₀.
- **D̂²Ψ_B (|B| ≤ N − 4):**
  - the ℰ-parts of the jets inserted in the recovery carry at most μ^(−(|B|+4)/2) with k₁^(N−4,μ), as in lem:tl5-hfs-linfty;
  - their ϱ and η₀ parts carry the unweighted coefficients of k₁^(N−4), plus k₂ϱ;
  - the nonlinear terms are at most k₃^♮𝔰², all factors being low.
- **Combining:** μ^(−(o+2)/2) ≤ μ^(−N/2). The four bounds are each at most half of the three-term expression; for H, (1/2)C_(∞,μ) ≥ 2C_S and (1/2)C_(∞,0) ≥ 2C_(0,0). Absorbing with k₃^♮𝔰 ≤ 1/2 gives eq:tl5-hft-small.
- **Unchanged constants:** 𝔰₁^t = 𝔰₁^♮ and ε_(w,t) = ε_(w,s) are right, so A_t = A_s and only 𝔰_(*,t) changes.

**Option (b).** In a monomial with b background letters, the 𝔧-factor Φ has order at most |J| − b + 2, and the extreme case is D̂²Ψ_(C′), |C′| = |J| − b. I checked every factor type:
- **The bound for Φ:**
  - μ^((|J|+1)/2)|Φ| ≤ μ^(b/2) max(2𝒥_g, M_g^(j)), including H, since b ≤ |J|;
  - μ^((|C|+1)/2) = μ^((|C|−|J|)/2)μ^((|J|+1)/2) gives the weight of 𝔔_CJ;
  - H D̂²Ψ_J gives μ^((|C|−|J|)/2) 𝔰 M_g.
- **The absorption:** eq:tl5-hfs-sum with ν′ = μ gives k₃^♮(μ)𝔰(2𝒥_g + M_g), and hence M_g^(j) ≤ 2(k₁^(j,μ)+1)𝒥_g + 2k₂ϱ.
- **The low-level step:** μ^((|J|+4)/2) ≤ μ^(b/2)μ^((o+2)/2) for o ≤ |J| − b + 2 gives k₃^♮(μ)𝔰𝔰_g^(m).
- **The first-order step:** it is unchanged with M_g, since μ^((|B|+3)/2) ≤ μ^((|JB|+1)/2).
- **The result:** 𝔰 ≤ μ^(−N/2)𝔰_g^(N−4) gives eq:tl5-hft-smallb.
- **The threshold:** k₃^♮(μ) ≤ k₃^♮, so 𝔰₀^μ ≥ 𝔰₀^♮. 𝔰₀^μ is defined over D^κ in def:tl5-hft-constants.

**"(a) and (b) cannot be combined" (Comparison, marked deduced and "in this proof").**
- **It is a limit of this proof, and it is worded as such.**
- To weight the absorption, a factor's bound must carry μ^(b/2) relative to its weighted bound. The ϱ part of D̂²Ψ_(C′) (2k₂ϱ, from eq:tl5-hfs-m2) does not.
- So the ϱ part of the absorption sums to 𝔠^♮(1)𝔰·2k₂ϱ and needs k₃^♮(1)𝔰 < 1. That is the threshold of (a).
- Any split under 𝔰₀^μ > 𝔰₀^♮ must therefore weight the ϱ part, which is (b). A threshold of min(𝔰₀^♮, 𝔰₀^μ) is (a) itself.
- Combining the two would need a different bound of the residual's share of D̂²Ψ, not a rearrangement of this one.
- The chapter text claims nothing on this.

### 2. lem:tl5-hft-products

- **The factor bound:** under (b), |Φ₂| ≤ μ^(−ℓ_E/2)(𝔨_A𝒥_g + 2k₂ϱ) for Φ₂ = D̂²Ψ_C, from M_g^(N−1). The other bounds need no smallness, and 𝔰_P and 𝔰_P⁰ come from (b).
- **The ϱ term:** it is ν𝔰^(q−1)μ^((n−ℓ_E)/2)2k₂ϱ.
  - b = 0: ℓ_E ≤ n.
  - b ≥ 1: ℓ_E ≤ o₂ − 1 ≤ n − b + 1.
  - So μ^((n−ℓ_E)/2) ≤ μ^(−1/2)μ^(b/2), which gives μ^(−1/2)𝔠^♮_n(μ).
- **The second inequality:** for |J| < n, it gives μ^(−1/2)(𝔠^♮_(|J|)(μ)+1)μ^((n−|J|)/2), both for 𝔑_J and for H D̂²Ψ_J (μ^((n−|J|−1)/2)).
- **lem:tl5-hfs-mixed:** it uses smallness only through ‖M_g‖_Σ, which (b) supplies, and eq:tl5-hfs-m needs only 𝔰 ≤ 𝔰_♭.
- **Step 2, option (b):** the ϱ terms per level are μ^(−j/2)μ^(−1/2)Σ μ^((j−j′)/2)𝔮_(jj′)7^(j′/2)(𝔠^♮_(j′)(μ)+1)2k₂𝔰ϱ. With the weights μ^j, they give (1/4)μ^(−1/2)𝔤_(𝒥,s)k₂ϱ, which is ε_(w,t).
- **Everything else** in Steps 2–3 (𝒥-parts, 𝔮_H, 𝔑^M, 𝔰_P) is unchanged, so S_(F,s), S_(M,s), 𝔯_s and ε_(M,s) stand.

### 3. lem:tl5-hft-leaf (the intrinsic Sobolev inequality on S³)

**The group theory:**
- SO(4) = (SU(2)×SU(2))/ℤ₂ has irreducibles (j₁, j₂) with j₁ + j₂ ∈ ℕ. The stabilizer of o is the diagonal SU(2)/±1, which restricts (j₁, j₂) to [|j₁−j₂|] ⊕ ⋯ ⊕ [j₁+j₂].
- E_o = (2[0] ⊕ [1])^(⊗r): the isotropy acts trivially on du and dv and by spin 1 on T*_oS³.
- E is the homogeneous bundle SO(4) ×_(SO(3)) E_o, so Frobenius reciprocity gives dim V_π = (2j₁+1)(2j₂+1)m_(j₁j₂)(r).
- The action fixes ∂_u and ∂_v and preserves γ₀ and dω, so it is unitary for h₀ with constant α, β, ρ. ℒ_K is its derivative and is skew-adjoint.

**The Casimir:** I verified numerically that −Σ_(a<b)K_ab² has eigenvalues 3 on ℝ⁴ and 0, 4, 8 on (ℝ⁴)^(⊗2). These are 2j₁(j₁+1) + 2j₂(j₂+1) for (1/2,1/2), (0,0), (1,0)/(0,1) and (1,1).
- With L₁ := K₂₃, L₂ := −K₁₃, L₃ := K₁₂ and M_i := K_(i4), take J_i^± := (L_i ± M_i)/2. As vector fields these satisfy [J₁^±, J₂^±] = −J₃^± (and cyclically) and [J_i⁺, J_l⁻] = 0.
- Then Σ K_ab² = 2Σ((J_i⁺)² + (J_i⁻)²). I checked this exactly.
- The text's parenthetical checks, (1/2,1/2) and (n/2,n/2), cannot show this: m1.

**The rest of the proof:**
- The pointwise bound dim V_π/(2π²) follows from invariance and transitivity.
- The Cauchy–Schwarz inequality over π, with ‖((1+Ω)A)_π‖ = (1+c_π)‖A_π‖, gives the bound.
- The series converges absolutely, so the expansion converges uniformly to A.
- ‖(1+Ω)A‖² ≤ 6Σ_(|J|≤2)‖ℒ^J A‖², by skew-adjointness and the Cauchy–Schwarz inequality over the six fields.
- The convergence bound (m ≤ 5^r, |j₁ − j₂| ≤ r, 2r + 1 values of j₂) is right.
- r = 0 gives Σ 1/(2π²(n+1)²) = 1/12.

**The multiplicities**, recomputed by iterating ⊗(2[0] ⊕ [1]) with dimension checks 25, 125, 625: e(2) = (5, 5, 1), e(3) = (15, 21, 8, 1), e(4) = (51, 86, 46, 11, 1). All agree.

**The constants:**
- Write a = 2j₁ + 1 and b = 2j₂ + 1. The denominator is 1 + 2j₁(j₁+1) + 2j₂(j₂+1) = (a² + b²)/2, so each term is 4abm/(a² + b²)² ≤ m/(ab).
- Σ_(j₂) m_(j₁j₂)(r) ≤ Σ_j (2j+1)e_j(r) = 5^r, and for 2j₁ = n, b ≥ n + 1 − 2r.
- So the sum over 2j₁ ≥ N is at most 5^r/(2π²(N − 2r)). That is a rigorous tail bound.
- Exact summation (scratchpad/reader/rpgrd3/calc/ce.py):

| r | sum over 2j₁ < 3000 | plus tail bound | sum over 2j₁ < 2·10⁵ | upper bound | file says |
|---|---|---|---|---|---|
| 0 | 0.083316 | 0.083333 | | | 1/12 (exact) |
| 2 | 0.893744 | 0.894167 | 0.8941601 | 0.8941664 | 0.894 |
| 3 | 3.635360 | 3.637476 | 3.6374393 | 3.6374710 | 3.635 |
| 4 | 15.699205 | 15.709787 | 15.7095991 | 15.7097575 | 15.70 |

- So the file's numbers are the truncated sums, and m2 applies.
- The factors against C_(S³)²𝔭_r = 2353/12, 11773/12 and 37057/12 (196.08, 981.08, 3088.08) are 219, 270 and 197, as stated.

### 4. lem:tl5-hft-face (the norm comparison)

- **The norm inequalities:** |A| ≤ 𝔴₀^r|A|₀ and |A|₀ ≤ 𝔳₀^r|A|, by the slotwise change of frame. The operator norms are 𝔳₀ and 𝔴₀, and the Frobenius estimate is the one of lem:tl5-hf-khat.
- **ℒ_(∂_γ)h₀ = 0:** α, β and ρ are constant, ∂_γ = ∂_v − κ′∂_u has constant coefficients and γ₀ does not depend on (u, v). So (d/dv)|B|₀² ≤ |B|₀² + |ℒ_(∂_γ)B|₀², and ℒ_(∂_γ) commutes with ℒ^J.
- **(a)–(c) and eq:tl5-hft-cs:** these follow, with 6C_(E,r)² for 6C_(S³)²𝔭_r = 𝔭_r/2.
- **The derived constants:**
  - C₁: 258 = 6·43;
  - C_(1,0): 516π² = 6·43·2π²;
  - C_(0,0) = 86π²C_(S,0)²;
  - level 4: 12C_(E,r)² for 𝔭_r in 𝔛, and 𝔳₀ in 𝔱_r, 𝔵_r and [𝔳^(2r)]_t.
- **The matrix M** is checked entry by entry from ĝ, with ê₃ = ∂_u + b̂∂_x, ê₄ = ∂_v and k equal to the identity in (E₀, E₁, f_j):
  - **Leaf vectors:** k = ĝ on leaf vectors, which are k-orthogonal to ê₃ and ê₄.
  - **The diagonal:** k(ê₃, ê₃) = 2Ω̂²/c, k(ê₄, ê₄) = 2cΩ̂² and k(ê₃, ê₄) = 0. So k(∂_u, ∂_u) = 2Ω̂²/c + b̂²e^(2ζ) and k(∂_v, ∂_v) = 2cΩ̂².
  - **The off-diagonal:** k(∂_u, ∂_x) = −b̂e^(2ζ). With e_x = 2(1−x²)^(1/2)∂_x and e^ζ·2(1−x²)^(1/2) = Re^(−(P+Q)), this gives M_ux = −b̂e^ζRe^(−(P+Q))/(αρ).
  - **The leaf entries:** M_xx = R²e^(−2(P+Q))/ρ², M_11 = R²e^(2P)/ρ² and M_22 = R²e^(2Q)/ρ².
  - **The zeros:** all other entries vanish.
- **The extreme norms:** 𝔳₀² = λ_max(M) and 𝔴₀² = 1/λ_min(M).
- **The seed point:** b̂ = 0, P = Q = 0, α² = 2Ω̂²/c, β² = 2cΩ̂² and ρ = R give M = I, so the condition number is 1 there.
- **Every listed constant** C_S^E, C_(S,0)^E, C_(0,0)^E, C₁^E, C_(1,0)^E, C_(1,ϱ)^E and the level-4 replacements is the merged formula with these substitutions.
- **Two small points:**
  - At level four, α, β and ρ must be the same on all faces Σ₁(t, b) with one t, because the brackets [·]_t are suprema over Σ₁(t, v*) (n2).
  - The Comparison lists C_(1,0)^E only with Λ₂, but option (b) needs C_(1,0)^♮ with Λ₂^μ (n4).

### 5. thm:tl5-hft and thm:tl5-hf4t

- **The constants:** for N ≥ 6, ε_(M,s) = S_(M,s) = 0, so A_t = √2δ_w + 2ε_(w,t), B_t = 2S_(F,s) and 𝔯_t = 𝔯_(w,s). That gives eq:tl5-hft-closing. At level 4, A_t and B_t give eq:tl5-hf4t-closing.
- **Step 1:** in either option, ℰ_g(p) ≤ e^(φ(p))Y_σ² ≤ 4e^(φ(p))A_t² yields 𝔰(p) ≤ 𝔰_(*,t). The bound 𝔰₁^t is at most half the threshold, c_*κ_m/2 and 𝔰_θ.
- **(H2):**
  - 𝔰₁^t ≤ 𝔰_♭/2 ≤ 1/16 in both options.
  - In option (b) at level four, eq:tl5-hf4-m2 (which needs 𝔰 ≤ 𝔰₀^♮) is rightly replaced by |D̂²Ψ_B| ≤ μ^(−2)(2(k₁^μ+1)𝒥₁ + 2k₂ϱ), |B| ≤ 3, from M_g^(3). P(4) of lem:tl5-hf4-persistence needs only a bound by a constant.
  - At N ≥ 6, lem:tl5-hf-persistence uses no bound of M₂.
- **Citations:** every citation is within its range of N.
- **Earlier conditions:** the earlier closing conditions stay valid; nothing earlier is changed.

**Overclaim.** The chapter claims only what is proved:
- the two options of the smallness;
- the intrinsic Sobolev inequality as an alternative choice ("any of them may be used");
- that the hypotheses are established for no background.

The Comparison marks the word count and 𝔠^M₁ as not done, which is right. Two wording points:
- The remark says 𝔜 carries 6C_(E,r)², but 𝔜 carries only 𝔳₀ (n1).
- The Placement's line reference is off by one (n3).

## Major

None.

## minor

### m1. The Casimir eigenvalue is asserted, not proved (lines 37–40)

**Where.** "on V_π it is the number c_π := 2j₁(j₁+1) + 2j₂(j₂+1), as so(4) is the sum of two copies of su(2) in which Σ_(a<b) K_ab² is twice the sum of the two Casimir operators of su(2) (on the representation ℝ⁴ = (1/2, 1/2) both sides are −3, … and on the functions of degree n, (n/2, n/2), they are −n(n+2) …)".

**Why it is a gap.**
- The degree-2 centre is spanned by the two su(2) Casimirs, so Σ K_ab² = x C₊ + y C₋.
- Both checks have j₁ = j₂, so they determine only x + y = 4. The claim x = y = 2 is left unproved, and the constants C_(E,r) depend on it whenever j₁ ≠ j₂.
- The edition must prove each step (STYLE §1).

**Why the result is still right.** The 't Hooft decomposition proves it in one sentence, and I verified it exactly: brackets [J₁^±, J₂^±] = −J₃^± and [J⁺, J⁻] = 0, and Σ K_ab² = 2Σ(J⁺² + J⁻²).

**Fix:** R1.

### m2. The Comparison's C_(E,r)² are truncated sums, not upper bounds (lines 273–274; not chapter text)

**Where.** "C_(E,2)² ≈ 0.894, C_(E,3)² ≈ 3.635, C_(E,4)² ≈ 15.70 … (computed, series summed to 2j₁ < 3000)".

**Why.**
- These are the partial sums 0.89374, 3.63536 and 15.6992.
- The true values are 0.89416, 3.63744 and 15.7096. For r = 3 and r = 4 the quoted numbers lie below them by more than rounding.
- The evaluation will put these numbers into sufficient conditions, so they must be upper bounds.
- The tail has a simple rigorous bound, 5^r/(2π²(N − 2r)) (derived in §3 above).

**Fix:** C1.

## Nits

- **n1 (lines 209–211).** "at level four also 𝔛 and 𝔜, carries 6C_(E,r)² and the operator norms": 𝔜 comes from lem:tl5-hf4-face (a), not from a Sobolev inequality on S³. It carries 𝔳₀ but not 6C_(E,r)². The same holds for 𝔪, with 𝔴₀. Fix: R2.
- **n2 (lines 55–57).** α, β and ρ are "fixed for each face Σ₁(a, b)". In (c) the brackets 𝔵_r(t), 𝔱_r(t) and 𝔪(t) are suprema over Σ₁(t, v*) for every face Σ₁(t, b), so h₀ must be the same for all b with one t. Fix: R3.
- **n3 (Placement, line 225).** "(line 5758, as changed by item 2)": item 2 adds a line, so the remark then ends at line 5759. This is the same nit as R-P-GRD2's n5. Fix: R4.
- **n4 (Comparison, line 287).** C_(1,0)^E is given with Λ₂ only. Option (b)'s C_((∞,0),μ) uses C_(1,0)^♮, with Λ₂^μ. Fix: C2.

## Observations (no change required)

- **O1.** Option (a) leaves A_t and B_t equal to those of sec:tl5-hfs: it changes only the constant of the A-term of 𝔰_(*,t). Option (b) trades a larger threshold 𝔰₁^t for μ^(−N/2) on the ϱ and η₀ terms. Neither option changes S_(F,s), S_(M,s), 𝔯_s or ε_(M,s).
- **O2.** On b = 0 monomials, the ϱ term of lem:tl5-hft-products (μ^(−1/2)𝔠^♮_n(μ)) is weaker than that of lem:tl5-hfs-products (μ^(n/2)𝔠^♮_n). That is the price of option (b), and it is correctly carried into ε_(w,t).
- **O3.** The convergence bound in the proof (5^r(2j₁ + 2r + 1)²/(2j₁²)², for 2r + 1 values of j₂) is crude but valid. The bound m/((2j₁+1)(2j₂+1)) above would give the tail directly.

## Replacement texts

Each old text occurs exactly once. Each block replaces whole lines, with the line breaks shown. R4 replaces a span; C1 and C2 replace lines of the Comparison.

### R1 (m1), lines 37–40

Old:

    the invariant form for which the K_ab are orthonormal; on V_π it is the number c_π := 2j₁(j₁ + 1) + 2j₂(j₂ + 1), as
    so(4) is the sum of two copies of su(2) in which Σ_(a<b) K_ab² is twice the sum of the two Casimir operators of su(2)
    (on the representation ℝ⁴ = (1/2, 1/2) both sides are −3, each K_ab² being minus the projection onto its plane, and
    on the functions of degree n, (n/2, n/2), they are −n(n + 2), the eigenvalue of the Laplacian of γ₀).

New:

    the invariant form for which the K_ab are orthonormal; on V_π it is the number c_π := 2j₁(j₁ + 1) + 2j₂(j₂ + 1).
    Indeed, with L₁ := K₂₃, L₂ := −K₁₃, L₃ := K₁₂ and M_i := K_(i4), the fields J_i^± := (L_i ± M_i)/2 satisfy
    [J₁^±, J₂^±] = −J₃^± and the cyclic relations, and [J_i⁺, J_l⁻] = 0; so they span the two copies of su(2) in so(4),
    of spins j₁ and j₂ on π, −Σ_i (J_i⁺)² and −Σ_i (J_i⁻)² are j₁(j₁ + 1) and j₂(j₂ + 1) on V_π, and Σ_(a<b) K_ab² =
    Σ_i (L_i² + M_i²) = 2 Σ_i ((J_i⁺)² + (J_i⁻)²). (On the representation ℝ⁴ = (1/2, 1/2) both sides are −3, each K_ab²
    being minus the projection onto its plane, and on the functions of degree n, (n/2, n/2), they are −n(n + 2), the
    eigenvalue of the Laplacian of γ₀.)

### R2 (n1), lines 209–211

Old:

    ε_(w,t). With the Sobolev constants of [[lem:tl5-hft-face]], every constant formed from the Sobolev inequality on a
    face, at level four also 𝔛 and 𝔜, carries 6C_(E,r)² and the operator norms 𝔳₀, 𝔴₀ of the comparison of k with h₀ in
    place of 6C_(S³)² 𝔭_r and the Euclidean component norms 𝔳, 𝔴; the numbers α, β, ρ of h₀ are free for each face. As for

New:

    ε_(w,t). With the Sobolev constants of [[lem:tl5-hft-face]], every constant formed from the Sobolev inequality on a
    face, at level four also 𝔛, carries 6C_(E,r)² in place of 6C_(S³)² 𝔭_r, and these constants, 𝔜 and 𝔪 carry the operator
    norms 𝔳₀, 𝔴₀ of the comparison of k with h₀ in place of the Euclidean component norms 𝔳, 𝔴; the numbers α, β, ρ of h₀
    are free for each face. As for

### R3 (n2), lines 56–57

Old:

    with numbers α, β, ρ fixed for each face Σ₁(a, b), and at each point let 𝔳₀ := sup |X|/|X|₀ and 𝔴₀ := sup |X|₀/|X| over
    the nonzero vectors X, |X| the norm of k. Then:

New:

    with numbers α, β, ρ fixed for each face Σ₁(a, b), in (c) the same for all the faces Σ₁(t, b) with one t, and at each
    point let 𝔳₀ := sup |X|/|X|₀ and 𝔴₀ := sup |X|₀/|X| over the nonzero vectors X, |X| the norm of k. Then:

### R4 (n3), Placement item 1 (a span of line 225)

Old: `(line 5758, as changed by item 2)`. New: `(line 5759 once item 2 is applied)`.

### C1 (m2), Comparison, lines 273–274

Old:

                     C_(E,2)² ≈ 0.894, C_(E,3)² ≈ 3.635, C_(E,4)² ≈ 15.70, C_(E,0)² = 1/12 (computed, series summed to
                     2j₁ < 3000), against C_(S³)² 𝔭_r = 196.1, 981.1, 3088.1: factors 219, 270, 197 in the squares;

New:

                     C_(E,2)² ≤ 0.8942, C_(E,3)² ≤ 3.6375, C_(E,4)² ≤ 15.710, C_(E,0)² = 1/12: the sums over 2j₁ < 3000
                     are 0.89374, 3.63536, 15.6992 (computed), and the tail is at most 5^r/(2π²(3000 − 2r)), as each term
                     is at most m_(j₁j₂)(r)/((2j₁ + 1)(2j₂ + 1)) and Σ_(j₂) m_(j₁j₂)(r) ≤ 5^r (the values are 0.89416,
                     3.63744, 15.7096); against C_(S³)² 𝔭_r = 196.1, 981.1, 3088.1: factors 219, 270, 197 in the squares;

### C2 (n4), Comparison, line 287

Old:

                     C_(1,0)^E² = 516π² C_(E,3)² 𝔴₀(p)⁶ sup_(S_a) 𝔳₀⁶ (1 + 6Λ₂)²;

New:

                     C_(1,0)^E² = 516π² C_(E,3)² 𝔴₀(p)⁶ sup_(S_a) 𝔳₀⁶ (1 + 6Λ₂)²  (with Λ₂^μ for C_(1,0)^♮, option (b));

## The replacements, checked together

All of R1–R4, C1 and C2 were applied by scratchpad/reader/rpgrd3/tools/fix.py. Each old text was found exactly once.

**Crosswalk.** The rows' line numbers were then updated to the new label lines: 1, 12, 17, 22, 58, 67, 90, 96, 104, 132, 145, 156, 158, 163, 179, 184, 192, 196, 206.

**Result.** scratchpad/reader/rpgrd3/P-GRD3.fixed.md, md5 88c8d48fa7ae99695c536c90a17ad66c, 345 lines; the chapter text is lines 1–217.

**Checks.** The copy was merged into a fresh archive of HEAD with the same two items:
- lint.py --chapters: 62 files, 5207 labels, 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: prints `[] 0`.
- Longest source line: 121 characters. No wrapped line starts with a forbidden marker.
- Crosswalk: the 19 updated rows, appended in order, give 363 rows equal to the 363 labels.

Verdict: NOT CONFIRMED
