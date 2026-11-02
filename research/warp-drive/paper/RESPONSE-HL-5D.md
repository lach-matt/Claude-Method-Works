# A Five-Dimensional Black Hole Grown by Null Dust Is a High-Frequency Limit of Vacuum Gravity

## The Formal Counterpart to Huneau and Luk

*The title is the form the author set on 2026-10-20: a statement that answers the theorem's question, and this
subtitle.*

**Matthew Lach** · Independent Researcher · 20 October 2026

*Status: draft for the author's review. It is to be published on the author's website, through the session that
builds the site.*

Labels used throughout: **computed** (an exact identity checked by a program named in Appendix A, with a negative
control the program must reject), **deduced** (an argument written out here or in the supplement, a standard theorem
being invoked only after its statement was read at source and its hypotheses checked), **READ** (quoted verbatim at
source, with identifier and page). "Proved" means proved in this sense, and nothing else.

---

## Abstract

Huneau and Luk proved that every generic, small-data, polarized U(1)-symmetric solution of the Einstein–null dust system
with angularly separated dusts is a weak limit of vacuum solutions on a fixed time interval, in an elliptic gauge in
which smallness is needed even for local existence. We prove a five-dimensional counterpart on a large background. In
the class of five-dimensional vacuum metrics with a T² isometry and both reflections, the Einstein equations reduce
exactly to 2+1 gravity coupled to two free waves whose target metric, (3/2) dψ² + 2 dω², is flat and positive definite;
this is Huneau and Luk's reduced system with one scalar replaced by two. The background is five-dimensional Vaidya, a
black hole of mass μ0 that grows by an ingoing shell, and the domain runs from before the shell reaches the hole to the
surface, inside the horizon or on it, where the limit's curvature reaches a fixed scale (spacelike when μ0 > √72 l5²).
For every amplitude A > 0 and every smooth compactly supported envelope, with no smallness of either, we construct a
family of T²-symmetric vacuum metrics g_λ on that domain, of wavelength λ ≤ λ0, with |g_λ − g0| ≤ Cλ, ∂g_λ bounded, and
∂g_λ → ∂g0 weakly but not strongly, where g0 is Vaidya with dμ/dv = (2/9) A² env²: Isaacson's flux, the null dust of one
family. The proof uses the wave-map gauge relative to the limit itself and an approximate solution of arbitrarily high
order, so that every nonlinear term is beaten by a power of λ rather than by the size of the data; what must be uniform
in λ is then a linear estimate on the black-hole background, and its one large coefficient is removed by a phase-shift
identity. The Cauchy data are constructed by solving the constraints outward in r as a parabolic–hyperbolic system from
a sphere inside the shell. When μ0 > √72 l5², on each column the outgoing expansion of the spheres {v, r = const} has at
most one zero, exactly one on the columns that reach across the limit's horizon, converging to it at O(λ). So does a
mean-mass rate: after the shell, the mass of every sphere {v, r = const} is the limit's to O(λ²), by a quarter-turn
symmetry of the two polarizations. Solutions with the same properties are constructed from the waves' free data at past
null infinity, where before the shell they are the black hole exactly and their radiation field is the prescribed one at
every λ (Theorem 2). At past null infinity they admit Bondi coordinates and an expansion in r^(−1/2), and the
five-dimensional Bondi mass law holds for them (Theorem 3): their Bondi mass is μ(v) + O(λ) while the shell passes and μ
+ (2/9) λ² A² ∫ env'² + O(λ³) after it, the second-order rate measured on a numerical solution (section 6), with its
coefficient. Beyond that domain, outside the black hole, we prove that in the class a continuation of their data beyond
a ball about the hole settles at late times to five-dimensional Schwarzschild–Tangherlini, and that every perturbation
of them without symmetry that is small in Hintz's data class settles to a slowly rotating Myers–Perry black hole
(Theorem 4). The proof is Hintz's proof of the nonlinear stability of Kerr carried into five dimensions and written out
in full in the supplement: every section of his stability paper and of the companion papers that the route uses is
proved at n = 4, self-contained, from statements read at source that hold in every dimension, every input that depends
on the dimension computed at Schwarzschild–Tangherlini and proved at nearby Myers–Perry parameters, and each part was
read line by line by an independent reader, its findings repaired and the repairs read again. It replaces the censuses
and the deductions by which an earlier version of this paper carried his arguments to five dimensions. The linear
statement -- the stability of five-dimensional Schwarzschild–Tangherlini against linearised perturbations, in the gauge
of the nonlinear problem -- is proved with it, as the nonlinear theorem's linearisation. We list what is not proved, the
application at physical wavelengths among it.

---

## 1. Introduction

### 1.1 Burnett's problem

Huneau and Luk state the problem as follows (READ, [HL18] p. 1): "On a fixed manifold, consider a one-parameter family
of Lorentzian metrics g λ for λ ∈ (0, λ 0 ], λ 0 ∈ R which satisfies the Einstein vacuum equations [1] R μν (g λ ) = 0.
(1.1) Assume moreover that there exists a metric g 0 such that as λ → 0, • g λ converges to g 0 uniformly on compact
sets; and • the derivatives of g λ converges weakly in L 2 to the derivatives of g 0 . Due to the nonlinearity of the
equations, it can happen that the limiting metric g 0 is a solution to the Einstein equations which is not vacuum"
(their footnote marker printed as "[1]"). Burnett's own assumptions, as Luk and Rodnianski print them (READ, [LR20] p.
3, their (1.3)): "|g n − g ∞ | ≤ λ n , |∂g n | ≤ C, |∂ 2 g n | ≤ Cλ −1 n". The direct question asks which limits occur;
the reverse asks whether a given Einstein–matter solution is such a limit.

### 1.2 The theorem answered

Huneau and Luk work with metrics (READ, [HL18] pp. 2–3) "(4) g = e −2φ g + e 2φ (dx 3 ) 2", for which "Einstein
vacuum equations R( (4) g) μν = 0 are equivalent to the following system for (g, φ): { □_g φ = 0, R μν (g) = 2∂ μ
φ∂ ν φ. (1.3)" (the box, lost in the extraction, restored).
Their main theorem (READ, [HL18] p. 10, verbatim; their footnotes 11 and 12 omitted, and the extraction's typography
restored: fractions, accents and arrows, and the two column vectors of (4.1) printed in a row with ";"):

> **Theorem 4.2 (Main theorem).** Let k ≥ 10, − 1/2 < δ < 0, R > 0 and A be a finite set. Given an admissible free
> initial data set ( φ̇, ∇φ, F̆ A , u A ) ↾ Σ 0 such that
> • |∇u A ↾ Σ 0 | > 1/2 ;
> • u A ↾ Σ 0 is angularly separated;
> • (Smallness condition) ‖∇u A − c⃗ A ‖ H 11 δ + ‖ φ̇‖ H 10 + ‖∇φ‖ H 10 + ‖ F̆ A ‖ H 10 ≤ ε;
> • (Genericity condition on initial data) there exists a point p ∈ R 2 such that ( (∂ 1 φ 0 ) ↾ Σ 0 ; (∂ 1 φ̇ 0 ) ↾
> Σ 0 ) (p) and ( (∂ 2 φ 0 ) ↾ Σ 0 ; (∂ 2 φ̇ 0 ) ↾ Σ 0 ) (p) are linearly independent. (4.1)
>
> Then, there exists ε 0 > 0 such that if ε < ε 0 , a unique solution (g 0 , φ 0 , (F 0 ) A , (u 0 ) A ) to (1.4)
> arising from the given admissible free initial data set exists on a time interval [0, 1], and there exists a
> one-parameter family of solutions (g λ , φ λ ) to (1.3) for λ ∈ (0, λ 0 ) (for some λ 0 ∈ R sufficiently small),
> which are all defined on the time interval [0, 1], such that (g λ , φ λ ) → (g 0 , φ 0 ) uniformly on compact sets
> and (∂g λ , ∂φ λ ) ⇀ (∂g 0 , ∂φ 0 ) weakly in L 2 with ∂g λ , ∂φ λ ∈ L ∞ loc uniformly.

Here (1.4) is the Einstein–null dust system with |A| families (READ, [HL18] p. 3), the admissible free data are posed
on a maximal slice of R² and solved for in an elliptic gauge (READ, [HL18] pp. 8–9, Definition 3.2 and Theorem 3.3),
and angular separation is Definition 4.1 (READ, [HL18] p. 10). Their review states where the smallness comes from and
names the large-data problem (READ, [HL24] p. 28): "Notice that in the U(1) setting, because of our use of an elliptic
gauge, smallness is required even for local existence of smooth solution. It would be interesting to carry out these
constructions without smallness assumptions: Problem 8.6. Construct local high-frequency solutions as in Sections 5, 6
and 7.2 but such that the limiting solution is far away from Minkowski spacetime."

### 1.3 What this paper proves

We prove the counterpart of Theorem 4.2 in five dimensions, for one family of null dust, on a background that is far
from Minkowski: a black hole growing by an ingoing shell, on a fixed domain that reaches inside the horizon to the
surface where the limit's curvature reaches a fixed scale (Theorem 1, section 3). It is an instance of Problem 8.6 in a
five-dimensional symmetry class, not an answer to Problem 8.6 as posed, which concerns four dimensions. Solutions with
the same properties are also constructed from the waves' free data at past null infinity (Theorem 2, section 3), and at
past null infinity they obey the five-dimensional Bondi mass law with the prescribed radiation field (Theorem 3, section
3).

Beyond that domain, and outside the black hole, we prove that in the class a continuation of their data beyond a ball
about the hole settles at late times to five-dimensional Tangherlini of a nearby mass, and that their perturbations
without symmetry that are small in Hintz's data class settle to slowly rotating Myers–Perry black holes (Theorem 4,
section 8.8). The route is Hintz's proof of the nonlinear stability of Kerr [Hin26], carried into five dimensions: every
input that depends on the dimension is computed at Tangherlini, the class removes his boosts, rotations and their gauge
modifications, and without it they are restored, with the inputs at every nearby Myers–Perry parameter proved by
perturbation from Tangherlini, in the manner of [HHV21], and the charges by which the gluing at large radius matches the
Myers–Perry family computed. The proof is written out in full at n = 4 in the supplement (`proof5/`): his stability
paper, the parts of his companion papers [Hin26a, Hin26c, Hin23a] that the route uses, and [CD03]'s gluing, part by
part, self-contained, from statements READ at source that hold in every dimension, each part read line by line by an
independent reader and its repairs read again. An earlier version of this paper reached Theorem 4 by deduction: those
papers' proofs were carried to five dimensions by modification, at every place a full-text census of the source found
the dimension, and the completeness of the censuses was evidenced by two methods, not proved. The write-out uses no
census of the source papers; its own three completeness claims are settled by enumeration and by a reading (section
8.8).

The two theorems share their architecture. Both reduce the vacuum equations in the symmetry class to 2+1 gravity coupled
to free waves with a flat, positive-definite target (Proposition 2.1 here; [HL18] (1.3)); both build an approximate
solution by geometric optics and correct it on a fixed interval; both conclude with uniform convergence of the metric
and weak, not strong, convergence of its derivatives (in Huneau and Luk, of the 3+1 metric; their reduced metric's
derivatives converge uniformly, [HL18] Remark 4.3, p. 10), the defect being null dust. They differ in what is large:
Huneau and Luk allow any finite number of angularly separated dusts on a small background; we allow one dust on a large
one, and the amplitude of the waves is not small either.

### 1.4 Why five dimensions and a black hole

In five dimensions the T² class is the natural analogue of polarized U(1): the two rotations of R⁴ = R² × R² commute,
the two reflections make the Killing fields hypersurface orthogonal and mutually orthogonal, and the reduction is exact
(Proposition 2.1). Unlike Huneau and Luk's translation, each rotation has an axis, where the reduced system degenerates;
the proof therefore never uses the reduced system and works in five-dimensional Cartesian coordinates, in which the axes
are regular points. Five-dimensional Vaidya is the simplest large solution of the limiting system: its mass grows by
exactly the averaged energy of the waves, and it carries a horizon. The domain ends where the curvature reaches a fixed
scale l5, x_K := l5² √K = 1 with K the Kretschmann scalar; that surface lies inside the horizon, or on it at equality,
and is spacelike when μ0 > √72 l5² (section 6), so the domain is the domain of dependence of its data and nothing inside
it is excised. The solution is constructed on a compact set Ω reaching a fixed distance inside that surface, and nothing
in Theorems 1–3 is claimed beyond Ω; Theorem 4 concerns the exterior of the black hole after the shell. Nothing in the
paper involves an inner or Cauchy horizon.

---

## 2. Setting

### 2.1 The class and the reduction

Let g5 be a Lorentzian metric on a five-manifold, invariant under an effective T² action and under both reflections
of its orbits. Invariance under each reflection removes the cross terms, so locally

    g5 = g3 + e^(2A) dφ1² + e^(2B) dφ2²,                                                                  (2.1)

with g3 a Lorentzian metric and A, B functions on the three-dimensional orbit space.

**Proposition 2.1 (the reduction; computed, `paper/response5.py` R1).** Put ψ := A + B, ω := (B − A)/2 and
h := e^(2ψ) g3. Then

    Ric[h]_ab = Ric[g5]_ab + (3/2) ∂_aψ ∂_bψ + 2 ∂_aω ∂_bω + (e^(−2A) R11 + e^(−2B) R22) (g3)_ab,
    e^(2ψ) □_h ψ = −(e^(−2A) R11 + e^(−2B) R22),     e^(2ψ) □_h ω = (e^(−2A) R11 − e^(−2B) R22)/2,

with R11, R22 the φ1φ1 and φ2φ2 components of Ric[g5], whose mixed components Ric[g5]_(aφi) and Ric[g5]_(φ1φ2)
vanish identically. Hence g5 is vacuum if and only if

    Ric[h] = (3/2) dψ² + 2 dω²,     □_h ψ = 0,     □_h ω = 0.                                              (2.2)

With ψ̃ := (√3/2) ψ, (2.2) reads Ric[h] = 2 (dψ̃² + dω²), □_h ψ̃ = □_h ω = 0: Huneau and Luk's (1.3) with the scalar φ
replaced by the pair (ψ̃, ω), whose target is the flat Euclidean plane. The check is exact: the identities are
tensorial, so at a point it takes coordinates normal for g3 and treats the second derivatives of g3 and the 2-jets of A
and B as free symbols; replacing 3/2 by 1 fails. The same reduction is computed independently, in other variables, by
`docket68/lemmas/kn_gauge.py` (K1–K2).

### 2.2 The background

Coordinates X = (τ, x) ∈ R × R⁴, r = |x|, x̂ = x/r, v := τ + r. The T² action rotates the planes (x1, x2) and
(x3, x4); its axes are regular points of R⁴. Let

    g0 := η + (μ(v)/r²) dv²,     g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0,     L0 := ∂_τ − x̂·∂_x,     det g0 = −1,       (2.3)

with μ smooth, nondecreasing, μ = μ0 > 0 for v ≤ v_start and constant for v ≥ v_end.

**Proposition 2.2 (computed: `paper/response5.py` R2–R4; `docket68/n1star/ks5.py` K1–K5).**
(a) g0 is five-dimensional Vaidya: Ric(g0) = (3 μ'(v)/(2 r³)) dv ⊗ dv, and its (τ, r) block has determinant −1.
(b) The Kretschmann scalar is K = 72 μ(v)²/r⁸, also where μ' ≠ 0; the round spheres have one apparent horizon, r = √μ.
(c) ℓ := g0⁻¹ dv = −L0 is null and geodesic, with L0(v) = 0, L0(τ) = 1, L0(r) = −1; the phase v is an exact
eikonal of g0 and its level sets are the ingoing cones.
(d) g0⁻¹(dτ, dτ) = −1 − μ/r², g0⁻¹(dr, dr) = 1 − μ/r², g0⁻¹(dr, dτ) = μ/r², g0⁻¹(d(v + τ), d(v + τ)) = −3 − μ/r²;
the slices {τ = const} are spacelike everywhere, and the lines of constant x are spacelike where r² < μ.
(e) For every function u, with □̃ := g0^(ab) ∂_a ∂_b acting componentwise and ∂_r := x̂·∂_x,

    [L0, □̃] u = (2/r)(□̃ u + (∂_τ + ∂_r) L0 u) − (3/r²) ∂_r u,                                          (2.4)

the mass dropping out (ks5.py K3, checked on every monomial of degree ≤ 3 with a symbolic base point). This is the
five-dimensional form of Touati's commutator lemma ([Tou23a] Lemma 3.1, p. 21, which bounds [L0, □]f by ∂L0 f, □f and
∂f), here an exact identity.

### 2.3 The curvature boundary and the domain

Fix a length l5 > 0. The surface x_K := l5² √K = 1 is r = r_q(v) := (√72 μ(v) l5²)^(1/4), and r_q ≤ √μ, so that it lies
inside or on the horizon, exactly when μ ≥ √72 l5² (computed, R3). The seed condition is μ0 ≥ √72 l5². Fix T > 0 and
let

    D_T := { v ≤ v_end + T,  r ≥ r_q(v) },                                                                (2.5)

the region from past null infinity to the curvature boundary, up to the time T after the shell has passed. Fix τ0
with v_start − τ0 > √μ0 + 1, so that on the slice Σ_τ0 := {τ = τ0} the shell lies outside the seed's horizon: the
slice is before the shell reaches the hole. The proof works on a compact set Ω ⊃ D_T ∩ {τ ≥ τ0} (supplement (1.1))
bounded by Σ_τ0, a slice Σ_τ_end, an inner sphere r = a with a < r_q(μ0), and an outer spacelike surface
{v + τ = const}. By (d), each part of the boundary other than Σ_τ0 is spacelike with Ω to its past, so Ω is a domain
of dependence of Σ_τ0 ∩ Ω, and so is every C⁰-small perturbation of g0 (supplement Lemma 1.1).

### 2.4 The waves and their average

The waves are two polarizations a quarter turn apart, with amplitude A, envelope env(v) supported in [v_start, v_end],
angular profile h(ζ) = √(2/(1 + ζ²)) on the orbit space (ζ = cos 2θ, c² = (1 + ζ)/2, s² = (1 − ζ)/2; the programs call ζ
"x") and phase v/λ; at past null infinity their free data are F = λ A env(v) h(ζ) sin(v/λ), G = λ A env(v) h(ζ)
cos(v/λ). In the gauge of section 2.5 the leading wave W_TT is traceless, transverse to ℓ, of amplitude r^(−3/2), and
smooth at both axes (computed, `docket68/n1star/ansatz5.py` A3). Explicitly, with c = cos θ and s = sin θ on the orbit
space (the round metric of S³ being dθ² + c² dφ1² + s² dφ2²), and F and G taken at the angle θ and the phase v/λ,

    λ W_TT = 2 r^(1/2) (c² p1 dφ1² + s² p2 dφ2² − (p1 + p2) dθ²),   p1 := (2c² G − s² F)/3,   p2 := (2s² F − c² G)/3,
                                                                                                         (2.5′)

traceless on the spheres and with no dv or dr component (computed: the components are those of the supplement's
programs, `data5.py` and `ansatz5.py` A3, and of Theorem M (b) of its section 11; `paper/response5.py` R12).

**Proposition 2.3 (the limit; computed: `docket68/n1star/lead5.py` L2; `docket68/lemmas/hf_theorem5.py` F3;
`paper/response5.py` R6).** The θ-mean of the leading equation of the two-scale expansion (section 4) vanishes exactly
when μ' = (2/9) A² env² h² (c⁴ + s⁴), and h² (c⁴ + s⁴) = 1: the averaged stress of the waves is round, and

    dμ/dv = (2/9) A² env².                                                                               (2.6)

This is Isaacson's effective stress as a five-dimensional null dust along dv. The part of R_vv quadratic in the wave
rates is −2 (P1_v² + P1_v P2_v + P2_v²), whose form is positive definite (4 (a² + ab + b²) = (2a + b)² + 3 b²), and
every other component of the Ricci tensor carries no such product: the defect is null dust and nothing else (computed
in Bondi-type variables, hf_theorem5.py F3, cross-checked there in Wolfram Language and Lean 4).

### 2.5 The gauge

The gauge is the wave-map gauge relative to g0 itself. For a Lorentzian metric g put

    D^ρ(g) := g^(ab) (Γ[g]^ρ_ab − Γ[g0]^ρ_ab),
    Ric^H(g)_mn := Ric(g)_mn − (1/2)(g_mρ ∇̂_n D^ρ + g_nρ ∇̂_m D^ρ)
                 = −(1/2) g^(ab) ∂_a ∂_b g_mn + Q_mn(X; g)(∂g, ∂g),                                               (2.7)

∇̂ the connection of g0 and Q a quadratic polynomial in ∂g, with a linear and a constant part (Ric^H(g0) = Ric(g0) ≠ 0
needs one), whose coefficients are rational in g and smooth in X on r > 0 (READ: [CBCM10] (2.7)–(2.9), arXiv v1 PDF p.
8, in n + 1 dimensions, formulae transcribed: "R_(α β) = R^(H)_(α β) + 1/2 (g_(α λ) D̂_β H^λ + g_(β λ) D̂_α H^λ)",
"R^(H)_(α β) = −1/2 g^(λ μ) D̂_λ D̂_μ g_(α β) + f̂[g, D̂ g]_(α β)", f̂ "independent of the second derivatives of g"). D
and Ric^H are built from g and g0 alone, so they are invariant under the isometries of g0, which include T² and both
reflections. Ric^H(g) = 0 is a quasilinear wave system, D(g0) = 0, Ric^H(g0) = Ric(g0), and a solution with D = 0 is
vacuum.

---

## 3. The theorem

**Theorem 1 (the five-dimensional counterpart; deduced, supplement sections 1–8, as summarized below).** Let l5 > 0, μ0
≥ √72 l5², A > 0 and env ∈ C_c^∞([v_start, v_end]), and let g0 be the Vaidya metric (2.3) with μ(v) = μ0 + (2/9) A²
∫_(−∞)^v env². Fix T > 0, τ0 with v_start − τ0 > √μ0 + 1, and K ≥ 6. There are λ0 > 0 and C, depending on (l5, μ0, A,
env, T, τ0, K) and the inner radius a of Ω, and not on λ, such that for every λ ∈ (0, λ0] there is a smooth Lorentzian
metric g_λ on Ω ⊃ D_T ∩ {τ ≥ τ0} with:

1. **Vacuum and symmetry.** Ric(g_λ) = 0 on Ω, and g_λ is invariant under the T² action and both reflections.
2. **Data.** On Σ_τ0, the Cauchy data of g_λ satisfy the vacuum constraints exactly, equal the data of the seed
   (five-dimensional Schwarzschild–Tangherlini of mass μ0) on r < v_start − τ0, and differ from those of an approximate
   solution g_app (section 4) by O(λ^K) in the λ-scaled norm (E4) of the supplement; the leading oscillation of g_app is
   the waves of section 2.4.
3. **The remainder.** g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω, where g_app = g0 + λ [g1] +
   Σ_(j=2)^N λ^j [g_j] with smooth profiles g_j(X, θ), 2π-periodic in θ, evaluated at θ = v/λ.
4. **Convergence.** |g_λ − g0| ≤ C λ and |∂g_λ| ≤ C on Ω; ∂g_λ − ∂g0 = dv ⊗ [∂_θ g1] + O(λ), so ∂g_λ → ∂g0 weakly in
   L²(Ω), and not strongly wherever env ≠ 0 (the phase mean of ∂_θ g1 is 0 and that of its g0-norm squared (4/3) A² env²
   r⁻³, computed, `docket68/n1star/checks/support3.py` D2). The limit g0 satisfies Ric(g0) = (3 μ'/(2 r³)) dv ⊗ dv with
   (2.6): it is not vacuum but Einstein–null dust with one family.
5. **Gauge and uniqueness.** D(g_λ) = 0 on Ω, and g_λ is the only C² solution of Ric^H(g) = 0 on Ω with its data within
   ε1 of g0 (supplement section 4, Step 8).
6. **The spheres' horizon.** If μ0 > √72 l5² and λ ≤ λ_H (Proposition 3.3), the outgoing expansion of the spheres {v, r =
   const} has at most one zero on each column (v and the angles fixed), exactly one within C λ of √μ(v) on the columns
   that reach across it, the spheres with r ≤ √μ(v) − C λ being trapped and those with r ≥ √μ(v) + C λ untrapped: no
   inner zero, and the zero converges to √μ at O(λ) (Proposition 3.3).
7. **Mean mass.** For every sphere S_(v,r) of the domain, its Hawking mass satisfies |M[S](g_λ) − μ(v)| ≤ C λ² before and
   after the shell (v ≤ v_start or v ≥ v_end), and ≤ C λ within it (Proposition 3.4).

The constants that the argument fixes explicitly: the order of the energy is k = 6, the approximant used has N = K + 3
stages, λ ≤ λ_Ω := min(1, δ0)/10 where δ0 := r_q(μ0) − a (a condition the construction imposes, not a bound below which
the theorem holds: that is λ0), and the data are solved in H^s(S³) with s > 3/2 + 4 (the derivative count as a ledger,
`docket68/n1star/checks/support3.py` D4). λ0 and C are not evaluated. Every constant of the approximant's own estimates
is λ-independent, because its profiles are (deduced: supplement 5.4; computed for the profiles the programs compute,
`paper/response5.py` R13); the waves are high-frequency on all of D_T once λ < l5/10 (computed:
`docket68/lemmas/counterpart5.py` P1).

**Proposition 3.2 (the boundary; computed R6, deduced).** On x_K = 1, with Φ := r − r_q(v),

    g0⁻¹(dΦ, dΦ) = 1 − √(μ/(√72 l5²)) − r_q μ'/(2 μ),                                                     (3.1)

