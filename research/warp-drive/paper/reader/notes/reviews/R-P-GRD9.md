# R-P-GRD9: review of proofs/P-GRD9.md (sec:tl5-hfz, "The recovery sharpened and counted over the words")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD9.md, md5 2cd3f900871544f6ed0bc098a79d1073, 313 lines, at
d8914603 (= HEAD). Chapter: chapters/87-ten-l5.md, 6392 lines, md5 e3ab2f41…, last changed by 7b592452 (sec:tl5-hfy
merged), identical at fa3fa0f0, as the Placement says; the crosswalk, lint.py and assemble.py are also unchanged since.
"87:n" is a chapter line, "P:n" a line of the file.

Fixed copy (nits only): scratchpad/reader/rpgrd9/P-GRD9.fixed.md, md5 d4edf2d932d64e8eb8c81101c8b34562, 316 lines, made by
scratchpad/reader/rpgrd9/tools/fix.py (6 replacements, each found exactly once; crosswalk @PENDING numbers recomputed).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 found once at 87:6391-6392; two
lines by two, so 6392 stays the last line):

| check | P-GRD9.md | P-GRD9.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5266 labels (5254 + 12), 0 hits | same, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| chapter text (P:1-204) lines ≤ 121 / wrapped starts | max 120 / none | max 121 / none |
| Comparison lines ≤ 121 | P:255 has 123 (n4) | all ≤ 121 |
| crosswalk rows: label at the stated line | 12 of 12 | 12 of 12 (1, 15, 23, 47, 70, 77, 97, 110, 135, 165, 176, 191) |
| chapter labels = crosswalk + new rows | 415 = 415 | 415 = 415 |
| printed numbers of the 5254 existing labels | 0 changed | 0 changed |

(The Comparison's bulleted lists start lines with "- " after a non-blank line; they are list items of the notes, not
wrapped chapter lines.)

## 2. The checks asked for

### 2.1 lem:tl5-hfz-rec, step by step: correct

- The norm: |·| is that of k, in which F = (E₀, E₁, f₁, f₂, f₃) is orthonormal, and "for a 2-tensor A, |A|² = Σ A(F_M,
  F_N)²" (87:3636-3639), for tensors of every type. So |H|² = Σ_MN |H^MN|², |H^11| ≤ |H|, and
  |Σ_((M,N)≠(1,1)) H^MN D̂²Ψ(M, N)| ≤ (Σ |H^MN|²)^(1/2) R ≤ |H| R by Cauchy–Schwarz on the coefficients and the triangle
  inequality on the tensors. The old proof uses the same facts (87:4072-4073). The writer's point 1 holds.
- X, X₀, X₁: X is the sum over all A and B ≠ 1 (old proof); X₀ (A ≠ 1), X₁ (A = 1). R² = X + Σ_(A≠1)|D̂²Ψ(A, 1)|², and as
  D̂²Ψ(1, A), A ≠ 1, are exactly the terms of X₁, Minkowski gives (Σ_(A≠1)|D̂²Ψ(A, 1)|²)^(1/2) ≤ X₁^(1/2) + ‖𝒞_(·1)‖|Ψ|;
  Minkowski in ℝ³ on (X₀^(1/2), X₁^(1/2), ·) gives R ≤ (X₀ + 2X₁)^(1/2) + ‖𝒞_(·1)‖|Ψ|.
- The (1, 1) identity: the four diagonal terms (0, 0), (j, j) are terms of X₀, so their norms add to at most 2X₀^(1/2);
  |1 + H^11| ≥ 1 − 𝔥; with R ≤ (2X)^(1/2) + ‖𝒞‖|Ψ| in the H term the displayed inequality follows.
- Minkowski in the plane on (R, |D̂²Ψ(1, 1)|) with X₀ = s²X gives g(s)^(1/2)X^(1/2) plus the |𝔣|, |Ψ| terms;
  ‖𝒞‖ + 𝔥‖𝒞‖/(1 − 𝔥) = ‖𝒞‖/(1 − 𝔥). g″ = −2 + 8/(1 − 𝔥)² > 0, g(1) − g(0) = (3 + (4√2 + 2)𝔥 − 𝔥²)/(1 − 𝔥)² > 0, so
  max g = 𝔨_♯². 𝔨_♯(0) = √5, 𝔨_♯(1/16) = 2.4418, 𝔨_♯(1/4) = 3.2936 (computed). The last claim's four inequalities hold
  for 𝔥 ≤ 1/4 (e.g. √2(1 − 𝔥) ≥ 1 − (4/3)𝔥 as √2 − 1 ≥ (√2 − 4/3)𝔥).
