# R-P-GRD4: independent reading of proofs/P-GRD4.md (the constants at level four sharpened a fourth time, sec:tl5-hfq)

**File read:** proofs/P-GRD4.md, md5 fa9f162d14a407c6666bd0e90bb99ed7, 267 lines. Its parts:
- chapter text, lines 1–155 (sec:tl5-hfq, 14 labels);
- Placement, lines 157–183;
- Comparison, lines 185–245;
- crosswalk rows, lines 247–267.

I read every line and every proof in full.

**Also read:**
- notes/reports/P-GRD4.md;
- notes/reports/G0f.md, for the figures the Comparison cites;
- notes/reviews/C-P-GRD3.md;
- the merged sec:tl5-hft (87:5760–5977), which differs from my P-GRD3.fixed.md only by the confirming reader's C1′, R2′ and C3′;
- sec:tl5-hfs, sec:tl5-hfg and sec:tl5-hf4, for every step reused.

**Line numbers** are those of P-GRD4.md unless marked "87:".

**Repository state:**
- HEAD is 82aa2785.
- Chapter 87 (md5 6fb0d2cf…) last changed at 1b8a7d43, so the Placement's quotations are current.
- I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/rpgrd4/.

## Verdict

**NOT CONFIRMED** — 0 Major, 1 minor, 4 nits. Every number in the Comparison is right.

**What is right.** Every statement of the chapter text is true and every proof is complete, except one passage:
- the exact count of the level-four products;
- the θ-family of absorptions;
- the three constants of lem:tl5-hfq-mixed;
- the bootstrap and thm:tl5-hf4q.

**The one minor (m1).** In the proof of eq:tl5-hfq-small (lines 65–72), two sentences do not prove what the constant needs:
- "with a factor 2 for H" in a_Φ, read literally, makes "max_Φ a_Φ ≤ μ^(−N/2)" false for μ > 1/2 at N = 4. The factor 2 is in fact absorbed by the 2C_S and 2C_(0,0) of the constants.
- "the parts with η₀(p) of … D̂Ψ_B are bounded unweighted, and 1 ≤ r_Φ" gives C_(1,0) with Λ₂. eq:tl5-hfq-small, however, carries the constant formed with ν, which has Λ₂^ν ≤ Λ₂.

The inequality does hold, by a one-line weighted bound on S_a (R1).

**The fixed copy** is scratchpad/reader/rpgrd4/P-GRD4.fixed.md, md5 8f464d0b5a7702cab0486aad721dbf15, 273 lines. It has all replacements applied and the crosswalk line numbers updated. It is checked in the last section.

## Checks on the file as submitted (scratch merge)

**Scratch tree:** a git archive of HEAD 82aa2785 in scratchpad/reader/rpgrd4/tree.
- Item 2's old text occurs exactly once, at 87:5976–5977.
- After item 2 the remark ends the chapter, at line 5978. The section is appended there with one blank line.

**Results:**
- lint.py --chapters: 62 files, 5221 labels (5207 + 14), 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: prints `[] 0`.
- Lines are at most 121 characters, in the source and after labels resolve.
- No wrapped line starts with a forbidden marker ("- " checked by hand).
- No printed number of the 5207 old labels changes. The section is Section 57.19, thm:tl5-hf4q is Theorem 57.191 and rem:tl5-hfq-what is Remark 57.192.
- Crosswalk: 14 rows, complete, in chapter order, with matching lines. Appended, the 377 rows equal the 377 labels in order.
- Format: the chapter text has no file or program names, no code and no AI language. Labels are lowercase.

## The points briefed, checked

### 1. lem:tl5-hfq-m

**b = 0.**
- The two high factors of a monomial of 𝔑^M_I have orders 3 and 3. With |I| = 4 and o₁ + o₂ ≤ n − b + 2 (lem:tl5-hfs-quadratic (b)), b = 0.
- So every factor carrying letters is one of the two high factors. Factors ĝ⁻¹ and R̂ carrying letters would be background factors, and none occurs.
- A factor g⁻¹ carrying letters gives blocks Ψ_(B_i) only. Two blocks would both have to be high, which needs 6 letters. So the only possibility is r = 1, |B| = 3, that is −g⁻¹Ψ_Bg⁻¹. The proof states exactly this.

