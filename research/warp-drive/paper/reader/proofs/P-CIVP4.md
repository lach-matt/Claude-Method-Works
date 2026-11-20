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
