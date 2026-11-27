# S-RULE: the approximant of each seed defined by an exactly specified rule (design brief)

Report only. I edited no repository file and committed nothing. I read nothing under method/, drive/, extracted/ or
recovered/. I did not touch the other agent's runs under scratchpad/bsolv/; every pilot of mine ran under `nice -n 19`
on one core, one at a time, and wrote only to `scratchpad/srule/` (§11).

**Scope.** The brief asked first whether a rule could replace the tables. Mid-task the author decided it
(notes/DECISIONS.md, 2026-11-27, commit 01d42cba): no printed tables; each seed's approximant is defined in the paper by
its rule. This report is therefore the design brief for that rule (§§1–7), with the candidates and the evidence that
chose it (§2). The reductions that would keep printed tables are only a fallback (§9).

**Labels.** Every figure is one of:
- **computed**: mine, here, by the scripts in §11;
- **deduced**: an argument or a scaling I give;
- **record**: cited from a report (G0g, G0f, B-SOLV, S-APP) or from the solver's validation files.

---

## 0. Recommendation in one table

**The rule.** Plain Picard iteration of the solver's own collocation map, cell by cell, in fixed-point integer arithmetic
with 320 fractional bits and one stated rounding (floor) for every product and quotient, every matrix–vector product an
exact dot product floored once. The right-hand side is the solver's generated straight-line program (226 temporaries,
about 950 products), evaluated on full values. The element boxes of "layout B" start at u = −10 and at v = ½, so the
rule needs only the quadrant u ≥ −10, v ≥ ½ and no analytic continuation. The output is z = ⌊10^p C + ½⌋ per
coefficient. Each case is then fixed in the paper by its parameters, a SHA-256 digest of a canonical text form of the
integers, per-block sums and spot values. The certification of P-APPC is applied unchanged to these integers.

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| ϱ to certify (record, G0g) | 10^−32.4 | 10^−30.9 | 10^−39.6 | 10^−36.9 |
| output quantum 10^−p (deduced, §1) | p = 58 | p = 56 | p = 65 | p = 62 |
| rule accuracy needed in G (deduced) | 10^−61 | 10^−59 | 10^−68 | 10^−65 |
| arithmetic | 320-bit fixed point (computed noise floor ≈ 10^−83 relative, §5) | same | same | same |
| layout B; elements | 2 × 2 | 2 × 2 | 3 × 2 | 2 × 2 |
| cells; (p_ξ, p_v); M | 30 × 30; (26, 39); M = 192 | 30 × 30; (26, 39); M = 176 | 60 × 30; (30, 45); M = 336 | 60 × 30; (28, 42); M = 192 |
| element degrees (N_t, N_s, M) | (112, 144, M) | (112, 144, M) | (136, 200, M) | (152, 192, M) |
| Picard sweeps per cell N_P (fixed) | 64 | 64 | 80 | 80 |
| **reader's cost, rule** (core-hours, deduced from the pilot) | ≈ 870 (≈ 580 with the precision ramp) | ≈ 760 (≈ 510) | ≈ 7,000 (≈ 2,300 with the ramp and a per-column M) | ≈ 2,500 (≈ 1,700) |
| reader's cost, certification (deduced from B-SOLV) | ≈ 6 | ≈ 6 | ≈ 12 | ≈ 8 |
| printed length of the rule | ≈ 12–15 pages for the rule, shared by all cases, plus ≈ 2 pages of digests and spot values per case | | | |

Against the tables it replaces: G0g's page model with ϱ certified gives 4,675 / 4,271 / 19,749 / 11,118 pages (record),
and the solver's pilot measured about 2.5 times S-APP's model (record, B-SOLV §4), so ≈ 11,700 / 10,700 / 49,000 /
28,000 pages (deduced).

**Recommendation.** **Adopt the rule of §3** (plain Picard in 320-bit fixed point on the solver's
discretisation, layout B) as the definition of the approximant, for seed 1 on D_A and seed 2 on D\* now, and seed 1 on
D\* when its closing is wanted.
- Under the rule, seed 1's D\* is a question of cost, not of reach. It is the dearest case, by about ×3 over seed 2's D\*,
  because of its slow angular decay near u\*.
- **Before the numbers are frozen in the text:**
  1. implement the rule, with an independent exact-integer implementation of one cell as a check of the text;
  2. measure the ratio of the order-3 certificate to the quantum (§1), which sets every parameter, by certifying the
     quad-double production's tables at p ≈ 36–38; at that point widen the transitions d, d′, which is free now;
  3. fix the parameters, run, certify, and enter the digests and spot values.
- **The reader's cost, which is also the authors':**
  - ≈ 500–900 core-hours for each D_A case;
  - ≈ 1,700–2,500 for seed 2's D\*;
  - ≈ 2,300–7,000 for seed 1's D\*.
  - That is about a day per D_A case on a 32-core workstation, two days for seed 2's D\* and up to a week for seed 1's.
    **It is not practical on this 4-core machine for the D\* cases.**
- **The text is ≈ 12–15 pages for the rule plus ≈ 2 pages per case.** That replaces ≈ 11,700–49,000 pages per case of
  tables.
- **The quad-double production runs are not the rule's output and cannot be made so** (§8). They remain a useful
  independent reference.

---

## 1. What the rule must reach

**The binding target is ϱ** in every case (record, G0g.0, at the least θ that attains the best f):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| f (weighted, orders ≤ 4) | 10^−30.2 | 10^−28.5 | 10^−36.9 | 10^−33.4 |
| ϱ | 10^−32.4 | 10^−30.9 | 10^−39.6 | 10^−36.9 |
| μ | 10⁻⁵ | 10⁻⁴ | 3 × 10⁻⁶ | 10⁻⁵ |

ϱ(p) is the supremum of max_(|J| ≤ N−1) |ℒ^J(2R̂ic)| over Q(a, b) (lem:tl5-hf-linfty; record): the residual and its Lie
derivatives along the commutation fields up to order 3 at level 4, **unweighted**. So the certificate must bound
derivatives of order ≤ 3 of the residual by ϱ, with margin. I keep G0b's margin of 10: the certified bound per element is
to be ≤ ϱ/10.

