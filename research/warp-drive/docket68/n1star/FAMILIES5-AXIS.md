# FAMILIES5-AXIS -- band-localised constraint data, the axes, and Vlasov, in the T² class

Status (2026-11-02, workstream C, round 4). This note takes up the three items FAMILIES5-NONROUND.md left open. It does
not edit the paper, FAMILIES5-FULL.md, N1STAR-PROOF.md or any proof5 Part. FAMILIES5-NONROUND.md is amended only by
dated bracketed amendments, which also seat the independent reader's findings on that note (section 6).

**Verdict.**

1. **The axis closes (deduced; every identity computed).** At an axis the one term of the class Raychaudhuri equation
   that is not first order, the planar shear s, is the trace-free part of the second fundamental form of the family's
   level sets in the slice, plus a term in the slice's extrinsic curvature K. The level sets near an axis are graphs
   over the planar disc, the axis is an interior point of that disc, and their mean curvature is fixed by the
   transported expansion θ. So elliptic regularity recovers s at the same order as θ, using only g and its first
   derivatives (Lemma A). The leaf's equation is a regular Volterra equation from the axis whose coefficients carry first
   derivatives of the metric only (computed: `axisellip5.py` E1). No curvature component and no torsion of the null
   hypersurface enters (E0). This answers the independent reader's question: the curved, non-planar terms are first
   order in the metric, and FAMILIES5-NONROUND's "the double-null hierarchy is needed" does not hold. **Theorem N′**:
   Theorem N holds with dusts reaching the axes, on domains whose lateral boundaries are adapted where they meet an
   axis. **Corollary N′1**: Part I's background carries any small non-round invariant perturbation, and any finite
   number of small extra families, on the whole (adapted) domain Ω₂. This supersedes Corollary N2, and closes the
   near-round, large-data problem posed in FAMILIES5-NONROUND section 1 (deduced; not independently read).
2. **Band-localised data exist; global angular support is not forced (computed, deduced).** Characteristic data: the
   class's cone constraints are ODEs in v at fixed angle (B6), so free data supported in an angular band stay there,
   exactly. Cauchy data: the record's split of the constraints ([Rac16]'s hyperbolic-parabolic one) does spread every
   perturbation to the axes (B5). [Rac16]'s other split, with the Hamiltonian constraint solved algebraically, is
   hyperbolic in R with finite angular speed. In the class its symbol is [Rac16] (4.22) (B1), and it is hyperbolic on
   Part I's seed region (B3) with speed c(R) = √((2 + μ/R²)/3)/R on Tangherlini (B2, cross-checked against [Rac16]
   (4.30) in four dimensions). So nonlinear data supported in a band widened by Δ = ∫c dR exist (Proposition L): 0.213
   rad for a perturbation within 0.2 of R = a in the example. At the linear level there are data compactly supported in
   R and θ on every round slice that are not pure gauge (B4).
3. **Vlasov (computed, deduced).** In the class a Burnett-type Vlasov field is restricted to p_φ = 0, and on that set
   the Vlasov equation is the orbit space's (V1). At an axis, smoothness of the stress forces the radial planar flux to
   vanish like ρ₂² (V2). So a restricted density continuous in momentum vanishes at the axes, and one that does not
   vanish there concentrates onto the axial directions, which are Part I's two radial dusts (V3). Einstein–restricted
   Vlasov in the class is then well-posed around large solutions (deduced: Vlasov theory away from the axes, Theorem N′
   for the dusts at them). **The background is not the obstruction, axes included.** What remains is the
   high-frequency approximation: N families have least mixed symbol 1 − cos(2π/N) ~ 2π²/N² (V4), and [HL25]'s
   constants grow like c^N N^N (READ).

[R5 2026-11-06 (FAMILIES5-VLASOV.md, round 5; with the verifier of round 4, whose findings are seated below as
"[R5 verifier of round 4]"). Item 3's last two sentences are withdrawn. For Vlasov the axes are an obstruction unless
the non-axial field stays off them, and a smooth solution's field does: restricted particles that reach an axis focus
there with density ~ 1/ρ2 (FAMILIES5-VLASOV Proposition Ax, vlasovhf5 H7; the verifier's MAJOR 1). N-dependence is not
the obstruction: Vlasov limits in the class are proved along a diagonal (FAMILIES5-VLASOV Theorem V), the background
step uniform in N, the high-frequency step made coherent by hierarchical frequencies, as in [HL25]. Item 2's band data
hold on the whole slice except a band inside the shell, where no foliation is hyperbolic (racglobal5 R1-R2).]

Labels as in the record: **computed** (a program `checks/<name>5.py` with a `.out` and a negative control that it must
reject), **deduced** (argued here), **READ** (verbatim, identifier and page, read at source through alphaXiv,
2026-11-02). New programs: `checks/bandconst5.py` (B1-B6), `checks/axisellip5.py` (E0-E2), `checks/vlasov5.py`
(V1-V4), each with its `.out`, all PASS. Repaired after the independent reader (section 6): `checks/augment5.py` (S3,
S5, S7 controls) and `checks/axisloss5.py` (X3 asserted, with a control), `.out` regenerated, PASS.

---

## 1. What was open

FAMILIES5-NONROUND.md proved Theorem N (Cauchy stability of class Einstein–N-null-dust solutions whose dusts avoid
the axes; deduced, identities computed) and located the obstruction at the axes. There the degenerate circle's
curvature κ2 = g⁻¹(du, dψ2) becomes a second derivative of u, and the planar shear s := θ_h − κ2 enters the
Raychaudhuri source through

    |χ|² = κ1² + ½ (θ − κ1)² + ½ s²                                                          (X)

(`axisloss5.py` X1 (e), exact). It recovered s elliptically in a flat model, s = f − 2Af, f the planar Laplacian, and
then asserted that the curved recovery needs the double-null Codazzi hierarchy, "available in four dimensions ([LR20])
and not here". The independent reader (2026-11-02; section 6) observed that the flat recovery loses nothing: Af = u′/ρ
= κ2 is the dilation average ∫₀¹ t f(t·) dt, bounded on every Ḣ^k. Any real loss would have to sit in the curved,
non-planar terms, which the note asserted but did not compute. Section 3 computes them.

## 2. Task 1: band-localised constraint data

### 2.1 Characteristic data: exact localisation (computed: `bandconst5.py` B6)

In the class's double-null gauge (`dnull5.py`: g5 = −2Ω²(du dv + dv du) + γ(dθ − b du)² + e^(2A) dφ1² + e^(2B) dφ2²,
every function of (u, v, θ)), on an outgoing cone u = u0:

