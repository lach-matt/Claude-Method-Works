# G0o: the twelfth sharpening (P-GRD12, one leaf constant for every rank and the type-D products over the words) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0o/` and ran
under `nice -n 19`, at most two at a time. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD12 (sec:tl5-hfd), at levels 4 and 6.
- **Source:** implemented from the draft at 59f30503 (P-GRD12.md md5 eec80894).
- **Confirmed text:** at bb003245 (md5 e3418723). Its changes touch no factor this evaluation uses, so the numbers here
  hold for it.

**Replacements implemented** (lem:tl5-hfd-leaf, lem:tl5-hfd-words, def:tl5-hfd-constants, thm:tl5-hfd):
- **The leaf constant.** C_(E,0)(𝔶) replaces C_(E,r)(𝔶) for every rank, and C_(E,0)^♯ replaces C_(E,r)^♯, in every
  face-Sobolev constant:
  - C_S^p, C₁(𝔚), C₁^p, C₁^Γ;
  - C_(1,ϱ)^p, C_(1,0)^p, C_(0,0)^p with their 𝔗;
  - the products' 𝔭₃ and 𝔭₄, and so 𝔛^u₁, 𝔛^u₂, 𝔛′^u₂;
  - through these, 𝔨_rec^(·,p), C_P^v, 𝔐_p^(m), 𝔎, S_F, S_M, 𝔯 and 𝔰_\*.
- **How the leaf constant is formed.** C_(E,0)(𝔶)² is computed as 𝔖₀(𝔶), the sum over π for spin zero, which is the
  largest of the 𝔖_j(𝔶): the maximum over j of the sum over π, as the proof forms it. The reader's figures are
  reproduced:
  - C_(E,0)(1)² = 0.0872507;
  - at 𝔶 = (μ⁻², μ⁻¹), μ = 10⁻⁴, the ratios to C_(E,r)(𝔶) are 0.200012 / 0.089451 / 0.040005 (r = 2 / 3 / 4);
  - 𝔖_j(1) agrees with the reader's 0.0872507 / 0.0290836 / 0.0165243 / 0.0115952 / 0.00894971 to the truncation tail
    (2.5 × 10⁻⁶ without the tail term).
- **The type-D products in S_F.** 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ replace 𝔤_(𝒥,s)𝔎, 𝔤_(𝒥,s)𝔎_ϱ and 𝔤_(𝒥,s)𝔎₀ in S_F and 𝔯_(w,s).
  - **𝔠^D_n(μ)** = 16Σ⁴_n λ̂^♮_(k₁)(μ)λ̂^♮_(k₂)(μ) is computed pointwise.
  - **𝔠^(D,7)_n(μ)** = 16Σ⁴_n λ̂^♮(7μ)λ̂^♮(7μ) 7^(min(k₃,k₄)/2) χ is computed pointwise. At Λ = 0 it is 80 / 160 / 583 / 1430 /
    1853 (N = 4) and 5213 at n = 4 for N = 6, the writer's table. At the optima 𝔠^(D,7)₄(μ) has its median at 1871–1908,
    above 1853 as the reader notes.
  - **The rest, 𝔠^♮_n − 𝔠^D_n + 1,** has its median at 55–117 at n = 4.
  - 𝔤_(𝒥,s) stays in the minimum of ε_(w,q).
- **Unchanged:** ε^z, 𝔤_(ϱ,s), 𝔰₀, 𝔰₁^v and the cap, 𝔨_♯, K_rec, k₂^z, 𝔵^z, 𝔩, 𝔞_𝔄, 𝔠^Mq and the rates.

**Method: as in G0n,** the same grid at level 4 and G0m's at level 6. A refined (𝔰_♭, ϑ₂) grid was added at level 4.

**Checks** (computed):
- With both changes switched off (`G0O_D=0 G0O_W=0`), the code reproduces G0n at level 4 (10^−24.81, seed 1 D_A) and
  G0m at level 6 (10^−35.84).
- **Containment.** The weights in this evaluation are 𝔶 = (μ^(−2s), μ^(−s)) with s ∈ [0, 1], so 𝔶₀, 𝔶₁ ≥ 1 throughout.
  Every optimum takes s = 1. So the comparison against thm:tl5-hfu (G0n), and against thm:tl5-hfp, is inside the range
  where thm:tl5-hfd contains them. The reader's caveat about 𝔶₀ < 0.0065 does not arise.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0o/` (§G0o.5);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0n, G0m or P-GRD12, cited.

---

