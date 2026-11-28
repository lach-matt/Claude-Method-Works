# R-P-GRD13: an independent review of proofs/P-GRD13.md (sec:tl5-hfe)

**File reviewed:** research/warp-drive/paper/reader/proofs/P-GRD13.md at 3b2784e4, md5 f1467bc970c05eb14befdcd0cc378d75,
403 lines. It has four parts:
- the chapter text, P:1–237, with 10 labels;
- the placement, P:239–260;
- the Comparison, P:262–388;
- the crosswalk rows, P:390–403.

The writer's report is notes/reports/P-GRD13.md, and the handoff notes are notes/reports/P-GRD13-handoff.md.

**Base:** chapters/87-ten-l5.md, md5 b8c2cff2a533d23139d4978ab065552c, 7265 lines, 5,301 labels. It is unchanged since
cee5c801. P:n refers to the proof file and 87:n to the chapter.

**Verdict: CONFIRMED.** There are 0 Major and 0 minor findings, and 5 nits.
- One nit is in the chapter text, in the opening paragraph.
- Four nits are in the Comparison.
- A tested fixed copy is provided. It leaves P:19–237 byte-identical and moves no label.

## 1. Mechanics

The scratch tree was built from `git archive HEAD`, using the writer's placement.

- **Item 2.** The two old lines are found exactly at 87:7264–7265. The new pointer line is 117 characters, as stated.
  "Line 7266, as changed by item 2" is right. The chapter becomes 7504 lines.
- **Checks.**
  - lint.py --chapters: 0 hits, 5311 labels (5301 + 10).
  - assemble.py --check: 0 problems.
  - In-memory check: `[] 0`. Plain `python3 assemble.py` was not run.
- **Crosswalk.**
  - All 10 rows give the line of their label.
  - 460 = 460, and the labels are lowercase.
  - None of the 5,301 existing printed numbers changes.
  - The descriptions match their labels.
- **Format.**
  - The longest line of chapter text is 120 characters.
  - No wrapped line of chapter text starts with a forbidden marker. The START flags fall only on the Comparison's
    bullets, P:343 onward.
  - There are no file or program names, no code and no AI language in P:1–237.
- **Numbering.** sec:tl5-hfe assembles as Section 57.28: Lemma 57.235 (lem:tl5-hfe-face), Lemma 57.236
  (lem:tl5-hfe-rho), Definition 57.237, Theorem 57.238, Remark 57.239, and displays (57.163)–(57.166). The writer's
  report (its lines 9–10) agrees.

## 2. lem:tl5-hfe-face (P:20–67): the transport with a variable weight holds

I checked each form against lem:tl5-hf-sobolev (87:4165–4203), lem:tl5-hf4-face (87:4684–4740), lem:tl5-hft-face,
lem:tl5-hfp-abs (a) and lem:tl5-hfu-face.

**No derivative of 𝔲 appears.**
- The weight never sits inside the quantity being differentiated. Along γ_ω, (d/dv)|B|₀² = 2⟨B, ℒ_(∂_γ)B⟩₀, because
  h₀ has constant coefficients and κ′ is constant, so ℒ_(∂_γ)h₀ = 0.
- That derivative is bounded at each point by 2|B|₀|ℒ_(∂_γ)B|₀ ≤ 𝔲|B|₀² + 𝔲⁻¹|ℒ_(∂_γ)B|₀². This is a pointwise
  inequality between numbers, valid for any value 𝔲 > 0 at that point.
- Only g_J(v) = ∫|ℒ^J A|₀²(γ_ω(v))dω is integrated in v. So 𝔲 needs no differentiability. Positivity and continuity
  on D̄ only make the suprema finite, and a positive bounded measurable weight would do as well.

**The integration.** g_J(v_p) − g_J(1/2) = ∫ g_J′ dv ≤ ∫∫(𝔲|B|₀² + 𝔲⁻¹|ℒ_(∂_γ)B|₀²) dω dv, with
dω dv = R⁻³ dμ dτ₂/(1 − κκ′). ✓

**The boundary term.** The only one is g_J(1/2) on S_a. It carries no 𝔲, and the bound by sup 𝔳₀^(2r)∫_(S_a)|ℒ^J A|²
is unchanged. The η₀ parts that come from S_a are therefore unweighted, as the Remark says. ✓

