# FAMILIES5 -- more matter families: several null dusts, angular separation, Vlasov

Status: scoping note (D361). Read by verifier 167 (D362), findings seated. Section 1's two deductions on the cross
coupling added (D363-D364). Section 4's first step computed (D376, section 4b: `checks/stage0two5.py`; read by verifier
174, D380). Section 4f: the record's section 5.2 with two families (D512, `checks/twophase5.py`), deduced; section 4g
its section 3 (D522), section 4h its Theorem A (D526), section 4i its Lemma 1.1 (D533, D546). Nothing proved beyond Stage 0.

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
  phase decomposition along ℓ_out absorbs it, as section 5.2's does along ℓ, was the analytic question that
  remained. It does, at the λ⁻¹ level; the generalised wave gauge, which removes it from E[w], brings a λ⁻¹ coupling
  back through the decomposition (section 4f, D512).

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
      conditions (D455). So, given that well-posedness and that of the coupled reduced Einstein-dust system, which [CP12]
      p. 9 assumes separately and which is not shown here (verifier 204, D480), the record's characteristic problem with
      its two dusts has a solution of the reduced equations near S, which solves the full equations since W = 0 on N ∪
      N′; uniqueness is stated there for vacuum and locally, and for the dusts rests on the same reduction (not read
      further); P2's propagation of W = 0 near S is the step [CP12] takes from [11] (not read). On the gauge (D484,
      corrected D485; read and deduced): [CP12]'s target ĝ "is only introduced so that the harmonicity vector H^μ,
      defined in equation (18), is a vector field, and plays no significant role in what follows" (p. 6), and W̊ is fixed
      on N1 ∪ N2 by the data and otherwise "any smooth vector field on M which coincides with W̊ on N1 ∪ N2" (p. 9). The
      record's gauge (III.B Definition 6.1, (6.3)) has target g0 and the source E^Υ_(g0) G_(g0)(g − g0), which is
      algebraic in g: on N1 ∪ N2 it is fixed by the data, as [CP12]'s W̊ is. It depends on g, so it is not a fixed vector
      field and [CP12]'s "any smooth vector field" does not literally cover it; what carries the step is the reduced
      operator. P = Ric(g) − δ*_(g0, E_C) Υ^E ((6.4)) differs from [CP12]'s R_μν − ∇_(μ H_ν) by first-order terms only:
      δ* of the source, which brings first derivatives of g (D484 said 'terms without derivatives of g', which is false;
      D485), δ* taken with g0 rather than g, which adds (Γ(g) − Γ(g0)) · Υ, and the damping E^C ((6.2)). The principal
      part is unchanged, so the reduced system stays a quasilinear wave system of the kind Rendall's theorem treats, and
      Υ obeys a homogeneous linear wave equation (the second Bianchi identity, □^C of (6.4)), so Υ = 0 on N1 ∪ N2 still
      propagates (deduced; Rendall's paper [36] not read). The quotations were checked word for word against the alphaXiv
      text of arXiv:1203.4534v2 when they were seated (D480, D484), by the author, not independently: the verifiers'
      routes to arXiv were refused (D480, D485).
    - Beyond a neighbourhood of S (D488, corrected D490; read: [CCTW16] Cabet-Chruściel-Tagne Wafo, arXiv:1406.3009v2;
      [CTWG23] Chruściel-Tagne Wafo-Gray, arXiv:2305.07306v1). [CCTW16] proves "the neighborhood theorem" for quasilinear
      symmetric hyperbolic systems split as A^u = diag(A^u_ϕϕ, 0), A^v = diag(0, A^v_ψψ) in double-null coordinates, in
      any dimension, with Y = S compact (Theorem 3.9, p. 32; Corollary 3.11, p. 35: "a unique solution ... defined on the
      neighborhood ([0, a_*] × [0, b_0] × Y) ∪ ([0, a_0] × [0, b_*] × Y) of N"), provided the transport equations along
      the generators have a solution on the hypersurfaces; the neighbourhood's "thickness ... might shrink to zero when
      receding to infinity" (Remark 3.12, p. 35). It applies this to Einstein in four dimensions only: the harmonic
      reduction "lead[s] to a loss of derivative of the coefficients" (p. 50), so it works with the Bianchi equations in
      a double-null frame (Theorem 5.3, p. 54, vacuum), and "generalises immediately to Einstein equations with matter
      fields satisfying wave equations", □_g Φ = F(Φ, ∂Φ, g, ∂g) (section 5.2, pp. 56-57). [CTWG23] does every higher
      dimension: "The maximal globally hyperbolic development of smooth initial data for vacuum Einstein equations with a
      (possibly zero) cosmological constant Λ ∈ ℝ, on two characteristic hypersurfaces intersecting transversally,
      contains a future neighborhood of the initial data hypersurfaces" (Theorem 1.1, pp. 2-3, stated for smooth data),
      by the same scheme on the higher-dimensional Bianchi equations, with no compactness of S, and assuming vacuum:
      J_jkl ≡ 0 in D_i W^i_jkl = J_jkl ((2.17)-(2.19), p. 6). So in 5D vacuum existence holds on a future neighbourhood
      of N ∪ N′, a statement about the maximal development, which does not depend on the record's gauge. For the record's
      data, which carry the null dusts, neither paper applies: [CTWG23] is vacuum, and [CCTW16]'s matter obeys wave
      equations, while the dusts obey transport equations, and J then carries first derivatives of the dusts' T. The
      route of adding the dusts and their first derivatives to [CTWG23]'s split system ((2.3) there) loses a derivative
      (verifier 209, D490; `checks/dustloss5.py`, exact): a dust along ∂_u, T = K dv ⊗ dv, obeys ∂_u K = cK with c =
      −½∂_u log det γ, minus the null expansion, and J contains ∂_x K, so the system needs ∂_x c, an angular derivative
      of a connection coefficient that is not among [CTWG23]'s unknowns (4.9)-(4.10) nor fixed by (4.1a)-(4.1b); adding
      it needs the derivative of the curvature, so ∂J and the dust's second derivatives, and the system does not close at
      any order (shown at the level of the equations, not as a no-go theorem; D488 had called this route evident). What
      is known instead: Luk and Rodnianski (arXiv:2009.08968, Theorem 4.6, p. 29) treat two null dusts in double-null
      gauge, in 4D with S = S², by a hyperbolic-elliptic-transport system with renormalised curvature that avoids the
      loss (p. 10), and the record's own [Tou24] cites them (p. 3); no 5D version is known here. Read at source (D494,
      corrected D495): Theorem 4.6 (p. 29) gives, for "strongly angularly regular" reduced characteristic data on H_0 =
      [0, I̲] × S² and H̲_0 = [0, I] × S² (Definition 4.5, p. 28, with b ≡ 0 on H̲_0; the dusts may be Radon measures),
      an ε > 0 such that "whenever u_∗ ∈ (0, I] and u̲_∗ ∈ (0, ε], there exists a unique angularly regular weak solution
      to the Einstein–null dust system [in the sense of Definition 2.37] in the domain [0, u_∗] × [0, u̲_∗] × S²": a slab
      along the whole of H̲_0, unique in that class (no statement found that smooth data give a smooth solution). The
      dusts are the two families along the double null directions: Ric = f² du ⊗ du + f̲² du̲ ⊗ du̲ with g⁻¹(du, du) =
      g⁻¹(du̲, du̲) = 0 (Definition 2.2 and Remark 2.3, p. 12; Remark 2.4 excludes non-exact null dusts), which is the
      record's T = K_in dv² + K_out du² (D470), provided the record's dusts are taken along optical functions through N
      and N′; in the record's gauge ∇v is null only where g^vv = 0, D470's own caveat. Existence goes through
      approximation by vacuum solutions (Theorem 4.1, on Luk-Rodnianski's existence theorem in Camb. J. Math. 5(4), 2017,
      their [42]); the coupled system is never solved directly. Uniqueness goes through renormalised curvature and
      transport estimates for tr χ, tr χ̲ and the dusts "in appropriate function spaces which avoid a potential loss of
      derivative" (p. 10; sections 8.4, 8.7, the loss being in the difference estimates, not identified there with
      D490's), with elliptic estimates on the 2-spheres (section 8.6, Proposition 8.15). The hairy-ball restriction of
      Remark 4.9 belongs to Theorem 4.7 and is removed for Theorem 4.6 by cut-off and finite speed of propagation (p.
      85). S² is notation: "all of our results apply if we replace S² by any compact 2-surface S" (footnote 14, p. 12);
      what restricts the result is the 2-dimensional sections, that is, four dimensions. So it is a theorem of the
      record's kind of dust, in four dimensions, for weak solutions in its class, and its route rests on 4D results. A
      dust version of [CCTW16]'s proof would also need its Theorems 5.1 (Rendall's corner) and 5.2 (the spacelike problem
      with boundary) for the coupled equations (pp. 55-56), which the record assumes (D480). Still not computed: the
      dusts' well-posedness given g written out, uniqueness beyond S, and that the record's solution solves the reduced
      equation exactly. For the record's dusts, whose directions ∝ ∇v and ∇u are each tangent to one of N, N′, the corner
      S needs no condition: each dust's value on S is the restriction of its free data on the hypersurface it crosses,
      which then seeds its transport along the other (D470). A general crossing dust, with D470's free k^A on N, may
      cross N′ too, which brings free data there and a compatibility condition at S (verifier 204).

