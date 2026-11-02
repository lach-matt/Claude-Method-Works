# FAMILIES5-NONROUND -- the non-round Einstein–null-dust background in the class: what the class recovers, and where not

Status (2026-11-02). This note attacks FAMILIES5-FULL.md Part II's obstruction (the existence of a non-round,
T²-invariant Einstein–null-dust background on a domain like Ω₂, without smallness) and does not edit that file, the
paper, N1STAR-PROOF.md, FAMILIES5.md, ROUTES-OPEN.md, N1STAR-LOG.md or any proof5 Part.

**Verdict.** The near-round, large-data problem posed in section 1 (Cauchy stability of Part I's round two-dust
background on Ω₂) **does not close**. The obstruction is **localised at the axes**: off them the problem closes
(Theorem N), at them the closing structure provably degenerates (computed), and what would replace it is identified:

- *Off the axes the class recovers the dust's derivative, with no smallness* (sections 2-3). In the T² × Z2 × Z2 class,
  the null second fundamental form of every invariant null hypersurface is diag(θ_h, κ1, κ2) with κ_i = g⁻¹(du, dψ_i)
  first order; so the five-dimensional Raychaudhuri equation for each family closes on its expansion θ (class equation
  (R), computed), the augmented system (g, p_A, θ_A, q_A) has sources of order zero, and its energy hierarchy closes at
  a fixed order like the record's section 4. **Theorem N** (deduced; every identity computed): Cauchy stability, on a
  domain of the record's type, of any smooth class Einstein–N-null-dust solution whose dusts stay a distance δ from the
  axes, for any N and any size of background. **Corollary N1**: the seed (Tangherlini, large) carrying any finite
  number of small non-round families supported away from the axes has its background on the whole domain.
- *At the axes the recovery fails* (section 4). There the degenerate circle's curvature κ2 becomes a Hardy quotient,
  of order one in the eikonal's gradient (computed: its axis value is ∂₃²u/a; its coefficient off the axis is
  1/(a ρ2); the ratio ‖κ2‖/‖du‖ is √2/ε for invariant data concentrating at the axis, bounded for rings), and the
  derivative lost is the planar shear, which is recovered only by an elliptic estimate across the family's generators
  (computed in a flat model), i.e. by the Codazzi/torsion hierarchy of the double-null method — available in four
  dimensions ([LR20]) and not here. Part I's round dusts meet the axes, so near-round perturbations of Part I's
  background stay open. **Corollary N2** (a shorter domain): a perturbation of Part I's data supported in an angular
  band has a background up to the time its influence reaches the axes (τ − τ0 < a(θ1 − θ2), from the computed bound
  R|dΩ/dτ| ≤ 1 on Part I's background), conditional on band-localised constraint data, which are not constructed here.

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a negative control that it must
reject), **deduced** (argued here), **READ** (verbatim, identifier and page, read at source through alphaXiv,
2026-11-02). New programs: `checks/classchi5.py`, `checks/augment5.py`, `checks/axisloss5.py`, and the exact jet
arithmetic they share, `checks/jetpoly5.py`, each with its `.out`, all PASS.

---

## 1. The problem posed, and the loss located

**Posing (deduced).** Let ů = (g̊, ů_A, F̊_A) be a smooth class solution of the Einstein–N-null-dust system
Ric(g) = Σ_A F_A² du_A ⊗ du_A, g⁻¹(du_A, du_A) = 0, div_g(F_A² ∇u_A) = 0 on a compact domain Ω of the record's type
(N1STAR-PROOF.md (1.1), Lemma 1.1 (a)-(f) for g̊) — for Part I, g̊ the round two-dust background on Ω₂, the families
v̂ and u, N = 2. Near-round, large data means: the data on Σ_τ0 are within ε of ů's in the energy norm of section 3,
non-round (θ-dependent densities, non-radial phases, or extra small families), while ů itself is large (a black hole,
μ ≥ μ0, R = a trapped). Existence on the fixed Ω for ε small is Cauchy stability, which is part of well-posedness in
Hadamard's sense: "for a solution u ∈ C([0, T]; H^s), small perturbations of the initial data u_0 yield solutions which
are also defined in [0, T]" (READ, [IT20] p. 2). So the question is whether the system is well-posed, at fixed order,
around a large solution, without smallness of the solution.