**Is μ-weighting [𝔠^(3♮)₄]_t useless?** On the monomials of 𝔑^M, μ^(b/2) = 1, so the weighting does not act on them.
- It would still lower the old bound, by damping the b > 0 monomials that 49𝔰_♭[𝔠^(3♮)₄]_t overcounts. The bound 49𝔰_♭[𝔠^(3♮)₄(μ)]_t is valid.
- The Comparison's wording ("cannot act on them … weights a constant whose b > 0 monomials are not in 𝔑^M at all") is accurate.
- The exact count dominates even the fully weighted old bound. At Λ_a ≡ 0 for a ≥ 1 and |R̂| = 1, 49𝔠^(3♮)₄ = 4.16·10⁶ (𝔰_♭ = 10⁻⁸) or 7.79·10⁶ (𝔰_♭ = 1/8). The exact count's coefficient is 96𝔤₁(𝔤₀+√5) = 453 or 567. I computed these in rpgrd4/calc.

**Completeness of the enumeration.** I went through every term of N(h) = Q + R₃:

**Q:**
- H₁^(λσ)D̂_λD̂_σh with three letters on h and one on D̂²h. The letter on D̂²h must give D̂²Ψ_Z, since the remainder would have b ≥ 1. This contributes coefficient 1, for 4 sets S.
- 2𝔮̂ with two letters on each D̂h. Again the remainders are excluded. The bound is 16·√5², for 6 sets S.
- 2𝔠(H₁)h has no derivative, and two high Ψ's would need 6 letters. It contributes nothing.
- The remaining letter distributions give at most one high factor.
- So Q gives 480P₁ + 4P₂, as in lem:tl5-hfs-quadratic (c).

**R₃, the term H₂D̂²h with H₂ = g⁻¹hĝ⁻¹hĝ⁻¹:** the derivative pair must be D̂²Ψ₁ (from D̂²h) with Ψ₃. That Ψ₃ comes from the first h, from the second h, or from the g⁻¹ block. Neither ĝ⁻¹ can supply it, since that would make b ≥ 1. The three bounds are:
- first h: the g⁻¹ joins D̂²Ψ to Ψ (𝔤₁), the two ĝ⁻¹ cost 1, and the other h is at most 𝔰. This gives 𝔤₁𝔰.
- second h: likewise 𝔤₁𝔰.
- the block −g⁻¹Ψ_Bg⁻¹: two g⁻¹, each joining distinct factors (𝔤₁ each), and two h. This gives 𝔤₁²𝔰².

So each S gives 2𝔤₁𝔰 + 𝔤₁²𝔰², and the four sets S give 4𝔤₁𝔰(2 + 𝔤₁𝔰) times P₂.

**R₃, the term 2𝔠(H₂)h:** it has no derivative, and two high Ψ's would need 6 letters. It contributes nothing.

**R₃, the terms 2𝔮 − 2𝔮̂ = Σc_m(𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹, H, D̂h, D̂h)):**
- The only derivatives are the two D̂h. A Ψ₃ (from h, or from a g⁻¹ block in H or in the slot g⁻¹) would be paired with D̂Ψ₁, which has order 2 and is low.
- So the only pair is D̂Ψ_(I_S)·D̂Ψ_(I_(S^c)), |S| = 2, with H and the inverse metric slot carrying no letter.
- |H| ≤ 𝔤₁|h|, and H enters as a tensor, so even a trace costs only |H|.
- The slot g⁻¹ costs at most 𝔤₀ (it may be a trace), and the slot ĝ⁻¹ costs at most √5.
- Σ|c_m| = 16, which gives 16𝔤₁𝔰(𝔤₀ + √5). The six sets S give 96𝔤₁(𝔤₀ + √5)𝔰 times P₁.

No monomial is missed.

**The sum over words.** For fixed S, I ↦ (I_S, I_(S^c)) is a bijection. Minkowski's inequality over S, applied to the Q and R₃ parts together, then gives eq:tl5-hfq-m.

