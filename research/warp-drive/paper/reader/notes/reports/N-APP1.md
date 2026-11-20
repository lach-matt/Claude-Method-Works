# N-APP1: the certified approximant, phase 1 (seed 2 D_A as pipeline test, then seed 1 D_A)

Report only. I wrote proofs/P-APPC.md (new) and files under scratchpad/napp1/; nothing in chapters/, crosswalk/ or
PAPER.md; no commit; nothing under method/, drive/, extracted/ or recovered/ read. Labels: **computed** (mine, scripts
in scratchpad/napp1/), **deduced** (an argument here), **record** (S-APP, G0, G0b, P-HF, chapter 87).

## 0. Status in one paragraph

The representation, the format with its checks, the axis-regular residual, and a rigorous certification procedure are
built and written up, for both seeds and all four cases, with the seed, region, layout, contact order κ and certificate
order K as parameters. **The coefficients at the target precision are not computed**: no solver exists that reaches
10⁻²⁷–10⁻³⁰ in the coefficients, and building one is multi-day work (§6). I measured its cost and stopped there, as the
brief asks. Instead the whole pipeline (printing → reading back with every check → certification in ball arithmetic)
was run end to end on a **stand-in** (G0/G0b's double-precision solution, refitted in the printed form) for seed 2's and
seed 1's D_A: it certifies 2.8 × 10⁻² to 5.2 × 10⁻¹ on the whole use regions of the four upper elements (the elements' own
residuals 6 × 10⁻⁴ to 4 × 10⁻², the rest from the overlaps), the stand-in's own level, and it showed
three places where S-APP's plan had to change (§9). The bootstrap update (level N ≥ 6) is addressed in §8: the size
model now takes N as a parameter, and hypothesis (a) of thm:tl5-hf cannot be met by any seed form (v − ½)^κ G.

## 1. What was computed

1. **Axis-regular residual** (P-APPC lem:appc-regular). Every component of eq:tl5-components, with f_lx, f_nx divided by
   √(1 − x²), equals an expression in which the only divisions are by R, Ω², e^S and 2, 3, 4, 8. Verified (computed):
   - symbolically: the regular scheme minus the chapter's formula simplifies to 0 identically, all eight components;
   - independently: against Ric of the 5D metric computed from scratch, at x = 0.3, −0.97, 0.999, agreement to 10⁻³⁸;
   - after cancellation each component is a polynomial in x and the 2-jets over a monomial in R, e^S, Ω² (no (1 ± x));
     f_lx and f_nx carry exactly one factor √(1 − x²) (they vanish at the axes);
   - the formula has 647 operations after common-subexpression elimination.
2. **The regular evolution system** (for a future solver; deduced and verified symbolically). The record's solver solves
   f_11, f_22, f_xx, f_ln for (R, m, n, W)_uv: that 4 × 4 system has determinant ∝ (1 − x²), degenerate at the axes (the
   record's D352/D354 axis loss). (f_11 − f_xx)/(1 + x) and (f_22 − f_xx)/(1 − x) are polynomials (f_11 − f_xx vanishes
   identically at x = −1, f_22 − f_xx at x = +1) and the resulting system is nondegenerate at both axes.
3. **The representation** (rep.py, P-APPC def:appc-layout to lem:appc-approximant). Rational element boxes for all four
   cases (P-APPC def:appc-layouts), each used on its inner 9/10; the partition of unity from Φ(s) = e^(−1/s)/(e^(−1/s) +
   e^(−1/(1−s))) with **rigorous** derivative bounds (computed, ball arithmetic on 20,000 intervals plus a Cauchy estimate):
   sup|Φ^(k)| ≤ 1, 2, 9.853, 111.3, 2345, 8.527 × 10⁴, 7.565 × 10⁶ for k = 0, …, 6; the contact form
   F = F_seed + (v − ½)^κ Σ χψG.
