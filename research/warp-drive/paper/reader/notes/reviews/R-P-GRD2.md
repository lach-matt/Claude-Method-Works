# R-P-GRD2: independent reading of proofs/P-GRD2.md (the constants sharpened a second time, sec:tl5-hfs)

File read: proofs/P-GRD2.md, md5 36c2df1c7c176aba0c8cdc781b7d3795, 490 lines:

- chapter text 1-329 (sec:tl5-hfs, 23 labels);
- Placement 331-362, Comparison 364-459, crosswalk rows 461-490.

I read every line and every proof in full. Also read:

- notes/reports/P-GRD2.md and notes/reports/G0d.md;
- sec:tl5-hf, sec:tl5-hf4 and the merged sec:tl5-hfg of chapter 87 (87:3596-5423).

Line numbers are lines of P-GRD2.md unless marked "87:". Chapter 87 at HEAD 7b09ac28 (md5 67344c1e…) is byte-identical
to my scratch merge of P-GRD with all R-P-GRD replacements, so sec:tl5-hfg is exactly the text I confirmed after
repair. HEAD moved to 363e8b5b during the reading; that commit touches only solver files. P-GRD2.md, chapter 87 and its
crosswalk are unchanged.

## Verdict

**NOT CONFIRMED** — 0 Major, 3 minor, 5 nits (two of them in the Comparison).

The mathematics holds. Every lemma, the proposition and both theorems are proved for the constants as defined. Every
reused step of the merged and P-GRD bootstraps, of persistence and of the theorems goes through at both levels. Every
stated number I could recompute is exact. The three minors:

- m1: 𝔰₀^♮ is defined only inside lem:tl5-hfs-linfty, with a supremum over Q(a, b) that depends on p. def:tl5-hfs-
  constants then defines 𝔰₁^♮ from it, and so do (a) and Step 1. That requires a p-independent 𝔰₀^♮, which
  def:tl5-hfg-constants supplied for 𝔰₀^⋆.
- m2: The opening says "no power Λ_k^r of one bound occurs". rem:tl5-hfs-what says "no product of one bound Λ_k with
  itself occurs beyond those in β₂^♮ and in b^♮_g". Both are false as stated: λ^♮_4 contains Λ₁⁴ and Λ₂², and 𝔠^(2♮)_n
  contains λ^♮_(k₁) λ^♮_(k₃), for instance Λ₁·Λ₁. What is true, and what (a) proves, is that the orders in every
  product of bounds add up to at most the number of letters of the term.
- m3: The opening says the level-four summation over the words "removes the word count and the coefficient 𝔠₄" from
  the products with no factor at a point. The terms of higher order keep 49 𝔰_♭ 𝔠^(3♮)₄ (lem:tl5-hfs-quadratic (c)). The
  Comparison (item 5) says the same.

Each finding has an exact replacement. A copy of P-GRD2.md with all replacements applied (the Comparison's included, and
the crosswalk line numbers updated) is checked in the last section. It is
scratchpad/rpgrd2/P-GRD2.fixed.md (md5 244bcb342034949ea1bdfcfd39d6ffa6), also copied to
scratchpad/reader/reviews/P-GRD2.fixed.md.

## Checks on the file as submitted (scratch merge)

Scratch tree: git archive of HEAD 7b09ac28 (scratchpad/rpgrd2/tree). Items applied by my own script
(rpgrd2/tools/merge.py):

- item 2's old text is found exactly once as whole lines, at 87:5422-5423;
- after item 2 it ends the chapter, and the section is appended after it with one blank line.

Results:

- lint.py --chapters: 62 files, 5188 labels (5165 + 23), 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: `[] 0`.
- Lines are at most 121 characters in source and after resolution. No wrapped line starts with a forbidden marker
  ("- " checked by hand).
- No printed number of the 5165 old labels changes. The new section is Section 57.17, thm:tl5-hfs is Theorem 57.174,
  thm:tl5-hf4s is Theorem 57.175, and rem:tl5-hfs-what is Remark 57.176.
- Crosswalk: the 23 rows have four columns, are in chapter order, and their lines match. Appended in the scratch tree,
  the 344 rows equal the chapter's 344 labels in order.
- Format: chapter text has no file or program names, code or AI language. Labels are lowercase.

## The claims, checked

### (1) Exact expansions, each piece by its own bound; no hypothesis on the background