**Where a derivative is lost (computed: `augment5.py` S1, controls (a)-(b)).** With g at order m + 1 (dg in H^m), the
eikonal's gradient p = du has the regularity of the geodesic flow, H^m; the generic second derivatives ∇²u are at H^(m−1)
(their Riccati equation is driven by the curvature); the density is transported by the expansion θ = □_g u, so
F² ∈ H^(m−1), T = Σ F² p ⊗ p ∈ H^(m−1), and the wave equation returns g at order m only. The loop wave → p → θ → F² →
T → wave loses one derivative (S1 control (a): the density transport with div P in place of an expansion unknown is at
order m − 1). Carrying θ as an unknown with the general five-dimensional Raychaudhuri equation does not help by itself:
its source |∇²u|² holds the shear, again at m − 1 (S1 control (b)). This is FAMILIES5.md 4i's dustloss5 in the Cauchy
setting.

## 2. The class structure (computed: `classchi5.py` C1-C4)

Off the axes, g = h_ab(y) dy^a dy^b + G1 dφ1² + G2 dφ2², G_i = |K_i|² = e^(2ψ_i), K_i = ∂_(φ_i) (the paper's
Proposition 2.1 form). For an invariant phase u, P := g⁻¹ du, κ_i := g⁻¹(du, dψ_i) = P(ψ_i).

**Proposition C.** (C1, exact, symbolic; h, its inverse, G_i, u arbitrary) ∇²u has no mixed components, ∇²u(∂_a,
∂_(φ_i)) = ∇²u(∂_(φ1), ∂_(φ2)) = 0, and ∇²u(∂_(φ_i), ∂_(φ_i)) = G_i κ_i: the Killing identity ∇²u(K, K) = ½ g⁻¹(du,
d|K|²) makes the torus components first order. So the null second fundamental form of {u = c} is, in an orthonormal
frame (e_θ, e_φ1, e_φ2) of a section, χ = diag(θ_h, κ1, κ2), and only θ_h := □u − κ1 − κ2 carries second derivatives
of u. Controls (rejected): g_(φ1φ2) ≠ 0 (T²-invariant, not Z2 × Z2), a Kaluza–Klein term g_(tφ1) ≠ 0, and a phase
u + w cos φ1 each break it.

(C2, exact at rational jets, three seeds) Where g⁻¹(du, du) vanishes to first order,

    |∇²u|²_g = (□u − κ1 − κ2)² + κ1² + κ2².                                                                  (C)

Controls (rejected): no null condition; g_(φ1φ2) = 1/3; the phase u + φ1²/5.

(C3, exact at jets) Bochner's identity P(□u) + |∇²u|² + Ric(P, P) = ½ □(g⁻¹(du, du)) holds at a non-null jet (a check
of the code, □ g⁻¹(du, du) ≠ 0 there); where g⁻¹(du, du) vanishes to second order (u an eikonal), with (C), the **class
Raychaudhuri equation**

    P(θ) = −(θ − κ1 − κ2)² − κ1² − κ2² − Ric(P, P),        θ := □_g u.                                       (R)

Controls (rejected): the shear-free right side −θ²/3 − Ric(P, P); the null condition to first order only ((R) fails,
(C) still holds). With Einstein–dust, Ric(P_A, P_A) = Σ_B F_B² g⁻¹(du_A, du_B)²: the right side of (R) holds θ, p and
dg, and no derivative of θ, of p, or second derivative of g.

(C4, exact at jets) P(κ_i) = −κ_i² − Rm(P, e_i, P, e_i), e_i = K_i/|K_i|: the torus curvatures have their own Riccati
equations, driven by curvature (wrong sign rejected). Their first-order character is therefore *algebraic* (the Killing
identity), not dynamical — which is why it can, and at the axes does, degenerate.

