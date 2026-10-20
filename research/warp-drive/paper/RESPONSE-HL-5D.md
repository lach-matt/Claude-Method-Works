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
is a weak limit of vacuum solutions on a fixed time interval, in an elliptic gauge in which smallness is needed even for
local existence. We prove a five-dimensional counterpart on a large background. In the class of five-dimensional vacuum
metrics with a T² isometry and both reflections, the Einstein equations reduce exactly to 2+1 gravity coupled to two
free waves whose target metric, (3/2) dψ² + 2 dω², is flat and positive definite; this is Huneau and Luk's reduced
system with one scalar replaced by two. The background is five-dimensional Vaidya, a black hole of mass μ0 that grows by
an ingoing shell, and the domain runs from before the shell reaches the hole to the surface inside the horizon where the
limit's curvature reaches a fixed scale (spacelike when μ0 > √72 l5²). For every amplitude A > 0 and every smooth
compactly supported envelope, with no smallness of either, we construct a family of T²-symmetric vacuum metrics g_λ on
that domain, of wavelength λ ≤ λ0, with |g_λ − g0| ≤ Cλ, ∂g_λ bounded, and ∂g_λ → ∂g0 weakly but not strongly, where g0
is Vaidya with dμ/dv = (2/9) A² env²: Isaacson's flux, the null dust of one family. The proof uses the wave-map gauge
relative to the limit itself and an approximate solution of arbitrarily high order, so that every nonlinear term is
beaten by a power of λ rather than by the size of the data; what must be uniform in λ is then a linear estimate on the
black-hole background, and its one large coefficient is removed by a phase-shift identity. The Cauchy data are
constructed by solving the constraints outward in r as a parabolic–hyperbolic system from a sphere inside the shell.
Part (iii) of the counterpart follows: on each column the outgoing expansion of the spheres {v, r = const} has one zero,
converging at O(λ). So does a mean-mass rate: after the shell, the mass of every sphere {v, r = const} is the limit's to
O(λ²), by a quarter-turn symmetry of the two polarizations. The same solutions are constructed from the waves' free data
at past null infinity, where before the shell they are the black hole exactly and their radiation field is the
prescribed one at every λ (Theorem 2). At past null infinity they admit Bondi coordinates and an expansion in r^(−1/2),
and the five-dimensional Bondi mass law holds for them (Theorem 3): their Bondi mass is μ(v) + O(λ) while the shell
passes and μ + (2/9) λ² A² ∫ env'² + O(λ³) after it, the second-order rate the numerics measure, with its coefficient.
We list what is not proved: settling at late times beyond the linear level, and the application at physical wavelengths.

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
five-dimensional symmetry class, not an answer to Problem 8.6 as posed, which concerns four dimensions. The same
solutions are also constructed from the waves' free data at past null infinity (Theorem 2, section 3), and at past null
infinity they obey the five-dimensional Bondi mass law with the prescribed radiation field (Theorem 3, section 3).

The two theorems share their architecture. Both reduce the vacuum equations in the symmetry class to 2+1 gravity
coupled to free waves with a flat, positive-definite target (Proposition 2.1 here; [HL18] (1.3)); both build an
approximate solution by geometric optics and correct it on a fixed interval; both conclude with uniform convergence of
the metric and weak, not strong, convergence of its derivatives, the defect being null dust. They differ in what is
large: Huneau and Luk allow any finite number of angularly separated dusts on a small background; we allow one dust on
a large one, and the amplitude of the waves is not small either.

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
is claimed beyond Ω; nothing in the theorem involves an inner or Cauchy horizon.

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
five-dimensional form of Touati's commutator lemma (READ, [Tou23a] Lemma 3.1, p. 21), here an exact identity.

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
angular profile h(ζ) = √(2/(1 + ζ²)) on the orbit space (ζ = cos 2θ, c² = (1 + ζ)/2, s² = (1 − ζ)/2; the programs
call ζ "x") and phase v/λ; at past null infinity their free data are F = λ A env(v) h(ζ) sin(v/λ),
G = λ A env(v) h(ζ) cos(v/λ). In the gauge of
section 2.5 the leading wave W_TT is traceless, transverse to ℓ, of amplitude r^(−3/2), and smooth at both axes
(computed, `docket68/n1star/ansatz5.py` A3).

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
needs one), whose coefficients are rational in g and smooth in X on r > 0 (READ: [CBCM10] (2.7)–(2.9), arXiv HTML,
unpaginated, in n + 1 dimensions, formulae transcribed: "R_(α β) = R^(H)_(α β) + 1/2 (g_(α λ) D̂_β H^λ + g_(β λ)
D̂_α H^λ)", "R^(H)_(α β) = −1/2 g^(λ μ) D̂_λ D̂_μ g_(α β) + f̂[g, D̂ g]_(α β)", f̂ "independent of the second
derivatives of g"). D and Ric^H are built from g and g0 alone, so they are invariant under the isometries of g0, which
include T² and both reflections. Ric^H(g) = 0 is a quasilinear wave system, D(g0) = 0, Ric^H(g0) = Ric(g0), and a
solution with D = 0 is vacuum.

---

## 3. The theorem

**Theorem 1 (the five-dimensional counterpart).** Let l5 > 0, μ0 ≥ √72 l5², A > 0 and env ∈ C_c^∞([v_start, v_end]), and
let g0 be the Vaidya metric (2.3) with μ(v) = μ0 + (2/9) A² ∫_(−∞)^v env². Fix T > 0, τ0 with v_start − τ0 > √μ0 + 1,
and K ≥ 6. There are λ0 > 0 and C, depending on (l5, μ0, A, env, T, τ0, K) and the inner radius a of Ω, and not on λ,
such that for every λ ∈ (0, λ0] there is a smooth Lorentzian metric g_λ on Ω ⊃ D_T ∩ {τ ≥ τ0} with:

