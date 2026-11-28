# R-P-GRD12: an independent review of proofs/P-GRD12.md (sec:tl5-hfd)

Reviewed: research/warp-drive/paper/reader/proofs/P-GRD12.md at 59f30503, md5 eec808945bded66de2878a78f1df8bc4, 319
lines. The chapter text is P:1–183 (9 labels), the placement P:185–206, the Comparison P:208–305 and the crosswalk rows
P:307–319. The writer's report is notes/reports/P-GRD12.md.

Base: chapters/87-ten-l5.md, md5 3fdd347418268d2002753071837ea0d3, 7077 lines, 5,292 labels. It has not changed since
the merge 01727fdd. In this review, P:n is a line of the proof file and 87:n a line of the chapter.

Verdict: **NOT CONFIRMED as submitted**: 0 Major, 1 minor, 6 nits. Every mathematical claim of the section holds.

- **The minor (m1)** is a sentence that occurs twice, in the section's opening paragraph and in its Remark. Read as
  written, it gives the order of "largest" and "summed over π" the wrong way round, and the constant that reading
  yields is not the one proved.
- **The nits.** Two are in the chapter text and four are in the placement and the Comparison.
- **The fixed copy** (tested) repairs all seven. I confirm it.

## 1. Mechanics

The scratch tree was made from `git archive HEAD`, with the writer's placement.

- **Item 2.** The two old lines were found exactly at 87:7076–7077, and the new pointer line has 105 characters as
  stated. Item 1's "line 7078, as changed by item 2" is right. The chapter grows to 7262 lines.
- **lint.py --chapters:** 62 files, 5301 labels (5292 + 9), 0 hits.
- **assemble.py --check:** 0 problems.
- **In-memory check:** `[] 0`. I did not run plain `python3 assemble.py`.
- **Crosswalk.**
  - All 9 rows give the line of their own label.
  - The chapter has 450 labels, which equals the crosswalk's rows plus the new labels (450).
  - The new labels are lowercase.
  - None of the 5,292 existing printed numbers changes.
  - Each row's description matches its label.
- **Format.**
  - The longest line of chapter text has 120 characters.
  - No wrapped line of chapter text starts with a forbidden marker. The START flags fall only on the Comparison's
    bullet lines (P:255 onward), which are notes.
  - The chapter text names no file or program and contains no code and no AI language.
- **Numbering.** sec:tl5-hfd is **Section 57.27**, with Lemma 57.230 (lem:tl5-hfd-leaf), Lemma 57.231
  (lem:tl5-hfd-words), Definition 57.232, Theorem 57.233 and Remark 57.234, and the displays (57.160)–(57.162).
  - The writer's report at 59f30503 already says "Section 57.27" (its line 7), and every item number in it matches the
    assembled numbering.
  - The only "57.26" in either file is in the proof's Placement (P:188), where it is sec:tl5-hfu's own number, and that
    is right.
  - So the numbering needs no change. The premise that the report calls the section 57.26 is not borne out by the
    committed report.

## 2. lem:tl5-hfd-leaf (P:18–58): one leaf constant for every rank, holds

Checked against lem:tl5-hft-leaf (87:5772–5816) and lem:tl5-hfp-leaf (87:6616–6642).

- **The subbundles E^U.**
  - Fix any orthogonal splitting of the complexified fibre E_o into SO(3)-irreducible pieces U. If g·o = g′·o then
    g⁻¹g′ lies in the isotropy group, so g′·U = g·U. Hence E^U is well defined.
  - E^U is SO(4)-invariant, and the E^U are mutually orthogonal because the action is isometric for h₀.
  - The isotypic part of an orthogonal sum of invariant subspaces is the sum of the isotypic parts, so
    V_π = ⊕_U V_π^U. ✓
- **Frobenius reciprocity.** L²(S³, E^U) is the representation of SO(4) induced from U. So the multiplicity of π is
  dim Hom_SO(3)(π, U).
  - That is 1 or 0, according as j_U ∈ CG(π) or not, because (j₁, j₂) restricted to the diagonal contains each spin at
    most once (Clebsch–Gordan).
  - Spins are integers here, since j₁ + j₂ ∈ ℕ. ✓
