## Restricted massless Vlasov limits {#ch:vlasov}

[[thm:two-dusts]] realises two crossing radial null dusts as high-frequency limits of vacuum metrics of the T²-mirror
class. This chapter treats a continuum of null dusts, that is, massless Vlasov matter. In four dimensions, under a U(1)
symmetry and in an elliptic gauge, Huneau and Luk prove that high-frequency limits of vacuum metrics are solutions of the
Einstein–massless Vlasov system whose measure is restricted to the cotangent bundle of the quotient [HL19, p. 1; p. 13],
and that suitable small, localised, U(1)-symmetric solutions of that system are such limits [HL25, Theorem 1.1, p. 2].
Their construction approximates the Vlasov field by n null dusts, approximates each Einstein–n-dust solution by vacuum
metrics of frequency 1/λ large compared with n, and joins the two steps along a diagonal [HL25, pp. 3, 19]. Without
symmetry, the construction for finitely many dusts is not uniform in their number [Tou24, p. 4].

We prove the five-dimensional counterpart in the class, without smallness, for fields that stay off the axes. In
[[sec:vlasov-limits]] we show that a high-frequency limit inside the class has no stress along the torus, so that a
massless Vlasov limit in the class is restricted: its momenta are tangent to the orbit space; if the limit is moreover
round, it is a two-dust solution of the kind of [[thm:two-dusts]]. In [[sec:vlasov-restricted]] we show that restricted
particles move on the null geodesics of the orbit space, and that those reaching an axis off the axial directions focus
there, so that the field of a smooth solution stays off the axes. [[thm:vlasov]] then states: every smooth class
Einstein–restricted massless Vlasov solution whose field is a caustic-free family of dusts labelled by initial direction
and off the axes, on a domain of the type [[eq:omega]] whose initial spheres have positive mean curvature, is a weak
limit of class vacuum metrics. The proof has the two steps of [HL25]. The n-dust approximants of the field are uniform
in n ([[prop:vlasov-uniform-n]]); the high-frequency step is not, and the steps are joined along a diagonal. Four facts
make the high-frequency step work for every n in the class: frequencies 1, Λ, …, Λ^(n−1) remove every resonance among
three or more phases up to the order the scheme uses ([[lem:vlasov-hierarchy]]); waves polarised along the torus leave
no term of order λ⁻¹, in the field equations or in the constraints ([[lem:vlasov-torus-ricci]],
[[lem:vlasov-constraint-coefficient]]); the orbit space has no shear ([[lem:vlasov-no-shear]]); and the constraints,
whose coefficients oscillate in every direction of the initial slice, are solved with bounds uniform in λ in norms in
which each angular derivative carries the factor λ that the oscillation costs, except the first two of the metric
unknown ([[prop:vlasov-scaled-correction]]). Each label is an eikonal only near its tube, and every transport of a
family is cut off away from its tube ([[lem:vlasov-local-stability]]). The last section shows that the hypotheses are
open and that an explicit family on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]]).

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
directions, and in double-null coordinates (u, v) of the round metric, Ric(g0) = 𝔮_in dv ⊗ dv + 𝔮_out du ⊗ du with
𝔮_in, 𝔮_out ≥ 0: g0 is an Einstein–two-null-dust solution, with one ingoing and one outgoing radial dust.

*Proof.* (a) The mixed components vanish identically for every metric of the class ([[lem:warped-ricci]]). Let U be a
compact set off the axes and put h := e^(2ψ) g3, as in [[prop:reduction]]. The functions ψi = ½ log g(∂_(φi), ∂_(φi))
and the components of h and of √|h| h⁻¹ are smooth functions of the components of g on U. Hence for the sequence g_i
they converge uniformly on U to those of g0, and their first derivatives, being smooth functions of the components times
first derivatives of the components, converge weakly in L²(U). Each g_i is vacuum, so by [[prop:reduction]]

    ∂_a(√|h[g_i]| h[g_i]^(ab) ∂_b ψ[g_i]) = 0,      ∂_a(√|h[g_i]| h[g_i]^(ab) ∂_b ω[g_i]) = 0

in the sense of distributions on U, where h[g_i], ψ[g_i], ω[g_i] are h, ψ, ω of g_i. The products √|h[g_i]| h[g_i]^(ab)
∂_b ψ[g_i] converge weakly in L²(U), a uniformly convergent factor times a weakly convergent one, so the identities pass
to the limit: ∂_a(√|h0| h0^(ab) ∂_b ψ0) = ∂_a(√|h0| h0^(ab) ∂_b ω0) = 0 in distributions, and classically since g0 is
C². That is □_(h0) ψ0 = □_(h0) ω0 = 0 on U, and by [[prop:reduction]], e^(−2ψ1) R11 + e^(−2ψ2) R22 = −e^(2ψ) □_h ψ = 0
and e^(−2ψ1) R11 − e^(−2ψ2) R22 = 2 e^(2ψ) □_h ω = 0 for g0, so R11 = R22 = 0 off the axes, and on the axes by
continuity.

(b) By (a), ∫ p(∂_(φi))² dμ_x = R_(ii)[g0](x) = 0. A nonnegative continuous function with zero integral against a
positive measure vanishes on its support, so p(∂_(φ1)) = p(∂_(φ2)) = 0 on the support of μ_x.

(c) Let r(x) > 0, let S_x be the sphere {τ, r = const} through x and γ its induced metric. The isotropy group of O(4) at
x contains a copy of SO(3) acting on T_x S_x ≅ ℝ³ by rotations, irreducibly, and Ric(g0)_x is invariant under it. The
symmetric endomorphism γ⁻¹B of the restriction B of Ric(g0)_x to T_x S_x commutes with this action, so its eigenspaces
are invariant subspaces, hence 0 or T_x S_x: B = c γ. At least one of ∂_(φ1), ∂_(φ2) is a nonzero vector of T_x S_x,
and B vanishes on it by (a); so c = 0. Then ∫ p(e)² dμ_x = B(e, e) = 0 for every e ∈ T_x S_x, and as in (b) μ_x is
carried by the null covectors that vanish on T_x S_x. These form a Lorentzian plane, whose null covectors are the
multiples of dv and du; writing p = E dv or p = E du on the two lines, Ric(g0)_x = (∫ E² dμ_in) dv ⊗ dv + (∫ E² dμ_out)
du ⊗ du. Each dust is conserved: Ric(g0) is traceless, dv and du being null, so the contracted Bianchi identity gives
div Ric(g0) = 0; since ∇_(g0⁻¹dv) dv = ½ d(g0⁻¹(dv, dv)) = 0, div(𝔮_in dv ⊗ dv) = div(𝔮_in g0⁻¹dv) dv, and likewise for
du; as dv and du are independent, div(𝔮_in g0⁻¹dv) = div(𝔮_out g0⁻¹du) = 0, in the sense of distributions where the
densities are only continuous. ∎

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

*Proof.* (a) H does not depend on φ1, φ2. (b) is Hamilton's equations for H at p_φ = 0, and T(∂_(φi), ·) = ∫ p(∂_(φi)) p
dμ = 0. (c) Since T^(φi μ) = 0 and the components do not depend on the angles, (div_(g5) T)_b = |g5|^(−1/2)
∂_a(|g5|^(1/2) T^a_b) − ½ ∂_b (g5)_(cd) T^(cd), the second term having orbit indices only; with |g5|^(1/2) = |g3|^(1/2)
e^ψ this is e^(−ψ)(|g3|^(−1/2) ∂_a(|g3|^(1/2) e^ψ T^a_b) − ½ ∂_b (g3)_(cd) e^ψ T^(cd)) = e^(−ψ) (div_(g3)(e^ψ T))_b. For
the dust, ∇^μ(q ∂_μ u ∂_ν u) = div_(g5)(q ℓ) ∂_ν u + q ℓ^μ ∇_μ ∂_ν u, and ℓ^μ ∇_μ ∂_ν u = ½ ∂_ν(g5⁻¹(du, du)) = 0; as du
≠ 0, div_(g5) T = 0 is div_(g5)(q ℓ) = ℓ(q) + q □5 u = 0. By [[eq:vlasov-box]], ℓ(e^ψ q) = e^ψ(ℓ(q) + q ⟨dψ, du⟩) = −e^ψ
q □3 u, and div_(g3)(e^ψ q ℓ) = ℓ(e^ψ q) + e^ψ q □3 u. ∎

