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
   6.13 in five dimensions (4.29; the orders and exponents computed, the rest deduced); his Lemma 6.13, on 10.20's
   readings, and Proposition 6.18 (1)-(3) hold there too (4.30; the leading terms computed, the rest deduced), and so
   does Proposition 6.18 (4)-(7) (4.31; the leading terms computed, the rest deduced); his section 7.2's dual states hold
   there on 10.21(e)'s readings, eleven against his seven, and section 7.2.1's structure at first order in the rotation
   (4.32; the leading terms computed, the rest deduced) and at every spin (4.37; Lemma 7.5 an identity of the
   Myers-Perry family, computed exactly, the rest deduced); his Lemma 8.12's pairings are non-degenerate there, so his
   Proposition 8.11 and Corollary 8.13 hold with eleven for seven up to [AHW24] Theorem 6.1(2) in five dimensions (4.33;
   the pairings computed, the rest deduced); and that rigidity holds on five-dimensional Tangherlini, the mass and the
   six rotations plus pure gauge, so they hold there, and near it on a reading (4.34; the stationary equations computed,
   the rest deduced); the line-by-line readings of [Hin26a] sections 2.3 and 5.2 and Appendix B and of [Hin26c] section
   9 at n = 4, and the rest of the item, section 8.5 beyond 4.35 (its physical states at a = 0, and near it on
   10.33(f)'s readings, the tensor types included; 4.36: on readings five dimensions needs only those at l = 2, for any
   iota+ order in (1, 2]), and [AHW24] Theorem 6.1(2) in five dimensions beyond a = 0, are OPEN.
3. *The zero-energy nullspace in the class* is the mass change in gauge (4.2(ii)), and in the harmonic gauge of
   W1-W6 it is not simple: K* = t pi_{W*} + (stationary) with Gamma[K*] = 0 (W3) is a t-linear zero-energy state, the
   second-order structure. Whether the five-dimensional E^Upsilon of item 2 removes W* and leaves a first-order pole,
   so that the forward solutions lose one power of t_* rather than two and no centre-of-mass or momentum
   elimination ([Hin26] section 1.4.2) is needed, is OPEN: it rests on item 2, not on the symmetry (D47). And at a = 0,
   where 10.35(b) reads the pole as of order 2, whether logarithms enter it, the mass state r^-2 lying just outside L^2
   in four spatial dimensions, is OPEN too (D95).
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
and 4.30 (10.29, Proposition 10.26, computed; deduced) deduces his Lemma 6.13 there on 10.20's readings and computes the
leading terms of his Proposition 6.18 (1)-(3), the time translation's state without his logarithm and his (6.40) as
(1/4)(1 +- 2 gam_U/5); and 4.31 (10.30, Proposition 10.27, computed; deduced) computes the leading terms of his
Proposition 6.18 (4)-(7) and deduces it there, every stationary correction one order faster; and 4.32 (10.31, Proposition
10.28, computed; deduced) computes the adjoint constraint operator's roots and the leading terms of his section 7.2's
dual states and deduces his Lemma 7.2 and Proposition 7.3 there, section 7.2.1 at first order in the rotation; and 4.33
(10.32, Proposition 10.29, computed; deduced) computes his Lemma 8.12's pairings as boundary pairings, -8 pi times the
ADM mass and angular momentum and 4 pi M times the centre of mass, and deduces his Proposition 8.11 and Corollary 8.13
there with eleven for seven, up to [AHW24] Theorem 6.1(2); and 4.34 (10.33, Proposition 10.30, computed; deduced)
computes the stationary solutions on Tangherlini harmonic by harmonic and deduces that theorem there, and with it his
Proposition 8.11 at a = 0 and, on a reading, near it, with his Corollary 8.13 (at a = 0 alone the augmented operator's
invertibility). And 4.35 (10.34, Proposition 10.31, computed; deduced) finds his section 8.5's physical states in five
dimensions: at a = 0 for every l >= 2 and the three types, the static tidal solutions in Gauss functions of r^2/mu, and
near it for his l = 2, 3 by his construction with its Step 2 modified, on his Proposition 7.4 in five dimensions, his
Lemma 8.15 carried over with so(4)'s bracket for the cross product. And 4.36 (10.35, Proposition 10.32, computed;
deduced) finds what five dimensions needs: for any iota+ order alpha_5 in (1, 2] the physical states s2, v2 and t2 at -2
alone, without companions, in the window [alpha_5 - 4, 0] -- [-2, 0] if the slowest iota+ term is the mass aspect's
t*^-2, [-5/2, 0] if the radiative order reaches iota+ as his index sets carry it (D95). And 4.37 (10.36, Proposition
10.33, computed; deduced) finds his section 7.2.1 at every spin: Lemma 7.5 is the identity delta* V_b = (1/2) D_A
g_b([A_b, A_V]) of the Myers-Perry family over so(4), so h-sharp is defined on all of so(4) and his Proposition 7.4 and
(7.19) follow on readings. Next: the rest of item 2 -- sections 9-10 -- in five dimensions.

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
  the interior uniqueness, as in 10.16 (both closed: 4.80); how small gam_Ups must be, and h_0; his Proposition 8.9,
  Remark 8.10 and
  Proposition 8.11 (zero energy; Proposition 8.9 deduced in 4.29, Proposition 8.11 in 4.33-4.34 at a = 0, and near it on
  a reading), section 8.5 and sections 9-10 in five dimensions. Labels: computed (gmodes5.py G1-G5, exact); deduced;
  READ ([Hin26] pp. 25, 153-154; [KI03] pp. 4-10, 13-15, 18-20); nothing proved.

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
- OPEN: the readings of 10.20, on which 4.30 deduces his Lemma 6.13 in five dimensions (and 4.30-4.31 his Proposition
  6.18); the index sets; Proposition 8.11, Lemma 8.12 and Corollary 8.13 in five dimensions beyond 4.33-4.34 (the kernel
  1 + 6 + 4 = 11 against his 7, the count deduced at a = 0, and near it on a reading); section 8.5 and sections 9-10;
  how small gam_Ups must be, and h_0. Labels: computed (zstates5.py Z1-Z6, exact); deduced; READ ([Hin26] pp. 25, 81,
  113, 117, 124-128, 154-155, 157; [ER08] p. 14); nothing proved.

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
- OPEN: the readings of 10.20 line by line; the index sets; section 7.2 (4.32's), Proposition 8.11, Lemma 8.12 and
  Corollary 8.13 in five dimensions beyond 4.33-4.34's a = 0 and its neighbourhood (his Proposition 6.18 (4)-(7) is
  4.31's); section 8.5 and sections 9-10; how small gam_Ups must be, and h_0. Labels: computed (genstates5.py H1-H5,
  exact); deduced; READ ([Hin26] pp. 51-52, 64-67, 81, 113, 117-119, 121, 124-125, 128-134); nothing proved.

### 4.31 [Hin26] Proposition 6.18 (4)-(7) in five dimensions (computed; D84, D85)

His parts (4)-(7) build the pure gauge states whose gauge potentials carry no symmetry, from the gauge potential
operator's growing roots below -1 and the s2 root -1. puregauge5.py computes the indicial families, the classes, the
symmetric gradient's injectivity, the resonances and the states' leading terms in five dimensions, four-dimensional
Minkowski the control; N1STAR-PROOF.md 10.30 states Proposition 10.27 and deduces.

- The families: det N0 exactly 10.15(i)'s polynomial, N1 = -2 (lam - 3/2) + 2 S-bar; in four dimensions his Lemma 6.6
  matrices entry by entry (J1).
- The classes: s0's -1 - z/3 + O(z^2), Q's two negative roots just below -l and -l - 1 for every l, sl's -l + 1 and vl's
  -l -- his four, with his ranges (J2); delta-bar* injective at each, his (2.46a)-(2.46c) reproduced (J3).
- No resonance for 0 < z < 4, sharp (the s0 class root -2 meets 0 there; four dimensions' 3 is the partner root's, not
  sharp), the z = 0 coincidences all at sl (J4); the states exact on Minkowski at every class's largest k, at vl kappa_1
  = 1 + 2 gam_U/(2l + 3) and the rest in closed form (J5); at e_U = 0, on Minkowski, a logarithm forced at mu_l,0's first
  step and none at -l + 1's first two steps (J6).
- Deduced: his Proposition 6.18 (4)-(7) in five dimensions on Tangherlini, each stationary correction one order faster,
  no logarithm in the leading terms; the tensor types carry no pure gauge state; delta-bar* injective at sl and vl for
  every l >= 2, the stationary Killing 1-forms having l <= 1.
- OPEN: the readings of 10.20 line by line; the index sets; whether five dimensions needs his window [-3, 0] (4.36: [-2,
  0] on readings); section 7.2 (4.32's), Proposition 8.11, Lemma 8.12 and Corollary 8.13 in five dimensions beyond
  4.33-4.34's a = 0 and its neighbourhood; section 8.5 (with t2 and t3) and sections 9-10; how small gam_Ups must be,
  and h_0. Labels: computed (puregauge5.py J1-J6, exact); deduced; READ ([Hin26] pp. 19, 67, 113, 117-118, 121, 128-134,
  149-151, 158); nothing proved.

### 4.32 [Hin26] section 7.2 in five dimensions: the constraint operator's dual states (computed; D86)

His section 7.2 records the large zero energy states of the adjoint of the constraint propagation operator, built on the
Killing 1-forms of Minkowski space; their trace-reversed symmetric gradients span the cokernel of the linearized
gauge-fixed Einstein operator in his section 8.4. dual5.py computes the adjoint's indicial roots, the translations' dual
state and the rotations' near a = 0 in five dimensions, four-dimensional Schwarzschild and Kerr the control;
N1STAR-PROOF.md 10.31 states Proposition 10.28 and deduces.

- The adjoint's roots: 2 - conj(lam) for each root lam of box^C of these types (four dimensions his 1 - conj(lam),
  (7.10)); at v1 -1 and 3 + 2 v gam_C, and N*_v1(2) = 3 + 6 gam_C v_C where his N*_v1(1) = 2 + 4 gam_C v_C (p. 143)
  (A1).
- The translations on Tangherlini: the source at rho^4, the correction at rho^2, h*_s1 at rho^3 -- one order faster than
  his (7.15) (A2).
- The rotations at first order in a on Myers-Perry: delta* V_a = -(mu/r^4) a dt (x)_s V', zero for the planes 12 and 34;
  c_0 = -2 mu/(3 (h + 2v)) where his (7.31) has -2M/(h + 2v); h-sharp's leading term at rho^3 with his (7.18)'s ratios
  (A3).
- Deduced: his Lemma 7.2 in five dimensions on 10.21(e)'s readings, the weights (0, C_0 + 2]; his Proposition 7.3 on
  Tangherlini, eleven dual states against his seven, the time translation's and the six rotations' h* rapidly decaying at
  a = 0, the translations' at rho^3; section 7.2.1's structure at first order in a, his (7.18) with m -> mu/2 and rho^2
  -> rho^3, two of the six rotations Killing.
- OPEN: the higher orders in a, Lemma 7.5 and (7.19) on the full Myers-Perry metric (10.36: Lemma 7.5 at every spin
  computed; Proposition 7.4 and (7.19) deduced on readings); Proposition 8.11, Lemma 8.12 and Corollary 8.13 in five
  dimensions beyond 4.33-4.34's a = 0 and its neighbourhood; section 8.5 and sections 9-10; the readings of 10.20-10.22
  line by line; how small gam_Ups must be, and h_0. Labels: computed (dual5.py A1-A3, exact); deduced; READ ([Hin26] pp.
  126, 134-144); nothing proved.

### 4.33 [Hin26] Lemma 8.12 and Proposition 8.11 in five dimensions: the zero energy pairings (computed; D88, D89)

His Proposition 8.11 counts the zero energy kernel of the linearized gauge-fixed Einstein operator -- the gauged
linearized Kerr metrics and the translations' deformation tensors -- and its cokernel, section 7.2's dual states, by the
pairings of his Lemma 8.12, which his proof reduces ([Hin24b] Lemma 3.17, [Hin23b] Theorem 9.6) to boundary pairings at
infinity on the leading terms. pairing5.py computes them on Minkowski, his four-dimensional table the control;
N1STAR-PROOF.md 10.32 states Proposition 10.29 and deduces.

- Four dimensions: -8 pi m-dot, -8 pi m (q . a-dot), 4 pi m (q . c), his table exactly (P1).
- Five dimensions: mass -3 pi^2 mu-dot, rotations -2 pi^2 mu on their planes, centres of mass (3 pi^2/2) mu (q . c), the
  cross terms 0 or, the mass and the centres of mass against the rotations, above the critical weight and undetermined
  by the leading terms (P2-P3; each entry classified by its weight before it is computed, D89); the 11 x 11 matrix
  non-degenerate whatever those are (P4); Kerr-Schild, a pure gauge tensor delta*(dG) whose cut-off source is not zero
  and whose 0 against dt is a cancellation of two nonzero sphere integrals, not a parity (D92), and t* = t - r change
  nothing (P5).
- Deduced: -8 pi times the ADM mass and angular momentum and 4 pi M times the centre of mass in both dimensions; his
  Lemma 8.12 in five dimensions at a = 0 for his L_b (his printed values are for 2 L_b, [Hin24b]'s L, and his s0 dual
  state, leading term -dt against [Hin23b]'s dt, reverses the s0 sign), and near it by continuity; his Proposition 8.11
  with dim ker = dim coker >= 11, equality up to [AHW24] Theorem 6.1(2) in five dimensions, which 4.34 deduces at a = 0;
  his Corollary 8.13 with eleven for seven on it.
- OPEN: [AHW24] Theorem 6.1(2) in five dimensions beyond a = 0 (4.34 has it at a = 0); section 8.5 beyond 4.35 and
  sections 9-10; the readings of 10.20-10.22 line by line; how small gam_Ups must be, and h_0. Labels: computed
  (pairing5.py P1-P5, exact); deduced; READ ([Hin26] pp. 125, 138, 145, 154-158; [Hin24b] pp. 13, 33, 38-39, 44, 49-53;
  [Hin23b] pp. 101-110, 116-117); nothing proved.

### 4.34 [AHW24] Theorem 6.1(2) in five dimensions: the stationary solutions on Tangherlini (computed; D90)

His Proposition 8.11's kernel bound takes from [AHW24] Theorem 6.1(2) that every decaying stationary solution of D
Ric(h) = 0, smooth across the horizon, is a linearized Kerr metric plus a pure gauge term, the gauge 1-form one power of
r larger; on Kerr its proof runs through the Teukolsky scalars. On Tangherlini, static, [KI03]'s decomposition reduces
it harmonic by harmonic to ordinary differential equations in r: static5.py computes them at sigma = 0 from D Ric, with
gmodes5.py's reduced operators; N1STAR-PROOF.md 10.33 states Proposition 10.30 and deduces.

- Tensor and vector types, l >= 2: f (f Phi')' = V_T Phi with Phi = r^(3/2) H, and (r^5 y')' = (k_V^2 - 2) r^3 y/f with
  F_t = r y once E_r has forced F_r = 0; energy identities on solutions, exponents l and -(l + 2) at infinity (S1-S2).
- Scalar type, l >= 2: F_tr = 0; in [KI03]'s X, Y the even equations are a flow, [KI03] (2.24b) at sigma = 0, and Z~
  defined by (2.24a) has Z~' = X; Phi solves f (f Phi')' = V_S Phi, det[Phi; Phi'] = r^3/(k^2 mu) up to r^(1/2); X and Y
  smooth at the horizon where F_tr = 0 (S3).
- l <= 1: scalar l = 0 the time rescaling and the mass, vector l = 1 f_t = a r + b r^-3 -- the rigid rotation and the
  rotation, regular in ingoing form -- and scalar l = 1 pure gauge, the stationary gauge algebraic (S4-S6).
- Deduced: [AHW24] Theorem 6.1(2) at a = 0 -- every stationary solution smooth across the horizon and O(r^-eps), 0 < eps
  < 1, is a mass and one of so(4)'s six rotations plus delta* omega, omega smooth there and O(r^(1 - eps)); his
  Proposition 8.11 at Tangherlini with dim ker = dim coker = 11, and his augmented operator invertible there; near
  Tangherlini, on the reading that (8.22)'s kernel dimension is upper semicontinuous in b -- a property of the uniform
  Fredholm estimates his Corollary 8.13's proof invokes, not read line by line; his proof takes the (co)kernel near b_0
  as Proposition 8.11 gives it (p. 157) -- Proposition 8.11 and his Corollary 8.13 (a statement for b near b_0) with
  eleven for seven (D92).
- OPEN: [AHW24] Theorem 6.1(2) on Myers-Perry with a != 0 beyond that reading; the class of (8.22)'s kernel elements in
  five dimensions line by line; omega's continuation inside the horizon (closed: 4.80); section 8.5 beyond 4.35 and
  sections 9-10; the
  readings of 10.20-10.22 line by line; how small gam_Ups must be, and h_0. Labels: computed (static5.py S1-S6, exact);
  deduced; READ ([AHW24] pp. 1, 35, 41; [Hin26] pp. 156-157; [KI03] pp. 4-10, 11, 13-15); nothing proved.

### 4.35 [Hin26] section 8.5 in five dimensions: the physical large zero energy states (computed; D91)

His section 8.5 builds the large zero energy states at the roots that are not pure gauge, sl and vl's -l for l >= 2,
smoothly in the rotation by his Lemma 8.15's pairings. In five dimensions the physical roots are -l at every type, the
tensor type included (4.25). physical5.py computes the stationary equations of 4.34 as Gauss's hypergeometric equation,
their solutions smooth at the horizon and their growth, the roots his Step 4 needs, and the rotation equivariance behind
his Remark 8.10; N1STAR-PROOF.md 10.34 states Proposition 10.31 and deduces.

- The equations: H, y and Y hypergeometric in z = r^2/mu, l symbolic (Y1); the solutions smooth at z = 1 Gauss functions
  of 1 - z, polynomials where the series terminates, growing like r^l with coefficients that never vanish (Y2).
- The roots: -l simple and -l - 1 none at sl, vl, tl, l = 2, 3, at Proposition 10.9's point (Y3).
- The rotations: L_R h_A = h_[A,B]; <[A_V, A_b], A_V'> on so(4) of rank 4 at one spin, kernel the two Killing rotations;
  in three dimensions his triple product (Y4).
- Deduced: his Proposition 8.14 at a = 0 for every l >= 2 and each of the tensor, vector and scalar types, the leading
  terms Y2's, put into the gauge (spanning where -l is simple, computed for l <= 12); his Lemma 8.15 in five dimensions,
  (1) minus section 10.32's centre-of-mass row, (2) -pi^2 mu <[A_V, A_b], A_V'>, 0 at a = 0, his -8 pi m in [Hin24b]'s
  normalization; his Proposition 8.14 near a = 0 for l = 2, 3 by his Steps 0-5, Step 2 modified (the non-Killing s1
  pairings absorbed into V_1), on his Proposition 7.4 in five dimensions on the full metric and on the readings 4.34
  rests on.
- OPEN: the window five dimensions needs, and whether t2, t3 and higher l enter the late-time expansion (4.36: on
  readings, for any iota+ order in (1, 2], t2 at -2 and no l >= 3); Lemma 8.15(1) against the non-Killing rotations at a
  != 0 beyond its lambda-sharp form (4.37 has his Proposition 7.4 at every spin, so the modified Step 2 stands); the
  readings and weights; sections 9-10. Labels: computed (physical5.py Y1-Y4; exact, and numerical at 40 and 50 digits);
  deduced; READ ([Hin26] pp. 25, 140-142, 154-163; [DLMF] 15.8.2, 15.8.8, 15.10.1); nothing proved.

### 4.36 [Hin26]'s window in five dimensions: the large indicial roots the expansion needs (computed; D93, D95)

His window [-3, 0] is set by two numbers: the iota+ order alpha = 1 of the iteration's slowest term, the mass aspect's
t*^-1 (footnote 27), and the K+ order 4 to which the sources must decay, twice the order 2 of the pole of
L-hat_b(sigma)^-1 at 0 (2-admissibility). A root mu then enters at K+ order alpha - mu and its j-th generalized companion
at alpha - mu + j. window5.py lists the roots in [-3, 0] in four and five dimensions, reproduces (9.32) from that
bookkeeping at alpha = 1, and computes the radiative and Coulombic orders of the flat wave operator; N1STAR-PROOF.md
10.35 states Proposition 10.32 and deduces.

- The roots: those of det N_L itself; in four dimensions his Lemma 8.4's in [-3, 0], (9.32)'s set; in five dimensions
  the same with t2's -2 and t3's -3; box^C's roots meet the window only at four-dimensional s0's 0 (W1; D95).
- The bookkeeping: alpha = 1 gives (9.32)'s orders; for alpha in (1, 2] the physical states kept are s2, v2 and t2 at
  -2, without companions; alpha = 2 in full; alpha = 3/2, the window [-5/2, 0], with s2's and s3's class roots just
  below -2 and more class-root companions (W2; D95).
- The orders: the Coulombic order d - 2 separates from the radiative (d - 1)/2 above four dimensions (W3).
- Deduced: for any iota+ order alpha_5 in (1, 2], five dimensions needs s2, v2 and t2 at -2 alone -- not 10.34's l = 3
  states, nor his Step 4; the pole order 2, on a reading, the centre-of-mass chain ended by Proposition 10.29(iii)'s
  pairing; the window [alpha_5 - 4, 0]. Which alpha_5 is a reading: 2, Theorem M(c)'s mass aspect at the Coulombic order
  r^-2, if nothing decays more slowly at iota+; 3/2 + O(gam), conservatively, as his iota+ index sets carry the I+
  (radiative-order) exponents (the forty-fourth verifier; D95, D98).
- OPEN: (5.28) and Proposition 11.16 in five dimensions (4.39: (5.28) at h = 0 computed); [Hin26c] Theorem 11.1
  there; a radiation field's late limit (4.39: zero at iota+ cap I+, on readings); the data class; which alpha_5 (4.39:
  2, on readings); logarithms at the pole; sections 9-10. Labels: computed (window5.py W1-W3; exact, and
  numerical at 50 digits); deduced; READ ([Hin26] pp. 16-18, 27-34, 37, 85, 92-93, 117, 128, 149, 169, 173-177, 199,
  218, 225, 228, 248, 273, 279, 324); nothing proved.

### 4.37 [Hin26] section 7.2.1 in five dimensions at every spin: Lemma 7.5 on the Myers-Perry family (computed; D96)

His Proposition 7.4 needs the deformation tensor of a rotation on Kerr to depend on the rotation only through a(b) x
a(V), linearly and for every vector (Lemma 7.5; footnote 82), and 4.32 had it in five dimensions at first order in one
spin. mp5.py writes the five-dimensional Myers-Perry metric in Kerr-Schild form for every spin matrix A in so(4) at
once, checks it, and computes Lemma 7.5 on it exactly; N1STAR-PROOF.md 10.36 states Proposition 10.33 and deduces.

- The family: (r^2 - A^2)^-1 = M/P by Cayley-Hamilton, k null on Q = 0, [ER08]'s form at block A, Tangherlini at A = 0,
  Ricci-flat exactly at rational points for two spins rotated out of block form, equal spins and one spin; Kerr likewise
  (M1).
- Lemma 7.5 at every spin: Q, P, x^T A^2 M^2 x invariant and M (r I + A) x covariant under so(4), symbolically, so
  delta* V_b = (1/2) L_R g_b = (1/2) D_A g_b([A_b, A_V]) -- checked on the full metric at the exact points (M2).
- The expansion: the leading term (mu/r^4)(dt + dr) (x)_s V(W) does not see the spin, the rest from rho^4 (M3); the
  Killing rotations 6, 4 at a = +-b != 0, 2 otherwise (M4); h-sharp's leading term the same from the Kerr-Schild term as
  from 4.32's, c_0 shifted by the pure gauge mu/3 (M5).
- Deduced: his Lemma 7.5 at every spin with W = [A_b, A_V], -A_(S') for his S' in four dimensions (A is minus the spin;
  D98), h~_b : so(4) -> rho^4 C^oo, and no spin-dependent pure gauge term at leading order in these coordinates; his
  Proposition 7.4 with h-sharp defined on all of so(4), smooth in the spin across the jumps 6, 4, 2, and (7.19) at
  rho^(floor(C_0) + 3) on 10.31(a)'s readings; so 4.35's condition is met and the modified Step 2 stands at every small
  spin, on the reading that route B's g_b is chosen SO(4)-equivariantly.
- OPEN: (7.19) itself and the formal solution beyond leading order, deduced not computed; Ricci-flatness symbolically;
  g_b in coordinates outgoing at infinity with his cut-offs; the readings of 10.31(a); sections 9-10. Labels: computed
  (mp5.py M1-M5; exact); deduced; READ ([Hin26] pp. 65, 126, 140-144, 161; [ER08] pp. 10, 14, 16, 19); nothing proved.

### 4.38 [Hin26] section 9.1 in five dimensions: the pure iota+ resonances (computed; D97)

His model at future timelike infinity has "pure" resonances, solutions with vanishing incoming data whose t*^-lam terms
enter the iota+ index set E_+ ((1.19); Definition 9.6); in five dimensions, without Huygens, they are functions -- his
own example is u_3 = (v/(v + 2))^(3/2) at lam = 3. 4.36 read alpha_5 = 2 on the reading that nothing at iota+ decays
more slowly; a pure resonance at or below 2 would. iota5.py builds the model by type from lin5.py's operators and
computes its pure resonances by a connection determinant; N1STAR-PROOF.md 10.37 states Proposition 10.34 and deduces.

- The model: M0(D) G + s M1(D) G = 0 with M0 = (x - lam) L1, L1 affine, and M1 lin5.py's N itself, the free transport at
  gam = 0 (I1). The connection through z = s/(s + 2), validated on the free wave's 3 + l + k and his u_3 (I2) and, with
  the argument principle and the moment, on box^C at gam_C = 10, where the zeros are exactly 1 + mu + k for det N's
  upper roots mu (I3).
- At the record's point: det N_L's roots with real part in (0, 3/2] are box^C's roots less 1 (s0 1.0000747438, s1
  1.0001201950, none at v1); over l <= 400 box^C's roots in [-100, 5/2] are the Coulomb 2 at l = 0, 1 and roots in (2,
  5/2) at every scalar l, the lowest 2 + 2.93 x 10^-6 at l = 2, none at the vector types (I4). L-bar has a pure
  resonant state at the s0 candidate at gam_C = 10 and 100 (I5), a resonance on the reading of index 0; at 10^6 the
  method fails (exponents near 10^6 need millions of terms and digits to match; D99).
- Deduced: the towers lam -> lam + 1 (d/dt*) and the descent lam -> lam - 1 (the moment int s^-lam G: N(lam - 1) m = 0,
  or the state is d/dt* of one at lam - 1); the injectivity half of his Proposition 9.2(2) below 1 + eps_ind in five
  dimensions as in four, on 10.24-10.25's readings, its index 0 half a reading (D99); hence every pure resonance of
  L-bar with real part below 5/2 sits at a root of box^C's zero energy operator in (2, 5/2) -- of the constraint kind,
  eta != 0 -- and none has real part at most 2: the second channel of alpha_5 is closed on the alpha_5 = 2 reading. On a
  reading (the injectivity along gam_C in [100, 10^6]) the s0 candidate 2.0000747 is a resonance at the record's point,
  by Hurwitz.
- OPEN: the candidates at the record's point by computation (their WKB form, or gam_C -> oo); s1's and l >= 2's (s1
  unresolved at 100 digits); the readings of the injectivity, of the index 0 half (his pp. 167-168) and of the path;
  whether his section 12 excites the constraint-kind states; four dimensions. Labels: computed (iota5.py I1-I5; exact,
  and numerical at 30-100 digits); deduced; READ ([Hin26] pp. 16-17, 149, 164-169, 170, 172, 180, 184-185); nothing
  proved.

### 4.39 [Hin26] (5.27)-(5.28) and Proposition 5.14 in five dimensions; the radiative order at iota+ (computed; D100)

His Proposition 5.11 writes the linearized gauge-fixed operator at future null infinity as (2 r^-1 d_0 r + r^-1 A_h)
d_1 + r^-1 B_h in a seven-part splitting, A_h lower triangular: its eigenvalues set the decay of each component, and
its (7, 4) and (7, 6) entries couple pi_01 and pi-slash_0 into the 11-component (Proposition 5.14), the second footnote
27's mass-aspect coupling. 4.36 left alpha_5 between 2 and 3/2 + O(gam) for want of a five-dimensional (5.28), and 4.38
closed only the pure resonance channel. scri5.py writes it at h = 0 in his splitting, gives the exponents by type, and
tests the radiative exponents at iota+; N1STAR-PROOF.md 10.38 states Proposition 10.35 and deduces.

- The matrix: A_0, sbar5.py's S-bar in the splitting with S^3, lower triangular, the same at two points, with his
  diagonal, his (5, 2) and his (7, 4) entry 2 (1 - e_Ups) gam_Ups, and four trace couplings changed ((3, 1), (4, 1), (4,
  3), (7, 3); with his (1/2) tr-slash for the trace slot, (4, 1) and (4, 3) alone); in four dimensions his printed
  (5.28) at h = 0, all 49 entries (C1).
- The exponents: iota5.py's det L1 by type is the product of 3/2 + (A_0)_ii - x over the slots the type occupies -- s0
  1, 3, 4, 7; v1 2, 5; v2 2, 5, 6; t2 6 (C2).
- At a radiative exponent: at s0, pi_01's and pi_11's, and at t2, 3/2, at gam_C = 10 and 100, no resonant state at
  iota+, the determinant continuous through the exponent (C3).
- Deduced: the perturbation's entries of A_h and B_h fall half an order in five dimensions (a scaling argument), so the
  (7, 6) coupling and the quadratic sources reach the 11-component at the Coulombic 2, the mass aspect's; the (7, 4)
  entry carries pi_01's radiative exponent into pi_11; a radiative term reaches iota+ at its own order only through a
  resonant state there, which 10.37's descent -- holding at an outgoing exponent under his (9.17), D99 -- and
  injectivity exclude below 2. So alpha_5 = 2 by both channels, on readings, and the window is [-2, 0].
- OPEN: the perturbation's entries by computation; Proposition 11.16 in five dimensions; 10.37(c)'s index 0 half,
  polyhomogeneity at iota+ cap I+, the data class, the decay lam_1 > 0 and nothing below 2 fed from K+; the radiative
  exponents at the record's gam_C; four dimensions. Labels: computed (scri5.py C1-C3; exact, and numerical at 50-100
  digits); deduced; READ ([Hin26] pp. 85, 87, 92-93, 96-98, 146, 168-169, 223); nothing proved.

### 4.40 [Hin26] section 10.1 in five dimensions: the augmented zero energy operator (computed; D102)

His Theorem 10.1, 2-admissibility, rests near zero energy on augmenting L-hat_b(sigma) by the eleven-dimensional -- in
four dimensions seven -- nullspace of L-hat_b(0). His naive augmentation (10.5) has entries [L_b, t*] g-dot and [L_b,
t*] h-breve^1 + (1/2)[[L_b, t*], t*] h_s1 that decay only like r^-2 ((10.9)), outside the target space, so he builds
improved states with t*^-1 and log t* terms (Lemma 10.3) and, on the spectral side, sigma log |sigma| corrections
(section 10.1.3); his angular momenta alone, already O(r^-2), take chi_K g-dot ((10.24a)). aug5.py computes the
mechanism on the model; N1STAR-PROOF.md 10.39 states Proposition 10.36 and deduces.

- The states: the gauged mass state r^-2 (dt^2 + dr^2) plus delta*(r^-1 (a dt + b dr)) and rotation state 2 r^-4 dt
  (x)_s w plus delta*(p r^-3 w) solve L-bar g-dot = 0 with no logarithm; in four dimensions the mass state's gauge
  1-form needs his (8.19)'s log (A1).
- The entries: [L-bar, T] g-dot is of degree -3 (mass) and -4 (rotation), nonzero, [[L-bar, T], T] g-dot = 0; four
  dimensions -2 and -3, his (10.9a) and (3, 0) (A2). The cut-off states chi(r/T) g-dot: iota+ order 4 and 5 (the boosts'
  deduced); four dimensions 3, his borderline, and 4 (A3).
- Deduced: every five-dimensional entry of (10.5) is in A^3, inside the target space for alpha_sf + 2 < 1; his (10.24a)
  serves every state, no improved states, no t*^-1 or log t* and no sigma log |sigma| in the augmentation; his
  Proposition 10.6 from 10.32's pairings; his Proposition 10.7 and Theorem 10.1, 2-admissibility with alpha_sf + 2 in
  (0, eps_ind), on the readings of 10.19-10.20 ([Hin26c] at n = 4, with its Theorem 12.2's proof and section 14.1),
  10.24-10.27 and 10.32-10.33.
- OPEN: his Proposition 10.7 and section 10.2 line by line in five dimensions; the boost entry and g^00 on Tangherlini
  and Myers-Perry by computation; whether L-tilde_b(sigma)^-1 has logarithms at 0, and whether the I+ asymptotics his
  Lemma 10.3 supplies are needed (his section 11). Labels: computed (aug5.py A1-A3; exact); deduced; READ ([Hin26] pp.
  145, 199-205, 207-209, 211-212, 214); nothing proved.

### 4.41 [Hin26] section 10.2 in five dimensions: 2-admissibility with no sf-loss (computed; D104, D105)

His Theorem 10.1 asks, for f in H^((s;k),(alpha_sf+2,0)), the forward solution u in H^((s-1;k),(alpha_sf-delta,-2)), and
his proof (section 10.2) loses delta > alpha_sf + 3/2 at spatial infinity, from the singular part of u alone: Lemma
10.12 puts d_t* g-dot at -1/2 - eps and d_t*^2 h_s1 at 1/2 - eps -- the tf weights of the r^-1 and r^-2 tails of his
states, and the scf weight -1/2 of their I+ order 1, through (2.25a), the requirement at R_out and Lemma 2.20 -- and
Lemma 10.13 integrates twice in t*. lowfreq5.py computes the two steps that carry the dimension; N1STAR-PROOF.md 10.40
states Proposition 10.37 and deduces.

- The columns at zero frequency: d_T(chi(r/T) g-dot) integrates over T to g-dot and d_T^2 of the h_s1 column to h_s1, so
  their zero-frequency values are the states; the mass state, of degree -2, and h_s1 one order faster give the weights 0
  and 1 in five dimensions, his -1/2 and 1/2 in four (W1).
- The weights: in five dimensions, the columns having no I+ term, d_t* g-dot at -eps and d_t*^2 h_s1 at 1 - eps, the
  states' own weights -- the requirement at R_out does not bind -- and u_sing at alpha_sf after Lemma 10.13 twice, the
  initial weights setting the bound, so no loss; with I+ terms at the radiative order 3/2, a loss of eps; in four his
  -1/2 - eps, 1/2 - eps, -3/2 - eps and his loss (W2; 598 rational points).
- Deduced: his Theorem 10.1 in five dimensions with no sf-loss (every delta >= 0, or every delta > 0 if [Hin26c]
  Definition 5.13 asks it), on the readings of 10.39 and of his Lemmas 10.9-10.11 and 10.13; his (10.52) as printed, at
  s' = s, would need s < -1 + eps at R_out, which Remark 10.2 does not give, but his proof uses it only at s - 1, where
  it holds. D104 took the requirement at R_out as his four-dimensional -1/2 and found it binding; D105 reads it from
  (2.25a).
- OPEN: [Hin26c] Definition 5.13's delta; [Hin26c] Lemmas 3.9 and 14.6, (13.30a) and Theorem 12.2 at n = 4; his Lemma
  10.9 line by line in five dimensions; the boosts' columns on Tangherlini by computation; his section 11 (Corollary
  11.10, Theorem 11.12). Labels: computed (lowfreq5.py W1-W2; exact); deduced; READ ([Hin26] pp. 21, 54-55, 60, 199-201,
  206, 212-217, 225); nothing proved.

### 4.42 [Hin26c]'s readings behind 10.40, at source (computed; D106)

Section 10.40 rested on [Hin26c] at n = 4 for Definition 5.13's delta, (13.30a), Lemmas 14.6 and 3.9, and the
Paley-Wiener argument and section 14.1 that [Hin26]'s proof of Theorem 10.1 follows. [Hin26c] is written on Kerr in 3 +
1 dimensions, so each is READ at n = 3; N1STAR-PROOF.md 10.41 records where n enters each and states Proposition 10.38.

- Definition 5.13 admits delta >= 0 (p. 106), and its Remark 5.14, with margin d and loss s - d, is the form of
  [Hin26]'s (10.3): on the readings of 10.40, 2-admissibility in five dimensions with sf-loss 0, the hedge on delta
  removed.
- (13.30a) sees n through the density, its shift 3/2 "due to the passage from mu to mu_b" (p. 255): at n = 4 the shift
  is 2, and the rule reproduces his printed instances on pp. 206 and 216 and at (10.59) (W3).
- Lemma 14.6 at s = 0 is in t at each fixed r, so it holds at every n; general s rests on the 3b-calculus. The
  Paley-Wiener argument (p. 235) is in t* alone. In section 14.1, the template, the loss comes from the zero energy
  state's decay through (14.16).
- OPEN: [Hin26c] Lemma 3.9, the microlocal part of Lemma 13.13, the 3b-calculus (his scaled bounded geometry paper, not
  read) and Theorems 9.5, 9.16 and 9.41 at n = 4; his section 11. Labels: computed (lowfreq5.py W3; exact); deduced;
  READ ([Hin26c] pp. 8, 20-21, 56-59, 106-107, 233, 235, 252, 255, 262-267); nothing proved.

### 4.43 [Hin26] section 11.1 in five dimensions: admissibility and forward solutions (computed; D108)

His section 11 begins by making the main result of [Hin26c] available: the dynamical linearized operator is admissible
relative to L_b (Corollary 11.10), and forward solutions lose two orders at iota+ plus his sf-loss delta (Theorem
11.12). cone5.py computes the inputs that carry the dimension; N1STAR-PROOF.md 10.42 states Proposition 10.39 and
deduces.

- The densities: the unweighted b-density shifts the weights by (n/2, (n+1)/2, 1/2), his (3/2, 2, 1/2) and (2, 5/2, 1/2)
  in five dimensions; beta_+ in (1/2, 1/2 + eps_ind) in both; the top of beta_I 3/2 for his 1, on the reading of
  [Hin26c] (10.2) at n = 4, the radiation field's I+ order computed (C1).
- The background differences at iota+ -- mass, rotation, boost -- of orders 2, 3, 2 for his 1, 2, 1, and the cut-off
  mass interpolation's curvature of order 4 for his 3 (C2-C3), the patched background's, with rotation and boost,
  deduced (10.42(c)).
- Deduced, on readings: E+ with (2, 0) in E+ and min Re E+ >= 2 (with 10.38's alpha_5 = 2); Corollary 11.9's P(g0, g0)
  in rho_+^4 C^oo; Corollary 11.10 with l_+ in (0, 1), sf-loss 0; Theorem 11.12 with delta = 0, beta_I in (beta_+, 3/2):
  u in H^(k, beta_I, beta_+, -3/2)_b.
- OPEN: [Hin26c] Theorem 11.1 and Definitions 5.15 and 5.18 at n = 4; the h-terms of (5.28) and Proposition 11.16 in
  five dimensions; E^C_I, gam_Ups and l_I at I+; his sections 11.2-11.8. Labels: computed (cone5.py C1-C3; exact);
  deduced; READ ([Hin26] pp. 218-226, 231, 244, 263; [Hin26c] pp. 107, 109, 201, 228); nothing proved.

### 4.44 The remaining route: what finishing the nonlinear work takes (plan; D110)

M's direction of 2026-10-24: the nonlinear work is to be finished first and then built fully into the paper (LOG D110).
What remains is READ from [Hin26]'s contents and section openings (alphaXiv, 2026-10-24; printed pp. iv, 218-219, 226,
263, 295, 318-321): section 11.2, "Asymptotics and formal solutions at I+" (Propositions 11.14-11.16); sections
11.3-11.8, six steps from "almost linear bounds" to "final gauge modifications; iota+- and K+-expansions,
t*^(-4-eps_K)-remainder" (Propositions 11.17, 11.20, 11.32, 11.34, 11.51, Theorem 11.59, Corollary 11.66); section 12,
"Efficient parameterization of metric perturbations" (Theorems 12.3, 12.8); and section 13, where "the global nonlinear
stability ... can be proved by concatenating the exterior stability result (Theorem 5.23) with a Nash-Moser iteration
based on Theorem 12.8" (p. 318), [SR89]'s scheme (p. 321). His section 5's Theorems 5.21 and 5.23 are not carried
either.

*The class.* What settling needs is stability within the T^2-mirror class (paper, section 8). The class carries no
vector type and no scalar l = 1 (settle5.py T1; Proposition 10.1), so the states Hintz's steps remove -- the boost (his
Step 2), the rotations, the centre-of-mass motions (Steps 4-5) -- should be absent and the final parameter the mass
alone. That is the first step to compute and deduce (the equivariance of his forward map, augmentation and gauge
modifications, and which states of 10.28-10.37 are invariant), not an assumption.

*Phase A, his argument completed in five dimensions in the class, on the readings already named:*

- A1 the class reduction: invariant zero energy, generalized, pure gauge and dual states; which of Steps 1-6 survive.
- A2 section 11.2: Propositions 11.14-11.16, with E^C_I, gam_Ups and l_I at I+ and the h-terms of (5.28) (the OPEN items
  of 10.38 and 10.42).
- A3 section 11.3, Step 1 (Proposition 11.17); A4 sections 11.4-11.5, Step 2 as A1 leaves it and Step 3 (Proposition
  11.32); A5 section 11.6, Step 4, the mass change (Proposition 11.34); A6 sections 11.7-11.8, Steps 5-6 (Theorem 11.59,
  Corollary 11.66).
- A7 section 12 in the class (Theorems 12.3, 12.8); A8 section 5's Theorems 5.21 and 5.23 in five dimensions, the data's
  orders at spatial and null infinity; A9 section 13: his Theorem 13.1 in five dimensions in the class by [SR89]'s
  iteration, READ.

*Phase B, the readings discharged, each by a line-by-line check at n = 4 or by computation:*

- B1 [Hin26c] section 9 on bundles (10.19); B2 its zero and low energy theorems at n = 4 (10.20, 10.41); B3 its Theorem
  11.1 and Definitions 5.15, 5.18 at n = 4 (10.42).
- B4 [Hin26a] Theorems 5.2 (the 3b-analysis), 6.2 and B.1 in five dimensions (10.21-10.23).
- B5 h_0 at the parameter point, or the conditions on a range of parameters; B6 the horizon threshold of 10.21; B7 the
  kernel class and the uniqueness inside the horizon of 10.27; B8 10.24's roots beyond l = 12; B9 the transfers from the
  Minkowski model (10.12, 10.39-10.42). Items of 10.31-10.36 that A1 removes are recorded as removed.

*Phase C, the global step:*

- C1 the solutions of Theorems 1-2 on a region containing a Cauchy surface of the exterior after the shell; C2 their
  data there in A8's spaces, small with lambda; C3 the conclusion, settling of g_lambda to Tangherlini of a nearby mass
  in the class for lambda <= lambda_1.

*Phase D:* the paper, built from the finished work, one verifier on the whole, the PDF. Every step as before: computed,
deduced or READ, one verifier at a time. Scale: Phase A covers about 110 printed pages of [Hin26]; Phase B is the
largest, [Hin26c] running to about 280; Phase C two or three steps.

### 4.45 A1: the class in [Hin26]'s construction (computed; D111)

ROUTES 4.44's first step. class5.py computes which of Hintz's generators and harmonic types are invariant under G = O(2)
x O(2); N1STAR-PROOF.md 10.43 states Proposition 10.40 and deduces.

- Computed (C1-C3): of the fifteen Killing fields of 4+1 Minkowski only d_t is G-invariant (T^2 alone: d_t and the two
  plane rotations); the mass change is invariant; one invariant scalar harmonic of S^3 at each even l and one invariant
  transverse traceless tensor harmonic at each even l >= 2, none at odd l, and no invariant divergence-free 1-form (l <=
  8); C3 bounds the counts from above by a second method, so they are exact (D115).
- Deduced: P and its linearizations commute with G (the damping 1-form and c_H radial); the final parameters are (m, 0);
  the boost S, the centre-of-mass shift and every S_1 and V_l component vanish; his Steps 2 and 5 reduce to Propositions
  11.20 and 11.51 with no S_1 terms and no modifications (D115), and Step 4 is the mass change alone; of the kernel and
  dual states only the mass's and the time translation's remain, of the physical states at l = 2 the scalar and the
  tensor ones; and the Nash-Moser iteration runs on the G-fixed subspaces, on the reading that his read-off in Theorem
  12.8's proof commutes with G (checked at A7).
- Next: A2, his section 11.2 in five dimensions (Propositions 11.14-11.16), on 10.38's (5.28).

### 4.46 A2: [Hin26] section 11.2 in five dimensions (computed; D112)

iplus5.py computes the I+ normal operator's structure in five dimensions; N1STAR-PROOF.md 10.44 states Proposition 10.41
and deduces his Lemma 11.15 and Propositions 11.14 and 11.16.

- Computed (P1-P3): the leading part -(rho_I d - 3/2)(rho_I d - rho_+ d), his with 3/2 for 1; A_0's exponents 3/2 + his
  diagonal; the 11-component's exceptional exponents 2 (from 10.38(a)'s scaling, a reading) and 3/2 + (1 - e_Ups)
  gam_Ups (his 1 and 1 + (1 - e_Ups) gam_Ups reproduced from his matrix); the Steps' coefficients nonzero for gam_Ups !=
  1/4, with the full A_0 (D121); the gap 3/2 + 2 gam_Ups < Re z < 3/2 + (1 - e_C)(1 - v) gam_C, at the point (38/25,
  499996.6171875).
- Deduced: the five-dimensional index sets at I+ (Definition 5.3 and (5.5)-(5.8) with 3/2 for 1 and E_I,11's (2, 0));
  Lemma 11.15 with min(alpha_I, 3/2, l_+), Proposition 11.14 as stated, Proposition 11.16 with E^#(1)_+ = E-breve_+ u
  {(2, 0)} u {(3/2 + (1 - e_Ups) gam_Ups, 0)}; and E_+ with min Re 3/2 + (1 - e_Ups) gam_Ups, which keeps 10.42's
  conclusions without 10.38's readings.
- OPEN: the weights l_I for the iteration (A3); 10.38(a)'s scaling argument; Definition 5.3's closure with section 5
  (A8). Next: A3, his section 11.3 (Step 1, Proposition 11.17).

### 4.47 A3-A5: [Hin26] sections 11.3-11.6 in the class (deduced; D113)

N1STAR-PROOF.md 10.45 deduces his Steps 1-4 in the class as one statement.

- Deduced: S-hat_1 = 0 at every frequency in the class, so u_lo = u_reg + g-dot and one integration of d_t* suffices
  (his footnote 116's case from the start); Step 2 reduces to Proposition 11.20 with S-dot = 0 (D115); u = chi_K
  g-dot^Ups_b(m-dot) + u~, with u~ of K+ order alpha_K - 1, on f of K+ order alpha_K in (1, 1 + eps_K) where his needs
  (2, 2 + eps_K); m-dot is removed by the final mass (his Lemma 11.45 at (0, m_0)); f's iota+ requirement is 3 + min Re
  E_+ - eps = 9/2 + (1 - e_Ups) gam_Ups - eps against his 4 - eps (D121).
- OPEN: the weight l_I at I+ (A6); [Hin26c] Proposition 13.18 and Corollary 13.17 at n = 4 (Phase B). Next: A6, his
  sections 11.7-11.8 (Theorem 11.59, Corollary 11.66) in the class.

### 4.48 A6: [Hin26] sections 11.7-11.8 in the class (computed and deduced; D114)

sharp5.py computes the class's late-time bookkeeping in five dimensions; N1STAR-PROOF.md 10.46 states Proposition 10.42
and deduces Proposition 11.51, Theorem 11.59 and Corollary 11.66 in the class.

- Computed (K1-K4): the class's types (scalar at even l, tensor at even l >= 2) and their roots in [-3, 0]; for every
  iota+ exponent from 3/2 + (1 - e_Ups) gam_Ups to 3, the eliminated pure gauge terms within s0 e0, s0 c0 and s2 e0, the
  recorded ones within these and s2 c-1, and no physical state; his eight parameters and his s2, v2, s3, v3 reproduced
  in four dimensions; his weights 3 + eps_I and 3 + eps_+ serve.
- Deduced: Proposition 11.51 with the mass alone; Theorem 11.59 with u_exp the mass change plus four pure gauge terms
  and u~ of K+ order 3 + eps_K, sources needing 3 + eps_K and h the same; Corollary 11.66 with q-vec the mass and those
  four.
- OPEN: Lemma 11.57's linearizations in five dimensions (Phase B); the readings of 10.39-10.45. Next: A7, his section 12
  in the class (Theorems 12.3 and 12.8).

### 4.49 A7: [Hin26] section 12 in the class (deduced; D116)

N1STAR-PROOF.md 10.47 deduces his Theorems 12.3 and 12.8 in the class.

- Deduced: the data U = (m - m_0, the G-fixed iota+ data, m_rem, h-tilde); his gauge remainders at 3 + eps_+ fall into
  h-tilde; Phi commutes with O(4) on all of D^oo, every step of its construction being canonical; P(Phi(U)) of K+ order
  3 + eps_K; Theorem 12.8's U' G-invariant, which discharges 10.43(e)'s reading.
- OPEN: the five-dimensional iota+ spectrum between 5/2 and 3 + eps_+; section 9's propositions in five dimensions
  (Phase B). Next: A8, his section 5's Theorems 5.21 and 5.23 in five dimensions.

### 4.50 A8: [Hin26] section 5 in five dimensions, in the class (deduced; D117)

N1STAR-PROOF.md 10.48 deduces his Theorems 5.17, 5.21 and 5.23 in five dimensions in the class.

- Deduced: every I+ exponent is at least 3/2, so Theorem 5.17's iteration carries no radiation-field term for 1 <
  l-flat_I < 3/2; Theorem 5.21's hypothesis becomes min Re E_0 > 3/2 + 2 gam_Ups, which a mass change (r^-2) meets
  exactly when gam_Ups < 1/4; in the class only S = 0 is used, h_0 = h, G-invariant by uniqueness.
- OPEN: [Hin23a]'s energy estimates at n = 4, added to Phase B as B10; section 5.7's gauged data (A9); the record's data
  near I0 (C2).

### 4.51 A9: [Hin26] Theorem 13.1 in five dimensions, in the class; Phase A complete on its readings (deduced; D117,
D126)

N1STAR-PROOF.md 10.49 states his Theorem 13.1 in five dimensions in the T^2-mirror class -- G-invariant data near
five-dimensional Tangherlini of mass m_0, partially polyhomogeneous with min Re E_0 > 3/2 + 2 gam_Ups, settle to
Tangherlini of a nearby mass m at t*^(-2-eps_K) in spatially compact sets -- deduced from 10.13-10.48.

- Deduced: his Steps 1-4 in the class: the parameters (10.14-10.25), the gauged data (Proposition 5.25, a reading), the
  exterior solution at S = 0 (10.48), [SR89]'s four assumptions from 10.47, the gauge and Ricci flatness by the Bianchi
  identity; the weakest K+ term the mass remainder's, at his order 2 + eps_K.
- Phase A of 4.44 is complete conditional on its readings -- B1-B4, B10 and 10.45(e)'s [Hin26c] Proposition 13.18 and
  Corollary 13.17 at n = 4 (D126). Phase B now has ten items: B1-B9 as listed in 4.44 and B10, [Hin23a]'s exterior
  estimates at n = 4 (10.48(c)); with them the iota+ spectrum between 5/2 and 3 + eps_+ (10.47(b)) and section 9's
  propositions in five dimensions (10.47's OPEN). Phase C applies 10.49 to the record's solution; C2 decides whether its
  data lie in 10.49's hypotheses (compact support near I0 would make 10.48's Step 1 empty).
- Next: Phase B, the readings discharged, starting with those the class leans on most -- B9's transfers and B2/B3's
  [Hin26c] theorems at n = 4.

### 4.52 Phase C: the record's solution in 10.49's hypotheses (deduced; D118)

N1STAR-PROOF.md 10.50 deduces C1-C3 from the record's own sections 1, 5 and 6, with three readings.

- Deduced: every oscillating profile vanishes on {v > v_end} (Lemmas 5.3 and 6.2 by induction; env = 0 there), so after
  the shell the approximant is Tangherlini(mu_end) plus smooth O(lam) means; a tau1-slice in (v_end - a, tau_end] lies
  there; beyond Omega the data are glued, G-equivariantly, to exact Tangherlini of a mass m = mu_end + O(lam), the
  obstruction being the one G-invariant Killing datum; the slice's data are then a compactly supported O(lam)
  perturbation of Tangherlini(m) in H^d, so 10.49 applies for lam small: the development settles in the class to
  Tangherlini of a nearby mass at t*^(-2-eps_K).
- Readings added: Theorem E at every order k >= d (C-i); equivariant gluing in five dimensions (C-ii); finite-time
  Cauchy stability (C-iii).
- Next: Phase B, with C-i (the record's own bootstrap at higher order) among its first items.

### 4.53 Phase B begun: C-i discharged; the companion papers audited for their dimension (D119)

- Discharged (10.51, deduced from the record's sections 4-6): Theorem E at every order k >= 6 with K >= 6 -- k = 6 is
  Step 4's floor (its L^inf range, i + 3 <= k + 1 for i <= 4; [DS23] asks only k > 3; D126), the bootstrap's closing
  condition K >= 6 does not see k -- with (E3) from Theorem A and (E4) from Proposition 6.5, which bounds the data's
  correction at every order.
- Done: the dimension audits of [Hin26c] (B1-B3) and of [Hin26a] and [Hin23a] (B4, B10) reported (4.55); their findings
  are claims to be checked at source before anything is discharged on them.

### 4.54 B8: 10.24's roots for every l (computed; D120)

- Computed (eind5.py E1-E2; N1STAR-PROOF.md 10.52, Proposition 10.43): every scalar, vector and tensor root of L simple
  for every l >= 2, exact (discriminants isolated between integers, Sturm); (8.13) for every l, by an exact certificate
  beyond l* = 10^4 for box^C's upper scalar and vector roots and a 30-digit scan below; eps_ind at most 1.94137 x 10^-8,
  box^Ups's root near 1 - l at l = 50, the edge of (8.13)'s |lam| <= 50.
- Deduced: [Hin26] Lemma 8.4 in five dimensions at the point for every l. B8 discharged.

### 4.55 The companion papers' dimension: the plan for B1-B4 and B10 (READ by two readers; D122)

- Reported, to be checked at source: [Hin26c] works in 3 + 1 "for concreteness" (Remark 5.6, printed p. 101), general
  dimension in [Hin23c] section 3.1.2, and states some results for general n (Corollary 9.39, Proposition 9.40);
  [Hin26a] is 3 + 1 by choice (p. 3, footnote 1: "we do not strive for any generality here"; p. 25, "dim M = 4") on
  calculi stated for general dimension ([Hin23d], [Hin26d] section 3, its own Lemma 5.14 and Corollary 5.15); [Hin23a]
  (arXiv:2302.13804v1) is 3 + 1 on a general calculus (section 3.1, p. 9; Lemma 3.33 on R^n, applied "with n = 4").
  [Hin26a] has no Theorem 7.1: [Hin26] Theorem 7.1 (printed p. 136) summarizes it; 10.49(a)'s label corrected.
- By citation: [Hin26c] Theorem 9.38, Corollary 9.39, Proposition 9.40, (9.37), (9.114)-(9.117), Corollary 9.39's -n +
  2 + beta (Definition 5.10 has -1 + beta; D126), section 13.1.2, Lemma 14.6 (via [Hin23d]) and Paley-Wiener; the
  general-dimension calculi above; the flat roots {-l, l + n - 2}; the harmonic split on S^(n-1) [KI03]; [SR89].
- By short argument at n = 4: [Hin26c] section 3's lemmas, Definition 5.13, Theorem 9.5(5), Theorems 9.36 and 9.41,
  Corollary 9.43, Lemma 14.5, section 13.2, (11.5) and (5.7); the trace weight 2/(D - 2) for [Hin26a] (3.2)'s weight 1,
  the record's own derivation (damping5.py U2; D126); [Hin26a] Theorems 5.2, 6.2 and B.1 and [Hin26] Theorem 7.1(1)-(4)
  at the record's point from its computed inputs (10.12-10.23); [Hin23a] Propositions 3.17, 3.29 and 3.32 at n = 4 and
  Corollary 3.36 with its new loss; Theorem 3.35 (peeling the radiation field) not needed in five dimensions, where no
  radiation field is carried (10.48(a); [Hin26] p. 102's first step).
- Real work: [Hin26c] Theorem 10.1 (sections 10.1-10.3), Theorem 11.1, whose proof rests on Theorem 8.14 (sections 6-8),
  and section 9's scalar to bundle step at n = 4; a five-dimensional [Hin26a] Theorem 4.9 for every small h (its
  Appendix A with S^3's harmonics), or the route of its Remarks 4.10 and 6.3 (Re lam >= 2 - eps suffices for (1.43)'s
  strip [-C_0, 1) in five dimensions); h_0 and the horizon threshold (B5, B6); the five-dimensional nonlinear error
  class (the analogue of [Hin23a] Corollary 3.31).
- Next: the citation items checked at source and recorded; then the short arguments, one section each; then the real
  work.

### 4.56 B1-B2: [Hin26c] section 9 at n = 4, at source (READ and deduced; D123)

- READ (N1STAR-PROOF.md 10.53): section 9 is set in general dimension (Definitions 9.3-9.4, "X an open n-dimensional
  manifold"; Remark 9.1, "some detail (and generality)"), and Theorem 9.38, Corollary 9.39 and Proposition 9.40
  ("Suppose the spatial dimension satisfies n >= 3 ... tensor wave operator ... tf-admissible with all weights beta in
  (0, n - 2)") carry n; Theorems 9.36 and 9.41, Corollary 9.43, Definition 5.13(2), Theorems 10.1 and 11.1 are written
  with n = 3's numerals; bundles are "purely notational" (p. 158).
- Deduced: the n = 3 numerals all come from the b-density (Lemma 3.11's <x>^3), so at n = 4 they read alpha + 2 for
  alpha + 3/2, the record's substitutions; Theorem 9.5(5)'s kernel class at n = 4 is A^(3/2 + S-bar - eps). B1 and B2
  discharged at source but for Theorem 9.16's proof at n = 4 (sections 9.3.1-9.3.5, on Proposition 4.24's dynamics,
  which 10.17-10.18 supply), left a reading.
- READ for B5 ([Hin26a], 2026-10-24): his own h_0 is not explicit. Theorem 4.9 (p. 37): "there exists e_0 ... such that
  for all e in (0, e_0), there exists h_0 > 0 such that for all h in (0, h_0)"; Theorem 6.2 (p. 67) likewise; Remark
  6.3: "Only a calculation of the indicial roots, as performed in Theorem 4.9, allows one to get invertibility ... for
  some fixed positive h in the full stated range of weights." So the five-dimensional statement is for every
  sufficiently small h at a fixed small e, and B5 becomes: each property the record computes at h = 10^-6 is to hold for
  every h in (0, h_1], h_1 explicit, at the record's e_C; then any h below min(h_0, h_1) serves.

### 4.57 B5-B6: every small h, not one point (computed and deduced; D124)

- Computed (uniform5.py H1-H2; N1STAR-PROOF.md 10.54, Proposition 10.44): at (v, e) = (1/2, 1/102400), for every h in
  (0, 10^-6], box^C's roots avoid [-100, 2] at every type and l but for the simple Coulomb root 2 at l = 0, 1, with
  10.12's counts -- damping5.py U4's certificate with h as a second parameter, exact.
- Deduced: [Hin26a] Theorem 4.9 in five dimensions for every h <= 10^-6 at the record's e; every conclusion the record
  drew from the point holds for every such h (10.21, 10.24, 10.35, 10.37, 10.46), or is free of h or improves as h falls
  (10.13, 10.23, 10.26, 10.31, 10.38, 10.44), or holds off a countable set of h (simplicity; (8.13)); the horizon
  threshold holds for every h below an uncomputed h_2 (his Remark 5.7's mechanism). So any h below min(10^-6, h_0, h_2)
  off a countable set serves, and the condition "10^-6 < h_0" is gone. B5 discharged; B6 deduced.
- Remaining in Phase B: B3 ([Hin26c] Theorem 11.1 and Definitions 5.15, 5.18 at n = 4; Theorem 9.16's proof at n = 4),
  B4 ([Hin26a] section 5.2 and Theorems 6.2 and B.1 line by line at n = 4), B7 (10.27's kernel class and uniqueness
  inside the horizon), B9 (the transfers from the Minkowski model), B10 ([Hin23a] in five dimensions), C-ii, the iota+
  spectrum between 5/2 and 3 + eps_+, (2.27) at n = 4, 10.38(a)'s scaling.

### 4.58 B4, B7, B9, B10 (computed, READ and deduced; D125)

- B9 discharged (transfer5.py T1-T2; N1STAR-PROOF.md 10.55, Proposition 10.45): Tangherlini in Kerr-Schild form, g =
  eta + (mu/r^2) k (x) k, exact; its connection two orders below Minkowski's, so every operator differs from its
  Minkowski model in rho^4 Diff^2_b and the indicial families, tf-normal operators and S-bar are the model's; g^00 = -4
  mu rho^2.
- B7 deduced (10.55(b)-(c)): the kernel class from 10.53(c); the interior uniqueness by the radial systems' regular
  singular point at the horizon (its last step proved as Lemma 10.56 (c): 4.80); the index 0 at nonzero frequency on
  Theorem 9.16's reading (10.53(e)).
- B4 deduced at source (10.56): [Hin26a] section 5.2's estimates take from the metric and c only symbol data, all
  computed in five dimensions (10.13, 10.14, 10.22), on a general calculus; one reading left, the sign of each
  commutator there as the five-dimensional symbol gives it. Theorems 6.2 and B.1 follow with 10.54(a).
- B10 deduced at source (10.57): for the record's compactly supported data [Hin23a] is needed only near a piece of I+;
  at n = 4 its A_g is 10.38's A_0 (the radiation couplings drop to the error at r^-(3/2)), its Theorem 3.35 is not
  needed, and [SR89] applies with a finite loss; the order count of (b) and the gain of (c) read, not computed.
- Remaining: B3 ([Hin26c] Theorems 10.1 and 11.1, Definitions 5.15 and 5.18, and Theorem 9.16's proof, at n = 4),
  10.45(e)'s [Hin26c] Proposition 13.18 and Corollary 13.17 at n = 4, C-ii, the iota+ spectrum between 5/2 and 3 +
  eps_+, (2.27) at n = 4, 10.38(a)'s scaling and the h-terms of (5.28).

### 4.59 B3, C-ii and the remaining items; Phase B's state (READ and deduced; D127)

- B3 deduced at source (N1STAR-PROOF.md 10.58): every n = 3 numeral of [Hin26c] Definitions 5.13, 5.15, 5.18, Theorems
  8.14, 10.1, 11.1, Proposition 13.18 and Corollary 13.17 comes from (5.7)'s (n - 1)/2 or a density (rho_I^n rho_+^(n+1)
  rho_K at n = 4: beta_I = alpha_I + 2, beta_+ = alpha_+ + 5/2); section 7 uses the principal symbol and thresholds
  only.
- Closed (10.59): [Hin26] (2.27), Proposition 2.25 being stated on X = R^n (10.46(e)'s reading); the iota+ spectrum
  between 5/2 and 3 + eps_+, whose locations sharp5.py K3's interval sweep makes unnecessary; 10.38(a)'s exponent, which
  is at least 2 > alpha_min under either reading; C-ii, [CD03]'s dimension-free gluing with the Tangherlini mass family,
  G-equivariant by uniqueness, the G-invariant KIDs d_t's alone.
- Phase B's state. Discharged: B5, B8, B9 (computed), C-i, 10.46(e)'s (2.27). Deduced at source: B1-B4, B6, B7, B10,
  C-ii, 10.45(e). One kind of reading remains, named in each place: that the propagation, radial point, trapping and
  energy estimates of [Hin26c] sections 7-9.3, [Hin26a] section 5.2 and [Hin23a] section 3 (and those [Hin26c] quotes
  from [HV26], [Hin23c], [Hin24a], [Hin21]) hold at n = 4 once their symbols are the five-dimensional ones the record
  computes -- with 10.57(b)'s order count. That is what separates the result from proved: a line-by-line check of those
  estimates at n = 4.
- Next: the fifty-fifth verifier's findings (D123-D126), a fifty-sixth on D127; then Phase D, the paper.

### 4.60 The general class: settling without symmetry (plan; D128)

M's direction of 2026-10-24 (LOG D128): settling has to hold only within the class for Theorem 4, and the general
class -- perturbations with no symmetry -- is to be included as well. Without G, [Hin26]'s final parameters are the mass
and the spin A in so(4) (10.36), the boost S and the centre-of-mass shift in S_1, four each in five dimensions; his Steps
2, 4 and 5 run with their modifications, forward solutions lose two orders at K+ (the boosts' second order pole), and the
final state is a boosted, centred, slowly rotating Myers-Perry black hole.

*What the record holds for it.* At Tangherlini, without symmetry: the zero energy, generalized and dual states (10.28-
10.31: the mass, six rotations, four translations, four boosts; eleven duals), the pairings and the rigidity (10.32-
10.33), his Lemma 8.15 and Proposition 8.14 near a = 0 with one class of rotations not established (10.34(b)-(c)), the
window (10.35), Lemma 7.5 at every spin (10.36), the pure iota+ resonances at every type (10.37), the augmentation and
2-admissibility (10.39-10.40), section 11.1 (10.42), and every reading of Phase B (10.52-10.59), none of which used G.

*Phase E, each step computed, deduced or READ, one verifier at a time:*

- E1 the inputs at every b near b0 = (m0, 0) in the Myers-Perry family, where [Hin26] takes them at each b from [AHW24]
  and [Hin26a]: mode stability of box^Ups, box^C and L_b at sigma != 0 (his Propositions 6.12, 7.1(1), 8.8) and the zero
  energy count (Proposition 8.11, [AHW24] Theorem 6.1(2)), by perturbation from b0 -- uniform high-energy estimates
  (r-normally hyperbolic trapping and the threshold conditions, strict and so open), continuity on compact frequency
  sets, and at low energy the states that exist at every b against the kernel's upper semicontinuity ([HHV21]'s
  argument at n = 4, READ).
- E2 his Lemma 8.15 and Proposition 7.4 on the rotations that do not stay Killing at a != 0 (10.34(b)'s "not
  established"), and (7.19) on the full metric.
- E3 the low-energy structure with the boosts: the boost entry of the augmentation on Tangherlini and Myers-Perry
  (10.39's OPEN), the boosts' columns (10.40's OPEN), the rotation and boost differences at iota+ computed (10.42), and
  the logarithm question of 10.35(b) at the second order pole.
- E4 [Hin26] sections 11.3-11.8 without the class: Step 2 with the boost parameter and augmentation #1 (Proposition
  11.20, Definition 11.25, Lemma 11.28), Step 4 with the spin and the centre-of-mass modulation (Proposition 11.34,
  Corollary 11.46), Step 5's shifts (Proposition 11.51); the iota+ index sets with the boost's exponents and 10.46's
  bookkeeping over every type and degree with his two orders of loss, the recorded physical states to be his kinds.
- E5 section 12 without the class: Definition 12.1's full U in five dimensions, Theorems 12.3 and 12.8.
- E6 section 5's Theorem 5.23 with the boost, and section 13's Theorem 13.1 without the class.
- E7 Phase C without the class: the data of 10.50 with any small perturbation, glued to the translated, rotated and
  boosted Myers-Perry family -- [CD03]'s "equivalent of Proposition F.1" for that family (Remark 8.2, p. 36), by the
  charge map's Jacobian at Tangherlini, computed -- and the settling statement.
- E8 the readings these add, at source.

Then the paper: Theorem 4 for both classes, one verifier on the whole, the PDF.

### 4.61 E1-E2: the inputs at every b near b0 (deduced; D130)

- Deduced (10.60): mode stability of the three operators at sigma != 0 and the zero energy count at every b = (mu, A)
  near (mu_0, 0) in the Myers-Perry family -- high energy by the open conditions at b0 and [HPS77]'s stability of normal
  hyperbolicity, intermediate frequencies by continuity, low energy by the eleven states that exist at every b against
  the kernel's upper semicontinuity, his Propositions 10.6-10.7 then making L^_b(sigma) invertible near 0: [HHV21]'s
  perturbative route, which its p. 14 expects to give slowly rotating Myers-Perry. E2: 10.34(b)'s modified Step 2 and
  10.36's Lemma 7.5 at every spin.
- Readings added: [HHV21]'s perturbation arguments (its Lemma 11.1, Propositions 10.11 and 11.3) at n = 4.

### 4.62 E3-E6: [Hin26] sections 11, 12, 5 and 13 without the class (computed and deduced; D131)

- Computed (general5.py G1, Proposition 10.46): his bookkeeping over every five-dimensional type with his two orders of
  loss, threshold 4, on [alpha_min, 4]: six pure gauge classes eliminated, fourteen recorded, the physical s2, v2 and t2
  at -2 with no companion and only while alpha <= 2, every recorded image above 4; his four-dimensional lists reproduced
  as the control.
- Deduced (10.61-10.62): his Steps 1-6 with the boosts, rotations and centre-of-mass motions, the index sets at iota+
  with the boost at (2, 0) and min Re alpha_min as in the class, the tensor type's physical state recorded by a parameter
  T_2 beside his S_2 and V_2; Definition 12.1's full U, Theorems 12.3 and 12.8; Theorem 5.23 with the boost; Theorem 13.1
  in five dimensions without the class, settling to a Myers-Perry metric g_b at O(t*^(-2-eps_K)) in spatially compact
  sets. 10.39's OPEN boost entry is 10.28(iii)'s computed residual.
- OPEN: whether five dimensions carry logarithms at (2, 1) at iota+ or his log t* h_b,s1 at K+ (covered either way, his
  parameters indexing log powers).

### 4.63 E7: the gluing to the Myers-Perry family; the general class done on readings (computed and deduced; D132)

- Computed (general5.py G2, Proposition 10.47): the Poincare charges' Jacobian at Tangherlini in the mass, the four
  boosts, the six rotations and the four translations, exactly: diagonal, E = 3 pi mu/8, J = (pi mu/4) W, P = -E v, E C =
  E c, determinant nonzero; [CD03]'s (F.4)-(F.6) reproduced in four dimensions.
- Deduced (10.63): [CD03]'s Proposition F.1 near Tangherlini by the inverse function theorem -- the element its Remark
  8.2 names as missing in higher dimensions -- so its Theorem 8.1 glues the data of g_lam after the shell, perturbed
  without symmetry, to a translated, rotated and boosted Myers-Perry metric, the whole fifteen-dimensional obstruction
  matched; then 10.62(d): the development settles to a Myers-Perry metric g_b with b near (mu_end, 0), the initial slice
  boosted, at O(t*^(-2-eps_K)).
- Phase E is complete on its readings: those of Phase B (B1-B4, B10), [HHV21]'s perturbation arguments at n = 4,
  [Hin26]'s sections 3.4, 5.6 and 11-13 with the boosts at n = 4, and [CD03]'s Theorem 8.1 in five dimensions. Next: the
  paper, Theorem 4 for both classes, and one verifier on the whole.

### 4.64 The fifty-sixth verifier: the parity condition and the gluing slice (READ and deduced; D133)

- READ ([CD03] pp. 35-38, 72-77; [ER08] pp. 14, 16; [Hin26] pp. 3, 119, 204, 208, 214-216; [Hin26c] p. 116): (E.9) on
  the spacetime metric under x^mu -> -x^mu, time included; (8.1) printed with K^-; Remark 8.4; the exact Myers-Perry
  charges; the uniformity and augmentation statements behind 10.60(b), (d).
- Deduced (10.63(b)-(d)): the 3 + 1 parity condition bounds gamma^- and k^+, alpha_- > 2 at n = 4; G-invariance gives
  gamma^- = 0, not k^+; on the tau-slice Tangherlini's own k is even at r^-3, the borderline, so the gluing moves to
  Sigma'', static far out, [Hin26]'s own initial surface there; Theorem 4(ii) restated on Sigma''. The glued member's
  charges lie in a ball about the data's; its boost and translation lie in 10.49's class. The separation's item (iii) is
  withdrawn as a gap: lambda_1 and delta exist, not evaluated, as Hintz's constant.

### 4.65 [Hin23a] section 3 at n = 4 by modification (computed and deduced; D134)

- Computed (exterior5.py X1-X6, Proposition 10.48): every place n enters his section 3, at n = 3 against his printed
  values and at n = 4 -- the conjugated wave operator's ((n-1)(n-3)/4) r^-2; the b-density rho_0^5 rho_I^4 |dg|; the
  energy form (3.25) with Lap + 3/4; the gauge endomorphism (2.11) from Definition 2.2, his matrix and five
  intermediates at n = 3, at n = 4 lower triangular with diagonal 2 gC, gC, 3gC/2, -3gU/2, -gU, 0, -2gU, Remark 2.3's
  duality at both; R_11's quadratic radiation term at r^-2k, r^-(1/2) below the linear terms at n = 4; the Sobolev
  counts.
- Deduced (10.64(a)-(i)): his section 3 at n = 4 step by step with the computed quantities in place: the A^0_h step
  absent, (3.47) without its quadratic term at leading order, the decay recovery with the same l_I, [SR89] with a finite
  loss. 10.57(b)'s order count is computed for R_11's quadratic term.
- B10 is discharged by modification rather than by reading. Remaining readings of Theorem 4: [Hin26c] sections 7-9 and
  [Hin26a] section 5.2 (Phase B's B1-B4), and for part (ii) [HHV21], his boost sections and [CD03]'s argument at n = 4.
  Next: the same census for [Hin26a] section 5.2.

### 4.66 [Hin26a] section 5.2 at n = 4: the calculus and the commutators (READ and deduced; D135)

- READ ([Hin23d] pp. 3, 7, 10-12, 109; [Hin26a] pp. 10, 38, 47, 51, 53-54, 58): the 3b-calculus is built on R_t x
  R^(n-1)_x for every n; each commutator of Propositions 5.8, 5.9 and 5.11 is a principal symbol identity whose square
  roots are Proposition 5.1 (3)-(6); Lemma 5.14 is stated for a Lorentzian vector space.
- Deduced (10.65(a)-(c)): B4's last reading, that the commutator computations give the computed five-dimensional signs,
  is discharged at source: the identities do not see the dimension, and their positivity inputs are 10.13, 10.14 and
  10.22's computations. [Hin26a] Theorem 5.2 holds at n = 4 with every sign computed; Theorems 6.2 and B.1 with it.
  Remaining readings of Theorem 4: [Hin26c] sections 7-9, and for part (ii) [HHV21], his boost sections and [CD03]'s
  argument at n = 4; their censuses are being taken in full text through the alphaXiv connector.

### 4.67 The 57th verifier on 10.64 and D133's repairs (computed and deduced; D136)

- Computed (`exterior5.py` X7-X8): the h-dependent entries of [Hin23a] Proposition 3.29 from P(g) = Ric(g) -
  delta*_(gb,E_C) Upsilon(g; gb) linearized in g = gb + r^-k h -- at n = 3 his printed A(7,1), B(7,1), A(4,7), B(4,1)
  in L_2's normalization, at n = 4 the same numbers times r^-(1/2), exactly (M2: the order was stated, not computed);
  his Lemma 3.6 at n = 4, xbar_I = min(sqrt3/2, 1/(2 mu^(1/4))) and (3.8) negative with f = 1 - mu/r^2.
- Deduced (10.63(b)-(c)): the base of the perturbed data is the glued development's, which contains g_lam on Omega and
  is exact Tangherlini outside a compact set of Sigma'' (M1); the class's gluing needs no parity condition, the charges
  of the KIDs other than d_t vanishing on G-invariant data by averaging over G. Paper: Theorem 4 (ii) in the norms of
  10.62(d); lambda1 and delta exist by the deduction, not evaluated; P = -E v with its sign convention.
- Remaining readings of Theorem 4: [Hin26c] sections 7-9, [HHV21]'s perturbation arguments, [Hin26]'s boost sections
  and [CD03]'s gluing at n = 4; their full-text censuses are in.

### 4.68 The censuses' readings carried to n = 4 (computed and deduced; D137)

- Computed (`gluing5.py` D1-D4): [CD03] Theorem 8.1's dimension-dependent numbers -- fifteen KIDs, the charges'
  scaling under the gluing's rescaling, R^-(n-2) and R^-(n-1), the weighted indices s = t + n - 2 -- and [Hin26]'s
  boost, a Lorentz boost of rapidity c/2 that pulls the mass term back to mu r^-2 (a^4 - 1)(dt*)^2 at n = 4, below the
  radiation order. (`edge5.py` E1-E4): [Hin26c] sections 7-8 -- the wave operator in edge coordinates at I+, the
  K-current (8.10) with its threshold alpha_I < -1/2 unchanged, the rotation fields of S^3, densities and counts.
- Deduced (10.66-10.68): [CD03] Theorem 8.1 at n = 4, and with decay faster than r^-(3/2) in place of its parity
  condition, which has no four-dimensional counterpart; [Hin26]'s boost sections at n = 4, the boost changing the data
  inside his class; [Hin26c] sections 7-8 and Theorem 9.16 at n = 4; [HHV21]'s two arguments with N = 11. Recorded:
  [CD03]'s printed s = t - 1 (the index (8.5) states is s = t + n - 2) and (8.7)'s R^-1 for every charge.
- Remaining: that the censuses are complete, read at source, not re-derived line by line; and the deductions, not
  written at proof level. Theorem 4 (ii) now admits perturbations that decay faster than r^-(3/2) without parity.

### 4.69 A second census by token sweep (computed; D139)

- Computed (`censusweep.py`): 278 markers of the dimension on 205 pages (D143; 270 on 204 before its [CD03] window was
  set right) of the carried passages, read against the sections: all accounted for by 10.53-10.58 and 10.63-10.68 but
  [Hin26a] p. 62's density on level sets of tau, r^3 |dr dgslash| at n = 3, r^4 |dr dgslash_S3| at n = 4 -- a norm
  convention fixed by the metric density, named in 10.69 (f).
- Remaining: completeness of the censuses is evidenced by two methods agreeing, not proved; a dimension entering
  through a bare numeral is found only by reading.

### 4.70 The 58th verifier on 10.65 and D136 (READ and deduced; D138)

- READ ([Hin26d], arXiv:2408.06651, pp. 4, 8, 14, 26): the scaled bounded-geometry calculus [Hin26a] section 2.3.1
  cites is set on a smooth n-dimensional manifold, with the 3b-algebra in every dimension among its examples: 10.56's
  OPEN item on [Hin26d] section 3 closes at source.
- Stated: X7's (4,7) identification uses the contraction reading (the coordinate reading would give -1); the computed
  coefficients and the n = 4 power are unchanged, reproduced independently by the verifier.

### 4.71 The deductions inventoried (measured; D140)

- Measured (`DEDUCTIONS.tsv`, section 10.70): 248 deduced items in 10.12-10.69 -- D 90, B 60, C 31, A 29, ? 38. The
  60 B items, each a 3 + 1 proof carried by modification, are what a line-by-line check would write out; the A, C and
  D items are proof-level once their hypotheses, standard arguments or computations are written.
- Next: write the C items (perturbation, continuity) and the A items' hypothesis checks at proof level, then the B
  items one proof at a time.

### 4.72 The perturbation steps at proof level (proved and deduced; D141)

- Proved (Lemma 10.52, section 10.71): openness of invertibility (Neumann), semicontinuity of the kernel by a
  rank-N stabilization, persistence of strict inequalities on compact sets; cited: Rouche/Hurwitz, the inverse
  function theorem, [HPS77].
- Deduced (the map): each of the 31 C rows of DEDUCTIONS.tsv rests on one of these and a continuity input READ from its
  source; ten rows were misfiled by the rule (exact, computed or B steps) and are listed as such.
- Remaining of 8.8 (ii): the 60 B steps, the A steps' hypothesis checks, the 38 undecided rows.

### 4.73 The general-n steps: every hypothesis placed (READ and deduced; D142)

- READ ([Hin26] pp. 110-111, 217; [Hin26c] pp. 264-265): Proposition 5.25's gauged-data construction is a triangular
  linear system in a frame, the same for any n; Lemmas 10.13 and 14.6 are Hardy inequalities in t at fixed (r, omega)
  with general s through the 3b calculus.
- Deduced (10.72): all 29 A rows of DEDUCTIONS.tsv have their hypotheses placed; 10.38 (a) with one deduced link (X7
  computes it for [Hin23a]'s gauge); 10.51 (c) misfiled (internal).
- Remaining of 8.8 (ii): the 60 B steps and the 38 undecided rows.

### 4.74 The fifty-ninth verifier on D137-D139 (D143)

- M1 seated: on the data, [CD03] needs (E.9) only for the convergence of J^munu ((E.19), (E.20b)); its other uses --
  that Lorentz maps preserve (E.5) and (E.9), and the T_R integral of (E.22) "by parity considerations" (p. 74), on the
  way to the transformation law (E.14) -- fall on the Myers-Perry family, which meets (E.9) with alpha_- = 3; (E.20b)'s
  bulk term vanishes because the data are vacuum (10.63(b)).
- M2 checked and refuted: printed (8.1) bounds r |K^-|, and boosted Kerr's odd K of order m r^-2 forces alpha_- <= 1;
  the verifier's reading dropped the factor r. The reading of (8.1) with k^+ stands (10.63(b)).
- Computed: `censusweep.py`'s CD03 page markers close their pages; read so, with p. 38 added, 278 hits on 205 pages
  (CD03 48); `gluing5.py` D2's conditions now computed from the charges' exponents, with (8.6)'s n = 3 error equal to
  J's main term; D3's embedding threshold derived; D4's pull-back a tensor identity; `edge5.py` E2 for every alpha <
  -1/2 (w > (n - 1)^2/(4(-2 alpha - 1))), E4's fields asserted.
- READ: [Hin26d] pp. 5, 9, 27 (pages corrected), its journal record (doi:10.1090/cams/58); [HHV21] p. 70.

### 4.75 The undecided rows read; symmetry and harmonic sums at proof level (computed, proved, deduced; D144)

- Computed (`synth5.py` S1-S3, Proposition 10.53): the scalar and vector gauge 1-forms on Tangherlini, coefficients
  r/k, r^2/k^2, 1/k, 1/k_V; k^2 = l(l + 2) >= 8 at l >= 2.
- Proved: Lemma 10.54 (harmonic synthesis: polynomially bounded coefficient maps on eigenspaces of a type Laplacian give
  a convergent sum, by the elliptic estimate, Sobolev and Weyl's law); Lemma 10.55 (equivariance: uniqueness gives
  invariance, the Haar mean projects, invertible equivariant maps restrict, averaged smoothing keeps its estimates).
- Deduced (10.73): of the 38 undecided rows, 12 have no step of their own, 25 are at proof level given their inputs (D
  10, A 3, E 5, G 5, H 2), and 10.40 (a) is a modification step. DEDUCTIONS.tsv's `final` column.

### 4.76 The modification steps: each change placed (measured, deduced; D145)

- Measured (`B-MAP.tsv`): 61 rows; 50 name 85 places where the dimension changes the proof, 11 name none; the 88
  placements are 26 computed, 50 at an earlier section, 11 arithmetic in n, 1 the record's choice; 30 rows rest on a
  reading that 10.64-10.68 carry.
- Deduced (10.74): a modification step holds at n = 4 if its source proof uses n only at its listed places (the census
  question) and each changed value meets the proof's conditions there (the table). So 8.8 (ii) reduces to (i).
- Remaining: the censuses' completeness, read at source and checked by two methods (10.64-10.69), not proved; writing
  the source proofs out at n = 4 would replace that evidence by proof.

### 4.77 Eleven modification steps written out at n = 4 (READ, deduced; D146)

- READ at source: [Hin26] Proposition 8.8, Lemmas 6.1, 6.10, 6.13, 7.2, 8.5, Propositions 7.3 and 10.6 and the remark
  after (2.46c); [Hin26c] Corollary 9.43; [CD03] Theorem 8.1's proof.
- Deduced (10.75): each source proof's steps matched to an identity in every dimension, a computed check or an earlier
  section; 10.15 (a), (b), 10.18 (b), 10.24 (b), 10.27 (b), 10.29 (a), 10.30 (c), 10.31 (a), (b), 10.39 (d), 10.63 (c)
  rest on their inputs, not on a census. B-MAP.tsv's column `written`.
- Remaining: 50 modification steps whose source proofs run to several pages each, in [Hin26] sections 5-13, [Hin26c]
  sections 5-14, [Hin26a] sections 4-6 and appendices A-B, and [Hin23a] section 3.

### 4.78 The sixtieth verifier on D140-D145 (D147)

- M1 seated: Lemma 10.54 (ii)'s differentiated sum needs d_r^2 u; the hypothesis now takes i <= 2 and states the two
  bounds on A_j, and 10.73 (vi) writes the weights for 10.33 (a) (w_i = r^(-eps-i), w = r^(1-eps), w' = r^(-eps)).
- M2 seated: the paper's abstract, 1.3, 8.8 and 9 now say "placed on its inputs, at proof level but for two" -- 10.38 (a)
  (one deduced link) and 10.21 (e) (a modification step) -- name 50 rows with places and 11 without, and mark the
  reduction of (ii) to (i) as a rule deduced, not proved.
- Minors: B-MAP.tsv's column `kind` and its rule (an instrument or check named counts as computed); the 30 readings'
  sources; 10.71's closing sentence covering its eleven misfiled rows; beta = min(alpha, n - 2) derived in 10.66 (c);
  mp5.py M2's symbolic block checks named for the family's equivariance; 10.70's ? sentence. Lemma 10.52's continuity of
  the inverse and onto-witness, and the isometry and strong continuity of the rotations, written out; Proposition 5.25's
  0j coefficient corrected.

### 4.79 One exception removed; three more modification steps written out (READ, deduced; D148)

- READ ([Hin26] pp. 81-82, Definitions 4.1-4.2, (4.3), (4.8), (4.13)): the gauge modifications E^Ups_g0, E^C_g0 are
  built from the background and fixed 1-forms alone, so the h-dependent terms of his linearized operator are [Hin23a]'s
  (3.30) term by term; 10.38 (a)'s deduced link is READ, and one exception remains, 10.21 (e).
- Deduced (10.75 (xii)-(xiv)): [Hin26] Proposition 6.15, Proposition 6.18 (4)-(7) and the injectivity half of
  Proposition 9.2 (2), read at source (pp. 125-128, 132-134, 165-167), are matched step by step by 10.28 (a), 10.30 (a)
  and 10.37 (c), the regularity in b added. With [Hin26] Propositions 8.11 and 7.4 (10.32 (c), 10.36 (b); pp. 155-156,
  140-144), sixteen of 61 are written out; 45 rest on the censuses.

### 4.80 The sixty-first verifier seated; a lemma at the horizon proved, the continuation deduced (D149)

- Proved (10.76, Lemma 10.56): for z X' = A(z) X with A smooth, a solution on one side of 0 vanishing to infinite
  order vanishes, by a Gronwall bound |X(z)| >= |X(z_1)| (z/z_1)^M; and one smooth up to 0 from one side is the
  restriction of a smooth solution through 0, by Borel's lemma and variation of constants against a flat error; the
  same for f phi'' + Q phi' + R phi = 0 with f vanishing simply.
- Deduced at proof level (10.76 (a)-(c)): every operator of the record splits over the harmonics into such systems with
  f = g^-1(dr, dr) = 1 - mu/r^2; so a kernel element vanishing outside the horizon vanishes on X, and in [Hin26]
  Proposition 8.8 at n = 4 the gauge 1-form omega, smooth up to r_h by the radial components of delta* omega = u (a
  regular system), continues inside the horizon as a solution of box^Ups omega = 0, so Proposition 6.12 applies on X.
  Closes the continuation (10.27 (b), 10.33) and the interior uniqueness (10.15 (a), 10.16, 10.55 (c)); the kernel
  class stays on its reading.
- The verifier's other findings: 10.75 (iii) rests on 10.19 (d)'s reading, now marked; B-MAP.tsv gives 10.15 (a) and
  10.63 (c) their places (52 name some, 9 none; 96 placements: 32 computed, 52 section, 11 arithmetic, 1 choice; 31
  rest on a reading, ten of the sixteen written out among them); the paper names readings among the deductions'
  inputs; nine minor findings seated (10.75 (ii), (iv)-(vi), (viii), (xi)).

### 4.81 Eleven more modification steps written out (READ, deduced; D150)

- Deduced (10.75 (xvii)-(xxvii)), each source proof READ at source and matched step by step at n = 4: [Hin26]
  Proposition 10.7 with Theorem 10.1 (10.39 (e)), Lemmas 10.9-10.11 (10.40 (a)), Lemma 8.15 with Proposition 7.4 and
  Lemmas 2.15, 7.2 (10.60 (f)), Lemma 11.15 with Proposition 11.14 (10.44 (c)), Theorem 5.23 with Lemma 3.19 (10.66
  (f)), Theorem 13.1 (10.62 (d)) and its Step 1 in the class (10.49 (a)); [Hin26c] Theorem 9.36 (10.20 (a)) and Lemma
  13.13 (10.41 (b)); [Hin24b] Lemma 3.17, which [Hin26] Lemma 8.12 cites verbatim (10.32 (b)); and [Hin26a] Theorem 4.9,
  replaced at n = 4 by Proposition 10.44's certificate (10.54 (a)).
- B-MAP.tsv: the write-outs named nine places their rows lacked and one reading (10.20 (a)); 53 rows name places, 8
  none, 105 placements (33 computed, 57 section, 14 arithmetic, 1 choice), 32 on a reading. Twenty-seven of 61 written
  out, fifteen of them on a reading; 34 rest on the censuses.
- D151 (10.75 (xxviii)-(xxx)): [Hin26] Proposition 8.14 (10.34 (c)), (2.27) with Proposition 2.25 (10.46 (e)) and
  section 5.6's boost pullback (10.62 (c)). Thirty of 61 written out, eighteen of them on a reading; 31 rest on the
  censuses. B-MAP: 104 places, 107 placements (34 computed, 58 section, 14 arithmetic, 1 choice).
- D152 (10.75 (xxxi)-(xxxiv)): [Hin23a] Propositions 3.17, 3.29 and 3.32 with Lemma 3.33, and Corollary 3.31 (10.64 (b),
  (e), (g), (f)), each matched to exterior5.py X1-X7. Thirty-four of 61 written out, eighteen on a reading; 27 rest on
  the censuses, one of them, 10.48 (c), on [Hin23a] Corollary 3.36 (written out in D154; the sixty-third verifier).

### 4.82 The sixty-second verifier seated (D153)

- Lemma 10.56 and 10.76 (a)-(c) checked line by line and passed; 10.75 (xii)-(xvi) and the D149 repairs matched at
  source; B-MAP's counts reproduced. M1: "proved" was said of the continuation, which 10.76 deduces at proof level from
  the lemma; the paper's record, the log's D149 heading and 4.80's heading now say so. Minors seated: the phi''
  coefficient a constant multiple of f; "flat" in Lemma 10.56 (c); the sigma = 0 remark's source and subtraction; the
  interior is Lemma 10.56 (c); [CD03]'s s = t - 1 on p. 37; cross-references in 10.75 (xii)-(xiii); (xv)'s cokernel
  argument; wrapped lines that began with a list marker; the paper's md5 and verifier-record scope.
- D154 (10.75 (xxxv)-(xxxvi)): [Hin26] Proposition 5.11 with Proposition 5.14 and Corollary 5.15 (10.48 (b)) and
  Theorem 5.17 (10.48 (c)), the latter clearing its reading of [Hin23a] at n = 4. Thirty-six of 61 written out,
  eighteen on a reading; 25 rest on the censuses.

### 4.83 [Hin26] section 12, and [Hin26] Theorem 11.12 with [Hin26a] section 6, written out (D155-D156)

- 10.75 (xxxvii)-(xxxix): Theorems 12.3 and 12.8, read at source (pp. 304-318) and matched step by step at n = 4 --
  without the class (10.62 (b)) and in it (10.47 (d)-(e)): the leading iota+ order (2, 0) for his (1, 0), t*^-4 for
  t*^-3 in Step 1, the induction from alpha_min, Proposition 10.46's lists (10.42 (ii)'s in the class), Res(L-bar, 2)
  = {0}. Section 9's iota+ solution theory is a reading at n = 4 (10.47's OPEN), now marked on 10.47 (d) and 10.62 (b).
  Thirty-nine of 61 written out, twenty-one on a reading; 22 rest on the censuses, eight of them [Hin26] section 11's.
- D156 (10.75 (xl)-(xliii)): [Hin26] Theorem 11.12 (10.42 (e)), [Hin26c] Theorem 11.1 applied through Corollary
  11.10 in the shifted densities; [Hin26a] (6.4) and Theorem 6.2 with its Part (2) injectivity (10.21 (a), 10.21 (c),
  10.56 (b)), matched at source (pp. 67-69). Forty-three of 61 written out, twenty-four on a reading;
  18 rest on the censuses.

### 4.84 The sixty-third verifier seated (D157)

- D150-D153 (10.75 (xvii)-(xxxiv)) read against the sources: no major, eleven minors, all seated -- two source misprints
  no longer carried ([Hin23a] (3.47)'s normalization, [Hin26c] p. 60's density factor), one step of [Hin24b]'s proof
  named, three places added to B-MAP, (xxii)'s (2, 0) moved to Step 3, wording and pages.

### 4.85 Fourteen more modification steps written out (READ, deduced; D158-D161)

- D158 (10.75 (xliv)-(xlvi)): [Hin26a] Appendix B -- Proposition B.2 (10.23 (b)), Theorem B.4 (10.23 (c)) and section
  B.4 (10.23 (d)) -- matched at source (pp. 87-98) to tface5.py F2-F5, cpmodes5.py K1-K2 and cform5.py C7.
  Forty-six of 61 written out, twenty-seven on a reading; 15 rest on the censuses,
  [Hin26a]'s only in Theorem 5.2 (10.22 (e)).
- D159 (10.75 (xlvii)-(xlviii)): [Hin26c] Proposition 9.10, the incoming radial estimate, written for general n at
  source (10.19 (a)), and Theorem 9.5 (3) and (5), the index's constancy and the kernel's class (10.55 (b)).
  Forty-eight of 61 written out, twenty-nine on a reading; 13 rest on the censuses.
- D160 (10.75 (xlix)-(lii)): [Hin26] sections 11.3-11.6 -- Propositions 11.17, 11.20, 11.30, 11.32 and 11.34, Lemmas
  11.18, 11.19 and 11.45 and Corollary 11.46 -- in the class (10.45 (b), (e); 10.43 (c)) and without it (10.61 (b)),
  read at source (pp. 231-262). Section 9's iota+ and tf solution theory (Corollary 9.12, Propositions 9.11, 9.30 and
  9.35) enters at n = 4 as a reading, beside [Hin26c] Proposition 13.18 and Corollary 13.17 (10.58 (c)).
  Fifty-two of 61 written out, thirty-two on a reading; 9 rest on the censuses.
- D161 (10.75 (liii)-(lv)): [Hin26] sections 11.7-11.8 -- Proposition 11.51, Theorem 11.59 and Corollary 11.66 -- in
  the class (10.46 (a)-(b)) and without it (10.61 (c)), read at source (pp. 262-295): the centre-of-mass motions in S_1
  = R^4, absent in the class; Proposition 10.46's lists (10.42 (ii)'s in the class) for (9.39b)'s; Lemma 11.65 by
  Proposition 10.46's L_b-images. Fifty-five of 61 written out, thirty-five on a reading;
  6 rest on the censuses, none in [Hin26].

### 4.86 The sixty-fourth verifier seated (D162)

- D154-D157 (10.75 (xxxv)-(xliii) and D157's repairs) read against the sources: one major, ten minors, all seated. The
  major: Theorem 12.3's centre-of-mass shift S^(0)_1 was not placed at n = 4. Its patch h^(0)_s1 keeps iota+ order 1 in
  every dimension, but is pure gauge for g-bar to leading order; what it feeds P is [L_b, chi_K] h_b,s1, of order 5 at
  n = 4 by 10.28's h_b,s1, and quadratic terms of order 4. So Step 2 clears the first and Step 1 the second, and
  Theorem 12.8 subtracts S^(0)'_1 with b' and S' (10.75 (xxxvii), 10.61 (a), B-MAP). The minors: (xxxvii)'s
  physical states and logarithm remark, (xxxv)'s Corollary 5.9, (xvii)'s sign, which cancels, (xxviii)'s endpoint
  closed by the root gap, whole-section citations of census rows counted, two reading marks, (xxxvii)'s reading
  clause, the paper's verifier record, headings and wording. Fifty-five of 61 written out,
  thirty-seven on a reading; thirteen cite a census row; 6 rest on the censuses.

### 4.87 [Hin26c] sections 7-8 written out (READ, deduced; D163)

- D163 (10.75 (lvi)-(lvii)): [Hin26c] section 7 -- Proposition 7.1's concatenation, the five radial point estimates,
  the trapping estimate through [Hin21] Theorem 3.9 (stated for a manifold of any dimension), Proposition 7.11 with
  Lemmas 7.12-7.21 -- and section 8 -- Lemma 8.1's energy estimate, the extension across the inner sphere, Propositions
  8.3-8.13 and Theorem 8.14 -- read at source (pp. 114-157) and matched at n = 4 (10.67 (a)-(b)). Places: the horizon's
  rate f'(r_h), 10.17's trapped set, (7.22)'s symmetric operator and density 2 rho_+^-5 x_I^-8 (checked exactly), the
  nine commuted operators, E2's K-current, the fifteen monomials. Fifty-seven of 61 written out,
  thirty-seven on a reading; 4 rest on the censuses: [Hin26c]'s sections 5, 9-11 and 13 and
  [Hin26a]'s Theorem 5.2.
- D164 (10.75 (lviii)-(lix)): [Hin26c] Theorem 9.5 -- Propositions 9.9 and 9.11, Lemma 9.13, parts (1), (2), (4) and
  (6) -- and Theorem 9.16 with section 9.3's proof, read at source (pp. 161-193) and matched at n = 4 (10.19 (d), 10.53
  (e)). Section 9.3 is written for a general stationary operator on R_t x X; its places are T*S^3, the five-dimensional
  horizon (10.18), the trapped set and loss (10.19 (b)) and the dynamics and timelike dr (10.19 (c)). Both keep one
  reading, his scalar-to-bundle remark (10.53 (d)), and 10.19 (d) the uniformity under small perturbations.
  Fifty-nine of 61 written out, thirty-nine on a reading; 2 rest on the censuses:
  10.58 (c), [Hin26c]'s sections 5, 10-11 and 13, and 10.22 (e), [Hin26a]'s Theorem 5.2.

### 4.88 The sixty-fifth verifier seated (D165)

- D158-D162 (10.75 (xliv)-(lv) and D162's repairs) read against the sources: three majors, eight minors and a note on
  D163, all seated or answered. (li), 10.43 (c), takes its steps from (xlix) and 10.46 (a)-(b), which rest on readings,
  and now says so; B-MAP marks it. (xxviii)'s Step 5: the source concludes eta = 0 from Theorem 7.1 (2) at mu + 1 >=
  -C_0, whose range meets A^(-C_0) only below its left end, and passes over that endpoint; the root gap that closes it
  at n = 4 is the record's own route, and is now said to be, with its check that A^(2-) lies in 10.21 (e)'s range.
  (xxxvii)'s subtraction of D_U Phi(b', S', S^(0)'_1, (0, f'_1), 0, ...) is the source's own, the general case of his
  Step 1.3 (p. 315), which the verifier had not found below the simplified display; it is now quoted, with
  Res_iota+(L-bar, 1) = {0} (p. 315) and Phi's direct use of S^(0)_1 (p. 302), and placing it at lam_0 = 2 is marked
  as the record's step. The minors: (11.135a)'s gauge 1-form, the commutator's two orders, three placements relabelled
  computed, 10.32 (b)'s placements, 10.45 (e)'s settled weight, three equation suffixes, the closing paragraph's ranges
  and 10.62 (b)'s inputs. Fifty-nine of 61 written out, forty on a reading (D162-D164 counted
  one fewer); 2 rest on the censuses.

### 4.89 [Hin26c] Theorem 10.1, Theorem 11.1 and section 13.2 written out (READ, computed, deduced; D166)

- D166 (10.75 (lx)): [Hin26c] Definitions 5.13-5.18, Theorem 10.1 (section 10), Theorem 11.1 and Corollary 13.17 with
  Proposition 13.18 (section 13.2), read at source (pp. 106-109, 201-233, 247-255) and matched at n = 4 (10.58 (c)).
  iplusnorm5.py N1-N9 computes every place the dimension enters, at n = 3 against print and at n = 4 (Proposition
  10.57): the constant 3/2 in N^0, Q_0, the four radial point thresholds, the densities R^4, x_I^-8, mu_b = |dt dx|/(t*
  r^4) and |dx|/|x|^4 with their shifts, (10.40)'s 5/2, Lemma 10.7's eight fields and Lemma 10.9's shift 3. Two of his
  printed sums are off at n = 3 alike: (1.3.1)'s omits Re S, (1.3.2)'s has +4 Re S for -4 Re S, and his stated
  thresholds are the right ones. Lemma 10.9's 0-calculus parametrix is READ for every dimension. Sixty
  of 61 written out, forty-one on a reading; one rests on its census: 10.22 (e), [Hin26a]'s Theorem 5.2.

### 4.90 [Hin26a] Theorem 5.2 written out: no census row left (READ, deduced; D167)

- D167 (10.75 (lxi)): [Hin26a] section 5.2 -- Lemmas 5.3-5.4, Propositions 5.5-5.6, 5.8, 5.9, 5.11, 5.12, 5.16 and 5.17,
  Lemma 5.14, Corollary 5.15 and the duality and initial value arguments -- read at source (pp. 41-66) and matched at n =
  4 (10.22 (e)). Every place five dimensions enter is computed (10.13, 10.14, 10.22's solv5.py Q1-Q4, cform5.py) or READ
  (10.65 (a)); the commutators are identities of symbols with those signs. It rests on no reading, and with it 10.21 (c)
  and 10.23 (c), whose one reading was Theorem 5.2's. All 61 rows of B-MAP.tsv are written out; thirty-nine
  take a reading among their inputs. What remains between Theorem 4 and a theorem is those readings and the census of
  section 8.8 (i).

### 4.91 The sixty-sixth verifier seated (D168)

- D163-D165 (10.75 (lvi)-(lix) and D165's repairs) read against the sources: no major, four minors, all seated. (7.11)
  is (7.11a)-(7.11b) (pp. 117-118); (7.25) is [Hin21] (3-24) for QPQ^-, "almost the content of Definition 5.8" for P
  (pp. 124-125), so the n = 4 check is (5.9) at the trapped set; 10.45 (e)'s place for the weight at I+ is no dimension
  change and is dropped; (lvii)'s two z's are told apart, Seeley's |x| - m and the monomials' (t*, x).

### 4.92 The readings traced to their roots (deduced; D169)

- 10.77 and READINGS.tsv trace the 39 rows that took a reading. Four rested on statements since READ or written out
  (10.23 (b) and (d) on Proposition 9.40, stated for every n >= 3; 10.46 (e) on Proposition 2.25, stated on R^n; 10.62
  (c) on 10.48 (c)-(d), written out) and are re-marked. The thirty-five others rest on ten roots: RB and RU, the
  source's own steps at every n (bundles; uniformity under perturbation); RL, RC and RI, companion results at n = 4
  READ at n = 3 ([Hin26c] section 9.5; [Hin26c] Lemma 3.9 and the calculi behind Lemmas 13.13 and 14.6; [Hin26]
  section 9); RP, RK, RG, RH and RE, the record's own (the pole's logarithm; Corollary 8.13's semicontinuity; the
  G-equivariant read-off; box^C's horizon threshold at small h; the equivariant g_b). OPEN, in this order: RH, RK and
  RG; RL; RC; RP; RE; RI.

### 4.93 Three of the record's roots settled (deduced; D170)

- 10.78: RK (Corollary 8.13's semicontinuity) by Lemma 10.58 from the uniform estimates, so it rests on RU; RG (the
  G-equivariant read-off) by the uniqueness of each step's data, which Hintz states (p. 315); RE (the equivariant g_b)
  by mp5.py M2's covariance, a choice made. Seven roots remain: RB and RU, the source's kind; RL, RC and RI, companion
  results at n = 4; RP and RH, computations. OPEN, in this order: RH at the record's point (box^C's horizon threshold
  in the fibre inner product B, whose conditioning at e = 1/102400 must be measured against h^-1 = 10^6); RL; RC; RP;
  RI.

### 4.94 RH computed: box^C's horizon threshold at the record's point (computed, READ; D171)

- 10.79, `hthresh5.py` T1-T5: [Hin26c] (5.17)'s quantity for box^C over the conormal bundle of the horizon, in [Hin26a]
  Lemma 3.3's B, from the operators' definitions with the g-pairing as the adjoint's control. The undamped part has
  spectrum +-(e^(1/2) + e^(-1/2))/r_h and 0, B's conditioning entering as e^(-1/2); the damping's is -h^-1 l(dr). At (v,
  e, h) = (1/2, 1/102400, 10^-6), 1/2 + vartheta_H+ = -4995.33..., below -C_0 = -100 for every h in (0, h_2), h_2 =
  2.6197... x 10^-5. 10.21 (d)'s threshold holds, and 10.21 (e)'s h is any h in (0, min(h_0, 10^-6)). Six roots remain:
  RB and RU, the source's kind; RL, RC and RI, companion results at n = 4; RP, a computation. OPEN, in this order: RL;
  RC; RP; RI.

### 4.95 The sixty-seventh verifier seated (READ, computed; D172)

- It read D166-D168 at source: two majors, five minors. M1 answered at source: (5.20) defines vartheta_dK+,in by the
  whole imaginary part, S's -(S + S^*) among it (Lemma 5.12's term), and his prefactor at R_cf,+1,in is printed -xi/2,
  equal to 1 there (p. 209), so sigma(Q_0,h)'s Re S is inside vartheta and his (1.3.1) sum omits nothing. D166's 'omits
  Re S' (4.89, 10.75 (lx), 10.57 (N6)) is withdrawn; iplusnorm5.py N6 now derives it, and (10.28) stands as printed at n
  = 3 and n = 4. M2 accepted: 10.22 (e)'s row listed the inputs of its second sentence, Theorem 6.2 by 10.21, which rests
  on 10.21 (d) -- RB through Theorem 9.36 on 1-forms, and RH until 10.79. The row is re-scoped to Theorem 5.2, whose
  proof precedes Theorem 6.2 (p. 67) and uses neither Proposition 10.9's roots nor the zero energy threshold, so its mark
  stands, and with it 10.21 (c)'s and 10.23 (c)'s, which use Theorem 5.2's estimates. Minors: five of 10.58 (c)'s
  placements re-kinded arithmetic, iplusnorm5.py N5 and N9 having checked them by comparisons typed by hand (88 computed,
  38 arithmetic); 10.22's stale sentences marked; the paper's 60 modification proofs are 61 with 10.73's reading;
  [Hin23e] for the 0-calculus paper in 10.75 (lx); 10.23 (d) had been re-marked in D169.

### 4.96 RL written out: [Hin26c] Theorem 9.38, Corollary 9.39 and Theorem 9.41 at n = 4 (READ, computed, deduced; D173)

- 10.80, `tfnorm5.py` R1-R4: section 9.5 is stated and proved for every n, section 9.6 at n = 3; read at source (pp.
  193-200) and written out at n = 4. The places n enters are computed: (9.117) at every n, S~ = S-bar for the Minkowskian
  model, with one misprint named in his intermediate line (-2i rho^(rho^ d - n + 1) for -2i rho^(2 rho^ d - 2n + 3)); the
  indicial roots -lambda and -n + 2 + lambda-bar; the densities' n/2 = 2 in the embedding and in (3.46), so Theorem 9.41
  takes alpha + 2 and the window (-2 + beta_-, -2 + beta_+); (9.122)'s leading part. RL leaves the twenty-two rows, each
  keeping RB. Five roots remain: RB and RU, the source's kind; RC and RI, companion results at n = 4; RP, a computation.
  OPEN, in this order: RC; RP; RI.

### 4.97 RC READ for general n (READ, deduced; D174)

- 10.81: [Hin23d] constructs the b-, scattering, scattering-b-transition and 3b-calculi on compact n-dimensional
  manifolds (pp. 22, 28-31, 37, 59) and characterizes 3b-Sobolev spaces by the Fourier transform with X in R^(n-1)
  (Propositions 4.24 and 4.29, pp. 96-101), which [Hin26c] Lemma 3.7 follows; Lemma 3.9's b-regularity, Lemma 13.13's
  microlocal parametrix and Lemma 14.6's integration in t carry no numeral of the dimension. RC is settled; 10.41 (b)
  leaves the readings, thirty-four rows remain. Four roots remain: RB and RU, the source's kind; RI, companion results at
  n = 4; RP, a computation. OPEN, in this order: RP; RI.

### 4.98 The sixty-eighth verifier seated (D175)

- On D169-D172: no majors. Seated: two semicolons inside B-MAP.tsv entries made commas, so that either separator counts
  214 places and 221 placements; his varrho^2 (Kerr's area-radius factor) for the record's rho^2 in (5.17)'s prefactor,
  in 10.18, 10.79 and `hthresh5.py`; 10.22 (e)'s r = m named as his inner bound; e named e_C beside e^(1/2); 10.77's
  counts marked D169's; N5's label; and, on the fibre inner product, the reading that (5.17) asks for one fixed in
  advance, with `hthresh5.py` T6 computing the threshold for B with e' = 10^-5, 1/10 and 3, each below -100. Not changed:
  the record's statement numbers are a counter apart from its section numbers (Lemma 10.58 in section 10.78, as
  Proposition 10.57 in section 10.58), and 10.74 says 10.21 (c)'s and 10.23 (c)'s one reading was Theorem 5.2's, not that
  it was their one input.

### 4.99 RI written out at n = 4 (computed, deduced; D176)

- 10.82 and `iotasol5.py` J1-J5 (5/5, mutants 5/5): [Hin26] section 9 read at source (pp. 165-199) and written out at n
  = 4. The dimension enters through c = (n - 1)/2 (the thresholds at v = 0, at I+ and at tf's outgoing end, l_scf <
  3/2), the five-dimensional roots and eps_ind (10.24, 10.35, 10.52; t2 and t3 join the expansions), the I+ index sets
  (10.44) and the states (10.28-10.30, 10.34). The index 0 half of Proposition 9.2 is written out through [Hin26c]
  section 10.1.2 at n = 4 ((lx)), Proposition 8.6 and Corollary 9.39 at n = 4. RI leaves its twelve rows; 10.47 (d)-(e)
  now rest on RB. Thirty-four rows take a reading. Three roots remain: RB and RU, the source's kind; RP, a computation.
  OPEN: RP.

### 4.100 The sixty-ninth verifier seated (D177)

- On D173-D175: no majors. Seated: (3.46)'s factor |sigma|^(-n/2 - alpha), the print's sign of n/2 reversed (10.80,
  `tfnorm5.py` R3, B-MAP 10.39 (e)); R3's embedding at ztf; R4's S term; 10.74's 34; the horizon threshold's dependence
  on the fibre inner product (`hthresh5.py` T6: positive at e' = 10, crossing at 7.764), with 10.79 resting on the
  existential reading of Proposition 7.4; 10.81's wording on [Hin23d], the scaled bounded geometry paper and Lemma
  13.13's numerals; 10.41 (b) kept in READINGS.tsv with '-'; the paper's 6/6.

### 4.101 RP settled (deduced; D178)

- 10.83: what the six rows use of the zero energy pole is Hintz's structure -- the augmented inverse uniformly bounded
  near 0 (Proposition 10.7, at n = 4 by (xvii)) and the augmentation's explicit sigma^-1 and sigma^-2 columns, which at n
  = 4 carry no logarithm (10.39) -- not a Laurent expansion; Remark 10.8's sigma log |sigma| terms do not arise at n = 4.
  RP leaves its six rows. Thirty-four rows take a reading; they rest on RB and RU alone, the source's own steps at every
  n. None of the record's roots is open. Not used and not settled: logarithms inside the augmented inverse at n = 4 (the
  five-dimensional tails).

### 4.102 The seventieth verifier seated (D179)

- On D176-D177: no majors; the index 0 half of Proposition 9.2 found placed, every n = 4 numeral of 10.82 checked against
  the source. Seated: 10.80 (c)'s remainder gains the S term; `tfnorm5.py` R3's embedding check now integrates on either
  side of the borderline; `hthresh5.py` splits T6 so that the inner product dependence is T7, with its own control (7/7,
  mutants 7/7); `iotasol5.py`'s J1 excludes a d_t*^2 term exactly, J4 checks the incoming exponent c - S, J2 the ranges
  of (9.5) and (9.21); 10.82's READ list from p. 164; 10.82 (e) names the exponent 2 as 10.59 (c)'s reading, on which
  nothing depends; one wrapped line that began with a number and a full stop, and four that began with + or -, rewrapped;
  the paper's `hthresh5.py` bullet states the dependence.

### 4.103 The seventy-first verifier seated (D180)

- On D178-D179: no majors; 10.83's conclusion holds, three parts of its argument corrected. 10.83 (a): his sections
  11.3-11.7 invert (10.26)'s L~, section 11.8 alone (10.41)'s L~'; section 11 also uses the coefficients' structure at
  zf (a value at 0 and a remainder of positive order: L~(0)^-1, Lemmas 11.21 and 11.33, [Hin26c] Proposition 13.18,
  (10.40)), all written out at n = 4 in (xlix), (l), (liii), (liv); Proposition 9.30's log r-hat term is RI's. 10.83
  (c): a Jensen term would not fit that structure, and the record's chain at n = 4 excludes it (Proposition 10.6,
  Lemma 11.21, Proposition 13.18). Proposition 10.7 is written out in (xvii), not (xviii) (10.83, 10.80 (c), B-MAP,
  4.101, LOG D178). 10.83 (d)'s routes; p. 211. Four wrapped lines with a numbered marker rewrapped. `iotasol5.py` J2's
  conjunct true by construction dropped; `hthresh5.py` T7's control now changes the e' = 10 check too. The paper's
  pole wording narrowed. No row of READINGS.tsv changes.

### 4.104 RB and RU written out (deduced; D181)

- 10.84: a census of [Hin26c] section 9 (pp. 157-200, every numbered item) places every step at which a proof uses
  that the operator is scalar -- subprincipal parts and commutators, thresholds, square roots and Garding, signs and
  norms, defect measures, scalar models -- each with its bundle form, the thresholds being section 5's spectra in a
  fibre inner product; and every constant, symbolic (uniform in b by the openness of strict inequalities, Remark 7.2's
  mechanism) or by contradiction (Theorem 9.28's loss-1 constant with b_j -> b_0 added, the inverse bounds by Lemma
  10.59). [Hin26] asserts RU for section 9 (pp. 119, 124). RB and RU leave their thirty-four rows; each of the ten
  roots is settled, written out or READ, and no row rests on a reading. Not re-run line by line: the scalar proofs
  with the substitutions placed.

### 4.105 The seventy-second verifier seated (D182)

- On D180-D181: one major, nine minors; the conclusion of 10.84 stands. Major: the trapped set's inner product is
  Definition 5.8's, on the pullback bundle over phase space (10.17 (a)'s B_eta), not one on E_X; 10.84 (b), (e) and (g)
  now run Theorem 9.28's arguments for Q-hat P_h,z Q-hat^-, (5.9)'s conjugation, as Proposition 7.10 does in spacetime,
  Q fixed at b_0 serving near b_0. Minors: (b)'s factor 2; the cited scalar energy estimates placed in (f) and (g); the
  delta_Gamma-loss step's uniformity in (g); Theorem 9.16 (3) off Lemma 10.59's list; Lemma 10.59's second part with
  its hypotheses (Y Hilbert, the duality on a dense subspace); the p. 157 "perturb" sentence before section 9's
  heading; `hthresh5.py` T7 split into T7-T8 and `iotasol5.py` J2 into J2 and J6, each with its own control; 10.83
  (c)'s wording. The paper's three standing descriptions of the readings and section 9's list are revised with
  10.85-10.86 (D183).

### 4.106 Section 9 re-run on bundles; the census by a second method (deduced and computed; D183)

- 10.85: `bundlesweep.py` (W1-W4) sweeps [Hin26c] section 9's full text for every marker of scalarity or bundles: 341
  markers in 38 of 62 items, proofs and subsections, each placed; it found the energy estimates near r = m (also the
  seventy-second verifier's) and Proposition 9.19, now placed. 10.86: each section 9 proof the record uses re-run on
  E_X, display by display, with a frame (F1)-(F8) of calculus facts, `bundle5.py` (E1-E6) computing those that are
  identities, and each proof's uniformity in b; at the trapped set the run is for Q P Q^-, (5.9)'s conjugation. What
  remains is the general caveat: deductions at proof level, read by independent verifiers, not proofs checked at the
  level of the theorem's statement.

### 4.107 The seventy-third verifier seated; a sign slip in the source repaired; the full write-out begun (D184)

- On D182-D183: one major, nine minors; 10.84-10.86's conclusion stands. Major: the energy estimate's weight in 10.86
  (r), now e^(lambda r) for the direct estimate and e^(-lambda r) for the adjoint, with a Poincare inequality along r for
  |u|^2 at bounded sigma; (e) and (t) follow. Minors in (F4), (F6), (F8), (k), (m), (n), (q), (u), (e) Part (5) (the n =
  4 exponents 3/2 + S-bar and 3/2 + S), the paper and bundlesweep.py.
- [Hin26c] (9.45)'s diagonal term has the wrong sign in the source (+ 2 i k sigma rho, not - 2 i k sigma rho), and with
  it Proposition 9.11's Step 2 as printed; 10.86 (c)-(d) rewrite the term through the equation, so the diagonal is
  P-hat_0(sigma) itself and (9.44) stands.
- M asked that the deductions and the censuses be closed by proof. The route: `proof5/`, the five-dimensional proof
  written in full, self-contained, from [Hin26c] section 9 on (Part I.A first: sections 9.1-9.2 on bundles at n = 4).
  Theorem 4 stays deduced until the write-out is complete.

### 4.108 The full write-out: Part I.A written (D185)

- `proof5/PART-I-SPECTRAL.md`: [Hin26c] Theorem 9.5 at n = 4, on bundles of any rank and uniformly in the operator, from
  [HJS]'s calculus READ at source; written, not yet verified. Five findings (F1-F5): three already seated in D184, one
  filling four steps the source leaves implicit, one a harmless misprint.
- Next: the seventy-fourth verifier on Part I.A; Part I.B ([Hin26c] section 9.3, Theorem 9.16).

### 4.109 The seventy-fourth verifier seated on Part I.A (D186)

- Part I.A read by the seventy-fourth verifier: two majors (Lemma 3.1's pairing with an absorbing term of top order;
  variable regularity orders outside the calculus READ), seven minors, all seated; F1-F5 confirmed; Theorem 7.2 now for
  constant s.
- Next: a reader for the D186 repairs; Part I.B continues (`proof5/` section 2, the semiclassical calculus, written in
  draft).

### 4.110 The seventy-fifth verifier seated on the D186 repairs (D187)

- The D186 repairs read by the seventy-fifth verifier: each confirmed; two minors in Remark 3.3's variant (the limit by
  weak lower semicontinuity; Step 1 without [A_eps, T_t]) and six nits, all seated; no statement changed.
- Next: Part I.B written in full (`proof5/PART-I-B-HIGHENERGY.md`), then one reader for it and for the two D187 repairs.

### 4.111 Part I.B of the write-out written (D188)

- `proof5/PART-I-B-HIGHENERGY.md` written: [Hin26c] Theorem 9.16 at n = 4 on bundles, uniformly in the operator, with the
  semiclassical calculus proved in its section 2; nine findings, among them the threshold gamma_- (F4) and the assumption
  gamma_- < 0 that Theorem 9.16 (1) needs at real frequencies (F5).
- Next: the seventy-sixth verifier on Part I.B and on the two D187 repairs of Part I.A; then Part I.C.

### 4.112 The seventy-sixth verifier seated on Part I.B; Part I.A proved (D189)

- Part I.A: the seventy-sixth verifier confirmed both D187 repairs; Part I.A is proved.
- Part I.B: one major finding (Proposition 7.2's regularity step, closed by Corollary 4.6') and nine minor ones, all
  seated in place; (F10) added, the range of [Hin26c] Theorem 9.28 (2).
- Next: Part I.C; its verifier also reads the D189 repairs of Part I.B.

### 4.113 Part I.C of the write-out written (D190)

- Part I.C (`proof5/PART-I-C-LOWENERGY.md`): [Hin26c] Theorems 9.36, 9.38 and 9.41, Corollaries 9.39 and 9.43 and
  Proposition 9.40 at n = 4, on bundles and uniformly in the operator; tf-admissibility stated on the Fredholm spaces; an
  adjoint low-energy estimate added.
- Seven source findings (F1)-(F7); (F6), a gap in the proof of Corollary 9.43, is closed by Theorem 6.4 (2)-(3).
- Not proved and not used: (9.115), Remark 9.37, a k-independent smallness and uniformity in alpha in Theorem 9.41
  (Remark 6.7).
- Next: the seventy-seventh verifier on Part I.C and the D189 repairs of Part I.B; then Part II.

### 4.114 The seventy-seventh verifier on Part I.C and the Part I.B repairs (D191)

- Part I.C: no major finding; one statement gap (Theorem 4.3 (4) uniform in theta, used by Corollary 5.2 (b) and
  Theorem 6.4) and nine minor findings, all seated; (F1)-(F7) confirmed.
- Part I.B: the thirteen D189 repairs confirmed; one further clause in Proposition 6.4, Step 2, seated.
- Status: Parts I.B and I.C verified; each is labelled proved once its D191 repairs are read.
- Next: Part II.A (in writing), whose reader also reads the D191 repairs.

### 4.115 Part II.A of the write-out written (D192)

- Part II.A (`proof5/PART-II-A-SETUP.md`): [Hin26c] sections 2-3 at n = 4, with [SBG] READ as the calculus; the weights
  of n = 4 at iota+ and in (3.72); Sobolev embedding on R^5 with the source's thresholds.
- Findings (G1)-(G5): two signs, a missing weight class, the tame estimates per representation, slips in section 3.4
  ((3.85) carries s-m+1), and the standard k = 0 estimates (L3)-(L4) set apart.
- Open: Part II.A' (the k = 0 elliptic and real principal type estimates with finite regularity and variable orders).
- Next: the seventy-eighth verifier on Part II.A and the D191 repairs; then Part II.A'.

### 4.116 Part II.A' of the write-out written (D193)

- Part II.A' (`proof5/PART-II-A2-STANDARD.md`): (L3)-(L4), [Hin26c] Propositions 3.23-3.24 at k = 0, proved for finite
  regularity, variable orders and locally uniform constants, without a sharp Gårding inequality.
- Findings (G6)-(G7): the source's hypothesis on the order is too weak; classical principal symbols.
- Open: the verifier of Part II.A'.
- Next: seat the seventy-eighth verifier's findings on Part II.A (D194).

### 4.117 The seventy-eighth verifier seated; Parts I.B and I.C proved (D194)

- Parts I.B and I.C: the D191 repairs confirmed; both proved.
- Part II.A: the hypothesis of (L4) on the order corrected (M1, the gap of II.A' (G6), found independently); the
  operators of Proposition 9.9 chosen by the openness statement (O) (M2); seven minor findings and the nits seated.
- Open: Part II.A' and the D194 repairs, unread; Parts II.B-II.F and III-VII.
- Next: the seventy-ninth verifier on Part II.A' and the D194 repairs; then Part II.B.

### 4.118 The seventy-ninth verifier seated; Part I.A returned to verified (D195)

- Part II.A': the class of symbols of finite regularity counts logarithmic factors (Definition 1.3); square roots cost
  one factor per derivative (Lemma 2.5, restated, proved and shown sharp); exact orders for z_eps and the parametrix of
  Lemma 4.2; seven minor findings and the nits seated.
- Part I.A: the one-sided cut-offs of Proposition 5.2 repaired; verified until the repair is read.
- Open: the D195 repairs, unread; Parts II.B-II.F and III-VII.
- Next: the eightieth verifier on the D195 repairs; Part II.B.

### 4.119 The eightieth verifier seated; Part II.B written (D196)

- Part II.A': every D195 repair confirmed; two minor findings (the support of g_j in Lemma 4.2, the seminorm count of
  Proposition 2.4) and six nits seated, among them the Theorem 3.51 reading as a READ decision.
- Part I.A: the repaired cut-offs confirmed; the h-symmetrised commutant of Proposition 4.9 stated.
- Part II.B written: [Hin26c] section 4 at n = 4 under (K1)-(K4); four slips of the source recorded.
- Open: the D196 repairs and Part II.B, unread; Parts II.C-II.F and III-VII.
- Next: the eighty-first verifier on Part II.B and the D196 repairs; Part II.C.

### 4.120 The eighty-first verifier seated; Parts I.A, II.A and II.A' proved (D197)

- Part II.B: computations confirmed; one minor finding (the statement of Lemma 3.3 (4)) and four nits seated; verified
  until the repairs are read.
- Parts I.A, II.A and II.A': every repair read and confirmed; proved.
- Open: the D197 repairs to Part II.B; Parts II.C-II.F and III-VII.
- Next: Part II.C, [Hin26c] sections 5-6 at n = 4.

### 4.121 Part II.C written (D198)

- Part II.C: [Hin26c] section 5 and Propositions 6.1, 6.4 at n = 4, with the order functions constructed in full and
  three slips of the source recorded.
- Open: Part II.C unread; Part II.C' (Proposition 6.3); Parts II.D-II.F and III-VII; the D197 repairs to Part II.B.
- Next: the eighty-second verifier on Part II.C; Part II.C'.

### 4.122 Part II.C' written (D199)

- Part II.C': [Hin26c] Proposition 6.3 at n = 4, by a self-contained quantitative persistence theorem in place of
  [Hin21] Theorem 2.6; the stable hypersurface loses one derivative.
- Open: Parts II.C and II.C' unread; Parts II.D-II.F and III-VII; the D197 repairs to Part II.B.
- Next: the eighty-second verifier's report on Part II.C; the eighty-third on Part II.C'; Part II.D.

### 4.123 Part II.C verified (D200)

- The eighty-second verifier on Part II.C: no major finding; one minor (Lemma 1.3's stated Minkowski metric, the claim
  holding) and seven nits, all seated; (C1)-(C3) confirmed at source.
- Open: Part II.C' unread; the D200 repairs; Parts II.D-II.F and III-VII; the D197 repairs to Part II.B.
- Next: the eighty-third verifier on Part II.C' and the D200 repairs; Part II.D.

### 4.124 Part II.C' verified (D201)

- The eighty-third verifier on Part II.C': no major finding; five minor (two gaps in Lemma 2.1, the exact value of
  W-hat_0 t_*, a citation, epsilon_0 for the unstable hypersurface) and nits, all seated; the D200 repairs confirmed.
- Open: the D197, D200 and D201 repairs; Parts II.D-II.F and III-VII.
- Next: Part II.D, [Hin26c] section 7.1 at n = 4.

### 4.125 Part II.D written (D202)

- Part II.D, [Hin26c] section 7.1 at n = 4: the global e3b-estimate, the radial estimates and the estimate at the
  trapped set, the last proved in full in the present calculus rather than quoted from [Hin21]; findings (D1)-(D8).
- Open: the D197, D200 and D201 repairs; Part II.D unread; Parts II.D', II.E-II.F and III-VII.
- Next: the eighty-fourth verifier on Part II.D; Part II.D', [Hin26c] section 7.2.

### 4.126 Part II.D' written (D203)

- Part II.D', [Hin26c] section 7.2 at n = 4: the global estimate with b-regularity and its tame version, by commuted
  systems indexed by words, with families near I+, at the horizon, over dK+ and at the trapped set; findings
  (D'1)-(D'8).
- Open: the D197, D200 and D201 repairs; Parts II.D and II.D' unread; Parts II.E-II.F and III-VII.
- Next: seat the eighty-fourth verifier on Part II.D; the eighty-fifth on Part II.D'; Part II.E, [Hin26c] section 8.

### 4.127 Part II.D verified (D204)

- The eighty-fourth verifier on Part II.D: no major finding; two minor (Lemma 2.5 in its general form in Step 3 of
  Proposition 4.2; the support of the time cut-off's term in Proposition 3.6) and six nits, all seated; (D1)-(D4)
  confirmed at source.
- Open: the D197, D200, D201 and D204 repairs; Part II.D' unread; Parts II.E-II.F and III-VII.
- Next: the eighty-fifth verifier on Part II.D'; Part II.E, [Hin26c] section 8, in writing.

### 4.128 Part II.E written (D205)

- Part II.E, [Hin26c] section 8 at n = 4: solvability with energy estimates on time slabs and in the black hole interior,
  with b-regularity and tame, and the global estimate at high frequencies (Theorem 8.14); findings (E1)-(E13).
- Open: the D197, D200, D201 and D204 repairs; Parts II.D' and II.E unread; Parts II.F and III-VII.
- Next: seat the eighty-fifth verifier on Part II.D'; Part II.F, [Hin26c] sections 10-13.

### 4.129 Part II.D' verified (D206)

- The eighty-fifth verifier on Part II.D': one major finding (the horizon coupling of the word system, indefinite for
  k >= 2), repaired by writing the system with commuting letters replaced in place; three minor (the form of R^(2) in
  (C2), the tame assembly, half of (D'3)) and seven nits, all seated; (D'1)-(D'2) confirmed at source.
- Open: the D197, D200, D201, D204 and D206 repairs; Part II.E unread; Parts II.F and III-VII.
- Next: the eighty-sixth verifier on Part II.E; Part II.F, [Hin26c] sections 10-13, in writing.

### 4.130 Part II.E verified (D207)

- The eighty-sixth verifier on Part II.E: no major finding; six minor (the order on the extension region below t* = 1,
  the domain of the collar flow, the nested-slab bookkeeping of the tame inductions, the support of E_+, the definition
  of the extended time function, a hypothesis of Proposition 3.2) and nine nits, all seated; (E1)-(E13) confirmed.
- Open: the D197, D200, D201, D204, D206 and D207 repairs; Parts II.F and III-VII.
- Next: Part II.F, [Hin26c] sections 10-13, in writing (D208); then its verifier.

### 4.131 Part II.F written (D208)

- Part II.F, [Hin26c] section 10 at n = 4: the normal operator at iota+ and its Mellin family at high and bounded
  frequencies (Proposition 10.6), forward solutions of the normal operator (Proposition 10.12) and of the modified
  operator P_+ (Proposition 10.14), and Theorem 10.1; findings (F1)-(F9) and gaps (G1)-(G7), all closed in the text.
- Open: the D197, D200, D201, D204, D206 and D207 repairs; Part II.F unread; Parts II.F', II.G, II.G' and III-VII.
- Next: the eighty-seventh verifier on Part II.F; Part II.F', [Hin26c] section 11.

### 4.132 Part II.F verified (D209)

- The eighty-seventh verifier on Part II.F: no major finding; seven minor (Step 0 of Theorem 10.1 at order s + 1, the
  bounded weight at I+ in Lemma 5.8, the density factor near 0f, the n = 4 decay rho_+^2 of the metric at iota+, the
  absorption time, finite speed of propagation, the [0C] statements) and eight nits, all seated; finite speed of
  propagation is now Lemma 1.3, from [BGP] Theorem 3.1.1 (READ); four further repairs found while seating (Lemma 6.3's
  slab, Proposition 7.4 (2)'s starting time, Lemma 7.3 (b)'s metric near K+, Theorem 10.1 on Omega_*); (F10)-(F14)
  added; II.E (E14) records the extension its tame estimates use.
- Open: the D197, D200, D201, D204, D206, D207 and D209 repairs; Parts II.F'-II.G' and III-VII.
- Next: Part II.F', [Hin26c] section 11, in writing (D210).

### 4.133 Part II.F' written (D210)

- Part II.F', [Hin26c] section 11 at n = 4: Theorem 11.1 (forward solutions of admissible wave-type operators on
  b-Sobolev spaces with decay at I+, iota+ and K+, tame in the b-regularity, on Omega_*), its form with unweighted
  b-densities and Remarks 11.2-11.4; the order margin 3 + delta + aleph, cut-offs in t-flat, and a simultaneous
  extension across r = r_0; findings (F'1)-(F'12). Not carried: the statement on Omega; uniformity in P_0.
- Open: the D197, D200, D201, D204, D206, D207 and D209 repairs; Part II.F' unread; Parts II.G, II.G' and III-VII;
  uniformity in P_0 (II.F' (F'11)).
- Next: the eighty-eighth verifier on the D209 repairs and Part II.F'; Part II.G, [Hin26c] section 12.

### 4.134 Part II.G written (D211)

- Part II.G, [Hin26c] section 12's tools: the Nash-Moser theorem (Theorem 12.4) proved here, with loss 21d + 6;
  smoothing operators on supported b-Sobolev spaces (Proposition 12.6), checked on Omega_*; tame bounds (Lemma 12.8);
  the section 12.1 weights at n = 4; findings (H1)-(H9). Not carried: Theorems 12.2-12.3 (12.3 due in Part III with
  aleph > 0) and the model problems 12.9-12.12.
- Open: the D197, D200, D201, D204, D206, D207 and D209 repairs; Parts II.F' and II.G unread; Parts II.G' and III-VII;
  uniformity in P_0 (II.F' (F'11)).
- Next: seat the eighty-eighth verifier (D209 repairs, II.F'); Part II.G', [Hin26c] section 13.

### 4.135 The eighty-eighth verifier seated (D212)

- Part II.F's D209 repairs confirmed; two further minor gaps (Lemma 6.3's time cut-off, Lemma 6.4's strip
  0 <= Im sigma < -gamma_+) and four notes repaired. Part II.F' read: one major (the uniqueness class of Theorem 1.1,
  restricted to s' >= inf s - 2), one minor ((E14) narrowed: II.E's tame bounds stated for orders constant and integer
  near the extension face), two notes; repaired. Part II.F' is verified.
- Open: the D197, D200, D201, D204, D206, D207 and D212 repairs; Part II.G unread; Parts II.G' and III-VII; uniformity
  in P_0 (II.F' (F'11)).
- Next: Part II.G', [Hin26c] section 13; the eighty-ninth verifier on the D212 repairs and Part II.G.

### 4.136 The eighty-ninth verifier seated (D213)

- Part II.G read: the Nash-Moser proof complete (24 exponent checks by machine), Proposition 3.1 and Lemma 4.1 correct up
  to presentation. Five minors (two findings against the source withdrawn, (H2) and (H7); (T3)'s first clause deleted;
  the orthant norm equivalence and the quotient-norm identification written out) and nine nits seated. The D212 repairs
  confirmed. Part II.G is verified.
- Open: the D197, D200, D201, D204, D206, D207, D212 and D213 repairs; Parts II.G' and III-VII; uniformity in P_0 (II.F'
  (F'11)).
- Next: Part II.G', [Hin26c] section 13; then one verifier on it with the D213 repairs.

### 4.137 Part II.G' written (D214)

- `proof5/PART-II-G2-DECAY.md`: [Hin26c] section 13 at n = 4. The Fourier transform on the line and on the resolved
  product spaces (sections 2-3), proved without [Tay11a] or complex interpolation; the resolvent bounds in b-Sobolev
  spaces with losses independent of the order (section 4), Proposition 13.16 proved from I.B; the radiation field at
  null infinity, the coefficient of r^(-3/2) (section 5), with [Hin26b]'s two ODE lemmas replaced. Findings (J1)-(J13):
  Lemma 13.4 and Corollary 13.5 fail at sigma = infinity; (13.7)-(13.8) as printed carry no Taylor terms; Proposition
  13.11 (2)'s first step needs l' >= 1 - delta; nonintegral losses, a combination step, the interval in Corollary 13.14
  (2), and k-dependent radii in Proposition 13.18.
- Open: the D197, D200, D201, D204, D206, D207, D212 and D213 repairs; Part II.G' unread; Parts III-VII; uniformity in
  P_0 (II.F' (F'11)), to which II.G' adds no condition.
- Next: one verifier on Part II.G' with the D213 repairs; then Part III, [Hin26] at n = 4.

### 4.138 Part III planned; Part III.B written (D215)

- Part III planned by [Hin26]'s sections: III.A section 2, III.B sections 3-4, III.C section 5, III.D section 6, III.E
  section 7, III.F section 8, III.G section 9, III.H section 10 with [Hin26c] Theorem 12.3 at a loss aleph > 0, III.I
  section 11, III.J section 12; section 13 goes to Part V. Digests of sections 2, 3-4 and 5 taken by extractors.
- `proof5/PART-III-B-FAMILY.md`: [Hin26] sections 3-4 at n = 4. Myers-Perry in Kerr-Schild form for every A in so(4); no
  logarithm between ingoing and outgoing times, so the family is smooth on M and t_* is explicit; mass at |x|^-2, spin
  at |x|^-3; boosts with a(omega)^4 and c^2 = (2/pi^2)||S||^2; trace weight 2/3 in E^Ups and E^C. Finding (K1):
  Definition 3.17's cut-offs inconsistent and Lemma 3.18's vanishing near the black hole not given; repaired by a radial
  cut-off.
- Open: the D197, D200, D201, D204, D206, D207, D212 and D213 repairs; Parts II.G' and III.B unread; Parts III.A,
  III.C-III.J and IV-VII; uniformity in P_0 (II.F' (F'11)).
- Next: seat the ninetieth verifier (II.G', D213 repairs); Part III.A or III.C from the digests.

### 4.139 The ninetieth verifier seated; Parts II.F, II.F' and II.G proved (D216)

- Part II.G' read by the ninetieth verifier: no major finding; Minor 1 (Lemma 3.4's proof, a reversed inequality, bound
  replaced) and Minor 2 (the order of Q_alpha,beta in (4.1b)) and eleven nits seated (II.G' section 7.3); Proposition
  4.7 now at every weight of the gap with one ell. Part II.G' is verified.
- The D213 repairs of II.G confirmed, and the D212 repairs of II.F and II.F' had been confirmed by the eighty-ninth
  verifier: Parts II.F, II.F' and II.G are proved.
- Open: the D197, D200, D201, D204, D206, D207 and D216 repairs; Part III.B unread; Parts III.A, III.C-III.J and IV-VII;
  uniformity in P_0 (II.F' (F'11)).
- Next: Part III.A' (harmonics on S^3, [Hin26] section 2.4; checks d216/harm.py under way) and III.A; the ninety-first
  verifier on Part III.B with the D216 repairs.

### 4.140 The ninety-first verifier seated; Part III.B verified, Part II.G' proved (D217)

- Part III.B read by the ninety-first verifier: no major finding; Minor 1 (a sign slip in Lemma 3.5 (b)'s intermediate
  line) and Minor 2 (Lemma 5.2's hypothesis exhaustive, cut-offs strictly nested, small boosts admissible) and ten nits
  seated (III.B section 7.3). Part III.B is verified.
- The D216 repairs of II.G' confirmed: Part II.G' is proved.
- Open: the D197, D200, D201, D204, D206, D207 and D217 repairs; Parts III.A, III.A', III.C-III.J and IV-VII; uniformity
  in P_0 (II.F' (F'11)).
- Next: Part III.A' ([Hin26] section 2.4 at n = 4; harm5.py K1-K4 computed); then the ninety-second verifier on III.A'
  with the D217 repairs.

### 4.141 Part III.A' written: harmonics on the three-sphere and the Minkowski operators at n = 4 (D218)

- `proof5/PART-III-A2-HARMONICS.md`: [Hin26] section 2.4 at n = 4, proved at general N and read at N = 3 (N = 2 is the
  source, entry by entry). Lemma 1.1 (commutators on S^N from the Ricci identity, replacing the Lichnerowicz citation),
  Lemma 1.2 (five ambient identities), Lemma 1.4 (the spectra on co-closed 1-forms, k_l^2 - 1, l >= 1, and on trace-free
  divergence-free tensors, k_l^2 - 2, l >= 2, proved from Lemma 1.2), Lemma 1.5 ((2.34)-(2.35) at n = 4), Lemma 2.1
  (Lemma 2.29 at n = 4, by the Cartesian route), Lemma 2.3 (indicial roots by type: -d and d + 2 over the degree lists),
  Lemma 2.4 (the symmetric gradient's kernels, Killing fields).
- harm5.py: K5 (Lemma 2.1 equals the Cartesian computation entry by entry, every type, N = 2 and 3, l symbolic), K6
  (the determinants), and a control.
- Open: the D197, D200, D201, D204, D206, D207 and D217 repairs; Part III.A' unread; Parts III.A, III.C-III.J and IV-VII;
  uniformity in P_0 (II.F' (F'11)).
- Next: the ninety-second verifier on III.A' with the D217 repairs; then Part III.A ([Hin26] sections 2.1-2.3).

### 4.142 Part III.A written: [Hin26] sections 2.1-2.3 at n = 4 (D219)

- `proof5/PART-III-A-PREREQ.md`: b-analysis (Lemmas 1.1-1.5: normal form, Fuchsian integration, testing, boundary
  spectrum with the Mellin argument written out, formal solutions), the 3b- and sc-b notions on R^{1+4} (Lemma 2.4,
  Plancherel; the normal operator at sf with S^3), Lemmas 3.1-3.2 (x d_x and x d_x - y d_y), Lemma 4.1 and Proposition
  4.2 (the Fourier transform with partial expansions; inputs II.G' Propositions 3.3 and 3.5).
- Findings (L1)-(L4): (2.29)'s log index is k(E_K, j + 1), not k(E_K, j) (as printed the condition is meaningless for
  E_K = (1,0)); a zf-weight misprint in the proof; the commutator with chi(sigma), harmless; Cauchy's constant in Lemma
  2.15.
- Open: the D197, D200, D201, D204, D206, D207 and D217 repairs; Parts III.A and III.A' unread; Parts III.C-III.J and
  IV-VII; uniformity in P_0 (II.F' (F'11)).
- Next: the ninety-third verifier on III.A after the ninety-second reports; then Part III.C-III.D ([Hin26] sections
  5-6).

### 4.143 Part III.D written: the gauge potential operator at n = 4, [Hin26] section 6 to Proposition 6.9 (D220)

- `proof5/PART-III-D-GAUGEPOT.md`: Lemma 2.1 (Lemma 6.1 at n = 4; S = S-bar near infinity, Q in rho^3 Diff^1_b, the
  zero-energy difference in rho^4 Diff^2_b), Lemma 3.1 (Lemma 6.3: E-bar with m = 2/N, S-bar, M_E with +-N e), Lemma 4.1
  (Lemma 6.6 and (6.17): roots by type, z = 4 e gamma^2, the gap (0, lambda_{s1,2})), Lemma 5.1 (threshold s > 3/2),
  Lemma 5.2 (gamma_- < 0 near b_0), Propositions 6.1-6.3 (6.5 and 6.9; Tangherlini mode stability away from 0 by ODEs,
  replacing [AHW24]), Lemma 7.1 (Lemma 6.8, tf-admissibility).
- harm5.py: K7 (the model operator equals the Cartesian computation, every type, N = 2 and 3), K8 (its indicial
  determinants), with a control.
- Findings (D1)-(D6); (D4): supplement 10.60 (b)'s "the inequalities are open" fails for strong trapping admissibility
  at every epsilon; the open condition gamma_- < 0 is what Part I.B uses and is proved.
- Open: the D197, D200, D201, D204, D206, D207 and D217 repairs; Parts III.A, III.A' and III.D unread; Parts III.C,
  III.D'-III.J and IV-VII; uniformity in P_0 (II.F' (F'11)); (Dyn) in Part VI.
- Next: seat the ninety-second verifier; the ninety-third on III.A and III.D; then Part III.D' ([Hin26] section 6.4).

### 4.144 The ninety-second verifier seated; Part III.A' verified, Part III.B proved (D221)

- Verifier 92 read Part III.A' line by line with harm5.py (Lemma 1.2 by machine at N = 2 with a failing control; every
  K5 matrix at lin5's second point; each Cartesian basis element traced against (2.2)) and the D217 repairs of III.B.
  No major. Minor 1: the labels (3.3, (H6)) said no outside result on harmonics is used; the classical theory of
  harmonic polynomials and the spectral theorem are quoted, and are now named. Minor 2: K2/K3 asserted closure only;
  the selftest now asserts their determinants against Lemma 2.3's lists. Six nits seated (III.A' section 3.4; K5 at two
  points, a 2-tensor control, Lemma 1.5's l ranges, the tensor type proved, (H6)'s READ dependence, `sign` removed).
- Every D217 repair confirmed: Part III.B is proved.
- III.D Proposition 6.2 (d) rewritten before its reading: the horizon is null, so the continuation inside it is by the
  mode equations, Fuchsian at r_h, and Gronwall's inequality, not by a Cauchy argument.
- Open: the D197, D200, D201, D204, D206, D207 repairs; Parts III.A and III.D unread; Parts III.C, III.D'-III.J and
  IV-VII; uniformity in P_0 (II.F' (F'11)); (Dyn) in Part VI.
- Next: the ninety-third verifier on III.A and III.D; Part III.D' ([Hin26] section 6.4).

### 4.145 Part III.D' written: the gauge potential operator at zero energy, [Hin26] section 6.4 and Lemma 6.13 (D222)

- `proof5/PART-III-D2-ZEROENERGY.md`: Lemma 2.1 (Lemma 6.10 at n = 4: kernel span W*, cokernel the horizon pairing l;
  the kernel by energy identities, the cokernel by Box_0 H(r - r_h) = 0 and I.C Corollary 6.6; replaces [AHW24] Theorem
  5.1 (2)), Lemma 3.1 (Lemma 6.11: both pairings 4 pi^2), Proposition 4.1 (Proposition 6.12: a Grushin problem with
  I.C (6.5), Schur complement -4 pi^2 (-i sigma + gamma) + o; Step 2 at every frequency), Lemma 5.1 (Lemma 6.13).
- Findings (D'1)-(D'5); (D'4): the source's Step 2 asserts that c_0 is independent of gamma_{Ups,H}; closed by
  perturbing around a base point where invertibility already holds at every frequency.
- Open: the D197, D200, D201, D204, D206, D207 repairs; Parts III.A, III.D, III.D' unread; Parts III.C, III.D''-III.J
  and IV-VII; uniformity in P_0 (II.F' (F'11)); (Dyn) in Part VI; [Hin26]'s nullspace claim on A^alpha at sigma != 0
  (III.D' Remark (a)).
- Next: seat the ninety-third verifier (III.A, III.D); the ninety-fourth on III.D'; Part III.D'' ([Hin26] section 6.5).

### 4.146 Part III.D'' written: zero energy states from the Minkowski symmetries, [Hin26] section 6.5.1 (D223)

- `proof5/PART-III-D3-SYMSTATES.md`: Lemma 2.1 (Lemma 6.14 at n = 4, one power better throughout, from III.B (3.5)),
  Lemma 2.2 (smooth dependence on b), Proposition 3.1 (Proposition 6.15: omega_s0, omega_s1(S), the boost correction,
  omega_v1(V), with h_s1, h_v1 in A^((3,0) u (3 + E_ind)) and h-breve^1 in A^((2,0) u (2 + E_ind)); no logarithm;
  Killing rotations by the triviality of the zero energy kernel).
- Findings (D''1)-(D''5); (D''3): the source's (6.32c) states less than its proof gives.
- Open: as at 4.145, plus Parts III.D'' unread; Part III.D''' ([Hin26] section 6.5.2, Proposition 6.18).
- Next: Part III.D'''; the verifiers in turn.

### 4.147 Part III.D''' written: generalized zero energy states, [Hin26] section 6.5.2 (D224)

- `proof5/PART-III-D4-GENSTATES.md`: Lemma 2.1 (solving with a prescribed leading term), Proposition 3.1 (Proposition
  6.18 at n = 4: parts (1)-(3) on the symmetries, (4)-(7) the classes, the source's degree ranges; leading terms the
  model's, computed by genstates5 H1-H3 and puregauge5 J5).
- Findings (D'''1)-(D'''6): the recursion's A_2 printed as A_0; (6.39a)'s normalisation; two orders and no logarithm in
  (1); the ranges 0 < z < 4; Lemma 2.1 as the source's "Lemmas 2.15 and 6.13 as usual"; no tensor-type gauge states.
- Deferred: the spanning of ker N(L-bar(0), lambda) (with Lemma 8.4 at n = 4); the window of roots n = 4 needs (with
  the decay of [Hin26] sections 11-12).
- Open: the D197, D200, D201, D204, D206, D207 repairs; Parts III.A, III.D, III.D', III.D'', III.D''' unread; Parts
  III.C, III.E-III.J and IV-VII; uniformity in P_0 (II.F' (F'11)); (Dyn) in Part VI.
- Next: verifier 93's report; Part III.E ([Hin26] section 7, the constraint propagation operator).

### 4.148 Part III.E written: the constraint propagation operator at zero energy, [Hin26] 7 to Proposition 7.3 (D225)

- `proof5/PART-III-E-CONSTRAINT.md`: Theorem 1.1 ([Hin26] Theorem 7.1 at n = 4, the input, proved in Part IV); Lemma 2.1
  (Lemma 7.2: the adjoint at zero energy invertible for b-weights in (0, C_0 + 2], s <= C_0 + 1, indicial roots
  2 - conj(lambda); partial polyhomogeneity; vanishing inside the horizon); Proposition 3.1 (Proposition 7.3: the large
  zero energy dual states of the time translation, the translations and the rotations, eleven at zero rotation).
- Findings (E1)-(E4): the weights move by one (Coulomb root 2 for 1); the corrections one order faster; eleven dual
  states against seven; the input Theorem 7.1.
- Deferred: section 7.2.1 (Proposition 7.4, Lemma 7.5) to Part III.E'; Theorem 7.1 at n = 4 to Part IV.

### 4.149 Verifier 93 seated: Parts III.A and III.D verified; I.B gains Lemma 6.0 (D226)

- III.A: M1 (Proposition 2.25 (1): the one-factor iteration gives a spurious logarithm at tf) repaired by a new Lemma
  3.3, the product operator solved coefficient by coefficient at zf; found while repairing, [Hin26] Lemma 2.23 needs
  alpha + Re z > beta, not alpha > beta (counterexample x^-z chi(xy) (xy)^c), repaired in Lemma 3.2 and by a larger
  free weight beta_K; m1 (the boundary weight in Lemmas 1.4-1.5) and m2 (integrate in decreasing real part) repaired;
  nits n1-n3. Findings (L5)-(L7).
- III.D: m3 (the trapped set's inner product depends on the covector; I.B section 6 assumed one from the base) repaired
  in I.B by Lemma 6.0 ([Hin26c] (5.9)): conjugation by Q = Op(b-tilde^(1/2)), Im(Q P Q^-1) = Q Im_B(P) Q^-1 exactly
  with B = Q*Q, the threshold symbol (6.0) = (1/2)(p_1 + b^-1 p_1 b) + (i/2) b^-1 [r, b] + (1/2) b^-1 H_G b, and the
  estimates carried back; Proposition 6.1 allows X to depend on z. II.C's remark corrected; Lemma 5.2 cites Lemma 6.0
  and names its density. Nits n5-n8 (a doubled gamma_{Ups,H}, the pairing centres, a sign, a Gronwall step).
- Status: III.A and III.D verified; I.B verified, Lemma 6.0 to be read (was proved); II.C's remark to be read.
- Open: the D197, D200, D201, D204, D206, D207 and D226 repairs; Parts III.D', III.D'', III.D''', III.E unread; Parts
  III.C, III.E', III.F-III.J and IV-VII; uniformity in P_0 (II.F' (F'11)); (Dyn) in Part VI.
- Next: verifier 94 on III.D'-III.E and the D226 repairs; Part III.E' ([Hin26] section 7.2.1).

### 4.150 Part III.E' written: the vector type 1 dual states, [Hin26] section 7.2.1 (D227)

- `proof5/PART-III-E2-V1STATES.md`: Lemma 2.1 (O(4)-equivariance of III.B's family); Lemma 2.2 ([Hin26] Lemma 7.5:
  delta*_(g_b) V_b = (1/2) D_A g_b([A, A_V]) exactly, leading term mu rho^3 (dt_* + 2 d|x|) (x)_s rho V(W), no gauge
  term); Lemma 2.3 (Killing rotations = ker ad_A, dimension 6, 4, 2); Proposition 3.1 ([Hin26] Proposition 7.4:
  h* = h-sharp([A(b), A_V]) + h-flat(V), h-sharp on all of so(4), c_0 = mu (1 + 2 (1 + v) gam) / (3 (1 + 2 v gam)),
  (delta*_E)* h-sharp in rho^(floor(C_0) + 5), D Ric(0)* h-sharp compactly supported).
- Findings (E'1)-(E'5): the exact Lemma 7.5; the bracket for the cross product; the coefficients; the source's
  G^2 = Id argument for D Ric* is four-dimensional, replaced by the self-adjointness of G D Ric; the source's statement
  of h-flat's space (T*X, C_0 + 1) misprints its proof's (S^2 T*X, C_0 + 2).
- `dualv1_5.py` V1-V4 (new) and `mp5.py` M1-M5 pass.
- Open: the D226 repairs; Parts III.D', III.D'', III.D''', III.E, III.E' unread (verifier 94 reads III.D', III.D'' and
  the D226 repairs); Parts III.C, III.F-III.J and IV-VII.
- Next: Part III.F ([Hin26] section 8, the linearised gauge-fixed Einstein operator).

### 4.151 Part III.F written: L_b's structure, S-bar, the trapped set, [Hin26] section 8 to 8.1 (D228)

- `proof5/PART-III-F-LINEARISED.md`: Lemma 2.1 ([Hin26] Lemma 8.1: shift 3/2, Q in rho^3 Diff^1_b, the zero energy
  difference in rho^4 Diff^2_b); Lemma 3.1 ([Hin26] Lemma 8.2 and (8.7): rho S-bar = U_1 V_1 + U_2 V_2 through 1-forms,
  V_1 U_2 = 0, so spec S-bar = spec S-bar^C u spec S-bar^Ups u {0 x 5}, both factors triangular by hand); Proposition 4.1
  ([Hin26] Proposition 8.3 in I.B's form: the grading W = 2 wt + s on S^2, preserved by the rotation of the angular
  plane, every lower-order term strictly lowering; scalars 0, 0, 0, -2 (1 - e_C) gam c_2, 0, -2 gam c_2, -4 gam c_2).
- Findings (F1)-(F5): the structure at n = 4; S-bar's spectrum without a matrix; the angular plane and non-spherical
  c_C (closes supplement 10.26 (b)); the covector-dependent inner product (I.B Lemma 6.0); strong trapping near b_0 for
  each fixed eps.
- `lgrade5.py` G1 (new), `sbar5.py` 3/3, `strap5.py` 3/3 pass.
- Next: Part III.F' ([Hin26] sections 8.2-8.3: indicial roots, Lemma 8.5, tf-admissibility, Corollary 8.7).

### 4.152 Verifier 94 seated: the D226 repairs confirmed, III.D proved, III.D' and III.D'' verified (D229)

- The ninety-fourth verifier read the D226 repairs (III.A Lemmas 1.3-1.5, 3.2, 3.3 and Proposition 4.2; I.B Lemma 6.0
  and section 6; II.C's remark; III.D Lemma 5.2 and Lemma 7.1) and Parts III.D' and III.D'' in full: Major 0, Minor 4,
  Nit 7, each scratch check with a failing control (the horizon pairings computed independently, 4 pi^2 at n = 4 and 4
  pi at n = 3; Definition 2.7's index sets on 4000 random cases, decreasing order inside the bound, increasing order
  outside it in 2336; (6.0) derived two ways; (L5)'s counterexample).
- Seated: m1 (III.A Lemma 1.3: the stated order by subtracting the particular solution u_p and reading the homogeneous
  coefficients off on rho_H >= 3/4); m2 (III.D'' Proposition 3.1: the general-b difference of the boost corrections lies
  in H-bar^(oo, alpha'') for every alpha'' < 2, enough through delta*_(g_b)(0)); m3 (I.B: Proposition 6.4 for P_Q also
  uses Proposition 4.5, Corollary 4.6 and Theorem 2.4, which hold for P + hX by Remark 4.7); m4 (I.B Proposition 6.1: b
  built from p'-natural at z); nits n1-n7 (chi_Gamma renamed theta_Gamma in Lemma 6.0; P'_Q dropped; Lemma 3.3's
  coefficient on (1/4, 3/8) by uniqueness; 'absorbed in l' at zf and scf; I.A Theorem 7.2 (3) for the index at bounded
  sigma; (M4)'s b gauge-invariant; omega_(b,v1) smooth on X).
- Status: III.D proved; III.D' and III.D'' verified, their nits to be read; III.A and I.B verified, the D229 repairs to
  be read; II.C's D226 remark confirmed.
- Next: verifier 95 on the D229 repairs and Parts III.D''', III.E, III.E', III.F; Part III.F' ([Hin26] sections
  8.2-8.3).

### 4.153 Part III.F' written: indicial roots and tf-admissibility of L_b, [Hin26] 8.2-8.3 (D230)

- `proof5/PART-III-F2-INDICIAL.md`: Lemma 2.1 (the factorisation, lin5.py E2); Lemma 2.2 (box^C at vector type 1: roots
  3 and -1 - 2 gam_C v_C, by hand); Proposition 2.3 ([Hin26] Lemma 8.4: the list by type, no root with real part in (0,
  1], the even split, 0 only at s0 and s2 and simple, simplicity and (8.13) under (C2)-(C4) and z off a countable set);
  Lemma 2.4 (roots in a strip lie on finitely many isotypic components, uniformly in a parameter); Lemma 2.5 ([Hin26]
  Lemma 8.5: h_s0 = -dt^2 + (2 - e_U)/(4 e_U) dx^2, h_s2 = delta*(rho^-1 w_S)); Lemma 3.1 (the relative index at ztf);
  Lemma 3.2 (common orders); Proposition 3.3 ([Hin26] Proposition 8.6); Corollary 3.4 ([Hin26] Corollary 8.7: beta_sctf
  < 3/2, beta_ztf in [-1, 0)).
- Findings (F'1)-(F'6): the n = 4 roots and the factor lam (lam - 2) at v1; simplicity and (8.13) rest on (C2)-(C4),
  added to Part IV's obligations; Lemma 8.5 is not needed for tf-admissibility at n = 4; the index argument without
  restriction to a type; the Fredholm spaces in place of the source's conormal kernels; Corollary 8.7's weights.
- `linroots5.py` R1-R3 (new) and `lin5.py` E1-E5 pass.
- Open: III.E Theorem 1.1 (3) to receive (C1)'s count and (C2)-(C4) once verifier 95 has read III.E; Parts III.C,
  III.F''-III.J and IV-VII.
- Next: Part III.F'' ([Hin26] section 8.4: mode stability, the gauged linearised black holes, the zero energy
  (co)kernel).

### 4.154 Verifier 95 seated: I.B, III.A, III.D', III.D'' proved; III.D''', III.E, III.F verified; III.E' proved (D231)

- The ninety-fifth verifier read the D229 repairs and Parts III.D''', III.E, III.E', III.F in full: Major 0, Minor 2,
  Nit 6; all eleven D229 repairs correct and complete; every instrument the parts cite rerun and checking what its part
  says; scratch checks with failing controls (the model states, box^C's indicial families at n = 4, the trapped set
  matrix, S-bar's spectrum, III.D''''s resonance conditions).
- Seated: M1 (III.D''' Proposition 3.1: in the recursion the other terms are shown lower by epsilon_ind, which is all
  the leading coefficient needs; the first correction of each state stays two orders down, (D'''3) narrowed); M2 (III.E
  consequence (a): the inverse at alpha in (0, min Re F - 2), the constructed solution equal to it by injectivity);
  n1-n6 (smooth on X; chi_partial W-bar; a sign; rho^6 C^oo + H-dot^(-1, C_0+6); the supported character inside the
  horizon; sigma kappa in III.F).
- III.E Theorem 1.1 (3) amended with the count by type (s0 2|2, scalar l >= 1 3|3, vector 1|1, checked by the verifier
  at the record's point for l <= 2) and III.F''s (C2)-(C4); the verifier's caution for Part IV: 'sufficiently large
  gamma_C' means gamma_C >~ 1/e_C (damping5.py U6).
- Next: verifier 96 on the D231 repairs and Parts III.F', III.F''.

### 4.155 Part III.F'' written: mode stability of L_b away from zero frequency, [Hin26] Proposition 8.8 (D232)

- `proof5/PART-III-F3-MODES.md`: Lemma 1.1 (the horizon threshold of L_b, [Hin26] footnote 78 at n = 4: det(k - K) = k^5
  (k - 1 + x)^3 (k - 2 + 2x)(k + (1 - e_C) x)(k - y)(k + 1 - y)^3 (k + 2 - 2y), x = a_v gam_C r_h, y = c_v gam_UH r_h,
  so s > 1/2 + max(0, 2 - 2x) with III.D''s horizon modification and a_v >= 0; lhor5.py H1-H2, new); Corollary 1.2 (Part
  I's hypotheses for L_b: Fredholm of index 0, invertible for |sigma| >= C_0, uniform in b); Lemma 1.3 (conormal kernel
  elements lie in X_sigma); Lemma 2.1 (the r-row of delta* omega = h as a radial ODE system); Theorem 2.2 ([AHW24]
  Theorem 6.1 (1) on five-dimensional Tangherlini: Kodama-Ishibashi master equations, V_T, V_V, V_S > 0 for l >= 2, the
  exceptional sectors s0, v1, s1 pure gauge, the s1 gauge glued across sigma^2 r^4 = mu_0 by analyticity); Lemma 2.3 (a
  solution continued inside the horizon: Borel and a flat correction); Proposition 3.1 ([Hin26] Proposition 8.8 at b_0,
  every sigma != 0 of the closed upper half plane, harmonic by harmonic: Bianchi, III.E Theorem 1.1 (1), Theorem 2.2,
  Lemma 2.3, III.D' Proposition 4.1); Proposition 4.1 (b near b_0, |sigma| >= c_0).
- Findings (F''1)-(F''4): [AHW24] replaced at b_0 with no estimate in l, the localisation to the exterior removed by
  continuing the gauge potential; the horizon threshold of L_b, absent from III.F; the scalar type 1 sector at real
  sigma; open: b != b_0 with 0 < |sigma| < c_0.
- `gmodes5.py` G3 now also checks that the trace-free angular equation is [KI03]'s algebraic relation, E_T = -(k^2/(4
  r^2)) (F^a_a + 2F); G1-G5, `lhor5.py` H1-H2 pass.
- Open: b != b_0 with small nonzero sigma (to the low-energy parts on [Hin26] 9-12, or Part VI); Parts III.C,
  III.F'''-III.J and IV-VII.
- Next: verifier 96 on the D231 repairs and Parts III.F', III.F''; Part III.F''' ([Hin26] Proposition 8.9 to Corollary
  8.13: the zero energy kernel and cokernel).

### 4.156 Part III.F''' written: the zero energy (co)kernel of L_b, [Hin26] 8.9-8.13 (D233)

- `proof5/PART-III-F4-ZERO.md`: Lemma 1.1 (g-dot at b_0 from the Kerr-Schild form: r^-2 (dt+dr)^2 and 2 mu_0 r^-4
  (dt+dr) (x)_s (A-dot x) . dx, r = |x|; mp5.py M3); Lemma 2.1 (inverse images of rho^(2+k) C^oo, k = 1, 2, lie in
  A^((k,0) u (k + E_ind))); Proposition 2.2 ([Hin26] Proposition 8.9: no logarithm; g-dot^Ups(1,0) in A^((2,0)...),
  g-dot^Ups(0,A-dot) in A^((3,0)...)); Remark 2.3 (Remark 8.10: g-dot^Ups(0,[A,A_V]) = 2 h_b,v1(V)); Theorem 3.1
  ([AHW24] Theorem 6.1 (2) on Tangherlini, per type and degree, static5.py S1-S6); Corollary 3.2 (stationary gauge
  invariants); Proposition 4.1 ([Hin26] Proposition 8.11: index 0, kernel and cokernel 11-dimensional, at b_0 directly
  and near b_0 by the augmented operator and I.C Theorem 7.1); Corollary 4.2 ([Hin26] Corollary 8.13).
- Findings (F'''1)-(F'''6): no logarithm; eleven for seven; [AHW24] replaced at b_0 and avoided near it; Lemma 8.12 not
  used (independence by types, gauge invariants, continuity and the dual states' leading terms); the adjoint (8.25) with
  G^-1 = Id - (1/3) g tr; densities |dg_b| = |dt*| |dx| and weights alpha in (0, 1].
- `static5.py` S1-S6, `zstates5.py` Z1-Z6, `mp5.py` M1-M5 rerun; `lin5.py` E3-E5 pass (E1-E5 all pass).
- Open: [Hin26] Lemma 8.12 at n = 4 at proof level (with section 8.5's pairings, the next part); b != b_0 with small
  nonzero sigma (III.F''); Parts III.C, III.F''''-III.J and IV-VII.
- Next: Part III.F'''' ([Hin26] Lemma 8.12 and section 8.5); verifier 97 (Opus) on III.F''' and the verifier 96 repairs.

### 4.157 Part III.F'''' written: the zero energy pairings and the physical states at -2 (D234)

- `proof5/PART-III-F5-PAIRINGS.md`: Lemma 2.1 (the t*-coefficients of G D Ric: symmetric, antisymmetric, symmetric; D
  Ric delta* = 0 gives P1 delta* omega = -P0 (dt* (x)_s omega), P2 delta* omega = -P1 (dt* (x)_s omega)); Lemma 2.2 (the
  reduction to infinity of [Hin24b] Lemma 3.17 written out, first and second order, critical weight a + c = 2 resp.
  min(a - 3, a-breve - 2) + c = 0, invariance under decaying gauge and t* -> t* + phi, phi in |x| C^oo); Lemma 3.1
  ([Hin26] Lemma 8.12: 3 pi^2 mu-dot, 2 pi^2 mu <A-dot, A'>_F, (3 pi^2/2) mu xi_S . xi_S', pairing5.py P2-P5, block
  triangular); Lemma 4.1 ([Hin26] Lemma 8.15: lambda-sharp = pi^2 mu <A_V, .>_F on all of so(4) by Remark 8.10 and
  spin-independence); Proposition 5.1 ([Hin26] Proposition 8.14 (1) at -2 for s2, v2, t2, Step 2 modified).
- Findings (F''''1)-(F''''5): the reduction written out; Lemma 8.15 (2) without a direct computation; which states (no
  -3, no companions; window5.py W2); Step 2 modified; the values and normalisations.
- Open: the window (the slowest iota+ term) in the part on [Hin26] sections 9-11; Parts III.C, III.G-III.J and IV-VII.
- Next: verifier 97 (Opus) on III.F''', III.F'''' and the verifier 96 repairs; Part III.G ([Hin26] section 9).

### 4.158 Verifier 97 seated: III.D''', III.E, III.F proved; III.F'-III.F'''' verified (D235)

- The ninety-sixth verifier (Fable) was stopped with no report; the ninety-seventh (Opus) read its brief and III.F'''
  and III.F'''': the D231 repairs, Parts III.F', III.F'', III.F''', III.F''''. No major finding; three minor, eleven
  nits.
- (A) The eight D231 repairs correct and complete; III.E Theorem 1.1 (3) as amended is an obligation of Part IV, as
  III.F' treats it. III.D''', III.E and III.F: proved.
- m1 (III.F'): C_0 = 100 (III.F; damping5.py U4 certifies 100), against C_0 >= 101; now -101 and |lambda| > 101. n1:
  (C1) needs gamma_C large against 1/e_C, and epsilon_ind < 3 x 10^-6 at the record's point (the scalar type 2 root 1 +
  2.93 x 10^-6); n2: the cancelled root at s1.
- m2 (III.F''): Lemma 2.1 (b)'s A = O(r^-1) false (the entry i sigma); the conclusion via the b-system in (w_r, w_t*/r,
  w_A/r), Gamma^lambda_rr, Gamma^lambda_rt* = O(r^-3) in III.B's t*. n3: Z := -Psi int ... (sign); n4: x > 0 since c_C
  is past timelike, the source's 5/2 ignores the damping; n5: C_hf; n6: III.F (1.2).
- III.F''': n7 the two epsilon_ind told apart; n8 energy identities for complex solutions; n9 Lemma 2.3 smooth up to r =
  r_0 (stated on {r > r_0 - delta_0}).
- m3 (III.F''''): Step 3 placed u_b in A^(alpha - eps) only; f_b is polyhomogeneous, so u_b is by III.A Lemma 1.4, and
  (5.1)'s index set is reached (it contains the roots lambda^C_+ - 1 just above 1, which the low-energy parts carry).
  n10: the weight > 1; n11: Lemma 3.1 (2) at spinning b, spin-independent leading term.
- Checks: linroots5, lhor5, gmodes5 rerun, pass; the verifier's scratch checks (horizon sign, F3 radial system, the
  factorisation at s0, v1, the mass and spin pairings 3 pi^2 mu-dot and 2 pi^2 mu) pass with failing controls.
- Status: III.D''', III.E, III.F proved; III.F', III.F'', III.F''', III.F'''' verified (D235), the repairs to be read.
- Next: Part III.G ([Hin26] section 9.1 at n = 4: Proposition 9.2 by the Fredholm theory on sf across v = 0 and the
  semiclassical estimate, Proposition 9.4); verifier 98 (Opus) on III.G and the D235 repairs.

### 4.159 Part III.G written: [Hin26] Proposition 9.2 at n = 4 (D236)

- PART-III-G-SPECTRAL.md: N_sf(lambda) = -2 d_v(v d_v + lambda - 3/2 - S) + L(0)(omega, v d_v + lambda, d_omega) on
  sf = R_v x S^3, supported at v = -1, across the light cone v = 0, b-elliptic at R = 1/v = 0.
- Fixed lambda: the light cone N*{v = 0} a radial source, beta_0 = 2(1 + v), threshold s < 2 - Re lambda (the source's
  3/2 - Re lambda at n = 3); the Fredholm property for s below it and mu in (Re lambda - 1, Re lambda); b-regularity by
  Lie derivatives along the rotations and v d_v, whose commuted terms have first-order symbols vanishing at the light
  cone.
- Injectivity for Re lambda < 3/2 (the source has 1 + epsilon_ind at n = 3): II.F Lemma 5.8 with III.F' tf-admissibility
  on (0, 1] and conormality at the light cone for s > 1/2.
- Index 0 and finite meromorphy: the semiclassical estimate in vertical strips, lambda = iz/h, |Im z| <= Ch; escape
  function -(v + 2)(v xi + 1), with H_p of it 2(v + 1)|eta|^2 on the characteristic set; II.F at the cone point.
- Check: sf5.py S1-S8 (new), each with a failing control, pass.
- Status: III.G written (D236).
- Next: Part III.G' ([Hin26] Proposition 9.4, Definitions 9.3 and 9.6 at n = 4: extendible conormality below 1/2 by
  multiplying by v^k, a Heaviside multiplier and the primitive in v); verifier 98 (Opus) on III.G and the D235 repairs.

### 4.160 Part III.G' written: [Hin26] Proposition 9.4 at n = 4 (D237)

- PART-III-G2-IOTA.md: the iota+-normal operator N_iota(lam) = R^(-2-lam) N_sf(lam) R^lam, which in v is
  -2v(v d_v - lam)(v d_v - 3/2 - S) + v^2 L(0)(omega, v d_v, d_omega), inverted through III.G's inverse; Definitions
  9.3, 9.6 and Remark 9.7 with it.
- S is semisimple at n = 4 (Lemma 1.1; sbar5.py S4, new, control at gamma_Ups = gamma_C (1 - v_C) has a Jordan block),
  so the I+ exponents are 3/2 + s, s in {0, (1 - e_Ups) gamma_Ups, gamma_Ups, 2 gamma_Ups}, one per eigencomponent.
- At K+ the index set is III.A Lemma 1.4's, generated by the III.F' roots with real part <= 0; its only exponent with
  real part 0 is (0, 0), the next ones lam^Ups_s0,2 - 2 and lam^Ups_s1,2 - 2 in (0, 1/4).
- Conormality at the light cone for every Sobolev order s not in 1/2 + Z (Lemma 2.1, by primitives in v), replacing
  the source's (9.5), (9.21); the v^lam-terms and their logarithms excluded through a Mellin recursion.
- Remark 9.7 as a lemma: poles of N_sf^-1 invisible on iota+ lie in 5/2 + spec S + N_0 (sf5.py S10, new).
- Source slips: (9.22) has v^2 for v/2; (9.17) holds only to order 2 + (1 - e_C)(1 - v_C) gamma_C.
- Checks: sf5.py S9-S10 and sbar5.py S4 (new), each with a failing control, pass.
- Status: III.G' written (D237).

### 4.161 Verifier 98 seated: III.F'-III.F'''' proved; III.G verified, injectivity raised to Re lam < 2 (D238)

- The ninety-eighth verifier (Opus) read III.G in full and the D235 repairs: one major finding, one minor, six nits on
  III.G; the D235 repairs correct, with three nits.
- A1 (major, III.G Proposition 4.6): Lemma 4.4's slab estimate is at constant semiclassical order, while Lemma 4.2's
  order varied over the slab. Repaired: the order 1 - (1 - g(v))(1 - psi f_1 f_2), with g non-increasing, 1 on {v <=
  -1/4}, 0 on {v >= -1/8}; constant b_in on the slab, and non-increasing in the direction of propagation (increasing v)
  over (-1/4, -1/8).
- A2 (minor): injectivity at Re lam < 3/2 was the method's limit (Lemma 3.1 for s > 1/2). Lemma 3.1 now holds for
  every s not in 1/2 + Z, II.F Lemma 5.7 for a > -1, and u is its own extension by zero for s > -1/2. So N_sf(lam) is
  invertible for Re lam < 2, the tf weight limit; pure iota+ resonances have real part >= 2 (10.37 (c)).
- Nits A3-A6: the turning point by H_p^2 v = -4(v + 1)/(v(v + 2)) < 0 (sf5.py S11, new); the compactness argument in
  Lemma 4.2 and the face F_K by II.F (3.12); the frames of b and xit; two wording slips.
- B1-B3 (nits on the D235 repairs): the angular row of III.F'''s b-system; III.F'' Lemma 2.3 needs w smooth on {r >=
  r_h} only; the leading term (dt* + 2 d|x|) in III.F''''.
- Checks: sf5.py S1-S11 pass, each control fails.
- Status: III.F', III.F'', III.F''', III.F'''' proved; III.G verified (D238), the repairs to be read; II.F Lemma 5.7
  amended; III.G' written.
- Next: Part III.G'' ([Hin26] Definitions 9.8, 9.10 and Proposition 9.9 at n = 4, the expansion at K+); verifier 99
  (Opus) on III.G' and the D238 repairs.

### 4.162 Part III.G'' written: [Hin26] Propositions 9.9, 9.11, Corollary 9.12 at n = 4 (D239)

- PART-III-G3-GRAFT.md: the window. Every iota+ order grafted exceeds 1 (pure resonances >= 2, III.G), so R^l_K with
  l_K < 3 suffices (K+ order lam + l_K > 4); no state at -3 and no companion of the physical states at -2 is needed.
- Table 1.1: the roots in (-3, 0] with the states constructed in III.D'', III.D''', III.F'''' and their companions;
  Lemma 1.2: the leading terms span the indicial kernels (the item III.D''' deferred), from simplicity and (R5).
- Towers and formal solutions (Minkowski and Myers-Perry), their errors; the expansion at K+ (Proposition 9.9) by
  induction on the least exponent, log-free; grafting (Proposition 9.11) with L-bar the iota+-normal operator of L_b by
  an exact identity; Corollary 9.12.
- New obligation for Part VI: (C5) gamma_C v_C >= 1/2 (else the window is l_K < 2 + 2 gamma_C v_C).
- Status: III.G'' written (D239).

### 4.163 Verifier 99 seated: III.G proved; III.G' verified (D240)

- The ninety-ninth verifier (Opus) read III.G' in full and the D238 repairs: one major finding, two minor, seven nits
  on III.G'; the D238 repairs correct and complete.
- M1 (major): III.G' Theorem 3.1 (2) claimed (v d_v - 3/2 - S) h in order l_I + 1 for finite-regularity f; the f-term
  limits it to l_I, as the source prints. Repaired; III.G'''s grafting uses order l_I, which suffices.
- m1: gamma_Ups < min(s_C / 2, 3/8) now assumed, and the choices of eps and l_I that keep exponents apart are stated.
  m2: the expansion coefficients are holomorphic in lam by fixed-circle Mellin integrals.
- Nits: "at most k_s" in Step 4; the v^lam log v term in Step 5; z_Ups for III.D's parameter and the root 0 in Lemma
  1.3; the induction exponents renamed; sbar5.py S4's control tests the product alone; sf5.py's S10 reference; and
  (G'3), the misprint read in the source's (9.22), withdrawn (the normalised text renders v/2 and v^2 alike).
- Checks: sf5.py S1-S11 and sbar5.py S1-S4 pass, each control fails.
- Status: III.G proved; III.G' verified (D240), the repairs to be read; III.G'' written.
- Next: Part III.G''' ([Hin26] Lemmas 9.13-9.14, Proposition 9.15 to Proposition 9.22); verifier 100 (Opus) on III.G''
  and the D240 repairs.

### 4.164 Verifier 100 seated: III.G' proved; III.G'' verified (D241)

- The hundredth verifier (Opus) read III.G'' in full and the D240 repairs of III.G': one major finding, two minor,
  seven nits on III.G''; the D240 repairs correct and complete, one nit.
- M1 (major): the iota+-normal operator is that of 2 L-bar (III.G (1.3), Lemma 1.2 (c)), so Lemma 4.1 and (4.4) were
  off by a factor 2. Repaired: (4.1) for 2 L_b, u_+ := N_iota(lam)^-1 (2 f_+).
- m1: the window l_K < 3 needs the least grafted order above 1 + max(eps_K, eps_ind); for the source's direct grafts
  at lam = 1 ((10.15), p. 247, (11.119a)) that is the record's open reading alpha_5. Stated as conditional, to be
  proved where those grafts are written (III.H-III.I).
- m2: Corollary 4.3's hypothesis is now a finite quasi-homogeneous sum plus a remainder of iota+-order infinity.
- Nits: E_ind contains (2, 1) at lam = 1, chi_K a function of R near iota+; B = B_0 + v B_1 + v^2 B_2; the origin of the
  s0 root 0; the root-shift wording; lam_0 != 1 for holomorphy; the v1 summands; section 13.2 out of scope. In III.G'
  the remainder's holomorphy in the l_I-weighted space by local boundedness ([AN00] Theorem 3.1).
- Checks: sf5.py S1-S11 and sbar5.py S1-S4 pass; the verifier's symbolic check of the factor 2 on 4+1 Minkowski.
- Status: III.G' proved; III.G'' verified (D241), the repairs to be read.
- Next: Part III.C ([Hin26] section 5 at n = 4) and III.G''' ([Hin26] Lemma 9.13 on); a verifier on them and these
  repairs.

### 4.165 Part III.C written: [Hin26] sections 5.1-5.3 at n = 4 (D242)

- Proved, at n = 4: the exterior region's corner coordinates (rho_0, rho_I, omega), global near infinity, with d_t* =
  rho_0 (X_0 - X_I) exactly; Definitions 5.2-5.4 and 5.13; Remark 5.5 where phi_S is the boost; Proposition 5.11 and
  (5.41a); Proposition 5.14; Corollary 5.15.
- The structure: L_(g,g0) == -rho_0^2 rho_I (X_I - 3/2 - A-bar)(X_0 - X_I) modulo (rho_0^2 rho_I^2 C^oo + H^(k-2, (E_0 +
  2, l_0 + 2), (E^tot, l_I))) Diff^2_b, A-bar constant and lower triangular (S-bar in the splitting, scri5.py C1). The
  perturbation's entries, the source's A^h - A_0 and B^h, are half an order lower: 10.38 (a)'s scaling argument proved.
- Index sets at I+ start at 3/2. One condition added, E^tot + (E^tot - 1) in E^C, which needs gamma_Ups < 1/4 (Part VI
  obligation, with III.G''s bound: gamma_Ups < min(s_C/2, 1/4)). pi_11 h has no radiation field; F_I,11 = 1 + (E^C u
  (3/2 + (1 - e_Ups) gamma_Ups, 0)): 10.38 (c)'s Coulombic coupling proved for the exterior.
- Findings (C1)-(C6): the simpler structure; the added condition; no radiation field in pi_11; Remark 5.5 holds where
  the cut-off boost is the boost (O(1) change elsewhere near I_0, the source's chi_0 in section 5.6); Corollary 5.15 with
  the perturbation measured from g_0; the product lemma.
- New instrument ext5.py E1-E5: 5/5 pass, 6/6 mutants caught.
- Next: Part III.G''' ([Hin26] Lemma 9.13 on), then III.C' ([Hin26] 5.4-5.7, with Part IV's exterior estimates);
  verifier 101 on III.C and the D241 repairs.

### 4.166 Part III.G''' written: [Hin26] section 9.1.3 at n = 4 (D243)

- Proved, at n = 4: Lemmas 9.13-9.14, Proposition 9.15, (9.49), Remark 9.17, Corollary 9.18, Definition 9.19, Lemma
  9.21, (9.54)-(9.55), Proposition 9.22, Remarks 9.23-9.24 (PART-III-G4-RESONANT.md).
- One exceptional exponent: F_I,11 = 1 + (E^C u (lambda_sharp, 0)), lambda_sharp = 3/2 + (1 - e_Ups) gam_Ups (III.C). The
  least incoming pole of N_iota^-1 on partially polyhomogeneous inputs is lambda_sharp, simple; all others have real part
  above 3/2 + 2 gam_Ups. The source's lambda = 1 pole has no counterpart.
- New proofs of steps the source asserts: the continuation agrees with III.G''s inverse below lambda_sharp (uniqueness
  in III.G's admissible spaces; at lambda_sharp the extension by zero creates delta(v) at the light cone, which is why it
  is a pole); the left inverse behind Lemma 9.21.
- OPEN, for III.J: the pole at lambda_sharp < 2 is excited only by sources with the exceptional term v^(1 + lambda_sharp)
  in the (dx^1)^2-component at I+ cap iota+, which arises exactly when Pi_(2 gam_Ups) h carries a v^lambda_sharp term
  (corrected D245: not from A-bar's (7, 4) entry alone). The record's 10.38 (d) does treat incoming terms below 2 and,
  on its readings, closes this channel (corrected D245: the D243 wording "did not consider" is withdrawn). What is open
  is whether section 12's linear grafting errors (iota+-index set lambda_0 + 2 + E_ind) reach frequency lambda_sharp.
  III.G'''s window condition (least grafted order above 1 + eps) holds for it when eps <= 1/2.
- ext5.py E6-E7 added: 7/7 with controls.
- Next: Part III.G'''' ([Hin26] section 9.2, the tf-normal operator); verifier 101 is reading III.C.

### 4.167 Verifier 101 seated: III.C verified, III.G'' proved (D244)

- Verifier 101 (Opus) read III.C and the D241 repairs to III.G''. No major finding in III.C; four minor and six nits,
  all seated: (m1) Definition 3.3's radiation allowance for pi-slash_0, with a new obligation (C7) for III.C'; (m2)
  A-bar constant in g-bar's null frame, modulo rho_0^2 rho_I^2 C^oo in eta's; (m3) E3's source table named, E5's third
  control (E^C built under the source's analogue condition misses (2, 0), and Proposition 5.2 fails), X7 cross-check;
  (m4) the index condition strengthens the source's and implies its j E^tot condition.
- III.G'': the D241 repairs are correct; one nit, (4.5)'s index set and u's membership, seated. III.G'' is proved.
- III.G''' gains the agreement of the null frames of eta, g_mu and g-bar on iota+.
- ext5.py: 7/7; E5 has three controls.
- Next: verifier 102 on III.G''' and these repairs; Part III.G''''.

### 4.168 Verifier 102 seated: III.G''' verified, III.C proved (D245)

- Verifier 102 (Opus) read III.G''' and the D244 repairs. The two claims asked are proved: lambda_sharp is the least
  incoming pole, simple; the continuation agrees with III.G''s inverse below it. No major finding; four minor and eleven
  nits in III.G''', three nits in the repairs, all seated.
- (m1) the frames on iota+ from III.C Lemma 1.3's proof (|x|^-1 = v/t_* at iota+); (m2) Lemmas 2.3 and 3.4 at finite
  regularity on strips; (m3) the exceptional term comes from a v^lambda_sharp term of Pi_(2 gam_Ups) h; (m4) the record's
  10.38 (d) closes the lambda_sharp channel on its readings; what III.J must settle is whether section 12's linear
  grafting errors reach it (4.166 corrected).
- III.C: (C7) moved into its findings; Remark 4.5 says what exterior5.py X7 computes; ext5.py build() drops the
  redundant 2 E^tot generator; E4-E7 pass.
- Next: Part III.G'''' ([Hin26] section 9.2).

### 4.169 Part III.G'''' written: [Hin26] section 9.2 at n = 4 (D246)

- Proved, at n = 4: (9.57)-(9.61), Definition 9.25, Lemma 9.26, Remarks 9.27-9.28, Definition 9.29, (9.72),
  Proposition 9.30, Remarks 9.31-9.34, Proposition 9.35 (PART-III-G5-TF.md).
- The expansion at r-hat = 0 runs over III.G'' Table 1.1's window (-3, 0] with c_mu = 2 - floor(-mu) companions; the
  functions l_beta come from a merged residue, uniformly across coincidences. The source treats two summands of each
  expansion and calls the rest analogous; here every row is treated.
- Corrected in the source: (9.58) is the operator of 2 L-bar (as III.G''s N_iota+); (9.59) prints rho^(-lambda-j) for
  rho^(-lambda+j); in Proposition 9.35's proof the pointwise inverse leaves an error of the size of a conormal source
  (tfgraft5.py T4), repaired by inverting the dilation-invariant operator on the weight line.
- OPEN, for III.I-III.J: the n = 4 statements need the window w_0 < l_K^max <= 3 (the source: 3 + eps_ind); whether
  sections 11.5-12 at n = 4 need more of it is the spectral counterpart of (G''1). (Corrected D247: D246 said l_zf < 3
  is needed and a larger l_zf would need one more companion; both are withdrawn, verifier 103.)
- tfgraft5.py T1-T4 (new), each with controls.
- Next: verifier 103 on III.G'''' and the D245 repairs; Part III.C' ([Hin26] sections 5.4-5.7).

### 4.170 Verifier 103 seated: III.G'''' verified, III.G''' proved (D247)

- Verifier 103 (Opus) read III.G'''' and the D245 repairs. No major finding in III.G''''; three minor and eight nits,
  all seated. The D245 repairs answer every finding of verifier 102 and are correct; one nit (the count of nits).
- (m1) l_zf < 3 is not needed by Theorem 3.1: for Re alpha_0 <= 2 the window gives it, for Re alpha_0 > 2 Lemma 3.3
  splits l_beta r^(3 + {-mu}) as the source's Case 1; (3.1) drops it, (G''''2) and 4.169 are corrected, tfgraft5.py T3's
  control is relabelled (it tests this proof's bound). Proposition 4.4 keeps (4.2), whose l_zf < 3 is used through the
  bound 3 of its Step 1.2 (iii), removable by the same split and not removed.
- (m2) the term l_(2 - alpha)(|sigma|) G^exc_s1 carries the tf-exponent 2 - alpha: (4.3)'s tf-index set is
  ((alpha_0, k) + E_ind) u ((4, k + 1) + ((0, 0) u E_ind)); the weights are unchanged; the source's (9.74), (9.81) have
  the same imprecision ((G''''7)).
- (m3) integer l_zf: (3.1), (4.2) and Proposition 5.1 now assume l_zf not in N_0, and Lemma 3.4 b + 1 != w_0
  ((G''''8)).
- Nits: III.D Lemma 4.1's ranges; the s1/v1 zf-orders; the form of Proposition 4.4 (2) derived from (4.5); the factor
  |sigma|^(alpha_0 - 2) in Remark 4.5 (2); the cut-offs chi_zf chi_tf in Proposition 5.1's Step 1 and chi^sharp_tf in
  (5.2); Re alpha_0.
- Next: Part III.H ([Hin26] section 10.1 at n = 4); verifier 104 on III.H and the D247 repairs.

### 4.171 Part III.H written: [Hin26] section 10.1 at n = 4 (D248)

- Proved, at n = 4: the cut-off states and their source terms (Lemma 10.4, (10.24)), the augmented zero energy operator
  (Proposition 10.6), the uniform low-energy estimates (Proposition 10.7, through Theorem 4.1, I.C Theorem 6.4 with
  columns depending on sigma), the spectral-side augmentation (section 10.1.3) (PART-III-H-AUGMENT.md).
- At n = 4 the states chi_K g-dot, chi_K (t_* h_s1 + h-breve) need no improvement at iota+ (the source's Lemma 10.3):
  their source terms are O(r^-4) in a cone inside iota+, the naive columns A^3 lie in the target for alpha + 2 in
  (0, 1), and no logarithm enters. The window of weights is (0, 1), not (0, eps_ind).
- Closed: III.F'' section 5's open range. L-hat_b(sigma) is invertible for 0 < |sigma| <= c_0, b near b_0, with c_0
  uniform in b (Corollary 4.3), so [Hin26] Proposition 8.8 holds at n = 4 on a fixed neighbourhood of b_0 (Corollary
  4.4); the source takes this range from [AHW24] Theorem 6.1 (1).
- Corrected in the source: (10.6b) does not give the injectivity of u -> (<u, f*_1>, <u, f*_2>) on the nullspace that
  its proof of Proposition 10.6 uses; a biorthogonal choice of f* gives both ((H2)).
- Next: verifier 104 on III.H and the D247 repairs; Part III.H' ([Hin26] section 10.2, Theorem 10.1 at n = 4).

### 4.172 Verifier 104 seated: III.H verified, III.G'''' proved (D249)

- Verifier 104 (Opus) read III.H and the D247 repairs. No major finding in III.H; two minor and six nits, all seated.
  The D247 repairs are correct and complete; one nit (tfgraft5.py T3's docstring: the control fails (ii) too).
- (m1) uniformity in b: the states are continuous in b only in b-Sobolev spaces below their weights, so the bounds of
  Lemmas 2.2-2.4 hold uniformly with a loss delta (Remark 2.6, new); Corollary 4.2 and Lemma 5.2 now take
  eps_0 = (1 - (alpha + 2))/4 = delta, which keeps (A1)-(A3).
- (m2) Theorem 4.1 (3): R(sigma) F_i(sigma) has a sigma-dependent argument; Banach-Steinhaus on the strongly continuous
  R^(i)(sigma), (A4) in norm and the Leibniz rule give M(sigma) and M(sigma)^-1 in C^j.
- Nits: renames (chi_c for the cone cut-off, kappa for Lemma 2.3's constants, Sigma' for Theorem 4.1's set); (2.4) and
  (A2) for |sigma| <= varsigma_1; (H2) strengthened: under (10.6a)-(10.6b) alone the source's Proposition 10.6 is false
  (off-diagonal blocks e, e^T with e isometric give a kernel); Lemma 2.2 (a)'s sharper set; Proposition 3.2 at every
  constant s > 1/2 + theta_L; "smooth on X" with only conormality at dX.
- Next: Part III.H' ([Hin26] section 10.2, Theorem 10.1 at n = 4); verifier 105 on III.H' and the D249 repairs.

### 4.173 Part III.H' written: [Hin26] Theorem 10.1 at n = 4 (D250)

- PART-III-H2-ADMISS.md: the 2-admissibility of L_b at n = 4, for alpha_sf + 2 in (0, 1), margin 1, sf-loss 0
  (Theorem 1.3), by the source's section 10.2: contour representation (Lemma 2.1), high frequencies at the weight
  alpha_sf + 1 (Lemma 3.1), the regular low-frequency part at regularity s + 1 (Lemma 4.1), the zero energy
  contributions through their t_*-derivatives (Lemma 5.1) integrated twice (Lemma 6.2).
- The loss: at n = 3 the derivatives of the singular terms have sf-weights -1/2 - eps and 1/2 - eps; at n = 4, with
  III.H's cone cut-off, below 0 and 1 with rapid decay at scf, room for alpha_sf + 1 and alpha_sf + 2 ((H'1)).
- Corrected in the source ((H'2)): with alpha_K = -2 and margin 1, II.C Definition 2.4 (6) gives
  s + alpha_sf > (-1 + theta_in)/2 - 1 at the incoming radial set, one short of what Lemmas 10.9-10.10 use at weight
  alpha_sf and regularity s; Remark 10.2 checks only the outgoing set, and without alpha_K. Repaired by the shifts above.
- (H'3) the neighbourhood of b_0 depends on k (strong trapping only at b_0, III.F Proposition 4.1); (H'4) the orders
  need (C1)-(C3) beyond Definition 2.4 for Part I to apply; (H'5) bounded frequencies by I.A Theorem 7.2 (6);
  (H'6) the variable-order step of Lemma 10.13 needs a translation-invariant parametrix localized near the diagonal
  (Lemma 6.1).
- OPEN, for the part applying II.C Definition 2.7 ([Hin26c] Theorem 11.1, [Hin26] section 11 at n = 4): orders in O_c,
  k <= K on B_K for b != b_0 ((H'7)).
- Next: verifier 105 on III.H' and the D249 repairs; then Part III.I ([Hin26] section 11 at n = 4).

### 4.174 Part III.I written: [Hin26] section 11.1 at n = 4 (D251)

- PART-III-I-CONE.md: Definition 11.3 at n = 4 ((2,0) in E_+, min Re E_+ > 1), Lemma 11.5 (no gam_Ups restriction on
  l_I), Proposition 11.6 (constant A-bar, the h-terms in the error, as III.C (C1)), Proposition 11.8, Corollary 11.9 (the
  patched background's curvature at rho_+^4), Corollary 11.10 with p_0 = p~_1 = 0, Theorem 11.12 at b_0 with sf-loss 0,
  beta_+ in (1/2, 3/2), beta_I in (beta_+, 3/2).
- III.H' (H'7) met: II.C Proposition 5.1's construction of orders lies in O_c (Lemma 5.1), once eps_iota also satisfies
  2/(eps_iota delta) >= r_2 - delta_0; the relaxed margin enters by II.F' Remark 7.1 and II.F Remark 8.2.
- OPEN ((I3)): Theorem 11.12 for b != b_0 needs (a) 2-admissibility of L_b for all k near b_0 (strong trapping
  admissibility near b_0, or a finite-k Nash-Moser), and (b) II.F' Theorem 1.1 uniformly in the stationary model
  ((F'11)). [Hin26] section 11.6 on varies b.
- OPEN ((I5)): the weights (a_I, a_+, a_K) of the iteration at n = 4, for the parts writing sections 11.2-11.8.
- Next: seat verifier 105 (III.H' and the D249 repairs); then Part III.I' ([Hin26] section 11.2 at n = 4).

### 4.175 Verifier 105 seated: III.H' verified, III.H proved (D252)

- Verifier 105 (Opus) read III.H' and the D249 repairs. No major finding in III.H'; three minor and nine nits, all
  seated. (H'2), the incoming-threshold gap in the source, confirmed against [Hin26c] (5.20): real. The D249 repairs are
  correct; one citation nit (III.H Remark 2.6 now cites III.D'' Lemma 2.2 for h, h-breve).
- (m1) bounded frequencies: I.A Theorem 7.2 (6) is uniform only for orders fixed near each point; the induced orders are
  frozen on finitely many intervals, at a cost 2 eps in the weight of u_hi ((3.1) at alpha_sf + 1 - 2 eps).
- (m2) Lemma 6.1 without b-regularity (variable-order commutators carry log factors); Lemma 6.2 reduces to k = 0 first.
- (m3) Lemma 6.2 near r = r_0: cut-off in r, constant order there (II.C Definition 2.4 (3)), Seeley extension in x.
- Nits: (C2) implied by Definition 2.4 (3) (so III.I Lemma 5.1 needs no extra condition on eps_iota, corrected there);
  the transfer of (C3) to P; I.C's J_pm used off the real axis only; c <= varsigma_1 fixed in section 2; III.H Lemma 2.5
  (d)'s proof for higher derivatives; II.A (S7) for the uniform equivalence; the kernel-range count; O_c a restriction.
- Next: verifier 106 on III.I and the D252 repairs; then Part III.I' ([Hin26] section 11.2 at n = 4).

### 4.176 Part III.I' written: [Hin26] section 11.2 at n = 4 (D253)

- PART-III-I2-SCRI.md: Lemma 1.1 (the structure at scri+: leading part (X_+ - X_I)(X_I - 3/2 - A-bar) with the constant
  A-bar for the dynamical operator, error in rho_I C^infty + H^{(E^tot_I - 1, a_I - 1),(E_+, a_+)} Diff^2), Proposition
  2.1 and Lemma 2.2 ([Hin26] Proposition 11.14, Lemma 11.15: partial polyhomogeneity at scri+ without loss at iota+,
  for l_+ < l_I < l_I^max, l_I not in 3/2 + sigma_Ups), Proposition 3.1 ([Hin26] Proposition 11.16: formal solutions,
  one exceptional term 5/2 + (1 - e_Ups) gam_Ups solved with factor -(1 + e_Ups) gam_Ups).
- (I'1): no radiation coupling into the 11-component at n = 4 (the h-dependent (A^h)_{7,6} is half an order lower);
  this proves in the forward cone N1STAR-PROOF.md 10.44's reading of the iteration's iota+ index set.
- (I'2): the upper weight is l_I^max = 3/2 + (1 - e_C)(1 - v_C) gam_C (> 100), where the source writes 3 + eps_I; the
  exclusion l_I not in 3/2 + sigma_Ups is stated, which the source's Proposition 11.14 leaves implicit.
- (I'3): the windows of (3.2) start at min Re E^C_I and step by 1.
- Next: seat verifier 106 (III.I and the D252 repairs); verifier 107 on III.I'; then Part III.I'' ([Hin26] section
  11.3 at n = 4).

### 4.177 Verifier 106 seated: III.I verified, III.H' repairs re-read (D254)

- Verifier 106 (Opus) read III.I and the D252 repairs. III.I: one major, two minor findings, eight nits, all seated.
- (M1) Proposition 4.1: the products need l_I < a_I + 1/2 at scri+ (a coefficient remainder of weight a_I acting on
  the radiation term rho_I^(3/2)) and l_+ < a_+ + min Re E_+ at iota+, and (4.2) l_+ <= max(a_+, min Re E_+). Now
  hypotheses; Corollary 4.2 (l = a) lies inside them. The source's Proposition 11.8 has the same restriction at n = 3
  (l_I < 3 + eps_I): recorded as (I6), carried by Remark 5.5 to the later parts.
- (m1) smallness: III.C Proposition 4.4's Neumann series needs H^k-smallness; replaced by a finite Taylor expansion of
  (g_b + delta)^(-1) with a Moser remainder of large weight, under H^3-smallness, constants depending on a bound for
  ||h||_(X^k). (m2) Lemma 3.1 stated on {rho_I <= C}, K+ separately.
- Nits: Lemma 2.2 for k >= 3 and with a_I below the index sets; the K+ frame; Lemma 3.6's second alternative; G+ in
  Proposition 4.1; (11.17b) not carried; the footnote 103 notation; Sigma^- by evenness; Lemma 4.3's support
  supp chi_K cap supp(1 - chi_K); the source's (11.23) K+-weights -2, 0 against (11.21)-(11.22)'s 1/2, -3/2 (read at
  source).
- III.H' D252 repairs: correct, except (m1) residual: a frozen order need not be admissible at nearby sigma, (C3) not
  being quantitative. Repaired by the induced orders themselves (I.A Theorem 7.2 (1) for continuous families, (7.3) by
  the chain of I.A section 7.1, the inverse bound by contradiction, (7.6) by the product formula). Lemma 1.2 (c)'s
  'near it' dropped (on the real axis sigma/|sigma| = +-1). Nits: Lemma 5.1's k; Lemma 6.2's constancy over
  {r <= r_0 + delta_1}.
- Next: verifier 107 on III.I' and the D254 repairs; Part III.I'' ([Hin26] section 11.3 at n = 4).

### 4.178 Part III.I'' written: [Hin26] section 11.3 at n = 4 (D255)

- PART-III-I3-ALMOST.md: Lemma 2.1 ([Hin26] Lemma 11.18: integration of d_t* by III.A Lemmas 3.2 and 1.2 in three
  charts, the third (2 - t_*)^(-1), (2 - t_*)/r covering {t_* < 2}); Lemma 3.1 (Lemma 11.19: the moment condition via
  II.G' Proposition 2.8 (2)); Lemmas 4.1-4.3 (high and bounded frequencies by II.G' Corollaries 4.2 (2) and 4.5;
  low frequencies of the augmented operator in b-spaces, II.G' Proposition 4.7's proof with III.H Corollary 4.2 and
  Theorem 4.1 (3); the cut-off states' transforms in X_sc-b); Proposition 5.1 ([Hin26] Proposition 11.17) at b_0.
- (I''1): the iota+-weight stays at min(alpha_+, 3/2, min Re E_+) - eps for every K+-weight alpha_K - 2, alpha_K in
  [1/2, 1); the source's falls to alpha_K - eps. The singular part's first integration takes beta_iota from the a
  priori bound on {t_* < 1}, not from its transform, whose tf-order is one higher at n = 4.
- (I''2): the window gamma_+ - alpha~_K in (0, 1), the exact gap (III.F' Proposition 2.3 (a)), for the source's
  (0, eps_ind). (I''3): Lemma 11.19 needs beta_K > -1 (for (2.26a)), unstated in the source. (I''4): 2 <= l_I <
  a_I + 1/2.
- Next: seat verifier 107 (III.I' and D254); verifier 108 on III.I''; then Part III.I''' ([Hin26] section 11.4 at
  n = 4).

### 4.179 Verifier 107 seated: III.I' verified, III.H' proved (D256)

- Verifier 107 (Opus) read III.I' and the D254 repairs. III.I': three major, two minor findings, eight nits, all
  seated.
- (M1) Proposition 2.1 / Lemma 2.2 Step 3: the third product inequality (the coefficient's remainder at a_I - 1
  against u's least exponent 3/2) caps l_I < a_I + 1/2, and at iota+ l_+ < a_+ + min Re E_+; both now hypotheses. The
  source's 3 + eps_I is this product bound at n = 3, not the pi_C-root bound: (I'2) rewritten.
- (M2) Lemma 2.2: alpha_+ < min Re E_+ added. (M3) (3.2) and Proposition 3.1's proof: III.A Lemma 1.2 gives the
  extended union, so E^sharp is built with bar-cup taken k + 1 times; the source's (11.33) has the same slip, (I'4).
- (m1) l_I > 3/2 in Propositions 2.1 and 3.1; (m2) l_+ not in Re pi_1 E^tot_I in Proposition 2.1. Nits: U_I closed
  at iota+, Lemma 1.2's a priori region, the clean split at z_1, integer shifts for L_b, the windows mu_j, the source's
  missing exclusion, alpha_I + eta off 3/2 + spec A-bar, two automatic conditions removed.
- D254 repairs: correct, except III.I Lemma 3.6's reason (now III.B Lemma 5.2's second alternative) and two nits (the
  inverse metric's H^k part is (g_b + delta)^(-1) - g_b^(-1); (11.23)'s pairing). III.H' repairs correct, one nit (the
  raised orders of the product formula): III.H' is proved. III.I'' (written D255) uses Proposition 2.1 inside the new
  range (l_I in [2, min(a_I + 1/2, l_I^max)), iota+ weights below 3/2); its two citations now say so.
- Next: verifier 108 on III.I'' and the D256 repairs; Part III.I''' ([Hin26] section 11.4 at n = 4).

### 4.180 Part III.I''' written: [Hin26] section 11.4.1 at n = 4 (D257)

- PART-III-I4-BOOST.md: Lemma 1.1 (sigma-independent profiles on X_sc-b, by Fubini), Lemma 1.2 ([Hin26] Lemma 11.21:
  L-hat_b(sigma) - L-hat_b(0) on chi_zf u_0, and the columns f-hat(sigma) - chi_zf f-hat(0) of tf-order 3 - eps), Lemma
  1.3 (the cut-off states near zero energy), Proposition 2.1 ([Hin26] Proposition 11.20 at b_0): u = chi_K
  h^(<=1)(S-dot) + u~, S-dot = S-hat_1(0), u~ of K+-weight alpha_K - 2, for alpha_K in (1, min(a_K - 1, 3/2)).
- (I'''1): no iota+ step (the source's Step 2, its Proposition 9.11 at lam = 1): the formal solution's iota+-index set
  starts at 3/2 + (1 - e_Ups) gam_Ups, above the weight. (I'''2): the iota+-weight min(alpha_+, 3/2, min Re E_+) - eps
  (the source's 1 - eps). (I'''3): the zero energy window (0, 1) (the source's (0, eps_ind)); the columns have
  tf-order 3 - eps (the source's 2 + eps_ind - eps). (I'''4): alpha_K < a_K - 1 from (4.2).
- Noted for verifier 108's seat: III.I'' Step 2b's scf-weight of f-hat^flat is min(l_I + 1, gamma_+ + 2) - eps, not
  gamma_+ + 2 - eps (at least 3 - eps either way, which is all Lemma 4.2 needs).
- Next: seat verifier 108; verifier 109 on III.I'''; Part III.I'''' ([Hin26] section 11.4.2, undoing the boost).

### 4.181 Verifier 108 seated: III.I'' verified; III.I and III.I' proved (D258)

- Verifier 108 on III.I'' (PART-III-I3-ALMOST.md) and the D256 repairs: 0 major, 3 minor, 9 nits on III.I''; the
  D256 repairs to III.I', III.I and III.H' all correct. The iota+-weight min(alpha_+, 3/2, min Re E_+) - eps holds.
- m1: Lemma 3.1 asked F u supported in [-1, 1]; II.G' Proposition 3.5's cut-off is 1 only near [-1/2, 1/2] and
  Definition 2.7 asks regularity across sigma = +-1. Now support in [-c_0, c_0], c_0 < 1/2, which the application
  has; the source's Lemma 11.19 shares the gap ((I''5)).
- m2: c depends on k (and on III.H's weight alpha, which changes with the step); (5.5)-(5.9) hold at order k for that
  c, and H^infinity follows as u, u_I, u^flat do not depend on c.
- m3: continuity in (S, h) needs locally uniform bounds; III.I' Proposition 2.1's proof is constructive, its bound
  depends on L through coefficient norms only (III.I Proposition 3.4), so the scheme's constants are locally uniform.
- Nits: the gap wording ((0, 1] inside the gap; (0, 1) is III.H (1.1)'s window; also in III.I'''), the source's cap 1
  at p. 232 (p. 238 names the transport), (2.25a)'s scf-weight min(l_I + 1, gamma_+ + 2) - eps (also in Step 2b, the
  item noted in 4.180), chart squares across r = r_0 (Seeley extension, cut-off psi(r)), [-1/2, 0), the source's
  (11.49) zf slip, l_+ < a_+ + min Re E_+ listed, density for extendible spaces, c_{j,k'}.
- Next: verifier 109 on III.I''' and the D258 repairs; Part III.I'''' ([Hin26] section 11.4.2, undoing the boost).

### 4.182 Verifier 109 seated: III.I''' verified; III.I'' proved (D259)

- Verifier 109 on III.I''' (PART-III-I4-BOOST.md) and the D258 repairs: 0 major, 3 minor, 7 nits; the D258 repairs
  correct, one not carried to the README (the gap wording). Confirmed: no iota+ step, the window (0, 1) inside the
  gap, the K+-range (1, min(a_K - 1, 3/2)), S-dot = S-hat_1(0) the coefficient of t_* at K+.
- M1: Step 4's a priori weight could exceed min Re E_+; now l_+ := min(l'_+, min Re E_+ - eps), off Re pi_1 E_+.
- M2: the support of F v is a compact subset of (-c, c), c <= 1/2, as III.I'' Lemma 3.1 now asks.
- M3: c fixed per order k, as in III.I'' section 4; S-dot and u~ do not depend on c.
- Nits: alpha#_+ < 7/4 (gamma_Ups < 1/4), the closed graph pointer, the README gap wording, c's k-independent bounds,
  (2.26a)'s cut-off, III.H Lemma 2.5 (d) "and its proof", (I'''4)'s "suffices".
- Next: Part III.I'''' ([Hin26] section 11.4.2, undoing the boost); verifier 110 on it and these repairs.

### 4.183 Part III.I'''' written: [Hin26] section 11.4.2 at n = 4 (D260)

- PART-III-I5-UNBOOST.md: the re-centred state h^(<=1)_nat = h^(<=1) - C' h (Lemma 1.2); the correction terms
  h^(-1), theta^(-1), theta_sharp (Definition 2.1; Lemma 2.2 = 11.24: (2,0) u (2 + E_ind) at iota+, no log); P_1 in
  the form of the source's Remark 11.27 (Definition 2.3; Lemma 2.5: L_{h,S} = L^{g',g_0}, h' = h^(-1)(S) + h, so
  III.I-III.I''' apply); the boost identity (Lemma 2.4 = (11.76)-(11.78b), exact with III.B's cut-off factor Theta);
  Lemma 3.1 (the S-derivative of the operator family maps as III.I (4.1)-(4.2)); Lemma 3.2 (= 11.28: iota+-order 4,
  I+-data (<E^C_I + 1>', a_I + 1)); Lemma 4.2 (S-dot = Pi(f - (L - L_b0)u), Pi fixed by L_b0: bounded, continuous
  in the operator); Proposition 4.1 (= 11.30) and Corollary 4.3 (= (11.95)).
- (I''''1) the time origin: t-bar - t = C' - 8 mu_0/|x|; without re-centring h^(-1) has an iota+-order 1 term.
  (I''''2) no logarithms. (I''''3) no splitting of the source term (order 4 at iota+, the source's 3). (I''''4) the
  form of P_1. (I''''5) a_I >= 2. (I''''6) the two one-line steps of the source written out.
- Requirement: 2 + E_ind in E_+ ((2.4), the source's 1 + E_ind in E_+).
- Next: verifier 110 on III.I'''' and the D259 repairs; then [Hin26] section 11.5 (almost boundedness) as III.I'''''.

### 4.184 Verifier 110 seated: III.I'''' verified; III.I''' proved (D261)

- Verifier 110 on III.I'''' (PART-III-I5-UNBOOST.md) and the D259 repairs: 0 major, 2 minor, 9 nits; the D259 repairs
  correct and complete. Confirmed: (2.3) exact with signs, Theta and the counterterm; the C' term of Lemma 1.2 is there
  (iota+-order 1); L_{h,S} = L^{g',g_0} and h^(-1) in X; Lemma 3.2's counts; S-dot = Pi(f - (L - L_b0)u); invertibility.
- m1: Lemma 4.2 (b) needs room l_I > 2; stated for l_I > 2 or f vanishing near I+ (then any l''_I > 2 serves, S-dot
  being determined by u), which is how Proposition 4.1 (2) uses it (f_00 is supported in C).
- m2: Lemma 3.1's proof said the C^infinity error does not depend on S; now the background difference k_S in K is
  counted with the perturbation, as in III.I Proposition 3.4's proof.
- Nits: (ii) derived from III.B's Upsilon^0 formula; III.B (3.5), Proposition 3.6 for g_b0 - eta; (Dyn) recorded; E_ind
  of (2.4) fixed; Corollary 4.2 dropped from Lemma 2.5's list; (3.3) without the bullet; "polynomial" qualified; d's
  size in Lemma 4.2 (b); t^flat_* in the closing remark; III.I''' Step 4's "eps chosen" made automatic.
- Next: Part III.I''''' ([Hin26] section 11.5) is written (D262); verifier 111 on it and these repairs.

### 4.185 Part III.I''''' written: [Hin26] section 11.5 at n = 4 (D262)

- PART-III-I6-ALMOSTBDD.md: Proposition 2.1 (= 11.32): with S-dot(f) = 0, u has K+-weight alpha_K - 2 for every
  alpha_K < 2 and iota+-weight min(alpha_+, 3/2, min Re E_+) - eps. Corollary 2.2: the solutions of (11.95).
- Proof: rounds raising the K+-weight by a_K - 2; each round is III.I''''s Steps 0-4 with S_0 = 0 (forced, as u has
  K+-weight > -1), plus a step at iota+ when alpha#_+ >= lam_sharp = 3/2 + (1 - e_Ups) gam_Ups: III.G'' Corollary 4.3
  (l_0 = 0, spec_iota+ in Re >= 2) on the finitely many exponents of E^sharp_+ below alpha#_+, the I+-errors re-solved by
  III.I' Proposition 3.1 with no exponent below 5/2 created (its last sentence), so each round raises the least
  exponent by eps_ind and finitely many end it.
- (I'''''1) the weights; (I'''''2) the step at iota+ starts at lam_sharp, not at 1, with no pole and no logarithm;
  (I'''''3) no Lemma 11.33, no expansion (11.107b), no Step 3.2 (Proposition 9.30): no indicial root in (0, 1], columns
  of tf-order 3 - eps.
- Next: verifier 111; then [Hin26] section 11.6 (black hole parameters) as III.I''''''.

### 4.186 Verifier 111 seated: III.I''''' verified; III.I'''' proved (D263)

- Verifier 111 on III.I''''' (PART-III-I6-ALMOSTBDD.md) and the D261 repairs: 0 major, 2 minor, 9 nits; the D261
  repairs correct, one incomplete (a stale input, now dropped). Confirmed: termination of the iota+ iteration; no
  exponent below 5/2 from re-solving at I+; l_0 = 0; S_0 = 0; every use of alpha_K < 3/2 in III.I'''.
- m1: l_K was fixed once, which holds in the first round only: later coefficients come from III.G'' Corollary 4.3's
  error, which does not vanish near K+. Now the K+-order c_K in (2, lam_sharp + 1) is fixed and l_K(lam_0) := c_K -
  Re lam_0 in (0, 1), as the source does in (11.102); errors have K+-weight c_K - eps > 2.
- m2: alpha#_+ is kept off Re(E#_+ + N_0 E^iota_ind), so no created exponent sits at alpha#_+.
- Nits: E^tot closure +N_0; the two index sets named E_ind separated (E^iota_ind, eps_ind defined); min Re E^gr_K
  >= Re lam_0 - 1 with the reason; III.C Lemma 3.2 (a) and the eigencomponent-to-slot change; tilde alpha_K >=
  alpha'_K; three more uses of alpha_K listed; chi^H_K; status D262; III.I'''' Proposition 4.1 (1) needs no l_I <= a_I.
- Next: verifier 112 on III.I'''''' and these repairs.

### 4.187 Part III.I'''''' written: [Hin26] section 11.6.1 at n = 4 (D264)

- PART-III-I7-PARAMS.md: Proposition 2.1 (= 11.34): alpha_K in (2, min(a_K, 2 + eps_ind, 5/2)), f real with
  S-dot(f) = 0: u = chi_K g-dot(b-dot) + chi_K h(S^(0)_1) + u-tilde, u-tilde of K+-weight alpha_K - 2 > 0.
- Lemmas: 1.1 first-order zf expansions; 1.2 conormal sections lie in X_sigma for an admissible order lowered near the
  zero section; 1.3 row data answered by w_e = chi_zf(g-dot(e_1) + h(e_2)); 1.4 the term |sigma|^(alpha-3) h(S') of
  III.G'''' Proposition 5.1 moved into the S_1-column exactly.
- Proof: Steps 1-2 of III.I''''' with alpha#_+ = 2 - eps and c_K in (alpha_K, lam_sharp + 1); zero energy (2.25a), the
  tf-improvement by III.G'''' Proposition 5.1 (the source's Proposition 9.35), a second inversion at relative order
  eps_ind - 2 eps, the low-energy estimate; one integration in t_*; matching b-dot and S^(0)_1; reality.
- (I''''''1) no logarithmic centre-of-mass term; (I''''''2) the boost-type term at tf; (I''''''3) Proposition 9.30 not
  needed, 9.35 needed; (I''''''4) conormal admissibility.
- Next: verifier 112; then [Hin26] section 11.6.2 (Definition 11.37 onward) as III.I'''''''.

### 4.188 Part III.I''''''' written: [Hin26] section 11.6.2 at n = 4 (D265)

- PART-III-I8-UNPARAM.md: parameters p = (S, b - b_0, S^(0)_1) (no logarithmic centre-of-mass parameter); corrections
  h^(0)(b-dot) = -dchi_K x omega-dot, h^(0)_s1(S) = -dchi_K x (omega_s1 - Theta w^0), gauge terms with the Remark 11.27
  counterterms; P_2 = Ric(g') - delta^*(Upsilon(g', g_0) - theta_tot); identities D_p P_2(0,0) = L_b0(chi_K state) for
  the boost, the Myers-Perry parameters and the centre of mass, all exact.
- Finding (I'''''''1): the source's centre-of-mass correction -dchi_K x omega_s1 has iota+-order 1, outside X at
  n = 4 (min Re E_+ > 1); the exterior background is translated, as it is boosted: g_p = (1 - chi_K)(psi_{-S0} o
  phi_{-S})^* g_b0 + chi_K g_b. III.B (5.3) holds for the composite with the same leading term (the translation
  difference is |x|^-3), so III.I Lemma 3.6 and everything after it hold; the correction becomes order 3. The parts
  writing (11.90), Definition 11.63 and Corollary 11.66 must carry the translation in the initial data.
- Elimination: Lemma 4.1 (parameters near the base point, by L_b0(u_j - u) = F_j - F - (L_j - L_b0)u_j and the
  uniqueness of the asymptotic parameters); Lemma 4.3 (= 11.43), Lemma 4.5 (= 11.45, close to -id), Corollary 4.6
  (= 11.46): u in H^{(<E^C_I>, l_I), beta_+, alpha_K - 2}, decaying at K+. Base points at b = b_0 (III.I Remark 5.4).
- Next: verifier 112's report on III.I'''''' (in hand); then verifier 113 on III.I''''''' and the D266 repairs.

### 4.189 Verifier 112 seated: III.I'''''' verified; III.I''''' proved (D266)

- Verifier 112 on III.I'''''' (PART-III-I7-PARAMS.md) and the D263 repairs: 0 major, 3 minor, 8 nits; the D263 repairs
  correct and complete but for a literal "\n\n" in III.I''''' (now a paragraph break) and a doubled III.G' label.
  Confirmed: Lemmas 1.1, 1.3, 1.4; Steps 0-6; the matching; b-dot = b-dot_0, S^(0)_1 = i S-hat_4; Steps 1-2 with c_K.
- m1: Lemma 1.2 said the zero section is elliptic for sigma != 0; it is R_out, a radial set in the characteristic set.
  Now the order is lowered near R_out (only an upper threshold applies there; I.A Lemma 7.1's construction), L-hat
  maps A^a to A^(a+1), and the inverses agree as kernels do not depend on the admissible order (I.A Theorem 7.2 (5)).
- m2: reality now from the real solution: the imaginary parts of b-dot, S-dot give a stationary tensor of positive
  K+-weight, hence zero.
- m3: (2.2) is for one fixed eps; b-dot and S-dot are the K+-limit of u, so they and u-tilde do not depend on eps.
- Nits: Lemma 1.4's tf-weight alpha - eps and the h-breve term near zf cap tf (III.G'''' Lemma 4.3); chi^H_K; the -mu
  set real and discrete; the distributional identity (2.10) before the matching; the source's second class f_2; c from
  III.I''' section 1; the sign of a_s1 dropped.
- Next: verifier 113 on III.I''''''' and these repairs; then [Hin26] section 11.7 as III.I''''''''.

### 4.190 Part III.I'''''''' written: [Hin26] section 11.7 at n = 4 (D267)

- PART-III-I9-COMMOTION.md: decaying centre-of-mass motions chi_K t_*^(-lam+1) (log t_*)^k h(S), (lam, k) in the
  index set M = E_++ cap {Re < 2}, Re lam in [lam_sharp, 2); E_++ fixed in advance (contains E#_+ below 2, closed under
  + E^iota_ind, E_ind, E_+, inside E_+).
- Corrections #3: h^(lam-1,k)_s1 = -dchi_K x omega^{<=4}(a S), theta^(lam-1,k)_s1 = delta G (chi_K delta^* omega^{<=4}),
  omega^{<=4}(a S) = sum a^(i) omega-breve^i with the generalised gauge 1-forms of III.D''' to order 4; the gauge term
  decays to K+-order Re lam + 4; the identity D P_3(0,0)(S) = L_b0(m(S)) is exact.
- Expansion at a level (Lemma 3.2): Steps 1-2 of III.I''''' with c_K = alpha, so the s1 row of III.G'' Corollary 4.3
  appears exactly when Re lam - 1 < alpha - 2 and gives the motions; zero energy as III.I'''''' with a tf-iteration
  (III.G'''' Proposition 5.1 repeated, the s1 terms moved into the S_1-column) for alpha >= 2 + eps_ind.
- Proposition 4.1 (= 11.51): induction over admissible levels; each level a finite-dimensional map close to the
  identity; u has K+-weight alpha - 2 - eps for every admissible alpha < min(a_K, 3).
- Findings (I''''''''1)-(I''''''''5): motions extracted on spacetime (no zero-energy motions at n = 4); no logarithm
  proliferation, no u_Sigma; the tf-iteration; assumptions on E_+; origin at lam_sharp.
- Next: verifier 114 on III.I'''''''' and the D268 repairs.

### 4.191 Verifier 113 seated: III.I''''''' verified; III.I'''''' proved (D268)

- Verifier 113 on III.I''''''' (PART-III-I8-UNPARAM.md) and the D266 repairs: 0 major, 2 minor, 7 nits; the D266 repairs
  correct and complete but for a stale sentence at Lemma 1.2's use site (now X'_sigma). Confirmed: the iota+-order 1 of
  the source's centre-of-mass correction, the translated background, Lemma 2.2's orders, (2.3) sign by sign, f^b near K+,
  Lemmas 4.3, 4.5 (close to -id), Corollary 4.6.
- m1: Lemma 2.5 (c)'s uniformity now also covers III.I' Proposition 2.1 applied to L (constructive, bounds through
  coefficient norms, III.I'' Proposition 5.1's continuity paragraph).
- m2: Lemma 4.1 counted order-2 terms at iota+-weight 2 - eps, beyond (4.2)'s hypothesis; now at min(2 - eps,
  max(a_+, min Re E_+)) > 1, which still suffices as l_+ + m_+ > 2.
- Nits: Lemma 11.38 vs (11.140); "accepts"; the |x|^-3 inclusion cited from III.B; Lemma 4.3 also uses (c); the sign
  of Lemma 11.45 recorded; a vacuous intersection dropped; "would not apply as stated".
- Next: verifier 114 on III.I'''''''' and these repairs; then [Hin26] section 11.8 as III.I'''''''''.

### 4.192 Verifier 114 seated: III.I'''''''' verified; III.I''''''' proved (D269)

- Verifier 114 on III.I'''''''' (PART-III-I9-COMMOTION.md) and the D268 repairs: 0 major, 2 minor, 7 nits; the D268
  repairs correct. Confirmed: motions only from the s1 row of III.G'' Corollary 4.3 when alpha - Re lambda_0 > 1, none
  from zero energy; E_++ closed, no new logarithms; (2.1) from III.D''' (1.3); Lemma 2.4 exact; Step 3.4' and (3.3);
  Steps 6-7; Lemma 3.3; the induction of Proposition 4.1 (T_{0,0} = id, uniqueness, continuity).
- m1: Lemma 3.1's Step 0 needed a_K > alpha_0 + 2 - lambda_sharp; now the iota+-terms of F_2 are extracted first
  (u_F, by Step 2), and III.I''''' Proposition 2.1 applies to u - u_F with every alpha_+ < 2.
- m2: Lemma 2.6 (a) now counts (d delta*_{g_0,E_C}) theta_mot, of iota+-order >= Re lambda + 4 and K+-weight
  Re lambda + 4 - eps > 3, in Y_1(alpha).
- Nits: E_ind enlarged by III.D''' Proposition 3.1 (2)'s index sets; E_+ + (E^iota_ind u E_ind u E_+) in E_+ in (1.1)'s
  example and (I''''''''4); the product index set in Lemma 2.6 (b); III.I' Proposition 2.1 in Step 8's list;
  complex exponents (conjugation-symmetric motion parameters); eps_ind < 1 for the tf-iteration; Y_2 for h in X^infty.
- Next: Part III.I''''''''' ([Hin26] section 11.8.1-11.8.2); verifier 115 on it and these repairs.

### 4.193 Part III.I''''''''' written: corrections #4 and the operator P_4 (D270)

- PART-III-I10-CORR4.md: [Hin26] section 11.8 to Lemma 11.57 at n = 4. Rows of six types: s1 (rate lambda - 1), v1,
  s0, s2 (rate lambda) and the class roots c0, c1 (rate lambda + d, 0 < d < 1). No exponent 1 at n = 4, so none of the
  source's logarithmic or lambda = 1 parameters, and no s3 or v2 rows (rate above 5/2).
- Gauge towers from III.D''' of lengths 4, 3, 4, 3, 2, 2; every counterterm has K+-order kappa_nu > 9/2 + delta_sharp.
- Lemma 2.6: f^nu = L_{h,p} m_nu + r^nu exactly; r^nu vanishes at (0,0) and has iota+-weight 2 lambda_sharp + 2 - eps
  > 5 + eps_+ with no index set, K+-weight above 4 + eps_K; f^S, f^b, f^s1 lie in Y(alpha) for alpha <= 4 + eps_K.
- Hypotheses: (H1) a_+ > lambda_sharp and E_+ in {Re >= lambda_sharp}; (H2) a_K >= 4 + eps_K; (H3) the index sets of
  the corrections in E_+. E_par and E_src are fixed by Part III.I'''''''''' within (1.2)-(1.3).
- Next: Part III.I'''''''''' (Theorem 11.59 at n = 4); verifier 115 on III.I''''''''' and the D269 repairs.

### 4.194 Verifier 115 seated: III.I''''''''' verified; III.I'''''''' proved (D271)

- Verifier 115 on III.I''''''''' (PART-III-I10-CORR4.md) and the D269 repairs: 0 major, 2 minor, 7 nits; the D269
  repairs correct except one residue (S in S_{1,C} in III.I'''''''' Lemma 2.4), now seated. Confirmed: the six rows and
  the exclusions; the tower lengths and (2.1); Lemma 2.2 (a)-(f) with kappa_nu and the antiderivative A_nu (whose
  (-1)^k the source's (11.190) omits); Lemma 2.4; (2.4) and both weights of (2.5); the source classes.
- m1: E_ind now also holds the index sets of III.D''' Proposition 3.1 (1), (3), (4)-(7) at b_0 and (2,0).
- m2: finding (I'''''''''5) now says the strong K+-decay of h is needed also for r^nu (a_K > alpha + 1 - lambda_sharp).
- Nits: the excluded rows worded by their rates; (2,0)+F in (2.1); footnote 125's j = 3 for s0; at b_0 = (mu_0,0)
  every rotation is Killing, so V' = 0 and the v1 rows carry no parameter; complex W; the (11.194) comparison worded
  as its L_b form; III.G'''' Proposition 5.1, III.B and II.E in the lists; delta_sharp in (0,1/4) from III.C (1.1).
- Next: Part III.I'''''''''' (Theorem 11.59 at n = 4, the spectral cascade); design notes in the D270 scratchpad.

### 4.195 Part III.I'''''''''' written (D272): Theorem 11.59 at n = 4, first half

- PART-III-I11-SPACETIME.md: the parameter exponents fixed (Lambda generated by E_++, G, E^C_I, lambda_sharp, 3 and
  closed under + E_ind, + E^iota_ind, + 1; log orders K(lambda) growing with the real part); E_par independent of E_+
  beyond E_++, so (H3) is consistent (the n = 4 Remark 11.62); the gap (G) on eps_K; admissible orders.
- Toolkit: III.G'' towers are the delta*-images of III.D''' 1-form towers, and differ from m_nu at K+-rate >= the
  row's rate + 3 (Lemma 2.1); joint injectivity of the states by spherical degree and order at the boundary (Lemma 2.2,
  Corollary 2.3); forward Fourier tails: a forward-supported function's K+-tail is read off its sigma > 0 side, log-free
  integer-degree pieces give none, and III.A Proposition 4.2's matching (4.4) holds (Lemma 2.4).
- Proposition 3.1: III.I''''' Steps 1-2 with c_K = alpha <= 4 + eps_K (C5 gives ell_K < 3), the I+-step to 3 + eps_+
  (H4), the K+-terms below alpha - 2 identified as the rows N_iota (Re lambda < 2).
- Design: the iota+-terms of u-exponent >= 2 stay spectral (re-solves at I+ create E^C_I-exponents >= 5/2 that a
  spacetime treatment would revisit); the spectral cascade (Taylor levels 0-3, zero energy at each, III.G'''' Prop 4.4
  at levels 1-2, Prop 5.1 at level 3, the s1-column moves, forward tails) and the elimination are III.I'''''''''''.
- Next: verifier 116 on III.I'''''''''' and the D271 repairs; then III.I'''''''''''.

### 4.196 Part III.I''''''''''' written (D273): Theorem 11.59 at n = 4, second half, and (11.222)

- PART-III-I12-SPECTRAL.md: the spectral phase. At n = 4 the zf-Taylor expansion of the transformed source has four
  terms (alpha - 1 > 3), so four zero-energy solves (levels 0-3), each with its expansion at dX (III.A Lemma 1.4; the
  root 2 is the mass); III.G'''' Proposition 4.4 at levels 1-2 for the polyhomogeneous tf-terms, Proposition 5.1 at
  level 3 for the conormal ones, and III.I'' Lemma 4.2 for the rest.
- Lemma 2.5: the low-energy resolvent is written as a sum of physical pieces (L-hat injective on X'_sigma), so the
  augmented system is inverted only at zero energy and at the last level; no row corrections or column moves.
- Lemma 2.3: Proposition 4.4's output in compact sets is a homogeneous function of sigma times the spectral towers plus
  log-free integer-degree pieces; III.I'''''''''' Lemma 2.4 turns the former into the rows N_sigma (s1 at
  2 <= Re lambda <= 3, s0 and s2 at Re lambda = 2) and the latter into nothing. The stationary columns vanish by decay.
- Lemma 3.2 (the expansion) and Theorem 4.1: the elimination from an admissible alpha' in (2,3), a perturbation of the
  identity (the exact linearisation f^nu = L m_nu + r^nu), = (11.222) at K+ with the plain iota+ weight.
- Next: verifier 117 on III.I''''''''''' (after verifier 116 is seated); then III.I'''''''''''' (Part 4, the iota+
  index set of (11.222), section 11.8.3).

### 4.197 Verifier 116 seated: III.I'''''''''' verified, III.I''''''''' proved; III.I''''''''''' amended (D274)

- Verifier 116 on III.I'''''''''' (PART-III-I11-SPACETIME.md) and the D271 repairs: 1 major, 3 minor, 7 nits; the D271
  repairs all made and correct, so III.I''''''''' is proved.
- M1: L_0 bounded the log orders of E^0_src and E_++ up to the real part 5; (H3) puts (2,K(2)) into E_+, hence
  (4,K(2)) into E_+ + G inside E^0_src, so L_0 >= K(2) > L_0. Repaired: L_0 bounds the log orders only below
  2 lambda_sharp = 3 + 2 delta_sharp > 3 + eps_+, where nothing involves E_+ (E_++ taken as the least choice); the log
  count (Lemma 1.2 (c)) is stated up to the u-exponent 3 + eps_+, all that the sources and the cascade record.
- m1: E_par closed under +1 (an index set in the sense of [Hin26] Definition 2.7) without changing E_par below 3.
  m2: (H4) asks a_I > 3 + eps_+ (l_I <= a_I is kept from III.I''''''''). m3: the factor (-1)^z in Lemma 2.4's proof.
- Nits: the unused e; the isotypic citation and the degree of breve omega^1_s0; h_s0's index set from III.D''' (3.1);
  m_nu for every triple; the v1 rows of N_sigma; K = L_0 + L_1(n+1); E_I in Lambda only below 3 + eps_+. Also a
  label: h_s1's index set is III.F''' Proposition 4.1 (4.2), not III.F''''.
- Found while seating: the cascade of III.I''''''''''' needs the column terms polyhomogeneous at tf (III.H Lemma 2.4 and
  III.I'''''' Lemma 1.1 (b) give them only conormally, weight 3 - eps, which after two divisions by sigma would cap
  the level-2 source at tf-weight 2 < 2 + eta_2). New Lemma 1.1 there: at b_0 the columns are r^{-3} G(sigma r, x)
  with G polyhomogeneous in x (the cut-off chi_c(r/t_*), the operator and dot g, h, breve h are), index set E_col;
  2 + E_col joins Lambda. Also eta_1, eta_2 < eps_+ and Lemmas 2.1-2.2 to the full remainder order.
- Next: verifier 117 on III.I''''''''''' and the D274 repairs; then III.I'''''''''''' (Part 4, the iota+ index set of
  (11.222), section 11.8.3).

### 4.198 Verifier 117 seated: III.I''''''''''' verified, III.I'''''''''' proved (D275)

- Verifier 117 on III.I''''''''''' (PART-III-I12-SPECTRAL.md) and the D274 repairs: 1 major, 3 minor, 12 nits; the
  D274 repairs (M1, m1-m3, n1-n7 of verifier 116) all made and correct, and the new generator 2 + pi_1 E_col of Lambda
  breaks nothing, so III.I'''''''''' is proved.
- M1: the zero-energy data at levels 1-3 are found for each sign of sigma, and S_1^+ != S_1^- in general (the
    sign-dependent zf-coefficient of III.G'''' Proposition 4.4's remainder); the odd part of sigma h^aug(S_1) is not
  locally integrable. Repaired by a matching step (as in III.I'''''' Step 5 and the source's p. 287 caveat): on d_t v
  the odd
  part is i sgn(sigma) h(S_o) + o(1), whose inverse transform ~ c t^{-1} as t -> -inf, while d_t v is rapidly
  decaying there; so S_o = 0. The other sign-dependent pieces are of integer degree without log and give no tail.
- m1: Step 4 applies Proposition 5.1 with alpha_tau = min(tau, 2 - delta), loops while tau <= 2 + l_3 + eps, and ends
  with tau in (2 + l_3 + eps, 3), so III.I'' Lemma 4.2's beta_tf - beta_zf lies in (0,1). m2: the s1 pieces have degree
  alpha_0 - 3 + j + i. m3: III.I'''''''' Proposition 4.1 is stated for P_3; with h' = h + sum h_nu(W_nu) it holds for
  (L_{h,p}, D_p P_4), the derivatives differing by an O(|W|) term in Y_2(alpha).
- Nits: Lemma 1.1's citation and rho_tf; the sign of i L_1 u; the commutators' index sets; c_tau and P_int at critical
  orders; the towers without their top term; Lemma 2.4's weights through III.A Proposition 4.2 (2); T W = W - S(...);
  the unused condition on alpha'; the fourth Taylor level made explicit rather than new; w_0 + a_K > alpha; the tail
  exponent beta = alpha - 3 - 2 eps; E^flat in Lambda only below 3 + eps_+ (III.I'''''''''').
- Next: III.I'''''''''''' (Part 4: the expansion modulo K+-order 4 + eps_K and the iota+ index set of (11.222));
  verifier 118 on it and the D275 repairs. Design notes in the D274 scratchpad.

### 4.199 Part III.I'''''''''''' written (D276): Theorem 11.59, Part 4, at n = 4

- PART-III-I13-EXPANSION.md: u = chi_K u_exp + u~ (Theorem 3.1), u~ of K+-order alpha - eps and partially
  polyhomogeneous at iota+ with E_sharp = {(lambda,k): lambda in Lambda, k <= K(lambda)} to 3 + eta_2 - 2 eps;
  u_exp = h^{<=1}_{s1}(S_rem) + gdot(b_rem) + sum over the rows of III.G'' Table 1.1 of towers with coefficients in
  Q(E_sharp - d_rho, w_rho); S_rem of order alpha - 2 - eps, b_rem of order alpha - 1 - eps, conormal.
- The iota+ phase already reaches K+-order alpha: the graft's remainder has K+-order lambda_0 + l_K (III.G'' Theorem
  4.2's proof; its statement records only l_K).
- Lemma 2.1: chi_zf(|sigma| r) is an approximate identity with vanishing moments, so each tower-times-scalar piece is the
  spacetime tower of the inverse transform of its scalar, up to terms rapidly decaying at K+. Lemma 2.2: the last-level
  columns give h^{<=1}_{s1}(A) and gdot(B) (the first moments cancel).
- Lemma 2.3: ker L_0 on sections of growth < r^3 is spanned by the Table 1.1 states, gdot, h_s1 and breve h^1_v1; no
  growing boost state, and L_1 gdot(bdot) is not in the range of L_0 there unless bdot = 0 (invertibility of
  tilde L(0) with III.H (2.2)). Lemma 2.4: formal solutions at K+ below the order alpha are towers.
- Why Lemma 2.4: the source argues that sign-dependent singular terms cannot be cancelled; at n = 4 the last level's
  conormal coefficients have K- tails of order alpha - 2 that could mask terms of order 3, 4, so the identification
  uses the equation instead of forward tails.
- Next: verifier 118 on III.I'''''''''''' and the D275 repairs; then III.I''''''''''''' (section 11.8.3).

### 4.200 D277: verifier 118 seated; III.I'''''''''''' verified, III.I''''''''''' proved

- M1: two tf-cut-off pieces were filed as K+-order alpha - eps: chi_tf rho_tf^{alpha_0 - 2} u_tf of III.G''''
  Proposition 4.4 (chi_tf = chi_2(rho + |sigma|) is 1 at tf cap zf, and u_tf has a zf (0,0) term) and sigma^3
  chi_tf^sharp u~ of Proposition 5.1 (its proof puts chi_zf chi_tf v_0 into u~). Repaired: both are expanded at zf and
  their zf-terms sigma^j |sigma|^k c(x) enter as pieces of type (v); the zf-remainders have K+-order alpha - eps.
- m1: the profiles (u-hat_2, u-hat_3, v_0) are only conormal: profiles are now conormal of a degree, Lemma 2.3 works on
  conormal sections of order > -3 (III.A Lemma 1.4 first), Lemma 2.1 (b) records iota+ polyhomogeneity for the
  polyhomogeneous part only. m2: Lemma 2.2's iota+ order by the scaling sigma = zeta/r. m3: Lemma 2.1 on {r <= t/8}
  by integration by parts in sigma (the symbol vanishes for |sigma| <= c_0/r). m4: the constant-data columns are
  polyhomogeneous at iota+ with exponents in Lambda (Psi = Phi(sigma r)), not of order alpha. m5: Step 0 row by row.
  m6: Lemma 2.4 now records the exponents (z + d_rho in the pieces' iota+ exponents plus E_ind), and Step 4 places
  them in E_sharp by III.I'''''''''' Lemma 1.2 (c).
- Eleven nits seated in III.I'''''''''''', and three in III.I''''''''''' (its D275 repairs are correct: proved).
- w_rho := 3 + eta_2 - 2 eps - d_rho for every row (v1 and the rows with mu <= -1 have finite-sum coefficients), so
  the iota+ order of every chi_K T_rho(Y_rho) is at least 3 + eta_2 - 2 eps, the source's (11.227b).

### 4.201 Section 11.8.3 at n = 4: the source's Corollary 11.66 does not transfer verbatim

- The source proves Corollary 11.66 by applying Theorem 11.59 at the background h + h_rem(q), whose K+-order is only
  2 + eps_K, "the iterative procedure applying verbatim". At n = 4 the background h + h_rem(q) has K+-order
  alpha - 2 - eps, and three steps fail there: III.I''''''''''' Lemma 3.2 jumps from an admissible alpha' < 3 to alpha >
  4 in one step using w_0 + a_K > alpha (w_0 < 1), and III.I'''''''''' Definition 1.3 has no admissible levels in
  [3, 4 + eps_K - eps'_0] for a slower iteration; III.I''''''''' Lemma 2.6 (c)'s r^nu needs a_K > alpha + 1 -
  lambda_sharp; and a Neumann series in q around III.I''''''''''' Theorem 4.1 at h loses derivatives (R_q is of order 2).
- The b-derivative with towers for L_b (the source's Lemma 11.65) has K+-order alpha - eps, but iota+ exponents
  (E_sharp + E_ind) + 2 from the b-derivative of the towers' profile corrections, which are not in E^0_src + 2;
  III.I'''''''''' Lemma 1.2 (c)'s induction admits such contributions, so an enlarged source class appears possible.
- Classes: the output's K+-order alpha - eps against (H2)'s 4 + eps_K is consistent if the classes are read as
  intersections over eps and the theorems run at admissible alpha'' < alpha (every use of a_K is strict there).
- Next: III.I''''''''''''' needs either the theory of III.I''''''''''' at intermediate levels beta in (3, 4 + eps_K]
  (fewer Taylor levels) with a finite bootstrap in steps alpha - 4 - 2 eps, or K+ formal solutions for products of
  towers. Design notes in the D276 scratchpad.

### 4.202 Part III.I''''''''''''' written (D278): the expansion at every level

- PART-III-I14-LEVELS.md: III.I''''''''''' Proposition 3.1 and Lemmas 3.2-3.3 at every admissible level beta in
  (3, 4 + eps_K] (dense), and III.I''''''''''' Theorem 4.1, III.I'''''''''''' Theorem 3.1 for sources in Y^natural.
- Below the order 4 the level-3 source has zf-weight beta - 4 - eps in (-1, 0): no zero-energy solve at level 3; the
  Proposition 5.1 loop with alpha_tau = tau and w in [-eps, 1); III.I'' Lemma 4.2 with the negative zf-weight.
- Y^natural: iota+ exponents E_sharp + (m >= 1 increments of Lambda); each increment raises n(lambda) by one, so the log
  order stays K(lambda') - N_*(l_* + 1) - 1, room for the raises (Lemma 1.3).
- The plan for section 11.8.3 (next part): linearise at h, not at h + h_rem(q). With u the forward solution at
  h + h_rem(q) (smooth, from the energy estimates there), L_h u = F - D_p P_5(p') - R_q u, and R_q u has K+-weight
  (that of u) + alpha - 2 - eps and iota+ weight above w_+; bootstrap level by level with steps below alpha - 4 - 2 eps,
  each step Lemma 2.2 at h (where a_K >= 4 + eps_K), the new rows' coefficients minus the identity small in the new
  parameter coordinates; no derivative loss (u is known smooth), no r^nu defect (rows at h); the b-direction by towers
  for L_b (Y^natural).
- Next: verifier 119 on III.I''''''''''''' and the D277 repairs; then III.I'''''''''''''' (section 11.8.3).

### 4.203 Part III.I'''''''''''''' written (D279): section 11.8.3 at n = 4

- PART-III-I15-AUGMENT5.md: P_5(h, p, q) = P_4(h + h_{b,rem}(q), p) with towers for L_b; D_b P_5 in Y^natural(alpha-)
  (the source's Lemma 11.65: L_b h_{b,rem}(q) has K+-order alpha- for each b, the remainder 2 alpha - 4 - > alpha);
  Theorem 3.1 = the source's Corollary 11.66.
- Proof: the forward solution u(p') at h + h_rem(q) exists (II.E Proposition 3.4 on slabs); III.I'''''''' Proposition
  4.1 at h + h_rem(q) (it needs only a_K above the level, below alpha - 2) gives the base level; then L_h u = F -
  D_p P_4(p') - Delta_q p' - R_q u, and III.I''''''''''''' Lemma 2.2 at h raises Z_{beta_k} to Z_{beta_{k+1}}, steps
  below alpha - 4; on the affine set of p' already fixed, the new coefficients are -(new coordinates) + o(1) (at the
  base point exactly, as in III.I''''''''''' Theorem 4.1's proof); finitely many levels, so a unique p'.
- The b-derivative needs the towers at b near b_0 with b-independent leading terms (Lemma 2.1: the states are smooth in
  b by III.D''' Proposition 3.1 and III.F'''' Proposition 5.1, normalised by the Minkowski-model leading terms).
- Classes: read with orders w- and constructions independent of the loss (Lemma 2.5), the class of h' is that of h.
- Next: seat verifier 119; verifier 120 on III.I''''''''''''''; then [Hin26] section 12 (efficient parameterization).

### 4.204 Verifier 119 seated (D280): III.I''''''''''''' verified, III.I'''''''''''' proved

- Verifier 119 read III.I''''''''''''' and the D277 repairs: 1 major, 3 minor, 11 nits; the D277 repairs correct.
- M1: E_sharp (III.I'''''''''''' section 1) admitted, below 2, the log orders K(lambda) > L_0 at the points of pi_1 M, so
  E^natural below 2 did not lie in E_++. Repaired: E_sharp := {(lambda, k): lambda in Lambda, Re lambda >= 2,
  k <= K(lambda)} together with M; below 2 it is M, which the increments keep below 2 (E_++ is closed under them).
  The uses in III.I'''''''''''' Steps 2, 4, 5 and in III.I'''''''''''''' Lemma 2.4 (c) were checked against it.
- m1: for beta in (4, 4 + eps) the step "tau <= beta - 2 < 2" failed; eps < beta - 4 is now required above 4, and
  beta = 4 is excluded by Definition 1.1 (a).
- m2 (the base of the bootstrap) and m3 (the row defect at h + h_rem(q)) were gaps in the plan of 4.202.
  III.I'''''''''''''' as written closes both. Its Step 1 is the base, III.I'''''''' Proposition 4.1 at h + h_rem(q),
  which asks for K+-order above alpha_1 < 3 only. The rows enter at h, and the difference at h + h_rem(q) is exactly
  R_q(h_nu(W)) (its Lemma 2.4 (a)), supported in C.
- Nits: n1-n4 on III.I''''''''''''', n5-n10 on III.I'''''''''''' and n11 on III.I''''''''''' are seated.
- Next: verifier 120 on III.I'''''''''''''' and the D280 repairs; then [Hin26] section 12.

### 4.205 Verifier 120 seated (D281): III.I'''''''''''''' verified

- Verifier 120 read III.I'''''''''''''' ([Hin26] section 11.8.3 at n = 4) and the D280 repairs: 1 major, 4 minor, 7
  nits; the D280 repairs correct.
- M1: at a rotating b near the non-rotating b_0 the rotation state h_{b,v1} does not vanish, so a v1 coefficient of q
  with exponent z in M (Re z < 2) has rate z, and the b-derivative of the quadratic term of P_5 has K+-order (alpha - 2
  + z)- < alpha. Repaired by rotation rows: rows (v1, lambda, k), (lambda, k) in M, carrying all rotations (Definition
  1.3). They enter P_5 through h_nu (supported away from K+) and theta_nu (K+-weight Re lambda + 4), q's v1 exponents
  are restricted to Re >= 2, and Theorem 3.1 fixes the rotation coordinates by the expansion (Step 4': the derivative
  is -id, as m_nu is the v1 tower up to K+-order Re lambda + 3 - eps).
- m1: the b-derivative of the conormal Y^c parts gains min Re E_ind at iota+ (Lemma 2.1); delta_+ <= min Re E_ind. m2:
  Lemma 2.1's mechanism is III.D''' Proposition 3.1 with the remark after its Lemma 2.1 (not the tower relations),
  normalised to the identity at b_0; h_{b,v1} is b-dependent. m3: Lemma 2.5's eps_0 also stabilises the level-3 weights
  and the switch; III.G'''' Proposition 5.1's Mellin line moves without crossing a root. m4: III.I'''''''' Lemma 3.3
  cited.
- Nits: Remark 11.61 is on p. 279; the admissible sense; the K+-weight of "q small"; the order of L(d_b h_rem b');
  spacing in III.I'''''''''''''; line lengths in 4.204; 4.203 omits that the levels below 3 use III.I'''''''' Lemma 3.2
  at h.
- Whether the source's Lemma 11.65 meets the same rotation term at a non-rotating Kerr b_0 was not adjudicated.
- Next: verifier 121 on the D281 repairs; [Hin26] section 12 at n = 4 (Part III.J) is being written.

### 4.206 Part III.J written (D282): efficient parameterisation I

- PART-III-J-PARAM.md: [Hin26] section 12 to Remark 12.6 at n = 4. Data space (Definition 1.1): b - b_0, S, S^(0)_1,
  iota+ data (u^0_lambda, f_lambda) at the resonances in pi_1 E_sharp, S_rem, b_rem, the conormal Y_rho for the rows mu
  in (-1, 0], and a remainder tensor.
- At n = 4 the iota+ series below 3 + eps_+ is linear (products start at 2 lambda_sharp = 3 + 2 delta_sharp), so each
  exponent lambda_0 is one equation Lbar G(lambda_0) = -F_0(lambda_0), solved by III.G''' Corollary 3.1; the formal
  solutions at R = 0 go to rows (rate <= 2), rotation rows (v1 below 2) or q (rates in (2, alpha)).
- Phi is affine in the infinite-dimensional data with coefficients smooth in (b, S, S^(0)_1): smooth and tame at once
  (Theorem 2.4). Conditions (G+) (no Lambda in (3, 3 + eps_+]) and (A_J) (finitely many exclusions for alpha).
- (J2) settles III.G''' (G'''1)'s reading: no step source carries the exceptional scri+ term, so the pole at
  lambda_sharp enters only through the datum f_{lambda_sharp}.
- Open for III.J' (Theorem 12.8): the iota+ order (3 + eta_2)- of III.I'''''''''''''' Theorem 3.1 against the (3 +
  eps_+)- of the classes; the linear theory at b != b_0 ((I3)). Psi (Lemma 12.7) after III.C'.
- Next: verifier 121 (D281 repairs); verifier 122 on III.J; then III.J' ([Hin26] Theorem 12.8).

### 4.207 Part III.J' written (D283): efficient parameterisation II

- PART-III-J2-LINEAR.md: [Hin26] Theorem 12.8 at n = 4 and b_0. Every solution (h', p', q') of III.I(14) Theorem 3.1
  for a source in F is D_U Phi(U'): subtract D_U Phi of the parameters p'_{<=0}, then exponent by exponent the resonant
  states (Case A: no pole, all terms vanish; Case B: III.G''' Proposition 3.7 gives the data), then the conormal
  remainders.
- Lemma 1.1 closes III.J (J5) (a): under (G+) the level-2 tf-exponents (u-exponents minus 1) avoid (2, 2 + eps_+], so
  eta_2 can approach eps_+ with the same construction, and the linear solutions have iota+-order (3 + eps_+)-.
- Open: the tame form of the estimates (III.I(8)-(14) state bounds uniform for small backgrounds, not tame); the linear
  theory at b != b_0 ((I3)); Psi after III.C'.
- Next: verifiers 121 (D281) and 122 (III.J, III.J'); then [Hin26] section 13 and III.C'.

### 4.208 Verifier 121 seated (D284): the D281 repairs read

- Verifier 121 read the D281 repairs to III.I'''''''''''''': 1 major, 2 minor, 6 nits; verifier 120's M1 and m1-m4
  closed.
- M1: Step 4 used the uniqueness in III.I''''''''''' Theorem 4.1, which fails on the P enlarged by the rotation rows
  (Step 3 itself makes the solutions a graph over the rotation coordinates). Repaired: Step 4' splits p' = p'_0 +
  W'^rot, moves the rotation-row terms f^nu(W'_nu) into the source (they lie in Y_2(alpha), III.I''''''''' Lemma 2.6
  (b)), and applies III.I''''''''''' Theorem 4.1 and III.I'''''''''''' Theorem 3.1 with the P of III.I''''''''';
  Definition 1.3 exempts the two from the enlarged P.
- m1: the rotation rows are an index set (rot, lambda, k) disjoint from N, whose v1 rows keep W = 0; Lemma 2.2 (f) is
  excluded for them. III.J and III.J' use the same notation.
- m2: the coefficients of the expansion are determined by u through dual functionals on a compact set, from the
  uniqueness in III.I'''''''''''' Lemma 2.3 (a); the conormal S_rem term is removed exactly. The continuity of C^rot is
  III.I''''''''''' Lemma 3.3's argument.
- Nits: the i = 3 and dt-terms have K+-order Re lambda + 3 - eps (also in 4.205); III.I'''''''''' Lemma 2.1 (b)'s
  argument for v1; (H3) from that of III.I'''''''''; the non-vanishing at a rotating b is a remark; the eps-stability
  wording; 4.204 rejoined.
- Next: verifier 122 on III.J, III.J' and the D284 repairs.

### 4.209 Verifier 122 seated (D285): III.J and III.J' verified

- Verifier 122 read III.J, III.J' and the D284 repairs to III.I'''''''''''''': 1 major, 3 minor, 10 nits. The D284
  repairs close verifier 121's M1, m1 and m2; page citations and format check out.
- M1: III.J Theorem 2.4's (2.5) at a rotating b. A v1 coefficient of q at an exponent of real part 2 (2 is in Lambda)
  has K+-order 2 through the rotation state h_{b,v1}, so its square in P_5 has K+-order 4 < alpha. Repaired by carrying
  these terms by rotation rows too: N_rot is indexed by M_rot := M + (E_sharp at real part 2) = E_sharp at real part <=
  2, whose rate at b_0 is Re lambda + 1 <= 3, so they are new rows at no level; E^alpha_v1 := E_sharp at real part > 2,
  hence > 2 + eps_K by (G), and h_{b,rem}(q) has K+-order (alpha - 2)- at every b near b_0. III.I'''''''''''''' Step 4'
  now separates the coefficients at M_rot modulo O(t^{-3-delta'}), delta' = min(eps_K, alpha - 4)/2.
- m1: (i) of Step lambda_0 claimed the rows up to rate 2 + eps_+; (G) clears only up to 2 + eps_K. m2: L_b, not
  L_{b_0}, acts on the towers in the K+-order of f. m3: III.J' Case A now states that the coefficients of q' and of D_U
  Phi have rate < alpha, so each carries a formal solution visible below ell_K.
- Nits n1-n10 seated (the s1 and v1 rates against the K+-order of the formal solution; Corollary 3.1 applied to 2f; the
  pole bound of III.G''' Proposition 2.4; the choices re-made after eps_+ decreases; the source's V_{1,rem} absent at n
  = 4; ell_K^max = 3 under (C5); the exponent claim of Lemma 2.1; real parts at real lambda_0; and in
  III.I'''''''''''''' the unknown parameter in the original P, and 'need not vanish' in finding 5).
- Next: verifier 123 on the D285 repairs; III.J'' (the tame estimates, (J'2)) is being written.

### 4.210 Part III.J'' written (D286): tame estimates

- III.J'' (PART-III-J3-TAME.md) discharges (J'2) at b_0, the tame estimates that [Hin26] asserts in Remark 11.13 and
  states for Corollary 11.66 and Theorem 12.8 without proof.
- Section 1: tame families (C_k(||e||_{k+d} + ||beta||_{k+d} ||e||_d)), closed under sums, composition (losses add),
  finite rank, fixed maps and a fixed number of compositions.
- Lemma 2.1, the elementary families: (a) the forward solutions, by III.I Theorem 5.3 with the background h + h_tot(p)
  + h_rem(q); (b) the background coefficients, by II.A Corollary 9.7 and Lemma 9.5 and II.G Lemma 4.1; (c)
  finite-dimensional inverses and coefficient functionals; (d)-(g) the model inverses at every finite order with a loss
  independent of the order, nine of them stated at order infinity and proved at finite order by their own proofs
  (III.G' Theorem 3.1 (2) at iota+, III.F' Corollary 3.4 at tf).
- Found: II.G' Corollary 4.5 (high frequencies) loses ceil(k delta) + ell. The loss is bounded in k only through strong
  trapping admissibility, which is proved at b_0 (III.F Proposition 4.1); near b_0 it holds on a neighbourhood
  shrinking with k (III.H' (H'3)), so the tame form at b != b_0 joins (J'3). The order-dependent choices (that cut-off,
  the radius c_k of III.H Corollary 4.2) cost constants only (Remark 2.2).
- Section 3 inventories every construction of III.I-III.I(14) and III.J' by these families, each loop of a length fixed
  by weights and orders. Theorem 4.1 is the tame form of III.I(14) Theorem 3.1 (the source's Corollary 11.66 estimate),
  Theorem 4.2 that of III.J' Theorem 2.1 (Theorem 12.8), and Proposition 4.3 the tame forward map U -> P_5(Phi(U))
  (section 13.1, Step 3 (2)).
- Open for [Hin26] section 13 at n = 4: (J'3), the linear theory and its tame form at b != b_0; III.C' and the exterior
  family h_{-S}; smoothing operators on the spaces of III.J Definition 1.1 (II.G Proposition 3.1).
- Next: verifier 124 on III.J'' once verifier 123 (the D285 repairs) is seated.

### 4.211 Verifier 123 seated (D287): III.I'''''''''''''', III.J and III.J' proved

- Verifier 123 read the D285 repairs to III.I'''''''''''''', III.J and III.J': 0 major, 0 minor, 7 nits. The rotation
  rows of real part 2 (M_rot), the rate bound by (G), Step 4''s separation modulo O(t^{-3-delta'}), the K+-order of
  (2.5) at a rotating b and III.J' Case A all check out. III.I'''''''''''''', III.J and III.J' are proved.
- Nits seated: (J4) of III.J now says real part at most 2; the v1 carrier's rate at a rotating b; the s1 formal
  solution's order Re lambda_0 + 1 <= 4 in III.J' Case A; lambda_sharp + 2 > 3 + delta' and the rate bound from
  III.I'''''''''''' Theorem 3.1 in Step 4'; Lemma 2.3 cited for M_rot; Re z in finding 5; two parentheticals merged.
- Next: verifier 124 on III.J'' (D286); III.C' ([Hin26] sections 5.4-5.5 at n = 4) is being written.

### 4.212 Part III.C' written (D288): the exterior solution and its partial polyhomogeneity

- III.C' (PART-III-C2-POLYHOM.md) writes [Hin26] sections 5.4-5.5 at n = 4.
- Lemma 1.1 (the source's Lemma 5.16): the exterior domain with the weights 3/2 < l_I^flat < min(l_0^flat, 3/2 + (1 -
  e_Ups) gam_Ups, 2), shifted by 1/2 at null infinity. The null boundary is spacelike for g_{b_0} + h: only delta_00,
  of pi_C type, competes with r^{-l}, and the n = 4 mass sits in the 11-slot at rho_0^2 rho_I^2.
- Theorem 2.1 (the source's Theorem 5.17 with (5.52)-(5.53)) is stated as the output of Part IV ([Hin23a] section 3 at
  n = 4); finding (C'1).
- Theorem 3.1 (the source's Theorem 5.21) at n = 4, with min Re E_0 > 3/2 + 2 gam_Ups. Step 1 commutes with prod(X_0 -
  z): index sets are closed under +N_0, and R annihilates the expansion terms up to alpha_1, so the commutator costs
  nothing. Step 2 integrates slot by slot through the constant lower-triangular A-bar (III.C Lemma 4.2), half a step at
  a time, enlarging E^C_I by the extended union with E_0 that the corner integration makes (the source's E^{C,new}_I).
- Settled: III.C's (C7). At n = 4 the radiation fields enter only the error (III.C (C1)), so the source's subtraction
  g_0 = g_{b_0} + h_0 and its source term P(g_0, g_{b_0}) are not needed.
- Next: verifier 125 on III.C' after verifier 124 (III.J''); then III.C'' ([Hin26] sections 5.6-5.7), Part IV ([Hin23a]
  section 3 and [Hin26a] at n = 4), (J'3), and [Hin26] section 13.

### 4.213 Part III.C'' written (D289): boosts and gauged Cauchy data

- III.C'' (PART-III-C3-BOOSTDATA.md) writes [Hin26] sections 5.6-5.7 at n = 4.
- Lemma 1.1: the pullback of g_{b_0} by a boost lies in the class G of III.C on Omega_ext,r1. With the past slab of
  III.C' Lemma 1.1 at slope 1/12 (zeta = dt_* + (13/12) dr, timelike for eta), Omega_ext stays in {chi_IVP = 1}.
  Settled: III.C's (C4).
- Section 2: the cut-off gauge Upsilon^{chi_0 E_Ups} (2.1) and its naturality under boosts (2.2); Lemma 2.1, the
  structure of III.C at null infinity holds in that gauge.
- Theorem 3.1 (the source's Theorem 5.23) (1)-(3): the exterior solution pulled back by boosts, by uniqueness and
  finite speed of propagation. Remark 3.2.
- Proposition 4.1 (the source's Proposition 5.25): gauged Cauchy data from the frame e_0, ..., e_4. Proposition 4.2:
  Boyer-Lindquist data at n = 4 carry no E_log, since t - t_BL = -mu r^{-1} + O(r^{-2}). Remark 4.3 (the source's
  Example 5.27).
- Findings: (C''1) a misprint in the source, {chi_0 = 1} for {chi_0 = 0} and [-1/8, -1/8] for [-1/8, 1/8]; (C''2) Part
  IV must deliver III.C' Theorem 2.1 in the cut-off gauge; (C''3) C4 settled; (C''4) no logarithms at n = 4.
- Next: verifier 125 on III.C' and III.C''; seat verifier 124 on III.J''.

### 4.214 Verifier 124 seated on III.J'' (D290): fixed losses, one norm, (J''4) found

- Verifier 124 on III.J'' (PART-III-J3-TAME.md): 2 major, 6 minor, 7 nits, seated.
- M1: the spaces of III.I(14) and III.J carry orders read 'w-', intersections over a loss, so their order-k spaces are
  Frechet. Section 1 now takes each at a fixed loss eps (Banach); a statement maps the input at a loss eps' <= eps
  (closed graph theorem) to the output at eps, and Theorems 4.1-4.2 and Proposition 4.3 are stated so. Found (J''4):
  Proposition 4.3 maps D_eps to F_eps and gains nothing in the weights, so II.G Theorem 2.1 needs eps' = eps, an
  inverse without loss in the weights. The source states exactly that (Theorem 12.8, p. 312: f at (4+eps_I, 5+eps_+,
  4+eps_K), h' at (3+eps_I, 3+eps_+, 4+eps_K)). Open; the route proposed is an improvement to exact weights after the
  fact, face by face (N_{iota+} on a line free of its spectrum with the gap of (G+); III.A Lemma 1.2 at I+; the
  low-energy estimates at K+).
- M2: Lemma 2.3 names the one norm: every 'small' of III.I-III.I(14) is smallness of ||h||_{X^{d_*}} + |S| + |p| +
  ||q||_{Q^{d_*}} (III.I Theorem 5.3, II.F' Theorem 1.1, III.I(4) Lemma 4.2 (b), III.I(7)'s and III.I(8)'s convention,
  III.I(14)'s seminorm for q); the d_k of III.J' Theorem 2.1 are not needed ((J''5)).
- Minors: (f) now derives (k+1) delta_Gamma <= 1 from I.B (1.4) and III.F Proposition 4.1, with ell depending only on
  orders and weights (m1); the inventory rows completed and relabelled (m2); III.I' Proposition 2.1 and III.A Lemma 3.2
  as regularity statements, Lemma 1.2 (f) (m3, n7); Case B and the conormal components of q' routed (m4); Lemma 2.4,
  tame products in partially polyhomogeneous spaces, and Proposition 4.3's use of the cancellation (m5); Remark 4.4
  lists II.G's support conditions (m6). Nits n1-n7 seated.
- Next: verifier 126 reads the D290 repairs together with D291 (verifier 125 on III.C', III.C''); then the exact-weight
  part for (J''4).

### 4.215 Verifier 125 seated on III.C' and III.C'' (D291): the boost theorem under the constraints

- Verifier 125 on III.C' (PART-III-C2-POLYHOM.md) and III.C'' (PART-III-C3-BOOSTDATA.md): 1 major, 8 minor, 17 nits,
  seated. Checked correct: the slope 1/12 and -143/144, Omega_ext inside {chi_IVP = 1}, the future boundary, (C7)
  settled, (C4), the frame algebra of Proposition 4.1, all pages.
- M1: III.C'' Theorem 3.1 (1) pulled back the whole gauge-fixed operator as if natural; E_C is built from the fixed
  1-form c_C of III.B (6.2), which a boost does not preserve. (1) is now stated under the constraints and proved by
  III.C' Remark 2.2 (1): both terms of the operator vanish near Sigma_IVP, where chi_0 = 0. The source has the same
  gap: finding (C''5).
- Minors: Step 1's commutator now uses that R commutes with the leading part, so [A, R] carries rho_I^2 and the
  radiation field of slot 6 is annihilated (m1); beta := min(alpha_I + eta, l_I) in the last round (m2); t_IVP r^{-1}
  h_1 in Remark 2.2 (1), the source's Remark 5.18 misprint, (C'5) (m3); a corrupted formula restored (m4); t - t_BL =
  +mu/r for III.B's time, with the citations corrected (m5); r_1 := 2r_0 so the boost's size is independent of r_0,
  (C''6) (m6); the cancellation from P(g_0, g_0) = 0 in Theorem 3.1 (2) (m7); (3) through (1)'s proof (m8). Nits n1-n17
  seated.
- Next: verifier 126 reads the D290 and D291 repairs; then the exact-weight part for (J''4).

### 4.216 Verifier 126 seated (D292): III.C' and III.C'' proved; III.J'' minors

- Verifier 126 read the D290 repairs (III.J'') and the D291 repairs (III.C', III.C''): every finding of verifiers 124
  and 125 resolved; (J''4) stated accurately and open; new: 0 major, 3 minor, 8 nits, seated. III.C' and III.C'' are
  proved; III.J'' stays verified, its three minor repairs to be read.
- m1: the closed graph theorem gives eps'(eps, k); section 1 now says so, lists the rows whose margins were read and
  are independent of k, and puts the rest into (J''4), where eps' = eps makes it moot.
- m2: Lemma 2.3 now names the remaining continuity inputs of III.I(14) Steps 3 and 4' and their topologies; the three
  lemmas that state (h_j, p_j) -> (0, 0) without a topology need it only in one fixed seminorm, since the coefficient
  functional they converge through is bounded by one (Lemma 2.1 (c)).
- m3: before the K+ step of (J''4), each minus at K+ is to be classified as a margin or a logarithm at the weight.
- Nits: d_0 := d_* + D; Theta may depend on the point; Ric(g_0) = 0 in the cancellation of III.C'' (two places); Remark
  2.2 (2) and the cut-off gauge cited in III.C'' Theorem 3.1 (3); README aligned with J3's qualifiers; 'for one eps' in
  (J''4); the K+ classification recorded in (J''4).
- Next: Part III.J''' (exact weights), from the five-reader survey of where the losses enter (d292).

### 4.217 Part III.J''' written (D293): exact weights at b_0; (J''4) discharged, to be verified

- III.J''' (PART-III-J4-EXACT.md) removes the losses in the weights where they arise instead of improving after the
  fact, the route 4.216 proposed. The d292 survey found three roots of every loss that reaches a final weight: (a) the
  graft's log t_* at K+, which hides log rho_K; (b) three pointwise proofs at the final weight; (c) margins at iota+,
  which are choices.
- (a): written in powers of log rho_+ (the source's Definition 2.8) the graft is exact (Corollary 3.2); in the log t_*
  convention no exact statement exists (Remark 3.1). III.A Proposition 4.2 is exact and only transmitted the loss.
- (b): III.I(12) Lemmas 2.2 and 2.1 (a) and Theorem 3.1's piece (vii) re-proved in L^2 (Lemmas 4.4-4.5).
- (c): at the closed endpoint of (G+) every map at iota+ is exact, and level 3's non-resonance holds automatically
  (Proposition 4.3).
- New conditions (E2)-(E5), each a finite exclusion (Lemma 1.4); alpha = 4 + eps_K is available under (A_K).
- Corollary 6.6: III.J'' Theorems 4.1-4.2 and Proposition 4.3 with eps' = eps = 0, on one pair of Banach scales;
  (J''4) is discharged at b_0, to be verified (verifier 127).
- Open: (J'3), the linear theory at b != b_0; the support conditions of II.G Theorem 2.1; smoothing operators on D_ex;
  the exterior family h_{-S}; Part IV; III.K ([Hin26] section 13).

### 4.218 Part III.H'' written (D294): uniformity near b_0; (I3) discharged, to be verified

- III.H'' (PART-III-H3-UNIFORM.md) supplies the two inputs that (I3) of III.I left open for b != b_0.
- Proposition 1.1: strong trapping admissibility of 2L_b at every b of a fixed neighbourhood B_*, uniformly. The frame
  is e_0 = zeta/sigma, a null e_2 built from dt_*, and the screen V = {e_0, e_2}^perp: e_0 is parallel along null
  bicharacteristics, the null filtration is invariant, and III.F's grading argument applies verbatim. Multiplying the
  inner product by f_b = |dg_b|/|dt_* dx| removes the density correction exactly. Corollary 1.2: delta_Gamma is
  uniformly small, so B^hi_k contains B_* for every k.
- Theorem 2.1: III.H' Theorem 1.3 on B_* for every k, uniformly (I.A Theorem 8.1, I.B section 9, III.H Remark 2.6).
- Lemma 3.2: N_{iota+}(2L_b) = N_{iota+}(2 bar L), since 2L_b - 2 bar L has coefficients rho^2, rho^3, rho^4. Theorem
  3.1: II.F Theorem 8.1 uniformly in b. Theorem 4.1: II.F' Theorem 1.1 uniformly in b, with continuity in b; (F'11)
  is discharged for the family 2L_b.
- Corollary 5.1: III.I Theorem 5.3 for b in B_*, with continuity in (b, S, h); (I3) and III.I Remark 5.4 discharged.
- Open, (H''5): the chain III.I'-III.J''' at base points b != b_0. The data at b_0 enter as the v1-rows (every
  rotation is Killing at b_0), as index sets of the zero energy states fixed at b_0, and as derivatives in b at b_0.
  This is the rest of (J'3). Also open: Part IV; III.K ([Hin26] section 13).

### 4.219 Verifier 127 seated (D295): III.J'' proved; III.J''' verified, its repairs to be read

- Verifier 127 read III.J''' and the D292 repairs of III.J''. III.J'': m1-m3 resolved, so it is proved. III.J''': 1
  major, 3 minor, 6 nits, seated. All Sources pages are correct.
- M1: the joint exact weight at the corner of iota+ and K+ was not proved. III.I(12) Lemma 2.1's bounds near iota+ and
  at the corner are pointwise, a fourth pointwise proof at a final weight (4.217 said three). Lemma 4.7 proves them in
  L^2: case (a) by Minkowski's inequality in zeta with the dilation invariance of dr/r, case (b) with m = 0 by a sup
  bound and the L^2 profile. Proposition 4.6's iota+ side is rewritten on it.
- m1: Remark 3.1, the t_*-convention's class and Definition 2.8's are incomparable at the exact weight; "no exact
  statement exists" withdrawn. m2: Corollary 6.6 now argues why the unchanged lossy rows do no harm (exact data enters
  every chain; margins chosen backwards per k change C_k, not d). m3: (E1) is a smallness condition; (E5) is vacuous.
- Nits: the indicial roots read with -Re mu; continuously embedded, not closed; (E2) covers the exclusions of III.I'
  Propositions 2.1 and 3.1, lambda_sharp included; the Laurent cut-off for the remainder's coefficients; "finite rank"
  dropped; "(P2: ...)" replaced by the use of (E1) in III.A's integrations.
- Next: verifier 128 reads the D295 repairs of III.J''' and III.H'' (D294).

### 4.220 Verifier 128 seated (D296): III.J''' proved; III.H'' verified, its repairs to be read

- Verifier 128 read III.H'' (D294) and the D295 repairs of III.J'''. III.J''': every finding of verifier 127
  resolved (Lemma 4.7 correct; the corner paragraph closes M1); four nits seated, and III.J''' is proved. (J''4) is
  discharged at b_0.
- III.H'': 0 major, 4 minor, 6 nits, seated. m1: Theorem 2.1's uniformity for every k comes from I.C Theorem 7.1 (2),
  local around each b at which its qualitative hypotheses hold, and compactness over a first neighbourhood B_1.
  m2: B_* is now chosen after the uniform constants, by (B5): Corollary 5.1's eps_0, the slab smallness up to
  tau_0^{-1}, and t^flat from g_{b_0} serving every b. m3: II.F section 6.3 uses P_0, so section 6 is run with
  2L_{b_0}. m4: (C3) at b by the margins of III.I Lemma 5.1.
- Nits: the limit operator's smallness in Theorem 4.1's continuity; the two further facts of the grading argument;
  the extension off Sigma by the same formulas; II.D at I+ and C' in section 7.6's list; the (H''5) sentence on
  III.G''; the frame comparison at b_0 marked as unused.
- Next: (H''5), the chain III.I'-III.J''' at base points b != b_0 (plan in the scratchpad, d296/plan.md).

### 4.221 III.I''''''''''''''' written (D297): the linear theory at base points near b_0

- (J'3) of III.J' and (H''5) of III.H'': the chain III.I'-III.J''' was written at b = b_0. The new part carries it to
  every b in B_* (III.H'' Corollary 5.1). The model objects transfer by (P1)-(P6), with L_b in place of L_{b_0}; joint
  injectivity of the states at b follows by perturbation.
- The one obstruction is v1: at a rotating b, h_{b,v1}(V) lies in ker hat L_b(0), whose dimension does not jump, so v1
  cannot be eliminated by the K+ extraction. As in the source (pp. 279-280, (11.229)), the v1 terms of exponent of real
  part at most 2 are carried by the rotation rows of III.I(14), with coefficients assigned from the construction: the
  graft's, read from the iota+ data, and the spectral one at level 1. No inversion of h_{b,v1} is used; at b_0 the
  assignment agrees with III.I(14) Step 4'.
- Theorem 3.1 lists the statements that hold at b, by a census of the uses of b_0; Corollary 3.2 gives right inverses
  at every base point. The census is a search, and (I^(15)4) says so.
- Next: verifier 130 reads it with the D298 repairs of III.H''.

### 4.222 Verifier 129 seated (D298): III.H'' repairs

- Verifier 129 read the D296 repairs of III.H''. 0 major, 2 minor, 5 nits. M1: the order of choices was still circular,
  as (B5) used eps_0 and tau_0 proved only on B_*. M2: (B5)'s slab clause did not cover the slabs of II.F Lemma 7.5 and
  of II.F' Proposition 3.1 (iv) and Lemma 2.9.
- Repairs: II.E is applied relative to 2L_b itself, as II.F section 7.5 and II.F' do; its constants depend on finitely
  many coefficient norms and margins, continuous in b, hence uniform on the compact closure of B_1. The slab clause is
  dropped; the eps_G clause moves to (B2); sections 1-4 are stated and proved on B_1; B_* is chosen by eps_0 alone.
- Nits: O fixed small in (B1) instead of shrunk later; the two further arguments behind the uniformity in k; the order
  in II.F section 6 with P_0 := 2L_{b_0}; a cleaner (C3).
- Next: verifier 130 reads the D298 repairs and III.I(15).

### 4.223 Verifier 130 seated (D299): III.H'' proved; III.I(15) verified, its repairs to be read

- III.H'': verifier 130 read the D298 repairs. M1 and M2 and the five nits are resolved; the II.E coefficient-norm claim
  is supported. Two nits are seated: the uniformity is per slab step, finitely many steps; B_* is shrunk further by
  III.I(15). III.H'' is proved.
- III.I(15): 1 major, 4 minor, 3 nits. M1: at a rotating b the rotation rows have K+-rate Re lambda <= 2, below the
  levels, so III.I(14) Step 2's (3.4) and the uniqueness via Step 4' fail at b. Repair: Lemma 2.4 (III.I(13) Lemmas
  2.2-2.3 at b, with the rotation rows at their assigned coordinates A_b(G)). Proposition 2.5 makes the rotation rows
  new rows of the levels at which their rates lie, with C = A_b(G') - W'. The joint elimination is -id + small, and
  uniqueness holds with the constraint W'^rot = A_b(G') (Remark 2.6; III.J'-III.J''' use only the constructed map).
- Minors. m1: the sign, which is now W' = A(G'). m2: rows at b and corrections at b_0 give a mismatch E^nu (1.1),
  supported away from K+ and O(|b-b_0|). Its iota+-exponents are those of the b-derivatives of the towers; its place
  in Y^natural rests on III.I(14) Lemma 2.4's argument, recorded as the point to check (I^(15)3). m3: the continuity
  lemmas were added to the list, and B_* is shrunk. m4: the reason v1 is excluded is that h_{b,v1}(V) is O(|b-b_0|) in
  the span of gdot_b, h_b(S).
- Next: verifier 131 reads the D299 repairs of III.I(15). III.K ([Hin26] section 13.1) is being drafted (plan:
  scratchpad d299/plan.md).

### 4.224 III.K written (D300): [Hin26] section 13.1 at n = 4, conditional on Part IV

- The assembly of the nonlinear theorem: initial family, Psi, right inverses, support classes, smoothing, II.G
  Nash-Moser, constraint propagation; Theorem 4.3 is the source's Theorem 13.1 at n = 4.
- Three changes from the source:
  - (K1) The initial family solves the cut-off gauge, and the cone uses the uncut one; they agree only where chi_0 = 1.
    The new cut-off chi_0-natural = 1 - (1 - chi_0)(1 - chi(t_*)) equals 1 on Omega_* and chi_0 on the exterior domain.
  - (K3) In Psi's right inverses the boost defect gains a term e_S supported in {1 <= t^flat_* <= 2}, small with the
    data.
  - (K4) II.G's closed support classes need conditions on every component of supported character. The q-tails are cut
    off to t_* >= 8 by Z at no cost, as they enter only through h_rem(q), which vanishes on t_* < 10.
- Part IV must deliver (K2): III.C' Theorem 2.1 in the cut-off gauge; its continuation on the slab near I+ up to
  t^flat_* = 3 (the source's "for globally small initial data" sentence, p. 321); and III.E Theorem 1.1.
- (K8): chi_iota is taken to vanish on {t^flat_* <= 2}; its choice in III.G'' is free, which is to be checked.
- Next: verifier 132 reads III.K (after verifier 131 on III.I(15)); then Part IV.

### 4.225 Part IV started (D301): [Hin23a] sections 3.1-3.2 at n = 4

- Part IV, the exterior estimates III.C' Theorem 2.1 rests on, is written out at n = 4 on III.C's region in III.C's
  Minkowski null coordinates (not the source's Schwarzschild ones; the mass enters only the error class).
- This first file covers the edge-b frame and metric; the operator L = rho_I rho^(-7/2) box rho^(3/2), symmetric on
  rho_0^5 rho_I^4 |dg|, with Delta+3/4; the energy estimate near I+ with Qbar of 10.64 X3; and the b-estimate near the
  interior of I_0, which the source cites from [HV20, Proposition 4.3] and which is written out here.
- Next: Part IV's tensor operator and tame estimates ([Hin23a] sections 3.3-3.5), then section 3.6 with III.C'
  Theorem 2.1, the cut-off gauge (C''2) and the slab (K2); [Hin26a] for III.E Theorem 1.1.

### 4.226 Verifier 131 seated (D302): III.I(15) repairs

- Verifier 131 read the D299 repairs: 1 major, 3 minor, 8 nits. Verifier 130's M1 (outside the continuity step), m1
  and m4 are resolved, and (I(15)3) is settled: E^nu's iota+-exponents lie in E^natural + 2.
- M1: Step 3's A_k -> 0 across b rested on continuity lemmas proved by perturbation from L_{b_0}, whose remainder has
  K+-weight at most lambda_sharp + 1 at b != b_0. Repair: A_k is bounded directly by the uniform bounds of S and A_b
  and the smallness of r^nu + E^nu, Delta_q, R_q; the continuity lemmas are used at fixed b with base point (0, p_b).
- m1: the cut-off split is dropped. f^nu_b is III.I(9) Lemma 2.6 (c) with every object at b, and E^nu is the
  b-difference of the corrections and counterterms, of K+-weight kappa_nu > alpha. m2: III.I(11) Theorem 4.1 and
  III.I(13) Proposition 2.4 are used at b only inside Lemma 2.4 and Proposition 2.5. m3: A_b and E^nu enter III.J'''s
  tame inventory.
- Next: verifier 133 reads the D302 repairs, after verifier 132 (III.K and Part IV).

### 4.227 Part IV' written (D303): the tensor operator and the tame estimate

- PART-IV2-TAME.md writes out [Hin23a] sections 3.3-3.5 at n = 4 for [Hin26]'s operator on III.C's exterior region.
  Proposition 1.2: L_g = 2 rho_I rho^(-7/2) L^{g,g0} rho^(3/2) = -2(X_I - Abar)(X_0 - X_I) + x_I^2 Delta + Ltilde_g,
  Abar constant lower triangular with diagonal >= 0, Ltilde_g in (x_I C^oo + H^{k-2,(E_0,l_0),(F-1,l_I-1)}_b) Diff^2_eb.
- Proposition 2.2: the energy estimate and its tame form for alpha_I < min(alpha_0, 0), by Lemma 2.1's fibre inner
  product and a per-slot quadratic form positive for kappa small; Lemmas 2.3-2.4 in dimension 5.
- (IV'1): the edge-b form needs the refined count of Lemma 1.1; III.C's pointer to III.C' for it is not borne out.
  (IV'2): A^0_h is absent at n = 4, so the basic and sharp-weight estimates are one argument.
- Next: Part IV'' ([Hin23a] section 3.6 -> III.C' Theorem 2.1, the cut-off gauge, the slab of (K2)).

### 4.228 Verifier 132 seated (D304): III.K and Part IV

- III.K: 3 major, 5 minor, 5 nits, each major an inherited gap of the source. A-M1: Lemma 2.3's support claim needs the
  tail of the base point to vanish below the level; II.G Theorem 2.1 (iii) is weakened to u in U cap B_eta, which its
  proof uses ((H10)). A-M2: D_S := phi_S^(-1)({t_IVP >= 0}) cap ..., h_S on an S-independent two-sided region D.
  A-M3: support classes, chi_- and the collar in t_*, not t^flat_*; levels at T^ = 2/C', D up to t_* = T^ + 3.
- Minors: Lemma 1.1 (d)'s proof completed (nu_0 = min(1/4, r_0/8), compactness on r <= r_1 + 1); the cover re-posed
  (R_8 >= 2r_1; the compact part a domain of dependence bounded by {rho'_I = c}; the slab after it); h_0 two-sided and
  the order of S = 0 and S != 0; chi_K's threshold above T_iota + 1; e_S's support, tame bound and Step 1 role.
- Part IV: 0 major, 3 minor, 5 nits: the domain in U (t_* <= T_0), the density step by exhaustion with f_j away from
  I_0 and {x_I = eps}, the backward problem on the past slab; nits seated.
- To be read: the D304 repairs, with (K9)'s two checks (II.G section 6 and II.F section 7.4 for t_*).

### 4.229 Part IV'' written (D305): sharp decay and the exterior solution

- PART-IV3-NM.md: Lemmas 1.1-1.2 (the two families of curves, integration without loss), Lemma 2.2 (the Cauchy problem
  near I_0, both directions), Lemma 2.3 (growth at I+), Theorem 2.4 (III.C' (2.2) and (5.52), d = 4), Theorem 3.1
  (III.C' Theorem 2.1 by II.G, k_0 = 14), Corollary 4.1 (the cut-off gauge, (C''2)).
- (IV''1): two rounds, all slots at once; (IV''2): the slab of III.K (K2) (b) is the next part's; (IV''3): the data and
  the backward problem added to Part IV's Proposition 4.1.
- Next: verifier 133 reads III.I(15)'s D302 repairs, the D304 repairs, Part IV' and Part IV''; then Part IV''' (the
  slab) and Part IV'''' ([Hin26a], III.E Theorem 1.1).

### 4.230 Part IV''' written (D306): the slab

- PART-IV4-SLAB.md: the slab of III.K (K2) (b) is posed on Omega_ext,r_1 cup S from Sigma_IVP,r_1 and the compact
  Sigma_c = {rho'_I = c} cap dS, so that no Cauchy data sit on Sigma_fut,r_1 near I+ (asymptotically null there);
  the chart is translated in t (T'' = T^ + 5); Lemma 0.1 puts phi_S^* g_{b_0} in the translated class by III.B Lemma
  5.2; Lemma 1.1 the curves; Theorems 2.1-2.2 Part IV'' Theorems 2.4 and 3.1 there; Corollary 2.3 the
  orders (III.C' Theorem 3.1's proof). III.K Proposition 1.2's slab paragraph cites it.
- Next: Part IV'''' ([Hin26a] sections 2.3, 3-6 and Appendix B at n = 4 -> III.E Theorem 1.1), in several files; the
  record's 10.21-10.23 and (lxi) carry the computed inputs (cpmodes5, solv5, tface5, 10.79's horizon threshold).

### 4.231 Part IV'''' written (D307): mode stability and the zero energy operator of box^C

- PART-IV5-CDMODES.md: III.E Theorem 1.1 (1)-(3) at n = 4 at (v_C, e_C, C_0) = (1/2, 1/102400, <= 100), gamma_C = 1/h,
  h < min(10^-6, h_0) off a countable set (IV''''1). Lemmas 1.1-1.5 from the record's exact computations (10.13, 10.18,
  10.54, 10.14, 10.22, 10.79), extended to b near b_0; Lemma 1.6 (H1)-(H4), (G). Theorem 2.1 = [Hin26a] Theorem 6.2:
  surjectivity by the adjoint estimate (5.81) (IV''''3).
- Conditional on [Hin26a] Theorem 5.2 at n = 4 with (5.16) and (5.81): Part IV''''' (section 5.2, pp. 41-66), written
  D308 (4.232); then Part IV'''''' (Theorem B.1 -> III.E Theorem 1.1 (4)).

### 4.232 Part IV''''' written (D308): [Hin26a] Theorem 5.2 at n = 4

- PART-IV6-SOLV.md: the forward problem, the initial value problem (5.16), (5.79) and (5.81) for box^C on g^KS_b, b
  near b_0, at the weights (alpha_sf, alpha_K) = (-C_0 - 5/2, 1), C_0 <= 100, with h_0 uniform in b (Lemma 8.1).
- Inputs where n enters: III.B (3.2), Lemma 3.3 (d)-(e), Proposition 3.6 (the 3sc structure and the causal facts in
  Kerr-Schild time), Part IV'''' Lemmas 1.1 and 1.4, record 10.13, 10.14, 10.22, 10.65 (a).
- Stated and proved here, left unstated by the source: Propositions 5.2-5.3 (K^+ outward, sf, the interior both ways),
  and the chains of Propositions 7.1-7.2 (IV'''''2).
- Amended: Part IV'''' Lemma 1.4's reading of (4)-(5) (IV'''''3) and Theorem 2.1 (1)'s data surface (IV'''''1).
- Next: Part IV'''''' ([Hin26a] Theorem B.1 -> III.E Theorem 1.1 (4)); seat verifier 133 (D309).

### 4.233 Verifier 133 seated (D309): III.K's support classes back on t^flat_*

- Verifier 133 read the D302 repairs (III.I(16)), the D304 repairs (III.K, Part IV, II.G), Part IV' and Part IV''.
  Totals: 1 MAJOR, 8 MINOR, 18 NIT.
- MAJOR B-M1: III.K's support classes, chi_-, D and the collar had been moved to t_* (D304), but II.F Lemma 1.3 needs
  tau to be a time function for G_S, and dt_*'s margin near I+ is only O(mu_0 r^-2) (g^-1(dt_*, dt_*) = -18 mu_0 r^-2).
  Repaired by restoring t^flat_* (II.C Lemma 3.2 (2): robust margin), with the collar along the levels of
  (t^flat_*, omega); the half-integer powers at I+ lie in every slot's index set (III.C (3.2)-(3.3), Lemma 3.2 (a)).
  T_iota, T_K, T'' and D re-posed; Part IV''' and Part IV'' follow.
- MINORs: nu (vanishes near r_0, an inflow boundary for the backward problem; r/64 at infinity); the slab's top on
  t^flat_*; III.I(16)'s direct bound at every level; Part IV' in polyhomogeneous norms; Part IV'' Lemma 2.2's tame
  smallness, the uniqueness qualifier (also in III.C' Theorem 2.1), and the slab's curves (Part IV''' Lemma 1.1).
- NITs seated, among them: t -> -t is not an isometry of the gauge-fixed operator (Part IV, Part IV''); II.G Example
  3.2 cited; J3 Remark 4.4 quotes the amended (iii).
- Status: Part IV proved; Part IV', Part IV'' verified; III.K and III.I(16) repairs to be read.

### 4.234 Part IV'''''' written (D310): [Hin26a] Theorem B.1 at n = 4, and III.E Theorem 1.1 (4)

- PART-IV7-TFACE.md: the tf model's spectral family (Lemma 0.1, record 10.20 (i)) is Fredholm of index 0 (Proposition
  1.1: radial estimates with the n = 4 shift 3/2; relative index per S^3 sector, counts 2, 3, 1 for both the damped
  and the free operator) and injective (Theorem 2.1 = Theorem B.4 on edge-b spaces; Theorem 3.1 = section B.4 with
  (l, beta) = (-1/2, 7/2), (alpha_sf, alpha_cf) = (-5/2, 5/2)).
- Theorem 4.1: box^C_b is tf-admissible (I.C Definition 5.1) with every weight in [-C_0, 2), C_0 in [3/2, 100]; I.C's
  spaces are Theorem B.1's with q = 2 - beta; the adjoint half from surjectivity (I.C Theorem 4.3 (3)), without
  [Hin26c] (9.115) (IV''''''1).
- Melrose's relative index theorem is cited as the source cites it (IV''''''2).
- So III.E Theorem 1.1 (1)-(4) are proved at n = 4 in Parts IV''''-IV'''''', given (Dyn) (Part VI).
- Next: Parts V-VII; verifier 134 reading IV'''-IV''''' and the D309 repairs; IV'''''' to the next verifier.

### 4.235 Verifier 134 seated (D311): IV''''s adjoint weight; IV', IV'' and III.I(16) proved

- IV'''' (MAJOR, B-M1): at n = 4 a stationary function of decay rho^k lies in the dual space at weight a iff k > a + 5/2
  (2 from rho^a L^2(r^3 dr), 1/2 from the slab), so at (2.1) the adjoint step needs decay above C_0 + 3, which Lemma
  1.3 does not give at C_0 = 100. Repaired: (5.81) is applied at the weight (2.1) with C_0 - 1, which needs decay above
  C_0 + 2; h_* is below both bounds h_0 (findings (IV''''6)-(IV''''7)).
- IV''''' (A-m1, A-m2): on the extended domain, Lemma 0.5 (6) is used only in r >= r_sharp, and the strip below is
  covered by (5.68)-(5.69); general data pass to the limit by the energy identity's boundary term at every tau, and
  uniqueness comes from (a) for the extension by zero (findings (IV'''''6)-(IV'''''7)).
- III.K and IV''' (D-m1): the slab's restriction to r >= R_9 is made vacuous by c <= min(1/2, 1/R_9); nits D-n1, C-n1,
  A-n1, A-n2, B-n1 to B-n3 seated.
- Status: IV', IV'' and III.I(16) proved; IV''', IV'''', IV''''' verified (repairs to be read); III.K's D309 repairs
  read, correct, one new minor seated.
- Next: Part V ([CD03] Theorem 8.1 at n = 4) in writing; IV'''-IV'''''' and the D311 repairs to the next verifier.

### 4.236 Verifier 135 seated (D312): Part IV'''''' verified; IV'''-IV''''' and III.K proved

- IV'''''' (three minors): the deformation of the damping runs over [0, h^-1] for the fixed h; the annihilator of the
  range is independent of the admissible orders (dual estimate (B.28)), so the index is, and the sector count is made
  at I.C's order for the free operator; the adjoint step (c) (2) is stated on {tau > kappa}, which contains (B.40)'s a
  priori set (findings (IV''''''6)-(IV''''''7)). Six nits seated (the density r|d tau| x r^3|dr dg|, the record's
  Proposition numbering, the loss rho^-3/2, C_1 = 1, eps_X <= delta_r T, the Sobolev order named).
- The D311 repairs read and correct: IV''''s adjoint weight at C_0 - 1, IV'''''s extended domain and general data,
  the slab's c <= 1/R_9. Formatting slips of the D311 script (literal line-break escapes, one TeX space) repaired.
- Status: Parts IV-IV''''' and III.K proved; IV'''''' verified (repairs to be read).
- Next: Part V ([CD03] Theorem 8.1 at n = 4).

### 4.237 Part V written (D313): [CD03] Theorem 8.1 at n = 4, gluing to the Myers-Perry family

- PART-V-GLUING.md. The fifteen KIDs of 4 + 1 Minkowski data (Lemma 1.1). A linear flux identity, with a quadratic
  remainder, replaces [CD03] Appendix E (Lemma 1.2). The charges are limits of linear fluxes, with the rate
  rho^(2 + d - 2 alpha): for alpha > 3/2 no parity condition is needed (Proposition 1.3; finding (V1)).
- The Kerr-Schild Myers-Perry family, translated, rotated and boosted, has a C^1 charge map whose derivative at
  Tangherlini is invertible (Proposition 2.3). Schur's lemma for O(4) leaves four scalars, 6 pi^2, -6 pi^2 mu_0,
  -4 pi^2 mu_0 and -6 pi^2 mu_0. They are computed by hand and checked numerically on all 225 entries (d312/jac5.py).
  This is [CD03] Proposition F.1's equivalent near Tangherlini, the element its Remark 8.2 names as missing.
- Theorem 3.1: [CD03] Theorem 5.9's exponentially weighted solvability on Gamma(1, 4) is READ for every n. The
  continuity in the background that Lemma 3.18 needs is proved (Lemma 3.2). The pairings are R^(-2-d) times the charge
  differences plus O(R^(3 - 2 alpha)). Lemma 3.18 is proved. The glued data are smooth and equal a family member for
  r >= 4R.
- Replaces record 10.63 (a)-(c), 10.66 (a)-(e) and Proposition 10.47 (finding (V2)).
- Next: Part VI ((Dyn) and the record's computed inputs); Part VII (assembly); Part V to the next verifier, with the
  D312 repairs of IV''''''.

### 4.238 Part VI.A written (D314): the dynamical hypotheses at Tangherlini

- PART-VI-DYN.md. The dynamical hypotheses that Parts I-IV call (Dyn) are proved for 5D Tangherlini with III.B's
  t_*. (H6) and (K1) are proved for every b. The horizon's radial source has beta_0 = 2 mu^(-1/2), beta = mu^(1/2)
  and quadratic defining function |eta/xi|^2. The trapped set is r^2 = 2 mu with C = 4 mu; its separatrices are
  exactly f xi = +-(1 - 2 mu r^-2), with exact rates. (K3) holds through the periodic geodesic flow of S^3. (H8)
  holds through the conserved angular momentum.
- Lemma 5.2: the escape function (r^2 - 2 mu) xi has H F = 2r(xi^2 (r^2 - mu)^2 + (r^2 - 2 mu)^2)/(r^2 - mu)^2, zero
  only on Gamma, and z_0 F = (r^2/4f)(phi_s^2 - phi_u^2) exactly. It is for the perturbation to b near b_0 in VI.B.
- Checks: d313/dyn5.py (sympy).
- Next: Part VI.B ((Dyn) for b near b_0: horizon by continuity on the fixed conormal, trapping by [HPS77]
  persistence, (H8) by the escape function with no return), VI.C (gamma_Upsilon < min(s_C/2, 1/4), (C5)), Part VII.

### 4.239 Verifier 136 seated (D315): Part V verified, IV'''''' proved

- Part V: no step uses an n = 3 fact; the four scalars, Schur, and every READ of [CD03] confirmed. Three minors:
  [CD03]'s projection is orthogonal in the current metric, so Step 3 pairs with the KIDs converted by g' and the Gram
  matrix tends to the flat one (V7); the continuity in the background and the Lipschitz derivative are deduced from
  product estimates, not read (V8); Proposition 1.3's normalisation and the rescaling sentence are dropped (V6). Seven
  nits seated; the checks jac5.py and dyn5.py are now in proof5/checks/.
- IV'''''': the D312 repairs read, correct; proved.
- Next: Part VI.B ((Dyn) near b_0), VI.C, Part VII; Part VI.A and the D315 repairs to verifier 137.

### 4.240 Part VI.B written (D316): the horizon near b_0

- PART-VI2-HORIZON.md. The Myers-Perry horizon in III.B's Kerr-Schild coordinates is {r_A = r_+}, where r_+ is the
  largest root of (r^2 + a^2)(r^2 + b^2) = mu r^2. The proof is the exact identity g^-1(dr_A, dr_A) = Delta_b(r_A)/(r_A^2
  Sigma) (Lemma 1.1, checks/horizon5.py).
- A diffeomorphism, the identity outside |x| < 2R_1, fixes the horizon at |x| = r_h (Lemma 1.2). Its conormal bundle
  is then invariant (Lemma 2.1), and (H3)-(H4) hold uniformly in b by continuity on fixed compact sets (Proposition
  2.2).
- Next: Part VI.B', the trapped set near b_0. Hirsch-Pugh-Shub persistence gives the separatrices only C^r for each r
  on shrinking neighbourhoods, while (H7) asks C^infinity. So VI.B' uses the separability of 5D Myers-Perry null
  geodesics, as [Hin26c] uses Carter's constant for Kerr. Then VI.C (parameters) and Part VII.

### 4.241 Verifier 137 seated (D317): Part V proved, Part VI.A verified

- Part VI.A (PART-VI-DYN.md): 0 MAJOR / 3 MINOR / 8 NIT, all repaired. Lemma 0.1 now has a part (a) without causal
  hypotheses and a part (c), q' = q - 2F' G(nu, dr), so q is the same in t_s and t_* on Gamma. That gives q^Gamma = 4
  and beta_0 = 2 in t_*, and (K3)'s field changes by a factor equal to 1 on Gamma.
- (H8): the limits at infinity are read off directly. The uniformity is proved with absorbing sets {r > R, |xi_*| < eps}
  and, at the horizon, a backward-invariant set on the singular root. Before the repair, R_in at z0 = -1 was missed.
  Findings (VI.A4)-(VI.A6).
- Part V: verifier 137 read the D315 repairs and found them all correct; its one note (Step 5's choice of r') is
  repaired. Part V is proved.
- Next: verifier 138 on Part VI.B and the D317 repairs; Part VI.B' (trapping near b_0 by separability) in parallel.

### 4.242 Verifier 138 seated (D318): Part VI.A proved, Part VI.B verified

- Part VI.B (PART-VI2-HORIZON.md): 0 MAJOR / 3 MINOR / 6 NIT, all repaired, findings (VI.B3)-(VI.B5).
  - The conjugation by Psi_b is now proved. Transporting the fibre inner product keeps the thresholds. The spaces are
    kept because Psi_b is the identity on {|x| <= 5R_1/8} and on {|x| >= 7R_1/4}.
  - xi != 0 on all of the fibre-infinity characteristic set, so the rescaled field and the split by sgn xi are global.
  - The no-re-entry step now rests on H_b q > 0 on the boundary of U.
- Part VI.A: verifier 138 read the D317 repairs, all correct; its four notes are repaired (energy sign on
  Sigma^{-z0}, the maximal interval, F' < 3/2 for A', co-orientation of dt_s and dt_*). Part VI.A is proved.
- Next: Part VI.B' (trapping near b_0 by separability), then one verifier on VI.B' and the D318 repairs.

### 4.243 Part VI.B' written (D319): trapping near b_0 by separability

- PART-VI3-TRAPPING.md, checks/trap5.py (S1-S6).
- Separation: rho^2 g^-1 = A(r, p_r; E, Phi, Psi) + K(omega, eta). This holds in III.B's Kerr-Schild coordinates
  written as x = (r^2 - A^2)^{1/2} omega, with Kerr-Schild time. It is checked to 40 digits against III.B's Cartesian
  formulas. Everything is defined without an eigenframe of A.
- Radial structure: u P R is a quintic in u = r^2, and its reversal Q(w) = E^2 - Lambda w + mu Lambda w^2 at
  Tangherlini. Near b_0, Q stays strictly convex where Lambda >= mu_0/6 and positive where Lambda < mu_0/6. So the only
  trapping is a nondegenerate double root near r_ph with Lambda near 4 mu.
- Trapped set: Gamma_b = {r = r_c, p~ = 0, m = 0}, with separatrices phi_pm = p~ -/+ (r - r_c) sqrt(S) and the exact
  rates H phi_pm = -/+ 2T phi_pm. The bracket is 2 alpha sqrt(S), and the rate at b_0 is 4 (2mu)^{-1/2}.
- (K3) for every epsilon: the flow on Gamma_b projects to H_h, h = F(K, Phi, Psi), on T^*S^3. Regular orbits grow
  linearly, by a commuting frame. The singular sets are the tori p_theta = 0 = U' and the circles omega_1 = 0 or
  omega_2 = 0, all elliptic because K is near 4 mu_0, much larger than |A|^2. Compactness then gives a C_eps uniform in b.
- (H8): from the radial classification, the inward crossing of H_b at finite covectors, the backward limit set at
  fibre infinity (contained in dR_+-, by (H4)), and the Lyapunov function L = q + M rho_inf at the source.
- Next: verifier 139 on Part VI.B' and the D318 repairs to Part VI.B; then Part VI.C (parameters) and Part VII.

### 4.244 Part VI.C written (D320): the parameters

- PART-VI4-PARAMS.md: every parameter condition of Parts III-VI, each with file:line and what its threshold depends
  on (17 rows), and Theorem 2.1, a consistent choice made in order.
- The order is (0) Part VI's ball, then (1) (v_C, e_C, C_0) = (1/2, 1/102400, 100) with gamma_C = 1/h for h in H, then
  (2) gamma_Ups,H, e_Ups, gamma_Ups (avoiding a countable set), then (3) III.H's c_0, III.F'''s B(c_0) and B_*, then
  (4) the weights eps_+, eps_K, alpha, then (5) E_0, ell_0, ell_I, and last (6) III.K's eps, d_1.
- Checks:
  - III.E Theorem 1.1 is proved only at the record's point, for gamma_C off a countable set, and every part uses a
    single gamma_C.
  - III.D Proposition 6.3 is implied by III.D' Proposition 4.1.
  - III.F'' section 5 is closed by III.H Corollary 4.3.
- Next: verifier 139's report (VI.B', D318); Part VII, the assembly of Theorem 4, then one verifier on VI.C and VII.

### 4.245 Verifier 139 seated (D321): Part VI.B' verified

- Report: 0 MAJOR. VI.B': 1 MINOR, 13 NIT; the D318 repairs: 1 MINOR, 2 NIT; every other D318 repair correct.
- A-m1 (VI.B' Proposition 4.1): an exterior curve with r -> r_+ forward and covector -> fibre infinity was not
  excluded. Now: its forward limit set lies in dR_pm (by (H4)), so it eventually lies in N, where L > 0 does not
  decrease forward; contradiction. L and N are defined before the horizon paragraph (n9, n10), and the half-line
  argument covers exterior curves in both directions and interior curves backward (n5, n6).
- Notes: E != 0 in N (n1); C_eps e^{eps|s|} (n2); Lemma 3.2 at the rotated point (n3); Z_1, Z_2, Z_2' as families
  (n4); Sigma_{z0} = Sigma^flat_{z0} on O and a fixed neighbourhood for (H5) (n7); t - t_* = psi - T_mu (n8);
  eps_8 <= eps(delta) (n11); a notation paragraph (n12); S2, S6 and Sources (n13).
- VI.B B-m1: h' := |det D Psi_b| B_b^*(h o Psi_b) B_b, so Im_{h'} of the conjugate is the conjugate of Im_h exactly.
  B-n1: Phi_mu fixes x. VI.A B-n2: r_h = R_1 (III.B section 2).
- Status: VI.B' verified (D321); VI.B verified (D318), its repairs read, one further minor repaired, to be read.
- Next: Part VII (Theorem 4 assembled from Parts I-VI); then verifier 140 on VI.C, VII and the D321 repairs.

### 4.246 Part VII written (D322): Theorem 4 assembled

- PART-VII-ASSEMBLY.md, Theorem 0.2. (i) in the class: Lemma 1.1 (Theorem E at every order; after the shell g_lam =
  Tangherlini + smooth O(lam)); Lemma 1.2 (the record's domain enlarged to contain Sigma_IVP near the hole); Lemma 2.1
  (Tangherlini on Sigma_IVP, charges 6 pi^2 m); Proposition 2.2 (Part V in the class: equivariant Step 1, one-dimensional
  obstruction, |m - mu_end| <= C eta by the flux identity); Lemma 3.1 (naturality, choices averaged over O(4));
  Proposition 3.2 (III.K on G-fixed spaces: Pi S_theta, Pi Psi_NM; b = (m', 0), S = 0). (ii): III.K Theorem 4.3 on
  perturbations in its own class.
- Findings: (VII1) the paper's (ii) via gluing concludes for the glued data only (late times near the hole depend on
  the far data); (VII2) l_0 > 3 + eps_+ ((H4) with l_I < l_0), VI.C rows d1-d2 repaired as (VI.C4); (VII3) no Cauchy
  stability; (VII4) rate t*^(-(alpha-2)+eps); g and g_lam share data on a ball; (VII5) equivariant choices; (VII6) the
  a priori mass bound keeps the glued data O(lam)-close in III.K's weighted norm at a fixed radius.
- Next: verifier 140 on VI.C, Part VII and the D321 repairs; then the paper's Theorem 4 and section 8.7-8.8 updated to
  Theorem 0.2 and findings (VII1), (VII4).

### 4.247 Verifier 140 seated (D323): Part VII and VI.C verified; VI.B and VI.B' proved

- Report: 0 MAJOR. Part VII: 3 MINOR, 12 NIT. VI.C: 2 MINOR, 4 NIT. The D321 repairs: all correct, 2 NIT.
- VII A-m1: Lemma 3.1 for any closed subgroup G' of O(4) and G'-invariant data. A-m2: (C3') averages the families
  in b (T_{rho,b}, h_{b,s1}, h_{b,v1}) as families. A-m3: the nested cut-offs are chosen radial directly; the gauge
  1-forms are already radial (III.D3:30-32, IV5:36-38). Notes: h_tot = 0 where chi_K = 1; the flux sign; q smooth to
  second order; k = d_1 + 5; G-sup norms change II.G's constants; D_0; I15 (1.1) at b != b_0; J >= 2; |x| >= r_0.
- VI.C B-m1: the order was circular (Lambda contains pi_1 E^C_I, which depends on l_I). Now: data classes (step 3),
  then eps_+ < l_I - 3 (step 4), then the parameter set (step 5). B-m2: row b4, III.I(16)'s shrinking of B_*.
- III.K section 0 cross-refers to row d1 (l_0 > 3). VI.B': U_R's closure; the interior backward case spelled out.
- Next: the paper's Theorem 4 and sections 8.7-8.8 to Theorem 0.2; verifier 141 on the D323 repairs, the paper
  changes and the old repairs of III.A' and III.I(13); verifier 142 on those of II.B-II.E.
- Paper (D323): Theorem 4 restated as Part VII's Theorem 0.2 ((i) on Hintz's initial surface; (ii) in Hintz's data
  class; rate t*^(-2-eps) for eps < eps_K); sections 8.6-8.7, abstract and introduction aligned; a paragraph records
  (VII1). response5.py passes.

### 4.248 Verifier 141 seated (D324): Part VII and VI.C proved; III.A' and III.I(13) proved

- Report: the D323 repairs all correct (3 NIT, seated: invariant parameter balls in |mu - mu_0| + |A|_F, the c_C
  citation, steps (0)-(4)). III.A' (harm5 K2-K3 lists re-run) and III.I(13) (PART-III-I14-LEVELS.md): repairs correct.
- Paper: B-m1, Theorem 4 now fixes l_0 in (3, 4) and eps < eps_K first and takes Theorem 1 with K large on an enlarged
  domain; B-m2, sections 8.4 and 8.6 give t*^(-2-eps) for every eps < eps_K; notes: the second fundamental form's
  terms, conormal remainders, 'a continuation of their data' in the abstract and introduction, 8.7's slice.
- Status: every part of proof5 is proved except II.B, II.C, II.C', II.D, II.D', II.E (verified D197-D207).
- Next: verifier 142 on the old repairs of II.B-II.E and the D324 paper repairs.

### 4.249 Verifier 142 seated (D326): II.B and II.D proved; II.C, II.C', II.D', II.E repairs to be read

- Report (scratchpad d324/verifier142.md): 0 major; 5 minor, 9 nits, all seated (D327: 5, not 6). II.C (C8) now cites I.B Lemma 6.0
  for (5.9); II.C' Proposition 3.4 starts at T_flat = 1/C' (Omega_* contains {t_* >= T_flat}, not {t_* >= 1}); II.D'
  (H_G xi_0)/xi_0 odd on dSigma^-; II.E Lemma 3.3 (b) quantises e_+ with kernel near the diagonal in t_*, so
  E_+ v~ = 0; nits: Sigma^+ in II.B Lemma 3.3 (4) and (B2), M_0 in II.C' 2.4, zeta's support in II.D, (2.2') in (D'3),
  chi_Z wording in II.E, II.C's status line.
- Paper: sections 8.4 and 8.6 put 'for every eps < eps_K' before the smallness; Theorem 4 says eps_K is chosen after
  l_0 and below l_0 - 3; remainders in r^(-l_0) H_b^inf; Part VII takes alpha > 4 + eps_t in row w2 (its eps_t is the
  paper's eps). response5.py passes.
- Status: every part of proof5 is proved except II.C, II.C', II.D', II.E, whose one minor repair each is to be read.
- Next: verifier 143 on the D326 repairs (those four parts, II.B and II.D's nits, Part VII's eps_t, the paper).

### 4.250 Verifier 143 seated (D327): II.C, II.D', II.E proved; two searches replaced by enumerations

- Report (scratchpad d326/verifier143.md): 0 major; 2 minor, 6 nits. II.C, II.D', II.E: D326 repairs correct. II.C':
  sections 3.2-3.3 still on {t_* > 1}; now on {t_* > T_flat}, T_flat := 1/C' (to be read). VII: Theorem 0.2 now opens
  'for every eps_m > 0 and eps_t < eps_K'; section 4 runs VI.C through eps_K first. Nits: delta_U < C' in II.D Lemma
  4.1, zeta's neighbourhood inside U(delta_1), the status lines of II.B and II.D, 5 minor not 6, the paper's eps_K.
- The three search-based completeness claims inside proof5: VI.C section 3 (gamma_C) and II.F' Lemma 2.1 (b)
  (Definition 3.3 (3)) are now proved by complete enumeration: checks/gammac5.py (175 lines, 26 parts; 176 at D328) and
  checks/admiss5.py (104 lines, 5 parts) list every line that can use the property, with its class, and fail on any
  line they do not list; the completeness argument is that a use of a property must name its object.
- Remaining: III.I16 Theorem 3.1's census of the uses of b_0 (finding (I^(15)5)). Route: line-by-line ledgers of
  III.I'-III.I^(14) and III.J-III.J''' (8,055 lines) in five batches, each use of the base point classed against
  (P1)-(P6), Lemma 1.2 and section 2.
- Next: verifier 144 on the D327 repairs and the two enumerations; then the ledgers.

### 4.251 Verifier 144 seated (D328): II.C' proved; the gamma_C argument restated

- Report (scratchpad d327/verifier144.md): 0 major; 3 minor, 7 nits. A1 II.C' correct (nit: start slice on the boundary
  of Omega_*; now T_flat := 2/C', inside it): II.C' proved. A2 II.D section 4's setting still on {t_* > 1}: now on
  {t_* > T_flat}, delta_U < C'/2 (to be read). A3 VII correct (nit: eps(eps_m, eps_t)). B1 gamma_C: conclusion holds,
  premise 'a use must cite it' false ((C1)-(C5), III.E Proposition 3.1, III.E', a split citation at III.F:163). Now:
  a use at another value needs an operator with another damping parameter, named only through gamma_C, s_C, h or a
  rescaled E_C; gammac5.py G3 checks there is none; labels fixed (F':55 R, III.E':21 F, III.K:49 T). B2 correct
  (nit: why the five parts close the scope, added).
- Both enumerations now read their classifications from checks/gammac5.tsv and checks/admiss5.tsv, keyed by line text.
- Status: II.D, VI.C (section 3) to be read; III.I16's census: verifier 145 reading batch 1 of 5 of the ledger.

### 4.252 Base-point ledger, batches 1 and 5 seated (D329): one major gap found and repaired

- proof5/BASEPOINT-LEDGER.md holds the reading that replaces III.I16 Theorem 3.1's census (finding (I^(15)5)).
- Batch 1 (verifier 145, III.I'-III.I''''', 68 rows): M1, III.I'''' Lemma 2.4's boost identity is exact only at b_0
  (Ric(g_{b_0}) = 0 in C); at b, S^(-1)_{0,0;b} = id + Sdot(E^S_b). Repaired: III.I16 section 2.6, Lemma 2.7 (E^S_b
  supported in C, O(|b - b_0|), iota+-order >= 4 - delta) and Proposition 2.8 (|S^(-1)_{h,S;b} - id| <=
  C(||h|| + |S| + |b - b_0|), Neumann series). m1-m4 and n1-n5 seated in III.I16 ((P1), (P4), (P6), (i), (iv)-(vi)).
- Batch 5 (verifier 149, III.J''-III.J''', 51 rows): m2, III.J''' Theorem 5.3 at b unstated; now listed in Theorem 3.1
  as Proposition 2.5 at exact weights, with reasons in (viii). m1: III.H'' Proposition 1.1 cited; (J''2) superseded.
  Nits seated, among them the (J'3) status pointers in III.J'' and III.J'''.
- Next: batches 2-4 (verifiers 146-148, reading); then one reader of all the repairs.

### 4.253 Base-point ledger complete (D330): batches 2-4 seated, two more major gaps repaired

- Batch 2 (verifier 146, III.I''''''-III.I''''''''', 69 rows): M1, III.I''''''' Lemma 2.4's parameter identities are
  exact only at (0,0), and the base level (III.I''''''' Lemmas 4.3, 4.5, Corollary 4.6; III.I'''''''' Proposition 4.1's
  base step; III.I16 Proposition 2.5 Step 3) inverted its maps by continuity from (0,0). Repaired: III.I16 section 2.8,
  Lemma 2.11 ((2.7), E^mot_b supported in C, O(|b - b_0|)) and Proposition 2.12 ((2.8), direct bound); Step 3 cites it.
  m1, m2, n1-n5 seated (the list, fixed-b qualifiers, corrections #1-#4 named by part, #3 through (1.1), pointers).
- Batch 3 (verifier 147, III.I''''''''''-III.I''''''''''''', 57 rows): M1, III.I'''''''''''' Lemmas 2.3-2.4 used
  h_{b_0,v1} = 0. Repaired: III.I16 section 2.7, kappa_b (2.6), Lemma 2.9 (rotation rows T_{v1,b}, no inversion) and
  Corollary 2.10 (with m2, the level-3 conormal rotation tower). m1 (E_col b-independent), n1-n3 seated.
- Batch 4 (verifier 148, III.I^(14), III.J, III.J', 79 rows): no major gap; m3, reality at b, now in (P3) and
  Definition 2.3; m1, III.J as written with rows at b_0; m2, III.J' Lemma 1.1 listed; n1-n7 seated.
- III.I16 Theorem 3.1's proof now cites the ledger as a reading; findings (I^(15)5)-(I^(15)8).
- Next: one reader of all the repairs (D329-D330), with the D328 repairs of II.D and VI.C.

### 4.254 Verifier 150 seated (D331): II.D proved; the rotation state at b is a parameter change

- Report (scratchpad d330/verifier150.md): 1 major, 2 minor, 8 nits. Sections 2.6 and 2.8 correct in substance; II.D
  section 4 correct (II.D proved); VI.C section 3's conclusion holds.
- M1: Lemma 2.9 (c) subtracted T_{v1,b}(a~V) - h^{<=2}(a~S_V), putting S_V into a_s at z_0 - 1. Repaired: -1 in SO(4)
  is central, so in every MP isometry torus; h_b(S) odd, gdot_b and h_{b,v1} even ((P3), Lemma 1.1's proof), so S_V = 0
  and h_{b,v1}(V) = gdot_b(bdot_V) (Lemma 1.2's remark). Section 2.7 now subtracts T_{v1,b} alone; a_s unchanged;
  (2.4) with h^{<=1} as at b_0; finding (I^(15)9).
- m1: Prop 2.12's bound (2) for pairs F_1, F_2 with Sdot = 0 each (UNPARAM Lemma 4.1 (b)); Lemma 4.5's map through it.
- m2: VI.C section 3 widened to v_C, e_C, C_0 (fixed once by row c1); gammac5.py G4 (42 lines, damping5.tsv; X 4, D 2,
  S 2, F 15, P 19) and G5 (h := gamma_C^{-1} only in IV''''); negative controls caught.
- Nits: alpha_+ < 2; interiors and k_0 in Lemma 2.7; Lipschitz citations; the base level's block-triangular map; the
  reality gap named; (J'3) pointers in J'' and J''' and the J'' inventory row at b; the n8 citation.
- Status: III.I16 (sections 2.6-2.8, (P3) parity) and VI.C section 3 to be read; every other part proved.
- Next: the paper's section 8.8 written out over all 74 parts; one reader of D331 and the paper.

### 4.255 Verifier 151 seated (D332): VI.C proved; III.I16's parity argued from the constructions

- Report (scratchpad d331/verifier151.md): 0 major, 3 minor, 11 nits. A: D331 correct in substance (-1 an isometry,
  S_V = 0, section 2.7, Prop 2.12's pairs, G4-G5). B: the paper's 74-part account matches proof5/README.
- a1: the parity's written reason (B(b) is interior pairings, not leading terms; gdot_b's gauge correction skipped).
  Now from the constructions: omega_{b,s1}(S) = omegabar - P_b^{-1}Box omegabar odd, omega_{b,v1}(V) = V - P_b^{-1}Box V
  even, gdot^Ups_b = gdot_b - delta* P_b^{-1} eta_b even (III.F''' (2.1)); I15 Lemma 2.1's reparametrisation keeps it.
- b1, b2 (paper draft): 7,577 lines, not 8,055; 'no census of the source papers'. Nits: (P3)'s isometry reason (commutes
  with the spin; (3.2) even in x), companions dropped, (I^(15)5) wording, README's I16 paragraph, G4's wording and
  c_C, G5 widened (control caught), (J''4) discharged in J'', the paper's damping point, gaps named, md5 rows.
- VI.C proved (nits only). III.I16: the parity argument to be read. Paper: committed once III.I16 is proved.
- Next: one reader of the parity argument and the paper draft (scratchpad d330/dry3.md).

### 4.256 Verifier 152 seated (D333): every part of proof5 proved; the paper updated

- Report (scratchpad d332/verifier152.md): the parity argument from the constructions correct; III.I16 proved.
- All 74 parts of proof5 are proved. The three in-proof completeness claims: gamma_C and the damping's constants
  (gammac5.py G1-G5), Definition 3.3 (3) (admiss5.py), the base-point census (BASEPOINT-LEDGER.md, a reading).
- Paper: abstract, introduction, Theorem 4 (proved: proof5, Part VII Theorem 0.2), section 8.8's account through all
  74 parts, section 9, the review bullet (verifiers 74-152), the source table and the md5 table.

### 4.257 Part VIII written (D334): linear stability of 5D Tangherlini, III.K linearised at the Tangherlini data

- The paper's section 9 lists three things not proved: lambda_1 and delta not evaluated; section 8.2's linear
  statements deduced; the physical wavelengths. M asked that they be proved (D334).
- Section 8.2: proved as Part VIII, in the gauge of the nonlinear problem (Theorem 2.2; Corollary 2.3 in the class).
  The RW-gauge and Hung routes stay as deduced routes in other gauges; the gauge comparison is not written (Remark
  2.4 (a)).
- lambda_1 and delta: their existence is proved; evaluating them needs every constant of the 74 parts made explicit,
  and several are produced by compactness, contradiction and Fredholm arguments that give no number. Not attempted.
- Physical wavelengths (10 l5): no small parameter; a large-data problem. It would need a certified numerical
  solution with an a posteriori stability theorem in five dimensions; the record's own scheme fails before the shell's
  peak there (ROUTES 4.3 and the 10 l5 go/no-go). Not attempted.
- Next: one reader on Part VIII; then the paper's sections 8.2 and 9.

### 4.258 Verifier 153 seated (D335): Part VIII verified

- Report (scratchpad d334/verifier153.md): 0 major, 1 minor, 6 nits; D_hP5(0) = L, the support clause at c = That+7/4
  and Corollary 2.3's equivariance checked.
- m1: Lemma 1.1 (3) now differentiates Gauss-Codazzi along g + s hdot and uses (1). Nits n1-n6 seated.
- Next: one reader on the D335 repairs; then the paper's sections 8.2, 8.8 and 9.

### 4.259 Verifier 154 seated (D336): Part VIII proved; the paper updated

- Report (scratchpad d335/verifier154.md): the seven repairs correct; three textual nits (p1-p3), seated.
- Part VIII is proved. Paper: abstract, section 8.2 (a new first paragraph: the linear statement proved in the gauge
  of the nonlinear problem; the deduced routes kept beside it), section 8.8 (the seventy-fifth part), section 9 (the
  Settling bullet: lambda_1 and delta with the reason they are not evaluated; 8.2 proved), the review bullet
  (verifiers 74-154), the source table and the md5 table.

### 4.260 Certified existence at 10 l5: feasibility study, phase 0 (D337); lambda_1 and delta: the Drive paper

- M (2026-10-30): start the feasibility study for the certified computation. CERTIFY-10L5.md, phase 0:
  [Wu26] Theorem 2.2 READ again (its threshold eps(C0) and constant C(C0) are not explicit, the proof is a sketch,
  3+1 on S^2); dnull5.py D1-D5, the class in double-null gauge keeps the characteristic structure in five
  dimensions (Raychaudhuri with 1/3, the shift, Tangherlini vacuum, constraints ODEs on the cones); python-flint
  ball arithmetic installs and is fast; at 10 l5 the data are one broad pulse (0.48 and 1.51 periods); the closing
  condition delta + int eps < 1/(4 G T F^2) makes the certified growth factor F the deciding number.
- Go/no-go: G1 the double-null gauge survives to the end of the domain (next, F2: a prototype solver), G2 a
  certified linear constant near the measured propagator's, G3 the far-field data with a certified tail, G4 the
  axes. Phase-0 verdict: no blocker found; G1 decides first.
- M (2026-10-30): lambda_1 and delta; the Drive paper 'Self-Tuning Cosmological Constant Framework' (warp folder,
  PDF, 3 pp., read in full) may offer a framework. Assessment: it does not. It is a programme for a different
  system (M4 x K compactification, moduli coupled to a defect measure), with no proofs: its 'Infrared Vacuum
  Attractor Theorem' (p. 3) is stated without proof, and the paper calls itself the architecture for 'ongoing
  calculations resolving the global existence and regularity' (p. 3). It contains no estimate with explicit
  constants and no device for making a compactness, contradiction or Fredholm argument quantitative.
- Where lambda_1 and delta come from: Part VII section 4 takes delta := eps/2 and lambda_1 with C_R lambda_1 <
  eps/2, eps III.K's Nash-Moser threshold, which depends on the norms of the linear theory's right inverses. In
  proof5's parts the words contradiction, compactness (and compact embedding, Rellich), Fredholm and subsequence
  occur 19, 51, 74 and 28 times across 36 parts (a text count, not a census of arguments). Each such argument would
  need a quantitative replacement (an explicit lower bound in place of 'injective, hence bounded below'), on
  Tangherlini by certified computation of the separated ODEs and near it by explicit perturbation. Not attempted.

### 4.261 lambda_1 and delta: methods, the reduction, the ledger (D338)

- M (2026-10-30): deep research for methods of evaluating constants from compactness, contradiction or Fredholm
  arguments, then prove them. EFFECTIVE-CONSTANTS.md.
- Methods READ: Sekine-Nakao-Oishi arXiv:1910.00759v1 (Thm 2.1 p. 5, Lemma 2.2 p. 6: L^-1 through a Schur complement,
  ||S^-1|| <= 1/(1-kappa)); Ferreira-Leustean-Pinto arXiv:1810.01508v4 (pp. 1-2: Heine-Borel in place of sequential
  compactness, bounded functional interpretation); Goldstein-Jejjala arXiv:2609.21797v2 (Taylor models, 512-bit
  intervals, a Poincare-Miranda certificate for a black hole). Datchev-Jin through the search index only.
- Proved (section 2), read by verifier 155 and repaired: Proposition 2.1, II.G's threshold theta0 = max{16,
  16 eta_G^-2, (4K3/delta_G)^(1/(6d+2)), 1+K4, C1K5 + C2K3^2/2}, eps = theta0^-(8d+2), confirmed. Proposition 2.2:
  eps <= min{1, eps_NM/A_2d, eps_dat, eps_G}, delta = eps/2, lambda_1 := min(lambda_1.1, eta_gl/C_R, eps/(4C_R));
  verifier 155's M1 (three smallness thresholds of III.K missing), M2 (the loss d, eps_G's norm-equivalence
  constants, III.J's inverse operators inside the map), m1-m5, n1-n6 seated. To be read again.
- Not explicit: d (a sum of III.J''' losses, not added up), the tame and smoothing constants, delta_K, eps_dat,
  A_2d, eps_G's constants, the record's C_J and lambda_1.1, the gluing's eta_gl and C_R.
- E1 done: EFFECTIVE-LEDGER.tsv, 165 rows (N1 6, N2 15, N3 1, N4 13, F 41, G 37, X 52), each row checked by script
  to cite an existing file with a keyword within two lines; classes are a reading. Next: E1' (add up d), E2 (a
  certified N1 constant at Tangherlini for one operator).
- CERTIFY-10L5.md section 6a: F2's scheme from the Ricci components' second derivatives (computed).

### 4.262 lambda_1 and delta: verifiers 156-157; delta_K and eps_dat defined (D339)

- Verifier 156: 155's findings repaired; MAJ-1 the exterior (III.C'' Thm 3.1 -> III.C' Thm 2.1 -> IV'' Thm 3.1,
  Nash-Moser, d := 7), slab (IV''' Thm 2.2, Nash-Moser) and data-map (III.C'' Prop 4.1) thresholds that III.K Prop 1.2
  imports; MIN-1 eps_G is a threshold on ||P5(Psi(0))||, now eps_NM^G / A_2d (VII Lemma 3.1 at U = 0); MIN-2; nits.
- Verifier 157: those repairs correct; MAJ-1 three more (higher-order exterior and slab thresholds, III.C Cor 5.3's,
  III.B Lemma 5.2's w_0); MIN-1 the Part IV N2 site (IV7:383) is constraint damping, not on the exterior/slab path.
- Repair: Proposition 2.2 now defines delta_K and eps_dat as the suprema below which every smallness hypothesis III.K
  takes, directly or through what it applies, holds (finitely many, so positive); the enumeration is an inventory, not
  claimed complete; E1'' finishes it. To be read.

### 4.263 lambda_1 and delta: verifier 158; admissible pairs (D340)

- Verifier 158: the chain VII section 4 -> lambda_1, delta correct (no condition on R, k, J or lambda outside
  Nash-Moser, Part VII's own and III.K's); MAJ-1 the sup-definitions of delta_K, eps_dat ill-posed (joint data-and-U
  hypotheses; U-thresholds depending on the data); MIN-1 section 0 overstated; MIN-2 orders and the eps-choice in
  III.K Prop 1.2 (3); MIN-3 g_1 at III.C:341; NIT-1..5.
- Repair: an admissible pair (eps_dat, delta_K) in (0,1]^2, for which every non-Nash-Moser smallness hypothesis of
  III.K holds on {data < eps_dat in H^d1} x {|U|_3d < delta_K}; it exists by III.K's proof (K:383-388, 410-411,
  465-469) and is down-closed; the eps-choice is made first; section 0 says the pair is defined, not computed.

### 4.264 lambda_1 and delta: verifier 159 (D341)

- Verifier 159: the admissible-pair definition well-posed and down-closed; MAJ-1 its existence cited K:410-411's
  wording instead of the proof's quantifiers; MIN-1 eps_m, eps_t, eps_K missing from section 0 and the not-explicit
  list; NIT-1..5 (stale D-numbers, "proves" before the read, eps_NM's C_k as data-ball bounds, the data map's
  topology unnamed, U's class B^inf). All seated; existence now from II.G's domain {|U|_3d < delta} with delta uniform
  over small data, then a shrink for the S-dependent and joint conditions. To be read.

### 4.265 lambda_1 and delta: verifier 160 (D342)

- Verifier 160: existence nearly valid; MAJ-1 delta's uniform lower bound unstated (now: eps_NM uniform, K:412, and
  theta0 >= (4K3/delta)^(1/(6d+2)) give delta >= delta_* > 0); MIN-1 III.C 4.4's S-dependent threshold is inside
  Lemmas 2.2-2.3, not a shrink; NIT-a..c. Seated. One narrow read of the clause follows.

### 4.266 lambda_1 and delta: verifier 161, no major (D343)

- Verifier 161: the existence of an admissible pair valid, no major; MIN-1 the tame constants taken >= 1 so that
  delta_G >= 4 eps_NM^((6d+2)/alpha) uniformly; NIT-1 III.C Cor 5.3 named; NIT-2 delta_G. Seated. Section 2 stands
  as a reduction (Proposition 2.1 confirmed by 155; Proposition 2.2 after 156-161).

### 4.267 10 l5: F2, the prototype double-null solver (D344)

- dnsolve5.py: the class in double-null gauge with the record's regular combinations (axis conditions identically);
  Ric_11, Ric_22, Ric_xx -> (R, m, n)_uv; Ric(Y, d_v) -> W_uv; Ric_vx -> shift transport; diamond scheme, Chebyshev-Gauss
  in x; Kretschmann from exact Christoffels and their exact derivatives. Selftest S1 (Tangherlini, ratio 3.90), S2
  (flat 2e-26; Tangherlini K median rel. error 6.4e-3), S3 (control W + 0.01 v, ratio 1.00) pass.
- Coordinate: u := -r on the first cone squeezes the late interior (r - 1 ~ (r0 - 1) e^v); grid u = -1 + a sinh xi,
  a = 0.002, fixes it (107 rows in 0.54 <= R <= 1 at v = 1.6).
- lambda = 1 (L = 100): second zero of R_v at v = 1.425, before the record's persistent break at the first seed
  (1.500; its 1.4516 was a single-step excursion, D43-D44; 1.583 at the second seed; corrected D346), passed;
  constraints converge at second order to v = 1.5; x_K > 1 near the cut from v ~ 1.45 (wave curvature), so D_q <
  {R >= r_core}; D_q computed (113,682 of 125,265 strip cells at 800 x 360, reaching v = 4.5); converged on D_q to
  v ~ 2.0 (400 vs 800), shears not converged beyond; axis growth from v ~ 1.61 lies outside D_q.
- lambda = 0.3162 (L = 1000): runs to v ~ 3.3-3.4; axis growth at x = +1 just outside the horizon, onset moving later
  with M (1.86, 3.28, 3.44 at M = 6, 8, 12) and with (u, v) (3.28, 3.36): resolution, not the gauge.
- G1 not yet answered to the end of the domain; next: angular resolution with an axis filter, refinement at D_q's
  edge, D_q at lambda = 0.3162, then F3.

### 4.268 The linear result in any gauge: Part IX (D345, D347)

- proof5/PART-IX-GAUGE.md: on D_U(Sigma_U), U open in N°, a linearised vacuum solution whose Cauchy data are those of
  L_Z g is L_X g, X unique up to Killing fields; Part VIII's solution in any gauge is dot g + L_X g (Corollary 2.3).
  Domain: D_{N°}(Sigma°) globally hyperbolic, contains N° cap {t_IVP >= 0} (Lemma 1.2); [BGP] Theorem 3.2.11 for data
  without compact support (Lemma 1.1). Gauge vector: 2 delta G delta^* w = Theta(k), w = 0 and nabla_nu w = Y^flat on
  Sigma; then k - L_X g has zero data and vanishes (uniqueness for DRic + delta^* Theta, normally hyperbolic).
- checks/ix5.py X1-X7 (identities by exact expansion or at four random rational points to 60 digits; seven controls).
- Not proved: the size or decay of X, so the Regge-Wheeler-type and harmonic-gauge decay routes of section 8.2 stay
  deductions. Verifier 162: sound; M1-M4, N1-N5 seated (D347).

### 4.269 The equality case mu0 = sqrt72 l5^2 (D346, D347)

- EQUALITY5.md: g_lam = g0 on Omega cap {v <= v_s} (Proposition E.2; the record's energy inequality with a null face);
  the boundary is null there, spacelike for g_lam on v >= v_s + eta once lam <= lam_eta (E.3); the layer between, of
  width -> 0 with lam, undecided (Remark E.6: margin and perturbation both flat at v_s); D_T^lam, within c lam eta* of
  D_T inside x_K <= 1, whose inner boundary nothing enters (E.4); the spheres' horizon at equality (E.5).
- checks/eq5.py E1-E6. Verifier 163: sound; MINOR-1..4 and nine nits seated (D347).
- Open: the causal character of x_K = 1 itself for g_lam in the layer, a question about the exact solution near v_s.

### 4.270 The loss d (E1'): bookkept, not a number (D347)

- LOSS-D.md: d = sum over III.J''' section 3's rows of (steps x step loss). Step losses explicit in the weights
  (II.G' Corollary 4.5's l = 2 l_3 + l_4 + l_5 and its parts, Proposition 3.5, III.F' Corollary 3.4, III.G''' 2.2/2.4,
  III.G' Theorem 3.1 (2) <= 2(ceil(l_I - Re lambda) + 2), III.I Theorem 5.3's +5, N_*), except five (III.A Proposition
  4.2 (1); II.G' Corollary 4.2; III.G''' Corollary 3.1 and Proposition 3.7; III.I'' Lemma 4.2). Weights fixed only by
  inequalities at n = 4 (l_I > 3 + eps_+, alpha_K = 4 + eps_K, eps_ind, ...); level and round counts chosen.
- Next: E1'a (numbers for the weights from the computed index sets), E1'b (the five losses), E1'c (the counts).
- Finding LD1: k'' (III.K, Part VIII) was never defined; now k'' := max_{k <= N} k'_k from III.K Proposition 1.2 (3).
- Finding LD3 (D348, restated after verifier 164): I15's beta-chain has steps below alpha - 4 <= eps_K and climbs
  more than 2, so K > 2/eps_K > 6.8e5 at the record's parameter point (eps_K < eps_ind < 3e-6); each level costs 2 in
  III.J''''s accounting, so the d it produces is > 1.3e6 and N = 21d + 6 > 2.8e7. Nested inside, I14's level-3 loop
  rises by eps_ind per round at every beta-level: about 5e10 rounds over the chain, and d beyond that if a round costs a
  derivative (E1'b). These bound the d this proof produces, not the optimal loss. Levers: the parameter point, a larger
  per-level gain, another proof of the level step (the source's one-step route is closed at n = 4).
- Verifier 164 (D348): M1 (d is a recursion over calls, not a flat sum over rows), M2 (LD3's scope), M3 (the nested
  level-3 loop), m1-m4, nits; all seated, with the k'' scope in III.K repaired at the e_S bound.

### 4.271 10 l5, G1: angular resolution at lambda = 1 (D351)

- dnsolve5.py --run ... [p]: exponential filter exp(-36 (k/(M-1))^p) on the Chebyshev coefficients in x after each
  diamond. Runs (scratchpad): M = 12 (p 32) at 400 x 180 and 800 x 360, M = 16 (p 32, 64), 24 (p 64) at 400 x 180,
  M = 12 (p 32), 16 (p 64) at 400 x 720; D_q recomputed on the M = 12 filtered 800 x 360 run (111,891 cells).
- On D_q: converged in (u, v) and in M to v ~ 1.5 (M16 vs M24 |dm| <= 4e-5). On [1.5, 2): M12/M16/M24 differ by
  0.36-0.44 in m (of 0.44-0.55); dv/4 changes M16 by 0.03 (not a step-size limit). The filter bounds the shears (no
  growth to ~100 as unfiltered) but does not give convergence.
- The discrepancy starts at the axis x = -1 near u ~ -1 (the seed's horizon generator), R ~ 0.7-1, from v ~ 1.6; the
  M24 Chebyshev spectrum of m flattens (3e-7 at v = 1.6, 1e-3 at 1.75, unresolved at 2.2). M = 24 at dv/4 and M = 32
  stop on a singular 4 x 4 solve.
- Correction: D344's "converged on D_q to v ~ 2.0" was (u, v) convergence only; in angle, to v ~ 1.5-1.6.
- Next: an axis treatment without division by 1 - x^2, or axis-concentrated angular grids; then D_q at lambda = 0.3162.

### 4.272 E2 at one operator (D350)

- E2-PILOT.md, checks/e2pilot5.py P1-P2: box on 5D Tangherlini by harmonics. V_l = f((l(l+2) + 3/4)/r^2 + 9 mu/(4r^4)),
  I_l = (l(l+2) + 3/2)/sqrt(mu). Off the real axis ||R_l(sigma)|| <= 1/dist(sigma^2, [0, inf)), uniform in l. On it,
  for every l and real sigma != 0: |W| >= 2|sigma| (flux), |u|^2 <= 2 exp(int V/|sigma|) (Gronwall), and the cut-off
  resolvent <= (Lambda/|sigma|) exp(I_l/(2|sigma|)): III.D Proposition 6.2's injectivity with a constant, per harmonic.
- Open: uniformity in l (an Agmon bound in the forbidden region), sigma -> 0, the trapping energies at large sigma, the
  record's b-Sobolev norms, Im sigma -> 0 joined to the real axis.

### 4.273 E1'a's first question: the indicial gap over the damping parameters (D353)

- checks/gapscan5.py G1-G3: the gap near 2 of box^C's scalar indicial roots (damping5.py's polynomial, weight 2/3) is
  about c(v) h for h << e (c(1/2) ~ 3.06), flat in e; over e <= e_0(v) ~ 6.9e-5 v^2 (semiclass5 W4) and h <= e (U6) its
  largest value is ~3.1e-5 (v ~ 0.45, h -> e = e_0), against 2.93e-6 at the record's point. So eps_ind < 3.1e-5 at every
  admissible point; LD3's counts improve by at most ~10 (K > 6.5e4, d > 1.3e5, nested rounds > 5e8). An order-one gap
  needs another constraint damping.

### 4.274 G1 at 10 l5: the axis nodes and 𝒟_q with |K| (D354)

- The singular solves at M = 24, 32 and part of the angular disagreement were rounding in the 4 x 4 uv-solve at the
  nodes next to an axis (error ~ (1 - |x|)^-4.5 eps). Fixed by an 80-bit long-double solve there (dnsolve5.py `ld k`,
  selftest S4); `reg` does not cure it. 𝒟_q rebuilt from |K| (K < 0 where the runs disagree): 111,370 common cells at
  M = 24, 32. Every field converges in M to v = 1.5; d(M24, M32) in m is 0.68 on [1.5, 2) and 3-20 later. The onset is
  at x = -1 inside the horizon (d > 1e-4 at u = -0.964, v = 1.650), where x_K = 0.81: inside 𝒟_q, so not removed by
  the curvature cut. Second seed: converges to v ~ 3-3.5, then n steepens at x = +1. Open: an axis treatment or a
  mapped grid at the axes (CERTIFY-10L5.md section 6b).

### 4.275 E2.5: the cut-off resolvent uniformly in l at real sigma (D355)

- E2-PILOT.md section 3b, checks/e2pilot5.py P3. Lemma E2.5a: H = |u'|^2 + (sigma^2 - V_l)|u|^2 has H' = -V_l' |u|^2,
  so H <= 2 sigma^2 for u_h left of the barrier's peak and for u_inf right of it. Lemma E2.5b: with the flux, the signs
  Re(conj(u_h) u_h') >= 0 at the left end of I and Re(conj(u_inf) u_inf') <= 0 at the right end. Proposition E2.5:
  then ||chi_I R_l(sigma) chi_I|| <= 1/min_I (V_l - sigma^2). Corollary E2.6 (mu = 1, I = r in [1.2, 4]): closed-form
  sufficient conditions, monotone in l; l_0 = 14, 19, 50 at sigma = 0.3, 1, 3 (3, 7, 18 by quadrature); bound
  <= 1/((15/256)(L + 3/4) - sigma^2), asymptotically 17.07/L. Open: l < l_0, Proposition E2.4's constant (where
  kappa_I^2 > 0 only the end signs are missing; where kappa_I^2 <= 0 another argument is needed); Im sigma -> 0; the
  record's b-Sobolev norms. Verifier 165: sound, 7 minor and 6 nits seated (D356).

### 4.276 E1'b: the six non-closed losses in closed form (D357)

- LOSS-D.md section 2b. III.A Prop 4.2: (1) l = 1 + n_iota + 2 max(n_K + floor(beta_K), n_I + floor(B)), (2) l = n_iota +
  n_K + ceil((max(beta_iota - beta_scf, beta_K) + eps - 1/2)_+). II.G' Cor 4.2 and III.I'' Lemma 4.2: ell =
  max(ceil((theta_in/2 + 3 - beta_scf)_+), ceil((s_c - 1)_+)) (in the proofs, II.G2:698-702). III.G''' Prop 3.7 and Cor
  3.1: Prop 2.4's l' = 2 ceil(ell_I) + 10 + sup d (Cor 3.1 (2): + 2). III.G' Thm 3.1 (2): d_1 = 0, d(lambda) = 6 +
  ceil(max(0, Re lambda - 2 + delta)) + ceil(max(0, Re lambda - 3/2) + delta) + 2 ceil(ell_I - Re lambda), not monotone;
  sup over a strip <= max(7 + 2 ceil(ell_I - lambda_-), 12) for 3 < ell_I < 3.5, so l' = 30 with lambda_- just below
  3/2. Verifier 166 (D358): forms and d_1 = 0 hold; the strip rule repaired; s_c >= 0 chosen; Cor 3.1 (2) loses l'.
  Remaining: E1'a (numbers for the data and the free choices) and E1'c (the counts).
- D365 (LOSS-D LD6): the beta-chain's step alpha - 4 is the gain of R_q (coefficients of K+-order (alpha - 2)-), and the
  cap alpha <= 4 + eps_K is the order four zero-energy solves reach (I12:14-16, 528-529), no obstruction named. Lever,
  not examined: a fifth solve, if the sigma^4 zf term exists at n = 4 (logs in even n to check), takes alpha towards 5,
  the step to about 1 and K from > 6.5 x 10^4 to about 3. The nested level-3 loop (eps_ind) is untouched.
- D377 (LOSS-D LD7, deduced from the record's text): the cap alpha <= 4 + eps_K is not the number of solves --
  four zf-Taylor terms serve every alpha <= 5 (I12:16) -- but I11 Definition 1.3 (G): no point of Lambda in
  (3, 3 + eps_K], and Lambda contains 2 + E_ind, which has 3 + 2.93e-6 (the damping root lambda^C - 1). So
  alpha - 4 < eps_K < gap, and LD6's lever reduces to LD5's (a damping with a gap of order one). Open: whether the
  cascade can treat the point 3 + gap instead of excluding it.

### 4.277 E2.7: the cut-off resolvent above the barrier (D359)

- E2-PILOT.md section 3c, checks/e2pilot5.py P4. V_l is unimodal for every l (r^3 V_l' a convex quadratic in 1/r^2
  negative at 0). If sigma^2 > max V_l: |u_h|^2, |u_inf|^2 <= 2 sigma^2/(sigma^2 - max V_l) everywhere (H non-increasing
  where V rises, H/(sigma^2 - V) where it falls), so ||chi_I R_l chi_I|| <= Lambda sigma/(sigma^2 - max V_l). Open: the
  harmonics with max V_l >= sigma^2 below l_0 (5 <= l < 50 at sigma = 3).
- D379 (E2-PILOT section 3e, checks/e2morawetz5.py M1-M3): Lemma E2.8, a 1D Morawetz bound. phi = tanh((r_* - x_p)/s),
  s < 1 (horizon tail), w = -phi V_l' - phi'''/2 >= 0 gives ||chi_I R_l chi_I|| <= ((2/m' + (M' + 2|sigma|)^2/w_I)/w_I)^1/2
  at every real sigma != 0, bounded as sigma -> 0. Every l >= 1 (computed to l = 30; l = 0 has no admissible s): B_l(3)
  <= 21.3 on the band 5 <= l <= 17, where only e^54 held. Not certified (w >= 0 on a grid); coarser than computed norms.

### 4.278 Beyond D_T: the interior after the shell (D360)

- BEYOND5.md. Theorem 0.2 (i)'s g lives on {r >= r_0 = sqrt(mu_end)/2} to the future of Sigma_IVP; if mu_end <= 16
  sqrt72 l5^2 then r_q >= r_0 and g covers {r >= r_q} for all later times (Proposition 6.1, deduced). It agrees with
  g_lambda on the domain of dependence of Sigma_IVP cap {r < R} (CB-G; (VII4) to write), not at late times near the hole
  (VII1). Open: (a) write (VII4); (b) g_lambda's own data on all of Sigma_IVP, in III.K's class, then Theorem 0.2 (ii);
  (c) r_0 lowered below r_q (census of r_0 in proof5); (d) or the finite-r-time slab by uniform Cauchy stability.
- D363, (c): the census (checks/r0census5.py, BEYOND5-R0.tsv). 308 lines in 25 files of Parts III-VII: 108 another
  r_0 (III.C''s exterior radius, the source's r_c), 19 definition and domain, 128 only "{r = r_0} spacelike, dr future
  timelike, inside the horizon", 48 through a constant, 5 put R_1/2 into an inequality (III.B 157-159, 244; VI3 374),
  each of which holds for every smaller radius once eps_param <= r/(4R_1). Proposition 6.2 (deduced from the census):
  with r_0 := min(R_1, r_q)/2, Proposition 6.1 holds for every mu_end, without (1.1). Rests on: a reading, not a
  re-proof; IV6's finding (IV'''''5) for [Hin26a] Prop 5.1 at m; Part VII's delta'_0 nearer q_0.
- D366: verifier 168 seated. MAJOR: IV6-SOLV's Lemma 0.5 (6) (record 10.14 (ii)) was checked on [r_h/2, oo) only; 8
  lines reclassed VAL (now SPC 120, VAL 13). It holds on (0, r_h) by hand: the inner piece dt + (v/2) dr has <c, dr> =
  1/4 + 3mu/(4r^2) > 0 and G(c) < 0, and f < 0 there. Minor: eps_param := min(1/20, r/(4R_1)); Lemma 3.3 (c) via
  r_A^2 > 3||A||^2; any delta_0 in (0, r) for F3/F4; r < 4R_1/7 in VI (r_h = R_1); Part IX outside the census.
- D367, (a): (VII4) written as BEYOND5 Lemma 6.3 (deduced). g_lambda on the past domain of dependence of Sigma =
  Sigma_IVP cap {r_0 < r < R} (in a neighbourhood V where t_IVP is a time function) and g after Sigma_IVP glue into one
  smooth vacuum spacetime N, since Ric = 0 in Gaussian normal gauge fixes every normal jet from (gamma, k). The future
  developments are identified on their maximal common development ([Sbi15] arXiv:1309.7591 Thms 2.6, 2.7, 3.4, 3.13,
  READ). Open: how far that common development reaches; Sigma's acausality in all of Omega'.
- D368-D372: BEYOND5-R0-PROOF.md re-proves each Part at r_flat (batches 1-3: Parts I-II, III.B-III.K, IV; verifiers
  169-171). Found (verifiers 170-171): the record's Part VI puts Part I's artificial boundary at 5R_1/8, while III.K and
  Part VII use III.B's R_1/2, so the record's development is controlled on {r >= 5R_1/8} only. Repair: r_0^A := r_flat
  with the collar delta_0 := min(R_1/16, r_flat/4). Proposition 6.1's bound 135.76 l5^2 holds with the repair; without
  it the condition is mu_end <= 55.61 l5^2, which the first seed fails. Proposition 6.2 assumes the repair. Batch 4
  (V-IX, including Part VI's checks at the new radii) open.
- D373: the repair is made in the record. Part VI now sets r_0 := R_1/2 (III.B's radius), delta_0 = R_1/16, so the
  collar reaches 3R_1/8, where Lemma 1.1 defines g_b and t_* by III.B's formulas (Lemma 3.3 (c) at |x| >= R_1/4, as
  IV6-SOLV section 0); VI2-VI3 read on {|x| >= 3R_1/8}; VI3 374-375's r_0 - delta_0 is 7R_1/16. Findings (VI.A7),
  (VI.B'6). Census
  320 lines (CON 60). Verifier 172 reads it.
- D374: BEYOND5-R0-PROOF.md batch 4, sections 7 and 9-11: Part V (only |x| >= 50R_1 used), Part VII (delta'_0 in
  (max(0, q_0 - r_flat/2), q_0), allowed by the record's (1.1); Lemma 1.2 from r_flat), Part VIII (III.K's sets at
  U = 0; II.C Lemma 3.2 (2) at the repaired radii), Part IX (II.C Lemma 3.2 (1) cited from R_1/2: a third site of the
  mismatch, closed by D373). Section 8 (Part VI at r_flat) after verifier 172; then one verifier for batch 4.
- D375: verifier 172 seated. M1: the forms of III.B Definition 6.1 must exist on the collar; they are smooth for
  r > 0, c_C past timelike (cform5.py C2), so the operators of III.D-III.F and IV'''' are defined on {r > 3R_1/8}
  (VI.A7). m1: F1 cited for its Lorentzian argument only. Census VI-DYN 81 reclassed VAL (322 lines: CON 61, VAL 14).
  Nits: VI3 and README marked amended, (VI.B'6) names Proposition 4.1. BEYOND5-R0-PROOF section 8 (Part VI at
  r_flat) written; batch 4 to verifier 173.
- D378: verifier 173 seated on batch 4 (no major). m1: II.F Lemma 1.3's compactness near {r = r_flat} needs
  II.C Lemma 3.2 (1) (as II.F Lemma 1.4 (a)); the record cited II.F 7.4 (the iota+ model); now named at VIII:284-286
  and III.K:459-463. m2: Part VII's constants depend on r_flat through delta'_0, c_0, T'. Nits seated. Re-proof done.

### 4.279 More families: several dusts, angular separation, Vlasov (D361)

- FAMILIES5.md (scoping, nothing proved). The single-family uses: exact eikonal v, one null dust, one lambda^-1 coupling
  s = w(l, l), one phase-shift identity and transport. N families: N couplings and cross terms
  [d^2_{theta_j} g1^(j)](l_k, l_k). READ abstracts: Touati arXiv:2402.17530 (multiphase, any number of dusts, 3+1, no
  symmetry); Huneau-Luk arXiv:2506.21779 (Vlasov via dusts, U(1), small localized). First step proposed: two-phase
  Stage 0 (v ingoing, u outgoing) in the class; mixed harmonics non-resonant, solved by division.
- D363 (deduced from the record's Stage 0): the cross couplings enter only through the second-harmonic gauge terms
  chi dv^2 and chi' du^2, W_TT being purely angular; a gauge removing chi, chi' at first order would remove them.
- D364 (deduced): chi dv^2 is pure gauge at order lambda (L_Z g0 for Z = lambda^2 Phi(X, v/lambda) grad v,
  d_theta Phi = chi/2). The record's wave-map gauge forces it, the reduced symbol vanishing at the null dv; a generalised
  wave gauge with fixed source H = lambda h(X, v/lambda) dv meets the vv second harmonic algebraically, so
  chi = chi' = 0 and the leading cross couplings vanish (a gauge artefact). Open: constraint propagation with H,
  comparison of gauges, no other lambda^-1 coefficient in the two-family linearization (step 4).
- D376 (FAMILIES5 section 4b; checks/stage0two5.py, computed): Stage 0 of the two-phase ansatz on a general round
  double-null background closes. R^(-1) = 0; the double mean of R^(0) is Ric(g0) - K_in dv^2 - K_out du^2 with no
  cross term, K R^3 = alpha(v)^2/3 and beta(u)^2/3 with the record's H (two round dusts, two Isaacson laws); the pure
  harmonics are lead5's per family under the R^(-3/2) transports; the mixed harmonics are present and ghat_2 solves
  them by division (symbol -e^(-2 sigma) n1 n2). Open: the two-dust background in the class; later stages; the
  energy estimate with two couplings.

