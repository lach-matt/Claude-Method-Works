# Registry notes: the programs behind the reader's edition

Companion to `registry.tsv` (same directory). Read-only survey of `research/warp-drive/` at the current commit; no
repository file was modified. Paths below are relative to the research tree; the edition itself must carry none of them.

## 0. Scope and how the registry was built

- **Universe: 369 programs.** 259 are cited by the paper (body, Appendix A, C or D); all 259 are in Appendix D's md5
  table and **all 259 hash to their pinned md5 at this commit** (no drift). 286 are cited by the supplement
  (`checks/*.py` in every `.md` under `docket68/n1star/` and `proof5/`): 179 of them also by the paper, **107 by the
  supplement only**. 3 more (`lemmas/emitter_process.py`, `source_spec.py`, `src_hole.py`) are cited by neither but are
  loaded at run time by cited programs, so they are rows too (`cited_by` = import-only).
- Fields were filled from Appendix A's entries (labels, controls, runtime), Appendix C (claims), Appendix D (run-line
  runtimes, md5s), the supplement's citing headings, each program's module docstring and header, and greps for imports,
  `open(`/`read_text`/`__file__`/`sys.path`/file-path loaders and the process words. `math_gist`, `method` and `class`
  are hand-assigned from those sources; `controls` and `runtime` are hand-written where Appendix A is silent, otherwise
  taken from it (or from the docstring's `Control:`/`Mutant:` sentences). Gists were written from the docstrings, not
  from reading the code, so a few may be coarser than the program.
- An extra last column, `proposed_number`, gives each row its C-number (section 2) or S-number (shared module).
- `cleaning` carries the grade and the reason counts: process words (warp, docket, n1star, verifier, seated, D-numbers)
  and path strings split into *code/printed strings* versus *docstring/comments*, md5 pins, text reads, print lines that
  print a path or file name, subprocess, cross-directory imports, absent data.

## Hand-proof triage

Changed directive: the edition carries no code and no computation appendix, so every step a program supports must be
written out as mathematics. `registry.tsv` has two more columns for this: `hand_route` (DERIVE, ENUMERATE, ARITH,
ANALYTIC, NUMERIC-ONLY or TEXT) and `hand_estimate` (the size estimate for DERIVE, ENUMERATE and ARITH; what the new
argument must show for ANALYTIC; the numerical part for NUMERIC-ONLY; and the route of any secondary part of a mixed
program). The C- and S-numbers of section 2 are kept only as stable identifiers; the code-appendix numbering is moot.

How routes were assigned. Defaults by class and method: TEXT class gives TEXT; MEASUREMENT and float-numerical give
NUMERIC-ONLY; interval gives ANALYTIC; exact-rational gives ENUMERATE; exact-symbolic and mixed give DERIVE. About 100
programs were then set by hand from their Appendix A entries and docstrings. A mixed program takes the route of the claim
the paper relies on; its other parts are named in `hand_estimate`. Estimates are rough (a factor of about 3 either way),
computed from the effective code size (code lines without docstrings, comments or blank lines): DERIVE takes the larger
of 8 lines per cited label and 0.3 x code lines, clamped to 10-300; ENUMERATE takes 0.2 x code lines of table, clamped to
10-200; ARITH takes 0.15 x code lines, clamped to 5-120. A derivation that expands the curvature of a general metric by
hand can print far longer than this rule says.

| route | programs | program lines | estimated printed size |
| --- | ---: | ---: | --- |
| DERIVE | 221 | 75,294 | about 16,165 lines |
| ENUMERATE | 26 | 8,641 | about 1,190 table lines |
| ARITH | 19 | 5,753 | about 600 lines |
| ANALYTIC | 25 | 9,059 | - |
| NUMERIC-ONLY | 63 | 16,269 | - |
| TEXT | 15 | 3,879 | - |
| total | 369 | 118,895 | |

The estimated printed length for DERIVE, ENUMERATE and ARITH together is about 17,955 lines (16,165 + 1,190 + 600).

Where the hard routes sit:

- **Theorems 1-3 (sections 2-7) need only DERIVE and ENUMERATE**, 23 programs. The two NUMERIC-ONLY programs placed
  there, C24 and C25, support section 6's account of the numerical solution, not a step of a proof.
- **Theorem 4 (section 8) has one ANALYTIC dependency**: C87, which certifies the distance ε_ind of the indicial roots
  from the integers below l = 10^4 for Hintz's condition (8.13) at the parameter point (section 8.5). Its exact half,
  simplicity of every root for l >= 2, is C86 (DERIVE). Section 8's two NUMERIC-ONLY programs, C48 (the seed's barrier
  and scattering) and C28 T3, T5, T6 (ringdown, settling times, tail), are context. C28 T1, the fact the section rests
  on, is DERIVE.
- **Everything else ANALYTIC or NUMERIC-ONLY is in section 9 or in the supplement's rounds**, behind section 9:
  - the certified constants of the linear theory (the resolvent band bound 11.477 and the one-derivative constants);
  - the λ0 bounds (envelope and profile derivatives to order 14, ε1, the energy constant);
  - the certified Einstein residuals of the numerical approximants;
  - the margins of the angle-localised families;
  - all of the double-null prototype's numerics.
- Three TEXT-class programs (`d0count5`, `modcount5`, `ordcensus5`) are routed ENUMERATE: they count the supplement's own
  steps that fix the integer d, so the edition needs their tables. The other 15 TEXT-class programs check wording, md5s,
  uses of named constants or cited papers' texts, and carry nothing over.
- Some programs contribute nothing of their own: C111 (a recount of C110), C238 (controls only), S4, S7 and S10 (absorbed
  into their importers).

ANALYTIC programs: the paper claim each supports, quoted around the program's citation (first body citation, else
Appendix C or A, else the supplement's file and heading), and the argument that must replace it:

- C87 eindcert5. Supports §8.5: "…ition (8.13) holds with ε_ind ≤ 1.94 × 10⁻⁸ ([eind5.py]: the certificate exact, the
  scan below l = 10⁴ certified by rigorous root inclusion in exact rational arithmetic ([eindcert5.py]: the least
  distance is δ_50 = 1.94137056846 × 10⁻⁸, enclosed to 3 × 10⁻⁴⁸, …" Argument needed: show every indicial root at 2 <= l
  < 10^4 keeps distance >= delta_50 from the integers: an asymptotic expansion of the roots in l with explicit remainder,
  plus enclosures for the finitely many small l it does not cover.
- C123 inverse6_5m. Supports §9: "…eal frequency, in a cut-off norm, carried exactly to the tensor-type blocks of the
  linearised operator and the vector-type blocks of the 1-form wave operator (certified, [inverse6_5m.py]); and the
  scalar-type zero-energy blocks of the linearised operator, writ…" Argument needed: show real-axis resolvent bounds for
  the mode-decomposed 1-form wave operator and the linearised operator at b0 for every harmonic and every real sigma !=
  0: Morawetz multipliers with positivity proved uniformly in (l, sigma).
- C125 envelope5. Supports §9: "…he proof of Theorem 1 delivers is traced term by term (supplement
  docket68/n1star/CONSTANTS5.md): at the numerical point (μ0 = 1, l5 = 1/10), with the smooth envelope of [envelope5.py],
  which has the numerics' integral, it is below 0.0024433 in the operator no…" Argument needed: give closed-form bounds
  on |env^(k)|, k <= 14, for the chosen bump (Cauchy estimates on a complex neighbourhood of its support, or an explicit
  Faa di Bruno bound).
- C129 m22cert5. Supports §9: "…, about 4.5 × 10⁻⁶ of the data (computed, floating point); this estimate cannot certify
  that number at the data's own truncation (supplement docket68/n1star/M22CERT5.md, [m22cert5.py])." Argument needed: a
  certified M_22 needs a validated solve of the stage-1 equation; the program only shows the a posteriori route cannot
  reach it. Supports a negative remark; the certified lambda0 bounds do not use it, so it can be dropped.
- C136 cdata5. Supports §9: "…etic): on the data cone the outgoing constraint of an explicit approximant holds to 5.0 ×
  10⁻⁵ and 2.3 × 10⁻⁵ at the two seeds, 4.1–4.3 % of the terms that cancel in it ([cdata5.py]); on u ∈ [−4, −1.1] r_h, v
  ∈ [0.55, 1.6] r_h, |x| ≤ cos(π/32), the Einstein re…" Argument needed: show the Raychaudhuri constraint residual of the
  explicit series data (Tangherlini plus a tensor Chebyshev series) is below the stated bound at every point of the data
  cone u = -10, e.g. from explicit bounds on the series coefficients and their derivatives.
- C137 rich5. Supports §9: "…over a sub-box of each of four of the 416 boxes covering that region, on which the
  single-grid approximant (data/rcert5_C3.npz) has certified values of 1.09–2.41 × 10⁻³ ([rich5.py]), and the single-grid
  approximant's supremum over one interior box of the 416 i…" Argument needed: show the Richardson approximant's Einstein
  residual is below the stated suprema on each sub-box (explicit derivative bounds for its pinned tensors).
- C138 rcert5d. Supports §9: "…rcert5_C3.npz) has certified values of 1.09–2.41 × 10⁻³ ([rich5.py]), and the single-grid
  approximant's supremum over one interior box of the 416 is at most 3.01 × 10⁻⁴ ([rcert5d.py]; both certificates' bounds
  are checked by a control that runs the whole bound…" Argument needed: show the single-grid approximant's Einstein
  residual is below the stated bound on the interior box: explicit derivative bounds replacing the order-3 Taylor models
  and bisection.