**From ϱ to the accuracy of the coefficients (deduced, by linear scaling of the pilot's certificate).** The pilot's
p = 30 tables (seed 2, D_A, layout A) were certified at derivative order 3 (record, `validation/cert_s2A_p30.txt`):

| at quantum 10⁻³⁰ | element (1,1) | (1,2) | (2,1) | (2,2) |
|---|---|---|---|---|
| own interpolant part Σ\|c\| at \|α\| = 3 | 2.3e-10 | 5.9e-10 | 1.0e-10 | 4.4e-11 |
| overlap Λ₃ | 1.7e-7 | 1.9e-7 | 1.2e-7 | 1.9e-7 |

B-SOLV §5 shows that both scale with the quantum: the element mismatch on the strips is the tables' own truncation,
about 200 quanta (record), and Λ is linear in it. The largest ratio is Λ₃ ≈ 1.9 × 10²³ × quantum. The tails E_α are not a
property of the integers; they fall with the certificate's node counts N (§8). So the quantum must satisfy
1.9 × 10²³ q ≤ ϱ/10:

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| ϱ/10 | 10^−33.4 | 10^−31.9 | 10^−40.6 | 10^−37.9 |
| q ≤ (ϱ/10)/(1.9 × 10²³) | 10^−56.7 | 10^−55.2 | 10^−63.9 | 10^−61.2 |
| **p chosen** (q = 10^−p; D\* one decade extra for its larger boxes) | **58** | **56** | **65** | **62** |
| rule accuracy (3 decades below q, so that no noise is quantized) | 10^−61 | 10^−59 | 10^−68 | 10^−65 |

The last row is a requirement on the rule, not on the printing. If the quantum sits below the coefficients' noise, the
noise is kept at high degree in two directions at once and the polyellipse majorant explodes (record, B-SOLV §7.2). So the
rule must be accurate to about three decades below its own output quantum.

**Uncertainty of this conversion (deduced).** The ratio 1.9 × 10²³ is measured on one case (seed 2, D_A, layout A, in
the element variables (t, σ, x)). The commutation fields are the static Killing field and the rotations; the arsinh chart
makes ξ-derivatives track the Killing field near the horizon, so the chart factors stay O(1) per order. The D\* layouts
have wider ξ-transitions (d = 14/125 for seed 2 and 3/40 for seed 1, against 11/200), which lowers Λ in the ξ-strips by
up to 2⁵, but not in the v-strips. I take the D_A ratio for all four cases and add one decade for D\*. The cost of the rule grows steeply with the
number of decades (§6), so **the authors should measure the ratio before fixing the parameters**. Two ways:
- certify the quad-double production's tables at p ≈ 36–38 (≈ 6 core-hours per case, §6);
- or certify a low-resolution run of the rule at p ≈ 40 (≈ 150–200 core-hours per D_A case, deduced from §6).

Then fix the final parameters.

---

## 2. The candidates, and why this rule

### 2.1 (R1) The solver's algorithm restated in exact fixed-point arithmetic

The solver (solver/solver.cpp) does more than the collocation map:
- defect correction, with the residual in dd/qd and the correction by Picard sweeps in **double** precision (IEEE binary64,
  libm `exp`, compiled with `-march=native`, so FMA contraction is up to the compiler);
- difference arithmetic about the seed;
- data-dependent stopping: a tolerance, a "floor", a stall test (gain < 4 over two evaluations), and in the inner loop a
  best-iterate rule and a growth stop;
- four quadrants around the corner, with the data continued analytically, for the boxes of layout A.

To make that reproducible bit for bit, the text would have to specify two arithmetics (the high-precision one and the
inner one), the scaling of the correction (a fixed-point inner loop cannot hold a correction 10⁻⁴⁰ times smaller than the
state unless it is rescaled and linearised), the Jacobian-vector products the linearised inner loop needs, and each
heuristic exactly. By my estimate that is at least twice the text of the chosen rule. And the saving is small (deduced from the pilot's
timings):
- one 320-bit sweep costs 6.9 s; a 64-bit fixed-point sweep 1.0 s (computed);
- the linearised inner loop needs dual numbers (about ×2), and each outer step repeats the inner convergence to the low
  precision;
- so defect correction in fixed point saves about ×1.6 against plain Picard;
- it saves ×4–5 only if the inner loop is IEEE binary64 in hardware, at the price of specifying IEEE arithmetic operation
  by operation and forbidding contraction.

**Not chosen.** The one part of R1 kept is the solver's discretisation itself: cells, nodes, the Goursat boundary terms,
the G-form near N₀ and the integration operators. That is what makes the rule's output agree with the solver's (§5).

### 2.2 (R2) A mathematically simpler rule

**(R2a) A formal power series without elements: none converges on D_A or D\*.**
- *Taylor series in v − ½ at fixed (u, x).* Computed from the pilot's jets on N₀⁺ (`scratchpad/bsolv/s2A_dd/s2A.jets`,
  the Taylor coefficients of F at orders 4–12, all x-modes): max_k |a_j| does not decay through order 12. The apparent
  radius (|a₆|/|a₁₂|)^(1/6) is **0.99–1.21** for m, n and s, and **0.42–0.47** for R, at u = −10, −5.6, −3.1 and −2.0
  (`jetrad.py`). The region needs v − ½ up to 3.
  - Why (deduced): B-SOLV §7.1 measured that the continuation into v < ½ loses x-analyticity. ρ_x falls from 2.3 to
    1.52 at Δv = −0.0855, Δu = 8.06; the Riemann function of an angular mode l there is I₀(2cl√|ΔuΔv|).
  - With that measured rate, the continuation at Δu ≈ 8 is analytic in x only for |Δv| ≲ 0.35. So the solution has
    singularities at distance 0.35–1.2 from v = ½ (for fixed real x), consistent with the jets.
  - So the series diverges at v ≥ ½ + 1.2 at the latest.
- *The double characteristic (Goursat) series at the corner (−10, ½).* It must also converge in u up to u = −2 (Δu = 8,
  D_A) or −1.1 (Δu = 8.9, D\*) with Δv = 3 at the same time.
  - The continuation into u < −10 has ρ_x = 1.73 at (Δu, Δv) = (−0.59, 3.08) (record, B-SOLV §7.1). With the same model
    that gives |Δu| ≲ 5 at Δv = 3 (deduced).
  - So it diverges too, before either corner of the region is reached.
- *Re-expansion* (re-centring the v-series along v, the u-dependence of every jet obtained by the transport of jets.cpp)
  is a Taylor-series marching solver. It is not shorter to state than the cell solver, needs ≈ 6–10 re-centrings at
  ≈ 100–150 orders each, and a u-discretisation of its own for every order. Not pursued.

**(R2b) Plain Picard on the solver's collocation map: chosen.** The definition of one sweep is one line,
G ← B + I[Ψ(G) − Ψ(seed)], and the cell problem, the data and the output are the solver's. In fixed point it converges
(computed, §5): ≈ 1.6 digits per sweep to 10⁻³⁷, then ≈ 0.9 digits per sweep, down to the arithmetic's floor ≈ 2 × 10⁻⁸³
at sweep ≈ 80. It agrees with the solver's quad-double cell to 1.4 × 10⁻⁶⁴ absolute (≈ 10⁻⁶² relative), the quad-double solver's own floor (§5.2).

### 2.3 (R3) Hybrids

- **A coarse printed table plus a correction rule.** The rule needs no starting table: Picard from the boundary terms
  converges in every cell. A coarse table would only add pages: S-APP's model gives ≈ 400 pages at f = 10⁻¹⁵ (record),
  so ≈ 1,000 at the measured ×2.5 (deduced). It would save the first ≈ 10 of the 64–80 sweeps per cell. **No gain.**
- **A low-precision start, then the full precision ("precision ramp").** The same sweep, in 64-bit arithmetic for the
  first sweeps and then 128, 192, 256 and 320 bits, is one more sentence in the text. It saves about ×1.5 (deduced from
  the measured per-sweep costs, 64 bits 1.0 s, 256 bits 5.4 s, 320 bits 6.9 s, and from the measured floor: each
  precision stalls about 12 decades above its resolution, because of the 1/ε³ of the first row, §5.1). A good option
  for the writer.
- **An existential theorem instead of a deterministic rule.** "The theorem holds for any approximant whose certificate
  passes; here is a procedure that produces one." The continuation lemma is existential in ĝ (lem:tl5-continuation only
  needs a background satisfying the certified conditions), so this would be logically sufficient. But the paper would
  then not contain its witness, which the author's decision (2026-11-27, "it contains the complete definition of the
  approximant") excludes. **Not recommended.**

### 2.4 A closed form for the correction

**None is known.** The seed (lem:tl5-seed) is the only closed-form part. The first-order correction is a solution of the
linearised equations on the seed with the cone data, whose Riemann function on this background is not known in closed
form either. I found no route to one.

---

## 3. The rule (specification for Appendix C)

Everything below is stated for one case (seed, region). The parameters of §4 are its only inputs besides the seed's
λ (1 for seed 1, √(1/10) for seed 2) and the formulas already in the paper (lem:tl5-seed, eq:cone-data,
lem:appc-regular).