- **The kernel and its equivariance.**
  - K_π^U(ω) = ev_ω ∘ ev_ω* does not depend on the basis. Since (g·s_k) is again an orthonormal basis and
    (g·s)(g·ω) = g s(ω), we get K(g·ω) = g K(ω) g⁻¹. ✓
  - At o, K maps into E^U_o = U, vanishes on U^⊥, and commutes with the isotropy group. By Schur's lemma over ℂ it is a
    multiple c P_U.
  - Its trace is Σ_k |s_k(o)|₀², which is an invariant function with integral dim V_π^U, hence equal to
    dim V_π^U/(2π²). So c = dim π/(2π²(2j_U + 1)). ✓
  - Consistency check: summed over U, the traces give dim π · m_π(r)/(2π²) = dim V_π/(2π²), which is the old trace.
- **Why the largest eigenvalue, not the trace.**
  - For a fixed unit u, ⟨A(ω), u⟩ = Σ_(π,U,k) a_(πUk) ⟨s_(πUk)(ω), u⟩. One Cauchy–Schwarz inequality over π and the
    basis together gives Σ_π w_π ‖A_π‖² times ⟨(Σ_π w_π⁻¹ K_π(ω)) u, u⟩.
  - By invariance this is the same as at o, with the unit vector g⁻¹u. At o the operator is Σ_U 𝔖_(j_U) P_U.
  - Its norm is the largest 𝔖_j over the spins of the fibre, and the supremum over u gives |A(ω)|₀². This is the
    vector-valued reproducing-kernel bound |f(x)|² ≤ ‖K(x, x)‖ ‖f‖², and it is correct.
  - The old proof used the trace, which is the sum of the eigenvalues over all 5^r fibre dimensions. ✓
  - **The order matters.** Summing over π comes before taking the largest eigenvalue. If each K_π is bounded by its own
    largest eigenvalue and the results are then summed over π with the weights, the constant is larger. This is finding
    m1.
- **The injection argument for 𝔖_j ≤ 𝔖_0.**
  - j₁ + j₂ − j ∈ ℕ with j ∈ ℕ forces d := j₁ − j₂ ∈ ℤ with |d| ≤ j, so d takes 2j + 1 values. For fixed d, κ determines
    (j₁, j₂) = (κ + d/2, κ − d/2), so the map to (κ, κ) is injective.
  - By AM–GM, (2j₁ + 1)(2j₂ + 1) ≤ (2κ + 1)².
  - c_(j₁j₂) = 2(j₁² + j₂²) + 2(j₁ + j₂) ≥ 4κ² + 4κ = c_(κκ). Since 𝔶₀ + 𝔶₁c + c² increases for c ≥ 0 and 𝔶₁ > 0, each
    term is at most the term at (κ, κ).
  - So each d-row is at most 2π²𝔖_0, and 𝔖_j ≤ (2j + 1)·2π²𝔖_0/(2π²(2j + 1)) = 𝔖_0. ✓
  - Numerically, over 𝔶₀ ∈ [10⁻⁶, 10¹²], 𝔶₁ ∈ [10⁻⁶, 10⁶] and j = 1, …, 6, the largest ratio 𝔖_j/𝔖_0 is 0.999999. The
    bound is approached when 𝔶₀ dominates and is never exceeded.
- **𝔖_0 = C_(E,0)(𝔶)².** The (κ, κ) terms give n = 2κ, c = n(n + 2) and (n + 1)², and m_(j₁j₂)(0) = 1 iff j₁ = j₂. ✓
- **C_(E,r)² = Σ_j e_j(2j + 1)𝔖_j**, by exchanging the sums through m_π(r) = Σ_(j∈CG(π)) e_j(r). The bounds follow
  from e_0(r) ≥ 1 and Σ_j e_j(2j + 1) = 5^r. ✓
  - Checked against the direct m_(j₁j₂)(r) form at r = 2 and 𝔶 = 1: both give 0.95513.
  - e_j(r) = {0: 1}, {0: 2, 1: 1}, {0: 5, 1: 5, 2: 1}, {0: 15, 1: 21, 2: 8, 3: 1}, {0: 51, 1: 86, 2: 46, 3: 11, 4: 1}, with
    Σ(2j + 1)e_j = 1, 5, 25, 125, 625.
