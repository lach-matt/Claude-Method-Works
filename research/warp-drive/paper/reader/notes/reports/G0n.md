# G0n: the eleventh sharpening (P-GRD11, S_M with the weights and the families of words) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0n/` and ran
under `nice -n 19`, at most two at a time. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD11 (sec:tl5-hfu), at level four only. At N ≥ 6, S_M = 𝔯_M = ε_M = 0, so G0m's level-6 values
stand.
- **Source:** implemented from the draft at b9d0f611 (P-GRD11.md md5 975cc207).
- **Confirmed text:** at 6c7bbfad (md5 ea6da21c). It changes only the Comparison's 𝔯_M figures, which this evaluation
  computes rather than reads, so the numbers here hold for it.

**Replacements implemented** (def:tl5-hfu-constants, lem:tl5-hfu-face, -fam, -mixed, thm:tl5-hfu):
- **𝔛₁** = C_(E,3)(𝔶) 𝔵₃^½ (1 + ϖ₁^½), that is q₃ · (C^♯²𝔵₃)^½ (1 + ϖ₁^½), in place of (2C^♯²𝔵₃(1 + ϖ₁))^½.
- **𝔛₂** = C_(E,4)(𝔶) 𝔵₄^½ ([𝔩(𝔙_Γ)]_t + μ^½ϖ₂^½), in place of C^♯𝔵₄^½(√602 λ_t^μ + (2ϖ₂)^½).
  - [𝔩(𝔙_Γ)]_t is G0m's 𝔩_D(Γ) + 𝔩_J(Γ), taken as a supremum over Σ₁(t, v\*), with 𝔞_𝔄 ≤ (301/2)^½ α_𝔄.
  - q₄ is summed like q₂ and q₃: 0.0737 / 0.1310 / 0.0414 at μ = 10⁻⁵ / 10⁻⁴ / 10⁻⁶, the writer's table.
- **𝔛′₂** = √301 𝔗 (μ/ν)² C_(E,4)(𝔶) 𝔵₄^½ ς_t.
- **𝔜₁** = (μ𝔱_(3,0) + 𝔱_(3,1)[𝔩(𝔙₂)]_t²)^½.
  - [𝔩(𝔙₂)]_t = [k₁^D + μ^½(k₁^D𝔷′ + (1 − 𝔰₁^v)⁻¹𝔯_♯) + (1 − 𝔰₁^v)⁻¹(49/2)^½α_𝔄^(2,μ) + 7𝔵^z(k₁^(2,μ,p) + 2)/(1 − 𝔵^z)]_t.
  - 𝔱_(3,0) and 𝔱_(3,1) are the two coefficients of 𝔱₃, each taken as a supremum with the face weights of 𝔱₃.
- **𝔜′₁** = 7(μ/ν)^(3/2)𝔱_(3,1)^½ς_t, and 𝔜″₁, 𝔜″₂ each × μ^(3/2).
- **𝔜₂, 𝔠^Mq₁, 𝔠^Mq₂, w_t and [𝔨₂]_t** are unchanged.
- **S_M^u, 𝔯_M^u and ε_M^u** are formed row by row, with the row's 𝔶, θ (ν = μ^θ) and 𝔗 = ((ν²𝔶₀ + 6ν𝔶₁ + 36)/43)^½.
- **𝔯^u** = 𝔯^p − 𝔯_M^p + 𝔯_M^u in η and in the 𝔯 budget of ϱ; ε_M^u enters A_u and ϱ's ε budget.

**Method: as in G0m**, the same grid and code, with ϑ₂ = 0.1 added; no optimum uses it.

**Check** (computed): the same code with P-GRD11 switched off (`G0N_U=0`) reproduces G0m: 10^−25.12 at seed 1 D_A,
μ = 10⁻⁵. So the whole difference from G0m is P-GRD11's.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0n/` (§G0n.5);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0m or P-GRD11, cited.

---

