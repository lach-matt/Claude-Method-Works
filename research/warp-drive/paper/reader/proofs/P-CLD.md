### Block. The leaves of a state, and the planar shear of nearby states

The text of this block replaces [[lem:class-leaf-differences]], its statement and its proof, in
[[sec:class-planar-shear]] of [[ch:class-system]]; the Placement section gives the position. It consists of a paragraph
of definitions, [[lem:class-leaf-states]] with its proof, and [[lem:class-leaf-differences]] with its proof.

Let Σ be a slice {τ = const} of a chart (τ, x) on a G-invariant open set in which G acts on x ∈ ℝ⁴ by its action on ℝ⁴
and Σ is spacelike for the metrics considered. The chart of [[sec:background]] is one, and the constructions of this
section use of it only these properties, through the future unit normal n and the second fundamental form K_Σ of Σ, the
totally geodesic M3 := Σ ∩ {φ1 = 0} and the coordinates (z, y) of [[lem:class-leaf]]. Fix a point p of axis 2 with
ρ1(p) > 0, a family A and a radius r_* ∈ (0, ρ1(p)/4], write r := |y|, z(p) for the value of z at p and 𝒰 := 𝒰_(r_*),
so that 𝒰_δ ∩ M3 = {|z − z(p)| < δ, |y| < δ} for δ ≤ ρ1(p)/4.

A *state* is a G-invariant U = (g, p_A, Θ_A, q_A) on 𝒰, given on Σ ∩ 𝒰 together with the first derivatives of g, with g
a Lorentzian metric for which Σ is spacelike and p_A(∂_z) ≠ 0 on the axis. We write W_U := (g, ∂g, p_A, Θ_A), ∂g all
first derivatives of the components of g in the chart, the one normal to Σ included, require W_U to be of class C¹ on Σ
∩ 𝒰, and write |U − U′| at a point for the sum of the absolute values of the components of W_U − W_(U′) there, so that
U − U′ includes the difference of the first derivatives of the metrics. A state has *bounds* (M, c), M ≥ 1 and c > 0,
if on Σ ∩ 𝒰 the C¹ norms of the components of W_U are at most M, g(X, X) ≥ |X|²/M for X tangent to Σ, |X| its flat
length, −g⁻¹(dτ, dτ) ≥ 1/M, and |p_A(∂_z)| ≥ c on the axis. Let p_A^Σ be the spatial part of p_A, tangent to M3 at its
points by invariance, ε the sign of p_A(∂_z), and, where p_A^Σ ≠ 0,

    H_L[U] := ε (Θ_A − κ_A1 + p_A(n) tr K_Σ|_Π)/|p_A^Σ|,      Π the γ3-orthogonal complement of p_A^Σ in TM3:

the formula of step (1) of the proof of [[lem:class-planar-shear]] with Θ_A, p_A^Σ and p_A(n) in place of Θ, ∇_Σ u and
n(u), and with the plane Π, which p_A fixes at each point, in place of TΣ_L. So H_L[U] is a function of the point, as
[[lem:class-volterra]] requires; when p_A is the differential of a phase, Π is the tangent plane of the level set of
the phase in M3 through the point, and H_L[U] is that formula for the level set. The *leaves* of U are the solutions
h(·; z0) of [[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, read as the graphs z = h(|y|; z0).
For a point x on a leaf, σ[U](x) := ε |p_A^Σ| (k_r − k_φ) − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e2, e2)) at x, with k_r and k_φ
the principal curvatures of the leaf in M3 for the normal ν of [[lem:class-leaf]] (b), e_r its unit tangent in the
meridional plane and e2 := K2/|K2|: this is [[eq:class-shear-leaf]] with p_A in place of du, the normal ν_L there being
εν. The *arc* of U through x is {(h(t; z0), t y(x)/r_x) : 0 ≤ t ≤ r_x}, with r_x := |y(x)| and z0 the axis point of the
leaf through x. Near axis 1 the same holds with the two planes exchanged and κ_A2 in place of κ_A1.