- **The weighted case.** The weights enter only through Σ_π w_π‖A_π‖² = Σ_J 𝔶_|J| ‖ℒ^J A‖², which is the identity of
  lem:tl5-hfp-leaf's proof, and through the monotonicity of w in c. Both hold for all 𝔶₀, 𝔶₁ > 0. ✓
- **Sharpness (Remark).** du is invariant and ℒ_K du = 0, so A = f du^⊗r has ℒ^J A = (K^J f) du^⊗r. Both sides scale by
  |du|₀^(2r), and the inequality reduces to the one for functions.
  - For functions, f = Σ_(c_π≤M) w_π⁻¹ K_π(·, o) gives f(o)²/Σ w_π‖f_π‖² = Σ_(c_π≤M) w_π⁻¹ dim V_π/(2π²), which tends
    to C_(E,0)(𝔶)².
  - So C_(E,0)(𝔶)² is the best constant for every rank. ✓

## 3. lem:tl5-hfd-words (P:60–106): holds; the count is 1853

Checked against def:tl5-hfg-graded and lem:tl5-hfg-quadratic (87:5028–5130), lem:tl5-hfg-products (87:5197),
def:tl5-hfs-bounds, lem:tl5-hfs-quadratic (87:5446–5544), lem:tl5-hfs-products (87:5592–5612), and Steps 2 and 3 of
prop:tl5-hfs-bootstrap (87:5696–5717).

- **Type D and its count.**
  - For each term c_m𝒯_m of 2𝔮̂ and each placement of the letters, exactly one monomial takes the leading D̂Ψ_K from
    both D̂h factors. Its background norm is |c_m| λ̂_(k₁) λ̂_(k₂), where ℒ^K ĝ⁻¹ is one background factor and √5 = λ̂₀
    is used for a letterless ĝ⁻¹.
  - In lem:tl5-hfs-quadratic (b) these monomials account for exactly the "1·1" part of 16Σ⁴λ̂λ̂β₁β₁. So their count is
    𝔠^D_n(ν′), and the other monomials count at most 𝔠^♮_n(ν′) − 𝔠^D_n(ν′).
  - 𝔠^D_n ≤ 𝔠^(2♮)_n, since β₁ ≥ 1 and Σ⁴λλβ₂ − 1 ≥ 0 (its term with k₁ = k₃ = 0 is at least 1). ✓
- **Low and high factors.**
  - At N = 4 the only type-D decomposition with two high factors is (0, 0, 2, 2) at n = 4. That one is in 𝔑^M_I, which
    is what χ removes.
  - At N ≥ 5, two first derivatives of order N − 1 or more need 2N − 4 > N letters.
  - So the factor with fewer letters, Φ₁ = D̂Ψ_(I_P), has order k_P + 1 ≤ N − 2. It is therefore a quantity of
    𝔰_P = 𝔰_g^(m_P), which carries μ^((|B|+3)/2)|D̂Ψ_B| for |B| ≤ N − 3, and |Φ₁| ≤ μ^(−(k_P+3)/2)𝔰_P. ✓
- **The weights.** μ^(n/2) μ^(−(k_P+3)/2) μ^(−k_E/2) = μ^(−3/2) μ^(b/2), with k_E = n − b − k_P. ✓
- **The sum over the words.**
  - For fixed m and fixed positions, I ↦ (I₁, I₂, I_P, I_E) is a bijection onto tuples of words, so the ℓ² norm over I
    factors.
  - Σ_(I₁)|X₁|² ≤ 7^(k₁) λ̂_(k₁)(1)², and the same holds for X₂.
  - Σ_(I_P) μ^(k_P+3)|Φ₁|² ≤ 7^(k_P) 𝔰_P².
  - Σ_(I_E) μ^(k_E)|D̂Ψ_(I_E)|² ≤ 𝒥_g², because the I_E are distinct words and 𝒥_g² contains every μ^|C||D̂Ψ_C|².
  - 7^(k/2)μ^(k/2)λ̂_k(1) = λ̂_k(7μ). For k = 0 this is √5 on both sides.
  - Minkowski's inequality over m (Σ|c_m| = 16) and over the multinomial count of placements gives
    μ^(−3/2) 𝔠^(D,7)_n(μ) 𝔰_P 𝒥_g. ✓
  - The ratio 𝔠^(D,7)_n ≤ 7^(n/2)𝔠^D_n holds because k₁ + k₂ + k_P ≤ n. ✓
