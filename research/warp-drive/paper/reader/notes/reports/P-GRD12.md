# P-GRD12 report

**File:** proofs/P-GRD12.md (not committed), md5 eec808945bded66de2878a78f1df8bc4, 319 lines.
- Lines 1–183 are the chapter text; Placement, Comparison and Crosswalk follow.
- Source: HEAD b6df4c77, chapter 87 md5 3fdd3474…, 7077 lines.

## What is proved: sec:tl5-hfd (Section 57.27), valid at every level N ≥ 4

The section is inserted after rem:tl5-hfu-what, with one pointer line added after it. It adds 9 labels:

- **Lemma 57.230, lem:tl5-hfd-leaf: one leaf constant for every rank** (target 1).
  - lem:tl5-hft-leaf bounds |A_π(ω)|₀² by the trace of the kernel of V_π at ω. That trace sums the kernel's eigenvalues
    over the 5^r dimensions of the fibre.
  - The kernel commutes with the isotropy SO(3). Splitting the fibre into irreducible pieces U gives homogeneous
    subbundles. By Frobenius reciprocity (multiplicity one in the Clebsch–Gordan series) and Schur's lemma, the kernel at
    o equals dim π P_U/(2π²(2j_U + 1)) on each U.
  - The sharp Cauchy–Schwarz step therefore gives the largest eigenvalue, max_j 𝔖_j(𝔶).
  - An injection (j₁, j₂) ↦ (κ, κ) for each d = j₁ − j₂, together with AM–GM and convexity of c, gives 𝔖_j ≤ 𝔖_0 = C_(E,0)(𝔶)².
  - **Result:** |A(ω)|₀² ≤ C_(E,0)(𝔶)² Σ_J 𝔶_|J| ∫|ℒ^J A|₀² for every rank. Also C_(E,r)² = Σ_j e_j(2j+1)𝔖_j ∈ [1, 5^r]·C_(E,0)².
  - The constant is best for each rank: take A = f du⊗⋯⊗du with kernel functions f.
- **Lemma 57.231, lem:tl5-hfd-words: products summed over the words** (target 2).
  - The monomials "of type D" are the monomials of 2𝔮̂ whose two factors are D̂Ψ. Their four subwords run independently.
  - So they are summed in ℓ² before being bounded. The energy factor is counted once by 𝒥_g, the low factor by 7^(k_P/2)
    with k_P = min(k₃, k₄), and the background factors through λ̂^♮(7μ).
  - These monomials carry 𝔰_P, not 𝔓: they need no recovery constant and no 𝔷.
  - The type-D count is 𝔠^(D,7)_n(μ). All other monomials keep 7^(n/2)(𝔠^♮_n − 𝔠^D_n) and 𝔓, and the parts with ϱ keep the
    old count.
- **Definition 57.232, def:tl5-hfd-constants (index d).**
  - C_(E,0)(𝔶) and C_(E,0)^♯ go into every face constant.
  - 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ replace 𝔤_(𝒥,s)𝔎, 𝔤_(𝒥,s)𝔎_ϱ and 𝔤_(𝒥,s)𝔎₀ in S_F and 𝔯_(w,s).
- **Theorem 57.233, thm:tl5-hfd.**
  - It applies thm:tl5-hfp (N ≥ 6) and thm:tl5-hfu (N = 4) with the constants of index d.
  - Closing condition: 4η_d^(−3/2)(δ_w + η_d^(−1/2)(ε^z + ε_M^d))(S_F^d + S_M^d) < 1, with 𝔰_*^d < 𝔰₁^v.
  - For all weights every constant is at most the old one, so it contains both earlier theorems.
- **Remark 57.234, rem:tl5-hfd-what.**

## Factors

**The leaf constant.** C_(E,0)(𝔶)/C_(E,r)(𝔶) for r = 2, 3, 4:

| Weights 𝔶 | r = 2 | r = 3 | r = 4 |
|---|---|---|---|
| 𝔶 = 1 | 0.302 (−0.52 dec) | 0.150 (−0.82 dec) | 0.0722 (−1.14 dec) |
| 𝔶 = (μ⁻², μ⁻¹) | 0.200 (−0.70 dec) | 0.0894 (−1.05 dec) | 0.0400 (−1.40 dec) |

At (μ⁻², μ⁻¹) the ratios equal 5^(−r/2) to four digits.

**The word sums.** Type-D counts at Λ = 0, against 7^(n/2)𝔠^D_n:

| n | Change |
|---|---|
| 1 | −0.42 dec |
| 2 | −0.58 dec |
| 3 | −0.92 dec |
| 4 (N = 4) | −1.53 dec |
| 6 (N = 6) | −1.55 dec |

## Deduced, not evaluated

**Level 4**
- The leaf lever lowers C_P^v by 1.05 decades. 2C_S falls only 0.70, so 𝔨_rec^p still leads. Both ε limits carry C_P^v,
  so the gain is up to about +1.0 on min(f, ϱ).
- The word sums lower the j′ = 4 term of 𝔤𝔎 by 1.0–1.7 decades and the j′ = 3 term by 0.9–1.5. They act on S_F alone,
  which is what G0n priced as the 7² lever (+0.28/+0.44/0/+0.34).

**Level 6**
- The leaf lever gives up to +0.7 to +1.05 on ϱ.

## Not done

- 1/z̲.
- Further levers on 𝔩 or k₁^D: there are none in this argument.
- Target 3 (ε's coefficient of ϱ): it carries no Sobolev constant.
- The word sums for the non-type-D monomials. The family costs in 𝔨_A and 𝔨_B would pay back part of the gain.
- The 𝒟_g split in S_M.

## Checks

All run in a scratch tree (git archive b6df4c77 plus merge):
- `lint.py --chapters`: 5301 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- In-memory check: `[] 0`.
- 0 of the 5292 existing label numbers changed; 9 added.
- Crosswalk: 450 rows for 450 labels, in order.
- The Placement quotes match the source lines.
