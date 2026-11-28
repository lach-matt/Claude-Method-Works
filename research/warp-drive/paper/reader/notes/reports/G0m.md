# G0m: the tenth sharpening (P-GRD10, the leaf constant, the weights of the words and the seven fields) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0m/` and ran
under `nice -n 19`, at most two at a time. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD10 (sec:tl5-hfp).
- **Source:** implemented from the draft at ee0925ad (P-GRD10.md md5 871190e2).
- **Confirmed text:** at 3d5ec668 (md5 e977107b). It changes only the Comparison's weighted leaf ratios (the sums to j₁
  ≤ 40000). My sums already run that far and reproduce the corrected values: q₃ (q₂) = 0.1216 (0.1097) at μ = 10⁻⁴,
  0.0684 (0.0617) at 10⁻⁵ and 0.0506 (0.0456) at 3 × 10⁻⁶. The numbers here hold for the confirmed text.

**Replacements implemented** (def:tl5-hfp-constants, lem:tl5-hfp-leaf, -abs, -words, -c1, -rec, -low, thm:tl5-hfp):
- **The leaf constant.** C_(E,r)^♯² replaces 6C_(E,r)² in every face-Sobolev constant: C_S, C_(0,0), C₁, C_(1,ϱ), C_(1,0),
  and 𝔭₃, 𝔭₄ of the products. I computed C_(E,r)^♯² = 0.9551 / 3.8832 / 16.727 for r = 2 / 3 / 4, ratios of the constants
  0.4219 / 0.4218 / 0.4213. These are the writer's table exactly.
- **The weights.** 𝔶 = (μ^(−2s), μ^(−s)), with s ∈ {0, ¼, ½, ⅝, ¾, ⅞, 1}, is optimised row by row with the other parameters.
  - **Parts with ℰ_g** (C_S^p, C₁(𝔚), so C_P^v, S_F and the A-term of 𝔰_\*): factor q = max(q₂, q₃). Using one common
    factor overstates the C_S entries by at most 0.05, and they do not lead.
  - **Parts with ϱ and η₀:** factor q₃𝔗 on C_(1,ϱ) and max(q₂, q₃)𝔗 on C_(1,0) and C_(0,0). 𝔗 = ((ν²𝔶₀ + 6ν𝔶₁ + 36)/43)^½,
    with ν = μ^θ at level 4 (lem:tl5-hfq-theta) and ν = μ at level 6 (lem:tl5-hft-small (b), so 𝔗 = 1 at s = 1).
  - **C_(P,ϱ)^v** = (1 − 𝔵^z)⁻¹ max(t C_(1,ϱ), t 𝔨_rec^(ϱ,·) + k₂^z) is not linear in t, so its face integral is formed on 57
    levels of t and rounded up.
- **The products** (S_M, 𝔯_M, ε_M) take C^♯ only, as the text has them.
- **k₁ with 𝔷′.**
  - 𝔷₁′ = 3(|∇T|² + 6|∇E|²)^½ from G0b's measured maxima (1.41 and 2.19 at seed 1; 0.93 and 1.78 at seed 2).
  - 𝔷₂′ = 2√7 max|D̂²Z|, since no per-field bound of D̂²Z is held.
  - 𝔷′ = (𝔷₁′² + 𝔷₂′²)^½ comes to 68 / 62 / 153 / 188 against the √7 form's 83 / 74 / 170 / 202.
- **C₁(𝔚) = min(C₁^U, C₁^D + C₁^J), point by point**, built from 𝔩_D, 𝔩_J, 𝔨₂′ = max(1/c, 1/κ′)/(2Ω̂²) and
  (μ^½ + ϖ′^½)².
  - 𝔞_𝔄(𝔚) is taken at its proved bound (43n/2)^½ α_𝔄.
  - C₁^D and C₁^J share one face-weight choice per face; C₁^U takes its own.
  - C₁^p = C₁({B}), and C₁^Γ = C₁(Γ) with n = 7.
- **𝔨_rec^p** = 𝔨_♯K_rec(C₁^Γ + 𝔷₁′μ^½C₁^p + 𝔷₂′μC_S^p) + (1 − 𝔰₁^v)⁻¹μ𝔯_♯C_S^p. 𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p) carry
  √7 + 𝔷₁′μ^½.
