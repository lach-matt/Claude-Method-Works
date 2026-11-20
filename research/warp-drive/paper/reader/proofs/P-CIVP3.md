### Developments of cone data through the axes {#sec:loc-axis}

This section develops cone data near the background's data whose perturbation reaches the axes, on the whole rectangle
spanned by the two cones. [[thm:loc-cone-development]] does not apply to such data: its proof uses the augmented system
of [[sec:class-augmented]] only off the axes, where it is local, and keeps the background near the axes
([[rem:loc-cone-scope]] (ii)). At an axis the Raychaudhuri equation of a family holds the planar shear of its null
hypersurfaces, and [[lem:class-leaf-differences]] computes the planar shear at a point from the leaf through it, the
section of the null hypersurface by a slice, by an integral from the axis along the leaf (Step 6 of the proof of
[[thm:class-stability]]). An energy estimate on a region therefore needs, at each point of a slice of the region near an
axis, the arc of the leaf from the axis to that point to lie in the region. For a time that increases with u and with v
the sections of the cones by the slices are spheres of the data's double-null coordinates, and each of them is a leaf of
both families of every state that has the right values and first derivatives along it ([[lem:loc-axis-leaf]]). The
leaves of a state foliate a neighbourhood of an axis and do not cross these spheres, so the part of a slice to the past
of the cones, and the part between them, consist of arcs of leaves; on such a set the planar shears of two states differ
in L² by at most a constant times the difference of the states, the constant not depending on the set
([[lem:loc-axis-shear]]). With these two facts the construction of [[sec:loc-cone-reduced]], case (I), runs with the
closure of the Raychaudhuri equation at the axes and without a cut-off near them. The constraints propagate on the region
bounded by the two cones and one slice, which contains the whole rectangle when the time is adapted to it
([[eq:loc-axis-time]]). Two solutions in one wave gauge that agree to all orders on the past faces of a double-null
rectangle agree on it, with no smallness of either ([[lem:loc-axis-dependence]]); this gives uniqueness in the
double-null gauge and localisation.

*The background on a rectangle.* We use the notation of [[sec:loc-cone-setting]] and [[sec:loc-cone-reduced]]. Let u_1,
v_1 > 0, δ_1 ∈ (0, min(u_1, v_1)/2] and Q1 := [0, u_1] × [0, v_1]. A *background on Q1 with margin δ_1* is a round metric
g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with σ_e and R_e > 0 smooth on Q^♯ := [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 + 2δ_1],
together with smooth profiles 𝒜(v), ℬ(u) ≥ 0, that solves [[eq:two-dust-limit]] on Q^♯ ∩ F. With l_u := u_1 + δ_1 and
l_v := v_1 + δ_1 the set 𝒮 of [[eq:loc-cone-collar]] lies in Q^♯ and the restriction is a background on 𝒮; so N_o =
{0} × [0, v_1 + 2δ_1] and N_i = [0, u_1 + 2δ_1] × {0}. The double-null functions, the densities q̊_A and the state Ů of
those sections are defined on all of Q^♯, and we put C_* := sup over Q^♯ of e^(σ_e)/R_e.