- **No 𝔨_B, no recovery constant, no 𝔷, no ϱ.** Φ₂ is a first derivative, bounded by 𝒥_g with factor 1. Neither factor
  is a second derivative, so neither 𝔨_A nor a ϱ-part enters. The old proof's 𝔨_B ≥ 𝔷 was needed only for Φ₂ ∈ {Ψ_C,
  H}. ✓
- **The other monomials.** They are bounded word by word with 𝔠^♮ − 𝔠^D, and 7^(n/2) comes from a uniform per-word
  bound. The ϱ-parts 𝔡 are kept at the old full count, which is a valid overcount. ✓
- **The second inequality.**
  - ℒ^J N(h) = 𝔑^L_J + H D̂²Ψ_J for j′ ≤ 3 at N = 4.
  - The first inequality at length j′ times μ^((n−j′)/2), plus the H term bounded word by word, gives the "+1" and
    𝔡′_(j′) = μ^(n/2)(𝔠^♮_(j′) + 1)2k₂𝔰ϱ. ✓
- **The count 49·1280 → 1853 at n = 4, N = 4 is right.** At Λ = 0, 𝔠^D_4 = 80·2⁴ = 1280, and 𝔠^(D,7)_4 is
  80 Σ_(k₃+k₄=4) C(4, k₃) 7^(min/2) χ = 80(1 + 4√7 + 0 + 4√7 + 1) = 80(2 + 8√7) = 1853.3.
  - Every entry of the table at P:245–248 reproduces: 7^(n/2)·80·2ⁿ = 80, 423, 2240, 11853, 62720, 331883, 1756160, and
    𝔠^(D,7)_n = 80, 160, 583, 1430, 1853 (N = 4), 5213 (N = 6), 13477, 49132.
  - The decades are −0.42, −0.58, −0.92, −1.53, −1.08, −1.39, −1.55.

## 4. def:tl5-hfd-constants and thm:tl5-hfd (P:108–161): hold

- **Step 2.** 𝔮_(jj′) is the operator norm of the block from the family (ℒ^J𝔤)_(|J|=j′) to (𝔔_IJℒ^J𝔤)_(|I|=j) in the
  Euclidean norms of the families (87:4086–4088).
  - So the family over |I| = j is bounded by Σ_(j′) 𝔮_(jj′) times the family norm that eq:tl5-hfd-words gives directly.
  - This replaces the old per-word bound followed by Cauchy–Schwarz over 7^(j′) words. Using "+1" at j′ = j is an
    overcount. ✓
- **Step 3.** The bounds 𝔰_P ≤ C_P e^(φ/2)Y_s + C_(P,ϱ)ϱ + C_(P,0)η₀ and 𝔓 ≤ 𝔎e^(φ/2)Y_s + 𝔎_ϱϱ + 𝔎₀η₀ hold at each
  point. The inner sums are linear with nonnegative coefficients, so Minkowski's inequality over j gives 𝔎^D, 𝔎^D_ϱ and
  𝔎^D₀. ✓
- **𝔎^D ≤ 𝔤_(𝒥,s)𝔎, termwise.** This uses 𝔠^(D,7) ≤ 7^(j′/2)𝔠^D, 0 ≤ 𝔠^D ≤ 𝔠^♮, and C_P ≤ 𝔎. The last holds because
  𝔎 ≥ C_P𝔨_B and 𝔨_B = max(𝔷, 𝔤₁) ≥ 1. The same argument applies to the ϱ and η₀ versions. ✓