- Ric(∂_v, ∂_v) has no θ-derivative and no u-derivative. It is the class Raychaudhuri constraint, an ODE in v at each θ
  (dnull5 D2).
- Ric(∂_v, ∂_θ) contains the shift only through ∂_v b and ∂_v² b, and no u-derivative. It is an ODE in v for ∂_v b, with
  sources that are θ-derivatives of fields already fixed on the cone.
- Control (rejected): Ric(∂_θ, ∂_θ) contains u-derivatives, so it is not a constraint on the cone.

So free characteristic data (the sections' conformal class, A − B and the shape of γ, and the dust densities on the cone)
supported in an angular band, with the corner sphere unperturbed, determine cone data that equal the background's
outside the band, exactly. This uses no smallness and no hyperbolicity condition (deduced from B6 and dnull5 D5; the
characteristic initial value problem itself, [Wu26] Theorem 2.1, is READ in the record).

### 2.2 Cauchy data: the two splits of [Rac16]

[Rac16] splits the constraints with respect to a foliation of the slice by the spheres S_R. In the variables (N̂, N̂ⁱ,
γ̂; κ, k_i, K^l_l, K̊) it shows that the momentum constraint is a first-order system with R as time. **Hyperbolic-
parabolic split (the record's):** the Hamiltonian constraint solved for the lapse N̂ "possess[es] the form of a
parabolic partial differential equation" ([Rac16] p. 4). This is the record's radial solve (N1STAR-PROOF.md 6.3;
twoslice5 S1: "the parabolic structure belongs to Racz's parametrisation, not to the slice").

- **It spreads (computed: B5).** The linearised equation of twoslice5 S1, (3/(RG²)) ∂_R a − (1/(GR²)) Δ_θ a = 0 with
  Δ_θ the S³ Laplacian on invariant functions, takes data supported in θ ∈ [π/8, 3π/8] at R = r1. After ΔR = 0.01,
  0.05 and 0.2 the solution is 4.0 × 10⁻⁹, 5.4 × 10⁻⁴ and 7.8 × 10⁻² at both axes (max 0.41). Control (rejected): the
  same march without the angular operator leaves the axes exactly 0.
- **The weakest decay there (deduced).** The solution is positive at every angle after any step (strong maximum
  principle), with heat-kernel tails of order exp(−d²·3R/(4G ΔR)) at angular distance d. So this split forces global
  angular support, with Gaussian decay, and nothing better.

**Algebraic-hyperbolic split.** [Rac16] (4.17) solves the Hamiltonian constraint algebraically for κ. With κ and
its angular derivatives eliminated, "a Friedrichs symmetrizable hyperbolic system can be deduced" (p. 7), and "Lemma
4.1 Assume that κ · K^l_l < 0 holds in a subset of Σ. Then equations (4.16) and (3.2) comprise a first order
symmetrizable hyperbolic system there" (p. 12). Its characteristic polynomial is "K^l_l (n̂ⁱξ_i)² − 2 (n̂ⁱξ_i)
(γ̂^KL k_K ξ_L) + κ (γ̂^KL ξ_K ξ_L) = 0 (4.22)" (p. 13), and Theorem 4.3 (p. 14) gives a unique smooth solution, the
constraints holding "in the domain of dependence of S_ρ0 in Σ". The free data are "N̂, N̂ⁱ, γ̂_ij; K̊_ij; e, p_i
(4.28)" (p. 14). In the class:

- **B1 (exact: the symbol symbolic, compared at three rational points with every function explicit).** With K_RR =
  Gκ, K_Rθ = √G p, K_θθ = R²(Kt/3 + s1), K_φ1φ1 = G1(Kt/3 + s2), K_φ2φ2 = G2(Kt/3 − s1 − s2) on γ = G dR² + R² dΩ₃²:
  - H is linear in κ with coefficient 2Kt.
  - After κ is eliminated, det of the principal symbol of (M_R, M_θ) in (Kt, p) equals (4.22) times a ξ-independent
    factor (245/156, 91/43, 7735/2973 at the three points).
  - At p = 0 the angular speeds are dθ/dR = ±√G √(−κ/(Kt R²)).
  - Control (rejected): with κ not eliminated the ratio depends on ξ.
- **B2 (exact).** On Part I's chart g0 = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃² with slice τ = v̂ − R and E := e^ψ:
  - Kt = 3(Ef − 1)/(ER√(2/E − f)), negative wherever Ef < 1 (K = ∇n).
  - κ = −N_k/(E√(2/E − f)(2 − Ef)), with N_k := E²f²ψ_R + ½E²f f_R − 3Efψ_R − ½E f_v − (3/2)E f_R − ψ_v + ψ_R.
  - Hence the split is hyperbolic (κ Kt < 0) exactly where N_k < 0.
  - On Tangherlini N_k = (μ/R³)(f − 3) < 0, with angular speed c(R) = √((2 + μ/R²)/3)/R.
  - Cross-check against a READ formula: the same code in four dimensions gives −K^l_l/κ = 2(1 + 2H)/(1 + H), H = M/r,
    which is [Rac16] (4.30), p. 14.
  - Control (rejected): the four-dimensional code with the trace factor 3 does not give (4.30).
- **B3 (computed, floating point; the record's background, `twobg5.py`, at n = 40 and 80).** On Part I's Σ_τ0 in the
  seed region a ≤ R ≤ r1 = 1.861 (region III: ψ = ψ_III(v̂) ∈ [−0.255, −0.155], |ψ′| ≤ 0.117):
  - max N_k = −0.318 < 0 at both resolutions, so the split is hyperbolic on the whole seed region;
  - c(a) = 1.270 and c(r1) = 0.375;
  - the spread is 0.213 rad from R = a + 0.2 down to a, and 0.752 rad over all of [a, r1], converged to 0.02.

**Proposition L (band-localised nonlinear Cauchy data; deduced from [Rac16] Lemma 4.1 and Theorem 4.3 (READ), with B1
and B3).** Let a < R2 ≤ r1 and 0 < θ1 < π/4. Take invariant free data (4.28) equal to Part I's outside a compact
subset of {a < R < R2, θ1 < θ < π/2 − θ1}, ε-close to them in C^∞. These may include any number of extra dust
families supported there: e and p_i are free. Take (k_i, K^l_l) at R = R2 equal to Part I's. Then for ε small the
system (4.16), (3.2) has a unique solution on [a, R2]. The resulting (γ, K), extended by Part I's data for R ≥ R2,
satisfy the constraints on Σ_τ0. They coincide with Part I's outside {a ≤ R ≤ R2, θ1 − Δ(R) ≤ θ ≤ π/2 − θ1 + Δ(R)}, with
Δ(R) = ∫_R^R2 c dR′ + O(ε).

*Proof.* On [a, R2] × S³ the background solves the system, and the system is symmetrisable hyperbolic there (B3:
N_k < 0). A smooth perturbation of the data of a symmetrisable hyperbolic system on a compact time interval has a
solution on the same interval for ε small (Cauchy stability; standard, not READ), and invariance follows by uniqueness.
The S_R are 3-spheres, so the axes are interior points of the leaves and regularity there is automatic. The support
statement is finite propagation speed in the domain of dependence ([Rac16] Theorem 4.3), with speeds within O(ε) of
B1's. ∎

[R5 verifier of round 4 (minor 4), re-derived. [Rac16] Theorem 4.3 is explicitly "(local)", for a "sufficiently small
neighborhood of S_ρ0" (READ p. 14); its locality concerns existence only, the constraints holding identically for any
solution of the system (READ p. 12). Existence on all of [a, R2] near the background is FAMILIES5-VLASOV Theorem K's
Cauchy stability (proved there), the background solving the system on the interval. B1's real speeds are the θ-only
symbol's; the full S³ system needs κ K^l_l < 0; B2's equivalence needs E f < 1, which Part I satisfies (bandconst5
docstring corrected).]

In the example, R2 = a + 0.2 gives Δ ≤ 0.213: a band θ ∈ [π/8, 3π/8] widens to [0.18, 1.39], away from both axes. A
radially long perturbation spreads more: 0.752 rad across the seed region.

### 2.3 Compact support in R and θ, linearised (computed: B4)

On every round slice (γ = G dR² + R² dΩ₃², K0 = κ0 n̂n̂ + Y0 R² dΩ₃², with G, κ0, Y0 arbitrary), take dγ = 0, a stream
function ψ(R, θ) of compact support, a(R) = −3/R − κ0/(R Y0) (computed), and

    dKt = e^(∫a) (sin θ cos θ)⁻¹ ∂_θψ,    dp = R² e^(∫a) (√G sin θ cos θ)⁻¹ ∂_Rψ,    ds1 = 0,

with ds2 fixed algebraically by M_θ. Its coefficient is −1/(sin θ cos θ): −25/12, −169/60 and −289/120 at the three
points. The linearised H, M_R and M_θ then vanish (exact at three rational points with explicit G, κ0, Y0 and ψ; the
construction symbolic). Every field is a local differential expression in ψ, so the data are supported in supp ψ: compact
in R and θ, anywhere on the slice, the packet region included.

- **Not pure gauge (exact).** A gauge perturbation of a round slice with dγ = 0 has X^θ = 0 and (L_Xγ)_Rθ = −R G Y0 ∂_θN,
  so N = N(R) and its dK is θ-independent; the stream perturbation is not.
- **Controls (rejected).** ds2 = 0 leaves M_θ, and dropping the weight sin θ cos θ leaves M_R.

The nonlinear version with exact compact support would need a correction of the quadratic error, which has one
integral charge (the weighted θ-moment of M_R). That correction is not constructed here.

[R5 (FAMILIES5-VLASOV section 4). [CS06] Theorem 2 and [CD03] Theorem 5.6 (READ) construct the correction up to the
invariant KIDs; in Part I's vacuum regions the only one is the static Killing field (racglobal5 R3), so the charge is
one number. On the stream-function seeds it is negative (R4: 45 seeds), so these seeds do not complete to exactly
localised vacuum data, with or without dust added in the band. Exact compact support is not obtained; band
localisation (Proposition L) and exact localisation on cones (B6) are what is proved.]

### 2.4 What this does to Corollary N2

N2's domain argument survives with θ1 replaced by θ1 − Δ (deduced). N2's input is supplied: by Proposition L near
R = a, and characteristically by 2.1. **N2 is in any case superseded by Corollary N′1 (section 3),** which needs no band
localisation, so any small invariant constraint solution serves as data: Proposition L's, B4's linear data once
corrected, or the record's parabolic solve with a small non-round source. Proposition L also answers the independent
reader's MAJOR 2 for perturbations in the seed region. It is a construction near the seed, its axis regularity
automatic (the leaves are 3-spheres), with a small non-round dust source allowed as free data. Elsewhere on Σ_τ0
hyperbolicity (N_k < 0) has not been checked. B2's formula shows that a strong ingoing flux (the −½E f_v = μ′/(2R²)
term) can break it in the shell region.

[R5 (racglobal5 R1-R2). Checked on the whole slice: hyperbolic except on R ∈ [4.30, 4.53] inside the shell (max N_k =
1.79 × 10⁻³, converged at n = 40, 80, 160), where the flux exceeds 2μ(2 + μ/R²)/R; there K is negative definite and no
foliation is hyperbolic. Proposition L holds for perturbations whose radial support avoids the band; data meeting it
are posed on the cone N (B6). Nit (the verifier of round 4): B6's "no smallness" concerns the localisation, not the
existence of cone data.]

## 3. Task 2: the axis

### 3.1 The slice picture (computed: `axisellip5.py` E0)

Let Σ_τ be a slice with future unit normal n and second fundamental form K(X, Y) = g(∇_X n, Y), and M3 := Σ_τ ∩ {φ1 =
0}. M3 is totally geodesic, the fixed set of φ1 ↦ −φ1, and contains ∇_Σ u for an invariant u. For a family's phase u
the section S_c = {u = c} ∩ Σ_τ of its null hypersurface is transverse to the generator. Near axis 2 its planar part
is the leaf Σ2 := S_c ∩ M3, a surface of revolution about the axis. Exact at rational jets of classchi5's class
metrics (three seeds):

    hess_g(u)(X, Y) = hess_M3(u)(X, Y) − n(u) K(X, Y)      for X, Y tangent to M3,          (G)

and for a null u the trace of hess_g(u) over TΣ2 is □u − κ1. So, with k̸ := hess_M3(u)/|∇_M3 u| on TΣ2 (the leaf's
second fundamental form in M3) and K̸ := K on TΣ2,

    χ̸ = |∇u| k̸ − n(u) K̸,    tr χ̸ = θ − κ1,    s = |∇u| (k_r − k_φ) − n(u) (K_rr − K_φφ).

The second fundamental form of the null hypersurface restricted to the plane is the leaf's, plus the slice's K. K is
first order in g. Neither a curvature component nor the torsion of the null hypersurface appears; both entered
FAMILIES5-NONROUND's version only because it used the null hypersurface's own Codazzi equation. Controls (rejected):
(G) without the K term, and the trace over the coordinate plane span(∂_y1, ∂_φ2) in place of TΣ2 (the tilt of
NONROUND X1 (d)).

[R5 verifier of round 4 (minor 7 and a nit), re-derived. (G) is the Gauss formula and holds for any u; tr χ̸ = θ − κ1
needs u null to first order. E0 alone does not exclude curvature terms: they drop out because on a surface of
revolution k_φ = ν(log √g_φφ), the Killing identity (as in Proposition C), so the recovery never uses Codazzi or
Ric_M3. In "K_rr − K_φφ" the r-direction is the leaf's tangent in the meridional plane, not ∂_r.]

### 3.2 The leaf's equation at the axis (computed: E1)

Near the axis every smooth invariant metric on M3 is γ3 = A dz² + 2C r dz dr + (B + D r²) dr² + B r² dφ², with A, B, C,
D functions of (z, r²), z along the axis and r the distance from it. By A1 of axisphase5, ∇u is along ∂_z on the axis,
so near it each leaf is a graph z = h(r), h a smooth function of r². With F = z − h and k = hess(F)/|∇F|:

- (a) H2 := k_r + k_φ is linear in h″ with coefficient a, and E := r H2/a − (r h′)′ contains no h″ (exact, sympy). E and
  k_φ contain derivatives of A, B, C, D of first order only (read off the expressions). The reader sees second
  derivatives when they are there: a Ricci component of γ3 (control).
- (b) On three random polynomial instances (rational coefficients), E/r and k_φ settle to finite values at the axis:
  E/r → 0.25243, 0.36883, 0.25400 and k_φ → −0.56153, 0.71160, 0.05412 (50-digit evaluation at r = 10⁻⁴, …, 10⁻⁸,
  settled to 10⁻¹²). Control (rejected): the non-smooth cross term C dz dr (for C r dz dr) makes k_φ grow like 1/r,
  −2.7 × 10⁷, −1.6 × 10⁷, −8.9 × 10⁶ at r = 10⁻⁸.

Hence the leaf obeys the regular Volterra equation

    r h′(r) = ∫₀^r (ρ H2/a − E) dρ,       σ := (k_r − k_φ)/2 = H2/2 − k_φ[h, h′],                  (V)

and the map H2 ↦ σ involves γ3 and its first derivatives only. In the flat case (V) is X3's s = f − 2Af: the reader's
dilation average. The 1/r of κ2 (NONROUND X1 (c)) is absorbed by the integral from the axis, which is where the
first-order route failed (X2).

### 3.3 Lemma A, and the estimate (deduced; identities E0-E1; numerics E2)

**Lemma A (the planar shear at an axis).** Let g be a smooth class metric and u an invariant phase with g⁻¹(du, du)
= 0 and du ≠ 0, near a point of axis 2 where ρ1 ≥ c0 > 0. On Σ_τ let D_δ := {ρ2 < δ}. Fix m ≥ 5. There is C,
depending on δ, on lower bounds for |∇_Σ u| and |∂_z u| on D_2δ, and on C² norms of (g, u), such that

    ‖s‖_(H^m(D_δ)) + ‖χ̸ − ½(tr χ̸) γ̸‖_(H^m(D_δ)) ≤ C (‖θ‖_(H^m(D_2δ)) + ‖dg‖_(H^m(D_2δ)) + ‖du‖_(H^m(D_2δ)) + 1),

H^m in all directions (along the axis, planar, and in τ through the equations). On the axis s = 0 and κ2 = (θ − κ1)/2.

*Proof.*
1. By (G), H2 = (θ − κ1 + n(u) tr K̸)/|∇u|, which is in H^m(D_2δ) whenever θ, dg and du are.
2. In Cartesian coordinates (z, x3, x4) of M3 the leaf is the graph z = h(x3, x4). The leaf solves the prescribed mean
   curvature equation a^ij(x, h, ∂h) ∂_ij h + b(x, h, ∂h) = H2. Here a^ij, built from γ3(h(x), x) and ∂h, is uniformly
   elliptic on the whole disc: the axis is an interior point, which is the point E1 (b) checks in polar form. And b
   contains ∂γ3 only (E1 (a)).
3. Interior elliptic regularity for quasilinear second-order equations in two variables (standard; not READ) gives
   ‖h‖_(H^(m+2)(D_δ)) ≤ C(‖H2‖_(H^m(D_2δ)) + ‖γ3‖_(H^(m+1)) + 1).
4. Derivatives across the leaves (in c = u) and in τ follow by differentiating the equation in c and τ. Each
   derivative gives the same elliptic equation for ∂_c h with a source one order lower; the coefficients are again
   first order in γ3, and ∂_c H2 = ∂_z H2 ∂_c h. The change of variables (z, x) ↔ (c, x) has Jacobian 1/∂_z u ∈ H^m.
5. Then k̸ ∈ H^m, and s by (G). On the axis s = 0 (NONROUND X1 (d)), so κ2 = θ_h = (θ − κ1)/2 there. ∎

(V) is the radial form of step 3. It shows the bound directly in the radial variable, with Hardy-type averages whose
norms the reader computed (Af = κ2 bounded on every Ḣ^k).

[R5 verifier of round 4 (minor 5, minor 6, nits), re-derived. Lemma A's constant as stated is circular (C² of u contains
s); it depends on C¹ of u and L^∞ of θ (h′ from H2 by (V)), and FAMILIES5-VLASOV Lemma A′ states it in the two forms
Theorem N′ uses, with Lemma E (interior regularity in two variables) proved there. ‖χ̸ − ½(tr χ̸)γ̸‖ = |s|/√2 is
counted once. Lemma A's m ≥ 5 is used within Theorem N's m ≥ 6. E2's ratios are frozen-coefficient limits (0.2886 =
1/(2√3) is the flat Gaussian value), showing no loss at m = 0, 1 only; the reconstruction now starts from axis
regularity, h′(r0) = 0, and recovers h′ to 4.1 × 10⁻¹¹ and σ to 8.0 × 10⁻¹⁰ (axisellip5 rerun).]