- **ℒ^J D̂h.** Induction on eq:tl5-hf-lie-d gives ℒ^J D̂h = D̂Ψ_J − Σ_l Σ_(S⊂{1..l−1}) (ℒ^(Z_S)Γ′[π^(Z_l)]) ⋆ Ψ_(J(l,S)).
  - ⋆ has two terms on a 2-tensor. It is a contraction, so it commutes with ℒ.
  - The coefficient carries |S| + 1 = j letters, and Σ_l C(l−1, j−1) = C(k, j).
  - So there are 2C(k, j) monomials with a j-letter coefficient, and β₁^♮ is right. The total count 2^(k+1) − 2 agrees
    with the merged m′_k.
- **ℒ^J D̂²h.** ℒ^J D̂²h = D̂²Ψ_J + Σ_l ℒ^(Z₁⋯Z_(l−1))[ℒ_(Z_l), D̂²]Ψ_(Z_(l+1)⋯Z_k).
  - [ℒ_Z, D̂²]Ψ is 3 + 2 terms of Γ′ with D̂Ψ plus 2 terms of D̂Γ′ with Ψ, which I rederived: five and two.
  - The coefficient takes j − 1 of the outer letters in C(l−1, j−1) ways. ℒ^T D̂Ψ_C adds 2C(l−j, i) monomials with an
    i-letter coefficient.
  - So β₂^♮(k) − 1 = Σ_l Σ_j C(l−1, j−1) Λ_j (7 + 10 Σ_i C(l−j, i) Λ_i) is right.
  - The monomial count is 5(3^k − 1) − 3(2^k − 1), which is ≤ (7/3)(4^k − 1); it gives 7 and 31 against the merged 7 and
    35.
- **ℒ^K ĝ⁻¹ and ℒ^K g⁻¹.**
  - There are k!/(a₁!⋯a_r!) ordered set partitions with block sizes a; summed over a, this gives F_k.
  - Each block ℒ^(B′)π^Z is at most Λ_(a_i).
  - A ĝ⁻¹ joining two distinct factors or raising a free index costs 1 in the frame. A g⁻¹ costs at most 1 + |H| ≤ 𝔤₁,
    with |H| ≤ 2|h| ≤ 2𝔰_♭.
  - So λ^♮_k and b^♮_g are right. O1 is proved: λ^♮₁ = Λ₁, and λ^♮_k = F_k at Λ ≡ 1.
- **(b), eq:tl5-hfs-sum.**
  - Every background factor's bound is Λ_a or Λ^R_a, with a its letters.
  - The "+1" of b^♮_g is the solution part and is not weighted.
  - So the weighting multiplies each monomial by ν′^(b/2). The orders of the solution factors add up to at most
    n − b + 2.
- **The comparison with P-GRD (line 116).** 𝔠^♮_n ≤ 𝔠^Q_n + 𝔰_♭𝔠^(3)_n holds:
  - Λ_(a_i) ≤ Λ_k, 𝔤₁ ≤ 𝔤₀ and r ≤ k;
  - β₁^♮(k) ≤ 1 + 2(2^k − 1)Λ_k;
  - β₂^♮(k) ≤ 1 + (5(3^k−1) − 3(2^k−1))Λ̄_k ≤ β₂^g(k).
- **The background hypothesis.** Nothing uses G0d's Λ_aΛ_b ≤ Λ₁Λ_(a+b−1).

### (2) μ weights

- **eq:tl5-hfs-m2** is a split bound: the 𝒥_g part carries μ^(−(|C|+1)/2) and the ϱ part none. Its proof by induction
  on |C| ≤ j is correct.
  - The words ZC give μ^(−(|C|+1)/2)𝒥_g.
  - The terms 𝔷_Z and 𝔯₀ carry μ^(1/2) more.
  - The jets of level |J| in 𝔄_CJ carry μ^((|C|+1−|J|)/2).
  - The residual is k₂ϱ.
  - In the nonlinear part the 𝔧-factor is at most 2μ^(−(|C|+1)/2)𝒥_g, or R_(C′) ≤ R_C for D̂²Ψ_(C′), |C′| < |C|.
    H D̂²Ψ_J is at most 𝔰R_C.
  - With k₃^♮𝔰 ≤ 1/2 the total is ≤ R_C.
  - k₁^(j,1) = k₁^(j) and k₁^(j,μ) ≤ k₁^(j).