**Definition {#def:vlasov-label}** (Fields in label form.) Let Ω be a domain of the type [[eq:omega]] for a metric g of
the class (its constants (τ0, τ_end, a, V) fixed and its sets defined by the coordinate functions τ, r, v). For a smooth
invariant function u on Ω the *rays* of u are the integral curves of g⁻¹du, and the *tube* of a compact set K ⊂ Σ_τ0 ∩ Ω
for u is the set of points of Ω on the rays of u from K, each followed forward while it stays in Ω. A *restricted field
in label form* on Ω is a pair (F, u) of smooth invariant functions on Ω × S¹, F ≥ 0, with density q := F², such that
each u_α := u(·, α) is an eikonal of g on a neighbourhood of the tube D_α of supp q(·, α) ∩ Σ_τ0 for u_α, with g⁻¹du_α
future directed there, with stress

    T_V := ∫_(S¹) q(·, α) du_α ⊗ du_α dα,                                                          {#eq:vlasov-stress}

and with every amplitude F(·, α) transported by

    2 ℓ_α(F) + (□5 u_α) F = 0,      ℓ_α := g⁻¹du_α,                                              {#eq:vlasov-amplitude}

and vanishing off D_α. The transport is [[eq:vlasov-dust]] for q(·, α) = F(·, α)², as in [HL25, (1.2)]. Off a
neighbourhood of D_α the function u_α enters neither T_V nor [[eq:vlasov-amplitude]], and nothing is assumed of it there:
a label is an eikonal only near its tube. Let β0(x, α) be the angle, in a frame of the orbit slice of Σ_τ0 orthonormal
for its induced metric, of the covector d(u_α|Σ_τ0)(x). The field is *labelled by initial direction* if for every x the
map α ↦ β0(x, α) is injective on the labels α with (x, α) ∈ supp q. T_V is the stress of the restricted field μ_x := ∫
q(x, α) δ_(du_α(x)) dα, and each label is a null dust. Replacing u_α by −u_α changes neither T_V nor
[[eq:vlasov-amplitude]], so the time orientation of ℓ_α only fixes a sign. It fixes the *branch* of the eikonal equation
used below: given the restriction of u_α to Σ_τ0, of nonzero differential, the τ-derivative of u_α there is the root of
g⁻¹(du_α, du_α) = 0 for which g⁻¹du_α is future directed. (With 𝔫 the future unit normal of Σ_τ0, the two roots are
du_α(𝔫) = ±|d(u_α|Σ_τ0)|, and g⁻¹du_α is future directed exactly when du_α(𝔫) < 0.)

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
and T(e_ρ, e_ρ)/ρ2² tends to 1/(2√π), while ∂_β f is unbounded. Indeed, since sin²β = sin²(|β| − π), ρ2 ∫ f sin²β dβ is,
up to terms O(e^(−c/ρ2²)), the sum of two Gaussian integrals ∫ e^(−t²/ρ2²)(t² + O(t⁴)) dt = (√π/2) ρ2³ + O(ρ2⁵);
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

**Proposition {#prop:vlasov-axis-focus}** (Restricted particles cannot reach an axis.) Let g5 be a C² metric of the
class near a point x0 of the axis {ρ2 = 0} with r(x0) > 0, and suppose that off the axes Ric(g5) = T := e^(−ψ) T3, where
T3 is the stress of a continuous density f ≥ 0 on the bundle of null directions of (Q, g3) transported by the null
geodesic flow of g3 (the Vlasov equation of (Q, g3), [[lem:vlasov-flow]] (b) and (c)): X(f) + κ f = 0 along the
generator X of that flow, with κ a continuous function of g3 and its first derivatives. Then f vanishes on every null
direction whose g3-geodesic reaches x0 transversally to the axis.

*Proof.* Suppose that f > 0 at a null direction whose geodesic reaches x0 transversally. Let P be the fixed set {x2 =
x4 = 0} of the two reflections, a three-dimensional submanifold with coordinates (τ, x1, x3). It meets every orbit near
x0, at the points (τ, ±ρ1, ±ρ2). The Killing fields ∂_(φ1), ∂_(φ2) are along ∂_2, ∂_4 at the points of P and orthogonal
to P by the reflection symmetry, so on {x1 > 0, x3 > 0} the induced metric g_P of P is g3 in the coordinates (τ, ρ1,
ρ2) = (τ, x1, x3). As g5 is C², g_P is a C² Lorentzian metric on P, even in x3: g3 extends across the edge {ρ2 = 0} to
g_P, and the null geodesic flow of g3 extends to the flow of g_P, which is C¹, under which the geodesic reaching x0
transversally crosses {x3 = 0}. In the coordinates of P, κ is the same function of g_P and its first derivatives, so it
is continuous on the bundle of null directions of g_P over a neighbourhood of x0. Hence f, which equals its initial
value times exp(−∫κ) along each flow line, stays positive along the flow line of the given direction, and, by
continuity, f ≥ c1 > 0 on a neighbourhood U of the arriving direction at the points of the geodesic near x0. So T3(e0,
e0) ≥ ∫_U f (p(e0))² ≥ c2 > 0 there, for a timelike vector field e0. The Killing field ∂_(φ2) = x3 ∂_4 − x4 ∂_3 has, at
points of P, e^(2ψ2) = g5(∂_(φ2), ∂_(φ2)) = x3² (g5)_(44) = ρ2² (g5)_(44), with (g5)_(44) > 0, and e^(ψ1) is bounded
near x0 since ρ1(x0) = r(x0) > 0. So T(e0, e0) = e^(−ψ1−ψ2) T3(e0, e0) ≥ c/ρ2 at the points of the geodesic near x0,
with c > 0. But Ric(g5) is continuous near x0, so Ric(g5)(e0, e0) is bounded there: a contradiction. ∎

The mechanism is the focusing of a converging beam: in a flat plane, particles moving radially inward with speed v have
a density ϱ(ρ, t) solving ∂_t ϱ − v ρ⁻¹ ∂_ρ(ρ ϱ) = 0, so ρ ϱ(ρ, t) = (ρ + v t) ϱ0(ρ + v t) and ρ ϱ → v t ϱ0(v t) > 0 as
ρ → 0 once the beam has reached the centre; particles moving along the axis (v = 0) keep their density.

### The theorem {#sec:vlasov-theorem}

Let Ω be a domain of the type [[eq:omega]], Ω = {τ0 ≤ τ ≤ τ_end, r ≥ a, v + (τ − τ_end) ≤ V + 1}, with Σ_τ := Ω ∩ {τ}
and its outer radius b(τ) := V + 1 − τ + (τ_end − τ). Let (g, F, u) be a smooth class solution on Ω of the
Einstein–restricted massless Vlasov system in label form, Ric(g) = T_V. For a compact set S ⊂ (Σ_τ0 ∩ Ω) × S¹ (points
and labels) put S_x := {α : (x, α) ∈ S}, S_α := {x : (x, α) ∈ S}, let D_α(S) be the tube of S_α for u_α
([[def:vlasov-label]]), and let 𝒟(S) be the set of the (x, α) with x ∈ D_α(S). We assume:

- (Ω) For g: each Σ_τ is spacelike; {r = a} is spacelike and r decreases along future causal curves near it;
  {v + τ = const} is spacelike and v + τ increases along future causal curves; every ray of u_α through a point of
  D_α(S), S the set of (V1), followed to the past, stays in Ω and meets Σ_τ0. These are (a)–(d) of [[lem:domain]], for
  g.
- (V1) F and u are smooth in (x, α), and there is a compact set S ⊂ (Σ_τ0 ∩ Ω) × S¹ whose interior int S, relative to
  (Σ_τ0 ∩ Ω) × S¹, contains supp q ∩ (Σ_τ0 × S¹), such that: u is an eikonal in each label, with ℓ_α future
  directed, on a neighbourhood 𝒲 of 𝒟(S) in Ω × S¹, that is g⁻¹(du_α, du_α)(x) = 0 for (x, α) ∈ 𝒲; for every x,
  α ↦ β0(x, α) is injective on S_x (the field is labelled by initial direction); ∂_α β0 ≥ b_* > 0 on S; and for
  (x0, α) ∈ S the point y_τ(x0) where the ray of u_α from x0 meets Σ_τ depends on x0 with Jacobian determinant ≥ J0 > 0
  in the coordinates (r, ϑ) of the orbit slices, for every τ with y_τ(x0) in a neighbourhood of Ω̄ (no caustic).
- (V2) dist(D_α(S), axes) ≥ 2δ > 0 for every α.
- (V3) On Σ_τ0 ∩ Ω the spheres {r = const} have positive mean curvature.

The tube D_α of supp q(·, α) ∩ Σ_τ0 lies in D_α(S), and 𝒟(S) is compact, as in [[rem:vlasov-v2]]. A neighbourhood of each
D_α(S) alone would not do: the cut-offs of [[sec:vlasov-uniform]] are smooth in (x, α), and they need the neighbourhood 𝒲
of (V1). (V3) is the first of the two signs of [[lem:constraints-evolution]] (a); the second, 𝒮 A0 > 0 for the
symmetrizer 𝒮 of [[eq:data-symmetrizer]], holds on every slice ([[lem:vlasov-symmetrizer]]).

**Theorem {#thm:vlasov}** (Restricted massless Vlasov limits.) Let (g, F, u) satisfy (Ω), (V1), (V2) and (V3). Then
there are smooth metrics g_i on Ω, invariant under T² and under both reflections, with Ric(g_i) = 0,

    g_i → g uniformly on Ω,      ∂g_i ⇀ ∂g weakly in L²(Ω).

The metric g_i is a vacuum approximation of the n_i-dust approximant of the field, along odd n_i → ∞.

No smallness of g or of the field is assumed. The properties (b) and (c) of [[lem:constraints-evolution]], no
coefficient of order λ⁻¹ and unchanged principal coefficients, are properties of the approximant's data; they are proved
in [[thm:vlasov-n-data]] for torus-polarised waves and are not hypotheses. The hypotheses are open
([[lem:vlasov-open]]), and an explicit family on Tangherlini meets them ([[prop:vlasov-nonempty]]), so the theorem
covers a nonempty open set of solutions. Radial null dusts reaching the axes, added to T_V: [[pending:issue-82-radial]].

**Remark {#rem:vlasov-v2}** ((V2) for smooth solutions.) Let (g, F, u) be smooth on Ω̄ and satisfy (Ω) and (V1), with S
disjoint from axes × S¹. Then (V2) holds for some δ > 0. Indeed, let x be a point of an axis, say {ρ2 = 0}, with
r(x) > 0. By [[lem:vlasov-axis-phases]], du_α(x) ∈ span(dτ, dr). The components of g⁻¹dτ and g⁻¹dr along ∂_3 are
g^(τ3) and (x1 g^(13) + x2 g^(23))/r at x, and those along ∂_4 are g^(τ4) and (x1 g^(14) + x2 g^(24))/r; g is invariant
under x3 ↦ −x3 (a rotation by π composed with x4 ↦ −x4) and under x4 ↦ −x4, so these components are odd in x3,
respectively x4, and vanish on the axis. So ℓ_α(x) is tangent to the axis, the axis is invariant under the flow of
ℓ_α, and by uniqueness of integral curves a ray that meets the axis lies in it at every parameter, its starting point
included. The rays start on S_α, off the axes, so the set 𝒟(S) = {(x, α) : x ∈ D_α(S)}, the image of the compact set of
(x0, α, τ) with (x0, α) ∈ S whose ray reaches Σ_τ inside Ω̄ under the continuous map (x0, α, τ) ↦ (y_τ(x0), α), is
compact and disjoint from the closed set axes × S¹, hence at positive distance from it.

**Remark {#rem:vlasov-obstructions}** (What the hypotheses avoid.) Four obstructions are proved in this chapter, and the
theorem is built so that none applies. (O1) At an axis point every invariant null phase is radial, and two of one
orientation have vanishing mixed symbol ([[lem:vlasov-axis-phases]]): the labels are kept off the axes. (O2) Under a C²
metric a continuous orbit density carries no particle to an axis transversally: it would focus there
([[prop:vlasov-axis-focus]]). (O3) Without a hierarchy of frequencies, an antipodal pair and any third phase resonate
exactly ([[lem:vlasov-resonance]]): the frequencies are 1, Λ, …, Λ^(n−1). (O4) A non-radial wave whose orbit part is a
nonzero multiple of q̂ ⊗ q̂, q̂ the unit covector of the orbit slice orthogonal to the phase's gradient, leaves a term of
order λ⁻¹ in the constraints ([[lem:vlasov-constraint-coefficient]] (c)): the waves are torus-polarised.

### Separation and coherence of the labels {#sec:vlasov-coherence}

**Lemma {#lem:vlasov-separation}** (The flow keeps the labels separated.) Assume (Ω), (V1) and (V2), and let S′ ⊂ int S
be compact. There is c0 > 0, depending on Ω, the field, S and S′ and not on any choice of labels, such that at every
point y ∈ D_α(S′) ∩ D_α′(S′)

    |g⁻¹(du_α, du_α′)(y)| ≥ c0 d(α, α′)².                                                       {#eq:vlasov-separation}

*Proof.* Let ℬ be the bundle of null directions of g3 over the orbit slices of the Σ_τ, a circle bundle. On the orbit
slices off the axes fix a smooth frame (e1, e2) orthonormal for the slice metric (by the Gram–Schmidt process from
(∂_r, ∂_ϑ)), let 𝔫 be the future unit normal of the orbit slice in (Q, g3), and describe a null direction at y by the
angle β with which a covector k on it, with g3⁻¹k future directed, is written k(𝔫) = −E, k(e1) = E cos β, k(e2) =
E sin β, E > 0. For two such covectors at y,

    g⁻¹(k, k′) = −E E′ + E E′ cos(β − β′) = −2 E E′ sin²((β − β′)/2).                    {#eq:vlasov-mixed-angle}

Let 𝔰(x0, α) := (x0, β0(x0, α)) on S, with values in ℬ over the orbit slice of Σ_τ0. It is injective, by (V1), and its
differential is triangular with determinant ∂_α β0 ≥ b_* > 0, so on int S it is an injective local diffeomorphism, hence
a diffeomorphism onto the open set 𝔰(int S). For τ ∈ [τ0, τ_end] and y in the orbit slice of Σ_τ ∩ Ω̄, let Ψ_τ(y, β) be
the point and direction in which the null geodesic of g3 through y with direction β, followed to the past, meets Σ_τ0.
It meets Σ_τ0 inside Ω̄: by (Ω) future causal curves leave Ω through its lateral boundaries, so a past causal curve from
Ω̄ does not; and τ is monotone along it. Ψ_τ is smooth, continuous in (τ, y, β), and a diffeomorphism onto its image,
its inverse being the future flow. By [[lem:vlasov-flow]] (b) the rays of u_α are null geodesics of g3, with direction
that of du_α; so if the ray of u_α from x0 ∈ S_α passes through y ∈ Σ_τ, then Ψ_τ(y, β(y; α)) = 𝔰(x0, α), β(y; α) the
angle of du_α at y.

Let 𝔇 be the compact set of (x0, α, τ) with (x0, α) ∈ S whose ray reaches Σ_τ inside Ω̄, and Φ_τ(x0, α) :=
(y_τ(x0), β(y_τ(x0); α)) = Ψ_τ⁻¹(𝔰(x0, α)) on it. det DΦ_τ = det DΨ_τ⁻¹ · ∂_α β0 is positive, the flow Ψ_τ⁻¹ depending
continuously on τ and being the identity at τ0, so det DΦ_τ ≥ c_Φ > 0 on 𝔇. Write DΦ_τ in blocks, with A := ∂y/∂x0,
B := ∂y/∂α, C := ∂β/∂x0, D := ∂β/∂α; A is invertible by (V1), with 0 < det A ≤ C_A on 𝔇. At fixed y, inverting
x0 ↦ y_τ(x0) gives x0 = x0(y, α) with ∂_α x0 = −A⁻¹B, and the angle β(y; α) = β(x0(y, α), α) has

    ∂_α β(y; α) = D − C A⁻¹ B = det DΦ_τ / det A ≥ c1 := c_Φ/C_A,

the Schur complement.

Fix τ and y ∈ Σ_τ ∩ Ω̄. On the open set B_y := {β : Ψ_τ(y, β) ∈ 𝔰(int S)} put Λ_y(β) := the label of 𝔰⁻¹(Ψ_τ(y, β)),
a smooth function; if y ∈ D_α(S′), then β(y; α) ∈ B_y and Λ_y(β(y; α)) = α. At β ∈ B_y, with (x0, α″) :=
𝔰⁻¹(Ψ_τ(y, β)) ∈ int S, whose ray reaches y, so that (x0, α″, τ) ∈ 𝔇, Λ_y is the inverse of α ↦ β(y; α) near α″, and
0 < Λ_y′(β) = 1/∂_α β(y; α″) ≤ 1/c1. Since 𝔰(S′) is a compact subset of the open set 𝔰(int S) and Ψ is uniformly
continuous on a compact neighbourhood, inside its domain, of the compact set of the (τ, y, β) with Ψ_τ(y, β) ∈ 𝔰(S′)
(the rays from S′ stay 2δ from the axes), there is ρ0 > 0 such that for every τ, y ∈ Σ_τ ∩ Ω̄ and β with Ψ_τ(y, β)
∈ 𝔰(S′), the arc of the β″ with |β″ − β| ≤ ρ0 lies in B_y.

Let y ∈ D_α(S′) ∩ D_α′(S′), β := β(y; α), β′ := β(y; α′), and δβ ∈ [0, π] their distance on the circle. Let E_* > 0 be
the minimum of E = −du_α(𝔫) over the compact set of the (y, α) with y in the closure of D_α(S); it is positive since
du_α ≠ 0 is null with g⁻¹du_α future directed. By [[eq:vlasov-mixed-angle]] and sin(t/2) ≥ t/π on [0, π], |g⁻¹(du_α,
du_α′)(y)| ≥ 2 E_*² sin²(δβ/2) ≥ 2 E_*² δβ²/π². If δβ ≥ ρ0, this is at least 2 E_*² ρ0²/π² ≥ (2 E_*² ρ0²/π⁴) d(α, α′)²,
as d(α, α′) ≤ π. If δβ < ρ0, the arc of length δβ from β to β′ lies in B_y, Λ_y maps its ends to α and α′, and Λ_y′ ≤
1/c1 on it, so d(α, α′) ≤ δβ/c1 and the bound is at least (2 E_*² c1²/π²) d(α, α′)². So [[eq:vlasov-separation]] holds
with c0 := (2 E_*²/π²) min(c1², ρ0²/π²). The injectivity of β0(x, ·) is used in the definition of Λ_y, which needs 𝔰
injective. ∎

For the n labels α_A := 2πA/n, d(α_A, α_B) ≥ 2π/n, so the dusts sampled at them are pairwise separated with constant
c0 (2π/n)² on the overlaps of the tubes D_(α_A)(S′). This is the separation η′ ≳ 1/n² of [HL25, Lemma 4.15, p. 18]; for
n directions 2πA/n on the flat orbit space with unit energies the least mixed symbol is exactly 1 − cos(2π/n), and
n²(1 − cos(2π/n)) → 2π².

Pairwise separation is not enough for the scheme of [[thm:vlasov-n-approximant]]. At stage m its residual carries the
harmonics e^(i j·θ) with |j|₁ ≤ m + 2, and a harmonic with two or more nonzero entries is removed by division by

    Q_j := g⁻¹(𝔎_j, 𝔎_j),      𝔎_j := Σ_A j_A ν_A du_A,                                           {#eq:vlasov-symbol}

ν_A the frequency of family A.

**Lemma {#lem:vlasov-resonance}** (An exact resonance.) In 2+1-dimensional Minkowski space let k_a, k_b be future null
covectors of equal energy with antipodal spatial directions, and k_c any future null covector of that energy. Then
𝔎 := k_a + k_b − k_c is null. So with equal frequencies the mixed harmonic e^(i(θ_a + θ_b − θ_c)) is exactly resonant,
whatever the pairwise separations.

*Proof.* In an orthonormal frame, k_a = E(−1, e), k_b = E(−1, −e), k_c = E(−1, f), with e, f unit vectors. Then 𝔎 =
E(−1, −f), and g⁻¹(𝔎, 𝔎) = E²(−1 + 1) = 0. ∎

**Lemma {#lem:vlasov-hierarchy}** (Coherence under a hierarchy of frequencies.) Let k_1, …, k_n be covectors at a point
of a 2+1-dimensional Lorentzian space with g⁻¹(k_A, k_A) = 0, |g⁻¹(k_A, k_B)| ≥ c > 0 for A ≠ B, and |k_A| ≤ Ē in an
orthonormal frame. Let Λ > 1 and ν_A := Λ^(A−1). For every j ∈ ℤⁿ with at least two nonzero entries and |j|₁ ≤ m, let B1
and B2, B1 > B2, be its two largest indices with nonzero entries. Then

    |g⁻¹(𝔎_j, 𝔎_j)| ≥ 2 ν_B1 ν_B2 (c − m Ē²/Λ − m² Ē²/(2Λ)),      𝔎_j := Σ_A j_A ν_A k_A.  {#eq:vlasov-hierarchy}

In particular every such combination is non-null, with this margin, once Λ > (m + m²/2) Ē²/c.

*Proof.* In the orthonormal frame |g⁻¹(k, k′)| ≤ |k| |k′|. Put 𝔎 := 𝔎_j = j_B1 ν_B1 k_B1 + V, V := Σ_(A ≠ B1) j_A ν_A
k_A. Since k_B1 is null, g⁻¹(𝔎, 𝔎) = 2 j_B1 ν_B1 g⁻¹(k_B1, V) + g⁻¹(V, V). Here g⁻¹(k_B1, V) = j_B2 ν_B2 g⁻¹(k_B1,
k_B2) + Σ_(A < B2) j_A ν_A g⁻¹(k_B1, k_A), and ν_A ≤ ν_B2/Λ for A < B2, so |g⁻¹(k_B1, V)| ≥ ν_B2 (c − m Ē²/Λ),
using |j_B2| ≥ 1 and Σ|j_A| ≤ m. Further |V| ≤ Σ_(A ≤ B2) |j_A| ν_A Ē ≤ m ν_B2 Ē, so |g⁻¹(V, V)| ≤ m² Ē² ν_B2² ≤ m² Ē²
ν_B1 ν_B2/Λ. With |j_B1| ≥ 1, |g⁻¹(𝔎, 𝔎)| ≥ 2 ν_B1 ν_B2 (c − m Ē²/Λ) − m² Ē² ν_B1 ν_B2/Λ, which is
[[eq:vlasov-hierarchy]]. ∎

With c = c0 (2π/n)², Λ is of order n², as in the choice a_A = c n² a_(A−1) of [HL25, Lemma 4.16, p. 18]. The phases ν_A
u_A are eikonals, so the two-scale scheme is unchanged; the wave of family A carries the amplitude λ F_A/ν_A, so that its
derivatives are of the size of F_A ([[eq:vlasov-wave]]).

**Remark {#rem:vlasov-coherence-values}** (Numerical observation.) On the orbit space of Tangherlini with μ = 1 and
labels in [−0.6, 0.6], the Schur formula of [[lem:vlasov-separation]] agreed with shooting to 1.1 × 10⁻⁹, ∂_α β was at
least 0.798, and the least mixed symbol of adjacent labels divided by (Δα)² was 0.2923, 0.2926, 0.2927, 0.2927 at n = 8,
16, 32, 64. For the four labels 2πA/4 on flat 2+1 with the hierarchy, every Q_j with |j|₁ ≤ 5 satisfied
exactly |Q_j|/(ν_B1 ν_B2) ≥ 359/216. No proof uses these values.

### Torus-polarised waves and the orbit space {#sec:vlasov-polarisation}

A wave of a non-radial family cannot be the wave W_TT of [[sec:waves]], which is adapted to radial phases. We take
it on the torus.

**Definition {#def:vlasov-torus-wave}** (Torus-polarised waves.) Let u be an invariant phase and ξ1, ξ2 invariant
functions. The *torus wave* of amplitudes (ξ1, ξ2) changes a class metric [[eq:vlasov-class]] by

    ψ_i ↦ ψ_i0 + λ ξ_i cos θ,      θ := u/λ,      g3 unchanged,

so that (g5)_(φiφi) = e^(2ψ_i0) e^(2λ ξ_i cos θ). It is *torus-polarised* if ξ2 = −ξ1 =: −ξ: it oscillates only in
ψ2 − ψ1, so that ψ is unchanged and ω ↦ ω − λ ξ cos θ.

**Lemma {#lem:vlasov-torus-ricci}** (Torus waves in the field equations.) In the setting of [[def:vlasov-torus-wave]] put
Ξ := ξ1 + ξ2, ψ0 := ψ10 + ψ20 and E_i := −R_(ii)/(g5)_(φiφi). In the two-scale expansion in λ:

(a) the coefficient of λ⁻¹ in Ric(g5)_(ab) is Ξ cos θ ∂_a u ∂_b u, and Ric(g5)_(aφi) = Ric(g5)_(φ1φ2) = 0;

(b) the coefficient of λ⁻¹ in E_i is −ξ_i |du|² cos θ;

(c) the coefficient of sin θ in the part of order λ⁰ of E_i is −(2⟨dξ_i, du⟩ + ξ_i(□3 u + ⟨du, dψ0⟩) + Ξ ⟨dψ_i0, du⟩);

(d) the terms of order λ⁰ quadratic in the oscillation have mean −½(ξ1² + ξ2²) du ⊗ du in Ric(g5)_(ab), and, for u
null, mean zero in E_i.

Hence, for u null and ξ2 = −ξ1, the whole part of order λ⁻¹ of Ric(g5) vanishes with g3 unperturbed. If the
coefficients (c) vanish for i = 1, 2, as the vacuum equations at order λ⁰ require, their sum is the homogeneous
transport

    2 ℓ(Ξ) + Ξ (□5 u + ℓ(ψ0)) = 0,      ℓ := g3⁻¹du,                                            {#eq:vlasov-xi-transport}

so Ξ = 0 on Σ_τ0 gives Ξ = 0 along every generator that reaches Σ_τ0: the torus polarisation is kept. The torus-polarised
wave of amplitude ξ contributes the mean ξ² du ⊗ du to the mean metric's Ricci tensor, so it realises every density
F² = ξ².

*Proof.* By [[lem:warped-ricci]], with A = ψ1 and B = ψ2,

    Ric(g5)_(ab) = Ric[g3]_(ab) − Σ_i (∇_a∇_b ψ_i + ∂_a ψ_i ∂_b ψ_i),      E_1 = □3 ψ1 + |dψ1|² + ⟨dψ1, dψ2⟩,

E_2 likewise, and the mixed components vanish. With the two-scale derivative, ∂_a ψ_i = ∂_a ψ_i0 + λ ∂_a ξ_i cos θ −
ξ_i sin θ ∂_a u. (a) Only ∇_a∇_b ψ_i has a term of order λ⁻¹, the fast derivative of −ξ_i sin θ ∂_a u, which is
−λ⁻¹ ξ_i cos θ ∂_a u ∂_b u; so the coefficient is (ξ1 + ξ2) cos θ ∂_a u ∂_b u. (b) In □3 ψ_i the same term traced is
−λ⁻¹ ξ_i cos θ |du|², and |dψ_i|², ⟨dψ1, dψ2⟩ are of order one. (c) In □3 ψ1 the terms of order λ⁰ in sin θ are
∇^a(λ ∂_a ξ1 cos θ) ⊃ −sin θ ⟨dξ1, du⟩ and ∇^a(−ξ1 sin θ ∂_a u) ⊃ −sin θ (⟨dξ1, du⟩ + ξ1 □3 u). In |dψ1|² they are
−2 ξ1 sin θ ⟨dψ10, du⟩, and in ⟨dψ1, dψ2⟩ they are −sin θ (ξ2 ⟨dψ10, du⟩ + ξ1 ⟨dψ20, du⟩). The sum is
−sin θ (2⟨dξ1, du⟩ + ξ1(□3 u + ⟨du, dψ0⟩) + Ξ ⟨dψ10, du⟩); E_2 is the same with the indices exchanged. (d) The fast
parts of ∂_a ψ_i ∂_b ψ_i are ξ_i² sin²θ ∂_a u ∂_b u, of mean ½ ξ_i² ∂_a u ∂_b u; in E_i the quadratic fast terms are
multiples of |du|². For the consequences: with u null and Ξ = 0, (a) and (b) vanish. Summing (c) over i gives
−(2 ℓ(Ξ) + Ξ(□3 u + 2 ℓ(ψ0))), and □3 u + ℓ(ψ0) = □5 u up to O(λ) by [[eq:vlasov-box]], which is
[[eq:vlasov-xi-transport]]; a linear homogeneous transport along ℓ keeps zero data. For ξ1 = −ξ2 = ξ the mean in (d) is
−ξ² du ⊗ du, and the vacuum equation at order λ⁰, averaged, gives Ric of the mean metric equal to ξ² du ⊗ du. The other
terms of order λ⁰ are linear in an oscillating profile or are θ-derivatives, so they have mean zero. ∎

The quadratic term of (d) has, besides its mean, a second harmonic in θ, which no term of order λ² can remove (its
symbol vanishes on harmonics of the null phase u alone, [[lem:two-dust-nonresonance]]); as for the waves of
[[thm:two-dusts]] ([[eq:two-dust-waves]]), it is removed by a gauge term of order λ along du ⊗ du, transported along the
generator. In the two-scale scheme the wave is the linear part of the torus-polarised wave plus that term.

**Definition {#def:vlasov-wave}** (The wave of a dust.) Let g0 be a class metric, u an invariant eikonal of g0 with ℓ :=
g0⁻¹du future directed, F ≥ 0 an invariant amplitude transported by [[eq:vlasov-amplitude]] (with u in place of u_α),
and ν > 0 a frequency; put ξ := F/ν and k := ν du. The *wave* of the dust (u, F) at frequency ν is the profile in
(X, θ)

    W := 2 ξ cos θ (e^(2ψ1) dφ1² − e^(2ψ2) dφ2²) + χ k ⊗ k,      χ := ½ c sin 2θ,                     {#eq:vlasov-wave}

where c solves ν (ℓ(c) + ½ (□5 u) c) = ξ² along the generators, with c = 0 on Σ_τ0. Its first term is the part of
order λ of the torus-polarised wave of amplitude ξ at the phase θ = ν u/λ; its second, χ k ⊗ k, is its *gauge part*,
which vanishes on Σ_τ0 with all its θ-derivatives.

**Lemma {#lem:vlasov-wave}** (The wave of a dust at order λ⁰.) In the setting of [[def:vlasov-wave]], W(ℓ, ·) = 0 and
tr_(g0) W = 0, and in the two-scale expansion of R[g0 + λ W] at the phase θ = ν u/λ (the reduced Ricci tensor relative to
g0, computed with ∂_a + λ⁻¹ ν ∂_a u ∂_θ), R^(−1) = 0 and

    R^(0) = Ric(g0) − F² du ⊗ du.                                                                    {#eq:vlasov-wave-r0}

*Proof.* The first term of W has torus components only and ℓ is an orbit vector, and (k ⊗ k)(ℓ, ·) = ν² g0⁻¹(du, du)
du = 0; tr_(g0) W = 2 ξ cos θ (e^(−2ψ1) e^(2ψ1) − e^(−2ψ2) e^(2ψ2)) + χ g0⁻¹(k, k) = 0. The proof of
[[lem:leading-coefficient]] uses of the background only that the phase is null and has gradient ℓ, and of the wave only
W(ℓ, ·) = 0 and tr W = 0 (as in the proof of [[lem:two-dust-stage-zero]] (b)); applied with v replaced by ν u, dv by k
and ℓ by ν ℓ, it gives R^(−1) = 0 and

    R^(0) = Ric(g0) − ν ∇_ℓ ∂_θ W − ½ ν (□5 u) ∂_θ W − ¼ |∂_θ W|² k ⊗ k.

For the Killing field K_i := ∂_(φi), the Christoffel symbols of [[lem:warped-ricci]] give ∇_ℓ K_i = ∇_(K_i) ℓ = ℓ(ψi)
K_i (ℓ is invariant, so it commutes with K_i), hence ∇_ℓ K_i♭ = ℓ(ψi) K_i♭, and e^(2ψi) dφi² = e^(−2ψi) K_i♭ ⊗ K_i♭ has
∇_ℓ (e^(2ψi) dφi²) = (−2 ℓ(ψi) + 2 ℓ(ψi)) e^(−2ψi) K_i♭ ⊗ K_i♭ = 0. Also ∇_ℓ du = ½ d(g0⁻¹(du, du)) = 0. With T0 :=
e^(2ψ1) dφ1² − e^(2ψ2) dφ2², ∂_θ W = −2 ξ sin θ T0 + c cos 2θ k ⊗ k, so

    ν ∇_ℓ ∂_θ W + ½ ν (□5 u) ∂_θ W = −2 ν sin θ (ℓ(ξ) + ½ (□5 u) ξ) T0 + ν (ℓ(c) + ½ (□5 u) c) cos 2θ k ⊗ k
                                   = ξ² cos 2θ k ⊗ k,

the first term vanishing because ξ = F/ν is transported by [[eq:vlasov-amplitude]], and the second by the choice of c.
Further |∂_θ W|² = 4 ξ² sin²θ |T0|² = 8 ξ² sin²θ, since |T0|² = e^(−4ψ1) e^(4ψ1) + e^(−4ψ2) e^(4ψ2) = 2, T0 and k ⊗ k
are orthogonal (T0(ν ℓ, ν ℓ) = 0) and |k ⊗ k|² = g0⁻¹(k, k)² = 0. So R^(0) = Ric(g0) − ξ² (cos 2θ + 2 sin²θ) k ⊗ k =
Ric(g0) − ξ² ν² du ⊗ du = Ric(g0) − F² du ⊗ du. ∎

The constraints on Σ_τ0 need the same cancellation, now for a phase that is not radial on a slice that is not round. On
Σ_τ0 write the data of a class metric as (γ, κ), the induced metric and the second fundamental form, and let Φ(γ, κ) :=
(ρ, J), ρ := R(γ) − |κ|² + (tr κ)², J := 2(−div κ + d tr κ), be the constraint map ([[eq:data-constraint-map]]). Let the
data oscillate as

    γ = γ0 + λ W(x, θ) + O(λ²),      κ = κ0 + κ1(x, θ) + O(λ),      θ = u/λ,      p := d(u|Σ_τ0) ≠ 0,

with profiles 2π-periodic in θ, where O(λ²) and O(λ) stand for λ² and λ times profiles. Write W″ := ∂_θ² W and κ1′ :=
∂_θ κ1, raise indices and take contractions with γ0, and put ⟨h, p ⊗ W″p⟩ := h^(ij) p_i W″_(jk) p^k.

**Lemma {#lem:vlasov-constraint-coefficient}** (The constraints' coefficient of order λ⁻¹.) (a) For slow h and k, the
coefficient of λ⁻¹ in the linearisation DΦ(γ, κ)[h, k] is

    dρ⁽⁻¹⁾ = −2 ⟨h, p ⊗ W″p⟩ + h(p, p) tr W″ + |p|² ⟨h, W″⟩,
    dJ_i⁽⁻¹⁾ = 2 (h^(jl) p_l κ1′_(ji) − p_i h^(jl) κ1′_(jl)).                         {#eq:vlasov-constraint-coefficient}

It is linear in (W, κ1) and does not involve k. With n families present at once, γ = γ0 + λ Σ_A W_A(x, θ_A) + λ²(…)
and κ = κ0 + Σ_A κ1_A(x, θ_A) + λ(…), the coefficient of λ⁻¹ is the sum over A of [[eq:vlasov-constraint-coefficient]]
for (W_A, κ1_A, p_A), and the second and mixed harmonics of order λ² in γ, of order λ in κ, enter at order λ⁰.

(b) For torus-polarised waves, W_A = 2 ξ_A cos θ_A (e^(2ψ10) dφ1² − e^(2ψ20) dφ2²) and κ1_A = z_A sin θ_A (e^(2ψ10)
dφ1² − e^(2ψ20) dφ2²), the part of order λ⁻¹ of Φ(γ + h, κ + k) vanishes for every slow h without torus components and
every slow k. In particular the corrections of [[lem:constraints-evolution]], which change γ by multiples of dr ⊗ dr,
meet no coefficient of order λ⁻¹. More precisely, the terms of Φ(γ + h, κ + k) that carry a second derivative of a
λ W_A or a first derivative of a κ1_A, which are those of order λ⁻¹, are, at every point and for every h without torus
components and every k, slow or not, −λ⁻¹ Σ_A |p_A|² tr W_A″ in ρ and 2 λ⁻¹ Σ_A p_A tr κ1_A′ in J, |p_A|² taken with
the inverse of γ + h and the traces in the torus block of γ, which h does not change; these traces are O(λ), so the
terms are of order one.

(c) For a wave with an orbit part, W = cos θ (ζ q̂ ⊗ q̂ + W_T) with q̂ the γ0-unit covector of the orbit slice orthogonal
to p, ζ ≠ 0, W_T with torus components only and tr W = 0 (for instance W_T = −½ ζ (e^(2ψ10) dφ1² + e^(2ψ20) dφ2²)),
and h = c dr ⊗ dr, dρ⁽⁻¹⁾ = −c ζ |p|² cos θ ⟨dr, q̂⟩², which is not zero where c ≠ 0 and the phase is not radial (p not
parallel to dr). So every non-radial wave whose orbit part is a nonzero multiple of q̂ ⊗ q̂ leaves a term of order λ⁻¹.

*Proof.* (a) Terms of order λ⁻¹ arise only where two derivatives fall on λ W, or one on κ1. In R(γ) = γ^(ij)(∂_k
Γ^k_ij − ∂_j Γ^k_ik) + ΓΓ the second derivatives of γ enter as γ^(ij) γ^(kl)(∂_i∂_k γ_jl − ∂_i∂_j γ_kl), and ∂_i∂_k(λ
W) = λ⁻¹ p_i p_k W″ + O(1), while ΓΓ is of order one. So the part of order λ⁻¹ of R(γ) is W″(p^♯, p^♯) − |p|² tr W″,
with p^♯ := γ⁻¹p and the inverse of the full γ. Varying γ ↦ γ + εh, so that γ^(ij) ↦ γ^(ij) − ε h^(ij), gives the first
line of [[eq:vlasov-constraint-coefficient]]; the remaining terms of DR[h], which carry derivatives of h or first
derivatives of γ, are of order one. In J, −div κ ⊃ −γ^(jl) ∂_l κ_(ji) and d tr κ ⊃ ∂_i(γ^(jl) κ_(jl)), whose parts of
order λ⁻¹ are −γ^(jl) p_l κ1′_(ji) and p_i γ^(jl) κ1′_(jl); varying γ gives the second line; the Christoffel terms are
of order one. The terms −|κ|² + (tr κ)² have no term of order λ⁻¹, and no term of order λ⁻¹ depends on k. With several
phases the fast derivatives of λ W_A(x, θ_A) give λ⁻¹ p_A p_A W_A″ and the cross terms vanish, each W_A depending on one
phase; ∂²(λ² M(x, θ_A ± θ_B)) is of order one, and ∂(λ(…)) is of order one.

(b) The terms of R(γ + h) and J(γ + h, κ + k) that carry a second derivative of λ W or a first derivative of κ1 are,
by the proof of (a) and up to terms of order one, λ⁻¹ (W″(p^♯, p^♯) − |p|² tr W″) and 2 λ⁻¹ (−γ_h^(jl) p_l κ1′_(ji) +
p_i γ_h^(jl) κ1′_(jl)), with the inverse γ_h⁻¹ of γ + h. Since γ0 and h have no mixed
orbit–torus components, γ_h⁻¹ is block-diagonal and p^♯ is an orbit vector, while W″ and κ1′ have torus components only.
So W″(p^♯, ·) = 0 and γ_h^(jl) p_l κ1′_(ji) = 0, and what remains is −λ⁻¹ |p|² tr W″ and 2 λ⁻¹ p tr κ1′, with the
traces in the torus block of γ + h, which is that of γ. That block is γ0's, diag(e^(2ψ10), e^(2ψ20)), plus λ Σ_B W_B and
terms of order λ², so tr W″ = −2ξ cos θ (e^(−2ψ10) e^(2ψ10) − e^(−2ψ20) e^(2ψ20)) + O(λ) = O(λ), and likewise tr κ1′ =
O(λ): these terms are λ⁻¹ O(λ), of order one, and the coefficient of λ⁻¹ vanishes. The corrections of
[[lem:constraints-evolution]] change γ by a multiple of dr ⊗ dr only. The argument is pointwise and algebraic in h and
k: the terms that carry a second derivative of λ W_A or a first derivative of κ1_A are those displayed, with the inverse
of γ + h, and they are of order one wherever γ + h is block-diagonal, whatever the derivatives of h.

(c) Here W″ = −W, W″p = 0 because q̂ ⊥ p and the torus block annihilates p, and tr W″ = −tr W = 0. So dρ⁽⁻¹⁾ = |p|² ⟨h,
W″⟩ = −c |p|² W(γ0⁻¹dr, γ0⁻¹dr) = −c ζ |p|² cos θ ⟨dr, q̂⟩², since γ0⁻¹dr is an orbit vector, on which W_T vanishes. In
the two-dimensional orbit slice ⟨dr, q̂⟩ = 0 exactly when dr is parallel to p. ∎

**Lemma {#lem:vlasov-leaf-curvature}** (The principal coefficients do not oscillate.) At data of the form of
[[lem:vlasov-constraint-coefficient]] with torus-polarised waves W_A and with second and mixed harmonics of order λ² in
γ, the principal coefficients of the constraint map in the unknowns of [[lem:constraints-evolution]] have no oscillating
part of order λ⁰: the coefficient (γ^(rr))^(3/2) H of the radial derivative of the metric unknown in ρ ([[eq:data-rho]]),
those of its angular second derivatives, and those of the first derivatives of the momentum unknowns in J, and the
symmetrizer 𝒮 of [[eq:data-symmetrizer]]. Their parts of order λ⁰ are those of γ0's data, so each of them is its value at
the data (γ0, κ0) plus λ times a smooth function of x, of the phases θ_A and of λ, also as functions of the metric
unknown α. For a wave with a trace on the spheres, ξ2 = ξ1, the mean curvature H oscillates at order λ⁰.

*Proof.* The coefficients of the angular second derivatives of the metric unknown in ρ and of the first derivatives of
the momentum unknowns in J, and 𝒮, involve γ, its inverse, Π and α, undifferentiated ([[lem:constraints-evolution]]
(a)), and γ = γ0 + λ (…), the dots a polynomial in λ with profile coefficients. In (γ^(rr))^(3/2) H, γ^(rr) is
undifferentiated, and H = H̃/ν with H̃ = ½ tr_Π(∂_r Π − 𝓛_σ Π). The torus directions are tangent to the spheres. The
shift σ is Π⁻¹ applied to the components γ_(rB), and its part of order λ vanishes: with Π = Π0 + λ Σ_A W_A + O(λ²), it
is −λ Π0⁻¹(Σ_A W_A(σ0, ·)), σ0 the shift of γ0, and the W_A have torus components only while σ0 is an orbit vector.
So σ = σ0 + O(λ²). Hence the part of order λ⁰ of ∂_r Π − 𝓛_σ Π is that of γ0 plus the oscillating part
Σ_A ν_A (∂_r u_A − σ0^C ∂_C u_A) ∂_(θ_A) W_A (𝓛_(σ0) differentiates λ W_A along the spheres, where the phase is not
constant), and Π^(AB) = Π0^(AB) + O(λ), so the part of order λ⁰ of H̃ is H̃0 plus ½ Σ_A ν_A (∂_r u_A − σ0^C ∂_C u_A)
∂_(θ_A) tr W_A = 0, the torus-polarised W_A being traceless. The harmonics of order λ² contribute O(λ) to first
derivatives, and so does the oscillating part of the shift, which is of order λ². The metric unknown enters these
coefficients only through ν_U² = ν² + α and γ_U⁻¹, algebraically, so the same holds as functions of α. If ξ2 = ξ1,
tr W_A = 4 ξ1 cos θ_A + O(λ) and H̃ acquires −2 ξ1 ν_A (∂_r u_A − σ0^C ∂_C u_A) sin θ_A at order λ⁰. ∎

Next the commutator of the wave operator with a generator, which the uniform estimate needs for each family. For a
radial family on a round background it is [[lem:two-dust-commutator]], whose proof uses that the generator is
shear-free. A non-radial family on a non-round background is not shear-free in five dimensions, but its shear lives
in the torus directions, where the Hessian of an invariant function is of first order, and in the orbit space it has
no shear.

**Lemma {#lem:vlasov-no-shear}** (No shear in the orbit space.) Let u be a function on a 2+1-dimensional Lorentzian
manifold (Q, g3) with |du|² = 0 to first order at a point, du ≠ 0 there, and ℓ := g3⁻¹du. Then for every symmetric
bilinear form S with S(ℓ, ·) = 0 at that point,

    ⟨Hess u, S⟩ = (□3 u) tr S.                                                                  {#eq:vlasov-no-shear}

So 𝔣(S) := ⟨Hess u, S⟩ − (□3 u) tr S depends only on S(ℓ, ·). In a null frame (ℓ, ℓ̄, e), g3(ℓ, ℓ̄) = −1, e a unit
vector orthogonal to both, with H := Hess u (not the mean curvature),

    𝔣(S) = H(ℓ̄, ℓ̄) S(ℓ, ℓ) − 2 H(ℓ̄, e) S(ℓ, e) + 2 H(e, e) S(ℓ, ℓ̄).                           {#eq:vlasov-shear-form}

*Proof.* H(ℓ, X) = ½ X(|du|²) = 0 for every X at the point, since |du|² vanishes to first order. In the frame, g3⁻¹ = −ℓ
⊗ ℓ̄ − ℓ̄ ⊗ ℓ + e ⊗ e. In ⟨H, S⟩ = g3^(ik) g3^(jl) H_(ij) S_(kl) only the components of H on ℓ̄ and e enter, and the
inverse metric pairs ℓ̄ with ℓ (with the sign −1) and e with e, so ⟨H, S⟩ = H(ℓ̄, ℓ̄) S(ℓ, ℓ) − 2 H(ℓ̄, e) S(ℓ, e) + H(e,
e) S(e, e). Further tr S = −2 S(ℓ, ℓ̄) + S(e, e) and □3 u = −2 H(ℓ, ℓ̄) + H(e, e) = H(e, e). Subtracting (□3 u) tr S
gives [[eq:vlasov-shear-form]], which vanishes when S(ℓ, ·) = 0. ∎

In 3+1 dimensions the transverse space of ℓ is two-dimensional, and ⟨H, S⟩ on it is not a multiple of the trace: the
shear of the generator enters. This is why the orbit space of the class, of dimension 2+1, is what makes the next
corollary hold.

**Corollary {#cor:vlasov-commutator}** (The commutator with a non-radial generator.) Let u be an invariant eikonal of a
class metric g5, ℓ := g5⁻¹du = g3⁻¹du and L := ℓ·∂. For every invariant function φ,

    [□5, L] φ = a □5 φ + 𝔐(L φ) + 𝔑 φ,      a := 2 □3 u,                                          {#eq:vlasov-commutator}

with 𝔐 and 𝔑 first-order operators whose coefficients are smooth off the axes where u is (𝔑 contains ⟨dψ_i, du⟩
⟨dψ_i, dφ⟩); the same holds for □̃ := g5^(ab) ∂_a∂_b in the chart X, with another 𝔑. On a round background with u = v,
a = 2 L(R)/R, the coefficient of [[lem:two-dust-commutator]].

*Proof.* For any metric, [□, ℓ^μ ∇_μ] φ = 2 ⟨∇ℓ, Hess φ⟩ + (□ℓ^μ + Ric^μ_ν ℓ^ν) ∂_μ φ, and ∇ℓ = Hess_(g5) u. For
invariant functions the Christoffel symbols of [[lem:warped-ricci]] give Hess_(g5) f(∂_a, ∂_b) = Hess_(g3) f(∂_a, ∂_b),
Hess_(g5) f(∂_a, ∂_(φi)) = 0 and Hess_(g5) f(∂_(φi), ∂_(φi)) = e^(2ψi) ⟨dψ_i, df⟩, of first order in f. So
⟨Hess_(g5) u, Hess_(g5) φ⟩ = ⟨Hess_(g3) u, Hess_(g3) φ⟩ + Σ_i ⟨dψ_i, du⟩ ⟨dψ_i, dφ⟩. Apply [[eq:vlasov-shear-form]] with
S := Hess_(g3) φ: S(ℓ, X) = X(Lφ) − Hess_(g3) u(X, ∇φ), so ⟨Hess_(g3) u, Hess_(g3) φ⟩ = (□3 u) □3 φ + 𝔐′(Lφ) + (first
order in φ), with 𝔐′ := H(ℓ̄, ℓ̄) ℓ − 2 H(ℓ̄, e) e + 2 H(e, e) ℓ̄ for any smooth null frame. Finally □3 φ = □5 φ −
⟨dψ, dφ⟩ by [[eq:vlasov-box]]. This gives [[eq:vlasov-commutator]] with 𝔐 := 2𝔐′. For □̃, □̃φ = □5 φ + H0·∂φ with
H0^ρ := g5^(ab) Γ^ρ_ab smooth, and [L, H0·∂] is of first order. On a round background g3 = −2 e^(2σ) du dv + R² dϑ² in
double-null coordinates, √|g3| = e^(2σ) R and g3^(uv) = −e^(−2σ), so □3 v = −e^(−2σ) R_u/R = L(R)/R. ∎

So if ℓ_A·dφ = f along the generator of family A, then Ψ := □̃φ satisfies L_A Ψ + a_A Ψ = □̃f − 𝔐_A(f) − 𝔑_A φ, the
form [[eq:ue-psi]] that the uniform estimate uses, with a_A = 2 □3 u_A.

### The constraints in scaled norms {#sec:vlasov-scaled}

The data of [[thm:vlasov-n-data]] are corrected by solving the constraints outward in r, as in [[sec:data-evolution]].
There the phase on the initial slice is radial, angular derivatives of the coefficients cost nothing, and
[[lem:linear-evolution]] applies with constants independent of λ. Here the phases ν_A u_A have angular gradients on the
slice, the j-th angular derivative of a coefficient is of size λ^(−j), and the constant of [[lem:linear-evolution]] grows
as λ → 0. We solve the constraints with bounds uniform in λ in norms in which every angular derivative carries a factor
λ. Two features make this possible: the principal coefficients oscillate only at order λ
([[lem:vlasov-leaf-curvature]]), so that their first derivatives are bounded; and the norm of the metric unknown α counts
its first two angular derivatives without the factor λ, which balances the coupling of α and (ϖ, q) through ∂_r α in J
and through (ϖ, q) in ρ. The section is used for the oscillating data of [[thm:vlasov-n-data]] and, with λ = 1 and no
phases, for the data of [[prop:vlasov-uniform-n]].

*Setting.* As in [[sec:data-evolution]], Σ := Σ_τ0 ∩ Ω = [a, b1] × S³ with b1 := b(τ0) and coordinates (r, ω), the data
are (γ, κ), the unknowns are U = (α, w) with w := (ϖ, q), q a covector with q(γ⁻¹dr) = 0 identified with its angular
components, a 1-form on S³ depending on r, and (γ_U, κ_U) is [[eq:data-u]]. Let E := ℝ ⊕ T*S³ be the bundle in which w
lies, with the fibre metric of the round S³; ∇, Δ and |·| are the Levi-Civita connection, the Laplacian and the
pointwise norms of the round S³, and ‖·‖ is the L²(S³) norm. Let X_1, …, X_6 be the Killing fields x_a ∂_b − x_b ∂_a
(a < b) of the round S³ ⊂ ℝ⁴, independent of r, and 𝓛_i the Lie derivative along X_i, acting on functions, sections of
E and tensor fields on S³. For a word I = (i_1, …, i_j) put 𝓛^I := 𝓛_(i_1)⋯𝓛_(i_j) and |I| := j. We use four facts.

(K1) Each 𝓛_i commutes with ∇, with Δ, with contractions by the round metric and with ∂_r (X_i is a Killing field).

(K2) Σ_i ⟨X_i, Υ⟩² = |Υ|² for every tangent vector Υ of S³, by Lagrange's identity: with |x| = 1 and x·Υ = 0,
Σ_(a<b) (x_a Υ_b − x_b Υ_a)² = |x|² |Υ|² − (x·Υ)² = |Υ|²; so Υ = Σ_i ⟨X_i, Υ⟩ X_i. Since 𝓛_i f − ∇_(X_i) f is of order
zero in f with coefficients built from ∇X_i, it follows that |∇f| ≤ C (Σ_i |𝓛_i f| + |f|), |∇² f| ≤ C Σ_(|J|≤2) |𝓛^J f|
and |𝓛_i f| ≤ C (|∇f| + |f|) for every function, section of E or tensor field f.

(K3) sup |f| ≤ C_S Σ_(|J|≤2) ‖𝓛^J f‖, by (K2) and the embedding of H² in the continuous functions on the compact
three-manifold S³ ([[thm:std-bh-manifold]]).

(K4) For a pointwise bilinear operation f · g built from the round metric (a product or a contraction), 𝓛^I (f · g) =
Σ (𝓛^(I′) f) · (𝓛^(I″) g), the sum over the 2^|I| ways of splitting the letters of I into two words I′, I″, each keeping
the order of I.

*Norms.* For 0 < λ ≤ 1, an integer j ≥ 0 and f on S³,

    ‖f‖_(j) := (Σ_(|I|≤j) λ^(2|I|) ‖𝓛^I f‖²)^(1/2),      ‖f‖_(j),∞ := Σ_(|I|≤j) λ^|I| sup |𝓛^I f|,

and, for the function α, ‖α‖_(j;1) and ‖α‖_(j;2) are defined in the same way with ‖𝓛^I α‖² replaced by ‖𝓛^I α‖² +
‖∇𝓛^I α‖², respectively by ‖𝓛^I α‖² + ‖∇𝓛^I α‖² + ‖∇²𝓛^I α‖². On [a, r] ⊂ [a, b1] put

    ‖U‖_(𝒴_j(a,r)) := sup_([a,r]) (‖α‖_(j;1) + ‖w‖_(j))
                       + (∫_a^r (‖α‖²_(j;2) + ‖∂_r α‖²_(j)) dr′)^(1/2),                          {#eq:vlasov-scaled-norm}

and ‖U‖_(𝒴_j) := ‖U‖_(𝒴_j(a,b1)). With constants depending on j only, (K1)–(K3) give

    (N1) ‖f‖_(j),∞ ≤ C λ⁻² ‖f‖_(j+2);   (N2) ‖α‖_(j),∞ ≤ C λ⁻¹ ‖α‖_(j+1;1);   (N3) λ ‖∇f‖_(j) ≤ C ‖f‖_(j+1);
    (N4) ‖∇α‖_(j) ≤ ‖α‖_(j;1),  ‖∇²α‖_(j) ≤ ‖α‖_(j;2).

Indeed, by (K3), λ^|I| sup |𝓛^I f| ≤ C_S Σ_(|J|≤2) λ^(−|J|) λ^(|I|+|J|) ‖𝓛^J 𝓛^I f‖, which gives (N1); for (N2), (K2)
bounds ‖𝓛^J 𝓛^I α‖ for |J| ≤ 2 by C (‖𝓛^I α‖ + ‖∇𝓛^I α‖ + Σ_i (‖𝓛_i 𝓛^I α‖ + ‖∇𝓛_i 𝓛^I α‖)); (N3) is (K2) applied to 𝓛^I
f; and (N4) holds because ∇ and ∇² commute with 𝓛^I (K1). By (K4), λ^|I| = λ^|I′| λ^|I″| and the fact that one
of |I′|, |I″| is at most ⌊j/2⌋,

    (P1) ‖f · g‖_(j) ≤ C ‖f‖_(j),∞ ‖g‖_(j);      (P2) ‖f · g‖_(j) ≤ C (‖f‖_(⌊j/2⌋),∞ ‖g‖_(j) + ‖f‖_(j) ‖g‖_(⌊j/2⌋),∞).

*Classes of coefficients.* Fix smooth functions φ_1, …, φ_(n_φ) on Σ (the phases; n_φ = 0 is allowed) and a closed
ball 𝔅 ⊂ ℝ^d centred at 0. A *profile function* is a smooth function
h(x, θ_1, …, θ_(n_φ), λ, y) on Σ × T^(n_φ) × [0, 1] × 𝔅, and [h](x, y) := h(x, φ_1(x)/λ, …, φ_(n_φ)(x)/λ, λ, y). By
the chain rule 𝓛_i [h] = [X_i h] + λ⁻¹ Σ_B X_i(φ_B) [∂_(θ_B) h] and ∂_r [h] = [∂_r h] + λ⁻¹ Σ_B ∂_r φ_B [∂_(θ_B) h], so

    (C0) λ^|I| |𝓛^I ∂_y^β [h]| ≤ C_(I,β) on Σ × 𝔅, for every word I and multi-index β,

and λ ∂_r [h] is again of the form [h′]. A function c(x, y) is of *class 𝔏* if it is [h] for a profile function h, and
of *class 𝔓* if c = c0 + λ [h] with c0 smooth on Σ × 𝔅 and independent of λ; then also λ^|I| |𝓛^I ∂_y^β c| ≤ C λ for |I|
≥ 1, and ∂_r c is of class 𝔏. The *class bounds* of c are the constants C_(I,β). With n_φ = 0 and λ = 1 both classes
consist of the smooth functions on Σ × 𝔅.

*Structure.* We consider maps 𝔉 = (𝔉_ρ, 𝔉_J) of the form, the dependence on x not written,

    𝔉_ρ(U) = p(α) ∂_r α − P(α)^(AB) ∇_A ∇_B α + g_ρ(α, ∇α, w),
    𝔉_J(U) = A0(α) ∂_r w + A^B(α) ∇_B w + f(α, w) ∂_r α + g_J(α, ∇α, w),                {#eq:vlasov-structure}

where the coefficients p (a function), P (a symmetric (2,0)-tensor on S³), A0 and A^B (linear maps from E to the space
of the values of 𝔉_J) are of class 𝔓 in (x, α), f is of class 𝔏 in (x, α, w), and g := (g_ρ, g_J) = 𝔉(0) + g̃ with g̃ of
class 𝔏 in (x, α, ∇α, w) and g̃(x, 0) = 0. We assume the *signs*: there are η0, p0, δ_e, A00 > 0 and 𝒮(x, α) of class 𝔓
with values in the invertible linear maps from the values of 𝔉_J to E* such that, for |α| ≤ η0, p ≥ p0, P(ζ, ζ) ≥
δ_e |ζ|² for every covector ζ of S³, the bilinear form 𝒮A0 on E is symmetric with 𝒮A0 ≥ A00, and every 𝒮A^B is a
symmetric bilinear form on E. The class bounds include bounds for |p⁻¹|, |𝒮⁻¹| and |A0⁻¹| on |α| ≤ η0. Quotients by p
and products with A0⁻¹ need not be of class 𝔓 or 𝔏 up to λ = 1, but they satisfy the bounds (C0), and, when their
factors are of class 𝔓, also λ^|I| |𝓛^I ∂_y^β c| ≤ C λ for |I| ≥ 1 and the bounds (C0) for ∂_r c, by the Leibniz rule
and the bounds on |p⁻¹| and |A0⁻¹|; Steps 1–2 of the proof of [[lem:vlasov-scaled-evolution]] use only these bounds. The
argument w is read in E ⊂ S³ × ℝ⁵, T*S³ ⊂ S³ × ℝ⁴ by the round metric, so that a function of class 𝔏 in (x, α, w) is
one of (x, y), y = (α, w) ∈ ℝ⁶, extended off the fibres of E by the orthogonal projection onto them; 𝓛_i of the
argument w then differs from the derivative X_i of its components in ℝ⁵ by a term of order zero in w with constant
coefficients (X_i is linear on ℝ⁴), which has the same bounds.

**Lemma {#lem:vlasov-structure}** (The structure of the constraints.) Let (γ, κ) be data on Σ and 𝒯(x, α) a smooth
function, valued in the space of the values of the constraint map. Then 𝔉(U) := 𝒞(γ_U, κ_U) − 𝒯(·, α) has the form
[[eq:vlasov-structure]], with p = (γ_U^(rr))^(3/2) H, P = γ_U^(rr) Π^(AB), A0 and A^B the coefficients of the principal
part of J in the proof of [[lem:constraints-evolution]] (a), f affine in w, and g_ρ, g_J polynomials of degree at most
two in (∇α, w) whose coefficients are smooth functions of α, of 𝒯 and of the values of γ, ∂γ, ∂²γ, κ and ∂κ at x. The
second derivatives of γ and the first derivatives of κ enter only g_ρ and g_J, and linearly.

*Proof.* We use the proof of [[lem:constraints-evolution]] (a). In R(γ_U) = R_Π − 2 ∂_(e_r) H − H² − |𝒜|² −
2 ν_U⁻¹ Δ_Π ν_U, with ν_U² = ν² + α, e_r = ν_U⁻¹(∂_r − σ), H = H̃ ν_U⁻¹ and 𝒜 = 𝒜̃ ν_U⁻¹, the quantities R_Π, H̃,
𝒜̃ := ½ (∂_r Π − 𝓛_σ Π), Π, σ and ν do not depend on U. Since 2 ν_U ∂ν_U = ∂(ν² + α),

    −2 ∂_(e_r) H = −2 ν_U⁻² (∂_r − σ) H̃ + H̃ ν_U⁻⁴ (∂_r − σ)(ν² + α),

so ∂_r α enters only through H̃ ν_U⁻⁴ ∂_r α = (γ_U^(rr))^(3/2) H ∂_r α (as γ_U^(rr) = ν_U⁻²), and σ(α) is a first angular
derivative. Further −2 ν_U⁻¹ Δ_Π ν_U = −ν_U⁻² Δ_Π(ν² + α) + ½ ν_U⁻⁴ |d(ν² + α)|²_Π, and Δ_Π α = Π^(AB) ∇_A ∇_B α +
(Π^(AB)(Γ̊ − Γ(Π))^C_(AB)) ∂_C α, with Γ̊ − Γ(Π) the difference of the Christoffel symbols of the round metric and of Π,
a tensor built from Π and its first angular derivatives; ν_U⁻² Π^(AB) = γ_U^(rr) Π^(AB). The remaining terms of R(γ_U),
and −|κ_U|² + (tr κ_U)², which is quadratic in w with coefficients algebraic in α through γ_U⁻¹, belong to g_ρ; second
derivatives of γ occur in ∂_r H̃, R_Π and Δ_Π ν², linearly. In J = 2(−div_(γ_U) κ_U + d tr_(γ_U) κ_U) the derivatives of
w come from κ_U − κ, with coefficients algebraic in α, and form A0(α) ∂_r w + A^B(α) ∇_B w up to terms of order zero in
w; the Christoffel symbols of γ_U are those of γ plus terms linear in ∂α with coefficients algebraic in α, and they
multiply κ_U, which is affine in w: this gives f(α, w) ∂_r α plus a term linear in ∇α that belongs to g_J; ∂κ enters
linearly. 𝒯 is algebraic in α. ∎

**Lemma {#lem:vlasov-symmetrizer}** (The symmetrizer on every slice.) Let γ be a Riemannian metric on Σ and α a function
with 1 + α γ^(rr) > 0. Then the matrix 𝒮 of [[eq:data-symmetrizer]] is invertible and depends on γ alone, 𝒮 A0 =
diag(6, γ_U^(rr) Π^(AB)) is positive definite, and every 𝒮 A^C is symmetric.

*Proof.* The derivation of the principal part of J in the proof of [[lem:constraints-evolution]] (a) uses only the
identities Π^(ij) = γ^(ij) − γ^(ri) γ^(rj)/γ^(rr) (so that Π^(rk) = 0 and Π_A^k ∂_k = ∂_A), tr_(γ_U) Π = γ^(ij) Π_ij =
4 − 1 = 3, q(γ⁻¹dr) = 0, γ_U⁻¹dr = (1 + α γ^(rr))⁻¹ γ⁻¹dr and (1 + α γ^(rr))⁻¹ γ^(rr) = γ_U^(rr), each of which holds
for every Riemannian γ and every α with 1 + α γ^(rr) > 0; the smallness of γ_(rA) assumed there enters only the
uniqueness of the symmetrizer, which [[lem:linear-evolution]] does not use. So that derivation gives, for every such γ
and α, the principal part 𝒮A0 ∂_r + 𝒮A^C ∂_C of 𝒮J in (ϖ, q_B), with 𝒮A0 = diag(6, γ_U^(rr) Π^(AB)) and the symmetric
𝒮A^C displayed there. γ_U^(rr) = γ^(rr)/(1 + α γ^(rr)) > 0, and Π^(AB), the inverse of the induced metric of the
spheres, is positive definite. 𝒮 = [[1, γ^(rB)/γ^(rr)], [0, −½ Π^(AB)]] is block triangular with invertible diagonal
blocks and involves γ only. ∎

So (V3), positive mean curvature of the spheres, is the only sign the radial solve needs on the initial slice of
[[thm:vlasov]]: the second sign of [[lem:constraints-evolution]] (a) holds on every slice.

**Lemma {#lem:vlasov-scaled-evolution}** (The linear evolution in scaled norms.) Let 𝔉 have the structure
[[eq:vlasov-structure]] with the signs, let k ≥ 6, and let V = (α_V, w_V) be smooth on Σ with ‖V‖_(𝒴_k) ≤ η1 λ³. Consider
the linear system for U = (α, w), with zero data at r = a,

    p(α_V) ∂_r α − P(α_V)^(AB) ∇_A ∇_B α + b·∇α + c α + e·w = F_ρ,
    ∂_r w + B^C(α_V) ∇_C w + f̂(α_V, w_V) ∂_r α + f′·∇α + c″ α + c′ w = F_J,           {#eq:vlasov-scaled-linear}

with B^C := A0⁻¹ A^C, f̂ := A0⁻¹ f, coefficients b, c, e, f′, c″, c′ of class 𝔏 in x, and F = (F_ρ, F_J) smooth on Σ.
There are η1 > 0 and C, depending on k, b1 − a, η0, p0, δ_e, A00 and the class bounds, and not on λ, V or F, such that
the solution exists, is unique and smooth, and

    ‖U‖_(𝒴_k(a,r)) ≤ C (∫_a^r ‖F‖²_(k) dr′)^(1/2),      a ≤ r ≤ b1.                     {#eq:vlasov-scaled-bound}

Moreover, for every k′ > k there is C_t′, depending on k′, λ, the class bounds and upper bounds for ‖V‖_(𝒴_(k′−1)),
∫_a^(b1) ‖F‖²_(k) dr and sup_([a,b1]) ‖F‖_(4), such that

    ‖U‖²_(𝒴_(k′)(a,r)) ≤ C_t′ (∫_a^r ‖F‖²_(k′) dr′ + ∫_a^r ‖V‖²_(𝒴_(k′)(a,r′)) dr′).   {#eq:vlasov-scaled-tame}

*Proof.* *Existence.* Put S0 := 𝒮(α_V) A0(α_V) and S^C := S0 B^C = 𝒮(α_V) A^C(α_V). With A0 replaced by the identity,
A^B by B^B and the symmetrizer 𝒮 by S0, [[eq:vlasov-scaled-linear]] is a system of the form [[eq:data-linear]] (the
difference between ∇_C and ∂_C on w being a term of order zero), with S0 ≥ A00 and S^C symmetric by the signs,
since |α_V| ≤ C λ⁻¹ ‖α_V‖_(k;1) ≤ C η1 λ² ≤ η0 by (N2) for η1 small. Its coefficients are smooth, so the quantity M_s of
[[lem:linear-evolution]] is finite for every s, and that lemma gives a unique solution, of every regularity in the
angles; the equations, solved for ∂_r α and ∂_r w, give its r-derivatives. So the identities below hold, every pairing
being absolutely continuous in r.

*Step 1: the coefficients.* Let c be one of P̂ := P(α_V)/p(α_V), 1/p(α_V), B^C, S0, S^C (the principal ones; of class 𝔓
in (x, α), evaluated at α_V) or f̂(α_V, w_V), b/p(α_V), c/p(α_V), e/p(α_V), f′, c″, c′ (the others). By the chain rule,
𝓛^I [c̃(x, Y)] for Y = α_V or Y = (α_V, w_V) is the sum, over the partitions of the letters of I into a word I_0 and
nonempty words J_1, …, J_l (l ≥ 0), each keeping the order of I, of (𝓛^(I_0) ∂_y^l c̃)(x, Y)[𝓛^(J_1) Y, …, 𝓛^(J_l) Y]:
applying 𝓛_i to such a term adds i to I_0, or to one J_s, or as a new word J_(l+1) = (i). By (N1), (N2) and the
hypothesis, λ^|J| sup |𝓛^J α_V| ≤ C η1 λ² for |J| ≤ k − 1, λ^|J| sup |𝓛^J w_V| ≤ C η1 λ for |J| ≤ k − 2, and ‖λ^|J| 𝓛^J
Y‖ ≤ η1 λ³ for |J| ≤ k. Put in c_I^♭ the terms of λ^|I| 𝓛^I c in which every factor 𝓛^(J_s) Y has |J_s| ≤ k − 2 (|J_s| ≤
k − 1 for an α_V factor), and the rest in c_I^♯. Then, for |I| ≤ k: |c_I^♭| ≤ C_0, and |c_I^♭| ≤ C_0 λ if c is principal
and I ≠ ∅ (a term with I_0 ≠ ∅ carries λ^|I_0| |𝓛^(I_0) c̃| ≤ C λ, and one with l ≥ 1 a factor at most C η1 λ²); c_I^♯ =
0 for |I| ≤ k − 2; and ‖c_I^♯‖ ≤ C_0 η1 λ³, since a term of c_I^♯ has exactly one factor of order at least k − 1 (two
such would have total order 2k − 2 > k), taken in L², the others being bounded. Also |∇c| ≤ C_0 for c principal, as
∇[c̃(x, α_V)] = (∇_x c̃) + (∂_y c̃) ∇α_V with |∇_x c̃| ≤ C by (C0) and (K2) and |∇α_V| ≤ C η1 λ; and |∂_r S0| ≤ C_0 (1 +
μ_V), μ_V := C_S λ⁻² ‖∂_r α_V‖_(2), with ∫_a^(b1) μ_V² ≤ C η1² λ² ≤ 1, as ∂_r c̃ is of class 𝔏.

*Step 2: products and commutators.* For c as in Step 1 and Z a function or section, by (K4):

    (R1) ‖c Z‖_(j) ≤ C ‖Z‖_(j),      3 ≤ j ≤ k;
    (R2) ‖Σ_(I′≠∅) (λ^|I′| 𝓛^(I′) c)(λ^|I″| 𝓛^(I″) Z)‖ ≤ C λ ‖Z‖_(|I|−1),      1 ≤ |I| ≤ k, c principal,

the sum in (R2) running over the splittings of I with I′ ≠ ∅. For (R1), the terms with c^♭ are at most C_0 times a term
of ‖Z‖_(j); a term with c^♯ has |I″| ≤ 1 and is at most ‖c^♯‖ sup |λ^|I″| 𝓛^(I″) Z| ≤ C_0 η1 λ³ · C λ⁻² ‖Z‖_(3) by
(N1). For (R2), the terms with c^♭ and I′ ≠ ∅ are at most C_0 λ ‖λ^|I″| 𝓛^(I″) Z‖ with |I″| ≤ |I| − 1, and the terms
with c^♯ occur only for |I| ≥ k − 1 ≥ 5 and are at most C η1 λ ‖Z‖_(3) ≤ C λ ‖Z‖_(|I|−1).

*Step 3: the parabolic energy.* Dividing the first equation by p(α_V), ∂_r α = P̂^(AB) ∇_A ∇_B α + R_ρ with R_ρ :=
p(α_V)⁻¹ (F_ρ − b·∇α − c α − e·w). For |I| ≤ k, by (K1),

    ∂_r 𝓛^I α = P̂^(AB) ∇_A ∇_B 𝓛^I α + 𝒦_I + 𝓛^I R_ρ,      𝒦_I := Σ_(I′≠∅) (𝓛^(I′) P̂)^(AB) ∇_A ∇_B 𝓛^(I″) α.

Put e_I := λ^(2|I|) (‖𝓛^I α‖² + ‖∇𝓛^I α‖²) and g_I := λ^(2|I|) ‖∇²𝓛^I α‖². Integrating by parts on S³, d/dr ½
(‖f‖² + ‖∇f‖²) = ⟨f − Δf, ∂_r f⟩. For a symmetric (2,0)-tensor P̂ with P̂(ζ, ζ) ≥ δ_P |ζ|² and |P̂| + |∇P̂| ≤ M,

    ⟨Δf, P̂^(AB) ∇_A ∇_B f⟩ ≥ δ_P ‖∇²f‖² − C_M (‖∇f‖ ‖∇²f‖ + ‖∇f‖²):                               {#eq:vlasov-elliptic}

integrating by parts twice, ⟨Δf, P̂^(AB) ∇_A ∇_B f⟩ = −∫ ∇^C f (∇_C P̂^(AB)) ∇_A ∇_B f − ∫ ∇^C f P̂^(AB) ∇_C ∇_A ∇_B f,
and ∇_C ∇_A ∇_B f = ∇_A ∇_B ∇_C f + (curvature of the round S³) · ∇f, while −∫ ∇^C f P̂^(AB) ∇_A ∇_B ∇_C f =
∫ P̂^(AB) ∇_A ∇^C f ∇_B ∇_C f + ∫ (∇_A P̂^(AB)) ∇^C f ∇_B ∇_C f ≥ δ_P ‖∇²f‖² − M ‖∇f‖ ‖∇²f‖. Here P̂ ≥ δ_P := δ_e/sup p
and |P̂| + |∇P̂| ≤ C_0 by Step 1. With f := 𝓛^I α, using |⟨f, P̂·∇²f⟩| ≤ C_0 ‖f‖ ‖∇²f‖ and ‖f − Δf‖ ≤ ‖f‖ + √3 ‖∇²f‖,

    λ^(2|I|) d/dr ½ (‖f‖² + ‖∇f‖²) ≤ −δ_P g_I + C (e_I^(1/2) g_I^(1/2) + e_I)
                                         + (e_I^(1/2) + √3 g_I^(1/2)) λ^|I| (‖𝒦_I‖ + ‖𝓛^I R_ρ‖).

By (R2) with Z := ∇²α and (N4), λ^|I| ‖𝒦_I‖ ≤ C λ ‖∇²α‖_(|I|−1) ≤ C (Σ_(|J|<|I|) g_J)^(1/2); by (R1) and (N4),
λ^|I| ‖𝓛^I R_ρ‖ ≤ ‖R_ρ‖_(k) ≤ C (‖F_ρ‖_(k) + ‖α‖_(k;1) + ‖w‖_(k)).

*Step 4: the hyperbolic energy.* The second equation reads ∂_r w = −B^C ∇_C w + R_J with R_J := F_J − f̂ ∂_r α −
f′·∇α − c″ α − c′ w. For |I| ≤ k, ∂_r 𝓛^I w = −B^C ∇_C 𝓛^I w − 𝒟_I + 𝓛^I R_J with 𝒟_I := Σ_(I′≠∅) (𝓛^(I′) B^C)
∇_C 𝓛^(I″) w. Put h_I := λ^(2|I|) ⟨𝓛^I w, S0 𝓛^I w⟩, the L² pairing of the bilinear form S0. Then

    ½ d/dr h_I = ½ λ^(2|I|) ⟨𝓛^I w, (∂_r S0) 𝓛^I w⟩ − λ^(2|I|) ⟨𝓛^I w, S^C ∇_C 𝓛^I w⟩
                 + λ^(2|I|) ⟨S0 𝓛^I w, −𝒟_I + 𝓛^I R_J⟩,

and since S^C is symmetric, ∇_C (S^C(w̃, w̃)) = (∇_C S^C)(w̃, w̃) + 2 S^C(∇_C w̃, w̃), so the middle term equals
½ λ^(2|I|) ⟨𝓛^I w, (∇_C S^C) 𝓛^I w⟩ and is at most C_0 λ^(2|I|) ‖𝓛^I w‖². By (R2) and (N3), λ^|I| ‖𝒟_I‖ ≤
C λ ‖∇w‖_(|I|−1) ≤ C ‖w‖_(k); by (R1), λ^|I| ‖𝓛^I R_J‖ ≤ C (‖F_J‖_(k) + ‖∂_r α‖_(k) + ‖α‖_(k;1) + ‖w‖_(k)); and by the
first equation, (R1) and (N4),

    ‖∂_r α‖_(k) ≤ ‖P̂·∇²α‖_(k) + ‖R_ρ‖_(k) ≤ C (‖α‖_(k;2) + ‖F_ρ‖_(k) + ‖α‖_(k;1) + ‖w‖_(k)).  {#eq:vlasov-scaled-dr}

So ½ d/dr h_I ≤ C (1 + μ_V) λ^(2|I|) ‖𝓛^I w‖² + C λ^|I| ‖𝓛^I w‖ (‖w‖_(k) + ‖α‖_(k;1) + ‖α‖_(k;2) + ‖F‖_(k)).

*Step 5: closing.* For ϵ ∈ (0, 1/12] put 𝓔 := Σ_(|I|≤k) ϵ^|I| ½ (e_I + h_I) and 𝓖 := Σ_(|I|≤k) ϵ^|I| g_I. Then
𝓔 ≥ c_ϵ (‖α‖²_(k;1) + ‖w‖²_(k)) with c_ϵ := ½ ϵ^k min(1, A00), 𝓔 ≤ C (‖α‖²_(k;1) + ‖w‖²_(k)), and ‖α‖²_(k;2) ≤
ϵ^(−k) (𝓖 + 2𝓔). In the sum of Step 3 over I with the weights ϵ^|I|, the commutator terms are at most
Σ_I ϵ^|I| C (e_I + g_I)^(1/2) (Σ_(|J|<|I|) g_J)^(1/2) ≤ (δ_P/8) 𝓖 + C𝓔 + C′ Σ_J g_J Σ_(|I|>|J|) ϵ^|I|; there are
6^i words of length i, so Σ_(|I|>|J|) ϵ^|I| ≤ 2 (6ϵ)^(|J|+1) ≤ 12 · 6^k ϵ · ϵ^|J|, and with ϵ := min(1/12,
δ_P/(96 · 6^k C′)) these terms are at most (δ_P/4) 𝓖 + C𝓔. The other terms of Step 3 are at most (δ_P/8) 𝓖 +
C_ϵ (𝓔 + ‖F‖²_(k)), by Young's inequality. In the sum of Step 4, C ‖w‖_(k) ‖α‖_(k;2) ≤ C ‖w‖_(k) ϵ^(−k/2) (𝓖 +
2𝓔)^(1/2) ≤ (δ_P/8) 𝓖 + C_ϵ 𝓔. Hence

    d𝓔/dr ≤ −(δ_P/4) 𝓖 + C_ϵ (1 + μ_V) 𝓔 + C_ϵ ‖F‖²_(k),      𝓔(a) = 0,

(the terms in 𝓖 add up to at most (−δ_P + δ_P/4 + δ_P/8 + δ_P/8) 𝓖), and Gronwall's lemma, with ∫_a^(b1) (1 + μ_V) ≤
b1 − a + (b1 − a)^(1/2), gives 𝓔(r) + (δ_P/4) ∫_a^r 𝓖 ≤ C ∫_a^r ‖F‖²_(k).
With [[eq:vlasov-scaled-dr]] this is [[eq:vlasov-scaled-bound]].

*Step 6: the tame bound.* Repeat Steps 1–5 at the index k′ > k. Step 1 changes: a factor 𝓛^J Y with |J| ≤ k′ − 2 for
α_V, |J| ≤ k′ − 3 for w_V, is bounded in sup norm by C λ⁻² ‖V‖_(𝒴_(k′−1)), by (N1)–(N2); the remaining factors have
order at least k′ − 2, so at most one occurs in a term (k′ ≥ 7), and it is bounded in L² by ‖V‖_(𝒴_(k′)(a,r)) at
points of [a, r], the other factors of the term having total order at most 2. So in (R1) and (R2) at the index k′ the
terms with such a factor are at most C ‖V‖_(𝒴_(k′)(a,r)) sup |λ^|I″| 𝓛^(I″) Z| with |I″| ≤ 2, which by (N1) is at most
C λ⁻² ‖V‖_(𝒴_(k′)(a,r)) ‖Z‖_(4); for the Z that occur (∇²α, ∇w, ∂_r α, α, ∇α, w and F), ‖Z‖_(4) is bounded by
C λ⁻¹ (‖α‖_(5;1) + ‖w‖_(5) + ‖F‖_(4)), by (N2), (N3) and [[eq:vlasov-scaled-dr]], hence by a constant, by
[[eq:vlasov-scaled-bound]] and the assumed bound on sup ‖F‖_(4). In the energy inequality of Step 5 at the index k′
these terms are at most C_t′ ‖V‖_(𝒴_(k′)(a,r)) (𝓔′^(1/2) + 𝓖′^(1/2)) ≤ (δ_P/8) 𝓖′ + C_t′ (𝓔′ + ‖V‖²_(𝒴_(k′)(a,r))), and
Gronwall's lemma gives [[eq:vlasov-scaled-tame]]. ∎

**Proposition {#prop:vlasov-scaled-correction}** (The constraints solved in scaled norms.) Let 𝔉 have the structure
[[eq:vlasov-structure]] with the signs, with class bounds of every order and 𝔉(0) smooth on Σ, let k ≥ 8, and put ε :=
sup_([a,b1]) ‖𝔉(0)‖_(k). There are η > 0 and C, depending on k, b1 − a, η0, p0, δ_e, A00 and the class bounds, and not
on λ, such that if ε ≤ η λ⁴, there is a smooth U on Σ with zero data at r = a,

    𝔉(U) = 0 on Σ,      ‖U‖_(𝒴_k) ≤ C ε;                                              {#eq:vlasov-scaled-solution}

it is the only smooth solution with zero data at r = a and ‖U‖_(𝒴_k) ≤ C ε. If 𝔉 commutes with a group of isometries
of the round S³ acting on U by pull-back, U is invariant under that group.

*Proof.* *The scheme.* For V = (α_V, w_V) let L_V U be the left side of [[eq:vlasov-scaled-linear]] with the coefficients
of [[eq:vlasov-structure]]: p(α_V), P(α_V), B^C(α_V), f̂(α_V, w_V), and the linear parts at U = 0 of the remaining terms,
b·∇α + c α + e·w := Dg̃_ρ(0)[α, ∇α, w] and f′·∇α + c″ α + c′ w := A0(0)⁻¹ Dg̃_J(0)[α, ∇α, w], which are of class 𝔏.
Put

    𝔈(V) := (𝔉_ρ(V), A0(α_V)⁻¹ 𝔉_J(V)) − L_V V
          = (𝔉_ρ(0) + g̃_ρ(V) − Dg̃_ρ(0)[V], A0(α_V)⁻¹ (𝔉_J(0) + g̃_J(V)) − A0(0)⁻¹ Dg̃_J(0)[V]),

with g̃(V) := g̃(α_V, ∇α_V, w_V). Since A0 is invertible, 𝔉(U) = 0 if and only if L_U U + 𝔈(U) = 0. Let U_0 := 0 and let
U_(i+1) solve L_(U_i) U_(i+1) = −𝔈(U_i) with zero data at r = a.

*The forcing.* 𝔈(V) is (𝔉_ρ(0), A0(α_V)⁻¹ 𝔉_J(0)) plus G(x, Y), Y := (α_V, ∇α_V, w_V), with G of class 𝔏 vanishing
with its first derivatives in Y at Y = 0; so G = Σ_(i,j) Y_i Y_j G_(ij)(x, Y) with G_(ij) := ∫_0^1 (1 − s) ∂_i ∂_j
G(x, s Y) ds of class 𝔏. By (K4) and the chain rule of Step 1 of the proof of [[lem:vlasov-scaled-evolution]], every term
of λ^|I| 𝓛^I G(·, Y), |I| ≤ k, is a product with at least two factors 𝓛^J Y, at most one with |J| > k/2; putting it in L²
and the others in sup norm, with ‖Y‖_(⌊k/2⌋+1),∞ ≤ C λ⁻² ‖V‖_(𝒴_k) ≤ 1 by (N1), (N2) and ⌊k/2⌋ + 4 ≤ k, and ‖Y‖_(k) ≤
2 ‖V‖_(𝒴_k) by (N4),

    ‖G(·, Y)‖_(k) ≤ C_2 λ⁻² ‖V‖²_(𝒴_k).

By (R1) of the proof of [[lem:vlasov-scaled-evolution]], ‖(𝔉_ρ(0), A0(α_V)⁻¹ 𝔉_J(0))‖_(k) ≤ C_3 ε. So sup_r ‖𝔈(V)‖_(k) ≤
C_3 ε + C_2 λ⁻² ‖V‖²_(𝒴_k).

*Boundedness.* Let C be the constant of [[eq:vlasov-scaled-bound]] at the index k and C_1 := C (b1 − a)^(1/2) C_3. If
‖U_i‖_(𝒴_k) ≤ 2 C_1 ε ≤ η1 λ³, then [[lem:vlasov-scaled-evolution]] applies with V := U_i and gives ‖U_(i+1)‖_(𝒴_k) ≤
C (b1 − a)^(1/2) (C_3 ε + C_2 λ⁻² 4 C_1² ε²) ≤ 2 C_1 ε for ε ≤ λ²/(4 C (b1 − a)^(1/2) C_2 C_1); both conditions hold for
ε ≤ η λ⁴ with η small. By induction every U_i is smooth and ‖U_i‖_(𝒴_k) ≤ 2 C_1 ε.

*Contraction.* Let j := k − 2 ≥ 6 and δ_(i+1) := U_(i+1) − U_i. Then L_(U_i) δ_(i+1) = −(L_(U_i) − L_(U_(i−1))) U_i −
(𝔈(U_i) − 𝔈(U_(i−1))). The first term is a sum of products (Δc) Z, with Δc := c(U_i) − c(U_(i−1)) for c one of p, P,
B^C, f̂, and Z := ∂_r α_i, ∇²α_i, ∇w_i, ∂_r α_i respectively. Writing Δc as ∫_0^1 ∂_y c ds applied to the difference of
the arguments, ‖Δc‖_(j) ≤ C ‖δ_i‖_(𝒴_j) and ‖Δc‖_(⌊j/2⌋),∞ ≤ C λ⁻² ‖δ_i‖_(𝒴_j) (as above, ⌊j/2⌋ + 3 ≤ j). By (P2),
‖(Δc) Z‖_(j) ≤ C ‖δ_i‖_(𝒴_j) (λ⁻² ‖Z‖_(j) + ‖Z‖_(⌊j/2⌋),∞) at each r; for Z = ∇w_i the bracket is at most
C λ⁻³ ‖w_i‖_(k), by (N1) and (N3), and for Z = ∂_r α_i, ∇²α_i it is at most C λ⁻² (‖∂_r α_i‖_(k) + ‖α_i‖_(k;2)),
square integrable in r. So the L² norm in r of ‖(L_(U_i) − L_(U_(i−1))) U_i‖_(j) is at most C λ⁻³ ‖U_i‖_(𝒴_k)
‖δ_i‖_(𝒴_j) ≤ C λ⁻³ ε ‖δ_i‖_(𝒴_j). In the same way ‖𝔈(U_i) − 𝔈(U_(i−1))‖_(j) ≤ C λ⁻² (ε + ‖U_i‖_(𝒴_k) +
‖U_(i−1)‖_(𝒴_k)) ‖δ_i‖_(𝒴_j), writing the difference of the terms A0(α)⁻¹ 𝔉_J(0) and of G as integrals of
derivatives. So, by [[eq:vlasov-scaled-bound]] at the index j with V := U_i, ‖δ_(i+1)‖_(𝒴_j) ≤ C λ⁻³ ε ‖δ_i‖_(𝒴_j) ≤
½ ‖δ_i‖_(𝒴_j) for η small.

*The limit.* So U_i converges in 𝒴_j to some U, and, being bounded in 𝒴_k, U satisfies ‖U‖_(𝒴_k) ≤ 2 C_1 ε (at each r the
norms of 𝒴_k are lower semicontinuous under convergence in 𝒴_j). The coefficients of L_(U_i) converge uniformly with
their first derivatives, so L_(U_i) U_(i+1) + 𝔈(U_i) → L_U U + 𝔈(U) in L²((a, b1); L²(S³)), and 𝔉(U) = 0. Uniqueness in
the ball: the difference of two solutions U, U′ there satisfies L_U (U − U′) = −(L_U − L_(U′)) U′ − (𝔈(U) − 𝔈(U′)), and
the estimate of the contraction gives ‖U − U′‖_(𝒴_j) ≤ ½ ‖U − U′‖_(𝒴_j). We take C := 2 C_1 in
[[eq:vlasov-scaled-solution]].

*Smoothness.* Fix λ. Let k′ > k and suppose sup_i ‖U_i‖_(𝒴_(k′−1)) < ∞, as holds for k′ = k + 1. As above, every term of
λ^|I| 𝓛^I 𝔈(U_i), |I| ≤ k′, has at most one factor of order greater than k′/2, so ‖𝔈(U_i)‖_(k′) ≤ C_t (1 + ‖U_i‖_(𝒴_(k′)
(a,r))) at r, and sup_r ‖𝔈(U_i)‖_(4) ≤ C_t, with C_t independent of i. By [[eq:vlasov-scaled-tame]], ℰ_i(r) :=
‖U_i‖_(𝒴_(k′)(a,r)) satisfies ℰ_(i+1)(r)² ≤ C_t′ (1 + ∫_a^r ℰ_i²) with C_t′ independent of i. By induction ℰ_i(r)² ≤
C_t′ e^(C_t′(r−a)): this holds for ℰ_0 = 0, and if it holds for ℰ_i then ℰ_(i+1)(r)² ≤
C_t′ (1 + ∫_a^r C_t′ e^(C_t′(r′−a)) dr′) = C_t′ e^(C_t′(r−a)). So the U_i are bounded in 𝒴_(k′), and U ∈ 𝒴_(k′), for
every k′: U is smooth in the angles, and the equations 𝔉(U) = 0, solved for ∂_r α and ∂_r w, give its r-derivatives,
so U is smooth.

*Invariance.* If 𝔉 commutes with an isometry ι of the round S³, then L_(V∘ι) U∘ι = (L_V U)∘ι and 𝔈(V∘ι) = 𝔈(V)∘ι,
so by the uniqueness in [[lem:vlasov-scaled-evolution]] each U_i is ι-invariant, and so is U. ∎

### The n-dust approximants are uniform in n {#sec:vlasov-uniform}

**Lemma {#lem:vlasov-trapezoid}** (The label quadrature.) Let h be smooth on 𝒪 × S¹, 𝒪 compact, and

    E_n(x) := ∫_(S¹) h(x, α) dα − (2π/n) Σ_(A=1)^n h(x, 2πA/n).

Then for every j and every k ≥ 2, sup_𝒪 |∂_x^j E_n| ≤ 2 ζ(k) n^(−k) sup_(x∈𝒪) ∫_(S¹) |∂_x^j ∂_α^k h(x, α)| dα, ζ the
Riemann zeta function.

*Proof.* The x-derivatives commute with both terms, so take j = 0. Expand h(x, α) = Σ_(m∈ℤ) ĥ_m(x) e^(imα), absolutely
convergent. Since (2π/n) Σ_A e^(2πimA/n) is 2π if n divides m and 0 otherwise, E_n = −2π Σ_(l≠0) ĥ_(ln). Integrating
by parts k times, |ĥ_m(x)| ≤ (2π)⁻¹ |m|^(−k) ∫ |∂_α^k h(x, α)| dα, so |E_n| ≤ Σ_(l≠0) (|l| n)^(−k) ∫ |∂_α^k h| dα. ∎

For an integrand with a kink in α the error is only of order n⁻²: the smoothness of the field in its label is what is
used.

The class Einstein–n-null-dust system and its augmented form, in the unknowns (g, p_A, Θ_A, q_A) with the expansions
Θ_A := □5 u_A transported by the Raychaudhuri equation, are those of [[sec:class-augmented]] ([[eq:class-aug1]]–
[[eq:class-aug4]], [[prop:class-augmented]]) with N_f = n families, and their Cauchy stability on Ω without smallness,
the families off the axes, is [[thm:class-stability-off-axes]]. That theorem takes the reference's families as eikonals
on the whole of Ω ((H1) there), and its transports run along every family's generators through every point of Ω, while
a field in label form gives each u_α as an eikonal only near its tube. The next lemma removes (H1): away from its tube,
every transport of a family is replaced by a transport along a timelike field, and the family's equations are kept only
where they hold.

**Lemma {#lem:vlasov-local-stability}** (Families eikonal only near their tubes.) Let Ω be admissible for g̊, fix an
integer k ≥ 6, δ > 0 and N_f ≥ 1, and let g̊ and, for A = 1, …, N_f, ů_A and q̊_A ≥ 0 be smooth and G-invariant on a
neighbourhood of Ω, with Ric(g̊) = Σ_A q̊_A dů_A ⊗ dů_A on Ω. Let S_A ⊂ Σ_τ0 be compact and G-invariant, put
P̊_A := g̊⁻¹dů_A, and let the *tube* 𝒯̊_A of S_A be the set of points of Ω on the integral curves of P̊_A from S_A, each
followed forward while it stays in Ω. Assume:

(H1′) ů_A is an eikonal of g̊, with P̊_A future directed, on a G-invariant neighbourhood 𝒱̊_A of 𝒯̊_A in Ω, and q̊_A
vanishes off 𝒯̊_A and satisfies div_g̊(q̊_A P̊_A) = 0 on 𝒱̊_A;

(H2′) 𝒯̊_A lies at distance at least 2δ from the axes.

A datum on Σ_τ0, as in [[sec:class-off-axes]], lies within ε of ů's if [[eq:class-energy]] at τ0, with spatial
derivatives only, ∂_τ w among the first derivatives and the family norms taken on 𝒱̊_A ∩ Σ_τ0, is at most ε; its covector
p_A is the one defined there, on 𝒱̊_A ∩ Σ_τ0, with spatial part ∂_x u_A and the root of g⁻¹(p_A, p_A) = 0 near that of
dů_A. Then there are ε, C > 0 such that every datum that satisfies the constraints and the gauge condition, lies within ε
of ů's, and has supp q_A ∩ Σ_τ0 ⊂ int S_A (interior relative to Σ_τ0) for every A, has a smooth G-invariant development
(g, u_A, q_A) on Ω in the gauge D(g) = 0 relative to g̊, with these properties. Each u_A is a smooth G-invariant eikonal
of g, with g⁻¹du_A future directed, on the tube 𝒯_A of int S_A for u_A (the points of Ω on the integral curves of
g⁻¹du_A from int S_A, each followed forward while it stays in Ω), which is relatively open in Ω and lies within C ε of
𝒯̊_A; q_A vanishes off the tube of supp q_A ∩ Σ_τ0, a compact subset of 𝒯_A; Ric(g) = Σ_A q_A du_A ⊗ du_A and
div_g(q_A g⁻¹du_A) = 0 on Ω, each term extended by zero off 𝒯_A; and 𝒩_k ≤ C ε on [τ0, τ1], with the family norms of
[[eq:class-energy]] taken on 𝒯_A ∩ Σ_τ, p_A := du_A and Θ_A := □_g u_A.

*Proof.* 𝒯̊_A is compact: on 𝒱̊_A the field P̊_A is future null, so τ increases along its integral curves, and 𝒯̊_A is
the image of the compact set of the (x0, τ) with x0 ∈ S_A whose curve reaches Σ_τ inside Ω under the continuous map to
the point reached. Shrinking 𝒱̊_A, we may assume that it lies at distance at least δ from the axes and that its closure
lies in the set of (H1′). Fix a G-invariant smooth ζ′_A on a neighbourhood of Ω with 0 ≤ ζ′_A ≤ 1, equal to 1 on a
neighbourhood of 𝒯̊_A and to 0 off 𝒱̊_A (a cut-off averaged over the compact group G). Put p̊_A := dů_A,
Θ̊_A := □_g̊ ů_A, T_g := −g⁻¹dτ, which is future timelike for |g − g̊| ≤ ε1 by [[def:class-admissible]] (a) and (c), and

    P̃_A := ζ′_A P_A + (1 − ζ′_A) T_g,      P_A := g⁻¹p_A.

(i) *The localised system.* In place of (Aug2)–(Aug4) take, for each A, componentwise in the chart,

    P̃_A(p_(A,a) − p̊_(A,a)) = ζ′_A (P_A^b Γ[g]^c_(ba) p_(A,c) − P_A(p̊_(A,a))),
    P̃_A(Θ_A − Θ̊_A) = ζ′_A (S_A − P_A(Θ̊_A)),                                                    {#eq:vlasov-localised}
    P̃_A(q_A) = −ζ′_A Θ_A q_A,

with S_A as in [[eq:class-aug3]]. Where ζ′_A = 1 these are (Aug2), (Aug3) with ζ_A = 1, and (Aug4); and ζ′_A S_A is
smooth, ζ′_A vanishing within δ of the axes. ů solves them. Indeed, on 𝒱̊_A, ∇_(P̊_A) dů_A = ½ d(g̊⁻¹(dů_A, dů_A)) = 0,
so the first right side vanishes at ů; P̊_A(Θ̊_A) = S_A(ů) by [[eq:class-raychaudhuri]], since Ric(g̊)(P̊_A, P̊_A) =
Σ_B q̊_B g̊⁻¹(dů_A, dů_B)²; and P̊_A(q̊_A) = −Θ̊_A q̊_A, the conservation law. Off 𝒱̊_A, ζ′_A = 0 and q̊_A = 0. And
P̃_A(q̊_A) = ζ′_A P_A(q̊_A) for every g and p_A, as q̊_A vanishes on the relatively open set Ω ∖ 𝒯̊_A, which contains
{ζ′_A < 1}. On Σ_τ0 the family data are cut off: p_A := p̊_A + ζ′_A (p_A^D − p̊_A), Θ_A := Θ̊_A + ζ′_A (Θ_A^D − Θ̊_A),
and q_A the datum's density, where p_A^D is the datum's covector and Θ_A^D := □_g u_A is computed as in
[[sec:class-off-axes]], both on 𝒱̊_A ∩ Σ_τ0. They are the datum's on {ζ′_A = 1} ∩ Σ_τ0, and [[eq:class-energy]] at τ0
is at most C ε.

(ii) *Steps 1–9.* These steps of the proof of [[thm:class-stability-off-axes]] hold for (Aug1) and
[[eq:vlasov-localised]], with the transport fields P̃_A, and give a smooth G-invariant solution on Ω with 𝒩_k ≤ C ε.
The changes are these. At ů, P̊̃_A := ζ′_A P̊_A + (1 − ζ′_A) T_g̊ is a convex combination of future causal vectors, P̊_A
being future null where ζ′_A > 0; so P̊̃_A is future causal with P̊̃_A(τ) ≥ c > 0 on the compact Ω, and on each lateral
boundary component {F = 0} of Ω, dF(P̊̃_A) ≥ c′ > 0, dF being positive on the compact set of the future causal vectors Y
at its points with dτ(Y) ≥ c and |Y| ≤ c⁻¹. By Step 1, |P̃_A − P̊̃_A| ≤ C 𝒩_k on Ω, so in the bootstrap of Step 3,
P̃_A(τ) ≥ c/2 and dF(P̃_A) ≥ c′/2 for ε small. The proof of [[lem:class-transport]] uses of its field P only the bounds
P(τ) ≥ c_P and |P| + |∂P| ≤ c_P⁻¹ and dF(P) ≥ 0 on the lateral boundary, so it applies to P̃_A. In Step 3, by the third
equation, q_A vanishes along every integral curve of P̃_A on which it vanishes initially; every point of Ω lies on such
a curve from Σ_τ0, followed backward inside Ω, P̃_A pointing out of Ω at its lateral boundary; so supp q_A lies in the
tube for P̃_A of the compact set supp q_A ∩ Σ_τ0, inside that of S_A. The integral curves of P̃_A from S_A stay
within C ε of those of P̊̃_A from S_A, as in Step 3, and these trace 𝒯̊_A, on which P̊̃_A = P̊_A; so for ε small the
tube of S_A for P̃_A lies in the interior of {ζ′_A = 1}, where P̃_A = P_A. In Steps 5–7, since ů solves
[[eq:vlasov-localised]], the equations for the differences are those of Steps 5–7 there multiplied by ζ′_A, with P̃_A
on the left:

    P̃_A(δp_(A,a)) = ζ′_A (P_A^b (Γ[g] − Γ[g̊])^c_(ba) p_(A,c) + Γ[g̊]^c_(ba) (P_A^b p_(A,c) − P̊_A^b p̊_(A,c))
                     − (P_A − P̊_A)^b ∂_b p̊_(A,a)),
    P̃_A(δΘ_A) = ζ′_A (S_A(U) − S_A(ů) − (P_A − P̊_A)(Θ̊_A)),
    P̃_A(δq_A) = −ζ′_A (Θ_A q_A − Θ̊_A q̊_A + (P_A − P̊_A)(q̊_A)),

and the commutator [∂^α, P̃_A·∂] has the top term (∂^α P̃_A)·∂, P̃_A being a smooth function of (g, p_A); so the bounds
of those steps hold, with constants depending also on ζ′_A. In Step 9 the transports have the coefficient
P̃_A^τ ≥ c/2 of ∂_τ (the cut-off on p_A there keeping it so), the boundary matrix of a transport at a conormal ν is
ν(P̃_A), positive at ů on the lateral boundary, and ζ′_A and T_g are G-invariant, G fixing τ.

(iii) *Step 10 on the tubes.* Let 𝒯_A be the set of points of Ω on the integral curves of P̃_A from int S_A, each
followed forward while it stays in Ω. It is relatively open in Ω: P̃_A is transverse to the slices and points out of Ω
at its lateral boundary, so the curve through a point of Ω near one of 𝒯_A, followed backward, meets Σ_τ0 near a point
of int S_A. By (ii) it lies in the interior of {ζ′_A = 1}, where P̃_A = P_A and [[eq:vlasov-localised]] is
(Aug2)–(Aug4). On Σ_τ0 ∩ 𝒯_A the data are the datum's, so ν_A := g⁻¹(p_A, p_A) vanishes there; ν_A is constant along
the integral curves of P_A in 𝒯_A ([[prop:class-augmented]] (b)), so ν_A = 0 on 𝒯_A, and dν_A = 0 there. As in Step
10, dp_A = 0 on Σ_τ0 ∩ 𝒯_A; by [[prop:class-augmented]] (b), i_(P_A) dp_A = 0 and ℒ_(P_A) dp_A = 0 on 𝒯_A, so
dp_A = 0 on 𝒯_A. Let Φ(x0, t) be the point reached at the parameter t by the integral curve of P_A from x0 ∈ int S_A:
Φ is a smooth bijection onto 𝒯_A with invertible differential, integral curves not meeting and τ increasing along them.
Define u_A on 𝒯_A by u_A(Φ(x0, t)) := u_A^D(x0), u_A^D the datum's function. The pull-back Φ*p_A is closed, and its
dt-component is p_A(P_A) = ν_A ∘ Φ = 0, so its dx0-components do not depend on t; at t = 0 they are the spatial
derivatives of u_A^D. Hence Φ*p_A = d(u_A ∘ Φ), and p_A = du_A on 𝒯_A: u_A is a smooth G-invariant eikonal of g there,
with g⁻¹du_A = P_A future directed, and 𝒯_A is the tube of int S_A for u_A. Let S′_A be compact with supp q_A ∩ Σ_τ0 ⊂
int S′_A and S′_A ⊂ int S_A, and 𝒯′_A ⊂ 𝒯_A its tube; it contains supp q_A, by (ii). The rest of Step 10 holds with
𝒯′_A in place of 𝒯_A there. Indeed (Aug2) and (Aug4) hold on the relatively open 𝒯_A, which contains supp q_A, q_A
vanishes on the relatively open Ω ∖ supp q_A, and ν_A = 0 on 𝒯_A; so, by [[prop:class-augmented]] (c),
div_g T = −Σ_A Δ_A q_A p_A and tr_g T = 0 on Ω, and B_g T = Σ_A Δ_A q_A p_A. [[eq:class-defect]] holds on 𝒯′_A, where
p_A = du_A with u_A an eikonal ([[prop:class-augmented]] (d)). And the linear Gronwall inequality for ‖∂D‖ + ‖D‖ +
Σ_A ‖Δ_A‖_(L²(𝒯′_A ∩ Σ_τ)), the transport of Δ_A having no flux through the part of the boundary of 𝒯′_A ruled by
integral curves of P_A, with value 0 at τ0, gives D = 0 and Δ_A = 0 on 𝒯′_A. Every point of 𝒯_A lies in such a
𝒯′_A. So Ric(g) = Σ_A q_A p_A ⊗ p_A = Σ_A q_A du_A ⊗ du_A, Θ_A = □_g u_A on 𝒯_A, and (Aug4) is div_g(q_A g⁻¹du_A) = 0
there. The bound 𝒩_k ≤ C ε of (ii) is the one stated, p_A and Θ_A being du_A and □_g u_A on 𝒯_A; and 𝒯_A lies within
C ε of 𝒯̊_A by (ii). ∎

Let (g, F, u) satisfy (Ω), (V1), (V2) and (V3), with the compact set S of (V1). A *datum in label form* near it is
D = (γ_D, κ_D, F_D, u_D): metric data (γ_D, κ_D) on Σ_τ0 ∩ Ω, completed to Cauchy data with the lapse and shift of g and
with ∂_τ of these fixed by the gauge condition D = 0 as in [[sec:data-identities]], and smooth invariant functions
F_D ≥ 0 and u_D on (Σ_τ0 ∩ Ω) × S¹ with supp F_D ⊂ int S and d(u_D(·, α))(x) ≠ 0 for (x, α) in a neighbourhood of S,
such that the constraints hold with the stress of the field, the τ-derivatives of the u_D(·, α) being the roots of the
eikonal equation fixed by the branch of [[def:vlasov-label]]. Its distance to the data of (g, F, u) is d(D), the C^(m+3)
norm of (γ_D − γ, κ_D − κ) on Σ_τ0 ∩ Ω plus that of (F_D − F, u_D − u) on (Σ_τ0 ∩ Ω) × S¹. The data of (g, F, u) form
such a datum: on 𝒲 ∩ (Σ_τ0 × S¹), du_α is null, nonzero and future directed, so its restriction to the spacelike slice
is not zero. For n ≥ 1 put α_A := 2πA/n. The *n-dust datum* D_n of D has the densities q_A := (2π/n) F_D(·, α_A)²,
the eikonal data u_D(·, α_A), and the metric data (γ_D, κ_D) corrected by
[[prop:vlasov-scaled-correction]], with λ = 1 and no phases, to satisfy the constraints with the stress T^(n) :=
Σ_A q_A du_A ⊗ du_A (the τ-components of the du_A being the roots for the corrected metric). The *n-dust approximant*
g^(n) of the field is the development of the n-dust datum of the data of (g, F, u) itself.

**Proposition {#prop:vlasov-uniform-n}** (The n-dust approximants are uniform in n.) Fix m ≥ 6. There are ε0 > 0 and
C, and for every k ≥ 2 constants n0 and C_k, depending also on bounds for the derivatives of D of order at most
k + 2m + 4, such that for every datum D in label form with d(D) ≤ ε0 and every n ≥ n0 the n-dust datum D_n has a smooth
invariant development g^(n) on Ω, with densities q_A and, for each A, an eikonal u_A of g^(n), with g^(n)⁻¹du_A future
directed, on the tube 𝒯_A of int S_(α_A) for u_A, such that Ric(g^(n)) = Σ_A q_A du_A ⊗ du_A and div(q_A g^(n)⁻¹du_A) =
0, q_A vanishing off a compact subset of 𝒯_A (the conclusions of [[lem:vlasov-local-stability]]), and on every Σ_τ

    ‖g^(n) − g‖_(H^(m+1)) + ((2π/n) Σ_A ‖(du_A, Θ_A, q_A/(2π/n)) − (du_(α_A), Θ(·, α_A), q(·, α_A))‖²_(H^m))^(1/2)
        ≤ C d(D) + C_k n^(−k),                                                                     {#eq:vlasov-uniform-n}

with Θ_A := □5 u_A, Θ(·, α) := □5 u_α, the family norms taken on 𝒯_A ∩ Σ_τ. The same holds with any m′ ≥ m in place
of m, with ε0 unchanged and C, n0, C_k depending on m′ and on derivatives of D of order at most k + 2m′ + 4. For the
data of (g, F, u), d = 0 and |g^(n) − g|_(C¹(Ω)) ≤ C_k n^(−k).

*Proof.* Let E_n := T_V − Σ_A (2π/n) q(·, α_A) du_(α_A) ⊗ du_(α_A), evaluated with g. It is the error of
[[lem:vlasov-trapezoid]] for the integrand q(x, α) du_α ⊗ du_α, smooth on Ω × S¹, so |∂^j E_n| ≤ C_(j,k) n^(−k) for all
j, k.

*Data.* The constraints of D_n are 𝔉(U) := 𝒞(γ_U, κ_U) − 𝒯_n(·, α) = 0, with (γ_U, κ_U) built on (γ_D, κ_D) and 𝒯_n the
constraint stress of T^(n), algebraic in α through γ_U⁻¹ (the unit normal and the roots of the eikonal equation involve
γ_U). By [[lem:vlasov-structure]] 𝔉 has the structure [[eq:vlasov-structure]], with λ = 1, no phases, and class bounds
independent of n, 𝒯_n being a quadrature of a smooth integrand. The signs hold: p > 0 by (V3) for γ and so for γ_D
and |α| ≤ η0, for ε0 and η0 small; P = γ_U^(rr) Π^(AB) is positive definite; and 𝒮 has the properties of
[[lem:vlasov-symmetrizer]]. 𝔉(0) is the difference of the constraint stresses of the field of D and of T^(n), a
quadrature error of [[lem:vlasov-trapezoid]] for the integrand F_D² du_D ⊗ du_D, whose derivatives of order 2m in x
and k in α hold derivatives of D of order at most k + 2m + 1, so sup_r ‖𝔉(0)‖_(2m) ≤ C_k n^(−k) at λ = 1.
[[prop:vlasov-scaled-correction]] at the index 2m (≥ 12) applies for n ≥ n0 and gives a smooth invariant correction U
with ‖U‖_(𝒴_(2m)) ≤ C_k n^(−k). At λ = 1 this bounds (α, w) in H^(m+1) × H^m on the slice. Indeed, write X^s :=
H^s(S³) and take norms in r on (a, b1). The norm of 𝒴_(2m) bounds α in L^∞X^(2m+1) ∩ L²X^(2m+2) and w in L^∞X^(2m).
Solving 𝔉(U) = 0 for ∂_r α = G_α(x, 𝔍) and ∂_r w = G_w(x, 𝔍), 𝔍 := (α, ∇α, ∇²α, w, ∇w), as in the proof of
[[thm:vlasov-n-data]], and differentiating in r, we show by induction on i ≥ 1 that ∂_r^i α is bounded in
L^∞X^(2m+1−2i) ∩ L²X^(2m+2−2i) and ∂_r^i w in L^∞X^(2m+1−2i) ∩ L²X^(2m+1−2i), for i ≤ m + 1 (the L^∞ bounds for
i ≤ m); we use that X^s · X^t ⊂ X^t for s ≥ t ≥ 0, s ≥ 2. For i = 1 this holds since ∇²α lies in L^∞X^(2m−1) ∩
L²X^(2m), ∇w in L^∞X^(2m−1), and α, ∇α, w, with the coefficients, in L^∞X^(2m). For i ≥ 2, ∂_r^i α = ∂_r^(i−1) G_α
and ∂_r^i w = ∂_r^(i−1) G_w are sums of products of a smooth function of (x, α, ∇α, w) with factors ∂_r^(i_s) ∇^(m_s)
Y_s, Y_s ∈ {α, w}, m_s ≤ 2 for α and m_s ≤ 1 for w, with Σ_s i_s ≤ i − 1. At most one factor has i_s > (i − 1)/2; by
the induction it lies in L^∞X^(2m+1−2i) and in L²X^(2m+2−2i). The others have i_s ≤ (i − 1)/2 and lie in
L^∞X^(2m−i), and 2m − i ≥ 2m + 2 − 2i, 2m − i ≥ m − 1 ≥ 2; the function lies in L^∞X^(2m). Since 2m + 2 − 2i ≥ m + 1 − i
and 2m + 1 − 2i ≥ m − i for i ≤ m + 1, and α ∈ L²X^(2m+2), w ∈ L^∞X^(2m), every derivative ∂_r^i ∂_ω^l of order at
most m + 1 of α, and m of w, is square integrable on the slice. So the metric data of D_n differ from those of g by at
most C d(D) + C_k n^(−k) in H^(m+1) × H^m, and the families' data from the sampled continuum's by C d(D), with the
weight 2π/n, on 𝒱̊_A ∩ Σ_τ0 for the sets 𝒱̊_A below.

*Evolution.* Take as reference the sampled continuum ů: the metric g, in the gauge relative to g itself, with the
families (ů_A, q̊_A) := (u_(α_A), (2π/n) q(·, α_A)), the sets S_A := S_(α_A), whose tubes 𝒯̊_A = D_(α_A)(S) lie at
distance at least 2δ from the axes by (V2), and Ω, admissible for g by (Ω). The neighbourhood 𝒲 of (V1) contains the
compact 𝒟(S) and is open in Ω × S¹, so it contains the set of the (x, α) at distance less than some ρ1 > 0 from 𝒟(S);
fix a G-invariant ζ′ smooth on Ω × S¹, 0 ≤ ζ′ ≤ 1, equal to 1 on a neighbourhood of 𝒟(S) and to 0 at distance at least
ρ1/2 from it, with ρ1 ≤ δ, and put 𝒱̊_A := {x : (x, α_A) is at distance less than ρ1 from 𝒟(S)} and ζ′_A := ζ′(·, α_A).
Then ů satisfies (H1′) and (H2′) of [[lem:vlasov-local-stability]], q(·, α) vanishing off D_α ⊂ D_α(S) and being
conserved ([[def:vlasov-label]]), except that Ric(g) = T_V = Σ_A q̊_A dů_A ⊗ dů_A + E_n; and ζ′_A is a cut-off for that
lemma. So ů solves [[eq:vlasov-localised]] up to the residual ζ′_A E_n(P̊_A, P̊_A) in its second equation, the Ricci
term of the Raychaudhuri equation being Ric(P̊_A, P̊_A) = T_V(P̊_A, P̊_A), and (Aug1) up to the matter term E_n. Parts
(ii) and (iii) of the proof of [[lem:vlasov-local-stability]], with its index k := m, apply to the difference between
the solution of (Aug1) and [[eq:vlasov-localised]] with the datum D_n, its family data cut off as in (i) there, and ů,
with these changes.
(1) The family norms of [[eq:class-energy]] are weighted: Σ_A is replaced by the ℓ² sum
((2π/n) Σ_A ‖·‖²)^(1/2) of the norms of (δp_A, δΘ_A, ς_A), ς_A := q_A/(2π/n) − q̄_A, q̄_A := q(·, α_A). (2) The matter
term of the metric equation for the difference, T := Σ_A q_A p_A ⊗ p_A minus Ric(g) = T_V, is exactly

    T − T_V = Σ_A (2π/n) (ς_A p_A ⊗ p_A + q̄_A (π_A ⊗ p_A + p̊_A ⊗ π_A)) − E_n,      π_A := p_A − p̊_A, p̊_A := du_(α_A),

and by the Cauchy–Schwarz inequality and Σ_A 2π/n = 2π its first part is bounded in H^m by C times the weighted family
norm; so is the difference of the terms Ric(P_A, P_A) = Σ_B (2π/n) (q_B/(2π/n)) g⁻¹(p_A, p_B)² of Step 6, uniformly in
A. (3) Every other term is estimated family by family, with constants uniform in A because the sampled families, the
sets 𝒱̊_A and the cut-offs ζ′_A come from functions smooth in α, uniformly. (4) The residuals add C_k n^(−k) to the right
side. So Step 8 gives 𝒩(τ) ≤ C2 (𝒩(τ0) + C_k n^(−k) + ∫_(τ0)^τ (𝒩 + 𝒩²)) with C2 independent of n, 𝒩(τ0) ≤ C d(D) +
C_k n^(−k) by the data step, and the bootstrap closes for d(D) ≤ ε0 and n ≥ n0. Step 9 of the proof of
[[thm:class-stability-off-axes]], as in (ii) of the proof of [[lem:vlasov-local-stability]] (for N_f = n, a fixed n),
gives the solution on Ω, smooth and invariant, and (iii) there, D_n satisfying the constraints and the gauge condition,
gives the eikonals u_A on the tubes 𝒯_A and the equations stated. The integral curves of the P̃_A from the S_A stay
within C (d(D) + C_k n^(−k)) of the tubes of ů, so (V2) keeps the families off the axes. At the order m′ ≥ m the
inequality of Step 8 is linear in the order-m′ norm, with coefficients bounded by the order-m norm (Step 9 of that
proof) and uniform in n by (1)–(4), which gives the clause on m′, with the data step at the index 2m′. The last
statement is Sobolev's inequality for m ≥ 6. ∎

**Remark {#rem:vlasov-uniform-model}** (Numerical observation.) In a mean-field wave–transport model of the quadrature
step, w_tt − w_xx = Σ_A (2π/n) q_A with q_A transported at speed tanh(2w + cos α_A), with no derivative-loss coupling,
the stability constant of the n-label system was measured as 0.603, 0.667 and 0.667 at n = 4, 8, 16, while a coupling
growing with n gave 0.603, 0.873, 1.654; the ratio of the n-label solution's error to the quadrature residual stayed
below 0.02 for n = 4, 8, 16. No proof uses these values.

### The high-frequency step with n families {#sec:vlasov-n}

In this section g0 is a smooth class metric on Ω, and u_A and F_A ≥ 0 (A = 1, …, n) are smooth invariant functions on Ω
with Ric(g0) = Σ_A F_A² du_A ⊗ du_A. Put ℓ_A := g0⁻¹du_A. For each A let S_A ⊂ Σ_τ0 ∩ Ω be a compact invariant set with
supp F_A ∩ Σ_τ0 ⊂ int S_A (interior relative to Σ_τ0), let 𝒱_A be the tube of S_A for u_A and 𝒯_A ⊂ 𝒱_A that of
supp F_A ∩ Σ_τ0, the *support* of family A ([[def:vlasov-label]]). We assume that u_A is an eikonal of g0, with ℓ_A
future directed, on a neighbourhood of 𝒱_A, and that F_A is transported by [[eq:vlasov-amplitude]] and vanishes off 𝒯_A;
and:

- (i) (Ω) holds for g0;
- (ii′) on the overlap of the supports of any two families |g0⁻¹(du_A, du_B)| ≥ c > 0, and the frequencies are ν_A :=
  Λ^(A−1), with Λ > (m* + m*²/2) Ē²/c, where m* := 2N + 4, N is the number of stages, and Ē bounds |du_A| in
  orthonormal frames on the supports;
- (iii) the wave of family A is the wave W_A of the dust (u_A, F_A) at frequency ν_A ([[def:vlasov-wave]]), at the phase
  θ_A = ν_A u_A/λ: torus-polarised, with its gauge part;
- (iv) every 𝒱_A lies at distance at least δ > 0 from the axes.

Off a neighbourhood of 𝒱_A the function u_A is not an eikonal in general, and nothing of family A is posed there:

(v) *Localisation.* (a) Every transport of family A runs along ℓ_A and is posed on 𝒱_A: the gauge part of its wave, its
phase corrections and pure harmonics in [[thm:vlasov-n-approximant]], its oscillating gauge transports in
[[thm:vlasov-n-data]], and φ_A and Ψ_A in [[thm:vlasov-n-uniform]]. The integral curve of ℓ_A through a point of 𝒱_A,
followed backward, reaches Σ_τ0 inside 𝒱_A, since 𝒱_A is a tube. The transport estimates hold on the slices 𝒱_A ∩ Σ_τ:
in the argument of [[lem:class-transport]] on 𝒱_A ∩ {τ0 ≤ t ≤ τ}, with the field ℓ_A, the flux through the part of the
boundary ruled by integral curves of ℓ_A vanishes, and that through the lateral boundary of Ω is nonnegative by (Ω),
ℓ_A being future directed and null; this is the estimate of [[lem:two-dust-transport]] for Z_A := ℓ_A/ℓ_A(τ), with the
norms on 𝒱_A ∩ Σ_τ. (b) If the data of the pure harmonics of family A vanish off supp F_A ∩ Σ_τ0, every profile that
carries a harmonic e^(i j·θ) with j_A ≠ 0 vanishes off 𝒯_A. Indeed F_A vanishes off 𝒯_A, and so does the gauge part of
W_A, whose transport has zero data and a right side proportional to F_A² ([[def:vlasov-wave]]): the integral curves of
ℓ_A through points of 𝒱_A ∖ 𝒯_A start outside supp F_A, integral curves not meeting. At each stage, a term of the
residual that carries such a harmonic is a product with a factor that carries a harmonic of θ_A, the means and the phase
corrections carrying none; by induction on the stage it vanishes off 𝒯_A. The pure harmonics of family A are
transported along ℓ_A with such right sides and with data vanishing off supp F_A ∩ Σ_τ0, so they vanish on the integral
curves from points of Σ_τ0 ∖ supp F_A, that is off 𝒯_A; and the mixed harmonics are quotients of such terms by Q_j,
pointwise. (c) Hence the phase corrections of family A, φ_A and Ψ_A enter every other equation only multiplied by
profiles that vanish off 𝒯_A, a compact subset of the tube of int S_A, which is relatively open in Ω and lies in 𝒱_A.
These products, extended by zero, are smooth on Ω, and the norms of φ_A and Ψ_A are taken on 𝒱_A ∩ Σ_τ. The
contraction s_A(h) := h(ℓ_A, ℓ_A), and the ℓ_A ⊗ ℓ_A component of the equation for h, use ℓ_A = g0⁻¹du_A on the whole
of Ω.

By [[lem:vlasov-hierarchy]] with m = m*, every symbol [[eq:vlasov-symbol]] with at least two nonzero entries and |j|₁ ≤
m* satisfies |Q_j| ≥ 2 ν_B1 ν_B2 c* on the overlaps, c* := c − m* Ē²/Λ − m*² Ē²/(2Λ) > 0. These conditions are those of
the two-dust theorem with one transport and one phase per family, the mixed symbols bounded below on every harmonic
used; we list what changes from two families to n.

**Theorem {#thm:vlasov-n-approximant}** (The approximant with n phases.) Under (i)–(iv), for every N ≥ 1 and every
smooth choice of stage data, those of the pure harmonics of family A vanishing off supp F_A ∩ Σ_τ0 for every A, there
are profiles g_1, …, g_N in (X, θ_1, …, θ_n), independent of λ, such that g_app = g0 + λ [g_1] + Σ_(l=2)^N λ^l [g_l],
with the phases θ_A = ν_A u_A/λ, is an n-phase approximant with N stages of order K = N − 1 at every regularity k, in
the sense of [[def:two-dust-approximant]] with one phase per family, and with g_1 = m_1 + Σ_A W_A(X, θ_A + φ_1^A(X)),
W_A the waves of (iii).

*Proof.* The stage system is that of [[lem:two-dust-stages]] with n phases: (a) the mean, a linear wave equation; (b)
n phase corrections, each transported along its own generator; (c) the pure harmonics of each family, transported along
its own generator; (d) every mixed harmonic e^(i j·θ) with at least two nonzero entries and |j|₁ ≤ 2m + 4 at stage m,
divided by Q_j. The bound on |j|₁: the waves W_A carry the first harmonic of θ_A and, through their gauge parts, the
second, so g_1 has |j|₁ ≤ 2; a product of profiles ĝ_(l_1), …, ĝ_(l_p) enters the expansion of the reduced Ricci tensor
at order λ^(l_1 + ⋯ + l_p − 2) at most, and, by induction on the stage, ĝ_l has |j|₁ ≤ 2l, so the residual of order
λ^m has |j|₁ ≤ 2(m + 2). On the overlaps |Q_j| ≥ 2 ν_B1 ν_B2 c* for |j|₁ ≤ m* = 2N + 4, by (ii′). The phase
corrections and the mean change Q_j by O(λ), and this change is moved to the next order, as in
[[lem:two-dust-nonresonance]], since |j|₁ is bounded at each stage; each division costs one derivative, and there are
finitely many stages. The transports of family A are posed on 𝒱_A, whose generators reach Σ_τ0 inside 𝒱_A, with the
estimates of (v) (a), and the transported unknowns of family A enter the other equations only through products that
vanish off 𝒯_A, by (v) (b)–(c); the Q_j are divided only on the overlaps of the supports, where (ii′) holds. So the
Picard argument of [[thm:approximant]] closes the stage system.

Stage 0: with g_1 := Σ_A W_A and ĝ_2 := q, R[g0 + λ Σ_A W_A + λ² q] has R^(−1) = 0, and its coefficient of λ⁰ is R^(0) =
Σ_A (R^(0)_A − Ric(g0)) + Ric(g0) + R^(0)_× + (the contribution of q), as in [[lem:two-dust-stage-zero]] (a)–(b) with n
phases: a term with two phase derivatives on one wave W_A is that of R[g0 + λ W_A], a product of two different waves has
only mixed harmonics, and the cross terms of order λ⁻¹ vanish since each W_A depends on one phase. By
[[lem:vlasov-wave]] on 𝒱_A, where u_A is an eikonal, and since W_A and F_A vanish off 𝒯_A, R^(0)_A = Ric(g0) −
F_A² du_A ⊗ du_A on Ω, with no oscillating part, the gauge part χ_A k_A ⊗ k_A removing the second harmonic of the
quadratic term; so the first three terms add up to Ric(g0) − Σ_A F_A² du_A ⊗ du_A + R^(0)_× = R^(0)_×, as
Ric(g0) = Σ_A F_A² du_A ⊗ du_A. The mixed harmonics R^(0)_× are removed by the mixed
harmonics of q, divided by the symbols Q_j of [[eq:vlasov-symbol]] with |j|₁ ≤ 4, bounded below by (ii′), since q enters
R^(0) only through −½ g0^(ab) ∂_a ∂_b, as multiplication of the harmonic e^(i j·θ) by ½ Q_j. The assembly is that of
[[thm:two-dust-approximant]]: the stages m = 1, …, N by (a)–(d) above, and the passage to the fixed phases ν_A u_A/λ by
the Taylor expansion in the phase corrections. ∎

Let s_A(h) := h(ℓ_A, ℓ_A), and let Y_A, G1^A, G2^A, 𝒫 and the energy be those of [[thm:two-dust-uniform]] (defined
before it), with one index per family and the phase derivative ∂_(θ_A) in place of the operator written F_𝔨 there:
G1^A := [∂_(θ_A) g1], G2^A := [∂²_(θ_A) g1] and Y_A := [∂_(θ_A) g1 + λ ∂_(θ_A) g2]. 𝒫 is the mollifier of
[[lem:mollifier]].

**Theorem {#thm:vlasov-n-uniform}** (Uniform existence with n phases.) Fix k = 6 and K ≥ 6. Under (i)–(iv) let g_app be
an n-phase approximant with N stages of order K at regularity k, with constant C_R in (E3), and let g be a Cauchy datum
on Σ_τ0 for Ric^H(g) = 0 with w := g − g_app satisfying (E4) of [[thm:uniform-existence]], Data(w) ≤ C_D λ^K. There are
λ0(n) > 0 and M(n), depending on Ω, k, K, C_R, C_D, n and the bounds on the profiles but not on λ, such that for 0 <
λ ≤ λ0(n) the solution g of Ric^H(g) = 0 with these data exists on Ω, is unique there among C² solutions with |g − g0|
≤ ε1, is smooth if the data are, and

    w = h + Σ_A φ_A Y_A,      𝒩_n(τ) ≤ M(n) λ^K   on [τ0, τ_end],                                {#eq:vlasov-n-remainder}

𝒩_n the energy [[eq:two-dust-energy]] summed over the n families, the norms of φ_A and Ψ_A taken on 𝒱_A ∩ Σ_τ
((v) (c)), and φ_A Y_A extended by zero off 𝒯_A. In particular |w| ≤ M(n) λ^(K−3) and |∂w| ≤ M(n) λ^(K−4) on Ω.

*Proof.* The proof of [[thm:two-dust-uniform]], with these changes.

(1) *The decomposition.* The phase shifts solve n transports ℓ_A·dφ_A = ½ 𝒫 s_A(h) on 𝒱_A, φ_A = 0 on 𝒱_A ∩ Σ_τ0, coupled
through the bounded maps φ ↦ 𝒫([Y_B(ℓ_A, ℓ_A)] φ) of [[eq:mollifier-m1]], the product [Y_B(ℓ_A, ℓ_A)] φ_B extended by
zero off 𝒯_B and the result restricted to 𝒱_A; on slabs of a length independent of the data the coupled map is a
contraction in the norms on the 𝒱_A ∩ Σ_τ, by (v) (a), and Picard's theorem gives the decomposition. For the bounds of
Step 1 of [[thm:two-dust-uniform]] on φ_A Y_A, write it as (χ_A φ_A) Y_A with χ_A a smooth cut-off equal to 1 on 𝒯_A
and vanishing off the tube of int S_A, independent of λ, and apply Sobolev's inequality to χ_A φ_A on Σ_τ.

(2) *The term of order λ⁻¹.* The part of order λ⁻¹ of the linearisation is ½ λ⁻¹ Σ_A s_A(h) G2^A, linear in the waves,
as in (L1) of [[lem:two-dust-facts]].

(3) *The ℓ_A ⊗ ℓ_A component.* Contracting the equation for h with ℓ_A ⊗ ℓ_A, ℓ_A = g0⁻¹du_A on the whole of Ω, kills
family A's term of order λ⁻¹ and its □̃φ_A term, as for one family: they carry G2^A and G1^A, which vanish off 𝒯_A, and
on 𝒯_A, ℓ_A is null and G1^A(ℓ_A, ·) = G2^A(ℓ_A, ·) = 0. Every B ≠ A remains exactly as the other family remains in
[[lem:two-dust-ell-ell]]: ½ λ⁻¹((1 − 𝒫) s_B(h)) G2^B(ℓ_A, ℓ_A) = O(∂ s_B(h)) and λ⁻¹((ℓ_app^B − ℓ_B)·dφ_B)
G2^B(ℓ_A, ℓ_A) = O(|dφ_B|), with Ψ_B := □̃φ_B carrying a bounded coefficient. The torus part of W_B vanishes on vectors
of the orbit space, so G2^B(ℓ_A, ℓ_A) is the contribution of the gauge part, ν_B² [∂²_(θ_B) χ_B] (ℓ_A·du_B)², a
bounded profile in θ_B alone, as for two families ([[lem:two-dust-facts]] (L4)).

(4) *The transport of Ψ_A.* On 𝒱_A, where u_A is an eikonal, Ψ_A := □̃φ_A satisfies L_A Ψ_A + a_A Ψ_A = □̃f_A −
𝔐_A(f_A) − 𝔑_A φ_A by [[cor:vlasov-commutator]], with f_A := ½ 𝒫 s_A(h); its coefficients are bounded on 𝒱_A, which
lies at distance at least δ from the axes by (iv).

(5) *The transport estimates.* Each family's transport field Z_A, with ℓ_A = ℓ_A(τ) Z_A and ℓ_A(τ) ≠ 0 on 𝒱_A since a
null vector is never tangent to a spacelike slice, satisfies on 𝒱_A the estimate of [[lem:two-dust-transport]] with
c x̂ replaced by the spatial part of Z_A, by (v) (a). Its boundary terms vanish on the part of the boundary of 𝒱_A ruled
by integral curves of ℓ_A, and are nonpositive on the lateral boundary of Ω by (Ω): at {r = a}, r decreases along future
causal curves, and at the outer boundary v + τ increases, which is b′(τ) − dr(Z_A) < 0 there. So the estimate holds for
every family, whatever its direction.

(6) *Closing.* Every term of the n-family linearisation is a term of one of the types of the two-family estimate, with
its family labels replaced; and the bound of each type in the bootstrap (its power of λ, its number of derivatives, the
part of the energy that controls it) depends on the type alone. From stage 1 on, terms carry three or more families;
they are products of profiles of the same orders, and a product of oscillating profiles at the phases θ_A has m-th
derivatives of order λ^(−m), by the Leibniz rule, whatever the phases. The number of terms is finite for each n and
enters only the constants. So Steps 4–7 of [[thm:uniform-existence]], in the form of [[thm:two-dust-uniform]], give
𝒩_n(τ) ≤ C3(n)((C_D + 1 + C_R) λ^K + C(n) M² λ^(K+1)), and the bootstrap closes with M(n) := C3(n)(C_D + 1 + C_R) + 1
and λ0(n) so small that C3(n) C(n) M(n)² λ0(n) ≤ 1. Existence, uniqueness and smoothness follow as in
[[thm:uniform-existence]]. ∎

**Remark {#rem:vlasov-boundary-instance}** (The boundary signs on Tangherlini.) For g0 = η + (μ/r²) dv ⊗ dv, μ > 0 and
any future null vector l with l(τ) = 1, radial or not, dr(l) ∈ [−1, (r² − μ)/(r² + μ)]. Indeed, writing l = ∂_τ + w with
w spatial, w_r := x̂·w, the null condition is −1 + |w|² + (μ/r²)(1 + w_r)² = 0, so with |w|² ≥ w_r² and 𝔪 := μ/r²,
(1 + 𝔪) w_r² + 2𝔪 w_r + 𝔪 − 1 ≤ 0, whose roots are −1 and (1 − 𝔪)/(1 + 𝔪). So at the outer boundary, b′ = −2,
b′ − dr(l) ≤ −1, and at r = a < √μ, dr(l) ≤ (a² − μ)/(a² + μ) < 0: both boundary terms of step (5) have the right sign
for every family on Tangherlini. For a general g the signs come from (Ω).

**Theorem {#thm:vlasov-n-data}** (Data with overlapping families.) Under (i)–(iv), with (V3) on Σ_τ0, let K ≥ 6 and
N := K + 10, and let g_app be the approximant of [[thm:vlasov-n-approximant]] with N stages and the stage data of
[[lem:stage-data]], taken family by family as below, in its fixed-phase form. For λ ≤ λ0(n) there is a smooth vacuum
Cauchy datum on Σ_τ0 ∩ Ω, invariant under T² and both reflections, with the gauge condition imposed through ∂_τ g, whose
w := g − g_app satisfies (E4) of [[thm:uniform-existence]], Data(w) ≤ C λ^K; the n families may overlap anywhere on
Σ_τ0.

*Proof.* *The approximant's data.* The gauge hierarchy is that of [[lem:gauge-hierarchy]] with n phases: the oscillating
part at each order is a transport along each generator for the pure harmonics, posed on 𝒱_A for family A by (v) (a),
and algebraic, with the divisor Q_j ≠ 0, for the mixed ones, which therefore take no data. The stage data are those of
[[lem:stage-data]] for each family's covector, its proof applied with the polarisation map Pol_A(Z) := ν_A (Z(ℓ_A, ·) −
½ du_A tr Z) of each family, onto at every point of 𝒱_A ∩ Σ_τ0 by the argument given there (with a null vector k_A,
du_A(k_A) = 1, and a covector ζ_A with ζ_A(ℓ_A) = 0 and g0⁻¹(ζ_A, ζ_A) = 1); Pol_A⁺ acts pointwise on terms that carry
harmonics of θ_A, which vanish off supp F_A ∩ Σ_τ0 by (v) (b), by induction on the stage, so the stage data of the pure
harmonics of family A vanish there, as [[thm:vlasov-n-approximant]] asks. The linear solves of its step (iii) have
coefficients independent of λ (θ-means of profile functions), so [[lem:linear-evolution]] applies to them as stated;
the mixed harmonics take no data and need not vanish on Σ_τ0, which no step uses. So, as in [[lem:gauge-hierarchy]],
the constraint map of the data (γ, κ) of g_app on Σ := Σ_τ0 ∩ Ω is λ^(N−2) times a function of the form [h] of
[[sec:vlasov-scaled]], with the phases φ_A := ν_A u_A|Σ (the phase corrections vanish on Σ_τ0). The data (γ, κ) are
polynomials in λ whose coefficients are of the form [h]; they carry every family's wave, whose gauge part vanishes on
Σ_τ0 with its θ-derivatives ([[def:vlasov-wave]]), so that W_A and κ1_A on Σ_τ0 are torus-polarised, and the second
and mixed harmonics at order λ².

*The structure.* Let 𝔉(U) := 𝒞(γ_U, κ_U). By [[lem:vlasov-structure]] (with 𝒯 = 0) it has the structure
[[eq:vlasov-structure]]. Its coefficients are smooth functions of the values of γ, ∂γ, ∂²γ, κ and ∂κ, so they are of the
form [h] except for the terms carrying a factor λ⁻¹, which come from ∂²(λ W_A) in ∂²γ and from ∂κ1_A in ∂κ, enter
linearly, and by [[lem:vlasov-constraint-coefficient]] (b) are, for every U, λ⁻¹ times traces of order λ (α dr ⊗ dr
has no torus components), hence of the form [h]; the second and mixed harmonics enter at order λ⁰ by
[[lem:vlasov-constraint-coefficient]] (a). So f and g̃ are of class 𝔏 and 𝔉(0) = 𝒞(γ, κ). By
[[lem:vlasov-leaf-curvature]], p, P, A0, A^B and 𝒮 are of class 𝔓, with parts of order λ⁰ those of the data (γ0, κ0)
of g0. The signs: at (γ0, κ0) and α = 0, p > 0 by (V3), P = γ0^(rr) Π0^(AB) is positive definite, and 𝒮A0 > 0 with
𝒮A^C symmetric by [[lem:vlasov-symmetrizer]]; by continuity in α these hold with constants p0, δ_e, A00 for |α| ≤ η0,
and for λ ≤ λ1 the terms λ[h] change them by at most half.

*The correction.* Take k := 18 in [[prop:vlasov-scaled-correction]]. Since 𝒞(γ, κ) = λ^(N−2)[h], ε := sup_r
‖𝒞(γ, κ)‖_(18) ≤ C λ^(N−2) by (C0), and ε ≤ η λ⁴ for λ ≤ λ0, as N − 2 > 4. So there is a smooth U with zero data at
r = a, 𝒞(γ_U, κ_U) = 0 and ‖U‖_(𝒴_18) ≤ C λ^(N−2), invariant under T² and both reflections, which act on S³ by
isometries commuting with 𝔉.

*The derivatives in r.* We show that for i ≥ 0 and words I with 2i + |I| ≤ 14,

    ‖λ^(2i+|I|) ∂_r^i 𝓛^I α‖_(L²((a,b1);L²(S³))) + ‖λ^(2i+|I|) ∂_r^i 𝓛^I w‖_(L²((a,b1);L²(S³)))
        ≤ C λ^(N−2).                                                                               {#eq:vlasov-data-dr}

Solving 𝔉(U) = 0 for ∂_r α and ∂_r w, and substituting the first into the second,

    ∂_r α = G_α(x, 𝔍),      ∂_r w = G_w(x, 𝔍),      𝔍 := (α, ∇α, ∇²α, w, ∇w),

with G_α = P̂ ∇²α − p⁻¹ g_ρ and G_w = −B^C ∇_C w − A0⁻¹ (f G_α + g_J), P̂ := P/p and B^C := A0⁻¹A^C taken at α; here g =
𝔉(0) + g̃, with 𝔉(0) = λ^(N−2)[h]. Give the factor ∇^m α the weight (m − 2)₊ := max(m − 2, 0) and ∇^m w the weight m. By
induction on i, ∂_r^i U is a finite sum of terms λ^(−β) c(x, α, ∇α, w) Π_(s=1)^l ∇^(m_s) Y_s, Y_s ∈ {α, w}, with c of
class 𝔏, or of class 𝔏 times a derivative of 𝔉(0), β plus the sum of the weights at most 2i, and l ≥ 1 unless c is of
class 𝔏 times a derivative of 𝔉(0) (a class-𝔏 term without factors vanishes at U = 0, as g̃ does, and Taylor's formula
writes it as a sum of terms with one factor α, ∇α or w): for i = 1 this is the form of G_α and G_w (weights 0 and 1);
applying ∂_r to a term, ∂_r of the x-dependence of c costs λ⁻¹ by (C0); ∂_r of an argument α, ∇α or w of c gives a factor
G_α, ∇G_α or G_w, of weight at most 1; and ∂_r ∇^m α = ∇^m G_α and ∂_r ∇^m w = ∇^m G_w raise the weight of the factor by
at most 2. Apply λ^(2i+|I|) 𝓛^I to such a term and expand by (K4) and the chain rule. Since λ ≤ 1, λ^(2i−β) is at most λ
to the sum of the weights, so every factor appears as λ^(|J|+(m−2)₊) 𝓛^J ∇^m α, of L²(S³) norm at most C
‖α‖_(|J|+(m−2)₊;2), square integrable in r, or as λ^(|J|+m) 𝓛^J ∇^m w, of norm at most C ‖w‖_(|J|+m) at each r, by (K2),
(N3) and (N4); the derivatives of c contribute at most C λ^(N−2) for c of class 𝔏 times a derivative of 𝔉(0) and at most
C otherwise. The orders |J| + (m − 2)₊, respectively |J| + m, add up to at most 2i + |I| ≤ 14, so at most one factor has
order greater than 7: it is taken in L², at order at most 14 ≤ 18, and the others in sup norm, where by (N1), (N2) and
(K2) (which bounds ∇²𝓛^J α by first derivatives of 𝓛_i 𝓛^J α) they are at most C λ⁻³ ‖U‖_(𝒴_18) ≤ C λ^(N−5) ≤ 1 at each
r. This gives [[eq:vlasov-data-dr]].

*The datum.* Put g on Σ as in [[sec:data-proof]]: the spatial part γ + α dr dr, the lapse and shift of g_app's
two-scale form, ∂_τ of the spatial part fixed by κ + ϖ Π + q ⊗ dr + dr ⊗ q, and ∂_τ of the lapse and shift fixed by
D(g) = 0. Then the constraints hold exactly, D = 0, and by [[eq:data-constraint-gauge]] ∂_τ D = 0 on Σ for the solution
of Ric^H = 0 with these data. As in [[sec:data-proof]], w′ := g − G on Σ, G the two-scale form, has spatial part α dr ⊗
dr, ∂_τ of its spatial part a combination of (ϖ, q) and of first tangential derivatives of α, components w′_(τ·)
algebraic in α, and ∂_τ w′_(τ·) fixed by the linear relation D(g) − D(G) = −D(G) = O(λ^(N−1)) with invertible
coefficient. A Cartesian derivative of order j on Σ is a combination, with coefficients bounded with all their
derivatives (r ≥ a > 0), of ∂_r^i 𝓛^I with i + |I| ≤ j, by (K2); and λ^(i+|I|) ≤ λ^(−i) λ^(2i+|I|). So, by
[[eq:vlasov-data-dr]] with 2i + |I| ≤ 14, Σ_(j≤7) λ^j ‖∂^j (α, ϖ, q)‖_(L²(Σ)) ≤ C λ^(−7) λ^(N−2), and Data(w′) ≤
C λ⁻¹ λ^(N−9) = C λ^(N−10) = C λ^K. The two-scale form and the fixed-phase form differ by O(λ^(N+1)) in scaled norms, as
in the proof of [[thm:two-dust-approximant]], so Data(w) ≤ C λ^K: (E4). The datum is smooth and invariant, U being so.

*No division on the slice.* The phases are the background's eikonals, with corrections φ_A = 0 on Σ_τ0, and the initial
value of Ψ_A is fixed by its transport, which divides only by ℓ_A(τ) ≠ 0. Nothing prescribes the eikonal's data against
a parametrix. The only divisors are the spacetime symbols Q_j; for an antipodal pair of labels of equal energy E,
2 ν_A ν_B g0⁻¹(k_A, k_B) = −4 ν_A ν_B E² ≠ 0. ∎

**Remark {#rem:vlasov-n-odd}** (Odd n.) [HL25] prescribe the data of their eikonals on the initial slice through the
symbol of Δ − (cos α_A ∂_1 + sin α_A ∂_2)², and bound below the divisors (ν_B sin(α_A − α_B))², which vanish for an
antipodal pair; this is the one place where they need n odd [HL25, (7.24)–(7.32), pp. 27–28, and footnote 10]. In
[[thm:vlasov-n-data]] that divisor does not arise, so n odd is not needed there; the diagonal of [[sec:vlasov-proof]]
takes n odd at no cost.

### Proof of the theorem {#sec:vlasov-proof}

*Proof of [[thm:vlasov]].* By [[prop:vlasov-uniform-n]], for n ≥ n0 the n-dust approximant g^(n) exists on Ω, with labels
α_A = 2πA/n and |g^(n) − g|_(C¹(Ω)) ≤ C_k n^(−k) for every k; its families' covectors are within C_k n^(−k) of the
continuum's du_(α_A) on their tubes 𝒯_A of int S_(α_A). Fix compact sets S′ and S″ with supp q ∩ (Σ_τ0 × S¹) ⊂ int S″,
S″ ⊂ int S′ and S′ ⊂ int S. Fix an odd n ≥ n0, enlarged if necessary, and check the setting of [[sec:vlasov-n]] for
g^(n), with S_A := S″_(α_A) and F_A := q_A^(1/2), and (i)–(iv). The tube 𝒱_A of S″_(α_A) for u_A is a compact subset of
𝒯_A, which is relatively open in Ω, so u_A is an eikonal near 𝒱_A; it is extended to a smooth invariant function on Ω
by a cut-off equal to 1 near 𝒱_A and vanishing off 𝒯_A. F_A is transported, and vanishes off the tube of
supp F_A ∩ Σ_τ0 ⊂ int S″_(α_A), by [[prop:vlasov-uniform-n]] and (iii) below. Rays are compared as follows: the ray of
u_A for g^(n) and that of u_(α_A) for g from a point of S_(α_A) are null geodesics whose metrics differ by C_k n^(−k)
in C¹ and whose initial covectors, the future roots over the same spatial covector, differ by C_k n^(−k); so they stay
within C n^(−k) of each other while both are in Ω, and as both leave Ω transversally through its lateral boundary, every
point of one in Ω is within C n^(−k) of a point of the other in Ω. In particular 𝒱_A lies within C n^(−k) of
D_(α_A)(S″) ⊂ D_(α_A)(S).

(i) (Ω) is a finite set of strict inequalities on the compact Ω̄, continuous in g in C¹, so it holds for g^(n) for n
large.

(ii′) Let y be a point where the supports of the families A and B of g^(n) overlap. By the comparison of rays, y is
within C n^(−k) of a point of D_(α_A)(S″), where u_(α_A) is an eikonal of g on a neighbourhood of uniform size by (V1);
so the ray of u_(α_A) for g through y, followed to the past, stays in Ω and meets Σ_τ0 within C n^(−k) of S″_(α_A), and
for n large y ∈ D_(α_A)(S′); likewise y ∈ D_(α_B)(S′). By [[lem:vlasov-separation]] with S′, the modulus of the mixed
symbol g⁻¹(du_(α_A), du_(α_B))(y) is at least c0 (2π/n)², so |g^(n)⁻¹(du_A, du_B)(y)| ≥ c0 (2π/n)² − C_k n^(−k) ≥
½ c0 (2π/n)² for n large (k = 3). So c := ½ c0 (2π/n)², and Λ = Λ(n) is chosen as in (ii′).

(iii) The wave of each label is the wave W_A of [[def:vlasov-wave]] of the dust (u_A, F_A) of g^(n) at frequency ν_A,
F_A² = q_A the density (F_A smooth, being transported by [[eq:vlasov-amplitude]] from the smooth data (2π/n)^(1/2)
F(·, α_A)).

(iv) Every 𝒱_A lies within C n^(−k) of D_(α_A)(S), at distance at least 2δ from the axes by (V2), hence at distance at
least δ for n large.

(V3) holds for g^(n), being an open condition on the slice data ([[lem:vlasov-open]]), which are within C_k n^(−k) of
those of g. So [[thm:vlasov-n-approximant]], [[thm:vlasov-n-uniform]] and [[thm:vlasov-n-data]] give vacuum metrics
g^(n)_λ on Ω, λ ≤ λ0(n), invariant under T² and both reflections (by uniqueness, the data being invariant), with

    |g^(n)_λ − g^(n)| ≤ C(n) λ,      ∂g^(n)_λ − ∂g^(n) = Σ_A ν_A du_A ⊗ [∂_(θ_A) W_A] + O(C(n) λ),

W_A the wave of family A at its phase θ_A = ν_A u_A/λ, of zero mean in θ_A, with |ν_A ∂_(θ_A) W_A| ≤ C(F_A + F_A²),
C independent of n and A. Indeed the torus part of ν_A ∂_(θ_A) W_A is −2 F_A sin θ_A T0, and its gauge part is
ν_A³ c_A cos 2θ_A du_A ⊗ du_A, where, by [[def:vlasov-wave]], ℓ_A(ν_A³ c_A) + ½ (□5 u_A) ν_A³ c_A = F_A² with zero data;
since F_A² is transported along the same generator, F_A²(s′) = F_A²(s) exp(∫_(s′)^s □5 u_A), the solution is at most
C F_A² at each point, C depending only on bounds for □5 u_A and for the length of the generators in Ω, which are uniform
in n and A.

*The diagonal.* Fix a sequence (η_j) of smooth tensor fields with compact support in the interior of Ω, dense in L²(Ω).
For each odd n ≥ n0 choose λ_n ≤ λ0(n) such that:

1. C(n) λ_n ≤ 1/n;
2. |∫_Ω η_j · (∂g^(n)_(λ_n) − ∂g^(n))| ≤ 1/n for j ≤ n. This is possible since each harmonic's integral is O(λ) at fixed
   n, by non-stationary phase: du_A ≠ 0 on the support, so e^(i k ν_A u_A/λ) = (λ/(i k ν_A |du_A|²_E)) du_A·∂ e^(i k ν_A
   u_A/λ) with the Euclidean norm of the chart, and one integration by parts gains λ;
3. ‖Σ_A ν_A du_A ⊗ [∂_(θ_A) W_A]‖²_(L²) ≤ Σ_A ‖ν_A du_A ⊗ [∂_(θ_A) W_A]‖²_(L²) + 1. The cross terms of distinct families
   have the phases ν_A u_A ± ν_B u_B, with d(ν_A u_A ± ν_B u_B) ≠ 0, since du_A, du_B are null and not parallel on the
   overlaps by (ii′); they tend to zero as λ → 0 at fixed n, by non-stationary phase.

The diagonal terms are at most C Σ_A ∫ |du_A|²_E (F_A² + F_A⁴), and F_A² = (2π/n) q(·, α_A) + O(n^(−k)) on the tubes by
[[prop:vlasov-uniform-n]]; so they are at most C Σ_A (2π/n) ∫ q(·, α_A) |du_(α_A)|²_E + C/n + O(n^(1−k)), and the sum is
a label quadrature of ∫∫ q |du_α|²_E dα, bounded independently of n by [[lem:vlasov-trapezoid]]. Put g_i :=
g^(n_i)_(λ_(n_i)) along the odd n_i → ∞. Then:

- |g_i − g| ≤ |g^(n_i)_(λ_(n_i)) − g^(n_i)| + |g^(n_i) − g| ≤ 1/n_i + C_k n_i^(−k) → 0 uniformly on Ω;
- ‖∂g_i‖_(L²) ≤ ‖∂g^(n_i)‖_(L²) + (Σ_A ‖ν_A du_A ⊗ [∂_(θ_A) W_A]‖²_(L²) + 1)^(1/2) + 1, bounded independently of i;
- for each j and n_i ≥ j, |∫ η_j · (∂g_i − ∂g)| ≤ 1/n_i + |∫ η_j · (∂g^(n_i) − ∂g)| ≤ 1/n_i + C_k n_i^(−k) ‖η_j‖_(L¹),
  which tends to zero.

A sequence bounded in L² that converges against a dense set converges weakly: ∂g_i ⇀ ∂g in L²(Ω). Each g_i is vacuum,
smooth and invariant under T² and both reflections. ∎

The high-frequency step is not uniform in n: λ0(n), M(n) and C(n) depend on n, as the constants c^n n^n of
[HL25, p. 5, footnote 5] do. Only the background step is uniform ([[prop:vlasov-uniform-n]]), which is what the diagonal
needs. No smallness threshold enters: the theorem is a large-data statement, its smallness at each n being λ alone.

### Openness, stability and an explicit family {#sec:vlasov-open}

**Lemma {#lem:vlasov-open}** (The hypotheses are open.) Let (g, F, u) satisfy (Ω) and (V3), and let S ⊂ (Σ_τ0 ∩ Ω) × S¹
be compact (points and labels) with supp q ∩ (Σ_τ0 × S¹) ⊂ int S. Suppose that on S and its tubes: u is an eikonal in
each label, with ℓ_α future directed, on a neighbourhood in Ω × S¹ of 𝒟(S); the Jacobian of (V1) is at least J0 on the
tubes D_α(S); ∂_α β0 ≥ b_* on S, and β0(x, ·) is injective on S_x; and dist(D_α(S), axes) ≥ 2δ. Then there is a
neighbourhood 𝒰 of (g, u|Σ_τ0, ∂u|Σ_τ0) in C² × C¹ with the following property. Let (g′, F′, u′) be a solution whose
metric on Ω and data lie in 𝒰, with supp q′ ∩ (Σ_τ0 × S¹) ⊂ int S, and let u″_α be the eikonal of g′ with the data
u′_α|Σ_τ0 and the future branch, on the points of Ω on its rays from a neighbourhood of S_α. It is defined and smooth
in (x, α) on a neighbourhood in Ω × S¹ of the set 𝒟′(S) of the (x, α) with x in the tube D′_α(S) of S_α for u″_α, and
it agrees with u′_α, with all derivatives, where q′(·, α) > 0. So replacing u′ by χ u″ + (1 − χ) u′, χ a smooth
invariant cut-off on Ω × S¹ equal to 1 near 𝒟′(S) and vanishing off the domain of u″, changes neither T_V nor
[[eq:vlasov-amplitude]] (which holds where q′ > 0, hence on its closure, and trivially elsewhere), and after this
replacement (g′, F′, u′) satisfies (V1) on S with the margins J0/2 and b_*/2, and (V2) with δ/2 in place of δ, that is
dist(D′_α(S), axes) ≥ δ. (Ω) and (V3) are open in C² × C¹.

*Proof.* The tubes are the images of S under the flows of the rays of u″, which are null geodesics of g′ with initial
covectors given by ∂u′|Σ_τ0, the τ-component being the future root. The rays and their first variation (whose
determinant is the Jacobian) solve ordinary differential equations whose coefficients are the Christoffel symbols of g′
and their first derivatives, so by continuous dependence on coefficients and data they depend continuously on (g′, u′) in
C² × C¹, uniformly on the compact S × [τ0, τ_end]; β0 and ∂_α β0 depend continuously on u′|Σ_τ0 in C¹. The Jacobian, the
margin b_* and the distance to the axes are infima over compact sets of continuous positive functions, so on a
neighbourhood they hold halved, also on a fixed neighbourhood of S. Where the Jacobian is positive the rays from a
neighbourhood of S_α foliate a neighbourhood of D′_α(S), uniformly in α, so the eikonal u″_α of g′ with the data
u′_α|Σ_τ0 exists there (the method of characteristics), and it is smooth in (x, α), the rays depending smoothly on their
initial points and on α; this is why the margins are asked on S and not only on supp q, the tube of supp q′ lying inside
that of S. The label form's u′_α is an eikonal of g′ near the tube of supp q′(·, α) ∩ Σ_τ0 with the same data and
branch. So the ray of u′_α from a point x0 of that set is the null geodesic of g′ from x0 with the covector du′_α(x0) =
du″_α(x0), also the ray of u″_α from x0; along it both functions are constant, with the value u′_α(x0). Hence u′_α =
u″_α on that tube, which contains the open set where q′(·, α) > 0, and there all derivatives agree. Injectivity is
kept: if α_k ≠ α′_k in S_(x_k) had β0′_k(x_k, α_k) = β0′_k(x_k, α′_k) for perturbations tending to zero, a limit point
would give, by injectivity of β0(x, ·), α = α′, and then for k large α_k and α′_k lie in an interval on which
∂_α β0′_k ≥ b_*/2 > 0, a contradiction. (Ω) consists of strict inequalities between contractions of g⁻¹, continuous
in C⁰, and of the statement on generators, which holds for the tubes by their definition; (V3) consists of strict
inequalities between functions of the slice data and their first derivatives. ∎

**Proposition {#prop:vlasov-cauchy}** (Cauchy stability of the restricted system off the axes.) Let (g̊, F̊, ů) be a
smooth class Einstein–restricted massless Vlasov solution on Ω in label form satisfying (Ω), (V1), (V2) and (V3), with
the compact set S of (V1); F̊ may vanish identically. Fix m ≥ 6. There are ε0 > 0, ε2 ∈ (0, ε1] and C such that every
smooth datum D in label form near (g̊, F̊, ů), as defined before [[prop:vlasov-uniform-n]], with d(D) ≤ ε0, has a smooth
class development (g, F, u) on Ω, invariant under T² and both reflections: a solution of the Einstein–restricted
massless Vlasov system in label form with Ric^H(g) = T_V, the gauge of [[sec:class-augmented]] relative to g̊, with
‖g − g̊‖_(H^(m+1)) ≤ C d(D) on every Σ_τ, and with each u_α the eikonal of g with the data u_D(·, α) on a neighbourhood
in Ω × S¹ of the (x, α) with x in its tube D_α(S). Its metric and field are unique: every such solution (g′, F′, u′)
whose metric is within ε2 of g̊ in C² and whose data are those of D has g′ = g and F′ = F, and u′_α = u_α on the tube of
supp q(·, α) ∩ Σ_τ0, for every α. No smallness of the reference is assumed.

*Proof.* *Existence.* For n ≥ n0 let g^(n) be the development of the n-dust datum D_n of D given by
[[prop:vlasov-uniform-n]], with (g̊, F̊, ů) as reference and k = 2: it exists on Ω and ‖g^(n) − g̊‖_(H^(m′+1)) ≤ C_(m′)
(d(D) + n⁻²) on every Σ_τ, for every m′ ≥ m, with C_(m′) independent of n. The energy [[eq:class-energy]] contains the
τ-derivatives, so by Sobolev's inequality on the slices ([[lem:sobolev]], with λ = 1) the g^(n) are bounded in C^j(Ω̄)
for every j, uniformly in n, and by the Arzelà–Ascoli theorem and a diagonal argument a subsequence converges in C^j(Ω̄)
for every j to a smooth metric g, invariant under T² and both reflections, with ‖g − g̊‖_(H^(m+1)) ≤ C d(D) on every
Σ_τ. For α ∈ S¹ let u^(n)_α be the eikonal of g^(n) with the data u_D(·, α) (the future root), which exists on a
neighbourhood in Ω × S¹ of the (x, α) with x in its tube D^(n)_α(S) by the proof of [[lem:vlasov-open]], g^(n) being
C²-close to g̊ and u_D C¹-close to ů on Σ_τ0, and F^(n)_α the solution of [[eq:vlasov-amplitude]] for g^(n) with the
data F_D(·, α), along the rays of u^(n)_α, vanishing off the tube of supp F_D(·, α); they are smooth in (x, α), with
derivatives bounded uniformly in n, the rays depending smoothly on g^(n) and on the data. For α = α_A, u^(n)_α agrees
on the tube 𝒯_A of int S_(α_A) with the eikonal u_A of the family A of g^(n), by the argument of the proof of
[[lem:vlasov-open]]: both are eikonals of g^(n) there with the same data and the future branch, so they have the same
rays from int S_(α_A), along which both are constant. The density q_A, supported in 𝒯_A, solves div(q_A g^(n)⁻¹du_A) =
0, which is [[eq:vlasov-amplitude]] for (q_A/(2π/n))^(1/2) by [[eq:vlasov-dust]], so q_A = (2π/n) (F^(n)_(α_A))². So,
with h^(n)(x, α) := F^(n)_α(x)² du^(n)_α ⊗ du^(n)_α (zero off the tubes), Ric(g^(n)) = (2π/n) Σ_A h^(n)(·, α_A). Along
the subsequence the null geodesic flows of g^(n) converge with their derivatives to that of g, so u^(n)_α → u_α and
F^(n)_α → F_α in C¹, uniformly in α, where u_α is the eikonal of g with the data u_D(·, α) on a neighbourhood of the
(x, α) with x ∈ D_α(S), extended smoothly to Ω × S¹ by a cut-off as in [[lem:vlasov-open]], and F_α solves
[[eq:vlasov-amplitude]] along its rays with the data F_D(·, α); and h^(n) → h := F_α² du_α ⊗ du_α uniformly. The
Riemann sum error is |(2π/n) Σ_A h^(n)(x, α_A) − ∫ h^(n)(x, α) dα| ≤ Σ_A ∫_(arc A) |h^(n)(x, α_A) − h^(n)(x, α)| dα ≤
2π (2π/n) sup |∂_α h^(n)| → 0, the arc A being the set of α with α_A − 2π/n ≤ α ≤ α_A. Hence Ric(g), the limit of
Ric(g^(n)), is ∫_(S¹) h dα = T_V: (g, F, u) solves the Einstein–restricted massless Vlasov system in label form, F_α
vanishing off the tube of supp F_D(·, α), on which u_α is an eikonal. The g^(n) solve Ric^H(g^(n)) = T^(n) in the gauge
relative to g̊ ([[lem:vlasov-local-stability]]), so g does in the limit, and its data are those of D, since the metric
data of D_n differ from those of D by at most C n⁻² ([[prop:vlasov-scaled-correction]]).

*Uniqueness.* Let (g_i, F_i, u_i), i = 1, 2, be two such solutions, q^i := F_i², and η := ε2 + ε0. By
[[lem:vlasov-open]], for η small, the eikonal û^i_α of g_i with the data u_D(·, α) and the future branch exists, smooth
in (x, α), on a neighbourhood of the (x, α) with x in its tube D^i_α(S), whose distance to the axes is at least δ, and
it agrees with u^i_α, with all derivatives, where q^i(·, α) > 0; q^i(·, α) is transported along its rays and vanishes
off the tube of supp F_D(·, α). So T^i_V = ∫ q^i(·, α) dû^i_α ⊗ dû^i_α dα, and we use û^i in place of u^i.

Fix a compact S′ with supp F_D ⊂ int S′ and S′ ⊂ int S, and put 𝒱_α := D^1_α(S′), the tube of S′_α for û^1_α. For η
small, 𝒱_α ⊂ D^2_α(S), and supp q^1(·, α) ∪ supp q^2(·, α) ⊂ 𝒱_α, for every α. Indeed, extend g_1, g_2 to a
neighbourhood of Ω, C²-close to an extension of g̊, and let y^i_τ and ẙ_τ map a point x0 near S_α to the point where the
null geodesic of g_i, respectively g̊, with the future covector over d(u_D(·, α)|Σ_τ0)(x0), respectively over
d(ů_α|Σ_τ0)(x0), meets Σ_τ, in the coordinates (r, ϑ) of the orbit slices. By the continuous dependence of the proof of
[[lem:vlasov-open]], ‖y^i_τ − ẙ_τ‖_(C¹) ≤ C η, uniformly in (α, τ), and by (V1) Dẙ_τ is invertible with |Dẙ_τ⁻¹| ≤ L
and is uniformly continuous. Let y ∈ 𝒱_α ∩ Σ_τ, y = y^1_τ(x0), x0 ∈ S′_α. Fix d > 0 such that the closed d-neighbourhood
of S′_α in the orbit slice lies in S_α and |Dẙ_τ(x) − Dẙ_τ(x0)| ≤ 1/(4L) for |x − x0| ≤ d. For η small, |Dy^2_τ(x) −
Dẙ_τ(x0)| ≤ 1/(2L) there, so the inverse function theorem gives y^2_τ(B(x0, d)) ⊃ B(y^2_τ(x0), d/(2L)), which contains
y once 2Cη < d/(2L). So y lies on the ray of û^2_α from a point of S_α, and that ray stays in Ω up to y, since a future
causal curve that leaves Ω through its lateral boundary does not return ([[def:class-admissible]] (b)): y ∈ D^2_α(S).
The same argument with the solutions exchanged, and supp F_D(·, α) ⊂ int S′_α in place of S′_α ⊂ int S_α, gives
supp q^2(·, α) lies in the tube of supp F_D(·, α) for û^2_α, inside 𝒱_α; and supp q^1(·, α) lies in that for û^1_α,
inside 𝒱_α.

So both û^i_α are eikonals near 𝒱_α. On 𝒱_α put p^i := dû^i_α, P^i := g_i⁻¹p^i, Θ^i := □_(g_i) û^i_α and q^i_α :=
q^i(·, α), with differences δp_α, δΘ_α, δq_α, and let w := g_1 − g_2. On 𝒱_α, ∇_(P^i) p^i = 0 for g_i, the Raychaudhuri
equation [[eq:class-raychaudhuri]] holds with Ric(g_i)(P^i, P^i) = ∫ q^i_β g_i⁻¹(p^i, dû^i_β)² dβ, in which dû^i_β
enters only on supp q^i_β ⊂ 𝒱_β, and P^i(q^i_α) = −Θ^i q^i_α. Subtracting, along P^1 on 𝒱_α,

    P^1(δp_(α,a)) = P^(1,b) (Γ[g_1] − Γ[g_2])^c_(ba) p^1_c + Γ[g_2]^c_(ba) (P^(1,b) p^1_c − P^(2,b) p^2_c)
                    − (P^1 − P^2)^b ∂_b p^2_a,
    P^1(δΘ_α) = S^1 − S^2 − (P^1 − P^2)(Θ^2),      P^1(δq_α) = −δΘ_α q^1_α − Θ^2 δq_α − (P^1 − P^2)(q^2_α),

S^i the right side of [[eq:class-raychaudhuri]] for g_i. Pointwise, |P^1 − P^2| ≤ C (|w| + |δp_α|); the terms of
S^1 − S^2 other than the Ricci terms are at most C (|w| + |∂w| + |δp_α| + |δΘ_α|), 𝒱_α lying at distance at least δ
from the axes; and the Ricci terms differ by at most C (|w| + |δp_α|) + C ∫ (|δq_β| + 𝟙_(𝒱_β) |δp_β|) dβ. The
constants are uniform in α, the fields being smooth in (x, α). The metrics solve Ric^H(g_i) = T^i_V, so, as in Step 4 of
the proof of [[thm:class-stability-off-axes]], −½ g_1^(ab) ∂_a∂_b w is the sum of terms at most C (|w| + |∂w|) and of
T^1_V − T^2_V = ∫ (δq_α p^1 ⊗ p^1 + q^2_α (δp_α ⊗ p^1 + p^2 ⊗ δp_α)) dα, whose integrand vanishes off 𝒱_α, so that its
L² norm on Σ_τ is at most C (∫ (‖δp_α‖² + ‖δq_α‖²)_(L²(𝒱_α ∩ Σ_τ)) dα)^(1/2) by the Cauchy–Schwarz inequality on S¹.
Put

    𝒩̃(τ) := ‖∂w‖ + ‖w‖ + (∫_(S¹) (‖δp_α‖² + ‖δΘ_α‖² + ‖δq_α‖²)_(L²(𝒱_α ∩ Σ_τ)) dα)^(1/2).

The energy inequality [[lem:energy]] for w, with g̊ in place of g0, and for each α the argument of
[[lem:class-transport]] on 𝒱_α, along the future null P^1 — no flux through the part of the boundary of 𝒱_α ruled by its
integral curves, and a nonnegative flux through the lateral boundary of Ω — with the Minkowski inequality in α, give
𝒩̃(τ) ≤ C (𝒩̃(τ0) + ∫_(τ0)^τ 𝒩̃). The two solutions have the same Cauchy data, completed by the gauge condition as in
the definition of D, so w = ∂w = 0 on Σ_τ0; and δp_α = δΘ_α = δq_α = 0 there, the p^i being the same roots over the
same spatial covectors, their τ-derivatives fixed by the geodesic equation, and q^i_α = F_D(·, α)². So 𝒩̃(τ0) = 0 and,
by Gronwall's lemma, 𝒩̃ ≡ 0: g_1 = g_2, and on 𝒱_α, q^1_α = q^2_α and dû^1_α = dû^2_α, so û^1_α = û^2_α, both being
constant along the common rays from S′_α with the values of u_D. As both q^i_α vanish off 𝒱_α, F_1 = F_2; and u^i_α =
û^i_α on the tube of supp F_D(·, α), the closure of the set where q^i(·, α) > 0. ∎

The explicit family is built on the orbit space of Tangherlini, where the eikonal equation separates. Let μ = 1, f :=
1 − 1/r², 𝔪 := 1/r², and let t := τ − κ(r) with κ′ = 𝔪/f be the static time on r > 1, so that g3 = −f dt² + f⁻¹dr² +
r² dϑ² there. For |α| < 0.7 put k(α) := 3 sin α and

    u_α := −t + k(α)(ϑ − π/4) + ∫_3^r f(s)⁻¹ (1 − f(s) k(α)²/s²)^(1/2) ds,      r > 1.              {#eq:vlasov-witness}

Since f/r² = (r² − 1)/r⁴ ≤ 1/4, with equality at r² = 2 only, and k² < 9 sin² 0.7 < 3.74 < 4, the square root is smooth
and positive on r > 1. We extend u to a smooth invariant function on Ω × S¹ that agrees with [[eq:vlasov-witness]] on
{r ≥ 2} × [−0.65, 0.65]; only its values on a neighbourhood in Ω × S¹ of the (x, α) with x in the tubes of the set S
below, in r ≥ 2.64 and |α| ≤ 0.6, enter.

**Proposition {#prop:vlasov-nonempty}** (The theorem is not vacuous.) Let g0 be Tangherlini of mass 1 in the chart of
[[sec:background]] with μ ≡ 1, and Ω the domain with τ0 = 0, τ_end = 3, a = 4/5 and V = 5. Let F0 ≥ 0 be a smooth
function of (r, ϑ, α), not identically zero, supported in {|r − 3| ≤ 0.3, |ϑ − π/4| ≤ 0.15} × [−0.5, 0.5], and let the
labels be the eikonals [[eq:vlasov-witness]]. Then for every small ε > 0 the class Einstein–restricted massless Vlasov
solution with the field of amplitude ε F0 and labels u_α, its metric data those of g0 corrected by
[[prop:vlasov-scaled-correction]] (λ = 1, no phases) to satisfy the constraints with the stress of the field, exists on Ω
and satisfies (Ω), (V1), (V2) and (V3). By [[lem:vlasov-open]], the solutions covered by [[thm:vlasov]] form a nonempty
open set.

*Proof.* *(Ω) and (V3) for g0.* With μ = 1 the contractions of [[lem:domain]] are g0⁻¹(dτ, dτ) = −1 − 1/r² < 0; at r = a,
g0⁻¹(dr, dr) = 1 − 25/16 = −9/16 < 0 and g0⁻¹(dr, dτ) = 25/16 > 0, so {r = a} is spacelike and r decreases along future
causal curves near it, as in the proof of [[lem:domain]] (b); g0⁻¹(d(v + τ), d(v + τ)) = −3 − 1/r² < 0, and v + τ
increases along future causal curves, as in [[lem:domain]] (c); and b(τ) = 9 − 2τ ≥ 3, so b(τ) − a ≥ 11/5. On Σ_0 the
data of g0 are γ = (1 + 1/r²) dr² + r² dΩ², and by [[lem:constraints-evolution]] (a) the spheres have mean curvature
3/(r² + 1)^(1/2) > 0 and 𝒮 A0 = diag(6, 1/(r² + 1)) > 0. The statement of (Ω) on generators holds for the tubes by their
definition.

*The rays.* Put w := (1 − f k²/r²)^(1/2). Then −u_t²/f + f u_r² + u_ϑ²/r² = −1/f + (1 − f k²/r²)/f + k²/r² = 0, so u_α is
an eikonal for |α| < 0.7, and ℓ_α = g3⁻¹du_α has the components (1/f, w, k/r²) in (t, r, ϑ), future directed on r > 1.
Its rays solve
dt/ds = 1/f, dr/ds = w, dϑ/ds = k/r², and with dτ/dt = 1 + κ′ dr/dt = 1 + 𝔪 w,

    dr/dτ = ṙ(r) := f w/(1 + 𝔪 w),      dϑ/dτ = ϑ̇(r) := f k/(r² (1 + 𝔪 w)),

functions of r alone at fixed α. Let S̃ := {|r − 3| ≤ 0.36, |ϑ − π/4| ≤ 0.18} and S := S̃ × [−0.6, 0.6], so that
supp F0 ⊂ int S. For |α| ≤ 0.6, |k| ≤ 3 sin 0.6 < 1.7, and for r ≥ 2.64, f k²/r² ≤ 2.89/6.9696 < 0.42, so w > 0.76,
f > 0.856 and 𝔪 < 0.1435, and ṙ ≥ f w/(1 + 𝔪) > 0.56. ṙ is increasing in r on r² > 2: f increases, 𝔪 decreases, and
f k²/r² = k²(r² − 1)/r⁴ has derivative 2k²(2 − r²)/r⁵ < 0, so w increases and ṙ = f/(w⁻¹ + 𝔪) has an increasing
numerator and a decreasing positive denominator. On the rays from S̃, r ≥ 2.64 and r increases, and |ϑ̇| ≤ |k|/r² <
1.7/r².

*(V1).* In the coordinates (r, ϑ) the flow map from Σ_0 to Σ_τ is (r0, ϑ0) ↦ (R(τ; r0), ϑ0 + ∫_0^τ ϑ̇(R(s; r0)) ds),
with dR/dτ = ṙ(R), R(0; r0) = r0. Its Jacobian is ∂R/∂r0 = ṙ(R(τ; r0))/ṙ(r0), since both sides solve y′ = ṙ′(R) y with
y(0) = 1; as R ≥ r0 and ṙ increases, it is at least 1 =: J0. On Σ_0, t = −κ(r), so d(u_α|Σ_0) = (κ′ + ϕ′) dr + k dϑ
with κ′ + ϕ′ = (𝔪 + w)/f, ϕ the integral in [[eq:vlasov-witness]]. In the coframe ((1 + 𝔪)^(1/2) dr, r dϑ), orthonormal
for the orbit part (1 + 𝔪) dr² + r² dϑ² of γ, its angle β0 from the outward radial direction satisfies tan β0 =
𝔗(r, k) := k f (1 + 𝔪)^(1/2)/(r (𝔪 + w)). Since ∂_k w = −f k/(r² w),

    ∂_k 𝔗 = (f (1 + 𝔪)^(1/2)/r) ((𝔪 + w) + f k²/(r² w))/(𝔪 + w)² ≥ f/(r (1 + 𝔪)) = (r² − 1)/(r (r² + 1)),

which decreases on r² > 2 + √5 and is > 0.249 on [2.64, 3.36]. There |𝔗| ≤ 1.7 · 1.0694/(2.64 · 0.8485) < 0.82, since
𝔪 > 0.0885 there, so cos²β0 = (1 + 𝔗²)⁻¹ > 0.59; and dk/dα = 3 cos α ≥ 3 cos 0.6 > 2.47. Hence ∂_α β0 = cos²β0 ∂_k 𝔗
dk/dα > 0.59 · 0.249 · 2.47 > 0.36 =: b_* on S, and β0(x, ·) is increasing, so injective: the field is labelled by
initial direction. The tubes of S lie in r ≥ 2.64, so u is an eikonal in each label, with ℓ_α future directed, on the
neighbourhood ({r > 2} × (−0.65, 0.65)) ∩ (Ω × S¹) of 𝒟(S).

*(V2).* A ray from S̃ is in Ω only while r ≤ b(τ) = 9 − 2τ, and r ≥ 2.64 + 0.56 τ on it, so only for τ ≤ 6.36/2.56 <
2.49. Over that time |ϑ − ϑ0| ≤ ∫_0^2.49 1.7 (2.64 + 0.56 s)⁻² ds = (1.7/0.56)(1/2.64 − 1/4.0344) < 0.3975. So on the
tubes of S, ϑ ∈ [0.2078, π/2 − 0.2078], since π/4 − 0.18 − 0.3975 > 0.2078, and r ≥ 2.64; so ρ1 = r cos ϑ and ρ2 =
r sin ϑ are at least 2.64 sin 0.2078 > 0.54 > 0.53 =: 2δ.

*The solutions.* The reference (g0, 0, u), with the zero field and the labels u_α, is a smooth class solution in label
form satisfying (Ω), (V1) on S with J0 = 1 and b_* = 0.36, (V2) with 2δ = 0.53, and (V3), by the preceding steps. The
datum D_ε has the field ε F0, the labels u_α|Σ_0 with the future roots, and the metric data of g0 on Σ_0 corrected to
satisfy the constraints with the stress of the field: 𝔉(U) := 𝒞(γ_U, κ_U) − 𝒯_ε(·, α), 𝒯_ε the constraint stress of ∫ ε²
F0(·, α)² du_α ⊗ du_α dα, has the structure of [[lem:vlasov-structure]] with λ = 1 and no phases, the signs by (V3) and
[[lem:vlasov-symmetrizer]], and sup_r ‖𝔉(0)‖_(20) ≤ C ε², since the data of g0 satisfy the vacuum constraints; so
[[prop:vlasov-scaled-correction]] with k = 20 gives a smooth invariant correction U with ‖U‖_(𝒴_20) ≤ C ε², which at
λ = 1 bounds U in C⁹. Indeed, by the induction in the data step of the proof of [[prop:vlasov-uniform-n]] with 2m = 20,
U is bounded in H^20(S³) and ∂_r^i U in H^(21−2i)(S³), 1 ≤ i ≤ 10, uniformly in r, and H^s(S³) ⊂ C^l(S³) for
s > l + 3/2; as 20 > 9 + 3/2 and 21 − 2i > (9 − i) + 3/2 for i ≤ 9, every ∂_r^i ∂_ω^l U with i + l ≤ 9 is bounded, and
the Cartesian derivatives of order at most 9 are combinations of these with bounded coefficients (r ≥ a > 0). So
d(D_ε) ≤ C ε, and [[prop:vlasov-cauchy]] around (g0, 0,
u), with m = 6, gives for ε small the solution on Ω, with ‖g − g0‖_(H^7) ≤ C ε on every Σ_τ, hence, by Sobolev's
inequality on the slices and the equations for the τ-derivatives, C²-close to g0, and with eikonals C¹-close to u_α. By
[[lem:vlasov-open]], whose eikonals u″ are those of the solution, it satisfies (V1) with the margins J0/2 = 1/2 and
b_*/2 = 0.18 and (V2) with dist(D_α(S), axes) ≥ 0.265, and (Ω), (V3) by openness. ∎

**Remark {#rem:vlasov-test-family}** (Numerical observation.) For the family with data u_α = cos α ρ(r) + 3 sin α ϑ on
Σ_0, ρ′ = (1 + 1/r²)^(1/2), outgoing labels α ∈ [−0.5, 0.5] and ingoing labels α ∈ [π − 0.15, π + 0.15] (inside the
horizon when they leave Ω), and the density on the same ball, the margins were measured on a 9 × 9 grid of rays over the
ball enlarged by 20 %, with 81 labels per interval: J0 = 1.0000 and 0.8978, δ = 0.157 and 0.098, b_* = 0.909. A family
focused at distance 1 ahead had a Jacobian changing sign (least value −0.071); a wider ingoing interval [π − 0.5, π +
0.5] reached an axis inside the horizon, as [[prop:vlasov-axis-focus]] predicts, so (V2) is a real restriction; with
mass 1.02 and directions tilted by 0.02 sin 2ϑ, the margins were J0 = 1.0000 and 0.8471, δ = 0.152 and 0.072. No proof
uses these values.
