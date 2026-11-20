### Block A1. Additions to the section on the planar shear at an axis (chapter 81)

The text of this block goes into [[sec:class-planar-shear]] after [[rem:class-leaf-numerics]]; the Placement section
gives the position. It compares the planar shears of two states leaf by leaf, along one arc from the axis, and gives the
bound of [[lem:class-leaf-differences]] (a) on the larger ball 𝔅′.

In the coordinates (z, y) of [[lem:class-leaf]] near a point p of axis 2 on a slice, a *state* is V = (g, p_A, Θ_A) on
𝒰_(2δ), smooth and G-invariant, with g Lorentzian and the slice spacelike for g. It has *bounds* (M, c) if the C² norms
of g and the C¹ norms of p_A and Θ_A on 𝒰_(2δ) are at most M, if A3, B3 and det₂ of [[lem:class-leaf]] are at least 1/M,
and if |p_A^Σ| ≥ c and p_A(∂_z) ≥ c on 𝒰_(2δ), p_A^Σ the spatial part of p_A. Its H_L is H_L[Θ_A] of
[[lem:class-leaf-differences]], with TΣ_L there the γ3-orthogonal complement in TM3 of p_A^Σ, so that H_L is a function
of position; its leaves are the solutions h(·; z0) of [[eq:class-leaf-volterra]] with h(0) = z0, and σ[V](x) is the
planar shear [[eq:class-shear-leaf]] of the leaf through x, with |p_A^Σ| for |∇_M3 u| and p_A(n) for n(u). For x on the
slice put r_x := |y(x)|. The *arc* of V through x is the part {(h(t; z0), t y(x)/r_x) : 0 ≤ t ≤ r_x} of the leaf through
x, z0 its axis point. For two states, |U − V| at a point is the sum of the absolute values of the differences of g, ∂g,
p_A and Θ_A there.