**E2 (computed, scipy; a curved metric: A, B, C, D non-constant, the background leaf z = 0 of O(1) mean curvature).**
- Leaves concentrating at the axis, h_ε = ε² exp(−r²/ε²), ε = 0.2, 0.1, 0.05, 0.025, are measured against the
  background leaf, on r < 1/2 with weight r dr.
  - ‖δσ‖/‖δH2‖ = 0.49713, 0.49928, 0.49982, 0.49996 tends to the flat value 1/2.
  - ‖∂_r δσ‖/‖∂_r δH2‖ = 0.28615, 0.28813, 0.28854, 0.28864 is bounded and converged.
  - Control: the first-order route ‖δk_φ‖/‖h′‖ = 7.07, 14.14, 28.28, 56.57 grows like 1/ε (X2's loss, curvature present).
- Integrating the leaf's equation from the axis with H2 given recovers h′ to 8.9 × 10⁻¹⁵ and σ to 1.8 × 10⁻¹³.
  Control (rejected): the flat equation h″ + h′/r = H2 misses them by 0.146 and 2.91.

### 3.4 Theorem N′ (deduced; identities computed in classchi5, augment5, axisloss5, axisellip5)

**Theorem N′.** The statement of Theorem N (FAMILIES5-NONROUND section 3) holds with (H2) replaced by:

- (H2′) where a lateral boundary component B of Ω meets an axis, the dust tubes meeting a neighbourhood of that point
  belong to one family A, and there B ∩ Σ_τ is a leaf {u_A = const} of that family (B adapted).

The dusts may reach the axes; the lateral boundaries depend on the solution through u_A and stay spacelike with Ω to
their past (open conditions). No smallness of ů or of the families is assumed; ε and C depend on ů, Ω, N and the
constants of Lemma A.

*Proof: the changes to Theorem N's proof.*

- *Step 6, near an axis.* Write family A's Raychaudhuri source by (X) as

      S_A^ax := −κ_A1² − ½(θ_A − κ_A1)² − |χ̸̂_A|²[θ_A] − Σ_B q_B g⁻¹(p_A, p_B)².

  Here |χ̸̂_A|²[θ_A] is computed from the leaves of u_A with H2 := H2[θ_A] (step 1 of Lemma A, θ_A for θ) through (V),
  with the coefficients a and E evaluated on the leaves of u_A. A partition of unity in the slice joins S_A^ax to the
  off-axis S_A of Theorem N, so no cut-off χ_A is needed. Lemma A gives ‖∂^α(S_A^ax(U) − S_A^ax(ů))‖ ≤ C N_m,
  |α| ≤ m. By (H2′) the leaves used at points of Ω lie in Ω: a leaf of the family meeting an adapted boundary does not
  cross it.
- *Step 9.* The augmented system's source is now non-local in the planar directions, an integral from the axis along
  each leaf, but locally Lipschitz on H^m (Lemma A applied to differences). Kato's iteration for symmetric hyperbolic
  systems with Lipschitz zero-order sources then applies (deduced; [IT20] Theorem 1 is READ for local sources only).
  The extension to R⁴ keeps P_A^τ > 0 by a cut-off on p_A, as the record's on w (the independent reader's point on
  Theorem N, which applies here too).