- **lem:tl5-hfs-products.** I checked ℓ_P + ℓ_E ≤ n − b + 3 and μ^((n−ℓ_P−ℓ_E)/2) ≤ μ^((b−3)/2).
  - The ϱ part enters only in branch A, with μ^(n/2).
  - eq:tl5-hfs-sum with ν′ = μ bounds the 𝒥_g part, and with ν′ = 1 the ϱ part.
  - The second inequality gives μ^((n−|J|−3)/2) for 𝔑_J and for H D̂²Ψ_J (ℓ_P(H) + ℓ_E(D̂²Ψ_J) = |J| + 3).
- **Step 2.** The family over |I| = j is at most μ^(−j/2)(A_j + B_j). With the weights μ^j, Minkowski and the
  Cauchy–Schwarz inequality over j give 𝔤_(𝒥,s)μ^(−3/2)𝔓𝒥_g + 𝔤_(ϱ,s)2k₂𝔰ϱ, as stated:
  - 𝔮_(jj′) carries μ^((j−j′)/2), the weight of 𝔒;
  - the ϱ part has the merged μ^j, which settles my R-P-GRD m4 for ε.
  ϱ and η₀ still carry μ^(−3/2) in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s). That is a correct bound, but see nit n2 and O1.
- **The illustration in the Comparison** is exact: 𝔠^(2♮)_6 = 1.46872·10¹⁸ and 𝔠^(2♮)_6(10⁻⁵) = 1.43623·10⁵ at Λ_a = Λ^R_a =
  10^(a+1).

### (3) The top-level k₁ once per term; k₁^(j,μ)

- **The two branches.**
  - Branch A: Φ₂ = D̂²Ψ_C uses both derivatives, so Φ₁ ∈ {H, h, Ψ_B}. It is low, so |B| ≤ N − 2, and it is bounded by
    𝔰_P⁰ ≤ 2C_Sℰ_g^(1/2) + 2C_(0,0)η₀, with no k₁. Only Φ₂ carries k₁^μ, through 𝔨_A.
  - Branch B: Φ₂ ∈ {H, h, Ψ_C, D̂Ψ_C} is bounded by max(𝔷, 2)𝒥_g without k₁. Φ₁ goes through 𝔰_P, whose C_P^♮ carries
    k₁^μ through C₁^♮ (and k₁^(m_P,μ)).
  - So 𝔓 ≤ 𝔎e^(φ/2)Y + 𝔎_ϱϱ + 𝔎₀η₀ with 𝔎 = max(2C_S𝔨_A, C_P^♮𝔨_B), 𝔎_ϱ = C_(P,ϱ)^♮𝔨_B (𝔰_P⁰ has no ϱ term) and
    𝔎₀ as stated. The top k₁ appears once in each entry.
- **"Fewer is impossible with this method"** (Comparison item 3, marked deduced, not in the chapter). It is right for
  the maximum over the monomials, which is what 𝔎 is:
  - A high D̂²Ψ_C (|C| up to N − 1) can only be the energy factor, and it needs the top recovery.
  - A point factor D̂Ψ_B with |B| up to N − 3 needs, in the Sobolev step, D̂_(∂_γ)D̂Ψ_(JB) with |JB| up to N − 1.
    ∂_γ = ê₄ − κ′ê₃ + κ′b̂∂_x has an E₁-component, so this involves D̂²Ψ(E₁, E₁), which only the equation gives.
  - Per monomial fewer is possible: a branch-B term whose point factor is H, h or Ψ_B needs no k₁. That does not lower
    the maximum.
- **C₁^♮ and C_(1,0)^♮.**
  - With a ≤ 2 letters on a coefficient, μ^((|B|+3)/2) ≤ μ^((1+a)/2)μ^(|C|/2) for |C| = |JB| − a, and
    μ^((1+a)/2)Λ_a ≤ Λ₂^μ.
  - D̂²Ψ_(JB) is bounded through eq:tl5-hfs-m2.
  - The formulas follow, and C_(1,ϱ) is unchanged.
- **At μ = 1** the constants are those of eq:tl5-hfg-cinf: Λ₂^1 = max(Λ₁, Λ₂) = Λ₂ and k₁^1 = k₁. So Step 1 and 𝔰_(*,s)
  are right.

### (5) Weighted 𝔮, the word count kept, and the level-four products