## G0n.0 Level 4 (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD11** | **10^−24.81** | **10^−23.48** | **10^−31.65** | **10^−28.66** |
| G0m (P-GRD10) | −25.12 | −23.80 | −31.99 | −28.80 |
| **gain (all of it P-GRD11's)** | **+0.31** | **+0.33** | **+0.34** | **+0.14** |
| G0m's hypothetical "S_M × q" | +0.31 | +0.26 | +0.34 | +0.14 |
| f / ϱ | −24.81 / −24.67 | −23.48 / −23.46 | −31.65 / −31.59 | −28.66 / −28.54 |
| η₀ (G0m) | −20.8 (−22.8) | −19.3 (−21.5) | −22.4 (−28.2) | −20.6 (−25.0) |
| 𝔶 | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) | (μ⁻², μ⁻¹) |
| 𝔵^z | 0.008 | 0.013 | 0.048 | 0.092 |
| 𝔰₁^v (what sets it) | 5.9 × 10⁻⁶ (the cap) | 2.0 × 10⁻⁶ (the cap) | 1.4 × 10⁻⁵ (the cap) | 4.5 × 10⁻⁶ (the cap) |
| θ | ¾ | 13/16 | ¾ | ⅞ |
| ϑ₁ / ϑ₂ | 0.00057 / 0.003 | 0.00019 / 0.001 | 0.0013 / 0.03 | 0.00044 / 0.01 |
| 𝔯; μ; 𝔰_♭ | 0.001; 10⁻⁵; 10⁻⁴ | 0.001; 10⁻⁴; 10⁻⁴ | 0.001; 10⁻⁶; 10⁻⁴ | 0.001; 10⁻⁵; 10⁻⁴ |
| share of ε given to f | 0.9 | 0.9 | 0.9 | 0.6 |
| log₁₀ S_F / log₁₀ S_M (G0m) | 19.00 / 17.02 (19.00 / 19.22) | 17.76 / 16.14 (17.71 / 17.96) | 25.16 / 23.04 (24.87 / 25.72) | 22.23 / 20.22 (22.03 / 22.51) |
| what binds | **f: 𝔰_\*** (closing 0.10 spare) | **f: 𝔰_\*** (0.02) | **f: 𝔰_\*** (0.24) | **f: 𝔰_\*** (0.05) |
| rule cost against G0m, (decades ratio)^4.5 | 0.95 | 0.94 | 0.95 | 0.98 |

**The new targets:** 10^−24.81 / 10^−23.48 / 10^−31.65 / 10^−28.66 at level 4. Level 6 stands at G0m's −35.84 / −32.49 /
−44.79 / −38.69.

**The writer's bracket holds.**
- The gain equals G0m's hypothetical lower bound at seed 1 D_A, seed 1 D\* and seed 2 D\*, and exceeds it by 0.07 at seed
  2 D_A.
- That is within the deduced "at most about 0.1 more".
- The ceiling is 𝔰_\*: P-GRD11 pushes the closing below it in every case.

**How far S_M fell:** 2.20 / 1.82 / 2.68 / 2.29 decades (deduced 1.8–2.3). It now lies 1.98 / 1.62 / 2.12 / 2.01 below S_F,
where in G0m it was 0.22–0.85 above. At the diagnostic point (𝔶 = 1, 𝔵^z = 0.05, the optimal μ) the factors are:

| factor | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | writer (deduced) |
|---|---|---|---|---|---|
| 𝔜₁: [𝔩(𝔙₂)]_t against 1 + 7λ^(μ,2) | 4.8 vs 23.3 (−0.70) | 6.2 vs 30.6 (−0.70) | 7.1 vs 36.1 (−0.70) | 7.8 vs 38.8 (−0.70) | −0.65 to −0.80 |
| 𝔛₂ before q₄: [𝔩(𝔙_Γ)]_t against √602 λ^μ | 7.6 vs 78 (−1.01) | 10.0 vs 104 (−1.03) | 10.7 vs 123 (−1.00) | 12.1 vs 133 (−1.01) | −1.2 to −1.3 at the optima's 𝔵^z |
| 𝔛₁ before q₃: the triangle inequality | −0.02 | 0.00 | 0.00 | 0.00 | 0 to −0.15 |
| q₃ / q₄ at the optimal 𝔶 | −1.17 / −1.13 | −0.92 / −0.88 | −1.42 / −1.38 | −1.17 / −1.13 | |
| 𝔱_(3,1)/𝔱₃ | −0.03 | −0.03 | −0.03 | −0.03 | 0 (assumed) |