so, μ being at least μ0 ≥ √72 l5² throughout, the boundary is spacelike for g0 wherever μ > √72 l5² or μ' > 0, and every
future causal curve that meets it leaves D_T there and does not return. If μ0 > √72 l5² the margin is uniform, g0⁻¹(dΦ,
dΦ) ≤ −δ with δ := √(μ0/(√72 l5²)) − 1 > 0, and for g_λ the margin is −δ + C λ ≤ −δ/2 once C λ ≤ δ/2 (deduced: |g_λ⁻¹ −
g0⁻¹| ≤ C λ on Ω by item 4, and the cone of future causal covectors moves continuously; the margin −δ computed exactly,
R13). If μ0 = √72 l5² exactly, the
boundary coincides with the seed's horizon for v ≤ v_start and is null there; g_λ equals the seed on {v ≤ inf supp env},
so it is null for g_λ too, and after the shell starts it is spacelike for g_λ outside a layer whose width tends to 0
with λ (supplement `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4).

**Proposition 3.3 (one zero per column of the spheres' outgoing expansion; deduced, with `docket68/n1star/horizon5.py`
H1–H3; supplement Proposition 8.1).** Let μ0 > √72 l5², K ≥ 6, and let θ⁺_λ(v, r, ω) be the outgoing null expansion, for
g_λ, of the sphere S_(v,r) := {τ = v − r, |x| = r} at its point of angle ω. There are λ_H ∈ (0, λ0] and C, δ1 > 0 such
that for λ ≤ λ_H: on every column (v and ω fixed, r varying, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero, positive
above it and negative below; on the columns with √μ(v) ≤ v − τ0 − δ1 it has exactly one, R_λ(v, ω), with |R_λ − √μ(v)| ≤
C λ; and the spheres with r ≤ √μ(v) − C λ are trapped, those with r ≥ √μ(v) + C λ untrapped.

*Proof.* For g0 the outgoing null normal of S_(v,r) with n(τ) = 1 has expansion θ⁺ = (2r²/(r² + μ)) · 3(1 − μ/r²)/(2r),
whose one zero r = √μ is simple, ∂_r θ⁺ = 3/μ there, and the ingoing expansion is −3/r (computed, H1). θ⁺ is a smooth
function of g, linear in ∂g. The approximant's leading wave enters θ⁺ at order λ⁰ only as (1/2) k(ℓ) ∂_θ(tr_S W), and
tr_S W = tr_g0 W = 0 because W(ℓ, ·) = 0 (computed: H2 for a sample profile tangent and traceless on the spheres, and H2b
for the wave (2.5′) itself at the shifted phase θ + φ1, with χ dv² and a mean m1, symbolically in every function; a trace
gives an O(1) oscillation); the mean m1 has no θ-dependence and the higher profiles enter at O(λ). Along a column v is
constant (H3), so the r-derivative of a profile term [f] is [∂_r f], with no λ⁻¹: θ⁺(g_app) − θ⁺(g0) and its r-derivative
along columns are O(λ). The remainder contributes C(|w| + |∂w| + |∂²w|) ≤ C λ^(K−5) ≤ C λ (Theorem E, supplement section
4 Step 1). Away from √μ the background expansion is bounded away from zero on the compact columns, and near it θ⁺_λ is
strictly increasing in r; √μ(v) − r_q(v) = μ^(1/4)(μ^(1/4) − (√72 l5²)^(1/4)) ≥ its value at μ0 > 0, the right side
increasing for μ > √72 l5²/16 (computed, `docket68/n1star/checks/support3.py` D1). The intermediate value theorem and the
monotonicity give the zero and its uniqueness. If μ0 = √72 l5², the first statement holds on every column, and the others
on the columns with μ(v) ≥ μ0 + δ1. ∎

**Proposition 3.4 (the mean mass; deduced, with `docket68/n1star/mass5.py` M1–M4; supplement Lemma 8.2 and Proposition
8.2).** For a 3-sphere S let M[S](g) := R²(1 + (R²/9)⟨Θ⟩), with R := (Area(S)/(2π²))^(1/3), Θ := 2θ⁺θ⁻/(−g(n⁺, n⁻))
built from its two future null normals and their expansions, and ⟨·⟩ the mean over S: the five-dimensional Hawking mass,
with M[S_(v,r)](g0) = μ(v) (computed, M1). Then for K ≥ 6 and λ ≤ λ0, |M[S_(v,r)](g_λ) − μ(v)| ≤ C λ² wherever v ≤
v_start or v ≥ v_end, and ≤ C λ for v_start < v < v_end.

*Proof.* Let σ be the isometry θ ↦ π/2 − θ, φ1 ↔ φ2 of S³; it fixes τ, r and v, is an isometry of g0 and maps each
S_(v,r) to itself (computed, M4). The waves' two polarizations are a quarter turn apart, and that makes the leading wave
odd under σ combined with the phase reflection θ ↦ 3π/2 − θ: W_TT(σX, 3π/2 − θ) = −W_TT(X, θ) (computed, M2; one
quadrature alone, or two in phase, is not odd). The two-scale operator is equivariant under θ ↦ c0 − θ with λ ↦ −λ
(computed, M3), and every stage of the approximant is the unique solution of a problem that this combined map carries to
itself, so the profiles obey σ*g_j(·, 3π/2 − ·) = (−1)^j g_j; for the first mean correction, σ*m1 = −m1 (its source in
the proof's gauge, the phase mean of R^(1)[g0 + λW], is nonzero only in dv dθ, −(4/9) A² env² H² sin 2θ/r³, and odd:
computed, `docket68/n1star/checks/stage5.py` S2). Outside the shell the oscillating profiles vanish, so g_app = g0 + λ m1
+ O(λ²) there, and M[S](g_λ) = μ(v) + λ DM[m1] + O(λ²) + O(|w| + |∂w|). M is natural, so DM[σ*m] = DM[m], and DM[m1] =
DM[σ*m1] = −DM[m1] = 0. The remainder is at most C λ^(K−4) ≤ C λ². Inside the shell the wave enters M only through its
trace on the sphere and the trace of its phase derivative, both zero, so the difference is O(λ) (computed: at order λ⁰
only θ⁺ carries the wave, through ∂_θ tr_S W, and θ⁻, the area and g(n⁺, n⁻) do not;
`docket68/n1star/checks/support5c.py` C13). ∎

The numerics' "mean mass" is the angular mean of the mass aspect at past null infinity; the Hawking mass of the spheres
of the domain is its counterpart here. Theorem 2 below gives the waves' field at past null infinity exactly; what it
implies for a mass there is in section 6, and what it does not, in section 9.

*How Theorem 1 follows.* It is the conjunction of three theorems proved in the supplement and summarized in sections 4
and 5: Theorem A (the approximant to any order), Theorem D (exact data within O(λ^K) of it) and Theorem E (existence on Ω
with λ-uniform remainder estimates). D(g_λ) solves a homogeneous linear wave system by the contracted Bianchi identity
and vanishes with its first derivative on Σ_τ0 (the gauge condition and the constraints), so D = 0 on Ω and g_λ is vacuum
(deduced; the identity, div(E − ½ g tr E) = −½ (□D + Ric(D)) with E := Ric − ∇_(μ D_ν), computed exactly at a point on
random 4+1 metrics, `paper/response5.py` R14, and READ in [LR05] p. 1 and, in n + 1 dimensions, [CBCL06] section 3: "the
harmonicity functions F^μ := □_g x^μ satisfy an homogeneous linear system of wave equations on (V, g), with also ∂_t F^μ
= 0, hence F^μ = 0 if (V, g) is globally hyperbolic"; for the wave-map gauge, [CBCM10] Theorem 3.3, (3.10)–(3.11), p.
14). The symmetry follows from uniqueness, since Ric^H and D are built from g and the O(4)-invariant g0 alone and the
data are invariant (the six generators of so(4) Killing for g0 and both reflections isometries of it, for every μ(v), and
g0 + λ W invariant under the T² action and the reflections: computed, `docket68/n1star/checks/support3.py` D3).

**Theorem 2 (the construction from past null infinity; deduced, supplement section 9; computed:
`docket68/n1star/past5.py` P1–P8).** Let the waves at past null infinity be the free data F, G of section 2.4, on the
background of Theorem 1. For every K ≥ 6 there is λ_P > 0 such that for 0 < λ ≤ λ_P there is a smooth vacuum metric
g_λ, in the wave-map gauge relative to g0, on Ω together with a past domain P: the region τ ≤ τ0, r ≥ a, below an outer
boundary v + ½(1 + τ0 − τ)^(−1/4) = V_P that is spacelike, chosen so that P and Ω share the slice Σ_τ0. It satisfies:

1. g_λ = g0 for v ≤ v_start: before the shell, the black hole exactly;
2. its radiation field at past null infinity is the prescribed one: at every fixed v < V_P and x̂,
   r^(3/2)(g_λ − g0 − λ[W_TT]) → 0 as r → ∞, at every λ;
3. on P, |g_λ − g_app| ≤ C λ^(K−3) t^(−2), with t = 1 + τ0 − τ and g_app the approximant built from past null
   infinity;
4. on Ω, the conclusions of Theorem E hold (items 1 and 3–5 of Theorem 1), with the data on Σ_τ0 now the trace of g_λ
   itself; items 6–7 are proved for Theorem 1's solutions, and the supplement carries them to these by the same argument
   without writing it out (supplement section 9.5; with χ carrying no radiation at past null infinity, m1's source is the
   same and odd, `docket68/n1star/checks/stage5.py` S3, m1 itself from past null infinity not computed);
5. g_λ is T² × Z2 × Z2-invariant, and unique among solutions with item 1 whose difference from g_app is, with its first
   derivatives, at most ε_P t^(−3/2) for a small ε_P > 0 (supplement Lemma 9.1 (f)), and whose energy on the slices
   tends to zero at past null infinity.

So the counterpart holds with the waves' own free data at past null infinity, and the constraints need not be solved
on this route (section 5.5 is the other route).

*How Theorem 2 is proved.* Before the shell the solution is the black hole: the region v ≤ v_start is a past set for the
black hole's cones, and the data there are the black hole's. Near past null infinity every stage of the approximant is
solved with nothing coming in. Each stage has an explicit leading term in r and a remainder half a power of r better, and
no source of the stages ever falls off like r^(−5/2), the rate that would produce a logarithm (P2–P5). So the residual
decays like r^(−3), and the remainder can be estimated with the rotations as commutators, which gain t^(−3/2) in
Sobolev's inequality. The past is split at t = λ^(−2). Before the split, the one large coefficient of section 5.1
integrates in time to a constant, and no decomposition is needed. After it, the decomposition of section 5.2 runs over an
interval of length λ^(−2). There the transport of its auxiliary field loses a logarithm per unit of log t, which weights
(T/t)^β0 absorb at a cost λ^(−2β0); β0 does not depend on the order of the approximant, so a higher order pays it (the
exponent ledger with β0 symbolic computed, `docket68/n1star/checks/ledger5.py` L1). The mollifier's commutator with the
wave operator is, apart from decaying terms, an exact derivative along the generators (P8), and is absorbed into the
auxiliary field. The limit is vacuum because the gauge field of the approximant decays at past null infinity, so its
energy tends to zero there and the gauge field vanishes (an r⁻² amplitude on a v-strip of fixed width has L² norm at most
C t^(−1/2), and r² D^(1) stays bounded at leading order with m1 generic: computed, `docket68/n1star/checks/gauge5.py`
G3). A first independent verifier found the near-region estimate incomplete: that commutator was missing. A second found
that the repair closes it (supplement section 9).

**Theorem 3 (the Bondi mass at past null infinity; deduced, supplement section 11; computed:
`docket68/n1star/bondi5.py` B1–B4).** Let g_λ be the metric of Theorem 2, 0 < λ ≤ λ_P. Near past null infinity it
admits Bondi coordinates (v_B, r_B, θ_B, φ1, φ2) — v_B null with v_B − v → 0 at past null infinity, θ_B constant along
the generators, r_B the areal radius — in which

    g_λ = −e^(2β) W dv_B² + 2 e^(2β) dv_B dr_B + r_B² [e^(−2(P1+P2)) (dθ_B − U dv_B)² + cos²θ_B e^(2P1) dφ1²
          + sin²θ_B e^(2P2) dφ2²],                                                                        (3.2)

with P1, P2, β, U, W − 1 expanded in r_B^(−1/2) to order r_B^(−3) with o(r_B^(−3)) remainders, coefficients smooth in
(v_B, θ_B) and zero for v_B ≤ v_start. In it:

1. P_i = r_B^(−3/2) p_i + O(r_B^(−5/2)), p1 = (2c² G − s² F)/3 and p2 = (2s² F − c² G)/3 as in (2.5′), with c = cos θ_B,
   s = sin θ_B and the free data F, G of section 2.4 at phase v_B/λ (the radiation field of Theorem 2, item 2;
   supplement Theorem M (b)); the r_B^(−2) coefficients vanish;
2. W = 1 + r_B^(−3/2) V1 − r_B^(−2) M + O(r_B^(−5/2)), with V1 a divergence on S³ and the mass aspect M obeying,
   pointwise, the five-dimensional Bondi law [TTS09] (28) time-reversed,

       ∂_v M = (4/3)(∂_v p1² + ∂_v p1 ∂_v p2 + ∂_v p2²),                                                      (3.3)

   with M = μ0 for v_B ≤ v_start;
3. the Bondi mass μ_B(v) := ⟨M(v, ·)⟩ (the mean over S³) therefore obeys μ_B' = the flux of section 6, exactly: it
   is μ(v) + O(λ) while the shell passes, with the oscillation (6.1) gives, and μ(v_end) + (2/9) λ² A² ∫ env'² + O(λ³)
   after it;
4. the Hawking mass M[S] of Proposition 3.4 of the Bondi spheres S = {v_B, r_B = const} tends to μ_B(v_B) as
   r_B → ∞.

This is the mean mass at past null infinity, the sphere mean of the Bondi mass aspect, the quantity the numerical
solution of section 6 integrates, now proved for g_λ.

*How Theorem 3 is proved.* At fixed λ the far region of Theorem 2 is a neighbourhood of past null infinity, and
there the remainder g_λ − g_app is a solution of a wave equation whose source decays like r^(−3): subtracting its
leading term, which is explicit, and estimating the rest with the energy of Theorem 2's far region gains half a power
of r at each step, so g_λ − g0 has an asymptotic expansion in r^(−1/2) to any order, with the radiation field as its
leading term; the derivatives along the ingoing generators of the remainders gain a full order, because the wave
equation is a transport along the outgoing generators for them, and those generators reach the seed region, where
everything vanishes, after a bounded parameter length (supplement Proposition 11.1; the half power gained at each step
and the generators' reach computed, `docket68/n1star/checks/ledger5.py` L3). The Bondi coordinates are then
built from the null geodesics of g_λ asymptotic to the ingoing generators of the background, in the manner of [HL21]'s
eikonal function at future null infinity: v_B is constant on the null hypersurfaces they sweep, and its eikonal
equation, a transport along those generators with a source that decays like r^(−2) because the first-order wave is
transverse to them, gives its expansion; the angular coordinates are the generators' asymptotic angles, the areal
radius is algebraic; every step has an expansion, and the leading angular coefficient is untouched (supplement
Proposition 11.2, computed B2). In the Bondi form the vacuum equations are a hierarchy in r_B^(−1/2) — the one [TTS09]
wrote in five dimensions — which B1 recomputes in the class with every coefficient from the first order general: the
radial equations kill every coefficient below the waves' (including the one the chart could carry at order r^(−1))
and fix β, U and V1, the traceless angular equation at order r^(−1) makes the r_B^(−2) coefficients of P constant in
v, which the seed sets to zero, and R_vv at order r^(−3) is (3.3) plus a divergence that vanishes with them. The
hierarchy needs the expansions only to the order Theorem 3 states, and the remainders cannot enter below it: an
r-derivative raises the order by two, the others preserve it, and which coefficients the equation at order r^(−3)
contains is read off the computation. The mass law integrates from the seed; its sphere mean is section 6's flux,
computed exactly in `past5.py` P7.

---

## 4. The approximant

**Phase and profiles.** The phase is v, an exact eikonal of g0 (Proposition 2.2(c)). A profile is a smooth f(X, θ) on Ω ×
S¹; [f](X) := f(X, v(X)/λ); ⟨f⟩ is its θ-mean. Derivatives are measured in the λ-scaled norm |f|_j := Σ_(i≤j) λ^i ‖∂^i
f‖_(L²(Σ_τ)), in which an oscillation costs nothing: ∂_a [f] = λ⁻¹ (∂_a v)[∂_θ f] + [∂_a f]. For a profile G the
two-scale operator R[G] is Ric^H with ∂_a replaced by ∂_a + λ⁻¹ (∂_a v) ∂_θ; it contains no explicit θ (computed for a
generic profile, all fifteen components functions of (v, r, θ) and the phase, shifted by a symbolic c:
`docket68/n1star/checks/support9.py` S6), so

    R[G(·, · + c)](X, θ) = R[G](X, θ + c)   for every constant c.                                       (4.1)

**Stage 0 (computed, `docket68/n1star/lead5.py` L1–L5).** With W := W_TT + χ dv², the expansion
R[g0 + λW] = λ⁻¹ R^(−1) + R^(0) + O(λ) has R^(−1) = 0 (because g0⁻¹(dv, dv) = 0); the θ-mean of R^(0) vanishes exactly
under (2.6); with χ = 0 its oscillating part is a second harmonic in the vv component only; χ enters R^(0) only as
−(∂_r + 3/(2r)) ∂_θ χ in vv; and W(ℓ, ·) = 0, tr W = 0. So χ solves a transport along ℓ, smooth at the axes because ℓ
has no angular component, and R^(0) ≡ 0 identically in (X, θ).

**Higher stages (deduced; supplement 5.2–5.4).** The ansatz G = ḡ + λW + Σ_(j≥2) λ^j ĝ_j(X, θ), with mean metric ḡ = g0 +
Σ λ^j m_j and phase u = v + Σ λ^j φ_j, is solved order by order. Each order m ≥ 1 is a linear system with smooth
coefficients for the mean m_m (a wave equation), the phase correction φ_m (a transport, imposing that u stays an eikonal
of the mean metric to that order), the oscillating profile ĝ_(m+1) (a transport along ℓ) and □̃φ_m (a transport by
(2.4)); the system closes without loss and has a unique smooth solution on Ω for smooth data (its triangular structure at
order λ¹ computed in the eight components the symmetry leaves, the new unknowns' second derivatives entering only through
−½ □̃ on the mean, (ℓ · ∂)∂_θ on the next profile and the two transports, the profile after next absent,
`docket68/n1star/checks/stage5.py` S1; the higher orders by induction, deduced). Rewritten with the fixed phase v, the
profiles g_j satisfy (supplement 0.4):

- (E1) transversality: (g1 − ⟨g1⟩)(ℓ, ·) = 0;
- (E2) the leading equation: R^(0) ≡ 0 in (X, θ);
- (E3) the residual: |Ric^H(g_app)|_k ≤ C λ^(N−1).

**Theorem A (deduced, supplement section 5; read by independent verifiers, supplement section 7).** For every N and
every smooth choice of stage data there are profiles with (E1)–(E3), whose oscillating part of g1 is the waves of
section 2.4 with the second harmonic χ dv² and a phase shift, on the background (2.6).

---

## 5. Proof of the uniform existence theorem

This is the uniform existence statement: for λ ≤ λ0 the vacuum solution with the given
data exists on the fixed domain, and its remainder after the approximant obeys estimates uniform in λ, in a formulation
that loses no derivatives, is regular across the axes, and works on the large background. The supplement gives every
step; here is its structure, with the identities on which it turns.

### 5.1 The linearization and its one large coefficient

Let P(w) := (d/ds) Ric^H(g_app + s w)|_(s=0). From (2.7),

    P(w) = −(1/2) g_app^(ab) ∂_a ∂_b w + (1/2) λ⁻¹ s(w) [∂_θ² g1] + B·∂w + C·w,     s(w) := w(ℓ, ℓ),           (5.1)

with B, C bounded profiles: second derivatives of g_app, of size λ⁻¹, enter only through w^(ab) ∂_a v ∂_b v, which is
w(ℓ, ℓ) up to O(λ)|w| by (E1). So the only coefficient of size λ⁻¹ couples one scalar component of the remainder, s =
w(ℓ, ℓ), to the wave (computed: second derivatives of g enter Ric^H only through −½ g^ab ∂_a ∂_b g, exactly, and the
chain rule gives the rest, `docket68/n1star/checks/support5.py` C1). This is the five-dimensional form of the coupling
Touati describes (READ, [Tou23a] section 3.2.2, p. 20, "The quasi-linear coupling and the loss of derivatives").

**Lemma 5.1 (the phase-shift identity; deduced; computed on the stage-0 profile, support5.py C2).** Write P([Y]) = [λ⁻¹ T
Y + P_0 Y] for profiles Y, T and P_0 operators bounded on profiles (supplement 3.2). Under (E2), T(∂_θ g1) = λ T1 with T1
a bounded profile.

*Proof.* Differentiate (4.1) at c = 0 for G the profile of g_app: the linearization of R at G in the direction ∂_θ G
equals ∂_θ R[G]. The left side is T(∂_θ g1) + O(λ); the right side is ∂_θ(λ⁻¹ R^(−1) + R^(0)) + O(λ) = O(λ). ∎

A constant shift of the phase is a symmetry of the leading equation, so its generator ∂_θ g1 is annihilated by the λ⁻¹
part of the linearized operator. (A remark, used nowhere below: this one line is the analytic content of Touati's
transport and polarization conditions at first order.)

### 5.2 The decomposition and the regained derivative

Write w = h + φ [∂_θ g1], with φ(X) defined by the transport along the background generator

    L0 φ = −(1/2) 𝒫 s,     φ = 0 on Σ_τ0,                                                              (5.2)

where 𝒫 is a compactly supported mollifier at scale λ adapted to the annuli Σ_τ = {a ≤ |x| ≤ b(τ)}, b(τ) the outer radius
of Ω's slice at τ: the averaging ball is shifted 2λ inward near the outer sphere and outward near the inner one, so that
𝒫 maps functions on the annulus to functions on it, with the Bernstein- and Friedrichs-type bounds ‖∂_x 𝒫 f‖ ≤ C λ⁻¹ ‖f‖,
‖f − 𝒫 f‖ ≤ C λ ‖∂_x f‖ and ‖[m, 𝒫] ∂_x f‖ ≤ C ‖∂_x m‖_∞ ‖f‖ for smooth m (supplement Lemma 2.2, σ0 non-increasing; that
the shifted ball and the segment to it stay in the annulus is certified, `docket68/n1star/checks/support5.py` C4). It
replaces Touati's Fourier projector Π≤ ("a Fourier multiplier supported in { |ξ| ≤ 1/λ }", READ, [Tou23a] section 3.2.3,
p. 21), which needs no boundary.

By Lemma 5.1, the equation for h has bounded coefficients except one, λ⁻¹ ((1 − 𝒫) s) [∂_θ² g1], which is O(∂s) by the
mollifier bound (supplement (3.5)). Two derivatives of φ remain on its right side through □̃φ. Contracting the equation
with ℓ ⊗ ℓ kills every λ⁻¹ term and the □̃φ term exactly ([∂_θ g1](ℓ, ·) = 0), so s satisfies a wave equation with no
large coefficient (supplement Lemma 3.3; computed on the stage-0 profile with φ = φ(v, r, θ) generic, T²-invariant as in
the class, support5.py C3: the ℓ ⊗ ℓ component has no λ⁻¹ term and no second derivative of φ, while a wave with W(ℓ, ℓ) ≠
0 gives one; in all fifteen components the λ⁻¹ part is −(ℓ · ∂φ)[∂_θ² g1] + φ T(∂_θ g1), with nothing of lower order, and
φ's second derivatives enter only as −½ (□̃φ)[∂_θ g1], `checks/support5b.py` C10). And Ψ := □̃φ satisfies, by (2.4)
applied to (5.2),

    L0 Ψ − (2/r) Ψ = −(1/2) □̃ 𝒫 s − (1/r)(∂_τ + ∂_r) 𝒫 s − (3/r²) ∂_r φ,                                 (5.3)

a transport whose source is controlled by the wave equation for s (supplement Lemma 3.4). This is Touati's mechanism
(READ, [Tou23a] p. 20: "The main idea is to show that □_g F is better than ∂² F"), carried out with the exact
commutator (2.4) on the black-hole background.

### 5.3 The energy and the bootstrap

The energy is

    𝒩(τ) := Σ_(j≤6) λ^j (‖∂^j ∂h‖ + ‖∂^j Ψ‖ + ‖∂^j ∂φ‖ + λ ‖∂^j ∂_x² φ‖) + ‖h‖ + ‖φ‖,                    (5.4)

norms in L²(Σ_τ). It controls the remainder: |w|_7 ≤ C 𝒩 (its exponent ledger over the 128 classes of Leibniz terms of w
computed, `docket68/n1star/checks/support5c.py` C11). The energy inequality for −(1/2) g̃^(ab) ∂_a ∂_b u = f on Ω uses
the multiplier −g̃⁻¹ dτ; the lateral boundaries are spacelike with Ω to their past, so their fluxes have a sign and are
dropped (supplement Lemma 2.3). The transport estimate along L0 uses div x̂ = 3/r and the sign of the outer boundary's
motion (supplement Lemma 2.4). Assume 𝒩 ≤ 2 M λ^K on [τ0, τ*]. Then |w| ≤ C M λ^(K−3), |∂w| ≤ C M λ^(K−4), so g = g_app +
w stays in the class where the domain lemma (supplement Lemma 1.1(e)) holds. The nonlinear terms are at most C λ⁻⁵ 𝒩² ≤ C
M² λ^(2K−5) ≤ C M² λ^(K+1); the residual contributes C λ^K; every linear term is C 𝒩. Gronwall gives

    𝒩(τ) ≤ C3 ((C_D + 1 + C_R) λ^K + C M² λ^(K+1)),     C3 independent of M and λ,                         (5.5)

where C_R bounds the residual, |Ric^H(g_app)|_k ≤ C_R λ^K on [τ0, τ_end] ((E3), as N − 1 ≥ K), and C_D the data, the
datum's departure from the approximant's on Σ_τ0 being at most C_D λ^K in the norms of (5.4) (section 5.5); with M := C3
(C_D + 1 + C_R) + 1 and λ0 small the bootstrap closes at 𝒩 ≤ M λ^K. The smallness that closes it is a power of λ, never
the size of the data or of the background; this is the decision on which the estimate turns, and one in which it departs
from Touati's (READ, [Tou23a] p. 12, Theorem 2.2, "There exists λ 0 > 0 and ε 0 = ε 0 (δ, R) > 0 such that if 0 < ε ≤ ε
0").

### 5.4 Existence, continuation and the time lines

The local theory needs the time lines timelike as well as the slices spacelike (READ: [AO14] Theorem 1.1 under (1.3), p.
2, "A^00(U) ≤ −κ" for the slices and "1/γ |ξ|² ≤ A^ij ξ_i ξ_j" for the time lines; [DS23] (A4), eigenvalues that "do not
meet each other"). Inside the horizon the lines of constant x are spacelike (Proposition 2.2(d)), so the local theorems
are applied in other coordinates: the coefficients are extended beyond Ω by a universal extension operator and convex
interpolation of lapse, shift and spatial metric to Minkowski's; the slices are kept and the time lines are taken along Z
= ∂_τ − β (β the shift), for which g(Z, Z) = −N² < 0 and, in coordinates with these time lines, g^ij is the inverse
spatial metric (computed, support5.py C6); the system is posed on a large torus with its coefficients clamped in time
outside [τ0 − 2, τ_end + 2] (τ_end the last time of Ω); and written as a symmetric hyperbolic first-order system it
satisfies (A1)–(A4) of [DS23] (its symmetry and positivity, A⁰ symmetric positive definite and each A^k symmetric,
computed exactly at admissible points, `docket68/n1star/checks/support5c.py` C12). Restarts use [DS23] Theorem 2.4
("there exists some T > 0 depending on ||u0||_r and M̃ such that (1.1) has a unique solution"), with data extended by the
universal operator of [LY22] Theorem 26; uniqueness and finite speed on Ω come from the energy inequality itself. With
(5.5) the solution continues across Ω (supplement section 4, Step 8).

### 5.5 The data: the constraints solved outward in r

Touati constructs his data by the conformal method, inverting flat elliptic operators, and closes each fixed point by
the smallness of the background (READ, [Tou23b] section 5.4.2, p. 29: "taking ε small enough ensures that Ψ is a
contraction", with (2.1), "‖g0 − e‖_(H^(N+1)_δ) + ‖K0‖_(H^N_(δ+1)) ≤ ε"). On Σ_τ0 the background passes through the
hole, and an elliptic method would need boundary data at r = a as well as far out. We solve the constraints instead
as an evolution in r, following Rácz (READ, [Rac16] p. 6, on (3.3): "Notice that the coefficients of ∂ρ and ∂K are
symmetric, and that the coefficient of ∂ρ is also positive definite"), from a sphere inside the shell where the
approximant's data are the seed's exactly, imposing nothing further out.

Correct the approximant's data (γ, κ) by U = (α, ϖ, q) (the programs' a, w, q): γ + α dr², κ + ϖ Π + q ⊗ dr + dr ⊗ q (Π
the metric of the spheres). The constraint map (J, ρ) = (2(−div κ + d tr κ), R − |κ|² + (tr κ)²) (READ, [CD03] (2.1), p.
4: "These are the general relativistic constraint equations whatever the space-dimension n") then has, at the
background's data (computed, `paper/response5.py` R5; `docket68/n1star/data5.py` S2–S4, S6):

    ρ:   (3 r³/(r² + μ)²) ∂_r α − (1/(r² + μ)) ∂_θ² α + …,
         3 r³/(r² + μ)² = ϑ³ H,   ϑ² = r²/(r² + μ),   H = 3/√(r² + μ),
    J_r: 6 ∂_r ϖ − (2/r²) ∂_θ q + …,     J_θ: −(2 r²/(r² + μ)) ∂_r q + 4 ∂_θ ϖ + …,                        (5.6)

so ρ is forward parabolic in r for every r > 0 (no ∂_r² α, no ∂_r ∂_θ α, no derivative of (ϖ, q)), and J is symmetric
hyperbolic in (ϖ, q) with r as time (θ here the angle of S³): the symmetrizer S = diag(1, −1/(2r²)) gives S A0 = diag(6,
1/(r² + μ)) > 0 and S A^θ symmetric, with real speeds c² = 2(r² + μ)/(3 r⁴). At the approximant's data there is no
coefficient of order λ⁻¹ (data5.py S2, S4), because the waves have zero trace on the spheres; an oscillating trace would
produce one (the instrument's mutants). The linear system is solved by a Faedo–Galerkin scheme on the eigenspaces of the
Laplacian of S³ with λ-uniform estimates (supplement Lemma 6.4), the nonlinear one by the Kato–Majda scheme, bounded in a
high norm and contracting in a low one (READ: [AO14] section 4.1; [AG22] abstract, p. 1, "the boundedness in the high
norm and contraction in the low norm"), with no smallness; the correction is O(λ^(N−2)) in every angular Sobolev norm,
each r-derivative costing a factor λ⁻¹ (supplement Proposition 6.5). Computed, on the stage-0 approximant's data
(`docket68/n1star/checks/csolve5.py`): the linear and the quadratic part of the constraint map have no coefficient of
order 1/λ (exact; the quadratic part's absence is new, so the remainder's coefficients are O(1) here, not merely O(1/λ));
the linear solve, a pseudo-spectral discretisation on the symmetric class marched in r with a source of size λ⁴ (N = 6),
gives sup_r of the H²-type norms of U, ∂_r U and ∂_r² U scaling as λ^4.00, λ^3.99 and λ^3.00 over the last halving, λ =
1/32 to 1/64 (floating point; the earlier halvings pre-asymptotic; resolution varied by M = 12, 16, 20 modes and λ/32,
λ/64 steps, the norms moving by 7 × 10⁻⁵), the solve uniform in λ and the first r-derivative costing nothing, both within
the λ^(N−2−j) stated (control: the mutant with an oscillating trace on the spheres, which has a 1/λ coefficient, makes
the first r-derivative cost λ⁻¹); and the scheme of the proof, principal coefficients frozen, contracts with first ratio
d_1/d_0 = 6.8 × 10⁻³, 5.8 × 10⁻⁴ and 3.5 × 10⁻⁵ at λ = 1/8, 1/16 and 1/32 (d_i the successive differences; at λ = 1/32
the next difference already sits at roundoff), falling at rates 3.55 and 4.03, at least the proof's λ^(N−3), its first
correction falling as λ^(N−2) (rates 3.76, 3.97); with a 1/λ quadratic coefficient of nonzero phase mean put in, the
first correction falls an order slower (rates 2.96, 3.15) and the check rejects it (`checks/csolve5.py` C7c, floating
point). Beforehand the approximant's stage data are chosen so that its data satisfy the constraints and D = 0 to order N
− 2, by a hierarchy that propagates the gauge order by order (supplement Lemmas 6.1–6.2; computed: the identity (6.2)
exactly at a point of a random 4+1 metric, and the first step, D^(1) = 0 on the slice under Lemma 6.2's stage-1 choices
with m1 kept generic, its mean solved by a determinant −(r² + μ)⁵/(2r¹⁰) ≠ 0, `docket68/n1star/checks/gauge5.py` G1–G2;
the later orders by the same induction, deduced).

---

## 6. The remaining parts

**The boundary.** Proposition 3.2: x_K = 1 is spacelike for the limit wherever μ > √72 l5² or μ' > 0, and for g_λ when μ0
> √72 l5² and C λ ≤ δ/2; every future causal curve that meets it leaves D_T there. Exact for g0 (computed R6, and
`docket68/lemmas/hf_theorem5.py` F2, there also machine-checked with Z3); deduced for g_λ, its first-order term computed:
−(χ + m1(♯dΦ, ♯dΦ)) with ♯dΦ = g0⁻¹ dΦ, the wave W_TT dropping out exactly (support5.py C8).

**The horizon.** Proposition 3.3 and item 6 of Theorem 1: for g_λ with μ0 > √72 l5² and λ ≤ λ_H, each column carries at
most one zero of the outgoing expansion of the spheres {v, r = const}, exactly one within C λ of √μ on the columns that
reach across it, trapped spheres below and untrapped above; no inner zero (deduced). The per-column zero set is not
itself a marginally trapped surface; the statement is about the round family, as the numerical solver's is:
`docket68/lemmas/hf_core5.py` evolves the metric of the class in the Bondi form (3.2) from the free data of section 2.4
and reads each quantity on the same spheres. Although ∂g_λ converges only weakly, the expansion of these spheres does not
see the oscillation at leading order, because the wave is traceless on them and the phase is constant along each column.
It agrees (`docket68/lemmas/hf_theorem5.py` F4: the horizon's departure halves with λ, ratios 2.47, 2.26, 2.14 at μ0/l5²
= 100 and 2.26, 2.14 at 1000).

**The mean mass.** Proposition 3.4 and item 7 of Theorem 1: after the shell, the mass of every sphere of the domain is
the limit's to O(λ²) (deduced) — the mass of the spheres {v, r = const}, not the solver's mass aspect at past null
infinity. The first-order mean correction m1 need not vanish (in the Bondi-type gauge its source, a tilt of the dust's
direction at O(λ), is computed in `docket68/n1star/ansatz5.py` A5), but it is odd under the quarter-turn symmetry, and a
rotation-invariant mass cannot see it. The solver measures a different quantity, the mean mass aspect at past null
infinity: its largest offset from μ after the shell (v ≥ 3.75) quarters at each halving of λ (hf_theorem5.py F4: ratios
5.17, 4.01, 4.02 at μ0/l5² = 100 and 4.00, 4.02 at 1000), and its law is computed and proved in the next paragraph.

**The mean mass at past null infinity.** By Theorem 2 the waves' field at past null infinity is exactly λ[W_TT]. The
sphere mean of its flux density, in the normalization of Proposition 2.3, is exactly

    (2/9) A² [env² + λ² env'² − ½ (env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ)]                          (6.1)

(computed, `past5.py` P7). Its integral in v is μ(v) − μ0 plus terms that oscillate with amplitude (λ/18) A² env² while
the shell passes; after the shell it exceeds μ − μ0 by exactly (2/9) λ² A² ∫ env'² + O(λ³). By Theorem 3 this is the law
the Bondi mass of g_λ obeys: the pointwise rate (3.3) of the mass aspect is (4/3)(∂_v p1² + ∂_v p1 ∂_v p2 + ∂_v p2²),
whose sphere mean is (6.1), so μ_B(v) − μ0 is that integral, and after the shell μ_B − μ(v_end) = (2/9) λ² A² ∫ env'² +
O(λ³). The numerical solver evolves the metric in the Bondi form (3.2) from the same free data and fixes the rate of its
mass aspect by the same equation, so its mean mass is μ_B as it integrates it: for its envelope sin⁴(π(v − ½)/3) on [½,
7/2] with A = 1 the coefficient is (2/9) ∫ env'² = 5π²/108 = 0.45693, and the solver's offset over λ² after the shell is
0.4589, 0.4577, 0.4568 at λ = 0.05, 0.025, 0.0125 (μ0 = 100 l5²) and 0.4578, 0.4569 at λ = 0.025, 0.0125 (1000 l5²), each
the mean over the samples after the shell (computed, `bondi5.py` B4, which checks agreement to 0.5 %; F4's ratios above
take the largest offset over the same samples). At λ = 0.0125 the agreement is within 0.05 %. The one finer run, λ =
0.00625 at μ0 = 100 l5², gives 0.4535, 0.74 % below, on the previous run's grid, which the solver's anchor check records
as grid-limited (`docket68/lemmas/hf_anchor5.py`); and the rows at 1000 l5² reproduce those at 100 l5² to about 10⁻⁴, the
far region not depending on the inner cut, so they are not an independent check. What the comparison tests is the law
against the solver's own integration of it; what Theorem 3 proves is that g_λ obeys it.

---

## 7. Relation to Huneau and Luk, Touati, and Luk and Rodnianski

Point by point; HL is [HL18], T is [Tou23a], LR is [LR20], and "here" is this paper.

- **Dimension and symmetry.** HL: 3+1, polarized U(1), a translation with no axis. T: 3+1, none. LR: 3+1, none. Here:
  4+1, T² with both reflections, rotations with two axes.
- **Reduced system.** HL: 2+1 gravity with one free wave φ, their (1.3). T, LR: none. Here: 2+1 gravity with two free
  waves on the target (3/2) dψ² + 2 dω² (Proposition 2.1), identified, and not used in the proof.
- **Gauge.** HL: elliptic (maximal slices, conformally flat). T: generalised wave. LR: double null. Here: the wave-map
  gauge relative to the limit g0.
- **Background.** HL: small, near Minkowski (the smallness condition of Theorem 4.2). T: small, (2.9), with an
  asymptotically planar phase, (2.10). LR: large and angularly regular, on a double null domain short in one null
  direction (u̲* ≤ ε, ε depending on the bound C of the data, their Theorem 1.9). Here: five-dimensional Vaidya with a
  black hole; no smallness of μ0, A or env.
- **Dusts.** HL: any finite number, angularly separated, with generic data. T: one. LR: two, measure-valued; their
  reverse statement, the counterpart of Huneau and Luk's theorem, is their Corollary 1.14, local. Here: one.
- **Data.** HL: admissible free data on a maximal slice. T: the conformal method of [Tou23b]. LR: characteristic. Here:
  Cauchy data on Σ_τ0, the constraints solved outward in r.
- **Domain.** HL: [0, 1] × R². T: [0, 1] × R³. LR: [0, u*] × [0, u̲*] × S². Here: Ω ⊃ D_T ∩ {τ ≥ τ0}, through the
  horizon to a spacelike boundary.
- **What closes the estimates.** HL: the smallness ε. T: the smallness ε, with λ ≤ λ0 as well (READ, [Tou23a] Proposition
  7.1, p. 13). LR: angular regularity on a domain short in one null direction. Here: powers of λ, with the approximant
  carried to any order.
- **The derivative loss.** HL: elliptic estimates for the metric. T: a null foliation and a Fourier cut-off. LR: angular
  regularity. Here: the phase-shift identity, the exact commutator (2.4) and a compact mollifier.
- **Conclusion.** HL: uniform convergence, weak L² convergence of derivatives, ∂ in L∞ uniformly. T: g_λ = g0 + λ g(1) +
  … in generalised wave gauge. LR: C⁰ and weak W^(1,2). Here: uniform at O(λ), ∂g bounded, weak L².

**What carries over.** The reduction to a 2+1 system with free waves on a flat, positive-definite target, which here
is two copies of Huneau and Luk's scalar (Proposition 2.1); the geometric-optics construction around an eikonal phase
of the limit; the weak limit as null dust with Isaacson's flux; the time interval fixed in advance.

**What changes.** One more dimension; a T²-mirror class whose orbits degenerate on two axes, so that the reduced system
cannot be used there; a large black-hole background in place of small data, so that the trapped region and a spacelike
inner boundary are inside the domain; Cauchy data before the shell reaches the hole, and by Theorem 2 data at past null
infinity, which none of the three poses, rather than on a maximal slice or characteristic hypersurfaces; one family of
dust, not many.

**What the proof needed beyond theirs.** (1) An approximant of every order (Theorem A), so that the nonlinear terms
are beaten by λ and only a linear estimate on the large background must be uniform; (2) the phase-shift identity
(Lemma 5.1), which removes the one large coefficient of that linear problem; (3) the exact commutator (2.4) on
five-dimensional Vaidya, in which the mass drops out; (4) a compactly supported mollifier adapted to a domain with
boundary, in place of a Fourier projector; (5) a domain inside the horizon whose time lines are spacelike, handled by
changing only the independent variables to lines along Z; (6) the constraints solved as a parabolic–hyperbolic
evolution in r with no smallness and no data imposed far out; (7) a gauge hierarchy making D vanish to every order.

---

## 8. Settling at late times

### 8.1 The question

The theorem holds on D_T for each fixed T; Huneau and Luk's theorem, Touati's and Luk and Rodnianski's hold on a fixed
interval too. Settling for all later v is the nonlinear stability of five-dimensional Schwarzschild–Tangherlini within
the class. What is known, READ: linear stability against every type of perturbation, "higher-dimensional Schwarzschild
black holes are stable with respect to all tensorial types of linear perturbations" ([IK03] p. 16); and nonlinear
asymptotic stability, "the evolution of (SU (2) × U (1))-symmetric vacuum perturbations of initial data for the
five-dimensional Schwarzschild metric finally converges in a suitable sense to a member of the Schwarzschild family"
([Hol08] p. 1, Theorem 1.1 pp. 5–6), in a class where the Einstein equations reduce to 1+1 dimensions. That class shares
our T² but not the reflections: its squashing is a dφ1 dφ2 term, which (2.1) excludes, so the two classes meet only in
spherical symmetry (computed: the squashing's dφ1 dφ2 coefficient is 2c²s²(e^(−4B) − e^(2B)), zero only at B = 0,
`docket68/n1star/checks/support8.py` K8). The waves here, which depend on the angle θ, lie outside it in any case. After
the shell the oscillating profiles vanish (supplement section 10.50(a), deduced; its base computed, `support8.py` K1, and
the source terms of stages 2–6 as Lemma 5.1's rule enumerates them, each carrying the envelope or an earlier profile,
`checks/ledger5.py` L4; that the rule produces every term is deduced) and only the mean corrections remain: on Ω ∩ {v ≥
v_end}, g_λ differs from Tangherlini of the final mass by λ m1 + O(λ²) with its first derivatives (Theorem 1, items 3–4).
Settling would therefore follow from the small-data stability of Tangherlini in the T²-mirror class, once the solution is
also constructed outside D_T. Sections 8.2–8.8 take up the first step. The second, continuing g_λ outside D_T, is
replaced by a gluing (section 8.7), and Theorem 4 is not shown to apply to g_λ's own data.

### 8.2 The linear level

The linear statement is proved (supplement `proof5/PART-VIII-LINEAR.md`, Theorem 2.2 and Corollary 2.3), in the gauge of
the nonlinear problem. Every solution of the linearised constraint equations in Hintz's data class (section 8.8) has a
linearised vacuum development in his generalised wave gauge. Up to a linearised boost it takes those data, and where the
late-time cut-off is 1 it differs from a linearised Myers–Perry metric by O(t*^(−2−ε)) in spatially compact subsets of
the exterior, for each ε < ε_K. In the class the boost vanishes and the Myers–Perry change is a change of mass alone. The
proof is Theorem 4's linearisation at the Tangherlini data: the linear initial-value problem near Hintz's initial
surface, the right inverse of the linearised operator at the zero perturbation, and the Bianchi identity linearised at a
Ricci-flat metric. It needs no new estimate. A linearised vacuum solution given in another gauge, such as the two below,
with the same data up to those of a linearised diffeomorphism, differs from this one by a linearised diffeomorphism L_X g
on its Cauchy development, X unique up to Killing fields (verified, not proved by the standard of section 8.8: supplement
`proof5/PART-IX-GAUGE.md`, Theorem 2.2 and Corollary 2.3). Nothing is asserted about the size or decay of X, so the decay
of such a solution in its own gauge is that of L_X g there. The rest of this section is the route by which the linear
level was first reached, in those gauges and by deduction; it stands beside the proof as an independent route.

Linearly more is known, and it applies to the class: the class carries no vector-type perturbation and no linearised
rotation (computed, `docket68/n1star/settle5.py` T1), and for the other two types the gauge-invariant master quantities
on five-dimensional Tangherlini decay, "in spacetime dimension six and below, the uniform decay estimate Ě^N_Ψ(Σ_τ) ≤
C(n, M) I_Ψ(Σ_0)/τ²" ([HKW18] p. 4, Theorem 2), the part with l < 2 being pure gauge plus a linearised Myers–Perry
solution (Theorem 1, p. 3), which in the class is a change of mass alone. The decay of the metric components themselves
is left open there: "We do not treat this matter in the current paper" (p. 4). In the class it follows from what is
written (supplement Proposition 10.1, deduced): for every scalar mode l ≥ 2 the gauge f_a = 0 = H_T of [KI03] exists, and
in it the metric components are [KI03]'s (3.14), the master field normalised as r^(3/2) Φ and its derivatives to order
two — two orbit-space derivatives, and a factor l(l + 2) − 3 through the trace — with coefficients bounded on r ≥ r_h
uniformly in l (computed: `docket68/n1star/checks/kirecon5.py` P1, every coefficient a sum of monomials H^a r^b with a, b
≤ 0 but the factor m/(6r²) of the trace). That normalisation is not one [HKW18] bound: their r^p energies are of Φ itself
((124), p. 43; (127), p. 46), and their scalar master quantity, r^(1/2) Φ times a tensor harmonic ((173), pp. 60–61), has
pointwise norm r^(−3/2)|Φ|; in those fields the coefficients grow as r^(3/2) and r³, uniformly in l, those powers
attained (computed, kirecon5.py P2); the tensor type is its own master field; and l = 1 is absent. So in that
Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation in the
class settles to a change of mass at [HKW18]'s rate on each region r ≤ R, uniformly in l with a constant growing as a
power of R (uniformly in r it is not shown), with the loss of two derivatives so counted. That gauge is not the wave
gauge of the nonlinear problem. The passage between the two was closed in four dimensions by Hung ([Hun19]: the
Lichnerowicz equation under the gauge, a gauge vector solving a tensorial wave equation with the master quantity as
source, the l = 0 sector's stationary one-form and linearly growing gauge-fixed mass change, decay for the rest), and its
five-dimensional structure is computed in the class (supplement Proposition 10.2, `docket68/n1star/wavegauge5.py`): the
tensor type is already in harmonic gauge, the scalar gauge vector solves three 1+1 wave equations per mode with the
master field as source, and the l = 0 sector's two non-decaying solutions are explicit and regular at the horizon; the
decay estimate for that system, Hung's sections 5–8 in five dimensions, does not exist in the literature and is deduced
below, not proved; the system is triangular (supplement Proposition 10.2(v)), each rung a scalar wave equation on
Tangherlini whose potential obeys the positivity condition Hung's method needs; the estimate is a route of known tools
rung by rung, with four things that had to be carried out rather than quoted (the Morawetz currents for the rungs, the
r^p weights, the l = 0 argument and Hung's Proposition 4.2 in five dimensions), all four carried out below. The last of
the four is computed (supplement Proposition 10.2(vi), W7): in Hung's components, with the harmonic gauge condition
admixed as he does it, the system is □H = AH + UH with U along the horizon generator in two rows only, the leading matrix
has the eigenvalues (l+a)(l+a+2) for a = −2, …, 2 where his has (l+a)(l+a+1), and the horizon-regular rows carry the
positive coefficients 2f′ and f′ in place of his 4M/r² and 2M/r²; the four-dimensional control
(`docket68/n1star/hung4.py`) reproduces his printed rows from the Schwarzschild metric. On that structure his Proposition
4.1 — the red-shift and r^p estimates for the metric itself, with the compact region between them as the only error — is
deduced in five dimensions (supplement Proposition 10.3, `wavegauge5.py` W8; constants not tracked): the energy of the
harmonic-gauge perturbation at every later time and in the bulk is bounded by its initial value and by the perturbation
on a compact region [r_rs, R + r_h], with [Sch13]'s weights at null infinity, where the five-dimensional radiation
field's potential is coercive at every l ≥ 2 (its leading eigenvalues are (l+a+1/2)(l+a+3/2) ≥ 3/4, so no Hardy
inequality is needed where Hung's l = 2 needs one), and the red-shift at r_h, where the identity acquires two terms
absent in four dimensions, both absorbed. It is not a decay statement: the compact region is where the master quantities
and the gauge vector enter. The gauge vector's rungs are done next (supplement Propositions 10.4–10.5, `rungs5.py`): each
rung is a scalar wave equation with a potential, 0 or the Maxwell potential −4μ/r⁴, and a source from the rungs below,
and the one input of Hung, Keller and Wang's chain that depends on the potential, the Morawetz multiplier, is computed
for it — their own n = 3 choice serves both potentials, with half the angular term lent to the bulk coefficient, which is
then positive on the whole exterior by a Sturm count — so every rung has the estimates of Hung's Appendix A in five
dimensions for a source in the norm those estimates take. The sources the rungs carry are not in that norm; Hung's
substitutions that bring them into it — the first rung taken as tr h, which solves the homogeneous wave equation, and the
master field's bad terms removed by corrections carrying the factor u + r — are computed in five dimensions term by term
in his shape, every residual weight checked (supplement section 10.7, `growing5.py`), and the identities of his l = 0
argument likewise (section 10.8, `lzero5.py`); of the two estimates the route then owed, the rapid decay of the first
rungs is deduced in five dimensions for every mode of the class but the spherically symmetric one by Hung's own argument,
with his conditions on the potential computed (supplement section 10.9, `hierarchy5.py`), and found obstructed for the
spherically symmetric mode, where the radiation field carries a potential his argument needs to vanish; the coupled
estimate for the last two components is carried into five dimensions likewise (supplement section 10.10, `coupled5.py`),
where its Morawetz bulk needs none of Hung's substitutions for its positivity because the lowest mode of the class is
already definite, so that every mode but the spherically symmetric one decays by his route, deduced; and the spherically
symmetric mode is taken by another route (supplement section 10.11, `lzerorate5.py`): the same commutation, its negative
potential absorbed by a Hardy inequality on each outgoing null leaf for p < 1, with Schlue's Morawetz estimate at l = 0
[Sch13], gives the decay Hung's l = 0 argument needs at a rate one power weaker, so that the spherically symmetric part
settles to a change of mass and a stationary gauge mode, deduced: every mode of the class is carried.

No growing mode appears in either type for l = 2, …, 10 to τ = 275 r_h (settle5.py T5; a finite-time observation), and
the late-time tail of the l = 2 master fields, measured from the pulse's launch, is t^(−7.05) (tensor) and t^(−7.06)
(scalar) on [550, 700] r_h, the same at half the step, approaching 7 from above with that origin and bracketing 7 (6.89,
7.23) when the origin is shifted by the launch radius either way (T6): [CYDL03]'s t^(−(2l+D−2)) for odd D, the flat
five-dimensional Green's function's tail; the nonlinear rate of Theorem 4 is t*^(−2−ε). The least-damped of the modes
[CLY03b] tabulates (l ≤ 4) is the scalar-type one with l = 2, σ r_h = 0.9477 − 0.2561i in this paper's e^(−iσt)
convention (READ: [CLY03b] Table 1, p. 8, which prints +0.2561i in its e^(iωt) convention), which evolving the master
equation in time reproduces to 1% (settle5.py T3, on the barrier of `docket68/lemmas/seed_escape.py`): an e-folding time
of 3.905 r_h. The reduced problem in the class is 2+1-dimensional, the dimension of Klainerman and Szeftel's polarized
axisymmetric stability of four-dimensional Schwarzschild ([HKW18] p. 2); their method is not carried into five dimensions
here: the class is settled by Hintz's route instead (sections 8.3–8.4, Theorem 4).

### 8.3 Hintz's route: the five-dimensional inputs

The nonlinear route through Hintz's generalized wave map gauge [Hin26] needs a strongly damped constraint propagation
operator: mode stability, invertibility at zero energy on weighted spaces, no indicial root with real part in [−C₀, 1),
and its tf-admissibility ([Hin26] Theorem 7.1(1)–(4) and (1.43), p. 29). The indicial condition sees only the Minkowski
model at infinity and is computed in five dimensions (supplement section 10.12, `damping5.py`): Hintz's constraint
damping [Hin26a], with the trace weight 2/(D − 2) in place of his 1 — his 1 transcribed literally puts a root in (0, 1) —
has, at a point below the five-dimensional bound of his Lemma 4.4 with h < e chosen here (supplement section 10.13,
`semiclass5.py`, which recomputes the semiclassical inputs of his proof), no indicial root of the model with real part in
[−100, 19/10], and in [−100, 2] only the Coulomb root r^−2, exactly; the transfer to Tangherlini is deduced. A damping
1-form of his kind exists on five-dimensional Tangherlini, explicitly, its conditions holding at that point by
computation, two of them near infinity, and its smoothing at the joins, by his arguments (supplement section 10.14,
`cform5.py`). The gauge potential operator, the other 1-form operator of the route, has on Tangherlini, unmodified (E^Υ =
0), the zero energy structure of Hintz's Kerr case: its zero energy kernel is a single Coulomb-type state, a functional
at the horizon annihilates its range, and the pairings his horizon modification needs are 4π² where his are 4π
(supplement section 10.15, `gaugepot5.py`; computed, the kernel deduced by an energy identity); and it has no mode at
nonzero frequency in the closed upper half plane — the input Hintz's Proposition 6.9 takes, on Kerr, from a separate
theorem — by the master equations of scalar waves and of both Maxwell types, whose potentials on Tangherlini are positive
at every l ≥ 1, the spherically symmetric Maxwell sector being settled by its own equation ([KI03b]; supplement section
10.16, `modes5.py`; computed, the mode stability deduced for modes smooth across the horizon and outgoing at infinity).
At high energies its trapping input carries over: at the photon sphere r² = 2μ Hintz's frame has the same nilpotent
connection along the null flow, so the operator is strongly trapping admissible (supplement section 10.17, `trap5.py`;
computed, the admissibility deduced); and the horizon and outgoing thresholds [Hin26c]'s estimates need are his: the
endomorphism at infinity has his spectrum, and the horizon threshold is 3/2, also under the horizon modification of
supplement section 10.15 (supplement section 10.18, `thresh5.py`; computed, the thresholds deduced). The remaining inputs
follow — at the incoming radial set the threshold is the mirror of the outgoing one, −1/2 − S̄ against −1/2 + S̄ (deduced
from a computed similarity), and at the photon sphere the gap is half the expansion rate per unit time and the
semiclassical loss as small as wished — so that, on the reading that [Hin26c]'s spectral theory — set up for scalar
operators in general dimension, its main theorems stated in three — carries over to operators on bundles in four, the
operator's spectral family is invertible at large frequency and, for small modifications, at every nonzero frequency in
the closed upper half plane: Hintz's Propositions 6.5 and 6.9 in five dimensions (supplement section 10.19,
`hienergy5.py`; computed, the threshold and the propositions deduced). The low-energy theory carries over in the same
way, on a reading widened to [Hin26c]'s zero energy and uniform low-energy theorems at n = 4 — the transition face is the
Helmholtz operator, whose outgoing solutions are excluded exactly for weights below n − 2 = 2, and the weights shift by
n/2 — so that, with the horizon modification of supplement section 10.15, the operator is mode stable on the whole closed
upper half plane: Hintz's Proposition 6.12 in five dimensions (supplement section 10.20, `lowenergy5.py`; computed, the
proposition deduced). Hintz's deduction of the constraint propagation operator's mode stability from his semiclassical
solvability theorem carries over as well — its endomorphism at infinity is his with three angular copies, all positive; a
mode's data lie in ρ^(−2−ε) for the volume r³, half an order below his; and the weights become α_sf = −C₀ − 5/2 and ℓ ∈
[−C₀ − 2, 0) — so that his Theorem 6.2 holds there, on his Theorem 5.2 and at the parameter point as section 8.5 takes
them up, with the horizon threshold computed in supplement section 10.79 (`hthresh5.py`: every h in (0, h_2), h_2 ≈ 2.6 ×
10⁻⁵) (supplement section 10.21, `cpmodes5.py`; computed, the theorem deduced). The inputs of that theorem carry over too
— Tangherlini is a three-body scattering metric with two powers of decay to spare, the time functions of his energy
estimates near the initial surface and inside the black hole are timelike, and the positivity of the constraint damping
1-form holds at these weights — so that it holds in five dimensions on the reading that his 3b-analysis does (supplement
section 10.22, `solv5.py`; computed, the theorem deduced). His transition face problem — the dilation-invariant model of
the operator on Minkowski space, his Theorem B.1 — carries over in the same way: the model is homogeneous of degree −2,
its weights at the origin move by a half to β ∈ (0, 2 + C₀], the thresholds at the cone face and at the sink, α_cf > 1/2
and α_sf < −1/2 in his, become α_cf > 0.0066 and α_sf < −0.0066 at the parameter point (0 and 0 as e → 0), his choice of
weights and his closing argument go through unchanged, and his index-0 argument carries with the free operator's roots,
so that on the same readings, at that point, for C₀ ≤ 100 and provided the point's h lies below h₀, the constraint
propagation operator is tf-admissible for every weight in [−C₀, 2), [Hin26] Theorem 7.1(4) with its top at the Coulomb
root 2 where his is at 1 (supplement section 10.23, `tface5.py`; computed, the theorems deduced). The indicial roots of
the linearized gauge-fixed Einstein operator itself, his Lemma 8.4, carry over, at that point, for every harmonic degree
l: on each harmonic type its determinant is that of the gauge potential operator shifted by one and that of the
constraint propagation operator shifted by minus one, times the physical factor with roots −l and l + 2, his −l and l +
1, the mass at the Coulomb root 2, over a factor at l ≤ 1 that removes the roots counted twice; no root has real part in
(0, 1], so that the gap begins at 0 as his does and reaches past 1; and the roots of each type, the tensor type included,
which four dimensions lacks, split evenly — so that his Lemma 8.5 holds, and his Proposition 8.6, tf-admissibility with a
weight in the gap for a small gauge parameter, on the same readings (supplement section 10.24, `lin5.py`; the
factorization computed for every l, the roots at the parameter point for l ≤ 12, the rest deduced). The one threshold
that it needs beyond them, the minimum of the endomorphism in his Lemma 8.2, is 0 in five dimensions as in four: that
endomorphism carries the gauge potential and constraint propagation operators' spectra and five zeros, so that the decay
improves to 3/2 − ε where his improves to 1 − ε (supplement section 10.25, `sbar5.py`; the spectrum computed, the
improvement deduced). And the operator is strongly trapping admissible at the photon sphere, his Proposition 8.3: its
subprincipal matrix there, 15 × 15 where his is 10 × 10 — his printed matrix recomputed exactly in four dimensions, with
his sign convention, as the control — has ten zero eigenvalues and five of one sign fixed by the damping 1-form being
past timelike, and is triangular in a fixed basis, the rotation of the angular plane along the flow absorbed by weighting
its pairs alike (supplement section 10.26, `strap5.py`; computed, the proposition deduced). Its spectral family has no
mode at nonzero frequency in the closed upper half plane, his Proposition 8.8: the one input he takes from the mode
stability of the linearized Einstein equations on Kerr is, on Tangherlini, the Kodama–Ishibashi reduction, here computed
from the linearized Ricci operator itself for every harmonic — each type at l ≥ 2 reduced to one master equation whose
potential is positive, the tensor type, which four dimensions lacks, with the scalar wave's, and l ≤ 1 pure gauge — so
that every mode of the linearized Einstein operator smooth across the horizon and outgoing at infinity is pure gauge
(supplement section 10.27, `gmodes5.py`; computed, the proposition deduced on the same readings, the kernel elements'
class deduced in section 8.5; the continuation and the uniqueness inside the horizon by a lemma proved in supplement
section 10.76). And the zero energy states he builds from the Minkowskian translations, boosts and rotations, with the
linearized Kerr metrics put into his gauge, his Proposition 8.9, have five-dimensional counterparts one order faster in
1/r and without his two logarithms: Tangherlini meets Minkowski at μ/r², the rotations are Killing, the rotating metrics
— the derivatives at zero rotation of the five-dimensional Myers–Perry family [ER08], checked — have their gauge source
from the gauge modification alone, and the exponents the constructions need, 1 and 2, miss the five-dimensional indicial
roots once that modification is on (supplement section 10.28, `zstates5.py`; the orders and exponents computed, the
propositions deduced on the five-dimensional form of his Lemma 6.13, itself deduced in supplement section 10.29 on the
reading of [Hin26c]'s section 9 taken up in section 8.5). There, too, the first three of his generalized zero energy
states — on the time translation, on the boosts carried to second order in time, and on the rotations — have
five-dimensional counterparts with exact leading terms: his rotation coefficients (1 ± γ/2)/4 become (1 ± 2γ/5)/4, each
of the six rotations gives such a state, and the time translation's state carries no logarithm (`genstates5.py`; the
leading terms computed, his four-dimensional numbers reproduced as the control, the lemma and the states deduced). And
the four remaining classes — the pure gauge states whose gauge potentials carry no symmetry, built on the gauge potential
operator's growing roots — carry over with his ranges, every stationary correction one order faster in 1/r and no
logarithm in their leading terms once the gauge modification is on (`puregauge5.py`; the leading terms computed exactly,
his four-dimensional indicial matrices reproduced entry by entry as the control, the proposition deduced in supplement
section 10.30). The dual states of the constraint propagation operator, whose symmetric gradients enter the cokernel of
the linearized gauge-fixed operator in his section 8.4, carry over too, on the readings supplement section 10.21 rests
on: eleven in five dimensions against his seven, the translations' one order faster in 1/r, and near zero rotation two of
the six rotations' stay Killing at first order, the other four carrying his (7.18) ratios (`dual5.py`; computed at first
order in the rotation, his four-dimensional values reproduced as the control, his Lemma 7.2 and Proposition 7.3 deduced
in supplement section 10.31). At every spin his Lemma 7.5 is an identity of the Myers–Perry family: written in
Kerr–Schild form for every spin matrix A in so(4) at once, the deformation tensor of a rotation is the family's
derivative along the bracket of the spin with the rotation, so that, on readings (an SO(4)-equivariant family; supplement
section 10.31(a)), his Proposition 7.4 holds with so(4) in place of R³, its leading term the same at every spin, the
Killing rotations six, four at a = ±b ≠ 0 and two otherwise (`mp5.py`; computed exactly, Ricci-flatness at exact points,
the rest deduced in supplement section 10.36). And the pairings that make his zero energy kernel and cokernel exact are
boundary pairings at infinity -- at zero rotation, -8π times the ADM mass and angular momentum and 4πM times the centre
of mass, in five dimensions as in four -- so the eleven kernel states and the eleven dual states are independent
(`pairing5.py`; the pairings computed, his four-dimensional table reproduced as the control, the rest deduced in
supplement section 10.32). The rigidity his count takes from Andersson, Häfner and Whiting ([AHW24] Theorem 6.1, p. 35) —
every decaying stationary linearised solution smooth across the horizon a linearised Myers–Perry metric plus pure gauge —
holds on five-dimensional Tangherlini: Kodama and Ishibashi's decomposition at zero frequency reduces it to ordinary
differential equations, whose energy identities leave nothing smooth at the horizon and decaying for l ≥ 2, while l ≤ 1
gives the mass, the six rotations and pure gauge; so his count holds there with eleven for seven, and near it on a
reading (`static5.py`; computed harmonic by harmonic, the rest deduced in supplement section 10.33). The physical states
of his section 8.5 exist too: at Tangherlini, for every l ≥ 2 and each of the tensor, vector and scalar types, the static
tidal solutions smooth at the horizon are Gauss functions of r²/μ growing like r^l with coefficients that never vanish,
and near it, on the same reading and on his Proposition 7.4 in five dimensions, his construction runs, one step modified,
with his Lemma 8.15 carried over, so(4)'s bracket in place of the cross product (`physical5.py`; computed, the rest
deduced in supplement section 10.34). And five dimensions needs only l = 2: if the slowest term at timelike infinity
decays like t^(−α) with α in (1, 2] — t^−2 for the mass aspect's, where four dimensions has t^−1, the Coulombic order
separating from the radiative one above four dimensions, or t^(−3/2) if the radiative order reached timelike infinity as
Hintz's index sets would carry it — his window [−3, 0] shrinks to [α − 4, 0] and the physical states needed are the
scalar, vector and tensor ones at −2, without his generalized companions, on readings (`window5.py`; computed, the rest
deduced in supplement section 10.35). And, at the parameters used and on readings, no pure resonance at timelike infinity
decays as slowly as t^−2. In five dimensions, without Huygens' principle, Hintz's model there has genuine pure resonant
states, his own u₃ among them; the time integral of one is a static solution, so that its exponent less one is a zero
energy indicial root, or vanishes, and the state is then the time derivative of one an order lower; with the injectivity
half of his inversion below 1 + ε_ind carried over, every pure resonance below 5/2 sits at a root of the constraint
operator's zero energy operator in (2, 5/2), of the constraint kind, the lowest at the spherical type a resonance where
the computation reaches (`iota5.py`; computed, the rest deduced in supplement section 10.37). Nor does the radiative
order. Hintz's linearized operator at null infinity in five dimensions — his (5.28) at the background, computed in his
splitting, his printed matrix reproduced in four — has his diagonal and his coupling of the 01-component into the
11-component, four trace couplings changed, while every coupling through the metric perturbation falls half an order, so
that the iteration's quadratic sources reach null infinity at the Coulombic order, the mass aspect's; and a radiative
term reaches timelike infinity at its own order only through a resonant state there, which the same descent and
injectivity exclude below 2. So α = 2 on readings, and the window is [−2, 0] (`scri5.py`; computed, the rest deduced in
supplement section 10.38). Nor, on readings, does the zero energy augmentation need Hintz's improved states. In five
dimensions the entries of his naive augmentation decay like r⁻³, one order better than his r⁻² and inside the target
space of his zero energy operator, and his own device for the angular momenta — the states themselves, cut off to vanish
near future null infinity — serves every state, the mass and the boosts included, with no logarithm in time; so his zero
energy operator, augmented by the eleven states, is invertible by the same pairings, and his uniform low energy bounds
and 2-admissibility hold on readings (`aug5.py`; computed on the model, the rest deduced in supplement section 10.39).
And, on readings, his proof of it loses no decay at spatial infinity in five dimensions: the time derivatives that remove
the poles at zero energy carry the states' own weights, one order better than his, and with the augmentation cut off near
future null infinity the threshold at the outgoing radial set does not bind, so the two integrations in time keep the
weights they start from; his loss of decay δ > α_sf + 3/2, α_sf the weight of his Theorem 10.1, becomes none
(`lowfreq5.py`; computed on the model, the rest deduced in supplement section 10.40). With it, his first step towards
decay carries over: on readings, the dynamical operator is admissible relative to the stationary one, the background's
orders at timelike infinity one higher than his, and its forward solutions lose there only the two orders the operator
takes (`cone5.py`; computed on the model, the rest deduced in supplement section 10.42). Several provisos of this section
— the parameter point and the threshold h₀, the roots beyond l = 12, the kernel elements' class and the uniqueness inside
the horizon, and the readings of [Hin26c] and [Hin26a] in five dimensions — are taken up in section 8.5.

### 8.4 Hintz's argument in the class

The class of section 2 is invariant under G = O(2) × O(2), acting on R⁴ = R² × R² by the rotations of the two planes and
the reflections x2 → −x2, x4 → −x4. Of the fifteen Killing fields of 4+1 Minkowski space only ∂_t is G-invariant, and a
G-invariant spin matrix in so(4) vanishes; so in the class Hintz's final parameters reduce to the mass, the boost and
rotation states of his construction are absent, and his Steps 2 and 5 reduce to his Propositions 11.20 and 11.51 at zero
boost (supplement section 10.43, `class5.py`: the invariant harmonics counted two ways, computed; the reduction deduced).
With that, his sections 11–13 carry into five dimensions in the class (supplement sections 10.44–10.49). At null infinity
the leading part of his normal operator is his with 3/2 for 1, its non-resonant gap at the parameter point is (38/25,
499996.62) against his (51/50, 499996.12), and its exceptional exponents are 2 and 3/2 + (1 − e_Υ)γ_Υ for his 1 and 1 +
(1 − e_Υ)γ_Υ (`iplus5.py`; computed, the exponent 2 from the indicial equation of the quadratic radiative term, whose
coefficient −12/25 does not vanish at the point, `docket68/n1star/checks/support8c.py` K4, on the Ricci part). The gauge
parameter changes his steps solve for vanish in the class, and his bookkeeping of the terms at the Kerr face, run over
every exponent at timelike infinity the class's sources carry — all at least α_min = 3/2 + (1 − e_Υ)γ_Υ = 1.5099 —
records no physical state: the class loses one order of decay at the Kerr face where he loses two, and the iteration
needs its forcing at order 3 + ε_K there (ε_K a small decay parameter, chosen after ℓ0 and below ℓ0 − 3) (`sharp5.py`;
computed, the bookkeeping deduced). The write-out runs the iteration with α ∈ (4 + ε_K − ε′₀, 4 + ε_K] and rate α − 2
(supplement `docket68/n1star/proof5/PART-VI4-PARAMS.md` row w2; deduced there; the table's order and its inequalities at
witness values computed, `docket68/n1star/checks/support8b.py` M4). His Theorems 12.3 and 12.8, the exterior theorems of
his section 5 with the radiative order 3/2 at null infinity, and his Theorem 13.1 follow: in the class, for every ε <
ε_K, G-invariant data near five-dimensional Tangherlini of mass m₀ that satisfy the constraints, have his decay and are
small enough, depending on ε, have a G-invariant vacuum development, and it settles to Tangherlini of a nearby mass at
the rate t*^(−2−ε) in spatially compact sets (supplement section 10.49; deduced, on the readings of section 8.5).

### 8.5 The readings taken up

Sections 8.3–8.4 rest on two kinds of reading: that a computation at one parameter point serves Hintz's "for all
sufficiently small h", and that arguments written in 3+1 dimensions hold in 4+1. The parameter point's values, γ_C = 10⁶
among them, are those the computations used; the constants Theorem 4 uses are those of the write-out's proved set
(supplement `docket68/n1star/proof5/PART-VI4-PARAMS.md` section 3; its table orders without a cycle, and Theorem 2.1's
steps follow the order, `docket68/n1star/checks/support8b.py` M4). Each has been taken up (supplement sections
10.52–10.59). Computed: every indicial root of the linearized gauge-fixed operator is simple at every harmonic degree l ≥
2, l = 0 and 1 being computed directly, and his distance condition (8.13) holds with ε_ind ≤ 1.94 × 10⁻⁸ (`eind5.py`: the
certificate exact, the scan below l = 10⁴ certified by rigorous root inclusion in exact rational arithmetic
(`docket68/n1star/checks/eindcert5.py`: the least distance is δ_50 = 1.94137056846 × 10⁻⁸, enclosed to 3 × 10⁻⁴⁸,
attained at l = 50 by a root of the gauge potential's operator; the constraint damping's own roots with |λ| ≤ 50 stay at
least 2.9 × 10⁻⁶ from the integers)). The constraint damping holds at every h in (0, 10⁻⁶], not only at the point: the
indicial roots of the constraint propagation operator avoid [−100, 2] but for the simple Coulomb root at l = 0 and 1, for
every such h, by the point's line-crossing certificate with h as a second parameter (`uniform5.py`; exact). Since Hintz's
own threshold is not explicit — "there exists e₀ = e₀(v) in (0, 1) such that for all e in (0, e₀), there exists h₀ > 0
such that for all h in (0, h₀)" ([Hin26a] Theorem 4.9, p. 37) — this removes the proviso that the point lie below it:
every other conclusion drawn at the point inherits from this, is free of h, improves as h falls, or, like simplicity,
fails at most on a countable set of h (the 68 lines of the supplement's section 10 that draw a conclusion at the point,
named by its value, each placed in one of these classes by the class's own text, `docket68/n1star/checks/census9.py` C23;
the last two classes computed: `docket68/n1star/checks/hclass5.py` — the quantities proportional to 1/h are positive at
the record's signs and grow as h falls on (0, 10⁻⁶], and simplicity and the integer values are, for each l ≤ 20 and
integer up to 52, nonvanishing polynomials in h with no root in (0, 10⁻⁶]; `docket68/n1star/checks/re813.py` — the
distance condition (8.13) holds off a countable set of h but not at every h: at l = 1000 and h = 6.6526 × 10⁻⁷ two
indicial roots are 2 ± 3.683 i, of integer real part, and for each l and each integer n with |n| ≤ 50 the h at which a
non-real root has real part n are roots of a resultant that is a nonzero polynomial in h; exact), and the horizon
threshold holds for small h by the sign of the damping. And the transfer from the Minkowski model is computed:
five-dimensional Tangherlini is exactly η + (μ/r²) k ⊗ k with k = dt + dr null, its connection two orders below
Minkowski's, so that every operator of the route differs from its model in ρ⁴ Diff_b against the model's ρ² Diff_b, one
order better than four dimensions (`transfer5.py`; exact). READ at source, with the substitutions they imply deduced:
[Hin26c]'s section 9 is set in general dimension (its Definitions 9.3–9.4; its Theorem 9.38, Corollary 9.39 and
Proposition 9.40 carry n), every three-dimensional numeral in it and in its sections 5–13 comes from (5.7)'s (n − 1)/2 or
from a density, and bundles are, in its words, "purely notational" (p. 158); [Hin26a]'s section 5.2 takes from the metric
only symbol data, all computed here in five dimensions; [Hin23a]'s exterior estimates are needed only near a piece of
null infinity for compactly supported data, its radiation couplings falling half an order at the five-dimensional
radiative order r^(−3/2); [Hin26]'s Proposition 2.25 is stated on Rⁿ; and [CD03]'s gluing is independent of the
dimension. Deduced: the kernel elements' class (its decay at infinity 3/2 + S̄ for his 1 + S̄, computed,
`docket68/n1star/checks/support8c.py` K2); and the uniqueness inside the horizon, with the continuation there that
Hintz's mode stability argument needs, by a lemma on the radial systems' simple zero at r_h proved in supplement section
10.76 (the Frobenius exponents at r_h computed, 0 with the damping's negative ones, so the solutions smooth there are the
exponent-0 family, K1); the resonances at timelike infinity between 5/2 and 3 + ε_+, whose locations the bookkeeping of
section 8.4 does not need (scanned for l ≤ 1200, 10⁴ and 10⁵: none in (3, 3 + ε_+] for any admissible ε_+, the nearest 3
+ 2.932 × 10⁻⁶, K3); and the gluing of section 8.7.

### 8.6 Without the class

Settling needs only the class, where Theorem 1's solutions lie; perturbations with no symmetry are included as well.
Without the class Hintz's construction keeps his boost, his rotations and his centre-of-mass motions: the zero energy
nullspace is eleven-dimensional (the mass, the six rotations of so(4), the four translations), the four boosts add a
second-order pole at zero energy, and forward solutions lose two orders of decay at the Kerr face, as in four
dimensions. Two things are needed beyond section 8.4; a third concerns a gluing that, as section 8.7 shows, Theorem 4
does not use.

First, Hintz takes mode stability and the zero energy count at every Kerr parameter from [AHW24] Theorem 6.1, p. 35. In
five dimensions they are deduced at every Myers–Perry parameter near Tangherlini by the perturbative route of [HHV21],
which expects "the linear stability of ... slowly rotating Myers–Perry black holes [MP86], to follow by similar
arguments" (p. 14; [MP86] in their numbering): the high-energy conditions are strict at Tangherlini and persist;
invertibility persists on compact sets of frequencies; and at low energy the eleven zero energy states exist at every
nearby parameter and exhaust the kernel by its upper semicontinuity, after which Hintz's augmented operator gives
invertibility near zero (supplement section 10.60; deduced).

Second, his bookkeeping at the Kerr face with two orders of loss, run over every harmonic type at every exponent at
timelike infinity the sources carry, eliminates six pure gauge classes, records fourteen, and records the physical
states of scalar, vector and tensor type at l = 2 — the tensor type the one kind four dimensions lack — with every
recorded term's image above the threshold (`general5.py` G1; computed, the steps deduced, supplement section 10.61). His
Theorem 13.1 follows in five dimensions without the class: for every ε < ε_K, data near Tangherlini with no symmetry
that are small enough, depending on ε, have a vacuum development that, its initial slice boosted by a small Lorentz
boost, settles to a Myers–Perry metric of nearby mass and small spin at the rate t*^(−2−ε) in spatially compact sets
(supplement section 10.62; deduced).

Third, gluing a perturbation at large radius to the family would have to match all fifteen Poincaré charges, which a
translated, rotated and boosted Myers–Perry metric supplies — in [CD03]'s words, "the only element missing is an
equivalent of Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry metrics" (Remark 8.2, p.
36). Near Tangherlini it is computed: the Jacobian of the charges in the mass, the four boosts, the six rotations and
the four translations is diagonal — energy 3πμ/8, angular momentum πμ/4 per unit rotation, momentum of size 3πμ/8 per
unit boost velocity (P = −Ev, v the velocity of the coordinate boost) and centre of mass 3πμ/8 per unit translation in
energy-weighted form — with nonzero determinant, so the charge map — polynomial in the parameters, the exact charges
being E = 3πμ/8 and J = (πμ/4)A ([ER08] (34)) — is a local diffeomorphism there and [CD03]'s gluing applies
(`general5.py` G2; computed, the gluing deduced, supplement section 10.63).


### 8.7 The solutions of Theorem 1 after the shell

After the shell, on {v > v_end}, every oscillating profile of the approximant vanishes — the waves are proportional to
the envelope, and the transports of Lemma 5.3 run along lines of constant v — so there the approximant g_app is
Tangherlini of mass μ_end plus smooth means independent of λ times powers of λ, and g_λ differs from it by O(λ^(K−3))
(supplement section 10.50; deduced, its inequalities computed, `docket68/n1star/checks/support8b.py` M2). The estimate of
Theorem 1 holds at every order of derivatives k ≥ 6 with K ≥ 6, its bootstrap closing whatever k is (supplement section
10.51; its ledger with k and K symbolic computed, `docket68/n1star/checks/ledger5.py` L2). So, with K large enough for
the number of derivatives needed, the data of g_λ on Hintz's initial surface near the hole, which lies in a suitably
enlarged domain of Theorem 1, are small in every norm his theorem uses. Beyond a ball they are glued G-equivariantly to
exact Tangherlini data on the same surface by [CD03]'s method. Its obstruction is the Killing initial data, of which the
G-invariant ones are ∂_t's alone, so only the mass is matched, and on G-invariant data no parity condition is needed. The
flux identity bounds the glued mass's distance from μ_end by the data's deviation (computed:
`docket68/n1star/checks/flux5.py` — the flux of the Kerr–Schild slice is 6π²m at every radius and its remainder q
vanishes there, the flux is the divergence of the linearised scalar curvature with a remainder quadratic at flat data,
and the remainder scales as R⁻⁶ on the annulus, which with its volume gives the bound; the difference bound for the
quadratic remainder is argued, not computed), so the glued data stay O(λ)-close to Tangherlini in Hintz's weighted norm
at a fixed gluing radius. Hintz's argument, run on G-invariant spaces with its smoothing operators and right inverses
averaged over G and its choices made symmetric, then gives a G-invariant development whose final parameters, fixed by G,
are a mass alone (supplement `proof5/PART-VII-ASSEMBLY.md`, Proposition 2.2 and Proposition 3.2). Without the class, his
theorem applies directly to perturbations of these data in his data class, which contains the data of every nearby
translated, rotated and boosted Myers–Perry metric (computed: their Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the
radial compactification, `docket68/n1star/checks/mpdata5.py`, exact series at three points of S³ with spins, a boost and
a translation, and the structural step that a Cartesian derivative gains a power of ρ). A perturbation that only decays,
faster than r^(−3/2), can be glued far out to such a metric by [CD03]'s gluing, which in five dimensions needs no parity
condition at that rate (section 8.6; supplement sections 10.63 and 10.66). But the glued data's development is not the
perturbation's: the solution near the hole at late times depends on the data near infinity. So the gluing would at most
show that such a perturbation agrees on a large ball with one to which Theorem 4 (ii) applies, and that is not proved
here: the glued data's smallness in Hintz's weighted norm depends on the gluing radius, a bump of relative size R^(−1) at
radius R costing about R^(ℓ0−3) there (deduced in supplement `docket68/n1star/proof5/PART-VII-ASSEMBLY.md` section 5;
computed for a bump of amplitude R^(−3), R^(−1) of the black hole's own deviation from flat space at R, in the norm's
b-density, `docket68/n1star/checks/support8b.py` M3).

### 8.8 Settling

**Theorem 4 (proved: supplement `docket68/n1star/proof5/PART-VII-ASSEMBLY.md` Theorem 0.2).** Fix ℓ0 ∈ (3, 4); let ε_K be
the decay parameter of section 8.4, with 0 < ε_K < ε_+ < min(δ♯, ε_ind, ℓ_I − 3) for some ℓ_I ∈ (3, ℓ0), δ♯ = (1 −
e_Υ)γ_Υ and ε_ind that of section 8.5 (supplement `docket68/n1star/proof5/PART-VI4-PARAMS.md` row w1); and fix ε < ε_K.
Let g_λ be the solutions of Theorem 1, with A and the envelope fixed, with K large enough and on a domain enlarged as in
section 8.7. For every ε_m > 0 there are λ1 > 0 and δ > 0, depending on ε_m and ε, such that for λ ≤ λ1:

 (i) (in the class) the data of g_λ on Hintz's initial surface, continued G-equivariantly to exact Tangherlini data
     beyond a ball (section 8.7), have a G-invariant vacuum development, with the same data as g_λ on that ball, which
     settles to five-dimensional Tangherlini of a mass m′ with |m′ − μ_end| < ε_m: its difference from that metric is
     O(t*^(−2−ε)) in spatially compact subsets of the exterior;

 (ii) (without symmetry) every smooth vacuum data set on the same surface whose difference from the data of (i) is small
     in Hintz's data class -- polyhomogeneous at spatial infinity, with terms of orders r^(−2) and r^(−3) in the metric
     and r^(−3) and r^(−4) in the second fundamental form, and conormal remainders in r^(−ℓ0) H_b^∞ and r^(−ℓ0−1) H_b^∞
     -- has a vacuum development that, its initial slice boosted by a Lorentz boost below ε_m, settles at the same rate
     to a Myers–Perry black hole of mass m′ with |m′ − μ_end| < ε_m and spin below ε_m.

The assembly of Theorem 4 from the parts is written out at n = 4 in supplement `proof5/PART-VII-ASSEMBLY.md`, which
proves it (read independently, its repairs read again). It narrowed (ii). An earlier version also covered perturbations
that merely decay faster than r^(−3/2), by gluing them far out to a boosted Myers–Perry metric. That gluing replaces the
data near infinity, and the solution near the hole at late times depends on those data, so it proved settling for the
glued data and not for the perturbation. (ii) now takes the perturbation in Hintz's own data class, where his theorem
applies without gluing. The assembly also found that his data must have their terms of orders r^(−2) and r^(−3)
polyhomogeneous, and that the rate holds for every ε < ε_K rather than at ε_K.

Theorem 4 is proved: the supplement's write-out, `proof5/`, described below, proves it in full at n = 4. Before that
write-out it was deduced, and two things separated it from proved, which the write-out replaces. (i) The censuses. Every
estimate of the companion papers that the route uses has been read at source for where the dimension enters (supplement
sections 10.53–10.58). The proofs that were left as readings are carried to n = 4 by modification: [Hin26c]'s sections
7–8 and 9.3, [Hin26a]'s section 5.2, [Hin23a]'s section 3, [CD03]'s gluing, Hintz's handling of the boost (his sections
3.4, 5.6 and 11–13) and the two arguments of [HHV21] the route uses. For each, a census of the source in full text finds
every place the dimension enters, each is computed at n = 3 against the printed value and at n = 4, and the proof is run
with the computed quantity in place (supplement sections 10.64–10.68; `exterior5.py`, `gluing5.py`, `edge5.py`). The
conjugated wave operator at null infinity gains (3/4)r^(−2), which only strengthens Hintz's energy form. The gauge
endomorphism there has the diagonal 2γ_C, γ_C, (3/2)γ_C, −(3/2)γ_Υ, −γ_Υ, 0, −2γ_Υ, lower triangular, with the same least
positive entry, −γ_Υ, as in four dimensions; there γ_Υ is [Hin23a]'s, in (−1, 0) (READ: [Hin23a] (2.8), p. 7), while
section 8.4's γ_Υ = 1/100 is [Hin26]'s. The quadratic radiation term and the metric-dependent entries fall by r^(−1/2),
so the coupling that four dimensions must track at leading order is an error term in five. The energy current at null
infinity keeps its threshold α_I < −1/2. The boost changes the data at r^(−2), inside Hintz's class, where in four
dimensions it changes them at the radiation order. [CD03]'s gluing needs its parity condition on the data only for decay
below r^(−3/2); its other uses of it fall on the Myers–Perry metrics glued to, which meet it. [Hin26a]'s calculus is
constructed in every dimension [Hin23d, Hin26d], and each positive commutator in its section 5.2 is an identity of
symbols whose sign is a positivity computed in five dimensions. A second census by another method agrees: a sweep of
every marker of the dimension on every page of the carried passages finds 278, all accounted for but one norm convention,
now named (supplement section 10.69; `censusweep.py`). What that route did not do was re-derive those papers line by
line: that the censuses found every place the dimension enters was evidenced by the two methods agreeing and read at
source, page by page, not proved. (ii) The deductions of the supplement's sections 10.12–10.72 were arguments from
computed inputs, inputs READ at source, and readings — statements of the companion papers at n = 4 that the modification
steps carry, on which 34 of those steps rested until each was settled, written out or READ — each read independently, not
proofs written out at the level of the theorem's statement. Inventoried by a fixed rule, the 248 deduced steps are 90
pieces of bookkeeping on computed values, 29 applications of results printed for general n, 31 perturbation or continuity
arguments, 38 other, and 60 proofs written in 3 + 1 dimensions and carried to five by modification, 61 with one undecided
step that supplement section 10.73 reads so (counted from the inventories, `docket68/n1star/checks/support8b.py` M5).
Those 61 are the core of what a line-by-line check would write out
(supplement sections 10.70 and 10.74, `DEDUCTIONS.tsv`, `B-MAP.tsv`). The perturbation steps are now at proof level given
their continuity inputs. They rest on five lemmas — openness of invertibility, semicontinuity of the kernel, persistence
of strict inequalities, Rouché and the inverse function theorem — of which the first three are proved in the supplement
and the last two are cited, and on continuity statements read from the sources (supplement section 10.71). The
applications of general-n results have every hypothesis placed, three of them now read at source (supplement section
10.72). The 38 others, read one by one, are twelve with no step of their own, 25 at proof level given their inputs —
among them steps by symmetry and sums over harmonics, put there by two lemmas proved in the supplement — and one more
modification step (supplement section 10.73; `synth5.py`). Each of the 61 modification steps lists the places where the
dimension changes its proof — 57 name some, 4 none, the proof being the source's as it stands — and each five-dimensional
value there is computed, deduced in an earlier section, arithmetic in n, or a choice the supplement makes (supplement
section 10.74, `B-MAP.tsv`). What they leave is that the source proofs use the dimension only at those places, which is
the census question of (i): by a rule the supplement deduces rather than proves, (ii) reduces to (i), but for one step,
which rests on a modification step and so on the census (supplement section 10.73). All 61 are now written out step by
step at n = 4 — forty-five with source proofs of at most about seven pages (two replaced by a computation), sixteen on
longer runs of proof, [Hin26] sections 11 and 12, [Hin26c] sections 5, 7–11 and 13 and [Hin26a] section 5.2 — so their
own steps rest on their inputs and not on a census, though thirty-four took a reading among those inputs, a statement at
n = 4 whose proof was not written out. Traced to their roots, the readings were ten statements, and each is now settled,
written out or READ: five of the supplement's own statements, among them the damped operator's threshold at the horizon,
by computation, and what the late-time expansion uses of the zero energy pole, by deduction; two groups of companion
results, written out at n = 4; one READ for general n; and two steps the source takes at every n without writing them
out, on which his own theorem in 3 + 1 dimensions rests too -- the passage from scalar operators to operators on bundles,
which he leaves to the reader, and the uniformity of the estimates under small perturbations, which he asserts -- both
written out site by site, the sites checked by a second census, and each proof of his spectral theory that the route uses
re-run on bundles with the changes in -- a re-run that found one sign slip in the source, in the commutator behind the
b-regularity at the outgoing radial set, repaired without change to the statement (supplement sections 10.75 and
10.77–10.86, `READINGS.tsv`, `hthresh5.py`, `tfnorm5.py`, `iotasol5.py`, `bundlesweep.py`, `bundle5.py`, with a lemma at
the horizon proved in section 10.76). λ1 and δ exist by the proof — from Hintz's smallness constant and Theorem 1's
estimates — and are not evaluated. A line-by-line check of those papers at n = 4, with the deductions written out, would
make Theorem 4 a theorem. That write-out is done: the proof written in full, complete at n = 4 given the
general-dimension results READ at source and the standard theorems it cites, in seventy-four parts, each proving its
statement in its own text (each part read independently, its repairs read again until found correct). Its first three
parts -- Hintz's spectral theory at bounded nonzero, at high and at low frequencies, on bundles and uniformly in the
operator -- are proved in their parts (the second has since gained one lemma, at the trapped set, asked for in reading
the nineteenth; the lemma read independently too). So are the fourth, the setup of his spacetime analysis, and the fifth,
which proves the two standard estimates that the fourth takes as inputs; the fourth corrects the hypothesis of his real
principal type estimate on the variable order, which as printed admits a counterexample. The sixth, the dynamics of light
rays in the stationary model, the seventh, the classes of operators, the time function and the order functions of his
spacetime analysis, and the eighth, the trapped sets of the perturbed metrics, proved here without the theorem on
normally hyperbolic trapping that he cites, are written out in their parts (supplement `proof5/`; each read
independently). The ninth, his microlocal regularity estimate on spacetime, with the radial estimates and the estimate at
the trapped set, which he quotes from his earlier paper and which is proved here in the present calculus, the tenth, that
estimate with b-regularity and in the tame form his iteration uses, and the eleventh, his energy estimates on bounded
time slabs and in the black hole interior, with the global estimate at high frequencies they give, are written out in
their parts likewise. The twelfth, his analysis at future timelike infinity -- the normal operator there, its spectral
family at bounded and high frequencies, its forward solutions, and the forward solutions of the stationary model on the
spaces his iteration uses -- is written out in its part likewise. The thirteenth, the forward solutions of the perturbed
wave operators with estimates tame in the regularity, and the fourteenth, the Nash-Moser theorem with the smoothing
operators and tame bounds it needs, proved here rather than quoted, are written out likewise, and the three parts, the
twelfth's included, prove their statements (their repairs read again). The fifteenth, the Fourier transform in time on
the weighted spaces, his resolvent bounds translated into them and the radiation field at null infinity, by which forward
solutions are shown to decay faster, is proved in its part. The sixteenth, the first of the parts on his stability paper
-- the five-dimensional black hole family on the compactified spacetime, its time functions, initial data and boosts, and
the gauge-fixed Einstein equation -- is proved in its part. The seventeenth, the harmonics on the three-sphere and the
operators of Minkowski space in the splittings his stability paper uses, is written out in its part. The eighteenth, the
b-analysis and Fourier transforms with partial expansions on which that paper's asymptotic analysis rests, and the
nineteenth, the wave operator on the gauge potential near the five-dimensional black hole -- its structure near infinity,
its model, its indicial roots, its threshold and trapped set, and its mode stability away from zero frequency, proved
there by ordinary differential equations -- are proved in their parts; the eighteenth's closes one gap more, in the order
of regularity of one lemma, found on a second reading. In the eighteenth, one step of his proof gives more logarithmic
terms than he states, and the stated set is proved here another way; in the nineteenth, the inner product at the trapped
set depends on the direction of the ray, which the second part now allows by the conjugation he uses, written out. The
twentieth, the same operator at zero frequency: its kernel and cokernel on the black hole, the modification at the
horizon that removes them, and mode stability at every frequency, and the twenty-first, the stationary gauge potentials
that begin as the translations, boosts and rotations of Minkowski space, are proved in their parts. The twenty-second,
the gauge potentials polynomial in time that carry them, and the remaining roots, to higher order, the twenty-third, the
constraint propagation operator of his gauge at zero frequency and the stationary dual states built from the symmetries
of Minkowski space, eleven in five dimensions against his seven, the twenty-fourth, the dual states of the rotations,
whose leading term depends on a rotation only through its bracket with the spin -- in five dimensions an exact identity
of the black hole family, and the twenty-fifth, the linearised gauge-fixed Einstein operator near infinity and at the
trapped set, where in five dimensions the plane of directions orthogonal to the trapped rays turns along them, are proved
in their parts; the twenty-fourth's needed no repair on reading. The twenty-sixth, the indicial roots of that operator
and its invertibility where low frequencies meet spatial infinity, is proved; there the source's claim that all those
roots are simple is shown to rest on properties of the constraint damping operator, which the parts on that operator
supply. The twenty-seventh, the mode stability of the same operator away from zero frequency, is proved: at the black
hole itself it is proved here, frequency by frequency and harmonic by harmonic, from the master equations of Kodama and
Ishibashi, where his proof cites a theorem on the four-dimensional rotating black hole that has no five-dimensional
counterpart; near it, it is proved for frequencies bounded away from zero, and small frequencies away from the black hole
itself are taken in the parts on low frequencies. The twenty-eighth, its kernel and cokernel at zero frequency,
eleven-dimensional in five dimensions against his seven, is proved: at the black hole itself through the stationary
solutions of the linearised Einstein equation there, which are classified here harmonic by harmonic in place of the
four-dimensional theorem he cites, and near it by perturbation of an augmented operator, with no classification for the
rotating black holes needed. The twenty-ninth, the pairings that make that count exact and the large stationary states it
needs, is proved: the pairings he takes from earlier papers are reduced here to integrals at infinity of leading terms,
and the states, which in five dimensions include a tensor type that four dimensions lacks, are built with one step of his
construction changed. Each of those four was read independently, its repairs read again.

The thirtieth, his spectral family at future timelike infinity -- its Fredholm property across the light cone, its
b-regularity there, its invertibility for Re λ < 2 and its finite meromorphy -- the thirty-first, the normal operator
there, with its inverse, its asymptotics at null infinity and near the black hole, and its boundary spectrum, and the
thirty-second, the formal solutions at late times near the black hole built from the zero energy states, their expansion
and their grafting into spacetime, are proved in their parts. So are the thirty-third, the metric perturbations at n = 4
and the linearised operator at null infinity, whose matrix there is constant and lower triangular, its perturbation half
an order lower; the thirty-fourth, the normal operator at future timelike infinity on partially polyhomogeneous inputs,
with one exceptional exponent and the least incoming pole 3/2 + (1 − e_Υ)γ_Υ; and the thirty-fifth, the normal operator
where low frequencies meet spatial infinity, with the expansion of its inverse over the window (−3, 0], where the first
step of his Proposition 9.35 is repaired. The thirty-sixth, the low-energy resolvent with his augmentation, uniform at
low frequencies, and the thirty-seventh, the 2-admissibility of the linearised operator, which at n = 4 loses nothing at
spatial infinity, are proved. So is the thirty-eighth, the uniformity of all this near Tangherlini: strong trapping
admissibility at every nearby parameter by a frame built from the null geometry, 2-admissibility on one neighbourhood at
every order, and the forward solutions uniformly over the family.

The thirty-ninth to the fifty-fourth carry his section 11, the linearised equation about the dynamical metric, and the
expansion of its solutions at late times near the black hole: the forward solutions and their partial polyhomogeneity at
null infinity; the almost linear bounds; the boost parameter, its correction terms, the boost identity and the boost's
elimination; almost boundedness; the extraction of the black hole parameters and of the translation, and their
elimination, where the shift of the centre of mass needs a translated exterior background at n = 4; the decaying motions
of the centre of mass; the correction terms for six types of rows; the expansion near the black hole in its spacetime and
its spectral phase and at every level up to 4 + ε_K; and the augmentation by the expansion's own parameters. At n = 4
several of his steps fall away -- the logarithms in the boost, the splitting of the source, the logarithmic term of the
centre of mass, the step at future timelike infinity in the boost's parameter -- and each part says which. The first
fifteen of these are proved in their parts. The fifty-fourth carries the whole linear theory from Tangherlini to the
nearby rotating black holes at which the iteration's base points lie, with constants uniform in the parameter. At a
rotating black hole the rotations are no longer symmetries, and their terms are new rows of the expansion, fixed inside
the elimination. Its census of where the linear theory uses the static black hole was first a search of the text; it is
now a reading, described below, and with the repairs that reading found the part proves its statement.

The fifty-fifth and the fifty-sixth, his efficient parameterisation of the data and the description of every linear
forward solution through it, the fifty-seventh, the estimates tame in the regularity, for which a calculus of tame
families is built, and the fifty-eighth, the same at exact weights, which his iteration needs on one pair of scales, are
proved. The fifty-seventh found that its inverse maps a source at one loss of weight to a solution at a larger loss,
where the iteration needs the same, and the fifty-eighth closes that gap. The fifty-ninth, his nonlinear theorem -- the
initial data in a cut-off gauge, the map whose zero is the solution and its right inverses, the Nash–Moser theorem of
the fourteenth part, and the propagation of the constraints -- is proved. The sixtieth to the sixty-sixth carry the
estimates of his companion papers near null infinity and his constraint damping: [Hin23a]'s analysis at null infinity,
the energy estimates for the system and their tame form, sharp decay by integration along two families of curves, and
the slab near null infinity; then [Hin26a]'s constraint damping operator, with its indicial roots for every small value
of the damping variable, its mode stability and its invertibility at zero frequency by the adjoint route, his estimates
on its compactification at n = 4, and its model on five-dimensional Minkowski space where low frequencies meet spatial
infinity. All seven are proved; the damping is proved at the values the iteration uses -- one point of two of its
constants, the third in a bounded interval, and the damping parameter large outside a countable set -- not over the
range his statement allows. The sixty-seventh, the exterior solution and its partial polyhomogeneity at spatial and null
infinity, obtained here without subtracting the radiation fields, and the sixty-eighth, the pullback by boosts in the
cut-off gauge, are proved. The sixty-ninth, [CD03]'s gluing to the Myers–Perry family at n = 4, with a linear flux
identity and charges that need no parity condition, is proved.

The seventieth to the seventy-third check, for the operators of this paper, the hypotheses the parts state for a class of
operators: the dynamics at Tangherlini, with the trapped set's separatrices in closed form; the horizon near Tangherlini;
the trapped set and the global dynamics near it, by the separability of the five-dimensional Myers–Perry metrics; and a
consistent choice of the parameters the parts leave open, in an order with no circular threshold. All four are proved;
the seventy-third's argument that the damping is used at one value only is now an enumeration, described below. The
seventy-fourth assembles Theorem 4 from the parts and the construction of Theorem 1, in the class and without it, and
proves it. The seventy-fifth, written after Theorem 4, linearises it at the Tangherlini data and proves the linear
statement of section 8.2. Its part had one gap in a justification, found on reading, and no step that fails: the
linearised constraints were carried to the initial surface along a family whose second derivatives the proof did not
control, and are now carried along the straight line through the background, so the part proves its statement.

Three completeness claims inside the write-out first rested on searches of its own text: that no part uses the constraint
damping at constants other than the ones proved, that no step uses a lower triangular structure of the subprincipal
symbol, and that every use of the static black hole's properties in the linear theory holds at the nearby rotating ones.
The first two are checked by enumeration, assuming every use names its object, an assumption the base-point reading found
false for the third claim: a program lists every line of the parts in scope that names the property's object, with its
class, and fails on any line it does not list; for the damping's other constants the program lists every line in which it
finds one of them set, bounded or quantified (`proof5/checks/gammac5.py`, `proof5/checks/admiss5.py`). The third is
checked by a reading: five independent readers went through the linear theory, 7,577 lines when they read it, and
recorded every use of the base point with what supplies it at a rotating one (`proof5/BASEPOINT-LEDGER.md`). The reading
found three gaps the search had missed -- two identities, of the boost and of the black hole's parameters, exact only at
the static black hole, whose metric and correction terms they use in a transition region, and an expansion that used,
without saying so, that the rotation state vanishes at the static black hole -- a smaller one, the reality of the objects
at a rotating black hole, and one theorem used at a rotating black hole but not stated there; each is repaired, with a
direct bound in place of continuity at a fixed black hole. A reader of those repairs found the expansion's incomplete. It
is completed by a symmetry: the antipodal map of the four spatial directions is a rotation by half a turn in both planes
of rotation, so it is an isometry of every five-dimensional Myers–Perry metric; translations and boosts are odd under it,
the time translation and the rotations even (computed on the metric with symbolic spins,
`docket68/n1star/checks/support8b.py` M1), so the rotation state at a rotating black hole is a change of its parameters
alone. With those repairs every part proves its statement in its own text, and Theorem 4 follows (the repairs read
again). That no proof in Parts III–IV uses more of the class's averaged choices than the conditions stated at their
sites was read at every line of Parts III–IV that names one of them by a printed symbol on a list of thirty-three, drawn
from Lemma 3.1's sites and III.G'' Table 1.1: 577 lines, listed by `docket68/n1star/checks/vii5census.py`, each given a
verdict by one of three independent readers (`docket68/n1star/checks/VII5-READING.tsv`; that the verdicts cover every
listed line once, each with its note, computed by `checks/vii5read.py`). 311 use only the conditions at the site, 189
only name the choice, 72 name another object spelt the same, and none uses more. Five were undecided, for one reason
that all three readers found: the proofs use the 1-form towers of every type themselves, and the supplement's Lemma 3.1
named 1-forms for one type only. It now names them all, the tensor towers being their images under δ*_(g_b0), which
commutes with the average (supplement `docket68/n1star/proof5/PART-VII-ASSEMBLY.md` Lemma 3.1 and section 5, deduced).
The verdicts are readings, not computations, and a choice named otherwise than by its printed symbol would not be found.

---

## 9. What is not proved

- **Settling.** Theorem 4 is proved, in the supplement's write-out (section 8.8); λ1 and δ exist by the proof and are not
  evaluated. Theorem 4 (i) concerns glued data that agree with g_λ's on a ball; settling of g_λ's own continuation is not
  shown. Evaluating λ1 and δ would need every constant of the write-out made explicit, and several come from compactness,
  contradiction and Fredholm arguments that give no number (supplement `docket68/n1star/EFFECTIVE-CONSTANTS.md`; the
  census of those arguments and the ledger's classes recounted, `docket68/n1star/checks/support9.py` S3). The linear
  statement of section 8.2 is proved, in the gauge of the nonlinear problem (supplement `proof5/PART-VIII-LINEAR.md`),
  and a linearised solution given in another gauge differs from it by a linearised diffeomorphism L_X g (supplement
  `proof5/PART-IX-GAUGE.md`; its pointwise identities computed, `docket68/n1star/checks/ix5.py` X1–X7). The decay of X is
  not proved, so the routes in a Regge–Wheeler-type gauge and in the harmonic gauge (Hung's sections 5–8 in five
  dimensions), which argue decay in those gauges, remain deductions. Three parts of that evaluation have since been taken
  further (supplement `docket68/n1star/`). The loss d of the write-out's tame estimates, with the regularity N = 21d + 6
  in which its Nash–Moser step asks smallness (not the N of section 4, which counts the approximant's stages), is reduced
  to finitely many weights chosen under inequalities, six elementary losses given closed forms, and loop counts
  (`LOSS-D.md`, deduced from the write-out's text; its losses, weights and loops counted, 6, 9 and 3,
  `docket68/n1star/checks/census9.py` C29). At the write-out's own parameter point two nested loops already give d > 7.95
  × 10¹⁵ and N > 1.66 × 10¹⁷ in its accounting (deduced: lower bounds on the loops' rounds, about ½/(ε_K ε_ind) for each
  loop (counted, `docket68/n1star/checks/level2loop5.py` and `checks/lambdacount5.py`), where ε_ind may be any number
  below δ_50 = 1.94137057 × 10⁻⁸ (computed, exact, `docket68/n1star/checks/epsind5.py` E3; the distance condition it
  enters by `eind5.py` E2, the certificate exact, the scan below l = 10⁴ certified (`checks/eindcert5.py`)) and the floor
  is computed from the upper bound 1.94138 × 10⁻⁸ (R10)), each round being charged 3 derivatives: 2 for the operator and
  1 for the inverse of its model at the transition face, a loss fixed by the threshold at the incoming radial set, which
  is 0 here (deduced from an exact computation, `checks/thetain5.py`). That is a floor for what this proof's bookkeeping
  delivers, not for the optimal loss. A round of the write-out's iteration at future timelike infinity is charged 15
  derivatives when the order ℓ_I to which it expands at future null infinity is taken in (3, 3.5), and 4 more for each
  further unit of ℓ_I, 19 on (3.5099, 4.5), then 23, 27 and 31 to ℓ_I = 7.5, with 17, 21, 25 and 29 on the short windows
  [k + 1/2, k + 0.5099] where a round is added before the loss d_G = 7 + 2⌈ℓ_I − Re λ⌉ rises (deduced; the steps counted
  exactly, `checks/prop31loss5.py` and `checks/charge5.py`, which reproduces the d_G of the supplement's loss record at
  its own points): sufficient charges, not shown minima. Still open: numbers for the weights the write-out chooses under
  its inequalities (ℓ_I among them), the logarithmic terms of one index set, the count of one regularity step beyond its
  floor, the loop counts themselves, and the evaluation of the recursion that composes them (`LOSS-D.md` section 4; the
  logarithmic terms and the regularity step, its finding LD16); so d is still not a number. For the first constant of the
  linear theory, the resolvent of the scalar wave operator on five-dimensional Tangherlini of mass 1 cut off to an
  interval about the photon sphere, a bound is certified for every real 0 < |σ| ≤ 384 and every harmonic, ‖χ_I R_l(σ)
  χ_I‖ ≤ 11.477 on 3 ≤ σ ≤ 384, and there the constant bounding the radial derivative is at most 963.4 for every harmonic
  l ≥ 1 and 1516 at l = 0, which also bounds the radial and angular derivatives summed over the harmonics (`E2-PILOT.md`;
  certified in exact rational and interval arithmetic, `checks/e2trapband5_384.out`, `checks/e2h1band5.out`); the bound
  lies 9.5 to 22 times above the computed norm at the sampled frequencies (computed, floating point,
  `docket68/n1star/checks/e2meas5.py`); certified lower bounds for the norm, by test functions with compact support in
  the interval (for which the resolvent is inverted exactly), are 0.450, 0.250, 0.147, 0.0827, 0.0448 and 0.0241 at σ =
  3, 6, 12, 24, 48 and 96, about 40–46 % of the computed values, so the certified bound lies at most 24.6, 23.4, 25.7,
  28.7, 34.0 and 41.4 times above the true norm there (certified, exact arithmetic,
  `docket68/n1star/checks/e2lower5.py`). The passage to the write-out's own function spaces and the other constants are
  not done, so λ1 and δ are still not evaluated.
- **Physical wavelengths.** λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
  curvature length, does not apply at a wavelength of 10 l5 here (λ is the reduced wavelength of the phase v/λ, as in the
  numerics' usage). The expansion parameter is the wavelength over the curvature length L = K^(−1/4); on x_K = 1, L = l5,
  and at the horizon L = √μ/72^(1/4). For λ = 10 l5 the ratio is 10 on x_K = 1, and 2.91 (μ = 100 l5²) or 0.92 (μ = 1000
  l5²) at the horizon (computed, R7): there is no separation of scales. The statement that the waves are high-frequency
  on all of D_T once λ < l5/10 is about the approximant, not about λ0. Against the scale on which the curvature varies,
  r, the ratio is 1.00 and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (computed, R7). That is the parameter a
  construction from exact waves would see, in the manner of [AB26], whose layers are waves exact on a locally linear
  background, with amplitudes solving ordinary differential equations ("no sinusoidal identity was used", section 3.1);
  it is not small either, and there the wavelengths are chosen, here prescribed. At a prescribed wavelength without a
  small parameter, existence on D_T is a large-data question; a computed solution with a certified residual and a
  certified linear estimate could settle it (the rigorous numerics cited in [AB26] as [4]), and that is not attempted.
  Its first step was taken: the growth factor measured on the solver's own computed solution at 10 l5
  (`docket68/n1star/growth5.py`, supplement section 10.2). At both seeds that scheme's premise — one zero of the round
  spheres' expansion per column and the core boundary outflow, so that the exterior is fixed by its own data — fails
  before the shell's peak: a second zero holds over 0.04 in v from 1.50 r_h at μ = 100 l5² (1.496 on the finer grid,
  1.476 with a shorter hold; a single-step excursion at 1.45 is not it) and from 1.583 r_h at 1000 l5² (three grids
  agreeing to 0.0005), and the boundary ceases to be outflow within 0.1 after; a deeper excision fails earlier, not later
  (r = 0.39 and 0.25 r_h at the first seed, 0.21 r_h at the second), on the next finer grid too: with the breakdown read
  as a second zero lasting 0.01 in v, the solver's criterion, the three move by 0.0008, 0.0025 and 0.0002 between the
  grids and the standard excision by 0.0041 and 0.0004, and the order holds for every such duration from 0.005 to 0.06
  (`docket68/n1star/checks/excise5.py`). So no approximant on D_T comes from that scheme at 10 l5 at the excision depths
  run. What the computed solution shows is that round spheres inside the seed's horizon cease to be trapped and the
  boundary to be outflow, in the scheme's gauge, while the shell passes; the direction of the untrapping is not a
  measurement of these runs, and nothing is said of the event horizon. The step is re-posed as the characteristic initial
  value problem in double-null gauge — the incoming wave on an ingoing null hypersurface from past null infinity, the
  seed's outgoing cone as the other — where Luk's theorem gives local existence without smallness ([Wu26] Theorem 2.1)
  and [Wu26]'s Theorem 2.2 is the a posteriori structure, introduced there by the sentence "the difference of metrics is
  controlled by the difference of curvature residues" (section 2.3, p. 6; the sentence before the theorem, not its text);
  its five-dimensional version in the class is not built. Up to the failure the radiation field's growth factor exp ∫K dv
  is 1.9 and 2.1, and a finite-difference amplification of the data along one direction, a lower bound for the
  propagator's norm, is 1.28 and 1.00; where the scheme completes (λ = 0.1 r_h) they are 6.9 and 1.71, while the sup-norm
  Grönwall factor is 17, 2 × 10⁵ and 6 × 10³: a certified argument would need the propagator's norm, not a sup-norm
  bound. The linear scattering of the shell off the seed at 10 l5 is computed in `docket68/lemmas/seed_escape.py`. That
  problem has since been computed as a prototype (supplement `docket68/n1star/CERTIFY-10L5.md` section 6b; computed, not
  certified): the class's Einstein equations in double-null gauge, evolved in (u, v) with an expansion in the polar
  angle, at the prescribed wavelength at both seeds. At the first seed the Kretschmann scalar is moderate and converged
  in angle up to the point where the runs stop converging, and unresolved after it, where a singularity, a steep smooth
  feature and a defect at the axis are not yet told apart. At the second seed, with the angular and null grids refined
  together, the two coarser angular resolutions agree up to v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at
  every angle. On a finer null grid, 2400 × 1080, the second seed's M = 32 and 40 angular resolutions agree to 0.09 K_0
  up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸, Tangherlini's Kretschmann scalar at the same areal radius),
  away from the cells M = 48 masks; M = 48 departs from v ≈ 3.25 exactly as at 1600 × 720, so the finer null grid does
  not move it, and the step condition M²/N ≤ c it had been ascribed to is refuted (M²/N = 0.96). The late region stays
  unresolved (computed, floating point: `docket68/n1star/checks/g1curv5.py --seed2-2400`, output
  `checks/g1curv5_seed2_2400.out`; supplement `CERTIFY-10L5.md` section 6b). No certified step has been taken, neither a
  certified residual nor the certified linear estimate about the computed solution, so existence at 10 l5 remains open.
- **Beyond the boundary.** Theorems 1–3 are made on D_T and Ω, whose inner boundary r = a lies a fixed distance inside
  x_K = 1; beyond them Theorem 4 is stated outside the black hole. Its development also reaches inside the black hole
  after the shell, up to the curvature boundary (supplement `docket68/n1star/BEYOND5.md` Propositions 6.1–6.2, deduced;
  every use of the write-out's inner radius listed with its class, `docket68/n1star/checks/r0census5.py`, and the lowered
  boundary spacelike, f(r_0) ≤ −3 for every final mass, `checks/census9.py` C27): with the write-out's inner radius
  lowered below r_q(μ_end) = (√72 μ_end l5²)^(1/4), and every part re-proved at the lowered radius
  (`BEYOND5-R0-PROOF.md`, which found the inner radius of one part out of line with the rest, now repaired), it is
  defined on all of {r ≥ r_q} to the future of its initial slice, for every final mass (its constants then depending on
  it), and settles there at Theorem 4's rate; on their common domain of dependence it and g_λ are one spacetime (Lemma
  6.3, deduced). It is not shown that Theorem 4 applies to g_λ's own data: g_λ is given on Ω, which does not contain the
  whole initial slice, and continuing it to spatial infinity asks for a scattering problem from past null infinity and an
  expansion of its solution at spatial infinity. Parts of that are done (deduced, with exact computations, all under
  `docket68/n1star/`): the leading Coulomb part carried to spatial infinity with no logarithm (`checks/coulomb5.py`, and
  under the full operator `checks/coulombL5.py`), the map from data on the initial null hypersurface to the leading
  coefficient at spatial infinity, under the write-out's full operator on Minkowski space, bounded uniformly in the
  harmonic (reduced for every harmonic, `checks/harmonics5.py`; bounded, `checks/uniform5.py`), the remainder's sources,
  supported where v is bounded along the initial null hypersurface, entering one order later at every harmonic computed
  (l ≤ 12) (`checks/sources5.py`, `checks/stripfull5.py`), and the approximant's stage profiles expanded in powers of
  r^(−1/2) at past null infinity, with the closure properties of that expansion shown (deduced, with an exact check,
  `checks/closure5.py`). The scattering estimate itself is not done. Below r = a nothing is attempted.
- **More families.** Angular separation and the passage to Vlasov matter are not attempted. Two crossing null dusts are
  scoped and taken through the leading orders (supplement `docket68/n1star/FAMILIES5.md`): the cross coupling of the two
  families is a gauge artefact at leading order (deduced; stage 0 computed, `docket68/n1star/checks/stage0two5.py`), and
  with two families the core estimate of section 5, its approximant to every order and its lemma on the domain are
  deduced (the lemma's form for the two-dust background computed, `docket68/n1star/checks/twodomain5.py`), the last given
  the two-dust background on the whole domain. That background's existence is deduced with one step sketched, given its
  characteristic data (the outgoing family's are open; the dusts' stress in the characteristic constraints computed,
  `checks/chardust5.py`), and computed on a region that does not reach the initial slice (`checks/twodust5.py` B5,
  floating point). With the outgoing family's characteristic data moved to an earlier cone (a choice, those data being
  open), it is computed on a rectangle reaching Σ_−1.5, every outgoing ray from the inner boundary leaving it at τ ≤
  −1.78, the constraint residuals converging at second order away from the steep inner boundary and the inner boundary
  trapped (computed, floating point, `docket68/n1star/checks/twodomainx5.py`, which also computes the earlier rectangle's
  exit range, τ from −0.960 to −0.702). The linearised constraint map at the approximant's slice data has no 1/λ
  coefficient with both families, on flat space, on Vaidya with an outgoing phase that is not null there, and on a static
  background with both phases null (computed, exactly, `checks/data5two.py`), and with both families' second harmonics as
  well (computed exactly on flat space and on Vaidya; with them the constraint system's principal coefficients are the
  background's, computed), and a wave with a trace on the spheres gives one. Not done: the background on the whole
  domain, the constraints' solution on its slice, the dynamic outgoing null phase, and the proof written out at the level
  of sections 5 and 6. No statement about several families is proved.
- **The boundary at equality.** If μ0 = √72 l5² exactly (computed, `docket68/n1star/checks/eq5.py` E1–E6; deduced,
  supplement `docket68/n1star/EQUALITY5.md`): g_λ equals the seed on {v ≤ v_s}, v_s := inf supp env, so x_K = 1 is the
  seed's horizon there; it is spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η; in the layer between, whose width tends to
  0 with λ, its causal character is not decided, because there the margin and the perturbation both vanish to every order
  (computed: `docket68/n1star/checks/eqlayer5.py` — for a flat-edged envelope the margin is o((v − v_s)^k) for every k
  tested and bounded below by a multiple of env², while env' and env'' are not bounded by the margin's order, which is
  why the expansion cannot decide the layer). A domain O(λ)-close to D_T, inside x_K ≤ 1, has an inner boundary that no
  future causal curve enters, and the spheres' horizon holds in the form: at most one zero per column, within C λ of
  √μ(v); exactly one on the columns with v ≤ v_s and on those that reach across √μ(v) + C λ with √μ(v) − r_q(v) ≥ C' λ.
- **Review.** Every part of the supplement and every section of this paper was read by independent verifiers, each
  recomputing what it read, and their findings are repaired in the text. The last check that awaited a reader, that no
  proof in Parts III–IV uses more of the class's averaged choices than the conditions stated at their sites, is done
  (section 8.8): the 577 listed uses read, none using more, and one amendment to the supplement's Lemma 3.1
  (`docket68/n1star/checks/VII5-READING.tsv`, `checks/vii5read.py`). The supplement's log,
  `docket68/n1star/N1STAR-LOG.md`, records the readings; it is provenance only, not a source for any claim.
- **Computational support.** Every computed claim names its program. The identities and bookkeeping behind the deductions
  of sections 3–6 and 8 are computed, each with a negative control: `paper/response5.py` R12–R14,
  `docket68/n1star/checks/support5.py` C1–C6, C8, C9, `checks/support5b.py`, `checks/support5c.py`, `checks/support3.py`,
  `checks/ledger5.py`, `checks/stage5.py`, `checks/gauge5.py`, `checks/csolve5.py` C7, `checks/support8.py` K1, K8,
  `checks/support8b.py`, `checks/support8c.py`, `checks/flux5.py`, `checks/mpdata5.py`, `checks/kirecon5.py`,
  `checks/hclass5.py`, `checks/re813.py`, `checks/eindcert5.py`, `checks/vii5census.py`, `checks/vii5read.py` and
  `checks/census9.py`, and for section 9 `checks/support9.py`, `checks/charge5.py`, `checks/eqlayer5.py`,
  `checks/e2lower5.py`, `checks/twodomainx5.py`, `checks/level2loop5.py`, `checks/lambdacount5.py`,
  `checks/twodomain5.py`, `checks/r0census5.py` and `checks/excise5.py`. A census of the deduced claims in sections 1–9
  (103 claims, of which 27 named no program for the step) left none without one but the analytic estimates named below,
  the settling write-out and one step resting on a reading at source; where a check stops short of the step (an order λ¹
  structure in place of every order, eight of fifteen components, a scan to a finite l) its entry in Appendix A says so.
  The analytic estimates themselves (the energy estimate and the bootstrap's analysis, the mollifier's Bernstein- and
  Friedrichs-type bounds, the Nash–Moser scheme, the settling write-out) are proved in the supplement and read by
  independent verifiers, not computed (deduced). The two-dust background's convergence on a rectangle reaching Σ_τ0 is
  computed for one choice of the outgoing family's characteristic data, those data themselves being among the items left
  open above.

---

## 10. References

Each was READ at source for this paper or for the proof, on the date and at the page given; quotations are verbatim
from the arXiv text, with the extraction's spacing.

- [HL18] C. Huneau, J. Luk, *High-frequency backreaction for the Einstein equations under polarized U(1)-symmetry*, Duke
  Math. J. 167(18) (2018) 3315–3402, arXiv:1706.09501v1. READ 2026-10-20: p. 1 (Burnett's formulation), pp. 2–3 ((1.3),
  (1.4), Theorem 1.1), pp. 8–10 (Definition 3.2, Theorem 3.3, Corollary 3.5, Definition 4.1, Theorem 4.2).
  arXiv:1706.09499 is the companion paper [HL18e]; the two are easily confused.
- [HL18e] C. Huneau, J. Luk, *Einstein equations under polarized U(1) symmetry in an elliptic gauge*, Comm. Math. Phys.
  361(3) (2018) 873–949, arXiv:1706.09499v1. READ 2026-10-20: abstract and introduction, p. 1. Not cited in the text;
  listed to tell it from [HL18].
- [HL24] C. Huneau, J. Luk, *High-frequency solutions to the Einstein equations*, arXiv:2404.07659v1. READ 2026-10-20:
  pp. 11–12 (the elliptic gauge, Theorem 4.1), p. 17 (Theorem 5.1), p. 28 (sections 8.4–8.5, Problem 8.6), p. 32
  (references [55], [56]).
- [Tou23a] A. Touati, *Geometric optics approximation for the Einstein vacuum equations*, Comm. Math. Phys. 402(3)
  (2023) 3109–3200, arXiv:2206.12318v4. READ 2026-10-19/20: p. 10 ((2.9), (2.10)), p. 12 (Theorem 2.2, (2.27)–(2.29)),
  pp. 20–21 (sections 3.2.2–3.2.3, Lemma 3.1).
- [Tou23b] A. Touati, *High-frequency solutions to the constraint equations*, Comm. Math. Phys. 402(1) (2023) 97–140,
  arXiv:2206.13062v2. READ 2026-10-19: (2.1), section 5.4.2, p. 29.
- [LR20] J. Luk, I. Rodnianski, *High-frequency limits and null dust shell solutions in general relativity*,
  arXiv:2009.08968v1. READ 2026-10-20: p. 1 (abstract), p. 3 ((1.3), Conjectures 1.2–1.3), p. 5 (Theorems 1.9–1.10), p.
  6 (Corollary 1.14).
- [CBCM10] Y. Choquet-Bruhat, P. T. Chruściel, J. M. Martín-García, *The Cauchy problem on a characteristic cone for
  the Einstein equations in arbitrary dimensions*, Ann. Henri Poincaré 12 (2011) 419–482, doi:10.1007/s00023-011-0076-5,
  arXiv:1006.4467. READ 2026-10-20: (2.7)–(2.9) (arXiv HTML, unpaginated).
- [CBCL06] Y. Choquet-Bruhat, P. T. Chruściel, J. Loizelet, *Global solutions of the Einstein-Maxwell equations in
  higher dimensions*, Class. Quantum Grav. 23 (2006) 7383–7394, doi:10.1088/0264-9381/23/24/011,
  arXiv:gr-qc/0608108v2. READ 2026-10-20: (3.1), sections 3 and 5.1.
- [LR05] H. Lindblad, I. Rodnianski, *Global existence for the Einstein vacuum equations in wave coordinates*,
  arXiv:math/0411109v2. READ 2026-10-19: p. 1, (1.3) p. 2, section 2.2 p. 8.
- [IK03] A. Ishibashi, H. Kodama, *Stability of higher-dimensional Schwarzschild black holes*, Prog. Theor. Phys. 110
  (2003) 901, arXiv:hep-th/0305185v3. READ 2026-10-20: abstract p. 1, sections 2.1–2.3, summary p. 16.
- [TTS09] K. Tanabe, N. Tanahashi, T. Shiromizu, *On asymptotic structure at null infinity in five dimensions*,
  arXiv:0909.0426v2 (2010). READ 2026-10-20: pp. 2–5, (4)–(5), (20)–(21), (26)–(28), (35)–(36).
- [HL21] L. He, H. Lindblad, *Masses at null infinity for Einstein's equations in harmonic coordinates*,
  arXiv:2107.01487v2 (2022). READ (date not recorded): section 3, Proposition 3.2, p. 11 (the eikonal function from wave
  coordinates).
- [HHV21] D. Häfner, P. Hintz, A. Vasy, *Linear stability of slowly rotating Kerr black holes*, Invent. Math. 223 (2021)
  1227–1406, arXiv:1906.00860v2. READ 2026-10-24: pp. 6, 14 (the expectation for slowly rotating Myers–Perry black
  holes), 90 (Proposition 10.11's proof), 92–98 (Lemma 11.1, Proposition 11.3 and its proof). READ 2026-10-24 in full
  text (supplement section 10.68): p. 92 (Lemma 11.1 and its proof); its counts and weights, pp. 28, 70, 89–93.
- [HKW18] P.-K. Hung, J. Keller, M.-T. Wang, *Linear stability of higher dimensional Schwarzschild spacetimes: decay
  of master quantities*, arXiv:1809.05144v1. READ 2026-10-20: abstract p. 1; pp. 2–4 (Theorems 1 and 2); p. 69
  (Theorem 22). READ 2026-10-21: section 7 (pp. 28–48), 9.3.2 (pp. 54–57), 10.4.2–10.5 (pp. 66–67).
- [CLY03b] V. Cardoso, J. P. S. Lemos, S. Yoshida, *Scalar-gravitational perturbations and quasinormal modes in the
  five dimensional Schwarzschild black hole*, arXiv:hep-th/0311260v2. READ 2026-10-20: (2.1)–(2.7), pp. 3–4; Tables
  1–3, pp. 8–9.
- [KI03] H. Kodama, A. Ishibashi, *A master equation for gravitational perturbations of maximally symmetric black
  holes in higher dimensions*, arXiv:hep-th/0305147v3. READ 2026-10-20: (2.4), (2.7)–(2.8), pp. 4–5; p. 7 (l = 1);
  (3.1), (3.13)–(3.14), pp. 8–10; section 5.1, p. 13. READ 2026-10-21: (2.11)–(2.13), (2.20)–(2.21), (3.5)–(3.7),
  (3.9)–(3.14), (6.1), Appendix A (A.1b). READ 2026-10-23: (2.1)–(2.8), pp. 4–5; (2.20)–(2.24), (3.1)–(3.14), pp. 7–10;
  section 5, (5.1)–(5.17), pp. 13–15; Appendices A and B, pp. 18–20.
- [KI03b] H. Kodama, A. Ishibashi, *Master equations for perturbations of generalised static black holes with charge in
  higher dimensions*, arXiv:hep-th/0308128v4. READ 2026-10-20: (5.20). READ 2026-10-22: (4.23), (5.17), (5.19), (5.20),
  at zero charge.
- [ER08] R. Emparan, H. S. Reall, *Black holes in higher dimensions*, arXiv:0801.3471v2. READ 2026-10-23: section 4.1,
  the single-spin Myers–Perry metric (32)–(33), p. 14. READ 2026-10-24: p. 14, (34), and p. 16, the general solution's
  charges "the same as (34)".
- [CYDL03] V. Cardoso, S. Yoshida, O. J. C. Dias, J. P. S. Lemos, *Late-time tails of wave propagation in higher
  dimensional spacetimes*, arXiv:hep-th/0307122v3. READ 2026-10-20: (14), p. 4; p. 2; Fig. 2 and p. 5.
- [Hun19] P.-K. Hung, *The linear stability of the Schwarzschild spacetime in the harmonic gauge: even part*,
  arXiv:1909.06733v1. READ 2026-10-20: (1.4); (4.21)–(4.23); (8.1), (8.39); sections 5–8 for their structure. READ
  2026-10-21: section 2, Lemma 3.2 and its corollaries, section 4.1 (Propositions 4.1–4.2 and the proof of 4.1),
  Appendices A and C; and, the same day, 2.2 (the foliation, g = r_* on [5M/2, R_null]) and 2.4 (the source norm,
  (2.23)–(2.24)) re-read, Proposition 5.2, Lemmas 5.5 and 5.8; and, for the growing source and l = 0, section 4.2 in full
  ((4.10)–(4.42), Lemmas 4.8–4.10), section 5 (Propositions 5.1–5.9, Lemma 5.5), (6.1)–(6.11), section 8 in full
  ((8.1)–(8.33), Theorems 8.1 and 8.7), Appendix A ((A.12)–(A.14), Proposition A.6), Appendix B; and, for the first
  rungs' rapid decay, Appendix A in full ((A.1)–(A.14), Definitions A.1–A.2, Remark A.3, Propositions A.4–A.6), Lemma 5.3
  with its proof, Propositions 5.2, 5.4 and 8.2, Lemma 8.3, (2.4), (2.19)–(2.23); and, for the coupled estimate, section
  6 in full ((6.1)–(6.37), Proposition 6.1); and, for the spherically symmetric sector, section 8 again in full (Theorem
  8.1, Propositions 8.2 and 8.4, Lemmas 8.3 and 8.5–8.6, Theorem 8.7), Proposition A.6 and Appendix B, with the
  definition of V^(j) before (A.7) and (6.17)–(6.18).
- [Sch13] V. Schlue, *Decay of linear waves on higher dimensional Schwarzschild black holes*, Anal. PDE 6 (2013),
  arXiv:1012.5963v1. READ 2026-10-21: (2.17)–(2.20), Proposition 3.1, (5.8)–(5.17); and, for the spherically symmetric
  sector, Theorem 1 ((1.9)–(1.10)), Proposition 4.1 ((4.4)) with its proof ((4.76)–(4.92)), Corollary 4.3, Propositions
  4.21–4.22 and (5.18)–(5.22); (4.64), (4.67), (4.71) and Corollary 4.18, pp. 38–39 and 43.
- [Hin21] P. Hintz, *Normally hyperbolic trapping on asymptotically stationary spacetimes*, Probab. Math. Phys. 2
  (2021) 71–126, arXiv:1811.07843. READ 2026-10-25: pp. 7, 25 (Theorem 2.6), 31 ((3.10)), 35–37 ((P.1)–(P.6′),
  Theorem 3.9), 47 (Lemma 4.6, the proof of Theorem 4.3).
- [Hin23a] P. Hintz, *Exterior stability of Minkowski space in generalized harmonic gauge*, Arch. Ration. Mech. Anal.
  247 (2023) 99, arXiv:2302.13804v1. READ 2026-10-24: pp. 1, 9, 21–22, 27–32 (section 3's exterior estimates). READ
2026-10-24 for section 3 at n = 4: pp. 1–4, 7–9, 15–18, 20–30, 32–33.
- [Hin23b] P. Hintz, *Gluing small black holes along timelike geodesics I: formal solution*, arXiv:2306.07409v2. READ
  2026-10-23: pp. 101–110 (Lemma 9.1, Definition 9.2, Lemma 9.3, Theorem 9.6 and its proof, Lemma 9.7), 116–117.
- [Hin23d] P. Hintz, *Microlocal analysis of operators with asymptotic translation- and dilation-invariances*,
  arXiv:2302.13803v1. READ 2026-10-24: pp. 3, 7, 10–12 (the 3b-calculus on R_t × R^(n−1)_x), 109 (Proposition 5.10,
  composition).
- [Hin23e] P. Hintz, *Elliptic parametrices in the 0-calculus of Mazzeo and Melrose*, Pure Appl. Anal. 5
  (2023) 729–766, arXiv:2112.08130. READ 2026-10-25: pp. 1 (the setting, an n-dimensional manifold with
  boundary, n ≥ 1), 5–6 (Definition 1.2, Theorem 1.5).
- [Hin24b] P. Hintz, *Gluing small black holes along timelike geodesics III: construction of true solutions and extreme
  mass ratio mergers*, arXiv:2408.06715v1. READ 2026-10-23 and 2026-10-24: pp. 13, 33 ((3.1a)), 38–39 (Lemma 3.8 and its
  proof), 44 (Lemma 3.11), 49–53 (Proposition 3.16, Lemma 3.17 and their proofs).
- [Hin26a] P. Hintz, *Constraint damping on subextremal Kerr spacetimes*, arXiv:2606.27658v2. READ 2026-10-21: pp. 1–3
  (Theorem 1.1, (1.1)–(1.2)), 5, 7, 9–10, 25–37 (section 3: Definition 3.1, Lemmas 3.2–3.9; sections 4.1–4.3:
  (4.1)–(4.9), Lemmas 4.1–4.4 and 4.6, Corollary 4.7, (4.19), Definition 4.8, Theorem 4.9, Remarks 4.10–4.12), 38–41
  (Proposition 5.1 and its proof, (5.1)–(5.13), footnote 14; Theorem 5.2, (5.14)–(5.15)), 43, 53, 66–68 (Definition 6.1,
  Theorem 6.2 and its proof), 69–74 (Appendix A, (A.1)–(A.2), (A.13)), 85, 93 (Theorem B.4). READ 2026-10-22: pp. 1–2,
  11, 85, 87–88, 90–91, 93, 98 (Appendix B: Theorem B.1, Proposition B.2 and its proof, Theorem B.4, section B.4). READ
  2026-10-22 for section 6 in five dimensions: pp. 1–3, 9–11 (section 1.2.2, Figure 1.1, Remark 1.4), 38–43 (Proposition
  5.1, Theorem 5.2, (5.14)–(5.18), Lemma 5.3, footnote 15), 47, 51, 54, 64, 66–69 (Definition 6.1, Theorem 6.2 and its
  proof, (6.1)–(6.4), Remarks 6.3–6.4), 87, 93, 98. READ 2026-10-22 for Theorem 5.2's inputs: pp. 12–16 (Definition 2.1,
  (2.4)–(2.14)), 25–27, 38, 41–44 (Lemma 5.3, Propositions 5.5–5.6), 47–48, 51–52, 54, 56 (Propositions 5.8, 5.9, 5.11,
  5.12), 58–60 (Lemma 5.14, Corollary 5.15, Proposition 5.16), 64, 66. READ 2026-10-22 for Theorem B.1 in five
  dimensions: pp. 85–88 ((B.1)–(B.17), Proposition B.2), 93–94 (Theorem B.4, (B.31)–(B.37)), 96–98 ((B.38)–(B.41), the
  eigenvalues of −½r²ℓ(dr/r) and Lemma 3.3's inner product, section B.4: (B.42)–(B.45)). READ 2026-10-24 for section 5.2
  at n = 4: pp. 37, 41–42, 60, 64–65, 67–69, 91. READ 2026-10-24 for the commutators: pp. 10, 38, 47, 51, 53–54, 58.
- [Hin26] P. Hintz, *Nonlinear stability of subextremal Kerr black holes*, arXiv:2606.28253v2. READ 2026-10-21: pp. 1,
  4, 17, 25–26, 29 ((1.43) and the reason for its strip), 82 (Definition 4.2, (4.6)–(4.9)), 113 (section 6,
  (6.1)–(6.6)), 117–124 (Lemma 6.6, (6.17), Lemma 6.8, Proposition 6.9, Lemmas 6.10–6.11, Proposition 6.12 and its
  proof, (6.20)–(6.28)), 134–137 (section 7.1, Theorem 7.1). READ 2026-10-22: pp. 113–116 (Lemma 6.1, footnote 60,
  Remark 6.2, Lemma 6.3, (6.10)–(6.11), section 6.1: (6.12)–(6.16c), Lemma 6.4 and its proof, Proposition 6.5), 124
  (footnote 71), 200 (Remark 10.2); and pp. 117–124 again (Lemmas 6.6 and 6.8, Proposition 6.12 and its proof). READ
  2026-10-22 for Theorem 7.1(4) in five dimensions: pp. 136–137 (Theorem 7.1 and the proof of its part (4)). READ
  2026-10-23 for section 8 in five dimensions: pp. 25, 28, 34, 113–117, 135–137, 144–154 (section 8 through Proposition
  8.8 and its proof). READ 2026-10-23 for sections 6.5 and 8.4: pp. 51–52, 64–67, 81, 113, 117–119, 121, 124–134,
  154–157 (Lemmas 2.13, 2.15 and 2.29, Definition 4.1, Lemmas 6.1, 6.6, 6.13 and 6.14, Propositions 6.12, 6.15 and 6.18,
  Proposition 8.9, Remark 8.10, Proposition 8.11, Lemma 8.12, Corollary 8.13). READ 2026-10-23 for Proposition 6.18
  (4)–(7): pp. 19, 67, 113, 117–118, 121, 128–134 (the proof's decomposition on p. 132), 149–151, 158. READ 2026-10-23
  for section 7.2: pp. 126, 134–144 (section 7, Lemma 7.2, Propositions 7.3–7.4, Lemma 7.5, (7.1)–(7.35)). READ
  2026-10-23 for Lemma 8.12 and Proposition 8.11: pp. 145 ((8.1)), 154–158 (Proposition 8.9 through Corollary 8.13).
  READ 2026-10-24 for the s0 dual state's normalization: pp. 125 ((6.29)), 138 ((7.12)); for [AHW24] Theorem 6.1(2)'s
  use: pp. 156–157. READ 2026-10-24 for sections 2, 5, 11–13 in the class: pp. 59–61 (Proposition 2.25), 84–110, 119,
  152–154, 218–323. READ 2026-10-24 without the class: pp. 3, 5, 40, 76–81, 118–124, 136, 144, 154, 200–216, 233, 251,
  318–319. READ 2026-10-24 in full text for the boost at n = 4 (supplement section 10.66): pp. 63 (Definition 2.27), 74
  ((3.21)), 77–81 (section 3.4, Lemmas 3.18–3.19), 108–110 (section 5.6), 238–247 (section 11.4), 301–302, 310–311 and
  318–326 (Theorem 13.1 and its proof). READ 2026-10-24 (supplement section 10.72): pp. 110–111 (Proposition 5.25 and
  its proof), 217 (Lemma 10.13 and its proof).
- [Hin26c] P. Hintz, *(Non-)linear waves on asymptotically flat spacetimes. II: trapping, bound states, nonlinear
  applications*, arXiv:2606.28008v1. READ 2026-10-22: pp. 88 (Definition 4.13, Lemma 4.14), 90–91 (Proposition 4.19),
  100 ((5.1a)–(5.2)), 101–105 (Example 5.4, Remark 5.6, Definitions 5.8, 5.10–5.11, Remark 5.9, Lemma 5.12), 158–159
  (Definition 9.4, (9.4)–(9.6)), 161–163 ((9.16), Theorem 9.5, (9.20)–(9.21)), 167–168 (Proposition 9.10,
  (9.32)–(9.42)), 174–175 (Theorem 9.16), 178, 180 (Propositions 9.25–9.27), 182 ((Γ.1)–(Γ.4), (9.79)–(9.81)), 191
  (Proposition 9.35), 193–200 (Theorem 9.36; section 9.5: Theorem 9.38, Corollary 9.39, Proposition 9.40; Theorem 9.41,
  Remark 9.42, Corollary 9.43), 265; and pp. 61 (Lemma 3.11, Definition 3.12, (3.47)), 81 (Definition 4.5), 98
  (Proposition 4.24). READ again 2026-10-22: pp. 157–159 (Notation 9.2, the
  sentence after Definition 9.4), 165 ((9.24)), 172–173 (section 9.2.3, Part (5), (9.55)), 193 (section 9.3.6). READ
  2026-10-24 (section 10.41): pp. 8 (the sf-loss δ), 20–21 (the setting on R³), 45–46 (the scaled bounded geometry
  calculus), 55–59 ((3.27), Lemmas 3.7 and 3.9), 106–107 (Definition 5.13, Remark 5.14), 233, 235 (Theorem 12.2 and its
  Paley–Wiener argument), 247, 252, 255 (section 13.1's spaces, Lemma 13.13, (13.30a)), 262–267 (Theorem 14.2 and its
  proof, Lemmas 14.3–14.6), 277 (its references). READ 2026-10-24 for sections 5–13 at n = 4: pp. 19, 39, 61, 101–102,
  106–109, 114–116, 156–158, 163, 168, 174, 193–201, 211, 228, 255. READ 2026-10-24 in full text for sections 7–8 and
  9.3 at n = 4 (supplement section 10.67): pp. 101 (Remark 5.6), 114–157 (sections 7–8; (8.3), Lemma 8.1 and
  (8.9)–(8.14) on pp. 142–145), 175, 179, 182, 188, 191 (section 9.3). READ 2026-10-24 (supplement section 10.72): pp.
  264–265 (Lemma 14.6 and its proof).
- [Hin26d] P. Hintz, *Pseudodifferential operators on manifolds with scaled bounded geometry*, Commun. Am. Math. Soc. 6
  (2026) 153–243, doi:10.1090/cams/58, arXiv:2408.06651. READ 2026-10-24 (supplement section 10.65): pp. 5 (Definition
  1.3), 9 (Definition 1.9), 14 (example (10), the 3b-algebra, (1.15)), 27 (section 3).
- [AHW24] L. Andersson, D. Häfner, B. F. Whiting, *Mode analysis for the linearized Einstein equations on the Kerr
  metric: the large a case*, arXiv:2207.12952v1. READ 2026-10-23 and 2026-10-24: pp. 1 (the abstract), 35 (Theorem 6.1),
  41 (section 6.4, the proof of Theorem 6.1).
- [DLMF] *NIST Digital Library of Mathematical Functions*, https://dlmf.nist.gov/, Version 1.2.8 (release
  2026-09-15). READ 2026-10-24: §15.8 ((15.8.2), the
  connection formula at large argument, and (15.8.8), its case b − a = m a nonnegative integer, the dominant coefficient
  Γ(c)Γ(m)/(Γ(b) Γ(c − a)) for m ≥ 1, here m = l + 1) and §15.10 ((15.10.1), the exponent pairs {0, 1 − c}, {0, c − a −
  b}, {a, b} at 0, 1, ∞).
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
- [AB26] L. Alpöge, T. Buckmaster, *Blowup for the Boussinesq equations with smooth forcing*, preprint (September
  2026), cims.nyu.edu/~tristanb/boussinesq.pdf; no arXiv id or DOI as of the READ date, so cited by the author's URL.
  READ 2026-10-20: section 1.2 (the layers and the wave), section 3.1
  (Lemma 3.1 and its proof), the bibliography ([4], Chen and Hou, arXiv:2210.07191v4 and arXiv:2305.05660v3).
- [Hol08] G. Holzegel, *Stability and decay-rates for the five-dimensional Schwarzschild metric under biaxial
  perturbations*, arXiv:0808.3246v1. READ 2026-10-20: abstract p. 1, the model pp. 3–5, Theorem 1.1 pp. 5–6.
- [CD03] P. T. Chruściel, E. Delay, *On mapping properties of the general relativistic constraints operator in weighted
  function spaces, with applications*, arXiv:gr-qc/0301073v2. READ 2026-10-20: (2.1)–(2.2), p. 4. READ 2026-10-24 for
  the gluing in the class: pp. 4, 34 (Theorem 7.7), 36 (Remark 8.2), 55. READ 2026-10-24 without the class: pp. 35–38
  (Theorem 8.1 and (8.1), Remarks 8.2–8.4, section 8.2's reference family), 72–77 ((E.5)–(E.9), Proposition E.1 with
  (E.14) on p. 73, Appendix F). READ 2026-10-24 in full text for Theorem 8.1 at n = 4 (supplement section 10.66): pp. 4,
  19, 22, 24 (Theorem 5.6 and its proof), 35–37 (the proof of Theorem 8.1, (8.2)–(8.7)), 58, 71–75 (Proposition E.1 and
  its proof, (E.15)–(E.23), the Lorentz invariance of the charges and its parity step on p. 74, (E.26)–(E.27)).
- [Rac16] I. Rácz, *Constraints as evolutionary systems*, Class. Quantum Grav. 33 (2016) 015014, arXiv:1508.01810v3.
  READ 2026-10-19: (3.3), p. 6.
- [DS23] M. M. Disconzi, Y. Shao, *Strongly hyperbolic quasilinear systems revisited*, arXiv:2308.09851v1. READ
  2026-10-20: (A1)–(A4), Theorems 2.4, 2.6, Remark 2.3.
- [AO14] L. Andersson, T. A. Oliynyk, *A transmission problem for quasi-linear wave equations*, arXiv:1401.0277v1. READ
  2026-10-20: Theorem 1.1, (1.3), Remark 1.2, section 4.1.
- [BH17] A. Behzadan, M. Holst, *Multiplication in Sobolev spaces, revisited*, arXiv:1704.07930. READ 2026-10-20:
  Theorems 7.21, 7.26, 9.14.
- [GO13] L. Grafakos, S. Oh, *The Kato–Ponce inequality*, arXiv:1303.5144. READ 2026-10-20: p. 1.
- [LY22] H. Lu, L. Yao, *On Seeley-type universal extension operators for the upper half space*, arXiv:2211.15567v2.
  READ 2026-10-20: Theorems 1, 26, Lemma 27.
- [SY21] Z. Shi, L. Yao, *New estimates of Rychkov's universal extension operator for Lipschitz domains and some
  applications*, arXiv:2110.14477v4. READ 2026-10-20: sections 1, 2.1 (Rychkov's and Stein's operators).
- [AG22] F. Angeles, *The Cauchy problem for a quasilinear system of equations with coupling in the linearization*,
  arXiv:2204.01179v3. READ 2026-10-20: abstract, p. 1; (9.6)–(9.7), p. 24.
- Burnett (1989), Isaacson (1968) and Choquet-Bruhat (1969) are cited through [HL18] p. 1, [HL24] pp. 1, 32 and [LR20]
  p. 3, where they are quoted: G. A. Burnett, J. Math. Phys. 30 (1989) 90; R. A. Isaacson, Phys. Rev. 166 (1968) 1263
  and 1272; Y. Choquet-Bruhat, Comm. Math. Phys. 12 (1969) 16 (identifiers as printed in [HL18]'s bibliography). Their
  originals were not re-READ for this paper.

---

## Appendix A. The computations

Every computation is exact unless marked; each program carries a self-test whose negative controls it must reject.
Paths are relative to the root of the research tree.

`paper/response5.py`, written for this paper, re-derives its own numbers independently of the proof's programs:

- R1: the reduction, Proposition 2.1, exactly, from symbolic 2-jets in coordinates normal for g3. Control: 3/2 → 1.
- R2: Ric(g0) = (3μ'/(2r³)) dv dv, and the τr-block has determinant −1. Control: μ/r in place of μ/r².
- R3: K = 72μ²/r⁸, for constant μ and for μ(v); x_K = 1 at r_q; r_q ≤ √μ iff μ ≥ √72 l5². Controls: 48 in place of
  72 in either computation.
- R4: ℓ null and geodesic; the contractions of Proposition 2.2(d). Control: dv − 2 dr is not null.
- R5: (5.6): ρ parabolic in α, J symmetric hyperbolic in (ϖ, q), S, the speeds, ϑ³H. Control: α γ in place of
  a dr² brings ∂_r² a into ρ.
- R6: h²(c⁴ + s⁴) = 1; 4(a² + ab + b²) = (2a + b)² + 3b²; (3.1). Controls, each run on its own: h = 1;
  (2a + b)² + 2b²; r + r_q in place of r − r_q; √48 in place of √72.
- R7: λ = 10 l5 against the curvature length: 10 on x_K = 1, 2.91 and 0.92 at the horizon; against r: 1.85 and
  1.04 on x_K = 1, 1.00 and 0.32 at the horizon. Control: 48 for 72.
- R8: the mass law's coefficient for the solver's envelope, (2/9) ∫ env′² = 5π²/108, and the shell's mass 35/192.
  Control: sin² in place of sin⁴.
- R9: every row of Appendix D's md5 table matches its file at this commit. Control: one printed digit changed.
- R10: section 9's floor on the loss, d > 7.95 × 10¹⁵ and N > 1.66 × 10¹⁷, from δ_50 < 1.94138 × 10⁻⁸
  (`checks/epsind5.py` E3) and a charge of 3 per round, in exact rationals: ε_ind may be any number below δ_50 =
  1.94137057 × 10⁻⁸, and the floor is computed from the upper bound 1.94138 × 10⁻⁸. Control: a charge of 2.
- R11: section 9's one-derivative constants on the band, 963.4 for l ≥ 1 and 1516 at l = 0, from the certified
  bound 11.477 and multipliers, the square root bracketed exactly. Control: σ = 3 in place of 384.
- R12: (2.5′). Its components are the λ-linear part of the approximant the proof's programs compute with (R12 and R13
  import `ansatz5.py`, to show that (2.5′) is the object they compute with); it is traceless
  on the round S³; and with Proposition 2.3's quadratic part of R_vv and R2, the phase mean of its flux is
  (2/9) A² env² h² (c⁴ + s⁴) = (2/9) A² env², the law (2.6). Control: the map p1 = F, p2 = G.
- R13: the stage profiles the proof's programs compute (the leading waves and the second-order terms of
  `ansatz5.py`) carry no λ; and Proposition 3.2's uniform margin, −δ − (3.1) = (μ − μ0)/(c^(1/2)(μ^(1/2) + μ0^(1/2)))
  + r_q μ′/(2μ) with c = √72 l5², an exact identity whose terms are nonnegative. Controls: a profile carrying a
  factor 1 + λ; the sign of the μ′ term reversed.
- R14: the vacuum step of section 3: for any 4+1 metric and covector field D, with E := Ric − ∇_(μ D_ν),
  div(E − ½ g tr E) = −½ (□D + Ric(D)), checked exactly at a point for two random metrics (Minkowski plus a cubic
  polynomial vanishing there) and random quadratic D, every series truncated at the degree the point needs.
  Control: E − g tr E in place of E − ½ g tr E.

All fourteen pass and every control is rejected (about a minute). The proof's programs, in `docket68/n1star/`:

- `ks5.py` K1–K5: the Kerr–Schild form, its inverse, the commutator (2.4), div L0, the gauge source H0. 5/5;
  mutants 4/4.
- `foliation5.py` B1–B4: the null foliation, the slices and the domain. 4/4; mutants 5/5.
- `ansatz5.py` A1–A5: the ansatz to order λ² on Vaidya with phase v. 5/5; mutants 5/5.
- `lead5.py` L1–L5: stage 0: R^(−1) = 0, the energy condition, χ. 5/5; mutants 4/4.
- `data5.py` S0–S6: the slice data, the constraints' principal part, no coefficient of order λ⁻¹. 7/7; mutants 6/6.
- `horizon5.py` H1–H3, H2b: the expansion of the spheres for g0, no O(1) oscillation from a wave traceless on them
  (H2b: the approximant's wave, phase-shifted, symbolically), the phase constant along columns. 4/4; mutants 4/4.
- `mass5.py` M1–M4: the Hawking mass of the Vaidya spheres, the wave odd under the quarter-turn symmetry, the
  two-scale operator's equivariance, σ an isometry of g0. 4/4; mutants 5/5.
- `past5.py` P1–P8: Theorem 2's past domain, the operator and the transport near past null infinity, the leading
  wave's components, the stage-0 source, the rotations, the flux of the radiation field, the mollifier's commutator.
  8/8; mutants 9/9.
- `growth5.py` G0–G5: the go/no-go at 10 l5 on `hf_core5.py`'s scheme — two measures of K at every step, the failure
  of the scheme's premise on three grids and at three deeper excisions, a finite-difference amplification; G0 live,
  G1–G5 against the twelve pinned runs (`data/growth5_runs.json`, regenerated by `--run` and `--merge`); numerical. all
  pass.
- `settle5.py` T1–T6: the class's perturbation types, the potentials, the l = 2 ringdown against [CLY03b], the
  settling times, no growing mode for l = 2, …, 10, the late-time tail t^(−7) against [CYDL03]; T3, T5, T6
  numerical. 6/6; mutants 6/6.
- `wavegauge5.py` W1–W8: the passage to the harmonic gauge on five-dimensional Tangherlini in the class (supplement
  Propositions 10.2–10.3): the Lichnerowicz identity and Γ[π_X] = □X on a tensor and a one-form of the class, the l = 0
  stationary one-form regular at the horizon, the gauge-fixed mass change growing linearly in t, the scalar gauge
  vector's three 1+1 equations at l = 2 and 4, the tensor type already harmonic, the gauge-vector system triangular with
  every rung a scalar wave equation whose potential obeys Hung's positivity condition, and Hung's Proposition 4.2 in five
  dimensions (his components with the gauge condition admixed, the leading matrix's eigenvalues (l+a)(l+a+2), the
  horizon-regular rows with ∇_{L′} coefficients 2f′ and f′, l = 0), and the identities of his Proposition 4.1 in five
  dimensions (the radiation field's potential and its spectrum, the first-order term, the p-current, red-shift and
  T-current divergences, the angular eigenvalues on S³, the k-degree of the matrices, l = 0). 8/8; mutants 8/8 (about
  seven and a half minutes; the mutants about six minutes).
- `rungs5.py` M1–M5: the rungs of the gauge-vector system (supplement Propositions 10.4–10.5): the Morawetz identity of
  [HKW18] (123) at n = 3 for a scalar with potential and source, the positivity of its bulk for the Maxwell potential
  −4μ/r⁴ and the free rung with [HKW18]'s multiplier and half the angular term borrowed (a Sturm count on a polynomial of
  degree ten; the bulk coefficient alone is negative on part of the exterior), Hung's positivity condition with room, the
  radiation variable's leading potential k² + 3/4 and the p-current with the source, the g-current. 5/5; mutants 6/6
  (about half a minute).
- `growing5.py` G1–G5: the growing source (supplement section 10.7): Kodama–Ishibashi's master equation and
  reconstruction at n = 3 checked against the Einstein equations modulo the master equation; the gauge source in h_RW's
  components; the direct system for the gauge vector's components, Hung's (4.21)–(4.23) in five dimensions; the rung
  sources in canonical form with their bad weights; the substitutions, Hung's (4.27)–(4.30), and the residual sources
  with every weight checked, exact at the sample points. 5/5; mutants 5/5 (about twelve minutes).
- `lzero5.py` Z1–Z5: the l = 0 sector (supplement section 10.8): the identities of Hung's section 8 in five dimensions —
  the components of the one-form wave equation, the quantity P with its wave equation, the regular component with the
  red-shift sign, the horizon constant, the two radial ODEs and their singular solutions, the l = 0 substitution. 5/5;
  mutants 5/5 (about a quarter of a minute).
- `hierarchy5.py` H1–H4: the first rungs' rapid decay (supplement section 10.9): Hung's Proposition A.5 at k = 1 in five
  dimensions — the commuted equation of the radiation field, the current it enters, his conditions on the potential with
  the radii and constants at four modes, and the obstruction at the spherically symmetric mode. 4/4; mutants 6/6 (about a
  minute).
- `coupled5.py` K1–K6: the coupled estimate for the last two components of the gauge vector (supplement section 10.10):
  Hung's section 6 in five dimensions — his three identities and a fourth, the pair's matrix against his, the energy
  current with exact positivity, the Morawetz current for a pair and its bulk, positive for every mode without his
  substitutions and uniformly in the mode, and the r^p current. 6/6; mutants 6/6 (about a minute).
- `lzerorate5.py` Y1–Y5: the spherically symmetric sector by another route (supplement section 10.11): the commuted
  equation and currents at l = 0, the Hardy step on the outgoing leaf with its exact absorption identity, the window
  [δ, 1 − δ] at the null radius, the base hierarchy without an angular term, and the cut-off source of the l = 0
  substitution. 5/5; mutants 7/7 (about forty seconds).
- `damping5.py` U1–U6: the constraint damping of the nonlinear route in five dimensions (supplement section 10.12): the
  indicial families of Hintz's constraint propagation operator on 4+1 Minkowski from the definitions, his
  four-dimensional formulas as the control, the trace weight 2/(D − 2), the exact certificate at a point below the
  five-dimensional bound of Hintz's Lemma 4.4, h < e chosen here, the strip [−100, 2] free but for the Coulomb root and
  the roots accumulating only at infinity, his weight 1 failing, and a numerical survey over the damping parameters.
  6/6; mutants 6/6 (about eighty seconds).
- `semiclass5.py` W1–W6: the semiclassical inputs of Hintz's constraint damping in five dimensions (supplement section
  10.13): the fibrewise theory at the weight 2/(D − 2), the subprincipal symbol from its definition with his
  four-dimensional formulas as the control and one misprint named, the weight thresholds at the two critical sets
  shifted by 1/2, the interior saddle's positivity with the admissible e about 0.000069 v² against 0.000154 v² computed
  in four dimensions (his ≈ 0.000152 v²), and the admissibility of the certificate's point for that bound. 6/6; mutants
  6/6 (about a minute).
- `cform5.py` C1–C7: a constraint damping 1-form of Hintz's kind on five-dimensional Tangherlini (supplement section
  10.14): one explicit c in Kerr–Schild time, its subprincipal symbol computed on the Tangherlini metric from its
  definition, the conditions of his Proposition 5.1 at the certificate's point — past timelike, its dual pointing into
  the black hole inside the saddle and out of it beyond, positive at the saddle, and at the critical sets at infinity
  with the weight thresholds moved by e — and the smallest r₀ measured, 86 r_h, where his footnote gives roughly 81
  m/e^(1/2) on Schwarzschild. 7/7; mutants 7/7 (about a minute and a half).
- `gaugepot5.py` G1–G7: the gauge potential operator of the nonlinear route in five dimensions (supplement section
  10.15): its indicial roots on 4+1 Minkowski with Hintz's Lemma 6.6 as the four-dimensional control, its zero energy
  equations on Tangherlini for every l and the energy identities that leave the unmodified operator one zero energy
  state, the functional at the horizon that annihilates its range, and the pairings of his Lemma 6.11, 4π² against his
  4π, with his value reproduced. 7/7; mutants 7/7 (about a minute and a half).
- `modes5.py` M1–M5: mode stability of the 1-form wave operator — the gauge potential operator without its modification
  — at nonzero frequency on five-dimensional Tangherlini (supplement section 10.16): the operator equal to the Hodge
  d'Alembertian on every 1-form, and the master equations of scalar waves and of both Maxwell types on arbitrary
  harmonics, with potentials (f/r²)(κ + 3/4 + 9μ/(4r²)), (f/r²)(λ − 1/4 + 5μ/(4r²)) and (f/r²)(κ + 3/4 − 7μ/(4r²)),
  positive for r > r_h at l ≥ 1, and the spherically symmetric Maxwell sector settled by its own equation. 5/5; mutants
  5/5 (under a minute).
- `trap5.py` T0–T4: the trapping input of the gauge potential operator's high-energy mode stability in five dimensions
  (supplement section 10.17): its subprincipal operator −i∇ along the Hamilton flow, computed from the full symbol, the
  trapped set at the photon sphere r² = 2μ with expansion rate 1/r_ph per unit time, and Hintz's frame, whose connection
  along the flow is nilpotent on Tangherlini as on Kerr, so that a scaled inner product makes the skew part as small as
  wished. 5/5; mutants 5/5 (about 12 seconds).
- `thresh5.py` U1–U4: the structure and threshold quantities of the gauge potential operator in five dimensions
  (supplement section 10.18): its form −2∂_t* ρ(ρ∂_ρ − 3/2 − S̄) on 4+1 Minkowski with S̄ and its spectrum, Hintz's (1 −
  e)γ, 2γ, γ, at the trace weight 2/3; the horizon threshold 3/2 (deduced), also under the horizon modification of
  section 10.15; and Tangherlini's O(ρ²) approach to Minkowski. 4/4; mutants 4/4 (about 8 seconds).
- `hienergy5.py` V1–V4: the remaining five-dimensional inputs of Hintz's high-energy and Fredholm estimates for the
  gauge potential operator (supplement section 10.19): at the incoming radial set A_w + S̄ = D S̄ D, so the threshold is
  −1/2 − S̄ (deduced); at the photon sphere (Γ.1)–(Γ.3) with ν = 4(2μ)^(−1/2), β₀ = 2 and the gap (8μ)^(−1/2), and (Γ.4)
  with the loss δ_Γ(0) = (μη)^(1/2); and the global dynamics, with no ergoregion and dr future timelike inside. 4/4;
  mutants 6/6 (about 25 seconds).
- `lowenergy5.py` L1–L3: the five-dimensional inputs of Hintz's low-energy theory (supplement section 10.20): the
  transition face model on 4+1 Minkowski, the Helmholtz operator componentwise; its Bessel reduction, of order l + 1,
  whose outgoing solutions are excluded exactly for weights below 2 (the Hankel asymptotics numerical); and the weights,
  shifted by n/2 = 2, with the augmentation's terms ρ³ and ρ⁴. 3/3; mutants 4/4 (about 7 seconds).
- `cpmodes5.py` K1–K3: the five-dimensional steps of Hintz's deduction of the constraint propagation operator's mode
  stability (supplement section 10.21): its form −2∂_t* ρ(ρ∂_ρ − 3/2 − S̄^C) on 4+1 Minkowski at the trace weight 2/3,
  with S̄^C's spectrum h⁻¹{2(1 − v), (1 − e)(1 − v), 1 − v (three times)}; at the incoming radial set A_w + S̄^C = D
  S̄^C(−v) D, so that his (B.13) ℓ-window is the same (deduced); and the weights of his section 6 at n = 4, a mode's
  data in ρ^(−2−ε), α_sf = −C₀ − 5/2 and ℓ ∈ [−C₀ − 2, 0). 3/3; mutants 3/3 (about 5 seconds).
- `solv5.py` Q1–Q4: the remaining five-dimensional inputs of Hintz's solvability theorem for the constraint propagation
  operator (supplement section 10.22): Tangherlini in Kerr–Schild time is a three-body scattering metric whose
  Christoffel symbols decay as μρ³, two powers beyond what his calculus needs; dτ is past timelike near the initial
  surface for every T < 1, and dr future timelike inside the black hole; and his positivity conditions hold at the
  corner and the sink themselves at the weights (1, −C₀ − 5/2) for every C₀ ≥ 0, and on the spatial face for ρ_K ≤ 10
  at C₀ = 100. 4/4; mutants 4/4 (about 15 seconds).
- `tface5.py` F1–F5: the five-dimensional inputs of Hintz's transition face theorem (supplement section 10.23), at the
  parameter point and for C₀ ≤ 100: the constraint propagation operator on 4+1 Minkowski at the trace weight 2/3 is
  homogeneous of degree −2 under dilations; its weights at the origin are β ∈ (0, 2 + C₀], his (1/2, 3/2 + C₀]; the
  threshold at the cone face is α_cf > 0.0066 (0 as e → 0, his 1/2 recomputed in four dimensions), the sink's being the
  solvability theorem's, met; −½r²ℓ(dr/r) is his matrix with three angular copies, with positive eigenvalues; his choice
  of weights, data and closing integral carry over; the weights of both halves of tf-admissibility; and the free
  operator's roots and counts in his index-0 argument, with the adjoint's threshold from the conjugated adjoint's
  computed spectrum (tf-admissibility for β ∈ [−C₀, 2) deduced, provided the point's h lies below h₀). 5/5; mutants 8/8
  (about 25 seconds).
- `lin5.py` E1–E5: the five-dimensional indicial roots of Hintz's linearized gauge-fixed Einstein operator (supplement
  section 10.24): on 4+1 Minkowski its zero energy operator preserves the scalar, vector and tensor harmonic types, and
  his identity with the wave operator holds; on each type its determinant is (λ + l)(λ − l − 2) times the gauge
  potential operator's at λ − 1 and the constraint propagation operator's at λ + 1, over a factor that removes, at l ≤
  1, the roots the Killing 1-forms and the constraint propagation operator's roots 2 (scalar) and 3 (vector) give twice,
  every parameter symbolic, with his four-dimensional factorizations recomputed as the control; the factors are those of
  `gaugepot5.py` and `damping5.py`, and without damping the roots are integers outside (0, 2); at the parameter point,
  for l ≤ 12, the roots are simple, none has real part in (0, 1], each type splits evenly, and the kernel at 0 satisfies
  the gauge condition (deduced at the point: his Lemma 8.4 for every l, Lemma 8.5 and, but for one threshold,
  Proposition 8.6 for a small gauge parameter). 5/5; mutants 4/4 (about 50 minutes).
- `sbar5.py` S1–S3: the endomorphism of Hintz's Lemma 8.2 in five dimensions (supplement section 10.25): on 4+1
  Minkowski the linearized gauge-fixed Einstein operator differs from the wave operator, in its terms along ∂_t*, by 2ρ
  times a constant endomorphism, whose spectrum is the gauge potential operator's, the constraint propagation operator's
  and five zeros, its minimum 0 for every admissible parameter (the diagonal of his (8.8) recomputed in four dimensions
  as the control); so the decay improves to 3/2 − ε and the threshold keeps −1/2 (Proposition 8.6 deduced on readings,
  at the parameter point for a small gauge parameter). 3/3; mutants 3/3 (about a minute).
- `strap5.py` P1–P3: Hintz's Proposition 8.3 in five dimensions (supplement section 10.26): the subprincipal matrix of
  the linearized gauge-fixed Einstein operator at the trapped set, his printed 10 × 10 reproduced in all 100 entries
  with his sign convention, and with the supplement's after reversing one frame vector, in four dimensions; in five, the
  15 × 15 matrix with ten zero eigenvalues and −2(1 − e_C)γc₂, −2γc₂ (three times), −4γc₂, triangular in a constant
  basis, and for a damping 1-form without angular part block triangular in units on which the rotation of the angular
  plane is skew (strong trapping admissibility on Tangherlini deduced). 3/3; mutants 3/3 (a few seconds).
- `gmodes5.py` G1–G5: Hintz's Proposition 8.8 in five dimensions (supplement section 10.27): the linearized Ricci
  operator on Tangherlini reduced by the harmonics of the three-sphere, computed at a point for every harmonic — the
  tensor type's master equation with potential (f/r²)(l(l + 2) + 3/4 + 9μ/(4r²)), the vector type's with (f/r²)(l(l +
  2) + 3/4 − 27μ/(4r²)), the scalar type through Kodama and Ishibashi's first-order system, one constraint and their
  master equation, every potential positive at l ≥ 2, and l ≤ 1 pure gauge at nonzero frequency (the mode stability of
  the linearized Einstein operator, and with it the proposition, deduced). 5/5; mutants 5/5 (about five minutes).
- `zstates5.py` Z1–Z6: Hintz's section 6.5.1 and Proposition 8.9 in five dimensions (supplement section 10.28):
  Tangherlini's metric and Christoffel symbols against Minkowski's at orders 1/r² and 1/r³, the tortoise coordinate
  without a logarithm, the defects of the asymptotic translations (1/r³) and boosts (1/r²), the rotations Killing, the
  linearized mass-changing and rotating metrics — the derivatives of the Myers–Perry family [ER08], whose Ricci-flatness
  is checked at exact points — with their gauge sources at 1/r³ and 1/r⁴, and the exponents 1 and 2 off the indicial
  roots of the gauge potential operator, four-dimensional Schwarzschild the control (the zero energy states and the
  gauged metrics, without logarithms, deduced). 6/6; mutants 7/7 (about half a minute).
- `genstates5.py` H1–H5: Hintz's Lemma 6.13 and the first three classes of his generalized zero energy states in five
  dimensions (supplement section 10.29): on the time translation, the boosts carried to second order and the rotations,
  their leading terms solved exactly on Minkowski space with the gauge modification, the time translation's source on
  Tangherlini without the sub-leading term that gives his logarithm, his printed four-dimensional numbers reproduced as
  the control, and the top of the indicial gap (the lemma, on the five-dimensional reading of [Hin26c]'s section 9, and
  the states deduced). 5/5; mutants 8/8 (about a minute).
- `puregauge5.py` J1–J6: Hintz's Proposition 6.18 (4)–(7) in five dimensions (supplement section 10.30): the indicial
  families of the gauge potential operator on the harmonic types through l = 5, his Lemma 6.6 matrices and his
  symmetric-gradient families reproduced in four dimensions, his four classes of growing roots with their ranges, the
  symmetric gradient injective at each, no resonance for 0 < z < 4, the generalized states' leading terms exact on
  Minkowski space, and at zero gauge modification which coincidences force a logarithm (the proposition deduced). 6/6;
  mutants 7/7 (about four minutes).
- `dual5.py` A1–A3: Hintz's section 7.2 in five dimensions (supplement section 10.31): the indicial roots of the adjoint
  constraint propagation operator, the translations' dual state, and the rotations' near zero rotation at first order on
  the Myers–Perry metric, his (7.8), (7.10), (7.18), (7.20) and (7.31) reproduced in four dimensions (his lemma and
  proposition deduced). 3/3; mutants 3/3 (about a minute and a half).
- `pairing5.py` P1–P5: Hintz's Lemma 8.12 in five dimensions (supplement section 10.32): the pairings of the zero energy
  kernel and cokernel as boundary pairings at infinity, [Hin23b]'s four-dimensional table reproduced, the
  five-dimensional 11 × 11 matrix non-degenerate (his Proposition 8.11 and Corollary 8.13 deduced, up to the
  five-dimensional rigidity, which `static5.py` supplies at zero rotation). 5/5; mutants 6/6 (about three and a half
  minutes).
- `static5.py` S1–S6: [AHW24] Theorem 6.1(2) in five dimensions at zero rotation (supplement section 10.33): the
  stationary solutions of the linearized Einstein equation on Tangherlini, harmonic by harmonic at zero frequency — the
  tensor and vector types' energy identities, the scalar type's flow and master equation in Kodama and Ishibashi's
  variables (their static system and master variable, identically), the mass and time rescaling at l = 0, the rotations
  at vector l = 1, pure gauge at scalar l = 1, and the ingoing forms (the theorem, and Hintz's Proposition 8.11 at
  Tangherlini and, on a reading, near it, deduced). 6/6; mutants 7/7 (about a minute and a quarter).
- `physical5.py` Y1–Y4: Hintz's section 8.5 in five dimensions (supplement section 10.34): the stationary equations
  hypergeometric in r²/μ, the solutions smooth at the horizon and their growth like r^l, the roots his construction
  needs, and the rotation equivariance behind his Lemma 8.15 (his Proposition 8.14 at Tangherlini deduced, and near it
  on a reading). 4/4; mutants 5/5 (about twelve minutes).
- `window5.py` W1–W3: Hintz's window in five dimensions (supplement section 10.35): the indicial roots in [−3, 0] in
  four dimensions, his Lemma 8.4's and the terms of his (9.32), and in five, the same and the tensor types, from the
  determinant itself, and the constraint operator's only in four dimensions at zero; the bookkeeping of decay orders at
  the Kerr face that returns (9.32) at his order 1 at timelike infinity; and the radiative and Coulombic orders of the
  flat wave operator in d + 1 dimensions, with the bookkeeping at 3/2 and 2 (the window [α − 4, 0] and the states at −2
  alone deduced). 3/3; mutants 4/4 (about twenty-five minutes).
- `mp5.py` M1–M5: Hintz's section 7.2.1 in five dimensions at every spin (supplement section 10.36): the Myers–Perry
  metric in Kerr–Schild form over so(4), Ricci-flat at exact rational points; his Lemma 7.5 as an identity of the
  family, symbolically and on the full metric; its expansion, the leading term spin-independent; the Killing rotations;
  and the leading term of his h♯ independent of the coordinates (his Lemma 7.5, Proposition 7.4 and (7.19) at every spin
  deduced; Kerr the control). 5/5; mutants 5/5 (about three minutes).
- `iota5.py` I1–I5: Hintz's section 9.1 in five dimensions (supplement section 10.37): the model at timelike infinity by
  harmonic type from `lin5.py`'s operators; a connection determinant through z = s/(s + 2), the free wave's pure
  resonances 3 + l + k and his u₃ reproduced; on the constraint operator the argument principle and the moment identity
  of the descent; at the parameters used, the zero energy roots below 3/2 and the constraint operator's roots in (2,
  5/2) for l ≤ 400; the spherical candidate a pure resonant state at γ_C = 10 and 100 (the descent, the injectivity
  below 1 + ε_ind and no pure resonance at or below 2 deduced). 5/5; mutants 6/6 (about twenty-five minutes).
- `scri5.py` C1–C3: Hintz's (5.27)–(5.28) and Proposition 5.14 in five dimensions (supplement section 10.38): his matrix
  at null infinity at the background in his splitting, his printed four-dimensional matrix reproduced, the diagonal and
  the coupling of the 01-component into the 11-component his, four trace couplings changed; the exponents at null
  infinity by harmonic type; at the radiative exponents, no resonant state at timelike infinity at γ_C = 10 and 100 (the
  perturbation's couplings half an order lower, the radiative order excluded at timelike infinity and α = 2 deduced, on
  readings). 3/3; mutants 4/4 (about twelve minutes).
- `aug5.py` A1–A3: Hintz's section 10.1 in five dimensions (supplement section 10.39): on Minkowski space the gauged
  mass and rotation states with no logarithm, his four-dimensional logarithm reproduced; the augmentation's entries of
  degree −3 and −4, his −2 and −3 reproduced in four dimensions; the cut-off states of order 4 and 5 at timelike
  infinity, his borderline 3 and 4 in four (the entries in the target space, his device for the angular momenta for
  every state, the invertibility and 2-admissibility deduced, on readings). 3/3; mutants 4/4 (about 8-12 minutes).
- `lowfreq5.py` W1–W3: Hintz's section 10.2 in five dimensions (supplement sections 10.40–10.41): on Minkowski space the
  time derivatives of the columns that carry the poles have the states as their zero-frequency values, of weights 0 and
  1, his −1/2 and 1/2 reproduced in four dimensions; the weights of his proof at 598 points, with the requirements at
  the outgoing radial set read from his Fourier transform's orders: −ε, 1 − ε and the last α_sf in five dimensions — no
  loss — and his −1/2 − ε, 1/2 − ε and −3/2 − ε in four (2-admissibility with no loss deduced, on readings); and the
  density shift in his companion paper's bound (13.30a), 3/2 in four dimensions and 2 in five, its rule reproducing his
  printed instances. 3/3; mutants 7/7 (about 5 seconds).
- `cone5.py` C1–C3: Hintz's section 11.1 in five dimensions (supplement section 10.42): the unweighted b-density's
  shifts at null infinity, timelike infinity and the Kerr face, 2, 5/2 and 1/2 for his 3/2, 2 and 1/2, his
  four-dimensional values reproduced; the background's differences at timelike infinity — mass, rotation, boost — of
  orders 2, 3 and 2 for his 1, 2 and 1; the cut-off mass interpolation's curvature of order 4 for his 3 (the patched
  background's, the admissibility and the forward solutions with no loss deduced, on readings). 3/3; mutants 3/3 (about
  ten seconds).
- `class5.py` C1–C3: the class in Hintz's construction (supplement section 10.43): of the fifteen Killing fields of 4+1
  Minkowski space only ∂_t is G-invariant (three under the torus alone); one invariant scalar harmonic of S³ at each even
  l and one invariant transverse traceless tensor harmonic at each even l ≥ 2, none at odd l, and no invariant
  divergence-free 1-form, for l ≤ 8, the counts made exact by a second method's upper bounds (his Steps 2 and 5 reduced
  to his Propositions 11.20 and 11.51, deduced). 3/3; mutants 5/5 (about forty seconds).
- `iplus5.py` P1–P3: Hintz's section 11.2 in five dimensions (supplement section 10.44): the leading part of the normal
  operator at null infinity, −(ρ_I∂_ρI − 3/2)(ρ_I∂_ρI − ρ₊∂_ρ₊) for his 1, the remainder in ρ_I Diff_b; the exponents
  of the five-dimensional source term, the exceptional exponents 2 and 3/2 + (1 − e_Υ)γ_Υ for his 1 and
  1 + (1 − e_Υ)γ_Υ, and the non-resonance γ_Υ ≠ 1/4 his steps need. 3/3; mutants 3/3 (a few seconds).
- `sharp5.py` K1–K4: Hintz's sections 11.7–11.8 in the class (supplement section 10.46): the class's types and their
  roots in [−3, 0]; for every exponent at timelike infinity from α_min to 3, the pure gauge terms eliminated and
  recorded and no physical state, his eight parameters and his four-dimensional terms reproduced; his weights 3 + ε in
  the five-dimensional gaps (his Proposition 11.51, Theorem 11.59 and Corollary 11.66 deduced in the class, the forcing
  at order 3 + ε_K at the Kerr face). 4/4; mutants 4/4 (about nine minutes).
- `general5.py` G1–G2: settling without the class (supplement sections 10.61–10.63): Hintz's bookkeeping over every
  five-dimensional harmonic type with his two orders of loss at the Kerr face — six pure gauge classes eliminated,
  fourteen recorded, the physical states of scalar, vector and tensor type at l = 2 recorded with no companion, his
  four-dimensional lists reproduced; and the Poincaré charges of the translated, rotated and boosted Myers–Perry family
  at Tangherlini, their 15 × 15 Jacobian diagonal with determinant (3π/8)(πμ/4)⁶(3πμ/8)⁸, [CD03]'s (F.4)–(F.6)
  reproduced in four dimensions. 2/2; mutants 2/2 (a few seconds).
- `exterior5.py` X1–X8: [Hin23a]'s section 3 at n = 4 (supplement section 10.64): every place the dimension enters, at n
  = 3 against his printed values and at n = 4 — the conjugated wave operator's term ((n − 1)(n − 3)/4)r^(−2), 3/4 at n =
  4; the b-density ρ0⁵ρ_I⁴|dg|; the energy form (3.25) with the angular operator ∆ + 3/4; the gauge endomorphism (2.11)
  from his Definition 2.2's operators, his matrix and five intermediates at n = 3, the duality of his Remark 2.3 at
  both, the diagonal 2γ_C, γ_C, (3/2)γ_C, −(3/2)γ_Υ, −γ_Υ, 0, −2γ_Υ at n = 4; the quadratic radiation term of R_11 at
  r^(−2k), r^(−1/2) below the linear terms at n = 4; the Sobolev counts; the metric-dependent entries of Proposition
  3.29, his four printed ones at n = 3 and r^(−1/2) times them at n = 4; Lemma 3.6's compactification, x̄_I = min(√3/2,
  1/(2μ^(1/4))) and (3.8) negative. 16/16; mutants 6/6 (about forty-five seconds).
- `gluing5.py` D1–D4: [CD03]'s gluing and Hintz's boost at n = 4 (supplement section 10.66): the Killing fields of
  R^(1,n), ten and fifteen; the charges carried to the gluing annulus, R^(−(n−2)) for energy and momentum and R^(−(n−1))
  for angular momentum and centre of mass, so that the errors' conditions are [CD03]'s (E.5b) and (E.9) and, at n = 4
  only, decay faster than r^(−3/2) replaces parity; the weighted indices of its proof, s = t + n − 2; the boost as the
  Lorentz boost of rapidity c/2, pulling the mass term back to μ r^(2−n) a^n (dt*)², Hintz's h_(S,11) at n = 3 and
  r^(−2) at n = 4. 4/4; mutants 4/4 (about fifteen seconds).
- `edge5.py` E1–E4: [Hin26c]'s sections 7–8 and 9.3 at n = 4 (supplement section 10.67): the wave operator in edge
  coordinates at null infinity, its first-order term x_I∂_(x_I) − (n − 1); the K-current of his energy estimate, his
  (8.10) at n = 3 and the threshold α_I < −1/2 unchanged at n = 4; the rotation fields of S^(n−1); the densities and
  counts. 4/4; mutants 4/4 (a few seconds).
- `censusweep.py`: a second census of the passages carried to n = 4 (supplement section 10.69): every marker of the
  dimension on every page, 278 on the 205 pages swept, each read against the supplement's sections. It runs where the
  alphaXiv full texts have been fetched; they are not stored here.
- `synth5.py` S1–S3: the harmonic sums of the gauge 1-forms (supplement section 10.73): on five-dimensional
  Tangherlini the scalar and vector gauge 1-forms have coefficients r/k, r²/k², 1/k and 1/k_V, and k² = l(l + 2) ≥ 8 for
  l ≥ 2, so the sums over harmonics converge. 3/3; mutants 3/3 (about forty seconds).
- `iplusnorm5.py` N1–N9: [Hin26c]'s Theorem 10.1 at n = 4 (supplement sections 10.58 and 10.75): the
  normal operator at future timelike infinity with the constant (n − 1)/2, every radial point threshold of
  its high-energy estimates, the densities and their shifts n/2 and (n + 1)/2, the Fourier step to the
  transition face, and the counts. 9/9; mutants 9/9 (seconds).
- `hthresh5.py` T1–T8: the damped operator's threshold at the horizon, [Hin26c] (5.17), at the parameter point of section
  8.5 (supplement section 10.79): the normalisation r_h/2, the adjoint from the operators' definitions with the metric
  pairing as its control, the undamped part in Lemma 3.3's inner product with spectrum ±(e^(1/2) + e^(−1/2))/r_h, the
  damping's −h⁻¹ℓ(dr), and 1/2 + ϑ = −4995.33… at h = 10⁻⁶, below −100 for every h under 2.62 × 10⁻⁵; in other fibre
  inner products of the same family it can fail (positive at e′ = 10, crossing −100 at e′ ≈ 7.76), so it holds in the one
  the write-out fixes. 8/8; mutants 8/8 (about half a minute).
- `tfnorm5.py` R1–R4: Hintz's transition face normal operator and uniform low-energy estimates ([Hin26c] Theorems 9.38
  and 9.41, Corollary 9.39) at n = 4 (supplement section 10.80): the conjugated adjoint (9.117) at every n, with one
  misprint of an intermediate line named, the indicial roots −λ and −n + 2 + λ̄, the densities' shift n/2 in the
  embedding and in (3.46), and (9.122)'s leading part. 4/4; mutants 4/4 (seconds).
- `iotasol5.py` J1–J6: Hintz's solution theory at future timelike infinity and at the transition face ([Hin26] section 9)
  at n = 4 (supplement section 10.82): the model from the wave operator with (n − 1)/2 for his 1, the exponents and
  thresholds at v = 0, the Fourier step to the transition face operator, the outgoing end of that face, and the weights
  at null infinity. 6/6; mutants 6/6 (seconds).
- `bundlesweep.py` W1–W4: a second census, by token sweep of the full text, of every step of Hintz's spectral theory
  ([Hin26c] section 9) that uses a scalar operator, each of the 38 items, proofs and subsections with a marker placed
  (supplement section 10.85). 4/4; mutants 4/4 (seconds).
- `bundle5.py` E1–E6: the calculus facts behind that section's proofs re-run on bundles (supplement section 10.86), in
  model cases (2 × 2 operators on the line; the energy identity on R^(1+1) with X Killing, u real and h constant): a
  scalar commutant keeps a commutator's principal part scalar, the imaginary part is first order and self-adjoint in the
  fibre inner product, positive square roots, the trace bound for matrix-valued defect measures, the energy identity with
  a connection, and sums of squares in a fibre inner product. 6/6; mutants 6/6 (seconds).
- `eind5.py` E1–E2: Hintz's Lemma 8.4 for every l (supplement section 10.52): every indicial root of the linearized
  gauge-fixed operator simple for l ≥ 2, exactly, in the scalar, vector and tensor types; his distance condition (8.13)
  by a certificate beyond l = 10⁴ and a 30-digit scan below, least distance δ_50 = 1.94137057 × 10⁻⁸
  (`checks/epsind5.py` E3), so ε_ind may be any number below it. 2/2; mutants 2/2 (about four
  minutes).
- `uniform5.py` H1–H2: the constraint damping at every h in (0, 10⁻⁶] (supplement section 10.54): `damping5.py` U4's
  line-crossing certificate with h a second parameter — the shifted constant coefficient and the Hurwitz determinant
  at Re λ = −100, 19/10 and 2, their critical values in h free of roots — so that no indicial root of the constraint
  propagation operator has real part in [−100, 2] but the simple Coulomb root 2 at l = 0 and 1. 2/2; mutants 2/2 (about
  twenty seconds).
- `transfer5.py` T1–T2: five-dimensional Tangherlini against its Minkowski model (supplement section 10.55): g =
  η + (μ/r²) k ⊗ k exactly, k = dt + dr null, Ric(g) = 0; every Christoffel symbol μG₃ + μ²G₅ with G_j homogeneous of
  degree −j, two orders below Minkowski's connection; g⁻¹(dt*, dt*) = −4μ/r² with t* = t − r; the damping 1-forms of
  the static and Kerr–Schild times differing at order r⁻³. 2/2; mutants 2/2 (about four minutes).
- `hung4.py` C1–C3: the four-dimensional control of W7, Hung's Proposition 4.2 recomputed from the Schwarzschild metric
  with the instrument W7 runs, reproducing his printed rows and naming two misprints in the printed combinations, and
  the red-shift divergence of his (2.13) at r = 2M for one component (C3). 3/3; mutants 4/4 (about two and a half
  minutes).
- `bondi5.py` B1–B4: Theorem 3's hierarchy in the Bondi form with general coefficients from the first order (the
  orders below the waves' vanish; the mass law from R_vv at order r^(−3)), the chart from the wave-gauge expansion,
  the Hawking mass of the Bondi spheres, the numerics' coefficient; B4 numerical. 4/4; mutants 5/5 (about ten minutes,
  B2 the slow one).


Earlier programs cited, in `docket68/lemmas/`:

- `hf_theorem5.py` F1–F5: the horizon of the limit, (iv) with Z3, the dust (Wolfram Language, Lean 4), the
  numerical rates. 7/7.
- `counterpart5.py` P1: K = 72μ²/r⁸ and the bound λ < l5/10 for the high-frequency regime. 8/8.
- `kn_gauge.py` K1–K2: the reduction in other variables. 18/18.
- `hf_core5.py`: the numerical sequence at two seeds (rates; one zero per column). 10/10; numerical, not exact.
- `seed_escape.py` E1–E5: the barrier of the hole and its linear scattering at the wavelength 10 l5.

Programs behind section 9, in `docket68/n1star/`:

- `checks/thetain5.py` T1–T6: the incoming radial threshold of the transition-face model, ϑ_in = 0 (the ∂_t*
  endomorphism in the incoming time has spectrum ≥ 0 containing 0, and is semisimple), the two 1-form operators'
  (negative), and the losses it fixes: 1 for the model's inverse, 2 for (2.3)–(2.4) of the loss count. Exact; the
  reduction from the definitions and the choice of regularity deduced. 11/11 with controls (about 25 seconds).
- `checks/prop31loss5.py` Q1–Q4: the step counts behind the round charges 15 and 17. Exact. 5/5 (seconds).
- `checks/e2trapband5.py` B1–B3, run to σ = 384 (`checks/e2trapband5_384.out`, 194 minutes): the band bound
  11.477, certified in interval arithmetic; `checks/e2h1band5.py` W1–W3: the one-derivative constants on the band,
  exact rationals (`checks/e2h1band5.out`). 3/3 each.
- `checks/closure5.py` K1–K5: the closure properties of the expansion at past null infinity (K1 and K5 exact at
  five points, K4 an enumeration of the weight patterns). 9/9 with controls (about 17 seconds).
- `dnsolve5.py` with `checks/g1curv5.py`: the double-null prototype at the prescribed wavelength and its
  curvature comparisons. Floating point; computed, not certified.
- `checks/data5two.py` T1–T11: the constraint map's linearisation with two families, on flat, Vaidya and static
  backgrounds. Exact.
- `checks/support5.py` C1–C6, C8, C9: Ric^H's second-derivative structure and (5.1)'s λ⁻¹ coefficient (exact),
  Lemma 5.1 and supplement Lemma 3.3 on the stage-0 profile of `lead5.py` (exact), the mollifier's annulus (Z3 over
  the reals), the bootstrap's power counting as a ledger (C5, exact; failing at K = 5), the time lines of section 5.4
  (exact), the boundary's first-order term for g_λ (exact) and m1's source odd under σ, in `ansatz5.py`'s Bondi-type
  gauge (C9, exact), each with a control that must fail. About a minute.
- `checks/support8.py` K1, K8: section 8.1's two steps. K8, the class of [Hol08] and the class (2.1) meet only in
  spherical symmetry: the squashed sphere's dφ1 dφ2 coefficient is 2c²s²(e^(−4B) − e^(2B)), zero for cs ≠ 0 exactly
  at B = 0; control, e^(2B) on the fibre. K1, the base of supplement 10.50(a): every oscillating profile of
  `ansatz5.py` and `lead5.py`'s leading wave carries the envelope and vanishes where it does, and χ's transport source
  is quadratic in it; control, a profile with an envelope-free term. Exact.
- `checks/csolve5.py` C7a–C7c: the constraint solve's λ^(N−2) scaling (supplement Lemmas 6.3–6.4, Proposition 6.5): no
  coefficient of order 1/λ in the linear or the quadratic part of the constraint map at the stage-0 approximant's data
  (C7a, exact); the linear solve's rates λ^(N−2), λ^(N−2), λ^(N−3) for U, ∂_r U and ∂_r² U (C7b); the nonlinear scheme's
  first contraction ratio d_1/d_0, 6.8 × 10⁻³, 5.8 × 10⁻⁴, 3.5 × 10⁻⁵ at λ = 1/8, 1/16, 1/32 (rates 3.55, 4.03, at least
  the proof's λ^(N−3); the rate test's tolerance accepts 2.8, a 1/λ² term failing it), and its first correction at
  λ^(N−2) (C7c), floating point. Controls: an oscillating trace on the spheres (C7a, C7b), a 1/λ quadratic coefficient
  with nonzero phase mean, which slows the first correction by an order (C7c). About two hours.
- `checks/eindcert5.py` I1–I2: the scan of `eind5.py` E2 below l = 10⁴ made rigorous: every root it visits enclosed by an
  inclusion disc computed in exact rational arithmetic (the gauge potential's quartic for l ≤ 60), δ_50 certified,
  attained by the gauge potential's operator at l = 50, its disc inside |λ| ≤ 50 (I1); for l ≥ 52 no root of the gauge
  potential's quartic has |λ| ≤ 50, its roots in s = λ′(λ′ − 1) increasing in z from their values at z = 0, so |λ| ≥ l −
  1 (I2). Controls: a planted root 10⁻³⁰ from the integers and discs seeded off x² − 1's roots (I1); the z terms' sign
  flipped (I2). About twelve minutes.
- `checks/kirecon5.py` P1–P2: supplement Proposition 10.1 (iii)'s coefficients, bounded on r ≥ r_h uniformly in l for the
  master field normalised as r^(3/2) Φ (P1), and O(r^(3/2)) and O(r³), uniformly in l and attained, in the fields [HKW18]
  bound, Φ and r^(−3/2) Φ (P2). Controls: the monomial test on Φ, which must find the r^(3/2); the bound r¹ in Φ. Exact;
  about half a minute.
- `checks/mpdata5.py` B1–B4: the data of translated, rotated and boosted Myers–Perry metrics lie in the class of
  supplement Part VII Lemma 0.1, ρ²C^∞ and ρ³C^∞ of the radial compactification. Controls: a mass term falling as ρ (B1,
  B4); a split-signature form, which vanishes on the sphere (B2); the projection term dropped (B3). Exact series; about
  four minutes.
- `checks/flux5.py` F1–F3: the flux 6π²m of the Kerr–Schild slice (F1–F2) and the glued mass bound's ingredients (F3: R⁶
  q_2 = −10294529/36000, the annulus volume 255π²R⁴/2, |δm| ≤ C η (R² + 1)/(6π²R² − C) for C < 6π²R²; the bilinear
  difference bound of step (6) is argued, not computed) (supplement Part VII Lemma 2.1 (c), Proposition 2.2 step (6)).
  Controls: the flux with the trace term's sign reversed; the curvature without its Γ·Γ terms (F3). Exact; a few minutes.
- `checks/vii5census.py` V1: an enumeration for (VII5): every line of Parts III–IV that names an averaged or equivariant
  choice by one of thirty-three printed symbols -- the cut-offs (χ_K, χ_r, χ_∞, χ_−, Θ and those inside t♭_* among them),
  the states and towers of III.G'' Table 1.1 as maps (h̆, h^(μ), h_(b,s1), h^(0)_(b,s0), h^(−2)_b, h^(≤k)_(b,s1),
  h^(≤k)_(b,v1)) and their domain -- each symbol's own site marked as its site, not as a use; the reading it makes finite
  is recorded in `checks/VII5-READING.tsv` (next entry). Control: every symbol must be found at its site, so a planted
  symbol and a site moved, to another file or to other lines of its own, are reported. A second.
- `checks/vii5read.py` Q1–Q2: the reading (VII5) asks for, held against that census. Q1, `checks/VII5-READING.tsv` has
  exactly one row for each of the 577 lines naming a choice of (C3), (C3′) or (C4) outside its site, with the census's
  symbols, a verdict (SITE-ONLY 311, NAMING 189, HOMONYM 72, UNDECIDED 5, MORE 0), a note where one is required, and the
  symbol still printed on that line; Q2, every undecided row carries its resolution (the amended Lemma 3.1). Controls: a
  row dropped, a row doubled, a verdict misspelt, a resolution removed, and the census widened by one radial cut-off must
  each fail. The verdicts are three readers' readings, not computed. A second.
- `checks/hclass5.py` H1–H2: the h-dependence of the conclusions drawn at the parameter point, by class: the quantities
  proportional to 1/h, A_0's diagonal among them, positive at the record's signs (c_2 < 0) and growing as h falls on (0,
  10⁻⁶] (H1); for l ≤ 20, box^C's discriminant (simplicity), its values at the integers |n| ≤ 52, the vector quadratic
  and the resultant with Q(λ − 1), each a nonzero polynomial in h but three that vanish identically (the roots λ = 1 at l
  = 0, 1 and λ = 2 of the vector type at l = 1, integers for every h), their roots in (0, 10⁻⁶] counted by Sturm: none,
  which H2 requires (H2; at l = 1000 the vector quadratic has one, h = 1/1001992). The distance condition (8.13) is
  `checks/re813.py`'s. Controls: h itself; the sextic times (λ − 3). Exact; a few minutes.
- `checks/epsind5.py` E1–E3: ε_ind at the parameter point of section 8.5 (z = 4 × 10⁻⁶). E1, the non-integer roots
  lie δ_l from an integer with δ_l → 0, so read over every l no positive least distance exists; E2, the finite
  reading, roots with real part in [−10, 10]; E3, the least distance from Z of the non-integer roots with |λ| ≤ 50,
  δ_50 = 1.94137057 × 10⁻⁸ (7.3846 × 10⁻⁸ over l ≤ 12). Control: at z = 0 every root is an integer. Exact, mpmath at
  50 digits.
- `checks/e2meas5.py`: the resolvent norm ‖χ_I R_l(σ) χ_I‖ measured at σ = 96, 128, 160 and 192 over the 13 harmonics
  around the first whose barrier top lies above σ², for comparison with the certified band bound. Floating point (a
  numerical ODE solve), not certified; one to two hours per σ.
- `checks/support9.py` S3, S6: the census of the arguments that give no number (contradiction, compactness, Fredholm and
  their kin over the write-out's parts) and the ledger's classes recounted (S3, a text census); (4.1) for a generic
  profile, all fifteen components functions of (s, v, r, θ) shifted by a symbolic c, the λ⁰ parts nonzero in all fifteen
  and the λ⁻¹ parts identically zero (g0^vv = 0) (S6, exact). Controls: an absent word; W_vv not shifted. About five
  minutes.
- `checks/charge5.py` G1–G2: the charge of a round for larger ℓ_I by `checks/prop31loss5.py`'s rules with d_G = 7 + 2⌈ℓ_I
  − Re λ⌉ per ℓ_I: 15 on (3, 3.5), then 4 more for each unit of ℓ_I, 19, 23, 27 and 31 to ℓ_I = 7.5 (17, 21, 25, 29 on [k
  + 1/2, k + 0.5099]); a sufficient charge, not a shown minimum (G1); d_G = 9, 11, 13, 15 at the loss record's own points
  (G2). Controls: windows of width 1/2 (J exactly {3}); d_G frozen at 11. Exact rationals; under a minute.
- `checks/eqlayer5.py` L1–L2: the equality layer for a flat-edged envelope: the margin o((v − v_s)^k) for every k tested
  and positive, bounded below by a multiple of env² (L1, read from the lower bound); env' and env'' not bounded by the
  margin's order (L2). Controls: an envelope with an edge of finite order (L1); env = 1 + x, for which the ratio stays
  bounded (L2). Exact; a few seconds.
- `checks/e2lower5.py` E1: certified lower bounds for ‖χ_I R_l(σ) χ_I‖ by test functions with compact support in I, and
  the ratio of the certified upper bound to them. Control: a test function vanishing only to first order at the ends.
  Exact; about ten minutes.
- `checks/twodomainx5.py` X1–X2: the two-dust background's exit range on the earlier rectangle (X1) and the background on
  a rectangle reaching Σ_−1.5 with the outgoing data moved to an earlier cone, its constraint residuals converging at
  second order away from the steep inner boundary (X2). Control: data off the constraint. Floating point; under a minute.
- `checks/stage5.py` S1–S3: the approximant's stages in the proof's gauge, from `lead5.py`'s reduced Ricci carried to
  order λ¹ (its orders λ⁻¹ and λ⁰ reproduced exactly). S1, with generic stage-1 and stage-2 unknowns, in the eight
  components the symmetry leaves: (5.2)'s e1, e2 are the λ¹, λ² parts of ḡ⁻¹(du, du); in R^(1) the profile after next is
  absent, m2 and φ2 enter only through −½ e2 ∂_θ² W, g2 only through −(ℓ · ∂)∂_θ g2 − ½ e1 ∂_θ² g2 and terms with no
  X-derivative and at most one ∂_θ, the second derivatives of m1 only in −½ □̃ m1 and of φ1 only in −½ (□̃ φ1) ∂_θ W; S2,
  m1's source, the phase mean of R^(1)[g0 + λW] with χ from its transport, nonzero only in dv dθ, −(4/9) A² env² H² sin
  2θ/r³, and σ-odd, g1 = W S-odd; S3, the same source with χ carrying no radiation at past null infinity. Not computed:
  order λ², the other seven components, m1 from past null infinity. Controls: the non-null phase v + r/3 (six of the
  eight structural checks fail); one quadrature (g1 no longer S-odd; the source alone stays odd). About forty-five
  minutes.
- `checks/excise5.py` E1–E2: `growth5.py`'s deeper excisions on the next finer grid (Ny = 28 at μ0 = 100 l5², Ny = 20 at
  1000 l5²), the breakdown read by `growth5.py`'s criterion (a second zero of the round spheres' expansion lasting 0.01
  in v, or W ≥ 0 at the boundary): from v = 1.41033, 1.35549 and 1.52374, moved by 0.00076, 0.00251 and 0.00020 from the
  single grids (the standard excision by 0.0041 and 0.0004), all before the standard excision on both grids (E1); the
  order the same for every duration from 0.005 to 0.06, the y = 2 run moving 0.0083 at 0.04 (E2). Control: each deeper
  run replaced by its seed's standard run, which the order must reject. Floating point (the solver's scheme, not
  certified); the runs one to three hours each, the check seconds.
- `checks/gauge5.py` G1–G3: the gauge field. G1, supplement (6.2) exactly at a point of a random 4+1 metric over a random
  background, D = 0 imposed along the slice, with `paper/response5.py` R14 rerun; G2, the order-λ gauge field D^(1) in
  `lead5.py`'s coordinates with m1, the next oscillating profile and φ1 generic: D^(−1) = D^(0) = 0 off the slice, the
  next profile entering D^(1) only through Pol(∂_θ ·), and on the slice Lemma 6.2's stage-1 choices kill the oscillating
  part and the mean (a linear system in ∂_τ m1 of determinant −(r² + μ)⁵/(2r¹⁰)); G3, an r⁻² amplitude on a v-strip of
  fixed width has L² norm at most π(2d1)^(1/2) t^(−1/2), the rate sharp, and r² D^(1) bounded at leading order with m1
  generic. Not computed: (F2) at order 1, D^(2), Lemma 6.1's propagation off the slice; Pol⁺ taken in
  Eddington–Finkelstein components. Controls: (6.2) without its Z term, and on a slice with ∂_i D ≠ 0; no choices, Pol^T
  for Pol⁺; amplitude r⁻¹, W(ℓ, ·) ≠ 0. About five minutes.
- `checks/support8c.py` K1–K4: section 8.4–8.5's deduced steps. K1, the Frobenius exponents at r_h of the scalar wave,
  P_0, box^C and 2L at the record's point (0 with the damping's negative ones, the σ part iσ, free of the angle), so the
  solutions smooth at r_h are the exponent-0 family (at γ = 0, 2L has 1 at σ = i, which the lemma does not use); K2, the
  kernel elements' decay class 3/2 + S̄ at n = 4 for his 1 + S̄; K3, box^C's roots with real part in (5/2, 13/4] (2,771
  for l ≤ 1200, none at l = 10⁴, 10⁵; 614 tower images), exactly 3 only the vector l = 1 root, the nearest above 3 +
  2.932 × 10⁻⁶ > 3 + ε_ind; K4, the exponent 2 of the quadratic radiative term from its indicial equation, coefficient
  −12/25 at the point (his 1 at n = 3; the Ricci part). Controls: box^C's damping sign reversed; the wrong density; a
  root at 3 + 10⁻⁹; decay r⁻². About nine minutes.
- `checks/level2loop5.py` L1–L4, `checks/lambdacount5.py` C1–C5: the rounds of the write-out's loops, about ½/(ε_K ε_ind)
  per loop at the parameter point, counted from the write-out's own index sets; `checks/twodomain5.py` D1–D4: the
  record's lemma on the domain for the two-dust background; `checks/r0census5.py`: every line of Parts III–VII naming the
  inner radius, with its class (323 lines, 121 of them using only that the boundary is spacelike; `BEYOND5-R0.tsv`). Each
  with its control. A few seconds each, `twodomain5.py` under a minute.
- `checks/census9.py` C23, C29, C27: section 8.5's and section 9's censuses. C23, the 78 lines of the supplement's
  section 10 that name the parameter point by its value (γ_C = 10⁶, h = 10⁻⁶, or the tuple (1/2, 1/102400, …)), each
  placed in one of 10.54's classes, the anchor standing in the class's own text (a 16, twelve of them through its
  setting's list; b 15; b by its opening sentence 8; c 16; d 8; e 5; outside the classification 10), none unlisted; lines
  naming the point another way are outside the pattern; C29, `LOSS-D.md`'s six losses each with its closed form, its nine
  weights each with its inequality, its three loop counts; C27, the lowered inner boundary of `BEYOND5.md` spacelike,
  g^rr = f(r_0) ≤ −3 for every final mass, exactly. Controls: a planted unlisted conclusion; a planted seventh loss; r_0
  = 2 r_h. A few seconds.
- `checks/support5c.py` C11–C13: section 5's remaining steps. C11, |w|_7 ≤ C 𝒩 as an exponent ledger: each derivative of
  [∂_θ g1] costs λ⁻¹ (computed), and every one of the 128 classes of Leibniz terms of w = h + φ[∂_θ g1] is covered by
  (5.4)'s weights with λ-exponent ≥ 0; C12, the first-order reduction in the Z-coordinates at random admissible rational
  points, A⁰ symmetric positive definite (Sylvester) and every A^k symmetric, the symmetry and positivity of (A1)–(A4)
  and not the rest; C13, M[S] at g0 + λ(W_TT + χ dv² + m1) to order λ⁰: only θ⁺ carries the wave there, through ∂_θ tr_S
  W, zero for the TT wave. Controls: (5.4) without its ‖∂^j ∂φ‖ term (C11; without its λ‖∂^j ∂_x² φ‖ term nothing is
  uncovered, that term being Step 4's); Vaidya's constant-x lines inside the horizon (C12); a wave with a trace on the
  spheres (C13). Exact; about a minute.
- `checks/ledger5.py` L1–L4: exponent ledgers. L1, supplement Propositions 9.8–9.9 with β0 symbolic (∫_(t≥λ⁻²) λ⁻¹
  t^(−3/2) dt = 2, K′ > 8 + 4β0, K′ − 2β0 − 1 ≥ K + 2, the Gronwall margin); L2, the bootstrap's ledger
  (`checks/support5.py` C5) with k and K symbolic, every row linear and holding for k, K ≥ 6; L3, Proposition 11.1's
  iteration, a gain of r^(−1/2) per step, and g0's outgoing generators reaching v_start (RK4, floating point); L4, the
  stages' source terms (56 at m = 2 to 1268 at m = 6) each carrying the envelope or an earlier profile, so all vanish
  after the shell (that the enumeration is complete is deduced). Controls: the split at λ⁻¹, K′ = K + 3; K = 5; the
  perturbation in E_1; an envelope-free term. About forty seconds.
- `checks/support8b.py` M1–M5: section 8's bookkeeping. M1, the antipodal map is an isometry of the Myers–Perry metric at
  symbolic spins (`checks/mpdata5.py`'s Kerr–Schild form), the 15 Killing initial data split 7 even (∂_t, the rotations)
  and 8 odd (translations, boosts); M2, supplement 10.50 (b)–(d)'s inequalities; M3, a bump of amplitude R⁻³ costs
  R^(ℓ0−3) in the norm's b-density; M4, `proof5/PART-VI4-PARAMS.md`'s 18 rows order without a cycle and Theorem 2.1's
  steps follow; M5, the counts 248 = 90 + 29 + 31 + 38 + 60, 61, 57/4, 45/16, 34 from the inventories. Controls: x1 ↦
  −x1; T ≤ r_q(μ_end) − a; the literal reading, amplitude R⁻¹, whose cost R^(ℓ0−1) must not pass as R^(ℓ0−3); a planted
  cycle; a planted row. Exact; a few seconds.
- `checks/support3.py` D1–D4: section 3's steps. D1, √μ − r_q = μ^(1/4)(μ^(1/4) − (√72 l5²)^(1/4)), increasing for μ >
  √72 l5²/16; D2, the phase mean of ∂_θ g1 is 0 and that of its g0-norm squared (4/3) A² env² r⁻³ (χ drops out, g0^vv =
  0), with ∫ψ[∂_θ g1] → 0 by quadrature (floating point); D3, the six so(4) generators Killing and both reflections
  isometries of g0 for every μ(v), g0 + λW invariant under the T² action and the reflections, with `past5.py` P6 and
  `mass5.py` M4; D4, the data's Sobolev index as a derivative ledger, s > 3/2 + 4. Controls: exponent 1/2 (D1); env = 0
  (D2); grad x1 (D3); s0 = 9/2 (D4). About two minutes.
- `checks/support5b.py` C10, C10b: supplement Lemma 3.2's (3.3) at w = 0 in all fifteen components of P(φ [∂_θ g1]), φ(v,
  r, θ) generic (T²-invariant, as in the class), on `lead5.py`'s stage-0 profile: no order below λ⁻¹, the λ⁻¹ part −(ℓ ·
  ∂φ)[∂_θ² g1] + φ T(∂_θ g1), and φ's second derivatives at λ⁰ only in −½ (□̃φ)[∂_θ g1] (C10); the same with an
  oscillating dr dr component added, W(ℓ, ℓ) ≠ 0, whose extra λ⁻¹ term is proportional to φ (C10b). Controls: −2 (ℓ · ∂φ)
  and −(□̃φ) in place of the true coefficients. Exact; about eight minutes.
- `checks/re813.py` R1–R3: (8.13) as h = 1/γ_C varies (supplement 10.54(d)). R1: at l = 1000 the resultant in h of a
  non-real root of real part 2 has one root in (0, 10⁻⁶], h = 6.652623172 × 10⁻⁷, where two indicial roots are 2 ± 3.6833
  i, |λ| = 4.19: (8.13) fails there. R2: for |n| ≤ 50 and each of box^C's sextic, vector quadratic and l = 0 quartic,
  that resultant is a nonzero polynomial in h at every l (the gcd of its coefficients has no root κ = l(l + 2)). R3: the
  top coefficient in κ is free of λ, so at each h finitely many roots have |λ| ≤ 50. Controls: R1 at h = 10⁻⁶; (λ − 2)² +
  1 + κh for R2; a λ-dependent top coefficient for R3. Exact (R1's root located at 60 digits); about a minute.
- `checks/coulomb5.py` K1–K6: the Coulomb part of the means carried from the initial null hypersurface to spatial
  infinity, a Gegenbauer polynomial in (v − v1)/r on flat space (l ≤ 10), bounded uniformly in l, and on Tangherlini
  a recursion whose factor 1 + 2j never vanishes, so no logarithm (K6 exact rationals). Control: the cross term's sign
  flipped. About five minutes.
- `checks/coulombL5.py` Q1–Q6: the same under the full flat operator of the write-out: self-similar reduction to an
  ODE system in s = v/r whose only singular points are s = 0 and 2, so spatial infinity, s = 1, is ordinary and no
  logarithm enters; the undamped polynomials as a control; the l = 1 scalar sector; Tangherlini to first order in μ
  (Q6). Exact, Q4 floating point.
- `checks/harmonics5.py` S1–S3, T, G: that reduction for every harmonic, l a parameter, of scalar, vector and tensor
  type (the tensor type free of the damping), and the transfers at γ_C = 10⁶ and 10⁵ computed as series at 30 digits.
- `checks/uniform5.py` U1–U6: the transfer bounded uniformly in l ≥ 2 by an energy with an exact Lyapunov metric and
  explicit constants (U6 a floating-point consistency check). Control: the anti-damped A(0), with no positive
  metric. (Not `uniform5.py` above.)
- `checks/sources5.py` Q1–Q6: the quadratic sources of static r⁻² means homogeneous of degree −6, the cross terms with
  a remainder, and the sources from g_λ − g_app (computed at 50 digits). Control: the linear part and a non-static h.
  `checks/stripfull5.py` P1–P5: the strip of bounded v along the initial null hypersurface entering one order later
  under the full operator, at every scalar- and vector-type harmonic l ≤ 12 and the tensor type.
- `checks/stage0two5.py` T1–T6: stage 0 of the two-phase ansatz on a general round double-null background, exact in
  sympy: no λ⁻¹ term, each family's own null stress in the mean, the transports, and the cross harmonics present and
  solved by division, their symbol −e^(−2σ) n1 n2 nonzero. Six mutants caught. About 8 seconds.
- `checks/chardust5.py` D1–D5: the two null dusts' stress in the characteristic constraints leaves their hierarchy
  closed. Control: without nullity the trace is nonzero. Exact, n = 4 and 5; seconds.
- `checks/twodust5.py` B1–B5: the two-dust round background, its evolution and constraints (B1), their propagation
  (B2), the mass flux (B3), Minkowski (B4), exact; and (B5) a characteristic problem on a rectangle, its constraint
  residuals falling at second order, floating point. Control: B depending on v. About 7 seconds.
- `checks/eq5.py` E1–E6: the algebra of the boundary at equality: the boundary's normal, the margin at μ0 = √72 l5²,
  the bound on the layer, the expansion's gap (E6), the future cone sampled (E4, about 42,600 causal vectors) and the
  margins of the domain (E5). Each with a control that must fail.
- `checks/ix5.py` X1–X7: the pointwise identities of the gauge statement: the flat principal parts (X1, X2), the
  first variations of the second fundamental form and of the gauge 1-form (X3, X4), the vector field realising data
  (X5) and inducing none (X7), and DRic(L_X g) = 0 on Tangherlini (X6). Each with a control. About 14 minutes.
- `proof5/checks/gammac5.py` G1–G5 and `proof5/checks/admiss5.py` A1–A2: enumerations over the write-out's parts,
  failing on any unlisted line: every use of the constraint damping parameter γ_C, applied only at its one fixed value;
  and every use of the lower triangular condition (3), used by none of the parts that might.

## Appendix B. The author's words

The commission and the rules that bind it, verbatim, with the item numbers of the author's record; where they enter,
they are the author's postulates, not evidence. Line breaks and runs of spaces are normalized; one word naming the
research tree, and in 509 the part of the message about another matter, are elided and marked "[…]". In them "N1*" is
the working name of the uniform existence statement (the supplement's Theorem E), and "SOURCE" that of a separate part
of the author's programme, not treated in this paper.

- 249 (2026-10-11): "Continue all work here in order, so you and I may keep an open dialogue as the work is done...
  And please run one agent in tandem with our work to verify each claim, but only after you and I have finalized the
  claim and have determined it's ready for verification and you and I can move on"
- 440 (2026-10-16): "Correction - A station is green at an end only when every row it rests on there is proved, or
  derived from first principles and established mathematics. - this is the criteria for each pass... And anything
  derived must be proved separately with computation."
- 441 (2026-10-16): "Questions for me: 1 - no 2 - no. Each definition must be proved 3 - yes 4 - approach approved"
- 442 (2026-10-16): "1 - yes 2 - yes 3 - yes 4 - yes I assert that anything derived from first principles can be
  proven using computation. Prove all readings in the […] theorem using previous arts and works in the field, and
  after that, then use computation to prove the rest."
- 475 (2026-10-17): "yes, but please do not be wasteful with my data. Work efficiently, and concisely."
- 481 (2026-10-17): "But that means the last several rounds of work are moot because even though it was an inner
  horizon was proven not possible in our work, you continued to model further work under the assumption that it was
  still possible. You failed, and wasted my time and data even though I told you not to"
- 484 (2026-10-17): "Remember, there are no chaucy horizons. If you are calculating anything involving a chaucy
  horizon, you have already failed"
- 509 (2026-10-18): "[…] No proof for every λ - we will build this proof from the calculations when the SOURCE work is
  finished"
- 511 (2026-10-18): "I think you can now build nonlinear PDE theorem for this, and fairly quickly now that you have
  done the computations ... Utilize outside research and publications, and utilize all the proof building tools
  available to you."
- 519 (2026-10-19): "Please confirm that you ARE NOT chasing a chaucy horizon again"
- 520 (2026-10-19): "Can you finish the counterpart proof?"
- 521 (2026-10-19): "Does SOURCE rely on or need N1* ?"
- 522 (2026-10-19): "Two tasks: Continue SOURCE AND Prepare instructions for another session to finish N1* and the
  counterpart theorem, and then right a formal response paper to the Huneau and Luk's theorem. That session will need
  access to all you work on the proof, so it'll all need to be pushed to the repo and identified there for the other
  session"
- 524 (2026-10-19): "Please bring forward the handoff and instructions for the N1 session"

To the session that wrote the proof and this paper (dates as recorded in its log):

- 2026-10-19: "I have every confidence that you are up to the task assigned to you. Great assessment was taken before
  hand to make sure you have every tool available to you for this paper"
- 2026-10-19: "Continue" (twice)
- 2026-10-19: "Two outside papers that may be useful to you, the noether theorem, and the navier-stokes equations that
  anthropic released a couple of months ago"
- 2026-10-20: "You can use my indexing model as a Internet navigation and retrieval protocol.... You can also access
  thoughts works by looking for what those papers cite, and also who else has cited the work we are trying to access"
- 2026-10-20: "Excellent work. Yes please, continue with the paper"

Where they enter: 440–442 set the standard of proof and the order (prior art read first, then computation); 481, 484
and 519 fix the scope (the domain ends at the spacelike x_K = 1, nothing involves an inner or Cauchy horizon); 509, 520
and 522 commission the proof for every λ ≤ λ0 and this paper; 249 and 475 fix the method (one verifier at a time,
concisely); the retrieval message of 2026-10-20 is the protocol by which the standard theorems were READ.

## Appendix C. Source map

Paths are relative to the root of the research tree; "supplement" is `docket68/n1star/N1STAR-PROOF.md`, the proof in
full, and its log `docket68/n1star/N1STAR-LOG.md` records each decision.

| claim | where it is established |
| --- | --- |
| Proposition 2.1 | R1; `docket68/lemmas/kn_gauge.py` K1–K2 |
| Proposition 2.2 | R2–R4; `docket68/n1star/ks5.py` K1–K5; supplement 0.1, Lemma 1.1 |
| (2.4) | `docket68/n1star/ks5.py` K3; [Tou23a] Lemma 3.1 for comparison |
| domain Ω | supplement (1.1), Lemma 1.1; `docket68/n1star/foliation5.py` B1–B4 |
| (2.5′) | `paper/response5.py` R12; `docket68/n1star/ansatz5.py` A3–A4; `docket68/n1star/data5.py` |
| section 3: λ-free profiles; Proposition 3.2's margin | `paper/response5.py` R13 |
| section 3: the vacuum step | `paper/response5.py` R14; [LR05] p. 1; [CBCL06] section 3 |
| (5.1), Lemma 5.1, supplement Lemma 3.3 | `docket68/n1star/checks/support5.py` C1–C3; `docket68/n1star/lead5.py` |
| section 5.2: supplement Lemma 3.2's (3.3) in every component | `docket68/n1star/checks/support5b.py` C10, C10b |
| sections 5.2, 5.4, 6: mollifier, time lines, boundary for g_λ | `docket68/n1star/checks/support5.py` C4, C6, C8 |
| sections 3, 4: the stages' structure at λ¹, m1's source and parity | `docket68/n1star/checks/stage5.py` S1–S3 |
| sections 3, 5.5: (6.2), the gauge field's first order and decay | `docket68/n1star/checks/gauge5.py` G1–G3 |
| sections 3, 5.3, 5.4: the remainder, the first-order system, M[S] | `docket68/n1star/checks/support5c.py` C11–C13 |
| sections 3, 8.1, 8.7: the exponent ledgers, the stages after the shell | `docket68/n1star/checks/ledger5.py` L1–L4 |
| section 3: √μ − r_q, the weak limit, the symmetries, the Sobolev index | `docket68/n1star/checks/support3.py` D1–D4 |
| Proposition 2.3, (2.6) | `docket68/n1star/lead5.py` L2; R6; `docket68/lemmas/hf_theorem5.py` F3 |
| (2.7) | [CBCM10] (2.7)–(2.9); supplement 0.2 |
| (4.1) | supplement 3.1–3.2; `docket68/n1star/mass5.py` M3 (the reflection) |
| Theorem 1 items 1–5 | supplement 0.4–0.7 (Theorems E, A, D), sections 1–6 |
| Proposition 3.2 | R6; `docket68/lemmas/hf_theorem5.py` F2 (Z3); deduction in section 3 |
| Theorem A | supplement section 5; `docket68/n1star/lead5.py`, `ansatz5.py` |
| Lemma 5.1, (5.1)–(5.3) | supplement 3.2–3.3, Lemmas 3.1–3.4 |
| (5.4)–(5.5) | supplement section 4, Steps 1–7 |
| section 5.4 | supplement section 4, Step 8; [DS23], [AO14], [LY22], [SY21], [BH17] |
| (5.6) | R5; `docket68/n1star/data5.py` S2–S4, S6; [Rac16]; [CD03] |
| section 5.5 iteration | supplement Lemma 6.4, Proposition 6.5; [AO14], [AG22], [GO13] |
| section 5.5: the constraint solve's scaling | `docket68/n1star/checks/csolve5.py` C7a–C7c |
| part (iii), Proposition 3.3 | supplement Proposition 8.1; `docket68/n1star/horizon5.py` H1–H3; Theorem E Step 1 |
| mean mass, Proposition 3.4 | supplement Lemma 8.2, Proposition 8.2; `docket68/n1star/mass5.py` M1–M4 |
| Theorem 2 | supplement section 9 (Lemmas 9.1–9.7, 9.4b, Theorem A_P, Propositions 9.8–9.9); `past5.py` P1–P8 |
| the flux at past null infinity | supplement section 9.5; `docket68/n1star/past5.py` P7 |
| Theorem 3, (3.2)–(3.3) | supplement section 11 (Propositions 11.1–11.3); `docket68/n1star/bondi5.py` B1–B3; |
| | [TTS09] (28); [HL21] section 3 for the chart's construction |
| the numerics' mean mass, section 6 | `docket68/n1star/bondi5.py` B4 over the solver's runs |
| | (`docket68/lemmas/data/hf_core5_runs.json`); `paper/response5.py` R8 |
| the wavelength 10 l5, section 9 | supplement section 10.2; `docket68/n1star/growth5.py` G0–G5 over its pinned runs; |
| | `paper/response5.py` R7 |
| settling, section 8 | supplement sections 10.1, 10.3–10.63 (Propositions 10.1–10.47); |
| | `docket68/n1star/settle5.py` |
| | T1–T6; `docket68/n1star/wavegauge5.py` W1–W8; `docket68/n1star/hung4.py` C1–C3; `docket68/n1star/rungs5.py` |
| | M1–M5; `docket68/n1star/growing5.py` G1–G5; `docket68/n1star/lzero5.py` Z1–Z5; |
| | `docket68/n1star/hierarchy5.py` H1–H4; `docket68/n1star/coupled5.py` K1–K6; |
| | `docket68/n1star/lzerorate5.py` Y1–Y5; `docket68/n1star/damping5.py` U1–U6; |
| | `docket68/n1star/semiclass5.py` W1–W6; `docket68/n1star/cform5.py` C1–C7; |
| | `docket68/n1star/gaugepot5.py` G1–G7; `docket68/n1star/modes5.py` M1–M5; |
| | `docket68/n1star/trap5.py` T0–T4; `docket68/n1star/thresh5.py` U1–U4; |
| | `docket68/n1star/hienergy5.py` V1–V4; `docket68/n1star/lowenergy5.py` L1–L3; |
| | `docket68/n1star/cpmodes5.py` K1–K3; `docket68/n1star/solv5.py` Q1–Q4; |
| | `docket68/n1star/tface5.py` F1–F5; `docket68/n1star/lin5.py` E1–E5; `docket68/n1star/sbar5.py` S1–S3; |
| | `docket68/n1star/strap5.py` P1–P3; `docket68/n1star/gmodes5.py` G1–G5; `docket68/n1star/zstates5.py` Z1–Z6; |
| | `docket68/n1star/genstates5.py` H1–H5; `docket68/n1star/puregauge5.py` J1–J6; |
| | `docket68/n1star/dual5.py` A1–A3; `docket68/n1star/pairing5.py` P1–P5; |
| | `docket68/n1star/static5.py` S1–S6; `docket68/n1star/physical5.py` Y1–Y4; |
| | `docket68/n1star/window5.py` W1–W3; `docket68/n1star/mp5.py` M1–M5; `docket68/n1star/iota5.py` I1–I5; |
| | `docket68/n1star/scri5.py` C1–C3; `docket68/n1star/aug5.py` A1–A3; `docket68/n1star/lowfreq5.py` W1–W3; |
| | `docket68/n1star/cone5.py` C1–C3; `docket68/n1star/class5.py` C1–C3; `docket68/n1star/iplus5.py` P1–P3; |
| | `docket68/n1star/sharp5.py` K1–K4; `docket68/n1star/eind5.py` E1–E2; `docket68/n1star/uniform5.py` H1–H2; |
| | `docket68/n1star/transfer5.py` T1–T2; `docket68/n1star/general5.py` G1–G2; [HKW18], [KI03], |
| | [KI03b], [CLY03b], [CYDL03], [Hun19], |
| | [Sch13], [Hin23a], [Hin23b], [Hin24b], [Hin26a], [Hin26], [Hin26c], [AHW24], [CD03], [HHV21], [DLMF] |
| Theorem 4 and its proof, section 8.8 | supplement `proof5/` (`proof5/README.md`, Part VII), |
| | `proof5/BASEPOINT-LEDGER.md`, `proof5/checks/`; the earlier route, supplement sections 10.43–10.74 |
| section 8.2's linear statement; the gauge statement | `docket68/n1star/proof5/PART-VIII-LINEAR.md` Theorem 2.2, |
| | Corollary 2.3; `docket68/n1star/proof5/PART-IX-GAUGE.md` Theorem 2.2, Corollary 2.3; `checks/ix5.py` |
| the general class, section 8.6 | supplement sections 10.60–10.63; `docket68/n1star/general5.py` G1–G2; |
| | [HHV21], [CD03] |
| [Hin23a]'s section 3 at n = 4, section 8.8 | supplement section 10.64; `docket68/n1star/exterior5.py` X1–X8; [Hin23a] |
| [Hin26a]'s section 5.2 at n = 4, section 8.8 | supplement section 10.65; [Hin26a], [Hin23d] |
| [CD03]'s gluing and the boost at n = 4, sections 8.7–8.8 | supplement section 10.66; |
| | `docket68/n1star/gluing5.py` D1–D4; [CD03], [Hin26] |
| [Hin26c]'s sections 7–8 and 9.3 and [HHV21] at n = 4, section 8.8 | supplement sections 10.67–10.68; |
| | `docket68/n1star/edge5.py` E1–E4; [Hin26c], [HHV21] |
| a second census by token sweep, section 8.8 | supplement section 10.69; `docket68/n1star/censusweep.py` |
| the deductions inventoried, section 8.8 | supplement section 10.70; `docket68/n1star/DEDUCTIONS.tsv` |
| the perturbation steps at proof level, section 8.8 | supplement section 10.71 |
| the general-n steps' hypotheses placed, section 8.8 | supplement section 10.72; [Hin26], [Hin26c] |
| the undecided steps placed, section 8.8 | supplement section 10.73; `docket68/n1star/synth5.py` S1–S3; [KI03] |
| the modification steps' changes placed, section 8.8 | supplement section 10.74; `docket68/n1star/B-MAP.tsv` |
| the readings traced to their roots, section 8.8 | supplement section 10.77; `docket68/n1star/READINGS.tsv` |
| the horizon threshold, section 8.8 | supplement section 10.79; `docket68/n1star/hthresh5.py` T1–T8 |
| Hintz's sections 9.5–9.6 at n = 4, section 8.8 | supplement section 10.80; `docket68/n1star/tfnorm5.py` |
| Hintz's section 9 at n = 4, section 8.8 | supplement section 10.82; `docket68/n1star/iotasol5.py` |
| Hintz's section 9's census by a second method, section 8.8 | supplement section 10.85; |
| | `docket68/n1star/bundlesweep.py` |
| Hintz's section 9 re-run on bundles, section 8.8 | supplement section 10.86; `docket68/n1star/bundle5.py` |
| the zero energy pole at n = 4, section 8.8 | supplement section 10.83; [Hin26] |
| Hintz's section 9 on bundles and uniformly in the operator, section 8.8 | supplement section 10.84; [Hin26c], |
| | [Hin26] |
| sixty-one modification steps written out, section 8.8 | supplement section 10.75; [Hin26], [Hin26a], [Hin26c], |
| | [Hin21], [Hin23a], [Hin23e], [Hin24b], [CD03]; `docket68/n1star/iplusnorm5.py` N1–N9 |
| the continuation and uniqueness inside the horizon, sections 8.4, 8.5 | supplement section 10.76 |
| (4.1) for a generic profile | `docket68/n1star/checks/support9.py` S6 |
| section 8.2: Proposition 10.1's coefficients | `docket68/n1star/checks/kirecon5.py` P1–P2 |
| section 8.5: the scan below l = 10⁴ certified | `docket68/n1star/checks/eindcert5.py` I1 |
| section 8.5: the conclusions' dependence on h | `docket68/n1star/checks/hclass5.py` H1–H2 |
| sections 8.1–8.8: the half-turn, 10.50's bounds, the bump's cost | `docket68/n1star/checks/support8b.py` M1–M3 |
| sections 8.4, 8.8: the parameter order, the inventories' counts | `docket68/n1star/checks/support8b.py` M4–M5 |
| section 8.5: (8.13) off a countable set of h, not at every h | `docket68/n1star/checks/re813.py` R1–R3 |
| sections 8.4–8.5: the exponent 2, the class, r_h, roots past 5/2 | `docket68/n1star/checks/support8c.py` K1–K4 |
| sections 8.5, 9: the point's conclusions, the losses, the lowered boundary | `docket68/n1star/checks/census9.py` |
| section 8.7: the glued mass bound | `docket68/n1star/checks/flux5.py` F1–F3 |
| section 8.7: Myers–Perry data in the class | `docket68/n1star/checks/mpdata5.py` B1–B4 |
| section 8.8: the sites of the averaged choices enumerated | `docket68/n1star/checks/vii5census.py` V1 |
| section 8.8: every listed use of the averaged choices read | `docket68/n1star/checks/vii5read.py` Q1–Q2 |
| section 9, settling: the loss d | `docket68/n1star/LOSS-D.md` LD3, LD10–LD16, section 2b; `checks/thetain5.py`; |
| | `checks/prop31loss5.py`; R10 |
| section 9, settling: the resolvent band | `docket68/n1star/E2-PILOT.md` section 3j; `checks/e2trapband5_384.out`; |
| | `checks/e2h1band5.out`; R11 |
| section 9, settling: the constants without a number | `docket68/n1star/checks/support9.py` S3 |
| section 9, settling: the charge for larger ℓ_I | `docket68/n1star/checks/charge5.py` G1–G2 |
| section 9, settling: the certified lower bound | `docket68/n1star/checks/e2lower5.py` E1 |
| section 9, the double-null prototype | `docket68/n1star/CERTIFY-10L5.md` section 6b; `dnsolve5.py`, |
| | `checks/g1curv5.py` |
| section 9, deeper excisions on a second grid | `docket68/n1star/checks/excise5.py` E1–E2 |
| section 9, beyond the boundary | `docket68/n1star/BEYOND5.md` Propositions 6.1–6.2, Lemma 6.3, section 3(b); |
| | `BEYOND5-R0-PROOF.md`; `checks/closure5.py` |
| the boundary at equality | `docket68/n1star/EQUALITY5.md`; `checks/eq5.py` E1–E6 |
| the boundary at equality: the layer | `docket68/n1star/checks/eqlayer5.py` L1–L2 |
| section 9, more families | `docket68/n1star/FAMILIES5.md` sections 1, 4b–4i; `checks/data5two.py` |
| section 9, the two-dust background reaching Σ_τ0 | `docket68/n1star/checks/twodomainx5.py` X1–X2 |
| provenance | the supplement's log `docket68/n1star/N1STAR-LOG.md` records the independent readings (not a source |
| | for any claim) |
| the standard theorems READ | supplement section 7, the retrieval table |
| [HL18] Theorem 4.2, (1.4), (4.1) as quoted | READ, [HL18] pp. 2–3, 10 |

## Appendix D. Reproduction

Python 3 with sympy (Python 3.13.16, sympy 1.14.0, mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1, z3 5.3.1 in the runs recorded
here); z3-solver for `foliation5.py`; numpy for `bondi5.py` and `growth5.py`, numpy and scipy for `settle5.py`; mpmath
for `damping5.py` and every program that imports it, and for `lowenergy5.py`. `growth5.py` imports the solver
`docket68/lemmas/hf_mirror5.py` and `hf_core5.y_core`, `past5.py` imports `lead5.py`, `growing5.py`, `lzero5.py` and
`coupled5.py` import `wavegauge5.py`, `lzerorate5.py` imports `hierarchy5.py`, `semiclass5.py` imports `damping5.py`,
`cform5.py` imports `semiclass5.py` and `damping5.py`, `gaugepot5.py` imports `damping5.py`, `modes5.py` imports
`gaugepot5.py` and `damping5.py`, `trap5.py` and `thresh5.py` import `gaugepot5.py`, `damping5.py` and `modes5.py`,
`hienergy5.py` imports `gaugepot5.py`, `damping5.py`, `thresh5.py` and `trap5.py`, `lowenergy5.py` imports `thresh5.py`
and `damping5.py`, `cpmodes5.py` imports `damping5.py`, `solv5.py` imports `cform5.py` and `damping5.py`, `tface5.py`
imports `cform5.py`, `gaugepot5.py`, `semiclass5.py` and `damping5.py`, `lin5.py` imports `damping5.py` and
`gaugepot5.py`, `sbar5.py`, `strap5.py`, `gmodes5.py` and `zstates5.py` import `damping5.py`, `genstates5.py` imports
`damping5.py` and `zstates5.py`, `puregauge5.py` imports `damping5.py`, `genstates5.py` and `zstates5.py`, `dual5.py`
imports `damping5.py`, `genstates5.py` and `puregauge5.py`, `pairing5.py` imports `damping5.py`, `static5.py` imports
`damping5.py` and `gmodes5.py`, `physical5.py` imports `damping5.py` and `lin5.py`, `window5.py` imports `damping5.py`
and `lin5.py`, `mp5.py` imports `damping5.py` and `dual5.py`, `iota5.py` imports `damping5.py` and `lin5.py`, `scri5.py`
imports `damping5.py`, `iota5.py`, `lin5.py` and `sbar5.py`, `aug5.py` imports `damping5.py` and `sbar5.py`,
`lowfreq5.py` imports `aug5.py`, `damping5.py` and `sbar5.py`, `cone5.py`, `class5.py`, `eind5.py`, `uniform5.py` and
`transfer5.py` import `damping5.py`, `iplus5.py` imports `damping5.py`, `lin5.py`, `sbar5.py` and `scri5.py`, `sharp5.py`
imports `class5.py`, `damping5.py`, `iplus5.py` and `window5.py`, `general5.py` imports `damping5.py`, `sharp5.py`,
`window5.py` and `iplus5.py`, `checks/csolve5.py` imports `data5.py`, `checks/eindcert5.py` imports `eind5.py` and
`damping5.py`, `checks/hclass5.py` imports `damping5.py`, `checks/re813.py` imports `damping5.py`, `checks/support5b.py`
imports `checks/support5.py` and `lead5.py`, `checks/support3.py` imports `lead5.py`, `past5.py` and `mass5.py`,
`checks/support8b.py` imports `checks/mpdata5.py`, `checks/ledger5.py` imports `checks/support5.py`,
`checks/support5c.py` imports `horizon5.py` and `lead5.py`, `checks/lambdacount5.py` imports `checks/level2loop5.py`,
`checks/support8c.py` imports `damping5.py`, `hthresh5.py`, `iplus5.py`, `lhor5.py`, `sbar5.py` and `scri5.py`,
`checks/gauge5.py` imports `data5.py`, `lead5.py` and `paper/response5.py`, `checks/excise5.py` imports `growth5.py`,
`checks/stage5.py` imports `lead5.py`, `checks/support9.py` imports `lead5.py`, `checks/charge5.py` imports
`checks/prop31loss5.py` and `checks/dg5.py`, `checks/twodomainx5.py` imports `checks/twodomain5.py`, `checks/vii5read.py`
imports `checks/vii5census.py`; the others import nothing from the research tree:

    cd paper && python3 response5.py --selftest          # R1-R14, about a minute
    python3 response5.py --selftest --full               # and the five proof programs, about 20 minutes
        cd ../docket68/n1star && python3 ks5.py --selftest   # and foliation5, ansatz5, lead5, data5, horizon5, mass5,
                                                         # past5 (about 4 minutes), settle5, bondi5 (about ten minutes)
                                                         # wavegauge5 (about 7.5 minutes), hung4 (about 2.5 minutes),
                                                         # rungs5 (about half a minute)
                                                         # growing5 (about twelve minutes)
                                                         # lzero5 (a quarter of a minute)
                                                         # hierarchy5 (about a minute)
                                                         # coupled5 (about a minute)
                                                         # lzerorate5 (about forty seconds)
                                                         # damping5 (about eighty seconds)
                                                         # semiclass5 (about a minute)
                                                         # cform5 (about a minute and a half)
                                                         # gaugepot5 (about a minute and a half)
                                                         # modes5 (under a minute)
                                                         # trap5 (about 12 seconds)
                                                         # thresh5 (about 8 seconds)
                                                         # hienergy5 (about 25 seconds)
                                                         # lowenergy5 (about 7 seconds)
                                                         # cpmodes5 (about 5 seconds)
                                                         # solv5 (about 15 seconds)
                                                         # tface5 (about 25 seconds)
                                                         # lin5 (about 50 minutes)
                                                         # sbar5 (about a minute)
                                                         # strap5 (a few seconds)
                                                         # gmodes5 (about five minutes)
                                                         # zstates5 (about half a minute)
                                                         # genstates5 (about a minute)
                                                         # puregauge5 (about four minutes)
                                                         # dual5 (about a minute and a half)
                                                         # pairing5 (about three and a half minutes)
                                                         # static5 (about a minute and a quarter)
                                                         # physical5 (about twelve minutes)
                                                         # window5 (about twenty-five minutes)
                                                         # mp5 (about three minutes)
                                                         # iota5 (about twenty-five minutes)
                                                         # scri5 (about twelve minutes)
                                                         # aug5 (about 8-12 minutes)
                                                         # lowfreq5 (about five seconds)
                                                         # cone5 (about ten seconds)
                                                         # class5 (about forty seconds)
                                                         # iplus5 (a few seconds)
                                                         # sharp5 (about nine minutes)
                                                         # eind5 (about four minutes)
                                                         # uniform5 (about twenty seconds)
                                                         # transfer5 (about four minutes)
                                                         # general5 (a few seconds)
                                                         # exterior5 (about forty-five seconds)
                                                         # gluing5 (about fifteen seconds)
                                                         # edge5 (a few seconds)
                                                         # synth5 (about forty seconds)
                                                         # and behind section 9: checks/thetain5, closure5,
                                                         # e2h1band5, prop31loss5 (seconds to half a minute),
                                                         # checks/data5two (hours), checks/e2trapband5.py
                                                         # 768 0.05 384 (about 194 minutes)
                                                         # and iplusnorm5, hthresh5, tfnorm5, iotasol5, bundle5
                                                         # (seconds to half a minute)
    python3 bundlesweep.py --texts DIR --selftest        # DIR the fetched full texts; not stored here
    python3 censusweep.py --texts DIR --cd03 FILE --out hits.tsv   # likewise
    python3 growth5.py --selftest                        # G1-G5 against data/growth5_runs.json; --run, --merge redo it
    python3 proof5/checks/gammac5.py                     # and proof5/checks/admiss5.py (seconds)
    python3 checks/support5.py                           # about a minute; and checks/support8.py
    python3 checks/eq5.py                                # and checks/ix5.py (about 14 minutes)
    python3 checks/epsind5.py --selftest
    python3 checks/csolve5.py                            # about two hours
    python3 checks/eindcert5.py                          # about ten minutes
    python3 checks/kirecon5.py                           # about half a minute
    python3 checks/mpdata5.py                            # about four minutes
    python3 checks/flux5.py                              # a few minutes
    python3 checks/vii5census.py                         # a second
    python3 checks/vii5read.py                           # a second
    python3 checks/hclass5.py                            # a few minutes
    python3 checks/support9.py                           # about five minutes
    python3 checks/charge5.py                            # under a minute
    python3 checks/eqlayer5.py                           # a few seconds
    python3 checks/e2lower5.py                           # about ten minutes
    python3 checks/twodomainx5.py                        # under a minute
    python3 checks/stage5.py                              # about forty-five minutes
    python3 checks/excise5.py                             # seconds, on the runs merged into data/
    python3 checks/gauge5.py                              # about five minutes
    python3 checks/support8c.py                           # about nine minutes
    python3 checks/level2loop5.py; python3 checks/lambdacount5.py; python3 checks/twodomain5.py
    python3 checks/census9.py                             # a few seconds
    python3 checks/support5c.py                           # about a minute
    python3 checks/ledger5.py                             # about forty seconds
    python3 checks/support8b.py                           # a few seconds
    python3 checks/support3.py                            # about two minutes
    python3 checks/support5b.py                           # about eight minutes
    python3 checks/re813.py                              # about a minute
    python3 dnsolve5.py --run lam rcut M Nu Nv out.npz   # the double-null runs; then checks/g1curv5.py --seed2-2400 DIR
    python3 data5.py --mutants                           # about 80 minutes

Of the programs cited, every one in `docket68/n1star/` and `docket68/lemmas/` takes `--mutants` except `censusweep.py`,
`dnsolve5.py`, `growth5.py` and `hf_core5.py`; under `checks/` only `checks/stage0two5.py` does; `paper/response5.py`
and `proof5/checks/` take none, their negative controls running inside the self-test or the plain run.

The md5 of each file this paper rests on, at this commit (R9 checks every row; `python3 response5.py
--update-md5` rewrites the column):

| file | md5 |
| --- | --- |
| `paper/response5.py` | `e61b6d48c2a9159c7d2ef3cf6c7c3c1c` |
| `docket68/n1star/N1STAR-PROOF.md` | `69928b6a63e02cf22ef142c2318b0a60` |
| `docket68/n1star/README.md` | `d18e78829222d34b1b3dba6e3089f129` |
| `docket68/n1star/ks5.py` | `4fb7563006d79b3144b42b761300830a` |
| `docket68/n1star/foliation5.py` | `dab023e393662863f1f608b5d087dc9c` |
| `docket68/n1star/ansatz5.py` | `e0f4a8fbf191effb4115aff1e4a655ac` |
| `docket68/n1star/lead5.py` | `ba26d7df17f37eb6932d5b7133656d1a` |
| `docket68/n1star/mass5.py` | `ebe2ee78219553f4b57a4200604752e5` |
| `docket68/n1star/horizon5.py` | `962ca2fb9404bebbce8420075f080dbd` |
| `docket68/n1star/past5.py` | `d6742977ac642377ecc3785759dd526c` |
| `docket68/n1star/settle5.py` | `8f2c81317211e47666881113aa18e3a0` |
| `docket68/n1star/bondi5.py` | `998cfceff0a2781cd161fe0640408e63` |
| `docket68/n1star/growth5.py` | `7493d63335c521c78d35653716881934` |
| `docket68/n1star/wavegauge5.py` | `d2d8e22bf8d52fe42eea3f32ae49306f` |
| `docket68/n1star/rungs5.py` | `2bc4e9021ae529e63eb548a99049cb08` |
| `docket68/n1star/growing5.py` | `f0af993ae740166648df5e57bb0bd8ee` |
| `docket68/n1star/lzero5.py` | `15b82c25a3f446d596d4f34119eab15f` |
| `docket68/n1star/hierarchy5.py` | `0ccf0a2d871a186c6391eda8e0ab9d95` |
| `docket68/n1star/coupled5.py` | `bdf92b44776f162add54534ae04d68c3` |
| `docket68/n1star/lzerorate5.py` | `5a4d15308940fa5e4acf3bb0e4426f74` |
| `docket68/n1star/damping5.py` | `37cab567c21d749ae1d666b5c5a7914f` |
| `docket68/n1star/semiclass5.py` | `139089729105c047b67c3fd3223c1613` |
| `docket68/n1star/cform5.py` | `380e49f6d5a6712ce883c3f456ae4ebf` |
| `docket68/n1star/gaugepot5.py` | `e547d9d20ff4428d1fa60dcf4a2c5b89` |
| `docket68/n1star/modes5.py` | `0e61753d554d6447aaf466571c3e8283` |
| `docket68/n1star/trap5.py` | `45625a944c610a406f4622fbde411f49` |
| `docket68/n1star/thresh5.py` | `a8fb23d38fd7425b56b5b2cc8b1adbef` |
| `docket68/n1star/hienergy5.py` | `e855d66955c409646409c6e32ae87678` |
| `docket68/n1star/lowenergy5.py` | `b8eae0d5730b39836cbe21cb1ec2c46d` |
| `docket68/n1star/hung4.py` | `7f3d68853fde8bda4ff383dc039dadfe` |
| `docket68/n1star/data5.py` | `9404eb2d500b5b5fc810ee136bea2272` |
| `docket68/lemmas/hf_theorem5.py` | `7d146a8a610dc709d6ab5484756d4cc8` |
| `docket68/lemmas/counterpart5.py` | `e7dcf7bf898c2147492d28c5fb888d18` |
| `docket68/lemmas/kn_gauge.py` | `7e9e9ef8ec12e670f1717ec4fe8bd491` |
| `docket68/lemmas/hf_core5.py` | `84b715eb461838abcb5e018cd455eb5c` |
| `docket68/lemmas/seed_escape.py` | `1a8b2ff82872e7096f13bf891a10424c` |
| `docket68/n1star/cpmodes5.py` | `4579a4605556992e5398c4d2abef2add` |
| `docket68/n1star/solv5.py` | `dfc11365958695d53d4dc98ccdd747bc` |
| `docket68/n1star/tface5.py` | `de9625072d570b423959da1af7654e41` |
| `docket68/n1star/lin5.py` | `b108caf5ebecc29dc61ce56d7f49af37` |
| `docket68/n1star/sbar5.py` | `1da168fe2b9ab33ec28e71609623844e` |
| `docket68/n1star/strap5.py` | `8d716c0c7dd36f8cd23987f1c79fec3d` |
| `docket68/n1star/gmodes5.py` | `9dd520feec732b5924306b060bf222c1` |
| `docket68/n1star/zstates5.py` | `ea860787d2a4345a193e6ce2f9a19b7f` |
| `docket68/n1star/genstates5.py` | `f2ef7478e67760e3d6ff05d0a0dd74e5` |
| `docket68/n1star/puregauge5.py` | `6fda612d263dcfa82b79a9ff76a70000` |
| `docket68/n1star/dual5.py` | `c85cd907bd71d3c4fb1a12be89adf783` |
| `docket68/n1star/pairing5.py` | `e831c01861f659eddcaeb7a1d0a047bb` |
| `docket68/n1star/static5.py` | `328a406c8499edf359eca522d34c7895` |
| `docket68/n1star/physical5.py` | `76a5cc7311dbeb9c4b185d543a7a5676` |
| `docket68/n1star/window5.py` | `e1ee57bdf2abb6cb5b99c52732c82066` |
| `docket68/n1star/mp5.py` | `4f3521cc717fb1b0363cb73d045c26f7` |
| `docket68/n1star/iota5.py` | `8731cc8b878418d9750c8cdd313d8ef1` |
| `docket68/n1star/scri5.py` | `6c63e01b0582c528bd84431edbc8eac6` |
| `docket68/n1star/aug5.py` | `3bcbdc239f889819b64436ad7b562ae5` |
| `docket68/n1star/lowfreq5.py` | `b952a94d5a9313a66b1c166c7ed0d1ed` |
| `docket68/n1star/cone5.py` | `ae24d0704a713c2ceb8bc26c8a809a44` |
| `docket68/n1star/class5.py` | `108d83c73f1c7c5ed3358bf4ffd46e7d` |
| `docket68/n1star/iplus5.py` | `f305c6a146fc9f032c1070df101a9f3a` |
| `docket68/n1star/sharp5.py` | `8a71490bfe17eb8de23d9b7560c6168b` |
| `docket68/n1star/eind5.py` | `c7dab684f8cc6ce75bf89a00b6705cec` |
| `docket68/n1star/uniform5.py` | `cb12ee070583b3a33ab82aa5b04cf282` |
| `docket68/n1star/transfer5.py` | `1983b9deebdae3c16bb891f4919340bc` |
| `docket68/n1star/general5.py` | `13496fd0a93ea070731a78ed96123f4d` |
| `docket68/n1star/exterior5.py` | `dd978b8bee559d76cd22b3e449e7579b` |
| `docket68/n1star/gluing5.py` | `f95d805e595c5ff690c46c793177fd36` |
| `docket68/n1star/edge5.py` | `946af1dd2106301526e999c1db064096` |
| `docket68/n1star/censusweep.py` | `ce45d94e55923b6c19577ab5668afba0` |
| `docket68/n1star/iplusnorm5.py` | `1f7fb424e6bb7109eecbc9b75ec0b682` |
| `docket68/n1star/hthresh5.py` | `dc476b28d2bd87f0be6e1bcc88361bb6` |
| `docket68/n1star/tfnorm5.py` | `7a80137c05c54689832006a42c989c22` |
| `docket68/n1star/iotasol5.py` | `6b5e1dcdf9aaff9f60c07570c88cc83f` |
| `docket68/n1star/bundlesweep.py` | `a1b1831bb6023782629e2a2eac4ffc76` |
| `docket68/n1star/bundle5.py` | `60755692ad9a4d2aaf6b94b8ad1e11f1` |
| `docket68/n1star/synth5.py` | `f6a462a7f1f3bff318f6ea0ce75e4134` |
| `docket68/n1star/READINGS.tsv` | `edef9a4c3d82824574cc05c6ab5d3a08` |
| `docket68/n1star/B-MAP.tsv` | `c8030f38e1160b539974f0feb9dc717a` |
| `docket68/n1star/proof5/PART-II-F-IOTA.md` | `51c14571e7c29685fb8a757713dc2015` |
| `docket68/n1star/proof5/README.md` | `82d46566d3bc11e766a7af9896a89d5d` |
| `docket68/n1star/proof5/PART-VII-ASSEMBLY.md` | `5b5d06532383a4b7a804d980179e9261` |
| `docket68/n1star/proof5/BASEPOINT-LEDGER.md` | `44c0036ebaa29156a161956911094f75` |
| `docket68/n1star/proof5/checks/gammac5.py` | `19491acb21cdd07ea9f93a827d970737` |
| `docket68/n1star/proof5/checks/gammac5.tsv` | `0801ba6869e3884ed3ef309acf872ad1` |
| `docket68/n1star/proof5/checks/admiss5.py` | `e3ec393be73a893b76b2c66130c474c8` |
| `docket68/n1star/proof5/checks/admiss5.tsv` | `133a673e184f911e6529c318eac95950` |
| `docket68/n1star/proof5/checks/damping5.tsv` | `4e7c226efd96b04206eb1c8e207e6861` |
| `docket68/n1star/proof5/PART-III-I16-BASEPOINTS.md` | `d7532a0cb202e4fe77a109fa1f6dbf0f` |
| `docket68/n1star/proof5/PART-VI4-PARAMS.md` | `e5ccb190d92288c1b8f489d3ed206495` |
| `docket68/n1star/proof5/PART-VIII-LINEAR.md` | `5fcfded92005ed06251f1216515d082f` |
| `docket68/n1star/proof5/PART-IX-GAUGE.md` | `de9afd2470c80c26ff6b172d35992a51` |
| `docket68/n1star/checks/ix5.py` | `3aef2fc325684b0a489e2b04c9a89c4a` |
| `docket68/n1star/EQUALITY5.md` | `9a36681c3862dd10f528ecc011cdcc73` |
| `docket68/n1star/checks/eq5.py` | `fae5dce11668492f91fec0657408090b` |
| `docket68/n1star/LOSS-D.md` | `363b7acd423b6201dbcc7faa8b42f8eb` |
| `docket68/n1star/proof5/PART-III-K-NONLINEAR.md` | `3a43fc786ec3d98b0f06e179dddc7814` |
| `docket68/n1star/E2-PILOT.md` | `d156cd3b591817ccef7f7df714fd1239` |
| `docket68/n1star/CERTIFY-10L5.md` | `7eb88136e65eca92b84f53549d957cc0` |
| `docket68/n1star/BEYOND5.md` | `967dac4b469933f49f796bb57486bace` |
| `docket68/n1star/BEYOND5-R0-PROOF.md` | `08c7e0c71e22dc803f3332aad5b41433` |
| `docket68/n1star/FAMILIES5.md` | `34c0c29c24010c93ac191c3351b1c564` |
| `docket68/n1star/checks/thetain5.py` | `70071c8799a311f8f572d4bd46737d15` |
| `docket68/n1star/checks/thetain5.out` | `2e29df7215e015e4fb8c8e0c50ea4b56` |
| `docket68/n1star/checks/prop31loss5.py` | `7f8004a1801aca2a1aa3e777e6ee2907` |
| `docket68/n1star/checks/prop31loss5.out` | `962916acee770eb2f1f8e78350d36531` |
| `docket68/n1star/checks/e2trapband5.py` | `4637d18c90b0ee2ebee7df637cce22d7` |
| `docket68/n1star/checks/e2trapband5_384.out` | `de0fac402970aa209517f5902595c1c2` |
| `docket68/n1star/checks/e2h1band5.py` | `4eed2befe76129e5c01d9b7a4fbea138` |
| `docket68/n1star/checks/e2h1band5.out` | `1fd8053f3fdac83cf070974bf7db38be` |
| `docket68/n1star/checks/closure5.py` | `c65098b4a3c6f0a36b37a5de0ccf902b` |
| `docket68/n1star/checks/closure5.out` | `8388cf3bd8a7eee36f599a210effd723` |
| `docket68/n1star/checks/data5two.py` | `2bd3a44619ea4392c5754bf46506a876` |
| `docket68/n1star/checks/support5.py` | `936c4d30255562e3e9ddc0339cbddd65` |
| `docket68/n1star/checks/support5.out` | `893971e444efc2d1e8d610be42c9476b` |
| `docket68/n1star/checks/g1curv5.py` | `d98ed86deaee1c04d6eb92653cf1cf2b` |
| `docket68/n1star/dnsolve5.py` | `f5c59a474498f3e2a215acfbdf46dbbd` |
| `docket68/n1star/checks/epsind5.py` | `8a255f7058dc653627001236cb7075ad` |
| `docket68/n1star/checks/support8.py` | `72d445c7b9dc7ea3d64601a14050c344` |
| `docket68/n1star/checks/support8.out` | `c21dd4e1fd48ef692ae0414346281063` |
| `docket68/n1star/checks/coulomb5.py` | `077be1d127c4b4c5464284a3394b00b4` |
| `docket68/n1star/checks/coulombL5.py` | `94a056283755d6ebcd1290dc4789e4e6` |
| `docket68/n1star/checks/harmonics5.py` | `5f77b6633fe5c7c84564fa74aeed08dd` |
| `docket68/n1star/checks/uniform5.py` | `5a98d50f13f610a2ad9ac5e901285ebc` |
| `docket68/n1star/checks/sources5.py` | `81f7b6045605ea4b289189819ba2866f` |
| `docket68/n1star/checks/stripfull5.py` | `78db05f21f7138279f3172e40d89aaa3` |
| `docket68/n1star/checks/stage0two5.py` | `8ba3a603740a03e33b4f5dece011482e` |
| `docket68/n1star/checks/chardust5.py` | `195f9b6ea6406635b1a6ff0e5dada7f8` |
| `docket68/n1star/checks/twodust5.py` | `c095bd6aa55d8bfc95c48153a805004e` |
| `docket68/n1star/checks/e2meas5.py` | `9142cd462955de2f7d832ea477a98a52` |
| `docket68/n1star/checks/g1curv5_seed2_2400.out` | `d4b3e16ed75dcaa2b17d5b674dd230a5` |
| `docket68/n1star/checks/data5two.out` | `9d628d9645dff8a0ca17f68cf349937b` |
| `docket68/n1star/checks/csolve5.py` | `a1a4c89f9fd66090448b1ed7a42d2da0` |
| `docket68/n1star/checks/csolve5.out` | `01d62ffee616675b0e90773eed0d70a4` |
| `docket68/n1star/checks/eindcert5.py` | `8d77fd0d316a9db49b6f16d5fa578b67` |
| `docket68/n1star/checks/eindcert5.out` | `f09e6bfc454413da6a5b568636c0fea2` |
| `docket68/n1star/checks/kirecon5.py` | `1ee4325b5c8c0594e7f535c60793acf9` |
| `docket68/n1star/checks/kirecon5.out` | `32adeaa42985094794fde34fb95b27fe` |
| `docket68/n1star/checks/mpdata5.py` | `681c8b0f36027724f1146945decd6efe` |
| `docket68/n1star/checks/mpdata5.out` | `2095b2cfc3584b322e8603301cbb815f` |
| `docket68/n1star/checks/flux5.py` | `a07d563b85624f31979317b22c671e84` |
| `docket68/n1star/checks/flux5.out` | `2764f0c5d211c1470b1fa0a03fd49dad` |
| `docket68/n1star/checks/vii5census.py` | `72bd25c139eb7fd1d50047e54081300d` |
| `docket68/n1star/checks/vii5census.out` | `0c0af2356bbe42ee7dc272dadc492969` |
| `docket68/n1star/checks/vii5read.py` | `ac923c34340fa8526238423002d6e395` |
| `docket68/n1star/checks/vii5read.out` | `49414b30b52bc778f5d8f449b505f38e` |
| `docket68/n1star/checks/VII5-READING.tsv` | `592b0fc609b682fe2afb2d3d466e0eb4` |
| `docket68/n1star/checks/hclass5.py` | `8ad8a55f77406eb4a4d0e481fb1fe85c` |
| `docket68/n1star/checks/hclass5.out` | `761509082809bc9a23fb1b876f3b0b0f` |
| `docket68/n1star/checks/support9.py` | `617014162b849cf055ed4ca7d196141a` |
| `docket68/n1star/checks/support9.out` | `552a1eaac629af5e1b5db1d68ac64be7` |
| `docket68/n1star/checks/charge5.py` | `7f78e7f02736f138363e4a8c277867cf` |
| `docket68/n1star/checks/charge5.out` | `858fa75aa8361216f468484c6bfa3817` |
| `docket68/n1star/checks/dg5.py` | `869df568b7e2aeacd00fe2204bcb70f4` |
| `docket68/n1star/checks/eqlayer5.py` | `aceb659f3442f76e65b7abafa73e6617` |
| `docket68/n1star/checks/eqlayer5.out` | `0d245a8e736d6253014280e6ac46c4ce` |
| `docket68/n1star/checks/e2lower5.py` | `d3e494e451d09f0396f78e0675888c4d` |
| `docket68/n1star/checks/e2lower5.out` | `52399ee19568a0c934fa4006f70e7025` |
| `docket68/n1star/checks/twodomainx5.py` | `9c750e4d51193b98f9a9617b414f2ce3` |
| `docket68/n1star/checks/twodomainx5.out` | `da73ca3c4e843bb4cf59f7a40db798d5` |
| `docket68/n1star/checks/stage5.py` | `9ce714c13eb450223ddbdde68db53928` |
| `docket68/n1star/checks/stage5.out` | `f5f85af8c080b0ccfd162ad58c60f211` |
| `docket68/n1star/checks/excise5.py` | `dfa3d996d7acf9d79ea2de1fef1a6f08` |
| `docket68/n1star/checks/excise5.out` | `8cc3d5d8a5fea8a901bf010c6bc0ff26` |
| `docket68/n1star/checks/gauge5.py` | `0b34a91dde8253a839e62aff2904e19f` |
| `docket68/n1star/checks/gauge5.out` | `0efc8e4c9ee0663fbd2d4b539012fadf` |
| `docket68/n1star/checks/support8c.py` | `f79e1f948f8b06bd5595a3e01facdfb2` |
| `docket68/n1star/checks/support8c.out` | `1cad614d5707093dea720c5779647754` |
| `docket68/n1star/checks/level2loop5.py` | `0f30611bc4ab8b842ed10524032f012d` |
| `docket68/n1star/checks/lambdacount5.py` | `9bf52dfa6ebad7e688399b2bfaa79668` |
| `docket68/n1star/checks/lambdacount5.out` | `8fe050e0aef4c0e3c23d9f83b23cc637` |
| `docket68/n1star/checks/twodomain5.py` | `ae5a1243d42d239e268b5d7f199e8788` |
| `docket68/n1star/checks/twodomain5.out` | `c0b6bf5ba5ce15583d0590d79398af0f` |
| `docket68/n1star/checks/r0census5.py` | `929105da47fc44cd9c31a5d47a76866a` |
| `docket68/n1star/BEYOND5-R0.tsv` | `11b1d5a98db3a2f9dab96eef6a813a21` |
| `docket68/n1star/checks/census9.py` | `2df668cb63c0e15be15e346af3187d6d` |
| `docket68/n1star/checks/census9.out` | `9ba93588dbc0dfa50fb6f3a0bf920a3f` |
| `docket68/n1star/checks/support5c.py` | `494d4b4a969248f3d27ccadcda1df4c6` |
| `docket68/n1star/checks/support5c.out` | `8c79ff003b7091b3d434def27a44aab9` |
| `docket68/n1star/checks/ledger5.py` | `457f7834c9a7341f193b6ca05c676cbf` |
| `docket68/n1star/checks/ledger5.out` | `ebeebba20e8ad1af2afbe1f72271a2c1` |
| `docket68/n1star/checks/support8b.py` | `04a01a972f84fd709e6ac0c67c1a9224` |
| `docket68/n1star/checks/support8b.out` | `31f257595fe1ad9b21b656aa35d0755b` |
| `docket68/n1star/checks/support3.py` | `ccb757a7004d3f01394df42509d0ac0b` |
| `docket68/n1star/checks/support3.out` | `942b4bbb050bc43215891c1bd8b8b36d` |
| `docket68/n1star/checks/support5b.py` | `138607d30937efd6098e1305a9621cf2` |
| `docket68/n1star/checks/support5b.out` | `75905d3feccf03e6faa6bd60bdcc6743` |
| `docket68/n1star/checks/re813.py` | `3d6ee947bc9ff7c99ec8ec908866555d` |
| `docket68/n1star/checks/re813.out` | `b46caeed4bdb7c0e9bcf6ccc8cacefd7` |
| `docket68/lemmas/hf_mirror5.py` | `bbe7d6df6092609ee3c420f97b1dd733` |
| `docket68/lemmas/data/hf_core5_runs.json` | `3e360c45bc4436c2e9012b9f88f7e1ed` |
| `docket68/n1star/data/growth5_runs.json` | `c351486fa869bcb1864a637a6fe5cd0b` |
| `docket68/n1star/DEDUCTIONS.tsv` | `0234cb27d38a833ec4ab6768c5754f79` |

The paper's own md5 is recorded in the commit that adds it, not in itself.
