# G0l: the ninth sharpening (P-GRD9, the recovery sharpened and counted over the words) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0l/`, through job
scripts with absolute paths. After the coordinator's status check, the remaining jobs ran under `nice -n 19`, at most two
at a time. The four level-6 baseline jobs were first dropped and then, at the author's request, run after all. I read
nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD9 (sec:tl5-hfz).
- **Source:** implemented from the draft at d8914603.
- **Confirmed text:** at 0584a614 (P-GRD9.md md5 d4edf2d9). It differs from the draft by four nits and no factor, so the
  numbers here hold for it.

**Replacements implemented** (def:tl5-hfz-constants, lem:tl5-hfz-abs, lem:tl5-hfz-words, lem:tl5-hfz-c1, thm:tl5-hfz):
- **The recovery.**
  - 𝔨_♯(𝔥) K_rec replaces (6/5)(√3 + 8/3) K_rec in every k₁^(j,ν′): every level j, and the weights μ, ν and 1.
  - It also replaces it in 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0.
  - (1 − 𝔥)⁻¹ replaces 8/5 in front of α_𝔄, and 𝔯_♯/(1 − 𝔥) replaces (6/5)𝔯₀.
  - For 𝔥 I take one upper bound of 𝔰₁^v over all rows, min(c_*κ/2, the largest cap): 3.9 × 10⁻⁴ (D_A), 9.1 × 10⁻⁵ (D\*).
    This is conservative and gives 𝔨_♯ = 2.237 against 5.278.
- **k₂^z = q₁/(1 − 𝔥)** wherever k₂ enters:
  - C_(1,ϱ);
  - C_(P,ϱ)^v through "𝔨_rec^ϱ + k₂";
  - ς_t, and through it 𝔯_M and ε_M;
  - the ϱ terms of the products;
  - ε's coefficient.
- **𝔵^z = 𝔰₁^v (5/8)(1 − 𝔰₁^v)⁻¹ sup k₃,** computed row by row. It enters every replacement of lem:tl5-hfy-abs. The
  thresholds 𝔰₀ and 𝔰₁^v keep k₃.
- **C₁^z of eq:tl5-hfz-c1.**
  - The k-term is 2|∂_γ|²(𝔩 + (2ϖ′)^½)².
  - 𝔩 = 𝔩₀ + √43 𝔵^z (k₁^z + 2)/(1 − 𝔵^z).
  - 𝔩₀ is k₁^z with 𝔞_𝔄 taken at its proved bound (43/2)^½ α_𝔄^(N−1,μ).
  - C₁^z replaces C₁^x everywhere, with no minimum: in C_P^v, 𝔨_rec^z, S_F and the 𝔰_\* terms, and at level 6 in
    C_(∞,μ).
- **C_(1,ϱ)^z:** 2(k₂^z)²/(1 − 𝔵^z)² replaces 8k₂²/(1 − 𝔵)².
- **The closing condition** is eq:tl5-hfz-closing, with ε^z's coefficient of ϱ equal to 𝔰₁^v(1 − 𝔵^z)⁻¹ 𝔤_ϱ^v k₂^z.

**Method: as in G0k.** Every parameter maximises min(f, ϱ): θ, ϑ₁, ϑ₂, 𝔯, μ, 𝔰_♭ and the ε share. I made three changes
to the search and measured them separately.

| change | G0k | G0l |
|---|---|---|
| ϑ₂ starts at | 3 × 10⁻³ | 10⁻³ |
| floor on ϑ₁ | 10⁻³ | 10⁻⁴ |
| 𝔯 starts at | 0.01 | 0.003 |
| μ | 10⁻⁶ to 10⁻⁴ | 3 × 10⁻⁷ to 3 × 10⁻⁴ |
| ε shares added | | 0.999 and 10⁻⁴ |
| 𝔵 levels | 0, 10⁻³, 3 × 10⁻³, 0.01, 0.03, 0.1, ¼ | every 0.01 up to 0.1, then 0.12–0.25; rounding up now costs ≤ 0.01 |
| face weights of C₁ | optimised once | also optimised for the C₁ in use, per face the better of the two choices |