**(a)** |ℒ_(∂_γ)B| ≤ |∂_γ||D̂B| + r|D̂∂_γ||B| (torsion free; the proof of lem:tl5-hf4-face). Squaring with
(x + y)² ≤ 2x² + 2y² gives 𝔲 + 2r²𝔲⁻¹|D̂∂_γ|² and 2𝔲⁻¹|∂_γ|² exactly. The leaf inequality eq:tl5-hfd-leaf with the
weights, and |A| ≤ 𝔴₀^r|A|₀, give the leading factor. ✓

**(b)** |ℒ_(∂_γ)B| ≤ |D̂_(∂_γ)B| + 2|D̂∂_γ||B| gives (𝔲 + 8𝔲⁻¹|D̂∂_γ|²)|B|² + 2𝔲⁻¹|D̂_(∂_γ)B|². Then the density bounds
|D̂_(∂_γ)B|² ≤ 𝔨₁(e_o + κ′e_i) and |B|² ≤ (e_o + κ′e_i)/(2Ω̂²z̲) give the C_S coefficient
(𝔲 + 8𝔲⁻¹|D̂∂_γ|²)/(2Ω̂²z̲) + 2𝔲⁻¹𝔨₁. C_(S,0) is unchanged. ✓

**(c)** In lem:tl5-hf4-face (a), the factor e^(−φ(v)) is handled by e^(−φ(v)) ≤ e^(−φ(v′)) for v′ ≤ v and by e^(−φ) ≤ 1.
That step does not depend on how the integrand was bounded. So the weighted integrand passes through, giving
𝔱_(r,0)(t; 𝔲) and 𝔱_(r,1)(t; 𝔲) as separate suprema. ✓

**At 𝔲 = 1** the three forms are exactly those of index d:
- eq:tl5-hf-cs-r intrinsic, with C_(E,0)(𝔶)²;
- lem:tl5-hft-face (b) with the weights;
- eq:tl5-hfu-face. ✓

## 3. lem:tl5-hfe-rho (P:69–124): holds, and no other monomial carries a part with ϱ

**Which monomials have a ϱ part.** I checked this against lem:tl5-hfs-products (87:5592–5612), lem:tl5-hft-products
(87:5892–5903) and lem:tl5-hfq-theta (87:6017–6064).
- In each of these lemmas, the term with ϱ(p) of a monomial comes only from its factor Φ₂ when Φ₂ = D̂²Ψ_C. That
  factor is bounded by eq:tl5-hfs-m2, eq:tl5-hfq-m2, or the M_g bound of lem:tl5-hft-small (b).
- Otherwise Φ₂ ≤ 𝔨_B𝒥_g, with no ϱ.
- A low D̂²Ψ_B taken as Φ₁ is bounded by μ^(−ℓ_P/2)𝔰_P, also with no ϱ.
- There are at most two D̂ on the solution factors, so a monomial has at most one second derivative.
- Hence the monomials with a ϱ part are a subset of those with a factor D̂²Ψ_C, and (a) counts all of the latter. ✓

**Which monomials have a factor D̂²Ψ_C.** I checked the factors of the second expansion of lem:tl5-hfg-quadratic,
using (ii)–(iv) of lem:tl5-hf-quadratic and lem:tl5-hfs-quadratic (a).
- ℒ^J D̂h has solution factors D̂Ψ_J and Ψ_B.
- ℒ^J D̂²h is D̂²Ψ_J, with coefficient 1, plus monomials in D̂Ψ or Ψ. The commutator [ℒ_Z, D̂²] gives Γ′ ⋆ D̂Ψ and
  D̂Γ′ ⋆ Ψ, and further Lie derivatives of D̂Ψ_C give D̂Ψ and Ψ again.
- ℒ^J g⁻¹ has only factors Ψ_B, besides background factors and factors g⁻¹.
- ℒ^J h = Ψ_J. ℒ^J R̂ and ℒ^K ĝ⁻¹ are background factors.
- Of the terms of Q and R₃, only H₁^(λσ)D̂_λD̂_σh and H₂^(λσ)D̂_λD̂_σh have a factor D̂²h. The other terms are
  2𝔠(H₁)h and 2𝔠(H₂)h (H, R̂, h), 2𝔮̂ (ĝ⁻¹, ĝ⁻¹, D̂h, D̂h) and 2𝔮 − 2𝔮̂ (H = −g⁻¹hĝ⁻¹, g⁻¹, D̂h, D̂h).
