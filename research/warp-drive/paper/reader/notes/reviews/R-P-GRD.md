# R-P-GRD: independent reading of proofs/P-GRD.md (the sharpened constants, sec:tl5-hfg)

File read: proofs/P-GRD.md, md5 68240c7f7c76de1ec19edb0737c6741b, 595 lines (594 newline-terminated): chapter text
1-403 (sec:tl5-hfg, 24 labels), Placement 405-453, Comparison 455-562, crosswalk rows 564-594. I read every line and
every proof in full. Also read: STYLE.md; the writer's report notes/reports/P-GRD.md; notes/reports/G0c.md §G0c.6 and
§G0c.1-3; sec:tl5-hf and sec:tl5-hf4 in full (87:3596-5006), with rem:tl5-beyond and the paragraph before it
(87:3540-3595). Line numbers are lines of P-GRD.md unless marked "87:".

Chapter 87 at HEAD aeaf95c7 (md5 7bd572dce708e2f6f57493cbf6f49498) is unchanged since 8ceedd0e, so the Placement's
quotations and line numbers (87:4594-4596, 87:4992-4994, 87:5006) are current.

HEAD moved to f437eb37 during the reading. That commit adds only notes/reports/G0d.md; P-GRD.md, chapter 87 and its
crosswalk are byte-identical. G0d §G0d.1, item 2 ("𝔤_(N,g) carries no μ^j weights ... no longer suppressed by
μ^(N/2)"), measures independently the effect that m4 below asks the text to state.

## Verdict

**NOT CONFIRMED** - 0 Major, 5 minor (m4 partly on the Comparison), 7 nits (n7 on the Comparison, which is not
chapter text).

The mathematics holds: every lemma, the proposition and both theorems are proved for the constants as defined, every
reused step of the merged bootstraps and persistence lemmas goes through with the graded constants, and every number I
could recompute is right (below). What is open is wording and two definitional gaps:

- m1: lem:tl5-hfg-products does not state the hypothesis 𝔰 ≤ 𝔰₀^⋆ on Q(a, b) that its proof uses.
- m2: [𝔠^⋆₄]_t is formed with the suprema of the Λ_k and λ_k but not of the Λ^R_k.
- m3: Placement item 3 says S_F and S_M "both carry μ^(−3/2)" with the constants of thm:tl5-hf4g; with the ungraded
  triple, which that theorem allows, S_(M,g) carries μ^(−2).
- m4: the μ-comparison with the merged constants (opening paragraph, rem:tl5-hfg-powers, and the Comparison) leaves
  out that 𝔤_N carries the weights μ^j and 𝔤_(N,g) does not. This changes the gain on S_F from μ^(−(N−3/2)) as
  written to about μ^(−(N−3)/2) where the top level dominates 𝔤_N (as for the G0c backgrounds), and it makes ε_(w,g) ≥ ε_w
  (and 𝔯_(w,g) about μ^(−3/2) times 𝔯_w at equal constants). The evaluation must know this.
- m5: Step 1 of prop:tl5-hfg-bootstrap cites Step 1 of the merged proof but not the first paragraph it rests on. This
  is the R-P-HF34 m1 precedent, which was repaired at level four as "the first paragraph and Step 1".

Each finding has an exact replacement. All replacements of this review, applied together to a copy of P-GRD.md (md5
89589533b2065bba461764920e91e17c) and merged into a fresh archive of HEAD, pass every check (last section).

## Checks on the file as submitted (scratch merge)

Scratch tree: git archive of HEAD aeaf95c7 in scratchpad/rpgrd/tree. Items 1-3 were applied by my own script
(rpgrd/tools/merge.py), each old text found exactly once as whole lines: item 3 at 87:4992, item 2 at 87:4594, and the
section appended after 87:5006 ("at 10 l5.") with one blank line.

- lint.py --chapters: 62 files, 5165 labels (5141 + 24), 0 hits.
- assemble.py --check: labels 5165, problems 0.
- in-memory assembled check: prints `[] 0`.
- Line lengths: at most 121 characters in the source and in the assembled text. No wrapped line starts with "+ ", "- ",
  "* ", "> ", "#", "=" or "|" (checked by hand for "- ", which lint does not test).
- The assembled numbers of all 5141 old labels are unchanged; the new labels run Section 57.16, Definition 57.157 to
  Remark 57.166 and (57.100) to (57.112).
- Crosswalk: the 24 rows have four columns, follow chapter order, and give label lines that match the file (1, 18, 35, 61,
  66, 122, 131, 139, 143, 187, 192, 212, 228, 235, 258, 287, 289, 292, 297, 341, 351, 362, 372, 384). Appended to
  crosswalk/87-ten-l5.tsv in the scratch tree, the 321 rows equal the chapter's 321 labels in order.
- Format: no file or program names, code or AI language in chapter text. Labels are lowercase. The Placement and the
  Comparison are marked as not chapter text.

## The claims, checked

### (1) Graded background bounds

- **def:tl5-hfg-graded.**
  - The letter count is right: ℒ^B R̂ carries |B| letters; ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] carry
    |B| + 1.
  - So Λ_N must cover |B| ≤ N − 1. That is enough: in Lemma G with |I| ≤ N, every such factor takes its letters from
    one subword of I.
  - Λ̄_k = max(Λ_k, Λ_k²) correctly covers the monomials of (iii) with one or two background factors when Λ_k < 1.
  - β₁^g, β₂^g, b_g^g, b_H^g are those of def:tl5-hf-levels with Λ_k (Λ̄_k in β₂^g); m′_k ≤ 2^(k+1) − 2.
  - 𝔠^g_n reproduces 𝔠_n term by term:
    - Σ²_n b_H β₂ is β₂(n) + Σ_(k≥1) C(n,k) b_H(k) β₂(n−k);
    - 5Σ³_n b_H Λ^R becomes 5Λ Σ_k C(n,k) 2^(n−k) b_H(k) when Λ^R_j = Λ;
    - Σ⁴ is unchanged.
  - 𝔠^g_n ≤ 𝔠_n when the Λ_k and Λ^R_k are at most Λ ≥ 1.
