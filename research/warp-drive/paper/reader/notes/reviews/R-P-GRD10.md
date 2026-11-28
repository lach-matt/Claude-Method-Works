# R-P-GRD10: review of proofs/P-GRD10.md (sec:tl5-hfp, "The leaf constant, the weights of the words and the seven fields")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD10.md, md5 871190e2fcc85ccaf1fcff32a454f7a3, 459 lines, at
ee0925ad (= HEAD). Chapter: chapters/87-ten-l5.md, 6599 lines, md5 29a18cc0…, last changed by 626bca77 (sec:tl5-hfz
merged); chapter and crosswalk are unchanged since 3a6a1ee0, as the Placement says. "87:n" is a chapter line, "P:n" a
line of the file.

Fixed copy (one nit, Comparison only; the chapter text P:1-283 is byte-identical): scratchpad/reader/rpgrd10/
P-GRD10.fixed.md, md5 e977107b28c3822c2ba112530a574608, 460 lines, made by scratchpad/reader/rpgrd10/tools/fix.py (4
replacements, each found once).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 found once at 87:6598-6599; two
lines by two, so 6599 stays the last line):

| check | P-GRD10.md | P-GRD10.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5281 labels (5266 + 15), 0 hits | same, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| lines ≤ 121, no forbidden wrapped starts (chapter text) | yes | yes |
| crosswalk rows: label at the stated line | 15 of 15 | 15 of 15 (same lines) |
| chapter labels = crosswalk + new rows | 430 = 430 | 430 = 430 |
| printed numbers of the 5266 existing labels | 0 changed | 0 changed |

The amendment to the crosswalk row of rem:tl5-hfz-what ("; points to sec:tl5-hfp (P-GRD10 item 2)") has the form of the
one applied at row 322 (rem:tl5-hfg-powers, "points to sec:tl5-hfs (P-GRD2 item 2)"). Observation for the merge: the
same notes of P-GRD3 to P-GRD9 have not been applied; rows 364, 378, 389, 395, 400, 404 and 416 (rem:tl5-hft-what …
rem:tl5-hfz-what) carry no "points to". Apply this one, and those, or none, but consistently.

## 2. The checks asked for

### 2.1 The sharp leaf constant (lem:tl5-hfp-leaf): correct; table reproduced

- On V_π (87:5792-5815): the projection commutes with SO(4), hence with every ℒ_(K_ab), so ℒ_(K_ab)V_π ⊂ V_π and Ω = c_π
  there. Skew-adjointness gives Σ_(a<b)‖ℒ_(K_ab)B‖² = ⟨ΩB, B⟩ = c_π‖B‖² for B ∈ V_π; with B = A_π (length one) and
  B = ℒ_(K_cd)A_π summed over the six (K_cd) (length two, the 36 ordered pairs) the weighted sum over the 43 words is
  exactly (𝔶₀ + 𝔶₁c_π + c_π²)‖A_π‖². Orthogonality of the V_π and ℒ^J A_π ∈ V_π give Parseval for the sum over J; the
  pointwise bound |A_π(ω)|₀² ≤ (dim V_π/(2π²))‖A_π‖² and Cauchy–Schwarz over π are those of lem:tl5-hft-leaf.
- (4/3)(1 + c + c²) − (1 + c)² = (1 − c)²/3 ≥ 0 gives C^♯² ≤ (4/3)C_(E,r)² = (2/9)·6C_(E,r)²; convergence from
  𝔶₀ + 𝔶₁c + c² ≥ min(𝔶₀, 𝔶₁, 1)(1 + c + c²) ≥ min(…)(1 + c)²/2; monotone in 𝔶₀, 𝔶₁.
