## Restricted massless Vlasov limits {#ch:vlasov}

[[thm:two-dusts]] realises two crossing radial null dusts as high-frequency limits of vacuum metrics of the T²-mirror
class. This chapter treats a continuum of null dusts, that is, massless Vlasov matter. In four dimensions, under a U(1)
symmetry and in an elliptic gauge, Huneau and Luk prove that high-frequency limits of vacuum metrics are solutions of the
Einstein–massless Vlasov system whose measure is restricted to the cotangent bundle of the quotient [HL19, p. 13], and
that suitable small, localised, U(1)-symmetric solutions of that system are such limits [HL25, Theorem 1.1, p. 2]. Their
construction approximates the Vlasov field by n null dusts, approximates each Einstein–n-dust solution by vacuum metrics
of frequency 1/λ large compared with n, and joins the two steps along a diagonal [HL25, pp. 3, 19]. Without symmetry,
the construction for finitely many dusts is not uniform in their number [Tou24, p. 4].

We prove the five-dimensional counterpart in the class, without smallness. In [[sec:vlasov-limits]] we show that a
high-frequency limit inside the class has no stress along the torus, so that a massless Vlasov limit in the class is
restricted: its momenta are tangent to the orbit space; a round one is a two-dust solution of the kind of
[[thm:two-dusts]]. In [[sec:vlasov-restricted]] we show that restricted particles move on the null geodesics of the orbit
space, and that those reaching an axis off the axial directions focus there, so that the field of a smooth solution stays
off the axes. [[thm:vlasov]] then states: every smooth class Einstein–restricted massless Vlasov solution whose field is
a caustic-free family of dusts labelled by initial direction, off the axes and at an angle from any radial dust, on a
domain of the type [[eq:omega]] whose initial spheres have positive mean curvature, is a weak limit of class vacuum
metrics. The proof has the two steps of [HL25]. The n-dust approximants of the field are uniform in n
([[prop:vlasov-uniform-n]]); the high-frequency step is not, and the steps are joined along a diagonal. Three facts make
the high-frequency step work for every n in the class: frequencies 1, Λ, …, Λ^(n−1) remove every resonance among three
or more phases ([[lem:vlasov-hierarchy]]); waves polarised along the torus leave no term of order λ⁻¹, in the field
equations or in the constraints ([[lem:vlasov-torus-ricci]], [[lem:vlasov-constraint-coefficient]]); and the orbit space
has no shear ([[lem:vlasov-no-shear]]). The last section shows that the hypotheses are open and that an explicit family
on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]]).