- **(c), the summation over the words.**
  - b = 0 is forced for two high factors.
  - The terms of Q in 𝔑^M_I are only:
    - H₁^(λσ)D̂_λD̂_σh with three letters on h and one on D̂²h, with coefficient 1, for 4 sets S;
    - 2𝔮̂ with two letters on each D̂h, with coefficient 16·√5² = 80, for 6 sets S.
  - Any letter on D̂²h, D̂h or ĝ⁻¹ beyond these makes b ≥ 1.
  - I ↦ (I_S, I_(S^c)) is a bijection, so Minkowski over S gives 480P₁ + 4P₂.
  - The terms of R₃ give 49𝔰_♭𝔠^(3♮)₄𝔭_M ≤ 49𝔰_♭𝔠^(3♮)₄(P₁ + P₂).
  - So 𝔠^M₁ and 𝔠^M₂ are right.
- **lem:tl5-hfs-mixed.**
  - ρ′₁ = 2μ^(1/2)Λ₁ and ρ′₂ = 4μ^(1/2)Λ₁ + 2μΛ₂, and ϖ₁ = 6ρ′₁² + 36ρ′₂². At μ = 1 and Λ ≡ Λ₂ this is 1320Λ₂², the merged
    count.
  - β₂^♮(1) − 1 = 7Λ₁ and β₂^♮(2) − 1 = 14Λ₁ + 10Λ₁² + 7Λ₂, so ϖ₂ is right.
  - Both bounds use μ² ≤ μ^(a/2)μ^(|C|/2).
  - The counts are right: 2·49ϖ₁, 2·7·43 = 602 and 2·7ϖ₂.
  - The first line follows from eq:tl5-hf4-holder per pair; the sums factor into X_iY_i.
  - k₁ enters once per product: in 𝔜_(1,t) and in 𝔛_(2,t).
- **S_(M,s), 𝔯_(M,s), ε_(M,s)** are exactly the expansion of the two products with 𝔍_g ≤ [𝔨₂]_t^(1/2)Y_s. [𝔠^M_i]_t is
  formed with the suprema of the Λ_k and Λ^R_k, which is complete, since λ^♮ comes from the Λ_k.
- **7^(j′/2)** is kept, as the file says.

### (6) O1

Proved in (a): λ^♮₁ = Λ₁, and λ^♮_k = F_k at Λ ≡ 1 (computed: 1, 1, 3, 13, 75, 541, 4683).

### (4) Sobolev on the leaves

The chapter text claims nothing for it. C_S, C₁^♮ and 𝔭₃ are used as in the merged lemmas, and the Comparison marks it
"not done". 𝔭₃ = 1 + 108 + 11664 = 11773, as stated.

### Recomputed numbers (exact, mpmath at 40 digits; rpgrd2/calc/nat.py)

- At Λ_a = Λ^R_a = 1: 𝔠^(2♮)_n = 85, 586.554, 3902.31, 26776.3, 201357, 1.7264·10⁶, 1.71011·10⁷. The Comparison's "85, 587,
  3.90e3, 2.68e4, 2.01e5, 1.73e6, 1.71e7" is right.
- β₁^♮ = 1, 3, 7, 15, 31 and β₂^♮ = 1, 8, 32, 110, 356 at Λ ≡ 1.
- 𝔠^(3♮)_n at 𝔰_♭ = 1/8: 200.263, …, 1.31448·10⁹.
- The illustration (above), and 480 = 6·80, 4, 49.

### Reused steps and citations

- **Step 1.** It cites hfg Step 1, which now cites the first paragraph and Step 1 of the merged proof (my R5). This
  works at μ = 1 with constants equal to eq:tl5-hfg-cinf. It needs the p-independent 𝔰₀^♮ (m1).
- **Step 2.** It cites hfg Step 2, and through it the merged Step 2 at both levels. It also cites prop:tl5-hf-linear-n,
  and prop:tl5-hf4-bootstrap for 𝔑^M. The pointwise Cauchy–Schwarz over I equals the merged face-wise one.
- **Step 3.** The foliation is the level-free one.
- **thm:tl5-hfs** (N ≥ 6, through thm:tl5-hfg).
  - (H2) uses 𝔰 ≤ 𝔰_(*,s) < 𝔰₁^♮ ≤ 𝔰_♭/2 ≤ 1/16 and Y_σ ≤ 2A_s.
  - A_s = 0 gives R̂ic = 0 and G^♯ = ĝ.
