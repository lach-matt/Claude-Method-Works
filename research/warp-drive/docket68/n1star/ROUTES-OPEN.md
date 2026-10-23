# Routes for the three open items (D36)

M, 2026-10-20: "Still open, and stated as open in the paper: - do some deep research on the web and suggest a method
for closing these." The three items are those of RESPONSE-HL-5D.md section 8 and N1STAR-PROOF.md section 10: the mass
at past null infinity, existence at the prescribed wavelength 10 l5, and nonlinear settling. **Nothing here is proved.**
This note is a proposal: for each item, what the literature already settles (READ, with page), what this session
computed for it (`routes5.py`, 2/2, mutants 2/2), the recommended method step by step, and the first step to take.
Sources were read through alphaXiv on 2026-10-20; a search for a nonlinear stability result for five-dimensional
Tangherlini in any class depending on more than (t, r) found none.

| Item | Recommended method | Precedent | First step |
|---|---|---|---|
| Mass at I⁻ | the 5D Bondi law, time-reversed; prove g_λ's expansion | [TTS09], [KK25] | the numerics' coefficient |
| 10 l5 | a posteriori existence: Theorem E with certified numbers | [CCRT07], [MP11], [RT12] | growth factor exp ∫K |
| Settling | generalized wave map gauge in the class, finite modulation | [Hin26], [KS17] | linear stability, L1 |

Recommended order: the mass first (one lemma beyond section 9), then the 10 l5 go/no-go measurement, then the linear
milestone of settling.

## 1. The mass at past null infinity

**What is open.** Section 6 gives the flux at I⁻ exactly (past5.py P7); identifying the numerics' mean mass aspect with
its integral needs a mass law at I⁻ in five dimensions and an expansion of g_λ there beyond r^(−2).

**The law is already published (READ).** [TTS09] set up Bondi coordinates in five dimensions, ds² = −(V e^B/r²) du² −
2 e^B du dr + r² h_AB (dx^A + U^A du)(dx^B + U^B du), h_AB built from C1, C2, C3, D1, D2, D3 (p. 2, (4)–(5)), and find
"C behaves as ∼ 1/r^{3/2} near null infinity" (p. 3), V = r² + V1 r^{1/2} − M + O(r^{−1/2}) (p. 4, (26)), and

    ∂M/∂u = −(1/3)((C11,u)² + C11,u C21,u + (C21,u)² + (D11,u)² + (D21,u)² + (D31,u)²)          ([TTS09] (28), p. 4)

(their appendix writes +M in (A8), the opposite sign, consistently with its (A21)). The r^(−2) term A of C obeys
∂A/∂u = 0 ((35), p. 5) and vanishes, since it vanishes at spatial infinity; the full fall-off is (40), (37)–(39), p. 5:
C to O(r^(−7/2)) through r^(−5/2) and r^(−3), V to O(r^(−1/2)), B to O(r^(−5)), U^A to O(r^(−9/2)). And "there is no
supertranslation freedom unlike in four dimensions" (p. 7).

**It is our flux (computed, routes5.py).** Q2: with D1 = D2 = D3 = 0, which both reflections force, [TTS09]'s form is
the class's ansatz of hf_theorem5.py exactly, diag(e^(−2(P1+P2)), c² e^(2P1), s² e^(2P2)), under θ_T = π/2 − θ and
C = 2P; run backwards in time (u → −v, the squares unchanged), (28) becomes

    ∂M/∂v = +(4/3)(p1_v² + p1_v p2_v + p2_v²),        p_i the r^(3/2) coefficients of P_i,

and M is the Tangherlini μ (g_vv = −1 + μ/r² + …). Q1: five-dimensional Vaidya has R_vv = 3μ'/(2r³) and nothing
else, so Proposition 2.3's −2(P1_v² + P1_v P2_v + P2_v²) gives the same coefficient 4/3. The sphere mean of this
density is the paper's P7 flux. So the five-dimensional mass law at I⁻ is not missing; what is missing is that g_λ is
asymptotically flat at I⁻ in [TTS09]'s sense.

**Method.**

0. *Before any proof (non-rigorous, cheap).* Read the numerics' mean mass aspect after the shell at each λ (hf_core5
   rows) and fit its offset to c λ²; compare c with (2/9) A² ∫ env'². F4 so far records only the quartering ratios.
1. *Bondi coordinates at I⁻.* Solve the eikonal equation for the incoming null function v with v → v* at I⁻, as [HL21]
   construct u at I⁺ from wave coordinates (§3, Proposition 3.2, p. 11); r areal through det h_AB. In the class the
   form stays diagonal; T² fixes only the centre, so no translation or boost survives, and with no supertranslations
   the frame is canonical (deduced).
2. *The expansion to [TTS09]'s order.* Extend Theorem P's decay classes by two half-steps: subtract the leading terms
   as Theorem A_P does and transport the remainder from I⁻ with Z = −r^(1−q) S_q/(q − 5/2), each pass half a power
   better. The resonance at q = 5/2 is where a logarithm would enter; the r^(−2) term of C is [TTS09]'s A, which
   obeys ∂_v A = 0 and vanishes for v < v_start, where the solution is exactly the seed, so A ≡ 0: [TTS09]'s argument
   with the seed in place of spatial infinity. Template for propagating expansions from I⁻ in harmonic gauge: [KK25]
   Theorem B.2 ("EVE scattering", p. 142, with propagation of polyhomogeneity in part c), proved in 3 + 1 ("see
   however Remark 1.9 for the generalisation to other dimensions", p. 15); they also record that "peeling, even for
   fixed angular frequencies, is extremely specific to even spacetime dimensions" (p. 20), so half-integer orders
   are what to expect here, and [TTS09]'s (40) says which.
3. *Conclusion.* With 1–2, (28) time-reversed holds for g_λ, and integrating its sphere mean with P7 gives the Bondi
   mass at I⁻ after the shell, μ + (2/9) λ² A² ∫ env'² + O(λ³). That closes the item and predicts the numerics' c.

**Alternative.** [HL21] define the mass at null infinity in harmonic coordinates "in three different ways that we show
satisfy the Bondi mass loss law" (p. 1), and the three coincide (Remark 1.5, p. 5). The asymptotic Hawking mass of the
wave-gauge spheres needs only the leading shear and o(r^(−2)) control of the mass term, possibly less than step 2.
Matching the numerics' mass aspect, which is a Bondi quantity, still needs step 1.

## 2. Existence at the prescribed wavelength 10 l5

**What is open.** Existence on D_T of the vacuum solution with the record's data at λ = 10 l5, where λ/r is 0.32 to
1.85 (R7). The amplitude gives no small parameter either: hf_core5's seed is "mu0 = 1 with the shell bringing 0.18",
so an expansion in the wave amplitude would run in about √0.18 ≈ 0.4 (an assessment, not computed).

**Method: a posteriori existence, Theorem E with certified numbers.** Theorem E is already of this shape: an
approximant, its residual, a linear energy estimate and a quadratic remainder. At fixed λ, replace each power of λ by
a computed, rigorously bounded number and close with a control inequality. Precedents (READ):

- [CCRT07] prove "a robustness theorem for strong solutions, from which we derive an a posteriori check that can be
  applied to a numerical solution to guarantee the existence of a strong solution of the corresponding exact problem"
  (p. 2). The check is (21), p. 15: ‖u(0) − v0‖ + ∫‖residual‖ < (c T)^(−1) exp(−c ∫(‖u‖_m + ‖u‖_(m+1))). The Euler
  case, quasilinear hyperbolic, is their Theorem 4 (p. 12).
- [MP11] sharpen this to a control inequality, d⁺R/dt ≥ −νR + (G D_n + K D_(n+1)) R + G R² + ε_n with R(0) ≥ δ_n
  ((1.10), p. 2). It gives existence on [0, T_c) and ‖u − u_a‖ ≤ R (Proposition 4.5, p. 13), with explicit constants
  K_3 = 0.323, G_3 = 0.438 ((7.7), p. 28), applied to a computed Galerkin solution (§7).
- [RT12], in general relativity: "The proof is computer assisted. Starting from an explicit approximate solution, we
  show that nearby there is a true solution" (p. 1); "This paper may be the first in general relativity" (p. 9).
  They use integer arithmetic and a Neumann series for the linear inverse (pp. 8–11), and a separate system shows the
  constraints vanish (pp. 18, 27), which is the place of D = 0 here.

The steps:

1. *Pose it on the orbit space.* Use the 2+1 system (2.2), the metric h with the flat-target pair (ψ̃, ω), in the wave
   map gauge of section 2.5 reduced, on (v, r, ζ) with the axes ζ = ±1 by parity. Two plus one dimensions, not four
   plus one.
2. *Approximant.* Solve numerically at λ = 10 l5 in the same gauge, re-solving or mapping hf_core5's Bondi-type
   solution through a certified coordinate change. At this λ the waves are resolved on a coarse grid. Store the result
   as piecewise polynomials with rational coefficients.
3. *Certified residual.* Compute ε(t) = ‖Ric^H(g_app)‖ in H^k(Σ_t) and the data error δ by ball arithmetic
   (python-flint's arb, on PyPI).
4. *Certified linear constants.* Take K(t) from enclosures of ∂g_app and ∂²g_app and the energy current's coercivity
   (the hyperbolicity margin). Check Proposition 3.2's spacelike condition for g_app at x_K = 1, and at the outer
   boundary, with a certified margin, so that the boundaries are outflow and take no condition. Take C_Q, the
   constant of the quadratic remainder, from explicit Sobolev and Moser constants on the slices, as [MP11] did for
   K_n and G_n.
5. *Close.* If the control inequality's solution R stays below the hyperbolicity threshold on [0, T], the solution
   exists on D_T with ‖g − g_app‖ ≤ R(t). D = 0 propagates as in Theorem E. The data come from Theorem D's outward
   ODE in r, certified by validated integration; the radii-polynomial method has a Lean 4 framework
   (arXiv:2610.02335) if the certificate is to be machine-checked.

**Go/no-go first.** The one number that decides feasibility is the growth factor exp ∫ K dt over D_T, measured
non-rigorously on the numerical solution; it sets how small ε must be. If it is very large (the large coefficient of
section 5.1 near the horizon), split D_T into slabs with re-centred approximants. [MP11]'s inequality is applied per
interval.

**What it would buy.** Existence at 10 l5 with explicit error bars. The record's question at that wavelength (the
escape through the barrier, seed_escape.py E2–E4, now linear) can then be asked of the nonlinear solution with
certified bounds.

## 3. Nonlinear settling

**What is open.** Nonlinear stability of five-dimensional Tangherlini in the T²-mirror class, and the continuation of
the solution outside D_T.

**Where the field stands (READ).**

- In four dimensions the problem is now closed. [KS17] treat perturbations with "a hypersurface orthogonal spacelike
  Killing vectorfield" (p. 17): "To a large extent, the restriction to this class of perturbations is only needed to
  ensure that the final state of evolution is another Schwarzschild space" (p. 2). They pose their data on null cones
  C1 ∪ C̲1 (p. 30). [DHRT21] prove codimension-three stability of Schwarzschild. [Hin26] settles full subextremal Kerr:
  "We use a generalized wave map gauge modified using gauge source terms that lie in a suitable finite-dimensional
  space ... Like the final black hole parameters (mass and angular momentum) and the gravitational wave tail, the
  gauge source terms are treated as unknowns in a nonlinear (Nash–Moser) iteration scheme. We work directly with the
  tensorial equation and in particular do not rely on reductions to scalar equations" (p. 1). The linear inputs are
  mode stability away from zero frequency, the resolvent at zero energy and constraint damping (p. 4, Theorem 7.1,
  p. 136).
- In five dimensions, linearly: [IK03], and [HKW18]'s τ^(−2) decay of the master quantities, with the metric
  components "not treated". Nonlinearly, only classes whose reduced problem is 1+1: [Hol08], and Dafermos and Holzegel's
  triaxial Bianchi IX (gr-qc/0510051).

**Why the class makes it tractable (deduced; computed where marked).**

- Both reflections make both Killing fields hypersurface orthogonal, so there is no rotation (settle5.py T1) and the
  final state is Tangherlini. This is [KS17]'s polarization.
- T² fixes only the centre, and the invariant harmonics have even degree, so l = 1 is absent. No translation, boost or
  rotation survives, and the only final parameter is the mass. [KS17] had to track motion along the axis and [Hin26]
  a boost; here a codimension-zero statement within the class is expected.
- There are no supertranslations ([TTS09] p. 7).
- Only scalar and tensor types occur, on l = 2k. The tensor type is a wave on the copper barrier (settle5.py T2).
- The reduced problem (2.2) is 2+1 gravity with a flat-target pair, the polarized structure.

**Method: [Hin26]'s route, in the class.** The construction already lives in a wave map gauge relative to g0 (section
2.5). Continue in that gauge, with g0 interpolating to the final Tangherlini and the final mass plus finitely many
gauge source terms as unknowns. Pose the late-time problem as [KS17] do, on null cones: data on {v = v_end} from
Theorems 1 and P, and no incoming radiation at I⁻ for v ≥ v_end, since the record's waves have ended there.

- L1, the first milestone, a paper on its own: linear stability of five-dimensional Tangherlini in a generalized wave
  gauge within the class, with decay of every metric component. This closes [HKW18]'s stated gap in the class. It
  needs mode stability at σ ≠ 0 from [IK03]'s master equations, and the zero-energy structure, where l < 2 is gauge
  plus δμ ([HKW18] Theorem 1). The four-dimensional templates are Johnson's generalized wave gauge paper and Hung, Keller
  and Wang's in the Regge-Wheeler gauge (both cited in [Hin26], p. 6).
