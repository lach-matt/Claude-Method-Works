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

**Where the cross coupling sits in the class (deduced from the record's Stage 0; computed in section 4d, D414).** The
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
  propagated [computed from a spacelike slice, D428, section 4e], and the solution compared with the record's gauge
  (by the diffeomorphism exp Z, O(λ²) in C⁰). Step 4 must also check that no other λ⁻¹ coefficient appears in the
  two-family linearization; in one family (5.1) there is exactly one. [Checked, D414: in the two-family linearisation
  there is exactly one per family (section 4d, L1).]
  [Tou24]'s abstract names "a generalised wave gauge" for the interaction of the waves. Whether it is this one is not
  read: abstract only.

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

`checks/stage0two5.py` (computed, exact, sympy; selftest T1-T6 pass in about 8 s, and its six mutants are caught; read
by verifier 174, D380; `--gauge` adds T7 (D383) and T8 (D396), about a minute) runs Stage 0 on a general round
double-null background,

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
  2.8 × 10⁻² over 16 harmonics; ĝ_2 of the wrong sign fails). On the mean and the pure harmonics at order λ (T8,
  D396, the same numerical identity test):
  - *The mean.* The waves' (0, 0) part vanishes in every component, and no fast derivative of ĝ_2 reaches it.
  - *The pure harmonics.* At (n, 0) the fast divergence of ĝ_2 is kf_v(g0^(vu) g0^(rd) G_du − ½ g0^(rv) tr G). Its
    component r = v is set by G_uu, r = θ, φ1, φ2 by G_uθ, …, and r = u by the angular trace of G alone, as the G_uv
    terms cancel. So the waves' part at each of the 8 pure harmonics present is cancelled by ĝ_2's pure harmonics in
    those components (residual 2 × 10⁻¹⁶); at (0, n) likewise with u and v exchanged. These components do not enter
    R^(0), whose symbol −e^(−2σ) n1 n2 vanishes there (T4), so Stage 0 is unchanged. Controls (D402, verifier 179,
    who found the first control unable to fail, as angular off-diagonal G has no fast divergence): a unit G in each
    component reaches exactly the stated row; and without the angular diagonal the r = u equation loses its unknown
    and is unsolvable exactly where the waves' part has an r = u component (12 of the 24 harmonic-points tested). The
    waves' part has no r = v component at any harmonic (n, 0), so G_uu = 0 there (at (0, n): no r = u component, and
    G_vv = 0).
  - *The next stage at the pure harmonics (deduced, D401).* Let the background solve the two-dust equations
    (section 4c), α, β, χ and χ′ their transports (T3, T5), and ĝ_2 be fixed on the mixed harmonics by T4 and, at
    (n, 0), in G_uu, G_uA and g0^(AB) G_AB by T8; the other ten components of ĝ_2 there are free. Then R^(−1) = R^(0)
    = 0 and D^(0) = D^(1) = 0 on every harmonic (T1-T8).
    - Ric^H is Ric − ½(g_pr ∇̂_q D^r + g_qr ∇̂_p D^r), ∇̂ the connection of g0 (`ricci_orders`): Ric minus a term
      linear in D and its first derivatives. So the contracted Bianchi identity makes div_g(Ric^H − ½ g tr_g Ric^H)
      a linear second-order expression in D, L(D).
    - At order λ⁰ the left side is the fast divergence g0^(vu) F1 (R^(1) − ½ g0 tr_(g0) R^(1))_(u c). The slow
      divergence, and every term with W, act on the orders λ⁻¹ and λ⁰ of Ric^H, which vanish.
    - At order λ⁰ the right side is g0^(ab) F_a F_b D^(2) plus terms in D^(1), and g0^(ab) F_a F_b = −2 g0^(uv) n1 n2
      vanishes at (n, 0).
    - So at (n, 0), identically and whatever the free components of ĝ_2: c = u gives R^(1)_uu = 0, c = A gives
      R^(1)_uA = 0 (as g0_uu = g0_uA = 0), and c = v gives g0^(AB) R^(1)_AB = 0 (the R^(1)_uv terms cancel).
    - These five are the components in which T8 fixed ĝ_2 (through r = v, A and u). Their equations at this stage hold
      automatically, so the fixed components need no transport of their own. The other ten components of R^(1) at
      (n, 0) (vv, uv, vA and the angular trace-free part) are transports along ∂_u for the ten free components, with
      principal part −g0^(uv) i n ∂_u from −½ g^(ab) ∂_a ∂_b. At (0, n) the same holds with u and v exchanged.
    - *Computed, the linear core (D407; `checks/stage1pure5.py` P1-P2, exact, n = 1, 2).* At (n, 0), the part of
      R^(1) linear in ĝ_2 and independent of the waves, the λ coefficient of Ric^H(g0 + λ²ĝ_2), contains no Ric(g0)
      (wording corrected D413, verifier 181), so it can be computed on a general round double-null background.
      With ĝ_2's five reachable components zero and the other ten
      arbitrary functions, R^(1)_uu, R^(1)_uA and g0^(AB) R^(1)_AB vanish identically: the free components do not
      enter the five equations. Each of the other ten components of R^(1) contains the transport of its own free
      component, with coefficient −i n g0^(uv) times that component's weight. Control: with G_uu or the angular
      trace nonzero, the corresponding one of the five does not vanish.
    - Not computed: the whole of R^(1) at (n, 0), the waves' terms and their products with ĝ_2 included. Those
      products are also linear in ĝ_2 and sit at order λ (Γ at λ⁰ carries ½g0⁻¹FW, Γ at λ carries ½g0⁻¹Fĝ_2), and not
      only through the mixed harmonics: W_in at z1^(±1) times ĝ_2's pure harmonic (n ∓ 1, 0) lands on (n, 0) (D413,
      verifier 181). That needs an on-shell background, for instance a jet of section 4c's solution at a point.
