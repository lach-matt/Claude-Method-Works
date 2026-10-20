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
| Mass at I⁻ | published 5D Bondi law, time-reversed; prove g_λ's expansion | [TTS09], [KK25] | numerics' offset coefficient |
| 10 l5 | a posteriori existence: Theorem E with certified numbers | [CCRT07], [MP11], [RT12] | growth factor exp ∫K |
| Settling | generalized wave map gauge, finite modulation, in the class | [Hin26], [KS17] | linear stability, wave gauge |

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
  plus δμ ([HKW18] Theorem 1). The four-dimensional template is Hung, Keller and Wang's generalized-harmonic-gauge
  paper and Johnson's (both cited in [Hin26], p. 6).
- L2: constraint damping in five dimensions ([Hin26]'s companion [Hin26a]).
- L3: decay rates in the class (r^p hierarchy; [Sch10]'s higher-dimensional estimates; [HKW18]).
- N: the nonlinear iteration of [Hin26], or a bootstrap with these rates.

The low-energy analysis is where five dimensions differ: the spatial dimension is four. It must be redone, not copied.

**Cheap companion (computed, to do).** Extend settle5.py T3 to show no growing mode in the class for l = 2, …, 10, and
measure the late-time tail of the l = 2 master fields. That fixes the decay rate the nonlinear step must use.

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
- [IK03], [HKW18], [Hol08], [Sch10], [CLY03b], [AB26]: as in RESPONSE-HL-5D.md.
