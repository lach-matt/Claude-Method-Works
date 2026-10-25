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