**The comparison with Huneau–Luk (READ; deduced).** In their 2+1 quotient the null hypersurfaces have one-dimensional
sections, so χ_A is a scalar with no shear and Raychaudhuri closes: "L_A(χ) + χ² = −R_(L_A L_A) = −(L_A ϕ)² −
e^(−4ϕ)(L_A ϖ)²" ([HL25] (6.31), p. 22; the dust term enters Ric(L_A, L_A) as in their p. 49), and their local theory
carries the density one derivative above the generic second derivatives of the eikonal: "max_A (‖F_A‖_(H^k) + ...) ≤
C_h" with "‖∇u_A − c_A‖_(H^k_δ)" and the metric in H^(k+2) ([HL18] Theorem 3.3, p. 9). The smallness there is the
elliptic gauge's, not the dust's: "Due to the globality (in space) of the elliptic estimates for the metric components,
local existence in the elliptic gauge requires a smallness assumption" ([HL25] p. 4), and "it is important to note
that the smallness is not needed for the higher norms" ([HL18] p. 9). Their symmetry has no fixed points: φ and g are
viewed as functions on I × R³ "which do not depend on the variable x³" ([HL18] p. 3, footnote 5). At source, [HL25]'s
p. 5 use of Raychaudhuri, which FAMILIES5-FULL Part II quotes, is a gain in λ for the parametrix: "while general second
derivatives of u_A − u_A^0 is only O(λ^0) (with dependence on N), the special combination χ_A − χ_A^0 is better and is
O(λ^1) ... To obtain this improvement, we use the Raychaudhuri equation that χ_A satisfies" (pp. 4-5). Proposition C
is the five-dimensional class version of the 2+1 structure: the two torus directions add principal curvatures that are
first order, and the one orbit direction carries the whole expansion. It holds where the T² action is free.

## 3. The augmented system off the axes, its energy hierarchy, and Theorem N

**The system (A).** Unknowns: g, and per family a covector p_A, an expansion θ_A and a density q_A = F_A²;
P_A := g⁻¹p_A; κ_Ai := g⁻¹(p_A, dψ_i); χ_A an invariant cut-off, 1 on a neighbourhood of the background's dust tube
and 0 within distance δ of the axes; S̊_A the right side of (R) evaluated on ů (a fixed smooth function).

    (A1) Ric^H(g) = Σ_A q_A p_A ⊗ p_A        (the record's (0.2), wave-map gauge relative to g̊);
    (A2) P_A^b ∂_b p_(A,a) = P_A^b Γ[g]^c_(ba) p_(A,c)    (∇_(P_A) p_A = 0);
    (A3) P_A(θ_A) = χ_A S_A + (1 − χ_A) S̊_A,  S_A := −(θ_A − κ_A1 − κ_A2)² − κ_A1² − κ_A2² − Σ_B q_B g⁻¹(p_A, p_B)²;
    (A4) P_A(q_A) = −θ_A q_A.

**Proposition A (computed: `augment5.py`).** (S1) Every source of (A) is at order m when the energy controls ∂^j of dg,
p_A, θ_A, q_A for j ≤ m: the loop closes (the three controls lose one derivative each: the density transport with
div P, the general five-dimensional shear, and κ2 at an axis point). (S2, exact at jets, general 5D metric and covector
field) P(N) = 2 g⁻¹(p, ∇_P p) for N := g⁻¹(p, p); (∇_P p)_a = ½ ∂_a N + P^b (dp)_(ba); Cartan's L_P(dp) = d(i_P dp).
So under (A2) N = 0 and dp = 0 propagate along P_A (controls: the transport without the Christoffel term, and a
non-closed 2-form, are rejected): p_A stays du_A, u_A an eikonal. (S3) ∇^a T_ab = (P(q) + q div P) p_b + q (∇_P p)_b
and tr T = q N, so under (A) div T = −Σ_A d_A q_A p_A with d_A := θ_A − div P_A (control: P(q) = −θq/2 rejected).
(S4) With (R) for div P_A = □u_A: P_A(d_A) = −d_A(θ_A + div P_A − 2κ_A1 − 2κ_A2) − (T − Ric)(P_A, P_A), homogeneous
(control: the shear-free source leaves an inhomogeneous term). (S5) B_g T := −div T + ½ d tr T = Σ d_A q_A p_A + ½
d(Σ q_A N_A); with the record's propagation identities (`propagate5.py` P1-P2) the gauge vector W solves □W + Ric(W) +
(first order in W) = 2 B_g T. (S6) The transport roots meet the light cone at the conormal p_A (P_A(p_A) = 0 =
g⁻¹(p_A, p_A)); a timelike transport field (control) does not. (S7) On Part I's background in its chart (τ = v̂ − R,
ψ ≤ 0, f ≤ 1), every future causal vector with dτ = 1 has R|dΩ| ≤ (e^ψ/(2 − e^ψ f))^(1/2) ≤ 1 and dR ∈ [−1, e^ψ
f/(2 − e^ψ f)] ⊂ [−1, 1], negative where f < 0 (control: e^ψ f = 1.9 gives R|dΩ| up to 3.16).

