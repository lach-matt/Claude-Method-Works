### Null shells along the leaves {#sec:loc-shells}

This section extends the developments of [[thm:loc-cone-development]] and [[thm:civp-large]] to cone data that carry
finitely many null shells: an atom m(ϑ) δ(v − c) in the density on 𝒞_out, or n(ϑ) δ(u − d) on 𝒞_in, with m and n smooth
in ϑ and supported in the band, the other data being smooth between the atoms. The development is continuous, smooth
between the leaves {v = c} and {u = d} through the atoms, and solves the Einstein–null-dust equations in the sense of
distributions, with a null shell along each such leaf ([[thm:loc-shells]]). Between the leaves it is a smooth
characteristic problem, solved by the smooth theorems; at a leaf the pieces are glued by junction conditions, which are
derived here from the metric [[eq:loc-double-null]] ([[prop:loc-shell-junction]]). Across an ingoing leaf the transverse
derivative ∂_v b of the shift must be continuous, and this holds on the whole leaf once it holds where the leaf meets
𝒞_out; the shell's density is the jump of −tr χ, and it is carried along the leaf by the conservation law of a null dust.
Across an outgoing leaf no condition arises. On the neighbourhood of the cones on which the development is constructed no
two shells cross. Where two shells cross, the null expansions obey a product rule, which for round metrics is a relation
between the masses of the four adjacent regions ([[prop:loc-shell-crossing]]).

*Leaves and cells.* Throughout, g0, Q1 = [0, u_1] × [0, v_1], the open set 𝒪 ⊃ Q1 and the band 0 < ϑ_a < ϑ_b < π/2 are
as in [[sec:civp-large]]: g0 is given, in the gauge [[eq:loc-double-null]], on 𝒪 × S³, and solves [[eq:two-dust-limit]]
at the points of 𝒪 with u, v ≥ 0. Fix numbers 0 < c_1 < ⋯ < c_p < v_1 and 0 < d_1 < ⋯ < d_q < u_1, where p, q ≥ 0, and
put c_0 := 0, c_(p+1) := v_1, d_0 := 0 and d_(q+1) := u_1. The sets {v = c_k} (1 ≤ k ≤ p) are the *ingoing leaves*,
the sets {u = d_j} (1 ≤ j ≤ q) the *outgoing leaves*, their intersections the *crossing spheres*, and the rectangles
Q_jk := [d_j, d_(j+1)] × [c_k, c_(k+1)] the *cells*; as in [[sec:loc-cone-setting]], points of the (u, v)-plane stand
for the corresponding spheres. Let D ⊂ Q1 be a past set. A function on D × S³, or off the axes on D × (0, π/2), is
*cellwise smooth* if its restriction to the intersection of that set with each cell is the restriction of a smooth
function on a neighbourhood of it; it then has one-sided values and one-sided derivatives of every order on the
leaves. At a point of an ingoing leaf {v = c_k} that is not on a crossing sphere, the *jump* of a cellwise smooth F is
[F] := F(c_k⁺) − F(c_k⁻), the difference of the values from the cells above and below; across an outgoing leaf {u = d_j},
[F] := F(d_j⁺) − F(d_j⁻). A continuous cellwise smooth F has the same restriction to a leaf from both sides, so its
derivatives along the leaf are continuous across it: [∂_u F] = [∂_ϑ F] = 0 across an ingoing leaf, [∂_v F] = [∂_ϑ F] = 0
across an outgoing one, and likewise for every derivative along the leaf.

A metric g on D × S³ is *continuous and cellwise smooth* if it is a continuous G-invariant Lorentzian metric whose
restriction to the intersection of D × S³ with each cell is the restriction of a smooth G-invariant Lorentzian metric on
a neighbourhood of it, and which off the axes has the form [[eq:loc-double-null]] with Ω > 0, γ_ϑ > 0, b, A_c and A_s
continuous and cellwise smooth. A *class solution in the gauge* is one in the sense of [[sec:loc-cone-setting]], with the
corner at S and g0 as the background, as in [[sec:civp-large]]; its functions equal g0's near the axes. A *class solution
in double-null form* on D × S³ is a smooth class solution of [[eq:class-system]] with two families, phases v and u and
densities q_in and q_out, whose metric has the form [[eq:loc-double-null]] with Ω, γ_ϑ, b, A_c, A_s smooth functions of
(u, v, ϑ) ∈ D × (0, π/2): a class solution in the gauge without the condition near the axes. Its metric is smooth on
D × S³, the axes included, but need not equal g0 near them. Charts (u, v, y), with y = (y¹, y², y³) a chart of S³, cover
D × S³, the axes included. In such a chart the components of g are continuous with locally bounded first derivatives, and
its Christoffel symbols Γ^a_bc are locally bounded and cellwise smooth. Its *Ricci tensor in the sense of distributions*
is, in the chart,

    Ric(g)_bd := ∂_aΓ^a_bd − ∂_dΓ^a_ab + Γ^a_ae Γ^e_bd − Γ^a_de Γ^e_ab,

the derivatives being taken in the sense of distributions on the chart's domain and the products, which are bounded
functions, pointwise. For a number c, δ(v − c) is the distribution φ ↦ ∫ φ(u, c, y) du d³y of the chart, and for a
bounded function F on {v = c}, F δ(v − c) is φ ↦ ∫ F φ(u, c, y) du d³y; likewise δ(u − d).