**The numbers, recomputed at 30 digits:**

| 𝔰_♭ | 𝔠^Mq₁ | 𝔠^Mq₂ |
|---|---|---|
| 1/8 | 550.832039… | 5.34765625 |
| 10⁻¹⁰ | 480.0000000453 | 4.0000000008 |

- Both coefficients increase with 𝔰_♭, so 𝔠^Mq₁ ≤ 551 and 𝔠^Mq₂ ≤ 5.35 for every 𝔰_♭ ≤ 1/8.
- 96𝔤₁(𝔤₀+√5)𝔰_♭ ≤ 70.84 ≤ 71.

**The replacement is legitimate.** eq:tl5-hfq-m bounds the same quantity (Σ_I|𝔑^M_I|²)^(1/2) that eq:tl5-hfs-m bounds. Its coefficients do not depend on the background, so no face supremum is needed, and it holds wherever 𝔰(p) ≤ 𝔰_♭.

### 2. lem:tl5-hfq-theta

**The setting.** k₃^♮(·) is nondecreasing, since 𝔠^♮_n(ν) and ν^((|C|−|J|)/2) increase with ν. So 𝔰 ≤ 𝔰₀^q gives 𝔰 ≤ 𝔰₀^μ, and lem:tl5-hft-small (b) and lem:tl5-hft-products apply.

**eq:tl5-hfq-m2, by induction on |C|.** The induction uses R_C := 2(k₁^(j,μ)+1)μ^(−(|C|+1)/2)𝒥_g + 2k₂ν^(−(|C|+1)/2)ϱ.
- **Linear part:** it is at most k₁^(j,μ)μ^(−(|C|+1)/2)𝒥_g + k₂ϱ, and k₂ϱ ≤ k₂ν^(−(|C|+1)/2)ϱ.
- **Nonlinear part, a monomial of ℒ^J N(h), |J| ≤ |C|, with b background letters:**
  - H, Ψ_(C′) and D̂Ψ_(C′) have |C′| ≤ |J| − b, so they are at most 2μ^(b/2)μ^((|C|−|J|)/2)μ^(−(|C|+1)/2)𝒥_g.
  - D̂²Ψ_(C′), with |C′| ≤ |J| − b and |C′| < |C|, is bounded by R_(C′). This gives μ^(b/2)μ^((|C|−|J|)/2) on the 𝒥_g part and ν^(b/2)ν^((|C|−|J|)/2) on the ϱ part.
  - H D̂²Ψ_J has b = 0 and coefficient 𝔰.
- **Absorption:** eq:tl5-hfs-sum with ν′ = μ bounds the 𝒥_g part, and with ν′ = ν the ϱ part. Then k₃^♮(μ)𝔰 ≤ k₃^♮(ν)𝔰 ≤ 1/2 gives the bound by (R_C)/2 + (R_C)/2 = R_C.
- **The ϱ part:** this shows that the ϱ part of D̂²Ψ_C carries (μ^θ)^(−(|C|+1)/2).

**eq:tl5-hfq-small.**
- **Ψ_B:** μ^(−(|B|+2)/2)C_Sℰ_g^(1/2) + C_(0,0)η₀ ≤ a_Φ𝔈 + r_Φℜ, as (1/2)C_(∞,μ) ≥ 2C_S and (1/2)C_((∞,0),ν) ≥ 2C_(0,0).
- **D̂Ψ_B:**
  - The ℰ_g part gives C₁^♮(μ), with Λ₂^μ and k₁^μ.
  - The ϱ part of D̂²Ψ_(JB) is 2k₂ν^(−(|JB|+1)/2)ϱ ≤ 2k₂ν^(−(|B|+3)/2)ϱ, which gives r_Φ C_(1,ϱ).
  - The η₀ part on S_a is where the written step is wrong (m1).
- **D̂²Ψ_B:**
  - The jets carry the weights μ in their ℰ parts and ν in their ϱ and η₀ parts, which gives k₁^(N−4,μ) and k₁^(N−4,ν).
  - k₂ϱ ≤ r_Φk₂ϱ.
  - The nonlinear factor of largest order has a_(Φ′) ≤ μ^(b/2)a_Φ and r_(Φ′) ≤ ν^(b/2)r_Φ, with the extra μ^((|B|−|J|)/2) of 𝔔 available.
