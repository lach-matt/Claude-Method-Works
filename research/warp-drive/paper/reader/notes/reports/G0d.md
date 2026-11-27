# G0d: the sharpened constants of P-GRD at levels 4 and 6, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing; I read nothing under method/, drive/, extracted/ or
recovered/. Read for this report: proofs/P-GRD.md (md5 68240c7f…, the whole file) and notes/reports/P-GRD.md, and the
merged sec:tl5-hf4 of chapter 87 (def:tl5-hf4-levels to thm:tl5-hf4, for 𝔛_t, 𝔜_t, 𝔵_r, 𝔱_r, 𝔪 and the ungraded triple).

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0d/` (§G0d.7);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0b, G0c, S-APP, N-APP1, P-GRD or chapter 87, cited.

**Evaluated as in G0c.**
- Same provisional approximants (`appC_R528_264_40_48.npz` for seed 1, `appC2_…` for seed 2), same 48 × 37 × 15 grid, same
  bulk matrix 𝔅_N and LP rates. G0c's stored rates are reused wherever the μ was already computed, and new LPs were run
  for μ = 3 × 10⁻⁷ and 10⁻⁷ and for the level-4 reach.
- Same couplings (exact same-level norms), same derivative-growth model, κ = κ′ = ϑ = 10⁻².

**Targets** use the new closing conditions, G0b's margin of 10 and δ_w ≤ ε:
- level 6: 8(√2δ_w + 2ε_(w,g))S_(F,g) ≤ 0.1, together with 𝔯_(w,g) ≤ 1/40, η₀ < 𝔰₁^⋆ and 𝔰_(*,g) < 𝔰₁^⋆;
- level 4: 8(√2δ_w + 2ε_(w,g) + 2ε_(M,g))(S_(F,g) + S_(M,g)) ≤ 0.1, with 𝔯_(w,g) + 𝔯_(M,g) ≤ 1/40.

M_w := 8√2(S_(F,g) + S_(M,g)), so the closing reads M_w(δ_w + √2 ε) < 1. f bounds max over |I| ≤ N of μ^(|I|/2)|ℒ^I f_ab|,
in curvature units. ϱ and η₀ are absolute. The closing condition binds in every case below.

**Choices among P-GRD's options.**
- 𝔠^⋆ = 𝔠^g (𝔰_♭ = 1/8), or 𝔠^Q + 𝔰_♭𝔠^(3) with 𝔰_♭ ∈ {10⁻², 10⁻⁴, …, 10⁻¹²}.
- At level 4, the graded or the ungraded triple.
- μ ∈ {10⁻³, 3 × 10⁻⁴, …, 10⁻⁷}.
- Each entry gives the choice with the loosest f. The best is 𝔠^Q with 𝔰_♭ ≤ 10⁻¹², where 𝔰_♭ no longer binds, so that
  𝔠^⋆ is effectively 𝔠^Q. It is 1.1–1.8 decades better than 𝔠^g. The graded triple is 2.4–2.8 decades better than the
  ungraded.

**Checks of the implementation of eq:tl5-hfg-cn** (computed against P-GRD's own computed values):
- all bounds 1: 𝔠^g_n = 104 … 9.75 × 10¹⁰, 𝔠^Q_n = 85 … 4.58 × 10⁶, 𝔠^(3)_n = 200 … 1.21 × 10¹¹;
- the seed: 𝔠^Q_n = (81 + 5|R̂|)2^n − 1.
All three agree digit for digit.

---

## G0d.0 Headline (computed; log₁₀M_w; targets; optimal μ)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **Level 4, P-GRD, graded triple**: M_w | **60.9** | **61.3** | **77.7** | **71.1** |
| f / ϱ / η₀ | 10^−66.3 / 10^−86.8 / 10^−60.7 | 10^−66.7 / 10^−89.8 / 10^−61.1 | 10^−83.7 / 10^−107.0 / 10^−77.6 | 10^−77.0 / 10^−101.8 / 10^−71.0 |
| 𝔰₁^⋆; μ | 6 × 10⁻¹⁵; 10⁻⁵ | 1 × 10⁻¹⁵; 10⁻⁴ | 7 × 10⁻¹⁹; 10⁻⁶ | 7 × 10⁻¹⁸; 10⁻⁵ |
| Level 4, P-GRD, ungraded triple: M_w; f; η₀ | 63.3; 10^−68.8; 10^−54.1 | 63.3; 10^−68.7; 10^−55.1 | 80.5; 10^−86.5; 10^−69.4 | 73.6; 10^−79.5; 10^−64.4 |
| **Level 6, P-GRD**: M_w | **92.1** | **94.1** | **107.3** | **103.6** |
| f / ϱ / η₀ | 10^−98.4 / 10^−149.1 / 10^−84.3 | 10^−100.3 / 10^−156.2 / 10^−86.0 | 10^−114.1 / 10^−170.6 / 10^−96.0 | 10^−110.4 / 10^−169.1 / 10^−93.1 |
| 𝔰₁^⋆; μ | 4 × 10⁻³⁷; 10⁻⁵ | 1 × 10⁻³⁹; 3 × 10⁻⁵ | 1.5 × 10⁻⁴³; 10⁻⁶ | 2.5 × 10⁻⁴²; 3 × 10⁻⁶ |
| Reach (dd f ≥ 10⁻²⁰ / qd f ≥ 10⁻³⁵), levels 4 and 6 | none / none | none / none | none / none | none / none |
| Pages at the f target (level 4; level 6) | 24,152; 95,617 | 28,033; 114,268 | 120,878; ≈ 3.8 × 10⁵ | 67,315; ≈ 2.5 × 10⁵ |

**What the sharpened constants achieve, and what they do not:**
- **Level 6 improves by 34–38 decades** on G0c's "as written" row (126.5, 127.8, 145.0, 139.2). It remains NO-GO
  everywhere.
- **Level 4 is now 30–33 decades better than level 6.**
- **No reach at either precision**, at either level, for any u\* ≥ −9: at u\* = −9, f ≤ 10^−55.9 at level 4 and
  ≤ 10^−86.5 at level 6.

**Correction to G0c.** G0c's level-4 rows evaluated P-HF's level-6 formulas at N = 4 and omitted the mixed term S_M of
the merged thm:tl5-hf4. With it (computed, the merged S_M at G0c's rates and μ), the merged level 4 as written is about
83.5, 84.4, 101.8 and 94.9, not 72.2, 74.7, 87.2 and 84.0. At level 4, S_M dominates S_F.

## G0d.1 Against G0c's rows (log₁₀M_w; computed, except G0c's own rows, which are record)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| L6 as written (G0c) | 126.5 | 127.8 | 145.0 | 139.2 |
| **L6 P-GRD (proved)** | **92.1** | **94.1** | **107.3** | **103.6** |
| L6 "both levers" (G0c's estimate) | 65.1 | 66.2 | 79.5 | 75.6 |
| L6 per-factor lever (below, deduced) | 59.5 | 59.4 | 74.2 | 70.5 |
| L6 G0b-type constants, μ^(−N/2) (G0c) | 24.3 | 21.3 | 31.6 | 26.3 |
| L6 G0b-type constants, μ^(−3/2) (P-GRD's power) | 16.8 | 15.0 | 22.7 | 18.7 |
| L4 merged as written, with S_M (corrected) | ≈ 83.5 | ≈ 84.4 | ≈ 101.8 | ≈ 94.9 |
| **L4 P-GRD, graded triple (proved)** | **60.9** | **61.3** | **77.7** | **71.1** |
| L4 "both levers" (G0c, without S_M) | 43.4 | 46.7 | 57.3 | 55.3 |
| L4 per-factor lever | 50.3 | 50.8 | 65.8 | 61.6 |
| L4 G0b-type constants, μ^(−3/2) | 15.4 | 13.7 | 20.6 | 17.3 |

**Why the proved figures sit 27–28 decades above G0c's "both levers" estimate at level 6** (deduced from the formulas,
with the sizes computed):
1. **P-GRD grades the expansion of ℒ^K ĝ⁻¹ by the order of the whole factor, not of each piece.** It uses
   b_g^g(k) = F_k𝔤₀^(k+1)(Λ_k + 1)^k and λ_k = Σ r!S(k,r)5^((r+1)/2)Λ_k^r, so every one of the r pieces is bounded by
   Λ_k. G0c's variant used Λ_(k−1)Λ₀^(k−1).
2. **𝔤_(N,g) carries no μ^j weights.** P-GRD absorbs them into the single μ^(−3/2). With 𝔠^⋆₆ ≈ 10⁵¹–10⁵⁹, the top
   term 7^(N/2)𝔠^⋆₆ is no longer suppressed by μ^(N/2), as G0c's estimate assumed.
3. **What P-GRD gains instead:** μ^(−3/2) in place of μ^(−N/2), 𝔠^Q in place of 𝔠^g, and k₁^(1) and 𝔐^(1) = 57 in C_P.

The **per-factor lever** bounds each piece ℒ^(B_i)ĝ by its own Λ_(|B_i|) and uses Λ_aΛ_b ≤ Λ₁Λ_(a+b−1), which holds
for the factorial growth measured. In b_g and λ_k this turns (Λ_k + 1)^k into (Λ_k + 1)(Λ₁ + 1)^(k−1). It is computed as
a variant and deduced, not proved in P-GRD. It lands 5–7 decades below G0c's estimate.

## G0d.2 What dominates now (computed maxima at the optimal μ; log₁₀ of each factor)

**Level 6, S_(F,g)** (seed 1 D_A, with seed 1 D\* in brackets):
- 𝔤_(6,g) = 54.2 (61.8). Here 𝔠^Q₆ = 51.7 (59.3), carried by Λ₆^6-type products: Λ₆ ≈ 2.6 × 10⁷ (4.5 × 10⁸), the
  seventh derivatives of π at the wave's peak;
- C_P = 19.0 (21.9). It is made of C₁^g 14.7 (17.1), k₁^(1) 3.0 (3.7), √114 1.0 and the factor 2;
- 𝔨_g = 2k₁ + 2 with the top-level k₁: 8.6 (10.0);
- μ^(−3/2): 7.5 (9.0);
- the rest (e^(φ/2), 2Ω̂(1 + 1/z̲ + 1/c)^(1/2), the integral): about 2.
- Seed 2 is similar, with 𝔤_(6,g) = 58.1 (D_A) and 61.2 (D\*).

**Level 4.** S_(M,g) exceeds S_(F,g) by 6–11 decades:

| | seed 1 D_A | seed 1 D\* |
|---|---|---|
| log₁₀S_(M,g) | 59.9 | 76.7 |
| log₁₀S_(F,g) | 52.6 | 66.1 |

At the dominant face (u = −2.02, the u\* edge, at seed 1 D_A; the same breakdown at u\* = −1.1 for seed 1 D\* in
brackets), m_t^g is made of:
- [𝔠^⋆₄]_t: 23.1 (28.4), from (Λ₄ + 1)^4 with the face supremum Λ₄ ≈ 3 × 10⁴;
- 𝔛_t^g: 11.3 (14.7), all from the second entry: √(𝔭₄𝔵₄/2) 4.5, λ_t = 2([k₁]_t + 1) 4.6, √602 1.4;
- 𝔜_t: 7.3 (10.4), from √𝔱₃ (1.8) and 1 + 7λ_t (5.4). So the top-level k₁ enters a second time;
- e^(φ(t,v\*)/2): 4.5 (11.1);
- 98, [2Ω̂²(1 + c/κ′)^(1/2)]_t, 𝔪(t) and [𝔨₂]_t: 7.1 together;
- μ^(−3/2): 7.5 (9.0).
S_(F,g) at level 4 is 𝔤_(4,g) 24.6, C_P 14.3 (C₁^g 10.8, k₁^(0) 2.7), 𝔨_g 4.6 and μ^(−3/2) 7.5.

**Which factors dominate:**
- at level 6: the r-fold Λ_k powers in 𝔠^⋆ (through 𝔤_(N,g));
- at level 4: the same powers in [𝔠^⋆₄]_t;
- at both: the top-level k₁ (twice at each level), the component Sobolev chain (C₁^g; √𝔭₄𝔵₄ and 𝔱₃ in S_M), and μ^(−3/2).
- 𝔐 is no longer material: √114 is 1.0 decade and √16 is 0.6.

## G0d.3 What remains of lever 3's distance

**The distance**, the proved P-GRD figure minus the G0b-type constants at the same proved power μ^(−3/2), in decades
(computed):
- level 6: 75.3, 79.1, 84.6, 84.9 (seed 1 D_A, seed 2 D_A, seed 1 D\*, seed 2 D\*);
- level 4: 45.5, 47.6, 57.1, 53.8.

**Level 6, seed 1 D_A, item by item** (computed sizes; the items overlap by about 2.5, since the maxima sit at different
points):

| item | decades |
|---|---|
| 𝔤_(6,g) against c_NL = 9·2⁶ | 51.4 |
| of which the r-fold Λ_k powers in λ_k, b_g (removed by the per-factor lever) | 32.9 |
| of which 7^(N/2) (the ℓ² word count P-GRD (3c) names) | 2.5 |
| of which (81 + 5\|R̂\|)/9 at the peak | ≈ 1.3 |
| of which the single-factor Λ₆ growth and the 𝔮_(jj′) couplings | ≈ 15 |
| 𝔨_g (top-level k₁; P-GRD (3a) "needed by this way of bounding") | 8.6 |
| C_P against G0's C_S | 17.8 |
| of which the top-level k₁ inside C₁^g ((k₁ + 1)² under the root) | ≈ 8 |
| of which the component Sobolev chain (𝔳⁶𝔴⁶, 𝔭₃, 𝔨₂, 258; P-GRD (3b)) | ≈ 6 |
| of which k₁^(1) and √114 | 4.0 |

**Level 4, seed 1 D_A.** The 45.5 decades are mostly S_(M,g):
- [𝔠^⋆₄]_t: 23, of which about 10.6 goes with the per-factor lever (computed: S_(M,g) 59.9 → 49.3);
- the top-level k₁, twice (λ_t in 𝔛 and in 𝔜): about 10;
- the component constants √(𝔭₄𝔵₄/2), √𝔱₃ and 𝔪: about 8.5;
- [𝔨₂]_t: 2.

**The remainder after the per-factor lever is still 43 decades at level 6 and 35 at level 4** (seed 1 D_A, computed: 59.5
against 16.8, and 50.3 against 15.4). It is the top-level k₁ (8–10 per occurrence), the component Sobolev chain, the
word count and 𝔮, and the single-factor growth of Λ_N.

## G0d.4 Reach (computed, D\*'s grid restricted to u ≤ u\*; f in decades)

| u\* | −9 | −5 | −3 | −2 | −1.5 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|
| L4 P-GRD, seed 1 / 2 | −55.9 / −58.2 | −60.3 / −61.6 | −63.2 / −63.8 | −66.3 / −66.7 | −69.2 / −68.5 | −75.1 / −72.6 | −83.7 / −77.0 |
| L6 P-GRD, seed 1 / 2 | −86.5 / −89.5 | −91.8 / −94.2 | −95.1 / −97.3 | −98.4 / −100.3 | −101.2 / −102.9 | −105.9 / −106.9 | −114.1 / −110.4 |
| L4 per-factor lever, seed 1 / 2 | −46.9 / −48.3 | −50.6 / −51.3 | −53.0 / −53.2 | −55.8 / −56.2 | −58.4 / −57.7 | −64.0 / −61.8 | −71.8 / −67.5 |
| L6 per-factor lever, seed 1 / 2 | −57.9 / −57.7 | −61.7 / −61.1 | −63.7 / −63.1 | −65.7 / −65.6 | −67.6 / −68.3 | −72.8 / −72.3 | −81.0 / −77.2 |
| L4 G0b-type, μ^(−3/2), seed 1 / 2 | −14.2 / −14.0 | −17.3 / −16.4 | −19.0 / −17.6 | −20.6 / −18.9 | −21.8 / −19.9 | −23.9 / −21.5 | −26.2 / −22.9 |
| L6 G0b-type, μ^(−3/2), seed 1 / 2 | −15.8 / −15.5 | −19.4 / −18.2 | −21.1 / −19.6 | −22.8 / −21.0 | −24.0 / −22.0 | −26.4 / −23.6 | −29.2 / −25.2 |

**Reach:**
- **P-GRD as proved, and the per-factor lever:** no reach in double-double or in quad-double at either level, at either
  seed, for any u\* ≥ −9.
- **G0b-type constants at μ^(−3/2)**, for comparison:
  - double-double: level 4 to u\* ≈ −2.4 (seed 1) and ≈ −1.5 (seed 2); level 6 to u\* ≈ −4.3 and ≈ −2.7;
  - quad-double: all of D\* at both levels and both seeds.
- **The ϱ target is stricter than f throughout:** 20–57 decades below it. η₀ sits about 6 decades above f at level 4
  and 14 at level 6, but it is a C^N sup of the N₀ mismatch, not a weighted residual, so the two do not compare
  directly.

## G0d.5 Pages at the new targets

S-APP's size model, imported unchanged except the commutation weights to l ≤ N at the optimal μ. V2 levers, φ allocation
with the level-N rates, worst-case rule, dense format; computed unless marked.

| target | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| level 3 at G0b's targets (S-APP, record) | 451 | 425 | 1,740 | 1,158 |
| level 6 at G0b's targets, μ = 10⁻³ (N-APP1, record) | 577 | 558 | 1,982 | 1,588 |
| **L4 P-GRD target** (f = 10^−66.3, −66.7, −83.7, −77.0) | **24,152** | **28,033** | **120,878** | **67,315** |
| the same with the ϱ requirement (f_ρ ≈ 10^−87.2, unweighted, order ≤ 3) | 86,148 | | | |
| **L6 P-GRD target** (f = 10^−98.4, −100.3, −114.1, −110.4) | **95,617** | **114,268** | ≈ 3.8 × 10⁵ (extrapolated) | ≈ 2.5 × 10⁵ (extrapolated) |
| L4 per-factor-lever target (f = 10^−55.8) | 13,562 | | | |
| L6 per-factor-lever target (f = 10^−65.7) | 23,194 | | | |
| L4 G0b-type μ^(−3/2) target (f = 10^−20.6, −18.9, −26.2, −22.9) | 674 | 571 | 2,709 | 1,466 |
| L6 G0b-type μ^(−3/2) target (f = 10^−22.8, −21.0, −29.2, −25.2) | 889 | 735 | 3,581 | 1,911 |

- **Extrapolation of the D\* figures at level 6.** They come from the level-4 D\* runs with the calibrated slope
  pages ∝ (−log f)^3.4, which G0c measured, and a factor 1.1 for the level-6 weights. Running the model at 10^−110 and
  beyond needs lattices of more than 10⁸ points.
- **The ϱ requirement** multiplies the pages by 3.6 at seed 1 D_A, level 4. At level 6 it would be larger: f_ρ is
  10^−149 … 10^−171, unweighted to order 5.
- **No P-GRD target can be printed.** Every proved figure needs 2 × 10⁴ to 4 × 10⁵ pages for f alone. Only the
  G0b-type targets fall in S-APP's range.

## G0d.6 Caveats

1. **Everything rests on G0c's approximants, growth model and couplings.**
   - The derivative orders beyond 3 (T) and 5 (rotations) are modelled. G0c measured that halving the continued ratios
     moves the "as written" figures by about 12 decades.
   - Λ^R_k for k ≥ 1 is an estimate (3r_D²X_(k+1) + 2|R̂|X_(k−1)), and so are max|D̂²Z| and C_(∞,0) ≈ C_∞ (G0c).
   - Λ_k follows P-GRD's definition: the cumulative max of X_(k−1), 1.5r_DX_k and 1.5r_D²X_(k+1), with Λ₀ = 0 and no
     floor at 1.
2. **Sampling.** The sup over φ uses three phases. The rays are 21, and the grid sampling is G0c's. [·]_t is the max over
   the grid nodes of the face u = t (κ′ → 0).
3. **Budget split.** The ϱ and η₀ targets split the budgets as in G0c: half of ε to the f-part, 𝔯 split equally between
   the ϱ and η₀ parts, and 𝔰_\* < 𝔰₁^⋆ in quarters.
4. **The per-factor lever is not proved in P-GRD.** It is a computed variant of a deduced inequality, Λ_aΛ_b ≤
   Λ₁Λ_(a+b−1) on the measured sequence.

## G0d.7 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0d/`)

| file | what |
|---|---|
| `cg.py` | 𝔠^g_n, 𝔠^Q_n, 𝔠^(3)_n of eq:tl5-hfg-cn (vectorised), λ_k, and the per-factor variant `Bounds2`; self-check against P-GRD's numbers |
| `levelG.py` | the sharpened evaluation (thm:tl5-hfg, thm:tl5-hf4g with both triples; every factor of "Every factor, as a formula"); rates from G0c's cache or new LPs; the merged level-4 S_M; the G0b-type μ^(−3/2) comparison; level-4 diagnostics (`G0D_DIAG=1`) |
| `levelG_s{1,2}_{4,6}_-2.0_-1.1.json`, `main_*.out` | main results |
| `levelG_s{1,2}_{4,6}_-9.0_…_-1.2.json`, `reach_*.out` | reach sweeps |
| `levelG_s{1,2}_4_-2.00_-1.10.json`, `diag_*.out` | level-4 diagnostics and the merged S_M |
| `summ.py`, `reach.py` | tables |
| `pages_L4.out`, `pages_L6.out`, `pages_other.out` | page-model runs (driver `scratchpad/g0c/pages.py`) |
