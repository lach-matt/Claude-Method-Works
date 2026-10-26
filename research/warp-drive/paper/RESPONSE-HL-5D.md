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

Huneau and Luk proved that every generic, small-data, polarized U(1)-symmetric solution of the Einstein–null dust
system is a weak limit of vacuum solutions on a fixed time interval, in an elliptic gauge in which smallness is needed
even for local existence. We prove a five-dimensional counterpart on a large background. In the class of
five-dimensional vacuum metrics with a T² isometry and both reflections, the Einstein equations reduce exactly to 2+1
gravity coupled to two free waves whose target metric, (3/2) dψ² + 2 dω², is flat and positive definite; this is Huneau
and Luk's reduced system with one scalar replaced by two. The background is five-dimensional Vaidya, a black hole of
mass μ0 that grows by an ingoing shell, and the domain runs from before the shell reaches the hole to the surface
inside the horizon where the limit's curvature reaches a fixed scale (spacelike when μ0 > √72 l5²). For every amplitude
A > 0 and every smooth compactly supported envelope, with no smallness of either, we construct a family of T²-symmetric
vacuum metrics g_λ on that domain, of wavelength λ ≤ λ0, with |g_λ − g0| ≤ Cλ, ∂g_λ bounded, and ∂g_λ → ∂g0 weakly but
not strongly, where g0 is Vaidya with dμ/dv = (2/9) A² env²: Isaacson's flux, the null dust of one family. The proof
uses the wave-map gauge relative to the limit itself and an approximate solution of arbitrarily high order, so that
every nonlinear term is beaten by a power of λ rather than by the size of the data; what must be uniform in λ is then a
linear estimate on the black-hole background, and its one large coefficient is removed by a phase-shift identity. The
Cauchy data are constructed by solving the constraints outward in r as a parabolic–hyperbolic system from a sphere
inside the shell. Part (iii) of the counterpart follows: on each column the outgoing expansion of the spheres {v, r =
const} has one zero, converging at O(λ). So does a mean-mass rate: after the shell, the mass of every sphere {v, r =
const} is the limit's to O(λ²), by a quarter-turn symmetry of the two polarizations. The same solutions are constructed
from the waves' free data at past null infinity, where before the shell they are the black hole exactly and their
radiation field is the prescribed one at every λ (Theorem 2). At past null infinity they admit Bondi coordinates and an
expansion in r^(−1/2), and the five-dimensional Bondi mass law holds for them (Theorem 3): their Bondi mass is μ(v) +
O(λ) while the shell passes and μ + (2/9) λ² A² ∫ env'² + O(λ³) after it, the second-order rate the numerics measure,
with its coefficient. Beyond that domain, outside the black hole, we deduce without proving that in the class the
solutions settle at late times to five-dimensional Schwarzschild–Tangherlini, and that every small perturbation of them
without symmetry settles to a slowly rotating Myers–Perry black hole: Hintz's proof of the nonlinear stability of Kerr
carried into five dimensions, every input that depends on the dimension computed at Schwarzschild–Tangherlini and
deduced at nearby Myers–Perry parameters, his companion papers' arguments read at source, and the proofs of theirs the
route uses carried to five dimensions by modification, every place where a full-text census of the source finds the
dimension computed, and every other deduced step placed on its computed and read inputs and on the modification steps,
each now written out at n = 4 against its source proof, at proof level but for one the supplement names; the completeness
of those censuses, evidenced by two methods and not proved, and the deductions themselves, written out at proof level and
read by independent verifiers but not proofs checked at the level of the theorem's statement, separate this from a proof
(Theorem 4). We list what is not proved, the application at physical wavelengths among it.

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

Beyond that domain, and outside the black hole, we deduce — we do not prove — that in the class the solutions settle at
late times to five-dimensional Tangherlini of a nearby mass, and that their small perturbations without symmetry settle
to slowly rotating Myers–Perry black holes (Theorem 4, section 8.8). The route is Hintz's proof of the nonlinear
stability of Kerr [Hin26], carried into five dimensions: every input that depends on the dimension is computed at
Tangherlini, his arguments and those of his companion papers [Hin26a, Hin26c, Hin23a] are read at source for where the
dimension enters, the class removes his boosts, rotations and their gauge modifications, and without it they are
restored, with the inputs at every nearby Myers–Perry parameter deduced by the perturbative route of [HHV21] and the
charges by which the gluing at large radius matches the Myers–Perry family computed, the gluing deduced. What separates
the deduction from a proof is stated in section 8.8. The proofs of those papers that the route uses — [Hin26c]'s
estimates, [Hin26a]'s constraint damping, [Hin23a]'s at null infinity, [CD03]'s gluing, Hintz's boost and [HHV21]'s
perturbation arguments — are carried to five dimensions by modification, every place a full-text census of the source
finds the dimension computed. Every other deduced step is placed on its computed and read inputs and on the modification
steps' conclusions, at proof level but for one that section 8.8 names, and each modification step lists the places where
the dimension changes it, each value computed, deduced in an earlier section, arithmetic in n, or the record's choice.
Each modification step is now written out at n = 4 against its source proof. What remains is that those censuses are
complete, which two methods evidence and nothing proves; the statements at n = 4 that thirty-four of the steps took as
readings are each settled, written out or READ, Hintz's spectral theory re-run proof by proof on bundles among them
(section 8.8).

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

The numerics' "mean mass" is the angular mean of the mass aspect at past null infinity; the Hawking mass of the spheres
of the domain is its counterpart here. Theorem 2 below gives the waves' field at past null infinity exactly; what it
implies for a mass there is in section 6, and what it does not, in section 9.

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
spherical symmetry. The waves here, which depend on the angle θ, lie outside it in any case. After the shell only the
mean corrections remain: on Ω ∩ {v ≥ v_end}, g_λ differs from Tangherlini of the final mass by λ m1 + O(λ²) with its
first derivatives (Theorem 1, items 3–4). Settling would therefore follow from the small-data stability of Tangherlini
in the T²-mirror class, once the solution is also constructed outside D_T. Sections 8.2–8.7 take up both steps.

### 8.2 The linear level

Linearly more is known, and it applies to the class: the class carries no vector-type perturbation and no linearised
rotation (computed, `docket68/n1star/settle5.py` T1), and for the other two types the gauge-invariant master quantities
on five-dimensional Tangherlini decay, "in spacetime dimension six and below, the uniform decay estimate Ě^N_Ψ(Σ_τ) ≤
C(n, M) I_Ψ(Σ_0)/τ²" ([HKW18] p. 4, Theorem 2), the part with l < 2 being pure gauge plus a linearised Myers–Perry
solution (Theorem 1, p. 3), which in the class is a change of mass alone. The decay of the metric components themselves
is left open there: "We do not treat this matter in the current paper" (p. 4). In the class it follows from what is
written (supplement Proposition 10.1, deduced): for every scalar mode l ≥ 2 the gauge f_a = 0 = H_T of [KI03] exists,
and in it the metric components are [KI03]'s (3.14), the master field and its derivatives to order two — two orbit-space
derivatives, and a factor l(l + 2) − 3 through the trace — with coefficients bounded on r ≥ r_h uniformly in l; the
tensor type is its own master field; and l = 1 is absent. So in that Regge–Wheeler-type gauge, with the l = 0 gauge
fixed to the mass change, every metric component of a perturbation in the class settles to a change of mass at [HKW18]'s
rate, with the loss of two derivatives so counted. That gauge is not the wave gauge of the nonlinear problem. The
passage between the two was closed in four dimensions by Hung ([Hun19]: the Lichnerowicz equation under the gauge, a
gauge vector solving a tensorial wave equation with the master quantity as source, the l = 0 sector's stationary
one-form and linearly growing gauge-fixed mass change, decay for the rest), and its five-dimensional structure is
computed in the class (supplement Proposition 10.2, `docket68/n1star/wavegauge5.py`): the tensor type is already in
harmonic gauge, the scalar gauge vector solves three 1+1 wave equations per mode with the master field as source, and
the l = 0 sector's two non-decaying solutions are explicit and regular at the horizon; the decay estimate for that
system, Hung's sections 5–8 in five dimensions, does not exist in the literature and is deduced below, not proved; the
system is triangular (supplement Proposition 10.2(v)), each rung a scalar wave equation on Tangherlini whose potential
obeys the positivity condition Hung's method needs; the estimate is a route of known tools rung by rung, with four
things to be done rather than quoted (the Morawetz currents for the rungs, the r^p weights, the l = 0 argument and
Hung's Proposition 4.2 in five dimensions) — a route, not a proof. The last of the four is computed (supplement
Proposition 10.2(vi), W7): in Hung's components, with the harmonic gauge condition admixed as he does it, the system is
□H = AH + UH with U along the horizon generator in two rows only, the leading matrix has the eigenvalues (l+a)(l+a+2)
for a = −2, …, 2 where his has (l+a)(l+a+1), and the horizon-regular rows carry the positive coefficients 2f′ and f′ in
place of his 4M/r² and 2M/r²; the four-dimensional control (`docket68/n1star/hung4.py`) reproduces his printed rows from
the Schwarzschild metric. On that structure his Proposition 4.1 — the red-shift and r^p estimates for the metric itself,
with the compact region between them as the only error — is deduced in five dimensions (supplement Proposition 10.3,
`wavegauge5.py` W8; constants not tracked): the energy of the harmonic-gauge perturbation at every later time and in the
bulk is bounded by its initial value and by the perturbation on a compact region [r_rs, R + r_h], with [Sch13]'s weights
at null infinity, where the five-dimensional radiation field's potential is coercive at every l ≥ 2 (its leading
eigenvalues are (l+a+1/2)(l+a+3/2) ≥ 3/4, so no Hardy inequality is needed where Hung's l = 2 needs one), and the
red-shift at r_h, where the identity acquires two terms absent in four dimensions, both absorbed. It is not a decay
statement: the compact region is where the master quantities and the gauge vector enter. The gauge vector's rungs are
done next (supplement Propositions 10.4–10.5, `rungs5.py`): each rung is a scalar wave equation with a potential, 0 or
the Maxwell potential −4μ/r⁴, and a source from the rungs below, and the one input of Hung, Keller and Wang's chain that
depends on the potential, the Morawetz multiplier, is computed for it — their own n = 3 choice serves both potentials,
with half the angular term lent to the bulk coefficient, which is then positive on the whole exterior by a Sturm count —
so every rung has the estimates of Hung's Appendix A in five dimensions for a source in the norm those estimates take.
The sources the rungs carry are not in that norm; Hung's substitutions that bring them into it — the first rung taken as
tr h, which solves the homogeneous wave equation, and the master field's bad terms removed by corrections carrying the
factor u + r — are computed in five dimensions term by term in his shape, every residual weight checked (supplement
section 10.7, `growing5.py`), and the identities of his l = 0 argument likewise (section 10.8, `lzero5.py`); of the two
estimates the route then owed, the rapid decay of the first rungs is deduced in five dimensions for every mode of the
class but the spherically symmetric one by Hung's own argument, with his conditions on the potential computed
(supplement section 10.9, `hierarchy5.py`), and found obstructed for the spherically symmetric mode, where the radiation
field carries a potential his argument needs to vanish; the coupled estimate for the last two components is carried into
five dimensions likewise (supplement section 10.10, `coupled5.py`), where its Morawetz bulk needs none of Hung's
substitutions for its positivity because the lowest mode of the class is already definite, so that every mode but the
spherically symmetric one decays by his route, deduced; and the spherically symmetric mode is taken by another route
(supplement section 10.11, `lzerorate5.py`): the same commutation, its negative potential absorbed by a Hardy inequality
on each outgoing null leaf for p < 1, with Schlue's Morawetz estimate at l = 0 [Sch13], gives the decay Hung's l = 0
argument needs at a rate one power weaker, so that the spherically symmetric part settles to a change of mass and a
stationary gauge mode, deduced: every mode of the class is carried.

