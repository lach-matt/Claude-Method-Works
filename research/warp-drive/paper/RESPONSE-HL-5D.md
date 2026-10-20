# High-frequency vacuum limits on a five-dimensional black hole: a response to Huneau and Luk

**Title proposed**, not settled: titles are the author's.

**Matthew Lach** · Independent Researcher · 20 October 2026

*Status: draft for the author's review, not released. Whether and where it is released is the author's decision.*

Labels used throughout: **computed** (an exact identity checked by a program named in Appendix A, with a negative
control the program must reject), **deduced** (an argument written out here or in the supplement, a standard theorem
being invoked only after its statement was read at source and its hypotheses checked), **READ** (quoted verbatim at
source, with identifier and page). "Proved" means proved in this sense, and nothing else.

---

## Abstract

Huneau and Luk proved that every generic, small-data, polarized U(1)-symmetric solution of the Einstein–null dust
system is a weak limit of vacuum solutions on a fixed time interval, in an elliptic gauge in which smallness is needed
even for local existence. We prove a five-dimensional counterpart on a large background. In the class of
five-dimensional vacuum metrics with a T² isometry and both reflections, the Einstein equations reduce exactly to
2+1 gravity coupled to two free waves whose target metric, (3/2) dψ² + 2 dω², is flat and positive definite; this is
Huneau and Luk's reduced system with one scalar replaced by two. The background is five-dimensional Vaidya, a black
hole of mass μ0 that grows by an ingoing shell, and the domain runs from before the shell reaches the hole to a
spacelike surface of fixed curvature inside the horizon. For every amplitude A > 0 and every smooth compactly
supported envelope, with no smallness of either, we construct a family of T²-symmetric vacuum metrics g_λ on that
domain, of wavelength λ ≤ λ0, with |g_λ − g0| ≤ Cλ, ∂g_λ bounded, and ∂g_λ → ∂g0 weakly but not strongly, where g0
is Vaidya with dμ/dv = (2/9) A² env²: Isaacson's flux, the null dust of one family. The proof uses the wave-map gauge
relative to the limit itself and an approximate solution of arbitrarily high order, so that every nonlinear term is
beaten by a power of λ rather than by the size of the data; what must be uniform in λ is then a linear estimate on the
black-hole background, and its one large coefficient is removed by a phase-shift identity. The Cauchy data are
constructed by solving the constraints outward in r as a parabolic–hyperbolic system from a sphere inside the shell.
We list what is not proved: settling at late times, the data at past null infinity, the rates beyond O(λ), and the
application at physical wavelengths.

---

## 1. Introduction

### 1.1 Burnett's problem

Huneau and Luk state the problem as follows (READ, [HL18] p. 1): "On a fixed manifold, consider a one-parameter family
of Lorentzian metrics g λ for λ ∈ (0, λ 0 ], λ 0 ∈ R which satisfies the Einstein vacuum equations R μν (g λ ) = 0.
(1.1) Assume moreover that there exists a metric g 0 such that as λ → 0, • g λ converges to g 0 uniformly on compact
sets; and • the derivatives of g λ converges weakly in L 2 to the derivatives of g 0 . Due to the nonlinearity of the
equations, it can happen that the limiting metric g 0 is a solution to the Einstein equations which is not vacuum".
Burnett's own assumptions, as Luk and Rodnianski print them (READ, [LR20] p. 3, their (1.3)): "|g n − g ∞ | ≤ λ n ,
|∂g n | ≤ C, |∂ 2 g n | ≤ Cλ −1 n". The direct question asks which limits occur; the reverse asks whether a given
Einstein–matter solution is such a limit.

### 1.2 The theorem answered

