## The data {#ch:data}

This chapter constructs the Cauchy data of the main theorem, which the proof of its items 1–5 in [[sec:main-proof]]
uses. The data are posed on the slice Σ := Σ_τ0, before the shell reaches the hole, and no smallness of the background
is used. The approximate solution of [[thm:approximant]], with suitable stage data, has data that satisfy the
constraints and the gauge condition D = 0 to high order ([[sec:data-approximant]]). The remaining error is removed
exactly by solving the constraints outward in r, as a parabolic–hyperbolic system, from a sphere inside the shell where
the approximant's data are the seed's exactly ([[sec:data-evolution]]). The data then coincide with the seed's on Σ ∩ {r
< v_start − τ0}.

Notation is that of [[ch:uniform-existence]]. In addition, the ansatz [[eq:ansatz]], G = ḡ + λ W + Σ_(j=2)^(N+1) λ^j ĝ_j
with the mean metric ḡ = g0 + Σ_(j=1)^(N) λ^j m_j, the phase u = v + Σ_(j=1)^(N) λ^j φ_j and the approximant g_app = G(X,
u/λ) (in (E4), and so in [[thm:data]], g_app is the fixed-phase form [[eq:approximant]] instead; the two differ by
O(λ^(N+1)) in scaled norms, [[sec:approximant]]), the two-scale operator R_u of [[def:two-scale]] with the orders ℛ^(m)
of the expansion R_u[G] = Σ_m λ^m ℛ^(m), and the coefficients e_j = 2 ℓ·dφ_j − m_j(ℓ, ℓ) − q_j of ḡ⁻¹(du, du) = Σ_(j≥1)
λ^j e_j ([[eq:eikonal-coefficients]]) are those of [[ch:approximant]]. Stage 0 is [[lem:stage-zero]]: the wave W = W_TT +
χ dv dv has W(ℓ, ·) = 0 and tr_g0 W = 0, and χ vanishes on Σ_τ0 ([[eq:chi-transport]]). Where each unknown first enters
the expansion is [[lem:first-entry]]; the stage equations (a)–(c), each a linear hyperbolic system solved without loss,
are [[lem:stage-system]]; and the passage from G(X, u/λ) to the fixed-phase form [[eq:approximant]], with ℛ^(m) = 0 for m
≤ N − 1, is the proof of [[thm:approximant]] ([[sec:approximant]]). The leading wave W_TT of [[eq:waves]] has no dv and
no dr component and is traceless on the spheres {τ, r = const} ([[lem:waves]] (b)).

### The theorem {#sec:data-theorem}