- r = 0: eq:tl5-hf-sphere's integrand f² + Σ(K_ab f)² + ΣΣ(K_cd K_ab f)² (87:4127) is the sum over the same 43 words.
- Series recomputed (computed; e_j(r) from (2[0] ⊕ [1])^⊗r, m_(j₁j₂)(r) = Σ_(j=|j₁−j₂|)^(j₁+j₂) e_j(r), j₁ ≤ 4000 with the
  1/j₁ tail extrapolated): 6C_(E,r)² = 0.5000, 1.4775, 5.3650, 21.825, 94.259; C^♯² = 0.0873, 0.2618, 0.9551, 3.8832,
  16.727; ratios 0.4177, 0.4209, 0.4219, 0.4218, 0.4213 for r = 0…4. All as printed.

### 2.2 The weights 𝔶₀ ≤ μ⁻², 𝔶₁ ≤ μ⁻¹: allowed by the energies everywhere they are used

- zeroth order: 𝔶_kμ^(|B|+2) ≤ μ^(|B|+k) = μ^(|JB|); first order: 𝔶_kμ^(b+3) ≤ μ·μ^(|JB|) (so even at 𝔶 = 1 the first
  factor is μ^(1/2), not 1); the remainders: 𝔶_kμ^(b+3) ≤ μ^(1+a)μ^(|σB|), |σB| = |JB| − a; the second derivatives:
  𝔬_J² ≤ μ^(|ZJB|) and ≤ μ·μ^(|JB|); the rows of 𝔞_𝔄(𝔚): (𝔶_kμ^(b+3−|K|))^(1/2) ≤ μ^((|JB|+1−|K|)/2). The weighted face
  inequalities follow because (d/dv)|ℒ^J A|₀² ≤ |ℒ^J A|₀² + |ℒ_(∂_γ)ℒ^J A|₀² holds word by word (87:5833-5838).
- 𝔗(𝔶): the ϱ part of the per-word bound of D̂²Ψ_C, |C| = b + k, is k₂ϱ/(1 − 𝔵) (uniform), μ^(−(|C|+1)/2) (hft-small (b))
  or ν^(−(|C|+1)/2) (hfq-theta) times it, i.e. 𝔢_k = 1, μ^((2−k)/2), ν^((2−k)/2) times P_ϱ; on S_a, |Ψ_(JB)| ≤ η₀ and
  η₀ ≤ μ^((2−k)/2)μ^(−(|B|+2)/2)η₀ (resp. ν, r_Φ), the step's form. So Σ_J𝔶_k𝔢_k² = 𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36 = 43𝔗², one
  form per lemma, ≤ 1 under hft-small (b) for every admissible 𝔶, = 1 at 𝔶 = 1 under (a), ≤ 1 at 𝔶 = 1 everywhere.

### 2.3 The seven fields as one family in 𝔨_rec, and 𝔐_p^(m): correct

- lem:tl5-hfp-words: ZJB distinct for distinct (Z, J, B), the B of one length, so the leading term counts once against
  𝒟_g; the 𝔷, 𝔯 terms against 𝒥_g with μ^(1/2); the couplings through 𝔞_𝔄(𝔚). Residual and nonlinear per pair, with the
  refined per-word bound for 𝔐 (shorter words have a smaller ϱ part): 𝔬_J(1 − 𝔵)P_C + 𝔵(2𝒥 + 𝔬_J𝔐) =
  𝔬_JP_C + 𝔵(k₁^D𝒟_g + (k₁^p − k₁^D + 2)𝒥_g)/(1 − 𝔵), using 𝔬_Jμ^(−(|C|+1)/2) ≤ 1. The ℓ² sum over the 43n pairs gives
  (43n)^(1/2) on the nonlinear part and (43n)^(1/2)𝔗μ^((b+3)/2)P_ϱ on the ϱ part.
- Schur for 𝔞_𝔄(𝔚): row sums ≤ 2^(−1/2)α_𝔄^(N−1,μ), 43n rows, so ≤ (43n/2)^(1/2)α_𝔄; stacking the maps over B gives
  ≤ (Σ_B 𝔞_𝔄({B})²)^(1/2).
