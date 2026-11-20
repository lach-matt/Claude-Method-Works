### Block A1. Additions to the section on the planar shear at an axis (chapter 81)

The text of this block goes into [[sec:class-planar-shear]] after [[rem:class-leaf-numerics]]; the Placement section
gives the position. It compares the planar shears of two states leaf by leaf, along one arc from the axis, and gives
the bound of [[lem:class-leaf-differences]] (a) on the larger ball 𝔅′.

In the coordinates (z, y) of [[lem:class-leaf]] near a point p of axis 2 on a slice, a *state* is V = (g, p_A, Θ_A) on
𝒰_(2δ), smooth and G-invariant, with g Lorentzian and the slice spacelike for g. It has *bounds* (M, c) if the C² norms of
g and the C¹ norms of p_A and Θ_A on 𝒰_(2δ) are at most M, if A3, B3 and det₂ of [[lem:class-leaf]] are at least 1/M,
and if |p_A^Σ| ≥ c and p_A(∂_z) ≥ c on 𝒰_(2δ), p_A^Σ the spatial part of p_A. Its H_L is H_L[Θ_A] of
[[lem:class-leaf-differences]], with TΣ_L there the γ3-orthogonal complement in TM3 of p_A^Σ, so that H_L is a function
of position; its leaves are the solutions h(·; z0) of [[eq:class-leaf-volterra]] with h(0) = z0, and σ[V](x) is the planar
shear [[eq:class-shear-leaf]] of the leaf through x, with |p_A^Σ| for |∇_M3 u| and p_A(n) for n(u). For x on the slice
put r_x := |y(x)|. The *arc* of V through x is the part {(h(t; z0), t y(x)/r_x) : 0 ≤ t ≤ r_x} of the leaf through x, z0
its axis point. For two states, |U − V| at a point is the sum of the absolute values of the differences of g, ∂g, p_A and
Θ_A there.