## 4f. The record's section 5.2 with two families (D512)

Deduced, with `checks/twophase5.py` Q1-Q2 (computed, exact, sympy; about 5 s). The record closes the one-family estimate
(RESPONSE-HL-5D.md:490-511) with w = h + φ [∂_θ g1], L0 φ = −½ P s (P a mollifier at scale λ), and three facts: Lemma
5.1, the phase shift being a symmetry, so that ∂_θ g1 is annihilated by the λ⁻¹ part of the linearisation; [∂_θ g1](ℓ,
·) = 0, so that contracting with ℓ ⊗ ℓ kills every λ⁻¹ term and the □̃φ term; and the commutator (2.4), so that Ψ := □̃φ
obeys the transport (5.3). With two families:

- *The decomposition.* w = h + φ_in Y_in + φ_out Y_out, with Y_k := λ⁻¹ ∂_(c_k) G at c = 0, G the two-phase profile of
  section 4 with its phases shifted to (s1 + c1, s2 + c2): Y_in = F1 g1^in + λ F1 ĝ_2, g1^in = W_TT^in + χ dv², F_k :=
  ∂_(s_k), and likewise Y_out. Each φ_k is transported along its own family's generator, L_k φ_k = ½ P s_k(h), L_k :=
  ℓ_k · ∇, with zero data on Σ_τ0: the record's L0 φ = −½ P s, its L0 being −ℓ (RESPONSE-HL-5D.md:190; corrected D513,
  verifier 220, the sign having been carried over with L0's). Unlike the record's s(h) = s(w), here s_k(w) ≠ s_k(h):
  s_in(w) − s_in(h) = e^(−4σ) φ_out F2 χ′ + O(λ) by Q2. Every s_k below is s_k(h).
- *Lemma 5.1 for each phase (deduced).* Each constant shift c_k is a symmetry of the two-phase Stage 0: R^(−1) = 0, and
  R^(0) is met by the transports, ĝ_2 and the two-dust background, for every c (section 4b; its equations do not involve
  s1, s2 except through the profiles). Differentiating at c_k = 0, as in the record's proof, gives P(Y_k) = O(1). The
  ĝ_2 term must be differentiated with the waves: P(F1 W_in) alone keeps, at order λ⁻¹, the mixed harmonics that ĝ_2
  cancels by division at Stage 0 (section 4b T4), and λ F1 ĝ_2 reaches λ⁻¹ because a mixed harmonic's symbol is not
  null.
- *The λ⁻¹ terms (deduced, with section 4d L1).* The principal part of P is −½ g^(ab) ∂_a ∂_b on each component, so the
  commutator [P, φ] acting on a profile in s_k has λ⁻¹ part −(ℓ_k · ∇φ) F_k, the first-order terms of P adding only
  O(1), and −½(□φ) at order 1. With L1 (E[h] = ½(s_in F1² g1^in + s_out F2² g1^out), χ and χ′ included: the record's
  gauge), the λ⁻¹ part of P(w) is Σ_k ½((1 − P) s_k(h)) F_k² g1^(k), the record's remaining term once per family, each
  O(∂s_k) by the mollifier bound. Section 4d's cross terms (L2: −2 e^(−4σ) s_out χ′ in the ℓ_in ⊗ ℓ_in contraction) are
  part of family out's ½ s_out F2² g1^out and cancel with it. So in the record's gauge the decomposition along each
  family's own generator leaves no λ⁻¹ coefficient beyond the record's: section 4d's question is answered at the λ⁻¹
  level.