1. **Vacuum and symmetry.** Ric(g_λ) = 0 on Ω, and g_λ is invariant under the T² action and both reflections. 2.
**Data.** On Σ_τ0, the Cauchy data of g_λ satisfy the vacuum constraints exactly, equal the data of the seed
(five-dimensional Schwarzschild–Tangherlini of mass μ0) on r < v_start − τ0, and differ from those of an approximate
solution g_app (section 4) by O(λ^K) in the λ-scaled norm (E4) of the supplement; the leading oscillation of g_app is
the waves of section 2.4. 3. **The remainder.** g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω, where
g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j] with smooth profiles g_j(X, θ), 2π-periodic in θ, evaluated at θ = v/λ. 4.
**Convergence.** |g_λ − g0| ≤ C λ and |∂g_λ| ≤ C on Ω; ∂g_λ − ∂g0 = dv ⊗ [∂_θ g1] + O(λ), so ∂g_λ → ∂g0 weakly in L²(Ω),
and not strongly wherever env ≠ 0. The limit g0 satisfies Ric(g0) = (3 μ'/(2 r³)) dv ⊗ dv with (2.6): it is not vacuum
but Einstein–null dust with one family. 5. **Gauge and uniqueness.** D(g_λ) = 0 on Ω, and g_λ is the only C² solution of
Ric^H(g) = 0 on Ω with its data. 6. **The spheres' horizon.** If μ0 > √72 l5² and λ ≤ λ1 (Proposition 3.3), the outgoing
expansion of the spheres {v, r = const} has at most one zero on each column (v and the angles fixed), exactly one within
C λ of √μ(v) on the columns that reach across it, the spheres below it being trapped and those above it untrapped: no
inner zero, and the zero converges to √μ at O(λ) (Proposition 3.3). 7. **Mean mass.** For every sphere S_(v,r) of the
domain, its Hawking mass satisfies |M[S](g_λ) − μ(v)| ≤ C λ² before and after the shell (v ≤ v_start or v ≥ v_end), and
≤ C λ within it (Proposition 3.4).

The constants that the argument fixes explicitly: the order of the energy is k = 6, the approximant used has N = K + 3
stages, λ ≤ λ1 := min(1, δ0)/10 where δ0 := r_q(μ0) − a, and the data are solved in H^s(S³) with s > 3/2 + 4. λ0 and C
are not evaluated. Every constant of the approximant's own estimates is λ-independent, because its profiles are
(deduced: supplement 5.4); the waves are high-frequency on all of D once λ < l5/10 (computed:
`docket68/lemmas/counterpart5.py` P1).

**Proposition 3.2 (the boundary; computed R6, deduced).** On x_K = 1, with Φ := r − r_q(v),

    g0⁻¹(dΦ, dΦ) = 1 − √(μ/(√72 l5²)) − r_q μ'/(2 μ),                                                     (3.1)

so the boundary is spacelike for g0 wherever μ > √72 l5² or μ' > 0, and every future causal curve that meets it leaves
D_T there and does not return. If μ0 > √72 l5² the margin is uniform, g0⁻¹(dΦ, dΦ) ≤ −δ with δ := √(μ0/(√72 l5²)) − 1 >
0, and for g_λ the margin is −δ + C λ ≤ −δ/2 once C λ ≤ δ/2 (deduced: |g_λ⁻¹ − g0⁻¹| ≤ C λ on Ω by item 4, and the cone
of future causal covectors moves continuously). If μ0 = √72 l5² exactly, the boundary coincides with the seed's horizon
for v ≤ v_start and is null there.

**Proposition 3.3 (one zero per column of the spheres' outgoing expansion; deduced, with `docket68/n1star/horizon5.py`
H1–H3; supplement Proposition 8.1).** Let μ0 > √72 l5², K ≥ 6, and let θ⁺_λ(v, r, ω) be the outgoing null expansion, for
g_λ, of the sphere S_(v,r) := {τ = v − r, |x| = r} at its point of angle ω. There are λ1 ∈ (0, λ0] and C, δ1 > 0 such
that for λ ≤ λ1: on every column (v and ω fixed, r varying, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero, positive
above it and negative below; on the columns with √μ(v) ≤ v − τ0 − δ1 it has exactly one, R_λ(v, ω), with |R_λ − √μ(v)| ≤
C λ; and the spheres with r ≤ √μ(v) − C λ are trapped, those with r ≥ √μ(v) + C λ untrapped.

*Proof.* For g0 the outgoing null normal of S_(v,r) with n(τ) = 1 has expansion θ⁺ = (2r²/(r² + μ)) · 3(1 − μ/r²)/(2r),
whose one zero r = √μ is simple, ∂_r θ⁺ = 3/μ there, and the ingoing expansion is −3/r (computed, H1). θ⁺ is a smooth
function of g, linear in ∂g. The approximant's leading wave enters θ⁺ at order λ⁰ only as (1/2) k(ℓ) ∂_θ(tr_S W), and
tr_S W = tr_g0 W = 0 because W(ℓ, ·) = 0 (computed: H2 for a sample profile tangent and traceless on the spheres, and
H2b for the record's wave itself at the shifted phase θ + φ1, with χ dv² and a mean m1, symbolically in every function;
a trace gives an O(1) oscillation); the mean m1 has no θ-dependence and the higher profiles enter at O(λ). Along a
column v is constant (H3), so the r-derivative of a profile term [f] is [∂_r f], with no λ⁻¹: θ⁺(g_app) − θ⁺(g0) and its
r-derivative along columns are O(λ). The remainder contributes C(|w| + |∂w| + |∂²w|) ≤ C λ^(K−5) ≤ C λ (Theorem E,
supplement section 4 Step 1). Away from √μ the background expansion is bounded away from zero on the compact columns,
and near it θ⁺_λ is strictly increasing in r; √μ(v) − r_q(v) = μ^(1/4)(μ^(1/4) − (√72 l5²)^(1/4)) ≥ its value at μ0 > 0.
The intermediate value theorem and the monotonicity give the zero and its uniqueness. If μ0 = √72 l5², the first
statement holds on every column, and the others on the columns with μ(v) ≥ μ0 + δ1. ∎

**Proposition 3.4 (the mean mass; deduced, with `docket68/n1star/mass5.py` M1–M4; supplement Lemma 8.2 and Proposition
8.2).** For a 3-sphere S let M[S](g) := R²(1 + (R²/9)⟨Θ⟩), with R := (Area(S)/(2π²))^(1/3), Θ := 2θ⁺θ⁻/(−g(n⁺, n⁻))
built from its two future null normals and their expansions, and ⟨·⟩ the mean over S: the five-dimensional Hawking mass,
with M[S_(v,r)](g0) = μ(v) (computed, M1). Then for K ≥ 6 and λ ≤ λ0, |M[S_(v,r)](g_λ) − μ(v)| ≤ C λ² wherever v ≤
v_start or v ≥ v_end, and ≤ C λ for v_start < v < v_end.

*Proof.* Let σ be the isometry θ ↦ π/2 − θ, φ1 ↔ φ2 of S³; it fixes τ, r and v, is an isometry of g0 and maps each
S_(v,r) to itself (computed, M4). The waves' two polarizations are a quarter turn apart, and that makes the leading
wave odd under σ combined with the phase reflection θ ↦ 3π/2 − θ: W_TT(σX, 3π/2 − θ) = −W_TT(X, θ) (computed, M2;
one quadrature alone, or two in phase, is not odd). The two-scale operator is equivariant under θ ↦ c0 − θ with
λ ↦ −λ (computed, M3), and every stage of the approximant is the unique solution of a problem that this combined map
carries to itself, so the profiles obey σ*g_j(·, 3π/2 − ·) = (−1)^j g_j; for the first mean correction,
σ*m1 = −m1. Outside the shell the oscillating profiles vanish, so g_app = g0 + λ m1 + O(λ²) there, and
M[S](g_λ) = μ(v) + λ DM[m1] + O(λ²) + O(|w| + |∂w|). M is natural, so DM[σ*m] = DM[m], and
DM[m1] = DM[σ*m1] = −DM[m1] = 0. The remainder is at most C λ^(K−4) ≤ C λ². Inside the shell the wave enters M only
through its trace on the sphere and the trace of its phase derivative, both zero, so the difference is O(λ). ∎

The numerics' "mean mass" is the angular mean of the mass aspect at past null infinity; the Hawking mass of the
spheres of the domain is its counterpart here. Theorem 2 below gives the waves' field at past null infinity exactly; what
it implies for a mass there is in section 6, and what it does not, in section 8.

*How Theorem 1 follows.* It is the conjunction of three theorems proved in the supplement and summarized in sections 4
and 5: Theorem A (the approximant to any order), Theorem D (exact data within O(λ^K) of it) and Theorem E (existence on
Ω with λ-uniform remainder estimates). D(g_λ) solves a homogeneous linear wave system by the contracted Bianchi
identity and vanishes with its first derivative on Σ_τ0 (the gauge condition and the constraints), so D = 0 on Ω and
g_λ is vacuum (deduced; the identity READ in [LR05] p. 1 and, in n + 1 dimensions, [CBCL06] section 3: "the
harmonicity functions F^μ := □_g x^μ satisfy an homogeneous linear system of wave equations on (V, g), with also
∂_t F^μ = 0, hence F^μ = 0 if (V, g) is globally hyperbolic"). The symmetry follows from uniqueness, since Ric^H and D
are built from g and the O(4)-invariant g0 alone and the data are invariant.

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
4. on Ω, the conclusions of Theorem 1 hold, with the data on Σ_τ0 now the trace of g_λ itself;
5. g_λ is T² × Z2 × Z2-invariant, and unique among solutions with item 1 whose difference from g_app is O(t^(−3/2))
   with its first derivatives and whose energy on the slices tends to zero at past null infinity.

So the counterpart holds with the waves' own free data at past null infinity, and the constraints need not be solved
on this route (section 5.5 is the other route).

*How Theorem 2 is proved.* Before the shell the solution is the black hole: the region v ≤ v_start is a past set for
the black hole's cones, and the data there are the black hole's. Near past null infinity every stage of the approximant
is solved with nothing coming in. Each stage has an explicit leading term in r and a remainder half a power of r
better, and no source of the stages ever falls off like r^(−5/2), the rate that would produce a logarithm (P2–P5). So
the residual decays like r^(−3), and the remainder can be estimated with the rotations as commutators, which gain
t^(−3/2) in Sobolev's inequality. The past is split at t = λ^(−2). Before the split, the one large coefficient of
section 5.1 integrates in time to a constant, and no decomposition is needed. After it, the decomposition of section
5.2 runs over an interval of length λ^(−2). There the transport of its auxiliary field loses a logarithm per unit of
log t, which weights (T/t)^β0 absorb at a cost λ^(−2β0); β0 does not depend on the order of the approximant, so a
higher order pays it. The mollifier's commutator with the wave operator is, apart from decaying terms, an exact
derivative along the generators (P8), and is absorbed into the auxiliary field. The limit is vacuum because the gauge
field of the approximant decays at past null infinity, so its energy tends to zero there and the gauge field vanishes.
A first independent verifier found the near-region estimate incomplete: that commutator was missing. A second found
that the repair closes it (supplement log D34–D35).

**Theorem 3 (the Bondi mass at past null infinity; deduced, supplement section 11; computed:
`docket68/n1star/bondi5.py` B1–B4).** Let g_λ be the metric of Theorem 2, 0 < λ ≤ λ_P. Near past null infinity it
admits Bondi coordinates (v_B, r_B, θ_B, φ1, φ2) — v_B null with v_B − v → 0 at past null infinity, θ_B constant along
the generators, r_B the areal radius — in which

    g_λ = −e^(2β) W dv_B² + 2 e^(2β) dv_B dr_B + r_B² [e^(−2(P1+P2)) (dθ_B − U dv_B)² + cos²θ_B e^(2P1) dφ1²
          + sin²θ_B e^(2P2) dφ2²],                                                                        (3.2)

with P1, P2, β, U, W − 1 expanded in r_B^(−1/2) to order r_B^(−3) with o(r_B^(−3)) remainders, coefficients smooth in
(v_B, θ_B) and zero for v_B ≤ v_start. In it:

1. P_i = r_B^(−3/2) p_i + O(r_B^(−5/2)), p_i the free data of section 2.4 at phase v_B/λ (the radiation field of
   Theorem 2, item 2); the r_B^(−2) coefficients vanish;
2. W = 1 + r_B^(−3/2) V1 − r_B^(−2) M + O(r_B^(−5/2)), with V1 a divergence on S³ and the mass aspect M obeying,
   pointwise, the five-dimensional Bondi law [TTS09] (28) time-reversed,

       ∂_v M = (4/3)(∂_v p1² + ∂_v p1 ∂_v p2 + ∂_v p2²),                                                      (3.3)

   with M = μ0 for v_B ≤ v_start;
3. the Bondi mass μ_B(v) := ⟨M(v, ·)⟩ (the mean over S³) therefore obeys μ_B' = the flux of section 6, exactly: it
   is μ(v) + O(λ) while the shell passes, with the oscillation (6.1) gives, and μ(v_end) + (2/9) λ² A² ∫ env'² + O(λ³)
   after it;
4. the Hawking mass M[S] of Proposition 3.4 of the Bondi spheres S = {v_B, r_B = const} tends to μ_B(v_B) as
   r_B → ∞.

This is the record's "mean mass at past null infinity" — the sphere mean of the Bondi mass aspect, the quantity the
numerical solver integrates — now proved for g_λ.

*How Theorem 3 is proved.* At fixed λ the far region of Theorem 2 is a neighbourhood of past null infinity, and
there the remainder g_λ − g_app is a solution of a wave equation whose source decays like r^(−3): subtracting its
leading term, which is explicit, and estimating the rest with the energy of Theorem 2's far region gains half a power
of r at each step, so g_λ − g0 has an asymptotic expansion in r^(−1/2) to any order, with the radiation field as its
leading term; the derivatives along the ingoing generators of the remainders gain a full order, because the wave
equation is a transport along the outgoing generators for them, and those generators reach the seed region, where
everything vanishes, after a bounded parameter length (supplement Proposition 11.1). The Bondi coordinates are then
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

**Phase and profiles.** The phase is v, an exact eikonal of g0 (Proposition 2.2(c)). A profile is a smooth f(X, θ) on Ω
× S¹; [f](X) := f(X, v(X)/λ); ⟨f⟩ is its θ-mean. Derivatives are measured in the λ-scaled norm |f|_j := Σ_(i≤j) λ^i ‖∂^i
f‖_(L²(Σ_τ)), in which an oscillation costs nothing: ∂_a [f] = λ⁻¹ (∂_a v)[∂_θ f] + [∂_a f]. For a profile G the
two-scale operator R[G] is Ric^H with ∂_a replaced by ∂_a + λ⁻¹ (∂_a v) ∂_θ; it contains no explicit θ, so

    R[G(·, · + c)](X, θ) = R[G](X, θ + c)   for every constant c.                                       (4.1)

**Stage 0 (computed, `docket68/n1star/lead5.py` L1–L5).** With W := W_TT + χ dv², the expansion
R[g0 + λW] = λ⁻¹ R^(−1) + R^(0) + O(λ) has R^(−1) = 0 (because g0⁻¹(dv, dv) = 0); the θ-mean of R^(0) vanishes exactly
under (2.6); with χ = 0 its oscillating part is a second harmonic in the vv component only; χ enters R^(0) only as
−(∂_r + 3/(2r)) ∂_θ χ in vv; and W(ℓ, ·) = 0, tr W = 0. So χ solves a transport along ℓ, smooth at the axes because ℓ
has no angular component, and R^(0) ≡ 0 identically in (X, θ).

**Higher stages (deduced; supplement 5.2–5.4).** The ansatz G = ḡ + λW + Σ_(j≥2) λ^j ĝ_j(X, θ), with mean metric
ḡ = g0 + Σ λ^j m_j and phase u = v + Σ λ^j φ_j, is solved order by order. Each order m ≥ 1 is a linear system with
smooth coefficients for the mean m_m (a wave equation), the phase correction φ_m (a transport, imposing that u stays
an eikonal of the mean metric to that order), the oscillating profile ĝ_(m+1) (a transport along ℓ) and □̃φ_m (a
transport by (2.4)); the system closes without loss and has a unique smooth solution on Ω for smooth data. Rewritten
with the fixed phase v, the profiles g_j satisfy (supplement 0.4):

- (E1) transversality: (g1 − ⟨g1⟩)(ℓ, ·) = 0;
- (E2) the leading equation: R^(0) ≡ 0 in (X, θ);
- (E3) the residual: |Ric^H(g_app)|_k ≤ C λ^(N−1).

**Theorem A (deduced, supplement section 5; verified, see Appendix C).** For every N and every smooth choice of stage
data there are profiles with (E1)–(E3), whose oscillating part of g1 is the waves of section 2.4 with the second
harmonic χ dv² and a phase shift, on the background (2.6).

---

## 5. Proof of the uniform existence theorem

This is the uniform existence statement (called N1* in the working notes): for λ ≤ λ0 the vacuum solution with the given
data exists on the fixed domain, and its remainder after the approximant obeys estimates uniform in λ, in a formulation
that loses no derivatives, is regular across the axes, and works on the large background. The supplement gives every
step; here is its structure, with the identities on which it turns.

### 5.1 The linearization and its one large coefficient

Let P(w) := (d/ds) Ric^H(g_app + s w)|_(s=0). From (2.7),

    P(w) = −(1/2) g_app^(ab) ∂_a ∂_b w + (1/2) λ⁻¹ s(w) [∂_θ² g1] + B·∂w + C·w,     s(w) := w(ℓ, ℓ),           (5.1)

with B, C bounded profiles: second derivatives of g_app, of size λ⁻¹, enter only through w^(ab) ∂_a v ∂_b v, which is
w(ℓ, ℓ) up to O(λ)|w| by (E1). So the only coefficient of size λ⁻¹ couples one scalar component of the remainder,
s = w(ℓ, ℓ), to the wave. This is the five-dimensional form of the coupling Touati describes (READ, [Tou23a] section
3.2.2, p. 20, "The quasi-linear coupling and the loss of derivatives").

**Lemma 5.1 (the phase-shift identity; deduced).** Write P([Y]) = [λ⁻¹ T Y + P_0 Y] for profiles Y. Under (E2),
T(∂_θ g1) = λ T1 with T1 a bounded profile.

*Proof.* Differentiate (4.1) at c = 0 for G the profile of g_app: the linearization of R at G in the direction ∂_θ G
equals ∂_θ R[G]. The left side is T(∂_θ g1) + O(λ); the right side is ∂_θ(λ⁻¹ R^(−1) + R^(0)) + O(λ) = O(λ). ∎

A constant shift of the phase is a symmetry of the leading equation, so its generator ∂_θ g1 is annihilated by the
λ⁻¹ part of the linearized operator. This one line is the analytic content of Touati's transport and polarization
conditions at first order.

### 5.2 The decomposition and the regained derivative

Write w = h + φ [∂_θ g1], with φ(X) defined by the transport along the background generator

    L0 φ = −(1/2) P s,     φ = 0 on Σ_τ0,                                                              (5.2)

where P is a compactly supported mollifier at scale λ adapted to the annuli Σ_τ = {a ≤ |x| ≤ b(τ)}: the averaging ball
is shifted 2λ inward near the outer sphere and outward near the inner one, so that P maps functions on the annulus to
functions on it, with the Bernstein- and Friedrichs-type bounds ‖∂_x P f‖ ≤ C λ⁻¹ ‖f‖, ‖f − P f‖ ≤ C λ ‖∂_x f‖ and ‖[a,
P] ∂_x f‖ ≤ C ‖∂_x a‖_∞ ‖f‖ (supplement Lemma 2.2). It replaces Touati's Fourier projector Π≤ ("a Fourier multiplier
supported in { |ξ| ≤ 1/λ }", READ, [Tou23a] section 3.2.3, p. 21), which needs no boundary.

By Lemma 5.1, the equation for h has bounded coefficients except one, λ⁻¹ ((1 − P) s) [∂_θ² g1], which is O(∂s) by the
mollifier bound (supplement (3.5)). Two derivatives of φ remain on its right side through □̃φ. Contracting the
equation with ℓ ⊗ ℓ kills every λ⁻¹ term and the □̃φ term exactly ([∂_θ g1](ℓ, ·) = 0), so s satisfies a wave
equation with no large coefficient (supplement Lemma 3.3). And Ψ := □̃φ satisfies, by (2.4) applied to (5.2),

    L0 Ψ − (2/r) Ψ = −(1/2) □̃ P s − (1/r)(∂_τ + ∂_r) P s − (3/r²) ∂_r φ,                                 (5.3)

a transport whose source is controlled by the wave equation for s (supplement Lemma 3.4). This is Touati's mechanism
(READ, [Tou23a] p. 20: "The main idea is to show that □_g F is better than ∂² F"), carried out with the exact
commutator (2.4) on the black-hole background.

### 5.3 The energy and the bootstrap

The energy is

    N(τ) := Σ_(j≤6) λ^j (‖∂^j ∂h‖ + ‖∂^j Ψ‖ + ‖∂^j ∂φ‖ + λ ‖∂^j ∂_x² φ‖) + ‖h‖ + ‖φ‖,                    (5.4)

norms in L²(Σ_τ). It controls the remainder: |w|_7 ≤ C N. The energy inequality for −(1/2) g̃^(ab) ∂_a ∂_b u = f on Ω
uses the multiplier −g̃⁻¹ dτ; the lateral boundaries are spacelike with Ω to their past, so their fluxes have a sign and
are dropped (supplement Lemma 2.3). The transport estimate along L0 uses div x̂ = 3/r and the sign of the outer
boundary's motion (Lemma 2.4). Assume N ≤ 2 M λ^K on [τ0, τ*]. Then |w| ≤ C M λ^(K−3), |∂w| ≤ C M λ^(K−4), so
g = g_app + w stays in the class where the domain lemma holds. The nonlinear terms are at most C λ⁻⁵ N² ≤ C M² λ^(2K−5)
≤ C M² λ^(K+1); the residual contributes C λ^K; every linear term is C N. Gronwall gives

    N(τ) ≤ C3 ((C_D + 1 + C_R) λ^K + C M² λ^(K+1)),     C3 independent of M and λ,                         (5.5)

and with M := C3 (C_D + 1 + C_R) + 1 and λ0 small the bootstrap closes at N ≤ M λ^K. The smallness that closes it is
a power of λ, never the size of the data or of the background; this is the one decision in which the proof departs
from Touati's (READ, [Tou23a] p. 12, Theorem 2.2, "There exists λ 0 > 0 and ε 0 = ε 0 (δ, R) > 0 such that if
0 < ε ≤ ε 0").

### 5.4 Existence, continuation and the time lines

The local theory needs the time lines timelike as well as the slices spacelike (READ: [AO14] Theorem 1.1 under (1.3),
"A^00(U) ≤ −κ"; [DS23] (A4), eigenvalues that "do not meet each other"). Inside the horizon the lines of constant x
are spacelike (Proposition 2.2(d)), so the local theorems are applied in other coordinates: the coefficients are
extended beyond Ω by a universal extension operator and convex interpolation of lapse, shift and spatial metric to
Minkowski's; the slices are kept and the time lines are taken along Z = ∂_τ − β (β the shift), for which g(Z, Z) < 0;
the system is posed on a large torus with its coefficients clamped in time outside [τ0 − 1, τ_end + 1]; and written as
a symmetric hyperbolic first-order system it satisfies (A1)–(A4) of [DS23]. Restarts use [DS23] Theorem 2.4 ("there
exists some T > 0 depending on ||u0||_r and M̃ such that (1.1) has a unique solution"), with data extended by the
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

Correct the approximant's data (γ, κ) by U = (a, w, q): γ + a dr², κ + w Π + q ⊗ dr + dr ⊗ q (Π the metric of the
spheres). The constraint map (J, ρ) = (2(−div κ + d tr κ), R − |κ|² + (tr κ)²) (READ, [CD03] (2.1), p. 4: "These are
the general relativistic constraint equations whatever the space-dimension n") then has, at the background's data
(computed, `paper/response5.py` R5; `docket68/n1star/data5.py` S2–S4, S6):

    ρ:   (3 r³/(r² + μ)²) ∂_r a − (1/(r² + μ)) ∂_θ² a + …,
         3 r³/(r² + μ)² = θ³ H,   θ² = r²/(r² + μ),   H = 3/√(r² + μ),
    J_r: 6 ∂_r w − (2/r²) ∂_θ q + …,     J_θ: −(2 r²/(r² + μ)) ∂_r q + 4 ∂_θ w + …,                        (5.6)

so ρ is forward parabolic in r for every r > 0 (no ∂_r² a, no ∂_r ∂_θ a, no derivative of (w, q)), and J is symmetric
hyperbolic in (w, q) with r as time: the symmetrizer S = diag(1, −1/(2r²)) gives S A0 = diag(6, 1/(r² + μ)) > 0 and
S A^θ symmetric, with real speeds c² = 2(r² + μ)/(3 r⁴). At the approximant's data there is no coefficient of order
λ⁻¹ (data5.py S2, S4), because the waves have zero trace on the spheres; an oscillating trace would produce one (the
instrument's mutants). The linear system is solved by a Faedo–Galerkin scheme on the eigenspaces of the Laplacian of
S³ with λ-uniform estimates (supplement Lemma 6.4), the nonlinear one by the Kato–Majda scheme, bounded in a high norm
and contracting in a low one (READ: [AO14] section 4.1; [AG22] abstract, p. 1, "the boundedness in the high norm and
contraction in the low norm"), with no smallness; the correction is O(λ^(N−2)) at every order (supplement Proposition
6.5). Beforehand the approximant's stage data are chosen so that its data satisfy the constraints and D = 0 to order
N − 2, by a hierarchy that propagates the gauge order by order (supplement Lemmas 6.1–6.2).

---

## 6. The remaining parts

**(iv) The boundary.** Proposition 3.2: x_K = 1 is spacelike for the limit wherever μ > √72 l5² or μ' > 0, and for
g_λ, λ ≤ λ0, when μ0 > √72 l5²; every future causal curve that meets it leaves D_T there. Exact for g0 (computed R6, and
`docket68/lemmas/hf_theorem5.py` F2, there also machine-checked with Z3); deduced for g_λ.

**(iii) The horizon.** Proposition 3.3 and item 6 of Theorem 1: for g_λ, λ ≤ λ1, each column carries at most one zero of
the outgoing expansion of the spheres {v, r = const}, exactly one within C λ of √μ on the columns that reach across it,
trapped spheres below and untrapped above; no inner zero (deduced). The per-column zero set is not itself a marginally
trapped surface; the statement is about the round family, as the numerics' is. Although ∂g_λ converges only weakly, the
expansion of these spheres does not see the oscillation at leading order, because the wave is traceless on them and the
phase is constant along each column. The numerical solver agrees (`docket68/lemmas/hf_core5.py`; hf_theorem5.py F4: the
horizon's departure halves with λ, ratios 2.47, 2.26, 2.14 and 2.46, 2.26 at μ0/l5² = 100 and 1000).

**The mean mass.** Proposition 3.4 and item 7 of Theorem 1: after the shell, the mass of every sphere of the domain is
the limit's to O(λ²) (deduced) — the mass of the spheres {v, r = const}, not the numerics' mass aspect at past null
infinity. The first-order mean correction m1 need not vanish (in the Bondi-type gauge its source, a tilt of the dust's
direction at O(λ), is computed in `docket68/n1star/ansatz5.py` A5), but it is odd under the quarter-turn symmetry, and a
rotation-invariant mass cannot see it. The numerical solver measures a different quantity, the mean mass aspect at past
null infinity, whose offset quarters at each halving of λ (hf_theorem5.py F4: 5.17, 4.01, 4.02 and 4.65, 3.84); being
fixed by the incoming flux of the free data, its second-order offset is essentially kinematic (an assessment, not
computed).

**The mean mass at past null infinity.** By Theorem 2 the waves' field at past null infinity is exactly λ[W_TT]. The
sphere mean of its flux density, in the normalization of Proposition 2.3, is exactly

    (2/9) A² [env² + λ² env'² − ½ (env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ)]                          (6.1)

(computed, `past5.py` P7). Its integral in v is μ(v) − μ0 plus terms that oscillate with amplitude (λ/18) A² env² while
the shell passes; after the shell it exceeds μ − μ0 by exactly (2/9) λ² A² ∫ env'² + O(λ³). By Theorem 3 this is the
law the Bondi mass of g_λ obeys: the pointwise rate (3.3) of the mass aspect is (4/3)(∂_v p1² + ∂_v p1 ∂_v p2 +
∂_v p2²), whose sphere mean is (6.1), so μ_B(v) − μ0 is that integral, and after the shell μ_B − μ(v_end) = (2/9) λ²
A² ∫ env'² + O(λ³). The numerical solver evolves the metric in the Bondi form (3.2) from the same free data and fixes
the rate of its mass aspect by the same equation, so its mean mass is μ_B as it integrates it: for its envelope
sin⁴(π(v − ½)/3) on [½, 7/2] with A = 1 the coefficient is (2/9) ∫ env'² = 5π²/108 = 0.45693, and the solver's offset
over λ² after the shell is 0.4589, 0.4577, 0.4568 at λ = 0.05, 0.025, 0.0125 (μ0 = 100 l5²) and 0.4578, 0.4569 at λ =
0.025, 0.0125 (1000 l5²): within 0.05 % at the finest wavelength and converging as O(λ) (computed, `bondi5.py` B4;
the quartering of hf_theorem5.py F4 was this rate). What the comparison tests is the law against the solver's own
integration of it; what Theorem 3 proves is that g_λ obeys it.

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
- **What closes the estimates.** HL and T: the smallness ε. LR: angular regularity on a domain short in one null
  direction. Here: powers of λ, with the approximant carried to any order.
- **The derivative loss.** HL: elliptic estimates for the metric. T: a null foliation and a Fourier cut-off. LR: angular
  regularity. Here: the phase-shift identity, the exact commutator (2.4) and a compact mollifier.
- **Conclusion.** HL: uniform convergence, weak L² convergence of derivatives, ∂ in L∞ uniformly. T: g_λ = g0 + λ g(1) +
  … in generalised wave gauge. LR: C⁰ and weak W^(1,2). Here: uniform at O(λ), ∂g bounded, weak L².

**What carries over.** The reduction to a 2+1 system with free waves on a flat, positive-definite target, which here
is two copies of Huneau and Luk's scalar (Proposition 2.1); the geometric-optics construction around an eikonal phase
of the limit; the weak limit as null dust with Isaacson's flux; the time interval fixed in advance.

**What changes.** One more dimension; a T²-mirror class whose orbits degenerate on two axes, so that the reduced system
cannot be used there; a large black-hole background in place of small data, so that the trapped region and a
spacelike inner boundary are inside the domain; data before the shell reaches the hole rather than at past null
infinity or on a maximal slice; one family of dust, not many.

**What the proof needed beyond theirs.** (1) An approximant of every order (Theorem A), so that the nonlinear terms
are beaten by λ and only a linear estimate on the large background must be uniform; (2) the phase-shift identity
(Lemma 5.1), which removes the one large coefficient of that linear problem; (3) the exact commutator (2.4) on
five-dimensional Vaidya, in which the mass drops out; (4) a compactly supported mollifier adapted to a domain with
boundary, in place of a Fourier projector; (5) a domain inside the horizon whose time lines are spacelike, handled by
changing only the independent variables to lines along Z; (6) the constraints solved as a parabolic–hyperbolic
evolution in r with no smallness and no data imposed far out; (7) a gauge hierarchy making D vanish to every order.

---

## 8. What is not proved

- **Settling at late times.** The theorem holds on D_T for each fixed T; Huneau and Luk's theorem, Touati's and Luk
  and Rodnianski's hold on a fixed interval too. Settling for all later v is the nonlinear stability of five-dimensional
  Schwarzschild–Tangherlini within the class. What is known, READ: linear stability against every type of perturbation,
  "higher-dimensional Schwarzschild black holes are stable with respect to all tensorial types of linear perturbations"
  ([IK03] p. 16); and nonlinear asymptotic stability, "the evolution of (SU (2) × U (1))-symmetric vacuum perturbations
  of initial data for the five-dimensional Schwarzschild metric finally converges in a suitable sense to a member of the
  Schwarzschild family" ([Hol08] p. 1, Theorem 1.1 pp. 5–6), in a class where the Einstein equations reduce to 1+1
  dimensions. That class shares our T² but not the reflections: its squashing is a dφ1 dφ2 term, which (2.1) excludes,
  so the two classes meet only in spherical symmetry. The waves here, which depend on the angle θ, lie outside it in any
  case. After the shell only the mean corrections remain: on Ω ∩ {v ≥ v_end}, g_λ differs from Tangherlini of the final
  mass by λ m1 + O(λ²) with its first derivatives (Theorem 1, items 3–4). Settling would therefore follow from the
  small-data stability of Tangherlini in the T²-mirror class, once the solution is also constructed outside D_T. Both
  steps are open here. Linearly more is known, and it applies to the class: the class carries no vector-type
  perturbation and no linearised rotation (computed, `docket68/n1star/settle5.py` T1), and for the other two types the
  gauge-invariant master quantities on five-dimensional Tangherlini decay, "in spacetime dimension six and below, the
  uniform decay estimate Ě^N_Ψ(Σ_τ) ≤ C(n, M) I_Ψ(Σ_0)/τ²" ([HKW18] p. 4, Theorem 2), the part with l < 2 being pure
  gauge plus a linearised Myers–Perry solution (Theorem 1, p. 3), which in the class is a change of mass alone. The
  decay of the metric components themselves is left open there: "We do not treat this matter in the current paper" (p.
  4). In the class it follows from what is written (supplement Proposition 10.1, deduced): for every scalar mode l ≥ 2
  the gauge f_a = 0 = H_T of [KI03] exists, and in it the metric components are [KI03]'s (3.14), the master field and
  its derivatives to order two — two orbit-space derivatives, and a factor l(l + 2) − 3 through the trace — with
  coefficients bounded on r ≥ r_h uniformly in l; the tensor type is its own master field; and l = 1 is absent. So in
  that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation
  in the class settles to a change of mass at [HKW18]'s rate, with the loss of two derivatives so counted. That gauge is
  not the wave gauge of the nonlinear problem. The passage between the two was closed in four dimensions by Hung
  ([Hun19]: the Lichnerowicz equation under the gauge, a gauge vector solving a tensorial wave equation with the master
  quantity as source, the l = 0 sector's stationary one-form and linearly growing gauge-fixed mass change, decay for the
  rest), and its five-dimensional structure is computed in the class (supplement Proposition 10.2,
  `docket68/n1star/wavegauge5.py`): the tensor type is already in harmonic gauge, the scalar gauge vector solves three
  1+1 wave equations per mode with the master field as source, and the l = 0 sector's two non-decaying solutions are
  explicit and regular at the horizon; the decay estimate for that system, Hung's sections 5–8 in five dimensions, does
  not exist and is not attempted; the system is triangular (supplement Proposition 10.2(vi)), each rung a scalar wave
  equation on Tangherlini whose potential obeys the positivity condition Hung's method needs, so the estimate reduces to
  known tools rung by rung — a route, not a proof. No growing mode appears in either type for l = 2, …, 10 to τ = 275
  r_h (settle5.py T5; a finite-time observation), and the late-time tail of the l = 2 master fields, measured from the
  pulse's launch, is t^(−7.05) (tensor) and t^(−7.06) (scalar) on [550, 700] r_h, the same at half the step, approaching
  7 from above with that origin and bracketing 7 (6.89, 7.23) when the origin is shifted by the launch radius either way
  (T6): [CYDL03]'s t^(−(2l+D−2)) for odd D, the flat five-dimensional Green's function's tail, which is the rate a
  nonlinear argument in the class would carry. The least-damped mode of the class is the scalar-type one with l = 2, ω
  r_h = 0.9477 + 0.2561i ([CLY03b] Table 1, p. 8), which evolving the master equation in time reproduces to 1%
  (settle5.py T3, on the barrier of `docket68/lemmas/seed_escape.py`): an e-folding time of 3.905 r_h. The reduced
  problem in the class is 2+1-dimensional, the dimension of Klainerman and Szeftel's polarized axisymmetric stability of
  four-dimensional Schwarzschild ([HKW18] p. 2); its five-dimensional counterpart is open. - - **Physical wavelengths.**
  λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the curvature length, does not
  apply at a wavelength of 10 l5 here (λ is the reduced wavelength of the phase v/λ, as in the numerics' usage). The
  expansion parameter is the wavelength over the curvature length L = K^(−1/4); on x_K = 1, L = l5, and at the horizon L
  = √μ/72^(1/4). For λ = 10 l5 the ratio is 10 on x_K = 1, and 2.91 (μ = 100 l5²) or 0.92 (μ = 1000 l5²) at the horizon
  (computed, R7): there is no separation of scales. The statement that the waves are high-frequency on all of D once λ <
  l5/10 is about the approximant, not about λ0. Against the scale on which the curvature varies, r, the ratio is 1.00
  and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (computed, R7). That is the parameter a construction from exact
  waves would see, in the manner of [AB26], whose layers are waves exact on a locally linear background, with amplitudes
  solving ordinary differential equations ("no sinusoidal identity was used", section 3.1); it is not small either, and
  there the wavelengths are chosen, here prescribed. At a prescribed wavelength without a small parameter, existence on
  D_T is a large-data question; a computed solution with a certified residual and a certified linear estimate could
  settle it (the rigorous numerics cited in [AB26] as [4]), and that is not attempted. Its first step was taken: the
  growth factor measured on the record's own computed solution at 10 l5 (`docket68/n1star/growth5.py`, supplement
  section 10.2). At both seeds that scheme's premise — one zero of the round spheres' expansion per column and the core
  boundary outflow, so that the exterior is fixed by its own data — fails before the shell's peak: a second zero holds
  over 0.04 in v from 1.50 r_h at μ = 100 l5² (1.496 on the finer grid, 1.476 with a shorter hold; a single-step
  excursion at 1.45 is not it) and from 1.583 r_h at 1000 l5² (three grids agreeing to 0.0005), and the boundary ceases
  to be outflow within 0.1 after; a deeper excision fails earlier, not later (r = 0.39 and 0.25 r_h at the first seed,
  0.21 r_h at the second). So no approximant on D_T comes from that scheme at 10 l5 at any excision depth. What the
  computed solution shows is that round spheres inside the seed's horizon cease to be trapped and the boundary to be
  outflow, in the scheme's gauge, while the shell passes; the direction of the untrapping is not a measurement of these
  runs, and nothing is said of the event horizon. The step is re-posed as the characteristic initial value problem in
  double-null gauge — the incoming wave on an ingoing null hypersurface from past null infinity, the seed's outgoing
  cone as the other — where Luk's theorem gives local existence without smallness ([Wu26] Theorem 2.1) and [Wu26]'s
  Theorem 2.2, "the difference of metrics is controlled by the difference of curvature residues" (p. 6), is the a
  posteriori structure; its five-dimensional version in the class is not built. Up to the failure the radiation field's
  growth factor exp ∫K dv is 1.9 and 2.1, and a finite-difference amplification of the data along one direction, a lower
  bound for the propagator's norm, is 1.28 and 1.00; where the scheme completes (λ = 0.1 r_h) they are 6.9 and 1.71,
  while the sup-norm Grönwall factor is 17, 2 × 10⁵ and 6 × 10³: a certified argument would need the propagator's norm,
  not a sup-norm bound. The linear scattering of the shell off the seed at 10 l5 is computed in
  `docket68/lemmas/seed_escape.py`.
- **Beyond the boundary.** Nothing is claimed beyond Ω, whose inner boundary r = a lies a fixed distance inside x_K = 1;
  the statements of Theorem 1 are made on D_T.
- **More families.** Several dusts, angular separation, and the passage to Vlasov matter are not attempted.
- **The boundary at equality.** If μ0 = √72 l5² exactly, x_K = 1 is null on the seed's portion (Proposition 3.2).
- **Review.** An eighth independent verifier read this paper and the supplement's last restatement (log D26): no major
  finding; its two minor findings and 21 notes are seated. Propositions 3.3 and 3.4 were added after it, and were read
  with the supplement by a ninth (D30). Theorem 2's proof was read by a tenth, which found the near-region estimate
  incomplete, and, after the repair, by an eleventh, which found it closed (D34–D35). The paper's text on Theorem 2 and
  the additions to sections 6 and 8 have not been read by a verifier. Theorem 3 and the supplement's section 11 were
  read by a twelfth, which found no major gap and five minor ones, repaired in place with its four notes (D40); the
  repairs, the supplement's section 10.3 with its reading in section 8 (D39) and the measurement of section 10.2 (D38,
  D41) were read by a thirteenth (D44), which found two major gaps — Lemma 11.0's energy identity, run on a region
  unbounded toward past null infinity, repaired by running it on the approximating solutions of Theorem 2's
  construction; and section 10.2's break time at the first seed, a single-step transient of the root count, repaired by
  the persistence criterion that moves it from 1.45 to 1.50 — with nine minor findings and notes, seated. Those repairs,
  the deeper excisions (D43) and section 10.4 with its reading here (D42) were read by a fourteenth (D45): the repair of
  Lemma 11.0 closes the gap; one major finding, the physical reading of section 10.2's data (the direction of the
  untrapping and a sentence on the event horizon, not supported by what the runs stored, withdrawn here and in the
  supplement), and seven minor ones, seated. The repairs of D45, this paper's text on Theorem 3 and the route of D46
  have not been read by a verifier.

---

## 9. References

Each was READ at source for this paper or for the proof, on the date and at the page given; quotations are verbatim
from the arXiv text, with the extraction's spacing.

- [HL18] C. Huneau, J. Luk, *High-frequency backreaction for the Einstein equations under polarized U(1)-symmetry*, Duke
  Math. J. 167(18) (2018) 3315–3402, arXiv:1706.09501v1. READ 2026-10-20: p. 1 (Burnett's formulation), pp. 2–3 ((1.3),
  (1.4), Theorem 1.1), pp. 8–10 (Definition 3.2, Theorem 3.3, Corollary 3.5, Definition 4.1, Theorem 4.2).
  arXiv:1706.09499 is the companion paper [HL18e]; the two are easily confused.
- [HL18e] C. Huneau, J. Luk, *Einstein equations under polarized U(1) symmetry in an elliptic gauge*, Comm. Math. Phys.
  361(3) (2018) 873–949, arXiv:1706.09499v1. READ 2026-10-20: abstract and introduction, p. 1.
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
- [CBCM10] Y. Choquet-Bruhat, P. T. Chruściel, J. M. Martín-García, arXiv:1006.4467. READ 2026-10-20: (2.7)–(2.9) (arXiv
  HTML, unpaginated).
- [CBCL06] Y. Choquet-Bruhat, P. T. Chruściel, J. Loizelet, arXiv:gr-qc/0608108v2. READ 2026-10-20: (3.1), sections 3
  and 5.1.
- [LR05] H. Lindblad, I. Rodnianski, arXiv:math/0411109v2. READ 2026-10-19: p. 1, (1.3) p. 2, section 2.2 p. 8.
- [IK03] A. Ishibashi, H. Kodama, *Stability of higher-dimensional Schwarzschild black holes*, Prog. Theor. Phys. 110
  (2003) 901, arXiv:hep-th/0305185v3. READ 2026-10-20: abstract p. 1, sections 2.1–2.3, summary p. 16.
- [TTS09] K. Tanabe, N. Tanahashi, T. Shiromizu, *On asymptotic structure at null infinity in five dimensions*,
  arXiv:0909.0426v2 (2010). READ: pp. 2–5, (4)–(5), (20)–(21), (26)–(28), (35)–(36).
- [HL21] L. He, H. Lindblad, *Masses at null infinity for Einstein's equations in harmonic coordinates*,
  arXiv:2107.01487v2 (2022). READ: section 3, Proposition 3.2, p. 11 (the eikonal function from wave coordinates).
- [HKW18] P.-K. Hung, J. Keller, M.-T. Wang, *Linear stability of higher dimensional Schwarzschild spacetimes: decay
  of master quantities*, arXiv:1809.05144v1. READ 2026-10-20: abstract p. 1; pp. 2–4 (Theorems 1 and 2); p. 69
  (Theorem 22).
- [CLY03b] V. Cardoso, J. P. S. Lemos, S. Yoshida, *Scalar-gravitational perturbations and quasinormal modes in the
  five dimensional Schwarzschild black hole*, arXiv:hep-th/0311260v2. READ 2026-10-20: (2.1)–(2.7), pp. 3–4; Tables
  1–3, pp. 8–9.
- [KI03] H. Kodama, A. Ishibashi, *A master equation for gravitational perturbations of maximally symmetric black
  holes in higher dimensions*, arXiv:hep-th/0305147v3. READ 2026-10-20: (2.4), (2.7)–(2.8), pp. 4–5; p. 7 (l = 1);
  (3.1), (3.13)–(3.14), pp. 8–10; section 5.1, p. 13.
- [CYDL03] V. Cardoso, S. Yoshida, O. J. C. Dias, J. P. S. Lemos, *Late-time tails of wave propagation in higher
  dimensional spacetimes*, arXiv:hep-th/0307122v3. READ 2026-10-20: (14), p. 4; p. 2; Fig. 2 and p. 5.
- [Hun19] P.-K. Hung, *The linear stability of the Schwarzschild spacetime in the harmonic gauge: even part*,
  arXiv:1909.06733v1. READ 2026-10-20: (1.4); (4.21)–(4.23); (8.1), (8.39); sections 5–8 for their structure.
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
- [AB26] L. Alpöge, T. Buckmaster, *Blowup for the Boussinesq equations with smooth forcing*, preprint (September
  2026), cims.nyu.edu/~tristanb/boussinesq.pdf. READ 2026-10-20: section 1.2 (the layers and the wave), section 3.1
  (Lemma 3.1 and its proof), the bibliography ([4], Chen and Hou, arXiv:2210.07191v4 and arXiv:2305.05660v3).
- [Hol08] G. Holzegel, *Stability and decay-rates for the five-dimensional Schwarzschild metric under biaxial
  perturbations*, arXiv:0808.3246v1. READ 2026-10-20: abstract p. 1, the model pp. 3–5, Theorem 1.1 pp. 5–6.
- [CD03] P. T. Chruściel, E. Delay, *On mapping properties of the general relativistic constraints operator in weighted
  function spaces, with applications*, arXiv:gr-qc/0301073v2. READ 2026-10-20: (2.1)–(2.2), p. 4.
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
- [SY21] Z. Shi, L. Yao, arXiv:2110.14477v4. READ 2026-10-20: sections 1, 2.1 (Rychkov's and Stein's operators).
- [AG22] F. Angeles, *The Cauchy problem for a quasilinear system of equations with coupling in the linearization*,
  arXiv:2204.01179v3. READ 2026-10-20: abstract, p. 1; (9.6)–(9.7), p. 24.
- Burnett (1989), Isaacson (1968) and Choquet-Bruhat (1969) are cited through [HL18] p. 1, [HL24] pp. 1, 32 and [LR20]
  p. 3, where they are quoted; their originals were not re-READ for this paper.

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
- R5: (5.6): ρ parabolic in a, J symmetric hyperbolic in (w, q), S, the speeds, θ³H. Control: a γ in place of
  a dr² brings ∂_r² a into ρ.
- R6: h²(c⁴ + s⁴) = 1; 4(a² + ab + b²) = (2a + b)² + 3b²; (3.1). Controls, each run on its own: h = 1;
  (2a + b)² + 2b²; r + r_q in place of r − r_q; √48 in place of √72.
- R7: λ = 10 l5 against the curvature length: 10 on x_K = 1, 2.91 and 0.92 at the horizon; against r: 1.85 and
  1.04 on x_K = 1, 1.00 and 0.32 at the horizon. Control: 48 for 72.

All seven pass and every control is rejected (about 30 seconds). The proof's programs, in `docket68/n1star/`:

- `ks5.py` K1–K5: the Kerr–Schild form, its inverse, the commutator (2.4), div L0, the gauge source H0. 5/5;
  mutants 4/4.
- `foliation5.py` B1–B4: the null foliation, the slices and the domain. 4/4; mutants 5/5.
- `ansatz5.py` A1–A5: the ansatz to order λ² on Vaidya with phase v. 5/5; mutants 5/5.
- `lead5.py` L1–L5: stage 0: R^(−1) = 0, the energy condition, χ. 5/5; mutants 4/4.
- `data5.py` S0–S6: the slice data, the constraints' principal part, no coefficient of order λ⁻¹. 7/7; mutants 6/6.
- `horizon5.py` H1–H3, H2b: the expansion of the spheres for g0, no O(1) oscillation from a wave traceless on them
  (H2b: the record's wave, phase-shifted, symbolically), the phase constant along columns. 4/4; mutants 4/4.
- `mass5.py` M1–M4: the Hawking mass of the Vaidya spheres, the wave odd under the quarter-turn symmetry, the
    two-scale operator's equivariance, σ an isometry of g0. 4/4; mutants 5/5.
- `past5.py` P1–P8: Theorem 2's past domain, the operator and the transport near past null infinity, the leading
  wave's components, the stage-0 source, the rotations, the flux of the radiation field, the mollifier's commutator.
  8/8; mutants 9/9.
- `growth5.py` G0–G5: the go/no-go at 10 l5 on the record's own scheme — two measures of K at every step, the failure
  of the scheme's premise on three grids and at three deeper excisions, a finite-difference amplification; G0 live,
  G1–G5 against the twelve pinned runs (`data/growth5_runs.json`, regenerated by `--run` and `--merge`); numerical. all
  pass.
- `settle5.py` T1–T6: the class's perturbation types, the potentials, the l = 2 ringdown against [CLY03b], the
  settling times, no growing mode for l = 2, …, 10, the late-time tail t^(−7) against [CYDL03]; T3, T5, T6
  numerical. 6/6; mutants 6/6.
- `wavegauge5.py` W1–W6: the passage to the harmonic gauge on five-dimensional Tangherlini in the class (supplement
  Proposition 10.2): the Lichnerowicz identity and Γ[π_X] = □X on a tensor and a one-form of the class, the l = 0
  stationary one-form regular at the horizon, the gauge-fixed mass change growing linearly in t, the scalar gauge
  vector's three 1+1 equations at l = 2 and 4, the tensor type already harmonic, the gauge-vector system triangular with
  every rung a scalar wave equation whose potential obeys Hung's positivity condition. 6/6; mutants 6/6 (about a minute
  and a half).
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

## Appendix B. The author's words

The commission and the rules that bind it, verbatim, with the item numbers of the author's record; where they enter,
they are the author's postulates, not evidence. Line breaks and runs of spaces are normalized; one word naming the
research tree, and in 509 the part of the message about another matter, are elided and marked "[…]".

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
full, and its log `docket68/n1star/N1STAR-LOG.md` records each decision (D1–D46).

| claim | where it is established |
| --- | --- |
| Proposition 2.1 | R1; `docket68/lemmas/kn_gauge.py` K1–K2 |
| Proposition 2.2 | R2–R4; `docket68/n1star/ks5.py` K1–K5; supplement 0.1, Lemma 1.1 |
| (2.4) | `docket68/n1star/ks5.py` K3; [Tou23a] Lemma 3.1 for comparison |
| domain Ω | supplement (1.1), Lemma 1.1; `docket68/n1star/foliation5.py` B1–B4 |
| Proposition 2.3, (2.6) | `docket68/n1star/lead5.py` L2; R6; `docket68/lemmas/hf_theorem5.py` F3 |
| (2.7) | [CBCM10] (2.7)–(2.9); supplement 0.2 |
| Theorem 1 items 1–5 | supplement 0.4–0.7 (Theorems E, A, D), sections 1–6 |
| Proposition 3.2 | R6; `docket68/lemmas/hf_theorem5.py` F2 (Z3); deduction in section 3 |
| Theorem A | supplement section 5; `docket68/n1star/lead5.py`, `ansatz5.py` |
| Lemma 5.1, (5.1)–(5.3) | supplement 3.2–3.3, Lemmas 3.1–3.4 |
| (5.4)–(5.5) | supplement section 4, Steps 1–7 |
| section 5.4 | supplement section 4, Step 8; [DS23], [AO14], [LY22], [SY21], [BH17] |
| (5.6) | R5; `docket68/n1star/data5.py` S2–S4, S6; [Rac16]; [CD03] |
| section 5.5 iteration | supplement Lemma 6.4, Proposition 6.5; [AO14], [AG22], [GO13] |
| part (iii), Proposition 3.3 | supplement Proposition 8.1; `docket68/n1star/horizon5.py` H1–H3; Theorem E Step 1 |
| mean mass, Proposition 3.4 | supplement Lemma 8.2, Proposition 8.2; `docket68/n1star/mass5.py` M1–M4 |
| Theorem 2 | supplement section 9 (Lemmas 9.1–9.7, 9.4b, Theorem A_P, Propositions 9.8–9.9); `past5.py` P1–P8 |
| the flux at past null infinity | supplement section 9.5; `docket68/n1star/past5.py` P7 |
| Theorem 3, (3.2)–(3.3) | supplement section 11 (Propositions 11.1–11.3); `docket68/n1star/bondi5.py` B1–B3; |
| | [TTS09] (28); [HL21] section 3 for the chart's construction |
| the numerics' mean mass, section 6 | `docket68/n1star/bondi5.py` B4 over the solver's runs |
| | (`docket68/lemmas/data/hf_core5_runs.json`); `paper/response5.py` R8 |
| the wavelength 10 l5, section 8 | supplement section 10.2; `docket68/n1star/growth5.py` G0–G5 over its pinned runs; |
| | `paper/response5.py` R7 |
| settling, section 8 | supplement sections 10.1, 10.3 and 10.4 (Propositions 10.1–10.2); `docket68/n1star/settle5.py` |
| | T1–T6; `docket68/n1star/wavegauge5.py` W1–W6; [HKW18], [KI03], [CLY03b], [CYDL03], [Hun19] |
| verification | supplement section 7: seven independent verifiers, one at a time (log D12, D15, D16, D18–D21); the |
| | eighth read this paper and the supplement's last restatement (log D26); the ninth sections 8.1–8.2 (D30); |
| | the tenth and eleventh Theorem 2's proof (D34–D35); the twelfth Theorem 3 (D40); the thirteenth |
| | the repairs of D40 and sections 10.2–10.3 (D44) |
| the standard theorems READ | supplement section 7, the retrieval table (log D17–D18) |

## Appendix D. Reproduction

Python 3.11 with sympy; z3-solver for `foliation5.py`; numpy for `bondi5.py` and `growth5.py`, numpy and scipy for
`settle5.py`. `growth5.py` imports the solver `docket68/lemmas/hf_mirror5.py` and `past5.py` imports `lead5.py`; the
others import nothing from the research tree:

    cd paper && python3 response5.py --selftest          # R1-R7, about 30 seconds
    python3 response5.py --selftest --full               # and the five proof programs, about 20 minutes
        cd ../docket68/n1star && python3 ks5.py --selftest   # and foliation5, ansatz5, lead5, data5, horizon5, mass5,
                                                         # past5 (about 4 minutes), settle5, bondi5 (about ten minutes)
                                                         # wavegauge5 (about a minute and a half)
    python3 data5.py --mutants                           # about 80 minutes; each program has --mutants

The md5 of each file this paper rests on, at the commit that adds it:

| file | md5 |
| --- | --- |
| `paper/response5.py` | `187d2de19d94308e5f1e0881e97b1fa6` |
| `docket68/n1star/N1STAR-PROOF.md` | `4a0d06bb18c39c8787578a8611aae368` |
| `docket68/n1star/N1STAR-LOG.md` | `e4a0b4abc61c5da4c22f7463f9100397` |
| `docket68/n1star/README.md` | `e2021ca4cf393f523f34259ec7dc884e` |
| `docket68/n1star/ks5.py` | `4fb7563006d79b3144b42b761300830a` |
| `docket68/n1star/foliation5.py` | `dab023e393662863f1f608b5d087dc9c` |
| `docket68/n1star/ansatz5.py` | `e0f4a8fbf191effb4115aff1e4a655ac` |
| `docket68/n1star/lead5.py` | `ba26d7df17f37eb6932d5b7133656d1a` |
| `docket68/n1star/mass5.py` | `ebe2ee78219553f4b57a4200604752e5` |
| `docket68/n1star/horizon5.py` | `962ca2fb9404bebbce8420075f080dbd` |
| `docket68/n1star/past5.py` | `d6742977ac642377ecc3785759dd526c` |
| `docket68/n1star/settle5.py` | `8f2c81317211e47666881113aa18e3a0` |
| `docket68/n1star/bondi5.py` | `bbd4416da0fcf101b89e1d782e7b4955` |
| `docket68/n1star/growth5.py` | `08250577e8cdb45b3f1623dd15268257` |
| `docket68/n1star/wavegauge5.py` | `a0fe5c550659ec6219673a0111b4f75c` |
| `docket68/n1star/data5.py` | `9404eb2d500b5b5fc810ee136bea2272` |
| `docket68/lemmas/hf_theorem5.py` | `81e96f5af9eb31fc80669d582763d5be` |
| `docket68/lemmas/counterpart5.py` | `e7dcf7bf898c2147492d28c5fb888d18` |
| `docket68/lemmas/kn_gauge.py` | `7e9e9ef8ec12e670f1717ec4fe8bd491` |
| `docket68/lemmas/hf_core5.py` | `84b715eb461838abcb5e018cd455eb5c` |
| `docket68/lemmas/seed_escape.py` | `1a8b2ff82872e7096f13bf891a10424c` |

The paper's own md5 is recorded in the commit that adds it, not in itself.