No growing mode appears in either type for l = 2, …, 10 to τ = 275 r_h (settle5.py T5; a finite-time observation), and
the late-time tail of the l = 2 master fields, measured from the pulse's launch, is t^(−7.05) (tensor) and t^(−7.06)
(scalar) on [550, 700] r_h, the same at half the step, approaching 7 from above with that origin and bracketing 7 (6.89,
7.23) when the origin is shifted by the launch radius either way (T6): [CYDL03]'s t^(−(2l+D−2)) for odd D, the flat
five-dimensional Green's function's tail, which is the rate a nonlinear argument in the class would carry. The
least-damped mode of the class is the scalar-type one with l = 2, ω r_h = 0.9477 + 0.2561i ([CLY03b] Table 1, p. 8),
which evolving the master equation in time reproduces to 1% (settle5.py T3, on the barrier of
`docket68/lemmas/seed_escape.py`): an e-folding time of 3.905 r_h. The reduced problem in the class is 2+1-dimensional,
the dimension of Klainerman and Szeftel's polarized axisymmetric stability of four-dimensional Schwarzschild ([HKW18] p.
2); its five-dimensional counterpart is open.

### 8.3 Hintz's route: the five-dimensional inputs

The nonlinear route through Hintz's generalized wave map gauge [Hin26] needs a strongly damped constraint propagation
operator: mode stability, invertibility at zero energy on weighted spaces, no indicial root with real part in [−C₀, 1),
and its tf-admissibility ([Hin26] Theorem 7.1(4)). The indicial condition sees only the Minkowski model at infinity and
is computed in five dimensions (supplement section 10.12, `damping5.py`): Hintz's constraint damping [Hin26a], with the
trace weight 2/(D − 2) in place of his 1 — his 1 transcribed literally puts a root in (0, 1) — has, at a point below the
five-dimensional bound of his Lemma 4.4 with h < e chosen here (supplement section 10.13, `semiclass5.py`, which
recomputes the semiclassical inputs of his proof), no indicial root of the model with real part in [−100, 19/10], and in
[−100, 2] only the Coulomb root r^−2, exactly; the transfer to Tangherlini is deduced. A damping 1-form of his kind
exists on five-dimensional Tangherlini, explicitly, its conditions holding at that point by computation, two of them
near infinity, and its smoothing at the joins, by his arguments (supplement section 10.14, `cform5.py`). The gauge
potential operator, the other 1-form operator of the route, has on Tangherlini, unmodified (E^Υ = 0), the zero energy
structure of Hintz's Kerr case: its zero energy kernel is a single Coulomb-type state, a functional at the horizon
annihilates its range, and the pairings his horizon modification needs are 4π² where his are 4π (supplement section
10.15, `gaugepot5.py`; computed, the kernel deduced by an energy identity); and it has no mode at nonzero frequency in
the closed upper half plane — the input Hintz's Proposition 6.9 takes, on Kerr, from a separate theorem — by the master
equations of scalar waves and of both Maxwell types, whose potentials on Tangherlini are positive at every l ≥ 1, the
spherically symmetric Maxwell sector being settled by its own equation ([KI03b]; supplement section 10.16, `modes5.py`;
computed, the mode stability deduced for modes smooth across the horizon and outgoing at infinity). At high energies its
trapping input carries over: at the photon sphere r² = 2μ Hintz's frame has the same nilpotent connection along the null
flow, so the operator is strongly trapping admissible (supplement section 10.17, `trap5.py`; computed, the admissibility
deduced); and the horizon and outgoing thresholds [Hin26c]'s estimates need are his: the endomorphism at infinity has
his spectrum, and the horizon threshold is 3/2, also under the horizon modification of supplement section 10.15
(supplement section 10.18, `thresh5.py`; computed, the thresholds deduced). The remaining inputs follow — at the
incoming radial set the threshold is the mirror of the outgoing one, −1/2 − S̄ against −1/2 + S̄ (deduced from a
computed similarity), and at the photon sphere the gap is half the expansion rate per unit time and the semiclassical
loss as small as wished — so that, on the reading that [Hin26c]'s spectral theory — set up for scalar operators in
general dimension, its main theorems stated in three — carries over to operators on bundles in four, the operator's
spectral family is invertible at large frequency and, for small modifications, at every nonzero frequency in the closed
upper half plane: Hintz's Propositions 6.5 and 6.9 in five dimensions (supplement section 10.19, `hienergy5.py`;
computed, the threshold and the propositions deduced). The low-energy theory carries over in the same way, on a reading
widened to [Hin26c]'s zero energy and uniform low-energy theorems at n = 4 — the transition face is the Helmholtz
operator, whose outgoing solutions are excluded exactly for weights below n − 2 = 2, and the weights shift by n/2 — so
that, with the horizon modification of supplement section 10.15, the operator is mode stable on the whole closed upper
half plane: Hintz's Proposition 6.12 in five dimensions (supplement section 10.20, `lowenergy5.py`; computed, the
proposition deduced). Hintz's deduction of the constraint propagation operator's mode stability from his semiclassical
solvability theorem carries over as well — its endomorphism at infinity is his with three angular copies, all positive;
a mode's data lie in ρ^(−2−ε) for the volume r³, half an order below his; and the weights become α_sf = −C₀ − 5/2 and ℓ
∈ [−C₀ − 2, 0) — so that, his Theorem 5.2 granted in five dimensions, his Theorem 6.2 holds there — its zero energy part
at one parameter point, and given a horizon threshold not computed here — (supplement section 10.21, `cpmodes5.py`;
computed, the theorem deduced on his Theorem 5.2). The inputs of that theorem carry over too — Tangherlini is a
three-body scattering metric with two powers of decay to spare, the time functions of his energy estimates near the
initial surface and inside the black hole are timelike, and the positivity of the constraint damping 1-form holds at
these weights — so that it holds in five dimensions on the reading that his 3b-analysis does (supplement section 10.22,
`solv5.py`; computed, the theorem deduced). His transition face problem — the dilation-invariant model of the operator
on Minkowski space, his Theorem B.1 — carries over in the same way: the model is homogeneous of degree −2, its weights
at the origin move by a half to β ∈ (0, 2 + C₀], the thresholds at the cone face and at the sink, α_cf > 1/2 and α_sf <
−1/2 in his, become α_cf > 0.0066 and α_sf < −0.0066 at the parameter point (0 and 0 as e → 0), his choice of weights
and his closing argument go through unchanged, and his index-0 argument carries with the free operator's roots, so that
on the same readings, at that point, for C₀ ≤ 100 and provided the point's h lies below h₀, the constraint propagation
operator is tf-admissible for every weight in [−C₀, 2), [Hin26] Theorem 7.1(4) with its top at the Coulomb root 2 where
his is at 1 (supplement section 10.23, `tface5.py`; computed, the theorems deduced). The indicial roots of the
linearized gauge-fixed Einstein operator itself, his Lemma 8.4, carry over, at that point, for every harmonic degree l:
on each harmonic type its determinant is that of the gauge potential operator shifted by one and that of the constraint
propagation operator shifted by minus one, times the physical factor with roots −l and l + 2, his −l and l + 1, the mass
at the Coulomb root 2, over a factor at l ≤ 1 that removes the roots counted twice; no root has real part in (0, 1], so
that the gap begins at 0 as his does and reaches past 1; and the roots of each type, the tensor type included, which
four dimensions lacks, split evenly — so that his Lemma 8.5 holds, and his Proposition 8.6, tf-admissibility with a
weight in the gap for a small gauge parameter, on the same readings (supplement section 10.24, `lin5.py`; the
factorization computed for every l, the roots at the parameter point for l ≤ 12, the rest deduced). The one threshold
that it needs beyond them, the minimum of the endomorphism in his Lemma 8.2, is 0 in five dimensions as in four: that
endomorphism carries the gauge potential and constraint propagation operators' spectra and five zeros, so that the decay
improves to 3/2 − ε where his improves to 1 − ε (supplement section 10.25, `sbar5.py`; the spectrum computed, the
improvement deduced). And the operator is strongly trapping admissible at the photon sphere, his Proposition 8.3: its
subprincipal matrix there, 15 × 15 where his is 10 × 10 — his printed matrix recomputed exactly in four dimensions, with
his sign convention, as the control — has ten zero eigenvalues and five of one sign fixed by the damping 1-form being
past timelike, and is triangular in a fixed basis, the rotation of the angular plane along the flow absorbed by
weighting its pairs alike (supplement section 10.26, `strap5.py`; computed, the proposition deduced). Its spectral
family has no mode at nonzero frequency in the closed upper half plane, his Proposition 8.8: the one input he takes from
the mode stability of the linearized Einstein equations on Kerr is, on Tangherlini, the Kodama–Ishibashi reduction, here
computed from the linearized Ricci operator itself for every harmonic — each type at l ≥ 2 reduced to one master
equation whose potential is positive, the tensor type, which four dimensions lacks, with the scalar wave's, and l ≤ 1
pure gauge — so that every mode of the linearized Einstein operator smooth across the horizon and outgoing at infinity
is pure gauge (supplement section 10.27, `gmodes5.py`; computed, the proposition deduced on the same readings, the
kernel elements' class open; the continuation and the uniqueness inside the horizon by a lemma proved in supplement
section 10.76). And the zero energy states he builds from the
Minkowskian translations, boosts and rotations, with the linearized Kerr metrics put into his gauge, his Proposition
8.9, have five-dimensional counterparts one order faster in 1/r and without his two logarithms: Tangherlini meets
Minkowski at μ/r², the rotations are Killing, the rotating metrics — the derivatives at zero rotation of the
five-dimensional Myers–Perry family [ER08], checked — have their gauge source from the gauge modification alone, and the
exponents the constructions need, 1 and 2, miss the five-dimensional indicial roots once that modification is on
(supplement section 10.28, `zstates5.py`; the orders and exponents computed, the propositions deduced on the
five-dimensional form of his Lemma 6.13, itself deduced in supplement section 10.29 on the reading of [Hin26c]'s section
9 that is open below). There, too, the first three of his generalized zero energy states — on the time translation, on
the boosts carried to second order in time, and on the rotations — have five-dimensional counterparts with exact leading
terms: his rotation coefficients (1 ± γ/2)/4 become (1 ± 2γ/5)/4, each of the six rotations gives such a state, and the
time translation's state carries no logarithm (`genstates5.py`; the leading terms computed, his four-dimensional numbers
reproduced as the control, the lemma and the states deduced). And the four remaining classes — the pure gauge states
whose gauge potentials carry no symmetry, built on the gauge potential operator's growing roots — carry over with his
ranges, every stationary correction one order faster in 1/r and no logarithm in their leading terms once the gauge
modification is on (`puregauge5.py`; the leading terms computed exactly, his four-dimensional indicial matrices
reproduced entry by entry as the control, the proposition deduced in supplement section 10.30). The dual states of the
constraint propagation operator, whose symmetric gradients enter the cokernel of the linearized gauge-fixed operator in
his section 8.4, carry over too, on the readings supplement section 10.21 rests on: eleven in five dimensions against
his seven, the translations' one order faster in 1/r, and near zero rotation two of the six rotations' stay Killing at
first order, the other four carrying his (7.18) ratios (`dual5.py`; computed at first order in the rotation, his
four-dimensional values reproduced as the control, his Lemma 7.2 and Proposition 7.3 deduced in supplement section
10.31). At every spin his Lemma 7.5 is an identity of the Myers–Perry family: written in Kerr–Schild form for every spin
matrix A in so(4) at once, the deformation tensor of a rotation is the family's derivative along the bracket of the spin
with the rotation, so that, on readings (an SO(4)-equivariant family; supplement section 10.31(a)), his Proposition 7.4
holds with so(4) in place of R³, its leading term the same at every spin, the Killing rotations six, four at a = ±b ≠ 0
and two otherwise (`mp5.py`; computed exactly, Ricci-flatness at exact points, the rest deduced in supplement section
10.36). And the pairings that make his zero energy kernel and cokernel exact are boundary pairings at infinity -- at
zero rotation, -8π times the ADM mass and angular momentum and 4πM times the centre of mass, in five dimensions as in
four -- so the eleven kernel states and the eleven dual states are independent (`pairing5.py`; the pairings computed,
his four-dimensional table reproduced as the control, the rest deduced in supplement section 10.32). The rigidity his
count takes from Andersson, Häfner and Whiting [AHW24] — every decaying stationary linearised solution smooth across the
horizon a linearised Myers–Perry metric plus pure gauge — holds on five-dimensional Tangherlini: Kodama and Ishibashi's
decomposition at zero frequency reduces it to ordinary differential equations, whose energy identities leave nothing
smooth at the horizon and decaying for l ≥ 2, while l ≤ 1 gives the mass, the six rotations and pure gauge; so his count
holds there with eleven for seven, and near it on a reading (`static5.py`; computed harmonic by harmonic, the rest
deduced in supplement section 10.33). The physical states of his section 8.5 exist too: at Tangherlini, for every l ≥ 2
and each of the tensor, vector and scalar types, the static tidal solutions smooth at the horizon are Gauss functions of
r²/μ growing like r^l with coefficients that never vanish, and near it, on the same reading and on his Proposition 7.4
in five dimensions, his construction runs, one step modified, with his Lemma 8.15 carried over, so(4)'s bracket in place
of the cross product (`physical5.py`; computed, the rest deduced in supplement section 10.34). And five dimensions needs
only l = 2: if the slowest term at timelike infinity decays like t^(−α) with α in (1, 2] — t^−2 for the mass aspect's,
where four dimensions has t^−1, the Coulombic order separating from the radiative one above four dimensions, or t^(−3/2)
if the radiative order reached timelike infinity as Hintz's index sets would carry it — his window [−3, 0] shrinks to [α
− 4, 0] and the physical states needed are the scalar, vector and tensor ones at −2, without his generalized companions,
on readings (`window5.py`; computed, the rest deduced in supplement section 10.35). And, at the parameters used and on
readings, no pure resonance at timelike infinity decays as slowly as t^−2. In five dimensions, without Huygens'
principle, Hintz's model there has genuine pure resonant states, his own u₃ among them; the time integral of one is a
static solution, so that its exponent less one is a zero energy indicial root, or vanishes, and the state is then the
time derivative of one an order lower; with the injectivity half of his inversion below 1 + ε_ind carried over, every
pure resonance below 5/2 sits at a root of the constraint operator's zero energy operator in (2, 5/2), of the constraint
kind, the lowest at the spherical type a resonance where the computation reaches (`iota5.py`; computed, the rest deduced
in supplement section 10.37). Nor does the radiative order. Hintz's linearized operator at null infinity in five
dimensions — his (5.28) at the background, computed in his splitting, his printed matrix reproduced in four — has his
diagonal and his coupling of the 01-component into the 11-component, four trace couplings changed, while every coupling
through the metric perturbation falls half an order, so that the iteration's quadratic sources reach null infinity at
the Coulombic order, the mass aspect's; and a radiative term reaches timelike infinity at its own order only through a
resonant state there, which the same descent and injectivity exclude below 2. So α = 2 on readings, and the window is
[−2, 0] (`scri5.py`; computed, the rest deduced in supplement section 10.38). Nor, on readings, does the zero energy
augmentation need Hintz's improved states. In five dimensions the entries of his naive augmentation decay like r⁻³, one
order better than his r⁻² and inside the target space of his zero energy operator, and his own device for the angular
momenta — the states themselves, cut off to vanish near future null infinity — serves every state, the mass and the
boosts included, with no logarithm in time; so his zero energy operator, augmented by the eleven states, is invertible
by the same pairings, and his uniform low energy bounds and 2-admissibility hold on readings (`aug5.py`; computed on the
model, the rest deduced in supplement section 10.39). And, on readings, his proof of it loses no decay at spatial
infinity in five dimensions: the time derivatives that remove the poles at zero energy carry the states' own weights,
one order better than his, and with the augmentation cut off near future null infinity the threshold at the outgoing
radial set does not bind, so the two integrations in time keep the weights they start from; his loss of decay δ > α_sf +
3/2, α_sf the weight of his Theorem 10.1, becomes none (`lowfreq5.py`; computed on the model, the rest deduced in
supplement section 10.40). With it, his first step towards decay carries over: on readings, the dynamical operator is
admissible relative to the stationary one, the background's orders at timelike infinity one higher than his, and its
forward solutions lose there only the two orders the operator takes (`cone5.py`; computed on the model, the rest deduced
in supplement section 10.42). Several provisos of this section — the parameter point and the threshold h₀, the roots
beyond l = 12, the kernel elements' class and the uniqueness inside the horizon, and the readings of [Hin26c] and
[Hin26a] in five dimensions — are taken up in section 8.5.

