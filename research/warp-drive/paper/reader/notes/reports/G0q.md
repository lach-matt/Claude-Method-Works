# G0q: the fourteenth sharpening (P-GRD14, the threshold Y_c and the factor 𝔤₁) on top of P-GRD13, at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0p/` and ran
under `nice -n 19`, at most two at a time. I read nothing under method/, drive/, extracted/ or recovered/. G0p
(`G0p.md`) is the baseline throughout.

**What I evaluated.** P-GRD14 (sec:tl5-hfc, lem:tl5-hfc-cont, lem:tl5-hfc-h, def:tl5-hfc-constants, thm:tl5-hfc), from
the chapter at 203efd5e (`ch87_203efd5e.md`), applied on top of the P-GRD13 code of G0p.

**Implemented:**
- **Lever 1, the threshold Y_c** (lem:tl5-hfc-cont, eq:tl5-hfc-constants).
  - 𝔰_\*'s term with A carries Y_c = 2A_c/(1 + (1 − 4A_cB_c)^½) in place of 2A_c.
  - The code closes with 4AB ≤ 0.1 (margin 10), so at every admissible point Y_c ≤ 2A_c/(1 + 0.9^½). I use that bound,
    which raises 𝔰_\*'s ε-threshold by log₁₀(1 + 0.9^½) = 0.290 everywhere. The exact factor gives at most 0.011 more
    (log₁₀ 2 = 0.301 as 4AB → 0), so this is conservative.
- **Lever 2, the factor 𝔤₁** (lem:tl5-hfc-h, def:tl5-hfc-constants).
  - 𝔤₁ C_S and 𝔤₁ C_(0,0) replace 2C_S and 2C_(0,0) at every site where the factor is that of |H| ≤ 2|h|: the entries
    of C_P^v and C_(P,0)^v, of C_∞^(m), C_(∞,0)^(m) and their forms with μ and ν, and of 𝔎 and 𝔎₀. From these it passes
    into 𝔎^D, S_F, 𝔯 and 𝔰_\*. That is 16 sites with C_S and 7 with C_(0,0), the diagnostics among them.
  - 𝔤₁ = 1 + 2𝔰_♭ is taken at the largest 𝔰_♭ of the grid (1.02 at level 4, 1.0002 at level 6), conservative. At the
    level-4 optima 𝔰_♭ = 10⁻⁴, where the exact 𝔤₁ would be lower by 0.009 decades.
  - Unchanged, as rem:tl5-hfc-what states: the recovery constants (C_S inside 𝔨_rec^p keeps its own constant), the
    factor 2 of 2𝒥_g, the counts and the weights 𝔲.

**Check** (computed): with both levers off (`G0Q_Y=0 G0Q_G1=0`) the code reproduces G0p, 10^−22.01 at seed 1 D_A,
μ = 10⁻⁵.

**Labels:**
- **computed**: floating point, mine;
- **deduced**: an argument or bookkeeping given here;
- **record**: G0p or P-GRD14, cited.

---

## G0q.0 The targets (computed)

| | **seed 1, D_A** | **seed 2, D_A** | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **level 4, P-GRD14** | **10^−21.73** | **10^−20.67** | **10^−28.68** | **10^−25.73** |
| G0p (P-GRD13), main grid | −22.01 | −20.70 | −29.14 | −26.02 |
| **gain** | **+0.27** | **+0.02** | **+0.46** | **+0.29** |
| lever 1 alone (Y_c) | +0.09 | 0.00 | +0.24 | +0.29 |
| lever 2 alone (𝔤₁) | +0.19 | +0.01 | +0.26 | 0.00 |
| writer: lever 1 / lever 2 | +0.075 / ≤ +0.30 | 0 / ≤ +0.30 | +0.154 / ≤ +0.30 | +0.176 / ≤ +0.30 |
| what binds afterwards | **the closing** (𝔰_\* 0.20 spare) | **the closing** (0.28) | **𝔰_\*** (closing 0.07 spare) | **𝔰_\*** (0.01) |
| f / ϱ | −21.73 / −21.59 | −20.67 / −20.63 | −28.68 / −28.47 | −25.73 / −25.29 |
| θ; ϑ₂; μ; 𝔰_♭ | 13/16; 0.03; 10⁻⁵; 10⁻⁴ | ⅞; 0.01; 3 × 10⁻⁵; 10⁻⁴ | 13/16; 0.03; 10⁻⁶; 10⁻² | ⅞; 0.03; 3 × 10⁻⁶; 10⁻⁴ |
| log₁₀ S_F / S_M | 16.00 / 14.91 | 14.97 / 13.78 | 22.40 / 20.52 | 19.52 / 17.66 |
| **level 6, P-GRD14** | **10^−31.72** | **10^−28.53** | **10^−40.25** | **10^−34.53** |
| G0p, main grid | −32.01 | −28.82 | −40.54 | −34.82 |
| **gain** | **+0.29** | **+0.29** | **+0.29** | **+0.29** |
| lever 1 alone / lever 2 alone | +0.29 / 0.00 | +0.29 / 0.00 | +0.29 / 0.00 | +0.29 / 0.00 |
| writer: lever 1 / lever 2 | ≈ +0.30 / ≈ 0 | ≈ +0.30 / ≈ 0 | ≈ +0.30 / ≈ 0 | ≈ +0.30 / ≈ 0 |
| what binds afterwards | ϱ and f together; 𝔰_\* 4.65 below the closing | 3.45 | 5.82 | 4.69 |

