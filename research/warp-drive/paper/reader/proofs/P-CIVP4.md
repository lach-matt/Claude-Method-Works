### Block A. Addition to the planar shear at an axis

The text of this block goes into [[sec:class-planar-shear]] of [[ch:class-system]] after [[rem:class-leaf-numerics]]; the
Placement section below gives the position and one clause added to [[lem:class-leaf-differences]].

**Lemma {#lem:class-leaf-reference}** (The planar shear about a reference that is not a solution.) Near a point p of axis
2 with ρ1(p) > 0, on a slice Σ_τ, fix a family A and use the coordinates (z, y) of [[lem:class-leaf]]. A *state* is a
G-invariant U = (g, p_A, Θ_A, q_A) near the orbit of p, with g of class C², p_A and Θ_A of class C¹, g Lorentzian, Σ_τ
spacelike for g and p_A(∂_z) ≠ 0 on the axis. Its function H_L[U] is that of [[lem:class-leaf-differences]], its *leaves*
are the solutions h(·; z0) of [[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its planar shear
σ[U] at a point is [[eq:class-shear-leaf]] for the leaf through that point, with |p_A^Σ| in place of |∇_M3 u| and p_A(n)
in place of n(u), and for a state V, 𝒩_k^V(U) is [[eq:class-energy]] with V in place of ů. Let V be a smooth state
with |p_V(∂_z)| ≥ c > 0 on the axis near p.

(o) (Foliation.) There are r_V ∈ (0, ρ1(p)/4] and C_V, depending only on c, on lower bounds for A3, B3 and det₂ of the
metric γ3 of V and on bounds for the C² norms of g_V and the C¹ norms of p_V and Θ_V near the orbit of p, such that
for |z0 − z(p)| ≤ r_V the leaf h_V(·; z0) is defined on [0, r_V] with |h_V′(r; z0)| ≤ C_V r, and for |z0 − z(p)| ≤
r_V, |z0′ − z(p)| ≤ r_V, z0 ≠ z0′ and 0 ≤ r ≤ r_V

    1/2 ≤ (h_V(r; z0) − h_V(r; z0′))/(z0 − z0′) ≤ 3/2.                                    {#eq:class-leaf-lipschitz}

Every point x of 𝒰_(r_V/4) lies on exactly one of these leaves; we write z0^V(x) for its axis point. The map (z0, y) ↦
h_V(|y|; z0) is smooth, and so is z0^V.

(a), (b) The conclusions (a) and (b) of [[lem:class-leaf-differences]] hold with ů replaced by V, 𝒩_k by 𝒩_k^V and δ ≤
r_V/8, the balls 𝔅 and 𝔅′ being balls about V; the balls and C depend only on k, δ, c, r_V and bounds for the C^(k+2)
norms of V near the orbit of p.

(b′) (Leaf by leaf.) Let 𝔐 ≥ 1 bound, on 𝒰_(ρ1(p)/4), the C³ norms of g and the C¹ norms of p_A and Θ_A of two states U
and U′, the inverses of lower bounds for A3, B3, det₂ of their metrics γ3 and the inverse of a lower bound for |p_A^Σ|,
and let |p_A(∂_z)| ≥ c on the axis for both. There are δ_𝔐 ∈ (0, ρ1(p)/16] and C, depending only on 𝔐 and c, such that
for 0 < δ ≤ δ_𝔐 and every set D ⊂ Σ_τ for which the leaf of U through each point of D ∩ 𝒰_δ lies, over the disc 𝔻_(2δ),
in D,

    ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D∩𝒰_(2δ))),                               {#eq:class-leaf-wise}

where U − U′ includes the difference of the first derivatives of the metrics. No ball about a reference state and no
extension operator enters, and C does not depend on D.

Here V need not solve any equation: the leaves are defined by [[eq:class-leaf-volterra]] from H_L[V], and no phase is
involved. For a solution of the class system with Θ_A = □_g u_A they are the level sets of u_A
([[lem:class-leaf-differences]]), so (a) and (b) with V := ů are [[lem:class-leaf-differences]].

*Proof.* Constants C below depend only on the quantities named in the part concerned. Write G(r, z, q) := r H(z, r)/
a_L(r, z, q) − E_L(r, z, q) as in the proof of [[lem:class-volterra]], with H := H_L[V] in (o), so that a leaf solves r
h′(r) = ∫_0^r G(ρ, h(ρ), h′(ρ)) dρ.

(o) *Step 1.* At an axis point the spatial part of p_V is p_V(∂_z) dz ([[lem:class-phase-axis]]), of γ3-length at least c
(sup A3)^(−1/2); so |p_V^Σ| ≥ c (sup A3)^(−1/2)/2 on a neighbourhood of the axis whose size depends only on c and the C¹
bounds, and there H_L[V] is C¹, with H and its first derivatives bounded in terms of c, the C² norms of g_V (which bound
n, K_Σ, κ_A1 and γ3 with its first two derivatives) and the C¹ norms of p_V and Θ_V. [[lem:class-volterra]] applies at
every z0 with |z0 − z(p)| ≤ r_1, r_1 depending only on these bounds, with one r0 and one C_0 for all such z0, since its
constants are bounds over a neighbourhood of (z0, 0) that hold uniformly. Its proof provides C_1, C_2 and δ_p with |∂_z
G| ≤ C_1, |∂_q G| ≤ C_2 (r + |q|), C_2 (r0 + δ_p) ≤ 1/4, C_1 r0 ≤ 1/2 and C_0 r0 ≤ δ_p, and it gives |h′| ≤ C_0 r ≤ δ_p
on [0, r0].

*Step 2.* Let h_1, h_2 be the leaves through z_1, z_2 and w_i := h_i′. As |h_1(ρ) − h_2(ρ)| ≤ |z_1 − z_2| + ρ
sup_[0,ρ] |w_1 − w_2| and both |w_i| ≤ δ_p,

    |w_1(r) − w_2(r)| ≤ r⁻¹ ∫_0^r (C_1 |h_1 − h_2| + C_2 (ρ + δ_p) |w_1 − w_2|) dρ
                     ≤ C_1 |z_1 − z_2| + (C_1 r + 1/4) sup_[0,r] |w_1 − w_2|,

and C_1 r + 1/4 ≤ 3/4; so sup_[0,r] |w_1 − w_2| ≤ 4C_1 |z_1 − z_2| and |h_1(r) − h_2(r) − (z_1 − z_2)| ≤ 4C_1 r |z_1 −
z_2|. Put r_V := min(r0, r_1, 1/(8C_1), 1/C_0, ρ1(p)/4) and C_V := C_0. Then [[eq:class-leaf-lipschitz]] holds.

*Step 3.* For |y| = r ≤ r_V/4 the map z0 ↦ h_V(r; z0) on [z(p) − r_V, z(p) + r_V] is continuous and strictly increasing,
and |h_V(r; z0) − z0| ≤ C_0 r²/2 ≤ r_V/32; so its image contains [z(p) − 3r_V/4, z(p) + 3r_V/4], and each point of
𝒰_(r_V/4) lies on exactly one leaf.

*Step 4.* For r > 0 the leaf equation is the regular ordinary differential equation (r h′)′ = r H/a_L − E_L with smooth
coefficients, so each leaf is smooth on (0, r_V], and the graph y ↦ h_V(|y|; z0) is C¹ on 𝔻_(r_V) with mean curvature
H_L[V] off the axis ([[lem:class-leaf]] (c)). The bound on the second derivatives in step (3) of the proof of
[[lem:class-planar-shear]] uses only these facts; it gives |h″| ≤ C on (0, r_V], so the first derivatives of the graph
are Lipschitz on 𝔻_(r_V) and the graph lies in H²(𝔻_(r_V)), and it solves [[eq:class-leaf-cartesian]] there in the sense
of distributions, a point being removable for a C¹ function with bounded second derivatives off it. The induction of that
step, applied with H_L[V] smooth, gives the graph in H^(j+2) on smaller discs for every j, so it is smooth. The map (z0,
w) ↦ r⁻¹ ∫_0^r G(ρ, z0 + ∫_0^ρ w, w(ρ)) dρ is smooth from an interval times a ball of C([0, r_V]) into C([0, r_V]), and
by Step 2 its differential in w has norm at most 3/4; by the implicit function theorem the leaf depends smoothly on z0
with values in C¹([0, r_V]). Differentiating [[eq:class-leaf-cartesian]] in z0, each ∂_(z0)^j of the graph solves that
equation linearised at the leaf, with a right side holding lower derivatives in z0, and [[lem:class-interior-regularity]]
at every order gives all derivatives in y, as in step (4) of the proof of [[lem:class-planar-shear]] with z0 in place of
the value of the phase. So (z0, y) ↦ h_V(|y|; z0) is smooth, and by [[eq:class-leaf-lipschitz]], ∂_(z0) h_V ∈ [1/2, 3/2];
the implicit function theorem gives z0^V smooth.

(a), (b) The proof of [[lem:class-leaf-differences]] holds with the following changes; it uses no equation satisfied by
ů. (i) The leaves h̊ are the leaves h_V of (o), smooth by (o). (ii) The difference δh of the leaves of U and of V **with
the same axis point** z0 solves L_V δh = δH_L − (terms in δγ3 and its first derivatives) + Q(δh), where L_V is
[[eq:class-leaf-cartesian]] linearised at h_V and δH_L is evaluated on the leaf of U; the zero-order term −(∂_z H_L[V])
δh comes from H_L[V](h_U(y), y) − H_L[V](h_V(y), y). L_V is smooth and uniformly elliptic with the axis interior by
[[lem:class-leaf]] (b), which holds at every graph. (iii) Derivatives transverse to the disc are taken in z0 and τ in
place of the value of ů_A and τ. They commute with L_V up to operators of lower order with smooth coefficients, as h_V is
smooth in (τ, z0, y) by (o) on each slice and the smooth dependence of V on τ; the change of variables (z0, y) ↦
(h_V(|y|; z0), y) has Jacobian ∂_(z0) h_V ∈ [1/2, 3/2]. (iv) At a point x, with σ_W(z0, y) := σ[W] at (h_W(|y|; z0), y),

    σ[U](x) − σ[V](x) = (σ_U − σ_V)(z0^U(x), y) + (σ_V(z0^U(x), y) − σ_V(z0^V(x), y)),

and by [[eq:class-leaf-lipschitz]] |z0^U(x) − z0^V(x)| ≤ 2 |δh(y; z0^U(x))|: the shift of the foliation enters as (∂_(z0)
σ_V)(z0^U(x) − z0^V(x)) up to a quadratic remainder, the derivative falling on V. (v) The balls are about V; the sup
norms of the coefficients of L_U on 𝔅′ are bounded by [[lem:sobolev]] and by step (3) of the proof of
[[lem:class-planar-shear]], with sup |∂h| ≤ C r from [[lem:class-volterra]] for U in place of the bound through −∂_y
u/∂_z u. For U ∈ 𝔅′ the leaves of U exist and foliate 𝒰_(r_V/8) by (o) for U, the C² norms of g and the C¹ norms of p_A,
Θ_A being within C 𝒩_(k−1)^V(U) of those of V by [[lem:sobolev]] (k − 4 ≥ 2).

(b′) Apply Steps 1–3 of (o) to U and to U′; they use only the bounds named in (b′) and give r_V, C_0, C_1, C_2, δ_p for
both, depending only on 𝔐 and c. In addition |∂_z G(r, z, q)| ≤ C_3 (r + |q|³) for |q| ≤ δ_p, for G built from either
state: G(0, z, q) = −A3 q³/B3 by the proof of [[lem:class-volterra]], so ∂_z G(0, z, q) = −∂_z(A3/B3) q³, and ∂_r ∂_z G
is bounded by the C³ norms of g and the C¹ norms of p_A, Θ_A. Along a leaf |q| = |h′| ≤ C_0 r, so there |∂_z G| ≤ C_4 r
and |∂_q G| ≤ C_4 r with C_4 := C_3 (1 + C_0³ r_V²) + C_2 (1 + C_0).

*One leaf.* Fix z0 and let h := h_U(·; z0), h̃ := h_(U′)(·; z0), δh := h − h̃, δw := h′ − h̃′ (so δh(0) = 0) and ω(r)
:= |δw(r)|/r, which is bounded since |δw| ≤ 2C_0 r. Subtracting the two Volterra equations, and writing the difference of
the integrands as G_U − G_(U′) at (ρ, h(ρ), h′(ρ)) plus G_(U′)(ρ, h(ρ), h′(ρ)) − G_(U′)(ρ, h̃(ρ), h̃′(ρ)),

    r δw(r) = ∫_0^r (ρ F(ρ) + θ_1(ρ) δh(ρ) + θ_2(ρ) δw(ρ)) dρ,      |θ_1|, |θ_2| ≤ C_4 ρ,

where |F(ρ)| ≤ C |U − U′| at the point (h(ρ), ρ) of the leaf of U: H_L[U] − H_L[U′] there is bounded by C |U − U′|, since
H_L holds Θ_A, p_A and the metric with its first derivatives, and E_L(ρ, z, q) for the two metrics differs by at most C
(ρ + |q|³) times the difference of the 1-jets of γ3, its value at ρ = 0 being A3 q³/B3. As |δh(ρ)| ≤ ∫_0^ρ t ω(t) dt,

    ω(r) ≤ 𝒜|F|(r) + C_4 (T_1 ω + T_2 ω)(r),   𝒜f(r) := r⁻² ∫_0^r ρ f dρ,   T_1 ω(r) := r⁻² ∫_0^r ρ² ∫_0^ρ t ω dt dρ,
    T_2 ω(r) := r⁻² ∫_0^r ρ² ω dρ.

On L²(r dr; [0, R]): 𝒜f(r) = ∫_0^1 s f(rs) ds and ‖f(·s)‖ ≤ s⁻¹ ‖f‖ give ‖𝒜f‖ ≤ ‖f‖, as in [[prop:class-flat-model]] (b);
T_2 ω(r) = r ∫_0^1 s² ω(rs) ds gives ‖T_2 ω‖ ≤ (R/2) ‖ω‖; and |∫_0^ρ t ω dt| ≤ (ρ/√2) ‖ω‖ by the Cauchy–Schwarz
inequality, so |T_1 ω(r)| ≤ (r²/(3√2)) ‖ω‖ and ‖T_1 ω‖ ≤ R³ ‖ω‖. With C_4 (R/2 + R³) ≤ 1/2,

    ‖ω‖_(L²(r dr; [0,R])) ≤ 2 ‖F‖_(L²(r dr; [0,R])),      |δh(r)| ≤ √2 r ‖F‖_(L²(r dr; [0,R])),      |δw| ≤ R ω.

Let δ_𝔐 := min(R_0/2, r_V/8, 1/(3C_0), ρ1(p)/16) with C_4 (R_0/2 + R_0³) ≤ 1/2, and take R := 2δ ≤ R_0.

*The shear.* By [[eq:class-shear-leaf]] and [[eq:class-leaf-volterra]], σ = 2 |p_A^Σ| σ_L − p_A(n)(K_Σ(e_r, e_r) −
K_Σ(e2, e2)) with σ_L = ½ H_L − k_φ, k_φ = ν^r/r + ½ ν(log B3) and ν^r = −(C3 r + A3 h′)/(det₂^(1/2) N_L): at a point of
a leaf, σ is a smooth function of the point, of h′, of h′/r and of the values of Θ_A, p_A and of the metric with its
first derivatives there, with derivatives bounded in terms of 𝔐 and c. Let x = (h(|y|), y) be the point of the leaf of U
over y and x̃ = (h̃(|y|), y). Then |σ[U](x) − σ[U′](x̃)| ≤ C (|δw| + ω + |U − U′|(x) + |δh|), the last term from moving
the point of evaluation of U′, whose 1-jet is Lipschitz with constant 𝔐. Let z0′ be the axis point of the leaf of U′
through x. By [[eq:class-leaf-lipschitz]] for U′, |z0′ − z0| ≤ 2 |δh(|y|)|. Along the leaves of U′ through (ζ, y), the
position and h′ are Lipschitz in ζ by Step 2, and so is h′/r: by Step 2 and |∂_z G|, |∂_q G| ≤ C_4 ρ, |Δh′(r)|/r ≤ r⁻²
∫_0^r C_4 ρ (|Δh| + |Δh′|) dρ ≤ C_4 (3/2 + 4C_1) |Δζ|. So σ[U′] on the leaf with axis point ζ, over y, is Lipschitz in ζ
with a constant depending only on 𝔐 and c, and |σ[U′](x) − σ[U′](x̃)| ≤ C |δh(|y|)|. Hence

    ‖σ[U] − σ[U′]‖_(L²(𝔻_δ)) ≤ C ‖F‖_(L²(r dr; [0,2δ])) + C ‖(U − U′)(h(|y|), y)‖_(L²(𝔻_δ)),

the L² norms over the leaf of U, in the variable y; the norm of F is at most C times the L² norm of U − U′ on that leaf
over 𝔻_(2δ).

*All leaves.* For x ∈ D ∩ 𝒰_δ the axis point z0 of the leaf of U through x satisfies |z0 − z(p)| ≤ δ + C_0 δ², and over
𝔻_(2δ) that leaf lies in D, by the hypothesis on D, and in 𝒰_(2δ), as |h − z(p)| ≤ δ + 3C_0 δ² ≤ 2δ. In the slice, for
G-invariant functions, the L² norm over a G-invariant set is the L² norm in (z, y) with the weight 2π ρ1, and ρ1 ∈
[ρ1(p)/2, 2ρ1(p)] on 𝒰_(2δ). For fixed y, z0 ↦ h_U(|y|; z0) is increasing with difference quotients in [1/2, 3/2], so ∫
f(z, y) dz = ∫ f(h_U(|y|; z0), y) ∂_(z0) h_U dz0 with ∂_(z0) h_U ∈ [1/2, 3/2] almost everywhere. Squaring the bound of
one leaf, integrating over z0 and changing variables on both sides gives [[eq:class-leaf-wise]]. ∎

### Block B. The new section of chapter 83

### Developments of data of any size through the axes {#sec:civp-axes}

The developments of [[sec:loc-cone-proof]] and [[sec:civp-large]] take cone data equal to the background's near the axes,
and those of [[pending:tier3-section]] take data near the background's. This section drops both conditions for the two
adapted families: cone data of any size, reaching the axes, with or without dust, have a development on a neighbourhood
of the two cones, unique in the double-null gauge, and a maximal development with a continuation criterion
([[thm:civp-axes]]). A development of the whole rectangle is not asserted: a large density can make a cone focus, and
then the cone data, and with them the developments in the gauge, do not extend past the focal sphere
([[rem:civp-axes-scope]]).

The route has four steps. First, the derivatives of the metric functions across each cone obey linear ordinary
differential equations along the generators, through the axes, when the equations are written on the sections as
equations for tensor fields ([[lem:civp-axes-principal]], [[lem:civp-axes-jets]]); so they exist and are bounded on the
whole of each cone. Second, near a corner sphere, Rendall's reduction is carried out with chapter 81's closure at the
axes, about the formal solution Û rather than about a background, for a short time; this needs the planar shear about a
state that is not a solution ([[lem:class-leaf-reference]]), and the time obtained depends only on norms of the data near
the corner ([[prop:civp-axes-corner]]). Third, two developments in the gauge agree, without smallness
([[prop:civp-axes-unique]]). Fourth, corner problems at the spheres of the cones and of null hypersurfaces of the
solution, glued by uniqueness, continue the development along the generators; no a priori estimate is used, the width of
the development being allowed to shrink ([[prop:civp-axes-faces]]).

#### Data reaching the axes {#sec:civp-axes-data}

Let γ̊ be the round metric of S³ and ∇̊ its connection. For an interval I and a function, a vector field or a symmetric
2-tensor field X on S³ depending on s ∈ I, ‖X‖_(C^m(I × S³)) is the largest of the suprema of |∂_s^j ∇̊^i X|_γ̊ over j +
i ≤ m. A metric on D × S³, D a subset of the (u, v)-plane, is in *natural double-null form* if

    g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ(· − b du, · − b du),                                  {#eq:civp-axes-form}

that is g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_AB (dθ^A − b^A du)(dθ^B − b^B du) in every chart (θ^A) of S³, where for each (u,
v) the function Ω > 0, the vector field b and the Riemannian metric γ are smooth on S³, and they depend smoothly on (u,
v). Such a g is a smooth Lorentzian metric on D × S³, for which u and v are null. It is G-invariant with b = b∂_ϑ and γ =
γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2² exactly when Ω, b and γ are G-invariant, since the reflections φ_i ↦ −φ_i make an
invariant vector field a multiple of ∂_ϑ and an invariant symmetric tensor diagonal in (ϑ, φ1, φ2); off the axes it is
then [[eq:loc-double-null]]. Conversely the metric of a class solution in the gauge of [[sec:civp-large]] is in this
form: Ω² = −g(∂_u, ∂_v)/2, γ is the restriction of g to the sections and γ(b, ·) = −g(∂_u, ·) on their tangent vectors,
all smooth on D × S³ because g and the coordinate fields of the product are.

An invariant vector field vanishes at the axes: at a point of axis 2 the rotations of the (x3, x4)-plane fix the point
and act on the plane of the K2-directions without fixed vector, and the reflection in the (x1, x2)-plane through the
point reverses K1. Near axis 2, with x := ϑ, smoothness of the invariant tensors gives, as for [[eq:class-axis-metric]],
that Ω, γ_ϑ and e^(2A_c) are even smooth functions of x, that b is odd, and that e^(2A_s) = sin²x e^(2s) with s even and
γ_ϑ = e^(2s) at x = 0 (the conical condition); near axis 1 the same holds with x := π/2 − ϑ and the roles of A_c and A_s
exchanged. No step below uses these coordinate conditions: the data are tensor fields on S³, and the conditions are their
smoothness written in coordinates.

**Definition {#def:civp-axes-data}** (Cone data through the axes.) Let (u_c, v_c) be a point, λ_u, λ_v > 0, N_o := {u_c}
× [v_c, v_c + λ_v] and N_i := [u_c, u_c + λ_u] × {v_c}, the *edges*, and S_c := {(u_c, v_c)} × S³ the *corner sphere*.
*Cone data* consist of G-invariant smooth families, in the sense of [[eq:civp-axes-form]], of a function Ω > 0, a vector
field b, a Riemannian metric γ and a function q_in on N_o, and of Ω, b, γ and q_out on N_i, such that: (i) Ω, b and γ of
the two edges agree on S_c; (ii) Ric(∂_v, ∂_v) = q_in and Ric(∂_v, X) = 0 for X tangent to the sections on N_o, and
Ric(L̲, L̲) = q_out on N_i, L̲ := ∂_u + b; and (iii) q_in ≥ 0 and q_out ≥ 0. *Cone data of any sign* omit (iii). Their
*size* in C^m is the largest of ‖ln Ω‖, ‖b‖, ‖γ‖ and ‖q_A‖ in C^m of the two edges, and they are *κ-nondegenerate*, κ ∈
(0, 1], if γ ≥ κ γ̊ on both edges.

In (ii), Ric(∂_v, ∂_v) and Ric(∂_v, X) on N_o are those of any metric in natural double-null form inducing the functions
of N_o, and Ric(L̲, L̲) on N_i those of any such metric inducing the functions of N_i: off the axes they are given by
[[eq:loc-cone]] and by the last line of [[eq:loc-cone-frame-ricci]] in terms of the functions on that edge, and they are
continuous up to the axes. The free part of cone data is that of [[def:loc-cone-data]]: Ω on both edges, b on N_i, the
conformal class of γ and the densities, the corner values being arbitrary subject to (i). In the normalised form γ = ỹ²
γ̂ with μ_γ̂ = μ_γ̊, μ the Riemannian volume density, ỹ = (μ_γ/μ_γ̊)^(1/3) is a smooth positive function on S³, and by
the proof of [[prop:loc-cones]], with trace and norm of ½ ∂_v γ taken in γ, the first constraint on N_o reads

    ∂_v² ỹ − 2 ∂_v ln Ω ∂_v ỹ + (1/3)(¼ |∂_v γ̂|²_γ̂ + q_in) ỹ = 0,                        {#eq:civp-axes-raychaudhuri}

a linear ordinary differential equation along each generator with coefficients smooth on S³, axis generators included; on
N_i with b = 0 the constraint is the same equation with u in place of v. Positivity of ỹ on an edge is the absence of a
focal sphere there. The constraint Ric(∂_v, X) = 0 is a linear first-order equation for ∂_v b along the generators, with
the leading coefficient (1/(4Ω²)) γ(∂_v ·, X) (the second line of [[eq:loc-cone]]).

A *class solution in the gauge* on D × S³, for a set D of the (u, v)-plane, is as in [[sec:civp-large]]: a smooth class
solution (g, v, u, q_in, q_out) of [[eq:class-system]] with N_f = 2, v the phase of the density q_in and u that of q_out,
whose metric is in natural double-null form. It *induces* cone data on edges contained in D if its functions Ω, b, γ and
the densities restrict to them. A set D is a *past set* relative to (u_c, v_c) if [u_c, u] × [v_c, v] ⊂ D for every (u,
v) ∈ D. Every statement below holds for cone data of any sign, a class solution in the gauge being then read as one whose
densities may take either sign; the densities of the solutions constructed are nonnegative at the points whose past on
the cones carries nonnegative data, by the argument on the signs in the proof of [[lem:loc-cone-constraints]].

#### The derivatives across the edges {#sec:civp-axes-jets}

**Lemma {#lem:civp-axes-principal}** (The equations across an outgoing edge.) Let g be a metric in natural double-null
form on {0 ≤ u < ε} × I × S³, I an interval of v, smooth up to u = 0, q_in and q_out any functions, E := Ric(g) − q_in dv
⊗ dv − q_out du ⊗ du and ℰ := (E(L̲, ∂_v), E(L̲, ·), E(·, ·)), the last two restricted to vectors tangent to the
sections: for each (u, v) a function, a 1-form and a symmetric 2-tensor field on S³. Put J_j := ∂_u^j (Ω, b, γ) at u = 0,
for j ≥ 0.

(a) ℰ contains no second u-derivative of Ω, b, γ, and does not contain q_in or q_out. So for j ≥ 1, ∂_u^(j−1) ℰ at u = 0
is a smooth expression in J_0, …, J_j and their derivatives along N_o := {0} × I × S³ of order at most two.

(b) For j ≥ 2 it is affine in J_j: ∂_u^(j−1) ℰ|_(u=0) = 𝔏_j J_j + 𝔖_j, with 𝔖_j depending on J_0, …, J_(j−1) only and,
for J = (ω, β, h),

    𝔏_j J = (−(2/Ω) ∂_v ω − ½ tr_γ ∂_v h, −(1/(4Ω²)) γ(∂_v β, ·), (1/(2Ω²)) ∂_v h) + 𝔏_j′ J,   {#eq:civp-axes-principal}

Ω and γ those of J_0. The operator 𝔏_j′ contains no ∂_v. Its first and third components are linear in (ω, β, h) at each
point, with no derivative on S³; its second component contains derivatives on S³ of order at most one of ω and h and none
of β. The coefficients are smooth on N_o, axes included, and built from J_0, J_1 and their first derivatives.

(c) If g is G-invariant, then (b) holds also for j = 1, the coefficients of 𝔏_1 being built from J_0 alone, and for j ≥ 1
the first and third components of ∂_u^(j−1) ℰ|_(u=0) do not depend on the β-component of J_j.

*Proof.* (a), (b) Work in coordinates (u, v, θ^A), (θ^A) any chart of S³. The components of g are g_uv = −2Ω², g_uA =
−γ_AB b^B, g_uu = γ_AB b^A b^B, g_AB = γ_AB and g_vv = g_vA = 0, and since g(L̲, ∂_v) = −2Ω², g(L̲, L̲) = g(L̲, ∂_A) = 0
and g(∂_v, ∂_v) = g(∂_v, ∂_A) = 0, the inverse metric is −(2Ω²)⁻¹ (L̲ ⊗ ∂_v + ∂_v ⊗ L̲) + γ^AB ∂_A ⊗ ∂_B: g^uu = g^uA =
g^vv = 0, g^uv = −1/(2Ω²), g^vA = −b^A/(2Ω²), g^AB = γ^AB. From the Christoffel symbols,

    Ric_μν = ½ g^αβ (∂_α∂_μ g_βν + ∂_α∂_ν g_βμ − ∂_μ∂_ν g_αβ − ∂_α∂_β g_μν) + Q_μν,

with Q_μν a polynomial in g^αβ and the first derivatives of the g_αβ, quadratic in the latter. A term ∂_u∂_u g_·· can
arise from the first sum only with α = μ = u, then β = v and ν = u, as g^uβ ≠ 0 only for β = v and g_vν ≠ 0 only for ν =
u; from the second only with μ = ν = u; from the third only with μ = ν = u; and the fourth would need g^uu ≠ 0. So ∂_u²
occurs only in Ric_uu, which is not in ℰ: E(L̲, ∂_v) = E_uv + b^A E_Av and E(L̲, ∂_A) = E_uA + b^B E_BA, and T(L̲, ∂_v) =
T(L̲, ∂_A) = T(∂_A, ∂_B) = 0 because dv(L̲) = du(∂_v) = du(∂_A) = dv(∂_A) = 0. Every term of ℰ is therefore a product of
factors each containing at most one u-derivative, and ∂_u^(j−1) at u = 0 produces u-derivatives of order at most j. J_j
appears only where all j − 1 derivatives fall on one factor that already contains ∂_u; for j ≥ 2 at most one factor of a
term can receive them, so the dependence on J_j is affine, through ∂_u ∂_v g, ∂_u ∂_A g and ∂_u g at u = 0, the
components of ∂_u^j g being J_j-linear modulo lower jets.

The ∂_u∂_v- and ∂_u∂_C-terms are read off the four sums, with the inverse metric above. In Ric_AB only the fourth sum
with (α, β) = (u, v), (v, u) contributes, giving (1/(2Ω²)) ∂_u∂_v γ_AB, and there is no ∂_u∂_C-term: the first two sums
with α = u need g_vB = 0, the fourth with (α, β) = (u, C) needs g^uC = 0. In Ric_uv the four sums contribute (1/(2Ω²) +
1/(2Ω²) − 1/Ω² − 1/Ω²) ∂_u∂_v Ω² − ½ γ^CD ∂_u∂_v γ_CD and no ∂_u∂_C-term, and Ric_Av contains no second derivative with a
u at all (its first sum needs β = u, α = v; its second α = u, β = v and g_vA = 0; its fourth vanishes as g_Av ≡ 0). In
Ric_uA the first sum gives (1/(4Ω²)) ∂_u∂_v b_A − (b^C/(4Ω²)) ∂_u∂_v γ_CA + ½ γ^DC ∂_D∂_u γ_CA, b_A := γ_AC b^C, the
second (1/(2Ω²)) ∂_u∂_A Ω², the third −(1/Ω²) ∂_u∂_A Ω² − ½ γ^CD ∂_u∂_A γ_CD, and the fourth −(1/(2Ω²)) ∂_u∂_v b_A. With
∂_u∂_v b_A = γ_AC ∂_u∂_v b^C + b^C ∂_u∂_v γ_AC modulo products of first derivatives, and b^B times the term of Ric_BA,

    E(L̲, ∂_A) = −(1/(4Ω²)) γ_AC ∂_u∂_v b^C + ½ γ^CD (∂_D∂_u γ_CA − ∂_A∂_u γ_CD) − (1/(2Ω²)) ∂_u∂_A Ω²
                + (terms with at most first derivatives),
    E(L̲, ∂_v) = −(2/Ω) ∂_u∂_v Ω − ½ γ^CD ∂_u∂_v γ_CD + (terms with at most first derivatives),
    E(∂_A, ∂_B) = (1/(2Ω²)) ∂_u∂_v γ_AB + (terms with no second derivative containing ∂_u).

Applying ∂_u^(j−1) at u = 0 gives [[eq:civp-axes-principal]] and the statements on 𝔏_j′: derivatives on S³ of J_j arise
only from the ∂_u∂_C-terms, which occur only in the second component and hold Ω and γ only; the terms with at most first
derivatives give zero-order terms in J_j. Every coefficient is a polynomial in the components of g, of the inverse metric
and of their derivatives at u = 0 in the chart, so smooth on N_o; it is independent of the chart, the components of ℰ
being tensorial on the sections.

(c) Off the axes, in the class, the components of ℰ are linear combinations of E(L̲, ∂_v), E(L̲, ∂_ϑ), E(∂_ϑ, ∂_ϑ) and
E(K_i, K_i), the others vanishing by the reflections, and [[eq:loc-cone-frame-ricci]] gives them explicitly in terms of
ln Ω, the ϰ_i and b. Each of their monomials contains at most one factor among L̲ ln Ω, L̲ϰ_i (in χ̲_i and tr χ̲), ∂_v L̲
ln Ω, ∂_v L̲ϰ_i, L̲∂_v b, ∂_ϑ L̲ ln Ω and ∂_ϑ L̲ϰ_i; with L̲ = ∂_u + b∂_ϑ these are affine in the first u-derivatives at
u = 0. And ∂_u b and ∂_u ln Ω do not occur in E(∂_ϑ, ∂_ϑ) and E(K_i, K_i), nor ∂_u b in E(L̲, ∂_v). So off the axes, for
invariant g, ℰ|_(u=0) − 𝔏_1 J_1 − 𝔖_1 = 𝔔(J_1, J_1) vanishes, where 𝔏_1 is the operator of [[eq:civp-axes-principal]]
with coefficients from J_0 and 𝔔 the quadratic part, a pointwise quadratic form with smooth coefficients; at the axes
𝔔(J_1, J_1) vanishes by continuity, J_1 being a smooth section. For j ≥ 1 the β-component of J_j enters the first and
third components through ∂_u b only, after j − 1 further derivatives, so not at all off the axes; at the axes the
β-component of the invariant J_j vanishes. ∎

On an ingoing edge {v = 0} with b = 0 there, put ψ_(u,v) for the flow of the vector field b(·, v, ·) on S³ in the
variable u from 0, which commutes with G, and θ̃ := ψ_(u,v)⁻¹(θ). Then dθ − b du = Dψ (dθ̃ − b̃ dv) with b̃ := −Dψ⁻¹ ∂_v
ψ, and g = −2Ω̃² (du ⊗ dv + dv ⊗ du) + γ̃(· − b̃ dv, · − b̃ dv) with Ω̃ := Ω ∘ ψ and γ̃ := ψ^*γ: the form
[[eq:civp-axes-form]] with u and v exchanged, equal to the given one on {v = 0}, where ψ = id. The lemma applies there
with u and v exchanged, and the v-derivatives at v = 0 of (Ω, b, γ) and of (Ω̃, b̃, γ̃) determine one another: ∂_v ψ =
−Dψ b̃ with ψ = id at v = 0, b = (∂_u ψ) ∘ ψ⁻¹, Ω = Ω̃ ∘ ψ⁻¹ and γ = ψ_*γ̃.

**Lemma {#lem:civp-axes-jets}** (The derivatives across the edges through the axes.) Let cone data of any sign be given
on edges N_o = {0} × [0, λ_v] and N_i = [0, λ_u] × {0}, with b = 0 on N_i. There are unique sequences a_j (j ≥ 0) on N_o
and b_k (k ≥ 0) on N_i of G-invariant smooth families of a function, a vector field and a symmetric 2-tensor field on S³,
with a_0 and b_0 the data, together with unique invariant smooth densities a_j^ρ, b_k^ρ (of q_in μ_γ and q_out μ_γ), such
that for every metric g in natural double-null form near N := N_o ∪ N_i with ∂_u^j (Ω, b, γ) = a_j on N_o and ∂_v^k (Ω,
b, γ) = b_k on N_i for all j, k, and densities with the corresponding derivatives, the evolution components ℰ of
[[lem:civp-axes-principal]] on N_o, the corresponding components with u and v exchanged on N_i, and the conservation laws
vanish to infinite order on N. Moreover:

(i) (Linear and triangular.) For j ≥ 1, a_j = (ω, β, h) solves along each generator of N_o the linear system 𝔏_j a_j =
−𝔖_j: a linear ordinary differential equation in v for (ω, h) at each point of S³, followed by one for β whose
inhomogeneous term contains (ω, h) and their first derivatives on S³; the initial values at v = 0 are the u-derivatives
of the data of N_i at the corner. The same holds on N_i, in the form of [[lem:civp-axes-principal]] with u and v
exchanged. No Riccati term occurs at any order, and the a_j exist on the whole of N_o and the b_k on the whole of N_i,
whatever their lengths.

(ii) (Corner.) ∂_v^k a_j = ∂_u^j b_k on S_c for all j, k.

(iii) (Bounds.) If the data have size at most Λ in C^m on edges of length at most 1 and are κ-nondegenerate, then for 4j
≤ m, ‖a_j‖_(C^(m−4j)) + ‖b_j‖_(C^(m−4j)) ≤ C_j, with C_j depending only on j, m, Λ and κ.

(iv) (Solutions.) Every class solution in the gauge on D × S³, D ⊃ N a past set relative to (0, 0) containing a
neighbourhood of N in it, that induces the data has ∂_u^j (Ω, b, γ) = a_j on N_o and ∂_v^k (Ω, b, γ) = b_k on N_i, and
the corresponding densities.

(v) a_j on N_o ∩ {v ≤ v′} depends only on the data on N_o ∩ {v ≤ v′} and on the derivatives at the corner of the data of
N_i, and b_k on N_i ∩ {u ≤ u′} only on the data on N_i ∩ {u ≤ u′} and the derivatives at the corner of the data of N_o.

*Proof.* *Existence and uniqueness on N_o.* Induction on j. For j ≥ 1, given a_0, …, a_(j−1), [[lem:civp-axes-principal]]
(b), (c) turns ∂_u^(j−1) ℰ|_(u=0) = 0, for invariant a_j, into the system 𝔏_j a_j = −𝔖_j: by [[eq:civp-axes-principal]]
the first and third components form a linear system for (ω, h) whose v-derivatives have the invertible coefficient matrix
((−2/Ω, −½ tr_γ), (0, (1/(2Ω²)) id)), with no derivative on S³ and no β; the second is then a linear equation for γ(∂_v
β, ·)/(4Ω²) with coefficients and an inhomogeneous term smooth on N_o. Linear ordinary differential equations with smooth
coefficients have unique solutions on the whole interval, depending smoothly on the point of S³ and on v; the solution
with the initial values ∂_u^j b_0 at the corner is invariant, since the system is natural and commutes with G and the
data are invariant, so its image under each element of G solves it with the same initial values. Conversely every
invariant a_j with ∂_u^(j−1) ℰ|_(u=0) = 0 solves this system. For the densities put ρ_in := q_in μ_γ and ρ_out := q_out
μ_γ: by [[lem:loc-cone-ricci]] (b), written in a chart, the conservation laws are ∂_u ρ_in + ℒ_b ρ_in = 0 and ∂_v ρ_out =
0 for these densities on S³, so ∂_u^j ρ_in at u = 0 is ∂_u^(j−1) of −ℒ_b ρ_in, a polynomial in lower jets, and ∂_u^j
ρ_out is constant along each generator, with its value at the corner given by the data of N_i.

*On N_i* the same, in the form with u and v exchanged given before the lemma, with the generators of N_i, the integral
curves of ∂_u (b = 0 there), and the initial values at u = 0 the v-derivatives of the data of N_o at the corner; the
change of form is smooth through the axes, ψ commuting with G.

*Vanishing to infinite order.* For g as in the statement, ∂_u^(j−1) ℰ vanishes on N_o for every j ≥ 1 and the
corresponding derivatives on N_i; all their derivatives along N then vanish, and so ℰ and the components on N_i vanish to
infinite order on N; likewise the conservation laws.

(ii) Off the axes the a_j and b_k solve the equations of the proof of [[lem:loc-cone-jets]] with the same initial values,
and that proof, being local in ϑ, applies at every ϑ ∈ (0, π/2) to cone data of any sign; so they are the sequences
constructed there on N ∩ {0 < ϑ < π/2}, and (ii) holds there by [[lem:loc-cone-jets]] (i). At the axes it holds by
continuity.

(iii) For a linear system ∂_v Z = MZ + h on an interval of length at most 1, ‖Z‖_(C^r) ≤ C(r, ‖M‖_(C^r))(‖Z(0)‖_(C^r) +
‖h‖_(C^r)), by differentiating with ∇̊ and in v. With Ω ≥ e^(−Λ) and γ ≥ κγ̊ the leading coefficients of
[[eq:civp-axes-principal]] have inverses bounded in terms of Λ and κ, and the induction of the proof of
[[lem:loc-cone-jets]] (iii), with the data in place of their differences from a background, gives the bound: 𝔖_j holds
derivatives of order at most two of a_0, …, a_(j−1), and the β-equation one derivative on S³ of (ω, h).

(iv) Such a solution satisfies E = 0 and the conservation laws on D, hence their derivatives of every order on N by
continuity; its derivatives across N are invariant and solve the systems above with the same initial values.

(v) The systems on N_o at the points with v ≤ v′ involve the data there and the initial values at v = 0 only. ∎

The loss of four derivatives per order in (iii) is that of [[lem:loc-cone-jets]] (iii). On a cone of finite length the
derivatives across it of every order are bounded, by smoothness on the compact edge; their bounds grow at most
exponentially in its length, by Gronwall's inequality.

**Lemma {#lem:civp-axes-extension}** (Extending and normalising cone data.) Let m ≥ 1. Constants C_m depend only on m.

(a) (Past an end.) Let w ∈ (0, 1] and f a smooth family on [−w, 0] × S³ of functions, vector fields or symmetric 2-tensor
fields on S³. There is a smooth family F on [−w, 1] × S³ with F = f on [−w, 0] and ‖F‖_(C^m([−w,1]×S³)) ≤ C_m w^(−m)
‖f‖_(C^m([−w,0]×S³)), depending linearly on f and G-invariant when f is.

(b) (Short pieces.) Let f be a smooth family on [0, w] × S³, w > 0, let Λ bound |∇̊^i ∂_s^j f| at s = 0 for i, j ≤ m, and
let L bound |∇̊^i ∂_s^(m+1) f| on [0, w] × S³ for i ≤ m. For 0 < a ≤ min(w, 1/2, 1/(1 + L)) there is a smooth family F on
[0, 1] × S³, G-invariant when f is, with F = f on [0, a], F = Σ_(j≤m) ∂_s^j f(0) s^j/j! on [2a, 1], and
‖F‖_(C^m([0,1]×S³)) ≤ C_m (Λ + 1).

(c) (Solving the constraints past an end.) Let cone data of any sign, κ-nondegenerate and of size at most Λ in C^m, be
given on edges N_o = {0} × [0, λ_v] and N_i = [0, λ_u] × {0}, λ_u, λ_v > 0, with b = 0 on N_i. On each edge let ln Ω, the
density, and γ̂ := (μ_γ̊/μ_γ)^(2/3) γ be extended to smooth invariant families on [0, λ + 1] (λ the length of the edge)
with C^m norms at most Λ, γ̂ positive definite with μ_γ̂ = μ_γ̊, and keep b = 0 on the extension of N_i. There are ℓ ∈
(0, 1], C and κ′ > 0, depending only on m, Λ and κ, such that solving the constraints from the corner with the given
corner values gives cone data of any sign on {0} × [0, λ_v + ℓ] and [0, λ_u + ℓ] × {0}, equal to the given data on N_o
and N_i, of size at most C in C^(m−3), κ′-nondegenerate, and with these free functions.

(d) (The shift on the ingoing edge.) For cone data with any b on N_i, let ψ_u be the flow on S³ of the vector fields b(u,
0, ·): ∂_u ψ_u = b(u, 0, ψ_u), ψ_0 = id. The change of coordinates θ = ψ_u(θ′), independent of v, carries every metric in
natural double-null form to one in natural double-null form, with Ω′ = Ω ∘ ψ_u, γ′ = ψ_u^* γ and b′ = ψ_u^*(b(u, v, ·) −
b(u, 0, ·)). It commutes with G, it is the identity on N_o except that b becomes b − b(0, 0, ·) there, and b′ = 0 on N_i.
The new functions on the edges are cone data, of size in C^m bounded by C_m times a function of the size of the old ones
in C^(m+1), and κ-nondegeneracy becomes κ″-nondegeneracy with κ″ depending only on κ and that size. A class solution in
the gauge for the new data gives one for the old data by the inverse change.

*Proof.* (a) By [LY22, Theorem 1 (i)] ([[thm:std-ly-extension]]) there are numbers a_j and b_j > 0, j ∈ ℤ, with Σ_j a_j
(−b_j)^i = 1 and A_i := Σ_j |a_j| b_j^i < ∞ for every integer i ≥ 0; the second follows from Σ_j 2^(δ_i|j|) |a_j| b_j^i <
∞. Let χ be smooth on ℝ with χ = 1 on [−1/3, 0] and χ = 0 on (−∞, −2/3], put f_1(s) := χ(s/w) f(s) for −w ≤ s ≤ 0 and f_1
:= 0 for s < −w, and F(s) := f(s) for s ≤ 0 and F(s) := Σ_j a_j f_1(−b_j s) for s > 0. The series of the derivatives
∂_s^i ∇̊^α converge uniformly, since |∂_s^i ∇̊^α (f_1(−b_j s))| ≤ b_j^i sup |∂^i ∇̊^α f_1|, so F is smooth on (0, 1]
with |∂_s^i ∇̊^α F| ≤ A_i sup |∂^i ∇̊^α f_1|, and as s → 0⁺, ∂_s^i ∇̊^α F → Σ_j a_j (−b_j)^i ∂^i ∇̊^α f(0) = ∂^i ∇̊^α
f(0), χ being 1 near 0; so F is smooth on [−w, 1]. The derivatives of χ(s/w) of order i are at most C w^(−i). F is linear
in f and acts at each point of S³, so it commutes with G.

(b) Let P(s) := Σ_(j≤m) ∂_s^j f(0) s^j/j!, so ‖P‖_(C^m([0,1]×S³)) ≤ C_m Λ, and g := f − P on [0, w]. Every ∇̊^α g
with |α| ≤ m has vanishing s-derivatives of order at most m at s = 0, and ∂_s^(m+1) P = 0, so by Taylor's formula |∂_s^i
∇̊^α g(s)| ≤ L s^(m+1−i) for i ≤ m. Apply (a) to s ↦ g(a + s), −a ≤ s ≤ 0, with w := a, and multiply the extension by
ψ((s − a)/a), ψ smooth with ψ = 1 on (−∞, 1/2] and ψ = 0 on [1, ∞): the result g_e equals g on [0, a] and vanishes for s
≥ 2a. In (a) the bound is A_i sup |∂^i ∇̊^α f_1| with f_1 = χ((s − a)/a) g, at most C_m Σ_(i′≤i) a^(−(i−i′)) L a^(m+1−i′)
≤ C_m L a^(m+1−i), and the cut-off ψ costs the same powers of a; so ‖g_e‖_(C^m([0,1]×S³)) ≤ C_m L a ≤ C_m. Put F := P +
g_e.

(c) The proof of [[lem:loc-cone-extension]] holds with the following changes. The free functions are the given
extensions, not Borel sums at the end, and are not measured against a background; ϕ and ℓ_i are replaced by ỹ and γ̂, and
(∗) there by [[eq:civp-axes-raychaudhuri]], whose coefficients have C^(m−1) norms at most C(Λ). On the given edges ỹ =
(μ_γ/μ_γ̊)^(1/3) ≥ κ^(1/2) and |∂ ln ỹ| ≤ C(Λ), so the Gronwall bound there keeps ỹ ≥ ỹ(λ)/2 on [λ, λ + ℓ] for ℓ
depending only on m, Λ and κ; with ỹ ≤ C(Λ), γ = ỹ² γ̂ and the C¹ bound of γ̂, γ ≥ κ′ γ̊ after decreasing ℓ. The second
constraint on N_o is linear in b, through ∂_v b and ∂_v² b, off the axes by the second line of [[eq:loc-cone]] and at the
axes by continuity, its leading coefficient being (1/(4Ω²)) γ(∂_v ·, X); solving it from the corner values loses the
derivatives counted there, and the size of the extension is at most C in C^(m−3).

(d) dθ = Dψ_u dθ′ + b(u, 0, ψ_u) du, so dθ − b(u, v, θ) du = Dψ_u (dθ′ − b′ du) with b′ as stated, and γ(Dψ_u ·, Dψ_u
·) = ψ_u^* γ. ψ_u commutes with G because b is invariant, and ψ_0 = id. The constraints are components of the Ricci
tensor of the same metric along the same generators: ∂_v at fixed θ′ is ∂_v at fixed θ, and on N_i, ∂_u at fixed θ′ is
L̲. The bounds follow from those of ψ_u, whose derivatives of order m are bounded by the derivatives of b of order at
most m. ∎

**Proposition {#prop:civp-axes-formal}** (The formal solution through the axes.) Let the data of [[lem:civp-axes-jets]]
have size at most Λ in C^m, m ≥ 6k + 18, on edges of length λ_u, λ_v ∈ [λ_0, 1], be κ-nondegenerate, and let 0 < δ_e ≤
1/8. Extend a_0 to v ∈ [−1, 0] and b_0 to u ∈ [−1, 0] by [[lem:civp-axes-extension]] (a), and put X_0(u, v) := a_0(v) +
b_0(u) − a_0(0). There are G-invariant smooth families X̂ = (Ω̂, b̂, γ̂) and ρ̂_in, ρ̂_out on 𝒮_e := [−1, λ_u] × [−1,
λ_v] with ∂_u^j X̂ = a_j on N_o and ∂_v^k X̂ = b_k on N_i for all j, k, likewise for the densities, such that, with
constants depending only on k, Λ, κ and λ_0 unless stated otherwise:

(a) ‖X̂‖_(C^(k+3)(𝒮_e)) ≤ C, C depending also on δ_e;

(b) |X̂ − X_0| ≤ C_b (|u| + |v|) on 𝒮_e, and |b̂| ≤ C_b |v| where u ≥ 2δ_e, with C_b not depending on δ_e;

(c) at the points of 𝒮_e with |u|, |v| ≤ d, and at those within distance d of N, for a number d > 0, Ω̂ ≥ e^(−Λ)/2 and γ̂
≥ (κ/2) γ̊; there the metric Ĝ of [[eq:civp-axes-form]] with the functions X̂ is a smooth G-invariant Lorentzian metric
for which u and v are null, and Ĝ, q̂_in := ρ̂_in/μ_γ̂ and q̂_out := ρ̂_out/μ_γ̂ induce the data on N;

(d) E := Ric(Ĝ) − q̂_in dv ⊗ dv − q̂_out du ⊗ du and the conservation laws vanish to infinite order on N.

*Proof.* Apply [[lem:loc-cone-borel]] to the components of a_j − ∂_u^j X_0 and b_k − ∂_v^k X_0, which agree at the corner
by [[lem:civp-axes-jets]] (ii) and vanish for j = 0 and k = 0, in the Cartesian components on ℝ⁴ ⊃ S³ of tensor fields on
S³, with Y replaced by S³, r := k + 3, ε_0 := δ_e and γ_0 := 1, and add X_0. That proof uses Y only as a parameter set,
the Borel sums being taken in u and v with cut-offs depending on u and v alone; so the sums are G-invariant when their
coefficients are, and the bound of its part (b) holds with ∇̊-derivatives, which gives (a) by [[lem:civp-axes-jets]]
(iii), since m − 4(k + 3) ≥ 2(k + 3). (b) is the argument of the paragraph on the reference metric in case (II) of
[[sec:loc-cone-reduced]], which uses only the form of the Borel sums: the terms of index 0 vanish on N, as the jets of
order 0 of X − X_0 vanish, every other term vanishes at u = 0 (respectively v = 0) and is at most |u| (respectively |v|)
times a bound of the jets of order at most k + 3 or 2^(−j); and b vanishes on N_i and on N_o at v = 0, so b_0 = 0
and |a_0^b(v)| ≤ Λ |v|. (c) X_0 equals the data on N, so |X_0 − X| ≤ Λ (|u| + |v|) with X the data at the nearest point
of N, Λ being replaced by the bound of the extended a_0 and b_0 in C^1, and Ω ≥ e^(−Λ), γ ≥ κ γ̊ there; with (b) this
gives (c) for d a small multiple, depending only on these bounds, of min(1, κ, e^(−Λ)). (d) The evolution components and
the conservation laws vanish to infinite order on N by [[lem:civp-axes-jets]]. The other components of E vanish to
infinite order on N by the proof of [[prop:loc-cone-formal]] (c), which uses the contracted Bianchi identity in the form
[[eq:loc-cone-bianchi]] and the constraints of the data and is local in ϑ: it applies off the axes, and at the axes by
continuity, E being a smooth tensor field. ∎

#### The corner theorem {#sec:civp-axes-corner}

**Proposition {#prop:civp-axes-corner}** (Developments near a corner sphere through the axes, without smallness.) Let k ≥
6 and m := 6k + 19. For Λ ≥ 1, κ ∈ (0, 1] and l ∈ (0, 1] there is σ ∈ (0, l/3], depending only on k, Λ, κ and l, with the
following property. Let cone data be given on edges N_o = {u_c} × [v_c, v_c + λ_v] and N_i = [u_c, u_c + λ_u] × {v_c}
with λ_u, λ_v ≥ l, with any Ω on both edges and any b on N_i, of size at most Λ in C^m and κ-nondegenerate on N_o ∩ {v ≤
v_c + l} and on N_i ∩ {u ≤ u_c + l}. Then there is a class solution in the gauge on [u_c, u_c + σ] × [v_c, v_c + σ] × S³
that induces the data on N_o ∩ {v ≤ v_c + σ} and on N_i ∩ {u ≤ u_c + σ}. The number σ depends neither on the corner, nor
on λ_u and λ_v, nor on the data at distance more than l from the corner sphere; no background and no smallness of the
data enter, and the data may differ from any background at the axes.

*Proof.* We follow case (II) of [[sec:loc-cone-reduced]], with the formal solution Û as the reference state everywhere,
with chapter 81's closure at the axes in place of the angular cut-off, and with [[thm:class-kato]] (a) about Û in place
of [[thm:class-kato-stability]] (a). Constants C below depend only on k, Λ, κ and l.

*Step 0 (Reductions).* Translate u and v so that the corner is (0, 0), and restrict the data to edges of length l. By
[[lem:civp-axes-extension]] (d) we may assume b = 0 on N_i, the size becoming at most Λ_1 in C^(m−1) = C^(6k+18) and the
nondegeneracy κ_1, both depending only on k, Λ and κ: a class solution in the gauge for the new data gives one for the
old on the same rectangle, the change of angle not depending on v.

*Step 1 (The formal solution and the constants).* Let C_b and d be the numbers of [[prop:civp-axes-formal]] (b), (c) for
Λ_1, κ_1 and λ_0 := l. By (b) there, |b̂| ≤ C_b (|u| + |v|) and |b̂| ≤ C_b |v| where u ≥ 2δ_e, with C_b independent of
δ_e; so the argument of the paragraph on the reference metric in case (II) of [[sec:loc-cone-reduced]], with |X̂ − X̊| ≤
C_b replaced by these bounds and by (c) there, gives δ_2 > 0, depending only on Λ_1, κ_1 and l, such that

    4Ĝ(∂_τ, ∂_τ) = −4Ω̂² (u + δ_c)(v + δ_c) + γ̂(b̂, b̂) (u + δ_c)² ≤ −2Ω̂² (u + δ_c)(v + δ_c)

on the set 𝒮 of [[eq:loc-cone-collar]] whenever δ_1 ≤ δ_2, ∂_τ being the field of [[eq:loc-cone-time]]. Fix δ_1 :=
min(l/3, d/4, δ_2), l_u = l_v := 2δ_1 (so that N_o and N_i have length l ≥ 3δ_1 = l_u + δ_1), c_+ := (δ_1/4)², δ_c :=
√c_+/8 = δ_1/32 and δ_e := δ_c/8, and let X̂, Ĝ, q̂_A be the formal solution of [[prop:civp-axes-formal]] for these data.
Every point of 𝒮 lies within δ_1 ≤ d of N and has |u|, |v| ≤ 3δ_1, so by (c) there Ĝ is a smooth G-invariant Lorentzian
metric on 𝒮 × S³, for which u and v are null, ∂_τ is timelike and dτ is timelike with P̂_A(τ) > 0, where P̂_A := Ĝ⁻¹p̂_A,
p̂_in := −dv and p̂_out := −du; then the block Ĝ^(ab) of the inverse metric on the dy^a is positive definite, as in that
paragraph. By (a) there ‖X̂‖_(C^(k+3)) ≤ C. Put Θ̂_A := div_Ĝ P̂_A and Û := (Ĝ, p̂_A, Θ̂_A, q̂_A).

*Step 2 (Chart, region, and the leaves of Û).* Use the chart (τ, y) of [[eq:loc-cone-time]] with this δ_c, τ_c := 2 ln
δ_c, the time of the corner sphere, τ_+ := ln c_+, and the region 𝒰 of [[eq:loc-cone-region]] with its lower end τ_init ∈
[τ_c − 1/2, τ_c] to be fixed in Step 4 (τ_c − 1/2 > ln(δ_c²/4), so the description of 𝒰 in [[sec:loc-cone-reduced]]
holds). 𝒰 is a compact subset of the interior of 𝒮 in the chart, and the pieces of its boundary other than Σ_init ∩ 𝒰 are
spacelike, with 𝒰 to their past, for Ĝ and for every Lorentzian metric C⁰-close to it. The chart is G-equivariant onto ℝ
× (ℝ⁴ ∖ {0}), and metrics in natural double-null form are smooth in it through the axes, the axes being {y3 = y4 = 0} and
{y1 = y2 = 0}. On Σ_τ := {τ = const}, (u + δ_c)(v + δ_c) = e^τ and |y| = (v + δ_c)/(u + δ_c), so u and v are functions
of |y| on each slice: every set {F(u, v) = c} ∩ Σ_τ is a round sphere {|y| = r}, among them the face sections N_o ∩ Σ_τ =
{|y| = e^τ/δ_c²} and N_i ∩ Σ_τ = {|y| = δ_c² e^(−τ)}. For τ > τ_c, F ∩ Σ_τ is the shell between them and P ∩ Σ_τ consists
of the ball inside N_i ∩ Σ_τ and the exterior of N_o ∩ Σ_τ; for τ ≤ τ_c, Σ_τ ∩ 𝒰 ⊂ P.

The p̂_A are differentials of the eikonals −v and −u of Ĝ and Θ̂_A = □_Ĝ(−u_A), u_in := v, u_out := u. So, by the last
statement of [[lem:class-leaf-differences]], whose proof uses no field equation, the leaves of Û of both families in Σ_τ
are the level sets of u and v there: the round spheres {|y| = r}. At a point of axis 2, |p̂_A(∂_z)| = |du_A(∂_r)| with
∂_r the radial field of the chart in Σ_τ, and du(∂_r) = −(u + δ_c)/(2|y|), dv(∂_r) = (v + δ_c)/(2|y|); on 𝒰 these are
bounded below by a number c_Û > 0 depending only on δ_1, and likewise at axis 1. [[lem:class-leaf-reference]] therefore
applies with V := Û on every slice, at every axis point of 𝒰, with constants depending only on C^(k+3) bounds of Û, on
c_Û and on the radius r_Û of its part (o), so only on k, Λ, κ, l. Fix δ ∈ (0, r_Û/8], also at most δ_𝔐 of its part (b′)
for 𝔐 := 1 + (the bound of 𝔐 for Û), and at most a quarter of the least distance of 𝒰 to {y = 0}; and let χ_ax be a
smooth G-invariant function of y equal to 1 where dist(y, axes) ≤ δ/2 and to 0 where dist(y, axes) ≥ δ.

*Step 3 (The modified system).* The unknowns U = (g, p_A, Θ_A, q_A), A ∈ {in, out}, and their first-order variables 𝐔 :=
(g, g_τ, g_a, p_A, Θ_A, q_A) in the chart, are those of case (II), with the reduced Ricci tensor and the gauge vector
D(g) := g^(ab) (Γ[g] − Γ[Ĝ])_(ab) relative to Ĝ, and with ζ_A := 1. (Aug1), (Aug2) and (Aug4) are as in
[[sec:class-augmented]], and (Aug3) is P_A(Θ_A) = S_A^♮, S_A^♮ := (1 − χ_ax) S_A + χ_ax S_A^ax, with S_A of
[[sec:class-augmented]], a smooth function of (g, dg, p_B, Θ_A, q_B) where dist(y, axes) ≥ δ/2, and S_A^ax the axis
closure of Step 6 of the proof of [[thm:class-stability]], built near axis 2 from κ_A1 and the planar shear σ_A[U] of the
leaves of U in Σ_τ ([[lem:class-leaf-reference]]), and near axis 1 likewise with the two circles exchanged. We write
𝒜(U) = 0 for this system; its right side at a time depends on the unknowns at that time only.

Let ξ be a smooth function of (u, v), equal to 1 on a neighbourhood 𝒰_1 of 𝒰 and supported in the interior of 𝒮 in the
chart, χ_♭ and A^μ_♭ as in case (II) with Ĝ⁻¹ and P̂_A in place of g_e⁻¹ and P̊_A (so A^μ_♭ = A^μ(x, 𝐔̂) on supp ξ), and
c_0, r_0, ϒ as there with 𝐔_c := 𝐔̂. For Z := 𝐔 − 𝐔̂ (𝐔̂ needed only on supp ξ) consider

    ξ (A^μ(x, 𝐔̂ + ϒ(Z)) ∂_μ(𝐔̂ + Z) − F^♮(x, 𝐔̂ + Z)) + (1 − ξ) A^μ_♭ ∂_μ Z = F̃,
    F̃ := 1_P ξ 𝒜(Û),                                                                          {#eq:civp-axes-modified}

where A^μ ∂_μ 𝐔 = F^♮ is the first-order form of 𝒜(U) = 0 and 𝒜(Û) := A^μ(x, 𝐔̂) ∂_μ 𝐔̂ − F^♮(x, 𝐔̂). (i) *F̃ is smooth.*
In (Aug1), Ric^H(Ĝ) = Ric(Ĝ) since D(Ĝ) = 0, so its residual is E of [[prop:civp-axes-formal]] (d); (Aug2) holds exactly,
∇_(P̂_A) p̂_A = ½ d Ĝ⁻¹(p̂_A, p̂_A) = 0; in (Aug3), for the eikonal u_A of Ĝ, the Raychaudhuri equation of the proof of
[[prop:class-structure]] (c), which holds everywhere, gives P̂_A(Θ̂_A) = −|∇²u_A|² − Ric(Ĝ)(P̂_A, P̂_A), and |∇²u_A|²
equals the expression of [[eq:class-identity]] off the axes and that of [[eq:class-x]], with σ the planar shear of the
level sets of u_A, which is σ_A[Û] by Step 2, and both extend continuously to the axes ([[prop:class-axis]] (d)); so
S_A(Û) = S_A^ax(Û) wherever both are defined and the residual of (Aug3) is −E(P̂_A, P̂_A); and (Aug4) is the conservation
law, by [[lem:loc-cone-ricci]] (b) in a chart. So 𝒜(Û) is local in Û and vanishes to infinite order on N, by
[[prop:civp-axes-formal]] (d), and 1_P ξ 𝒜(Û) is smooth. (ii) *Form.* [[eq:civp-axes-modified]] reads A^μ_ξ(x, Z) ∂_μ Z =
Φ(τ, Z) with A^μ_ξ := ξ A^μ(x, 𝐔̂ + ϒ(Z)) + (1 − ξ) A^μ_♭ symmetric and A^0_ξ ≥ c_1 I, as in [[lem:loc-cone-system]] (a),
and Φ(τ, Z) := ξ (F^♮(x, 𝐔̂ + Z) − A^μ(x, 𝐔̂ + ϒ(Z)) ∂_μ 𝐔̂) + F̃. The first and third rows of its wave block give g_τ =
∂_τ g and g_a = ∂_a g if they hold initially, as in [[lem:loc-cone-system]] (c). (iii) *The forcing.* Let ρ > 0 be so
small that, for (τ, Z) with ‖Z‖_(H^k) ≤ ρ, C_S ρ ≤ r_0 (so ϒ(Z) = Z) and the states 𝐔̂ + Z lie, at the axis points of
supp ξχ_ax, in the balls 𝔅 and 𝔅′ of [[lem:class-leaf-reference]] (a), (b) about Û and have their leaves foliating the
sets 𝒰_δ, as in Step 9 of the proof of [[thm:class-stability]]; ρ depends only on k, Λ, κ, l. On 𝒟_ρ := {‖Z‖_(H^k) ≤ ρ},
with u_* := 0, Φ satisfies (F1)–(F3): its local part by [[rem:class-kato-local]], Φ_loc(τ, x, 0) being supported in supp
ξ; and its non-local part −½ ξχ_ax (σ_A[𝐔̂ + Z]² − σ_A[Û]²) in the Θ-rows, σ_A[Û] being smooth, by
[[lem:class-leaf-reference]] (a) for (F1), with Moser's estimate ([[cor:std-moser-product]] (1)), by
[[lem:class-leaf-reference]] (b) for (F2), σ_A being bounded in L^∞ on 𝒟_ρ by (a) and [[lem:sobolev]], and by (F2) and
the smoothness in τ of Û, of ξ and of the leaves of Û for (F3).

*Step 4 (The Cauchy problem, and the time it gives).* Apply [[thm:class-kato]] (a) with d = 4, s = k, on the slab [τ_c −
1/2, τ_c + 1/2] × ℝ⁴, with u_* := 0 and the radius ρ of Step 3. Its hypotheses hold on [τ_init, τ_c + 1/2] for every
τ_init ∈ [τ_c − 1/2, τ_c] with the same bounds, as in the continuation part of its proof, and by its proof the time T* it
gives for the datum Z = 0 at τ_init depends only on c_1, ρ, C_A, the constants of [[lem:class-kato-linear]] for bounds of
order k of the A^μ_ξ on {|Z| ≤ C_S (1 + ρ)}, and the functions C_F and L of (F1), (F2): u_* = 0 enters through nothing
else, and ‖u0‖_(H^k) = 0. Each of these is bounded in terms of the C^(k+3) norm of X̂ on 𝒮, the chart and the cut-offs,
which are fixed by δ_1, and the constants of [[lem:class-leaf-reference]] for Û, so T* depends only on k, Λ, κ and l; we
may take T* ≤ 1. Put

    τ_init := τ_c − T*/2,      τ_end := τ_c + T*/2,      σ := δ_c (e^(T*/4) − 1)/2.

Σ_init ⊂ P, every point of it having (u + δ_c)(v + δ_c) < δ_c². [[thm:class-kato]] (a) gives a solution Z on [τ_init,
τ_end] × ℝ⁴ with Z(τ_init) = 0 and ‖Z(τ)‖_(H^k) ≤ ρ; it is smooth, by the argument of *Smoothness* in the proof of
[[thm:class-stability]], with [[lem:class-leaf-reference]] (a) at every order in place of [[lem:class-leaf-differences]]
(a), and G-invariant, the system and the datum being G-invariant and the solution unique. g_τ = ∂_τ g and g_a = ∂_a g
hold, as at τ_init. Below U denotes the corresponding state on 𝒰 ∩ {τ ≤ τ_end}. F ∩ {τ ≤ τ_end} lies in {u, v ≥ 0, (u +
δ_c)(v + δ_c) ≤ δ_c² e^(1/2)}, inside 𝒰 and away from its far cuts and from {τ = τ_+}, and it contains [0, 2σ]².

*Step 5 (The past of the edges).* U = Û on P ∩ 𝒰 ∩ {τ ≤ τ_end}. Indeed, on P, F̃ = ξ 𝒜(Û), so z := 𝐔 − 𝐔̂ satisfies, with
the coefficients at Û as in [[lem:loc-cone-past]],

    A^μ_ξ(x, 0) ∂_μ z = M z − ½ ξχ_ax (σ_A[U]² − σ_A[Û]²)  (in the Θ-rows),

M bounded. Let e(τ) := ∫_(P∩𝒰∩Σ_τ) ⟨A^0_ξ(x, 0) z, z⟩. The divergence theorem on the Lipschitz domain P ∩ 𝒰 ∩ {τ ≤ s}, as
in [[lem:loc-cone-past]], has nonnegative boundary terms on N, which is null for Ĝ with du(P̂_out) = dv(P̂_in) = 0 and
the other pairings positive, and on the far cuts, and z = 0 on Σ_init. For the non-local term, P ∩ 𝒰 ∩ Σ_τ has at most
two components D, each bounded near the axes by round spheres {|y| = r}, and the leaves of Û through points of D near the
axes, being such spheres, lie in D. Let 𝔼_D be the extension operator from D used in the proof of [[thm:class-stability]]
(*The adapted domain is a domain of dependence*): Stein's operator ([[thm:std-sy-extension]]) for a fixed annulus,
transported by a radial diffeomorphism of y and averaged over G. D is an annulus {r_1 < |y| < r_2} whose radii lie in a
compact subinterval of (0, ∞), with r_2/r_1 bounded below by a number larger than 1, uniformly for τ ∈ [τ_init, τ_end];
so 𝔼_D is bounded on H^σ, σ ≤ k − 1, uniformly in τ, as in the proof of [[thm:class-kato]] (b) (ii). Put Ŭ := U − 𝔼_D(U −
Û) on Σ_τ. Then Ŭ = Û on D with its first derivatives, and Ŭ lies in the ball 𝔅′ of [[lem:class-leaf-reference]] (b)
about Û, ‖Ŭ − Û‖_(H^(k−1)) ≤ (1 + C) ρ, for ρ small. For x ∈ D near the axes the leaf of Û through x lies in D, so it
solves the leaf equation of Ŭ and is the leaf of Ŭ, by the uniqueness in [[lem:class-volterra]]; so σ_A[Ŭ] = σ_A[Û] on D,
and by [[lem:class-leaf-reference]] (b)

    ‖σ_A[U] − σ_A[Û]‖_(L²(D∩𝒰_δ)) = ‖σ_A[U] − σ_A[Ŭ]‖_(L²(D∩𝒰_δ)) ≤ C ‖𝔼_D(U − Û)‖_(L²(𝒰_(2δ))) ≤ C ‖z‖_(L²(D)).

So e(s) ≤ C ∫_(τ_init)^s e, and e = 0. Hence U − Û vanishes with all its derivatives on N ∩ {τ ≤ τ_end}, U carries the
formal solution's derivatives across N, and g and the densities induce the data on N ∩ {τ ≤ τ_end}.

*Step 6 (The constraints on the slice triangle).* Let 𝒯 := F ∩ {τ ≤ τ_end}, whose slices 𝒯 ∩ Σ_τ are the shells between
the two face sections, and whose boundary consists of N ∩ {τ ≤ τ_end} and 𝒯 ∩ Σ_(τ_end). On 𝒯, ξ = 1, F̃ = 0 and ϒ(Z) =
Z, so 𝒜(U) = 0. Then g⁻¹(p_A, p_A) = 0, dp_A = 0 and p_A = −du_A on (P ∩ 𝒰) ∪ 𝒯, with u_in = v and u_out = u on P ∩ 𝒰, as
in [[lem:loc-cone-constraints]]: ν_A and dp_A are transported along P_A ([[prop:class-augmented]] (b)), and the integral
curve of P_A through a point of 𝒯, followed to the past, reaches N inside 𝒯, where they vanish by Step 5. For D and Δ_A
:= Θ_A − div_g P_A: off the axes [[prop:class-augmented]] (d), (e) give P_A(Δ_A) = −Δ_A (Θ_A + div_g P_A − 2κ_A1 −
2κ_A2) + g(∇_(P_A) D, P_A) + L(P_A, P_A), and near the axes Step 10 of the proof of [[thm:class-stability]] gives the
same with −½ Δ_A (Θ_A + div_g P_A − 2κ_A1) − ½ (σ_A[U]² − σ_A[U′]²) in place of the first term, U′ := U with Θ_A replaced
by div_g P_A; on the overlap the equation is the corresponding combination with the weights 1 − χ_ax and χ_ax, since
S_A(U′) = S_A^ax(U′) there, the leaves of U′ being the level sets of u_A. D solves [[eq:class-gauge-wave]] with B_g T =
Σ_A Δ_A q_A p_A. On N, U = Û to infinite order and div_Ĝ P̂_A = Θ̂_A, so U′ = U to infinite order there; so the face
sections, which are leaves of Û, solve the leaf equations of U and of U′ and are their leaves through their axis points,
by the uniqueness in [[lem:class-volterra]]; the leaves of U foliate the sets 𝒰_δ ([[lem:class-leaf-reference]] (o) for
U), so the leaf of U through a point of a shell 𝒯 ∩ Σ_τ near the axes lies, over 𝔻_(2δ), between the two face sections,
in the shell. So [[lem:class-leaf-reference]] (b′), with D the shell, gives

    ‖σ_A[U] − σ_A[U′]‖_(L²(𝒯∩Σ_τ∩𝒰_δ)) ≤ C ‖Δ_A‖_(L²(𝒯∩Σ_τ∩𝒰_(2δ))),

with C depending on bounds of U and U′ that hold on 𝒯, and not on the width of the shell, which tends to 0 as τ → τ_c;
the bound 𝔐 of (b′) holds for U and U′ by ‖Z‖_(H^k) ≤ ρ, k ≥ 6. The energy of [[lem:loc-cone-energy]] for z := (D, ∂_τ D,
∂_y D, Δ_in, Δ_out) on 𝒯, with B_0 := N ∩ {τ ≤ τ_end}, where z = 0 by Step 5, B_1 := 𝒯 ∩ Σ_(τ_end), and the non-local
term bounded as above, gives D = 0 and Δ_A = 0 on 𝒯. So (g, u_in, u_out, q_in, q_out) solves [[eq:class-system]] on 𝒯, in
the gauge D(g) = 0 relative to Ĝ, as in [[lem:loc-cone-constraints]]; q_A ≥ 0 there by the argument on the signs there,
the data being nonnegative.

*Step 7 (The double-null gauge).* Let θ′: 𝒰′ := (P ∩ 𝒰 ∩ {τ ≤ τ_end}) ∪ 𝒯 → S³ be constant along the integral curves of
P_out and equal to the identity on P ∩ 𝒰: as in [[lem:loc-cone-gauge]], with the past integral curves of P_out reaching P
∩ 𝒰. It is smooth through the axes and G-equivariant, P_out being smooth and G-invariant, so that its flow commutes with
G and preserves the zero sets of K_1 and K_2. Put Ψ := (u_out, u_in, θ′). In the coordinates (u′, v′, θ′) := Ψ, g⁻¹(du′,
du′) = g⁻¹(dv′, dv′) = 0 and g⁻¹du′ = −P_out annihilates the dθ′; so in every chart of S³, g^(u′u′) = g^(v′v′) =
g^(u′A) = 0, and inverting, g_(v′v′) = g_(v′A) = 0, g_(u′v′) = 1/g^(u′v′), and the (θ′, θ′)-block of g is the inverse of
that of g⁻¹: g is in natural double-null form [[eq:civp-axes-form]], with −2Ω² = 1/g^(u′v′), γ the inverse of the block
g^(AB) and b^A = g^(v′A)/g^(u′v′). Ψ and its differential are the identity on N, where g = Ĝ to infinite order, so the
functions of g in the new coordinates and the densities are the data on N.

Ψ is a diffeomorphism near the identity: d(u_out − u) = −(p_out − p̂_out), d(u_in − v) = −(p_in − p̂_in) and P_out(θ′ −
θ) = −(P_out − P̂_out)(θ) with zero values on P, and ‖Z‖_(H^k) ≤ ρ bounds 𝐔 − 𝐔̂ and its first derivatives by C_S ρ;
so |d(Ψ − id)| ≤ C ρ on 𝒯. For ρ small, depending only on k, Λ, κ and l, this is at most 1/4. 𝒯 is a down-set in (u, v),
so two of its points are joined in it by a path of length at most three times their distance, and Ψ is injective. Ψ − id
and its differential vanish on N, so a point at distance d′ from N moves by at most C ρ d′; every point of [0, σ]² is at
distance at least σ/2 from 𝒯 ∩ Σ_(τ_end), as [0, 2σ]² ⊂ 𝒯, and at distance at most 2σ from N; so for C ρ ≤ 1/8 the image
Ψ(𝒯) contains [0, σ]², by the homotopy invariance of the degree of id + t(Ψ − id), 0 ≤ t ≤ 1, as in
[[lem:loc-cone-gauge]]. The smallness of ρ is imposed in Step 3, before T* is fixed in Step 4, so there is no
circularity.

So on [0, σ]² × S³ the metric g in the coordinates Ψ, with v′ and u′ the phases and the densities q_in, q_out, is a class
solution in the gauge that induces the data on the two edges. σ depends only on k, Λ, κ and l through δ_1, δ_c, ρ and T*.
Undoing the change of angle of Step 0 and the translation gives the proposition. ∎

The proof uses of the data only their restriction to the edges of length l, through the formal solution: so
[[prop:civp-axes-corner]] is the corner part of Rendall's reduction for data of any size, at the axes, with the size of
the rectangle bounded below in terms of norms of the data near the corner sphere. The sizes it uses enter at exactly
these places: the C^(6k+18) norm of the data with b = 0 on N_i, which bounds Û in C^(k+3) ([[prop:civp-axes-formal]]);
the nondegeneracy, through d and the reference metric; the constants of [[lem:class-leaf-reference]] for Û, which also
fix δ; and the time T* of [[thm:class-kato]] (a), which depends on Û only through bounds of order k of the coefficients
and the bounds C_F, L of the forcing, the reference path being 0 in the variable Z.

#### Uniqueness and the maximal development {#sec:civp-axes-unique}

**Proposition {#prop:civp-axes-unique}** (Uniqueness in the gauge, without smallness.) Let cone data be given on edges
N_o = {u_c} × [v_c, v_c + λ_v] and N_i = [u_c, u_c + λ_u] × {v_c}, put Q := [u_c, u_c + λ_u] × [v_c, v_c + λ_v], and let
(g, q_in, q_out) on D × S³ and (g′, q′_in, q′_out) on D′ × S³ be class solutions in the gauge that induce the data on N ∩
D and N ∩ D′, where D, D′ ⊂ Q are past sets relative to (u_c, v_c), relatively open in Q. Then they are equal on (D ∩ D′)
× S³. No smallness of either solution is assumed.

*Proof.* *Step 1 (Reductions).* Translate so that the corner is (0, 0), and apply the change of angle of
[[lem:civp-axes-extension]] (d) to both solutions, which keeps them class solutions in the gauge, with the same new data,
b = 0 on N_i; it suffices to prove the claim for the new solutions. D″ := D ∩ D′ is a relatively open past set. A point
(u, v) ∈ D″ with u < λ_u and v < λ_v lies in R := [0, a] × [0, b] ⊂ D″ for a := u, b := v, and as R is compact and D″
relatively open there is ε > 0 with R_ε := [0, a + 2ε] × [0, b + 2ε] ⊂ D″. The points of D″ with u < λ_u and v < λ_v are
dense in D″: with (u, v) every (u − s, v − s), s small, lies in D″ when u, v > 0, and a point with u = 0 or v = 0 is a
limit of such points or lies on N. The solutions are continuous, so it suffices to show that they agree on each such R.
By [[lem:civp-axes-jets]] (iv) both have the derivatives a_j, b_k across N ∩ R_ε, so their difference vanishes to
infinite order on N ∩ R_ε.

*Step 2 (The first disagreement).* Put R′ := [0, a + ε] × [0, b + ε], t := u + v, Σ_t := {u + v = t} and D_t := R′ ∩ Σ_t.
Let t* be the supremum of the s ∈ [0, a + b + 2ε] such that the two solutions agree on R′ ∩ {t ≤ s}; the set of these s
contains 0 and is closed. Suppose t* < a + b + 2ε. The solutions agree on R′ ∩ {t ≤ t*}, so their difference vanishes to
infinite order on D_(t*), all its derivatives being limits from the side t < t* or, for t* = 0, vanishing on N. We show
that they agree on R′ ∩ {t ≤ t* + θ′} for some θ′ > 0, against the choice of t*.

*Step 3 (A wave map near D_(t*)).* Use the coordinates (t, y), y := e^(v−u) ω, ω ∈ S³ ⊂ ℝ⁴, a G-equivariant chart on
which metrics in natural double-null form are smooth through the axes, with dt timelike for every such metric, as g⁻¹(dt,
dt) = 2 g^(uv) < 0. Extend g by [[lem:civp-axes-extension]] (a), applied in u and then in v to Ω, b and γ, to a smooth
G-invariant metric g_e in natural double-null form on [−ε_1, a + 2ε] × [−ε_1, b + 2ε] × S³ for some ε_1 > 0, and put g′_e
:= g′ on R_ε and g′_e := g_e elsewhere there; g′_e is smooth, g′ − g vanishing to infinite order on N ∩ R_ε. Seek Φ =
id + φ with id : (g′_e) → (g_e) a wave map,

    g′_e^(μν) (∂_μ∂_ν Φ^λ − Γ[g′_e]^ρ_(μν) ∂_ρ Φ^λ + Γ[g_e]^λ_(αβ)(Φ) ∂_μ Φ^α ∂_ν Φ^β) = 0,

a semilinear wave system for φ with principal part g′_e^(μν) ∂_μ∂_ν, for which φ = 0 is a solution wherever g′_e = g_e.
Cut it off in (u, v) outside a compact neighbourhood, inside the domain of g′_e, of R′ ∪ ([−ε_1/2, 0] × [0, b + ε]) ∪
([0, a + ε] × [−ε_1/2, 0]), with frozen flat coefficients there as for A^μ_♭ in case (II) of [[sec:loc-cone-reduced]],
and write it in first-order form in the chart; its forcing term is local, so [[thm:class-kato]] (a) with
[[rem:class-kato-local]] gives a smooth solution φ on [t*, t* + θ] × ℝ⁴ with φ = 0 and ∂φ = 0 at t = t*, for some θ > 0;
it is G-equivariant, by uniqueness. As in [[lem:loc-cone-past]], the energy of [[lem:loc-cone-energy]] on the part of {t*
≤ t ≤ t* + θ} where u ≤ 0 or v ≤ 0 and u, v ≥ −ε_1/2 + 2(t − t*), u ≤ a + ε and v ≤ b + ε, whose faces {u = 0} and {v =
0} are null with outward conormals du and dv future directed and whose faces {u = −ε_1/2 + 2(t − t*)} and {v = −ε_1/2 +
2(t − t*)} have the outward conormals 2dv + du and 2du + dv, timelike and future directed for every metric in natural
double-null form, and whose faces {u = a + ε}, {v = b + ε} are null with the region to their past, gives φ = 0 there for
4θ ≤ ε_1, where g′_e = g_e. So Φ = id to infinite order on N ∩ R′ ∩ {t ≤ t* + θ}. And Φ − id vanishes to infinite order
on D_(t*): the t-derivatives of φ at t = t* are determined, through the equation, by the residual g′_e^(μν) (Γ[g_e] −
Γ[g′_e])^λ_(μν) of φ = 0 and its derivatives, which vanish on D_(t*), and by derivatives along the slice of lower
t-derivatives. Put Φ := id on {t ≤ t*}. For θ small Φ is a diffeomorphism near the identity, and Φ(R_ε ∩ {t ≤ t* + θ}) ⊃
R′ ∩ {t ≤ t* + θ}.

*Step 4 (Comparison in the wave gauge of g).* Put G̃ := (Φ⁻¹)^* g′, ũ := u ∘ Φ⁻¹, ṽ := v ∘ Φ⁻¹ and q̃_A := q′_A ∘ Φ⁻¹ on
R′ ∩ {t ≤ t* + θ}. The wave map condition says D(G̃) = 0 for the gauge vector relative to g, and D(g) = 0 relative to g.
So U := (g, −dv, −du, □_g(−v), □_g(−u), q_in, q_out) and Ũ := (G̃, −dṽ, −dũ, □_G̃(−ṽ), □_G̃(−ũ), q̃_in, q̃_out) solve the
augmented system relative to g with ζ_A := 1 and chapter 81's closure at the axes, in the slicing by t: the closure holds
for both in every slicing, their leaves being the level sets of their phases in the slices (the last statement of
[[lem:class-leaf-differences]]) and the right side of [[eq:class-raychaudhuri]] being, by [[eq:class-identity]] and
[[eq:class-x]], the closure. Ũ − U vanishes to infinite order on D_(t*) and on N ∩ R′. For t* ≤ s ≤ t* + θ let R′_s := R′
∩ {t* ≤ t ≤ s} and z := 𝐔̃ − 𝐔 its first-order variables, so that, with the coefficients at U,

    A^μ(x, 𝐔) ∂_μ z = M z − ½ χ_ax (σ_A[Ũ]² − σ_A[U]²)  (in the Θ-rows),      M bounded,

χ_ax as in Step 2 of the proof of [[prop:civp-axes-corner]]. The boundary of R′_s consists of D_(t*), of pieces of N,
where z = 0, of D_s, and of the future faces {u = a + ε} and {v = b + ε}, null for g with R′_s to their past, on which
the boundary form at U is nonnegative, du(P_out) = dv(P_in) = 0 and the other pairings positive.

*The non-local term.* D_t is bounded by at most two double-null spheres of g, each on N or on a future face; each is a
level set of u or of v within Σ_t, hence a leaf of U of both families, and the leaves of U foliate a neighbourhood of
each axis point, so D_t is closed under the leaves of U. (i) If t* < min(a, b) + ε, then for t near t* both boundary
spheres of D_t lie on N, where Ũ = U to infinite order; they are therefore leaves of Ũ too, by the uniqueness in
[[lem:class-volterra]], the leaf equations of Ũ and U agreeing along them, and D_t is closed under the leaves of Ũ.
[[lem:class-leaf-reference]] (b′) with (U, U′) := (Ũ, U), whose bounds 𝔐 hold on R′_(t*+θ), gives ‖σ_A[Ũ] −
σ_A[U]‖_(L²(D_t∩𝒰_δ)) ≤ C ‖z‖_(L²(D_t)), C not depending on the width of D_t. (ii) Otherwise the width of D_t, in the
variable v − u, is bounded below near t = t*, since t* < a + b + 2ε. Let 𝔼_t be Stein's operator for an annulus
transported to D_t by a radial map of y and averaged over G, as in Step 5 of the proof of [[prop:civp-axes-corner]],
bounded on H^σ, σ ≤ k − 1, uniformly for t near t*. Put Ŭ := Ũ − 𝔼_t(Ũ − U). Then Ŭ = U on D_t, and since the leaves of U
through points of D_t lie in D_t, σ_A[Ŭ] = σ_A[U] there, by the uniqueness in [[lem:class-volterra]]. As Ũ − U vanishes
to infinite order on D_(t*), ‖Ũ − U‖_(H^(k−1)(D_t)) → 0 as t ↓ t*; so for t near t* both Ũ and Ŭ lie in the ball 𝔅′ of
[[lem:class-leaf-differences]] (b) about the smooth class solution ů := U, in the slicing by t, and

    ‖σ_A[Ũ] − σ_A[U]‖_(L²(D_t∩𝒰_δ)) = ‖σ_A[Ũ] − σ_A[Ŭ]‖_(L²(D_t∩𝒰_δ)) ≤ C ‖𝔼_t z‖_(L²(𝒰_(2δ))) ≤ C ‖z‖_(L²(D_t)).

In both cases e(s) := ∫_(D_s) ⟨A^0(x, 𝐔) z, z⟩ satisfies e(s) ≤ C ∫_(t*)^s e for t* ≤ s ≤ t* + θ′, some θ′ ∈ (0, θ], by
the divergence theorem on R′_s as in [[lem:loc-cone-energy]]; e(t*) = 0, so z = 0 on R′_(t*+θ′).

*Step 5 (The coordinates).* So G̃ = g, ũ = u, ṽ = v and q̃_A = q_A on R′ ∩ {t ≤ t* + θ′}: Φ is an isometry from g′ to g
with u ∘ Φ = u and v ∘ Φ = v. In natural double-null form g⁻¹du = g^(uv) ∂_v, as g^(uu) = g^(uA) = 0, so the angle θ of
the coordinates is constant along the integral curves of g⁻¹du, and likewise for g′. Φ carries g′⁻¹du to g⁻¹du, so θ ∘
Φ⁻¹ is constant along the integral curves of g⁻¹du; each of these in R′ ∩ {t* ≤ t ≤ t* + θ′}, followed to the past, meets
{t ≤ t*} or N_i, where Φ = id. So θ ∘ Φ⁻¹ = θ, Φ = id, and g′ = g and q′_A = q_A on R′ ∩ {t ≤ t* + θ′}. This contradicts
the choice of t*; so t* = a + b + 2ε, and the solutions agree on R′ ⊃ R. ∎

**Corollary {#cor:civp-axes-maximal}** (The maximal development.) Let cone data be given on N_o and N_i, with Q as in
[[prop:civp-axes-unique]]. Let D_max be the union of the sets D, past sets relative to the corner and relatively open in
Q, that carry a class solution in the gauge inducing the data on N ∩ D. Then D_max is a past set, relatively open in Q,
and there is exactly one class solution in the gauge on D_max × S³ that induces the data; it restricts to each of those
solutions. If the data are of size at most Λ in C^(6k+19) and κ-nondegenerate on the parts of the edges within distance 1
of the corner sphere, D_max contains [u_c, u_c + σ) × [v_c, v_c + σ), σ the number of [[prop:civp-axes-corner]] for Λ, κ
and l := min(1, λ_u, λ_v).

*Proof.* By [[prop:civp-axes-unique]] any two of the solutions agree on the intersection of their domains, so they define
one function on the union, which is smooth, smoothness being local, and solves the equations there; a union of past sets
relatively open in Q is one. The last statement is [[prop:civp-axes-corner]], a solution on [u_c, u_c + σ] × [v_c, v_c +
σ] restricting to one on the relatively open past set [u_c, u_c + σ) × [v_c, v_c + σ). ∎

#### Continuation along the generators {#sec:civp-axes-faces}

**Proposition {#prop:civp-axes-faces}** (Continuation along the generators.) Let cone data be given on N_o = {0} × [0,
λ_v] and N_i = [0, λ_u] × {0}, Q := [0, λ_u] × [0, λ_v], and let D_max be as in [[cor:civp-axes-maximal]]. Then N_o ∪ N_i
⊂ D_max, and there are u*, v* > 0 with ([0, u*] × [0, λ_v]) ∪ ([0, λ_u] × [0, v*]) ⊂ D_max. No estimate of the solution
inside D_max enters, and no lower bound for u* or v* is asserted.

*Proof.* The four facts used are: (C) the corner theorem, [[prop:civp-axes-corner]], whose σ depends only on norms of the
data within a fixed distance of the corner sphere; (E) the extension of short pieces of edges,
[[lem:civp-axes-extension]] (b)–(d); (J) the derivatives across the edges, [[lem:civp-axes-jets]], which exist and are
bounded on the whole of each edge because they solve linear equations; and (U) uniqueness, [[prop:civp-axes-unique]] and
[[cor:civp-axes-maximal]].

*Step 0 (Constants).* By [[lem:civp-axes-extension]] (d), applied along N_i to the data and to every development, we may
assume b = 0 on N_i. Extend the free functions past the far ends of the edges by [[lem:civp-axes-extension]] (a), in the
variables v − λ_v and u − λ_u, and solve the constraints by its part (c): this gives cone data of any sign on N_o^+ :=
{0} × [0, λ_v + ℓ_1] and N_i^+ := [0, λ_u + ℓ_1] × {0}, ℓ_1 ∈ (0, 1], equal to the given data on N_o and N_i. Let m :=
6k + 19, Λ_0 their size in C^m and κ_0 their nondegeneracy. By [[lem:civp-axes-jets]] the derivatives a_j across N_o^+
and b_k across N_i^+ exist on the whole of these edges and are smooth, so

    K′ := the largest of the suprema of |∇̊^i a_j| over N_o^+ and of |∇̊^i b_j| over N_i^+, i, j ≤ m + 4,

is finite. The functions that a class solution in the gauge induces on a piece of a null hypersurface {v = const} through
a point of N_o, after the change of angle of [[lem:civp-axes-extension]] (d), have u-derivatives at u = 0 that are
polynomials in the a_j there and their ∇̊-derivatives, the flow of that change being determined by b; let K″ bound, in
terms of K′, those of order at most m + 3, with ∇̊-derivatives of order at most m + 3. Let ℓ′, κ′ and C be the numbers of
part (c) of that lemma for the order m + 3, the size C_(m+3) (K″ + 1) and the nondegeneracy κ_0/2, C being the bound of
the size of the extension in C^m. Put l := min(ℓ_1, ℓ′), Λ_c := max(Λ_0, C), κ_c := min(κ_0, κ′), and σ_c := σ(k, Λ_c,
κ_c, l) of [[prop:civp-axes-corner]]. These depend on the data, and not on the point of the edges considered below.

*Step 1.* Let V be the supremum of the v ∈ [0, λ_v] with (0, v) ∈ D_max. By [[prop:civp-axes-corner]] at (0, 0), with the
pieces of length l of N_o^+ and N_i^+, and [[cor:civp-axes-maximal]], V ≥ min(σ_c, λ_v); and (0, v) ∈ D_max for v < V,
D_max being a past set. Suppose (0, λ_v) ∉ D_max. Put η := min(σ_c/4, V/2) and v_η := V − η.

*Step 2 (An ingoing null hypersurface of the solution).* {0} × [0, V − η/2] is a compact subset of the relatively open
D_max, so there is w ∈ (0, 1] with [0, w] × [0, V − η/2] ⊂ D_max. On N_η := [0, w] × {v_η} the maximal development
induces smooth invariant families Ω, b, γ, q_out of (u, θ), with q_out ≥ 0, satisfying Ric(L̲, L̲) = q_out, which agree
on S_η := {(0, v_η)} × S³ with the data of N_o. With the piece {0} × [v_η, v_η + l] of N_o^+ they are cone data of any
sign at the corner (0, v_η), nonnegative where v ≤ λ_v.

*Step 3 (Their norms near the corner).* By [[lem:civp-axes-jets]] (iv), applied to the development on [0, w] × [0, V −
η/2], the u-derivatives at u = 0 of the functions on N_η are a_j(v_η), so their derivatives of order at most m + 4 at S_η
are bounded by K′, whatever η. Apply [[lem:civp-axes-extension]] (d) to N_η, and then (b) of that lemma, at the order m +
3, to the free functions on N_η, with L = L(η) < ∞ a bound for their derivatives of order m + 4 on [0, w] × S³ and a =
a(η) ≤ min(w, 1/2, 1/(1 + L)) so small that γ ≥ (κ_0/2) γ̊ on [0, a]: the free functions on [0, a] have extensions to [0,
1] with C^(m+3) norms at most C_(m+3)(K″ + 1), and by the estimate of (b) all the functions on [0, a] have C^(m+3) norms
at most C_(m+3)(K″ + 1). Part (c) then gives cone data of any sign on [0, a + ℓ′] × {v_η}, equal to those of N_η on [0,
a], of size at most Λ_c in C^m and κ_c-nondegenerate. Neither w nor a is bounded below as η → 0.

*Step 4 (The corner problem).* [[prop:civp-axes-corner]] at the corner (0, v_η), with the edges {0} × [v_η, v_η + l] and
[0, a + ℓ′] × {v_η}, both of length at least l, gives a class solution in the gauge g_η on [0, σ_c] × [v_η, v_η + σ_c] ×
S³ inducing these data; undoing the change of angle of Step 3, it induces the functions of N_η on [0, a] × {v_η}.

*Step 5 (Gluing).* Let ā := min(a, σ_c), Q′ := [0, ā] × [v_η, min(v_η + σ_c, λ_v)] and 𝒬 := ([0, ā) × [v_η, v_η + σ_c)) ∩
Q. On Q′, g_η has nonnegative densities (the data being nonnegative on N_o ∩ {v ≤ λ_v} and on N_η ∩ {u ≤ a}), so it is a
class solution in the gauge there. D_max ∩ Q′ is a past set relative to (0, v_η), relatively open in Q′, and the maximal
development and g_η are class solutions in the gauge on it inducing the same functions on the edges of Q′: the data of
N_o and the functions of N_η. By [[prop:civp-axes-unique]] they agree there, hence on D_max ∩ 𝒬. D_new := D_max ∪ (𝒬 ∩
{v > v_η}) is a past set relative to (0, 0), since for (u, v) ∈ 𝒬, [0, u] × [0, v_η] ⊂ [0, w] × [0, V − η/2] ⊂ D_max and
[0, u] × [v_η, v] ⊂ 𝒬, and it is relatively open in Q. The function equal to the maximal development on D_max and to g_η
on 𝒬 is well defined, smooth and a class solution in the gauge inducing the data; so D_new ⊂ D_max. As v_η + σ_c ≥ V +
3σ_c/4, this gives (0, v) ∈ D_max for some v > V if V < λ_v, against the definition of V, and (0, λ_v) ∈ D_max if V =
λ_v, against the assumption. So (0, λ_v) ∈ D_max, and N_o ⊂ D_max.

*Step 6 (The ingoing edge).* The same argument with u and v exchanged, the corner problems being posed at the corners
(u_η, 0) with ingoing edge a piece of N_i^+ and outgoing edge a piece {u_η} × [0, a] of a null hypersurface of the
solution, extended by [[lem:civp-axes-extension]] (b) and (c) on an outgoing edge, gives N_i ⊂ D_max; the constants are
those of Step 0 with the b_k in place of the a_j.

Finally N_o is compact and D_max relatively open in Q, so D_max contains [0, u*] × [0, λ_v] for some u* > 0, and likewise
[0, λ_u] × [0, v*]. ∎

The continuation asks of the data only the facts (C), (E), (J) and (U), and of the solution only that it is smooth up to
the cones on the part already constructed. The width w of Step 2 may tend to 0 as the corner moves along the generators;
only σ_c must not, and it does not, because the corner data of Step 3 are bounded by Λ_0 and by the bound K′ of the
derivatives across the cone, which does not depend on the point of the cone.

**Remark {#rem:civp-axes-riccati}** (Why the derivatives across the cones must solve linear equations.) In Step 3 the
bound K′ is finite because the derivatives across a cone solve linear ordinary differential equations along its
generators ([[lem:civp-axes-jets]] (i)), which have solutions on the whole cone. For a wave equation with a Riccati term
this fails: for □φ = (∂_u φ)² on ℝ × ℝ × S¹ with □ = −4∂_u∂_v + ∂_y², data φ = 0 on {u = 0} and w := ∂_u φ, the equation
at u = 0 reads −4∂_v w = w², so w = w_0/(1 + w_0 v/4), which becomes unbounded at v = 4/|w_0| when w_0 < 0; then no
solution that is C¹ up to the cone exists on a neighbourhood of {u = 0, 0 ≤ v ≤ 4/|w_0|}, and the argument cannot reach
past it. For □φ = ∂_u φ ∂_v φ the same reasoning gives −4∂_v w + ∂_y² φ = w ∂_v φ at u = 0, which is linear in w.

#### The continuation criterion {#sec:civp-axes-criterion}

**Proposition {#prop:civp-axes-criterion}** (Continuation criterion.) In the setting of [[prop:civp-axes-faces]], let 0 <
a ≤ λ_u and 0 < b ≤ λ_v, R_(a,b) := [0, a] × [0, b], and suppose that R_(a,b) ∖ {(a, b)} ⊂ D_max, that on (R_(a,b) ∖ {(a,
b)}) × S³ the functions ln Ω, b, γ, q_in and q_out of the maximal development have bounded derivatives of order at most
6k + 26 in (u, v) and ∇̊, and that γ ≥ κ γ̊ there for some κ > 0. Then (a, b) ∈ D_max, so D_max contains a neighbourhood
of R_(a,b) relative to Q.

*Proof.* Let K_1 bound the derivatives named and m := 6k + 19. For a corner (a − η, b − η) with 0 < η ≤ min(a, b) the
edges {a − η} × [b − η, b] and [a − η, a] × {b − η} lie in R_(a,b) ∖ {(a, b)}, and the maximal development induces cone
data on them. Normalise b on the second by [[lem:civp-axes-extension]] (d), and extend both edges by its parts (b) and
(c), at the order m + 3, with L := C K_1 and the corner derivatives bounded by C K_1, which is possible for η ≤ 1/(2(1 +
L)): this gives cone data on edges of length at least ℓ″ > 0, of size at most Λ″ in C^m and κ″-nondegenerate, with ℓ″,
Λ″, κ″ depending only on k, K_1 and κ, and equal to the induced data on the given edges. [[prop:civp-axes-corner]] gives
a class solution in the gauge on [a − η, a − η + σ″] × [b − η, b − η + σ″] × S³, σ″ := σ(k, Λ″, κ″, ℓ″) independent of η.
Take η := min(a, b, σ″/2, 1/(2(1 + L))). As in Step 5 of the proof of [[prop:civp-axes-faces]], this solution agrees with
the maximal development on their common domain, by [[prop:civp-axes-unique]], and the union of their domains is a
relatively open past set carrying a class solution in the gauge that induces the data; so it lies in D_max, and it
contains (a, b). D_max is relatively open, so it contains a relative neighbourhood of the compact R_(a,b). ∎

So D_max = Q, or near a point of its boundary in Q the derivatives of order at most 6k + 26 of the metric functions and
densities are unbounded or γ degenerates.

#### The theorem {#sec:civp-axes-theorem}

**Lemma {#lem:civp-axes-free-data}** (Cone data from free data through the axes.) On N_o = {0} × [0, λ_v] let G-invariant
smooth families ln Ω, γ̂ and q_in ≥ 0 be given, and on N_i = [0, λ_u] × {0} likewise ln Ω, γ̂ and q_out ≥ 0, with γ̂
Riemannian, μ_γ̂ = μ_γ̊, and the two γ̂ and the two Ω agreeing on S_c; and let a positive invariant function ỹ_c on S³,
invariant functions ỹ_o′, ỹ_i′ and an invariant vector field β_c be given. Solve [[eq:civp-axes-raychaudhuri]] along N_o
with ỹ = ỹ_c and ∂_v ỹ = ỹ_o′ at v = 0, its analogue along N_i with ∂_u ỹ = ỹ_i′ at u = 0, put γ := ỹ² γ̂, and solve the
constraint Ric(∂_v, X) = 0 along N_o for b with b = 0 and ∂_v b = β_c at v = 0; put b := 0 on N_i. If ỹ > 0 on both
edges, these are cone data. If the free functions, ỹ_c, ỹ_o′, ỹ_i′ and β_c equal those of a second set of cone data at
the points of an invariant open set of S³, the two sets of cone data agree on the generators through it.

*Proof.* [[eq:civp-axes-raychaudhuri]] is a linear ordinary differential equation along each generator with coefficients
smooth on [0, λ] × S³, axes included, so ỹ is smooth and invariant, by uniqueness. The constraint Ric(∂_v, X) = 0 is, by
the formula of the proof of [[lem:civp-axes-principal]], a smooth expression in a chart; off the axes it is linear in b,
through ∂_v b and ∂_v² b, with the leading coefficient (1/(4Ω²)) γ(∂_v² b, X) (the second line of [[eq:loc-cone]]), and
its part quadratic in b, evaluated on an invariant b, vanishes off the axes and so, by continuity, everywhere; so for
invariant b it is a linear first-order equation for ∂_v b with smooth coefficients, and b is smooth and invariant. On
N_i, with b = 0, Ric(L̲, L̲) = q_out is the analogue of [[eq:civp-axes-raychaudhuri]]. The constraints hold by
construction, and (i) of [[def:civp-axes-data]] by the corner values. The last statement is uniqueness for these
equations, whose coefficients at a point of S³ are built from the free functions there and their derivatives on S³. ∎

For the cones of [[sec:loc-cones]], ỹ = e^ϕ (sin ϑ cos ϑ)^(−1/3) and γ̂ = (sin ϑ cos ϑ)^(2/3) (e^(2ℓ_1) dϑ² + e^(2ℓ_2)
dφ1² + e^(2ℓ_3) dφ2²), and [[eq:civp-axes-raychaudhuri]] is the equation for y = e^ϕ in the proof of [[prop:loc-cones]],
since ¼ |∂_v γ̂|²_γ̂ = Σ_i (∂_v ℓ_i)². So the data of [[prop:loc-cones]] and [[lem:loc-cone-in]] whose γ̂ is a smooth
tensor field on S³ are those of [[lem:civp-axes-free-data]], and they are cone data wherever ỹ stays positive, the axis
generators included.

**Theorem {#thm:civp-axes}** (Developments of cone data of any size through the axes.) Let k ≥ 6, and let cone data be
given on N_o = {0} × [0, λ_v] and N_i = [0, λ_u] × {0} ([[def:civp-axes-data]]): any Ω on both edges, any b on N_i,
densities q_in ≥ 0 and q_out ≥ 0, no smallness, and no condition at the axes beyond smoothness. Put Q := [0, λ_u] × [0,
λ_v].

(a) (*Corner.*) Let Λ be the size in C^(6k+19) and κ the nondegeneracy of the data on N_o ∩ {v ≤ l} and N_i ∩ {u ≤ l}, l
:= min(1, λ_u, λ_v). There is a class solution in the gauge on [0, σ]² × S³ that induces the data, with σ > 0 depending
only on k, Λ, κ and l.

(b) (*Neighbourhood of the cones.*) There are u*, v* > 0 and a class solution in the gauge on (([0, u*] × [0, λ_v]) ∪
([0, λ_u] × [0, v*])) × S³ that induces the data. So v and u are the phases of the ingoing and the outgoing family, the
development contains the strips {u ≤ u*} along N_o and {v ≤ v*} along N_i, and the dust on the cones lies in it.

(c) (*Uniqueness and the maximal development.*) Two class solutions in the gauge on past sets relatively open in Q that
induce the data agree on the intersection of their domains. The set D_max of [[cor:civp-axes-maximal]] is a past set,
relatively open in Q, carrying the unique class solution in the gauge that induces the data and restricts to each of
them. It contains [0, σ)², the set ([0, u*) × [0, λ_v]) ∪ ([0, λ_u] × [0, v*)), and the relatively open past sets on
which the developments of [[thm:loc-cone-development]], [[thm:civp-large]] and [[pending:tier3-theorem]] are defined,
whenever the data satisfy their hypotheses; there the development is theirs.

(d) (*Continuation criterion.*) If D_max ⊃ R_(a,b) ∖ {(a, b)} for a rectangle R_(a,b) = [0, a] × [0, b] ⊂ Q, and the
metric functions and densities of the maximal development have bounded derivatives of order at most 6k + 26 there with γ
≥ κγ̊ for some κ > 0, then D_max contains a neighbourhood of R_(a,b) relative to Q.

(e) (*Localisation.*) If a class solution in the gauge on a past set D_0 relatively open in Q, for instance the
background of [[sec:loc-setting]] or a background of [[prop:two-dust-background]] on a rectangle [0, a) × [0, b), induces
the data on N ∩ D_0, then D_0 ⊂ D_max and the maximal development equals it on D_0.

*Proof.* (a) is [[prop:civp-axes-corner]]. (b) is [[prop:civp-axes-faces]], restricted to a past set: [0, u*] × [0, λ_v]
∪ [0, λ_u] × [0, v*] is one. (c) is [[prop:civp-axes-unique]] and [[cor:civp-axes-maximal]]; the developments named there
are class solutions in the gauge in the sense of [[sec:civp-large]], their metrics being smooth through the axes (they
equal a background there, or are those of [[pending:tier3-theorem]]), and their domains are past sets whose relative
interiors in Q are relatively open past sets containing the points concerned; their data are cone data in the sense of
[[def:civp-axes-data]]. The closed sets of (a) and (b) contain the relatively open past sets [0, σ)², and [0, u*) × [0,
λ_v] ∪ [0, λ_u] × [0, v*). (d) is [[prop:civp-axes-criterion]]. (e) follows from (c), D_0 being the domain of a
development. ∎

**Corollary {#cor:civp-axes-cones}** (The cones of the two-dust background.) Let free data on 𝒞_out ∩ {v ≤ λ_v} and on
𝒞_in ∩ {u ≤ λ_u} be given as in [[prop:loc-cones]] and [[lem:loc-cone-in]], with the background's corner values, of any
size and with any support in angle, including the axes, such that γ̂ is a smooth tensor field on S³, and suppose that the
factor e^ϕ of [[prop:loc-cones]] and [[lem:loc-cone-in]] stays positive on every generator, the axis generators included.
Then these cone data have a development in the gauge [[eq:loc-double-null]] on a neighbourhood ([0, u*] × [0, λ_v]) ∪
([0, λ_u] × [0, v*]) of the two cones, through the axes, with or without dust; it is unique in the gauge, it equals the
background on every rectangle [0, a) × [0, b) on whose edges the data are the background's, and it is the restriction of
the maximal development of [[thm:civp-axes]] (c).

*Proof.* By [[lem:civp-axes-free-data]] and the paragraph after it the data are cone data in the sense of
[[def:civp-axes-data]], the background being smooth through the axes. Apply [[thm:civp-axes]] (b), (c) and (e). ∎

So every perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5}, of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, and every density
added on the cones, of any amplitude and reaching the axes or not, has a development near the two cones, provided the
cones do not focus; for large perturbations that positivity is a hypothesis, and it can fail.

**Corollary {#cor:civp-axes-perturbations}** (Small perturbations of a background that is round.) Let g_0 be a two-dust
background of [[prop:two-dust-background]], which is round, given in the gauge [[eq:loc-double-null]] on a neighbourhood
of a rectangle Q_0 := [0, a] × [0, b] contained in its set G, and assume [[pending:tier3-theorem-general]]: there is
ε_0 > 0 such that cone data within ε_0 of g_0's on the edges of Q_0, in the norm of that theorem and with no condition in
angle, have a class solution in the gauge on Q_0 × S³ that induces them. Then for such data D_max = Q_0, and the maximal
development of [[thm:civp-axes]] (c) is that solution. So small non-round perturbations of the cone data of g_0, reaching
the axes, develop on every rectangle contained in G, ε_0 depending on the rectangle, and on every finite union of such
rectangles.

*Proof.* Q_0 is a past set relatively open in itself, so the solution of [[pending:tier3-theorem-general]] is a
development in the sense of [[cor:civp-axes-maximal]], and D_max = Q_0; for a finite union of rectangles take the data on
the longest edges and apply [[thm:civp-axes]] (c) to the developments on each rectangle. ∎

**Remark {#rem:civp-axes-scope}** (What [[thm:civp-axes]] does not give.) (i) *The width.* u* and v* are not bounded
below in terms of the data: the continuation of [[prop:civp-axes-faces]] uses no a priori estimate, and an explicit width
would need estimates near the axes on a strip of fixed width. For data near the background's,
[[thm:loc-cone-development]] and [[pending:tier3-theorem]] give explicit domains, and [[thm:civp-large]] gives its width
through the constants of [[thm:std-cctw-strips]] and suprema of its solution ([[rem:civp-large-domain]]). (ii) *The
rectangle.* A development on the whole of Q is not asserted. For data of any size the factor ỹ of
[[eq:civp-axes-raychaudhuri]] can vanish on a cone, at a focal sphere, beyond which there are no cone data, and the round
backgrounds of [[prop:two-dust-background]] are constructed only on their set G; D_max and the criterion (d) take the
place of the rectangle. (iii) *Further families.* The theorem concerns the two adapted families, whose phases are the
coordinates u and v. The proof uses at the axes that the spheres {u, v = const} of every corner problem are leaves of
every family present there; a further family has this property only if its phase is constant on those spheres, and
further families reaching the axes are not treated. (iv) *Regularity.* The data are smooth; the corner theorem uses their
norms in C^(6k+19) near the corner sphere. Data of finite regularity, densities that are only bounded, and shells, are
not covered; for the 3 + 1 problem with measure-valued null dusts see [[rem:loc-cone-scope]] (iii). (v) *Symmetry.* The
T²-symmetry and the two reflections are used throughout; the problem without symmetry is not treated.

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as lines of the chapter sources,
unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:". Line numbers are those
of the current chapter sources and of proofs/P-CIVP.md and proofs/P-CIVP2.md, and serve only to find the place. The
section of Block B follows the Tier 3 section ([[pending:tier3-section]]), which is being written; where that section,
Tier 1 or Tier 2 changes a text listed below, the coordinator merges the new texts.

*1. Block A, [[ch:class-system]].* The text of Block A from the statement of [[lem:class-leaf-reference]] through the end
of its proof (without the heading "Block A" and its first paragraph) is inserted in [[sec:class-planar-shear]]
immediately after [[rem:class-leaf-numerics]], whose last line ends "0.146 and 2.91. No proof uses these observations."
(line 1363), and before the heading "### Cauchy stability with the dusts at the axes {#sec:class-axes-stability}" (line
1365), with one blank line before and one after. It defines lem:class-leaf-reference, eq:class-leaf-lipschitz and
eq:class-leaf-wise.

*2. [[ch:class-system]], [[lem:class-leaf-differences]], the definition of H_L (lines 1326–1328).* The subspace TΣ_L in
H_L[Θ_A] must be fixed by the state, as [[lem:class-volterra]] takes H as a function of position. The Tier 3 section may
ask for the same clause; one copy is kept. Old:

be the graphs z = h(r) through the points of the axis near that point, each solving [[eq:class-leaf-volterra]] with
H_L := H_L[Θ_A], the formula of step (1) of [[lem:class-planar-shear]] with Θ_A in place of Θ and the spatial part of
p_A in place of ∇_Σ u; they exist and are unique by [[lem:class-volterra]], and for U near ů they are C¹-close to the

New:

be the graphs z = h(r) through the points of the axis near that point, each solving [[eq:class-leaf-volterra]] with
H_L := H_L[Θ_A], the formula of step (1) of [[lem:class-planar-shear]] with Θ_A in place of Θ, the spatial part of p_A
in place of ∇_Σ u and, for TΣ_L there, the γ3-orthogonal complement in TM3 of the spatial part of p_A, so that
H_L[Θ_A] is a function of position; they exist and are unique by [[lem:class-volterra]], and for U near ů they are
C¹-close to the

*3. Block B, [[ch:localised-data]].* The section of Block B, from its heading through the end of
[[rem:civp-axes-scope]], is inserted as a new section after the Tier 3 section, which follows [[sec:civp-large]], and
before the heading "### The static Killing field and the charge {#sec:loc-kid}" (line 602 of the current chapter), with
one blank line before and one after. Its heading line is "### Developments of data of any size through the axes
{#sec:civp-axes}". It defines sec:civp-axes, sec:civp-axes-data, eq:civp-axes-form, def:civp-axes-data,
eq:civp-axes-raychaudhuri, sec:civp-axes-jets, lem:civp-axes-principal, eq:civp-axes-principal, lem:civp-axes-jets,
lem:civp-axes-extension, prop:civp-axes-formal, sec:civp-axes-corner, prop:civp-axes-corner, eq:civp-axes-modified,
sec:civp-axes-unique, prop:civp-axes-unique, cor:civp-axes-maximal, sec:civp-axes-faces, prop:civp-axes-faces,
rem:civp-axes-riccati, sec:civp-axes-criterion, prop:civp-axes-criterion, sec:civp-axes-theorem,
lem:civp-axes-free-data, thm:civp-axes, cor:civp-axes-cones, cor:civp-axes-perturbations and rem:civp-axes-scope, none
of which is defined elsewhere. The prefix may be changed to loc- without other changes.

*4. [[ch:localised-data]], the paragraph after [[prop:loc-cones]], its last sentence, as Tier 2's item 3 writes it
(proofs/P-CIVP2.md, lines 694–695).* Old:

the solution. No development is asserted for cone data that differ from the background's near an axis, for data of
finite regularity or for densities that are not smooth, and no other result of this paper uses these developments.

New:

the solution. For cone data of any size that reach the axes, with or without dust, a development in the gauge on a
neighbourhood of the two cones, unique in the gauge, and a maximal development with a continuation criterion are given
by [[thm:civp-axes]], provided the cones do not focus ([[cor:civp-axes-cones]]); the neighbourhood is not explicit, and a
development of the whole rectangle is not asserted ([[rem:civp-axes-scope]]). No development is asserted for data of
finite regularity or for densities that are not smooth, and no other result of this paper uses these developments.

*5. [[ch:localised-data]], its opening paragraph, as Tier 2's item 2 writes it.* After the parenthesis that closes with
the citation of the small-data theorem and before "On Σ_τ0 the constraints split, after Rácz", insert the sentence:

Data of any size that reach the axes have a development on a neighbourhood of the two cones, unique in the gauge, and a
maximal development, provided the cones do not focus ([[thm:civp-axes]]).

*6. [[ch:scope]], the paragraph on localised data, as Tier 2's item 4 writes its last sentence (proofs/P-CIVP2.md,
lines 720–721).* Old:

near the background's ([[thm:civp-large]], [[pending:civp-tier1-theorem]]). Developments of cone data that differ from
the background's near an axis are not established.

New:

near the background's ([[thm:civp-large]], [[pending:civp-tier1-theorem]]). For data of any size that reach the axes,
a development on a neighbourhood of the two cones, unique in the gauge, and a maximal development with a continuation
criterion exist when the cones do not focus; that neighbourhood is not explicit, and a development of the whole
rectangle is not asserted ([[thm:civp-axes]], [[rem:civp-axes-scope]]).

The citation [[pending:civp-tier1-theorem]] in the old and new texts is the one that Tier 2's wiring replaces.

*7. [[ch:theorems]], the item *More families*, as Tier 2's item 6 writes it (proofs/P-CIVP2.md, line 744).* Old:

  near the axes ([[thm:civp-large]]); and exactly localised vacuum data

New:

  near the axes ([[thm:civp-large]]); for such data of any size and reaching the axes, a development near the two
  cones, unique in the gauge, with a maximal development and a continuation criterion ([[thm:civp-axes]]); and exactly
  localised vacuum data

*8. Unchanged.* [[ch:introduction]] (its text on [[part:further]] already names the development from two null cones, as
Tier 1's item 5 writes it), [[ch:two-dusts]], [[ch:vlasov]] and [[ch:ten-l5]] need no change. [[rem:class-scope]] is not
changed: it concerns the high-frequency construction.

*9. Appendix A and the references.* No new entry. The proofs use [LY22, Theorem 1 (i)] ([[thm:std-ly-extension]]) in
[[lem:civp-axes-extension]] (a), Stein's operator ([[thm:std-sy-extension]]) in [[prop:civp-axes-corner]] and
[[prop:civp-axes-unique]], and the results of chapters 81 and 83; [[thm:std-cctw-strips]] is cited in a remark only.