- **thm:tl5-hf4s** (through thm:tl5-hf4g). eq:tl5-hf4-m2 is eq:tl5-hfs-m2 at μ = 1, j = 3, since k₁^(3,1) = k₁.
- **Citation ranges.** Every merged result is cited within its range of N. The expansions of lem:tl5-hf-quadratic
  (iii)-(iv) are level-free by lem:tl5-hf4-quadratic (a).
- **Interlocking.** 𝔰_♭ fixes 𝔤₁, 𝔠^♮, k₃^♮, 𝔰₀^♮ and 𝔰₁^♮ in that order, and (a) η₀ < 𝔰₁^♮ ≤ 𝔰_♭/2. 𝔤₁ needs
  𝔰 ≤ 𝔰_♭, which 𝔰 ≤ 𝔰₀^♮ gives.

### The Comparison against the chapter text

Every formula of "Every new factor, as a formula" agrees with the chapter text. The writing differs from the chapter
in three places, none of them changing a value:

- In β₂^♮ the sums are written Σ_(j≤l) and Σ_(i≤l−j) without a lower limit. That is harmless, as C(l−1, −1) = 0 and
  Λ₀ = 0.
- 𝔰_(*,s) is written with ϱ for ϱ(p), a valid upper bound.
- [𝔠^M_i]_t is abbreviated 𝔠^M_i.

Two statements are wrong: item 5 (m3) and item 2's "the ϱ-part keeps the merged weights" (n2).

## Major

None.

## minor

### m1. 𝔰₀^♮ has no p-independent definition (line 224; lem:tl5-hfs-linfty, lines 119-120)

lem:tl5-hfs-linfty defines 𝔰₀^♮ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^♮)), and that depends on p.
def:tl5-hfs-constants then puts 𝔰₁^♮ := min(𝔰₀^♮/2, …), and thm (a), (c) and Step 1 compare η₀ and 𝔰_(*,s) with
𝔰₁^♮, and 𝔰 with 𝔰₀^♮/2, on all of D^κ_σ. The merged def:tl5-hfg-constants defines 𝔰₀^⋆ with sup_(D^κ) for exactly
this reason (and def:tl5-hf-constants defines 𝔰₀). The fix is R1.

### m2. "No power Λ_k^r of one bound occurs" is false as stated (lines 4-6, 320-321)

λ^♮_k sums Λ_(a₁)⋯Λ_(a_r) over all compositions of k, including Λ₁^k and, for k = 4, Λ₂². The remark's exception list
("beyond those in β₂^♮ and in b^♮_g") leaves out λ^♮_k. The products across the factors of a term in 𝔠^(2♮), 𝔠^(3♮)
(λ^♮_(k₁)λ^♮_(k₃), …) are also products of bounds with themselves. What lem:tl5-hfs-quadratic (a) proves is the right
statement: the factors carry disjoint letters, so in every product of bounds the orders add up to at most the number of
letters of the term. The powers Λ_k^r of def:tl5-hfg-graded break this. The fix is R2 (opening) and R3 (remark).

### m3. The level-four summation does not remove the count from the terms of higher order (lines 12-13; Comparison 452-453)

lem:tl5-hfs-quadratic (c) sums only the terms of Q exactly (480P₁ + 4P₂). The terms of R₃ in 𝔑^M_I are bounded as
before, by 49𝔰_♭𝔠^(3♮)₄𝔭_M, so 𝔠^M_i still contains the word count 49 and a coefficient of the 𝔠₄ kind. The remark
(325-326) states 𝔠^M_i correctly; the opening ("removes the word count and the coefficient 𝔠₄ from them") and Comparison
item 5 ("have no count left … removes [𝔠^⋆₄]_t from S_M") overstate it. The fix is R4, and C2 for the Comparison.

## Nits

- **n1 (line 4).** "Five changes are made", but the paragraph lists four. Folded into R2 as "Four".
- **n2 (remark 321; Comparison 433-434).**
  - In the remark, "The constant of the terms with ϱ, 𝔤_(ϱ,s), has the weights μ^j" holds only for the term with ϱ in
    ε_(w,s). ϱ also enters 𝔯_(w,s) (through C_(P,ϱ)^♮ and 𝔎_ϱ), 𝔯_(M,s) and ε_(M,s) with μ^(−3/2).
  - The Comparison's "The ϱ-part keeps the merged weights μ^j" could make the evaluation treat all ϱ targets as merged.
  - Folded into R3, and C1 for the Comparison.