- L2: constraint damping in five dimensions ([Hin26]'s companion [Hin26a]).
- L3: decay rates in the class (r^p hierarchy; [Sch13]'s higher-dimensional estimates; [HKW18]).
- N: the nonlinear iteration of [Hin26], or a bootstrap with these rates.

The low-energy analysis is where five dimensions differ: the spatial dimension is four. It must be redone, not copied.

**Cheap companion (computed, to do).** Extend settle5.py T3 to show no growing mode in the class for l = 2, …, 10, and
measure the late-time tail of the l = 2 master fields. That fixes the decay rate the nonlinear step must use.

## Status, the same day (D37-D44)

1. *The mass at past null infinity: closed.* Theorem M (N1STAR-PROOF.md section 11; the paper's Theorem 3): Bondi
   coordinates on g_lam at past null infinity, the hierarchy recomputed in the class with every coefficient from s^1
   general (bondi5.py B1-B3), the mean mass mu + (2/9) lam^2 A^2 int env'^2 + O(lam^3) after the shell. Read by the
   twelfth verifier: no major finding, five minor repaired in place (D40). Step 0 first: the solver's offset/lam^2 ->
   0.4569 against the law's 0.45693 (B4, R8).
2. *The go/no-go at 10 l5: measured, growth5.py (D38, D41, D43; section 10.2).* At both seeds the scheme's premise
   fails before the shell's peak: the round spheres' expansion acquires a second zero holding over 0.04 in v from 1.500
   (mu0 = 100 l5^2; 1.496 on the finer grid; 1.476 with a hold of 0.008) and from 1.583 (1000 l5^2, three grids to
   0.0005), and the core boundary ceases to be outflow within 0.1 after; a deeper excision fails earlier, not later (r =
   0.39 and 0.25 r_h at the first seed, 0.21 r_h at the second). So no approximant on D_T comes from the record's own
   scheme at 10 l5 at any excision depth: in the stored samples a column loses every zero of its expansion and the zero
   of W moves inward to the boundary; the direction of the untrapping is not a measurement of these runs, and nothing is
   said of the event horizon (D45). The step is re-posed as the characteristic initial value problem in double-null
   gauge -- the incoming wave on an ingoing null hypersurface from past null infinity, the seed's outgoing cone from
   inside x_K = 1 -- where Luk's theorem gives local existence without smallness ([Wu26] Theorem 2.1) and [Wu26]'s
   Theorem 2.2, the metric controlled by the curvature residues, is the a posteriori structure; its five-dimensional
   version in the class, a 2+1 problem, is not built. To the break the radiation field's growth factor is 1.9 and 2.1
   and the finite-difference amplification along one direction of the data, a lower bound for the propagator's norm,
   1.28 and 1.00; in the record's own regime (lam = 0.1, the control, complete) they are 6.9 and 1.71, while the
   sup-norm Groenwall factor exp int K_all is 17 and 2e5 at 10 l5 and 6e3 in the control: the certified argument would
   have to carry the propagator's norm, as [MP11] do, not a sup-norm bound.
3. *Settling: the linear milestone in the class, as far as [KI03] carries it (D39, section 10.3).* Every metric
   component in the Regge-Wheeler-type gauge f_a = 0 = H_T is a combination of [HKW18]'s master quantities and their
   derivatives to order two -- two orbit-space derivatives, and the factor l^2 that Phi~ carries, through F and the
   trace of F_ab -- (Proposition 10.1, deduced), so linear settling of the components follows at their rate; L1 proper
   (the wave-map gauge) stays open. The cheap companion ran: no growing mode for l = 2, ..., 10 to tau = 275 r_h
   (settle5.py T5, a finite-time observation) and the l = 2 tail t^-7, [CYDL03]'s law (T6). The passage to the harmonic
   gauge then (D42, section 10.4, wavegauge5.py): Hung's four-dimensional structure ([Hun19], arXiv:1909.06733) computed
   in five dimensions in the class -- the tensor type needs no gauge vector, the scalar one solves three 1+1 wave
   equations per mode with the master field as source, and the l = 0 sector's W* and K* are explicit; L1 now rests on
   the decay estimate for that system, which does not exist in five dimensions.

## 4. Settling proper: the decay of the gauge-vector system, and the nonlinear problem (D46)

Section 3 ended where the literature ends: in the class every metric component settles in the Regge-Wheeler-type
gauge (Proposition 10.1), the passage to the harmonic gauge is computed in its explicit parts (Proposition 10.2,
wavegauge5.py W1-W5), and the decay estimate for the gauge-vector system -- Hung's sections 5-8 in five
dimensions -- exists nowhere. This section proposes how to get it (route A), and how the nonlinear settling would
then be closed (route B), with the literature READ at source on 2026-10-20 and one new computed input (W6). Nothing
in it is proved.

### 4.1 What exists

- **[Hun19]** (P.-K. Hung, arXiv:1909.06733v1, the even part in four dimensions). Theorems 1.1-1.4: a one-form solving
  box W = 0 decays at tau^(-2+) in energy after its l = 0 part is subtracted; so does h solving the harmonic gauge and
  the Lichnerowicz equation; the l = 0 part of W converges to c W*, W* = dt/r + (2M/r^2) f^-1 dr (8.1); and h_(l=0)
  converges to c_1 K* + c_2 pi_{W*}, K* = K + pi_{W**} (8.39) growing linearly in t. The mechanism (sections 4-8): h is
  split into seven components whose zeroth-order matrix A + B + O in box H = (A + B + U) H is semi-positive (Proposition
  4.2, Remark 4.5), which gives red-shift and r^p estimates near the horizon and null infinity (Proposition 4.1); a
  gauge vector W = (W_0, W_1, W_2) carries h to the Regge-Wheeler gauge, determined by invertible angular operators for
  l >= 2 ((4.11)-(4.13)); the trace S_W of pi_W, and P_even and Q_even -- components of dW when S_W and the Zerilli
  field vanish ((4.18)-(4.20)) -- satisfy with W_0, W_1, W_2 a *triangular* system of scalar wave equations with
  potentials and sources (Proposition 4.7, (4.21)-(4.25)): box S = 0, box P_even = d_t S_W, and box W_0 + (2M/r^3) W_0 =
  -(2M/r^3) P_even + (Zerilli terms)                                           (4.21) and its two companions; each rung
  is an inhomogeneous wave equation with a radial potential V treated by the vector field method of Appendix A under the
  single condition l_0(l_0 + 1)/r^2 + V >= 0 ((A.3)) -- red-shift, Morawetz and the r^p hierarchy of Dafermos and
  Rodnianski, Schlue's commutators L and rL, Angelopoulos-Aretakis-Gajic's r^2 L -- with a modification W_0 -> W_0 +
  eta_b (...) absorbing a source that grows like u + r ((4.35)-(4.36), Lemma 4.9). The l = 0 sector (section 8): if
  P_even and S_W vanish the one-form is stationary and solves an ODE in r with two solutions, one regular at the horizon
  (W*); with P_even and S_W decaying, the coefficient of the singular solution decays by the red-shift estimate (Theorem
  8.1); K does not satisfy the gauge (Gamma[K] = dv/R^2) and K* repairs it. - **[HKW18]** (arXiv:1809.05144v1). Theorem
  2: the gauge-invariant master quantities of the scalar and tensor type decay at tau^-2 in energy in spacetime
  dimension six and below, uniformly in l (section 10.5: the potentials converge as l -> oo); the metric components are
  deferred ("We do not treat this matter in the current paper", p. 4), and Hung's wave-map gauge work is named there as
  "more promising". The tools are stated for a general Regge-Wheeler-type equation (Definition 8: V radial, bounded,
  comparable to 1/r^2 at infinity, not necessarily non-negative): the T-energy comparison (111), the Morawetz current
  with Schlue's f vanishing at the photon sphere (Lemma 13, (119)-(123); for n = 3 the choice f = (1 - 4M/r^2)(1 -
  M/r^2 + 4M^2/(5r^4)), beta = 1/2, section 9.3.2), the r^p hierarchy with Phi = r^(n/2) Psi for 1 <= p <= 2
  (Proposition 15, Theorem 16) requiring V = a_0/r^2 + b_0 M/r^(n+1) + ... with a_0 > 0, and the decay theorem (Theorem
  18). The restriction to six dimensions is the near-horizon positivity of the Morawetz current, impossible by their
  construction for n >= 5 (section 9.3.2). - **[Sch13]** (V. Schlue, arXiv:1012.5963, Anal. PDE 6 (2013)). For the
  scalar wave equation on Schwarzschild of spatial dimension n >= 3 (five spacetime dimensions is n = 4 there):
  E[phi](Sigma_tau) <= C D/tau^2 (Theorem 1, (1.9)), the first-order energy at tau^-(4-2delta) on bounded r ((1.10)),
  and r^((n-2)/2)|phi| <= C D/tau^(3/2-delta) (Theorem 2); the photon sphere at r = (nm)^(1/(n-2)) (section 2), r^2 = 2
  mu here; radial multipliers f(r*) d_r* changing sign at the photon sphere with Poincare on the spheres (section 4);
  the p-hierarchy with r^p d_v* on psi = r^((n-1)/2) phi, p in {1, 2}, and the commutation with d_v* for the four-step
  hierarchy (section 5). No potential and no source are treated there; Hung's Appendix A says how both enter. -
  **[CYDL03]**: the tails t^-(2l+3) in five dimensions, measured here as T6. - **[KI03b]** (H. Kodama, A. Ishibashi,
  arXiv:hep-th/0308128v4). The Maxwell field on the n+2-dimensional static black hole, scalar type: F_ab = epsilon_ab E
  S, F_ai = r epsilon_ab E^b S_i at Q = 0 ((5.10b), p. 17, as the twenty-sixth verifier read at source; this entry had
  F_ai = E_a S_i), with E_a = (k/r^(n-1))(D_a A + J~_a) (5.17), r^n E = -k^2 A at Q = 0 (5.19), and the master equation
  r^(n-2) D^a (D_a A / r^(n-2)) - (k^2/r^2) A = -r^(n-2) D^a (J~_a / r^(n-2)) (5.20) -- no potential beyond k^2/r^2 in
  that normalisation; the vector type (4.23) has (k_V^2 + (n - 1)K)/r^2. - **[Hin26]** (P. Hintz, arXiv:2606.28253v2,
  with [Hin26a] arXiv:2606.27658 and [Hin26c] arXiv:2606.28008). The nonlinear stability of subextremal Kerr in a
  generalized wave map gauge Upsilon(g) - theta = 0 whose source theta lies in a finite-dimensional space, with strong
  constraint damping (the modified symmetric gradient delta*_{g,E^C}) and a Nash-Moser iteration; "we work directly with
  the tensorial equation" and use as black boxes the mode stability of the ungauged linearized equation (via Teukolsky,
  by Andersson, Hafner and Whiting, cited there) and of two 1-form wave operators -- the gauge potential operator
  box^Upsilon = 2 delta_{E^Upsilon} G delta* and the constraint propagation operator box^C (section 1.4.1): "mode
  stability for [both] implies mode stability for the gauge-fixed linearized Einstein operator L_b, and a simple
  structure of its (generalized) zero energy nullspace". That nullspace on Kerr is the linearized Kerr family in gauge,
  the deformation tensors of asymptotic translations, and (generalized) those of boosts -- a second-order pole of the
  resolvent at zero energy, "forward solutions of L_b lose two powers of t_*-decay". The constraint damping must satisfy
  (1.43): no indicial root of the zero energy operator of box^C with real part in [-C_0, 1), C_0 = 100, which needs a
  non-perturbative E^C ([Hin26a]); mode stability of box^Upsilon at zero energy is arranged perturbatively (Proposition
  6.12), since the plain 1-form wave operator has a zero energy bound state ([Hin26c] p. 21, citing Andersson, Hafner
  and Whiting) -- Hung's W*. [Hin26c] gives the tame estimates for wave-type operators whose stationary model is mode
  stable and may carry zero energy bound states ("examples include the wave operator on 1-forms and the linearization of
  the Einstein field equations in generalized harmonic gauge"), "in 3 + 1 dimensions for concreteness" (Remark 5.6),
  with the Minkowskian zero-energy structure stated in general spatial dimension n: the wave operator on tensors is
  tf-admissible with all weights in the indicial gap (0, n - 2) (Proposition 9.40). - **The 2+1 reductions.** [KS17]
  (Klainerman-Szeftel, arXiv:1711.07597): nonlinear stability of Schwarzschild under polarized axisymmetric
  perturbations, a 2+1 problem. [Hun15] (C. Huneau, arXiv:1511.07002): nonlinear stability of Minkowski with a
  translation Killing field, where "the 3 + 1 vacuum Einstein equations reduce to the 2 + 1 Einstein equations coupled
  to a wave map". [HL17] (Huneau-Luk, arXiv:1706.09499): the polarized U(1) Einstein equations in an elliptic gauge, the
  setting of the theorem this paper answers. [Hol08]: the five-dimensional biaxial class, a 1+1 problem, closed by
  vector field multipliers and a bootstrap.

### 4.2 What the class removes

Deduced from the symmetry, not from an estimate. (i) The perturbations are scalar type on the even harmonics P_k(cos
2theta), one per l = 2, 4, ..., plus the tensor type, which needs no gauge vector (W5); there is no vector type and no
rotation (T1). (ii) There is no translation and no boost: a vector fixed by both rotations of the T^2 is zero, since the
two planes of rotation span R^4, so the asymptotic translations and the generalized boosts that give Kerr's zero-energy
nullspace its second-order pole ([Hin26] section 1.4.1, the boosts) are absent, and the only parameter of the final state
is the mass. (iii) The l = 0 sector is one function of (t, r) for each of two components, with W* and K* explicit (W2,
W3). (iv) The angular eigenvalue starts at k^2 = 8, so Hung's condition (A.3) reads 8/r^2 + V >= 0 at the lowest mode,
and the Morawetz borrowing from the angular term (HKW18 (98), Schlue section 4.2) has room. What the dimension changes:
the weights r^(n-1)/2 = r^(3/2) in place of r in the r^p identity ([Sch13] (5.11)-(5.12)), the photon sphere at r^2 = 2
mu, the flat tails t^-(2l+3) ([CYDL03]), and the indicial gap (0, 2) at zero energy ([Hin26c] Proposition 9.40, n = 4).

### 4.3 Route A: the decay of the gauge-vector system, Hung's architecture in five dimensions

The object: X solving box X = J := -Gamma[h_RW] per mode (W4), where h_RW is the Regge-Wheeler-type gauge metric of
Proposition 10.1, whose components are the master field's derivatives to order two and decay at [HKW18]'s rate; and
the l = 0 one-form. L1 follows from the decay of X: h = h_RW - pi_X.

1. *The triangular system (computed, W6).* With S := div X, F := dX, P := F_tr/S_l, Q_t := -F_{t th}/S_l' and
   Q_r := -F_{r th}/S_l' (S_l the harmonic), and box_l := -f^-1 d_t^2 + f d_r^2 + ((3r^2 - mu)/r^3) d_r - k^2/r^2 the
   scalar wave operator at mode l, seven identities hold in X, exactly
   (at l = 2 in the selftest; at l = 4 under --l4, where all seven pass
   and the control fails, in 72 minutes):
       div(box X) = box_l (div X),
       (box X)_t = box_l X_t + (2 mu/r^3) P,
       (box X)_r = d_r S - f^-1 d_t P - (k^2/r^2) Q_r,
       r (box X)_L = box_l (r X_L) - (2 k f/r) Q_r,
       (box X)_t = d_t S - (f/r^3) d_r (r^3 P) - (k^2/r^2) Q_t,
       d(box X)_tr = box_l P - ((3 r^2 - 9 mu)/r^4) P - (2 k^2/r^3) Q_t,
       box_l (r P) + (4 mu/r^4) r P = r d(box X)_tr + 2 (d_t S - (box X)_t).
   So for box X = J: S solves the free scalar wave equation with source div J; r P solves the scalar wave equation
   with the potential -4 mu/r^4 and a source in S and J -- the Maxwell master equation of [KI03b] (5.20) at n = 3 in
   another normalisation (their A = -r^3 P/k^2); X_t solves box_l X_t = J_t - (2 mu/r^3) P, with no potential; r X_L
   solves the scalar wave equation with source (2 k f/r) Q_r + r J_L, where Q_r = (r^2/k^2)(d_r S - f^-1 d_t P - J_r)
   is algebraic in the rungs below; and X_r = Q_r - d_r(r X_L)/k is algebraic. Hung's condition (A.3) holds on every
   rung: V = 0 for S, X_t and r X_L, and V = -4 mu/r^4 for r P gives k^2/r^2 - 4 mu/r^4 >= 0 for r^2 >= 4 mu/k^2,
   true on the exterior for k^2 >= 8. The counterpart of [Hun19] (4.21) carries no potential where four dimensions
   has 2M/r^3, and X_r needs no wave equation where four dimensions has (4.22).
2. *The rungs.* In order: S (free wave, source div J); A (Maxwell master, source from J and dS); X_t (source
   (2 mu/r^3) P + J_t, no potential); r X_L (source (2 k f/r) Q_r + r J_L, no potential); X_r algebraic. Each rung is an
   inhomogeneous scalar wave equation with a radial potential on five-dimensional Tangherlini, and the proposition to
   prove for it is the five-dimensional form of [Hun19] Appendix A: the red-shift estimate ([Sch13] Proposition
   3.1), the Morawetz estimate with a current of the form HKW18 (122) and f changing sign at r^2 = 2 mu (the choice
   of f and beta is the computation HKW18 made for the master potentials in section 9.3.2 and 10.4.2, to be redone
   for V_r, V_L and for the Maxwell potential), the r^p hierarchy on r^(3/2) X with 1 <= p <= 2 ([Sch13] section
   5.2, HKW18 Proposition 15 -- whose a_0 > 0 is supplied by k^2 >= 8), and Theorem 18's dyadic argument with the
   source carried in the r^p-weighted norm (Hung's Decay[.] norms, (5.1)). The sources are controlled by the rung
   below and by [HKW18] Theorem 2 for J, at the cost of the derivatives (10.1) spends: this is where "the loss of
   two derivatives" of Proposition 10.1 and Hung's K^{<= 8} enter.
3. *The growing source.* J contains the master field with coefficients bounded in r, but the gauge vector that
   carries h to h_RW is determined by inverting angular operators ((4.11)-(4.13)) and its P-type component is sourced
   by d_t of the master field: in four dimensions this made a source growing like u + r, absorbed by the modification
   (4.35)-(4.36). The five-dimensional modification must be found in the same way, from the explicit sources of W6.
4. *The l = 0 sector.* The one-form W_0 dt + W_1 dr: S and P := F_tr solve closed equations (box S = 0; P's equation
   from the Maxwell system at k = 0); if both vanish W is stationary and solves W2's ODE, whose regular solution is
   W*; with S and P decaying, the singular coefficient decays by the red-shift estimate, as in [Hun19] Theorem 8.1.
   Then h_(l=0) = c K + pi_W -> c K* + c_1 pi_{W*} with K* of W3 ([Hun19] Theorem 8.7).
5. *The sum.* One harmonic per even l, constants uniform in l by the Poincare inequality and the convergence of the
   potentials (HKW18 section 10.5); the statement obtained: in the harmonic gauge, h - h_(l=0) decays at tau^(-2+) in
   energy with the loss of a fixed number of derivatives, and h_(l=0) -> c K* + c_1 pi_{W*}, the mass change growing
   linearly in t as in four dimensions -- L1 in the class.
6. *What is new in five dimensions and must be done, not quoted.* (a) The Morawetz current for the Maxwell
   potential -4 mu/r^4 at n = 3 (HKW18's construction is specific to each potential; the other rungs are the free wave,
   [Sch13]'s). (b) The lower-order terms of the
   r^p identity with the weight r^(3/2) ((5.11)-(5.12) of [Sch13]). (c) The semi-positivity of the zeroth-order
   matrix of the harmonic-gauge Lichnerowicz system in the class's components (Hung's Proposition 4.2), which gives
   the red-shift and r^p estimates for h itself (Proposition 4.1): W7, computed (4.6). (d) The l = 0 ODE and red-shift
   argument. None of (a)-(d) needs an idea absent from [Hun19], [HKW18] and [Sch13]; each is a computation and an
   estimate in a dimension where the three papers already did the analogous one.

### 4.4 Route B: the nonlinear settling in a generalized wave map gauge

Route A gives L1, the linear decay in the gauge the nonlinear problem uses. The nonlinear step that has closed in
four dimensions is [Hin26]'s, and its inputs read as follows in the class.

1. *Mode stability of the ungauged linearized equation* is in hand in every dimension: [IK03] for the master
   equations, strengthened to uniform boundedness by [HKW18] (Theorem 2, (6)); in four dimensions this is the role of
   the Teukolsky mode stability in [Hin26] -- the one black box there that took a separate theorem.
2. *Mode stability of the two 1-form operators.* The gauge potential operator box^Upsilon on five-dimensional
   Tangherlini has, unmodified (E^Upsilon = 0), the zero energy state W* (W2); the perturbative modification E^Upsilon
   that removes it ([Hin26] Proposition 6.12) is a static argument and should carry. The constraint propagation operator
   box^C needs the strong damping (1.43), and [Hin26a]'s construction is on Kerr; a five-dimensional construction did
   not exist and is the first genuinely new object of the route. Tangherlini being static, the indicial-root computation
   it needs is an ODE problem in r for each l of the class. Its indicial half is computed (4.13; N1STAR-PROOF.md 10.12),
   the semiclassical inputs of the construction (4.14; 10.13), and a five-dimensional c of his Proposition 5.1's kind on
   Tangherlini (4.15; 10.14), the zero energy inputs of the modification E^Upsilon (4.16; 10.15), the mode stability of
   the unmodified operator at nonzero frequency (4.17; 10.16), the trapping input of the high energies (4.18; 10.17),
   its structure and thresholds (4.19; 10.18), the remaining inputs of [Hin26c]'s estimates at nonzero frequency (4.20;
   10.19), its low-energy theory (4.21; 10.20), [Hin26a] section 6 for the constraint propagation operator (4.22;
   10.21), the inputs of his Theorem 5.2 (4.23; 10.22), and those of his Theorem B.1 (4.24; 10.23): with the trace
   weight 2/(D - 2) in place of his 1 the strip is clear at a point below the five-dimensional bound of his Lemma 4.4, h
   < e chosen here, the c's conditions hold at that e, and the unmodified operator's (E^Upsilon = 0) zero energy kernel
   is W* alone, with pairings that let a horizon modification remove it, and it has no mode at sigma != 0, Im sigma >=
   0, in a class (deduced); box^Upsilon is strongly trapping admissible at the photon sphere r^2 = 2 mu (deduced); S-bar
   has his spectrum (computed) and its horizon threshold is 3/2, for 10.15's c_H (deduced); at R_in the threshold is
   -1/2 - S-bar (deduced from a computed similarity) and at the photon sphere the loss is as small as wished (computed
   at a point, deduced on the trapped set), so that [Hin26] Propositions 6.5 and 6.9 hold there on the reading that
   [Hin26c] section 9's scalar estimates hold on bundles and his Theorems 9.5 and 9.16 restated at n = 4 (deduced); with
   [Hin26c]'s low-energy theory at n = 4 the operator is tf-admissible and its zero energy operator of index 0, so that
   [Hin26] Proposition 6.12 holds there on the same reading (deduced): box^Upsilon with 10.15's modification is mode
   stable on the closed upper half plane; and, with his Theorem 5.2 there on the reading that his 3b-analysis carries to
   five dimensions (4.23; its inputs computed or deduced from computed quantities), the constraint propagation operator
   has no outgoing mode at sigma != 0, Im sigma >= 0, and, at one parameter point, an invertible zero energy operator on
   l in [-C_0 - 2, 0), [Hin26a] Theorem 6.2 (deduced; the horizon threshold its Fredholm property needs is OPEN); with
   his Theorem B.1 on 4+1 Minkowski on the same readings (4.24; its numbers computed), the constraint propagation
   operator is tf-admissible for every beta in [-C_0, 2) at that point, for C_0 <= 100 and h = 10^-6 if that is below
   h_0, [Hin26] Theorem 7.1(4) (deduced); the linearized gauge-fixed Einstein operator's indicial roots are those of his
   Lemma 8.4 in five dimensions, its gap beginning at 0, for every l at that point (4.25; the factorization computed,
   the roots at the point for l <= 12, the rest deduced), so that his Lemma 8.5 and, with his Lemma 8.2's S-bar computed
   (4.26; min spec S-bar = 0, his (8.7)), his Proposition 8.6, for small gam_Ups, hold on the same readings (deduced),
   and 2 L is strongly trapping admissible, his Proposition 8.3 (4.27; deduced); the linearized Einstein operator on
   Tangherlini has no outgoing mode but pure gauge at sigma != 0, Im sigma >= 0, so that his Proposition 8.8 holds on
   the same readings (4.28; the reduction computed, the rest deduced); his section 6.5.1's zero energy states and
   Proposition 8.9's gauged linearized metrics hold one order faster in rho and without his logarithms, on his Lemma
   6.13 in five dimensions (4.29; the orders and exponents computed, the rest deduced); his Lemma 6.13 and Proposition
   6.18 (1)-(3) hold there too (4.30; the leading terms computed, the rest deduced); the line-by-line readings of
   [Hin26a] sections 2.3 and 5.2 and Appendix B and of [Hin26c] section 9 at n = 4, and the rest of the item, [Hin26]
   Proposition 6.18 (4)-(7) and sections 7.2, 8.4 beyond Proposition 8.9 and 8.5, are OPEN.
3. *The zero-energy nullspace in the class* is the mass change in gauge (4.2(ii)), and in the harmonic gauge of
   W1-W6 it is not simple: K* = t pi_{W*} + (stationary) with Gamma[K*] = 0 (W3) is a t-linear zero-energy state, the
   second-order structure. Whether the five-dimensional E^Upsilon of item 2 removes W* and leaves a first-order pole,
   so that the forward solutions lose one power of t_* rather than two and no centre-of-mass or momentum
   elimination ([Hin26] section 1.4.2) is needed, is OPEN: it rests on item 2, not on the symmetry (D47).
4. *The tame estimates* of [Hin26c] in 4 + 1: the microlocal pieces -- edge-b near null infinity, 3b in the forward
   cone, normally hyperbolic trapping at r^2 = 2 mu -- are stated in 3 + 1 "for concreteness" with the general-dimension
   conventions in [Hin23c] section 3.1.2; the zero-energy indicial gap is (0, 2) (Proposition 9.40). Rewriting the
   framework in 4 + 1 is work, not a new idea.
5. *The iteration* is then [Hin26]'s: gauge source terms in a finite-dimensional space, which in the class reduce to
   the mass and the pure-gauge l = 0 terms; the final state is Tangherlini of the final mass. In the class and on the
   domain of Theorem E this would be the nonlinear settling the paper leaves open, with the rate [Hin26] obtains in
   compact sets, t_*^(-2-eps), expected to improve with the tails t^-(2l+3).

The alternative is the 2+1 reduction: both Killing fields are hypersurface-orthogonal in the class (the reflections
exclude dphi_1 dphi_2 and the twists), so the SL(3, R)/SO(3) sigma model of two commuting Killing fields reduces to
the flat-target pair (psi~, omega) of section 2 -- 2+1 gravity coupled to a flat wave map, the exact analogue of the
polarized U(1) class of [HL17] and [Hun15] with two scalars for one, and of [KS17]'s polarized axisymmetry. [KS17]
closed Schwarzschild there with a generalized-covariant-modulated gauge, in 2+1, and the five-dimensional counterpart
would follow their architecture with the two scalars; [Hun15] closed Minkowski with the elliptic gauge of [HL17],
which has no horizon to pass. This route uses nothing of routes A and B and its gauge is not the wave gauge of
Theorem E; it is the heavier of the two for this problem and is recorded, not recommended.

### 4.5 The first step, and the order

W6 is finished (4.3(1), all seven identities at l = 2 and 4), W7, Hung's Proposition 4.2 in five dimensions, is computed
(4.6), his Proposition 4.1 is deduced on it (4.7; N1STAR-PROOF.md Proposition 10.3), and the rungs are done (4.8;
Propositions 10.4-10.5): every scalar wave equation of 4.3(1), with its potential and its source, has the estimates of
[Hun19] Appendix A in five dimensions, the Morawetz multiplier for the Maxwell potential computed, so the gauge vector
decays at tau^(-2+) with the loss of a fixed number of derivatives once its sources do. The growing source (4.3(3)) and
l = 0 (4.3(4)) are computed (4.9; N1STAR-PROOF.md 10.7-10.8): [Hun19]'s substitutions (4.27)-(4.30) in five dimensions,
every bad weight removed and the residual sources in the norm's weights, and the identities of his section 8; what they
left open was two estimates. The first, the rapid decay of the first rungs, is 4.10 (N1STAR-PROOF.md 10.9): his
Proposition A.5 with k = 1 goes through in five dimensions for l >= 2, and for Sigma at l >= 1 (Proposition 10.6,
deduced), and at l = 0 his Proposition A.6 does not -- the radiation field carries V_inf = 3/4 there, not zero, so the
hierarchy of S_W stops at p < 2 and 10.8's conditional is not discharged by his method. The second, the coupled (X_1,
X_L) estimate of his section 6, is 4.11 (N1STAR-PROOF.md 10.10, Proposition 10.7, deduced): the Morawetz bulk of the
pair is positive without his compact-region substitution, and with it route A is carried through for every mode l >= 2
of the class. The l = 0 sector is 4.12 (N1STAR-PROOF.md 10.11, Proposition 10.8, deduced): the same commutator, its
negative V^(1)_inf = -5/4 absorbed by a Hardy inequality on the leaf for p < 1, with [Sch13]'s Morawetz estimate at l =
0, gives S_W and P-hat the decay 10.8 needs at a weaker rate, and with it route A is carried through for every mode of
the class. Route B's item 2, the five-dimensional constraint damping, is 4.13 for its indicial roots (N1STAR-PROOF.md
10.12, Proposition 10.9, computed): Hintz's damping with the trace weight 2/(D - 2) clears the strip [-100, 19/10], and
[-100, 2] but for the Coulomb root, at a point below the five-dimensional bound of his Lemma 4.4, h < e chosen here;
4.14 (10.13, Proposition 10.10, computed) recomputes the semiclassical inputs of [Hin26a] in five dimensions, and 4.15
(10.14, Proposition 10.11, computed) gives a five-dimensional c of his Proposition 5.1's kind on Tangherlini, its
conditions checked at that e; 4.16 (10.15, Proposition 10.12, computed; the kernel deduced) gives the unmodified gauge
potential operator's zero energy kernel, cokernel functional and pairings in five dimensions, the inputs of [Hin26]
Proposition 6.12; and 4.17 (10.16, Proposition 10.13, computed; the mode stability deduced) gives that operator's mode
stability at sigma != 0 on Tangherlini, in a class, the input of his Proposition 6.9; and 4.18 (10.17, Proposition
10.14, computed; deduced) gives the strong trapping admissibility of box^Upsilon, his Lemma 6.4, the input of his
Proposition 6.5; and 4.19 (10.18, Proposition 10.15, computed; deduced) gives his Lemma 6.1's structure, S-bar of his
(6.11) and the horizon threshold 3/2 of his footnote 71 in five dimensions; and 4.20 (10.19, Proposition 10.16,
computed; deduced) gives the remaining inputs of [Hin26c] Theorems 9.5 and 9.16 -- the threshold at R_in, -1/2 - S-bar,
the trapped set's hypotheses and loss, the dynamics -- and deduces [Hin26] Propositions 6.5 and 6.9 there, on the
reading that [Hin26c] section 9's scalar estimates hold on bundles and his Theorems 9.5 and 9.16 restated for n = 4; and
4.21 (10.20, Proposition 10.17, computed; deduced) carries [Hin26c]'s low-energy theory to n = 4 -- the transition face
model and its Bessel reduction, the weights -- and deduces [Hin26] Proposition 6.12 there: the gauge potential operator
is mode stable on the closed upper half plane; and 4.22 (10.21, Proposition 10.18, computed; deduced) carries [Hin26a]
section 6 to five dimensions -- S-bar^C with three angular copies, the radial sets and (B.13)'s l-window, the weights
alpha_sf = -C_0 - 5/2 and l in [-C_0 - 2, 0) -- and deduces his Theorem 6.2 there from his Theorem 5.2; and 4.23 (10.22,
Proposition 10.19, computed; deduced) computes the inputs of his Theorem 5.2 that 10.13-10.14 had not -- Tangherlini a
3sc-metric with two powers to spare, the time functions of his energy estimates, his Proposition 5.1 (4)-(5) at 10.21's
weights -- and deduces Theorem 5.2 on the reading that his 3b-analysis carries to five dimensions; and 4.24 (10.23,
Proposition 10.20, computed; deduced) computes the five-dimensional inputs of his Theorem B.1, the transition face model
on Minkowski space -- its dilation structure, the beta-range (0, 2 + C_0] at the origin, the thresholds at the cone face
and the sink, section B.4's weights, data and closing integral -- and deduces Theorem B.1 there and [Hin26] Theorem
7.1(4), tf-admissibility for every beta in [-C_0, 2), on the same readings, at Proposition 10.9's point, for C_0 <= 100
and h = 10^-6 if that is below h_0; and 4.25 (10.24, Proposition 10.21, computed; deduced) computes the indicial roots
of the linearized gauge-fixed Einstein operator -- its factorization through box^Upsilon and box^C with the physical
roots -l and l + 2, the tensor type -- and deduces his Lemma 8.4 for every l at Proposition 10.9's point, Lemma 8.5 and,
but for the spectrum of his Lemma 8.2's S-bar, Proposition 8.6 for small gam_Ups; and 4.26 (10.25, Proposition 10.22,
computed; deduced) computes that S-bar -- the gauge potential operator's spectrum, the constraint propagation operator's
and five zeros, min spec S-bar = 0 -- and completes Proposition 8.6 on readings, at that point for small gam_Ups; and
4.27 (10.26, Proposition 10.23, computed; deduced) computes the subprincipal matrix of 2 L at the trapped set -- his
printed 10 x 10 reproduced, the 15 x 15 with ten zeros and the eigenvalues -2 (1 - e_C) gam c_2, -2 gam c_2 (three
times), -4 gam c_2, triangular in a constant basis -- and deduces his Proposition 8.3 on Tangherlini; and 4.28 (10.27,
Proposition 10.24, computed; deduced) computes the Kodama-Ishibashi reduction of D Ric on Tangherlini -- each harmonic
type at l >= 2 to one master equation with a positive potential, l <= 1 pure gauge at sigma != 0 -- and deduces [AHW24]
Theorem 6.1(1) there and his Proposition 8.8; and 4.29 (10.28, Proposition 10.25, computed; deduced) computes
Tangherlini's orders against Minkowski, the asymptotic symmetries' defects and the linearized metrics' gauge sources,
and deduces his Proposition 6.15 and Proposition 8.9 there, one order faster and without logarithms, on his Lemma 6.13;
and 4.30 (10.29, Proposition 10.26, computed; deduced) deduces his Lemma 6.13 there and computes the leading terms of
his Proposition 6.18 (1)-(3), the time translation's state without his logarithm and his (6.40) as (1/4)(1 +- 2
gam_U/5). Next: the rest of item 2 -- [Hin26] Proposition 6.18 (4)-(7), sections 7.2, 8.4 from Proposition 8.11 on, and
8.5 -- in five dimensions.

