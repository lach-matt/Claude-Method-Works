# B-SOLV: the compiled solver for the approximant, the double-double pilot, and the quad-double production

Report only. Code and small validation files are in `research/warp-drive/paper/reader/solver/` (README there); large
outputs in `scratchpad/bsolv/`. Nothing in chapters/, crosswalk/, proofs/, notes/ or PAPER.md was edited; nothing was
committed; nothing under method/, drive/, extracted/ or recovered/ was read. The record's solver
(docket68/n1star/dnsolve5.py) and runs (G0/G0b's `scratchpad/g0/runs/`) were used read-only as the reference.
Labels: **computed** (floating point unless said otherwise), **certified** (ball arithmetic, a bound), **deduced**.

## 0. Status in one paragraph

A compiled characteristic solver (C++, OpenMP, double-double, quad-double by `-DUSE_QD`) for the axis-regular
evolution system is built and validated. The double-double pilot (seed 2, D_A, P-APPC's layout) ran in 66 min of
cell time on 4 cores; its unquantized approximant has residual **max 8.3e-26, median 8.5e-28** (curvature units,
1960 points incl. the axes, dd evaluation), and its printed tables reach **max 1.3e-22–2.0e-22** at per-element quanta
p = 32–34 / 32–33 (2,823 / 2,505 pages) and **1.8e-19** at p = 30 (1,932 pages) — the level-4 target 10^−20.9 of
G0c is met at the sample points by 1.8–2 decades (computed). The certification pipeline was restructured for blocks
of 10⁶ integers (FLINT integer matrices) and reproduces N-APP1's stand-in bound exactly. **Certified** from the printed
integers of the pilot's p = 30 tables: on the whole use region of every element the residual is **≤ 1.0e-15**
(10^−15.0; per element 5.5e-16, 1.0e-15, 1.5e-16, 9.9e-16), the elements' own residuals being 6e-19–2.5e-17 and the
**overlap correction** the rest — G0b's level-3 target 10^−14.6 is met at level 0, P-APPC's tabled f = 10^−16.6 and
G0c's level-4 target are not; the derivative orders (to 4) are certified but far above every target, limited by the
E_α tails (N) and by the overlaps, which scale with the quantum (§5). Double-double tables cannot be printed finer
than p ≈ 30–31 and still certify (§7.2), so **level 4 needs the quad-double tables**, at p ≈ 40 by the scaling of the
overlap term (deduced). Three structural findings bear on P-APPC (§7): the box extensions into the side quadrants,
the double-double noise floor against the certificate, and the blend's derivatives at order K. Seed 1 on D_A is
running in quad-double (production, checkpointed; ≈ 9–10 h under the present load, ≈ 6–7 h alone);
seed 2 on D* is configured, not run (projected ≈ 14 h qd); seed 1 on D* was not run, as instructed.
**Targets moved after the last brief:** notes/reports/G0d.md and G0e.md (dated today) put level 4 at f ≈ 10^−39.7
(seed 2, D_A), 10^−40.9 (seed 1, D_A), 10^−49.1 (seed 2, D*); the qd runs as configured (M = 92–100, p 16/24) are
sized for G0c's 10^−20.9–10^−25.4 and resolve ≈ 1e-28–1e-34 in x; G0e's figures would need M ≈ 120–180 and higher
p_v (deduced from the measured rates, §2(b)). I have not changed the runs for it.

## 1. What was built (solver/, see its README)

- `derive.py`, `gen.py`, `gen_res.py`: from P-APPC's axis-regular components (regform.py, verified identical to
  chapter 87's formula by N-APP1), the evolution system E1 = (f_11 − f_xx)/(1 + x), E2 = (f_22 − f_xx)/(1 − x),
  E3 = f_xx, E4 = f_ln for (R, m, n, W)_uv and E5 = f_lx/√w for s_vv, with exact polynomial divisions by 1 ± x.
  **The target matrix has determinant −1/(Ω⁸R)** (nondegenerate at the axes, solved explicitly: m_uv = −Ω²r₁,
  n_uv = −Ω²r₂, R_uv = R(S_uv − Ω²r₃), W_uv = Ω²r₄ − 3R_uv/(2R)); E5 contains no u-derivative (a transport of s
  along each outgoing cone). Generated C++ templates: 948 multiplications (RHS), 2,096 (the eight residual
  components). (computed, exact sympy)
- `dd.h`, `qd.h`, `real.h`: double-double (≈ 32 digits) and quad-double (≈ 64 digits; Hida–Li–Bailey accurate
  addition and multiplication), with exp, log, expm1, log1p, sin/cos, sinh/cosh, asinh, sqrt; checked against
  mpmath to 1e-32 and 1e-64. `diff.h`: difference arithmetic about a reference state.
- `solver.cpp`: characteristic cell marching. Chebyshev–Lobatto in x (axes included), a tensor grid of cells in
  (ξ, v) with Lobatto nodes of degrees p_ξ, p_v; unknown G = (F − F_seed)/(v − ½)⁴ in every cell; the cells next to
  N₀ use Radau nodes excluding v = ½ and the exact operators q ↦ ε⁻⁴∫₀^ε t³q, φ ↦ ε⁻⁴∫₀^ε(ε − t)t²φ, so **G is
  produced directly near N₀**; the right-hand sides in difference arithmetic about the seed (relative accuracy
  in the perturbation, not in R ≈ 10); **defect correction**: residual in dd/qd, correction by Picard sweeps in
  double (difference arithmetic about the current state), 3–4 outer steps in dd, 5–6 in qd (the first three in dd);
  N₁ data (m, n of eq:cone-data, W = W_seed, R by Raychaudhuri, s by its own transport), N₀ the seed, and the
  analytic continuation into all four quadrants around (−10, ½) for the boxes that extend beyond the region;
  OpenMP within cells; checkpoints every `ckpt_minutes` (default 20) at column ends, resume by rerunning.
  The implicit angular treatment was not needed: with defect correction the inner Picard sweeps in double cost
  ≈ 10 % of a qd cell; the cost is the working-precision residual (§6).
- `jets.cpp`: the jets on N₀⁺ by the transport hierarchy (Taylor arithmetic through the same equations; s_k
  algebraic in lower orders, a_k by the linear transport with the seed's coefficients, initial values the data's
  Taylor coefficients at (−10, ½)) — independent of the cells. (On the seed the coefficient of F_vx vanishes, so
  the transport is pointwise in x, as N-APP1 read off.)
- `coef.cpp` (element-node values → Chebyshev coefficients), `tables.py` (P-APPC's printed blocks with line checks
  and block sums, read back and verified; page counts), `evalres.cpp` (the residual of a printed or unquantized
  approximant at sample points, partition of unity included, dd or qd), `post.py`, `rates.py`, `jetcheck.py`,
  `cert3.py` (P-APPC prop:appc-element-bound from the printed integers, FLINT integer matrices for the exact
  re-expansions, slab-wise ball arithmetic; reproduces N-APP1's stand-in bound 5.889e-4 for element (2,2) in 2.4 min
  against 6.5), `overlapK.py` (prop:appc-overlap for derivative orders ≤ K with (K + 2)-jets: derivative-majorant
  arithmetic, exact strip coefficients of the difference polynomials, the seed's derivatives by bivariate Taylor
  arithmetic in balls; at K = 0 it reproduces N-APP1's overlap.py within a factor 3–10, being more conservative),
  `overlap2.py`/`cert2.py` (N-APP1's procedures with one quantum per block; reproduce N-APP1 exactly); `certsum.py`
  sums an element's certificate B = own + Λ per derivative order).

## 2. Validation

**(a) Against the record (computed; `validation/record_s2A.txt`).** The pilot against the Richardson combination
(4F₅₂₈ − F₂₆₄)/3 of dnsolve5.py at M = 16, by u-bands over D_A (60 random points each, all x-nodes):

| u-band | R | m | n | W | s | record's own |F₅₂₈ − F₂₆₄| (m) |
|---|---|---|---|---|---|---|
| [−10, −8] | 3.6e-7 | 5.6e-7 | 9.6e-7 | 2.4e-7 | 1.4e-8 | 7.1e-8 |
| [−8, −6] | 3.1e-8 | 9.0e-8 | 4.0e-8 | 6.1e-8 | 9.1e-9 | 2.8e-7 |
| [−6, −4] | 3.4e-8 | 1.1e-7 | 1.3e-7 | 1.2e-7 | 1.6e-8 | 8.7e-7 |
| [−4, −3] | 8.5e-8 | 2.1e-7 | 2.5e-7 | 1.9e-7 | 2.2e-8 | 5.7e-6 |
| [−3, −2] | 1.9e-7 | 4.5e-7 | 4.6e-7 | 2.7e-7 | 6.9e-8 | 1.6e-5 |

Within the record's discretization error except in the first band, where the record's M = 16 angular truncation
(not in its 528/264 estimate) is the larger (the M = 24 run agrees with the solver to 8e-7 there). A first
comparison showed a v-independent R offset of 5e-5: an artefact of cubic interpolation of the record in ξ, removed
by subtracting the interpolant at v = ½.

**(b) Convergence (computed; `validation/convergence.txt`, `validation/rates_s2A.txt`).**
- Degree (first three columns, u ∈ [−10, −8.9], 30 × 30 cells): p_ξ/p_v 10/12 → 12/16 lowers the error from 4e-16 to
  1.3e-22 (relative, R): ≈ 30× per unit of p_v. Cell size at p_v = 16: 30 → 45 rows lowers it by 1300 ≈ 1.5^17.7,
  i.e. h^(p+1). The pilot (16/24) is beyond the dd floor in the cells.
- Angle: M = 40 → 56 → 80: 1e-15 → 1e-21 → ≈ 1e-30 (relative), ρ_x = 2.37 (the data's bound is 1 + √2 = 2.414).
- Element coefficients (geometric fits over 25–30 decades; S-APP's in brackets, its 2 × 2 equal-split layout):

| element | ρ_t | ρ_σ | ρ_x |
|---|---|---|---|
| (1,1) | 5.4–6.4 (9–21) | 2.9–3.0 (2.4–4.1) | 2.0–2.1 (2.4–2.8) |
| (1,2) | 3.7–4.1 (5–21) | 3.0 (2.5–4.1) | 2.0–2.2 (2.4–2.8) |
| (2,1) | 5.4–6.6 (8–21) | 2.1–2.7 (2.4–3.5) | 1.7 (2.4–3.7) |
| (2,2) | 4.5–5.2 (5–20) | 2.7–2.8 (2.5–3.6) | 2.3–2.4 (2.3–3.2) |

  ρ_σ is within S-APP's ±30 % except element (2,1) (m −38 %); ρ_t and ρ_x are 20–50 % slower than S-APP's. S-APP's
  x-rates above 2.414 cannot persist (they were fitted over 10 decades of M = 24 runs); the elements (2,1) and
  (1,1) are slowed by their box extensions below v = ½ (§7.1). S-APP's risk 1 (slower decay → more pages) is
  realised: §4.
- The qd solver at the pilot's resolution agrees with the dd pilot to ≈ 1e-28 relative (m, n) on the first column:
  the dd pilot's own accuracy.

**(c) The axis-regular residual at test points (computed, dd; `validation/residual_s2A.txt`).** max_ab |f̃_ab|,
1960 points (7 × 7 per element use box, 6 random x plus x = ±1, ±0.999):

| approximant | max | median | worst element |
|---|---|---|---|
| unquantized (solver's coefficients) | 8.3e-26 | 8.5e-28 | (2,2), at (u, v, x) = (−2, 3.5, −1), f_nn |
| printed, p = 30 | 1.8e-19 | 5.2e-23 | (1,2) |
| printed, p = 32, 33, 31, 32 | 2.0e-22 | 6.3e-25 | (1,2) |
| printed, p = 32, 34, 32, 33 | 1.3e-22 | 1.1e-25 | (1,1), (1,2) |
| printed, p = 27 / 29 / 31 | 1.4e-16 / 8.1e-19 / 1.5e-20 | | (1,2) |

  The printed residual is ≈ 1e11 × quantum in max and 1e7 × in median (N-APP1 measured 9 decades on its stand-in).

**The jets on N₀⁺ (computed; `validation/jets_s2A.txt`).** The pilot's approximant carries the development's
v-jets through G (κ = 4). Against the transport hierarchy (45-digit comparison, interior of the ξ-elements):
order 4: ≤ 5e-28 (m), 1.5e-29 (n), ~1e-31 for R, W, s (whose order-4 jets vanish, as does R's order-5 jet: the
hierarchy gives 0 there); order 5: ≤ 1e-25 (m), 6e-27 (n); order 6: ≤ 9e-24; order 7: ≤ 1.5e-21. So for level 4
(orders 4–5) the carried jets agree with the transport to ≤ 1e-25 — the size of the jets' error that stands beside
δ_w (computed; not an enclosure, §5);
level 6 (orders 4–7) to ≤ 2e-21. The hierarchy itself agrees with the solver's first-row cells to the same level.
A reference part with κ = N + 2 (separate jet tables and G_κ = (F − F_ref)/(v − ½)^κ) is ill-conditioned near N₀
unless G_κ is produced in the first-row cells against the hierarchy's jets; in qd that is feasible (the
inconsistency of the hierarchy's jets is ~1e-60), in dd it is not; not built.

## 3. Runs

| case | precision | resolution | cells | time (4 cores) | status |
|---|---|---|---|---|---|
| seed 2, D_A (pilot) | dd | M = 80, p 16/24, 30 × 30 (+ Q2–Q4 31) | 961 | 66 min cell time (≈ 2 min/column alone) | done |
| seed 1, D_A | qd | M = 92, p 16/24, 30 × 30 (+ 31), both layouts sampled | 961 | 5 of 30 Q1 columns in 103 min (load 9–10 on 4 cores) → ≈ 9–10 h under that load, 6–7 h alone | running (PID 22070), checkpoint every 20 min |
| seed 2, D* | qd | M = 100, p 16/24, 62 × 30 (+ 2 + 31 + 2) | ≈ 1,990 | ≈ 14 h projected | config written, not run |
| seed 2, D_A | qd | M = 92, p 16/24 | 961 | ≈ 7 h projected | config written, not run |
| seed 1, D* | — | — | — | — | not run, as instructed (§8) |

The dd seed 1 D_A and seed 2 D* runs of the original brief were replaced by the qd production (the coordinator's
update): the pilot validates the pipeline; the level-4 targets of G0c are beyond dd except seed 2 D_A.

**When seed 1 D_A finishes** (`s1A.log` ends with `DONE`; if the process is interrupted, rerun `../solver_qd s1A.cfg`
in `bsolv/s1A_qd/` and it resumes from `s1A.ckpt`; `$SOL` = research/warp-drive/paper/reader/solver):

    cd bsolv/s1A_qd && ../coef_qd s1A.elem s1A.coef                      # ≈ 30 min (8 elements, qd)
    python3 $SOL/tables.py s1A s1A.coef tab_P P P P P P                 # or e<p11>/<p12>/<p21>/<p22>
    EVALRES=../evalres_qd python3 $SOL/post.py s1A s1A.coef post "P,..." 7  # residual of the printed tables
    python3 $SOL/rates.py s1A s1A.coef <S-APP rates> rates.json; python3 $SOL/jetcheck.py ...
    cert3.py / overlapK.py / certsum.py as in §5 (ρ per element from `cert3.py --majorant`)

The qd path was checked on a one-column qd run as far as the tables' integers (the coefficient transform of a qd
`.elem`, 8 min for four elements under load; the four-part coefficients read and quantized exactly at p = 40); the
printing, read-back and certification code is precision-independent (Python integers). `tables.py` and the certification print and certify P-APPC's
layout (the `.elem`'s elements 1–4); layout B (elements 5–8, §7.1) is sampled but printing it needs its boxes in
`napp1/rep.py`'s layouts, i.e. a change of def:appc-layouts, which is the editors' decision.

## 4. Tables and page counts (pilot, P-APPC's layout, 79 lines × 121 characters)

| quanta (elements 11, 12, 21, 22) | entries | lines | pages | text size |
|---|---|---|---|---|
| 26, 26, 26, 26 (≈ level-3 target /10) | 1,062,231 | 83,095 | 1,052 | 9.8 MB |
| 27 uniform | 1,215,085 | 97,669 | 1,236 | 11.5 MB |
| 30 uniform (certifiable, §5) | 1,747,576 | 152,593 | 1,932 | 18.1 MB |
| 32, 33, 31, 32 (dd noise excluded) | 2,161,619 | 197,906 | 2,505 | 23.5 MB |
| 32, 34, 32, 33 (max 1.3e-22) | 2,478,499 | 223,023 | 2,823 | 26.5 MB |

Every block was printed and read back with all line checks and block sums verified. Against S-APP's 425 pages
(worst-case rule) at the level-3 target, the level-3 equivalent here is ≈ 1,050 pages: x-degree 80 everywhere
(slower x-decay than S-APP assumed), σ-degrees up to 144 in the elements whose boxes extend below v = ½, and rows
printed with interior zeros (fill ≈ 37 % of the box against S-APP's staircase 17.5 %). Above p ≈ 31 the dd noise
plateau is printed too (degrees 96 in t for m, n); qd tables at the same quanta would be smaller.
**Format**: at p ≳ 30 the block sums are ~p-digit integers and the line "S1 = …,  S2 = …,  S0 = …" exceeds 121
characters; `tables.py` sets them one per line (P-APPC sec:appc-format has them on one line).

## 5. Certification (pilot, p = 30 tables; level 0 and orders ≤ 4)

From the printed integers of the p = 30 tables (1,932 pages): `cert3.py` (prop:appc-element-bound, the element's own
residual on its use box, 192-bit balls), `overlapK.py` (prop:appc-overlap on every transition strip, derivative orders
≤ K = 4 with 6-jets, 256-bit balls; slivers of width < 1/1000 that lie outside U_ij dropped), `certsum.py` for the
sums. All **certified**; curvature units; derivatives in the element's (t, σ, x) as in eq:appc-certificate. Files:
`validation/cert_s2A_p30.txt`.

B_k = own + Λ, the largest over the multi-indices |α| = k and the eight components ab:

| element | N; ρ; M; nodes; time (1 core) | k = 0 | k = 1 | k = 2 | k = 3 | k = 4 |
|---|---|---|---|---|---|---|
| (1,1) | (68,152,205); (2.5,1.5,1.35); 3.9e5; 2.17M; 17 min | 6.4e-19 + 5.5e-16 | 7.8e-15 + 4.6e-13 | 1.1e-10 + 3.1e-10 | 9.5e-7 + 1.7e-7 | 6.0e-3 + 8.8e-5 |
| (1,2) | (85,144,173); (2,1.5,1.4); 7.7e5; 2.17M; 16 min | 2.5e-17 + 9.9e-16 | 3.1e-13 + 6.6e-13 | 3.2e-9 + 3.8e-10 | 2.0e-5 + 1.9e-7 | 8.8e-2 + 8.4e-5 |
| (2,1) | (88,151,182); (2,1.5,1.4); 1.0e6; 2.48M; 18 min | 1.8e-18 + 1.5e-16 | 2.2e-14 + 1.5e-13 | 2.5e-10 + 1.4e-10 | 1.7e-6 + 1.2e-7 | 8.4e-3 + 8.8e-5 |
| (2,2) | (72,141,194); (2.5,1.6,1.4); 2.6e8; 2.02M; 15 min | 3.6e-18 + 9.9e-16 | 8.1e-14 + 6.6e-13 | 1.1e-9 + 3.8e-10 | 8.2e-6 + 1.9e-7 | 4.6e-2 + 8.4e-5 |
| **whole use region, max** | | **1.0e-15** | 9.7e-13 | 3.5e-9 | 2.0e-5 | 8.8e-2 |

**Against the targets** (seed 2, D_A; the element targets f_ij = f e^(φ_ij/2) ≥ f, so comparing with f is safe):
- **Level 0**: 1.0e-15 = 10^−15.0 everywhere. G0b's level-3 target 10^−14.6: **met** (by 0.4 decade, at level 0).
  P-APPC sec:appc-outcomes' f = 10^−16.6: **not met** (1.6 decades over). G0c's level-4 10^−20.9: **not met**, and not
  reachable from these tables at all (their residual at the sample points is already 1.8e-19).
- **Derivatives**, weighted by μ^(k/2) as an indication only (the norm weights the Lie derivatives ℒ^I, combinations of
  these derivatives with f_ab and the fields' jets, pending:lem-tl5-f3-residual; (u, v)-derivatives differ from
  (t, σ)-derivatives by chart factors 0.2–1.8 per order): max over k ≤ 3 at μ = 1e-3, 3.6e-11 / 6.3e-10 / 5.8e-11 /
  2.7e-10 (elements 11, 12, 21, 22) against 10^−14.6, **not met by 5.4 decades**; max over k ≤ 4 at μ = 1e-4 (G0c's μ
  for seed 2, D_A), 6.1e-11 / 8.8e-10 / 8.5e-11 / 4.6e-10 against 10^−20.9, **not met by 11.8 decades**.

**What limits it** (computed from the same runs):
- **The own bounds are tail-dominated at every order.** The interpolant part Σ|c^(ab,α)| is 5e-20–4e-18 at k = 0 and
  1.7e-8–2.6e-7 at k = 4; the tails E_α are 4e-19–2e-17 and 6e-3–9e-2. E_α grows like N^(2|α|)ρ^(−N): with N → ∞ the
  own bounds would fall to the Σ|c| column (k = 4 weighted at μ = 1e-4: 1.7e-16–2.6e-15). For k = 4 at the Σ|c| level
  element (2,2) needs N ≈ (104, 202, 280) (≈ 6M nodes, ≈ 45 min; cert3 is linear in the nodes).
- **The overlaps are not tail-limited**, and with N → ∞ they bind: μ^(3/2)Λ₃ ≈ 6e-12 at μ = 1e-3. Λ is linear in
  the mismatch of neighbouring elements on the strips, and that mismatch is the tables' own truncation: on the dominant
  strip of (2,2), sup|G_12 − G_22| = 2e-28 at p = 30 (≈ 200 quanta, ~10⁶ dropped or rounded coefficients), carried
  mostly by the high x-modes (sup |∂_x²| = 3.9e-22, sup |∂_x⁴| = 2.3e-16; computed, §7.3). **Λ falls with the quantum**:
  at p ≈ 40, Λ₀ ≈ 1e-25 and μ²Λ₄ ≈ 1e-22 (μ = 1e-4), below a tenth of G0c's target (deduced, linear scaling, if
  the qd tables' mismatch is set by their quantum as the dd tables' is). Seed 2 D_A at p ≈ 40: ≈ 4,400 pages
  (the pilot's 1,932 at p = 30 plus ≈ 250 per decade; deduced).
- **Double-double forbids p ≈ 40**: the dd coefficients plateau at ≈ 1e-33 and tables printed at p > 31 make the
  majorant M explode (§7.2). The qd production's tables are the ones to certify for level 4.

**The jets of the printed tables** (computed, 45 digits; `validation/jets_s2A.txt`): the p = 30 tables carry the
v-jets on N₀⁺ against the transport hierarchy to ≤ 3.1e-28 at order 4 (m; R and W, whose exact order-4 jets vanish,
1.2e-28 and 1.9e-28 — the quantization, against 2e-31 unquantized), ≤ 5.6e-26 at order 5, ≤ 3.1e-24 at order 6,
≤ 4.4e-22 at order 7. These are differences of floating evaluations, not enclosures; a certified enclosure (the
hierarchy in ball arithmetic beside cert3) is not built.

**Cost**: 15–18 min per element at 2.0–2.5M nodes on one core (four elements 66 min), 1–2 min per strip for the
overlaps (all strips of an element ≈ 4–5 min).

## 6. Costs

- dd pilot: 961 cells, 3,974 s of cell time; per cell ≈ 4 s (34k nodes): 4 outer residuals (≈ 0.4 s each) and
  ≈ 90 inner double sweeps (≈ 30 ms each).
- qd at M = 92, p 18/26: the qd residual ≈ 8 s per evaluation on 4 threads (47.7k nodes: ≈ 500 µs per node in
  difference arithmetic, ≈ 30 % in the x-derivative products); inner sweeps ≈ 1 s per outer step. With the first
  three outer steps in dd and the stop at 1e-39: ≈ 20–28 s per cell alone. **Measured in production** (seed 1, D_A,
  M = 92, p 16/24, element nodes 112 × 160 × 93 for eight elements): columns of 30 cells in 826, 1,579, 1,355 and 908 s
  (28–53 s per cell) with the machine's load average at 9–10 on 4 cores (other agents' jobs and the certification);
  the outer iteration settles at updates ≈ 1e-40 (relative), the cells that stop there against tol 1e-44 are logged.
- Projections: seed 2 or seed 1 on D_A ≈ 6–7 h; seed 2 on D* ≈ 13–14 h (twice the columns); seed 1 on D* at
  M ≈ 160–190 (its x-rate 1.6–1.9 near u*) ≈ 3–5 × seed 2 D*, ≈ 40–70 h on 4 cores in qd.
- Certification (cert3, python-flint, one core): measured 15–18 min per element at 2.0–2.5M nodes (the pilot's
  p = 30 tables, §5); linear in the nodes. Level 4 at the qd targets: ≈ 6M nodes per element (≈ 45 min) if the qd
  coefficients decay as the pilot's (larger ρ, fewer nodes, if they decay faster). Overlaps (overlapK): 1–2 min per
  strip, ≈ 4–5 min per element.

## 7. Findings that bear on P-APPC and S-APP

1. **The side-quadrant extensions.** def:appc-layouts lets the boxes of the elements (1, ·) extend to u ≈ −10.6 and
   those of (·, 1) to v = 0.4145. There the polynomial must represent the analytic continuation of the solution into
   the quadrants {u < −10, v > ½} and {u > −10, v < ½} of the characteristic problem, where the Riemann function of
   an angular mode l is I₀(2l√|ΔuΔv|) rather than J₀ (deduced): angular structure grows like e^(2l√|ΔuΔv|).
   Measured (m): ρ_x = 2.24 at (−10.59, 1), 1.73 at (−10.59, 3.58); 1.99 at (−5, 0.4145), 1.75 at (−3, 0.4145),
   **1.52 at (−1.94, 0.4145) with |c₈₀| = 1e-20**, against |c₈₀| ≤ 1e-31 throughout the region itself. For seed 2 D*
   (u to −1.09 and −11.26) it is worse. Resolving the continuation needs M ≈ 160–170 for those elements and raises
   their σ-degrees (144 in the pilot); boxes that start at u = −10 and v = ½ (no inner nine tenths on those two
   edges; the endpoint Markov factor there instead of the interior Bernstein factor) remove the problem. The qd
   runs sample both layouts ("layout B": ξ from −9.105, v from ½ at those edges) so either can be printed.
2. **Double-double noise and Method B.** The dd coefficients plateau at ≈ 1e-33 (absolute). Printed with quanta
   below it, the noise sits at high degree in two directions at once and the polyellipse majorant explodes
   (10¹⁰ in the weighted sums at ρ = (2, 1.6, 1.6)); certifiable dd tables need p ≤ 30–31, i.e. a residual
   ≈ 1e-19 (pilot): enough for level 3, not for level 4. This is N-APP1's §9.2 in numbers.
3. **The overlaps at order K.** prop:appc-overlap multiplies the mismatch of neighbouring elements on the strips by
   the partition's derivatives up to order K + 2 (φ₆/(2d)⁶ ≈ 4e12 in ξ, 4e13 in v). With the mismatch bounded by
   coefficient sums of the exact difference polynomial (≈ 7e-25 in F at p = 30), the certified Λ is ≈ 1e-15 at level 0
   and ≈ 1e-4 at order 4 (all four elements, §5) — above the elements' own residuals by 1–3 decades at level 0.
   **Measured lever** (computed: the exact strip coefficients of G_12 − G_22 at 256 bits, evaluated on a 63 × 63 × 161
   grid of the dominant strip of (2,2), all five fields): the coefficient sums exceed the sup of the difference by
   ×39–44 for the values, ×24–43 for first and second t- and σ-derivatives, but only **×5–8 for the first and second
   x-derivatives and ×4–6 at ∂_x⁴**,
   which carry Λ at the orders that bind. A certified sup by interpolation at nodes pays a Lebesgue constant (≈ 74 for
   the tensor grid at these degrees, more for derivatives), which cancels that gain: sharper bounds of the difference
   polynomial are not the lever. The lever that works is **the quantum**: the mismatch is the tables' truncation (≈ 200 quanta), and Λ is linear in it.
   Wider transitions d (Λ_k ∝ d^(−k−2) at the top orders) and the μ^(|I|/2) weights of the level-K norm are the others.
4. **Page counts**: ≈ 2.5 × S-APP's at the level-3 equivalent (§4); x needs 80+ modes everywhere.
5. **Header format** at p ≳ 30 (§4).

## 8. What remains for seed 1 on D*

Not run (decision pending). G0c puts its level-4 target at f ≈ 10^−29.0, at the end of qd's reach; G0e (today) at
10^−52.2, beyond it. On the solver side, at G0c's target (deduced from the measured rates and costs):
- qd, M ≈ 160–190 (x-rate 1.6–1.9 near u*), 61 × 30 cells or smaller (the inner Picard's stiffness grows with M²:
  ≈ 1.5× the sweeps), p 16/24 or 18/26; layout B (§7.1), since P-APPC's side-quadrant boxes reach u ≈ −10.83 and
  −1.09 where the continuation is worst; ≈ 40–70 h on 4 cores without other load (≈ 1.5× that under the present
  load), checkpointed and resumable as the other runs.
- Tables at p ≈ 40–45 (the overlap term falls linearly with the quantum, §5): ≈ 15,000–20,000 pages (deduced,
  rough: S-APP's ratio 1,740/425 = 4.1 to seed 2 D_A at level 3, applied to the pilot's 1,932 pages at p = 30 and its
  ≈ 250 pages per decade of quantum).
- Certification at f ≈ 1e-30 with Method B: N ≈ 200–300 per direction (10⁷ nodes per element, ≈ 1.5–2 h per element
  in cert3) unless the qd coefficients decay fast enough to allow larger ρ.
- The jets on N₀⁺ to order 5 (level 4): the hierarchy in qd is consistent to ~1e-60; the carried jets of a qd run
  are measured against it with `jetcheck.py`.

## 9. Files

Code and small files: `research/warp-drive/paper/reader/solver/` (README.md; derive/gen/gen_res, rhs_gen.h,
res_gen.h, dd.h, qd.h, real.h, diff.h, solver.cpp, jets.cpp, coef.cpp, evalres.cpp, consts.py, mkcfg.py, bsio.py,
approx.py, tables.py, post.py, rates.py, jetcheck.py, cert2.py, cert3.py, overlap2.py, overlapK.py, certsum.py,
seedtower.py, regform.py; napp1/ = N-APP1's rep, cert, majorant, overlap, regform copied unchanged so that the
directory is self-contained; validation/*.txt, among them cert_s2A_p30.txt).

Large outputs (scratchpad `bsolv/`; sizes):

| path (under scratchpad/bsolv/) | size | content |
|---|---|---|
| s2A_dd/s2A_merged.elem | 365 MB | pilot: G at the element boxes' Lobatto nodes (96 × 144 × 80), all four elements, dd |
| s2A_dd/s2A.coef | 365 MB | pilot: Chebyshev coefficients (dd), the source of every table |
| s2A_dd/s2A.ckpt | 395 MB | pilot: final checkpoint (resume state; not needed any more) |
| s2A_dd/s2A.elem | 365 MB | pilot as run (one node line per element of row 1 unfilled; superseded by _merged) |
| s2A_dd/s2A.jets, s2A_hier.bin | 31 MB, 21 MB | jets on N₀⁺: from the cells, and from the transport hierarchy |
| s2A_dd/tab_{26,27,30,n,e}_tables.txt | 10, 12, 18, 23, 27 MB | the printed tables (quanta of §4) |
| s2A_dd/tab_*_z.pkl, tab_*.json | 8–29 MB, 4 kB | the integers (for the certification) and the block statistics |
| s2A_dd/cert/, lever/ | 0.2 MB | certification logs and JSON (cert3, overlapK, certsum; copied to validation/) |
| s1A_qd/ | 2.1 GB now (≈ 5.4 GB at the end: .ckpt and .elem of 8 elements, qd) | seed 1 D_A production, running |
| conv/, qcheck/ | 245 MB, 0.7 GB | convergence study and the qd/dd consistency check (both can go) |
| s2A_qd/, s2D_qd/ | configs | ready to run (`../solver_qd s2D.cfg`) |