- **Worth of the search changes** (computed: a baseline run of G0k's own formulas on the same grids): **+0.10 to +0.17**
  at level 4 and **+0.15 to +0.33** at level 6. The baseline run gives C₁^x the same weight freedom as C₁^z.
- **A refined grid adds at most 0.07 at level 4 and 0.06 at level 6.** It has ϑ₂ from 3 × 10⁻⁴ (11 values), 9 values of
  θ, 17 shares and 𝔯 down to 0.001.

**Check** (computed): the same code with every P-GRD9 factor reverted (`G0L_Z=0`), on G0k's grids, reproduces G0k
exactly. Seed 1 D_A gives 10^−28.50, and every μ step matches G0k's log.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0l/` (§G0l.6);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0k or P-GRD9, cited.

---

## G0l.0 Level 4 (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD9** (refined grid) | **10^−26.70** | **10^−25.12** | **10^−33.70** | **10^−30.39** |
| same, on the main grid | −26.77 | −25.15 | −33.70 | −30.40 |
| G0k (P-GRD8) | −28.50 | −26.88 | −35.34 | −32.07 |
| **gain over G0k** | **+1.80** | **+1.76** | **+1.64** | **+1.68** |
| of which P-GRD9 (main grid, same grids for both) | **+1.59** | **+1.56** | **+1.53** | **+1.57** |
| of which the search (baseline + refinement) | +0.21 (0.13 + 0.07) | +0.20 (0.17 + 0.03) | +0.11 (0.10 + 0.00) | +0.11 (0.10 + 0.01) |
| G0k's formulas on the main grid (the baseline) | −28.37 | −26.71 | −35.24 | −31.97 |
| f / ϱ | −26.70 / −26.61 | −25.12 / −25.10 | −33.70 / −33.65 | −30.39 / −30.27 |
| η₀ | −23.3 | −21.8 | −28.8 | −25.4 |
| **𝔵^z at the optimum** | **0.017** | **0.013** | **0.076** | **0.092** |
| 𝔰₁^v (what sets it) | 9.8 × 10⁻⁶ (the cap) | 2.0 × 10⁻⁶ (the cap) | 1.4 × 10⁻⁵ (the cap) | 4.5 × 10⁻⁶ (the cap) |
| θ | 0.6875 | 0.8125 | ¾ | 0.875 |
| ϑ₁ / ϑ₂ | 0.00095 / 0.005 | 0.00019 / 0.001 | 0.0013 / 0.03 | 0.00044 / 0.01 |
| 𝔯 | 0.001 | 0.001 | 0.001 | 0.001 |
| μ | 10⁻⁵ | 10⁻⁴ | 3 × 10⁻⁶ | 10⁻⁵ |
| 𝔰_♭ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ |
| share of ε given to f | 0.95 | 0.9 | 0.9 | 0.6 |
| what binds | **f** (closing; 𝔰_\* 0.13 spare) | **f** (closing; 𝔰_\* 0.03 spare) | **f** (closing; 𝔰_\* 0.02 spare) | **f** (𝔰_\*; closing 0.02 spare) |
| rule cost against G0k, (decades ratio)^4.5 | 0.75 | 0.74 | 0.81 | 0.79 |

**What P-GRD9 does on these backgrounds:**
- **The gain from P-GRD9 itself is 1.53–1.59 decades**, measured against G0k's formulas on the same grids. That is
  more than three times G0k's step (+0.41 to +0.51).
- **The optimum moves to smaller ϑ:** ϑ₂ = 0.001–0.03 and ϑ₁ down to 2 × 10⁻⁴, with θ = 0.69–0.875. The cap 𝔰_(θ,v)
  sets 𝔰₁^v in all four cases. 𝔵^z ends up at 0.013–0.092; on the main grid it was as low as 0.008 (seed 1, D_A).
- **Every parameter is interior to the refined grid except 𝔯,** which takes its smallest value, 0.001. That is worth
  ≤ 0.01: the 𝔯 budget of ϱ is 2.6–4.4 decades away from binding, and η changes by 0.002.

## G0l.1 How much of the constants' fall reaches min(f, ϱ) (computed)

**Basis of the comparison.** The constants are compared at each case's optimal μ, at a fixed level: 𝔵^z = 0.05 against
G0k's 𝔵 = 0.08. The two are the same 𝔰₁^v sup k₃, since 𝔵^z = (5/8)(1 − 𝔰₁^v)⁻¹ 𝔵.

**Like for like** means both constants take their per-face best face weights. Against G0k's single weight choice, C₁^z
gains a further 0–0.13 decades (seed 1, D\*: 0.13).

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| k₁^z at μ\* (G0k's k₁^μ) | 2.37 (5.59) | 3.05 (7.20) | 2.31 (5.46) | 2.35 (5.54) |
| 𝔩 (G0k's √43 (k₁^μ + 2𝔵)/(1 − 𝔵)) | 3.88 (41.0) | 4.81 (≈ 52) | 3.80 (≈ 40) | 3.84 (≈ 40) |
| share of the k-term in C₁^z's bracket at its supremum | 0.934 | 0.955 | 0.931 | 0.933 |
| **C₁^z / C₁^x**, like for like (writer's deduction) | **−1.16** (1.18) | **−1.17** (1.14) | **−1.06** (1.16) | **−1.15** (1.08) |
| **C_P^v ratio**, like for like (writer's deduction) | **−1.54** (1.57) | **−1.56** (1.53) | **−1.45** (1.55) | **−1.50** (1.48) |
| **min(f, ϱ): P-GRD9's part** | **+1.59** | **+1.56** | **+1.53** | **+1.57** |
| entry of C_P^v that leads | 𝔨_rec^z at every point | 𝔨_rec^z at every point | 𝔨_rec^z at every point | 𝔨_rec^z at every point |
| log₁₀ 𝔨_rec^z/C₁^z, C₁^z/2C_S, C_P^v/2C_S | 0.82, 1.01, 1.86 | 0.82, 1.08, 1.92 | 0.97, 1.12, 2.11 | 1.02, 1.16, 2.20 |
| log₁₀ S_F − log₁₀ S_M at the optimum | 2.4 | 2.0 | 2.0 | 2.1 |

**The writer's deductions hold.**
- **C₁** falls 1.06–1.17 decades (deduced 1.08–1.18).
- **C_P^v** falls 1.45–1.56 (deduced 1.48–1.57).
- **k₁^z** is 2.3 at small μ (deduced 2.245). At μ = 10⁻⁴ it is 3.05, because the μ^½ terms 𝔷 and 𝔯_♯ are not
  negligible there.
- **𝔩** is 3.8–4.8 (deduced 3.6–5.1).

**All of the C_P^v fall reaches min(f, ϱ), and a little more.** The gain exceeds the C_P^v fall by 0.01–0.08. That excess
comes from:
- k₂^z, which lowers ε's coefficient of ϱ (by 0.6 at G0k's 𝔵, as the confirmed text records) and so moves the share
  towards f;
- C_(1,ϱ)^z;
- the smaller 𝔵^z in the outer 1/(1 − 𝔵^z).

Both ε limits carry C_P^v:
- the closing through S_F;
- 𝔰_\* through sup C_(∞,μ) = C_P^v.

So the 1:1 transfer that G0i and G0j measured still holds. **C₁ ÷ 2 gives +0.26 to +0.30** (computed, table in §G0l.3).

## G0l.2 What binds next (computed)

The coordinator named three candidates: the 𝔰_\* slack, ϱ, and the part of C₁ without k₁.

**1. The 𝔰_\* slack is used up. It binds next, together with the closing.**
- In G0k the closing bound f with 0.4–0.5 decades of 𝔰_\* to spare in D_A.
- Now the closing and 𝔰_\* < 𝔰₁^v are within 0.02–0.13 of each other in all four cases. The optimiser places ϑ at their
  crossover, through the cap 𝔰_(θ,v), which is 𝔰₁^v here: a larger ϑ raises 𝔰₁^v and with it the 𝔰_\* threshold, while
  a smaller ϑ lowers the rate integrals in S_F.
- **Consequence:** a lever that lowers only S_F + S_M, without C_P^v, is now capped by 𝔰_\*. The word count is worth
  +0.02 at seed 1, D\*, where after it 𝔰_\* binds by 0.9 (§G0l.3).

**2. ϱ does not limit ε.**
- f and ϱ share ε through the split, and ϱ sits 0.02–0.12 above f at the optimum.
- On the main grid ϱ was the smaller at seed 2, D\*, by 0.08.
- The 𝔯 budget and the 𝔰_\* term of ϱ are 2.6–4.4 and 9.5–13 decades away.
- A ϱ lever (the coefficient × 0.1) is worth only +0.04–0.18, because it only moves the share.

**3. The part of C₁ without k₁ is far from binding.**
- At C₁^z's supremum the k-term is 93–95.5 % of the bracket.
- (1 + 18|D̂∂_γ|²)(1 + ϖ′^½)² is the remaining 4.5–7 %.
- ϖ′ is at most 10⁻⁵, so √(2ϖ′) inside the k-term does not matter.
- Removing the rest entirely would lower C₁ by at most 0.02 decades. The k-term is still k₁^z's: 𝔩 ≈ k₁^z(1 + √43
  𝔵^z/(1 − 𝔵^z)) + 2√43 𝔵^z/(1 − 𝔵^z).

**After those three:**
- C_P^v stands 1.86–2.20 decades above 2C_S, so C_S takes over only after another ~1.9 decades of 𝔨_rec^z.
- S_M stays 2.0–2.4 decades below S_F.

## G0l.3 The levers re-ranked for min(f, ϱ) at level 4

Each lever is priced against the main-grid optimum of P-GRD9 (computed where marked; hypothetical, not proved).

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **√301 𝔵^z over the seven fields** (the writer's unfinished lever: √7 only on the ϱ and η₀ parts of 𝔨_rec) | **+0.36** | **+0.25** | **+0.23** | **+0.18** | computed |
| word count 7² in S_F | +0.47 | +0.50 | +0.02 | +0.32 | computed; capped by 𝔰_\* |
| 𝔠^♮₄(μ) → 9·2⁴ | +0.47 | +0.37 | +0.02 | +0.05 | computed; capped by 𝔰_\* |
| 1/z̲ out of 𝔨₂ (in C₁) | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | at the measured rate below; z̲ also changes the rates |
| the rank-3 Sobolev constant | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | at the measured rate |
| k₁^z itself (𝔨_♯ K_rec), halved | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | at the measured rate; 𝔨_♯ → √5 is the best this argument gives (P-GRD9's comparison) |
| a further ϱ lever (ε's coefficient × 0.1) | +0.04 | +0.07 | +0.04 | +0.18 | computed |
| the nonlinear part absorbed over the words, 𝔩 = (𝔩₀ + 2√43 𝔵^z)/(1 − 𝔵^z) | +0.02 | +0.05 | +0.05 | +0.13 | computed |
| a Schur bound of 𝔞_𝔄 equal to α_𝔄 (in place of (43/2)^½ α_𝔄) | ≤ +0.03 | ≤ +0.03 | ≤ +0.03 | ≤ +0.03 | deduced: α_𝔄 ≤ 0.06 against k₁^z ≥ 2.3 |
| the part of C₁ without k₁, removed | ≤ +0.02 | ≤ +0.02 | ≤ +0.02 | ≤ +0.02 | deduced from the bracket shares |
| *measured rate:* C₁ ÷ 2 (−0.30) | +0.30 | +0.26 | +0.26 | +0.28 | computed |

**The √301 lever, as priced.**
- **Where it acts.** In 𝔨_rec^z the term 𝔨_♯ K_rec √7 C₁^z becomes 𝔨_♯ K_rec C₁^(301). C₁^(301) is C₁^z with √301 𝔵^z in
  place of √43 𝔵^z in 𝔩. The 𝔷 terms keep their √7, as do the ϱ and η₀ parts (𝔨_rec^ϱ, 𝔨_rec^0). C₁^z itself is
  unchanged where it enters C_P^v directly.
- **On 𝔨_rec, at the diagnostic level 𝔵^z = 0.05:** C₁^(301)/C₁^z = 10^0.10–0.19, so 𝔨_rec^z falls 0.24–0.32 decades.
  The writer deduced 0.14–0.22 at G0k's 𝔵.
- **At the optimum it is worth +0.18 to +0.36.** It is worth most where 𝔵^z is small: seed 1, D_A takes 𝔵^z = 0.008
  with it.
- **𝔨_rec^z still leads C_P^v** everywhere after it, by 0.59–0.74 decades over C₁^z.

**Ranking at level 4:**
1. **The √301 lever: 0.18–0.36.** It is conditional on writing the family argument over (D̂Ψ_Z)_Z.
2. **The word count and 𝔠^♮₄: up to 0.5,** but capped by 𝔰_\*. Each gives only 0.02 at seed 1, D\*.
3. **About 0.3 each, at the 1:1 rate,** because C_P^v ∝ C₁ still leads:
   - z̲;
   - the rank-3 constant;
   - any reduction of k₁^z.
4. **ϱ levers and the nonlinear absorption: ≤ 0.18.**
5. **The Schur bound of 𝔞_𝔄 and C₁'s non-k₁ part: ≤ 0.03.**

The C₁ and 𝔨_rec levers together still have about 1.9 decades of room before 2C_S leads C_P^v.

## G0l.4 Level 6, briefly (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD9** (refined grid) | **−38.40** | **−34.61** | **−47.47** | **−41.03** |
| same, on the main grid | −38.41 | −34.61 | −47.47 | −41.09 |
| G0k (P-GRD8) | −40.55 | −36.75 | −49.37 | −43.01 |
| **gain over G0k** | **+2.15** | **+2.14** | **+1.90** | **+1.98** |
| of which P-GRD9 (main grid, same grids for both) | **+1.81** | **+1.82** | **+1.64** | **+1.77** |
| of which the search (baseline + refinement) | +0.34 (0.33 + 0.01) | +0.32 (0.32 + 0.00) | +0.26 (0.26 + 0.00) | +0.21 (0.15 + 0.06) |
| G0k's formulas on the main grid (the baseline) | −40.22 | −36.43 | −49.11 | −42.86 |
| f / ϱ | −38.05 / −38.40 | −34.13 / −34.61 | −47.26 / −47.47 | −40.80 / −41.03 |
| 𝔵^z | 0.002 | 0.010 | 0.002 | 0.011 |
| option; 𝔰_♭; 𝔰₁^v | (b); 10⁻⁶; 5 × 10⁻⁷ (𝔰_♭/2) | (b); 10⁻⁶; 5 × 10⁻⁷ (𝔰_♭/2) | (b); 10⁻⁶; 2.3 × 10⁻⁷ (the cap) | (b); 10⁻⁶; 1.4 × 10⁻⁷ (the cap) |
| ϑ₂; μ | 3 × 10⁻⁴; 10⁻⁵ | 3 × 10⁻⁴; 10⁻⁴ | 5 × 10⁻⁴; 3 × 10⁻⁶ | 3 × 10⁻⁴; 10⁻⁵ |
| what binds | **ϱ** (ε budget); 𝔰_\* sets ε, 5.2 below the closing | ϱ; 3.5 | ϱ; 6.3 | ϱ; 5.5 |
| ϱ coefficient × 0.1 | +0.99 | +0.97 | +0.99 | +0.97 |
| rule cost against G0k, (decades ratio)^4.5 | 0.78 | 0.76 | 0.84 | 0.81 |

**The split.** **P-GRD9 itself gives 1.64–1.82 decades at level 6**, measured against G0k's formulas on the same grids.
The search changes give 0.21–0.34. The search counts for more at level 6 than at level 4 (0.11–0.21): G0k's level-6
optimum took ϑ₂ and 𝔯 at the lower ends of G0k's grids, and it now goes on down to ϑ₂ = 10⁻³ and 𝔯 = 0.003.

**Why P-GRD9 gives about 1.7–1.8 here** (deduced; the measured 1.64–1.82 agrees).
- **ϱ binds, and ε is set by the 𝔰_\* threshold.**
- **𝔰₁^v cancels.** ε ∝ 𝔰₁^v / sup C_(∞,μ) and the coefficient of ϱ ∝ 𝔰₁^v k₂^z, so ϱ ∝ 1/(sup C_(∞,μ) · k₂^z).
- **Three factors fall:**
  - C₁^z (−1.1 to −1.2) and k₁^z (−0.37) together, through the leading term k₁^(N−4,μ) √(2M) C₁ of C_(∞,μ);
  - k₂^z (−0.2).

**What is unchanged from G0k:**
- 𝔵^z stays small (0.002–0.01), because the optimum keeps 𝔰_♭ = 10⁻⁶.
- The ϱ coefficient remains the first lever at level 6: × 0.1 gives +1.0.

**The refined grid** moves level 6 by 0.00–0.06. ϑ₂ goes to its smallest value, 3 × 10⁻⁴, in three cases; the most
refinement gained there is 0.06 (seed 2, D\*).

**Cross-check of the refined-grid results against the baselines** (computed, both levels).
- **On G0k's own grids** the reverted code reproduces G0k exactly (§ Check).
- **On the main grid** the baseline gains over G0k only what the search adds: 0.10–0.17 at level 4 and 0.15–0.33 at
  level 6. That is at most a fifth of P-GRD9's part at the same points.
- **The refined grid** adds ≤ 0.07 more to P-GRD9's optimum, small against every entry of the split. The splits above
  are taken on the main grid, where both formulas share every grid point, and the refinement is booked to the search.
- **The baselines' optima repeat G0k's binding pattern:** at level 4 the closing or 𝔰_\*; at level 6 ϱ with 𝔰_\* setting
  ε by 3.5–6.0. Their level-4 optima keep G0k's region: θ 0.625–0.875, 𝔰₁^v set by the cap, and 𝔵 = 0.073 / 0.033 /
  0.122 / 0.147 against G0k's 0.073 / 0.099 / 0.086 / 0.147. So the baseline is G0k at a better grid point, not a
  different optimum.
- **Bottom line:** the P-GRD9 gains of +1.53–1.59 (level 4) and +1.64–1.82 (level 6) are not grid artefacts.

## G0l.5 Caveats

1. **G0c's approximants, growth model and couplings,** as before. The couplings (α_𝔄, q₁, k₃) are G0c's estimates.
   P-GRD9 leaves them as they are and changes only the factors in front of them.
2. **𝔥 is the largest 𝔰₁^v over the rows** (conservative). 𝔨_♯(𝔥) − √5 ≤ 0.0012, negligible.
3. **𝔞_𝔄 is taken at its proved bound** (43/2)^½ α_𝔄^(N−1,μ). A Schur bound would gain ≤ 0.03.
4. **Two levers are hypothetical:** the √301 lever and the nonlinear absorption over the words.
5. **The face weights.** Each C₁ takes, per face, the better of two admissible weight choices:
   - G0k's;
   - one optimised for that C₁ at the middle μ and 𝔵 level 0.05.

   The baseline gives C₁^x the same choice, so the P-GRD9 part is like for like.
6. **The splits are taken on the main grid.** The baselines were not run on the refined grid, so the refinement (≤ 0.07)
   is booked entirely to the search.

## G0l.6 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0l/`)

| file | what |
|---|---|
| `levelZ.py` (`levelZ_head.py` + `levelZ_mid.py` + `levelZ_tail.py`; `patch.py` turns G0k's tail into it) | thm:tl5-hfz: every factor of def:tl5-hfz-constants, C₁^z and C_(1,ϱ)^z of eq:tl5-hfz-c1, 𝔵^z per row. Switches: `G0L_Z=0` gives thm:tl5-hfy (G0k); `G0L_W301=1` the √301 lever; `G0L_NL2=1` the nonlinear absorption; `G0L_AA` the factor on α_𝔄 in 𝔩₀; `G0L_REOPT` / `G0L_REOPT_OLD` the face weights; `G0I_C1S` scales C₁ |
| `runjob.sh`, `jobs*.txt`, `sched2.sh`, `sched3.sh` | the job lists and variants. `val`: the G0k reproduction; `main`, `fine`: P-GRD9; `valg`: the G0k-formula baseline; `w301`, `nl2`, `c1h`: the levers |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_z.json`, `*_zfine.json`, `z_*.log` | P-GRD9 max-min, main and refined grids |
| `levelV_s{1,2}_{4,6}_*_zvalg.json`, `*_zw301.json`, `*_znl2.json`, `*_zc1h.json`, `levelV_s1_4_-2.0_zval.json` | the baseline, the levers and the check |
| `ruleZ.py` | tables (`python3 ruleZ.py _zfine _z x` adds the per-μ constant diagnostics) |
| `G0l.md` | copy of this report |