### 4.6 W7: Hung's Proposition 4.2 in five dimensions (computed, D47)

Hung's Proposition 4.2 ([Hun19] p. 18; Appendix C, pp. 75-79) is not the Lichnerowicz system alone: each row is a
combination of the Lichnerowicz components and of the harmonic gauge condition Gamma[h] = 0, the admixture chosen so
that the first-order terms cancel except along nabla_L in rows 6 and 7. The control `hung4.py` recomputes his seven
rows from the Schwarzschild metric with the instrument W7 runs and reproduces the printed A, B and U: rows 1-5 as
printed; row 7 as printed once the "(ME3)" of its combination is read as (HG3), the angular gauge component, which
is what balances its first-order terms; row 6 as printed once its combination is read as f (ME3) + (M/r^3)(ME6) +
(4M(r - 2M)/r^3)(HG2) for the printed (ME2), M/r^2 and 4M(r - 2M)/r^2 -- the component with one t index and the
powers of r the dimensions require; the printed row-6 combination leaves second-order terms. Two misprints, no
finding about the theorem. On Tangherlini, in the class (wavegauge5.py W7):
- the components H1 = (h_tt + f^2 h_rr)/2 + ((1 - f)/2) trs h, H2 = trs h/sqrt3, H3 = (h_tt/f - f h_rr)/2,
  H6 = f h_tr + ((1 - f)/2) trs h, H4 = f k h_rth/(r S'), H7 = k h_tth/(r S'), hhat_ij = 2 r^2 H5 S_ij, with
  (1 - f)/2 = mu/(2 r^2) where Hung has M/r = (1 - f)/2: the same coefficient in both dimensions;