- the profile H: it is imposed, the record's, not derived for the outgoing family;
- the next stages: ĝ_2's own transport at order λ (at the pure harmonics, its ten free components', D401) and the
  mixed terms it feeds back;
- the energy estimate with the two large couplings of section 1.

Section 1's claim that the cross couplings are a gauge artefact concerns the linearised operator, not Stage 0, and is
not tested here. It is tested at the level of the λ⁻¹ coefficients in section 4d (D414).

## 4d. The large coefficients of the two-phase linearisation (D414)

`checks/twolin5.py` (computed, exact, sympy; selftest A, L1-L3 and a control pass in about 14 s) linearises Ric^H at
g = g0 + λ(W_in + W_out) in a slow perturbation w. It works on section 4b's general round double-null background with
its waves and reads off the λ⁻¹ coefficient E[w]. The λ⁻¹ part of Ric^H involves fast derivatives only, so E[w] is
algebraic in w, with no derivative of w. Write ℓ_in := g0⁻¹ dv and ℓ_out := g0⁻¹ du, s_in := w(ℓ_in, ℓ_in) =
e^(−4σ) w_uu and s_out := w(ℓ_out, ℓ_out) = e^(−4σ) w_vv.

- *A, the assembly.* It reproduces stage0two5's λ⁻¹ coefficient: zero for the waves (T1), and nonzero, in agreement,
  once terms depending on both phases are added. A mutant of one family alone cannot test it, since the coefficient is
  −½ g0⁻¹(k_j, k_k) ∂_(s_j) ∂_(s_k) W (k_in = dv, k_out = du), which vanishes for any W_in(s1) + W_out(s2).
- *L1, one coefficient per family.* E[w] = ½(s_in ∂²_(s1) W_in + s_out ∂²_(s2) W_out) in all 15 components, for every
  w. This is the record's coefficient ½ λ⁻¹ s(w) [∂²_θ g1] of (5.1) (RESPONSE-HL-5D.md:473), once for each family,
  and nothing else, so section 1's "no other λ⁻¹ coefficient" holds for two families. L1 holds for any
  W_in(s1) + W_out(s2), transverse or not (verifier 182, D420), so it does not test the ansatz; L2-L3 carry that. It is
  the linearised coefficient −½ g^(ab) of the principal part in −½ g^(ab) ∂_a ∂_b (λW). The λ² term ĝ_2, whose
  harmonics mix the two phases, enters only at λ⁰.
- *L2, which contraction kills which.*
  - E(ℓ_in, ℓ_in) = −2 e^(−4σ) s_out χ′ and E(ℓ_out, ℓ_out) = −2 e^(−4σ) s_in χ; E(ℓ_in, ℓ_out) = 0.
  - So each family's own coupling is killed by its own ℓ_k ⊗ ℓ_k, as in the record's section 5.2
    ([∂_θ g1](ℓ, ·) = 0, RESPONSE-HL-5D.md:504).
  - The other family's coupling survives, through its second-harmonic gauge term alone (χ′ du², with
    du(ℓ_in) = −e^(−2σ) ≠ 0). That is section 1's deduction, now computed. The transverse-traceless waves never enter
    a contraction with the (u, v) plane.