- lem:tl5-hfp-rec: μ²(Σ_Z|D̂Ψ_Z|²)^(1/2) by the family bound with 𝔚 = Γ (b = 1, n = 7): C₁^Γ in place of √7C₁, √7 on
  the ϱ and η₀ parts; (Σ_Z𝔷_Z²)^(1/2) ≤ 𝔷₁′|D̂h| + 𝔷₂′|h| (Minkowski over Z), μ^(3/2)|D̂h| by C₁^p (B = ∅), μ|h| by
  C_S^p. 𝔨_rec^p, 𝔨_rec^(ϱ,p), 𝔨_rec^(0,p) are as printed. The nonlinear part keeps (7·43)^(1/2); the couplings keep
  √7 through 𝔞_𝔄(Γ) ≤ (301/2)^(1/2)α_𝔄 (0.74 against 0.28 at α_𝔄 = 0.06, as the Comparison says).
- lem:tl5-hfp-low: per length b the families 𝔚_b (7^b words) give C_S^p and C₁(𝔚_b) on ℰ_g and 7^(b/2) on the other
  parts; Minkowski over b and the two kinds, Σ_b 2·7^b = 2𝔐^(m). At 𝔶 = 1, 𝔐_p^(m)² ≤ Σ_b 7^b(C_S² + C₁²) ≤ 2𝔐^(m)max².

### 2.4 The 1/z̲ split: correct

|D̂Ψ_C|² ≤ e_o/(2cΩ̂²) + e_i/(2Ω̂²) ≤ 𝔨₂′(e_o + κ′e_i) with 𝔨₂′ = max(1/c, 1/κ′)/(2Ω̂²) (eq:tl5-hf-coercive), and
𝔨₂ = 𝔨₂′ + 1/(2Ω̂²z̲) (87:4318). Only 𝒟_g-terms (the leading term and μ𝒟_g of the first factor) take 𝔨₂′; z̲ itself and
the rates are untouched. In lem:tl5-hfp-c1, Minkowski in L² and in ℝ² gives the split C₁^D + C₁^J, and 𝒟_g ≤ 𝒥_g gives
C₁^U; both are bounds, so the minimum is.

### 2.5 𝔷′: correct

(Σ_Z𝔷_Z²)^(1/2) ≤ 3(Σ|D̂Z|²)^(1/2)|D̂Ψ| + 2(Σ|D̂²Z|²)^(1/2)|Ψ| ≤ 𝔷′(|D̂Ψ|² + |Ψ|²)^(1/2), and 𝔷′ ≤ 𝔷₁′ + 𝔷₂′ ≤
√7(3max|D̂Z| + 2max|D̂²Z|); the ratio lies in [1/√14, 1] (equality at one field with 3|D̂Z| = 2|D̂²Z|).

### 2.6 K_rec is sharp for its step: correct

The step (87:4060-4064) applies the block-diagonal map (v_Z) ↦ (|T|⁻¹v_T, (Σ c^ab_j v_(K_ab))_j); its norm is
max(|T|⁻¹, ‖C‖), and CCᵀ = M⁻¹ (87:3952-3953, lem:tl5-hf-fields (a)), so ‖C‖ = λ_M^(−1/2), attained. The remark's claim is
limited to that step, as it should be.

### 2.7 The closing condition and the containment: correct

thm:tl5-hfp has the form of thm:tl5-hfz with η_p, A_p, B_p, 𝔰_*^p; ε^z is unchanged (no Sobolev constant in its ϱ
coefficient). At 𝔶 = 1: C^♯² ≤ 6C², 𝔗 ≤ 1, k₁^(j,·,p) ≤ k₁^(j,·,z), C_S^p ≤ C_S^E, C_(1,ϱ)^p ≤ C_(1,ϱ)^z, C_(1,0)^p ≤ C_(1,0),
C_(0,0)^p ≤ C_(0,0); C₁^U({B}) ≤ C₁^z ((μ^(1/2) + ϖ′^(1/2))² ≤ (1 + ϖ′^(1/2))², 𝔩_D + 𝔩_J = 𝔩 with 𝔷′, k₁^p, 𝔞_𝔄({B}));
C₁^Γ ≤ √7C₁^z; 𝔷₁′ ≤ √7𝔷₁, 𝔷₂′ ≤ √7𝔷₂, so 𝔨_rec^(·,p) ≤ 𝔨_rec^(·,z); 𝔐_p^(m) ≤ (2𝔐^(m))^(1/2)max(C_S^E, C₁^z); every
constant is monotone in these, so η_p ≥ η_z and the hypotheses of thm:tl5-hfz (intrinsic choice) imply those of
thm:tl5-hfp. Nothing earlier is edited except the pointer sentence; every earlier closing condition stays valid.

