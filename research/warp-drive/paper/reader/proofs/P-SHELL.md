### Null shells along the leaves {#sec:loc-shells}

This section extends the developments of [[thm:loc-cone-development]] and [[thm:civp-large]] to cone data that carry
finitely many null shells: an atom m(ϑ) δ(v − c) in the density on 𝒞_out, or n(ϑ) δ(u − d) on 𝒞_in, with m and n
smooth in ϑ and supported in the band, the other data being smooth between the atoms. The development is continuous,
smooth between the leaves {v = c} and {u = d} through the atoms, and solves the Einstein–null-dust equations in the sense
of distributions, with a null shell along each such leaf ([[thm:loc-shells]]). Between the leaves it is a smooth
characteristic problem, solved by the smooth theorems; at a leaf the pieces are glued by junction conditions, which are
derived here from the metric [[eq:loc-double-null]] ([[prop:loc-shell-junction]]). Across an ingoing leaf the transverse
derivative ∂_v b of the shift must be continuous, and this holds on the whole leaf once it holds where the leaf meets
𝒞_out; the shell's density is the jump of −tr χ, and it is carried along the leaf by the conservation law of a null
dust. Across an outgoing leaf no condition arises. On the neighbourhood of the cones on which the development is
constructed no two shells cross. Where two shells cross, the null expansions obey a product rule, which for round
metrics is a relation between the masses of the four adjacent regions ([[prop:loc-shell-crossing]]).

*Leaves and cells.* Throughout, g0, Q1 = [0, u_1] × [0, v_1] and the band 0 < ϑ_a < ϑ_b < π/2 are as in
[[sec:civp-large]]: g0 is defined, in the gauge [[eq:loc-double-null]], on a neighbourhood of Q1 × S³. Fix numbers 0 <
c_1 < ⋯ < c_p < v_1 and 0 < d_1 < ⋯ < d_q < u_1, where p, q ≥ 0, and put c_0 := 0, c_(p+1) := v_1, d_0 := 0 and
d_(q+1) := u_1. The sets {v = c_k} (1 ≤ k ≤ p) are the *ingoing leaves*, the sets {u = d_j} (1 ≤ j ≤ q) the *outgoing
leaves*, their intersections the *crossing spheres*, and the rectangles Q_jk := [d_j, d_(j+1)] × [c_k, c_(k+1)] the
*cells*; as in [[sec:loc-cone-setting]], points of the (u, v)-plane stand for the corresponding spheres. Let D ⊂ Q1 be a
past set. A function on D × S³, or off the axes on D × (0, π/2), is *cellwise smooth* if its restriction to the
intersection of that set with each cell is the restriction of a smooth function on a neighbourhood of it; it then has
one-sided values and one-sided derivatives of every order on the leaves. At a point of an ingoing leaf {v = c_k} that is
not on a crossing sphere, the *jump* of a cellwise smooth F is [F] := F(c_k⁺) − F(c_k⁻), the difference of the values
from the cells above and below; across an outgoing leaf {u = d_j}, [F] := F(d_j⁺) − F(d_j⁻). A continuous cellwise
smooth F has the same restriction to a leaf from both sides, so its derivatives along the leaf are continuous across
it: [∂_u F] = [∂_ϑ F] = 0 across an ingoing leaf, [∂_v F] = [∂_ϑ F] = 0 across an outgoing one, and likewise for every
derivative along the leaf.

A metric g on D × S³ is *continuous and cellwise smooth* if it is a continuous G-invariant Lorentzian metric whose
restriction to the intersection of D × S³ with each cell is the restriction of a smooth G-invariant Lorentzian metric on
a neighbourhood of it, and which off the axes has the form [[eq:loc-double-null]] with Ω > 0, γ_ϑ > 0, b, A_c and A_s
continuous and cellwise smooth. Charts (u, v, y), with y = (y¹, y², y³) a chart of S³, cover D × S³, the axes
included. In such a chart the components of g are continuous with locally bounded first derivatives, and its
Christoffel symbols Γ^a_bc are locally bounded and cellwise smooth. Its *Ricci tensor in the sense of distributions* is,
in the chart,

    Ric(g)_bd := ∂_aΓ^a_bd − ∂_dΓ^a_ab + Γ^a_ae Γ^e_bd − Γ^a_de Γ^e_ab,

the derivatives being taken in the sense of distributions on the chart's domain and the products, which are bounded
functions, pointwise. For a number c, δ(v − c) is the distribution φ ↦ ∫ φ(u, c, y) du d³y of the chart, and for a
bounded function F on {v = c}, F δ(v − c) is φ ↦ ∫ F φ(u, c, y) du d³y; likewise δ(u − d).

