# Part. The horizon, the construction from past null infinity and the mass law {#part:remaining}

## The boundary, the spheres' horizon and the mean mass {#ch:horizon-mass}

This chapter proves the three propositions of [[thm:main]] that concern the geometry of the solutions g_λ: the
curvature boundary x_K = 1 is spacelike ([[prop:boundary-spacelike]]), the outgoing expansion of the round spheres
has exactly one zero on each column, close to √μ ([[prop:one-zero]]), and the Hawking mass of every round sphere is
μ(v) up to O(λ²) outside the shell ([[prop:mean-mass]]). Items 6 and 7 of [[thm:main]] are the last two.

### Notation and the facts used {#sec:horizon-notation}

Throughout, K ≥ 6, 0 < λ ≤ λ0, g_λ is the solution of [[thm:main]] on Ω, g_app = g0 + λ[g1] + Σ_(j=2)^N λ^j [g_j] is
its approximant ([[thm:approximant]]) and w := g_λ − g_app. The profiles and the bracket [f](X) := f(X, v(X)/λ) are
those of [[sec:profiles]]. Step 1 of the proof of [[thm:uniform-existence]] gives, with M the constant of that
theorem,

    ‖∂^i w‖_∞ ≤ C M λ^(K−3−i),   i ≤ 4,   on Ω.                                                 {#eq:remainder-pointwise}

The first profile is g1 = m1 + W(X, θ + φ1(X)), where the mean m1 and the phase φ1 do not depend on θ, and
W = W_TT + χ dv², with W_TT the wave of [[eq:waves]] and χ its second harmonic ([[eq:chi-transport]]). We use two
properties of W: W(ℓ, ·) = 0 ([[lem:stage-zero]] (a)), and W_TT has no dτ, dr or dv component ([[lem:waves]] (b)).

On R⁴ we use r = |x|, and on S³ the angles (ϑ, ξ1, ξ2) given by x1 + i x2 = r cos ϑ e^(iξ1), x3 + i x4 = r sin ϑ e^(iξ2),
0 ≤ ϑ ≤ π/2. The round metric of S³ is dϑ² + cos²ϑ dξ1² + sin²ϑ dξ2², and ζ := cos 2ϑ. We write ξ1, ξ2 for the two
azimuths because φ1 is the first phase. In this chart

    g0 = −dτ² + dr² + r² (dϑ² + cos²ϑ dξ1² + sin²ϑ dξ2²) + (μ(v)/r²)(dτ + dr)²,

which is block diagonal between the (τ, r) plane and the sphere, and the wave of [[eq:waves]] reads

    λ W_TT = 2 r^(1/2) (cos²ϑ p1 dξ1² + sin²ϑ p2 dξ2² − (p1 + p2) dϑ²),
    p1 := (2 cos²ϑ G − sin²ϑ F)/3,   p2 := (2 sin²ϑ F − cos²ϑ G)/3,                                   {#eq:waves-hopf}

with F := λ A env(v) h(ζ) sin θ, G := λ A env(v) h(ζ) cos θ and h(ζ) := √(2/(1 + ζ²)), at the phase θ.

For a sphere S_(v,r) := {τ = v − r, |x| = r} we write tr_S f := γ0^(AB) f_AB for the trace on S_(v,r), with γ0 the
metric g0 induces there, r² times the round metric. The covectors dτ and dr vanish on the tangent spaces of S_(v,r),
and so does dv = dτ + dr. It follows at once from [[eq:waves-hopf]] that

    tr_S W = 0   on every S_(v,r) and at every phase.                                                {#eq:wave-traceless}

Indeed χ dv² vanishes on tangent vectors of the sphere, and tr_S W_TT = r⁻² · 2 r^(1/2) λ⁻¹ (cos²ϑ p1/cos²ϑ + sin²ϑ
p2/sin²ϑ − (p1 + p2)) = 0.

A *column* is the set of points of D_T ∩ {τ ≥ τ0} with v and x̂ ∈ S³ fixed and r varying. Its points are
(τ, x) = (v − r, r x̂), so d/dr along a column is −∂_τ + x̂·∂_x = ℓ, and a column is an integral curve of ℓ. Since
ℓ(v) = 0, the derivative along a column of a bracket is

    (d/dr) [f] = [ℓ f],                                                                           {#eq:column-derivative}

with ℓ acting on X only: no factor λ⁻¹ appears. A column lies in {r_q(v) ≤ r ≤ v − τ0}.

### The boundary {#sec:boundary}

*Proof of [[prop:boundary-spacelike]].* Write m := μ/r². By [[prop:vaidya]] (d),
g0⁻¹(dr, dr) = 1 − m, g0⁻¹(dr, dτ) = m and g0⁻¹(dτ, dτ) = −1 − m; since dv = dτ + dr, also g0⁻¹(dv, dv) = 0,
g0⁻¹(dv, dr) = 1 and g0⁻¹(dv, dτ) = −1. On x_K = 1 put Φ := r − r_q(v), r_q = (√72 μ l5²)^(1/4). Then
dΦ = dr − r_q′ dv with r_q′ = r_q μ′/(4μ), and

    g0⁻¹(dΦ, dΦ) = g0⁻¹(dr, dr) − 2 r_q′ g0⁻¹(dr, dv) + r_q′² g0⁻¹(dv, dv) = 1 − m − 2 r_q′.

At r = r_q, m = μ/r_q² = μ/(√72 μ l5²)^(1/2) = √(μ/(√72 l5²)), and 2 r_q′ = r_q μ′/(2μ). This is the formula of
[[prop:boundary-spacelike]].

*Sign.* μ is nondecreasing, so μ′ ≥ 0, and μ ≥ μ0 ≥ √72 l5². The second term is therefore at most −1 and the third at
most 0. Where μ > √72 l5² the second term is below −1; where μ′ > 0 the third is negative. At such points dΦ is
timelike for g0, which is to say that the hypersurface {Φ = 0} is spacelike.

*Time orientation.* g0⁻¹(dΦ, dτ) = g0⁻¹(dr, dτ) − r_q′ g0⁻¹(dv, dτ) = m + r_q′ > 0. The covector dτ is timelike
([[lem:domain]] (a)), and it is positive on future causal vectors because τ is a time function for the time orientation
of g0, in which L0, with L0(τ) = 1, is future directed. Where dΦ is timelike too, the two have positive
g0⁻¹-product and so lie in opposite halves of the cone of timelike covectors: dΦ(Z) < 0 for every future causal vector
Z there. In particular dΦ(Y) = −g0⁻¹(dΦ, dτ) < 0 for the future timelike Y := −g0⁻¹ dτ. By continuity of the cone, every
point of {Φ = 0} at which dΦ is timelike has a neighbourhood U and a c > 0 with dΦ(Z) ≤ −c dτ(Z) for every future causal
Z at points of U.

*No return.* A future causal curve γ has dτ(γ′) > 0, so it may be parametrized by τ. Suppose γ meets {Φ = 0} at γ(τ1),
a point where μ > √72 l5² or μ′ > 0. Along γ, v does not decrease (dv(Z) = −g0(L0, Z) ≥ 0 for future causal Z) and μ is
nondecreasing; so if μ(v) > √72 l5² at γ(τ1) it holds at every later point of γ, and if μ′ > 0 there, then μ(v) >
μ(v(γ(τ1))) ≥ √72 l5² at every later point with larger v, while the points with the same v satisfy μ′ > 0. Hence the
condition holds at every later point of γ on {Φ = 0}, and at each such point Φ ∘ γ is strictly decreasing near it, by
the inequality of the time orientation. So Φ ∘ γ < 0 immediately after τ1: γ leaves D_T = {r ≥ r_q(v)} ∩ {v ≤ v_end + T}
there. If γ(τ2) ∈ D_T for some τ2 > τ1, let τ3 be the infimum of the τ > τ1 with Φ(γ(τ)) ≥ 0. Then τ3 > τ1,
Φ(γ(τ3)) = 0 and Φ ∘ γ < 0 on (τ1, τ3), which contradicts the strict decrease of Φ ∘ γ near τ3. So γ does not return.

*The margin.* If μ0 > √72 l5², then 1 − √(μ/(√72 l5²)) ≤ 1 − √(μ0/(√72 l5²)) = −δ_b and the third term is at most
0, so g0⁻¹(dΦ, dΦ) ≤ −δ_b on the whole boundary. By item 4 of [[thm:main]], |g_λ − g0| ≤ C λ on Ω; since g0⁻¹ is bounded on
the compact Ω and inversion is smooth, |g_λ⁻¹ − g0⁻¹| ≤ C1 λ. The covector dΦ = dr − r_q′ dv is bounded on Ω, so

    g_λ⁻¹(dΦ, dΦ) ≤ g0⁻¹(dΦ, dΦ) + C λ ≤ −δ_b + C λ ≤ −δ_b/2      once C λ ≤ δ_b/2.

Moreover g_λ⁻¹(dΦ, dτ) ≥ m + r_q′ − C λ, and m ≥ μ0/r² is bounded below on Ω, so g_λ⁻¹(dΦ, dτ) > 0 for λ small.
The covector dτ is timelike for g_λ ([[lem:domain]] (e)), and g_λ is time oriented, as g0 is, so that dτ is positive
on its future causal vectors. The argument of the time orientation, with g_λ in place of g0, then gives at every point
of {Φ = 0} a neighbourhood U and a c > 0 with dΦ(Z) ≤ −c dτ(Z) for every future causal vector Z of g_λ at points of U.
The no-return argument for g0 used that v does not decrease along causal curves of g0, and only to carry the condition
μ > √72 l5² or μ′ > 0 from γ(τ1) to the later points of γ on {Φ = 0}. For g_λ no such step is needed: the margin
g_λ⁻¹(dΦ, dΦ) ≤ −δ_b/2 holds at every point of the boundary, so the inequality dΦ(Z) ≤ −c dτ(Z) holds near every point
of {Φ = 0}, and the first-return argument applies to every future causal curve of g_λ as it stands.

*Equality.* If μ0 = √72 l5², then on {v ≤ inf supp env} μ = μ0 and μ′ = 0, so the formula gives g0⁻¹(dΦ, dΦ) = 0,
and r_q = (√72 μ0 l5²)^(1/4) = (μ0²)^(1/4) = √μ0: the boundary is the seed's horizon r = √μ0, null for g0. That g_λ
equals g0 on that region, so that the boundary is null for g_λ there, and that after the shell starts the boundary is
spacelike for g_λ outside a layer whose width tends to 0 with λ, are proved in [[ch:equality-layer]];
that for λ small every column of the layer has points where the boundary is timelike for g_λ, so that the no-return
property fails at equality, is [[thm:layer]], [[cor:layer]] and [[thm:very-edge]]. ∎

**Remark {#rem:boundary-first-order}** (The first-order term at the boundary.) Put ♯dΦ := g0⁻¹ dΦ. Expanding
g_app⁻¹ = g0⁻¹ − λ g0⁻¹ [g1] g0⁻¹ + O(λ²),

    g_λ⁻¹(dΦ, dΦ) = g0⁻¹(dΦ, dΦ) − λ ([χ(·, θ + φ1)] + m1(♯dΦ, ♯dΦ)) + O(λ²) + O(|w|).

Indeed [g1](♯dΦ, ♯dΦ) = m1(♯dΦ, ♯dΦ) + [χ(·, θ + φ1)] (dv(♯dΦ))² + [W_TT(·, θ + φ1)](♯dΦ, ♯dΦ). Here dv(♯dΦ) =
g0⁻¹(dv, dr) − r_q′ g0⁻¹(dv, dv) = 1. The covector dΦ lies in the span of dτ and dr, so ♯dΦ lies in the span of ∂_τ
and ∂_r, g0 being block diagonal; W_TT has only components on the sphere, so its value on ♯dΦ is 0. The wave W_TT
drops out exactly.

### The expansions of the round spheres {#sec:sphere-expansions}

**Lemma {#lem:round-spheres}** (The round spheres of g0.) For the sphere S_(v,r) and g0, the future null normals with
n(τ) = 1 are

    n⁺ = ∂_τ + ((r² − μ)/(r² + μ)) ∂_r,      n⁻ = L0 = ∂_τ − ∂_r,                                   {#eq:round-normals}

with expansions and inner product

    θ⁺ = 3 (r² − μ)/(r (r² + μ)),     θ⁻ = −3/r,     g0(n⁺, n⁻) = −2 r²/(r² + μ).                  {#eq:round-expansions}

θ⁺ has one zero on (0, ∞), at r = √μ, where ∂_r θ⁺ = 3/μ. The area of S_(v,r) is 2π² r³, and M[S_(v,r)](g0) = μ(v)
for the mass M of [[prop:mean-mass]].

*Proof.* Put m := μ/r². In the chart of [[sec:horizon-notation]], g0 restricted to the (τ, r) plane is
g_ττ = −1 + m, g_τr = m, g_rr = 1 + m, and the normal plane of S_(v,r) is spanned by ∂_τ and ∂_r. A vector
∂_τ + β ∂_r is null when −1 + m + 2 m β + (1 + m) β² = 0, whose roots are β = (1 − m)/(1 + m) and β = −1. The root
β = −1 gives L0, which points inward, and the other gives n⁺. Both have n(τ) = 1 > 0, and τ is a time function, so both
are future directed.

Since g0 is block diagonal with sphere part r² times the round metric, the second fundamental form of S_(v,r) along a
normal n is r n(r) times the round metric, and the expansion is θ_n = (r²)⁻¹ · 3 · r n(r) = 3 n(r)/r. So θ⁺ =
3(1 − m)/((1 + m) r) = 3(r² − μ)/(r(r² + μ)) and θ⁻ = 3 L0(r)/r = −3/r. Next, g0(n⁺, L0) = g_ττ + (β − 1) g_τr − β g_rr
= −1 − β = −2/(1 + m) = −2r²/(r² + μ). The numerator of θ⁺ vanishes on (0, ∞) only at r² = μ; there the derivative
falls on the numerator alone, ∂_r θ⁺ = 6r/(r · 2μ) = 3/μ.

The area is r³ times the volume 2π² of S³, so R = r. Then Θ = 2 θ⁺ θ⁻/(−g0(n⁺, n⁻)) = 2 · 3(1 − m)/((1 + m) r) ·
(−3/r) · (1 + m)/2 = −9(1 − m)/r², constant on the sphere, and M = r² (1 + (r²/9)(−9(1 − m)/r²)) = r² m = μ(v). ∎

The next lemma is the reason the oscillation is invisible to the spheres at leading order. It is stated for every
metric of the two-scale form of g_app, so that it applies to the solutions of [[ch:past-construction]] as well.

**Lemma {#lem:sphere-two-scale}** (The sphere quantities of a two-scale metric.) Let

    g = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j]

with profiles g_j bounded on Ω × S¹ with all their (X, θ)-derivatives, independently of λ, and with g1 = m1 + W(X, θ +
φ1(X)), where m1 and φ1 do not depend on θ, W(ℓ, ·) = 0, and tr_S W = 0 on every S_(v,r) at every phase. There are
λ* > 0 and C such that for 0 < λ ≤ λ* the following holds on every sphere S_(v,r) in Ω.

(a) The future null expansions of S_(v,r) for g, with normals normalized by n(τ) = 1, are

    θ^±(g) = θ^±(g0) + λ [Θ^±_1] + λ² E^±,                                                         {#eq:theta-two-scale}

with profiles Θ^±_1 and functions E^± = e^±(X, v/λ, λ), where e^± is smooth in (X, θ, λ) and bounded with all its
X-derivatives, uniformly in λ ≤ λ*. No term of order λ⁻² or λ⁻¹ occurs, and none of order λ⁰ beyond g0's.

(b) The area element of S_(v,r), the inner product g(n⁺, n⁻) and the normals have expansions of the same form.

(c) Along a column, (d/dr)(θ^±(g) − θ^±(g0)) = O(λ), and the same holds for the quantities of (b).

*Proof.* The conormal plane of S_(v,r), the covectors that vanish on its tangent spaces, is spanned by dτ and dr at
every point with r > 0, the axes included. For a metric g near g0 let k^± := c^±(X, g)(dr + α^±(X, g) dτ) be its two
null covectors in that plane, with n^± := g⁻¹ k^± normalized by n^±(τ) = 1; for g near g0 the two null directions stay
distinct, so c^±, α^± are smooth functions of (X, g). Let Π_g^(ab) be the inverse of the metric g induces on the sphere,
pushed forward:

    Π_g = g⁻¹ + (n⁺ ⊗ n⁻ + n⁻ ⊗ n⁺)/(−g(n⁺, n⁻)),

smooth in (X, g); it annihilates k⁺ and k⁻, hence every covector of the conormal plane. The covector field k^± is, at
each point, the null conormal of the sphere S_(v,r) through that point, and the second fundamental form of S_(v,r)
along n^± is (∇k^±)(Y, Z) = Y^a Z^b (∂_a k^±_b − Γ[g]^c_(ab) k^±_c) on tangent vectors Y, Z. So, in Cartesian
coordinates,

    θ^±(g) = Π_g^(ab) (∂_a k^±_b − Γ[g]^c_(ab) k^±_c),     Γ[g]^c_(ab) = ½ g^(cd) (∂_a g_db + ∂_b g_da − ∂_d g_ab).
                                                                                                    {#eq:theta-cartesian}

The first term contains no derivative of g. The Cartesian components of dτ are constant and those of dr are ∂_b r, so

    ∂_a k^±_b = (∂_a c^±) (dr + α^± dτ)_b + c^± ∂_a ∂_b r + c^± (∂_a α^±) dτ_b.

The derivatives of c^± and α^± are where ∂g enters, and they multiply dr + α^± dτ and dτ, which Π_g annihilates. Hence

    Π_g^(ab) ∂_a k^±_b = c^±(X, g) Π_g^(ab) ∂_a ∂_b r,

a smooth function of (X, g) on r > 0. So θ^±(g) is a smooth function of (X, g) plus a smooth function of (X, g) times
∂g: it is affine in ∂g. (In the polar chart of [[sec:horizon-notation]] the components of k^± along the sphere vanish
identically and the first term is absent; in Cartesian components it is not, and for the flat metric η, where Γ = 0,
it is the whole expansion ±3/r.)

Let ĝ(X, θ; λ) := g0 + λ g1 + Σ_(j≥2) λ^j g_j be the profile of g, so g = [ĝ]. By the chain rule of
[[sec:profiles]], ∂_a g = λ⁻¹ (∂_a v) [∂_θ ĝ] + [∂_a ĝ]. The first term of [[eq:theta-cartesian]] depends on g only
through its value, so it is c^±(X, [ĝ]) Π_[ĝ]^(ab) ∂_a ∂_b r, with no fast part. In Γ_(dab) the fast parts of ∂_a g_db
and ∂_b g_da carry the factor ∂_a v or ∂_b v, and Π_g^(ab) ∂_a v = 0 because dv lies in the conormal plane. Only the
fast part of −½ ∂_d g_ab survives, and it contributes ½ λ⁻¹ k^±_c g^(cd) ∂_d v Π_g^(ab) [∂_θ ĝ_ab] = ½ λ⁻¹ k^±(ℓ_g)
Π_g^(ab) [∂_θ ĝ_ab], with ℓ_g := g⁻¹ dv. Hence θ^±(g) = f^±(X, v/λ, λ) with

    f^±(X, θ, λ) := Θ^±_slow(X, ĝ, ∂_X ĝ) + ½ k^±(ℓ_ĝ) Π_ĝ^(ab) (∂_θ g1 + λ ∂_θ g2 + λ² ∂_θ g3 + …)_ab,

where Θ^±_slow(X, ĝ, ∂_X ĝ) := c^±(X, ĝ) Π_ĝ^(ab) ∂_a ∂_b r − Π_ĝ^(ab) Γ^c_(ab) k^±_c, with Γ formed from ĝ and ∂_X ĝ
in place of g and ∂g, and we used ∂_θ ĝ = λ ∂_θ g1 + λ² ∂_θ g2 + …, which cancels the factor λ⁻¹. The function f^± is
smooth in (X, θ, λ) for λ ≤ λ*, λ* small enough that ĝ stays near g0, and it is bounded with all its X- and
θ-derivatives. At λ = 0, ĝ = g0 and ∂_X ĝ = ∂g0, so the first term is the right side of [[eq:theta-cartesian]] for g0,
which is θ^±(g0), and the second is ½ k^±_0(ℓ) γ0^(AB) ∂_θ (g1)_AB = ½ k^±_0(ℓ) ∂_θ tr_S g1. Now tr_S g1 = tr_S m1 +
tr_S W(X, θ + φ1), the first independent of θ and the second zero by hypothesis, so this term vanishes and
f^±(X, θ, 0) = θ^±(g0). Taylor's formula in λ with integral remainder gives f^± = θ^±(g0) + λ Θ^±_1 + λ² e^± with
Θ^±_1 := ∂_λ f^±(·, ·, 0) and e^± of the stated kind. This is (a).

The term c^± Π_g^(ab) ∂_a ∂_b r is what distinguishes [[eq:theta-cartesian]] from the polar formula, and it changes
none of these conclusions, because it contains no derivative of g: it produces no factor λ⁻¹, so it lies in Θ^±_slow
and leaves the fast term ½ λ⁻¹ k^±(ℓ_g) Π_g^(ab) [∂_θ ĝ_ab] as it is; at λ = 0 it is the corresponding term of
θ^±(g0); and it is part of the smooth function f^±, to which the argument of (c) below applies as to the rest.

The area element, g(n⁺, n⁻) and n^± are smooth functions of (X, g) alone, with no derivative of g, so the same Taylor
argument applies with no fast term at all: (b). For (c), along a column v is constant, so by [[eq:column-derivative]]
the derivative of f(X, v/λ, λ) along it is (ℓ_X f)(X, v/λ, λ), bounded with no factor λ⁻¹; applied to λ Θ^±_1 + λ² e^±
it is O(λ). ∎

The first profile of g_app satisfies the hypotheses of [[lem:sphere-two-scale]]: W(ℓ, ·) = 0, and tr_S W = 0 by
[[eq:wave-traceless]]. The remaining profiles are bounded with their derivatives by [[thm:approximant]].

*Proof of [[prop:one-zero]].* Let λ ≤ λ0 and write θ⁺_λ := θ⁺(g_λ).

(i) The expansion as a function of the metric. By [[eq:theta-cartesian]] and the identity after it, θ⁺(g) =
c⁺(X, g) Π_g^(ab) ∂_a ∂_b r − Π_g^(ab) Γ[g]^c_(ab) k⁺_c: a smooth function of (X, g) plus a smooth function of (X, g)
times ∂g, so affine in ∂g. It is estimated in the Cartesian arrays, in which the axes are regular points.

(ii) The background. By [[lem:round-spheres]], θ⁺(g0) = 3(r² − μ)/(r(r² + μ)). Since S_(v,r) lies in {v = const}, μ =
μ(v) enters only algebraically. Its one zero on (0, ∞) is r = √μ, simple, with ∂_r θ⁺(g0) = 3/μ there. The ingoing
expansion is −3/r < 0.

(iii) The approximant. By [[lem:sphere-two-scale]] applied to g = g_app, θ⁺(g_app) = θ⁺(g0) + λ [Θ⁺_1] + λ² E⁺, and
along every column

    |θ⁺(g_app) − θ⁺(g0)| + |(d/dr)(θ⁺(g_app) − θ⁺(g0))| ≤ C λ.

(iv) The remainder. Since θ⁺ is smooth in g and affine in ∂g, and ∂g_app and ∂g_λ are bounded,
|θ⁺(g_λ) − θ⁺(g_app)| ≤ C (|w| + |∂w|). Its derivative along a column is at most C (|w| + |∂w| + |∂²w|): the derivative
falls on w, on ∂w, or on coefficients that are smooth functions of (X, g) at g_app or g_λ, times ∂g_app; these have
bounded derivatives along a column, since ℓ g_app and ℓ ∂g_app = dv ⊗ [ℓ ∂_θ g1] + O(1) are bounded, because
ℓ(v) = 0. By [[eq:remainder-pointwise]] both are at most C M λ^(K−5) ≤ C λ, as K ≥ 6. With (iii), along every column

    |θ⁺_λ − θ⁺(g0)| + |(d/dr)(θ⁺_λ − θ⁺(g0))| ≤ C3 λ.                                              {#eq:theta-plus-close}

The same two steps, with [[lem:sphere-two-scale]] (a) for θ⁻ and θ⁻(g0) = −3/r, give |θ⁻(g_λ) + 3/r| ≤ C3 λ on the
columns, C3 enlarged if necessary.

(v) The zero. The columns lie in the compact Ω, and r ≥ r_q(v) ≥ q0 > 0 on them. The difference
√μ − r_q = μ^(1/2) − b μ^(1/4), b := (√72 l5²)^(1/4), equals μ^(1/4)(μ^(1/4) − b) and has derivative
¼ μ^(−3/4)(2 μ^(1/4) − b) in μ, which is positive for μ > b⁴/16 = √72 l5²/16, in particular for μ ≥ μ0 ≥ √72 l5².
So √μ(v) − r_q(v) is at least its value at μ0, which is positive when μ0 > √72 l5². Put μ_max := μ(v_end). Fix δ in
(0, that value) such that ∂_r θ⁺(g0) ≥ 3/(2 μ_max) on |r − √μ(v)| ≤ δ (possible by continuity, since ∂_r θ⁺(g0) = 3/μ ≥
3/μ_max at r = √μ), and let m_δ > 0 be the minimum of |θ⁺(g0)| on the compact rest of the columns. Let r_max be the
largest value of r on Ω, and let λ_H ≤ λ0 be such that C3 λ_H < min(m_δ, 3/(4 μ_max), 3/r_max) and λ_H ≤ λ*. For
λ ≤ λ_H, by [[eq:theta-plus-close]], θ⁺_λ has no zero
where |r − √μ| > δ, and on |r − √μ| ≤ δ its r-derivative is at least 3/(2 μ_max) − C3 λ > 3/(4 μ_max), so it is strictly
increasing there. Hence it has at most one zero on each column, positive above it and negative below it.

If the column contains [√μ − δ, √μ + δ], which holds when √μ(v) ≤ v − τ0 − δ1 with δ1 := δ, then θ⁺_λ changes sign on
that interval (|θ⁺_λ(√μ)| ≤ C3 λ and the slope exceeds 3/(4 μ_max)), so it has exactly one zero R_λ, and

    |R_λ − √μ(v)| ≤ C′ λ,     C′ := C3/(3/(4 μ_max)).

Put C := 2 C′. On the band, for r ≤ √μ − C λ,

    θ⁺_λ(r) ≤ θ⁺_λ(√μ) − (3/(4 μ_max)) (√μ − r) ≤ C3 λ − 2 C3 λ < 0,

and likewise θ⁺_λ(r) ≥ C3 λ > 0 for r ≥ √μ + C λ. At distance C′ λ these bounds give only θ⁺_λ ≤ 0 and θ⁺_λ ≥ 0,
which is why C is taken to be twice C′. Off the band θ⁺_λ has the sign of θ⁺(g0). The ingoing expansion satisfies
θ⁻(g_λ) ≤ −3/r + C3 λ ≤ −3/r_max + C3 λ < 0 at every point of the columns, by the bound after
[[eq:theta-plus-close]] and the choice of λ_H. So the spheres with r ≤ √μ − C λ are trapped, both future null
expansions being negative at every point, and those with r ≥ √μ + C λ are untrapped.

If μ0 = √72 l5², fix instead δ in (0, √μ_max − r_q(μ_max)) with the same band property. The argument for the zero and
the signs runs on the columns where √μ − r_q ≥ δ; by the monotonicity in μ shown above, this is μ(v) ≥ μ0 + δ2 for some
δ2 > 0. The first assertion uses only the monotonicity band and the absence of zeros off it, and holds on every column. ∎

**Remark {#rem:round-family}** (The round family.) The zero set of θ⁺_λ on the columns is not a marginally trapped
surface: the statement concerns the round family {S_(v,r)}. Although ∂g_λ converges only weakly, the expansion of these
spheres does not see the oscillation at leading order, because the wave is traceless on them
([[eq:wave-traceless]]) and the phase v/λ is constant along each column ([[eq:column-derivative]]).

**Remark {#rem:round-family-numerics}** (Numerical observation.) A numerical evolution of the metric in the Bondi form
[[eq:bondi-form]] from the free data of [[sec:waves]], with each quantity read on the same round spheres, agrees with
[[prop:one-zero]]: the departure of the computed zero of θ⁺ from √μ halves when λ is halved, the successive ratios being
2.47, 2.26 and 2.14 at μ0/l5² = 100, and 2.26 and 2.14 at μ0/l5² = 1000. No proof in this paper uses this observation.

### The Hawking mass and the quarter turn {#sec:quarter-turn}

For a spacelike 3-sphere S and a Lorentzian metric g near g0, let M[S](g) be the five-dimensional Hawking mass of
[[prop:mean-mass]]: M[S](g) := R²(1 + (R²/9)⟨Θ⟩), R := (Area(S)/(2π²))^(1/3), Θ := 2 θ⁺ θ⁻/(−g(n⁺, n⁻)), ⟨·⟩ the mean
over S. Θ does not depend on the normalization of n^±. M is natural: M[S](ψ* g) = M[ψ(S)](g) for every diffeomorphism
ψ and every g near g0, since every ingredient is defined by g and S alone. It is a smooth function of g and ∂g on S.

Let J be the linear map (τ, x1, x2, x3, x4) ↦ (τ, x3, x4, x1, x2), which exchanges the two planes of the T² action. In
the angles of [[sec:horizon-notation]] it is ϑ ↦ π/2 − ϑ, ξ1 ↔ ξ2. J lies in O(4) acting on x, so it fixes τ, r and v,
maps each S_(v,r) to itself, and is an isometry of g0 = η + (μ(v)/r²) dv², both terms being O(4)-invariant; J² is the
identity, and J_* ℓ = ℓ. For a family of profiles (g_j) put

    (S g)_j (X, θ) := (−1)^j (J* g_j)(X, 3π/2 − θ).                                             {#eq:quarter-turn-action}

**Lemma {#lem:quarter-turn}** (The quarter-turn symmetry.) (a) For every family of profiles (g_j) with
g := g0 + Σ_j λ^j g_j, the sum g̃ := g0 + Σ_j λ^j (S g)_j has two-scale residual R[g̃](X, θ; λ) =
J* R[g](X, 3π/2 − θ; −λ). Its coefficient of λ^m is (−1)^m J* R^(m)(·, 3π/2 − ·), so S preserves (E1)–(E3) of
[[def:approximant]] at every order: it preserves (E1), (E2) and the vanishing of each coefficient R^(m).

(b) The stage-0 wave is S-invariant: (J* W_TT)(X, 3π/2 − θ) = −W_TT(X, θ); so is χ, and so is W = W_TT + χ dv² at
weight 1.

(c) The profiles of the approximant of [[thm:approximant]], with the stage data of [[lem:stage-data]], satisfy
S g = g:

    (J* g_j)(·, 3π/2 − ·) = (−1)^j g_j,   and for the means,   J* ⟨g_j⟩ = (−1)^j ⟨g_j⟩;   in particular J* m1 = −m1.

*Proof.* (a) The operator R[g] is Ric^H of [[eq:gauge]] with every ∂_a replaced by D^λ_a := ∂_a + λ⁻¹
(∂_a v) ∂_θ ([[def:two-scale]]), and it contains no explicit θ. Let ρ(θ) := 3π/2 − θ. Since ∂_θ (f ∘ ρ) =
−(∂_θ f) ∘ ρ, we have D^λ_a (f ∘ ρ) = (D^(−λ)_a f) ∘ ρ, hence R[g ∘ ρ](·; λ) = R[g](·; −λ) ∘ ρ. Since J is linear in
x and fixes v, D^λ commutes with J*, and Ric^H(J* g) = J* Ric^H(g) for every metric g, because Ric^H is built from g
and g0 alone and J is an isometry of g0. So R[J* g] = J* R[g]. Now g̃ = J* g(·, ρ(·); −λ), because λ^j (S g)_j =
(−λ)^j J* g_j ∘ ρ and J* g0 = g0; combining the two identities gives the formula. Expanding in λ gives the coefficients. (E1) is preserved because
J_* ℓ = ℓ; (E2) and the vanishing of each R^(m) because R^(m) ↦ (−1)^m J* R^(m) ∘ ρ; and J preserves each slice
and its flat L² norms.

(b) Under ϑ ↦ π/2 − ϑ, cos ϑ and sin ϑ exchange, ζ ↦ −ζ and h(−ζ) = h(ζ). Under θ ↦ 3π/2 − θ, sin θ ↦ −cos θ and
cos θ ↦ −sin θ. So F(JX, 3π/2 − θ) = −G(X, θ) and G(JX, 3π/2 − θ) = −F(X, θ), and from [[eq:waves-hopf]]

    p1(JX, 3π/2 − θ) = (2 sin²ϑ (−F) − cos²ϑ (−G))/3 = −p2(X, θ),    p2(JX, 3π/2 − θ) = −p1(X, θ).

Pulling back by J exchanges dξ1² and dξ2² and fixes dϑ², so (J* W_TT)(X, 3π/2 − θ) = 2 r^(1/2) λ⁻¹ (cos²ϑ (−p1)
dξ1² + sin²ϑ (−p2) dξ2² − (−p1 − p2) dϑ²) = −W_TT(X, θ). The two polarizations being a quarter turn apart is what makes
this work: with one quadrature alone (G = 0), F(JX, 3π/2 − θ) = −λ A env h cos θ is not −F(X, θ), and the identity
fails.

χ is the solution with zero data of the transport (ℓ + 3/(2r)) ∂_θ χ = f along ℓ, f the dv² second harmonic of
R^(0)[g0 + λ W_TT] ([[eq:chi-transport]]). By (a) at order 0 and the S-invariance of W_TT, f(JX, 3π/2 − θ) = f(X,
θ), as J* (dv ⊗ dv) = dv ⊗ dv. Put χ̃(X, θ) := −χ(JX, 3π/2 − θ). Then ∂_θ χ̃ = (∂_θ χ)(JX, 3π/2 − θ), the operator ℓ +
3/(2r) commutes with J, so χ̃ solves the same transport with the same zero data, and by uniqueness χ̃ = χ. Hence χ dv²
is S-invariant at weight 1, and so is W. By (a) applied to the S-invariant family g0 + λ W, its residual is S-odd at
order one: J* R^(1)[g0 + λ W](·, 3π/2 − ·) = −R^(1)[g0 + λ W], the mean part and the oscillating part alike.

(c) The unknowns of the ansatz [[eq:ansatz]] are the means m_j, the phases φ_j and the oscillating profiles ĝ_j,
with profile 𝒢(X, θ; λ) := g0 + Σ λ^j m_j + λ W + Σ λ^j ĝ_j(X, θ) and phase u = v + Σ λ^j φ_j. Let S act by

    m_j ↦ (−1)^j J* m_j,    φ_j ↦ (−1)^j J* φ_j,    ĝ_j ↦ (−1)^j J* ĝ_j(·, 3π/2 − ·).

The transformed phase is ũ(X; λ) = J* u(X; −λ), so λ⁻¹ dũ = −J*((−λ)⁻¹ du(−λ)), and the calculation of (a) with u in
place of v shows that the transformed unknowns solve the transformed stage equations. Every stage of
[[lem:stage-system]] and every choice of [[lem:stage-data]] (φ_m = 0 and (m_m)_(τ·) = 0 on Σ_τ0,
∂_θ ĝ_(m+1) given by an O(4)-equivariant right inverse, and the unique solutions of the linear problems there) is the
unique solution of a problem that S maps to itself. So each unknown is S-invariant, given that the earlier ones are:
the transformed unknowns solve the same problem and coincide with the originals by uniqueness. At j = 1 this is the
uniqueness of stage 1, whose unknowns (m1, φ1, ĝ2) solve a system that S maps to itself; it gives J* m1 = −m1 and,
through L0 φ1 = −½ m1(ℓ, ℓ) with zero data, J* φ1 = −φ1.

The rewriting with the fixed phase (in the proof of [[thm:approximant]]) commutes with S. There the profiles g_j are the
coefficients of 𝒢̂(X, θ; λ) := 𝒢(X, θ + φ1 + λΨ; λ), Ψ := Σ_(j≥2) λ^(j−2) φ_j. For the transformed unknowns φ̃1 = −J*
φ1 and λ Ψ̃(λ) = −J*((−λ) Ψ(−λ)), and their profile is 𝒢̃(X, θ′; λ) = J* 𝒢(X, 3π/2 − θ′; −λ), so their rewritten
profile is

    𝒢̃(X, θ + φ̃1 + λ Ψ̃(λ); λ) = J* 𝒢(X, 3π/2 − θ + φ1 + (−λ) Ψ(−λ); −λ) = J* 𝒢̂(X, 3π/2 − θ; −λ),

whose coefficient of λ^j is (−1)^j J* g_j(·, 3π/2 − ·) = (S g)_j. Hence S g = g. Taking the θ-mean, which the
reflection θ ↦ 3π/2 − θ preserves, gives J* ⟨g_j⟩ = (−1)^j ⟨g_j⟩, and ⟨g1⟩ = m1 since W has θ-mean zero. ∎

*Proof of [[prop:mean-mass]].* *Outside the shell.* The oscillating profiles (W, χ, the ĝ_m and the phase terms of the
fixed-phase rewriting) vanish outside v_start < v < v_end: each solves a transport along ℓ, at fixed v, whose forcing
and data are supported there ([[lem:stage-system]], and step (i) of the proof of [[lem:stage-data]]), the wave being
proportional to env. So for v outside that interval g_app = g0 + λ m1 + λ² E, with E bounded with its derivatives, and

    M[S_(v,r)](g_λ) = M[S_(v,r)](g0) + λ DM[m1] + O(λ²) + O(|w| + |∂w|),

with DM the derivative of M at g0 on S_(v,r). By [[lem:round-spheres]], M[S_(v,r)](g0) = μ(v). DM is linear, and
naturality with J fixing g0 and S_(v,r) gives DM[J* m] = DM[m]: as g0 + ε J* m = J*(g0 + ε m),

    M[S](g0 + ε J* m) = M[J(S)](g0 + ε m) = M[S](g0 + ε m).

By [[lem:quarter-turn]] (c), DM[m1] = DM[J* m1] = −DM[m1], so DM[m1] = 0. The remainder is at most C λ^(K−4) ≤ C λ² by
[[eq:remainder-pointwise]]. For v < v_start the means vanish too: their forcing terms and data on Σ_τ0 are supported in
v ≥ v_start, and v does not decrease along future causal curves of g0.

*Inside the shell.* By [[lem:sphere-two-scale]] (a)–(b) for g = g_app, θ^±, the area and g_app(n⁺, n⁻) are those of g0
up to O(λ): the wave enters at order λ⁰ only through the term ½ k^±(ℓ) ∂_θ tr_S g1 of the proof of that lemma, which
vanishes by [[eq:wave-traceless]]. So M[S_(v,r)](g_app) − μ(v) = O(λ), and the remainder contributes C(|w| + |∂w|) ≤
C λ^(K−4).

*Larger λ.* The two steps above hold for λ ≤ λ*, with λ* that of [[lem:sphere-two-scale]], taken so small that the
Taylor expansion about g0 applies. For λ* < λ ≤ λ0 the bounds hold with a larger C. Indeed |g_λ − g0| ≤ C λ ≤ ε1 and
|∂g_λ| ≤ C on Ω ([[thm:uniform-existence]], λ0 being so small that C λ0 ≤ ε1), and ε1 < 3/5. Each S_(v,r) lies in a
slice Σ_τ, on whose tangent space ker dτ the form g0 has least eigenvalue 1 relative to the Euclidean inner product
([[lem:eigen]]); so g_λ restricted to ker dτ has least eigenvalue at least 2/5, and the spheres are spacelike for g_λ.
The quantities R, θ^±, g(n⁺, n⁻) and Θ that make up M are continuous functions of (X, g, ∂g) on the compact set where
X ∈ Ω, |g − g0(X)| ≤ ε1 and |∂g| ≤ C, on which −g(n⁺, n⁻) > 0; so |M[S_(v,r)](g_λ)| ≤ C_M there, and for λ > λ*,
|M[S_(v,r)](g_λ) − μ(v)| ≤ C_M + μ(v_end) ≤ (C_M + μ(v_end)) λ*⁻² λ². ∎

The first mean m1 is driven by the following forcing. By [[lem:first-entry]], the coefficient of λ is ℛ^(1) =
T̂ ĝ2 − ½ e_2 ∂_θ² W + 𝒲(m1, φ1) + 𝒦_1. The term 𝒦_1 contains none of the unknowns of the stages, so it is the value of
ℛ^(1) with all of them set to zero, which is the coefficient R^(1) of λ in R[g0 + λ W]. The term −½ e_2 ∂_θ² W, which
contains m2 and φ2, is not part of 𝒦_1, but its θ-mean is zero: e_2 does not depend on θ ([[eq:eikonal-coefficients]]),
and ∂_θ² W has θ-mean zero. So the forcing of the mean equation of stage 1 ([[lem:stage-system]] (a)) is
𝒮_1 = −⟨𝒦_1⟩ = −⟨R^(1)⟩.

**Lemma {#lem:first-mean-forcing}** (The forcing of the first mean.) Let W = W_TT + χ dv ⊗ dv with χ a profile of zero
θ-mean, and let R^(1) be the coefficient of λ in the two-scale expansion of R[g0 + λ W] ([[def:two-scale]]). In the
coordinates (v, r, ϑ, ξ1, ξ2) of [[eq:vr-form]],

    ⟨R^(1)⟩ = −(4/9) A² env² h(ζ)² r⁻³ sin 2ϑ (dv ⊗ dϑ + dϑ ⊗ dv).                             {#eq:first-mean-forcing}

In particular ⟨R^(1)⟩ does not depend on χ.

*Proof.* Write v_a := ∂_a v, Ẇ := ∂_θ W and δg := λ[W], with indices raised by g0. Four facts are used. (W1) W(ℓ, ·) = 0
and tr W = 0 ([[lem:stage-zero]] (a)). (W2) As mixed tensors W and Ẇ commute, and ⟨W Ẇ⟩ = 0. The term χ dv ⊗ dv
contributes nothing to W^ρ_c Ẇ^c_σ or Ẇ^ρ_c W^c_σ, since ℓ^c Ẇ_cσ = 0 and W_TT^(ρc) v_c = 0. W_TT and Ẇ_TT are diagonal
in the coordinates (ϑ, ξ1, ξ2), on which g0 is diagonal, so W Ẇ = ½ ∂_θ (W_TT W_TT). (W3) ⟨W⟩ = 0, since W_TT is a first
harmonic in θ and χ has zero mean. (W4) In the coordinates of [[eq:vr-form]], with f = 1 − μ/r² and ℓ = ∂_r, the
Christoffel symbols of g0 give ∇̂_v ℓ^r = −μ/r³, ∇̂_A ℓ^B = r⁻¹ δ^B_A for angular A, B, and ∇̂_a ℓ^c = 0 otherwise; so
∇̂_ℓ ℓ = 0. Since g0^(vc) = δ^c_r, the Hessian of v is ∇̂_a v_b = −Γ^v_ab = ½ ∂_r g0_ab, that is −(μ/r³) dv² + r γ, with
γ the round metric; so ∇̂_ℓ v = 0.

*The expansion.* As in the proof of [[lem:mean-leading]], with C := Γ[g] − Γ[g0], Ric(g) = Ric(g0) + ∇̂_ρ C^ρ_ab − ∇̂_b
C^ρ_aρ + C^ρ_ρσ C^σ_ab − C^ρ_bσ C^σ_aρ, C^ρ_ab = ½ g^(ρσ)(∇̂_a δg_bσ + ∇̂_b δg_aσ − ∇̂_σ δg_ab) and D^ρ = g^(ab) C^ρ_ab.
With ∇̂_a [u] = λ⁻¹ v_a [∂_θ u] + [∇̂_a u] and g⁻¹ = g0⁻¹ − λ W^♯ + O(λ²), C = [C⁽⁰⁾] + λ [C⁽¹⁾] + O(λ²), where C⁽⁰⁾ρ_ab
= ½(v_a Ẇ_b^ρ + v_b Ẇ_a^ρ − ℓ^ρ Ẇ_ab) and

    C⁽¹⁾ρ_ab = G^ρ_ab − ½ (v_a (WẆ)^ρ_b + v_b (WẆ)^ρ_a),      G^ρ_ab := ½ (∇̂_a W_b^ρ + ∇̂_b W_a^ρ − ∇̂^ρ W_ab);

the second term comes from −λ W^(ρσ) acting on C⁽⁰⁾, whose term in v_σ drops since W^(ρσ) v_σ = 0. By (W1),
C⁽⁰⁾ρ_ρb = 0, v_ρ C⁽⁰⁾ρ_ab = 0 and g0^(ab) C⁽⁰⁾ρ_ab = 0. By (W2) and (W3), ⟨C⁽¹⁾⟩ = 0.

*The Ricci part.* At order λ the derivative terms give λ⁻¹ v_ρ [∂_θ C⁽²⁾] and ∇̂ C⁽¹⁾, both of θ-mean zero. The products
give C⁽⁰⁾ C⁽¹⁾ + C⁽¹⁾ C⁽⁰⁾. In C^ρ_ρσ C^σ_ab the cross terms are C⁽⁰⁾ρ_ρσ C⁽¹⁾σ_ab, zero since C⁽⁰⁾ρ_ρσ = 0, and
C⁽¹⁾ρ_ρσ C⁽⁰⁾σ_ab. For the second, the trace of C⁽¹⁾ is C⁽¹⁾ρ_ρσ = −½ v_σ tr(WẆ), the trace C_1^c_ac = −½ v_a W·∂W
of [[lem:leading-coefficient]]: the G-part has trace G^ρ_ρσ = ½ ∂_σ tr W = 0, and v_ρ (WẆ)^ρ_σ = 0 by W(ℓ, ·) = 0. So
C⁽¹⁾ρ_ρσ C⁽⁰⁾σ_ab = −½ tr(WẆ) v_σ C⁽⁰⁾σ_ab = 0, as v_σ C⁽⁰⁾σ_ab = 0. In C^ρ_bσ C^σ_aρ the two cross terms are
transposes in (a, b). So the mean of the Ricci part is −2 times the symmetric part
of ⟨T⟩, T_ab := C⁽⁰⁾ρ_bσ C⁽¹⁾σ_aρ. By (W1), Ẇ^ρ_σ v_ρ = 0, (WẆ)^σ_ρ ℓ^ρ = 0 and v·ℓ = 0, so

    Ẇ^ρ_σ C⁽¹⁾σ_aρ = ½ Ẇ^(ρσ) ∇̂_a W_ρσ − ½ v_a tr(ẆWẆ),
    v_σ C⁽¹⁾σ_aρ = −½ (W_ρσ ∇̂_a ℓ^σ + W_aσ ∇̂_ρ ℓ^σ + (∇̂_ℓ W)_aρ),
    ℓ^ρ C⁽¹⁾σ_aρ = ½ (−W_ρ^σ ∇̂_a ℓ^ρ + (∇̂_ℓ W)_a^σ + W_aρ ∇̂^σ ℓ^ρ).

In the first line the terms of G with ∇̂_ρ and ∇̂^σ cancel by the symmetry of Ẇ^(ρσ); the others use W(ℓ, ·) = 0.
Inserting these into T_ab = ½ v_b Ẇ^ρ_σ C⁽¹⁾σ_aρ + ½ Ẇ^ρ_b v_σ C⁽¹⁾σ_aρ − ½ Ẇ_bσ ℓ^ρ C⁽¹⁾σ_aρ, the two terms with ∇̂_a ℓ
cancel (both are (ẆW)_bσ ∇̂_a ℓ^σ), and

    T_ab = ¼ v_b Ẇ^(ρσ) ∇̂_a W_ρσ − ¼ v_a v_b tr(ẆWẆ) − ½ Ẇ^ρ_b (∇̂_ℓ W)_aρ − ½ Ẇ^ρ_b W_aσ ∇̂_ρ ℓ^σ.

The terms with χ in the last two vanish: Ẇ^ρ_b with χ̇ ℓ^ρ v_b meets (∇̂_ℓ W)(ℓ, ·) = −W(∇̂_ℓ ℓ, ·) = 0 and ℓ^ρ ∇̂_ρ ℓ =
0; W_aσ = χ v_a v_σ meets v_σ ∇̂_ρ ℓ^σ = −(∇̂_ρ v)(ℓ) = 0 by (W4); and ∇̂_ℓ (χ v ⊗ v) = (ℓχ) v ⊗ v by (W4), which Ẇ_TT
annihilates. For W_TT, (∇̂_ℓ W_TT)_AB = ∂_r W_AB − (2/r) W_AB = −(3/(2r)) W_AB ([[eq:transport-angular]], W_TT being
r^(1/2) times a function of (v, ϑ, θ)), and ∇̂_ρ ℓ^σ = r⁻¹ δ^σ_ρ on angular indices, so the last two terms are multiples
of (ẆW)_ba, of θ-mean zero by (W2). The term tr(ẆWẆ) involves W_TT only and is cubic in a first harmonic, so its mean
is zero. Hence the Ricci part has mean −¼ (v_a X_b + v_b X_a), with X_a := ⟨Ẇ^(ρσ) ∇̂_a W_ρσ⟩.

*The gauge part.* D⁽⁰⁾ = g0^(ab) C⁽⁰⁾ = 0, and D⁽¹⁾ = g0^(ab) C⁽¹⁾ρ_ab − W^(ab) C⁽⁰⁾ρ_ab = (div W)^ρ + ½ ℓ^ρ W^(ab) Ẇ_ab,
with (div W)^ρ := g0^(ab) ∇̂_a W_b^ρ, by tr W = 0 and W^(ab) v_a = 0. The coefficient of λ in −½(g_aρ ∇̂_b D^ρ + g_bρ
∇̂_a D^ρ) is −½ times the symmetrization of g0_aρ (v_b ∂_θ D⁽²⁾ρ + ∇̂_b D⁽¹⁾ρ) + W_aρ v_b ∂_θ D⁽¹⁾ρ. The first two terms
have mean zero, as ⟨D⁽¹⁾⟩ = 0 by (W2) and (W3). In the third, W_aρ ℓ^ρ = 0 removes the ℓ-part of D⁽¹⁾. For W = χ v ⊗ v,
v_ρ (div Ẇ)^ρ = −Ẇ^(ab) ∇̂_a v_b = −r Ẇ_TT^(AB) γ_AB = −r⁻¹ tr_S Ẇ_TT = 0 by (W4), the χ̇-part dropping since (∇̂ v)(ℓ,
ℓ) = 0; and the χ̇-part of div Ẇ is (ℓχ̇ + χ̇ □_(g0) v) ℓ, which W_TT annihilates. So the gauge part has mean −½ (v_a V_b
+ v_b V_a), with V_a := ⟨(W_TT)_aρ (div Ẇ_TT)^ρ⟩. Altogether

    ⟨R^(1)⟩_ab = −¼ (v_a X_b + v_b X_a) − ½ (v_a V_b + v_b V_a).

*The evaluation.* By [[eq:waves-hopf]], W_TT = r^(1/2) ω with ω := −2P dϑ² + 2 cos²ϑ Q1 dξ1² + 2 sin²ϑ Q2 dξ2², where
Q_i := λ⁻¹ p_i and P := Q1 + Q2 are functions of (v, ϑ, θ). In X_a the Christoffel terms pair Ẇ^(ρσ) with W_cσ and have
mean zero by (W2), and the χ-terms vanish by (W1); so X_a = ⟨Ẇ^(ρσ) ∂_a W_ρσ⟩ = r⁻³ ⟨ω̇ · ∂_a ω⟩ for a = v, ϑ, with ·
the contraction by γ; X_r = (2r)⁻¹ ⟨Ẇ^(ρσ) W_ρσ⟩ = 0, and X_ξ1 = X_ξ2 = 0. Since ω = env · ω̃ with ω̃ independent of v,
ω̇ · ∂_v ω = ½ env env′ ∂_θ (ω̃ · ω̃), so X_v = 0. For angular c, the (v, r)-block contributes nothing to (div Ẇ_TT)_c
(Γ^D_vr = Γ^D_rr = 0, and Ẇ_TT has no v or r component), so (div Ẇ_TT)_c = r⁻² (div_γ Ẇ_TT)_c = r^(−3/2) (div_γ ω̇)_c,
div_γ the divergence on the unit S³; and V_a = r⁻³ ⟨ω_a^c (div_γ ω̇)_c⟩ for angular a, zero otherwise. ω does not depend
on ξ1, ξ2 and is diagonal, so (div_γ ω̇)_ξ1 = (div_γ ω̇)_ξ2 = 0. Every component therefore vanishes except
⟨R^(1)⟩_vϑ = −¼ X_ϑ − ½ V_ϑ.

Write c := cos ϑ, s := sin ϑ and κ_A := A env/3. By [[eq:waves-hopf]] each of Q1, Q2, P has the form
κ_A h (α cos θ + β sin θ), with (α, β) = (2c², −s²), (−c², 2s²) and (c², s²) respectively. For two such functions Q and Q′, the second with
coefficients (α′, β′), the terms with ∂_ϑ h cancel and

    ⟨∂_θ Q ∂_ϑ Q⟩ = ½ κ_A² h² (β ∂_ϑ α − α ∂_ϑ β),      ⟨Q ∂_θ Q′⟩ = ½ κ_A² h² (α β′ − β α′).

This gives ⟨∂_θ P ∂_ϑ P⟩ = −κ_A² h² c s, ⟨∂_θ Q_i ∂_ϑ Q_i⟩ = 2 κ_A² h² c s (i = 1, 2), ⟨P ∂_θ Q1⟩ = −(3/2) κ_A² h² c² s²
and ⟨P ∂_θ Q2⟩ = (3/2) κ_A² h² c² s². Now ω̇ · ∂_ϑ ω = 4 (∂_θ P ∂_ϑ P + ∂_θ Q1 ∂_ϑ Q1 + ∂_θ Q2 ∂_ϑ Q2) plus multiples of
Q_i ∂_θ Q_i, which have mean zero; so X_ϑ = 4 r⁻³ κ_A² h² c s (−1 + 2 + 2) = 12 κ_A² h² c s/r³. The divergence of a diagonal
tensor depending on ϑ alone is (div_γ T)_ϑ = (cs)⁻¹ ∂_ϑ(cs T_ϑϑ) − ½ (∂_ϑ γ_AB) T^(AB), which gives

    (div_γ ω̇)_ϑ = −2 ∂_ϑ ∂_θ P + (4 s/c − 2 c/s) ∂_θ Q1 + (2 s/c − 4 c/s) ∂_θ Q2.

With ω_ϑ^ϑ = −2P and ⟨P ∂_ϑ ∂_θ P⟩ = −⟨∂_θ P ∂_ϑ P⟩ = κ_A² h² c s,

    V_ϑ = r⁻³ (4 κ_A² h² c s + 3 κ_A² h² c² s² ((4 s/c − 2 c/s) − (2 s/c − 4 c/s))) = r⁻³ κ_A² h² (4 c s + 6 c s)
        = 10 κ_A² h² c s/r³.

So ⟨R^(1)⟩_vϑ = −(3 + 5) κ_A² h² c s/r³ = −(8/9) A² env² h² c s/r³ = −(4/9) A² env² h² sin 2ϑ/r³. ∎

**Remark {#rem:mean-mass-aspect}** (What the mass sees.) By [[lem:first-mean-forcing]] the forcing −⟨R^(1)⟩ of the
mean equation of stage 1 is nonzero wherever env ≠ 0 off the axes, and it lies in the dv dϑ component. The phase φ1 and
the oscillating profile ĝ2 also enter that equation, ĝ2 through the mean of a product with ∂_θ W, so the forcing alone
does not decide whether m1 vanishes; nothing in the structure of the stage forces m1 = 0, and [[prop:mean-mass]] does
not need to know whether it does, since it uses only J* m1 = −m1. The forcing term is odd under the quarter turn, as
[[lem:quarter-turn]] requires (J fixes dv and h(ζ)², maps sin 2ϑ to itself and dϑ to −dϑ), and a rotation-invariant
mass cannot see such a term. The quantity of [[prop:mean-mass]] is the
Hawking mass of the spheres S_(v,r) of the domain. It is not the angular mean of the mass aspect at past null infinity,
which is a different quantity, governed by the mass law of [[thm:bondi-law]].