**Lemma {#lem:class-leaf-arc}** (Two states compared along one arc.) Let U and V be states with bounds (M, c). There are
r_1 > 0 and C, depending only on M, c, p and the chart, such that for δ ≤ r_1:

(a) the leaves of V through the axis points z0 with |z0 − z(p)| < δ are graphs over the disc {|y| ≤ δ}, with |h′(r; z0)|
≤ C r, |∂_(z0)h′(r; z0)| ≤ C r and |∂_(z0)h(r; z0) − 1| ≤ ½; every x ∈ 𝒰_(δ/2) lies on exactly one of them; and the same
holds for U;

(b) for x ∈ 𝒰_(δ/2), with f(t) := |U − V| at the point of the arc of V through x at radius t,

    |σ[U](x) − σ[V](x)| ≤ C (f(r_x) + r_x⁻² ∫_0^(r_x) t f(t) dt + (∫_0^(r_x) t f(t)² dt)^(1/2));  {#eq:class-leaf-arc}

(c) if D is a G-invariant set such that the arc of V through every point of D ∩ 𝒰_(δ/2) lies in D, then ‖σ[U] −
σ[V]‖_(L²(D∩𝒰_(δ/2))) ≤ C ‖U − V‖_(L²(D∩𝒰_δ)).

Only the values of U − V on the arcs of V enter (b) and (c), and only bounds of U elsewhere.

*Proof.* (a) Write G_X(r, z, q) := r H_X(z, r)/a_L^X(r, z, q) − E_L^X(r, z, q) for a state X, with a_L^X and E_L^X the
functions of [[lem:class-leaf]] (c) for the metric γ3 of X, evaluated with h := z and h′ := q, and H_X the H_L of X at
the point (z, r). By the proof of [[lem:class-volterra]], on a neighbourhood of (0, z(p), 0) whose size depends only on
(M, c), |G_X(r, z, 0)| ≤ C_0 r, |∂_z G_X| ≤ C_1 and |∂_q G_X| ≤ C_2 (r + |q|), and the map 𝒯 of that proof, with the
parameter z0, is a contraction with constant ½ on {q ∈ C([0, r_1]) : sup |q| ≤ δ_q} for r_1 and δ_q small; its fixed
point q = h′ satisfies |q(r)| ≤ C_0 r. 𝒯 depends continuously differentiably on (q, z0), so the fixed point does, and π
:= ∂_(z0) h′ solves r π(r) = ∫_0^r (∂_z G_X (1 + ∫_0^ρ π) + ∂_q G_X π) dρ. Hence sup_[0,r] |π| ≤ C_1 r/2 (1 + r
sup_[0,r] |π|) + ¼ sup_[0,r] |π|, which gives |π| ≤ C r for r ≤ r_1 small, and |∂_(z0) h − 1| ≤ ∫_0^r |π| ≤ C r² ≤ ½. So
for fixed y the map z0 ↦ h(|y|; z0) is increasing with derivative in [½, 3/2], and its range over |z0 − z(p)| < δ
contains {|z − z(p)| < δ/2} when C δ² ≤ δ/4, as |h(r; z0) − z0| ≤ C_0 r²/2. This gives the foliation of 𝒰_(δ/2).

(b) Let L̂ be the leaf of V through x, z0 its axis point, ĥ := h_V(·; z0), q̂ := ĥ′, and let h̃ := h_U(·; z0) be the
leaf of U from the same axis point, q̃ := h̃′, x′ := (h̃(r_x), y(x)). On the leaf through a point the leaf equation
gives k_r = H_L − k_φ, so by [[eq:class-shear-leaf]], [[lem:class-gauss]] (c) and the formulas for ν^r and k_φ in
[[lem:class-leaf]] (c), σ[X] at a point x̄ of the leaf h of X is 𝔖_X(x̄, h′(r_x̄)/r_x̄), where 𝔖_X(x̄, s) is a smooth
function of the point and of s, built from H_X, γ3 and its first derivatives, p_A and K_Σ at x̄: k_φ = ν^r/r + ½ ν(log
B3) with ν^r/r = −(C3 + A3 s)/ (det₂^(1/2) N_L), N_L² = B3 + D3 r² + 2C3 r² s + A3 r² s², at s = h′/r, and the leaf's
unit tangent e_r depends only on h′. So, for |s| ≤ C, |∂_s 𝔖_X| + |∂_x̄ 𝔖_X| ≤ C and |𝔖_U − 𝔖_V|(x̄, s) ≤ C |U − V|(x̄).
Write

    σ[U](x) − σ[V](x) = (σ[U](x) − σ[U](x′)) + (𝔖_U(x′, q̃/r) − 𝔖_U(x, q̃/r)) + (𝔖_U(x, q̃/r) − 𝔖_U(x, q̂/r))
                       + (𝔖_U(x, q̂/r) − 𝔖_V(x, q̂/r)),      r := r_x.

The leaves of U foliate by (a), and σ[U](h_U(r; z̄), y) = 𝔖_U((h_U(r; z̄), y), ∂_r h_U(r; z̄)/r) has a z̄-derivative
bounded by C, since |∂_(z̄) h_U| ≤ 3/2 and |∂_(z̄) h_U′|/r ≤ C by (a); as ∂_(z̄) h_U ≥ ½, the first two terms are at
most C |x − x′| = C |δh(r)|, δh := h̃ − ĥ. The third is at most C |δq(r)|/r, δq := q̃ − q̂, and the fourth at most C
f(r). Now r δq(r) = ∫_0^r (G_U(ρ, h̃, q̃) − G_U(ρ, ĥ, q̂) + g(ρ)) dρ with g(ρ) := (G_U − G_V)(ρ, ĥ(ρ), q̂(ρ)). By the
proof of [[lem:class-volterra]], E_L^X = (C3 r + A3 q) N_L²/det₂ − q + r B̃_X/a_L^X with B̃_X smooth in (r, z, q) and in
the 1-jet of γ3; the first part vanishes identically at r = q = 0, so its difference for the two metrics at a point is
at most C (r + |q|) times the difference of their 1-jets there, and so is that of the second part. With |q̂| ≤ C ρ this
gives |g(ρ)| ≤ C ρ f(ρ). Put D(r) := sup_[0,r] |δq|; then |δh(ρ)| ≤ ρ D(ρ), and r |δq(r)| ≤ ∫_0^r (C_1 ρ D(ρ) + C_2 (ρ +
C ρ) D(ρ) + |g(ρ)|) dρ ≤ C r² D(r) + ∫_0^r |g|. So D(r) ≤ C r D(r) + sup_(ρ≤r) ρ⁻¹ ∫_0^ρ |g|, and for C r_1 ≤ ½, by the
Cauchy–Schwarz inequality ρ⁻¹ ∫_0^ρ t f ≤ (∫_0^ρ t f²)^(1/2)/√2,

    D(r) ≤ C (∫_0^r t f² dt)^(1/2),      |δh(r)| ≤ C r (∫_0^r t f² dt)^(1/2),
    |δq(r)|/r ≤ C D(r) + r⁻² ∫_0^r |g| ≤ C ((∫_0^r t f² dt)^(1/2) + r⁻² ∫_0^r t f dt).

Together these give [[eq:class-leaf-arc]].

(c) Use the coordinates (z0, y) of (a) for V on 𝒰_(δ/2): x = (h_V(|y|; z0), y), with Jacobian ∂_(z0) h_V ∈ [½, 3/2]. As
D is G-invariant and closed under the arcs of V, for each z0 the set of y with x ∈ D ∩ 𝒰_(δ/2) is a disc {|y| < R(z0)}
or {|y| ≤ R(z0)}; the arc points of its points lie in D, and in 𝒰_δ, since they are within C δ² of x in z. For the
average 𝒜f(r) := r⁻² ∫_0^r t f(t) dt = ∫_0^1 s f(s r) ds and every R, Minkowski's inequality and ∫_0^R f(s r)² r dr =
s⁻² ∫_0^(sR) f² t dt give ‖𝒜f‖_(L²(r dr; [0,R])) ≤ ‖f‖_(L²(r dr; [0,R])), and ∫_0^R (∫_0^r t f² dt) r dr ≤ R² ∫_0^R t f²
dt. Square [[eq:class-leaf-arc]], integrate over the disc in y and then over z0, and change variables back: the L² norms
of invariant functions over 𝒰_δ and over the (z, y)-coordinates are comparable, the orbits of K1 having length 2π ρ1 ∈
[π ρ1(p), 3π ρ1(p)] there. ∎

**Lemma {#lem:class-leaf-tame}** (The planar shear on the ball 𝔅′.) In the setting of [[lem:class-leaf-differences]],
let U ∈ 𝔅′ with 𝒩_k(U) < ∞. Then ‖∂^α(σ[U] − σ[ů])‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U) for |α| ≤ k, with C depending only on 𝔅′, δ and
k.

*Proof.* Put Z := U − ů and U_s := ů + s Z, s ∈ [0, 1]; U_s ∈ 𝔅′, the ball being convex, and 𝒩_k(U_s) = s 𝒩_k(U). By
[[lem:sobolev]] at the order k − 4 ≥ 2 the C² norms of the first-order variables of U_s − ů are at most C 𝒩_(k−1)(U)
≤ C on 𝔅′, so every U_s has bounds (M, c) in the sense of [[lem:class-leaf-arc]] uniform in s, and its leaves foliate.
For a leaf h_s := h_(U_s)(·; z0) the bound of step (3) of the proof of [[lem:class-planar-shear]], which uses the leaf
equation [[eq:class-leaf-cartesian]] only and constants depending on sup |∂h_s|, sup |∂²h_s| and the 1-jet of γ3, gives
‖h_s‖_(H^(j+2)(𝔻)) ≤ C (‖H_L[U_s]‖_(H^j(𝔻′)) + ‖γ3^s‖_(H^(j+1)) + 1) for j ≤ k on nested discs 𝔻 ⊂ 𝔻′, so ‖h_s −
h̊‖_(H^(k+2)) ≤ C (1 + 𝒩_k(U)) on the disc. The derivative ζ := ∂_s h_s solves the leaf equation linearised at h_s, L_s
ζ = (∂_s H_L[U_s]) − (∂_s 𝔪_s)(h_s), 𝔪_s the mean-curvature map of [[eq:class-leaf-cartesian]] for γ3^s, with ζ = 0 at
the axis; L_s is uniformly elliptic on the disc with the axis interior ([[lem:class-leaf]] (b)), with principal
coefficients smooth functions of (y, h_s, ∂h_s) and lower coefficients of (y, h_s, ∂h_s, ∂²h_s), and the right side is
linear in the 1-jet of Z with coefficients smooth in (y, h_s, ∂h_s). Apply [[lem:class-interior-regularity]] with j = 0
to ∂^β ζ, |β| ≤ k, on nested discs, as in step (3) of [[lem:class-planar-shear]]: the commutator [∂^β, L_s] ζ is a sum
of products of a derivative of order i ≥ 1 of the coefficients and a derivative of order |β| + 2 − i of ζ, and by
[[thm:std-gn-moser]] (1) on the disc (after Stein's extension) its L² norm is at most C (‖ζ‖_(H^(|β|+1)) + ‖h_s −
h̊‖_(H^(|β|+2)) ‖ζ‖_(C²) + ‖ζ‖_(C²)), the C² and C¹ norms of the coefficients being bounded on 𝔅′. By induction on |β|,
with ‖ζ‖_(C²) ≤ C 𝒩_(k−1)(U) by [[lem:sobolev]] and the case of lower order, ‖ζ‖_(H^(k+2)) ≤ C (𝒩_k(U) + (1 + 𝒩_k(U))
𝒩_(k−1)(U)) ≤ C 𝒩_k(U). The derivatives transverse to the disc, in z0 and in τ, are bounded in the same way by
differentiating the linearised equation, as in the proof of [[lem:class-leaf-differences]] (a), and the shift of the
foliation enters as there. So ‖∂^α ∂_s σ[U_s]‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U), σ[U_s] being a smooth function of h_s, ∂h_s,
H_L[U_s] and the 1-jet of γ3^s by
(b) of [[lem:class-leaf-arc]]; integrating in s gives the bound. ∎

### Block A2. Additions to the section on Kato's iteration (chapter 81)

The text of this block goes into [[sec:class-kato]] after [[rem:class-kato-model]]. It solves [[eq:class-kato-system]]
when the forcing term at a time depends on the solution over an interval of earlier times and is controlled only in
space-time norms. Such forcing terms arise when a non-local term is computed on the leaves of hypersurfaces that are not
the slices of the time: the fixed-time hypotheses (F1)–(F2) then fail, while their integrated forms hold
([[rem:class-kato-memory]]).

*Space-time norms.* Keep the setting of this section, and let J = [a, b] be an interval. H^σ(J) is the space of
functions on J × R^d with all derivatives ∂_t^j ∂_x^β, j + |β| ≤ σ, in L²(J × R^d), with the norm of the sum of their
squared L² norms. 𝒳^σ(J) is the space of u with ∂_t^j u ∈ L^∞(J; H^(σ−j)) for 0 ≤ j ≤ σ, the derivatives in the sense of
distributions, and ⟦u⟧_(σ,J) := Σ_(j≤σ) ess sup_J ‖∂_t^j u‖_(H^(σ−j)). For u ∈ 𝒳^σ(J) and j ≤ σ − 1, ∂_t^j u is
Lipschitz into H^(σ−j−1), hence continuous, and its value at every t lies in H^(σ−j), with norm at most ⟦u⟧_(σ,J), a
closed ball of H^(σ−j) being weakly closed; and ‖u‖_(H^σ(J)) ≤ (b − a)^(1/2) ⟦u⟧_(σ,J). For f ∈ H^σ(J) and i ≤ σ − 1,
∂_t^i f and ∂_t^(i+1) f lie in L²(J; H^(σ−1−i)), so ∂_t^i f is continuous into H^(σ−1−i), with

    ‖∂_t^i f(t) − ∂_t^i f(t′)‖_(H^(σ−1−i)) ≤ |t − t′|^(1/2) ‖f‖_(H^σ([t′,t])),
    sup_J ‖∂_t^i f‖_(H^(σ−1−i)) ≤ ((b − a)^(−1/2) + (b − a)^(1/2)) ‖f‖_(H^σ(J)),                  {#eq:class-trace}

by ∂_t^i f(t) − ∂_t^i f(t′) = ∫_(t′)^t ∂_t^(i+1) f and the Cauchy–Schwarz inequality, and by averaging the first bound
over t′ ∈ J. If u ∈ 𝒳^σ([a, b]) and u′ ∈ 𝒳^σ([b, c]) have ∂_t^j u(b) = ∂_t^j u′(b) for j ≤ σ − 1, the function equal to
u on [a, b] and to u′ on [b, c] lies in 𝒳^σ([a, c]): its distributional derivatives of order j ≤ σ are the piecewise
ones, since those of order j − 1 are continuous at b. *Extension beyond b.* For an integer N ≥ 1 let c_1, …, c_N solve
Σ_l c_l (−1/l)^i = 1, 0 ≤ i ≤ N − 1, a Vandermonde system with the distinct nodes −1/l, and for b − a ≥ m > 0 and t ∈
(b, b + m] put (E_b u)(t) := Σ_l c_l u(b − (t − b)/l), and E_b u := u on [a, b]. Each term takes the values of u on [b −
m, b]; its j-th derivative is l^(−j) (∂_t^j u)(b − (t − b)/l); so for N = σ + 1, E_b maps 𝒳^σ([a, b]) into 𝒳^σ([a, b +
m]) with ⟦E_b u⟧_(σ,[a,b+m]) ≤ C_E ⟦u⟧_(σ,[a,b]), C_E := Σ_l |c_l|, the derivatives of order at most σ − 1 matching at
b, and ‖E_b u‖_(H^σ([b,b+m])) ≤ C_E ‖u‖_(H^σ([b−m,b])), ‖E_b u‖_(L²([b,b+m]×R^d)) ≤ C_E ‖u‖_(L²([b−m,b]×R^d)).

**Lemma {#lem:class-mixed-product}** (Products at one time.) Let σ1, σ2 ≥ σ ≥ 0 be integers with σ1 + σ2 − σ > d/2.

(a) ‖f g‖_(H^σ) ≤ C ‖f‖_(H^(σ1)) ‖g‖_(H^(σ2)), C depending only on d, σ1, σ2.

(b) Let Φ be as in [[lem:class-composition]], v ∈ 𝒳^s(J) with ⟦v⟧_(s,J) ≤ 𝔐, and 0 ≤ a ≤ s − 1. At every t ∈ J, ∂_t^a
[Φ(t, ·, v(t))] = (∂_t^a Φ)(t, ·, v(t)) + R_a(t) with ‖R_a(t)‖_(H^(s−a)) ≤ C(𝔐), R_0 := 0, and multiplication by (∂_t^a
Φ)(t, ·, v(t)) is bounded on H^σ, σ ≤ s, with norm at most C(𝔐); R_a depends only on ∂_t^i v, i ≤ a, and its bound on
bounds of these.

*Proof.* (a) For |γ| ≤ σ, ∂^γ(fg) is a sum of terms ∂^(γ1) f ∂^(γ2) g with |γ1| + |γ2| ≤ σ; put α := σ1 − |γ1| ≥ 0 and β
:= σ2 − |γ2| ≥ 0, so α + β > d/2. Choose p, q ∈ [2, ∞] with 1/p + 1/q = 1/2: p = ∞, q = 2 if α > d/2; p = 2, q = ∞ if
β > d/2; otherwise 1/p := 1/2 − α/d + λ and 1/q := 1/2 − β/d + λ with 2λ := (α + β)/d − 1/2 > 0, for which 0 < 1/p, 1/q
≤ 1/2 since β − α ≤ d/2 and α − β ≤ d/2. On every unit cube Q of the lattice, [[thm:std-bh17-embedding]] (for finite
exponents, α − d/2 ≥ −d/p) and [[thm:std-bh-embedding]] (for the exponent ∞) give ‖F‖_(L^p(Q)) ≤ C ‖F‖_(H^α(Q)) and
‖G‖_(L^q(Q)) ≤ C ‖G‖_(H^β(Q)), C independent of Q by translation. With F := ∂^(γ1) f and G := ∂^(γ2) g, Hölder's
inequality on each cube and summation give ‖FG‖² ≤ Σ_Q C ‖F‖²_(H^α(Q)) ‖G‖²_(H^β(Q)) ≤ C ‖F‖²_(H^α) sup_Q ‖G‖²_(H^β(Q))
≤ C ‖f‖²_(H^(σ1)) ‖g‖²_(H^(σ2)).
(b) By the chain rule ∂_t^a [Φ(t, x, v)] − (∂_t^a Φ)(t, x, v) is a sum, with coefficients depending on a, of terms
(∂_t^(a0) ∂_u^l Φ)(t, x, v)[∂_t^(a1) v, …, ∂_t^(al) v] with l ≥ 1, every a_i ≥ 1 and a0 + a1 + … + al = a. The product
of the l factors lies in H^(s−a1−…−al) ⊂ H^(s−a) by (a) applied l − 1 times, as (s − a1) + (s − a2) − (s − a1 − a2) =
s > d/2 and s − a ≥ 1, with the bound C 𝔐^l. A function Ψ(t, x, v) with Ψ smooth as Φ multiplies H^σ, σ ≤ s, with norm
at most C(𝔐): Ψ(t, x, 0) has bounded derivatives of every order, and ‖Ψ(t, ·, v) − Ψ(t, ·, 0)‖_(H^s) ≤ C(𝔐) by
[[lem:class-composition]] (b), so (a) with σ1 = s and σ2 = σ applies to it. ∎

**Lemma {#lem:class-kato-history}** (The linear problem with forcing in a space-time space and a history.) Let m > 0,
J_− := [t1 − m, t1], J := [t1, t2] and J_+ := [t1 − m, t2], with t2 − t1 ≤ T0. Let v ∈ 𝒳^s(J_+) with ⟦v⟧_(s,J_+) ≤ 𝔐,
𝐀^μ := A^μ(t, x, v), f ∈ H^s(J_+), and w̄ ∈ 𝒳^s(J_−) a solution of 𝐀^0 ∂_t w̄ + 𝐀^j ∂_j w̄ = f on J_−. There is exactly
one w ∈ C(J_+; L²) equal to w̄ on J_− that solves 𝐀^0 ∂_t w + 𝐀^j ∂_j w = f on J_+ with ∂_t w ∈ C(J_+; L²). It lies in
𝒳^s(J_+), and for t ∈ J, with E_s of [[lem:class-kato-linear]]:

(i) E_s(t; w)^(1/2) ≤ e^(C(t−t1)) (E_s(t1; w)^(1/2) + C (t − t1)^(1/2) ‖f‖_(H^s([t1,t]))), C depending on d, s, c0, 𝔐
and bounds of order s for the A^μ;

(ii) for 1 ≤ j ≤ s and almost every t ∈ J, ‖∂_t^j w(t)‖_(H^(s−j)) ≤ B_j (‖w(t)‖_(H^s) + Σ_(i<j) ‖∂_t^i
f(t)‖_(H^(s−1−i))), B_j depending on d, s, c0, bounds of order s for the A^μ and a bound for ‖∂_t^i v‖_(L^∞(H^(s−i))), i
≤ j − 1;

(iii) ‖∂_t^i f(t)‖_(H^(s−1−i)) ≤ ‖∂_t^i f(t1)‖_(H^(s−1−i)) + (t − t1)^(1/2) ‖f‖_(H^s([t1,t])) for i ≤ s − 1.

*Proof.* By [[eq:class-trace]], f ∈ C(J_+; H^(s−1)). On J, v satisfies the hypotheses of [[lem:class-kato-linear]], with
‖v(t)‖_(H^s) ≤ 𝔐 and Lipschitz constant 𝔐 into H^(s−1). For ε ∈ (0, 1] the mollified f_ε := J_ε f lies in C(J; L²) with
f_ε(t) ∈ H^s and sup_t ‖f_ε(t)‖_(H^s) ≤ C ε⁻¹ sup_t ‖f(t)‖_(H^(s−1)) < ∞, so part (b) of that lemma gives a solution w_ε
on J with w_ε(t1) = w̄(t1) and E_s(t; w_ε)^(1/2) ≤ e^(C(t−t1)) (E_s(t1; w̄)^(1/2) + C ∫_(t1)^t ‖f‖_(H^s)), J_ε not
increasing the norms. By part (a) of that lemma, sup_t ‖w_ε − w_(ε′)‖ ≤ C ∫_J ‖f_ε − f_(ε′)‖ → 0, since f_ε → f in C(J;
L²). As in step (4) of its proof the limit w lies in C(J; L²), w(t) ∈ H^s with the bound (i) (the integral of ‖f‖_(H^s)
being at most (t − t1)^(1/2) ‖f‖_(L²([t1,t]; H^s)) ≤ (t − t1)^(1/2) ‖f‖_(H^s([t1,t]))), w_ε → w in C(J; H^(s−1)) by
[[eq:class-interpolation]], and passing to the limit in w_ε(t) = w̄(t1) + ∫_(t1)^t (𝐀^0)⁻¹ (f_ε − 𝐀^j ∂_j w_ε) shows
that w solves the equation with ∂_t w ∈ C(J; L²). Uniqueness is part (a) of [[lem:class-kato-linear]].

(ii) On J, ∂_t w = (𝐀^0)⁻¹ (f − 𝐀^j ∂_j w). Suppose that ∂_t^i w ∈ L^∞(J; H^(s−i)) for i < j, with the bounds (ii).
Differentiating j − 1 times in the sense of distributions, ∂_t^j w is a sum of terms ∂_t^a[(𝐀^0)⁻¹] ∂_t^b f and
∂_t^a[(𝐀^0)⁻¹] ∂_t^(b1)[𝐀^i] ∂_t^(b2) ∂_i w with a + b = a + b1 + b2 = j − 1. Write each factor ∂_t^a[Ψ(v)] as in
[[lem:class-mixed-product]] (b), a multiplier plus R_a ∈ H^(s−a); ∂_t^b f ∈ H^(s−1−b) and ∂_t^(b2) ∂_i w ∈ H^(s−1−b2).
By [[lem:class-mixed-product]] (a), every product of factors in H^(s−a), H^(s−b1) and H^(s−1−b2) lies in
H^(s−1−a−b1−b2) = H^(s−j), each exponent being at least s − j and the sum of any two exceeding the target by at least
s > d/2; likewise for the terms with f. The bound (ii) follows, with only ∂_t^i v, i ≤ j − 1, entering. The same
products with one order less show that ∂_t^j w is continuous into H^(s−j−1) for j ≤ s − 1, and ∂_t^s w ∈ L^∞(J; L²). So
w|_J ∈ 𝒳^s(J). On J_− the same identities hold for w̄, with the same v and f. At t1, w(t1) = w̄(t1), and by induction on
j ≤ s − 1 the formula gives ∂_t^j w(t1) = ∂_t^j w̄(t1), all its ingredients ∂_t^i v, ∂_t^i f (i ≤ j − 1) and ∂_t^i w (i
< j) being continuous at t1 into H^(s−j−1). So w ∈ 𝒳^s(J_+), by the concatenation property. (iii) is [[eq:class-trace]].
∎

Fix m > 0, T0 > 0, a reference path u_* ∈ 𝒳^(s+1)([−2m, T0]) and ρ > 0, and put 𝔐_ρ := ⟦u_*⟧_(s+1,[−2m,T0]) + ρ. For t̄
∈ (−2m, T0] let 𝒫_t̄ := {u ∈ 𝒳^s([−2m, t̄]) : ⟦u − u_*⟧_(s,[−2m,t̄]) ≤ ρ}; every u ∈ 𝒫_t̄ has ⟦u⟧_(s,[−2m,t̄]) ≤ 𝔐_ρ.
Let F assign to every t̄ and every u ∈ 𝒫_t̄ a function F(u) ∈ H^s([−m, t̄]) such that, for −m ≤ t1 < t2 ≤ t̄ and u, u′ ∈
𝒫_t̄, with constants C_F and L:

(M0) if u = u′ on [−2m, t], then F(u) = F(u′) on [−m, t]; and F(u|_([−2m,t])) = F(u) on [−m, t];
(M1) ‖F(u)‖_(H^s([t1,t2])) ≤ C_F (t2 − t1 + m)^(1/2);
(M2) ‖F(u) − F(u′)‖_(L²([t1,t2]×R^d)) ≤ L ‖u − u′‖_(L²([t1−m,t2]×R^d)).

A *solution on [−m, t̄]* is a u ∈ 𝒫_t̄ with ∂_t u ∈ C([−m, t̄]; L²) and A^0(t, x, u) ∂_t u + A^j(t, x, u) ∂_j u = F(u)
on [−m, t̄]. The number m is the *memory*.

**Theorem {#thm:class-kato-memory}** (Kato's iteration with memory.) Assume (M0)–(M2).

(a) There are η ∈ (0, 1] and T* ∈ (0, m], depending only on d, s, c0, bounds of order s for the A^μ, ρ, m, 𝔐_ρ, C_F and
L, such that every solution on [−m, t1], 0 ≤ t1 < T0, with ⟦u − u_*⟧_(s,[−2m,t1]) ≤ η ρ extends to a solution on [−m,
min(t1 + T*, T0)]. Two solutions on [−m, t̄] that agree on [−2m, t1] agree. If u is a solution on [−m, t] for every t <
T2 ≤ T0, with ⟦u − u_*⟧_(s,[−2m,t]) ≤ η ρ for t < T2, then u extends to a solution on [−m, min(T2 + T*/2, T0)].

(b) (Stability.) Assume moreover that u_* satisfies A^0(t, x, u_*) ∂_t u_* + A^j(t, x, u_*) ∂_j u_* = F(u_*) + R on [−m,
T0], with R ∈ H^s([−m, T0]), and

(M1′) ‖F(u) − F(u_*)‖_(H^s([t1,t2])) ≤ C′ ‖u − u_*‖_(H^s([t1−m,t2])) for u ∈ 𝒫_t̄ and −m ≤ t1 < t2 ≤ t̄.

There are ε0 > 0 and C, depending on the quantities of (a), on C′ and on T0, such that every solution h on [−m, 0] with
δ := ⟦h − u_*⟧_(s,[−2m,0]) + ‖R‖_(H^s([−m,T0])) ≤ ε0 extends to a solution u on [−m, T0], with ⟦u − u_*⟧_(s,[−2m,T0]) ≤
C δ.

*Proof.* (a) *Uniqueness.* Let u, ũ be solutions on [−m, t̄] that agree on [−2m, t1]. z := u − ũ solves the linear
problem with the coefficients at u and the forcing term F(u) − F(ũ) − (A^μ(u) − A^μ(ũ)) ∂_μ ũ, continuous into L² by
[[eq:class-trace]]; ‖∂ũ‖_(L^∞) ≤ C_S 𝔐_ρ, and z = 0 before t1. By [[lem:class-kato-linear]] (a), the Cauchy–Schwarz
inequality and (M2), e(t) := ‖z(t)‖² satisfies e(t) ≤ C (t − t1) ∫_(t1)^t (L² + C) e for t ≥ t1, so e = 0.

*Existence.* Let u be a solution on [−m, t1] with ⟦u − u_*⟧_(s,[−2m,t1]) ≤ η ρ, η to be fixed, and h := u. Put u^0 :=
u_* + E_(t1)(h − u_*) on [−2m, t1 + m], with E_(t1) the extension beyond t1 (N = s + 1), so that ⟦u^0 − u_*⟧_s ≤ C_E η ρ
≤ ρ/2 for η ≤ 1/(2C_E), and let J := [t1, t1 + T], T ≤ min(T*, T0 − t1). For n ≥ 0 let u^(n+1) := h on [−2m, t1] and, on
J, the solution of [[lem:class-kato-history]] with v := u^n, f := F(u^n) on [t1 − m, t1 + T] and w̄ := h on [t1 − m,
t1]; by (M0), F(u^n) = F(h) on [−m, t1], so w̄ solves the linear equation there. Suppose u^n ∈ 𝒫_(t1+T), u^n = h on
[−2m, t1]. Then u^(n+1) ∈ 𝒳^s([−2m, t1 + T]) by [[lem:class-kato-history]], and w := u^(n+1) − u_* solves on J the
linear problem with the coefficients 𝐀^μ := A^μ(u^n), the data h(t1) − u_*(t1) and the forcing term f_w := F(u^n) − 𝐀^μ
∂_μ u_*, to which [[lem:class-kato-history]] applies (with w̄ := h − u_*). By [[lem:class-mixed-product]] at each time,
‖𝐀^μ ∂_μ u_*‖_(H^s([t1,t])) ≤ (t − t1)^(1/2) C(𝔐_ρ), u_* ∈ 𝒳^(s+1); with (M1), ‖f_w‖_(H^s([t1,t])) ≤ C (T + m)^(1/2). By
(i), with C_A := sup |A^0| at |u| ≤ C_S 𝔐_ρ, ‖w(t)‖_(H^s) ≤ c0^(−1/2) e^(CT) (C_A^(1/2) η ρ + C T^(1/2) (T + m)^(1/2)).
On [t1 − m, t1] the equation for h gives f_w = A^μ(h) ∂_μ(h − u_*), and ∂_t^i f_w is continuous into H^(s−1−i) for i ≤ s
− 1; so by [[lem:class-mixed-product]], ‖∂_t^i f_w(t1)‖_(H^(s−1−i)) ≤ C(𝔐_ρ) ⟦h − u_*⟧_(s,[t1−m,t1]) ≤ C η ρ. By
(ii) for w and (iii),

    ⟦w⟧_(s,J) ≤ B (η ρ + T^(1/2) (T + m)^(1/2)),

B depending only on the quantities of (a). Choose η ≤ 1/(2B) and then T* so small that B T*^(1/2) (T* + m)^(1/2) ≤ ρ/2:
then ⟦u^(n+1) − u_*⟧_(s,[−2m,t1+T]) ≤ ρ, and u^(n+1) ∈ 𝒫_(t1+T). *Contraction.* For n ≥ 1, δ^(n+1) := u^(n+1) − u^n
vanishes on [−2m, t1] and solves on J the linear problem with the coefficients at u^n, data 0 and the forcing term
F(u^n) − F(u^(n−1)) − (A^μ(u^n) − A^μ(u^(n−1))) ∂_μ u^n, whose L²(J × R^d) norm is at most (L + C) T^(1/2) sup_J ‖δ^n‖
by (M2). [[lem:class-kato-linear]] (a) and the Cauchy–Schwarz inequality give sup_J ‖δ^(n+1)‖ ≤ C T sup_J ‖δ^n‖ ≤ ½
sup_J ‖δ^n‖ for T* small. *Limit.* So u^n → u in C([−2m, t1 + T]; L²). For each j ≤ s, ∂_t^j u^n is bounded in
L^∞(H^(s−j)), the dual of L¹(H^(j−s)); its weak-* limit points are ∂_t^j u, so ∂_t^j u^n converges weak-* to it, and ⟦u
− u_*⟧_s ≤ ρ: u ∈ 𝒫_(t1+T). By [[eq:class-interpolation]], u^n → u in L^∞(H^(s−1)); by (M2), F(u^n) → F(u) in L²(J ×
R^d). Passing to the limit in u^(n+1)(t) = h(t1) + ∫_(t1)^t (A^0(u^n))⁻¹ (F(u^n) − A^j(u^n) ∂_j u^(n+1)) gives the same
identity for u, with an integrand continuous into L², F(u) ∈ H^s([−m, t1 + T]) being continuous into L². So u is a
solution on [−m, t1 + T]. *Continuation.* With t1 := max(T2 − T*/2, 0), the solution on [−m, t1 + T*] given by the first
part agrees with u on [−2m, T2) by uniqueness.

(b) By (a), the solution u with history h exists on a maximal interval [−m, T_m) ∩ [−m, T0] on which ⟦u − u_*⟧_s ≤ η ρ.
Let τ1 < τ2 < T_m with τ2 − τ1 ≤ θ, θ ≤ m to be fixed, and z := u − u_*. z solves the linear problem with coefficients
at u and the forcing term f_z := F(u) − F(u_*) − R − (A^μ(u) − A^μ(u_*)) ∂_μ u_*, and ‖f_z‖_(H^s([τ1,τ])) ≤ C
(‖z‖_(H^s([τ1−m,τ])) + ‖R‖_(H^s([τ1,τ]))) by (M1′) and [[lem:class-mixed-product]] at each time. Put X(τ) :=
⟦z⟧_(s,[−2m,τ]); then ‖z‖_(H^s([τ1−m,τ])) ≤ (2m)^(1/2) X(τ). By the two equations, f_z + R = A^μ(u) ∂_μ z on [τ1 − m,
τ1], so, as in (a), ‖∂_t^i f_z(τ1)‖_(H^(s−1−i)) ≤ C (X(τ1) + ‖R‖_(H^s([−m,T0]))) for i ≤ s − 1, by [[eq:class-trace]]
for R. Then (i)–(iii) give, for almost every τ ∈ [τ1, τ2],

    Σ_(j≤s) ‖∂_t^j z(τ)‖_(H^(s−j)) ≤ B′ (X(τ1) + θ^(1/2) X(τ2) + ‖R‖_(H^s([−m,T0]))),

so X(τ2) ≤ B′ X(τ1) + B′ θ^(1/2) X(τ2) + B′ δ, and for B′ θ^(1/2) ≤ ½, X(τ2) ≤ 2B′ (X(τ1) + δ). Over the N := ⌈T0/θ⌉
intervals of length θ this gives X ≤ (4B′)^N δ =: C δ on [−2m, T_m). For C δ ≤ η ρ/2, (a) excludes T_m ≤ T0. ∎

**Remark {#rem:class-kato-memory}** (Why the hypotheses are integrated.) In the application ([[sec:loc-t5]]) the
forcing term at a point x of the slice {t = t̄} is computed on the hypersurface through x of a second foliation, tilted
against the slices, from the state on an arc of that hypersurface from the axis to x, whose other points have earlier
times. Its value on a slice is then a trace of a function that is controlled in space-time: the square of its space-time
norm is the integral, over the second foliation, of the squares of norms on its hypersurfaces, which the slice estimates
of [[lem:class-leaf-differences]] and [[lem:class-leaf-arc]] control. This is
(M1) and (M2); the fixed-time hypotheses (F1) and (F2) would ask for bounds on each slice {t = t̄} itself, which the
slice estimates do not give. [[thm:class-kato-memory]] uses only (M0)–(M2).

### Block B. Further dust families at the axes (chapter 83)

The text of this block is a new section of [[ch:localised-data]], placed after the section on perturbations that reach
the axes; the Placement section gives the position.

### Further dust families at the axes {#sec:loc-t5}

The developments of the preceding sections carry two dust families adapted to the cones, with the phases v and u, and
further families only where their densities vanish near the points at which a cone meets an axis. This section admits
further families whose densities are nonzero at such points. At an axis the gradient of every phase of the class is a
multiple of dv or of du ([[lem:class-phase-axis]]), so a further family meets the axis generator of each cone in one of
two ways: it *crosses* the cone there, transversally, or it is *tangent* to it, its rays running in the cone. A family
crosses one cone along its axis generator and is tangent to the other ([[lem:loc-t5-dichotomy]]). We prove the
development for any number of families that carry density only where they cross a cone and not at the corner circles of
the axes ([[thm:loc-t5]]), and, for families that carry density where they are tangent to a cone, a development on a
region that avoids the axis near the points concerned ([[prop:loc-t5-cut]]). The closure of the expansion at an axis
needs, for each family, the leaves of its own null hypersurfaces; we compute them, for each family, on the slices of a
time function of its own, whose sections of the cones are that family's sections, and we bend the evolution time so that
every arc used lies in the past of its end point. The forcing term then has a memory, and the Cauchy problem is solved
by [[thm:class-kato-memory]].

*The construction of the preceding section.* We use the following objects of the development of data that reach the axes
[[pending:t3-setting]]: a rectangle Q1 = [0, u1] × [0, v1] of the double-null coordinates (u, v) of the background, with
Q1^η := [0, u1 + η] × [0, v1 + η] in the set where the background is defined; a chart time τ0 = Φ(u, v) with Φ_u, Φ_v >
0 on Q1^η and a number s* with max_(Q1) τ0 < s* and F ∩ {τ0 ≤ s*} ⊂ Q1^η, F := {u ≥ 0, v ≥ 0} and P its complement; a
G-equivariant chart x of the slices of τ0, in which class metrics near the background are smooth; the data extended past
u1 and v1 to the faces of Q1^η, with the constraints solved along the extension; the formal solution Û, a smooth
G-invariant state equal to the background state Ů on {τ0 ≤ τ_init}, τ_init < Φ(0, 0), carrying the formal jets on ∂F :=
(𝒞_out ∪ 𝒞_in) ∩ Q1^η, with ‖Û − Ů‖_(C^(k+3)) ≤ C ε; its metric Ĝ as the reference of the wave gauge; and a space-time
cut-off ξ with ξ = 1 on a neighbourhood of F ∩ {τ0 ≤ s*}, of the strip of P along ∂F ∩ {τ0 ≤ s*} and of ∂F ∩ supp(Û − Ů)
∩ {τ0 ≤ s*}. Here k ≥ 6 and m ≥ m0(k) are the orders of that construction, ε is the size of the data in C^m, and
constants C depend on the background, Q1, η, s* and k.

#### Further families and their type at an axis {#sec:loc-t5-families}

**Definition {#def:loc-t5-family}** (Further families.) A *further family* A ∈ {3, …, N_f} is given by a smooth
G-invariant eikonal ů_A of the background g0 without caustics on a neighbourhood 𝒩 of Q1^η × S³, with g0⁻¹dů_A future
directed, and by data on ∂F: a phase U_A and a density q_A ≥ 0, smooth and G-invariant on each face, with U_A − ů_A and
q_A of size at most ε in C^m. The family *crosses* 𝒞_out at a point where g0⁻¹(du, dů_A) ≠ 0, and 𝒞_in where g0⁻¹(dv,
dů_A) ≠ 0; the open sets of the faces where it crosses are its *crossing sets*. Let 𝒦_A := supp q_A ⊂ ∂F. The data
satisfy:

(F-a) 𝒦_A does not meet a neighbourhood, in ∂F, of the circles S ∩ (axis 1 ∪ axis 2) in which the corner sphere S meets
the axes;
(F-b) every point of 𝒦_A ∩ 𝒞_out lies in the crossing set of 𝒞_out, and every point of 𝒦_A ∩ 𝒞_in in that of 𝒞_in;
(F-c) at the points of 𝒦_A ∩ S the transverse derivatives of the phase and the density computed on the two faces agree
([[lem:loc-t5-jets]]).

The family is of *ingoing type* at axis i if dů_A is a multiple of dv at the points of axis i in 𝒩, and of *outgoing
type* if it is a multiple of du there. Its *tangency set* at axis i is the closed axis generator 𝒞_in ∩ axis i ∩ Q1^η in
the first case and 𝒞_out ∩ axis i ∩ Q1^η in the second; it contains the corner circle S ∩ axis i.

**Lemma {#lem:loc-t5-dichotomy}** (Crossing and tangency at the axes.) Let 𝒩 ∩ axis i be connected. A further family is
of ingoing type or of outgoing type at axis i. If it is of ingoing type, it crosses 𝒞_out at every point of its axis-i
generator, and at the points of its tangency set g0⁻¹(dv, dů_A) = 0, the rays of ů_A through them being the generators
of 𝒞_in on the axis; likewise for outgoing type with the faces exchanged. So by (F-b) a further family carries density
at a point where a cone meets an axis only if it crosses that cone there, and its density vanishes on a neighbourhood of
its tangency sets in ∂F.

*Proof.* At a point of axis i, dů_A lies in span(du, dv) by [[lem:class-phase-axis]] and is null and nonzero, so it is a
multiple of du or of dv, g0⁻¹(du, du) = g0⁻¹(dv, dv) = 0 and g0⁻¹(du, dv) ≠ 0 being the only possibilities on that span.
The two lines meet only at 0, and dů_A is continuous and nonzero on the connected set 𝒩 ∩ axis i, so it stays on one
line. For ingoing type, g0⁻¹(du, dů_A) = λ g0⁻¹(du, dv) ≠ 0 at the axis points of 𝒞_out, and g0⁻¹(dv, dů_A) = λ g0⁻¹(dv,
dv) = 0 at those of 𝒞_in; there g0⁻¹dů_A is a multiple of g0⁻¹dv, which is tangent to the axis and to 𝒞_in, and its
integral curves are the generators of 𝒞_in in the axis. The last claim: 𝒦_A is closed, contains no point of the compact
tangency set by (F-b), and so has positive distance from it. ∎

So the tangency sets are exactly where a family meets a cone with the cone's own orientation, the case in which two
families are not angularly separated at the axis ([[prop:class-separation]] (c)).

**Lemma {#lem:loc-t5-tubes}** (The tubes avoid the tangency sets.) Let A be a further family and 𝒦′ ⊂ ∂F a compact
G-invariant set that satisfies (F-a) and (F-b). There are a neighbourhood 𝒲 of the tangency sets of A in Q1^η × S³ and
ε_t > 0 such that, for every smooth future causal vector field P within ε_t of g0⁻¹dů_A in C⁰ on Q1^η × S³, no integral
curve of P from a point of 𝒦′ into F meets 𝒲 ∩ F.

*Proof.* Let p lie in the tangency set at axis i, of ingoing type say; then p = (u_p, 0) on the axis, u_p ∈ [0, u1 + η].
By [[lem:loc-t5-dichotomy]] the integral curve of P̊ := g0⁻¹dů_A through p, followed backwards, is the axis generator of
𝒞_in; it reaches the corner circle and then, past it, points with u < 0 in the neighbourhood of Q1^η where the
background is defined, after a parameter length bounded uniformly in u_p. On future causal vectors du and dv are
nonnegative, so along a future causal curve u and v do not decrease, a curve that starts in F stays in F, and a point x
of F lies on a curve from a point of 𝒦′ exactly when the backward curve through x leaves F through a point of 𝒦′. By
continuous dependence on the initial point and on the field on a compact parameter interval, for x near p and P near P̊
in C⁰ the backward curve through x stays within any given distance of the backward curve through p until it reaches u <
0, so it leaves F at a point of ∂F near the closed segment of the axis generator of 𝒞_in from p to the corner circle: a
point of 𝒞_in near its axis generator, or a point of 𝒞_out near the corner circle. Neither is in 𝒦′, by (F-b) and
[[lem:loc-t5-dichotomy]] on 𝒞_in and by (F-a) on 𝒞_out. Compactness of the tangency set gives 𝒲 and ε_t. ∎

The hypothesis (F-a) cannot be weakened to the vanishing of the density on the corner circles alone: a family of ingoing
type at axis i whose density is nonzero at points of 𝒞_out arbitrarily close to the corner circle has, by the proof
above, integral curves that come arbitrarily close to its tangency set on 𝒞_in.

*Carrying a family near its tube.* For a further family A let 𝒦_A′ ⊂ ∂F be a compact G-invariant neighbourhood of 𝒦_A in
∂F satisfying (F-a) and (F-b), let 𝒯̊_A be the union of the integral curves of P̊_A := g0⁻¹dů_A in F ∩ Q1^η from 𝒦_A′,
and let ξ_A be a smooth G-invariant function on space-time, equal to 1 on a neighbourhood of 𝒯̊_A and of 𝒦_A′ in ∂F,
whose support meets ∂F only in the crossing sets and does not meet the set 𝒲 of [[lem:loc-t5-tubes]] for 𝒦′ := 𝒦_A′;
this is possible since 𝒯̊_A ∩ ∂F = 𝒦_A′ (a curve from a point of 𝒞_out into F does not meet 𝒞_in again, and conversely)
and by [[lem:loc-t5-tubes]]. In the system below the transports (Aug2)–(Aug4) of family A are multiplied by ξ_A and
completed by (1 − ξ_A) A^0(Ů) ∂_τ of the difference from the background's family A, (dů_A, □_(g0) ů_A, 0), as 𝔄_ξ does
for the whole system. Family A enters the other equations only through q_A, which vanishes off its tube as long as the
tube lies in {ξ_A = 1}. The phase data of family A near its tangency sets, where the face is characteristic for it and
the jets of its phase on the face are not determined without further conditions, are then never used.

**Lemma {#lem:loc-t5-jets}** (Cone data and jets with further families.) (a) The constraints of [[prop:loc-cones]] on
𝒞_out and of [[lem:loc-cone-in]] on 𝒞_in, with the stress T := q_in dv ⊗ dv + q_out du ⊗ du + Σ_A q_A du_A ⊗ du_A, are
linear ordinary differential equations along the generators, axis generators included, whose further sources on 𝒞_out
are T(∂_v, ∂_v) − q_in = Σ_A q_A (∂_v U_A)² and T(∂_v, ∂_ϑ) = Σ_A q_A ∂_v U_A ∂_ϑ U_A, and on 𝒞_in T(∂_u, ∂_u) − q_out =
Σ_A q_A (∂_u U_A)²; the solutions equal the background's on every generator on which the free data, q_in, q_out and all
q_A equal the background's.

(b) Near every point of the crossing set of 𝒞_out the transverse derivatives ∂_u^j u_A, ∂_u^j Θ_A and ∂_u^j q_A on 𝒞_out
of a solution with the data are determined recursively, as smooth functions on the face, by the eikonal equation, the
Raychaudhuri equation and the transport (Aug4), from the derivatives of the metric functions of order at most j and the
tangential derivatives of the data; at order j the derivatives of order j of the further families enter the jets of the
metric of order j + 1 only. The same holds on 𝒞_in with u and v exchanged.

*Proof.* (a) On 𝒞_out, ∂_v u_A = ∂_v U_A and ∂_ϑ u_A = ∂_ϑ U_A are tangential, and dv(∂_v) = du(∂_v) = du(∂_ϑ) =
dv(∂_ϑ) = 0, which gives the sources. They are smooth invariant functions on the face, and T(∂_v, ·) restricted to the
sections is a smooth invariant 1-form, ∂_ϑ U_A being odd at the axis generators. With these sources the proof of
[[prop:loc-cones]] and of [[lem:loc-cone-in]], through the axis generators [[pending:t3-cone-data]], applies unchanged:
the sources are known on the face and enter the two equations as inhomogeneous terms. (b) In the double-null form
[[eq:loc-double-null]], g^(uu) = g^(uϑ) = g^(vv) = 0, so on 𝒞_out the eikonal equation reads 2g^(uv) ∂_u u_A ∂_v U_A +
2g^(vϑ) ∂_v U_A ∂_ϑ U_A + g^(ϑϑ) (∂_ϑ U_A)² = 0, linear in ∂_u u_A with the coefficient 2g^(uv) ∂_v U_A = 2g⁻¹(du,
du_A), nonzero on the crossing set; applying ∂_u^(j−1) gives ∂_u^j u_A linearly with the same coefficient. Likewise
P_A(q_A) = −Θ_A q_A and P_A(Θ_A) = −|∇²u_A|² − Ric(P_A, P_A) are linear in ∂_u q_A and ∂_u Θ_A with the coefficient
P_A^u = g^(uv) ∂_v U_A. In the equations of [[lem:loc-cone-jets]] differentiated j − 1 times in u, which fix the
u-derivatives of order j of the metric, the stress enters through its u-derivatives of order j − 1, which hold those of
q_A of order j − 1 and of u_A of order j; by the three equations above these are fixed by the metric's u-derivatives of
order at most j − 1 and by the data. So the recursion of [[lem:loc-cone-jets]], through the axis generators
[[pending:t3-jets]], with these equations added, determines all jets. ∎

On the crossing sets near 𝒦_A the jets of family A are therefore smooth, also at the axis generators of the cone it
crosses; with (F-c) at S, [[lem:loc-cone-borel]] extends them, and the formal solution Û carries family A on a
neighbourhood of 𝒦_A′, with q̂_A supported near 𝒦_A and ξ_A = 1 there. We take Û so, with ‖Û − Ů‖_(C^(k+3)) ≤ C ε.

#### A closure time for each family {#sec:loc-t5-times}

Near axis i let ρ := ρ_i be the distance to it in the chart x (ρ2 = |(x3, x4)| near axis 2, ρ1 = |(x1, x2)| near axis
1), let χ be smooth on [0, ∞), equal to 1 on [0, ½] and to 0 on [1, ∞), and put T_o(v) := Φ(0, v) and T_i(u) := Φ(u, 0),
the restrictions of τ0 to the two faces, which are increasing. Let A be a further family of ingoing type at axis i. Near
the axis-i generator of 𝒞_out, away from the corner circle, ∂_v U_A ≠ 0, as ∂_v ů_A ≠ 0 there ([[lem:loc-t5-dichotomy]])
and U_A is within ε of ů_A; so the sections {U_A = c} of 𝒞_out, its *A-sections*, are there the graphs v = V_A(c, ϑ) of
smooth functions, even about the axis, and g_A := T_o(v) − T_o(V_A(U_A(v, ϑ), ϑ_i)), ϑ_i the angle of axis i, is a
smooth function on 𝒞_out, even about the axis and zero on it. So g_A = Ĝ_A ρ² with Ĝ_A smooth, and we extend Ĝ_A to
space-time as a function of (v, ϑ). Let ψ_A be a smooth function of (u, v), equal to 1 near the points (0, v) of the
axis-i generator where ξ_A ≠ 0 near the axis, and to 0 near u ≥ u_A and near v ≤ v_A, where 0 < u_A and v_A > 0 are
chosen so that ξ_A = 0 near the corner circle on {v ≤ 2v_A} ([[def:loc-t5-family]] (F-a)). For outgoing type the same
with 𝒞_in, U_A(u, ϑ), T_i and the faces exchanged. For the adapted families put t_v := t_u := τ0. For a further family
put

    t_A := τ0 − Σ_i χ(ρ_i/δ_*) ψ_A Ĝ_A^(i) ρ_i²,      τ := τ0 + K Σ_i χ(ρ_i/δ_*) ρ_i²,  {#eq:loc-t5-times}

the sums over the axes at which A is carried, Ĝ_A^(i) the function above for axis i.

**Lemma {#lem:loc-t5-times}** (The closure times and the evolution time.) Let K ≥ 1 + max_(A,i) sup |Ĝ_A^(i)|, the
supremum over the support of ψ_A within distance 1 of axis i. There is δ_1 > 0 such that for δ_* ≤ δ_1:

(a) τ and every t_A are time functions for every Lorentzian metric within ε1 of g0 in C⁰ on Q1^η × S³, ε1 > 0 fixed; (τ,
x) and every (t_A, x) are charts; and all of them equal τ0 where ρ1, ρ2 ≥ δ_*;
(b) on the face that A crosses at axis i, within ρ_i < δ_*/2 and where ψ_A = 1, t_A is constant on every A-section; the
sections of the faces by the slices of t_v = t_u = τ0 are the double-null spheres of the data;
(c) along every curve z = h(r) in a slice of t_A or of τ0, from the axis, with |h′(r)| ≤ C_L r and r < δ_*/2, τ is
strictly increasing, C_L being a constant of [[lem:class-leaf-arc]] (a) for the states used below;
(d) 0 ≤ τ − t_A ≤ m := (K + max sup |Ĝ_A^(i)|) δ_*² and 0 ≤ τ − τ0 ≤ K δ_*².

K is fixed by the data, uniformly for ε ≤ ε0, and then δ_*.

*Proof.* (a) With ρ := ρ_i, |d(χ(ρ/δ_*) ψ_A Ĝ_A ρ²)| ≤ C (δ_*⁻¹ δ_*² + δ_* + δ_*²) ≤ C δ_* on {ρ ≤ δ_*}, and likewise
for the bend of τ, C depending on K and on the C¹ norms of Ĝ_A and ψ_A. dτ0 is timelike for g0 on the compact set Q1^η ×
S³ with a margin (Φ_u, Φ_v > 0 and g0^(uv) < 0, g0^(uu) = g0^(vv) = 0), so for δ_* small τ and t_A are time functions
for the metrics within ε1 of g0, and ∂t_A/∂τ0 = 1 + O(δ_*) in the chart (τ0, x). (b) On the face, where χ = ψ_A = 1,
t_A = T_o(v) − g_A = T_o(V_A(U_A, ϑ_i)), a function of U_A alone. For τ0 the faces' sections are {v = const} and {u =
const}, the data's double-null spheres [[pending:t3-setting]]. (c) On a slice of t_A, τ = t_A + f with f := χ(ρ/δ_*)(ψ_A
Ĝ_A + K) ρ² near axis i, as the bend of τ and the term of t_A use the same χ. For r < δ_*/2, χ = 1, and along the curve,
with ∂_ρ of the invariant smooth function ψ_A Ĝ_A of order ρ,

    d/dr f(h(r), r) = 2 (ψ_A Ĝ_A + K) r + r² (∂_z(ψ_A Ĝ_A) h′ + ∂_ρ(ψ_A Ĝ_A)) ≥ 2 r − C r³ > 0

for δ_* small, as ψ_A Ĝ_A + K ≥ 1. For the slices of τ0 the same holds with ψ_A Ĝ_A replaced by 0. (d) f ≥ 0 and f ≤
(K + sup |Ĝ_A|) δ_*². ∎

So, for every family A and every point x within δ_*/2 of an axis, the arc of a leaf through x in the slice {t_A =
t_A(x)} lies in {τ ≤ τ(x)} and in {τ ≥ τ(x) − m}.

**Lemma {#lem:loc-t5-faces}** (The face sections are leaves of each family.) Let A be a family that crosses a face at
its axis-i generator, within the set where (b) of [[lem:loc-t5-times]] holds, or an adapted family, and let V be a state
on a slice of t_A, near the background state in C², whose p_A and Θ_A on the face section S of that slice are the formal
values and whose metric has the formal 1-jet there. Then near each axis point of S, S is V's A-leaf through it. The
sides of S in the slice near that point, the one in F and the one in P, are unions of V's A-leaves.

*Proof.* By the leaf criterion of the preceding section [[pending:t3-leaf-criterion]], S is V's A-leaf near the point if
p_A annihilates TS and Θ_A = −tr_(TS) p_A(∇_X Y), the trace of the second fundamental form of S along g⁻¹p_A computed
with V's metric. The formal phase ũ_A restricted to the face is U_A, constant on S by [[lem:loc-t5-times]] (b), so
p̃_A = dũ_A annihilates TS. ũ_A is an eikonal to infinite order on the face, so ∇²ũ_A(g⁻¹dũ_A, ·) = 0 there; TS is a
spacelike subspace of the orthogonal complement of the null vector g⁻¹dũ_A not containing it, hence a screen in the
sense of [[prop:class-structure]] (b), and Θ̃_A = □ũ_A = tr_(TS) ∇²ũ_A = −tr_(TS) dũ_A(∇_X Y), as X(Y ũ_A) = 0 for X, Y
tangent to S. Both sides depend only on (p_A, Θ_A) and the 1-jet of the metric on S. The leaves of V foliate a
neighbourhood of the axis point ([[lem:class-leaf-arc]] (a)), so a leaf that meets one side of S near it stays on that
side. ∎

#### The system with memory {#sec:loc-t5-system}

Let 𝔄_ξ(U) = F̃ be the system of the preceding section [[pending:t3-setting]], with the following three changes, and let
us use the time τ of [[eq:loc-t5-times]] and the chart (τ, x).

(i) For every family A, adapted or further, that is carried near axis i, within ρ_i < δ_*/4 the closure of (Aug3) is
S_A^ax of the proof of [[thm:class-stability]], with σ_A[U](x) the planar shear at x of the A-leaf through x of the
state U restricted to the slice {t_A = t_A(x)}, computed in the chart (t_A, x) as in [[lem:class-leaf-differences]];
S_A^ax is joined to the local closure S_A of (Aug3) by a partition of unity in ρ_i on δ_*/8 ≤ ρ_i ≤ δ_*/4, with ζ_A :=
1.
(ii) Further families are carried as described before [[lem:loc-t5-jets]], with the cut-offs ξ_A.
(iii) F̃ := 1_P 𝔄_ξ(Û), with 𝔄_ξ as changed by (i) and (ii).

In the first-order variables Z := U − Ů of Step 9 of the proof of [[thm:class-stability-off-axes]], and with ϒ as in the
preceding section, the system reads A^μ(x, Z) ∂_μ Z = F(Z), F(Z) := F̃ − (the remaining terms of 𝔄_ξ), and it has the
form [[eq:class-kato-system]] with A^0 ≥ c1 I [[pending:t3-setting]]. By [[lem:loc-t5-times]] (d) the value of F(Z) at a
point of {τ = t} depends on Z on {t − m ≤ τ ≤ t} only. We use [[thm:class-kato-memory]] with s := k, the time τ, the
memory m_A := 2m and the history at τ_init.

**Lemma {#lem:loc-t5-forcing}** (The forcing term.) For δ_* small and then ρ > 0 small, F satisfies (M0), (M1), (M2) and
(M1′) of [[thm:class-kato-memory]] with u_* := 0, s := k and the memory m_A, on the paths of the slab [τ_init − 2m_A,
τ_fin], τ_fin := s* + 1; the constants depend on the background, Q1, η, s*, k and δ_*.

*Proof.* Fix a path Z with ⟦Z⟧_(k) ≤ ρ on [τ_init − 2m_A, t̄], and let Z_e := E_t̄ Z be its extension beyond t̄ by the
operator of [[sec:class-kato]] (N = k + 1), U_e := Ů + Z_e. For x with τ(x) ≤ t̄, the arc through x used by σ_A lies in
{τ ≤ τ(x)} (the remark after [[lem:loc-t5-times]]), where U_e = U; so F(Z) on {τ ≤ t̄} does not depend on the extension,
and the value of F(Z) at a time t depends on Z on [t − m, t] only: this is (M0). *The slices of t_A.* For every t,
{t_A = t} is a slice of the chart (t_A, x), spacelike, and the change of chart (τ, x) ↦ (t_A, x) has derivatives bounded
with their inverses. By [[eq:class-trace]] in the chart (t_A, x), on an interval of t_A-length 1, the norm 𝒩_(k−1) of
U_e − Ů on {t_A = t} (all space-time derivatives of order at most k − 1 of the first-order variables) is at most C
‖Z_e‖_(H^k) over a slab of bounded thickness, hence at most C C_E ρ; for ρ small U_e lies, on every such slice, in the
ball 𝔅′ of [[lem:class-leaf-differences]] about Ů, and has bounds (M, c) in the sense of [[lem:class-leaf-arc]] uniform
in t, by [[lem:sobolev]]. *(M1′).* The local terms of F are smooth functions of (x, Z, ∂Z) of first order vanishing
outside a compact set where Z = 0 [[pending:t3-setting]]; their difference from those at Z = 0 is bounded in H^k([t1,
t2]) by C ‖Z‖_(H^k([t1,t2])), by [[lem:class-composition]] (b) in the five variables (τ, x) after the extension E_(t2).
For the closure of family A near axis i, [[lem:class-leaf-tame]] on each slice {t_A = t}, with ů := Ů, gives
‖∂^α(σ_A[U_e] − σ_A[Ů])‖_(L²(𝒰_δ∩{t_A=t})) ≤ C 𝒩_k(U_e − Ů; {t_A = t}), |α| ≤ k, with δ := δ_*/2. Squaring and
integrating over t ∈ [t1 − m, t2], by Fubini's theorem in the chart (t_A, x), the left sides give the square of the H^k
norm of σ_A[U] − σ_A[Ů] over the part of [t1, t2] × R⁴ within δ_*/4 of axis i, and the right sides at most C
‖Z_e‖²_(H^k([t1−m,t2+m])) ≤ C ‖Z‖²_(H^k([t1−2m,t2])). S_A^ax holds σ_A through ½ σ_A², and σ_A[Ů] is bounded with all
its derivatives; by [[cor:std-moser-product]] (1) in the variables (τ, x), with the bound of σ_A[U_e] − σ_A[Ů] in L^∞
given by the slice bound and [[lem:sobolev]], the difference of S_A^ax is bounded likewise; the partition of unity
has bounded derivatives. So ‖F(Z) − F(0)‖_(H^k([t1,t2])) ≤ C′ ‖Z‖_(H^k([t1−m_A,t2])). *(M1)* follows, as F(0) is smooth
with bounded derivatives and ‖Z‖_(H^k([t1−m_A,t2])) ≤ (t2 − t1 + m_A)^(1/2) ρ. *(M2).* The local terms are Lipschitz
pointwise. For two paths Z, Z′, [[lem:class-leaf-arc]] (c) on each slice {t_A = t}, with D the whole slice, gives
‖σ_A[U_e] − σ_A[U′_e]‖_(L²(𝒰_(δ/2)∩{t_A=t})) ≤ C ‖U_e − U′_e‖_(L²(𝒰_δ∩{t_A=t})); squaring, integrating over t and using
‖E_(t2) g‖_(L²([t2,t2+m])) ≤ C_E ‖g‖_(L²([t2−m,t2])) gives (M2) with the memory 2m = m_A. ∎

**Lemma {#lem:loc-t5-residual}** (The forcing term is smooth across the faces.) 𝔄_ξ(Û), with the closures of
[[sec:loc-t5-system]], vanishes to infinite order on ∂F ∩ {τ ≤ τ_fin}. Hence F̃ = 1_P 𝔄_ξ(Û) is smooth, and R := 𝔄_ξ(Ů)
− F̃ satisfies ‖R‖_(H^k([τ_init−m_A,τ_fin])) ≤ C ε.

*Proof.* The local parts of 𝔄_ξ(Û) vanish to infinite order on ∂F by the construction of Û [[pending:t3-jets]] and
[[lem:loc-t5-jets]]; so does the part of the closures of the adapted families computed on the slices of τ0, which is
that of the preceding section [[pending:t3-residual]]. Let A be a further family, carried near axis i, and x ∈ P with
d(x) := dist(x, ∂F) small and ρ_i(x) < δ_*/4. Then x lies near the face that A crosses at axis i, away from the corner
circle, where (b) of [[lem:loc-t5-times]] holds, and the slice {t_A = t_A(x)} meets that face near x in an A-section S.
Let û_A be the phase of Û's family A, with p̂_A = dû_A, a smooth extension of the formal phase, and let W be the state
(Ĝ, dû_A, θ_A) on the slice, θ_A(y) := −tr_(TΛ_y) dû_A(∇_X Y) with Λ_y the level set of û_A through y in the slice. By
the proof of the leaf criterion [[pending:t3-leaf-criterion]], which computes the mean curvature of a level set from
these quantities, the level sets of û_A near the axis are W's A-leaves; S is one of them. Since ∇²û_A(P̂_A, ·) = ½
d(Ĝ⁻¹(dû_A, dû_A)), and the inverse metric on the timelike plane orthogonal to TΛ_y has, in the basis (P̂_A, Q) with Q
in that plane, entries that are smooth and that put the factor Ĝ⁻¹(dû_A, dû_A) on ∇²û_A(Q, Q), the difference □_Ĝ û_A −
θ_A is a smooth function of (Ĝ, dĜ, dû_A, ∇²û_A) vanishing where Ĝ⁻¹(dû_A, dû_A) and its differential vanish; these
vanish to infinite order on ∂F near the crossing set, û_A being a formal eikonal there, and so does Θ̂_A − □_Ĝ û_A.
So |Û − W| = |Θ̂_A − θ_A| ≤ C_N d^N near ∂F for every N. The level sets of û_A in the slice foliate a neighbourhood of
the axis, ∂_z û_A being bounded below there; S is one of them; and the slice is transverse to the face. So the level set
through x lies within C d(x) of S, hence of ∂F, and so does the arc of W through x. [[lem:class-leaf-arc]] (b) with V :=
W and U := Û gives |σ_A[Û](x) − σ(û_A)(x)| ≤ C_N d(x)^N, σ(û_A)(x) := σ[W](x) the planar shear of the level set. For û_A
the identities of [[prop:class-structure]] (b) and (c), with [[eq:class-x]], hold up to smooth functions vanishing where
Ĝ⁻¹(dû_A, dû_A) and its differential vanish, so P̂_A(□_Ĝ û_A) − S_A^ax with σ(û_A) in place of σ_A vanishes to infinite
order on ∂F near x, the Ricci term being that of the formal solution. Hence the residual P̂_A(Θ̂_A) − S_A^ax(Û) is
O(d^N) for every N near ∂F. It is smooth on a two-sided neighbourhood of ∂F, Û being smooth and the leaves depending
smoothly on the point and on t ([[lem:class-leaf-arc]] (a) and step (4) of the proof of [[lem:class-planar-shear]]); a
smooth function that is O(d^N) for every N vanishes to infinite order on ∂F, by Taylor's formula in the normal
direction. This gives the first claim, and F̃ is smooth. For R: R = (𝔄_ξ(Ů) − 𝔄_ξ(Û)) + 1_F 𝔄_ξ(Û). The first term is
bounded in H^k by C ‖Û − Ů‖_(C^(k+1)) ≤ C ε, by the bounds of the proof of [[lem:loc-t5-forcing]] applied to the path Û
− Ů. On F, 𝔄_ξ(Û) = (𝔄_ξ(Û) − 𝔄_ξ(Ů)) + 𝔄_ξ(Ů), and 𝔄_ξ(Ů) is the residual of the gauge reference, bounded in C^k by C ε
[[pending:t3-setting]], Ů satisfying (Aug3) with its true planar shears in every slicing
([[lem:class-leaf-differences]], last statement); 1_F times a smooth function vanishing to infinite order on ∂F with C^k
norm at most C ε has H^k norm at most C ε on the bounded support. ∎

**Lemma {#lem:loc-t5-existence}** (Existence on space-time.) For ε small there is a solution U of the system of
[[sec:loc-t5-system]] on [τ_init, τ_fin] × R⁴ with U = Û on {τ ≤ τ_init}, ⟦U − Ů⟧_(k,[τ_init−2m_A,τ_fin]) ≤ C ε, and the
integral curves of P_A in F from 𝒦_A′ lie in {ξ_A = 1} for every further family A.

*Proof.* {τ ≤ τ_init} ⊂ {τ0 ≤ τ_init} ⊂ P, where 𝔄_ξ(Û) = F̃, and at points of {τ ≤ τ_init} the closures read Û on arcs
in {τ ≤ τ_init}; so h := Û − Ů = 0 on [τ_init − 2m_A, τ_init] is a history. Apply [[thm:class-kato-memory]] (b) with u_*
:= 0, the residual R of [[lem:loc-t5-residual]], (M0)–(M2) and (M1′) by [[lem:loc-t5-forcing]], and T0 := τ_fin −
τ_init: δ ≤ C ε. With ⟦Z⟧_k ≤ C ε, P_A is within C ε of P̊_A in C⁰, by [[lem:sobolev]]; for ε small the integral
curves from 𝒦_A′ stay in the neighbourhood of 𝒯̊_A on which ξ_A = 1, by continuous dependence on the field. ∎

#### Dependence on the past and the constraints {#sec:loc-t5-dependence}

**Lemma {#lem:loc-t5-energy}** (Energy on a region with memory.) Let 𝒟, B_0, B_1, 𝐀^μ, M and the slices 𝒟_s be as in
[[lem:loc-cone-energy]], except that z ∈ C¹ solves 𝐀^μ ∂_μ z = Mz + 𝔫 on 𝒟 with z(τ) ∈ H¹ on each slice and 𝔫 measurable
with ∫_(𝒟_s) |𝔫|² ≤ C_𝔫 ∫_(𝒟_s) |z|² for every s. Then z = 0 on 𝒟.

*Proof.* The divergence identity of the proof of [[lem:loc-cone-energy]] holds for the W^(1,1) field ⟨𝐀^μ z, z⟩ on the
Lipschitz domains 𝒟_s, by approximation with compactly supported fields when 𝒟_s is unbounded, and gives e(s) ≤ ∫_(𝒟_s)
(C |z|² + 2 |z| |𝔫|) ≤ (C + 1) ∫_(𝒟_s) |z|² + C_𝔫 ∫_(𝒟_s) |z|² ≤ C′ ∫_(τ_init)^s e, the boundary terms over B_1 being
nonnegative and those over B_0 zero. Gronwall's inequality gives e = 0. ∎

**Lemma {#lem:loc-t5-past}** (The past of the faces.) U = Û on P ∩ {τ ≤ τ_fin}. So U carries the formal jets on ∂F ∩ {τ
≤ τ_fin}, and induces the data there.

*Proof.* On P both solve 𝔄_ξ(·) = F̃. Let z := U − Û and 𝒟 := the closure of P ∩ {τ_init ≤ τ ≤ τ_fin}, with B_0 := 𝒟 ∩
{τ = τ_init}, where z = 0, and B_1 := ∂F ∩ 𝒟. Write the difference of the two systems with the coefficients at Û: A^μ(Û)
∂_μ z = Mz + 𝔫, with M bounded and 𝔫 the difference of the closures of the families carried near the axes, times bounded
factors. On ∂F the outward conormal of P is du on 𝒞_out and dv on 𝒞_in; at Û the wave block has the inverse metric Ĝ⁻¹,
for which du and dv are null with du(∂_τ), dv(∂_τ) > 0, and the transport fields are future causal, with du and dv
nonnegative on them, convexly combined with ∂_τ where ξ_A < 1; so ν_μ 𝐀^μ ≥ 0 on B_1, by the remark after
[[lem:loc-cone-energy]]. Let x ∈ 𝒟_s with ρ_i(x) < δ_*/4 and A a family whose closure is used at x, and D := P ∩ {t_A =
t_A(x)} ∩ {τ ≤ s}. Every point y of D near the axis has its arc of Û in D: in {τ ≤ τ(y)} ⊂ {τ ≤ s} by
[[lem:loc-t5-times]] (c), and in P, since near a point where a face meets axis i the face section of the slice is a leaf
of Û for A ([[lem:loc-t5-faces]]): A crosses that face there, ξ_A vanishing near the face–axis points where A is tangent
([[lem:loc-t5-tubes]]), or A is adapted, both face sections of the slices of τ0 being leaves of both adapted families;
and away from the faces the arc lies in P, being within C δ_*² of y. [[lem:class-leaf-arc]] (c) with V := Û and U := U
gives ‖σ_A[U] − σ_A[Û]‖_(L²(D∩𝒰_(δ/2))) ≤ C ‖z‖_(L²(D∩𝒰_δ)). Squaring and integrating over t_A(x), by Fubini's theorem
in the chart (t_A, x), ∫_(𝒟_s) |𝔫|² ≤ C ∫_(𝒟_s) |z|², the sets D lying in 𝒟_s. [[lem:loc-t5-energy]] gives z = 0. ∎

**Lemma {#lem:loc-t5-constraints}** (The constraints.) Let 𝒯 := F ∩ {τ ≤ s*}. For the adapted families, and for every
further family A on 𝒯_A′, the union of the integral curves of P_A in 𝒯 from the set 𝒦_A″ defined in the proof: g⁻¹(p_A,
p_A) = 0, dp_A = 0, p_A = du_A with u_A an eikonal, and Θ_A = □_g u_A; D(g) = 0 on 𝒯; supp q_A ∩ 𝒯 ⊂ 𝒯_A′; and (g, u_A,
q_A) is a class solution of [[eq:class-system]] with N_f families on 𝒯, q_A ≥ 0, the phase u_A of a further family being
defined on 𝒯_A′.

*Proof.* *The set 𝒦_A″.* Let δ_2 > 0. Near the generator where A crosses a face at axis i, let 𝒦_A″ consist of 𝒦_A′ and
of the caps {ρ_i ≤ δ_2} of the A-sections that meet 𝒦_A′ ∩ {ρ_i ≤ δ_2}. For δ_2 small, 𝒦_A″ satisfies (F-a) and (F-b)
and its curves lie in {ξ_A = 1} (choosing 𝒦_A′ and ξ_A for 𝒦_A″ from the start, as we may). *ν_A and dp_A.* By
[[lem:loc-t5-past]] they vanish, with all derivatives, on ∂F ∩ {τ ≤ s*}, as they do for Û. Every point of 𝒯 (of 𝒯_A′)
lies on an integral curve of P_A that, followed backwards, stays in 𝒯 (in 𝒯_A′ ⊂ {ξ_A = 1}) until it reaches ∂F: τ
decreases along it at a rate bounded below, and τ ≥ Φ(0, 0) on F. Along it P_A(ν_A) = 0 and ℒ_(P_A) dp_A = d(i_(P_A)
dp_A) = 0 where ν_A = 0 ([[prop:class-augmented]] (b)), so ν_A = 0 and dp_A = 0. Then ℒ_(P_A) p_A = d(i_(P_A) p_A) =
dν_A = 0. Let u_A be constant along the integral curves of P_A, equal on ∂F to the face coordinate (for the adapted
families) or to U_A (for a further family). Then ℒ_(P_A) du_A = d(P_A(u_A)) = 0, and du_A = p_A on ∂F, as U = Û there
with p̂_A = dû_A; the two 1-forms are Lie transported by the flow from ∂F, so p_A = du_A, and g⁻¹(du_A, du_A) = ν_A = 0.
*D and Δ_A.* Let U′ be U with Θ_A replaced by div_g P_A = □_g u_A. For the eikonal u_A, the level sets of u_A in a slice
solve [[eq:class-leaf-volterra]] with H_L[U′] ([[lem:class-leaf]] (c), [[lem:class-gauss]] (b)), so by
[[lem:class-volterra]] they are the A-leaves of U′. On ∂F, u_A is the face datum, so the face sections of the slices of
t_A, within ρ_i < δ_*/2, are level sets of u_A ([[lem:loc-t5-times]] (b)). Put 𝒯_A′ := 𝒯 for the adapted families and,
for s ≤ s*, D_(A,t,s) := 𝒯_A′ ∩ {t_A = t} ∩ {τ ≤ s}. Every point of D_(A,t,s) within δ_*/4 of an axis has its arc of U′
in D_(A,t,s): in {τ ≤ s} by [[lem:loc-t5-times]] (c); in F, as the face sections are leaves of U′ and leaves do not
cross; and for a further family in 𝒯_A′, since the arc lies in the level set of u_A through the point, whose points near
the axis lie on integral curves of P_A from the cap {u_A = c} ∩ {ρ_i ≤ δ_2} ⊂ 𝒦_A″ of the crossing face, for δ_*
e^(L(s*−Φ(0,0))) ≤ δ_2, L a Lipschitz constant of the flow of P_A, the axis being invariant under it as [P_A, K_i] = 0.
Where S_A^ax is used, the proof of [[thm:class-stability]], Step 10, gives P_A(Δ_A) = −½ Δ_A (Θ_A + div_g P_A − 2κ_A1) −
½ (σ_A[U]² − σ_A[U′]²) + g(∇_(P_A) D, P_A) + L(P_A, P_A), and elsewhere [[eq:class-defect]] with
[[prop:class-augmented]] (e); and D solves [[eq:class-gauge-wave]] with B_g T = Σ_A Δ_A q_A p_A. By
[[lem:class-leaf-arc]] (c) with V := U′, the middle term is bounded in L²(D_(A,t,s) ∩ 𝒰_(δ/2)) by C
‖Δ_A‖_(L²(D_(A,t,s))), U − U′ having only the component Δ_A. On 𝒯 ∩ {τ ≤ s} the faces are the past boundary, where D, ∂D
and Δ_A vanish; the lateral boundary of 𝒯_A′ is ruled by integral curves of P_A, so the transport has no flux through
it; and {τ = s} is spacelike. The energy ‖∂D‖² + ‖D‖² on 𝒯 ∩ {τ = s} plus Σ_A ‖Δ_A‖² on 𝒯_A′ ∩ {τ = s} therefore obeys
the integrated inequality of [[lem:loc-t5-energy]], the non-local terms being bounded, after integration over t by
Fubini's theorem, by the L² norms of Δ_A over 𝒯_A′ ∩ {τ ≤ s}. So D = 0 and Δ_A = 0. Hence Ric(g) = T by (Aug1), Θ_A =
□_g u_A, and (Aug4) is the conservation law; q_A vanishes off the curves from 𝒦_A ⊂ 𝒦_A″ and keeps its sign along them.
∎

#### Uniqueness, the theorem and data tangent to a cone {#sec:loc-t5-theorem}

**Lemma {#lem:loc-t5-uniqueness}** (Dependence on the past faces.) Let R′ := [0, u′] × [0, v′] ⊂ Q1, and let U1, U2 be
solutions of the augmented system on R′ × S³, in the wave gauge relative to Ĝ, with p_A = du_A and Θ_A = □_g u_A, every
further family A carried on the union 𝒯_A^(1) of the integral curves of U1's P_A in R′ from 𝒦_A″, with q_A = 0 off
𝒯_A^(1) for both, within ε2 of Ů in the norm 𝒩_(k−1) of [[eq:class-energy]] on the slices, and agreeing to infinite
order on the past faces ∂F ∩ R′. Then U1 = U2 on R′ × S³.

*Proof.* For N ≥ 1 let Φ_N := (u/u′)^N + (v/v′)^N + κ_N (u + v), κ_N := 1/(N (u′ + v′)), and T_N := F ∩ {Φ_N ≤ 1} ⊂ R′.
Φ_N has Φ_(N,u), Φ_(N,v) ≥ κ_N > 0, so it is a chart time whose restrictions to the faces are increasing, and
[[lem:loc-t5-times]] applies with Φ_N in place of τ0, for the data of R′'s faces, giving times t_A^N and τ^N := τ0^N +
bend, with δ_* depending on N. Since τ^N ≥ Φ_N, T′_N := F ∩ {τ^N ≤ 1} ⊂ T_N ⊂ R′; and every point (u, v) with u < u′ and
v < v′ lies in T′_N for N large, as Φ_N(u, v) → 0 and the bend is at most K δ_*². For genuine solutions the planar shear
is that of the level sets of u_A in every slicing ([[lem:class-leaf-differences]], last statement), so both satisfy the
closures of [[sec:loc-t5-system]] computed on the slices of t_A^N. Extend U2 beyond R′ to a smooth state with the same
bounds; by [[lem:class-leaf-arc]] only its bounds enter outside R′, and the arcs of U2 through points of T′_N, used by
U2's own closures, lie in F ∩ {τ^N ≤ 1} ⊂ R′, the face sections being leaves of U2 and the arcs running into the past.
Let z := U2 − U1 (for a further family, on 𝒯_A^(1) only) and write the difference of the systems with the coefficients
at U1. Apply [[lem:loc-t5-energy]] on 𝒟 := T′_N, with B_0 := ∂F ∩ T′_N, where z vanishes to infinite order, and B_1 :=
{τ^N = 1} ∩ F, spacelike for both metrics with T′_N to its past by [[lem:loc-t5-times]] (a), together with the lateral
boundaries of the 𝒯_A^(1), ruled by integral curves of U1's P_A, through which the transports have no flux. Exactly as
in the proof of [[lem:loc-t5-constraints]], with V := U1, the sets T′_N ∩ {t_A^N = t} ∩ {τ^N ≤ s} (intersected with
𝒯_A^(1) for further families) contain the arc of U1 through each of their points near the axes, the face sections being
level sets of u_A^(1); [[lem:class-leaf-arc]] (c) with V := U1 and U := U2 bounds the non-local terms. So z = 0 on T′_N
for every N, hence on R′ minus its future faces, and on R′ by continuity. ∎

The past faces of R′ lie in 𝒞_out ∪ 𝒞_in. A rectangle with a past face {u = u0}, u0 > 0, inside F is not covered: a
further family of outgoing type at an axis is tangent to every hypersurface {u = const} along its axis generator, its
rays running there in {u = const}; its density on that generator is transported from 𝒞_in; and where it is nonzero the
section of {u = u0} by a slice is not a leaf of the family, the argument of [[rem:loc-t5-scope]] (i) applying to it.
Likewise for {v = v0} and families of ingoing type.

**Theorem {#thm:loc-t5}** (Development with further families at the axes.) Let k ≥ 6 and m ≥ m0(k) be the orders, and
let the data be cone data on the faces of Q1 as in the development of data reaching the axes [[pending:t3-theorem]], of
size at most ε in C^m, together with further families A = 3, …, N_f as in [[def:loc-t5-family]], satisfying (F-a),
(F-b) and (F-c), in place of that theorem's condition that their densities vanish near the points where the faces meet
the axes. There are ε0, C, ε2 > 0 such that for ε ≤ ε0:

(a) *Existence.* There is a class solution (g, u_in, u_out, u_A, q_in, q_out, q_A) of [[eq:class-system]] with N_f
families on Q1 × S³, the phase u_A of a further family defined on a neighbourhood of supp q_A, of class C^(k−3), whose
metric has the form [[eq:loc-double-null]], with u_in = v and u_out = u, that induces the data on 𝒞_out ∩ Q1 and 𝒞_in ∩
Q1.
(b) *Estimate.* The metric functions, the densities and, near supp q_A, the further phases differ from the background's
by at most C ε, with their derivatives of order at most k − 3.
(c) *Uniqueness.* On every rectangle R′ = [0, u′] × [0, v′] ⊂ Q1, Q1 included, every class solution on R′ × S³ of the
same kind, in the gauge [[eq:loc-double-null]], that induces the same data on ∂F ∩ R′ and is within ε2 of the
background, with its derivatives of order at most k − 2, equals it there.
(d) *Localisation.* The solution equals the background on every rectangle [0, u′] × [0, v′] ⊂ Q1 on whose two faces the
data are the background's and every density of a further family vanishes.

*Proof.* The system of [[sec:loc-t5-system]] has a solution U on [τ_init, τ_fin] × R⁴ with ⟦U − Ů⟧_k ≤ C ε
([[lem:loc-t5-existence]]). It is G-invariant: the system is invariant under G, the closure times being invariant
functions, and the image of U under an element of G is a solution with the same history, equal to U by the uniqueness of
[[thm:class-kato-memory]] (a). By [[lem:loc-t5-past]] it induces the data, and by [[lem:loc-t5-constraints]] it is a
class solution on 𝒯 = F ∩ {τ ≤ s*} ⊃ Q1 (for δ_* small, as max_(Q1) τ0 < s* and τ − τ0 ≤ K δ_*²), in the wave gauge
relative to Ĝ. By [[lem:sobolev]] on the slices, all derivatives of U − Ů of order at most k − 3 are at most C ε. The
phases u_in, u_out and an angle transported along the outgoing generators from 𝒞_in are double-null coordinates in which
the metric has the form [[eq:loc-double-null]] and induces the data, as for the preceding section's solution
[[pending:t3-gauge]]; this gives (a) and (b). (c) A second solution of that kind, brought to the wave gauge relative to
Ĝ by the wave map of the preceding section [[pending:t3-wave-map]], gives a solution of the augmented system with p_A :=
du_A and Θ_A := □_g u_A, agreeing with U to infinite order on the faces by [[lem:loc-cone-jets]] (iv) and
[[lem:loc-t5-jets]] (b); its further densities vanish off the union of its own curves from 𝒦_A, which for ε2 small lies
in 𝒯_A^(1) by continuous dependence on the field. [[lem:loc-t5-uniqueness]] gives equality on the rectangle, and the
double-null coordinates are then the same.
(d) On such a rectangle the densities of the further families vanish for the solution, the integral curves from 𝒦_A not
entering it (a curve that enters F through a face point with u > u′ or v > v′ keeps that inequality); the background is
a class solution of the same kind there, inducing the same data on its faces, and (c) applies. ∎

For N_f = 2 and for further families whose densities vanish near the points where the faces meet the axes, (F-a)–(F-c)
hold, and [[thm:loc-t5]] contains the theorem of the preceding section, except that it gives the solution in the
class C^(k−3) and not as a smooth solution ([[rem:loc-t5-scope]] (v)).

**Proposition {#prop:loc-t5-cut}** (Families tangent to a cone: a development off the axes concerned.) Let the data be
as in [[thm:loc-t5]] except that, for the further families A of a set 𝒢, (F-a) or (F-b) fails. Let N ⊂ ∂F be a
closed G-invariant set such that: (N1) N contains a neighbourhood in ∂F of the tangency sets of the families of 𝒢 at the
axes where they carry density near them, and of the corner circles of those axes, on both faces; (N2) N contains, with a
point, the points of larger v (on 𝒞_out) or larger u (on 𝒞_in) on its generator; (N3) outside the interior of N the data
of every family of 𝒢 satisfy (F-b) and (F-c). Let D′ ⊂ Q1 × S³ be compact and G-invariant, with boundary in ∂F ∖ N, in a
G-invariant hypersurface Λ at distance at least w > 0 from the axes that is spacelike for g0 with D′ to its past, and in
the future faces {u = u1} ∪ {v = v1} of Q1. Then for ε small there is a class solution on D′, in the gauge
[[eq:loc-double-null]], that induces the data on D′ ∩ ∂F; it is unique among class solutions on D′ in that gauge within
ε2 of the background, for the wave-gauge reference Ĝ built with the scale δ_e of [[prop:loc-cone-formal]] small enough
depending on D′ and N.

*Proof.* Let χ be a smooth G-invariant function on ∂F, equal to 1 outside N and to 0 on a neighbourhood of the tangency
sets and corner circles of (N1). Replace q_A by χ q_A for A ∈ 𝒢, keep the free data, and solve the constraints of
[[lem:loc-t5-jets]] (a): the solution changes only on generators through points where χ q_A ≠ q_A, and only at and
beyond them, hence only in N by (N2). The new data are of size at most C ε, satisfy (F-a)–(F-c) by (N1) and (N3), and
agree with the old ones on ∂F ∖ N; the phase data of A ∈ 𝒢 near the tangency sets are not used, family A being carried
only near its new tube (the paragraph before [[lem:loc-t5-jets]]). [[thm:loc-t5]] gives a solution Ũ on Q1 × S³; its
restriction to D′ induces the old data on D′ ∩ ∂F. The jets of [[lem:loc-cone-jets]] and [[lem:loc-t5-jets]] at a point
of ∂F depend on the data on the generator up to that point, so on ∂F ∖ N they are those of the old data, by (N2); and Ĝ
at a point within 2δ_e of ∂F depends, by the construction of [[lem:loc-cone-borel]], on the jets at the points of ∂F
with the same angle ϑ and with v, respectively u, within 2δ_e, which lie outside N for δ_e small depending on D′ and N.
*Uniqueness.* Let U2 be a second class solution on D′ as stated, brought to the wave gauge relative to Ĝ
[[pending:t3-wave-map]]. Run the proof of [[lem:loc-t5-uniqueness]], with R′ := Q1, on D′ ∩ T′_N, with B_1 enlarged by
Λ: its conormal is future timelike, with a margin, for g0, hence for both metrics, and positive on the transport fields.
The arcs used near the axes lie in D′: within δ_* < w/2 of an axis, points of D′ are at distance at least w/2 from Λ,
and the arcs are within C δ_*² of their end points, while near the faces the face sections are leaves; families of 𝒢 are
tangent to no part of D′ ∩ ∂F near an axis, by (N1). So U2 = Ũ on D′. ∎

The region D′ is bounded by a hypersurface Λ that is spacelike for g0, and the finite-speed bound of
[[thm:loc-cone-development]] (b), with its constant 2C_0, is not used: Λ carries the causal bound, and any such Λ may be
taken.

**Remark {#rem:loc-t5-scope}** (What [[thm:loc-t5]] and [[prop:loc-t5-cut]] do not give.) (i) *Families tangent to a
cone with density on the tangency set.* Let a further family carry density on a neighbourhood of a point of its tangency
set, of ingoing type at axis 2 say, so that its density is nonzero near the axis generator of 𝒞_in. On that generator
g⁻¹(dv, du_A) = 0 ([[lem:loc-t5-dichotomy]]), the coefficient by which [[lem:loc-t5-jets]] (b) solves for the transverse
derivatives on 𝒞_in vanishes, and the face is characteristic for the family there: its jets on 𝒞_in are not determined
by the recursion. Nor are the sections of 𝒞_in by the slices of any time function leaves of the family near the
generator: there U_A = c + a(u) ϑ² + O(ϑ⁴), since ∂_u U_A vanishes on the generator and U_A is even in ϑ; such a section
through an axis point is a G-invariant sphere u = u_0 + b ϑ² + O(ϑ⁴), on which U_A = c + a(u_0) ϑ² + O(ϑ⁴), as ∂_u U_A =
O(ϑ²); so U_A is constant on it only if a(u_0) = 0, and otherwise p_A does not annihilate its tangent space and the leaf
criterion fails. The development of such data, through the axis, is not established here; [[prop:loc-t5-cut]] gives it
away from that axis near the points concerned. (ii) *The condition (F-a).* It cannot be dropped for a family that
crosses a cone near the corner circle, by the remark after [[lem:loc-t5-tubes]]. (iii) *Further families in the
preceding section.* Every further family is tangent to one cone along an axis generator through a corner circle
([[lem:loc-t5-dichotomy]]), where its phase data have undetermined jets; so the preceding section's further families are
carried, as here, only near the tubes of their densities, with the cut-offs ξ_A, whatever their densities near the axes.
(iv) *One crossing family at each point.* When at each point where a face meets an axis the families present have phases
that are functions of one of them on the face, a single closure time serves them all there, and the bend of τ can be
dropped near that point; the proof above applies with t_A := τ near it, and needs the cut-offs ξ_A as well. (v)
*Regularity and size.* The solution is given in the class C^(k−3) for data small in C^m; that a smooth datum gives a
smooth solution, which the preceding sections prove for their systems, would need a bound of the higher norms of the
system with memory that is linear in them, which is not proved here. Large data at the axes, and densities that are only
bounded or are measures, are not covered.

### Placement

Each item names the place, the old text and the new text, as lines of the chapter source. Line numbers are those of the
current sources and serve only to find the place.

*1. Block A1, chapter 81.* The text of Block A1 from "In the coordinates (z, y) of [[lem:class-leaf]] near a point p" to
the end of the proof of [[lem:class-leaf-tame]] (without the heading "Block A1" and its first paragraph) is inserted in
[[sec:class-planar-shear]] after [[rem:class-leaf-numerics]], whose last line is "0.146 and 2.91. No proof uses these
observations." (line 1363), and before the heading of [[sec:class-axes-stability]] (line 1365), with one blank line
before and after. It defines lem:class-leaf-arc, eq:class-leaf-arc and lem:class-leaf-tame.

*2. Block A2, chapter 81.* The text of Block A2 from "*Space-time norms.*" to the end of [[rem:class-kato-memory]] is
inserted in [[sec:class-kato]] after [[rem:class-kato-model]], whose last line is "proof uses these observations." (line
875), and before the heading of [[sec:class-off-axes]] (line 877), with the first paragraph of Block A2 (from "It solves
[[eq:class-kato-system]] when") kept as its opening paragraph, without the words "The text of this block goes into
[[sec:class-kato]] after [[rem:class-kato-model]]." It defines eq:class-trace, lem:class-mixed-product,
lem:class-kato-history, thm:class-kato-memory and rem:class-kato-memory.

*3. Block B, chapter 83.* The section of Block B, from its heading "### Further dust families at the axes {#sec:loc-t5}"
to the end of [[rem:loc-t5-scope]] (without the line "### Block B. …" and its paragraph), is inserted as a new section
of [[ch:localised-data]] immediately after the section on perturbations that reach the axes (the section of the
development whose results this section cites as [[pending:t3-setting]] and its companions) and before the section on
large data at the axes, if that is placed after it; in any case after [[sec:loc-cone-proof]] and before [[sec:loc-kid]].
This section extends the preceding one to further families and is cited by nothing that the large-data section needs; it
precedes that section because it rests on the same small-data construction. It defines sec:loc-t5, sec:loc-t5-families,
def:loc-t5-family, lem:loc-t5-dichotomy, lem:loc-t5-tubes, lem:loc-t5-jets, sec:loc-t5-times, eq:loc-t5-times,
lem:loc-t5-times, lem:loc-t5-faces, sec:loc-t5-system, lem:loc-t5-forcing, lem:loc-t5-residual, lem:loc-t5-existence,
sec:loc-t5-dependence, lem:loc-t5-energy, lem:loc-t5-past, lem:loc-t5-constraints, sec:loc-t5-theorem,
lem:loc-t5-uniqueness, thm:loc-t5, prop:loc-t5-cut and rem:loc-t5-scope. Wherever the section says "the preceding
section", the coordinator replaces the words by [[sec:…]] of that section once its key is fixed, and each
[[pending:t3-…]] marker by the label of the result named in the report.

*4. Chapter 83, the paragraph after [[prop:loc-cones]] (the loss sentence).* The cones development (item 4 of its
Placement) ends this paragraph with the sentences "For cone data that carry dust and are not small, and for data whose
perturbation reaches an axis, no development is asserted by [[thm:loc-cone-development]] ([[rem:loc-cone-scope]]). No
result of the other chapters uses these developments.", and the section on perturbations that reach the axes shortens
that list of excluded cases. Old: those closing sentences, in the form in which the earlier sections leave them. New:

For cone data that carry dust and are not small, no development on the whole rectangle is asserted. Further dust
families are admitted at the points where a cone meets an axis when they cross that cone there and carry no density near
the corner circles of the axes ([[thm:loc-t5]]); for a family that carries density where it is tangent to a cone
along an axis generator, a development is asserted only on regions that avoid that axis near the points concerned
([[prop:loc-t5-cut]], [[rem:loc-t5-scope]]). Densities that are only bounded, or are measures, are not covered. No
result of the other chapters uses these developments.

If the earlier sections keep further cases in that list (large data on a neighbourhood of the cones, say), they stay;
only the case of non-adapted families at the points where a face meets an axis is replaced by the sentence on further
families above.

*5. Chapter 81, [[rem:class-scope]], its last two lines (lines 1670–1671).* Old:

polarisation of the waves for a non-radial family, and the limits that carry massless Vlasov matter are taken up in
[[ch:vlasov]].

New:

polarisation of the waves for a non-radial family, and the limits that carry massless Vlasov matter are taken up in
[[ch:vlasov]]. For the characteristic problem the same alternative at an axis, gradient a multiple of dv or of du,
decides whether a further family crosses a cone at its axis generator or is tangent to it ([[lem:loc-t5-dichotomy]]).

*6. The section on perturbations that reach the axes (its clause on further families).* Every further family is tangent
to one cone along the axis generator through a corner circle ([[lem:loc-t5-dichotomy]]), where the jets of its phase on
that cone are not determined. That section's further families must therefore be carried only near the tubes of their
densities, by cut-offs ξ_A as in the paragraph before [[lem:loc-t5-jets]], whatever their densities near the axes; its
statement and its system should say so, and [[rem:loc-t5-scope]] (iii) records it. If that section also carries the
closures of the adapted families on the slices of τ0 with the time τ0, nothing else in it changes: [[sec:loc-t5-system]]
only adds the bend of τ and the further families' closure times.

*7. Chapter 83, opening paragraph, chapter 03 "More families", chapter 90.* No change is required by this section beyond
those of the earlier sections; where those sentences list the cases not covered, the case "non-adapted families that
cross a face where it meets an axis" becomes "further families that carry density where they are tangent to a cone at an
axis" ([[thm:loc-t5]], [[prop:loc-t5-cut]]).

*8. Appendix A.* No new entry. The proofs use [[thm:std-bh-embedding]], [[thm:std-bh17-embedding]], [[thm:std-gn-moser]]
and [[cor:std-moser-product]], already there, and no other published result.

### Crosswalk rows

New rows, one per label, in chapter order, each given as its four fields (label; source; source_name; note), to be
written with tab separators. The source is "P-CIVP5" with the line of the label in this file.

For crosswalk/81-class-system.tsv, after the row of rem:class-kato-model:

Row 1. eq:class-trace; P-CIVP5:125; P-CIVP5 Block A2, display; trace of a space-time Sobolev function on the slices; the
extension E_b beyond b.
Row 2. lem:class-mixed-product; P-CIVP5:137; P-CIVP5 Block A2, Lemma (Products at one time); new: H^σ1 · H^σ2 ⊂ H^σ on
unit cubes; time derivatives of compositions.
Row 3. lem:class-kato-history; P-CIVP5:161; P-CIVP5 Block A2, Lemma (The linear problem with forcing in a space-time
space and a history); new: the linear step of GN-T5 §2.6 written in full; history matched at t1.
Row 4. thm:class-kato-memory; P-CIVP5:211; P-CIVP5 Block A2, Theorem (Kato's iteration with memory); new: GN-T5
condition C1, integrated hypotheses (M0)–(M2), (M1′) in place of (F1)–(F2); S-T5 §4.3 M4 step 3 (contraction on each
slice) not used.
Row 5. rem:class-kato-memory; P-CIVP5:274; P-CIVP5 Block A2, Remark (Why the hypotheses are integrated); GN-T5 §2.4
mechanism stated without the model; no proof uses it.

For crosswalk/81-class-system.tsv, after the row of rem:class-leaf-numerics:

Row 6. lem:class-leaf-arc; P-CIVP5:18; P-CIVP5 Block A1, Lemma (Two states compared along one arc); new: GN-T5
conditions C2 and C7 (§6.2), one-sided, on arc-closed sets, by the Volterra form and the Hardy average; implies GN-T3
T3-2(b) at order 0.
Row 7. eq:class-leaf-arc; P-CIVP5:27; P-CIVP5 Block A1, display; pointwise one-sided bound.
Row 8. lem:class-leaf-tame; P-CIVP5:82; P-CIVP5 Block A1, Lemma (The planar shear on the ball 𝔅′); new: GN-T5 §2.2
lighter form of lem:class-leaf-differences (a), bound linear in 𝒩_k on the ball 𝔅′.

For crosswalk/83-localised-data.tsv, after the rows of the section on perturbations that reach the axes:

Row 9. sec:loc-t5; P-CIVP5:288; P-CIVP5 Block B, section heading; Tier 5 (S-T5, GN-T5): Route M for crossing families;
statement W for tangent families.
Row 10. sec:loc-t5-families; P-CIVP5:316; P-CIVP5 Block B, subsection; families and their type at an axis.
Row 11. def:loc-t5-family; P-CIVP5:318; P-CIVP5 Block B, Definition (Further families); S-T5 §1.2; GN-T5 C3 as (F-a);
(H×) follows from (F-b); corner condition (F-c).
Row 12. lem:loc-t5-dichotomy; P-CIVP5:335; P-CIVP5 Block B, Lemma (Crossing and tangency at the axes); S-T5 §1.2
dichotomy (crossing/grazing).
Row 13. lem:loc-t5-tubes; P-CIVP5:353; P-CIVP5 Block B, Lemma (The tubes avoid the tangency sets); GN-T5 §1.3 (C3),
proved by continuous dependence.
Row 14. lem:loc-t5-jets; P-CIVP5:385; P-CIVP5 Block B, Lemma (Cone data and jets with further families); S-T5 M0 with
GN-T5 C4; sources of the cone constraints; transverse jets on the crossing sets.
Row 15. sec:loc-t5-times; P-CIVP5:417; P-CIVP5 Block B, subsection; closure times.
Row 16. eq:loc-t5-times; P-CIVP5:432; P-CIVP5 Block B, display; t_A := τ0 − χ g_A, τ := τ0 + K ρ² χ (GN-T5 §1.1).
Row 17. lem:loc-t5-times; P-CIVP5:436; P-CIVP5 Block B, Lemma (The closure times and the evolution time); S-T5 M1 as
built in GN-T5 §1.1, (a)–(d) proved.
Row 18. lem:loc-t5-faces; P-CIVP5:466; P-CIVP5 Block B, Lemma (The face sections are leaves of each family); S-T5 M2 by
the leaf criterion of Tier 3 (GN-T3 §1.2).
Row 19. sec:loc-t5-system; P-CIVP5:482; P-CIVP5 Block B, subsection; the system with memory; closures per family on the
slices of t_A; ξ_A.
Row 20. lem:loc-t5-forcing; P-CIVP5:501; P-CIVP5 Block B, Lemma (The forcing term); S-T5 M4 hypotheses verified:
(M0)–(M2), (M1′) by coarea (Fubini) over the t_A-foliation.
Row 21. lem:loc-t5-residual; P-CIVP5:530; P-CIVP5 Block B, Lemma (The forcing term is smooth across the faces); S-T5 M6
/ GN-T5 §3 (GN-M3), written in full in the t_A-slicing.
Row 22. lem:loc-t5-existence; P-CIVP5:564; P-CIVP5 Block B, Lemma (Existence on space-time); thm:class-kato-memory (b).
Row 23. sec:loc-t5-dependence; P-CIVP5:574; P-CIVP5 Block B, subsection; dependence on the past and constraints.
Row 24. lem:loc-t5-energy; P-CIVP5:576; P-CIVP5 Block B, Lemma (Energy on a region with memory); integrated Gronwall
(GN-T5 §2.6, where M5 enters).
Row 25. lem:loc-t5-past; P-CIVP5:585; P-CIVP5 Block B, Lemma (The past of the faces); S-T5 M5 (P) with GN-T5 C7:
one-sided bound, closure under the arcs of Û only.
Row 26. lem:loc-t5-constraints; P-CIVP5:603; P-CIVP5 Block B, Lemma (The constraints); S-T5 M5 (F) on the slice-triangle
of the bent time (GN-T3 §4.2), tubes from 𝒦_A″.
Row 27. sec:loc-t5-theorem; P-CIVP5:640; P-CIVP5 Block B, subsection; uniqueness, theorem, statement W.
Row 28. lem:loc-t5-uniqueness; P-CIVP5:642; P-CIVP5 Block B, Lemma (Dependence on the past faces); S-T5 M7 / GN-T5 §4
(C5): rectangles with past faces in the cones, by exhaustion with triangles.
Row 29. thm:loc-t5; P-CIVP5:672; P-CIVP5 Block B, Theorem (Development with further families at the axes); S-T5 M8;
class C^(k−3), smoothness not proved.
Row 30. prop:loc-t5-cut; P-CIVP5:712; P-CIVP5 Block B, Proposition (Families tangent to a cone: a development off the
axes concerned); statement W of S-T5 §4.4 with GN-T5 W1–W4; N closed under the generators.
Row 31. rem:loc-t5-scope; P-CIVP5:745; P-CIVP5 Block B, Remark (What the theorem does not give); grazing families open
(S-T5 §5.1); Tier 3 family clause (C4); Route S; regularity.