- **The leaf constant in every face constant.**
  - Every constant with index p is formed with C_(E,r)(𝔶) or C_(E,r)^♯. def:tl5-hfp-constants puts C^♯² in place of
    6C² "in every other constant formed with a Sobolev inequality on a face" (87:6681–6682). Replacing each with its
    rank-0 analogue at the same weights lowers it, since C_(E,0)(𝔶) ≤ C_(E,r)(𝔶) for all 𝔶.
  - Every constant is built from nonnegative terms by sums, products, maxima and suprema, so it is nondecreasing in the
    Sobolev constants.
  - The thresholds 𝔰₀ and 𝔰₁ (87:4451, 5652, 6087) carry no Sobolev constant. ✓
- **The comparison is valid for all admissible weights.** η_d ≥ η_p (or η_u), A_d ≤ A_p, B_d ≤ B_p and 𝔰_*^d ≤ 𝔰_*^p (or
  u). So the hypotheses of thm:tl5-hfp (N ≥ 6) and of thm:tl5-hfu (N = 4) imply those of thm:tl5-hfd at every weight.
  - The earlier theorems are not edited, so every earlier closing condition remains valid.
  - At N = 4, thm:tl5-hfp is contained only through thm:tl5-hfu, that is for 𝔶₀, 𝔶₁ ≥ 1. For small 𝔶₀, C_(E,0)(𝔶)²
    ≥ 1/(2π²𝔶₀) exceeds 2C_(E,3)^♯² = 7.77 once 𝔶₀ < 0.0065, and S_M^p is formed with C^♯.
  - The theorem's last sentence does not say this. That is nit n1.

## 5. The Comparison

- **Item 1, the leaf table.** Recomputed independently: numpy sums to n ≤ 160000 with Richardson extrapolation in 1/n,
  and stable at n ≤ 40000.
  - C_(E,0)(1)² = 0.087251. The ratios are 0.3022, 0.1499, 0.0722 (−0.52, −0.82, −1.14).
  - At μ = 10⁻⁴: C_(E,0)² = 4.59464 × 10⁻⁴, ratios 0.200012, **0.0894508**, 0.040005.
  - At μ = 10⁻⁵: 1.45289 × 10⁻⁴, ratios 0.200001, 0.089444, 0.040000.
  - At μ = 10⁻⁶: 4.59441 × 10⁻⁵, which is 5^(−r/2) to four digits.
  - 𝔖_j(1) = 0.087251, 0.029084, 0.016524, 0.011595, **0.0089497**.
  - 6C_(E,3)² = 21.8248, so (0.0873/21.825)^(1/2) = 0.0632, which is −1.20 decades.
  - Everything agrees except two roundings (n3).
- **Item 2.** The table reproduces exactly (§3). The sentence "The rest, 𝔠^♮_n − 𝔠^D_n, is 2^n − 1 at Λ = 0" drops
  𝔰_♭𝔠^(3♮)_n, which P:273 then uses correctly (n4).
  - The figures 80·2ⁿ + 2ⁿ − 1 = 81·2ⁿ − 1 agree with G0n's evaluation of 𝔠^(2♮)_n at Λ = 0 (80, 161, 323, 647, 1295).
- **The deduced figures.** The cited figures match G0g line 138 and G0n lines 86–137:
  - 𝔨_B = 10^0.59–0.75;
  - 𝔨_rec^p leads C_P^v, which lies 1.6–1.9 decades above 2C_S;
  - 𝔠^♮₄ medians are 1337–1401 against a floor of 1303;
  - the 7² lever is +0.28 / +0.44 / 0.00 / +0.34;
  - the 1/z̲ lever is ≤ +0.15 (D_A).

  The leaf-lever deductions follow, assuming the constants are linear in the Sobolev constant:
  - rank 3 is −1.05 and rank 2 is −0.70;
  - C_P^v still leads, at 1.25–1.55;
  - S_M falls 1.05 and 1.40.

  The level-6 reasoning matches G0m.4: ϱ binds there, ε is set by 𝔰_*, and ϱ ∝ 1/(sup C_(∞,μ)^(2) k₂^z).