- *Step 10.* (V) is uniquely solvable, so on a solution with θ_A = □u_A it returns the true leaf, hence the true
  χ̸̂. So d_A := θ_A − □u_A obeys P_A(d_A) = −d_A(…) − (|χ̸̂_A|²[θ_A] − |χ̸̂_A|²[□u_A]) + (δ*W)(P_A, P_A). The middle
  term is a bounded L² → L² operator applied to d_A (the Volterra map of (V) is a Hardy average). With zero data the
  energy of (W, d_A) obeys a linear Gronwall inequality, as before, so d_A = 0. ∎

[R5 verifier of round 4 (minors 1-2), re-derived. *Step 6.* "No cut-off is needed" holds for family A at its adapted
boundary only: the leaves of another family B can cross that boundary at O(ε). So χ_B = 0 near the boundary–axis points
for B ≠ A ((H2′) puts no B-dust there), and Step 10's d_B energy is taken on a leaf-saturated set inside {χ_B = 1}.
*Step 9.* Lemma A is an inhomogeneous bound, not a difference estimate; Kato's iteration needs (K1) boundedness on H^m
balls and (K2) L²-Lipschitz continuity there, which Lemma A′ (b) gives, and FAMILIES5-VLASOV Theorem K (proved there)
is the iteration with a non-local source. [IT20] Theorem 1 is READ for ∂_t u = A^j(u)∂_j u with no source (corrected
from "local sources"). On the extension to R⁴ the source is χ_A S^ax, and near an axis the leaves are defined by u_A's
values on the axis (transported along it, the generator being along the axis there, axisphase5 A1) and by (V) from
θ_A, so p_A need not be closed for them to exist. Nit: (H2′) is vacuous where no dust meets a boundary–axis point.]

