# G0r: the fifteenth sharpening (P-GRD15, route (𝔯) for the parts with ϱ and the zeroth order through the shorter words) on top of P-GRD14, at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0r/` and ran
under `nice -n 19`, at most two at a time. No background command ran past 100 minutes. I touched no process except my own
jobs; the seed-1 reference solver (PID 11454) ran throughout. I read nothing under method/, drive/, extracted/ or
recovered/. G0q (`g0p/G0q.md`) is the baseline throughout.

**What I evaluated.** P-GRD15: sec:tl5-hff, Section 57.30, from the chapter at becf0eb0. Its section is identical to
proofs/P-GRD15.md (md5 21ef7990) apart from one trailing blank line. I applied it on top of the P-GRD14 code of G0q.

**Implemented, lever 3a (lem:tl5-hff-zero, eq:tl5-hff-cs).**
- **C_S^f.** At each face point the smaller of the two ways is taken.
  - The first way: 𝔲₀^♯X + 2𝔲₀⁻¹𝔨₁, with X = 1/(2Ω̂²z̲) and 𝔲₀^♯ = 𝔲₀ + 8𝔲₀⁻¹|D̂∂_γ|².
  - The second way: max(6μ𝔷²𝔨₂𝔲₀^♯ + 2𝔲₀⁻¹𝔨₁, 7μ𝔷²𝔨₂𝔲₀^♯).
  - 𝔷 is the code's pointwise 𝔷 (the one behind 𝔨_B = max(𝔷, 𝔤₁)); 𝔨₁ and 𝔨₂ are those of C_S^l.
- **C_S^h, the own leaf weight.**
  - The own leaf weight is 𝔶₀^h = tμ⁻², with t on a 14-value grid (1, ½, 0.3, 0.2, 0.1, 0.05, 0.03, 0.02, 0.01,
    3 × 10⁻³, 10⁻³, 10⁻⁴, 10⁻⁶, 10⁻⁸).
  - Per μ, the chosen t is the one that minimises sup C_P⁰, ties going to the smaller sup C_S^h.
  - Its cost ρ_h = C_(E,0)(𝔶^h)/C_(E,0)(𝔶) is computed with G0m's `ceq.py` at 𝔶 = (μ⁻², μ⁻¹).
- **C_(0,0)^h := ρ_h C_(0,0).** This is an upper bound: it drops the factor 𝔗(𝔶^h)/𝔗(𝔶) ≤ 1.
- **One 𝔲₀.** The text fixes one 𝔲₀ for both constants.
  - At each point, 𝔲₀ minimises max(the bracket of C_S^f, (𝔤₁ρ_h)² times the bracket of C_S^h).
  - The search is a refined log grid, with the old 𝔲₀ = (Y/X)^½ and C_S^f's own optimum among the candidates.
  - With either part off, 𝔲₀ is the old one, which is then the minimiser.
- **The face weights.** Per face, for each constant, the best of G0p's two searches and one new search per μ.

**Implemented, def:tl5-hff-constants.**
- C_P⁰ = max(𝔤₁C_S^h, C_S^f) and C_(P,0)⁰ = max(𝔤₁C_(0,0)^h, C_(0,0)) replace 𝔤₁C_S^l and 𝔤₁C_(0,0) at every G0q site
  of lem:tl5-hfc-h, and in 𝔎 and 𝔎₀.
- C_S^h and C_(0,0)^h go into 𝔨_rec^p and 𝔨_rec^(0,p).
- 𝔐_p^(m) takes C_S^h at b = 0 and C_S^f at b ≥ 1.
- max(C_(0,0)^h, C_(0,0)) goes into the η₀ parts of lem:tl5-hfp-low's step (k₁ × max(C_(0,0), C_(1,0)) in C_(P,0)^v and
  C_(∞,0); at level 4, inside the form with ν).

**Implemented, lever 4 (lem:tl5-hff-rho, route (𝔯) of eq:tl5-hff-routes), level 6.**
- 𝔯_ϱ^f = ϱ 𝒮₀[μ⁻¹(1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰] is added to the ϱ part of the 𝔯 budget.
- In ε's coefficient of ϱ, 𝔰₁^v is replaced pointwise by μ⁻¹C_(P,0)⁰η₀.
- 𝒮₀ is the code's `Snorm` with weight 1, which is the bound the code already uses for 𝒮.
- Both routes are evaluated at every grid point and the better is kept, as the theorem allows. The records keep each route
  apart.

**Unchanged.** η₀ is taken at its largest admissible value, the code's convention since G0m. Lever 1 (Y_f, bounded
through the closing margin 4AB ≤ 0.1) and 𝔤₁ (at the largest 𝔰_♭ of the grid) are as in G0q. The weights 𝔶 are taken at
s = 1 only: G0q's eight optima all take s = 1, and that is where ρ_h is formed. The main grid is G0q's.