- **Level 6.** 𝔐_p^(m) replaces (2𝔐^(m))^½ max(C_S, C₁) in the ℰ_g parts of C_(∞,μ)^(1) (= C_P) and C_(∞,μ)^(2) (in 𝔰_\*).
  It is formed with C₁(𝔚_b) for n = 1, 7, 49, 343. The ϱ and η₀ parts keep (2𝔐^(m))^½. Only option (b) is evaluated; G0l
  found it optimal in all four cases.
- **Unchanged, as the Comparison says:** 𝔰₀, 𝔰₁^v and the cap; 𝔨_♯, K_rec, 𝔯_♯, k₂^z, k₃^z, 𝔵^z, ε^z; the rates. At level 4
  the A-term of 𝔰_\* is carried by C_P^v, as since G0g (lem:tl5-hfv-rec bounds 𝔰_P); 𝔐_p^(0) is not used there.

**Method: as in G0l.** Every parameter maximises min(f, ϱ): θ, ϑ₁, ϑ₂, 𝔯, μ, 𝔰_♭, the ε share and now s. The grid is
narrowed around G0l's optima and widened where P-GRD10 moves them:

| parameter | values |
|---|---|
| θ | ½, ⅝, 11/16, ¾, 13/16, ⅞, 1 |
| ϑ₂ | 3 × 10⁻⁴ … 0.03 (ϑ₁ cap-matched, floor 10⁻⁵) |
| 𝔯 | 0.001, 0.003 |
| μ | 3 × 10⁻⁷ … 10⁻⁴ |
| 𝔰_♭ | 10⁻², 10⁻⁴, 10⁻⁶ (level 6: 10⁻⁴, 10⁻⁶, 10⁻⁸) |
| ε shares | 15 values |

**Checks** (computed):
1. **The G0l code path** (`G0M_P=0`) reproduces G0l: 10^−26.77 at seed 1 D_A, μ = 10⁻⁵, on G0l's main grid.
2. **The new code path** with every P-GRD10 change switched off also reproduces 10^−26.77. Switched off means:
   - 6C² in place of C^♯²;
   - 𝔶 = 1 and 𝔗 = 1;
   - no family and no split;
   - the √7 form of 𝔷;
   - (1 + ϖ′^½)² in the first bracket.
3. **The leaf sums** reproduce the writer's table at 𝔶 = 1 and the confirmed weighted ratios. They are summed to 2j₁ <
   80000 with the tail extrapolated; they are stable to four digits from 2j₁ = 8000 at μ ≥ 3 × 10⁻⁶ and from 2j₁ = 40000
   at 3 × 10⁻⁷.
4. **A baseline: G0l's formulas on G0m's grid** (all eight cases). It reproduces G0l's refined values exactly in seven
   of the eight cases. At seed 1, D_A, level 4 it gives −26.77 against −26.70: G0m's grid lacks G0l's refined point
   ϑ₂ = 0.005. P-GRD10's part below is measured against this baseline, on the same grid.

**A correction to G0l** (deduced from its own records).
- **What was wrong.** G0l's tables printed as "log₁₀ S_F" the record's entry, which carries + log₁₀(8√2) = 1.05. The
  closing condition uses S_F itself.
- **The true figures.** At G0l's optima S_M was 1.39 / 0.94 / 1.00 / 1.02 decades below S_F, not 2.0–2.4 as G0l §G0l.1
  and §G0l.2 say. P-GRD10's Comparison took the 2.0–2.4 from G0l.