### 3.1 The arithmetic model (≈ 0.5 page)

- B := 320. A *number* is an element of 𝔽 := 2^(−B) ℤ, held as the integer X = 2^B x. There is no bound on X.
- For real y, ⌊y⌋_B := 2^(−B) ⌊2^B y⌋, the largest element of 𝔽 not exceeding y. **Floor, not truncation toward zero**: an
  implementation in a language whose integer division truncates (C, C++, Java) must correct for negative quotients.
- Operations on 𝔽:
  - x + y and x − y are exact;
  - n x for an integer n is exact;
  - x ⊙ y := ⌊xy⌋_B;
  - x ⊘ y := ⌊x/y⌋_B for y ≠ 0, and x ⊘ n := ⌊x/n⌋_B for an integer n ≠ 0;
  - √x := ⌊√x⌋_B for x ≥ 0 (the integer square root of 2^B X);
  - a **dot product** ⟨a, b⟩ := ⌊Σ_i a_i b_i⌋_B: the exact sum of the exact products, floored once. Every matrix–vector
    product of the rule is a dot product in this sense. Since the inner sum is exact, it does not depend on the order of
    summation, so the result is the same under any parallelisation.
- A rational number q given in the text enters as ⌊q⌋_B.
- An expression written as a product chain a ⊙ b ⊙ c means (a ⊙ b) ⊙ c, left to right, as in the printed program (§3.6).