- C173 intcert5. Supports §9: "…l arithmetic for the background with the record's characteristic data, whose reduction to
  ordinary differential equations is deduced, each edge enclosed to within 0.008, [intcert5.py], [truebg5.py]), where no
  foliation of that slice is hyperbolic (deduced from…" Argument needed: show the margins of Theorems Q and L'' are
  positive on the whole slice, for the computed background and for the background itself (inequalities in one or two
  variables on a continuum).
- C174 truebg5. Supports §9: "…r the background with the record's characteristic data, whose reduction to ordinary
  differential equations is deduced, each edge enclosed to within 0.008, [intcert5.py], [truebg5.py]), where no foliation
  of that slice is hyperbolic (deduced from Rácz's charact…" Argument needed: show the true background on the slice below
  R_* lies in the stated tube around the computed one: an a posteriori ODE error bound with explicit constants.
- C203 hyp5. Supports App C: "the boundary at equality: the very edge; one crossing per column; the dips" Argument
  needed: show the chosen envelope satisfies the edge theorem's hypotheses (derivative ratios near the flat edge) at
  every point of its support.
- C210 e2trapband5. Supports App A: "The trapping band bound 11.477 for the cut-off resolvent up to σ = 384, certified in
  interval arithmetic." Argument needed: show the cut-off resolvent of the scalar wave on 5D Tangherlini is bounded by
  11.477 for every harmonic and every sigma in the band up to 384: a semiclassical trapping estimate at the photon sphere
  with explicit constants, uniform in (l, sigma).
- C222 eps1hyp5. Supports supplement CONSTANTS5 (Round 2); N1STAR-PROOF (0.3 Profiles and scaled norms; 2. Inequalities
  on the slices) Argument needed: show Lemma 1.1(e)'s eps1 at the paper's point by a lower bound on the hypersurfaces'
  margin as a function of (v, r): an inequality on a continuum.
- C256 e2trapcert5. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); E2-PILOT (3j. Large σ, harmonic by harmonic
  (D486, corrected D493)) Argument needed: show the trapping bound for every l >= 0 at sigma = 3, 6, 12, 24, 48, 96:
  uniformity in l by an explicit large-l asymptotic, finitely many small l by hand.
- C258 e2certify5. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); CONSTANTS5 (R14.7 Final replacement text for
  the paper (supersedes R13.7; R15.7 Fi); E2-PILOT (3f. Every harmonic l ≥ 1, certified (E2.9, D384); 5. Labels and sourc
  Argument needed: show the Morawetz hypothesis w = -phi V' - phi'''/2 >= 0 for the photon-sphere multiplier, for every
  harmonic l >= 1 and every r, with explicit tail bounds.
- C259 stage1rate5. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); CONSTANTS5 (R14.7 Final replacement text for
  the paper (supersedes R13.7; R15.7 Fi) Argument needed: the energy lemma's constant at the background: a supremum over
  the domain of explicit functions of r; likely reducible to a one-variable monotonicity argument.
- C261 stage0bd5. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); CONSTANTS5 (R14.7 Final replacement text for
  the paper (supersedes R13.7; R15.7 Fi) Argument needed: bounds to order 14 on every derivative of Theorem A's explicit
  profiles at the paper's point; follows from C125's envelope bounds by explicit Leibniz and Faa di Bruno sums.
- C262 rcert5. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); CERTIFY-10L5-RESULT (10.4 The paper: blocks A–E,
  and Appendix D's rows; 11.4 The paper: blo) Argument needed: show the Einstein residual of the explicit smoothed
  approximant is below the stated bound on the whole region: explicit derivative bounds for its tensor-product
  polynomials.
- C263 rcert5c. Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); CERTIFY-10L5-RESULT (10.4 The paper: blocks A–E,
  and Appendix D's rows; 11.4 The paper: blo) Argument needed: as C262: the residual enclosure for the approximant with
  its pinned coefficients.
- C281 e2h1_5. Supports supplement E2-PILOT (3i. One derivative, uniformly in l (E2.11, D404); 5. Labels and source)
  Argument needed: show the one-derivative resolvent constants are bounded uniformly in l (a supremum over l of explicit
  expressions in the Morawetz constants B_l).
- C282 e2lzero5. Supports supplement E2-PILOT (3g. The harmonic l = 0, certified (E2.8′, D387); 5. Labels and sources)
  Argument needed: show the l = 0 Morawetz weight with a Lagrangian term is nonnegative on the whole line, tails
  included.
- C284 e2asymcert5. Supports supplement E2-PILOT (3i. One derivative, uniformly in l (E2.11, D404); 5. Labels and source)
  Argument needed: show the asymmetric multiplier's Morawetz weight is positive for every harmonic l >= 1 and every r in
  the interval: a large-l asymptotic argument with explicit remainder plus finitely many l by hand.
- C285 e2asymlzero5. Supports supplement E2-PILOT (3i. One derivative, uniformly in l (E2.11, D404); 5. Labels and
  source) Argument needed: show the l = 0 weight of the asymmetric multiplier (with its Lagrangian term) is nonnegative
  on the whole real line in the tortoise coordinate, tails included.
- C286 e2asympsi5. Supports supplement E2-PILOT (3i. One derivative, uniformly in l (E2.11, D404)) Argument needed: show
  sup_r of psi/psi_* is bounded by the stated constant, so the l >= 2 constants carry over to the standard angular
  weight.
- C287 e2bandtop5. Supports supplement E2-PILOT (3j. Large σ, harmonic by harmonic (D486, corrected D493)) Argument
  needed: show the trapping band bound holds on every interval [sigma - 1/20, sigma] up to sigma = 384, i.e. uniformly in
  sigma over the band.
- C292 rcert5b. Supports supplement CERTIFY-10L5-RESULT (7.0 Answers; 7.6 Task 2: the demand on the residual, and one
  sub-box c) Argument needed: as C262 on one refined sub-box (a convergence study of the enclosure; droppable).

NUMERIC-ONLY programs, with the part that is numerical where only part is, and the paper claim each supports:

- C24 hf_core5 (floating point, no certificate). Supports §6: "The per-column zero set is not itself a marginally trapped
  surface; the statement is about the round family, as the numerical solver's is: [hf_core5.py] evolves the metric of the
  class in the Bondi form (3.2) from the free data o…"
- C25 hf_anchor5 (the anchor to the numerical runs (section 6)). Supports §6: "The one finer run, λ = 0.00625 at μ0 = 100
  l5², gives 0.4535, 0.74 % below, on the previous run's grid, which the solver's anchor check records as grid-limited
  ([hf_anchor5.py]); and the rows at 1000 l5² reproduce those at 100 l5² to about 10⁻⁴, the f…"
- C28 settle5 (T3 (l = 2 ringdown), T5 (settling times), T6 (tail t^-7) are numerical; T1, T2, T4 are DERIVE). Supports
  §8.2: "Linearly more is known, and it applies to the class: the class carries no vector-type perturbation and no
  linearised rotation (computed, [settle5.py] T1), and for the other two types the gauge-invariant master quantities on
  fiv…"
- C48 seed_escape (scattering of the shell off the seed computed numerically). Supports §8.2: "…: [CLY03b] Table 1, p. 8,
  which prints +0.2561i in its e^(iωt) convention), which evolving the master equation in time reproduces to 1%
  (settle5.py T3, on the barrier of [seed_escape.py]): an e-folding time of 3.905 r_h."
- C116 e2meas5 (floating point, no certificate). Supports §9: "…ithmetic, checks/e2trapband5_384.out,
  checks/e2h1band5.out); the bound lies 9.5 to 22 times above the computed norm at the sampled frequencies (computed,
  floating point, [e2meas5.py]); certified lower bounds for the norm, by test functions with compact support…"
- C127 lam0data5 (the data in closed form are DERIVE; the harmonic solve is floating point and feeds only the uncertified
  M_22 sharpening). Supports §9: "…initial slice are the second-order constraint expansion in closed form (exact), solved
  harmonic by harmonic (floating point; supplement docket68/n1star/LAMBDA0-DATA5.md, [lam0data5.py]); solved numerically
  for this envelope on the point's past, the stage gives…"
- C128 m22evol5 (M_22 = 2.207738). Supports §9: "… on the point's past, the stage gives that number as 2.207738, stable
  under refinement to 1.4 × 10⁻⁷ and reproduced by a second discretisation (computed, floating point, [m22evol5.py]), and
  with it the three bounds would be 0.0020789, 0.0018902 and 0.0010404."
- C130 growth5 (floating point, no certificate). Supports §9: "The solver's own scheme came first, with the growth factor
  measured on its computed solution at 10 l5 ([growth5.py], supplement section 10.2)."
- C131 excise5 (floating point, no certificate). Supports §9: "…three move by 0.0008, 0.0025 and 0.0002 between the grids
  and the standard excision by 0.0041 and 0.0004, and the order holds for every such duration from 0.005 to 0.06
  ([excise5.py])."
- C132 g5angle5 (floating point, no certificate). Supports §9: "…reakdown times are at one angular resolution, N_x = 16:
  at its own step it is unstable in angle at N_x = 24 and 32 on the seed itself, before the wave arrives (computed,
  [g5angle5.py] A1–A2; supplement CERTIFY-10L5-RESULT.md section 1.5)."
- C134 secondzero5 (floating point, no certificate). Supports §9: "… section of an ingoing cone lies near areal radius
  1.01–1.05 r_h (deduced, its identities computed in [sectexp5.py]; the zero set computed at 100 l5² for v ≤ 1.75 r_h in
  [secondzero5.py]; supplement note CERTIFY-10L5-RESULT.md section 1)."
- C135 szconv5 (floating point, no certificate). Supports §9: "…106 r_h at the smaller), which is therefore not the
  double-null grid's; it is consistent with the data truncation, halving as the radius doubles, at two radii (computed,
  [szconv5.py])."
- C144 wgron5 (the weighted constant measured on a model Goursat pair). Supports §9: "…ed domains of dependence away from
  the axes, at level 0 and at level 1 in the cones' L² norms (supplement CERTIFY-10L5-RESULT.md Theorems 7.L, 8.L1 and
  8.W; [lev1_5.py], [wgron5.py]); near each axis the class is four-dimensional axisymmetric Einstein–scalar in…"
