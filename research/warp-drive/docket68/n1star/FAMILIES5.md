# FAMILIES5 -- more matter families: several null dusts, angular separation, Vlasov

Status: scoping note (D361). Read by verifier 167 (D362), findings seated. Section 1's two deductions on the cross
coupling added (D363-D364). Section 4's first step computed (D376, section 4b: `checks/stage0two5.py`; read by verifier
174, D380). Nothing proved beyond Stage 0.

The paper's open item "more families" (RESPONSE-HL-5D.md section 9): "Several dusts, angular separation, and the passage
to Vlasov matter are not attempted." This note sets out what each would need, given what the record's proof uses of
having a single family. It names the published work closest to each, read at its abstract, and proposes a first
computable step.

## 1. What the proof uses of one family

- **The phase.** v is an exact eikonal of g0 (paper section 4: "The phase is v, an exact eikonal of g0"), and
  g0⁻¹(dv, dv) = 0 makes the λ⁻¹ term of the expansion vanish (Stage 0).
- **The averaged stress.** It is one null dust along dv, and the θ-mean of the leading equation fixes dμ/dv (2.6)
  (Proposition 2.3).
- **The one large coefficient.** In the linearization (5.1) the only λ⁻¹ coefficient couples s = w(ℓ, ℓ) to the wave
  (section 5.1). The phase-shift identity (Lemma 5.1) comes from the single translation θ ↦ θ + c.
- **The decomposition.** w = h + φ [∂_θ g1], with φ transported along ℓ (5.2). Contracting with ℓ ⊗ ℓ kills every λ⁻¹
  term, because [∂_θ g1](ℓ, ·) = 0 (section 5.2).

With families k = 1, …, N, phases φ_k and generators ℓ_k, the ansatz becomes a profile in (X, θ_1, …, θ_N). (4.1) holds
for each θ_k separately, so there are N phase-shift identities, N large couplings λ⁻¹ s_k [∂²_(θ_k) g1^(k)] with
s_k := w(ℓ_k, ℓ_k), and N transported phases φ_k. Contracting with ℓ_k ⊗ ℓ_k kills family k's coupling but not family
j's: [∂²_(θ_j) g1^(j)](ℓ_k, ℓ_k) is not zero in general. These cross couplings are the new analytic difficulty.