- *Where the cross coupling goes (deduced from Q2's contractions, which are computed).* [F1 g1^in](ℓ_in, ·) = 0 and [F2
  g1^out](ℓ_out, ·) = 0 in every component, so contracting h's equation with ℓ_in ⊗ ℓ_in kills family in's λ⁻¹ term and
  its □̃φ_in term, as in the record. Family out's survive, through χ′ alone: [F2 g1^out](ℓ_in, ℓ_in) = e^(−4σ) F2 χ′. So
  s_in's wave equation carries ½ e^(−4σ) λ⁻¹((1 − P) s_out) F2² χ′, a bounded coefficient times O(∂s_out), and −½
  e^(−4σ) (F2 χ′) Ψ_out, a bounded coefficient oscillating in s2 times Ψ_out := □̃φ_out; the s_out equation carries the
  mirror terms with χ and Ψ_in. No large coefficient enters either equation: the cross coupling is of order 1, at the
  top order of Ψ. Control: with χ′ ≠ 0, [F2 g1^out](ℓ_in, ·) = 0 fails.
- *The transports (Q1, computed).* On every round double-null metric −2 e^(2σ) du dv + R² dΩ_3, σ and R any functions of
  (u, v) (section 4c's two-dust background is one), with L_in = −e^(−2σ) ∂_u and L_out = −e^(−2σ) ∂_v: [□, L_k] f = a_k
  □f + M_k(L_k f) + N_k f, a_k = 2 L_k R/R (two-thirds of ℓ_k's expansion), M_k and N_k first order; the third
  derivatives cancel identically, as in any commutator of a second-order with a first-order operator. Every second
  derivative not in □ carries the generator's own index (for L_out, ∂_u ∂_v f with coefficient −4 e^(−4σ) R_v/R and ∂_v²
  f with −4 e^(−4σ) σ_u), because each generator is shear-free: the derivative of the angular inverse metric along it is
  a multiple of itself. So Ψ_k := □φ_k obeys L_k Ψ_k + a_k Ψ_k = ½ □P s_k − ½ M_k(P s_k) − N_k φ_k (signs corrected
  D513), the structure of the record's (5.3): on Vaidya R = r and ℓ(r) = 1, so a = 2/r, and ℓΨ + (2/r)Ψ = −(L0 Ψ −
  (2/r)Ψ). Q1 uses □ of g0; the record's □̃ is not restated here. Control: with shear, an angular metric R²(e^(2b) dθ² +
  e^(−2b)(cos²θ dφ1² + sin²θ dφ2²)), the three diagonal angular second derivatives of [□, L_out] remain and no multiple
  of □ removes them.