## G0o.0 Level 4 (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD12** | **10^−23.46** | **10^−22.19** | **10^−30.60** | **10^−27.61** |
| on the main grid | −23.48 | −22.19 | −30.60 | −27.61 |
| G0n (P-GRD11) | −24.81 | −23.48 | −31.65 | −28.66 |
| **gain** | **+1.35** | **+1.28** | **+1.05** | **+1.05** |
| of which the leaf constant | +1.05 | +1.05 | +1.05 | +1.05 |
| of which the type-D word sums | +0.28 | +0.24 | 0.00 | 0.00 |
| of which the refined grid | +0.02 | 0.00 | 0.00 | 0.00 |
| f / ϱ | −23.48 / −23.45 | −22.19 / −22.08 | −30.60 / −30.54 | −27.61 / −27.50 |
| η₀ | −18.9 | −17.7 | −20.4 | −18.8 |
| 𝔶 | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) |
| 𝔵^z | 0.086 | 0.039 | 0.048 | 0.092 |
| 𝔰₁^v (what sets it) | 5.0 × 10⁻⁵ (𝔰_♭/2) | 5.9 × 10⁻⁶ (the cap) | 1.4 × 10⁻⁵ (the cap) | 4.5 × 10⁻⁶ (the cap) |
| θ | 11/16 | 13/16 | ¾ | ⅞ |
| ϑ₁ / ϑ₂ | 0.0057 / 0.03 | 0.00057 / 0.003 | 0.0013 / 0.03 | 0.00044 / 0.01 |
| 𝔯; μ; 𝔰_♭ | 0.001; 10⁻⁵; 10⁻⁴ | 0.001; 10⁻⁴; 10⁻⁴ | 0.001; 10⁻⁶; 10⁻⁴ | 0.001; 10⁻⁵; 10⁻⁴ |
| share of ε given to f | 0.8 | 0.7 | 0.9 | 0.6 |
| log₁₀ S_F / log₁₀ S_M (G0n) | 17.61 / 16.32 (19.00 / 17.02) | 16.27 / 15.17 (17.76 / 16.14) | 23.67 / 21.98 (25.16 / 23.04) | 20.84 / 19.17 (22.23 / 20.22) |
| what binds | **f: 𝔰_\*** (closing 0.08 spare) | **f: 𝔰_\*** (0.09) | **f: 𝔰_\*** (0.67) | **f: 𝔰_\*** (0.39) |
| rule cost against G0n, (decades ratio)^4.5 | 0.78 | 0.78 | 0.86 | 0.85 |

The parts are computed by switching each change off in turn. Each part is the same whether or not the other is on: the
leaf constant alone gives +1.05 in every case, and the word sums alone +0.28 / +0.24 / 0 / 0.

**The leaf constant is worth +1.05 in all four cases, as the writer deduced.**
- C_P^v falls by the leaf ratio, 1.05 at 𝔶 = (μ⁻², μ⁻¹). It is still led by 𝔨_rec^p at every point.
- 𝔰_\*, whose A-term carries C_P^v, binds throughout, so the 1:1 rate passes the fall on whole.
- Measured at 𝔶 = 1 against the same constants: C_P^v −0.82, then −0.22 more from q₀ against q₃ at s = 1.

**The type-D word sums are worth +0.28 and +0.24 in D_A, and nothing in D\*.**
- They act on S_F alone. In D_A the optimum uses the room they free in the closing to take a larger ϑ: at seed 1 D_A, ϑ₂
  goes from 0.003 to 0.03, and 𝔰₁^v rises from 5.9 × 10⁻⁶ to 5.0 × 10⁻⁵, which pushes the 𝔰_\* threshold out.
- In D\* 𝔰_\* already has 0.39–0.67 to spare, which no S_F lever reaches.
- **𝔎^D against 𝔤_(𝒥,s)𝔎** at the supremum, at the optima: −0.57 / −0.16 / −0.24 / −0.06. **S_F falls by 0.34–0.44 beyond
  the leaf's 1.05** (at the same parameters in D\*; about the same in D_A). That is less than the writer's −1.0 to −1.65 for the j′ = 4 term. The other terms of 𝔤𝔎 (j′ ≤ 3,
  and the rest 𝔠^♮ − 𝔠^D + 1 carried with 7^(j′/2)) keep 𝔎^D from falling as far as its j′ = 4 term.

**Grid edges.** At seed 1 D_A, 𝔰₁^v is now set by 𝔰_♭/2. A refined grid (𝔰_♭ ∈ {10⁻⁴, 2 × 10⁻⁴, 5 × 10⁻⁴, 10⁻³,
3 × 10⁻³}, seven ϑ₂ up to 0.1) moves it by +0.02 and the other three by 0.00.

## G0o.1 What binds (computed)

**𝔰_\* binds in all four cases,** 0.08–0.67 below the closing.

**What is now far from binding:**
- S_M stays 1.1–1.7 decades below S_F.
- ϱ sits 0.03–0.11 above f, and its 𝔯 budget is 3.4–5.2 decades away.

**C_S.** It took only the rank-2 factor (−0.70 at the weights, against −1.05 on C_P^v). So C_P^v now stands 1.29 / 1.37 /
1.44 / 1.55 decades above 2C_S, closer than in G0n (1.6–1.9) but still ahead. C_S takes over after about 1.3–1.5 more
decades of 𝔨_rec^p.

**The C_P^v levers stay at the 1:1 rate.** C₁ ÷ 2 gives +0.30 in all four cases (computed).