### 8.4 Hintz's argument in the class

The class of section 2 is invariant under G = O(2) × O(2), acting on R⁴ = R² × R² by the rotations of the two planes and
the reflections x2 → −x2, x4 → −x4. Of the fifteen Killing fields of 4+1 Minkowski space only ∂_t is G-invariant, and a
G-invariant spin matrix in so(4) vanishes; so in the class Hintz's final parameters reduce to the mass, the boost and
rotation states of his construction are absent, and his Steps 2 and 5 reduce to his Propositions 11.20 and 11.51 at zero
boost (supplement section 10.43, `class5.py`: the invariant harmonics counted two ways, computed; the reduction
deduced). With that, his sections 11–13 carry into five dimensions in the class (supplement sections 10.44–10.49). At
null infinity the leading part of his normal operator is his with 3/2 for 1, its non-resonant gap at the parameter point
is (38/25, 499996.62) against his (51/50, 499996.12), and its exceptional exponents are 2 and 3/2 + (1 − e_Υ)γ_Υ for his
1 and 1 + (1 − e_Υ)γ_Υ (`iplus5.py`; computed, the exponent 2 resting on a scaling argument). The gauge parameter
changes his steps solve for vanish in the class, and his bookkeeping of the terms at the Kerr face, run over every
exponent at timelike infinity the class's sources carry — all at least α_min = 3/2 + (1 − e_Υ)γ_Υ = 1.5099 — records no
physical state: the class loses one order of decay at the Kerr face where he loses two, and the iteration needs its
forcing at order 3 + ε_K there (`sharp5.py`; computed, the bookkeeping deduced). His Theorems 12.3 and 12.8, the
exterior theorems of his section 5 with the radiative order 3/2 at null infinity, and his Theorem 13.1 follow: in the
class, G-invariant data near five-dimensional Tangherlini of mass m₀ that satisfy the constraints, have his decay and
are small have a G-invariant vacuum development, and it settles to Tangherlini of a nearby mass at the rate t*^(−2−ε_K)
in spatially compact sets (supplement section 10.49; deduced, on the readings of section 8.5).