**Corollary N′1 (Part I with non-round perturbations, on the whole domain; deduced).** Let ů be Part I's round
two-dust background on Ω₂ (FAMILIES5-FULL section 2). Replace Ω₂'s lateral boundaries by adapted ones:

- *Inner:* {v̂_ε − τ = a}, a leaf of the ingoing family in each slice. The outgoing packet never comes near: its inner
  edge stays at R ≥ R_H + 0.61 on every column (twobg5 G5, computed in the record), and R_H ≥ √μ0 = 0.907 > a = 0.7.
- *Outer:* {u_ε = U_b(τ)}, U_b(τ) the background's outgoing phase on R = b(τ), a leaf of the outgoing family. The shell
  is absent there: on the record's outer boundary v̂ = V + 1 + τ_end − τ ≥ V + 1 > v_end (N1STAR-PROOF.md (1.1);
  deduced).

For the background both boundaries are the record's spheres, and they stay spacelike for small ε. Then every invariant
datum on Σ_τ0 within ε of Part I's, satisfying the constraints and the gauge condition, has its Einstein–N-null-dust
background on the whole adapted domain, within Cε of ů. The datum may be non-round, and may carry any finite number of
extra small families whose tubes avoid the lateral boundaries near the axes. This supersedes Corollary N2 and the
corresponding item of FAMILIES5-NONROUND section 7. Data: section 2 (Proposition L), or any small invariant constraint
solution.