- **The admissible λ_k.** With h = 0, (iv) gives r! S(k, r) products of r + 1 factors ĝ⁻¹ (√5 each) and r factors ℒ^(B′)π^Z
  (each at most Λ_k). It is admissible; see Observation O1 for a smaller admissible choice.
- **lem:tl5-hfg-quadratic, first expansion.** Each of (i)-(iv) is graded correctly: the coefficient of R′_J and the at most
  two factors of R_J carry letters of J, and the factors ℒ^B ĝ of (iv) carry |B| ≤ k letters. The three sums and the
  "−1" are right.
- **𝔤_(N,g), k₃^⋆, 𝔰₀^⋆, 𝔰₁^⋆** are the merged formulas with 𝔠^⋆, and k₃^⋆ ≤ k₃ when 𝔠^⋆ ≤ 𝔠.
- **C₁^g, C_(1,0)^g.** In the first-order step every coefficient of R′ in ℒ^J D̂Ψ_B, |J| ≤ 2, and its derivative D̂,
  carries at most two letters, so Λ₂ suffices. I recomputed C₁² from the weighted bounds:
  - (1 + 6Λ₂)² 𝒥_g²;
  - 2M_g² + 144Λ₂²𝒥_g², with M_g² ≤ 8(k₁ + 1)²𝒥_g² + 8k₂²ϱ²;
  - this gives the same formula as the merged C₁ and C_(1,ϱ) (unchanged), and C_(1,0)^g with (1 + 6Λ₂)².
- **𝔛_t^g.**
  - In X₁ the coefficients belong to words of rotations of length ≤ 2, which gives 2 · 49 · 1320 = 129360 = 2 · 64680.
  - In X₂ there are at most two such factors, which gives 2 · 7 · 43 = 602, 2 · 7 · 44394 = 621516 and √621516 < 789,
    with [Λ̄₂]_t in place of [Λ]_t².
- **The graded k₁.**
  - k₁^(j) uses α_𝔄^(j), the couplings with |C| ≤ j, and enters M_g^(j) and C_∞^(m) as stated.
  - k₁^(N−1) = k₁ and 𝔐^(N−4) = 𝔐.
  - 𝔄_∅J = 0 follows from eq:tl5-hf-system at j = 0 (an empty sum), so k₁^(0) has α_𝔄^(0) = 0.

### (2) Level-matched μ

- **lem:tl5-hfg-linfty.**
  - Weights: every bound is multiplied by the weight of what it bounds.
    - Ψ_B: μ^(|B|+2) ≤ μ^(|JB|) for the 43 words JB.
    - D̂Ψ_B: μ^((|B|+3)/2) against D̂Ψ_(JB), |JB| ≤ |B| + 2 ≤ N − 1. D̂²Ψ_(JB) goes through M_g = M_g^(N−1).
    - Ψ_(C′): |C′| ≤ |B| + 1.
    - D̂²Ψ_B, |B| ≤ m: the terms D̂Ψ_(ZB), D̂Ψ_B, Ψ_B and 𝔄_BJ are weighted exactly or better. L_g ≤ (2𝔐^(m))^(1/2)(...).
    - The nonlinear factor of largest order o ≤ |B| + 1 enters 𝔰_g^(m) with weight μ^((o+2)/2) ≥ μ^((|B|+4)/2). This
      also holds for D̂²Ψ_J, |J| < |B| ≤ m.
  - The absorption of M_g^(j)/2 and of 𝔰_g^(m)/2 is right.
  - The three C^(m) are those of the merged lemma with k₁^(m), 𝔐^(m), C₁^g and C_(1,0)^g. They hold for every μ ∈ (0, 1],
    and no constant depends on μ.
  - 𝔰_g^(N−4) ≤ 𝔰 ≤ μ^(−N/2) 𝔰_g^(N−4), as o + 2 ≤ N for low quantities.