- *The loop (deduced; not written at the level of the record's supplement).* □P s_in comes from s_in's wave equation, so
  it contains Ψ_out with a bounded coefficient, and □P s_out contains Ψ_in. So (Ψ_in, Ψ_out) obey two transports along
  transversal null directions, coupled through bounded coefficients (P is bounded on L² whatever the oscillation of what
  it acts on), with sources controlled by the energies of h, s_in and s_out. Gronwall on the sum of their L² norms over
  Σ_τ closes this with no loss in λ. The record's supplement Lemmas 3.3-3.4 are written for one family; their two-family
  form, with these couplings, is not written here.
- *The generalised wave gauge (deduced).* H is fixed, so shifting the phases is not a symmetry of Ric − δ*(Υ − H):
  differentiating P_(H)(G(c)) = O(λ) at c1 = 0 with H held fixed gives P_H(Y_in) = −λ⁻¹ F1² h dv ⊗ dv + O(1) (section 4e
  H1: (δ*H)^(0) = F1 h dv² + F2 h′ du²). The decomposition then leaves −λ⁻¹ φ_in F1² h dv ⊗ dv in h's equation, killed
  by ℓ_in ⊗ ℓ_in (dv(ℓ_in) = 0) but entering the s_out equation with (dv(ℓ_out))² = e^(−4σ) (Q2): a λ⁻¹ coupling of φ_in
  to s_out. Removing it needs a transported corrector ψ(X, s1) dv², which is χ again. So for the energy estimate the
  record's gauge is the better one; section 4d's 'the generalised wave gauge removes it' holds for E[w], not for the
  decomposition.

What it does not give: the two-family energy estimate itself (the supplement's Lemmas 3.3-3.4 with these couplings);
(E1)-(E2) for two families; the mollifier against coefficients oscillating at scale λ (P(cΨ) is bounded, not close to c
PΨ); later stages.

## 4g. The record's section 3 with two families (D522)

Deduced from the record's section 3 (N1STAR-PROOF.md:240-337) and sections 4b-4f; nothing is computed beyond 4f's Q1-Q2.
Two-phase profiles G(X, s1, s2), s1 = v/λ, s2 = u/λ; F_k := ∂_(s_k); k_in := dv, k_out := du; ℓ_k := g0⁻¹k_k; the
record's gauge, so χ and χ′ are present; g1^(k) is family k's wave with its gauge term, Y_k := F_k g1^(k) + λ F_k ĝ_2,
G1^k := [F_k g1^(k)], G2^k := [F_k² g1^(k)], and, by Q2, c_in := G1^out(ℓ_in, ℓ_in) = e^(−4σ) F2 χ′ and c_out :=
G1^in(ℓ_out, ℓ_out) = e^(−4σ) F1 χ. The record's section 3 carries over term by term, with three changes: ĝ_2 enters the
phase-shift identity, the phases φ_k solve a coupled system, and the contraction with ℓ_in ⊗ ℓ_in keeps family out's
terms.

- *(3.1′) and (E1′).* R[G] contains no explicit s1 or s2, so R[G(·, · + c1, · + c2)] = R[G](·, · + c1, · + c2).
  g_app⁻¹(k_k, k_k) = λ n1^k with n1^in = −e^(−4σ) χ′ + O(λ) and n1^out = −e^(−4σ) χ + O(λ), each oscillating in the
  other phase (verifier 220); ℓ_app^in := g_app⁻¹ dv = ℓ_in + λ e^(−2σ) χ′ ℓ_out + O(λ²), and likewise for out, so
  |ℓ_app^k − ℓ_k| ≤ Cλ as in the record. G1^k(ℓ_k, ·) = G2^k(ℓ_k, ·) = 0 (Q2), but c_in, c_out ≠ 0.
- *(3.2′) and Lemma 3.1′.* P(w) = −½ g_app^(ab) ∂_a ∂_b w + ½ λ⁻¹ Σ_k s_k(w) G2^k + B·∂w + C·w (D414's L1, with ℓ_app^k
  for the record's ℓ_app). On a two-phase profile, P([Y]) = [λ⁻² P_(−2) Y + λ⁻¹ T Y + P_0 Y] with P_(−2) Y = −g0⁻¹(k_in,
  k_out) F1 F2 Y, nonzero only on mixed harmonics; T is the record's with −½ n1^in F1² − ½ n1^out F2² in place of its −½
  n1 ∂_θ² (g_app⁻¹(dv, du) = g0^(uv) + O(λ²), so there is no mixed λ⁻¹ correction; verifier 225, D523). Differentiating
  (3.1′) at c_k = 0 as in the record gives T(F_k g1^(k)) + P_(−2)(F_k ĝ_2) = O(λ), so P(Y_k) = O(1): λ F_k ĝ_2 reaches
  order λ⁻¹ through P_(−2), and it has to be in Y_k.
- *Lemma 3.2′ (the record's (3.3)).* For φ(X), P(φ Y_k) = −λ⁻¹ (ℓ_app^k · dφ) G2^k − ½ (□̃_app φ) G1^k − ½ λ (□̃_app φ)
  F_k ĝ_2 + (the second term O(λ|d²φ|), handled as the record's c^(ab) ∂_a ∂_b φ in Lemma 3.4; added D523) B1^k · dφ +
  C1^k φ + N_φ^k, with bounded profiles B1^k, C1^k and |N_φ^k| ≤ C|w|(λ⁻²|φ| + λ⁻¹|dφ| + |d²φ|). The cross terms from λ
  F_k ĝ_2, such as −(ℓ_j · dφ) F_j F_k ĝ_2, are of order |dφ| with bounded profile coefficients and go into B1^k.
- *(3.4′) The phases.* ℓ_k · dφ_k = ½ P s_k(h), with h := w − Σ_j φ_j Y_j and φ_k = 0 on Σ_τ0. Since s_k(h) = s_k(w) −
  Σ_j φ_j Y_j(ℓ_k, ℓ_k), with Y_out(ℓ_in, ℓ_in) = c_in + O(λ) and Y_in(ℓ_in, ℓ_in) = O(λ) (and likewise for out), this
  is a linear system for (φ_in, φ_out). It consists of two transports along transversal null generators, coupled through
  the bounded operators φ ↦ P(c φ), and is solvable by Picard iteration wherever both generators are transversal to Σ_τ
  (the analogue of the record's Lemma 1.1(d), not written for the two-dust background). The record's choice, s = s(w) =
  s(h), does not carry over. Defining φ_k from s_k(w) would leave −½ λ⁻¹ P(c_in φ_out) G2^in in h's equation, which is
  not small: a mollifier at scale λ does not remove an oscillation at that scale.
- *(3.5′) The equation for h.* −½ g^(ab) ∂_a ∂_b h + B·dh + C·h = F + N(w) − Σ_k N_φ^k − ½ λ⁻¹ Σ_k ((1 − P) s_k(h)) G2^k
  + λ⁻¹ Σ_k ((ℓ_app^k − ℓ_k) · dφ_k) G2^k − Σ_k φ_k [T1^k] + ½ Σ_k (□̃_app φ_k) G1^k − Σ_k (B1^k · dφ_k + C1^k φ_k).
  This is the record's (3.5) with one 1/λ coefficient per family, (1 − P) s_k(h) = O(λ ∂s_k(h)) by (M3).
- *Lemma 3.3′ (the ℓ_in ⊗ ℓ_in component).* □̃ s_in(h) is the record's Lemma 3.3 for family in (up to O(λ|d²φ_in|) from
  λ F1 ĝ_2(ℓ_in, ℓ_in), which N′ controls; D523), minus 2q times the family-out terms of (3.5′) contracted with ℓ_in ⊗
  ℓ_in. Among these, the term at the top order is −q c_in (□̃_app φ_out) = −q c_in Ψ_out + O(λ|d²φ_out|). The only 1/λ
  one is q λ⁻¹ ((1 − P) s_out(h)) G2^out(ℓ_in, ℓ_in), with G2^out(ℓ_in, ℓ_in) = e^(−4σ) F2² χ′; it is O(∂s_out(h)). The
  rest are bounded profiles times dφ_out, φ_out and λ⁻¹(ℓ_app^out − ℓ_out) · dφ_out = O(dφ_out), together with
  N_φ^out(ℓ_in, ℓ_in). The last keeps the term |w||d²φ_out| that the record's contraction removes, small times second
  derivatives, as in the record's (3.5). So s_in's equation has no large coefficient, and at the top order it couples to
  Ψ_out through a bounded profile oscillating in s2. The equation for s_out is the mirror image.
- *Lemma 3.4′ (Q1).* On a round double-null background (Q1's □ is g0's covariant one on scalars and differs from □̃ by
  first-order terms in φ_k, which join N_k φ_k, as 4f remarks; D523), Ψ_k := □̃ φ_k obeys L_k Ψ_k + a_k Ψ_k = ½ □̃ P
  s_k(h) − ½ M_k(P s_k(h)) − N_k φ_k, with □̃ P s_k(h) = P □̃ s_k(h) + [□̃, P] s_k(h) and □̃ s_k(h) from Lemma 3.3′. So
  Ψ_in's source contains P(c_in Ψ_out) and Ψ_out's contains P(c_out Ψ_in), both bounded on L² whatever the oscillation.
  No □̃ falls on a fast coefficient, because the coupling enters through s_k(h) and not through an explicit c φ. As in
  the record, the second derivatives of φ_k are combinations of L_k P s_k(h), ∂_x P s_k(h), dφ_k and the spatial
  Hessian, which has its own transport.
- *Section 4 with two families.* N′(τ) := Σ_(j≤k) λ^j (‖∂^j ∂h‖ + Σ_k (‖∂^j Ψ_k‖ + ‖∂^j ∂φ_k‖ + λ ‖∂^j ∂_x² φ_k‖)) + ‖h‖
  + Σ_k ‖φ_k‖. Every new term is a bounded two-phase profile times a quantity N′ controls at the same scaled order. A
  derivative of a coefficient costs λ⁻¹, which the weight λ^j absorbs, as for the record's profiles. So the energy
  inequalities take the record's form with N′ for N, and the bootstrap closes as it does there (deduced, not written
  step by step).

What it does not give: (E2) for two families, that is, the two-phase approximant to the order the bootstrap needs (only
Stage 0 is computed, sections 4b and 4e); the two-dust domain Ω, its foliation and Lemma 1.1's transversality; the
mollifier P on that domain; and section 4's steps written out.

## 4h. Theorem A with two families (D526)

Deduced from the record's section 5 (N1STAR-PROOF.md:450-533, Lemmas 5.1-5.3) with section 4g's notation; nothing
computed beyond sections 4b-4f. It concerns the (E2) of section 4g: the two-phase approximant to every order, the
record's Theorem A with two families.

- *(5.1′) The ansatz.* The unknowns are the means m_j (j ≥ 1), two phase corrections φ_j^in, φ_j^out (j ≥ 1), and
  zero-mean profiles ĝ_j(X, θ1, θ2) (j ≥ 2). With ḡ := g0 + Σ_j λ^j m_j, u_in := v + Σ_j λ^j φ_j^in, u_out := u + Σ_j
  λ^j φ_j^out and G := ḡ + λ(W_in(X, θ1) + W_out(X, θ2)) + Σ_(j≥2) λ^j ĝ_j, put g_app := G(X, u_in/λ, u_out/λ). The
  two-scale operator replaces ∂_a by ∂_a + λ⁻¹(∂_a u_in F1 + ∂_a u_out F2), with F_k := ∂_(θ_k).
- *(5.2′) The eikonals.* ḡ⁻¹(du_k, du_k) = Σ_(j≥1) λ^j e_j^k, e_j^k = 2 ℓ_k · dφ_j^k − m_j(ℓ_k, ℓ_k) − q_j^k, with q_j^k
  polynomial in the earlier stages, as in the record's (5.2), once per phase. The cross contraction ḡ⁻¹(du_in, du_out) =
  g0^(uv) + O(λ) = −e^(−2σ) + O(λ) does not vanish. That is the one structural difference from one family.
- *Lemma 5.1′ (where each unknown first enters).* As in the record's proof, by weights, a factor of stage m + 1 reaches
  order m in two ways. The first is ĝ_(m+1)'s pure harmonics (functions of one phase) hit by one λ⁻¹ phase derivative:
  the transports Th^in, Th^out of section 4g, each along its own ℓ_k. The second is m_(m+1) and dφ_(m+1)^k in the
  contractions e_(m+1)^k. In addition, ĝ_(m+2)'s mixed harmonics hit by two λ⁻¹ derivatives of different phases reach
  order m through P_(−2) = −g0⁻¹(k_in, k_out) F1 F2 = e^(−2σ) F1 F2 (section 4g, verifier 225). The pure harmonics of
  ĝ_(m+2) do not, since g0⁻¹(k_k, k_k) = 0. So Rm^(m) = Π_in Th ĝ_(m+1)^in + Π_out Th ĝ_(m+1)^out + P_(−2) ĝ_(m+2)^mix −
  ½ Σ_k e_(m+1)^k F_k² W_k + Wm(m_m, φ_m) + K_m. The mixed projections of Th ĝ_(m+1)^k, algebraic in Z_k, go to (d). K_m
  depends on earlier stages only, ĝ_(m+1)'s mixed harmonics included, which (d) fixed at stage m − 1. On mixed profiles
  Th also carries −c_1 F1 F2, c_1 := ℓ_in · dφ_1^out + ℓ_out · dφ_1^in − m1(ℓ_in, ℓ_out), the λ-coefficient of
  ḡ⁻¹(du_in, du_out): a coefficient known at each stage (verifier 227, D527).
- *Lemma 5.3′ (each stage is a linear hyperbolic system plus a division).* Given everything of earlier stages, impose
  e_m^k = 0 and the four projections of (5.3′). (a) The mean, the record's (a) on the two-dust background: −½ □̃ m_m +
  B̄ · dm_m + C̄ m_m = (sources). (b) The two phases: ℓ_k · dφ_m^k = ½ m_m(ℓ_k, ℓ_k) + ½ q_m^k, along each family's
  generator. (c) The pure harmonics: Π_k Th^k ĝ_(m+1) = −Π_k(Wm + K_m), k = in, out, where Π_k projects on the nonzero
  harmonics of θ_k alone; each is the record's transport for Z_k := F_k ĝ_(m+1), with its source, along ℓ_k. (d) The
  mixed harmonics: P_(−2) ĝ_(m+2)^mix = −Π_mix(Wm + K_m + Th ĝ_(m+1)). On the harmonic e^(i(n1 θ1 + n2 θ2)), n1 n2 ≠ 0,
  P_(−2) is multiplication by −e^(−2σ) n1 n2 on each component, whose inverse is bounded by e^(2σ), uniformly in the
  harmonic: there are no small divisors, and the division loses no derivative. (d) is algebraic, as section 4b's T4 is
  at Stage 0, and it feeds stage m + 1 through K_(m+1). Ψ_m^k := □̃ φ_m^k obey transports of Q1's form along ℓ_k
  (section 4f). The system (a)-(c) for (m_m, φ_m^k, Ψ_m^k, Z_k) is then linear with smooth coefficients and closes
  without loss as in the record, with m_m in H^(s+1), φ_m^k in H^(s+1) and Ψ_m^k, Z_k in H^s. Within each stage, Picard
  iteration gives a unique smooth solution wherever both generators reach Σ_τ0 transversally, with data (m_m, ∂_τ m_m),
  φ_m^in, φ_m^out and the pure harmonics of ĝ_(m+1) on Σ_τ0; the mixed harmonics take no data. (d) then gives
  ĝ_(m+2)^mix with one derivative less than ĝ_(m+1)^mix, through −(ℓ_in · ∂_X) F1 − (ℓ_out · ∂_X) F2 acting on it
  (corrected D527, verifier 227): one derivative per stage, harmless for smooth data and finitely many stages, as for
  the record's K_m.
- *Theorem A′ (deduced).* For every N and every smooth choice of stage data (each family's wave and its phase shift on
  Σ_τ0, the means' data) there are profiles ĝ_2, …, ĝ_(N+1), means and phases with residual Ric^H(g_app) = λ^N times a
  profile bounded with all its derivatives. This is the record's (E3) with K = N − 1; (E1′) is section 4g's, and (E2) is
  Stage 0. Section 4g's (E2), Stage 0 solved, is the case m = 0 (sections 4b and 4e), and the record's Theorem A is the
  case W_out = 0.

What it does not give: the two-dust domain Ω, its foliation and the transversality of both generators to Σ_τ0 (the
analogue of the record's Lemma 1.1, needed for (b)-(c)); the data (Theorem D and Lemma 6.2 with two families: an
outgoing packet's Cauchy data satisfying the constraints and the gauge condition to the order needed); and the proof
written at the level of the record's (one item each: the order counting, the closing of (a)-(c), and the matching of the
stage data).

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

## 4i. The record's Lemma 1.1 with two dusts (D533)

`checks/twodomain5.py` D1-D4 (D1-D2 exact, sympy; D3-D4 computed; about 25 s). The record's Lemma 1.1
(N1STAR-PROOF.md:154-173) is read off the explicit Vaidya g0. For the two-dust background of section 4c it holds in the
same form, with one condition.

- *The record's form with one more function (D1).* Wherever R_u < 0, (v̂, R) are coordinates, v̂(v) any increasing
  function, and g0 = −e^(2ψ)(1 − μ/R²) dv̂² + 2e^ψ dv̂ dR + R² dΩ₃², with e^ψ = −e^(2s)/(R_u v̂′) and μ section 4c's B3
  mass; the inverse has g^(v̂v̂) = 0, g^(v̂R) = e^(−ψ), g^(RR) = 1 − μ/R². The outgoing dust's constraint gives
  (e^(−2s)R_u)_u = −e^(−2s)B/(3R²) ≤ 0 and ψ_u = B/(3R²R_u) ≤ 0. So R_u < 0 everywhere once it holds on the outer cone u
  = u_0, which it does when R_u < 0 at the corner and μ > 0 along u = u_0 (there (R_u)_v = −e^(2s)μ/R³, from the
  evolution; corrected D537); and with v̂ fixed by ψ = 0 on u = u_0, ψ ≤ 0 everywhere. With B = 0, ψ ≡ 0 and μ = μ(v̂):
  the record's g0, with v̂ its v (not the double-null v: in D3 v̂′ is 1.04 to 1.07).
- *Lemma 1.1′ (D2, deduced).* With τ := v̂ − R and Ω, Σ_τ, b(τ) as in the record's (1.1): (a) g^(−1)(dτ, dτ) = 1 − μ/R²
  − 2e^(−ψ) ≤ −1 − μ/R²; (b) on {R = a}, g^(−1)(dR, dR) = 1 − μ/a², negative exactly when μ > a² there, and then
  g^(−1)(dR, dτ) = e^(−ψ) − 1 + μ/a² > 0; (c) g^(−1)(d(v̂ + τ), d(v̂ + τ)) = 1 − μ/R² − 4e^(−ψ) ≤ −3 − μ/R² and
  g^(−1)(dv̂, dτ) = −e^(−ψ) < 0; (d) the ingoing generators are {v̂ = const}, R increasing to the past, so Ω's shape and
  (d) are the record's; (e) follows from (a)-(c) on the compact Ω as in the record. So (a)-(e) hold with at least the
  record's margins, apart from (b), which asks μ > a² on the inner boundary: exactly, μ(u_in, v) = μ(u_0, v) − (2/3)∫ B
  e^(−2s)R_v du > a², the integral along the ingoing ray from u_0 to R = a (section 4c's μ_u). The outgoing dust carries
  mass off across the ray's untrapped part and gives some back across its trapped part, so carrying off less than μ(v̂)
  − a² across the untrapped part is sufficient, not necessary (corrected D537). Both generators are transverse to every
  Σ_τ, a null vector never being orthogonal to the timelike dτ, and by (e) the past integral curve of either, normalised
  by dτ = 1, stays in Ω, so, the background being given on all of the compact Ω, it meets Σ_τ0: what section 4g's (3.4′)
  asked of the domain, given that background (corrected D537, verifier 231: (e) alone gives containment, not the
  meeting). Ω's third constraint is to be read with v̂, and V, T and τ_end need the two-dust r_q (D537). Not covered:
  (f), which needs D_T for two dusts, that is, the curvature threshold r_q of the two-dust background; and the
  background's existence on Ω, which is section 4c's Goursat problem continued over the past of Ω, where R ≥ a (local
  existence is standard; the continuation is not read; D552 supplies the extension criterion, not the continuation, D556).
- *Computed (D3).* A seeded hole: corner data with mass μ0 = 1 at R = 4 (μ and R_u as 5D Tangherlini's, the gauge e^(2s)
  = R_v = ½); an ingoing pulse A = sin⁴ on v ∈ [0.5, 2] and an outgoing one B = 0.4 sin⁴ on u ∈ [1, 2]; section 4c's
  diamond scheme on u ∈ [0, U1], v ∈ [0, 2], U1 where R(U1, 2) = 0.62, clear of the singularity (later v needs resolving
  a strip between the horizon and the singularity that thins exponentially). At n = 40, 80, 160 steps per unit: R_u < 0
  everywhere; with B = 0, max |ψ| (0.100, 0.043, 0.015) and max |μ − μ(v)| (0.072, 0.033, 0.012) fall to 0, the scheme
  converging to Vaidya; with B, max ψ falls to 0 (0.091, 0.039, 0.010) while min ψ rises with n (−0.077, −0.035, −0.016,
  −0.0098 at n = 40 to 320, verifier 231), its limit small and negative, and μ departs from μ(v) by about 0.1, still
  moving with n (0.156, 0.125, 0.105, 0.098); max g^(−1)(dτ, dτ) = −1.051, attained on the data cone u = 0, its ratio to
  −1 − μ/R² (at least 1 analytically) rising to 0.992 and 0.995 at n = 160; the cells with 0.7 ≤ R ≤ 0.75 are trapped,
  with μ − a² ≥ 0.76, but on this rectangle they lie only at v ≥ 1.975 (verifier 231, D537). On the whole curve (D3b: u
  ∈ [0, 8], cells with R ≤ 0.3 left out), every v-column of [0, 2] crosses R = a and is trapped there, with min μ − a² =
  0.510 (B = 0) and 0.413 (B = 0.4), the same at n = 80 and 160 to 10⁻³; s at the crossing reaches 1.08, the cut lying
  near the singularity in R.
- *Control (D4).* A strong outgoing pulse just outside the horizon, B = 3 sin⁴ on u ∈ [3.5, 5]: on 0.7 ≤ R ≤ 0.75 the
  least μ − a² is −0.41 and 1 − μ/R² reaches 0.85, so part of R = a is untrapped and (b) fails there, while (a) and (c)
  still hold. The condition is a real one.
- *D_T and (f) (D546; `checks/twodt5.py` T1-T3, T1 exact and the rest deduced; corrected D549).* On the two-dust
  solutions the Kretschmann scalar is R_abcd R^abcd = 72μ²/R⁸ + (8/3)e^(−4s)AB/R⁶ (T1, sympy, with the evolution and
  both constraints), the record's 72μ²/r⁸ at B = 0; the dust term is ≥ 0 when AB ≥ 0, as for the record's dusts (A, B ≥
  0; corrected D549): one null dust has R_abR^ab = 0, two crossing ones do not. The record's D_T is radial, {v ≤ V, r ≥
  r_q(v)} (N1STAR-PROOF.md:172-173); its two-dust form D_T := {v̂ ≤ V, R ≥ r_q(μ)}, μ the Misner-Sharp mass at the
  point, contains the curvature form {v̂ ≤ V, K ≤ l5⁻⁴}, since K ≤ l5⁻⁴ gives R ≥ r_q(μ) = (√72 μ l5²)^(1/4) when AB ≥
  0; on Vaidya both are the record's (corrected D549: the l5⁻⁴ form is ours, not the record's). With r_q^♭(v̂) the least
  r_q(μ) over D_T's points on the ingoing ray v̂, D_T ⊂ {R ≥ r_q^♭(v̂)}, and the record's proof of (f) runs with r_q^♭
  for r_q, q0 := min r_q^♭ and τ_end := max_(v̂≤V)(v̂ − r_q^♭(v̂)). (f) needs no mass condition: it holds with any q0 at
  most min r_q^♭. (b) follows from the record's seed condition read for the Misner-Sharp mass over the region, R = a
  included: with μ_min a lower bound of μ there (the record's μ0, Vaidya's μ being non-decreasing; a bound on a larger
  set fixed in advance avoids Ω depending on a) and q0 := r_q(μ_min) ≤ min r_q^♭, μ_min ≥ √72 l5² gives q0⁴ = √72 μ_min
  l5² ≤ μ_min², so q0 ≤ √μ_min, and a := q0 − δ0 has a² < μ on R = a (T2; the control μ_min = √72 l5²/2 fails).
  (Corrected D549, verifier 238: D546 took q0 := min r_q^♭, D_T's least value, and both (b) and (f) from μ_min ≥ √72
  l5²; but R = a lies outside D_T, where the outgoing flux may lower μ below D_T's least mass, and then a² ≥ μ there:
  T3, l5 = 1, μ = 10 on D_T and 8.6 on R = a, q0 = 3.0351 > √8.6 = 2.9326, while q0 := r_q(8.6) = 2.9227 holds.) The
  outgoing dust lowers μ outside the hole, so this bounds the mass it may carry off before the region; D4's strong pulse
  breaks it.
- *The background on Ω: an extension principle (D552; `checks/twoext5.py` X1-X3; X1-X2 exact, the chain deduced, X3
  computed; corrected D556).* [Mos17] (G. Moschidis, arXiv:1704.08685) Lemma 5.1 (pp. 42-43, READ) is the continuation
  criterion for the spherically symmetric Einstein-null dust system with ingoing and outgoing dust in 3 + 1: a smooth
  solution on [u1, u2) × [v1, v2) whose data on the two initial cones extend to their far ends, with inf r > 0 and sup r
  < ∞, extends smoothly to the closed rectangle; its proof integrates ∂_u∂_v(r²) = −½Ω², the mass's ∂_u∂_v m̃ (the two
  dusts' cross term) and ∂_u∂_v log Ω² ((5.210)-(5.222)). The 5D two-dust form holds with R³ for r²: on the evolution
  (R³)_uv = −3Re^(2s), R_uv = −e^(2s)μ/R³ and s_uv = (3/2)e^(2s)μ/R⁴ (X1; the cross term R_uR_v cancels at exponent 3
  exactly, and (R²)_uv keeps it), and with the constraints μ_uv = (2/9)AB e^(−2s)/R² ≥ 0 (X2; with B depending on v a
  residual remains, which detects the compatibility condition B_v = 0). On a rectangle where R ≥ a > 0, with D[F] :=
  F(u1, v) + F(u, v1) − F(u1, v1) the data's corner combination: 3∫∫Re^(2s) = D[R³] − R³, so sup R ≤ (max D[R³])^(1/3)
  needs no hypothesis and ∫∫Re^(2s) ≤ R_max³/3; μ ≥ min D[μ]; s ≥ min D[s] − (3/2)(m0⁻/a⁵)R_max³/3, since e^(2s)/R⁴ ≤
  Re^(2s)/a⁵; then μ ≤ max D[μ] + (2/9) max(AB) e^(2S)|Q|/a² and s ≤ max D[s] + (3/2)(M⁺/a⁵)R_max³/3; R_u, R_v by
  integrating R_uv from the cones; higher derivatives by commuting, linear in the top order, as [Mos17] does. No
  bootstrap is needed, each bound coming from the data, a and the ones before it (corrected D556: a = min R is an
  interior value, not data). So a solution given on a half-open rectangle with R ≥ a extends to the closed rectangle:
  [Mos17] Lemma 5.1's extension criterion in 5D. (Corrected D556, verifier 241: D552 went on to "the development ends
  only where R → 0". That needs 5D local existence, [Mos17] Proposition 5.3 being a small-step statement that assumes
  ∂_u r < 0 (R_u < 0 holds here, D537) and smallness conditions, and the continuation loop of [Mos17] section 5.4 (pp.
  48-59); neither is written.) On D3's background (X3, n = 40 to 320; U1 the last u at n = 160 with R(u, 2) ≥ 0.62,
  R(U1, 2) ≈ 0.68 being the rectangle's least, corrected D556) the identity's residual falls to 2.0 × 10⁻⁵ (local orders
  0.78, 1.52, 1.80), the constraint residuals fall at second order in the bulk and, from n = 80, at the far corner,
  where R_uu is large (D556), and the bounds from the cones' data and a contain the computed R, μ and s (μ and s attain
  their lower bounds on the data; the upper bounds are coarse, s ≤ 2.7 × 10³ against 1.12). With Lemma 1.1′: {R ≥ a} is
  closed to the past in the rectangle wherever μ > a² on R = a, since R_u < 0 and R = a is trapped there (going back in
  v, R cannot fall through a), so the criterion applies on Ω's past part of the rectangle, given the data on its two
  cones (deduced; closed in u as well, R_u < 0 at R = a; and checkable from the data, μ ≥ min D[μ] > a² sufficing, 0.903
  against a² = 0.46 in X3). Existence there needs the local existence and continuation above (corrected D556). Not: the
  data themselves, that is, the outgoing family's data at past null infinity.
- *Existence: a truncated Volterra iteration (D558; deduced; `checks/twoext5.py` X4 computed; corrected D561).* D556
  left existence open, the extension criterion needing a solution to extend; the system's integral form gives both. With
  U := (R, s, P, Q), F := −(e^(2s) + 2PQ)/R and G := 3(e^(2s) + 2PQ)/(2R²), a continuous solution of P = P(u, v0) +
  ∫_(v0)^v F dv′, Q = Q(u0, v) + ∫_(u0)^u F du′, R = R(u0, v) + ∫_(u0)^u P du′, s = D[s] + ∫∫G, with the cones' data
  (P(u, v0) = ∂_uR(u, v0), Q(u0, v) = ∂_vR(u0, v)), solves B1: R_u = P and R_v = Q follow, so R_uv = F and s_uv = G, and
  the constraints hold by B2's propagation from the cones, given cone data that satisfy them, C_u(·, v0) = 0 and C_v(u0,
  ·) = 0, and A, B ≥ 0, which the chain's (ii) and (iv) use (corrected D561, verifier 243: the integral system imposes
  nothing on the cone data, and propagation only transports a violation; with C_u violated by 5 % of the dust term on
  the cone the bulk |C_u| stays at 2.4 × 10⁻³ under refinement, and Picard without the truncation diverges, so the
  truncation is essential). Fix a > 0 and K > K_0, K_0 the bound the chain (i)-(vi) gives on Q with that a (it depends
  on the data, a and Q only); replace F, G by F_K, G_K, equal to them on {|U| ≤ K, R ≥ a} and globally Lipschitz in U.
  The truncated map is a contraction in the Bielecki norm sup e^(−γ(u − u0 + v − v0))|U| for γ large (each single
  integral divides the Lipschitz constant by γ, the double one by γ²), so it has one continuous fixed point Ũ on all of
  Q. Let p ∈ Q have R̃ > a on J⁻(p) ∩ Q. If |Ũ| ≥ K somewhere there, take such a point q with u + v least: on J⁻(q) ∖
  {q}, Ũ solves the true system with R ≥ a, so the chain gives |Ũ| ≤ K_0 there and, by continuity, at q, a
  contradiction. So Ũ solves B1 on J⁻(p) ∩ Q, within the bounds, and is smooth there (differentiating the integral
  equations, the data being smooth; the commuting step of [Mos17]; sketched, not written); and any solution on a
  past-closed set agrees with it (the same contraction). Hence the solution exists on Q_a := {p ∈ Q : R̃ > a on J⁻(p) ∩
  Q} for every a > 0, the truncations agreeing where both solve B1, and the development within Q is the union of the
  Q_a: it ends only where R → 0, which is D552's claim D556 withdrew, now deduced without [Mos17] Proposition 5.3 and
  section 5.4 (corrected D561: "proved" ran ahead of a sketch whose smoothness step is not written). Its part {R ≥ a} is
  closed to the past where μ > a² on R = a (D552, D556), the region Ω lies in, so the background exists on Ω's past part
  of Q given the cones' data. Computed (X4): the integral system's Picard iteration, by the trapezoidal rule, converges
  on all of D3's rectangle, not only near the corner (to 10⁻¹³ in 32 to 52 iterations at n = 40, 80, 160), and its limit
  agrees with the diamond scheme's to second order in the bulk (u ≤ 5, R ≥ 1: max |R| difference 1.29 × 10⁻⁵, 3.22 ×
  10⁻⁶, 8.13 × 10⁻⁷, ratio 4.0); the 3.1 × 10⁻², 6.2 × 10⁻³, 1.5 × 10⁻³ quoted before were the far corner's (corrected
  D561). The far corner (U1, 2), at R ≈ 0.68, is resolved by neither scheme: R_uu there grows with n (38 to 227 at n =
  40 to 640, two cells from the corner) while interior points converge (R_uu(U1 − 0.05, 1.95) = −34.57 to −33.58), so
  the computation supports smoothness in the bulk only, not at the corner; it shows no singularity either (verifier
  243). The example's data are C³ bumps (sin⁴), not smooth. Open: the cones' data, that is, the outgoing family's data
  at past null infinity.