**Where the cross coupling sits in the class (deduced from the record's Stage 0; to be computed in step 4).** The
record's first-order wave is W = W_TT + χ dv² (`lead5.py`). W_TT has components only on the block of the S³
angles, so W_TT(ℓ, ·) = 0 for every vector ℓ in the (τ, r) plane, and χ dv² is the second harmonic's gauge term.

- For an outgoing family the analogue is W'_TT + χ' du².
- So [∂²_(θ_2) g1^(out)](ℓ_in, ℓ_in) = ∂²_(θ_2) χ' (du(ℓ_in))², and [∂²_(θ_1) g1^(in)](ℓ_out, ℓ_out) = ∂²_(θ_1) χ
  (dv(ℓ_out))².
- Since du(ℓ_in) ≠ 0 ≠ dv(ℓ_out) away from the horizon (in ingoing coordinates du degenerates there; verifier 168's
  F2), the cross couplings are present. They enter only through the second-harmonic gauge terms χ and χ', not
  through the transverse-traceless waves.
- A gauge or an ansatz that removes χ and χ' at first order, or moves them to higher order, would remove the cross
  couplings at leading order. Whether one exists in the class is the first analytic question of the two-family case.

**χ dv² is pure gauge, and a generalised wave gauge removes it (deduced, D364; to be computed in step 4).**
Write k := dv, null and geodesic for g0 (k = ∇v, so ∇_k k = ½∇|k|² = 0). Take ∂ for the derivative in X at fixed θ.

- *Pure gauge.* For Z := λ² Φ(X, v/λ) k^♯, ∂_a Φ = Φ_(,a) + λ⁻¹ ∂_θΦ k_a gives
  L_Z g0 = 2λ ∂_θΦ k ⊗ k + λ²(2Φ_(,(a) k_(b)) + 2Φ ∇_a k_b). With ∂_θΦ = χ/2, which exists since χ has θ-mean zero
  (`lead5.py`:149), χ dv² is L_Z g0 at order λ, with an order-λ² completion.
- *Why the record carries it.* In the wave-map gauge relative to g0 (RESPONSE-HL-5D.md:238) the reduced operator's
  principal part is −½ g^(ab) ∂_a ∂_b, whose symbol vanishes at k. So no λ² term can meet a λ⁰ second harmonic; only
  g1's transport −(k·∇ + ½□v) ∂_θ g1 can. The vv second harmonic of R^(0) is therefore met by χ's transport along ℓ
  (RESPONSE-HL-5D.md:439-442; `lead5.py`:19-20).
- *A generalised wave gauge.* Solve instead Ric(g) − δ*_g(Υ(g) − H) = 0 with a fixed gauge source H := λ h(X, v/λ) k.
  Then δ*H = ∂_θh k ⊗ k + O(λ), so the vv second harmonic S k ⊗ k of R^(0) is met algebraically by ∂_θh = −S,
  periodic since S has mean zero. Then χ = 0. Likewise H' := λ h'(X, u/λ) du gives χ' = 0.
- *The cross couplings.* With χ = χ' = 0, g1^(in) = W_TT and g1^(out) = W'_TT are purely angular. So
  [∂² g1^(j)](ℓ_k, ℓ_k) = 0 for all j, k, and contracting the linearization with ℓ_k ⊗ ℓ_k kills both families' large
  terms, as for one family (section 5.2). The cross coupling of section 1 is then a gauge artefact of the record's
  gauge.
- *What it costs, still open.* H is fixed, so it does not enter the linearization. But the constraint Υ − H must be
  propagated, and the solution compared with the record's gauge (by the diffeomorphism exp Z, O(λ²) in C⁰). Step 4
  must also check that no other λ⁻¹ coefficient appears in the two-family linearization; in one family (5.1) there is
  exactly one. [Tou24]'s abstract names "a generalised wave gauge" for the interaction of the waves. Whether it is
  this one is not read: abstract only.

## 2. Several null dusts

- **Published (READ: abstract of [Tou24], arXiv:2402.17530v2).** For a regular solution of Einstein-null dusts "without
  restriction on the number of dusts", families of vacuum solutions are built "based on a multiphase geometric optics
  ansatz", working "in a generalised wave gauge" and controlling "the interaction of waves propagating in different
  null directions, relying crucially on the non-linear structure of the Einstein vacuum equations". That is in 3 + 1
  dimensions, without symmetry. Its theorem also assumes the background close to Minkowski, as the repository's own
  reading records (N1STAR-STATUS.md:81-82; lemmas/BOUNCE-RESEARCH.md:3120-3121). That is the decisive contrast here:
  our setting has five dimensions, the class, and a black-hole background.
- **In the class.** A phase must be a function of the orbit space (τ, r, θ). The two radial null phases of g0 are v
  (ingoing) and u (outgoing, along the outgoing null direction of the background). A θ-dependent null phase solves the
  eikonal equation in the orbit space with angular momentum; its rays focus, and it is not proposed first.
- **The natural first case** is two families, the ingoing shell (phase v) and an outgoing wave packet (phase u) given
  on Σ_τ0 outside the hole. The two crossing at an angle is what "angular separation" requires. dv and du are
  transversal null covectors, so d(v ± u) is timelike or spacelike, and more generally k_1 dv + k_2 du is non-null
  whenever k_1 k_2 ≠ 0. The quadratic interactions at (v ± u)/λ are then non-resonant (deduced, in the wave-map gauge of
  the paper's section 2.5, where the principal part of Ric^H is −½ g^(ab) ∂_a ∂_b). The two-scale operator acts on them
  through the non-zero symbol g0⁻¹(d(v ± u), d(v ± u)), so the approximant solves for them by division, with no
  transport. "Angular separation" is meant in the sense of [HL18] Definition 4.1, as in the paper (RESPONSE-HL-5D.md:96).
- **The limit** is expected to be Einstein with two null dusts, ingoing and outgoing, in the class: a crossing-dust
  generalisation of Vaidya, each dust's energy obeying its own Isaacson law and the dusts coupling only through the
  metric. This is to be shown by step 4 (b). The background stays round, of Vaidya type, only if the outgoing packet's
  averaged stress is round. For the ingoing wave that needed the profile identity h²(c⁴ + s⁴) = 1 (paper section 2.4).

## 3. Vlasov

- **Published (READ: abstract of [HL25], arXiv:2506.21779v1).** "Given suitable small, localized, U(1)-symmetric
  solutions to the Einstein-massless Vlasov system in an elliptic gauge, we prove that they can be approximated by
  high-frequency vacuum spacetimes". "The proof proceeds by first approximating solutions to the Einstein-massless
  Vlasov system by solutions to the Einstein-(multiple) null dust system, then approximating solutions to the
  Einstein-null dust system by vacuum solutions. In the process, we take the number of families of dusts to infinity."
- **Here.** The background is large (a black hole), not small and localized. So the route would need sections 1-2
  with constants uniform in the number of families, on the record's domain. That is beyond the two-family step and is
  not proposed yet.

## 4. The first computable step (proposed)

Stage 0 of a two-phase ansatz in the class:

    G = g0^(2) + λ(W_in(X, θ_1) + W_out(X, θ_2)) + λ² ĝ_2(X, θ_1, θ_2),     θ_1 = v/λ, θ_2 = u/λ,

on an exact two-dust background g0^(2). It is not explicit: u and v are its double-null coordinates, and the record's
explicit Vaidya computations (domain, foliation) would all need redoing on it. The aim is to compute, as `lead5.py`
does for one phase:

- (a) R^(−1) = 0;
- (b) the θ-means of R^(0) give two Isaacson laws, one for each dust;
- (c) the mixed harmonics e^(i(θ_1 ± θ_2)) of R^(0) are solved algebraically by ĝ_2, the symbol being non-zero wherever
  dv and du are independent;
- (d) the second harmonics of each family are handled as in one-phase Stage 0 (the χ dv² term and its outgoing twin).

The analytic step after that is the energy estimate with two large couplings and their cross terms (section 1), as in
[Tou24].

## 4b. Stage 0 with two phases, computed (D376, D380)

`checks/stage0two5.py` (computed, exact, sympy; selftest T1-T6 pass in about 5 s, and its six mutants are caught; read
by verifier 174, D380) runs Stage 0 on a general round double-null background,

    g0 = −2 e^(2σ(u,v)) du dv + R(u,v)² (dθ² + cos²θ dφ1² + sin²θ dφ2²),

with σ and R arbitrary, so no field equation for g0 is assumed. The ansatz is g = g0 + λ(W_in + W_out), each family in
`lead5.py`'s form: the transverse-traceless wave of the S³ angles with amplitude α(v) R^(−3/2) H(θ) and phase
s1 = v/λ (resp. β(u) R^(−3/2) H(θ) and s2 = u/λ), plus a free second-harmonic term χ dv² (resp. χ′ du²). The fast
variables are carried as exp(i s_k), so each harmonic (n1, n2) is read off as a coefficient. The reduced Ricci tensor is
`lead5.py`'s, in the wave-map gauge relative to g0; verifier 174 checked the order-by-order assembly against
`lead5.py`'s truncation in all 15 components.

- (a) **T1:** R^(−1) = 0 in every component. This holds for any W_in(s1) + W_out(s2), since g0^(uu) = g0^(vv) = 0; it
  is recorded, not tested against a mutant.
- (b) **T2:** the (0, 0) harmonic of R^(0) is Ric(g0) − K_in dv² − K_out du², with no other component and no term
  coupling the two families. That the families do not meet in the mean is harmonic bookkeeping: their product terms
  carry e^(±i s1 ± i s2) only. K_in = (cos⁴θ + sin⁴θ) H² α²/(3R³) and K_out the same with β; with the record's H,
  K_in R³ = α²/3 and K_out R³ = β²/3. So the averaged equation is Einstein with two round null dusts, ingoing and
  outgoing, coupled only through g0. Each dust's energy is transported along its own direction (K_in R³ constant along
  ∂_u, which spans ℓ_in = g0^(−1) dv; K_out R³ along ∂_v). That Isaacson law is the input chosen so that T3 holds,
  as for one phase, not an output of T2.
- (c) **T4:** the mixed harmonics (n1, n2), n1 n2 ≠ 0, of R^(0) are present: the cross terms do not vanish. A term
  λ² q E in g, for each of the 15 symmetric basis tensors E and any q(u, v, θ, s1, s2), adds exactly
  −g0^(uv) ∂_(s1) ∂_(s2) q E = e^(−2σ) ∂_(s1) ∂_(s2) q E to R^(0). Its symbol at (n1, n2) is −e^(−2σ) n1 n2 ≠ 0, so
  ĝ_2 solves every mixed harmonic by division, with no transport. The mutant without the gauge term is caught.
- (d) **T3, T5:** with these amplitudes, the harmonics (n, 0), n ≠ 0, vanish except in vv at n = ±2, and (0, n) except in
  uu at n = ±2; the mutants without either transport are caught. Writing χ = χ_2 e^(2i s1) + χ_(−2) e^(−2i s1), χ
  enters the vv (±2, 0) harmonics only as ±2i e^(−2σ) R^(−3/2) ∂_u(R^(3/2) χ_(±2)), its transport along ℓ_in, and χ′
  likewise along ∂_v (T5; the mutant with χ on dv du is caught). So each family's second harmonic is met as for one
  phase (`lead5.py`'s L4), or removed by section 1's generalised wave gauge.

So Stage 0 of the two-phase ansatz closes on any round double-null background whose Ricci tensor is the two dusts'
stress. What it does not give:

- the background itself, a solution of Einstein-two-null-dusts in the class (a characteristic problem; reduced and
  computed in section 4c, D389);
- the gauge condition beyond what is checked: at order λ⁰ the gauge 1-form D = g^(ab)(Γ − Γ0)_(ab) vanishes (T6,
  D381; each W is transverse to its own generator and traceless, `lead5.py`'s L5). At order λ, on the mixed
  harmonics, the waves' part plus ĝ_2's fast divergence vanishes once ĝ_2 is fixed by T4 (T7 with `--gauge`, D383: a
  numerical identity test of the exact assembly on concrete functions at random points, residual 5 × 10⁻¹⁸ against
  2.8 × 10⁻² over 16 harmonics; ĝ_2 of the wrong sign fails). The pure harmonics at order λ, which need ĝ_2's own
  transport, are not checked;
- the profile H: it is imposed, the record's, not derived for the outgoing family;
- the next stages (ĝ_2's own transport at order λ, and the mixed terms it feeds back);
- the energy estimate with the two large couplings of section 1.

Section 1's claim that the cross couplings are a gauge artefact concerns the linearised operator, not Stage 0, and is
not tested here.

## 4c. The two-dust background (D389)

`checks/twodust5.py` B1-B5 (B1-B4 exact, sympy; B5 floating point; selftest about 7 s). With
g0 = −2e^(2s) du dv + R² dΩ₃² and the stress of section 4b, K_in R³ = A(v) and K_out R³ = B(u):

- *B1, the equations.* The off-diagonal and angular-mixed components of Ric(g0) vanish. Ric_uv = 0 and the angular
  equation are equivalent to the evolution

      R_uv = −(e^(2s) + 2R_u R_v)/R,      s_uv = 3(e^(2s) + 2R_u R_v)/(2R²).

  The two remaining components are the Raychaudhuri constraints C_u := R_uu − 2s_u R_u + B/(3R²) = 0 and
  C_v := R_vv − 2s_v R_v + A/(3R²) = 0. The dust enters only through them.
- *B2, propagation.* Modulo the evolution, ∂_v(R² C_u) = 0 and ∂_u(R² C_v) = 0 identically. This holds because B
  depends on u alone and A on v alone: with B = B(u, v) a residual in ∂_v B remains (the control). So section 4b's
  Isaacson laws are exactly what propagates the constraints. Data with C_v = 0 on u = u_0 and C_u = 0 on v = v_0,
  evolved by B1's two equations, give a solution of Einstein with the two dusts.
- *B3, the mass.* μ := R²(1 + 2e^(−2s) R_u R_v), so that g0^(ab) ∂_aR ∂_bR = 1 − μ/R², obeys μ_v = −(2/3) A e^(−2s) R_u
  and μ_u = −(2/3) B e^(−2s) R_v. Where R_u < 0 < R_v, the ingoing dust adds mass and the outgoing dust carries it away.
- *B4.* Minkowski, e^(2s) = ½ and R = (v − u)/2, solves the evolution with A = B = 0.
- *B5, a computed background.* Flat corner data at (u, v) = (−10, 0); an ingoing pulse A = 2 sin⁴ on v ∈ [1, 3] and an
  outgoing pulse B = sin⁴ on u ∈ [−9, −7]; each cone's data from its constraint with s = −½ ln 2 there; the interior
  by a second-order diamond scheme on u ∈ [−10, −3], v ∈ [0, 6].
  - The interior residuals of C_u and C_v fall at second order: ratio 4.00 between 40 and 80 steps per unit, where
    they are 2.7 × 10⁻⁶ and 1.4 × 10⁻⁵. The control, C_u with B shifted by ½ in u, stays at 2.0 × 10⁻².
  - μ rises to 1.001 across the ingoing pulse, and is 0.5202 at the far corner after the outgoing one. Integrating
    B3's fluxes along the two far edges gives 0.5203.
  - The region is untrapped throughout (R_u < 0 < R_v), and min R = 1.42.

So the background exists on this rectangle as a computed solution. Local existence near the corner for any smooth
data is the standard Picard iteration for this 1+1 semilinear Goursat system; it is not read at source here.

What it does not give: the background on the record's domain, which would need the outgoing family's data at past
null infinity; a horizon (these pulses leave the region untrapped); and the next stages listed in section 4b.

## 5. Sources

READ (abstracts, fetched from arxiv.org on 2026-10-31 and quoted from those pages): [Tou24] A. Touati, "The reverse
Burnett conjecture for null dusts", arXiv:2402.17530v2; [HL25] C. Huneau, J. Luk, "High-frequency backreaction for
the Einstein equations under U(1) symmetry: from Einstein-dust to
Einstein-Vlasov", arXiv:2506.21779v1. The record: RESPONSE-HL-5D.md sections 2.4, 4, 5.1-5.2 and 9.