- *L3, the generalised wave gauge.* With χ = χ′ = 0, E[w] has no component with an index u or v. Every contraction
  with vectors of the (u, v) plane vanishes, so ℓ_in ⊗ ℓ_in and ℓ_out ⊗ ℓ_out kill both families' couplings, as for
  one family.
- *Control.* Without the gauge term the coefficient gains ½ Σ_k (−k_b (P_k w k)_c − k_c (P_k w k)_b + k_b k_c ⟨w,
  P_k⟩), P_k := ∂²_(s_k) W_k, indices raised by g0; it is nonzero in the uu, uA, vv and vA components. The
  one-coefficient structure belongs to the wave gauge.

What it does not give:

- the order-λ⁰ coefficients (B·∂w + C·w in (5.1)), which carry first fast derivatives of W and are bounded;
- section 1's gauge source in the linearisation. H = O(λ) is fixed, so only Γ(g)·H depends on g, at order λ (deduced);
  the Stage 0 of that gauge is not computed;
- the energy estimate. In the record's gauge, the s_in equation (the ℓ_in ⊗ ℓ_in contraction) carries the large
  coupling −2 λ⁻¹ e^(−4σ) χ′ s_out, oscillating in s2 with mean zero, and the s_out equation the mirror one. Whether a
  phase decomposition along ℓ_out absorbs it, as section 5.2's does along ℓ, is the analytic question that remains.
  The generalised wave gauge removes it.

## 4e. Stage 0 in the generalised wave gauge (D419)

`checks/stage0h5.py` (H1 deduced; H2 and a control computed, exact, sympy; about 10 s) takes section 1's operator
Ric(g) − δ*_g(Υ(g) − H), with the fixed source H := λ(h(X, s1) dv + h′(X, s2) du), and section 4b's ansatz with
χ = χ′ = 0.

- *H1.* δ*_g H has no λ⁻¹ part, and its λ⁰ part is ∂_(s1)h dv² + ∂_(s2)h′ du². The fast derivative brings λH to λ⁰,
  and Γ·H is O(λ). So the source enters Stage 0 only in vv and uu.
- *H2.* With χ = χ′ = 0, stage0two5's R^(0) − Ric(g0) has, among the pure harmonics, only the vv (±2, 0) and uu (0, ±2)
  entries S_(±2), S′_(±2). These are the second harmonics that χ's and χ′'s transports met in T5. With
  h = Σ_± h_(±2) z1^(±2), h_(±2) := −S_(±2)/(±2i), and h′ likewise, every pure harmonic of R^(0) + (δ*H)^(0) − Ric(g0)
  vanishes.
  - The second harmonics are met algebraically, with no transport, and h is periodic because S has no mean part.
  - h_2 = (4i cos 2θ − sin² 2θ) H(θ)² α(v)²/(48 R³).
  - The mean (T2) and the mixed harmonics (T4) are untouched.
- *Control.* With h = 0 the vv (2, 0) entry is nonzero, and with h_2 of the wrong sign it doubles.

So section 1's gauge exists at Stage 0, χ = χ′ = 0 is consistent there, and by section 4d's L3 both families' large
couplings are then killed by their own contractions.