**Checks** (computed).
- With P-GRD15 switched off, the code reproduces G0q: 10^−21.731 at level 4 and 10^−31.72 at level 6 (seed 1 D_A,
  μ = 10⁻⁵).
- In the runs with both C_S levers off, the route-(𝔰) records reproduce all four G0q level-6 targets to 0.001.
- The single-μ diagnostic runs reproduce the main optima to 0.001.
- `levelR.py` is built by the recipe that rebuilds `g0p/levelQ.py` byte for byte.

**Coordinator's additions.** Both are evaluated, in §G0r.4. Round 16 is implemented from the draft at 8776cb9a. Its
confirmed text (proofs/P-GRD16.md at 810ef3a6, md5 03dc1572) differs from the draft in wording only (four passages), with
every display and constant unchanged.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0r/` (§G0r.6);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0q, P-GRD15 or P-GRD16, cited.

---
## G0r.0 The targets (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **level 4, P-GRD15** | **10^−21.73** | **10^−20.67** | **10^−28.52** | **10^−25.73** |
| G0q (P-GRD14), main grid | −21.73 | −20.67 | −28.68 | −25.73 |
| **gain** | **+0.003** | **+0.001** | **+0.161** | **0.000** |
| lost with C_S^f off (C_S^f = C_S^l) | −0.003 | −0.001 | −0.152 | 0.000 |
| lost with 𝔶₀^h = 𝔶₀ (C_S^h = C_S^l) | −0.003 | −0.001 | −0.161 | 0.000 |
| writer (deduced, upper) | ≈ 0 through 𝔰_\*; S_F not evaluated | same | same | same |
| what binds afterwards | **the closing** (𝔰_\* 0.20 spare) | **the closing** (0.28) | **𝔰_\*** (closing 0.37 spare) | **𝔰_\*** (0.01) |
| f / ϱ | −21.73 / −21.59 | −20.67 / −20.63 | −28.52 / −28.32 | −25.73 / −25.29 |
| θ; ϑ₂; μ; 𝔰_♭ | 13/16; 0.03; 10⁻⁵; 10⁻⁴ | ⅞; 0.01; 3 × 10⁻⁵; 10⁻⁴ | ⅞; 0.03; 10⁻⁶; 10⁻⁴ | ⅞; 0.03; 3 × 10⁻⁶; 10⁻⁴ |
| log₁₀ S_F (G0q) | 16.00 (16.00) | 14.97 (14.97) | 21.91 (22.40) | 19.52 (19.52) |
| **level 6, P-GRD15** | **10^−29.27** | **10^−27.26** | **10^−37.87** | **10^−33.69** |
| G0q, main grid | −31.72 | −28.53 | −40.25 | −34.53 |
| **gain** | **+2.45** | **+1.27** | **+2.38** | **+0.83** |
| route (𝔰) in place of route (𝔯), lever 3a kept | −31.40 (+0.33) | −28.45 (+0.08) | −39.97 (+0.28) | −34.51 (+0.02) |
| **so route (𝔯) is worth** | **+2.12** | **+1.19** | **+2.10** | **+0.81** |
| lost with C_S^f off | −0.036 | −0.009 | −0.132 | −0.017 |
| lost with 𝔶₀^h = 𝔶₀ | −0.017 | −0.004 | −0.078 | −0.010 |
| lost with both off (route (𝔯) alone) | −0.044 | −0.011 | −0.151 | −0.020 |
| writer (deduced, upper): route at fixed parameters; re-optimised ≈ ρ × 0.1 price | +1.57; ≈ +0.90 | +0.30; ≈ +0.61 | +1.02; ≈ +0.81 | +0.40; ≈ +0.40 |
| writer: lever 3a at least (G0p's C_S ÷ 2) | +0.22 | +0.06 | +0.18 | +0.02 |
| what binds afterwards | **f alone, through 𝔰_\*'s term with A**; the closing 3.60 away | 2.95 | 5.21 | 4.72 |
| f / ϱ | −29.27 / −24.58 | −27.26 / −23.30 | −37.87 / −30.01 | −33.69 / −27.50 |
| ϑ₁; ϑ₂; μ; 𝔰_♭ | 0.0057; 0.03; 10⁻⁵; 10⁻⁴ | 0.0019; 0.01; 3 × 10⁻⁵; 10⁻⁴ | 0.0013; 0.03; 10⁻⁶; 10⁻⁴ | 4.4 × 10⁻⁴; 0.01; 3 × 10⁻⁶; 10⁻⁴ |
| 𝔰₁^v (G0q); share of ε to f (G0q) | 4.0 × 10⁻⁵ (2.0 × 10⁻⁶); 0.999 (0.03) | 1.7 × 10⁻⁵ (5 × 10⁻⁷); 0.999 (0.5) | 1.4 × 10⁻⁵ (4.5 × 10⁻⁷); 0.999 (0.1) | 4.5 × 10⁻⁶ (4.5 × 10⁻⁷); 0.999 (0.4) |

**Route (𝔯) carries the round at level 6.**
- It empties ε's coefficient of ϱ. In its place μ⁻¹C_(P,0)⁰η₀ϱ stands, 10^−10.6 to 10^−13.8 of 0.1𝔰₁^v (§G0r.2). The
  term it adds to 𝔯, 𝔯_ϱ^f, is 5.3–7.0 decades below the ϱ part 𝔯 already had.
- So f takes the whole of ε (share 0.999, the grid's top).
- The optimum moves to an 𝔰₁^v 10–35 times larger (ϑ₂ 0.001 → 0.03 at seed 1 D_A). Under route (𝔰) a larger 𝔰₁^v raised
  ε's ϱ coefficient in proportion, so small ϑ₂ was optimal; that cost is gone.
- The gains, +2.45 / +1.27 / +2.38 / +0.83, exceed both of the writer's figures in all four cases.
  - They exceed the re-optimised figure, G0q's price of ε's coefficient of ϱ × 0.1, because the coefficient falls by 10 or
    more decades, not one.
  - They exceed the fixed-parameter figure (+1.57 / +0.30 / +1.02 / +0.40) through the move of 𝔰₁^v.
- The smallest gain is at seed 2 D\*. There f already had 0.4 of ε, and 𝔰₁^v rises only by 10.
- Under route (𝔯) the ϱ × 0.1 price is now 0.00 in all four cases.

**Lever 3a pays at level 6 through 𝔐_p, little on route (𝔯), more on route (𝔰).**
- On route (𝔯): +0.044 / +0.011 / +0.151 / +0.020.
- On route (𝔰): +0.33 / +0.08 / +0.28 / +0.02, against the writer's at least +0.22 / +0.06 / +0.18 / +0.02.
- On route (𝔯), C_S's part of 𝔐_p^(2) is 2–7 % of its square at the supremum (5–18 % in 𝔐_p^(1), §G0r.2), so the
  fall of C_S reaches the leading entry k₁𝔐_p only through that share.

**Lever 3a at level 4.** It pays only at seed 1 D\* (+0.16), and there both its parts are needed: switching off either
C_S^f or 𝔶₀^h takes back the whole gain, as rem:tl5-hff-what says (C_P⁰ falls only if both fall).
- C_P⁰ falls 0.35–0.58 decades below 𝔤₁C_S^l. After it, 𝔨_rec^p leads every point (100 %, against 14–49 % in G0q).
- sup C_P^v is still 𝔨_rec^p's, so 𝔰_\*'s supremum does not move.
- At seed 1 D\* the products of S_F fall with C_P^v at the points where 𝔤₁C_S^l led. S_F is 21.91 at the new optimum,
  against 22.40 at G0q's (𝔰_♭ = 10⁻², θ = 13/16).
- The closing, which bound by 0.07 there, moves away. The optimum moves to 𝔰_♭ = 10⁻⁴, θ = ⅞, where 𝔰_\* binds with the
  closing 0.37 spare.
- At the other three the integrals of S_F do not move (to 0.004), because their face maxima sit where 𝔨_rec^p or the
  products already led.
- Lever 1 and 𝔤₁ are unchanged from G0q.

## G0r.1 What binds afterwards (computed)

**Level 4.** As in G0q: the closing at seed 1 D_A (𝔰_\* 0.21 spare) and seed 2 D_A (0.28), and 𝔰_\* at seed 1 D\*
(closing 0.37 spare) and seed 2 D\* (0.01). f binds in all four; ϱ is 0.04–0.44 above it, bound by ε.

C_P^v at the optimal μ, x = 𝔵_D = 0.05:

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| share of points led by C_P⁰ / C₁ / 𝔨_rec^p | 0 / 0 / **100 %** | 0 / 0 / **100 %** | 0 / 0 / **100 %** | 0 / 0 / **100 %** |
| log₁₀ sup 𝔨_rec^p / sup C_P⁰ | +0.584 | +0.750 | +0.766 | +0.957 |
| log₁₀ sup C₁ / sup C_P⁰ | +0.096 | +0.258 | +0.153 | +0.386 |
| log₁₀ sup 𝔨_rec^p / sup 𝔤₁C_S^l (G0q) | +0.097 (+0.098) | +0.402 (+0.402) | +0.185 (+0.185) | +0.515 (+0.515) |
| share of 𝔨_rec^p at its sup from its C₁ term | 95.8 % | 94.2 % | 98.6 % | 98.1 % |

- **𝔨_rec^p holds sup C_P^v alone now.** C₁ is the next entry, 0.49–0.61 decades below it, and C_P⁰ is 0.58–0.96 below.
- So the C₁ term of 𝔨_rec^p is the level-4 lever in all four cases (§G0r.3).
- The S_F split is as in G0q: the products f₂𝔎^D lead the linear part by 4.2–4.9 decades at level 4. 𝔎 is led by
  C_P^v𝔨_B at every point (the share led by C_P⁰𝔨_A is 0).

**Level 6.**
- **f binds alone**, through ε, which 𝔰_\*'s term with A sets.
- ϱ is 4.0–7.9 decades above f. It is bound by 𝔰_\*'s ϱ term, with 𝔯's ϱ part 1.0–3.5 decades further and ε's 1.2–3.3
  further.
- The closing is 2.9–5.2 decades away.
- In 𝔰_\*'s term with A, f ∝ 𝔰₁^v/sup(C_(∞,μ)^(2) μ^(−3) e^(φ/2)):
  - **𝔰₁^v** is at 𝔰₀/2 = 1/(4k₃) in D_A. There ϑ's cap is 1.48 and 1.14 times higher, and 𝔰₀ is below 𝔰_♭ = 10⁻⁴, so
    𝔰_♭ does not bind (deduced from the record).
  - In D\*, 𝔰₁^v is at the cap of ϑ₂, c₂ϑ₂ with c₂ = 4.5 × 10⁻⁴.
  - **The supremum** is led by k₁𝔐_p^(2) at every point. 𝔐_p^(2)'s C₁ part holds 93–98 % of its square at the supremum
    (§G0r.2).
  - k₁ there is 𝔨_♯K_rec(1 + μ^½𝔷′) + μ^½𝔯_♯ to 99.7 %, with α_𝔄 at 0.1–0.3 % (§G0r.4).
- So after round 15 the level-6 targets are bound by 𝔐_p's C₁ part (the families C₁(𝔚_b), b ≤ 3), by k₁'s recovery
  factor, and by 𝔰₁^v (k₃ in D_A, the ϑ cap in D\*).

## G0r.2 The quantities the Comparison could not price (computed)

| at the level-6 optimum | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| log₁₀ 𝔯_ϱ^f (𝔯's ϱ budget r/2 = 10^−3.30) | −10.20 | −9.90 | −13.84 | −12.61 |
| log₁₀ 𝔯_ϱ^f/ϱ against the ϱ part 𝔯 had (R_ϱ + r_M) | 14.38 / 19.71 | 13.40 / 19.00 | 16.17 / 23.18 | 14.89 / 21.34 |
| log₁₀ η₀/𝔰₁^v | −17.22 | −15.90 | −20.17 | −18.88 |
| log₁₀ (sup μ⁻¹C_(P,0)⁰η₀)/(0.1𝔰₁^v) | −11.58 | −10.63 | −13.76 | −12.84 |
| the cost C_(E,0)(𝔶^h)/C_(E,0)(𝔶) at the chosen 𝔶₀^hμ² | 1.237 at 0.02 (+0.092) | 1.200 at 0.05 (+0.079) | 1.282 at 0.003 (+0.108) | 1.237 at 0.02 (+0.092) |
| fall of C_S^f: log₁₀ sup C_S^f/sup C_S^l (median pointwise) | −0.58 (−0.61) | −0.43 (−0.49) | −0.69 (−0.81) | −0.53 (−0.63) |
| fall of C_S^h, the cost included | −0.49 (−0.51) | −0.35 (−0.41) | −0.58 (−0.70) | −0.44 (−0.53) |
| C_P⁰ against 𝔤₁C_S^l (h leads C_P⁰ at every point) | −0.49 | −0.35 | −0.58 | −0.44 |
| C_S^f with 𝔶₀^h = 𝔶₀ (the old 𝔲₀) | −0.36 | −0.30 | −0.26 | −0.28 |
| pointwise log₁₀(X/X′), X′ = 6μ𝔷²𝔨₂: min / median / max | 1.74 / 2.03 / 2.13 | 1.40 / 1.62 / 1.72 | 2.19 / 2.94 / 3.18 | 1.88 / 2.52 / 2.77 |
| what one 𝔲₀ costs C_S^f (max / median, decades) | 0.03 / 0.02 | 0.04 / 0.02 | 0.06 / 0.03 | 0.14 / 0.09 |
| 𝔐_p^(2) at the supremum of k₁𝔐_p^(2): C₁ part / C_S part of its square | 0.928 / 0.072 | 0.963 / 0.037 | 0.941 / 0.059 | 0.982 / 0.018 |
| log₁₀ sup (C₁ part) / sup 𝔐_p^(2); (C_S part) / sup 𝔐_p^(2) | −0.015; −0.58 | −0.008; −0.70 | −0.011; −0.65 | −0.004; −0.83 |
| the same for 𝔐_p^(1) (in C_P^v) | 0.82 / 0.18 | 0.90 / 0.10 | 0.85 / 0.15 | 0.95 / 0.05 |

- **Route (𝔯)'s two factors are negligible** by 10–14 decades (ε) and 5–7 decades (𝔯). So the Comparison's condition
  μ⁻¹C_(P,0)⁰η₀ ≤ 0.1𝔰₁^v holds with room, and route (𝔯) attains more than the price it was compared with (§G0r.0).
- **The cost of h's own weight is larger than "1 at 𝔶₀^h = 𝔶₀" suggests.** 𝔶₀ sits in every term of C_(E,0)(𝔶)², not
  only the term with j₁ = j₂ = 0. At 𝔶 = (μ⁻², μ⁻¹) the cost depends on 𝔶₀^hμ² alone: 1.056 at ½, 1.094 at 0.3, 1.164 at
  0.1, 1.222 at 0.03, 1.257 at 0.01, 1.296 at 10⁻³, 1.310 at 10⁻⁴, 1.33 at 10⁻⁶ and 2.28 at 10⁻⁸.
- Since C_S^h's bracket stops falling near 𝔶₀^hμ² ≈ X′/X, the best weight is at 0.003–0.05, and the cost is 0.08–0.11
  decades.
- **The cost decides C_P⁰.** 𝔤₁C_S^h is above C_S^f at every point, so C_P⁰ falls by C_S^h's fall, 0.35–0.58, not by
  C_S^f's.
- **The falls of C_S^f are below the writer's.** The writer gave 0.65–1.30 / 0.56–1.12 / 0.95–1.90 / 0.87–1.74 at level
  4 and 0.65–1.30 / 0.43–0.86 / 0.83–1.66 / 0.74–1.48 at level 6; I measure 0.43–0.69.
  - log₁₀(X/X′) at the face points is 1.6–2.9 (median), against the writer's 1.73–3.79.
  - The fall sits near the ¼ end of the writer's bracket: the integrand falls by ¼ log₁₀(XY/(X′Y′)), with log₁₀(Y/Y′)
    0.40–0.49 (median), as 8|D̂∂_γ|²X is small against 2𝔨₁.
- **One 𝔲₀ costs C_S^f 0.02–0.09 (median).** 𝔲₀ follows C_S^h, which leads C_P⁰. Without the second way at all (𝔶₀^h = 𝔶₀,
  the old 𝔲₀), C_S^f falls only 0.26–0.36.

## G0r.3 Item 4 and the level-6 prices (computed, except where marked deduced)

**1. K_rec at the point holding sup 𝔨_rec^p** (level 4, the optimal μ, x = 𝔵_D = 0.05; in the form of G0q §G0q.2).
- The point is G0q's. 𝔨_rec^p's C₁ term does not depend on C_S, and its terms with C_S^h are below 0.1 % of it.

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| \|T\|⁻¹ | 1.098 | 1.088 | 1.578 | 1.371 |
| λ_M^(−½) | 0.380 | 0.399 | 0.866 | 0.757 |
| K_rec (which part) | 1.098 (T) | 1.088 (T) | 1.578 (T) | 1.371 (T) |
| K_rec²: the T part / the rotation part | 1.205 / 0.144 | 1.185 / 0.160 | 2.489 / 0.750 | 1.879 / 0.573 |
| share of 𝔨_rec^p there from 𝔨_♯K_rec C₁^Γ (rest: the 𝔷₁ term) | 95.8 % | 94.2 % | 98.6 % | 98.1 % |
| over all face points: T part leads; log₁₀(\|T\|⁻¹/λ_M^(−½)) median (range) | 100 %; +0.83 (+0.40 … +1.07) | 100 %; +0.83 (+0.40 … +1.07) | 100 %; +0.46 (+0.07 … +1.07) | 100 %; +0.47 (+0.23 … +1.07) |
| bracket (deduced, as G0q): equal shares / floor, on 𝔨_rec^p | −0.29 / −0.43 | −0.27 / −0.39 | −0.19 / −0.26 | −0.19 / −0.25 |

**2. Prices on the P-GRD15 optimum** (hypothetical scalings, not proved; against the level-4 targets above):

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **𝔨_rec^p's C₁ term (𝔨_♯K_rec C₁^Γ) ÷ 2** | **+0.285** | **+0.254** | **+0.295** | **+0.293** |
| (G0q, on P-GRD14) | (+0.09) | (+0.24) | (+0.06) | (+0.29) |
| after it, share of points led by C_P⁰ / C₁ / 𝔨_rec^p | 41 / 0 / 59 % | 6 / 0 / 94 % | 30 / 0 / 70 % | 33 / 0 / 67 % |
| round 16's constants (P-GRD16, §G0r.4), for comparison | +0.076 | +0.077 | +0.035 | +0.069 |
| level 4: ε's coefficient of ϱ × 0.1 | +0.020 | +0.046 | +0.018 | +0.159 |

- **The C₁ term ÷ 2 now pays nearly its whole 0.28–0.30 in all four cases.** In G0q it paid +0.09 and +0.06 at seed 1,
  because 𝔤₁C_S took the supremum back after 0.10 and 0.19 decades. C_P⁰ is now 0.58–0.96 below 𝔨_rec^p, and the next
  entry, C₁, is 0.49–0.61 below.
- A halving of the C₁ term is now worth its full size at level 4; it was not in G0q. The ceiling it meets next is C₁ (the
  single word), 0.20–0.32 below 𝔨_rec^p's halved supremum (deduced from the margins).
- Against that, round 16's constants lower 𝔨_rec^p's supremum by only 0.05–0.08 decades (§G0r.4), because kind 1 keeps K_rec. The
  deduced brackets (−0.19 to −0.43 on 𝔨_rec^p) bound what a weighted bound on all of C₁^Γ could give, and the ÷ 2 price
  shows what such a fall is worth.

**3. Level 6** (on the P-GRD15 optimum, route (𝔯)):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| share of the points where k₁𝔐_p leads C_P^v (C_P⁰ / C₁ / k₁𝔐_p) | **100 %** (0 / 0 / 100) | **100 %** | **100 %** | **100 %** |
| log₁₀ sup C_P^v / sup C_P⁰; / sup C₁ | +1.02; +0.88 | +1.17; +0.88 | +1.20; +1.01 | +1.43; +1.01 |
| **price of 𝔐_p's C₁ part ÷ 2** | **+0.286** | **+0.295** | **+0.276** | **+0.295** |
| **price of 𝔐_p's C_S part ÷ 2** | +0.009 | +0.002 | +0.007 | +0.002 |
| ε's coefficient of ϱ × 0.1 | 0.00 | 0.00 | 0.00 | 0.00 |
| (route (𝔰), for comparison: ϱ × 0.1) | (+0.83) | (+0.61) | (+0.82) | (+0.39) |

- **At level 6 the lever is 𝔐_p's C₁ part.** Halving it pays +0.28 to +0.30, nearly its whole size: k₁𝔐_p^(2) leads
  𝔰_\*'s supremum, and its C₁ part holds 93–98 % of its square there.
- Halving 𝔐_p's C_S part pays +0.002 to +0.009. After P-GRD15, C_S has done what it can at level 6: 𝔐_p's C_S part is
  0.57–0.83 decades below its C₁ part at the supremum.
- ε's coefficient of ϱ no longer prices: route (𝔯) has emptied it.
- The next levers at level 6 are therefore three: 𝔐_p's families C₁(𝔚_b); the recovery factor k₁ ≈ 𝔨_♯K_rec, which
  multiplies them (§G0r.4); and 𝔰₁^v (k₃ in D_A, the ϑ cap in D\*).

## G0r.4 The coordinator's additions (rounds 16 and 17)

**1. Level 4: the three kinds of C₁^(Γ,l) at the point holding sup 𝔨_rec^p** (x = 𝔵_D = 0.05, the optimal μ).
- **The method.** C₁^(Γ,l) (n = 7, min(C₁^U, C₁^D + C₁^J), the face weights as in the code) is recomputed with kind 2
  scaled by λ, and separately with kind 3 scaled by λ. Kind 2 is the nonlinear parts (43n)^½𝔵^z(…)/(1 − 𝔵^z) of 𝔩_D(Γ) and
  𝔩_J(Γ); kind 3 is the term with 𝔞_𝔄.
- A kind's share is the elasticity log(C₁(λ)/C₁)/log λ at λ = 0.99. The constant is homogeneous of degree one in the
  three kinds, so the shares add to 1 (deduced), and kind 1 is the rest.
- **Kind 1** is the leading terms (μ^½ + ϖ′^½), the remainders (2ϖ′)^½, the face recovery's leading term k₁^D and its
  terms with 𝔷′ and 𝔯_♯.
- The part with ϱ and the terms on S_a are not in C₁^(Γ,l). They sit in 𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p), which round 16 treats
  through 𝔨_Γ (below).

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **kind 1 (family, keeps K_rec)** | **68.8 %** | **69.6 %** | **71.2 %** | **70.9 %** |
| **kind 2 (one number for the seven fields: nonlinear)** | **29.7 %** | **30.1 %** | **28.0 %** | **28.0 %** |
| **kind 3 (𝔞_𝔄)** | **1.5 %** | **0.3 %** | **0.8 %** | **1.1 %** |
| C₁^(Γ,l) with kind 2 ÷ 2; with kind 3 ÷ 2 (log₁₀) | −0.067; −0.003 | −0.064; −0.001 | −0.059; −0.002 | −0.060; −0.002 |
| 𝔨_Γ = (\|T\|⁻² + 6λ_M⁻¹)^½ there; ω = 𝔨_Γ/(√7 K_rec) | 1.439; 0.495 | 1.464; 0.508 | 2.643; 0.633 | 2.306; 0.636 |

**Round 16's constants** (def:tl5-hfk-constants, implemented with `G0R_K16=1`):
- C₁^k(p) = K_rec(p)·C₁^(Γ,l)(p), formed at every face point with ω(p) times the old factor on kinds 2 and 3. That is
  43^½𝔨_Γ/K_rec in place of 301^½, and 𝔞_𝔄^k/K_rec in place of 𝔞_𝔄(Γ).
- **𝔞_𝔄^k.** The code bounds 𝔞_𝔄(𝔚) by (43n/2)^½ α_𝔄, a stacked-rows bound, as it does not form the operator norm.
  With the rows weighted by |T(p)|⁻¹ and λ_M(p)^(−½), the same bound gives 𝔞_𝔄^k ≤ (43/2)^½ α_𝔄 𝔨_Γ (deduced). So
  𝔞_𝔄^k/K_rec carries the same factor ω.
- ω(p) is rounded up to a grid (0.378 … 0.8), which is conservative, as C₁ is nondecreasing in ω.
- 𝔷₁^k = 3(|T|⁻²|D̂T|² + λ_M⁻¹ Σ|D̂K_ab|²)^½ uses the code's per-field bounds; 𝔷₂^k = 2𝔨_Γ × the code's per-field bound of
  |D̂²Z|.
- 𝔨_Γ replaces √7K_rec in 𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k).

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **target with round 16's constants** | **10^−21.65** | **10^−20.60** | **10^−28.49** | **10^−25.66** |
| gain on P-GRD15 (on G0q) | **+0.076** (+0.079) | **+0.077** (+0.078) | **+0.035** (+0.196) | **+0.069** (+0.069) |
| log₁₀ sup 𝔨_rec^k / sup 𝔨_rec^p | −0.080 | −0.076 | −0.047 | −0.048 |
| C₁^k/(K_rec C₁^(Γ,l)) at the sup point | 0.850 | 0.866 | 0.901 | 0.902 |
| ω at the sup point (grid value used) | 0.495 (0.50) | 0.508 (0.52) | 0.633 (0.635) | 0.636 (0.645) |
| what binds | the closing (𝔰_\* 0.21 spare) | the closing (0.29) | 𝔰_\* (closing 0.37) | 𝔰_\* (0.01) |

- **Round 16 gives +0.035 to +0.077 at level 4.** It reaches 0.12–0.30 of the C₁ term's ÷ 2 price, because the 69–71 % of
  kind 1 keeps K_rec.
- Kind 2 carries nearly all the rest. 𝔞_𝔄 is 0.3–1.5 % of C₁^(Γ,l), so its weighted operator norm is worth ≤ 0.003
  decades.
- The ϱ and η₀ parts (through 𝔨_Γ) do not bind at level 4: ϱ is bound by ε there.
- **For a later round, the remaining lever on 𝔨_rec^p is kind 1.** If it took ω as well, the whole C₁ term would fall by
  −log₁₀ ω = 0.31 / 0.29 / 0.20 / 0.20 (the "equal shares" bracket). That is in the range of the ÷ 2 price above.

**2. Level 6: α_𝔄 in k₁, and C₁^l({ZB}) against 𝔐_p^(2)** (the optimal μ; at x = 𝔵_D = 0.05 and at the optimum's x;
the point is the one holding sup C_P^v, where k₁𝔐_p^(1) leads).

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **α_𝔄's share of k₁** (k₁ there) | **0.1 %** (2.91) | **0.2 %** (3.16) | **0.1 %** (4.05) | **0.1 %** (4.13) |
| the same at the point holding sup k₁𝔐_p^(2) (in 𝔰_\*'s supremum) | 0.3 % | 0.3 % | 0.2 % | 0.3 % |
| **log₁₀ C₁^l({ZB}) / 𝔐_p^(2)**, x = 𝔵_D; at the optimum's x | **−0.62**; −0.70 (x 0.17) | **−0.61**; −0.70 (0.17) | **−0.61**; −0.66 (0.10) | **−0.59**; −0.68 (0.14) |
| the same with the suprema taken apart | −0.62; −0.70 | −0.60; −0.69 | −0.62; −0.67 | −0.59; −0.68 |
| log₁₀ 𝔐_p^(1) / 𝔐_p^(2) there, x = 𝔵_D; optimum's x | −0.26; −0.33 | −0.27; −0.34 | −0.26; −0.31 | −0.27; −0.33 |
| log₁₀ C₁^l({ZB}) / C₁ (one word) | +0.08; +0.11 | +0.08; +0.11 | +0.08; +0.09 | +0.08; +0.10 |

- **k₁ in k₁𝔐_p is the recovery factor**, 𝔨_♯K_rec(1 + μ^½𝔷′) + μ^½𝔯_♯/(1 − 𝔰₁^v), to 99.7–99.9 %. α_𝔄 is
  negligible.
- **C₁^l({ZB}) for the seven words ZB is 0.59–0.62 decades below 𝔐_p^(2) at 𝔵_D, and 0.66–0.70 below at the optimum's
  x.** It is 0.32–0.37 below 𝔐_p^(1) there.
- It is only 0.08–0.11 above the one-word C₁, against √7 (0.42) for seven separate words.
- So a bound of the low-level step through the seven words ZB alone in place of 𝔐_p^(2), if the recovery's factor k₁
  stayed, would lower k₁𝔐_p^(2) by up to that 0.6–0.7 decades (deduced). It would then meet C₁, which is 1.1–1.3 decades
  below k₁𝔐_p^(2) now.

## G0r.5 Caveats

- **The weights 𝔶** are at s = 1 only. G0q's optima all take s = 1, and the cost of h's weight is formed there.
- **C_(0,0)^h** is taken as ρ_h C_(0,0), an upper bound.
- **One 𝔲₀.** It is chosen pointwise by a minimax of the two brackets; any choice is admissible. Where the better way
  switches, this 𝔲₀ can jump. A continuous 𝔲₀ near it costs arbitrarily little, as both brackets are continuous in 𝔲₀
  (deduced).
- **𝔶₀^h** comes from a 14-value grid, chosen per μ to minimise sup C_P⁰.
- **η₀** is at its largest admissible value (the code's convention). Under route (𝔯) it enters ε, by 10^−11 to 10^−14 of
  the budget.
- **Round 16:**
  - ω is rounded up to a grid (seed 1 and 2 D\*: refined to 0.635 and 0.645 in a rerun, `k16f`, which the table uses; the coarse grid's 0.70 gave +0.035 and +0.055).
  - 𝔞_𝔄^k is the code's stacked-rows bound with the rows weighted, not the operator norm (deduced, ≤ K_rec𝔞_𝔄 as the lemma
    requires).
  - 𝔷₂^k uses one bound for all seven |D̂²Z|, as 𝔷₂′ does.
- **The kinds' shares** are finite-difference elasticities at λ = 0.99, at x = 𝔵_D, as G0q's item 2.
- **The prices** (÷ 2, × 0.1) are scalings of one term each, not proved bounds.
- **The runner incident.** While a job was running I rewrote `runR.sh` in place. I wrote its old text back before that
  job's shell resumed, so no job ran twice or lost its record (checked: no log carries a shell error). Later replacements
  went through `mv`.

## G0r.6 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0r/`)