This model is exactly what `fx.h` implements (computed: 200 random cases of ⊙, −, ⊘, the reciprocal, dot products and
⊘ n agree bit for bit with Python's integer arithmetic, `fxtest.cpp`).

### 3.2 Elementary functions and constants (≈ 1 page)

Each is a stated finite computation in 𝔽, so the rule is a finite integer computation throughout. Accuracy is not part
of the definition; the stated degrees make each function accurate to a few units of 2^(−B) on the arguments that occur.
- **π̂** := 16 A(5) − 4 A(239), where A(n) := Σ_(j=0)^(J_n) (−1)^j ⌊1/((2j + 1) n^(2j+1))⌋_B, J₅ = 70, J₂₃₉ = 20
  (Machin's formula; every term an exact floored rational).
- **L̂₂** (log 2) := 2 Σ_(j=0)^(100) ⌊1/((2j + 1) 3^(2j+1))⌋_B.
- **exp(y)**:
  - let k ≥ 0 be the least integer with |y| ≤ 2^(k−3), and z := y ⊘ 2^k;
  - E := 1, then for n = 45, 44, …, 1: E := 1 + ((z ⊙ E) ⊘ n);
  - then k times E := E ⊙ E.
- **log(y)**, y > 0:
  - let m be the integer with 1 ≤ w := 2^(−m) y < 2 (exact, a shift); if w ≥ 3/2, put w := w/2 and m := m + 1;
  - t := (w − 1) ⊘ (w + 1);
  - log y := m L̂₂ + 2 S, where S := Σ_(j=0)^(70) t^(2j+1)/(2j + 1), by Horner in t ⊙ t from j = 70 down.
- **sin, cos (y)**:
  - k and z as for exp;
  - S and C, the Taylor polynomials of sin and cos of degrees 45 and 44 at z, by Horner;
  - then k times (S, C) := (2 S ⊙ C, C ⊙ C − S ⊙ S).
- **sinh, cosh**: (exp(ξ) − exp(−ξ)) ⊘ 2 and (exp(ξ) + exp(−ξ)) ⊘ 2.
- **ξ̂₀** := −log(4500 + √(4500² + 1)) (= −arsinh 4500, the image of u = −10); **â** := ⌊1/500⌋_B;
  **λ̂** := 1 (seed 1) or √(⌊1/10⌋_B) (seed 2).
- **ĉ(r)** := cos(π̂ ⊙ r) for rational r (all node sets below).

### 3.3 Nodes and spectral matrices (≈ 1–1.5 pages)

- **Node sets** on [−1, 1], all in 𝔽:
  - Chebyshev–Lobatto τ^L_j := −ĉ(j/p), j = 0, …, p (ascending);
  - Radau τ^R_j: the numbers ĉ(2j/(2p + 1)), j = 0, …, p, in ascending order (they include 1 and exclude −1);
  - angle x_k := ĉ(k/M), k = 0, …, M (descending).
- **Matrices.** Each entry is ⌊e⌋_B of an exact rational number e determined by the (dyadic) nodes. The nodes are
  rational, so e is rational and ⌊e⌋_B is an exact integer computation; any rational arithmetic gives it. With
  ℓ_j the Lagrange basis of the node set:
  - integration Q_ij := ∫_(−1)^(τ_i) ℓ_j;
  - differentiation D_ij := ℓ′_j(τ_i), with D₂ := the matrix of dot products ⟨D_i·, D_·j⟩;
  - for the Radau set on σ = (τ + 1)/2: W4_ij := σ_i^(−4) ∫_0^(σ_i) s³ ℓ_j(s) ds and
    V4_ij := σ_i^(−4) ∫_0^(σ_i) (σ_i − s) s² ℓ_j(s) ds;
  - QQ := the dot-product square of Q (the double integral);
  - the values-to-coefficients matrix of degree N (DCT-I): C_nm := ⌊(2/N) ε_n ε_m ĉ((nm mod 2N)/N)⌋_B, with ε = ½ at the
    two ends and 1 otherwise;
  - the barycentric weights, and for an element node t the values ℓ_j(t), again as floors of exact rationals.
- These are the matrices of `consts.py` (which computes them in 90-digit floating point) with the nodes first rounded to 𝔽.

### 3.4 The seed at a node (≈ 0.5 page)

At (ξ, v) ∈ 𝔽²:
- u + 1 := â ⊙ sinh ξ, u := (u + 1) − 1, du/dξ := â ⊙ cosh ξ;
- H := v − 2u + log((u + 1) ⊘ (u − 1));
- R_s: bisection on [r₀, r₁] with r₀ := 1 + 2^(−32), r₁ := max(H, 0) ⊘ 2 + 3, 80 steps
  (mid := (r₀ + r₁) ⊘ 2; r₀ := mid if 2 mid + log((mid − 1) ⊘ (mid + 1)) < H, else r₁ := mid), then 6 Newton steps
  R := R − (2R + log((R − 1) ⊘ (R + 1)) − H) ⊘ (2 + 2 ⊘ (R ⊙ R − 1)) from R := r₀;
- f := 1 − 1 ⊘ (R ⊙ R), g := 1 − 1 ⊘ (u ⊙ u); R_v := f ⊘ 2, R_u := −(f ⊘ g), Ω² := f ⊘ (2g), W_v := 1 ⊘ (2 R ⊙ R ⊙ R)
  (eq:appc-seed-jets).

### 3.5 Data on N₁ and N₀ (≈ 1 page)

- **N₀** (v = ½) enters only through the seed form: G := (F − F_seed)/(v − ½)⁴ is the unknown, and the first row of cells
  uses the Radau nodes, which exclude v = ½, with the exact operators W4 and V4. Nothing is divided by (v − ½)⁴ near N₀.
- **N₁** (u = −10, i.e. ξ = ξ̂₀), at the v-nodes of each row and the x-nodes:
  - m and n of eq:cone-data in G-form: with ε := v − ½, z := π̂ ⊙ ε ⊘ 3, s_c := (π̂ ⊘ 3) ⊙ (sin z ⊘ z),
    h := √(2 ⊘ (1 + x ⊙ x)), θ := v ⊘ λ̂ and r := R_s(ξ̂₀, v):
    G_m := h ⊙ λ̂ ⊙ ½ ⊙ (1 ⊘ (r ⊙ √r)) ⊙ s_c⁴ ⊙ cos θ, and G_n the same with sin θ (amp = 1);
  - W := W_seed, so G_W := 0;
  - R from the Raychaudhuri equation D_R,vv = 2W_s,v D_R,v − (R_s + D_R) σ²/3 along the row (σ² the shear of the data),
    by a fixed number N_Ray := 40 of sweeps of the row's integration operator (V4 in the first row, QQ with the
    Goursat end values in the others), from G_R := 0 in the first row and the continuation of the row below otherwise;
  - s is not needed on N₁: its equation is a transport in v.
- These are `n1_row` and `mn_data` of solver.cpp, with a fixed count in place of the tolerance.

### 3.6 Cells and the cell problem (≈ 2 pages, the straight-line program another 2–3)

- **Cells.** n_c columns of equal width in ξ from ξ̂₀ to ξ_e, and n_r rows of equal height in v from ½ to v_e, where ξ_e
  and v_e are the far ends of the element boxes (§4). Breakpoints ξ̂₀ + ((ξ_e − ξ̂₀) i) ⊘ n_c and ½ + ((v_e − ½) j) ⊘ n_r.
- **Nodes of cell (i, j).** Lobatto of degree p_ξ in ξ; in v, Radau of degree p_v in row j = 0, Lobatto of degree p_v
  otherwise; the x-nodes. The unknown is G^F at the nodes, F ∈ {R, m, n, W, s}.
- **Order.** Columns from ξ̂₀ outward; in each column, rows from v = ½ upward. A cell takes its left edge (R, m, n, W at
  the last ξ-node of its left neighbour, or the N₁ data) and its lower edge (all five fields at the last v-node of the
  cell below, and s_v there).
- **The boundary term B** (the Goursat terms, as in `solve_cell`):
  - row 0: B^F := G^F_left for F ≠ s, B^s := 0;
  - other rows: B^F := (ε_b⁴ G^F_bot(a) + ε⁴ G^F_left(b) − ε_b⁴ G^F_bot(0)) ⊘ ε⁴ for F ≠ s, and
    B^s := (ε_b⁴ G^s_bot(a) + (v − v_b) s_v,bot(a)) ⊘ ε⁴, with ε := v − ½ and ε_b the value at the lower edge.
- **Jets at a node** from the derivative matrices (dot products, then ⊙ 1/h): D^F := ε⁴ ⊙ G^F, D^F_x, D^F_xx,
  D^F_v := 4ε³ G^F + ε⁴ ⊙ ∂_v G^F, D^F_vx, D^F_u := (ε⁴ ⊙ ∂_ξ G^F) ⊙ (1 ⊘ du/dξ) (F = R, m, n). Then the full jets:
  - R := R_s + D_R and 1 ⊘ R;
  - e^(±S) := exp(±S), with S := ((1 + x) D_m + (1 − x) D_n) ⊘ 3;
  - Ω² := Ω_s² ⊙ exp(2D_W), Ω⁻² := (1 ⊘ Ω_s²) ⊙ exp(−2D_W);
  - R_u, R_v, W_v: the seed's plus the D's; all other jets are the D's.
- **The right-hand side** X = (X_R, X_m, X_n, X_W, S_vv) is the axis-regular evolution system of lem:appc-regular, solved
  for (R, m, n, W)_uv and s_vv (B-SOLV §1). **It is printed as a straight-line program**: 226 lines t_k := (product of
  earlier t's, jets and 29 rational constants), five sums r₁…r₅, and five output lines. This is `rhs_gen.h` (15.2 kB;
  computed), about 1.6 pages at 79 × 121 and 2–3 pages typeset. The program fixes the order of every rounded operation,
  and it can be checked against lem:appc-regular by symbolic algebra.
  - The alternative is to define X̂ := ⌊X(J)⌋_B, the exact polynomial value floored once. That is order-free but costs
    exact big-integer evaluation of degree-8 products, several times slower. Not recommended.
- **Ψ** := du/dξ ⊙ (X(J) − X(J_seed)) for F = R, m, n, W, and Φ := S_vv(J) − S_vv(J_seed), where J_seed is the same node
  with D = 0. In exact arithmetic X(J_seed) is the seed's own right-hand side; the difference makes D = 0 an exact solution
  for seed data.
- **The integration I**:
  - row 0: I^F := h_ξ ⊙ ⟨Q_ξ, ⟨W4, Ψ^F ⊙ (1 ⊘ ε³)⟩⟩ and I^s := ⟨V4, Φ ⊙ (1 ⊘ ε²)⟩;
  - other rows: I^F := (h_ξ h_v) ⊙ ⟨Q_ξ, ⟨Q_v, Ψ^F⟩⟩ ⊘ ε⁴ and I^s := h_v² ⊙ ⟨QQ, Φ⟩ ⊘ ε⁴.
- **The top edge's s_v** := s_v,bot + h_v ⊙ ⟨Q_v(p_v, ·), Φ⟩ (zero below row 0), from the final iterate.

### 3.7 The iteration and the stopping rule (≈ 0.3 page)

- G⁰ := B; G^(n+1) := B + I(G^n); the cell's value is G^(N_P), with N_P fixed per case (§4).
- **The stopping rule is the fixed count.** An implementation may stop early if a sweep leaves every integer unchanged:
  G^(n+1) is a function of G^n, so the remaining sweeps would change nothing, and the output is identical.
- In the pilot the iterate reaches no exact fixed point. From sweep ≈ 80 on it wanders within ≈ 2 × 10⁻⁸³ (relative) of
  the limit, the rounding noise amplified by the 1/ε³ of the first row (computed, §5). The fixed count decides which of
  these states is the output, deterministically.

### 3.8 Element values and coefficients (≈ 0.7 page)

- For element (i, j) with box [ξ_lo, ξ_hi] × [v_lo, v_hi] and degrees (N_t, N_s, M): nodes
  ξ_a := (ξ_lo + ξ_hi) ⊘ 2 − ((ξ_hi − ξ_lo) ⊘ 2) ⊙ ĉ(a/N_t), and v_b likewise with N_s.
- **The cell of a node**: the column with the least index whose right end is ≥ ξ_a (the first column for ξ_a < ξ̂₀:
  the box edge −1821/200 lies 2 × 10⁻⁵ outside, so its first node is a short extrapolation), and likewise the row.
- The value: ⟨ℓ(ξ_a), ⟨ℓ(v_b), G⟩⟩, the cell's interpolant at the node, with the Lagrange values of §3.3 (a node that
  equals a cell node takes that value).
- The coefficients C^F_abk: the DCT-I in t, then σ, then x, each a dot product with the matrix C of §3.3 (x in the
  order of x_k, t and σ ascending).
- **The output**: z^F_abk := ⌊10^p C^F_abk + ½⌋ (exact: ⌊(10^p X + 2^(B−1))/2^B⌋), the index set the nonzero z, and p
  the case's quantum. This is def:appc-approximant's input, unchanged.

### 3.9 Output in canonical form, digest and spot values

- **Canonical text** of a case:
  - ASCII only, LF line ends, no trailing blanks, a final LF;
  - for each element (i, j) in the order of i then j, and each field in the order R, m, n, W, s, a header line
    `block i j F p Nt Ns M`;
  - then one line per row (a, b) that has a nonzero entry, in the order of a then b: `a b z_ab0 z_ab1 … z_abK`, with K
    the last k of a nonzero entry, zeros inside the row written `0`, negatives with `-` (U+002D), single blanks.
  - This is P-APPC's row structure without labels, wrapping or line checks.
  - Size (deduced): ≈ 10⁷ integers of ≈ 15–65 digits, about 0.3–1 GB per case. Not printed.