- Numerical test (computed, scalar entries in place of tensors): 200,000 random configurations with the identity and
  D̂²Ψ(A, 1) = D̂²Ψ(1, A) + 𝒞_(A1)Ψ imposed, 𝔥 ∈ [0, 0.9), |H| ≤ 𝔥, a third near the extremal diagonal case: the left
  side never exceeded 0.93 times the right side of eq:tl5-hfz-rec.

### 2.2 def:tl5-hfz-constants and lem:tl5-hfz-abs: correct

The old (6/5) is 1/(1 − (4/3)·(1/8)), applied to the whole bound (87:4335-4339); so (6/5)(√3 + 8/3) on K_rec,
(6/5)𝔯₀ = (6/5)((8/3)‖𝓡̂‖ + √2‖𝒞_(·1)‖) on |Ψ| and (6/5)(4/3) = 8/5 on |𝔣|, which carries the couplings (the (4/3)α_𝔄 of
k₁), the residual (k₂ = (8/5)q₁) and the nonlinear terms (k₃ = (8/5)max(…)). With |H| ≤ 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 ≤ 1/16 on Q(a, b)
(the hypothesis of the bounds since P-GRD8, 𝔰 including |H|, 87:4241), lem:tl5-hfz-rec gives 𝔨_♯, (1 − 𝔰₁^v)⁻¹𝔯_♯ and
(1 − 𝔰₁^v)⁻¹ in their place, with the same weights (ν′^(1/2) on 𝔷 and 𝔯 in k₁^(j,ν′), μ in 𝔨_rec, 𝔨_rec^0). The
comparisons 𝔨_♯ < 2.45 < 5.278, 16/15 < 8/5, 32/15 ≤ 16/5, 16/15 ≤ (6/5)√2 hold; 𝔵^z = (5/8)(1 − 𝔰₁^v)⁻¹𝔵 ≤ 2𝔵/3 ≤ 1/6.
The thresholds keep k₃, so no hypothesis moves, and at level four k₃^♮(μ) ≤ k₃^♮(ν) covers both absorptions.

### 2.3 lem:tl5-hfz-words (a), the Schur bound: correct

With a_JK = μ^((|B|+3−|K|)/2)𝔄_(JB,K): |Σ_K a_JKξ_K|² ≤ (Σ_K‖a_JK‖)(Σ_K‖a_JK‖|ξ_K|²) ≤ r_B Σ_K‖a_JK‖|ξ_K|², summed over J
≤ r_B c_B Σ|ξ_K|²: the norm is at most (r_B c_B)^(1/2), r_B the largest row sum, c_B the largest column sum. Each of the
43 terms of a column sum is at most a row sum, so c_B ≤ 43 r_B. The weight: |B| + 3 ≥ |JB| + 1 and μ ≤ 1 give
μ^((|B|+3−|K|)/2) ≤ μ^((|JB|+1−|K|)/2), so r_B ≤ 2^(−1/2)α_𝔄^(N−1,μ) by the definition α_𝔄^(j,μ) = √2 max Σ … (87:5468);
hence 𝔞_𝔄(B) ≤ (43/2)^(1/2)α_𝔄^(N−1,μ). 𝔩₀ − k₁^z = (1 − 𝔰₁^v)⁻¹(𝔞_𝔄 − α_𝔄) ≤ (√43 − 1)k₁^z, and the identity
√43(k₁^z + 2𝔵^z) − (1 − 𝔵^z)𝔩 = (1 − 𝔵^z)(√43k₁^z − 𝔩₀) gives 𝔩 ≤ √43(k₁^z + 2𝔵^z)/(1 − 𝔵^z).

### 2.4 lem:tl5-hfz-words (b), the per-word bound of the nonlinear part: used correctly

- Leading term: ZJB distinct for distinct (Z, J), |ZJB| ≤ |B| + 3 ≤ N, so it counts once against 𝒥_g.
- 𝔷 and 𝔯_♯ terms: (Σ_Z 𝔷_Z²)^(1/2) ≤ √7(3max|D̂Z| + 2max|D̂²Z|)(|D̂Ψ_C|² + |Ψ_C|²)^(1/2), and the JB are distinct with
  |JB| ≤ |B| + 2: factor μ^(1/2)μ^(−(|B|+3)/2).