- **lem:tl5-hfg-products.**
  - (∗) holds for every factor:
    - H ≤ 2𝒥_g;
    - μ^((|C|−1)/2)|Ψ_C| ≤ 𝔷 𝒥_g, by eq:tl5-hf-lie and the Cauchy-Schwarz inequality;
    - μ^(|C|/2)|D̂Ψ_C| ≤ 𝒥_g;
    - μ^((|C|+1)/2)|D̂²Ψ_C| ≤ M_g ≤ 2(k₁ + 1)𝒥_g + 2k₂ϱ(p).
  - The choice of Φ₂ and Φ₁ gives eq:tl5-hfg-count: ℓ_E(Φ₂) ≤ o₂ − 1 if o₂ ≥ 1, and all orders are 0 otherwise.
  - Φ₁ is low. If Φ₁ = D̂²Ψ_B, then q = 2, Φ₂ = Ψ_C with |C| ≥ N − 1, and |B| ≤ min(1, N − 4) = m_P.
  - The exponents (n − ℓ_P − ℓ_E)/2 ≥ −3/2 and (n − ℓ_E)/2 ≥ 0 give the bound.
  - The second inequality (H D̂²Ψ_J: ℓ_P(H) = 2, ℓ_E = |J| + 1) is right.
  - The count is exactly n + 3 for D̂Ψ_B · D̂Ψ_(B′), |B| ≤ N − 3, as the remark says.
- **Step 2.**
  - The family over |I| = j has norm at most μ^(−j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2)(𝔠^⋆_(j′) + 1) X. The weights μ^j cancel
    μ^(−j), which gives 𝔤_(N,g) without weights.
  - 2Ω̂²𝒥_g² ≤ (1/z̲ + 1/c)e_o + e_i with the weighted sums. This replaces the merged conversion
    𝒥₁² ≤ μ^(−N)(...), and with it the weights μ^j of 𝔤_N are lost (m4).
  - 𝔮_H: |D̂h| ≤ μ^(−3/2)𝔰_P and |H| ≤ μ^(−1)𝔰_P.
- **Step 3.** ℰ_g(p) ≤ e^(φ(p)) Y_s² gives 𝔰_P ≤ C_P e^(φ/2) Y_s + C_(P,ϱ)ϱ + C_(P,0)η₀. So S_(F,g) and 𝔯_(w,g) carry
  μ^(−3/2) as defined. The final algebra gives Y_s ≤ A_g + B_g Y_s².
- **Why 𝔰_(*,g) keeps μ^(−N/2).**
  - Step 1 must bound the unweighted 𝔰. Every smallness used concerns 𝔰 itself: 𝔰 ≤ 𝔰_♭ in Lemma G, k₃^⋆𝔰 ≤ 1/2 in
    the absorption, |h| < c_*κ_m/2 and θ_H ≤ ϑ.
  - Its quantities of order N − 2 are controlled only through the energies of level N, at the cost μ^(−N/2).
  - The proof does this with eq:tl5-hfg-linfty at μ = 1, so the terms in ϱ and η₀ carry no μ. That is the best this
    route gives, and the claim stands. The remark's one-clause reason is incomplete (nit n4).

### (3) The sharper chain

- **(a)** Proved as stated:
  - The factor at a point is never D̂²Ψ_B with |B| ≥ 2, so C_P = C_∞^(m_P) with k₁^(m_P), 𝔐^(1) = 57 and 𝔐^(0) = 8.
  - The top k₁ still enters twice. In 𝔨_g it bounds the high factor D̂²Ψ_C, |C| ≤ N − 1.
  - It also enters through C₁^g, which C_P needs: 𝔰_P contains μ^((|B|+3)/2)|D̂Ψ_B| for every |B| ≤ N − 3, whatever m.
  - The remark says exactly this and claims no more.
- **(b)** Not claimed anywhere in the chapter text. Only Λ → Λ₂ in C₁^g is stated, which is right.
- **(c)** Second expansion:
  - H₂ = H − H₁ = g⁻¹hĝ⁻¹hĝ⁻¹ and 2𝔮 − 2𝔮̂ = Σ c_m(𝒯_m(H, g⁻¹, ·) + 𝒯_m(ĝ⁻¹, H, ·)).
  - N(h) = Q + R₃ by the linearity of 𝔠 in its first argument.
  - A letterless ĝ⁻¹ that joins two distinct factors costs 1 by the Cauchy-Schwarz inequality in the frame. One that
    traces a single factor costs √5. Every letterless ĝ⁻¹ of H₁, H₂ and H = −g⁻¹hĝ⁻¹ joins h to another factor.
  - The terms of Q have q = 2 and those of R₃ have q ≥ 3, so 𝔰^(q−2) ≤ 𝔰_♭.
  - The three sums of 𝔠^Q_n and of 𝔠^(3)_n, the "−1" and the "−𝔤₀" are right.
- **(d)** (2𝔐^(1))^(1/2) = √114 = 10.677 (against √800 = 28.284 at N = 6), and √16 = 4 at N = 4.

### Recomputed numbers (exact, mpmath at 40 digits; my scratch rpgrd/calc/cn.py)

- F₀…F₆ = 1, 1, 3, 13, 75, 541, 4683.
- At Λ = Λ_k = Λ^R_k = 1:
  - 𝔠_n = 𝔠^g_n = 103.889, 1816.21, 41444.3, 1.21977·10⁶, 4.43854·10⁷, 1.92838·10⁹, 9.74753·10¹⁰ (n = 0…6). This
    matches the Comparison's "104 … 9.75e10".
  - With λ_k = 1 as well: 𝔠^Q_n = 85, 586.554, 3739.2, 22719.7, 134514, 786699, 4.58241·10⁶. This matches "85, 587, 3.74e3,
    2.27e4, 1.35e5, 7.87e5, 4.58e6".
  - 𝔠^(3)_n = 200.263, …, 1.21436·10¹¹, which matches "200 … 1.21e11".
  - log₁₀(𝔠_6/𝔠^Q_6) = 4.33. The "4.3 decades" is right.