### 8.5 The readings taken up

Sections 8.3–8.4 rest on two kinds of reading: that a computation at one parameter point serves Hintz's "for all
sufficiently small h", and that arguments written in 3+1 dimensions hold in 4+1. Each has been taken up (supplement
sections 10.52–10.59). Computed: every indicial root of the linearized gauge-fixed operator is simple at every harmonic
degree l ≥ 2, l = 0 and 1 being computed directly, and his distance condition (8.13) holds with ε_ind ≤ 1.94 × 10⁻⁸
(`eind5.py`; exact, with a 30-digit scan below l = 10⁴). The constraint damping holds at every h in (0, 10⁻⁶], not only
at the point: the indicial roots of the constraint propagation operator avoid [−100, 2] but for the simple Coulomb root
at l = 0 and 1, for every such h, by the point's line-crossing certificate with h as a second parameter (`uniform5.py`;
exact). Since Hintz's own threshold is not explicit — "there exists e₀ = e₀(v) in (0, 1) such that for all e in (0, e₀),
there exists h₀ > 0 such that for all h in (0, h₀)" ([Hin26a] Theorem 4.9, p. 37) — this removes the proviso that the
point lie below it: every other conclusion drawn at the point inherits from this, is free of h, improves as h falls, or,
like simplicity, fails at most on a countable set of h, and the horizon threshold holds for small h by the sign of the
damping. And the transfer from the Minkowski model is computed: five-dimensional Tangherlini is exactly η + (μ/r²) k ⊗ k
with k = dt + dr null, its connection two orders below Minkowski's, so that every operator of the route differs from its
model in ρ⁴ Diff_b against the model's ρ² Diff_b, one order better than four dimensions (`transfer5.py`; exact). READ at
source, with the substitutions they imply deduced: [Hin26c]'s section 9 is set in general dimension (its Definitions
9.3–9.4; its Theorem 9.38, Corollary 9.39 and Proposition 9.40 carry n), every three-dimensional numeral in it and in
its sections 5–13 comes from (5.7)'s (n − 1)/2 or from a density, and bundles are, in its words, "purely notational" (p.
158); [Hin26a]'s section 5.2 takes from the metric only symbol data, all computed here in five dimensions; [Hin23a]'s
exterior estimates are needed only near a piece of null infinity for compactly supported data, its radiation couplings
falling half an order at the five-dimensional radiative order r^(−3/2); [Hin26]'s Proposition 2.25 is stated on Rⁿ; and
[CD03]'s gluing is independent of the dimension. Deduced: the kernel elements' class; and the uniqueness inside the
horizon, with the continuation there that Hintz's mode stability argument needs, by a lemma on the radial systems'
simple zero at r_h proved in supplement section 10.76; the resonances at timelike infinity between 5/2 and
3 + ε_+, whose locations the bookkeeping of section 8.4 does not need; and the gluing of section 8.7.

### 8.6 Without the class

Settling needs only the class, where Theorem 1's solutions lie; perturbations with no symmetry are included as well.
Without the class Hintz's construction keeps his boost, his rotations and his centre-of-mass motions: the zero energy
nullspace is eleven-dimensional (the mass, the six rotations of so(4), the four translations), the four boosts add a
second-order pole at zero energy, and forward solutions lose two orders of decay at the Kerr face, as in four dimensions.
Three things are needed beyond section 8.4.

First, Hintz takes mode stability and the zero energy count at every Kerr parameter from [AHW24]. In five dimensions they
are deduced at every Myers–Perry parameter near Tangherlini by the perturbative route of [HHV21], which expects "the
linear stability of ... slowly rotating Myers–Perry black holes [MP86], to follow by similar arguments" (p. 14): the
high-energy conditions are strict at Tangherlini and persist; invertibility persists on compact sets of frequencies; and
at low energy the eleven zero energy states exist at every nearby parameter and exhaust the kernel by its upper
semicontinuity, after which Hintz's augmented operator gives invertibility near zero (supplement section 10.60; deduced).

Second, his bookkeeping at the Kerr face with two orders of loss, run over every harmonic type at every exponent at
timelike infinity the sources carry, eliminates six pure gauge classes, records fourteen, and records the physical states
of scalar, vector and tensor type at l = 2 — the tensor type the one kind four dimensions lack — with every recorded
term's image above the threshold (`general5.py` G1; computed, the steps deduced, supplement section 10.61). His Theorem
13.1 follows in five dimensions without the class: small data near Tangherlini with no symmetry have a vacuum development
that, its initial slice boosted by a small Lorentz boost, settles to a Myers–Perry metric of nearby mass and small spin
at the rate t*^(−2−ε_K) in spatially compact sets (supplement section 10.62; deduced).

Third, the gluing at large radius must match all fifteen Poincaré charges, which a translated, rotated and boosted
Myers–Perry metric supplies — in [CD03]'s words, "the only element missing is an equivalent of Proposition F.1 for the
family of translated, rotated, and boosted Myers-Perry metrics" (Remark 8.2, p. 36). Near Tangherlini it is computed:
the Jacobian of the charges in the mass, the four boosts, the six rotations and the four translations is diagonal —
energy 3πμ/8, angular momentum πμ/4 per unit rotation, momentum of size 3πμ/8 per unit boost velocity (P = −Ev, v the
velocity of the coordinate boost) and centre of mass 3πμ/8 per unit translation in energy-weighted form — with nonzero
determinant, so the charge map — polynomial in the parameters, the exact charges being E = 3πμ/8 and J = (πμ/4)A ([ER08]
(34)) — is a local diffeomorphism there and [CD03]'s gluing applies (`general5.py` G2; computed, the gluing deduced,
supplement section 10.63).