- So a D̂²Ψ_C comes only from the leading term of ℒ^K D̂²h in these two terms. ✓
- The terms with ϱ of ε also include the forcing 2R̂ic (unchanged) and the 𝔑^M_I terms. The 𝔑^M_I terms enter 𝔯_M and
  ε_M, not ε, and are unchanged. The ϱ parts inside 𝔓 (𝔎_ϱ) enter 𝔯_(w,s), not ε. So 𝔤_ϱ counts exactly the
  monomials above. ✓

**The count.**
- In H₁^(λσ)D̂_λD̂_σh (ĝ⁻¹, h, ĝ⁻¹, D̂²h; q = 2), the lettered ĝ⁻¹ factors are bounded by λ^♮_(k₁) and λ^♮_(k₃).
- Unlettered joining ĝ⁻¹ count 1, and b = k₁ + k₃, so νν′^(b/2) = λ^♮_(k₁)(ν′)λ^♮_(k₃)(ν′).
- The subtracted H₁D̂²Ψ_I is the term with k = (0, 0, 0, n), of value 1.
- In H₂^(λσ)D̂_λD̂_σh (g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h; q ≥ 3, so 𝔰^(q−2) ≤ 𝔰_♭), ℒ^(I₁)g⁻¹ is bounded by
  b^♮_g(k₁, ν′). The extra solution factors Ψ_(B_i) of its expansion carry no background letter and raise q only.
- The subtracted H₂D̂²Ψ_I is the term of value 𝔤₀.
- This gives eq:tl5-hfe-rho. ✓

**(b), the weights per lemma.** For each lemma I checked the factor that multiplies νν′^(b/2)𝔰^(q−2).
- lem:tl5-hfs-products: μ^(n/2)2k₂𝔰ϱ, with ν′ = 1.
- lem:tl5-hft-products: ν𝔰^(q−1)μ^((n−ℓ_E)/2)2k₂ϱ ≤ νμ^(b/2)𝔰^(q−2)μ^(−1/2)2k₂𝔰ϱ, with ν′ = μ.
- lem:tl5-hfq-theta: μ^(n/2)ν^(−ℓ_E/2) ≤ μ^((1−θ)n/2)ν^(−1/2)ν^(b/2), with ν′ = ν.
- The second inequality takes the "+1" from H^(αβ)D̂_αD̂_βΨ_J, which has a ϱ part. ✓
- The later forms (index v, w, z, p) use the same counts with k₂^z/(1 − 𝔵^z) in place of 2k₂ (thm:tl5-hfz,
  87:6578–6579). So the replacement passes to 𝔤_ϱ^v and ε^z as the theorem says. ✓

**0 ≤ 𝔠^ϱ_n ≤ 𝔠^♮_n − 𝔠^D_n.**
- Lower bound: the k = (0, 0, 0, n) term is 1 and the term with all letters on D̂²h is 𝔤₀.
- Upper bound: β₁, β₂ ≥ 1 and the other sums are nonnegative, so 𝔠^(2♮) ≥ (Σ⁴λλ − 1) + 𝔠^D and
  𝔠^(3♮) ≥ Σ⁶b_gλλ − 𝔤₀. ✓

**The count at Λ = 0**, recomputed by brute-force enumeration of Σ^m_n, with 𝔤₀ = √5 + 1/4, 𝔤₁ = 1 + 2𝔰_♭ and
b_g(k) = Σ_r r!S(k, r)𝔤₁^(r+1).

| n | 𝔠^♮ + 1 (𝔰_♭ = 10⁻⁴) | 𝔠^ϱ + 1 (10⁻⁴) | 𝔠^♮ + 1 (𝔰_♭ = 10⁻⁶) | 𝔠^ϱ + 1 (10⁻⁶) |
|---|---|---|---|---|
| 0 | 81.019 | 1 | 81.000 | 1 |
| 1 | 162.069 | 2.0006 | 162.001 | 2.00001 |
| 2 | 324.279 | 4.0029 | 324.003 | 4.00003 |
| 3 | 649.351 | 8.0132 | 648.014 | 8.00013 |
| 4 | 1304.145 | 16.070 | 1296.081 | 16.0007 |
| 5 | | | 2592.615 | 32.005 |
| 6 | | | 5189.647 | 64.038 |

- Every entry of the table at P:329–334 reproduces.
- The ratio is 0.01234–0.01235, which is −1.91 decades, in every column printed.
- 𝔠^♮₄ − 𝔠^D₄ = 23.14 at the floor, which agrees with G0n's 1303 (15 + 𝔰_♭𝔠^(3♮)₄).
- At Λ = 0, 𝔠^ϱ_n + 1 = 2^n and 𝔠^♮_n + 1 = 81·2^n, up to 𝔰_♭ terms, as stated.