- **The j′ = 4 word count (P:271–274).**
  - The old figure 49(𝔠^♮₄ + 1)𝔎 = (6.6–6.9) × 10⁴ 𝔎 is right.
  - The new count is written "1853 C_P" in both extremes. In the extreme where the part above the floor is of type D,
    𝔠^(D,7)₄(μ) exceeds 1853 by between 7^(1/2) and 49 times that part, x = 34–98 at G0n's medians.
  - Computed over 𝔠^♮₄ ∈ {1337, 1401} and 𝔨_B ∈ {10^0.6, 10^0.75}:
    - all of the excess in the rest gives (3.2–6.4) × 10³ 𝔎, a fall of −1.03 to −1.32;
    - all of it of type D gives (1.5–2.8) × 10³ 𝔎, a fall of −1.38 to −1.65.
  - The range is −1.0 to −1.65 against the stated −1.0 to −1.7. The stated lower end of 1.5 × 10³ holds only with the
    smallest factor, 7^(1/2) (n5).
  - The j′ = 3 figure (−0.9 to −1.5) cannot be checked from the reports, because 𝔠^♮₃ at the optima is not reported.
    It is consistent at the floor with 𝔰_♭𝔠^(3♮)₃ small.

## 6. Findings

**m1 (minor), P:6–8 and P:164–167: the order of the sum over π and the largest multiple.**

- **The text.**
  - The opening paragraph says the kernel "on each isotypic component of the fibre … is a multiple of the identity, and
    the largest of these multiples, summed over π with the weights, is at most the constant of the functions".
  - The Remark says "the pointwise bound needs only the largest; … so the largest eigenvalue, summed over π with the
    weights, is 𝔖_j(𝔶) for some spin j of the fibre".
- **What it gets wrong.** Both read as taking, for each π, the largest eigenvalue of K_π and then summing over π. That
  gives Σ_π w_π⁻¹ max_j c_(π,j), and with c_(π,j) = dim π/(2π²(2j + 1)) the maximum falls at j = |j₁ − j₂|. That sum is
  not 𝔖_j for any j, and it is strictly larger than C_(E,0)(𝔶)².
  - Computed for r = 1, 2, 3, 4: 1.194, 1.252, 1.280 and 1.296 times C_(E,0)² at 𝔶 = 1.
  - At 𝔶 = (μ⁻², μ⁻¹), μ = 10⁻⁴: 1.667, 2.066, 2.352 and 2.573 times.
- **What is proved.** The proof (P:45–50) does the opposite, and correctly. One Cauchy–Schwarz inequality over π and the
  basis, for a fixed direction u, sums over π first. The largest eigenvalue is then taken of Σ_π w_π⁻¹K_π(o) =
  Σ_U 𝔖_(j_U)P_U.
- **Why it is minor.** The lemma and its proof are right. The two summaries, however, describe a mechanism that would
  not reach C_(E,0)(𝔶), and that mechanism is the point of the section.
- **Replacement**, tested.
  - In the opening paragraph: "…so on each isotypic component of the fibre it is a multiple of the identity; summed over
    π with the weights, these multiples give one number for each spin, the largest being that of spin zero, the constant
    of the functions ([[lem:tl5-hfd-leaf]])."
  - In the Remark: "…where the pointwise bound needs only the largest eigenvalue of the kernels summed over π with the
    weights, the Cauchy–Schwarz inequality being taken over π and the basis together for one direction in the fibre;
    each kernel is a multiple of the identity on each isotypic component of the fibre for the isotropy group, so that
    sum is 𝔖_j(𝔶) on the component of spin j, and 𝔖_j(𝔶) ≤ 𝔖_0(𝔶)."
  - Both paragraphs are re-wrapped at 120 characters.

**n1 (nit), P:140–141: the scope of the last implication of thm:tl5-hfd.**

- **The text.** "so the hypotheses of [[thm:tl5-hfp]] and of [[thm:tl5-hfu]] imply these".
- **Why.** The parentheses "(or η_u)" and "(or A_u, …)" pair thm:tl5-hfp with N ≥ 6 and thm:tl5-hfu with N = 4, but the
  sentence itself does not. At N = 4 the hypotheses of thm:tl5-hfp imply these only for 𝔶₀, 𝔶₁ ≥ 1, through
  thm:tl5-hfu (§4).