### 8.7 The solutions of Theorem 1 after the shell

After the shell, on {v > v_end}, every oscillating profile of the approximant vanishes — the waves are proportional to
the envelope, and the transports of Lemma 5.3 run along lines of constant v — so there g_λ is Tangherlini of mass μ_end
plus smooth means independent of λ times powers of λ (supplement section 10.50). The estimate of Theorem 1 holds at
every order of derivatives k ≥ 6 with K ≥ 6, its bootstrap closing whatever k is (supplement section 10.51), so the data
of g_λ on a τ-slice after the shell are small in every norm Hintz's theorem uses. Beyond Ω they are glued
G-equivariantly to exact Tangherlini by [CD03]'s method: its obstruction is the Killing initial data, of which the
G-invariant ones are ∂_t's alone, so only the mass is matched — on G-invariant data the charge of any other Killing
initial datum is that of its G-average, so no parity condition is needed — and the glued data are G-invariant by
uniqueness, as [CD03] obtains parity. The result is a compactly supported perturbation of Tangherlini — the case of
Hintz's Theorem 1.1 — and near spatial infinity its development is Tangherlini by finite speed of propagation
(supplement sections 10.50, 10.59; deduced). Without the class, the gluing is done on a slice Σ″ that is the τ-slice
near the hole and a static slice {t = const} of the exterior Tangherlini metric far out. On the τ-slice itself, where τ
= t − μ/r + O(r^(−3)), Tangherlini's second fundamental form is even and of order r^(−3), the borderline that [CD03]'s
parity condition (E.9) excludes. That condition is stated on the spacetime metric under x^μ → −x^μ, time included, so in
3 + 1 form it bounds the odd part of the spatial metric and the even part of the second fundamental form; its (8.1), as
printed, bounds the odd part of K, which boosted Kerr — a reference family on its p. 38 — would fail, and we read it
with the even part (supplement section 10.63(b)). On Σ″ the data of the glued development — g_λ's on Ω, exact
Tangherlini outside a compact set — are the base: the construction applies to every small perturbation of them whose
metric's odd part γ̃⁻ and second fundamental form's even part k̃⁺ satisfy |γ̃⁻| + r|∂γ̃⁻| + r|k̃⁺| ≤ C r^(−α₋) for some
α₋ > 2 — [CD03]'s (E.9) at n = 4 in 3 + 1 form, its (8.1) with k̃⁺ for K⁻ — which the G-invariance of the unperturbed
data does not supply: it removes the metric's odd part, not the even part of k. In five dimensions decay can replace the
condition: a perturbation with |γ̃| + r|∂γ̃| + r|k̃| ≤ C r^(−α) for some α > 3/2, of either parity, keeps every charge
convergent — the data being vacuum, as [CD03]'s theorem assumes — and every error of the gluing below its main term. In
four dimensions no admissible α does (`gluing5.py` D2; supplement section 10.66). The perturbed data are glued to a
translated, rotated and boosted Myers–Perry metric whose charges lie in a small ball about theirs (section 8.6;
supplement section 10.63).

### 8.8 Settling

**Theorem 4 (deduced).** Let g_λ be the solutions of Theorem 1, with A and the envelope fixed. There are λ1 > 0 and δ > 0
such that for λ ≤ λ1:

 (i) (in the class) the maximal vacuum development of the data of section 8.7, which contains g_λ on Ω, lies in the class
     and settles there to five-dimensional Tangherlini of a mass near μ_end: its difference from that metric is
     O(t*^(−2−ε_K)) in spatially compact subsets of the exterior;

 (ii) (without symmetry) every vacuum data set on the slice Σ″ of section 8.7 within δ of the glued development's data
      there, in the norms of supplement section 10.62(d), whose difference from them satisfies the parity condition of
      section 8.7 or decays faster than r^(−3/2), has a maximal vacuum development that, its initial slice boosted by a
      small Lorentz boost, settles at the same rate to a Myers–Perry black hole of mass near μ_end and small spin.