- the admixtures 2 f f' Gamma_r in rows 1 and 6 and k f' Gamma_th/r in rows 4 and 7 (Hung's 4M(r - 2M)/r^3 = 2 f f'
  and 2M/r^2 = f', in his normalisation of h_rA);
- box_l H = A H + U H with U = (2f'/f) nabla_L (H6 - H1) in row 6 and (f'/f) nabla_L (H7 - H4) in row 7, nothing
  else, A rational in r, mu and k;
- r^2 A_main at k^2 = l(l+2) has the eigenvalues (l+a)(l+a+2), a = -2, -1, 0, 0, 0, 1, 2 (Hung's Lemma 4.3:
  (l+a)(l+a+1)): semi-positive for l >= 2, one zero at l = 2, comparable to the angular term for l >= 4;
  A - A_main/r^2 = O(mu/r^4) where Hung's A_sub is O(M/r^3); at l = 0 (H1, H2, H3, H6) the eigenvalues are 0, 0, 3, 8;
- in the regular variables H6' = (H6 - H1)/f^2 = -h(L', L')/2 and H7' = (H7 - H4)/f every coefficient is regular at
  the horizon, rows 1-5 carry no first-order term, and rows 6', 7' carry 2f' nabla_L' H6' and f' nabla_L' H7',
  f' = 2 mu/r^3 > 0, and no nabla_L: Hung's 4M/r^2 and 2M/r^2 (p. 23), so the red-shift step of his Proposition 4.1
  applies as written.
What the gauge condition does. The Lichnerowicz operator alone carries, in the null frame, -f' times the boost weight
as the nabla_L' coefficient of each component: -2f' on h(L, L), -f' on h(L, d_th), 0 on h(L, L') and the angular
part, +f' on h(L', d_th), +2f' on h(L', L') -- the Teukolsky-type structure, in which a red-shift estimate for the
positive weights would need commutation with L'; the admixture of Gamma[h] = 0 removes the negative ones. In the
orthonormal frame, without the admixture, the system is box v = T d_t v + M v with no d_r term, M symmetric with the
same leading spectrum, T the chain coupling (h_00, h_01), (h_01, h_11) with sqrt2 f'/f and (h_0th, h_1th) with f'/f.
What W7 does not do: it is the structure, not the estimate. Proposition 4.1 (Hung's (4.1), r^p and red-shift for h
with the compact region as the error) is to be proved on it with [Sch13]'s weights; the Morawetz step for the Maxwell
rung, the growing source and l = 0 are 4.3(3), (4), (6)(a), (b), (d). Labels: computed (wavegauge5.py W7, hung4.py);
READ ([Hun19] pp. 18-25 and 70-79, alphaXiv, 2026-10-21); OPEN (the estimate).

### 4.7 Hung's Proposition 4.1 in five dimensions (deduced, D48)

Hung's Proposition 4.1 ([Hun19] p. 18, (4.1); its proof pp. 20-25: Lemma 4.4 with the current (4.5), the J_{H,delta}
current (4.6), the red-shift (4.7)-(4.8), the T-current (4.9)) is deduced in five dimensions as N1STAR-PROOF.md
Proposition 10.3, its proof written in the same three steps on the structure of 4.6, from the identities wavegauge5.py W8
computes (exact; the three divergence identities formally, on two components with the matrices symbolic):
- the radiation field Psi = s^(3/2) Hhat has the potential V = Ahat + V0, V0 = (3/4 + 9 mu/(4 r^2))/r^2 ([Sch13]
  (5.11)-(5.12) at n = 4), and V_inf = lim r^2 V, symmetric in the rescaling diag(sqrt2, 1, sqrt2, sqrt2, 2 n_S, sqrt2,
  sqrt2), has the eigenvalues (l+a+1/2)(l+a+3/2), a = -2, -1, 0, 0, 0, 1, 2: at least 3/4 at every l >= 2 and at least
  (3/32) l(l+2). Hung's zero eigenvalue at l = 2 is lifted by the 3/4 of the five-dimensional radiation weight, so the
  far-region estimate needs no Hardy inequality where four dimensions needs his Corollary 3.3;
- the p-current's divergence (W8c) is his (4.5) with the powers of s lowered by one, its flux at I^+ is s^(p-5) Psi .
  V_inf . Psi >= 0, and the first-order term Uhat is bounded by 9 mu r^-3 f^-1 |nabla_L Psi| + 13 mu r^-4 |Psi|,
  absorbed for R_H ~ delta^-1/2 r_h as his is;
- the red-shift identity at r = r_h (W8d) is his (2.13) with (1/(2M), 2/M) read as (2/r_h, 6/r_h) and two terms new in
  five dimensions, (1/r_h)|nabla-slash Q|^2 and (2c/mu^(3/2))|Q|^2, absorbed for sigma > 18/r_h and then sigma large
    (the (2c/mu) Q . Q_R and c sigma/mu |Q|^2 terms are the four-dimensional current's own, hung4.py C3, which his print
      carries as c sigma/(8M^2) without the Q . Q_R term); the first-order term along nabla_L' enters as 2 Q_R . diag(0,
        0, 0, 0, 0, 2f', f') Q_R >= 0, the
  sign his argument needs (4.6);
- the sub-leading and horizon matrices have entries of degree at most one in k (W8g), so one angular derivative bounds
  them uniformly in l, which is what his (4.3) states for A_sub and B_sub;
- l = 0 (W8h): A0 - A0_main/r^2 = O(mu/r^4) and V_inf has the eigenvalues 3/4, 3/4, 15/4, 35/4, so the proposition
  holds for h_{l=0} too, as his Remark 4.5 -- without bounding it: K* grows linearly in t and the right side with it.
What it is not: a decay statement. The right side carries h on [r_rs,H, R_null + r_h]; in [Hun19] the compact region is
bounded through the Zerilli quantity and the gauge vector W (sections 4.2-7), here through Proposition 10.1's master
quantities and the gauge vector system of 4.3(1)-(2), whose rungs are the next item. Labels: computed (wavegauge5.py W8);
deduced (Proposition 10.3, constants not tracked); READ ([Hun19] pp. 4-25 and 70-72, [Sch13] (2.17)-(2.20), Proposition
3.1 and (5.8)-(5.17); alphaXiv, 2026-10-21). Read by the sixteenth verifier (D48): no blocking or major finding; one
  intermediate inequality of Step 1 repaired with the five-dimensional powers, and this section's count of the new terms
    corrected from three to two.

### 4.8 The rungs: the Morawetz current for the Maxwell potential, and the decay of each rung (deduced, D49)

4.3(6)(a) asked for the one thing in [HKW18]'s chain that depends on the potential, the Morawetz multiplier, for the
Maxwell potential -4 mu/r^4 of the rung r P; rungs5.py computes it and the rest of what the chain uses, and
N1STAR-PROOF.md 10.6 runs the chain with the source carried (Propositions 10.4-10.5):
- the Morawetz identity [HKW18] (123) at n = 3 holds for a scalar with potential and source, exactly (M1);
- with [HKW18]'s n = 3 choice read in mu = 2M, F = (1 - 2 mu/r^2)(1 - mu/(2 r^2) + mu^2/(5 r^4)) and beta = 1/(2 sqrt
  mu), and half the angular term borrowed at k^2 = 8 (the other half stays in the bulk, where the current needs it), the
  bulk coefficient W is -(y^3/40) Q(y) mu^(-3/2) with y = sqrt(mu)/r and Q a polynomial of degree ten without a root in
  [0, 1], Q(0) = -140 -- so W > 0 on the whole exterior, W >= r^-3/5 (Maxwell) and r^-3/7 (free); W0 alone is negative at
  the horizon (Maxwell) and at infinity (both), so some borrowing is necessary, the thresholds 27/112 and 1/16; F' > 0 on
  the closed exterior, the angular coefficient a square at the photon sphere (M2). Their choice, made for their master
  potentials, serves both rung potentials unchanged; beta = 0 or beta >= 1/sqrt mu does not;
- Hung's (A.3) holds with room, k^2/r^2 - 4 mu/r^4 >= k^2/(2 r^2) on the exterior, so the T-energy comparison is
  pointwise and no Hardy inequality enters (M3); the radiation variable's potential has V_inf = k^2 + 3/4 and a remainder
  -7 mu/(4 r^4) or 9 mu/(4 r^4), so the r^p step is Proposition 10.3's Step 1 for one component (M4); the g-current that
  supplies |d_t u|^2 is (M5);
- Proposition 10.4: the energy inequality with the degenerate Morawetz bulk and no compact-region term, F + E^p +
  int (B + E^{p-1}) <~ F + E^p + E^p_source[G], for p in [delta, 2 - delta], the source norm the five-dimensional one
  this proof produces (mu^1/2 int s^(p+1) |G|^2 in the bulk, |G|^2 on the two slices, |nabla_T G|^2 on a compact region
  in r, from an integration by parts in T at the photon sphere);
- Proposition 10.5: the decay (1 + tau/sqrt mu)^(-2 + p + delta + delta-bar) of F + E^p by [HKW18] Theorem 18's dyadic
  argument with the source, the commuted quantities T u and k u in the data, the photon-sphere degeneracy lifted by the
  one-dimensional Poincare inequality in r -- [Hun19] (A.10) with one more delta in the exponent, the cost of the
  intermediate times, cosmetic for L1.