### 2.8 The Comparison's numbers

Item 1 (table, (2/9)^(1/2) = 0.4714, −0.327, −0.375), item 3 ([1/√14, 1]), item 5 (0.74, 0.28), item 6 (√114, √800),
and the weighted ratios at 𝔶 = (μ⁻¹, μ^(−1/2)) reproduce. The ratios at 𝔶 = (μ⁻², μ⁻¹) do not quite: summing to
j₁ ≤ 40000 (with j₁ ≤ 3000 giving the same four digits) I get q₃ = 0.1216, 0.0684, 0.0506 (q₂ = 0.1097, 0.0617, 0.0456)
against the printed 0.1211, 0.0674, 0.0493 (0.1092, 0.0608, 0.0444); the cut at j₁ ≤ 4000 is too short when 𝔶₁ = μ⁻¹ is
large. Hence q₃𝔗 = 0.416, 0.187, 0.212, 0.0928 and the level-4 and level-6 decades −1.165, −0.915, −1.296, −1.165 and
−0.381, −0.729, −0.673, −1.033, against −1.17, −0.92, −1.31, −1.17 and −0.39, −0.73, −0.68, −1.04: at most 0.011
decades. n1.

## 3. Findings

### Major

None.

### minor

None.

### nits

**n1. Comparison item 2 and the level-4/level-6 lines (P:336-341, P:396-397, P:411).** Replacements (fixed copy):

    Summed ratios q_r := C_(E,r)(𝔶)/C_(E,r)^♯, rank 3 (rank 2 in brackets), j₁ ≤ 40000 and the tail extrapolated (the
    cut j₁ ≤ 4000 is too short when 𝔶₁ is large):
        𝔶 = (μ⁻², μ⁻¹):       μ = 10⁻⁴: 0.1216 (0.1097);   10⁻⁵: 0.0684 (0.0617);   3 × 10⁻⁶: 0.0506 (0.0456)
        𝔶 = (μ⁻¹, μ^(−1/2)):  μ = 10⁻⁴: 0.3821 (0.3456);   10⁻⁵: 0.2878 (0.2598);   3 × 10⁻⁶: 0.2478 (0.2236)

"q₃ 𝔗 = 0.41, 0.186, 0.207, 0.0914 … 0.266, 0.351, 0.227, 0.263" → "q₃ 𝔗 = 0.416, 0.187, 0.212, 0.0928 … 0.266, 0.351,
0.228, 0.264"; "further −1.17, −0.92, −1.31, −1.17 (q₃) … further −0.39, −0.73, −0.68, −1.04 (q₃ 𝔗)" → "further −1.165,
−0.915, −1.296, −1.165 (q₃) … further −0.381, −0.729, −0.673, −1.033 (q₃ 𝔗)"; and at level 6 (the same μ, G0l.4)
"further −1.17, −0.92, −1.31, −1.17" → "further −1.165, −0.915, −1.296, −1.165". The totals ("about 2.0, 1.75, 2.0, 1.8")
stand.

## 4. Verdict

The representation theory and the series of the sharp leaf constant, the weights against the energies, the family
argument for the seven fields and for the low levels, the 1/z̲ split, 𝔷′, the sharpness of K_rec for its step, the
closing condition and the containment of thm:tl5-hfz all check. No Major or minor finding is open; one nit in the
Comparison's figures, with a tested replacement (lint 0 hits, assemble --check 0 problems, in-memory `[] 0`, crosswalk
430 = 430, no printed number changed).

Verdict: CONFIRMED