## 4. def:tl5-hfe-constants and thm:tl5-hfe (P:126–213): hold

**The constants.**
- C₁^(U,l), C₁^(D,l), C₁^(J,l) and C_(1,ϱ)^l are C₁^U, C₁^D, C₁^J (def:tl5-hfp-constants) and C_(1,ϱ)^z (eq:tl5-hfz-c1,
  87:6462). They carry the index-d leaf constant, and the f and W of lem:tl5-hfp-c1's proof (87:6772–6810) are replaced
  by 𝔳₀⁶R⁻³(𝔲₁ + 18𝔲₁⁻¹|D̂∂_γ|²) and 2𝔲₁⁻¹|∂_γ|²𝔳₀⁶R⁻³.
- That proof uses f and W only as nonnegative functions: Minkowski's inequality, ∫g𝒟_g² ≤ sup(g𝔨₂′)ℰ_g and
  ∫g𝒥_g² ≤ sup(g𝔨₂)ℰ_g, and V² = ∫Wy² for C_(1,ϱ). ✓
- C_S^l is the form of (b). 𝔜^l and 𝔜′^l are the form of (c) in the Y₁ step of lem:tl5-hfu-mixed. Y₂ keeps 𝔲 = 1. ✓
- 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t) and 𝔤^l_(ϱ,q) are 𝔤_(ϱ,s), μ^(−1/2)𝔤_(𝒥,s) and 𝔤_(ϱ,q) (def:tl5-hfs-constants,
  def:tl5-hft-constants, def:tl5-hfq-constants) with 𝔠^ϱ at the same argument (1, μ, ν).
- 𝔤_ϱ^l is selected exactly as 𝔤_ϱ^v is in def:tl5-hfw-constants (87:6267–6268).
- ε^l has the form of ε^z (87:6562). ✓

**Containment at 𝔲₀ = 𝔲₁ = 𝔲_M = 1.**
- Every constant with index l equals the index-d one. 𝔤_ϱ^l ≤ 𝔤_ϱ^v term by term, since 𝔠^ϱ ≤ 𝔠^♮.
- So ε^l ≤ ε^z, η_l = η_d (𝔯 holds no 𝔤_ϱ), B_l = B_d, A_l ≤ A_d and 𝔰_*^l ≤ 𝔰_*^d.
- Hence thm:tl5-hfd is contained, and through it every earlier theorem in the range where thm:tl5-hfd contains it.
  Nothing earlier is edited. ✓

**"A per-constant minimum would not be valid": correct.**
- One application of a face step at p, with one weight, gives one inequality, D̂Ψ_B(p) ≤ C₁(𝔲)ℰ^(1/2) +
  C_(1,ϱ)(𝔲)ϱ + E₀. Its three parts are split only afterwards, by Minkowski's inequality.
- Two weights give two valid inequalities, but min_𝔲 C₁(𝔲)ℰ^(1/2) + min_(𝔲′) C_(1,ϱ)(𝔲′)ϱ is the sum of parts of
  different inequalities, and it bounds nothing.
- Step 3 then uses the parts together, through 𝔰_P ≤ C_P e^(φ/2)Y_s + C_(P,ϱ)ϱ + C_(P,0)η₀.
- What is valid, and what the definition does, is to give each separate application its own weight: zeroth order,
  first order and the Y₁ step.
- Since C_(1,ϱ)^l carries 𝔲₁⁻¹ and C₁'s optimum has 𝔲₁ = (Y/X)^(1/2) ≫ 1, the shared weight costs nothing in practice. ✓

**The remaining changes in the proof.**
- The zeroth-order, first-order and Y₁ changes are as stated.
- The ϱ change is Step 2 of prop:tl5-hfs/hft/hfq-bootstrap with 𝔠^ϱ + 1 in place of 𝔠^♮ + 1, and then the 𝔰 ≤ 𝔰₁^v
  bound of thm:tl5-hfw/hfz. ✓
- The bounds that are built from the steps (lem:tl5-hfp-rec, lem:tl5-hfp-low, lem:tl5-hfv-rec, C_(∞,μ)) use them
  through their values only. The thresholds and the absorption carry no Sobolev constant. ✓