- **The fixed-point step:** t ≤ 1 + t/2 is sound, since t is a finite maximum. If 𝔈 = ℜ = 0, everything vanishes by induction.
- **The conclusion:** max a_Φ ≤ μ^(−N/2) and max r_Φ ≤ ν^(−N/2), once the factor 2 for H is dropped (m1).

**The products.**
- The ϱ term of a monomial is μ^(n/2)ν^(−ℓ_E/2) = μ^((1−θ)n/2)ν^((n−ℓ_E)/2).
- For b ≥ 1, n − ℓ_E ≥ b − 1. For b = 0, n − ℓ_E ≥ 0. So the ϱ term is at most μ^((1−θ)n/2)ν^(−1/2)ν^(b/2), which gives the first replacement.
- H D̂²Ψ_J gives μ^((n−|J|)/2)μ^((1−θ)|J|/2)ν^(−1/2), which gives the second.
- In Step 2, μ^((j−j′)/2)μ^((1−θ)j′/2) = μ^((j−θj′)/2). With the weights μ^j this gives 𝔤_(ϱ,q) as stated.

**ε_(w,q).** Both bounds of the ϱ forcing hold pointwise under 𝔰 ≤ 𝔰₀^q: the θ bound, and option (b)'s μ^(−1/2)𝔤_(𝒥,s), which holds since 𝔰 ≤ 𝔰₀^μ. So the pointwise minimum is valid.

**θ = 0 and θ = 1 recover the two options.**
- **θ = 0, ν = 1:**
  - k₃^♮(1) = k₃^♮, so 𝔰₀^q = 𝔰₀^♮ and 𝔰₁^q = 𝔰₁^♮.
  - C_((∞,ϱ),1) = C_(∞,ϱ) and C_((∞,0),1) = C_(∞,0) of eq:tl5-hfg-cinf, since Λ₂^1 = Λ₂ and k₁^(m,1) = k₁^(m). So 𝔰_(*,q) is option (a)'s 𝔰_(*,t).
  - 𝔤_(ϱ,q) = 𝔤_(ϱ,s).
  - The two products replacements reduce to those of lem:tl5-hfs-products.
- **θ = 1, ν = μ:**
  - 𝔰₀^q = 𝔰₀^μ, 𝔰_(*,q) is option (b)'s, and 𝔤_(ϱ,q) = μ^(−1/2)𝔤_(𝒥,s).
  - The replacements are those of lem:tl5-hft-products.
- **What changes in either case:**
  - Because of the minimum, ε_(w,q) is at most both options' ε.
  - S_(M,q), 𝔯_(M,q) and ε_(M,q) improve on S_(M,s), 𝔯_(M,s) and ε_(M,s) by lem:tl5-hfq-m and lem:tl5-hfq-mixed.

**The hybrid ((b)'s threshold with (a)'s ϱ requirement) is a limit of this proof only, and it is worded as such** ("not given by this proof", marked deduced).
- In the nonlinear terms, the ϱ part of a factor D̂²Ψ_(C′) gains ν^(b/2) only through its own power ν^(−(|C′|+1)/2).
- So the background norms Λ_b that multiply it are damped by ν^(b/2) and no further. Absorbing it needs k₃^♮(ν)𝔰 < 1, and a threshold formed with μ forces ν = μ.
- Getting past this would take a bound of the residual's share of D̂²Ψ that gains in b differently. Nothing in the chapter text claims more.

### 3. lem:tl5-hfq-mixed