- **What it does not change:** no max-min value, binding constraint or lever of G0l. S_F + S_M was computed correctly;
  only the printed column was mislabelled. ruleP.py prints S_F itself.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0m/` (§G0m.6);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0l or P-GRD10, cited.

---

## G0m.0 Level 4 (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD10** | **10^−25.12** | **10^−23.80** | **10^−31.99** | **10^−28.80** |
| G0l (refined grid) | −26.70 | −25.12 | −33.70 | −30.39 |
| **gain over G0l** | **+1.58** | **+1.32** | **+1.71** | **+1.59** |
| of which P-GRD10 (against the baseline, same grid) | **+1.65** | **+1.31** | **+1.71** | **+1.59** |
| of which the grid (baseline − G0l) | −0.07 | 0.00 | 0.00 | 0.00 |
| G0l's formulas on this grid (the baseline) | −26.77 | −25.12 | −33.70 | −30.39 |
| f / ϱ | −25.12 / −24.98 | −23.80 / −23.65 | −31.99 / −31.76 | −28.80 / −28.59 |
| η₀ | −22.8 | −21.5 | −28.2 | −25.0 |
| **𝔶 at the optimum** | **(μ⁻², μ⁻¹), s = 1** | **(μ⁻², μ⁻¹)** | **(μ⁻², μ⁻¹)** | **(μ⁻², μ⁻¹)** |
| log₁₀ q₃, log₁₀ q₃𝔗 | −1.17, −0.65 | −1.05, −0.39 | −1.42, −0.69 | −1.17, −0.88 |
| 𝔵^z | 0.008 | 0.017 | 0.016 | 0.054 |
| 𝔰₁^v (what sets it) | 5.9 × 10⁻⁶ (the cap) | 2.0 × 10⁻⁶ (the cap) | 4.5 × 10⁻⁶ (the cap) | 1.4 × 10⁻⁶ (the cap) |
| θ | ¾ | 11/16 | ¾ | 13/16 |
| ϑ₁ / ϑ₂ | 0.00057 / 0.003 | 0.00019 / 0.001 | 0.00044 / 0.01 | 0.00013 / 0.003 |
| 𝔯; μ; 𝔰_♭ | 0.001; 10⁻⁵; 10⁻⁴ | 0.001; 3 × 10⁻⁵; 10⁻⁴ | 0.001; 10⁻⁶; 10⁻⁴ | 0.001; 10⁻⁵; 10⁻⁴ |
| share of ε given to f | 0.9 | 0.99 | 0.95 | 0.95 |
| log₁₀ S_F / log₁₀ S_M | 19.00 / **19.22** | 17.71 / **17.96** | 24.87 / **25.72** | 22.03 / **22.51** |
| what binds | **f: the closing, with S_M above S_F** (𝔰_\* 0.31 spare) | f: closing (0.19 spare) | f: closing (0.19 spare) | f: closing (0.01 spare) |
| rule cost against G0l, (decades ratio)^4.5 | 0.76 | 0.78 | 0.79 | 0.79 |

**P-GRD10 itself gives 1.31–1.71 decades.** The baseline is G0l's formulas on the same grid. That is about the same step as
P-GRD9 (1.53–1.59), and short of the writer's 1.75–2.0, because S_M now binds (§G0m.2).

**The optimum takes the largest admissible weight in all four cases**, 𝔶 = (μ⁻², μ⁻¹). There q₃𝔗 < 1, so the parts with ϱ
and η₀ fall as well, by 0.4–0.9 decades. The weight is not limited by 𝔗, as it can be under lem:tl5-hfs-linfty; it is
limited by its admissible range. The last step, from s = ⅞ to 1, is still worth +0.07.

**Grid edges.**
- 𝔯 takes its smallest value, 0.001. That is worth ≤ 0.01, since the 𝔯 budget of ϱ is 1.2–2.1 decades away.
- s sits at the bound of the theorem, not of the grid.
- Every other parameter is interior.

## G0m.1 What P-GRD10 does to the constants and to min(f, ϱ) (computed)

**The constants at each case's optimal μ.** These are compared at 𝔶 = 1 and 𝔵^z = 0.05, against G0l's C₁^z, 𝔨_rec^z and
C_P^v at the same point.

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | writer (deduced) |
|---|---|---|---|---|---|
| C₁^p / C₁^z | −0.41 | −0.40 | −0.65 | −0.43 | −0.375 − 0.2 (split) |
| C₁^Γ / (√7 C₁^p): the family | −0.21 | −0.22 | −0.21 | −0.23 | −0.27, −0.30, −0.15, −0.13 |
| C_P^v at 𝔶 = 1 (𝔨_rec leads at every point) | −0.62 | −0.63 | −0.85 | −0.71 | |
| × q at the optimal 𝔶 | −1.17 | −1.05 | −1.42 | −1.17 | −1.17, −0.92, −1.31, −1.17 |
| **C_P^v in all** | **−1.79** | **−1.68** | **−2.27** | **−1.88** | **≈ −2.0, −1.75, −2.0, −1.8** |
| S_F (G0l's optimum → G0m's) | −2.01 | −1.67 | −2.54 | −1.93 | |
| S_M (C^♯ only) | −0.40 | −0.48 | −0.69 | −0.43 | ≈ −0.375 |
| **min(f, ϱ): P-GRD10's part** | **+1.65** | **+1.31** | **+1.71** | **+1.59** | up to 1.75–2.0 |

**The writer's deductions hold for C_P^v,** at 1.7–2.3 decades against 1.75–2.0, with one exception: **the split is worth
nothing at the supremum.**
- C₁^D + C₁^J ≥ C₁^U where C₁ is largest. Their sups differ by ≤ 0.01, and the run without the split gives the same max-min
  to 0.003.
- **The cause is the size of 𝔨₂′ against 𝔨₂.** The writer assumed 𝔨₂′ = 𝔨₂/4. Measured, (𝔨₂′/𝔨₂)^½ has its median at
  10^−0.15 (seed 1, D_A) and 10^−0.03 (seed 2, D\*), so 1/z̲ is about half of 𝔨₂ in D_A and a sixth in D\*. On top of that,
  𝔩_J is not small next to 𝔩_D: it carries the μ^½ terms and the nonlinear part.
- Where the split does lower C₁ pointwise (the median by 0.07–0.10 in D_A), it is not at the supremum that C_P^v and S_F
  take.

**The attribution at level 4,** each part computed as the main run against the run without it:

| part | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| the weights 𝔶 (against 𝔶 = 1) | **+0.85** | **+0.65** | **+1.07** | **+1.03** |
| at 𝔶 = 1: C^♯, the family, 𝔷′, 𝔗 ≤ 1, (μ^½ + ϖ′^½)² | +0.79 | +0.66 | +0.64 | +0.56 |
| of which the family Γ (at the optimum) | +0.16 | +0.13 | +0.10 | +0.16 |
| of which the split | 0.00 | 0.00 | 0.00 | 0.00 |
| **P-GRD10 in all** | **+1.65** | **+1.31** | **+1.71** | **+1.59** |

**About 0.3–0.6 decades of the C_P^v fall do not reach min(f, ϱ).** S_F falls 1.7–2.5 decades and S_M only 0.4–0.7, so S_M
overtakes S_F, and S_F + S_M falls only about as far as S_M allows.

## G0m.2 What binds (computed)

The writer named three caps on the gain.

**1. S_M binds next. It caps P-GRD10's gain.**
- At every optimum the closing binds f. In the closing's S_F + S_M, **S_M is now the larger, by 0.22 / 0.25 / 0.85 / 0.48
  decades.**
- In G0l S_M was 0.94–1.39 below S_F, by the corrected figure above. S_F fell 1.7–2.5 decades and S_M 0.4–0.7.
- The weights are taken to their admissible limit anyway, since each step still lowers S_F + S_M.

**2. The 𝔰_\* slack is no longer binding.**
- It has 0.01–0.31 decades spare at the optimum. In G0l it was co-binding, within 0.02–0.13.
- The A-term of 𝔰_\* takes C_P^v's full fall, so 𝔰_\* moved past the closing.
- It is the next limit after S_M: with S_M also weighted (§G0m.3), 𝔰_\* binds again or comes within 0.06.

**3. ϱ is not binding.**
- ϱ sits 0.14–0.23 decades above f.
- **ε share:** the ϱ coefficient × 0.1 is worth only +0.02–0.05.
- **The 𝔯 budget:** 1.2–2.1 decades away under the reading used here (𝔗 of lem:tl5-hfq-theta on every part with ϱ at
  level 4).
- **Under the other reading** (lem:tl5-hfs-linfty's 𝔗, which grows with 𝔶, on the bootstrap's C_(P,ϱ)^v and C_(P,0)^v):
  - t = q₃𝔗 rises to 10^2.7–3.8, and in D_A the 𝔯 budget comes within 0.01 of f;
  - the max-min does not change in any case (computed);
  - so the reading does not matter here, although ϱ then has no room.

**Also not near binding:**
- C_P^v is still led by 𝔨_rec^p at every point. It stands 1.6–1.9 decades above 2C_S at 𝔶 = 1; C_S takes q₂ < q₃, so a
  little more after the weights.
- C₁'s non-k₁ part is unchanged in size (G0l: ≤ 0.02).

## G0m.3 The levers re-ranked at level 4

Each lever is priced against the P-GRD10 optimum (computed where marked; hypothetical, not proved).

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **S_M with the weighted constants as well** (its ℰ_g part × q, the products' Sobolev constants at 𝔶 = (μ⁻², μ⁻¹)) | **+0.31** | **+0.26** | **+0.34** | **+0.14** | computed; 𝔰_\* then binds again or within 0.06 |
| word count 7² in S_F | +0.22 | +0.19 | +0.06 | +0.13 | computed; capped by S_M |
| 𝔠^♮₄(μ) → 9·2⁴ | +0.19 | +0.17 | +0.05 | +0.06 | computed; capped by S_M |
| *measured rate:* C₁ ÷ 2 (−0.30) | +0.15 | +0.11 | +0.09 | +0.13 | computed; 0.3–0.5 per decade, against 0.9–1.0 in G0l |
| 1/z̲ out of 𝔨₂ (in C₁), the rank-3 constant, k₁^D | ≤ +0.1 each | ≤ +0.1 | ≤ +0.1 | ≤ +0.1 | at the measured rate; 1/z̲ is worth least in D\*, where it is a sixth of 𝔨₂ |
| a further ϱ lever (ε's coefficient × 0.1) | +0.04 | +0.04 | +0.02 | +0.05 | computed |
| the nonlinear absorption over the words | ≤ +0.05 | ≤ +0.05 | ≤ +0.05 | ≤ +0.05 | deduced: G0l's +0.02–0.13 at the new rate |
| the split C₁^D + C₁^J, as proved | 0.00 | 0.00 | 0.00 | 0.00 | computed (it is in the main run) |

**Ranking at level 4:**
1. **S_M: about 0.15–0.35, then 𝔰_\* binds.** This is the lever P-GRD10 leaves. The products' face constants (lem:tl5-hf4-face
   (b)) take C^♯ but not the weights. The price assumes weights in them on the ℰ_g part only, with the factor of S_F.
   Lowering S_M's own word counts (√602, 7, 𝔠^Mq) would act the same way, up to the same cap.
2. **The word count and 𝔠^♮₄: ≤ 0.22,** capped by S_M.
3. **Every C₁ or C_P lever transfers at only 0.3–0.5 per decade now** (C₁ ÷ 2 gives +0.09–0.15), because S_M holds the
   closing. G0l's 1:1 rate returns only once S_M is lowered.
4. **ϱ levers and the nonlinear absorption: ≤ 0.05.**

## G0m.4 Level 6, briefly (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD10** | **−35.84** | **−32.49** | **−44.79** | **−38.69** |
| G0l (refined grid) | −38.40 | −34.61 | −47.47 | −41.03 |
| **gain over G0l** | **+2.56** | **+2.12** | **+2.68** | **+2.34** |
| of which P-GRD10 (against the baseline, same grid) | **+2.56** | **+2.12** | **+2.68** | **+2.34** |
| of which the grid (baseline − G0l) | 0.00 | 0.00 | 0.00 | 0.00 |
| G0l's formulas on this grid (the baseline) | −38.40 | −34.61 | −47.47 | −41.03 |
| f / ϱ | −35.48 / −35.84 | −32.01 / −32.49 | −44.28 / −44.79 | −38.57 / −38.69 |
| 𝔶; log₁₀ q₃ (𝔗 = 1) | (μ⁻², μ⁻¹); −1.17 | (μ⁻², μ⁻¹); −0.92 | (μ⁻², μ⁻¹); −1.30 | (μ⁻², μ⁻¹); −1.17 |
| 𝔵^z | 0.002 | 0.010 | 0.001 | 0.0004 |
| option; 𝔰_♭; 𝔰₁^v | (b); 10⁻⁶; 5 × 10⁻⁷ | (b); 10⁻⁶; 5 × 10⁻⁷ | (b); 10⁻⁶; 1.4 × 10⁻⁷ (the cap) | (b); 10⁻⁸; 5 × 10⁻⁹ |
| ϑ₂; μ | 3 × 10⁻⁴; 10⁻⁵ | 3 × 10⁻⁴; 10⁻⁴ | 3 × 10⁻⁴; 3 × 10⁻⁶ | 3 × 10⁻⁴; 10⁻⁵ |
| what binds | **ϱ** (ε budget); 𝔰_\* sets ε, 5.0 below the closing | ϱ; 3.4 | ϱ; 6.4 | ϱ; 6.7 |
| ϱ coefficient × 0.1 | +0.99 | +0.97 | +1.00 | +0.85 |
| rule cost against G0l, (decades ratio)^4.5 | 0.73 | 0.75 | 0.77 | 0.77 |

**The split.** P-GRD10 gives **2.12–2.68 decades at level 6,** all of the gain: the baseline reproduces G0l exactly in all
four cases.

**It reaches further than at level 4 because no S_M caps it** (deduced).
- **ϱ binds and ε is set by 𝔰_\*,** so ϱ ∝ 1/(sup C_(∞,μ)^(2) · k₂^z), as in G0l.
- **The leading term of C_(∞,μ)^(2) falls three ways:**
  - C^♯ (−0.375);
  - the weight (−0.92 to −1.30, with 𝔗 = 1);
  - 𝔐_p^(2) in place of (2𝔐^(2))^½ max(C_S, C₁).
- **𝔐_p measured.** At the diagnostic level 𝔵^z = 0.05, 𝔐_p^(1)/C₁ = 10^0.62–0.76 against √114 = 10^1.03, and 𝔐_p^(2)/C₁ =
  10^0.98–1.16 against √800 = 10^1.45. At the optima's 𝔵^z ≤ 0.01 the family terms (43n)^½𝔵^z are smaller, which brings
  these toward the writer's 10^0.3–0.46 and 10^0.44–0.76 (deduced).
- **Total:** about 2.0–2.6, in line with the measured 2.1–2.7.

**What is unchanged from G0l:**
- f sits 0.1–0.5 above ϱ.
- The ϱ coefficient remains the first lever at level 6: × 0.1 gives +0.85–1.0.

**Grid edges:**
- ϑ₂ takes the smallest value of the grid, 3 × 10⁻⁴, in all four cases. G0l's refinement from 10⁻³ to 3 × 10⁻⁴ was worth
  ≤ 0.06.
- 𝔰_♭ takes its smallest, 10⁻⁸, at seed 2, D\*. There 𝔰₁^v cancels out of ϱ, so a lower 𝔰_♭ moves only the rates.

## G0m.5 Caveats

1. **G0c's approximants, growth model and couplings,** as before. α_𝔄, q₁ and k₃ are G0c's estimates. 𝔞_𝔄(𝔚) is taken
   at its proved trivial bound.
2. **𝔷′ uses G0b's maxima of |∇T| and |∇E_ab|,** an upper bound of the ℓ² sum. 𝔷₂′ keeps √7, since no per-field bound of
   D̂²Z is held. 𝔷′ acts only through the μ^½ parts.
3. **One factor q = max(q₂, q₃) on the ℰ_g parts,** conservative by ≤ 0.05 on the C_S entries, which do not lead.
4. **𝔗 at level 4 is lem:tl5-hfq-theta's** on every part with ϱ and η₀, as the writer reads it. The other reading for the
   bootstrap's C_(P,ϱ)^v and C_(P,0)^v changes no max-min value (§G0m.2).
5. **The products take C^♯ and no weights,** as the text has them. Weights there are the hypothetical lever of §G0m.3.
6. **Level 6 evaluates option (b) only.**
7. **The level-6 𝔐_p diagnostics are at 𝔵^z = 0.05,** which overstates them against the optima's 𝔵^z.
8. **No refined grid was run.** G0l's refinement was worth ≤ 0.07, and the baseline shows G0m's grid within 0.07 of G0l's
   refined one.
9. **The correction to G0l's S_F column** (see the head of this report) changes no G0l result.

## G0m.6 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0m/`)

