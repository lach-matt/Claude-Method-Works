# G0j: the seventh sharpening (P-GRD7, C₁^x) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0j/` with
absolute paths. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD7 (sec:tl5-hfx).
- **Versions:** the draft at 3d367b13 (md5 3f06af92), the reader's corrections at 12ca1ed3, and the confirmed text at
  7789e2ec, merged at 2500bc7f.
- **The reader's corrections:**
  - C₁^x := min(C₁^♮, new number);
  - C₁^x enters level 6 through C_P^v = C_(∞,μ)^(1) and C_(∞,μ)^(2).
  - The last change, in the wording of the ϱ part, changes no factor here: the old C_(1,ϱ) is still used.
- **The new factor:** C₁^x² = 6C_(E,3)² 𝔴₀⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 4|∂_γ|² (2√43(k₁^μ + 1) +
  (2ϖ′)^(1/2))²), with ϖ′ = 6(2μΛ₁)² + 36(4μΛ₁ + 2μ^(3/2)Λ₂)².
- **Where it goes:** in place of C₁^♮ everywhere, at both levels: 𝔎, 𝔨_rec of C_P^v, C_(∞,μ)^(N−4) in 𝔰_\*^w, and the
  level-4 constants. The closing condition is thm:tl5-hfw's.

**Method: as in G0i** (`levelX.py` = G0i's `levelW` with C₁^x).
- Every parameter is chosen to maximise min(f, ϱ): θ, ϑ₁, ϑ₂, 𝔯, μ, 𝔰_♭ and the share of ε given to f.
- **The face constants for C₁^x** use the face choice of C₁^♮ (admissible), with the C₁^x weight inside the face supremum.
- **The min is not needed in practice.** The new number is below C₁^♮ at every grid point: Λ₂^μ/(k₁^μ + 1) ≤ 7 × 10⁻⁴,
  far outside the reader's interval (0.134, 2.82).

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0j/` (§G0j.4);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0i or P-GRD7, cited.

---

## G0j.0 Level 4 (computed)

| | **seed 1, D_A** | seed 2, D_A | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD7** | **10^−29.0** | **10^−27.3** | **10^−35.75** | **10^−32.6** |
| G0i (P-GRD6) | −29.16 | −27.46 | −35.90 | −32.72 |
| gain | +0.15 | +0.15 | +0.15 | +0.15 |
| f / ϱ | −29.0 / −29.0 | −27.3 / −26.8 | −35.75 / −35.6 | −32.6 / −32.1 |
| η₀ | −22.9 | −21.2 | −28.3 | −24.7 |
| θ | 0.375 | 0.625 | ¾ | ¾ |
| ϑ₁ / ϑ₂ | 0.0019 / 0.01 | 0.001 / 0.003 | 0.0013 / 0.03 | 0.001 / 0.01 |
| 𝔯 | 0.01 | 0.01 | 0.01 | 0.01 |
| μ | 10⁻⁵ | 10⁻⁴ | 3 × 10⁻⁶ | 10⁻⁵ |
| 𝔰_♭ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ |
| share of ε given to f | 0.99 | 0.9 | 0.7 | 0.9 |
| **C₁^x / C₁^♮** (max over the domain; median) | **10^−0.15; 10^−0.15** | 10^−0.15; 10^−0.15 | 10^−0.16; 10^−0.15 | 10^−0.15; 10^−0.15 |
| what binds | **f** (the closing and 𝔰_\* together) | **f** (closing; 𝔰_\* 0.4 spare) | **f** (closing and 𝔰_\* together) | **f** (𝔰_\* by 0.4) |
| rule cost against G0i | ×0.98 | ×0.98 | ×0.98 | ×0.98 |

**What P-GRD7 does on these backgrounds:**
- **C₁^x is C₁^♮ divided by √2, i.e. 0.15 decades.** The k₁ part is the whole of the bracket at the C₁ supremum (share
  1.000). ϖ′ is 10^−13…10^−6 there and at most 3 × 10⁻³ anywhere.
  - So of the writer's two gains, only the halved k₁ coefficient (4 · 43 · 4 against 4 · 43 · 8) acts.
  - The other gain, 43(1 + 6Λ₂^μ)² → (1 + ϖ′^(1/2))², multiplies a term that was already negligible.
- **min(f, ϱ) rises by exactly 0.15** in every case. That confirms G0i's measured rate of about one decade of the
  stricter quantity per decade of C₁.
- **The optimal parameters do not move.** f binds, as in G0i, and further ϱ levers are worth 0.0–0.3 (computed with the
  ϱ coefficient × 0.1: 0.00, 0.04, 0.11, 0.28).

## G0j.1 What is left of the C₁^E–C_S^E gap, and what dominates it (computed)

C₁^x/C_S^E is 10^2.85–2.91 at level 4, against 10^3.00–3.06 for C₁^♮.

**The anatomy of C₁^x at its supremum** (pointwise, log₁₀):

| factor | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| the k₁ part, (4|∂_γ|² · 4 · 43 (k₁^μ + 1)²)^(1/2) | **2.09** | **2.19** | **2.09** | **2.09** |
| — of which √43 (the word count kept with k₁) | 0.82 | 0.82 | 0.82 | 0.82 |
| — of which (k₁^μ + 1), with k₁^μ = 5.5–7.2 | 0.81 | 0.91 | 0.81 | 0.81 |
| — of which 2 · 2 (the factors 4|∂_γ|²·4 under the root) | 0.60 | 0.60 | 0.60 | 0.60 |
| — of which |∂_γ| = 0.72 | −0.14 | −0.14 | −0.14 | −0.14 |
| ϖ′ terms | 0.00 | 0.00 | 0.00 | 0.00 |
| √𝔨₂ (𝔨₂ = 10^2.57–2.72) | **1.30** | **1.28** | **1.36** | **1.36** |
| — share of 1/z̲ in 𝔨₂'s numerator; of 1/κ′ | 0.75; 0.25 | 0.73; 0.27 | 0.81; 0.19 | 0.81; 0.19 |
| rank-3 against rank-2 constant, (C_(E,3)²/C_(E,2)²)^(1/2) | 0.30 | 0.30 | 0.30 | 0.30 |

C_S^E's own bracket ((1 + 8|D̂∂_γ|²)/(2Ω̂²z̲) + 2𝔨₁, which also carries 1/z̲) and the face factors take back 0.8–0.9
decades. That leaves the 2.85–2.91.

**What dominates the remaining gap:**
1. **The k₁ part, 2.1–2.2 decades.**
   - √43, the count kept because the second derivatives are bounded through their maximum: 0.82.
   - The recovery constant k₁^μ + 1: 0.81–0.91, near its unweighted floor (6/5)(√3 + 8/3)K_rec.
2. **√𝔨₂, 1.3–1.4 decades.** At the supremum 1/z̲ makes three quarters of 𝔨₂ and 1/κ′ one quarter. Without 1/z̲,
   C₁ would fall 0.28–0.36 decades; without the 1/κ′ part, 0.06–0.10.
3. **The rank-3 constant: 0.30.**
4. **ϖ′: nothing.**

## G0j.2 The levers re-ranked for min(f, ϱ) at level 4 (computed where marked; decades)

| lever (hypothetical, not proved) | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* | how priced |
|---|---|---|---|---|---|
| **the count 43 with k₁ removed** (an ℓ² recovery; C₁^x ÷ √43) | **+0.82** | **+0.81** | **+0.81** | **+0.82** | computed |
| **the recovery constant, (k₁^μ + 1) → 1** | ≈ +0.8 | ≈ +0.9 | ≈ +0.8 | ≈ +0.8 | at the measured rate of 1:1 |
| the word count 7² in S_F | +0.68 | +0.59 | 0.00 | +0.22 | computed; capped by 𝔰_\* |
| 𝔠^♮_j(μ) → 9·2^j in 𝔤_(𝒥,s) | +0.68 | +0.59 | 0.00 | +0.07 | computed; capped by 𝔰_\* |
| 1/z̲ out of 𝔨₂ (in C₁) | ≈ +0.3 | ≈ +0.3 | ≈ +0.35 | ≈ +0.35 | at the measured rate (C₁ −0.28…−0.36); z̲ also changes the rates, not computed |
| the rank-3 constant (rank 2 in its place) | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | ≈ +0.3 | at the measured rate |
| 1/κ′ out of 𝔨₂ (larger κ) | ≤ +0.1 | ≤ +0.1 | ≤ +0.1 | ≤ +0.1 | at the measured rate; G0h's κ estimate ≤ 0.3 |
| a further ϱ lever (coefficient × 0.1) | 0.00 | 0.04 | 0.11 | 0.28 | computed |
| ϖ′ | 0.0 | 0.0 | 0.0 | 0.0 | — |

**Reading the table:**
- **The C₁ parts lead**, in particular the count √43 with k₁ (computed +0.8) and k₁^μ + 1 itself (≈ +0.8). Each acts on
  both conditions that bind f: S_F through 𝔎, and the A-term of 𝔰_\* through C_P^v.
- **Together the C₁ parts are worth about 2.5–2.9 decades** (G0i's C₁ ÷ 10³: +2.5…+2.9). After that the closing's other
  factors and the cap 𝔰_(θ,v) bind.
- **The word count and 𝔠^♮₄(μ) act on S_F only.** They are capped by the 𝔰_\* slack (≤ 0.7 on D_A, ≤ 0.2 on D\*).

## G0j.3 Level 6, briefly (computed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD7** | **−41.5** | **−37.65** | **−50.3** | **−43.8** |
| G0i | −41.65 | −37.81 | −50.47 | −43.95 |
| gain | +0.15 | +0.16 | +0.15 | +0.15 |
| f / ϱ | −41.1 / −41.5 | −37.2 / −37.65 | −49.75 / −50.3 | −43.0 / −43.8 |
| C₁^x / C₁^♮ | 10^−0.15 | 10^−0.15 | 10^−0.15 | 10^−0.15 |
| what binds | **ϱ** (ε budget); 𝔰_\* binds f by 5.2 | ϱ; 𝔰_\* by 3.5 | ϱ; 𝔰_\* by 6.0 | ϱ; 𝔰_\* by 4.9 |

**At level 6 the same 0.15 passes through C_P^v and C_(∞,μ).**
- ϱ still binds through the ε budget, at option (b) with 𝔰_♭ = 10⁻⁶.
- The ϱ coefficient remains the first lever there: × 0.1 gives +1.0 (computed). The room is about 3.0–4.8 decades up to
  the best f.

## G0j.4 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0j/`)

| file | what |
|---|---|
| `levelX.py` (`levelX_head.py` + `levelX_mid.py` + `levelX_tail.py`) | thm:tl5-hfx: C₁^x in place of C₁^♮ (`G0J_X=1`), with the face sup of its own weight; the pointwise anatomy of C₁^x (`xatt`); P-GRD6's ε^w; max-min search; hypotheticals (nw, c9, `G0I_C1S`) |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_x.json`, `x_*.log` | P-GRD7 max-min, levels 4 and 6 |
| `levelV_s{1,2}_4_*_x43.json`, `x43_*.log` | hypothetical: the count 43 with k₁ removed |
| `ruleX.py` | tables |
| `G0j.md` | copy of this report |