- `P-GRD15.md` (md5 21ef7990) and `ch87_becf0eb0.md`: the texts evaluated. `P-GRD16_8776cb9a.md` and
  `P-GRD16_810ef3a6.md` (md5 03dc1572): round 16, draft and confirmed.
- `patchR.py` builds `levelR_tail.py` from `g0p/levelQ_tail.py`. `levelR.py` = `g0l/levelZ_head.py` +
  `g0p/levelL_mid.py` + `levelR_tail.py`; `ceq.py` is G0m's.
- Switches: `G0R_ZERO` (C_S^f), `G0R_H` (𝔶₀^h), `G0R_ROUTE` (route (𝔯)), `G0R_K16` (round 16, with `G0R_OMG`),
  `G0R_MPC1` and `G0R_MPCS` (𝔐_p's parts scaled), `G0R_XDG`; G0q's `G0Q_KRC1`; `G0R_TGH` (the 𝔶₀^h grid).
- `runR.sh SEED N U* VARIANT [MU XDG]` runs one case at nice 19. Variants: `v0` (all off), `s1`, `main`, `nof`, `noh`,
  `zo`, `krc`, `k16`, `k16f`, `k16d`, `d4`, `d6`, `mpc1`, `mpcs`.
- `schedR.sh QUEUE` runs a queue two at a time (`jobsA.txt`, `jobsB.txt`, `jobsC.txt`).
- Printers: `ruleR.py TAG` (targets, routes, what binds, C_S falls, 𝔐_p splits); `r16.py _rd4` (item 4); `sumR.py` (every
  variant against G0q and the main run).
- Records `levelV_s<seed>_<N>_<u*>_r<variant>.json`, logs `r_*.log`. `HANDOFF-G0r-2.md` is the mid-run note.
