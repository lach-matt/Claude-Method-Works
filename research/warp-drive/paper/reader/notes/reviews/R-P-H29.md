# R-P-H29: independent reading of proofs/P-H29.md (L2 wave gauge, L9 double-null conversion)

File read: `git show 77c50d0d:research/warp-drive/paper/reader/proofs/P-H29.md`, md5 af8f59071e5deb5d3e13cd7e896b52f7,
896 lines (chapter text lines 1-806, Placement 808-848, crosswalk rows 850-896). All line numbers below are lines of
that file. Pending P-F123 labels checked against proofs/P-F123.md md5 136974866398756b795a9175460c7675. HEAD at the time
of reading: ffd472cd (chapter 87 unchanged since 77c50d0d). The subsection the writer is adding for the wave-gauge
data, and the [[pending:wave-gauge-data]] marker itself, are out of scope.

## Verdict

**NOT CONFIRMED.** 2 Major, 8 minor, 9 nits. Both Majors are in the places the writer named as weakest (the past-side
identification and the gluing of prop:tl5-wg-local); both have short repairs, given exactly below. Everything else in
L2 and L9 re-derives, including every explicit constant.

## Major

### M1. lem:tl5-wg-nullfn is false at the corner S, and Step 2 of prop:tl5-wg-local uses it there (lines 372-378, 386-391, 442-446)

*What is wrong.* The lemma asserts, for every q ∈ 𝒱 ∩ N₁, an open neighbourhood U of q with {ũ = −10} = U ∩ N₁ and
{ũ < −10} = U ∩ {u < −10} (line 375), and that U ∩ {u < −10} is a past set (line 377). For q ∈ S (v(q) = 1/2) this
cannot hold: {ũ = −10} is a level set of a function with dũ ≠ 0, a hypersurface without boundary in U, while
U ∩ N₁ = U ∩ {u = −10, v ≥ 1/2} has the boundary S. In the proof (lines 386-388) the curves λ ↦ Θ(−10, λ, y) with
λ < 0 leave N₁ into {v < 1/2}, where {u = −10} need not be null for G; so below v = 1/2 the hypersurface {ũ = −10} is
in general not {u = −10}, and {u < −10} need not be a past set there. The same holds for the N₀⁺ statement at q ∈ S.
This case is used: in part (a) (the case s = 1/2) every q ∈ K_(1/2) = S, and Step 2 (lines 443-446) obtains
R_q = U_q ∖ Q₊ as {ũ < −10} ∪ {ṽ < 1/2} ∪ ({τ₁ < u*} ∩ {τ₂ < 1/2}) from the false identities. Steps 4-5 need exactly
that each point of R_q lies in one of three past sets contained in R_q. So (F1_W) is not proved as written. The
conclusion is true, and the repair below proves it: with U a coordinate box and ∂_uũ > 0, ũ = −10 on U ∩ N₁, the sign
of ũ + 10 on U ∩ {v ≥ 1/2} is that of u + 10 (likewise ṽ − 1/2 on U ∩ {u ≥ −10}), and the quadrant
{u < −10, v < 1/2}, which neither null set need cover, lies in {τ₁ < u*} ∩ {τ₂ < 1/2}. Away from S the lemma as stated
is correct (there U ⊂ {v > 1/2}, resp. U ⊂ {u > −10}); note also that it needs v(q) < v* (resp. u(q) < u⁺), which
holds where it is used.