4. **The format**: blocks, rows, line check (Σ m z_m) mod 97, block sums S1, S2, S0 = 10^p G at (1,1,1), (−1,−1,−1),
   (0,0,0). Printer and reader written; every block of every stand-in table was printed and read back with all line
   checks and block sums verified (20 blocks per D_A case, 30 for seed 1's D*).
5. **Kernel timings** (computed): the residual per node 1.05 µs in double (numpy), **24 µs in double-double** (numpy,
   relative error 7 × 10⁻²⁹ against 60-digit arithmetic), 101 µs in 192-bit balls (scalar).
6. **Angular stiffness** (computed): the linearised angular operator of the regular system on the seed, M = 84 Lobatto
   nodes, has max |λ| = 136 at u = −10, 3.1 × 10³ at u = −2, 1.5 × 10⁴ at u = −1.1, within 4 % of 4M²Ω²/R². This sets
   the solver's cell size (§6).
7. **The certification procedure** (cert.py, majorant.py, overlap.py; P-APPC sec:appc-certification): exact affine
   re-expansion of the printed polynomials on the certification box; seed by complex interval Newton with a proof of
   holomorphy (G injective on Re R > 3/2); Chebyshev–Lobatto interpolation of the residual in ball arithmetic; a
   polyellipse bound M by a **majorant** of the regular formula (one evaluation); the coefficient/aliasing bound
   E_α for all derivatives |α| ≤ K; the overlap correction Λ by a mean-value bound with exact difference polynomials.
8. **Stand-in pipeline runs** for s2A and s1A (and stand-in fits of s2D, s1D for rates).

## 2. Measured rates against S-APP's

- **No new data deeper than S-APP's.** The only solutions are G0/G0b's double-precision runs (noise floor ≈ 10⁻¹¹ of the
  amplitude); S-APP measured the rates over those ≈ 10 decades. The rates over the 26–33 decades the tables need remain
  unmeasured until a high-precision solution exists, so S-APP's risk 1 (×3.3 pages if 30 % slower) stands.
- On my exact layout the stand-in's upper elements (v ≥ 1.96) reproduce S-APP's rates within about ±20 % (computed,
  rates_napp_*.json): e.g. seed 2 D_A element (2,2): ρ_t 5–12, ρ_σ 1.8–2.6, ρ_x 2.6–3.3 (S-APP 2 × 2: 5–11, 2.3–3.6,
  2.4–3.2); seed 1 (2,2): 5.5–10, 1.7–3.4, 2.3–2.6.
- On the lower elements (v ≤ 2.04) the stand-in's rates are meaningless (ρ 1.1–1.5): the runs do not match the seed's
  3-jet on N₀ exactly (they differ from the seed by ≈ 5 × 10⁻⁵ there, record S-APP §1), and dividing by (v − ½)⁴
  turns that into large high-degree coefficients of G. This is a stand-in artefact, not a rate.

## 3. Entry and page counts (dense format, 79 × 121, S-APP's size model on S-APP's rates; my layout is S-APP's up to the
rational rounding of breakpoints)

At the present targets (G0b /10) and level 3 the model reproduces S-APP exactly (computed): worst-case / expected rule

| case | target f | entries (worst) | pages worst | pages expected | max degrees (t, σ, x) | 30 % slower decay |
|---|---|---|---|---|---|---|
| seed 1, D_A | 10^−17.5 | 0.42 × 10⁶ | 451 | 395 | 42, 56, 79 | ≈ 1,500 |
| seed 2, D_A | 10^−16.6 | 0.41 × 10⁶ | 425 | 371 | 42, 65, 74 | ≈ 1,440 |
| seed 2, D* (dd) | 10^−20.1 | 0.98 × 10⁶ | 1,158 | 1,022 | 80, 77, 88 | ≈ 3,860 |
| seed 1, D* (qd) | 10^−22.9 | 1.46 × 10⁶ | 1,740 | 1,527 | 60, 93, 134 | ≈ 5,730 |

The stand-in tables themselves (p = 13) have 217,000 entries and 246–248 pages per D_A case; that number measures the
stand-in's noise, not the target (§5).

## 4. Certified bounds per element (stand-in; targets for comparison)

Each element's bound is certified on its use interval (inner 9/10 of its box) in two parts: the element's own
polynomial approximant (P-APPC prop:appc-element-bound) and the overlap correction (prop:appc-overlap). Level 0 (sup of
max_ab |f̃_ab|), 1.2–1.4 × 10⁶ nodes, 128-bit balls, p = 13. The four upper elements have the whole chain done.