**Lever 1 pays min(0.290, the margin by which 𝔰_\* bound), to 0.001 in every case.**
- Level 4: the margins were 0.087 / (the closing bound) / 0.235 / 0.301 (G0p §G0p.1). The gains are 0.087 / 0.000 /
  0.235 / 0.290.
- At seed 1 the closing then binds, with 𝔰_\* 0.20 and 0.06 spare. At seed 2 D\* the whole 0.290 passes, and 𝔰_\* still
  binds by 0.01.
- Level 6: 𝔰_\* binds by 3.7–6.1, so the whole 0.290 passes in all four cases.
- The writer's +0.075 / +0.154 / +0.176 are below the measured gains by 0.01 / 0.08 / 0.11. The code gives 𝔰_\*'s term
  with A a fixed half of 𝔰₁^v, so the factor on that term passes into ε whole until the closing binds.

**Lever 2 pays where 2C_S held the supremum of C_P^v, and stops where 𝔨_rec^p takes over.**
- Level 4: +0.19 / +0.01 / +0.26 / 0.00, the same as G0p's hypothetical C_S ÷ 2 (+0.19 / +0.01 / +0.27 / 0.00).
- At seed 2 it pays nothing, as G0p found, because 𝔨_rec^p already held the supremum.
- Level 6: 0.00 in all four cases. The family term k₁𝔐_p leads C_P^v at every point there, 0.49–1.09 above sup 2C_S
  even before the lever. (G0p's C_S ÷ 2 paid +0.02 to +0.22 at level 6 because it also halves the C_S inside 𝔐_p, which
  lem:tl5-hfc-h leaves alone.)

**Together they nearly add:** 0.27 / 0.02 / 0.46 / 0.29 against the sums 0.28 / 0.01 / 0.50 / 0.29. Rule cost against
G0p, (decades ratio)^4.5: 0.95 / 0.99 / 0.93 / 0.95 at level 4, 0.96 / 0.96 / 0.97 / 0.96 at level 6.

## G0q.1 What binds, which entry leads C_P^v, and the closing at seed 2 D_A (computed)

**What binds at level 4:** the closing at seed 1 D_A (0.20 below 𝔰_\*) and seed 2 D_A (0.28); 𝔰_\* at seed 1 D\* (0.07)
and seed 2 D\* (0.01). f binds in all four; ϱ is 0.04–0.44 above it. At level 6, ϱ and f balance through the share of ε,
and the closing is 3.4–5.8 decades away.

**C_P^v is now led at its supremum by 𝔨_rec^p in all four level-4 cases** (§G0q.2 gives the table). 𝔤₁C_S still leads
most points (51–86 %), but 𝔨_rec^p holds the supremum, 0.10–0.52 above sup 𝔤₁C_S. C₁ leads no point. At level 6 the
third entry of C_P^v (k₁ 𝔐_p, the family term) leads every point, 0.79–1.39 above sup 𝔤₁C_S, which is why lever 2
does nothing there.

**At seed 2 D_A the closing is led by the products of S_F.**
- S_F splits into its linear part f₀C_P^v + f₁C_P^v and its products f₂𝔎^D, each formed to its own supremum and
  integrated as S_F is. log₁₀ 10.60 against 14.97: the products lead by 4.4 decades. The same holds in all eight cases,
  by 4.2–6.8 decades.