- **Digest: SHA-256** (FIPS 180-4) of the canonical text of the case, and of each block's text. That is 20 block digests
  (2 × 2 × 5) or 30 (3 × 2 × 5) per case.
  - Why SHA-256: a published standard, defined on bytes, with implementations everywhere; the canonical form makes it a
    function of the integers alone.
  - **What it checks, mathematically.** SHA-256 is a fixed function, so "SHA-256(canon(Z)) = h" is a decidable statement
    about Z. A **mismatch proves** that a reader's integers are not the rule's output. A **match does not prove
    equality**: a digest of 256 bits cannot be injective on sets of 10⁷ integers, and the inference rests on collision
    resistance, which is not a theorem.
  - **Nothing in the proof rests on the match.** The certificate is a theorem about the rule's exact output, and the
    reader who computes the output and runs the certification on it has the whole proof, digest or not. The digest
    tells the reader that the paper's printed certificate numbers B_ij apply to the integers in hand, and it localises
    an implementation error to a block.
  - The per-block sums S₁, S₂, S₀ (eq:appc-sums; values of the block's polynomial at three points) are exact checks. A
    match there is a proved equality of three linear functionals, and a mismatch is a proof of difference.
- **Spot values**, printed per case:
  - per block: S₁, S₂, S₀, the number of nonzero entries, and z₀₀₀, z₁₀₀, z₀₁₀, z₀₀₁;
  - intermediate values, as hexadecimal integers 2^B x, for an implementer to locate an error by bisection: π̂, L̂₂,
    ξ̂₀, R_s at (ξ̂₀, ½), G_m on N₁ at the first node of row 0, G at the last node of cell (0, 0) after N_P sweeps, and the
    first element node value.
- **Pages** (deduced): a block line of a 64-hex digest, three ≈ 60-digit sums, a count and four ≈ 60-digit coefficients
  is ≈ 500 characters, 4–5 lines; 20–30 blocks are 100–150 lines; the intermediates ≈ 30 lines. So **≈ 2 pages per
  case**, ≈ 8 pages for all four.

---

## 4. Parameters for the four cases

Layout B is P-APPC's def:appc-layouts with the first ξ-box starting at −1821/200 (just outside ξ₀ = −9.104979…) and the
first v-box at ½. The breakpoints c_i, d, c′₁ = 2, d′ = 3/80 and the far edges are unchanged:

| case | ξ-boxes (layout B) | v-boxes | ξ_e, v_e |
|---|---|---|---|
| (1, D_A), (2, D_A) | [−1821/200, −7891/1000], [−813/100, −3421/500] | [1/2, 21231/10000], [18769/10000, 7171/2000] | −3421/500, 7171/2000 |
| (2, D\*) | [−1821/200, −827/125], [−1421/200, −4473/1000] | same | −4473/1000, 7171/2000 |
| (1, D\*) | [−1821/200, −7447/1000], [−7777/1000, −5943/1000], [−6273/1000, −4517/1000] | same | −4517/1000, 7171/2000 |

These are the boxes the quad-double production samples as its "layout B" (record, B-SOLV §7.1, `s1A.cfg`, `s2D.cfg`).

**The resolution** (deduced from the measured decay rates; the rule accuracy of §1):

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| rule accuracy (in G) | 10^−61 | 10^−59 | 10^−68 | 10^−65 |
| x-rate used (record: B-SOLV §2, S-APP §2.1) | 2.1 | 2.2 | 1.6 (s near u\*) | 2.2 |
| **M** | **192** | **176** | **336** | **192** |
| (ρ_t, ρ_σ) used (record) | (3.7, 2.7) | (3.7, 2.7) | (3.2, 2.2) | (2.7, 2.2) |
| **element degrees (N_t, N_s)** | **(112, 144)** | **(112, 144)** | **(136, 200)** | **(152, 192)** |
| **cells n_c × n_r** | **30 × 30** | **30 × 30** | **60 × 30** | **60 × 30** |
| **(p_ξ, p_v)** | **(26, 39)** | **(26, 39)** | **(30, 45)** | **(28, 42)** |
| **N_P** (sweeps per cell) | **64** | **64** | **80** | **80** |
| B (bits); p (quantum) | 320; 58 | 320; 56 | 320; 65 | 320; 62 |
| fixed counts | N_Ray = 40; Newton 6 after 80 bisection steps; exp, sin/cos degree 45; log 70 terms | | | |

- **M** is the least multiple of 8 with ρ_x^(−M) A ≤ (rule accuracy)/10, A ≈ 10⁻² the largest x-coefficient of G
  (record, `validation/rates_s2A.txt`).
- **Seed 1's D\* sets the hardest x-resolution.** Its shift s has ρ_x ≈ 1.6 at (u\*, 2.5), with a real singularity just
  beyond the axis at x ≈ −1.11 (record, S-APP §2.1). One Chebyshev expansion in x then needs M ≈ 330 at 10⁻⁶⁸. That is a
  question of cost, not of reach (§6).
- **(N_t, N_s)** come from the same rule with the element rates; seed 2's D_A takes seed 1's values.
- **The cells and (p_ξ, p_v)** come from the cell discretisation error measured in quad-double (computed, §5.3).

---

## 5. The pilot: the rule's cell in fixed point against the solver's cell in quad-double (computed)

**What was run** (`fxpilot.cpp`, `fx.h`; one core, `nice -n 19`, on a machine whose load was 5–11 on its 4 cores from the
other agent's runs):
- the corner cell (first column, first row) of the double-double pilot's configuration: seed 2, D_A domain, 30 × 30
  cells, (p_ξ, p_v) = (16, 24), M = 80, 34,425 nodes;
- (a) the solver's own `solve_cell`, built in quad-double, run to its own stall (the floor and tolerance set to 10⁻³⁰⁰);
- (b) the rule's plain Picard sweep in fixed point with B = 320 (and 256 and 64 for the timing). The geometry, the seed
  values, the N₁ data and the spectral constants were taken from the solver and converted exactly into 𝔽: the rule
  computes them itself, and that one-off per-cell cost is not in the timings.

### 5.1 Convergence and the arithmetic's floor

| sweep | 1 | 5 | 10 | 15 | 20 | 25 | 30 | 40 | 50 | 60 | 70 | 75 | 80–200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| max\|G^(n+1) − G^n\| / max\|G\| | 9.0e-2 | 4.8e-7 | 1.2e-15 | 6.2e-24 | 1.3e-32 | 1.7e-38 | 3.8e-42 | 7.4e-50 | 1.4e-58 | 1.6e-68 | 5.1e-76 | 1.2e-81 | 8e-85 … 2.6e-83 |

- ≈ 1.6 digits per sweep down to 10⁻³⁷, then ≈ 0.9 digits per sweep. The solver's defect correction shows the same
  two phases: its first inner solve gains 14 digits in 17–18 sweeps; later inner solves gain ≈ 12 digits in 28–35 sweeps
  (computed: three dd cells with `BSOLV_VERBOSE`, `p1.err`).
- **The floor of 320-bit arithmetic** here is ≈ 10⁻⁸³ relative: the rounding of 2^(−320) amplified by 1/ε³ ≈ 8 × 10¹¹ at
  the first Radau node (ε ≈ 1.06 × 10⁻⁴). It is 12–15 decades below every case's need (10⁻⁶⁸ at most). **B = 256 would
  put the floor near 10⁻⁶⁴, too close for the D\* cases; B = 320 is the choice** (deduced from the measured floor).
- **No exact fixed point** is reached in 200 sweeps: from sweep ≈ 80 the update stays between 8 × 10⁻⁸⁵ and 2.6 × 10⁻⁸³
  (relative). The fixed count of §3.7 therefore matters for the last bits, and only for them.

### 5.2 Agreement with the solver

| field | max\|G_rule − G_qd\| | max\|G_qd\| | relative |
|---|---|---|---|
| R | 4.0e-67 | 5.7e-8 | 7.0e-60 |
| m | 1.4e-64 | 2.9e-3 | 4.8e-62 |
| n | 6.6e-65 | 9.0e-3 | 7.3e-63 |
| W | 2.2e-68 | 3.3e-6 | 6.5e-63 |
| s | 8.7e-67 | 1.7e-5 | 5.3e-62 |

After 200 sweeps the rule's cell agrees with the solver's quad-double cell to 1.4 × 10⁻⁶⁴ absolute, ≈ 10⁻⁶² relative.
The quad-double cell stopped at a relative update of 3.3 × 10⁻⁶³ after 8 outer steps and 198 inner double sweeps, in
114 s.

So the rule computes the solver's discrete solution, not merely a nearby one; the difference is the quad-double
solver's own iteration floor.

### 5.3 The cell discretisation error against (p_ξ, p_v) (quad-double, `pconv.cpp`)

The corner cell of the pilot's grid (30 × 30 cells on D_A, M = 80), solved by `solve_cell` in quad-double at four
degrees, each compared with the finest at its own nodes. Each was solved to the quad-double floor: relative updates
3.4e-63, 3.3e-63, 8.6e-64 and 2.7e-63 after 8 outer steps.

| (p_ξ, p_v) | 12/18 | 16/24 | 20/30 | 24/36 |
|---|---|---|---|---|
| max\|ΔG\| against 24/36: R / m / n | 1.5e-31 / 6.6e-33 / 2.1e-32 | 2.5e-42 / 8.3e-42 / 2.5e-41 | 1.3e-52 / 1.9e-51 / 8.9e-51 | (reference) |
| the same, W / s | 2.5e-33 / 9.9e-34 | 3.0e-43 / 9.6e-44 | 1.3e-51 / 7.1e-54 | |
| qd cell time (one core) | 56 s | 100 s | 155 s | 249 s |

- Each step (+4, +6) gains ≈ 10 decades: ≈ 2.4 decades per unit of p_ξ with p_v = 1.5 p_ξ (computed).
- **Extrapolated** (deduced, geometric): 24/36 ≈ 2 × 10⁻⁶⁰, 26/39 ≈ 3 × 10⁻⁶⁵, 28/42 ≈ 5 × 10⁻⁷⁰, 30/45 ≈ 8 × 10⁻⁷⁵
  (absolute in G).
- **The choices of §4** keep a margin of ≥ 3–6 decades over each case's rule accuracy at this cell:
  - (26, 39) for D_A (need 10⁻⁶¹ and 10⁻⁵⁹);
  - (28, 42) for seed 2's D\* (need 10⁻⁶⁵);
  - (30, 45) for seed 1's D\* (need 10⁻⁶⁸).
- This is one cell. The far cells have larger G (amplitudes up to ≈ 2 × 10⁻² against 9 × 10⁻³ here; record,
  `validation/rates_s2A.txt`), and the cells near u\* on D\* are not measured. The margin is meant for that, and the
  measurement of B₃/q in §1 checks it.

### 5.4 Cost per sweep

| arithmetic (one core) | per sweep, M = 80, 34,425 nodes | per node |
|---|---|---|
| 64-bit fixed point | 1.0 s | 29 µs |
| 256-bit fixed point | 5.4 s | 157 µs |
| **320-bit fixed point (the rule)** | **6.9 s** (5.4–10.6 with the load) | **200 µs** |
| M = 160, 320 bits | 16.3 s (68,425 nodes) | 238 µs |
| for comparison: the solver's dd residual (difference arithmetic) | 1.4–1.8 s | 41–52 µs |
| the solver's whole dd cell (4 outer, 78–85 inner double sweeps) | 18.6–20.3 s | |
| the solver's whole qd cell, to its stall (8 outer, 198 inner) | 114 s | |

A 320-bit fixed-point sweep, without difference arithmetic, costs about 4.3 dd residual evaluations and about
0.45 of a quad-double one (the quad-double residual is ≈ 10× dd; record, B-SOLV §6: ≈ 500 µs per node in qd).

**The sweep count does not grow with M (computed, M = 160, same cell, `run_M160.out`, `run2_M160.out`).**

| sweep | 10 | 20 | 25 | 30 | 35 | 40 | 41 | 46 | 55 | 63 | 64–77 |
|---|---|---|---|---|---|---|---|---|---|
| M = 80 | 1.2e-15 | 1.3e-32 | 1.7e-38 | 3.8e-42 | 1.9e-45 | 7.4e-50 | 3.6e-50 | 5.5e-55 | 1.8e-62 | 3.5e-70 | 1.6e-71 … 7.1e-81 |
| M = 160 | 1.2e-15 | 1.3e-32 | 3.7e-40 | 9.8e-49 | 2.2e-57 | 1.7e-65 | 1.5e-67 | 9.8e-72 | 1.2e-76 | 4.6e-82 | 8.8e-83 … 4.2e-82 (floor) |

- Up to 10⁻³² the two runs agree digit for digit, since the low angular modes dominate.
- At M = 160 there is no slow phase at 10⁻³⁸: the cell is at 10⁻⁶⁷ after 41 sweeps.
- From sweep 42 the largest update sits at the axis node x = −1, in m and n equally. There m drops out of P and Q
  ((1 + x)m = 0), so it is fixed only through the regularity of the system. It decays at ≈ 0.55 digits per sweep, while
  every node away from the axis has reached the arithmetic's floor (the update of m at the middle node is 10⁻⁸⁷ by sweep
  47). It reaches the 320-bit floor (≈ 10⁻⁸² relative) at sweep 63 and stays there through sweep 77 with no growth,
  where the run was stopped.
- The slow phase at M = 80 sets in near that grid's own angular truncation level (≈ 10⁻³⁰; record, B-SOLV §2(b)) and
  is absent at M = 160. So it appears to be a property of the under-resolved angular grid, not of Picard (deduced,
  not proved).
- So N_P = 64 (D_A) and 80 (D\*) carry a margin over the sweeps that reach each case's accuracy, 10⁻⁶⁴ and 10⁻⁷¹ relative:
  ≈ 57 and ≈ 65 sweeps at M = 80, ≈ 39 and ≈ 46 at M = 160. Two builds (`fxpilot_q6`, `fxpilot2_q6`) give the same per-sweep figures, as an integer computation must.

---

## 6. The reader's cost

**Model (deduced from §5).**
- Cost per sweep of a cell = nodes × c(M), with nodes = (p_ξ + 1)(p_v + 1)(M + 1) and c(M) = c₀ + c_x (M + 1) per node.
  Fitted to the two pilot points: c(80) ≈ 180 µs (160–200 with the load) and c(160) = 238 µs give c₀ ≈ 121 µs
  and c_x ≈ 0.73 µs per x-node. So c(176) ≈ 250, c(192) ≈ 262 and c(336) ≈ 366 µs per node per sweep.
- The cost of the rule ≈ n_c n_r N_P × that, on one core of this machine.
- The element sampling and the coefficient transforms are a few core-hours per case (deduced: ≈ 10¹⁰ dot-product terms
  per element).

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| nodes per cell (p_ξ + 1)(p_v + 1)(M + 1) | 208,440 | 191,160 | 480,562 | 240,671 |
| one sweep of one cell | 55 s | 48 s | 176 s | 63 s |
| one cell (N_P sweeps) | 58 min | 51 min | 3.9 h | 1.4 h |
| **the rule, one core of this machine** | **≈ 870 core-hours** | **≈ 760** | **≈ 7,000** | **≈ 2,500** |
| with the precision ramp (×1/1.5) | ≈ 580 | ≈ 510 | ≈ 4,700 | ≈ 1,700 |
| … and a per-column M for seed 1's D\* (×0.5, below) | | | ≈ 2,300 | |
| wall time, 32 cores at 1.5× this machine's per-core speed | ≈ 12–18 h | ≈ 11–16 h | ≈ 2–6 days | ≈ 1.5–2.2 days |
| wall time, this machine (4 cores, if it were free) | ≈ 6–9 days | ≈ 5–8 days | ≈ 24–73 days | ≈ 18–26 days |
| memory (deduced) | ≈ 0.3 GB per cell in flight; ≈ 1 GB per element's node values | | ≈ 0.6 GB per cell; ≈ 2.2 GB per element | ≈ 0.3 GB; ≈ 1.2 GB |

All figures are ± 50 %:
- the per-node cost moved by ± 25 % with the machine's load;
- N_P carries a margin (below);
- the cells near u\* are not measured.

**The authors pay the same cost**: the rule's output exists only once someone has computed it. **On this 4-core machine,
shared with other runs, the D\* cases are not practical.** A 32–64-core workstation or a short cluster allocation is
needed: about a day for each D_A case, 2 days for seed 2's D\*, and up to a week for seed 1's D\*.

**What lowers the cost** (each deduced; none changes the certificate):
- **the precision ramp** (§2.3): ×1/1.5, one sentence of text;
- **a per-column M for seed 1's D\***: only the columns near u\* (ρ_x ≈ 1.6) need M ≈ 336. The others (ρ_x ≥ 2.2–2.4;
  record, S-APP §2.1) need M ≈ 200. Columns of different M pass their edge data by Chebyshev resampling in x (one
  paragraph of text). With about 10 of 60 columns at M = 336 this is ×0.5;
