# G0p: the thirteenth sharpening (P-GRD13, the transport weights and the ϱ count) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0p/` and ran
under `nice -n 19`, at most two at a time. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD13 (sec:tl5-hfe) at levels 4 and 6, from the draft at 3b2784e4 (P-GRD13.md md5 f1467bc9).

**Replacements implemented** (lem:tl5-hfe-face, lem:tl5-hfe-rho, def:tl5-hfe-constants, thm:tl5-hfe):
- **𝔲₁, the first-order steps.**
  - C₁^(U,l), C₁^(D,l) and C₁^(J,l) take (𝔲₁ + 18𝔲₁⁻¹|D̂∂_γ|²) and 2𝔲₁⁻¹|∂_γ|², for every family 𝔚.
  - 𝔲₁ is one continuous function per (μ, 𝔵^z) row: the pointwise optimum (Y/X)^½ of C₁^(U,l)(Γ)'s bracket, as the
    Comparison proposes, floored at 1. The same 𝔲₁ serves C₁^(D,l), C₁^(J,l), every family (n = 1, 7, 49, 343) and
    C_(1,ϱ)^l.
  - C_(1,ϱ)^l is taken at its 𝔲₁ = 1 value. Since 𝔲₁ ≥ 1 that is an upper bound, and conservative.
  - A check scales 𝔲₁ by 2 and by ½ (§G0p.2).
- **𝔲₀, C_S^l.** 𝔲₀ = (Y/X)^½ pointwise, with X = 1/(2Ω̂²z̲) and Y = 8|D̂∂_γ|²X + 2𝔨₁, giving the bracket 2(XY)^½.
  C_(0,0) is unchanged, as the text has it.
- **𝔲_M, the Y₁ step of S_M.**
  - 𝔲_M is a constant on each face Σ₁(t, v\*), a function of τ₁: the best of 49 values from 0.1 to 10⁵ (1 among them)
    for μ𝔱_(3,0)(t; 𝔲) + 𝔱_(3,1)(t; 𝔲)[𝔩(𝔙₂)]_t².
  - The two suprema are formed from face4opt's per-point 𝔳₀⁶R⁻³.
  - 𝔜′^l₁ uses the same 𝔲_M.
- **The face weights α : β : ρ are re-optimised** for each constant's new face function.
  - C₁: per μ, one search with the new C₁^(U,l)(Γ) as its objective, besides G0o's two. Per face the best is taken,
    U on its own, D and J together.
  - C_S: one search with the new face function, besides the old weights applied to it, per face the better.
  - face4opt's weights (for 𝔵_r, 𝔱_r) are kept. Any choice is admissible.
- **𝔠^ϱ in ε's coefficient of ϱ.**
  - 𝔠^ϱ_n(ν′) = Σ⁴_n λ^♮_(k₁)λ^♮_(k₃) − 1 + 𝔰_♭(Σ⁶_n b^♮_g(k₁)λ^♮_(k₃)λ^♮_(k₅) − 𝔤₀) is computed pointwise. At Λ = 0 it
    reproduces the writer's table (𝔠^ϱ_n + 1 = 1, 2.0006, 4.0029, 8.0132, 16.070 at 𝔰_♭ = 10⁻⁴).
  - It replaces 𝔠^♮ in 𝔤^l_(ϱ,q) (argument ν) and 𝔤^l_(ϱ,t) (argument μ), with min of the two at level 4 and 𝔤^l_(ϱ,t)
    at level 6 (option (b)).
  - The parts with 𝒥_g (𝔎^D) keep their counts.

**Check** (computed): with P-GRD13 switched off (`G0P_L=0`) the code reproduces G0o, 10^−23.48 at level 4 and 10^−34.79
at level 6 (seed 1 D_A, μ = 10⁻⁵).