**The Remark.**
- The least value 2(XY)^(1/2) ≤ 2^(3/2)|∂_γ|𝔩′X^(1/2) + 6√2|D̂∂_γ|X is right.
- The value at 𝔲₁ = 1 is ≥ 2|∂_γ|²𝔩′². ✓
- 𝔨_♯ ≥ √5 (rem:tl5-hfz-what). ✓

## 5. The Comparison

**Item 1.**
- The bracket algebra checks: (2(XY)^(1/2)/(X + Y))^(1/2) ≤ 2^(1/2)(X/Y)^(1/4), and (r + 1/r)/2 at 𝔲 = r𝔲*.
- 𝔲₁ := (Y/X)^(1/2) is a positive continuous function on D̄. X ≥ μ > 0, and Y ≥ 2|∂_γ|²(k₁^D)² > 0.
- X and Y do not depend on p or on h₀, so 𝔲₁ is pointwise optimal for its family on every face.
- The unchanged list is right. In particular C_(P,0)^v, 𝔨_rec^(0,p), C_((∞,0),·), 𝔎₀ and 𝔎^D₀ carry only the S_a
  constants (lem:tl5-hfp-low, 87:6822–6834).

**Item 2.** The table reproduces (§3).
- "55–117" and "1338–1402" are G0o line 30 and G0n's medians plus 1.
- Without the pairing of medians, the fall of the j′ = 4 term is at least −1.06 to −1.41 decades.

**The deduced figures**, recomputed:
- The factor (2(μ/13)^(1/2))^(1/2) gives −1.378, −1.128, −1.628 and −1.378 at the level-4 μ, and −1.509 at
  μ = 3 × 10⁻⁶.
- The S_M cap: with S_F falling by the C_P^v fall x, the cap is ΔB(x) + spare, with ΔB(x) = log(1 + 10^(−gap)) −
  log(10^(−x) + 10^(−gap)).
  - Seed 1 D_A gives 1.09; seed 2 D_A gives 0.94–1.03 for x = 1.13–1.37.
  - The D* cases give 1.92 and 1.60–1.70, so they are not capped.
- C_S falls by 0.07–0.31 for X = 280–390 and Y = 6–50, with X = (3/4)𝔨₂ (G0j line 85).

**The figures cited from the reports all match:**
- C_P^v 1.29/1.37/1.44/1.55 above 2C_S, S_M 1.29/1.10/1.69/1.67 below S_F, spares 0.08/0.09, ε × 0.1 at
  +0.15/+0.23/+0.08/+0.20, ϱ 0.03–0.11 above f, and the other-monomials lever at +0.21/+0.34 (G0o);
- the k-part at 93–95.5 % (G0l lines 109 and 156–157);
- 𝔨₂ = 10^2.57–2.72 (G0j);
- level 6 at +0.99/+0.97/+1.00/+0.85 with f 0.12–0.51 above ϱ (G0o.3), and G0m's level-6 μ.

**Two remarks, not findings.**
- **X ≈ μ needs 24.5μ^(1/2)Λ₁ ≪ 1 at the supremum.** G0j measured ϖ′ ≤ 10⁻⁶ at C₁'s supremum, so ϖ′^(1/2) ≤ 10⁻³.
  That is small against μ^(1/2) at μ ≥ 10⁻⁵ whatever the scaling, and at μ = 10⁻⁶ because ϖ′ scales as μ². The
  evaluation computes X in any case.
- **The handoff notes say "G0n prices it at ≤ 0.03"** for the √7 on 𝔞_𝔄(Γ). G0n contains no such figure; its only
  "≤ +0.03" is the 1/z̲ lever in D* (G0n line 117). See n4.

## 6. Findings (all nits)

**n1 (nit), chapter text P:10–11.**
- **Text.** "and Y from their derivatives D̂ℒ^J D̂Ψ_B, which carry the recovery constant".
- **Why.** Y = 18|D̂∂_γ|²X + 2|∂_γ|²𝔩′² is the coefficient of 𝔲⁻¹, that is of |ℒ_(∂_γ)B|². Its part 18|D̂∂_γ|²X comes
  from the first derivatives themselves, through |D̂∂_γ||B|. The Remark (P:222) states this correctly.
- **Replacement (tested).** "and Y from their Lie derivatives along the curves, that is from their derivatives D̂ℒ^J
  D̂Ψ_B, which carry the recovery constant, and from the terms with D̂∂_γ."
- The paragraph is re-wrapped within its 16 lines, so no label moves.