[R5 verifier of round 4 (minor 3), re-derived. (H2′) needs support conditions on the background families near the
boundary–axis points: an ε-small shell density reaching the outer boundary near an axis, or packet density near the
inner one, violates it. Add supp F_shell ⊂ {v̂ ≤ v_end + η} near the outer boundary's axis points and the packet's
support in R ≥ R_H + 0.6 near the inner one. "R_H ≥ √μ0" is marginal (twobg5: μ_III ≥ 0.82207 against μ0 = 0.82211):
R_H ≥ 0.906.]

**What this does not give.** The high-frequency construction for non-round backgrounds still needs FAMILIES5-FULL Part
II's (ii) and (iii). (ii), angular separation, fails at an axis for two families of one orientation (axisphase5 A2), so
beyond one ingoing and one outgoing family the extra families must vanish near the axes. (iii), the constraint
cancellation for the second polarisation, is not examined.

### 3.5 Status of section 3

- E0, E1 (a): exact. E1 (b): 50-digit evaluation of exact expressions. E2: floating point (scipy).
- Lemma A: deduced, from standard elliptic regularity (not READ) and E0-E1.
- Theorem N′ and Corollary N′1: deduced, at the record's section 4 level. Not independently read.
- The one new analytic ingredient is Step 9's Kato iteration with a non-local Lipschitz source. It is standard in form,
  but its statement for non-local sources is not READ.

