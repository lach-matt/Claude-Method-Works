## Restricted massless Vlasov limits {#ch:vlasov}

[[thm:two-dusts]] realises two crossing radial null dusts as high-frequency limits of vacuum metrics of the T²-mirror
class. This chapter treats a continuum of null dusts, that is, massless Vlasov matter. In four dimensions, under a U(1)
symmetry and in an elliptic gauge, Huneau and Luk prove that high-frequency limits of vacuum metrics are solutions of the
Einstein–massless Vlasov system whose measure is restricted to the cotangent bundle of the quotient [HL19, p. 1; p. 13],
and that suitable small, localised, U(1)-symmetric solutions of that system are such limits [HL25, Theorem 1.1, p. 2]. Their
construction approximates the Vlasov field by n null dusts, approximates each Einstein–n-dust solution by vacuum metrics
of frequency 1/λ large compared with n, and joins the two steps along a diagonal [HL25, pp. 3, 19]. Without symmetry,
the construction for finitely many dusts is not uniform in their number [Tou24, p. 4].

We prove the five-dimensional counterpart in the class, without smallness, for fields that stay off the axes. In
[[sec:vlasov-limits]] we show that a
high-frequency limit inside the class has no stress along the torus, so that a massless Vlasov limit in the class is
restricted: its momenta are tangent to the orbit space; if the limit is moreover round, it is a two-dust solution of the
kind of [[thm:two-dusts]]. In [[sec:vlasov-restricted]] we show that restricted particles move on the null geodesics of
the orbit space, and that those reaching an axis off the axial directions focus there, so that the field of a smooth
solution stays off the axes. [[thm:vlasov]] then states: every smooth class Einstein–restricted massless Vlasov solution
whose field is a caustic-free family of dusts labelled by initial direction and off the axes, on a domain of the type
[[eq:omega]] whose initial spheres have positive mean curvature, is a weak limit of class vacuum metrics. The proof has
the two steps of [HL25]. The n-dust approximants of the field are uniform in n ([[prop:vlasov-uniform-n]]); the
high-frequency step is not, and the steps are joined along a diagonal. Four facts make the high-frequency step work for
every n in the class: frequencies 1, Λ, …, Λ^(n−1) remove every resonance among three or more phases up to the order the
scheme uses ([[lem:vlasov-hierarchy]]); waves polarised along the torus leave no term of order λ⁻¹, in the field
equations or in the constraints ([[lem:vlasov-torus-ricci]], [[lem:vlasov-constraint-coefficient]]); the orbit space has
no shear ([[lem:vlasov-no-shear]]); and the constraints, whose coefficients oscillate in every direction of the initial
slice, are solved with bounds uniform in λ in norms in which each angular derivative carries the factor λ that the
oscillation costs ([[prop:vlasov-scaled-correction]]). The last section shows that the hypotheses are open and that an
explicit family on Tangherlini meets them ([[lem:vlasov-open]], [[prop:vlasov-nonempty]]).

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
∂_b ψ[g_i] converge weakly in L²(U), a uniformly
convergent factor times a weakly convergent one, so the identities pass to the limit: ∂_a(√|h0| h0^(ab) ∂_b ψ0) =
∂_a(√|h0| h0^(ab) ∂_b ω0) = 0 in distributions, and classically since g0 is C². That is □_(h0) ψ0 = □_(h0) ω0 = 0 on U,
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
the class (its constants (τ0, τ_end, a, V) fixed and its sets defined by the coordinate functions τ, r, v). A *restricted
field in label form* on Ω is a pair (F, u) of smooth invariant functions on Ω × S¹, F ≥ 0, with density q := F², such
that each u_α := u(·, α) is an eikonal of g on a neighbourhood of the *tube* D_α of supp q(·, α), with g⁻¹du_α future
directed there, and with stress

    T_V := ∫_(S¹) q(·, α) du_α ⊗ du_α dα,                                                          {#eq:vlasov-stress}

and with every amplitude F(·, α) transported by

    2 ℓ_α(F) + (□5 u_α) F = 0,      ℓ_α := g⁻¹du_α,                                              {#eq:vlasov-amplitude}

which is [[eq:vlasov-dust]] for q(·, α) = F(·, α)², as in [HL25, (1.2)]. Here the *rays* of u_α are the integral curves
of ℓ_α, and D_α is the set of points of Ω on the future rays from supp q(·, α) ∩ Σ_τ0 that stay in Ω. Let β0(x, α) be the
angle, in a frame of the orbit slice of Σ_τ0 orthonormal for its induced metric, of the covector d(u_α|Σ_τ0)(x). The
field is *labelled by initial direction* if for every x the map α ↦ β0(x, α) is injective on the labels α with (x, α) ∈
supp q. T_V is the stress of the restricted field μ_x := ∫ q(x, α) δ_(du_α(x)) dα, and each label is a null dust.
Replacing u_α by −u_α changes neither T_V nor [[eq:vlasov-amplitude]], so the time orientation of ℓ_α only fixes a sign.
It fixes the *branch* of the eikonal equation used below: given the restriction of u_α to Σ_τ0, of nonzero differential,
the τ-derivative of u_α there is the root of g⁻¹(du_α, du_α) = 0 for which g⁻¹du_α is future directed. (With n the
future unit normal of Σ_τ0, the two roots are du_α(n) = ±|d(u_α|Σ_τ0)|, and g⁻¹du_α is future directed exactly when
du_α(n) < 0.)

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

*Proof.* Suppose that f > 0 at a null direction whose geodesic reaches x0 transversally. Let P be the fixed set {x2 = x4
= 0} of the two reflections, a three-dimensional submanifold with coordinates (τ, x1, x3). It meets every orbit near x0,
at the points (τ, ±ρ1, ±ρ2). The Killing fields ∂_(φ1), ∂_(φ2) are along ∂_2, ∂_4 at the points of P and orthogonal to P
by the reflection symmetry, so on {x1 > 0, x3 > 0} the induced metric g_P of P is g3 in the coordinates (τ, ρ1, ρ2) =
(τ, x1, x3). As g5 is C², g_P is a C² Lorentzian metric on P, even in x3: g3 extends across the edge {ρ2 = 0} to g_P, and
the null geodesic flow of g3 extends to the flow of g_P, which is C¹, under which the geodesic reaching x0 transversally
crosses {x3 = 0}. In the coordinates of P, κ is the same function of g_P and its first derivatives, so it is continuous
on the bundle of null directions of g_P over a neighbourhood of x0. Hence f, which equals its initial value times
exp(−∫κ) along each flow line, stays positive along the flow line of the given direction, and, by continuity, f ≥ c1 > 0
on a neighbourhood U of the arriving direction at the points of the geodesic near x0. So T3(e0, e0) ≥ ∫_U f (p(e0))² ≥
c2 > 0 there, for a timelike vector field e0. The Killing field ∂_(φ2) = x3 ∂_4 − x4 ∂_3 has, at points of P, e^(2ψ2) =
g5(∂_(φ2), ∂_(φ2)) = x3² (g5)_(44) = ρ2² (g5)_(44), with (g5)_(44) > 0, and e^(ψ1) is bounded near x0 since ρ1(x0) =
r(x0) > 0. So T(e0, e0) = e^(−ψ1−ψ2) T3(e0, e0) ≥ c/ρ2 at the points of the geodesic near x0, with c > 0. But Ric(g5)
is continuous near x0, so Ric(g5)(e0, e0) is bounded there: a contradiction. ∎

The mechanism is the focusing of a converging beam: in a flat plane, particles moving radially inward with speed v have
a density ϱ(ρ, t) solving ∂_t ϱ − v ρ⁻¹ ∂_ρ(ρ ϱ) = 0, so ρ ϱ(ρ, t) = (ρ + v t) ϱ0(ρ + v t) and ρ ϱ → v t ϱ0(v t) > 0 as
ρ → 0 once the beam has reached the centre; particles moving along the axis (v = 0) keep their density.

### The theorem {#sec:vlasov-theorem}

Let Ω be a domain of the type [[eq:omega]], Ω = {τ0 ≤ τ ≤ τ_end, r ≥ a, v + (τ − τ_end) ≤ V + 1}, with Σ_τ := Ω ∩ {τ}
and its outer radius b(τ) := V + 1 − τ + (τ_end − τ). Let (g, F, u) be a smooth class solution on Ω of the
Einstein–restricted massless Vlasov system in label form, Ric(g) = T_V. For a compact set S ⊂ (Σ_τ0 ∩ Ω) × S¹ (points
and labels) put S_x := {α : (x, α) ∈ S}, S_α := {x : (x, α) ∈ S}, and let D_α(S) be the set of points of Ω on the
future rays of u_α from S_α that stay in Ω, the *tube* of S_α. We assume:

- (Ω) For g: each Σ_τ is spacelike; {r = a} is spacelike and r decreases along future causal curves near it;
  {v + τ = const} is spacelike and v + τ increases along future causal curves; every ray of u_α through a point of
  D_α(S), S the set of (V1), followed to the past, stays in Ω and meets Σ_τ0. These are (a)–(d) of [[lem:domain]], for
  g.
- (V1) F and u are smooth in (x, α), and there is a compact set S ⊂ (Σ_τ0 ∩ Ω) × S¹ whose interior int S, relative to
  (Σ_τ0 ∩ Ω) × S¹, contains supp q ∩ (Σ_τ0 × S¹), such that: each u_α is an eikonal of g, with ℓ_α future directed, on
  a neighbourhood of D_α(S); for every x, α ↦ β0(x, α) is injective on S_x (the field is labelled by initial
  direction); ∂_α β0 ≥ b_* > 0 on S; and for (x0, α) ∈ S the point y_τ(x0) where the ray of u_α from x0 meets Σ_τ
  depends on x0 with Jacobian determinant ≥ J0 > 0 in the coordinates (r, ϑ) of the orbit slices, for every τ with
  y_τ(x0) in a neighbourhood of Ω̄ (no caustic).
- (V2) dist(D_α(S), axes) ≥ 2δ > 0 for every α.
- (V3) On Σ_τ0 ∩ Ω the spheres {r = const} have positive mean curvature.

The tube D_α of supp q(·, α) lies in D_α(S). (V3) is the first of the two signs of [[lem:constraints-evolution]] (a);
the second, 𝒮 A0 > 0 for the symmetrizer 𝒮 of [[eq:data-symmetrizer]], holds on every slice ([[lem:vlasov-symmetrizer]]).

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
included. The rays start on S_α, off the axes, so the set {(x, α) : x ∈ D_α(S)}, the image of the compact set of
(x0, α, τ) with (x0, α) ∈ S whose ray reaches Σ_τ inside Ω̄ under the continuous map (x0, α, τ) ↦ (y_τ(x0), α), is
compact and disjoint from the closed set axes × S¹, hence at positive distance from it.

**Remark {#rem:vlasov-obstructions}** (What the hypotheses avoid.) Four obstructions are proved in this chapter, and the
theorem is built so that none applies. (O1) At an axis point every invariant null phase is radial, and two of one
orientation have vanishing mixed symbol ([[lem:vlasov-axis-phases]]): the labels are kept off the axes. (O2) Under a C²
metric a continuous orbit density carries no particle to an axis transversally: it would focus there
([[prop:vlasov-axis-focus]]). (O3) Without a hierarchy of frequencies, an antipodal pair and any third phase resonate
exactly ([[lem:vlasov-resonance]]): the frequencies are 1, Λ, …, Λ^(n−1). (O4) A non-radial wave with a component on
the orbit block leaves a term of order λ⁻¹ in the constraints ([[lem:vlasov-constraint-coefficient]] (c)): the waves are
torus-polarised.

### Separation and coherence of the labels {#sec:vlasov-coherence}

**Lemma {#lem:vlasov-separation}** (The flow keeps the labels separated.) Assume (Ω), (V1) and (V2), and let S′ ⊂ int S
be compact. There is c0 > 0, depending on Ω, the field, S and S′ and not on any choice of labels, such that at every
point y ∈ D_α(S′) ∩ D_α′(S′)

    |g⁻¹(du_α, du_α′)(y)| ≥ c0 d(α, α′)².                                                       {#eq:vlasov-separation}

*Proof.* Let ℬ be the bundle of null directions of g3 over the orbit slices of the Σ_τ, a circle bundle. On the orbit
slices off the axes fix a smooth frame (e1, e2) orthonormal for the slice metric (by the Gram–Schmidt process from
(∂_r, ∂_ϑ)), let n be the future unit normal of the orbit slice in (Q, g3), and describe a null direction at y by the
angle β with which a covector k on it, with g3⁻¹k future directed, is written k(n) = −E, k(e1) = E cos β, k(e2) =
E sin β, E > 0. For two such covectors at y,

    g⁻¹(k, k′) = −E E′ + E E′ cos(β − β′) = −2 E E′ sin²((β − β′)/2).                                 {#eq:vlasov-mixed-angle}

Let 𝔰(x0, α) := (x0, β0(x0, α)) on S, with values in ℬ over the orbit slice of Σ_τ0. It is injective, by (V1), and its
differential is triangular with determinant ∂_α β0 ≥ b_* > 0, so on int S it is an injective local diffeomorphism, hence
a diffeomorphism onto the open set 𝔰(int S). For τ ∈ [τ0, τ_end] and y in the orbit slice of Σ_τ ∩ Ω̄, let Ψ_τ(y, β) be
the point and direction in which the null geodesic of g3 through y with direction β, followed to the past, meets Σ_τ0.
It meets Σ_τ0 inside Ω̄: by (Ω) future causal curves leave Ω through its lateral boundaries, so a past causal curve from
Ω̄ does not; and τ is monotone along it. Ψ_τ is smooth, continuous in (τ, y, β), and a diffeomorphism onto its image,
its inverse being the future flow. By [[lem:vlasov-flow]] (b) the rays of u_α are null geodesics of g3, with direction
that of du_α; so if the ray of u_α from x0 ∈ S_α passes through y ∈ Σ_τ, then Ψ_τ(y, β(y; α)) = 𝔰(x0, α), β(y; α) the
angle of du_α at y.

Let K be the compact set of (x0, α, τ) with (x0, α) ∈ S whose ray reaches Σ_τ inside Ω̄, and Φ_τ(x0, α) :=
(y_τ(x0), β(y_τ(x0); α)) = Ψ_τ⁻¹(𝔰(x0, α)) on it. det DΦ_τ = det DΨ_τ⁻¹ · ∂_α β0 is positive, the flow Ψ_τ⁻¹ depending
continuously on τ and being the identity at τ0, so det DΦ_τ ≥ c_Φ > 0 on K. Write DΦ_τ in blocks, with A := ∂y/∂x0,
B := ∂y/∂α, C := ∂β/∂x0, D := ∂β/∂α; A is invertible by (V1), with 0 < det A ≤ C_A on K. At fixed y, inverting
x0 ↦ y_τ(x0) gives x0 = x0(y, α) with ∂_α x0 = −A⁻¹B, and the angle β(y; α) = β(x0(y, α), α) has

    ∂_α β(y; α) = D − C A⁻¹ B = det DΦ_τ / det A ≥ c1 := c_Φ/C_A,

the Schur complement.

Fix τ and y ∈ Σ_τ ∩ Ω̄. On the open set B_y := {β : Ψ_τ(y, β) ∈ 𝔰(int S)} put Λ_y(β) := the label of 𝔰⁻¹(Ψ_τ(y, β)),
a smooth function; if y ∈ D_α(S′), then β(y; α) ∈ B_y and Λ_y(β(y; α)) = α. At β ∈ B_y, with (x0, α″) :=
𝔰⁻¹(Ψ_τ(y, β)) ∈ int S, whose ray reaches y, so that (x0, α″, τ) ∈ K, Λ_y is the inverse of α ↦ β(y; α) near α″, and
0 < Λ_y′(β) = 1/∂_α β(y; α″) ≤ 1/c1. Since 𝔰(S′) is a compact subset of the open set 𝔰(int S) and Ψ is uniformly
continuous on the compact set of the (τ, y, β), there is ρ0 > 0 such that for every τ, y ∈ Σ_τ ∩ Ω̄ and β with Ψ_τ(y, β)
∈ 𝔰(S′), the arc of the β″ with |β″ − β| ≤ ρ0 lies in B_y.

Let y ∈ D_α(S′) ∩ D_α′(S′), β := β(y; α), β′ := β(y; α′), and δβ ∈ [0, π] their distance on the circle. Let E_* > 0
be the minimum of E = −du_α(n) over the compact set of the (y, α) with y in the closure of D_α(S); it is positive since
du_α ≠ 0 is null with g⁻¹du_α future directed. By [[eq:vlasov-mixed-angle]] and sin(t/2) ≥ t/π on [0, π],
|g⁻¹(du_α, du_α′)(y)| ≥ 2 E_*² sin²(δβ/2) ≥ 2 E_*² δβ²/π². If δβ ≥ ρ0, this is at least 2 E_*² ρ0²/π² ≥
(2 E_*² ρ0²/π⁴) d(α, α′)², as d(α, α′) ≤ π. If δβ < ρ0, the arc of length δβ from β to β′ lies in B_y, Λ_y maps its ends
to α and α′, and Λ_y′ ≤ 1/c1 on it, so d(α, α′) ≤ δβ/c1 and the bound is at least (2 E_*² c1²/π²) d(α, α′)². So
[[eq:vlasov-separation]] holds with c0 := (2 E_*²/π²) min(c1², ρ0²/π²). The injectivity of β0(x, ·) is used in the
definition of Λ_y, which needs 𝔰 injective. ∎

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
K := k_a + k_b − k_c is null. So with equal frequencies the mixed harmonic e^(i(θ_a + θ_b − θ_c)) is exactly resonant,
whatever the pairwise separations.

*Proof.* In an orthonormal frame, k_a = E(−1, e), k_b = E(−1, −e), k_c = E(−1, f), with e, f unit vectors. Then K =
E(−1, −f), and g⁻¹(K, K) = E²(−1 + 1) = 0. ∎

**Lemma {#lem:vlasov-hierarchy}** (Coherence under a hierarchy of frequencies.) Let k_1, …, k_n be covectors at a point
of a 2+1-dimensional Lorentzian space with g⁻¹(k_A, k_A) = 0, |g⁻¹(k_A, k_B)| ≥ c > 0 for A ≠ B, and |k_A| ≤ Ē in an
orthonormal frame. Let Λ > 1 and ν_A := Λ^(A−1). For every j ∈ ℤⁿ with at least two nonzero entries and |j|₁ ≤ m, let B1
and B2, B1 > B2, be its two largest indices with nonzero entries. Then

    |g⁻¹(K_j, K_j)| ≥ 2 ν_B1 ν_B2 (c − m Ē²/Λ − m² Ē²/(2Λ)).                                    {#eq:vlasov-hierarchy}

In particular every such combination is non-null, with this margin, once Λ > (m + m²/2) Ē²/c.

*Proof.* In the orthonormal frame |g⁻¹(k, k′)| ≤ |k| |k′|. Put K := K_j = j_B1 ν_B1 k_B1 + V, V := Σ_(A ≠ B1) j_A ν_A
k_A. Since k_B1 is null, g⁻¹(K, K) = 2 j_B1 ν_B1 g⁻¹(k_B1, V) + g⁻¹(V, V). Here g⁻¹(k_B1, V) = j_B2 ν_B2 g⁻¹(k_B1,
k_B2) + Σ_(A < B2) j_A ν_A g⁻¹(k_B1, k_A), and ν_A ≤ ν_B2/Λ for A < B2, so |g⁻¹(k_B1, V)| ≥ ν_B2 (c − m Ē²/Λ), using
|j_B2| ≥ 1 and Σ|j_A| ≤ m. Further |V| ≤ Σ_(A ≤ B2) |j_A| ν_A Ē ≤ m ν_B2 Ē, so |g⁻¹(V, V)| ≤ m² Ē² ν_B2² ≤ m² Ē² ν_B1
ν_B2/Λ. With |j_B1| ≥ 1, |g⁻¹(K, K)| ≥ 2 ν_B1 ν_B2 (c − m Ē²/Λ) − m² Ē² ν_B1 ν_B2/Λ, which is [[eq:vlasov-hierarchy]]. ∎

With c = c0 (2π/n)², Λ is of order n², as in the choice a_A = c n² a_(A−1) of [HL25, Lemma 4.16, p. 18]. The phases ν_A
u_A are eikonals, so the two-scale scheme is unchanged; the wave of family A carries the amplitude λ F_A/ν_A, so that its
derivatives are of the size of F_A.

**Remark {#rem:vlasov-coherence-values}** (Numerical observation.) On the orbit space of Tangherlini with μ = 1 and
labels in [−0.6, 0.6], the Schur formula of [[lem:vlasov-separation]] agreed with shooting to 1.1 × 10⁻⁹, ∂_α β was at
least 0.798, and the least mixed symbol of adjacent labels divided by (Δα)² was 0.2923, 0.2926, 0.2927, 0.2927 at n = 8,
16, 32, 64. For the four labels 2πA/4 on flat 2+1 with the hierarchy, every Q_j with |j|₁ ≤ 5 satisfied exactly
|Q_j|/(ν_B1 ν_B2) ≥ 359/216; with two radial covectors added and labels at angle at least η from them (label–radial
symbols at least 1/5), every combination with |j|₁ ≤ 4 had |Q_j|/(ν_B1 ν_B2) ≥ 35612/609961, above the bound 4/50765 of
[[eq:vlasov-hierarchy]]. No proof uses these values.

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
meet no coefficient of order λ⁻¹.

(c) For the other polarisation, W = ζ cos θ (q̂ ⊗ q̂ − ½ (e^(2ψ10) dφ1² + e^(2ψ20) dφ2²)) with q̂ the γ0-unit covector
of the orbit slice orthogonal to p and ζ ≠ 0, and h = c dr ⊗ dr, dρ⁽⁻¹⁾ = −c ζ |p|² cos θ ⟨dr, q̂⟩², which is not zero
where c ≠ 0 and the phase is not radial (p not parallel to dr).

*Proof.* (a) Terms of order λ⁻¹ arise only where two derivatives fall on λ W, or one on κ1. In
R(γ) = γ^(ij)(∂_k Γ^k_ij − ∂_j Γ^k_ik) + ΓΓ the second derivatives of γ enter as γ^(ij) γ^(kl)(∂_i∂_k γ_jl − ∂_i∂_j
γ_kl), and ∂_i∂_k(λ W) = λ⁻¹ p_i p_k W″ + O(1), while ΓΓ is of order one. So the part of order λ⁻¹ of R(γ) is
W″(p^♯, p^♯) − |p|² tr W″, with p^♯ := γ⁻¹p and the inverse of the full γ. Varying γ ↦ γ + εh, so that γ^(ij) ↦ γ^(ij)
− ε h^(ij), gives the first line of [[eq:vlasov-constraint-coefficient]]; the remaining terms of DR[h], which carry
derivatives of h or first derivatives of γ, are of order one. In J, −div κ ⊃ −γ^(jl) ∂_l κ_(ji) and d tr κ ⊃
∂_i(γ^(jl) κ_(jl)), whose parts of order λ⁻¹ are −γ^(jl) p_l κ1′_(ji) and p_i γ^(jl) κ1′_(jl); varying γ gives the
second line; the Christoffel terms are of order one. −|κ|² + (tr κ)² has no term of order λ⁻¹, and no term of order
λ⁻¹ depends on k. With several phases the fast derivatives of λ W_A(x, θ_A) give λ⁻¹ p_A p_A W_A″ and the cross terms
vanish, each W_A depending on one phase; ∂²(λ² M(x, θ_A ± θ_B)) is of order one, and ∂(λ(…)) is of order one.

(b) The parts of order λ⁻¹ of R(γ + h) and J(γ + h, κ + k) are, by the proof of (a), W″(p^♯, p^♯) − |p|² tr W″ and
2(−γ_h^(jl) p_l κ1′_(ji) + p_i γ_h^(jl) κ1′_(jl)) with the inverse γ_h⁻¹ of γ + h. Since γ0 and h have no mixed
orbit–torus components, γ_h⁻¹ is block-diagonal and p^♯ is an orbit vector, while W″ and κ1′ have torus components only.
So W″(p^♯, ·) = 0, γ_h^(jl) p_l κ1′_(ji) = 0, and the torus traces vanish: tr W″ = −2ξ cos θ (e^(−2ψ10) e^(2ψ10) −
e^(−2ψ20) e^(2ψ20)) + O(λ) = O(λ) and likewise tr κ1′ = O(λ). The corrections of [[lem:constraints-evolution]] change γ
by a multiple of dr ⊗ dr only.

(c) Here W″ = −W, W″p = 0 because q̂ ⊥ p and the torus block annihilates p, and tr W″ = −ζ cos θ (|q̂|² − ½ − ½) = 0.
So dρ⁽⁻¹⁾ = |p|² ⟨h, W″⟩ = −c ζ |p|² cos θ ⟨dr, q̂⟩². In the two-dimensional orbit slice ⟨dr, q̂⟩ = 0 exactly when dr is
parallel to p. ∎

**Lemma {#lem:vlasov-leaf-curvature}** (The principal coefficients do not oscillate.) At data of the form of
[[lem:vlasov-constraint-coefficient]] with torus-polarised waves W_A and with second and mixed harmonics of order λ² in
γ, the principal coefficients of the constraint map in the unknowns of [[lem:constraints-evolution]] have no oscillating
part of order λ⁰: the coefficient (γ^(rr))^(3/2) H of the radial derivative of the metric unknown in ρ ([[eq:data-rho]]),
those of its angular second derivatives, and those of the first derivatives of the momentum unknowns in J. For a wave
with a trace on the spheres, ξ2 = ξ1, the mean curvature H oscillates at order λ⁰.

*Proof.* The coefficients of the angular second derivatives of the metric unknown in ρ and of the first derivatives of
the momentum unknowns in J involve γ, its inverse and Π, undifferentiated ([[lem:constraints-evolution]] (a)), and γ =
γ0 + O(λ). In (γ^(rr))^(3/2) H, γ^(rr) is undifferentiated, and H = H̃/ν with H̃ = ½ tr_Π(∂_r Π − 𝓛_σ Π). The torus
directions are tangent to the spheres, so the oscillating part of order λ⁰ of ∂_r Π is Σ_A ν_A ∂_r u_A ∂_(θ_A) W_A, and
its Π-trace is Σ_A ν_A ∂_r u_A ∂_(θ_A) tr W_A = 0, the torus-polarised W_A being traceless. The harmonics of order λ²
contribute O(λ) to first derivatives, and so does the shift of the foliation, whose oscillating part is of order λ². If
ξ2 = ξ1, tr W_A = 4 ξ1 cos θ_A + O(λ) and H̃ acquires −2 ξ1 ∂_r u_A sin θ_A at order λ⁰. ∎

Next the commutator of the wave operator with a generator, which the uniform estimate needs for each family. For a
radial family on a round background it is [[pending:two-dust-commutator]], whose proof uses that the generator is
shear-free. A non-radial family on a non-round background is not shear-free in five dimensions, but its shear lives
in the torus directions, where the Hessian of an invariant function is of first order, and in the orbit space it has
no shear.

**Lemma {#lem:vlasov-no-shear}** (No shear in the orbit space.) Let u be a function on a 2+1-dimensional Lorentzian
manifold (Q, g3) with |du|² = 0 to first order at a point, du ≠ 0 there, and ℓ := g3⁻¹du. Then for every symmetric
bilinear form S with S(ℓ, ·) = 0 at that point,

    ⟨Hess u, S⟩ = (□3 u) tr S.                                                                  {#eq:vlasov-no-shear}

So F(S) := ⟨Hess u, S⟩ − (□3 u) tr S depends only on S(ℓ, ·). In a null frame (ℓ, ℓ̄, e), g3(ℓ, ℓ̄) = −1, e a unit
vector orthogonal to both, with H := Hess u (not the mean curvature),

    F(S) = H(ℓ̄, ℓ̄) S(ℓ, ℓ) − 2 H(ℓ̄, e) S(ℓ, e) + 2 H(e, e) S(ℓ, ℓ̄).                           {#eq:vlasov-shear-form}

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

    [□5, L] φ = a □5 φ + M(L φ) + N φ,      a := 2 □3 u,                                          {#eq:vlasov-commutator}

with M a first-order operator and N a first-order operator, with coefficients smooth where u is; the same holds for
□̃ := g5^(ab) ∂_a∂_b in the chart X, with another N. On a round background with u = v, a = 2 L(R)/R, the coefficient of
[[pending:two-dust-commutator]].

*Proof.* For any metric, [□, ℓ^μ ∇_μ] φ = 2 ⟨∇ℓ, Hess φ⟩ + (□ℓ^μ + Ric^μ_ν ℓ^ν) ∂_μ φ, and ∇ℓ = Hess_(g5) u. For
invariant functions the Christoffel symbols of [[lem:warped-ricci]] give Hess_(g5) f(∂_a, ∂_b) = Hess_(g3) f(∂_a, ∂_b),
Hess_(g5) f(∂_a, ∂_(φi)) = 0 and Hess_(g5) f(∂_(φi), ∂_(φi)) = e^(2ψi) ⟨dψ_i, df⟩, of first order in f. So
⟨Hess_(g5) u, Hess_(g5) φ⟩ = ⟨Hess_(g3) u, Hess_(g3) φ⟩ + Σ_i ⟨dψ_i, du⟩ ⟨dψ_i, dφ⟩. Apply [[eq:vlasov-shear-form]] with
S := Hess_(g3) φ: S(ℓ, X) = X(Lφ) − Hess_(g3) u(X, ∇φ), so ⟨Hess_(g3) u, Hess_(g3) φ⟩ = (□3 u) □3 φ + M′(Lφ) + (first
order in φ), with M′ := H(ℓ̄, ℓ̄) ℓ − 2 H(ℓ̄, e) e + 2 H(e, e) ℓ̄ for any smooth null frame. Finally □3 φ = □5 φ −
⟨dψ, dφ⟩ by [[eq:vlasov-box]]. This gives [[eq:vlasov-commutator]] with M := 2M′. For □̃, □̃φ = □5 φ + H0·∂φ with
H0^ρ := g5^(ab) Γ^ρ_ab smooth, and [L, H0·∂] is of first order. On a round background g3 = −2 e^(2σ) du dv + R² dϑ² in
double-null coordinates, √|g3| = e^(2σ) R and g3^(uv) = −e^(−2σ), so □3 v = −e^(−2σ) R_u/R = L(R)/R. ∎

So if ℓ_A·dφ = f along the generator of family A, then Ψ := □̃φ satisfies L_A Ψ + a_A Ψ = □̃f − M_A(f) − N_A φ, the
form [[eq:ue-psi]] that the uniform estimate uses, with a_A = 2 □3 u_A.

### The n-dust approximants are uniform in n {#sec:vlasov-uniform}

**Lemma {#lem:vlasov-trapezoid}** (The label quadrature.) Let F be smooth on K × S¹, K compact, and

    E_n(x) := ∫_(S¹) F(x, α) dα − (2π/n) Σ_(A=1)^n F(x, 2πA/n).

Then for every j and every k ≥ 2, sup_K |∂_x^j E_n| ≤ 2 ζ(k) n^(−k) sup_(x∈K) ∫_(S¹) |∂_x^j ∂_α^k F(x, α)| dα, ζ the
Riemann zeta function.

*Proof.* The x-derivatives commute with both terms, so take j = 0. Expand F(x, α) = Σ_(m∈ℤ) F̂_m(x) e^(imα), absolutely
convergent. Since (2π/n) Σ_A e^(2πimA/n) is 2π if n divides m and 0 otherwise, E_n = −2π Σ_(l≠0) F̂_(ln). Integrating
by parts k times, |F̂_m(x)| ≤ (2π)⁻¹ |m|^(−k) ∫ |∂_α^k F(x, α)| dα, so |E_n| ≤ Σ_(l≠0) (|l| n)^(−k) ∫ |∂_α^k F| dα. ∎

For an integrand with a kink in α the error is only of order n⁻²: the smoothness of the field in its label is what is
used.

Let (g, F, u) satisfy (Ω), (V1), (V2), (V2′) and (V3). For n ≥ 1 put α_A := 2πA/n. The *n-dust approximant* of the
field is the class Einstein–n-null-dust solution g^(n), with the radial dusts of g, whose data on Σ_τ0 are: the
densities q_A := (2π/n) q(·, α_A); eikonals u_A with the data of u_(α_A) on Σ_τ0 (on the same branch of the eikonal
equation); the radial dusts' data of g; and the metric data of g corrected, by the radial solve of [[sec:data-evolution]]
under (V3), to satisfy the constraints with the stress T^(n) + T_rad, T^(n) := Σ_A q_A du_A ⊗ du_A. The class
Einstein–n-null-dust system and its augmented form, in the unknowns (w, du_A, Θ_A, q_A) with the expansions Θ_A :=
□5 u_A transported by the Raychaudhuri equation, are those of [[pending:class-augmented-system]], and their Cauchy
stability on Ω without smallness is [[thm:class-stability]].

**Proposition {#prop:vlasov-uniform-n}** (The n-dust approximants are uniform in n.) Fix m ≥ 6. There are n0 and, for
every k, a constant C_k independent of n, such that for n ≥ n0 the n-dust approximant g^(n) exists on Ω and, on every
Σ_τ,

    ‖g^(n) − g‖_(H^(m+1)) + ((2π/n) Σ_A ‖(du_A, Θ_A, q_A/(2π/n)) − (du_(α_A), Θ(·, α_A), q(·, α_A))‖²_(H^m))^(1/2)
        ≤ C_k n^(−k),                                                                          {#eq:vlasov-uniform-n}

with Θ(·, α) := □5 u_α, the family norms taken on the tubes. In particular |g^(n) − g|_(C¹(Ω)) ≤ C_k n^(−k).

*Proof.* Let E_n := T_V − Σ_A (2π/n) q(·, α_A) du_(α_A) ⊗ du_(α_A), evaluated with g. It is the error of
[[lem:vlasov-trapezoid]] for the integrand q(x, α) du_α ⊗ du_α, smooth on Ω × S¹ by (V1), so |∂^j E_n| ≤ C_(j,k) n^(−k)
for all j, k.

*Data.* The data of g on Σ_τ0 satisfy the constraints with the stress T_V + T_rad; those of g^(n) are corrected to the
stress T^(n) + T_rad by the radial solve, whose hypotheses on Σ_τ0 ∩ Ω are (V3), and whose linear evolution
([[lem:linear-evolution]]) is stable under a change of the matter term. That change is E_n on Σ_τ0, up to the
difference of the eikonals, which have the same data. So the corrected data differ from those of g by at most C_k n^(−k)
in H^(m+1) × H^m, and the families' data from the sampled continuum's by the same amount, with the weight 2π/n.

*Evolution.* The sampled continuum, the metric g with (du_(α_A), Θ(·, α_A), (2π/n) q(·, α_A)), solves the eikonal and
density transports of the n-dust system exactly, since each involves only g and its own family. It solves the Einstein
equation and the Raychaudhuri transports up to the residual E_n, which enters the first as a matter term and the second
through E_n(ℓ_A, ℓ_A), the Ricci term of the Raychaudhuri equation being Ric(ℓ_A, ℓ_A). Take the energy of the proof of
[[thm:class-stability]] for the difference, with the family norms weighted by 2π/n, an ℓ² sum over A. It closes with
constants independent of n: the matter term of the metric equation for the difference is Σ_A (2π/n)(ς_A p_A ⊗ p_A + q̂_A
(π_A ⊗ p_A + p_A ⊗ π_A)), with (π_A, ς_A) the differences of (du_A, q_A/(2π/n)) and q̂_A := q(·, α_A), bounded by
Cauchy–Schwarz by C times the weighted family norm, as Σ_A 2π/n = 2π; each family's transport depends on the others only
through the metric and through Ric(ℓ_A, ℓ_A) = Σ_B (2π/n) q̂_B g⁻¹(du_A, du_B)², a quadrature bounded in the same way;
every other term is that of the n-dust energy, family by family, with constants uniform in A because the sampled
families are uniformly smooth in α. Gronwall's lemma and the bootstrap give [[eq:vlasov-uniform-n]] for n ≥ n0, n0
chosen so that C_k n0^(−k) lies below the bootstrap's threshold; the tubes of g^(n) stay within C_k n^(−k) of those of
g, so (V2) keeps the families off the axes. The last statement is Sobolev's inequality for m ≥ 6. ∎

**Remark {#rem:vlasov-uniform-model}** (Numerical observation.) In a mean-field wave–transport model of the quadrature
step, w_tt − w_xx = Σ_A (2π/n) q_A with q_A transported at speed tanh(2w + cos α_A), with no derivative-loss coupling,
the stability constant of the n-label system was measured as 0.603, 0.667 and 0.667 at n = 4, 8, 16, while a coupling
growing with n gave 0.603, 0.873, 1.654; the ratio of the n-label solution's error to the quadrature residual stayed
below 0.02 for n = 4, 8, 16. No proof uses these values.

### The high-frequency step with n families {#sec:vlasov-n}

In this section g0 is a smooth class Einstein–n-null-dust solution on Ω, n families u_A with densities F_A² (A = 1, …,
n), possibly with two radial dusts, such that:

- (i) (Ω) holds for g0;
- (ii′) on the overlap of the supports of any two families, the radial ones included, |g0⁻¹(du_A, du_B)| ≥ c > 0, and
  the frequencies are ν_A := Λ^(A−1) over all the phases, with Λ > (m* + m*²/2) Ē²/c, where m* := N + 2, N is the number
  of stages, and Ē bounds |du_A| in orthonormal frames on the supports;
- (iii) the waves of the non-radial families are torus-polarised ([[def:vlasov-torus-wave]]), those of the radial dusts
  are those of [[thm:two-dusts]].

By [[lem:vlasov-hierarchy]] with m = m*, every symbol [[eq:vlasov-symbol]] with at least two nonzero entries and |j|₁ ≤
m* satisfies |Q_j| ≥ 2 ν_B1 ν_B2 c* on the overlaps, c* := c − m* Ē²/Λ − m*² Ē²/(2Λ) > 0. These conditions are those of
the two-dust theorem with one transport and one phase per family, the mixed symbols bounded below on every harmonic
used; we list what changes from two families to n.

**Theorem {#thm:vlasov-n-approximant}** (The approximant with n phases.) Under (i)–(iii), for every N ≥ 1 and every
smooth choice of stage data there are profiles g_1, …, g_N in (X, θ_1, …, θ_n), independent of λ, such that g_app = g0 +
λ [g_1] + Σ_(l=2)^N λ^l [g_l], with the phases θ_A = ν_A u_A/λ, is an n-phase approximant with N stages of order K =
N − 1 at every regularity k, in the sense of [[pending:two-dust-approximant-definition]] with one phase per family.

*Proof.* The stage system is that of [[pending:two-dust-stages]] with n phases: (a) the mean, a linear wave equation; (b)
n phase corrections, each transported along its own generator; (c) the pure harmonics of each family, transported along
its own generator; (d) every mixed harmonic e^(i j·θ) with at least two nonzero entries and |j|₁ ≤ m + 2 at stage m,
divided by Q_j. On the overlaps |Q_j| ≥ 2 ν_B1 ν_B2 c*, by (ii′). The phase corrections and the mean change Q_j by O(λ),
and this change is moved to the next order, as in [[pending:two-dust-nonresonance]], since |j|₁ is bounded at each stage;
each division costs one derivative, and there are finitely many stages. Every generator through a point of Ω reaches Σ_τ0
inside Ω, by (Ω), so the Picard argument of [[thm:approximant]] closes the stage system. Stage 0 is
[[lem:vlasov-torus-ricci]] for each non-radial family: no term of order λ⁻¹, the torus polarisation kept by
[[eq:vlasov-xi-transport]]; the wave of family A is the torus-polarised wave of the eikonal ν_A u_A with amplitude
F_A/ν_A, whose mean F_A² du_A ⊗ du_A balances the background's stress. The assembly is that of
[[pending:two-dust-approximant]]. ∎

Let s_A(h) := h(ℓ_A, ℓ_A), and let Y_A, G1^A, G2^A, 𝒫 and the energy be those of [[pending:two-dust-uniform]], with one
index per family; 𝒫 is the mollifier of [[lem:mollifier]].

**Theorem {#thm:vlasov-n-uniform}** (Uniform existence with n phases.) Fix k = 6 and K ≥ 6. Under (i)–(iii) let g_app be
an n-phase approximant with N stages of order K at regularity k, with constant C_R in (E3), and let g be a Cauchy datum
on Σ_τ0 for Ric^H(g) = 0 with w := g − g_app satisfying (E4) of [[thm:uniform-existence]], Data(w) ≤ C_D λ^K. There are
λ0(n) > 0 and M(n), depending on Ω, k, K, C_R, C_D, n and the bounds on the profiles but not on λ, such that for 0 <
λ ≤ λ0(n) the solution g of Ric^H(g) = 0 with these data exists on Ω, is unique there among C² solutions with |g − g0|
≤ ε1, is smooth if the data are, and

    w = h + Σ_A φ_A Y_A,      𝒩_n(τ) ≤ M(n) λ^K   on [τ0, τ_end],                                {#eq:vlasov-n-remainder}

𝒩_n the energy of [[pending:two-dust-uniform]] summed over the n families. In particular |w| ≤ M(n) λ^(K−3) and |∂w| ≤
M(n) λ^(K−4) on Ω.

*Proof.* The proof of [[pending:two-dust-uniform]], with these changes.

(1) *The decomposition.* The phase shifts solve n transports ℓ_A·dφ_A = ½ 𝒫 s_A(h), φ_A = 0 on Σ_τ0, coupled through the
bounded maps φ ↦ 𝒫([Y_B(ℓ_A, ℓ_A)] φ) of [[eq:mollifier-m1]]; on slabs of a length independent of the data the coupled
map is a contraction, and Picard's theorem gives the decomposition.

(2) *The term of order λ⁻¹.* The part of order λ⁻¹ of the linearisation is ½ λ⁻¹ Σ_A s_A(h) G2^A, linear in the waves,
as in (F1) of [[pending:two-dust-facts]].

(3) *The ℓ_A ⊗ ℓ_A component.* Contracting the equation for h with ℓ_A ⊗ ℓ_A kills family A's term of order λ⁻¹ and its
□̃φ_A term, as for one family. Every B ≠ A remains exactly as the other family remains in [[pending:two-dust-ell-ell]]:
½ λ⁻¹((1 − 𝒫) s_B(h)) G2^B(ℓ_A, ℓ_A) = O(∂ s_B(h)) and λ⁻¹((ℓ_app^B − ℓ_B)·dφ_B) G2^B(ℓ_A, ℓ_A) = O(|dφ_B|), with Ψ_B :=
□̃φ_B carrying a bounded coefficient. For a torus-polarised wave of family B, the wave part of G2^B vanishes on vectors
of the orbit space, so G2^B(ℓ_A, ℓ_A) is its gauge part χ_B (ℓ_A·du_B)², as for two families.

(4) *The transport of Ψ_A.* For a non-radial family, Ψ_A := □̃φ_A satisfies L_A Ψ_A + a_A Ψ_A = □̃f_A − M_A(f_A) − N_A
φ_A by [[cor:vlasov-commutator]], with f_A := ½ 𝒫 s_A(h); for a radial family this is [[pending:two-dust-commutator]].

(5) *The transport estimates.* Each family's transport field Z_A, with ℓ_A = ℓ_A(τ) Z_A and ℓ_A(τ) ≠ 0 since a null
vector is never tangent to a spacelike slice, satisfies the identity of [[pending:two-dust-transport]] with c x̂ replaced
by the spatial part of Z_A. Its boundary terms are nonpositive by (Ω): at {r = a}, r decreases along future causal
curves, and at the outer boundary v + τ increases, which is b′(τ) − dr(Z_A) < 0 there. So the estimate holds for every
family, whatever its direction.

(6) *Closing.* Every term of the n-family linearisation is a term of one of the types of the two-family estimate, with
its family labels replaced; and the bound of each type in the bootstrap (its power of λ, its number of derivatives, the
part of the energy that controls it) depends on the type alone. From stage 1 on, terms carry three or more families;
they are products of profiles of the same orders, and a product of oscillating profiles at the phases θ_A has m-th
derivatives of order λ^(−m), by the Leibniz rule, whatever the phases. The number of terms is finite for each n and
enters only the constants. So Steps 4–7 of [[thm:uniform-existence]], in the form of [[pending:two-dust-uniform]], give
𝒩_n(τ) ≤ C3(n)((C_D + 1 + C_R) λ^K + C(n) M² λ^(K+1)), and the bootstrap closes with M(n) := C3(n)(C_D + 1 + C_R) + 1
and λ0(n) so small that C3(n) C(n) M(n)² λ0(n) ≤ 1. Existence, uniqueness and smoothness follow as in
[[thm:uniform-existence]]. ∎

**Remark {#rem:vlasov-boundary-instance}** (The boundary signs on Tangherlini.) For g0 = η + (μ/r²) dv ⊗ dv, μ > 0 and
any future null vector l with l(τ) = 1, radial or not, dr(l) ∈ [−1, (r² − μ)/(r² + μ)]. Indeed, writing l = ∂_τ + w with
w spatial, w_r := x̂·w, the null condition is −1 + |w|² + (μ/r²)(1 + w_r)² = 0, so with |w|² ≥ w_r² and m := μ/r²,
(1 + m) w_r² + 2m w_r + m − 1 ≤ 0, whose roots are −1 and (1 − m)/(1 + m). So at the outer boundary, b′ = −2,
b′ − dr(l) ≤ −1, and at r = a < √μ, dr(l) ≤ (a² − μ)/(a² + μ) < 0: both boundary terms of step (5) have the right sign
for every family on Tangherlini. For a general g the signs come from (Ω).

**Theorem {#thm:vlasov-n-data}** (Data with overlapping families.) Under (i)–(iii), with (V3) on Σ_τ0, let K ≥ 6 and N :=
K + 3. For λ ≤ λ0(n) there is a vacuum Cauchy datum on Σ_τ0 ∩ Ω, with the gauge condition imposed through ∂_τ g,
within O(λ^K) of the data of the approximant of [[thm:vlasov-n-approximant]], in the sense of (E4); the n families may
overlap anywhere on Σ_τ0.

*Proof.* The approximant's slice data carry every family's wave and the second and mixed harmonics at order λ²; the
mixed amplitudes are those of the spacetime scheme (stage (d)) evaluated on Σ_τ0, algebraic in the pure ones. They
satisfy the constraints to O(λ^(N−1)), g_app solving Einstein's equations to that order. The correction is the radial
solve of [[lem:linear-evolution]] and [[prop:exact-correction]], whose hypotheses are: (a) the two signs of
[[lem:constraints-evolution]] (a) on the slice, which are (V3); (b) no coefficient of order λ⁻¹ in the constraint map
at the approximant's data, as a function of the unknowns, which is [[lem:vlasov-constraint-coefficient]] (a)–(b): the
coefficient is linear in the waves and the sum of the single-family ones, each zero for a torus-polarised wave (for the
radial dusts' waves, by [[thm:two-dusts]]), while the second and mixed harmonics enter at order λ⁰; (c) the principal
coefficients at order λ⁰ are the background's, which is [[lem:vlasov-leaf-curvature]]; (d) the constraint map depends
on (γ, κ) only ([[eq:data-constraint-map]]). The gauge hierarchy is that of [[lem:gauge-hierarchy]] with n phases: the
oscillating part at each order is a transport along each generator for the pure harmonics, and algebraic, with the
divisor Q_j ≠ 0, for the mixed ones, which therefore take no data. The stage data are those of [[lem:stage-data]] for
each family's covector, the polarisation map being onto for each; the mixed harmonics take no data and need not vanish
on Σ_τ0, which no step uses.

No division is made on the slice. The phases are the background's eikonals, with corrections φ_A = 0 on Σ_τ0, and the
initial value of Ψ_A is fixed by its transport, which divides only by ℓ_A(τ) ≠ 0. Nothing prescribes the eikonal's data
against a parametrix. The only divisors are the spacetime symbols Q_j; for an antipodal pair of labels of equal energy
E, 2 ν_A ν_B g0⁻¹(k_A, k_B) = −4 ν_A ν_B E² ≠ 0. ∎

**Remark {#rem:vlasov-n-odd}** (Odd n.) [HL25] prescribe the data of their eikonals on the initial slice through the
symbol of Δ − (cos α_A ∂_1 + sin α_A ∂_2)², and bound below the divisors (ν_B sin(α_A − α_B))², which vanish for an
antipodal pair; this is the one place where they need n odd [HL25, (7.24)–(7.32), pp. 27–28, and footnote 10]. In
[[thm:vlasov-n-data]] that divisor does not arise, so n odd is not needed there; the diagonal of [[sec:vlasov-proof]]
takes n odd at no cost.

**Remark {#rem:vlasov-radial-pair}** (Labels and radial dusts.) Hypothesis (V2′) cannot be dropped: where a label's
momentum is parallel to a radial null direction on the support of the radial dust of that direction, g0⁻¹(du_A, du_rad)
= 0 there, and every harmonic j supported on that pair has Q_j = j_A² ν_A² · 0 + 2 j_A j_rad ν_A ν_rad g0⁻¹(du_A,
du_rad) + j_rad² ν_rad² · 0 = 0, at every Λ. With an angle at least η, the label–radial symbols are |g0⁻¹(du_A,
du_rad)| = E E′ (1 − cos β) ≥ E E′ (1 − cos η) =: c(η) > 0 by the formula in the proof of [[lem:vlasov-separation]], and
the hierarchy runs over all n + 2 phases with c = min(c0 (2π/n)², c(η)).

### Proof of the theorem {#sec:vlasov-proof}

*Proof of [[thm:vlasov]].* By [[prop:vlasov-uniform-n]], for n ≥ n0 the n-dust approximant g^(n) exists on Ω, with labels
α_A = 2πA/n and |g^(n) − g|_(C¹(Ω)) ≤ C_k n^(−k) for every k; its families' covectors are within C_k n^(−k) of the
continuum's du_(α_A) on the tubes. Fix an odd n ≥ n0, enlarged if necessary, and check (i)–(iii) for g^(n).

(i) (Ω) is a finite set of strict inequalities on the compact Ω̄, continuous in g in C¹, so it holds for g^(n) for n
large, the generators of its families being C⁰-close to those of g.

(ii′) By [[lem:vlasov-separation]], |g⁻¹(du_(α_A), du_(α_B))| ≥ c0 (2π/n)² on the overlaps, so for g^(n),
|g^(n)⁻¹(du_A, du_B)| ≥ c0 (2π/n)² − C_k n^(−k) ≥ ½ c0 (2π/n)² for n large (k = 3). By (V2′) and
[[rem:vlasov-radial-pair]], the label–radial symbols are at least ½ c(η), and the radial pair, one ingoing and one
outgoing, is separated with some c_rad > 0, its two null directions being distinct at every point of its compact
overlap. So c := min(½ c0 (2π/n)², ½ c(η), c_rad) > 0, and Λ = Λ(n) is chosen as in (ii′).

(iii) The wave of each label is the torus-polarised wave of the eikonal ν_A u_A with amplitude F_A/ν_A, F_A² = q_A the
density of g^(n) (smooth, F_A being transported by [[eq:vlasov-amplitude]] from the smooth data (2π/n)^(1/2) F(·, α_A)),
and the radial dusts carry the waves of [[thm:two-dusts]].

So [[thm:vlasov-n-approximant]], [[thm:vlasov-n-uniform]] and [[thm:vlasov-n-data]] give vacuum metrics g^(n)_λ on Ω,
λ ≤ λ0(n), invariant under T² and both reflections (by uniqueness, the data being invariant), with

    |g^(n)_λ − g^(n)| ≤ C(n) λ,      ∂g^(n)_λ − ∂g^(n) = Σ_A ν_A du_A ⊗ [∂_(θ_A) W_A] + O(C(n) λ),

W_A the wave of family A at its phase θ_A = ν_A u_A/λ, of zero mean in θ_A, with |ν_A ∂_(θ_A) W_A| ≤ C(F_A + F_A²),
C independent of n and A (the wave is linear in its amplitude and its gauge part quadratic), and the radial dusts'
terms of the same form.

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

**Corollary {#cor:vlasov-two-dust}** (The two-dust background with a restricted Vlasov field.) Let g0 be the two-dust
background of [[thm:two-dusts]] on its domain, with lateral boundaries adapted where they meet an axis as in
[[pending:class-adapted-domain]]. Let (F, u) be a restricted field in label form on Σ_τ0 whose labels satisfy (V1), (V2)
and the angle clause of (V2′) for g0, with margins, on a compact set S ⊂ (Σ_τ0 ∩ Ω) × S¹ with supp q ⊂ int S. Then for
amplitudes ε small the class Einstein–restricted massless Vlasov solution with the two radial dusts of g0 and the field
of amplitude ε F, with data corrected by the radial solve, exists on the domain and is a weak limit of class vacuum
metrics in the sense of [[thm:vlasov]].

*Proof.* The solution exists on the domain for ε small by [[prop:vlasov-cauchy]] around g0, the radial pair being
governed by [[thm:class-stability]], and it is C²-close to g0 with C¹-close eikonals. By [[lem:vlasov-open]] it satisfies
(V1), (V2) and (V2′); (Ω) and (V3) hold for g0 with margins, by the domain and slice lemmas of the proof of
[[thm:two-dusts]], and they are open. [[thm:vlasov]] applies. ∎

### Openness, stability and an explicit family {#sec:vlasov-open}

**Lemma {#lem:vlasov-open}** (The hypotheses are open.) Let (g, F, u), possibly with radial dusts (q_rad, u_rad),
satisfy (Ω) and (V3). Fix compact sets S ⊂ (Σ_τ0 ∩ Ω) × S¹ (points and labels) and S_r ⊂ Σ_τ0 ∩ Ω, with supp q ⊂ int S
and supp q_rad ⊂ S_r, and write D_α(S) for the tube of S_α := {x : (x, α) ∈ S}. Suppose that on the tubes of S and S_r
themselves: the Jacobian of (V1) is at least J0 on the tubes D_α(S); ∂_α β0 ≥ b on S, and β0(x, ·) is injective on
S_x := {α : (x, α) ∈ S}; dist(D_α(S), axes) ≥ 2δ; and every label of S makes an angle at least η with the radial null
directions on the tubes of S_r, or those tubes lie at distance at least η. Then there is a neighbourhood 𝒩 of (g, u|Σ_τ0,
∂u|Σ_τ0, u_rad|Σ_τ0, ∂u_rad|Σ_τ0) in C² × C¹ such that every solution (g′, F′, u′) with radial dusts (q′_rad, u′_rad)
whose data lie in 𝒩, with supp q′ ⊂ int S and supp q′_rad ⊂ S_r, and whose radial dusts satisfy the second clause of
(V2′), satisfies (V1), (V2) and the angle clause of (V2′) with margins J0/2, b/2, δ and η/2. (Ω) and (V3) are open in
C² × C¹.

*Proof.* The tubes are the images of S and S_r under the flows of the rays of (g′, u′) and (g′, u′_rad), which are null
geodesics of g′ with initial directions given by ∂u′|Σ_τ0 and ∂u′_rad|Σ_τ0. The rays and their first variation (whose
determinant is the Jacobian) solve ordinary differential equations whose coefficients are the Christoffel symbols of g′
and their first derivatives, so by continuous dependence on coefficients and data they depend continuously on (g′, u′) in
C² × C¹, uniformly on the compact S × [τ0, τ_end]; β0 and ∂_α β0 depend continuously on u′|Σ_τ0 in C¹. The four margins
are infima over compact sets of continuous positive functions, so on a neighbourhood they hold halved. For (V1), supp q′
is a compact subset of int S and the flow is a diffeomorphism, so the tube of supp q′ has a neighbourhood inside the tube
of S, where the Jacobian bound holds; this is why int S is needed. Injectivity is kept: if α_k ≠ α′_k in S_(x_k) had
β0′_k(x_k, α_k) = β0′_k(x_k, α′_k) for perturbations tending to zero, a limit point would give, by injectivity of β0(x,
·), α = α′, and then for k large α_k and α′_k lie in an interval on which ∂_α β0′_k ≥ b/2 > 0, a contradiction. For (V2′)
the radial tubes are those of S_r, the perturbed radial supports being kept in S_r; its second clause, (H2′) with adapted
boundaries, is a structural condition at the axes, not an inequality, and it is imposed on the perturbations. (Ω)
consists of strict inequalities between contractions of g⁻¹, continuous in C⁰, and of the statement on generators, which
holds for the tubes by their definition; (V3) consists of strict inequalities between functions of the slice data and
their first derivatives. ∎

**Proposition {#prop:vlasov-cauchy}** (Cauchy stability of the restricted system off the axes.) Let (g̊, F̊, ů) be a
smooth class Einstein–restricted massless Vlasov solution on Ω in label form, possibly with radial dusts satisfying
(H2′) of [[thm:class-stability]], and let S, S_r be as in [[lem:vlasov-open]] with the margins there. Fix m ≥ 6. There
are ε > 0 and C such that every invariant datum on Σ_τ0 (metric data satisfying the constraints and the gauge
condition, a field (F, u|Σ_τ0, ∂u|Σ_τ0) with supp F ⊂ int S, radial dusts with supports in S_r) within ε of the
reference's in H^m has a unique smooth class development on Ω, a solution of the Einstein–restricted massless Vlasov
system with radial dusts, within C ε of the reference in H^m. No smallness of the reference is assumed.

*Proof.* By [[lem:vlasov-open]] the perturbed labels keep their margins, so their tubes stay at distance at least δ from
the axes and free of caustics. Off the axes write the field as an orbit density f on the bundle ℬ of null directions
of g3, as in the proof of [[lem:vlasov-separation]]: at each point the labels present are mapped diffeomorphically onto
their directions, and T_V is algebraic in (f, g). By [[lem:vlasov-flow]] (b) and (c) the Vlasov equation is the
transport of f along the generator of the null geodesic flow on ℬ, whose coefficients are first derivatives of g3. In
the energy of the proof of [[thm:class-stability]] put the transport of f in place of the transports of finitely many
dusts: m derivatives of f cost m + 1 derivatives of the metric through the flow's coefficients, which the metric's
energy controls at that order, and m derivatives of T_V cost m derivatives of f and of g. So there is no loss of
derivatives, unlike a single dust in eikonal form, whose density is transported by □5 u, one derivative below g. The
radial dusts are governed by [[thm:class-stability]], with (H2′). The bootstrap, Gronwall's lemma and local existence
for the resulting symmetric hyperbolic system with these sources are as in the proof of [[thm:class-stability]]. On the
tubes, the eikonals of the solution with the data u|Σ_τ0, and the amplitudes transported by [[eq:vlasov-amplitude]],
represent the solution's field in label form, since by (V1) no caustic forms. ∎

The explicit family is built on the orbit space of Tangherlini, where the eikonal equation separates. Let μ = 1, f :=
1 − 1/r², m := 1/r², and let t := τ − κ(r) with κ′ = m/f be the static time on r > 1, so that g3 = −f dt² + f⁻¹dr² +
r² dϑ² there. For |α| ≤ 0.6 put k(α) := 3 sin α and

    u_α := t − k(α)(ϑ − π/4) − ∫_3^r f(s)⁻¹ (1 − f(s) k(α)²/s²)^(1/2) ds,      r > 1.                {#eq:vlasov-witness}

Since f/r² = (r² − 1)/r⁴ ≤ 1/4 and k² < 2.89, the square root is smooth and positive on r > 1.

**Proposition {#prop:vlasov-nonempty}** (The theorem is not vacuous.) Let g0 be Tangherlini of mass 1 in the chart of
[[sec:background]] with μ ≡ 1, and Ω the domain with τ0 = 0, τ_end = 3, a = 4/5 and V = 5. Let F0 ≥ 0 be a smooth
function of (r, ϑ, α), not identically zero, supported in {|r − 3| ≤ 0.3, |ϑ − π/4| ≤ 0.15} × [−0.5, 0.5], and let the
labels be the eikonals [[eq:vlasov-witness]]. Then for every small ε > 0 the class Einstein–restricted massless Vlasov
solution with the field of amplitude ε F0 and labels u_α, its metric data corrected by the radial solve, exists on Ω and
satisfies (Ω), (V1), (V2), (V2′) and (V3). By [[lem:vlasov-open]], the solutions covered by [[thm:vlasov]] form a
nonempty open set.

*Proof.* *(Ω) and (V3) for g0.* With μ = 1 the contractions of [[lem:domain]] are g0⁻¹(dτ, dτ) = −1 − 1/r² < 0; at r = a,
g0⁻¹(dr, dr) = 1 − 25/16 = −9/16 < 0 and g0⁻¹(dr, dτ) = 25/16 > 0, so {r = a} is spacelike and r decreases along future
causal curves near it, as in the proof of [[lem:domain]] (b); g0⁻¹(d(v + τ), d(v + τ)) = −3 − 1/r² < 0, and v + τ
increases along future causal curves, as in [[lem:domain]] (c); and b(τ) = 9 − 2τ ≥ 3, so b(τ) − a ≥ 11/5. On Σ_0 the
data of g0 are γ = (1 + 1/r²) dr² + r² dΩ², and by [[lem:constraints-evolution]] (a) the spheres have mean curvature
3/(r² + 1)^(1/2) > 0 and 𝒮 A0 = diag(6, 1/(r² + 1)) > 0. The statement of (Ω) on generators holds for the tubes by their
definition.

*The rays.* Put w := (1 − f k²/r²)^(1/2). Then −u_t²/f + f u_r² + u_ϑ²/r² = −1/f + (1 − f k²/r²)/f + k²/r² = 0, so u_α is
an eikonal. Its future rays solve dt/ds = 1/f, dr/ds = w, dϑ/ds = k/r², and with dτ/dt = 1 + κ′ dr/dt = 1 + m w,

    dr/dτ = W(r) := f w/(1 + m w),      dϑ/dτ = Θ(r) := f k/(r² (1 + m w)),

functions of r alone at fixed α. Let S̃ := {|r − 3| ≤ 0.36, |ϑ − π/4| ≤ 0.18} and S := S̃ × [−0.6, 0.6], so that
supp F0 ⊂ int S. For |α| ≤ 0.6, |k| ≤ 3 sin 0.6 < 1.7, and for r ≥ 2.64, f k²/r² ≤ 2.89/6.9696 < 0.42, so w > 0.76,
f > 0.856 and m < 0.1435, and W ≥ f w/(1 + m) > 0.56. W is increasing in r on r² > 2: f increases, m decreases, and
f k²/r² = k²(r² − 1)/r⁴ has derivative 2k²(2 − r²)/r⁵ < 0, so w increases and W = f/(w⁻¹ + m) has an increasing
numerator and a decreasing positive denominator. On the rays from S̃, r ≥ 2.64 and r increases, and |Θ| ≤ |k|/r² <
1.7/r².

*(V1).* In the coordinates (r, ϑ) the flow map from Σ_0 to Σ_τ is (r0, ϑ0) ↦ (R(τ; r0), ϑ0 + ∫_0^τ Θ(R(s; r0)) ds), with
dR/dτ = W(R), R(0; r0) = r0. Its Jacobian is ∂R/∂r0 = W(R(τ; r0))/W(r0), since both sides solve y′ = W′(R) y with y(0)
= 1; as R ≥ r0 and W increases, it is at least 1 =: J0. On Σ_0, t = −κ(r), so d(u_α|Σ_0) = −(κ′ + ϕ′) dr − k dϑ with
κ′ + ϕ′ = (m + w)/f, ϕ the integral in [[eq:vlasov-witness]]. In the coframe ((1 + m)^(1/2) dr, r dϑ), orthonormal for
the orbit part (1 + m) dr² + r² dϑ² of γ, its angle β0 from the inward radial direction satisfies tan β0 = T(r, k) :=
k f (1 + m)^(1/2)/(r (m + w)). Since ∂_k w = −f k/(r² w),

    ∂_k T = (f (1 + m)^(1/2)/r) ((m + w) + f k²/(r² w))/(m + w)² ≥ f/(r (1 + m)) = (r² − 1)/(r (r² + 1)),

which decreases on r² > 2 + √5 and is > 0.249 on [2.64, 3.36]. There |T| ≤ 1.7 · 1.0694/(2.64 · 0.8485) < 0.82, since m >
0.0885 there, so cos²β0 = (1 + T²)⁻¹ > 0.59; and dk/dα = 3 cos α ≥ 3 cos 0.6 > 2.47. Hence ∂_α β0 = cos²β0 ∂_k T dk/dα >
0.59 · 0.249 · 2.47 > 0.36 =: b on S, and β0(x, ·) is increasing, so injective: the field is labelled by initial
direction.

*(V2).* A ray from S̃ is in Ω only while r ≤ b(τ) = 9 − 2τ, and r ≥ 2.64 + 0.56 τ on it, so only for τ ≤ 6.36/2.56 <
2.49. Over that time |ϑ − ϑ0| ≤ ∫_0^2.49 1.7 (2.64 + 0.56 s)⁻² ds = (1.7/0.56)(1/2.64 − 1/4.0344) < 0.40. So on the tubes
of S, ϑ ∈ [0.2054, π/2 − 0.2054] and r ≥ 2.64, and ρ1 = r cos ϑ, ρ2 = r sin ϑ are at least 2.64 sin 0.2054 > 0.53 =: 2δ.
(V2′) is vacuous, there being no radial dust.

*The solutions.* The data are those of g0 on Σ_0 with the field ε F0 and the labels u_α|Σ_0 on the outgoing branch, the
metric data corrected by the radial solve of [[sec:data-evolution]] with the stress of the field, which is small and
which (V3), holding at g0 with margin, allows. By [[prop:vlasov-cauchy]] around g0 (with the zero field, the margins of
[[lem:vlasov-open]] holding on the tubes of S by the two preceding steps), the solution exists on Ω for ε small and is
close to g0 in H^m for every m, hence in C², and its eikonals with the data u_α|Σ_0 are C¹-close to u_α. By
[[lem:vlasov-open]] it satisfies (V1) and (V2) with margins 1/2, 0.18 and δ = 0.265, and (Ω), (V3) by openness. ∎

**Remark {#rem:vlasov-test-family}** (Numerical observation.) For the family with data u_α = cos α ρ(r) + 3 sin α ϑ on
Σ_0, ρ′ = (1 + 1/r²)^(1/2), outgoing labels α ∈ [−0.5, 0.5] and ingoing labels α ∈ [π − 0.15, π + 0.15] (inside the
horizon when they leave Ω), and the density on the same ball, the margins were measured on a 9 × 9 grid of rays over
the ball enlarged by 20 %, with 81 labels per interval: J0 = 1.0000 and 0.8978, δ = 0.157 and 0.098, b = 0.909. A family
focused at distance 1 ahead had a Jacobian changing sign (least value −0.071); a wider ingoing interval [π − 0.5,
π + 0.5] reached an axis inside the horizon, as [[prop:vlasov-axis-focus]] predicts, so (V2) is a real restriction;
with mass 1.02 and directions tilted by 0.02 sin 2ϑ, the margins were J0 = 1.0000 and 0.8471, δ = 0.152 and 0.072. No
proof uses these values.