**𝔛^q₁ without 49.**
- For fixed J and a fixed monomial type of R′ in ℒ^J D̂Ψ_B, the solution factor is Ψ_(σB), with σ fixed. B ↦ σB is injective, and the coefficient depends on J only.
- Also μ⁴ ≤ μ^a μ^(|σB|), since |σB| + a = |JB| ≤ 4.
- So μ²(Σ_B|monomial_B|²)^(1/2) ≤ μ^(a/2)Λ_a𝒥_g. Minkowski's inequality over the monomials gives ρ′_(|J|)𝒥_g.
- Then μ⁴Σ_BΣ_J|ℒ^JD̂Ψ_B|² ≤ 2𝒥_g² + 2ϖ₁𝒥_g², and X₁² ≤ (1/2)𝔭₃𝔵₃·2(1 + [ϖ₁]_t)𝔍_g² gives 𝔛^q₁.

**𝔛^q₂ without the 7.**
- The remainders of ℒ^J D̂²Ψ_Z have solution factors D̂Ψ_(σZ) or Ψ_(σZ), and Z ↦ σZ is injective. This gives 2ϖ₂ in place of 14ϖ₂.
- The term 2·7·43 M_g² = 602 M_g² comes from the D̂²Ψ_(JZ), |JZ| ≤ 3, each bounded by M_g = M_g^(3). It stays, and √602 λ_t^μ, with the top-level constant, is correct there.

**𝔜^q₁ with the level-2 constant.**
- The bound of Y₁ = Σ_(|B|=2)⟦D̂Ψ_B⟧_(∞,2)² involves D̂(D̂Ψ_B) = D̂²Ψ_B with |B| = 2 only.
- μ^(3/2)|D̂²Ψ_B| = μ^((|B|+1)/2)|D̂²Ψ_B| ≤ M_g^(2) ≤ 2(k₁^(2,μ)+1)𝒥_g + 2k₂ϱ, by lem:tl5-hft-small (b) with j = 2, which applies since 𝔰₀^q ≤ 𝔰₀^μ.
- So λ_t^(μ,2) is enough where it is used. 𝔜′₁, with ς_t, is unchanged.

**One citation is missing.** X₂ still needs ‖M_g^(3)‖_Σ ≤ λ_t^μ𝔍_g + ς_tϱ under 𝔰 ≤ 𝔰₀^q. That bound holds by lem:tl5-hfq-theta (through lem:tl5-hft-products), but "The rest of that proof holds as written" does not say so (n4).

### 4. thm:tl5-hf4q

**The constants.** A_q = √2δ_w + 2ε_(w,q) + 2ε_(M,q), B_q = 2(S_(F,s) + S_(M,q)) and 𝔯_q = 𝔯_(w,s) + 𝔯_(M,q). So 4A_qB_q is eq:tl5-hf4q-closing.

**S_(F,s) and 𝔯_(w,s)** are valid under the weighted absorption: Steps 2 and 3 of option (b) hold, since 𝔰 ≤ 𝔰₀^μ.

**The 𝔑^M term.** It is the expansion of [𝔠^Mq₁](μ²X₁)(μ^(3/2)Y₁) + [𝔠^Mq₂](μ²X₂)(μ^(3/2)Y₂), with the new 𝔛^q and 𝔜^q, and 𝔍_g ≤ [𝔨₂]_t^(1/2)Y_s. This gives S_(M,q), 𝔯_(M,q) and ε_(M,q) exactly.

**Step 1.** It holds with eq:tl5-hfq-small, since 𝔰₁^q ≤ 𝔰₀^q/2.

**(H2).** It uses:
- 𝔰₁^q ≤ 𝔰_♭/2 ≤ 1/16;
- Y_σ ≤ 2A_q;
- the bound of M_g^(3) from lem:tl5-hft-small (b), which holds since 𝔰 ≤ 1/(2 sup k₃^♮(μ)), and which replaces eq:tl5-hf4-m2 in lem:tl5-hf4-persistence.

**Earlier closing conditions.** The section is additive, so all earlier closing conditions stay valid. They are those of thm:tl5-hf, thm:tl5-hf4, thm:tl5-hfg, thm:tl5-hf4g, thm:tl5-hfs, thm:tl5-hf4s, thm:tl5-hft and thm:tl5-hf4t.

**Citation ranges.** Every citation is within its range of N. lem:tl5-hfq-theta is stated for N ≥ 4, and the rest for N = 4.

## Every number of the Comparison