The 𝔩(𝔙) above are taken at 𝔵^z = 0.05, which makes them larger than at the optima's 𝔵^z. That is why 𝔛₂ falls 1.0
here and 1.2–1.3 in the deduction.

**η₀ improves by 2.0–5.8 decades,** through the μ^(3/2) on the terms with η₀. It is not one of the targets.

## G0n.1 What binds (computed)

**𝔰_\* binds in all four cases.**
- It sits 0.02–0.24 decades below the closing, and ϱ sits 0.02–0.14 above f.
- Its term with A carries C_P^v (led by 𝔨_rec^p at every point) and the closing's A.

**What is now far from binding:**
- S_M is 1.6–2.1 decades below S_F.
- The 𝔯 budget of ϱ is 3.3–5.2 decades away.
- ϱ's ε share costs little: ε's coefficient × 0.1 gives only +0.04 to +0.20.

**The C_P^v levers return to the 1:1 rate.**
- C₁ ÷ 2 (−0.30) gives **+0.30 in all four cases** (computed), against 0.3–0.5 per decade in G0m.
- The weights transfer 1:1 as well. Setting 𝔶 = 1 costs −1.17 / −0.92 / −1.40 / −1.17, the same as log₁₀ q₃ at the optimum.
  Both ε limits, and S_F and S_M, now carry the weight.

**A larger cap is not a lever.** The cap 𝔰_(θ,v) × 2 (hypothetical) gives −0.04 to +0.04. 𝔰₁^v is a minimum, not a free
choice, and a larger one also raises 𝔵^z and ε's coefficient of ϱ; the optimiser already sets 𝔰₁^v through ϑ.

## G0n.2 The levers re-ranked at level 4