**Lemma {#lem:class-leaf-arc}** (Two states compared along one arc.) Let U and V be states with bounds (M, c). There are
r_1 > 0 and C, depending only on M, c, p and the chart, such that for δ ≤ r_1:

(a) the leaves of V through the axis points z0 with |z0 − z(p)| < δ are graphs over the disc {|y| ≤ δ}, with
|h′(r; z0)| ≤ C r, |∂_(z0)h′(r; z0)| ≤ C r and |∂_(z0)h(r; z0) − 1| ≤ ½; every x ∈ 𝒰_(δ/2) lies on exactly one of
them; and the same holds for U;

(b) for x ∈ 𝒰_(δ/2), with f(t) := |U − V| at the point of the arc of V through x at radius t,

    |σ[U](x) − σ[V](x)| ≤ C (f(r_x) + r_x⁻² ∫_0^(r_x) t f(t) dt + (∫_0^(r_x) t f(t)² dt)^(1/2));      {#eq:class-leaf-arc}

(c) if D is a G-invariant set such that the arc of V through every point of D ∩ 𝒰_(δ/2) lies in D, then
‖σ[U] − σ[V]‖_(L²(D∩𝒰_(δ/2))) ≤ C ‖U − V‖_(L²(D∩𝒰_δ)).

Only the values of U − V on the arcs of V enter (b) and (c), and only bounds of U elsewhere.

*Proof.* (a) Write G_X(r, z, q) := r H_X(z, r)/a_L^X(r, z, q) − E_L^X(r, z, q) for a state X, with a_L^X and E_L^X the
functions of [[lem:class-leaf]] (c) for the metric γ3 of X, evaluated with h := z and h′ := q, and H_X the H_L of X at
the point (z, r). By the proof of [[lem:class-volterra]], on a neighbourhood of (0, z(p), 0) whose size depends only on
(M, c), |G_X(r, z, 0)| ≤ C_0 r, |∂_z G_X| ≤ C_1 and |∂_q G_X| ≤ C_2 (r + |q|), and the map 𝒯 of that proof, with the
parameter z0, is a contraction with constant ½ on {q ∈ C([0, r_1]) : sup |q| ≤ δ_q} for r_1 and δ_q small; its fixed
point q = h′ satisfies |q(r)| ≤ C_0 r. 𝒯 depends continuously differentiably on (q, z0), so the fixed point does, and
π := ∂_(z0) h′ solves r π(r) = ∫_0^r (∂_z G_X (1 + ∫_0^ρ π) + ∂_q G_X π) dρ. Hence sup_[0,r] |π| ≤ C_1 r/2 (1 + r sup_[0,r]
|π|) + ¼ sup_[0,r] |π|, which gives |π| ≤ C r for r ≤ r_1 small, and |∂_(z0) h − 1| ≤ ∫_0^r |π| ≤ C r² ≤ ½. So for fixed
y the map z0 ↦ h(|y|; z0) is increasing with derivative in [½, 3/2], and its range over |z0 − z(p)| < δ contains
{|z − z(p)| < δ/2} when C δ² ≤ δ/4, as |h(r; z0) − z0| ≤ C_0 r²/2. This gives the foliation of 𝒰_(δ/2).

(b) Let L̂ be the leaf of V through x, z0 its axis point, ĥ := h_V(·; z0), q̂ := ĥ′, and let h̃ := h_U(·; z0) be the leaf
of U from the same axis point, q̃ := h̃′, x′ := (h̃(r_x), y(x)). On the leaf through a point the leaf equation gives k_r =
H_L − k_φ, so by [[eq:class-shear-leaf]], [[lem:class-gauss]] (c) and the formulas for ν^r and k_φ in [[lem:class-leaf]]
(c), σ[X] at a point x̄ of the leaf h of X is 𝔖_X(x̄, h′(r_x̄)/r_x̄), where 𝔖_X(x̄, s) is a smooth function of the point and
of s, built from H_X, γ3 and its first derivatives, p_A and K_Σ at x̄: k_φ = ν^r/r + ½ ν(log B3) with ν^r/r = −(C3 + A3 s)/
(det₂^(1/2) N_L), N_L² = B3 + D3 r² + 2C3 r² s + A3 r² s², at s = h′/r, and the leaf's unit tangent e_r depends only on
h′. So, for |s| ≤ C, |∂_s 𝔖_X| + |∂_x̄ 𝔖_X| ≤ C and |𝔖_U − 𝔖_V|(x̄, s) ≤ C |U − V|(x̄). Write

    σ[U](x) − σ[V](x) = (σ[U](x) − σ[U](x′)) + (𝔖_U(x′, q̃/r) − 𝔖_U(x, q̃/r)) + (𝔖_U(x, q̃/r) − 𝔖_U(x, q̂/r))
                       + (𝔖_U(x, q̂/r) − 𝔖_V(x, q̂/r)),      r := r_x.

The leaves of U foliate by (a), and σ[U](h_U(r; z̄), y) = 𝔖_U((h_U(r; z̄), y), ∂_r h_U(r; z̄)/r) has a z̄-derivative bounded
by C, since |∂_(z̄) h_U| ≤ 3/2 and |∂_(z̄) h_U′|/r ≤ C by (a); as ∂_(z̄) h_U ≥ ½, the first two terms are at most
C |x − x′| = C |δh(r)|, δh := h̃ − ĥ. The third is at most C |δq(r)|/r, δq := q̃ − q̂, and the fourth at most C f(r). Now
r δq(r) = ∫_0^r (G_U(ρ, h̃, q̃) − G_U(ρ, ĥ, q̂) + g(ρ)) dρ with g(ρ) := (G_U − G_V)(ρ, ĥ(ρ), q̂(ρ)). By the proof of
[[lem:class-volterra]], E_L^X = (C3 r + A3 q) N_L²/det₂ − q + r B̃_X/a_L^X with B̃_X smooth in (r, z, q) and in the 1-jet of
γ3; the first part vanishes identically at r = q = 0, so its difference for the two metrics at a point is at most
C (r + |q|) times the difference of their 1-jets there, and so is that of the second part. With |q̂| ≤ C ρ this gives
|g(ρ)| ≤ C ρ f(ρ). Put D(r) := sup_[0,r] |δq|; then |δh(ρ)| ≤ ρ D(ρ), and r |δq(r)| ≤ ∫_0^r (C_1 ρ D(ρ) + C_2 (ρ + C ρ) D(ρ)
+ |g(ρ)|) dρ ≤ C r² D(r) + ∫_0^r |g|. So D(r) ≤ C r D(r) + sup_(ρ≤r) ρ⁻¹ ∫_0^ρ |g|, and for C r_1 ≤ ½, by the
Cauchy–Schwarz inequality ρ⁻¹ ∫_0^ρ t f ≤ (∫_0^ρ t f²)^(1/2)/√2,

    D(r) ≤ C (∫_0^r t f² dt)^(1/2),      |δh(r)| ≤ C r (∫_0^r t f² dt)^(1/2),
    |δq(r)|/r ≤ C D(r) + r⁻² ∫_0^r |g| ≤ C ((∫_0^r t f² dt)^(1/2) + r⁻² ∫_0^r t f dt).

Together these give [[eq:class-leaf-arc]].

(c) Use the coordinates (z0, y) of (a) for V on 𝒰_(δ/2): x = (h_V(|y|; z0), y), with Jacobian ∂_(z0) h_V ∈ [½, 3/2]. As D
is G-invariant and closed under the arcs of V, for each z0 the set of y with x ∈ D ∩ 𝒰_(δ/2) is a disc {|y| < R(z0)} or
{|y| ≤ R(z0)}; the arc points of its points lie in D, and in 𝒰_δ, since they are within C δ² of x in z. For the
average 𝒜f(r) := r⁻² ∫_0^r t f(t) dt = ∫_0^1 s f(s r) ds and every R, Minkowski's inequality and ∫_0^R f(s r)² r dr =
s⁻² ∫_0^(sR) f² t dt give ‖𝒜f‖_(L²(r dr; [0,R])) ≤ ‖f‖_(L²(r dr; [0,R])), and ∫_0^R (∫_0^r t f² dt) r dr ≤ R² ∫_0^R t f²
dt. Square [[eq:class-leaf-arc]], integrate over the disc in y and then over z0, and change variables back: the L²
norms of invariant functions over 𝒰_δ and over the (z, y)-coordinates are comparable, the orbits of K1 having length
2π ρ1 ∈ [π ρ1(p), 3π ρ1(p)] there. ∎

**Lemma {#lem:class-leaf-tame}** (The planar shear on the ball 𝔅′.) In the setting of [[lem:class-leaf-differences]],
let U ∈ 𝔅′ with 𝒩_k(U) < ∞. Then ‖∂^α(σ[U] − σ[ů])‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U) for |α| ≤ k, with C depending only on 𝔅′, δ
and k.

*Proof.* Put Z := U − ů and U_s := ů + s Z, s ∈ [0, 1]; U_s ∈ 𝔅′, the ball being convex, and 𝒩_k(U_s) = s 𝒩_k(U).
By [[lem:sobolev]] at the order k − 4 ≥ 2 the C² norms of the first-order
variables of U_s − ů are at most C 𝒩_(k−1)(U) ≤ C on 𝔅′, so every U_s has bounds (M, c) in the sense of
[[lem:class-leaf-arc]] uniform in s, and its leaves foliate. For a leaf h_s := h_(U_s)(·; z0) the bound of step (3) of the
proof of [[lem:class-planar-shear]], which uses the leaf equation [[eq:class-leaf-cartesian]] only and constants
depending on sup |∂h_s|, sup |∂²h_s| and the 1-jet of γ3, gives ‖h_s‖_(H^(j+2)(𝔻)) ≤ C (‖H_L[U_s]‖_(H^j(𝔻′)) +
‖γ3^s‖_(H^(j+1)) + 1) for j ≤ k on nested discs 𝔻 ⊂ 𝔻′, so ‖h_s − h̊‖_(H^(k+2)) ≤ C (1 + 𝒩_k(U)) on the disc. The
derivative ζ := ∂_s h_s solves the leaf equation linearised at h_s, L_s ζ = (∂_s H_L[U_s]) − (∂_s 𝔪_s)(h_s), 𝔪_s the
mean-curvature map of [[eq:class-leaf-cartesian]] for γ3^s, with ζ = 0 at the axis; L_s is uniformly elliptic on the
disc with the axis interior ([[lem:class-leaf]] (b)), with principal coefficients smooth functions of (y, h_s, ∂h_s)
and lower coefficients of (y, h_s, ∂h_s, ∂²h_s), and the right side is linear in the 1-jet of Z with coefficients
smooth in (y, h_s, ∂h_s). Apply [[lem:class-interior-regularity]] with j = 0 to ∂^β ζ, |β| ≤ k, on nested discs, as in
step (3) of [[lem:class-planar-shear]]: the commutator [∂^β, L_s] ζ is a sum of products of a derivative of order
i ≥ 1 of the coefficients and a derivative of order |β| + 2 − i of ζ, and by [[thm:std-gn-moser]] (1) on the disc (after
Stein's extension) its L² norm is at most C (‖ζ‖_(H^(|β|+1)) + ‖h_s − h̊‖_(H^(|β|+2)) ‖ζ‖_(C²) + ‖ζ‖_(C²)), the C² and
C¹ norms of the coefficients being bounded on 𝔅′. By induction on |β|, with ‖ζ‖_(C²) ≤ C 𝒩_(k−1)(U) by
[[lem:sobolev]] and the case of lower order, ‖ζ‖_(H^(k+2)) ≤ C (𝒩_k(U) + (1 + 𝒩_k(U)) 𝒩_(k−1)(U)) ≤ C 𝒩_k(U). The
derivatives transverse to the disc, in z0 and in τ, are bounded in the same way by differentiating the linearised
equation, as in the proof of [[lem:class-leaf-differences]] (a), and the shift of the foliation enters as there. So
‖∂^α ∂_s σ[U_s]‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U), σ[U_s] being a smooth function of h_s, ∂h_s, H_L[U_s] and the 1-jet of γ3^s by
(b) of [[lem:class-leaf-arc]]; integrating in s gives the bound. ∎

### Block A2. Additions to the section on Kato's iteration (chapter 81)

The text of this block goes into [[sec:class-kato]] after [[rem:class-kato-model]]. It solves
[[eq:class-kato-system]] when the forcing term at a time depends on the solution over an interval of earlier times
and is controlled only in space-time norms. Such forcing terms arise when a non-local term is computed on the leaves
of hypersurfaces that are not the slices of the time: the fixed-time hypotheses (F1)–(F2) then fail, while their
integrated forms hold ([[rem:class-kato-memory]]).

*Space-time norms.* Keep the setting of this section, and let J = [a, b] be an interval. H^σ(J) is the space of
functions on J × R^d with all derivatives ∂_t^j ∂_x^β, j + |β| ≤ σ, in L²(J × R^d), with the norm of the sum of their
squared L² norms. 𝒳^σ(J) is the space of u with ∂_t^j u ∈ L^∞(J; H^(σ−j)) for 0 ≤ j ≤ σ, the derivatives in the sense
of distributions, and ⟦u⟧_(σ,J) := Σ_(j≤σ) ess sup_J ‖∂_t^j u‖_(H^(σ−j)). For u ∈ 𝒳^σ(J) and j ≤ σ − 1, ∂_t^j u is
Lipschitz into H^(σ−j−1), hence continuous, and its value at every t lies in H^(σ−j), with norm at most ⟦u⟧_(σ,J), a
closed ball of H^(σ−j) being weakly closed; and ‖u‖_(H^σ(J)) ≤ (b − a)^(1/2) ⟦u⟧_(σ,J). For f ∈ H^σ(J) and i ≤ σ − 1,
∂_t^i f and ∂_t^(i+1) f lie in L²(J; H^(σ−1−i)), so ∂_t^i f is continuous into H^(σ−1−i), with

    ‖∂_t^i f(t) − ∂_t^i f(t′)‖_(H^(σ−1−i)) ≤ |t − t′|^(1/2) ‖f‖_(H^σ([t′,t])),
    sup_J ‖∂_t^i f‖_(H^(σ−1−i)) ≤ ((b − a)^(−1/2) + (b − a)^(1/2)) ‖f‖_(H^σ(J)),                  {#eq:class-trace}

by ∂_t^i f(t) − ∂_t^i f(t′) = ∫_(t′)^t ∂_t^(i+1) f and the Cauchy–Schwarz inequality, and by averaging the first bound
over t′ ∈ J. If u ∈ 𝒳^σ([a, b]) and u′ ∈ 𝒳^σ([b, c]) have ∂_t^j u(b) = ∂_t^j u′(b) for j ≤ σ − 1, the function equal to u
on [a, b] and to u′ on [b, c] lies in 𝒳^σ([a, c]): its distributional derivatives of order j ≤ σ are the piecewise
ones, since those of order j − 1 are continuous at b. *Extension beyond b.* For an integer N ≥ 1 let c_1, …, c_N solve
Σ_l c_l (−1/l)^i = 1, 0 ≤ i ≤ N − 1, a Vandermonde system with the distinct nodes −1/l, and for b − a ≥ m > 0 and t ∈
(b, b + m] put (E_b u)(t) := Σ_l c_l u(b − (t − b)/l), and E_b u := u on [a, b]. Each term takes the values of u on
[b − m, b]; its j-th derivative is l^(−j) (∂_t^j u)(b − (t − b)/l); so for N = σ + 1, E_b maps 𝒳^σ([a, b]) into
𝒳^σ([a, b + m]) with ⟦E_b u⟧_(σ,[a,b+m]) ≤ C_E ⟦u⟧_(σ,[a,b]), C_E := Σ_l |c_l|, the derivatives of order at most σ − 1
matching at b, and ‖E_b u‖_(H^σ([b,b+m])) ≤ C_E ‖u‖_(H^σ([b−m,b])), ‖E_b u‖_(L²([b,b+m]×R^d)) ≤ C_E ‖u‖_(L²([b−m,b]×R^d)).

**Lemma {#lem:class-mixed-product}** (Products at one time.) Let σ1, σ2 ≥ σ ≥ 0 be integers with σ1 + σ2 − σ > d/2.

(a) ‖f g‖_(H^σ) ≤ C ‖f‖_(H^(σ1)) ‖g‖_(H^(σ2)), C depending only on d, σ1, σ2.

(b) Let Φ be as in [[lem:class-composition]], v ∈ 𝒳^s(J) with ⟦v⟧_(s,J) ≤ 𝔐, and 0 ≤ a ≤ s − 1. At every t ∈ J,
∂_t^a [Φ(t, ·, v(t))] = (∂_t^a Φ)(t, ·, v(t)) + R_a(t) with ‖R_a(t)‖_(H^(s−a)) ≤ C(𝔐), R_0 := 0, and multiplication by
(∂_t^a Φ)(t, ·, v(t)) is bounded on H^σ, σ ≤ s, with norm at most C(𝔐); R_a depends only on ∂_t^i v, i ≤ a, and its bound
on bounds of these.

*Proof.* (a) For |γ| ≤ σ, ∂^γ(fg) is a sum of terms ∂^(γ1) f ∂^(γ2) g with |γ1| + |γ2| ≤ σ; put α := σ1 − |γ1| ≥ 0 and
β := σ2 − |γ2| ≥ 0, so α + β > d/2. Choose p, q ∈ [2, ∞] with 1/p + 1/q = 1/2: p = ∞, q = 2 if α > d/2; p = 2, q = ∞ if
β > d/2; otherwise 1/p := 1/2 − α/d + λ and 1/q := 1/2 − β/d + λ with 2λ := (α + β)/d − 1/2 > 0, for which 0 < 1/p, 1/q ≤
1/2 since β − α ≤ d/2 and α − β ≤ d/2. On every unit cube Q of the lattice, [[thm:std-bh17-embedding]] (for finite
exponents, α − d/2 ≥ −d/p) and [[thm:std-bh-embedding]] (for the exponent ∞) give ‖F‖_(L^p(Q)) ≤ C ‖F‖_(H^α(Q)) and
‖G‖_(L^q(Q)) ≤ C ‖G‖_(H^β(Q)), C independent of Q by translation. With F := ∂^(γ1) f and G := ∂^(γ2) g, Hölder's
inequality on each cube and summation give ‖FG‖² ≤ Σ_Q C ‖F‖²_(H^α(Q)) ‖G‖²_(H^β(Q)) ≤ C ‖F‖²_(H^α) sup_Q ‖G‖²_(H^β(Q)) ≤
C ‖f‖²_(H^(σ1)) ‖g‖²_(H^(σ2)).
(b) By the chain rule ∂_t^a [Φ(t, x, v)] − (∂_t^a Φ)(t, x, v) is a sum, with coefficients depending on a, of terms
(∂_t^(a0) ∂_u^l Φ)(t, x, v)[∂_t^(a1) v, …, ∂_t^(al) v] with l ≥ 1, every a_i ≥ 1 and a0 + a1 + … + al = a. The product of
the l factors lies in H^(s−a1−…−al) ⊂ H^(s−a) by (a) applied l − 1 times, as (s − a1) + (s − a2) − (s − a1 − a2) = s >
d/2 and s − a ≥ 1, with the bound C 𝔐^l. A function Ψ(t, x, v) with Ψ smooth as Φ multiplies H^σ, σ ≤ s, with norm at
most C(𝔐): Ψ(t, x, 0) has bounded derivatives of every order, and ‖Ψ(t, ·, v) − Ψ(t, ·, 0)‖_(H^s) ≤ C(𝔐) by
[[lem:class-composition]] (b), so (a) with σ1 = s and σ2 = σ applies to it. ∎

**Lemma {#lem:class-kato-history}** (The linear problem with forcing in a space-time space and a history.) Let m > 0,
J_− := [t1 − m, t1], J := [t1, t2] and J_+ := [t1 − m, t2], with t2 − t1 ≤ T0. Let v ∈ 𝒳^s(J_+) with ⟦v⟧_(s,J_+) ≤ 𝔐,
𝐀^μ := A^μ(t, x, v), f ∈ H^s(J_+), and w̄ ∈ 𝒳^s(J_−) a solution of 𝐀^0 ∂_t w̄ + 𝐀^j ∂_j w̄ = f on J_−. There is exactly one
w ∈ C(J_+; L²) equal to w̄ on J_− that solves 𝐀^0 ∂_t w + 𝐀^j ∂_j w = f on J_+ with ∂_t w ∈ C(J_+; L²). It lies in
𝒳^s(J_+), and for t ∈ J, with E_s of [[lem:class-kato-linear]]:

(i) E_s(t; w)^(1/2) ≤ e^(C(t−t1)) (E_s(t1; w)^(1/2) + C (t − t1)^(1/2) ‖f‖_(H^s([t1,t]))), C depending on d, s, c0, 𝔐 and
bounds of order s for the A^μ;

(ii) for 1 ≤ j ≤ s and almost every t ∈ J, ‖∂_t^j w(t)‖_(H^(s−j)) ≤ B_j (‖w(t)‖_(H^s) + Σ_(i<j) ‖∂_t^i f(t)‖_(H^(s−1−i))),
B_j depending on d, s, c0, bounds of order s for the A^μ and a bound for ‖∂_t^i v‖_(L^∞(H^(s−i))), i ≤ j − 1;

(iii) ‖∂_t^i f(t)‖_(H^(s−1−i)) ≤ ‖∂_t^i f(t1)‖_(H^(s−1−i)) + (t − t1)^(1/2) ‖f‖_(H^s([t1,t])) for i ≤ s − 1.

*Proof.* By [[eq:class-trace]], f ∈ C(J_+; H^(s−1)). On J, v satisfies the hypotheses of [[lem:class-kato-linear]],
with ‖v(t)‖_(H^s) ≤ 𝔐 and Lipschitz constant 𝔐 into H^(s−1). For ε ∈ (0, 1] the mollified f_ε := J_ε f lies in
C(J; L²) with f_ε(t) ∈ H^s and sup_t ‖f_ε(t)‖_(H^s) ≤ C ε⁻¹ sup_t ‖f(t)‖_(H^(s−1)) < ∞, so part (b) of that lemma gives
a solution w_ε on J with w_ε(t1) = w̄(t1) and E_s(t; w_ε)^(1/2) ≤ e^(C(t−t1)) (E_s(t1; w̄)^(1/2) + C ∫_(t1)^t ‖f‖_(H^s)),
J_ε not increasing the norms. By part (a) of that lemma, sup_t ‖w_ε − w_(ε′)‖ ≤ C ∫_J ‖f_ε − f_(ε′)‖ → 0, since f_ε → f
in C(J; L²). As in step (4) of its proof the limit w lies in C(J; L²), w(t) ∈ H^s with the bound (i) (the integral of
‖f‖_(H^s) being at most (t − t1)^(1/2) ‖f‖_(L²([t1,t]; H^s)) ≤ (t − t1)^(1/2) ‖f‖_(H^s([t1,t]))), w_ε → w in C(J; H^(s−1)) by
[[eq:class-interpolation]], and passing to the limit in w_ε(t) = w̄(t1) + ∫_(t1)^t (𝐀^0)⁻¹ (f_ε − 𝐀^j ∂_j w_ε) shows that w
solves the equation with ∂_t w ∈ C(J; L²). Uniqueness is part (a) of [[lem:class-kato-linear]].

(ii) On J, ∂_t w = (𝐀^0)⁻¹ (f − 𝐀^j ∂_j w). Suppose that ∂_t^i w ∈ L^∞(J; H^(s−i)) for i < j, with the bounds (ii).
Differentiating j − 1 times in the sense of distributions, ∂_t^j w is a sum of terms ∂_t^a[(𝐀^0)⁻¹] ∂_t^b f and
∂_t^a[(𝐀^0)⁻¹] ∂_t^(b1)[𝐀^i] ∂_t^(b2) ∂_i w with a + b = a + b1 + b2 = j − 1. Write each factor ∂_t^a[Ψ(v)] as in
[[lem:class-mixed-product]] (b), a multiplier plus R_a ∈ H^(s−a); ∂_t^b f ∈ H^(s−1−b) and ∂_t^(b2) ∂_i w ∈ H^(s−1−b2). By
[[lem:class-mixed-product]] (a), every product of factors in H^(s−a), H^(s−b1) and H^(s−1−b2) lies in H^(s−1−a−b1−b2) =
H^(s−j), each exponent being at least s − j and the sum of any two exceeding the target by at least s > d/2; likewise
for the terms with f. The bound (ii) follows, with only ∂_t^i v, i ≤ j − 1, entering. The same products with one order
less show that ∂_t^j w is continuous into H^(s−j−1) for j ≤ s − 1, and ∂_t^s w ∈ L^∞(J; L²). So w|_J ∈ 𝒳^s(J). On J_−
the same identities hold for w̄, with the same v and f. At t1, w(t1) = w̄(t1), and by induction on j ≤ s − 1 the formula
gives ∂_t^j w(t1) = ∂_t^j w̄(t1), all its ingredients ∂_t^i v, ∂_t^i f (i ≤ j − 1) and ∂_t^i w (i < j) being continuous at
t1 into H^(s−j−1). So w ∈ 𝒳^s(J_+), by the concatenation property. (iii) is [[eq:class-trace]]. ∎

Fix m > 0, T0 > 0, a reference path u_* ∈ 𝒳^(s+1)([−2m, T0]) and ρ > 0, and put 𝔐_ρ := ⟦u_*⟧_(s+1,[−2m,T0]) + ρ. For
t̄ ∈ (−2m, T0] let 𝒫_t̄ := {u ∈ 𝒳^s([−2m, t̄]) : ⟦u − u_*⟧_(s,[−2m,t̄]) ≤ ρ}; every u ∈ 𝒫_t̄ has ⟦u⟧_(s,[−2m,t̄]) ≤ 𝔐_ρ.
Let F assign to every t̄ and every u ∈ 𝒫_t̄ a function F(u) ∈ H^s([−m, t̄]) such that, for −m ≤ t1 < t2 ≤ t̄ and u, u′ ∈
𝒫_t̄, with constants C_F and L:

(M0) if u = u′ on [−2m, t], then F(u) = F(u′) on [−m, t]; and F(u|_([−2m,t])) = F(u) on [−m, t];
(M1) ‖F(u)‖_(H^s([t1,t2])) ≤ C_F (t2 − t1 + m)^(1/2);
(M2) ‖F(u) − F(u′)‖_(L²([t1,t2]×R^d)) ≤ L ‖u − u′‖_(L²([t1−m,t2]×R^d)).

A *solution on [−m, t̄]* is a u ∈ 𝒫_t̄ with ∂_t u ∈ C([−m, t̄]; L²) and A^0(t, x, u) ∂_t u + A^j(t, x, u) ∂_j u = F(u) on
[−m, t̄]. The number m is the *memory*.

**Theorem {#thm:class-kato-memory}** (Kato's iteration with memory.) Assume (M0)–(M2).

(a) There are η ∈ (0, 1] and T* ∈ (0, m], depending only on d, s, c0, bounds of order s for the A^μ, ρ, m, 𝔐_ρ, C_F and
L, such that every solution on [−m, t1], 0 ≤ t1 < T0, with ⟦u − u_*⟧_(s,[−2m,t1]) ≤ η ρ extends to a solution on [−m,
min(t1 + T*, T0)]. Two solutions on [−m, t̄] that agree on [−2m, t1] agree. If u is a solution on [−m, t] for every
t < T2 ≤ T0, with ⟦u − u_*⟧_(s,[−2m,t]) ≤ η ρ for t < T2, then u extends to a solution on [−m, min(T2 + T*/2, T0)].

(b) (Stability.) Assume moreover that u_* satisfies A^0(t, x, u_*) ∂_t u_* + A^j(t, x, u_*) ∂_j u_* = F(u_*) + R on
[−m, T0], with R ∈ H^s([−m, T0]), and

(M1′) ‖F(u) − F(u_*)‖_(H^s([t1,t2])) ≤ C′ ‖u − u_*‖_(H^s([t1−m,t2])) for u ∈ 𝒫_t̄ and −m ≤ t1 < t2 ≤ t̄.

There are ε0 > 0 and C, depending on the quantities of (a), on C′ and on T0, such that every solution h on [−m, 0] with
δ := ⟦h − u_*⟧_(s,[−2m,0]) + ‖R‖_(H^s([−m,T0])) ≤ ε0 extends to a solution u on [−m, T0], with ⟦u − u_*⟧_(s,[−2m,T0]) ≤ C δ.

*Proof.* (a) *Uniqueness.* Let u, ũ be solutions on [−m, t̄] that agree on [−2m, t1]. z := u − ũ solves the linear
problem with the coefficients at u and the forcing term F(u) − F(ũ) − (A^μ(u) − A^μ(ũ)) ∂_μ ũ, continuous into L² by
[[eq:class-trace]]; ‖∂ũ‖_(L^∞) ≤ C_S 𝔐_ρ, and z = 0 before t1. By [[lem:class-kato-linear]] (a), the Cauchy–Schwarz
inequality and (M2), e(t) := ‖z(t)‖² satisfies e(t) ≤ C (t − t1) ∫_(t1)^t (L² + C) e for t ≥ t1, so e = 0.

*Existence.* Let u be a solution on [−m, t1] with ⟦u − u_*⟧_(s,[−2m,t1]) ≤ η ρ, η to be fixed, and h := u. Put u^0 :=
u_* + E_(t1)(h − u_*) on [−2m, t1 + m], with E_(t1) the extension beyond t1 (N = s + 1), so that ⟦u^0 − u_*⟧_s ≤ C_E η ρ
≤ ρ/2 for η ≤ 1/(2C_E), and let J := [t1, t1 + T], T ≤ min(T*, T0 − t1). For n ≥ 0 let u^(n+1) := h on [−2m, t1] and, on
J, the solution of [[lem:class-kato-history]] with v := u^n, f := F(u^n) on [t1 − m, t1 + T] and w̄ := h on [t1 − m, t1];
by (M0), F(u^n) = F(h) on [−m, t1], so w̄ solves the linear equation there. Suppose u^n ∈ 𝒫_(t1+T), u^n = h on
[−2m, t1]. Then u^(n+1) ∈ 𝒳^s([−2m, t1 + T]) by [[lem:class-kato-history]], and w := u^(n+1) − u_* solves on J the linear
problem with the coefficients 𝐀^μ := A^μ(u^n), the data h(t1) − u_*(t1) and the forcing term f_w := F(u^n) − 𝐀^μ ∂_μ u_*,
whose ingredients are those of [[lem:class-kato-history]] (with w̄ := h − u_*). By [[lem:class-mixed-product]] at each
time, ‖𝐀^μ ∂_μ u_*‖_(H^s([t1,t])) ≤ (t − t1)^(1/2) C(𝔐_ρ), u_* ∈ 𝒳^(s+1); with (M1), ‖f_w‖_(H^s([t1,t])) ≤ C (T + m)^(1/2).
By (i), with C_A := sup |A^0| at |u| ≤ C_S 𝔐_ρ, ‖w(t)‖_(H^s) ≤ c0^(−1/2) e^(CT) (C_A^(1/2) η ρ + C T^(1/2) (T + m)^(1/2)).
At t1 the equation for h gives f_w(t1) = A^μ(h) ∂_μ (h − u_*)(t1), and its time derivatives of order i ≤ s − 2 there are
those of A^μ(h) ∂_μ(h − u_*) from the left, by [[lem:class-kato-history]] applied to h; by [[lem:class-mixed-product]],
‖∂_t^i f_w(t1)‖_(H^(s−1−i)) ≤ C(𝔐_ρ) ⟦h − u_*⟧_(s)(t1) ≤ C η ρ. By (ii) for w and (iii),

    ⟦w⟧_(s,J) ≤ B (η ρ + T^(1/2) (T + m)^(1/2)),

B depending only on the quantities of (a). Choose η ≤ 1/(2B) and then T* so small that B T*^(1/2) (T* + m)^(1/2) ≤ ρ/2:
then ⟦u^(n+1) − u_*⟧_(s,[−2m,t1+T]) ≤ ρ, and u^(n+1) ∈ 𝒫_(t1+T). *Contraction.* For n ≥ 1, δ^(n+1) := u^(n+1) − u^n
vanishes on [−2m, t1] and solves on J the linear problem with the coefficients at u^n, data 0 and the forcing term
F(u^n) − F(u^(n−1)) − (A^μ(u^n) − A^μ(u^(n−1))) ∂_μ u^n, whose L²(J × R^d) norm is at most (L + C) T^(1/2) sup_J ‖δ^n‖ by
(M2). [[lem:class-kato-linear]] (a) and the Cauchy–Schwarz inequality give sup_J ‖δ^(n+1)‖ ≤ C T sup_J ‖δ^n‖ ≤
½ sup_J ‖δ^n‖ for T* small. *Limit.* So u^n → u in C([−2m, t1 + T]; L²). For each j ≤ s, ∂_t^j u^n is bounded in
L^∞(H^(s−j)), the dual of L¹(H^(j−s)); its weak-* limit points are ∂_t^j u, so ∂_t^j u^n converges weak-* to it, and
⟦u − u_*⟧_s ≤ ρ: u ∈ 𝒫_(t1+T). By [[eq:class-interpolation]], u^n → u in L^∞(H^(s−1)); by (M2), F(u^n) → F(u) in
L²(J × R^d). Passing to the limit in u^(n+1)(t) = h(t1) + ∫_(t1)^t (A^0(u^n))⁻¹ (F(u^n) − A^j(u^n) ∂_j u^(n+1)) gives
the same identity for u, with an integrand continuous into L², F(u) ∈ H^s([−m, t1 + T]) being continuous into L². So u is a
solution on [−m, t1 + T]. *Continuation.* With t1 := max(T2 − T*/2, 0), the solution on [−m, t1 + T*] given by the
first part agrees with u on [−2m, T2) by uniqueness.

(b) By (a), the solution u with history h exists on a maximal interval [−m, T_m) ∩ [−m, T0] on which ⟦u − u_*⟧_s ≤ η ρ.
Let τ1 < τ2 < T_m with τ2 − τ1 ≤ θ, θ ≤ m to be fixed, and z := u − u_*. z solves the linear problem with coefficients at
u and the forcing term f_z := F(u) − F(u_*) − R − (A^μ(u) − A^μ(u_*)) ∂_μ u_*, and ‖f_z‖_(H^s([τ1,τ])) ≤ C (‖z‖_(H^s([τ1−m,τ]))
+ ‖R‖_(H^s([τ1,τ]))) by (M1′) and [[lem:class-mixed-product]] at each time. At τ1, by the two equations, ∂_t^i f_z(τ1) =
∂_t^i(A^μ(u) ∂_μ z)(τ1) for i ≤ s − 2, so ‖∂_t^i f_z(τ1)‖_(H^(s−1−i)) ≤ C ⟦z⟧_s(τ1). Put X(τ) := ⟦z⟧_(s,[−2m,τ]); then
‖z‖_(H^s([τ1−m,τ])) ≤ (2m)^(1/2) X(τ). (i)–(iii) give, for τ ∈ [τ1, τ2],

    ⟦z⟧_(s)(τ) ≤ B′ (⟦z⟧_(s)(τ1) + θ^(1/2) X(τ) + ‖R‖_(H^s([−m,T0]))),

so X(τ2) ≤ B′ X(τ1) + B′ θ^(1/2) X(τ2) + B′ δ, and for B′ θ^(1/2) ≤ ½, X(τ2) ≤ 2B′ (X(τ1) + δ). Over the N := ⌈T0/θ⌉
intervals of length θ this gives X ≤ (4B′)^N δ =: C δ on [−2m, T_m). For C δ ≤ η ρ/2, (a) excludes T_m ≤ T0. ∎

**Remark {#rem:class-kato-memory}** (Why the hypotheses are integrated.) Let the forcing term be an average along arcs
that lie on hypersurfaces tilted against the slices: at a point x of the slice {t = t̄}, the value at x is an average of
an L² function over the arc from the axis to x on the hypersurface through x of a second foliation, whose points have
earlier times. On each slice of both foliations the function may be bounded in L² while the average is not bounded in
L² on the slice {t = t̄}: by a factor that grows like the square root of the logarithm of the inverse scale of the
function near the axis, the Jacobian of the map from the arcs to the slice vanishing at the axis. The square of the
space-time L² norm of the average is the integral over the second foliation of the squares of its L² norms on its
hypersurfaces, which are bounded. So (F2) fails for such terms, while (M2) holds; [[thm:class-kato-memory]] uses only
(M0)–(M2).