**Theorem N (deduced; identities computed in classchi5, augment5).** Fix m ≥ 6 and δ > 0. Let Ω be a compact domain of
the record's type for g̊ (N1STAR-PROOF.md Lemma 1.1 (a)-(e) with g0 := g̊) and ů a smooth T² × Z2 × Z2-invariant
Einstein–N-null-dust solution on Ω with (H1) each ů_A smooth on Ω with dů_A ≠ 0 (no caustic on Ω), and (H2) closed sets
S_A ⊂ Σ_τ0 containing supp F̊_A ∩ Σ_τ0 whose P̊_A-tubes D̊_A in Ω lie at distance ≥ 2δ from the axes. Then there are
ε > 0 and C such that every invariant datum on Σ_τ0 satisfying the constraints and the gauge condition, within ε of ů's
in the norm N_m below, with supp F_A ∩ Σ_τ0 ⊂ S_A, has a unique smooth invariant Einstein–N-null-dust development on Ω,
within Cε of ů in N_m, with p_A = du_A, θ_A = □u_A on the dust and supp F_A within Cε of D̊_A. No smallness of ů or of
the families is assumed; ε and C depend on ů, Ω, N and δ.

*Proof, at the level of the record's section 4.* Put w := g − g̊, π_A := p_A − p̊_A, ϑ_A := θ_A − θ̊_A and
ς_A := q_A − q̊_A,

    N_m(τ) := Σ_(j≤m) ( ‖∂^j ∂w‖ + Σ_A ( ‖∂^j π_A‖ + ‖∂^j ϑ_A‖ + ‖∂^j ς_A‖ ) ) + ‖w‖     on Σ_τ ∩ Ω

(no λ: the background has no oscillation).

- *Step 1 (Sobolev).* The record's Lemma 2.1 without the λ weights: ‖∂^i U‖_∞ ≤ C N_m for i ≤ m − 3, and Moser's
  product estimate on the annuli A(τ).
- *Step 2 (data).* τ-derivatives on Σ_τ0 from (A); N_m(τ0) ≤ C ε. The data of θ_A are □u_A, those of q_A are F_A².
- *Step 3 (bootstrap).* Suppose N_m ≤ 2C*ε on [τ0, τ*]. For ε small, g satisfies Lemma 1.1(e); each P_A is future
  causal and transverse to Σ_τ; its integral curves from S_A stay within Cε of D̊_A (ODE comparison on the compact Ω),
  hence in {χ_A = 1}; θ_A stays bounded (no caustic).
- *Step 4 (w).* ∂^α (A1), the record's Lemma 2.3: the source ∂^α(T − T̊), T − T̊ = Σ (ς_A p_A p_A + q̊_A(π_A p_A +
  p̊_A π_A)), is at most C N_m; the commutators [∂^α, g^(ab)] ∂_a ∂_b w and the quadratic terms give C N_m + C N_m².
- *Step 5 (π_A).* ∂^α (A2), the record's Lemma 2.4 for the transport along P_A: the source holds (Γ[g] − Γ[g̊]) p p,
  Γ[g̊](p p − p̊ p̊) and (P_A − P̊_A)·∂p̊_A, the commutator [∂^α, P_A·∂]π_A has top term (∂^α P_A)·∂π_A; all at most
  C N_m. The boundary terms have the record's sign for every family: the lateral boundaries are spacelike with Ω to
  their past (Lemma 1.1 (b), (c), (e)), so every future causal transport field leaves Ω through them (on Part I's
  background, explicitly, S7: outer b′ − c ≤ −2 + 1, inner c(a) < 0 since R = a is trapped); the angular part of P_A
  enters only the bulk divergence term.
- *Step 6 (ϑ_A).* ∂^α (A3): χ_A (S_A(U) − S_A(ů)) is a smooth function of (dg, p, θ, q) on supp χ_A, where |K_i| ≥ cδ
  (Proposition C, S1), so its ∂^α is at most C(δ) N_m (the constant carries δ^(−1−j) from the derivatives of
  1/|K_i|²); the term (P_A − P̊_A)·∂θ̊_A and the commutator likewise.
- *Step 7 (ς_A).* ∂^α (A4): −ϑ_A q_A − θ̊_A ς_A − (P_A − P̊_A)·∂q̊_A, at most C N_m.
- *Step 8 (closing).* N_m(τ) ≤ C2 (N_m(τ0) + ∫ (N_m + N_m²)); Gronwall: N_m ≤ C3 ε < 2C3 ε for ε ≤ ε0, which improves
  the bootstrap. The smallness is of the perturbation only.