**Attribution.** Each part is switched off in turn with the rest on: 𝔲₁, 𝔲₀, 𝔲_M, 𝔠^ϱ, and the two new face searches
(C₁'s per-μ search, C_S's search). The figures in the interim message are unchanged; §G0p.1 gives the margins behind them.
P-GRD14 on top of this is reported separately as G0q (`G0q.md`).

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0p/` (§G0p.6);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0o or P-GRD13, cited.

---

## G0p.0 Level 4 (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD13** | **10^−21.95** | **10^−20.70** | **10^−29.10** | **10^−26.02** |
| on the main grid | −22.01 | −20.70 | −29.14 | −26.02 |
| G0o (P-GRD12), its best | −23.46 | −22.19 | −30.60 | −27.61 |
| **gain** | **+1.51** | **+1.49** | **+1.50** | **+1.59** |
| on the main grids (−23.48 / −22.19 / −30.60 / −27.61) | +1.48 | +1.50 | +1.46 | +1.59 |
| lost with 𝔲₁ = 1 | −1.26 | −1.12 | −1.30 | −1.19 |
| lost with 𝔲_M = 1 | −0.21 | −0.31 | 0.00 | 0.00 |
| lost with 𝔲₀ = 1 | −0.01 | 0.00 | −0.13 | 0.00 |
| lost with 𝔠^♮ in place of 𝔠^ϱ | −0.08 | −0.26 | −0.11 | −0.28 |
| lost without the new C₁ face search | 0.00 | 0.00 | 0.00 | 0.00 |
| lost without the new C_S face search | 0.00 | 0.00 | 0.00 | 0.00 |
| f / ϱ | −22.01 / −21.92 | −20.70 / −20.65 | −29.14 / −28.65 | −26.02 / −25.58 |
| η₀ | −18.6 | −18.0 | −20.1 | −19.3 |
| 𝔶 | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) |
| 𝔵^z | 0.068 | 0.047 | 0.109 | 0.122 |
| 𝔰₁^v (what sets it) | 5.0 × 10⁻⁵ (𝔰_♭/2) | 2.0 × 10⁻⁵ (the cap) | 4.5 × 10⁻⁵ (the cap) | 1.4 × 10⁻⁵ (the cap) |
| θ | ¾ | ⅞ | 13/16 | ⅞ |
| ϑ₁ / ϑ₂ | 0.0057 / 0.03 | 0.0019 / 0.01 | 0.0044 / 0.1 | 0.0013 / 0.03 |
| 𝔯; μ; 𝔰_♭ | 0.001; 10⁻⁵; 10⁻⁴ | 0.001; 3 × 10⁻⁵; 10⁻⁴ | 0.001; 10⁻⁶; 10⁻⁴ | 0.001; 3 × 10⁻⁶; 10⁻⁴ |
| share of ε given to f | 0.99 | 0.95 | 0.95 | 0.95 |
| log₁₀ S_F / log₁₀ S_M (G0o) | 16.22 / 14.93 (17.61 / 16.32) | 15.00 / 13.78 (16.27 / 15.17) | 22.61 / 21.07 (23.67 / 21.98) | 19.52 / 17.66 (20.84 / 19.17) |
| what binds | **f: 𝔰_\*** (closing 0.09 spare) | **f: the closing** (𝔰_\* 0.01 spare) | **f: 𝔰_\*** (0.24) | **f: 𝔰_\*** (0.30) |
| rule cost against G0o, (decades ratio)^4.5 | 0.75 | 0.73 | 0.80 | 0.77 |

The headline row takes the best of the main grid and the two refined grids (§G0p.2): seed 1 D_A from the 𝔰_♭ grid
(𝔰_♭ = 2 × 10⁻⁴, the closing and 𝔰_\* then meet), seed 1 D\* from the ϑ₂ grid (ϑ₂ = 0.05, μ = 3 × 10⁻⁶). The other two
are unchanged by either grid. The parts are computed by switching each change off in turn, the rest on. They do not add
exactly (the sum is 1.56 / 1.69 / 1.54 / 1.47 against 1.48 / 1.50 / 1.46 / 1.59), because the optimum moves.

**𝔲₁ is worth +1.1 to +1.3, and C_S now stops it.**
- At 𝔶 = 1 and the optimal μ, 𝔲₁ lowers C₁ by 1.35 / 1.04 / 1.55 / 1.18 decades and 𝔨_rec^p by 1.47 / 1.15 / 1.67 /
  1.40, against the run with 𝔲₁ = 1. (C₁ now sits 2.59 / 2.26 / 3.03 / 2.43 below its z-form, against 1.24 / 1.23 /
  1.47 / 1.25 in G0o.)
- With 𝔲₁ = 1, C_P^v stood 1.30 / 1.28 / 1.59 / 1.66 above 2C_S at the supremum, led by 𝔨_rec^p at every point, as in
  G0o. 2C_S, which 𝔲₁ does not touch, now stops the fall: sup C_P^v falls by 1.28 / 1.15 / 1.56 / 1.41, and at seed 2
  𝔨_rec^p still holds the supremum, 0.11 / 0.22 above 2C_S (§G0p.1).
- The loss with 𝔲₁ = 1 is 1.26 / 1.12 / 1.30 / 1.19. In D_A the fall of C_P^v passes 1:1. In D\* the optimum without
  𝔲₁ moves (𝔰_♭ = 10⁻², smaller ϑ) and recovers 0.2–0.3 of it.
- 𝔲₁ itself (pointwise (Y/X)^½ of C₁^(U,l)(Γ)'s bracket, floored at 1), at the optimal μ: median 1994 / 1146 / 6144 /
  3500, minimum 1313 / 328 / 2903 / 747. The floor never acts there.

**𝔲_M is worth +0.2 to +0.3 in D_A and nothing in D\*.**
- 𝔜′₁ falls 1.41 / 1.30 / 1.65 / 1.53 decades (𝔲_M median 1334 / 750 / 4217 / 2371). S_M falls by 1.29 / 1.28 / 1.41 /
  1.61 against the same run with 𝔲_M = 1.
- With 𝔲_M = 1, S_M stands level with S_F in D_A (16.22 / 16.21, 15.06 / 15.00), and the closing binds by 0.20 / 0.32.
  With it, S_M is 1.2–1.9 below S_F in every case and out of the way. In D\* S_M was below S_F even without it.

**𝔲₀ is worth 0.13 at seed 1 D\* and nothing elsewhere.** It moves C_S by −0.008 / −0.006 / −0.188 / −0.102 at the
supremum (median −0.056 / −0.054 / −0.083 / −0.066; 𝔲₀ median 0.44 / 0.44 / 1.07 / 1.04, range 0.24–5.2). C_S leads
C_P^v now, so what it moves at the supremum passes into 𝔰_\*.

**The face weights α : β : ρ, re-optimised, are worth 0.00 at level 4.**
- C₁: the per-μ search with the new C₁^(U,l)(Γ) as objective changes the optimum nowhere, because C₁ leads C_P^v at no
  point (§G0p.1). It moves C₁ at 𝔶 = 1 by at most 0.02 (seed 1 D\*: −3.03 against −3.01 below the z-form). Per face the
  better of C₁^(U,l) and C₁^(D,l) + C₁^(J,l) is taken; the split wins on 80 % / 66 % / 48 % / 39 % of the points at n = 1.
- C_S: the search with the new face function wins on 28 % / 41 % / 31 % / 32 % of the faces, but never on the face that
  holds the supremum. sup C_S is the same with the old weights to 0.001, the median moves by 0.003–0.004.
- So the fall of C_S at seed 1 D\* (−0.19) is 𝔲₀'s, with the old weights.

**𝔠^ϱ is worth +0.08 to +0.28 at level 4.** ϱ sits 0.05–0.49 above f, so the count acts through ϱ's share of ε, which
the optimum gives back to f (the share rises to 0.95–0.99).

## G0p.1 What binds, and the margins behind the interim figures (computed)

**𝔰_\* binds at three of the four optima, the closing at the fourth.** The margin is lclose − log ε_s at the optimum, in
decades: **+0.09 (seed 1 D_A), −0.01 (seed 2 D_A: the closing binds, 𝔰_\* 0.01 spare), +0.24 (seed 1 D\*), +0.30 (seed 2
D\*).** These are the 0.09 / 0.24 / 0.30 of the interim message.

**C_P^v is led by 2C_S.** At the optimal μ, x = 𝔵_D = 0.05, over the face points (𝔶 = 1 basis):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| share of points led by 2C_S / C₁ / 𝔨_rec^p | **100 %** / 0 / 0 | **91 %** / 0 / 9 % | **100 %** / 0 / 0 | **83 %** / 0 / 17 % |
| log₁₀ sup C_P^v / sup 2C_S | +0.022 | +0.132 | +0.022 | +0.245 |
| log₁₀ sup 𝔨_rec^p / sup 2C_S | −0.195 | +0.109 | −0.108 | +0.223 |
| log₁₀ sup C₁ / sup 2C_S | −0.68 | −0.38 | −0.72 | −0.35 |

- The 83–100 % of the interim message is the first row.
- At seed 1, 2C_S leads at the supremum as well: +0.022 is the factor 1/(1 − 𝔵_D) alone.
- At seed 2, **𝔨_rec^p leads the supremum** by 0.11 (D_A) and 0.22 (D\*), though 2C_S leads most points. That is why the
  C_S lever does nothing at seed 2 and the C₁ lever does (§G0p.3).

**Far from binding:** S_M, 1.2–1.9 below S_F; ϱ's 𝔯 budget, 2.2–4.4 decades away. ϱ itself sits 0.05–0.49 above f.

## G0p.2 Grid edges and refined grids (computed)

| grid | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| 𝔰_♭ ∈ {10⁻⁴, 2 × 10⁻⁴, 5 × 10⁻⁴, 10⁻³, 3 × 10⁻³}, seven ϑ₂ to 0.1 | **+0.06** (𝔰_♭ = 2 × 10⁻⁴) | 0.00 | **+0.04** (ϑ₂ = 0.05) | 0.00 |
| ϑ₂ ∈ {0.003, …, 0.05, 0.1, 0.15, 0.2, 0.3} | 0.00 | 0.00 | **+0.04** (ϑ₂ = 0.05) | 0.00 |

- seed 1 D_A: 𝔰₁^v = 𝔰_♭/2 at the main optimum; 𝔰_♭ = 2 × 10⁻⁴ raises it to 5.9 × 10⁻⁵ (where the cap takes over) and
  brings the closing and 𝔰_\* level.
- seed 1 D\*: the main optimum sat at ϑ₂ = 0.1, the top of the main grid. The extended grid finds the maximum inside,
  at ϑ₂ = 0.05; nothing above 0.1 is better. The edge was not binding.

## G0p.3 The levers re-ranked at level 4

Each lever is priced against the P-GRD13 optimum on the main grid (computed; hypothetical scalings, not proved).

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **C_S ÷ 2** (everywhere C_S^l enters) | **+0.19** | +0.01 | **+0.27** | 0.00 | computed |
| C₁ ÷ 2 | 0.00 | +0.07 | 0.00 | **+0.21** | computed |
| ε's coefficient of ϱ × 0.1 | 0.00 | +0.03 | +0.02 | +0.16 | computed |
| 𝔲₁ × 2, 𝔲₁ × ½ | 0.00, 0.00 | −0.04, −0.04 | 0.00, 0.00 | −0.05, −0.05 | computed |
| the refined (𝔰_♭, ϑ₂) grids | +0.06 | 0.00 | +0.04 | 0.00 | computed |

**C_S is now the lever, at seed 1.**
- C_S ÷ 2 pays +0.19 and +0.27 at seed 1, against +0.30 at a 1:1 rate. C_S enters the closing as well as 𝔰_\*
  (S_F falls 0.22 and 0.23), so 𝔰_\*'s 0.09 at seed 1 D_A does not cap it; at seed 1 D\* ϱ binds under it (f −28.85,
  ϱ −28.87).
- At seed 2 it pays nothing, because 𝔨_rec^p already leads the supremum.

**C₁ pays only where 𝔨_rec^p leads the supremum** (seed 2: +0.07, +0.21), and nothing at seed 1.
- After 𝔲₁, C₁ is not the leading entry at any point. It acts only through 𝔨_rec^p (the k-term 𝔨_♯K_rec√7 C₁^(G)).
- The pointwise 𝔲₁ is the optimum of C₁^(U,l)(Γ)'s bracket. Scaling it by 2 or ½ changes nothing at seed 1, where C₁
  does not act, and costs 0.04–0.05 either way at seed 2, where it does: the pointwise choice is the optimum of the
  pair.

**The ranking at level 4:**
1. **C_S** at seed 1 (≤ +0.27) and **𝔨_rec^p's C₁ term** at seed 2 (≤ +0.21). Each pays where the other does not.
2. **The 𝔰_\* threshold itself.** At three optima 𝔰_\* binds by 0.09–0.30. A sharper 𝔰_\* (a smaller multiple of A,
   or a smaller η₀ term) passes up to that margin through, and then the closing binds.
3. ϱ levers: ≤ +0.16 at level 4.

## G0p.4 Level 6 (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD13** | **10^−31.99** | **10^−28.81** | **10^−40.54** | **10^−34.82** |
| on the main grid | −32.01 | −28.82 | −40.54 | −34.82 |
| with 𝔰_♭ ∈ {10⁻², 10⁻³, 10⁻⁴, 10⁻⁵, 10⁻⁶, 10⁻⁸} | −31.99 (𝔰_♭ = 10⁻⁵) | −28.81 (10⁻⁵) | −40.54 | −34.82 |
| G0o (P-GRD12) | −34.79 | −31.44 | −43.75 | −37.64 |
| **gain on the main grids** | **+2.78** | **+2.62** | **+3.20** | **+2.83** |
| lost with 𝔠^♮ in place of 𝔠^ϱ | −1.88 | −1.69 | −2.00 | −1.76 |
| lost with 𝔲₁ = 1 | −0.90 | −0.92 | −1.20 | −1.16 |
| lost without the new face searches (C₁ and C_S) | 0.00 | 0.00 | 0.00 | 0.00 |
| f / ϱ | −31.96 / −32.01 | −28.82 / −28.75 | −40.52 / −40.54 | −34.82 / −34.80 |
| share of ε given to f | 0.03 | 0.5 | 0.1 | 0.4 |
| μ; 𝔰_♭; ϑ₁ / ϑ₂ | 10⁻⁵; 10⁻⁴; 0.00019 / 0.001 | 10⁻⁴; 10⁻⁶; 5.7 × 10⁻⁵ / 0.0003 | 3 × 10⁻⁶; 10⁻⁶; 4.4 × 10⁻⁵ / 0.001 | 10⁻⁵; 10⁻⁴; 4.4 × 10⁻⁵ / 0.001 |
| log₁₀ S_F | 19.00 | 18.29 | 26.38 | 22.45 |
| what binds | **ϱ and f together** (ε budget); 𝔰_\* sets ε, 4.94 below the closing | 3.74 | 6.11 | 4.98 |
| ε's coefficient of ϱ × 0.1 | +0.90 | +0.61 | +0.81 | +0.40 |
| C_S ÷ 2 | +0.22 | +0.06 | +0.18 | +0.02 |
| rule cost against G0o | 0.69 | 0.68 | 0.71 | 0.70 |

- The parts nearly add: 𝔠^ϱ and 𝔲₁ give 2.78 / 2.61 / 3.20 / 2.92 together against the gains 2.78 / 2.62 / 3.20 / 2.83;
  the new face searches give nothing, as at level 4.
- **𝔲₁ is worth 0.9–1.2 at level 6.** It acts through S_F (19.57 → 19.00, 19.13 → 18.29, 27.46 → 26.38, 23.52 → 22.45
  with it, at the two optima), and so through f; ϱ follows because the optimum re-balances the share of ε.
- **𝔠^ϱ is the larger part at level 6** (+1.7 to +2.0). In G0o ϱ bound, 0.12–0.51 below f. With 𝔠^ϱ the optimum gives
  most of ε to ϱ (the share to f is 0.03–0.5), and f and ϱ end within 0.02–0.06 of each other.
- **𝔰_\* sets ε 3.7–6.1 decades below the closing.** The closing is nowhere near binding at level 6, so anything that
  raises 𝔰_\*'s threshold passes through whole to ε.
- The ϱ coefficient lever is worth 0.4–0.9 at level 6, against ≤ 0.16 at level 4.
- 𝔐_p at x = 0.05: 𝔐_p^(1)/C₁ is 0.79–1.21 decades, 𝔐_p^(2)/C₁ 0.92–1.29.

## G0p.5 Caveats

- C_(1,ϱ)^l is taken at 𝔲₁ = 1. Since 𝔲₁ ≥ 1 this overstates it; no figure here depends on it at level 4, where ϱ does
  not bind.
- 𝔲_M is chosen from 49 values per face; a continuous choice would do at most marginally better.
- The face weights are the best of the searches named, not an optimum over all α : β : ρ.
- The type-D counts and 𝔠^ϱ are pointwise at Λ = 0 and the grid's Λ; 𝔠^♮₄ stays at its proved value (9·2⁴ withdrawn).

## G0p.6 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0p/`)