- Inside 𝔎 = max(𝔤₁C_S 𝔨_A, C_P^v 𝔨_B), the entry C_P^v 𝔨_B leads at every point (the share where 𝔤₁C_S 𝔨_A leads is 0).
- So the closing at seed 2 D_A runs on C_P^v through 𝔎^D. Its supremum is 𝔨_rec^p's, 0.40 above 𝔤₁C_S, and that is why
  lever 2 moved S_F there by only 0.03 (15.00 → 14.97).
- The lever for seed 2 D_A's closing is 𝔨_rec^p, and within it the term 𝔨_♯K_rec C₁^Γ (§G0q.2).

## G0q.2 The three additions for round 15 (computed, except where marked deduced)

**1. Which entry leads sup C_P^v on the P-GRD14 optimum** (level 4, the optimal μ, x = 𝔵_D = 0.05, face points, 𝔶 = 1
basis; in the form of G0p §G0p.1):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| share of points led by 𝔤₁C_S / C₁ / 𝔨_rec^p | 86 % / 0 / **14 %** | 51 % / 0 / **49 %** | 81 % / 0 / **19 %** | 57 % / 0 / **43 %** |
| log₁₀ sup C_P^v / sup 𝔤₁C_S | +0.120 | +0.424 | +0.207 | +0.538 |
| **log₁₀ sup 𝔨_rec^p / sup 𝔤₁C_S** | **+0.098** | **+0.402** | **+0.185** | **+0.515** |
| log₁₀ sup C₁ / sup 𝔤₁C_S | −0.39 | −0.09 | −0.43 | −0.06 |

- **𝔨_rec^p leads sup C_P^v in all four cases.** At seed 1 its lead is 0.10 / 0.19 decades, at seed 2 0.40 / 0.52.
- 𝔤₁C_S still leads most points. C₁ leads none.
- At level 6 the entry k₁𝔐_p leads every point (sup C_P^v / sup 𝔤₁C_S = +0.79 / +1.20 / +1.01 / +1.39).

**2. K_rec at the point holding sup 𝔨_rec^p.**
- The code forms K_rec pointwise as max(|T|⁻¹, λ_M^(−½)): the operator norm of the block map, T on one side and the six
  K_ab on the other. λ_M is the smallest eigenvalue of M = Σ_ab v_ab v_abᵀ, where v_ab are the spatial frame components
  of K_ab, so λ_M^(−½) is the norm of the least-squares recovery through the c^ab.

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| \|T\|⁻¹ | 1.098 | 1.088 | 1.578 | 1.371 |
| λ_M^(−½) | 0.380 | 0.399 | 0.866 | 0.757 |
| K_rec (which part) | 1.098 (T) | 1.088 (T) | 1.578 (T) | 1.371 (T) |
| K_rec²: the T part / the rotation part | 1.205 / 0.144 | 1.185 / 0.160 | 2.489 / 0.750 | 1.879 / 0.573 |
| share of 𝔨_rec^p there from 𝔨_♯K_rec C₁^Γ (rest: 𝔷₁ term; 𝔷₂ and 𝔯_♯ ≤ 0.1 %) | 95.8 % | 94.2 % | 98.6 % | 98.0 % |
| over all face points: T part leads; log₁₀(\|T\|⁻¹/λ_M^(−½)) median (range) | 100 %; +0.83 (+0.40 … +1.07) | 100 %; +0.83 (+0.40 … +1.07) | 100 %; +0.46 (+0.07 … +1.07) | 100 %; +0.47 (+0.23 … +1.07) |

K_rec² is a maximum here, not a sum, so its "split" is the two candidates; the T part is the larger at every point.
𝔨_♯ = 2.236 (√5).

**The code does not carry the per-word split.** C₁^Γ enters as the family face constant C₁^(U,l) of the seven fields,
with the family counted through the word count (√(43·7) in the absorption terms), not as seven separate per-field
constants. So the question cannot be settled from these runs. What can be given is a bracket (deduced from the figures
above):

- A weighted family bound (|T|⁻²C_T² + λ_M⁻¹ Σ_ab C_ab²)^½, against K_rec (Σ_Z C_Z²)^½, lies between λ_M^(−½)/|T|⁻¹
  (T carrying none of the family norm) and 1 (T carrying all of it).
- With the seven fields sharing the family norm equally it is ((|T|⁻² + 6λ_M⁻¹)/7)^½/K_rec.