Two readings of [HKW18] recorded: Proposition 15 states a_0 > 0 for the 1/r^2 coefficient of the potential, but its proof
uses only a_0 bar = a_0 + (n^2 - 2n)/4 > 0, which the rungs' a_0 = 0 satisfies at n = 3 (a_0 bar = 3/4, the 3/4 of
Proposition 10.3's V_inf); and their beta = 1/2 and f are written in units M = 1 (beta has the dimension of 1/length),
read here as 1/(2 sqrt mu). What the rungs give: the estimate for each rung's equation with a source in the norm (10.16).
What they do not: the decay of the gauge vector, because the sources the rungs carry -- 2 d_t S in r P's, (2 f r/k) d_r S
in r X_L's -- are not in that norm's weights (S's rung supplies s^(p'-4) |nabla_L Psi_S|^2 with p' <= 2 - delta where r
P's source needs p' = p + 2); that is the growing source (4.3(3)), the next step, and l = 0 (4.3(4)) stands beside it.
Labels: computed (rungs5.py M1-M5); deduced (Propositions 10.4-10.5, constants not tracked); READ ([HKW18] section 7 pp.
28-48, 9.3.2 pp. 54-57, 10.4.2-10.5 pp. 66-67; [Hun19] 2.2 (g = r_* on [5M/2, R_null]), 2.4 (the source norm,
(2.23)-(2.24)), Proposition 5.2, Lemma 5.5; alphaXiv, 2026-10-21). The seventeenth verifier (2026-10-21): three major
findings, all repaired -- the angular term spent twice at l = 2 (now half of it borrowed, the thresholds computed), the
claim that X decays (withdrawn: the sources are not in the norm), I^(0) short of the p-weighted data the proof uses
(carried at every order of T and k, where [Hun19]'s (2.23) carries them at K^{<= 1}) -- eight minor ones repaired and two
notes seated (r_1 >= 5 r_h/4; the leaves t = const on [5 r_h/4, R_null], settled from [Hun19] 2.2); sound otherwise, by
an independent sympy derivation of M1-M5 and the arithmetic of 10.6 by hand.

## References (READ 2026-10-20 unless marked)

- [TTS09] K. Tanabe, N. Tanahashi, T. Shiromizu, On asymptotic structure at null infinity in five dimensions,
  arXiv:0909.0426v2.
- [HL21] L. He, H. Lindblad, Masses at null infinity for Einstein's equations in harmonic coordinates,
  arXiv:2107.01487v2.
- [KK25] I. Kadar, L. Kehrberger, Scattering, polyhomogeneity and asymptotics for quasilinear wave equations from past
  to future null infinity, arXiv:2501.09814v2.
- [CCRT07] S. I. Chernyshenko, P. Constantin, J. C. Robinson, E. S. Titi, A posteriori regularity of the
  three-dimensional Navier–Stokes equations from numerical computations, arXiv:math/0607181v2.
- [MP11] C. Morosi, L. Pizzocchero, On approximate solutions of the incompressible Euler and Navier–Stokes equations,
  arXiv:1104.3832v1.
- [RT12] M. Reiterer, E. Trubowitz, Choptuik's critical spacetime exists, arXiv:1203.3766v1.
- [KS17] S. Klainerman, J. Szeftel, Global nonlinear stability of Schwarzschild spacetime under polarized
  perturbations, arXiv:1711.07597v2.
- [Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2.
- [DHRT21] M. Dafermos, G. Holzegel, I. Rodnianski, M. Taylor, arXiv:2104.08222 (abstract only).
- [Hun19] P.-K. Hung, The linear stability of the Schwarzschild spacetime in the harmonic gauge: even part,
  arXiv:1909.06733v1.
- [HKW18] P.-K. Hung, J. Keller, M.-T. Wang, Linear stability of higher dimensional Schwarzschild spacetimes: decay
  of master quantities, arXiv:1809.05144v1 (section 7 and 9.3.2 READ 2026-10-21).
- [Wu26] S. Wu, Picard iteration for the characteristic initial value problem in Einstein equations,
  arXiv:2609.08421v1.
- [Sch13] V. Schlue, Decay of linear waves on higher dimensional Schwarzschild black holes, Anal. PDE 6 (2013),
  arXiv:1012.5963v1.
- [KI03b] H. Kodama, A. Ishibashi, Master equations for perturbations of generalised static black holes with
  charge in higher dimensions, arXiv:hep-th/0308128v4.
- [Hin26] P. Hintz, Nonlinear stability of subextremal Kerr black holes, arXiv:2606.28253v2; [Hin26a] Constraint
  damping on subextremal Kerr spacetimes, arXiv:2606.27658v1; [Hin26c] (Non-)linear waves on asymptotically flat
  spacetimes. II, arXiv:2606.28008v1; [Hin23c] Linear waves on asymptotically flat spacetimes. I,
  arXiv:2302.14647 (cited through [Hin26c], not read).
- [KS17] S. Klainerman, J. Szeftel, Global nonlinear stability of Schwarzschild spacetime under polarized
  perturbations, arXiv:1711.07597v2 (abstract).
- [Hun15] C. Huneau, Stability of Minkowski space-time with a translation space-like Killing field,
  arXiv:1511.07002 (abstract).
- [HL17] C. Huneau, J. Luk, Einstein equations under polarized U(1) symmetry in an elliptic gauge,
  arXiv:1706.09499 (abstract).
- [IK03], [HKW18], [Hol08], [CLY03b], [AB26]: as in RESPONSE-HL-5D.md ([Sch13] carried the label [Sch10] here and in
  N1STAR-PROOF.md section 10.1 until D47; one paper, one label now).

### 4.9 The growing source and the l = 0 sector: Hung's sections 4.2 and 8 in five dimensions (computed, deduced; D50)

4.3(3) asked for the five-dimensional form of [Hun19]'s modification (4.35)-(4.36), read off the explicit sources; 4.3(4)
for the l = 0 argument. growing5.py and lzero5.py compute both, and N1STAR-PROOF.md 10.7-10.8 state what follows.
- The master field of [KI03] at n = 3 is transcribed ((3.5)-(3.7), (3.13)-(3.14)) and checked against the Einstein
  equations E_a = 0 modulo the master equation, at three (mu, k) and three radii, and against the Zerilli potential at n
  = 2 (G1); J = -Gamma[h_RW] is computed in h_RW's components (G2); the direct system for (X_t, X_1 = f X_r, X_L) with
  d_t X_t eliminated through div X is Hung's (4.21)-(4.23) in five dimensions, the (X_1, X_L) pair coupled at zeroth
  order (G3).
- In Hung's canonical form (d_r^2 eliminated) and the scalar-wave normalisation phi = r^(-3/2) Phi_KI, with box_l phi =
  V_phi phi, V_phi = -12 mu (k^2 + 3)((k^2 - 3) r^2 + 2 mu)/(r^6 H^2) = O(mu/r^4), and Sigma := tr h the homogeneous
  first rung (S = (Sigma - 4F)/2), the rung sources are exactly: G_P = 4 r f d_t d_r phi + c_2 d_t phi + d_t Sigma, J_t =
  -2 r f d_t d_r phi + c_t d_t phi, f J_r = -2 r d_t^2 phi + O(mu/r^2) d_r phi - r f V_phi phi, J_L = 0, tr h_RW = 2 r f
  d_r phi + c_F phi -- his (4.25), (4.21), (4.22), (4.23): the same bad terms, O(r) d_t d_r, O(1) d_t, d_t Sigma and O(r)
  d_t^2 on phi, and nothing else (G4, at four (k^2, mu) points; the coefficient functions read at k^2 = 8, 24, 48, fitted
  in k and checked at k^2 = 80: c_F = (12 mu + (2/3)(k^2 - 3)(k^2 + 6) r^2)/(r^2 H), c_2 = 2 c_F, c_t = -2 (3m r^4 - (4m
  - 6) mu r^2 - 12 mu^2)/(r^4 H), m = k^2 - 3).
- The substitutions, his (4.27)-(4.30): r P-bar = r P - r^2 d_t phi + (u + r)((2 k^2/3) phi + Sigma/2); X_t-bar = X_t +
  (r^2/2) d_t phi - (u + r) phi; X_1-bar = X_1 + (r^2 f/2) d_r phi + (m r^4 + 6 mu^2)/(r^3 H) phi; X_L-bar = X_L + (k
  r/2) phi. Each coefficient is forced: the r^2 d_t phi terms by the d_t d_r coefficients, (r^2 f/2) d_r phi by the ODE
  the d_t^2 coefficient imposes, (k r/2) phi by the X_1-X_L coupling, the (u + r) coefficients as the limits at infinity
  of the exact functions that would remove d_t phi and d_t Sigma outright. The barred rungs' sources carry no
  second-order term, every coefficient O(r^-2) or better and the (u + r)-weighted ones O(r^-4), with s^-2 nabla_L Sigma
  where his (4.31) has s^-1 nabla_L S (G5, exact at the four (k^2, mu) points; r P-bar's Sigma terms exact and its phi
  terms to leading order, X_t-bar's d_r phi, phi and (u + r) phi terms exact, X_1-bar's and X_L-bar's single phi terms to
  leading order, as 10.7 prints them). Interpolated by eta_b as his (4.35)-(4.38).
- l = 0: the identities of his section 8 in five dimensions -- P = r (dW)_tr - 2 W0 with box_s P = d_t S_W, box_s S_W =
  0; the (W0, W3) form with f' L' W3 (the red-shift sign); c_1(oo) = mu (W0 + P/2 - (sqrt mu/4) S_W)|_{H^+} (deduced from
  (8.12)); the radial ODEs with the solutions 1/r^2 and 1 + (mu/r^2) log(r^2/mu - 1), 1/(r^3 f) and W*'s own W3; the
  substitution P + (u + r) S_W/2 whose source is -(mu/(r^2 f)) nabla_L S_W - (mu/(2 r^3)) S_W (Z1-Z5). His Theorem 8.1's
  argument goes through on them (10.8, deduced).
- What remained (10.7-10.8, said there): (a) the rapid decay of the first rungs, Sigma and phi at l >= 2 and S_W at l = 0
  -- the extension of the r^p hierarchy past p = 2 by one commutation with r^2 nabla_L, his Proposition A.5 with k = 1
  and A.6, in five dimensions, where V_inf = k^2 + 3/4 is never zero and the potentials' tails are r^-4 -- now 4.10: done
  for l >= 2, obstructed at l = 0; (b) the coupled estimate for (X_1-hat, X_L-hat), his section 6 for the matrix of
  (10.29). With (b) and an l = 0 rate, his Theorem 2.5 and Theorems 1.3-1.4 follow in the class. Labels: computed
  (growing5.py G1-G5, lzero5.py Z1-Z5, exact at the sample points); deduced (the three-region bounds, the l = 0
  argument); READ ([KI03] sections 2-3 and 6, Appendix A; [Hun19] 4.2, 5, (6.1)-(6.11), 8, Appendices A-B; alphaXiv,
  2026-10-21); nothing proved; (a) is 4.10 (open at l = 0) and (b) is 4.11.

### 4.10 The first rungs' rapid decay: Hung's A.5 in five dimensions, and the l = 0 obstruction (computed, deduced; D51)

4.9's item (a). hierarchy5.py computes the commuted equation, the current and his conditions (A.3), (A.5), (A.7)-(A.9) in
five dimensions; N1STAR-PROOF.md 10.9 states Proposition 10.6 and the obstruction.
- The commuted field Psi_1 := f^-1 r^2 nabla_L Psi of the radiation field Psi = r^(3/2) u satisfies L Lbar Psi_1 =
  -(2/r)(1 - 2 mu/r^2) nabla_L Psi_1 - f Vcal_1 Psi_1 + f (9 mu/(2 r^3) - r^2 V' - 2 r V) Psi with Vcal_1 = Vcal -
  2/r^2 + 12 mu/r^4, V^(1)_inf = k^2 - 5/4 = (l - 1/2)(l + 5/2), exactly for a symbolic potential (H1). In four
  dimensions the same computation gives his V^(1) exactly -- his 14 M/r^3 is the 12 M/r^3 here with the radiation
  field's own 2M/r^3, which his V^(j) counts from V -- and a first-order term his remark does not print, which enters
  the current with a good sign (READ).
- The p-current identity for Psi_1 is (10.7) with the first-order term adding 2(1 - 2 mu/r^2) to the |nabla_L Psi_1|^2
  bulk, positive for r^2 > (10 + p) mu/(4 + p) (H2). The Psi_1^2 bulk is ((2 - p)/2)(k^2 - 5/4) + (57/8)(4 - p) mu/r^2
  for Sigma, positive on the exterior for p in [0, 2] and l >= 1 -- (A.7) with no R_null -- and for phi it has the room
  (1/4)(2 - p)(k^2 - 5/4) for r >= 8.14 r_h at k^2 = 8 and everywhere at k^2 = 24, 48, 80; the base bulk (A.5) likewise
  with R_0 = 10.56, 4.61, 3.04, 2.29 r_h; (A.8) holds for l >= 1; (A.9) with r^4 |V_phi|/mu <= 12 (k^2 + 3)/(k^2 - 3),
  attained at infinity, and V_phi -> -12 mu/r^4 as k -> oo; (A.3) holds with the margin 4/11 at k^2 = 8 and fails at k^2
  = 3 (H3).
- Proposition 10.6 (deduced): for Sigma and phi at l >= 2, F + E^{p,(0)}_L + the bulks decay as (1 + tau/sqrt mu)^(-4+p+3
  delta) against I^(1)[u], by his argument on (10.34)-(10.35): the base hierarchy, the commuted one, the Hardy step
  E^{2,(0)}_L <= 4 (100/99)^2 E^{0,(1)}_L (his exponents, the radiation field carrying s^(3/2)), and the dyadic argument
  twice. With it 10.7's three-region bound closes as his Lemma 5.5: I_source[G] of each hatted rung decays at (1 +
  tau/sqrt mu)^(-2+p+3 delta).
- l = 0 (H4): V_inf = 3/4 and V^(1)_inf = -5/4, so (A.8) fails and the base bulk (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 is
  negative for p > 2 once r^2 > 3(4 - p) mu/(p - 2): the hierarchy of S_W stops at p < 2, where in four dimensions (V_inf
  = 0) it reaches p < 3 and, with the Newman-Penrose constant, p < 4 (his Proposition A.6(1), the input of his
  Proposition 8.2). His route gives S_W the rate (1 + tau/sqrt mu)^(-2+p+delta) of Propositions 10.4-10.5 and nothing
  more; 10.8's conditional is not discharged by it. Open: a different commutator at l = 0 in odd dimension (the l = 0
  tail is t^-3 by [CYDL03], so the obstruction is the method's), or his Appendix B's O_j bounds re-run at the weaker
  rate.
- Labels: computed (hierarchy5.py H1-H4, exact; the radii and constants at k^2 = 8, 24, 48, 80); deduced (Proposition
  10.6); READ ([Hun19] Appendix A in full, Lemma 5.3, Propositions 5.2, 5.4, 8.2, Lemma 8.3, (2.4), (2.19)-(2.23);
  alphaXiv, 2026-10-21); nothing proved; l = 0 open; 4.9's (b) is 4.11.

### 4.11 The coupled estimate: Hung's section 6 in five dimensions; route A through for l >= 2 (computed, deduced; D52)

4.9's item (b). coupled5.py computes the identities, the pair's matrix and three of the four currents in five
dimensions, the red-shift current being deduced;
N1STAR-PROOF.md 10.10 states Proposition 10.7.
- The identities (K1): d_r X_1 + (3/r) X_1 + (k/r) X_L = S + f^-1 d_t X_t, f d_r X_L + (f/r) X_L + (k/r) X_1 = (k f/r)
  Q_r, d_t X_1 = f (P + d_r X_t) -- his (6.8)-(6.10) -- and d_t X_L = (k/r)(Q_t - X_t), a fourth: every first derivative
  of the pair is zeroth order in it modulo the rungs S, P, X_t and the source J (W6 re-run).
- The pair's matrix (K2): at infinity its eigenvalues are (l + 1)(l + 3) and (l - 1)(l + 1), positive definite for l >=
  2, where Hung's are (l + 1)(l + 2) and l(l - 1), zero at l = 1; A_12 vanishes at the photon sphere, so no diagonal
  symmetriser exists, as in four dimensions.
- The T-current (K3): with the weights (10, 1) inside (his are (10, 2), (6.17)-(6.18)) and the inner and outer symmetric
  parts, N_in, N_ex >= (k^2/4) r^-2 I for every k^2 >= 8, exactly; the inner error involves d_t X_1 only, which is the
  identity's F_3, and the outer one is (4 k mu/r^4) d_t X_L X_1, absorbed by the r^p bulk.
- The Morawetz current (K4-K5): the identity for a pair with arbitrary V, and with M = sym(V), the record's F and beta =
  1/(2 sqrt mu), the antisymmetric cross term completed into the radial square, a tenth of the angular term kept, the
  zeroth-order bulk satisfies W_rest >= r^-3/40 for every real k^2 >= 8 on the whole exterior, exactly (Sturm); 0.0352
  r^-3 at l = 2, at 1.261 r_h. Hung needs (6.8)-(6.9) for positivity on [2M, bM] because his pair is semi-definite at l =
  1; here the identities are used only to remove the photon-sphere degeneracy of the derivatives, as he also does --
  uniformly in l, the completion cost being at most 35/13 of the kept tenth (the twentieth verifier's repair, D52).
- The r^p current (K6): V_inf = [[k^2 + 15/4, 2k], [2k, k^2 - 1/4]], eigenvalues (l + 3/2)(l + 5/2) and (l - 1/2)(l +
  1/2), remainders O(mu/r^4).
- Proposition 10.7 (deduced): the pair decays at (1 + tau/sqrt mu)^(-2+p+3 delta) against Decay[X], by his argument; the
  red-shift step by [HKW18] Lemma 11 for a bounded matrix potential, without a computation. With 4.9, 4.10 and the rungs
  of 10.6, every component of the gauge vector and h = h_RW + pi_X decay in harmonic gauge at every mode l >= 2 of the
  class, by his section 7 on Proposition 10.3: [Hun19]'s Theorem 2.4(1) (h at l >= 2; the l >= 2 part of his Theorem 1.2)
  in five dimensions, deduced.
- Labels: computed (coupled5.py K1-K6, exact; K1 at l = 2, K3 and K5 for every real k^2 >= 8); deduced (Proposition 10.7
  and its consequences); READ ([Hun19] section 6 in full, (6.1)-(6.37); alphaXiv, 2026-10-21); nothing proved; l = 0 open
  here, and 4.12's.

### 4.12 The l = 0 sector by another route: the commuted hierarchy with a Hardy absorption (computed, deduced; D53)

4.10's obstruction at l = 0, taken by another route. lzerorate5.py computes what it needs; N1STAR-PROOF.md 10.11 states
Proposition 10.8.
- The currents at l = 0 (Y1): Vcal_1 = -5/(4 r^2) + 57 mu/(4 r^4) and C = 9 mu f/(2 r^3); the base current's |nabla_L
  Psi|^2 coefficient p f/2 - mu/r^2; on the outgoing leaf the commuted bulk r^(p-1) c w'^2 + r^(p-3) B_1 w^2 - (9 mu/2)
  r^(p-3) Psi w', c = p f/2 + 2 - 5 mu/r^2, B_1 = -(5/8)(2 - p) + (57/8)(4 - p) mu/r^2.
- The Hardy step (Y2) and the window (Y3): with A and B the leaf's zeroth- and first-order integrals and A <= 4 B/(2 -
  p)^2, the bulk is at least (Q/(2 (2 - p))) B + (Q (2 - p)/8) A, exactly, Q = (2 + p/2 - (5 + p/2) mu/R_null^2)(2 - p) -
  5/2; Q(p, 0) = (1 - p)(3 + p)/2, and Q > 0 on [delta, 1 - delta] at R_null = 10 r_h for delta = 1/10 and at R_null = 3
  r_h/delta^(1/2) for every delta in (0, 1/10]. At leading order the window needs V^(1)_inf > -2: open at five
  dimensions' -5/4, empty at four dimensions' -2.
- The base hierarchy (Y4): B_0 >= (3/8)(2 - p) at l = 0, and the T-energy density is at most 12 times the p = 1 bulk: the
  radiation field's (3/4)/r^2 replaces the angular term. The base Morawetz estimate at l = 0 is READ: [Sch13] Proposition
  4.1, which holds for every spherical harmonic number.
- The cut-off source (Y5): the terms of G_P carrying u + r are S_W and d_r S_W only, on [b r_h, 2 b r_h] (his Lemma 8.3).
- Proposition 10.8 (deduced): S_W at (1 + tau/sqrt mu)^(-3+p+3 delta), P-hat at (1 + tau/sqrt mu)^(-1+4 delta), and W' ->
  c_1(oo) W* at the second rate, so h_0 -> c K* + c_1(oo) pi_{W*}: Proposition 10.2(iv)'s conditional discharged, his
  Theorems 1.3-1.4 and 8.7 in five dimensions at a rate one power below his, with no Newman-Penrose condition on the
  data. With 4.11, route A is carried through for every mode of the class.
- Labels: computed (lzerorate5.py Y1-Y5, exact); deduced (Proposition 10.8); READ ([Sch13] Theorem 1, Propositions 4.1
  and 4.21-4.22, Corollary 4.3, (4.76)-(4.92), (5.8)-(5.22); [Hun19] section 8, Proposition A.6 and Appendix B; alphaXiv,
  2026-10-21); nothing proved. Next: route B's item 2.

### 4.13 Route B's constraint damping in five dimensions: the indicial roots at zero energy (computed; D54)

ROUTES 4.4 item 2's new object. damping5.py computes it; N1STAR-PROOF.md 10.12 states Proposition 10.9.
- The families (U1): box^C = 2 delta_g G_g (delta*_g + C) on 4+1 Minkowski, the model at infinity, on stationary 1-forms
  of scalar and vector type, gives 3 x 3, 2 x 2 and 1 x 1 indicial matrices affine in kappa = l (l + 2); the
  four-dimensional control reproduces [Hin26a] (4.19), p_v (the display of his section A.1), p_s0 and (A.13).
- The weight (U2): G (g f) = (1 - D/2) g f, so Hintz's form 2 c (x)_s omega - e g <c, omega> after G needs the trace
  weight m = 2/(D - 2): 1 in four dimensions, 2/3 in five. His weight transcribed literally fails in five dimensions
  (U5): a root in (0, 1) at l = 0.
- The roots (U3): lam = 2, the Coulomb rate r^-(n-2), is a root at l = 0 and 1 for every (v, e, h), as lam = 1 is in
  four dimensions; at h = 0 the scalar sextic is 8 v (lam - 2) Q_5; the very negative roots have his h = 0 limit.
- Proposition 10.9 (U4, computed, exact): at (v, e, h) = (1/2, 1/102400, 10^-6), below Lemma 4.4's five-dimensional
  bound (4.14) with h < e chosen here, no indicial root of the Minkowski model at any l has real part in [-100, 19/10],
  and in [-100, 2] only lam = 2 at l = 0 and 1, simple; the roots accumulate only at +-infinity. That (1.43) then holds
  on Tangherlini with C_0 = 100 is deduced: the roots see only the model at infinity. Four-dimensional control: his
  Theorem 4.9, the same at 9/10 and 1. The first version used (1/2, 1/100, 1/1000), above Lemma 4.4's bound (the
  twenty-second verifier, D54).
- The configuration (U6, numerical): over e, h in {10^-2, 10^-3, 10^-4} the upper roots other than lam = 2 at l = 1 stay
  above 1.93, and above 2 exactly where h <= e; the lower ones sit near -1/h, so C_0 = 100 asks h below 1/100. The grid
  does not contain the point of U4.
- OPEN: whether the five-dimensional gauge-fixed operator's indicial gap begins at 0 (it does at the point: 4.25), on
  which [Hin26] p. 29's reason for the strip [-C_0, 1) rests (both strips are clear at the point); [Hin26] Theorem 7.1
  (1), (2) and (4) for box^C on Tangherlini; the modification E^Upsilon of [Hin26] Proposition 6.12. Labels: computed
  (damping5.py U1-U6; U6 numerical); deduced (the transfer to Tangherlini); READ ([Hin26a] and [Hin26], alphaXiv,
  2026-10-21, pages as in 10.12); nothing proved.

### 4.14 The semiclassical inputs of the constraint damping in five dimensions (computed; D55)

[Hin26a]'s Theorem 6.2 rests on semiclassical estimates whose inputs are computations on Minkowski space. semiclass5.py
recomputes them on 4+1 Minkowski; N1STAR-PROOF.md 10.13 states Proposition 10.10.
- The fibrewise theory (W1): at the weight 2/(D - 2) the operator has his form, B makes l(zeta) self-adjoint and is
  positive definite, and the characteristic polynomial of l(zeta)/2 is his (3.8) with one more copy of G(c) zeta_0: his
  Lemmas 3.3-3.8 hold verbatim. At the weight 1 the effective e is (3e - 1)/2 < 0 and B is indefinite.
- The subprincipal symbol (W2), from its definition: his (4.6), (4.7), Lemma 4.2 and Lemma 4.4 reproduced in four
  dimensions, but for a misprint in Lemma 4.4's a_01 (x e^(1/2) for x/e^(1/2)), which his own determinant refutes.
- The weight thresholds (W3): b_K > b_sf - 1 at dK+ and b_sf < 1 at R_v, his -1/2 and 1/2 shifted by 1/2; his (5.14)
  would become a_sf < 0, a_K > a_sf (deduced: b_sf = a_sf + 1, his p. 39).
- The interior saddle (W4): the e = 0 limit is his, positive on |x| <= 6/5; the admissible e is about 0.000069 v^2
  (numerical), against about 0.000154 v^2 in four dimensions (his ~ 0.000152); exact positivity at e = 1/102400, v =
  1/2. Lemma 4.3 is dimension-free (W5).
- The certificate's point (W6): damping5.py's (1/2, 1/102400, 10^-6) is admissible for Lemma 4.4, h < e; the first
  version's e = 1/100 is not.
- OPEN: the 3b-estimates of his section 5 (his Theorem 5.2, with h_0(e), which his proof does not make explicit);
  section 6's own five-dimensional steps -- the weight interval of (6.1) with the density r^3, the exponent of (6.4),
  the data weights of (5.16) -- of which only S^C, his (4.17), is a Minkowski input (it carries, by the twenty-third
  verifier); and his Theorem B.1, in five dimensions. The c is 4.15. Labels: computed (semiclass5.py W1-W6, exact; W4's
  e_0 numerical); READ ([Hin26a] pp. 9-10, 25-33, 38-41, 43, 53, 66-68; [Hin26] pp. 17, 29, 134-137; alphaXiv,
  2026-10-21); nothing proved.

### 4.15 A constraint damping 1-form on five-dimensional Tangherlini (computed; D56)

ROUTES 4.4 item 2's c. cform5.py computes it; N1STAR-PROOF.md 10.14 states Proposition 10.11.
- The 1-form: in Kerr-Schild time, (2 r_0)^-1 (dt + (v/2) dr) inside r_0/2, his (5.1) on [r_0/2, 2 r_0], r^-1 (dt - v
  dr) beyond 2 r_0; continuous; one inner piece, past timelike for every r > 0, where his construction, in
  Boyer-Lindquist time, uses three and a partition of unity -- the saving is the horizon-regular time (C2).
- At (v, e) = (1/2, 1/102400) and r_0 = 100, exactly, on Tangherlini: condition (1), r c past timelike on [r_h/2, oo)
  (C2); condition (6), -c# pointing into the black hole inside the saddle and out of it beyond, with Lemma 3.8's
  inequality (C3); condition (3), S computed on Tangherlini from its definition and positive definite on the saddle
  window (C1, C4).
- On sf, exactly: (4)-(5) at dK+ and R_v iff b_K > b_sf - b* and b_sf < b*, b* = 0.99341, the e = 0 thresholds moved by
  0.0066; at the weights (1, -102), T is positive on all of sf with rho_K <= 10 (C7); (5.8) fails only within 0.00166 of
  v (C5).
- The bound on r_0 (C6, a measurement): 86 r_h at this e, 137 r_h at e/4; footnote 14's on Schwarzschild is roughly 81
  m/e^(1/2), 25920 m at this e; by the twenty-fourth verifier's threshold analysis every r_0 > 85.52 r_h works.
- Deduced, by his arguments: (4)-(5) off sf near it, with delta_r not explicit; the smoothing at r_0/2 and 2 r_0.
- OPEN: his Theorem 5.2 in five dimensions (the 3b-estimates of his section 5, with h_0(e), so that h = 10^-6 is not
  certified below it); section 6's five-dimensional steps; his Theorem B.1; E^Upsilon. Labels: computed (cform5.py
  C1-C7; C6 a measurement); deduced; READ ([Hin26a] pp. 3, 38-41, 53, 67; alphaXiv, 2026-10-21); nothing proved.

### 4.16 The gauge potential operator in five dimensions: inputs of [Hin26] Proposition 6.12 (computed; D57)

ROUTES 4.4 item 2's E^Upsilon. gaugepot5.py computes them; N1STAR-PROOF.md 10.15 states Proposition 10.12.
- The indicial roots (G1): s0 lam (lam - 3)(lam^2 - lam - 2 - 4 e gam^2), vl (lam + l)(l + 2 - lam), sl (l + 3 -
  lam)(lam + l - 1) Q; the gap (0, 2) at gam = 0, (0, lam_s1,2) with 2 < lam_s1,2 < lam_s0 for e gam^2 > 0, at the
  weight 2/3 near infinity; the weight 1 moves the root 2 into (1, 2) when e < 1/3 and 0 < gam^2 (1 - 3e) < 1.
  Four-dimensional control: his Lemma 6.6.
- The zero energy kernel of the unmodified box (G2-G4): the dt and spatial parts decouple on the static metric; at l = 0
  the kernel is W*; for l >= 1, A(r_h) = 0 from the equation at the horizon and three energy identities with positive
  forms give none (deduced: [AHW24]'s role in his Lemma 6.10, here elementary).
- The cokernel functional (G5): delta(r - r_h) dr annihilates the range of box(0) at every l; that it spans the cokernel
  needs index 0 ([Hin26c] in five dimensions, OPEN).
- The pairings (G6): (6.21) is 4 pi^2 (his 4 pi, reproduced); W* is divergence-free; eta = -mu^(-3/2) (dv + (3/2) dr) !=
  0; (6.23) = -12 pi^2 c_v - 8 pi^2 c_r, 4 pi^2 at c_H = -(1/2) dr, so (6.26) holds: 4 pi^2 (-i sigma^ + gamma^) != 0.
  The first term of f decays at rho^3 by the dimension, where his needs a cancellation (G7).
- OPEN: [Hin26c]'s low-energy theory in five dimensions (index 0, tf-admissibility, the estimates (6.27)-(6.28)); his
  Step 2, the perturbation near infinity; mode stability of box at nonzero frequencies in five dimensions (his
  Proposition 6.9 rests on [AHW24] Theorem 5.1; deduced in 4.17); the high-energy side of his Proposition 6.9
  (Proposition 6.5, section 6.1's Lemma 6.4; the latter deduced in 4.18) and Lemma 6.1's structure; the radial-point and
  b-regularity behind the kernel. Labels: computed (gaugepot5.py G1-G7, exact); deduced (the kernel, the augmented
  operator's injectivity); READ ([Hin26] pp. 25-26, 82, 113, 117-124; alphaXiv, 2026-10-21); nothing proved.

### 4.17 Mode stability of the 1-form wave operator at nonzero frequency in five dimensions (computed; D58)

ROUTES 4.4 item 2's [Hin26] Proposition 6.9 rests, beside his Proposition 6.5 and [Hin26c]'s Fredholm estimates, on the
mode stability of the unmodified operator box = 2 delta G delta* at sigma != 0, which on Kerr he takes from [AHW24]
Theorem 5.1. modes5.py computes the five-dimensional reductions on Tangherlini; N1STAR-PROOF.md 10.16 states Proposition
10.13 and deduces the mode stability.
- box = d delta + delta d on every 1-form (M1, five arbitrary functions of all coordinates), so delta omega is a scalar
  mode, d omega a Maxwell field, and omega = (i/sigma)(d iota_T omega + iota_T d omega) (M5).
- The master equations, on arbitrary harmonics (M2-M4): scalar waves V_0 = (f/r^2)(kappa + 3/4 + 9 mu/(4 r^2)), Phi =
  r^(3/2) R; Maxwell vector type V_1 = (f/r^2)(lam - 1/4 + 5 mu/(4 r^2)), lam = (l + 1)^2; Maxwell scalar type V_2 =
  (f/r^2)(kappa + 3/4 - 7 mu/(4 r^2)) for W = r^3 F_tr, from Maxwell by R[r^3 F_tr] = (r^2 M_t)' + i sigma r^2 M_r, with
  F_tr = 0 and M = 0 forcing the field to vanish (kappa != 0); at l = 0, M_r = -i sigma F_tr/f. [KI03b]'s (4.23),
  (5.17), (5.19) and (5.20) at Q = 0 (READ).
- All three potentials are positive for r > r_h at l >= 1, and V_0 at l = 0 (M5); the l = 0 Maxwell scalar potential is
  negative near the horizon and is not needed.
- Deduced: for sigma != 0, Im sigma >= 0, a mode smooth across the future horizon and outgoing at infinity vanishes --
  each step an energy identity (Im sigma > 0) or the constant Wronskian (sigma real).
- OPEN: that his spectral family's kernel elements lie in the class in five dimensions ([Hin26c] Theorem 9.5(5)), and
  the index 0 that makes the injective operator invertible; his Proposition 6.5 (its trapping input in 4.18) and
  [Hin26c] Theorem 9.5 in five dimensions, which with this give his Proposition 6.9 there; the low-energy part (4.16).
  Labels: computed (modes5.py M1-M5, exact); deduced (the mode stability); READ ([Hin26] pp. 118-119; [KI03b]); nothing
  proved.

### 4.18 Strong trapping admissibility of the gauge potential operator in five dimensions (computed; D59)

ROUTES 4.4 item 2's [Hin26] Proposition 6.5, mode stability of box^Upsilon at high energies, comes from [Hin26c] Theorem
9.16 with his Lemma 6.4 as the input at the trapped set: strong trapping admissibility ([Hin26c] Definition 5.8).
trap5.py computes the five-dimensional pieces on Tangherlini; N1STAR-PROOF.md 10.17 states Proposition 10.14 and deduces
the lemma.
- S_sub(box) = -i nabla_{H_G} ((6.13)) from the full symbol of 2 delta G delta* on half densities (T0); E^Upsilon
  vanishes near the trapped set ((6.1)), so box is all that enters.
- The trapped set ([Hin26c] Definition 4.13) is the photon sphere r^2 = 2 mu, xi = 0, with C = 4 mu sigma^2 > 0,
  codimension 2, and expansion rate per unit t 1/r_ph = (2 mu)^(-1/2) (T1; four-dimensional control 1/(3^(3/2) M)).
- His frame e_0 = zeta, e_1, e_2 carries over: Gram matrix C J on the characteristic set, and nabla_{H_G} = 0, -2 sigma
  e_0, -2 sigma e_1 on it -- nilpotent (T2-T3; (6.16c) at a = 0 up to the sign of e_1). The complement, the angular
  covectors orthogonal to eta, is a plane in five dimensions where it is his e_3 in four; it is invariant and g is
  parallel on it, so it adds nothing to the skew part (deduced).
- With diag(1, eta^-1, eta^-2) the skew part has norm 2^(1/2) eta^(1/2) (his "O(eta)" holds for the squared weights;
  T4): strongly trapping admissible (deduced). The trapped set is r-normally hyperbolic: the round S^3 geodesic flow,
  periodic, at the normal rate nu (deduced).
- OPEN: [Hin26c] Theorem 9.16 in five dimensions, and with it his Proposition 6.5; [Hin26c] is in 3 + 1 "for
  concreteness" (Remark 5.6). Labels: computed (trap5.py T0-T4, exact); deduced (the lemma, the normal hyperbolicity);
  READ ([Hin26] pp. 113-116; [Hin26c] pp. 88, 90-91, 101-103, 265); nothing proved.

### 4.19 The structure and thresholds of the gauge potential operator in five dimensions (computed; D60)

10.15 named [Hin26] Lemma 6.1's structure and the regularity behind its deduced (a) as OPEN in five dimensions;
[Hin26c]'s estimates need, from them, threshold quantities ([Hin26c] Definition 5.11, (9.16), Lemma 5.12). thresh5.py
computes them; N1STAR-PROOF.md 10.18 states Proposition 10.15.
- On 4+1 Minkowski, box^Upsilon = -2 d_t* rho (rho d_rho - 3/2 - S-bar) + (stationary), S-bar omega = gam (omega +
  omega_t dt* + e <dt*, omega> dt) (U1); spec S-bar = gam (1 - e), 2 gam, gam -- his (6.11)'s, at the weight 2/(D - 2)
  in any dimension; at the weight 1 in five dimensions it would be (3/2)(1 - e) gam, 2 gam, gam (U2). S-bar is this
  endomorphism here and, in a threshold, the number min Re spec of it ([Hin26c] (5.2); [Hin26] footnote 60).
- The horizon threshold: K (the subprincipal symbol at N^*H+ being i xi f'(r_h) K, as in Proposition 10.15(iii)) lower
  triangular with diagonal 1 + c_v gam_H r_h, -1 + 2 c_v gam_H r_h, c_v gam_H r_h (U3), so vartheta_H+ = 1 and s > 3/2
  at gam_H = 0 and, for 10.15's c_H = -(1/2) chi dr, at every gam_H (deduced). Four-dimensional control: his footnote
  71's 3/2.
- Tangherlini at infinity: g00 in rho^2 C^oo for t* = t - r, and g - g-bar = O(rho^2) (U4), so (6.7) holds with a power
  to spare; outgoing kernel elements ~ rho^(3/2 + S-bar), the threshold at R_out -1/2 + S-bar as in (9.16c) (deduced).
- OPEN: the radial point, propagation and trapping estimates of [Hin26c] in five dimensions; the threshold at R_in.
  Labels: computed (thresh5.py U1-U4, exact); deduced; READ ([Hin26] pp. 113-115, 124; [Hin26c] pp. 100-101, 104-105,
  158, 163); nothing proved.

### 4.20 The inputs of the high-energy and Fredholm estimates in five dimensions (computed; D62)

4.18 and 4.19 left [Hin26c] Theorem 9.16 -- and with it [Hin26] Proposition 6.5 -- and the threshold at R_in OPEN;
10.16's OPEN list adds Theorem 9.5(5), the index 0 and the interior. [Hin26c] section 9 sets up general n (Definition
9.4, (9.37), (9.41)) for scalar operators, the bundle case left to the reader (p. 158), and states Theorems 9.5 and 9.16
on the Kerr model with three-dimensional numbers ((9.20), (9.21), (9.55), his Proposition 4.24). hienergy5.py computes
the remaining inputs on five-dimensional Tangherlini; N1STAR-PROOF.md 10.19 states Proposition 10.16 and deduces.
- R_in: at the incoming covector the first-order part of the zero energy operator satisfies A_w + S-bar = D S-bar D, D
  the radial reflection (V1, computed), so vartheta_in = -2 S-bar and the threshold is r + alpha > -1/2 - S-bar, the
  mirror of R_out's (deduced); at gamma = 0 his r > -1/2 (p. 122). Four-dimensional control: the same.
- The trapped set of the semiclassical family: r^2 = 2 mu, nu = 4 (2 mu)^(-1/2), beta_0 = 2, {phi_u, phi_s} > 0, the gap
  nu/(4 beta_0) = (8 mu)^(-1/2), half the expansion rate per unit t (V2); (Gamma.4) with sup p_1 = (2 eta)^(1/2) at a
  point and delta_Gamma(0) = (mu eta)^(1/2) -> 0 (V3; on all of Gamma by the symmetry and 10.17's p_1 = 0 on V_perp,
  deduced).
- The dynamics: W = f/r^2 with one maximum, at the photon sphere; no ergoregion; dr future timelike inside, g_vr = 1 and
  g(g^-1 dr, -d_r) = -1 (V4).
- Deduced, on the reading that section 9's scalar estimates hold on bundles and Theorems 9.5 and 9.16 restated for n = 4
  ((9.20), (9.55) at 3/2, Proposition 4.24 replaced by V4's dynamics): Theorem 9.16, and so [Hin26] Proposition 6.5;
  Theorem 9.5 with kernel elements in A^(3/2 + S-bar - eps) and index 0, and with 10.16 and uniqueness inside the
  horizon the invertibility of the unmodified spectral family at sigma != 0; so his Proposition 6.9 for small E^Upsilon.
- OPEN: section 9's proofs line by line for n = 4 and on bundles (the scalar-to-bundle step, and with the propositions
  Lemmas 9.20, 9.21 and 9.33, Parts (3) and (5) of section 9.2.3 and section 9.3.6); the low-energy theory (Theorems
  9.36-9.41) and his Proposition 6.12; [Hin26a] Theorem 5.2, section 6 and Theorem B.1. Labels: computed (hienergy5.py
  V1-V4, exact); deduced; READ ([Hin26c] pp. 81, 98, 100, 104-105, 157-168, 172, 174-182, 191-193; [Hin26] pp. 113-122,
  200); nothing proved.

### 4.21 The low-energy theory in five dimensions (computed; D64)

4.16 left the index 0, tf-admissibility and the low-energy estimates of [Hin26] Proposition 6.12 OPEN. [Hin26c] section
9.5 is stated for R^n -- Proposition 9.40 for every n >= 3, with the weights (0, n - 2) -- and Theorems 9.36, 9.41 and
Corollary 9.43 write Lemma 3.11's shift at n = 3. lowenergy5.py computes the five-dimensional pieces; N1STAR-PROOF.md
10.20 states Proposition 10.17 and deduces.
- The transition face: on 4+1 Minkowski the 1-form wave operator acts componentwise and, conjugated by e^(i sigma r),
  its spectral family is Delta_e - sigma^2 (L1).
- Bessel at n = 4: order l + 1, exponents l and -(l + 2) -- the zero energy roots -l, l + 2 of 10.15 -- and the Hankel
  asymptotics (mpmath): the outgoing solution, of size r^^-(l+2) near 0, is excluded exactly for weights below 2 (L2);
  with the lower end 0 from the adjoint condition (READ, his Proposition 9.40 for n >= 3), box is tf-admissible on (0,
  2), his Proposition 9.40 at n = 4 (deduced).
- The weights: the shift is n/2 = 2; the augmentation's terms are rho^3 and rho^4, inside the target iff alpha + 2 < 1
  (L3).
- Deduced, on 10.19's reading widened to Lemma 3.11, Theorems 9.36-9.41 and Corollary 9.43 at n = 4 with alpha + 2:
  Theorem 9.36 at n = 4; his Lemma 6.8 (box^Upsilon tf-admissible on (0, lam_s1,2)); Corollary 9.43, index 0, so 10.15's
  horizon functional spans the cokernel of box(0); and his Proposition 6.12, Steps 1-2: with 10.15's modification
  box^Upsilon is mode stable at every sigma with Im sigma >= 0.
- OPEN: section 9 line by line at n = 4; his section 6.5 and Lemma 6.13; his section 7 ([Hin26a]) and section 8 in five
  dimensions. Labels: computed (lowenergy5.py L1-L3; exact, L2's asymptotics numerical); deduced; READ ([Hin26c] pp. 61,
  104, 193-200; [Hin26] pp. 117-124); nothing proved.

### 4.22 [Hin26a] section 6 in five dimensions: the constraint propagation operator (computed; D66)

10.12-10.14 computed the indicial roots, the semiclassical inputs and a c on Tangherlini, and left [Hin26a] section 6's
own steps OPEN: his Theorem 6.2 ([Hin26] Theorem 7.1 (1)-(2)), deduced from his Theorem 5.2 by (6.4), the data weights
of (5.16) and the indicial roots. cpmodes5.py computes the five-dimensional pieces; N1STAR-PROOF.md 10.21 states
Proposition 10.18 and deduces.
- The structure at infinity: box^C = -2 d_t* rho (rho d_rho - 3/2 - S-bar^C) plus a stationary operator on 4+1
  Minkowski, spec S-bar^C = h^-1 {2 (1 - v), (1 - e)(1 - v), 1 - v (3x)}, positive (K1). Four-dimensional control: his,
  with two copies and the shift 1.
- The radial sets: A_w + S-bar^C = D S-bar^C(-v) D, spec h^-1 {2 (1 + v), (1 - e)(1 + v), 1 + v (3x)} (K2); so his
  (B.13) l-window is the same in five dimensions (deduced); its beta-range carries the density's shift.
- The weights: a mode's data in rho^(-2-eps) H-bar_b (r^3), alpha_sf = -C_0 - 5/2 with alpha_K = 1, and l in [-C_0 - 2,
  0) (K3).
- Deduced, on [Hin26a] Theorem 5.2 in five dimensions (OPEN): no outgoing mode of box^C at sigma != 0, Im sigma >= 0;
  the zero energy operator injective, both for every h < h_0; of index 0 by the radial ODEs of the static metric with
  10.12's roots at Proposition 10.9's point (h = 10^-6), C_0 <= 100, and invertible given the Fredholm property, whose
  horizon threshold is OPEN; so his Theorem 6.2 there, (2) at one parameter point, provided 10^-6 < h_0.
- OPEN: his Theorem 5.2 and Theorem B.1 in five dimensions; [Hin26] Theorem 7.1(4); [Hin26] section 6.5, Lemma 6.13 and
  sections 7-8 (4.23 and 4.24 deduce Theorems 5.2, B.1 and 7.1(4) on readings). Labels: computed (cpmodes5.py K1-K3,
  exact); deduced; READ ([Hin26a] pp. 1-3, 9-11, 38-43, 47, 51, 54, 64, 66-69, 87, 93, 98; [Hin26] p. 135); nothing
  proved.

### 4.23 [Hin26a] Theorem 5.2 in five dimensions: the inputs, and the reading (computed; D67)

4.22 deduced [Hin26a] Theorem 6.2 from his Theorem 5.2 and left Theorem 5.2 OPEN. His proof (section 5.2) takes from the
metric and from c: Lemma 5.3's memberships, from (2.12)-(2.14); Lemmas 3.5 and 3.7 (Propositions 5.5-5.6); his
Proposition 5.1 (3)-(6) (Propositions 5.8-5.12); and two time functions (Proposition 5.16, whose Lemma 5.14 and
Corollary 5.15 are stated for general n). 10.13-10.14 computed most of these or deduced them from computed quantities;
solv5.py computes the rest, the uniformity Corollary 5.15 asks being deduced from Q1; N1STAR-PROOF.md 10.22 states
Proposition 10.19 and deduces.
- The 3sc structure: in Cartesian coordinates g^-1 = eta^-1 - mu r^-2 k# (x) k#, and Gamma(lam x; mu) = lam^-1 Gamma(x;
  mu lam^-2) with no mu^0 term, so Gamma in mu rho^3 C^oo, two powers better than (2.12) asks (Q1). Four-dimensional
  control: Schwarzschild, rho^2.
- Near X: r^2 G(d tau) = -(1 - tau^2) - mu r^-2 (1 + tau)^2, so d tau is past timelike for g_3b on tau in [0, T] for
  every T < 1, uniformly to infinity (Q2). Near Sigma# = {r = r_h/2}: dr future timelike, m - r a time function (Q3).
- The weights: his Proposition 5.1 (4)-(5) at (alpha_K, alpha_sf) = (1, -C_0 - 5/2), with positive roots at the critical
  points for every C_0 >= 0, and on all of sf with rho_K <= 10 at C_0 = 100 (Q4); the five-dimensional (5.14) at e =
  1/102400 is alpha_sf < b* - 1, alpha_K > alpha_sf + 1 - b*, b* = 0.99340731... (10.14).
- Deduced, on the reading that his 3b-analysis (sections 2.3 and 5.2) holds in five dimensions: his Theorem 5.2 on
  Tangherlini at (v, e) = (1/2, 1/102400) with 10.14's c, h_0 = h_0(e, C_0) not explicit; with 4.22, his Theorem 6.2
  there, (1) for every h < h_0 and (2) at h = 10^-6 if that is below h_0, C_0 <= 100, given 10.21(d)'s horizon threshold
  (OPEN).
- OPEN: that reading line by line; h_0; 10.21(d)'s horizon threshold; his Theorem B.1 and [Hin26] Theorem 7.1(4) (4.24
  deduces them on the same reading); [Hin26] sections 6.5, 7.2 and 8. Labels: computed (solv5.py Q1-Q4, exact); deduced;
  READ ([Hin26a] pp. 9, 12-16, 25-27, 38, 41-44, 47-48, 51-52, 54, 56, 58-60, 64, 66); nothing proved.

### 4.24 [Hin26a] Theorem B.1 in five dimensions, and [Hin26] Theorem 7.1(4) (computed; D69, D71, D72)

4.22-4.23 left [Hin26a] Theorem B.1, the transition face problem on Minkowski space, OPEN in five dimensions, and with
it [Hin26] Theorem 7.1(4), which applies it at beta' = -beta + 3/2 - eps. tface5.py computes the five-dimensional
pieces; N1STAR-PROOF.md 10.23 states Proposition 10.20 and deduces.
- Dilations: box^C on 4+1 Minkowski in t* = t - r is homogeneous of degree -2, every coefficient checked (F1); so
  (B.10), and, deduced, (B.12): at the origin r^2 box^C(0), whose indicial roots are minus those at infinity.
  Four-dimensional control: his, at the trace weight 1.
- The origin: r^mu lies in r^beta L^2(r^3 dr) iff mu > beta - 2, so with 10.12's roots the weights there are beta in (0,
  2 + C_0], C_0 <= 100; his (1/2, 3/2 + C_0] (F2).