*Replacement 1* (lines 372-378, the statement), new text:

    **Lemma {#lem:tl5-wg-nullfn}** (Null functions near N.) Let G be a smooth Lorentzian metric on an open set 𝒱 ⊂ 𝒪̂, and
    q ∈ 𝒱 ∩ N₁ with v(q) < v*. Suppose that the tangent spaces of N₁ ∩ 𝒱 are degenerate for G with kernel spanned by ∂_v,
    and that du(V) ≥ 0 for every future directed G-causal vector V at points of N₁ ∩ 𝒱. Then there are an open
    neighbourhood U ⊂ 𝒱 of q that is a coordinate box (u(q) − a, u(q) + a) × (v(q) − a, v(q) + a) × U′, U′ open in S³, and
    a smooth function ũ on U with G⁻¹(dũ, dũ) = 0, ∂_uũ > 0, ũ = −10 on U ∩ N₁ and dũ(V) ≥ 0 for every future directed
    G-causal V on U; so ũ does not increase along past directed G-causal curves in U, {ũ < −10} is a past set in U, and on
    U ∩ {v ≥ 1/2} the sign of ũ + 10 is that of u + 10. If v(q) > 1/2, U may be taken in {v > 1/2}, and then
    {ũ < −10} = U ∩ {u < −10} and {ũ = −10} = U ∩ N₁. Likewise, let q ∈ 𝒱 ∩ N₀⁺ with u(q) < u⁺, let the tangent spaces of
    N₀⁺ ∩ 𝒱 be degenerate for G with kernel spanned by a vector field e with du(e) = 1, and let dv(V) ≥ 0 for every future
    directed G-causal V at points of N₀⁺ ∩ 𝒱. Then there are such a box U and a smooth function ṽ on U with
    G⁻¹(dṽ, dṽ) = 0, ∂_vṽ > 0, ṽ = 1/2 on U ∩ N₀⁺ and dṽ(V) ≥ 0 for every future directed G-causal V on U; so
    {ṽ < 1/2} is a past set in U, and on U ∩ {u ≥ −10} the sign of ṽ − 1/2 is that of v − 1/2. If u(q) > −10, U may be
    taken in {u > −10}, and then {ṽ < 1/2} = U ∩ {v < 1/2} and {ṽ = 1/2} = U ∩ N₀⁺.

*Replacement 2* (lines 386-388), old text:

    point onto a neighbourhood U of q; put ũ := c ∘ Θ⁻¹. For c = −10 the curves λ ↦ Θ(−10, λ, y) are null geodesics
    tangent to ∂_v at their initial points, so they are reparametrised generators of N₁ (the generators of a null
    hypersurface are null pregeodesics), and for U small {ũ = −10} = U ∩ N₁. The level sets of ũ are null: their tangent

new text:

    point onto a neighbourhood U of q; put ũ := c ∘ Θ⁻¹. For c = −10 the curves λ ↦ Θ(−10, λ, y) are null geodesics
    tangent to ∂_v at their initial points, so their arcs in N₁ (λ ≥ 0, and all λ if v_q > 1/2) are reparametrised
    generators of N₁ (the generators of a null hypersurface are null pregeodesics); for U small these arcs cover U ∩ N₁, so
    ũ = −10 on U ∩ N₁, and {ũ = −10} = U ∩ N₁ if v_q > 1/2. The level sets of ũ are null: their tangent

*Replacement 3* (lines 390-391), old text:

    J(G(J₀, J₀))/2 = 0 with G(J, J₀) = 0 at λ = 0, as K is normal to 𝒮_c; so G⁻¹(dũ, dũ) = 0. As dũ(∂_u) = 1 at q,
    dũ = ϱ du on U ∩ N₁ with ϱ > 0 for U small, which gives the two descriptions of the sides and dũ(V) ≥ 0 on U ∩ N₁;

new text:

    J(G(J₀, J₀))/2 = 0 with G(J, J₀) = 0 at λ = 0, as K is normal to 𝒮_c; so G⁻¹(dũ, dũ) = 0. As dũ(∂_u) = 1 at q, for
    U small ∂_uũ > 0 on U and dũ = ϱ du on U ∩ N₁ with ϱ > 0, which gives dũ(V) ≥ 0 on U ∩ N₁. Shrinking U to a box as
    stated, ũ = −10 at the points (−10, v, y) of U with v ≥ 1/2 and ∂_uũ > 0 give the sign of ũ + 10 on U ∩ {v ≥ 1/2},
    and, if v_q > 1/2 and a < v_q − 1/2, the description of {ũ < −10};

(Line 392 continues unchanged: "since dũ is a nowhere vanishing null covector field on U, taken connected, …".)

*Replacement 4* (lines 442-446, Step 2), old text:

    On 𝒱_q ∩ Q₊ ∩ {τ₁ < u*} ∩ {τ₂ < s} ⊂ D^κ_s, Ric^W(G_q) = 0 = F_q; so Ric^W(G_q) = F_q on R_q. By
    [[lem:tl5-wg-domains]] (c) and (W1), [[lem:tl5-wg-nullfn]] applies to G_q at q if q ∈ N₁ or q ∈ N₀ (both if q ∈ S);
    shrinking 𝒱_q to a neighbourhood U_q of q on which the null functions ũ, ṽ of that lemma exist, R_q is the union of the
    sets {ũ < −10} (if q ∈ N₁), {ṽ < 1/2} (if q ∈ N₀) and {τ₁ < u*} ∩ {τ₂ < s}, each of which is a past set in U_q for
    G_q: along past directed causal curves ũ, ṽ, τ₁ and τ₂ do not increase ([[lem:tl5-wg-domains]] (b)).

new text:

    On 𝒱_q ∩ Q₊ ∩ {τ₁ < u*} ∩ {τ₂ < s} ⊂ D^κ_s, Ric^W(G_q) = 0 = F_q; so Ric^W(G_q) = F_q on R_q. By
    [[lem:tl5-wg-domains]] (c) and (W1), [[lem:tl5-wg-nullfn]] applies to G_q at q if q ∈ N₁ or q ∈ N₀ (both if q ∈ S);
    shrinking 𝒱_q to a coordinate box U_q about q on which the null functions ũ, ṽ of that lemma exist, R_q is the union
    of the sets {ũ < −10} (if q ∈ N₁), {ṽ < 1/2} (if q ∈ N₀) and U_q ∩ {τ₁ < u*} ∩ {τ₂ < s}. If q ∉ S, this is the
    description of {ũ < −10} or of {ṽ < 1/2} in that lemma. If q ∈ S, then s = 1/2 and R_q = U_q ∖ Q₊; by the signs of
    ũ + 10 on U_q ∩ {v ≥ 1/2} and of ṽ − 1/2 on U_q ∩ {u ≥ −10}, the first two sets do not meet Q₊ and contain
    U_q ∩ {u < −10} ∩ {v ≥ 1/2} and U_q ∩ {u ≥ −10} ∩ {v < 1/2} respectively, and U_q ∩ {u < −10} ∩ {v < 1/2} lies in
    the third set, as τ₁ < −10 < u* and τ₂ < 1/2 there. Each of the three sets is a past set in U_q for G_q: along past
    directed causal curves ũ, ṽ, τ₁ and τ₂ do not increase ([[lem:tl5-wg-domains]] (b)).

(Minor m4 below makes lem:tl5-wg-domains (c) cover the points of N₀⁺, which this step uses at q ∈ N₀ with u(q) = u*.
The crosswalk note of lem:tl5-wg-nullfn, "N1 (or N0+) as a level set", should then read "N1 (or N0+) as a level set
away from S".)

### M2. Step 6 of prop:tl5-wg-local claims δ̃ = 0 on {τ₂ ≤ s}, which fails at points of K_s on the face {τ₁ = u*} (lines 477-486, 490)

*What is wrong.* Step 5 gives g_q = g = g_(q′) on D^κ_s only. Near a point p ∈ K_s with τ₁(p) = u* and p ∉ N₀ (such
points exist for every s ∈ (1/2 + κ(u* + 10), v*)), Q₊ ∩ {τ₂ ≤ s} contains the points with τ₁ > u*, which are not in
D^κ_s. There g_q and g_(q′) are the solutions of two Cauchy problems with different extensions G_q, G_(q′) of g across
{τ₁ = u*} as data, and nothing makes them agree. So "vanishes on {τ₂ ≤ s}" (line 478) is unproved there, the
hypothesis supp δ̃ ⊂ {τ > −ε′} of lem:ii-f-1-3 (lines 485-486) fails, and the conclusion "g_i = g_j on Q₊ ∩ O_ij"
(line 490) is not established. Only agreement on Q₊ ∩ {τ₁ ≤ u*} is needed, since D^κ_(s′) ⊂ {τ₁ ≤ u*}, and this
follows by running the argument on 𝒞_p ∩ {τ₁ < u*}, with {τ₁ < u*} as a past set. (Taking X inside {τ₁ < u*} also
removes the need for flatness of δ at the points of N₀⁺ ∖ N₀ near the corner (u*, 1/2), which line 477 does not supply.)

*Replacement 1* (lines 477-480), old text:

    all its derivatives at the points of N, since by Step 4 and (P2) both metrics equal G^♯ to infinite order there. So
    δ̃ := δ on Q₊ and δ̃ := 0 off Q₊ is smooth near p ([[pending:lem-tl5-cip-extend]] (c)), vanishes on {τ₂ ≤ s}, and
    satisfies 2𝔓̃δ̃ = 0 for the operator 𝔓̃ of the proof of [[prop:tl5-wg-unique]] built from g_q and g_(q′), with
    principal part −(1/2) g_q^(λμ) ∂_λ∂_μ: on Q₊ as both are solutions, and off Q₊ as δ̃ = 0. In the chart of

new text:

    all its derivatives at the points of N, since by Step 4 and (P2) both metrics equal G^♯ to infinite order there. So
    δ̃ := δ on Q₊ and δ̃ := 0 off Q₊ is smooth on {τ₁ < u*} near p ([[pending:lem-tl5-cip-extend]] (c)), vanishes on
    {τ₁ < u*} ∩ {τ₂ ≤ s}, as Q₊ ∩ {τ₁ < u*} ∩ {τ₂ ≤ s} ⊂ D^κ_s, and satisfies 2𝔓̃δ̃ = 0 for the operator 𝔓̃ of the
    proof of [[prop:tl5-wg-unique]] built from g_q and g_(q′), with principal part −(1/2) g_q^(λμ) ∂_λ∂_μ: on Q₊ as both
    are solutions, and off Q₊ as δ̃ = 0. In the chart of

*Replacement 2* (lines 485-486), old text:

    C_c bounds |dz/dτ| along g_q-causal curves, as g_q is within η″ ≤ η′ of G_q. As in Step 4, with X := 𝒞_p, no past
    sets other than X, and c := −ε′, [[lem:ii-f-1-3]] gives δ̃ = 0 on 𝒞_p, a neighbourhood of p.

new text:

    C_c bounds |dz/dτ| along g_q-causal curves, as g_q is within η″ ≤ η′ of G_q. As in Step 4, with
    X := 𝒞_p ∩ {τ₁ < u*}, the past set {τ₁ < u*}, on which τ₁ ≤ τ₁(p′) along past directed causal curves from p′, and
    c := −ε′, [[lem:ii-f-1-3]] gives δ̃ = 0 on X; so g_q = g_(q′) on Q₊ ∩ {τ₁ ≤ u*} ∩ 𝒞_p, by continuity, and 𝒞_p is a
    neighbourhood of p.

*Replacement 3* (lines 489-491), old text:

    such that the 𝒲″_j cover the compact set K_s, and let g_j be the local solutions. For each i, j the compact set K_s ∩
    𝒲̄″_i ∩ 𝒲̄″_j ⊂ 𝒲′_i ∩ 𝒲′_j is covered by finitely many of the neighbourhoods of Step 6, so g_i = g_j on Q₊ ∩ O_ij for
    an open set O_ij containing it. With Y_(s′) the closure of D^κ_(s′) ∖ D^κ_s, the compact sets Y_(s′) ∩ 𝒲̄″_i ∩ 𝒲̄″_j

new text:

    such that the 𝒲″_j cover the compact set K_s, and let g_j be the local solutions. For each i, j the compact set K_s ∩
    𝒲̄″_i ∩ 𝒲̄″_j ⊂ 𝒲′_i ∩ 𝒲′_j is covered by finitely many of the neighbourhoods of Step 6, so g_i = g_j on
    Q₊ ∩ {τ₁ ≤ u*} ∩ O_ij for an open set O_ij containing it. With Y_(s′) the closure of D^κ_(s′) ∖ D^κ_s, the compact sets
    Y_(s′) ∩ 𝒲̄″_i ∩ 𝒲̄″_j

(Line 492 continues unchanged with "and Y_(s′) ∖ ⋃_j 𝒲″_j decrease, …"; the well-definedness at line 494 then holds
because D^κ_(s′) ∖ D^κ_s ⊂ Q₊ ∩ {τ₁ ≤ u*}.)

## minor

### m1. lem:tl5-wg-cauchy does not say in which coordinates "components" are measured (lines 321-326, 333)

η′ is fixed in (i) by conditions on (τ, z)-components of g′⁻¹, the bound "|g′ − G| ≤ η′ in components" (line 333)
names no chart, while (ii)-(iii) bound the (u, v, y)-components w by ϒ (|ϒ(w)| ≤ ε₂ = η″, "maximum of the
components"). Steps 3 and 6 of prop:tl5-wg-local use the conclusion "within η″ of G_q in components". The two
component systems differ by the Jacobian of the chart, so the proof needs one fixed choice; (u, v, y) makes (i)-(v)
consistent, η′ being still found by continuity and compactness. Replace lines 321-326 by:

    K₀ := [−r₀, r₀] × B̄_(r₀), B̄_r the closed Euclidean ball of radius r about 0, every vector V that is causal for some
    symmetric 2-tensor g′ whose components in the coordinates (u, v, y) of 𝒬 differ from those of G by at most a number
    η′ ∈ (0, 1], fixed in the proof, satisfies |V^z| ≤ C_c |V^τ|. For every η″ ∈ (0, η′] there is
    ε₀ ∈ (0, r₀/(16 C_c)] such that for every ε ∈ (0, ε₀] there is a smooth Lorentzian metric g on
    𝒲_ε := (−2ε, ε) × B_(r₀/2) with Ric^W(g) = F on 𝒲_ε, with g and its first partial derivatives equal to those of G on
    𝒲_ε ∩ {τ = −ε}, and with the components of g − G in the coordinates (u, v, y) at most η″ on 𝒲_ε.

and lines 333-335 by:

    also for every g′ with |g′ − G| ≤ η′ in the components in (u, v, y) at points of K₀, and such that these g′ are
    Lorentzian with −g′^(ττ) ≥ c₀ and g′^(ab) ξ_a ξ_b ≥ c₀ |ξ|². Then |V^z|/|V^τ| is bounded on the compact set of such
    (p, g′, V) with V causal for g′ and |V^τ|² + |V^z|² = 1; let C_c ≥ 1 be a bound.

### m2. Two claims after def:tl5-wg-data are not proved (lines 203-208)

(a) "so the data g_N satisfy the constraints" (lines 204-205). Ric(G^♯) = 0 on N⁺ gives Ric(e₄, e₄) = 0 on N₁ and
Ric(e₃, e₃) = 0 on N₀ for g_N, through (W1) and (W3) (these depend only on γ, the non-affinity and b on N₀). It does not
give Ric(e₄, ∂_A) = 0 for g_N on N₁: that constraint involves the shift b of g_N along N₁, which is not a tangential
component on N₁, so (W1) does not tie it to G^♯, and (W3) fixes the torsion only at S. The claim is not needed (the
constraints are assumed in def:tl5-wg-data), so it should be removed. (The writer's report item 3 is right that the
proof of (F4_W) uses no constraint hypothesis; it is not right that the constraints follow from (W2).)

(b) "by [[lem:tl5-wg-jets]] below, any two choices of G^♯ have the same values and the same derivatives of all orders at
N" (lines 207-208). lem:tl5-wg-jets assumes g₁ = g₂ at the points of N; (W1) fixes only the tangential components, so
equality of the values is not given by that lemma (it would need the transport of the remaining components along the
generators from S under (W2)-(W3), which is not written).

Replace lines 203-208 by:

    By (W1), N₀⁺ and N₁ are null for G^♯, with null directions e₃ and ∂_v. By (W2), Ric(G^♯) also vanishes to infinite
    order on N⁺, as Ric(G^♯) − Ric^W(G^♯) is linear in Υ(G^♯) and its first derivatives; and (W2) says in addition that
    the coordinates are wave coordinates relative to ĝ along N⁺, to infinite order. The existence of data in the wave
    gauge for the data of [[pending:cor-tl5-cip-staged]] (a) is the content of [[pending:wave-gauge-data]]: by
    [[lem:tl5-wg-jets]] below, two choices of G^♯ that agree at the points of N have the same derivatives of all orders
    there, so only the field G^♯|_N enters, and G^♯ is needed only near N.

### m3. prop:tl5-wg-vacuum (c) applies lem:tl5-wg-jets to G^♯, which is not defined on D^κ_s (lines 214-217, 288)

The lemma takes g₁, g₂ "smooth Lorentzian metrics on D^κ_s"; G^♯ lives on 𝒰^♯, an open set containing N⁺, not
necessarily containing D^κ_s. The proof of the lemma uses the metrics only along N. Replace lines 214-217 by:

    **Lemma {#lem:tl5-wg-jets}** (Transverse derivatives on N.) Let s ∈ (1/2, v*], 𝒰 an open set containing N ∩ D^κ_s,
    and g₁, g₂ smooth Lorentzian metrics on D^κ_s ∩ 𝒰 such that every partial derivative of Ric^W(g₁) and of Ric^W(g₂)
    vanishes on N ∩ D^κ_s, g₁ = g₂ at every point of N ∩ D^κ_s, and N₀ and N₁ are null for g₁, with null directions e₃
    and ∂_v. Then every partial derivative of g₁ − g₂ vanishes on N ∩ D^κ_s.

and lines 288-289 by:

    *Proof.* (c) is [[lem:tl5-wg-jets]] with 𝒰 := 𝒰^♯, since Ric^W(G^♯) vanishes to infinite order on N by (W2); (W1) and
    (W3) involve only the values and the first derivatives of the metric on N.

(prop:tl5-wg-unique applies the lemma with 𝒰 = 𝒬, unchanged.)

### m4. lem:tl5-wg-domains (c) is stated on N₀ but used on N₀⁺ (lines 146-148, 167-169)

Step 2 of prop:tl5-wg-local applies lem:tl5-wg-nullfn (second statement) at q ∈ N₀ with u(q) = u*, whose hypotheses
are needed at the points of N₀⁺ near q, beyond u*; the hypothesis dv(V) ≥ 0 there is lem:tl5-wg-domains (c), stated
only for p ∈ N₀. Its proof uses only that p lies on {v = 1/2} (dv(e) = 0, du(e) = 1). Replace lines 146-148 by:

    future directed null at p, and du(V) ≥ 0 for every future directed g-causal vector V at p. Likewise, if p ∈ X lies on
    {v = 1/2} and the tangent space of {v = 1/2} at p is degenerate for g with kernel spanned by a vector e with
    du(e) = 1, then e is future directed null at p and dv(V) ≥ 0 for every future directed g-causal V at p.

and lines 167-169 by:

    1/(8Ω̂²) and ĝ^(uv) = −1/(2Ω̂²), λ < 0. For future directed causal V, g(∂_v, V) ≤ 0, so du(V) = λ g(∂_v, V) ≥ 0. At
    a point of {v = 1/2} the same argument with e, for which dτ₂(e) = κ > 0, with g⁻¹(dv) = g^(uv) e and dv(V) =
    g^(uv) g(e, V), gives the second statement.

### m5. rem:tl5-wg-continuation understates what the proof of lem:tl5-continuation uses (lines 515-518)

The closedness step of lem:tl5-continuation (chapter 87, lines 1212-1221 at HEAD) also uses that D_(s̄) is the closure
of ⋃_(s<s̄) D_s, that smooth functions there with bounded derivatives extend smoothly to D_(s̄), and that the conditions
defining a solution pass to such limits. For D^κ_s and the reduced problem these hold (the sets are convex in (u, v),
and |g⁻¹ − ĝ⁻¹| ≤ κ_m, Ric^W(g) = 0 and g = G^♯ on N are closed conditions), but the remark says "only". Replace lines
515-518 by (line 519 "bound y ≤ 2A must imply. …" unchanged):

    **Remark {#rem:tl5-wg-continuation}** (Use in the continuation argument.) The proof of [[lem:tl5-continuation]] uses of
    the regions D_s only that they increase with s, that a solution on D_s restricts to solutions on D_σ, σ < s, that
    D_(s̄) is the closure of ⋃_(s<s̄) D_s and a smooth function on that union whose derivatives of every order are bounded
    extends smoothly to D_(s̄), that the conditions defining a solution pass to such limits, and (F1)–(F3). The regions
    D^κ_s and the solutions of the reduced problem have these properties, the tilt |g⁻¹ − ĝ⁻¹| ≤ κ_m being a closed
    condition, and [[thm:tl5-wg]] supplies (F1)–(F3), with the strict tilt in (F3_W) as an extra hypothesis that an a priori

### m6. The method of sec:tl5-wg-existence is attributed to [CP12, Section 2, pp. 2-5], which does not describe it (lines 312, 847-848)

Read on alphaXiv (arXiv:1203.4534v2): CP12 Section 2 (pp. 2-5) reviews Rendall's constraint hierarchy in harmonic
coordinates and states Rendall's theorem (Theorem 2.1, p. 5); it does not describe building a metric equal to the data
to infinite order, cutting off its residual as a forcing term, and identifying on the past side. That is Rendall's
reduction, which the edition already cites as [Ren90, p. 221] for the same method in chapter 83 (line 711 at HEAD,
with the quotation "A method is described by means of which the characteristic initial value problem can be reduced to
the Cauchy problem …"). Replace in line 312 "by the method of [CP12, Section 2, pp. 2–5]:" by "by Rendall's method
([Ren90, p. 221]):" (the line becomes "Existence is reduced to the Cauchy problem, by Rendall's method ([Ren90, p. 221]):
near the boundary of the", 107 characters), in Placement item 5 (lines 847-848) replace "[CP12, Section 2, pp. 2–5] is
cited for the method" by "[Ren90, p. 221] is cited for the method", and in the crosswalk row sec:tl5-wg-existence
replace "method of CP12 Section 2 (Rendall)" by "method of Ren90 (Rendall)".

### m7. "The reflection ϑ ↦ −ϑ is ρ₂ restricted to M_σ" is false (lines 748-749)

ρ₂ : (z₁, z₂) ↦ (z₁, z̄₂) fixes M_σ pointwise (M_σ is the common fixed set of ρ₁ and ρ₂, lem:tl5-dn-geodesic (a)). On
M_σ, ϑ ↦ −ϑ is the rotation by π of z₂, and ϑ ↦ π − ϑ the rotation by π of z₁ (ρ₁ composed with it acts the same way
on M_σ, so the second half of the sentence is correct but roundabout), as in the proof of lem:tl5-cip-axis (a). The
argument that follows is right with these maps. Replace line 749 "is ρ₂ restricted to M_σ, and ϑ ↦ π − ϑ is ρ₁
composed with the rotation by π of z₁; both are isometries of g_σ and ĝ_σ" by:

    is the rotation by π of z₂ restricted to M_σ, and ϑ ↦ π − ϑ the rotation by π of z₁; both are isometries of g_σ and ĝ_σ

### m8. The description of D_Y F̂ at Y = Ŷ is false for β̂ ≠ 0 (lines 611-615)

At Ŷ, Ẋ = (1, 0, β̂) = ê, and the entries of D_Y F̂ are Γ̂^μ_αβ ê^β and first derivatives of Γ̂^μ_αβ ê^α ê^β, with
coefficients in β̂; for the ingoing family (β̂ = dϑ(b̂)) they contain Γ̂^μ_zα, not only Γ̂^μ_tα. The (z, q) entry
Γ̂^t_tt − 2Γ̂^z_tz and 2Γ̂^z_tz = ∂_t ln ĝ_zz at β̂ = 0 are correct (with ĝ_tt = ĝ_tz = 0 one has ĝ^(zr) = 0 and
ĝ^(zz) = 1/ĝ_zz). Replace lines 611-615 by:

    η₀, η₁ and η₂ are at most a constant times ε, the constants depending only on ĝ, β̂, ρ and the box. At Y = Ŷ the
    entries of D_Y F̂ are built from the Christoffel symbols Γ̂^μ_αβ contracted with ê and their first derivatives; for
    β̂ = 0 these are the Γ̂^μ_tα, the entry for the pair (z, q) is Γ̂^t_tt − 2Γ̂^z_tz, and 2Γ̂^z_tz = ∂_t ln ĝ_zz is twice
    the null expansion of the circles {t, r constant} along ê; so the exponential rate L is a bound for the null expansions
    and the related connection coefficients of ĝ along the reference generators, enlarged to the tube 𝒯.

## nits

- n1 (line 833, Placement item 3): 125 characters, over the limit of 121. The item concerns the pending wave-gauge data
  and will presumably be rewritten with the new subsection; re-wrap it then.
- n2 (lines 703, 804): ε of eq:tl5-dn-eps is the maximum of the derivatives of order ≤ 2, a C² distance; "the
  C^(1,1)-distance" and "in C^(1,1)" are accurate only up to the norm used for the Lipschitz constant. Suggest "the
  C²-distance (in the maximum of the components)" at 703, and "in C²" at 804.
- n3 (line 767): "at least 1 − η₁ > 0 by (b)" is the outgoing family (b_min = 1); for "likewise Φ^in" the factor is at
  least b_min − η₁ ≥ b_min/2 > 0. Suggest "at least 1 − η₁ > 0 by (b) (for Φ^in at least b_min − η₁ ≥ b_min/2)".
- n4 (lines 546-547): "the positivity on the leaves restrict to g_σ" → "the positivity on the leaves restricts to g_σ".
- n5 (line 12): D̄ is not among the regions of def:tl5-cip-data (there it is D_(v*)); it is defined in the display
  that follows, so "and the regions D̄, N₀, …" could read "the regions N₀, N₁, N = N₀ ∪ N₁ and S = N₀ ∩ N₁ of
  [[pending:def-tl5-cip-data]], and D̄:" with D̄ kept in the display.
- n6 (line 626, lem:tl5-dn-gronwall): ψ(t) ≤ α(t)(e^(L(t−a)) − 1)/L needs L > 0; add "L > 0" to the hypothesis (in the
  application L ≥ 1).
- n7 (lines 675-676): Ĵ⁻ is a maximum over c ∈ [r₀ − ρ, r₁] only, so "ψ̂_t of [r₀ − ρ, r₁ + ρ] × ℝ is Ĵ⁻-Lipschitz on
  convex sets" should read "… is Ĵ⁻-Lipschitz on convex subsets of [r₀ − ρ, r₁] × ℝ" (all uses lie there).
- n8 (lines 410-414, Step 1): "In the coordinates (w₁, τ₂, y), D^κ_s is a box near q" holds for s > 1/2 (for s = 1/2,
  D^κ_(1/2) = S, and the box is not used); when the first condition is absent, w₁ may be taken to be u. Also, the
  extension "from the box by lem:tl5-cip-extend (a)" is applied in the variables (w₁, τ₂), a linear change of (u, v);
  Placement item 2 could list this beside the local use of (c).
- n9 (lines 741-742, thm:tl5-dn "Five dimensions"): the null geodesics of g are taken from B, a closed set; as in the
  proof of lem:tl5-dn-family, say that g is first extended to a neighbourhood of B (G-invariantly, e.g. by
  lem:tl5-cip-extend (a), which commutes with G), solutions that stay in B not depending on the extension.

## Placement and form (checked)

- Old text: the only anchor, "### Continuation beyond the seed {#sec:tl5-beyond}", occurs exactly once as a whole line
  in the chapter sources at HEAD (chapters/87-ten-l5.md:1148, as Placement item 1 says).
- Scratch merge in scratch/rph29/ (chapters/87 with lines 1-806 inserted at line 1148 with one blank line on each
  side; the 43 rows inserted before the sec:tl5-beyond row of crosswalk/87-ten-l5.tsv): `lint.py --chapters`
  4778 labels (4735 at HEAD + 43), 29 hits, all [[pending:…]] markers; `assemble.py --check` and `assemble.py`
  "labels 4778, computations cited 0, problems 0"; `lint.py --paper` 58 hits, the 29 markers each reported as pending
  and as unresolved symbolic label, nothing else.
- Chapter text: maximum raw line 121 characters, maximum assembled line 121; the only line starting with a marker,
  line 708 "- the ingoing family: …", is the second item of a deliberate two-item list (not a wrapped line).
  No backslash, no quotation, no process language (lint clean apart from the markers).
- Crosswalk: 43 rows, 4 tab-separated columns each, in chapter order, each row's line number is the line of its label
  in the file at 77c50d0d, every label defined in the text has a row, none is defined elsewhere. (The line numbers
  will move when the writer's new subsection lands; they must be re-taken then.)
- The 14 pending P-F123 labels all exist in P-F123 (md5 136974…) and are used for what they state: sec:tl5-cip-form
  (𝒬, G, charts), def:tl5-cip-data, def:tl5-cip-null, lem:tl5-cip-form (a) inverse and (b) class, eq:tl5-cip-
  constraints, lem:tl5-cip-shift, def:tl5-cip-development (a)-(c), cor:tl5-cip-staged (a), lem:tl5-cip-extend (a)-(c)
  ((c) used locally, as item 2 says; its proof is indeed local), lem:tl5-cip-wave (in lem:tl5-wg-zero, hypotheses met),
  lem:tl5-cip-causal (c) (null gradients are pregeodesic), lem:tl5-cip-axis (a) (on the box D′), lem:tl5-cip-chart
  steps (4) and (5) (step (4): ∂_ṽ future directed, ∇ũ past directed via dũ(e₃) = 1 on N₀; step (5): γ, b on N₀ from
  (a), W from (b)-(c), b on N₁ from lem:tl5-cip-shift with g_N's constraint, which thm:tl5-dn assumes), thm:tl5-cip
  (notion of solution).

## The writer's findings and named risks

1. G0 §9.4, "(F1_W) is thm:std-ctg-neighbourhood as it stands": agreed, it is not. [CTG23, Theorem 1.1] as quoted in
   Appendix A asserts that the maximal globally hyperbolic development contains a future neighbourhood of the data
   hypersurfaces; it says nothing of wave coordinates relative to ĝ in the chart (u, v, y), of the tilted regions, or of
   a solution of Ric^W = 0 equal to G^♯ on N. Getting (F1_W) from it would need a characteristic problem for the wave
   map on the development, which is not in it.
2. [CCTW16] (read on alphaXiv, arXiv:1406.3009v2): Theorem 4.3 (p. 49) is for semilinear systems of wave equations
   (Section 4 title "Application to semi-linear wave equations"); p. 40 says the loss of a derivative in passing to
   double-null coordinates "leads to difficulties when attempting to apply our techniques to the harmonically-reduced
   Einstein equations", and p. 50 repeats it; the mixed problems of p. 54 (Figures 5.3, 5.4) are for the vacuum
   Einstein equations, obtained "from Theorems 5.1 and 5.2" without a statement in a wave gauge. Agreed: there is no
   theorem there to quote for (F3_W). The text of P-H29 cites neither CCTW16 nor CTG23 for (F1_W)/(F3_W), correctly.
3. "(F4_W) needs no separate constraint hypothesis": the proof of (F4_W) indeed uses only (W2); the further statement
   that the constraints follow from (W2) does not hold for Ric(e₄, ∂_A) (m2).
4. Risk: DS23's existence time read as structure-only. P-H29 does not use this reading: lem:tl5-wg-cauchy (iv) applies
   [DS23, Theorem 2.4] once, at the datum (0, 0) of the system with the initial time σ adjoined, and gets the other
   initial times near 0 from [DS23, Theorem 2.5] (stability, by the usual contradiction argument on sequences σ_n → 0).
   Chapter 46's reading in (N) ("T > 0 depending on ‖u₀‖_r = 0 and on the structure only, so not on t₀") is DS23's own:
   Theorem 2.4 (p. 4) makes T depend on ‖u0‖_r and M̃; Remark 4.2 (p. 9) says "the existence time T and the bound C is
   determined by ‖u0‖_r and dist(U^c, Im(u0))"; and DS23 itself restarts Theorem 2.4 at later times in the proof of
   Theorem 2.6 (§4.7, p. 13: "By Theorem 2.4, the existence time depends only on the H^r-norm of the initial data and the
   distance between ∂U and the image of the initial data"). The structural constants (F_I, Λ₀, Λ₁ of Remark 2.3) are
   uniform under a shift of time when the bounds of (A1)-(A2) are uniform in t, which chapter 46 states and which holds
   there (coefficients constant in τ outside a compact interval). So chapter 46's use is supported by DS23's text.
5. Risks at Steps 4-7 and at the axes: Steps 4-7 contain M1 and M2; the isotropy and immersion argument at the axes is
   correct apart from m7 (details below).

## What I checked and found correct

- def:tl5-wg-background and eq:tl5-wg-khat: ĝ(e₀, e₀) = ĝ(ê₃, ê₄)/(2Ω̂²) = −1; (e₀, e₁, f_i) ĝ-orthonormal (the leaves
  are ĝ-orthogonal to ê₃ and ê₄); e₀⊗e₀ + e₁⊗e₁ = (ê₃⊗ê₃ + ê₄⊗ê₄)/(2Ω̂²); |du|² = |dv|² = 1/(2Ω̂²), k̂⁻¹(du, dv) = 0.
- def:tl5-wg-gauge, eq:tl5-wg-form: Υ = H and Ric^W = R^(H) of [CBCM10, (2.7)-(2.9), p. 8] (read on alphaXiv,
  arXiv:1006.4467v1: (2.7) H^λ := g^(αβ)Γ^λ_αβ − W^λ, W^λ := g^(αβ)Γ̂^λ_αβ; (2.8) R_αβ ≡ R^(H)_αβ + ½(g_αλ D̂_β H^λ +
  g_βλ D̂_α H^λ); (2.9) with f̂ "independent of the second derivatives of g"), signs and factors as in the text; the
  passage to coordinates and the polynomial Φ.
- lem:tl5-wg-linear re-derived: δΓ, Palatini, δΓ^μ_μα = ½ D̂_α tr h, both commutators with the stated curvature
  convention, R̂^ρ_βμα h_ρ^μ = (R̂iem·h)_αβ by the pair and antisymmetries, (h∘R̂ic)_βα = (R̂ic∘h)_αβ,
  δΥ = ψ = div h − ½ d tr h, so δRic^W = −½(□̂h + 2𝓡̂h) with 𝓡̂ = R̂iem· − ½(R̂ic∘ + ∘R̂ic); (c), (d).
- def:tl5-wg-domains and lem:tl5-wg-domains: (a) ĝ⁻¹(dτ₁, dτ₁) = −κ′/Ω̂², ĝ⁻¹(dτ₂, dτ₂) = −κ/Ω̂²,
  ĝ⁻¹(dτ₁, dτ₂) = −(1 + κκ′)/(2Ω̂²); (b) |dτ₂|² = (1 + κ²)/(2Ω̂²), so g⁻¹(dτ₂, dτ₂) ≤ (−κ + κ(17/16)/2)/Ω̂² =
  −15κ/(32Ω̂²) for κ_m ≤ κ ≤ 1/4, likewise τ₁, and g⁻¹(dτ₁, dτ₂) ≤ (−1 − κκ′ + 17/64)/(2Ω̂²) < 0; (c) g^(uv) ≤
  −3/(8Ω̂²) and the signs of du(V), dv(V); (d) both inclusions; D^κ_(1/2) = S; N ⊂ D^κ from the two conditions on κ, κ′;
  the consequence [−10, u* − 3κ′] × [1/2, v* − 9κ] × S³ ⊂ D^κ for v* − 1/2 = 3, u* ≤ −1.
- lem:tl5-wg-norms (a), (b): the Neumann-series bounds, |h| ≤ |K|/(1 − ‖K‖) ≤ 1/3, convex combinations Lorentzian.
- lem:tl5-wg-jets: the orders in ∂_v of every term of ∂_v^(k−1)E (coefficient −½g^(vv) = 0 of ∂_v^(k+1), the terms
  −V(∂_v^k g), −½(k − 1)∂_v g^(vv) ∂_v^k g, ∂Φ/∂(∂_v g) ∂_v^k g), the case k = 1 by the integral mean value, V = g^(uv)e₃
  with g^(uv) ≠ 0, the initial values at S, and the same on N₁.
- lem:tl5-wg-zero: the exhaustion τ, compactness of X ∩ {τ ≤ c}, the first point of disagreement, the flat extension
  across N (also at S), and the use of lem:tl5-cip-wave and thm:std-bgp-development.
- prop:tl5-wg-unique: the difference identity, g₁⁻¹ − g₂⁻¹ = g₂⁻¹δg₁⁻¹, smooth coefficients by lem:tl5-wg-norms (b).
- prop:tl5-wg-vacuum: D̂_βΥ^λ = ∇_βΥ^λ − C^λ_βμΥ^μ; the formula for S; ∇^αS_αβ − ½∇_β tr S = ½□Υ_β +
  ½g^(αγ)[∇_γ, ∇_β]Υ_α + (terms with at most one derivative of Υ); flat data from (W2); G-invariance via (F2_W) (σ*g
  tilted because σ preserves ê₃, ê₄, Ω̂); the eight-dimensional subspace (15 − 7 components).
- lem:tl5-wg-cauchy: the transported chart and zero shift; the causal-cone bound C_c by compactness; the cut-off system
  with 𝔤 satisfying 𝔤^(ττ) ≤ −min(c₀, 1) and 𝔤^(ab) ≥ min(c₀, 1) (convexity); (A1)-(A4) of [DS23] on the whole state
  space via chapter 6, Step 8 (iii), with σ adjoined; r = 4 > N/2 + 1 = 3; [BH17, Theorem 9.14] (s p = 8 > 4); the
  choice of ε₀ and the interval [−2ε, ε]; smoothness via the first clause of [DS23, Theorem 2.6]. The quotations of
  [DS23] Theorems 2.4-2.6 in Appendix A agree with the arXiv text (pp. 4-5).
- prop:tl5-wg-local apart from M1, M2: Step 1 (the three kinds of points of K_s, including the corner u = u*, v = 1/2,
  where κ(u − u*) ≤ 1/2 − v and τ₁ − u* ≤ (u − u*)(1 − κκ′) ≤ 0; the Borel sum: derivatives of order < k of c_k are
  O(ε_k), ∂_u^k c = d_k at u = −10, c = 0 for τ₂ ≤ s; (P1)-(P3); 𝒱_q ∩ ∂Q₊ ⊂ N⁺); Step 2 smoothness of F_q; Step 3
  (the choice of η″); Step 4 (C¹ cut at τ = −ε, distributional equation, the cone 𝒞, the compact sets L_p ⊂ X, and
  r₀/2 − 3C_c ε ≥ 5r₀/16 ≥ r₀/8); Step 5; Step 7 (the compactness argument for s′ and smoothness of g′ across K_s).
- thm:tl5-wg collects the propositions correctly; rem:tl5-wg-continuation's |h| ≤ κ_m/2 ⇒ |g⁻¹ − ĝ⁻¹| ≤ κ_m.
- def:tl5-dn-slice, lem:tl5-dn-geodesic: fixed set of ρ₁, ρ₂; joint eigenspaces at points off and on the axes; totally
  geodesic; every orbit meets M_σ; g_σ⁻¹(dv, dv) = g⁻¹(dv, dv) because g⁻¹(dv) is tangent to M_σ.
- sec:tl5-dn-one: 𝔉 is the pregeodesic equation parametrised by t (κ = Γ^t_αβẊẊ); 𝔑: g(V, V) =
  C + 2B̃p + (g_rr − g_rz²/g_zz)p² with the last coefficient 0 at t₀ by (i), q₀ from g(V, ∂_z) = 0, and 𝔑(ĝ) = (0, β̂)
  since Ĉ = 0, B̂ = ĝ(ê, ∂_r) < 0, β̂ = −ĝ_tz/ĝ_zz; the reference generators; the (z, q) entry Γ̂^t_tt − 2Γ̂^z_tz at
  β̂ = 0.
- def:tl5-dn-constants and eq:tl5-dn-eta: η₀ = (Λ₀ + Λ₁T) ε e^(LT) (initial error Λ₀ε, forcing Λ₁ε, rate L);
  η₁ = (2(Λ₀′M₁ + Λ₀)ε + TĴ(Λ₂ε + L₂η₀)) e^((L + Λ₂ε)T) (the initial rows ∂(𝔑(j⁰g) − 𝔑(j⁰ĝ)) bounded by
  Λ₀′ε·2M₁ + Λ₀·2ε, the bracket by Λ₂ε + L₂η₀, the rate by L + Λ₂ε); η₂ = η₀ + 2(b_∞ + 1)η₁/b_min (|a_z| ≤ 2η₁/b_min,
  |a_t| ≤ η₀ + (b_∞ + η₀)·2η₁/b_min with η₀ < 1).
- lem:tl5-dn-gronwall and lem:tl5-dn-family (a)-(d): the bootstrap on [t₀, t₂), r > r₀ by (iii) and uniqueness, L ≥ 1;
  the variational equation; injectivity and surjectivity of ψ_t by the contraction T_w (w_r − Δ̃_r ∈ [r₀ − η₀,
  r₁ − η₀], a*_r ≥ r₀); invertible differential; the conormal (pb − qa, −b, a); λ > 0 from the bracket ≥ 1/2, using
  η₁(1 + 2(Ĵ + 1)/b_min) ≤ 1/2, hence η₁ ≤ b_min/2.
- thm:tl5-dn: B ⊂ D^κ; the two families satisfy the reference conditions and (i)-(iii) (by (a) of the development, the
  kernels e₃, ∂_v, and lem:tl5-wg-domains (c)); the 5D null normals tangent to M_σ and the equivariance; the
  interval-preservation argument (a generator from ϑ₀ ∈ (0, π/2) meeting an axis would meet its mirror image,
  against injectivity of ψ_t); φ_i constant along generators; injectivity through the isotropy groups (ℤ₂ × ℤ₂ off the
  axes, O(2) × ℤ₂ on them, a closed subgroup of the same dimension and number of components being the whole group);
  invertibility of dΦ^out off the axes (TM_σ ⊕ orbit) and on them (the fixed subspace of the rotations of z₂, and on
  the z₂-plane a map commuting with SO(2) and with z₂ ↦ z̄₂, a real multiple ∂_(ϑ₀)ϑ ≥ 1 − η₁); V(1/2) = 1/2,
  V ≥ v − η₀^in, ∂_vV ≥ λ(1 − 2η₂^in η₀^out) > 0; u* − η ≤ u_m − η₀^out and v* − η ≤ v_m − 3η₀^in, so
  η = max(κ′(v* − 1/2) + η₀^out, κ(u* + 10) + 3η₀^in) gives D′; Ψ the identity on N ∩ D″; N ∩ D′ ⊂ D″; double-null form,
  G-invariance, the class with fields smooth up to the axes, and g̃ = g_N on N ∩ D′ by step (5) of lem:tl5-cip-chart.
- rem:tl5-dn-use: η is the tilt plus a multiple of ε, and no double-null uniqueness or existence is used.
- lem:ii-f-1-3 (chapter 27, line 244): used at its hypotheses in Step 4 (X open, 2𝔓 with principal symbol G_q⁻¹(ζ, ζ),
  τ a time function, compact L_p ⊃ J⁻_X(p) ∩ {τ ≥ c}, supp w ⊂ {τ > c}); after M2's repair also in Step 6.
- Self-containedness: every step not covered by M1, M2 and the minors is proved in the text or cited at a statement
  that says it; the only unproved input is the marked [[pending:wave-gauge-data]], out of scope here.