**Closing condition and smallness (190–196):** they agree with the chapter text.

**Formulas (198–220):** every formula agrees with the chapter text:
- 𝔠^Mq₁, 𝔠^Mq₂, 𝔤₁ and 𝔤₀;
- k₃^♮(ν), 𝔰₀^q and 𝔰₁^q;
- 𝔰_(*,q);
- C_(∞,μ)^(0) = 2max(2C_S, C₁^♮(μ), 4k₁^(0,μ)max(C_S, C₁^♮(μ))), with (2𝔐^(0))^(1/2) = √16 = 4;
- C_((∞,ϱ),ν)^(0) and C_((∞,0),ν)^(0);
- k₁^(j,ν) and α_𝔄^(j,ν), with α^(0,ν) = 0;
- 𝔤_(ϱ,q) and ε_(w,q);
- λ_t^(μ,2), 𝔛^q₁, 𝔛^q₂ and 𝔜^q₁;
- S_(M,q), 𝔯_(M,q) and ε_(M,q);
- A_q, B_q and 𝔯_q.

**"C₁^♮(ν), C_(1,0)^♮(ν): C₁, C_(1,0) with Λ₂^ν and k₁^(3,ν)"** is a generic notation. It gives C₁^♮(μ) as used, and C_(1,0) has no k₁ in it, so this is harmless.

**"Computed: at 𝔰_♭ = 10⁻¹⁰ these are 480 and 4 to nine digits; at 𝔰_♭ = 1/8, 550.8 and 5.35":** right (480.0000000453, 4.0000000008; 550.832, 5.348).

**Item 1:**
- "96𝔤₁(𝔤₀ + √5)𝔰_♭ ≤ 71" and "𝔠^Mq₁ ≤ 551 for every 𝔰_♭ ≤ 1/8" are right (70.83 and 550.83).
- "49𝔰_♭[𝔠^(3♮)₄]_t (10^5.0–8.0 at G0f's optimum)" matches G0f (notes/reports/G0f.md, lines 173–174 and 208). G0f gives [𝔠^M₁]_t = 480 + 49𝔰_♭[𝔠^(3♮)₄]_t as 10^5.0–8.0, and the 480 is negligible at these sizes (log₁₀(10⁵ − 480) = 4.998).

**Item 3:**
- "G0f's 2.1 decades sit in 1 + 7λ_t^μ" matches G0f line 212.
- "up to 0.85 decades" is log₁₀7 = 0.845, the √49 in 𝔛₁.
- "2ϖ₂ in place of 14ϖ₂" and "602 = 2·7·43" are right.

**Item 2:** it states the endpoints and the trade correctly.

**No Comparison number is wrong.**

## Major

None.

## minor

### m1. The proof of eq:tl5-hfq-small (lines 65–72)

**First error.** "let a_Φ := μ^(−(o+2)/2) and r_Φ := ν^(−(o+2)/2) … (with a factor 2 for H, as |H| ≤ 2|h|)", then "max_Φ a_Φ ≤ μ^(−N/2), max_Φ r_Φ ≤ ν^(−N/2)".
- With a_H = 2μ^(−1), the maximum fails whenever 2μ^(−1) > μ^(−N/2). That is μ > 1/2 at N = 4, and μ > 2^(−2/3) at N = 5.
- No factor is needed: |H| ≤ 2μ^(−1)C_Sℰ_g^(1/2) + 2C_(0,0)η₀ ≤ μ^(−1)𝔈 + ν^(−1)ℜ already, because (1/2)C_(∞,μ) ≥ 2C_S and (1/2)C_((∞,0),ν) ≥ 2C_(0,0).

**Second error.** "the parts with η₀(p) of Ψ_B and D̂Ψ_B are bounded unweighted, and 1 ≤ r_Φ".
- For D̂Ψ_B, the unweighted bound on S_a, (1 + 6Λ₂)η₀, gives C_(1,0)^g.
- eq:tl5-hfq-small claims the constant formed with ν. That is C_(1,0) with Λ₂^ν = max(νΛ₁, ν^(3/2)Λ₂) ≤ Λ₂.
- "1 ≤ r_Φ" alone does not bridge the two.