- Seed (Λ_k = λ_k = Λ^R_(k≥1) = 0, Λ^R_0 = |R̂|):
  - 𝔠^Q_n = (81 + 5|R̂|)2^n − 1 exactly, for |R̂| = 1 and |R̂| = 2, n = 0…6.
  - For |R̂| = 1: 85, 171, 343, 687, 1375, 2751, 5503.
- 𝔐^(1) = 57, 𝔐^(0) = 8, 𝔐 = 400 at N = 6.
- 64680, 602, 621516 < 789², 98π² = 49 · 2π², 686π² = 343 · 2π².

### Reused steps and citations

- **Step 1** with eq:tl5-hfg-linfty at m = N − 4, μ = 1 (but see m5).
- **Step 2** of the merged proofs up to the nonlinear terms. At N = 4, 𝔑^M_I uses:
  - eq:tl5-hf4-g with 𝔠^⋆₄;
  - lem:tl5-hfg-mixed, valid for every μ, so its use at μ = 1 for the ungraded triple is legitimate;
  - 𝔍_g ≤ [𝔨₂]_t^(1/2) Y_s, which together give S_(M,g)Y³ + 𝔯_(M,g)Y² + ε_(M,g)Y for either triple.
- **thm:tl5-hfg, (H2).** lem:tl5-hf-persistence uses the bootstrap only for:
  - |H| ≤ 1/8 and θ_H ≤ ϑ;
  - Y_σ ≤ 2A (in P(N));
  - |h| ≤ 1/8 in the expansion.
  𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤ min(1/16, 𝔰_θ) supplies all three.
- **thm:tl5-hf4g, (H2).** lem:tl5-hf4-persistence also uses eq:tl5-hf4-m2 in P(4). It is eq:tl5-hfg-m2 at μ = 1, j = 3,
  since k₁^(3) = k₁ at N = 4. Its hypothesis holds, as 𝔰 < 𝔰₀^⋆/2 on D^κ_s.
- **A_g = 0** gives δ_w = ε_(w,g) = ε_(M,g) = 0, hence R̂ic = 0 and G^♯ = ĝ on N, as in the merged proofs.
- **The bound for ε** is eq:tl5-hf-eps with 𝔰_(*,g).
- **Citations of merged results** are within their range of N:
  - lem:tl5-hf-quadratic's expansion is level-free by lem:tl5-hf4-quadratic (a);
  - lem:tl5-hf-linfty at N = 4 is used through lem:tl5-hf4-linfty;
  - thm:tl5-hf and lem:tl5-hf-persistence are used at N ≥ 6.
- **Interlocking.**
  - 𝔰_♭ is fixed before 𝔠^⋆, and k₃^⋆ depends on 𝔠^⋆, then 𝔰₀^⋆ = min(𝔰_♭, 1/(2 sup k₃^⋆)), then 𝔰₁^⋆ ≤ 𝔰_♭/2. There
    is no circularity.
  - (a) η₀ < 𝔰₁^⋆ ≤ 𝔰_♭/2 couples the choice of 𝔰_♭ to (a), as the Placement says.
  - With the first expansion 𝔰_♭ = 1/8 reproduces the merged form of 𝔰₀.

### Formulas of the Comparison against the chapter text

Every formula of "Every factor, as a formula" agrees with the chapter text, symbol by symbol. These are Λ_k, Λ^R_k,
λ_k, β, b, 𝔠^g, 𝔠^Q, 𝔠^(3), 𝔠^⋆, α, k₁^(j), k₂, k₃^⋆, 𝔰₀^⋆, 𝔰₁^⋆, C₁^g, C_(1,0)^g, 𝔐^(m), m_P, the three C^(m), C_P,
𝔷, 𝔨_g, 𝔤_(N,g), 𝔞, S_(F,g), 𝔯_(w,g), ε_(w,g), 𝔰_(*,g), 𝔛_t^g, m_t^g and the graded triple. Two remarks:

- 𝔰_(*,g) is written there with ϱ in place of ϱ(p). That is an upper bound, so it is safe for the evaluation.
- The Comparison's [𝔠^⋆₄]_t correctly includes the Λ^R_k. The chapter text does not (m2).

What is wrong in the Comparison is the μ-bookkeeping of "Leading μ-powers" (m4) and the reading of "all bounds equal
to 1" (n7).

## Major

None.

## minor

### m1. lem:tl5-hfg-products states no smallness hypothesis (lines 187-189)

"In the setting of [[lem:tl5-hfg-linfty]]" brings in g, h, p and the constants. The condition 𝔰 ≤ 𝔰₀^⋆ on Q(a, b),
however, is the antecedent of that lemma's conclusion, not part of its setting. The proof of products needs it at every
point of Q(a, b):

- for Lemma G (𝔰 ≤ 𝔰_♭) in the first inequality;
- for eq:tl5-hfg-m2, which bounds D̂²Ψ_C in (∗).

lem:tl5-hfg-mixed states the corresponding hypothesis explicitly ("with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b)"), and so does the merged
lem:tl5-hf4-mixed. Replacement R1 below.

