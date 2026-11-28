# G0k: the eighth sharpening (P-GRD8, absorption at the bootstrap's smallness) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0k/`, through a
job script with absolute paths. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD8 (sec:tl5-hfy).
- **Versions:** the draft at c0543b1e, and the confirmed text at bcf07954 with the review's corrections, merged at
  7b592452.
- **The new number:** 𝔵 := 𝔰₁^v sup k₃ ≤ 1/4. k₃ is the absorption constant of the set in use: k₃^♮(ν) at level 4,
  k₃^♮(μ) under option (b), k₃^♮ under (a). 𝔵 is computed row by row as 𝔰₁^v · sup k₃.

**Replacements implemented,** including every place the review added:
- **2(k₁ + 1) → (k₁ + 2𝔵)/(1 − 𝔵)** in 𝔨_A, λ_t^μ, λ_t^(μ,2) and the M_g bounds. In C₁^x the term 2√43(k₁^μ + 1)
  becomes √43(k₁^μ + 2𝔵)/(1 − 𝔵).
- **2k₂ → k₂/(1 − 𝔵)** in:
  - C_(1,ϱ), whose 32k₂² becomes 8(k₂/(1 − 𝔵))²;
  - ς_t, and through it 𝔯_M and ε_M;
  - the products' ϱ terms, so ε^w's coefficient 2𝔰₁^v becomes 𝔰₁^v/(1 − 𝔵).
- **The factor 2 before the maxima → 1/(1 − 𝔵)** in C_P^v, C_(P,ϱ)^v, C_(P,0)^v, C_(∞,μ), C_((∞,ϱ),ν), C_((∞,0),ν),
  and at level 6 also the unweighted forms.

**The confirming reader's remark** (C₁^♮'s entry with the replaced recovery 8((k₁^μ + 2𝔵)/(1 − 𝔵))²) changes nothing.
Both entries of C₁^x are dominated by their k₁ term, and C₁^♮'s remains √8 times the new number, so the min is the new
number everywhere.

**Method: as in G0i and G0j.**
- Every parameter maximises min(f, ϱ): θ, ϑ₁, ϑ₂, 𝔯, μ, 𝔰_♭ and the ε share.
- The 𝔵-dependent constants are formed on 𝔵 ∈ {0, 10⁻³, 3 × 10⁻³, 0.01, 0.03, 0.1, ¼}. Each row uses the smallest level
  ≥ its 𝔵, which is conservative by at most 0.06 decades (seed 2 D\*, 𝔵 = 0.147 on the ¼ level; elsewhere ≤ 0.02).