- *Step 9 (existence).* (A) in the record's first-order form ((w, ∂_τ w, ∂_y w) as in its Step 8 (ii)-(iii), plus the
  transports) is a quasilinear symmetric hyperbolic system with smooth zero-order sources; extended to R⁴ by the
  record's Step 8 (i), (iv). Local existence and continuation are Kato's theorem: "The equation (1.2) is locally
  well-posed in H^s in the Hadamard sense for s > d/2 + 1" (READ, [IT20] Theorem 1, p. 3, for ∂_t u = A^j(u)∂_j u with
  "the m × m matrices A^j ... symmetric", p. 2; the general A⁰(u, x) with zero-order sources is Kato's original
  setting, [IT20]'s [16], not READ). The record's [DS23] does not apply as stated: its (A4) asks the eigenvalues not
  to meet, and here the transport roots meet the light cone at ξ = p_A (S6). Symmetry by uniqueness: (A) is invariant
  (|K_i|² is invariant, K_i up to sign).
- *Step 10 (constraints).* S2: N_A ≡ 0 and dp_A ≡ 0, so p_A = du_A with u_A an eikonal (the slices are annuli in R⁴,
  simply connected). On the dust tube D_A ⊂ {χ_A = 1}, (R) holds for □u_A (Proposition C) and S4 gives P_A(d_A) =
  −d_A(...) + (δ*W)(P_A, P_A); S5 gives □W + Ric(W) + (first order) = 2 Σ d_A q_A p_A. The energy ‖∂W‖² + ‖W‖² +
  Σ_A ‖d_A‖²_(L²(D_A ∩ Σ_τ)) obeys a linear Gronwall inequality (the tube's lateral boundary is ruled by P_A, so the
  transport has no flux through it), with zero data: W = 0, ∂_τ W = 0 (the gauge condition and the constraints, the
  record's P3-P4) and d_A = 0 (θ_A := □u_A on Σ_τ0). So D(g) = 0, Ric(g) = T, θ_A = □u_A, and (A4) is the dust's
  conservation law: an Einstein–N-null-dust solution. ∎

**Corollary N1 (deduced).** Let g̊ be the seed (Tangherlini of mass μ0 ≥ √72 l5²; F̊_A = 0) on the record's domain with
μ ≡ μ0, and ů_A any finite set of invariant eikonals of the seed, smooth on Ω, with sets S_A whose tubes stay 2δ from
the axes (radial phases with S_A in an angular band; or non-radial phases such as axisphase5's ellipse phases, where
they have no caustic on Ω). Then every small invariant datum with densities in S_A has its non-round
Einstein–N-null-dust background on the whole Ω. Data (deduced, not computed): the record's outward radial solve
(Proposition 6.5, Lemma 6.3 (a)-(c)) with a small dust source; its hypotheses are open conditions (H > 0, S A0 > 0,
FAMILIES5-FULL §6 S1-S3) and the density data are free, so they stay in S_A, while the metric correction spreads in θ,
which Theorem N allows. The hole then grows by O(ε): this is not the record's growing hole, but it is a large,
non-round background with any number of families — Part II's case "more families, with envelopes vanishing near the
axes".

**Corollary N2 (a shorter domain; deduced, conditional on data).** Let ů be Part I's round two-dust background on Ω₂ and
suppose the data coincide with Part I's on Σ_τ0 ∩ {θ < θ1 or θ > π/2 − θ1} (θ the angle of the orbit quarter plane)
and are within ε of them (any number of extra families supported in the band). For 0 < θ2 < θ1, on Ω₂ ∩ {τ − τ0 <
a(θ1 − θ2)(1 − Cε)} the background exists and equals Part I's on {θ < θ2 or θ > π/2 − θ2}. *Proof.* (A) with χ_A = 1
on {θ2/2 ≤ θ ≤ π/2 − θ2/2}; its characteristic speeds are within g's light cone, whose angular speed is at most
(1 + Cε)/R ≤ (1 + Cε)/a (S7), so by uniqueness on domains of dependence U = ů on the axis neighbourhoods, where (A3)'s
source is ů's own; elsewhere Theorem N's proof. ∎ In the computed example (a = 0.7, Part I §2(f)) the bound is at most
0.7 · π/4 ≈ 0.55 in τ, before the shell (v_start − τ0 = 3.68) reaches the hole. The band-localised constraint data are
not constructed here: the record's radial solve is parabolic in θ (its ρ-equation has ∂_R a against ∂_θ² a, FAMILIES5-
FULL §6 S1) and spreads every perturbation over all angles; a localised gluing in the class with dust would supply them.

