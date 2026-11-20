### Block A1. Additions to the section on the planar shear at an axis (chapter 81)

The text of this block goes into [[sec:class-planar-shear]] after [[rem:class-leaf-numerics]]; the Placement section
gives the position. It compares the planar shears of two states leaf by leaf, along one arc from the axis, with no
smallness of their difference, and bounds the planar shear of a path of states in space-time in every Sobolev norm,
linearly in the norm of the path.

In the coordinates (z, y) of [[lem:class-leaf]] near a point p of axis 2 on a slice, a *state* is V = (g, p_A, Θ_A) on
𝒰_(2δ), smooth and G-invariant, with g Lorentzian and the slice spacelike for g. It has *bounds* (M, c) if the C² norms
of g and the C¹ norms of p_A and Θ_A on 𝒰_(2δ) are at most M, if A3, B3 and det₂ of [[lem:class-leaf]] are at least 1/M,
and if |p_A^Σ| ≥ c and p_A(∂_z) ≥ c on 𝒰_(2δ), p_A^Σ the spatial part of p_A. Its H_L is H_L[Θ_A] of
[[lem:class-leaf-differences]], with TΣ_L there the γ3-orthogonal complement in TM3 of p_A^Σ, so that H_L is a function
of position; its leaves are the solutions h(·; z0) of [[eq:class-leaf-volterra]] with h(0) = z0, and σ[V](x) is the
planar shear [[eq:class-shear-leaf]] of the leaf through x, with |p_A^Σ| for |∇_M3 u| and p_A(n) for n(u). For x on the
slice put r_x := |y(x)|. The *arc* of V through x is the part {(h(t; z0), t y(x)/r_x) : 0 ≤ t ≤ r_x} of the leaf through
x, z0 its axis point. For two states, |U − V| at a point is the sum of the absolute values of the differences of g, ∂g,
p_A and Θ_A there. A state may carry, in place of the first derivatives of g, a field 𝔤 of their type; H_L, the leaves
and σ are then computed with 𝔤 in place of ∂g, the C² norms of g in the bounds (M, c) read the C¹ norms of g and of 𝔤,
and |U − V| holds the difference of the 𝔤 in place of that of ∂g.

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