**Theorem {#thm:data}** (Exact data.) Let K ≥ 6 and N := K + 3, and let g_app be the approximant of [[thm:approximant]]
with N stages and the stage data of [[lem:stage-data]], in its fixed-phase form [[eq:approximant]]. For λ small there is
a vacuum Cauchy datum (γ, κ) on Σ (the constraints hold exactly), with the gauge condition D = 0 imposed through ∂_τ g,
whose w := g − g_app satisfies (E4) of [[thm:uniform-existence]]; it equals the seed's datum on Σ ∩ {r < v_start − τ0}.
The datum is smooth and invariant under the T² action and both reflections.

The proof is in [[sec:data-proof]].

### Two identities {#sec:data-identities}

For a Lorentzian g put E := Ric^H(g) and

    S(D)_mn := (1/2)(g_(mρ) ∇̂_n D^ρ + g_(nρ) ∇̂_m D^ρ),

∇̂ the connection of g0, so that Ric(g) = E + S(D) by the definition [[eq:gauge]] of Ric^H, and Gt(T) := T − (1/2)(tr_g
T) g.

(I1) The contracted Bianchi identity div_g Gt(Ric) = 0 reads

    B_g[D] := div_g Gt(S(D)) = −div_g Gt(E),                                                        {#eq:data-bianchi}

with B_g linear in D, of second order with principal part (1/2) g^(ab) ∂_a ∂_b (acting on D with its index lowered by
g), and with other coefficients involving g, ∂g, g0 and the derivatives of g0, and no second derivative of g.

*Proof.* The identity is div_g Gt(E + S(D)) = 0. For the structure, put T^ρ_n := ∇̂_n D^ρ and T_(mn) := g_(mρ) T^ρ_n, so
that S(D)_mn = (1/2)(T_(mn) + T_(nm)). Since ∇g = 0 for the connection ∇ of g,

    (div_g S(D))_n = (1/2)(∇_ρ T^ρ_n + g_(nρ) g^(ab) ∇_a T^ρ_b),     tr_g S(D) = T^ρ_ρ = ∇̂_ρ D^ρ.

Each ∇_a T^ρ_b = ∂_a T^ρ_b + Γ[g] T − Γ[g] T, and ∂_a T^ρ_b = ∂_a ∂_b D^ρ + (∂Γ[g0]) D + Γ[g0] ∂D. So div_g Gt(S(D)) =
div_g S(D) − (1/2) d tr_g S(D) has coefficients built from g, ∂g (through Γ[g]) and g0 with its derivatives, and no
second derivative of g. Its second-order part is (1/2)(∂_ρ ∂_n D^ρ + g_(nρ) g^(ab) ∂_a ∂_b D^ρ) − (1/2) ∂_n ∂_ρ D^ρ =
(1/2) g_(nρ) g^(ab) ∂_a ∂_b D^ρ. ∎

(I2) On a slice {τ = const} with future unit normal n, the induced data (γ, κ) have the constraint map

    (J, ρ) = (2(−div κ + d tr κ), R − |κ|² + (tr κ)²)                                          {#eq:data-constraint-map}

of [CD03, (2.1), p. 4], with R the scalar curvature of γ; these are the constraint equations in every space dimension.
By the Gauss and Codazzi equations, (J, ρ) equals 2 G(n, ·), G := Gt(Ric): ρ is its n-component and J its tangential
components, up to the sign convention of κ. If D = 0 on the slice, its tangential derivatives vanish there, so ∂D = −n♭
⊗ Z there, with n♭ := g(n, ·) and Z := ∂_n D (indeed n♭(n) = −1, so ∂_n D = Z). At D = 0, ∇̂D = ∂D, so

    S(D) = −(1/2)(n♭ ⊗ Z♭ + Z♭ ⊗ n♭),     tr_g S(D) = −g(n, Z),

and Gt(S(D))(n, ·) = −(1/2)(n♭(n) Z♭ + g(Z, n) n♭) + (1/2) g(n, Z) n♭ = (1/2) Z♭. Hence on a slice where D = 0,

    2 G(n, ·) = 2 Gt(E)(n, ·) + Z♭,                                                          {#eq:data-constraint-gauge}

and for a solution of Ric^H(g) = 0 with D = 0 on the slice the constraints hold there exactly when ∂_n D = 0 there.

*What the theorem asks.* Let (γ, κ) on Σ satisfy the constraints, and give g on Σ the lapse and shift of G(X, u/λ), the
spatial part γ, ∂_τ of the spatial part fixed by κ, and ∂_τ of the lapse and shift fixed by D(g) = 0 on Σ. The last
choice is possible because D is linear in ∂_τ g_(τ ·), with an invertible coefficient on a spacelike slice. Indeed, with
D_σ := g_(σρ) D^ρ = g^(ab) (∂_a g_(σb) − (1/2) ∂_σ g_(ab)) − g_(σρ) g^(ab) Γ[g0]^ρ_ab, the terms containing y_σ := ∂_τ
g_(στ) are g^(ττ) y_σ + δ^τ_σ g^(τj) y_j − (1/2) δ^τ_σ (g^(ττ) y_τ + 2 g^(τj) y_j): that is, (1/2) g^(ττ) y_τ in D_τ and
g^(ττ) y_j in D_j. The coefficient matrix is diag((1/2) g^(ττ), g^(ττ), …, g^(ττ)), of determinant (1/2) (g^(ττ))⁵ ≠ 0,
since g^(ττ) < 0 on a spacelike slice; at g0, g0^(ττ) = −(r² + μ)/r² and the determinant is −(r² + μ)⁵/(2 r¹⁰). Then (g,
∂_τ g) is a Cauchy datum for Ric^H = 0 with D = 0 on Σ and, by [[eq:data-constraint-gauge]], ∂_τ D = 0 on Σ; D = 0 and
the constraints on Σ are the hypotheses of [[lem:gauge-propagation]], which the proof of the main theorem uses. (E4)
asks that w := g − g_app be O(λ^K) in the scaled norm Data. So there are two steps: the approximant's data must satisfy
the constraints and D = 0 to high order ([[sec:data-approximant]]), and the error must be removed exactly with λ-uniform
bounds ([[sec:data-evolution]]).

**Remark {#rem:data-conformal}** (The conformal method.) Touati constructs high-frequency data by the conformal method,
inverting the flat operators Δ_e and div_e L_e and closing each fixed point by the smallness of the background: the
contraction of [Tou23b, Section 5.4.2, p. 29] holds for ε small, under his assumption [Tou23b, (2.1)] that the
background data are within ε of the Euclidean data in weighted Sobolev norms ([Tou23b, Theorem 2.1]). Here the slice
passes through the hole, the background data are not close to Euclidean, and an elliptic method needs boundary data at r
= a as well as far out. The evolution in r used below needs neither: it is solved outward from a sphere inside the
shell, where the approximant's data are the seed's exactly, and nothing is imposed further out.

### The approximant's data {#sec:data-approximant}

D(g_app) has the two-scale form [D_u[G]]_u, D_u[G] = Σ_(m≥0) λ^m D^(m)(X, θ), as Ric^H does. [[eq:data-bianchi]] is an
identity of differential polynomials in g, and the operators ∂_a + λ⁻¹ (∂_a u) ∂_θ are commuting derivations, so
[[eq:data-bianchi]] holds order by order for the profiles; its right side at order j involves ℛ^(i), i ≤ j + 1, only.
These vanish for i ≤ N − 1. Moreover D^(0) = g0⁻¹(∂_θ W(ℓ, ·) − (1/2) dv tr ∂_θ W) = 0, since W(ℓ, ·) = 0 and tr W = 0.

**Lemma {#lem:gauge-hierarchy}** (The gauge hierarchy.) Let N ≥ 3 and suppose that on Σ

- (F1) D^(m)(X, θ) = 0 for all θ, m = 1, …, N − 1;
- (F2) ∂_τ ⟨D^(m)⟩ = 0, m = 1, …, N − 2.

Then D^(m) = 0 on Ω × S¹ for m ≤ N − 2, and ∂_θ D^(N−1) = 0. Hence |D(g_app)|_k ≤ C λ^(N−1) on every Σ_τ, and the
constraint map of g_app's data on Σ has scaled norm |·|_(k−1) ≤ C λ^(N−2).

*Proof.* In two-scale form the principal part of B_g on λ^m [Y]_u is

    λ^(m−2) (1/2) g⁻¹(du, du) ∂_θ² Y + λ^(m−1) (g⁻¹(du, ∂_X) + (1/2) □_g u + M) ∂_θ Y + λ^m (1/2) g^(ab) ∂_a ∂_b Y,

where g⁻¹(du, du) = O(λ²) (ḡ⁻¹(du, du) = O(λ^(N+1)), and W(ℓ, ·) = 0; the leading part, −λ² ĝ_2(ℓ, ℓ), multiplies ∂_θ²
Y, which vanishes for the Y = D^(m) of the induction), g⁻¹(du, ∂_X) = ℓ·∂_X + O(λ), □_g u = □_(g0) v + O(λ), and M(X,
θ), from the coefficient Γ[g] of ∂D (of size ∂g = O(1)), is a bounded multiplication operator on profiles. Induction on
m = 0, …, N − 2 with the hypothesis: D^(j) = 0 for j < m and ∂_θ D^(m) = 0 (true at m = 0). At order m the oscillating
part of [[eq:data-bianchi]] is the transport

    (ℓ·∂_X + (1/2) □_(g0) v) Z + Π_osc(M Z) = (first order in ⟨D^(m)⟩)     for Z := ∂_θ D^(m+1),

Π_osc the projection onto zero θ-mean, and its mean is the linear wave equation (1/2) □_(g0) ⟨D^(m)⟩ + (first order)
⟨D^(m)⟩ + ⟨M Z⟩ = 0 (M depends on θ, so M Z has a mean part, which the wave equation carries; the order-m equation does
not depend on λ, so its wave operator is g0's). Every other term vanishes by the hypothesis or because it contains
ℛ^(i), i ≤ m + 1 ≤ N − 1. The data are zero: ⟨D^(m)⟩ by (F1), ∂_τ ⟨D^(m)⟩ by (F2), Z by (F1) at order m + 1. This linear
system for (⟨D^(m)⟩, Z) closes without loss exactly as the stage equations do ([[lem:stage-system]]: the mean in
H^(s+1), Z in H^s; the energy inequality of [[lem:energy]] and the transport estimate of [[lem:transport]]; the
transport curves reach Σ inside Ω by [[lem:domain]] (d)), so ⟨D^(m)⟩ = 0 and Z = 0: the hypothesis at m + 1. Then
D(g_app) = λ^(N−1) [D^(N−1)] + O(λ^N) with bounded profiles, and 2 G(g_app)(n, ·) = 2 Gt(E)(n, ·) + 2 Gt(S(D))(n, ·)
with S(D) of first order in D: the scaled norm of the second term is at most C λ⁻¹ λ^(N−1), and of the first at most C
λ^(N−1), by (E3). ∎

**Lemma {#lem:stage-data}** (The stage data.) For every N there are stage data for [[thm:approximant]] satisfying (F1)
and (F2), all vanishing on Σ ∩ {r < v_start − τ0}. The stage data constructed in the proof are fixed by the seed, by N
and by the slice Σ (on which they are posed: τ0 enters through the data on Σ, the phase (τ0 + r)/λ there and the region
r < v_start − τ0); "the stage data of [[lem:stage-data]]" means these, and not any others with the stated properties.

*Proof.* Stage 0: χ = 0 on Σ, as chosen in [[eq:chi-transport]]. Stage m = 1, …, N, everything of the earlier stages
given: put φ_m = 0 and (m_m)_(τ ·) = 0 on Σ. Stage N's data are not needed for (F1) and (F2), but they are fixed here,
so that every stage's data are smooth, invariant under T² and both reflections, and vanish on Σ ∩ {r < v_start − τ0}; at
m = N step (iii) below runs inside [[thm:approximant]] of order N, since after stage N ℛ^(N) = −(1/2) e_(N+1) ∂_θ² W
with e_(N+1) = −q_(N+1) independent of θ. The unknowns left on Σ are γ_m and κ_m, the order-m means of the induced
metric and of the second fundamental form (γ_m is the spatial part of m_m, and, given γ_m, κ_m fixes ∂_τ of that spatial
part), ∂_τ (m_m)_(τ ·), and ĝ_(m+1).

(i) On Σ the oscillating part of D^(m), its index lowered by g0, is Pol(∂_θ ĝ_(m+1)) + Λ_m(γ_m) + (known), where

    Pol(Y) := Y(ℓ, ·) − (1/2) dv tr_(g0) Y

for symmetric 2-tensors Y, and Λ_m is algebraic: it collects the terms of the order-m oscillating part of D that are
linear in m_m or in ∂φ_m (bilinear with ∂_θ W, such as m_m(ℓ, ·) contracted with ∂_θ W, ⟨m_m, ∂_θ W⟩ ℓ and ∂_θ W(grad
φ_m, ·)), in which ∂_τ φ_m = −(1/2)(m_m(ℓ, ℓ) + q_m) by the stage equation (b) of [[lem:stage-system]] and the
tangential derivatives of φ_m vanish. Pol is onto at every point. Indeed, fix a null vector k with dv(k) = g0(ℓ, k) = 1,
put k♭ := g0(k, ·), and fix a covector ξ with ξ(ℓ) = 0 and g0⁻¹(ξ, ξ) = 1. For a covector β put

    Y_β := β ⊗ k♭ + k♭ ⊗ β − β(ℓ) k♭ ⊗ k♭ − 2 β(k) ξ ⊗ ξ.

Then Y_β(ℓ, ·) = β(ℓ) k♭ + β − β(ℓ) k♭ = β, using k♭(ℓ) = 1 and ξ(ℓ) = 0, and tr_(g0) Y_β = 2 β(k) − 0 − 2 β(k) = 0,
using g0⁻¹(k♭, k♭) = g0(k, k) = 0; so Pol(Y_β) = β. Put Pol⁺ := Pol^T (Pol Pol^T)⁻¹, the transposes taken in the
Euclidean structure of the Cartesian coordinates (τ, x); Pol Pol^T is invertible because Pol is onto, and that structure
is O(4)-invariant, so Pol⁺ commutes with the symmetries. Then ∂_θ ĝ_(m+1) := −Pol⁺(Λ_m(γ_m) + known) on Σ solves the
equation (the right side has zero θ-mean, and ĝ_(m+1) is its zero-mean antiderivative in θ), smoothly, pointwise and
linearly in γ_m.

(ii) The mean of D^(m) on Σ is linear in ∂_τ (m_m)_(τ ·), with the invertible coefficient of the gauge's data
([[sec:data-identities]]), plus terms in γ_m, κ_m and known quantities: it fixes ∂_τ (m_m)_(τ ·).

(iii) First, every first derivative of D^(j), j < m, vanishes on Σ. Solve stage m with any data: D^(j), j ≤ m − 1, does
not depend on the data of stage m, and ℛ^(i) = 0 for i ≤ m − 1 once stage m is solved (before it, ℛ^(m−1) = −(1/2) e_m
∂_θ² W, and stage m imposes e_m = 0; [[lem:first-entry]], [[lem:stage-system]]). For m ≥ 3, [[lem:gauge-hierarchy]] with
N := m applies (its hypotheses, (F1) at orders 1, …, m − 1 and (F2) at orders 1, …, m − 2, were arranged at the earlier
stages) and gives D^(j) = 0 on Ω for j ≤ m − 2 and ∂_θ D^(m−1) = 0; then the first derivatives of D^(m−1) on Σ vanish
too: the tangential ones by (F1), the normal one of the mean by (F2) at order m − 1, and the oscillating part is zero.
For m = 1, 2 the same holds directly: D^(0) = 0, and for m = 2 the order-0 transport, with ∂_θ D^(1) = 0 on Σ by (F1),
gives ∂_θ D^(1) = 0 on Ω, and the normal derivative of ⟨D^(1)⟩ vanishes on Σ by (F2) at order 1. The tangential
derivatives of D^(m) vanish by (F1), and the phase part λ⁻¹ (du) ∂_θ D^(m+1) of the derivatives has mean zero. So the
order-m mean of 2 G(g_app)(n, ·) on Σ is ∂_n ⟨D^(m)⟩, the order-m mean of [[eq:data-constraint-gauge]], the E-part
having mean zero (after stage m, ℛ^(i) = 0 for i < m and ℛ^(m) = −(1/2) e_(m+1) ∂_θ² W, of mean zero): (F2) at order m
is the order-m mean of the constraint equations. That is

    𝔓(γ_m, κ_m) + B_m(γ_m) = S_m,

with 𝔓 the linearisation of the constraint map at the data of g0 on Σ [CD03, (2.2), p. 4], B_m algebraic in γ_m (the
means of the products of γ_m and of ĝ_(m+1) of (i) with the oscillating data), and S_m known. Solve it with γ_m = α_m dr
dr and κ_m = ϖ_m Π + q′_m ⊗ dr + dr ⊗ q′_m by [[lem:linear-evolution]] (B_m is a zeroth-order term of the kind allowed
there), from zero data at r = a. Its forcing terms vanish where the earlier stages' data and the waves do, so (α_m, ϖ_m,
q′_m) vanish on r < v_start − τ0, and they are smooth. ∎

### The constraints as an evolution in r {#sec:data-evolution}

On Σ use (r, ω), ω ∈ S³, a ≤ r ≤ b1 := b(τ0); a stays the inner radius of Ω. For data (γ, κ) on Σ put Π := γ − |dr|_γ⁻²
dr ⊗ dr; on vectors tangent to the spheres {r = const} Π is the induced metric, and Π(γ⁻¹dr, ·) = 0. For U := (α, ϖ, q),
with α and ϖ functions and q a covector with q(γ⁻¹dr) = 0 (so that q is fixed by its angular components q_A, and q_r =
−γ^(rA) q_A/γ^(rr)), put, as in [Rac16] (the lapse of the foliation by the spheres, and the mixed and trace parts of κ),

    γ_U := γ + α dr ⊗ dr,      κ_U := κ + ϖ Π + q ⊗ dr + dr ⊗ q.                                          {#eq:data-u}

Write 𝒞(γ, κ) := (J, ρ) for the constraint map [[eq:data-constraint-map]]. Note that γ_U and γ induce the same metric on
the spheres, and that γ_U⁻¹ = γ⁻¹ − c(α) γ⁻¹dr ⊗ γ⁻¹dr with c(α) := α/(1 + α γ^(rr)).

**Lemma {#lem:constraints-evolution}** (The constraints as an evolution in r.) (a) The constraint map of (γ_U, κ_U) is
quasilinear in U: of second order in α with no ∂_r² α and no ∂_r of an angular derivative of α, of first order in (ϖ,
q), and α enters J to first order only. Its ρ-component,

    ρ = p ∂_r α − γ^(rr) Π^(AB) ∂_A ∂_B α + (first order in the angular derivatives of α) + (algebraic in U),
        p := (γ^(rr))^(3/2) H,                                                                           {#eq:data-rho}

with γ^(rr), H and Π^(AB) evaluated at γ_U (H the mean curvature of the spheres with respect to the unit normal toward
increasing r, Π^(AB) the inverse of their induced metric), is parabolic in r where the spheres have positive mean
curvature. Its J-component is symmetric hyperbolic in (ϖ, q) with r as time. At the data of g0 on Σ, γ = (1 + μ/r²)
dr² + r² dΩ² with μ = μ(τ0 + r), so that γ^(rr) = r²/(r² + μ), γ^(rA) = 0, Π = r² dΩ² and H = 3/(r² + μ)^(1/2) > 0 for
all r, and

    ρ = (3 r³/(r² + μ)²) ∂_r α − (r² + μ)⁻¹ Δ_(S³) α + …,
    J_r = 6 ∂_r ϖ − 2 Π^(AB) ∂_A q_B + …,     J_A = −(2 r²/(r² + μ)) ∂_r q_A + 4 ∂_A ϖ + …;

the symmetrizer 𝒮 = diag(1, −(1/2) Π⁻¹), which depends on γ alone, gives 𝒮 A0 = diag(6, (r²/(r² + μ)) Π⁻¹) > 0 and 𝒮 A^B
symmetric for every angle B. In the class of fields of (r, ϑ) invariant under T² and both reflections (q = q_ϑ dϑ; the
components q_(φ1), q_(φ2) and J_(φ1), J_(φ2) vanish by the reflections) these equations are the whole system: J_r = 6
∂_r ϖ − (2/r²) ∂_ϑ q + …, J_ϑ = −(2 r²/(r² + μ)) ∂_r q + 4 ∂_ϑ ϖ + …, with 𝒮 = diag(1, −1/(2r²)), 𝒮 A0 = diag(6, 1/(r² +
μ)), 𝒮 A^ϑ = [[0, −2/r²], [−2/r², 0]], and real characteristic speeds c² = 2 (r² + μ)/(3 r⁴) > 0; the construction stays
in that class. For γ_rA small, as at the approximant's data (where γ_rA = O(λ²), by (b) below), and with q and Π read
as above, the symmetrizers still form a one-dimensional space, depending on γ alone; its generator, the matrix 𝒮 that
takes (J_r, J_A) to

    (J_r + (γ^(rA)/γ^(rr)) J_A,  −(1/2) Π^(AB) J_B),                                              {#eq:data-symmetrizer}

has 𝒮 A0 = diag(6, γ_U^(rr) Π^(AB)) > 0 and 𝒮 A^C symmetric for every angle C. The construction needs only γ_rA small.

(b) At the approximant's data (the data on Σ of g_app built from the stage data of [[lem:stage-data]]) the constraint
map of (γ_U, κ_U), as a function of U, has no coefficient of order 1/λ: the second derivatives of γ of order 1/λ enter
the coefficients of U only through the trace of W on the spheres, which vanishes, and the ∂_r κ_rr terms of div κ and d
tr κ cancel.

(c) The phase on Σ is (τ0 + r)/λ, so angular derivatives of every coefficient are bounded uniformly in λ. At the
approximant's data the order-0 parts of all principal coefficients equal the background's, so p, γ^(rr) Π^(AB) and 𝒮 A0
keep their signs for λ small; 𝒮 depends on γ alone, whose first derivatives are bounded uniformly in λ; and
[[lem:linear-evolution]] needs no ∂_r p. Lower-order coefficients may oscillate at O(1), and some do: the coefficient of
α in ρ contains the term |𝒜|²/ν² of the proof below, where the second fundamental form 𝒜 of the spheres has the
oscillating part (1/(2ν)) [∂_θ W_AB] of order one, so that it oscillates, with a nonzero θ-mean where the waves do not
vanish (such a mean is part of B_m in [[lem:stage-data]] (iii)); and the coefficient of ∂_C α in J_A contains −γ^(rr)
Π^(BC) κ_AB, where κ_AB has the oscillating part (1/2) n0(v) [∂_θ W_AB] of order one, n0 the future unit normal of g0
to Σ. [[lem:linear-evolution]] needs only their angular regularity.

*Proof.* (a), ρ. Write γ = ν² dr² + Π_AB (dω^A + σ^A dr)(dω^B + σ^B dr), with lapse ν > 0 and shift σ of the foliation
by the spheres; then γ^(rr) = ν⁻², and γ_U has the same Π and σ and the lapse ν_U with ν_U² = ν² + α. Let e_r := ν⁻¹(∂_r
− σ) be the unit normal, 𝒜 := (1/(2ν))(∂_r Π − 𝓛_σ Π) the second fundamental form of the spheres and H := tr_Π 𝒜.
The Gauss equation for the spheres, R = R_Π + 2 Ric(e_r, e_r) − H² + |𝒜|², and the Riccati equation along the normal
flow, Ric(e_r, e_r) = −∂_(e_r) H − |𝒜|² − ν⁻¹ Δ_Π ν, give

    R(γ) = R_Π − 2 ∂_(e_r) H − H² − |𝒜|² − 2 ν⁻¹ Δ_Π ν.

Replace ν by ν_U. In H = H̃/ν, H̃ := (1/2) Π^(AB)(∂_r Π_AB − (𝓛_σ Π)_AB) does not depend on α, so −2 ∂_(e_r) H ⊃ 2 ν⁻³
H̃ ∂_r ν = H̃ ν⁻⁴ ∂_r(ν²): the coefficient of ∂_r α is H ν⁻³ = (γ^(rr))^(3/2) H, evaluated at γ_U. The second
derivatives of α come from −2 ν_U⁻¹ Δ_Π ν_U = −ν_U⁻² Δ_Π α + (first order): −γ_U^(rr) Π^(AB) ∂_A ∂_B α, angular only.
R_Π, H², |𝒜|² and the σ-part of ∂_(e_r) H contain α algebraically or through its angular derivatives. The terms
−|κ_U|² + (tr κ_U)² contain U algebraically. This proves the form [[eq:data-rho]].

(a), J. Let γ_rA be small. Put Π^(ij) := γ^(ik) γ^(jl) Π_kl and Π_i^k := γ^(kj) Π_ji. Since Π = γ − dr ⊗ dr/γ^(rr),
Π^(ij) = γ^(ij) − γ^(ri) γ^(rj)/γ^(rr), that is γ⁻¹ = Π^♯ + γ⁻¹dr ⊗ γ⁻¹dr/γ^(rr) with Π^♯ := (Π^(ij)); so Π^(rk) = 0, and
the angular block Π^(AB) = γ^(AB) − γ^(rA) γ^(rB)/γ^(rr) is the inverse of the angular block (γ_AB) of γ (the inverse of
a block of a matrix is the Schur complement of the complementary block of the inverse matrix), that is of the induced
metric of the spheres, as in the statement. In J = 2(−div_(γ_U) κ_U + d tr_(γ_U) κ_U) the derivatives of (ϖ, q) come from
κ_U − κ. Since Π(γ⁻¹dr, ·) = 0 and q(γ⁻¹dr) = 0, the formula for γ_U⁻¹ gives tr_(γ_U) Π = 3 and tr_(γ_U)(q ⊗ dr + dr ⊗ q)
= 0, so d tr_(γ_U) κ_U contains 3 dϖ. Further, γ_U^(jk) Π_ij ∂_k ϖ = Π_i^k ∂_k ϖ, γ_U⁻¹dr = (1 + α γ^(rr))⁻¹ γ⁻¹dr, and
γ_U^(jk) ∂_k q_j = Π^(AB) ∂_A q_B + (lower order), because (γ⁻¹dr)^j ∂_k q_j = ∂_k(q(γ⁻¹dr)) − q_j ∂_k (γ⁻¹dr)^j is of
order zero and Π^(rk) = 0. So the principal part of J is

    J_i ≅ 2 (3 ∂_i ϖ − Π_i^k ∂_k ϖ − (1 + α γ^(rr))⁻¹ (γ⁻¹dr)^k ∂_k q_i − ∂_i r Π^(AB) ∂_A q_B).

Contracting with γ⁻¹dr, which Π annihilates, and using q(γ⁻¹dr) = 0 again, J_r + (γ^(rA)/γ^(rr)) J_A = J(γ⁻¹dr)/γ^(rr) ≅
6 ∂_r ϖ + 6 (γ^(rC)/γ^(rr)) ∂_C ϖ − 2 Π^(CB) ∂_C q_B. For the angular components, ∂_A r = 0 and Π_A^k ∂_k = ∂_A, so J_A
≅ 4 ∂_A ϖ − 2 (1 + α γ^(rr))⁻¹ (γ^(rr) ∂_r + γ^(rC) ∂_C) q_A, and −(1/2) Π^(AB) J_B ≅ −2 Π^(AC) ∂_C ϖ + (1 + α γ^(rr))⁻¹
Π^(AB)(γ^(rr) ∂_r + γ^(rC) ∂_C) q_B. Since (1 + α γ^(rr))⁻¹ γ^(rr) = γ_U^(rr), the matrix 𝒮 of [[eq:data-symmetrizer]]
makes the principal part of J, in (ϖ, q_B), equal to 𝒮 A0 ∂_r + 𝒮 A^C ∂_C with 𝒮 A0 = diag(6, γ_U^(rr) Π^(AB)), positive
definite, and

    𝒮 A^C = [[6 γ^(rC)/γ^(rr), −2 Π^(CB)], [−2 Π^(AC), (1 + α γ^(rr))⁻¹ γ^(rC) Π^(AB)]],

symmetric; at the data of g0, where γ^(rA) = 0 and α = 0, 𝒮 = diag(1, −(1/2) Π⁻¹). α enters J through γ_U⁻¹ and through
the connection of γ_U, so to first order. A symmetrizer is a matrix S with S A0 and every S A^C symmetric: linear
conditions on S, with coefficients continuous in γ and α. Where γ_rA = 0, in a frame orthonormal for Π, A0 = diag(6, −2
γ_U^(rr) I) and A^C has the row −2 e_C^T (the J_r-equation on q) and the column 4 e_C (the J_A-equations on ϖ), e_C the
C-th unit vector. Writing S = [[s, b^T], [c, D]], S A^C = [[4 b·e_C, −2 s e_C^T], [4 D e_C, −2 c e_C^T]] is symmetric
for C = 1, 2, 3 only if D = −(s/2) I and c = 0, and then S A0 = [[6 s, −2 γ_U^(rr) b^T], [0, s γ_U^(rr) I]] is symmetric
only if b = 0: S = s diag(1, −(1/2) I), a one-dimensional space. The dimension of the solution space of such a linear
system cannot increase under small changes of its coefficients, and the space contains 𝒮 ≠ 0; so for γ_rA small it is
one-dimensional, generated by 𝒮. At the data of g0, ν² = 1 + μ/r², σ = 0 and Π = r² dΩ²; the volume density is r² (r² +
μ)^(1/2) times that of the unit sphere and e_r = (r/(r² + μ)^(1/2)) ∂_r, so H = div e_r = (r² (r² + μ)^(1/2))⁻¹ ∂_r (r³)
= 3/(r² + μ)^(1/2), and p = (r²/(r² + μ))^(3/2) · 3/(r² + μ)^(1/2) = 3 r³/(r² + μ)². In the symmetric class the speeds
solve det(A^ϑ − c A0) = 0 with A0 = diag(6, −2 r²/(r² + μ)) and A^ϑ = [[0, −2/r²], [4, 0]]: −12 c² r²/(r² + μ) + 8/r²
= 0.

(b) Write γ and κ for the data of g_app on Σ, and expand in λ. On Σ the phases φ_j vanish, the means m_j have (m_j)_(τ
·) = 0 and spatial part α_j dr dr, W_TT has only angular components and χ dv dv only (τ, r) components, so γ_rA = λ² (…)
and the profiles ĝ_j, j ≥ 2, carry the factor λ^j. A derivative of order k along Σ of a term λ^j [f] is O(λ^(j−k)) in
the radial direction and O(λ^j) in the angular ones, since ∂_r v = 1 and ∂_A v = 0 on Σ. Hence the second derivatives of
γ of order 1/λ are λ⁻¹ [∂_θ² W_ij] in ∂_r² γ_ij, and κ has an oscillating part κ̃ of order one, with ∂_k κ = λ⁻¹ δ_k^r
[∂_θ κ̃] + O(1). Here κ = (1/2)(𝓛_n g)|_Σ up to sign, n the unit normal; the order-one oscillating part of 𝓛_n(λ [g1])
is n0(v) [∂_θ W_ij] and that of g0(∂_i n, ∂_j) + g0(∂_i, ∂_j n) is ∂_i v [∂_θ n♭_(1)]_j + ∂_j v [∂_θ n♭_(1)]_i, where
n♭_(1) := g0(n_(1), ·) and n_(1) is the coefficient of λ in n, which is algebraic in g1: n^a = −g^(aτ)/(−g^(ττ))^(1/2).
Its angular components are combinations of (g1)_(Ab) g0^(bτ) and of g0(n0, ∂_A) = 0; the oscillating part W_(Ab) g0^(bτ)
vanishes, since W_TT has no τ or r component, (dv)_A = 0, and g0^(Bτ) = 0. So κ̃_rA = 0, κ̃_AB = (1/2) n0(v) [∂_θ W_AB]
up to sign, and κ̃_rr is some function.

In ρ, by the formula for R(γ_U) above with ν_U² = ν² + α, the coefficients of U involve second r-derivatives of γ only
through ∂_(e_r) H, that is through (1/(2 ν_U²)) Π^(AB) ∂_r² Π_AB and through ∂_r 𝓛_σ Π; the second is O(1), since σ =
O(λ²), and the order-1/λ part of the first is λ⁻¹ (1/(2 ν_U²)) Π0^(AB) [∂_θ² W_AB] = λ⁻¹ (1/(2 ν_U²)) [∂_θ² tr_(Π0) W] =
0, W being traceless on the spheres. Every other coefficient of ρ involves at most one r-derivative of γ (angular
derivatives cost nothing) and no derivative of κ, so it is O(1). In J, the coefficients of (ϖ, q) involve γ, Π, dr and
the connection of γ_U, so they are O(1); and α enters through the connection of γ_U (O(1) coefficients) and through
γ_U⁻¹ in the terms with ∂κ. These are, by the formula for γ_U⁻¹,

    2 c(α) ((γ⁻¹dr)^j (γ⁻¹dr)^k ∂_k κ_ij − ∂_i(κ(γ⁻¹dr, γ⁻¹dr))) + (terms with ∂c(α) or ∂γ⁻¹: O(1) coefficients),

whose order-1/λ part is λ⁻¹ 2 c(α) (γ0^(rr))² ([∂_θ κ̃_ir] − δ_i^r [∂_θ κ̃_rr]), since γ⁻¹dr = γ0^(rr) ∂_r + O(λ): it
vanishes for i = r, where the two ∂_r κ_rr terms cancel, and for i = A, where κ̃_Ar = 0. Were W to have a nonzero trace
on the spheres, the term −ν_U⁻² Π^(AB) ∂_r² Π_AB of −2 ∂_(e_r) H would give the coefficient of α in ρ the part λ⁻¹ ν⁻⁴
[∂_θ² tr_(Π0) W], of order 1/λ.

(c) The principal coefficients are γ^(rr), Π^(AB), γ^(rA) and p = (γ^(rr))^(3/2) H; the first three are algebraic in γ =
γ0 + O(λ), and H = (1/(2 ν)) Π^(AB)(∂_r Π_AB − (𝓛_σ Π)_AB) has the order-one oscillating part (1/(2 ν)) Π0^(AB) [∂_θ
W_AB] = 0, the rest being γ0's value plus O(λ). The coefficient of α in ρ contains, from −|𝒜|² with 𝒜 = (1/(2 ν_U))(∂_r Π
− 𝓛_σ Π), the term ∂_α(−(ν²/ν_U²)|𝒜|²) = |𝒜|²/ν² at α = 0, and the oscillating part of 𝒜 is (1/(2 ν)) [∂_θ W_AB], so that
|𝒜|²/ν² has the oscillating part (1/(4 ν⁴)) |[∂_θ W]|²_(Π0) − (its θ-mean), and the θ-mean (1/(4 ν⁴)) ⟨|∂_θ W|²_(Π0)⟩,
positive where the waves do not vanish. (|∂_θ W|² is not constant in θ: by the form [[eq:waves]] of W_TT it is a positive
multiple of c⁴ sin²θ + s⁴ cos²θ + c²s² sin θ cos θ, with c = cos ϑ and s = sin ϑ, a quadratic form in (sin θ, cos θ) that
is not a multiple of sin²θ + cos²θ.) The other terms of the coefficient quadratic in the oscillation come from ∂_r H̃ in
∂_(e_r) H, whose quadratic part (1/2) ∂_r Π^(AB) ∂_r Π_AB + (1/2) Π^(AB) ∂_r² Π_AB ⊃ −(1/2) |[∂_θ W]|² − (1/2) [W^(AB)
∂_θ² W_AB] has θ-mean zero, and from H², which has no oscillating part of order one; the κ-terms carry κ̃(γ⁻¹dr, ·) and
tr κ̃, and κ̃_rA = 0, while tr_(Π0) κ̃_AB = 0 and κ̃_rr vanishes with χ on Σ. In J_A = 2(…), the term −γ^(jk)
Γ(γ_U)^l_(jk) κ_lA of div κ_U contributes 2 γ^(jk) Γ(γ_U)^B_(jk) κ_BA ⊃ −γ^(rr) Π^(BC) κ_AB ∂_C α (the part l = r carries
κ_rA), from γ^(jk) Γ(γ_U)^B_(jk) ⊃ −(1/2) γ^(rr) Π^(BC) ∂_C α, while the other terms with ∂_C α carry κ(γ⁻¹dr, γ⁻¹dr)
δ_A^C or κ_Ar, whose oscillating parts are multiples of δ_A^C or zero; the oscillating part −γ^(rr) Π^(BC) κ̃_AB is not a
multiple of δ_A^C, W_TT being traceless, so it does not cancel. The remaining claims are those of (a). ∎

**Lemma {#lem:linear-evolution}** (The linear evolution.) Consider on [a, b1] × S³, b1 > a, the linear system, with
coefficients measurable in r for which M_s below is finite,

    p ∂_r α − Δ_p α + b′·∂_S α + c α + e·(ϖ, q) = F_ρ,
    A0 ∂_r (ϖ, q) + A^B ∂_B (ϖ, q) + c′ (ϖ, q) + f ∂_r α + f′·∂_S α + c″ α = F_J,                      {#eq:data-linear}

with ∂_S the first-order angular derivatives, Δ_p a second-order angular operator, elliptic on each sphere with
ellipticity constant at least δ_e > 0, p ≥ p0 > 0, and an invertible symmetrizer 𝒮 with 𝒮 A0 ≥ A00 > 0 and 𝒮 A^B
symmetric, with zero data at r = a. For s > 3/2 + 2 there is a unique solution, and

    sup_r (‖α‖_(H^(s+1)) + ‖(ϖ, q)‖_(H^s)) + ‖α‖_(L² H^(s+2)) ≤ C (‖F_ρ‖_(L² H^s) + ‖F_J‖_(L² H^s)),

norms on the spheres S³, with C depending only on s, b1 − a, p0, δ_e, A00 and an upper bound for

    M_s := sup_r ‖(p, Δ_p, 𝒮, 𝒮 A0, 𝒮 A^B)‖_(H^(s+1)(S³)) + sup_r ‖(b′, c, e, c′, f, f′, c″)‖_(H^s(S³))
           + ∫_a^(b1) ‖∂_r (𝒮 A0)‖_(L^∞) dr,

and increasing in M_s; no other r-derivative of a coefficient enters. Write ‖U‖_(X_s) for the left side of the bound plus
‖∂_r α‖_(L² H^s). The bound is tame: at an index s″ > s, with ‖U‖_(s″; [a, r]) the left side at index s″ on [a, r] and
m_(s″)(r) the norms at index s″ of the coefficients at r (those of M_(s″), without the supremum),

    ‖U‖_(s″; [a, r]) ≤ C (‖F‖_(L²((a, r); H^(s″))) + ∫_a^r m_(s″)(r′) ω_s(r′) dr′ + ‖m_(s″) ω_∞‖_(L²(a, r))),

with C depending only on s″, M_s and the bounds above; ω_s square-integrable on (a, b1), its L² norm bounded by the
solution's X_s norm and ‖F‖_(L² H^(s−1)) (‖∂_r (ϖ, q)‖_(L^∞), a part of ω_s, contains F_J); and ω_∞ := ‖α‖_(W^(1,∞)) +
‖(ϖ, q)‖_(L^∞), bounded by C times the X_s norm. For the squared energy 𝒴 at index s″ (the parabolic energy at index s″ +
1 plus the hyperbolic one at index s″) the proof gives

    ∂_r 𝒴 + c0 ‖α‖²_(H^(s″+2)) ≤ ω_0 𝒴 + C ‖F‖²_(H^(s″)) + C m_(s″) ω_s 𝒴^(1/2) + C m_(s″)² ω_∞²,

with c0 > 0 the gain from the ellipticity of Δ_p after division by p, depending only on δ_e and M_s (also below, at index
s), and ω_0 := C (1 + ‖∂_r (𝒮 A0)‖_(L^∞)), integrable on (a, b1), with C as above; and integrating, taking the supremum
over [a, r], and Young's and Gronwall's lemmas give the bound.

The commutator and product estimates used are these. The Kato–Ponce inequality [GO13, p. 1] ([[thm:std-kato-ponce]], for
Schwartz functions, extended at p = 2 to the compactly supported functions used here by [[cor:std-kato-ponce]]): for 1 <
p < ∞ and s > 0, ‖𝒥^s(f g) − f 𝒥^s g‖_(L^p) ≤ C (‖∇f‖_(L^∞) ‖𝒥^(s−1) g‖_(L^p) + ‖𝒥^s f‖_(L^p) ‖g‖_(L^∞)), 𝒥 := (1 −
Δ)^(1/2) on R^n. The Moser estimate [DS23, Remark 2.3(i)] ([[rem:std-ds-moser]], for s > n/2 in n dimensions and Φ
satisfying (A2) of [DS23]): for a smooth function Φ of u, ‖Φ(u)‖_s ≤ C_I + F_I(‖u‖_∞) ‖u‖_s for u ∈ H^s, with C_I and F_I
depending on Φ. On S³ both follow from R³ through a finite atlas and a partition of unity, the Moser estimate for s >
3/2, which covers every index used here (s > 3/2 + 2).

*Proof.* Commute s angular derivatives, by the Killing fields X^I of the round S³, through [[eq:data-linear]]; the
commutators are estimated in terms of M_s by the Moser and Kato–Ponce inequalities on S³. Parabolic energy:

    ∂_r (1/2) ‖α‖²_(H^(s+1)) + c0 ‖α‖²_(H^(s+2)) ≤ C (‖α‖²_(H^(s+1)) + ‖(ϖ, q)‖²_(H^s) + ‖F_ρ‖²_(H^s))

after dividing by p (its ∂_r is not needed: the equation is solved for ∂_r α). Hyperbolic energy, after applying 𝒮 to
the second equation:

    ∂_r ⟨(ϖ, q), 𝒮 A0 (ϖ, q)⟩_(H^s) ≤ C (1 + ‖∂_r (𝒮 A0)‖_(L^∞)) ‖(ϖ, q)‖²_(H^s)
                                       + C ‖(ϖ, q)‖_(H^s) (‖∂_r α‖_(H^s) + ‖α‖_(H^(s+1)) + ‖F_J‖_(H^s)),

the 𝒮 A^B terms integrating by parts on the closed spheres, and ‖∂_r α‖_(H^s) ≤ C (‖α‖_(H^(s+2)) + ‖(ϖ, q)‖_(H^s) +
‖F_ρ‖_(H^s)) from the first equation. Young's inequality and Gronwall's lemma (which needs ‖∂_r (𝒮 A0)‖_(L^∞) only
integrable in r) give the bound.

At an index s″ > s the same pairings, with the Moser and Kato–Ponce inequalities applied to the top norms of the
coefficients, give the differential inequality of the statement. Its last term comes from the parabolic equation. The
coefficients b′, c and e lie in H^(s″) only, so pairing the first equation at index s″ + 1 must move one derivative onto
α: |⟨α, c α⟩_(H^(s″+1))| ≤ ‖α‖_(H^(s″+2)) ‖c α‖_(H^(s″)), with ‖c α‖_(H^(s″)) ≤ C (‖c‖_(H^(s″)) ‖α‖_(L^∞) + ‖c‖_(L^∞)
‖α‖_(H^(s″))), and Young's inequality against the gain c0 ‖α‖²_(H^(s″+2)) leaves C m_(s″)² ‖α‖²_(L^∞); likewise b′·∂_S α,
with ‖α‖_(W^(1,∞)), and e·(ϖ, q), with ‖(ϖ, q)‖_(L^∞), which must be paired so in any case, (ϖ, q) lying in H^(s″) only.
The hyperbolic part needs no such term: it is paired at index s″, where C m_(s″) ω_s 𝒴^(1/2) suffices.

Existence, by the Faedo–Galerkin method. Let P_L be the L²(S³)-orthogonal projection onto the eigenfunctions of the
Laplacian with eigenvalue at most L(L + 2), and for the covector q onto those of the Hodge Laplacian on 1-forms. The
eigenspaces are SO(4)-invariant, so P_L commutes with the Laplacian and with the Lie derivative along every Killing
field, which is what X^I means on q. Solve the first equation for ∂_r α (dividing by p), and seek α_L and (ϖ, q)_L in the
range of P_L with ∂_r α_L = P_L[…] and P_L[𝒮 A0 ∂_r (ϖ, q)_L] = P_L[…] (the symmetrized second equation, ∂_r α_L in it),
with the data of the lemma projected by P_L. This is a linear system of ordinary differential equations in r for finitely
many coefficients, whose matrix P_L 𝒮 A0 P_L is positive definite on the range (𝒮 A0 > 0) and continuous in r, the other
coefficients and the forcing terms being integrable in r, so Picard iteration gives a unique absolutely continuous
solution on [a, b1]. The test functions of the argument above, X^(I*) X^I applied to α_L or to (ϖ, q)_L, lie in the range
of P_L, so the projection drops out of each tested equation (⟨P_L G, f⟩ = ⟨G, f⟩ for f in the range), and the energy
identities are those above, with one addition: the commutator [X^I, 𝒮 A0] ∂_r (ϖ, q)_L needs ‖∂_r (ϖ, q)_L‖_(H^(s−1)),
which testing the projected second equation with X^(I′*) X^(I′) ∂_r (ϖ, q)_L, |I′| = 0, …, s − 1 in turn, bounds by C
(‖(ϖ, q)_L‖_(H^s) + ‖∂_r α_L‖_(H^(s−1)) + ‖F_J‖_(H^(s−1))) (𝒮 A0 > 0; the commutators are of lower order in I′). So the
bound holds for (α_L, (ϖ, q)_L) uniformly in L; a weak-* limit as L → ∞ solves [[eq:data-linear]] and obeys it.

Uniqueness follows from the energy estimate at index 0, applied to the difference of two solutions whose left side is
finite. For such a difference α lies in L² H^(s+2) with ∂_r α in L² H^s, and (ϖ, q) in L^∞ H^s with ∂_r (ϖ, q) in L²
H^(s−1), by the equations; so at index 0 every pairing of the two energy identities is defined and absolutely continuous
in r, which at index s it need not be. The index-0 estimate commutes no derivative and needs only the L^∞ and W^(1,∞)
norms of the coefficients and ∫ ‖∂_r (𝒮 A0)‖_(L^∞) dr, all bounded by M_s; with zero forcing and data it gives zero. ∎

**Proposition {#prop:exact-correction}** (The exact correction.) Let the stage data be those of [[lem:stage-data]] with
N ≥ K + 3, and (γ, κ) the data of g_app on Σ. For λ ≤ λ0 there is U on Σ, U = 0 on r < v_start − τ0, with 𝒞(γ_U, κ_U) =
0 on Σ and sup_r ‖∂_r^j U(r)‖_(H^s(S³)) ≤ C_(j,s) λ^(N−2−j).

*Proof.* Write 𝒞(γ_U, κ_U) = 𝒞(γ, κ) + 𝔏 U + 𝒬(U), 𝔏 the linearisation ([[lem:constraints-evolution]]) and 𝒬 the
remainder, quadratic in (U, ∂U, ∂ ∂_S α), with coefficients involving at most two derivatives of γ and one of κ, hence
of size at most C λ⁻¹. 𝒞(γ, κ) = O(λ^(N−2)) with all its angular derivatives (its profiles vanish below order N − 2 by
[[lem:gauge-hierarchy]], and angular derivatives of profiles cost nothing on Σ), and it vanishes on r < v_start − τ0.
(It is in fact O(λ^(N−1)) with all its angular derivatives: [[lem:gauge-hierarchy]] gives ∂_θ D^(N−1) = 0, so the phase
part λ^(N−2) (du) ∂_θ D^(N−1) of ∂D(g_app) vanishes and ∂D = O(λ^(N−1)), while Ric^H(g_app) = O(λ^N). The order gained
is not used, and N ≥ K + 3 is kept.) The ρ-component is linear in ∂_r α and in the angular second derivatives of α, with
coefficients depending on α algebraically (the scalar curvature of γ + α dr dr contains no (∂_r α)²), and the
J-component is linear in ∂(ϖ, q) with coefficients depending on α algebraically. Recall

    ‖U‖_(X_s) = sup_r (‖α‖_(H^(s+1)) + ‖(ϖ, q)‖_(H^s)) + ‖α‖_(L² H^(s+2)) + ‖∂_r α‖_(L² H^s),

the left side of [[lem:linear-evolution]] with the ∂_r α the first equation gives.

Iterate: U_(i+1) solves, with zero data at r = a, the linear system [[eq:data-linear]] whose principal coefficients are
frozen at U_i, as is the whole coefficient f of ∂_r α in the J-equation, f(γ, κ; α, ϖ, q), evaluated at U_i and
multiplying ∂_r α_(i+1). (It depends on α and on (ϖ, q), so the terms q_ϑ ∂_r α and α ∂_r α of J's remainder are not
left among the forcing terms; in the contraction the extra forcing term (f(U_i) − f(U_(i−1))) ∂_r α_i is at most C
λ^(N−2) ‖U_i − U_(i−1)‖_(X_(s_1)) in L² H^(s_1).) Its forcing terms are −𝒞(γ, κ) and the remaining terms, at least
quadratic and evaluated at U_i. Fix s_1 > 3/2 + 4 and s := s_1 + 2. At U = 0 the coefficients are those of
[[lem:constraints-evolution]]; frozen at U_i they change by at most C λ⁻¹ ‖U_i‖_X, ∂_r α_i entering M_s only through ∫
‖∂_r (𝒮 A0)‖_(L^∞) dr ≤ C (1 + ‖U_i‖_(X_(s_1))). So while ‖U_i‖_(X_s) ≤ 2 C_0 λ^(N−2), the hypotheses of
[[lem:linear-evolution]] hold at the indices s_1 and s with constants independent of λ, for λ small and N ≥ 4.
[[lem:linear-evolution]] at index s keeps the iterates in the ball of radius 2 C_0 λ^(N−2) of X_s, and at index s_1
gives ‖U_(i+1) − U_i‖_(X_(s_1)) ≤ C λ^(N−3) ‖U_i − U_(i−1)‖_(X_(s_1)) (the difference of the frozen coefficients
multiplies U_i, estimated in the higher norm), a contraction. Bounded in X_s and contracting in X_(s_1), the iterates
converge to a solution in X_s; this is the scheme of Kato and Majda for quasilinear symmetric hyperbolic systems
([[rem:std-iteration]]; [AO14, Section 4.1, p. 19], [DS23, Section 4], [AG22, p. 1]: boundedness in a high norm and
contraction in a low norm), and the parabolic component obeys the same estimates. Uniqueness holds in the ball of radius
2 C_0 λ^(N−2) of X_s, by the difference estimate.

U = 0 on r < v_start − τ0. There 𝒞(γ, κ) vanishes, and where U_i vanishes so do the quadratic terms at U_i; so for every
r1 < v_start − τ0 the system for U_(i+1) has zero forcing terms on [a, r1] and zero data at r = a, and
[[lem:linear-evolution]] on [a, r1], whose bound there involves the forcing terms on [a, r1] alone, gives U_(i+1) = 0 on
[a, r1]. By induction from U_0 = 0 every iterate, and so the limit, vanishes there. The r-derivatives follow from the
equations, each ∂_r of a coefficient costing at most λ⁻¹.

Smoothness (persistence of regularity). The coefficients and forcing terms of each step are smooth in the angles when
the previous iterate is, so by [[lem:linear-evolution]] at every index the iterates U_i are smooth, by induction. At an
index s″ > s the bound of [[lem:linear-evolution]] is linear in the top norms, those of the coefficients (functions of
α) entering linearly by the Moser and Kato–Ponce inequalities with factors depending only on the X_s bound. With ℰ_i(r)
the X_(s″) norm of U_i on [a, r] it reads

    ℰ_(i+1)(r) ≤ Ξ_0 + Ξ_1 (∫_a^r ℰ_i²)^(1/2),

with Ξ_1 uniform in i. Indeed, by the tame form of [[lem:linear-evolution]] the forcing terms enter in L² H^(s″), and
the weight built from ‖∂_r α_(i+1)‖_∞ and ‖∂_r (ϖ, q)_(i+1)‖_∞, bounded in L²(a, b1), enters through the Cauchy–Schwarz
inequality, ‖∂_r (𝒮 A0)‖_∞ entering Gronwall's exponent; a forcing term carrying ∂_r α_i would put ℰ_i(r) itself on the
right, which is why the coefficient of ∂_r α is frozen. The term ‖m_(s″) ω_∞‖_(L²(a, r)) of the tame bound changes
neither the rate of Ξ_0 nor the uniformity of Ξ_1: ω_∞ ≤ C ‖U_(i+1)‖_(X_(s_1)) ≤ C λ^(N−2) in the ball; the lower-order
coefficients b′, c, e, c′, f′, c″ are those of [[lem:constraints-evolution]] at U = 0, independent of U and smooth in the
angles uniformly in λ; and the others are functions of U_i entering linearly and changing by C λ⁻¹ ‖U_i‖, so that m_(s″)
≤ C (1 + λ⁻¹ ℰ_i), and the term is at most C λ^(N−2) (b1 − a)^(1/2) + C λ^(N−3) (∫_a^r ℰ_i²)^(1/2): a part of Ξ_0
proportional to λ^(N−2) and a part of Ξ_1 at most C λ^(N−3) ≤ C, as N ≥ 4.

By induction, ℰ_i(r) ≤ Ξ_0 Σ_(k≥0) Ξ_1^k ((r − a)^k/k!)^(1/2) for every i, with no smallness. For ℰ_0 = 0 this holds,
and if it holds for ℰ_i, then Minkowski's inequality gives (∫_a^r ℰ_i²)^(1/2) ≤ Ξ_0 Σ_k Ξ_1^k (∫_a^r (r′ − a)^k/k!
dr′)^(1/2) = Ξ_0 Σ_k Ξ_1^k ((r − a)^(k+1)/(k + 1)!)^(1/2), so ℰ_(i+1)(r) ≤ Ξ_0 + Ξ_0 Σ_(k≥0) Ξ_1^(k+1) ((r −
a)^(k+1)/(k + 1)!)^(1/2), which is the claim for i + 1; the series converges by the ratio test. So the limit U lies in
X_(s″) for every s″. Ξ_0 is proportional to λ^(N−2) (the forcing term 𝒞(γ, κ) and the low norms are) and Ξ_1 is bounded
independently of λ, so ‖U‖_(X_(s″)) ≤ C_(s″) λ^(N−2) for every s″, which with the equations gives the stated rate at
every s and j. So U is smooth for λ ≤ λ0, λ0 independent of s″. [[thm:uniform-existence]] needs only k + 1 = 7
derivatives of the data in any case. ∎

**Remark {#rem:data-rates}** (Numerical observation.) On the data of the stage-0 approximant, in the class of fields of
(r, ϑ) invariant under T² and both reflections, the linear system of [[lem:linear-evolution]] was solved numerically by a
pseudo-spectral discretisation in the angle, marched in r, with a forcing term of size λ⁴ (the size λ^(N−2) at N = 6).
Over the last halving of λ, from 1/32 to 1/64, the suprema in r of norms of H² type of U, ∂_r U and ∂_r² U decreased as
λ^4.00, λ^3.99 and λ^3.00, within the rates λ^(N−2−j) of [[prop:exact-correction]] (the first r-derivative costing
nothing). With a trace of the waves on the spheres put in, which creates a coefficient of order 1/λ
([[lem:constraints-evolution]] (b)), the first r-derivative cost a factor λ⁻¹. The iteration of the proof, principal
coefficients frozen, contracted with first ratios 6.8 × 10⁻³, 5.8 × 10⁻⁴ and 3.5 × 10⁻⁵ at λ = 1/8, 1/16 and 1/32. These
are floating-point observations, and no proof uses them.

### Proof of the theorem {#sec:data-proof}

*Proof of [[thm:data]].* Take the stage data of [[lem:stage-data]] with N := K + 3 and U of [[prop:exact-correction]].
Put g on Σ: the spatial part γ + α dr dr, the lapse and shift of G(X, u/λ), ∂_τ of the spatial part fixed by κ + ϖ Π + q
⊗ dr + dr ⊗ q, and ∂_τ of the lapse and shift fixed by D(g) = 0 (as in [[sec:data-identities]], "What the theorem asks").
Then the constraints hold exactly ([[prop:exact-correction]]), D = 0, and, by [[eq:data-constraint-gauge]], ∂_τ D = 0 on
Σ for the solution of Ric^H = 0 with these data.

For w := g − g_app on Σ, g_app the fixed-phase form of the statement: G(X, u/λ) and that form differ by O(λ^(N+1)) in
scaled norms ([[sec:approximant]]), within C λ^K since N + 1 > K, so it suffices to bound w′ := g − G(X, u/λ). The
spatial part of w′ and ∂_τ of it are U and combinations of U and its tangential derivatives. The components w′_(τ ·) do
not vanish but are algebraic in U: g and G(X, u/λ) have the same lapse and the same shift β, and their spatial parts
differ by α dr ⊗ dr, so w′_(τi) = α (dr)_i dr(β) and w′_(ττ) = α dr(β)², with β bounded with its derivatives in the
scaled norms. And ∂_τ w′_(τ ·) solves the linear relation D(g) − D(G(X, u/λ)) = −D(G(X, u/λ)) = O(λ^(N−1)) with
invertible coefficient. So, each derivative costing at most λ⁻¹, Data(w′) ≤ C λ⁻¹ λ^(N−2) = C λ^K, hence Data(w) ≤ C λ^K:
(E4). The data are smooth ([[prop:exact-correction]]) and invariant under T² and both reflections: the construction
commutes with the symmetries, by the uniqueness in [[lem:linear-evolution]], [[prop:exact-correction]] and the stage
equations, Pol⁺ being equivariant. They equal the seed's data on Σ ∩ {r < v_start − τ0}. ∎

### The main theorem, items 1–5 {#sec:data-assembly}

Items 1–5 of [[thm:main]] follow from [[thm:approximant]], [[thm:data]] and [[thm:uniform-existence]] with
[[lem:gauge-propagation]]; the proof is in [[sec:main-proof]].
