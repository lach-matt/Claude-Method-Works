# Part. The horizon, the construction from past null infinity and the mass law {#part:remaining}

## The boundary, the spheres' horizon and the mean mass {#ch:horizon-mass}

This chapter proves the three propositions of [[thm:main]] that concern the geometry of the solutions g_λ: the
curvature boundary x_K = 1 is spacelike ([[prop:boundary-spacelike]]), the outgoing expansion of the round spheres
has exactly one zero on each column, close to √μ ([[prop:one-zero]]), and the Hawking mass of every round sphere is
μ(v) up to O(λ²) outside the shell ([[prop:mean-mass]]). Items 6 and 7 of [[thm:main]] are the last two.

### Notation and the facts used {#sec:horizon-notation}

Throughout, K ≥ 6, 0 < λ ≤ λ0, g_λ is the solution of [[thm:main]] on Ω, g_app = g0 + λ[g1] + Σ_(j=2)^N λ^j [g_j] is
its approximant ([[thm:approximant]]) and w := g_λ − g_app. The profiles and the bracket [f](X) := f(X, v(X)/λ) are
those of [[pending:def-profiles]]. Step 1 of the proof of [[thm:uniform-existence]] gives, with M the constant of that
theorem,

    ‖∂^i w‖_∞ ≤ C M λ^(K−3−i),   i ≤ 4,   on Ω.                                                 {#eq:remainder-pointwise}

The first profile is g1 = m1 + W(X, θ + φ1(X)), where the mean m1 and the phase φ1 do not depend on θ, and
W = W_TT + χ dv², with W_TT the wave of [[pending:eq-waves]] and χ its second harmonic ([[pending:stage-zero]]). We use
two properties of W from there: W(ℓ, ·) = 0, and W_TT has no dτ, dr or dv component.

On R⁴ we use r = |x|, and on S³ the angles (ϑ, ξ1, ξ2) given by x1 + i x2 = r cos ϑ e^(iξ1), x3 + i x4 = r sin ϑ e^(iξ2),
0 ≤ ϑ ≤ π/2. The round metric of S³ is dϑ² + cos²ϑ dξ1² + sin²ϑ dξ2², and ζ := cos 2ϑ. We write ξ1, ξ2 for the two
azimuths because φ1 is the first phase. In this chart

    g0 = −dτ² + dr² + r² (dϑ² + cos²ϑ dξ1² + sin²ϑ dξ2²) + (μ(v)/r²)(dτ + dr)²,

which is block diagonal between the (τ, r) plane and the sphere, and the wave of [[pending:eq-waves]] reads

    λ W_TT = 2 r^(1/2) (cos²ϑ p1 dξ1² + sin²ϑ p2 dξ2² − (p1 + p2) dϑ²),
    p1 := (2 cos²ϑ G − sin²ϑ F)/3,   p2 := (2 sin²ϑ F − cos²ϑ G)/3,                                   {#eq:waves-hopf}

with F := λ A env(v) h(ζ) sin θ, G := λ A env(v) h(ζ) cos θ and h(ζ) := √(2/(1 + ζ²)), at the phase θ.

For a sphere S_(v,r) := {τ = v − r, |x| = r} we write tr_S f := γ0^(AB) f_AB for the trace on S_(v,r), with γ0 the
metric g0 induces there, r² times the round metric. The covectors dτ and dr vanish on the tangent spaces of S_(v,r),
and so does dv = dτ + dr. Two consequences for W follow at once from [[eq:waves-hopf]]:

    tr_S W = 0   on every S_(v,r) and at every phase.                                                {#eq:wave-traceless}

Indeed χ dv² vanishes on tangent vectors of the sphere, and tr_S W_TT = r⁻² · 2 r^(1/2) λ⁻¹ (cos²ϑ p1/cos²ϑ + sin²ϑ
p2/sin²ϑ − (p1 + p2)) = 0.

A *column* is the set of points of D_T ∩ {τ ≥ τ0} with v and the angle ω ∈ S³ fixed and r varying. Its points are
(τ, x) = (v − r, r ω), so d/dr along a column is −∂_τ + ω·∂_x = ℓ, and a column is an integral curve of ℓ. Since
ℓ(v) = 0, the derivative along a column of a bracket is

    (d/dr) [f] = [ℓ f],                                                                           {#eq:column-derivative}

with ℓ acting on X only: no factor λ⁻¹ appears. A column lies in {r_q(v) ≤ r ≤ v − τ0}.

### The boundary {#sec:boundary}

*Proof of [[prop:boundary-spacelike]].* Write m := μ/r². By [[pending:prop-vaidya-contractions]],
g0⁻¹(dr, dr) = 1 − m, g0⁻¹(dr, dτ) = m and g0⁻¹(dτ, dτ) = −1 − m; since dv = dτ + dr, also g0⁻¹(dv, dv) = 0,
g0⁻¹(dv, dr) = 1 and g0⁻¹(dv, dτ) = −1. On x_K = 1 put Φ := r − r_q(v), r_q = (√72 μ l5²)^(1/4). Then
dΦ = dr − r_q′ dv with r_q′ = r_q μ′/(4μ), and

    g0⁻¹(dΦ, dΦ) = g0⁻¹(dr, dr) − 2 r_q′ g0⁻¹(dr, dv) + r_q′² g0⁻¹(dv, dv) = 1 − m − 2 r_q′.

At r = r_q, m = μ/r_q² = μ/(√72 μ l5²)^(1/2) = √(μ/(√72 l5²)), and 2 r_q′ = r_q μ′/(2μ). This is the formula of
[[prop:boundary-spacelike]].

*Sign.* μ is nondecreasing, so μ′ ≥ 0, and μ ≥ μ0 ≥ √72 l5². The second term is therefore at most −1 and the third at
most 0. Where μ > √72 l5² the second term is below −1; where μ′ > 0 the third is negative. At such points dΦ is
timelike for g0, which is to say that the hypersurface {Φ = 0} is spacelike.

*Time orientation.* g0⁻¹(dΦ, dτ) = g0⁻¹(dr, dτ) − r_q′ g0⁻¹(dv, dτ) = m + r_q′ > 0. The covector dτ is timelike and
positive on future causal vectors ([[pending:lem-domain]], (a)). Where dΦ is timelike too, the two have positive
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

*The margin.* If μ0 > √72 l5², then 1 − √(μ/(√72 l5²)) ≤ 1 − √(μ0/(√72 l5²)) = −δ and the third term is at most 0,
so g0⁻¹(dΦ, dΦ) ≤ −δ on the whole boundary. By item 4 of [[thm:main]], |g_λ − g0| ≤ C λ on Ω; since g0⁻¹ is bounded on
the compact Ω and inversion is smooth, |g_λ⁻¹ − g0⁻¹| ≤ C1 λ. The covector dΦ = dr − r_q′ dv is bounded on Ω, so

    g_λ⁻¹(dΦ, dΦ) ≤ g0⁻¹(dΦ, dΦ) + C λ ≤ −δ + C λ ≤ −δ/2      once C λ ≤ δ/2.

Moreover g_λ⁻¹(dΦ, dτ) ≥ m + r_q′ − C λ, and m ≥ μ0/r² is bounded below on Ω, so g_λ⁻¹(dΦ, dτ) > 0 for λ small;
since dτ is timelike for g_λ and positive on its future causal vectors ([[pending:lem-domain]], (e)), the argument of
the time orientation and of the no return applies to g_λ verbatim.

*Equality.* If μ0 = √72 l5², then on {v ≤ inf supp env} μ = μ0 and μ′ = 0, so the formula gives g0⁻¹(dΦ, dΦ) = 0,
and r_q = (√72 μ0 l5²)^(1/4) = (μ0²)^(1/4) = √μ0: the boundary is the seed's horizon r = √μ0, null for g0. That g_λ
equals g0 on that region, so that the boundary is null for g_λ there, and that after the shell starts the boundary is
spacelike for g_λ outside a layer whose width tends to 0 with λ, are proved in [[pending:equality-seed-and-boundary]];
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
∂_τ + β ∂_r is null when −1 + m + 2 m β + (1 + m) β² = 0, whose roots are β = (1 − m)/(1 + m) and β = −1. The second
gives L0, which is future directed with L0(τ) = 1 and points inward; the first gives n⁺. Each has n(τ) = 1 > 0 and τ is a
time function, so both are future directed.

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

    G = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j]

with profiles g_j bounded on Ω × S¹ with all their (X, θ)-derivatives, independently of λ, and with g1 = m1 + W(X, θ +
φ1(X)), where m1 and φ1 do not depend on θ, W(ℓ, ·) = 0, and tr_S W = 0 on every S_(v,r) at every phase. There are
λ* > 0 and C such that for 0 < λ ≤ λ* the following holds on every sphere S_(v,r) in Ω.

(a) The future null expansions of S_(v,r) for G, with normals normalized by n(τ) = 1, are

    θ^±(G) = θ^±(g0) + λ [Θ^±_1] + λ² E^±,                                                         {#eq:theta-two-scale}

with profiles Θ^±_1 and functions E^± = e^±(X, v/λ, λ), where e^± is smooth in (X, θ, λ) and bounded with all its
X-derivatives, uniformly in λ ≤ λ*. No term of order λ⁻² or λ⁻¹ occurs, and none of order λ⁰ beyond g0's.

(b) The area element of S_(v,r), the inner product G(n⁺, n⁻) and the normals have expansions of the same form.

(c) Along a column, (d/dr)(θ^±(G) − θ^±(g0)) = O(λ), and the same holds for the quantities of (b).

*Proof.* The normal plane of S_(v,r) is spanned by dτ and dr at every point with r > 0, the axes included. For G near
g0 let k^± := c^±(G)(dr + α^±(G) dτ) be its two null covectors in that plane, with n^± := G⁻¹ k^± normalized by
n^±(τ) = 1; for G near g0 the two null directions stay distinct, so c^±, α^± are smooth functions of (X, G). Let
Π_G^(ab) be the inverse of the metric G induces on the sphere, pushed forward:

    Π_G = G⁻¹ + (n⁺ ⊗ n⁻ + n⁻ ⊗ n⁺)/(−G(n⁺, n⁻)),

smooth in (X, G); it annihilates k⁺ and k⁻, hence every covector of the normal plane. The second fundamental form along n^± is −k^±_c Γ[G]^c_(ab) on tangent vectors, so

    θ^±(G) = −Π_G^(ab) Γ[G]^c_(ab) k^±_c,     Γ[G]^c_(ab) = ½ G^(cd) (∂_a G_db + ∂_b G_da − ∂_d G_ab),

in Cartesian coordinates: a smooth function of (X, G) times ∂G, affine in ∂G.

Let ĝ(X, θ; λ) := g0 + λ g1 + Σ_(j≥2) λ^j g_j be the profile of G, so G = [ĝ]. By the chain rule of
[[pending:def-profiles]], ∂_a G = λ⁻¹ (∂_a v) [∂_θ ĝ] + [∂_a ĝ]. In Γ_(dab) the fast parts of ∂_a G_db and ∂_b G_da
carry the factor ∂_a v or ∂_b v, and Π_G^(ab) ∂_a v = 0 because dv lies in the normal plane. Only the fast part of
−½ ∂_d G_ab survives, and it contributes ½ λ⁻¹ k^±_c G^(cd) ∂_d v Π_G^(ab) [∂_θ ĝ_ab] = ½ λ⁻¹ k^±(ℓ_G) Π_G^(ab)
[∂_θ ĝ_ab], with ℓ_G := G⁻¹ dv. Hence θ^±(G) = f^±(X, v/λ, λ) with

    f^±(X, θ, λ) := Θ^±_slow(X, ĝ, ∂_X ĝ) + ½ k^±(ℓ_ĝ) Π_ĝ^(ab) (∂_θ g1 + λ ∂_θ g2 + λ² ∂_θ g3 + …)_ab,

where Θ^±_slow is the formula above with ∂G replaced by ∂_X ĝ, and we used ∂_θ ĝ = λ ∂_θ g1 + λ² ∂_θ g2 + …, which
cancels the factor λ⁻¹. The function f^± is smooth in (X, θ, λ) for λ ≤ λ*, λ* small enough that ĝ stays near g0, and
it is bounded with all its X- and θ-derivatives. At λ = 0, ĝ = g0 and ∂_X ĝ = ∂g0, so the first term is θ^±(g0) and the
second is ½ k^±_0(ℓ) γ0^(AB) ∂_θ (g1)_AB = ½ k^±_0(ℓ) ∂_θ tr_S g1. Now tr_S g1 = tr_S m1 + tr_S W(X, θ + φ1), the first
independent of θ and the second zero by hypothesis, so this term vanishes and f^±(X, θ, 0) = θ^±(g0). Taylor's formula
in λ with integral remainder gives f^± = θ^±(g0) + λ Θ^±_1 + λ² e^± with Θ^±_1 := ∂_λ f^±(·, ·, 0) and e^± of the stated
kind. This is (a).

The area element, G(n⁺, n⁻) and n^± are smooth functions of (X, G) alone, with no derivative of G, so the same Taylor
argument applies with no fast term at all: (b). For (c), along a column v is constant, so by [[eq:column-derivative]]
the derivative of f(X, v/λ, λ) along it is (ℓ_X f)(X, v/λ, λ), bounded with no factor λ⁻¹; applied to λ Θ^±_1 + λ² e^±
it is O(λ). ∎

The first profile of g_app satisfies the hypotheses of [[lem:sphere-two-scale]]: W(ℓ, ·) = 0, and tr_S W = 0 by
[[eq:wave-traceless]]. The remaining profiles are bounded with their derivatives by [[thm:approximant]].

*Proof of [[prop:one-zero]].* Let λ ≤ λ0 and write θ⁺_λ := θ⁺(g_λ).

(i) The expansion as a function of the metric. As in the proof of [[lem:sphere-two-scale]], θ⁺(G) is a smooth function
of (X, G) times ∂G, affine in ∂G, and it is estimated in the Cartesian arrays, in which the axes are regular points.

(ii) The background. By [[lem:round-spheres]], θ⁺(g0) = 3(r² − μ)/(r(r² + μ)). Since S_(v,r) lies in {v = const}, μ =
μ(v) enters only algebraically. Its one zero on (0, ∞) is r = √μ, simple, with ∂_r θ⁺(g0) = 3/μ there. The ingoing
expansion is −3/r < 0.

(iii) The approximant. By [[lem:sphere-two-scale]] applied to G = g_app, θ⁺(g_app) = θ⁺(g0) + λ [Θ⁺_1] + λ² E⁺, and
along every column

    |θ⁺(g_app) − θ⁺(g0)| + |(d/dr)(θ⁺(g_app) − θ⁺(g0))| ≤ C λ.

(iv) The remainder. Since θ⁺ is smooth in G and affine in ∂G, |θ⁺(g_λ) − θ⁺(g_app)| ≤ C (|w| + |∂w|). Its derivative
along a column is at most C (|w| + |∂w| + |∂²w|): the derivative falls on w, on ∂w, or on the coefficients through
g_app and ∂g_app, and ℓ ∂g_app = dv ⊗ [ℓ ∂_θ g1] + O(1) is bounded because ℓ(v) = 0. By [[eq:remainder-pointwise]]
both are at most C M λ^(K−5) ≤ C λ, as K ≥ 6. With (iii), along every column

    |θ⁺_λ − θ⁺(g0)| + |(d/dr)(θ⁺_λ − θ⁺(g0))| ≤ C3 λ.                                              {#eq:theta-plus-close}

(v) The zero. The columns lie in the compact Ω, and r ≥ r_q(v) ≥ q0 > 0 on them. The difference
√μ − r_q = μ^(1/2) − c μ^(1/4), c := (√72 l5²)^(1/4), equals μ^(1/4)(μ^(1/4) − c) and has derivative
¼ μ^(−3/4)(2 μ^(1/4) − c) in μ, which is positive for μ > c⁴/16 = √72 l5²/16, in particular for μ ≥ μ0 ≥ √72 l5².
So √μ(v) − r_q(v) is at least its value at μ0, which is positive when μ0 > √72 l5². Put μ_max := μ(v_end). Fix δ in
(0, that value) such that ∂_r θ⁺(g0) ≥ 3/(2 μ_max) on |r − √μ(v)| ≤ δ (possible by continuity, since ∂_r θ⁺(g0) = 3/μ ≥
3/μ_max at r = √μ), and let m_δ > 0 be the minimum of |θ⁺(g0)| on the compact rest of the columns. Let λ_H ≤ λ0 be
such that C3 λ_H < min(m_δ, 3/(4 μ_max)) and λ_H ≤ λ*. For λ ≤ λ_H, by [[eq:theta-plus-close]], θ⁺_λ has no zero
where |r − √μ| > δ, and on |r − √μ| ≤ δ its r-derivative is at least 3/(2 μ_max) − C3 λ > 3/(4 μ_max), so it is strictly
increasing there. Hence it has at most one zero on each column, positive above it and negative below it.

If the column contains [√μ − δ, √μ + δ], which holds when √μ(v) ≤ v − τ0 − δ1 with δ1 := δ, then θ⁺_λ changes sign on
that interval (|θ⁺_λ(√μ)| ≤ C3 λ and the slope exceeds 3/(4 μ_max)), so it has exactly one zero R_λ, and

    |R_λ − √μ(v)| ≤ C′ λ,     C′ := C3/(3/(4 μ_max)).

Put C := 2 C′. On the band, for r ≤ √μ − C λ,

    θ⁺_λ(r) ≤ θ⁺_λ(√μ) − (3/(4 μ_max)) (√μ − r) ≤ C3 λ − 2 C3 λ < 0,

and likewise θ⁺_λ(r) ≥ C3 λ > 0 for r ≥ √μ + C λ. At distance C′ λ these bounds give only θ⁺_λ ≤ 0 and θ⁺_λ ≥ 0,
which is why C is taken to be twice C′. Off the band θ⁺_λ has the sign of θ⁺(g0). The ingoing expansion is
θ⁻(g_λ) = −3/r + O(λ) < 0 everywhere, by [[lem:sphere-two-scale]] (a) for g_app and the bound C (|w| + |∂w|) for the
remainder. So the spheres with r ≤ √μ − C λ are trapped, both future null expansions being negative at every point,
and those with r ≥ √μ + C λ are untrapped.

If μ0 = √72 l5², fix instead δ in (0, √μ_max − r_q(μ_max)) with the same band property. The argument for the zero and
the signs runs on the columns where √μ − r_q ≥ δ; by the monotonicity in μ shown above, this is μ(v) ≥ μ0 + δ2 for some
δ2 > 0. The first assertion uses only the monotonicity band and the absence of zeros off it, and holds on every column. ∎

**Remark {#rem:round-family}** (The round family.) The zero set of θ⁺_λ on the columns is not a marginally trapped
surface: the statement concerns the round family {S_(v,r)}. Although ∂g_λ converges only weakly, the expansion of these
spheres does not see the oscillation at leading order, because the wave is traceless on them
([[eq:wave-traceless]]) and the phase v/λ is constant along each column ([[eq:column-derivative]]). The agreement of
this statement with an evolution of the same free data in Bondi-type variables, the departure of the horizon from √μ
halving with λ, is [[pending:computational-1]].

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

**Lemma {#lem:quarter-turn}** (The quarter-turn symmetry.) (a) For every family of profiles with G = g0 + Σ_j λ^j g_j,
the family G̃ := g0 + Σ_j λ^j (S g)_j has two-scale residual R[G̃](X, θ; λ) = J* R[G](X, 3π/2 − θ; −λ). Its
coefficient of λ^m is (−1)^m J* R^(m)(·, 3π/2 − ·), so S preserves (E1)–(E3) of [[thm:uniform-existence]] at every
order: it preserves (E1), (E2) and the vanishing of each coefficient R^(m).

(b) The stage-0 wave is S-invariant: (J* W_TT)(X, 3π/2 − θ) = −W_TT(X, θ); so is χ, and so is W = W_TT + χ dv² at
weight 1.

(c) The profiles of the approximant of [[thm:approximant]], with the stage data of [[pending:lem-stage-data]], satisfy
S g = g:

    (J* g_j)(·, 3π/2 − ·) = (−1)^j g_j,   and for the means,   J* ⟨g_j⟩ = (−1)^j ⟨g_j⟩;   in particular J* m1 = −m1.

*Proof.* (a) The operator R[G] is Ric^H of [[pending:eq-reduced]] with every ∂_a replaced by D^λ_a := ∂_a + λ⁻¹
(∂_a v) ∂_θ ([[pending:eq-two-scale]]), and it contains no explicit θ. Let ρ(θ) := 3π/2 − θ. Since ∂_θ (f ∘ ρ) =
−(∂_θ f) ∘ ρ, we have D^λ_a (f ∘ ρ) = (D^(−λ)_a f) ∘ ρ, hence R[G ∘ ρ](·; λ) = R[G](·; −λ) ∘ ρ. Since J is linear in
x and fixes v, D^λ commutes with J*, and Ric^H(J* g) = J* Ric^H(g) because Ric^H is built from g and g0 alone and J is
an isometry of g0. So R[J* G] = J* R[G]. Now G̃ = J* G(·, ρ(·); −λ), because λ^j (S g)_j = (−λ)^j J* g_j ∘ ρ and J* g0 =
g0; combining the two identities gives the formula. Expanding in λ gives the coefficients. (E1) is preserved because
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
R^(0)[g0 + λ W_TT] ([[pending:stage-zero]]). By (a) at order 0 and the S-invariance of W_TT, f(JX, 3π/2 − θ) = f(X,
θ), as J* (dv ⊗ dv) = dv ⊗ dv. Put χ̃(X, θ) := −χ(JX, 3π/2 − θ). Then ∂_θ χ̃ = (∂_θ χ)(JX, 3π/2 − θ), the operator ℓ +
3/(2r) commutes with J, so χ̃ solves the same transport with the same zero data, and by uniqueness χ̃ = χ. Hence χ dv²
is S-invariant at weight 1, and so is W.

(c) The unknowns of the ansatz ([[pending:ansatz]]) are the means m_j, the phases φ_j and the oscillating profiles ĝ_j,
with G(X, θ; λ) = g0 + Σ λ^j m_j + λ W + Σ λ^j ĝ_j(X, θ) and phase u = v + Σ λ^j φ_j. Let S act by

    m_j ↦ (−1)^j J* m_j,    φ_j ↦ (−1)^j J* φ_j,    ĝ_j ↦ (−1)^j J* ĝ_j(·, 3π/2 − ·).

The transformed phase is ũ(X; λ) = J* u(X; −λ), so λ⁻¹ dũ = −J*((−λ)⁻¹ du(−λ)), and the calculation of (a) with u in
place of v shows that the transformed unknowns solve the transformed stage equations. Every stage of
[[pending:lem-stage-system]] and every choice of [[pending:lem-stage-data]] (φ_m = 0 and (m_m)_(τ·) = 0 on Σ_τ0,
∂_θ ĝ_(m+1) given by an O(4)-equivariant right inverse, and the unique solutions of the linear problems there) is the
unique solution of a problem that S maps to itself. So each unknown is S-invariant, given that the earlier ones are:
the transformed unknowns solve the same problem and coincide with the originals by uniqueness. At j = 1 this is the
uniqueness of stage 1, whose unknowns (m1, φ1, ĝ2) solve a system that S maps to itself; it gives J* m1 = −m1 and,
through L0 φ1 = −½ m1(ℓ, ℓ) with zero data, J* φ1 = −φ1.

The rewriting with the fixed phase ([[pending:sec-fixed-phase]]) commutes with S. There the profiles g_j are the
coefficients of Ĝ(X, θ; λ) := G(X, θ + φ1 + λΨ; λ), Ψ := Σ_(j≥2) λ^(j−2) φ_j. For the transformed unknowns φ̃1 = −J*
φ1 and λ Ψ̃(λ) = −J*((−λ) Ψ(−λ)), and G̃(X, θ′; λ) = J* G(X, 3π/2 − θ′; −λ), so

    Ĝ̃(X, θ; λ) = J* G(X, 3π/2 − θ + φ1 + (−λ) Ψ(−λ); −λ) = J* Ĝ(X, 3π/2 − θ; −λ),

whose coefficient of λ^j is (−1)^j J* g_j(·, 3π/2 − ·) = (S g)_j. Hence S g = g. Taking the θ-mean, which the
reflection θ ↦ 3π/2 − θ preserves, gives J* ⟨g_j⟩ = (−1)^j ⟨g_j⟩, and ⟨g1⟩ = m1 since W has θ-mean zero. ∎

*Proof of [[prop:mean-mass]].* *Outside the shell.* The oscillating profiles (W, χ, the ĝ_m and the phase terms of the
fixed-phase rewriting) vanish outside v_start < v < v_end: each solves a transport along ℓ, at fixed v, whose forcing
and data are supported there ([[pending:lem-stage-system]], [[pending:lem-stage-data]] (i)), the wave being
proportional to env. So for v outside that interval g_app = g0 + λ m1 + λ² E, with E bounded with its derivatives, and

    M[S_(v,r)](g_λ) = M[S_(v,r)](g0) + λ DM[m1] + O(λ²) + O(|w| + |∂w|),

with DM the derivative of M at g0 on S_(v,r). By [[lem:round-spheres]], M[S_(v,r)](g0) = μ(v). DM is linear, and
naturality with J fixing g0 and S_(v,r) gives DM[J* m] = DM[m]: as g0 + ε J* m = J*(g0 + ε m),

    M[S](g0 + ε J* m) = M[J(S)](g0 + ε m) = M[S](g0 + ε m).

By [[lem:quarter-turn]] (c), DM[m1] = DM[J* m1] = −DM[m1], so DM[m1] = 0. The remainder is at most C λ^(K−4) ≤ C λ² by
[[eq:remainder-pointwise]]. For v < v_start the means vanish too: their forcing terms and data on Σ_τ0 are supported in
v ≥ v_start, and v does not decrease along future causal curves of g0.

*Inside the shell.* By [[lem:sphere-two-scale]] (a)–(b) for G = g_app, θ^±, the area and g_app(n⁺, n⁻) are those of g0
up to O(λ): the wave enters at order λ⁰ only through the term ½ k^±(ℓ) ∂_θ tr_S g1 of the proof of that lemma, which
vanishes by [[eq:wave-traceless]]. So M[S_(v,r)](g_app) − μ(v) = O(λ), and the remainder contributes C(|w| + |∂w|) ≤
C λ^(K−4). ∎

**Remark {#rem:mean-mass-aspect}** (What the mass sees.) The first mean m1 need not vanish: in the gauge of the proof
its forcing, the phase mean of R^(1)[g0 + λ W], is nonzero only in its dv dϑ component, where it equals
−(4/9) A² env² h(ζ)² sin 2ϑ/r³ [[pending:computational-2]]. This term is odd under the quarter turn, as
[[lem:quarter-turn]] requires, and a rotation-invariant mass cannot see it. The quantity of [[prop:mean-mass]] is the
Hawking mass of the spheres S_(v,r) of the domain. It is not the angular mean of the mass aspect at past null infinity,
which is a different quantity, governed by the mass law of [[thm:bondi-law]].