### m2. [𝔠^⋆₄]_t omits the Λ^R_k (lines 274-275)

𝔠^⋆₄ depends on the Λ^R_k through the second sums of 𝔠^g, 𝔠^Q and 𝔠^(3). The bound ‖𝔑^M_I‖_Σ ≤ [𝔠^⋆₄]_t ‖𝔭_M‖_Σ in
Step 2 needs 𝔠^⋆₄ ≤ [𝔠^⋆₄]_t at every point of the face. That holds only if the Λ^R_k are also replaced by their face
suprema; as written they are left pointwise. The merged [𝔠₄]_t uses [Λ]_t, and that Λ bounds ℒ^B R̂ too. The
Comparison (line 519) has the right definition. Replacement R2.

### m3. Placement item 3 claims μ^(−3/2) for S_M with either triple (lines 447-448)

The new text reads "with the sharpened constants of [[thm:tl5-hf4g]] both carry μ^(−3/2)". thm:tl5-hf4g is stated for
the constants of def:tl5-hfg-constants with either triple ("the graded triple, or ... the ungraded triple", lines
282-283). With the ungraded triple S_(M,g) = μ^(−2) ∫ m_t^g [𝔨₂]_t dt carries μ^(−2), so the sentence overclaims. The
Comparison (lines 471-472) and rem:tl5-hfg-powers ("with the graded triple") say it correctly. Replacement R3.

### m4. The μ-comparison ignores the weights μ^j of 𝔤_N (lines 6-10, 386-387; Comparison 470-474)

In the merged def:tl5-hf-constants, 𝔤_N = (Σ_j μ^j a_j²)^(1/2), with a_j := Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2)(𝔠_(j′) + 1).
𝔤_(N,g) = (Σ_j (a_j^⋆)²)^(1/2) has no weights (the Comparison notes "absorbed"). So:

- μ^(−N/2) 𝔤_N = (Σ_j μ^(j−N) a_j²)^(1/2) lies between 𝔤₁ := (Σ a_j²)^(1/2) and μ^(−N/2) 𝔤₁. When 𝔠^⋆ = 𝔠 (first
  expansion with Λ_k = Λ^R_k = Λ), 𝔤₁ = 𝔤_(N,g). In general 𝔤_N ≤ 𝔤_(N,g) ≤ μ^(−N/2) 𝔤_N.
- Where the top level dominates 𝔤_N, μ^(−N/2)𝔤_N is about 𝔤₁. It does so for the G0c backgrounds, with 𝔠₆ ≈ 10⁷¹–10⁸⁰
  against 𝔠₀ ≈ 5Λ ≤ 10¹¹ and μ ≈ 10⁻⁵. There, at equal 𝔠, 𝔨 and C:
  - S_(F,g)/S_F ≈ μ^((N−3)/2): μ^(3/2) at level 6 and μ^(1/2) at level 4, not μ^(N−3/2);
  - 𝔯_(w,g)/𝔯_w ≈ μ^(−3/2) (the ϰ₀-terms of 𝔞 carry μ^(−3/2) in 𝔯_(w,g) and μ⁰ in 𝔯_w at every μ);
  - the term with ϱ of ε_(w,g) is 𝔤₁/𝔤_N ≈ μ^(−N/2) times that of ε_w, and ε_(w,g) ≥ ε_w always when 𝔠^⋆ = 𝔠.

The chapter text is not false. "Against μ^(−N) in S_F" is the explicit factor, as the merged rem:tl5-hf4-level also
counts it. But two places mislead:

- The opening paragraph describes the merged cost of the high factor as "μ^(−N/2) again" without the return μ^(j/2) at
  level j.
- The remark compares powers without saying that 𝔤_N carries weights.

A reader, and the evaluation, would take the gain on S_F as μ^(−(N−3/2)) and expect 𝔯 and ε to improve as well. The
residual targets ϱ and η₀ are what G0c found to dominate the printing (§G0c.1, §G0c.5). In fact they become stricter in
μ with the sharpened set, so the gain there must come from 𝔠^⋆ and C_P alone. Replacements:

- R4a (opening) and R4b (remark): the facts above that are proved, in the chapter;
- R4c: the bookkeeping for the evaluation, in the Comparison.

### m5. Step 1 of prop:tl5-hfg-bootstrap omits the first paragraph it rests on (lines 299-301)

Step 1 of the merged proof starts its continuity argument from "It contains 1/2, as D^κ_(1/2) = S ⊂ N₀". That rests on
the first paragraph: g is vacuum with the derivatives of G^♯ on N, so 𝔰 ≤ η₀ < 𝔰₁ on N₀ ∩ D^κ_s. Here that paragraph is
needed with 𝔰₁^⋆ (from η₀ < 𝔰₁^⋆). This is the R-P-HF34 m1 finding, repaired in the merged prop:tl5-hf4-bootstrap as
"The first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]] hold as written". Replacement R5.

## Nits

- **n1 (lines 133-137).** "the Λ_k evaluated at the point of the supremum in C₁^g" leaves C_(1,0)^g out. There (1 + 6Λ₂)²
  belongs inside sup_(S_a), as the proof bounds the S_a term pointwise. Replacement R6.