**Corollary N3 (large data, short time; deduced).** For any smooth invariant datum whose densities vanish within 2δ of
the axes, (A) has a solution on Ω ∩ {τ ≤ τ0 + T}, T depending on the data (Step 9 and Steps 4-8 on a short interval),
which is an Einstein–N-null-dust solution as long as the tubes stay in {χ_A = 1}.

## 4. The axes: what fails, exactly (computed: `axisloss5.py` X1-X3; deduced)

Near the axis {x3 = x4 = 0} (ρ1 > 0; the origin is outside Ω), in coordinates (τ, ρ1, x3, x4) of the quotient by the free
circle φ1, the general smooth invariant metric is h_AB dX^A dX^B + 2(c_τ dτ + c_1 dρ1)(x·dx) + a|dx|² + b(x·dx)², every
coefficient smooth in (τ, ρ1, s), s = |x|², and an invariant phase is u = U(τ, ρ1, s).

**Proposition X.** (X1 (a), exact) |K2|² = a s and g(∂_ρ2, ∂_ρ2) → a on the axis: elementary flatness is automatic for a
metric smooth in Cartesian form (control: a conical metric, c = 3/2, has g_xx → 1 and 9/4 along the two axes).
(X1 (b), exact) κ2 = g⁻¹(du, dψ2) is smooth across the axis and its axis value is (2/a) U_s + (terms in U_τ, U_ρ1 and the
metric's 1-jet), with U_s = ½ ∂₃²u there, while du on the axis holds no U_s (axisphase5 A1): **on the axis κ2 is a
second derivative of u**, not a function of the 1-jets (control: κ1, of the circle that does not degenerate there,
holds no U_s). (X1 (c), exact) Off the axis κ2 is a function of the 1-jets, with the coefficient of ∂₃u equal to
1/(a ρ2) + O(1). (X1 (d), exact) At (ρ2, 0), ∇²u(e4, e4) = κ2 exactly and ∇²u(∂₃, ∂₃)/g33 − κ2 = (4U_ss/a + ...)
ρ2² + o(ρ2²): the planar anisotropy vanishes to second order, so on the axis θ_h = κ2 and |χ|² = κ1² + ½(θ − κ1)², and
near it, exactly,

    |χ|² = κ1² + ½ (θ − κ1)² + ½ s²,      s := θ_h − κ2   (the planar shear).                                (X)

(X2, mpmath) In the flat model κ2 = ∂_ρ u/ρ. For u_ε = exp(−ρ²/ε²), concentrating at the axis, ‖κ2‖/‖∇u‖ = √2/ε in
L²(R²) (to 12 digits at ε = 0.2, ..., 0.025) and 5.02, 10.01, 20.01, 40.00 in H¹; for the ring u_ε = exp(−(ρ − 1/2)²/
ε²) (control) both ratios stay at 2.00 = 1/ρ0. (X3, exact identity and mpmath) For a planar invariant u, s_pl :=
u_ρρ − u_ρ/ρ = f − 2Af with f the planar Laplacian and Af := ρ⁻² ∫_0^ρ r f dr, and ‖s_pl‖ = ‖f‖ in L²(R²) for both
families (the flat Bochner identity in the plane), ‖Af‖/‖f‖ = 0.7071 at the axis at every ε.

**What this proves, and why the Raychaudhuri transport cannot repair it (deduced from X1-X3, axisphase5 A1).**

1. *The failing estimate.* The order-zero structure of (R) — its right side a smooth function of (θ, p, dg) — holds
   on {dist(·, axes) ≥ δ} with constants growing like δ^(−1−j) at order j (X1 (c)), and fails at the axis: the map
   p ↦ κ2 is not bounded H^m → H^m near the axis (X2), and on the axis κ2 is of the order of ∂p (X1 (b)). In the
   derivative ledger the θ-source becomes order m − 1 there and the loop loses one derivative (augment5 S1 control
   (c)). By (X) the quantity that must be recovered is exactly the planar shear s.
2. *The repair is elliptic and runs across the generators.* At an axis point the family's generator lies in span(∂_τ,
   ∂_ρ1) (axisphase5 A1): it runs along the axis. The flat-model recovery of s (X3) is an integral in ρ2 from the axis,
   transverse to every generator: no transport along P_A supplies it. In curved space it is the Codazzi equation on the
   two-dimensional planar sections of the family's null hypersurfaces, whose right side carries a curvature component
   (β, at the order of ∂²g) and the torsion ζ of the null hypersurface; and the planar trace that the elliptic estimate
   needs differs from the improved θ − κ1 by the tilt of the sections, which brings the transverse second derivatives
   of u (∇²u(N, ·), the torsion again) with coefficients O(ρ2²) (X1 (d)'s remark).
3. *What would close it.* Control of ζ at the improved order — the mass-aspect transport and the Hodge systems on the
   sections of the double-null method — together with the curvature component β, i.e. the renormalised hierarchy that
   [LR20] Theorem 4.6 carries out for two null dusts in four dimensions (read in FAMILIES5.md 4e, D494-D495; "in
   appropriate function spaces which avoid a potential loss of derivative", p. 10 there). Near an axis the class is a
   four-dimensional axisymmetric problem with one more scalar (the free circle's ψ1) and an axis; no such theorem for
   Einstein–scalar–null dust with an axis, or for five-dimensional T²-invariant metrics, is available here. **That is
   the exact obstruction:** not the size of the data, not the black hole, and not the number of families, but the
   elliptic recovery of the planar shear of each family that reaches an axis.
4. *Which families meet it.* Every family whose density is nonzero at an axis — in particular Part I's round ingoing
   and outgoing dusts, for which s ≡ 0 on the round background and is perturbed by any non-round perturbation (the
   metric perturbation reaches the axes at the speed of light, through the constraints at once). Part II's separated
   families with envelopes vanishing near the axes do not meet it (Theorem N, N1).

## 5. Part II's conditions, several families, and Vlasov

**Conditions (i)-(iii) of FAMILIES5-FULL Part II (deduced).** For the backgrounds of N1 (and of N2 on its shorter
domain): (i) holds — the background exists on Ω, and Lemma 1.1 (a)-(f) hold for it by openness (Lemma 1.1(e)), every
generator of every family reaching Σ_τ0 inside Ω by S7's signs (past causal curves cannot leave through R = a, which is
trapped, nor through the outer boundary); (ii) is a hypothesis on the chosen phases, |g⁻¹(du_A, du_B)| ≥ c > 0 on the
overlaps of supports — open, so it holds for the perturbed background if it holds with margin for the seed's phases
(Part II: possible for non-radial phases of different ellipses supported away from the axes; at the axes it fails for
two families of one orientation, axisphase5 A2); (iii) is not settled here: for a non-radial family the transverse
traceless polarisations in the class are diag(α, β, −α − β) in (e_θ, e_φ1, e_φ2) (deduced: the Z2 × Z2 reflections
kill the off-diagonal ones), and S2's constraint cancellation is known only for α = 0 (FAMILIES5-FULL §6 S2, Part II (iii)).
Given (ii)-(iii), Part II's conditional extension of sections 4-6 gives the high-frequency limits of N1's backgrounds;
Part I's background with any non-round perturbation is not reached (section 4).

**Several families.** Any finite number N of non-round families, supported away from the axes, small, on the seed:
background on the whole domain (N1); large, on a short domain (N3). Near Part I's growing hole: only on N2's shorter
domain, and conditionally on localised data. The constants of Theorem N depend on N.

**Vlasov (deduced; standard, not READ).** A non-round massless Vlasov field in the class is restricted (Part III
Proposition V(b)). For f smooth on the cotangent bundle and supported away from p = 0, Einstein–massless Vlasov loses no
derivative (T = ∫ f p ⊗ p takes x-derivatives only from f, whose transport has coefficients ∂g), so a non-round Vlasov
background near the seed exists on Ω by Cauchy stability, axes included: for Vlasov the background is not the
obstruction. The passage to vacuum is: [HL25] approximate the Vlasov field by N families with N → ∞ and constants
"C(N) = c^N N^N" (p. 5, footnote 5, READ in FAMILIES5-FULL Part III), and Theorem N's ε, C are not uniform in N, while
Part II's separation constant c tends to 0 as the families' directions accumulate; families reaching the axes add
section 4's obstruction. So non-round Vlasov limits in the class remain open, now with the background removed from the
list of obstructions near the seed.

## 6. Literature (READ, alphaXiv, 2026-11-02)

- [HL25] C. Huneau, J. Luk, arXiv:2506.21779v1. P. 4: "Due to the globality (in space) of the elliptic estimates for the
  metric components, local existence in the elliptic gauge requires a smallness assumption." Pp. 4-5: "In order for
  this scheme to work, we separately control the null expansion χ_A = □_g u_A. ... we show that while general second
  derivatives of u_A − u_A^0 is only O(λ^0) (with dependence on N), the special combination χ_A − χ_A^0 is better and
  is O(λ^1) (again with dependence on N). ... To obtain this improvement, we use the Raychaudhuri equation that χ_A
  satisfies. In this equation, the main oscillatory terms are O_N(λ), as opposed to O_N(1) in the transport equations
  for the general second derivatives of u_A." P. 22, (6.31): "L_A(χ) + χ² = −R_(L_A L_A) = −(L_A ϕ)² − e^(−4ϕ)(L_A ϖ)²"
  (sub- and superscripts restored from the extraction).
- [HL18] C. Huneau, J. Luk, arXiv:1706.09501v1. P. 3, footnote 5: "we will also view φ as a function φ : I × R³ → R and
  g as a metric on I × R³, which do not depend on the variable x³." P. 4: "(3) Since the reduced equations are in (2 +
  1)-dimensions, the elliptic gauge can be introduced such that the equations for the metric of the reduced system are
  semilinear". P. 9, before Theorem 3.3: "While the theorem requires a smallness assumption (3.17), it is important to
  note that the smallness is not needed for the higher norms." Theorem 3.3 (p. 9): estimates "‖F_A‖_(H^k)", "‖∇u_A −
  c_A‖_(H^k_δ)" and "‖γ̃‖_(H^(k+2)_δ)" for the density, the eikonal and the metric.
- [IT20] M. Ifrim, D. Tataru, *Local well-posedness for quasilinear problems: a primer*, arXiv:2008.05684v2. P. 2: "for
  a solution u ∈ C([0, T]; H^s), small perturbations of the initial data u_0 yield solutions which are also defined in
  [0, T]." P. 3: "Theorem 1. The equation (1.2) is locally well-posed in H^s in the Hadamard sense for s > d/2 + 1."
  P. 4: "Theorem 1 has been first proved by Kato [16]".
- [Tou24] Remark 1.3 and [LR20] Theorem 4.6: as READ in FAMILIES5-FULL Part II and FAMILIES5.md 4e (not re-read).

## 7. What is proved, and what is not

- Class identity (C) and class Raychaudhuri (R): computed, exact, with controls (classchi5 C1-C3); torus Riccati (C4).
- Augmented system off the axes: zero-order sources (augment5 S1), constraint propagation identities (S2-S5), meeting
  roots (S6), speeds and transport signs for every family on Part I's background (S7): computed.
- Theorem N (Cauchy stability, axis-free dust, any N, large background): deduced, at the record's section 4 level, its
  identities computed; local existence from Kato's theorem (READ in [IT20] for the model case). Not verified
  independently.
- Corollary N1 (seed + small non-round families, whole domain): deduced; its data by the record's radial solve,
  deduced from open conditions, not computed.
- Corollary N2 (Part I + band perturbation, shorter domain): deduced, **conditional** on band-localised constraint data,
  not constructed. Corollary N3 (large axis-free data, short time): deduced.
- The axes: the failure of the order-zero structure and its size computed (axisloss5 X1-X2); the elliptic nature of
  the repair computed in a flat model (X3); that the repair needs the double-null torsion/curvature hierarchy deduced.
- **Open:** the non-round background near Part I's growing hole on the whole Ω₂ (for families meeting the axes); the
  band-localised data of N2; Part II's (iii); uniformity in N (Vlasov).

## 8. Proposed text for the paper's section 9, "More families" (≤ 8 lines)

> More families. In the class the null second fundamental form of each family is diag(θ_h, κ1, κ2) with the torus terms
> first order, so off the axes each family's Raychaudhuri equation closes on its expansion and the Einstein–null-dust
> system is well-posed there without smallness: a large background (the seed) carries any finite number of small
> non-round families supported away from the axes on the whole domain. At the axes the degenerate circle's curvature
> becomes a second derivative, and the lost derivative (the planar shear) is recovered only elliptically, across the
> generators, by the double-null hierarchy, known in four dimensions and not here; so non-round perturbations of the
> two-dust background, whose dusts meet the axes, and non-round Vlasov limits (whose dust approximations are not uniform
> in their number) remain open.

## Files

`FAMILIES5-NONROUND.md` (this note); `checks/classchi5.py` (C1-C4, about 15 s), `checks/augment5.py` (S1-S7, under a
minute), `checks/axisloss5.py` (X1-X3, under a minute), `checks/jetpoly5.py` (exact jet arithmetic, J1, seconds), each
with its `.out`.