**Definition {#def:loc-shell-solution}** (Solutions with null shells along the leaves.) Let D ⊂ Q1 be a past set. A
*solution with null shells along the leaves* on D × S³ consists of a continuous and cellwise smooth metric g, the phases
v and u, cellwise smooth densities q_in ≥ 0 and q_out ≥ 0, and *shell densities*: continuous functions 𝔪_k ≥ 0 on
(D ∩ {v = c_k}) × S³ (1 ≤ k ≤ p) and 𝔫_j ≥ 0 on (D ∩ {u = d_j}) × S³ (1 ≤ j ≤ q), smooth on the parts of these sets
between consecutive crossing spheres, all of them invariant under G, such that in every chart (u, v, y), on the interior
of D × S³ and in the sense of distributions,

    Ric(g) = q_in^♯ dv ⊗ dv + q_out^♯ du ⊗ du,      q_in^♯ := q_in + Σ_k 𝔪_k δ(v − c_k),
                                                     q_out^♯ := q_out + Σ_j 𝔫_j δ(u − d_j),  {#eq:loc-shell-einstein}

    ∂_a(|det g|^(1/2) q_in^♯ g^(ab) ∂_b v) = 0,      ∂_a(|det g|^(1/2) q_out^♯ g^(ab) ∂_b u) = 0.  {#eq:loc-shell-dust}

In such a chart g^(vv) = g⁻¹(dv, dv) = 0 and g^(uu) = 0, so the first field |det g|^(1/2) g^(ab) ∂_b v has no
∂_v-component and the second no ∂_u-component, and the products with δ(v − c_k) and δ(u − d_j) in [[eq:loc-shell-dust]]
are products of continuous functions with these distributions. The solution *induces* the functions Ω, γ_ϑ, b, A_c, A_s
and q_in of its restriction to 𝒞_out ∩ D, and Ω, γ_ϑ, b, A_c, A_s and q_out of its restriction to 𝒞_in ∩ D, the densities
being one-sided at the leaves.

Away from the leaves [[eq:loc-shell-einstein]] and [[eq:loc-shell-dust]] are the class system [[eq:class-system]] with
the two families of [[sec:loc-cone-setting]]. So on the interior of each cell (g, v, u, q_in, q_out) is a class solution
in double-null form, and by continuity its equations hold on each closed cell for the one-sided values. When p = q = 0 a
solution with null shells is a class solution in double-null form, and a class solution in the gauge if it equals g0 near
the axes.

**Lemma {#lem:loc-shell-ricci}** (The curvature of a continuous, cellwise smooth metric.) Let g be continuous and
cellwise smooth on D × S³, and let Ric_c(g) be its Ricci tensor on each cell, a locally bounded cellwise smooth tensor.

(a) In every chart (u, v, y), on the interior of D × S³,

    Ric(g) = Ric_c(g) + Σ_k 𝔖_k δ(v − c_k) + Σ_j 𝔖′_j δ(u − d_j),
    𝔖_k := ½ (dv ⊗ Y + Y ⊗ dv) − ½ (tr_g h) dv ⊗ dv,      h := [∂_v g_ab] dx^a ⊗ dx^b,      Y := h(g⁻¹dv, ·),
                                                                                                {#eq:loc-shell-singular}

with the jumps across {v = c_k}, and with 𝔖′_j given by the same formula with u and the jumps across {u = d_j} in place
of v and the jumps across {v = c_k}.

(b) Off the axes, in the coordinates (u, v, ϑ, φ1, φ2), with tr χ and tr χ̲ of [[eq:loc-cone-quantities]],

    𝔖_k = −[tr χ] dv ⊗ dv + (γ_ϑ [∂_v b]/(4Ω²)) (dv ⊗ (dϑ − b du) + (dϑ − b du) ⊗ dv),      𝔖′_j = −[tr χ̲] du ⊗ du.

So 𝔖′_j involves no jump of ∂_u b, and neither 𝔖_k nor 𝔖′_j involves the jumps of the derivatives of ln Ω or of the
ϰ_i − ϕ, ϕ := (ϰ_1 + ϰ_2 + ϰ_3)/3; tr χ = 3 ∂_vϕ, and tr χ̲ = 3 ∂_uϕ where b vanishes identically, as on 𝒞_in.

*Proof.* (a) Let F be bounded and cellwise smooth on the domain of the chart and φ a test function supported in the
interior of D × S³. For fixed (u, y) the points of D with these coordinates form an interval in v, since D is a past set,
and the numbers c_k cut it into intervals on each of which v ↦ F is smooth with one-sided limits. Integrating by parts on
each of them, and using Fubini's theorem,

    ∫ F ∂_vφ du dv d³y = −∫ {∂_vF} φ du dv d³y − Σ_k ∫ [F] φ(u, c_k, y) du d³y,

{∂_vF} denoting the cellwise derivative; the boundary of D does not enter, as φ vanishes near it, and the crossing
spheres, where [F] is not defined, have measure zero in the leaves. So ∂_vF = {∂_vF} + Σ_k [F] δ(v − c_k); likewise
∂_uF = {∂_uF} + Σ_j [F] δ(u − d_j), and ∂F/∂y^A = {∂F/∂y^A}, F being smooth in y on each cell. We apply this to the
Γ^a_bd. On {v = c_k}, g is continuous and its derivatives along the leaf are continuous across it, so [∂_e g_ab] = δ^v_e
h_ab and

    [Γ^a_bd] = ½ g^(ae) (δ^v_b h_ed + δ^v_d h_eb − δ^v_e h_bd).

With Y_d = g^(ve) h_ed and g^(vv) = 0, [Γ^v_bd] = ½ (δ^v_b Y_d + δ^v_d Y_b), and [Γ^a_ab] = ½ (Y_b + δ^v_b tr_g
h − Y_b) = ½ δ^v_b tr_g h. So the coefficient of δ(v − c_k) in Ric(g)_bd is [Γ^v_bd] − δ^v_d [Γ^a_ab] = (𝔖_k)_bd. The
products of the Christoffel symbols are bounded and equal their cellwise values off the leaves, a set of measure zero.
The outgoing leaves are treated in the same way, with g^(uu) = 0.

(b) The functions Ω, γ_ϑ, b and e^(ϰ_i) are continuous, so the nonzero components of h are

    h_uv = −4Ω² [∂_v ln Ω],   h_uu = b² [∂_vγ_ϑ] + 2γ_ϑ b [∂_v b],   h_uϑ = −b [∂_vγ_ϑ] − γ_ϑ [∂_v b],
    h_ϑϑ = [∂_vγ_ϑ],   h_(φiφi) = 2 e^(2ϰ_(i+1)) [∂_vϰ_(i+1)].

By the inverse metric of the proof of [[lem:loc-cone-equations]], g⁻¹dv = −(2Ω²)⁻¹ L̲, L̲ = ∂_u + b∂_ϑ, so Y_d = −(2Ω²)⁻¹
(h_ud + b h_ϑd): Y_u = −(2Ω²)⁻¹ γ_ϑ b [∂_v b], Y_v = 2[∂_v ln Ω], Y_ϑ = (2Ω²)⁻¹ γ_ϑ [∂_v b] and Y_(φi) = 0, that is

    Y = 2 [∂_v ln Ω] dv + (γ_ϑ [∂_v b]/(2Ω²)) (dϑ − b du).

Since g^(ab) ∂_v g_ab = ∂_v ln |det g| on each side and |det g|^(1/2) = 2Ω²𝒱 ([[lem:loc-cone-ricci]] (b)), with ∂_v ln
𝒱 = tr χ, tr_g h = [∂_v ln |det g|] = 4[∂_v ln Ω] + 2[tr χ]. Substituting in [[eq:loc-shell-singular]] gives 𝔖_k. Across
an outgoing leaf, h′ := [∂_u g_ab] dx^a ⊗ dx^b has h′(∂_v, ∂_d) = 0 for d ≠ u and h′_vu = −4Ω² [∂_u ln Ω], and
g⁻¹du = −(2Ω²)⁻¹ ∂_v; so Y′ := h′(g⁻¹du, ·) = 2[∂_u ln Ω] du and tr_g h′ = 4[∂_u ln Ω] + 2[∂_u ln 𝒱], and 𝔖′_j = −[∂_u ln
𝒱] du ⊗ du. Finally ∂_u ln 𝒱 = L̲ ln 𝒱 − b ∂_ϑ ln 𝒱 = tr χ̲ − ∂_ϑ b − b ∂_ϑ ln 𝒱, and ∂_ϑ b and b ∂_ϑ ln 𝒱 are continuous
across {u = d_j}; so [∂_u ln 𝒱] = [tr χ̲]. ∎

The next two identities are read off from [[eq:loc-cone-frame-ricci]].

**Lemma {#lem:loc-shell-identities}** (Two identities.) Let g have the form [[eq:loc-double-null]] off the axes, with
smooth functions, and let L̲, 𝒱, ϖ, χ_i, χ̲_i, tr χ and tr χ̲ be as in [[eq:loc-cone-quantities]] and K_i = ∂_(φi). Then

    Ric(L̲, ∂_ϑ) = −(γ_ϑ/(4Ω²)) (L̲∂_v b + (L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) + 2∂_ϑ b) ∂_v b) + r̲,

with r̲ of [[eq:loc-cone-frame-ricci]], and

    γ_ϑ⁻¹ Ric(∂_ϑ, ∂_ϑ) + Σ_(i=1,2) e^(−2ϰ_(i+1)) Ric(K_i, K_i)
        = (Ω²𝒱)⁻¹ (L̲∂_v𝒱 + (∂_ϑ b) ∂_v𝒱 + ½ ∂_ϑ(𝒱 ∂_v b)) − (γ_ϑ/(8Ω⁴)) (∂_v b)² + 𝔞,  {#eq:loc-shell-trace}

    𝔞 := −γ_ϑ⁻¹ Σ_(i=2,3) (∂_ϑ²ϰ_i + (∂_ϑϰ_i)² − ∂_ϑϰ_1 ∂_ϑϰ_i) − 2γ_ϑ⁻¹ (∂_ϑϖ + ϖ² − ∂_ϑϰ_1 ϖ)
          − (Ω²𝒱)⁻¹ Σ_(i=2,3) ∂_ϑ(Ω²𝒱 γ_ϑ⁻¹ ∂_ϑϰ_i).

The function r̲ contains derivatives of Ω, γ_ϑ, b, A_c, A_s only along L̲ and ∂_ϑ, and 𝔞 only along ∂_ϑ. For a round
metric (b = 0, γ_ϑ = R², e^(A_c) = R cos ϑ, e^(A_s) = R sin ϑ, Ω² = e^(2σ)/2) both sides of [[eq:loc-shell-trace]] equal
(6e^(−2σ)/R²)(R R_uv + 2R_u R_v + e^(2σ)), the trace of the angular components of [[lem:two-dust-equations]].

*Proof.* Take q_in = q_out = 0 in [[lem:loc-cone-ricci]], so that E = Ric there. The first identity is the formula for
E(L̲, ∂_ϑ) in [[eq:loc-cone-frame-ricci]]; r̲ is built from ϖ = ∂_ϑ ln Ω, the ∂_ϑϰ_i, the χ̲_i, ∂_ϑL̲ ln Ω and the
∂_ϑχ̲_i, and χ̲_1 = L̲ϰ_1 + ∂_ϑ b, χ̲_i = L̲ϰ_i for i = 2, 3. For the second, [[eq:loc-cone-frame-ricci]] gives, for
i = 1, 2, since ∂_vL̲ϰ_(i+1) = ∂_vχ̲_(i+1),

    e^(−2ϰ_(i+1)) Ric(K_i, K_i) = −□_g ϰ_(i+1) = Ω⁻² (∂_vχ̲_(i+1) + ½ (tr χ̲ χ_(i+1) + tr χ χ̲_(i+1) − ∂_v b ∂_ϑϰ_(i+1)))
                                   − (Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 γ_ϑ⁻¹ ∂_ϑϰ_(i+1)),

and γ_ϑ⁻¹ Ric(∂_ϑ, ∂_ϑ) is Ω⁻² (∂_vχ̲_1 + ½ (tr χ χ̲_1 + χ_1 tr χ̲) − ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b)) − (γ_ϑ/(8Ω⁴))(∂_v
b)² plus the first two terms of 𝔞. In the sum, ½ (tr χ χ̲_1 + χ_1 tr χ̲) + ½ Σ_(i=2,3) (tr χ̲ χ_i + tr χ χ̲_i) = tr χ tr
χ̲ and e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b) + ∂_v b ∂_ϑ(ϰ_2 + ϰ_3) = 𝒱⁻¹ ∂_ϑ(𝒱 ∂_v b), so the left side of [[eq:loc-shell-trace]]
is Ω⁻² (∂_v tr χ̲ + tr χ tr χ̲ − ½ 𝒱⁻¹ ∂_ϑ(𝒱 ∂_v b)) − (γ_ϑ/(8Ω⁴))(∂_v b)² + 𝔞. Since ∂_v𝒱 = 𝒱 tr χ, 𝒱 tr χ̲ = L̲𝒱 + 𝒱
∂_ϑ b, and ∂_vL̲ = L̲∂_v + (∂_v b) ∂_ϑ as operators,

    𝒱 (∂_v tr χ̲ + tr χ tr χ̲) = ∂_v(𝒱 tr χ̲) = L̲∂_v𝒱 + (∂_v b) ∂_ϑ𝒱 + (∂_ϑ b) ∂_v𝒱 + 𝒱 ∂_ϑ∂_v b
                             = L̲∂_v𝒱 + (∂_ϑ b) ∂_v𝒱 + ∂_ϑ(𝒱 ∂_v b),

which gives [[eq:loc-shell-trace]]. For a round metric ϖ = 0, ∂_ϑϰ_1 = 0, ∂_ϑϰ_2 = −tan ϑ, ∂_ϑϰ_3 = cot ϑ and
Ω²𝒱γ_ϑ⁻¹ = Ω²R sin ϑ cos ϑ, so the first sum in 𝔞 is (tan²ϑ − sec²ϑ) + (cot²ϑ − csc²ϑ) = −2 and the last one is R⁻² (sin
ϑ cos ϑ)⁻¹ ∂_ϑ(cos²ϑ − sin²ϑ) = −4R⁻², and 𝔞 = 6/R²; with 𝒱 = R³ sin ϑ cos ϑ, (Ω²𝒱)⁻¹
∂_u∂_v𝒱 = 2e^(−2σ)(R³)_uv/R³ = (6e^(−2σ)/R²)(R R_uv + 2R_u R_v). The left side is R⁻² times the trace over the unit
sphere of the angular components, which [[lem:two-dust-equations]] gives as the same expression. ∎

**Proposition {#prop:loc-shell-junction}** (The junction conditions.) Let D ⊂ Q1 be a past set, g a continuous
and cellwise smooth metric on D × S³ and q_in, q_out ≥ 0 cellwise smooth functions, such that on each closed cell
(g, v, u, q_in, q_out) is a class solution in double-null form. Then the following hold off the axes and off the crossing
spheres.

(a) *The torsion jump.* On each ingoing leaf,

    L̲ [∂_v b] + (L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) + 2∂_ϑ b) [∂_v b] = 0,  {#eq:loc-shell-torsion}

and [∂_v b] is continuous at the crossing spheres. So [∂_v b] vanishes along each integral curve of L̲ in the leaf that
starts at a point of {(0, c_k)} × S³ where it vanishes; when b vanishes near the axes, these curves fill the leaf off the
axes.

(b) *An ingoing shell.* If [∂_v b] = 0 on {v = c_k}, then there

    ∂_u(𝒱 [tr χ]) + ∂_ϑ(b 𝒱 [tr χ]) = 0,  {#eq:loc-shell-conservation}

and 𝒱[tr χ] is continuous at the crossing spheres; so [tr χ] keeps its sign along each integral curve of L̲ in the leaf.

(c) *An outgoing shell.* On each outgoing leaf ∂_v(𝒱 [tr χ̲]) = 0, and 𝒱[tr χ̲] is continuous at the crossing spheres; so
[tr χ̲] keeps its sign along each generator of the leaf.

(d) *The junction.* Let 𝔪_k and 𝔫_j be shell densities as in [[def:loc-shell-solution]]. Then (g, v, u, q_in, q_out, 𝔪_k,
𝔫_j) is a solution with null shells along the leaves on D × S³ if and only if, off the axes and off the crossing spheres:

(J1) [∂_v b] = 0 on every ingoing leaf;

(J2) 𝔪_k = −[tr χ] on {v = c_k} and 𝔫_j = −[tr χ̲] on {u = d_j};

(J3) [q_out] = 0 across every ingoing leaf and [q_in] = 0 across every outgoing leaf.

No condition is placed on the jumps of ∂_u b across an outgoing leaf, of the derivatives of ln Ω, or of the derivatives
of the ϰ_i − ϕ.

*Proof.* (a) Off the leaves Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, and dv and du vanish on ∂_ϑ; so on each closed cell
Ric(L̲, ∂_ϑ) = 0 for the one-sided values. In the first identity of [[lem:loc-shell-identities]], the coefficient of ∂_v
b and r̲ contain only b, which is continuous, and derivatives along L̲ and ∂_ϑ, which are tangent to {v = c_k}; so they
are continuous across the leaf, and [L̲∂_v b] = L̲[∂_v b]. The jump of the identity is [[eq:loc-shell-torsion]]. At a
crossing sphere {(d_j, c_k)} × S³, ∂_v b is a derivative along {u = d_j}, so above the leaf {v = c_k} its values from
u < d_j and from u > d_j agree on {u = d_j}, and likewise below; hence the jump across {v = c_k} has the same limits from
u < d_j and from u > d_j. Along an integral curve of L̲ in the leaf, [[eq:loc-shell-torsion]] is a linear homogeneous
ordinary differential equation for [∂_v b] whose coefficients are locally bounded along the curve and continuous off the
crossing spheres, at which [∂_v b] is continuous; so [∂_v b] vanishes along the curve if it vanishes at its starting
point. When b vanishes near the axes, the integral curves of L̲ = ∂_u + b ∂_ϑ in the leaf, the
solutions of dϑ/du = b(u, c_k, ϑ), b being bounded, continuous and smooth in ϑ, are defined for all u in the leaf, do not
reach the axes, and through every point of the leaf off the axes passes one of them that starts at u = 0.

(b) By [[eq:loc-shell-einstein]] off the leaves, Ric(∂_ϑ, ∂_ϑ) = Ric(K_i, K_i) = 0 on each closed cell, so the left side
of [[eq:loc-shell-trace]] vanishes on both sides of {v = c_k}. On its right side Ω²𝒱 and 𝔞 are continuous across the
leaf, 𝔞 containing only derivatives along ∂_ϑ; [L̲∂_v𝒱] = L̲[∂_v𝒱] and [(∂_ϑ b) ∂_v𝒱] = (∂_ϑ b)[∂_v𝒱]; [∂_ϑ(𝒱 ∂_v
b)] = ∂_ϑ(𝒱[∂_v b]) = 0; and [(∂_v b)²] = [∂_v b](∂_v b(c_k⁺) + ∂_v b(c_k⁻)) = 0. So L̲[∂_v𝒱] + (∂_ϑ b)[∂_v𝒱] = 0, which
is [[eq:loc-shell-conservation]], as [∂_v𝒱] = 𝒱[tr χ] and L̲F + (∂_ϑ b)F = ∂_uF + ∂_ϑ(bF). At a crossing sphere, ∂_v𝒱 is
a derivative along {u = d_j}, and the continuity follows as in (a). Along an integral curve of L̲, L̲(𝒱[tr χ]) = −(∂_ϑ b)
𝒱[tr χ], so 𝒱[tr χ] keeps its sign, and 𝒱 > 0.

(c) Since L̲F + (∂_ϑ b)F = ∂_uF + ∂_ϑ(bF), [[eq:loc-shell-trace]] with vanishing left side gives on each closed cell

    ∂_v∂_u𝒱 = −∂_ϑ(b ∂_v𝒱) − ½ ∂_ϑ(𝒱 ∂_v b) + (γ_ϑ 𝒱/(8Ω²)) (∂_v b)² − Ω²𝒱 𝔞.

The right side contains Ω, γ_ϑ, b, 𝒱 and derivatives along ∂_v and ∂_ϑ only, which are tangent to {u = d_j}; so it is
continuous across the leaf, and ∂_v[∂_u𝒱] = [∂_v∂_u𝒱] = 0. By the end of the proof of [[lem:loc-shell-ricci]] (b),
[∂_u𝒱] = 𝒱[∂_u ln 𝒱] = 𝒱[tr χ̲]. At a crossing sphere, ∂_u𝒱 = L̲𝒱 − b ∂_ϑ𝒱 is built from derivatives along {v = c_k}, so
it is continuous across that leaf, and the continuity follows as in (a).

(d) By [[lem:loc-shell-ricci]] (a), in a chart (u, v, y), since Ric_c(g) = q_in dv ⊗ dv + q_out du ⊗ du on each cell,

    Ric(g) − q_in^♯ dv ⊗ dv − q_out^♯ du ⊗ du = Σ_k (𝔖_k − 𝔪_k dv ⊗ dv) δ(v − c_k) + Σ_j (𝔖′_j − 𝔫_j du ⊗ du) δ(u − d_j).

The coefficients are bounded functions on the leaves, continuous off the crossing spheres; testing with functions
supported near a point of one leaf off the others shows that the sum vanishes if and only if every coefficient vanishes
off the crossing spheres. On each part of a leaf between crossing spheres the coefficients are continuous up to the axes,
so it suffices that they vanish off the axes, where [[lem:loc-shell-ricci]] (b) applies: since γ_ϑ/(4Ω²) ≠ 0 and
dv ⊗ (dϑ − b du) + (dϑ − b du) ⊗ dv is not a multiple of dv ⊗ dv, 𝔖_k = 𝔪_k dv ⊗ dv if and only if [∂_v b] = 0 and
𝔪_k = −[tr χ], and 𝔖′_j = 𝔫_j du ⊗ du if and only if 𝔫_j = −[tr χ̲]. So [[eq:loc-shell-einstein]] holds if and only if
(J1) and (J2) do.

For [[eq:loc-shell-dust]], let X^a := |det g|^(1/2) g^(av), a continuous and cellwise smooth vector density with X^v = 0.
By the rule for derivatives in the proof of [[lem:loc-shell-ricci]] (a), applied to X^a q_in and, on the leaf {v = c_k},
to X^a 𝔪_k as a function of (u, y),

    ∂_a(X^a q_in^♯) = {∂_a(X^a q_in)} + Σ_j [X^u q_in] δ(u − d_j)
                      + Σ_k ({∂_u(X^u 𝔪_k) + ∂_A(X^A 𝔪_k)} + Σ_j [X^u 𝔪_k] δ(u − d_j)) δ(v − c_k),

the last jump being taken along the leaf at u = d_j; no term at the ingoing leaves comes from the first part, as X^v = 0.
The cellwise term vanishes by the conservation law on each cell. So the first equation of [[eq:loc-shell-dust]] holds if
and only if [X^u q_in] = 0 across every outgoing leaf, ∂_u(X^u 𝔪_k) + ∂_A(X^A 𝔪_k) = 0 on the parts of the ingoing leaves
between crossing spheres, and X^u 𝔪_k is continuous at the crossing spheres. The divergence of a vector density along the
leaf does not depend on the chart, the functions involved are continuous up to the axes on the parts of the leaves, and
X^u = |det g|^(1/2) g^(uv) ≠ 0 is continuous; off the axes, in the coordinates (u, v, ϑ, φ1, φ2), X = −𝒱 ∂_u − b𝒱 ∂_ϑ
([[lem:loc-cone-ricci]] (b)). So these conditions are [q_in] = 0 across the outgoing leaves, ∂_u(𝒱𝔪_k) + ∂_ϑ(b𝒱𝔪_k) = 0
off the axes, and the continuity of 𝒱𝔪_k at the crossing spheres; given (J1) and (J2), the last two are (b). In the same
way, with X′^a := |det g|^(1/2) g^(au), which off the axes is −𝒱 δ^a_v, the second equation of [[eq:loc-shell-dust]]
holds if and only if [q_out] = 0 across the ingoing leaves, ∂_v(𝒱𝔫_j) = 0 and 𝒱𝔫_j is continuous at the crossing spheres,
and given (J2) the last two are (c). Hence [[eq:loc-shell-einstein]] and [[eq:loc-shell-dust]] hold if and only if
(J1)–(J3) do. ∎

**Remark {#rem:loc-shell-poisson}** (Null shells in four dimensions.) In four dimensions, Poisson's reformulation of the
null-shell formalism of Barrabès and Israel associates with the δ-part of the curvature of a metric that is continuous
across a null hypersurface a surface stress-energy tensor, formed from the δ-part of the Einstein tensor, and gives it
"a simple characterization in terms of a mass density, a mass current, and an isotropic pressure" [Poi02, p. 1]:
"S^(αβ) = μk^α k^β + j^A (k^α e^β_A + e^α_A k^β) + p σ^(AB) e^α_A e^β_B" [Poi02, (2.15), p. 4], k tangent to the null
generators. [[lem:loc-shell-ricci]] is the analogue in five dimensions and in the gauge of the class, proved directly.
By its part (b), 𝔖_k and 𝔖′_j are trace-free, as g⁻¹(dv, dv) = g⁻¹(du, du) = g⁻¹(dv, dϑ − b du) = 0, so they are also
the δ-parts of the Einstein tensor. On an ingoing leaf, whose generators are tangent to L̲ = −2Ω² g⁻¹dv, the term in
dv ⊗ dv is the density, the term in [∂_v b] the current, and no pressure term occurs; a null-dust shell, whose stress is
a multiple of dv ⊗ dv, is the case of zero current, (J1). A jump of the derivatives of the ϰ_i − ϕ across a leaf
produces no δ in Ric; in four dimensions such a jump gives a δ in the Weyl tensor, which [Poi02, p. 1] interprets as "an
independent impulsive tidal wave". No proof here uses [Poi02].

**Definition {#def:loc-shell-data}** (Cone data with shells.) *Cone data with shells along the leaves* consist of
functions Ω > 0, γ_ϑ > 0, b, A_c and A_s of (v, ϑ) ∈ [0, v_1] × (0, π/2) on 𝒞_out, continuous and smooth on each [c_k,
c_(k+1)] × (0, π/2), a density q_in ≥ 0 smooth on each of these sets and smooth functions m_k ≥ 0 of ϑ (1 ≤ k ≤ p), and
of functions Ω > 0, γ_ϑ > 0, A_c and A_s of (u, ϑ) ∈ [0, u_1] × (0, π/2) on 𝒞_in, with b = 0 there, continuous and smooth
on each [d_j, d_(j+1)] × (0, π/2), a density q_out ≥ 0 smooth on each of these sets and smooth functions n_j ≥ 0 of ϑ
(1 ≤ j ≤ q), such that:

(i) the two sets of functions agree on S;

(ii) on each [c_k, c_(k+1)] the functions on 𝒞_out satisfy Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0, by
[[eq:loc-cone]], and at each c_k, [∂_v b] = 0 and [tr χ] = −m_k; on each [d_j, d_(j+1)] the functions on 𝒞_in satisfy
Ric(∂_u, ∂_u) = q_out, by [[eq:loc-cone-in]], which holds for every Ω when b = 0, and at each d_j, [tr χ̲] = −n_j, where
tr χ̲ = ∂_u ln 𝒱 on 𝒞_in;

(iii) they equal the background's, and the m_k and n_j vanish, outside compact sets K_out ⊂ [0, v_1] × (ϑ_a, ϑ_b) and
K_in ⊂ [0, u_1] × (ϑ_a, ϑ_b).

Here the jumps are taken along the cones: [F] := F(c_k⁺) − F(c_k⁻) on 𝒞_out and F(d_j⁺) − F(d_j⁻) on 𝒞_in. With p = q = 0
these are the cone data on Q1 of [[def:civp-large-data]].

**Proposition {#prop:loc-shell-cones}** (Free data with atoms.) On 𝒞_out write γ_ϑ = e^(2ϕ + 2ℓ_1), A_c = ϕ + ℓ_2 and
A_s = ϕ + ℓ_3 with ℓ_1 + ℓ_2 + ℓ_3 = 0, and keep Ω the background's. Let the free data (ℓ_1, ℓ_2, ℓ_3) be continuous on
[0, v_1] × (0, π/2) and smooth on each [c_k, c_(k+1)] × (0, π/2), let q_in ≥ 0 be smooth on each of these sets and the
m_k ≥ 0 smooth, all equal to the background's, and m_k = 0, outside a compact subset of [0, v_1] × (ϑ_a, ϑ_b), and let
the corner values of ϕ, ∂_vϕ, b and ∂_v b be the background's. On each generator read the constraints

    Ric(∂_v, ∂_v) = q_in + Σ_k m_k δ(v − c_k),      Ric(∂_v, ∂_ϑ) = 0,

with the left sides of [[eq:loc-cone]], as equations between distributions in v at fixed ϑ for functions ϕ and b that are
continuous and smooth on each [c_k, c_(k+1)]. They determine ϕ and b on every generator on which e^ϕ stays positive; the
resulting functions satisfy (ii) of [[def:loc-shell-data]] on 𝒞_out, with [∂_vϕ] = −m_k/3 at c_k, and equal the
background's at every ϑ outside the band. The same holds on 𝒞_in in the gauge b = 0, with Ω the background's there, with
the free data there, q_out, the n_j, the points d_j, u and [[eq:loc-cone-in]] in place of the free data on 𝒞_out, q_in,
the m_k, the points c_k, v and the first line of [[eq:loc-cone]], the corner values of ϕ and ∂_uϕ being the background's;
then [∂_uϕ] = −n_j/3. No smallness is used; for free data near the background's and small m_k and n_j, e^ϕ stays
positive on [0, v_1] and on [0, u_1].

*Proof.* As distributions in v, for ϰ_i continuous and smooth on each [c_k, c_(k+1)], ∂_v²ϰ_i = {∂_v²ϰ_i} + Σ_k [∂_vϰ_i]
δ(v − c_k), as in the proof of [[lem:loc-shell-ricci]] (a), while the other terms of the first line of [[eq:loc-cone]]
are bounded. So the first constraint holds if and only if it holds on each [c_k, c_(k+1)] and −Σ_i [∂_vϰ_i] = m_k at each
c_k, that is −3[∂_vϕ] = m_k, as Σ_i ℓ_i = 0; then [tr χ] = −m_k. With y := e^ϕ, on each interval the constraint is, as in
the proof of [[prop:loc-cones]], the linear equation y″ − 2(ln Ω)′ y′ + (1/3)(Σ_i (ℓ_i′)² + q_in) y = 0, ′ := ∂_v. With
the corner values and the conditions y′(c_k⁺) = y′(c_k⁻) − (m_k/3) y(c_k) it has exactly one continuous solution that is
smooth on each interval, and this solution is positive near v = 0 and smooth in (v, ϑ) on each [c_k, c_(k+1)] × (0, π/2),
by induction on k, the coefficients and the jumps being smooth in ϑ. In the second line of [[eq:loc-cone]] the
coefficient ∂_v ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) and the term r of [[eq:loc-cone-r]] are bounded: r contains ∂_v∂_ϑ ln Ω
and the ∂_v∂_ϑϰ_i only as derivatives in v of ∂_ϑ ln Ω and of the ∂_ϑϰ_i, which are continuous in v, since ϕ and the ℓ_i
are continuous and smooth in ϑ on each closed interval. So the δ-part of the second line is (γ_ϑ/(4Ω²)) [∂_v b]
δ(v − c_k), and the line holds if and only if it holds on each interval and [∂_v b] = 0: a linear first-order equation
for ∂_v b on each interval, with ∂_v b continuous at the c_k, which with the corner value has exactly one solution; b
follows by integration from the corner. At an angle outside the band the coefficients, the m_k and the corner values are
the background's, so ϕ and b are the background's, by uniqueness. On 𝒞_in, [[eq:loc-cone-in]] is treated in the same way,
and [tr χ̲] = 3[∂_uϕ] = −n_j. For free data near the background's and small m_k and n_j, y is near the background's on
the compact intervals, by continuous dependence on the coefficients and on the jumps, and so positive. ∎

*The smooth theorems at other corners.* [[thm:civp-large]] and [[thm:loc-cone-development]] are stated at the corner
sphere S. The proof of [[thm:loc-shells]] applies them at corner spheres on the cones, and [[prop:loc-shell-crossing]]
(c) at crossing spheres. The next two lemmas state what is used and prove it from the proofs of the two theorems.

**Lemma {#lem:loc-shell-corner-large}** (Developments without smallness at a corner sphere in Q1.) Let 𝒬 = [u_c, u′] ×
[v_c, v′] ⊂ Q1 with u_c < u′ and v_c < v′, let N_o := {u_c} × [v_c, v′] and N_i := [u_c, u′] × {v_c} be its edges and
S_𝒬 := {(u_c, v_c)} × S³ its corner sphere, and let 0 < ϑ_a′ < ϑ_b′ < π/2 and η0′ := (1/3) min(ϑ_a′, π/2 − ϑ_b′).
*Cone data on 𝒬* for the band (ϑ_a′, ϑ_b′) are smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of
(v, ϑ) ∈ [v_c, v′] × (0, π/2) on N_o, and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) ∈ [u_c, u′] × (0, π/2) on
N_i, with b = 0 on N_i, that satisfy (i)–(iii) of [[def:civp-large-data]] with S_𝒬, N_o, N_i, [v_c, v′], [u_c, u′] and
(ϑ_a′, ϑ_b′) in place of S, 𝒞_out, 𝒞_in, [0, v_1], [0, u_1] and (ϑ_a, ϑ_b); Ω on both edges and b on N_o are arbitrary.
A *past set of 𝒬* is a set D ⊂ 𝒬 with [u_c, u] × [v_c, v] ⊂ D for every (u, v) ∈ D. For cone data on 𝒬 there is
δ > 0 such that, with 𝒬_δ := {(u, v) ∈ 𝒬 : min(u − u_c, v − v_c) ≤ δ}, the following hold.

(a) There is a class solution in the gauge on 𝒬_δ × S³ that induces the cone data on N_o and on N_i.

(b) It equals (g0, q̊_in, q̊_out) at the points with ϑ ∉ [ϑ_a′ − η0′, ϑ_b′ + η0′].

(c) Let D′ be a past set of 𝒬 and (g′, v, u, q′_in, q′_out) a class solution in the gauge on D′ × S³ that induces the
cone data on N_o ∩ D′ and on N_i ∩ D′ and equals (g0, q̊_in, q̊_out) at the points with ϑ ∉ [η′, π/2 − η′], for some
η′ > 0. Then it equals the solution of (a) on (D′ ∩ 𝒬_δ) × S³.

*Proof.* For 𝒬 = Q1 and the band (ϑ_a, ϑ_b) these are (a)–(c) of [[thm:civp-large]]. In general the proof of that
theorem applies with the following replacements. We go through it in order and name every place where it uses the
cones 𝒞_out and 𝒞_in, the corner sphere S, the numbers u_1 and v_1, the band, the past sets of Q1, or the function Ω.

*The results it uses.* [[lem:civp-large-frame]], [[lem:civp-large-reduction]] and [[prop:civp-large-system]] are
identities at the points of open sets off the axes, and [[lem:civp-large-energy]] is stated for an arbitrary rectangle
and interval. [[prop:civp-large-corner]] is stated for an arbitrary rectangle in Q1, with the background on the open set
𝒪 ⊃ Q1, so it applies to rectangles in 𝒬. [[lem:civp-large-data]] (a) is stated for an arbitrary rectangle in Q1.
[[lem:civp-large-data]] (b) holds for cone data on 𝒬, with N_o, N_i, S_𝒬, the lines {u = u_c} and {v = v_c} and 𝒬 in
place of 𝒞_out, 𝒞_in, S, {u = 0}, {v = 0} and Q1. Its proof defines the fields on each edge from the functions given
there. It solves linear ordinary differential equations along the generators of the edges, with initial values at the
corner. It uses b = 0 on N_i to write e3 = e^(−α) ∂_u there, and for (ii) only that near each angle outside the band the
data are the background's. None of this depends on the position of the corner. No step requires Ω to be the background's
on an edge: [[def:civp-large-data]] leaves Ω free on both cones, and [[lem:civp-large-data]], [[prop:civp-large-corner]]
and the steps below take the functions on the edges as given.

*Step 1.* Q1 × Y becomes 𝒬 × Y. f̊ becomes the restriction of the background's reduced fields to 𝒬 × (0, π/2), and f̊_e
a function in C^∞(𝒬 × Y; ℝ²³) with the same properties. The band, η0 and J0 become (ϑ_a′, ϑ_b′), η0′ and
J0′ := [ϑ_a′ − 2η0′, ϑ_b′ + 2η0′], and the cut-off ϱ is taken for them. The data are given on {u_c} × Y and {v_c} × Y,
and the transport equations are restricted to {v = v_c} and to {u = u_c}.

*Step 2.* In the coordinates u − u_c and v − v_c the localised system keeps the form (2.7)–(2.8) of [CCTW16], its
coefficients and right side being smooth functions of f and of the coordinates. So [[thm:std-cctw-existence]] and
[[thm:std-cctw-strips]] apply with a0 := u′ − u_c and b0 := v′ − v_c. They give a* and b* and a solution on
𝒰 := ([u_c, u_c + a*] × [v_c, v′] ∪ [u_c, u′] × [v_c, v_c + b*]) × Y.

*Step 3.* In [[eq:civp-large-delta]] the suprema are taken over the corresponding sets, and η0, v_1 and u_1 become η0′,
v′ − v_c and u′ − u_c. [[lem:civp-large-energy]] (a) is applied on [u_c, u_c + s1] × [v_c, v′] and on
[u_c, u′] × [v_c, v_c + s2]. On the second set the b-component of f vanishes at v = v_c: on J0′ because b = 0 on N_i,
and elsewhere because f̊_e has b = 0. So |b| ≤ β1 (v − v_c) there. The set 𝒮 becomes
[u_c, u_c + s1] × [v_c, v′] ∪ [u_c, u′] × [v_c, v_c + s2] ⊃ 𝒬_δ. F is defined on 𝒬_δ × (0, π/2). Its f₃-components
on N_o are f̄₃ and its f₄-components on N_i are f̄₄, and the other components there are the solutions of
[[lem:civp-large-data]] (b) (i) in the form above. In the paragraph on the signs of the densities:
- 𝒬_δ is a past set of 𝒬;
- the segments through a point (u″, v″) are [u_c, u″] × {v″} and {u″} × [v_c, v″];
- the integral curves of D_3 are followed back to u = u_c;
- the densities at u = u_c and at v = v_c are those of the data, which are nonnegative.

*Step 4.* 𝒯₁ := [u_c, u_c + δ] × [v_c, v′] and 𝒯₂ := [u_c, u′] × [v_c, v_c + δ]; 𝒯 is one of them, with sides l1 and
l2. The constants Λ, σ and L are found as there, with η0′ in place of η0. In the corner step, the alternatives that the
corner of the small rectangle has u = 0, or v = 0, become that it has u = u_c, or v = v_c, so that the corresponding edge
lies in N_o, or in N_i. The edges that lie in 𝒞_out or 𝒞_in become those that lie in N_o or N_i, on which the functions
are the cone data. In the continuation in u + v:
- D_t := {(u, v) ∈ 𝒯 : (u − u_c) + (v − v_c) < t};
- the first rectangle is [u_c, u_c + min(L, l1)] × [v_c, v_c + min(L, l2)], with corner sphere S_𝒬, at which F is
  geometric to first order because the values of f̄ there are those of [[eq:civp-large-coefficients]] in the cone data;
- Γ := {(u, v) ∈ 𝒯 : (u − u_c) + (v − v_c) = t*};
- the rectangle about p ∈ Γ has the corner (max(u_p − L/2, u_c), max(v_p − L/2, v_c)), and its edges in N_o or N_i
  carry the cone data.

*Step 5.* The functions induced on N_o and N_i are those of the cone data, by Step 3, as there.

*Step 6.* D′ is a past set of 𝒬, f′₃ = f̄₃ on N_o ∩ D′ and f′₄ = f̄₄ on N_i ∩ D′ ([[lem:civp-large-data]] (b) (iii) in the
form above). For (u, v) ∈ D′ ∩ 𝒬_δ, z := f′ − F is treated on [u_c, u] × [v_c, v] × [η″/2, π/2 − η″/2], with z₃ = 0
at u = u_c and z₄ = 0 at v = v_c, and η″ := min(η′, η0′).

No other step refers to the position of the corner, to u_1 or v_1, or to Ω. With these replacements the proof of
[[thm:civp-large]] proves (a), (b) and (c). ∎

**Lemma {#lem:loc-shell-corner-small}** (Developments near the background's data at a corner sphere in Q1.) Let
(u_c, v_c) ∈ Q1, l_u, l_v > 0 and δ_1 := min(l_u, l_v)/2. Assume that the set

    𝒮_c := {(u, v) : −δ_1 ≤ u − u_c ≤ l_u + δ_1, −δ_1 ≤ v − v_c ≤ l_v + δ_1, min(u − u_c, v − v_c) ≤ δ_1},

the set [[eq:loc-cone-collar]] at this corner, lies in 𝒪. Let 0 < ϑ_a′ < ϑ_b′ < π/2, η := (1/4) min(ϑ_a′, π/2 − ϑ_b′)
and k ≥ 6. Put

    C_* := sup over 𝒮_c of √2 Ω/R,      c_+ := (min(δ_1, η/C_*)/4)²,      δ_* := √c_+/2,

Ω and R being g0's. There are ε_0, C > 0, depending only on k, η, l_u, l_v and g0 on 𝒮_c, with the following property.
Let cone data at the corner (u_c, v_c) be given in the sense of [[def:loc-cone-data]], with the restriction of g0 to 𝒮_c
as the background. Let them be in the normalised gauge, b = 0 on N_i, equal g0's at the points with ϑ outside a compact
subset of (ϑ_a′, ϑ_b′), and have size ε ≤ ε_0. Then there is a class solution in the gauge on G_c × S³,

    G_c := {(u, v) : u_c ≤ u ≤ u_c + l_u, v_c ≤ v ≤ v_c + l_v, (u − u_c)(v − v_c) ≤ δ_*²},

with the following properties. It induces the cone data on the two edges. It equals (g0, q̊_in, q̊_out) at the points
with ϑ ≤ ϑ_a′ − η or ϑ ≥ ϑ_b′ + η. Its functions ln Ω, ½ ln γ_ϑ, b, A_c, A_s, q_in and q_out differ from g0's by at most
Cε, together with their derivatives of order at most k − 4. The width δ_* depends only on l_u, l_v, η and g0 on 𝒮_c, and
not on the data.

*Proof.* [[thm:loc-cone-development]] states this only at S. [[prop:loc-cone-local]] holds at every corner, with a
width that depends on the data only through a bound for their norms, but it gives neither a neighbourhood of the whole
edges nor an estimate. So we
prove it from the proof of [[thm:loc-cone-development]], that is from case (I) of [[sec:loc-cone-reduced]], at the
corner (u_c, v_c).

Translate u and v so that the corner is (0, 0). Then 𝒮_c is the set 𝒮 of [[eq:loc-cone-collar]], and G_c is the set
G_* of [[eq:loc-cone-domain]] with l_u and l_v in place of u_1 and v_1.

*The background.* Put e^(2σ_e) := 2Ω², R_e := R and g_e := −2e^(2σ_e) du dv + R_e² dΩ₃², with the profiles 𝒜 and ℬ of
g0. This is a background on 𝒮 in the sense of [[sec:loc-cone-setting]]: σ_e and R_e are smooth on 𝒮 ⊂ 𝒪, R_e > 0, and
𝒮 ∩ F lies in the set of the points of 𝒪 with u ≥ u_c ≥ 0 and v ≥ v_c ≥ 0 (in the original coordinates), where g0
solves [[eq:two-dust-limit]] ([[sec:civp-large]]). Its double-null functions and densities are g0's. This replaces
[[lem:loc-cone-strips]], which the proof of [[thm:loc-cone-development]] uses only to provide a background on 𝒮 and the
number C_0. The paragraph after [[lem:loc-cone-strips]] records that [[sec:loc-cone-reduced]] and the lemmas after it use
of the background only these properties and a number C_* ≥ sup_𝒮 e^(σ_e)/R_e. Here e^(σ_e)/R_e = √2 Ω/R, so the C_*
above is admissible. It takes the place of C_0.

*The data.* The given data are cone data at the corner of size ε, in the normalised gauge. They equal the background's
at the points with ϑ ∉ [ϑ_a″, ϑ_b″], the least interval that contains the angles at which they differ from it. Here
[ϑ_a″, ϑ_b″] ⊂ (ϑ_a′, ϑ_b′) ⊂ [4η, π/2 − 4η], so they equal the background's off [2η, π/2 − 2η]. They are therefore data
of case (I) of [[sec:loc-cone-reduced]] with this η. This replaces the first part of the proof of
[[thm:loc-cone-development]], which builds the cone data from free data by [[prop:loc-cones]] and [[lem:loc-cone-in]] and
bounds their size.

*The steps reused.* The rest of the proof of [[thm:loc-cone-development]] is used as written, with l_u, l_v and C_* in
place of u_1, v_1 and C_0:
- the choice of δ_c ∈ (0, √c_+/8] with δ_c (l_u + l_v + 1) ≤ c_+/2 ([[sec:loc-cone-reduced]], case (I)) and
  2C_* (δ_c (l_u + l_v + 1))^(1/2) ≤ η/4. So δ_c depends only on l_u, l_v, η and C_*, and G_c ⊂ F ∩ 𝒰;
- [[lem:loc-cone-cauchy]] in case (I), [[lem:loc-cone-past]], [[lem:loc-cone-support]], [[lem:loc-cone-constraints]] and
  [[lem:loc-cone-gauge]]. These are stated and proved for cone data at a corner with a background on 𝒮. Their proofs
  refer to the background only through the properties above and C_*. They give a class solution in the gauge on G_c × S³
  that induces the cone data on the two edges. By the last sentence of [[lem:loc-cone-gauge]], its functions differ from
  the background's by at most Cε with their derivatives of order at most k − 4;
- the localisation, as in the proof of [[thm:loc-cone-development]] (b). By [[lem:loc-cone-support]] and
  [[lem:loc-cone-gauge]] the solution equals the background where ϑ < ϑ_a″ − 2C_* ((u + δ_c)(v + δ_c))^(1/2) or
  ϑ > ϑ_b″ + 2C_* ((u + δ_c)(v + δ_c))^(1/2). On G_c, (u + δ_c)(v + δ_c) ≤ uv + δ_c (l_u + l_v + 1), as δ_c ≤ 1, and
  2C_* (uv)^(1/2) ≤ 2C_* δ_* ≤ η/4, as δ_* ≤ η/(8C_*). With the choice of δ_c this gives
  2C_* ((u + δ_c)(v + δ_c))^(1/2) ≤ η/2. So the solution equals the background where ϑ < ϑ_a″ − η/2 or
  ϑ > ϑ_b″ + η/2, and in particular where ϑ ≤ ϑ_a′ − η or ϑ ≥ ϑ_b′ + η.

The steps of that proof not used are the construction of the data, the clause of its part (b) on u_K and v_K, and its
part (d) with [[lem:loc-cone-unique]].

*The constants.* δ_* = √c_+/2 depends only on δ_1, η and C_*, that is on l_u, l_v, η and g0 on 𝒮_c. ε_0 is the number
for which [[lem:loc-cone-system]], [[lem:loc-cone-cauchy]] and [[lem:loc-cone-gauge]] hold in case (I), and C is the
constant of their estimates. They depend only on:
- the bounds for the modified system in [[lem:loc-cone-system]] (a), which depend only on η, k, δ_c and the background
  on 𝒮, the size being at most ε ≤ 1;
- the region 𝒰 of [[eq:loc-cone-region]], which is fixed by δ_1, δ_c, c_+ and κ = δ_1/(4(l_u + l_v + 1)).
None of them depends on the data. ∎

**Theorem {#thm:loc-shells}** (Developments of cone data with null shells.) Let cone data with shells along the leaves be
given ([[def:loc-shell-data]]); no smallness is assumed. Let N := max(p, q) + 1, and define bands by
(ϑ_a^(0), ϑ_b^(0)) := (ϑ_a, ϑ_b) and

    ϑ_a^(i+1) := ϑ_a^(i) − w_i,      ϑ_b^(i+1) := ϑ_b^(i) + w_i,
    w_i := ½ min(ϑ_a^(i), π/2 − ϑ_b^(i)),                                                       {#eq:loc-shell-bands}

so that ϑ_a^(N) ≥ 2^(−N) ϑ_a and π/2 − ϑ_b^(N) ≥ 2^(−N) (π/2 − ϑ_b). There is δ ∈ (0, min(c_1, d_1)) such
that, with 𝒮_δ := {(u, v) ∈ Q1 : min(u, v) ≤ δ}, the following hold.

(a) *Existence.* There is a solution with null shells along the leaves on 𝒮_δ × S³ ([[def:loc-shell-solution]]) that
induces the cone data. No crossing sphere lies in 𝒮_δ. On every ingoing leaf [∂_v b] = 0; q_out is continuous across the
ingoing leaves and q_in across the outgoing ones. The shell densities are 𝔪_k = −[tr χ] on {v = c_k}, with 𝔪_k = m_k at
u = 0 and ∂_u(𝒱𝔪_k) + ∂_ϑ(b𝒱𝔪_k) = 0, and 𝔫_j = −[tr χ̲] on {u = d_j}, with 𝔫_j = n_j at v = 0 and ∂_v(𝒱𝔫_j) = 0.

(b) *Localisation.* The solution equals (g0, q̊_in, q̊_out), and its shell densities vanish, at the points with ϑ ∉
(ϑ_a^(N), ϑ_b^(N)).

(c) *Uniqueness.* Let D′ ⊂ Q1 be a past set and (g̃, v, u, q̃_in, q̃_out, 𝔪̃_k, 𝔫̃_j) a solution with null shells along
the same leaves on D′ × S³ that induces the cone data on 𝒞_out ∩ D′ and on 𝒞_in ∩ D′ and equals (g0, q̊_in, q̊_out) at
the points with ϑ ∉ [η′, π/2 − η′], for some η′ > 0. Then it equals the solution of (a) on (D′ ∩ 𝒮_δ) × S³.

(d) *Small data.* Let u_1 and v_1 be as in [[thm:loc-cone-development]], and let the cone data
be given by [[prop:loc-shell-cones]] from free data whose pieces extend: for 0 ≤ k ≤ p there are smooth free data
(ℓ_1^(k), ℓ_2^(k), ℓ_3^(k)) and a density q_in^(k) ≥ 0 on [c_k, v_1] × (0, π/2), equal to the given ones on [c_k,
c_(k+1)] × (0, π/2) and to the background's outside a compact subset of [0, v_1) × (ϑ_a, ϑ_b), and likewise on 𝒞_in for
0 ≤ j ≤ q. Let k_(N−1) := 6, k_(i−1) := 6k_i + 23 for 1 ≤ i ≤ N − 1, and m_* := 6k_0 + 21, and let ε be the largest
absolute value of a derivative of order at most m_* of the differences of these extensions from the background's and of
the m_k and n_j. There are w ∈ (0, min(c_1, d_1)) and ε_0, C > 0, depending only on g0, u_1, v_1, the leaves and the
band, such that for ε ≤ ε_0 the conclusions of (a) and (b) hold with 𝒮_w in place of 𝒮_δ; the
solution equals that of (a) on 𝒮_(min(δ, w)) × S³; and on each closed cell of 𝒮_w its functions ln Ω, ½ ln γ_ϑ, b, A_c,
A_s, q_in and q_out differ from the background's by at most Cε, together with their first derivatives, one-sided at the
leaves.

*Proof.* Write 𝒵_k := [c_k, c_(k+1)] and 𝒴_j := [d_j, d_(j+1)]. For a band (ϑ_a′, ϑ_b′), with η0′ := (1/3) min(ϑ_a′,
π/2 − ϑ_b′) as in [[eq:civp-large-band]] and w′ := ½ min(ϑ_a′, π/2 − ϑ_b′) = (3/2) η0′, the interval [ϑ_a′ − η0′,
ϑ_b′ + η0′] is a compact subset of (ϑ_a′ − w′, ϑ_b′ + w′). The development is built on the rectangles 𝒫_0 := [0,
d_1] × [0, c_1], 𝒫_k^out := [0, λ_k^out] × 𝒵_k (1 ≤ k ≤ p) along 𝒞_out and 𝒫_j^in := 𝒴_j × [0, λ_j^in] (1 ≤ j ≤ q) along
𝒞_in, with numbers λ chosen below; 𝒫_k^out has depth k, 𝒫_j^in depth j and 𝒫_0 depth 0.

*Step 1: the corner rectangle.* The restrictions of the cone data to {0} × [0, c_1] and [0, d_1] × {0} are cone
data on 𝒫_0 in the sense of [[def:civp-large-data]], with d_1 and c_1 in place of u_1 and v_1: they are smooth
up to the ends, and (i)–(iii) hold by [[def:loc-shell-data]]. [[thm:civp-large]] gives a class solution in the
gauge on {(u, v) ∈ 𝒫_0 : min(u, v) ≤ δ} for some δ > 0, inducing these data and equal to (g0, q̊_in, q̊_out) at
the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0], so off (ϑ_a^(1), ϑ_b^(1)), and unique in the sense of its part (c). Let
δ_0 := min(δ, min(c_1, d_1)/2), 𝒮_0 := {(u, v) ∈ 𝒫_0 : min(u, v) ≤ δ_0} and g_0 the restriction of that solution to
𝒮_0 × S³.

*Step 2: along 𝒞_out.* For k = 1, …, p in turn put λ_k^out := δ_(k−1)^out, with δ_0^out := δ_0; then 𝒫_k^out lies in the
cell Q_0k, as λ_k^out ≤ δ_0 < d_1. On N_o := {0} × 𝒵_k take the cone data, which are smooth up to the ends of 𝒵_k. On
N_i := [0, λ_k^out] × {c_k}, which lies in the domain 𝒮_(k−1)^out of g_(k−1)^out (𝒮_0^out := 𝒮_0, g_0^out := g_0), take
the functions Ω, γ_ϑ, b, A_c, A_s and q_out of g_(k−1)^out. The two agree at (0, c_k), where both are the values of the
cone data, g_(k−1)^out inducing them; and Ric(L̲, L̲) = q_out on N_i, the left side involving only derivatives along N_i
([[def:loc-cone-data]] (ii)), because g_(k−1)^out solves the class system up to {v = c_k}. Let Φ_k(u, ϑ) solve
(∂_u + b(u, c_k, ϑ) ∂_ϑ) Φ_k = 0 with Φ_k(0, ϑ) = ϑ. As b vanishes on N_i outside a compact subset of (ϑ_a^(k), ϑ_b^(k)),
where g_(k−1)^out is g0, Φ_k(u, ·) is a diffeomorphism of (0, π/2) equal to the identity off that set. The change of
angle (u, v, ϑ) ↦ (u, v, Φ_k(u, ϑ)) maps a metric of the form [[eq:loc-double-null]] to one of the same form, with Ω,
A_c, A_s unchanged, γ_ϑ replaced by γ_ϑ/(∂_ϑΦ_k)² and b by ∂_uΦ_k + b ∂_ϑΦ_k, because Φ_k does not depend on v and

    dϑ − b du = (∂_ϑΦ_k)⁻¹ (dΦ_k − (∂_uΦ_k + b ∂_ϑΦ_k) du).

It commutes with the action of G, it is the identity on N_o and off that set, and it makes b vanish on N_i, while b on
N_o becomes b − b(0, c_k, ·). The transformed functions on N_o and N_i are cone data on 𝒬 := 𝒫_k^out for the band
(ϑ_a^(k), ϑ_b^(k)) in the sense of [[lem:loc-shell-corner-large]]: the constraints are statements about Ric(∂_v, ·) on
N_o and Ric(L̲, L̲) on N_i, and the fields ∂_v and L̲, and ∂_ϑ on N_o, are unchanged. By [[lem:loc-shell-corner-large]] (a)
and (b) there are δ_k^out ∈ (0, λ_k^out] and a class
solution in the gauge on 𝒮_k^out := {(u, v) ∈ 𝒫_k^out : min(u, v − c_k) ≤ δ_k^out} that induces these functions and
equals (g0, q̊_in, q̊_out) off (ϑ_a^(k+1), ϑ_b^(k+1)); changing the angle back gives g_k^out on 𝒮_k^out × S³, which
induces the cone data on N_o and the functions of g_(k−1)^out on N_i.

*Step 3: along 𝒞_in.* For j = 1, …, q in turn put λ_j^in := δ_(j−1)^in, with δ_0^in := δ_0, 𝒮_0^in := 𝒮_0 and
g_0^in := g_0. On N_i := 𝒴_j × {0} ⊂ 𝒞_in take the cone data, with b = 0. On N_o := {d_j} × [0, λ_j^in], which lies in
𝒮_(j−1)^in, take the functions Ω, γ_ϑ, b, A_c, A_s and q_in of g_(j−1)^in. They agree at (d_j, 0), and Ric(∂_v,
∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o by [[lem:loc-cone-equations]], since g_(j−1)^in solves the class system up to
{u = d_j}. No change of angle is needed. By [[lem:loc-shell-corner-large]] (a) and (b), for 𝒬 := 𝒫_j^in and the band
(ϑ_a^(j), ϑ_b^(j)), there are δ_j^in ∈ (0, λ_j^in] and a class solution g_j^in in the gauge
on 𝒮_j^in := {(u, v) ∈ 𝒫_j^in : min(u − d_j, v) ≤ δ_j^in} that induces these functions and equals (g0, q̊_in, q̊_out) off
(ϑ_a^(j+1), ϑ_b^(j+1)).

*Step 4: the glued metric.* Let δ be the least of δ_0, the δ_k^out and the δ_j^in; then δ < min(c_1, d_1). A point of 𝒮_δ
with v ≥ c_1 has u ≤ δ < d_1, and one with u ≥ d_1 has v ≤ δ < c_1. So no crossing sphere lies in 𝒮_δ, and 𝒮_δ is the
union of 𝒮_δ ∩ 𝒫_0 ⊂ 𝒮_0, of the sets [0, δ] × 𝒵_k ⊂ 𝒮_k^out and of the sets 𝒴_j × [0, δ] ⊂ 𝒮_j^in, two of which meet
only along a leaf {v = c_k} or {u = d_j}. Define g, q_in and q_out on 𝒮_δ × S³ by g_0, the g_k^out and the g_j^in. On a
common leaf the two solutions induce the same functions, by Steps 2 and 3. So g is continuous and cellwise smooth, each
closed cell carries a class solution in the gauge, and q_out is continuous across the ingoing leaves and q_in across the
outgoing ones: (J3) of [[prop:loc-shell-junction]] holds.

*Step 5: the junction.* At (0, c_k), the jump of ∂_v b across {v = c_k} is that of the cone data along 𝒞_out, since
g_(k−1)^out and g_k^out induce b on 𝒞_out; it vanishes by [[def:loc-shell-data]] (ii). As b vanishes near the axes,
[[prop:loc-shell-junction]] (a) gives [∂_v b] = 0 on {v = c_k} ∩ 𝒮_δ: (J1). At u = 0, −[tr χ] is the jump of −tr χ = −∂_v
ln 𝒱 of the cone data along 𝒞_out, which is m_k ≥ 0; by [[prop:loc-shell-junction]] (b), 𝔪_k := −[tr χ] ≥ 0 on the leaf
and ∂_u(𝒱𝔪_k) + ∂_ϑ(b𝒱𝔪_k) = 0. At v = 0, −[tr χ̲] is the jump of −∂_u ln 𝒱 of the cone data along 𝒞_in, where b = 0,
which is n_j ≥ 0; by [[prop:loc-shell-junction]] (c), 𝔫_j := −[tr χ̲] ≥ 0 on the leaf and ∂_v(𝒱𝔫_j) = 0. These functions
are smooth and vanish near the axes, the solution being g0 there. So (J1)–(J3) hold with these shell densities, and by
[[prop:loc-shell-junction]] (d), g is a solution with null shells along the leaves on 𝒮_δ × S³. It induces the cone data:
on 𝒞_out ∩ 𝒮_δ through g_0 and the g_k^out, and on 𝒞_in ∩ 𝒮_δ through g_0 and the g_j^in. This proves (a).

(b) g_0 equals g0 off (ϑ_a^(1), ϑ_b^(1)), g_k^out off (ϑ_a^(k+1), ϑ_b^(k+1)) and g_j^in off (ϑ_a^(j+1), ϑ_b^(j+1)); these
bands increase with the index, and k + 1, j + 1 ≤ N. The shell densities are jumps of functions that equal g0's off
(ϑ_a^(N), ϑ_b^(N)). Finally w_i ≤ ϑ_a^(i)/2 and w_i ≤ (π/2 − ϑ_b^(i))/2, which give the bounds after
[[eq:loc-shell-bands]] by induction.

(c) Let g̃ be as stated. The set D′ ∩ 𝒫_0 is a past set of 𝒫_0, and the restriction of g̃ to it, which is smooth since
𝒫_0 is a cell, is a class solution in the gauge that induces the data of Step 1 and equals g0 near the axes; by
[[thm:civp-large]] (c), g̃ = g_0 on D′ ∩ 𝒮_0. Suppose that g̃ = g_(k−1)^out on D′ ∩ 𝒮_(k−1)^out. The set D′ ∩ 𝒫_k^out is
a past set of 𝒫_k^out relative to its corner (0, c_k), g̃ is smooth on it since 𝒫_k^out ⊂ Q_0k, and g̃ induces the cone
data on N_o ∩ D′ and the functions of g_(k−1)^out on N_i ∩ D′ ⊂ 𝒮_(k−1)^out: Ω, γ_ϑ, b, A_c and A_s by continuity,
q_out by (J3) of [[prop:loc-shell-junction]] (d). After the change of angle Φ_k, which depends only on these functions,
[[lem:loc-shell-corner-large]] (c) gives g̃ = g_k^out on D′ ∩ 𝒮_k^out. In the same way, with q_in on N_o by (J3) across {u = d_j},
g̃ = g_j^in on D′ ∩ 𝒮_j^in for every j. So g̃ = g on D′ ∩ 𝒮_δ, the densities q̃_in and q̃_out included, and the shell
densities, which (J2) determines from the metric, agree as well.

(d) We repeat Steps 1–5, with [[thm:loc-cone-development]] at S and [[lem:loc-shell-corner-small]] in place of
[[lem:loc-shell-corner-large]] at the other corners, and keep
track of sizes; C denotes constants that depend only on g0, u_1, v_1, the leaves, the band and N. The rectangle of depth
i is developed with the index k_i, and its band is (ϑ_a^(i), ϑ_b^(i)); the localisation of [[thm:loc-cone-development]]
(b) and of [[lem:loc-shell-corner-small]], with η = w_i/2, gives g0 off (ϑ_a^(i) − η, ϑ_b^(i) + η), a compact subset of (ϑ_a^(i+1), ϑ_b^(i+1)). As
the extensions equal the background's near v = v_1 and u = u_1 and 𝒪 is an open neighbourhood of Q1, there is δ_e > 0
such that the extended free data, continued by the background's, are defined on [c_k, v_1 + δ_e] and on [d_j, u_1 + δ_e],
and such that 𝒪 contains [−δ_e, 3δ_e] × [−δ_e, v_1 + δ_e] and [−δ_e, u_1 + δ_e] × [−δ_e, 3δ_e].

*Extended data.* On 𝒞_out ∩ {c_k ≤ v ≤ v_1 + δ_e} solve the equations of the proof of [[prop:loc-shell-cones]] with the
free data (ℓ_i^(k), q_in^(k)) and the values of ϕ, ∂_vϕ, b and ∂_v b of the cone data at c_k⁺. By uniqueness the result
agrees with the cone data on 𝒵_k. The initial values differ from the background's by at most Cε, with their derivatives
in ϑ of order at most m_* − 3, as they come from the solutions on the earlier intervals and from the m_k; so, as in the
proof of [[thm:loc-cone-development]], for ε small e^ϕ stays positive and the result differs from the background's by at
most Cε in C^(m_* − 3) = C^(6k_0 + 18). These are the *extended cone data of depth k*; likewise on 𝒞_in.

*Depth 0.* [[thm:loc-cone-development]] with the free data (ℓ_i^(0), q_in^(0)) and their analogues on 𝒞_in, k = k_0 and
m = m_*, gives for ε ≤ ε_0 a solution on {(u, v) ∈ Q1 : uv ≤ δ_*,0²}, within Cε of the background's with the derivatives
of order at most k_0 − 4, and equal to them off (ϑ_a^(1), ϑ_b^(1)); this set contains [0, λ_1] × [0, v_1] and [0,
u_1] × [0, λ_1], λ_1 := min(δ_*,0²/max(u_1, v_1), min(c_1, d_1)/2, 3δ_e), and the solution induces the cone data on 𝒵_0
and 𝒴_0.

*Depth k ≥ 1 along 𝒞_out.* Let λ_k^out be the width found at depth k − 1, so that the solution of depth k − 1 contains
[0, λ_k^out] × 𝒵_(k−1) and is within Cε of the background's there with its derivatives of order at most k_(k−1) − 4 (at
depth 0 as stated above, at depth k − 1 ≥ 1 by the next paragraph, applied at that depth). Apply
[[lem:loc-shell-corner-small]] at (0, c_k), with the band (ϑ_a^(k), ϑ_b^(k)), the index k_k, l_u := (2/3) λ_k^out and
l_v := v_1 − c_k: then δ_1 ≤ λ_k^out/3 ≤ δ_e, so N_i ⊂ [0, λ_k^out] × {c_k}, N_o = {0} × [c_k, v_1 + δ_1] carries the
extended cone data of depth k, and the set 𝒮_c of that lemma lies in [−δ_e, 3δ_e] × [−δ_e, v_1 + δ_e] ⊂ 𝒪, as
l_u + δ_1 ≤ λ_k^out ≤ λ_1 ≤ 3δ_e. Its width δ_*,k depends only on λ_k^out, v_1 − c_k, the band and g0, and not on the
data. On N_i take
the functions of the solution of depth k − 1. The map Φ_k(u, ·) is the inverse of the flow from 0 to u of the
u-dependent vector field b(u, c_k, ·) ∂_ϑ on (0, π/2), which is within Cε of 0 in C^(k_(k−1) − 4); such a flow and its
inverse are within Cε of the identity in C^(k_(k−1) − 4), so Φ_k(u, ϑ) − ϑ and Φ_k(u, ·)⁻¹(ϑ) − ϑ are at most Cε with
their derivatives in (u, ϑ) of order at most k_(k−1) − 4. The transformed functions are γ_ϑ/(∂_ϑΦ_k)², ∂_uΦ_k + b ∂_ϑΦ_k
and the other functions, composed in the angle with Φ_k(u, ·)⁻¹; by the argument of the next paragraph, with
Φ_k(u, ·)⁻¹ in place of Φ_k and k_(k−1) − 5 in place of k_k − 4, they are within Cε of the background's with their
derivatives of order at most k_(k−1) − 5 = 6k_k + 18, the order m_0 of [[def:loc-cone-data]] for the index k_k. On N_o
the change of angle subtracts b(0, c_k, ·). So the data have size at most Cε, and for ε small the lemma gives a solution on
{0 ≤ u ≤ l_u, c_k ≤ v ≤ v_1, u(v − c_k) ≤ δ_*,k²}, which contains [0, λ_(k+1)^out] × [c_k, v_1] with
λ_(k+1)^out := min(l_u, δ_*,k²/(v_1 − c_k)), and which is within Cε of the background's with its derivatives of order at
most k_k − 4 in the transformed angle.

*Changing the angle back loses no derivative.* The change back replaces each function F(u, v, ϑ) by F(u, v, Φ_k(u, ϑ)),
written F ∘ Φ_k, and then multiplies γ_ϑ by (∂_ϑΦ_k)² and replaces b by (b − ∂_uΦ_k)/∂_ϑΦ_k. Let F be one of the
functions of the solution, within Cε of the background's F̊ in C^(k_k − 4). Then F ∘ Φ_k − F̊ = (F − F̊) ∘ Φ_k +
(F̊ ∘ Φ_k − F̊). The first term is within Cε in C^(k_k − 4) by the chain rule, the derivatives of Φ_k of order at most
k_k − 4 being bounded. The second is (Φ_k − ϑ) ∫_0^1 ∂_ϑF̊(u, v, ϑ + t(Φ_k − ϑ)) dt. Here Φ_k(u, ·) is the identity off a
compact subset K of (0, π/2) and maps K onto K, so the second term vanishes off K, and on K the angles ϑ + t(Φ_k − ϑ)
lie in the least interval that contains K, a compact subset of (0, π/2) on which F̊ is smooth; so the integral is
bounded in C^(k_k − 4) on K, and the second term is within Cε in C^(k_k − 4). The factors (∂_ϑΦ_k)², ∂_uΦ_k and
1/∂_ϑΦ_k, and ln ∂_ϑΦ_k, which the change adds to ½ ln γ_ϑ, are within Cε of 1, 0, 1 and 0 in C^(k_(k−1) − 5), and
k_(k−1) − 5 = 6k_k + 18 ≥ k_k − 4. As the background's b is 0, the solution of depth k is within Cε of the background's
with its derivatives of order at most k_k − 4 in the original angle too. Along 𝒞_in the same holds with
l_v := (2/3) λ_j^in, l_u := u_1 − d_j and no change of angle, the functions on N_o being those of the solution of depth
j − 1, within Cε with their derivatives of order at most k_(j−1) − 4 ≥ 6k_j + 18, and the set 𝒮_c of
[[lem:loc-shell-corner-small]] at (d_j, 0) lying in [−δ_e, u_1 + δ_e] × [−δ_e, 3δ_e] ⊂ 𝒪.

All these widths depend only on g0, u_1, v_1, the leaves, the band and the k_i, and not on the data; let w be the least
of them. Steps 4 and 5 and the proof of (b) apply with w in place of δ, and give a solution with null shells on 𝒮_w × S³
with the properties of (a) and (b) and the stated estimate, as k_i − 4 ≥ k_(N−1) − 4 = 2 at every depth i. It
induces the cone data and equals g0 near the axes, and 𝒮_w is a past set; by (c) it equals the solution of (a) on
𝒮_w ∩ 𝒮_δ = 𝒮_(min(δ, w)). ∎

**Proposition {#prop:loc-shell-crossing}** (Crossing shells.) Let D ⊂ Q1 be a past set, (g, v, u, q_in, q_out, 𝔪_k, 𝔫_j)
a solution with null shells along the leaves on D × S³, and Z := {(d_j, c_k)} × S³ a crossing sphere in D. Number the
four cells at Z by (±, ±), the first sign being that of u − d_j and the second that of v − c_k, and write F_(±±) for the
value at a point of Z, from the cell (±, ±), of a cellwise smooth function F. For a set D′ ⊂ Q1 that meets every line
{u = const} and every line {v = const} in an interval, a solution with null shells along the leaves on D′ × S³ is
defined by [[def:loc-shell-solution]], and the definitions before it, with D′ in place of D, and [[lem:loc-shell-ricci]]
and [[prop:loc-shell-junction]] hold with D′ in place of D, the last sentence of (a) of the latter with any sphere
{(u′, c_k)} × S³ ⊂ D′ × S³ in place of {(0, c_k)} × S³ and the part of the leaf where u ≥ u′ in place of the leaf. The
sets 𝔏, 𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s] and 𝔏 ∪ D″ of (b) and (c) have this property.

(a) *The crossing rule.* If D contains a neighbourhood of (d_j, c_k), then at every point of Z, tr χ_(+−) = tr χ_(−−),
tr χ_(++) = tr χ_(−+), tr χ̲_(−+) = tr χ̲_(−−) and tr χ̲_(++) = tr χ̲_(+−), so that

    (tr χ tr χ̲)_(++) (tr χ tr χ̲)_(−−) = (tr χ tr χ̲)_(+−) (tr χ tr χ̲)_(−+),

and 𝒱𝔪_k and 𝒱𝔫_j are continuous at Z. If g is round, b = 0, γ_ϑ = R², e^(A_c) = R cos ϑ, e^(A_s) = R sin ϑ and
Ω² = e^(2σ)/2 with R and σ functions of (u, v), then tr χ = 3R_v/R and tr χ̲ = 3R_u/R, the function f = 1 − μ/R² =
−2e^(−2σ) R_u R_v of [[eq:two-dust-mass]], μ the mass function, is −(R²/(9Ω²)) tr χ tr χ̲, R and σ are continuous, and on
Z

    f_(++) f_(−−) = f_(+−) f_(−+),      that is,      (R² − μ_(++)) (R² − μ_(−−)) = (R² − μ_(+−)) (R² − μ_(−+)).
                                                                                           {#eq:loc-shell-crossing-rule}

Moreover, for round g, R²[R_v] is constant along {v = c_k}, through Z, and R²[R_u] along {u = d_j}; and the mass function
jumps by [μ] = 2e^(−2σ) R² R_u [R_v] across {v = c_k} and by [μ] = 2e^(−2σ) R² R_v [R_u] across {u = d_j}.

(b) *Round continuation.* Let λ > 0 be less than the distance from (d_j, c_k) to the other leaves, and put
𝔏 := ([d_j − λ, d_j + λ] × [c_k − λ, c_k + λ]) ∖ ((d_j, d_j + λ] × (c_k, c_k + λ]). If 𝔏 ⊂ D and g is round on 𝔏 × S³,
there is s ∈ (0, λ] such that the restriction of the solution to 𝔏 × S³ extends to a round solution with null shells
along the leaves on (𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s]) × S³; the extension is unique among round ones, and its shells
continue those of the solution through Z.

(c) *Continuation off the axes.* With λ and 𝔏 as in (b), let 𝔏 ⊂ D and let the solution equal (g0, q̊_in, q̊_out) at the
points of 𝔏 × S³ with ϑ ∉ [2η, π/2 − 2η], where η ∈ (0, π/8]. There is s ∈ (0, λ] such that its restriction to 𝔏 × S³
extends to a solution with null shells along the leaves on (𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s]) × S³ that equals (g0,
q̊_in, q̊_out) at the points with ϑ ∉ [η, π/2 − η], its shells continuing those of the solution through Z. With
𝒬 := [d_j, d_j + λ] × [c_k, c_k + λ], there are δ > 0 and such an extension on (𝔏 ∪ 𝒬_δ) × S³, 𝒬_δ := {(u, v) ∈ 𝒬 :
min(u − d_j, v − c_k) ≤ δ}, and it is unique: a solution with null shells along the leaves on (𝔏 ∪ D″) × S³, D″ a past
set of 𝒬 relative to its corner, that equals the given one on 𝔏 × S³ and (g0, q̊_in, q̊_out) near the axes, equals it on
D″ ∩ 𝒬_δ.

(d) *At an axis.* The identities of (a) hold at the points of Z on the axes too, for every solution in the sense of
[[def:loc-shell-solution]], and so do the junction conditions of [[prop:loc-shell-junction]], by continuity. No
continuation through a crossing sphere is asserted for solutions that near Z are neither round nor equal to g0 near the
axes; in particular nothing is asserted for shells that are not round at an axis, whether or not they cross: (b) uses the
equations of round metrics, and the results used in (c) need data equal to a smooth round background near the axes
([[rem:loc-cone-scope]] (ii), [[rem:loc-cone-local-scope]]).

*Proof.* *The sets D′.* The proof of [[lem:loc-shell-ricci]] (a) uses of D only that for fixed (u, y) the points of D
with these coordinates form an interval in v, and for fixed (v, y) an interval in u; the proof of its part (b) works at
each point separately. The proof of [[prop:loc-shell-junction]] solves linear ordinary differential equations along
integral curves of L̲ and along generators in a leaf, over the interval in which the line {v = c_k} or {u = d_j} meets
D, and in (d) applies the rule for derivatives of the proof of [[lem:loc-shell-ricci]] (a) on such intervals and tests
with functions supported near single points; it uses the sphere {(0, c_k)} × S³ only in the last sentence of (a), where
the same argument, with the curves started at u = u′, gives the form stated. So both results hold with D′ in place of D.
The set 𝔏 meets {u = u′} in {u′} × [c_k − λ, c_k + λ] if d_j − λ ≤ u′ ≤ d_j, in {u′} × [c_k − λ, c_k] if
d_j < u′ ≤ d_j + λ, and nowhere otherwise, and it meets the lines {v = v′} in the same way, with u and v exchanged. For
s ∈ (0, λ] the set 𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s] meets {u = u′} in {u′} × [c_k − λ, c_k + s] if
d_j < u′ ≤ d_j + s and as 𝔏 does otherwise, since {d_j} × [c_k, c_k + s] ⊂ 𝔏. Let D″ be a past set of 𝒬 relative to
its corner, and d_j ≤ u′ ≤ d_j + λ. If (u′, v) ∈ D″, then {u′} × [c_k, v] ⊂ D″; so D″ meets {u = u′} in the empty set
or in {u′} × I, I ⊂ [c_k, c_k + λ] an interval that contains c_k. Hence 𝔏 ∪ D″ meets {u = u′} in
{u′} × ([c_k − λ, c_k] ∪ I), an interval, if u′ > d_j, and as 𝔏 does if u′ = d_j or u′ ∉ [d_j, d_j + λ]. The lines
{v = v′} are treated in the same way.

(a) Ω, b and 𝒱 are continuous. ∂_v is tangent to {u = d_j}, so tr χ = ∂_v ln 𝒱 has the same values at Z from the
two cells on the same side of {v = c_k}; L̲ and ∂_ϑ are tangent to {v = c_k}, so tr χ̲ = L̲ ln 𝒱 + ∂_ϑ b has the same
values at Z from the two cells on the same side of {u = d_j}. Multiplying gives the identity. By
[[prop:loc-shell-junction]] (d) the solution satisfies (J1) and (J2), so 𝒱𝔪_k = −𝒱[tr χ] and 𝒱𝔫_j = −𝒱[tr χ̲] are
continuous at Z by [[prop:loc-shell-junction]] (b) and (c). For a round metric 𝒱 = R³ sin ϑ cos ϑ and b = 0, so tr
χ = 3R_v/R and tr χ̲ = 3R_u/R, and with 2e^(−2σ) = Ω⁻², f = −(R²/(9Ω²)) tr χ tr χ̲. R and Ω are continuous, so the
identity for tr χ tr χ̲ gives the first form of [[eq:loc-shell-crossing-rule]], and R² − μ = R² f gives the second.
Further, 𝒱[tr χ] = 3R²[R_v] sin ϑ cos ϑ, so [[prop:loc-shell-junction]] (b), with b = 0, shows that R²[R_v] is constant
in u along {v = c_k} and continuous at Z; likewise (c) for R²[R_u]. Finally R_u is continuous across {v = c_k}, being a
derivative along it, so [μ] = −R²[f] = 2e^(−2σ) R² R_u [R_v] there, and likewise across {u = d_j}.

(b) Translate u and v so that Z is {(0, 0)} × S³. A round class solution in double-null form with the phases v and u
has q_in = 𝒜/R³ and q_out = ℬ/R³ with 𝒜 a function of v and ℬ of u, since its conservation laws are ∂_u(R³ q_in) = 0
and ∂_v(R³ q_out) = 0; so the cells (−, +) and (+, −) carry round solutions of the two-null-dust equations, with
smooth profiles 𝒜 on [0, λ] and ℬ on [0, λ]. The functions R, σ and R_v of the cell (−, +) on N_o := {0} × [0, λ],
and R, σ and R_u of the cell (+, −) on N_i := [0, λ] × {0}, agree at Z and satisfy C_v = 0 on N_o and C_u = 0 on N_i
([[eq:two-dust-constraints]]), these being equations along the edges. Let r_0 > 0 be the least value of R on N_o ∪ N_i,
and U := (R, σ, P, Q̄). On [0, s]², s ≤ λ, consider [[eq:two-dust-volterra]] with (u0, v0) := (0, 0), P(·, 0) := R_u on
N_i and Q̄(0, ·) := R_v on N_o, and let U_D(u, v) := (R(0, v), D[σ](u, v), P(u, 0), Q̄(0, v)) be the part of its right
sides given by the data. On the set B of continuous U on [0, s]² with |U − U_D| ≤ r_0/2 in each component, R ≥ r_0/2
and |U| ≤ M_0, with M_0 depending only on the data, and 𝔉 and ℌ are bounded by a number M_1 and Lipschitz with a constant
L_1. Each single integral in [[eq:two-dust-volterra]] runs over an interval of length at most s and the double one over
a square of area at most s², so the right sides map B into itself if s(M_0 + M_1) + s²M_1 ≤ r_0/2, and are a contraction
in the supremum norm if s(1 + 2L_1) + s²L_1 ≤ 1/2. For such s they have exactly one fixed point in B. As in the proof
of [[prop:two-dust-background]] (d), it solves [[eq:two-dust-evolution]], the constraints [[eq:two-dust-constraints]]
hold by [[lem:two-dust-equations]], propagated from the edges, and it is smooth on [0, s]², the data being smooth on the
closed edges; and two continuous solutions of [[eq:two-dust-volterra]] on [0, s]² with R > 0 agree, by the contraction in
the norm sup e^(−γ(u + v))|U| with γ large used there, applied on the compact set of values of the two solutions.

Extend the solution by the round metric of this (R, σ) on [0, s]², with q_in = 𝒜/R³ and q_out = ℬ/R³. The extended metric
is continuous and cellwise smooth, and each closed cell carries a class solution in double-null form. (J1) holds, as
b = 0, and (J3), as 𝒜 depends on v alone, ℬ on u alone, and R is continuous. By [[prop:loc-shell-junction]] (b) and (c),
applied to the extended metric, 𝒱[tr χ] = 3R²[R_v] sin ϑ cos ϑ is constant along {v = 0} through Z, and 𝒱[tr χ̲] along
{u = 0}; so 𝔪 := −[tr χ] ≥ 0 and 𝔫 := −[tr χ̲] ≥ 0 continue 𝔪_k and 𝔫_j. By [[prop:loc-shell-junction]] (d) the extension
is a solution with null shells along the leaves. A round extension that is such a solution has R and σ continuous,
and R_v on N_o and R_u on N_i are derivatives along the edges, so it takes the same data on N_o and N_i and solves
[[eq:two-dust-volterra]] on the new cell; so it is the one constructed.

(c) Translate u and v so that Z is {(0, 0)} × S³. On N_o := {0} × [0, λ] take the functions Ω, γ_ϑ, b, A_c, A_s and
q_in of the cell (−, +), and on N_i := [0, λ] × {0} the functions Ω, γ_ϑ, b, A_c, A_s and q_out of the cell (+, −).
They agree at Z, the metric being continuous; Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(L̲, L̲) = q_out
on N_i, these being equations along the edges that the two cells satisfy up to their boundaries; and they equal g0's
at the points with ϑ ∉ [2η, π/2 − 2η]. Change the angle by Φ, with (∂_u + b(u, 0, ϑ) ∂_ϑ) Φ = 0 and Φ(0, ϑ) = ϑ, as
in Step 2 of the proof of [[thm:loc-shells]], so that b = 0 on N_i; Φ is the identity where ϑ ∉ [2η, π/2 − 2η]. Apply
[[prop:loc-cone-local]] with the background g0 on the open set 𝒪 of [[sec:civp-large]], Q := Q1 (after the translation),
d ∈ (0, 1] so small that the points within 4d of Q form a compact subset of 𝒪, the rectangle 𝒬, and Λ the largest C^(m_1)
norm of the differences of the transformed functions from g0's: it gives s ∈ (0, λ] and a class solution in the gauge
on [0, s]² × S³ that induces these functions and equals (g0, q̊_in, q̊_out) at the points with ϑ ∉ [η, π/2 − η]; change
the angle back. The extended metric is continuous and cellwise smooth, each closed cell carries a class solution in the
gauge, and (J3) holds, the new cell inducing q_in on N_o and q_out on N_i. By [[prop:loc-shell-junction]] (a), applied
to the extended metric, [∂_v b] on {v = 0} is continuous at Z, where its value from u < 0 vanishes by (J1) for the given
solution; b vanishing near the axes, it vanishes on the new part of the leaf, by the last sentence of (a) with Z in place
of {(0, c_k)} × S³, (J1). By [[prop:loc-shell-junction]] (b) and (c), 𝒱[tr χ] and 𝒱[tr χ̲] are continuous at Z and keep
their signs along the new parts of the two leaves, so 𝔪 := −[tr χ] ≥ 0 and 𝔫 := −[tr χ̲] ≥ 0 continue 𝔪_k and 𝔫_j; by
[[prop:loc-shell-junction]] (d) the extension is a solution with null shells along the leaves. The same transformed functions are cone data on 𝒬 for the band (3η/2, π/2 − 3η/2), in the sense of [[lem:loc-shell-corner-large]], for which η0′ = η/2; by its parts (a) and (b) they have a development on 𝒬_δ for some δ > 0 that equals (g0, q̊_in, q̊_out) at the points with ϑ ∉ [η, π/2 − η], and it is glued in the same way. If g̃ is
a solution on (𝔏 ∪ D″) × S³ as in (c), its restriction to D″, which is smooth since 𝒬 lies in a cell, is a class solution
in the gauge on a past set of 𝒬 that equals g0 near the axes and induces on N_o ∩ D″ and N_i ∩ D″ the functions of the
given solution, the metric functions by continuity and q_in and q_out by (J3) of [[prop:loc-shell-junction]] (d); after
the same change of angle, [[lem:loc-shell-corner-large]] (c) shows that it equals the development on D″ ∩ 𝒬_δ.

(d) The functions tr χ and tr χ̲ are the expansions of the spheres {u, v = const} along the null normal fields ∂_v and
L̲ = −2Ω² g⁻¹dv, which are smooth on each closed cell, the axes included. So the values in (a) extend continuously to the
points of Z on the axes, and the identities of (a) hold there by continuity; likewise the coefficients 𝔖_k and 𝔖′_j of
[[lem:loc-shell-ricci]] are continuous up to the axes, which is how the junction conditions were extended to the axes in
the proof of [[prop:loc-shell-junction]] (d). The remaining assertions of (d) state what is not proved. ∎

**Remark {#rem:loc-shell-scope}** (What this section does not give.) (i) *Measures.* Only finitely many atoms along
leaves, with densities smooth in ϑ, are treated. A density with a continuous singular part in v, atoms on sections
{v = f(ϑ)} of 𝒞_out that are not leaves, whose supports are not null hypersurfaces of the development, and infinitely
many atoms accumulating on a cone are not; [LR20, Theorem 4.6] concerns angularly regular measures in 3 + 1 dimensions
([[rem:loc-cone-scope]] (iii)). Data that are only piecewise smooth, with breaks on finitely many leaves and no atoms,
are covered by [[thm:loc-shells]] with every m_k and n_j zero; a jump of the derivatives of the free data across a leaf
gives no singular part of Ric ([[lem:loc-shell-ricci]] (b)). (ii) *Domains.* The development of [[thm:loc-shells]] lies
in a neighbourhood of the cones on which no two shells cross. [[prop:loc-shell-crossing]] continues a solution through
one crossing sphere, on a small square and on a neighbourhood of the two leaves beyond it; a development on
the whole rectangle Q1, where the shells cross away from the cones, is not asserted, as for smooth data
([[rem:loc-cone-scope]] (iv)). (iii) *Backgrounds with shells.* [[thm:loc-shells]] perturbs the smooth background g0. A
round solution with shells, as in [[prop:loc-shell-crossing]] (b), is smooth only on each cell, and developing
perturbations of it slab by slab needs [[thm:civp-large]] and [[thm:loc-cone-development]] around a round background that
is smooth only on a closed rectangle, which are not stated in this paper. (iv) *The axes.* As in [[rem:loc-cone-scope]]
(ii), the part of the data that is not the background's must avoid the axes; shells that are not round at an axis are not
treated ([[prop:loc-shell-crossing]] (d)). (v) *Uniqueness.* Uniqueness is asserted among solutions with null shells
along the same leaves, smooth on each cell and equal to the background near the axes; among continuous or Lipschitz
metrics with measure-valued densities it is not. (vi) *Limits.* Nothing is asserted about smooth densities that
concentrate on a leaf: their C^m norms, m = 6k + 21, are not bounded as the width of their support tends to 0, so
[[thm:loc-cone-development]] does not apply to them uniformly.

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:". The old texts
are quoted from the chapter sources at the current head, into which the sections of Tiers 1 and 2 are merged
([[sec:loc-cone-proof]] and [[sec:civp-large]], with the texts of their placements); every old text occurs there exactly
once, as whole lines. Line numbers are those of the current chapter sources and serve only to find the place. The
section uses those two sections' results by their labels. It carries them to the other corner spheres in two lemmas of
its own, [[lem:loc-shell-corner-large]] and [[lem:loc-shell-corner-small]], proved from the proofs of [[thm:civp-large]]
and [[thm:loc-cone-development]].

*1. Where the section goes.* The section above, from its heading through [[rem:loc-shell-scope]], is inserted in
[[ch:localised-data]] after the Tier 2 section, which ends with [[rem:civp-large-beyond]], immediately before the
heading "### The static Killing field and the charge {#sec:loc-kid}" (line 2391 of the current source), with one blank
line before and one after; it depends only on the sections of Tiers 1 and 2, and so follows any further section placed
between the Tier 2 section and that heading. It defines sec:loc-shells, def:loc-shell-solution, eq:loc-shell-einstein,
eq:loc-shell-dust, lem:loc-shell-ricci, eq:loc-shell-singular, lem:loc-shell-identities, eq:loc-shell-trace,
prop:loc-shell-junction, eq:loc-shell-torsion, eq:loc-shell-conservation, rem:loc-shell-poisson, def:loc-shell-data,
lem:loc-shell-corner-large, lem:loc-shell-corner-small, prop:loc-shell-cones, thm:loc-shells, eq:loc-shell-bands,
prop:loc-shell-crossing, eq:loc-shell-crossing-rule and rem:loc-shell-scope, none of which is defined elsewhere. Numbers
are resolved at assembly.

*2. [[ch:localised-data]], [[rem:loc-cone-scope]] (iii), its second line (line 681).* Only this line is replaced, so
that the item composes with a placement that rewrites the end of (ii) on the line before it. Old:

that are only bounded, or measures (shells), are not covered. For the 3 + 1 problem with two families of null dust,

New:

that are only bounded, and measure-valued densities in general, are not covered. Finitely many null shells along leaves
{v = c} of 𝒞_out and {u = d} of 𝒞_in, with densities smooth in angle and supported in the band, and data that are smooth
except across finitely many such leaves, are covered by [[thm:loc-shells]]: their development is continuous, smooth
between the leaves and a solution in the sense of distributions ([[def:loc-shell-solution]]), and near the background's
data it exists on a neighbourhood of the two cones that does not depend on the data ([[thm:loc-shells]] (d)). For the
3 + 1 problem with two families of null dust,

*3. [[ch:localised-data]], [[rem:civp-large-domain]], its last sentence (lines 2369–2371).* Old:

are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
or measure-valued.

New:

are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity, densities that are only bounded,
or measure-valued densities other than finitely many null shells along leaves of the two cones with densities smooth in
angle; those, and data that are smooth except across finitely many leaves, are developed slab by slab with
[[thm:civp-large]] in [[thm:loc-shells]].

*4. [[ch:localised-data]], the opening (lines 26–27).* A paragraph is inserted before the last paragraph of the opening,
which neither the Tier 1 nor the Tier 2 placement changes. Old:

The inequalities on the background that these results use are proved at the end of the chapter, in
[[sec:bg-below]] and [[sec:margins]], from the tables of [[sec:tab-bg]] and [[sec:table-margins]].

New:

The developments extend to cone data that carry finitely many null shells along leaves {v = c} of 𝒞_out and {u = d} of
𝒞_in, with densities smooth in angle and supported in a band away from the axes: the development is then continuous,
smooth between the leaves, and a solution of the Einstein–null-dust equations in the sense of distributions with a null
shell along each leaf, and the junction conditions and the conservation laws of the shells follow from the metric of
the double-null gauge ([[thm:loc-shells]], [[prop:loc-shell-junction]]). Where two shells cross, the null expansions
obey a product rule, for round metrics a relation between the masses of the four adjacent regions
([[prop:loc-shell-crossing]]).

The inequalities on the background that these results use are proved at the end of the chapter, in
[[sec:bg-below]] and [[sec:margins]], from the tables of [[sec:tab-bg]] and [[sec:table-margins]].

*5. [[ch:scope]], the paragraph on localised data, its last two lines (lines 217–218), which close the text on the
developments from the two null cones.* The text is appended at the end of the paragraph. Old:

estimate ([[thm:loc-cone-development]]). Developments of cone data that differ from the background's near an axis are
not established ([[rem:loc-cone-scope]]).

New:

estimate ([[thm:loc-cone-development]]). Developments of cone data that differ from the background's near an axis are
not established ([[rem:loc-cone-scope]]). Cone data with finitely many null shells along leaves of the two cones, with
densities smooth in angle and supported in a band away from the axes, have developments that are continuous, smooth
between the shells and solutions in the sense of distributions, on a neighbourhood of the cones on which the shells do
not cross, and a solution continues through a crossing sphere on a small square; general measure-valued densities and
shells that are not round at an axis are not treated ([[thm:loc-shells]], [[prop:loc-shell-crossing]],
[[rem:loc-shell-scope]]).

*6. The references.* New entry, in alphabetical place, before [Rac16] (lines 157–158). Old:

- [Rac16] I. Rácz, *Constraints as evolutionary systems*, Class. Quantum Grav. 33 (2016), 015014.
  doi:10.1088/0264-9381/33/1/015014 arXiv:1508.01810v3

New:

- [Poi02] E. Poisson, *A reformulation of the Barrabès–Israel null-shell formalism*, preprint (2002).
  arXiv:gr-qc/0207101v1
- [Rac16] I. Rácz, *Constraints as evolutionary systems*, Class. Quantum Grav. 33 (2016), 015014.
  doi:10.1088/0264-9381/33/1/015014 arXiv:1508.01810v3

*7. Appendix A.* No new entry. No proof uses a published result as a black box: [Poi02] is quoted in
[[rem:loc-shell-poisson]] for comparison only, its wording checked against the arXiv text (version 1, pp. 1 and 4), and
[LR20, Theorem 4.6] is already quoted in [[rem:loc-cone-scope]] (iii).

*8. [[ch:localised-data]], the paragraph after [[lem:loc-cone-in]] and [[rem:loc-cone-scope]] on the developments of
these cone data (lines 689–705), the last two lines of its last sentence (lines 704–705).* The closing clause is narrowed to the other chapters: [[thm:loc-shells]] applies
[[thm:civp-large]] to restrictions of cone data of this kind and [[thm:loc-cone-development]] to extensions of them, so
"no other result of this paper" would no longer hold. Where another placement rewrites this sentence, the exception for
null shells and the narrowed clause are carried into the merged text. Old:

asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
that are not smooth, and no other result of this paper uses these developments.

New:

asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
that are not smooth, except finitely many null shells along leaves of the two cones and data that are smooth except
across such leaves, which [[thm:loc-shells]] develops slab by slab with [[thm:civp-large]] and
[[thm:loc-cone-development]]; no result of the other chapters uses these developments.

*9. No other change.* No text outside items 1–8 changes. [[ch:two-dusts]], [[ch:class-system]], [[ch:ten-l5]],
[[ch:theorems]] and [[ch:introduction]] need no change: no result there uses the section, and the section uses only
results those chapters state.

### Crosswalk rows

New rows for the crosswalk table of [[ch:localised-data]], one per label, in chapter order, after the rows of the Tier 2
section. Each row is given as one line with its four fields separated by tab characters (label, source, source_name,
note); the source is this file with the line of the label.

sec:loc-shells	paper/reader/proofs/P-SHELL.md:1	proof P-SHELL, section heading	new: leaf-aligned null shells for the characteristic problem of the class (scoping report S-T6, route M1); slabs between the leaves developed by the smooth theorems and glued by the junction
def:loc-shell-solution	paper/reader/proofs/P-SHELL.md:50	proof P-SHELL, Definition (Solutions with null shells along the leaves)	new: continuous, cellwise smooth metric in the gauge; distributional Ricci in charts (u, v, y); measure-valued null dust on the leaves; conservation laws in divergence form; on each cell a class solution in double-null form (Tier 1's class solution in the gauge without the condition near the axes)
eq:loc-shell-einstein	paper/reader/proofs/P-SHELL.md:58	proof P-SHELL, display	Ric(g) = q_in^♯ dv ⊗ dv + q_out^♯ du ⊗ du with the shell measures
eq:loc-shell-dust	paper/reader/proofs/P-SHELL.md:60	proof P-SHELL, display	the conservation laws of the two families in divergence form
lem:loc-shell-ricci	paper/reader/proofs/P-SHELL.md:74	proof P-SHELL, Lemma (The curvature of a continuous, cellwise smooth metric)	new: δ-part of Ric across a null leaf in invariant form; in the gauge −[tr χ] dv² plus a current term in [∂_v b]; no condition across outgoing leaves; checked independently by computer algebra (private)
eq:loc-shell-singular	paper/reader/proofs/P-SHELL.md:81	proof P-SHELL, display	the singular tensors 𝔖_k and 𝔖′_j
lem:loc-shell-identities	paper/reader/proofs/P-SHELL.md:132	proof P-SHELL, Lemma (Two identities)	new: Ric(L̲, ∂_ϑ) from lem:loc-cone-ricci, and the angular trace identity with remainder 𝔞 containing only ϑ-derivatives; formulas of lem:loc-cone-ricci checked independently by computer algebra (private); round check 𝔞 = 6/R²
eq:loc-shell-trace	paper/reader/proofs/P-SHELL.md:140	proof P-SHELL, display	the angular trace identity
prop:loc-shell-junction	paper/reader/proofs/P-SHELL.md:172	proof P-SHELL, Proposition (The junction conditions)	new: (J1) [∂_v b] = 0, (J2) densities −[tr χ], −[tr χ̲], (J3) continuity of the transverse densities; necessary and sufficient; transport of [∂_v b]; conservation of the shell densities (S-T6 3.2 (a)–(d) written symbolically); hypothesis: a class solution in double-null form on each closed cell
eq:loc-shell-torsion	paper/reader/proofs/P-SHELL.md:179	proof P-SHELL, display	homogeneous transport of [∂_v b] along L̲
eq:loc-shell-conservation	paper/reader/proofs/P-SHELL.md:187	proof P-SHELL, display	null-dust conservation law of an ingoing shell
rem:loc-shell-poisson	paper/reader/proofs/P-SHELL.md:268	proof P-SHELL, Remark (Null shells in four dimensions)	comparison with [Poi02, (2.15), p. 4] and [Poi02, p. 1]; Poisson's S^αβ is formed from the singular part of the Einstein tensor, equal here to the δ-part of Ric since 𝔖_k and 𝔖′_j are trace-free; no proof uses it; Barrabès–Israel named only through the title of [Poi02]
def:loc-shell-data	paper/reader/proofs/P-SHELL.md:281	proof P-SHELL, Definition (Cone data with shells)	new: cone data of def:civp-large-data with atoms m_k, n_j and breaks on leaves; jump conditions [∂_v b] = 0, [tr χ] = −m_k, [tr χ̲] = −n_j
prop:loc-shell-cones	paper/reader/proofs/P-SHELL.md:301	proof P-SHELL, Proposition (Free data with atoms)	new: prop:loc-cones and lem:loc-cone-in with measure-valued densities (S-T6 MV-2); [∂_vϕ] = −m_k/3, ∂_v b continuous automatically
thm:loc-shells	paper/reader/proofs/P-SHELL.md:361	proof P-SHELL, Theorem (Developments of cone data with null shells)	new: existence on {min(u, v) ≤ δ} with no crossings, localisation in widened bands, uniqueness among solutions with shells along the same leaves, small-data part with data-independent widths (S-T6 MV-3); uses (T2) and (T1), marked pending; derivative count k_(i−1) = 6k_i + 23, the change of angle back losing no derivative
eq:loc-shell-bands	paper/reader/proofs/P-SHELL.md:366	proof P-SHELL, display	the widened bands, w_i = ½ min(ϑ_a^(i), π/2 − ϑ_b^(i))
prop:loc-shell-crossing	paper/reader/proofs/P-SHELL.md:531	proof P-SHELL, Proposition (Crossing shells)	new: product rule for tr χ tr χ̲ at a crossing sphere; round crossing rule (R² − μ_++)(R² − μ_−−) = (R² − μ_+−)(R² − μ_−+) (S-T6 MV-0); round continuation by the Volterra system; continuation off the axes by prop:loc-cone-local; nothing asserted for shells not round at an axis; the lemma and the junction conditions extended to sets meeting every coordinate line in an interval (𝔏 and its unions); the crossing rule where the domain contains a neighbourhood of the crossing sphere
eq:loc-shell-crossing-rule	paper/reader/proofs/P-SHELL.md:552	proof P-SHELL, display	the crossing rule f_++ f_−− = f_+− f_−+
rem:loc-shell-scope	paper/reader/proofs/P-SHELL.md:663	proof P-SHELL, Remark (What this section does not give)	general measures, domains beyond the cones, backgrounds with shells, axes, uniqueness classes, limits of concentrating densities (S-T6 5.2, open items)