- **n2 (line 229).** λ_t = 2([k₁]_t + 1) of lem:tl5-hf4-mixed shares its letter with the new bounds λ_k. 𝔛_t^g uses
  λ_t, and the next definition uses "the λ_k". t is a real face parameter in [−10, u*] and k ≥ 0 an integer, so this is
  readable, but a clause helps. Replacement R7.
- **n3 (lines 395-396).** "the third k₁ of C_∞": C_∞ contains k₁ twice, in C₁ and in its third entry. The k₁ meant is
  the one of the third entry. Replacement R8.
- **n4 (lines 389-390).** The reason given for μ^(−N/2) in 𝔰_(*,g) ("as the recovery of second derivatives absorbs the
  ungraded 𝔰") is only part of it: Lemma G's 𝔰 ≤ 𝔰_♭ is the same unweighted smallness, and what costs μ^(−N/2) is that
  the quantities of order N − 2 are bounded only by the energies of level N. Replacement R9.
- **n5 (lines 402-403).** Two small points:
  - The seed sentence omits the "−1" of the formula it explains.
  - Unlike rem:tl5-hf4-level for thm:tl5-hf4, the section does not say that the hypotheses of the new theorems are
    established for no background at 10 l5. The paragraph that item 2 extends says so of thm:tl5-hf only.
  Replacement R10.
- **n6 (Placement item 2, lines 434-435).** "the factor μ^(−3/2) in place of μ^(−N)" should name the quantity, S_F
  (𝔯_(w,g) has μ^(−3/2) against μ^(−N/2), and 𝔰_(*,g) keeps μ^(−N/2)). Replacement R11.
- **n7 (Comparison, lines 545-546; not chapter text).** "Computed at all bounds equal to 1" takes λ_k = 1. The
  admissible λ_k that the text gives for Λ_k = 1 are 5, 27.36, 222.1, 2403, 32507 and 527651. With them 𝔠^Q_n = 85, 921,
  1.08·10⁴, 1.44·10⁵, 2.20·10⁶, 3.87·10⁷, 7.73·10⁸, and 𝔠^(3)_6 = 2.23·10¹¹. That is 2.1 decades below 𝔠_6, not 4.3.
  The evaluation should use the actual λ_k (see O1).

## Observations (no change required)

- **O1.** The factor 5^((r+1)/2) in the admissible λ_k can be dropped. In ĝ⁻¹(ℒ^(B₁)ĝ)ĝ⁻¹⋯(ℒ^(B_r)ĝ)ĝ⁻¹ each inner ĝ⁻¹
  joins two distinct factors, and each end one raises a free index; in the frame both cost 1, by the argument the
  second expansion already uses. So λ_k = Σ_r r! S(k, r) Λ_k^r is admissible, with λ₁ = Λ₁. At Λ = 1 this gives λ_k = F_k
  and 𝔠^Q_6 = 1.73·10⁷ (3.75 decades below 𝔠_6).
- **O2.** 𝔨_g = max(𝔷, 2k₁ + 2) may exceed the merged 2k₁ + 4 where 𝔷 > 2k₁ + 4. Together with m4 this means the two
  sets are not ordered term by term, which is why "either may be used" (line 14) is the right claim.
- **O3.** The Comparison's 𝔰_(*,g) uses ϱ where the chapter has ϱ(p); this is a valid upper bound.
- **O4.** eq:tl5-hfg-cn, eq:tl5-hfg-cinf, eq:tl5-hfg-mixed, eq:tl5-hfg-constants and eq:tl5-hfg-smallness are defined but
  never cited. That is harmless.

## Replacement texts

Each old text occurs exactly once in P-GRD.md. Line breaks are as shown, and each block replaces whole lines.

### R1 (m1), lines 187-189

Old:

    **Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] let I be a
    word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I if N ≥ 5, 𝔑^L_I as in
    [[lem:tl5-hfg-quadratic]] if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2) and 𝔰_P := 𝔰_g^(m_P). Then at every point of Q(a, b)

New:

    **Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] suppose that
    𝔰 ≤ 𝔰₀^⋆ on Q(a, b), and let I be a word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I
    if N ≥ 5, 𝔑^L_I as in [[lem:tl5-hfg-quadratic]] if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2) and 𝔰_P := 𝔰_g^(m_P). Then at
    every point of Q(a, b)

### R2 (m2), line 275

Old:

    Σ₁(t, v*) of the Λ_k and the λ_k,

New:

    Σ₁(t, v*) of the Λ_k, the Λ^R_k and the λ_k,

### R3 (m3), Placement item 3, the last two lines of its New text (lines 447-448)

Old:

    factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2); with the sharpened constants of
    [[thm:tl5-hf4g]] both carry μ^(−3/2) ([[rem:tl5-hfg-powers]]). On N₀ they involve the derivatives of

New:

    factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2); with the constants of [[thm:tl5-hf4g]]
    and the graded triple both carry μ^(−3/2) ([[rem:tl5-hfg-powers]]). On N₀ they involve the derivatives of

### R4a (m4), lines 6-10