- **n3 (line 324).** "its terms with 𝔯₀ and the fields Γ other than K_rec": K_rec is not a field. The weighted terms are
  those with D̂Z and D̂²Z. Folded into R3.
- **n4 (lines 182-183).** "is bounded by the first inequality for J" uses 𝔑_J = 𝔑^L_J, which at N = 4 holds because
  |J| ≤ 3. The P-GRD proof says so; this one does not. The fix is R5.
- **n5 (Placement item 1, line 343).** "(line 5423, as changed by item 2)": item 2 adds a line, so the remark then ends
  at 5424. The fix is R6.

## Observations (no change required)

- **O1.** The split technique of eq:tl5-hfs-m2 would also free the ϱ parts elsewhere:
  - the ϱ part of 𝔰_P (C_(P,ϱ)^♮, 𝔎_ϱ);
  - that of ‖M_g‖_Σ in μ²X₂ and μ^(3/2)Y₁ (ς_t), which could carry μ² and μ^(3/2).
  The ϱ terms of 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s) would then lose their μ^(−3/2) at least in part. This is not claimed, so
  it is a lever, not a defect.
- **O2.** |H| is among the quantities of 𝔰, so 1 + |H| ≤ 1 + 𝔰_♭, and 𝔤₁ = 1 + 𝔰_♭ would do. The letterless g⁻¹ of H
  and H₂ joins distinct factors and could count 𝔤₁ instead of 𝔤₀. The X = g⁻¹ slot of 𝒯_m may be a trace, where 𝔤₀
  stays.
- **O3.** λ_t^μ (lem:tl5-hfs-mixed) and λ^♮_k share a letter. Both are defined in place, so this is readable.

## Replacement texts

Each old text occurs exactly once in P-GRD2.md. Each block replaces whole lines with the line breaks shown (C1 and C2
replace a span inside an item of the Comparison).

### R1 (m1), line 224

Old:

        𝔰₁^♮ := min(𝔰₀^♮/2, c_* κ_m/2, 𝔰_θ),

New:

        𝔰₀^♮ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮)),      𝔰₁^♮ := min(𝔰₀^♮/2, c_* κ_m/2, 𝔰_θ),

### R2 (m2, n1), lines 4-6

Old:

    Five changes are made, each a proved restatement. First, every background factor is bounded by a bound of its own order,
    also inside the iterated Lie derivatives of ĝ⁻¹, of g⁻¹, of D̂h and of D̂²h, so that no power Λ_k^r of one bound occurs
    ([[def:tl5-hfs-bounds]], [[lem:tl5-hfs-quadratic]]). Second, the letters that a quadratic term of level n places on

New:

    Four changes are made, each a proved restatement. First, every background factor is bounded by a bound of its own order,
    also inside the iterated Lie derivatives of ĝ⁻¹, of g⁻¹, of D̂h and of D̂²h, so that in every product of bounds the
    orders add up to at most the number of letters of the term ([[def:tl5-hfs-bounds]], [[lem:tl5-hfs-quadratic]]). Second,
    the letters that a quadratic term of level n places on

### R3 (m2, n2, n3), lines 320-324

Old:

    the weights of the coupling 𝔒 of [[eq:tl5-hf-bn]]; no product of one bound Λ_k with itself occurs beyond those in
    β₂^♮ and in b^♮_g, where the letters of the factors add up to at most k. The constant of the terms with ϱ, 𝔤_(ϱ,s), has
    the weights μ^j of 𝔤_N of [[def:tl5-hf-constants]]. The recovery constant of the highest level enters 𝔎 through 𝔨_A
    in the first entry and through C₁^♮ in the second, not as a product; it enters as k₁^μ, whose couplings 𝔄_CJ carry
    the weights μ^((|C|+1−|J|)/2) ≤ μ^(1/2), as do its terms with 𝔯₀ and the fields Γ other than K_rec. At level four,