Each lever is priced against the P-GRD11 optimum (computed where marked; hypothetical, not proved).

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **any C_P^v lever, at the measured rate:** C₁ ÷ 2 (−0.30 on C₁, hence on 𝔨_rec^p and C_P^v) | **+0.30** | **+0.30** | **+0.30** | **+0.30** | computed; 1:1 |
| word count 7² in S_F | +0.28 | +0.44 | 0.00 | +0.34 | computed; the optimum moves to larger ϑ (𝔰_\* spare 0.4–0.7), and at seed 1 D\* 𝔰_\* caps it |
| a further ϱ lever (ε's coefficient × 0.1) | +0.04 | +0.10 | +0.08 | +0.20 | computed |
| 𝔠^♮₄(μ) at its reachable floor (the b = 0 terms alone) | 0.00 | +0.01 | 0.00 | 0.00 | computed (see below) |
| 𝔠^♮₄(μ) → 9·2⁴ | unproved | unproved | unproved | unproved | below the b = 0 floor; withdrawn (see below) |
| the cap 𝔰_(θ,v) × 2 | −0.04 | +0.02 | −0.02 | +0.04 | computed; not a lever |

**The C_P^v levers at 1:1, each priced at the measured rate (deduced):**
- **1/z̲ out of 𝔨₂ in C₁: ≤ +0.15 (D_A), ≤ +0.03 (D\*).** This is the median (𝔨₂′/𝔨₂)^½ of G0m; G0m found it worth nothing
  at the supremum through the split.
- **The rank-3 Sobolev constant: ≈ +0.3**, if halved.
- **k₁^D = 𝔨_♯K_rec: none in this argument.** K_rec is sharp for its step (P-GRD10) and 𝔨_♯ → √5.
- **The √7 on the ϱ and η₀ parts of 𝔨_rec:** not binding.

**𝔠^♮₄ (checked, and corrected).**
- **The implementation agrees with the writer and the reader.** cg2.py evaluates eq:tl5-hfs-cn. At Λ = 0 it gives c^(2♮)_n
  = 80 · 2^n + … : 80, 161, 323, 647, 1295 for n = 0, …, 4. So 𝔠^♮₄(μ) + 1 ≥ 1296 from the b = 0 terms alone, with
  𝔰_♭ c^(3♮)₄ adding about 8 at 𝔰_♭ = 10⁻⁴.
- **At the optima 𝔠^♮₄(μ) sits at that floor:** its median over the points is 1337 / 1362 / 1399 / 1401, against a floor
  of 1303.
- **The "9·2⁴ + 1 = 145" of G0g–G0m was not a count.** It lies below the proved floor, and reaching it needs a bound of 2𝔮̂
  about ten times sharper, which the chapter does not state.
- **The withdrawn prices:** G0k's +0.55 / +0.59 / 0 / 0, G0l's +0.47 / +0.37 / +0.02 / +0.05 and G0m's +0.19 / +0.17 /
  +0.05 / +0.06, and here +0.28 / +0.24 / 0 / +0.10 at that figure. All are withdrawn as unproved.
- **What can be reached** is the Λ-dependent part above the floor. Removing it entirely (𝔠^♮_j(μ) → its b = 0 value,
  computed) is worth 0.00–0.01.

**Ranking at level 4:**
1. **C_P^v levers: 1:1, until C_S or S_F leads.** C_P^v is 1.6–1.9 decades above 2C_S. Candidates: the rank-3 constant,
   1/z̲ at the supremum, and a sharper bound of C₁'s k-term.
2. **The word count 7² in S_F: up to +0.44.** It is worth more than at G0m, as the optimum can now buy 𝔰_\* room with
   larger ϑ. It needs eq:tl5-hfs-products restated over each word length (P-GRD11's "Not done").
3. **ϱ levers: ≤ +0.20.**
4. **𝔠^♮₄ at its reachable floor: ≈ 0.** The 9·2⁴ figure is unproved and withdrawn.

## G0n.3 Level 6

Unchanged from G0m: at N ≥ 6, S_M = 𝔯_M = ε_M = 0. The values are −35.84 / −32.49 / −44.79 / −38.69, with ϱ binding.

## G0n.4 Caveats

1. **G0c's approximants, growth model and couplings,** as before. 𝔞_𝔄(𝔙) is taken at its trivial bounds: (301/2)^½α_𝔄^(3,μ)
   and (49/2)^½α_𝔄^(2,μ).
2. **𝔱_(3,0) and 𝔱_(3,1) are taken with the face weights that face4opt chooses for 𝔱₃,** not re-optimised. Any choice is
   admissible.
3. **[𝔩(𝔙)]_t is taken as a supremum over the face of the pointwise 𝔩(𝔙),** with the pointwise K_rec, 𝔷′, 𝔯_♯ and α_𝔄.
4. **No refined grid was run.** G0l's refinement was worth ≤ 0.07.
5. **The G0m S_F correction** (G0m's head) still applies to G0l. ruleU.py prints S_F itself.

## G0n.5 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0n/`)

| file | what |
|---|---|
| `levelU.py` (G0l's `levelZ_head.py` + `levelU_mid.py` + `levelU_tail.py`; `patchU.py` builds the mid and the tail from G0l's mid and G0m's tail) | thm:tl5-hfu on top of thm:tl5-hfp. Switches: `G0N_U=0` the G0m path; `G0N_CAPF` the cap; HYPS `nw`, `c9` and `cfl` (𝔠^♮ at its b = 0 floor); and G0m's switches |
| `ceq.py` | G0m's leaf sums, now also used for rank 4 |
| `runU.sh`, `schedU.sh`, `jobsU.txt` | variants and job list, nice 19, at most two at a time. `v0`: the check; `main`; `c1h`, `hy`, `hyf`, `cap2`, `noy`: levers |
| `levelV_s{1,2}_4_{-2.0,-1.1}_u*.json`, `u_*.log` | the runs |
| `ruleU.py` | tables against G0m (`python3 ruleU.py _u g0m x` adds the diagnostics) |
| `P-GRD11.md`, `P-GRD11-report.md` | the draft and the writer's report as read (b9d0f611) |
| `G0n.md` | copy of this report |
