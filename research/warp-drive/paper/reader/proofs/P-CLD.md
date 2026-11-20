### Block. The leaves of a state, and the planar shear of nearby states

The text of this block replaces [[lem:class-leaf-differences]], its statement and its proof, in
[[sec:class-planar-shear]] of [[ch:class-system]]; the Placement section gives the position. It consists of a paragraph
of definitions, [[lem:class-leaf-states]] with its proof, and [[lem:class-leaf-differences]] with its proof.

Let Σ be a slice {τ = const} of a chart (τ, x) on a G-invariant open set in which G acts on x ∈ ℝ⁴ by its action on ℝ⁴
and Σ is spacelike for the metrics considered. The chart of [[sec:background]] is one, and the constructions of this
section use of it only these properties, through the future unit normal n and the second fundamental form K_Σ of Σ, the
totally geodesic M3 := Σ ∩ {φ1 = 0} and the coordinates (z, y) of [[lem:class-leaf]]. Fix a point p of axis 2 with
ρ1(p) > 0 and a family A, write r := |y|, z(p) for the value of z at p and 𝒰 := 𝒰_(ρ1(p)/4), so that 𝒰_δ ∩ M3 =
{|z − z(p)| < δ, |y| < δ} for δ ≤ ρ1(p)/4.

A *state* is a G-invariant U = (g, p_A, Θ_A, q_A) on 𝒰 with g a Lorentzian metric of class C² for which Σ is spacelike,
p_A a covector field and Θ_A a function of class C¹, and p_A(∂_z) ≠ 0 on the axis. We write W_U := (g, ∂g, p_A, Θ_A),
∂g all first derivatives of the components of g in the chart, and |U − U′| at a point for the sum of the absolute
values of the components of W_U − W_(U′) there, so that U − U′ includes the difference of the first derivatives of the
metrics. A state has *bounds* (M, c), M ≥ 1 and c > 0, if on 𝒰 the C² norms of the components of g and the C¹ norms of
those of p_A and Θ_A are at most M, g(X, X) ≥ |X|²/M for X tangent to Σ, |X| its flat length, −g⁻¹(dτ, dτ) ≥ 1/M,
and |p_A(∂_z)| ≥ c on the axis. Let p_A^Σ be the spatial part of p_A, tangent to M3 at its points by invariance, ε the
sign of p_A(∂_z), and, where p_A^Σ ≠ 0,

    H_L[U] := ε (Θ_A − κ_A1 + p_A(n) tr K_Σ|_Π)/|p_A^Σ|,      Π the γ3-orthogonal complement of p_A^Σ in TM3:

the formula of step (1) of the proof of [[lem:class-planar-shear]] with Θ_A, p_A^Σ and p_A(n) in place of Θ, ∇_Σ u and
n(u), and with the plane Π, which p_A fixes at each point, in place of TΣ_L. So H_L[U] is a function of the point, as
[[lem:class-volterra]] requires; when p_A is the differential of a phase, Π is the tangent plane of the level set of the
phase in M3 through the point, and H_L[U] is that formula for the level set. The *leaves* of U are the solutions
h(·; z0) of [[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, read as the graphs z = h(|y|; z0).
For a point x on a leaf, σ[U](x) := ε |p_A^Σ| (k_r − k_φ) − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e2, e2)) at x, with k_r and k_φ
the principal curvatures of the leaf in M3 for the normal ν of [[lem:class-leaf]] (b), e_r its unit tangent in the
meridional plane and e2 := K2/|K2|: this is [[eq:class-shear-leaf]] with p_A in place of du, the normal ν_L there being
εν. The *arc* of U through x is {(h(t; z0), t y(x)/r_x) : 0 ≤ t ≤ r_x}, with r_x := |y(x)| and z0 the axis point of
the leaf through x. Near axis 1 the same holds with the two planes exchanged and κ_A2 in place of κ_A1.