*Notation.* g5 is a metric of the T²-mirror class of [[sec:class]]. We write ψ1 := A and ψ2 := B for the functions of
[[eq:class-metric]], so that

    g5 = g3 + e^(2ψ1) dφ1² + e^(2ψ2) dφ2²,      ψ := ψ1 + ψ2,      ω := (ψ2 − ψ1)/2,                {#eq:vlasov-class}

with ψ and ω those of [[prop:reduction]]. The orbit space Q carries the Lorentzian metric g3; a, b, c are its indices;
⟨·,·⟩, |·|², ∇ and □3 are taken in g3, and □5 is the wave operator of g5. An invariant function is a function on Q.
Since √|g5| = √|g3| e^ψ, for every invariant u

    □5 u = □3 u + ⟨dψ, du⟩.                                                                        {#eq:vlasov-box}

In the chart X = (τ, x) of [[sec:background]] we put ρ1² := x1² + x2² and ρ2² := x3² + x4², r := |x| and v := τ + r.
The axes are {ρ1 = 0} and {ρ2 = 0}, where one circle of the action degenerates; the distance to the axes is
min(ρ1, ρ2), the Euclidean distance of the chart. The orbit slice of Σ_τ is its quotient by T², with coordinates
(r, ϑ), ρ1 = r cos ϑ, ρ2 = r sin ϑ. Families of null dusts are indexed by A, B, C ∈ {1, …, n}, n being their number;
multi-indices are j ∈ ℤⁿ, with |j|₁ := Σ_A |j_A|. Labels are points α of the circle S¹ = ℝ/2πℤ, with its distance
d(α, α′). As in [[thm:two-dusts]], the stress of a massless matter model is the tensor T with Ric(g5) = T; a null dust
is T = q du ⊗ du with u an eikonal (g5⁻¹(du, du) = 0) and q ≥ 0, and ℓ := g5⁻¹du is its generator. For an invariant
u, ℓ = g3⁻¹du.

### Massless Vlasov limits in the class {#sec:vlasov-limits}

**Definition {#def:vlasov-field}** (Massless Vlasov fields and limits.) A massless Vlasov field on a Lorentzian manifold
assigns to each point x a finite positive Borel measure μ_x on the null covectors at x; its stress is T_x := ∫ p ⊗ p
dμ_x(p). A field on a metric of the class is *restricted* at x if μ_x is carried by the covectors with p(∂_(φ1)) =
p(∂_(φ2)) = 0, that is, by the null covectors of the orbit space. A *high-frequency limit in the class* is a C² metric
g0 of the class for which there are vacuum metrics g_i of the class with g_i → g0 uniformly and ∂g_i ⇀ ∂g0 weakly in L²
on compact sets. It is a *massless Vlasov limit* if Ric(g0) is the stress of a massless Vlasov field.

**Proposition {#prop:vlasov-limits}** (Massless Vlasov limits in the class.) Let g0 be a high-frequency limit in the
class.

(a) Ric(g0) has no torus components: R11[g0] = R22[g0] = 0, and the components Ric(g0)(∂_a, ∂_(φi)) and
Ric(g0)(∂_(φ1), ∂_(φ2)) vanish.

(b) If g0 is a massless Vlasov limit, its field is restricted at every point.

(c) If moreover g0 is round (invariant under the action of O(4) on the spheres {τ, r = const} of the chart, as every
background of [[thm:two-dusts]] is), then at every point with r > 0 the field is carried by the two radial null
directions, and in double-null coordinates (u, v) of the round metric, Ric(g0) = K_in dv ⊗ dv + K_out du ⊗ du with
K_in, K_out ≥ 0: g0 is an Einstein–two-null-dust solution, with one ingoing and one outgoing radial dust.

*Proof.* (a) The mixed components vanish identically for every metric of the class ([[lem:warped-ricci]]). Let K be a
compact set off the axes and put h := e^(2ψ) g3, as in [[prop:reduction]]. The functions ψi = ½ log g(∂_(φi), ∂_(φi))
and the components of h and of √|h| h⁻¹ are smooth functions of the components of g on K. Hence for the sequence g_i
they converge uniformly on K to those of g0, and their first derivatives, being smooth functions of the components times
first derivatives of the components, converge weakly in L²(K). Each g_i is vacuum, so by [[prop:reduction]]

    ∂_a(√|h_i| h_i^(ab) ∂_b ψ_i) = 0,      ∂_a(√|h_i| h_i^(ab) ∂_b ω_i) = 0

in the sense of distributions on K. The products √|h_i| h_i^(ab) ∂_b ψ_i converge weakly in L²(K), a uniformly
convergent factor times a weakly convergent one, so the identities pass to the limit: ∂_a(√|h0| h0^(ab) ∂_b ψ0) =
∂_a(√|h0| h0^(ab) ∂_b ω0) = 0 in distributions, and classically since g0 is C². That is □_(h0) ψ0 = □_(h0) ω0 = 0 on K,
and by [[prop:reduction]], e^(−2ψ1) R11 + e^(−2ψ2) R22 = −e^(2ψ) □_h ψ = 0 and e^(−2ψ1) R11 − e^(−2ψ2) R22 = 2 e^(2ψ)
□_h ω = 0 for g0, so R11 = R22 = 0 off the axes, and on the axes by continuity.

(b) By (a), ∫ p(∂_(φi))² dμ_x = R_(ii)[g0](x) = 0. A nonnegative continuous function with zero integral against a
positive measure vanishes on its support, so p(∂_(φ1)) = p(∂_(φ2)) = 0 on the support of μ_x.

(c) Let r(x) > 0, let S_x be the sphere {τ, r = const} through x and γ its induced metric. The isotropy group of O(4) at
x contains a copy of SO(3) acting on T_x S_x ≅ ℝ³ by rotations, irreducibly, and Ric(g0)_x is invariant under it. The
symmetric endomorphism γ⁻¹B of the restriction B of Ric(g0)_x to T_x S_x commutes with this action, so its eigenspaces
are invariant subspaces, hence 0 or T_x S_x: B = c γ. At least one of ∂_(φ1), ∂_(φ2) is a nonzero vector of T_x S_x,
and B vanishes on it by (a); so c = 0. Then ∫ p(e)² dμ_x = B(e, e) = 0 for every e ∈ T_x S_x, and as in (b) μ_x is
carried by the null covectors that vanish on T_x S_x. These form a Lorentzian plane, whose null covectors are the
multiples of dv and du; writing p = E dv or p = E du on the two lines, Ric(g0)_x = (∫ E² dμ_in) dv ⊗ dv + (∫ E² dμ_out)
du ⊗ du. ∎

So the round massless Vlasov limits in the class are Einstein–two-radial-null-dust solutions, and those with the
configuration of [[thm:two-dusts]] (a seed, an ingoing shell and an outgoing packet between them on Σ_τ0) are realised
as limits by that theorem. The proposition does not say that every round limit has this configuration. Radial momenta
stay radial along radial geodesics, so for a round metric the Einstein–(radial) massless Vlasov system is the
Einstein–two-null-dust system.

**Remark {#rem:vlasov-divergence-form}** (Why the torus stress vanishes.) The proof of (a) uses only the divergence form
of the torus components of the Ricci tensor, the five-dimensional form of [HL19, p. 4]. In a two-scale expansion it reads
as follows. Let H^(ab) := √|h| h^(ab) = H0^(ab) + λ H1^(ab)(X, θ) and f = f0 + λ f1(X, θ) at the phase θ = u/λ, with
H0(du, du) = 0. With the two-scale derivative [[eq:two-scale-derivative]], the coefficient of λ⁻¹ in ∂_a(H^(ab) ∂_b f)
is H0^(ab) u_a u_b ∂_θ² f1 = 0, and its coefficient of λ⁰ is ∂_a(H0^(ab) ∂_b f0) + ∂_a(H0^(ab) u_b ∂_θ f1) + u_a ∂_θ
(H0^(ab) ∂_b f1 + H1^(ab) ∂_b f0 + H1^(ab) u_b ∂_θ f1), whose mean over θ is ∂_a(H0^(ab) ∂_b f0): every oscillating
contribution is a θ-derivative. For the operator h^(ab) ∂_a∂_b f, not in divergence form, with h = h0 + λ h1, the mean of
the coefficient of λ⁰ contains ⟨h1(du, du) ∂_θ² f1⟩ = −⟨∂_θ h1(du, du) ∂_θ f1⟩, nonzero in general. The quadratic term
(3/2) dψ ⊗ dψ of Ric[h] in [[eq:reduced]] acquires the mean (3/2) ⟨(∂_θ ψ^(1))²⟩ du ⊗ du, λψ^(1) the oscillating part of
ψ: the stress of a limit lives on the orbit block.

### The restricted system {#sec:vlasov-restricted}

**Lemma {#lem:vlasov-flow}** (Restricted geodesics.) Off the axes the geodesic Hamiltonian of g5 is

    H(x, p) = ½ (g3^(ab) p_a p_b + e^(−2ψ1) p_(φ1)² + e^(−2ψ2) p_(φ2)²).

(a) p_(φ1) and p_(φ2) are constant along every geodesic.

(b) On {p_(φ1) = p_(φ2) = 0}, Hamilton's equations read ẋ^a = g3^(ab) p_b, ṗ_a = −½ ∂_a g3^(bc) p_b p_c, φ̇_i = 0: the
restricted null geodesics are the null geodesics of g3 at fixed angles. So the restricted fields form an invariant set
of the Vlasov equation of g5, on which it is the Vlasov equation of (Q, g3), and their stress T has T(∂_(φi), ·) = 0.
Off this set ṗ_a contains −½ p_(φi)² ∂_a e^(−2ψi), and the geodesics do not project to geodesics of g3.

(c) Let T be a symmetric tensor field of the class with T(∂_(φi), ·) = 0. Then, on orbit indices,
div_(g5) T = e^(−ψ) div_(g3)(e^ψ T). In particular a null dust T = q du ⊗ du with u an invariant eikonal satisfies
div_(g5) T = 0 if and only if

    ℓ(q) + q □5 u = 0,      equivalently      div_(g3)(e^ψ q ℓ) = 0,                                   {#eq:vlasov-dust}

and the orbit density e^ψ q is transported by ℓ with the expansion □3 u: ℓ(e^ψ q) + (□3 u) e^ψ q = 0.

*Proof.* (a) H does not depend on φ1, φ2. (b) is Hamilton's equations for H at p_φ = 0, and T(∂_(φi), ·) = ∫ p(∂_(φi))
p dμ = 0. (c) Since T^(φi μ) = 0 and the components do not depend on the angles, (div_(g5) T)_b = |g5|^(−1/2) ∂_a(|g5|^(1/2)
T^a_b) − ½ ∂_b (g5)_(cd) T^(cd), the second term having orbit indices only; with |g5|^(1/2) = |g3|^(1/2) e^ψ this is
e^(−ψ)(|g3|^(−1/2) ∂_a(|g3|^(1/2) e^ψ T^a_b) − ½ ∂_b (g3)_(cd) e^ψ T^(cd)) = e^(−ψ) (div_(g3)(e^ψ T))_b. For the dust,
∇^μ(q ∂_μ u ∂_ν u) = div_(g5)(q ℓ) ∂_ν u + q ℓ^μ ∇_μ ∂_ν u, and ℓ^μ ∇_μ ∂_ν u = ½ ∂_ν(g5⁻¹(du, du)) = 0; as du ≠ 0,
div_(g5) T = 0 is div_(g5)(q ℓ) = ℓ(q) + q □5 u = 0. By [[eq:vlasov-box]], ℓ(e^ψ q) = e^ψ(ℓ(q) + q ⟨dψ, du⟩) =
−e^ψ q □3 u, and div_(g3)(e^ψ q ℓ) = ℓ(e^ψ q) + e^ψ q □3 u. ∎

**Definition {#def:vlasov-label}** (Fields in label form.) Let Ω be a domain of the type [[eq:omega]] for a metric g of
the class (its constants (τ0, τ_end, a, V) fixed and its sets defined by the coordinate functions τ, r, v). A *restricted
field in label form* on Ω is a pair (q, u) of smooth invariant functions on Ω × S¹, q ≥ 0, such that each u_α :=
u(·, α) is an eikonal of g on a neighbourhood of the *tube* D_α of supp q(·, α), with stress

    T_V := ∫_(S¹) q(·, α) du_α ⊗ du_α dα,                                                          {#eq:vlasov-stress}

and with every q(·, α) transported by [[eq:vlasov-dust]] for u = u_α. Here the *rays* of u_α are the integral curves of
ℓ_α := g⁻¹du_α, and D_α is the set of points of Ω on the future rays from supp q(·, α) ∩ Σ_τ0 that stay in Ω. Let
β0(x, α) be the angle, in a frame of the orbit slice of Σ_τ0 orthonormal for its induced metric, of the covector
d(u_α|Σ_τ0)(x). The field is *labelled by initial direction* if for every x the map α ↦ β0(x, α) is injective on the
labels α with (x, α) ∈ supp q. T_V is the stress of the restricted field μ_x := ∫ q(x, α) δ_(du_α(x)) dα, and each
label is a null dust.

In [HL25, (1.2), p. 2] the labels are the initial directions themselves: u_α↾Σ0 = x¹ cos α + x² sin α, so β0 = α.

**Lemma {#lem:vlasov-axis-stress}** (The stress at an axis.) Let T be a smooth symmetric 2-tensor field on a
neighbourhood of a point x0 of the axis {ρ2 = 0}, invariant under the rotations of the (x3, x4)-plane and under x4 ↦
−x4. For ρ2 > 0 put e_ρ := ρ2⁻¹(x3 ∂_3 + x4 ∂_4) and e_φ := ρ2⁻¹(x3 ∂_4 − x4 ∂_3). Then T(e_ρ, e_φ) = 0 and

    T(e_ρ, e_ρ) − T(e_φ, e_φ) = O(ρ2²).

If T is the stress of a restricted field, T(e_φ, e_φ) = ρ2⁻² T(∂_(φ2), ∂_(φ2)) = 0, so T(e_ρ, e_ρ) = O(ρ2²), and at x0
the field's measure is carried by the covectors in span(dτ, dr): at an axis point the momenta of a restricted field with
smooth stress are radial.

*Proof.* At x with ρ2 > 0 let R be the reflection of the (x3, x4)-plane in the line through (x3, x4), the identity on the
other coordinates; it is a rotation composed with x4 ↦ −x4, it fixes x, and Re_ρ = e_ρ, Re_φ = −e_φ. So T(e_ρ, e_φ) =
T(Re_ρ, Re_φ) = −T(e_ρ, e_φ) = 0. Let T_(ij), i, j ∈ {3, 4}, be the planar block, a smooth function of y := (x3, x4) at
fixed other coordinates, and expand T_(ij)(y) = T_(ij)(0) + L_(ij)(y) + O(|y|²) with L linear. Invariance under the
rotations and the reflection makes T(0) commute with O(2) acting on ℝ², which is irreducible, so T(0) = c I. Invariance
under the rotation by π, y ↦ −y, gives T_(ij)(−y) = T_(ij)(y), so L(−y) = L(y) and L = 0. Hence T_(ij) = c δ_(ij) +
O(ρ2²), and T(e_ρ, e_ρ) − T(e_φ, e_φ) = (T_(ij) − c δ_(ij))(e_ρ^i e_ρ^j − e_φ^i e_φ^j) = O(ρ2²). For a restricted field
T(∂_(φ2), ∂_(φ2)) = 0 and ∂_(φ2) = ρ2 e_φ, so T(e_φ, e_φ) = 0, T(e_ρ, e_ρ) = O(ρ2²), and c = lim T(e_φ, e_φ) = 0; so
∫ p(∂_3)² dμ_(x0) = ∫ p(∂_4)² dμ_(x0) = 0. On the support p also vanishes on ∂_(φ1) = x1 ∂_2 − x2 ∂_1, and with ρ2 = 0,
ρ1 = r at x0, so p ∈ span(dτ, dr). ∎

**Remark {#rem:vlasov-axis-density}** (Densities at an axis.) Let a restricted field near the axis {ρ2 = 0} have, at
distance ρ2, the density f(ρ2, β) dβ/(2π) on unit-energy momenta whose spatial part makes the angle β with the axis in
an orthonormal frame (e_axis, e_ρ) of the orbit slice, so that T(e_ρ, e_ρ) = (2π)⁻¹ ∫ f sin²β dβ. If f is continuous and
f(0, ·) does not vanish off {sin β = 0}, then T(e_ρ, e_ρ) has a positive limit at the axis, not O(ρ2²), and by
[[lem:vlasov-axis-stress]] the stress is not smooth. A density concentrating on the axial directions keeps the stress
of size ρ2²: for f = ρ2⁻¹(e^(−β²/ρ2²) + e^(−(|β|−π)²/ρ2²)) on (−π, π], the total density (2π)⁻¹ ∫ f dβ tends to π^(−1/2)
and T(e_ρ, e_ρ)/ρ2² tends to 1/(2√π), while ∂_β f is unbounded. Indeed, up to terms O(e^(−c/ρ2²)), each Gaussian
contributes ∫ e^(−t²/ρ2²)(t² + O(t⁴)) dt = (√π/2) ρ2³ + O(ρ2⁵) to ∫ f sin²β dβ times ρ2, since sin²β = sin²(|β| − π);
so T(e_ρ, e_ρ) = (2π)⁻¹ ρ2⁻¹ (√π ρ2³ + O(ρ2⁵)). So at an axis a restricted field with smooth stress is zero, or, in the
limit, two radial dusts along the axis.

**Lemma {#lem:vlasov-axis-phases}** (Invariant null phases at an axis.) Let u be an invariant function and x0 a point of
the axis {ρ2 = 0} with r(x0) > 0. Then du(x0) ∈ span(dτ, dr). If u is null at x0 and du(x0) ≠ 0, then du(x0) lies on
one of the two null lines of the Lorentzian plane span(dτ, dr) at x0, and two invariant null phases on the same line
have g⁻¹(du_A, du_B) = 0 at x0. So among the null dusts present at an axis point at most two, one on each line (one
ingoing and one outgoing), are pairwise separated.

*Proof.* The reflection x3 ↦ −x3 is a rotation by π composed with x4 ↦ −x4, so u is even in x3 and ∂_3 u = 0 on
{x3 = 0}; likewise ∂_4 u = 0 on {x4 = 0}. The rotation field x1 ∂_2 − x2 ∂_1 annihilates du. At x0 these give du(x0)
∈ span(dτ, x1 dx1 + x2 dx2) = span(dτ, dρ1), and dρ1 = dr there. The plane span(dτ, dr) contains the timelike dτ (the
slices are spacelike) and the null du(x0) ≠ 0, so g⁻¹ restricted to it is Lorentzian, and its null covectors form two
lines. Two covectors on one null line are proportional and null, so their product vanishes. ∎

**Proposition {#prop:vlasov-axis-focus}** (Restricted particles focus at an axis.) Let g5 be a smooth metric of the class
near a point x0 of the axis {ρ2 = 0} with r(x0) > 0. Let a restricted massless Vlasov field be given off the axes by an
orbit density: T = e^(−ψ) T3, where T3 is the stress of a density F ≥ 0 on the bundle of null directions of (Q, g3),
continuous, and transported by the null geodesic flow of g3 (the Vlasov equation of (Q, g3), [[lem:vlasov-flow]] (b) and
(c)). If F > 0 at a null direction whose g3-geodesic reaches x0 transversally to the axis, then there are c > 0 and a
timelike vector field n near x0 with T(n, n) ≥ c/ρ2 at the points of that geodesic near x0. So T and Ric(g5) = T are
unbounded near x0, and g5 is not C² there.

*Proof.* Let P be the fixed set {x2 = x4 = 0} of the two reflections, a three-dimensional submanifold with coordinates
(τ, x1, x3). It meets every orbit near x0, at the points (τ, ±ρ1, ±ρ2). The Killing fields ∂_(φ1), ∂_(φ2) are along ∂_2,
∂_4 at the points of P and orthogonal to P by the reflection symmetry, so on {x1 > 0, x3 > 0} the induced metric g_P of
P is g3 in the coordinates (τ, ρ1, ρ2) = (τ, x1, x3). As g5 is smooth, g_P is a smooth Lorentzian metric on P, even in
x3: g3 extends across the edge {ρ2 = 0} to the smooth metric g_P, and the null geodesic flow of g3 extends to the smooth
flow of g_P, under which the geodesic reaching x0 transversally crosses {x3 = 0}. On the bundle of null directions the
transport of F is X(F) + κ F = 0 along the generator X of this flow, with κ smooth, so F stays positive along the flow
line of the given direction and, by continuity, F ≥ c1 > 0 on a neighbourhood U of the arriving direction at the points
of the geodesic near x0. Hence T3(n, n) ≥ ∫_U F (p(n))² ≥ c2 > 0 there, for n timelike. The Killing field ∂_(φ2) = x3 ∂_4
− x4 ∂_3 has, at points of P, e^(2ψ2) = g5(∂_(φ2), ∂_(φ2)) = x3² (g5)_(44) = ρ2² (g5)_(44), with (g5)_(44) > 0, and e^(ψ1)
is bounded near x0 since ρ1(x0) = r(x0) > 0. So T(n, n) = e^(−ψ1−ψ2) T3(n, n) ≥ c/ρ2. ∎

The mechanism is the focusing of a converging beam: in a flat plane, particles moving radially inward with speed v have
a density n(ρ, t) solving ∂_t n − v ρ⁻¹ ∂_ρ(ρ n) = 0, so ρ n(ρ, t) = (ρ + v t) n0(ρ + v t) and ρ n → v t n0(v t) > 0 as
ρ → 0 once the beam has reached the centre; particles moving along the axis (v = 0) keep their density.

### The theorem {#sec:vlasov-theorem}

Let Ω be a domain of the type [[eq:omega]], Ω = {τ0 ≤ τ ≤ τ_end, r ≥ a, v + (τ − τ_end) ≤ V + 1}, with Σ_τ := Ω ∩ {τ}
and its outer radius b(τ) := V + 1 − τ + (τ_end − τ). Let (g, q, u) be a smooth class solution on Ω of the
Einstein–restricted massless Vlasov system in label form, Ric(g) = T_V + T_rad, where T_rad is zero or a pair of null
dusts q_in du_in ⊗ du_in + q_out du_out ⊗ du_out, one ingoing and one outgoing, that may reach the axes as in
[[thm:class-stability]] (the *radial dusts*; on the round backgrounds of [[thm:two-dusts]] they are the two radial
families). We assume:

- (Ω) For g: each Σ_τ is spacelike; {r = a} is spacelike and r decreases along future causal curves near it;
  {v + τ = const} is spacelike and v + τ increases along future causal curves; every generator of a dust present in Ω
  (a ray of u_α through a point of D_α, or a generator of a radial dust on its support), followed to the past, stays
  in Ω and meets Σ_τ0. These are (a)–(d) of [[lem:domain]], for g.
- (V1) q and u are smooth in (x, α), and the field is labelled by initial direction. For each α and each x0 in a
  neighbourhood of supp q(·, α) ∩ Σ_τ0, the point y_τ(x0) where the ray of u_α from x0 meets Σ_τ depends on x0 with
  Jacobian determinant ≥ J0 > 0 in the coordinates (r, ϑ) of the orbit slices, for every τ with y_τ(x0) in a
  neighbourhood of Ω (no caustic). On Σ_τ0 ∩ supp q, ∂_α β0 ≥ b > 0.
- (V2) dist(D_α, axes) ≥ 2δ > 0 for every α.
- (V2′) On the support of each radial dust, every label present has a momentum du_α whose spatial part makes an angle
  ≥ η > 0, in the orbit slice, with both radial null directions, or the supports are disjoint. The radial dusts satisfy
  the condition (H2′) of [[thm:class-stability]], with the lateral boundaries of Ω adapted where they meet an axis.
- (V3) On Σ_τ0 ∩ Ω the spheres {r = const} have positive mean curvature, and the symmetrizer 𝒮 of
  [[eq:data-symmetrizer]] makes the r-coefficient 𝒮 A0 of the momentum system positive definite: the two signs of
  [[lem:constraints-evolution]] (a).

**Theorem {#thm:vlasov}** (Restricted massless Vlasov limits.) Let (g, q, u) satisfy (Ω), (V1), (V2), (V2′) and (V3).
Then there are smooth metrics g_i on Ω, invariant under T² and under both reflections, with Ric(g_i) = 0,

    g_i → g uniformly on Ω,      ∂g_i ⇀ ∂g weakly in L²(Ω).

The metric g_i is a vacuum approximation of the n_i-dust approximant of the field, along odd n_i → ∞.

No smallness of g or of the field is assumed. The properties (b) and (c) of [[lem:constraints-evolution]], no
coefficient of order λ⁻¹ and unchanged principal coefficients, are properties of the approximant's data; they are proved
in [[thm:vlasov-n-data]] for torus-polarised waves and are not hypotheses. The hypotheses are open
([[lem:vlasov-open]]), and an explicit family on Tangherlini meets them ([[prop:vlasov-nonempty]]), so the theorem
covers a nonempty open set of solutions.

**Remark {#rem:vlasov-v2}** ((V2) for smooth solutions.) Let (g, q, u) be smooth on Ω̄, with no label having an axial
momentum at an axis point of supp q. Then (V2) holds for some δ > 0. Indeed, the set D := {(x, α) : x ∈ D_α} is the
image of the compact set supp q ∩ (Σ_τ0 × S¹) under the continuous flow of the rays, intersected with Ω̄ × S¹, so it is
compact. A ray of g3 that meets an axis either crosses it transversally or lies in it: in the meridional picture of
the proof of [[prop:vlasov-axis-focus]], a null geodesic of g_P tangent to {x3 = 0} at a point is mapped to a geodesic
with the same initial data by x3 ↦ −x3, so it lies in that set. The first is excluded by [[prop:vlasov-axis-focus]],
since g is C²; the second by assumption. So D does not meet axes × S¹, and a compact set disjoint from a closed set lies
at positive distance from it.

**Remark {#rem:vlasov-obstructions}** (What the hypotheses avoid.) Four obstructions are proved in this chapter, and the
theorem is built so that none applies. (O1) At an axis point every invariant null phase is radial, and two of one
orientation have vanishing mixed symbol ([[lem:vlasov-axis-phases]]): the labels are kept off the axes, which only the
radial dusts reach. (O2) Restricted particles reaching an axis focus there ([[prop:vlasov-axis-focus]]). (O3) Without a
hierarchy of frequencies, an antipodal pair and any third phase resonate exactly ([[lem:vlasov-resonance]]): the
frequencies are 1, Λ, …, Λ^(n−1). (O4) A non-radial wave with a component on the orbit block leaves a term of order λ⁻¹
in the constraints ([[lem:vlasov-constraint-coefficient]] (c)): the waves are torus-polarised. Where a label is
parallel to a radial direction on a radial dust's support every mixed harmonic of the pair is resonant
([[rem:vlasov-radial-pair]]): hence (V2′).

### Separation and coherence of the labels {#sec:vlasov-coherence}

**Lemma {#lem:vlasov-separation}** (The flow keeps the labels separated.) Under (Ω), (V1) and (V2) there is c0 > 0,
depending on Ω and on the field and not on any choice of labels, such that at every point y ∈ D_α ∩ D_α′

    |g⁻¹(du_α, du_α′)(y)| ≥ c0 d(α, α′)².                                                       {#eq:vlasov-separation}

*Proof.* Let 𝒫 be the bundle of null directions of g3 over the orbit slices, a circle bundle, with the angle β of the
spatial part in a frame orthonormal for the slice metric. For τ ∈ [τ0, τ_end] let Φ_τ take (x0, α) ∈ Σ_τ0 × S¹ to (y, β)
∈ 𝒫|Σ_τ, the point where the ray of u_α from x0 meets Σ_τ and the angle of du_α there. Φ_τ is the flow of the null
geodesic spray on 𝒫 from Σ_τ0 to Σ_τ composed with the section σ(x0, α) := (x0, β0(x0, α)). The flow is a
diffeomorphism with positive Jacobian (it depends continuously on τ and is the identity at τ0), and Dσ is triangular
with determinant ∂_α β0 ≥ b. So det DΦ_τ ≥ c_Φ > 0 on the compact set of the (x0, α) in question. Write DΦ_τ in blocks,
with A := ∂y/∂x0, B := ∂y/∂α, C := ∂β/∂x0, D := ∂β/∂α. At fixed y the label α determines its ray, and x0 = x0(y, α),
since A is invertible by (V1); the angle at y of du_α is β(y; α) := β(x0(y, α), α), and

    ∂_α β(y; α) = D − C A⁻¹ B = det DΦ_τ / det A,

the Schur complement. Since 0 < det A ≤ C_A on the compact set, ∂_α β(y; α) ≥ c1 := c_Φ/C_A > 0 wherever the labels
between α and α′ are present at y, which holds on a uniform neighbourhood of the diagonal α′ = α by (V1). In 2+1
dimensions null covectors at y are k = E(−1, cos β, sin β) in an orthonormal frame, E > 0, and

    g⁻¹(k, k′) = −E E′ (1 − cos(β − β′)),      |g⁻¹(k, k′)| = 2 E E′ sin²((β − β′)/2).

So near the diagonal |g⁻¹(du_α, du_α′)| ≥ c d(α, α′)², with E bounded below on the compact set. Away from the diagonal
the left side of [[eq:vlasov-separation]] divided by d(α, α′)² is continuous on a compact set, and it is positive: if
du_α and du_α′ were parallel at y, the null geodesic of g3 through y in that direction, followed to the past, would
meet Σ_τ0 at one point x0 with one direction, so β0(x0, α) = β0(x0, α′), and α = α′ since the field is labelled by
initial direction. Its infimum c0 is positive. ∎

For the n labels α_A := 2πA/n, d(α_A, α_B) ≥ 2π/n, so the dusts sampled at them are pairwise separated with constant
c0 (2π/n)². This is the separation η′ ≳ 1/n² of [HL25, Lemma 4.15, p. 18]; for n directions 2πA/n on the flat orbit
space with unit energies the least mixed symbol is exactly 1 − cos(2π/n), and n²(1 − cos(2π/n)) → 2π².

Pairwise separation is not enough for the scheme of [[thm:vlasov-n-approximant]]. At stage m its residual carries the
harmonics e^(i j·θ) with |j|₁ ≤ m + 2, and a harmonic with two or more nonzero entries is removed by division by

    Q_j := g⁻¹(K_j, K_j),      K_j := Σ_A j_A ν_A du_A,                                           {#eq:vlasov-symbol}

ν_A the frequency of family A.

**Lemma {#lem:vlasov-resonance}** (An exact resonance.) In 2+1-dimensional Minkowski space let k_a, k_b be future null
covectors of equal energy with antipodal spatial directions, and k_c any future null covector of that energy. Then
K := k_a + k_b − k_c is null. So with equal frequencies the mixed harmonic e^(i(θ_a + θ_b − θ_c)) is exactly resonant,
whatever the pairwise separations.

*Proof.* In an orthonormal frame, k_a = E(−1, e), k_b = E(−1, −e), k_c = E(−1, f), with e, f unit vectors. Then K =
E(−1, −f), and g⁻¹(K, K) = E²(−1 + 1) = 0. ∎

**Lemma {#lem:vlasov-hierarchy}** (Coherence under a hierarchy of frequencies.) Let k_1, …, k_n be covectors at a point of
a 2+1-dimensional Lorentzian space with g⁻¹(k_A, k_A) = 0, |g⁻¹(k_A, k_B)| ≥ c > 0 for A ≠ B, and |k_A| ≤ M in an
orthonormal frame. Let Λ > 1 and ν_A := Λ^(A−1). For every j ∈ ℤⁿ with at least two nonzero entries and |j|₁ ≤ m, let
B1 > B2 be its two largest indices with nonzero entries. Then

    |g⁻¹(K_j, K_j)| ≥ 2 ν_B1 ν_B2 (c − m M²/Λ − m² M²/(2Λ)).                                    {#eq:vlasov-hierarchy}

In particular every such combination is non-null, with this margin, once Λ > (m + m²/2) M²/c.

*Proof.* In the orthonormal frame |g⁻¹(k, k′)| ≤ |k| |k′|. Put K := K_j = j_B1 ν_B1 k_B1 + V, V := Σ_(A ≠ B1) j_A ν_A k_A.
Since k_B1 is null, g⁻¹(K, K) = 2 j_B1 ν_B1 g⁻¹(k_B1, V) + g⁻¹(V, V). Here g⁻¹(k_B1, V) = j_B2 ν_B2 g⁻¹(k_B1, k_B2) +
Σ_(A < B2) j_A ν_A g⁻¹(k_B1, k_A), and ν_A ≤ ν_B2/Λ for A < B2, so |g⁻¹(k_B1, V)| ≥ ν_B2 (c − m M²/Λ), using |j_B2| ≥ 1
and Σ|j_A| ≤ m. Further |V| ≤ Σ_(A ≤ B2) |j_A| ν_A M ≤ m ν_B2 M, so |g⁻¹(V, V)| ≤ m² M² ν_B2² ≤ m² M² ν_B1 ν_B2/Λ. With
|j_B1| ≥ 1, |g⁻¹(K, K)| ≥ 2 ν_B1 ν_B2 (c − m M²/Λ) − m² M² ν_B1 ν_B2/Λ, which is [[eq:vlasov-hierarchy]]. ∎

With c = c0 (2π/n)² this is the choice ν_A = c n² ν_(A−1) of [HL25, Lemma 4.16, p. 18]. The phases ν_A u_A are
eikonals, so the two-scale scheme is unchanged; the wave of family A carries the amplitude λ F_A/ν_A, so that its
derivatives are of the size of F_A.

**Remark {#rem:vlasov-coherence-values}** (Numerical observation.) On the orbit space of Tangherlini with μ = 1 and labels
in [−0.6, 0.6], the Schur formula of [[lem:vlasov-separation]] agreed with shooting to 1.1 × 10⁻⁹, ∂_α β was at least
0.798, and the least mixed symbol of adjacent labels divided by (Δα)² was 0.2923, 0.2926, 0.2927, 0.2927 at n = 8, 16,
32, 64. For the four labels 2πA/4 on flat 2+1 with the hierarchy, every Q_j with |j|₁ ≤ 5 was found exactly to satisfy
|Q_j|/(ν_B1 ν_B2) ≥ 359/216; with two radial covectors added and labels at angle at least η from them (label–radial
symbols at least 1/5), every combination with |j|₁ ≤ 4 had |Q_j|/(ν_B1 ν_B2) ≥ 35612/609961, above the bound 4/50765
of [[eq:vlasov-hierarchy]]. No proof uses these values.