**Why the result still holds.** The weighted bound on S_a does bridge them. A coefficient with a ≤ 2 letters is at most Λ_a ≤ ν^(−(|B|+3)/2)ν^((1+a)/2)Λ_a ≤ ν^(−(|B|+3)/2)Λ₂^ν, and |D̂Ψ_(JB)| ≤ η₀ ≤ ν^(−(|B|+3)/2)η₀. Equivalently, ν^(−(|B|+3)/2)(1 + 6Λ₂^ν) ≥ 1 + 6Λ₂. This is the bound of lem:tl5-hfs-linfty, and it is the form the D̂²Ψ_B step already uses for the jets.

**Fix:** R1.

## Nits

- **n1 (lines 78–79).** "at most ν 𝔰^(q−1) μ^(n/2) ν^(−ℓ_E(Φ₂)/2)": the first ν is a monomial's background norm, in the notation of the earlier products lemmas. Within this lemma, however, ν := μ^θ. Read with ν = μ^θ, the bound has the wrong power. The fix is R2.
- **n2 (lines 103–104).** 𝔰₁^q := min(…, 𝔰_θ) appears next to the new parameter θ. 𝔰_θ (def:tl5-hf-constants, formed with ϑ) does not depend on θ, and one clause says so. The fix is R3.
- **n3 (Placement, line 167).** "(line 5977, as changed by item 2)": item 2 adds a line, so the remark then ends at line 5978. This is the same nit as in R-P-GRD2 and R-P-GRD3. The fix is R5.
- **n4 (line 99).** "The rest of that proof holds as written" uses the bound of ‖M_g‖_Σ (top level) under 𝔰 ≤ 𝔰₀^q. That bound holds by lem:tl5-hfq-theta (through lem:tl5-hft-products), and the sentence should say so. The fix is R4.

## Observations (no change required)

- **O1.** The exact count makes 𝔰_♭ irrelevant for 𝔠^M: the R₃ part is at most 71 and 1.35 for every 𝔰_♭ ≤ 1/8. 𝔰_♭ still enters 𝔠^♮ (through 𝔰_♭𝔠^(3♮)) and caps 𝔰₁^q ≤ 𝔰_♭/2.
- **O2.** ε_(w,q) with the minimum is at most both options' ε. The pointwise minimum is legitimate, because both bounds hold at every point under 𝔰 ≤ 𝔰₀^q.
- **O3.** The θ-family is monotone in its two ends: the threshold k₃^♮(μ^θ) decreases with θ, and the factor μ^(−2θ) increases. The constants C_((∞,·),ν) also decrease with θ, through Λ₂^ν and k₁^(0,ν). So the evaluation's optimum over θ is genuinely interior in general.

## Replacement texts

Each old text occurs exactly once. Each replaces whole lines with the line breaks shown, except R5, which replaces a span.

### R1 (m1), lines 65–66 and 71–72

Old (65–66):

    For [[eq:tl5-hfq-small]] let a_Φ := μ^(−(o+2)/2) and r_Φ := ν^(−(o+2)/2) for a low quantity Φ of order o (with a factor 2
    for H, as |H| ≤ 2|h|). The steps of the proof of [[lem:tl5-hft-small]] (a), with [[eq:tl5-hfq-m2]] in place of

New:

    For [[eq:tl5-hfq-small]] let a_Φ := μ^(−(o+2)/2) and r_Φ := ν^(−(o+2)/2) for a low quantity Φ of order o (for H the
    factor 2 of |H| ≤ 2|h| is taken up by 2C_S and 2C_(0,0) in the constants). The steps of the proof of
    [[lem:tl5-hft-small]] (a), with [[eq:tl5-hfq-m2]] in place of

Old (71–72):

    and η₀(p), which gives k₁^(N−4,μ) and k₁^(N−4,ν); the parts with η₀(p) of Ψ_B and D̂Ψ_B are bounded unweighted, and 1 ≤
    r_Φ. Here 𝔫_Φ = 0 unless Φ = D̂²Ψ_B, and then 𝔫_Φ is the nonlinear part, whose factor Φ′ of largest order is a low