- *The data with two families, scoped, and the constraint iteration's linearisation (D566; deduced, and
  `checks/data5two.py` T1-T5, exact).* The record's Theorem D (N1STAR-PROOF.md:546-802) builds the data on Σ_τ0 in three
  steps, read here for a second, outgoing family. (i) Lemma 6.1, the gauge's propagation from (F1)-(F2) (600-621): its
  oscillating part is a transport along ℓ = −L0 (614); with two families each family's pure harmonics are transports
  along its own generator, and both generators reach Σ_τ0 inside Ω (Lemma 1.1′, D537); the mixed harmonics are
  algebraic, their symbol −e^(−2σ)n1n2 not vanishing (section 4h's (d)), so they vanish with the lower orders. (ii)
  Lemma 6.2's stage data: the polarization Pol(Y) = Y(ℓ, ·) − ½dv tr Y is onto for any nonzero null covector (635-636;
  data5.py S1, every pair of a Lorentzian metric and a null covector being GL(5)-equivalent), so each family's pure
  harmonics are fixed as the record's; the mixed harmonics take no data (Lemma 5.3′ (d)); the means' constraints are
  Lemma 6.4's radial problem, now on the two-dust background's slice, which needs the spheres' mean curvature H > 0
  there (Lemma 6.3, 670-672): not checked here. (iii) Proposition 6.5's iteration needs the linearisation of the
  constraint map at the approximant's slice data to have no 1/λ coefficient (data5.py S2). With both families (T1, flat
  background) and with the outgoing one alone (T2) it has none; and the outgoing phase need not be null for this (T3,
  speed 1/2; T4, u = τ − r on Vaidya, where du is not null): the cancellation rests on the waves' tracelessness on the
  spheres, an outgoing wave with an oscillating trace giving a 1/λ coefficient (T5, the control), as data5's mutant
  trace_W does for the ingoing one. The 1/λ coefficients are linear in the waves, so the mixed terms enter at order λ⁰
  only (deduced). The outgoing family's waves cannot come in from past null infinity, outgoing rays traced back running
  inward: their data, and the outgoing dust's, are posed on Σ_τ0 and on the cone v = v0, not at I⁻. Open: data5.py's
  S3-S6 for two families (the parabolicity and the symmetrizer on the two-dust slice, with H > 0), and the proof written
  at the record's level.

What it does not give: the background on Ω beyond the computed rectangle, which does not
reach Σ_τ0 (outgoing rays from R = a leave it through v = 0 at τ between −0.96 and −0.69, above the τ0 < −1.47 the
record's rule gives for these parameters, verifier 231); Theorem E on the two-dust background, which needs C^k bounds
and the two families' transversality (E1), (e) being a C⁰ statement; the outgoing family's data, which in the record's
setting come from Σ_τ0 or from past null infinity (section 4c).

## 5. Sources

READ (abstracts, fetched from arxiv.org on 2026-10-31 and quoted from those pages): [Tou24] A. Touati, "The reverse
Burnett conjecture for null dusts", arXiv:2402.17530v2; [HL25] C. Huneau, J. Luk, "High-frequency backreaction for
the Einstein equations under U(1) symmetry: from Einstein-dust to
Einstein-Vlasov", arXiv:2506.21779v1. The record: RESPONSE-HL-5D.md sections 2.4, 4, 5.1-5.2 and 9.
