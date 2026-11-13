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