**Theorem {#thm:loc-axis}** (Development of cone data through the axes.) Let k ≥ 9, m_0 = 6k + 18 and m_1 = 12k + 42,
and let a background on Q1 with margin δ_1 be given. Let cone data through the axes ([[def:loc-axis-data]]) be given on
{0} × [0, v_1] and [0, u_1] × {0}, in the normalised gauge and with nonnegative densities, and let ε be their size in
C^(m_1). There are ε_0, C, ε_2 > 0, depending only on k, u_1, v_1, δ_1 and the background, such that for ε ≤ ε_0 the
following hold.

(a) *Existence.* There is a class solution in the gauge through the axes on Q1 × S³ ([[def:loc-axis-data]]), with an
ingoing family of phase v and density q_in and an outgoing family of phase u and density q_out, so that Ric(g) =
q_in dv ⊗ dv + q_out du ⊗ du, that induces the cone data on {0} × [0, v_1] and on [0, u_1] × {0}. Its metric is smooth on
Q1 × S³, the axes included.

(b) *Estimate.* Its fields ln Ω, γ and b and its densities differ from the background's by at most Cε in C^(k−4), in the
norms of [[def:loc-axis-data]].

(c) *Uniqueness.* Let Q1′ := [0, u_1′] × [0, v_1′] ⊂ Q1 with u_1′, v_1′ > 0. A class solution in the gauge through the
axes on Q1′ × S³ that induces the cone data on {0} × [0, v_1′] and on [0, u_1′] × {0}, and whose fields differ from the
background's by at most ε_2 in C^(k−4), equals the solution of (a) on Q1′ × S³.

(d) *Localisation.* If the data equal the background's on {0} × [0, v_K) and on [0, u_K) × {0}, where u_K, v_K > 0, the
solution equals the background, with its densities, at the points of Q1 × S³ with u < u_K and v < v_K. If the data
equal the background's at the points with ϑ < ϑ_a′, where ϑ_a′ ∈ (0, π/4], the solution equals the background at the
points of Q1 × S³ with ϑ < ϑ_a′ − 2C_* (uv)^(1/2); likewise, for ϑ_b′ ∈ [π/4, π/2), with ϑ > ϑ_b′ and ϑ > ϑ_b′ +
2C_* (uv)^(1/2).

Data with q_in = 0 and q_out = 0 are vacuum data, and their development is vacuum, the densities being transported. By
(b) and (c) the solution on Q1′ × S³ depends only on the data on the two edges of Q1′; in particular it does not depend
on how they are extended beyond u_1 and v_1 in the proof. For data that equal the background's near the axes,
[[thm:loc-cone-development]] gives a development on the set G_* of [[eq:loc-cone-domain]]; on every rectangle [0, u′] ×
[0, v′] ⊂ G_* it coincides with the solution of (a), by (c), its fields being within Cε of the background's in C^(k−4)
by [[thm:loc-cone-development]] (c). The theorem is proved at the end of [[sec:loc-axis-reduced]];
[[cor:loc-axis-cones]] applies it to the background of [[sec:bg-data]].

#### Cone data through the axes {#sec:loc-axis-data}

**Definition {#def:loc-axis-data}** (Fields smooth through the axes.) Let D be a set of the (u, v)-plane or one of the
edges N_o, N_i. Functions Ω > 0, γ_ϑ > 0, A_c, A_s and b of the points of D and of ϑ ∈ (0, π/2) are *smooth through the
axes* if the field of symmetric forms [[eq:loc-double-null]] that they define at the points of D × S³ off the axes extends
to a smooth field on D × S³. Since g(∂_u, ∂_v) = −2Ω², the restriction of g to the tangent spaces of the spheres is γ :=
γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2², and g(∂_u, X) = −γ(b∂_ϑ, X) for X tangent to the spheres, this holds exactly
when ln Ω extends to a smooth G-invariant function, γ to a smooth family over D of G-invariant Riemannian metrics on S³,
and b∂_ϑ to a smooth family of G-invariant vector fields on S³. We call ln Ω, γ and the vector field b∂_ϑ, which we also
write b, the *fields*. A density is smooth through the axes if it extends to a smooth G-invariant function. A *class
solution in the gauge through the axes* on D × S³, D ⊂ F, is a class solution in the gauge ([[sec:loc-cone-setting]])
whose fields are smooth through the axes, in place of being equal to the background's near the axes. *Cone data through
the axes*, of either sign, are defined as in [[def:loc-cone-data]], with (iii) there replaced by: their fields and
densities are smooth through the axes. The C^r norm of a field T on an edge is the supremum of |∂^i ∇̊^l T| over
i + l ≤ r, ∂ the derivative along the edge at a fixed point of S³ and ∇̊, |·| the Levi-Civita connection and the norm of
the unit round metric dΩ₃²; on a set D the derivatives in u and in v enter alike. The *size in C^r* of cone data through
the axes is the largest C^r norm, over the two edges, of the differences of their fields and densities from the
background's.

**Lemma {#lem:loc-axis-constraints}** (The constraints through the axes.) Let ln Ω, γ and b be fields on N_o smooth
through the axes, q_in a density smooth through the axes, dvol_1 the volume form of dΩ₃², and put

    χ := ½ ∂_vγ,      Y := (dvol_γ/dvol_1)^(1/3),      γ̂ := Y^(−2) γ,      W := ∂_v b.

(a) On N_o, with E := Ric(g) − q_in dv ⊗ dv − q_out du ⊗ du,

    E(∂_v, ∂_v) = −(3/Y)(∂_v²Y − 2 ∂_v ln Ω ∂_vY + (1/12) |∂_vγ̂|²_γ̂ Y) − q_in,
    E(∂_v, X) = (4Ω²)⁻¹ (γ(∂_vW, X) + (tr_γχ − 2 ∂_v ln Ω) γ(W, X) + 2χ(W, X)) + 𝔯(X),                {#eq:loc-axis-cone}

for X tangent to S³, where 𝔯 is the 1-form X ↦ E(∂_v, X) of the fields ln Ω, γ and 0 in place of b; 𝔯 is smooth and
G-invariant and depends only on Ω and γ on N_o. In the normalised gauge, on N_i, E(L̲, L̲) = E(∂_u, ∂_u) is given by the
first line with ∂_u, the fields of N_i and q_out in place of ∂_v, those of N_o and q_in.

(b) Let ln Ω, a smooth family γ̂ of G-invariant Riemannian metrics on S³ with dvol_γ̂ = dvol_1, and q_in ≥ 0 be given on
N_o ∩ {v ≤ v′}, smooth through the axes, together with smooth G-invariant functions Y_0 > 0 and Y_1 and G-invariant
vector fields b_0 and W_0 on S³. Let Y solve E(∂_v, ∂_v) = 0, which by (a) is a linear equation for Y, with Y = Y_0 and
∂_vY = Y_1 at v = 0. Then Y is smooth on N_o ∩ {v ≤ v′}; on every N_o ∩ {v ≤ v″} on which Y > 0, γ := Y²γ̂ and the
solution b of E(∂_v, ·) = 0 with b = b_0 and ∂_vb = W_0 at v = 0 are smooth through the axes, and ln Ω, γ, b and q_in
satisfy the constraints of (ii) of [[def:loc-cone-data]] on N_o. Every set of fields and densities smooth through the
axes that satisfies them arises in this way. The same holds on N_i in the normalised gauge, with the first line of (a)
only. In the coordinates, γ̂ = (sin ϑ cos ϑ)^(2/3)(e^(2ℓ_1) dϑ² + e^(2ℓ_2) dφ1² + e^(2ℓ_3) dφ2²) and Y = e^ϕ (sin ϑ
cos ϑ)^(−1/3), with ϕ and the ℓ_i of [[prop:loc-cones]] and [[lem:loc-cone-in]]: their free data are smooth through the
axes exactly when this γ̂ is a smooth metric on S³. For the background, γ̂ = dΩ₃² and Y = R_e.

(c) Let a background on Q1 with margin δ_1 be given, and cone data through the axes on {0} × [0, v_1] and [0, u_1] × {0},
in the normalised gauge, of size ε in C^(2p), p := m_0 + 3. For ε ≤ ε_0 they extend to cone data of either sign through
the axes on N_o and N_i, in the normalised gauge, of size at most Cε in C^(m_0); ε_0 and C depend only on k, u_1, v_1,
δ_1 and the background.

*Proof.* (a) Every term is a smooth G-invariant field on N_o, the fields being smooth and Y positive. Off the axes, in
the coordinates, dvol_γ = e^(ϰ_1 + ϰ_2 + ϰ_3) dϑ dφ1 dφ2 = e^(3ϕ) dϑ dφ1 dφ2 and dvol_1 = sin ϑ cos ϑ dϑ dφ1 dφ2, so Y and
γ̂ are those stated in (b); γ̂ is diagonal with the entries (sin ϑ cos ϑ)^(2/3) e^(2ℓ_i), so |∂_vγ̂|²_γ̂ = 4 Σ_i
(∂_vℓ_i)². The proof of [[prop:loc-cones]], which does not use that Ω is the background's, gives E(∂_v, ∂_v) = −3y″/y +
6 (ln Ω)′ y′/y − Σ_i (ℓ_i′)² − q_in with y := e^ϕ and ′ := ∂_v; as y = Y (sin ϑ cos ϑ)^(1/3), with a factor that does not
depend on v, y″/y = Y″/Y and y′/y = Y′/Y, which is the first line. With W = (∂_v b) ∂_ϑ and 𝒱 := γ_ϑ^(1/2) e^(A_c +
A_s), the second line of [[eq:loc-cone]] reads E(∂_v, ∂_ϑ) = (γ_ϑ/(4Ω²))(∂_v²b + ∂_v ln(γ_ϑ 𝒱 Ω⁻²) ∂_v b) + r, with r
of [[eq:loc-cone-r]], which does not contain b, so that r = 𝔯(∂_ϑ); and ∂_v ln 𝒱 = tr_γχ and γ_ϑ ∂_v ln γ_ϑ ∂_v b =
2χ(W, ∂_ϑ). This is the second line at X = ∂_ϑ; at X = K_i both sides vanish, by the reflection φ_i ↦ −φ_i, W being a
multiple of ∂_ϑ and χ diagonal. So both lines hold off the axes and, both sides being continuous, on N_o. On N_i, with
b = 0, E(∂_u, ∂_u) is the right side of [[eq:loc-cone-in]] minus q_out, the first line of [[eq:loc-cone]] with u in place
of v ([[lem:loc-cone-in]]), and the same calculation applies.

(b) The equation for Y is linear and of second order in v, with the coefficients −2∂_v ln Ω of ∂_vY and (1/3)((1/4)
|∂_vγ̂|²_γ̂ + q_in) of Y, smooth G-invariant functions on N_o ∩ {v ≤ v′}; so its solution with smooth G-invariant initial
values is smooth, by the smooth dependence of the solutions of linear ordinary differential equations on parameters, here
the point of S³, and G-invariant, by uniqueness. Where Y > 0, γ = Y²γ̂ is a smooth family of metrics, so χ and 𝔯 are
smooth, and the second line of (a) with E(∂_v, ·) = 0 is the linear equation ∂_vW = −(tr_γχ − 2∂_v ln Ω) W − 2γ⁻¹χ(W,
·) − 4Ω² γ⁻¹𝔯 for the vector field W along each generator, with smooth coefficients; its solution with W = W_0 at v = 0
is smooth and G-invariant, and so is b := b_0 + ∫_0^v W. By (a) the constraints hold. Conversely, fields satisfying the
constraints define Y, γ̂ and W as above, which solve these equations with their own initial values, and by uniqueness
they are the solutions. On N_i the same argument applies to the first line. The coordinate expressions were found in the
proof of (a); for the background γ = R_e² dΩ₃², whose volume form is R_e³ dvol_1.

(c) We extend the data on {0} × [0, v_1]; on [0, u_1] × {0} the same argument applies with u, q_out and the first line of
(a) only, b = 0 being kept. As in the proof of [[lem:loc-cone-extension]], for f each of ln Ω, γ̂ and q_in, with
background value f̊, let B_f be the Borel sum in t := v − v_1 of the v-derivatives at v = v_1 of f − f̊, G-invariant
fields on S³, with ε_j := δ_1/4 for j ≤ p and ε_j ≤ δ_1/4 for j > p so small that the j-th term has C^p norm at most
2^(−j) ε; put f̃ := f on [0, v_1] and f̃ := f̊ + B_f on [v_1, v_1 + 2δ_1]. Then f̃ is smooth and G-invariant, and, a term
of index j ≤ p having C^p norm at most C(p) ‖f − f̊‖_(C^(p+j)), ‖f̃ − f̊‖_(C^p) ≤ Cε. Replace the extended γ̃ by (dvol_1/
dvol_γ̃)^(2/3) γ̃, which has the volume form dvol_1, is unchanged on [0, v_1] and, for ε small, is a metric within Cε of
dΩ₃² in C^p. Solve the two equations of (b) on [0, v_1 + 2δ_1] with the values of the data at v = 0; by uniqueness the
solutions are the data on [0, v_1]. R_e and 0 solve the same equations with the background's coefficients; the
coefficients of the equation for Y differ from these by at most Cε in C^(p−1), and so do its initial values. By
Gronwall's inequality for the equation and for its derivatives along S³ (∇̊ commutes with ∂_v), the v-derivatives being
given by the equation, Y − R_e is at most Cε in C^(p−1) on the extended edge, so Y > 0 for ε small. Then the
coefficients of the equation for W are within Cε of the background's in C^(p−2) and 𝔯 is at most Cε in C^(p−3), and b is
at most Cε in C^(p−3) = C^(m_0). The extended functions satisfy (i) and (ii) of [[def:loc-cone-data]] and are smooth
through the axes; the extended q_in may be negative beyond v_1. ∎

**Lemma {#lem:loc-axis-jets}** (The formal solution through the axes.) Let a background be given on 𝒮 and cone data
through the axes, of either sign, on N_o and N_i.

(a) [[lem:loc-cone-borel]] holds with the interval Y replaced by S³, the functions a_j and b_k by G-invariant fields on S³
of one tensor type, with the C^r norms of [[def:loc-axis-data]], and f by a G-invariant field of that type; in its (a),
"at every ϑ" reads "at every point of S³".

(b) [[lem:loc-cone-jets]] holds, with these changes: its a_j and b_k are, at ϑ ∈ (0, π/2), those of its proof, and they
are the derivatives across N of fields and densities smooth through the axes; in (ii) the first statement reads: if the
data equal the background's at the points of a G-invariant open set of S³, so do all a_j and b_k; (iii) holds with the
C^r norms of fields; and (iv) holds for class solutions in the gauge through the axes.

(c) [[prop:loc-cone-formal]] holds, with Δ the difference of fields and densities smooth through the axes and Ĝ a smooth
G-invariant symmetric form on 𝒮 × S³ of the form [[eq:loc-double-null]], Lorentzian when the size is at most a number
depending on the background; in its (a), Δ vanishes at the points of every G-invariant open set of S³ at which all a_j
and b_k are the background's, in place of outside {ϑ_a′ ≤ ϑ ≤ ϑ_b′}, and ‖Δ‖_(C^(k+3)) is measured as in
[[def:loc-axis-data]].

*Proof.* (a) The proof of [[lem:loc-cone-borel]] uses of the variable ϑ only that the coefficients h_j of the Borel sums
are smooth functions of further variables with C^r norms; for G-invariant fields on S³ every term χ(x/ε_j) x^j h_j/j! is a
G-invariant field of the same type, the cut-offs depending on u and v only, and the estimates hold verbatim.

*The equations in fields.* For fields X = (ln Ω, γ, b) smooth through the axes and densities q_A on an open set of 𝒮, let
𝐄(X) consist of the restriction E|_(S³) of E := Ric(g) − q_in dv ⊗ dv − q_out du ⊗ du to the tangent vectors of the
spheres, of E(L̲, ∂_v), L̲ := ∂_u + b, and of the 1-form E(L̲, ·)|_(S³), and put 𝒞_in := L̲q_in + tr_γχ̲ q_in and 𝒞_out :=
∂_vq_out + tr_γχ q_out, with χ̲ := ½(∂_uγ + ℒ_bγ), ℒ_b the Lie derivative on S³. These are smooth G-invariant fields. Off
the axes the reflections reduce E|_(S³) to E(∂_ϑ, ∂_ϑ), E(K_1, K_1), E(K_2, K_2) and E(L̲, ·)|_(S³) to E(L̲, ∂_ϑ) dϑ, so
that 𝐄(X) = 0 is E′ = 0 of [[lem:loc-cone-ricci]] (c); and tr_γχ̲ = L̲ ln 𝒱 + ∂_ϑ b and tr_γχ = ∂_v ln 𝒱, so that 𝒞_in =
𝒱⁻¹(∂_u ρ_in + ∂_ϑ(b ρ_in)) and 𝒞_out = 𝒱⁻¹ ∂_v ρ_out, the conservation expressions of [[lem:loc-cone-jets]]. The
densities do not enter 𝐄, as T(L̲, ∂_v), T(L̲, ·)|_(S³) and T|_(S³) vanish.

*The principal parts.* In coordinates (u, v, θ¹, θ², θ³), with θ^a coordinates on an open set of S³, a metric of the
form [[eq:loc-double-null]] has g_vv = g_va = 0, g_uv = −2Ω², g_ab = γ_ab, g_ua = −γ_ab b^b, g_uu = γ_ab b^a b^b and
g^uu = g^ua = g^vv = 0, g^uv = −1/(2Ω²), g^va = b^a g^uv, g^ab = γ^ab, as the frame (L̲, ∂_v, ∂_a) is dual to (du, dv,
dθ^a − b^a du); and

    Ric_μν = −½ g^ρσ (∂_ρ∂_σ g_μν + ∂_μ∂_ν g_ρσ − ∂_ρ∂_μ g_σν − ∂_ρ∂_ν g_σμ) + Q_μν,

with Q_μν a polynomial in g_αβ, g^αβ and the first derivatives of g_αβ. In the linearisation of 𝐄 at X in the direction
δX = (δ ln Ω, δγ, δb), the second derivatives of δX come from the first part only, the frame and T holding no derivative
of the metric, and δg_vv = δg_va = 0. Collecting the terms with a derivative in u, and using g^vb = b^b g^uv, by which the
terms in ∂_u∂_vδγ of E(L̲, ·) cancel, one finds, up to terms with at most one derivative of δX,

    E(∂_a, ∂_b):   (2Ω²)⁻¹ ∂_u∂_vδγ_ab,
    E(L̲, ∂_v):    −2 ∂_u∂_vδ ln Ω − ½ γ^ab ∂_u∂_vδγ_ab,
    E(L̲, ∂_a):    −(4Ω²)⁻¹ γ_ab ∂_u∂_vδb^b + ½ γ^bc ∂_u∂_bδγ_ca − ½ γ^bc ∂_u∂_aδγ_bc − ∂_u∂_aδ ln Ω,
                                                                                                {#eq:loc-axis-principal}

and, collecting those with a derivative in v other than ∂_v² (the terms in ∂_v²δX enter E(L̲, ∂_v) only, through
∂_v²δg_uu and ∂_v²δg_ua, with no further derivative), up to terms with at most one derivative of δX,

    E(∂_a, ∂_b):   (2Ω²)⁻¹ (L̲∂_vδγ_ab + ½ (γ_ac ∂_b + γ_bc ∂_a) ∂_vδb^c),
    E(L̲, ∂_v):    −2 L̲∂_vδ ln Ω − ½ γ^ab L̲∂_vδγ_ab − ½ ∂_a∂_vδb^a,
    E(L̲, ∂_a):    −(4Ω²)⁻¹ γ_ab L̲∂_vδb^b,

with L̲ = ∂_u + b^c ∂_c applied to components; here the terms in ∂_v∂_cδγ and ∂_u∂_vδγ of E(L̲, ·) cancel in the same way.
Off the axes these are the second derivatives of [[eq:loc-cone-frame-ricci]].

*The derivatives across N_o.* Let j ≥ 1, and let a_0, …, a_(j−1) be the derivatives across N_o of fields and densities
smooth through the axes; by (a) there are such fields X♭ and densities q♭ with ∂_u^jX♭ = 0 and ∂_u^jq♭ = 0 on N_o. For
G-invariant fields Z = (Z_Ω, Z_γ, Z_b) on N_o, a function, a symmetric form and a vector field on the spheres, put
𝔏(Z) := ∂_u^(j−1) 𝐄(X♭ + u^jZ/j!) at u = 0. Ric is linear in the second derivatives of the metric, with coefficients in
g^αβ, and quadratic in the first, and each derivative of u^jZ/j! of order i holds the factor u^(j−i); so a term of
degree at least two in Z holds a factor u^(2j−2) and vanishes at u = 0 after ∂_u^(j−1) when j ≥ 2. For j = 1 such terms
are quadratic forms in the first u-derivatives Z, with smooth coefficients; off the axes they vanish for G-invariant Z,
since by (Ψ2) and (Ψ3) of the proof of [[lem:loc-cone-jets]] every term of E′ holds at most one factor among the first
u-derivatives of ln Ω, the ϰ_i and b, and the first u-derivatives at u = 0 of the class functions of X♭ + uZ are affine in
Z; so they vanish everywhere, by continuity. The terms linear in Z are ∂_u^(j−1) of L(u^jZ/j!) at u = 0, L =
c^μν∂_μ∂_ν + c^μ∂_μ + c the linearisation of 𝐄 at X♭, that is 2c^uv∂_vZ + 2c^ua∂_aZ + (c^u + (j − 1)∂_uc^uu)Z; by
[[eq:loc-axis-principal]],

    𝔏(Z) = 𝔏(0) + ((2Ω²)⁻¹ ∂_vZ_γ, −2 ∂_vZ_Ω − ½ tr_γ ∂_vZ_γ, −(4Ω²)⁻¹ γ(∂_vZ_b, ·)) + 𝔪(Z, ∇̊Z_Ω, ∇̊Z_γ),

with 𝔪 linear, with smooth G-invariant coefficients, its first two components free of ∇̊Z. So 𝔏(Z) = 0 is a linear
system of ordinary differential equations in v along the generators: for (Z_Ω, Z_γ), with the invertible coefficient
(Z_Ω, Z_γ) ↦ ((2Ω²)⁻¹ Z_γ, −2Z_Ω − ½ tr_γ Z_γ) of ∂_v, and then for Z_b, whose inhomogeneous term holds ∇̊Z_Ω and ∇̊Z_γ.
For the densities put Z_in := the solution of ∂_u^(j−1)𝒞_in = 0 at u = 0, in which ∂_u^jq_in enters with the factor 1
and nothing else of order j but Z_γ, and let Z_out solve ∂_u^j𝒞_out = 0 at u = 0, the linear equation ∂_vZ_out + tr_γχ
Z_out = (terms in a_0, …, a_(j−1) and Z) along the generators. We solve with the initial values at v = 0 the j-th
u-derivatives at the corner of the data on N_i; the coefficients and the initial values being smooth and G-invariant and
the system G-equivariant, the solution is smooth and G-invariant, and we take it as a_j. Off the axes a_j is the
derivative of the proof of [[lem:loc-cone-jets]]: both solve ∂_u^(j−1)E′ = 0 and the conservation equations, in class
functions and in fields respectively, with the same initial values, and those solutions are unique.

*The derivatives across N_i.* Likewise, with 𝔏′(Z) := ∂_v^(k−1) 𝐄(X♭ + v^kZ/k!) at v = 0 and the second list: the terms
in ∂_v² contribute only terms without derivatives of Z, and the third component of 𝔏′(Z) − 𝔏′(0) is −(4Ω²)⁻¹ γ(L̲Z_b, ·)
plus terms without derivatives of Z, the others being (2Ω²)⁻¹ L̲Z_γ and −2L̲Z_Ω − ½ tr_γ L̲Z_γ plus terms in Z and ∇̊Z_b.
So 𝔏′(Z) = 0 consists of transport equations along L̲, first for Z_b and then for (Z_Ω, Z_γ); Z_out solves ∂_v^(k−1)
𝒞_out = 0 at v = 0, algebraically, and Z_in solves ∂_v^k𝒞_in = 0, a transport along L̲. The generators of N_i, the
integral curves of L̲, start on S_c and cover N_i, b being a smooth vector field on S³. The initial values are the k-th
v-derivatives at the corner of the data on N_o. For k = 1 the quadratic terms vanish as before.

*The statements.* (i): off the axes it is (i) of [[lem:loc-cone-jets]], whose proof is local in ϑ; both sides are
continuous. (ii): the coefficients, inhomogeneous terms and initial values of the equations at a point of S³ are built
from the data and their derivatives at that point and from the derivatives along S³ of the solutions of order j there;
where the data equal the background's on a G-invariant open set, the background's derivatives solve the same equations
with the same initial values, and by uniqueness they are the solutions; the second statement is proved as there. (iii):
𝔏(0) holds derivatives of order at most two of a_0, …, a_(j−1), the equation for Z_b one derivative along S³ of (Z_Ω,
Z_γ), and the initial values j derivatives along N_i of the data, and likewise on N_i; the induction of the proof of (iii)
there gives the bound with the C^r norms of fields. (iv): such a solution satisfies 𝐄 = 0 and 𝒞_in = 𝒞_out = 0 near N in
F, hence, by continuity, their derivatives of every order on N, and its derivatives across N solve the equations above
with the same initial values.

(c) The proof of [[prop:loc-cone-formal]] applies, with (a) applied to the differences from the background's of the
fields and densities whose derivatives are the a_j and b_k. Ĝ is of the form [[eq:loc-double-null]] with fields smooth
through the axes, smooth by (a) and (b), and Lorentzian when γ̂ := γ_e + Δ_γ is positive definite and Ω̂ > 0, which holds
when ‖Δ‖_(C⁰) is small. The vanishing to infinite order on N of E and of the conservation expressions holds off the axes
by the proof there, which is local in ϑ, and on N by continuity of every derivative. The support of Δ is as stated, by
(ii) and the support property of (a). ∎

#### The sections of the cones are leaves {#sec:loc-axis-leaves}

*Leaves in a chart.* Let (t, x) be a chart on an open G-invariant set in which G acts on x ∈ ℝ⁴ ∖ {0} by its action on ℝ⁴,
and whose slices Σ_s := {t = s} are spacelike for the metrics considered. The constructions of [[sec:class-planar-shear]]
use of the chart of [[sec:background]] only these properties, through the slice, its future unit normal n, its second
fundamental form K_Σ, the totally geodesic M3 := Σ_s ∩ {φ1 = 0} near axis 2 and the coordinates (z, y) of
[[lem:class-leaf]]; we use them in such charts. Let V = (g, p_A, Θ_A, q_A) be a G-invariant state on Σ_s near a point p of
axis 2 with ρ1(p) > 0, at which the spatial part p_A^Σ of p_A satisfies p_A(∂_z) ≠ 0; p_A^Σ is tangent to M3 at the points
of M3, by invariance. Put

    H_L[V] := ± (Θ_A − κ_A1 + p_A(n) tr K_Σ|_Π)/|p_A^Σ|,      Π := the γ3-orthogonal complement of p_A^Σ in TM3,
                                                                                                    {#eq:loc-axis-hl}

the sign that of p_A(∂_z): the formula of step (1) of the proof of [[lem:class-planar-shear]], with Θ_A, p_A^Σ and p_A(n)
in place of Θ, ∇_Σu and n(u), and with the plane Π fixed by p_A. This is how H_L[Θ_A] of [[lem:class-leaf-differences]] is
read: a function of the point, as [[lem:class-volterra]] requires, which for a solution of the class system with p_A =
du_A equals that formula on each level set of u_A, Π being its tangent plane there. The *A-leaves* of V are the solutions
of [[eq:class-leaf-volterra]] with H_L := H_L[V] through the points of the axis, and σ_A[V] at a point is 2|p_A^Σ| σ_L −
p_A(n)(K_Σ(e_r, e_r) − K_Σ(e_2, e_2)) for the leaf through it, σ_L of [[eq:class-leaf-volterra]] and e_r the unit tangent
of the leaf in the meridional plane, which is [[eq:class-shear-leaf]] with p_A in place of du. For a solution of
[[eq:class-system]] with p_A = du_A and Θ_A = □_g u_A the leaves are the level sets of u_A in the slices, by the last
statement of [[lem:class-leaf-differences]], whose proof uses only these two properties, and σ_A is the planar shear of
those level sets. Near axis 1 the same holds with the two planes exchanged, κ_A2 in place of κ_A1.

**Lemma {#lem:loc-axis-leaf}** (The sections of the cones are leaves.) (i) Let t be a smooth function on a neighbourhood
of N with ∂_vt > 0 on N_o and ∂_ut > 0 on N_i. Then each level set {t = s} meets N_o in at most one sphere {(0, c)} × S³
and N_i in at most one sphere {(c′, 0)} × S³, spheres of the data's double-null coordinates, c and c′ increasing in s.
This holds for t = u + v and for every smooth function of (u, v) that increases with u and with v.

(ii) In a chart as above, let V be a state on Σ_s whose A-leaves through the points of the axis near p exist over a disc
𝔻_(2δ), and let S ⊂ Σ_s be a G-invariant hypersurface through a point of the axis near p such that S ∩ M3 is a graph z =
h_S(y) over 𝔻_(2δ) with h_S smooth. Then S ∩ M3 is the A-leaf of V through its point of the axis if and only if, along S
over 𝔻_(2δ), (a) p_A vanishes on TS and (b) Θ_A = θ_S, where θ_S := −Σ_α p_A(∇_(e_α) e_α) for a g-orthonormal frame
(e_α) of TS, the expansion of S along g⁻¹p_A computed with the metric of V.

(iii) If two states have the same p_A, Θ_A, metric and first derivatives of the metric at the points of S, then S ∩ M3 is
an A-leaf of one if and only if it is one of the other. For Ů and Û, in every chart as above in which the spheres
{(u, v)} × S³ meet M3 in such graphs and p_A(∂_z) ≠ 0, the spheres in Σ_s are the leaves of both families.

*Proof.* (i) t(0, v) is strictly increasing in v and t(u, 0) in u, so each takes the value s at most once.

(ii) Let F := z − h_S(y) and ν := ∇F/|∇F|, the unit normal of S in Σ_s; ν is G-invariant, hence tangent to M3 at the
points of M3, the fixed set of φ1 ↦ −φ1. For X, Y tangent to S, ∇_XY = ∇^S_XY − k(X, Y) ν + K_Σ(X, Y) n, with k(X, Y) :=
g(∇_Xν, Y), the second fundamental form of S in Σ_s; the last term is that of the proof of [[lem:class-gauss]] (a). At the
points of M3, TS is the orthogonal sum of TS ∩ TM3, the tangent space of Σ_S := S ∩ M3, and of ℝe_1, e_1 := K_1/|K_1|.
As K_1 is a Killing field and |K_1| is invariant, ∇_(e_1)e_1 = −½ |K_1|⁻² ∇g(K_1, K_1) = −∇ψ_1, so −p_A(∇_(e_1)e_1) =
g⁻¹(p_A, dψ_1) = κ_A1 for every invariant p_A. Assume (a). Then p_A(∇^S_XY) = 0, so −p_A(∇_XY) = p_A(ν) k(X, Y) − p_A(n)
K_Σ(X, Y); on TΣ_S, k is the second fundamental form of Σ_S in M3, M3 being totally geodesic and ν tangent to it. Taking
the trace over a g-orthonormal frame of TS adapted to this sum,

    θ_S = κ_A1 + p_A(ν) H_S − p_A(n) tr K_Σ|_(TΣ_S),

H_S the mean curvature of Σ_S in M3 for ν. By (a), p_A^Σ is conormal to S, so Π = TΣ_S along S and p_A^Σ = p_A(∂_z) dF,
since dF(∂_z) = 1; so p_A(ν) = ±|p_A^Σ| with the sign of p_A(∂_z). Comparing with [[eq:loc-axis-hl]], H_S = H_L[V]
along S exactly when Θ_A = θ_S. By [[lem:class-leaf]] (c), for every graph H_S = a_L h_S″ + (terms free of h_S″), and
E_L := rH_S/a_L − (rh_S′)′ is the function of (r, h_S, h_S′) of that lemma; and h_S′(0) = 0, h_S being smooth and
invariant. So if H_S = H_L[V], integrating (rh_S′)′ = rH_L[V]/a_L − E_L from 0 shows that h_S solves
[[eq:class-leaf-volterra]] with h_S(0) its point of the axis, and by the uniqueness in [[lem:class-volterra]] it is the
leaf of V there. Conversely, if Σ_S is the leaf, differentiating [[eq:class-leaf-volterra]] at r > 0, and by continuity at
r = 0, gives H_S = H_L[V] along it, and with (a), (b) follows.

(iii) The frame of TS and ∇_XY for X, Y tangent to S are determined by the metric and its first derivatives at the points
of S, so (a) and (b) involve only the quantities named. For Ů and Û, p_in = −dv and p_out = −du vanish on the tangent
spaces of the spheres. u and v are null for every metric of the form [[eq:loc-double-null]], so ∇²v(P, ·) = 0 by
[[prop:class-structure]] (b), and the tangent space of a sphere is a screen there: it is spacelike, orthogonal to P := Ĝ⁻¹
(−dv), which it does not contain, and so equal to {P, L̄}^⊥ for the null L̄ orthogonal to it with Ĝ(P, L̄) = −1. As v is
constant on the sphere, −p_in(∇_XX) = dv(∇_XX) = −∇²v(X, X) for X tangent to it, so θ_S = −tr_(TS)∇²v = □_Ĝ(−v) =
div_Ĝ P̂_in = Θ̂_in, and likewise for the outgoing family and for Ů. By (ii) the spheres are the leaves. ∎

**Lemma {#lem:loc-axis-shear}** (The planar shear on unions of arcs of leaves.) In a chart as above, let ů be a smooth
class solution near Σ_s, and let δ, the balls 𝔅 ⊂ 𝔅′ and C_L be those of [[lem:class-leaf-differences]] and
[[def:class-adapted]] for ů at a point p of axis 2 with ρ1(p) > 0, δ decreased so that 8C_Lδ ≤ 1 and the A-leaves of the
states of 𝔅′ through the points of the axis within 2δ of p are graphs over 𝔻_(2δ). Let U, U′ ∈ 𝔅′ be states on Σ_s, U
including ∂g among its components, and let O ⊂ Σ_s be a G-invariant open set, with boundary of measure zero, such that for
every x ∈ O ∩ 𝒰_δ(p) the arc of the A-leaf of U from its point on the axis to x lies in the closure of O. Then

    ‖σ_A[U] − σ_A[U′]‖_(L²(O∩𝒰_δ(p))) ≤ C ‖U − U′‖_(L²(O∩𝒰_(2δ)(p))),                                {#eq:loc-axis-shear}

with C depending only on 𝔅′, δ and the chart near p, and not on O. Near axis 1 the same holds with the planes exchanged.

For O the union of the leaves of U over 𝔻_δ through the points of the axis within δ/2 of p, a neighbourhood of the
points of 𝒰_(δ/4)(p), [[eq:loc-axis-shear]] is a bound of the kind of [[lem:class-leaf-differences]] (b); the proof below
is that bound written leaf by leaf.

*Proof.* (1) *The leaves.* For V ∈ 𝔅′ write h_V(z0, ·) for its A-leaf through (z0, 0), a function of r = |y| by
invariance, p_V := ∂_r h_V and q_V := p_V/r. By the proof of [[lem:class-volterra]], with G_V(r, z, p) := r H_L[V](z, r)/
a_L(r, z, p) − E_L(r, z, p), a_L and E_L those of [[lem:class-leaf]] (c) for the metric of V,

    r p_V(r) = ∫_0^r G_V(ρ, h_V(ρ), p_V(ρ)) dρ,      |∂_pG_V| ≤ C (r + |p|),      |p_V| ≤ C r,

and also |∂_zG_V| ≤ C (r + |p|), since by that proof E_L = (C3 r + A3 p) N_L²/det₂ − p + r B̃/a_L with B̃ smooth. These
constants hold the C¹ norms of H_L[V], which hold p_A, Θ_A and first derivatives of the metric, and the C² norms of γ3,
bounded on 𝔅′ by the Sobolev inequality of [[lem:sobolev]] at the order k − 4 ≥ 2. The map 𝒯 of that proof is C¹ in (p,
z0) and a contraction uniformly in z0, so z0 ↦ h_V(z0, ·) is C¹, and w := ∂_(z0)h_V solves r ∂_r w(r) = ∫_0^r (∂_zG_V w +
∂_pG_V ∂_r w) dρ with w(0) = 1. So |∂_r w| ≤ C r sup |w| on [0, 2δ] and |w − 1| ≤ C δ² sup |w|, and after decreasing δ,
w ∈ [1/2, 2] and |∂_(z0) q_V| = |∂_r w|/r ≤ C. Hence (z0, y) ↦ (h_V(z0, y), y), for |z0 − z(p)| < 3δ/2 and |y| < 2δ, is a
C¹ diffeomorphism onto a neighbourhood of 𝒰_δ(p) ∩ M3 contained in 𝒰_(2δ)(p), with Jacobian in [1/2, 2].

(2) *The leaf through a point.* σ_A[V](x) = 𝔖(x, V(x), q_V(z0, r)) for x = (h_V(z0, y), y), r = |y|, with 𝔖 smooth: by
[[eq:class-leaf-volterra]], σ_L = ½ H_L[V] − k_φ with k_φ = ν^r/r + ½ ν(log B3) and ν^r/r = −(C3 + A3 q_V)/(det₂^(1/2)
N_L), while N_L, ν and e_r hold h′ = r q_V, the metric and its first derivatives at x. For x ∈ 𝒰_δ(p) let z0 and z0′ be
the points of the axis of the leaves of U and of U′ through x. As h_U(z0, r) = z(x) = h_(U′)(z0′, r) and ∂_(z0)h_(U′) ≥
1/2, |z0 − z0′| ≤ 2|h_U(z0, r) − h_(U′)(z0, r)|, so with Δh := h_U(z0, ·) − h_(U′)(z0, ·) and Δq := q_U(z0, ·) −
q_(U′)(z0, ·),

    |σ_A[U](x) − σ_A[U′](x)| ≤ C (|U − U′|(x) + |Δq(r)| + |q_(U′)(z0, r) − q_(U′)(z0′, r)|) ≤ C (|U − U′|(x) + |Δq(r)| +
    |Δh(r)|).

(3) *Two leaves from one point of the axis.* Fix z0, put Δp := ∂_rΔh, and let w(ρ) be |U − U′| at the point (h_U(z0, ρ),
ρ) of the leaf of U. Subtracting the equations of (1),

    r Δp(r) = ∫_0^r [G_U(ρ, h_U, p_U) − G_(U′)(ρ, h_U, p_U)] + [G_(U′)(ρ, h_U, p_U) − G_(U′)(ρ, h_(U′), p_(U′))] dρ.

The second bracket is at most C(|Δh| + ρ |Δp|). In the first, (ρ, h_U(ρ)) is a point of the leaf of U; H_L[·] is a smooth
function of p_A, Θ_A, the metric and its first derivatives there, a_L one of γ3 there, and E_L, by the form in (1) and
|p| ≤ Cρ, differs for two metrics at the same (ρ, z, p) by at most Cρ times the difference of γ3 and its first
derivatives; so the first bracket is at most Cρ w(ρ). With |Δh(r)| ≤ ∫_0^r |Δp|, r |Δp(r)| ≤ C r ∫_0^r |Δp| + C ∫_0^r ρ
w(ρ) dρ, and Gronwall's inequality gives |Δp(r)| ≤ C(r 𝒜w(r) + ∫_0^r ρ 𝒜w(ρ) dρ), with 𝒜w(r) := r⁻² ∫_0^r ρ w(ρ) dρ the
average of [[prop:class-flat-model]] (b). So |Δq| ≤ C(𝒜w + R 𝒜(𝒜w)) and |Δh| ≤ C R² (𝒜(𝒜w) + 𝒜(R 𝒜(𝒜w))) on [0, R],
and as 𝒜 does not increase the L² norm of radial functions on the plane ([[prop:class-flat-model]] (b) at the order 0, by
density), and 𝒜f on [0, R] depends only on f there, for every R ≤ 2δ

    ‖Δq‖_(L²(𝔻_R)) + ‖Δh‖_(L²(𝔻_R)) ≤ C ‖w‖_(L²(𝔻_R)),

radial functions being read as functions on the disc 𝔻_R.

(4) *Integration.* For |z0 − z(p)| < 3δ/2 let R(z0) be the supremum of |y| over the points (h_U(z0, y), y) of O ∩
𝒰_δ(p), and 0 if there are none. By the hypothesis on O, the arc of the leaf of U from (z0, 0) to such a point lies in the
closure of O, so every (h_U(z0, y), y) with |y| < R(z0) lies there. The volume of Σ_s near M3 is comparable to the product
of that of M3 and the length 2πρ1 of the orbit of K_1, with ρ1 bounded above and below on 𝒰_(2δ)(p). By (2), (3) and the
change of variables of (1), first to (z0, y) and then back,

    ∫_(O∩𝒰_δ(p)) |σ_A[U] − σ_A[U′]|² ≤ C ∫_(O∩𝒰_δ(p)) |U − U′|² + C ∫ dz0 ∫_(𝔻_(R(z0))) w(z0, |y|)² dy
                                     ≤ C ∫_(O∩𝒰_(2δ)(p)) |U − U′|²,

the points (h_U(z0, y), y) with |y| < R(z0) lying in the closure of O ∩ 𝒰_(2δ)(p), whose boundary has measure zero. ∎
