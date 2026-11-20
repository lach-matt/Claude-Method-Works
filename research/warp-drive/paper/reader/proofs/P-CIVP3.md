### Developments of cone data through the axes {#sec:loc-axis}

This section develops cone data near the background's data whose perturbation reaches the axes, on the whole rectangle
spanned by the two cones. [[thm:loc-cone-development]] does not apply to such data: its proof uses the augmented system
of [[sec:class-augmented]] only off the axes, where it is local, and keeps the background near the axes
([[rem:loc-cone-scope]] (ii)). At an axis the Raychaudhuri equation of a family holds the planar shear of its null
hypersurfaces, and [[lem:class-leaf-differences]] computes the planar shear at a point from the leaf through it, the
section of the null hypersurface by a slice, by an integral from the axis along the leaf (Step 6 of the proof of
[[thm:class-stability]]). An energy estimate on a region therefore needs, at each point of a slice of the region near
an axis, the arc of the leaf from the axis to that point to lie in the region. For a time that increases with u and
with v the sections of the cones by the slices are spheres of the data's double-null coordinates, and each of them is a
leaf of both families of every state that has the right values and first derivatives along it ([[lem:loc-axis-leaf]]).
The leaves of a state foliate a neighbourhood of an axis and do not cross these spheres, so the part of a slice to the
past of the cones, and the part between them, consist of arcs of leaves; on such a set the planar shears of two states
differ in L² by at most a constant times the difference of the states, the constant not depending on the set
([[lem:loc-axis-shear]]). With these two facts the construction of [[sec:loc-cone-reduced]], case (I), runs with the
closure of the Raychaudhuri equation at the axes and without a cut-off near them. The constraints propagate on the
region bounded by the two cones and one slice, which contains the whole rectangle when the time is adapted to it
([[eq:loc-axis-time]]). Two solutions in one wave gauge that agree to all orders on the past faces of a double-null
rectangle agree on it, with no smallness of either ([[lem:loc-axis-dependence]]); this gives uniqueness in the
double-null gauge and localisation.

*The background on a rectangle.* We use the notation of [[sec:loc-cone-setting]] and [[sec:loc-cone-reduced]]. Let u_1,
v_1 > 0, δ_1 ∈ (0, min(u_1, v_1)/2] and Q1 := [0, u_1] × [0, v_1]. A *background on Q1 with margin δ_1* is a round
metric g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with σ_e and R_e > 0 smooth on Q^♯ := [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 +
2δ_1], together with smooth profiles 𝒜(v), ℬ(u) ≥ 0, that solves [[eq:two-dust-limit]] on Q^♯ ∩ F. With l_u := u_1 +
δ_1 and l_v := v_1 + δ_1 the set 𝒮 of [[eq:loc-cone-collar]] lies in Q^♯ and the restriction is a background on 𝒮; so
N_o = {0} × [0, v_1 + 2δ_1] and N_i = [0, u_1 + 2δ_1] × {0}. The double-null functions, the densities q̊_A and the
state Ů of those sections are defined on all of Q^♯, and we put C_* := sup over Q^♯ of e^(σ_e)/R_e.