- C149 blocks5 (H1 (independence of N) is DERIVE; H2, the size on the record's coefficients, is numerical). Supports §9:
  "…r which an estimate on the high angular modes would lower the constant fails at every angular resolution, in Theorem
  7.L's unweighted norms and at Theorem 8.W's weights ([blocks5.py], [blockw5.py]); the first seed's solution, in a
  constraint-preserving scheme …"
- C150 blockw5 (exact arithmetic, but on figures printed by floating-point runs (C149 H2, C144)). Supports §9: "…imate on
  the high angular modes would lower the constant fails at every angular resolution, in Theorem 7.L's unweighted norms
  and at Theorem 8.W's weights ([blocks5.py], [blockw5.py]); the first seed's solution, in a constraint-preserving scheme
  whose singular…"
- C151 cpaxis5 (floating point, no certificate). Supports §9: "…d at Theorem 8.W's weights ([blocks5.py], [blockw5.py]);
  the first seed's solution, in a constraint-preserving scheme whose singular coupling at the axes is regularised
  ([cpaxis5.py]), converges at second order in the null step to v ≈ 1.8 r_h at areal radius ≥…"
- C152 cp3grid5 (floating point, no certificate). Supports §9: "…is resolved in angle there on the finest grid, M = 40
  and 48 changing the metric by at most 3.0 × 10⁻⁹ and 3.3 × 10⁻⁹, with M = 48 also second order on three null grids
  ([cp3grid5.py]), and the free scheme's solution is consistent with second-order convergence…"
- C153 late5b (floating point, no certificate). Supports §9: "…econd order on three null grids ([cp3grid5.py]), and the
  free scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h at areal radius ≥ r_h as well
  ([late5b.py]); beyond, at M = 32 the metric still converges at second order in the null ste…"
- C154 mtrunc5 (floating point, no certificate). Supports §9: "…t M = 48, the unimposed constraint falls 3.84-fold from
  400 to 800 rows and 2.77-fold from 800 to 1600, and at 1600 rows M = 40 leaves it 3.5 times larger ([cpaxis5.py],
  [mtrunc5.py], [cp3grid5.py])."
- C156 r5op5 (decay exponents and residual degrees measured; a homogeneity derivation (DERIVE) would replace it).
  Supports §9: "…boundary, of width tending to 0 with λ, stays in the domain of dependence ([r9beyond5.py]); the
  coefficient decays and the residuals' degrees, measured on that operator ([r5op5.py], and [r6sigma5.py], which also
  builds the r^(−4) term there for one example, th…"
- C161 twobg5 (numerical ODE background). Supports §9: "… the record's argument: the two-dust background on the whole
  domain, the approximant to every order, the uniform estimate and the data (deduced, the identities computed,
  [twobg5.py], [twodecomp5.py], [twoledger5.py]; supplement docket68/n1star/FAMILIES5-FULL.m…"
- C172 racglobal5 (floating version; the certified margins are C173-C174 (ANALYTIC)). Supports §9: "… I's slice in a band
  widened by a computed amount (deduced): Rácz's split is hyperbolic on the slice except one band inside the shell, R
  between 4.29 and 4.53 (computed, [racglobal5.py]; its extent certified by interval arithmetic for the background with
  the r…"
- C175 racslice5 (S1 is DERIVE; S2-S3 are numerical). Supports §9: "…eristic equation), and a slice bent by at most
  0.0012 is hyperbolic everywhere (certified for that background and for its computed approximation in a stated
  interpolant; [racslice5.py], [intcert5.py], [truebg5.py])."
- C180 twodomainx5 (floating point, no certificate). Supports §9: "…, [hclass5.py], [re813.py], [eindcert5.py],
  [vii5census.py], [vii5read.py] and [census9.py], and for section 9 [support9.py], [charge5.py], [eqlayer5.py],
  [e2lower5.py], [twodomainx5.py], [level2loop5.py], [lambdacount5.py], [twodomain5.py], [excise5.py], [ix5…"
- C182 g1curv5 (floating point, no certificate). Supports §9: "…, [r9beyond5.py], [r5op5.py], [r6sigma5.py],
  [r5settle5.py], [eind5.py], [growth5.py] and [seed_escape.py]; [r0census5.py] (a census read at the lines),
  [e2meas5.py] and [g1curv5.py] (measurements) carry no negative control."
- C184 dnsolve5 (floating point, no certificate). Supports App C: "section 9, the double-null prototype"
- C212 resid5 (floating point, no certificate). Supports App A: "The computed Einstein residual of a smoothed double-null
  run (superseded in the paper by the certified residuals)."
- C255 e2high5 (floating point, no certificate). Supports supplement GLUEDECAY5 (8.5 Round 5 (current)); E2-PILOT (4.
  What remains for E2 at this operator)
- C265 gapscan5 (floating point, no certificate). Supports supplement LOSS-D (5. Findings)
- C266 gapsums5 (floating point, no certificate). Supports supplement CONSTANTS5 (R2.7 Sources (round 2)); LOSS-D (5.
  Findings)
- C268 s1coef5 (floating point, no certificate). Supports supplement LOSS-D (5. Findings)
- C277 e2band5 (floating point, no certificate). Supports supplement E2-PILOT (3d. The band between the two bounds,
  computed (D371); E2-PILOT -- E2 a)
- C278 e2pilot5 (P1 (the radial equation) is DERIVE; the resolvent at real sigma is a numerical ODE solve). Supports
  supplement E2-PILOT (E2-PILOT -- E2 at one operator: □ on 5D Tangherlini, harmoni)
- C283 e2asym5 (floating point, no certificate). Supports supplement E2-PILOT (3i. One derivative, uniformly in l (E2.11,
  D404))
- C288 late5 (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (3. The late region (computed,
  `checks/late5.py`); 4. Files, runs and o)
- C289 jordan5 (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (6.0 Answers; 6.2 F5: the linear
  estimate, and why it cannot be had in )
- C290 ampresp5 (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (6.0 Answers; 6.2 F5: the
  linear estimate, and why it cannot be had in )
- C291 cplate5 (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (6.0 Answers; 6.4 R: the late
  region)
- C293 cplate5c (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (7.8 Files and outputs (round
  3); 7.9 A proposed replacement for the pa)
- C294 cplate5d (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (7.8 Files and outputs (round
  3))
- C296 axisdrift5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C297 g1geom5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C298 g1cells5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C299 g1uv5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C300 g1cut5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C301 g1axis5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C302 g1amp5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C303 g1map5 (floating point, no certificate). Supports supplement CERTIFY-10L5 (6b. F2: the prototype and what it
  measured (computed, D344; )
- C304 transfer5 (floating point, no certificate). Supports supplement BEYOND5 (3. What remains)
- C305 strip5 (floating point, no certificate). Supports supplement BEYOND5 (3. What remains)
- C307 stripderiv5 (floating point, no certificate). Supports supplement BEYOND5 (3. What remains)
- C308 stripradial5 (floating point, no certificate). Supports supplement BEYOND5 (3. What remains)
- C319 r5models5 (floating point, no certificate). Supports supplement FAMILIES5-R6 (FAMILIES5-R6 -- round 6: the
  charge's sign, the band crossed; Files)
- C320 katonl5 (floating point, no certificate). Supports supplement FAMILIES5-VLASOV (FAMILIES5-VLASOV -- restricted
  Vlasov limits in the T² class; Files); FAMILIES5-R6 (FAMILIES5-R6 -- round 6: the charge's sign, the band crossed;
  Files); FAMILIES5-R7 (FAMILIES5-R7 -
- C321 ehband5 (floating point, no certificate). Supports supplement FAMILIES5-MB (FAMILIES5-MB -- the sign of the charge
  on seeds that perturb); FAMILIES5-R10 (R10.0 The findings and what was done); FAMILIES5-R11 (R11.0 What was done)
- S1 emitter_process (separate programme's module; goes with C48). Supports the claims of its importers (C48)
- S2 hf_mirror5 (solver). Supports the claims of its importers (C130, C24)
- S3 source_spec (separate programme's module; goes with C25). Supports the claims of its importers (C25)
- S5 bondisph5 (floating point, no certificate). Supports the claims of its importers (C134, C212, C262, C288)
- S6 cpsolve5 (floating point, no certificate). Supports the claims of its importers (C151, C152, C289)
- S8 e2trap5 (floating point, no certificate). Supports the claims of its importers (C210, C287)
- S9 g5zeros5 (floating point, no certificate). Supports supplement GLUEDECAY5 (8.5 Round 5 (current));
  CERTIFY-10L5-RESULT (1.4 The Bondi spheres rebuilt from the double-null solution; 4. Files,)
- S11 szrun5 (floating point, no certificate). Supports supplement CERTIFY-10L5-RESULT (13.2 The rebuild against growth5
  from v = 1.3, at a second n; 4. Files)

## 1. Counts per class

| class | programs | lines | paper-cited | supplement-only | import-only |
| --- | ---: | ---: | ---: | ---: | ---: |
| MATH | 317 | 105,991 | 235 | 82 | 0 |
| MEASUREMENT | 20 | 3,511 | 3 | 17 | 0 |
| DATA | 14 | 3,738 | 10 | 1 | 3 |
| TEXT | 18 | 5,655 | 11 | 7 | 0 |
| total | 369 | 118,895 | 259 | 107 | 3 |

Class rules as applied. MATH: computes mathematics and carries (or is) a check; numerical programs with a negative
control are MATH with `method` float-numerical. MEASUREMENT: floating-point measurement with no control (the G1-prototype
diagnostics, the resolvent samples, a few scans). DATA: produces runs or a library other programs consume and makes no
claim of its own (solvers, run drivers, jet arithmetic, the separate programme's modules). TEXT: its input is the paper's
or the supplement's text (censuses, enumerations, replacement-text checks, md5 or wording checks) or cited papers'
fetched full texts.

## 2. Proposed numbering

(Superseded as a code-appendix numbering by the changed directive; kept because the triage and the tables below use the
numbers as identifiers.)

Rules. One number per program, all its labels under it. Order: the paper's sections 1-9 by the line of first mention in
the body; a program the body never names is placed at the end of the section its Appendix C row names; Appendix A's
"programs behind section 9" that neither the body nor Appendix C names follow §9; then the supplement-only programs in
the supplement's order (the main proof file by section, then `proof5/` Parts I-IX, then the round documents in the order
the paper first cites them). MATH, MEASUREMENT (tag `[MEAS]`) and the two DATA programs the paper presents as
computations (the numerical sequence and the double-null prototype) are numbered; libraries get S-numbers; TEXT gets
none.

- paper §2.1: C1 response5, C2 kn_gauge
- paper §2.2: C3 ks5
- paper §2.4: C4 ansatz5, C5 data5, C6 hf_theorem5, C7 lead5
- paper §3: C8 support3, C9 counterpart5, C10 horizon5, C11 mass5, C12 stage5, C13 support5c, C14 past5, C15 ledger5, C16
  gauge5, C17 bondi5
- paper §3 (placed by Appendix C): C18 foliation5, C19 stage5b
- paper §4: C20 support9
- paper §5.1: C21 support5
- paper §5.2: C22 support5b
- paper §5.5: C23 csolve5
- paper §6: C24 hf_core5[DATA], C25 hf_anchor5
- paper §8.1: C26 support8
- paper §8.2: C27 ix5, C28 settle5, C29 kirecon5, C30 redshift5, C31 rwgauge5u, C32 wavegauge5, C33 gdrepair5, C34
  gdscri5, C35 gdext5, C36 gdkplus5, C37 gdlge2_5, C38 gdrad5, C39 gdtail5, C40 gdr9_5, C41 hung4, C42 rungs5, C43
  growing5, C44 lzero5, C45 hierarchy5, C46 coupled5, C47 lzerorate5, C48 seed_escape
- paper §8.2 (placed by Appendix C): C49 admbox5
- paper §8.3: C50 damping5, C51 semiclass5, C52 cform5, C53 gaugepot5, C54 modes5, C55 trap5, C56 thresh5, C57 hienergy5,
  C58 lowenergy5, C59 hthresh5, C60 cpmodes5, C61 solv5, C62 tface5, C63 lin5, C64 sbar5, C65 strap5, C66 gmodes5, C67
  zstates5, C68 genstates5, C69 puregauge5, C70 dual5, C71 mp5, C72 pairing5, C73 static5, C74 physical5, C75 window5,
  C76 iota5, C77 scri5, C78 aug5, C79 lowfreq5, C80 cone5
- paper §8.4: C81 class5, C82 iplus5, C83 support8c, C84 sharp5, C85 support8b
- paper §8.5: C86 eind5, C87 eindcert5, C88 uniform5, C89 hclass5, C90 re813, C91 transfer5
- paper §8.6: C92 general5
- paper §8.7: C93 flux5, C94 mpdata5, C95 gluedecay5
- paper §8.8: C96 edge5, C97 exterior5, C98 gluing5, C99 synth5, C100 bundle5, C101 iotasol5, C102 tfnorm5
- paper §8.8 (placed by Appendix C): C103 iplusnorm5
- paper §9: C104 lambdacount5, C105 level2loop5, C106 epsind5, C107 thetain5, C108 charge5, C109 prop31loss5, C110
  dnumber5, C111 x7indep5, C112 l2par5, C113 logind5, C114 iotaind5, C115 rootavoid5, C116 e2meas5[MEAS], C117 e2lower5,
  C118 deltacap5, C119 inverse6_5a, C120 tensorzero5, C121 zeroext5, C122 inverse6_5, C123 inverse6_5m, C124
  scalarblock5, C125 envelope5, C126 classm5, C127 lam0data5, C128 m22evol5, C129 m22cert5, C130 growth5, C131 excise5,
  C132 g5angle5, C133 sectexp5, C134 secondzero5, C135 szconv5, C136 cdata5, C137 rich5, C138 rcert5d, C139 reduce5, C140
  symbol5s, C141 linest5, C142 null3, C143 lev1_5, C144 wgron5, C145 axis5, C146 axisbianchi5, C147 axhier5, C148 cont5,
  C149 blocks5, C150 blockw5, C151 cpaxis5, C152 cp3grid5, C153 late5b, C154 mtrunc5, C155 tail5, C156 r5op5, C157
  r9beyond5, C158 r6sigma5, C159 r5settle5, C160 innerr5, C161 twobg5, C162 twodecomp5, C163 twoledger5, C164
  torusstress5, C165 vlasovhf5, C166 axisphase5, C167 nledger5, C168 nfamily5, C169 twoscale5, C170 vlasovex5, C171
  bandconst5, C172 racglobal5, C173 intcert5, C174 truebg5, C175 racslice5, C176 qsign5, C177 mbslice5, C178 mbsign5,
  C179 eqlayer5, C180 twodomainx5, C181 twodomain5, C182 g1curv5[MEAS]
- paper §9 (placed by Appendix C): C183 closure5, C184 dnsolve5[DATA], C185 eq5, C186 layerlin5, C187 layerwin5, C188
  layerdeg5, C189 layerledger5, C190 layerfix5, C191 layerband5, C192 veryedge5, C193 lamL5, C194 stagen5, C195 edgeP5,
  C196 stagefree5, C197 bandL4p5, C198 lamL5b, C199 edge1_5, C200 degtwo5, C201 constL5, C202 bfam5, C203 hyp5, C204
  lam25_5, C205 lamconst5, C206 lzerotrace5, C207 layernull5, C208 layerpast5
- paper §9 (Appendix A's section-9 list, not cited in the body): C209 e2h1band5, C210 e2trapband5, C211 data5two, C212
  resid5, C213 coulomb5, C214 coulombL5, C215 harmonics5, C216 uniform5, C217 sources5, C218 stripfull5, C219 stage0two5,
  C220 chardust5, C221 twodust5
- supplement: N1STAR-PROOF: C222 eps1hyp5, C223 gronwall5, C224 indepcons5, C225 tame5, C226 symmshift5, C227 rwgauge5,
  C228 f1lemma5, C229 cclass5
- supplement: proof5/PART-III-K-NONLINEAR: C230 scrirad5
- supplement: proof5/PART-V-GLUING: C231 jac5[MEAS]
- supplement: proof5/PART-VI3-TRAPPING: C232 trap5
- supplement: proof5/PART-VI2-HORIZON: C233 horizon5
- supplement: proof5/PART-VI-DYN: C234 dyn5
- supplement: SETTLE-GLAM5: C235 wedge5, C236 halfclass5, C237 scatter5, C238 r1controls5, C239 spatinf5, C240 poly5,
  C241 scale5, C242 trunc5, C243 order5, C244 boot5, C245 vac5, C246 zinv5, C247 r6settle5, C248 r7settle5
- supplement: GLUEDECAY5: C249 hgauge5, C250 stage1cap5, C251 dceiling5, C252 dweights5, C253 lambdagen5, C254 eflat5,
  C255 e2high5[MEAS], C256 e2trapcert5, C257 iotapoles5, C258 e2certify5, C259 stage1rate5, C260 lzeroconst5, C261
  stage0bd5, C262 rcert5, C263 rcert5c, C264 symbol5
- supplement: LOSS-D: C265 gapscan5[MEAS], C266 gapsums5, C267 s1reson5, C268 s1coef5[MEAS]
- supplement: CONSTANTS5: C269 cover5, C270 zeroinv5, C271 bbar5, C272 iotamut5, C273 lzerorank5, C274 zerohardy5, C275
  r6fixes5, C276 r7fixes5
- supplement: E2-PILOT: C277 e2band5[MEAS], C278 e2pilot5, C279 e2morawetz5, C280 e2cplx5, C281 e2h1_5, C282 e2lzero5,
  C283 e2asym5[MEAS], C284 e2asymcert5, C285 e2asymlzero5, C286 e2asympsi5, C287 e2bandtop5
- supplement: CERTIFY-10L5-RESULT: C288 late5, C289 jordan5, C290 ampresp5[MEAS], C291 cplate5, C292 rcert5b, C293
  cplate5c, C294 cplate5d, C295 prop5
- supplement: CERTIFY-10L5: C296 axisdrift5[MEAS], C297 g1geom5[MEAS], C298 g1cells5[MEAS], C299 g1uv5[MEAS], C300
  g1cut5[MEAS], C301 g1axis5[MEAS], C302 g1amp5[MEAS], C303 g1map5[MEAS]
- supplement: BEYOND5: C304 transfer5[MEAS], C305 strip5, C306 uniform3_5, C307 stripderiv5[MEAS], C308
  stripradial5[MEAS]
- supplement: FAMILIES5-FULL: C309 h3proof5, C310 twoslice5, C311 nonres5, C312 twotransport5, C313 twohorizon5, C314
  twoparity5
- supplement: FAMILIES5-AXIS: C315 axisellip5, C316 vlasov5, C317 augment5, C318 axisloss5
- supplement: FAMILIES5-R6: C319 r5models5, C320 katonl5
- supplement: FAMILIES5-MB: C321 ehband5
- supplement: GAUGEDECAY5: C322 gdix5, C323 gdsk5, C324 gdr3fix5, C325 gdrate5
- supplement: FAMILIES5: C326 twophase5, C327 stage1pure5, C328 twolin5, C329 stage0h5, C330 propagate5, C331 charprop5,
  C332 charcons5, C333 charcorner5, C334 chardustdata5, C335 dustloss5, C336 twodt5, C337 twoext5
- supplement: FAMILIES5-NONROUND: C338 classchi5
- paper Appendix D only (imported by C83): C339 lhor5

Points for the editor:

- **C1 is the paper's own program and spans §§2-9** (R1-R14). One number per the brief; the edition may prefer
  C1.1-C1.14, since R2-R14 support different sections. R9 (Appendix D's md5 table matches the files) is a TEXT check and
  should not survive into the reader's archive.
- C222-C338 are numbered after the paper: 117 programs, the 99 numbered supplement-only ones (21,305 lines) and 18 that
  the paper names only in Appendix D's import list. If the edition interleaves the supplement's proofs with the paper's
  sections, renumber by the supplement section each one supports (`paper_sections` gives the citing file and heading).
- C339 (`lhor5`) is named only in Appendix D's import list; it is imported by C83.

Shared modules (S-numbers; DATA libraries, no claim of their own):

- S1 emitter_process (362 lines, imported by C48): Module of the author's separate (non-paper) programme: the bulk
  emitter process for the opening shell; loaded by the seed-scattering program.
- S2 hf_mirror5 (615 lines, imported by C24 C130): The double-null solver for the mirror-symmetric vacuum sequence of the
  round shell, used as a library by the numerical runs.
- S3 source_spec (368 lines, imported by C25): Module of the author's separate (non-paper) programme: source
  specification constants; loaded by the error-constant program.
- S4 src_hole (370 lines, imported by C6 C25): Module of the author's separate programme: the shell collapsing onto its
  seed and the interior core of the limit, used for the single-horizon check.
- S5 bondisph5 (194 lines, imported by C134 C212 C262 C288): Library: the round spheres of the Bondi chart rebuilt on the
  double-null solution, and their outgoing expansion.
- S6 cpsolve5 (302 lines, imported by C151 C152 C289): Library: the constraint-preserving double-null solver that imposes
  the Raychaudhuri constraint along every outgoing generator.
- S7 dg5 (70 lines, imported by C108): Library: the loss d_G on the ι+ window, d = 7 + 2⌈ℓ_I − Re λ⌉.
- S8 e2trap5 (264 lines, imported by C210 C287): The two Morawetz lemmas harmonic by harmonic at large σ with a
  multiplier narrow at the photon sphere and wide in the flanks (floating-point library for the certified band).
- S9 g5zeros5 (32 lines, imported by none): Re-runs the Bondi scheme recording every zero of the round spheres'
  expansion, for the program that reads them.
- S10 jetpoly5 (182 lines, imported by C315 C317 C338): Library: exact truncated multivariate polynomials in rationals
  for the jet checks.
- S11 szrun5 (84 lines, imported by none): Runs of the double-null solver stopped at a given v, for the programs that
  read them.
- S12 dnull5 (152 lines, imported by C139 C145 C171 C184): The class in double-null gauge: the five-dimensional
  characteristic structure behind the a posteriori route at 10 l5 (shared library).

TEXT programs (no number; what each checks):

- bundlesweep (217 lines; paper §8.8): A token-sweep census of every step of Hintz's spectral theory that uses a scalar
  operator (38 items), over the cited paper's fetched full text.
- censusweep (95 lines; paper §8.8): A census of every dimension marker on the 205 pages of the cited papers swept, each
  read against the supplement's sections; needs fetched full texts that are not stored.
- baire5 (188 lines; supplement CONSTANTS5): Classifies the supplement's 18 closed-graph, open-mapping and
  Banach–Steinhaus sites by whether each constant is effective.
- census9 (361 lines; paper §8.5, §9): Censuses of the supplement's section 10: the 78 lines that name the parameter
  point by value, the losses and the lowered boundary, each placed in a class.
- d0count5 (518 lines; paper §9): Counts the coefficient orders the supplement fixes by the closed graph theorem, from a
  census of its text, and the arithmetic built on them.
- lzeroaudit5 (337 lines; supplement CONSTANTS5): Audits whether every step of the threshold λ0's construction in the
  supplement is constructive, by reading the supplement's text.
- modcount5 (858 lines; paper §9): The fixed per-level steps of the β-levels and every other step a level charges, read
  from the supplement and counted at the chosen weights, so that c′ and d become numbers.
- nkind5 (242 lines; supplement CONSTANTS5): Which steps behind λ1 and δ admit no effective bound from the proof as
  written, read from the supplement's text.
- nrows5 (171 lines; supplement CONSTANTS5): Every non-effective step behind λ1 and δ in the supplement, with its
  quantitative replacement, read from the text and a ledger table.
- ordcensus5 (400 lines; paper §9): The orders at which the forward-solution chain invokes the calculus fixed by the
  closed graph theorem, read site by site from the supplement.
- r0census5 (124 lines; paper §9): Census of every use of the inner radius r_0 = R_1/2 in the supplement's Parts III–VII,
  each placed in a class.
- r5edits5 (194 lines; supplement N1STAR-LOG, N1STAR-PROOF, SETTLE-GLAM5): A replacement text for the supplement's Lemma
  11.0 checked against the current text, with the facts its new sentences state computed.
- r6edits5 (829 lines; supplement N1STAR-LOG, SETTLE-GLAM5): The final replacement text for the supplement's Lemma 11.0
  applied to a copy of the live file, and the mathematics it states checked.
- r9text5 (168 lines; supplement SETTLE-GLAM5): Checks the wording of a supplement file's own text against a reader's
  findings.
- vii5census (394 lines; paper §8.8, §9): Enumerates every line of the supplement's Parts III–IV that names an averaged
  or equivariant choice by one of 58 printed symbols.
- vii5read (383 lines; paper §8.8, §9): Holds a reading table of the 713 averaged-choice lines against that census and
  checks a value worked by hand.
- admiss5 (52 lines; paper §8.8): Enumerates every line of the supplement's parts that uses the admissibility property,
  failing on any unlisted line.
- gammac5 (124 lines; paper §8.8): Enumerates every line of the supplement's parts that uses the constraint damping's
  constants, failing on any unlisted line.

## 3. Dependency graph among the numbered programs

Import edges, `module (in-degree) <- importers`, for every module imported by two or more programs:

- C50 damping5 (51) <- C51 C52 C53 C54 C55 C56 C57 C58 C59 C60 C61 C62 C63 C64 C65 C66 C67 C68 C69 C70 C71 C72 C73 C74
  C75 C76 C77 C78 C79 C80 C81 C82 C83 C84 C86 C88 C89 C90 C91 C92 C96 C98 C99 C100 C101 C102 C103 C115 C124 C257 C265
- C7 lead5 (13) <- C8 C12 C13 C14 C16 C19 C20 C21 C22 C26 C261 C271 C314
- C227 rwgauge5 (11) <- C31 C33 C34 C37 C38 C39 C40 C49 C249 C323 C324
- C249 hgauge5 (9) <- C33 C34 C37 C38 C39 C40 C49 C323 C324
- C252 dweights5 (8) <- C110 C111 C113 C115 C251 C253 C254 C276
- C68 genstates5 (7) <- C69 C70 C214 C215 C218 C267 C268
- C184 dnsolve5 (7) <- C141 C182 C212 C264 C289 C303 S6
- C186 layerlin5 (7) <- C188 C190 C192 C196 C199 C202 C208
- C53 gaugepot5 (6) <- C54 C55 C56 C57 C62 C63
- C63 lin5 (6) <- C74 C75 C76 C77 C82 C257
- C64 sbar5 (6) <- C77 C78 C79 C82 C83 C107
- C109 prop31loss5 (6) <- C108 C110 C115 C251 C252 C253
- C214 coulombL5 (6) <- C215 C216 C218 C304 C306 C307
- C219 stage0two5 (6) <- C313 C314 C326 C327 C328 C329
- C260 lzeroconst5 (6) <- C206 C222 C223 C250 C261 C276
- C297 g1geom5 (5) <- C298 C300 C301 C302 C303
- C5 data5 (4) <- C16 C23 C127 C211
- C141 linest5 (4) <- C143 C144 C145 C149
- C215 harmonics5 (4) <- C216 C218 C306 C307
- C228 f1lemma5 (4) <- C156 C158 C229 C247
- C251 dceiling5 (4) <- C110 C114 C254 C257
- C254 eflat5 (4) <- C110 C113 C114 C276
- C262 rcert5 (4) <- C137 C138 C263 C292
- S5 bondisph5 (4) <- C134 C212 C262 C288
- S12 dnull5 (4) <- C139 C145 C171 C184
- C4 ansatz5 (3) <- C1 C21 C26
- C24 hf_core5 (3) <- C6 C25 C130
- C32 wavegauge5 (3) <- C43 C44 C46
- C38 gdrad5 (3) <- C37 C39 C40
- C49 admbox5 (3) <- C34 C323 C324
- C51 semiclass5 (3) <- C52 C62 C265
- C54 modes5 (3) <- C55 C56 C123
- C66 gmodes5 (3) <- C73 C99 C123
- C82 iplus5 (3) <- C83 C84 C92
- C125 envelope5 (3) <- C206 C222 C261
- C130 growth5 (3) <- C131 C132 S9
- C142 null3 (3) <- C141 C148 C295
- C181 twodomain5 (3) <- C161 C180 C337
- C206 lzerotrace5 (3) <- C250 C273 C276
- C253 lambdagen5 (3) <- C110 C115 C251
- S6 cpsolve5 (3) <- C151 C152 C289
- S10 jetpoly5 (3) <- C315 C317 C338
- C12 stage5 (2) <- C19 C314
- C21 support5 (2) <- C15 C22
- C25 hf_anchor5 (2) <- C2 C48
- C28 settle5 (2) <- C30 C31
- C52 cform5 (2) <- C61 C62
- C56 thresh5 (2) <- C57 C58
- C67 zstates5 (2) <- C68 C69
- C75 window5 (2) <- C84 C92
- C76 iota5 (2) <- C77 C257
- C77 scri5 (2) <- C82 C83
- C81 class5 (2) <- C84 C120
- C94 mpdata5 (2) <- C85 C95
- C110 dnumber5 (2) <- C111 C113
- C159 r5settle5 (2) <- C158 C247
- C218 stripfull5 (2) <- C306 C307
- C255 e2high5 (2) <- C116 S8
- C256 e2trapcert5 (2) <- C210 C287
- C257 iotapoles5 (2) <- C254 C272
- C259 stage1rate5 (2) <- C127 C276
- C279 e2morawetz5 (2) <- C255 S8
- C284 e2asymcert5 (2) <- C256 C286
- C300 g1cut5 (2) <- C301 C302
- S2 hf_mirror5 (2) <- C24 C130
- S4 src_hole (2) <- C6 C25
- S8 e2trap5 (2) <- C210 C287

Modules imported by exactly one program (`imported<-importer`):

C1<-C16; C2<-C9; C10<-C13; C11<-C8; C14<-C8; C27<-C322; C29<-C31; C34<-C324; C35<-C38; C37<-C40; C45<-C47; C55<-C57;
C59<-C83; C65<-C122; C69<-C70; C70<-C71; C78<-C79; C84<-C92; C86<-C87; C92<-C98; C103<-C102; C105<-C104; C121<-C120;
C127<-C128; C128<-C129; C133<-S5; C134<-C135; C138<-C137; C144<-C143; C146<-C147; C151<-C152; C161<-C171; C169<-C165;
C191<-C197; C192<-C195; C193<-C198; C197<-C200; C201<-C205; C204<-C205; C210<-C287; C212<-C262; C216<-C306; C250<-C126;
C258<-C123; C261<-C206; C263<-C292; C264<-C140; C280<-C281; C291<-C293; C299<-C298; C331<-C332; C338<-C315; C339<-C83;
S1<-C48; S3<-C25; S7<-C108; c_junction<-S1; earth_cap<-S3; encode_labels<-S3; encode_read<-S3; field_open<-S1;
ledger<-S3; p2_gravity<-S3; reader<-S1; settle_arrival<-S3; source_capacity<-S3

Data-file edges (a numbered program reads a file another program wrote, or a pinned data file):

- C2 kn_gauge reads kn_gauge_k8.json
- C17 bondi5 reads hf_core5_runs.json from C24
- C24 hf_core5 reads hf_core5_runs.json
- C48 seed_escape reads seed_escape_R.json
- C95 gluedecay5 reads gluedecay5.out
- C112 l2par5 reads dnumber5.out from C110
- C113 logind5 reads dnumber5.out from C110
- C115 rootavoid5 reads lambdagen5.out from C253
- C130 growth5 reads growth5_runs.json
- C134 secondzero5 reads growth5_runs.json from C130
- C137 rich5 reads l1_M16_400.npz (not in repository); l1_M16_800.npz (not in repository); rcert5_C3.npz from C262;
  rcert5_C3R.npz from C262
- C138 rcert5d reads census_vals.npy; rcert5_C3.npz from C262
- C150 blockw5 reads blocks5.out from C149; wgron5.out from C144
- C153 late5b reads l1_rc0.7_M%d.npz (not in repository); l1_rc0.7_M32.npz (not in repository); l1_rc0.9_M%d.npz (not in
  repository); l1_rc0.9_M%d_1600.npz (not in repository); l1_rc0.9_M32.npz (not in repository); l1_rc0.9_M32_1600.npz
  (not in repository)
- C154 mtrunc5 reads cpaxis5_a5.out from C151; cpaxis5_a5_m48.out from C151; cpaxis5_a5_m56.out from C151
- C182 g1curv5 reads amp%s_M%d.npz (not in repository); amp1_M40.npz (not in repository); curv%s_M%d.npz (not in
  repository); curvS2_M%d.npz (not in repository); curvS2_M%d_%d%s.npz (not in repository); curvS2_M%d_1600%s.npz (not in
  repository); curvS2_M%d_1600.npz (not in repository); curvnull_M%d_%d.npz (not in repository); l1_rc0.9_M%d%s.npz (not
  in repository); l1_rc0.9_M40.npz (not in repository); s2_M%d.npz (not in repository); s2_M%d_%d.npz (not in
  repository); s2_M%d_1600.npz (not in repository); s2_M32.npz (not in repository)
- C263 rcert5c reads l1_M16_800.npz (not in repository); rcert5_C3.npz from C262
- C279 e2morawetz5 reads e2band5_s3.out from C277
- C290 ampresp5 reads amp%s_M32.npz (not in repository)
- C291 cplate5 reads amp0.875_M32.npz (not in repository); cp_M32_400.npz (not in repository); cp_M32_800.npz (not in
  repository); l1_rc0.9_M32.npz (not in repository); l1_rc0.9_M32_1600.npz (not in repository)
- C293 cplate5c reads amp0.875_M32.npz (not in repository); cp_M32_400.npz (not in repository); cp_M32_800.npz (not in
  repository); l1_rc0.9_M32.npz (not in repository); l1_rc0.9_M32_1600.npz (not in repository)
- C302 g1amp5 reads amp%s_M%d.npz (not in repository); amp%s_M40.npz (not in repository); amp*_M32.npz (not in
  repository)
- C303 g1map5 reads amp%s_M%d.npz (not in repository); amp1_M%d.npz (not in repository)
- S2 hf_mirror5 reads hf_mirror5_runs.json

Corrections to the mechanical table: `rcert5_C3R.npz` is written by C137 (`rich5 --write`), not C262; `rcert5_C3.npz` by
C263 (`rcert5c --write`). The pinned data files that must ship with the archive are `growth5_runs.json`,
`hf_core5_runs.json`, `hf_mirror5_runs.json`, `hf_mirror5_eqs.json.gz`, `kn_gauge_k8.json`, `seed_escape_R.json`,
`rcert5_C3.npz`, `rcert5_C3R.npz`, plus the printed outputs that later programs parse (`blocks5.out`, `wgron5.out`,
`cpaxis5_a5*.out`, `e2band5_s3.out`, `dnumber5.out`, `lambdagen5.out`, `scalarblock5_block.txt`). Order matters: C110
before C112-C113, C253 before C115, C149 and C144 before C150, C151 (about four hours) before C154, C277 before C279.

**Minimal shared modules.** The archive must ship every imported module: 123 of the registry's programs are imported by
another (67 by two or more). No refactoring is needed if each file is named by its number and importers write, for
example, `import C50 as damping`. If the editor prefers a few named libraries, the in-degree suggests these groups (each
keeps its own C-numbered self-test):

- the five-dimensional linearised operators and constraint damping on Tangherlini: C50 (51 importers), C53, C63, C64,
  C54, C56, C51, C52, C66, C67, C68, C75, C76, C77, C81, C82;
- the background, ansatz and stage-0 profiles: C7 (13 importers), C4, C5, C12, C21;
- harmonic and Regge-Wheeler gauge: C227 (11), C249 (9), C49, C38, C32, C28;
- the loss count d: C252 (8), C109, C251, C254, C253, C110, C257;
- the double-null class, solvers and transport: C184 (7), S12, S6, S5, C141, C142, C133;
- the λ0 constants and envelopes: C260 (6), C125, C206, C259, C261;
- the equality layer: C186 (7);
- Coulomb parts and strip transfers: C214 (6), C215, C218;
- two crossing families: C219 (6), C181;
- the gauge-fixed operator in Cartesian components and the settling wedge: C228 (4), C159;
- Morawetz and resolvent bounds on Tangherlini: C279, C255, S8, C256, C284;
- certified residuals in ball arithmetic: C262 (4), C138;
- the numerical high-frequency solver: S2, C24, C130;
- jets in exact rationals: S10; the double-null diagnostics: C297, C300.

Cross-tree edges that will look odd in a reader's archive: **C16 (the gauge field) imports C1** (the paper's own program,
for its R14); C1 imports C4 and, under `--full`, runs C3, C18, C7, C4, C5 by subprocess.

## 4. Programs that cannot run outside the repository as they stand

- reads paper/supplement text or ledgers (28): C1 C2 C6 C9 C14 C20 C25 C30 C31 C48 C85 C95 C112 C113 C114 C115 C119 C157
  C194 C196 C198 C205 C206 C274 S1 S2 S3 S4
- cross-directory imports (sys.path / file loads) (141): C1 C8 C12 C13 C15 C16 C19 C20 C21 C22 C23 C24 C26 C30 C31 C43
  C44 C46 C47 C83 C85 C87 C89 C90 C95 C104 C107 C108 C110 C111 C113 C114 C115 C116 C120 C122 C123 C124 C126 C127 C128
  C129 C130 C131 C132 C134 C135 C137 C138 C139 C141 C145 C156 C158 C161 C165 C171 C172 C173 C174 C175 C176 C177 C180 C182
  C188 C190 C192 C195 C196 C197 C198 C199 C200 C202 C205 C206 C208 C210 C211 C212 C214 C215 C216 C218 C222 C223 C229 C247
  C250 C251 C252 C253 C254 C255 C256 C257 C261 C262 C263 C264 C265 C267 C268 C271 C272 C273 C276 C281 C287 C288 C289 C292
  C298 C300 C301 C302 C303 C304 C306 C307 C313 C314 C315 C317 C326 C327 C328 C329 C332 C337 C338 S6 S8 S9 baire5.py
  d0count5.py modcount5.py r5edits5.py r6edits5.py vii5read.py
- md5 pins of repository files (17): C1 C2 C48 C112 C113 C114 C115 C119 C137 C138 C194 C196 C198 C205 C206 C263 C292
- run directory of .npz files not in repository (9): C137 C153 C182 C263 C290 C291 C293 C302 C303

What each group needs:

- **Text dependence (28 non-TEXT programs read the paper, the supplement or its ledgers).** Most are MATH programs with a
  READ step: a quoted line located by content, often md5-pinned (C1 R9, C14 P9, C30, C31, C85, C95, C112-C115, C119,
  C157, C194, C196, C198, C205, C206, C274; C20 S3 is a census over `proof5/PART-*.md` and `EFFECTIVE-LEDGER.tsv`). In
  the archive these steps must be cut or the quoted passages carried as constants. The 18 TEXT programs are blocked by
  definition. C112-C115 and the unnumbered TEXT programs `d0count5`, `modcount5` and `ordcensus5` read the supplement's
  sites behind the paper's integer d: if the text reads go, the site tables must enter the archive as data.
- **The earlier lemma programs (C2, C6, C9, C25, C48, C24, S2) are the worst.** All but C24 read
  `docket68/M-RULINGS-2026-10-03.md` (a process rulings file outside the tree being published; C24 reaches it through S2)
  and load siblings by file path. C25 loads S3, which loads seven modules of the author's separate programme, which load
  more: **28 files, 10,817 lines in all**, including `docket68/warptheorem.py` and the research root's `stability.py`. C2
  (`kn_gauge`, Proposition 2.1) loads C25 in its K5 and K8 paths, which its default self-test always runs (with a K0 that
  checks two items' wording in the rulings file), so the separate programme is a run-time dependency of Proposition 2.1's
  check unless K1-K2 are extracted alone (the paper cites only K1-K2). C48 loads S1 (three more of those modules) and
  C25. C6 loads S4 and runs Lean 4 on `lemmas/lean/HFTarget.lean`, falling back to the absolute path
  `/root/sci/bin/lean/lean`; its Wolfram Language result is quoted in the docstring, not run. C9 reads C6's source text.
- **Run directories not in the repository (9).** C153, C182, C290, C291, C293, C302, C303 read `.npz` runs of the
  double-null solver passed as a directory argument; C137 and C263 need them only under `--write` (their default runs use
  the pinned `data/rcert5_C3*.npz`). The runs are regenerable with C184/S11 but slowly; the archive must either ship them
  or state the regeneration commands.
- **Cited papers' full texts.** `bundlesweep` and `censusweep` (TEXT) need fetched full texts that are not stored.
- **Version control.** `r9text5` (TEXT) runs `git show` on a past commit; `census9` (TEXT) copies the tree to a temp
  directory and runs `r0census5` by subprocess.
- **Cross-directory imports (141).** `sys.path` inserts into `docket68/n1star`, `docket68/lemmas` and `paper`, and
  file-path loaders. Mechanical in a flat archive, but five basenames occur twice in the tree with different content
  (`uniform5`, `transfer5`: `docket68/n1star/` vs `checks/`; `horizon5`, `trap5`: `docket68/n1star/` vs `proof5/checks/`;
  `gauge5`: `checks/` vs `lemmas/`, the latter uncited), so files must be renamed by number, not copied by name.
- **Libraries beyond sympy.** numpy 111 programs, mpmath 102, scipy 26, python-flint 13 (C126-C129, C136-C138, C250,
  C259, C262, C263, C276, C292), z3-solver 7 (C6, C18, C21, C30, C148, C157, C230); C6 also needs a Lean 4 binary.

## 5. Size of the MATH set

- MATH alone: **317 programs, 105,991 lines**. With MEASUREMENT: 337 programs, 109,502 lines.
- Numbered set C1-C339: 110,245 lines (221 placed in the paper's sections, 118 after it).
- What the archive must actually ship to run them: MATH and MEASUREMENT plus every module they import inside the
  registry, **349 programs, 113,124 lines**, plus the separate programme's chain (25 further files, about 9,700 lines)
  unless C2, C25 and C48 are cut down to the checks the paper cites. TEXT (5,655 lines) is excluded.

## 6. Cleaning burden

- Grades: heavy 61 (MATH 36, TEXT 16, DATA 5, MEASUREMENT 4), light 302, none 6 (`hung4`, `exterior5`, `settle5`, and the
  docstring-less `proof5/checks/dyn5`, `horizon5`, `jac5` once the header comment is checked; `hf_core5` is light only
  through its cross-directory import).
- **Light is not trivial: it is a docstring rewrite almost everywhere.** 282 of 369 docstrings or comment blocks carry
  process words (round numbers of working files, D-numbers, "verifier", "seated", the working names of the supplement's
  files) and 344 carry paths or working-file names. Each needs a new header in the edition's words.
- **Process words in code or printed strings: 42 programs.** By pattern (programs): n1star/N1STAR 19, D-numbers 22,
  verifier 8, seated 4, docket 4 (C30 5, C1 3, C95 2, `r9text5` 1), warp 2 (S3, a module of the separate programme, and
  `r9text5`, which prints the repository path `research/warp-drive/docket68/n1star/SETTLE-GLAM5.md`). Docstrings name
  "warp" in five programs (S1, S3, C145, C176, C227).
- Path strings in code or printed strings: 51 programs; print lines that print a path, a working file name or an md5: C25
  hf_anchor5, C24 hf_core5, S2 hf_mirror5, C6 hf_theorem5, C2 kn_gauge, S4 src_hole, C4 ansatz5, d0count5 (TEXT), C89
  hclass5, C127 lam0data5, C198 lamL5b, C205 lamconst5, C129 m22cert5, C128 m22evol5, C178 mbsign5, nkind5 (TEXT),
  r5edits5 (TEXT), r6edits5 (TEXT), C115 rootavoid5, C196 stagefree5, C194 stagen5, C274 zerohardy5, C5 data5, C18
  foliation5, C3 ks5, C7 lead5, gammac5 (TEXT) (the `basename(__file__)` prints are harmless once files are renamed; the
  others print the supplement's file names, md5s or line numbers).
- Heavy rows and why:

- C1 response5 [MATH]: reads text RESPONSE-HL-5D.md; 1 md5 pins; 6 process words in code/printed strings; 1 path strings
  in code; subprocess; cross-directory imports; docstring/comments: 0 process words, 1 paths
- C2 kn_gauge [MATH]: reads text M-RULINGS-2026-10-03.md; 1 md5 pins; 1 path strings in code; 1 print lines with paths
- C6 hf_theorem5 [MATH]: reads text M-RULINGS-2026-10-03.md; 1 process words in code/printed strings; 2 path strings in
  code; 1 print lines with paths; subprocess; loads separate-programme modules; docstring/comments: 2 process words, 0
  paths
- C9 counterpart5 [MATH]: reads text M-RULINGS-2026-10-03.md; 1 path strings in code; docstring/comments: 2 process
  words, 0 paths
- C14 past5 [MATH]: reads text N1STAR-PROOF.md; 2 process words in code/printed strings; 2 path strings in code;
  docstring/comments: 11 process words, 4 paths
- C20 support9 [MATH]: reads text EFFECTIVE-LEDGER.tsv,PART-*.md; 5 process words in code/printed strings;
  cross-directory imports; docstring/comments: 4 process words, 2 paths
- C25 hf_anchor5 [MATH]: reads text M-RULINGS-2026-10-03.md; 1 path strings in code; 1 print lines with paths; loads
  separate-programme modules
- C30 redshift5 [MATH]: reads text N1STAR-PROOF.md,RESPONSE-HL-5D.md; 18 process words in code/printed strings; 13 path
  strings in code; cross-directory imports; docstring/comments: 35 process words, 4 paths
- C31 rwgauge5u [MATH]: reads text RESPONSE-HL-5D.md,RWGAUGE5.md; 4 path strings in code; cross-directory imports;
  docstring/comments: 6 process words, 8 paths
- C48 seed_escape [MATH]: reads text M-RULINGS-2026-10-03.md; 1 md5 pins; 1 process words in code/printed strings; 1 path
  strings in code; loads separate-programme modules; docstring/comments: 1 process words, 0 paths
- C85 support8b [MATH]: reads text B-MAP.tsv,BASEPOINT-LEDGER.md,DEDUCTIONS.tsv,N1STAR-PROOF.md,PART-VI4-PARAMS.md,; 2
  process words in code/printed strings; 4 path strings in code; cross-directory imports; docstring/comments: 3 process
  words, 17 paths
- C95 gluedecay5 [MATH]: reads text GLUEDECAY5.md,PART-V-GLUING.md,RESPONSE-HL-5D.md; 13 process words in code/printed
  strings; 20 path strings in code; cross-directory imports; docstring/comments: 15 process words, 12 paths
- C110 dnumber5 [MATH]: 3 path strings in code; cross-directory imports; docstring/comments: 4 process words, 4 paths
- C112 l2par5 [MATH]: reads text LOSS-D.md,PART-III-G5-TF.md,PART-III-I12-SPECTRAL.md,PART-III-J3-TAME.md; 2 md5 pins; 4
  path strings in code; docstring/comments: 4 process words, 3 paths
- C113 logind5 [MATH]: reads text PART-III-G3-GRAFT.md,PART-III-G5-TF.md,PART-III-I11-SPACETIME.md,PART-III-I12-SP; 1 md5
  pins; 7 path strings in code; cross-directory imports; docstring/comments: 1 process words, 3 paths
- C114 iotaind5 [MATH]: reads text PART-III-D3-SYMSTATES.md,PART-III-D4-GENSTATES.md,PART-III-F5-PAIRINGS.md,PART-I; 1
  md5 pins; 6 path strings in code; cross-directory imports; docstring/comments: 0 process words, 2 paths
- C115 rootavoid5 [MATH]: reads text PART-III-F2-INDICIAL.md,PART-III-G2-IOTA.md,PART-III-G5-TF.md,PART-III-I10-CORR4; 2
  md5 pins; 21 path strings in code; 1 print lines with paths; cross-directory imports; docstring/comments: 2 process
  words, 5 paths
- C119 inverse6_5a [MATH]: reads text CONSTANTS5.md,EFFECTIVE-CONSTANTS.md,PART-III-D2-ZEROENERGY.md,PART-VI4-PARAMS.m; 1
  md5 pins; 19 path strings in code; docstring/comments: 1 process words, 9 paths
- C127 lam0data5 [MATH]: 4 path strings in code; 2 print lines with paths; cross-directory imports; docstring/comments: 1
  process words, 6 paths
- C128 m22evol5 [MATH]: 5 path strings in code; 3 print lines with paths; cross-directory imports; docstring/comments: 1
  process words, 6 paths
- C137 rich5 [MATH]: 2 md5 pins; cross-directory imports; needs absent data files; docstring/comments: 3 process words, 4
  paths
- C138 rcert5d [MATH]: 1 md5 pins; cross-directory imports; docstring/comments: 14 process words, 5 paths
- C153 late5b [MATH]: needs absent data files; docstring/comments: 2 process words, 5 paths
- C157 r9beyond5 [MATH]: reads text N1STAR-PROOF.md,PART-VII-ASSEMBLY.md; 7 process words in code/printed strings; 18
  path strings in code; docstring/comments: 1 process words, 3 paths
- C182 g1curv5 [MEASUREMENT]: cross-directory imports; needs absent data files; docstring/comments: 55 process words, 10
  paths
- C194 stagen5 [MATH]: reads text N1STAR-PROOF.md; 2 md5 pins; 6 process words in code/printed strings; 3 path strings in
  code; 2 print lines with paths; docstring/comments: 11 process words, 5 paths
- C196 stagefree5 [MATH]: reads text N1STAR-PROOF.md,RESPONSE-HL-5D.md; 2 md5 pins; 2 process words in code/printed
  strings; 4 path strings in code; 1 print lines with paths; cross-directory imports; docstring/comments: 5 process
  words, 3 paths
- C198 lamL5b [MATH]: reads text CONSTANTS5.md,N1STAR-PROOF.md; 2 md5 pins; 2 process words in code/printed strings; 4
  path strings in code; 1 print lines with paths; cross-directory imports; docstring/comments: 5 process words, 5 paths
- C205 lamconst5 [MATH]: reads text N1STAR-PROOF.md; 1 md5 pins; 2 process words in code/printed strings; 2 path strings
  in code; 1 print lines with paths; cross-directory imports; docstring/comments: 4 process words, 6 paths
- C206 lzerotrace5 [MATH]: reads text N1STAR-PROOF.md; 2 md5 pins; 15 process words in code/printed strings; 4 path
  strings in code; cross-directory imports; docstring/comments: 89 process words, 7 paths
- C222 eps1hyp5 [MATH]: 8 process words in code/printed strings; cross-directory imports; docstring/comments: 17 process
  words, 4 paths
- C246 zinv5 [MATH]: subprocess; docstring/comments: 1 process words, 2 paths
- C263 rcert5c [MATH]: 3 md5 pins; cross-directory imports; needs absent data files; docstring/comments: 3 process words,
  3 paths
- C274 zerohardy5 [MATH]: reads text N1STAR-PROOF.md; 2 process words in code/printed strings; 2 path strings in code; 1
  print lines with paths; docstring/comments: 2 process words, 4 paths
- C290 ampresp5 [MEASUREMENT]: needs absent data files; docstring/comments: 1 process words, 6 paths
- C291 cplate5 [MATH]: needs absent data files; docstring/comments: 4 process words, 2 paths
- C292 rcert5b [MATH]: 1 md5 pins; cross-directory imports; docstring/comments: 1 process words, 2 paths
- C293 cplate5c [MATH]: needs absent data files; docstring/comments: 2 process words, 3 paths
- C302 g1amp5 [MEASUREMENT]: cross-directory imports; needs absent data files; docstring/comments: 5 process words, 1
  paths
- C303 g1map5 [MEASUREMENT]: cross-directory imports; needs absent data files; docstring/comments: 8 process words, 2
  paths
- S1 emitter_process [DATA]: reads text M-RULINGS-2026-10-03.md; 1 path strings in code; docstring/comments: 1 process
  words, 0 paths
- S2 hf_mirror5 [DATA]: reads text M-RULINGS-2026-10-03.md; 1 path strings in code; 1 print lines with paths
- S3 source_spec [DATA]: reads text M-RULINGS-2026-10-03.md; 2 process words in code/printed strings; 1 path strings in
  code; docstring/comments: 3 process words, 0 paths
- S4 src_hole [DATA]: reads text M-RULINGS-2026-10-03.md; 1 path strings in code; 1 print lines with paths
- S8 e2trap5 [DATA]: 6 process words in code/printed strings; cross-directory imports; docstring/comments: 11 process
  words, 1 paths
- baire5 [TEXT, unnumbered]: reads text PART-II-A-SETUP.md,PART-II-A2-STANDARD.md,PART-II-F-IOTA.md,PART-III-H-AUGMENT.m;
  13 path strings in code; cross-directory imports; docstring/comments: 1 process words, 2 paths
- census9 [TEXT, unnumbered]: reads text
  LOSS-D.md,N1STAR-PROOF.md,PART-II-G2-DECAY.md,PART-III-J-PARAM.md,RESPONSE-HL-5D; 2 process words in code/printed
  strings; 5 path strings in code; subprocess; docstring/comments: 1 process words, 10 paths
- d0count5 [TEXT, unnumbered]: reads text
  PART-II-A-SETUP.md,PART-II-A2-STANDARD.md,PART-II-C-OPERATORS.md,PART-III-I-CONE; 3 process words in code/printed
  strings; 11 path strings in code; 1 print lines with paths; cross-directory imports; docstring/comments: 16 process
  words, 13 paths
- lzeroaudit5 [TEXT, unnumbered]: reads text N1STAR-PROOF.md,PART-I-C-LOWENERGY.md; 2 md5 pins; 47 process words in
  code/printed strings; 5 path strings in code; docstring/comments: 93 process words, 9 paths
- modcount5 [TEXT, unnumbered]: reads text
  PART-II-G2-DECAY.md,PART-III-I11-SPACETIME.md,PART-III-I12-SPECTRAL.md,PART-III-; 4 md5 pins; 2 process words in
  code/printed strings; 12 path strings in code; cross-directory imports; docstring/comments: 14 process words, 9 paths
- nkind5 [TEXT, unnumbered]: reads text PART-I-B-HIGHENERGY.md,PART-I-C-LOWENERGY.md,PART-II-F-IOTA.md,PART-III-D-GAUGEP;
  7 path strings in code; 1 print lines with paths; docstring/comments: 0 process words, 4 paths
- nrows5 [TEXT, unnumbered]: reads text EFFECTIVE-LEDGER.tsv,PART-*.md,PART-I-B-HIGHENERGY.md,PART-I-C-LOWENERGY.md,PART;
  58 path strings in code; docstring/comments: 3 process words, 3 paths
- ordcensus5 [TEXT, unnumbered]: reads text
  PART-II-A2-STANDARD.md,PART-II-C-OPERATORS.md,PART-II-D-REGULARITY.md,PART-II-D2; 1 md5 pins; 7 path strings in code;
  docstring/comments: 1 process words, 2 paths
- r0census5 [TEXT, unnumbered]: reads text
  BEYOND5-R0.tsv,PART-*.md,PART-III-B-FAMILY.md,PART-III-C2-POLYHOM.md,PART-III-C3; 4 process words in code/printed
  strings; 56 path strings in code; docstring/comments: 10 process words, 3 paths
- r5edits5 [TEXT, unnumbered]: reads text N1STAR-PROOF.md,SETTLE-GLAM5.md; 4 process words in code/printed strings; 4
  path strings in code; 1 print lines with paths; cross-directory imports; docstring/comments: 7 process words, 6 paths
- r6edits5 [TEXT, unnumbered]: reads text N1STAR-PROOF.md,RESPONSE-HL-5D.md,SETTLE-GLAM5.md; 40 process words in
  code/printed strings; 16 path strings in code; 2 print lines with paths; cross-directory imports; docstring/comments:
  29 process words, 7 paths
- r9text5 [TEXT, unnumbered]: reads text SETTLE-GLAM5.md; 1 md5 pins; 3 process words in code/printed strings; 4 path
  strings in code; subprocess; docstring/comments: 0 process words, 3 paths
- vii5census [TEXT, unnumbered]: reads text
  PART-II-C-OPERATORS.md,PART-III*.md,PART-III-B-FAMILY.md,PART-III-D2-ZEROENERGY.; 2 process words in code/printed
  strings; 38 path strings in code; docstring/comments: 19 process words, 9 paths
- vii5read [TEXT, unnumbered]: reads text PART-VII-ASSEMBLY.md,VII5-READING.tsv; 5 path strings in code; cross-directory
  imports; docstring/comments: 12 process words, 6 paths
- admiss5 [TEXT, unnumbered]: reads text
  PART-II-C-OPERATORS.md,PART-II-C2-TRAPPING.md,PART-II-D-REGULARITY.md,PART-II-D2; 12 path strings in code;
  docstring/comments: 1 process words, 0 paths
- gammac5 [TEXT, unnumbered]: reads text
  PART-*.md,PART-III-B-FAMILY.md,PART-III-F-LINEARISED.md,PART-III-F2-INDICIAL.md,; 18 path strings in code; 1 print
  lines with paths; docstring/comments: 6 process words, 2 paths

## 7. Suspicious or noteworthy

- **No program the paper cites is missing**, and all 259 match Appendix D's md5s. The supplement's citations resolve,
  with five path slips: `ROUTES-OPEN.md` cites `checks/horizon5.py`, `checks/trap5.py`, `checks/gammac5.py` and
  `checks/admiss5.py`, which live in `proof5/checks/` (and `docket68/n1star/horizon5.py` and `trap5.py` are *different*
  programs); `LOSS-D.md` cites `checks/iota5.py:44`, which is `docket68/n1star/iota5.py`.
- **Labels the program does not define as a computed check:** `hf_anchor5` A5 is "deduced" (no code check carries the
  label; Appendix A lists A0-A5); `growth5` G4 is described in the docstring but no run is tagged G4 (tags G1-G3, G5).
  `kn_gauge` defines K1-K8 but the paper cites K1-K2; `hf_theorem5` is listed as F1-F5 with "7/7" while the body also
  cites F7 (present in the code). Every other cited label appears in its program's code.
- **Same name, different program:** the paper itself warns "(Not `uniform5.py` above.)"; `transfer5.py` likewise has two
  unrelated versions (C91 the Tangherlini-Minkowski transfer of estimates, C304 a numerical F(0) -> F(1) transfer).
- **The paper's program is imported by a proof program** (C16 imports C1), and C1's `--full` runs five proof programs.
- **TEXT programs whose output the paper uses as a number:** `d0count5`, `modcount5`, `ordcensus5` (d's integer, §9),
  `census9` (§§8.5, 9), `vii5census`/`vii5read` (§8.8), `gammac5`/`admiss5` (§8.8). Excluding them leaves those numbers
  supported only by text unless their census tables are published as data.
- **No-control computations the paper relies on:** C24 (`hf_core5`, the numerical sequence, "numerical, not exact") and
  C116 (`e2meas5`); C182 (`g1curv5`) is cited in §9 with no control. Appendix A's opening sentence says every program
  carries negative controls, but C210 (`e2trapband5`, the certified band bound 11.477 behind section 9's constants) has
  none, C209 (`e2h1band5`) has only a positive control, and the four supplement checks C231-C234 have none.
- **Generated or synthetic inputs that look like files:** `PART-PLANTED.md` (a planted control name in `baire5` and
  `nrows5`), `bbar5_R*.pkl` (optional cache), `census_vals.npy` (scratch output of C138), `hits.tsv` (written by
  `censusweep`).
- Four supplement programs have no docstring at all (C231-C234, `proof5/checks/`); their gists come from header comments.
- `zinv5` (C246) re-launches itself in four subprocesses; `hf_theorem5` (C6) has a hard-coded absolute Lean path.
- `classchi5` (C338) and `jetpoly5` (S10) are cited only by `FAMILIES5-NONROUND.md`, a round document the paper never
  names; consider whether that document is part of the edition's supplement.