**Lemma {#lem:class-leaf-tame}** (Tame bounds for the planar shear in space-time.) Let t be a time function and x a
G-equivariant chart of its slices on a neighbourhood of 𝒱^0 := I × 𝒰̄_(4δ0)(p), where I is a compact interval of length
between 1 and L_I, p is a point of axis 2 with ρ1(p) > 0, 0 < δ0 ≤ ρ1(p)/4, and 𝒰_δ(p) is the set defined before
[[lem:class-planar-shear]] in the chart x; on each slice {t = const} use the coordinates (z, y) of [[lem:class-leaf]]. A
*state path* is a G-invariant W = (g, 𝔤, p_A, Θ_A) on a set of points (t, x) that is a state on each slice, with 𝔤 in
place of ∂g. Let W̊ be a smooth state path on a neighbourhood of 𝒱^0 with bounds (M, c) on every slice, and for δ ∈ (0,
δ0] put 𝒱_j := I × 𝒰_(jδ)(p), j = 1, 4. There are δ ∈ (0, δ0], r > 0 and, for every integer n ≥ 0, C_n such that for
every state path W on 𝒱_4 with ‖W − W̊‖_(C^5(𝒱_4)) ≤ r and W − W̊ ∈ H^n(𝒱_4), σ_A[W], computed on each slice, is defined
on 𝒱_1, and

    ‖σ_A[W] − σ_A[W̊]‖_(H^n(𝒱_1)) ≤ C_n ‖W − W̊‖_(H^n(𝒱_4)),                                       {#eq:class-leaf-tame}

H^n(𝒪) being the space of functions on 𝒪 with all derivatives in (t, x) of order at most n in L²(𝒪). δ and r depend only
on M, c, L_I, the chart and the C^6 norms of W̊ on 𝒱^0, and C_n also on n and the C^(n+6) norms of W̊.

*Proof.* Constants C depend only on the quantities named, and on n when n is fixed. By [[lem:class-leaf-arc]], with M
and c replaced by 2M and c/2, for r small every slice of every W of the lemma has bounds (2M, c/2) on 𝒰_(4δ0)(p), and we
take 4δ ≤ r_1 of that lemma, so that the leaves of W through the axis points z0 with |z0 − z(p)| < 3δ exist over the
disc 𝔻_(3δ) := {|y| < 3δ}, with |∂_y h| ≤ C|y| and ∂_(z0)h ∈ [1/2, 3/2]. As W ↦ σ_A[W] is continuous into L²
([[lem:class-leaf-arc]] (b)), a bounded set of H^n being weakly compact, and as W − W̊ is the limit in C^5 ∩ H^n of
smooth functions (mollify after Stein's extension, [[thm:std-sy-extension]]), it suffices to treat smooth W.

(1) *The leaf in divergence form.* Fix t and z0. For a function h on 𝔻_(3δ) let F := z − h(y), let ν be the γ3-gradient
of F divided by its length, a vector field on a neighbourhood of the graph that depends on (z, y) and on ∂h(y), and √γ
:= (det γ3)^(1/2) in the coordinates (z, y). The mean curvature of the graph is (√γ)⁻¹ ∂_a(√γ ν^a) at its points, ν
being the unit normal field of the graphs z = h(y) + const. Let 𝔙^i(y, z, P), i = 1, 2, be √γ ν^i at (z, y) with ∂h
replaced by P. Along the graph ∂_(y_i)[𝔙^i(y, h, ∂h)] = (∂_i(√γ ν^i) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)), ∂_z acting at fixed
∂h, so the graph has mean curvature H_L[W] exactly when

    div_y V = Φ,      V := 𝔙(y, h, ∂h),      Φ := (√γ H_L[W] − ∂_z(√γ ν^z) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)),       (D)

Φ a smooth function Φ_W(y, h, ∂h) of y, h, ∂h and of the values of W at (t, h(y), y). For an invariant state and an
invariant graph V is invariant, so V(y) = v(|y|) y, and the bounded solution of (D) is V = y 𝒜Φ, 𝒜Φ(y) := ∫_0^1 s Φ(s y)
ds: div(y 𝒜Φ)(y) = ∫_0^1 (d/ds)(s² Φ(s y)) ds = Φ(y), and the radial solutions of div V = 0 on 𝔻 ∖ {0} are the multiples
of y/|y|², which are unbounded. As ∂_P𝔙 = −√γ |dF|⁻¹ (γ3^(ij) − ν^i ν^j) is negative definite ([[lem:class-leaf]] (b)),
P ↦ 𝔙(y, z, P) has a smooth inverse V ↦ 𝔓(y, z, V) near the values of W̊. So the leaf through z0 satisfies

    P = 𝔓(y, h_P, y 𝒜Φ_W(·, h_P, P)),      h_P(y) := z0 + ∫_0^1 P(s y) · y ds,      P = ∂h.            (V)

On {P ∈ C(𝔻_(3δ)) : |P(y)| ≤ C_1 |y|} the right side of (V) has Lipschitz constant at most C δ in the sup norm, every
occurrence of P being multiplied by y or integrated against y, and it maps the set into itself for C_1 large and δ
small, P vanishing at y = 0 by invariance. So (V) has exactly one solution there. It is invariant, by uniqueness, so it
solves (D); its graph has mean curvature H_L[W] and passes through z0, so it is the leaf, by [[lem:class-volterra]]. The
right side of (V) at y holds P and W only at the points s y, s ∈ [0, 1], and at the graph points over them, that is on
the arc of the leaf from the axis.

(2) *The planar shear.* By [[lem:class-gauss]] (c), k_φ = ν(log |K2|) = ν(log r) + ½ ν(log B3), and ν(log r) = ν^i
y_i/|y|² = 𝒜Φ/√γ, by √γ ν^y = V = y 𝒜Φ. With σ_L = ½ H_L − k_φ ([[eq:class-leaf-volterra]]) and [[eq:class-shear-leaf]],
whose last term K_Σ(e_r, e_r) − K_Σ(e2, e2) is a smooth function of the point and of ∂h by invariance, as a_⊥ in
[[eq:class-axis-metric]] is, σ_A[W] at the point (h(y), y) is 𝔖(W(t, h, y), y, h, ∂h, 𝒜Φ) with 𝔖 smooth; no division
by |y| occurs.

(3) *The coordinates of the leaves.* On the box 𝒟̂ := I × {|z0 − z(p)| < 3δ} × 𝔻_(3δ) put Λ(t, z0, y) := (t, h(t, z0,
y), y), h the leaf of W, and Λ̊ likewise for W̊. Λ maps 𝒟̂ into 𝒱_4 with Jacobian ∂_(z0)h ∈ [1/2, 3/2], and Λ(𝒟̂) ⊃ 𝒱_1,
as in [[lem:class-leaf-arc]] (a). For F ∈ L²(𝔻_(3δ)) and j ≥ 0, Minkowski's inequality and ‖F(s ·)‖_(L²(𝔻_(3δ))) = s⁻¹
‖F‖_(L²(𝔻_(3sδ))) give

    ‖∫_0^1 s^(1+j) F(s ·) ds‖_(L²(𝔻_(3δ))) ≤ ‖F‖_(L²(𝔻_(3δ)))/(j + 1).                                       (H)

(4) *Bounds of low order.* Let π := P − P̊ and η := h − h̊ on 𝒟̂, P̊, h̊ those of W̊. (V) for W and for W̊, subtracted,
is a fixed-point equation for π with the contraction constant C δ and with the inhomogeneous term 𝔓(y, h̊, y 𝒜Φ_W(·, h̊,
P̊)) − 𝔓(y, h̊, y 𝒜Φ_(W̊)(·, h̊, P̊)), which is at most C sup |W − W̊| pointwise; and η = ∫_0^1 π(s y) · y ds. So
sup |π| + sup |η| ≤ C sup |W − W̊|. Differentiating (V) once or twice in (t, z0, y), the derivatives of π solve
fixed-point equations of the same form and contraction constant, whose inhomogeneous terms hold derivatives of W − W̊ of
order at most three and derivatives of (π, η) of lower order; so

    ‖π‖_(C²(𝒟̂)) + ‖η‖_(C²(𝒟̂)) ≤ C_0 ‖W − W̊‖_(C^4(𝒱_4)) ≤ C_0 r.                                         (L)

(5) *Products and compositions on 𝒟̂.* By Stein's extension ([[thm:std-sy-extension]]), bounded on H^m and on L^∞, the
interpolation inequality of the proof of [[lem:class-composition]] (a), max_(|γ|=j) ‖∂^γ f‖_(L^(2k/j)) ≤ C ‖f‖_∞^(1−j/k)
‖f‖_(H^k)^(j/k), holds on 𝒟̂ and on 𝒱_4, and so do [[thm:std-gn-moser]] (1) and [[lem:class-composition]] (a)–(c), D
denoting the derivatives in (t, z0, y). We show, for m ≥ 1 and F on 𝒱_4 with F ∈ H^m and ‖F‖_(C¹) ≤ 1,

    ‖F∘Λ‖_(H^m(𝒟̂)) ≤ C (‖F‖_(H^m(𝒱_4)) + ‖F‖_(C¹(𝒱_4)) ‖η‖_(H^m(𝒟̂))).                                       (C)

By the chain rule D^α(F∘Λ), |α| = m, is a sum of terms (∂^βF)∘Λ · Π_(i=1)^ℓ D^(α_i)Λ^(c_i), ℓ = |β| ≥ 1, |α_1| +
… + |α_ℓ| = m, every |α_i| ≥ 1. The factors with |α_i| ≤ 2 are bounded, by (L) and the smoothness of Λ̊. If all are of
this kind, the term is at most C |(∂^βF)∘Λ|, whose L² norm is at most C ‖F‖_(H^m), the Jacobian of Λ being at least 1/2.
Otherwise ℓ ≤ m − 2, and the factors D^(α_i)Λ with |α_i| ≥ 3 are D^(α_i)Λ̊, bounded, plus D^(α_i − e_i)(Dη), e_i a unit
index ≤ α_i. Write (∂^βF)∘Λ = (∂^(β−e)G)∘Λ with G := ∂_e F, e ≤ β, and let k′ := ℓ − 1 + Σ (|α_i| − 1), the sum over the
factors D^(α_i−e_i)(Dη), so that k′ ≤ m − 1. If k′ = 0 the term is at most C |G∘Λ|. Otherwise Hölder's inequality with
the exponents 2k′/(ℓ − 1) for the first factor and 2k′/(|α_i| − 1) for the factors D^(α_i−e_i)(Dη), whose reciprocals
add to 1/2, the change of variables Λ and the interpolation inequality at the order k′ for G on 𝒱_4 and for Dη on 𝒟̂
bound the term by C ‖G‖_∞^(1−θ_0) ‖G‖_(H^k′)^(θ_0) Π_i ‖Dη‖_∞^(1−θ_i) ‖Dη‖_(H^k′)^(θ_i), θ_0 + Σ_i θ_i = 1; by the
inequality between weighted geometric and arithmetic means, and ‖Dη‖_∞ ≤ C, this is at most C (‖G‖_(H^(m−1)) + ‖G‖_∞
‖η‖_(H^m)), which gives (C).

(6) *Induction.* Put 𝒩_m := ‖π‖_(H^m(𝒟̂)) + ‖η‖_(H^m(𝒟̂)) and 𝒩_(−1) := 0. We show 𝒩_m ≤ C (‖W − W̊‖_(H^m(𝒱_4)) +
𝒩_(m−1)). Let |α| = m and apply D^α to (V) and to its version for W̊. For a derivative ∂_y^β, ∂_y^β(y 𝒜F) = y ∫_0^1
s^(1+|β|) (∂^β F)(s ·) ds + Σ_e ∫_0^1 s^(|β|) (∂^(β−e) F)(s ·) ds e, the sum over the unit indices e ≤ β, and
derivatives in (t, z0) commute with 𝒜. So D^α π = ∂_V𝔓 · y ∫_0^1 s^(1+|β|) (∂_PΦ_W · D^α π + ∂_hΦ_W · D^α η)(s ·) ds +
𝔯_α, where 𝔯_α collects the terms of the chain rule in which every factor is a derivative of order below m of π or η, or
a derivative of order at most m of (W − W̊)∘Λ or of W̊∘Λ − W̊∘Λ̊, multiplied by derivatives of 𝔓, Φ_W and their versions
for W̊, smooth functions of bounded arguments. By (H) on each disc the first term is at most C δ (‖D^α π‖ + ‖D^α η‖) in
L²(𝒟̂). D^α η is ∫_0^1 D^α[π(s y) · y] ds, at most C δ ‖D^α π‖ + C 𝒩_(m−1) by (H). W̊∘Λ − W̊∘Λ̊ = Ψ(x, η) η with Ψ
smooth, so its H^m norm is at most C 𝒩_m by [[lem:class-composition]] (c) and (L). By (C) for F := W − W̊ and by
[[lem:class-composition]] (a) for the products, with the undifferentiated factors bounded by (L) and by r,
‖𝔯_α‖_(L²(𝒟̂)) ≤ C (‖W − W̊‖_(H^m(𝒱_4)) + 𝒩_(m−1)) + C r 𝒩_m. Summing over |α| ≤ m and absorbing C (δ + r) 𝒩_m for δ and
r small, which is possible as 𝒩_m is finite for smooth W, gives the claim. By induction, 𝒩_n ≤ C_n ‖W − W̊‖_(H^n(𝒱_4)).

(7) *Conclusion.* By (2), σ_A[W]∘Λ − σ_A[W̊]∘Λ̊ = 𝔖(W∘Λ, y, h, P, 𝒜Φ_W) − 𝔖(W̊∘Λ̊, y, h̊, P̊, 𝒜Φ_(W̊)), whose H^n(𝒟̂)
norm is at most C (‖W − W̊‖_(H^n(𝒱_4)) + 𝒩_n), by (C), [[lem:class-composition]] (b) and (c), (H) and W∘Λ − W̊∘Λ̊ = (W −
W̊)∘Λ + (W̊∘Λ − W̊∘Λ̊). σ_A[W̊]∘Λ − σ_A[W̊]∘Λ̊ is bounded by 𝒩_n in the same way. On 𝒱_1, Λ⁻¹ has derivatives that are
polynomials in those of h and in (∂_(z0)h)⁻¹ ∈ [2/3, 2], so (C) with Λ⁻¹ in place of Λ, whose proof uses only these
bounds and (L), gives [[eq:class-leaf-tame]]. ∎

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

(c) (Regularity.) Assume moreover that the A^μ and u_* are smooth, with u_* ∈ H^σ([−2m, T0]) for every σ, that R = 0 on
[−m, 0], that ‖R‖_(H^s([−m,T0])) ≤ ε0, and, for every integer σ > s,

(M1_σ) ‖F(u)‖_(H^σ([t1,t2])) ≤ C_σ (1 + ‖u‖_(H^σ([t1−m,t2]))) for u ∈ 𝒫_t̄ ∩ H^σ([−2m, t̄]) and −m ≤ t1 < t2 ≤ t̄.

Then, for ε0 small, the solution of (b) with the history h := u_* lies in H^σ([−2m, T0]) for every σ.

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
intervals of length θ this gives X ≤ (4B′)^N δ =: C δ on [−2m, T_m). For C δ ≤ η ρ/2, (a) excludes T_m ≤ T0.

(c) *A global iteration.* Let u^0 := u_* on [−2m, T0] and, for n ≥ 0, u^(n+1) := u_* on [−2m, 0] and, on [0, T0], the
solution of [[lem:class-kato-history]] with v := u^n, f := F(u^n) and w̄ := u_* on [−m, 0], which solves the linear
equation there, as R = 0 on [−m, 0] and F(u^n) = F(u_*) there by (M0). Put Y_n(τ) := ⟦u^n − u_*⟧_(s,[−2m,τ]) and fix 0 =
τ_0 < τ_1 < … < τ_N = T0 with τ_(i+1) − τ_i ≤ θ. The proof of (b), applied to z := u^(n+1) − u_* with the coefficients
at u^n, gives, as long as the u^j lie in the ball, Y_(n+1)(τ_(i+1)) ≤ B′ Y_(n+1)(τ_i) + B′ θ^(1/2) Y_n(τ_(i+1)) + B′ δ.
Put M_0 := 0 and M_(i+1) := 2B′ (M_i + δ), and take B′ θ^(1/2) ≤ ¼. If Y_n(τ_j) ≤ M_j for all j, then by induction on i,
Y_(n+1)(τ_(i+1)) ≤ B′ M_i + M_(i+1)/4 + B′ δ ≤ M_(i+1); as Y_0 = 0, this holds for all n, and M_N ≤ (4B′)^N δ ≤ ρ, δ :=
‖R‖_(H^s([−m,T0])) ≤ ε0, for ε0 small: every u^n lies in 𝒫_(T0). *Convergence.* δ^(n+1) := u^(n+1) − u^n vanishes on
[−2m, 0], and, as in the contraction of (a), ‖δ^(n+1)(t)‖ ≤ C t^(1/2) ‖δ^n‖_(L²([0,t]×R^d)); with Q_n := sup_t e^(−λt)
‖δ^n(t)‖, ‖δ^n‖²_(L²([0,t]×R^d)) ≤ Q_n² e^(2λt)/(2λ), so Q_(n+1) ≤ C T0^(1/2) (2λ)^(−1/2) Q_n ≤ ½ Q_n for λ large. So
u^n converges in C([−2m, T0]; L²); its limit is a solution, as in (a), within ρ of u_*, hence the solution u of (b), by
the uniqueness of (a).

*Higher norms.* We show by induction on σ ≥ s that L_σ := sup_n ‖u^n‖_(H^σ([−2m,T0])) < ∞; for σ = s, ‖u^n‖_(H^s) ≤
(T0 + 2m)^(1/2) 𝔐_ρ. Let σ > s with L_(σ−1) < ∞. For w := u^(n+1) put S_(n+1)(τ) := sup_([0,τ]) E_σ(t; w)^(1/2), with
E_σ of [[lem:class-kato-linear]]. (i) *Spatial energy.* Part (c) of [[lem:class-kato-linear]] at the order σ, on an
interval [τ_i, t], with v := u^n and f := F(u^n), gives E_σ(t; w)^(1/2) ≤ e^(C_* θ) (E_σ(τ_i; w)^(1/2) + C_* ∫_(τ_i)^t
(‖f‖_(H^σ) + K_w ‖v‖_(H^σ))), C_* and K_w bounded by the order s, the ball and bounds of order σ of the A^μ; it applies
with f and v replaced by J_ε f and J_ε v, whose values at each time lie in H^σ, and the bound passes to the limit ε → 0,
the solutions converging in C(L²) by part (a) of that lemma and the norms on the right not increasing. With (M1_σ) and
the Cauchy–Schwarz inequality, S_(n+1)(τ_(i+1)) ≤ e^(C_* θ) S_(n+1)(τ_i) + C θ^(1/2) (1 + ‖u^n‖_(H^σ([−2m,τ_(i+1)]))).
(ii) *Time derivatives.* On [0, τ], for j ≥ 1 and j + |β| ≤ σ, ∂_t^j ∂_x^β w = ∂_t^(j−1) ∂_x^β[(𝐀^0)⁻¹ (f − 𝐀^l ∂_l w)]
in the sense of distributions. Extend the factors to R × R^d in t by the operators E_b at both ends, bounded on every
H^σ′ and on L^∞; by [[thm:std-gn-moser]] (1) and [[lem:class-composition]] (b) in the d + 1 variables (t, x), every
product in which a derivative falls on (𝐀^0)⁻¹ or 𝐀^l, and every term with f, is bounded in L²([0, τ] × R^d) by C (1 +
L_(σ−1) + ‖F(u^n)‖_(H^(σ−1)([0,τ]))), the sup norms of v, ∂v, ∂w and f being bounded by the order s (f by
‖F(u^n)‖_(H^s), as s > (d + 1)/2); and ‖F(u^n)‖_(H^(σ−1)) ≤ C_(σ−1) (1 + L_(σ−1)) by (M1_(σ−1)) (by (M1) if σ − 1 = s).
The remaining term is (𝐀^0)⁻¹ 𝐀^l ∂_t^(j−1) ∂_x^β ∂_l w, with one time derivative fewer. By induction on j,
‖w‖_(H^σ([0,τ])) ≤ C (τ^(1/2) S_(n+1)(τ) + 1 + L_(σ−1)). On [−2m, 0], w = u_*, and at t = 0 all derivatives of w equal
those of u_* from the left, by the equation, as in [[lem:class-kato-history]]; so ‖w‖_(H^σ([−2m,τ])) ≤
‖u_*‖_(H^σ([−2m,0])) + C (τ^(1/2) S_(n+1)(τ) + 1 + L_(σ−1)). (iii) *Induction in n.* So S_(n+1)(τ_(i+1)) ≤ e^(C_* θ)
S_(n+1)(τ_i) + C θ^(1/2) (A + T0^(1/2) S_n(τ_(i+1))), A depending on L_(σ−1) and u_*. Let C_A ≥ sup |A^0| over the ball,
so that E_σ(t; u_*)^(1/2) ≤ C_A^(1/2) ‖u_*(t)‖_(H^σ) for the coefficients of every path in the ball; sup_([0,T0])
‖u_*‖_(H^σ) is finite by [[eq:class-trace]], u_* lying in H^(σ+1). Put S_0(τ) := C_A^(1/2) sup_([0,τ]) ‖u_*‖_(H^σ), M′_0
:= S_0(T0) + 1 and M′_(i+1) := 2 (e^(C_* θ) M′_i + C θ^(1/2) A), and take C θ^(1/2) T0^(1/2) ≤ ¼. If S_n(τ_j) ≤ M′_j for
all j, then S_(n+1)(τ_0) = E_σ(0; u_*)^(1/2) ≤ M′_0 and, by induction on i, S_(n+1)(τ_(i+1)) ≤ ½ M′_(i+1) + ¼ M′_(i+1);
as S_0(τ_j) ≤ M′_0 ≤ M′_j, this holds for all n, and L_σ < ∞ by (ii). (Each u^n lies in H^σ([−2m, T0]), by induction on
n with (i), (ii) and (M1_σ), so that (M1_σ) applies to it.) Since u^n → u in C(L²) and the u^n are bounded in H^σ([−2m,
T0]), u ∈ H^σ([−2m, T0]). ∎

**Remark {#rem:class-kato-memory}** (Why the hypotheses are integrated.) In the application ([[sec:loc-t5]]) the
forcing term at a point x of the slice {t = t̄} is computed on the hypersurface through x of a second foliation, tilted
against the slices, from the state on an arc of that hypersurface from the axis to x, whose other points have earlier
times. Its value on a slice is then a trace of a function that is controlled in space-time: the square of its space-time
norm is the integral, over the second foliation, of the squares of norms on its hypersurfaces, which
[[lem:class-leaf-arc]] controls at the order 0; at higher orders [[lem:class-leaf-tame]] bounds it in space-time
directly. This gives (M1), (M2), (M1′) and (M1_σ); the fixed-time hypotheses (F1) and (F2) would ask for bounds on each
slice {t = t̄} itself, which these estimates do not give. [[thm:class-kato-memory]] uses only the integrated hypotheses.
No proof uses this remark.

### Block B. Further dust families at the axes (chapter 83)

The text of this block is a new section of [[ch:localised-data]], placed immediately after [[sec:loc-axis]]; the
Placement section gives the position.

### Further dust families at the axes {#sec:loc-t5}

[[thm:loc-axis]] develops cone data through the axes with the two dust families adapted to the cones, of phases v and
u, and with no other ([[rem:loc-axis-scope]] (ii)). This section adds further null dusts, whose phases are not functions
of u or of v and whose densities may be nonzero where an edge meets an axis. At a point of an axis the gradient of a
phase of the class lies in the span of du and dv and is null, so it is a multiple of dv or of du: a further family
*crosses* the edge N_o along its generator in that axis, transversally, and is *tangent* to N_i along its generator
there, its rays running in N_i, or the reverse ([[lem:loc-t5-dichotomy]]). Cone data with any number of further families
that carry density only where they cross the edges, and none near the circles in which the corner sphere meets the axes,
are developed on the whole rectangle, with the regularity, the estimate and the uniqueness of [[thm:loc-axis]]
([[thm:loc-t5]]). A family that carries density where it is tangent to an edge at an axis is excluded, and the
reason is proved: no section of that edge by the slice of a time function is a leaf of the family there, while the
energy estimates of the construction need these sections to be leaves ([[prop:loc-t5-grazing]]). Such families are
developed on regions that avoid the axes near the points concerned ([[prop:loc-t5-cut]]).

The closure of the Raychaudhuri equation at an axis computes the planar shear at a point from the leaf through it, on
the arc from the axis to the point ([[sec:loc-axis-leaves]]). In [[sec:loc-axis-reduced]] the slices of the time are
unions of spheres of the data, which are leaves of both adapted families. For a further family they are not, and we
compute its leaves on the slices of a time t_A of its own, whose sections of the edge it crosses are its own sections of
that edge; the evolution time τ is bent near the axes so that every arc used lies in the past of its end point. The
forcing term at a time then depends on the solution over an interval of earlier times, and the Cauchy problem is solved
by [[thm:class-kato-memory]].

*The setting.* We keep the setting and the notation of [[sec:loc-axis-reduced]]: a background on Q1 := [0, u_1] × [0,
v_1] with margin δ_1, with Q^♯, N_o, N_i, N, F, P, S_c and C_* as there; τ0 denotes the time τ of [[eq:loc-axis-time]],
in the chart (τ0, y), with the numbers δ_c, s*, τ_init and the sets 𝒰^♯ and 𝔗(s) of [[eq:loc-axis-region]], for which Q1
⊂ 𝔗(s* − 1); Ů, Û and the reference metric Ĝ, built from Δ of [[lem:loc-axis-jets]] (c) with δ_e := δ_c/8, so that Û = Ů
on {τ0 ≤ τ_0′}, τ_0′ := ln(9δ_c²/16) > τ_init ([[sec:loc-cone-reduced]]); the cut-offs χ and θ, the compact sets 𝒰_2 ⊂
𝒰_3, the number δ, the radius ρ_- and the balls 𝔅 ⊂ 𝔅′ of the paragraph *The system* there; and 𝔄_χ, F̃ := (1 − θ 1_F)
𝔄_χ(Û) of [[eq:loc-cone-modified]], with 𝐔_c := 𝐔̊, ϒ, r_0 and A^μ_♭. Let k ≥ 9, m_0 := 6k + 18 and m_1 := 12k + 42 be
the numbers of [[thm:loc-axis]], and let the cone data through the axes, of size ε in C^(m_1), be extended to N_o and
N_i by [[lem:loc-axis-constraints]] (c), with the further sources of [[lem:loc-t5-jets]] (a). C and the smallness
conditions depend only on k, u_1, v_1, δ_1, the background, the background phases of the further families and the
numbers fixed below in terms of these, and not on ε.

#### Further families and their type at an axis {#sec:loc-t5-families}

**Definition {#def:loc-t5-family}** (Further families.) A *further family* A ∈ {3, …, N_f} consists of a smooth
G-invariant eikonal ů_A of g_e on a G-invariant neighbourhood 𝒩 of 𝒰_3, with dů_A ≠ 0 and P̊_A := g_e⁻¹p̊_A, p̊_A :=
−dů_A, future directed, and of data on the edges of Q1: a phase U_A and a density q_A ≥ 0, smooth and G-invariant on {0}
× [0, v_1] × S³ and on [0, u_1] × {0} × S³, with U_A − ů_A and q_A of size at most ε in C^(m_1). The family *crosses*
N_o at a point where g_e⁻¹(du, dů_A) ≠ 0, and N_i where g_e⁻¹(dv, dů_A) ≠ 0; these open sets of the edges are its
*crossing sets*. Let 𝒦_A := supp q_A. The data satisfy:

(F-a) 𝒦_A has positive distance from the circles S_c ∩ axis 1 and S_c ∩ axis 2;
(F-b) A crosses N_o at every point of 𝒦_A ∩ N_o and N_i at every point of 𝒦_A ∩ N_i;
(F-c) at every point of S_c at which A crosses both edges, for every j ≥ 1, the j-th u-derivatives of U_A and q_A along
N_i equal those that [[lem:loc-t5-jets]] (b) determines from the data on N_o, and the j-th v-derivatives along N_o those
it determines from the data on N_i.

A is of *ingoing type* at axis i if dů_A is a multiple of dv at the points of axis i in 𝒩, and of *outgoing type* if it
is a multiple of du there. Its *tangency set* at axis i is N_i ∩ axis i ∩ 𝒩 in the first case and N_o ∩ axis i ∩ 𝒩 in
the second; it contains the corner circle S_c ∩ axis i.

**Lemma {#lem:loc-t5-dichotomy}** (Crossing and tangency at the axes.) Let 𝒩 ∩ axis i be connected. A further family is
of ingoing type or of outgoing type at axis i. If it is of ingoing type, it crosses N_o at every point of N_o ∩ axis i ∩
𝒩, and at the points of its tangency set g_e⁻¹(dv, dů_A) = 0, the rays of ů_A through them being the generators of N_i
in the axis; likewise for outgoing type with the edges exchanged. So, by (F-b), a further family carries density at a
point where an edge meets an axis only if it crosses that edge there, and its density vanishes on a neighbourhood, in N,
of its tangency sets.

*Proof.* τ0 and |y| are functions of (u, v) whose differentials are independent ([[sec:loc-axis-reduced]]), so at a
point of axis i the span of dτ0 and d|y| is that of du and dv, and dů_A lies in it by the first claim of
[[lem:class-phase-axis]], whose proof uses of the chart only that G acts on y by its action on ℝ⁴. A null covector of
that span is a multiple of du or of dv, as g_e⁻¹(du, du) = g_e⁻¹(dv, dv) = 0 and g_e⁻¹(du, dv) ≠ 0. The two lines meet
only at 0, and dů_A is continuous and nonzero on the connected set 𝒩 ∩ axis i, so it stays on one of them. For ingoing
type, g_e⁻¹(du, dů_A) = λ g_e⁻¹(du, dv) ≠ 0 at the axis points of N_o, and g_e⁻¹(dv, dů_A) = λ g_e⁻¹(dv, dv) = 0 at
those of N_i; there P̊_A is a multiple of g_e⁻¹dv, which is tangent to the axis and to N_i, and its integral curves are
the generators of N_i in the axis. For the last claim, 𝒦_A is closed and contains no point of the compact tangency set,
by (F-b), so it has positive distance from it. ∎

So the tangency sets are where a family meets an edge with the edge's own orientation, the case in which two families
are not angularly separated at the axis ([[prop:class-separation]] (c)).

**Lemma {#lem:loc-t5-tubes}** (The tubes avoid the tangency sets.) Let A be a further family and 𝒦′ ⊂ N a compact
G-invariant set that satisfies (F-a) and (F-b). There are a neighbourhood 𝒲 of the tangency sets of A and ε_t > 0 such
that, for every smooth future causal vector field P within ε_t of P̊_A in C⁰ on 𝒰_3, no integral curve of P from a point
of 𝒦′ into F meets 𝒲 ∩ F ∩ 𝒰^♯.

*Proof.* Let p lie in the tangency set at axis i, of ingoing type say; then p = (u_p, 0) on the axis. By
[[lem:loc-t5-dichotomy]] the integral curve of P̊_A through p, followed backwards, is the axis generator of N_i; it
reaches the corner circle and then points with u < 0 in 𝒰_3, after a parameter length bounded uniformly in p ∈ 𝒰^♯. On
future causal vectors du and dv are nonnegative, so along a future causal curve u and v do not decrease, a curve that
starts in F stays in F, and a point x of F lies on a curve from a point of 𝒦′ exactly when the backward curve through x
leaves F through a point of 𝒦′. By continuous dependence on the initial point and on the field on a compact parameter
interval, for x near p and P near P̊_A in C⁰ the backward curve through x stays within any given distance of that
through p until it reaches u < 0; so it leaves F at a point of N near the segment of the axis generator of N_i from p to
the corner circle, that is at a point of N_i near its axis generator or of N_o near the corner circle. Neither lies in
𝒦′, by
(F-b) and [[lem:loc-t5-dichotomy]] on N_i and by (F-a) on N_o. Compactness of the tangency set in 𝒰^♯ gives 𝒲 and ε_t. ∎

(F-a) cannot be weakened to the vanishing of the density on the corner circles alone: by the proof above, a family of
ingoing type at axis i whose density is nonzero at points of N_o arbitrarily close to the corner circle has integral
curves that come arbitrarily close to its tangency set on N_i.

*Carrying a family near its tube.* For a further family A let 𝒦_A′ be as in [[thm:loc-t5]], a compact G-invariant
neighbourhood of 𝒦_A in N satisfying (F-a) and (F-b), let 𝒯̊_A be the union of the integral curves of P̊_A in F ∩ 𝒰^♯
from 𝒦_A′, and let B_A be the set of the points within 2δ_e, in u or in v, of the points of 𝒦_A on the same generator of
N, which contains the support of the density of the formal state below. Let ξ_A be a smooth G-invariant function,
supported in the interior of 𝒰_1 and equal to 1 on a neighbourhood of 𝒯̊_A ∪ B_A, whose support meets N only in the
crossing sets and does not meet the set 𝒲 of [[lem:loc-t5-tubes]] for 𝒦′ := 𝒦_A′, 𝒲 being taken disjoint from B_A, as we
may, shrinking it. This is possible: 𝒯̊_A ∩ N = 𝒦_A′ ∩ 𝒰^♯, since a curve that leaves N_o into F has u > 0 afterwards
and one that leaves N_i has v > 0, both being transverse to the edge at the start by (F-b); B_A ∩ N = 𝒦_A; and 𝒯̊_A ∪
B_A is compact and disjoint from the tangency sets. In the system below the rows (Aug2)–(Aug4) of family A are
multiplied by ξ_A and completed by 1 − ξ_A times the first-order form of P̄_A·∂, P̄_A of [[sec:loc-t5-system]], acting
on the difference of (p_A, Θ_A, q_A) from that of the formal state Û below. Family A enters the other rows only through
q_A; the row of q_A is homogeneous in q_A where ξ_A < 1, the formal density vanishing there. The phase data of family A
near its tangency sets, where the edge is characteristic for it and the jets of its phase are not determined by the data
([[prop:loc-t5-grazing]] (a)), are never used.

**Lemma {#lem:loc-t5-jets}** (Cone data and jets with further families.) (a) [[lem:loc-axis-constraints]] holds with E
:= Ric(g) − q_in dv ⊗ dv − q_out du ⊗ du − Σ_A q_A du_A ⊗ du_A, u_A = U_A on the edges, and with q_in + Σ_A q_A
(∂_vU_A)² in place of q_in in the equation for Y on N_o, q_out + Σ_A q_A (∂_uU_A)² in place of q_out on N_i, and the
inhomogeneous term −4Ω² γ⁻¹(Σ_A q_A ∂_vU_A dU_A|_(S³)) added in the equation for W, the sums over the further families.
The extension of its part (c) applies to U_A − ů_A and to q_A, the Borel sums of q_A beyond v_1 and u_1 being multiplied
by β_A(v − v_1), respectively β_A(u − u_1), with β_A smooth, equal to 1 near 0 and to 0 beyond a length ℓ_A ≤ δ_1 so
small that (F-a) and (F-b) hold for the extended data with the extended supports; their sizes are then at most Cε in
C^(m_0).

(b) Near every point of the crossing set of N_o the derivatives ∂_u^j u_A and ∂_u^j q_A on N_o of a class solution with
the data are determined recursively, as smooth G-invariant functions, by the eikonal equation and the transport (Aug4),
from the u-derivatives of the fields of order at most j − 1 and the derivatives of the data along N_o, and enter the
equations of [[lem:loc-axis-jets]] (b) for the derivatives of the fields of order j as inhomogeneous terms, through
∂_u^(j−1) of the stress. The same holds on N_i with u and v exchanged.

*Proof.* (a) On N_o, du_A(∂_v) = ∂_vU_A and du_A(X) = X(U_A) for X tangent to the spheres, while du(∂_v) = dv(∂_v) =
du(X) = dv(X) = 0; so Ric(g)(∂_v, ∂_v) − q_in is −(3/Y)(…) of [[eq:loc-axis-cone]] and equals Σ_A q_A (∂_vU_A)² when E
vanishes, and E(∂_v, X) = 0 adds Σ_A q_A ∂_vU_A X(U_A) to the second line of [[eq:loc-axis-cone]]. The added terms are
smooth G-invariant functions and 1-forms on the edges, dU_A|_(S³) being a smooth G-invariant 1-form on S³; the equation
for Y stays linear, with the coefficient (1/3)((1/4)|∂_vγ̂|²_γ̂ + q_in + Σ_A q_A (∂_vU_A)²) of Y, and the equation for W
gains an inhomogeneous term. So the proofs of (b) and (c) of [[lem:loc-axis-constraints]] apply verbatim, the Gronwall
bounds of (c) holding with these terms, of size Cε in C^(p−1). The Borel extension of q_A has its support, at each v ≥
v_1, in the angles of supp q_A ∩ {v = v_1}, as every term of the sum vanishes where all v-derivatives of q_A at v_1
vanish; the crossing sets are open and contain the compact set 𝒦_A ∩ {v = v_1}, so for ℓ_A small the extended support
lies in them and away from S_c. (b) In the double-null form [[eq:loc-double-null]], g^(uu) = g^(ua) = g^(vv) = 0, so on
N_o the eikonal equation g⁻¹(du_A, du_A) = 0 reads 2g^(uv) ∂_uu_A ∂_vU_A + 2g^(va) ∂_vU_A ∂_aU_A + g^(ab) ∂_aU_A
∂_bU_A = 0, linear in ∂_uu_A with the coefficient 2g^(uv) ∂_vU_A = 2g⁻¹(du, du_A), nonzero on the crossing set;
∂_u^(j−1) of it is linear in ∂_u^j u_A with the same coefficient, the other terms holding ∂_u^i u_A, i < j, and ∂_u^i of
the fields, i ≤ j − 1. P_A(q_A) + Θ_A q_A = 0 with Θ_A := div_g P_A = □_g(−u_A) is linear in ∂_uq_A with the coefficient
P_A^u = g^(uv) ∂_vU_A ≠ 0; ∂_u^(j−1) of it holds ∂_u^j q_A with this coefficient, ∂_u^i q_A for i < j, ∂_u^i u_A for i ≤
j and ∂_u^i of the fields for i ≤ j − 1, as □_g holds no ∂_u² (g^(uu) = 0). In the equations of [[lem:loc-axis-jets]]
(b) for the fields' derivatives of order j, the stress enters through ∂_u^(j−1)(q_A du_A ⊗ du_A), which holds ∂_u^i q_A,
i ≤ j − 1, and ∂_u^i u_A, i ≤ j, already determined; it enters 𝔏(0) only, as an inhomogeneous term. By induction on j
the recursion of [[lem:loc-axis-jets]] (b), with these equations added, determines all derivatives, as smooth
G-invariant functions near the crossing set, the axis generators included. ∎

Let ζ_A be a smooth G-invariant function on N, supported in the crossing sets and equal to 1 near supp ξ_A ∩ N. The
fields' derivatives a_j, b_k of [[lem:loc-axis-jets]] (b), now with the further families, and ζ_A times those of u_A −
ů_A and q_A, are smooth on the edges, and at S_c they agree in the sense of (i) of [[def:loc-cone-data]] by (F-c); the
Borel sums of [[lem:loc-axis-jets]] (a) and (c), at the scale δ_e of Δ, give the formal state Û with further families:
û_A := ů_A plus the sum for u_A − ů_A, p̂_A := −dû_A, Θ̂_A := div_Ĝ P̂_A, P̂_A := Ĝ⁻¹p̂_A, and q̂_A the sum for q_A,
supported in B_A, as the derivatives of q_A vanish on N ∖ 𝒦_A; Ů carries family A as (p̊_A, div_(g_e) P̊_A, 0). On a
neighbourhood of N ∩ {ζ_A = 1}, Ĝ⁻¹(dû_A, dû_A) and P̂_A(q̂_A) + Θ̂_A q̂_A vanish to infinite order on N, and the
residuals of [[lem:loc-axis-jets]] (c) vanish to infinite order on N with the further stress included. Û = Ů on {τ0 ≤
τ_0′}, and ‖Û − Ů‖_(C^(k+3)) ≤ Cε.

#### A closure time for each family {#sec:loc-t5-times}

Near axis i let ρ_i be the radius of [[sec:class-phases]] in the coordinates y, let χ_* ∈ C^∞([0, ∞)) equal 1 on [0, ½]
and 0 on [1, ∞), and put T_o(v) := τ0(0, v) and T_i(u) := τ0(u, 0), the restrictions of τ0 to the edges, which are
increasing. A further family A is *carried near axis i* if supp ξ_A meets {ρ_i ≤ δ}. Let A be carried near axis i and of
ingoing type there. By [[lem:loc-t5-dichotomy]], ∂_vů_A ≠ 0 on N_o ∩ axis i ∩ 𝒩, and U_A is within Cε of ů_A in C¹ on
the extended edge; so near the axis-i generator of N_o the sections {U_A = c} of N_o, its *A-sections*, are the graphs
v = V_A(c, ω) of smooth G-invariant functions. Fix v_A > 0 such that supp ξ_A ∩ N_o ∩ {ρ_i ≤ δ} lies in {v ≥ 2v_A}
([[lem:loc-t5-tubes]] and the choice of ξ_A). Then g_A := T_o(v) − T_o(V_A(U_A(v, ω), ω_i)), ω_i a point of S³ in axis
i, on which nothing depends by invariance, is a smooth G-invariant function on N_o ∩ {v ≥ v_A} near the axis-i
generator, zero on it; by Taylor's formula, as before [[eq:class-axis-metric]], g_A = Ĝ_A ρ_i² with Ĝ_A smooth and
G-invariant, and we extend Ĝ_A to a neighbourhood of 𝒰_3 near axis i as a function of (v, ω), independent of u. Let ψ_A
be a smooth function of (u, v) with values in [0, 1], equal to 1 on a neighbourhood of the points (u, v) of supp ξ_A ∩
{ρ_i ≤ δ} with u ≤ 2u_A, and to 0 for v ≤ v_A and for u ≥ 3u_A, where u_A > 0 is fixed so small that this is possible.
For outgoing type the same holds with N_i, U_A(u, ω), T_i and the roles of u and v exchanged. For the adapted families
put t_in := t_out := τ0, and for a further family

    t_A := τ0 − Σ_i χ_*(ρ_i/δ_*) ψ_A^(i) Ĝ_A^(i) ρ_i²,      τ := τ0 + K Σ_(i=1,2) χ_*(ρ_i/δ_*) ρ_i²,  {#eq:loc-t5-times}

the first sum over the axes near which A is carried, ψ_A^(i), Ĝ_A^(i) the functions above for axis i.

**Lemma {#lem:loc-t5-times}** (The closure times and the evolution time.) Let K := 1 + max_(A,i) sup |Ĝ_A^(i)|, the
supremum over supp ψ_A^(i) ∩ 𝒰_3 ∩ {ρ_i ≤ δ}. There are δ_* ∈ (0, δ/2] and ε_1 > 0 such that:

(a) on 𝒰_3, τ and every t_A are time functions for every Lorentzian metric within ε_1 of g_e in C⁰; (τ, y) and every
(t_A, y) are charts, their coordinate fields ∂_τ and ∂_(t_A) being positive multiples of the field ∂_(τ0) of the chart
(τ0, y), future timelike for g_e; and all of them equal τ0 where ρ1, ρ2 ≥ δ_*;
(b) on the edge that A crosses at axis i, at the points with ρ_i < δ_*/2 and ψ_A^(i) = 1, t_A is constant on every
A-section; the sections of N by the slices of τ0 are the spheres S_o(s) and S_i(s);
(c) let C_L ≥ 1; there is r_L > 0, depending on C_L and on δ_*, such that along every curve z = h(r), 0 ≤ r < r_L, in a
slice of t_A or of τ0, starting on the axis, with |h′(r)| ≤ C_L r, τ is strictly increasing;
(d) 0 ≤ τ − t_A ≤ m_* := (K + max sup |Ĝ_A^(i)|) δ_*², 0 ≤ τ − τ0 ≤ K δ_*² ≤ ½, and Q1 ⊂ {τ ≤ s* − ½}.

*Proof.* (a) With ρ := ρ_i, |d(χ_*(ρ/δ_*) ψ_A Ĝ_A ρ²)| ≤ C (δ_*⁻¹ δ_*² + δ_*) ≤ C δ_* on {ρ ≤ δ_*}, and likewise for the
bend of τ, C depending on K and on the C¹ norms of Ĝ_A and ψ_A, on 𝒰_3. dτ0 is timelike for g_e on the compact set 𝒰_3
with a margin ([[sec:loc-axis-reduced]]), so for δ_* small τ and t_A are time functions for the metrics within ε_1 of
g_e, and their derivatives along ∂_(τ0) are 1 + O(δ_*), the bends not depending on τ0 at fixed y beyond through ψ_A and
Ĝ_A, whose ∂_(τ0)-derivatives are bounded. So (t_A, y) is a chart, and its field ∂_(t_A), which is tangent to the curves
of constant y, is a positive multiple of ∂_(τ0). (b) On the edge, where χ_* = ψ_A = 1, t_A = T_o(v) − g_A = T_o(V_A(U_A,
ω_i)), a function of U_A alone. For τ0 this is [[lem:loc-axis-leaf]] (i) and [[sec:loc-axis-reduced]]. (c) On a slice of
t_A, τ = t_A + f with f := χ_*(ρ/δ_*)(ψ_A Ĝ_A + K) ρ² near axis i, the two bends using the same χ_*. For r < δ_*/2,
χ_* = 1, and along the curve, with ∂_ρ(ψ_A Ĝ_A) = O(ρ), ψ_A Ĝ_A being smooth and invariant,

    d/dr f(h(r), r) = 2 (ψ_A Ĝ_A + K) r + r² (∂_z(ψ_A Ĝ_A) h′ + ∂_ρ(ψ_A Ĝ_A)) ≥ 2 r − C (1 + C_L) r³ > 0

for r < r_L := min(δ_*/2, (C (1 + C_L))^(−1/2)), as ψ_A Ĝ_A + K ≥ 1. For the slices of τ0 the same holds with ψ_A Ĝ_A
replaced by 0. (d) f ≥ 0 and f ≤ (K + sup |Ĝ_A|) δ_*². Take K δ_*² ≤ ½; then Q1 ⊂ 𝔗(s* − 1) ⊂ {τ ≤ s* − ½}. ∎

Fix δ_* by (a) and (d). For every family A and every point x of a slice of t_A within r_L of an axis, the arc from the
axis to x of a curve of (c) lies in {τ ≤ τ(x)} and in {τ ≥ τ(x) − m_*}.

**Lemma {#lem:loc-t5-faces}** (The edge sections are leaves of each family.) Let A be a further family that crosses an
edge at its axis-i generator, at the points where (b) of [[lem:loc-t5-times]] holds, or an adapted family, and let V be
a state on a slice of t_A whose p_A, Θ_A, metric and first derivatives of the metric agree with those of Û at the points
of the edge section S of that slice, and whose A-leaves through the points of the axis near S exist over a disc 𝔻_(2δ′).
Then near its point on the axis S is V's A-leaf through it, and the parts of the slice on either side of S near that
point are unions of V's A-leaves.

*Proof.* For an adapted family this is [[lem:loc-axis-leaf]] (iii) and [[lem:loc-axis-past]]. Let A be further. By
[[lem:loc-axis-leaf]] (iii) it suffices to treat Û. S is a G-invariant hypersurface of the slice; the axis meets it
transversally, as dU_A does not vanish along the axis generator in the direction of the generator, so S ∩ M3 is a graph
z = h_S(y) with h_S smooth, and p̂_A(∂_z) ≠ 0 there, dû_A being near the axis a multiple of du or dv and ∂_z, the
direction of the axis in the slice, a combination of ∂_u and ∂_v with both coefficients nonzero, as t_A increases with u
and v along the axis. û_A = U_A on the edge, constant on S by [[lem:loc-t5-times]] (b), so p̂_A vanishes on TS. On S,
û_A is null for Ĝ to infinite order and ∇²û_A(P̂_A, ·) = ½ d(Ĝ⁻¹(dû_A, dû_A)) vanishes, so TS, spacelike, orthogonal to
the null P̂_A and not containing it, is a screen, and as in the proof of [[lem:loc-axis-leaf]] (iii), θ_S = −tr_(TS)
∇²(−û_A) = □_Ĝ(−û_A) = Θ̂_A. By [[lem:loc-axis-leaf]] (ii), S ∩ M3 is Û's A-leaf over the disc on which it is a graph.
The leaves foliate a neighbourhood of the axis point ([[lem:class-leaf-arc]] (a)) and do not cross, so a leaf that meets
one side of S near it stays on that side. ∎

#### The system with memory {#sec:loc-t5-system}

*The closure radius.* By compactness, as in the paragraph *The system* of [[sec:loc-axis-reduced]], there are M, c > 0,
δ′ ∈ (0, δ_*/4], ρ′ > 0 and C_L ≥ 1 such that, near every point p ∈ 𝒰_2 of an axis, in every slice of τ0, of τ and of
every t_A meeting 𝒰_2, every state within ρ′ of Ů in C^5 in the chart of that time has bounds (M, c),
[[lem:class-leaf-arc]] holds for it with r_1 ≥ 4δ′ and its leaves satisfy |h′(r)| ≤ C_L r, and [[lem:class-leaf-tame]]
holds in the charts (t_A, y) and (τ0, y), with W̊ := Ů, intervals I of length between 1 and L_I := s* − τ_init + 3m_* +
3, δ ≥ δ′ and r ≥ ρ′. Fix δ_♮ ∈ (0, δ′] with δ_♮ ≤ r_L of [[lem:loc-t5-times]] (c) for this C_L, and let ψ_♮ :=
ψ_♮0(ρ1) + ψ_♮0(ρ2), ψ_♮0 ∈ C^∞(ℝ) equal to 1 on [0, δ_♮/4] and to 0 on [δ_♮/2, ∞); it is smooth and G-invariant on 𝒰_3,
the sets {ρ1 ≤ δ_♮/2} and {ρ2 ≤ δ_♮/2} being disjoint there. Let 𝒰^♭ := {(u, v) : u, v > −δ_c, τ_init ≤ τ ≤ s*, u + κv ≤
l_u + δ_1/2, v + κu ≤ l_v + δ_1/2}. For δ_* small it lies in the interior of 𝒰_1, its boundary consists of pieces of
{τ = τ_init}, of {τ = s*} and of the far cuts, spacelike with 𝒰^♭ to their past as in (2) of [[sec:loc-axis-reduced]],
and F ∩ 𝒰^♭ = 𝒯 := F ∩ {τ ≤ s*} ⊂ 𝔗(s*), which contains Q1 by [[lem:loc-t5-times]] (d), as τ ≥ τ0 ≥ τ_c > τ_init on F.
We take ξ_A supported at positive distance from the far cuts, as we may, 𝒯̊_A lying in [0, l_u) × [0, l_v) and the
supports of the data in {u ≤ u_1 + ℓ_A} ∪ {v ≤ v_1 + ℓ_A}.

*The system.* For G-invariant states U = (g, p_A, Θ_A, q_A), A ∈ {in, out, 3, …, N_f}, let 𝒜^♮(U) = 0 be (Aug1), (Aug2)
and (Aug4) of [[sec:class-augmented]], with the reduced Ricci tensor and the gauge vector relative to Ĝ, together with,
in place of (Aug3),

    P_A(Θ_A) = (1 − ψ_♮) S_A + ψ_♮ S_A^ax,

with S_A of (Aug3) and S_A^ax of [[eq:loc-axis-closure]], its sum running over all families, and σ_A[U](x) the planar
shear at x of the A-leaf of U through x in the slice {t_A = t_A(x)}, computed in the chart (t_A, y) as in
[[sec:loc-axis-leaves]]; for a further family A all four rows of A are multiplied by ξ_A and completed as before
[[lem:loc-t5-jets]], with P̄_A := χ′ P̊_A + (1 − χ′) ∂_τ, χ′ a G-invariant function equal to 1 on 𝒰_2 and supported in
𝒩. Let 𝔄_χ and F̃ := (1 − θ 1_F) 𝔄_χ(Û) be defined by [[eq:loc-cone-modified]] in the chart (τ, y), with 𝒜^♮ in place of
𝒜 in the first-order form of Step 9 of the proof of [[thm:class-stability-off-axes]], its local terms evaluated at 𝐔̊ +
ϒ(𝐔 − 𝐔̊) and its terms in σ_A at 𝐔, and with P̄_A as here for the further families in A^μ_♭. The proofs of (a)–(c) of
[[lem:loc-axis-system]] apply: in the variables Z := 𝐔 − 𝐔̊ the system has the form [[eq:class-kato-system]], A^μ_χ(x,
Z) ∂_μZ = F(Z), with A^μ_χ symmetric and A^0_χ ≥ c_1 I, as ∂_τ is future timelike for g_e ([[lem:loc-t5-times]] (a)) and
every transport field of the rows, among them ξ_A P_A + (1 − ξ_A) P̄_A, has a positive τ-component; F(Z) is Φ(·, Z) of
the proof of [[lem:loc-axis-system]] (a), with the rows of the further families and the terms in σ_A included; where χ =
1 and |Z| ≤ r_0, 𝔄_χ(𝐔) = 𝒜^♮(𝐔); and g_τ = ∂_τ g, g_a = ∂_a g hold for all τ if they hold at one. The value of F(Z) at
a point x depends on Z at x and, through σ_A, on Z on the arcs used at x, which lie in {τ(x) − m_* ≤ τ ≤ τ(x)}
([[lem:loc-t5-times]], the remark after it). We apply [[thm:class-kato-memory]] with the time t := τ − τ_init, T0 := s*
− τ_init, s := k, u_* := 0, the memory m := 2m_* + 2 and a radius ρ ≤ ρ′/(C_E C_5), where C_E is the constant of the
extension E_b with N := k + 1 and C_5 is such that ‖Z‖_(C^5) ≤ C_5 ⟦Z⟧_(k,J) for Z ∈ 𝒳^k(J) on intervals J of length at
least 1, by [[lem:sobolev]] on the slices, as k − 5 > 2.

**Lemma {#lem:loc-t5-forcing}** (The forcing term.) F satisfies (M0), (M1), (M2), (M1′) and, for every σ > k, (M1_σ) of
[[thm:class-kato-memory]]; the constants depend on the quantities named in the setting.

*Proof.* Let Z be a path in 𝒫_t̄, and for t̄′ ≤ t̄ let Z_e := E_(t̄′) Z be its extension beyond t̄′ by the operator of
[[sec:class-kato]] with N := σ + 1, σ ≥ k the order considered, and with the length m_* + 1; ‖Z_e‖_(C^5) ≤ C_E C_5 ρ.
*(M0).* For x with τ(x) ≤ t̄′ the arcs used at x lie in {τ ≤ τ(x)}, where Z_e = Z; so F(Z) = F(Z_e) on {τ ≤ t̄′}, and
the value of F(Z) at a time t depends on Z on [t − m_*, t] only. *The local part.* It is a smooth function Φ_loc(x, Z)
with every derivative bounded on bounded sets of Z, and Φ_loc(x, Z) − Φ_loc(x, 0) = Ψ(x, Z) Z with Ψ smooth. By
[[lem:class-composition]] (b) and (c) in the five variables (τ, y), after Stein's extension from the slab
([[thm:std-sy-extension]]), its H^σ norm on [t1, t2] is at most C_σ ‖Z‖_(H^σ([t1,t2])), and its L² norm on [t1, t2] at
most C ‖Z‖_(L²([t1,t2])). *The terms in σ_A.* They are −½ χ ψ_♮ σ_A[𝐔]² in the rows of the closure, times ξ_A for a
further family, in the first-order form; χ ψ_♮ ξ_A is smooth with bounded derivatives. Fix t1 < t2 ≤ t̄ with t1 ≥ −m,
let Z_e := E_(t2) Z, and cover the axes in 𝒰_2 by finitely many sets 𝒰_(δ′)(p). At a point x near p with τ(x) ∈ [t1, t2]
and ρ_i(x) < δ_♮/2, t_A(x) ∈ [τ(x) − m_*, τ(x)] ⊂ I := [t1 − m_* − 1, t2]; so [[lem:class-leaf-tame]] in the chart (t_A,
y), with W := 𝐔̊ + Z_e and W̊ := 𝐔̊, bounds σ_A[𝐔] − σ_A[𝐔̊] in H^σ near x by C_σ ‖Z_e‖_(H^σ) on I × 𝒰_(4δ′)(p) ⊂ {t1 −
m_* − 1 ≤ τ ≤ t2 + m_*}, the change of chart (τ, y) ↦ (t_A, y) having bounded derivatives of every order with its
inverse. By the bound of E_(t2) the right side is at most C_σ ‖Z‖_(H^σ([t1−m,t2])). As σ_A[𝐔]² − σ_A[𝐔̊]² = (σ_A[𝐔] −
σ_A[𝐔̊])² + 2σ_A[𝐔̊] (σ_A[𝐔] − σ_A[𝐔̊]), with σ_A[𝐔̊] smooth and |σ_A[𝐔] − σ_A[𝐔̊]| ≤ C sup |Z_e| ≤ C ρ by
[[eq:class-leaf-arc]], [[cor:std-moser-product]] (1) after extension bounds the H^σ norm on [t1, t2] of the terms in
σ_A, minus their values at Z = 0, by C_σ ‖Z‖_(H^σ([t1−m,t2])). *(M1′) and (M1_σ).* So ‖F(Z) − F(0)‖_(H^σ([t1,t2])) ≤ C_σ
‖Z‖_(H^σ([t1−m,t2])), which is (M1′) at σ = k; F(0) = −R is smooth with compact support in x ([[lem:loc-t5-residual]]),
so ‖F(0)‖_(H^σ([t1,t2])) ≤ C_σ, which with the above gives (M1_σ). *(M1).* With σ = k, ‖F(0)‖_(H^k([t1,t2])) ≤ C (t2 −
t1)^(1/2) and ‖Z‖_(H^k([t1−m,t2])) ≤ (t2 − t1 + m)^(1/2) ρ. *(M2).* The local terms are Lipschitz in Z pointwise,
uniformly for |Z| ≤ C ρ. For two paths, [[lem:class-leaf-arc]] (c) on each slice {t_A = t′}, with D the whole slice,
gives ‖σ_A[𝐔_e] − σ_A[𝐔′_e]‖_(L²(𝒰_(δ′/2)(p)∩{t_A=t′})) ≤ C ‖𝐔_e − 𝐔′_e‖_(L²(𝒰_(δ′)(p)∩{t_A=t′})); with sup |σ_A|
bounded, squaring, integrating over t′ ∈ I by Fubini's theorem in the chart (t_A, y), and ‖E_(t2) f‖_(L² on
[t2,t2+m_*+1]) ≤ C_E ‖f‖_(L² on [t2−m_*−1,t2]), this gives (M2). ∎

**Lemma {#lem:loc-t5-residual}** (The residual.) (a) 𝔄_χ(Û) = F̃ on P, and F̃ is smooth and supported in supp χ.
(b) R := 𝔄_χ(Ů) − F̃ is smooth, supported in supp χ, zero on {τ0 ≤ τ_0′}, and sup_τ ‖R(τ)‖_(H^k) ≤ C ε.

*Proof.* (a) On P, θ 1_F = 0. F̃ = 𝔄_χ(Û) − θ 1_F 𝔄_χ(Û), and θ 1_F 𝔄_χ(Û) is smooth if 𝒜^♮(Û), which equals 𝔄_χ(Û) on
supp θ ⊂ {χ = 1}, |𝐔̂ − 𝐔̊| ≤ r_0 for ε small, vanishes to infinite order on N ∩ 𝒰^♭. Its local rows do, by
[[lem:loc-axis-system]] (d) and the paragraph after [[lem:loc-t5-jets]]: where ξ_A ≠ 0 near N, ζ_A = 1, and the rows of
family A vanish to infinite order there, (Aug1) holding the further stress; where ξ_A < 1 the completion vanishes for Û
identically. For an adapted family σ_A[Û] is that of [[lem:loc-axis-system]] (d), the spheres of the slices of τ0 being
its leaves, and its closure row is −E(P̂_A, P̂_A) by the proof there, with any partition ψ_♮ and with the further stress
in T̂. Let A be a further family, carried near axis i, and x near N with ψ_♮ ξ_A(x) ≠ 0; let d(x) be its distance from
N. x lies near the edge that A crosses at axis i, at a point where (b) of [[lem:loc-t5-times]] holds, since ξ_A vanishes
near the tangency sets; the slice {t_A = t_A(x)} meets that edge near x in an A-section S. Let W be the state (Ĝ, p̂_A,
θ_A) on the slice, θ_A(y) the expansion θ_S of [[lem:loc-axis-leaf]] (ii) for the level set of û_A through y in the
slice. By [[lem:loc-axis-leaf]] (ii) the level sets of û_A near the axis are W's A-leaves; S is one of them. Since
∇²û_A(P̂_A, ·) = ½ d(Ĝ⁻¹(dû_A, dû_A)), the difference Θ̂_A − θ_A = □_Ĝ(−û_A) − θ_A is a smooth function of (Ĝ, ∂Ĝ, dû_A,
∇²û_A) vanishing where Ĝ⁻¹(dû_A, dû_A) and its differential vanish, hence O(d^N) for every N near N ∩ {ζ_A = 1}. The
level set through x lies within C d(x) of S, hence of N, and so does its arc; [[lem:class-leaf-arc]] (b) with V := W and
U := Û gives |σ_A[Û](x) − σ(û_A)(x)| ≤ C_N d(x)^N, σ(û_A) := σ_A[W] the planar shear of the level sets of û_A. For û_A
the identities of [[prop:class-structure]] (b) and (c), with [[eq:class-x]], hold up to smooth functions vanishing where
Ĝ⁻¹(dû_A, dû_A) and its differential vanish, so the closure row of A at Û with σ(û_A) in place of σ_A is −E(P̂_A, P̂_A)
up to O(d^N), and the row at Û is O(d^N) for every N. It is smooth on a two-sided neighbourhood of N, Û being smooth and
its leaves depending smoothly on the point and on t_A ([[lem:class-leaf-tame]], step (1) of its proof), and a smooth
function that is O(d^N) for every N vanishes to infinite order on N, by Taylor's formula across N.
(b) R = (𝔄_χ(Ů) − 𝔄_χ(Û)) + θ 1_F 𝔄_χ(Û). On {τ0 ≤ τ_0′}, Û = Ů, the arcs used there lying in {τ ≤ τ(x)} ⊂ {τ0 ≤ τ_0′},
and θ 1_F = 0; so R = 0 there. The local part of the first term is bounded in C^k by C ‖Û − Ů‖_(C^(k+1)) ≤ C ε; its
terms in σ_A are bounded in H^k by C ε by [[lem:class-leaf-tame]] with W := Û, W̊ := Ů, on the compact support. On F ∩
supp θ, 𝔄_χ(Û) = (𝔄_χ(Û) − 𝔄_χ(Ů)) + 𝔄_χ(Ů), where 𝔄_χ(Ů) is the residual of (Aug1) for the reference Ĝ in place of g_e,
at most C ε in C^k, Ů solving the background's system on F with the true planar shears of its level sets in every
slicing ([[lem:class-leaf-differences]], last statement) and with zero densities of the further families. As 𝔄_χ(Û)
vanishes to infinite order on N, θ 1_F 𝔄_χ(Û) has H^k norm at most that of θ 𝔄_χ(Û) on F, at most C ε. ∎

**Lemma {#lem:loc-t5-existence}** (Existence and smoothness.) For ε small the system has a smooth G-invariant solution 𝐔
on [τ_init, s*] × ℝ⁴ with 𝐔 = 𝐔̊ on {τ ≤ τ_init}, g_τ = ∂_τ g, g_a = ∂_a g and ⟦𝐔 − 𝐔̊⟧_(k,[τ_init−2m,s*]) ≤ C ε; so the
derivatives of order at most k − 3 of 𝐔 − 𝐔̊ are at most C ε. For every further family A, the integral curves of P_A in
F ∩ 𝒰^♭ from 𝒦_A′ lie in {ξ_A = 1}.

*Proof.* The history Z := 0 on [τ_init − 2m, τ_init] is a solution there, F(0) = −R vanishing on {τ ≤ τ_init} ⊂ {τ0 ≤
τ_0′}. [[thm:class-kato-memory]] (b), with (M0)–(M2) and (M1′) by [[lem:loc-t5-forcing]] and δ := ‖R‖_(H^k([τ_init−m,
s*])) ≤ C ε by [[lem:loc-t5-residual]], gives a solution on [τ_init, s*] with ⟦Z⟧_k ≤ C ε; by (c) of that theorem, with
(M1_σ) and R = 0 on [τ_init − m, τ_init], Z lies in H^σ([τ_init − 2m, s*] × ℝ⁴) for every σ, so it is smooth by the
Sobolev inequality in the five variables. The rows of (c) of [[lem:loc-cone-system]] hold at τ_init, where 𝐔 = 𝐔̊. The
system is invariant under G, the times t_A and τ and the cut-offs being invariant, and the image of the solution under
an element of G is a solution with the same history; by the uniqueness of [[thm:class-kato-memory]] (a) it is the
solution. The pointwise bounds follow by [[lem:sobolev]] on the slices. With them P_A is within C ε of P̊_A in C⁰, so
for ε small the integral curves from 𝒦_A′ stay in the neighbourhood of 𝒯̊_A on which ξ_A = 1, by continuous dependence
on the field, and they avoid 𝒲 by [[lem:loc-t5-tubes]]. ∎

Below U denotes this solution, (g, p_A, Θ_A, q_A) its components and P_A := g⁻¹p_A.

#### Dependence on the past and the constraints {#sec:loc-t5-dependence}

**Lemma {#lem:loc-t5-energy}** (Energy with an integrated non-local term.) Let 𝒟, B_0, B_1, 𝐀^μ, M and 𝒟_s be as in
[[lem:loc-cone-energy]], in a chart (t, x) whose slices are spacelike for the systems concerned and without the
condition that the pieces of B_1 meet the slices transversally, and let z ∈ C¹(𝒟) solve 𝐀^μ ∂_μ z = Mz + 𝔫 on 𝒟, with
z = 0 on B_0 and 𝔫 measurable with ∫_(𝒟_s) |𝔫|² ≤ C_𝔫 ∫_(𝒟_s) |z|² for every s. Then z = 0 on 𝒟.

*Proof.* As in the proof of [[lem:loc-axis-energy]], the divergence theorem on the Lipschitz domains 𝒟_s gives e(s) ≤
∫_(𝒟_s) (C |z|² + 2 |z| |𝔫|) ≤ (C + 1 + C_𝔫) ∫_(𝒟_s) |z|² ≤ C′ ∫_(t_0)^s e, t_0 the least time on 𝒟, the integral over
B_1 being nonnegative and that over B_0 zero; Gronwall's inequality gives e = 0. ∎

**Lemma {#lem:loc-t5-past}** (The past of the edges.) U = Û on P ∩ 𝒰^♭. So U − Û vanishes with all its derivatives on N
∩ 𝒰^♭, g, the densities and the further phases induce the data there, and near the points where an edge meets an axis
the edge sections of the slices of t_A are leaves of U for every family A whose closure is used there.

*Proof.* On P, 𝔄_χ(𝐔) = F̃ = 𝔄_χ(Û) ([[lem:loc-t5-residual]] (a)). As in the proof of [[lem:loc-axis-past]], z := 𝐔 − 𝐔̂
satisfies on 𝒟 := the closure of P ∩ 𝒰^♭ a system 𝐀^μ ∂_μ z = Mz + 𝔫, with 𝐀^μ at 𝐔̂, M bounded and 𝔫 the difference of
the terms in σ_A, times bounded factors. Let B_0 := 𝒟 ∩ {τ = τ_init}, where z = 0, and B_1 the pieces of N and of the
far cuts; there the outward conormals are du, dv, du + κdv and dv + κdu, future causal for Ĝ and nonnegative on the
transport fields, which are future causal or, where ξ_A < 1, convex combinations of P_A and P̄_A; so the boundary matrix
is nonnegative (the paragraph after [[lem:loc-cone-energy]]). Let x ∈ 𝒟_s at which the closure of a family A is used, so
ρ_i(x) < δ_♮/2 for an axis i and, for a further family, ξ_A(x) ≠ 0, and let D := (𝒟 ∪ {τ ≤ τ_init}) ∩ {t_A = t_A(x)} ∩
{τ ≤ s}. Every point y of D near the axis has its arc of Û in D: in {τ ≤ τ(y)} by [[lem:loc-t5-times]] (c); in the
closure of P, since near a point where an edge meets axis i the edge section of the slice is a leaf of Û for A
([[lem:loc-t5-faces]]), A crossing that edge there, ξ_A vanishing near the tangency sets, or A being adapted; away from
the edges and from the far cuts, the arc being within C_L δ_♮² of y, for δ_♮ small; and ξ_A vanishing near the far cuts,
whose slices are unions of spheres, the leaves of the adapted families. The arcs in {τ ≤ τ_init} lie where z = 0.
[[lem:class-leaf-arc]] (c), with V := Û and U := U, gives ‖σ_A[U] − σ_A[Û]‖_(L²(D∩𝒰_(δ′/2)(p))) ≤ C
‖z‖_(L²(D∩𝒰_(δ′)(p))) at every point p of the axis; squaring and integrating over t_A(x), by Fubini's theorem in the
chart (t_A, y), ∫_(𝒟_s) |𝔫|² ≤ C ∫_(𝒟_s) |z|². [[lem:loc-t5-energy]] gives z = 0. The last claim is [[lem:loc-t5-faces]]
with V := U. ∎

**Lemma {#lem:loc-t5-constraints}** (The constraints.) Let 𝒦_A″ ⊃ 𝒦_A′ be the compact set defined in the proof, and 𝒯_A
the union of the integral curves of P_A in 𝒯 = F ∩ {τ ≤ s*} from 𝒦_A″. On 𝒯, g⁻¹(p_A, p_A) = 0, dp_A = 0 and Θ_A = div_g
P_A for the adapted families, and on 𝒯_A for every further family A, and D(g) = 0. There are smooth G-invariant
functions u_in, u_out on 𝒰′ := (P ∩ 𝒰^♭) ∪ 𝒯 and u_A on a neighbourhood of 𝒯_A with p_in = −du_in, p_out = −du_out,
p_A = −du_A, u_in = v and u_out = u on P ∩ 𝒰^♭ and u_A = û_A on P near 𝒦_A″; q_A vanishes on 𝒯 ∖ 𝒯_A; and (g, u_in,
u_out, u_A, q_in, q_out, q_A) solves [[eq:class-system]] with N_f families on 𝒯, with Ric(g) = Σ_A q_A du_A ⊗ du_A, in
the gauge D(g) = 0 relative to Ĝ, and with q_A ≥ 0 on Q1 for every family.

*Proof.* *The sets.* Let δ_2 > 0. Near the generator of the edge that A crosses at axis i, let 𝒦_A″ consist of 𝒦_A′ and
of the caps {ρ_i ≤ δ_2} of the A-sections that meet 𝒦_A′ ∩ {ρ_i ≤ δ_2}. For δ_2 small, 𝒦_A″ satisfies (F-a) and (F-b),
and we choose 𝒦_A′ and ξ_A for 𝒦_A″ from the start, as we may, so that the curves from 𝒦_A″ lie in {ξ_A = 1}
([[lem:loc-t5-existence]]). By [[lem:loc-t5-past]] the quantities below vanish, with all their derivatives, on N ∩ 𝒰^♭,
as they do for Û, on N ∩ {ζ_A = 1} for a further family. Every point of 𝒯 (of 𝒯_A) lies on an integral curve of P_A
that, followed backwards, stays in 𝒯 (in 𝒯_A ⊂ {ξ_A = 1}) until it reaches N: τ decreases along it at a rate bounded
below, and it cannot leave 𝒯 through its slice in {τ = s*}. *The phases.* For the adapted families this is the paragraph
*The phases* of the proof of [[lem:loc-axis-propagation]], with 𝒯 and 𝒰′ in place of 𝔗(s*) and its 𝒰′. For a further
family, on 𝒯_A, where ξ_A = 1, (Aug2) holds, and P_A(ν_A) = 0, ℒ_(P_A) dp_A = d(i_(P_A) dp_A) = 0 where ν_A = 0
([[prop:class-augmented]] (b)), ν_A := g⁻¹(p_A, p_A); so ν_A = 0 and dp_A = 0 on 𝒯_A, these vanishing on N. Then ℒ_(P_A)
p_A = d(i_(P_A) p_A) = dν_A = 0. Let u_A be constant along the integral curves of P_A and equal to û_A on N near 𝒦_A″;
then ℒ_(P_A) du_A = 0 and du_A = −p_A on N, so p_A = −du_A on 𝒯_A, and on a neighbourhood of it on which the curves are
defined. *The gauge and the expansions.* Let U′ be U with each Θ_A replaced by div_g P_A = □_g(−u_A) where u_A is
defined. For an eikonal u_A the level sets of u_A in a slice of t_A, near an axis, are leaves of U′, by
[[lem:loc-axis-leaf]] (ii): p_A vanishes on them, and their expansion is □_g(−u_A), as in the proof of its part (iii).
For s ≤ s* and a further family put D_(A,t,s) := 𝒯_A ∩ {t_A = t} ∩ {τ ≤ s}, and D_(A,t,s) := 𝒯 ∩ {t_A = t} ∩ {τ ≤ s} for
the adapted ones. Every point of D_(A,t,s) within δ_♮/2 of an axis has its arc of U′ in D_(A,t,s): in {τ ≤ s} by
[[lem:loc-t5-times]] (c); in F, the edge sections being leaves of U′ near the points where an edge meets the axis
([[lem:loc-t5-past]], [[lem:loc-axis-leaf]] (iii)) and leaves not crossing; and, for a further family, in 𝒯_A: the arc
lies in the level set of u_A through the point, whose points near the axis lie on integral curves of P_A from the cap of
that level set in the edge, contained in 𝒦_A″ for δ_♮ e^(L(s*−τ_c)) ≤ δ_2, L a Lipschitz constant of the flow of P_A,
the axis being invariant under the flow as [P_A, K_i] = 0. With Δ_A := Θ_A − div_g P_A, subtracting the equation of
[[eq:class-raychaudhuri]] for the eikonal from the closure row, as in the proof of [[lem:loc-axis-propagation]] and with
[[eq:class-defect]] off the axes and [[prop:class-augmented]] (e),

    P_A(Δ_A) = −Δ_A ((1 − ψ_♮)(Θ_A + div_g P_A − 2κ_A1 − 2κ_A2) + ½ ψ_♮ (Θ_A + div_g P_A − 2κ_A⊥))
               − ½ ψ_♮ (σ_A[U]² − σ_A[U′]²) + g(∇_(P_A) D, P_A) + L(P_A, P_A),

and D solves [[eq:class-gauge-wave]] with B_g T = Σ_A Δ_A q_A p_A. U′ has bounds (M, c) on the slices, the norm of
[[lem:loc-t5-existence]] controlling div_g P_A at the order k − 1, as in Step 10 of the proof of
[[thm:class-stability]]. [[lem:class-leaf-arc]] (c) with V := U′, U − U′ having the components Δ_A only, bounds the term
in σ_A in L²(D_(A,t,s) ∩ 𝒰_(δ′/2)(p)) by C ‖Δ_A‖_(L²(D_(A,t,s))). On 𝒯 ∩ {τ ≤ s} the edges are the past boundary, where
D, ∂D and Δ_A vanish; the lateral boundary of 𝒯_A is ruled by integral curves of P_A, so the transport of Δ_A has no
flux through it, and Δ_A is estimated on 𝒯_A only, as q_A, the only other entry of family A in the equations of D,
vanishes on 𝒯 ∖ 𝒯_A (below); and {τ = s} is spacelike. So the first-order variables of D and the Δ_A satisfy, on 𝒯, a
system of the form of [[lem:loc-t5-energy]], the non-local terms being bounded after integration over t by Fubini's
theorem, and D = 0, Δ_A = 0. Then (Aug1) is Ric(g) = Σ_A q_A p_A ⊗ p_A and (Aug4) the conservation law, as in the proof
of [[lem:loc-cone-constraints]]. *The densities.* The row of q_A is ξ_A (P_A(q_A) + Θ_A q_A) + (1 − ξ_A) P̄_A(q_A −
q̂_A) = 0, and q̂_A vanishes where ξ_A < 1, its support lying in the interior of {ξ_A = 1}; so q_A is transported along
the integral curves of ξ_A P_A + (1 − ξ_A) P̄_A, which on 𝒯 start on N, homogeneously, and vanishes along those that do
not start in 𝒦_A, where q_A = q̂_A = 0 on N. The curves from 𝒦_A lie in 𝒯_A, where ξ_A = 1. So q_A vanishes on 𝒯 ∖ 𝒯_A,
and along each curve keeps the sign of its value on N; a curve that reaches Q1 starts on N ∩ Q1, where the densities are
nonnegative, u and v not decreasing along it. ∎

#### Families tangent to an edge, uniqueness and the theorem {#sec:loc-t5-theorem}

**Proposition {#prop:loc-t5-grazing}** (Families tangent to an edge at an axis.) Let A be a further family of ingoing
type at axis i, x_0 a point of N_i ∩ axis i, and U a class solution near x_0 with N_f families in which the phase u_A of
family A is defined, equals U_A on N_i and satisfies |du_A − dů_A| < |dů_A| at the points of the axis near x_0. Let ϑ_i
be the distance on S³ from axis i, and a(u) := ½ ∂²U_A/∂ϑ_i² at the point (u, 0) of the axis generator of N_i.

(a) ∂_uU_A = 0 on N_i ∩ axis i near x_0, and the coefficient 2g⁻¹(dv, du_A) of ∂_vu_A in the eikonal equation on N_i
vanishes there: N_i is characteristic for family A along its axis generator, and the derivatives of u_A across N_i are
not determined there as in [[lem:loc-t5-jets]] (b).

(b) Let t be a time function near x_0, Σ its slice through x_0 and S := Σ ∩ N_i. If the restriction of U_A − U_A(x_0) to
S vanishes at x_0 to a finite order 2j in ϑ_i, as it does with j = 1 when a(u(x_0)) ≠ 0, the level set L of u_A in Σ
through x_0 meets S near x_0 only at x_0, and L ∖ {x_0} lies near x_0 on one side of N_i; and every neighbourhood of x_0
in Σ contains points on that side whose arcs from the axis along the level sets of u_A through them meet the other side.

(c) If, for every slice Σ′ of t through a point x′ of N_i ∩ axis i near x_0, the level set of u_A in Σ′ through x′
contains Σ′ ∩ N_i near x′, then U_A is constant on a neighbourhood of x_0 in N_i, du_A is a multiple of dv there, and
the rays of family A there are generators of N_i.

The same holds for outgoing type, with N_o, u and v exchanged.

*Proof.* (a) At a point of the axis du_A lies in the span of du and dv and is null ([[lem:loc-t5-dichotomy]]), so it is
a multiple of du or of dv; dů_A is a multiple of dv, and |du_A − dů_A| < |dů_A| excludes a multiple of du. So ∂_uu_A = 0
there, and on N_i, where u_A = U_A, ∂_uU_A = 0 on the axis generator. In the double-null form, g^(uu) = g^(ua) =
g^(vv) = 0, so the eikonal equation on N_i reads 2(g^(uv) ∂_uU_A + g^(va) ∂_aU_A) ∂_vu_A + g^(ab) ∂_aU_A ∂_bU_A = 0, and
the coefficient of ∂_vu_A is 2g⁻¹(dv, du_A). On the axis ∂_aU_A = 0, U_A being G-invariant and so even in ϑ_i, and
∂_uU_A = 0; so the coefficient vanishes, and ∂_u^(j−1) of the equation does not contain ∂_u^(j−1)∂_vu_A with a nonzero
factor.

(b) In the coordinates (z, y) of [[lem:class-leaf]] on Σ near x_0 (near axis 2, say), the axis meets N_i and L
transversally at x_0: its direction ∂_z in Σ is a combination of ∂_u and ∂_v with both coefficients nonzero, t
increasing with u and with v along the axis, and dv(∂_z) ≠ 0, du_A being a multiple of dv on the axis. So S ∩ M3 and L ∩
M3 are graphs z = h_S(y) and z = h_L(y) over a disc, with h_S(0) = h_L(0) = z(x_0), and the level sets of u_A in Σ
through the axis points z_0 near z(x_0) are graphs z = h(y; z_0) with |h(y; z_0) − h_L(y)| ≤ 2 |z_0 − z(x_0)|, as
∂_(z_0)h → 1 at y = 0. Parametrise S near x_0 by the point of S³ and write it u = u(x_0) + O(ϑ_i²), S being G-invariant
and transverse to the generators. By (a), U_A = c_0 + a(u) ϑ_i² + O(ϑ_i⁴), c_0 := u_A(x_0), so on S, U_A − c_0 =
a(u(x_0)) ϑ_i² + O(ϑ_i⁴), and in general U_A − c_0 = b_j ϑ_i^(2j) + O(ϑ_i^(2j+2)) on S with b_j ≠ 0, U_A being even in
ϑ_i. As u_A − c_0 = ∂_zu_A (z − h_L(y)) + O((z − h_L)²) near x_0 and ϑ_i is comparable with |y| on S, h_S − h_L has, for
small y ≠ 0, the sign of b_j/∂_zu_A, and |h_S − h_L| ≥ c_1 |y|^(2j) with c_1 > 0. This is the first claim. Let L lie,
off x_0, on the side z < h_S, say. For d > 0 small take the axis point z_0 := z(x_0) + d, on the other side. Then h(y;
z_0) − h_S(y) ≤ 2d − c_1 |y|^(2j) < 0 for |y| > (2d/c_1)^(1/(2j)): the level set through z_0 has points on the side of L
at radii between (2d/c_1)^(1/(2j)) and a fixed r_0, whose arcs from the axis start at z_0, on the other side. As d → 0
these points tend to x_0.

(c) The slices of t through the points x′ of the axis generator near x_0 meet N_i in the level sets of the restriction
of t to N_i, which has a nonzero derivative along the generators, dt being timelike and the generators null; so these
sets cover a neighbourhood of x_0 in N_i, each containing its point x′ of the axis. On Σ′ ∩ N_i near x′, U_A = u_A(x′) =
c_0, by (a). So U_A = c_0 on a neighbourhood of x_0 in N_i, du_A vanishes on the tangent spaces of N_i there, and du_A
is a multiple of the conormal dv of N_i; g⁻¹du_A is then tangent to the generators. ∎

So (F-b) excludes the families that carry density near a point x_0 of a tangency set because the construction of this
section, in any slicing, cannot treat them there. At every point x′ of the tangency set near x_0 at which, for the slice
through x′, the restriction of U_A − U_A(x′) to the edge section vanishes to a finite order, as when a(u(x′)) ≠ 0, the
arcs of points on one side of the edge arbitrarily near x′ meet the other side by (b), and the estimate of
[[lem:loc-t5-past]] (on P) or that of [[lem:loc-t5-constraints]] (on F), which needs the slices of the region to contain
the arcs of their points, fails for family A near x′: the arcs on the other side carry the solution of the other region.
If all the edge sections near x_0 are leaves, then by (c) the rays of family A run in the edge on an open set, the edge
is characteristic for the family there, as in (a), and its density there is not free data but must satisfy the transport
equation along the generators. In the remaining case the restriction vanishes to infinite order at x′ without vanishing
near it, and the construction is not analysed.

**Lemma {#lem:loc-t5-uniqueness}** (Dependence on the past faces with further families.) Let Ĝ′ be a smooth G-invariant
Lorentzian metric and, for i = 1, 2, U_i smooth G-invariant states with N_f families on a neighbourhood 𝒪 of a compact
set R′, each p_i^A the negative of the differential of a phase null for g_i, P_i^A := g_i⁻¹p_i^A future directed and
Θ_i^A = div_(g_i) P_i^A, the phases of the further families being defined on the sets given below, that solve
[[eq:class-system]] with N_f families on R′ in the gauge D(g_i) = 0 relative to Ĝ′. Let (ũ, ṽ, ω̃) be coordinates on 𝒪
with p_1^out = −dũ and p_1^in = −dṽ, in which g_1 has the form [[eq:loc-double-null]] with fields smooth through the
axes and R′ = [0, a] × [0, b] × S³. For every further family A let 𝒦_A″ be a compact G-invariant subset of the past
faces R′ ∩ ({ũ = 0} ∪ {ṽ = 0}) on which family A of U_1 crosses the face it lies in, at positive distance from the
circles in which {ũ = ṽ = 0} meets the axes, and which contains, with each of its points within δ_2 > 0 of an axis, the
cap within δ_2 of that axis of the section of the face by the level set of the phase of A of U_1 through the point; let
𝒯_A be the union of the integral curves of P_1^A in R′ from 𝒦_A″, let the phases of A of U_1 and U_2 be defined on a
neighbourhood of 𝒯_A, and let the densities of A of both vanish on R′ ∖ 𝒯_A. If U_2 and U_1 agree, with all their
derivatives, on the past faces, then U_2 = U_1 on R′. No smallness of U_1, of U_2 or of U_2 − U_1 is assumed.

*Proof.* *Times.* Let μ and x := e^(ṽ−μũ) ω̃ be as in the proof of [[lem:loc-axis-dependence]]. For an integer N ≥ 1 put
Φ_N := (ũ/a)^N + (ṽ/b)^N + (ũ + ṽ)/(N(a + b)); its derivatives in ũ and ṽ are positive near R′, so dΦ_N is timelike for
g_1, which has g_1^(ũũ) = g_1^(ṽṽ) = 0 and g_1^(ũṽ) < 0, and (Φ_N, x) is a chart whose field ∂_(Φ_N), a positive
multiple of ∂_ũ + μ∂_ṽ, is future timelike for g_1. The construction of [[sec:loc-t5-times]], with Φ_N in place of τ0,
the faces of R′ in place of the edges, the sections of the faces by the level sets of the phases of U_1, the sets 𝒯_A in
place of the supports of the ξ_A and g_1 in place of g_e, gives times t_A^N, an evolution time τ^N and numbers δ_*(N),
r_L(N), for which (a)–(d) of [[lem:loc-t5-times]] hold, with δ_*(N) chosen also with K(N) δ_*(N)² ≤ 1/(4N). The proof of
[[lem:loc-t5-times]] uses of τ0 and g_e only these properties. Let δ_♮(N) be a closure radius for U_1 in these charts as
in [[sec:loc-t5-system]]. U_1 and U_2, being solutions with null phases, solve the rows of 𝒜^♮ with ψ_♮ of radius
δ_♮(N), Ĝ′ in place of Ĝ and σ_A computed in the slices of t_A^N, at every point x near an axis at which the level set
through x of the phase of family A, in the slice through x, is from the axis to x a graph as in [[lem:loc-axis-leaf]]
(ii) in 𝒪 with p_A(∂_z) ≠ 0: by that lemma it is then the leaf through x, and the paragraph *The equations* of the proof
of [[lem:loc-axis-dependence]] applies to every family. For U_1 this holds at every point of R′ within δ_♮(N)/2 of an
axis, after decreasing δ_♮(N), U_1 being smooth on the compact R′ and its leaves satisfying |h′| ≤ C_L r.

*Triangles.* By the proof of [[lem:loc-t5-tubes]], with P_1^A in place of P̊_A and the tangency sets of family A of U_1
on the faces, 𝒯_A avoids a neighbourhood of those sets, so near the axes the closure of a further family is used only
near the faces it crosses. Let T_N := {ũ, ṽ ≥ 0} ∩ {τ^N ≤ 1}. As τ^N ≥ Φ_N ≥ (ũ/a)^N, (ṽ/b)^N, T_N ⊂ R′, and every point
with ũ < a and ṽ < b lies in T_N for N large, since Φ_N tends to 0 there and τ^N − Φ_N ≤ 1/(4N). For s ≤ 1 and a family
A put D_(A,t,s) := T_N ∩ {t_A^N = t} ∩ {τ^N ≤ s}, intersected with 𝒯_A for a further family. As in the proof of
[[lem:loc-t5-constraints]], with U_1 in place of U′ and the cap condition on 𝒦_A″ in place of its choice there, every
point of D_(A,t,s) within δ_♮(N)/2 of an axis has its arc of U_1 in D_(A,t,s), after decreasing δ_♮(N): the sections of
the faces by the slices of t_A^N are leaves of U_1 near the axes, by the proof of [[lem:loc-t5-faces]] with U_1 in place
of Û.

*Continuity in τ^N.* Fix N, and let s_* be the supremum of the s ∈ [0, 1] with U_2 = U_1 on 𝒦_s := T_N ∩ {τ^N ≤ s}; the
set of these s is closed and contains 0, 𝒦_0 lying in the past faces. Suppose s_* < 1. U_2 − U_1 is smooth and vanishes
with all derivatives on 𝒦_(s_*), and on the past faces by hypothesis. For θ ∈ (0, 1] let 𝒩_θ be the set of points of 𝒪
whose coordinates (ũ, ṽ) lie within θ of those of a point of 𝒦_(s_*) or of the past faces of R′ with the same ω̃; as in
the paragraph *Continuity in t* of the proof of [[lem:loc-axis-dependence]], Taylor's formula along the segment to a
nearest such point bounds the derivatives of order at most k of U_2 − U_1 on 𝒩_θ by Cθ^(k+1), and with a G-invariant
cut-off χ_θ equal to 1 on 𝒩_(θ/2), supported in 𝒩_θ, with derivatives of order j at most Cθ^(−j), W := U_1 + χ_θ (U_2 −
U_1) is within Cθ of U_1 in C^k. For θ small W has, on the slices of every t_A^N, the bounds of U_1 doubled, and its
slices are spacelike for its metric. Along the curves of constant x, on which τ^N grows at a rate bounded below near R′,
every point of T_N ∩ {s_* ≤ τ^N ≤ s_* + θ′} lies within Cθ′ of 𝒦_(s_*) or of the past faces; for θ′ := θ/(8C) the slab
lies in 𝒩_(θ/8), and the arc of U_1 through each of its points near an axis lies in T_N ∩ {τ^N ≤ s_* + θ′}, by the arc
property of the sets D_(A,t,s), hence in 𝒩_(θ/8) ∪ 𝒦_(s_*). While the arc of the leaf of W through such a point stays in
𝒩_(θ/2), where W = U_2, it lies within Cθ² of that of U_1 in C¹; so it stays there, is the arc of the leaf of U_2 by the
uniqueness in [[lem:class-volterra]], and σ_A[W] = σ_A[U_2] at the point. Likewise the level set of the phase of A of
U_2 through the point is a graph within Cθ² in C¹ of that of U_1, in 𝒩_(θ/2) ⊂ 𝒪, so U_2 solves the rows of 𝒜^♮ there,
with σ_A[W]. So the difference z of the first-order variables of U_2 and U_1, for a further family on 𝒯_A only,
satisfies on 𝒟 := T_N ∩ {s_* ≤ τ^N ≤ s_* + θ′} a system 𝐀^μ ∂_μ z = Mz + 𝔫, with 𝐀^μ at U_1, M bounded and 𝔫 the
difference of the terms in σ_A, times bounded factors. [[lem:class-leaf-arc]] (c) with V := U_1 and U := W on the sets
D_(A,t,s), where W − U_1 = z on the slab and 0 on 𝒦_(s_*), and Fubini's theorem in the charts (t_A^N, x) give
∫_(𝒟_s) |𝔫|² ≤ C ∫_(𝒟_s) |z|². The boundary of 𝒟 consists of the slice {τ^N = s_*} and pieces of the past faces, where
z = 0 (B_0), of the slices {τ^N = s}, spacelike for g_1, and of the lateral boundaries of the 𝒯_A, ruled by integral
curves of P_1^A, through which the transports of family A have no flux; the densities of A of both vanishing off 𝒯_A,
family A enters the other rows only on 𝒯_A. [[lem:loc-t5-energy]] gives z = 0 on 𝒟, against the definition of s_*. So
s_* = 1, and U_2 = U_1 on T_N for every N, hence on R′ ∩ {ũ < a, ṽ < b}, and on R′ by continuity. ∎

**Theorem {#thm:loc-t5}** (Development with further families at the axes.) Let k ≥ 9, m_0 = 6k + 18 and m_1 = 12k + 42,
let a background on Q1 with margin δ_1 be given, cone data through the axes ([[def:loc-axis-data]]) on {0} × [0, v_1]
and [0, u_1] × {0}, in the normalised gauge and with nonnegative densities, and further families A = 3, …, N_f
([[def:loc-t5-family]]) satisfying (F-a), (F-b) and (F-c); fix for each A a compact G-invariant neighbourhood 𝒦_A′ of
𝒦_A in N satisfying (F-a) and (F-b). Let ε be the largest size in C^(m_1) of the cone data and of the U_A − ů_A and q_A.
(F-b) excludes the families that carry density where they are tangent to an edge along an axis generator, as the
construction cannot treat them there ([[prop:loc-t5-grazing]]); (F-a) excludes density near the circles in which the
corner sphere meets the axes, where the rays of a crossing family approach its tangency set ([[lem:loc-t5-tubes]]).

A *class solution with the further families* on D × S³, D ⊂ F, is a class solution in the gauge through the axes on D ×
S³ ([[def:loc-axis-data]]) together with, for each further family, a smooth G-invariant density q_A ≥ 0 on D × S³ and a
smooth G-invariant phase u_A, null for g with −g⁻¹du_A future directed, defined on a neighbourhood of the union 𝒯_A^g of
the integral curves of −g⁻¹du_A in D × S³ from 𝒦_A′, such that q_A = 0 off 𝒯_A^g, Ric(g) = q_in dv ⊗ dv + q_out du ⊗
du + Σ_A q_A du_A ⊗ du_A and div_g(q_A g⁻¹du_A) = 0; it *induces the data* on the edges of D if g, q_in and q_out induce
the cone data and u_A = U_A and q_A equals the data on 𝒦_A′ ∩ D × S³. There are ε_0, C, ε_2 > 0, depending only on k,
u_1, v_1, δ_1, the background, the ů_A and the 𝒦_A′, such that for ε ≤ ε_0:

(a) *Existence.* There is a class solution with the further families on Q1 × S³ that induces the data on {0} × [0, v_1]
and [0, u_1] × {0}. Its metric, densities and phases are smooth, the axes included.

(b) *Estimate.* Its fields and densities differ from the background's, and its phases u_A from ů_A, by at most Cε in
C^(k−4), the phases on the neighbourhoods of the 𝒯_A^g.

(c) *Uniqueness.* Let Q1′ := [0, u_1′] × [0, v_1′] ⊂ Q1, u_1′, v_1′ > 0. A class solution with the further families on
Q1′ × S³ that induces the data on the edges of Q1′, and whose fields and densities differ from the background's, and
phases u_A from ů_A, by at most ε_2 in C^(k−4), equals the solution of (a) on Q1′ × S³, with its densities and, on the
𝒯_A^g, its phases.

(d) *Localisation.* If the cone data equal the background's and every further density vanishes on {0} × [0, v_K) and [0,
u_K) × {0}, u_K, v_K > 0, the solution equals the background, with zero further densities, at the points of Q1 × S³ with
u < u_K and v < v_K.

*Proof.* By [[lem:loc-axis-constraints]] (c) and [[lem:loc-t5-jets]] (a), with 2p = m_1, the data extend to N_o and N_i,
of size at most Cε in C^(m_0), equal to the given ones on the edges of Q1. [[lem:loc-t5-existence]], [[lem:loc-t5-past]]
and [[lem:loc-t5-constraints]] give a smooth solution of [[eq:class-system]] with N_f families on 𝒯 ⊃ Q1, in the gauge
D(g) = 0 relative to Ĝ, that induces the data, with the bounds of [[lem:loc-t5-existence]]. [[lem:loc-axis-gauge]],
whose proof uses the adapted families only, with 𝒯 and the 𝒰′ of [[lem:loc-t5-constraints]] in place of 𝔗(s*) and its
𝒰′, Q1 ⊂ {τ ≤ s* − ½} lying at positive distance from the slice of 𝒯 in {τ = s*}, gives the map Ψ onto a set containing
Q1 × S³, in whose coordinates the metric has the form [[eq:loc-double-null]] with fields smooth through the axes within
Cε of the background's in C^(k−4); the further phases and densities are carried by Ψ, the curves of −g⁻¹du_A from 𝒦_A′
being those of P_A, and Ψ is the identity with its differential on N, so they induce the data. This gives (a) and (b),
the densities being nonnegative on Q1 by [[lem:loc-t5-constraints]].

(c) Steps (1) and (2) of the proof of [[lem:loc-axis-unique]] apply to the metric and the adapted densities of the
second solution and give the extension g″ and the wave map Φ; the further families do not enter them. In step (3), put
also ũ_A := u′_A ∘ Φ⁻¹ and q̃_A := q′_A ∘ Φ⁻¹, u′_A and q′_A the further phases and densities of the second solution.
The state of g̃ with these families agrees with U, with all derivatives, on N ∩ Φ(Q1′): for the fields and the adapted
densities by step (3) there, and for the further families by [[lem:loc-t5-jets]] (b) on the crossing sets, Φ being the
identity with all derivatives on N, as U = Û on P. Apply [[lem:loc-t5-uniqueness]] with Ĝ′ := Ĝ, U_1 the state of g̃, R′
:= Φ(Q1′) = [0, u_1′] × [0, v_1′] × S³ in the coordinates (ũ, ṽ, ω̃), U_2 := U, and, for each further family, 𝒦_A″ :=
the union of the η-neighbourhood of 𝒦_A in N and of the caps within δ_2 of the axes of the A-sections through its points
within δ_2 of the axes, with η and δ_2 so small that this set lies in the interior of 𝒦_A′ and satisfies the conditions
there for U_1, for ε and ε_2 small, as these hold with a margin for the background. The phases of A of U_1 and of U are
defined on a neighbourhood of 𝒯_A, the union of the curves of P_1^A in R′ from 𝒦_A″, that of U_1 by the hypothesis on
𝒯_A^g and that of U by [[lem:loc-t5-constraints]], for ε and ε_2 small by continuous dependence on the field; and both
densities vanish off 𝒯_A, being carried by curves from 𝒦_A, which lie in 𝒯_A for ε and ε_2 small. So U = U_1 on R′, and
step (4) of the proof of [[lem:loc-axis-unique]] concludes, the further phases and densities being carried along.

(d) Let 0 < u′ < min(u_K, u_1) and 0 < v′ < min(v_K, v_1). All derivatives across N at the points of {0} × [0, v′] and
[0, u′] × {0} are the background's ([[lem:loc-axis-jets]] (b), [[lem:loc-t5-jets]] (b)), so Δ and the further Borel sums
vanish at the points with u < u_K and v < v_K, Δ being supported within 2δ_e of N, and Ĝ = g_e and Û = Ů there. The
further densities of U vanish on [0, u′] × [0, v′] × S³, the curves from 𝒦_A entering F at points with v ≥ v_K or u ≥
u_K and keeping that inequality. [[lem:loc-t5-uniqueness]], with U_1 := Ů in the coordinates (u, v, ω), which solves
[[eq:class-system]] in the gauge relative to g_e = Ĝ there, R′ := [0, u′] × [0, v′] × S³, U_2 := U and 𝒦_A″ := ∅, gives
U = Ů there, and Ψ is the identity there by the last statement of [[lem:loc-axis-gauge]]. ∎

For N_f = 2 there are no further families, and [[thm:loc-t5]] is [[thm:loc-axis]].

**Proposition {#prop:loc-t5-cut}** (Families tangent to an edge: developments away from the axes concerned.) Let the
data be as in [[thm:loc-t5]] except that, for the further families of a set 𝒢, (F-a) or (F-b) fails. Let N_c ⊂ N and
N_0 ⊂ N_c be compact and G-invariant, N_0 in the interior of N_c, such that: (N1) the interior of N_0 contains the
tangency sets of the families of 𝒢 at the axes near which they carry density, and the corner circles of those axes; (N2)
with a point of N_o (of N_i), N_c contains the points of larger v (of larger u) on its generator; (N3) every family of 𝒢
satisfies (F-a),
(F-b) and (F-c) with supp q_A ∖ int N_0 in place of 𝒦_A. Let λ be a smooth G-invariant function with dλ future timelike
for g_e near Q1 × S³, such that D′ := F ∩ {λ ≤ 0} lies in Q1 × S³, does not meet N_c, and has {λ = 0} ∩ F at a positive
distance w from the axes. For ε small, depending also on N_0, N_c and λ, with δ_c small depending on the distance from
D′ to N_c:

(a) for every smooth G-invariant χ_c on N, equal to 1 outside N_c and to 0 near N_0, the solution U of the system of
[[sec:loc-t5-system]] for the data with q_A replaced by χ_c q_A for A ∈ 𝒢, and the constraints solved again, is on D′ a
class solution with N_f families in the gauge D(g) = 0 relative to Ĝ that induces the given data on D′ ∩ N, and in the
coordinates Ψ of [[lem:loc-axis-gauge]] it has the form [[eq:loc-double-null]] on Ψ(D′);
(b) U and Ψ on D′ do not depend on χ_c.

*Proof.* (a) The constraints of [[lem:loc-t5-jets]] (a) change only on the generators through points where χ_c q_A ≠
q_A, and only at and beyond them, hence only in N_c, by (N2). The new data are of size at most Cε, satisfy (F-a)–(F-c)
by (N1) and (N3), and agree with the old ones on N ∖ N_c. Take 𝒦_A′ for A ∈ 𝒢 a neighbourhood of supp q_A ∖ int N_0, the
same for every χ_c, and ξ_A, ψ_A, t_A built from it, and take δ_♮ ≤ w/4. [[thm:loc-t5]] and its proof give U, a
class solution on 𝒯 ⊃ D′, and Ψ; D′ ∩ N ⊂ N ∖ N_c, where the data are the given ones. (b) The jets on N at a point
outside N_c depend only on the data on the generator up to that point ([[lem:loc-cone-jets]], [[lem:loc-t5-jets]] (b)),
which lies outside N_c by (N2), and the Borel sums at a point within 2δ_e of N hold jets at points of N within 2δ_e of
it; so for δ_c small Û and Ĝ are the same for two cut-offs χ_c on a neighbourhood 𝒱 of D′, and so is the system there,
the closures at points of 𝒱 using arcs within C δ_♮ of them. Let U and U′ be the two solutions and z their difference.
On P ∩ 𝒱 both equal Û ([[lem:loc-t5-past]]). On D′, z satisfies a system of the form of [[lem:loc-t5-energy]], with B_0
:= D′ ∩ N, where z = 0, and the face {λ = 0}, whose conormal dλ is future timelike for both metrics and positive on
their transport fields, so that the boundary matrix there is nonnegative. Points of D′ within δ_♮/2 of an axis lie at
distance at least w/2 from {λ = 0}, and their arcs, within δ_♮ of them, lie in {λ < 0}; near the edges the edge sections
are leaves; so the sets D′ ∩ {t_A = t} ∩ {τ ≤ s} contain the arcs of U′ of their points near the axes, and
[[lem:class-leaf-arc]] (c) bounds the non-local terms as in the proof of [[lem:loc-t5-constraints]]. So z = 0 on D′. A
past causal curve from a point of D′ decreases λ and stays in D′ until it meets D′ ∩ N; so the phases u_out, u_in and
the angle ω′ of [[lem:loc-axis-gauge]], fixed by their values on P ∩ 𝒰^♭ and transported along the curves of P_out, are
the same, and so is Ψ. ∎

**Remark {#rem:loc-t5-scope}** (What [[thm:loc-t5]] and [[prop:loc-t5-cut]] do not give.) (i) *Families tangent to an
edge at an axis.* A further family that carries density where it is tangent to an edge along an axis generator is
excluded by (F-b); [[prop:loc-t5-grazing]] shows that the construction of this section cannot treat it there in any
slicing, except possibly where the edge sections are leaves to infinite order only, and that where they are leaves the
edge is characteristic for the family on an open set. [[prop:loc-t5-cut]] develops such data on regions bounded by a
spacelike hypersurface that avoid those axes near the points concerned, and shows that the development there does not
depend on how the data are cut near those points; it gives no uniqueness among other solutions on D′. (ii) *The
condition (F-a).* It cannot be dropped for a family that crosses an edge near a corner circle, by the remark after
[[lem:loc-t5-tubes]], as long as the family is carried by cut-offs ξ_A. (iii) *Size.* As in [[rem:loc-axis-scope]] (i),
the data must be near the background's at the axes, the term in σ_A being estimated on balls about the background.
(iv) *Regularity.* The data are smooth and small in C^(m_1), and the development is smooth, with the estimate of
[[thm:loc-axis]] in C^(k−4); smoothness comes from the tame bound [[eq:class-leaf-tame]] through part (c) of
[[thm:class-kato-memory]].

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as lines of the chapter sources at
the current head, each preceded by a line ending "Old:" or "New:"; every old text occurs there exactly once, as whole
lines, and line numbers serve only to find the place.

*1. Block A1, [[ch:class-system]].* The text of Block A1 from the paragraph beginning "In the coordinates (z, y) of
[[lem:class-leaf]] near a point p of axis 2 on a slice" through the end of the proof of [[lem:class-leaf-tame]] (without
the heading "Block A1" and its first paragraph) is inserted in [[sec:class-planar-shear]] after
[[rem:class-leaf-numerics]], whose last line is "0.146 and 2.91. No proof uses these observations." (line 1367), after
any text another placement puts there (Tier 4's [[lem:class-leaf-reference]]), and before the heading "### Cauchy
stability with the dusts at the axes {#sec:class-axes-stability}" (line 1369), with one blank line before and after. It
defines lem:class-leaf-arc, eq:class-leaf-arc, lem:class-leaf-tame and eq:class-leaf-tame. The proof of
[[lem:class-leaf-tame]] is complete in itself and does not use the proof of [[lem:class-leaf-differences]].

*2. Block A2, [[ch:class-system]].* The text of Block A2 from its paragraph beginning "It solves
[[eq:class-kato-system]] when the forcing term" (without the sentence before those words and without the heading "Block
A2") through the end of [[rem:class-kato-memory]] is inserted in [[sec:class-kato]] after [[rem:class-kato-model]],
whose last line is "proof uses these observations." (line 875), and before the heading "### Cauchy stability off the
axes {#sec:class-off-axes}" (line 877), with one blank line before and after. It defines eq:class-trace,
lem:class-mixed-product, lem:class-kato-history, thm:class-kato-memory and rem:class-kato-memory.

*3. Block B, [[ch:localised-data]].* The section of Block B, from its heading "### Further dust families at the axes
{#sec:loc-t5}" through the end of [[rem:loc-t5-scope]] (without the line "### Block B. …" and its paragraph), is
inserted immediately after the last line of [[sec:loc-axis]], which ends [[rem:loc-axis-scope]] with the line "are only
bounded, or measures, are not covered ([[rem:loc-cone-scope]] (iii))." (line 3246), with one blank line before and one
after; if the Tier 4 section is merged, it goes before the heading "### Developments of data of any size through the
axes {#sec:civp-axes}", and otherwise before the heading "### Null shells along the leaves {#sec:loc-shells}" (line
3248). It rests on [[sec:loc-axis]] only and is cited by no other section except through items 4 and 5. Its heading is
of the level of [[sec:loc-axis]] and its five subsections of the level below. It defines sec:loc-t5,
sec:loc-t5-families, def:loc-t5-family, lem:loc-t5-dichotomy, lem:loc-t5-tubes, lem:loc-t5-jets, sec:loc-t5-times,
eq:loc-t5-times, lem:loc-t5-times, lem:loc-t5-faces, sec:loc-t5-system, lem:loc-t5-forcing, lem:loc-t5-residual,
lem:loc-t5-existence, sec:loc-t5-dependence, lem:loc-t5-energy, lem:loc-t5-past, lem:loc-t5-constraints,
sec:loc-t5-theorem, prop:loc-t5-grazing, lem:loc-t5-uniqueness, thm:loc-t5, prop:loc-t5-cut and rem:loc-t5-scope, none
of which is defined elsewhere. The notion of class solution it uses with further families is defined in
[[thm:loc-t5]] from that of [[def:loc-axis-data]]; the broader notion of Tier 4 is not needed.

*4. [[ch:localised-data]], the paragraph after [[prop:loc-cones]], line 728.* Only this line is replaced, so that the
item composes with placements that rewrite the sentence beginning "No development is" on the lines after it. Old:

([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. No development is

New:

([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. Near the background's,
further null dusts, of phases that are not functions of u or of v, may be added to the cone data through the axes, any
number of them, when at the points where a cone meets an axis each carries density only where it crosses that cone and
none near the circles in which the corner sphere meets the axes; the development on the whole rectangle is then smooth,
with an estimate, and unique in the gauge among nearby solutions ([[thm:loc-t5]]). A family that carries density
where it is tangent to a cone along an axis generator is not treated, the construction failing there
([[prop:loc-t5-grazing]]); such data are developed on regions that avoid that axis near those points
([[prop:loc-t5-cut]]). No development is

*5. [[ch:localised-data]], [[rem:loc-axis-scope]] (ii), lines 3244–3245.* The remark records that further families are
not treated in [[sec:loc-axis]]; a pointer to [[sec:loc-t5]] is added. Old:

while ζ_A must vanish near the points where the cones meet the axes. Neither case is treated here, nor are further
families whose densities avoid the axes. (iii) *Regularity.* The data are smooth and small in C^(m_1); densities that

New:

while ζ_A must vanish near the points where the cones meet the axes. Neither case is treated here, nor are further
families whose densities avoid the axes; [[sec:loc-t5]] treats them, with a closure time for each further family and
an evolution time bent near the axes, when each carries density only where it crosses a cone and none near the circles
in which the corner sphere meets the axes ([[thm:loc-t5]]), and shows that this construction cannot treat a family
with density where it is tangent to a cone at an axis ([[prop:loc-t5-grazing]]). (iii) *Regularity.* The data are smooth
and small in C^(m_1); densities that

*6. [[ch:class-system]], [[rem:class-scope]], its last two lines (lines 1674–1675).* Old:

polarisation of the waves for a non-radial family, and the limits that carry massless Vlasov matter are taken up in
[[ch:vlasov]].

New:

polarisation of the waves for a non-radial family, and the limits that carry massless Vlasov matter are taken up in
[[ch:vlasov]]. For the characteristic problem the same alternative at an axis, a gradient that is a multiple of dv
or of du, decides whether a further family crosses a cone along its axis generator or is tangent to it
([[lem:loc-t5-dichotomy]]).

*7. Unchanged.* [[ch:theorems]], the opening of [[ch:localised-data]] and [[ch:scope]] speak of the characteristic
problem with the two adapted families only, and stay true; the sentence of [[ch:scope]] on further families with
densities vanishing near the axes (line 183) concerns the Cauchy problem of [[thm:class-stability]] and is unchanged. No
statement of this file depends on the null-shells section or on the Tier 4 section.

*8. Appendix A and the references.* No new entry. The proofs use [[thm:std-sy-extension]], [[thm:std-gn-moser]],
[[cor:std-moser-product]], [[thm:std-bh-embedding]] and [[thm:std-bh17-embedding]], already stated in
[[app:standard-results]], and the interpolation inequality established in the proof of [[lem:class-composition]] (a).

### Crosswalk rows

New rows, one per label, in chapter order, each a line of four tab-separated fields (label, source,
source_name, note).

For crosswalk/81-class-system.tsv, after the row of rem:class-kato-model:

eq:class-trace	paper/reader/proofs/P-CIVP5.md:208	proof P-CIVP5, display	trace of a space-time Sobolev function on the slices; the extension E_b beyond b
lem:class-mixed-product	paper/reader/proofs/P-CIVP5.md:220	proof P-CIVP5, Lemma (Products at one time)	products at one time; time derivatives of compositions
lem:class-kato-history	paper/reader/proofs/P-CIVP5.md:244	proof P-CIVP5, Lemma (The linear problem with forcing in a space-time space and a history)	linear step with forcing in a space-time space and a history matched at t1
thm:class-kato-memory	paper/reader/proofs/P-CIVP5.md:294	proof P-CIVP5, Theorem (Kato's iteration with memory)	Kato iteration with memory: integrated hypotheses (M0)-(M2), stability with (M1′), regularity (c) with the tame hypotheses (M1_σ) by a global iteration
rem:class-kato-memory	paper/reader/proofs/P-CIVP5.md:404	proof P-CIVP5, Remark (Why the hypotheses are integrated)	why the hypotheses are integrated; no proof uses it

For crosswalk/81-class-system.tsv, after the row of rem:class-leaf-numerics (and after the rows of Tier 4 placed there):

lem:class-leaf-arc	paper/reader/proofs/P-CIVP5.md:21	proof P-CIVP5, Lemma (Two states compared along one arc)	two states compared along one arc, one-sided, on arc-closed sets, by the Volterra form and the Hardy average; no smallness of the difference
eq:class-leaf-arc	paper/reader/proofs/P-CIVP5.md:30	proof P-CIVP5, display	pointwise one-sided bound
lem:class-leaf-tame	paper/reader/proofs/P-CIVP5.md:85	proof P-CIVP5, Lemma (Tame bounds for the planar shear in space-time)	tame space-time bound of the planar shear in every H^n on C^5-small balls, by the divergence form of the leaf equation, a fixed point along arcs and a composition estimate; complete proof, independent of the proof of lem:class-leaf-differences
eq:class-leaf-tame	paper/reader/proofs/P-CIVP5.md:95	proof P-CIVP5, display	the tame bound

For crosswalk/83-localised-data.tsv, after the row of rem:loc-axis-scope:

sec:loc-t5	paper/reader/proofs/P-CIVP5.md:419	proof P-CIVP5, section heading	Tier 5: further dust families at the axes, closure times per family and a bent evolution time
sec:loc-t5-families	paper/reader/proofs/P-CIVP5.md:454	proof P-CIVP5, section heading	families and their type at an axis
def:loc-t5-family	paper/reader/proofs/P-CIVP5.md:456	proof P-CIVP5, Definition (Further families)	further families; (F-a) corner circles, (F-b) density only where crossing, (F-c) corner compatibility
lem:loc-t5-dichotomy	paper/reader/proofs/P-CIVP5.md:473	proof P-CIVP5, Lemma (Crossing and tangency at the axes)	at an axis a further family crosses one edge and is tangent to the other
lem:loc-t5-tubes	paper/reader/proofs/P-CIVP5.md:493	proof P-CIVP5, Lemma (The tubes avoid the tangency sets)	tubes from crossing sets avoid the tangency sets, by continuous dependence
lem:loc-t5-jets	paper/reader/proofs/P-CIVP5.md:529	proof P-CIVP5, Lemma (Cone data and jets with further families)	constraints with further sources through lem:loc-axis-constraints; extension of the further data; transverse jets on the crossing sets
sec:loc-t5-times	paper/reader/proofs/P-CIVP5.md:575	proof P-CIVP5, section heading	closure times
eq:loc-t5-times	paper/reader/proofs/P-CIVP5.md:592	proof P-CIVP5, display	t_A := τ0 − χ_* ψ_A Ĝ_A ρ², τ := τ0 + K χ_* ρ²
lem:loc-t5-times	paper/reader/proofs/P-CIVP5.md:596	proof P-CIVP5, Lemma (The closure times and the evolution time)	time functions, edge sections constant, τ increasing along arcs, memory m_*
lem:loc-t5-faces	paper/reader/proofs/P-CIVP5.md:626	proof P-CIVP5, Lemma (The edge sections are leaves of each family)	edge sections are leaves of each family, by lem:loc-axis-leaf (ii), (iii)
sec:loc-t5-system	paper/reader/proofs/P-CIVP5.md:645	proof P-CIVP5, section heading	closure radius, region 𝒰^♭ and the system with memory
lem:loc-t5-forcing	paper/reader/proofs/P-CIVP5.md:685	proof P-CIVP5, Lemma (The forcing term)	hypotheses (M0)-(M2), (M1′), (M1_σ) of thm:class-kato-memory via lem:class-leaf-tame and lem:class-leaf-arc in the charts (t_A, y)
lem:loc-t5-residual	paper/reader/proofs/P-CIVP5.md:713	proof P-CIVP5, Lemma (The residual)	F̃ smooth across N; residual small in H^k and zero near τ_init
lem:loc-t5-existence	paper/reader/proofs/P-CIVP5.md:744	proof P-CIVP5, Lemma (Existence and smoothness)	existence and smoothness by thm:class-kato-memory (b), (c)
sec:loc-t5-dependence	paper/reader/proofs/P-CIVP5.md:762	proof P-CIVP5, section heading	dependence on the past and the constraints
lem:loc-t5-energy	paper/reader/proofs/P-CIVP5.md:764	proof P-CIVP5, Lemma (Energy with an integrated non-local term)	energy with an integrated non-local term
lem:loc-t5-past	paper/reader/proofs/P-CIVP5.md:773	proof P-CIVP5, Lemma (The past of the edges)	U = Û on P by arc-closed slices of P
lem:loc-t5-constraints	paper/reader/proofs/P-CIVP5.md:794	proof P-CIVP5, Lemma (The constraints)	constraint propagation on F ∩ {τ ≤ s*} and on the tubes from 𝒦_A″
sec:loc-t5-theorem	paper/reader/proofs/P-CIVP5.md:846	proof P-CIVP5, section heading	grazing obstruction, uniqueness, theorem, statement W
prop:loc-t5-grazing	paper/reader/proofs/P-CIVP5.md:848	proof P-CIVP5, Proposition (Families tangent to an edge at an axis)	why the construction cannot treat families with density where tangent to an edge at an axis: characteristic edge, sections not leaves, arcs crossing the edge
lem:loc-t5-uniqueness	paper/reader/proofs/P-CIVP5.md:908	proof P-CIVP5, Lemma (Dependence on the past faces with further families)	dependence on the past faces with further families, by triangles T_N and continuity in τ^N; no smallness
thm:loc-t5	paper/reader/proofs/P-CIVP5.md:972	proof P-CIVP5, Theorem (Development with further families at the axes)	development with any number of crossing families: smooth, C^(k−4) estimate, uniqueness, localisation; grazing families excluded with the reason
prop:loc-t5-cut	paper/reader/proofs/P-CIVP5.md:1040	proof P-CIVP5, Proposition (Families tangent to an edge: developments away from the axes concerned)	statement W: development on F ∩ {λ ≤ 0} away from the axes concerned, independent of the cut
rem:loc-t5-scope	paper/reader/proofs/P-CIVP5.md:1076	proof P-CIVP5, Remark (What thm:loc-t5 and prop:loc-t5-cut do not give)	what is not given: grazing families on the axis, (F-a), size; regularity as Tier 3