- **fewer sweeps**: at M = 160 the corner cell converged faster than at M = 80 (10⁻⁶⁷ after 41 sweeps, against 7 × 10⁻⁵⁰;
  computed, §5.4). If the production resolution behaves so, N_P = 48 (D_A) and 56 (D\*) suffice: ×0.7–0.75;
- **wider transitions** d, d′. They cost nothing now that there are no pages. Λ_k falls like (2d)^(−(k+2)) at the top
  orders (record, B-SOLV §7.3), so d′ = 1/4 in place of 3/80 lowers the v-strip overlaps at order 3 by ≈ 10⁴. That
  lowers the precision the rule must reach by up to ≈ 2–4 decades, worth ≈ ×0.7. **The rule's cost grows about like the
  4.5th power of the number of decades** (p_ξ, p_v, M and N_P each grow linearly with it), so each decade saved is worth
  ≈ 7 %;
- **targets that loosen** after a further sharpening help in the same proportion.

**Parallelism.** Within a cell every node is independent, and the cells on each anti-diagonal i + j = const are
independent. In exact integer arithmetic the result does not depend on the order or the number of threads. So a
workstation with P cores divides the wall time by about P, up to the anti-diagonal length (30–62 cells).

**The certification** of the rule's output (deduced from B-SOLV's measured cert3 rate, 15–18 min per element at 2.0–2.5M
nodes at 192 bits, linear in the nodes):
- with clean coefficients the majorant's ellipse can be taken near the coefficients' own rates, about (2.5, 2, 1.8),
  instead of the pilot's (2.5, 1.5, 1.35), which the dd noise forced;
