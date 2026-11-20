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

    ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D∩𝒰_(2δ))).                                         {#eq:class-leaf-sets}

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

    G(r, z, q) = r (H/a_L − C3 N_L²/det₂ − B̃/a_L) − q (C3 r + γ_zz q)²/det₂.                          {#eq:class-leaf-g}

On R := {0 ≤ r ≤ r_2, |z − z(p)| ≤ r_2, |q| ≤ 1} the first bracket and its first derivatives in z and in q are bounded
by C, by Step 1 and the C² bounds of g, and ∂_z(C3 r + γ_zz q) = r ∂_z C3 + q ∂_z γ_zz. So G(0, z, q) = −γ_zz q³/γ_22,
and on R

    |G(r, z, 0)| ≤ C_0 r,      |∂_z G| ≤ C_1 (r + |q|),      |∂_q G| ≤ C_2 (r + |q|).           {#eq:class-leaf-g-bounds}

Every factor of [[eq:class-leaf-g]] is a smooth function of r, q and the values of W_U at the point, with ℋ in place of
H; so for a second state U′ with bounds (M, c) and the same (r, z, q) ∈ R, |G_U − G_(U′)| ≤ C (r + |q|) |U − U′| at
(z, (r, 0)), G_U and G_(U′) the functions [[eq:class-leaf-g]] of the two states.

*Step 3 (One leaf).* Put δ_p := min(1, 1/(8C_2)) and r_0 := min(1, r_2/2, δ_p/C_0, 1/(8C_2), 1/(4C_1),
(r_2/C_0)^(1/2)).
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

    σ[U](x̄) = 𝔖(x̄, W_U(x̄), s),                                                                {#eq:class-leaf-shear-s}

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

    s(r) = ∫_0^1 t 𝔤(r t, h(r t), s(r t)) dt,      h(r) = z0 + ∫_0^r ρ s(ρ) dρ.                        {#eq:class-leaf-s}

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

**Lemma {#lem:class-leaf-differences}** (The planar shear of nearby solutions.) Let ů be a smooth state on a
neighbourhood of the closure of 𝒰, for instance a smooth class solution with ∂_z ů_A ≠ 0 on the axis, p_A := dů_A and
Θ_A := □ů_A; its leaves h̊ and its planar shear σ[ů] are those defined before [[lem:class-leaf-states]], as are the
leaves and the planar shear of every state U. For a state U on Σ and m ≥ 0 let

    𝒩_m(U) := Σ_(j≤m) ‖∂^j (W_U − W_ů)‖_(L²(Σ∩𝒰)),

∂^j all derivatives of order j in x; for a family U(τ) of states on the slices Σ_τ of an interval, for instance a
solution, let 𝒩_m(U)(τ) be the same expression on Σ_τ with ∂^j all spacetime derivatives of order j. When ů and U are
solutions, 𝒩_m is at most twice [[eq:class-energy]]. Let k ≥ 6. There are δ > 0, a ball 𝔅 around ů in the norm 𝒩_k, a
ball 𝔅′ ⊃ 𝔅 around ů in the norm 𝒩_(k−1), and C, such that the states of 𝔅′ have bounds (M, c) for which 4δ ≤ r_1, r_1
of [[lem:class-leaf-states]], and:

(a) ‖∂^α(σ[U]² − σ[ů]²)‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U) for |α| ≤ k, both for a state U ∈ 𝔅, ∂^α the derivatives in x, and for
a family of states in 𝔅, ∂^α the spacetime derivatives and 𝒩_k(U) taken at the time considered; and for m > k and a
state U ∈ 𝔅 with 𝒩_m(U) < ∞, ‖σ[U]² − σ[ů]²‖_(H^m(𝒰_δ)) ≤ C_m 𝒩_m(U), C_m depending also on m and on an upper bound
for 𝒩_(m−1)(U);
(b) ‖σ[U] − σ[U′]‖_(L²(𝒰_δ)) ≤ C ‖U − U′‖_(L²(𝒰_(2δ))) and |σ[U]| ≤ C on 𝒰_δ, for U, U′ ∈ 𝔅′;
(c) for U ∈ 𝔅, δh(z0, y) := h_U(|y|; z0) − h̊(|y|; z0), the difference of the leaves through one axis point, and I :=
[z(p) − δ, z(p) + δ], Σ_(j≤2) ‖∂_(z0)^j δh‖_(L²(I; H^(k+2−j)(𝔻_δ))) ≤ C 𝒩_k(U); and for a family of states in 𝔅, every
derivative of δh in (τ, z0, y) of order at most k − 2 is bounded on I × 𝔻_δ by C 𝒩_k(U).

C depends only on ů, k and ρ1(p), and in (b) only on the bounds (M, c). The planar shear enters [[eq:class-x]], and the
closure of the Raychaudhuri equation at an axis, through σ². For a solution of the class system with p_A = du_A and
Θ_A = □_g u_A the leaves are the level sets of u_A near the axis, and σ[U] is the planar shear [[eq:class-shear-leaf]] of
those level sets.

*Proof.* Constants C depend only on ů, k and ρ1(p), and C_m also on m and on an upper bound for 𝒩_(m−1)(U).

*The balls.* As ů is smooth up to the closure of 𝒰, with p_A(∂_z) ≠ 0 on the axis, it has bounds (M_0, 2c_0) for some
M_0 and c_0. On the Lipschitz domain Σ ∩ 𝒰, Sobolev's embedding ([[thm:std-bh-embedding]], 3 · 2 > 4) gives sup |f| ≤
C Σ_(j≤3) ‖∂^j f‖; applied to the derivatives of W_U − W_ů, spacetime ones for a family,

    sup_(Σ∩𝒰) |∂^i (W_U − W_ů)| ≤ C 𝒩_(i+3)(U).                                                      {#eq:class-leaf-sup}

So there is r′ > 0 such that every state with 𝒩_4(U) ≤ r′ has bounds (M, c) := (2M_0, c_0): the C² norms of its metric
and the C¹ norms of its p_A and Θ_A differ from those of ů by at most C r′, and so do the quantities bounded below in
the definition of bounds. Let 𝔅′ := {𝒩_(k−1) ≤ r′}, as k − 1 ≥ 4; let r_1 and C_0, …, C_4 be the numbers of
[[lem:class-leaf-states]] and its proof for (M, c), δ := min(r_1/4, 1/(9C_0), δ_1) with δ_1 > 0 fixed in Step 5 below,
depending only on (M, c) and ů, and 𝔅 := {𝒩_k ≤ r″}, with r″ ∈ (0, r′/2] fixed in Step 3 below.

*(b)* is [[lem:class-leaf-states]] (c) with D := Σ, as 2δ ≤ r_1/2, together with its part (a).

*The last statement.* Let g⁻¹(du_A, du_A) = 0, p_A = du_A, Θ_A = □_g u_A and ∂_z u_A ≠ 0 near the axis. By
[[lem:class-leaf]] (b) the level set of u_A through an axis point (z0, 0) is, near it, an invariant smooth graph
z = h(y) with h(0) = z0, and du_A = ∂_z u_A dF along it, F := z − h(y); so |∇_M3 u_A| = |p_A^Σ|, ν_L = εν, and Π is its
tangent plane TΣ_L. By [[lem:class-gauss]] (b), tr χ̸ = |∇_M3 u_A| tr k_L − n(u_A) tr K_Σ|_(TΣ_L) = Θ_A − κ_A1, k_L
taken for ν_L; so its mean curvature for ν is H_L[U], as in step (1) of the proof of [[lem:class-planar-shear]]. By
[[lem:class-leaf]] (c), h′(0) = 0 and (r h′)′ = r H_L[U]/a_L − E_L for r > 0; integrating from 0 gives
[[eq:class-leaf-volterra]], and h is the leaf of U through z0, by the uniqueness in [[lem:class-volterra]]. Then k_r,
k_φ, e_r and e2 are those of the level set, and σ[U] is [[eq:class-shear-leaf]] for it.

*(a) and (c).* *Step 1 (Smooth states suffice).* It suffices to prove (a) and (c) for smooth states, or smooth families,
with 𝒩_k(U) ≤ 2r″, with constants that do not depend on their smoothness. Indeed, for U ∈ 𝔅 let U_n be obtained by
extending the components of g, ∂_τ g, p_A and Θ_A from Σ ∩ 𝒰 by Stein's operator ([[thm:std-sy-extension]]),
mollifying, averaging over G, which acts by isometries of ℝ⁴, and restricting; for a family, likewise in (τ, x). Then
Σ_(j≤m) ‖∂^j (W_(U_n) − W_U)‖ → 0 for every m with 𝒩_m(U) < ∞, so 𝒩_k(U_n) ≤ 2r″ for n large. By (b), σ[U_n] → σ[U]
in L²(𝒰_δ), and these functions are bounded by C, so σ[U_n]² → σ[U]² in L²(𝒰_δ); a sequence bounded in H^m and
convergent in L² has its limit in H^m, with the same bound. For (c), the proof of [[lem:class-leaf-states]] (b) gives
sup |h_(U_n) − h_U| ≤ C sup |U_n − U| → 0 on the leaves, and the bounds pass to the limit in the same way. From now on U
is smooth, or a smooth family, with 𝒩_k(U) ≤ 2r″.

*Step 2 (Leaf coordinates and norms).* Let Q_ρ := 𝒰_ρ ∩ M3 in the coordinates (z, y), Q̂ := {(z0, y) : |z0 − z(p)| <
3δ, |y| < 3δ}, and, for X ∈ {U, ů}, Λ_X(z0, y) := (h_X(|y|; z0), y), which is smooth, injective on Q̂ and has
Jacobian ∂_(z0) h_X ∈ [1/2, 3/2] ([[lem:class-leaf-states]] (a)). As |h_X − z0| ≤ C_0 (3δ)²/2 ≤ δ/2, Λ_X(Q̂) ⊂ Q_(4δ),
and Λ_X maps {|z0 − z(p)| < 3δ, |y| < ρ} onto a set containing Q_δ for ρ ≥ δ. For a G-invariant function f on 𝒰_ρ,
ρ ≤ 4δ, the H^m norms of f on Σ ∩ 𝒰_ρ and of f(z, y) on Q_ρ agree up to factors depending only on m and ρ1(p): the
volume elements differ by the factor 2π z of the proof of [[lem:class-leaf-states]] (c), and ∂_(x_i) f = (x_i/ρ1) ∂_z f
for i = 1, 2 and ∂_z f = Σ_(i≤2) (x_i/ρ1) ∂_(x_i) f, the functions x_i/ρ1 having bounded derivatives of every order
where ρ1 ≥ ρ1(p)/2. Below, D denotes the derivatives in (z0, y), or in (z, y), and, for a family, also in τ; T denotes
∂_(z0) and, for a family, also ∂_τ; all norms are taken at the time considered, and a norm without index on Q̂, on
Q_(4δ) or on a subset is that of L², ‖f‖_n := Σ_(|α|≤n) ‖D^α f‖. Put ω := W_U − W_ů and ω_g := g_U − g_ů on Q_(4δ),
and Ω_n := ‖ω‖_n + ‖ω_g‖_(n+1) on Q_(4δ); then Ω_n ≤ C 𝒩_n(U), the first derivatives of g being components of W.

*Step 3 (The divergence form).* Let X ∈ {U, ů}. For a C¹ G-invariant function h on a disc of the y-plane put F :=
z − h(y), let ν be the unit normal γ3⁻¹dF/|dF| of the graphs z = h(y) + const, a field near the graph that depends on
(z, y) and on ∂h(y), let √γ := (det γ3)^(1/2) in the coordinates (z, y), and 𝔙(y, z, P; w) := √γ ν^y at (z, y), with
∂h replaced by P ∈ ℝ², ν^y := (ν^(y1), ν^(y2)) and w the value of g_X there. The mean curvature of a C² graph at its
points is (√γ)⁻¹ ∂_a(√γ ν^a), and along the graph ∂_(y_i)[𝔙^i(y, h, ∂h)] = (∂_i(√γ ν^i) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)),
∂_z at fixed ∂h. So the graph has mean curvature H_L[X] at its points exactly when

    div_y 𝔙(y, h, ∂h) = Φ_X(y, h, ∂h),      Φ_X := (√γ H_L[X] − ∂_z(√γ ν^z) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)),      {#eq:class-leaf-divergence}

Φ_X a smooth function of (y, h, ∂h) and of W_X at (h(y), y). The leaf h_X(·; z0) satisfies [[eq:class-leaf-divergence]]
off the axis (Step 6 of the proof of [[lem:class-leaf-states]]), and 𝔙(y, h_X, ∂h_X) is an invariant vector field,
v(|y|) y, with (r² v)′ = r div(v y) = r Φ_X for r > 0 and r² v → 0; so

    𝔙(y, h_X, ∂h_X) = y 𝔰_X,      𝔰_X(y) := ∫_0^1 t Φ_X(t y) dt.                                  {#eq:class-leaf-radial}

By [[lem:class-leaf]] (b), ∂_P 𝔙 = −√γ |dF|⁻¹ (γ3^(ij) − ν^i ν^j)_(i,j) is negative definite, with eigenvalues in
[−Λ_1, −1/Λ_1] for |P| ≤ 1, Λ_1 depending only on M; so P ↦ 𝔙(y, z, P; w) is injective on {|P| ≤ 1}, its inverse
𝔓(y, z, ·; w) is smooth on the image, and

    ∂_y h_X = 𝔓(y, h_X, y 𝔰_X; g_X(h_X, y)).                                                     {#eq:class-leaf-inverse}

On the tangent plane TΣ_L of the graph, spanned by X_i := ∂_(y_i) + ∂_i h ∂_z, the second fundamental form for ν is
k_L(X_i, X_j) = −(∂_i ∂_j h + Γ[γ3]^c_ab X_i^a X_j^b ∂_c F)/|dF|. The form χ̸ := ε |p_A^Σ| k_L − p_A(n) K_Σ on TΣ_L is
diagonal in the frame (e_r, e2), by the reflection y2 ↦ −y2 at the points (z, (r, 0)), and χ̸(e_r, e_r) − χ̸(e2, e2) =
σ[X]; so σ[X]² = 2 |χ̸ − ½ (tr χ̸) γ̸|², γ̸ the induced metric, a symmetric form on a plane with eigenvalues a and b
having trace-free part of squared norm (a − b)²/2. In the frame (X_i) this reads

    σ[X]² ∘ Λ_X = 𝔗(y, h_X, ∂_y h_X, ∂_y² h_X; W_X ∘ Λ_X),                                        {#eq:class-leaf-square}

𝔗 a smooth function, the same for all states, the contractions being taken with γ̸_ij = γ3(X_i, X_j).

*Step 4 (Bounds of low order).* For X ∈ {U, ů} write s_X := h_X′/r, the solution of [[eq:class-leaf-s]]; it is smooth
and even (Step 7 of the proof of [[lem:class-leaf-states]]), and by Step 2 of that proof the integrand of
[[eq:class-leaf-s]] is 𝔤̂(r t, s, W_X(h, (r t, 0))) with 𝔤̂ smooth, the same for all states. Differentiating
[[eq:class-leaf-s]] once or twice in r, z0 and, for a family, τ, each derivative of s_X solves a linear equation whose map
has norm at most 1/2, as in that Step 7, and whose inhomogeneous term holds derivatives of order at most 2 of W_X and
derivatives of s_X and h_X of lower order; with [[eq:class-leaf-sup]] at i ≤ 2, so 𝒩_5 ≤ 𝒩_k, the derivatives of order
at most 2 of s_X, of h_X = z0 + |y|² ∫_0^1 θ s_X(θ |y|) dθ, of ∂_y h_X = s_X y, of W_X ∘ Λ_X, of g_X ∘ Λ_X and of
𝔰_X = ∫_0^1 t Φ_X(t ·) dt are bounded on Q̂ by C. The same equations for the differences η := h_U − h_ů, δs := s_U −
s_ů, with the terms in ω ∘ Λ_U as inhomogeneous terms, bound the derivatives of order at most 2 of η, ∂_y η, δs,
δ𝔰 := 𝔰_U − 𝔰_ů, ω ∘ Λ_U and ω_g ∘ Λ_U on Q̂ by C 𝒩_k(U). We fix r″ so small that these bounds are at most 1.

*Product and composition rules.* (P) The terms estimated below at an order n, n ≤ k + 1, or n ≤ m + 1 in the second part
of (a), are sums of products of a bounded smooth function with derivatives of factors among h_X, ∂_y h_X, s_X, 𝔰_X,
y 𝔰_X, W_X ∘ Λ_X, g_X ∘ Λ_X, ∂_y² h_X and their differences, in which the numbers of derivatives add to at most n.
Every factor but the one carrying the most derivatives carries a ≤ n/2 of them. If a ≤ 1, it is bounded by Step 4.
If two factors carry two derivatives each and n = 4, Hölder's inequality and H¹(Q̂) ⊂ L⁴ ([[thm:std-bh17-embedding]])
bound their product by norms of order 3. Otherwise a ≤ n − 3, and the factor is bounded pointwise by Sobolev's
embedding H²(Q̂) ⊂ L^∞ ([[thm:std-bh-embedding]], 2 · 2 > 3) and its norm of order a + 2, below the order of the term
and bounded before, or, for a derivative of ω or ω_g, by [[eq:class-leaf-sup]], with 𝒩_(a+3) ≤ 𝒩_k for n ≤ k + 1, k ≥ 6, and
𝒩_(a+3) ≤ 𝒩_(m−1) for n ≤ m + 1, m ≥ 7. So the L² norm of such a product is at most C, or C_m, times the L² norm of its
factor of highest order, or the norms of order below n just named. (Q) For F on Q_(4δ) and |α| ≤ n, D^α(F ∘ Λ_U) is a sum of
products of (D^β F) ∘ Λ_U, |β| ≥ 1, with factors D^(α_i) Λ_U, |α_i| ≥ 1, Σ |α_i| = |α|; counting D^(α_i) Λ_U as a
derivative of order |α_i| − 1 of DΛ_U, the orders add to |α|. (P) applies, and the change of variables Λ_U, with
Jacobian at least 1/2, gives ‖(D^β F) ∘ Λ_U‖ ≤ √2 ‖D^β F‖ on Q_(4δ). With F := ω, and F := ω_g at the order n + 1, the
term in which all of D^α falls on h_U being multiplied by sup |Dω| ≤ C 𝒩_k(U),

    ‖ω ∘ Λ_U‖_n + ‖ω_g ∘ Λ_U‖_(n+1) ≤ C (Ω_n + 𝒩_k(U) (‖η‖_n + ‖∂_y η‖_n)).                      {#eq:class-leaf-compose}

The same holds with Λ_U⁻¹ in place of Λ_U, for functions on Q̂: DΛ_U⁻¹ = B ∘ Λ_U⁻¹ with B a smooth function of Dh_U,
∂_(z0) h_U ≥ 1/2, so the derivatives of Λ_U⁻¹ are polynomials in the derivatives of h_U composed with Λ_U⁻¹, and the
Jacobian of Λ_U⁻¹ lies in [2/3, 2].

*Step 5 (Transverse derivatives).* For X ∈ {U, ů}, 𝔤̂(r t, s_U, W_U(h_U, ·)) − 𝔤̂(r t, s_ů, W_ů(h_ů, ·)) = a_1 · (ω ∘
Λ_U) + a_2 δs + a_3 η at the point (r t, 0) of the leaves, with a_1, a_2, a_3 smooth functions of r t, s_U, s_ů, W_U ∘
Λ_U, W_ů ∘ Λ_U and W_ů ∘ Λ_ů, the last difference being (∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ) η; and |a_2| = |∂_s 𝔤̂| ≤ C_2 (1
+ C_0) r t and |a_3| ≤ C. Let j ≤ k, or j ≤ m. Applying T^j to the difference of the equations [[eq:class-leaf-s]],

    T^j δs(r) = ∫_0^1 t (a_2 T^j δs + a_3 T^j η + a_1 · T^j(ω ∘ Λ_U) + R_j)(r t) dt,
    T^j η(r) = r² ∫_0^1 θ T^j δs(θ r) dθ,

R_j the terms of Leibniz's rule in which δs, η or ω ∘ Λ_U carries fewer than j derivatives. As ‖F(t ·)‖_(L²(𝔻_ρ)) ≤
t⁻¹ ‖F‖_(L²(𝔻_ρ)), Minkowski's inequality bounds the operators F ↦ ∫_0^1 t F(t ·) dt and F ↦ |y|² ∫_0^1 θ F(θ ·) dθ on
L²(𝔻_ρ), ρ ≤ 3δ, by 1 and by 9δ², on each disc of fixed (τ, z0), as in the proof of [[lem:class-leaf-states]] (c). So
‖T^j η‖ ≤ 9δ² ‖T^j δs‖ and ‖T^j δs‖ ≤ (3C_2 (1 + C_0) δ + 9C δ²) ‖T^j δs‖ + C ‖T^j(ω ∘ Λ_U)‖ + ‖R_j‖ on Q̂. Fix δ_1
with 3C_2 (1 + C_0) δ_1 + 9C δ_1² ≤ 1/2. By (P), and by induction on j, ‖R_j‖ ≤ C (Ω_j + 𝒩_k(U)) for j ≤ k, the
factors of R_j other than δs, η and ω ∘ Λ_U being bounded in the norms of order j by Step 4 and (Q), and ‖R_j‖ ≤ C_m
(Ω_j + 𝒩_k(U)) for k < j ≤ m. By (Q), ‖T^j(ω ∘ Λ_U)‖ ≤ C (Ω_j + 𝒩_k(U) ‖T^j η‖) plus terms bounded by (P) and the
derivatives of η of order below j. With ∂_y η = δs y and Ω_j ≤ C 𝒩_j(U), induction on j gives, on Q̂,

    ‖T^j δs‖ + ‖T^j η‖ + ‖T^j ∂_y η‖ ≤ C 𝒩_k(U) for j ≤ k,      ≤ C_m 𝒩_m(U) for k < j ≤ m.   {#eq:class-leaf-transverse}

*Step 6 (Derivatives along the disc).* Let ρ_n := (3/2 + 3 · 2^(−n−2)) δ and Q̂_n := {|z0 − z(p)| < 3δ, |y| < ρ_n}, and
for functions on Q̂_n let ‖f‖_(j,n) be the L² norm in z0 of the H^(n+2−j) norm in y on 𝔻_(ρ_n). We show, by induction
on n, for n ≤ k, and for n ≤ m in the second part of (a),

    Σ_(j≤n) ‖T^j η‖_(j,n) ≤ C 𝒩_k(U)      (n ≤ k),      Σ_(j≤n) ‖T^j η‖_(j,n) ≤ C_m 𝒩_m(U)      (k < n ≤ m),   {#eq:class-leaf-elliptic}

T^j any product of j transverse derivatives; for n − 1 it holds by induction (it is empty for n = 0), and with Step 5
it bounds all norms of order below n + 2 of η, ∂_y η, δs, δ𝔰 and of order below n + 1 of ω ∘ Λ_U that (P) uses. We
write the bound for n ≤ k; for n > k the same lines give C_m 𝒩_m(U).

(i) δΦ := Φ_U(y, h_U, ∂_y h_U; W_U ∘ Λ_U) − Φ_ů(y, h_ů, ∂_y h_ů; W_ů ∘ Λ_ů) is a smooth function of these arguments
times (η, ∂_y η, ω ∘ Λ_U, W_ů ∘ Λ_U − W_ů ∘ Λ_ů), the last being (∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ) η. For j + |β| ≤ n,
T^j ∂_y^β δΦ is a sum of terms linear in T^j ∂_y^β of η, ∂_y η and ω ∘ Λ_U, with bounded coefficients, and of products
of lower order covered by (P). The derivatives T^j ∂_y^β ∂_y η, n + 1 derivatives of η, are bounded by
[[eq:class-leaf-elliptic]] at n − 1 for j ≤ n − 1 and by [[eq:class-leaf-transverse]] for j = n; those of η by both;
those of ω ∘ Λ_U by [[eq:class-leaf-compose]]. So Σ_(j+|β|≤n) ‖T^j ∂_y^β δΦ‖ ≤ C 𝒩_k(U) on Q̂_(n−1), Q̂_(−1) := Q̂.

(ii) Put u_X(y) := |y|² ∫_0^1 t 𝔰_X(t y) dt, a radial function with ∇_y u_X = y 𝔰_X and, by
[[eq:class-leaf-radial]], Δ_y u_X = div_y(y 𝔰_X) = Φ_X. So δu := u_U − u_ů satisfies Δ_y T^j δu = T^j δΦ on each disc
of fixed (τ, z0). By [[lem:class-interior-regularity]] with L := Δ_y, c_a = 1 and j := n − j, whose proof applies to any
two concentric discs, here 𝔻_(ρ_n) ⊂ 𝔻_(ρ_(n−1)), with C depending also on their radii,

    ‖T^j δu‖_(H^(n−j+2)(𝔻_(ρ_n))) ≤ C (‖T^j δΦ‖_(H^(n−j)(𝔻_(ρ_(n−1)))) + ‖T^j δu‖_(L²(𝔻_(ρ_(n−1))))),

and the last norm is at most 9δ² ‖T^j δΦ‖_(L²(𝔻_(ρ_(n−1)))), by the operator bounds of Step 5 applied to δ𝔰 = ∫_0^1 t
δΦ(t ·) dt and to δu. Squaring, integrating over z0 and using (i), Σ_(j≤n) ‖T^j ∇_y δu‖_(L²(H^(n+1−j))) ≤ C 𝒩_k(U)
on Q̂_n.

(iii) By [[eq:class-leaf-inverse]], ∂_y η = 𝔓(y, h_U, ∇_y u_U; g_U ∘ Λ_U) − 𝔓(y, h_ů, ∇_y u_ů; g_ů ∘ Λ_ů), a smooth
function of these arguments times (η, ∇_y δu, ω_g ∘ Λ_U, g_ů ∘ Λ_U − g_ů ∘ Λ_ů). For j ≤ n and |β| ≤ n + 1 − j,
T^j ∂_y^β ∂_y η is a sum of terms linear in T^j ∂_y^β of η, ∇_y δu and ω_g ∘ Λ_U, with bounded coefficients, and of
products covered by (P), with n + 1 derivatives in all. The derivatives of ∇_y δu are bounded by (ii); those of η, which
carry |β| ≥ 1 derivatives in y as j ≤ n, by [[eq:class-leaf-elliptic]] at n − 1 for j ≤ n − 1 and by
[[eq:class-leaf-transverse]] for j = n; and those of ω_g ∘ Λ_U by [[eq:class-leaf-compose]], whose term in ∂_y η of
order n + 1 carries the factor C 𝒩_k(U) ≤ 2C r″ and is absorbed for r″ small. So Σ_(j≤n) ‖T^j ∂_y η‖_(L²(H^(n+1−j)))
≤ C 𝒩_k(U) on Q̂_n, which with [[eq:class-leaf-transverse]] for ‖T^j η‖ is [[eq:class-leaf-elliptic]] at n.

*Step 7 (Conclusion).* By [[eq:class-leaf-square]], S := σ[U]² ∘ Λ_U − σ[ů]² ∘ Λ_ů is a smooth function times (η, ∂_y η,
∂_y² η, ω ∘ Λ_U, W_ů ∘ Λ_U − W_ů ∘ Λ_ů). Its derivatives of order at most k are bounded in L²(Q̂_k) by (P),
[[eq:class-leaf-elliptic]] at n = k, which bounds T^j ∂_y^β ∂_y² η for j + |β| ≤ k, and [[eq:class-leaf-compose]]:
‖S‖_k ≤ C 𝒩_k(U) on Q̂_k, and likewise ‖S‖_m ≤ C_m 𝒩_m(U) on Q̂_m. Write S̊ := σ[ů]² ∘ Λ_ů, a smooth function on Q̂.
Then σ[U]² − σ[ů]² = S ∘ Λ_U⁻¹ + S̊ ∘ Λ_U⁻¹ − S̊ ∘ Λ_ů⁻¹, and as h_U(|y|; z0[U]) = z, Λ_ů ∘ Λ_U⁻¹(z, y) = (z − η(Λ_U⁻¹(z,
y)), y), so that

    S̊ ∘ Λ_U⁻¹ − S̊ ∘ Λ_ů⁻¹ = −(∫_0^1 ∂_z(S̊ ∘ Λ_ů⁻¹)(z − θ η ∘ Λ_U⁻¹, y) dθ) η ∘ Λ_U⁻¹.

Λ_U maps Q̂_k onto a set containing Q_δ (Step 2, ρ_k > δ), and (Q) for Λ_U⁻¹, with (P), gives ‖σ[U]² −
σ[ů]²‖_(H^k(Q_δ)) ≤ C (‖S‖_k + ‖η‖_k) ≤ C 𝒩_k(U), and at the order m the bound C_m 𝒩_m(U). By Step 2 these are the
bounds of (a) on 𝒰_δ, with the derivatives in x for a state and the spacetime derivatives for a family. For (c),
[[eq:class-leaf-elliptic]] at n = k with j ≤ 2, restricted to I × 𝔻_δ ⊂ Q̂_k, is the first bound; for a family it bounds
every derivative of η of order at most k in (τ, z0, y) in L²(Q̂_k), and Sobolev's embedding H²(Q̂_k) ⊂ L^∞ gives the
second. ∎