- The thresholds at (v, e) = (1/2, 1/102400): at the cone face alpha_cf > 1 - b* (0 as e -> 0; his 1/2, recomputed in
  four dimensions), bracketed at d = 0.9934 and 0.9935 in cform5.py's T; at the sink alpha_sf < b* - 1 (4.23); -(1/2)
  r^2 l(dr/r) is his matrix with three copies of v, with positive eigenvalues (F3).
- Section B.4: (alpha_sf, alpha_cf) = (-5/2, 5/2), the closing integral divergent, l = -1/2 in the l-window, beta = 7/2
  for C_0 >= 3/2, (B.33)'s data weights alpha_sf + 1/2 and alpha_cf - 1/2 from Omega's one time direction; beta' =
  -beta + 2 - eps in (0, 2 + C_0] for every small eps iff beta in [-C_0, 2), and the adjoint half's threshold at R_in,
  from the conjugated adjoint's computed bottom h^-1 (1 - e)(1 + v), the l-window's lower end (F4).
- Proposition B.2's index 0: the free operator's roots at the origin, -3, -2 | 0, 1 at l = 0, -l - 3, -l - 2, -l - 1 |
  l - 1, l, l + 1 for scalar type l >= 1, -l - 2 | l for vector type; the windows contain (-2, 0) and the crossing
  counts 2, 3, 1 are 10.12's (F5). Four-dimensional control: his p. 91.
