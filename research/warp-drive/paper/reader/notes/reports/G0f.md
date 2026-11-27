# G0f: the third sharpening (P-GRD3) at levels 4 and 6, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing. I read nothing under method/, drive/, extracted/ or
recovered/.

**What I evaluated.** P-GRD3, which moved three times during the run:
- the draft at 46fc10fc (md5 fce4240d);
- the reader's fixed copy at 3748e932 (md5 88c8d48f);
- the confirmed text at b9bfd6ad (md5 650c18c6), merged as sec:tl5-hft at 1b8a7d43.

I read the chapter text and "Comparison and the factors for the evaluation" of the draft whole, and the two later diffs.
None of the later changes alters a factor evaluated here:
- **C_(E,r)².** I use the rigorous bounds 0.8942, 3.6375 and 15.710 throughout. My own series with the tail extrapolated
  gives 0.8942, 3.6375, 15.7098, and the file's values are 0.894166, 3.637471, 15.70976 (computed, `ce.py`). The
  multiplicities (5, 5, 1), (15, 21, 8, 1) and (51, 86, 46, 11, 1) agree.
- **Level 4.** α, β, ρ are chosen once per t in (c), as implemented.
- **Option (b).** C_(1,0)^♮ uses Λ₂^μ, as implemented.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0f/` (§G0f.8);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0e, G0d, G0b or P-GRD3, cited.

**Evaluated as in G0e.**
- Same approximants, grids, rates (G0c's cache, new LPs where needed), couplings and growth model; κ = κ′ = ϑ = 10⁻².
- Same targets: G0b's margin of 10, δ_w ≤ ε, half of ε to f, 𝔯 split between ϱ and η₀ (total ≤ 1/40), and 𝔰_\* < 𝔰₁
  split in quarters.
- Choices: 𝔰_♭ ∈ {1/8, 10⁻², …, 10⁻¹²} and μ ∈ {10⁻³, …, 10⁻⁶}. μ = 3 × 10⁻⁷ and 10⁻⁷ were checked at level 4 and do
  not improve f. Each entry takes the loosest f.

**Variants.** Every combination of Sobolev choice {merged M, intrinsic E} × smallness option {(a), (b)}.
- **(a):** the A-term weighted by C_(∞,μ)^(N−4); ϱ and η₀ with the unweighted constants; 𝔰₁^t = 𝔰₁^♮;
  ε_(w,t) = ε_(w,s).
- **(b):** k₃^♮(μ) and 𝔰₀^μ; μ^(−N/2) on the ϱ- and η₀-terms with C_((∞,ϱ),μ) and C_((∞,0),μ);
  ε_(w,t) = 𝒮[s_N[2R̂ic] + (1/4)μ^(−1/2)𝔤_(𝒥,s)k₂ϱ].
- **E:** C_S^E, C_(S,0)^E, C₁^E, C_(1,0)^E, C_(1,ϱ)^E with 6C_(E,r)², 𝔳₀ and 𝔴₀ (eq:tl5-hft-cs and the formula list). At
  level 4: 𝔵_r, 𝔱_r, 𝔪, [𝔳⁴], [𝔳⁶] with 𝔳₀, 𝔴₀, and 12C_(E,r)² for 𝔭_r in 𝔛.
- **The item-3 hypotheticals** on top of E.
- **Cross-check (computed):** M (a) reproduces G0e's "weighted 𝔰_\*" variant digit for digit (L4 seed 1 D_A f = 10^−36.4;
  L6 10^−47.2).

**How α, β, ρ are chosen** (computed). Only α : β : ρ matters, since 𝔴₀^k sup 𝔳₀^k is scale-free. For each face Σ₁(a, b)
and each constant:
- (α²/ρ², β²/ρ²) is searched on a grid of ±6 in ln about the seed α² = 2Ω̂²/c, β² = 2cΩ̂², ρ = R (median over the
  row), in steps of 0.25, then refined in steps of 0.05;
- the objective is max_x 𝔴₀(p)^k · sup_face(𝔳₀^k g), with k = 4 for C_S and C_(S,0), k = 6 for C₁, C_(1,0) and
  C_(1,ϱ), and g the constant's own face weight;
- no optimum lay on the search edge;
- at level 4 one triple per t (face Σ₁(t, v\*)) minimises [𝔴₀⁶R^(3/2)]_t[𝔳₀⁶R⁻³]_t^(1/2)[𝔳₀⁶R⁻³ max(1 + 18|D̂∂_γ|²,
  2|∂_γ|²)]_t^(1/2), then is scaled so that 𝔴₀ ≥ 1 on the face, which makes max(1, 𝔴₀) = 𝔴₀ optimal;
- 𝔳₀² and 𝔴₀² are the extreme eigenvalues of the file's M: one 2 × 2 block (u, x) and three diagonal entries.

---

## G0f.0 Headline (computed; best proved variant = intrinsic Sobolev E with option (b), in every case)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **Level 4: f** | **10^−31.1** | **10^−30.0** | **10^−39.8** | **10^−36.0** |
| ϱ / η₀ | 10^−37.7 / 10^−26.5 | 10^−36.3 / 10^−26.4 | 10^−46.6 / 10^−34.9 | 10^−42.1 / 10^−30.8 |
| log₁₀ M_w; μ; 𝔰_♭; 𝔰₁^t | 24.9; 10⁻⁵; 10⁻⁶; 5 × 10⁻⁷ | 24.6; 3 × 10⁻⁵; 10⁻⁶; 5 × 10⁻⁷ | 33.9; 10⁻⁶; 10⁻⁶; 5 × 10⁻⁷ | 30.0; 10⁻⁵; 10⁻⁸; 5 × 10⁻⁹ |
| what binds (by how much) | 𝔰_\* < 𝔰₁ (0.7) | closing (𝔰_\* has 0.9 to spare) | closing (1.8 to spare) | 𝔰_\* < 𝔰₁ (0.1) |
| **Level 6: f** | **10^−37.2** | **10^−34.6** | **10^−46.6** | **10^−41.2** |
| ϱ / η₀ | 10^−46.1 / 10^−25.0 | 10^−42.7 / 10^−23.7 | 10^−56.6 / 10^−27.5 | 10^−49.4 / 10^−26.3 |
| log₁₀ M_w; μ; 𝔰_♭; 𝔰₁^t | 27.7; 10⁻⁵; 10⁻⁴; 2.0 × 10⁻⁵ | 25.8; 3 × 10⁻⁵; 10⁻⁴; 1.7 × 10⁻⁵ | 36.0; 3 × 10⁻⁶; 10⁻²; 4.5 × 10⁻⁶ | 30.4; 10⁻⁵; 10⁻⁴; 1.9 × 10⁻⁶ |
| what binds (by how much) | 𝔰_\* < 𝔰₁ (3.3) | 𝔰_\* < 𝔰₁ (2.5) | 𝔰_\* < 𝔰₁ (3.8) | 𝔰_\* < 𝔰₁ (4.0) |
| G0e (P-GRD2) f: L4; L6 (record) | 10^−40.9; 10^−56.6 | 10^−39.7; 10^−54.7 | 10^−52.2; 10^−71.2 | 10^−49.1; 10^−66.4 |
| Reach in quad-double (f ≥ 10⁻³⁵) | L4 to u\* ≈ −1.24; L6 to ≈ −2.84 | L4 to ≈ −1.15; L6 to ≈ −1.85 | (per seed: as left) | (as left) |
| Reach in double-double (f ≥ 10⁻²⁰) | none (best 10^−23.5 at u\* = −9) | none (10^−22.8) | | |
| Pages at f (with the ϱ requirement) | L4 2,161 (6,988); L6 3,651 (16,325) | 2,047 (6,570); 3,145 (13,899) | 9,826 (31,416); 15,637 (68,751) | 5,519 (16,222); 8,402 (32,593) |

**What the third sharpening achieves (computed):**
- **f improves on G0e** by 9.7–13.1 decades at level 4 and 19.4–25.2 at level 6.
- **Level 6 is still 4.6–6.8 decades harder than level 4.**
- **Quad-double now covers level 4 on almost all of D\*.** It reaches u\* ≈ −1.24 and −1.15, against −5.4 and −4.7 in
  G0e, and level 6 to u\* ≈ −2.84 and −1.85, against none.
- **Double-double is still out of reach** at both levels.
- **At level 6 the smallness binds everywhere, and the cause is almost entirely 𝔰₁^t.** The margin equals
  log₁₀(0.05/𝔰₁^t) minus 0.1–1.0 decades. The A-term sup C_(∞,μ)^(2)μ^(−3)e^(φ/2) is now no larger than S_tot.
  𝔰₁^t sits at the cap 𝔰_θ = ϑ/((√2 + ½) max(…)) in three of the four cases: 𝔰_θ = 1.97 × 10⁻⁵ on D_A and
  4.5 × 10⁻⁶ on D\* for seed 1, computed. The fourth (seed 2 D\*) sits at 1/(4k₃^♮(μ)), with k₃^♮(μ) = 1.3 × 10⁵.
- **At level 4 the closing and the smallness are within 0–2 decades of each other.**

## G0f.1 Options (a) and (b), merged and intrinsic (computed; best f over 𝔰_♭ and μ; log₁₀ M_w in brackets)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| L4 merged (a) | −36.4 [31.0] | −35.2 [29.3] | −45.9 [39.8] | −43.3 [36.0] |
| L4 merged (b) | −36.4 [31.0] | −34.9 [29.3] | −45.7 [39.8] | −42.6 [36.0] |
| L4 E (a) | −32.2 [24.9] | −31.2 [23.3] | −41.2 [32.1] | −38.7 [28.1] |
| **L4 E (b)** | **−31.1 [24.9]** | **−30.0 [24.6]** | **−39.8 [33.9]** | **−36.0 [30.0]** |
| L6 merged (a) | −47.2 [31.5] | −46.2 [30.2] | −60.0 [39.3] | −56.6 [34.8] |
| L6 merged (b) | −41.0 [31.6] | −38.4 [30.0] | −50.9 [40.3] | −45.7 [34.8] |
| L6 E (a) | −43.4 [27.6] | −42.5 [26.4] | −55.7 [35.0] | −52.1 [30.4] |
| **L6 E (b)** | **−37.2 [27.7]** | **−34.6 [25.8]** | **−46.6 [36.0]** | **−41.2 [30.4]** |

**(a) against (b).** (b) is better for f in every case:
- by 1.1, 1.2, 1.4 and 2.7 decades at level 4;
- by 6.2, 7.9, 9.1 and 10.9 decades at level 6.

The reason is 𝔰₁:
- under (a) it stays 𝔰₁^♮ = 1/(4k₃^♮), with the unweighted k₃^♮ = 7 × 10⁶ … 10¹⁶;
- under (b) k₃^♮(μ) is 1.4 × 10³ … 1.3 × 10⁵, so 𝔰₁^t rises to 𝔰_♭/2 at level 4 or the 𝔰_θ cap at level 6.

**The price of (b) is ϱ.** μ^(−N/2) on the ϱ-term of 𝔰_\* puts ϱ 6–10 decades below f under (b), against 1–3 under (a).
- At level 4: ϱ = 10^−37.7, −36.3, −46.6, −42.1 under (b), against 10^−33.5, −32.3, −42.1, −39.6 under (a).
- At level 6 the two are mixed: (a) is ahead on seed 1 D_A by 0.8 decades; (b) is ahead elsewhere by 0.9–5.9.

Once the page model must also certify ϱ:
- (a) needs fewer pages at level 4: 5,100, 4,827, 23,663, 13,726 against (b)'s 6,988, 6,570, 31,416, 16,222;
- (b) is better at level 6 in three cases: 16,325, 13,899, 68,751, 32,593 against (a)'s 15,582, 15,651, 71,774, 43,774.

So (b) is the choice for f at both levels, and for the printed approximant at level 6 except seed 1 D_A, where (a) needs
5 % fewer pages. At level 4, if ϱ is certified by the same enclosure, (a) prints 1.2–1.4 times fewer pages.

## G0f.2 The intrinsic Sobolev constants against the merged ones (computed)

**What E is worth:**
- **f:** 5.3, 4.9, 5.9, 6.6 decades at level 4 with option (b) (4.0–4.7 with (a)), and 3.8, 3.8, 4.3, 4.5 at level 6;
- **M_w:** 4–6 decades at level 4 and about 4 at level 6;
- **the constants themselves:**
  - C_S falls by 3.5–3.7 decades (max 10^4.21 → 10^0.58 for seed 1 D_A, 10^4.55 → 10^1.09 for seed 1 D\*);
  - C_(0,0) falls by 4.07;
  - the unweighted C₁^g falls by 3.9–4.7 (L4 seed 1 D_A 10^10.76 → 10^6.81; L6 10^14.73 → 10^10.83).
- **Against G0e's optimistic estimate.** G0e put the worth at ≈ 6 decades at level 6 and 6–10 at level 4. That estimate
  used 6 in place of 258 C_(E,3)² and left out the condition number, so the proved worth is lower.

**Where the gain comes from.**
- **Constants:** 6C_(E,r)² against 6C_(S³)²𝔭_r is a factor 219, 270 and 197 in the squares, i.e. 1.17–1.21 decades in
  each constant.
- **Products:** the rest is the product 𝔴₀^k sup 𝔳₀^k against 𝔴^k sup 𝔳^k. The merged 𝔴⁴ sup 𝔳⁴ is 10^6.04 at its
  max (median 10^4.5–5.1). The intrinsic 𝔴₀⁴ sup 𝔳₀⁴ after the choice of α, β, ρ is:

| max (median) of 𝔴₀⁴ sup 𝔳₀⁴ | seed 1 | seed 2 |
|---|---|---|
| D_A | 10^0.28 (10^0.02) | 10^0.12 (10^0.02) |
| D\* | 10^0.87 (10^0.06) | 10^0.33 (10^0.02) |

**Condition numbers** (λ_max(M)/λ_min(M))^(1/2), computed:

| | seed 1 D_A | seed 2 D_A | seed 1 D\* | seed 2 D\* |
|---|---|---|---|---|
| pointwise, at the point's own seed: max (median) | 1.16 (1.008) | 1.07 (1.002) | 1.59 (1.02) | 1.20 (1.006) |
| over a face Σ₁(a, b), seed at the face tip: max (median) | 1.65 (1.13) | 1.59 (1.12) | 2.17 (1.20) | 1.86 (1.18) |
| over a face, after the choice for C_S: max (median) | 1.63 (1.13) | 1.59 (1.12) | 2.24 (1.19) | 1.92 (1.18) |
| over a face, after the choice for C₁ | 1.63 (1.13) | 1.59 (1.12) | 2.29 (1.19) | 1.83 (1.17) |
| level-4 face Σ₁(t, v\*), one triple per t: max (median) | 1.63 (1.25) | 1.59 (1.24) | 2.05 (1.65) | 1.81 (1.61) |

- **The pointwise condition number** (b̂, P, Q away from zero) is at most 1.6.
- **The face condition number grows with u\***: 1.16 at u\* = −9, 1.65 at −2, 2.2 at −1.1 for seed 1. It is the
  variation of Ω̂, c and R over a face, which one ρ per face cannot follow.
- **The seed choice is already within 0.0–0.2 decades of the optimum.** The optimiser minimises the weighted product,
  not the condition number, so its κ can come out slightly above the seed's.

## G0f.3 Item 3, priced as hypotheticals (computed; on top of E, at each option's optimum)

| hypothetical | effect on f | effect on M_w |
|---|---|---|
| **(i) word count** 7^(j′/2) dropped from 𝔤_(𝒥,s) altogether (upper bound) | **0.0** everywhere | L6 2.5 (E (b): 27.7 → 25.2, 25.8 → 23.3, 36.0 → 33.5, 30.4 → 27.9); L4 0.0–0.6 (S_F 1.6–1.7, but S_M dominates) |
| (i′) the same with √7 moved into each factor's Leibniz sum (model, deduced) | **0.0** everywhere | L6 0.4–1.0; L4 ≤ 0.4 |
| — the same two, f from the closing alone | — | L6 2.4–2.5 (i) / 0.4–1.0 (i′); L4 0.0–0.6 / 0.0–0.4 |
| **(ii) 𝔠^M₁ = 480 → 96** | **0.0** everywhere | 0.0 everywhere |

**The model behind (i′).** Each letter on a background factor, or on the factor at a point, keeps √7, implemented as a
weight 7^(k/2) on the non-free slots of the composition sums of eq:tl5-hfs-cn. The free slots are the None slots and one
of the two β₁ slots of the term quadratic in D̂h. With μ-weighted Λ the dominant terms put the letters on the solution
slots, which is why the gain is about 1 decade at level 6, not the 2.5 of the bound. The exact count needs the
energy-factor assignment per monomial, which is not done.

**Neither is worth more than a decade in f:**
- **(i)** acts only through the closing, and the closing does not bind at level 6. At level 4 S_M sets the closing, and
  the word count is not in S_M. Even with the closing alone the moved version is worth about 1 decade at level 6.
- **(ii)** does nothing because, at the f-optimal 𝔰_♭ (10⁻⁶…10⁻⁸), [𝔠^M₁]_t = 480 + 49𝔰_♭[𝔠^(3♮)₄]_t is
  10^5.0–8.0, i.e. the higher-order term. At 𝔰_♭ = 10⁻¹², where 480 would matter, S_F dominates S_M.

**The S_M lever that does matter is 49𝔰_♭[𝔠^(3♮)₄]_t.** A third hypothetical, (iii) (deduced, not proved, not in the
brief), weights its background letters by μ^(a/2) as 𝔤_(𝒥,s) does. With option (b):
- f improves by 0.9, 1.4, 2.9 and 2.6 decades at level 4: 10^−30.2, −28.6, −36.9, −33.4;
- 𝔰_♭ = 10⁻⁴ becomes optimal, and 𝔰₁^t rises to the 𝔰_θ cap.

## G0f.4 What binds, and the remaining levers ranked (computed; decades of f unless marked)

**Level 6, E (b).** The smallness binds by 3.3, 2.5, 3.8 and 4.0. In order of worth:
1. **𝔰₁^t** (the 𝔰_θ cap from ϑ = κ = 10⁻² in three cases; k₃^♮(μ) in seed 2 D\*): **2.5–4.0**, the whole smallness
   margin.
   - 𝔰_θ ≈ ϑκc/(√2 + ½), so ϑ = κ = 10⁻¹ would buy about 2 decades (deduced).
   - Changing ϑ or κ changes the rates and the domain D^κ, so I have not evaluated it.
   - Beyond the margin, f is set by the closing.
2. **The closing.** It is 10.9, 10.8, 13.3 and 11.7 decades of M_w above the G0b-type floor. Items, at the sup of S_F:

| item | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| C₁^E against C_S^E (258C_(E,3)²/6C_(E,2)² = 175 under the root; 𝔨₂ with 1/κ; (k₁^μ + 1)\|∂_γ\|) | 3.2 | 3.2 | 3.1 | 3.1 |
| 7^(N/2) = 7³ in 𝔤_(𝒥,s) (upper bound; moved model ≈ 1.0) | 2.5 | 2.5 | 2.5 | 2.5 |
| recovery factor 2k₁^(1,μ)√114 in C_P^♮ | 2.1 | 2.1 | 2.1 | 2.3 |
| 𝔠^♮₆(μ) + 1 against 9·2⁶ | 1.0 | 1.0 | 2.1 | 1.5 |
| 𝔣₂ against Ω̂/√c | 0.8 | 0.8 | 0.4 | 0.4 |
| 𝔨_B = max(𝔷, 2) | 0.75 | 0.70 | 0.68 | 0.59 |
| 8√2 against 4√2 | 0.3 | 0.3 | 0.3 | 0.3 |
| C_S^E against G0's C_S | −0.1 | −0.1 | 0.4 | 0.2 |
| sum (against the total) | 10.6 (10.9) | 10.6 (10.8) | 11.6 (13.3) | 11.0 (11.7) |

   - These count in f only once item 1 is relieved.
   - C₁^E also enters C_(∞,μ)^(2), so lowering it would also ease the A-term of 𝔰_\*.

**Level 4, E (b).** Binding: 𝔰_\* by 0.7 (seed 1 D_A) and 0.1 (seed 2 D\*); the closing elsewhere, with 0.9 and 1.8 to
spare. In order of worth:
1. **49𝔰_♭[𝔠^(3♮)₄]_t in 𝔠^M** (hypothetical (iii), deduced): **0.9–2.9**. [𝔠^M₁]_t is 10^5.0, 10^6.4, 10^8.0 and
   10^7.4 at the optimum. It is the largest factor of S_M. S_M exceeds S_F by 1.4, 3.2 and 2.6 in three cases; in seed 1 D_A S_F leads by 0.4, but
   (iii) still lets 𝔰_♭ rise.
2. **The rest of S_M** (seed 1 D_A, seed 1 D\* in brackets):
   - 𝔜₁: 1.7 (3.1), of which 1 + 7λ_t^μ, the top-level k₁, is 2.1;
   - 𝔛₁: 0.8 (1.8);
   - [𝔨₂]_t: 2.0 (1.9);
   - 𝔪(t): 1.4 (1.2);
   - [2Ω̂²(1 + c/κ′)^(1/2)]_t: 0.9 (1.3).
3. **𝔰₁^t** (𝔰_♭/2 at the optimum; the 𝔰_θ cap once (iii) holds): 0.0–0.7.
4. **S_F's items**, as at level 6 but with 7² = 1.7. They count once S_M is brought down to S_F.

The M_w distance to the G0b-type floor is 9.5, 10.9, 13.3 and 12.7 decades at the f-optimal rows.

**Not worth more than a decade in f:** item 3 (i) and (ii), as written (G0f.3).

## G0f.5 Reach (computed; D\*'s grid restricted to u ≤ u\*; best f over 𝔰_♭ and μ)

| u\* | −9 | −7 | −5 | −3 | −2 | −1.5 | −1.3 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|---|---|
| L4 E (b), seed 1 | −23.5 | −25.5 | −27.0 | −29.0 | −31.1 | −32.5 | −34.2 | −35.6 | −39.8 |
| L4 E (b), seed 2 | −22.8 | −24.6 | −25.7 | −27.4 | −30.0 | −31.3 | −33.0 | −34.1 | −36.0 |
| L6 E (b), seed 1 | −26.8 | −29.7 | −31.9 | −34.6 | −37.2 | −39.3 | −41.2 | −42.5 | −46.6 |
| L6 E (b), seed 2 | −26.1 | −27.9 | −29.6 | −32.1 | −34.6 | −36.0 | −37.5 | −38.6 | −41.2 |
| L4 E (a), seed 1 / 2 | −23.5 / −22.8 | −25.5 / −24.6 | −27.0 / −25.9 | −29.5 / −28.5 | −32.2 / −31.2 | −34.1 / −32.6 | −36.2 / −34.3 | −37.6 / −35.5 | −41.2 / −38.7 |
| L6 E (a), seed 1 / 2 | −30.7 / −30.3 | −33.9 / −33.2 | −36.4 / −35.4 | −39.8 / −38.8 | −43.4 / −42.5 | −46.1 / −44.0 | −48.6 / −46.2 | −50.4 / −47.8 | −55.7 / −52.1 |
| L6 merged (b), seed 1 / 2 | −32.3 / −31.7 | −34.9 / −33.1 | −36.6 / −34.4 | −38.8 / −36.3 | −41.0 / −38.4 | −42.9 / −39.6 | −45.0 / −41.2 | −46.5 / −42.5 | −50.9 / −45.7 |
| L4 / L6 E (b), closing alone, seed 1 | −23.5 / −26.8 | −25.5 / −28.9 | −27.0 / −30.3 | −28.6 / −32.0 | −30.2 / −33.8 | −31.5 / −35.2 | −32.9 / −36.7 | −33.9 / −37.9 | −36.6 / −41.1 |
| L4 / L6 G0b-type, seed 1 | −13.5 / −15.6 | −15.8 / −17.9 | −17.3 / −19.4 | −19.0 / −21.1 | −20.6 / −22.8 | −21.8 / −24.0 | −23.1 / −25.4 | −23.9 / −26.6 | −26.2 / −29.2 |

**Quad-double reach** (f ≥ 10⁻³⁵):
- E (b): level 4 to u\* ≈ −1.24 (seed 1) and −1.15 (seed 2); level 6 to ≈ −2.84 and −1.85;
- E (a): level 4 to ≈ −1.41 and −1.24; level 6 to ≈ −6.1 and −5.4;
- merged (b) at level 6: to ≈ −6.8 and −4.4;
- with the closing alone (if 𝔰₁^t were not capped): level 4 to −1.16 and all of D\*; level 6 to −1.57 and −1.19.

**Double-double:** none for any proved variant. The best is 10^−22.8 (level 4, seed 2, u\* = −9). The G0b-type constants
reach it to u\* ≈ −2.4 / −1.5 (level 4) and −4.3 / −2.7 (level 6).

## G0f.6 Pages (computed; S-APP's model via `scratchpad/g0c/pages.py`, as in G0d and G0e)

| target | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| G0e L4 P-GRD2 (record) | 4,942 | 5,121 | 23,716 | 15,259 |
| **L4 E (b)** (f above) | **2,161** | **2,047** | **9,826** | **5,519** |
| with the ϱ requirement | 6,988 | 6,570 | 31,416 | 16,222 |
| L4 E (a) (f = 10^−32.2, −31.2, −41.2, −38.7) | 2,397 | 2,424 | 10,843 | 6,910 |
| with the ϱ requirement | 5,100 | 4,827 | 23,663 | 13,726 |
| G0e L6 P-GRD2 (record) | 14,045 | 15,080 | 67,485 | 40,911 |
| **L6 E (b)** | **3,651** | **3,145** | **15,637** | **8,402** |
| with the ϱ requirement | 16,325 | 13,899 | 68,751 | 32,593 |
| L6 E (a) (f = 10^−43.4, −42.5, −55.7, −52.1) | 5,922 | 6,618 | 28,683 | 18,048 |
| with the ϱ requirement | 15,582 | 15,651 | 71,774 | 43,774 |
| G0b-type μ^(−3/2) floor, L4 / L6 (record) | 674 / 889 | 571 / 735 | 2,709 / 3,581 | 1,466 / 1,911 |

- **f alone:** the best proved targets need 2.3–2.8 times fewer pages than G0e at level 4, and 3.8–4.9 times fewer at
  level 6. That leaves them 3.2–3.8 (level 4) and 4.1–4.4 (level 6) times above the G0b-type floor.
- **With ϱ also certified**, level 4 under (a) is the cheapest: 4,827–23,663 pages.

## G0f.7 Caveats

1. **G0c's approximants, growth model and couplings,** as in G0d and G0e. Most exposed are k₃^♮(μ) (option (b), and
   𝔰₁^t in seed 2 D\*) and the cap 𝔰_θ, which depends on min c over the domain.
2. **α, β, ρ.** Every choice is admissible by lem:tl5-hft-face, so a grid optimum is a valid bound, only possibly not the
   least.
   - C₁'s face choice is optimised for the unweighted weight and reused for the weighted C₁^♮ (admissible).
   - 𝔴₀ and 𝔳₀ are sampled at the grid nodes (15 Gauss points in x), and the sup over a face is the max over its nodes.
3. **The hypotheticals (i), (i′), (ii) and (iii) are not proved.** (i′) is my slot model of the writer's description;
   (iii) is outside the brief. Every headline figure is P-GRD3 as written, under the best of its proved options.
4. **ϑ and κ** stay at 10⁻². The level-6 smallness margin is set by them through 𝔰_θ, but changing them needs new rates
   and a new D^κ.

## G0f.8 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0f/`)

| file | what |
|---|---|
| `ce.py` | e_j(r), m_(j₁j₂)(r) and the series C_(E,r)² with tail |
| `levelT.py` (= `levelT_head.py` + `levelT_mid.py` + `levelT_tail.py`) | P-GRD3: options (a), (b) × merged / E Sobolev constants; the face optimisation of α, β, ρ (per face; per t at level 4); condition numbers; hypotheticals nw (i), pt (i′), c96 (ii), c3w (iii); pointwise attribution |
| `levelT_s{1,2}_46_-2.0.json`, `…_-1.1.json`, `run_*.log` | main grids |
| `levelT_s{1,2}_4_-2.0.json`, `…_-1.1.json`, `l4hyp_*.log` | level-4 hypothetical (iii) |
| `levelT_s1_4_-1.1_-2.0.json` | μ = 3 × 10⁻⁷, 10⁻⁷ check |
| `levelT_s{1,2}_46_-9.0_…_-1.2.json`, `reach_*.log` | reach sweeps (proved variants) |
| `sumT.py`, `diagT.py`, `reachT.py` | tables and attributions |
| `pages_main.out`, `pages_a.out` (`pages_cmds*.sh`) | page-model runs |