| file | what |
|---|---|
| `levelP.py` (G0l's `levelZ_head.py` + `levelZ_mid.py` + `levelP_tail.py`; `patchP.py` turns G0l's tail into it) | thm:tl5-hfp. Switches: `G0M_P=0` the G0l path; `G0M_SHARP`, `G0M_FAM`, `G0M_SPLITC`, `G0M_ZP`, `G0M_TT`, `G0M_MU1`, `G0M_YS` each P-GRD10 change; `G0M_TLIN` the other 𝔗 reading; `G0M_SMQ` the S_M hypothetical; `G0M_SB` the 𝔰_♭ list |
| `ceq.py` | C_(E,r)(𝔶)² of lem:tl5-hfp-leaf (multiplicities as G0f's ce.py), summed to 2j₁ < 80000 with the tail |
| `runP.sh`, `schedP.sh`, `schedB.sh`, `jobsP.txt`, `jobsB.txt` | variants and job lists, nice 19, at most two at a time. `v0` and `voff`: the checks; `main`; `base`: the G0l formulas on this grid; `noy`, `nofam`, `nosplit`: attribution; `tlin`, `smq`, `hy`, `c1h`: readings and levers; `diag`: split diagnostics |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_p.json`, `*_pbase.json`, `*_p{noy,nofam,nosplit,tlin,smq,hy,c1h}.json`, `p_*.log` | the runs |
| `ruleP.py` | tables (`python3 ruleP.py _p g0l x` adds θ × s and the constant diagnostics); it prints S_F itself |
| `G0m.md` | copy of this report |
