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

- **[Hun19]** (P.-K. Hung, arXiv:1909.06733v1, the even part in four dimensions). Theorems 1.1-1.4: a one-form
  solving box W = 0 decays at tau^(-2+) in energy after its l = 0 part is subtracted; so does h solving the harmonic
  gauge and the Lichnerowicz equation; the l = 0 part of W converges to c W*, W* = dt/r + (2M/r^2) f^-1 dr (8.1); and
  h_(l=0) converges to c_1 K* + c_2 pi_{W*}, K* = K + pi_{W**} (8.39) growing linearly in t. The mechanism (sections
  4-8): h is split into seven components whose zeroth-order matrix A + B + O in box H = (A + B + U) H is semi-positive
  (Proposition 4.2, Remark 4.5), which gives red-shift and r^p estimates near the horizon and null infinity (Proposition
  4.1); a gauge vector W = (W_0, W_1, W_2) carries h to the Regge-Wheeler gauge, determined by invertible angular
  operators for l >= 2 ((4.11)-(4.13)); the trace S_W of pi_W, and P_even and Q_even -- components of dW when S_W and
  the Zerilli field vanish ((4.18)-(4.20)) -- satisfy with W_0, W_1, W_2 a *triangular* system of scalar wave equations
  with potentials and sources (Proposition 4.7, (4.21)-(4.25)): box S = 0, box P_even = d_t S_W, and box W_0 + (2M/r^3)
  W_0 = -(2M/r^3) P_even + (Zerilli terms)                                           (4.21) and its two companions; each
  rung is an inhomogeneous wave equation with a radial potential V treated by the vector field method of Appendix A
  under the single condition l_0(l_0 + 1)/r^2 + V >= 0 ((A.3)) -- red-shift, Morawetz and the r^p hierarchy of Dafermos
  and Rodnianski, Schlue's commutators L and rL, Angelopoulos-Aretakis-Gajic's r^2 L -- with a modification W_0 -> W_0 +
  eta_b (...) absorbing a source that grows like u + r ((4.35)-(4.36), Lemma 4.9). The l = 0 sector (section 8): if
  P_even and S_W vanish the one-form is stationary and solves an ODE in r with two solutions, one regular at the horizon
  (W*); with P_even and S_W decaying, the coefficient of the singular solution decays by the red-shift estimate (Theorem
  8.1); K does not satisfy the gauge (Gamma[K] = dv/R^2) and K* repairs it. - **[HKW18]** (arXiv:1809.05144v1). Theorem
  2: the gauge-invariant master quantities of the scalar and tensor type decay at tau^-2 in energy in spacetime
  dimension six and below, uniformly in l (section 10.5: the potentials converge as l -> oo); the metric components are
  deferred ("We do not treat this matter in the current paper", p. 4), and Hung's wave-map gauge work is named there as
  "more promising". The tools are stated for a general Regge-Wheeler-type equation (Definition 8: V radial, bounded,
  comparable to 1/r^2 at infinity, not necessarily non-negative): the T-energy comparison (111), the Morawetz current
  with Schlue's f vanishing at the photon sphere (Lemma 13, (119)-(123); for n = 3 the choice f = (1 - 4M/r^2)(1 - M/r^2
  + 4M^2/(5r^4)), beta = 1/2, section 9.3.2), the r^p hierarchy with Phi = r^(n/2) Psi for 1 <= p <= 2 (Proposition 15,
  Theorem 16) requiring V = a_0/r^2 + b_0 M/r^(n+1) + ... with a_0 > 0, and the decay theorem (Theorem 18). The
  restriction to six dimensions is the near-horizon positivity of the Morawetz current, impossible by their construction
  for n >= 5 (section 9.3.2). - **[Sch13]** (V. Schlue, arXiv:1012.5963, Anal. PDE 6 (2013)). For the scalar wave
  equation on Schwarzschild of spatial dimension n >= 3 (five spacetime dimensions is n = 4 there): E[phi](Sigma_tau) <=
  C D/tau^2 (Theorem 1, (1.9)), the first-order energy at tau^-(4-2delta) on bounded r ((1.10)), and r^((n-2)/2)|phi| <=
  C D/tau^(3/2-delta) (Theorem 2); the photon sphere at r = (nm)^(1/(n-2)) (section 2), r^2 = 2 mu here; radial
  multipliers f(r*) d_r* changing sign at the photon sphere with Poincare on the spheres (section 4); the p-hierarchy
  with r^p d_v* on psi = r^((n-1)/2) phi, p in {1, 2}, and the commutation with d_v* for the four-step hierarchy
  (section 5). No potential and no source are treated there; Hung's Appendix A says how both enter. - **[CYDL03]**: the
  tails t^-(2l+3) in five dimensions, measured here as T6. - **[KI03b]** (H. Kodama, A. Ishibashi,
  arXiv:hep-th/0308128v4). The Maxwell field on the n+2-dimensional static black hole, scalar type: F_ab = epsilon_ab E
  S, F_ai = E_a S_i, with E_a = (k/r^(n-1))(D_a A + J~_a) (5.17), r^n E = -k^2 A at Q = 0 (5.19), and the master
  equation r^(n-2) D^a (D_a A / r^(n-2)) - (k^2/r^2) A = -r^(n-2) D^a (J~_a / r^(n-2)) (5.20) -- no potential beyond
  k^2/r^2 in that normalisation; the vector type (4.23) has (k_V^2 + (n - 1)K)/r^2. - **[Hin26]** (P. Hintz,
  arXiv:2606.28253v2, with [Hin26a] arXiv:2606.27658 and [Hin26c] arXiv:2606.28008). The nonlinear stability of
  subextremal Kerr in a generalized wave map gauge Upsilon(g) - theta = 0 whose source theta lies in a
  finite-dimensional space, with strong constraint damping (the modified symmetric gradient delta*_{g,E^C}) and a
  Nash-Moser iteration; "we work directly with the tensorial equation" and use as black boxes the mode stability of the
  ungauged linearized equation (via Teukolsky, by Andersson, Hafner and Whiting, cited there) and of two 1-form wave
  operators -- the gauge potential operator box^Upsilon = 2 delta_{E^Upsilon} G delta* and the constraint propagation
  operator box^C (section 1.4.1): "mode stability for [both] implies mode stability for the gauge-fixed linearized
  Einstein operator L_b, and a simple structure of its (generalized) zero energy nullspace". That nullspace on Kerr is
  the linearized Kerr family in gauge, the deformation tensors of asymptotic translations, and (generalized) those of
  boosts -- a second-order pole of the resolvent at zero energy, "forward solutions of L_b lose two powers of
  t_*-decay". The constraint damping must satisfy (1.43): no indicial root of the zero energy operator of box^C with
  real part in [-C_0, 1), C_0 = 100, which needs a non-perturbative E^C ([Hin26a]); mode stability of box^Upsilon at
  zero energy is arranged perturbatively (Proposition 6.12), since the plain 1-form wave operator has a zero energy
  bound state ([Hin26c] p. 21, citing Andersson, Hafner and Whiting) -- Hung's W*. [Hin26c] gives the tame estimates for
  wave-type operators whose stationary model is mode stable and may carry zero energy bound states ("examples include
  the wave operator on 1-forms and the linearization of the Einstein field equations in generalized harmonic gauge"),
  "in 3 + 1 dimensions for concreteness" (Remark 5.6), with the Minkowskian zero-energy structure stated in general
  spatial dimension n: the wave operator on tensors is tf-admissible with all weights in the indicial gap (0, n - 2)
  (Proposition 9.40). - **The 2+1 reductions.** [KS17] (Klainerman-Szeftel, arXiv:1711.07597): nonlinear stability of
  Schwarzschild under polarized axisymmetric perturbations, a 2+1 problem. [Hun15] (C. Huneau, arXiv:1511.07002):
  nonlinear stability of Minkowski with a translation Killing field, where "the 3 + 1 vacuum Einstein equations reduce
  to the 2 + 1 Einstein equations coupled to a wave map". [HL17] (Huneau-Luk, arXiv:1706.09499): the polarized U(1)
  Einstein equations in an elliptic gauge, the setting of the theorem this paper answers. [Hol08]: the five-dimensional
  biaxial class, a 1+1 problem, closed by vector field multipliers and a bootstrap.

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
   Tangherlini has the zero energy state W* (W2); the perturbative modification E^Upsilon that removes it ([Hin26]
   Proposition 6.12) is a static argument and should carry. The constraint propagation operator box^C needs the
   strong damping (1.43), and [Hin26a]'s construction is on Kerr; a five-dimensional construction does not exist and
   is the first genuinely new object of the route. Tangherlini being static, the indicial-root computation it needs is
   an ODE problem in r for each l of the class.
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
(4.6), and his Proposition 4.1 is deduced on it (4.7; N1STAR-PROOF.md Proposition 10.3): the energy of h in the harmonic
gauge is controlled by its data and by h on the compact region [r_rs,H, R_null + r_h], with [Sch13]'s r^p weights at
null infinity and the red-shift at r_h, constants not tracked. Next, in order: route A's rungs, one proposition each, in
the order of 4.3(2), the Morawetz current for the Maxwell potential first -- the compact region is where they enter;
the growing source (4.3(3)) and l = 0 (4.3(4)); then route B's item 2, the five-dimensional constraint damping.

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