- 𝔄 terms: with ξ_K = μ^(|K|/2)(D̂Ψ_K, Ψ_K) and Σ_K μ^|K|(|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², the definition of 𝔞_𝔄(B) gives
  (1 − 𝔰₁^v)⁻¹μ^(−(|B|+3)/2)𝔞_𝔄(B)𝒥_g.
- Residual and nonlinear, per J: ≤ (1 − 𝔵^z)P_ϱ and ≤ 𝔵^z(2μ^(−(|C|+1)/2)𝒥_g + 𝔐) with 𝔐 the per-word bound for the
  shorter words (the old induction's R_C, 87:5563-5572, or its ν-split at level four, 87:6034-6042); their sum is
  P_ϱ + μ^(−(|B|+3)/2)𝒥_g𝔵^z(2 + 𝔨) = P_ϱ + μ^(−(|B|+3)/2)𝒥_g𝔵^z(k₁^z + 2)/(1 − 𝔵^z), the same for every J, so the ℓ² sum
  over the 43 words is √43 times it. No absorption over the words is attempted, so no condition on √43𝔵^z is needed.
- The weights w of P_ϱ: w = 1 where eq:tl5-hfs-m2 is used (lem:tl5-hfs-linfty, lem:tl5-hft-small (a), ϱ part 2k₂ϱ(p)
  unweighted); w = μ^(−(|B|+3)/2) under lem:tl5-hft-small (b), whose M_g^(j) bound carries 2k₂ϱ after the weight
  μ^((|C|+1)/2); w = ν^(−(|B|+3)/2) in lem:tl5-hfq-theta (eq:tl5-hfq-m2, and its first-order step, 87:6049). In each
  case |C′| + 1 ≤ |B| + 3 for every word C′ of length ≤ |B| + 2, so P_ϱ bounds the ϱ part of every per-word bound used,
  and w ≥ 1. Correct.
- Notation: 𝔑_C is the chapter's ℒ^C N(h) − H D̂²Ψ_C (87:4485, lem:tl5-hfg-products), but here it must also hold
  Σ_(K≠C)𝔔_CKℒ^K N(h) for 𝔣 to be L̂Ψ_C + HD̂²Ψ_C (87:4331-4333). n1.

### 2.5 lem:tl5-hfz-c1, the Minkowski step: correct

The Sobolev inequality eq:tl5-hf-cs-r (r = 3) has the weight 2|∂_γ|²𝔳⁶R⁻³ on Σ_J|D̂ℒ^J A|². Pointwise
(Σ_J|D̂ℒ^J A|²)^(1/2) ≤ a + b with a = μ^(−(|B|+3)/2)(𝔩 + (2ϖ′)^(1/2))𝒥_g and b = 43^(1/2)P_ϱ; Minkowski in L²(W) gives
∫WΣ_J|D̂ℒ^JA|² ≤ (P + V)², and Minkowski in ℝ³ gives (F + (P + V)² + S)^(1/2) ≤ (F + P²)^(1/2) + V + S^(1/2). F + P² ≤
μ^(−(|B|+3)) sup(f𝔨₂)ℰ_g gives C₁^z; V² = 43∫W w²(k₂^z)²ϱ(p)²/(1 − 𝔵^z)² gives w C_(1,ϱ)^z ϱ(p) with k₂^z inside the
supremum, as C_(1,ϱ) has k₂ (87:4328). In the weighted forms the factor w is then removed by the weight of the step, as
for C_(1,ϱ) before. The δ-split comparison holds: Minkowski gives the factors (1, 1), every (1 + δ, 1 + 1/δ) is worse
in both.

### 2.6 Each new constant is no larger than the old: correct

- C₁^z ≤ the second entry of C₁^x: 2(𝔩 + (2ϖ′)^(1/2))² ≤ 2(√43𝔨 + (2ϖ′)^(1/2))² ≤ 4(√43𝔨′ + (2ϖ′)^(1/2))², with 𝔨 =
  (k₁^z + 2𝔵^z)/(1 − 𝔵^z) ≤ 𝔨′ = (k₁^μ + 2𝔵)/(1 − 𝔵) (monotone; k₁^z ≤ k₁^μ, 𝔵^z ≤ 𝔵).
- C₁^z ≤ C₁^♮ (with or without the replaced recovery): (1 + ϖ′^(1/2))² ≤ (1 + 37Λ)² ≤ 43(1 + 6Λ)², and
  2(𝔩 + (2ϖ′)^(1/2))² ≤ 4𝔩² + 8ϖ′ ≤ 4·43𝔨² + 10560Λ² ≤ 43·4(72Λ² + 2𝔨²) ≤ 43·4(72Λ² + 8(k₁^μ + 1)²). So no minimum is
  needed.
- C_(1,ϱ)^z: 2(k₂^z)²/(1 − 𝔵^z)² ≤ 8k₂²/(1 − 𝔵)², the factor of thm:tl5-hfy.
- k₁^(j,·,z), k₂^z, 𝔵^z, the 𝔨_rec^(·,z) (§2.2); hence 𝔨_A, λ_t^μ, λ_t^(μ,2), ς_t, the C_∞, C_P, 𝔎, S_F, S_M, ε_M, 𝔯 and
  𝔰_*, each nondecreasing in these; ε^z ≤ ε^w of thm:tl5-hfy as 𝔰₁^v(1 − 𝔵^z)⁻¹k₂^z ≤ 𝔰₁^v(1 − 𝔵)⁻¹k₂; η_z ≥ η.

### 2.7 Every earlier closing condition stays valid: yes

Nothing earlier is edited except the appended pointer sentence. The hypotheses of thm:tl5-hfy imply those of
thm:tl5-hfz (2.6): (a) and (b) are the same, 𝔰_*^z ≤ 𝔰_*^w < 𝔰₁^v, η_z ≥ η > 0, and 4A_zB_z ≤ 4A_w^vB_v < 1. The proof:
Step 1 as in thm:tl5-hfy (the bounds at p hold under 𝔰 ≤ 𝔰₁^v on Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ), Steps 2 and 3 with the
index-z bounds, ε^z from k₂^z𝔰ϱ/(1 − 𝔵^z) ≤ 𝔰₁^v k₂^zϱ/(1 − 𝔵^z): correct.

### 2.8 The Comparison's numbers (checked, computed)

𝔨_♯ = √5 + 3.05𝔰₁^v (derivative (8 + 4√2)/(2√5) = 3.054); ratio 0.42362 (−0.373); k₁^z ≈ 2.245 with K_rec = 5.3/5.2785;
𝔵^z = 0.046, 0.062, 0.054, 0.092; per-word 5.9-6.6 → 2.45-2.68; k-term 38.5, 40.0, 39.3, 43.0 → 𝔩 = 3.58, 4.08, 3.83,
5.06; C₁ −1.18, −1.14, −1.16, −1.08 decades; C_P^v −1.57, −1.53, −1.55, −1.48 with the outer factor; C_(1,ϱ) × 0.30
(0.294-0.304); k₂ × 0.625; the nonlinear part of 𝔩 1.33-2.82. All reproduce, under the stated assumptions. Item 7's
"≈ 0.63 (−0.20 decades)" omits the factor (1 − 𝔵)/(1 − 𝔵^z): 0.607, 0.600, 0.604, 0.587 at level 4 (−0.217 to −0.231),
0.609-0.624 at level 6 (n3). These are deduced figures; the evaluation settles them.

## 3. Findings

### Major

None.

### minor

None.

### nits

**n1. lem:tl5-hfz-words (b), proof (P:120-121, P:128).** 𝔑_C clashes with the chapter's 𝔑_C := ℒ^C N(h) − H D̂²Ψ_C. Old
(P:120-121):

    with 𝔣 = Σ_K 𝔄_CK(D̂Ψ_K, Ψ_K) + Σ_K 𝔔_CK ℒ^K(2R̂ic) − 𝔑_C, 𝔑_C the nonlinear terms of the proof of
    [[lem:tl5-hf-linfty]]. Take the Euclidean norm over J and apply Minkowski's inequality to each kind of term. The words

New:

    with 𝔣 = Σ_K 𝔄_CK(D̂Ψ_K, Ψ_K) + Σ_K 𝔔_CK ℒ^K(2R̂ic) − 𝔑′_C, where 𝔑′_C := Σ_(K≠C) 𝔔_CK ℒ^K N(h) + ℒ^C N(h) −
    H^(αβ) D̂_αD̂_βΨ_C collects the nonlinear terms of the proof of [[lem:tl5-hf-linfty]]. Take the Euclidean norm over J
    and apply Minkowski's inequality to each kind of term. The words

and at P:128 "(1 − 𝔰₁^v)⁻¹ |𝔑_C| ≤" → "(1 − 𝔰₁^v)⁻¹ |𝔑′_C| ≤".

**n2. "The count 43 remains only with the nonlinear part" (intro P:9-10; remark P:195-199).** 𝔞_𝔄 can carry up to
(43/2)^(1/2) too, as the remark itself says two sentences on. Old (P:9-13):

    counts once, the couplings 𝔄 count through the operator norm of their family over the words, and the count 43 remains
    only with the nonlinear part. Finally the parts with 𝒥_g and with ϱ of the first-order step are separated by the
    triangle inequality on the face, in place of (x + y)² ≤ 2x² + 2y² ([[lem:tl5-hfz-c1]]). The closing condition is
    [[eq:tl5-hfz-closing]]; every new constant is at most the one it replaces, and the earlier closing conditions remain
    valid. The notation is that of [[sec:tl5-hfy]].

New:

    counts once, the couplings 𝔄 count through the operator norm of their family over the words, and the count 43 remains
    only with the nonlinear part and in the bounds of that norm. Finally the parts with 𝒥_g and with ϱ of the first-order
    step are separated by the triangle inequality on the face, in place of (x + y)² ≤ 2x² + 2y² ([[lem:tl5-hfz-c1]]). The
    closing condition is [[eq:tl5-hfz-closing]]; every new constant is at most the one it replaces, and the earlier closing
    conditions remain valid. The notation is that of [[sec:tl5-hfy]].

Old (P:195-199, through "The triangle"):

    In the part of C₁^z with 𝒥_g the count 43 of the words remains only in the nonlinear part 43^(1/2) 𝔵^z (k₁^z + 2)/(1 −
    𝔵^z), against 43^(1/2) (k₁^μ + 2𝔵)/(1 − 𝔵) in [[eq:tl5-hfx-c1]] with the replacements of [[lem:tl5-hfy-abs]]: the
    nonlinear terms are bounded through the largest second derivative and are not absorbed over the words, so no condition
    on 43^(1/2) 𝔵^z is needed. The couplings 𝔄 enter through the norm 𝔞_𝔄 of their family over the words, which any bound of
    it may replace, Schur's (r_B c_B)^(1/2) among them, and which is at most (43/2)^(1/2) α_𝔄^(N−1,μ). The triangle

New:

    In the part of C₁^z with 𝒥_g the count 43 of the words remains in the nonlinear part 43^(1/2) 𝔵^z (k₁^z + 2)/(1 − 𝔵^z)
    and in the bounds of 𝔞_𝔄 below, against 43^(1/2) (k₁^μ + 2𝔵)/(1 − 𝔵) in [[eq:tl5-hfx-c1]] with the replacements of
    [[lem:tl5-hfy-abs]]: the nonlinear terms are bounded through the largest second derivative and are not absorbed over
    the words, so no condition on 43^(1/2) 𝔵^z is needed. The couplings 𝔄 enter through the norm 𝔞_𝔄 of their family over
    the words, which any bound of it may replace, Schur's (r_B c_B)^(1/2) among them, and which is at most (43/2)^(1/2)
    α_𝔄^(N−1,μ). The triangle

**n3. Comparison item 7 (P:261-262).** Old: "… ratio (5/8)(1 − 𝔰₁^v)⁻¹(1 − / 𝔵)/(1 − 𝔵^z) ≈ 0.63 (−0.20 decades)."
New second line:

       𝔵)/(1 − 𝔵^z): 0.607, 0.600, 0.604, 0.587 at G0k's level-4 𝔵 (−0.217, −0.222, −0.219, −0.231 decades) and
       0.609–0.624 at its level-6 𝔵 (−0.205 to −0.216); the factor 5/8 alone is −0.204.

**n4. Comparison item 5 (P:255) has 123 characters.** Rewrapped in the fixed copy (P:254-257, same words).

## 4. Checked and correct, no change

lem:tl5-hfz-rec in full (statement, proof, 𝔨_♯ values, the comparison with 1 − (4/3)𝔥); def:tl5-hfz-constants;
lem:tl5-hfz-abs (scope as in lem:tl5-hfy-abs, the three factors, every inequality); lem:tl5-hfz-words (a) and (b),
including the four weights w; lem:tl5-hfz-c1 (Minkowski on the face and in ℝ³, C₁^z ≤ both entries of C₁^x,
C_(1,ϱ)^z ≤ C_(1,ϱ)); thm:tl5-hfz (closing condition, ε^z, η_z, the proof and the containment of thm:tl5-hfy);
rem:tl5-hfz-what apart from n2; the Placement and its commits; the Comparison's figures apart from n3; the deduced
equality case of √5 (X diagonal, D̂²Ψ(0, 0) = −D̂²Ψ(j, j), H = 0, 𝔣 = Ψ = 0 gives |D̂²Ψ|² = 5X).

## 5. Verdict

Every step of the recovery, the Schur bound, the per-word treatment of the nonlinear part, the Minkowski step with its
weights, the comparisons with the old constants and the containment of thm:tl5-hfy check. No Major or minor finding is
open; four nits, with tested replacements in the fixed copy (lint 0 hits, assemble --check 0 problems, in-memory `[] 0`,
crosswalk 415 = 415, no printed number changed), may be applied at merge.

Verdict: CONFIRMED