New:

    and η₀(p), which gives k₁^(N−4,μ) and k₁^(N−4,ν); the part with η₀(p) of Ψ_B is C_(0,0) η₀(p), with 1 ≤ r_Φ, and in that
    of D̂Ψ_B, on S_a, a coefficient of the remainder of ℒ^J D̂Ψ_B carrying a ≤ 2 letters is at most Λ_a ≤ ν^(−(|B|+3)/2)
    ν^((1+a)/2) Λ_a ≤ ν^(−(|B|+3)/2) Λ₂^ν, which gives r_Φ times the constant C_(1,0) formed with ν. Here 𝔫_Φ = 0 unless
    Φ = D̂²Ψ_B, and then 𝔫_Φ is the nonlinear part, whose factor Φ′ of largest order is a low

### R2 (n1), lines 78–79

Old:

    2k₂ ν^(−ℓ_E(Φ₂)/2) ϱ(p); so the term with ϱ(p) of a monomial with b background letters is at most ν 𝔰^(q−1) μ^(n/2)
    ν^(−ℓ_E(Φ₂)/2) 2k₂ ϱ(p), and ℓ_E(Φ₂) ≤ n − b + 1 for b ≥ 1, ℓ_E(Φ₂) ≤ n for b = 0, give μ^(n/2) ν^(−ℓ_E(Φ₂)/2) ≤

New:

    2k₂ ν^(−ℓ_E(Φ₂)/2) ϱ(p); so the term with ϱ(p) of a monomial with b background letters is at most its background norm
    times 𝔰^(q−1) μ^(n/2) ν^(−ℓ_E(Φ₂)/2) 2k₂ ϱ(p), and ℓ_E(Φ₂) ≤ n − b + 1 for b ≥ 1, ℓ_E(Φ₂) ≤ n for b = 0, give
    μ^(n/2) ν^(−ℓ_E(Φ₂)/2) ≤

### R3 (n2), lines 103–104

Old:

    [0, 1] and put ν := μ^θ, 𝔰₀^q as in [[lem:tl5-hfq-theta]] with the supremum over D^κ, 𝔰₁^q := min(𝔰₀^q/2, c_* κ_m/2,
    𝔰_θ), and, with the notation of [[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]],

New:

    [0, 1] and put ν := μ^θ, 𝔰₀^q as in [[lem:tl5-hfq-theta]] with the supremum over D^κ, 𝔰₁^q := min(𝔰₀^q/2, c_* κ_m/2,
    𝔰_θ), 𝔰_θ being that of [[def:tl5-hf-constants]], which does not depend on θ, and, with the notation of
    [[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]],

### R4 (n4), line 99

Old:

    ς_t ϱ takes the place of the bound of ‖M_g‖_Σ there. The rest of that proof holds as written. ∎

New:

    ς_t ϱ takes the place of the bound of ‖M_g‖_Σ there. The rest of that proof holds as written, its bound of ‖M_g‖_Σ
    holding by [[lem:tl5-hfq-theta]]. ∎

### R5 (n3), Placement item 1 (a span of line 167)

Old: `(line 5977, as changed by item 2)`. New: `(line 5978 once item 2 is applied)`.

## The replacements, checked together

**Applying them.** R1–R5 were applied by scratchpad/reader/rpgrd4/tools/fix.py; each old text was found exactly once. The crosswalk rows' line numbers were then updated to the new label lines: 1, 15, 19, 38, 43, 48, 87, 106, 120, 122, 127, 140, 144, 153.

**The result.** scratchpad/reader/rpgrd4/P-GRD4.fixed.md, md5 8f464d0b5a7702cab0486aad721dbf15, 273 lines; the chapter text is lines 1–161.

**The checks.** Merged into a fresh archive of HEAD with the same two items:
- lint.py --chapters: 62 files, 5221 labels, 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: prints `[] 0`.
- The longest source line is 121 characters. No wrapped line starts with a forbidden marker.
- Crosswalk: the 14 updated rows, appended in order, give 377 rows equal to the 377 labels.

Verdict: NOT CONFIRMED