| at the sup point | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| equal shares | 0.495 (−0.31) | 0.508 (−0.29) | 0.633 (−0.20) | 0.636 (−0.20) |
| floor (T carries none) | 0.346 (−0.46) | 0.367 (−0.44) | 0.549 (−0.26) | 0.552 (−0.26) |
| on 𝔨_rec^p, equal shares / floor | −0.29 / −0.43 | −0.27 / −0.39 | −0.19 / −0.26 | −0.19 / −0.25 |

- **In D_A it could fall well below K_rec × the family norm, by 0.3–0.45 decades.** That is more than the ÷ 2 priced in
  item 3. In D\* it could fall by 0.2–0.26.
- The bracket is pointwise at the sup point. In D\* the two parts come within +0.07 to +0.23 decades of each other at some
  points, so the supremum of the weighted bound may move to where the reduction is smaller.
- Whether the bracket is reached depends on how much of C₁^Γ the field T carries, which this code does not measure.

**3. Prices on the P-GRD14 optimum** (hypothetical scalings, not proved; against G0q's level-4 targets):

| lever | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **𝔨_rec^p's C₁ term (𝔨_♯K_rec C₁^Γ) ÷ 2 alone** | **+0.09** | **+0.24** | **+0.06** | **+0.29** |
| C_S ÷ 2 alone | 0.00 | 0.00 | +0.16 | 0.00 |
| both together | +0.26 | +0.25 | +0.30 | +0.29 |
| (C₁ ÷ 2 everywhere, for comparison) | +0.09 | +0.25 | +0.06 | +0.30 |
| level 6: ε's coefficient of ϱ × 0.1 | +0.90 | +0.61 | +0.81 | +0.40 |

- **The C₁ term of 𝔨_rec^p is now the level-4 lever at seed 2** (+0.24, +0.29). It is the only lever that moves seed 2
  D_A's closing (S_F 14.97 → 14.72).
- C₁ ÷ 2 everywhere is worth what the 𝔨_rec^p term alone is worth, to 0.01: C₁ acts only through 𝔨_rec^p.
- At seed 1 the C₁ term pays +0.09 and +0.06, because 𝔤₁C_S takes the supremum back after 0.10 and 0.19 decades. C_S ÷ 2
  alone pays only where 𝔤₁C_S was close (seed 1 D\*, +0.16); elsewhere 𝔨_rec^p holds the supremum.
- **Together they give +0.25 to +0.30 in every case.** At seed 1 each frees the other: +0.26 and +0.30, against +0.09 /
  +0.06 (C₁ term) and 0.00 / +0.16 (C_S) alone. At seed 2 the C₁ term alone gives nearly all of it.
- At level 6 neither C_S nor 𝔨_rec^p's term enters C_P^v's lead. The ϱ coefficient is still worth +0.4 to +0.9, as in
  G0p.

## G0q.3 Caveats

- Lever 1 is taken with the bound 4A_cB_c ≤ 0.1 of the code's closing, not with the exact 4A_cB_c at each point: up to
  0.011 decades are left on the table where 𝔰_\* binds.
- 𝔤₁ is taken at the largest 𝔰_♭ of the grid (conservative by ≤ 0.009 decades at level 4).
- The prices in §G0q.2 are scalings of one term each, not proved bounds.
- The scheduler that ran G0q reached its two-hour limit during the last two jobs (seed 1 and 2 D\*, C₁ term and C_S
  both ÷ 2). They were run again on their own, at nice 19, two at a time.

## G0q.4 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0p/`)

- `ch87_203efd5e.md`: the chapter at 203efd5e, sec:tl5-hfc as read.
- `patchQ.py` builds `levelQ_tail.py` from G0p's `levelL_tail.py`. `levelQ.py` = `g0l/levelZ_head.py` + `levelL_mid.py`
  + `levelQ_tail.py`.
- Switches: `G0Q_Y` (lever 1), `G0Q_G1` (lever 2), `G0Q_KRC1` (the C₁ term of 𝔨_rec^p, scaled); with G0p's `G0P_CSS`
  and `G0I_C1S`.
- `runQ.sh SEED N U* VARIANT` runs one case at nice 19. Variants: `v0`, `main`, `qy`, `qg`, `qcsh`, `qc1h`, `qd` (main
  with the sup-point diagnostic), `qkr`, `qkcs`.
- `schedQ.sh` with `jobsQ.txt` runs them two at a time.
- `ruleQ.py TAG [REFTAG]` prints the tables (with the S_F split); `q15.py [TAG]` prints §G0q.2's items 1 and 2.
- Records `levelV_s<seed>_<N>_<u*>_q*.json`, logs `q_*.log`.