**Lemma {#lem:class-leaf-states}** (The leaves of a state.) Let M ≥ 1 and c > 0. There are r_1 ∈ (0, r_*/8] and C,
depending only on M, c, ρ1(p) and r_*, such that for all states U and U′ with bounds (M, c):

(a) (Foliation.) For |z0 − z(p)| ≤ r_1 the leaf h(·; z0) of U is defined on [0, r_1], with |h′(r; z0)| ≤ C r, and for
two such axis points z0 ≠ z0′ and 0 ≤ r ≤ r_1

    1/2 ≤ (h(r; z0) − h(r; z0′))/(z0 − z0′) ≤ 3/2,
    |h′(r; z0) − h′(r; z0′)| ≤ C r |z0 − z0′|.                                                  {#eq:class-leaf-quotient}

Every point x of 𝒰_(r_1/2) lies on exactly one of these leaves; we write z0[U](x) for its axis point. The arc of U
through a point of 𝒰_δ, δ ≤ r_1/2, lies in 𝒰_(2δ), and |σ[U]| ≤ C on 𝒰_(r_1/2). If U is smooth, the map (z0, y) ↦
h(|y|; z0) and the function z0[U] are smooth, and they depend smoothly on parameters on which U depends smoothly.

(b) (Along one arc.) For x ∈ 𝒰_(r_1/2), with r_x := |y(x)| and f(t) := |U − U′| at the point of the arc of U through x
at radius t,

    |σ[U](x) − σ[U′](x)|
        ≤ C (f(r_x) + r_x⁻² ∫_0^(r_x) t f(t) dt + (∫_0^(r_x) t f(t)² dt)^(1/2)).  {#eq:class-leaf-pointwise}

(c) (On sets closed under arcs.) Let 0 < δ ≤ r_1/2, and let D ⊂ Σ be a measurable G-invariant set such that the arc of
U through every point of D ∩ 𝒰_δ lies in D. Then

    ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D∩𝒰_(2δ))).                                         {#eq:class-leaf-sets}

Only the values of U − U′ on the arcs of U enter (b) and (c), and C depends neither on D nor on δ.

*Proof.* Constants C, C_0, C_1, … depend only on M, c, ρ1(p) and r_*.

*Step 1 (H_L).* At a point of the axis every rotation of y fixes the point, so the invariant covector p_A^Σ has no
component along dy there, p_A^Σ = p_A(∂_z) dz, and γ3 has no component along dz dy (as in the proof of
[[lem:class-leaf]] (a)); so |p_A^Σ| = |p_A(∂_z)| A3^(−1/2) ≥ c M^(−1/2), as A3 ≤ M. The function |p_A^Σ|² has Lipschitz
constant at most C, so there is r_2 ∈ (0, r_*/4] with |p_A^Σ| ≥ c M^(−1/2)/2 on 𝒰_(4r_2), where p_A(∂_z) then has the
constant sign ε. There H_L[U](x) = ℋ(x, W_U(x)), with ℋ a smooth function, the same for all states, on the set of (x,
w) with ρ1 ≥ ρ1(p)/2 at which the components of w satisfy the lower bounds g(X, X) ≥ |X|²/(2M), −g⁻¹(dτ, dτ) ≥ 1/(2M)
and |p_A^Σ| ≥ c M^(−1/2)/4: n, K_Σ and γ3 are smooth functions of the metric and its first derivatives, κ_A1 = g⁻¹(p_A,
dψ1) with ψ1 = ½ log g(K1, K1) and g(K1, K1) ≥ ρ1²/M, and Π and the trace of K_Σ over it are smooth functions of γ3,
K_Σ and p_A^Σ ≠ 0. As W_U is of class C¹ with C¹ norm at most C, so is H_L[U] on 𝒰_(4r_2).

*Step 2 (The function G).* At the point (z, (r, 0)) write γ_zz := γ3(∂_z, ∂_z) = A3, γ_z1 := γ3(∂_z, ∂_(y1)) = C3 r,
γ_11 := γ3(∂_(y1), ∂_(y1)) = B3 + D3 r² and γ_22 := γ3(∂_(y2), ∂_(y2)) = B3. By invariance γ3(∂_z, ∂_(y_i)) = C3 y_i
near the axis, a vector field on the y-plane invariant under its rotations and reflections being a multiple of y by a
function of |y|; so C3 = ∂_(y2) γ3(∂_z, ∂_(y2)) at (z, (r, 0)), a component of the first derivatives of g there. With h
:= z and h′ := q, det₂ = γ_zz γ_11 − γ_z1² ≥ M⁻² and N_L² = γ3(∂_(y1) + q ∂_z, ∂_(y1) + q ∂_z) ≥ (1 + q²)/M. By the
proof of [[lem:class-volterra]], E_L = ν^r/a_L − q + r B̃/a_L, with ν^r/a_L = (γ_z1 + γ_zz q) N_L²/det₂ and B̃ the part
of H_L free of h″ and of ν^r/r in the divergence formula of the proof of [[lem:class-leaf]] (c); in that formula (det
γ3)^(1/2) = r (γ_22 det₂)^(1/2), ν^z = (γ_11 + γ_z1 q)/(det₂^(1/2) N_L) and ν^r = −(γ_z1 + γ_zz q)/(det₂^(1/2) N_L), so
B̃ is a smooth function of q and of the components of γ3 and their first derivatives at the point. As det₂ − γ_zz
N_L² = −(γ_z1 + γ_zz q)², the function G(r, z, q) := r H(z, r)/a_L − E_L of that proof, H(z, r) := H_L[U] at (z, (r,
0)), is

    G(r, z, q) = r (H/a_L − C3 N_L²/det₂ − B̃/a_L) − q (C3 r + γ_zz q)²/det₂.                          {#eq:class-leaf-g}

On R := {0 ≤ r ≤ r_2, |z − z(p)| ≤ r_2, |q| ≤ 1} the first bracket and its first derivatives in z and in q are bounded
by C, by Step 1 and the C¹ bounds of W_U, and ∂_z(C3 r + γ_zz q) = r ∂_z C3 + q ∂_z γ_zz. So G(0, z, q) = −γ_zz
q³/γ_22, and on R

    |G(r, z, 0)| ≤ C_0 r,      |∂_z G| ≤ C_1 (r + |q|),      |∂_q G| ≤ C_2 (r + |q|).           {#eq:class-leaf-g-bounds}

Every factor of [[eq:class-leaf-g]] is a smooth function of r, q and the values of W_U at the point, with ℋ in place of
H; so for a second state U′ with bounds (M, c) and the same (r, z, q) ∈ R, |G_U − G_(U′)| ≤ C (r + |q|) |U − U′| at (z,
(r, 0)), G_U and G_(U′) the functions [[eq:class-leaf-g]] of the two states.

*Step 3 (One leaf).* Put δ_p := min(1, 1/(8C_2)) and r_0 := min(1, r_2/2, δ_p/C_0, 1/(8C_2), 1/(4C_1),
(r_2/C_0)^(1/2)). For |z0 − z(p)| ≤ r_2/2 consider the map 𝒯 of the proof of [[lem:class-volterra]] on {p ∈ C([0, r_0])
: sup |p| ≤ δ_p}, which uses of G only G(0, z, q) = −γ_zz q³/γ_22 and bounds of the form [[eq:class-leaf-g-bounds]],
here with |∂_z G| ≤ 2C_1 on R. As there, |𝒯p(r)| ≤ C_0 r/2 + C_2 (r_0 + δ_p) δ_p ≤ δ_p and 𝒯 has Lipschitz constant at
most C_1 r_0 + C_2 (r_0 + δ_p) ≤ 1/2; its fixed point is the leaf on [0, r_0], with |h′(r)| ≤ C_0 r ≤ 1 and |h(r) − z0|
≤ C_0 r²/2 ≤ r_2/2, so that it stays in R, and that proof gives its uniqueness among the C¹ solutions with h(0) = z0.

*Step 4 (Two axis points).* For |z_i − z(p)| ≤ r_2/2, i = 1, 2, let h_i be the leaves, w_i := h_i′, Δz := z_1 − z_2 and
D(r) := sup_[0,r] |w_1 − w_2|. Along both leaves, and on the segment between their values, |q| ≤ C_0 ρ, so by
[[eq:class-leaf-g-bounds]] the values of G at (ρ, h_1, w_1) and at (ρ, h_2, w_2) differ by at most C_4 ρ (|h_1 −
h_2| + |w_1 − w_2|), C_4 := (C_1 + C_2)(1 + C_0); and |h_1 − h_2|(ρ) ≤ |Δz| + ρ D(ρ). Subtracting the two Volterra
equations, r |w_1 − w_2|(r) ≤ C_4 r² (|Δz| + 2D(r))/2 for r ≤ r_0, so D(r) ≤ C_4 r |Δz|/2 + C_4 r D(r), and for C_4 r ≤
1/2

    |h_1′(r) − h_2′(r)| ≤ C_4 r |Δz|,      |h_1(r) − h_2(r) − Δz| ≤ C_4 r² |Δz|/2.

*Step 5 (Foliation).* Put r_1 := min(r_0, 1/(2C_4), 1/(2C_0)), so that r_1 ≤ r_*/8 and C_4 r_1² ≤ 1. For |z0 − z(p)| ≤
r_1 the leaf is defined on [0, r_1] with |h′| ≤ C_0 r, and Step 4 gives [[eq:class-leaf-quotient]] with C := C_4.
For |y| = r ≤ r_1 the map z0 ↦ h(r; z0) on [z(p) − r_1, z(p) + r_1] is continuous and strictly increasing, and |h(r;
z0) − z0| ≤ C_0 r²/2 ≤ r_1/4; so its image contains [z(p) − 3r_1/4, z(p) + 3r_1/4], and every point x of 𝒰_(r_1/2) lies
on exactly one leaf, with |z0[U](x) − z(p)| ≤ 3r_1/4. For t ≤ r_x the point of the arc of x at radius t has |h(t; z0) −
z(x)| ≤ C_0 (r_x² − t²)/2 ≤ r_x/4, so the arc of a point of 𝒰_δ lies in 𝒰_(5δ/4) ⊂ 𝒰_(2δ).

*Step 6 (The shear on a leaf).* Let x̄ = (h(r), (r, 0)), r > 0, be a point of a leaf of U and s := h′(r)/r. The graph
has mean curvature H_L[U] at x̄: by the definition of E_L in [[lem:class-leaf]] (c), (r h′)′ = r H_L[U]/a_L − E_L says
exactly that. So k_r = H_L[U] − k_φ, with k_φ = ν^r/r + ½ ν(log γ_22) and ν^r/r = −(C3 + γ_zz s)/(det₂^(1/2) N_L) by
[[lem:class-leaf]] (c), e_r = (∂_(y1) + q ∂_z)/N_L with q = r s, and e2 = ∂_(y2)/γ_22^(1/2). Hence

    σ[U](x̄) = 𝔖(x̄, W_U(x̄), s),                                                                {#eq:class-leaf-shear-s}

with 𝔖 a smooth function, the same for all states, on the set of Step 1 times {|s| ≤ C_0}: every quantity entering is a
smooth function of s, of the point and of the components of W there, C3 by Step 2. Since r⁻² ∫_0^r G dρ = h′(r)/r and
G(ρ, h, h′)/ρ is continuous by [[eq:class-leaf-g]], s has a limit at r = 0, |s| ≤ C_0, and [[eq:class-leaf-shear-s]]
holds there by continuity. So |σ[U]| ≤ C on 𝒰_(r_1/2); |∂_s 𝔖| ≤ C; along each line {y = const} the function x̄ ↦ 𝔖(x̄,
W_U(x̄), s) is Lipschitz with constant C, W_U being of class C¹; and |𝔖(x̄, W_U(x̄), s) − 𝔖(x̄, W_(U′)(x̄), s)| ≤ C |U
− U′|(x̄).

*Step 7 (Smoothness).* Let U be smooth. The components at (z, (r, 0)), r ∈ (−r_2, r_2), are smooth in (z, r), and G(−r,
z, −q) = −G(r, z, q), by the parities of [[lem:class-leaf]] (c). So 𝔤(r, z, s) := G(r, z, r s)/r, which by
[[eq:class-leaf-g]] is the first bracket there at q = r s minus r² s (C3 + γ_zz s)²/det₂, is smooth and even in r. With
h′ = r s the leaf equation reads, on [−r_1, r_1], the leaf being even,

    s(r) = ∫_0^1 t 𝔤(r t, h(r t), s(r t)) dt,      h(r) = z0 + ∫_0^r ρ s(ρ) dρ.                        {#eq:class-leaf-s}

Its right side defines a map 𝒦 of {s ∈ C([−r_1, r_1]) : sup |s| ≤ C_0} into itself, smooth in s, in z0 and in the
parameters on which U depends smoothly, and a contraction with constant at most 1/2, since |∂_s 𝔤| = |∂_q G| ≤ C_2 (1 +
C_0) |r|, |∂_z 𝔤| ≤ C_1 (1 + C_0) and the values of h for two functions s differ by at most r² sup |Δs|/2.
Differentiating [[eq:class-leaf-s]] j times in r, the j-th derivative of 𝒦s is ∫_0^1 t^(1+j) (∂_s 𝔤 · s^(j) + R_j)(r t)
dt, with R_j a polynomial in the derivatives of s of order below j and in derivatives of 𝔤 and of h; so 𝒦 maps {Σ_(i≤j)
sup |s^(i)| ≤ K_j} into itself for K_j large, its iterates are bounded there and converge uniformly to s, and s ∈
C^(j−1) for every j, by the theorem of Arzelà and Ascoli. The implicit function theorem in C([−r_1, r_1]) makes s
smooth in z0 and in the parameters; its derivatives in them solve linear equations of the form [[eq:class-leaf-s]], and
the same argument makes them smooth in r. s is even, s(−·) solving the same equation. So the graph z0 + |y|² ∫_0^1 θ
s(θ |y|) dθ is smooth in y: by Taylor's formula s(r) = Σ_(i<N) a_i r^(2i) + r^(2N) R_N(r) with R_N smooth and even, and
y ↦ |y|^(2N) R_N(|y|) is of class C^N. By [[eq:class-leaf-quotient]], ∂_(z0) h ∈ [1/2, 3/2], and the implicit function
theorem makes z0[U] smooth.

(a) is Steps 3–7.

(b) Let x ∈ 𝒰_(r_1/2); by invariance we may take x = (h_U(r; z0), (r, 0)) with r := r_x and z0 := z0[U](x). Let ĥ :=
h_U(·; z0) and h̃ := h_(U′)(·; z0), the leaf of U′ from the same axis point, δh := ĥ − h̃, δq := ĥ′ − h̃′, D(r) :=
sup_[0,r] |δq|, ŝ := ĥ′(r)/r, s̃ := h̃′(r)/r and x′ := (h̃(r), (r, 0)). By Step 6,

    σ[U](x) − σ[U′](x) = (𝔖(x, W_U, ŝ) − 𝔖(x, W_(U′), ŝ)) + (𝔖(x, W_(U′), ŝ) − 𝔖(x, W_(U′), s̃))
                        + (𝔖(x, W_(U′), s̃) − 𝔖(x′, W_(U′), s̃)) + (σ[U′](x′) − σ[U′](x)),

each W at the point written first, and the first three terms are at most C f(r), C |δq(r)|/r and C |δh(r)|. The point x
lies on the leaf of U′ with axis point ζ := z0[U′](x), and |ζ − z0| ≤ 2 |δh(r)| by [[eq:class-leaf-quotient]] for U′;
along the line {y = (r, 0)} the function ζ′ ↦ σ[U′](h_(U′)(r; ζ′), (r, 0)) = 𝔖(·, W_(U′), h_(U′)′(r; ζ′)/r) is
Lipschitz with constant C, by Step 6 and [[eq:class-leaf-quotient]]; so the fourth term is at most C |δh(r)|.
Subtracting the Volterra equations of the two leaves,

    r δq(r) = ∫_0^r ((G_U − G_(U′))(ρ, ĥ, ĥ′) + G_(U′)(ρ, ĥ, ĥ′) − G_(U′)(ρ, h̃, h̃′)) dρ.

By Step 2 the first difference is at most C ρ f(ρ), as |ĥ′| ≤ C_0 ρ, and as in Step 4 the second is at most C_4 ρ
(|δh| + |δq|), with |δh(ρ)| ≤ ρ D(ρ) since δh(0) = 0. So |δq(r)| ≤ C_4 r D(r) + C r⁻¹ ∫_0^r ρ f(ρ) dρ; with r⁻¹ ∫_0^r ρ
f dρ ≤ (∫_0^r ρ f² dρ)^(1/2)/√2, by the Cauchy–Schwarz inequality, and C_4 r ≤ 1/2,

    D(r) ≤ C (∫_0^r t f(t)² dt)^(1/2),      |δh(r)| ≤ r D(r),      |δq(r)|/r ≤ C_4 D(r) + C r⁻² ∫_0^r t f(t) dt,

which with r ≤ 1 give [[eq:class-leaf-pointwise]].

(c) For a G-invariant function F ≥ 0 on 𝒰_ρ, ρ ≤ ρ1(p)/4, ∫_(Σ∩𝒰_ρ) F = 2π ∫ F(z, y) z dz dy over 𝒰_ρ ∩ M3, the flat
measure of ℝ⁴ being ρ1 dρ1 dφ1 dy, with z = ρ1 ∈ [3ρ1(p)/4, 5ρ1(p)/4]. For fixed y the map z0 ↦ h_U(|y|; z0) is
increasing with difference quotients in [1/2, 3/2], hence absolutely continuous with derivative in [1/2, 3/2] almost
everywhere, and ∫ F(z, y) dz = ∫ F(h_U(|y|; z0), y) ∂_(z0) h_U dz0. For |z0 − z(p)| ≤ 3r_1/4 let Y(z0) be the set of y
with (h_U(|y|; z0), y) ∈ D ∩ 𝒰_δ, R(z0) the supremum of |y| over Y(z0) (0 if Y(z0) is empty), and f_(z0)(t) := |U − U′|
at (h_U(t; z0), (t, 0)). If y ∈ Y(z0), the arc of U through that point lies in D, by hypothesis, and in 𝒰_(2δ), by (a);
by G-invariance, every point (h_U(|y′|; z0), y′) with |y′| < R(z0) lies in D ∩ 𝒰_(2δ). The arc of U through (h_U(|y|;
z0), y) is that leaf over [0, |y|], so [[eq:class-leaf-pointwise]] gives

    ∫_(Y(z0)) |σ[U] − σ[U′]|²(h_U(|y|; z0), y) dy
        ≤ C ∫_(𝔻_(R(z0))) (f_(z0)² + (𝒜f_(z0))² + ∫_0^(|y|) t f_(z0)(t)² dt) dy,

with f_(z0) and 𝒜f(r) := r⁻² ∫_0^r t f dt = ∫_0^1 s f(s r) ds read at |y|. As ‖f(s ·)‖_(L²(𝔻_R)) ≤ s⁻¹ ‖f‖_(L²(𝔻_R))
for radial f, Minkowski's inequality gives ‖𝒜f‖_(L²(𝔻_R)) ≤ ‖f‖_(L²(𝔻_R)), as in [[prop:class-flat-model]] (b), and the
last term is at most (R²/2) ‖f‖²_(L²(𝔻_R)) ≤ ‖f‖²_(L²(𝔻_R)). So the right side is at most C ∫_(𝔻_(R(z0))) f_(z0)(|y|)²
dy, an integral over points of D ∩ 𝒰_(2δ). Every point of D ∩ 𝒰_δ is (h_U(|y|; z0), y) with y ∈ Y(z0) and |z0 − z(p)| ≤
δ + C_0 δ²/2 ≤ 3r_1/4. Integrating over z0 and changing variables on both sides, with the Jacobian ∂_(z0) h_U ∈ [1/2,
3/2] and the weights 2π z, gives [[eq:class-leaf-sets]]. ∎

**Lemma {#lem:class-leaf-differences}** (The planar shear of nearby solutions.) Let ů be a smooth state on a
neighbourhood of the closure of 𝒰, for instance a smooth class solution with ∂_z ů_A ≠ 0 on the axis, p_A := dů_A and
Θ_A := □ů_A; its leaves h̊ and its planar shear σ[ů] are those defined before [[lem:class-leaf-states]], as are the
leaves and the planar shear of every state U. For a state U on Σ and m ≥ 0 let

    𝒩_m(U) := Σ_(j≤m) ‖∂^j (W_U − W_ů)‖_(L²(Σ∩𝒰)),

∂^j all derivatives of order j in x; for a family U(τ) of states on the slices Σ_τ of an interval, for instance a
solution, let 𝒩_m(U)(τ) be the same expression on Σ_τ with ∂^j all spacetime derivatives of order j. When ů and U are
solutions, 𝒩_m is at most twice [[eq:class-energy]]. Let k ≥ 6. There are δ_0 > 0, a ball 𝔅 around ů in the norm 𝒩_k
and a ball 𝔅′ ⊃ 𝔅 around ů in the norm 𝒩_(k−1), and for every δ ∈ (0, δ_0] a number C, such that the states of 𝔅′ have
bounds (M, c) for which 4δ_0 ≤ r_1, r_1 of [[lem:class-leaf-states]], and for 0 < δ ≤ δ_0:

(a) ‖∂^α(σ[U]² − σ[ů]²)‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U) for |α| ≤ k, both for a state U ∈ 𝔅, ∂^α the derivatives in x, and for a
family of states in 𝔅, ∂^α the spacetime derivatives and 𝒩_k(U) taken at the time considered; and for m > k and a state
U ∈ 𝔅 with 𝒩_m(U) < ∞, ‖σ[U]² − σ[ů]²‖_(H^m(𝒰_δ)) ≤ C_m 𝒩_m(U), C_m depending also on m and on an upper bound for
𝒩_(m−1)(U);
(b) ‖σ[U] − σ[U′]‖_(L²(𝒰_δ)) ≤ C ‖U − U′‖_(L²(𝒰_(2δ))) and |σ[U]| ≤ C on 𝒰_δ, for U, U′ ∈ 𝔅′;
(c) for U ∈ 𝔅, δh(z0, y) := h_U(|y|; z0) − h̊(|y|; z0), the difference of the leaves through one axis point, and I :=
[z(p) − δ, z(p) + δ], Σ_(j≤2) ‖∂_(z0)^j δh‖_(L²(I; H^(k+2−j)(𝔻_δ))) ≤ C 𝒩_k(U); and for a family of states in 𝔅, every
derivative of δh in (τ, z0, y) of order at most k − 2 is bounded on I × 𝔻_δ by C 𝒩_k(U).

C depends only on k, δ, ρ1(p), r_*, the bounds of ů and a bound for the derivatives of order at most k + 2 of the
components of W_ů (of order at most m + 2 for C_m), and in (b) only on (M, c), ρ1(p) and r_*. The planar shear enters
[[eq:class-x]], and the closure of the Raychaudhuri equation at an axis, through σ². For a solution of the class system
with p_A = du_A and Θ_A = □_g u_A the leaves are the level sets of u_A near the axis, and σ[U] is the planar shear
[[eq:class-shear-leaf]] of those level sets.

*Proof.* Constants C depend only on the quantities named in the statement, and C_m also on m and on an upper bound for
𝒩_(m−1)(U).

*The balls.* As ů is smooth up to the closure of 𝒰, with p_A(∂_z) ≠ 0 on the axis, it has bounds (M_0, 2c_0) for some
M_0 and c_0. On the Lipschitz domain Σ ∩ 𝒰, Sobolev's embedding ([[thm:std-bh-embedding]], 3 · 2 > 4) gives sup |f| ≤ C
Σ_(j≤3) ‖∂^j f‖; applied to the derivatives of W_U − W_ů, spacetime ones for a family,

    sup_(Σ∩𝒰) |∂^i (W_U − W_ů)| ≤ C 𝒩_(i+3)(U).                                                      {#eq:class-leaf-sup}

So there is r′ > 0 such that every state with 𝒩_4(U) ≤ r′ has bounds (M, c) := (2M_0, c_0): the C¹ norms of the
components of its W_U differ from those of ů by at most C r′, and so do the quantities bounded below in the definition
of bounds. Let 𝔅′ := {𝒩_(k−1) ≤ r′}, as k − 1 ≥ 4; let r_1 and C_0, …, C_4 be the numbers of [[lem:class-leaf-states]]
and its proof for (M, c), δ_0 := min(r_1/4, 1/(9C_0), δ_1) with δ_1 > 0 fixed in Step 5 below, depending only on (M, c)
and ů, and 𝔅 := {𝒩_k ≤ r″}, with r″ ∈ (0, r′/2] fixed in Steps 4 and 6 below; let 0 < δ ≤ δ_0.

*(b)* is [[lem:class-leaf-states]] (c) with D := Σ, as 2δ ≤ r_1/2, together with its part (a).

*The last statement.* Let g⁻¹(du_A, du_A) = 0, p_A = du_A, Θ_A = □_g u_A and ∂_z u_A ≠ 0 near the axis. By
[[lem:class-leaf]] (b) the level set of u_A through an axis point (z0, 0) is, near it, an invariant smooth graph z =
h(y) with h(0) = z0, and du_A = ∂_z u_A dF along it, F := z − h(y); so |∇_M3 u_A| = |p_A^Σ|, ν_L = εν, and Π is its
tangent plane TΣ_L. By [[lem:class-gauss]] (b), tr χ̸ = |∇_M3 u_A| tr k_L − n(u_A) tr K_Σ|_(TΣ_L) = Θ_A − κ_A1, k_L
taken for ν_L; so its mean curvature for ν is H_L[U], as in step (1) of the proof of [[lem:class-planar-shear]]. By
[[lem:class-leaf]] (c), h′(0) = 0 and (r h′)′ = r H_L[U]/a_L − E_L for r > 0; integrating from 0 gives
[[eq:class-leaf-volterra]], and h is the leaf of U through z0, by the uniqueness in [[lem:class-volterra]]. Then k_r,
k_φ, e_r and e2 are those of the level set, and σ[U] is [[eq:class-shear-leaf]] for it.

*(a) and (c).* *Step 1 (Smooth states suffice).* It suffices to prove (a) and (c) for smooth states, or smooth
families, with 𝒩_k(U) ≤ 2r″, with constants that do not depend on their smoothness. Indeed, for U ∈ 𝔅 let U_n be
obtained by extending the components of g, ∂_τ g, p_A and Θ_A from Σ ∩ 𝒰 by Stein's operator
([[thm:std-sy-extension]]), mollifying, averaging over G, which acts by isometries of ℝ⁴, and restricting; for a
family, likewise in (τ, x). Then Σ_(j≤m) ‖∂^j (W_(U_n) − W_U)‖ → 0 for every m with 𝒩_m(U) < ∞, so 𝒩_k(U_n) ≤ 2r″ for n
large. By (b), σ[U_n] → σ[U] in L²(𝒰_δ), and these functions are bounded by C, so σ[U_n]² → σ[U]² in L²(𝒰_δ); a
sequence bounded in H^m and convergent in L² has its limit in H^m, with the same bound. For (c), the proof of
[[lem:class-leaf-states]] (b) gives sup |h_(U_n) − h_U| ≤ C sup |U_n − U| → 0 on the leaves, and the bounds pass to the
limit in the same way. From now on U is smooth, or a smooth family, with 𝒩_k(U) ≤ 2r″.

*Step 2 (Leaf coordinates and norms).* Let Q_ρ := 𝒰_ρ ∩ M3 in the coordinates (z, y), Q̂ := {(z0, y) : |z0 − z(p)| <
3δ, |y| < 3δ}, and, for X ∈ {U, ů}, Λ_X(z0, y) := (h_X(|y|; z0), y), which is smooth, injective on Q̂ and has Jacobian
∂_(z0) h_X ∈ [1/2, 3/2] ([[lem:class-leaf-states]] (a)). As |h_X − z0| ≤ C_0 (3δ)²/2 ≤ δ/2, Λ_X(Q̂) ⊂ Q_(4δ), and Λ_X
maps {|z0 − z(p)| < 3δ, |y| < ρ} onto a set containing Q_δ for ρ ≥ δ. For a G-invariant function f on 𝒰_ρ, ρ ≤ 4δ, the
H^m norms of f on Σ ∩ 𝒰_ρ and of f(z, y) on Q_ρ agree up to factors depending only on m and ρ1(p): the volume elements
differ by the factor 2π z of the proof of [[lem:class-leaf-states]] (c), and ∂_(x_i) f = (x_i/ρ1) ∂_z f for i = 1, 2
and ∂_z f = Σ_(i≤2) (x_i/ρ1) ∂_(x_i) f, the functions x_i/ρ1 having bounded derivatives of every order where ρ1 ≥
ρ1(p)/2. Below, D denotes the derivatives in (z0, y), or in (z, y), and, for a family, also in τ; T denotes ∂_(z0) and,
for a family, also ∂_τ; all norms are taken at the time considered, and a norm without index on Q̂, on Q_(4δ) or on a
subset is that of L², ‖f‖_n := Σ_(|α|≤n) ‖D^α f‖. Put ω := W_U − W_ů and ω_g := g_U − g_ů on Q_(4δ), and Ω_n := ‖ω‖_n +
‖ω_g‖_(n+1) on Q_(4δ); then Ω_n ≤ C 𝒩_n(U), the first derivatives of g being components of W.

*Step 3 (The divergence form).* Let X ∈ {U, ů}. For a C¹ G-invariant function h on a disc of the y-plane put F := z −
h(y), let ν be the unit normal γ3⁻¹dF/|dF| of the graphs z = h(y) + const, a field near the graph that depends on (z,
y) and on ∂h(y), let √γ := (det γ3)^(1/2) in the coordinates (z, y), and 𝔙(y, z, P; w) := √γ ν^y at (z, y), with ∂h
replaced by P ∈ ℝ², ν^y := (ν^(y1), ν^(y2)) and w the value of g_X there. The mean curvature of a C² graph at its
points is (√γ)⁻¹ ∂_a(√γ ν^a), and along the graph ∂_(y_i)[𝔙^i(y, h, ∂h)] = (∂_i(√γ ν^i) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)),
∂_z at fixed ∂h. So the graph has mean curvature H_L[X] at its points exactly when

    div_y 𝔙(y, h, ∂h) = Φ_X(y, h, ∂h),
    Φ_X := (√γ H_L[X] − ∂_z(√γ ν^z) + ∂_z(√γ ν^i) ∂_i h)|_(z=h(y)),                           {#eq:class-leaf-divergence}

Φ_X a smooth function of (y, h, ∂h) and of W_X at (h(y), y). The leaf h_X(·; z0) satisfies [[eq:class-leaf-divergence]]
off the axis (Step 6 of the proof of [[lem:class-leaf-states]]), and 𝔙(y, h_X, ∂h_X) is an invariant vector field,
v(|y|) y, with (r² v)′ = r div(v y) = r Φ_X for r > 0 and r² v → 0; so

    𝔙(y, h_X, ∂h_X) = y 𝔰_X,      𝔰_X(y) := ∫_0^1 t Φ_X(t y) dt.                                  {#eq:class-leaf-radial}

By [[lem:class-leaf]] (b), ∂_P 𝔙 = −√γ |dF|⁻¹ (γ3^(ij) − ν^i ν^j)_(i,j) is negative definite, with eigenvalues in
[−Λ_1, −1/Λ_1] for |P| ≤ 1, Λ_1 depending only on M; so P ↦ 𝔙(y, z, P; w) is injective on {|P| ≤ 1}, its inverse 𝔓(y,
z, ·; w) is smooth on the image, and

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
[[eq:class-leaf-s]] once or twice in r, z0 and, for a family, τ, each derivative of s_X solves a linear equation whose
map has norm at most 1/2, as in that Step 7, and whose inhomogeneous term holds derivatives of order at most 2 of W_X
and derivatives of s_X and h_X of lower order; with [[eq:class-leaf-sup]] at i ≤ 2, so 𝒩_5 ≤ 𝒩_k, the derivatives of
order at most 2 of s_X, of h_X = z0 + |y|² ∫_0^1 θ s_X(θ |y|) dθ, of ∂_y h_X = s_X y, of W_X ∘ Λ_X, of g_X ∘ Λ_X and of
𝔰_X = ∫_0^1 t Φ_X(t ·) dt are bounded on Q̂ by C. The same equations for the differences η := h_U − h_ů, δs := s_U −
s_ů, with the terms in ω ∘ Λ_U as inhomogeneous terms, bound the derivatives of order at most 2 of η, ∂_y η, δs, δ𝔰 :=
𝔰_U − 𝔰_ů, ω ∘ Λ_U and ω_g ∘ Λ_U on Q̂ by C 𝒩_k(U). We fix r″ so small that these bounds are at most 1.

*Product and composition rules.* (P) The terms estimated below at an order n, n ≤ k + 1, or n ≤ m + 1 in the second
part of (a), are sums of products of a bounded smooth function with derivatives of factors among h_X, ∂_y h_X, s_X,
𝔰_X, y 𝔰_X, W_X ∘ Λ_X, g_X ∘ Λ_X, ∂_y² h_X and their differences, in which the numbers of derivatives add to at most n.
Every factor but the one carrying the most derivatives carries a ≤ n/2 of them. If a ≤ 1, it is bounded by Step 4. If
two factors carry two derivatives each and n = 4, Hölder's inequality and H¹(Q̂) ⊂ L⁴ ([[thm:std-bh17-embedding]])
bound their product by norms of order 3. Otherwise a ≤ n − 3, and the factor is bounded pointwise by Sobolev's
embedding H²(Q̂) ⊂ L^∞ ([[thm:std-bh-embedding]], 2 · 2 > 3) and its norm of order a + 2, below the order of the term
and bounded before, or, for a derivative of ω or ω_g, by [[eq:class-leaf-sup]], with 𝒩_(a+3) ≤ 𝒩_k for n ≤ k + 1, k ≥
6, and 𝒩_(a+3) ≤ 𝒩_(m−1) for n ≤ m + 1, m ≥ 7. So the L² norm of such a product is at most C, or C_m, times the L² norm
of its factor of highest order, or the norms of order below n just named. (Q) For F on Q_(4δ) and |α| ≤ n, D^α(F ∘ Λ_U)
is a sum of products of (D^β F) ∘ Λ_U, |β| ≥ 1, with factors D^(α_i) Λ_U, |α_i| ≥ 1, Σ |α_i| = |α|; counting D^(α_i)
Λ_U as a derivative of order |α_i| − 1 of DΛ_U, the orders add to |α|. (P) applies, and the change of variables Λ_U,
with Jacobian at least 1/2, gives ‖(D^β F) ∘ Λ_U‖ ≤ √2 ‖D^β F‖ on Q_(4δ). With F := ω, and F := ω_g at the order n + 1,
the term in which all of D^α falls on h_U being multiplied by sup |Dω| ≤ C 𝒩_k(U),

    ‖ω ∘ Λ_U‖_n + ‖ω_g ∘ Λ_U‖_(n+1) ≤ C (Ω_n + 𝒩_k(U) (‖η‖_n + ‖∂_y η‖_n)).                      {#eq:class-leaf-compose}

The same holds with Λ_U⁻¹ in place of Λ_U, for functions on Q̂: DΛ_U⁻¹ = B ∘ Λ_U⁻¹ with B a smooth function of Dh_U,
∂_(z0) h_U ≥ 1/2, so the derivatives of Λ_U⁻¹ are polynomials in the derivatives of h_U composed with Λ_U⁻¹, and the
Jacobian of Λ_U⁻¹ lies in [2/3, 2].

*Step 5 (Transverse derivatives).* For X ∈ {U, ů}, 𝔤̂(r t, s_U, W_U(h_U, ·)) − 𝔤̂(r t, s_ů, W_ů(h_ů, ·)) = a_1 · (ω ∘
Λ_U) + a_2 δs + a_3 η at the point (r t, 0) of the leaves, with a_1, a_2, a_3 smooth functions of r t, s_U, s_ů, W_U ∘
Λ_U, W_ů ∘ Λ_U and W_ů ∘ Λ_ů, the last difference being (∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ) η; and |a_2| = |∂_s 𝔤̂| ≤ C_2
(1 + C_0) r t and |a_3| ≤ C. Let j ≤ k, or j ≤ m. Applying T^j to the difference of the equations [[eq:class-leaf-s]],

    T^j δs(r) = ∫_0^1 t (a_2 T^j δs + a_3 T^j η + a_1 · T^j(ω ∘ Λ_U) + R_j)(r t) dt,
    T^j η(r) = r² ∫_0^1 θ T^j δs(θ r) dθ,

R_j the terms of Leibniz's rule in which δs, η or ω ∘ Λ_U carries fewer than j derivatives. As ‖F(t ·)‖_(L²(𝔻_ρ)) ≤ t⁻¹
‖F‖_(L²(𝔻_ρ)), Minkowski's inequality bounds the operators F ↦ ∫_0^1 t F(t ·) dt and F ↦ |y|² ∫_0^1 θ F(θ ·) dθ on
L²(𝔻_ρ), ρ ≤ 3δ, by 1 and by 9δ², on each disc of fixed (τ, z0), as in the proof of [[lem:class-leaf-states]] (c). So
‖T^j η‖ ≤ 9δ² ‖T^j δs‖ and ‖T^j δs‖ ≤ (3C_2 (1 + C_0) δ + 9C δ²) ‖T^j δs‖ + C ‖T^j(ω ∘ Λ_U)‖ + ‖R_j‖ on Q̂. Fix δ_1
with 3C_2 (1 + C_0) δ_1 + 9C δ_1² ≤ 1/2. By (P), and by induction on j, ‖R_j‖ ≤ C (Ω_j + 𝒩_k(U)) for j ≤ k, the factors
of R_j other than δs, η and ω ∘ Λ_U being bounded in the norms of order j by Step 4 and (Q), and ‖R_j‖ ≤ C_m (Ω_j +
𝒩_k(U)) for k < j ≤ m. By (Q), ‖T^j(ω ∘ Λ_U)‖ ≤ C (Ω_j + 𝒩_k(U) ‖T^j η‖) plus terms bounded by (P) and the derivatives
of η of order below j. With ∂_y η = δs y and Ω_j ≤ C 𝒩_j(U), induction on j gives, on Q̂,

    ‖T^j δs‖ + ‖T^j η‖ + ‖T^j ∂_y η‖ ≤ C 𝒩_k(U) for j ≤ k,      ≤ C_m 𝒩_m(U) for k < j ≤ m.   {#eq:class-leaf-transverse}

*Step 6 (Derivatives along the disc).* Let ρ_n := (3/2 + 3 · 2^(−n−2)) δ and Q̂_n := {|z0 − z(p)| < 3δ, |y| < ρ_n}, and
for functions on Q̂_n let ‖f‖_(j,n) be the L² norm in z0 of the H^(n+2−j) norm in y on 𝔻_(ρ_n). We show, by induction
on n, for n ≤ k, and for n ≤ m in the second part of (a),

    Σ_(j≤n) ‖T^j η‖_(j,n) ≤ C 𝒩_k(U) for n ≤ k,      Σ_(j≤n) ‖T^j η‖_(j,n) ≤ C_m 𝒩_m(U) for k < n ≤ m,
                                                                                                {#eq:class-leaf-elliptic}

T^j any product of j transverse derivatives; for n − 1 it holds by induction (it is empty for n = 0), and with Step 5
it bounds all norms of order below n + 2 of η, ∂_y η, δs, δ𝔰 and of order below n + 1 of ω ∘ Λ_U that (P) uses. We
write the bound for n ≤ k; for n > k the same lines give C_m 𝒩_m(U).

(i) δΦ := Φ_U(y, h_U, ∂_y h_U; W_U ∘ Λ_U) − Φ_ů(y, h_ů, ∂_y h_ů; W_ů ∘ Λ_ů) is a smooth function of these arguments
times (η, ∂_y η, ω ∘ Λ_U, W_ů ∘ Λ_U − W_ů ∘ Λ_ů), the last being (∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ) η. For j + |β| ≤ n,
T^j ∂_y^β δΦ is a sum of terms linear in T^j ∂_y^β of η, ∂_y η and ω ∘ Λ_U, with bounded coefficients, and of products
of lower order covered by (P). The derivatives T^j ∂_y^β ∂_y η, n + 1 derivatives of η, are bounded by
[[eq:class-leaf-elliptic]] at n − 1 for j ≤ n − 1 and by [[eq:class-leaf-transverse]] for j = n; those of η by both;
those of ω ∘ Λ_U by [[eq:class-leaf-compose]]. So Σ_(j+|β|≤n) ‖T^j ∂_y^β δΦ‖ ≤ C 𝒩_k(U) on Q̂_(n−1), Q̂_(−1) := Q̂.

(ii) Put u_X(y) := |y|² ∫_0^1 t 𝔰_X(t y) dt, a radial function with ∇_y u_X = y 𝔰_X and, by [[eq:class-leaf-radial]],
Δ_y u_X = div_y(y 𝔰_X) = Φ_X. So δu := u_U − u_ů satisfies Δ_y T^j δu = T^j δΦ on each disc of fixed (τ, z0). By
[[lem:class-interior-regularity]] with L := Δ_y, c_a = 1 and j := n − j, whose proof applies to any two concentric
discs, here 𝔻_(ρ_n) ⊂ 𝔻_(ρ_(n−1)), with C depending also on their radii,

    ‖T^j δu‖_(H^(n−j+2)(𝔻_(ρ_n))) ≤ C (‖T^j δΦ‖_(H^(n−j)(𝔻_(ρ_(n−1)))) + ‖T^j δu‖_(L²(𝔻_(ρ_(n−1))))),

and the last norm is at most 9δ² ‖T^j δΦ‖_(L²(𝔻_(ρ_(n−1)))), by the operator bounds of Step 5 applied to δ𝔰 = ∫_0^1 t
δΦ(t ·) dt and to δu. Squaring, integrating over z0 and using (i), Σ_(j≤n) ‖T^j ∇_y δu‖_(L²(H^(n+1−j))) ≤ C 𝒩_k(U) on
Q̂_n.

(iii) By [[eq:class-leaf-inverse]], ∂_y η = 𝔓(y, h_U, ∇_y u_U; g_U ∘ Λ_U) − 𝔓(y, h_ů, ∇_y u_ů; g_ů ∘ Λ_ů), a smooth
function of these arguments times (η, ∇_y δu, ω_g ∘ Λ_U, g_ů ∘ Λ_U − g_ů ∘ Λ_ů). For j ≤ n and |β| ≤ n + 1 − j, T^j
∂_y^β ∂_y η is a sum of terms linear in T^j ∂_y^β of η, ∇_y δu and ω_g ∘ Λ_U, with bounded coefficients, and of
products covered by (P), with n + 1 derivatives in all. The derivatives of ∇_y δu are bounded by (ii); those of η,
which carry |β| ≥ 1 derivatives in y as j ≤ n, by [[eq:class-leaf-elliptic]] at n − 1 for j ≤ n − 1 and by
[[eq:class-leaf-transverse]] for j = n; and those of ω_g ∘ Λ_U by [[eq:class-leaf-compose]], whose term in ∂_y η of
order n + 1 carries the factor C 𝒩_k(U) ≤ 2C r″ and is absorbed for r″ small. So Σ_(j≤n) ‖T^j ∂_y η‖_(L²(H^(n+1−j))) ≤
C 𝒩_k(U) on Q̂_n, which with [[eq:class-leaf-transverse]] for ‖T^j η‖ is [[eq:class-leaf-elliptic]] at n.

*Step 7 (Conclusion).* By [[eq:class-leaf-square]], S := σ[U]² ∘ Λ_U − σ[ů]² ∘ Λ_ů is a smooth function times (η, ∂_y
η, ∂_y² η, ω ∘ Λ_U, W_ů ∘ Λ_U − W_ů ∘ Λ_ů). Its derivatives of order at most k are bounded in L²(Q̂_k) by (P),
[[eq:class-leaf-elliptic]] at n = k, which bounds T^j ∂_y^β ∂_y² η for j + |β| ≤ k, and [[eq:class-leaf-compose]]:
‖S‖_k ≤ C 𝒩_k(U) on Q̂_k, and likewise ‖S‖_m ≤ C_m 𝒩_m(U) on Q̂_m. Write S̊ := σ[ů]² ∘ Λ_ů, a smooth function on Q̂.
Then σ[U]² − σ[ů]² = S ∘ Λ_U⁻¹ + S̊ ∘ Λ_U⁻¹ − S̊ ∘ Λ_ů⁻¹, and as h_U(|y|; z0[U]) = z, Λ_ů ∘ Λ_U⁻¹(z, y) = (z −
η(Λ_U⁻¹(z, y)), y), so that

    S̊ ∘ Λ_U⁻¹ − S̊ ∘ Λ_ů⁻¹ = −(∫_0^1 ∂_z(S̊ ∘ Λ_ů⁻¹)(z − θ η ∘ Λ_U⁻¹, y) dθ) η ∘ Λ_U⁻¹.

Λ_U maps Q̂_k onto a set containing Q_δ (Step 2, ρ_k > δ), and (Q) for Λ_U⁻¹, with (P), gives ‖σ[U]² −
σ[ů]²‖_(H^k(Q_δ)) ≤ C (‖S‖_k + ‖η‖_k) ≤ C 𝒩_k(U), and at the order m the bound C_m 𝒩_m(U). By Step 2 these are the
bounds of (a) on 𝒰_δ, with the derivatives in x for a state and the spacetime derivatives for a family. For (c),
[[eq:class-leaf-elliptic]] at n = k with j ≤ 2, restricted to I × 𝔻_δ ⊂ Q̂_k, is the first bound; for a family it
bounds every derivative of η of order at most k in (τ, z0, y) in L²(Q̂_k), and Sobolev's embedding H²(Q̂_k) ⊂ L^∞ gives
the second. ∎

### Placement

Each item names the place, the old text and the new text. Old texts are the lines of the chapter sources at the current
head, each occurring there exactly once as whole lines; line numbers serve only to find the place.

*1. [[ch:class-system]], [[sec:class-planar-shear]]: [[lem:class-leaf-differences]], its statement and its proof
(lines 1324–1357).* The new text is the text of the Block above, from "Let Σ be a slice {τ = const}" to the end of the
proof of [[lem:class-leaf-differences]] ("… gives the second. ∎"), with one blank line between paragraphs as there. It
contains the definitions that the old statement gave in its first sentences, Tier 3's reading of H_L[Θ_A] (p_A(n) and
the plane fixed by p_A) included. Old:

**Lemma {#lem:class-leaf-differences}** (The planar shear of nearby solutions.) Let ů be a smooth class solution and,
near a point of axis 2, let h̊ be the leaves of ů_A. For U = (g, p_A, Θ_A, q_A) on a slice let the leaves of family A
be the graphs z = h(r) through the points of the axis near that point, each solving [[eq:class-leaf-volterra]] with
H_L := H_L[Θ_A], the formula of step (1) of [[lem:class-planar-shear]] with Θ_A in place of Θ, the spatial part p_A^Σ
of p_A in place of ∇_Σ u, p_A(n) in place of n(u), the sign that of p_A(∂_z), and the trace of K_Σ taken over the
γ3-orthogonal complement of p_A^Σ in TM3 in place of TΣ_L. That plane is fixed by p_A at each point, so H_L[Θ_A] is a
function of the point, as [[lem:class-volterra]] requires; when p_A is the differential of a phase it is the tangent
plane of the level set of the phase through the point, and H_L[Θ_A] is the formula of step (1) for that level set. The
leaves exist and are unique by [[lem:class-volterra]], and for U near ů they are C¹-close to the leaves of ů and
foliate a neighbourhood of the axis. Let σ[U] at a point be the planar shear [[eq:class-shear-leaf]] of
the leaf through it. Let k ≥ 6. There are a ball 𝔅 around ů in the norm 𝒩_k, a ball 𝔅′ ⊃ 𝔅 around ů in the norm
𝒩_(k−1), and C, such that:

(a) ‖∂^α(σ[U] − σ[ů])‖_(L²(𝒰_δ)) ≤ C 𝒩_k(U) for |α| ≤ k and U ∈ 𝔅;
(b) ‖σ[U] − σ[U′]‖_(L²(𝒰_δ)) ≤ C ‖U − U′‖_(L²(𝒰_(2δ))) for U, U′ ∈ 𝔅′, where U includes ∂g among its components.

The constants use C¹ norms of the phases and sup |Θ_A|, not C² norms of the phases. For a solution of the class system
with Θ_A = □_g u_A the leaves are the level sets of u_A near the axis, by [[lem:class-leaf]] (c) and the uniqueness in
[[lem:class-volterra]].

*Proof.* (a) The difference δh of the leaves solves L_ů δh = δH_L − (terms in δγ3 and its first derivatives) + Q(δh),
with L_ů the mean curvature operator of [[eq:class-leaf-cartesian]] linearised at h̊, smooth and uniformly elliptic on
the disc with the axis interior, and Q collecting the terms at least quadratic in (δh, ∂δh, ∂²δh), with smooth
coefficients. [[lem:class-interior-regularity]] with j = k, the quadratic terms absorbed on 𝔅, bounds δh in
H^(k+2) along the disc. Derivatives transverse to the disc commute with L_ů up to operators of lower order with smooth
coefficients, so ∂_⊥ δh obeys the same equation with a right side controlled by the previous step; induction on the
number of transverse derivatives gives (a) for all |α| ≤ k. The shift δc of the foliation enters as (∂_c σ[ů]) δc, the
derivative falling on ů.
(b) The same with [[lem:class-interior-regularity]] for j = 0 applied to the difference of the leaves of U and U′, on a
ball 𝔅′ small enough that L_U − L_ů is absorbed. The constant of that lemma at j = 0 holds the sup norms of the
coefficients of L_U and of their first derivatives, that is, of first and second derivatives of the leaves and of first
derivatives of g; on 𝔅′ these are bounded by the Sobolev inequality of [[lem:sobolev]] at the order k − 4 ≥ 2 and by the
bound of step (3) of [[lem:class-planar-shear]]. The shift of the foliation costs ∂_c σ, bounded on 𝔅′. The bound
needs the coefficients of L_U, which hold first derivatives of g, among the components of U. ∎

New: the text of the Block above, as described.

*2. [[lem:class-leaf-reference]], the reference for H_L[U] (lines 1373–1374).* Old:

H_L[U] is that of [[lem:class-leaf-differences]], its *leaves* are the solutions h(·; z0) of [[eq:class-leaf-volterra]]
with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its planar shear σ[U] at a point is [[eq:class-shear-leaf]] for the leaf

New:

H_L[U] is that defined before [[lem:class-leaf-states]], its *leaves* are the solutions h(·; z0) of
[[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its planar shear σ[U] at a point is
[[eq:class-shear-leaf]] for the leaf

*3. [[lem:class-leaf-reference]], the statement of (a) and (b) (lines 1388–1391).* Old:

(a), (b) The conclusions (a) and (b) of [[lem:class-leaf-differences]] hold with ů replaced by V, 𝒩_k by 𝒩_k^V and 0 < δ
≤ δ_V, the balls 𝔅 and 𝔅′ being balls about V. Here δ_V := min(r_V/8, δ_𝔐), δ_𝔐 the number of (b′) below for 2𝔐_V in
place of 𝔐 and c/2 in place of c, 𝔐_V ≥ 1 a bound for V as in (b′); the balls and C depend only on k, δ, r_*, c, r_V, 𝔐_V
and bounds for the C^(k+2) norms of V.

New:

(a), (b) The conclusions (a) and (b) of [[lem:class-leaf-differences]] hold with ů replaced by V, 𝒩_k by 𝒩_k^V and 0 < δ
≤ δ_V, the balls 𝔅 and 𝔅′ being balls about V. Here δ_V := min(δ_0, r_V/8, δ_𝔐), δ_0 the number of
[[lem:class-leaf-differences]] for ů := V and the radius r_*, δ_𝔐 the number of (b′) below for 2𝔐_V in place of 𝔐 and
c/2 in place of c, 𝔐_V ≥ 1 a bound for V as in (b′); the balls and C depend only on k, δ, r_*, c, r_V, 𝔐_V, lower
bounds for −g_V⁻¹(dτ, dτ) and for g_V on TΣ_τ, and bounds for the derivatives of order at most k + 2 of W_V.

*4. [[lem:class-leaf-reference]], the proof of (a) and (b) (lines 1449–1480).* Old:

(a) The proof of [[lem:class-leaf-differences]] (a) holds with the following changes; it uses no equation satisfied by ů.
(i) The leaves h̊ are the leaves h_V of (o), smooth by (o). (ii) The difference δh of the leaves of U and of V **with the
same axis point** z0 solves L_V δh = δH_L − (terms in δγ3 and its first derivatives) + Q(δh), where L_V is
[[eq:class-leaf-cartesian]] linearised at h_V and δH_L is evaluated on the leaf of U; the zero-order term −(∂_z H_L[V])
δh comes from H_L[V](h_U(y), y) − H_L[V](h_V(y), y). L_V is smooth and uniformly elliptic with the axis interior by
[[lem:class-leaf]] (b), which holds at every graph. (iii) Derivatives transverse to the disc are taken in z0 and τ in
place of the value of ů_A and τ. They commute with L_V up to operators of lower order with smooth coefficients, as h_V is
smooth in (τ, z0, y) by (o) on each slice and the smooth dependence of V on τ; the change of variables (z0, y) ↦
(h_V(|y|; z0), y) has Jacobian ∂_(z0) h_V ∈ [1/2, 3/2]. (iv) At a point x, with σ_W(z0, y) := σ[W] at (h_W(|y|; z0), y),

    σ[U](x) − σ[V](x) = (σ_U − σ_V)(z0^U(x), y) + (σ_V(z0^U(x), y) − σ_V(z0^V(x), y)),

and by [[eq:class-leaf-lipschitz]] |z0^U(x) − z0^V(x)| ≤ 2 |δh(y; z0^U(x))|: the shift of the foliation enters as (∂_(z0)
σ_V)(z0^U(x) − z0^V(x)) up to a quadratic remainder, the derivative falling on V. (v) The balls are about V; the sup
norms of the coefficients of L_U on 𝔅 are bounded by [[lem:sobolev]] and by step (3) of the proof of
[[lem:class-planar-shear]], with sup |∂h| ≤ C r from [[lem:class-volterra]] for U in place of the bound through −∂_y
u/∂_z u. For U ∈ 𝔅′ the leaves of U exist and foliate 𝒰_(r_V/8) by Steps 1–3 of the proof of (o) for U, which use only
its C² and C¹ bounds, the C³ norms of g and the C¹ norms of p_A, Θ_A being within C 𝒩_(k−1)^V(U) of those of V by
[[lem:sobolev]] (k − 4 ≥ 2); so for 𝔅′ small, U has the bounds of (b′) for 2𝔐_V and c/2. (vi) The term ‖δh‖_(L²(𝔻_(2δ)))
on the right of [[lem:class-interior-regularity]] is bounded by the radial form: the two leaves have the same axis point,
so δh(0) = 0, and the step *One leaf* of the proof of (b′), with (U, U′) := (U, V), gives |δh(r)| ≤ √2 r ‖F‖_(L²(r dr;
[0,2δ])) with |F| ≤ C |U − V| along the leaf of U; the same bound and [[eq:class-leaf-lipschitz]] control the shift
z0^U(x) − z0^V(x) of (iv). (vii) The bounds along the leaves are integrated over their axis points z0, with the Jacobian
∂_(z0) h_V ∈ [1/2, 3/2] of (iii) and the weight 2π ρ1, ρ1 ∈ [ρ1(p)/2, 2ρ1(p)], of the L² norms of G-invariant functions,
as in the step *All leaves* of the proof of (b′); this gives the bounds in L²(𝒰_δ), the zero-order terms being at most C
‖U − V‖_(L²(𝒰_(2δ))) ≤ C 𝒩_k^V(U).

(b) This is (b′) with D := Σ_τ, which contains the leaves through all its points: for U, U′ ∈ 𝔅′ the C³ norms of g and
the C¹ norms of p_A and Θ_A are bounded by the Sobolev inequality of [[lem:sobolev]] at the order k − 4 ≥ 2,
and |p_A^Σ|, |p_A(∂_z)| and the lower bounds for A3, B3 and det₂ are those of V up to a factor 2, by (v); so U and U′
have the bounds of (b′) for 2𝔐_V and c/2, and δ ≤ δ_V ≤ δ_𝔐. The bound needs the first derivatives of g among the
components of U.

New:

(a), (b) [[lem:class-leaf-differences]] holds for every smooth state ů on a neighbourhood of the closure of 𝒰_(r_*), r_*
being the radius of its setting; its proof uses no equation satisfied by ů. With ů := V it gives (a) and (b), its balls
being balls about V and its norm 𝒩_k at most 𝒩_k^V. For U in its ball 𝔅′, decreased if necessary, the C³ norms of g and
the C¹ norms of p_A and Θ_A are within C 𝒩_(k−1)^V(U) of those of V, by Sobolev's embedding ([[thm:std-bh-embedding]])
and k − 1 ≥ 5, and so are |p_A^Σ|, |p_A(∂_z)| and the lower bounds for A3, B3 and det₂; so U has the bounds of (b′) for
2𝔐_V and c/2.

*5. [[def:class-adapted]], the bound on T_(τ,U) − id (lines 1590–1591 and 1605–1606).* Two old texts. First old:

proof of [[lem:class-leaf-differences]] (a), through its induction on the derivatives transverse to the disc, bounds
∂_(z0)^j δh, j ≤ 2, in L² over I with values in H^(k+2−j)(D_B) by C 𝒩_k(τ). So for |β| ≤ k, ∂_y^β δh lies in H² of (z0,

First new:

bounds of [[lem:class-leaf-differences]] (c), at the axis point z̊_B(τ), bound ∂_(z0)^j δh, j ≤ 2, in L² over I with
values in H^(k+2−j)(D_B) by C 𝒩_k(τ). So for |β| ≤ k, ∂_y^β δh lies in H² of (z0,

Second old:

each x′; and of class C^(k−1), with bounded derivatives of order k and invertible differential. The same argument for the
τ-derivatives, which the proof of [[lem:class-leaf-differences]] (a) bounds as well, shows that B_U is a C¹-small

Second new:

each x′; and of class C^(k−1), with bounded derivatives of order k and invertible differential. The same argument for the
τ-derivatives, which [[lem:class-leaf-differences]] (c) bounds pointwise as well, shows that B_U is a C¹-small

*6. [[thm:class-stability]], the step *Smoothness* of its proof (lines 1745–1757).* Old:

*Smoothness.* Let σ ≥ k be an integer. The proof of [[lem:class-leaf-differences]] (a), with
[[lem:class-interior-regularity]] at j = σ, the quadratic terms absorbed on 𝔅 and Moser's estimate for the terms of lower
order, gives ‖σ_A[U] − σ_A[ů]‖_(H^σ(𝒰_δ)) ≤ C_σ (1 + ‖U‖_(H^σ)) for U ∈ 𝔅 ∩ H^σ; with [[lem:class-composition]] (b) for
the local terms, ‖F(τ, U)‖_(H^σ) ≤ C_σ (1 + ‖U‖_(H^σ)) for U ∈ 𝒟_ρ ∩ H^σ. The proof of [[thm:class-kato]] (a) then runs
at the order σ with the ball 𝒟_ρ kept in H^k (the step *Boundedness* at the order σ, the others at the order k), and its
continuation holds while sup_τ ‖U(τ)‖_(H^σ) < ∞ and ‖U(τ)‖_(H^k) ≤ η_ρ ρ. On each interval of the restarts the extended
data lie in H^σ: the data are smooth on the slice by induction over the intervals, so are the leaves through the axis
points, by [[lem:class-interior-regularity]] at every order, hence d_B, Stein's operator being bounded on every W^(m,∞),
and T_(τ_i,U); and E_⋆ is bounded on every H^σ. So the solution in H^σ exists for a short time, equals the solution in
H^k by uniqueness, and [[lem:class-kato-linear]] (c) at the order σ, with the bound on F(τ, U) in H^σ and K_U bounded by
the H^k bound, gives a linear Gronwall inequality for ‖U(τ)‖_(H^σ), so that it lies in H^σ on the whole interval. By the
equation, and by differentiating [[eq:class-leaf-volterra]] in τ as in step (4) of the proof of
[[lem:class-planar-shear]], every ∂_τ^j U is bounded in every H^σ, by induction on j. So the solution is smooth.

New:

*Smoothness.* Let σ ≥ k be an integer. [[lem:class-leaf-differences]] (a) at the order σ gives ‖σ_A[U]² −
σ_A[ů]²‖_(H^σ(𝒰_δ)) ≤ C_σ (1 + ‖U‖_(H^σ)) for U ∈ 𝔅 ∩ H^σ, with C_σ depending also on an upper bound for ‖U‖_(H^(σ−1));
with [[lem:class-composition]] (b) for the local terms, ‖F(τ, U)‖_(H^σ) ≤ C_σ (1 + ‖U‖_(H^σ)) for U ∈ 𝒟_ρ ∩ H^σ, with C_σ
of the same kind. We argue by induction on σ, so that ‖U(τ)‖_(H^(σ−1)) is bounded on each interval of the restarts and
C_σ is a constant there. The proof of [[thm:class-kato]] (a) then runs at the order σ with the ball 𝒟_ρ kept in H^k (the
step *Boundedness* at the order σ, the others at the order k), and its continuation holds while sup_τ ‖U(τ)‖_(H^σ) < ∞
and ‖U(τ)‖_(H^k) ≤ η_ρ ρ. On each interval of the restarts the extended data lie in H^σ: the data are smooth on the slice
by induction over the intervals, so are the leaves through the axis points, by [[lem:class-leaf-states]] (a), hence d_B,
Stein's operator being bounded on every W^(m,∞), and T_(τ_i,U); and E_⋆ is bounded on every H^σ. So the solution in H^σ
exists for a short time, equals the solution in H^k by uniqueness, and [[lem:class-kato-linear]] (c) at the order σ,
with the bound on F(τ, U) in H^σ and K_U bounded by the H^k bound, gives a linear Gronwall inequality for ‖U(τ)‖_(H^σ),
so that it lies in H^σ on the whole interval. By the equation, and by differentiating [[eq:class-leaf-volterra]] in τ as
in step (4) of the proof of [[lem:class-planar-shear]], every ∂_τ^j U is bounded in every H^σ, by induction on j. So the
solution is smooth.

*7. [[ch:localised-data]], [[lem:loc-axis-system]], the proof of (a) (lines 2933–2934 of that chapter).* Old:

so [[lem:class-leaf-differences]] (a) about Ů, with [[lem:class-composition]] (a) for the square and sup |σ_A| bounded
on 𝔅, bounds it in H^k by C ‖Z‖_(H^k), which gives (F1) and the linear bound; [[lem:class-leaf-differences]] (b), with

New:

so [[lem:class-leaf-differences]] (a) about Ů, which bounds σ_A[𝐔]² − σ_A[Ů]² = σ_A[𝐔]² in H^k, bounds it by C ‖Z‖_(H^k),
which gives (F1) and the linear bound; [[lem:class-leaf-differences]] (b), with

*8. [[lem:class-planar-shear]], its bound and step (5) of its proof (lines 1286 and 1318–1319).* Its uses are steps
(1), (3) and (4) of its proof and its constants ([[lem:class-leaf-differences]], [[lem:class-leaf-reference]],
[[thm:class-stability]], [[ch:localised-data]]); none uses an H^k bound of σ itself, and σ enters [[eq:class-x]] and the
closure through σ². Two old texts. First old:

    ‖σ‖_(H^k(𝒰_δ)) ≤ C (‖Θ‖_(H^k(𝒰_(2δ))) + ‖dg‖_(H^k(𝒰_(2δ))) + ‖du‖_(H^k(𝒰_(2δ))) + 1),

First new:

    ‖σ²‖_(H^k(𝒰_δ)) ≤ C (‖Θ‖_(H^k(𝒰_(2δ))) + ‖dg‖_(H^k(𝒰_(2δ))) + ‖du‖_(H^k(𝒰_(2δ))) + 1),

Second old:

(5) Then k_L ∈ H^k, and σ ∈ H^k by [[eq:class-shear-leaf]], whose last term is a smooth function of dg and of the leaf's
tangent. On the axis σ = 0 and κ2 = (Θ − κ1)/2 by [[prop:class-axis]] (d). ∎

Second new:

(5) In the frame X_i := ∂_(y_i) + ∂_i h ∂_z of TΣ_L, the second fundamental form of the leaf for the normal ν of
[[lem:class-leaf]] (b) is k_L(X_i, X_j) = −(∂_i ∂_j h + Γ[γ3]^c_ab X_i^a X_j^b ∂_c F)/|∇F|, F := z − h, so its components
lie in H^k by (3) and (4), and so do those of χ̸ = ± |∇_M3 u| k_L − n(u) K_Σ on TΣ_L, the sign that of ∂_z u, by
Moser's estimate. By [[lem:class-gauss]] (b), σ² = 2 |χ̸ − ½ (tr χ̸) γ̸|² with γ̸_ij = γ3(X_i, X_j), a smooth function
of these components, of γ3 and of ∂h, which are bounded by step (3), the C² norms of g and the C¹ norms of u; so σ²
lies in H^k with the bound stated, by Moser's estimate. On the axis σ = 0 and κ2 = (Θ − κ1)/2 by
[[prop:class-axis]] (d). ∎

*9. [[ch:class-system]], the opening paragraph (lines 17–18).* Old:

shear, the trace-free part of the second fundamental form of the family's level sets in the slice, and elliptic
regularity of those level sets recovers it from the expansion with no loss ([[lem:class-planar-shear]]). With lateral

New:

shear, the trace-free part of the second fundamental form of the family's level sets in the slice, and elliptic
regularity of those level sets recovers its square, the form in which it enters the Raychaudhuri equation, from the
expansion with no loss ([[lem:class-planar-shear]]). With lateral

### Crosswalk rows

For crosswalk/81-class-system.tsv. Each row is given as its four fields (label; source; source_name; note), to be
written with tab separators. The second field is "paper/reader/proofs/P-CLD.md@PENDING:N", N the line of the label in
this file, to be replaced as usual.

New rows, after the row of lem:class-planar-shear and before the row of lem:class-leaf-differences, in this order:

Row 1. lem:class-leaf-states; paper/reader/proofs/P-CLD.md@PENDING:36; proof P-CLD, Lemma (The leaves of a state);
new: the definitions of state, bounds (M, c), H_L[U] with the plane fixed by p_A, leaves, σ[U] and arcs, moved out of
lem:class-leaf-differences; (a) foliation with quotients in [1/2, 3/2] and |Δh′| ≤ C r |Δz0|, smoothness by the
radial Volterra form in s = h′/r; (b) the bound along one arc; (c) the bound on sets closed under arcs, constant
independent of the set; constants from C² of g and C¹ of p_A, Θ_A only, by the decomposition eq:class-leaf-g.
Row 2. eq:class-leaf-quotient; paper/reader/proofs/P-CLD.md@PENDING:43; proof P-CLD, display; difference quotients of
the leaves in the axis point.
Row 3. eq:class-leaf-pointwise; paper/reader/proofs/P-CLD.md@PENDING:53; proof P-CLD, display; σ[U] − σ[U′] at a
point by f, its Hardy average and its weighted L² norm along the arc.
Row 4. eq:class-leaf-sets; paper/reader/proofs/P-CLD.md@PENDING:58; proof P-CLD, display; the L² bound on sets closed
under arcs.
Row 5. eq:class-leaf-g; paper/reader/proofs/P-CLD.md@PENDING:86; proof P-CLD, display; G = r(…) − q(C3 r + γ_zz q)²/det₂,
from det₂ − γ_zz N_L² = −(γ_z1 + γ_zz q)².
Row 6. eq:class-leaf-g-bounds; paper/reader/proofs/P-CLD.md@PENDING:92; proof P-CLD, display; the bounds of G on R,
including the bound of ∂_z G by C_1 (r + |q|) with C² of g.
Row 7. eq:class-leaf-shear-s; paper/reader/proofs/P-CLD.md@PENDING:126; proof P-CLD, display; σ at a point of a leaf
as a smooth function of the point, of W there and of s = h′/r; C3 = ∂_(y2)γ3(∂_z, ∂_(y2)) by invariance.
Row 8. eq:class-leaf-s; paper/reader/proofs/P-CLD.md@PENDING:140; proof P-CLD, display; the leaf equation in s = h′/r on
[−r_1, r_1].
Rows for lem:class-leaf-differences's displays, after the row of lem:class-leaf-differences and before the row of
rem:class-leaf-numerics, in this order:
Row 9. eq:class-leaf-sup; paper/reader/proofs/P-CLD.md@PENDING:234; proof P-CLD, display; Sobolev on Σ ∩ 𝒰.
Row 10. eq:class-leaf-divergence; paper/reader/proofs/P-CLD.md@PENDING:283; proof P-CLD, display; the mean curvature
equation in divergence form, after the divergence form of P-CIVP5's tame lemma.
Row 11. eq:class-leaf-radial; paper/reader/proofs/P-CLD.md@PENDING:289; proof P-CLD, display; 𝔙 = y 𝔰, 𝔰 the Hardy
average of Φ.
Row 12. eq:class-leaf-inverse; paper/reader/proofs/P-CLD.md@PENDING:295; proof P-CLD, display; ∂_y h = 𝔓(y, h, y 𝔰).
Row 13. eq:class-leaf-square; paper/reader/proofs/P-CLD.md@PENDING:303; proof P-CLD, display; σ² = 2|χ̸ − ½ (tr χ̸) γ̸|²
in the frame X_i.
Row 14. eq:class-leaf-compose; paper/reader/proofs/P-CLD.md@PENDING:333; proof P-CLD, display; composition with the leaf
coordinates.
Row 15. eq:class-leaf-transverse; paper/reader/proofs/P-CLD.md@PENDING:356; proof P-CLD, display; transverse derivatives
by the radial form, the zero-order bound of R-P-CIVP4 Major 5.
Row 16. eq:class-leaf-elliptic; paper/reader/proofs/P-CLD.md@PENDING:363; proof P-CLD, display; derivatives along the
disc by the flat Laplacian of the radial potential u_X.

Changed rows:

- lem:class-leaf-differences keeps its label; its source field becomes "paper/reader/proofs/P-CLD.md@PENDING:199"
  followed by the present sources, its source_name field gains "; proof P-CLD (statement and proof replaced)", and its
  note becomes: "ů any smooth state; (a) for σ², at every order, spacetime derivatives for families; (b) from
  lem:class-leaf-states (c); (c) the leaves, ∂_(z0)^j δh in L²(I; H^(k+2−j)), j ≤ 2, used by def:class-adapted; the
  zero order by the radial form (R-P-CIVP4 Major 5); the definitions of the leaves, with P-CIVP3's reading of H_L, moved
  before lem:class-leaf-states".
- lem:class-leaf-reference appends to its source field "; paper/reader/proofs/P-CLD.md (Placement 2–4)" and to its note
  "; (a), (b) are lem:class-leaf-differences with ů := V (P-CLD)".
- lem:class-planar-shear appends to its note "; bound stated for σ², step (5) by the Cartesian form of χ̸ (P-CLD
  Placement 8)", and ch:class-system appends "; opening paragraph: the square of the planar shear (P-CLD Placement 9)".
- def:class-adapted and thm:class-stability append to their notes "; lem:class-leaf-differences (c), and (a) for σ² at
  every order, cited (P-CLD Placement 5, 6)"; lem:loc-axis-system in crosswalk/83-localised-data.tsv appends "; (a) for
  σ² (P-CLD Placement 7)".

### Notes on the changes and on the later sections

*From the reader's replacement text (R-P-CIVP4, Major 5).* The reader's text added two sentences to the old proof of
(a) and replaced (b) by (b′) of lem:class-leaf-reference with D the whole slice; Tier 4's merge carried the same steps
into lem:class-leaf-reference (its (vi) and (vii)). I kept the reader's three points and changed the rest:

1. The zero-order bound and the shift δc: kept, but proved for every transverse derivative, not only at order zero, by
   the radial form in s = h′/r (Step 5, eq:class-leaf-transverse), with the factor r² in η = r² ∫ θ δs(θr) dθ. The
   reader's route (the bound |δh| ≤ C r ‖F‖ of *One leaf*) covers order zero only; the transverse derivatives T^j η
   need the same bound, and the Cartesian form cannot give it: η = ∫_0^1 ∂_y η(ty) · y dt is not bounded in L² by
   ∂_y η in L² (a logarithmic loss at the axis).
2. The integration over the axis points: kept (lem:class-leaf-states (c), Step 2), with the weight 2π z and the
   Jacobian ∂_(z0) h ∈ [1/2, 3/2], and the comparison of H^m norms on 𝒰_δ and in (z, y).
3. (b) from the leaf-by-leaf bound: kept, as lem:class-leaf-states (c) with D the slice. The leaf-by-leaf proof is new,
   after P-CIVP5's lem:class-leaf-arc (b): it needs only C² of g (not C³), because by invariance C3 = ∂_(y2)γ3(∂_z,
   ∂_(y2)) is a first derivative of g at the point, and G = r(…) − q(C3 r + γ_zz q)²/det₂ gives |∂_z G| ≤ C (r + |q|)
   directly (this also settles the reader's minor 2 for Tier 4).
4. The elliptic step: the old proof applied lem:class-interior-regularity with j = k to an operator linearised at h̊ and
   absorbed the quadratic terms; that absorption fails across the shrinking discs, and the coefficients carry the leaf of
   U. I replaced it by the divergence form (eq:class-leaf-divergence, after P-CIVP5's Block A1) and the flat Laplacian of
   the radial potential u_X (Step 6), which needs lem:class-interior-regularity for Δ only.
5. **A statement change, accepted on two conditions, both met below.** (a) now bounds σ[U]² − σ[ů]², not σ[U] − σ[ů].
   The H^k norm of σ itself needs a bound for the coefficient α of a G-invariant symmetric tensor field αδ + β y ⊗ y
   on the y-plane (α = T(K2, K2)/|y|²) in H^m by the field in H^m; σ involves α of K_Σ and of ∂γ3 (through K_Σ(e2, e2)
   and ν(log B3)). Pointwise |α| ≤ |T|, but in H^m the only bound I can prove loses a derivative (α = tr T − 𝒜(div(T
   y))); a loss-free bound needs Rellich-type inequalities for angular mode 2, which the paper does not contain. σ² =
   2|χ̸ − ½(tr χ̸)γ̸|² is a smooth function of the Cartesian quantities, and every use of (a) — Steps 6, 9 and
   *Smoothness* of thm:class-stability, lem:loc-axis-system (a), Tier 4's corner proof, lem:class-leaf-reference (a) —
   is through σ² (the closure −½ σ²). The old step (5) of lem:class-planar-shear (σ ∈ H^k "by eq:class-shear-leaf,
   whose last term is a smooth function of dg and of the leaf's tangent") used the same unproved bound; Placement 8
   restates that lemma for σ² and proves step (5) from the Cartesian form of χ̸, and Placement 9 adjusts the sentence
   of the chapter's opening paragraph that cites it. With these, no H^k bound of σ itself remains in the chapters; the
   list below checks this.
6. The higher orders: (a) at every order m > k with C_m depending on 𝒩_(m−1)(U); Placement 6 makes *Smoothness* use it
   by induction on σ.
7. ů may be any smooth state (no equation is used), so lem:class-leaf-reference (a), (b) follow at once (Placement 3, 4).
   The lemma holds for every δ ≤ δ_0 with fixed balls, as Tier 4's δ_V requires.

*Every use of [[lem:class-leaf-differences]] (a), and every H^k bound of σ, in the chapters at HEAD.* Found by grepping
all chapter sources for the label, for lem:class-leaf-reference, for lem:class-planar-shear, and for the shear (σ_A,
σ[·], "planar shear", ‖σ‖); only chapters 81, 82 and 83 contain any. Line numbers are those at HEAD 9d133b0c, whose
chapters are those of 5a238875 and edafc288.

Uses of (a), or of the H^k bounds in its proof:
- 81:1388–1391, lem:class-leaf-reference (a), (b): the conclusions of (a), (b) for V; after Placement 3 they are the
  σ²-form, used only as listed below for chapter 83.
- 81:1405, the remark after lem:class-leaf-reference: "(a) and (b) with V := ů are lem:class-leaf-differences"; no
  bound of its own; consistent.
- 81:1449–1474, the proof of lem:class-leaf-reference (a) as changes to the old proof of (a): replaced by Placement 4;
  through σ².
- 81:1590–1591, def:class-adapted: the leaves δh in L²(I; H^(k+2−j)), j ≤ 2; no σ; now (c) (Placement 5).
- 81:1605–1606, def:class-adapted: τ-derivatives of the leaves, for B_U C¹-close to B; no σ; now (c), pointwise.
- 81:1675, Step 6 of thm:class-stability: ‖∂^α(S_A^ax(U) − S_A^ax(ů))‖ ≤ C 𝒩_k, S_A^ax holding the shear only as
  −½ σ_A[Θ_A]² (81:1671), its other terms local; through σ².
- 81:1704, Step 9 of thm:class-stability, (F1): the forcing holds the shear only through S_A^ax; through σ².
- 81:1745–1748, *Smoothness* of thm:class-stability: ‖σ_A[U] − σ_A[ů]‖_(H^σ); replaced by Placement 6 with the σ²-form
  and the induction on σ; the forcing holds σ_A only as −½ σ_A².
- 82:2198–2199 and 82:2229, prop:vlasov-uniform-n (proof): the right side S^ax_𝔨 near the axes and the balls 𝔅, 𝔅′ of
  the lemma, checked as in Step 6 of thm:class-stability; through σ².
- 83:2933–2934, lem:loc-axis-system (a): the term −½ χ ψ_ax σ_A[𝐔]² with σ_A[Ů] = 0; through σ² (Placement 7).
- 83:2975, the smoothness of the solution of lem:loc-axis-cauchy, "by the argument of the paragraph *Smoothness*" of
  thm:class-stability; through σ², by Placement 6.
- 83:3697–3698, Step 3 of the proof of prop:civp-axes-corner, (F1): the non-local part −½ ξχ_ax (σ_A[𝐔̂ + Z]² −
  σ_A[Û]²), by lem:class-leaf-reference (a); through σ².
- 83:3714–3716, Step 4 there: smoothness by the argument of *Smoothness* with lem:class-leaf-reference (a) at every
  order; through σ².

H^k bounds of σ itself:
- 81:18, the opening paragraph: "recovers it from the expansion with no loss ([[lem:class-planar-shear]])"; reworded to
  the square (Placement 9).
- 81:1286 and 81:1318–1319, lem:class-planar-shear and step (5) of its proof: restated for σ² and proved (Placement 8).
  Its uses (81:1327 and 81:1356 in the old text of Placement 1; 81:1437, 1445 and 1464, steps (3) and (4), in
  lem:class-leaf-reference; 81:1659, its constants in thm:class-stability; 81:1757, step (4) in *Smoothness*; 83:503,
  step (1)) use steps (1), (3), (4) or its constants, not the bound for σ.
- 81:1747, *Smoothness*: as above, Placement 6.
- 81:1102–1103, after prop:class-axis: "σ is nevertheless recovered from the Laplacian with no loss" refers to the flat
  model and is proved there (prop:class-flat-model (b): σ_pl = ℓ − 2𝒜ℓ, ‖σ_pl‖ = ‖ℓ‖, 𝒜 bounded on every Ḣ^j); no
  curved claim.
- 81:1137, "The next section carries the recovery of (b) over to curved metrics": qualitative; in L² it is
  lem:class-leaf-states (c), in H^k it is the σ²-form of (a).

Bounds of σ in L² or L^∞ only, which are not affected: 81:1717 and 81:1732–1734 (domain of dependence, (b)); 81:1785–1787
(Step 10: (b) and |σ| ≤ C on 𝔅′); 83:509–511 (eq:loc-lens-shear, (b)); 83:2781 and 83:3095 (lem:loc-axis-shear, the
case D := Ō of lem:class-leaf-states (c)); 83:2934–2935 and 83:2991 ((b), σ_A bounded on 𝔅′); 83:3738–3740,
83:3759–3761 and 83:3891–3893 (lem:class-leaf-reference (b), (b′)). Qualitative statements: 82:1802 and 82:1957
(σ2/ρ2² smooth for a smooth eikonal, with its own proof in chapter 82; no Sobolev bound).

*Tier 3 (merged; its item 8).* Its definitional clause is carried into the definitions before lem:class-leaf-states
(H_L[U] with p_A(n), the sign of p_A(∂_z), and Π the γ3-orthogonal complement of p_A^Σ); no statement changes.
lem:loc-axis-shear is lem:class-leaf-states (c) with D := Ō (Ō closed, arcs of its points in Ō by continuity, ∂O null);
lem:loc-axis-system (a) needs the wording of Placement 7, as (a) now bounds σ². Its uses of 𝔅, 𝔅′, δ and the last
statement are served.

*Tier 4 (merged as lem:class-leaf-reference).* (o) and (b′) keep their own proofs and are also lem:class-leaf-states (a)
and (c) (whose arc hypothesis is weaker than (b′)'s disc hypothesis; (b′) asks C³ of g, (c) only C²). (a), (b) become
lem:class-leaf-differences with ů := V (Placements 3, 4); their uses in the corner proof (F1), (F2), *Smoothness* and
the uniqueness proof go through σ² or (b). One point outside this file: (o) Step 1 and (b′) bound n, K_Σ and κ_A1 by C²
norms of g, which needs also lower bounds for −g⁻¹(dτ, dτ) and for g on TΣ_τ; the bounds (M, c) of this file include
them, and Placement 3 names them for (a), (b).

*Tier 5 (P-CIVP5, fix round).* lem:class-leaf-arc (a), (b), (c) is lem:class-leaf-states (a), (b), (c) with the roles of
the two states exchanged ((b) and (c) here take f on the arcs of the first state); it can be cited instead. For
lem:class-leaf-tame (a lighter form of (a), on past sets, in spacetime norms): its step (6) bounds D^α η, for α
transverse, by (H) applied to ∫_0^1 D^α π(sy) · y ds; for transverse α the weight is s⁻¹ and (H) does not apply (the
logarithmic loss of note 1). Step 5 here (the radial form in s, η = r² ∫ θ δs(θr) dθ) repairs it and runs on star-shaped
fibres. Its step (2) asserts σ = 𝔖(W, y, h, ∂h, 𝒜Φ) smooth, which meets the coefficient question of note 5; stated for
σ², as here, it holds. Its labels lem:class-leaf-arc, eq:class-leaf-arc, lem:class-leaf-tame, eq:class-leaf-tame do not
collide with the labels of this file.