Old:

    the level where it is used ([[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]]). Second, in Step 2 of the proof of
    [[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
    μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again; here each factor is bounded by the energies of
    the lowest level that controls it, and in every term of level n the two levels used add up to at most n + 3, so that
    the factor becomes μ^(−3/2) at every level N ≥ 4 ([[lem:tl5-hfg-products]]). Third, the quadratic part of N(h) is

New:

    the level where it is used ([[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]]). Second, in Steps 2 and 3 of the proof
    of [[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
    μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again, of which the weight of level j in 𝔤_N returns
    μ^(j/2); here each factor is bounded by the energies of the lowest level that controls it, and in every term of level n
    the two levels used add up to at most n + 3, so that the factor becomes μ^(−3/2) at every level N ≥ 4
    ([[lem:tl5-hfg-products]]). Third, the quadratic part of N(h) is

(This also corrects "in Step 2": the low quantities are bounded in Step 3 of the merged proof.)

### R4b (m4), lines 386-387

Old:

    and μ^(−2) in S_M of [[thm:tl5-hf]] and [[thm:tl5-hf4]]:
    𝔤_(N,g), 𝔨_g, 𝔞_(o,g), 𝔞_(i,g), C_P, C_(P,ϱ), C_(P,0) and m_t^g do not depend on μ. The power is that of the count

New:

    and μ^(−2) in S_M of [[thm:tl5-hf]] and [[thm:tl5-hf4]]: for given rates,
    𝔤_(N,g), 𝔨_g, 𝔞_(o,g), 𝔞_(i,g), C_P, C_(P,ϱ), C_(P,0) and m_t^g do not depend on μ. If 𝔠^⋆_n = 𝔠_n, then 𝔤_(N,g) is the
    value at μ = 1 of 𝔤_N of [[def:tl5-hf-constants]], and the weights μ^j of 𝔤_N give 𝔤_N ≤ 𝔤_(N,g) ≤ μ^(−N/2) 𝔤_N; so
    ε_(w,g) ≥ ε_w, and in S_F and 𝔯_w these weights offset part of the powers μ^(−N) and μ^(−N/2). The power μ^(−3/2)
    is that of the count

What is stated is proved:

- 𝔮_(jj′) does not depend on μ, so 𝔤_(N,g) is 𝔤_N at μ = 1 when 𝔠^⋆ = 𝔠.
- Σ μ^j a_j² ≤ Σ a_j² ≤ μ^(−N) Σ μ^j a_j².
- 𝒮 is monotone in its argument, so ε_(w,g) ≥ ε_w.
- m_t^g contains e^(φ(t,v*)/2), so its μ-independence holds for given rates.

### R4c (m4), Comparison, "Leading μ-powers" (not chapter text; for the evaluation)

Replace "𝔯_(w,g): μ^(−3/2) (against μ^(−N/2) through 𝔞_o, 𝔞_i)." with "𝔯_(w,g): μ^(−3/2) (against μ⁰ in the first two
terms of 𝔞_o, 𝔞_i and μ^(−N/2) 𝔤_N in the third)." Then append after "𝔤_(N,g) has none.":

    With a_j := Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠_(j′) + 1), μ^(−N/2) 𝔤_N = (Σ_j μ^(j−N) a_j²)^(1/2) lies between
    𝔤₁ := (Σ_j a_j²)^(1/2) (= 𝔤_(N,g) when 𝔠^⋆ = 𝔠) and μ^(−N/2) 𝔤₁, and is close to 𝔤₁ where the top level dominates,
    as for the G0c backgrounds (𝔠₆ ≈ 10⁷¹–10⁸⁰ against 𝔠₀ ≈ 5Λ). There, at equal 𝔠, 𝔨 and C: S_(F,g)/S_F ≈ μ^((N−3)/2)
    (μ^(3/2) at level 6, μ^(1/2) at level 4), not μ^(N−3/2); 𝔯_(w,g)/𝔯_w ≈ μ^(−3/2) (the ϰ₀-terms carry μ^(−3/2) in
    𝔯_(w,g) and μ⁰ in 𝔯_w at every μ); the term with ϱ of ε_(w,g) is 𝔤₁/𝔤_N ≈ μ^(−N/2) times that of ε_w (ε_(w,g) ≥ ε_w
    whenever 𝔠^⋆ = 𝔠). So the targets on ϱ and η₀ in 𝔯 ≤ 1/4 and in ε are stricter in μ with the sharpened set; the gain
    there must come from 𝔠^⋆ and C_P.

### R5 (m5), lines 299-301

Old:

    *Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hf-bootstrap]], with 𝔰₀^⋆, 𝔰₁^⋆ and A_g in place of 𝔰₀,
    𝔰₁ and A_w, and with [[eq:tl5-hfg-linfty]] for m = N − 4 and μ = 1 in place of [[eq:tl5-hf-linfty]]: if 𝔰 ≤ 𝔰₀^⋆ on
    D^κ_σ and p ∈ D^κ_σ, then ℰ⁰_N(p) ≤ μ^(−N) e^(φ(p)) Y_σ(g)² ≤ 4μ^(−N) e^(φ(p)) A_g², so 𝔰(p) ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤

