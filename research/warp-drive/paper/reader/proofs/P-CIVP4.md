### Block A. Addition to the planar shear at an axis

The text of this block goes into [[sec:class-planar-shear]] of [[ch:class-system]] after [[rem:class-leaf-numerics]];
the Placement section below gives the position and one clause added to [[lem:class-leaf-differences]].

**Lemma {#lem:class-leaf-reference}** (The planar shear about a reference that is not a solution.) Near a point p of
axis 2 with ρ1(p) > 0, on a slice Σ_τ, fix a family A and use the coordinates (z, y) of [[lem:class-leaf]]. A *state*
is a G-invariant U = (g, p_A, Θ_A, q_A) near the orbit of p, with g of class C², p_A and Θ_A of class C¹, g Lorentzian,
Σ_τ spacelike for g and p_A(∂_z) ≠ 0 on the axis. Its function H_L[U] is that of [[lem:class-leaf-differences]], its
*leaves* are the solutions h(·; z0) of [[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its
planar shear σ[U] at a point is [[eq:class-shear-leaf]] for the leaf through that point, with |p_A^Σ| in place of
|∇_M3 u| and p_A(n) in place of n(u), and for a state V, 𝒩_k^V(U) is [[eq:class-energy]] with V in place of ů. Let V be
a smooth state with |p_V(∂_z)| ≥ c > 0 on the axis near p.

(o) (Foliation.) There are r_V ∈ (0, ρ1(p)/4] and C_V, depending only on c, on lower bounds for A3, B3 and det₂ of the
metric γ3 of V and on bounds for the C² norms of g_V and the C¹ norms of p_V and Θ_V near the orbit of p, such that for
|z0 − z(p)| ≤ r_V the leaf h_V(·; z0) is defined on [0, r_V] with |h_V′(r; z0)| ≤ C_V r, and for |z0 − z(p)| ≤ r_V,
|z0′ − z(p)| ≤ r_V, z0 ≠ z0′ and 0 ≤ r ≤ r_V

    1/2 ≤ (h_V(r; z0) − h_V(r; z0′))/(z0 − z0′) ≤ 3/2.                                    {#eq:class-leaf-lipschitz}

Every point x of 𝒰_(r_V/4) lies on exactly one of these leaves; we write z0^V(x) for its axis point. The map (z0, y) ↦
h_V(|y|; z0) is smooth, and so is z0^V.

(a), (b) The conclusions (a) and (b) of [[lem:class-leaf-differences]] hold with ů replaced by V, 𝒩_k by 𝒩_k^V and
δ ≤ r_V/8, the balls 𝔅 and 𝔅′ being balls about V; the balls and C depend only on k, δ, c, r_V and bounds for the
C^(k+2) norms of V near the orbit of p.

(b′) (Leaf by leaf.) Let 𝔐 ≥ 1 bound, on 𝒰_(ρ1(p)/4), the C³ norms of g and the C¹ norms of p_A and Θ_A of two states
U and U′, the inverses of lower bounds for A3, B3, det₂ of their metrics γ3 and the inverse of a lower bound for |p_A^Σ|,
and let |p_A(∂_z)| ≥ c on the axis for both. There are δ_𝔐 ∈ (0, ρ1(p)/16] and C, depending only on 𝔐 and c, such that
for 0 < δ ≤ δ_𝔐 and every set D ⊂ Σ_τ for which the leaf of U through each point of D ∩ 𝒰_δ lies, over the disc
𝔻_(2δ), in D,

    ‖σ[U] − σ[U′]‖_(L²(D∩𝒰_δ)) ≤ C ‖U − U′‖_(L²(D∩𝒰_(2δ))),                               {#eq:class-leaf-wise}

where U − U′ includes the difference of the first derivatives of the metrics. No ball about a reference state and no
extension operator enters, and C does not depend on D.

Here V need not solve any equation: the leaves are defined by [[eq:class-leaf-volterra]] from H_L[V], and no phase is
involved. For a solution of the class system with Θ_A = □_g u_A they are the level sets of u_A
([[lem:class-leaf-differences]]), so (a) and (b) with V := ů are [[lem:class-leaf-differences]].

*Proof.* Constants C below depend only on the quantities named in the part concerned. Write G(r, z, q) := r H(z, r)/
a_L(r, z, q) − E_L(r, z, q) as in the proof of [[lem:class-volterra]], with H := H_L[V] in (o), so that a leaf solves
r h′(r) = ∫_0^r G(ρ, h(ρ), h′(ρ)) dρ.

(o) *Step 1.* At an axis point the spatial part of p_V is p_V(∂_z) dz ([[lem:class-phase-axis]]), of γ3-length at least
c (sup A3)^(−1/2); so |p_V^Σ| ≥ c (sup A3)^(−1/2)/2 on a neighbourhood of the axis whose size depends only on c and the
C¹ bounds, and there H_L[V] is C¹, with H and its first derivatives bounded in terms of c, the C² norms of g_V (which
bound n, K_Σ, κ_A1 and γ3 with its first two derivatives) and the C¹ norms of p_V and Θ_V. [[lem:class-volterra]]
applies at every z0 with |z0 − z(p)| ≤ r_1, r_1 depending only on these bounds, with one r0 and one C_0 for all such
z0, since its constants are bounds over a neighbourhood of (z0, 0) that hold uniformly. Its proof provides C_1, C_2
and δ_p with |∂_z G| ≤ C_1, |∂_q G| ≤ C_2 (r + |q|), C_2 (r0 + δ_p) ≤ 1/4, C_1 r0 ≤ 1/2 and C_0 r0 ≤ δ_p, and it gives
|h′| ≤ C_0 r ≤ δ_p on [0, r0].

*Step 2.* Let h_1, h_2 be the leaves through z_1, z_2 and w_i := h_i′. As |h_1(ρ) − h_2(ρ)| ≤ |z_1 − z_2| + ρ sup_[0,ρ]
|w_1 − w_2| and both |w_i| ≤ δ_p,

    |w_1(r) − w_2(r)| ≤ r⁻¹ ∫_0^r (C_1 |h_1 − h_2| + C_2 (ρ + δ_p) |w_1 − w_2|) dρ
                     ≤ C_1 |z_1 − z_2| + (C_1 r + 1/4) sup_[0,r] |w_1 − w_2|,

and C_1 r + 1/4 ≤ 3/4; so sup_[0,r] |w_1 − w_2| ≤ 4C_1 |z_1 − z_2| and |h_1(r) − h_2(r) − (z_1 − z_2)| ≤ 4C_1 r
|z_1 − z_2|. Put r_V := min(r0, r_1, 1/(8C_1), 1/C_0, ρ1(p)/4) and C_V := C_0. Then [[eq:class-leaf-lipschitz]] holds.

*Step 3.* For |y| = r ≤ r_V/4 the map z0 ↦ h_V(r; z0) on [z(p) − r_V, z(p) + r_V] is continuous and strictly
increasing, and |h_V(r; z0) − z0| ≤ C_0 r²/2 ≤ r_V/32; so its image contains [z(p) − 3r_V/4, z(p) + 3r_V/4], and each
point of 𝒰_(r_V/4) lies on exactly one leaf.

*Step 4.* For r > 0 the leaf equation is the regular ordinary differential equation (r h′)′ = r H/a_L − E_L with
smooth coefficients, so each leaf is smooth on (0, r_V], and the graph y ↦ h_V(|y|; z0) is C¹ on 𝔻_(r_V) with mean
curvature H_L[V] off the axis ([[lem:class-leaf]] (c)). The bound on the second derivatives in step (3) of the proof of
[[lem:class-planar-shear]] uses only these facts; it gives |h″| ≤ C on (0, r_V], so the first derivatives of the graph
are Lipschitz on 𝔻_(r_V) and the graph lies in H²(𝔻_(r_V)), and it solves [[eq:class-leaf-cartesian]] there in the
sense of distributions, a point being removable for a C¹ function with bounded second derivatives off it. The induction
of that step, applied with H_L[V] smooth, gives the graph in H^(j+2) on smaller discs for every j, so it is smooth. The
map (z0, w) ↦ r⁻¹ ∫_0^r G(ρ, z0 + ∫_0^ρ w, w(ρ)) dρ is smooth from an interval times a ball of C([0, r_V]) into
C([0, r_V]), and by Step 2 its differential in w has norm at most 3/4; by the implicit function theorem the leaf depends
smoothly on z0 with values in C¹([0, r_V]). Differentiating [[eq:class-leaf-cartesian]] in z0, each ∂_(z0)^j of the
graph solves that equation linearised at the leaf, with a right side holding lower derivatives in z0, and
[[lem:class-interior-regularity]] at every order gives all derivatives in y, as in step (4) of the proof of
[[lem:class-planar-shear]] with z0 in place of the value of the phase. So (z0, y) ↦ h_V(|y|; z0) is smooth, and by
[[eq:class-leaf-lipschitz]], ∂_(z0) h_V ∈ [1/2, 3/2]; the implicit function theorem gives z0^V smooth.

(a), (b) The proof of [[lem:class-leaf-differences]] holds with the following changes; it uses no equation satisfied
by ů. (i) The leaves h̊ are the leaves h_V of (o), smooth by (o). (ii) The difference δh of the leaves of U and of V
**with the same axis point** z0 solves L_V δh = δH_L − (terms in δγ3 and its first derivatives) + Q(δh), where L_V is
[[eq:class-leaf-cartesian]] linearised at h_V and δH_L is evaluated on the leaf of U; the zero-order term −(∂_z H_L[V])
δh comes from H_L[V](h_U(y), y) − H_L[V](h_V(y), y). L_V is smooth and uniformly elliptic with the axis interior by
[[lem:class-leaf]] (b), which holds at every graph. (iii) Derivatives transverse to the disc are taken in z0 and τ in
place of the value of ů_A and τ. They commute with L_V up to operators of lower order with smooth coefficients, as h_V
is smooth in (τ, z0, y) by (o) on each slice and the smooth dependence of V on τ; the change of variables (z0, y) ↦
(h_V(|y|; z0), y) has Jacobian ∂_(z0) h_V ∈ [1/2, 3/2]. (iv) At a point x, with σ_W(z0, y) := σ[W] at (h_W(|y|; z0),
y),

    σ[U](x) − σ[V](x) = (σ_U − σ_V)(z0^U(x), y) + (σ_V(z0^U(x), y) − σ_V(z0^V(x), y)),

and by [[eq:class-leaf-lipschitz]] |z0^U(x) − z0^V(x)| ≤ 2 |δh(y; z0^U(x))|: the shift of the foliation enters as
(∂_(z0) σ_V)(z0^U(x) − z0^V(x)) up to a quadratic remainder, the derivative falling on V. (v) The balls are about V; the
sup norms of the coefficients of L_U on 𝔅′ are bounded by [[lem:sobolev]] and by step (3) of the proof of
[[lem:class-planar-shear]], with sup |∂h| ≤ C r from [[lem:class-volterra]] for U in place of the bound through
−∂_y u/∂_z u. For U ∈ 𝔅′ the leaves of U exist and foliate 𝒰_(r_V/8) by (o) for U, the C² norms of g and the C¹ norms of
p_A, Θ_A being within C 𝒩_(k−1)^V(U) of those of V by [[lem:sobolev]] (k − 4 ≥ 2).

(b′) Apply Steps 1–3 of (o) to U and to U′; they use only the bounds named in (b′) and give r_V, C_0, C_1, C_2, δ_p
for both, depending only on 𝔐 and c. In addition |∂_z G(r, z, q)| ≤ C_3 (r + |q|³) for |q| ≤ δ_p, for G built from
either state: G(0, z, q) = −A3 q³/B3 by the proof of [[lem:class-volterra]], so ∂_z G(0, z, q) = −∂_z(A3/B3) q³, and
∂_r ∂_z G is bounded by the C³ norms of g and the C¹ norms of p_A, Θ_A. Along a leaf |q| = |h′| ≤ C_0 r, so there
|∂_z G| ≤ C_4 r and |∂_q G| ≤ C_4 r with C_4 := C_3 (1 + C_0³ r_V²) + C_2 (1 + C_0).

*One leaf.* Fix z0 and let h := h_U(·; z0), h̃ := h_(U′)(·; z0), δh := h − h̃, δw := h′ − h̃′ (so δh(0) = 0) and
ω(r) := |δw(r)|/r, which is bounded since |δw| ≤ 2C_0 r. Subtracting the two Volterra equations, and writing the
difference of the integrands as G_U − G_(U′) at (ρ, h(ρ), h′(ρ)) plus G_(U′)(ρ, h(ρ), h′(ρ)) − G_(U′)(ρ, h̃(ρ), h̃′(ρ)),

    r δw(r) = ∫_0^r (ρ F(ρ) + θ_1(ρ) δh(ρ) + θ_2(ρ) δw(ρ)) dρ,      |θ_1|, |θ_2| ≤ C_4 ρ,

where |F(ρ)| ≤ C |U − U′| at the point (h(ρ), ρ) of the leaf of U: H_L[U] − H_L[U′] there is bounded by C |U − U′|,
since H_L holds Θ_A, p_A and the metric with its first derivatives, and E_L(ρ, z, q) for the two metrics differs by at
most C (ρ + |q|³) times the difference of the 1-jets of γ3, its value at ρ = 0 being A3 q³/B3. As |δh(ρ)| ≤ ∫_0^ρ t
ω(t) dt,

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
first derivatives there, with derivatives bounded in terms of 𝔐 and c. Let x = (h(|y|), y) be the point of the leaf of
U over y and x̃ = (h̃(|y|), y). Then |σ[U](x) − σ[U′](x̃)| ≤ C (|δw| + ω + |U − U′|(x) + |δh|), the last term from
moving the point of evaluation of U′, whose 1-jet is Lipschitz with constant 𝔐. Let z0′ be the axis point of the leaf
of U′ through x. By [[eq:class-leaf-lipschitz]] for U′, |z0′ − z0| ≤ 2 |δh(|y|)|. Along the leaves of U′ through
(ζ, y), the position and h′ are Lipschitz in ζ by Step 2, and so is h′/r: by Step 2 and |∂_z G|, |∂_q G| ≤ C_4 ρ,
|Δh′(r)|/r ≤ r⁻² ∫_0^r C_4 ρ (|Δh| + |Δh′|) dρ ≤ C_4 (3/2 + 4C_1) |Δζ|. So σ[U′] on the leaf with axis point ζ, over y,
is Lipschitz in ζ with a constant depending only on 𝔐 and c, and |σ[U′](x) − σ[U′](x̃)| ≤ C |δh(|y|)|. Hence

    ‖σ[U] − σ[U′]‖_(L²(𝔻_δ)) ≤ C ‖F‖_(L²(r dr; [0,2δ])) + C ‖(U − U′)(h(|y|), y)‖_(L²(𝔻_δ)),

the L² norms over the leaf of U, in the variable y; the norm of F is at most C times the L² norm of U − U′ on that leaf
over 𝔻_(2δ).

*All leaves.* For x ∈ D ∩ 𝒰_δ the axis point z0 of the leaf of U through x satisfies |z0 − z(p)| ≤ δ + C_0 δ², and over
𝔻_(2δ) that leaf lies in D, by the hypothesis on D, and in 𝒰_(2δ), as |h − z(p)| ≤ δ + 3C_0 δ² ≤ 2δ. In the slice, for
G-invariant functions, the L² norm over a G-invariant set is the L² norm in (z, y) with the weight 2π ρ1, and ρ1 ∈
[ρ1(p)/2, 2ρ1(p)] on 𝒰_(2δ). For fixed y, z0 ↦ h_U(|y|; z0) is increasing with difference quotients in [1/2, 3/2], so
∫ f(z, y) dz = ∫ f(h_U(|y|; z0), y) ∂_(z0) h_U dz0 with ∂_(z0) h_U ∈ [1/2, 3/2] almost everywhere. Squaring the bound of
one leaf, integrating over z0 and changing variables on both sides gives [[eq:class-leaf-wise]]. ∎

### Block B. The new section of chapter 83

### Developments of data of any size through the axes {#sec:civp-axes}

The developments of [[sec:loc-cone-proof]] and [[sec:civp-large]] take cone data equal to the background's near the axes,
and those of [[pending:tier3-section]] take data near the background's. This section drops both conditions for the two
adapted families: cone data of any size, reaching the axes, with or without dust, have a development on a neighbourhood
of the two cones, unique in the double-null gauge, and a maximal development with a continuation criterion
([[thm:civp-axes]]). The development of the whole rectangle is not asserted, and for data of any size it does not
exist in general: a large density makes the cones focus, and then no development in the gauge reaches beyond the focal
sphere ([[rem:civp-axes-scope]]).

The route has four steps. First, the derivatives of the metric functions across each cone obey linear ordinary
differential equations along the generators, through the axes, when the equations are written on the sections as
equations for tensor fields ([[lem:civp-axes-principal]], [[lem:civp-axes-jets]]); so they exist and are bounded on the
whole of each cone. Second, near a corner sphere, Rendall's reduction is carried out with chapter 81's closure at the
axes, about the formal solution Û rather than about a background, for a short time; this needs the planar shear about a
state that is not a solution ([[lem:class-leaf-reference]]), and the time obtained depends only on norms of the data
near the corner ([[prop:civp-axes-corner]]). Third, two developments in the gauge agree, without smallness
([[prop:civp-axes-unique]]). Fourth, corner problems at the spheres of the cones and of null hypersurfaces of the
solution, glued by uniqueness, continue the development along the generators; no a priori estimate is used, the width of
the development being allowed to shrink ([[prop:civp-axes-faces]]).

#### Data reaching the axes {#sec:civp-axes-data}

Let γ̊ be the round metric of S³ and ∇̊ its connection. For an interval I and a function, a vector field or a symmetric
2-tensor field X on S³ depending on s ∈ I, ‖X‖_(C^m(I × S³)) is the largest of the suprema of |∂_s^j ∇̊^i X|_γ̊ over
j + i ≤ m. A metric on D × S³, D a subset of the (u, v)-plane, is in *natural double-null form* if

    g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ(· − b du, · − b du),                                  {#eq:civp-axes-form}

that is g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_AB (dθ^A − b^A du)(dθ^B − b^B du) in every chart (θ^A) of S³, where for each
(u, v) the function Ω > 0, the vector field b and the Riemannian metric γ are smooth on S³, and they depend smoothly on
(u, v). Such a g is a smooth Lorentzian metric on D × S³, for which u and v are null. It is G-invariant with b = b∂_ϑ
and γ = γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2² exactly when Ω, b and γ are G-invariant, since the reflections φ_i ↦ −φ_i
make an invariant vector field a multiple of ∂_ϑ and an invariant symmetric tensor diagonal in (ϑ, φ1, φ2); off the axes
it is then [[eq:loc-double-null]]. Conversely the metric of a class solution in the gauge of [[sec:civp-large]] is in this
form: Ω² = −g(∂_u, ∂_v)/2, γ is the restriction of g to the sections and γ(b, ·) = −g(∂_u, ·) on their tangent vectors,
all smooth on D × S³ because g and the coordinate fields of the product are.

An invariant vector field vanishes at the axes: at a point of axis 2 the rotations of the (x3, x4)-plane fix the point and
act on the plane of the K2-directions without fixed vector, and the reflection in the (x1, x2)-plane through the point
reverses K1. Near axis 2, with x := ϑ, smoothness of the invariant tensors gives, as for [[eq:class-axis-metric]], that
Ω, γ_ϑ and e^(2A_c) are even smooth functions of x, that b is odd, and that e^(2A_s) = sin²x e^(2s) with s even and
γ_ϑ = e^(2s) at x = 0 (the conical condition); near axis 1 the same holds with x := π/2 − ϑ and the roles of A_c and A_s
exchanged. No step below uses these coordinate conditions: the data are tensor fields on S³, and the conditions are
their smoothness written in coordinates.

**Definition {#def:civp-axes-data}** (Cone data through the axes.) Let (u_c, v_c) be a point, λ_u, λ_v > 0, N_o :=
{u_c} × [v_c, v_c + λ_v] and N_i := [u_c, u_c + λ_u] × {v_c}, the *edges*, and S_c := {(u_c, v_c)} × S³ the *corner
sphere*. *Cone data* consist of G-invariant smooth families, in the sense of [[eq:civp-axes-form]], of a function Ω > 0,
a vector field b, a Riemannian metric γ and a function q_in on N_o, and of Ω, b, γ and q_out on N_i, such that: (i) Ω, b
and γ of the two edges agree on S_c; (ii) Ric(∂_v, ∂_v) = q_in and Ric(∂_v, X) = 0 for X tangent to the sections on N_o,
and Ric(L̲, L̲) = q_out on N_i, L̲ := ∂_u + b; and (iii) q_in ≥ 0 and q_out ≥ 0. *Cone data of any sign* omit (iii). Their
*size* in C^m is the largest of ‖ln Ω‖, ‖b‖, ‖γ‖ and ‖q_A‖ in C^m of the two edges, and they are *κ-nondegenerate*,
κ ∈ (0, 1], if γ ≥ κ γ̊ on both edges.

In (ii), Ric(∂_v, ∂_v) and Ric(∂_v, X) on N_o are those of any metric in natural double-null form inducing the functions
of N_o, and Ric(L̲, L̲) on N_i those of any such metric inducing the functions of N_i: off the axes they are given by
[[eq:loc-cone]] and by the last line of [[eq:loc-cone-frame-ricci]] in terms of the functions on that edge, and they are
continuous up to the axes. The free part of cone data is that of [[def:loc-cone-data]]: Ω on both edges, b on N_i, the
conformal class of γ and the densities, the corner values being arbitrary subject to (i). In the normalised form
γ = ỹ² γ̂ with μ_γ̂ = μ_γ̊, μ the Riemannian volume density, ỹ = (μ_γ/μ_γ̊)^(1/3) is a smooth positive function on S³, and
by the proof of [[prop:loc-cones]], with trace and norm of ½ ∂_v γ taken in γ, the first constraint on N_o reads

    ∂_v² ỹ − 2 ∂_v ln Ω ∂_v ỹ + (1/3)(¼ |∂_v γ̂|²_γ̂ + q_in) ỹ = 0,                        {#eq:civp-axes-raychaudhuri}

a linear ordinary differential equation along each generator with coefficients smooth on S³, axis generators included;
on N_i with b = 0 the constraint is the same equation with u in place of v. Positivity of ỹ on an edge is the absence of
a focal sphere there. The constraint Ric(∂_v, X) = 0 is a linear first-order equation for ∂_v b along the generators,
with the leading coefficient (1/(4Ω²)) γ(∂_v ·, X) (the second line of [[eq:loc-cone]]).

A *class solution in the gauge* on D × S³, for a set D of the (u, v)-plane, is as in [[sec:civp-large]]: a smooth class
solution (g, v, u, q_in, q_out) of [[eq:class-system]] with N_f = 2, v the phase of the density q_in and u that of
q_out, whose metric is in natural double-null form. It *induces* cone data on edges contained in D if its functions Ω, b,
γ and the densities restrict to them. A set D is a *past set* relative to (u_c, v_c) if [u_c, u] × [v_c, v] ⊂ D for every
(u, v) ∈ D.

#### The derivatives across the edges {#sec:civp-axes-jets}

**Lemma {#lem:civp-axes-principal}** (The equations across an outgoing edge.) Let g be a metric in natural double-null
form on {0 ≤ u < ε} × I × S³, I an interval of v, smooth up to u = 0, q_in and q_out any functions, E := Ric(g) − q_in
dv ⊗ dv − q_out du ⊗ du and ℰ := (E(L̲, ∂_v), E(L̲, ·), E(·, ·)), the last two restricted to vectors tangent to the
sections: for each (u, v) a function, a 1-form and a symmetric 2-tensor field on S³. Put J_j := ∂_u^j (Ω, b, γ) at
u = 0, for j ≥ 0.

(a) ℰ contains no second u-derivative of Ω, b, γ, and does not contain q_in or q_out. So for j ≥ 1, ∂_u^(j−1) ℰ at
u = 0 is a smooth expression in J_0, …, J_j and their derivatives along N_o := {0} × I × S³ of order at most two.

(b) For j ≥ 2 it is affine in J_j: ∂_u^(j−1) ℰ|_(u=0) = 𝔏_j J_j + 𝔖_j, with 𝔖_j depending on J_0, …, J_(j−1) only and,
for J = (ω, β, h),

    𝔏_j J = (−(2/Ω) ∂_v ω − ½ tr_γ ∂_v h, −(1/(4Ω²)) γ(∂_v β, ·), (1/(2Ω²)) ∂_v h) + 𝔏_j′ J,          {#eq:civp-axes-principal}

Ω and γ those of J_0. The operator 𝔏_j′ contains no ∂_v. Its first and third components are linear in (ω, β, h) at each
point, with no derivative on S³; its second component contains derivatives on S³ of order at most one of ω and h and
none of β. The coefficients are smooth on N_o, axes included, and built from J_0, J_1 and their first derivatives.

(c) If g is G-invariant, then (b) holds also for j = 1, the coefficients of 𝔏_1 being built from J_0 alone, and for
j ≥ 1 the first and third components of ∂_u^(j−1) ℰ|_(u=0) do not depend on the β-component of J_j.

*Proof.* (a), (b) Work in coordinates (u, v, θ^A), (θ^A) any chart of S³. The components of g are g_uv = −2Ω², g_uA =
−γ_AB b^B, g_uu = γ_AB b^A b^B, g_AB = γ_AB and g_vv = g_vA = 0, and since g(L̲, ∂_v) = −2Ω², g(L̲, L̲) = g(L̲, ∂_A) = 0 and
g(∂_v, ∂_v) = g(∂_v, ∂_A) = 0, the inverse metric is −(2Ω²)⁻¹ (L̲ ⊗ ∂_v + ∂_v ⊗ L̲) + γ^AB ∂_A ⊗ ∂_B: g^uu = g^uA = g^vv
= 0, g^uv = −1/(2Ω²), g^vA = −b^A/(2Ω²), g^AB = γ^AB. From the Christoffel symbols,

    Ric_μν = ½ g^αβ (∂_α∂_μ g_βν + ∂_α∂_ν g_βμ − ∂_μ∂_ν g_αβ − ∂_α∂_β g_μν) + Q_μν,

with Q_μν a polynomial in g^αβ and the first derivatives of the g_αβ, quadratic in the latter. A term ∂_u∂_u g_·· can
arise from the first sum only with α = μ = u, then β = v and ν = u, as g^uβ ≠ 0 only for β = v and g_vν ≠ 0 only for
ν = u; from the second only with μ = ν = u; from the third only with μ = ν = u; and the fourth would need g^uu ≠ 0.
So ∂_u² occurs only in Ric_uu, which is not in ℰ: E(L̲, ∂_v) = E_uv + b^A E_Av and E(L̲, ∂_A) = E_uA + b^B E_BA, and
T(L̲, ∂_v) = T(L̲, ∂_A) = T(∂_A, ∂_B) = 0 because dv(L̲) = du(∂_v) = du(∂_A) = dv(∂_A) = 0. Every term of ℰ is therefore a
product of factors each containing at most one u-derivative, and ∂_u^(j−1) at u = 0 produces u-derivatives of order at
most j. J_j appears only where all j − 1 derivatives fall on one factor that already contains ∂_u; for j ≥ 2 at most
one factor of a term can receive them, so the dependence on J_j is affine, through ∂_u ∂_v g, ∂_u ∂_A g and ∂_u g at
u = 0, the components of ∂_u^j g being J_j-linear modulo lower jets.

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
only from the ∂_u∂_C-terms, which occur only in the second component and hold Ω and γ only; the terms with at most
first derivatives give zero-order terms in J_j. Every coefficient is a polynomial in the components of g, of the inverse
metric and of their derivatives at u = 0 in the chart, so smooth on N_o; it is independent of the chart, the components
of ℰ being tensorial on the sections.

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
variable u from 0, which commutes with G, and θ̃ := ψ_(u,v)⁻¹(θ). Then dθ − b du = Dψ (dθ̃ − b̃ dv) with b̃ := −Dψ⁻¹ ∂_v ψ,
and g = −2Ω̃² (du ⊗ dv + dv ⊗ du) + γ̃(· − b̃ dv, · − b̃ dv) with Ω̃ := Ω ∘ ψ and γ̃ := ψ^*γ: the form
[[eq:civp-axes-form]] with u and v exchanged, equal to the given one on {v = 0}, where ψ = id. The lemma applies there
with u and v exchanged, and the v-derivatives at v = 0 of (Ω, b, γ) and of (Ω̃, b̃, γ̃) determine one another: ∂_v ψ =
−Dψ b̃ with ψ = id at v = 0, b = (∂_u ψ) ∘ ψ⁻¹, Ω = Ω̃ ∘ ψ⁻¹ and γ = ψ_*γ̃.

**Lemma {#lem:civp-axes-jets}** (The derivatives across the edges through the axes.) Let cone data of any sign be given on
edges N_o = {0} × [0, λ_v] and N_i = [0, λ_u] × {0}, with b = 0 on N_i. There are unique sequences a_j (j ≥ 0) on N_o and
b_k (k ≥ 0) on N_i of G-invariant smooth families of a function, a vector field and a symmetric 2-tensor field on S³,
with a_0 and b_0 the data, together with unique invariant smooth densities a_j^ρ, b_k^ρ (of q_in μ_γ and q_out μ_γ),
such that for every metric g in natural double-null form near N := N_o ∪ N_i with ∂_u^j (Ω, b, γ) = a_j on N_o and ∂_v^k
(Ω, b, γ) = b_k on N_i for all j, k, and densities with the corresponding derivatives, the evolution components ℰ of
[[lem:civp-axes-principal]] on N_o, the corresponding components with u and v exchanged on N_i, and the conservation
laws vanish to infinite order on N. Moreover:

(i) (Linear and triangular.) For j ≥ 1, a_j = (ω, β, h) solves along each generator of N_o the linear system 𝔏_j a_j =
−𝔖_j: a linear ordinary differential equation in v for (ω, h) at each point of S³, followed by one for β whose
inhomogeneous term contains (ω, h) and their first derivatives on S³; the initial values at v = 0 are the u-derivatives
of the data of N_i at the corner.
The same holds on N_i, in the form of [[lem:civp-axes-principal]] with u and v exchanged. No Riccati term occurs at any
order, and the a_j exist on the whole of N_o and the b_k on the whole of N_i, whatever their lengths.

(ii) (Corner.) ∂_v^k a_j = ∂_u^j b_k on S_c for all j, k.

(iii) (Bounds.) If the data have size at most Λ in C^m on edges of length at most 1 and are κ-nondegenerate, then for
4j ≤ m, ‖a_j‖_(C^(m−4j)) + ‖b_j‖_(C^(m−4j)) ≤ C_j, with C_j depending only on j, m, Λ and κ.

(iv) (Solutions.) Every class solution in the gauge on D × S³, D ⊃ N a past set relative to (0, 0) containing a
neighbourhood of N in it, that induces the data has ∂_u^j (Ω, b, γ) = a_j on N_o and ∂_v^k (Ω, b, γ) = b_k on N_i, and the
corresponding densities.

(v) a_j on N_o ∩ {v ≤ v′} depends only on the data on N_o ∩ {v ≤ v′} and on the derivatives at the corner of the data
of N_i, and b_k on N_i ∩ {u ≤ u′} only on the data on N_i ∩ {u ≤ u′} and the derivatives at the corner of the data of
N_o.

*Proof.* *Existence and uniqueness on N_o.* Induction on j. For j ≥ 1, given a_0, …, a_(j−1), [[lem:civp-axes-principal]]
(b), (c) turns ∂_u^(j−1) ℰ|_(u=0) = 0, for invariant a_j, into the system 𝔏_j a_j = −𝔖_j: by [[eq:civp-axes-principal]]
the first and third components form a linear system for (ω, h) whose v-derivatives have the invertible coefficient
matrix ((−2/Ω, −½ tr_γ), (0, (1/(2Ω²)) id)), with no derivative on S³ and no β; the second is then a linear equation
for γ(∂_v β, ·)/(4Ω²) with coefficients and an inhomogeneous term smooth on N_o. Linear ordinary differential equations
with smooth coefficients have unique solutions on the whole interval, depending smoothly on the point of S³ and on v;
the solution with the initial values ∂_u^j b_0 at the corner is invariant, since the system is natural
and commutes with G and the data are invariant, so its image under each element of G solves it with the same initial
values. Conversely every invariant a_j with ∂_u^(j−1) ℰ|_(u=0) = 0 solves this system. For the densities put ρ_in :=
q_in μ_γ and ρ_out := q_out μ_γ: by [[lem:loc-cone-ricci]] (b), written in a chart, the conservation laws are ∂_u ρ_in +
ℒ_b ρ_in = 0 and ∂_v ρ_out = 0 for these densities on S³, so ∂_u^j ρ_in at u = 0 is ∂_u^(j−1) of −ℒ_b ρ_in, a polynomial
in lower jets, and ∂_u^j ρ_out is constant along each generator, with its value at the corner given by the data of N_i.

*On N_i* the same, in the form with u and v exchanged given before the lemma, with the generators of N_i, the integral
curves of ∂_u (b = 0 there), and the initial values at u = 0 the v-derivatives of the data of N_o at the corner; the change of form is smooth through the
axes, ψ commuting with G.

*Vanishing to infinite order.* For g as in the statement, ∂_u^(j−1) ℰ vanishes on N_o for every j ≥ 1 and the
corresponding derivatives on N_i; all their derivatives along N then vanish, and so ℰ and the components on N_i vanish
to infinite order on N; likewise the conservation laws.

(ii) Off the axes the a_j and b_k solve the equations of the proof of [[lem:loc-cone-jets]] with the same initial values,
and that proof, being local in ϑ, applies at every ϑ ∈ (0, π/2) to cone data of any sign; so they are the sequences
constructed there on N ∩ {0 < ϑ < π/2}, and (ii) holds there by [[lem:loc-cone-jets]] (i). At the axes it holds by
continuity.

(iii) For a linear system ∂_v Z = MZ + h on an interval of length at most 1, ‖Z‖_(C^r) ≤ C(r, ‖M‖_(C^r))(‖Z(0)‖_(C^r)
+ ‖h‖_(C^r)), by differentiating with ∇̊ and in v. With Ω ≥ e^(−Λ) and γ ≥ κγ̊ the leading coefficients of
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

(a) (Past an end.) Let w ∈ (0, 1] and f a smooth family on [−w, 0] × S³ of functions, vector fields or symmetric
2-tensor fields on S³. There is a smooth family F on [−w, 1] × S³ with F = f on [−w, 0] and ‖F‖_(C^m([−w,1]×S³)) ≤
C_m w^(−m) ‖f‖_(C^m([−w,0]×S³)), depending linearly on f and G-invariant when f is.

(b) (Short pieces.) Let f be a smooth family on [0, w] × S³, w > 0, let Λ bound |∇̊^i ∂_s^j f| at s = 0 for i, j ≤ m,
and let L bound |∇̊^i ∂_s^(m+1) f| on [0, w] × S³ for i ≤ m. For 0 < a ≤ min(w, 1/2, 1/(1 + L)) there is a smooth family
F on [0, 1] × S³, G-invariant when f is, with F = f on [0, a], F = Σ_(j≤m) ∂_s^j f(0) s^j/j! on [2a, 1], and
‖F‖_(C^m([0,1]×S³)) ≤ C_m (Λ + 1).

(c) (Solving the constraints past an end.) Let cone data of any sign, κ-nondegenerate and of size at most Λ in C^m, be
given on edges N_o = {0} × [0, λ_v] and N_i = [0, λ_u] × {0}, λ_u, λ_v ≤ 1, with b = 0 on N_i. On each edge let ln Ω,
the density, and γ̂ := (μ_γ̊/μ_γ)^(2/3) γ be extended to smooth invariant families on [0, 1] with C^m norms at most Λ, γ̂
positive definite with μ_γ̂ = μ_γ̊, and keep b = 0 on the extension of N_i. There are ℓ ∈ (0, 1], C and κ′ > 0,
depending only on m, Λ and κ, such that solving the constraints from the corner with the given corner values gives cone
data of any sign on {0} × [0, max(λ_v, ℓ)] and [0, max(λ_u, ℓ)] × {0}, equal to the given data on N_o and N_i, of size at
most C in C^(m−3), κ′-nondegenerate, and with these free functions.

(d) (The shift on the ingoing edge.) For cone data with any b on N_i, let ψ_u be the flow on S³ of the vector fields
b(u, 0, ·): ∂_u ψ_u = b(u, 0, ψ_u), ψ_0 = id. The change of coordinates θ = ψ_u(θ′), independent of v, carries every
metric in natural double-null form to one in natural double-null form, with Ω′ = Ω ∘ ψ_u, γ′ = ψ_u^* γ and b′ =
ψ_u^*(b(u, v, ·) − b(u, 0, ·)). It commutes with G, it is the identity on N_o except that b becomes b − b(0, 0, ·) there,
and b′ = 0 on N_i. The new functions on the edges are cone data, of size in C^m bounded by C_m times a function of the
size of the old ones in C^(m+1), and κ-nondegeneracy becomes κ″-nondegeneracy with κ″ depending only on κ and that size.
A class solution in the gauge for the new data gives one for the old data by the inverse change.

*Proof.* (a) By [LY22, Theorem 1 (i)] ([[thm:std-ly-extension]]) there are numbers a_j and b_j > 0, j ∈ ℤ, with
Σ_j a_j (−b_j)^i = 1 and A_i := Σ_j |a_j| b_j^i < ∞ for every integer i ≥ 0; the second follows from Σ_j 2^(δ_i|j|)
|a_j| b_j^i < ∞. Let χ be smooth on ℝ with χ = 1 on [−1/3, 0] and χ = 0 on (−∞, −2/3], put f_1(s) := χ(s/w) f(s) for
−w ≤ s ≤ 0 and f_1 := 0 for s < −w, and F(s) := f(s) for s ≤ 0 and F(s) := Σ_j a_j f_1(−b_j s) for s > 0. The series
of the derivatives ∂_s^i ∇̊^α converge uniformly, since |∂_s^i ∇̊^α (f_1(−b_j s))| ≤ b_j^i sup |∂^i ∇̊^α f_1|, so F is
smooth on (0, 1] with |∂_s^i ∇̊^α F| ≤ A_i sup |∂^i ∇̊^α f_1|, and as s → 0⁺, ∂_s^i ∇̊^α F → Σ_j a_j (−b_j)^i ∂^i ∇̊^α f(0)
= ∂^i ∇̊^α f(0), χ being 1 near 0; so F is smooth on [−w, 1]. The derivatives of χ(s/w) of order i are at most C w^(−i).
F is linear in f and acts at each point of S³, so it commutes with G.

(b) Let P(s) := Σ_(j≤m) ∂_s^j f(0) s^j/j!, so ‖P‖_(C^m([0,1]×S³)) ≤ C_m Λ, and g := f − P on [0, w]. Every ∇̊^α g with
|α| ≤ m has vanishing s-derivatives of order at most m at s = 0, and ∂_s^(m+1) P = 0, so by Taylor's formula
|∂_s^i ∇̊^α g(s)| ≤ L s^(m+1−i) for i ≤ m. Apply (a) to s ↦ g(a + s), −a ≤ s ≤ 0, with w := a, and multiply the extension
by ψ((s − a)/a), ψ smooth with ψ = 1 on (−∞, 1/2] and ψ = 0 on [1, ∞): the result g_e equals g on [0, a] and vanishes for
s ≥ 2a. In (a) the bound is A_i sup |∂^i ∇̊^α f_1| with f_1 = χ((s − a)/a) g, at most C_m Σ_(i′≤i) a^(−(i−i′)) L a^(m+1−i′)
≤ C_m L a^(m+1−i), and the cut-off ψ costs the same powers of a; so ‖g_e‖_(C^m([0,1]×S³)) ≤ C_m L a ≤ C_m. Put F :=
P + g_e.

(c) The proof of [[lem:loc-cone-extension]] holds with the following changes. The free functions are the given
extensions, not Borel sums at the end, and are not measured against a background; ϕ and ℓ_i are replaced by ỹ and γ̂,
and (∗) there by [[eq:civp-axes-raychaudhuri]], whose coefficients have C^(m−1) norms at most C(Λ). On the given edges
ỹ = (μ_γ/μ_γ̊)^(1/3) ≥ κ^(1/2) and |∂ ln ỹ| ≤ C(Λ), so the Gronwall bound there keeps ỹ ≥ ỹ(λ)/2 on [λ, λ + ℓ] for ℓ
depending only on m, Λ and κ; with ỹ ≤ C(Λ), γ = ỹ² γ̂ and the C¹ bound of γ̂, γ ≥ κ′ γ̊ after decreasing ℓ. The second
constraint on N_o is linear in b, through ∂_v b and ∂_v² b, off the axes by the second line of [[eq:loc-cone]] and at the
axes by continuity, its leading coefficient being (1/(4Ω²)) γ(∂_v ·, X); solving it from the corner values loses the
derivatives counted there, and the size of the extension is at most C in C^(m−3).

(d) dθ = Dψ_u dθ′ + b(u, 0, ψ_u) du, so dθ − b(u, v, θ) du = Dψ_u (dθ′ − b′ du) with b′ as stated, and γ(Dψ_u ·,
Dψ_u ·) = ψ_u^* γ. ψ_u commutes with G because b is invariant, and ψ_0 = id. The constraints are components of the
Ricci tensor of the same metric along the same generators: ∂_v at fixed θ′ is ∂_v at fixed θ, and on N_i, ∂_u at fixed
θ′ is L̲. The bounds follow from those of ψ_u, whose derivatives of order m are bounded by the derivatives of b of order
at most m. ∎

**Proposition {#prop:civp-axes-formal}** (The formal solution through the axes.) Let the data of [[lem:civp-axes-jets]]
have size at most Λ in C^m, m ≥ 6k + 18, on edges of length λ_u, λ_v ∈ [λ_0, 1], be κ-nondegenerate, and let 0 < δ_e ≤
1/8. Extend a_0 to v ∈ [−1, 0] and b_0 to u ∈ [−1, 0] by [[lem:civp-axes-extension]] (a), and put X_0(u, v) := a_0(v) +
b_0(u) − a_0(0). There are G-invariant smooth families X̂ = (Ω̂, b̂, γ̂) and ρ̂_in, ρ̂_out on 𝒮_e := [−1, λ_u] × [−1, λ_v]
with ∂_u^j X̂ = a_j on N_o and ∂_v^k X̂ = b_k on N_i for all j, k, likewise for the densities, such that, with constants
depending only on k, Λ, κ and λ_0 unless stated otherwise:

(a) ‖X̂‖_(C^(k+3)(𝒮_e)) ≤ C, C depending also on δ_e;

(b) |X̂ − X_0| ≤ C_b (|u| + |v|) on 𝒮_e, and |b̂| ≤ C_b |v| where u ≥ 2δ_e, with C_b not depending on δ_e;

(c) at the points of 𝒮_e with |u|, |v| ≤ d, and at those within distance d of N, for a number d > 0,
Ω̂ ≥ e^(−Λ)/2 and γ̂ ≥ (κ/2) γ̊; there the metric Ĝ of [[eq:civp-axes-form]] with the functions X̂ is a smooth
G-invariant Lorentzian metric for which u and v are null, and Ĝ, q̂_in := ρ̂_in/μ_γ̂ and q̂_out := ρ̂_out/μ_γ̂ induce the
data on N;

(d) E := Ric(Ĝ) − q̂_in dv ⊗ dv − q̂_out du ⊗ du and the conservation laws vanish to infinite order on N.

*Proof.* Apply [[lem:loc-cone-borel]] to the components of a_j − ∂_u^j X_0 and b_k − ∂_v^k X_0, which agree at the corner
by [[lem:civp-axes-jets]] (ii) and vanish for j = 0 and k = 0, in the Cartesian components on ℝ⁴ ⊃ S³ of tensor fields on
S³, with Y replaced by S³, r := k + 3, ε_0 := δ_e and γ_0 := 1, and add X_0. That proof uses Y only as a parameter set,
the Borel sums being taken in u and v with cut-offs depending on u and v alone; so the sums are G-invariant when their
coefficients are, and the bound of its part (b) holds with ∇̊-derivatives, which gives (a) by [[lem:civp-axes-jets]]
(iii), since m − 4(k + 3) ≥ 2(k + 3). (b) is the argument of the paragraph on the reference metric in case (II) of
[[sec:loc-cone-reduced]], which uses only the form of the Borel sums: the terms of index 0 vanish on N, as the jets of
order 0 of X − X_0 vanish, every other term vanishes at u = 0 (respectively v = 0) and is at most |u| (respectively |v|)
times a bound of the jets of order at most k + 3 or 2^(−j); and b vanishes on N_i and on N_o at v = 0, so b_0 = 0 and
|a_0^b(v)| ≤ Λ |v|. (c) X_0 equals the data on N, so |X_0 − X| ≤ Λ (|u| + |v|) with X the data at the nearest point of
N, Λ being replaced by the bound of the extended a_0 and b_0 in C^1, and Ω ≥ e^(−Λ), γ ≥ κ γ̊ there; with (b) this
gives (c) for d a small multiple, depending only on these bounds, of min(1, κ, e^(−Λ)). (d) The evolution
components and the conservation laws vanish to infinite order on N by [[lem:civp-axes-jets]]. The other components of E
vanish to infinite order on N by the proof of [[prop:loc-cone-formal]] (c), which uses the contracted Bianchi identity in
the form [[eq:loc-cone-bianchi]] and the constraints of the data and is local in ϑ: it applies off the axes, and at the
axes by continuity, E being a smooth tensor field. ∎