| case, element | use region (u; v) | own residual ≤ | overlap Λ ≤ (largest strip) | **certified on the whole use region** | allocated target f_e (estimate) |
|---|---|---|---|---|---|
| s2A (1,1) | [−10, −3.85]; [½, 2.04] | 2.0 × 10⁻² | not run | own part only | 10^−16.6 |
| s2A (2,1) | [−4.18, −2]; [½, 2.04] | 7.3 × 10⁻³ | not run | own part only | 10^−15.4 |
| s2A (1,2) | [−10, −3.85]; [1.96, 3.5] | 3.6 × 10⁻² | 1.7 × 10⁻¹ (v-strip) | **2.0 × 10⁻¹** | 10^−16.1 |
| s2A (2,2) | [−4.18, −2]; [1.96, 3.5] | 5.9 × 10⁻⁴ | 2.7 × 10⁻² (ξ-strip) | **2.8 × 10⁻²** | 10^−14.8 |
| s1A (1,2) | as s2A (1,2) | 3.8 × 10⁻² | 4.8 × 10⁻¹ (v-strip) | **5.2 × 10⁻¹** | 10^−16.8 |
| s1A (2,2) | as s2A (2,2) | 6.5 × 10⁻³ | 8.7 × 10⁻² (ξ-strip) | **9.4 × 10⁻²** | 10^−15.3 |
| s1A (1,1), (2,1) | lower | not run (memory, §7) | — | — | 10^−17.5, 10^−15.9 |

Strips of each upper element: one ξ-strip, one v-strip, one corner square (plus slivers of width ≤ 10⁻³ from the
outward rounding of use regions); all done. Lower elements: ρ = (1.3, 1.2, 1.6), N = (106, 120, 64); upper:
ρ = (1.3, 1.3, 1.6), N = (106, 106, 64). Floating-point samples of the stand-in's residual (diagnostic only): median
7 × 10⁻⁶, max 1.2 × 10⁻³ in the interior, 1.6 × 10⁻² near v = 7/2 and u = −10, 7 × 10⁻⁴ near v = ½. The v-strips
couple the upper elements to the lower ones, whose stand-in fits carry the v = ½ artefact (§2); that is why Λ is largest
there for the (1,2) elements. A first pass returned NaN on some strips: a single ball over a whole strip made
R_s = 3.8 ± 1.25 and R_s³ = 55 ± 74, which contains 0; the seed is now enclosed on a 48 × 8 subdivision of each strip.