- **Check** (computed): the same code with every 1/(1 − 𝔵) set to 2 (𝔵 = ½ formally) reproduces G0j exactly (10^−29.01 at
  seed 1 D_A).

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0k/` (§G0k.4);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0j or P-GRD8, cited.

---

## G0k.0 Level 4 (computed)

| | **seed 1, D_A** | seed 2, D_A | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD8** | **10^−28.5** | **10^−26.9** | **10^−35.3** | **10^−32.1** |
| G0j (P-GRD7) | −29.01 | −27.31 | −35.75 | −32.57 |
| gain | +0.51 | +0.43 | +0.41 | +0.50 |
| f / ϱ | −28.5 / −28.3 | −26.9 / −26.5 | −35.3 / −35.0 | −32.1 / −32.1 |
| η₀ | −22.6 | −21.0 | −28.0 | −24.6 |
| **𝔵 at the optimum** | **0.073** | **0.099** | **0.086** | **0.147** |
| 𝔰₁^v (what sets it) | 2.0 × 10⁻⁵ (the cap) | 5.9 × 10⁻⁶ (the cap) | 1.4 × 10⁻⁵ (the cap) | 4.5 × 10⁻⁶ (the cap) |
| θ | 0.625 | ¾ | ¾ | 0.875 |
| ϑ₁ / ϑ₂ | 0.0019 / 0.01 | 0.001 / 0.003 | 0.0013 / 0.03 | 0.001 / 0.01 |
| 𝔯 | 0.01 | 0.01 | 0.01 | 0.01 |
| μ | 10⁻⁵ | 10⁻⁴ | 10⁻⁶ | 10⁻⁵ |
| 𝔰_♭ | 10⁻⁴ | 10⁻⁴ | 10⁻² | 10⁻⁴ |
| share of ε given to f | 0.9 | 0.7 | 0.7 | 0.5 |
| what binds | **f** (closing; 𝔰_\* 0.4 spare) | **f** (closing; 0.5 spare) | **f** (𝔰_\* and the closing) | **f** (𝔰_\* by 0.1) |
| rule cost against G0j, (decades ratio)^4.5 | 0.92 | 0.93 | 0.95 | 0.93 |

**What P-GRD8 does on these backgrounds:**
- **The optimum moves to larger θ (0.625–0.875).** There 𝔰₁^v is set by the cap 𝔰_(θ,v) rather than by 1/(4k₃^♮(ν)), so
  𝔵 stays below ¼, at 0.07–0.15.
- **The gain is about 0.4–0.5 decades.** Each replaced factor 2 gains log₁₀(2(1 − 𝔵)) ≈ 0.24–0.27 at these 𝔵. Two such
  factors act on the binding constant C_P^v: its outer 2, and the recovery 2(k₁ + 1) → (k₁ + 2𝔵)/(1 − 𝔵) inside C₁^x,
  worth ≈ 0.3. Choosing a larger θ to keep 𝔵 small costs a little.
- **f binds in all four cases, as in G0j.** A further ϱ lever is worth 0.04–0.26 (computed with the coefficient × 0.1).

## G0k.1 The levers re-ranked for min(f, ϱ) at level 4 (computed where marked; hypothetical, not proved)

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **ℓ² recovery over the words** (the √43 with k₁ removed, with the nonlinear terms carrying 𝔵 per word) | **+0.78** | **+0.76** | **+0.74** | **+0.73** | computed (see below) |
| the recovery constant itself, k₁^μ → 0 in (k₁ + 2𝔵)/(1 − 𝔵) | ≈ +0.8 | ≈ +0.9 | ≈ +0.8 | ≈ +0.8 | at the 1:1 rate of G0i and G0j |
| word count 7² in S_F | +0.55 | +0.60 | 0.00 | +0.22 | computed; capped by 𝔰_\* |
| 𝔠^♮_j(μ) → 9·2^j | +0.55 | +0.59 | 0.00 | 0.00 | computed; capped by 𝔰_\* |
| **the optimised split (x + y)² ≤ (1 + δ)x² + (1 + 1/δ)y²**, δ = 0.01 | +0.15 | +0.15 | +0.15 | +0.15 | computed (see below) |
| 1/z̲ out of 𝔨₂ (in C₁) | ≈ +0.3 | ≈ +0.3 | ≈ +0.35 | ≈ +0.35 | at the 1:1 rate (G0j); z̲ also changes the rates |
| the rank-3 constant | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | at the 1:1 rate |
| a further ϱ lever (× 0.1) | +0.04 | +0.11 | +0.12 | +0.26 | computed |
| 1/κ′ part of 𝔨₂ | ≤ +0.1 | ≤ +0.1 | ≤ +0.1 | ≤ +0.1 | G0j |

**The ℓ² recovery, as priced.**
- **The bound.** Summed in ℓ² over the 43 words, the bound of the second derivatives reads ‖M‖ ≤ (k₁^ℓ² + 2√43𝔵)𝒥/(1 −
  𝔵) + …, with the nonlinear terms carrying 𝔵 per word. So C₁^x's term √43(k₁^μ + 2𝔵)/(1 − 𝔵) becomes (k₁^μ + 2√43𝔵)/(1 −
  𝔵).
- **The assumption.** I took the ℓ² (Schur) norm of the coupling family to equal its row norm, i.e. k₁^ℓ² = k₁^μ. That is
  optimistic: P-GRD8's Comparison says that bound is not written.
- **The worth: +0.73–0.78 decades** at these 𝔵. It is a little less than the full √43 (0.82), because 2√43𝔵 is not small
  at 𝔵 ≈ 0.1. It would need 𝔵 ≪ 0.1 to reach 0.8, and the optimum does not choose that.

**The optimised split, as priced.**
- **Where it acts.** Wherever a bound is split as (x + y)² ≤ 2x² + 2y² between the part with 𝒥_g and the part with ϱ, the
  choice δ = 0.01 gives (1 + δ) to the 𝒥_g part and (1 + 1/δ) to the ϱ part. In C₁ that is C₁ ÷ √2 and C_(1,ϱ) ×
  √((1 + 1/δ)/2) = × 7.1.
- **The worth: +0.15 per such split.** ϱ has room at level 4 to pay for it.
- **One split was priced:** the one in C₁, whose ϱ part is C_(1,ϱ). A split elsewhere (C_S, C_(0,0) against η₀) would add
  at most 0.15 more, and only where that constant leads.

**Ranking at level 4:**
1. the ℓ² recovery: about 0.75, conditional on a Schur bound of the couplings;
2. the recovery constant: about 0.8;
3. the word count and 𝔠^♮₄: ≤ 0.6, capped by 𝔰_\*;
4. z̲ and the rank-3 constant: about 0.3 each;
5. the δ split: 0.15;
6. κ and ϱ levers: ≤ 0.3.

The C₁ parts together remain worth about 2.5 decades (G0i's C₁ ÷ 10³), since C₁ still sits about 2.6 decades above C_S.

## G0k.2 Level 6, briefly (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD8** | **−40.55** | **−36.75** | **−49.4** | **−43.0** |
| G0j | −41.50 | −37.65 | −50.32 | −43.80 |
| gain | +0.95 | +0.90 | +0.95 | +0.79 |
| f / ϱ | −40.5 / −40.55 | −36.55 / −36.75 | −49.1 / −49.4 | −42.5 / −43.0 |
| 𝔵 | 0.003 | 0.015 | 0.007 | 0.066 |
| option; 𝔰_♭; 𝔰₁^v | (b); 10⁻⁶; 5 × 10⁻⁷ | (b); 10⁻⁶; 5 × 10⁻⁷ | (b); 10⁻⁶; 5 × 10⁻⁷ | (b); 10⁻⁶; 5 × 10⁻⁷ |
| what binds | **ϱ** (ε budget); 𝔰_\* binds f by 5.2 | ϱ; by 3.5 | ϱ; by 6.0 | ϱ; by 4.9 |

**At level 6, 𝔵 is small** (0.003–0.07). The optimum takes 𝔰_♭ = 10⁻⁶, so 𝔰₁^v = 𝔰_♭/2 = 5 × 10⁻⁷. Each factor 2 then
gains nearly the full 0.3: ε^w's coefficient (ϱ binds, about 0.3), and C_P^v and C₁^x through the A-term and S_F. That
gives 0.8–0.95 in all.

The review's warning that 𝔵 can be ¼ applies at G0h's f-optimal level-6 points, where 𝔰₁^v = 1/(4k₃). At the max-min
points it does not, because of the small 𝔰_♭.

ϱ still binds at level 6, and the ϱ coefficient remains the first lever there (× 0.1 gives +1.0, computed).

## G0k.3 Caveats

1. **G0c's approximants, growth model and couplings,** as before. 𝔵 depends on k₃ and on the cap, so the growth model
   enters every replaced factor.
2. **The 𝔵 grid** rounds up (conservative, ≤ 0.06 decades).
3. **The ℓ² recovery and the δ split are hypothetical.** The first assumes a Schur bound of the couplings equal to their
   row norm.

## G0k.4 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0k/`)

| file | what |
|---|---|
| `levelY.py` (`levelY_head.py` + `levelY_mid.py` + `levelY_tail.py`, body in `body.py`) | thm:tl5-hfy: every replacement of lem:tl5-hfy-abs (with the review's additions), 𝔵 per row on a grid of levels, C₁^x per 𝔵 level through the face supremum; P-GRD6/7 as before; `G0K_XFIX=0.5` reproduces G0j; `G0K_L2=1` the ℓ² recovery; `G0I_C1S`/`G0K_C1RS` the δ split |
| `runjob.sh`, `jobs.txt` | the job list, launched with xargs from the scratchpad |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_y.json`, `y_*_main.log` | P-GRD8 max-min |
| `levelV_s{1,2}_4_*_yl2.json`, `levelV_s{1,2}_4_*_ydsp.json` | hypotheticals |
| `levelV_s1_4_-2.0_val*.json` | the G0j reproduction check |
| `ruleY.py` | tables |
| `G0k.md` | copy of this report |