- Deduced, on the readings of 4.21 and 4.23, the latter here in Theorem B.4's edge-b version: Proposition B.2 (index 0
  by F5), Theorem B.4 and his Theorem B.1 on 4+1 Minkowski with beta in (0, 2 + C_0], and [Hin26] Theorem 7.1(4), both
  halves, with every beta in [-C_0, 2), at (v, e) = (1/2, 1/102400), C_0 <= 100, and h = 10^-6 if that is below h_0.
- OPEN: the readings line by line; h_0; box^C's horizon threshold; [Hin26] sections 6.5, 7.2 and 8 (4.25 takes
  section 8's Lemma 8.4). Labels: computed (tface5.py F1-F5, exact); deduced; READ ([Hin26a] pp. 85-91, 93-94, 96-98;
  [Hin26] pp. 136-137; [Hin26c] Definition 5.10, Theorem 9.38(3), (5), Corollary 9.39, Proposition 9.40); nothing
  proved.

### 4.25 [Hin26] Lemma 8.4 in five dimensions: the gauge-fixed Einstein operator's indicial roots (computed; D72)

4.24 left [Hin26] section 8 OPEN in five dimensions. lin5.py computes the indicial roots of the linearized gauge-fixed
Einstein operator L = D Ric + delta*_{E^C} delta_{E^Ups} G on 4+1 Minkowski by harmonic type; N1STAR-PROOF.md 10.24
states Proposition 10.21 and deduces.
- The types: at two points of R^4 the scalar, vector and tensor types (harmonics of C^2 = R^4) are preserved with the
  same indicial matrix, and his (8.5) holds (E1).