**n2 (nit), Comparison P:337–339: what 𝔠^ϱ drops.**
- **Text.** "the β₁ − 1 and λ̂_(k≥1) in 16Σ⁴λ̂λ̂β₁β₁".
- **Why.** The terms λ̂_(k≥1) with β₁ = 1 are in 𝔠^D, not in 𝔠^♮ − 𝔠^D. The sentence also omits the 𝔰_♭ parts.
- **Replacement (tested).** "Of 𝔠^♮ − 𝔠^D, 𝔠^ϱ drops 5Σ⁵λλΛ^R (whose terms with k₄ = 0 carry Λ^R₀ = |R̂| undamped by
  ν′), 16Σ⁴λ̂λ̂(β₁β₁ − 1), Σ⁴λλ(β₂ − 1) and the corresponding parts of 𝔰_♭𝔠^(3♮), and keeps Σ⁴λλ − 1 and
  𝔰_♭(Σ⁶b_gλλ − 𝔤₀)."

**n3 (nit), Comparison P:342–348: an assumption is missing.**
- **Why.** The falls of C₁ (P:350) and of C_S (P:360) are computed at the supremum of each constant for 𝔲 = 1. With the
  weights, the supremum can move to points where Y/X is smaller and the fall is less.
- The earlier Comparisons listed "every supremum at one point" as an assumption, and G0o found the last such deduced
  fall too optimistic (−0.34 to −0.44 measured against −1.0 to −1.65 deduced).
- **Replacement (tested):** a new assumption bullet, "every supremum at one point: the falls below are those at the
  supremum of each constant for 𝔲 = 1. With the weights the supremum may move to points where Y/X is smaller, where
  the fall is less, so these are upper figures."

**n4 (nit), Comparison P:384.**
- **Text.** "The √7 on 𝔞_𝔄(Γ): ≤ 0.03 (G0n)".
- **Why.** G0n does not price this lever. It takes 𝔞_𝔄 at its trivial bounds (G0n.4, line 150).
- **Replacement (tested).** "The √7 on 𝔞_𝔄(Γ): skipped. No report prices it; G0n takes 𝔞_𝔄 at its trivial bounds
  (G0n.4)."

**n5 (nit), Comparison P:385–387.**
- **Text.** "both parts … are bounded together by 𝒥_g², so the balance gives nothing there".
- **Why.** Because the two norms are bounded together, the bound is max(𝔱_(2,0)(t; 𝔲), 𝔱_(2,1)(t; 𝔲))𝒥_g², and a
  weight lowers that maximum wherever the two coefficients differ. For example, with |D̂∂_γ| = 0 and 2|∂_γ|² = 9,
  max(1, 9) = 9 becomes max(𝔲, 9/𝔲) = 3 at 𝔲 = 3. The lever is small only because it acts on S_M's 𝔠^Mq₂ term alone.
- **Replacement (tested).** "so the bound is max(𝔱_(2,0)(t; 𝔲), 𝔱_(2,1)(t; 𝔲)) 𝒥_g², and a weight lowers that maximum
  where the two coefficients differ; it acts only on S_M's term with 𝔠^Mq₂, and S_M is 1.1–1.7 decades below S_F
  (G0o.1)."

## 7. The fixed copy

**Location:** /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd13/P-GRD13.fixed.md

- md5 ce2c5cc4a36fbaafec6084be34fff3e8, 406 lines.
- Made by /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd13/tools/fix.py.
  Each old text occurs exactly once.
- The chapter text keeps its 237 lines, and P:19–237 is byte-identical to the original. The crosswalk rows are
  therefore unchanged.

**Re-merged in a fresh tree:**
- item 2 at 7264;
- lint: 0 hits, 5311 labels;
- check: 0 problems;
- `[] 0`;
- crosswalk: 10 of 10, 460 = 460;
- 0 existing numbers changed;
- the longest line of chapter text is 120 characters.

## Verdict

**CONFIRMED.** There are 0 Major and 0 minor findings, and 5 nits; the fixed copy repairs all five.
- The transport step with a variable weight is sound. No derivative of 𝔲 arises, and the boundary term is unweighted.
- No monomial outside the leading D̂²Ψ_K terms of H₁D̂²h and H₂D̂²h carries a ϱ part. The count 𝔠^ϱ and the
  2^n : 81·2^n table reproduce.
- thm:tl5-hfd is contained at 𝔲 = 1.
- One weight per step is necessary.