New:

    the weights of the coupling 𝔒 of [[eq:tl5-hf-bn]]; a product of bounds Λ_(a₁) ⋯ Λ_(a_r) occurs only with a₁ + ⋯ + a_r
    at most the number of letters of the term, against the powers Λ_k^r of [[def:tl5-hfg-graded]]. The constant of the term
    with ϱ in ε_(w,s), 𝔤_(ϱ,s), has the weights μ^j of 𝔤_N of [[def:tl5-hf-constants]]; in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s), ϱ
    carries μ^(−3/2) as in [[sec:tl5-hfg]]. The recovery constant of the highest level enters 𝔎 through 𝔨_A
    in the first entry and through C₁^♮ in the second, not as a product; it enters as k₁^μ, whose couplings 𝔄_CJ carry
    the weights μ^((|C|+1−|J|)/2) ≤ μ^(1/2), as do its terms with 𝔯₀ and with D̂Z and D̂²Z. At level four,

### R4 (m3), line 13

Old:

    before the Hölder inequality, which removes the word count and the coefficient 𝔠₄ from them ([[lem:tl5-hfs-mixed]]).

New:

    before the Hölder inequality, which removes the word count and the coefficient 𝔠₄ from their terms of second order, the
    terms of higher order keeping 49 𝔰_♭ 𝔠^(3♮)₄ ([[lem:tl5-hfs-quadratic]], [[lem:tl5-hfs-mixed]]).

### R5 (n4), lines 182-183

Old:

    By [[eq:tl5-hfs-sum]] with ν′ = μ and with ν′ = 1 this gives the first inequality. For |J| < n, μ^(n/2) |𝔑_J| =
    μ^((n−|J|)/2) μ^(|J|/2) |𝔑_J| is bounded by the first inequality for J, and in H^(αβ) D̂_αD̂_βΨ_J the factor D̂²Ψ_J is

New:

    By [[eq:tl5-hfs-sum]] with ν′ = μ and with ν′ = 1 this gives the first inequality. For |J| < n, 𝔑_J = 𝔑^L_J, also for
    N = 4 as |J| ≤ 3, and μ^(n/2) |𝔑_J| = μ^((n−|J|)/2) μ^(|J|/2) |𝔑_J| is bounded by the first inequality for J; in
    H^(αβ) D̂_αD̂_βΨ_J the factor D̂²Ψ_J is

### R6 (n5), Placement item 1 (line 343, a span)

Old: `(line 5423, as changed by item 2)`. New: `(line 5424 once item 2 is applied)`.

### C1 (n2), Comparison item 2 (lines 433-434, a span)

Old:

    The ϱ-part keeps the merged
       weights μ^j (𝔤_(ϱ,s), the target ϱ of the merged set, m4); η₀ enters 𝔯 and 𝔰_* as in P-GRD.

New:

    The ϱ-part of ε_(w,s) keeps
       the merged weights μ^j (𝔤_(ϱ,s), the target ϱ of the merged set, m4); in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s), ϱ and η₀
       carry μ^(−3/2) as in P-GRD, and 𝔰_* is as in P-GRD.

### C2 (m3), Comparison item 5 (lines 452-453, a span)

Old:

    At level 4 the products with no factor at a point have no count left: they
       are summed over the words exactly (lem:tl5-hfs-quadratic (c)), which also removes [𝔠^⋆₄]_t from S_M (proved).

New:

    At level 4 the terms of second order of the products with no factor at a
       point have no count left: they are summed over the words exactly (lem:tl5-hfs-quadratic (c)), which replaces
       49 [𝔠^⋆₄]_t in S_M by 480 and 4; the terms of higher order keep 49 𝔰_♭ [𝔠^(3♮)₄]_t (proved).

## The replacements, checked together

All of R1-R6, C1 and C2 were applied by rpgrd2/tools/fix.py, each old text found exactly once. The crosswalk rows'
line numbers were then updated to the new label lines: 1, 21, 36, 55, 69, 75, 120, 128, 133, 167, 174, 189, 204, 221,
252, 254, 258, 263, 294, 299, 308, 313, 321.

Result: scratchpad/rpgrd2/P-GRD2.fixed.md, md5 244bcb342034949ea1bdfcfd39d6ffa6, 496 lines, chapter text 1-333. It is
also copied to scratchpad/reader/reviews/P-GRD2.fixed.md. Merged into a fresh archive of HEAD with the same two items:

- lint.py --chapters: 62 files, 5188 labels, 0 hits.
- assemble.py --check: problems 0.
- In-memory assembled check: `[] 0`.
- Longest source line: 121. No wrapped line starts with a forbidden marker.
- Crosswalk: the 23 updated rows are appended in order, and 344 rows equal the 344 labels.

Verdict: NOT CONFIRMED