[R5. Proved in the needed version: FAMILIES5-VLASOV Theorem K (the iteration computed in a model, katonl5). The
verifier of round 4 adds that Step 9 also needed Lemma A step 4's uniform-in-leaf mixed norms, the solution-dependent
domain, and the leaves' definition before p_A is closed; these are Lemma A′ and the Step 9 amendment above.]

## 4. Task 3: Vlasov in the class (computed: `vlasov5.py` V1-V4; deduced)

- **V1 (exact).** Off the axes, g = h + Σ e^(2ψ_i) dφ_i², with geodesic Hamiltonian
  ½(h^ab p_a p_b + Σ e^(−2ψ_i) p_φi²).
  - p_φi is conserved.
  - On {p_φ = 0}, Hamilton's equations are h's null geodesic flow. So the restricted measures, to which every Burnett
    limit in the class belongs (FAMILIES5-FULL Part III V(b)), form an invariant set, on which Vlasov's equation is
    the 2+1 orbit space's, and T_φiφi = 0.
  - Control (rejected): off the set, −½ p_φ² ∂_a e^(−2ψ) appears in ṗ_a.
- **V2 (exact).** The general smooth planar block of a symmetric 2-tensor invariant under the rotation about axis 2 and
  the reflections (degree ≤ 4, solved) is A(s)δ_ij + B(s)x_ix_j. So T_φφ = A and T_ρρ = A + sB, and T_φφ = 0 forces
  T_ρρ = O(ρ2²). Control (rejected): the non-smooth x̂ ⊗ x̂ of a radial dust through the axis has T_ρρ → 1.
- **V3 (mpmath).** For a restricted density f(ρ2, α) ≥ 0, α the momentum's angle with the axis in the meridional
  plane, T_ρρ = (2π)⁻¹ ∫ f sin²α dα.
  - A density continuous in α with f(0, ·) = 1 gives T_ρρ(0) = 1/2: not O(ρ2²), so not smooth (control).
  - A density concentrating on the axial directions with fixed total density, f = ρ2⁻¹(e^(−α²/ρ2²) + e^(−(|α|−π)²/ρ2²)),
    gives T_ρρ/ρ2² → 1/(2√π) at second order (0.27653, 0.28069, 0.28174, 0.28201), with ∂_α f unbounded.
  - So at an axis a restricted field with smooth stress is either zero or, in the limit, two radial dusts along the
    axis (Part I's). A density smooth in (x, α) vanishes there.
- **V4 (exact).** N restricted families with orbit-space directions 2πk/N have least mixed symbol |g⁻¹(du_A, du_B)| =
  1 − cos(2π/N) (unit energies, flat orbit space): 2, 1.5, 1, 0.293, 0.0761, 0.0192, 0.00482 for N = 2, 3, 4, 8, 16,
  32, 64, and N²(1 − cos(2π/N)) → 2π². N = 2 is Part I's in/out pair, with −2 (axisphase5 A4).

**Where well-posedness stands (deduced).**

- *Unrestricted.* For f smooth on the five-dimensional mass shell, supported away from p = 0 and invariant, Einstein–
  massless Vlasov is the general system: large-data well-posed, axes included (standard, not READ; FAMILIES5-NONROUND
  section 5). Its limits are not Burnett limits in the class (V(a)).
- *Restricted.* Write f = f_s + (two radial dusts at the axes), where f_s is smooth in (x, α) on the orbit space's null
  bundle and vanishes near the axes (V2-V3). Then Einstein–restricted-Vlasov–dust in the class is Vlasov's count away
  from the axes (no loss: T's derivatives fall on f_s, whose transport has coefficients ∂h) joined to Theorem N′ for
  the dusts. Cauchy stability around large solutions follows (deduced, by Theorem N′'s argument with f_s's transport
  added).

So the background is not the obstruction, now with the axes included. **The obstruction is the high-frequency
approximation's dependence on N.** [HL25]'s route approximates the Vlasov field by N families, with constants "C(N) =
c^N N^N" (READ in FAMILIES5-FULL Part III), and Part II's division costs 1/(1 − cos(2π/N)) ~ N²/(2π²) per stage (V4).
Touati's existence is "not uniform in |A|" ([Tou24] p. 4, READ). A construction uniform in N is not available, in the
class or elsewhere.

[R5 verifier of round 4 (MAJOR 1), re-derived (vlasovhf5 H7). V2-V3 show the non-axial density vanishes on the axis,
not near it, and say nothing about propagation; restricted momenta at a nonzero orbit-plane angle reach the axis and
converge cylindrically, with stress ~ 1/ρ2 in the non-smooth x̂ ⊗ x̂ form. "Axes included" is withdrawn for Vlasov: the
restricted system is well posed around large solutions whose non-axial support stays off the axes on Ω (a property of
every smooth solution, FAMILIES5-VLASOV Proposition Ax). The last paragraph is superseded: uniformity in N is not
needed (FAMILIES5-VLASOV Theorem V, the diagonal of [HL25] p. 19, READ), and the obstruction to the every-order scheme
is resonance among three or more phases, removed by hierarchical frequencies (Lemma C).]

## 5. Literature (READ, alphaXiv, 2026-11-02)

- [Rac16] I. Rácz, *Constraints as evolutionary systems*, arXiv:1508.01810v3 (READ in the record for its section 4.1).
  - P. 4: "the Hamiltonian constraint can also be solved algebraically for one of the components of K_ij. By
    eliminating this component, along with its derivatives tangent to the foliating surfaces, the momentum constraint,
    under suitable conditions, maintains its hyperbolic character."
  - P. 12: "Lemma 4.1 Assume that κ · K^l_l < 0 holds in a subset of Σ. Then equations (4.16) and (3.2) comprise a
    first order symmetrizable hyperbolic system there."
  - P. 13: (4.22), quoted in section 2.2.
  - P. 14, Theorem 4.3: "The fields h_ij and K_ij which can be built up from the solution to (4.16), (3.2) and (4.17)
    and from the freely specifiable part of the data do satisfy the full constraint system (1.1)-(1.2) in the domain of
    dependence of S_ρ0 in Σ."
  - P. 14, (4.30): "− K^l_l/κ ≈ 2(1 + 2H)/(1 + H)" on Kerr–Schild slices of near-Schwarzschild data.
  - Indices and fractions are restored from the extraction.
- [HL18] C. Huneau, J. Luk, arXiv:1706.09501v1. Theorem 3.3, p. 9: "Given a free initial data set as in Definition 3.2
  such that ‖φ̇‖_(L∞) + ‖∇φ‖_(L∞) + max_A ‖F̆_A‖_(L∞) ≤ ε, (3.17)". The smallness includes the dust's, which corrects
  FAMILIES5-NONROUND line 94 (the independent reader's finding, read at source here).
- [HL25], [Tou24], [IT20], [Wu26]: as READ in FAMILIES5-FULL, FAMILIES5-NONROUND and the record (not re-read).

## 6. The independent reader's findings on FAMILIES5-NONROUND (2026-11-02), and their disposition

**Verdicts.**
- No hard errors.
- The class identity (C) was confirmed by an independent route.
- Theorem N is sound as a sketch, and "deduced" is the right label.
- N2's window was re-derived exactly: 1 − R²|Ω̇|² = (2 − e^ψ(1 + f))/(2 − e^ψ f).
- All four programs rerun byte-identically.

The reader's scripts were run in a scratch directory and are not banked here. Each finding is seated in
FAMILIES5-NONROUND.md as a dated bracketed amendment at the place it concerns. In summary:

- *(R) in two lines (seated, deduced).* The 3D orbit Raychaudhuri equation has no shear term. With P(κ_i) =
  ∇²ψ_i(P, P) and Rm(P, e_i, P, e_i) = −(∇²ψ_i(P, P) + κ_i²), (R) follows.
- *The flat model loses no derivative; compute the curved terms (done).* Section 3 here: they are first order in the
  metric, and the axis closes.
- *MAJOR 1: "only", "needs", "deduced" overclaim (seated).* The double-null-hierarchy statements were analogy. Section
  3 supersedes them.
- *MAJOR 2: N1's data (seated).* N1 is conditional on data. Section 2 constructs them near the seed (Proposition L),
  and the record's Proposition 6.5 is unchecked for a non-round source.
- *Minor.*
  - augment5 S1 is relabelled deduced.
  - augment5's S3/S5 claims and controls now compare with the computed div T, and S7 evaluates the computed bounds
    (repaired; mutations of the divergence now fail).
  - axisloss5 X3 now asserts ‖s‖ = ‖f‖ and ‖Af‖ = ‖f‖/√2 to 10⁻¹², with a rejecting control; the reader's mutations
    s := 2u_ρρ and Af := f/2 now fail.
  - jetpoly5 J1's and classchi5 C1's third controls are weak (they reject trivially): recorded, not repaired.
  - [DS23] (A4) fails more generically than stated.
  - [HL18]'s smallness includes the dust's (READ here).
  - Step 9's extension needs a cut-off on p_A.
  - N3 needs Ω's boundaries spacelike for the data's metric.
- *Nits (seated).* The wording of the verdict, and κ2 = (θ − κ1)/2 on the axis. X2 tests m = 0 and 1 only.

[R5 verifier of round 4 (nits). X3's ‖Af‖ = ‖f‖/√2 holds for the Gaussian family; only ‖s‖ = ‖f‖ is an identity
(FAMILIES5-NONROUND line 313's amendment should be read so). B5's 4.0 × 10⁻⁹ comes from ten implicit-Euler steps and is
qualitative, not converged.]

## 7. What is proved, and what is not

- Characteristic band data: exact localisation (B6, computed); the data themselves deduced.
- Cauchy band data:
  - the record's split forces global support (B5, computed);
  - the algebraic-hyperbolic split in the class (B1, computed), its signs (B2, computed, cross-checked against READ
    (4.30)), and its hyperbolicity on the seed region (B3, computed);
  - Proposition L: deduced from READ statements;
  - linear compact support in R and θ, not gauge (B4, computed);
  - nonlinear exact compact support: not done.
- The axis:
  - (G) and the planar trace (E0, computed);
  - the leaf's Volterra equation with first-order coefficients (E1, computed);
  - the estimate on curved data (E2, computed);
  - Lemma A, Theorem N′ and Corollary N′1: deduced. Not independently read.
- Vlasov:
  - the restricted system (V1), the axis condition (V2-V3) and the N-family symbol (V4): computed;
  - well-posedness of Einstein–restricted-Vlasov–dust in the class: deduced;
  - the high-frequency limit: open, its obstruction the N-dependence ([HL25], [Tou24], READ; V4, computed).
- **Open:**
  - an independent reading of sections 3.3-3.4;
  - Part II's (ii) at the axes for more than two families, and Part II's (iii);
  - a high-frequency construction uniform in N;
  - hyperbolicity of the algebraic split away from the seed region.

[R5 (FAMILIES5-VLASOV). The open items: an independent reading of sections 3.3-3.4 is done (the verifier of round 4,
seated above); Part II's (ii) at the axes is decided by (O1), (ii) for three or more families is replaced by (ii′),
(iii) is settled by the torus polarisation; Vlasov limits are proved without uniformity in N (Theorem V); the
algebraic split's hyperbolicity is decided on the whole slice (racglobal5 R1-R2), and replaced on its failing band by
cone data.]

## 8. Proposed replacement text for the paper's section 9, "More families"

> More families. In the class the null second fundamental form of each family is diag(θ_h, κ1, κ2), the torus terms
> first order, so off the axes each family's Raychaudhuri equation closes on its expansion. At an axis the one term
> left, the planar shear, is the trace-free part of the second fundamental form of the family's level sets in the
> slice. Elliptic regularity recovers it from the expansion using only first derivatives of the metric. So the
> Einstein–null-dust system in the class is stable around large solutions, without smallness, with any finite number of
> families, axes included: the two-dust background carries small non-round perturbations and small extra families on
> the whole domain. Data localised in an angle exist, on cones exactly and on slices in a slightly wider band. What does
> not extend is the high-frequency limit. Two families of one orientation are not separated at an axis, so beyond one
> ingoing and one outgoing family the extra families must vanish there. A non-round massless Vlasov field in the class
> has momenta in the orbit space and, at an axis, is either zero or the two radial dusts. Approximating it by N
> families costs a factor of order N² per stage, and the known constants grow faster with N, so non-round Vlasov limits
> remain open.

[R5 verifier of round 4 (MAJOR 2). Superseded by FAMILIES5-VLASOV.md section 9: this text overclaims ("stable around
large solutions" for Cauchy stability on compact domains of the record's type; it drops no caustics, the adapted
lateral boundaries with one family at each boundary–axis point and the support conditions; "the whole domain" for
the adapted one; no status labels; localised slice data claimed beyond the seed region; "momenta in the orbit space"
holds for limits only; the N² factor is a flat-orbit-space model).]

## Files

`FAMILIES5-AXIS.md` (this note). New, each with its `.out`:
- `checks/bandconst5.py` (B1-B6, a few minutes);
- `checks/axisellip5.py` (E0-E2, several minutes);
- `checks/vlasov5.py` (V1-V4, under a minute).

Repaired: `checks/augment5.py` and `checks/axisloss5.py` (`.out` regenerated). FAMILIES5-NONROUND.md: dated bracketed
amendments only.