- The factorization, every parameter symbolic: det N_L = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det N_C(lam + 1)
  / D, with D = (lam - 1)^2 at s0 and s1, lam (lam - 2) at v1 and 1 for l >= 2, and at the tensor type det N_L = c
  (lam + l)(lam - l - 2) (E2); four-dimensional control, his (1)-(5) (E3). The factors are gaugepot5.py's and
  damping5.py's, and at zero damping the roots are integers outside (0, 2), as many on each side (E4).
- At the point (v, e_C, gam_C) = (1/2, 1/102400, 10^6), (e_U, gam_U) = (1/100, 1/100), for l <= 12: simple; none with
  real part in (0, 1]; s0 4 | 4, s1 6 | 6, sl 7 | 7, v1 2 | 2, vl 3 | 3, tl 1 | 1; box^C's nonpositive ones below
  -101; 0 a root at s0 and s2 only, its kernel annihilated by the gauge operator (E5).
- Deduced, for every l at the point, from 10.12(i)'s box^Upsilon roots and Proposition 10.9's box^C roots: his Lemma 8.4
  in five dimensions -- the gap begins at 0, which 4.13 left open, and reaches past 1; each type splits evenly; box^C's
  nonpositive roots lie below -101 -- his Lemma 8.5, and his Proposition 8.6, tf-admissibility with weight in (0,
  eps_ind) for small gam_Ups, on the readings of 4.20-4.24, but for the spectrum of S-bar_{E^Ups, E^C} (his Lemma 8.2),
  which the domain step of its kernel half needs.
- OPEN: that spectrum and his (8.7) in five dimensions (computed in 4.26); simplicity and (8.13) beyond l <= 12; how
  small gam_Ups must be, and h_0; sections 8.4-8.5 and 9-10 in five dimensions (his Propositions 8.3 and 8.8 deduced in
  4.27 and 4.28). Labels: computed (lin5.py E1-E5, exact, the point's roots by mpmath); deduced; READ ([Hin26] pp. 28,
  117, 135-137, 144-146, 149-153); nothing proved.

### 4.26 [Hin26] Lemma 8.2's S-bar and (8.7) in five dimensions (computed; D74, D76)

4.25 left one input of [Hin26] Proposition 8.6 OPEN: the spectrum of S-bar_{E^Ups, E^C}, by which the linearized
gauge-fixed Einstein operator's d_t* terms differ from the wave operator's, and his (8.7), min spec S-bar = 0, with
which the kernel half's decay improves before the outgoing threshold is applied. sbar5.py computes it; N1STAR-PROOF.md
10.25 states Proposition 10.22 and deduces.
- The structure: on 4+1 Minkowski in t* = t - r the wave operator is -2 d_t* rho (rho d_rho - 3/2) plus a stationary
  operator, and 2 L - box is first order with d_t* coefficient 2 rho S-bar, S-bar constant (S1).
- The spectrum: {0 (five times), gam_Ups (three times), 2 gam_Ups, (1 - e_Ups) gam_Ups, (1 - v) gam_C (three times),
  2 (1 - v) gam_C, (1 - e_C)(1 - v) gam_C}, the union of the S-bar of box^Ups (4.19) and of box^C (4.22) with five
  zeros; every eigenvalue >= 0, so min spec S-bar = 0, his (8.7); at the trace weight 1 the (1 - e) gam scale by 3/2
  and the minimum stays 0. Four-dimensional control: his (8.8) (S2).
- The consequences: the improvement to 3/2 - eps (his 1 - eps), the threshold -1/2 dimension-free, and Corollary 8.7's
  beta_sctf < 3/2 (his 1) (S3).
- Deduced: his (8.4) on Tangherlini, and Proposition 8.6 at Proposition 10.9's point for small gam_Ups on the readings
  of 4.20-4.25, the step 4.25 left OPEN now filled.
- OPEN: the readings line by line; how small gam_Ups must be, and h_0; sections 8.4-8.5 and 9-10 in five dimensions
  (his Propositions 8.3 and 8.8 deduced in 4.27 and 4.28). Labels: computed (sbar5.py S1-S3, exact); deduced; READ
  ([Hin26] pp. 144-146, 152-153); nothing proved.

### 4.27 [Hin26] Proposition 8.3 in five dimensions: strong trapping admissibility of L (computed; D75, D77)

His Proposition 8.3 makes 2 L strongly trapping admissible for fixed modification parameters, from a printed 10 x 10
matrix A at the trapped set ((8.10)-(8.12)). strap5.py computes it on an abstract quasi-orthonormal frame;
N1STAR-PROOF.md 10.26 states Proposition 10.23 and deduces.
- Four-dimensional control: with his sign convention the computed A equals his printed matrix in all 100 entries and is
  upper triangular in his (8.12) with his eigenvalues in his order; 10.17's sign is his after e_1 -> -e_1, c_1 -> -c_1
  (P1).
- Five dimensions: det(lam - A) = lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2), the last
  factor with 3 (1 - e_C) at the trace weight 1; a constant basis triangularizes A for every c (P2).
- With c's angular part zero, as for 10.14's c = a(r) dt + b(r) dr: A commutes with the rotation of the angular plane,
  and in rotation-adapted units it is block triangular with scalar blocks and the rotation skew within each unit (P3).
- Deduced: his Proposition 8.3 on Tangherlini, c_2 < 0 at the photon sphere since c is past timelike there, the angular
  pairs weighted alike so that the rotation of the plane along the flow stays skew.
- OPEN: [Hin26c]'s high-energy estimates for symmetric 2-tensors at n = 4 (the reading of 4.20); his sections 8.4-8.5
  and 9-10 in five dimensions (his Proposition 8.8 deduced in 4.28). Labels: computed (strap5.py P1-P3, exact); deduced;
  READ ([Hin26] pp. 34, 113-116, 147-149); nothing proved.

### 4.28 [Hin26] Proposition 8.8 in five dimensions: the linearized Einstein operator's mode stability (computed; D78)

His Proposition 8.8 makes L-hat(sigma) injective at 0 != sigma, Im sigma >= 0, from his Theorem 7.1(1), his Proposition
6.12 and [AHW24] Theorem 6.1(1): an outgoing mode of D Ric is pure gauge. gmodes5.py computes the Kodama-Ishibashi
reduction of D Ric on five-dimensional Tangherlini for every harmonic; N1STAR-PROOF.md 10.27 states Proposition 10.24
and deduces.
- Every type at l >= 2: the tensor type with [KI03] (5.3) and V_T = (f/r^2)(l (l + 2) + 3/4 + 9 mu/(4 r^2)) (G1); the
  vector type in the gauge H_T = 0, its master field r^(-3/2) Omega with V_V = (f/r^2)(l (l + 2) + 3/4 - 27 mu/(4 r^2))
  (G2); the scalar type in [KI03]'s gauge, the computed equations giving their first-order system (2.24) and one
  preserved constraint, their master field (3.1) solving (3.5), det[Phi; Phi'; C] = -r^4 (r^2 - mu)^5 (G3).
- l <= 1 at sigma != 0 (scalar l = 0 and 1, vector l = 1): pure gauge, through gauge 1-forms algebraic in the mode (G4).
- The potentials positive at l >= 2; in ingoing coordinates the r-row of delta* xi = u an ODE across the horizon, and
  the master fields free of 1/f (G5).
- Deduced: [AHW24] Theorem 6.1(1) on five-dimensional Tangherlini, in the class of 10.16, by 10.16's argument on each
  master equation; and his Proposition 8.8 there, on the readings of 4.20-4.27, at Proposition 10.9's point with gam_Ups
  small.
- OPEN: the kernel elements' class, omega's continuation inside the horizon (before his Proposition 6.12 applies) and
  the interior uniqueness, as in 10.16; how small gam_Ups must be, and h_0; his Proposition 8.9, Remark 8.10 and
  Proposition 8.11 (zero energy, [AHW24] Theorem 6.1(2); Proposition 8.9 deduced in 4.29), section 8.5 and sections 9-10
  in five dimensions. Labels: computed (gmodes5.py G1-G5, exact); deduced; READ ([Hin26] pp. 25, 153-154; [KI03] pp.
  4-10, 13-15, 18-20); nothing proved.

### 4.29 [Hin26] section 6.5.1 and Proposition 8.9 in five dimensions: the zero energy states (computed; D80, D82)

His section 6.5.1 builds box^Ups's zero energy states from the Minkowskian translations, boosts and rotations, and his
Proposition 8.9 brings the linearized Kerr metrics into the gauge, with logarithms at (6.31) and (8.19) where an
indicial root is met. zstates5.py computes the five-dimensional orders, defects and exponents; N1STAR-PROOF.md 10.28
states Proposition 10.25 and deduces.
- Orders: g - gbar in rho^2, Gamma in rho^3, so the delta* and box^Ups differences in rho^3 Diff^0_b and rho^4 Diff^2_b;
  r* without a logarithm (Z1).
- Translations: delta*_g dx^1 at rho^3, box dx^1 at rho^4, the correction at rho^2, 2 an s1 root only at z = 0 (Z2);
  boosts: the stationary defect K at rho^2, with his t-bar = t* + r too, and the stationary residual at rho^3, the
  correction at rho^1, 1 no s1 root (Z3); all six rotations Killing on Tangherlini, V_1 = so(4) (Z4).
- The linearized metrics: d_mu g at rho^2, h_A at rho^3, both vacuum; the sources at rho^3 (s0) and, delta G h_A
  vanishing, E^Ups h_A at rho^4 (v1); 1 no s0 root, 2 no v1 root (Z5).
- The Myers-Perry family ([ER08] (32)-(33)): Ricci-flat at three exact points, Tangherlini at a = 0, d_a g at a = 0 =
  -h_A (Z6).
- Deduced: his Proposition 6.15 and Proposition 8.9 in five dimensions, every order one higher and neither logarithm, on
  his Lemma 6.13 in five dimensions; six angular momenta in place of three.
- OPEN: his Lemma 6.13 in five dimensions (10.20; deduced in 4.30); the index sets; his Proposition 6.18, section 7.2,
  Proposition 8.11, Lemma 8.12 and Corollary 8.13 in five dimensions (the candidates for the kernel number 1 + 6 + 4 =
  11 against his 7, the count not established); section 8.5 and sections 9-10; how small gam_Ups must be, and h_0.
  Labels: computed (zstates5.py Z1-Z6, exact); deduced; READ ([Hin26] pp. 25, 81, 113, 117, 124-128, 154-155, 157;
  [ER08] p. 14); nothing proved.

### 4.30 [Hin26] Lemma 6.13 and Proposition 6.18 (1)-(3) in five dimensions (computed; D81)

His Lemma 6.13 inverts box^Ups(0) on the weights of its indicial gap; his Proposition 6.18 builds generalized zero
energy states, polynomials in t*, for the roots of L-hat(0) in [-3, 0] that are not stationary pure gauge. genstates5.py
computes the leading terms of the first three in five dimensions, with his printed four-dimensional numbers as the
control; N1STAR-PROOF.md 10.29 states Proposition 10.26 and deduces.
- Part (1), the s0 root 0: W = r(-dt + b dr), b = (2 - e_U)/(4 e_U); the Tangherlini source without a rho^2 term, so no
  logarithm (H1).
- Part (2), the s1 root -1: the boost to second order, W at rho^-2 with exact coefficients, h-bar^2_s1 stationary and
  nonzero (H2). Part (3), the v1 root -1: kappa = 1 + 2 gam_U/5, his (6.40) as (1/4)(1 +- 2 gam_U/5) (H3).
- The control: his (0, -1/4, -1/2, 0), (0, 0, 0, -1, 1/2, 0), kappa = 1 + gam_U/2 and (6.40) reproduced (H4); the gap's
  top lam_s1,2 = 2 + z/12 + O(z^2) < lam_s0 (H5).
- Deduced: his Lemma 6.13 in five dimensions on 10.20's readings, every correction of 4.29 inside the gap; his
  Proposition 6.18 (1)-(3) there, six rotation states at a = 0.
- OPEN: the readings of 10.20 line by line; the index sets; his Proposition 6.18 (4)-(7), section 7.2, Proposition 8.11,
  Lemma 8.12 and Corollary 8.13 in five dimensions; section 8.5 and sections 9-10; how small gam_Ups must be, and h_0.
  Labels: computed (genstates5.py H1-H5, exact); deduced; READ ([Hin26] pp. 51-52, 64-67, 81, 113, 117-119, 121,
  124-125, 129-134); nothing proved.