**Definition {#def:loc-shell-solution}** (Solutions with null shells along the leaves.) Let D ⊂ Q1 be a past set. A
*solution with null shells along the leaves* on D × S³ consists of a continuous and cellwise smooth metric g, the phases
v and u, cellwise smooth densities q_in ≥ 0 and q_out ≥ 0, and *shell densities*: continuous functions 𝔪_k ≥ 0 on (D ∩
{v = c_k}) × S³ (1 ≤ k ≤ p) and 𝔫_j ≥ 0 on (D ∩ {u = d_j}) × S³ (1 ≤ j ≤ q), smooth on the parts of these sets between
consecutive crossing spheres, all of them invariant under G, such that in every chart (u, v, y), on the interior of
D × S³ and in the sense of distributions,

    Ric(g) = q_in^♯ dv ⊗ dv + q_out^♯ du ⊗ du,      q_in^♯ := q_in + Σ_k 𝔪_k δ(v − c_k),
                                                     q_out^♯ := q_out + Σ_j 𝔫_j δ(u − d_j),       {#eq:loc-shell-einstein}

    ∂_a(|det g|^(1/2) q_in^♯ g^(ab) ∂_b v) = 0,      ∂_a(|det g|^(1/2) q_out^♯ g^(ab) ∂_b u) = 0.       {#eq:loc-shell-dust}

In such a chart g^(vv) = g⁻¹(dv, dv) = 0 and g^(uu) = 0, so the first field |det g|^(1/2) g^(ab) ∂_b v has no
∂_v-component and the second no ∂_u-component, and the products with δ(v − c_k) and δ(u − d_j) in [[eq:loc-shell-dust]]
are products of continuous functions with these distributions. The solution *induces* the functions Ω, γ_ϑ, b, A_c, A_s
and q_in of its restriction to 𝒞_out ∩ D, and Ω, γ_ϑ, b, A_c, A_s and q_out of its restriction to 𝒞_in ∩ D, the
densities being one-sided at the leaves.

Away from the leaves [[eq:loc-shell-einstein]] and [[eq:loc-shell-dust]] are the class system [[eq:class-system]] with
the two families of [[sec:loc-cone-setting]]. So on the interior of each cell (g, v, u, q_in, q_out) is a class solution
in the gauge, and by continuity its equations hold on each closed cell for the one-sided values. When p = q = 0 a
solution with null shells is a class solution in the gauge.

**Lemma {#lem:loc-shell-ricci}** (The curvature of a continuous, cellwise smooth metric.) Let g be continuous and
cellwise smooth on D × S³, and let Ric_c(g) be its Ricci tensor on each cell, a locally bounded cellwise smooth tensor.

(a) In every chart (u, v, y), on the interior of D × S³,

    Ric(g) = Ric_c(g) + Σ_k 𝒮_k δ(v − c_k) + Σ_j 𝒮′_j δ(u − d_j),
    𝒮_k := ½ (dv ⊗ Y + Y ⊗ dv) − ½ (tr_g h) dv ⊗ dv,      h := [∂_v g_ab] dx^a ⊗ dx^b,      Y := h(g⁻¹dv, ·),
                                                                                                {#eq:loc-shell-singular}

with the jumps across {v = c_k}, and with 𝒮′_j given by the same formula with u and the jumps across {u = d_j} in place
of v and the jumps across {v = c_k}.

(b) Off the axes, in the coordinates (u, v, ϑ, φ1, φ2), with tr χ and tr χ̲ of [[eq:loc-cone-quantities]],

    𝒮_k = −[tr χ] dv ⊗ dv + (γ_ϑ [∂_v b]/(4Ω²)) (dv ⊗ (dϑ − b du) + (dϑ − b du) ⊗ dv),      𝒮′_j = −[tr χ̲] du ⊗ du.

So 𝒮′_j involves no jump of ∂_u b, and neither 𝒮_k nor 𝒮′_j involves the jumps of the derivatives of ln Ω or of the
ϰ_i − ϕ, ϕ := (ϰ_1 + ϰ_2 + ϰ_3)/3; tr χ = 3 ∂_vϕ, and tr χ̲ = 3 ∂_uϕ wherever b = 0.

*Proof.* (a) Let F be bounded and cellwise smooth on the domain of the chart and φ a test function supported in the
interior of D × S³. For fixed (u, y) the points of D with these coordinates form an interval in v, since D is a past set,
and the numbers c_k cut it into intervals on each of which v ↦ F is smooth with one-sided limits. Integrating by parts
on each of them, and using Fubini's theorem,

    ∫ F ∂_vφ du dv d³y = −∫ {∂_vF} φ du dv d³y − Σ_k ∫ [F] φ(u, c_k, y) du d³y,

{∂_vF} denoting the cellwise derivative; the boundary of D does not enter, as φ vanishes near it, and the crossing
spheres, where [F] is not defined, have measure zero in the leaves. So ∂_vF = {∂_vF} + Σ_k [F] δ(v − c_k); likewise ∂_uF
= {∂_uF} + Σ_j [F] δ(u − d_j), and ∂F/∂y^A = {∂F/∂y^A}, F being smooth in y on each cell. We apply this to the Γ^a_bd.
On {v = c_k}, g is continuous and its derivatives along the leaf are continuous across it, so [∂_e g_ab] = δ^v_e h_ab and

    [Γ^a_bd] = ½ g^(ae) (δ^v_b h_ed + δ^v_d h_eb − δ^v_e h_bd).

With Y_d = g^(ve) h_ed and g^(vv) = 0, [Γ^v_bd] = ½ (δ^v_b Y_d + δ^v_d Y_b), and [Γ^a_ab] = ½ (Y_b + δ^v_b tr_g h − Y_b) =
½ δ^v_b tr_g h. So the coefficient of δ(v − c_k) in Ric(g)_bd is [Γ^v_bd] − δ^v_d [Γ^a_ab] = (𝒮_k)_bd. The products of
the Christoffel symbols are bounded and equal their cellwise values off the leaves, a set of measure zero. The outgoing
leaves are treated in the same way, with g^(uu) = 0.

(b) The functions Ω, γ_ϑ, b and e^(ϰ_i) are continuous, so the nonzero components of h are

    h_uv = −4Ω² [∂_v ln Ω],   h_uu = b² [∂_vγ_ϑ] + 2γ_ϑ b [∂_v b],   h_uϑ = −b [∂_vγ_ϑ] − γ_ϑ [∂_v b],
    h_ϑϑ = [∂_vγ_ϑ],   h_(φiφi) = 2 e^(2ϰ_(i+1)) [∂_vϰ_(i+1)].

By the inverse metric of the proof of [[lem:loc-cone-equations]], g⁻¹dv = −(2Ω²)⁻¹ L̲, L̲ = ∂_u + b∂_ϑ, so Y_d =
−(2Ω²)⁻¹ (h_ud + b h_ϑd): Y_u = −(2Ω²)⁻¹ γ_ϑ b [∂_v b], Y_v = 2[∂_v ln Ω], Y_ϑ = (2Ω²)⁻¹ γ_ϑ [∂_v b] and Y_(φi) = 0, that
is

    Y = 2 [∂_v ln Ω] dv + (γ_ϑ [∂_v b]/(2Ω²)) (dϑ − b du).

Since g^(ab) ∂_v g_ab = ∂_v ln |det g| on each side and |det g|^(1/2) = 2Ω²𝒱 ([[lem:loc-cone-ricci]] (b)), with ∂_v ln 𝒱
= tr χ, tr_g h = [∂_v ln |det g|] = 4[∂_v ln Ω] + 2[tr χ]. Substituting in [[eq:loc-shell-singular]] gives 𝒮_k. Across an
outgoing leaf, h′ := [∂_u g_ab] dx^a ⊗ dx^b has h′(∂_v, ∂_d) = 0 for d ≠ u and h′_vu = −4Ω² [∂_u ln Ω], and g⁻¹du =
−(2Ω²)⁻¹ ∂_v; so Y′ := h′(g⁻¹du, ·) = 2[∂_u ln Ω] du and tr_g h′ = 4[∂_u ln Ω] + 2[∂_u ln 𝒱], and 𝒮′_j = −[∂_u ln 𝒱] du ⊗
du. Finally ∂_u ln 𝒱 = L̲ ln 𝒱 − b ∂_ϑ ln 𝒱 = tr χ̲ − ∂_ϑ b − b ∂_ϑ ln 𝒱, and ∂_ϑ b and b ∂_ϑ ln 𝒱 are continuous across
{u = d_j}; so [∂_u ln 𝒱] = [tr χ̲]. ∎

The next two identities hold for every metric of the form [[eq:loc-double-null]]; they are read off from
[[eq:loc-cone-frame-ricci]]. For a round metric the second is the angular part of [[lem:two-dust-equations]].

**Lemma {#lem:loc-shell-identities}** (Two identities.) Let g have the form [[eq:loc-double-null]] off the axes, with
smooth functions, and let L̲, 𝒱, η, χ_i, χ̲_i, tr χ and tr χ̲ be as in [[eq:loc-cone-quantities]] and K_i = ∂_(φi). Then

    Ric(L̲, ∂_ϑ) = −(γ_ϑ/(4Ω²)) (L̲∂_v b + (L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) + 2∂_ϑ b) ∂_v b) + r̲,

with r̲ of [[eq:loc-cone-frame-ricci]], and

    γ_ϑ⁻¹ Ric(∂_ϑ, ∂_ϑ) + Σ_(i=1,2) e^(−2ϰ_(i+1)) Ric(K_i, K_i)
        = (Ω²𝒱)⁻¹ (L̲∂_v𝒱 + (∂_ϑ b) ∂_v𝒱 + ½ ∂_ϑ(𝒱 ∂_v b)) − (γ_ϑ/(8Ω⁴)) (∂_v b)² + 𝔞,                {#eq:loc-shell-trace}

    𝔞 := −γ_ϑ⁻¹ Σ_(i=2,3) (∂_ϑ²ϰ_i + (∂_ϑϰ_i)² − ∂_ϑϰ_1 ∂_ϑϰ_i) − 2γ_ϑ⁻¹ (∂_ϑη + η² − ∂_ϑϰ_1 η)
          − (Ω²𝒱)⁻¹ Σ_(i=2,3) ∂_ϑ(Ω²𝒱 γ_ϑ⁻¹ ∂_ϑϰ_i).

The function r̲ contains derivatives of Ω, γ_ϑ, b, A_c, A_s only along L̲ and ∂_ϑ, and 𝔞 only along ∂_ϑ. For a round
metric, b = 0, γ_ϑ = R², e^(A_c) = R cos ϑ, e^(A_s) = R sin ϑ and Ω² = e^(2σ)/2, one finds 𝔞 = 6/R², and
[[eq:loc-shell-trace]] reads (6e^(−2σ)/R²)(R R_uv + 2R_u R_v + e^(2σ)), the angular trace of [[lem:two-dust-equations]].

*Proof.* Take q_in = q_out = 0 in [[lem:loc-cone-ricci]], so that E = Ric there. The first identity is the formula for
E(L̲, ∂_ϑ) in [[eq:loc-cone-frame-ricci]]; r̲ is built from η = ∂_ϑ ln Ω, the ∂_ϑϰ_i, the χ̲_i, ∂_ϑL̲ ln Ω and the
∂_ϑχ̲_i, and χ̲_1 = L̲ϰ_1 + ∂_ϑ b, χ̲_i = L̲ϰ_i for i = 2, 3. For the second, [[eq:loc-cone-frame-ricci]] gives, for
i = 1, 2, since ∂_vL̲ϰ_(i+1) = ∂_vχ̲_(i+1),

    e^(−2ϰ_(i+1)) Ric(K_i, K_i) = −□_g ϰ_(i+1) = Ω⁻² (∂_vχ̲_(i+1) + ½ (tr χ̲ χ_(i+1) + tr χ χ̲_(i+1) − ∂_v b ∂_ϑϰ_(i+1)))
                                   − (Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 γ_ϑ⁻¹ ∂_ϑϰ_(i+1)),

and γ_ϑ⁻¹ Ric(∂_ϑ, ∂_ϑ) is Ω⁻² (∂_vχ̲_1 + ½ (tr χ χ̲_1 + χ_1 tr χ̲) − ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b)) − (γ_ϑ/(8Ω⁴))(∂_v b)²
plus the first two terms of 𝔞. In the sum, ½ (tr χ χ̲_1 + χ_1 tr χ̲) + ½ Σ_(i=2,3) (tr χ̲ χ_i + tr χ χ̲_i) = tr χ tr χ̲
and e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b) + ∂_v b ∂_ϑ(ϰ_2 + ϰ_3) = 𝒱⁻¹ ∂_ϑ(𝒱 ∂_v b), so the left side of [[eq:loc-shell-trace]] is
Ω⁻² (∂_v tr χ̲ + tr χ tr χ̲ − ½ 𝒱⁻¹ ∂_ϑ(𝒱 ∂_v b)) − (γ_ϑ/(8Ω⁴))(∂_v b)² + 𝔞. Since ∂_v𝒱 = 𝒱 tr χ, 𝒱 tr χ̲ = L̲𝒱 + 𝒱
∂_ϑ b, and ∂_vL̲ = L̲∂_v + (∂_v b) ∂_ϑ as operators,

    𝒱 (∂_v tr χ̲ + tr χ tr χ̲) = ∂_v(𝒱 tr χ̲) = L̲∂_v𝒱 + (∂_v b) ∂_ϑ𝒱 + (∂_ϑ b) ∂_v𝒱 + 𝒱 ∂_ϑ∂_v b
                             = L̲∂_v𝒱 + (∂_ϑ b) ∂_v𝒱 + ∂_ϑ(𝒱 ∂_v b),