Theorem 4 is deduced, not proved. Two things separate it from proved. (i) The censuses. Every estimate of the companion
papers that the route uses has been read at source for where the dimension enters (supplement sections 10.53–10.58). The
proofs that were left as readings are carried to n = 4 by modification: [Hin26c]'s sections 7–8 and 9.3, [Hin26a]'s
section 5.2, [Hin23a]'s section 3, [CD03]'s gluing, Hintz's handling of the boost (his sections 3.4, 5.6 and 11–13) and
the two arguments of [HHV21] the route uses. For each, a census of the source in full text finds every place the
dimension enters, each is computed at n = 3 against the printed value and at n = 4, and the proof is run with the
computed quantity in place (supplement sections 10.64–10.68; `exterior5.py`, `gluing5.py`, `edge5.py`). The conjugated
wave operator at null infinity gains (3/4)r^(−2), which only strengthens Hintz's energy form. The gauge endomorphism
there has the diagonal 2γ_C, γ_C, (3/2)γ_C, −(3/2)γ_Υ, −γ_Υ, 0, −2γ_Υ, lower triangular, with the same least positive
entry, −γ_Υ, as in four dimensions. The quadratic radiation term and the metric-dependent entries fall by r^(−1/2), so
the coupling that four dimensions must track at leading order is an error term in five. The energy current at null
infinity keeps its threshold α_I < −1/2. The boost changes the data at r^(−2), inside Hintz's class, where in four
dimensions it changes them at the radiation order. [CD03]'s gluing needs its parity condition on the data only for decay
below r^(−3/2); its other uses of it fall on the Myers–Perry metrics glued to, which meet it. [Hin26a]'s calculus is
constructed in every dimension [Hin23d, Hin26d], and each positive commutator in its section 5.2 is an identity of
symbols whose sign is a positivity computed in five dimensions. A second census by another method agrees: a sweep of
every marker of the dimension on every page of the carried passages finds 278, all accounted for but one norm
convention, now named (supplement section 10.69; `censusweep.py`). What is not done is to re-derive those papers line by
line: that the censuses found every place the dimension enters is evidenced by the two methods agreeing and read at
source, page by page, not proved. (ii) The deductions of the supplement's sections 10.12–10.72 are arguments from
computed inputs, inputs READ at source, and readings — statements of the companion papers at n = 4 that the modification
steps carry, on which 34 of those steps rested until each was settled, written out or READ — each read by an independent
verifier, not proofs written out at the level of the theorem's statement. Inventoried by a fixed rule, the 248 deduced
steps are 90 pieces of bookkeeping on computed values, 29 applications of results printed for general n, 31 perturbation
or continuity arguments, 38 other, and 60 proofs written in 3 + 1 dimensions and carried to five by modification, 61
with one undecided step that supplement section 10.73 reads so. Those 61 are the core of what a line-by-line check would
write out (supplement sections 10.70 and 10.74, `DEDUCTIONS.tsv`, `B-MAP.tsv`). The perturbation steps are now at proof
level given their continuity inputs. They rest on five lemmas — openness of invertibility, semicontinuity of the kernel,
persistence of strict inequalities, Rouché and the inverse function theorem — of which the first three are proved in the
supplement and the last two are cited, and on continuity statements read from the sources (supplement section 10.71).
The applications of general-n results have every hypothesis placed, three of them now read at source (supplement section
10.72). The 38 others, read one by one, are twelve with no step of their own, 25 at proof level given their inputs —
among them steps by symmetry and sums over harmonics, put there by two lemmas proved in the supplement — and one more
modification step (supplement section 10.73; `synth5.py`). Each of the 61 modification steps lists the places where the
dimension changes its proof — 57 name some, 4 none, the proof being the source's as it stands — and each
five-dimensional value there is computed, deduced in an earlier section, arithmetic in n, or the record's choice
(supplement section 10.74, `B-MAP.tsv`). What they leave is that the source proofs use the dimension only at those
places, which is the census question of (i): by a rule the supplement deduces rather than proves, (ii) reduces to (i),
but for one step, which rests on a modification step and so on the census (supplement section 10.73). All 61 are now
written out step by step at n = 4 — forty-five with source proofs of at most about seven pages (two replaced by a
computation), sixteen on longer runs of proof, [Hin26] sections 11 and 12, [Hin26c] sections 5, 7–11 and 13 and [Hin26a]
section 5.2 — so their own steps rest on their inputs and not on a census, though thirty-four took a reading among those
inputs, a statement at n = 4 whose proof was not written out. Traced to their roots, the readings were ten statements,
and each is now settled, written out or READ: the record's own five, among them the damped operator's threshold at the
horizon, by computation, and what the rows use of the zero energy pole, by deduction; two groups of companion results,
written out at n = 4; one READ for general n; and two steps the source takes at every n without writing them out, on
which his own theorem in 3 + 1 dimensions rests too -- the passage from scalar operators to operators on bundles, which
he leaves to the reader, and the uniformity of the estimates under small perturbations, which he asserts -- both written
out site by site, the sites checked by a second census, and each proof of his spectral theory that the route uses re-run
on bundles with the changes in -- a re-run that found one sign slip in the source, in the commutator behind the
b-regularity at the outgoing radial set, repaired without change to the statement (supplement sections 10.75 and
10.77–10.86, `READINGS.tsv`, `hthresh5.py`, `tfnorm5.py`, `iotasol5.py`, `bundlesweep.py`, `bundle5.py`, with a lemma at
the horizon proved in section 10.76). λ1 and δ exist by the deduction — from Hintz's smallness constant and Theorem 1's
estimates — and are not evaluated; that is not a separate gap. A line-by-line check of those papers at n = 4, with the
deductions written out, would make Theorem 4 a theorem. That write-out has begun: the proof written in full at n = 4,
self-contained, part by part. Its first three parts -- Hintz's spectral theory at bounded nonzero, at high and at low
frequencies, on bundles and uniformly in the operator -- are written, read line by line, their repairs read again, and
proved (the second has since gained one lemma, at the trapped set, which a reader of the nineteenth asked for; it has
been read, and its smaller repairs read again). So are the fourth, the setup of his spacetime analysis, and the fifth,
which proves the two standard estimates that the fourth takes as inputs; one finding of the fourth corrects the
hypothesis of his real principal type estimate on the variable order, which as printed admits a counterexample. The
sixth, the dynamics of light rays in the stationary model, the seventh, the classes of operators, the time function and
the order functions of his spacetime analysis, and the eighth, the trapped sets of the perturbed metrics, proved here
without the theorem on normally hyperbolic trapping that he cites, have been read line by line and their findings seated
(supplement `proof5/`). The ninth, his microlocal regularity estimate on spacetime, with the radial estimates and the
estimate at the trapped set, which he quotes from his earlier paper and which is proved here in the present calculus,
the tenth, that estimate with b-regularity and in the tame form his iteration uses, and the eleventh, his energy
estimates on bounded time slabs and in the black hole interior, with the global estimate at high frequencies they give,
have been read line by line too and their findings seated. The twelfth, his analysis at future timelike infinity -- the
normal operator there, its spectral family at bounded and high frequencies, its forward solutions, and the forward
solutions of the stationary model on the spaces his iteration uses -- has been read line by line and its findings
seated. The thirteenth, the forward solutions of the perturbed wave operators with estimates tame in the regularity, and
the fourteenth, the Nash-Moser theorem with the smoothing operators and tame bounds it needs, proved here rather than
quoted, have been read line by line and their findings seated, and with the twelfth their repairs have been read again,
which proves the three. The fifteenth, the Fourier transform in time on the weighted spaces, his resolvent bounds
translated into them and the radiation field at null infinity, by which forward solutions are shown to decay faster, has
been read line by line, its findings seated and its repairs read again, which proves it.
The sixteenth, the first of the parts on his stability paper -- the five-dimensional black hole family on the
compactified spacetime, its time functions, initial data and boosts, and the gauge-fixed Einstein equation -- has been
read line by line, its findings seated and its repairs read again, which proves it. The seventeenth, the harmonics on
the three-sphere and the operators of Minkowski space in the splittings his stability paper uses, has been read line by
line and its findings seated. The eighteenth, the b-analysis and Fourier transforms with partial expansions on which
that paper's asymptotic analysis rests, and the nineteenth, the wave operator on the gauge potential near the
five-dimensional black hole -- its structure near infinity, its model, its indicial roots, its threshold and trapped
set, and its mode stability away from zero frequency, proved there by ordinary differential equations -- have been read
line by line, their findings seated and their repairs read again, which proves both; the second reading of the
eighteenth found one gap more, in the order of regularity of one lemma, closed and read again. In the eighteenth, one
step of his proof gives more logarithmic terms than he states, and the stated set is proved here another way; in the
nineteenth, the inner product at the trapped set depends on the direction of the ray, which the second part now allows
by the conjugation he uses, written out. The twentieth, the same operator at zero frequency: its kernel and cokernel on
the black hole, the modification at the horizon that removes them, and mode stability at every frequency, and the
twenty-first, the stationary gauge potentials that begin as the translations, boosts and rotations of Minkowski space,
have been read line by line, their findings seated and their repairs read again, which proves them. The twenty-second,
the gauge potentials polynomial in time that carry them, and the remaining roots, to higher order, the twenty-third, the
constraint propagation operator of his gauge at zero frequency and the stationary dual states built from the symmetries
of Minkowski space, eleven in five dimensions against his seven, the twenty-fourth, the dual states of the rotations,
whose leading term depends on a rotation only through its bracket with the spin -- in five dimensions an exact identity
of the black hole family, and the twenty-fifth, the linearised gauge-fixed Einstein operator near infinity and at the
trapped set, where in five dimensions the plane of directions orthogonal to the trapped rays turns along them, have been
read line by line and their findings seated; the twenty-fourth had none to repair, which proves it. The twenty-sixth,
the indicial roots of that operator and its invertibility where low frequencies meet spatial infinity, is written; there
the source's claim that all those roots are simple is shown to rest on properties of the constraint damping operator,
which the part on that operator must now supply. The twenty-seventh, the mode stability of the same
operator away from zero frequency, is written: at the black hole itself it is proved here, frequency by frequency and
harmonic by harmonic, from the master equations of Kodama and Ishibashi, where his proof cites a theorem on the
four-dimensional rotating black hole that has no five-dimensional counterpart; near it, it is proved for frequencies
bounded away from zero, and small frequencies away from the black hole itself are left to the parts on low frequencies.
The twenty-eighth, its kernel and cokernel at zero frequency, eleven-dimensional in five dimensions against his seven,
is written: at the black hole itself through the stationary solutions of the linearised Einstein equation there, which
are classified here harmonic by harmonic in place of the four-dimensional theorem he cites, and near it by perturbation
of an augmented operator, with no classification for the rotating black holes needed. The twenty-ninth, the pairings
that make that count exact and the large stationary states it needs, is written: the pairings he takes from earlier
papers are reduced here to integrals at infinity of leading terms, and the states, which in five dimensions include a
tensor type that four dimensions lacks, are built with one step of his construction changed. Theorem 4 stays deduced
until the last part is proved.

---

## 9. What is not proved

- **Settling as a theorem.** Theorem 4 is deduced: what separates it from a theorem is stated in section 8.8 — the
  completeness of the censuses that carry the companion papers' proofs to five dimensions, and of the census of the steps
  where Hintz's spectral theory uses scalar operators, each evidenced by two methods and not proved; and the deductions,
  written out step by step at proof level and read by independent verifiers, not proofs checked at the level of the
  theorem's statement. The readings thirty-four of the modification steps took are each settled, written out or READ. The
  other deductions are placed on their inputs, at proof level but for one named in section 8.8. λ1 and δ exist by the
  deduction and are not evaluated, which is not a separate gap. The linear statements of section 8.2 are deduced too, the
  route of Hung's sections 5–8 in five dimensions not a proof.