- **Replacement**, tested: "so the hypotheses of [[thm:tl5-hfp]] (N ≥ 6) and of [[thm:tl5-hfu]] (N = 4) imply these,
  and for N = 4 and 𝔶₀, 𝔶₁ ≥ 1 so do those of [[thm:tl5-hfp]]."

**n2 (nit), P:12–13: "counted … by the number of its own words, in place of the count 7^(j′/2) of all the words".**

- **Why.** The factor is the square root of the number of words (7^(k_P/2)), not the number itself, and 7^(j′/2) is the
  square root of 7^(j′).
- **Replacement**, tested: "the factor at a point by the square root of the number of its own words, in place of
  7^(j′/2), that of all the words of the level".

**n3 (nit), Comparison P:230 and P:233: two roundings.**

- At μ = 10⁻⁴ and r = 3 the ratio is 0.0894508, so it should read 0.0895, not 0.0894.
- 𝔖_4(1) = 0.0089497, so it should read 0.0089, not 0.0090.
- Both are corrected in the fixed copy.

**n4 (nit), Comparison P:249: "The rest, 𝔠^♮_n − 𝔠^D_n, is 2^n − 1 at Λ = 0 (15 at n = 4)".**

- **Why.** That is 𝔠^(2♮)_n − 𝔠^D_n. 𝔠^♮_n also carries 𝔰_♭𝔠^(3♮)_n, as P:273 uses.
- **Replacement**, tested: "is 2^n − 1 + 𝔰_♭𝔠^(3♮)_n at Λ = 0 (15 + 𝔰_♭𝔠^(3♮)₄ at n = 4)".

**n5 (nit), Comparison P:272–274: 𝔠^(D,7)₄(μ) is taken as 1853 in both extremes.**

- **Why.** See §5.
- **Replacement**, tested: the lines state 𝔠^(D,7)₄(μ) ∈ [1853 + 7^(1/2)x, 1853 + 49x], with x the type-D part above
  the floor, and give both extremes: (3.2–6.4) × 10³ 𝔎 at −1.0 to −1.3, and (1.5–2.8) × 10³ 𝔎 at −1.4 to −1.65. The
  overall range becomes −1.0 to −1.65.

**n6 (nit), Placement P:204: the pointer line names one of the section's two changes.**

- **Replacement**, tested: "[[sec:tl5-hfd]] gives the leaves one Sobolev constant for every rank and sums products over
  the words ([[thm:tl5-hfd]])." It is 120 characters, and the heading at P:200 is updated to match.

## 7. The fixed copy

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd12/P-GRD12.fixed.md

- md5 e3418723eb11471d2dc20e27267c96b2, 325 lines.
- It was made by /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd12/tools/fix.py.
  Each old text must occur exactly once. The two summary paragraphs are re-wrapped at 120 characters with no forbidden
  line starts, and the crosswalk line numbers are recomputed from the label lines.
- The chapter text grows from 183 to 186 lines: one line each from m1's opening paragraph, m1's Remark and n1. The
  labels from lem:tl5-hfd-leaf onward move by 1 to 3 lines, and the crosswalk rows carry the new numbers.
- **Re-merged in a fresh tree:**
  - item 2 at 7076, and the chapter at 7265 lines;
  - lint 0 hits, 5301 labels;
  - check 0 problems;
  - `[] 0`;
  - crosswalk 9 of 9 at their labels, 450 = 450;
  - 0 existing numbers changed;
  - the longest chapter-text line is 120 characters, with no forbidden line starts;
  - the numbering is unchanged (Section 57.27).

## Verdict

**NOT CONFIRMED as submitted** (0 Major, 1 minor, 6 nits). The mathematics of all four items holds, including the
5^(−r/2)-sized gain of lem:tl5-hfd-leaf, which is genuine and sharp, and the count 1853.

**CONFIRMED with the fixed copy** P-GRD12.fixed.md (e3418723…), which repairs m1 and the six nits and passes every
check.