New:

    *Proof.* *Step 1.* As in the first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]], with 𝔰₀^⋆, 𝔰₁^⋆
    and A_g in place of 𝔰₀, 𝔰₁ and A_w, and with [[eq:tl5-hfg-linfty]] for m = N − 4 and μ = 1 in place of
    [[eq:tl5-hf-linfty]]: if 𝔰 ≤ 𝔰₀^⋆ on D^κ_σ and p ∈ D^κ_σ, then ℰ⁰_N(p) ≤ μ^(−N) e^(φ(p)) Y_σ(g)² ≤ 4μ^(−N) e^(φ(p)) A_g²,
    so 𝔰(p) ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤

### R6 (n1), lines 134-137

Old:

    C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂ in place of Λ, and the Λ_k evaluated at the point of the supremum in
    C₁^g; so k₁^(N−1) = k₁, 𝔐^(N−4) = 𝔐 and k₃^⋆ ≤ k₃ when 𝔠^⋆_n ≤ 𝔠_n. None of these constants depends on μ. If 𝔰 ≤
    𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^⋆)) on Q(a, b), a := τ₁(p), b := τ₂(p), then for every μ ∈ (0, 1], at every point
    of Q(a, b)

New:

    C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂ in place of Λ, Λ₂ evaluated at the points of the suprema in C₁^g and
    C_(1,0)^g; so k₁^(N−1) = k₁, 𝔐^(N−4) = 𝔐 and k₃^⋆ ≤ k₃ when 𝔠^⋆_n ≤ 𝔠_n. None of these constants depends on μ. If
    𝔰 ≤ 𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^⋆)) on Q(a, b), a := τ₁(p), b := τ₂(p), then for every μ ∈ (0, 1], at every
    point of Q(a, b)

### R7 (n2), line 229

Old:

    in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b). With the notation of that lemma, 𝔍_g := ‖𝒥_g‖_Σ and

New:

    in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b). With the notation of that lemma, whose λ_t = 2([k₁]_t + 1) is not
    one of the bounds λ_k, 𝔍_g := ‖𝒥_g‖_Σ and

### R8 (n3), lines 395-396

Old:

    smallness constants C_∞^(N−4), C_(∞,ϱ)^(N−4) and C_(∞,0)^(N−4) contain k₁^(N−4) in place of the third k₁ of C_∞. The
    background bounds enter graded: 𝔠^⋆_n through Λ_k, Λ^R_k and λ_k with k ≤ n, C₁^g, C_(1,0)^g and 𝔛_t^g through Λ₂ only.

New:

    smallness constants C_∞^(N−4), C_(∞,ϱ)^(N−4) and C_(∞,0)^(N−4) contain k₁^(N−4) in place of the k₁ of the third entry
    of C_∞. The background bounds enter graded: 𝔠^⋆_n through Λ_k, Λ^R_k and λ_k with k ≤ n, C₁^g, C_(1,0)^g and 𝔛_t^g
    through Λ₂ only.

### R9 (n4), line 390

Old:

    smallness 𝔰_(*,g) < 𝔰₁^⋆ keeps the factor μ^(−N/2), as the recovery of second derivatives absorbs the ungraded 𝔰.

New:

    smallness 𝔰_(*,g) < 𝔰₁^⋆ keeps the factor μ^(−N/2): it bounds the unweighted 𝔰, which the absorption in the recovery of
    second derivatives and the hypothesis of [[lem:tl5-hfg-quadratic]] require, and whose quantities of order N − 2 are
    bounded through the energies of level N only.

### R10 (n5), lines 402-403

Old:

    the number of distributions of n letters over the two solution factors of each quadratic term, 2^n, times the norms of
    its coefficients.

New:

    the number of distributions of n letters over the two solution factors of each quadratic term, 2^n, times the norms of
    its coefficients, less 1 for the subtracted term. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
    [[thm:tl5-hfg]] and [[thm:tl5-hf4g]] are established in this paper for no background at 10 l5.

### R11 (n6), Placement item 2, its New text (lines 434-435)

Old:

    N₀ of order at most N are close to those of G^♯. [[thm:tl5-hfg]] gives the conclusions of [[thm:tl5-hf]] under
    sharpened constants, with graded background bounds and the factor μ^(−3/2) in place of μ^(−N) ([[sec:tl5-hfg]]).

New:

    N₀ of order at most N are close to those of G^♯. [[thm:tl5-hfg]] gives the conclusions of [[thm:tl5-hf]] under
    sharpened constants: graded background bounds, and μ^(−3/2) in place of the factor μ^(−N) of S_F ([[sec:tl5-hfg]]).

## The replacements, checked together

All of R1-R11 (R4c is not chapter text and was not merged) were applied to a copy of P-GRD.md by
scratchpad/rpgrd/tools/fix.py, each old text found exactly once. The copy, scratchpad/rpgrd/P-GRD.fixed.md, has md5
89589533b2065bba461764920e91e17c and its chapter text runs to line 414. I merged it into a fresh git archive of HEAD with
the same three items:

- lint.py --chapters: 62 files, 5165 labels, 0 hits.
- assemble.py --check: problems 0.
- in-memory assembled check: `[] 0`.
- Longest source line: 121 characters. No wrapped line starts with a forbidden marker.
- Still 24 labels, now at lines 1, 19, 36, 62, 67, 123, 132, 140, 144, 188, 194, 214, 230, 238, 261, 290, 292, 295, 300,
  345, 355, 366, 376 and 388. The crosswalk rows' line numbers move accordingly.

Verdict: NOT CONFIRMED