**Theorem {#thm:loc-axis}** (Development of cone data through the axes.) Let k ≥ 9, m_0 = 6k + 18 and m_1 = 12k + 42,
and let a background on Q1 with margin δ_1 be given. Let cone data through the axes ([[def:loc-axis-data]]) be given on
{0} × [0, v_1] and [0, u_1] × {0}, in the normalised gauge and with nonnegative densities, and let ε be their size in
C^(m_1). There are ε_0, C, ε_2 > 0, depending only on k, u_1, v_1, δ_1 and the background, such that for ε ≤ ε_0 the
following hold.

(a) *Existence.* There is a class solution in the gauge through the axes on Q1 × S³ ([[def:loc-axis-data]]), with an
ingoing family of phase v and density q_in and an outgoing family of phase u and density q_out, so that Ric(g) = q_in
dv ⊗ dv + q_out du ⊗ du, that induces the cone data on {0} × [0, v_1] and on [0, u_1] × {0}. Its metric is smooth on Q1
× S³, the axes included.

(b) *Estimate.* Its fields ln Ω, γ and b and its densities differ from the background's by at most Cε in C^(k−4), in
the norms of [[def:loc-axis-data]].

(c) *Uniqueness.* Let Q1′ := [0, u_1′] × [0, v_1′] ⊂ Q1 with u_1′, v_1′ > 0. A class solution in the gauge through the
axes on Q1′ × S³ that induces the cone data on {0} × [0, v_1′] and on [0, u_1′] × {0}, and whose fields differ from the
background's by at most ε_2 in C^(k−4), equals the solution of (a) on Q1′ × S³.

(d) *Localisation.* If the data equal the background's on {0} × [0, v_K) and on [0, u_K) × {0}, where u_K, v_K > 0, the
solution equals the background, with its densities, at the points of Q1 × S³ with u < u_K and v < v_K. If the data
equal the background's at the points with ϑ < ϑ_a′, where ϑ_a′ ∈ (0, π/4], the solution equals the background at the
points of Q1 × S³ with ϑ < ϑ_a′ − 2C_* (uv)^(1/2); likewise, for ϑ_b′ ∈ [π/4, π/2), with ϑ > ϑ_b′ and ϑ > ϑ_b′ + 2C_*
(uv)^(1/2).

Data with q_in = 0 and q_out = 0 are vacuum data, and their development is vacuum, the densities being transported.
Decreasing ε_0 so that Cε_0 ≤ ε_2, by (b) and (c) the solution on Q1′ × S³ depends only on the data on the two edges of
Q1′; in particular it does not depend on how they are extended beyond u_1 and v_1 in the proof. For data that equal the
background's near the axes, [[thm:loc-cone-development]] gives a development on the set G_* of [[eq:loc-cone-domain]];
on every rectangle [0, u′] × [0, v′] ⊂ G_* it coincides with the solution of (a), by (c), its fields being within Cε of
the background's in C^(k−4) by [[thm:loc-cone-development]] (c). The theorem is proved at the end of
[[sec:loc-axis-reduced]]; [[cor:loc-axis-cones]] applies it to the background of [[sec:bg-data]].

#### Cone data through the axes {#sec:loc-axis-data}

**Definition {#def:loc-axis-data}** (Fields smooth through the axes.) Let D be a set of the (u, v)-plane or one of the
edges N_o, N_i. Functions Ω > 0, γ_ϑ > 0, A_c, A_s and b of the points of D and of ϑ ∈ (0, π/2) are *smooth through the
axes* if the field of symmetric forms [[eq:loc-double-null]] that they define at the points of D × S³ off the axes
extends to a smooth field of Lorentzian forms on D × S³. Since g(∂_u, ∂_v) = −2Ω², the restriction of g to the tangent
spaces of the spheres is γ := γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2², and g(∂_u, X) = −γ(b∂_ϑ, X) for X tangent to the
spheres, this holds exactly when ln Ω extends to a smooth G-invariant function, γ to a smooth family over D of
G-invariant Riemannian metrics on S³, and b∂_ϑ to a smooth family of G-invariant vector fields on S³. We call ln Ω, γ
and the vector field b∂_ϑ, which we also write b, the *fields*. A density is smooth through the axes if it extends to a
smooth G-invariant function. A *class solution in the gauge through the axes* on D × S³, D ⊂ F, is a class solution in
the gauge ([[sec:loc-cone-setting]]) whose fields are smooth through the axes, in place of being equal to the
background's near the axes. *Cone data through the axes*, of either sign, are defined as in [[def:loc-cone-data]], with
(iii) there replaced by: their fields and densities are smooth through the axes. The C^r norm of a field T on an edge
is the supremum of |∂^i ∇̊^l T| over i + l ≤ r, ∂ the derivative along the edge at a fixed point of S³ and ∇̊, |·| the
Levi-Civita connection and the norm of the unit round metric dΩ₃²; on a set D the derivatives in u and in v enter
alike. The *size in C^r* of cone data through the axes is the largest C^r norm, over the two edges, of the differences
of their fields and densities from the background's.

**Lemma {#lem:loc-axis-constraints}** (The constraints through the axes.) Let ln Ω, γ and b be fields on N_o smooth
through the axes, q_in a density smooth through the axes, dvol_1 the volume form of dΩ₃², and put

    χ := ½ ∂_vγ,      Y := (dvol_γ/dvol_1)^(1/3),      γ̂ := Y^(−2) γ,      W := ∂_v b.

(a) On N_o, with E := Ric(g) − q_in dv ⊗ dv − q_out du ⊗ du,

    E(∂_v, ∂_v) = −(3/Y)(∂_v²Y − 2 ∂_v ln Ω ∂_vY + (1/12) |∂_vγ̂|²_γ̂ Y) − q_in,
    E(∂_v, X) = (4Ω²)⁻¹ (γ(∂_vW, X) + (tr_γχ − 2 ∂_v ln Ω) γ(W, X) + 2χ(W, X)) + 𝔯(X),                {#eq:loc-axis-cone}

for X tangent to S³, where 𝔯 is the 1-form X ↦ E(∂_v, X) of the fields ln Ω, γ and 0 in place of b; 𝔯 is smooth and
G-invariant and depends only on Ω and γ on N_o. In the normalised gauge, on N_i, E(L̲, L̲) = E(∂_u, ∂_u) is given by
the first line with ∂_u, the fields of N_i and q_out in place of ∂_v, those of N_o and q_in.

(b) Let ln Ω, a smooth family γ̂ of G-invariant Riemannian metrics on S³ with dvol_γ̂ = dvol_1, and q_in, of either
sign, be given on N_o ∩ {v ≤ v′}, smooth through the axes, together with smooth G-invariant functions Y_0 > 0 and Y_1
and G-invariant vector fields b_0 and W_0 on S³. Let Y solve E(∂_v, ∂_v) = 0, which by (a) is a linear equation for Y,
with Y = Y_0 and ∂_vY = Y_1 at v = 0. Then Y is smooth on N_o ∩ {v ≤ v′}; on every N_o ∩ {v ≤ v″} on which Y > 0, γ :=
Y²γ̂ and the solution b of E(∂_v, ·) = 0 with b = b_0 and ∂_vb = W_0 at v = 0 are smooth through the axes, and ln Ω, γ,
b and q_in satisfy the constraints of (ii) of [[def:loc-cone-data]] on N_o. Every set of fields and densities smooth
through the axes that satisfies them arises in this way. The same holds on N_i in the normalised gauge, with the first
line of (a) only. In the coordinates, γ̂ = (sin ϑ cos ϑ)^(2/3)(e^(2ℓ_1) dϑ² + e^(2ℓ_2) dφ1² + e^(2ℓ_3) dφ2²) and Y =
e^ϕ (sin ϑ cos ϑ)^(−1/3), with ϕ and the ℓ_i of [[prop:loc-cones]] and [[lem:loc-cone-in]]: their free data are smooth
through the axes exactly when this γ̂ is a smooth metric on S³. For the background, γ̂ = dΩ₃² and Y = R_e.

(c) Let a background on Q1 with margin δ_1 be given, and cone data through the axes on {0} × [0, v_1] and [0, u_1] ×
{0}, in the normalised gauge, of size ε in C^(2p), p := m_0 + 3. For ε ≤ ε_0 they extend to cone data of either sign
through the axes on N_o and N_i, in the normalised gauge, of size at most Cε in C^(m_0) and equal to the background's
at the points of every G-invariant open set of S³ at which the given data are; ε_0 and C depend only on k, u_1, v_1,
δ_1 and the background.

*Proof.* (a) Every term is a smooth G-invariant field on N_o, the fields being smooth and Y positive. Off the axes, in
the coordinates, dvol_γ = e^(ϰ_1 + ϰ_2 + ϰ_3) dϑ dφ1 dφ2 = e^(3ϕ) dϑ dφ1 dφ2 and dvol_1 = sin ϑ cos ϑ dϑ dφ1 dφ2, so Y
and γ̂ are those stated in (b); γ̂ is diagonal with the entries (sin ϑ cos ϑ)^(2/3) e^(2ℓ_i), so |∂_vγ̂|²_γ̂ = 4 Σ_i
(∂_vℓ_i)². The proof of [[prop:loc-cones]], which does not use that Ω is the background's, gives E(∂_v, ∂_v) = −3y″/y +
6 (ln Ω)′ y′/y − Σ_i (ℓ_i′)² − q_in with y := e^ϕ and ′ := ∂_v; as y = Y (sin ϑ cos ϑ)^(1/3), with a factor that does
not depend on v, y″/y = Y″/Y and y′/y = Y′/Y, which is the first line. With W = (∂_v b) ∂_ϑ and 𝒱 := γ_ϑ^(1/2) e^(A_c +
A_s), the second line of [[eq:loc-cone]] reads E(∂_v, ∂_ϑ) = (γ_ϑ/(4Ω²))(∂_v²b + ∂_v ln(γ_ϑ 𝒱 Ω⁻²) ∂_v b) + r, with r
of [[eq:loc-cone-r]], which does not contain b, so that r = 𝔯(∂_ϑ); and ∂_v ln 𝒱 = tr_γχ and γ_ϑ ∂_v ln γ_ϑ ∂_v b =
2χ(W, ∂_ϑ). This is the second line at X = ∂_ϑ; at X = K_i both sides vanish, by the reflection φ_i ↦ −φ_i, W being a
multiple of ∂_ϑ and χ diagonal. So both lines hold off the axes and, both sides being continuous, on N_o. On N_i, with
b = 0, E(∂_u, ∂_u) is the right side of [[eq:loc-cone-in]] minus q_out, the first line of [[eq:loc-cone]] with u in
place of v ([[lem:loc-cone-in]]), and the same calculation applies.

(b) The equation for Y is linear and of second order in v, with the coefficients −2∂_v ln Ω of ∂_vY and
(1/3)((1/4) |∂_vγ̂|²_γ̂ + q_in) of Y, smooth G-invariant functions on N_o ∩ {v ≤ v′}; so its solution with smooth
G-invariant initial values is smooth, by the smooth dependence of the solutions of linear ordinary differential
equations on parameters, here the point of S³, and G-invariant, by uniqueness. Where Y > 0, γ = Y²γ̂ is a smooth family
of metrics, so χ and 𝔯 are smooth, and the second line of (a) with E(∂_v, ·) = 0 is the linear equation ∂_vW = −(tr_γχ
− 2∂_v ln Ω) W − 2γ⁻¹χ(W, ·) − 4Ω² γ⁻¹𝔯 for the vector field W along each generator, with smooth coefficients; its
solution with W = W_0 at v = 0 is smooth and G-invariant, and so is b := b_0 + ∫_0^v W. By (a) the constraints hold.
Conversely, fields satisfying the constraints define Y, γ̂ and W as above, which solve these equations with their own
initial values, and by uniqueness they are the solutions. On N_i the same argument applies to the first line. The
coordinate expressions were found in the proof of (a); for the background γ = R_e² dΩ₃², whose volume form is R_e³
dvol_1.

(c) We extend the data on {0} × [0, v_1]; on [0, u_1] × {0} the same argument applies with u, q_out and the first line
of (a) only, b = 0 being kept. As in the proof of [[lem:loc-cone-extension]], for f each of ln Ω, γ̂ and q_in, with
background value f̊, let B_f be the Borel sum in t := v − v_1 of the v-derivatives at v = v_1 of f − f̊, G-invariant
fields on S³, with ε_j := δ_1/4 for j ≤ p and ε_j ≤ δ_1/4 for j > p so small that the j-th term has C^p norm at most
2^(−j) ε; put f̃ := f on [0, v_1] and f̃ := f̊ + B_f on [v_1, v_1 + 2δ_1]. Then f̃ is smooth and G-invariant, and, a
term of index j ≤ p having C^p norm at most C(p) ‖f − f̊‖_(C^(p+j)), ‖f̃ − f̊‖_(C^p) ≤ Cε. Replace the extended γ̃ by
(dvol_1/ dvol_γ̃)^(2/3) γ̃, which has the volume form dvol_1, is unchanged on [0, v_1] and, for ε small, is a metric
within Cε of dΩ₃² in C^p. Solve the two equations of (b) on [0, v_1 + 2δ_1] with the values of the data at v = 0; by
uniqueness the solutions are the data on [0, v_1]. R_e and 0 solve the same equations with the background's
coefficients; the coefficients of the equation for Y differ from these by at most Cε in C^(p−1), and so do its initial
values. By Gronwall's inequality for the equation and for its derivatives along S³ (∇̊ commutes with ∂_v), the
v-derivatives being given by the equation, Y − R_e is at most Cε in C^(p−1) on the extended edge, so Y > 0 for ε small.
Then the coefficients of the equation for W are within Cε of the background's in C^(p−2) and 𝔯 is at most Cε in
C^(p−3), and b is at most Cε in C^(p−3) = C^(m_0). At the points of a G-invariant open set of S³ at which the given
data are the background's, every v-derivative of f − f̊ at v = v_1 vanishes, so f̃ = f̊ there, γ̃ is not changed by its
renormalisation, and the equations of (b) have the background's coefficients and initial values there, so that their
solutions are the background's. The extended functions satisfy (i) and (ii) of [[def:loc-cone-data]] and are smooth
through the axes; the extended q_in may be negative beyond v_1. ∎

**Lemma {#lem:loc-axis-jets}** (The formal solution through the axes.) Let a background be given on 𝒮 and cone data
through the axes, of either sign, on N_o and N_i.

(a) [[lem:loc-cone-borel]] holds with the interval Y replaced by S³, the functions a_j and b_k by G-invariant fields on
S³ of one tensor type, with the C^r norms of [[def:loc-axis-data]], and f by a G-invariant field of that type; in its
(a), "at every ϑ" reads "at every point of S³".

(b) [[lem:loc-cone-jets]] holds, with these changes: its a_j and b_k are, at ϑ ∈ (0, π/2), those of its proof, and they
are the derivatives across N of fields and densities smooth through the axes; in (ii) the first statement reads: if the
data equal the background's at the points of a G-invariant open set of S³, so do all a_j and b_k; (iii) holds with the
C^r norms of fields; and (iv) holds for class solutions in the gauge through the axes.

(c) [[prop:loc-cone-formal]] holds, with Δ the difference of fields and densities smooth through the axes and Ĝ a
smooth G-invariant symmetric form on 𝒮 × S³ of the form [[eq:loc-double-null]], Lorentzian when the size is at most a
number depending on the background; in its (a), Δ vanishes at the points of every G-invariant open set of S³ at which
all a_j and b_k are the background's, in place of outside {ϑ_a′ ≤ ϑ ≤ ϑ_b′}, and ‖Δ‖_(C^(k+3)) is measured as in
[[def:loc-axis-data]].

*Proof.* (a) The proof of [[lem:loc-cone-borel]] uses of the variable ϑ only that the coefficients h_j of the Borel
sums are smooth functions of further variables with C^r norms; for G-invariant fields on S³ every term χ(x/ε_j) x^j
h_j/j! is a G-invariant field of the same type, the cut-offs depending on u and v only, and the estimates hold
verbatim.

*The equations in fields.* For fields X = (ln Ω, γ, b) smooth through the axes and densities q_A on an open set of 𝒮,
let 𝐄(X) consist of the restriction E|_(S³) of E := Ric(g) − q_in dv ⊗ dv − q_out du ⊗ du to the tangent vectors of the
spheres, of E(L̲, ∂_v), L̲ := ∂_u + b, and of the 1-form E(L̲, ·)|_(S³), and put 𝒞_in := L̲q_in + tr_γχ̲ q_in and 𝒞_out
:= ∂_vq_out + tr_γχ q_out, with χ̲ := ½(∂_uγ + ℒ_bγ), ℒ_b the Lie derivative on S³. These are smooth G-invariant
fields. Off the axes the reflections reduce E|_(S³) to E(∂_ϑ, ∂_ϑ), E(K_1, K_1), E(K_2, K_2) and E(L̲, ·)|_(S³) to
E(L̲, ∂_ϑ) dϑ, so that 𝐄(X) = 0 is E′ = 0 of [[lem:loc-cone-ricci]] (c); and tr_γχ̲ = L̲ ln 𝒱 + ∂_ϑ b and tr_γχ = ∂_v
ln 𝒱, so that 𝒞_in = 𝒱⁻¹(∂_u ρ_in + ∂_ϑ(b ρ_in)) and 𝒞_out = 𝒱⁻¹ ∂_v ρ_out, the conservation expressions of
[[lem:loc-cone-jets]]. The densities do not enter 𝐄, as T(L̲, ∂_v), T(L̲, ·)|_(S³) and T|_(S³) vanish.

*The principal parts.* In coordinates (u, v, θ¹, θ², θ³), with θ^a coordinates on an open set of S³, a metric of the
form [[eq:loc-double-null]] has g_vv = g_va = 0, g_uv = −2Ω², g_ab = γ_ab, g_ua = −γ_ab b^b, g_uu = γ_ab b^a b^b and
g^uu = g^ua = g^vv = 0, g^uv = −1/(2Ω²), g^va = b^a g^uv, g^ab = γ^ab, as the frame (L̲, ∂_v, ∂_a) is dual to (du, dv,
dθ^a − b^a du); and

    Ric_μν = −½ g^ρσ (∂_ρ∂_σ g_μν + ∂_μ∂_ν g_ρσ − ∂_ρ∂_μ g_σν − ∂_ρ∂_ν g_σμ) + Q_μν,

with Q_μν a polynomial in g_αβ, g^αβ and the first derivatives of g_αβ. In the linearisation of 𝐄 at X in the direction
δX = (δ ln Ω, δγ, δb), the second derivatives of δX come from the first part only, the frame and T holding no
derivative of the metric, and δg_vv = δg_va = 0. Collecting the terms with a derivative in u, and using g^vb = b^b
g^uv, by which the terms in ∂_u∂_vδγ of E(L̲, ·) cancel, one finds, up to terms with at most one derivative of δX,

    E(∂_a, ∂_b):   (2Ω²)⁻¹ ∂_u∂_vδγ_ab,
    E(L̲, ∂_v):    −2 ∂_u∂_vδ ln Ω − ½ γ^ab ∂_u∂_vδγ_ab,
    E(L̲, ∂_a):    −(4Ω²)⁻¹ γ_ab ∂_u∂_vδb^b + ½ γ^bc ∂_u∂_bδγ_ca − ½ γ^bc ∂_u∂_aδγ_bc − ∂_u∂_aδ ln Ω,
                                                                                                {#eq:loc-axis-principal}

and, collecting those with a derivative in v other than ∂_v² (the terms in ∂_v²δX cancel: they enter E(L̲, ∂_v) only,
through ∂_v²(δg_uu + 2b^a δg_ua + b^a b^b δg_ab) = 0), up to terms with at most one derivative of δX,

    E(∂_a, ∂_b):   (2Ω²)⁻¹ (L̲∂_vδγ_ab + ½ (γ_ac ∂_b + γ_bc ∂_a) ∂_vδb^c),
    E(L̲, ∂_v):    −2 L̲∂_vδ ln Ω − ½ γ^ab L̲∂_vδγ_ab − ½ ∂_a∂_vδb^a,
    E(L̲, ∂_a):    −(4Ω²)⁻¹ γ_ab L̲∂_vδb^b,

with L̲ = ∂_u + b^c ∂_c applied to components; here the terms in ∂_v∂_cδγ and ∂_u∂_vδγ of E(L̲, ·) cancel in the same
way. Off the axes these are the second derivatives of [[eq:loc-cone-frame-ricci]].

*The derivatives across N_o.* Let j ≥ 1, and let a_0, …, a_(j−1) be the derivatives across N_o of fields and densities
smooth through the axes; by (a) there are such fields X♭ and densities q♭ with ∂_u^jX♭ = 0 and ∂_u^jq♭ = 0 on N_o. For
G-invariant fields Z = (Z_Ω, Z_γ, Z_b) on N_o, a function, a symmetric form and a vector field on the spheres, put 𝔏(Z)
:= ∂_u^(j−1) 𝐄(X♭ + u^jZ/j!) at u = 0. Ric is linear in the second derivatives of the metric, with coefficients in
g^αβ, and quadratic in the first, and each derivative of u^jZ/j! of order i holds the factor u^(j−i); so a term of
degree at least two in Z holds a factor u^(2j−2) and vanishes at u = 0 after ∂_u^(j−1) when j ≥ 2. For j = 1 such terms
are quadratic forms in the first u-derivatives Z, with smooth coefficients; off the axes they vanish for G-invariant Z,
since by (Ψ2) and (Ψ3) of the proof of [[lem:loc-cone-jets]] every term of E′ holds at most one factor among the first
u-derivatives of ln Ω, the ϰ_i and b, and the first u-derivatives at u = 0 of the class functions of X♭ + uZ are affine
in Z; so they vanish everywhere, by continuity. The terms linear in Z are ∂_u^(j−1) of L(u^jZ/j!) at u = 0, L =
c^μν∂_μ∂_ν + c^μ∂_μ + c the linearisation of 𝐄 at X♭, that is 2c^uv∂_vZ + 2c^ua∂_aZ + (c^u + (j − 1)∂_uc^uu)Z; by
[[eq:loc-axis-principal]],

    𝔏(Z) = 𝔏(0) + ((2Ω²)⁻¹ ∂_vZ_γ, −2 ∂_vZ_Ω − ½ tr_γ ∂_vZ_γ, −(4Ω²)⁻¹ γ(∂_vZ_b, ·)) + 𝔪(Z, ∇̊Z_Ω, ∇̊Z_γ),

with 𝔪 linear, with smooth G-invariant coefficients, its first two components free of ∇̊Z and of Z_b, since off the
axes these two components of 𝐄 hold no u-derivative of b ((Ψ1) of the proof of [[lem:loc-cone-jets]]) and their
coefficients are continuous. So 𝔏(Z) = 0 is a linear system of ordinary differential equations in v along the
generators: for (Z_Ω, Z_γ), with the invertible coefficient (Z_Ω, Z_γ) ↦ ((2Ω²)⁻¹ Z_γ, −2Z_Ω − ½ tr_γ Z_γ) of ∂_v, and
then for Z_b, whose inhomogeneous term holds ∇̊Z_Ω and ∇̊Z_γ. For the densities put Z_in := the solution of
∂_u^(j−1)𝒞_in = 0 at u = 0, in which ∂_u^jq_in enters with the factor 1 and nothing else of order j but Z_γ, and let
Z_out solve ∂_u^j𝒞_out = 0 at u = 0, the linear equation ∂_vZ_out + tr_γχ Z_out = (terms in a_0, …, a_(j−1) and Z)
along the generators. We solve with the initial values at v = 0 the j-th u-derivatives at the corner of the data on
N_i; the coefficients and the initial values being smooth and G-invariant and the system G-equivariant, the solution is
smooth and G-invariant, and we take it as a_j. Off the axes a_j is the derivative of the proof of
[[lem:loc-cone-jets]]: both solve ∂_u^(j−1)E′ = 0 and the conservation equations, in class functions and in fields
respectively, with the same initial values, and those solutions are unique.

*The derivatives across N_i.* Likewise, with 𝔏′(Z) := ∂_v^(k−1) 𝐄(X♭ + v^kZ/k!) at v = 0 and the second list: the terms
in ∂_v² contribute only terms without derivatives of Z, and the third component of 𝔏′(Z) − 𝔏′(0) is −(4Ω²)⁻¹ γ(L̲Z_b,
·) plus terms in Z_b without derivatives, by (Ψ3) of the proof of [[lem:loc-cone-jets]] and continuity, the others
being (2Ω²)⁻¹ L̲Z_γ and −2L̲Z_Ω − ½ tr_γ L̲Z_γ plus terms in Z and ∇̊Z_b. So 𝔏′(Z) = 0 consists of transport equations
along L̲, first for Z_b and then for (Z_Ω, Z_γ); Z_out solves ∂_v^(k−1) 𝒞_out = 0 at v = 0, algebraically, and Z_in
solves ∂_v^k𝒞_in = 0, a transport along L̲. The generators of N_i, the integral curves of L̲, start on S_c and cover
N_i, b being a smooth vector field on S³. The initial values are the k-th v-derivatives at the corner of the data on
N_o. For k = 1 the quadratic terms vanish as before.

*The statements.* (i): off the axes it is (i) of [[lem:loc-cone-jets]], whose proof is local in ϑ; both sides are
continuous. (ii): the coefficients, inhomogeneous terms and initial values of the equations at a point of S³ are built
from the data and their derivatives at that point and from the derivatives along S³ of the solutions of order j there;
where the data equal the background's on a G-invariant open set, the background's derivatives solve the same equations
with the same initial values, and by uniqueness they are the solutions; the second statement is proved as there. (iii):
𝔏(0) holds derivatives of order at most two of a_0, …, a_(j−1), the equation for Z_b one derivative along S³ of (Z_Ω,
Z_γ), and the initial values j derivatives along N_i of the data, and likewise on N_i; the induction of the proof of
(iii) there gives the bound with the C^r norms of fields. (iv): such a solution satisfies 𝐄 = 0 and 𝒞_in = 𝒞_out = 0
near N in F, hence, by continuity, their derivatives of every order on N, and its derivatives across N solve the
equations above with the same initial values.

(c) The proof of [[prop:loc-cone-formal]] applies, with (a) applied to the differences from the background's of the
fields and densities whose derivatives are the a_j and b_k. Ĝ is of the form [[eq:loc-double-null]] with fields smooth
through the axes, smooth by (a) and (b), and Lorentzian when its metric γ_e + Δ_γ on the spheres is positive definite,
which holds when ‖Δ‖_(C⁰) is small. The vanishing to infinite order on N of E and of the conservation expressions holds
off the axes by the proof there, which is local in ϑ, and on N by continuity of every derivative. The support of Δ is
as stated, by (ii) and the support property of (a). ∎

#### The sections of the cones are leaves {#sec:loc-axis-leaves}

*Leaves in a chart.* Let (t, x) be a chart on an open G-invariant set in which G acts on x ∈ ℝ⁴ ∖ {0} by its action on
ℝ⁴, and whose slices Σ_s := {t = s} are spacelike for the metrics considered. The constructions of
[[sec:class-planar-shear]] use of the chart of [[sec:background]] only these properties, through the slice, its future
unit normal n, its second fundamental form K_Σ, the totally geodesic M3 := Σ_s ∩ {φ1 = 0} near axis 2 and the
coordinates (z, y) of [[lem:class-leaf]]; we use them in such charts. Let V = (g, p_A, Θ_A, q_A) be a G-invariant state
on Σ_s near a point p of axis 2 with ρ1(p) > 0, at which the spatial part p_A^Σ of p_A satisfies p_A(∂_z) ≠ 0; p_A^Σ is
tangent to M3 at the points of M3, by invariance. Put

    H_L[V] := ± (Θ_A − κ_A1 + p_A(n) tr K_Σ|_Π)/|p_A^Σ|,      Π := the γ3-orthogonal complement of p_A^Σ in TM3,
                                                                                                    {#eq:loc-axis-hl}

the sign that of p_A(∂_z): the formula of step (1) of the proof of [[lem:class-planar-shear]], with Θ_A, p_A^Σ and
p_A(n) in place of Θ, ∇_Σu and n(u), and with the plane Π fixed by p_A. This is how H_L[Θ_A] of
[[lem:class-leaf-differences]] is read: a function of the point, as [[lem:class-volterra]] requires, which for a
solution of the class system with p_A = du_A equals that formula on each level set of u_A, Π being its tangent plane
there. The *A-leaves* of V are the solutions of [[eq:class-leaf-volterra]] with H_L := H_L[V] through the points of the
axis, and σ_A[V] at a point is ±2|p_A^Σ| σ_L − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e_2, e_2)) for the leaf through it, the sign
that of p_A(∂_z), σ_L of [[eq:class-leaf-volterra]], taken for the normal ν of [[lem:class-leaf]] (b), and e_r the unit
tangent of the leaf in the meridional plane, which is [[eq:class-shear-leaf]] with p_A in place of du. For a solution
of [[eq:class-system]] with p_A = du_A and Θ_A = □_g u_A the leaves are the level sets of u_A in the slices, by the
last statement of [[lem:class-leaf-differences]], whose proof uses only these two properties, and σ_A is the planar
shear of those level sets. Near axis 1 the same holds with the two planes exchanged, κ_A2 in place of κ_A1.

**Lemma {#lem:loc-axis-leaf}** (The sections of the cones are leaves.) (i) Let t be a smooth function on a
neighbourhood of N with ∂_vt > 0 on N_o and ∂_ut > 0 on N_i. Then each level set {t = s} meets N_o in at most one
sphere {(0, c)} × S³ and N_i in at most one sphere {(c′, 0)} × S³, spheres of the data's double-null coordinates, c and
c′ increasing in s. This holds for t = u + v and for every smooth function of (u, v) that increases with u and with v.

(ii) In a chart as above, let V be a state on Σ_s whose A-leaves through the points of the axis near p exist over a
disc 𝔻_(2δ), and let S ⊂ Σ_s be a G-invariant hypersurface through a point of the axis near p such that S ∩ M3 is a
graph z = h_S(y) over a disc 𝔻_r, r ≤ 2δ, with h_S smooth, and such that p_A vanishes on TS along S over 𝔻_r. Then S ∩
M3 is, over 𝔻_r, the A-leaf of V through its point of the axis if and only if Θ_A = θ_S along S over 𝔻_r, where θ_S :=
−Σ_α p_A(∇_(e_α) e_α) for a g-orthonormal frame (e_α) of TS, the expansion of S along g⁻¹p_A computed with the metric
of V.

(iii) If two states have the same p_A, Θ_A, metric and first derivatives of the metric at the points of S, then S ∩ M3
is an A-leaf of one if and only if it is one of the other. For Ů and Û, in every chart as above in which the spheres
{(u, v)} × S³ meet M3 in such graphs and p_A(∂_z) ≠ 0, the spheres in Σ_s are the leaves of both families.

*Proof.* (i) t(0, v) is strictly increasing in v and t(u, 0) in u, so each takes the value s at most once.

(ii) Let F := z − h_S(y) and ν := ∇F/|∇F|, the unit normal of S in Σ_s; ν is G-invariant, hence tangent to M3 at the
points of M3, the fixed set of φ1 ↦ −φ1. For X, Y tangent to S, ∇_XY = ∇^S_XY − k(X, Y) ν + K_Σ(X, Y) n, with k(X, Y)
:= g(∇_Xν, Y), the second fundamental form of S in Σ_s; the last term is that of the proof of [[lem:class-gauss]] (a).
At the points of M3, TS is the orthogonal sum of TS ∩ TM3, the tangent space of Σ_S := S ∩ M3, and of ℝe_1, e_1 :=
K_1/|K_1|. As K_1 is a Killing field and |K_1| is invariant, ∇_(e_1)e_1 = −½ |K_1|⁻² ∇g(K_1, K_1) = −∇ψ_1, so
−p_A(∇_(e_1)e_1) = g⁻¹(p_A, dψ_1) = κ_A1 for every invariant p_A. As p_A vanishes on TS, p_A(∇^S_XY) = 0, so
−p_A(∇_XY) = p_A(ν) k(X, Y) − p_A(n) K_Σ(X, Y); on TΣ_S, k is the second fundamental form of Σ_S in M3, M3 being
totally geodesic and ν tangent to it. Taking the trace over a g-orthonormal frame of TS adapted to this sum,

    θ_S = κ_A1 + p_A(ν) H_S − p_A(n) tr K_Σ|_(TΣ_S),

H_S the mean curvature of Σ_S in M3 for ν. As p_A vanishes on TS, p_A^Σ is conormal to S, so Π = TΣ_S along S and
p_A^Σ = p_A(∂_z) dF, since dF(∂_z) = 1; so p_A(ν) = ±|p_A^Σ| with the sign of p_A(∂_z). Comparing with
[[eq:loc-axis-hl]], H_S = H_L[V] along S exactly when Θ_A = θ_S. By [[lem:class-leaf]] (c), for every graph H_S = a_L
h_S″ + (terms free of h_S″), and E_L := rH_S/a_L − (rh_S′)′ is the function of (r, h_S, h_S′) of that lemma; and
h_S′(0) = 0, h_S being smooth and invariant. So if H_S = H_L[V], integrating (rh_S′)′ = rH_L[V]/a_L − E_L from 0 shows
that h_S solves [[eq:class-leaf-volterra]] with h_S(0) its point of the axis, and by the uniqueness in
[[lem:class-volterra]] it is the leaf of V there. Conversely, if Σ_S is the leaf, differentiating
[[eq:class-leaf-volterra]] at r > 0, and by continuity at r = 0, gives H_S = H_L[V] along it, hence Θ_A = θ_S.

(iii) [[eq:class-leaf-volterra]] for the curve S ∩ M3 holds H_L[V], a_L and E_L at the points of the curve only, and
these are functions of p_A, Θ_A, the metric and its first derivatives there ([[eq:loc-axis-hl]], [[lem:class-leaf]]
(c)); so the curve solves it for one state if and only if it solves it for the other. For Ů and Û, p_in = −dv and
p_out = −du vanish on the tangent spaces of the spheres. u and v are null for every metric of the form
[[eq:loc-double-null]], so ∇²v(P, ·) = 0 by [[prop:class-structure]] (b), and the tangent space of a sphere is a screen
there: it is spacelike, orthogonal to P := Ĝ⁻¹ (−dv), which it does not contain, and so equal to {P, L̄}^⊥ for the null
L̄ orthogonal to it with Ĝ(P, L̄) = −1. As v is constant on the sphere, −p_in(∇_XX) = dv(∇_XX) = −∇²v(X, X) for X
tangent to it, so θ_S = −tr_(TS)∇²v = □_Ĝ(−v) = div_Ĝ P̂_in = Θ̂_in, and likewise for the outgoing family and for Ů. By
(ii), over every disc on which a sphere meets M3 in a graph, the spheres are the leaves. ∎

**Lemma {#lem:loc-axis-shear}** (The planar shear on unions of arcs of leaves.) In a chart as above, let ů be a smooth
class solution near Σ_s, and let δ, the balls 𝔅 ⊂ 𝔅′ and C_L be those of [[lem:class-leaf-differences]] and
[[def:class-adapted]] for ů at a point p of axis 2 with ρ1(p) > 0, δ decreased, depending only on 𝔅′ and the chart, so
that 8C_Lδ ≤ 1, that ξ ∈ [1/2, 2] in step (1) of the proof, and that the A-leaves of the states of 𝔅′ through the
points of the axis within 2δ of p are graphs over 𝔻_(2δ). Let U, U′ ∈ 𝔅′ be states on Σ_s, U including ∂g among its
components, and let O ⊂ Σ_s be a G-invariant open set, with boundary of measure zero, such that for every x ∈ O ∩
𝒰_δ(p) the arc of the A-leaf of U from its point on the axis to x lies in the closure of O. Then

    ‖σ_A[U] − σ_A[U′]‖_(L²(O∩𝒰_δ(p))) ≤ C ‖U − U′‖_(L²(O∩𝒰_(2δ)(p))),                                {#eq:loc-axis-shear}

with C depending only on 𝔅′, δ and the chart near p, and not on O. Near axis 1 the same holds with the planes
exchanged.

For O the union of the leaves of U over 𝔻_δ through the points of the axis within δ/2 of p, a neighbourhood of the
points of 𝒰_(δ/4)(p), [[eq:loc-axis-shear]] is a bound of the kind of [[lem:class-leaf-differences]] (b); the proof
below is that bound written leaf by leaf.

*Proof.* (1) *The leaves.* For V ∈ 𝔅′ write h_V(z0, ·) for its A-leaf through (z0, 0), a function of r = |y| by
invariance, p_V := ∂_r h_V and q_V := p_V/r. By the proof of [[lem:class-volterra]], with G_V(r, z, p) := r H_L[V](z,
r)/ a_L(r, z, p) − E_L(r, z, p), a_L and E_L those of [[lem:class-leaf]] (c) for the metric of V,

    r p_V(r) = ∫_0^r G_V(ρ, h_V(ρ), p_V(ρ)) dρ,      |∂_pG_V| ≤ C (r + |p|),      |p_V| ≤ C r,

and also |∂_zG_V| ≤ C (r + |p|), since by that proof E_L = (C3 r + A3 p) N_L²/det₂ − p + r B̃/a_L with B̃ smooth. These
constants hold the C¹ norms of H_L[V], which hold first derivatives of p_A and Θ_A and second derivatives of the
metric, and the C² norms of γ3, bounded on 𝔅′ by the Sobolev inequality of [[lem:sobolev]] at the order k − 4 ≥ 2. The
map 𝒯 of that proof is C¹ in (p, z0) and a contraction uniformly in z0, and the equation is regular for r > 0, so z0 ↦
h_V(z0, ·) is C¹ on [0, 2δ], and ξ := ∂_(z0)h_V solves r ∂_r ξ(r) = ∫_0^r (∂_zG_V ξ + ∂_pG_V ∂_r ξ) dρ with ξ(0) = 1.
So |∂_r ξ| ≤ C r sup |ξ| on [0, 2δ] and |ξ − 1| ≤ C δ² sup |ξ|, and after decreasing δ, ξ ∈ [1/2, 2] and |∂_(z0)
q_V| = |∂_r ξ|/r ≤ C. Hence (z0, y) ↦ (h_V(z0, y), y), for |z0 − z(p)| < 3δ/2 and |y| < 2δ, is a C¹ diffeomorphism onto
a neighbourhood of 𝒰_δ(p) ∩ M3 contained in 𝒰_(2δ)(p), with Jacobian in [1/2, 2].

(2) *The leaf through a point.* σ_A[V](x) = 𝔖(x, V(x), q_V(z0, r)) for x = (h_V(z0, y), y), r = |y|, with 𝔖 smooth: by
[[eq:class-leaf-volterra]], σ_L = ½ H_L[V] − k_φ with k_φ = ν^r/r + ½ ν(log B3) and ν^r/r = −(C3 + A3 q_V)/(det₂^(1/2)
N_L), while N_L, ν and e_r hold h′ = r q_V, the metric and its first derivatives at x. For x ∈ 𝒰_δ(p) let z0 and z0′ be
the points of the axis of the leaves of U and of U′ through x. As h_U(z0, r) = z(x) = h_(U′)(z0′, r) and ∂_(z0)h_(U′) ≥
1/2, |z0 − z0′| ≤ 2|h_U(z0, r) − h_(U′)(z0, r)|, so with Δh := h_U(z0, ·) − h_(U′)(z0, ·) and Δq := q_U(z0, ·) −
q_(U′)(z0, ·),

    |σ_A[U](x) − σ_A[U′](x)| ≤ C (|U − U′|(x) + |Δq(r)| + |q_(U′)(z0, r) − q_(U′)(z0′, r)|)
                             ≤ C (|U − U′|(x) + |Δq(r)| + |Δh(r)|).

(3) *Two leaves from one point of the axis.* Fix z0, put Δp := ∂_rΔh, and let w(ρ) be |U − U′| at the point (h_U(z0,
ρ), ρ) of the leaf of U. Subtracting the equations of (1),

    r Δp(r) = ∫_0^r [G_U(ρ, h_U, p_U) − G_(U′)(ρ, h_U, p_U)] + [G_(U′)(ρ, h_U, p_U) − G_(U′)(ρ, h_(U′), p_(U′))] dρ.

The second bracket is at most C(|Δh| + ρ |Δp|). In the first, (ρ, h_U(ρ)) is a point of the leaf of U; H_L[·] is a
smooth function of p_A, Θ_A, the metric and its first derivatives there, a_L one of γ3 there, and E_L, by the form in
(1) and |p| ≤ Cρ, differs for two metrics at the same (ρ, z, p) by at most Cρ times the difference of γ3 and its first
derivatives; so the first bracket is at most Cρ w(ρ). With |Δh(r)| ≤ ∫_0^r |Δp|, r |Δp(r)| ≤ C r ∫_0^r |Δp| + C ∫_0^r ρ
w(ρ) dρ, and Gronwall's inequality gives |Δp(r)| ≤ C(r 𝒜w(r) + ∫_0^r ρ 𝒜w(ρ) dρ), with 𝒜w(r) := r⁻² ∫_0^r ρ w(ρ) dρ the
average of [[prop:class-flat-model]] (b). So |Δq| ≤ C(𝒜w + R 𝒜(𝒜w)) and |Δh| ≤ C R² (𝒜(𝒜w) + 𝒜(R 𝒜(𝒜w))) on [0, R], and
as 𝒜 does not increase the L² norm of radial functions on the plane ([[prop:class-flat-model]] (b) at the order 0, by
density), and 𝒜f on [0, R] depends only on f there, for every R ≤ 2δ

    ‖Δq‖_(L²(𝔻_R)) + ‖Δh‖_(L²(𝔻_R)) ≤ C ‖w‖_(L²(𝔻_R)),

radial functions being read as functions on the disc 𝔻_R.

(4) *Integration.* For |z0 − z(p)| < 3δ/2 let R(z0) be the supremum of |y| over the points (h_U(z0, y), y) of O ∩
𝒰_δ(p), and 0 if there are none. By the hypothesis on O, the arc of the leaf of U from (z0, 0) to such a point lies in
the closure of O, so every (h_U(z0, y), y) with |y| < R(z0) lies there. For G-invariant functions the volume of Σ_s on
𝒰_(2δ)(p) is comparable to the product of that of M3 and the length of the orbit of K_1, which is bounded above and
below there. By (2), (3) and the change of variables of (1), first to (z0, y) and then back,

    ∫_(O∩𝒰_δ(p)) |σ_A[U] − σ_A[U′]|² ≤ C ∫_(O∩𝒰_δ(p)) |U − U′|² + C ∫ dz0 ∫_(𝔻_(R(z0))) w(z0, |y|)² dy
                                     ≤ C ∫_(O∩𝒰_(2δ)(p)) |U − U′|²,

the points (h_U(z0, y), y) with |y| < R(z0) lying in the closure of O ∩ 𝒰_(2δ)(p), whose boundary has measure zero. ∎

#### The reduced problem through the axes {#sec:loc-axis-reduced}

In this subsection a background on Q1 with margin δ_1 is fixed, together with cone data through the axes, of either
sign, on N_o and N_i, of size at most ε in C^(m_0), with k ≥ 6 and with nonnegative densities on {0} × [0, v_1] and [0,
u_1] × {0}; ε is as small as needed, and C, ε_0 depend only on k, u_1, v_1, δ_1, the background and the numbers fixed
below in terms of these. We follow case (I) of [[sec:loc-cone-reduced]], whose notation is kept, with the changes
stated.

*The chart and the regions.* Fix δ_c ∈ (0, δ_1/8] and a nondecreasing β ∈ C^∞(ℝ) with β = 0 on (−∞, 0] and β = 1 on [1,
∞), and put s* := ln((u_1 + δ_c)(v_1 + δ_c)) + 1, M := s* − 2 ln δ_c + 1 and, on {u > −δ_c, v > −δ_c},

    τ := ln((u + δ_c)(v + δ_c)) + M (β((u − u_1)/δ_1) + β((v − v_1)/δ_1)),      y := ((v + δ_c)/(u + δ_c)) ω(ϑ, φ1, φ2),
                                                                                                    {#eq:loc-axis-time}

the chart [[eq:loc-cone-time]] with its time changed by a function of (u, v). Its partial derivatives τ_u ≥ 1/(u + δ_c)
and τ_v ≥ 1/(v + δ_c) are positive, so along each ray (u + δ_c, v + δ_c) = λ(1, ϱ), λ > 0, τ increases strictly with λ,
from −∞ to ∞; hence (u, v) ↦ (τ, (v + δ_c)/(u + δ_c)) is a diffeomorphism of {u, v > −δ_c} onto ℝ × (0, ∞), and (τ, y)
is a G-equivariant chart onto ℝ × (ℝ⁴ ∖ {0}) in which the metrics with fields smooth through the axes are smooth. The
form dτ = τ_u du + τ_v dv is timelike, and positive on future causal vectors, for g_e, for every metric of the form
[[eq:loc-double-null]], which has g^uu = g^vv = 0 and g^uv < 0, and for every Lorentzian metric close enough to g_e in
C⁰ on a compact set; and ∂_τ = λ((u + δ_c)∂_u + (v + δ_c)∂_v), λ := ((u + δ_c)τ_u + (v + δ_c)τ_v)⁻¹, is future timelike
for g_e. By [[lem:loc-axis-leaf]] (i) the slice Σ_s := {τ = s} meets N_o in at most one sphere S_o(s) and N_i in at
most one sphere S_i(s); with τ_c := 2 ln δ_c the time of the corner sphere, for τ_c < s ≤ s* + 1 it meets both, for s =
τ_c both are S_c, and for s < τ_c the slice does not meet F. Put τ_init := ln(δ_c²/4), κ := δ_1/(4(l_u + l_v + 1)) and

    𝒰^♯ := {(u, v) : u, v > −δ_c, τ_init ≤ τ ≤ s*, u + κv ≤ l_u + δ_1/2, v + κu ≤ l_v + δ_1/2},      𝔗(s) := F ∩ {τ ≤ s}.
                                                                                                    {#eq:loc-axis-region}

Then: (1) Q1 ⊂ 𝔗(s* − 1), the terms in β vanishing on Q1; and 𝔗(s*) ⊂ [0, l_u) × [0, l_v), since at a point of F with u
≥ l_u = u_1 + δ_1, τ ≥ ln(δ_c²) + M = s* + 1, and likewise for v. As u + κv < l_u + δ_1/4 and v + κu < l_v + δ_1/4 on
[0, l_u) × [0, l_v), and τ ≥ τ_c > τ_init on F, F ∩ 𝒰^♯ = 𝔗(s*). (2) 𝒰^♯ is a compact subset of the interior of Q^♯ in
the chart: on it v + δ_c ≤ l_v + δ_1, so τ ≥ τ_init gives u + δ_c ≥ e^(τ_init − 2M)/(l_v + δ_1), and likewise v + δ_c
is bounded below. Its boundary consists of pieces of Σ_init, of Σ_(s*) and of the two far cuts, with the conormals dτ,
du + κdv and dv + κdu, timelike and positive on future causal vectors for g_e, for every metric of the form
[[eq:loc-double-null]] and for the Lorentzian metrics C⁰-close to g_e; so these pieces are spacelike, with 𝒰^♯ to their
past. (3) Every slice of 𝒰^♯, of P ∩ 𝒰^♯ and of 𝔗(s) is a union of spheres {(u, v)} × S³, these sets being defined by
conditions on (u, v); for s > τ_c the slice of 𝔗(s*) in Σ_s is bounded by S_o(s) and S_i(s) only. Every time that is a
function of (u, v), increasing in both, has (3) and the property of [[lem:loc-axis-leaf]] (i); the choice
[[eq:loc-axis-time]] makes 𝔗(s*), whose slices are bounded by sections of the two cones only, contain the whole of Q1
while meeting the cones only where the data are given.

*The system.* In case (I) of [[sec:loc-cone-reduced]] take Δ of [[lem:loc-axis-jets]] (c) with δ_e := δ_c/8, extended
by 0 to Q^♯, smoothly, as it vanishes outside {|u| ≤ 2δ_e} ∪ {|v| ≤ 2δ_e} and 2δ_e < δ_1, so that Δ vanishes near
Σ_init, where (u + δ_c)(v + δ_c) ≤ δ_c²/4 as the terms in β are nonnegative; χ := χ_𝒰, with no factor χ_ϑ, equal to 1
on a neighbourhood 𝒰_1 of 𝒰^♯ and supported in a compact set 𝒰_2 in the interior of Q^♯ in the chart; θ equal to 1 on a
neighbourhood of 𝒰^♯ and supported in 𝒰_1; and Ů, Û, 𝐔_c := 𝐔̊, ϒ and A^μ_♭ as there. Let 𝒰_3 be a compact
neighbourhood of 𝒰_2 in the interior of Q^♯ in the chart, and ρ_- the least value of |y| on 𝒰_3. By compactness, as in
step (4) of the proof of [[lem:loc-lens-dependence]], there are δ ∈ (0, ρ_-/4] and balls 𝔅 ⊂ 𝔅′ about Ů for which
[[lem:class-leaf-differences]], for both families, and [[lem:loc-axis-shear]] hold near every point p ∈ 𝒰_2 of an axis
in a slice Σ_s, τ_init ≤ s ≤ s*, with the same constants, and the leaves of the states of 𝔅′ through the points of the
axis within 2δ of such p lie in 𝒰_3. Let ψ_0 ∈ C^∞(ℝ) equal 1 on [0, δ/4] and 0 on [δ/2, ∞), and ψ_ax := ψ_0(ρ1) +
ψ_0(ρ2), with ρ1, ρ2 the radii of [[sec:class-phases]] in the coordinates y; it is smooth and G-invariant, the sets {ρ1
≤ δ/2} and {ρ2 ≤ δ/2} being disjoint where |y| ≥ ρ_-. For G-invariant states U = (g, p_A, Θ_A, q_A) near Ů on the
slices, let 𝒜^ax(U) = 0 be (Aug1), (Aug2) and (Aug4) of [[sec:class-augmented]], with the reduced Ricci tensor and the
gauge vector relative to Ĝ, together with, in place of (Aug3),

    P_A(Θ_A) = (1 − ψ_ax) S_A + ψ_ax S_A^ax,
    S_A^ax := −κ_A⊥² − ½ (Θ_A − κ_A⊥)² − ½ σ_A[U]² − Σ_B q_B g⁻¹(p_A, p_B)²,                       {#eq:loc-axis-closure}

A ∈ {in, out}, with S_A of (Aug3), κ_A⊥ := κ_A1 near axis 2 and κ_A⊥ := κ_A2 near axis 1, and σ_A[U] that of the slice
Σ_s of [[eq:loc-axis-time]] through the point ([[sec:loc-axis-leaves]]): the closure of Step 6 of the proof of
[[thm:class-stability]], for both families and with no cut-off ζ_A. Let 𝔄_χ and F̃ be defined by
[[eq:loc-cone-modified]], with 𝒜^ax in place of 𝒜 in the first-order form of Step 9, its local terms evaluated at 𝐔̊ +
ϒ(𝐔 − 𝐔̊) and its term in σ_A at 𝐔.

**Lemma {#lem:loc-axis-system}** (The modified system through the axes.) Let ρ > 0 be so small that every 𝐔 = 𝐔̊ + Z on
a slice with ‖Z‖_(H^k) ≤ ρ has |Z| ≤ r_0 and lies, near the points of the axes in 𝒰_2, in the balls 𝔅 and 𝔅′, and let
𝒟_ρ be the set of [[sec:class-kato]] with s := k, u_* := 0 and the time interval [τ_init, s*]. For ε small:

(a) on 𝒟_ρ, 𝔄_χ(𝐔) = F̃ has the form [[eq:class-kato-system]] for Z, with A^μ_χ symmetric and A^0_χ ≥ c_1 I as in
[[lem:loc-cone-system]] (a), and with a forcing term Φ(τ, Z) that satisfies (F1)–(F3) and ‖Φ(τ, Z) − Φ(τ, 0)‖_(H^k) ≤ C
‖Z‖_(H^k); these bounds and c_1 do not depend on ε;

(b) where χ = 1, 𝔄_χ(𝐔) = 𝒜^ax(𝐔) for (τ, Z) ∈ 𝒟_ρ;

(c) (c) of [[lem:loc-cone-system]] holds;

(d) σ_A[Ů] = 0, and σ_A[Û] is the planar shear for Ĝ of the spheres {(u, v)} × S³ in the slices, a smooth function of Ĝ
and its first derivatives; 𝒜^ax(Û) is a smooth function on supp χ that vanishes to infinite order on N; 𝔄_χ(Û) = F̃ on
P, and F̃ is smooth and supported in supp χ;

(e) R := 𝔄_χ(Ů) − F̃ is smooth and supported in supp χ, and sup_τ ‖R(τ)‖_(H^k) ≤ Cε.

*Proof.* (a) The matrices and their bounds are those of [[lem:loc-cone-system]] (a) with χ_ϑ := 1, and its proof
applies, A^0 being positive definite at 𝐔̊ on supp χ, where g_e is Lorentzian with dτ and ∂_τ timelike and P̊_A(τ) > 0.
Put Φ(τ, Z) := χ (F_0(x, 𝐔) − A^μ(x, 𝐔̊ + ϒ(Z)) ∂_μ𝐔̊) + (1 − χ) B_♭Z + F̃, with F_0(x, 𝐔) the right side of the
first-order form of 𝒜^ax, its local terms evaluated at 𝐔̊ + ϒ(Z) and its term in σ_A at 𝐔. Its local part satisfies
(F1)–(F3) and the linear bound, by [[rem:class-kato-local]] and [[lem:class-composition]] (b). Its term in σ_A is −½ χ
ψ_ax σ_A[𝐔]² in the rows of [[eq:loc-axis-closure]], times bounded factors of the first-order form; by (d), σ_A[Ů] = 0,
so [[lem:class-leaf-differences]] (a) about Ů, with [[lem:class-composition]] (a) for the square and sup |σ_A| bounded
on 𝔅, bounds it in H^k by C ‖Z‖_(H^k), which gives (F1) and the linear bound; [[lem:class-leaf-differences]] (b), with
σ_A bounded on 𝔅′, gives (F2); and (F3) follows from (F2) and the smoothness in τ of the coefficients, as in Step 9 of
the proof of [[thm:class-stability]]. The term in σ_A at a time depends on the state at that time only. (b) is read
off, ϒ being inactive where |Z| ≤ r_0, and (c) is proved as there.

(d) Along a slice, v increases and u decreases with |y|, so the spheres {(u, v)} × S³ in Σ_s meet M3 in graphs with
p_A(∂_z) ≠ 0 near the axes, and by [[lem:loc-axis-leaf]] (iii) they are the leaves of both families of Ů and of Û. So
σ_A[Û] is their planar shear for Ĝ, a smooth function of Ĝ and its first derivatives, and σ_A[Ů] = 0, the null second
fundamental form of a round sphere for g_e being a multiple of its metric. By [[lem:class-gauss]] (b), σ_A[Û] = Θ_h −
κ_2 for the eikonal −v, respectively −u, of Ĝ, so by [[eq:class-identity]], [[eq:class-x]] and [[prop:class-axis]] (d),
(1 − ψ_ax) S_A(Û) + ψ_ax S_A^ax(Û) = −|∇²v|²_Ĝ − T̂(P̂_A, P̂_A), respectively with u, off the axes and by continuity at
them, T̂ := q̂_in dv ⊗ dv + q̂_out du ⊗ du; and [[eq:class-raychaudhuri]] for that eikonal shows that the residual of
[[eq:loc-axis-closure]] for Û is −E(P̂_A, P̂_A). The other residuals are those of the proof of [[lem:loc-cone-system]]
(d). By [[lem:loc-axis-jets]] (c) they vanish to infinite order on N. The rest is the proof of (d) there.

(e) R = 𝔄_χ(Ů) − 𝔄_χ(Û) + θ 1_F 𝔄_χ(Û). By (d) the term in σ_A of each is a smooth function of x and of the 1-jet of
𝐔̊, respectively of 𝐔̂, vanishing for 𝐔̊; for Ů the residual of [[eq:loc-axis-closure]] vanishes on F, the background
solving [[eq:class-system]]. So the proof of (e) of [[lem:loc-cone-system]], case (I), applies: R is smooth, supported
in supp χ, and its C^k norm is at most C ‖Δ‖_(C^(k+3)) ≤ Cε, by [[lem:loc-axis-jets]] (c). ∎

**Lemma {#lem:loc-axis-energy}** (Energy with a non-local term.) [[lem:loc-cone-energy]] holds in every chart (t, x)
whose slices are spacelike for the systems concerned, with t in place of τ, without the condition that the pieces of
B_1 meet the slices transversally, and with 𝐀^μ ∂_μ z = Mz + 𝔫 in place of 𝐀^μ ∂_μ z = Mz, where 𝔫 is continuous on 𝒟
and ‖𝔫‖_(L²(𝒟∩{t=s})) ≤ C ‖z‖_(L²(𝒟∩{t=s})) for every s.

*Proof.* The proof of [[lem:loc-cone-energy]] uses of the boundary only that every 𝒟_s is a Lipschitz domain, for the
divergence theorem. In it ∂_μ V^μ gains the term 2⟨𝔫, z⟩, whose integral over 𝒟 ∩ {t = s} is at most 2C
‖z‖²_(L²(𝒟∩{t=s})) ≤ (2C/c) e(s); the rest of the proof is unchanged. ∎

**Lemma {#lem:loc-axis-cauchy}** (The Cauchy problem through the axes.) For ε ≤ ε_0 the system 𝔄_χ(𝐔) = F̃ has a smooth
G-invariant solution on [τ_init, s*] × ℝ⁴ with 𝐔 = 𝐔̊ at τ_init, g_τ = ∂_τ g, g_a = ∂_a g, (τ, 𝐔 − 𝐔̊) ∈ 𝒟_ρ and sup_τ
‖𝐔 − 𝐔̊‖_(H^k) ≤ Cε; so the derivatives of order at most k − 3 of 𝐔 − 𝐔̊ are at most Cε.

*Proof.* [[thm:class-kato]] (a), with (F1)–(F3) of [[lem:loc-axis-system]] (a), gives a solution Z with Z = 0 at τ_init
on a maximal interval [τ_init, τ_m) ∩ [τ_init, s*], continued while ‖Z‖_(H^k) ≤ η_ρ ρ. On it Z solves the linear
problem of [[lem:class-kato-linear]] with v := Z and f := Φ(τ, Z), ∂_τZ being bounded in H^(k−1) by the equation, and
by part (a) of that lemma it is the solution of part (b) there. Part (c), with ‖Φ(τ, Z)‖_(H^k) ≤ ‖R(τ)‖_(H^k) + C
‖Z‖_(H^k), as Φ(τ, 0) = −R, and with K_Z bounded, ‖Z‖_(W^(1,∞)) ≤ C_S ρ and ∂_τZ being bounded by the equation, gives
E_k(τ; Z)^(1/2) ≤ C ∫_(τ_init)^τ (‖R‖_(H^k) + ‖Z‖_(H^k)), C independent of ε. By Gronwall's inequality and
[[lem:loc-axis-system]] (e), ‖Z(τ)‖_(H^k) ≤ C_2 ε on the interval. For ε ≤ η_ρ ρ/(2C_2) the continuation of
[[thm:class-kato]] (a) extends the solution to [τ_init, s*]. [[thm:class-kato-stability]] is not used: it needs ρ = ∞,
while the term in σ_A is defined on 𝒟_ρ only. The solution is smooth by the argument of the paragraph *Smoothness* of
the proof of [[thm:class-stability]], without restarts, F̃ being smooth with compact support; and it is G-invariant, as
the system is G-invariant, σ_A of the image of a state under an element of G being the image of σ_A, and as the
solution is unique ([[thm:class-kato]] (a)). The rows of (c) of [[lem:loc-cone-system]] hold at τ_init, where 𝐔 = 𝐔̊.
The pointwise bounds follow by the Sobolev inequality on the slices. ∎

Below U denotes this solution, (g, p_A, Θ_A, q_A) its components and P_A := g⁻¹p_A.

**Lemma {#lem:loc-axis-past}** (The past of the edges.) U = Û on P ∩ 𝒰^♯. So U − Û vanishes with all its derivatives on
N ∩ 𝒰^♯, g and the densities induce the cone data there, and for τ_c ≤ s ≤ s* the spheres S_o(s) and S_i(s) are leaves
of both families of U in Σ_s.

*Proof.* On P, 𝔄_χ(𝐔) = F̃ = 𝔄_χ(Û). As in the proof of [[lem:loc-cone-past]], z := 𝐔 − 𝐔̂ satisfies on P ∩ 𝒰^♯ a
system 𝐀^μ ∂_μ z = Mz + 𝔫, with 𝐀^μ := A^μ_χ(x, 𝐔̂ − 𝐔̊), M bounded, and 𝔫 := −½ χ ψ_ax (σ_A[𝐔]² − σ_A[Û]²) in the rows
of [[eq:loc-axis-closure]], times bounded factors. The slices of P ∩ 𝒰^♯ are unions of spheres {(u, v)} × S³, which are
the leaves of both families of Û in Σ_s ([[lem:loc-axis-system]] (d)); so [[lem:loc-axis-shear]], with Û in place of U
and U in place of U′, both in 𝔅′, near the points of the axes in 𝒰_2, with σ_A bounded on 𝔅′, gives ‖𝔫(s)‖ ≤ C ‖z(s)‖
on the slices of P ∩ 𝒰^♯. [[lem:loc-axis-energy]] on the closure of P ∩ 𝒰^♯, with B_0 := Σ_init ∩ 𝒰^♯ and B_1 the
pieces of N and of the far cuts, where the boundary matrix is nonnegative as in the proof of [[lem:loc-cone-past]],
gives z = 0. U and Û are smooth, so they agree with all derivatives on N ∩ 𝒰^♯. By [[lem:loc-axis-leaf]] (iii), S_o(s)
and S_i(s), which are leaves of both families of Û, are leaves of U. ∎

**Lemma {#lem:loc-axis-propagation}** (The constraints on the slice-triangle.) On 𝔗(s*), g⁻¹(p_A, p_A) = 0, dp_A = 0,
D(g) = 0 and Θ_A = div_g P_A. There are smooth G-invariant functions u_in, u_out on 𝒰′ := (P ∩ 𝒰^♯) ∪ 𝔗(s*) with p_in =
−du_in, p_out = −du_out, u_in = v and u_out = u on P ∩ 𝒰^♯; (g, u_in, u_out, q_in, q_out) solves [[eq:class-system]] on
𝔗(s*), with Ric(g) = q_in du_in ⊗ du_in + q_out du_out ⊗ du_out, in the gauge D(g) = 0 relative to Ĝ; and q_in ≥ 0
where u_in ≤ v_1 and q_out ≥ 0 where u_out ≤ u_1.

*Proof.* On 𝔗(s*) ⊂ F ∩ 𝒰^♯, θ = 1 and χ = 1, so F̃ = 0 and 𝒜^ax(U) = 0 ([[lem:loc-axis-system]] (b)). An integral
curve of P_A through a point of 𝔗(s*), followed to the past, decreases τ at a rate bounded below and cannot leave 𝔗(s*)
through its slice in Σ_(s*), so it reaches N. *The phases.* (Aug2) holds on 𝔗(s*), the axes included, and the argument
of the paragraph *The phases* of the proof of [[lem:loc-cone-constraints]], with 𝒪_1 := 𝔗(s*), gives ν_A = 0 and dp_A =
0 on 𝔗(s*), and p_A = −du_A on the simply connected 𝒰′, with u_A fixed by its values on P ∩ 𝒰^♯. *The gauge and the
expansions.* Put Δ_A := Θ_A − div_g P_A and let U′ be U with Θ_A replaced by div_g P_A. With p_A = −du_A an eikonal on
𝒰′, [[eq:class-raychaudhuri]] holds for div_g P_A = □_g(−u_A). Near an axis the level sets of u_A in the slices of
𝔗(s*) are graphs close to the spheres, and they are leaves of U′, by [[lem:loc-axis-leaf]] (ii): p_A vanishes on them,
and their expansion is □_g(−u_A), as in the proof of its part (iii), u_A being null on 𝒰′. So by [[eq:class-identity]],
[[eq:class-x]] and [[prop:class-axis]] (d) the right side of [[eq:class-raychaudhuri]] is both S_A and S_A^ax with
div_g P_A in place of Θ_A, σ_A[U′] in place of σ_A[U] and Ric(g) in place of T. Subtracting it from
[[eq:loc-axis-closure]] and using [[prop:class-augmented]] (e),

    P_A(Δ_A) = −Δ_A ((1 − ψ_ax)(Θ_A + div_g P_A − 2κ_A1 − 2κ_A2) + ½ ψ_ax (Θ_A + div_g P_A − 2κ_A⊥))
               − ½ ψ_ax (σ_A[U]² − σ_A[U′]²) + g(∇_(P_A) D, P_A) + L(P_A, P_A),

and D solves [[eq:class-gauge-wave]] with B_g T = Σ_A Δ_A q_A p_A, as ν_A = 0. In the first-order variables z := (D,
∂_τ D, ∂_y D, Δ_in, Δ_out) this is a system 𝐀^μ ∂_μ z = Mz + 𝔫 on 𝔗(s*) of the form of Step 9, with the inverse metric
g and the transport fields P_A, and 𝔫 the term in σ_A. For s > τ_c the slice of 𝔗(s*) in Σ_s is bounded by S_o(s) and
S_i(s), leaves of U ([[lem:loc-axis-past]]); the leaves of U foliate a neighbourhood of each point of an axis, so the
leaf of U through a point of that slice near an axis lies between these two, and its arc from the axis lies in the
slice. U′ lies in 𝔅′, 𝒩_k controlling div_g P_A at the order k − 1, as in Step 10 of the proof of
[[thm:class-stability]]. So [[lem:loc-axis-shear]] gives ‖𝔫(s)‖ ≤ C ‖Δ(s)‖, with C independent of s, also near τ_c,
where these slices are thin. By [[lem:loc-axis-past]], z vanishes on N ∩ 𝔗(s*), as D(Ĝ) = 0 relative to Ĝ and Θ̂_A =
div_Ĝ P̂_A. [[lem:loc-axis-energy]] on 𝔗(s*), whose boundary consists of B_0 := N ∩ 𝔗(s*) and of its slice in Σ_(s*),
gives z = 0. Then (Aug1) is Ric(g) = Σ_A q_A p_A ⊗ p_A and (Aug4) the conservation law, as in the proof of
[[lem:loc-cone-constraints]], whose paragraph *The signs* gives the signs, the densities of the data being nonnegative
on {0} × [0, v_1] and on [0, u_1] × {0}. ∎

**Lemma {#lem:loc-axis-gauge}** (The double-null gauge through the axes.) Let ω′ be the map of 𝒰′ into S³ that is
constant along the integral curves of P_out and equals ω on P ∩ 𝒰^♯, and Ψ := (u_out, u_in, ω′). Then Ψ is a
G-equivariant diffeomorphism from 𝔗(s*) onto a set that contains Q1 × S³, equal to the identity with its differential
on N ∩ 𝔗(s*). In the coordinates (u′, v′, ω′) := Ψ the metric g has the form [[eq:loc-double-null]] with fields smooth
through the axes, and (g, v′, u′, q_in, q_out) is a class solution in the gauge through the axes on Ψ(𝔗(s*)) that
induces the cone data on the edges. Its fields and densities differ from the background's by at most Cε in C^(k−4) on
Q1 × S³. Ψ is the identity on every set on which U = Ů that contains, with each point, its past integral curve of P_out
up to P ∩ 𝒰^♯.

*Proof.* The proof of [[lem:loc-cone-gauge]], case (I), applies, with the point ω′ of S³ in place of the angle ϑ′ and
𝔗(s*) ⊃ Q1 in place of F ∩ 𝒰_σ ⊃ G_*. The flow of P_out commutes with G, P_out being G-invariant, so ω′ is smooth and
G-equivariant; Ψ − id is at most Cε in C^(k−3), by [[lem:loc-axis-cauchy]]; 𝔗(s*) is a down-set in (u, v), so Ψ is
injective; and as Q1 ⊂ 𝔗(s* − 1) lies at positive distance from the slice of 𝔗(s*) in Σ_(s*), the contraction argument
there gives Ψ(𝔗(s*)) ⊃ Q1 for ε small. In the coordinates (u′, v′, ω′), g⁻¹(du′, du′) = g⁻¹(dv′, dv′) = 0, and g⁻¹du′ =
−P_out annihilates du′ and dω′; so with coordinates θ^a of S³, g^(u′u′) = g^(v′v′) = g^(u′a) = 0. A metric with such an
inverse is −2Ω² (du′ ⊗ dv′ + dv′ ⊗ du′) + γ_ab (dθ^a − b^a du′)(dθ^b − b^b du′), with −1/(2Ω²) = g^(u′v′), γ_ab the
inverse of g^ab and b^a = g^(v′a)/g^(u′v′), as the frame calculation in the proof of [[lem:loc-axis-jets]] shows; these
are smooth, since g and the coordinates are, and by G-equivariance γ is a G-invariant metric on S³ and b a G-invariant
vector field: this is [[eq:loc-double-null]] with fields smooth through the axes. The rest is as there. ∎

**Lemma {#lem:loc-axis-dependence}** (Dependence on the past faces of a double-null rectangle.) Let Ĝ′ be a smooth
G-invariant Lorentzian metric, and, for i = 1, 2, let U_i = (g_i, p_i^in, p_i^out, div_(g_i) P_i^A, q_i^A) be smooth
G-invariant states on a neighbourhood 𝒪 of a compact set R′, with p_i^A the negative of the differential of a function
on 𝒪 that is null for g_i, the phase of family A of U_i, and P_i^A := g_i⁻¹p_i^A future directed, that solve
[[eq:class-system]] on R′ in the gauge D(g_i) = 0 relative to Ĝ′. Let (ũ, ṽ, ω̃), ω̃ ∈ S³, be coordinates on 𝒪 with
p_1^out = −dũ and p_1^in = −dṽ, in which g_1 has the form [[eq:loc-double-null]] with fields smooth through the axes
and R′ = [0, a] × [0, b] × S³. If U_2 and U_1 agree, with all their derivatives, on R′ ∩ ({ũ = 0} ∪ {ṽ = 0}), then
U_2 = U_1 on R′. No smallness of U_1, of U_2 or of U_2 − U_1 is assumed.

*Proof.* *The chart.* Fix μ ≥ 1 with 4μΩ_1² > γ_1(b_1, b_1) on R′, and put t := ũ + ṽ and x := e^(ṽ − μũ) ω̃. (t, x) is
a G-equivariant chart near R′ onto an open set of ℝ × (ℝ⁴ ∖ {0}); dt is timelike for g_1, and ∂_t, a positive multiple
of ∂_ũ + μ ∂_ṽ, is future timelike for g_1 on R′, as g_1(∂_ũ + μ∂_ṽ, ∂_ũ + μ∂_ṽ) = −4μΩ_1² + γ_1(b_1, b_1). So the
first-order form of Step 9 of the proof of [[thm:class-stability-off-axes]] in this chart has A^0 positive definite at
U_1 on R′. The slices O_s := R′ ∩ {t = s} are unions of spheres {ũ = c, ṽ = s − c}.

*The equations.* Let x ∈ R′ lie near an axis in a slice {t = s}, and let the level set through x, in that slice, of the
phase of family A of U_i be, from the axis to x, a graph as in [[lem:loc-axis-leaf]] (ii) that lies in 𝒪, with p_A(∂_z)
≠ 0. Then it is the leaf of U_i through x, by that lemma: p_A vanishes on it, and its expansion is Θ_A, as in the proof
of its part (iii), the phase being null on 𝒪. So σ_A[U_i](x) is its planar shear, and by [[eq:class-identity]],
[[eq:class-x]] and [[prop:class-axis]] (d) both S_A and S_A^ax equal −|∇²u_A|² − T(P_A, P_A) at x, u_A the phase; by
[[eq:class-raychaudhuri]], U_i solves at x the rows of 𝒜^ax, with [[eq:loc-axis-closure]], Ĝ′ in place of Ĝ and every
partition ψ_ax. For U_1 this holds at every point of R′ near an axis: the level sets of its phases in {t = s} are the
spheres {ũ = c, ṽ = s − c}, which are therefore the leaves of both families of U_1.

*Continuity in t.* Let t* be the supremum of the s ∈ [0, a + b] with U_2 = U_1 on R′ ∩ {t ≤ s}; the set of these s is
closed, and it contains 0, R′ ∩ {t ≤ 0} being the corner sphere. Suppose t* < a + b. Take δ, the balls 𝔅 ⊂ 𝔅′ and the
constants of [[lem:class-leaf-differences]] and [[lem:loc-axis-shear]] for ů := U_1 in this chart (their proofs use of
ů only that it is a smooth G-invariant state whose p_A are minus the differentials of null phases and whose Θ_A are div
P_A, which U_1 is on 𝒪), uniform near the points of the axes in R′ ∩ {t* ≤ t ≤ t* + 1}. U_2 − U_1 is smooth and
vanishes with all derivatives on 𝒦 := R′ ∩ {t ≤ t*}, on the past faces by hypothesis. For θ ∈ (0, 1] let 𝒩_θ be the set
of the points of 𝒪 whose coordinates (ũ, ṽ) lie within θ of those of a point of 𝒦. 𝒦 is convex in (ũ, ṽ), so for θ
small each point of 𝒩_θ is joined to its nearest point of 𝒦, with the same ω̃, by a segment in 𝒩_θ ⊂ 𝒪, and Taylor's
formula along it bounds the derivatives of order at most k of U_2 − U_1 on 𝒩_θ by Cθ^(k+1), C not depending on θ. Let
χ_θ be a G-invariant cut-off equal to 1 on 𝒩_(θ/2) and supported in 𝒩_θ, whose derivatives of order j are at most
Cθ^(−j), and W := U_1 + χ_θ (U_2 − U_1); by Leibniz's rule the derivatives of order at most k of W − U_1 are at most
Cθ, so for θ small W ∈ 𝔅′ on the slices. Let s ∈ [t*, t* + θ/8] and let x ∈ O_s lie near an axis. R′ is star-shaped
about (0, 0) in (ũ, ṽ), and the point (t*/s)(ũ, ṽ)(x) lies in 𝒦 within √2 (s − t*) of (ũ, ṽ)(x); so O_s ⊂ 𝒩_(θ/4), and
the arc of the leaf of U_1 through x lies in 𝒩_(θ/4), O_s being a union of its leaves. While the arc of the leaf of W
through x stays in 𝒩_(θ/2), where W = U_2, it lies within Cθ² of that one in C¹, U_2 − U_1 being at most Cθ² in C¹
there; for θ small, Cθ² < θ/4, so it stays in 𝒩_(θ/2), and by the uniqueness in [[lem:class-volterra]] it is the arc of
the leaf of U_2, and σ_A[W] = σ_A[U_2] on O_s. Likewise the level set through x, in O_s, of the phase of family A of
U_2, whose differential is within Cθ² of that of U_1 on 𝒩_θ, is from the axis to x a graph within Cθ² in C¹ of the
sphere through x, which lies in 𝒩_(θ/4); for θ small it lies in 𝒩_(θ/2) ⊂ 𝒪, so U_2 solves the rows of 𝒜^ax at x.
[[lem:loc-axis-shear]], with U_1 in place of U, O_s being a union of its leaves, and W in place of U′, gives ‖σ_A[U_2]
− σ_A[U_1]‖_(L²(O_s∩𝒰_δ(p))) ≤ C ‖U_2 − U_1‖_(L²(O_s)) at every such point p of an axis. So the difference z of the
first-order variables of U_2 and U_1 satisfies on R′ ∩ {t* ≤ t ≤ t* + θ/8} a system 𝐀^μ ∂_μ z = Mz + 𝔫, with 𝐀^μ at
U_1, M bounded and ‖𝔫(s)‖ ≤ C ‖z(s)‖. The lateral boundary of this set consists of pieces of {ũ = 0} and {ṽ = 0}, where
z = 0, and of {ũ = a} and {ṽ = b}, whose outward conormals dũ and dṽ are null for g_1, positive on ∂_t and nonnegative
on the transport fields of U_1 (dũ(P_1^out) = 0 < dũ(P_1^in) and dṽ(P_1^in) = 0 < dṽ(P_1^out)); so the boundary matrix
is nonnegative there (the paragraph after [[lem:loc-cone-energy]]). [[lem:loc-axis-energy]], with B_0 the slice {t =
t*} and the pieces of the past faces, gives z = 0 on R′ ∩ {t ≤ t* + θ/8}, against the definition of t*. So t* = a + b.
∎



**Lemma {#lem:loc-axis-unique}** (Uniqueness in the double-null gauge.) Let k ≥ 9, let Q1′ := [0, u_1′] × [0, v_1′] ⊂
Q1 with u_1′, v_1′ > 0, and let (g′, q′_in, q′_out) be a class solution in the gauge through the axes on Q1′ × S³ that
induces the cone data on the edges of Q1′, with fields within ε_2 of the background's in C^(k−4). For ε and ε_2 small,
depending only on k, u_1, v_1, δ_1, the background and the numbers fixed in [[sec:loc-axis-reduced]], it equals the
solution of [[lem:loc-axis-gauge]] on Q1′ × S³.

*Proof.* (1) *An extension of g′.* By [[lem:loc-axis-jets]] (b) and (iv) of [[lem:loc-cone-jets]], Q1′ being a past set
in F, the fields and densities of g′, like those of Ĝ, have the derivatives a_j and b_k across N ∩ Q1′, so their
differences f from those of Ĝ vanish to infinite order on N ∩ Q1′; f is a family over Q1′ of G-invariant functions,
symmetric 2-tensors and vector fields on S³, and we put f := 0 on P. Fix δ_2 ∈ (0, δ_c/4] so small that Q1^+ := [−δ_2,
u_1 + δ_2] × [−δ_2, v_1 + δ_2] lies in the interior of 𝒰^♯ and Q1^+ ∩ F in 𝔗(s*), which is possible as Q1 ⊂ 𝔗(s* − 1)
and τ is continuous, and put Q1′^+ := [−δ_2, u_1′ + δ_2] × [−δ_2, v_1′ + δ_2]. The operator E of
[[thm:std-ly-extension]] (i) acts at each fixed x′, so it is an operator on functions of one variable on [0, ∞),
bounded on C^r for every r. Fix ψ ∈ C^∞(ℝ) equal to 1 on (−∞, δ_2/2] and to 0 on [3δ_2/4, ∞). For c ∈ ℝ and h smooth on
[c − δ_2, c] put X_c h := h on [c − δ_2, c] and (X_c h)(w) := E[ψ h(c − ·)](c − w) for w ∈ (c, c + δ_2], ψ h(c − ·)
being read as a function on [0, ∞) that vanishes beyond 3δ_2/4. X_c is linear, X_c h is smooth, E[ψ h(c − ·)] being
smooth on ℝ and equal to h(c − ·) on [0, δ_2/2], and its C^r norm is at most C_r times that of h, C_r depending only on
r and δ_2. Apply X_(u_1′) in u, at each fixed (v, ω) and in the space of tensors at ω, to f on [−δ_2, u_1′] × [−δ_2,
v_1′], and then X_(v_1′) in v, at each fixed (u, ω), to the result on [−δ_2, u_1′ + δ_2] × [−δ_2, v_1′]. These
operators act in (u, v) only and linearly, so they commute with derivatives along S³ and with G; the result f″ is
smooth on Q1′^+ × S³, G-invariant and smooth through the axes, equals f on Q1′, and its fields are at most C(ε + ε_2)
in C^(k−4), with C independent of u_1′ and v_1′. As f vanishes where u < 0 and where v < 0, so does f″. Let g″ be the
metric [[eq:loc-double-null]] whose fields are those of Ĝ plus those of f″ on Q1′^+ and those of Ĝ on P ∩ Q^♯, and q″_A
the densities of Ĝ plus those of f″, and those of Ĝ on P ∩ Q^♯. For ε and ε_2 small g″ is Lorentzian, and it is smooth
on Q1′^+ ∪ (P ∩ Q^♯); it equals g′ on Q1′ and Ĝ on P, and g″ − Ĝ vanishes to infinite order on N ∩ Q1′^+, being smooth
and zero on P there.

(2) *A wave map.* As in step (2) of the proof of [[lem:loc-cone-unique]], seek Φ = id + φ with id: (Φ(Q1′), (Φ⁻¹)^*g″)
→ Ĝ a wave map, here in the chart [[eq:loc-axis-time]] with the initial slice Σ_init, with no cut-off in ϑ, with the
cut-off χ′ := β′(u − u_1′) β′(v − v_1′) χ in (u, v), χ that of [[sec:loc-axis-reduced]] and β′ ∈ C^∞(ℝ) equal to 1 on
(−∞, δ_2/4] and to 0 on [δ_2/2, ∞), and with the frozen part taken with the wave operator of g_e. χ′ equals 1 on a
neighbourhood of Q1′ and is supported in (Q1′^+ ∪ P) ∩ supp χ, where g″ is defined. The wave map system is semilinear
and local, with coefficients smooth in the chart through the axes. φ := 0 satisfies the cut-off system on P exactly, as
g″ = Ĝ there, and on F up to the residual χ′ 1_F g″^(μν) (Γ[Ĝ] − Γ[g″])^λ_(μν), which is smooth, as g″ − Ĝ vanishes to
infinite order on N ∩ Q1′^+, and at most C(ε + ε_2) in C^(k−5), C independent of u_1′ and v_1′.
[[thm:class-kato-stability]] (a), with s := k − 5 > 3, gives a smooth G-equivariant solution φ on [τ_init, s*] × ℝ⁴, at
most C(ε + ε_2)^(1/(4s)) in W^(1,∞); φ = 0 on P ∩ 𝒰^♯, by the argument of the proof of [[lem:loc-cone-past]]; and φ
solves the wave map system near Q1′, χ′ being 1 there.

(3) *Comparison.* For ε and ε_2 small, Φ is a G-equivariant diffeomorphism near the identity, equal to it on P ∩ 𝒰^♯
and so, with all derivatives, on N, with Φ(F) ⊂ F near Q1, and Φ(Q1′) and a neighbourhood of it lie in 𝒰′ = (P ∩ 𝒰^♯) ∪
𝔗(s*), by the choice of δ_2. Put g̃ := (Φ⁻¹)^*g″, ũ := u ∘ Φ⁻¹, ṽ := v ∘ Φ⁻¹, ω̃ := ω ∘ Φ⁻¹ and q̃_A := q″_A ∘ Φ⁻¹ near
Φ(Q1′). Then g̃ is in the gauge D(g̃) = 0 relative to Ĝ near Φ(Q1′); it has the form [[eq:loc-double-null]] with fields
smooth through the axes in the coordinates (ũ, ṽ, ω̃), in which Φ(Q1′) = [0, u_1′] × [0, v_1′] × S³ and ũ, ṽ are null
for g̃; (g̃, ṽ, ũ, q̃_in, q̃_out) solves [[eq:class-system]] on Φ(Q1′); and the state of g̃ agrees with Û, hence with
U, with all derivatives on N ∩ Φ(Q1′) = N ∩ Q1′. U is, on 𝒰′, of the form required in [[lem:loc-axis-dependence]], its
phases u_in and u_out being null for g there, and solves [[eq:class-system]] on 𝔗(s*) in the same gauge
([[lem:loc-axis-propagation]]). [[lem:loc-axis-dependence]], with Ĝ′ := Ĝ, U_1 the state of g̃, R′ := Φ(Q1′) and U_2 :=
U, gives that U is the state of g̃ on Φ(Q1′).

(4) *Conclusion.* As in step (4) of the proof of [[lem:loc-cone-unique]], with the point ω of S³ in place of ϑ: Φ is an
isometry from (g′, u, v) to (g, u_out, u_in) on Q1′, with u = u_out ∘ Φ and v = u_in ∘ Φ; it carries g′⁻¹du to
g⁻¹du_out, so ω′ ∘ Φ is constant along the integral curves of g′⁻¹du, which are the curves of constant u and ω, and
equals ω on N_i, where Φ is the identity. So Ψ ∘ Φ is the identity on Q1′, and g′ has there the fields of the solution
of [[lem:loc-axis-gauge]]. ∎

**Lemma {#lem:loc-axis-angle}** (Localisation near an axis.) Let ϑ_a′ ∈ (0, π/4], and let the cone data equal the
background's at the points with ϑ < ϑ_a′. Then U = Ů at the points of 𝔗(s*) with ϑ < ϑ_a′ − 2C_* (uv)^(1/2), and Ψ is
the identity there. Likewise, for ϑ_b′ ∈ [π/4, π/2), with ϑ > ϑ_b′ and ϑ > ϑ_b′ + 2C_* (uv)^(1/2).

*Proof.* By [[lem:loc-axis-jets]] (b) all derivatives across N are the background's at the points with ϑ < ϑ_a′, so Δ
vanishes there ([[lem:loc-axis-jets]] (c)), and Ĝ = g_e and Û = Ů there. There Ů solves 𝒜^ax: the background solves
[[eq:class-system]], D(g_e) = 0 relative to Ĝ = g_e, and the residual of [[eq:loc-axis-closure]] vanishes for it
([[lem:loc-axis-system]] (d), (e)). For ι ∈ (0, ϑ_a′/4) and δ′ ∈ (0, δ_c] put α := ϑ_a′ − ι − 2C_* e^(τ_1/2), τ_1 :=
ln((u + δ′)(v + δ′)), and 𝒲 := 𝔗(s*) ∩ {α ≥ ι, ϑ ≤ α}; τ_1 is smooth on F. In the (u, v)-plane {τ ≤ s} and {α ≥ ι} are
the sets below the graphs of decreasing smooth functions of u, so every 𝒲 ∩ {τ ≤ s} lies below the graph of their
minimum, a Lipschitz function, and is a Lipschitz domain, as [[lem:loc-axis-energy]] needs, also where the face {α = ι}
touches a slice, as it does at the points of Q1 with u = v. Its lateral boundary consists of a piece of N, where U − Ů
vanishes with all derivatives ([[lem:loc-axis-past]], with Û = Ů there), of a piece of the level set {α = ι} of τ_1,
with the outward conormal dτ_1, future timelike for g_e and positive on ∂_τ and on the P̊_A, and of the face {ϑ = α},
which lies off the axes and has the outward conormal ν := dϑ + C_* e^(τ_1/2) dτ_1; as in the proof of
[[lem:loc-cone-support]], g_e⁻¹(ν, ν) = R_e⁻² − 2C_*² e^(−2σ_e) < 0, ν(∂_τ) > 0 and ν(P̊_A) > 0. So the boundary matrix
at 𝐔̊ is nonnegative on both faces. z := 𝐔 − 𝐔̊ satisfies on 𝒲, where U and Ů solve 𝒜^ax, a system 𝐀^μ ∂_μ z = Mz + 𝔫
with 𝐀^μ at 𝐔̊ and 𝔫 the difference of the terms in σ_A. Let O_s be the interior of 𝒲 ∩ Σ_s. Near axis 2 the leaf of Ů
through a point x of O_s is the sphere {(u(x), v(x))} × S³, and its arc from the axis to x has the same (u, v) and ϑ ≤
ϑ(x), so it lies in the closure of O_s; near axis 1 there is nothing to estimate, ψ_ax vanishing on {ϑ ≤ π/4} near axis
1, as ρ1 = |y| cos ϑ ≥ ρ_-/√2 > δ/2 there. So [[lem:loc-axis-shear]], with Ů in place of U and U in place of U′, gives
‖𝔫(s)‖ ≤ C ‖z(s)‖. [[lem:loc-axis-energy]] on 𝒲, with B_0 the piece of N and B_1 the two faces, gives z = 0. A point of
𝔗(s*) with ϑ < ϑ_a′ − 2C_* (uv)^(1/2) lies in 𝒲 for ι and δ′ small. The past integral curve of P_out = P̊_out, a
multiple of ∂_v, from a point of 𝒲 keeps u and ω and decreases v, so α increases along it, and it stays in 𝒲 until it
meets N_i, and then lies in P; so Ψ is the identity on 𝒲 ([[lem:loc-axis-gauge]]). Near axis 1 the same argument
applies with π/2 − ϑ in place of ϑ. ∎

*Proof of [[thm:loc-axis]].* By [[lem:loc-axis-constraints]] (c), with 2p = 2m_0 + 6 = m_1, the data extend to cone
data of either sign through the axes on N_o and N_i, in the normalised gauge, of size at most Cε in C^(m_0), equal to
the given data, with their nonnegative densities, on {0} × [0, v_1] and [0, u_1] × {0}. For ε small,
[[lem:loc-axis-cauchy]], [[lem:loc-axis-past]], [[lem:loc-axis-propagation]] and [[lem:loc-axis-gauge]] give (a) and
(b): in the coordinates of [[lem:loc-axis-gauge]] the phases are v′ and u′, so the densities are nonnegative on Q1 by
[[lem:loc-axis-propagation]]. (c) is [[lem:loc-axis-unique]]. For the first part of (d), the background is a class
solution in the gauge through the axes on [0, u′] × [0, v′] × S³ for 0 < u′ < min(u_K, u_1) and 0 < v′ < min(v_K, v_1),
inducing the data on the edges of that rectangle, so by (c) the solution equals it there. The second part is
[[lem:loc-axis-angle]], Ψ being the identity on the sets concerned, which contain those of (d) within Q1. ∎

#### The background of this chapter on the crossing rectangle {#sec:loc-axis-example}

**Corollary {#cor:loc-axis-cones}** (Cone data reaching the axes for the background of [[sec:bg-data]].) Let k ≥ 9 and
v_1 > 0, and let V1 be chosen as in [[lem:civp-large-rectangle]]. On 𝒞_out ∩ {v ≤ v_1} let free data (ℓ_1, ℓ_2, ℓ_3)
and q_in ≥ 0 be given as in [[prop:loc-cones]], and on 𝒞_in ∩ {u ≤ 7.2} free data and q_out ≥ 0 as in
[[lem:loc-cone-in]], with Ω the background's on both cones, b = 0 on 𝒞_in, the values of ϕ, ∂_vϕ, b and ∂_vb at v = 0
on 𝒞_out and of ϕ and ∂_uϕ at u = 0 on 𝒞_in the background's, and the two sets of free data agreeing on S, but with no
restriction of their supports in angle: the metrics γ̂ of [[lem:loc-axis-constraints]] (b) that they define are smooth
metrics on S³, the densities are smooth through the axes, and these differ from dΩ₃² and from the background's
densities by at most ε in C^(m_1 + 3). For ε small the constraints determine cone data through the axes, and their
development of [[thm:loc-axis]] exists on [0, 7.2] × [0, v_1] × S³, with (b)–(d) there. So, with v_1 = 4.5, every small
perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} and of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, at once, and every
small density added on either cone, the axes included, has a development on the whole rectangle [0, 7.2] × [0, 4.5] in
which the two dusts cross.

*Proof.* By [[lem:civp-large-rectangle]] (a) there is δ ∈ (0, 1/2) such that the background is smooth on [0, 7.2 + 2δ]
× [0, v_1 + 2δ] and solves [[eq:two-dust-limit]] there, and Ω and R extend to smooth positive functions on [−δ, 7.2 +
δ] × [−δ, v_1 + δ]. With δ_1 := min(δ, v_1)/2, σ_e := ln(√2 Ω) and R_e := R there, this is a background on Q1 := [0,
7.2] × [0, v_1] with margin δ_1, Q^♯ lying in [−δ, 7.2 + δ] × [−δ, v_1 + δ] and Q^♯ ∩ F in [0, 7.2 + 2δ] × [0, v_1 +
2δ]. By [[lem:loc-axis-constraints]] (b) the constraints determine Y and b along every generator, the axis generators
included. The coefficients of the equation for Y differ from the background's by at most Cε in C^(m_1 + 2), and its
initial values are the background's, so Y − R_e is at most Cε in C^(m_1 + 2) and Y > 0 for ε small; then the
coefficients and the inhomogeneous term of the equation for W are within Cε of the background's in C^(m_1), and b is at
most Cε in C^(m_1). So the cone data are cone data through the axes in the normalised gauge, of size at most Cε in
C^(m_1), with nonnegative densities, and [[thm:loc-axis]] applies. ∎

**Remark {#rem:loc-axis-constants}** (What the constants depend on.) [[lem:loc-axis-leaf]] and [[lem:loc-axis-shear]]
use no smallness: the constant of [[eq:loc-axis-shear]] depends only on the ball 𝔅′ about a solution, that is on bounds
of the states in C² and on the lower bound of |p_A(∂_z)| at the axis, and on the chart, and not on the set O.
[[lem:loc-axis-dependence]] uses no smallness of either solution, only the leaf constants of the first one near the
times up to which the two agree. [[lem:loc-axis-jets]] uses no smallness except for the Lorentzian character of Ĝ, and
the constraints of [[lem:loc-axis-constraints]] (b) need only Y > 0. In the existence proof smallness enters in four
places: Û must lie in the ball 𝔅′ about Ů, through ‖Δ‖_(C^(k+3)) ≤ Cε ([[lem:loc-axis-jets]] (c)); the solution must
stay, over the whole interval [τ_init, s*], in the ball 𝒟_ρ about the background in H^k on which the term in σ_A is
defined, which the bound of [[lem:loc-axis-system]] (e) gives ([[lem:loc-axis-cauchy]]); Ψ of [[lem:loc-axis-gauge]]
must be close enough to the identity for its image to contain Q1 × S³; and the extension of the data beyond u_1 and v_1
must keep Y positive ([[lem:loc-axis-constraints]] (c)), as must the constraints in [[cor:loc-axis-cones]]. The
uniqueness of [[lem:loc-axis-unique]] needs ε and ε_2 small for its wave map. The radius ρ, the number δ and the leaf
constants are those of the background, and the constants of [[lem:loc-axis-system]] (a) and of [[lem:loc-axis-cauchy]]
do not depend on ε.

**Remark {#rem:loc-axis-scope}** (What [[thm:loc-axis]] does not give.) (i) *Large data at the axes.* The term in σ_A
is defined, through [[lem:class-leaf-differences]], on balls about a solution, and the Cauchy problem is solved about
the background over the whole interval; for cone data that are not near the background's at the axes nothing is
asserted there. Off the axes, [[thm:civp-large]] needs no smallness. (ii) *Further families.* Only the two families
adapted to the double-null gauge are treated. A further family with a density at a point where a cone meets an axis
would need the sections of that cone by the slices to be among its leaves, which for a solution, whose leaves are the
level sets of its phase ([[lem:class-leaf-differences]]), requires its phase to be constant on them; one whose density
reaches an axis inside F would need its expansion defect to be estimated on a region that contains a whole
neighbourhood of the axis on which its cut-off ζ_A equals 1, as in Step 10 of the proof of [[thm:class-stability]],
while ζ_A must vanish near the points where the cones meet the axes. Neither case is treated here, nor are further
families whose densities avoid the axes. (iii) *Regularity.* The data are smooth and small in C^(m_1); densities that
are only bounded, or measures, are not covered ([[rem:loc-cone-scope]] (iii)).

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:". The old
texts are quoted from the chapter sources at the current head, into which the sections of Tiers 1 and 2 and the section
on null shells are merged ([[sec:loc-cone-proof]], [[sec:civp-large]] and [[sec:loc-shells]], with the texts of their
placements); every old text occurs there exactly once, as whole lines. Line numbers are those of the current chapter
sources and serve only to find the place. Where the text at a site was written by the null-shell placement (items 3, 7
and 10), the new text keeps that wording verbatim and adds only what this section adds.

*1. Where the section goes.* The section above, from its heading through [[rem:loc-axis-scope]], is inserted in
[[ch:localised-data]] as a new section between the Tier 2 section and the section on null shells: immediately after the
last line of [[rem:civp-large-beyond]], which ends the Tier 2 section with "not explicit and no estimate of the
solution is given." (line 2407), and immediately before the heading
"### Null shells along the leaves {#sec:loc-shells}" (line 2409), with one blank line before and one after. Its heading
is of the level of [[sec:civp-large]] and its four subsections of the level below. It defines sec:loc-axis,
thm:loc-axis, sec:loc-axis-data, def:loc-axis-data, lem:loc-axis-constraints, eq:loc-axis-cone, lem:loc-axis-jets,
eq:loc-axis-principal, sec:loc-axis-leaves, eq:loc-axis-hl, lem:loc-axis-leaf, lem:loc-axis-shear, eq:loc-axis-shear,
sec:loc-axis-reduced, eq:loc-axis-time, eq:loc-axis-region, eq:loc-axis-closure, lem:loc-axis-system,
lem:loc-axis-energy, lem:loc-axis-cauchy, lem:loc-axis-past, lem:loc-axis-propagation, lem:loc-axis-gauge,
lem:loc-axis-dependence, lem:loc-axis-unique, lem:loc-axis-angle, sec:loc-axis-example, cor:loc-axis-cones,
rem:loc-axis-constants and rem:loc-axis-scope, none of which is defined elsewhere. Numbers are resolved at assembly.

*2. [[ch:localised-data]], the opening paragraph, its last two lines on the cones (lines 13–14).* A sentence on this
section is added before the sentence on Σ_τ0. Old:

background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). On Σ_τ0 the
constraints split, after Rácz

New:

background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). Data near the
background's need not be localised away from the axes: they have a development in that gauge on the whole rectangle
spanned by the two cones, with an estimate, unique in the gauge among nearby solutions ([[thm:loc-axis]],
[[cor:loc-axis-cones]]). On Σ_τ0 the constraints split, after Rácz

*3. [[ch:localised-data]], the paragraph after [[rem:loc-cone-scope]] on the developments of these cone data (lines
702–721), first its lines 707–708.* A sentence on this section is inserted after the sentence that ends with
"([[lem:loc-cone-strips]] (c))", and the next sentence names its data, which are no longer the only ones the paragraph
speaks of. Old:

added in the band, supported away from the axes, is of this kind, with v_1 = 4.5 and u_1 = 7.2 ([[lem:loc-cone-strips]]
(c)). Without smallness, these cone data, completed on 𝒞_in in the gauge b = 0 ([[def:civp-large-data]]), have a

New:

added in the band, supported away from the axes, is of this kind, with v_1 = 4.5 and u_1 = 7.2
([[lem:loc-cone-strips]] (c)). Near the background's the restriction to a band can be dropped: cone data given as in
[[prop:loc-cones]] and [[lem:loc-cone-in]] with no restriction of their supports in angle, their metrics on the spheres
and their densities smooth through the axes, among them every small perturbation of the shell and of the packet at once
and every small density added on either cone, the axes included, have a development in the gauge [[eq:loc-double-null]]
on every rectangle [0, 7.2] × [0, v_1], among them [0, 7.2] × [0, 4.5], in which the two dusts cross, with an estimate,
unique in that gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]). Without smallness, the cone
data localised in a band, completed on 𝒞_in in the gauge b = 0 ([[def:civp-large-data]]), have a

*3, continued: its last five lines (lines 717–721), as the null-shell placement wrote them.* The data that the chapter
does not develop are now those that differ from the background's near an axis without being near the background's; the
rest of the sentence, with its exception for null shells, is unchanged. Old:

asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
that are not smooth, except finitely many null shells along leaves of the two cones with densities smooth in angle and
data that are smooth except across such leaves, where the metric functions are continuous, which [[thm:loc-shells]]
develops slab by slab with [[thm:civp-large]] and [[thm:loc-cone-development]]; no result of the other chapters uses
these developments.

New:

asserted for cone data that differ from the background's near an axis and are not near the background's
([[rem:loc-axis-scope]]), for data of finite regularity or for densities that are not smooth, except finitely many null
shells along leaves of the two cones with densities smooth in angle and data that are smooth except across such leaves,
where the metric functions are continuous, which [[thm:loc-shells]] develops slab by slab with [[thm:civp-large]] and
[[thm:loc-cone-development]]; no result of the other chapters uses these developments.

*4. [[rem:loc-cone-scope]] (ii), its last two sentences (lines 684–688).* Such data are developed near the background's
by [[thm:loc-axis]], and the statement that no domain-of-dependence statement with null boundaries near an axis is
proved no longer holds for double-null rectangles ([[lem:loc-axis-dependence]]). (iii), which begins on the next line,
is unchanged. Old:

background, which reach the axes, are carried there by the background itself. For data whose perturbation reaches an axis
this fails: at an axis the augmented system is not local, its Cauchy theory ([[thm:class-stability]]) needs lateral
boundaries adapted to the dust, and no domain-of-dependence statement with null boundaries near an axis is proved in this
paper. No development is asserted for such data, and (d) gives uniqueness near the axes only among solutions that equal
the background there. (iii) *Regularity.* The data are smooth and near the background's in C^m, m = 6k + 21. Densities

New:

background, which reach the axes, are carried there by the background itself. For data whose perturbation reaches an
axis this proof fails: at an axis the augmented system is not local, and its Cauchy theory ([[thm:class-stability]])
needs lateral boundaries adapted to the dust. Near the background's such data are developed on the whole rectangle when
the background is defined on it with a margin, with uniqueness in the gauge among nearby solutions, by a reduction that
keeps the closure of the Raychaudhuri equation at the axes ([[thm:loc-axis]]); (d) gives uniqueness near the axes only
among solutions that equal the background there. (iii) *Regularity.* The data are smooth and near the background's in
C^m, m = 6k + 21. Densities

*5. [[rem:loc-cone-scope]] (iv) (lines 698–700).* Old:

achieves the prescribed initial data." (iv) *The domain.* The development is asserted on G_*, a neighbourhood of the two
cones, and not on the whole rectangle [0, u_1] × [0, v_1]; in particular not where the two dusts cross away from the
cones.

New:

achieves the prescribed initial data." (iv) *The domain.* The development is asserted on G_*, a neighbourhood of the
two cones, and not on the whole rectangle [0, u_1] × [0, v_1]; in particular not where the two dusts cross away from
the cones. That rectangle is reached by [[thm:loc-axis]] when the background is defined on it with a margin, as the
background of [[sec:bg-data]] is on [0, 7.2] × [0, v_1] for every v_1 > 0 ([[lem:civp-large-rectangle]] (a),
[[cor:loc-axis-cones]]).

*6. [[rem:loc-cone-local-scope]], its last sentence (lines 1644–1646).* Old:

terms of the C^(m_1 + 1) norms of the old ones. A statement with no background, the data being prescribed up to the axes,
needs a local theory of the augmented system at the axes, with a domain of dependence for null boundaries there, and is
not given in this paper.

New:

terms of the C^(m_1 + 1) norms of the old ones. A statement with no background, the data being prescribed up to the
axes, needs a local theory of the augmented system at the axes for data that are not near a known solution there, and
is not given in this paper: [[thm:loc-axis]] solves the reduced problem through the axes about the background only, and
the dependence on the past faces of a double-null rectangle that its proof uses ([[lem:loc-axis-dependence]]), which
needs no smallness, gives uniqueness and not existence.

*7. [[rem:civp-large-domain]], its last sentence, as the null-shell placement wrote it (lines 2385–2389).* One sentence
is appended. Old:

are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity, densities that are only bounded,
or measure-valued densities other than finitely many null shells along leaves of the two cones with densities smooth in
angle; those, and data that are smooth except across finitely many leaves, where the metric functions are continuous,
are developed slab by slab with [[thm:civp-large]] in [[thm:loc-shells]].

New:

are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity, densities that are only bounded,
or measure-valued densities other than finitely many null shells along leaves of the two cones with densities smooth in
angle; those, and data that are smooth except across finitely many leaves, where the metric functions are continuous,
are developed slab by slab with [[thm:civp-large]] in [[thm:loc-shells]]. Cone data near the background's that differ
from it at the axes are developed on the whole rectangle by [[thm:loc-axis]].

*8. [[ch:class-system]], [[lem:class-leaf-differences]], the definition of the leaves (lines 1326–1329).* The formula
of step (1) of [[lem:class-planar-shear]] holds n(u) and the trace of K_Σ over TΣ_L, the tangent plane of the leaf,
which for a state whose p_A is not closed is not defined before the leaf is; the clause reads it with p_A(n) and with a
plane fixed by p_A, as [[eq:loc-axis-hl]] does, and changes no statement or proof of that chapter: on a solution with
p_A the differential of a phase the two readings agree. The placement of the Tier 4 section (its item 2) changes the
same lines for the same reason; this text contains its clause, the γ3-orthogonal complement of the spatial part of p_A
in place of TΣ_L, and one copy is kept. Old:

be the graphs z = h(r) through the points of the axis near that point, each solving [[eq:class-leaf-volterra]] with
H_L := H_L[Θ_A], the formula of step (1) of [[lem:class-planar-shear]] with Θ_A in place of Θ and the spatial part of
p_A in place of ∇_Σ u; they exist and are unique by [[lem:class-volterra]], and for U near ů they are C¹-close to the
leaves of ů and foliate a neighbourhood of the axis. Let σ[U] at a point be the planar shear [[eq:class-shear-leaf]] of

New:

be the graphs z = h(r) through the points of the axis near that point, each solving [[eq:class-leaf-volterra]] with
H_L := H_L[Θ_A], the formula of step (1) of [[lem:class-planar-shear]] with Θ_A in place of Θ, the spatial part p_A^Σ
of p_A in place of ∇_Σ u, p_A(n) in place of n(u), the sign that of p_A(∂_z), and the trace of K_Σ taken over the
γ3-orthogonal complement of p_A^Σ in TM3 in place of TΣ_L. That plane is fixed by p_A at each point, so H_L[Θ_A] is a
function of the point, as [[lem:class-volterra]] requires; when p_A is the differential of a phase it is the tangent
plane of the level set of the phase through the point, and H_L[Θ_A] is the formula of step (1) for that level set. The
leaves exist and are unique by [[lem:class-volterra]], and for U near ů they are C¹-close to the leaves of ů and
foliate a neighbourhood of the axis. Let σ[U] at a point be the planar shear [[eq:class-shear-leaf]] of

*9. [[ch:theorems]], the bullet "More families" (lines 376–381).* The two kinds of data are listed separately. Old:

  construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge
  of data on the two null cones through the corner sphere of the explicit two-dust background of [[sec:bg-data]],
  localised in an angular band away from the axes, with or without dust and without smallness, on a neighbourhood of
  the two cones that depends on the data, localised and unique in the gauge among solutions equal to the background
  near the axes ([[thm:civp-large]]), and, for data near the background's, on an explicit neighbourhood with an
  estimate ([[thm:loc-cone-development]]); and exactly localised vacuum data

New:

  construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge of
  data on the two null cones through the corner sphere of the explicit two-dust background of [[sec:bg-data]]: of data
  localised in an angular band away from the axes, with or without dust and without smallness, on a neighbourhood of
  the two cones that depends on the data, localised and unique in the gauge among solutions equal to the background
  near the axes ([[thm:civp-large]]), and, for such data near the background's, on an explicit neighbourhood with an
  estimate ([[thm:loc-cone-development]]), and of data near the background's, localised in angle or not, on the whole
  rectangle of the two cones in which the two dusts cross, [0, 7.2] × [0, 4.5], with an estimate and unique in the
  gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]); and exactly localised vacuum data

*10. [[ch:scope]], the paragraph on localised data, its last seven lines (lines 217–223), as the null-shell placement
wrote them.* A sentence on this section is inserted before the sentence on the developments that are not established,
which is narrowed accordingly; the sentence on null shells is unchanged. Old:

estimate ([[thm:loc-cone-development]]). Developments of cone data that differ from the background's near an axis are
not established ([[rem:loc-cone-scope]]). Cone data with finitely many null shells along leaves of the two cones, with
densities smooth in angle and supported in a band away from the axes, have developments that are continuous, smooth
between the shells and solutions in the sense of distributions, on a neighbourhood of the cones on which the shells do
not cross, and a solution continues through a crossing sphere on a small square; general measure-valued densities and
shells that are not round at an axis are not treated ([[thm:loc-shells]], [[prop:loc-shell-crossing]],
[[rem:loc-shell-scope]]).

New:

estimate ([[thm:loc-cone-development]]). Cone data near the background's, localised in angle or not, have a development
on the whole rectangle of the two cones, [0, 7.2] × [0, 4.5], in which the two dusts cross, with an estimate and unique
in the gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]). Developments of cone data that differ
from the background's near an axis and are not near the background's are not established ([[rem:loc-cone-scope]],
[[rem:loc-axis-scope]]). Cone data with finitely many null shells along leaves of the two cones, with densities smooth
in angle and supported in a band away from the axes, have developments that are continuous, smooth between the shells
and solutions in the sense of distributions, on a neighbourhood of the cones on which the shells do not cross, and a
solution continues through a crossing sphere on a small square; general measure-valued densities and shells that are
not round at an axis are not treated ([[thm:loc-shells]], [[prop:loc-shell-crossing]], [[rem:loc-shell-scope]]).

*11. Unchanged.* [[ch:introduction]] needs no change: its text on [[part:further]] names "localised data, their
development from two null cones", which covers this section. [[ch:ten-l5]] and the sentences of [[ch:scope]] on the
characteristic problem at 10 l5 stand: that problem is vacuum and not near an explicit background, its data are C³, and
the uniqueness it needs, (F2) of [[lem:tl5-continuation]], is uniqueness in the double-null gauge for solutions on
regions D_s, which [[lem:loc-axis-dependence]] does not give, as it compares two solutions in one wave gauge, and
[[lem:loc-axis-unique]] gives only near the background. [[ch:two-dusts]] is unchanged.

*12. Appendix A and the references.* No new entry: the proofs use no published result beyond those already stated in
[[app:standard-results]]. The extension operator of [[lem:loc-axis-unique]] is that of [[thm:std-ly-extension]] (i),
used in one variable, and the Borel sums of [[lem:loc-axis-constraints]] (c) are those of [[lem:loc-cone-borel]]. No
reference is added.

*13. [[ch:localised-data]], the proof of [[prop:bg-slice]], its paragraph *The packet*, a rewrap only (lines
4707–4711).* The section adds numbered statements to the chapter, so the numbers of its later labels grow; with them
the line that cites [[prop:bg-rays]] reaches 122 characters after assembly. The words are unchanged; the new lines are
at most 121 characters also with every label of the chapter numbered with three digits after the point. Old:

in u (∂_uΨ = G < 0 since f > 0, [[prop:bg-rays]]). It is also decreasing in ρ, since ∂_ρ(Ψ − T) = J − 1/a < 0; hence u_s
is decreasing in ρ, and so is the inverse ρ_s(u). For each row [u_a, u_b] of [[sec:tab-bg-slice-packet]], Ψ̃(u_a, ρ_hi) +
ε₀ < T(ρ_hi) and Ψ̃(u_b, ρ_lo) − ε₀ > T(ρ_lo) (by direct evaluation; at u_a = u1 take ρ_hi ≥ R_* from [[lem:bg-rstar]],
at u_b = u2 take ρ_lo ≤ ρ_u2 from [[prop:bg-seed]] (a)), so the slice points with u_s ∈ [u_a, u_b] have ρ ∈ [ρ_lo,
ρ_hi]. On the box [u_a, u_b] × [ρ_lo, ρ_hi]: μ and ℓ_v lie between their values at u_a and u_b (monotone,

New:

in u (∂_uΨ = G < 0 since f > 0, [[prop:bg-rays]]). It is also decreasing in ρ, since ∂_ρ(Ψ − T) = J − 1/a < 0; hence
u_s is decreasing in ρ, and so is the inverse ρ_s(u). For each row [u_a, u_b] of [[sec:tab-bg-slice-packet]], Ψ̃(u_a,
ρ_hi) + ε₀ < T(ρ_hi) and Ψ̃(u_b, ρ_lo) − ε₀ > T(ρ_lo) (by direct evaluation; at u_a = u1 take ρ_hi ≥ R_* from
[[lem:bg-rstar]], at u_b = u2 take ρ_lo ≤ ρ_u2 from [[prop:bg-seed]] (a)), so the slice points with u_s ∈ [u_a, u_b] have
ρ ∈ [ρ_lo, ρ_hi]. On the box [u_a, u_b] × [ρ_lo, ρ_hi]: μ and ℓ_v lie between their values at u_a and u_b (monotone,

### Crosswalk rows

New rows for the crosswalk table of [[ch:localised-data]], one per label, in chapter order, after the row of
rem:civp-large-beyond and before the row of sec:loc-shells. Each row is given as one line with its four fields
separated by tab characters (label, source, source_name, note). The source is
"paper/reader/proofs/P-CIVP3.md@PENDING:N", N the line of the label in this file and PENDING to be replaced by the
commit at which this file is merged, as in the rows of the Tier 1 and Tier 2 sections.

sec:loc-axis	paper/reader/proofs/P-CIVP3.md@PENDING:1	proof P-CIVP3, section heading	new: Tier 3 of the scoping report, Route B: the faces are leaves of both families; Rendall's reduction to the Cauchy theory of ch:class-system with the non-local closure at the axes
thm:loc-axis	paper/reader/proofs/P-CIVP3.md@PENDING:31	proof P-CIVP3, Theorem (Development of cone data through the axes)	k ≥ 9, m_0 = 6k + 18, m_1 = 12k + 42; existence on Q1 × S³ for any round background on a rectangle with a margin, estimate in C^(k−4), uniqueness in the double-null gauge among nearby solutions, localisation; proved at the end of sec:loc-axis-reduced
sec:loc-axis-data	paper/reader/proofs/P-CIVP3.md@PENDING:63	proof P-CIVP3, subsection	fields smooth through the axes
def:loc-axis-data	paper/reader/proofs/P-CIVP3.md@PENDING:65	proof P-CIVP3, Definition (Fields smooth through the axes)	ln Ω, γ, b as tensors on S³, the metric a smooth field of Lorentzian forms; cone data through the axes; C^r norms with ∇̊
lem:loc-axis-constraints	paper/reader/proofs/P-CIVP3.md@PENDING:82	proof P-CIVP3, Lemma (The constraints through the axes)	Y, γ̂, W in tensorial form; constraints as linear ODEs smooth through the axes; extension beyond u_1, v_1 by Borel sums, equal to the background's where the data are
eq:loc-axis-cone	paper/reader/proofs/P-CIVP3.md@PENDING:90	proof P-CIVP3, display	the constraint components E(∂_v, ∂_v) and E(∂_v, X)
lem:loc-axis-jets	paper/reader/proofs/P-CIVP3.md@PENDING:157	proof P-CIVP3, Lemma (The formal solution through the axes)	transverse jets as tensors on S³; the derivatives across N_o and N_i solve linear ODEs with coefficients smooth through the axes, decoupled by (Ψ1) and (Ψ3); Ĝ, Û and Δ
eq:loc-axis-principal	paper/reader/proofs/P-CIVP3.md@PENDING:204	proof P-CIVP3, display	principal parts of the transverse equations; checked by computer algebra in the review (private)
sec:loc-axis-leaves	paper/reader/proofs/P-CIVP3.md@PENDING:271	proof P-CIVP3, subsection	leaves in a chart; H_L[V] with the plane fixed by p_A
eq:loc-axis-hl	paper/reader/proofs/P-CIVP3.md@PENDING:282	proof P-CIVP3, display	H_L[V]; the reading of H_L[Θ_A] of lem:class-leaf-differences
lem:loc-axis-leaf	paper/reader/proofs/P-CIVP3.md@PENDING:296	proof P-CIVP3, Lemma (The sections of the cones are leaves)	Lemma A of the scoping report: criterion for a hypersurface annihilated by p_A to be a leaf, in the chart; the spheres are leaves of both families of Ů and Û for every time increasing in u and v
lem:loc-axis-shear	paper/reader/proofs/P-CIVP3.md@PENDING:344	proof P-CIVP3, Lemma (The planar shear on unions of arcs of leaves)	lem:class-leaf-differences (b) leaf by leaf, on any set closed under arcs of the first state's leaves, the constant independent of the set
eq:loc-axis-shear	paper/reader/proofs/P-CIVP3.md@PENDING:352	proof P-CIVP3, display	the leaf-wise L² bound
sec:loc-axis-reduced	paper/reader/proofs/P-CIVP3.md@PENDING:415	proof P-CIVP3, subsection	the chart adapted to Q1, the regions, the closure at the axes
eq:loc-axis-time	paper/reader/proofs/P-CIVP3.md@PENDING:427	proof P-CIVP3, display	the time τ adapted to Q1 and the chart (τ, y)
eq:loc-axis-region	paper/reader/proofs/P-CIVP3.md@PENDING:441	proof P-CIVP3, display	the region 𝒰^♯ and the slice-triangles 𝔗(s)
eq:loc-axis-closure	paper/reader/proofs/P-CIVP3.md@PENDING:472	proof P-CIVP3, display	the closure of the Raychaudhuri equation for both families, no cut-off at the axes
lem:loc-axis-system	paper/reader/proofs/P-CIVP3.md@PENDING:480	proof P-CIVP3, Lemma (The modified system through the axes)	(F1)–(F3) on 𝒟_ρ; the non-local residual of Û is local, Û's leaves being the coordinate spheres
lem:loc-axis-energy	paper/reader/proofs/P-CIVP3.md@PENDING:525	proof P-CIVP3, Lemma (Energy with a non-local term)	lem:loc-cone-energy with a term bounded in L² on each slice and without transversality of the faces
lem:loc-axis-cauchy	paper/reader/proofs/P-CIVP3.md@PENDING:534	proof P-CIVP3, Lemma (The Cauchy problem through the axes)	thm:class-kato (a) on the whole interval, smallness keeping the solution in 𝒟_ρ
lem:loc-axis-past	paper/reader/proofs/P-CIVP3.md@PENDING:554	proof P-CIVP3, Lemma (The past of the edges)	U = Û to the past of the cones; the sections of the cones are leaves of U
lem:loc-axis-propagation	paper/reader/proofs/P-CIVP3.md@PENDING:568	proof P-CIVP3, Lemma (The constraints on the slice-triangle)	constraints propagate on 𝔗(s*) ⊃ Q1, the axes included, by the leaf-wise bound
lem:loc-axis-gauge	paper/reader/proofs/P-CIVP3.md@PENDING:603	proof P-CIVP3, Lemma (The double-null gauge through the axes)	Ψ = (u_out, u_in, ω′), the form eq:loc-double-null with fields smooth through the axes
lem:loc-axis-dependence	paper/reader/proofs/P-CIVP3.md@PENDING:623	proof P-CIVP3, Lemma (Dependence on the past faces of a double-null rectangle)	Lemma R of the scoping report: no smallness; time t = ũ + ṽ, chart x = e^(ṽ − μũ) ω̃, continuity in t, a comparison state localised by Taylor's formula on the convex set where the two agree
lem:loc-axis-unique	paper/reader/proofs/P-CIVP3.md@PENDING:678	proof P-CIVP3, Lemma (Uniqueness in the double-null gauge)	extension of g′ by thm:std-ly-extension in one variable, wave map relative to Ĝ, then lem:loc-axis-dependence; k ≥ 9 for s = k − 5 > 3
lem:loc-axis-angle	paper/reader/proofs/P-CIVP3.md@PENDING:734	proof P-CIVP3, Lemma (Localisation near an axis)	ϑ_a′ ≤ π/4 (ϑ_b′ ≥ π/4) so that one axis only is met; face conormal dϑ + C_* e^(τ_1/2) dτ_1 for every δ′
sec:loc-axis-example	paper/reader/proofs/P-CIVP3.md@PENDING:771	proof P-CIVP3, subsection	the background of sec:bg-data on [0, 7.2] × [0, v_1], from lem:civp-large-rectangle (a)
cor:loc-axis-cones	paper/reader/proofs/P-CIVP3.md@PENDING:773	proof P-CIVP3, Corollary (Cone data reaching the axes for the background of sec:bg-data)	every v_1 > 0; with v_1 = 4.5 the shell and the packet perturbed at once, densities on either cone, the axes included
rem:loc-axis-constants	paper/reader/proofs/P-CIVP3.md@PENDING:797	proof P-CIVP3, Remark (What the constants depend on)	the four places where smallness enters in the existence proof, and the wave map of the uniqueness
rem:loc-axis-scope	paper/reader/proofs/P-CIVP3.md@PENDING:812	proof P-CIVP3, Remark (What thm:loc-axis does not give)	large data at the axes; further families (Tier 5); regularity

Changed rows. In the crosswalk table of [[ch:class-system]], the row of lem:class-leaf-differences appends to its
source field "; paper/reader/proofs/P-CIVP3.md@PENDING:965-987", the lines of item 8 above, to its source_name field ";
proof P-CIVP3, Placement 8", and to its note "; H_L[Θ_A] read with p_A(n) and the γ3-orthogonal complement of the
spatial part of p_A, a plane fixed by p_A (eq:loc-axis-hl)". In the table of [[ch:localised-data]] the rows of
rem:loc-cone-scope, rem:loc-cone-local-scope and rem:civp-large-domain append to their notes "; (ii) and (iv) amended
by proof P-CIVP3, Placement 4 and 5", "; last sentence amended by proof P-CIVP3, Placement 6" and "; a sentence on
thm:loc-axis appended by proof P-CIVP3, Placement 7".