- the tails E_α at |α| = 3 then fall below 10⁻⁴¹ at N ≈ (150, 250, 250), about 9 × 10⁶ nodes, ≈ 1–1.5 h per element;
- the overlaps take ≈ 5 min per strip;
- so ≈ 6 core-hours for a 2 × 2 case and ≈ 10–12 for seed 1's D\*. It is small next to the rule.

---

## 7. Reproducibility risks, and how the text removes them

| risk | removed by |
|---|---|
| truncation toward zero in place of floor (C's `/` and `>>` on negative values) | the text says "floor"; a spot value with a negative product |
| a sequence of rounded multiply-adds in place of the exact dot product | the text defines the dot product; a spot value of one D-application |
| the order of operations in the right-hand side | the straight-line program fixes it; any reordering is a different (wrong) implementation, caught by the first-cell spot value |
| elementary functions taken from a library | each is a stated algorithm (§3.2); spot values of π̂, L̂₂, exp, log and sin at fixed arguments |
| node orderings (ascending t and σ, descending x), Radau orientation, element node order | stated in §3.3 and §3.8, and in the block digests |
| which cell owns an element node on a cell boundary, or the box node outside u = −10 | the tie rule of §3.8 |
| data-dependent stopping | none: fixed counts throughout, with early stopping allowed only when a sweep changes nothing |
| overflow in fixed-width integers | the model has no bound. A fixed-width implementation needs a generous integer part: the pilot used 64 bits and nothing overflowed, and the entries of D₂ alone reach ≈ M⁴/15 ≈ 10⁹ at M = 336 (deduced). The text should say so |
| floating point anywhere | none is used |
| threads, platform, compiler | integer arithmetic is exact; the result is independent of them |
| a crash after days | determinism makes any checkpoint resumption exact |
| an implementation that disagrees with the digest | bisect with the intermediate spot values; or certify one's own output, which proves the theorem's existence claim for that output but not the paper's printed numbers B_ij |

The remaining risk is ambiguity in the prose. The cure is the intermediate spot values (§3.9), which pin each stage. A
second, independent implementation by the authors before publication (for example Python with exact integers for one
cell, against the production code) would check the text itself.

---

## 8. Certification of the rule's output, and the quad-double runs

**The certification stays as it is.** prop:appc-element-bound, prop:appc-overlap and the norm interface take the
integers z and p as given. Nothing in them depends on how the integers were obtained. Three adjustments only:
- def:appc-approximant reads "the rule of sec:appc-rule gives, for each element and field, an integer p and integers z"
  in place of "the tables give";
- def:appc-layout's admissibility drops the inner-nine-tenths condition at the two characteristic edges u = −10 and
  v = ½ (layout B). The certificate already uses the endpoint (Markov) values T_n^(l)(1) in eq:appc-ealpha, so no proof
  changes;
- sec:appc-outcomes takes the new targets (ϱ and f per case, the targets f_ij) and the certified numbers B_ij of the
  rule's output.

**The certificate is a theorem about the rule's exact output.** Its numbers are computed from that output, so they apply
to it and to nothing else.

**The quad-double production runs are a reference, not the output.** They cannot become the output:
- their arithmetic is floating point, with a double-precision inner loop using libm's `exp`, built with `-march=native`
  (FMA contraction at the compiler's choice), and a data-dependent stopping (tolerance, floor 10⁻³⁹, stall and growth
  tests);
- none of that is specified in the paper, and specifying it would mean specifying IEEE binary64 operation by operation
  and the compiler's choices;
- their resolution is sized for G0c's old targets: M = 92–100, a floor of 10⁻³⁹ against the rule's 10⁻⁵⁹–10⁻⁶⁸ (record,
  B-SOLV §0, §3);
- they sample layout A and layout B, while the rule needs layout B only.

What they are good for:
- **validating an implementation of the rule.** The rule's output must agree with them on the region to their accuracy
  (≈ 10⁻³⁵–10⁻⁴⁰). The rule's arithmetic, stopping and code differ from theirs, so that is an independent check;
- **choosing the rule's parameters** in the decades that quad-double reaches: rates, cell sizes and the B₃/q ratio of §1,
  measured on their tables.

**What has to be rerun:**
1. the rule itself, for each case to be printed (seed 1 on D_A and seed 2 on D\*, and seed 1 on D\* if decided; seed 2 on
   D_A only if wanted, since seed 2's D\* covers it);
2. the certification (cert3, overlapK, certsum) on the rule's outputs;
3. before that, the measurement of B₃/q (§1): the quad-double tables at p ≈ 36–38 certified, or a low-resolution rule run.

Whether to continue the quad-double production is the coordinator's call. Its value now is as a reference; the rule
does not need it.

**One open point outside the rule.** P-APPC's placement note 3a leaves to the writer of thm:tl5-hf whether the reference
part carries the solution's v-jets of orders 4 to N + 1 on N₀. If it does, the rule must also define those jets: the
transport hierarchy of jets.cpp, in the same arithmetic. That adds ≈ 1 page and a run along N₀ that is cheap next to
the cells.

---

## 9. Fallback: reductions that keep printed tables (one paragraph)

If tables were ever printed again, these would combine multiplicatively:
- **base 32** (Crockford, unambiguous to the eye) in place of decimal: ×0.75 of the characters on the pilot's p = 30
  tables, falling toward ×0.70 at p ≈ 60; base 64 ×0.67, base 85 ×0.64 (computed, `radix.py`). The line check
  generalises: 97 is prime, larger than 64 entries per line and than 32, and prime to 32 and 31;
- **layout B**: removes the side-quadrant degrees (σ up to 144, x-rate 1.52) in two of the four elements. B-SOLV §7.1
  measures the cause, but the factor is not measured; ×0.7–0.8 is my estimate (deduced);
- **an index-dependent quantum**: smaller where the derivatives amplify more. Not measured; it moves digits rather than
  removing them;
- **removing the jets on N₀⁺**: no gain, since the jets are themselves full functions of (u, x);
- **symmetries**: none unused (record, S-APP §3a, §2.1: no x-parity, and the data break the circle exchange);
- **per-element quanta**: already in the format.

Together ≈ ×0.5, so ≈ 6,000 / 5,000 / 25,000 / 14,000 pages (deduced): still far beyond a paper. This is the case for
the rule.

---

## 10. What changes in the paper

**proofs/P-APPC.md** (the draft Appendix C; nothing is merged yet, and chapters/ contains no reference to Appendix C, to
"Tables of the approximant" or to a final part: computed, `grep -rn`):

| section | change |
|---|---|
| opening paragraph (lines 3–7) | replace "fixes the format in which its coefficients are printed in the part 'Tables of the approximant' after the references" by "defines its coefficients by an exactly specified rule"; replace "A reader who has the printed integers, the formulas … can repeat every step" by: a reader who computes the integers by the rule of sec:appc-rule, in integer arithmetic, and has the formulas of ch:ten-l5 and of this appendix and any arithmetic of intervals with exact rational end points, can repeat every step. **This is the self-containedness statement**: the paper contains the complete definition of the approximant, not its coefficients (author, 2026-11-27) |
| eq:appc-regions, sec:appc-definition, def:appc-layout | kept; the admissibility condition relaxed at u = −10 and v = ½ |
| def:appc-layouts | replaced: layout B (§4 table), with the cell grid, degrees and quantum per case added or moved to the new section |
| def:appc-pou, lem:appc-pou | kept |
| def:appc-approximant, lem:appc-approximant, rem:appc-contact | kept; "the tables give" → "the rule gives" |
| **sec:appc-format** (the format, eq:appc-sums, eq:appc-linecheck, lem:appc-checks, the decay remark) | **replaced** by a new section "The rule" (sec:appc-rule, §3.1–3.8 of this report, ≈ 10–12 pages with the straight-line program) and "The output and its digest" (§3.9: canonical form, SHA-256, eq:appc-sums kept as the exact block checks). **eq:appc-linecheck and lem:appc-checks are dropped**: line checks guard transcription, and nothing is transcribed |
| sec:appc-regular, lem:appc-regular | kept. It is also the source of the right-hand side of the rule; the straight-line program cites it |
| sec:appc-certification and its five subsections | kept unchanged ("printed coefficients" → "the coefficients of the rule" in sec:appc-exact's title and first sentence) |
| sec:appc-outcomes | kept; the targets updated (G0g: ϱ binding), and a column with the digests' reference |
| **sec:appc-specimen** | **replaced** by "Digests and spot values" (§3.9), ≈ 2 pages per case |
| Placement, item 1 | the final part "Tables of the approximant" is dropped. The appendix stays after Appendix B and before the references; no part after the references |
| Placement, item 2 | the four computational items become: the rule's parameters fixed (after B₃/q is measured, §1), the outputs computed, certified, and digests and spot values entered |
| Placement, item 3a | add: if the reference part carries the jets of orders 4 to N + 1, the rule defines them (§8) |
| Crosswalk rows | drop eq:appc-linecheck and lem:appc-checks; retitle sec:appc-format and sec:appc-specimen; add sec:appc-rule, its displays (the arithmetic model, the elementary functions, the cell problem, the sweep, the output map) and the digest table |

**Elsewhere:**
- **notes/DECISIONS.md** already records the decision (01d42cba). The writer should add the rule's parameters once they
  are fixed. The order of work is unchanged.
- **chapters/01-introduction.md:199 and chapters/96-tables.md:3** say that Appendix B "prints the coefficients of the
  explicit polynomials, approximants and enclosures that the proofs use". That stays true of Appendix B. When Appendix C
  is merged, the introduction's list of appendices needs one added clause, e.g. "Appendix C defines the approximant of
  the continuation argument by an exactly specified rule, with digests of its output, and certifies its residual".
- **solver/README.md and tables.py** describe the printed tables; they are tools, not paper. A rule implementation (and
  a canonical-form writer and digest) would replace tables.py's role.
- **sec:tl5-beyond, rem:tl5-beyond**: P-APPC already notes that they will cite app:approximant once the continuation
  theorem is stated. Unchanged by this decision.

---

## 11. Files (under `scratchpad/srule/`)

| file | what |
|---|---|
| `fx.h` | the arithmetic model: fixed point with L 64-bit limbs, floor rounding, exact dot products, reciprocal, small-integer division, exp |
| `fxtest.cpp`, `fxtest.out` | 200 random cases against Python's exact integers (all agree) |
| `fxpilot.cpp`, `fxpilot_q{2,5,6}` | the rule's cell in fixed point against the solver's quad-double cell |
| `run_q6.out`, `run_q6.err` | the 200-sweep run and the comparison (§5.1, §5.2) |
| `run_M160.out`, `fxpilot2.cpp`, `run2_M160.out` | the sweep rate and cost at M = 160, and the long diagnostic run with per-field and angular-mode updates (§5.4) |
| `pconv.cpp`, `pconv.out`, `c_*_80.bin`, `c_16_24_160.bin` | the cell discretisation error against (p_ξ, p_v) (§5.3) and the constants it used |
| `p1.cfg`, `p1.err`, `p1_M160.cfg` | the configurations, and three dd cells with the solver's verbose log |
| `jetrad.py` | the Taylor radius in v from the jets on N₀⁺ (§2.2) |
| `radix.py` | the radix factors (§9) |
| `chain.sh`, `chain2.sh`, `chain.log`, `chain2.log` | the sequence of pilots |
| `cost.py` | the reader's cost model and table (§6) |