- **Physical wavelengths.** λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
  curvature length, does not apply at a wavelength of 10 l5 here (λ is the reduced wavelength of the phase v/λ, as in
  the numerics' usage). The expansion parameter is the wavelength over the curvature length L = K^(−1/4); on x_K = 1,
  L = l5, and at the horizon L = √μ/72^(1/4). For λ = 10 l5 the ratio is 10 on x_K = 1, and 2.91 (μ = 100 l5²) or 0.92
  (μ = 1000 l5²) at the horizon (computed, R7): there is no separation of scales. The statement that the waves are
  high-frequency on all of D once λ < l5/10 is about the approximant, not about λ0. Against the scale on which the
  curvature varies, r, the ratio is 1.00 and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (computed, R7). That is
  the parameter a construction from exact waves would see, in the manner of [AB26], whose layers are waves exact on a
  locally linear background, with amplitudes solving ordinary differential equations ("no sinusoidal identity was
  used", section 3.1); it is not small either, and there the wavelengths are chosen, here prescribed. At a prescribed
  wavelength without a small parameter, existence on D_T is a large-data question; a computed solution with a
  certified residual and a certified linear estimate could settle it (the rigorous numerics cited in [AB26] as [4]),
  and that is not attempted. Its first step was taken: the growth factor measured on the record's own computed
  solution at 10 l5 (`docket68/n1star/growth5.py`, supplement section 10.2). At both seeds that scheme's premise — one
  zero of the round spheres' expansion per column and the core boundary outflow, so that the exterior is fixed by its
  own data — fails before the shell's peak: a second zero holds over 0.04 in v from 1.50 r_h at μ = 100 l5² (1.496 on
  the finer grid, 1.476 with a shorter hold; a single-step excursion at 1.45 is not it) and from 1.583 r_h at 1000 l5²
  (three grids agreeing to 0.0005), and the boundary ceases to be outflow within 0.1 after; a deeper excision fails
  earlier, not later (r = 0.39 and 0.25 r_h at the first seed, 0.21 r_h at the second). So no approximant on D_T comes
  from that scheme at 10 l5 at any excision depth. What the computed solution shows is that round spheres inside the
  seed's horizon cease to be trapped and the boundary to be outflow, in the scheme's gauge, while the shell passes;
  the direction of the untrapping is not a measurement of these runs, and nothing is said of the event horizon. The
  step is re-posed as the characteristic initial value problem in double-null gauge — the incoming wave on an ingoing
  null hypersurface from past null infinity, the seed's outgoing cone as the other — where Luk's theorem gives local
  existence without smallness ([Wu26] Theorem 2.1) and [Wu26]'s Theorem 2.2, "the difference of metrics is controlled
  by the difference of curvature residues" (p. 6), is the a posteriori structure; its five-dimensional version in the
  class is not built. Up to the failure the radiation field's growth factor exp ∫K dv is 1.9 and 2.1, and a
  finite-difference amplification of the data along one direction, a lower bound for the propagator's norm, is 1.28
  and 1.00; where the scheme completes (λ = 0.1 r_h) they are 6.9 and 1.71, while the sup-norm Grönwall factor is 17,
  2 × 10⁵ and 6 × 10³: a certified argument would need the propagator's norm, not a sup-norm bound. The linear
  scattering of the shell off the seed at 10 l5 is computed in `docket68/lemmas/seed_escape.py`.
- **Beyond the boundary.** Theorems 1–3 are made on D_T and Ω, whose inner boundary r = a lies a fixed distance inside
  x_K = 1; beyond them only Theorem 4's deduced statement is made, outside the black hole.
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
  supplement), and seven minor ones, seated. Those repairs, this paper's Theorem 3 and the route of D46 were read by a
  fifteenth (D47): no blocking finding; nine repairs seated (among them a figure in section 10.2's repaired text that
  the stored samples do not support, 1.61 r_h, now 1.26; the route's first-order-pole label, now OPEN; its pre-W6
  wording; `bondi5.py`'s `--verbose` flag, which ran two checks alone) and seven notes. W7, `hung4.py`, those repairs
  and Proposition 10.3 with W8 were read by a sixteenth (D48): no blocking or major finding; one intermediate inequality
  in Proposition 10.3's proof carried a four-dimensional power and is repaired with the five-dimensional ones, the
  conclusion unchanged; the count of red-shift terms new in five dimensions is corrected from three to two, the
  four-dimensional identity now computed in `hung4.py` C3; three stale md5 rows, a decision count and four notes are
  repaired. Sections 10.6–10.42 of the supplement, with their programs, were read by the seventeenth to fifty-first
  verifiers, one or two sections at a time (D49–D109), each recomputing what it read by its own means. Three found major
  gaps: in section 10.6, the angular term spent twice at l = 2, a closing claim that the gauge vector decays at the
  rungs' rate, and an initial norm without the weighted data the proof uses (D49); in section 10.12, a certificate point
  above the bound on e that Hintz's construction needs, re-run inside it (D54); and in section 10.40, a mechanism
  misstated, the result standing with more room than stated (D105). Every finding was seated; the minor ones were mostly
  labels — computed where deduced, every parameter where one point — qualifiers and page numbers. Sections 10.43–10.57
  were read by the fifty-second to fifty-fifth (D111–D129): the fifty-second found that Hintz's Steps 2 and 5, called
  absent in the class, only lose their modifications (D115); the fifty-third, that the bookkeeping of section 8.4 had
  been stated for every exponent at timelike infinity, where the class's index sets were needed for it (D121); the
  fifty-fourth, that the argument of section 8.4 had been called complete while resting on the readings of section 8.5
  (D126); the fifty-fifth, that one use of the gauge parameter had been counted among lower bounds where it is a
  computation at two values (D129); each was repaired, with the minor findings. Sections 10.58–10.63 and this paper's
  Theorem 4 were read by the fifty-sixth (D133), which found the parity of the second fundamental form backwards in the
  gluing's parity condition — repaired with [CD03]'s condition in its spacetime form and a slice static far out, on
  which the unperturbed data meet it — with eight minor findings, seated; section 10.64 and those repairs were read by
  the fifty-seventh, which found the order of the metric-dependent entries of the gauge endomorphism at null infinity
  stated rather than computed — now computed, with the compactification, `exterior5.py` X7–X8 — and the base of the
  perturbed data in Theorem 4 (ii) left unnamed, with seven minor findings, all seated (D136); section 10.65 and those
  repairs were read by the fifty-eighth, which found one of Hintz's four printed entries matched only under an unstated
  reading — the reading now stated, the alternative value recorded — and the bounded-geometry calculus of [Hin26d] cited
  unread — now read at source, set on a manifold of any dimension — with six minor findings, all seated (D138); sections
  10.66–10.69 and the widening of Theorem 4 (ii) were read by the fifty-ninth, which found [CD03]'s other uses of its
  parity condition unlisted — they fall on the Myers–Perry metrics glued to, which meet it, and the charges' bulk term
  vanishes in vacuum — and the second census's [CD03] window one page late, its count now 278; its finding that the
  reading of [CD03]'s (8.1) rests on a false reason was checked and does not stand, (8.1)'s factor r having been
  dropped; with five minor findings, all seated (D143); sections 10.70–10.74 and those repairs were read by the
  sixtieth, which found Lemma 10.54's differentiated sum asking a second r-derivative its hypothesis did not give — the
  hypothesis widened and the weights for the two harmonic sums written out — and this paper's proof-status sentences
  stronger than the supplement's own accounting, now qualified, with six minor findings, all seated (D147); sections
  10.73–10.75 (i)–(xi) were read by the sixty-first, which found one step written out at n = 4 using the gauge 1-form's
  continuation inside the horizon, open in the supplement — now deduced at proof level from a lemma on the radial
  systems proved in supplement section 10.76 — two modification steps counted as naming no place and one reading
  unmarked, now placed and recounted,
  and this paper's account of the deductions' inputs silent on readings, now stated, with nine minor findings, all
  seated (D149); D148–D149, with sections 10.75 (xii)–(xvi) and 10.76, were read by the sixty-second, which found the
  lemma and its use sound and this record calling the continuation itself proved, now worded as the supplement has it,
  with twelve minor findings, all seated (D153); D150–D153, with sections 10.75 (xvii)–(xxxiv), were read by the
  sixty-third, which found no major fault and eleven minor ones — among them two misprints of the sources carried to n =
  4, a step of [Hin24b]'s proof left unnamed, and places the write-outs named that their rows lacked — all seated
  (D157).

---

## 10. References

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
  (Proposition 4.24). READ again 2026-10-22 (the twenty-eighth verifier's findings): pp. 157–159 (Notation 9.2, the
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
- [DLMF] *NIST Digital Library of Mathematical Functions*, https://dlmf.nist.gov/. READ 2026-10-24: §15.8 ((15.8.2), the
  connection formula at large argument, and (15.8.8), its case b − a = m a nonnegative integer, the dominant coefficient
  Γ(c)Γ(m)/(Γ(b) Γ(c − a)) for m ≥ 1, here m = l + 1) and §15.10 ((15.10.1), the exponent pairs {0, 1 − c}, {0, c − a −
  b}, {a, b} at 0, 1, ∞).
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
- [AB26] L. Alpöge, T. Buckmaster, *Blowup for the Boussinesq equations with smooth forcing*, preprint (September
  2026), cims.nyu.edu/~tristanb/boussinesq.pdf. READ 2026-10-20: section 1.2 (the layers and the wave), section 3.1
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
- `hthresh5.py` T1–T8: the damped operator's threshold at the horizon, [Hin26c] (5.17), at the record's point (supplement
  section 10.79): the normalisation r_h/2, the adjoint from the operators' definitions with the metric pairing as its
  control, the undamped part in Lemma 3.3's inner product with spectrum ±(e^(1/2) + e^(−1/2))/r_h, the damping's
  −h⁻¹ℓ(dr), and 1/2 + ϑ = −4995.33… at h = 10⁻⁶, below −100 for every h under 2.62 × 10⁻⁵; in other fibre inner products
  of the same family it can fail (positive at e′ = 10, crossing −100 at e′ ≈ 7.76), so it holds in the one the record
  fixes. 8/8; mutants 8/8 (about half a minute).
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
  by a certificate beyond l = 10⁴ and a 30-digit scan below, ε_ind ≤ 1.94137 × 10⁻⁸. 2/2; mutants 2/2 (about four
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
full, and its log `docket68/n1star/N1STAR-LOG.md` records each decision (D1–D135).

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
| Theorem 4 and what separates it from proved, section 8.8 | supplement sections 10.43–10.74; the route and its |
| | remaining reading, `docket68/n1star/ROUTES-OPEN.md` 4.44–4.69 |
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
| verification | supplement section 7: seven independent verifiers, one at a time (log D12, D15, D16, D18–D21); the |
| | eighth read this paper and the supplement's last restatement (log D26); the ninth sections 8.1–8.2 (D30); |
| | the tenth and eleventh Theorem 2's proof (D34–D35); the twelfth Theorem 3 (D40); the thirteenth |
| | the repairs of D40 and sections 10.2–10.3 (D44); the fourteenth D42–D44 (D45); the fifteenth the |
| | repairs of D45, Theorem 3 and the route of D46 (D47); the sixteenth W7, `hung4.py`, those repairs and |
| | Proposition 10.3 with W8 (D48); the seventeenth section 10.6 (D49); the eighteenth sections 10.7–10.8 |
| | (D50); the nineteenth section 10.9 (D51); the twentieth section 10.10 (D52); the twenty-first section |
| | 10.11 (D53); the twenty-second section 10.12 (D54); the twenty-third section 10.13 (D55); |
| | the twenty-fourth section 10.14 (D56); the twenty-fifth section 10.15 (D57); the twenty-sixth |
| | section 10.16 (D58); the twenty-seventh sections 10.17–10.18 (D59–D60); |
| | the twenty-eighth section 10.19 (D62); the twenty-ninth sections 10.20–10.21 (D64, D66); |
| | the thirtieth section 10.22 (D67, D70); the thirty-first section 10.23 (D69, D71); |
| | the thirty-second its repairs (D71, D72); the thirty-third section 10.24 (D72, D73); |
| | the thirty-fourth section 10.25 (D74, D76); the thirty-fifth section 10.26 (D75, D77); |
| | the thirty-sixth section 10.27 (D78, D79); the thirty-seventh section 10.28 (D80, D82); |
| | the thirty-eighth section 10.29 (D81, D83); the thirty-ninth section 10.30 (D84, D85); |
| | the fortieth section 10.31 (D86, D87); the forty-first section 10.32 (D88, D89); |
| | the forty-second section 10.33 (D90, D92); the forty-third section 10.34 (D91, D94); |
| | the forty-fourth section 10.35 (D93, D95); the forty-fifth section 10.36 (D96, D98); |
| | the forty-sixth section 10.37 (D97, D99); the forty-seventh section 10.38 (D100, D101); |
| | the forty-eighth section 10.39 (D102, D103); the forty-ninth section 10.40 (D104, D105); |
| | the fiftieth section 10.41 (D106, D107); the fifty-first section 10.42 (D108, D109); |
| | the fifty-second section 10.43 (D111, D115); the fifty-third sections 10.44–10.46 (D112–D114, D121); |
| | the fifty-fourth sections 10.47–10.52 (D116–D122, D126); the fifty-fifth sections 10.53–10.57 |
| | (D123–D126, D129); the fifty-sixth sections 10.58–10.63 and this paper (D127, D128, D130–D133) |
| | the fifty-seventh section 10.64 and the repairs of D133 (D134, D136); the fifty-eighth to |
| | sixty-second sections 10.65–10.76, 10.75 (xvii)–(lix) excepted (D138, D143, D147, D149, D153); |
| | the sixty-third 10.75 (xvii)–(xxxiv) (D157); the sixty-fourth 10.75 (xxxv)–(xliii) and D157's repairs |
| | (D162); the sixty-fifth 10.75 (xliv)–(lv) and D162 (D165); the sixty-sixth 10.75 (lvi)–(lix) and |
| | D165 (D168); the sixty-seventh 10.75 (lx)–(lxi) and D168 (D172); the sixty-eighth D169–D172 (D175); |
| | the sixty-ninth D173–D175 (D177); the seventieth D176–D177 (D179); the seventy-first D178–D179 (D180); |
| | the seventy-second D180–D181 (D182); the seventy-third D182–D183 (D184) |
| | the seventy-fourth Part I.A of the write-out (D186); the seventy-fifth its repairs (D187); |
| | the seventy-sixth Part I.B (D189) |
| | the seventy-seventh Part I.C and the Part I.B repairs (D191) |
| | the seventy-eighth Part II.A and the Part I.B and I.C repairs (D194) |
| | the seventy-ninth Part II.A′ and the D194 repairs (D195) |
| | the eightieth the D195 repairs (D196) |
| | the eighty-first Part II.B and the D196 repairs (D197) |
| | the eighty-second Part II.C (D200) |
| | the eighty-third Part II.C′ and the D200 repairs (D201) |
| | the eighty-fourth Part II.D (D204) |
| | the eighty-fifth Part II.D′ (D206) |
| | the eighty-sixth Part II.E (D207) |
| the standard theorems READ | supplement section 7, the retrieval table (log D17–D18) |

## Appendix D. Reproduction

Python 3 with sympy (3.13.16 and 1.14.0 in the runs recorded here); z3-solver for `foliation5.py`; numpy for `bondi5.py`
and `growth5.py`, numpy and scipy for `settle5.py`; mpmath for `damping5.py` and every program that imports it, and for
`lowenergy5.py`. `growth5.py` imports the solver `docket68/lemmas/hf_mirror5.py` and `hf_core5.y_core`, `past5.py`
imports `lead5.py`, `growing5.py`, `lzero5.py` and `coupled5.py` import `wavegauge5.py`, `lzerorate5.py` imports
`hierarchy5.py`, `semiclass5.py` imports `damping5.py`, `cform5.py` imports `semiclass5.py` and `damping5.py`,
`gaugepot5.py` imports `damping5.py`, `modes5.py` imports `gaugepot5.py` and `damping5.py`, `trap5.py` and `thresh5.py`
import `gaugepot5.py`, `damping5.py` and `modes5.py`, `hienergy5.py` imports `gaugepot5.py`, `damping5.py`, `thresh5.py`
and `trap5.py`, `lowenergy5.py` imports `thresh5.py` and `damping5.py`, `cpmodes5.py` imports `damping5.py`, `solv5.py`
imports `cform5.py` and `damping5.py`, `tface5.py` imports `cform5.py`, `gaugepot5.py`, `semiclass5.py` and
`damping5.py`, `lin5.py` imports `damping5.py` and `gaugepot5.py`, `sbar5.py`, `strap5.py`, `gmodes5.py` and
`zstates5.py` import `damping5.py`, `genstates5.py` imports `damping5.py` and `zstates5.py`, `puregauge5.py` imports
`damping5.py`, `genstates5.py` and `zstates5.py`, `dual5.py` imports `damping5.py`, `genstates5.py` and `puregauge5.py`,
`pairing5.py` imports `damping5.py`, `static5.py` imports `damping5.py` and `gmodes5.py`, `physical5.py` imports
`damping5.py` and `lin5.py`, `window5.py` imports `damping5.py` and `lin5.py`, `mp5.py` imports `damping5.py` and
`dual5.py`, `iota5.py` imports `damping5.py` and `lin5.py`, `scri5.py` imports `damping5.py`, `iota5.py`, `lin5.py` and
`sbar5.py`, `aug5.py` imports `damping5.py` and `sbar5.py`, `lowfreq5.py` imports `aug5.py`, `damping5.py` and
`sbar5.py`, `cone5.py`, `class5.py`, `eind5.py`, `uniform5.py` and `transfer5.py` import `damping5.py`, `iplus5.py`
imports `damping5.py`, `lin5.py`, `sbar5.py` and `scri5.py`, `sharp5.py` imports `class5.py`, `damping5.py`,
`iplus5.py` and `window5.py`, `general5.py` imports `damping5.py`, `sharp5.py`, `window5.py` and `iplus5.py`; the
others import nothing from the research tree:

    cd paper && python3 response5.py --selftest          # R1-R8, about 30 seconds
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
    python3 data5.py --mutants                           # about 80 minutes; each program has --mutants

The md5 of each file this paper rests on, at the commit that adds it:

| file | md5 |
| --- | --- |
| `paper/response5.py` | `1f62f6daff0ed15623cffd1c738b93df` |
| `docket68/n1star/N1STAR-PROOF.md` | `56e4e37ded37e80bf0b768cd69db6a34` |
| `docket68/n1star/N1STAR-LOG.md` | `e2dc1d2c3d67a0e548035ceaa8178692` |
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
| `docket68/lemmas/hf_theorem5.py` | `81e96f5af9eb31fc80669d582763d5be` |
| `docket68/lemmas/counterpart5.py` | `e7dcf7bf898c2147492d28c5fb888d18` |
| `docket68/lemmas/kn_gauge.py` | `7e9e9ef8ec12e670f1717ec4fe8bd491` |
| `docket68/lemmas/hf_core5.py` | `84b715eb461838abcb5e018cd455eb5c` |
| `docket68/lemmas/seed_escape.py` | `1a8b2ff82872e7096f13bf891a10424c` |
| `docket68/n1star/cpmodes5.py` | `4579a4605556992e5398c4d2abef2add` |
| `docket68/n1star/solv5.py` | `dfc11365958695d53d4dc98ccdd747bc` |
| `docket68/n1star/tface5.py` | `de9625072d570b423959da1af7654e41` |
| `docket68/n1star/lin5.py` | `b108caf5ebecc29dc61ce56d7f49af37` |
| `docket68/n1star/sbar5.py` | `a1899ea2f8470115ece25a400dc5fdc7` |
| `docket68/n1star/strap5.py` | `8d716c0c7dd36f8cd23987f1c79fec3d` |
| `docket68/n1star/gmodes5.py` | `5d2b68e8b13e2b921e08a733e0900031` |
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
| `docket68/n1star/B-MAP.tsv` | `9f27d6c25ade69aff81aa93ef814d6e9` |
| `docket68/n1star/proof5/PART-II-F-IOTA.md` | `58afe762b8bc571772529dd37ebae2cd` |

The paper's own md5 is recorded in the commit that adds it, not in itself.