- The allocated targets are f e^(φ_min/2) with G0's φ shape rescaled to G0b's totals (S-APP's estimate); the certified
  φ must come from L7 at the new level.
- The stand-in fails its targets by 12–15 decades, as it must: it is a double-precision object. What the run shows is
  that every step is a finite computation on the printed integers, that it closes (analyticity checks pass:
  Re R_seed ≥ 2.75 and Re R ≥ 2.67 on the whole polyellipse of element (2,2)), and what dominates.
- Order-3 derivative bounds at this N are ≈ 10⁷: all interpolation error (E_α grows like n^(2|α|)). For K = N ≥ 6 the
  interpolation degree must rise by about log(n^(2K)/(2K−1)!!)/log ρ per direction (§7).
- The overlap term dominates: the stand-in's neighbouring elements differ by up to 2 × 10⁻⁵ – 1.8 × 10⁻⁴ in their 2-jets
  on the strips, and the bound of ∂f̃/∂J carries ρ = R⁴/√72 ≈ 10²–10³. For the real tables this means the neighbouring elements
  must agree on the strips to about three decades below f_e (deduced): the quantum model should carry the overlap
  mismatch as a fourth error source beside omission, rounding and the interpolation tail.

## 5. The derivative loss, measured on a printed object (computed)

Rounding the same stand-in at three quanta and sampling its residual (floating point, diagnostic only): quantum 10⁻¹¹ →
residual up to 1.6 × 10⁻² (interior median 4 × 10⁻⁵); 10⁻¹³ → interior max 1.2 × 10⁻³, median 7 × 10⁻⁶; 10⁻¹⁵ → interior
median 2 × 10⁻⁶, at the stand-in's own floor (its global interpolant: median 4 × 10⁻⁷, max 1 × 10⁻⁵). So at degrees ≤ 40
the residual sits ≈ 9 decades above the quantum, consistent with S-APP's 10–14 decades at the targets' degrees.

## 6. The solver: not built; measured cost and what shortens it

**Design (deduced).** Characteristic cell marching: Chebyshev–Lobatto in x (M nodes, axes included, regular evolution
system of §1.2), cells in (u, v) of local degree p with Picard sweeps (exact double Chebyshev integration), Goursat data
from the cell's past edges; N₁ data from the Raychaudhuri ODE (prop:cone-exact) and the shift ODE (f_lx = 0 along v),
N₀ the seed; G on the lower v-elements taken from a Taylor expansion in v − ½ on the first cell row (division by
(v − ½)⁴ of a solution sampled at nodes amplifies errors like n⁸, §9).

**Measured inputs.** Picard needs λ h_u h_v ≲ 2 with λ = 4M²Ω²/R² (measured); p = 16, M = 80 (D_A), 92 (seed 2 D*), 140
(seed 1 D*); 20 sweeps per cell; cost per node-sweep 50 µs numpy-dd (measured kernel + x-derivatives), 8 µs compiled dd,
40 µs compiled quad-double (estimated from operation counts).

| case | cells | node-sweeps | single-core hours, numpy-dd | compiled dd | compiled qd | wall time on 4 cores |
|---|---|---|---|---|---|---|
| seed 1, D_A | 5.7 × 10³ | 2.7 × 10⁹ | 37 | 6 | 29 | **≈ 1.5 h (dd)** |
| seed 2, D_A | 5.7 × 10³ | 2.7 × 10⁹ | 37 | 6 | 29 | **≈ 1.5 h (dd)** |
| seed 2, D* | 1.7 × 10⁴ | 8.8 × 10⁹ | 122 | 20 | 98 | **≈ 5 h (dd)** |
| seed 1, D* | 3.8 × 10⁴ | 3.1 × 10¹⁰ | 431 | 69 | 345 | **≈ 86 h (qd)** |

At level N ≥ 6 the degrees grow by 2–4 per direction (§8): +10–20 % on these.

**Development**, not run time, is the obstacle: a compiled double-double cell solver with the regular system, the N₁
data ODEs, a backward solve to u ≈ −10.6 for the enlarged boxes (or no enlargement at u = −10), and validation to 10⁻²⁸
is several days of work (S-H123 estimated 1–2 person-months for a spectral solver). **What would shorten it:** (i)
compiled code (×6 over numpy), (ii) implicit treatment of the angular operator per cell (diagonalised once per cell row)
so cells are set by the solution's smoothness, not by λ (≈ ×5–20 fewer cells), (iii) defect correction: double-precision
linear solves for the corrections with the residual in double-double (each sweep gains ≈ 6 digits), (iv) not enlarging
boxes at u = −10 and v = ½ (no backward solve; costs some interior lever).

## 7. Certification cost (measured on the stand-in; projected)

- Measured: 1.2 × 10⁶ nodes per element, 128-bit balls: ≈ 6.5 min and 4.5 GB per element (fields 50 s, residual at nodes
  160 s, transform 28 s, majorant 20 s, bounds 130 s); overlap correction ≈ 5–15 min per element.
- At the targets, with ρ ≈ 2 (allowed once coefficients decay to the quantum) and K = 3: N ≈ 100–130 per direction,
  2–3 × 10⁶ nodes; with K = 6 about 130–180 (Markov factors) or 110–150 (with interior Bernstein factors on an enlarged
  interpolation box): 2–6 × 10⁶ nodes, 20–60 min and 8–25 GB per element at 192–256 bits in the present code. It must be
  restructured (chunked node evaluation; derivative maps as matrix products) to fit memory. Projected: seed 1 or 2 D_A
  ≈ 2–4 h; seed 2 D* ≈ 4–8 h; seed 1 D* ≈ 8–15 h (6 elements, 256 bits).

## 8. The bootstrap at level N ≥ 6 (coordinator's message)

**(1) Norm order.** The certificate's order K is a parameter (cert.py K; P-APPC eq:appc-certificate, |α| ≤ K): it
outputs bounds of all (t, σ, x)-derivatives of order ≤ K of the regular components, from which the level-N source
s_N[2R̂ic] of P-HF's def:tl5-hf-constants follows by the conversion still to be written (pending:lem-tl5-f3-residual;
only the chart factors and the commutation fields' components enter). The size model with the commutation weights up to
level N, at the **present** targets and μ (computed; worst-case pages, expected in brackets):

| case | N = 3 | 4 | 5 | 6 | 7 | 8 | per level |
|---|---|---|---|---|---|---|---|
| seed 2, D_A | 425 (371) | 463 | 508 | **558 (498)** | 616 | 681 | +9–10 % |
| seed 1, D_A | 451 (395) | 488 | 530 | **577 (515)** | 631 | 691 | +8–10 % |
| seed 2, D* | 1,158 (1,022) | 1,283 | 1,426 | **1,588 (1,429)** | 1,773 | 1,982 | +10–12 % |
| seed 1, D* | 1,740 (1,527) | 1,810 | 1,890 | **1,982 (1,770)** | 2,085 | 2,202 | +4–5 % (μ = 10⁻⁴) |

Entries at N = 6: 0.50, 0.51, 1.26, 1.62 × 10⁶; degrees rise by 1–2 per level. The new targets of G0c will move these by
≈ 12–17 % per decade of f (S-APP §0.2), and a different μ moves the per-level factor (it enters as μ^(l/2)).

**(2) Contact order on N₀: (v − ½)^κ G with a higher κ does not satisfy hypothesis (a)** (deduced). The solution agrees
with the seed on N₀ only to order 3 in v: at order (v − ½)³ the equations reduce to a linear system ∂_u a = 𝔄 a for the
fourth v-derivatives a = (a_R, a_W, a_m, a_n, a_s) along N₀ (terms without a v-derivative, and products of differences,
are O((v − ½)⁴); at order (v − ½)² the shift equation f_lx contains only R s_vv/(8e^SΩ²), so a_s = 0, and then the
only x-derivative of a perturbation that could enter the uv-equations at order (v − ½)³, through s_vx in L(k̲) and E(τ),
is absent, so the system is pointwise in x; this is read off the term structure of lem:appc-regular by hand, not by a
separate computation), with a(−10, x) ≠ 0 from env = (π/3)⁴(v − ½)⁴ + O((v − ½)⁶) (at seed 1
a_m ∝ cos(½) h(x); at seed 2 a_n ∝ sin(½√10) h(x)); so a(u, ·) ≢ 0 along N₀. Any approximant equal to the seed to order
κ − 1 ≥ 4 on N₀ therefore differs from G^♯ at order 4, and with the seed reference κ > 4 does not even give smooth
fields. Two ways out, for the P-HF writer to choose: (i) weaken (a) to a certified mismatch on N₀ entered as a data flux
beside δ_w (then κ = 4 stays and the mismatch is G's error in representing the orders 4..N + 1); (ii) a reference part
carrying the solution's v-derivatives of orders 4..N + 1 on N₀, defined by these transport equations and enclosed like
the N₁ data (then κ = N + 2). P-APPC makes κ a parameter (rem:appc-contact) and records this in its Placement 3a.
**Cost of κ:** with (ii) and exact (equation-defined) jets, no extra entries (G's amplitude and quantum both scale by
(v − ½)^(4−κ)); printing the jets instead as 2D tables per ξ-element would add (κ − 4) tables of ≈ 1,800 entries per field
and ξ-element, ≈ +15 % entries at κ = 8 on D_A, and would still not give exact contact.

**(3) Targets**: everything above is at G0b's level-3 targets; the pipeline takes f, μ, N, κ as inputs.

## 9. What S-APP assumed that changed (with numbers)

1. **The polyellipse step.** S-APP §5 4(B): "enclosed by covering the polyellipse with complex boxes". Direct ball
   evaluation of the formula on a covering of the distinguished boundary fails: at 64 × 48 × 24 arcs it gave M = 4 × 10³⁴
   on element (2,2) and could not show Re R > 0 on element (1,2) (min −93). Replaced by a majorant (P-APPC
   lem:appc-majorant), one evaluation: M = 1.4 × 10⁵ at ρ = (1.3, 1.3, 1.6), 3.4 × 10⁸ at (1.5, 1.5, 2), 7.8 × 10¹³ at
   (2, 1.6, 2) (computed, element (2,2)). The majorant needs (v − ½)⁴G formed as one exact polynomial: bounding the two
   factors separately overestimates by 50–90×.
2. **Method B's cost depends on the coefficients decaying to the quantum.** The stand-in's coefficients plateau near the
   quantum out to the top degree, forcing ρ ≈ 1.2–1.3 and N ≈ 106; a converged solution printed on the staircase allows
   ρ near the solution's rates. The solver must deliver geometrically decaying coefficients.
3. **Seed subtraction** needs the solver to produce G directly near N₀: dividing node values by (v − ½)⁴ amplifies errors
   ≈ n⁸ and, on the stand-in, leaves a residual of 7 × 10⁻⁴ near v = ½ against 2 × 10⁻⁶ elsewhere.
4. **The overlaps** (S-APP risk 5) are a real error source (§4), to be budgeted.
5. **A constant I had wrong and corrected**: the seed bound |R_s| ≤ (|H| + 2.35)/2 (not + 2); the jobs were rerun.
Confirmed: the 1/(1 ± x) cancellation (exactly as S-APP said, now explicit); no x-parity; format overhead (line length
≤ 120 at p = 13).

## 10. What would make seed 1's D* closing GO (record G0b §G0b.7, plus deduced)

G0b's level-3 figure is log₁₀F₃²G = 28.05 against the GO line 25 (seed 2: 22.33, GO). Levers, untested (G0b): (i)
Gagliardo–Nirenberg interpolation for |∇²h|_∞ (1–3 decades); (ii) zeroth-order weights re-optimised with the level-N bulk
form; (iii) a pointwise |∇Z|; (iv) level-dependent μ_j; together plausibly 2–4 decades. **But P-HF now needs N ≥ 6, which
adds cross-level couplings and a larger μ^(−N/2)** (record P-HF def:tl5-hf-constants), so the level-3 numbers no longer
decide; G0c (levels 4–7) does. A fallback that the record supports: seed 1 on [−10, −1.2] × [½, 7/2] (G0b:
F₃²G = 10^23.4, GO at level 3, target f ≈ 10^−19.7, double-double), between D_A and D*. On the approximant side seed 1's
D* needs quad-double, M = 140 x-nodes (its x-rate is 1.6–1.9 near (u*, v ≥ 2), S-APP §2.1), ≈ 86 h of compiled solver
time on 4 cores, and better angular resolution data than S-APP's (M16 and M24 runs differ by 5 × 10⁻⁴ there).

## 11. proofs/P-APPC.md

- md5 f16f1515c6e46d6dcb5014f47cb90d42, 608 lines, 49 labels (app:approximant; 5 sections of text + specimen, Placement, 49 crosswalk rows).
- Contents: definitions (regions, layout, the four layouts, partition of unity with proved bounds, the printed
  approximant with contact order κ), the format and lem:appc-checks, lem:appc-regular with full proof, the certification
  (exact re-expansion, seed holomorphy, interval Newton via Brouwer, analyticity on polyellipses, majorant, coefficient
  and aliasing bound for all derivatives, element bound, overlap perturbation), the interface to the level-N norm, an
  outcomes table (all rows pending:computational-appc-*), and a specimen block (format only, pending).
- Checks: no line over 121 characters; lint.py on the appendix text together with chapters 87 and 96: 0 hits other than
  the pending markers. Pending: lem-tl5-cip-axis, lem-tl5-f3-residual, lem-tl5-l7-rates, five computational items.
- Not in the text, by the no-code ruling: anything about how coefficients are obtained.

## 12. Time

About 2 hours of session time (20:35–22:35); compute about 2 core-hours (certification runs 6.5–10 min per element,
overlap corrections 5–20 min each, size-model scans a few minutes). Projected for seed 2's D*: solver ≈ 5 h wall on 4 cores once a compiled double-double solver exists
(≈ 30 h in numpy double-double), certification ≈ 4–8 h, plus the solver's development.

## 13. Files (all under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/napp1/)

| file | what |
|---|---|
| chform.py, regform.py | the chapter's formula (symbolic) and the axis-regular scheme (any number type) |
| axisreg.py, verify_reg.py, check_ricci.py | cancellation of the poles; identity of the two schemes; 5D Ricci check |
| axisdiv.py, opcount.py, stiff.py | divisibility of f11 − fxx, operation count and uv-matrix; angular stiffness |
| rep.py | cases, layouts, partition of unity, seed, printing and reading back with checks |
| provfit.py, provfit2.py, prov*_*.npz/json/_tables.txt | stand-in sources and their printed tables |
| assemble_f.py, where.py, globres.py | float diagnostics of printed approximants (not certificates) |
| dd.py, ddtime.py, solvercost.py | double-double arrays, kernel timings, solver projection |
| cert.py, majorant.py, overlap.py, phibound.py | the certification (ball arithmetic), majorant, overlap correction, Φ bounds |
| cert_*.json/log, overlap_*.json, ov_*.log | certification outcomes |
| rates_napp.py, rates_napp_*.json | stand-in rates on the printed layout |
| levels/model.py, levels/scale.py, levels/scale_*.log | S-APP's size model with the level N as a parameter |