- `P-GRD13.md` (md5 f1467bc9): the section as read, from 3b2784e4.
- `patchL.py` builds `levelL_tail.py` from `g0o/levelO_tail.py` and `levelL_mid.py` from `g0n/levelU_mid.py`. After it
  come the C_S scaling line (`G0P_CSS`) and `patchL2.py`, which adds two switches that isolate the new face searches
  (`G0P_REOM`, `G0P_CSNEW`), with their defaults unchanged. `levelL.py` = `g0l/levelZ_head.py` + `levelL_mid.py` +
  `levelL_tail.py`.
- Switches (default on): `G0P_L` (all of P-GRD13), `G0P_U1`, `G0P_U0`, `G0P_UM`, `G0P_RHO`, `G0P_REOM`, `G0P_CSNEW`;
  scalings `G0P_U1S` (𝔲₁), `G0P_CSS` (C_S), `G0I_C1S` (C₁).
- `runL.sh SEED N U* VARIANT` runs one case at nice 19. Variants: `v0`, `main`, `nou1`, `nou0`, `noum`, `norho`, `c1o`,
  `cso`, `reo`, `u1x2`, `u1h`, `c1h`, `csh`, `sbr`, `thx`, `sb6`.
- `schedL.sh` with `jobsL.txt` (58 jobs), then `schedL2.sh` with `jobsL2.txt` (20 jobs), two at a time.
- `ruleL.py TAG [REFTAG]` prints the tables; the records are `levelV_s<seed>_<N>_<u*>_<tag>.json`, the logs `p_*.log`.
