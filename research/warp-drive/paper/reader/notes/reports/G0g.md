# G0g: the fourth sharpening (P-GRD4) at level 4, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing. I read nothing under method/, drive/, extracted/ or
recovered/.

**What I evaluated.** proofs/P-GRD4.md at 82aa2785 (md5 fa9f162d): the chapter text (sec:tl5-hfq), the Comparison and
the writer's report. While this ran it was confirmed and merged as sec:tl5-hfq (Section 57.19) at 40140118. I read the
a08ce8c0 diff: proof wording only. The constant carried in C_((∞,0),ν)^(0) is C_(1,0)^♮(ν), as evaluated, and the
Comparison is unchanged.

**One process note.** My first launch of the two reach runs started in the repository directory: the `cd` sat inside a
backgrounded subshell. Each wrote only a "can't open file" log in `paper/reader/`. The coordinator deleted those logs. The
reach runs were relaunched at once from `scratchpad/g0g/` and are the ones used here. `git status` is clean.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0g/` (§G0g.7);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0f, G0e or P-GRD4, cited.

**Evaluated as in G0f, level 4 only.**
- **Sobolev constants:** intrinsic, with the rigorous C_(E,r)² bounds 0.8942 / 3.6375 / 15.710. α, β, ρ are optimised
  per face for C_S, C₁, C_(1,0) and C_(1,ϱ), and once per t for the level-4 face quantities.
- **Unchanged from G0f:** approximants, grids, rates, couplings, growth model, κ = κ′ = ϑ = 10⁻² and the targets
  (margin 10, δ_w ≤ ε, budget splits).
- **Implemented as in the formula list:**
  - 𝔠^Mq₁, 𝔠^Mq₂;
  - k₃^♮(ν), 𝔰₀^q and 𝔰₁^q;
  - 𝔰_(\*,q) with C_(∞,μ)^(0)μ^(−2) on A_q and ν^(−2)(C_((∞,ϱ),ν)^(0)ϱ + C_((∞,0),ν)^(0)η₀), where k₁^(0,ν) and
    C_(1,0)^♮(ν) use Λ₂^ν;
  - 𝔤_(ϱ,q), and ε_(w,q) with the pointwise min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s));
  - 𝔛^q₁ (no 49), 𝔛^q₂ (2ϖ₂) and 𝔜^q₁ with λ_t^(μ,2) = 2([k₁^(2,μ)]_t + 1);
  - S_(M,q), 𝔯_(M,q) and ε_(M,q);
  - S_(F,s) and 𝔯_(w,s) as in G0f's option (b).
- **Checks** (computed): θ = 0 reproduces G0f's E (a) f exactly at every u\*, since 𝔰_\* binds there. θ = 1 is G0f's
  E (b) with the new S_M.
- **Grid:** θ ∈ {0, ¼, ½, ¾, 1}, refined with {0.375, 0.4375, 0.5625, 0.625, 0.6875, 0.875}; 𝔰_♭ ∈ {1/8, 10⁻², …,
  10⁻¹²}; μ ∈ {10⁻³, …, 10⁻⁶, 3 × 10⁻⁷}.

---

## G0g.0 Headline (computed; P-GRD4 as proved, intrinsic Sobolev constants)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **best f** (G0f E (b)) | **10^−30.2** (−31.1) | **10^−28.5** (−30.0) | **10^−36.9** (−39.8) | **10^−33.4** (−36.0) |
| attained for θ ≥ | 0.375 | 0.5 | 0.625 | 0.75 |
| at the least such θ: ϱ / η₀ | 10^−32.4 / 10^−22.5 | 10^−30.9 / 10^−20.9 | 10^−39.6 / 10^−27.9 | 10^−36.9 / 10^−24.4 |
| μ; 𝔰_♭; 𝔰₁^q | 10⁻⁵; 10⁻⁴; 8.3 × 10⁻⁶ | 10⁻⁴; 10⁻⁴; 1.3 × 10⁻⁶ | 3 × 10⁻⁶; 10⁻⁴; 4.5 × 10⁻⁶ | 10⁻⁵; 10⁻⁴; 1.8 × 10⁻⁶ |
| log₁₀ M_w (S_F; S_M) | 24.8 (23.7; 20.3) | 23.1 (22.1; 19.2) | 30.8 (29.7; 27.0) | 27.4 (26.4; 23.6) |
| what binds (by how much) | closing (𝔰_\* has 0.3 to spare, 0.7 at θ ≥ ½) | closing (0.1 spare, up to 1.3 at θ = 1) | 𝔰_\* < 𝔰₁ by 0.2 (𝔰₁^q at the cap 𝔰_θ) | 𝔰_\* < 𝔰₁ by 0.1 (closing at θ ≥ 0.875, 0.3 spare) |
| pages for f alone | 1,981 | 1,845 | 7,607 | 4,388 |
| **printing: θ minimising pages with ϱ certified** | **θ = 0.375 (or ¼): 4,675** | **θ = 0.4375: 4,271** | **θ = 0.5625: 19,749** | **θ = 0.6875: 11,118** |
| at that θ: f / ϱ | 10^−30.2 / 10^−32.4 | 10^−28.7 / 10^−30.8 | 10^−37.0 / 10^−39.4 | 10^−33.8 / 10^−36.6 |
| G0f's best with ϱ (E (a)) (record) | 5,100 | 4,827 | 23,663 | 13,726 |
| quad-double reach (f ≥ 10⁻³⁵) | to u\* ≈ −1.16 (seed 1) | all of D\* (10^−33.4 at u\* = −1.1) (seed 2) | (per seed, as left) | |
| double-double (f ≥ 10⁻²⁰) | none (best 10^−23.5 at u\* = −9) | none (best 10^−22.8) | | |

**What the fourth sharpening achieves (computed):**
- **The new 𝔠^M removes S_M as the dominant term.**
  - [𝔠^M₁]_t falls from 10^5.0–8.0 (G0f) to 𝔠^Mq₁ = 480–551.
  - S_M now sits 2.7–3.4 decades below S_F.
  - With it, a large 𝔰_♭ (10⁻⁴) is optimal, and 𝔰₁ rises to 10^−5.1…−5.9.
- **f improves on G0f by 0.9, 1.5, 2.9 and 2.6 decades.**
- **Pages for f alone fall** from 2,161 / 2,047 / 9,826 / 5,519 to 1,981 / 1,845 / 7,607 / 4,388.
- **Printed with ϱ certified, pages fall 1.09–1.23 times** below G0f's best (option (a)).
- **What θ does.**
  - θ = 0 (option (a)) keeps 𝔰₁^♮ and loses 2.0–5.3 decades of f.
  - θ = 1 (option (b)) has the best f, but ϱ is 6.0–6.7 decades below f.
  - In between, the closing (D_A) or the 𝔰_θ cap (D\*) is reached at θ ≈ 0.4–0.75 while ϱ stays 2.2–3.5 decades below
    f.
  - The page-optimal θ is 0.375–0.69 in every case.
- **λ_t^(μ,2) is no gain** (computed): [k₁^(2,μ)]_t equals [k₁^(3,μ)]_t to 0.001 decades. Both sit at their unweighted
  floor (6/5)(√3 + 8/3)K_rec, so the coupling of level three contributes nothing to k₁^μ.

## G0g.1 θ, case by case (computed; best over 𝔰_♭ and μ at each θ; f / ϱ, and pages with ϱ at the best Pareto row)

| θ | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| 0 | −32.2 / −33.5; 5,100 | −31.2 / −32.3; 4,827 | −41.2 / −42.1; 23,663 | −38.7 / −39.6; 13,726 |
| 0.25 | −30.6 / −32.4; 4,675 | −29.7 / −31.4; 4,487 | −39.2 / −40.7; 21,568 | −36.8 / −38.4; 12,634 |
| 0.375 | **−30.2 / −32.4; 4,675** | −29.0 / −31.0; 4,342 | −38.2 / −40.1; 20,714 | −35.9 / −37.8; 12,113 |
| 0.4375 | −30.2 / −32.5; 4,712 | **−28.7 / −30.8; 4,271** | −37.7 / −39.9; 20,435 | −35.5 / −37.5; 11,858 |
| 0.5 | −30.2 / −32.7; 4,788 | −28.5 / −30.9; 4,306 | −37.3 / −39.6; 20,021 | −35.1 / −37.2; 11,608 |
| 0.5625 | −30.2 / −32.9; 4,865 | −28.6 / −31.1; 4,378 | **−37.0 / −39.4; 19,749** | −34.7 / −36.9; 11,361 |
| 0.625 | −30.2 / −33.1; 4,942 | −28.6 / −31.4; 4,487 | −36.9 / −39.6; 20,021 | −34.2 / −36.7; 11,199 |
| 0.6875 | −30.2 / −33.4; 5,060 | −28.6 / −31.8; 4,636 | −36.9 / −39.9; 20,435 | **−33.8 / −36.6; 11,118** |
| 0.75 | −30.2 / −33.9; 5,262 | −28.6 / −32.3; 4,827 | −36.9 / −40.3; 20,996 | −33.5 / −36.7; 11,199 |
| 0.875 | −30.2 / −35.3; 5,856 | −28.5 / −33.4; 5,268 | −36.9 / −41.8; 23,202 | −33.4 / −38.0; 12,285 |
| 1 | −30.4 / −36.8; 6,547 | −28.5 / −34.6; 5,781 | −36.9 / −43.4; 25,739 | −33.4 / −39.4; 13,540 |

- **The page minimum is shallow.** Pages stay within 10 % of the minimum for θ ∈ [0.25, 0.6875] on D_A and [0.375, 0.75]
  on D\*.
- **What sets ϱ.** In every optimal row it is the ε_(w,q) budget, the min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s))k₂ term. The ν^(−2)
  smallness term on ϱ never binds. ϱ worsens with θ because 𝔤_(ϱ,q) carries ν^(−1/2).
- **What sets η₀:** the budget 𝔯 ≤ 1/80.
- **Pages for f alone at the best f, for every θ that attains it:** 1,981, 1,845, 7,607 and 4,388.

## G0g.2 What binds, in detail (computed)

**D_A: the closing binds.** The slack in 𝔰_\* < 𝔰₁^q is 0.3 (seed 1, θ = 0.375) to 0.7 (θ ≥ ½), and 0.1 (seed 2, θ = ½)
to 1.3 (θ = 1).
- 𝔰₁^q reaches the cap 𝔰_θ = 2.0 × 10⁻⁵ for θ ≥ ½ (seed 1) and θ ≥ 0.875 (seed 2).
- The A-term C_(∞,μ)^(0)μ^(−2)e^(φ/2) of 𝔰_\* is ≈ S_tot.
- So a lever on S_F improves f by at most that slack (0.7 / 1.3) unless 𝔰_θ is raised too.

**D\*: 𝔰_\* < 𝔰₁ binds**, by 0.2 for seed 1 and 0.1 for seed 2.
- 𝔰₁^q is the cap 𝔰_θ = 4.5 × 10⁻⁶ (seed 1, θ ≥ 0.625), or 1/(4k₃^♮(ν)) with k₃^♮(ν) = 1.4 × 10⁵ (seed 2, θ = ¾).
- With the closing alone, f would be 10^−36.6 and 10^−33.4.

## G0g.3 The remaining levers at level 4, ranked (computed; decades)

**Hypotheticals the writer could not do**, each priced on S_(M,q) at the best rows. The face supremum is replaced by the
R³-weighted face mean, i.e. what a weighted Hölder inequality with the weight inside the integral could give at most;
602 is replaced by 2, as an ℓ² recovery could give at most.

| hypothetical | sup / mean on the face | S_M change | f change |
|---|---|---|---|
| [𝔨₂]_t → face mean | 0.04–0.05 (D_A), 0.33 (D\*) | ≤ 0.3 | **0.0** |
| 𝔪(t) → face mean | 0.18–0.35 (D_A), 0.39–0.50 (D\*) | ≤ 0.5 | **0.0** |
| [2Ω̂²(1 + c/κ′)^(1/2)]_t → face mean | 0.02–0.05 (D_A), 0.12–0.19 (D\*) | ≤ 0.2 | **0.0** |
| all three inside one weighted Hölder (mean of the product) | 0.22–0.45 (D_A), 0.98–0.99 (D\*) | ≤ 0.9 | **0.0** |
| 602 → 2 in 𝔛^q₂ and 𝔛′₂ | — | 0.0 (𝔛^q₁𝔜^q₁ leads 𝔛^q₂𝔜₂ by ≈ 1.5) | **0.0** (η₀ +0.4…+0.8) |

- **None is worth anything in f.** S_M is 2.7–3.4 decades below S_F, so a change to S_M cannot move the closing.
- **The size of these factors is intrinsic, not a supremum effect.** [𝔨₂]_t ≈ 10² is 1/κ over 2Ω̂²; 𝔪 is 𝔴₀⁶R^(3/2) with
  𝔴₀ ≥ 1; [Ω]_t ≈ 10^0.9–1.3.

**Where f now comes from: S_F**, unchanged since G0f. Its items at the new optimum (sb = 10⁻⁴), against the G0b-type
constants, are below. S_F sits 9.1–9.5 decades above the floor's M_w.

| S_F item (pointwise at the sup) | s1 D_A | s2 D_A | s1 D\* | s2 D\* |
|---|---|---|---|---|
| C₁^E against C_S^E (√(258C_(E,3)²/6C_(E,2)²) = 1.12; √𝔨₂ with 1/κ; (k₁^μ + 1)\|∂_γ\|) | 2.95 | 2.96 | 2.84 | 3.05 |
| recovery factor 4k₁^(0,μ) in C_P^♮ | 1.68 | 1.81 | 1.69 | 1.85 |
| word count 7² in 𝔤_(𝒥,s) | 1.69 | 1.69 | 1.69 | 1.69 |
| 𝔠^♮₄(μ) + 1 against 9·2⁴ | 0.98 | 1.22 | 1.15 | 1.38 |
| 𝔣₂ against Ω̂/√c | 0.82 | 0.77 | 0.41 | 0.39 |
| 𝔨_B = max(𝔷, 2) | 0.75 | 0.68 | 0.67 | 0.59 |
| 8√2 against 4√2 | 0.30 | 0.30 | 0.30 | 0.30 |
| C_S^E against G0's C_S | −0.08 | −0.08 | 0.38 | 0.22 |

**The levers ranked by what they can give in f:**
1. **The 𝔰_θ cap** (ϑ = κ = 10⁻²; 𝔰_θ ≈ ϑκc/(√2 + ½)).
   - It binds on D\* now and is within 0.3–1.3 decades on D_A, so it limits every other lever.
   - Raising ϑ and κ needs new rates and a new D^κ; not evaluated.
2. **C₁^E against C_S^E: ≈ 3 decades of S_F.** In f it is capped by item 1 until 𝔰_θ moves. It also lowers the A-term of
   𝔰_\*.
3. **The recovery factor 4k₁^(0,μ): 1.7–1.9.** Same cap.
4. **The word count 7².** At most 1.7 in S_F. In f, measured as an upper bound by dropping it: 0.7, 1.3, 0.0 and 0.3. The
   moved-√7 model of G0f gives 0.6, 0.6, 0.0 and 0.3. Same cap.
5. **𝔠^♮₄(μ) against 9·2⁴: 1.0–1.4. Then 𝔣₂ 0.4–0.8, 𝔨_B 0.6–0.75, and the factor 2, 0.3.**
6. **[𝔨₂]_t, 𝔪(t), [2Ω̂²(1 + c/κ′)^(1/2)]_t and the 602: 0.0 each.** S_M no longer sets the closing; even all three face
   factors together would lower S_M by only 0.2–0.9.

**Distance to the G0b-type floor at level 4 (best proved, computed):**
- f: 9.6, 9.6, 10.7 and 10.5 decades (G0b-type 10^−20.6, −18.9, −26.2, −22.9);
- M_w: 9.4, 9.4, 10.2 and 10.1;
- pages for f alone: ×2.9, ×3.2, ×2.8 and ×3.0 above the floor (674, 571, 2,709, 1,466).

## G0g.4 Reach (computed; D\*'s grid restricted to u ≤ u\*; best f over θ ∈ {0, ¼, ½, ¾, 1}, 𝔰_♭, μ)

| u\* | −9 | −7 | −5 | −3 | −2 | −1.5 | −1.3 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|---|---|
| P-GRD4, seed 1 | −23.5 | −25.5 | −27.0 | −28.6 | −30.2 | −31.5 | −32.9 | −34.0 | −36.9 |
| P-GRD4, seed 2 | −22.8 | −24.6 | −25.7 | −27.1 | −28.5 | −29.6 | −30.7 | −31.5 | −33.4 |
| θ = 0 (= G0f E (a)), seed 1 / 2 | −23.5 / −22.8 | −25.5 / −24.6 | −27.0 / −25.9 | −29.5 / −28.5 | −32.2 / −31.2 | −34.1 / −32.6 | −36.2 / −34.3 | −37.6 / −35.5 | −41.2 / −38.7 |
| G0b-type, seed 1 / 2 | −13.5 / −12.7 | −15.8 / −14.6 | −17.3 / −16.0 | −19.0 / −17.5 | −20.6 / −18.9 | −21.8 / −19.9 | −23.1 / −20.8 | −23.9 / −21.5 | −26.2 / −22.9 |

- **Quad-double** (f ≥ 10⁻³⁵): seed 1 to u\* ≈ −1.16 (G0f −1.24); seed 2 on all of D\* (G0f −1.15).
- **Double-double** (f ≥ 10⁻²⁰): nowhere. The best is 10^−22.8 at u\* = −9; the G0b-type constants reach it to u\* ≈ −2.4
  and −1.5.
- At u\* ≤ −5 the best f equals G0f's to 0.1. The inner domain is set by S_F and 𝔰_\*, which P-GRD4 does not change.

## G0g.5 Pages (computed; S-APP's model via `scratchpad/g0c/pages.py`)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| G0f E (b), f alone (record) | 2,161 | 2,047 | 9,826 | 5,519 |
| **P-GRD4, f alone (best f)** | **1,981** | **1,845** | **7,607** | **4,388** |
| G0f best with ϱ, E (a) (record) | 5,100 | 4,827 | 23,663 | 13,726 |
| **P-GRD4 with ϱ, page-optimal θ** | **4,675 (θ 0.375)** | **4,271 (θ 0.4375)** | **19,749 (θ 0.5625)** | **11,118 (θ 0.6875)** |
| P-GRD4 with ϱ at θ = 1 | 6,547 | 5,781 | 25,739 | 13,540 |
| G0b-type floor, f alone (record) | 674 | 571 | 2,709 | 1,466 |

At the page-optimal θ, certifying ϱ costs ×2.3–2.6 over f alone.

## G0g.6 Caveats

1. **G0c's approximants, growth model and couplings,** as before. k₃^♮(ν) (𝔰₁^q on D\* seed 2) and the cap 𝔰_θ (min c
   over the domain) are the most exposed.
2. **The S_M hypotheticals are not proved.** The face mean is a ceiling on what a weighted Hölder inequality could give,
   not a bound one proves. "602 → 2" is the ceiling of an ℓ² recovery. Both are moot while S_M is 3 decades under S_F.
3. **The page-optimal θ** is searched on the θ grid, with the Pareto rows (f, ϱ) over 𝔰_♭ and μ at each θ.
4. **ε_(w,q)** uses the pointwise min of the two 𝔤's.

## G0g.7 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0g/`)

| file | what |
|---|---|
| `levelQ.py` (= `levelQ_head.py` + `levelQ_mid.py` + `levelQ_tail.py`) | thm:tl5-hf4q with every factor of the Comparison; θ family; intrinsic Sobolev constants; hypotheticals k2, m, Om, all3, 602, nw, pt; S_M face attribution |
| `levelQ_s{1,2}_4_-2.0.json`, `…_-1.1.json`, `run_*.log` | main grids (θ ∈ {0, ¼, ½, ¾, 1}, all hypotheticals) |
| `levelQ_s{1,2}_4_-2.0_thr.json`, `…_-1.1_thr.json`, `thr_*.log` | θ refinement |
| `levelQ_s{1,2}_4_-9.0_…_-1.2.json`, `reach_*.log` | reach sweeps |
| `sumQ.py`, `pagesQ.py` (`pagesQ_cache.json`), `reachQ.py` | tables, Pareto page search, reach |