Huneau and Luk work with metrics (READ, [HL18] p. 3) "(4) g = e −2φ g + e 2φ (dx 3 ) 2", for which "Einstein vacuum
equations R( (4) g) μν = 0 are equivalent to the following system for (g, φ): { g φ = 0, R μν (g) = 2∂ μ φ∂ ν φ. (1.3)".
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
from Minkowski: a black hole growing by an ingoing shell, on a fixed domain that reaches inside the horizon to a
spacelike surface of fixed curvature (Theorem 1, section 3). It is an instance of Problem 8.6 in a five-dimensional
symmetry class, not an answer to Problem 8.6 as posed, which concerns four dimensions.

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
the proof therefore never uses the reduced system and works in five-dimensional Cartesian coordinates, in which the
axes are regular points. Five-dimensional Vaidya is the simplest large solution of the limiting system: its mass grows
by exactly the averaged energy of the waves, and it carries a horizon. The domain ends where the curvature reaches a
fixed scale l5, x_K := l5² √K = 1 with K the Kretschmann scalar; that surface lies inside the horizon and is spacelike
(section 6), so the domain is the domain of dependence of its data and nothing inside it is excised. The theorem says
nothing about what lies beyond that surface, and nothing in it involves an inner or Cauchy horizon.

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

With ψ̃ := (√3/2) ψ, (2.2) reads Ric[h] = 2 (dψ̃² + dω²), □_h ψ̃ = □_h ω = 0: Huneau and Luk's (1.3) with the
scalar φ replaced by the pair (ψ̃, ω), whose target is the flat Euclidean plane. The check evaluates every identity
from the exact 2-jets of explicit generic g3, A, B at three rational points (50 digits); replacing 3/2 by 1 fails. The
same reduction is computed independently, in other variables, by `docket68/lemmas/kn_gauge.py` (K1–K2).

### 2.2 The background

Coordinates X = (τ, x) ∈ R × R⁴, r = |x|, x̂ = x/r, v := τ + r. The T² action rotates the planes (x1, x2) and
(x3, x4); its axes are regular points of R⁴. Let

    g0 := η + (μ(v)/r²) dv²,     g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0,     L0 := ∂_τ − x̂·∂_x,     det g0 = −1,       (2.3)

with μ smooth, nondecreasing, μ = μ0 > 0 for v ≤ v_start and constant for v ≥ v_end.

**Proposition 2.2 (computed: `paper/response5.py` R2–R4; `docket68/n1star/ks5.py` K1–K5).**
(a) g0 is five-dimensional Vaidya: Ric(g0) = (3 μ'(v)/(2 r³)) dv ⊗ dv, and its (τ, r) block has determinant −1.
(b) For constant μ the Kretschmann scalar is K = 72 μ²/r⁸; the round spheres have one apparent horizon, r = √μ.
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

∇̂ the connection of g0 and Q quadratic in ∂g with coefficients rational in g and smooth in X on r > 0 (READ: [CBCM10]
(2.7)–(2.9), p. 8, in n + 1 dimensions, formulae transcribed: "R_(α β) = R^(H)_(α β) + 1/2 (g_(α λ) D̂_β H^λ + g_(β λ)
D̂_α H^λ)", "R^(H)_(α β) = −1/2 g^(λ μ) D̂_λ D̂_μ g_(α β) + f̂[g, D̂ g]_(α β)", f̂ "independent of the second
derivatives of g"). D and Ric^H are built from g and g0 alone, so they are invariant under the isometries of g0, which
include T² and both reflections. Ric^H(g) = 0 is a quasilinear wave system, D(g0) = 0, Ric^H(g0) = Ric(g0), and a
solution with D = 0 is vacuum.

---

## 3. The theorem

**Theorem 1 (the five-dimensional counterpart).** Let l5 > 0, μ0 ≥ √72 l5², A > 0 and env ∈ C_c^∞([v_start, v_end]),
and let g0 be the Vaidya metric (2.3) with μ(v) = μ0 + (2/9) A² ∫_(−∞)^v env². Fix T > 0, τ0 with
v_start − τ0 > √μ0 + 1, and K ≥ 6. There are λ0 > 0 and C, depending on (l5, μ0, A, env, T, τ0, K) and not on λ, such
that for every λ ∈ (0, λ0] there is a smooth Lorentzian metric g_λ on Ω ⊃ D_T ∩ {τ ≥ τ0} with:

1. **Vacuum and symmetry.** Ric(g_λ) = 0 on Ω, and g_λ is invariant under the T² action and both reflections.
2. **Data.** On Σ_τ0, the Cauchy data of g_λ satisfy the vacuum constraints exactly, equal the data of the seed
   (five-dimensional Schwarzschild–Tangherlini of mass μ0) on r < v_start − τ0, and differ from those of an explicit
   approximate solution g_app by O(λ^K) in the λ-scaled norm (E4) of the supplement; the leading oscillation of g_app
   is the waves of section 2.4.
3. **The remainder.** g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω, where
   g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j] with smooth profiles g_j(X, θ), 2π-periodic in θ, evaluated at θ = v/λ.
4. **Convergence.** |g_λ − g0| ≤ C λ and |∂g_λ| ≤ C on Ω; ∂g_λ − ∂g0 = dv ⊗ [∂_θ g1] + O(λ), so ∂g_λ → ∂g0 weakly
   in L²(Ω), and not strongly wherever env ≠ 0. The limit g0 satisfies Ric(g0) = (3 μ'/(2 r³)) dv ⊗ dv with (2.6): it
   is not vacuum but Einstein–null dust with one family.
5. **Gauge and uniqueness.** D(g_λ) = 0 on Ω, and g_λ is the only solution of Ric^H(g) = 0 on Ω with its data.

The constants that the argument fixes explicitly: the order of the energy is k = 6 (any k with k + 1 derivatives
available would do), the approximant used has N = K + 3 stages, λ ≤ λ1 := min(1, δ0)/10 where δ0 := r_q(μ0) − a, and
the data are solved in H^s(S³) with s > 3/2 + 4. λ0 and C are not evaluated. Every constant of the approximant's own
estimates is λ-independent (computed: `docket68/lemmas/counterpart5.py` P1), and the waves are high-frequency on all
of D once λ < l5/10 (same check).

**Proposition 3.2 (the boundary; computed R6, deduced).** On x_K = 1, with Φ := r − r_q(v),

    g0⁻¹(dΦ, dΦ) = 1 − √(μ/(√72 l5²)) − r_q μ'/(2 μ),                                                     (3.1)

so the boundary is spacelike for g0 wherever μ > √72 l5² or μ' > 0, and every future causal curve that meets it
leaves D_T there and does not return. If μ0 > √72 l5² the margin is uniform, g0⁻¹(dΦ, dΦ) ≤ −δ with
δ := √(μ0/(√72 l5²)) − 1 > 0, and the same holds for g_λ when λ ≤ λ0 (deduced: |g_λ⁻¹ − g0⁻¹| ≤ C λ on Ω by item 4,
and the cone of future causal covectors moves continuously). If μ0 = √72 l5² exactly, the boundary coincides with the
seed's horizon for v ≤ v_start and is null there.

*How Theorem 1 follows.* It is the conjunction of three theorems proved in the supplement and summarized in sections 4
and 5: Theorem A (the approximant to any order), Theorem D (exact data within O(λ^K) of it) and Theorem E (existence on
Ω with λ-uniform remainder estimates). D(g_λ) solves a homogeneous linear wave system by the contracted Bianchi
identity and vanishes with its first derivative on Σ_τ0 (the gauge condition and the constraints), so D = 0 on Ω and
g_λ is vacuum (deduced; the identity READ in [LR05] p. 1 and, in n + 1 dimensions, [CBCL06] section 3: "the
harmonicity functions F^μ := □_g x^μ satisfy an homogeneous linear system of wave equations on (V, g), with also
∂_t F^μ = 0, hence F^μ = 0 if (V, g) is globally hyperbolic"). The symmetry follows from uniqueness, since Ric^H and D
are built from g and the O(4)-invariant g0 alone and the data are invariant.

---

## 4. The approximant

**Phase and profiles.** The phase is v, an exact eikonal of g0 (Proposition 2.2(c)). A profile is a smooth
f(X, θ) on Ω × S¹; [f](X) := f(X, v(X)/λ); ⟨f⟩ is its θ-mean. Derivatives are measured in the λ-scaled norm
|f|_j := Σ_(i≤j) λ^i ‖∂^i f‖_(L²(Σ_τ)), in which an oscillation costs nothing: ∂_a [f] = λ⁻¹ (∂_a v)[∂_θ f] + [∂_a f].
For a profile G the two-scale operator R[G] is Ric^H with ∂_a replaced by ∂_a + λ⁻¹ (∂_a v) ∂_θ; it contains no
explicit θ, so

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
functions on it, with the Bernstein- and Friedrichs-type bounds ‖∂_x P f‖ ≤ C λ⁻¹ ‖f‖, ‖f − P f‖ ≤ C λ ‖∂_x f‖ and
‖[a, P] ∂_x f‖ ≤ C ‖∂_x a‖_∞ ‖f‖ (supplement Lemma 2.2). It replaces Touati's Fourier projector Π≤ ("a Fourier
multiplier supported in { |ξ| ≤ 1/λ }", READ, [Tou23a] section 3.2.3, p. 20), which needs no boundary.

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
g_λ, λ ≤ λ0, when μ0 > √72 l5²; every characteristic leaves the domain through it. Exact for g0 (computed R6, and
`docket68/lemmas/hf_theorem5.py` F2, there also machine-checked with Z3); deduced for g_λ.

**(iii) The horizon.** For the limit, the outgoing expansion of the round spheres on each ingoing cone has exactly one
zero, at r = √μ: one apparent horizon and no inner one (computed, exact; hf_theorem5.py F1). For g_λ, λ > 0, the
expansion involves ∂g_λ, which converges only weakly, so item 4 of Theorem 1 does not decide it; one zero per column
and convergence of the horizon at O(λ) are computed numerically at two seeds (μ0/l5² = 100 and 1000) by a
Bondi-type solver (`docket68/lemmas/hf_core5.py`; hf_theorem5.py F4: the horizon's departure halves with λ, ratios
2.47, 2.26, 2.14 and 2.46, 2.26), and **not proved**.

---

## 7. Relation to Huneau and Luk, Touati, and Luk and Rodnianski

Point by point; HL is [HL18], T is [Tou23a], LR is [LR20], and "here" is this paper.

- **Dimension and symmetry.** HL: 3+1, polarized U(1), a translation with no axis. T: 3+1, none. LR: 3+1, none.
  Here: 4+1, T² with both reflections, rotations with two axes.
- **Reduced system.** HL: 2+1 gravity with one free wave φ, their (1.3). T, LR: none. Here: 2+1 gravity with two
  free waves on the target (3/2) dψ² + 2 dω² (Proposition 2.1), identified but not used near the axes.
- **Gauge.** HL: elliptic (maximal slices, conformally flat). T: generalised wave. LR: double null. Here: the
  wave-map gauge relative to the limit g0.
- **Background.** HL: small, near Minkowski (the smallness condition of Theorem 4.2). T: small, (2.9), with an
  asymptotically planar phase, (2.10). LR: large and angularly regular, on a local double null domain. Here:
  five-dimensional Vaidya with a black hole; no smallness of μ0, A or env.
- **Dusts.** HL: any finite number, angularly separated, with generic data. T: one. LR: two, measure-valued.
  Here: one.
- **Data.** HL: admissible free data on a maximal slice. T: the conformal method of [Tou23b]. LR: characteristic.
  Here: Cauchy data on Σ_τ0, the constraints solved outward in r.
- **Domain.** HL: [0, 1] × R². T: [0, 1] × R³. LR: [0, u*] × [0, u̲*] × S². Here: Ω ⊃ D_T ∩ {τ ≥ τ0}, through the
  horizon to a spacelike boundary.
- **What closes the estimates.** HL and T: the smallness ε. LR: angular regularity. Here: powers of λ, with the
  approximant carried to any order.
- **The derivative loss.** HL: elliptic estimates for the metric. T: a null foliation and a Fourier cut-off. LR:
  angular regularity. Here: the phase-shift identity, the exact commutator (2.4) and a compact mollifier.
- **Conclusion.** HL: uniform convergence, weak L² convergence of derivatives, ∂ in L∞ uniformly. T:
  g_λ = g0 + λ g(1) + … in generalised wave gauge. LR: C⁰ and weak W^(1,2). Here: uniform at O(λ), ∂g bounded,
  weak L².

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

- **Settling at late times.** The theorem holds on D_T for each fixed T. Settling for all later v is the nonlinear
  stability of five-dimensional Schwarzschild–Tangherlini in the class, which is open and is not attempted. Huneau and
  Luk's theorem, Touati's and Luk and Rodnianski's hold on a fixed interval too.
- **The data at past null infinity.** The theorem is posed with Cauchy data on Σ_τ0, before the shell reaches the hole.
  The evolution from data at past null infinity down to Σ_τ0, and the equivalence of the two descriptions of the waves,
  are not proved; the data here carry the waves of section 2.4 at leading order and are otherwise constructed.
- **Rates beyond O(λ), and part (iii) for λ > 0.** The mean mass converging at O(λ²), one apparent horizon per column
  for g_λ and the horizon converging at O(λ) are computed numerically (section 6) and not proved.
- **Physical wavelengths.** λ0 is not evaluated. Whether the wavelengths of an intended application lie below it is
  not decided; the computed statement that the waves are high-frequency on all of D once λ < l5/10 is a statement
  about the approximant, not about λ0.
- **Beyond the boundary.** Nothing is claimed beyond x_K = 1.
- **More families.** Several dusts, angular separation, and the passage to Vlasov matter are not attempted.
- **The boundary at equality.** If μ0 = √72 l5² exactly, x_K = 1 is null on the seed's portion (Proposition 3.2).
- **Review.** The last restatement in the supplement (a clause of its Lemma 6.4 restated in the integral form its proof
  gives, and three notes) had not been read by an independent verifier when this draft was written.

---

## 9. References

Each was READ at source for this paper or for the proof, on the date and at the page given; quotations are verbatim
from the arXiv text, with the extraction's spacing.

- [HL18] C. Huneau, J. Luk, *High-frequency backreaction for the Einstein equations under polarized U(1)-symmetry*,
  Duke Math. J. 167(18) (2018) 3315–3402, arXiv:1706.09501v1. READ 2026-10-20: p. 1 (Burnett's formulation), p. 3
  ((1.3), (1.4), Theorem 1.1), pp. 8–10 (Definition 3.2, Theorem 3.3, Corollary 3.5, Definition 4.1, Theorem 4.2).
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
  arXiv:2009.08968v1. READ 2026-10-20: p. 1 (abstract), p. 3 ((1.3), Conjectures 1.2–1.3), p. 5 (Theorems 1.9–1.10).
- [CBCM10] Y. Choquet-Bruhat, P. T. Chruściel, J. M. Martín-García, arXiv:1006.4467. READ 2026-10-20: (2.7)–(2.9), p. 8.
- [CBCL06] Y. Choquet-Bruhat, P. T. Chruściel, J. Loizelet, arXiv:gr-qc/0608108v2. READ 2026-10-20: (3.1), sections 3
  and 5.1.
- [LR05] H. Lindblad, I. Rodnianski, arXiv:math/0411109v2. READ 2026-10-19: p. 1, (1.3) p. 2, section 2.2 p. 8.
- [CD03] P. T. Chruściel, E. Delay, *On mapping properties of the general relativistic constraints operator in
  weighted function spaces, with applications*, arXiv:gr-qc/0301073v2. READ 2026-10-20: (2.1)–(2.2), p. 4.
- [Rac16] I. Rácz, *Constraints as evolutionary systems*, Class. Quantum Grav. 33 (2016) 015014, arXiv:1508.01810v3.
  READ 2026-10-19: (3.3), p. 6.
- [DS23] M. M. Disconzi, Y. Shao, *Strongly hyperbolic quasilinear systems revisited*, arXiv:2308.09851v1. READ
  2026-10-20: (A1)–(A4), Theorems 2.4, 2.6, Remark 2.3.
- [AO14] L. Andersson, T. A. Oliynyk, *A transmission problem for quasi-linear wave equations*, arXiv:1401.0277v1.
  READ 2026-10-20: Theorem 1.1, (1.3), Remark 1.2, section 4.1.
- [BH17] A. Behzadan, M. Holst, *Multiplication in Sobolev spaces, revisited*, arXiv:1704.07930. READ 2026-10-20:
  Theorems 7.21, 7.26, 9.14.
- [GO13] L. Grafakos, S. Oh, *The Kato–Ponce inequality*, arXiv:1303.5144. READ 2026-10-20: p. 1.
- [LY22] H. Lu, L. Yao, *On Seeley-type universal extension operators for the upper half space*, arXiv:2211.15567v2.
  READ 2026-10-20: Theorems 1, 26, Lemma 27.
- [SY21] Z. Shi, L. Yao, arXiv:2110.14477v4. READ 2026-10-20: sections 1, 2.1 (Rychkov's and Stein's operators).
- [AG22] F. Angeles, *The Cauchy problem for a quasilinear system of equations with coupling in the linearization*,
  arXiv:2204.01179v3. READ 2026-10-20: abstract, p. 1; (9.6)–(9.7), p. 24.
- Burnett (1989), Isaacson (1968) and Choquet-Bruhat (1969) are cited through [HL18] p. 1, [HL24] pp. 1, 32 and
  [LR20] p. 3, where they are quoted; their originals were not re-READ for this paper.

---

## Appendix A. The computations

Every computation is exact unless marked; each program carries a self-test whose negative controls it must reject.
Paths are relative to the root of the research tree.

`paper/response5.py`, written for this paper, re-derives its own numbers independently of the proof's programs:

- R1: the reduction, Proposition 2.1, from the 2-jets at three rational points (50 digits). Control: 3/2 → 1.
- R2: Ric(g0) = (3μ'/(2r³)) dv dv, and the τr-block has determinant −1. Control: μ/r in place of μ/r².
- R3: K = 72μ²/r⁸; x_K = 1 at r_q; r_q ≤ √μ iff μ ≥ √72 l5². Control: 48 in place of 72.
- R4: ℓ null and geodesic; the contractions of Proposition 2.2(d). Control: dv − 2 dr is not null.
- R5: (5.6): ρ parabolic in a, J symmetric hyperbolic in (w, q), S, the speeds, θ³H. Control: a γ in place of
  a dr² brings ∂_r² a into ρ.
- R6: h²(c⁴ + s⁴) = 1; 4(a² + ab + b²) = (2a + b)² + 3b²; (3.1). Controls: h = 1, and r + r_q in place of r − r_q.

All six pass and every control is rejected (about 20 seconds). The proof's programs, in `docket68/n1star/`:

- `ks5.py` K1–K5: the Kerr–Schild form, its inverse, the commutator (2.4), div L0, the gauge source H0. 5/5;
  mutants 4/4.
- `foliation5.py` B1–B4: the null foliation, the slices and the domain. 4/4; mutants 5/5.
- `ansatz5.py` A1–A5: the ansatz to order λ² on Vaidya with phase v. 5/5; mutants 5/5.
- `lead5.py` L1–L5: stage 0: R^(−1) = 0, the energy condition, χ. 5/5; mutants 4/4.
- `data5.py` S0–S6: the slice data, the constraints' principal part, no coefficient of order λ⁻¹. 7/7; mutants 6/6.

Earlier programs cited, in `docket68/lemmas/`:

- `hf_theorem5.py` F1–F5: the horizon of the limit, (iv) with Z3, the dust (Wolfram Language, Lean 4), the
  numerical rates. 7/7.
- `counterpart5.py` P1: K = 72μ²/r⁸ and the λ-independent constants of the approximant. 8/8.
- `kn_gauge.py` K1–K2: the reduction in other variables. 18/18.
- `hf_core5.py`: the numerical sequence at two seeds (rates; one zero per column). 10/10; numerical, not exact.

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
full, and its log `docket68/n1star/N1STAR-LOG.md` records each decision (D1–D22).

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
| part (iii) | `docket68/lemmas/hf_theorem5.py` F1 (limit), F4 and `hf_core5.py` (numerical, not proved) |
| verification | supplement section 7: seven independent verifiers, one at a time (log D12, D15, D16, D18–D21) |
| the standard theorems READ | supplement section 7, the retrieval table (log D17–D18) |

## Appendix D. Reproduction

Python 3.11 with sympy (the programs import nothing from the research tree):

    cd paper && python3 response5.py --selftest          # R1-R6, about 20 seconds
    python3 response5.py --selftest --full               # and the five proof programs, about 20 minutes
    cd ../docket68/n1star && python3 ks5.py --selftest   # and likewise foliation5, ansatz5, lead5, data5
    python3 data5.py --mutants                           # about 80 minutes; each program has --mutants

The md5 of each file this paper rests on, at the commit that adds it:

| file | md5 |
| --- | --- |
| `paper/response5.py` | `96771980dfa72b1be03631ae3c7955ef` |
| `docket68/n1star/N1STAR-PROOF.md` | `03c920f8b88e8d985aac5e6b9426835e` |
| `docket68/n1star/N1STAR-LOG.md` | `9b0dfd1ac9e2bf4d0baf51956c09421d` |
| `docket68/n1star/README.md` | `b2d18c1e2412d36b8cc1d339b5377632` |
| `docket68/n1star/ks5.py` | `4fb7563006d79b3144b42b761300830a` |
| `docket68/n1star/foliation5.py` | `dab023e393662863f1f608b5d087dc9c` |
| `docket68/n1star/ansatz5.py` | `e0f4a8fbf191effb4115aff1e4a655ac` |
| `docket68/n1star/lead5.py` | `ba26d7df17f37eb6932d5b7133656d1a` |
| `docket68/n1star/data5.py` | `9404eb2d500b5b5fc810ee136bea2272` |
| `docket68/lemmas/hf_theorem5.py` | `81e96f5af9eb31fc80669d582763d5be` |
| `docket68/lemmas/counterpart5.py` | `e7dcf7bf898c2147492d28c5fb888d18` |
| `docket68/lemmas/kn_gauge.py` | `7e9e9ef8ec12e670f1717ec4fe8bd491` |
| `docket68/lemmas/hf_core5.py` | `84b715eb461838abcb5e018cd455eb5c` |

The paper's own md5 is recorded in the commit that adds it, not in itself.