- *H3, the gauge condition at order λ (computed, D423).* Υ − H = 0 at order λ on the pure harmonics reads
  D^(1) + (ĝ_2's fast divergence) − g0⁻¹H^(1) = 0.
  - H's raised form g0^(uv) h ∂_u enters only the r = u row at (n, 0), and h′ only r = v at (0, n). T8 sets those
    rows by ĝ_2's angular trace.
  - Solved by T8's components on all 8 pure harmonics present, the source's (±2, 0) and (0, ±2) included: the residual
    is 6.6 × 10⁻¹⁷. The method is stage0two5's gauge_pure, on concrete functions at three random points. The content
    is that the linear system is solvable at every harmonic and point; the residual only confirms the solve (D427).
  - Control: without the angular diagonal the system fails at 12 harmonic-points, exactly where that row carries a
    term.
- *The propagation of Υ − H = 0 (computed, D428).* `checks/propagate5.py` (exact, random polynomial jets of degree 3
  at a point, three metrics; about 15 s) checks, for any metric g and any 1-form W:
  - P1, the contracted Bianchi identity B_g Ric(g) = 0, with B_g := δ_g + ½ d tr_g and (δ_g h)_b := −∇^a h_ab;
  - P2, B_g δ*_g W = −½(□_g W + Ric(g)(W)). So a solution of Ric(g) − δ*_g W = 0, W := Υ(g) − H, has
    □_g W + Ric(g)(W) = 0, whatever H is;
  - P3, where W = 0 on {t = 0}: G(g)(n, ·) = (δ*W − ½ tr(δ*W) g)(n, ·) = ½ n⁰ ∂_t W there, with n^a := g^(a0) and
    n⁰ = g^(00) < 0, so the constraints give ∂_t W = 0;
  - P4, W = 0 on {t = 0} can be imposed: at a point Υ is affine in ∂_t g_(0μ) with coefficient g^(00) diag(½, 1, 1, 1).
    The constraints do not involve those four derivatives (standard: G(n, ·) depends only on the induced metric and the
    second fundamental form; not computed).
  - Controls: d tr for ½ d tr in P1, no curvature term in P2, a W vanishing on {x1 = 0} in P3, and ∂_t g_(1μ) for
    ∂_t g_(0μ) at Minkowski (rank 2) all fail.
  - So, for data satisfying the vacuum constraints and a solution regular enough for the energy estimate, W ≡ 0 on the
    domain of dependence (for g) of a spacelike slice, by uniqueness for the linear wave equation with zero data
    (standard, not computed; D433). H enters only through W: its being fixed matters for the reduced system's
    principal part, not here. Not computed: that the record's solution solves the reduced equation exactly. The
    characteristic case is the next bullet (D440).
  - *The characteristic case (D440; `checks/charprop5.py` N0-N4, exact in the transverse jets, vacuum as above,
    n = 4 and 5, three seeds each; about 5 s).* N = {u = 0} is null with generators ∂_v, so g_vv = g_vA = 0 on N. At
    a point of N, in the ring of polynomials in the transverse jets ∂_u g_ab and ∂_u ∂_c g_ab:
    - W depends on them only through ∂_u g_vv, ∂_u g_vA and γ^(AB) ∂_u g_AB, triangularly, with diagonal g^(uv),
      g^(uv) and −½ (N1). So W = 0 at a point of N fixes those n transverse derivatives there.
    - With E := Ric(g) − δ*W the reduced operator, E_vv = C_vv − ∂_v W_v + (κ − θ/2) W_v (N2; N0 checks Ric_vv against
      Raychaudhuri's form, κ = Γ^v_vv, θ the expansion of ∂_v). Modulo W_v and its derivatives along N, E_vA = C_vA − ∂_v
      W_A + (χ_A^B − ½θ δ_A^B) W_B (N3). Modulo W_v, W_A and theirs, γ^(AB) E_AB = C_tr + 2 g^(uv) ∂_v W_u − g^(uv) H_v
      W_u (N4). C_vv, C_vA and C_tr are free of the transverse jets: they involve only g on N, its derivatives along N,
      and H with its derivatives, and are the null constraints in the gauge W = 0.
    - So for data on N with C_vv = C_vA = C_tr = 0 and W = 0 on the section S where N meets N′ = {v = 0}, a solution of
      the reduced equation has W_v, then W_A, then W_u zero on N: three ODEs along the generators with zero data at S,
      linear with the solution's κ as a coefficient (κ contains ∂_u g_vv, so in the data alone the first is a Riccati
      equation, which W_v = 0 still solves uniquely; D441). The same holds on N′ with u and v exchanged. P2's linear wave
      equation then has zero data on N ∪ N′, and W ≡ 0 where its characteristic problem has uniqueness (near S as [CP12]
      states it, D476; beyond, standard, not computed).
    - Controls: a hypersurface with g_vv ≠ 0 (and g_vA's jets along N nonzero), θ for θ/2 in N2, N3 without the reduction
      modulo W_v, and one angular component in place of the trace in N4 all fail; the last because the trace-free angular
      equations carry the trace-free ∂_v ∂_u g_AB, which is not a constraint.
    - *The constraints as ODEs (D448-D449; `checks/charcons5.py` K1-K4, exact in the transverse jets and in the second
      v-derivatives of g_AB and the first and second of g_uu, g_uv, g_uA along N, n = 4 and 5).* Modulo every W-jet, C_vv
      contains of the second v-derivatives only the trace γ^(AB) ∂_v² g_AB, with coefficient −½ (Raychaudhuri, for the
      conformal factor); C_vA contains ∂_v² g_uB with coefficients g^(uv) δ_A^B and no ∂_v² g_uu; C_tr contains ∂_v² g_uu
      with coefficient −2 (g^(uv))². The hierarchy closes (K4, verifier 192): C_vv does not depend on g_uu or g_uA at
      all, C_vA not on g_uu nor on angular derivatives of g_uB, and C_tr not on angular derivatives of g_uu. So given the
      conformal class of γ and g_uv along N (free data and a gauge choice) and H, the gauge-reduced constraints are ODEs
      along each generator for the conformal factor, then g_uA, then g_uu; the first is nonlinear (it holds while θ stays
      finite), the other two linear in their unknown's second derivative. Each later step uses angular derivatives of the
      earlier unknowns, so each is solved on a neighbourhood of generators, smooth in x^A, with an existence interval
      uniform over the compact S. At S, g_uu = g_uA = 0 (N′ is null) and the conformal factor's value is free; their
      first v-derivatives and θ are tied to N′'s numbers by the corner conditions (next bullet; D449 had them fixed by
      those conditions, corrected D455).
    - *The corner conditions (D455; `checks/charcorner5.py` C1-C3, exact in the first u- and v-jets at a point of S, n =
      4 and 5).* At S all four of g_uu, g_uA, g_vv, g_vA vanish, so N1 and its mirror under u ↔ v hold together: W
      depends on the u-jets only through ∂_u g_vv, ∂_u g_vA and τ′ = γ^(AB) ∂_u g_AB, on the v-jets only through ∂_v
      g_uu, ∂_v g_uA and τ = γ^(AB) ∂_v g_AB = 2θ, and on nothing else of either (∂_u g_uv, ∂_v g_uv and both shears
      included). The Jacobian is diagonal in pairs: W_u = g^(uv) ∂_v g_uu − τ′/2 + f_u, W_v = g^(uv) ∂_u g_vv − τ/2 +
      f_v, W_A = g^(uv) (∂_u g_vA + ∂_v g_uA) + f_A, with f computed from g at S, its angular derivatives and H, and f_u
      = −H_u, f_v = −H_v exactly (verifier 196, D459). So W = 0 on S is n relations, each between one number of N and one
      of N′: N's expansion with N′'s ∂_u g_vv, N′'s expansion with N's ∂_v g_uu, and ∂_v g_uA with ∂_u g_vA. Both
      expansions and one of each mixed pair are free, and the other n numbers are fixed: given N′'s numbers the
      conditions fix N's, and conversely, but not both at once (D459); θ and ∂_u g_vv cannot both be prescribed
      (control).
    - *The null dusts (D463; `checks/chardust5.py` D1-D5, exact, n = 4 and 5).* With E := Ric − δ*W − κT for two null
      dusts, T = Σ_i ρ_i k_i ⊗ k_i, trace-free as k_i is null, T is algebraic in g and the dusts' data and has no
      transverse jet, so N2-N4 hold with C_vv, C_vA, C_tr shifted by −κT_vv, −κT_vA, −κγ^(AB)T_AB, and the propagation of
      W uses div T = 0 and tr T = 0 off N, which the dusts' own equations (geodesic flow and continuity) keep. The
      hierarchy still closes: T_vv = Σ ρ_i (g_uv k_i^u)² is free of g_uu, g_uA and γ (a source for Raychaudhuri's
      equation fixed by the data); T_vA is free of g_uu and linear in g_uA; γ^(AB)T_AB is free of g_uu. A dust along N's
      generators has k_v = 0 on N and drops out; only the crossing dust enters. With the record's dusts, the covectors √K
      dv and √K du (section 4c), T_vA = T_AB = 0 on N, and T_vv = K_in comes from the √K dv dust (T = K_in dv² + K_out
      du², section 4b; the du-dust runs along N's generators and drops out) (verifier 198, D464; corrected D468, verifier
      199). The corner conditions are matter-free.
    - *The dusts' own data (D470; `checks/chardustdata5.py` T1-T5, exact, D = 4 and 5).* At a point of N, every field
        a first-order jet: a null dust tangent to N lies along the generators (k^A = 0 by nullity), (div T)^u and (div
        T)^A vanish identically, and the remaining component is a transport along the generators, ∂_v q + c q = 0 for q =
        ρ(k^v)² (T_uu = g_uv² q), with c = (2∂_v g_uv − ∂_u g_vv)/g_uv + ½γ^(AB)∂_v g_AB. Its one transverse jet, ∂_u
        g_vv, is fixed on N by W_v = H_v, which depends on the transverse jets through ∂_u g_vv alone, with coefficient
        1/g_uv; indeed c = 2∂_v ln|g_uv| − W_v, so the expansion cancels and the transport is ∂_v T_uu = H_v T_uu
        (verifier 201, D471). So that dust is fixed on N by its value on S. For a dust crossing N, div T = 0 and the
        u-derivative of nullity determine its transverse derivatives up to the rescaling k → fk, ρ → ρ/f², which leaves T
        unchanged (one dependency, k_a(div T)^a = (ρ/2)k^u ∂_u g(k, k), and rank D), so its ρ, k^u and k^A on N are free,
        D − 1 functions up to the rescaling (the rank is D wherever ρ, k^u ≠ 0: a D × D block has determinant
        2ρ^D(k^u)^D, verifier 201). With the record's dusts, on N = {u = const} K_out (the du dust) is transported from
        S, reproducing section 4c's K_out R³ = B(u), and K_in, the dv dust's one function, is free where dv is null on N
        (g^vv = 0; in general that needs g_uu = γ^(AB)g_uA g_uB); on N′ the roles swap by symmetry (not computed).
        Whether the record's Υ is taken relative to g0 is not stated: with the coordinate Υ, Υ_v(g0) = −3R_v/R is of
        order 1, while 4e's H is of order λ (verifier 201); T3 holds either way.
    - *Existence and uniqueness near S (D476, read: [CP12] P. T. Chruściel and T.-T. Paetz, "The many ways of the
      characteristic Cauchy problem", arXiv:1203.4534v2).* Theorem 2.1 (Rendall), p. 5: for vacuum data on two
      characteristic hypersurfaces meeting transversely in S, "there exists an open neighbourhood U of S in the region
      {x¹ ≥ 0, x² ≥ 0}, a unique function Ω on (N1 ∪ N2) ∩ U and a unique smooth Lorentz metric g_μν on U" solving the
      vacuum equations; and "The above extends easily to non-vacuum models with energy-momentum tensors of the form"
      T_22, T_2A, T_12 given by matter data and the listed metric jets on {x¹ = 0} (p. 5). Section 3 (p. 5) treats
      "energy-momentum tensors of the form T_μν ℓ^ν = T_μ(g, φ, ∂_∥ g, ∂_∥ φ, x) (15), for some fields φ satisfying
      equations which, when the metric is considered as given, possess a well-posed characteristic Cauchy problem", with
      every metric component prescribed on N1 ∪ N2 in a generalised wave-map gauge, and concludes (p. 9), "assuming that
      the reduced Einstein equations (see (43) below) can be complemented by well-posed evolution equations for the
      matter fields", a solution of the reduced equations "in a future neighbourhood of S", which solves the full
      equations "if and only if [11] H^μ vanishes on N1 ∪ N2" (their H^λ = g^(αβ)Γ^λ_αβ − W^λ is this section's W, their
      W its source H). On uniqueness, Section 4.3 (p. 16), of vacuum data: "Here uniqueness is understood locally, though
      again it is clear that unique maximal globally hyperbolic developments should exist in the current context."
      Applied here: the dusts' T_μν ℓ^ν on N is algebraic in g and the dusts' fields (D463), so of the form (15) with no
      derivative; given g, each dust is a first-order transport along its own null direction with free data on the
      hypersurface it crosses and its value on the other fixed by transport from S (D470), which is the well-posedness
      (15) asks for, by characteristics (not written out); and W vanishes on N ∪ N′ by D440-D441 and the corner
      conditions (D455). So, given that well-posedness, the record's characteristic problem with its two dusts has a
      solution of the reduced equations near S, which solves the full equations since W = 0 on N ∪ N′; uniqueness is
      stated there for vacuum and locally, and for the dusts rests on the same reduction (not read further); P2's
      propagation of W = 0 near S is the step [CP12] takes from [11] (not read).
    - Not computed: existence and uniqueness beyond a neighbourhood of S (the reading gives them near S only, and
      uniqueness locally), the dusts' well-posedness given g written out, and that the record's solution solves the
      reduced equation exactly. The corner S needs no condition for the dusts: each dust's value on S is the restriction
      of its free data on the hypersurface it crosses, which then seeds its transport along the other (D470).

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
