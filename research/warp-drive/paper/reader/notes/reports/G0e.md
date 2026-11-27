# G0e: the second sharpening (P-GRD2) at levels 4 and 6, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing. I read nothing under method/, drive/, extracted/ or
recovered/.

**What I evaluated.** proofs/P-GRD2.md, md5 36c2df1c… as briefed, read whole: sec:tl5-hfs, thm:tl5-hfs, thm:tl5-hf4s and
"Every new factor, as a formula".

**The file moved while this ran.** It was confirmed in fe8b4e03 and merged into chapter 87 as sec:tl5-hfs in 53bd18fb,
where it is now Theorems 57.174 and 57.175. P-GRD2.md was then retired. I read the confirm diff (`git show`, read-only).
It touches none of the factors evaluated here. It states three things:
- 𝔰₀^♮ with sup over D^κ, as evaluated;
- the higher-order terms of S_M keep 49𝔰_♭𝔠^(3♮)₄, as evaluated;
- ϱ and η₀ carry μ^(−3/2) in 𝔯_w, 𝔯_M and ε_M, as evaluated.

The figures below therefore apply to the merged text as well.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0e/` (§G0e.7);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0b, G0c, G0d, S-APP, N-APP1 or P-GRD2, cited.

**Evaluated as in G0d.**
- Same provisional approximants and grid, same 𝔅_N and LP rates (G0c's stored rates, plus new LPs where needed), same
  couplings and growth model, κ = κ′ = ϑ = 10⁻², the same Λ_k and Λ^R_k.
- Every factor of "Every new factor, as a formula" is implemented as written:
  - λ^♮, b^♮_g, β₁^♮, β₂^♮ and 𝔠^(2♮), 𝔠^(3♮) by eq:tl5-hfs-cn;
  - 𝔠^♮(μ) with Λ_a, Λ^R_a weighted by μ^(a/2) before the products are formed; the +1 in b^♮_g is not weighted;
  - k₁^(j,μ) with α_𝔄^(j,μ) built per level pair from the couplings;
  - Λ₂^μ, C₁^♮, C_(1,0)^♮, C_P^♮, 𝔎, 𝔎_ϱ, 𝔎₀, 𝔤_(𝒥,s), 𝔤_(ϱ,s), 𝔣₀,₁,₂, 𝔞_(o,i), S_(F,s), 𝔯_(w,s), ε_(w,s);
  - k₃^♮, 𝔰₀^♮ and 𝔰₁^♮ from 𝔠^♮ at μ = 1;
  - 𝔰_(*,s) with P-GRD's μ-free constants;
  - at level 4: λ_t^μ, ϖ₁,₂, 𝔛₁,₂, 𝔛′₂, 𝔜₁, 𝔜′₁, 𝔜″₁, 𝔜₂, 𝔜″₂, 𝔠^M₁,₂, w_t, S_(M,s), 𝔯_(M,s), ε_(M,s).
- **Check** (computed against P-GRD2's own computed values): 𝔠^(2♮)_n at Λ ≡ 1 = 85, 587, 3.90e3, 2.68e4, 2.01e5,
  1.73e6, 1.71e7, and the illustration 𝔠^(2♮)_6(10⁻⁵) = 1.44e5 against 1.47e18. All agree.

**Targets.** G0b's margin of 10 and δ_w ≤ ε:
- level 6: 8(√2δ_w + 2ε_(w,s))S_(F,s) ≤ 0.1;
- level 4: 8(√2δ_w + 2ε_(w,s) + 2ε_(M,s))(S_(F,s) + S_(M,s)) ≤ 0.1;
- both levels: 𝔯 ≤ 1/40 (split between ϱ and η₀), 𝔰_(*,s) < 𝔰₁^♮ (half of it to the A_s part) and η₀ < 𝔰₁^♮/2.

M_w := 8√2(S_(F,s) + S_(M,s)). The free choices are 𝔰_♭ ∈ {1/8, 10⁻², 10⁻⁴, …, 10⁻¹²} and μ ∈ {10⁻³, 3 × 10⁻⁴, …, 10⁻⁶}.
μ = 3 × 10⁻⁷ and 10⁻⁷ were also run, and nowhere improve f or M_w. Each entry takes the choice with the loosest f.

---

## G0e.0 Headline (computed; log₁₀ M_w; targets; optimal choices)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **Level 4, P-GRD2**: M_w | **31.3** | **29.3** | **40.0** | **36.6** |
| f / ϱ / η₀ | 10^−40.9 / 10^−42.1 / 10^−33.4 | 10^−39.7 / 10^−40.9 / 10^−31.0 | 10^−52.2 / 10^−53.1 / 10^−40.8 | 10^−49.1 / 10^−50.7 / 10^−37.0 |
| 𝔰₁^♮; μ; 𝔰_♭ | 3.6 × 10⁻⁸; 3 × 10⁻⁵; 10⁻⁶ | 2.2 × 10⁻⁹; 10⁻⁴; 10⁻⁸ | 2.2 × 10⁻¹⁰; 3 × 10⁻⁶; 10⁻⁸ | 1.0 × 10⁻¹¹; 3 × 10⁻⁵; 10⁻¹⁰ |
| smallest M_w over all choices (𝔰_♭ = 10⁻¹²) | 29.4 (f 10^−45.8) | 28.3 (10^−43.4) | 36.6 (10^−55.1) | 34.1 (10^−50.4) |
| **Level 6, P-GRD2**: M_w | **31.5** | **30.2** | **39.3** | **34.8** |
| f / ϱ / η₀ | 10^−56.6 / 10^−58.5 / 10^−28.6 | 10^−54.7 / 10^−57.0 / 10^−27.3 | 10^−71.2 / 10^−73.0 / 10^−31.6 | 10^−66.4 / 10^−69.6 / 10^−32.9 |
| 𝔰₁^♮; μ; 𝔰_♭ | 1.3 × 10⁻¹¹; 10⁻⁵; 10⁻¹⁰ | 1.3 × 10⁻¹³; 10⁻⁴; 10⁻¹² | 3.1 × 10⁻¹⁵; 3 × 10⁻⁶; 10⁻¹² | 2.3 × 10⁻¹⁷; 10⁻⁵; 10⁻¹² |
| what binds f | 𝔰_\* (both levels, all cases) | 𝔰_\* | 𝔰_\* | 𝔰_\* |
| f from the closing alone (same row) | L4 10^−36.7; L6 10^−37.8 | 10^−34.7; 10^−36.5 | 10^−46.0; 10^−46.1 | 10^−42.5; 10^−41.6 |
| Reach, double-double (f ≥ 10⁻²⁰) | none | none | none | none |
| Reach, quad-double (f ≥ 10⁻³⁵); per seed, over u\* on D\*'s grid | L4 to u\* ≈ −5.4; L6 none | L4 to u\* ≈ −4.7; L6 none | (seed 1: as left) | (seed 2: as left) |
| Pages at the f target (L4; L6) | 4,942; 14,045 | 5,121; 15,080 | 23,716; 67,485 | 15,259; 40,911 |

**What the second sharpening achieves:**
- **Level 6 falls by 61–69 decades** on G0d (92.1, 94.1, 107.3, 103.6). Levels 6 and 4 now differ by less than 2
  decades either way: at the f-optimal rows level 6 is 0.2 and 0.9 above level 4 on D_A, and 0.7 and 1.8 below it on
  D\*.
- **Level 4 falls by 30–38 decades** on G0d (60.9, 61.3, 77.7, 71.1).
- **f improves by 25–32 decades at level 4 and 42–46 at level 6.**
- **Neither level closes at a printable target.** The closing condition no longer sets f anywhere: **the smallness
  𝔰_(\*,s) < 𝔰₁^♮ binds in every case.** It costs 4–7 decades at level 4 and 18–25 at level 6 against the closing
  alone (G0e.3).
- **ϱ is now within 1–3 decades of f**; in G0d it was 20–57 decades below. η₀ sits 7–12 decades above f at level 4
  and 27–40 at level 6.
- **Level 4 now reaches quad-double on the inner part of the domain** (u\* ≲ −5). Nothing reaches double-double.

## G0e.1 Side by side with G0d (log₁₀; G0d rows record, G0e rows computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| L6 M_w: G0d (P-GRD) | 92.1 | 94.1 | 107.3 | 103.6 |
| **L6 M_w: G0e (P-GRD2)** | **31.5** | **30.2** | **39.3** | **34.8** |
| L6 f: G0d → G0e | −98.4 → **−56.6** | −100.3 → **−54.7** | −114.1 → **−71.2** | −110.4 → **−66.4** |
| L6 ϱ: G0d → G0e | −149.1 → −58.5 | −156.2 → −57.0 | −170.6 → −73.0 | −169.1 → −69.6 |
| L6 η₀: G0d → G0e | −84.3 → −28.6 | −86.0 → −27.3 | −96.0 → −31.6 | −93.1 → −32.9 |
| L6 𝔰₁: G0d → G0e | 4e−37 → 1.3e−11 | 1e−39 → 1.3e−13 | 1.5e−43 → 3.1e−15 | 2.5e−42 → 2.3e−17 |
| L6 optimal μ: G0d → G0e | 10⁻⁵ → 10⁻⁵ | 3 × 10⁻⁵ → 10⁻⁴ | 10⁻⁶ → 3 × 10⁻⁶ | 3 × 10⁻⁶ → 10⁻⁵ |
| L6 per-factor lever (G0d's deduced variant) | 59.5 | 59.4 | 74.2 | 70.5 |
| L4 M_w: G0d (graded triple) | 60.9 | 61.3 | 77.7 | 71.1 |
| **L4 M_w: G0e** | **31.3** | **29.3** | **40.0** | **36.6** |
| L4 f: G0d → G0e | −66.3 → **−40.9** | −66.7 → **−39.7** | −83.7 → **−52.2** | −77.0 → **−49.1** |
| L4 ϱ: G0d → G0e | −86.8 → −42.1 | −89.8 → −40.9 | −107.0 → −53.1 | −101.8 → −50.7 |
| L4 η₀: G0d → G0e | −60.7 → −33.4 | −61.1 → −31.0 | −77.6 → −40.8 | −71.0 → −37.0 |
| L4 𝔰₁: G0d → G0e | 6e−15 → 3.6e−8 | 1e−15 → 2.2e−9 | 7e−19 → 2.2e−10 | 7e−18 → 1.0e−11 |
| L4 optimal μ: G0d → G0e | 10⁻⁵ → 3 × 10⁻⁵ | 10⁻⁴ → 10⁻⁴ | 10⁻⁶ → 3 × 10⁻⁶ | 10⁻⁵ → 3 × 10⁻⁵ |
| L4 per-factor lever (G0d) | 50.3 | 50.8 | 65.8 | 61.6 |
| G0b-type constants, μ^(−3/2): L6 / L4 M_w (unchanged) | 16.8 / 15.4 | 15.0 / 13.7 | 22.7 / 20.6 | 18.7 / 17.3 |
| G0b-type, μ^(−3/2): L6 / L4 f | −22.8 / −20.6 | −21.0 / −18.9 | −29.2 / −26.2 | −25.2 / −22.9 |

**Comparison with G0d's deduced levers.** The proved figures now sit 28–36 decades below G0d's per-factor lever at
level 6, and 19–26 below it at level 4. The exact expansion (O1, item 1) removes more than that lever did, because it
also drops the 5^((r+1)/2) of λ_k. Measured at the f-optimal points (computed):
- **unweighted 𝔠^♮₆**: 8 × 10¹¹ to 6 × 10¹⁸, against G0d's 𝔠^Q₆ ≈ 10^51.7 to 10^59.3;
- **𝔠^♮₆(μ)** with the μ^(a/2) weights: 8 × 10³ to 3 × 10⁵.

## G0e.2 What dominates now (computed; log₁₀ of each factor at the point of the supremum)

**Level 6, S_(F,s).** The sup sits at the u\* edge (u = −2.02, v = 7/2 for seed 1 D_A).

| factor | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| 𝔎 = C_P^♮𝔨_B (branch B binds everywhere; 2C_S𝔨_A is 5 decades lower) | 10.3 | 10.4 | 11.0 | 11.1 |
| — C₁^♮ (component Sobolev chain, 𝔨₂, (k₁^μ + 1)) | 7.4 | 7.5 | 8.2 | 8.3 |
| — 2k₁^(1,μ)(2𝔐^(1))^(1/2) = 2 · k₁^(1,μ) · √114 | 2.1 | 2.2 | 2.1 | 2.3 |
| — 𝔨_B = max(𝔷, 2) | 0.75 | 0.68 | 0.67 | 0.59 |
| μ^(−3/2) | 7.5 | 6.0 | 8.3 | 7.5 |
| 𝔤_(𝒥,s) | 6.3 | 6.6 | 6.5 | 6.8 |
| — 7^(N/2) = 7³ (word count) | 2.5 | 2.5 | 2.5 | 2.5 |
| — 𝔠^♮₆(μ) + 1 | 3.7 | 4.1 | 4.0 | 4.3 |
| — the 𝔮 couplings | 0.01 | 0.01 | 0.01 | 0.01 |
| e^(φ/2) at the point | 5.3 | 5.1 | 11.6 | 7.3 |
| 𝔣₂ = 2Ω̂(1 + 1/z̲ + 1/c)^(1/2) | 0.9 | 0.9 | 1.1 | 1.1 |
| the integral (S_F); then 8√2 adds 1.05 to M_w | ≈ 0.2 | | | |

- The top-level k₁ is no longer material. k₁^μ = 7–16 (0.85–1.2 decades), against G0d's 𝔨_g of 8.6–10.0 decades.
  Its unweighted floor (6/5)(√3 + 8/3)K_rec is most of it.
- Λ₂^μ ≤ 4 × 10⁻³ in C₁^♮: negligible.

**Level 4.** S_(M,s) exceeds S_(F,s) by 2.2, 1.8, 4.8 and 4.1 decades at the f-optimal rows. At 𝔰_♭ = 10⁻¹² they are
level (0.0, 0.8, 1.4, 2.2). At the dominant face (u = u\*), the larger of the two products is 𝔛₁𝔜₁:

| factor (S_M, f-optimal row) | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| [𝔠^M₁]_t = 480 + 49𝔰_♭[𝔠^(3♮)₄]_t | 5.0 | 4.4 | 6.0 | 5.4 |
| (the same at 𝔰_♭ = 10⁻¹²) | (2.7) | (2.7) | (2.8) | (3.5) |
| 𝔛₁ = (𝔭₃𝔵₃(1 + 49[ϖ₁]_t))^(1/2) | 4.5 | 5.2 | 5.7 | 6.4 |
| 𝔜₁ = 𝔱₃^(1/2)(1 + 7λ_t^μ), with 1 + 7λ_t^μ ≈ 2.1–2.4 | 3.9 | 3.9 | 5.5 | 5.2 |
| 𝔪(t) | 2.2 | 2.1 | 3.2 | 3.2 |
| [𝔨₂]_t | 2.0 | 2.0 | 1.9 | 1.9 |
| [2Ω̂²(1 + c/κ′)^(1/2)]_t | 0.9 | 0.9 | 1.3 | 1.2 |
| e^(φ(t,v\*)/2) | 5.4 | 4.2 | 9.4 | 7.7 |
| μ^(−3/2) | 6.8 | 6.0 | 8.3 | 6.8 |

- 𝔛₂𝔜₂ is within 0.2–1.4 decades of 𝔛₁𝔜₁: 𝔛₂ ≈ 7.2–8.4 and 𝔜₂ ≈ 0.9–2.2.
- At level 4, S_(F,s) is 𝔎 9.9–10.9, 𝔤_(𝒥,s) 4.8–5.4 (7² = 1.7) and μ^(−3/2).

**Which factors dominate:**
- **M_w at level 6:** the Sobolev chain inside 𝔎 (C₁^♮ and the recovery factor 2k₁^(1,μ)√114), then μ^(−3/2),
  𝔤_(𝒥,s) and e^(φ/2).
- **M_w at level 4:** the same chain in 𝔛₁, 𝔜₁ and 𝔪, the term 49𝔰_♭𝔠^(3♮)₄ in 𝔠^M, and [𝔨₂]_t.
- **f at both levels:** 𝔰_\*, which P-GRD2 does not sharpen (next section).

## G0e.3 What remains to the G0b-type floor, item by item

The floor is G0's constants, c_NL = 9·2^N and G0's C_S, at the proved power μ^(−3/2), with the closing alone. Every item
is a computed size in decades at the f-optimal row. The items are taken at the point of the supremum and sum to within
0.4–1.6 decades of the total, because the suprema sit at slightly different points.

**M_w, level 6.** The distance is 14.8, 15.2, 16.6 and 16.1 decades.

| item | s1 D_A | s2 D_A | s1 D\* | s2 D\* | status in P-GRD2 |
|---|---|---|---|---|---|
| C_S (component Sobolev: 𝔭₂, 𝔳⁴𝔴⁴, 6) against G0's C_S | 3.0 | 3.0 | 3.9 | 3.6 | item 4, not done |
| C₁^♮ against C_S (𝔭₃/𝔭₂, 𝔳²𝔴², 258/6, 𝔨₂, k₁^μ) | 3.9 | 4.0 | 3.9 | 4.1 | item 4 (k₁^μ part: item 3) |
| 2k₁^(1,μ)√114 in C_P^♮ | 2.1 | 2.2 | 2.1 | 2.3 | proved as is |
| 𝔨_B = max(𝔷, 2) | 0.75 | 0.68 | 0.67 | 0.59 | proved as is |
| 7^(N/2) = 7³ in 𝔤_(𝒥,s) | 2.5 | 2.5 | 2.5 | 2.5 | item 5, not done |
| (𝔠^♮₆(μ) + 1) against 9·2⁶ | 1.0 | 1.3 | 1.2 | 1.5 | proved |
| 𝔮 couplings | 0.01 | 0.01 | 0.01 | 0.01 | proved (item 2(ii)) |
| 𝔣₂ against G0b's Ω̂/√c | 0.8 | 0.8 | 0.4 | 0.4 | — |
| 8√2 against 4√2 | 0.3 | 0.3 | 0.3 | 0.3 | — |
| sum (against the total) | 14.3 (14.8) | 14.8 (15.2) | 15.0 (16.6) | 15.3 (16.1) | |

**M_w, level 4.** The distance is 15.8, 15.6, 19.4 and 19.3 decades at the f-optimal rows, and 13.9, 14.6, 16.0 and 16.8
at 𝔰_♭ = 10⁻¹². It is S_M's. For seed 1 D_A (total 15.8):

| item | decades |
|---|---|
| 𝔠^M₁ against c_NL = 144 | 2.8 (0.5 at 𝔰_♭ = 10⁻¹²) |
| 𝔛₁ (component chain √𝔭₃ and the 𝔳⁶ in 𝔵₃: 4.2; the rest, ([R⁻³]_t(1 + 49ϖ₁))^(1/2): 0.3) | 4.5 |
| 𝔜₁ (√𝔱₃: component part 2.1; 1 + 7λ_t^μ, the top-level k₁, 2.1; the rest −0.3) | 3.9 |
| 𝔪(t) | 2.2 |
| [𝔨₂]_t | 2.0 |
| [2Ω̂²(1 + c/κ′)^(1/2)]_t against Ω̂/√c | 0.8 |
| G0's C_S | −0.6 |
| 8√2 against 4√2 | 0.3 |
| sum (against the total) | 16.0 (15.8) |

**The intrinsic Sobolev inequality (P-GRD2 item 4, not done): what it would be worth.** The variant (computed) drops:
- the component factors (𝔭_r, 𝔴^(2r), 𝔳^(2r) and 258 → 6) in C_S, C₁^♮, C_(0,0), C_(1,0)^♮ and the 𝔰_\* constants;
- at level 4: 𝔵_r → [R⁻³]_t, 𝔭_r → 1, 𝔪 → [R^(3/2)]_t, 𝔳 out of 𝔱_r, and [𝔳⁶], [𝔳⁴] → 1.

It is **optimistic**. It omits the norm comparison of the round metric with k on the leaves, the condition number that
item 4 says comes back, and its C_S lands 0.5 decades below G0's C_S.

| worth (decades) | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| L6 M_w | 5.8 | 5.8 | 6.1 | 6.1 |
| L6 f (𝔰_\* binding) / f from the closing alone | 5.4 / 5.8 | 5.4 / 5.8 | 5.6 / 6.1 | 5.8 / 6.1 |
| L4 M_w (f-optimal row; at 𝔰_♭ = 10⁻¹²) | 7.6; 6.3 | 7.4; 6.8 | 9.9; 7.6 | 9.4; 8.2 |
| L4 f / f from the closing alone | 5.5 / 7.6 | 5.7 / 7.4 | 6.0 / 9.9 | 6.2 / 9.4 |

- **Where the level-6 worth comes from.** The intrinsic constant takes 𝔎 from 10.3 to 4.6 (seed 1 D_A). C_S goes 3.6 →
  0.0 and C₁ goes 7.4 → 1.8.
- **What remains of level 6's distance after it:** 9.0, 9.5, 10.4 and 10.0 decades (M_w 25.8, 24.5, 33.1, 28.7):
  - 𝔤_(𝒥,s) 3.5–4.0, of which the word count is 2.5;
  - the recovery factor 2k₁^(1,μ)√114, 2.1–2.3;
  - C₁ against G0's C_S, 1.3–1.7: 𝔨₂ and (k₁^μ + 1);
  - 𝔨_B, 0.6–0.75;
  - 𝔣₂, 0.4–0.8;
  - the factor 2, 0.3.
- **At level 4 it is worth more,** because 𝔛₁, 𝔜₁ and 𝔪 carry the component chain three times over. What remains there
  is 8.2, 8.2, 9.5 and 9.9 decades (M_w 23.6, 21.9, 30.1, 27.2).

**f: the smallness 𝔰_\* now binds, and P-GRD2 leaves it as in P-GRD.** The f distance to the G0b-type floor is:
- level 6: 33.8, 33.8, 41.9, 41.2 decades. Of these, 15.1, 15.5, 16.9 and 16.4 are the closing (the M_w distance
  above, plus conv_s) and **18.8, 18.2, 25.1 and 24.8 are 𝔰_\***;
- level 4: 20.3, 20.9, 26.0, 26.1, of which 𝔰_\* is 4.2, 5.0, 6.3 and 6.6.

The 𝔰_\* cost is log₁₀(1/𝔰₁^♮) + log₁₀(sup C_∞^(N−4)μ^(−N/2)e^(φ/2) / S_tot) − 1.3. Both terms are now large (computed):

| | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| L6: log₁₀(1/𝔰₁^♮) | 10.9 | 12.9 | 14.5 | 16.6 |
| L6: C_∞^(2)μ^(−3)e^(φ/2) over S_tot | 9.2 | 6.6 | 11.9 | 9.5 |
| L4: log₁₀(1/𝔰₁^♮) | 7.4 | 8.7 | 9.7 | 11.0 |
| L4: C_∞^(0)μ^(−2)e^(φ/2) over S_tot | −2.0 | −2.4 | −2.1 | −3.1 |

- **𝔰₁^♮ = 1/(4 sup k₃^♮) in every f-optimal row.** k₃^♮ is 7 × 10⁶ … 2 × 10¹⁰ at level 4 and 2 × 10¹⁰ … 10¹⁶ at level
  6. The reason: k₃^♮ uses the unweighted 𝔠^♮_(≤N−1) (P-GRD2, notes (ii)). 𝔰_♭ is then chosen just above it.
- **C_∞^(N−4)μ^(−N/2)** is P-GRD's μ-free constant (k₁^(m) and C₁^g unweighted) with the full μ^(−N/2).
- **A variant (deduced, not proved)** uses the lemma's own weighted C_(∞,μ)^(N−4) (k₁^(m,μ), C₁^♮) in 𝔰_\*, keeping
  μ^(−N/2). It recovers 9.4, 8.5, 11.2 and 9.8 decades of the level-6 𝔰_\* term: f = 10^−47.2, −46.2, −60.0, −56.6. At
  level 4 it reaches the closing in two cases.
- **If 𝔰_\* did not bind,** f would be the closing's: L6 10^−37.8, −36.5, −46.1, −41.6; L4 10^−36.7, −34.7, −46.0,
  −42.5.

**The briefed items in one line each:**
- **Item 1** (r-fold powers): done. They were G0d's largest item, 33 decades; now the measured 𝔠^♮₆(μ) costs 1.0–1.5
  decades against 9·2⁶.
- **Item 2** (μ weights): done. The level-6 coefficient went from G0d's 𝔤_(6,g) ≈ 10^54–62 to 𝔤_(𝒥,s) ≈ 10^6.3–6.8.
- **Item 3** (top-level k₁): done to within its unweighted floor. It is worth ≈ 0.8–1.2 per occurrence: in C₁^♮, in
  λ_t^μ, and in the recovery factor k₁^(1,μ).
- **Item 4** (intrinsic Sobolev): not done. Worth ≈ 6 decades of M_w at level 6 and 6–10 at level 4 (optimistic, as
  above).
- **Item 5** (word count): not done. 7^(N/2) = 2.5 decades at level 6, 1.7 at level 4.
- **New and not in the list:** 𝔰_\* (𝔰₁^♮ through the unweighted k₃^♮, and P-GRD's C_∞^(N−4)μ^(−N/2)). It is 18–25
  decades of f at level 6 and 4–7 at level 4, and it is now the largest single item in f.

## G0e.4 Reach (computed; D\*'s grid restricted to u ≤ u\*; best f over 𝔰_♭ and μ, in decades)

| u\* | −9 | −7 | −5 | −3 | −2 | −1.5 | −1.3 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|---|---|
| L4 P-GRD2, seed 1 | −31.5 | −33.8 | −35.3 | −38.1 | −40.9 | −43.2 | −45.6 | −47.5 | −52.2 |
| L4 P-GRD2, seed 2 | −30.7 | −32.6 | −34.6 | −37.0 | −39.7 | −41.2 | −43.3 | −44.9 | −49.1 |
| L6 P-GRD2, seed 1 | −43.9 | −47.1 | −49.5 | −52.9 | −56.6 | −59.4 | −62.4 | −64.6 | −71.2 |
| L6 P-GRD2, seed 2 | −43.0 | −45.9 | −48.0 | −51.3 | −54.7 | −56.5 | −59.0 | −61.0 | −66.4 |
| L4 closing alone, seed 1 / 2 | −29.4 / −29.1 | −31.3 / −30.9 | −32.4 / −31.8 | −33.5 / −32.8 | −34.8 / −33.8 | −35.8 / −34.5 | −37.1 / −35.4 | −38.4 / −36.2 | −42.5 / −40.1 |
| L6 closing alone, seed 1 / 2 | −32.3 / −31.6 | −34.1 / −33.1 | −35.2 / −34.0 | −36.5 / −35.1 | −37.8 / −36.2 | −38.9 / −37.1 | −40.4 / −38.0 | −41.8 / −38.9 | −45.4 / −41.2 |
| L4 intrinsic + closing alone, seed 1 / 2 | −21.9 / −21.2 | −23.9 / −23.0 | −25.2 / −24.1 | −26.8 / −25.5 | −28.5 / −26.9 | −29.9 / −28.1 | −31.3 / −29.2 | −32.3 / −30.0 | −35.0 / −31.8 |
| L6 intrinsic + closing alone, seed 1 / 2 | −25.0 / −24.4 | −27.1 / −26.1 | −28.5 / −27.3 | −30.2 / −28.8 | −31.9 / −30.2 | −33.4 / −31.4 | −35.0 / −32.5 | −36.3 / −33.4 | −39.3 / −35.2 |
| L4 G0b-type, seed 1 / 2 | −13.5 / −12.7 | −15.8 / −14.6 | −17.3 / −16.0 | −19.0 / −17.5 | −20.6 / −18.9 | −21.8 / −19.9 | −23.1 / −20.8 | −23.9 / −21.5 | −26.2 / −22.9 |
| L6 G0b-type, seed 1 / 2 | −15.6 / −14.6 | −17.9 / −16.7 | −19.4 / −18.2 | −21.1 / −19.6 | −22.8 / −21.0 | −24.0 / −22.0 | −25.4 / −22.9 | −26.6 / −23.6 | −29.2 / −25.2 |

**Reach:**
- **P-GRD2 as proved:**
  - double-double: nowhere at either level;
  - quad-double: **level 4 to u\* ≈ −5.4 (seed 1) and ≈ −4.7 (seed 2)**. Level 6 does not reach it: f ≤ 10^−43.0
    even at u\* = −9.
  - G0d had no reach at either precision.
- **If 𝔰_\* did not bind** (closing alone): quad-double at level 4 to u\* ≈ −1.9 / −1.4, and at level 6 to ≈ −5.3 /
  −3.2. Still no double-double.
- **Intrinsic Sobolev with the closing alone:**
  - quad-double: level 4 on all of D\* (seed 1 at the threshold, −35.0 at u\* = −1.1); level 6 to u\* ≈ −1.3 / −1.1;
  - double-double: nowhere. The best is 10^−21.2 at u\* = −9.
- **G0b-type, for comparison:** double-double at level 4 to u\* ≈ −2.4 / −1.5, and at level 6 to ≈ −4.3 / −2.7;
  quad-double on all of D\*.

## G0e.5 Pages at the new targets (computed; S-APP's model through `scratchpad/g0c/pages.py`, as in G0d)

| target | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| level 3 at G0b's targets (S-APP, record) | 451 | 425 | 1,740 | 1,158 |
| G0d, L4 P-GRD (record) | 24,152 | 28,033 | 120,878 | 67,315 |
| **L4 P-GRD2** (f = 10^−40.9, −39.7, −52.2, −49.1) | **4,942** | **5,121** | **23,716** | **15,259** |
| the same with the ϱ requirement (f_ρ = ϱ above, unweighted to order 3) | 9,469 | 9,100 | 45,720 | 27,396 |
| L4, f from the closing alone (10^−36.7, −34.7, −46.0, −42.5) | 3,514 | 3,360 | 15,556 | 9,560 |
| L4, intrinsic-Sobolev f (10^−35.4, −34.0, −46.2, −42.8) | 3,143 | 3,155 | 15,781 | 9,778 |
| L4, intrinsic + closing alone (10^−29.1, −27.3, −36.0, −33.1) | 1,740 | 1,624 | 7,033 | 4,367 |
| L4 G0b-type μ^(−3/2) (G0d, record) | 674 | 571 | 2,709 | 1,466 |
| G0d, L6 P-GRD (record) | 95,617 | 114,268 | ≈ 3.8 × 10⁵ | ≈ 2.5 × 10⁵ |
| **L6 P-GRD2** (f = 10^−56.6, −54.7, −71.2, −66.4) | **14,045** | **15,080** | **67,485** | **40,911** |
| the same with the ϱ requirement (unweighted to order 5) | 31,269 | 30,124 | 140,753 | 82,666 |
| L6, f from the closing alone (10^−37.8, −36.5, −46.1, −41.6) | 3,837 | 4,076 | 15,081 | 8,666 |
| L6, intrinsic-Sobolev f (10^−51.2, −49.3, −65.5, −60.6) | 10,092 | 10,711 | 50,338 | 29,958 |
| L6, intrinsic + closing alone (10^−32.0, −30.7, −40.0, −35.5) | 2,308 | 2,377 | 9,418 | 5,254 |
| L6 G0b-type μ^(−3/2) (G0d, record) | 889 | 735 | 3,581 | 1,911 |

- **The proved targets need 4.4–5.5 times fewer pages than G0d's at level 4, and 5.6–7.6 times fewer at level 6.**
  Every level-6 run is now within the model's range; no extrapolation was needed.
- **The ϱ requirement now costs ×1.8–2.2,** against ×3.6 in G0d. ϱ sits 1–3 decades below f.
- **Still nothing is printable at a proved target.** The least is ≈ 4,900 pages (level 4, D_A).
- **The levers in order of pages, level 6, D_A:** 𝔰_\* is worth ×3.7 (14,045 → 3,837), and the intrinsic Sobolev a
  further ×1.7 (→ 2,308). Both together come within ×2.6–3.2 of the G0b-type floor at level 6 and ×2.6–3.0 at level 4.

## G0e.6 Caveats

1. **G0c's approximants, growth model and couplings,** as in G0d.
   - The derivative orders beyond 3 (T) and 5 (rotations) are modelled.
   - Λ^R_k for k ≥ 1, max|D̂²Z| and C_(∞,0) are estimates.
   - New here: 𝔠^♮(μ) is now small enough (≤ 3 × 10⁵ at level 6) that the modelled orders enter mainly through Λ_k in
     the unweighted k₃^♮ and in 𝔰_\*. 𝔰₁^♮ ∝ 1/k₃^♮ is therefore the quantity most exposed to the growth model.
2. **α_𝔄^(j,μ)** is built from G0b's per-letter coupling data split by level pair (the same data as α^(j) in G0d). The
   same-level term carries μ^(1/2), as the formula's |C| + 1 − |J| = 1 gives.
3. **Budget split as in G0d:**
   - half of ε to the f part;
   - 𝔯 split equally between ϱ and η₀ (total ≤ 1/40, margin 10);
   - 𝔰_\* < 𝔰₁^♮ with half to the A_s part;
   - at level 4, ε_(M,s) is charged to the ϱ budget at the η₀ target.
4. **[·]_t** is the max over the grid nodes of the face u = t (κ′ → 0). The sup over φ uses three phases.
5. **Not proved:** the intrinsic-Sobolev variant (optimistic, see G0e.3) and the weighted-𝔰_\* variant. Both are
   labelled where used. Every headline figure is P-GRD2 as written.

## G0e.7 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0e/`)

| file | what |
|---|---|
| `cg2.py` | λ^♮, b^♮_g, β₁^♮, β₂^♮ with the ν^(a/2) weights; 𝔠^(2♮)_n, 𝔠^(3♮)_n of eq:tl5-hfs-cn; checked against P-GRD2's numbers |
| `levelS.py` (= `levelS_head.py` + `levelS_tail.py`) | the evaluation of thm:tl5-hfs / thm:tl5-hf4s with every new factor; the intrinsic-Sobolev variant; the weighted-𝔰_\* variant; the G0b-type μ^(−3/2) floor; pointwise attribution (`pt`) and level-4 face parts (`parts`) |
| `levelS_s{1,2}_46_-2.0.json`, `…_-1.1.json`, `run_*.log` | main grids |
| `levelS_s{1,2}_64_-1.1_-2.0.json`, `small_mu_*.log` | μ = 3 × 10⁻⁷, 10⁻⁷ |
| `levelS_s{1,2}_46_-9.0_…_-1.2.json`, `reach_*.log` | reach sweeps |
| `summS.py`, `bestS.py`, `tablesS.py`, `diagS.py`, `reachS.py` | tables and attributions |
| `pages_main.out`, `pages_other.out`, `pages_both.out` | page-model runs |