## G0o.2 The levers re-ranked at level 4

Each lever is priced against the P-GRD12 optimum (computed where marked; hypothetical, not proved).

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **any C_P^v lever, at the measured rate:** C₁ ÷ 2 | **+0.30** | **+0.30** | **+0.30** | **+0.30** | computed; 1:1 |
| the word sums for the other monomials too (the count 7^(j′/2) removed from the rest 𝔠^♮ − 𝔠^D + 1) | 0.00 | +0.21 | 0.00 | +0.34 | computed; 𝔰_\* caps it |
| a further ϱ lever (ε's coefficient × 0.1) | +0.15 | +0.23 | +0.08 | +0.20 | computed |
| 𝔠^♮₄ at its b = 0 floor | ≈ 0 | ≈ 0 | ≈ 0 | ≈ 0 | G0n's computed 0.00–0.01 |
| the refined (𝔰_♭, ϑ₂) grid | +0.02 | 0.00 | 0.00 | 0.00 | computed |

**Ranking at level 4:**
1. **C_P^v levers, at 1:1,** until C_S leads, about 1.3–1.5 decades away. The candidates are those G0n named, less the
   leaf constant now taken:
   - the k-term of C₁ (𝔩, k₁^D = 𝔨_♯K_rec ≈ √5, sharp in this argument);
   - 1/z̲ at the supremum (≤ +0.15 D_A, ≤ +0.03 D\*);
   - the rank-3 step's other factors (𝔵₃, 𝔳₀^r).
2. **The other monomials over the words:** up to +0.34, capped by 𝔰_\*. The family costs in 𝔨_A and 𝔨_B, which P-GRD12
   notes, are not included, so this is an upper bound.
3. **ϱ levers:** ≤ +0.23.

## G0o.3 Level 6, briefly (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD12** | **−34.79** | **−31.44** | **−43.75** | **−37.64** |
| G0m (P-GRD10; P-GRD11 does not act at N ≥ 6) | −35.84 | −32.49 | −44.79 | −38.69 |
| **gain** | **+1.05** | **+1.05** | **+1.05** | **+1.05** |
| of which the leaf constant / the word sums | +1.05 / 0.00 | +1.05 / 0.00 | +1.05 / 0.00 | +1.05 / 0.00 |
| f / ϱ | −34.44 / −34.79 | −30.96 / −31.44 | −43.24 / −43.75 | −37.52 / −37.64 |
| what binds | **ϱ** (ε budget); 𝔰_\* sets ε, 5.9 below the closing | ϱ; 3.8 | ϱ; 6.8 | ϱ; 7.0 |
| ϱ coefficient × 0.1 | +0.99 | +0.97 | +1.00 | +0.85 |
| rule cost against G0m | 0.87 | 0.86 | 0.90 | 0.88 |

**The gain is the writer's upper figure, +1.05,** as he deduced.
- ϱ ∝ 1/(sup C_(∞,μ)^(2) k₂^z), and the leading term of C_(∞,μ)^(2) is C₁'s, which falls by the rank-3 ratio. Measured at
  𝔶 = 1, C_(∞,μ)^(2) falls −0.824, and q₀ against q₃ adds −0.22.
- The word sums act on S_F, which does not bind at level 6: worth 0.00, computed.
- The grid edges are G0m's: ϑ₂ = 3 × 10⁻⁴ throughout, and 𝔰_♭ = 10⁻⁸ at seed 2 D\*.

## G0o.4 Caveats

1. **G0c's approximants, growth model and couplings,** as before.
2. **𝔠^D and 𝔠^(D,7) are formed pointwise** from G0c's λ̂^♮, as 𝔠^♮ is. Their split of 𝔠^♮'s part above its floor
   follows from those λ̂^♮, so it is not one of the writer's two extremes.
3. **The other-monomials lever is hypothetical** and omits the family costs.
4. **Level 6 evaluates option (b) only,** as in G0m.

## G0o.5 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0o/`)

| file | what |
|---|---|
| `levelO.py` (G0l's head + G0n's `levelU_mid.py` + `levelO_tail.py`; `patchO.py` builds the tail from G0n's) | thm:tl5-hfd on top of thm:tl5-hfu / thm:tl5-hfp. `G0O_D=0` and `G0O_W=0` switch off the leaf constant and the word sums; HYPS `nw` prices the other monomials over the words; plus G0m's and G0n's switches |
| `ceq.py` | the leaf sums (rank 0 now serves every rank) |
| `runO.sh`, `schedO.sh`, `jobsO.txt` | variants and job list, nice 19, at most two at a time. `v0`: the checks at levels 4 and 6; `main`; `nod`, `now`: attribution; `c1h`, `hyw`: levers; `sbr`: the refined grid |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_o*.json`, `o_*.log` | the runs |
| `ruleO.py` | tables against G0n (level 4) and G0m (level 6) |
| `P-GRD12.md`, `P-GRD12-report.md` | the draft and the writer's report as read (59f30503) |
| `G0o.md` | copy of this report |