**Lemma {#lem:class-leaf-states}** (The leaves of a state.) Let M ≥ 1 and c > 0. There are r_1 ∈ (0, ρ1(p)/32] and C,
depending only on M, c and ρ1(p), such that for all states U and U′ with bounds (M, c):

(a) (Foliation.) For |z0 − z(p)| ≤ r_1 the leaf h(·; z0) of U is defined on [0, r_1], with |h′(r; z0)| ≤ C r, and for
two such axis points z0 ≠ z0′ and 0 ≤ r ≤ r_1

    1/2 ≤ (h(r; z0) − h(r; z0′))/(z0 − z0′) ≤ 3/2,      |h′(r; z0) − h′(r; z0′)| ≤ C r |z0 − z0′|.       {#eq:class-leaf-quotient}

Every point x of 𝒰_(r_1/2) lies on exactly one of these leaves; we write z0[U](x) for its axis point. The arc of U
through a point of 𝒰_δ, δ ≤ r_1/2, lies in 𝒰_(2δ), and |σ[U]| ≤ C on 𝒰_(r_1/2). If U is smooth, the map (z0, y) ↦
h(|y|; z0) and the function z0[U] are smooth, and they depend smoothly on parameters on which U depends smoothly.

(b) (Along one arc.) For x ∈ 𝒰_(r_1/2), with r_x := |y(x)| and f(t) := |U − U′| at the point of the arc of U through x
at radius t,

    |σ[U](x) − σ[U′](x)| ≤ C (f(r_x) + r_x⁻² ∫_0^(r_x) t f(t) dt + (∫_0^(r_x) t f(t)² dt)^(1/2)).       {#eq:class-leaf-pointwise}

(c) (On sets closed under arcs.) Let 0 < δ ≤ r_1/2, and let D ⊂ Σ be a measurable G-invariant set such that the arc of
U through every point of D ∩ 𝒰_δ lies in D. Then

    ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D∩𝒰_(2δ))).                                          {#eq:class-leaf-sets}

Only the values of U − U′ on the arcs of U enter (b) and (c), and C depends neither on D nor on δ.

*Proof.* Constants C, C_0, C_1, … depend only on M, c and ρ1(p).

*Step 1 (H_L).* At a point of the axis every rotation of y fixes the point, so the invariant covector p_A^Σ has no
component along dy there, p_A^Σ = p_A(∂_z) dz, and γ3 has no component along dz dy (as in the proof of
[[lem:class-leaf]] (a)); so |p_A^Σ| = |p_A(∂_z)| A3^(−1/2) ≥ c M^(−1/2), as A3 ≤ M. The function |p_A^Σ|² has Lipschitz
constant at most C, so there is r_2 ∈ (0, ρ1(p)/16] with |p_A^Σ| ≥ c M^(−1/2)/2 on 𝒰_(4r_2), where p_A(∂_z) then has
the constant sign ε. There H_L[U](x) = ℋ(x, W_U(x)), with ℋ a smooth function, the same for all states, on the set of
(x, w) with ρ1 ≥ ρ1(p)/2 at which the components of w satisfy the lower bounds g(X, X) ≥ |X|²/(2M),
−g⁻¹(dτ, dτ) ≥ 1/(2M) and |p_A^Σ| ≥ c M^(−1/2)/4: n, K_Σ and γ3 are smooth functions of the metric and its first
derivatives, κ_A1 = g⁻¹(p_A, dψ1) with ψ1 = ½ log g(K1, K1) and g(K1, K1) ≥ ρ1²/M, and Π and the trace of K_Σ over it
are smooth functions of γ3, K_Σ and p_A^Σ ≠ 0. As W_U is of class C¹ with C¹ norm at most C, so is H_L[U] on 𝒰_(4r_2).

*Step 2 (The function G).* At the point (z, (r, 0)) write γ_zz := γ3(∂_z, ∂_z) = A3, γ_z1 := γ3(∂_z, ∂_(y1)) = C3 r,
γ_11 := γ3(∂_(y1), ∂_(y1)) = B3 + D3 r² and γ_22 := γ3(∂_(y2), ∂_(y2)) = B3. By invariance γ3(∂_z, ∂_(y_i)) = C3 y_i
near the axis, a vector field on the y-plane invariant under its rotations and reflections being a multiple of y by a
function of |y|; so C3 = ∂_(y2) γ3(∂_z, ∂_(y2)) at (z, (r, 0)), a component of the first derivatives of g there. With
h := z and h′ := q, det₂ = γ_zz γ_11 − γ_z1² ≥ M⁻² and N_L² = γ3(∂_(y1) + q ∂_z, ∂_(y1) + q ∂_z) ≥ (1 + q²)/M. By the
proof of [[lem:class-volterra]], E_L = ν^r/a_L − q + r B̃/a_L, with ν^r/a_L = (γ_z1 + γ_zz q) N_L²/det₂ and B̃ the part
of H_L free of h″ and of ν^r/r in the divergence formula of the proof of [[lem:class-leaf]] (c); in that formula
(det γ3)^(1/2) = r (γ_22 det₂)^(1/2), ν^z = (γ_11 + γ_z1 q)/(det₂^(1/2) N_L) and ν^r = −(γ_z1 + γ_zz q)/(det₂^(1/2) N_L),
so B̃ is a smooth function of q and of the components of γ3 and their first derivatives at the point. As det₂ − γ_zz N_L²
= −(γ_z1 + γ_zz q)², the function G(r, z, q) := r H(z, r)/a_L − E_L of that proof, H(z, r) := H_L[U] at (z, (r, 0)), is

    G(r, z, q) = r (H/a_L − C3 N_L²/det₂ − B̃/a_L) − q (C3 r + γ_zz q)²/det₂.                             {#eq:class-leaf-g}

On R := {0 ≤ r ≤ r_2, |z − z(p)| ≤ r_2, |q| ≤ 1} the first bracket and its first derivatives in z and in q are bounded
by C, by Step 1 and the C² bounds of g, and ∂_z(C3 r + γ_zz q) = r ∂_z C3 + q ∂_z γ_zz. So G(0, z, q) = −γ_zz q³/γ_22,
and on R

    |G(r, z, 0)| ≤ C_0 r,      |∂_z G| ≤ C_1 (r + |q|),      |∂_q G| ≤ C_2 (r + |q|).                     {#eq:class-leaf-g-bounds}

Every factor of [[eq:class-leaf-g]] is a smooth function of r, q and the values of W_U at the point, with ℋ in place of
H; so for a second state U′ with bounds (M, c) and the same (r, z, q) ∈ R, |G_U − G_(U′)| ≤ C (r + |q|) |U − U′| at
(z, (r, 0)), G_U and G_(U′) the functions [[eq:class-leaf-g]] of the two states.

*Step 3 (One leaf).* Put δ_p := min(1, 1/(8C_2)) and r_0 := min(r_2/2, δ_p/C_0, 1/(8C_2), 1/(4C_1), (r_2/C_0)^(1/2)).
For |z0 − z(p)| ≤ r_2/2 consider the map 𝒯 of the proof of [[lem:class-volterra]] on {p ∈ C([0, r_0]) : sup |p| ≤
δ_p}, which uses of G only G(0, z, q) = −γ_zz q³/γ_22 and bounds of the form [[eq:class-leaf-g-bounds]], here with
|∂_z G| ≤ 2C_1 on R. As there, |𝒯p(r)| ≤ C_0 r/2 + C_2 (r_0 + δ_p) δ_p ≤ δ_p and 𝒯 has Lipschitz constant at most
C_1 r_0 + C_2 (r_0 + δ_p) ≤ 1/2; its fixed point is the leaf on [0, r_0], with |h′(r)| ≤ C_0 r ≤ 1 and |h(r) − z0| ≤
C_0 r²/2 ≤ r_2/2, so that it stays in R, and that proof gives its uniqueness among the C¹ solutions with h(0) = z0.

*Step 4 (Two axis points).* For |z_i − z(p)| ≤ r_2/2, i = 1, 2, let h_i be the leaves, w_i := h_i′, Δz := z_1 − z_2
and D(r) := sup_[0,r] |w_1 − w_2|. Along both leaves, and on the segment between their values, |q| ≤ C_0 ρ, so by
[[eq:class-leaf-g-bounds]] the values of G at (ρ, h_1, w_1) and at (ρ, h_2, w_2) differ by at most C_4 ρ (|h_1 − h_2| +
|w_1 − w_2|), C_4 := (C_1 + C_2)(1 + C_0); and |h_1 − h_2|(ρ) ≤ |Δz| + ρ D(ρ). Subtracting the two Volterra equations,
r |w_1 − w_2|(r) ≤ C_4 r² (|Δz| + 2D(r))/2 for r ≤ r_0, so D(r) ≤ C_4 r |Δz|/2 + C_4 r D(r), and for C_4 r ≤ 1/2

    |h_1′(r) − h_2′(r)| ≤ C_4 r |Δz|,      |h_1(r) − h_2(r) − Δz| ≤ C_4 r² |Δz|/2.

*Step 5 (Foliation).* Put r_1 := min(r_0, 1/(2C_4), 1/(2C_0)), so that r_1 ≤ ρ1(p)/32 and C_4 r_1² ≤ 1. For
|z0 − z(p)| ≤ r_1 the leaf is defined on [0, r_1] with |h′| ≤ C_0 r, and Step 4 gives [[eq:class-leaf-quotient]] with
C := C_4. For |y| = r ≤ r_1 the map z0 ↦ h(r; z0) on [z(p) − r_1, z(p) + r_1] is continuous and strictly increasing,
and |h(r; z0) − z0| ≤ C_0 r²/2 ≤ r_1/4; so its image contains [z(p) − 3r_1/4, z(p) + 3r_1/4], and every point x of
𝒰_(r_1/2) lies on exactly one leaf, with |z0[U](x) − z(p)| ≤ 3r_1/4. For t ≤ r_x the point of the arc of x at radius
t has |h(t; z0) − z(x)| ≤ C_0 (r_x² − t²)/2 ≤ r_x/4, so the arc of a point of 𝒰_δ lies in 𝒰_(5δ/4) ⊂ 𝒰_(2δ).

*Step 6 (The shear on a leaf).* Let x̄ = (h(r), (r, 0)), r > 0, be a point of a leaf of U and s := h′(r)/r. The graph
has mean curvature H_L[U] at x̄: by the definition of E_L in [[lem:class-leaf]] (c), (r h′)′ = r H_L[U]/a_L − E_L says
exactly that. So k_r = H_L[U] − k_φ, with k_φ = ν^r/r + ½ ν(log γ_22) and ν^r/r = −(C3 + γ_zz s)/(det₂^(1/2) N_L) by
[[lem:class-leaf]] (c), e_r = (∂_(y1) + q ∂_z)/N_L with q = r s, and e2 = ∂_(y2)/γ_22^(1/2). Hence

    σ[U](x̄) = 𝔖(x̄, W_U(x̄), s),                                                                          {#eq:class-leaf-shear-s}

with 𝔖 a smooth function, the same for all states, on the set of Step 1 times {|s| ≤ C_0}: every quantity entering is a
smooth function of s, of the point and of the components of W there, C3 by Step 2. Since r⁻² ∫_0^r G dρ = h′(r)/r and
G(ρ, h, h′)/ρ is continuous by [[eq:class-leaf-g]], s has a limit at r = 0, |s| ≤ C_0, and [[eq:class-leaf-shear-s]]
holds there by continuity. So |σ[U]| ≤ C on 𝒰_(r_1/2); |∂_s 𝔖| ≤ C; along each line {y = const} the function
x̄ ↦ 𝔖(x̄, W_U(x̄), s) is Lipschitz with constant C, W_U being of class C¹; and |𝔖(x̄, W_U(x̄), s) − 𝔖(x̄, W_(U′)(x̄),
s)| ≤ C |U − U′|(x̄).

*Step 7 (Smoothness).* Let U be smooth. The components at (z, (r, 0)), r ∈ (−r_2, r_2), are smooth in (z, r), and
G(−r, z, −q) = −G(r, z, q), by the parities of [[lem:class-leaf]] (c). So 𝔤(r, z, s) := G(r, z, r s)/r, which by
[[eq:class-leaf-g]] is the first bracket there at q = r s minus r² s (C3 + γ_zz s)²/det₂, is smooth and even in r. With
h′ = r s the leaf equation reads, on [−r_1, r_1], the leaf being even,

    s(r) = ∫_0^1 t 𝔤(r t, h(r t), s(r t)) dt,      h(r) = z0 + ∫_0^r ρ s(ρ) dρ.                                {#eq:class-leaf-s}

Its right side defines a map 𝒦 of {s ∈ C([−r_1, r_1]) : sup |s| ≤ C_0} into itself, smooth in s, in z0 and in the
parameters on which U depends smoothly, and a contraction with constant at most 1/2, since |∂_s 𝔤| = |∂_q G| ≤
C_2 (1 + C_0) |r|, |∂_z 𝔤| ≤ C_1 (1 + C_0) and the values of h for two functions s differ by at most r² sup |Δs|/2.
Differentiating [[eq:class-leaf-s]] j times in r, the j-th derivative of 𝒦s is ∫_0^1 t^(1+j) (∂_s 𝔤 · s^(j) +
R_j)(r t) dt, with R_j a polynomial in the derivatives of s of order below j and in derivatives of 𝔤 and of h; so 𝒦 maps
{Σ_(i≤j) sup |s^(i)| ≤ K_j} into itself for K_j large, its iterates are bounded there and converge uniformly to s, and
s ∈ C^(j−1) for every j, by the theorem of Arzelà and Ascoli. The implicit function theorem in C([−r_1, r_1]) makes s
smooth in z0 and in the parameters; its derivatives in them solve linear equations of the form [[eq:class-leaf-s]], and
the same argument makes them smooth in r. s is even, s(−·) solving the same equation. So the graph z0 + |y|² ∫_0^1 θ
s(θ |y|) dθ is smooth in y: by Taylor's formula s(r) = Σ_(i<N) a_i r^(2i) + r^(2N) R_N(r) with R_N smooth and even,
and y ↦ |y|^(2N) R_N(|y|) is of class C^N. By [[eq:class-leaf-quotient]], ∂_(z0) h ∈ [1/2, 3/2], and the implicit
function theorem makes z0[U] smooth.

(a) is Steps 3–7.

(b) Let x ∈ 𝒰_(r_1/2); by invariance we may take x = (h_U(r; z0), (r, 0)) with r := r_x and z0 := z0[U](x). Let ĥ :=
h_U(·; z0) and h̃ := h_(U′)(·; z0), the leaf of U′ from the same axis point, δh := ĥ − h̃, δq := ĥ′ − h̃′, D(r) :=
sup_[0,r] |δq|, ŝ := ĥ′(r)/r, s̃ := h̃′(r)/r and x′ := (h̃(r), (r, 0)). By Step 6,

    σ[U](x) − σ[U′](x) = (𝔖(x, W_U, ŝ) − 𝔖(x, W_(U′), ŝ)) + (𝔖(x, W_(U′), ŝ) − 𝔖(x, W_(U′), s̃))
                        + (𝔖(x, W_(U′), s̃) − 𝔖(x′, W_(U′), s̃)) + (σ[U′](x′) − σ[U′](x)),

each W at the point written first, and the first three terms are at most C f(r), C |δq(r)|/r and C |δh(r)|. The point
x lies on the leaf of U′ with axis point ζ := z0[U′](x), and |ζ − z0| ≤ 2 |δh(r)| by [[eq:class-leaf-quotient]] for U′;
along the line {y = (r, 0)} the function ζ′ ↦ σ[U′](h_(U′)(r; ζ′), (r, 0)) = 𝔖(·, W_(U′), h_(U′)′(r; ζ′)/r) is Lipschitz
with constant C, by Step 6 and [[eq:class-leaf-quotient]]; so the fourth term is at most C |δh(r)|. Subtracting the
Volterra equations of the two leaves,

    r δq(r) = ∫_0^r ((G_U − G_(U′))(ρ, ĥ, ĥ′) + G_(U′)(ρ, ĥ, ĥ′) − G_(U′)(ρ, h̃, h̃′)) dρ.

By Step 2 the first difference is at most C ρ f(ρ), as |ĥ′| ≤ C_0 ρ, and as in Step 4 the second is at most
C_4 ρ (|δh| + |δq|), with |δh(ρ)| ≤ ρ D(ρ) since δh(0) = 0. So |δq(r)| ≤ C_4 r D(r) + C r⁻¹ ∫_0^r ρ f(ρ) dρ; with
r⁻¹ ∫_0^r ρ f dρ ≤ (∫_0^r ρ f² dρ)^(1/2)/√2, by the Cauchy–Schwarz inequality, and C_4 r ≤ 1/2,

    D(r) ≤ C (∫_0^r t f(t)² dt)^(1/2),      |δh(r)| ≤ r D(r),      |δq(r)|/r ≤ C_4 D(r) + C r⁻² ∫_0^r t f(t) dt,

which with r ≤ 1 give [[eq:class-leaf-pointwise]].

(c) For a G-invariant function F ≥ 0 on 𝒰_ρ, ρ ≤ ρ1(p)/4, ∫_(Σ∩𝒰_ρ) F = 2π ∫ F(z, y) z dz dy over 𝒰_ρ ∩ M3, the
flat measure of ℝ⁴ being ρ1 dρ1 dφ1 dy, with z = ρ1 ∈ [3ρ1(p)/4, 5ρ1(p)/4]. For fixed y the map z0 ↦ h_U(|y|; z0) is
increasing with difference quotients in [1/2, 3/2], hence absolutely continuous with derivative in [1/2, 3/2] almost
everywhere, and ∫ F(z, y) dz = ∫ F(h_U(|y|; z0), y) ∂_(z0) h_U dz0. For |z0 − z(p)| ≤ 3r_1/4 let Y(z0) be the set of
y with (h_U(|y|; z0), y) ∈ D ∩ 𝒰_δ, R(z0) the supremum of |y| over Y(z0) (0 if Y(z0) is empty), and f_(z0)(t) :=
|U − U′| at (h_U(t; z0), (t, 0)). If y ∈ Y(z0), the arc of U through that point lies in D, by hypothesis, and in 𝒰_(2δ),
by (a); by G-invariance, every point (h_U(|y′|; z0), y′) with |y′| < R(z0) lies in D ∩ 𝒰_(2δ). The arc of U through
(h_U(|y|; z0), y) is that leaf over [0, |y|], so [[eq:class-leaf-pointwise]] gives

    ∫_(Y(z0)) |σ[U] − σ[U′]|²(h_U(|y|; z0), y) dy ≤ C ∫_(𝔻_(R(z0))) (f_(z0)² + (𝒜f_(z0))² + ∫_0^(|y|) t f_(z0)(t)² dt) dy,

with f_(z0) and 𝒜f(r) := r⁻² ∫_0^r t f dt = ∫_0^1 s f(s r) ds read at |y|. As ‖f(s ·)‖_(L²(𝔻_R)) ≤ s⁻¹ ‖f‖_(L²(𝔻_R))
for radial f, Minkowski's inequality gives ‖𝒜f‖_(L²(𝔻_R)) ≤ ‖f‖_(L²(𝔻_R)), as in [[prop:class-flat-model]] (b), and the
last term is at most (R²/2) ‖f‖²_(L²(𝔻_R)) ≤ ‖f‖²_(L²(𝔻_R)). So the right side is at most C ∫_(𝔻_(R(z0))) f_(z0)(|y|)²
dy, an integral over points of D ∩ 𝒰_(2δ). Every point of D ∩ 𝒰_δ is (h_U(|y|; z0), y) with y ∈ Y(z0) and
|z0 − z(p)| ≤ δ + C_0 δ²/2 ≤ 3r_1/4. Integrating over z0 and changing variables on both sides, with the Jacobian
∂_(z0) h_U ∈ [1/2, 3/2] and the weights 2π z, gives [[eq:class-leaf-sets]]. ∎
