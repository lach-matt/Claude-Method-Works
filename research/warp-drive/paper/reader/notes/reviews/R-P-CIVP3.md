# R-P-CIVP3: independent line-by-line reading of proofs/P-CIVP3.md

File read: `research/warp-drive/paper/reader/proofs/P-CIVP3.md`, md5 1d196fae6ed5c92557721eb8dadfd294, 1,126 lines (the
section 1–833, Placement 835–1039, crosswalk rows 1041–1126), at branch head df9a4c35. Every line was read.

Also read: STYLE.md, READER-BRIEF.md; the writer's report notes/reports/P-CIVP3.md; the scoping notes/reports/S-T3.md
and the gap notes notes/reports/GN-T3.md (all); chapter 81 lines 1–380, 381–700 (sec:class-kato), 848–1040, 1038–1671
(sec:class-axes, sec:class-planar-shear, def:class-adapted, thm:class-stability, cor:class-two-dust); chapter 80 lines
75–240, 325–345; chapter 83 lines 1–80, 334–500 (lem:loc-lens-dependence, steps (4)–(6)), 520–605, 1711–1730, 2382–2400;
chapter 87 lem:tl5-continuation; Appendix A thm:std-ly-extension; Tier 1 proofs/P-CIVP.md as it stands now (md5
f8a1e948a7f9c53831719f5d526cc3a8, 1,279 lines: Blocks A and B in full, Placement and item 11) and its version at the
time P-CIVP3 was written (c7e724d3), for the diff; Tier 2 proofs/P-CIVP2.md as it stands now (md5
e80ea7a4542d128253dccbb16a7dd408, the fix round of df9a4c35: rem:civp-large-domain, rem:civp-large-beyond, Placement);
the first lines of notes/reviews/R-P-CIVP.md for the grading. Nothing under method/, drive/, extracted/ or recovered/
was read; no repository file was edited; plain assemble.py was run only in the scratch copy.

**Verdict: NOT CONFIRMED.** 1 Major, 7 minor, 20 nits.

The mathematics of the section is sound except at one step. The Major finding is an order-of-quantifiers gap in the
continuity argument of Lemma R (lem:loc-axis-dependence). The statement there is right, and one sentence fixes it,
using the infinite-order vanishing that the text already has. The minor findings are four definitional or justification
imprecisions in the section (the sign in σ_A, "smooth field" in place of "Lorentzian metric", the extension's
localisation, the decoupling of the jet equations), one inaccurate remark, and two placement texts: one says something
self-contradictory, and one is stale against the current Tier 1/2 files. Every replacement below is at most 121
characters a line, and no wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". These were checked by a
script in the scratchpad.

---------------------------------------------------------------------------------------------------------------------

## A. Findings

### Major 1: Lemma R, the continuity step: θ is chosen after ϵ′, so W need not be near U_1 (lines 638–649)

Current (lines 638–642, 646–649): "U_2 − U_1 is smooth and vanishes with all derivatives on R′ ∩ {t ≤ t*}, on the past
faces by hypothesis; so for every ϵ′ > 0 there is θ ∈ (0, 1] such that the derivatives of order at most k of U_2 − U_1
are at most ϵ′ on the set 𝒩_θ … Let χ_θ be a G-invariant cut-off equal to 1 on 𝒩_(θ/2) and supported in 𝒩_θ, and W :=
U_1 + χ_θ (U_2 − U_1); for ϵ′ small, W ∈ 𝔅′ on the slices. … The arc of the leaf of W through x, C¹-close to that one
for ϵ′ small, lies in 𝒩_(θ/2) … whose differential is within Cϵ′ of that of U_1 on 𝒩_θ, … for ϵ′ small it lies in
𝒩_(θ/2) ⊂ 𝒪".

What is wrong.
- θ = θ(ϵ′) comes from uniform continuity, and θ → 0 as ϵ′ → 0. The derivatives of order j of χ_θ are of size θ^(−j).
- So the derivatives of order up to k of W − U_1 = χ_θ (U_2 − U_1) are only bounded by Σ_j θ(ϵ′)^(−j) ϵ′. That need
  not be small, and "for ϵ′ small, W ∈ 𝔅′" does not follow. The ball 𝔅′ is in 𝒩_(k−1), which holds up to k derivatives
  of g.
- The other two closeness claims compare a deviation of size Cϵ′ with the gap θ/4 between 𝒩_(θ/4) and 𝒩_(θ/2). The leaf
  of W stays in 𝒩_(θ/2), and the level set of U_2's phase stays in 𝒩_(θ/2) ⊂ 𝒪. Both need Cϵ′ < θ(ϵ′)/4, which nothing
  gives.

The conclusion is right. U_2 − U_1 vanishes to infinite order on 𝒦 := R′ ∩ {t ≤ t*}, which is convex in (ũ, ṽ). So
Taylor's formula gives |∂^α(U_2 − U_1)| ≤ C_N θ^N on 𝒩_θ for every N, and this absorbs the cut-off. Replacement for
lines 638–649. Line 637 ends "uniform near the", and line 650 begins "the rows of 𝒜^ax at x.":

    points of the axes in R′ ∩ {t* ≤ t ≤ t* + 1}. U_2 − U_1 is smooth and vanishes with all derivatives on 𝒦 := R′ ∩ {t ≤
    t*}, on the past faces by hypothesis. For θ ∈ (0, 1] let 𝒩_θ be the set of the points of 𝒪 whose coordinates (ũ, ṽ)
    lie within θ of those of a point of 𝒦. 𝒦 is convex in (ũ, ṽ), so for θ small each point of 𝒩_θ is joined to its nearest
    point of 𝒦, with the same ω̃, by a segment in 𝒩_θ ⊂ 𝒪, and Taylor's formula along it bounds the derivatives of order at
    most k of U_2 − U_1 on 𝒩_θ by Cθ^(k+1), C not depending on θ. Let χ_θ be a G-invariant cut-off equal to 1 on 𝒩_(θ/2)
    and supported in 𝒩_θ, whose derivatives of order j are at most Cθ^(−j), and W := U_1 + χ_θ (U_2 − U_1); by Leibniz's
    rule the derivatives of order at most k of W − U_1 are at most Cθ, so for θ small W ∈ 𝔅′ on the slices. Let s ∈ [t*,
    t* + θ/8] and let x ∈ O_s lie near an axis. R′ is star-shaped about (0, 0) in (ũ, ṽ), and the point (t*/s)(ũ, ṽ)(x)
    lies in 𝒦 within √2 (s − t*) of (ũ, ṽ)(x); so O_s ⊂ 𝒩_(θ/4), and the arc of the leaf of U_1 through x lies in
    𝒩_(θ/4), O_s being a union of its leaves. While the arc of the leaf of W through x stays in 𝒩_(θ/2), where W = U_2, it
    lies within Cθ² of that one in C¹, U_2 − U_1 being at most Cθ² in C¹ there; for θ small, Cθ² < θ/4, so it stays in
    𝒩_(θ/2), and by the uniqueness in [[lem:class-volterra]] it is the arc of the leaf of U_2, and σ_A[W] = σ_A[U_2] on
    O_s. Likewise the level set through x, in O_s, of the phase of family A of U_2, whose differential is within Cθ² of
    that of U_1 on 𝒩_θ, is from the axis to x a graph within Cθ² in C¹ of the sphere through x, which lies in 𝒩_(θ/4); for
    θ small it lies in 𝒩_(θ/2) ⊂ 𝒪, so U_2 solves

The rest of the proof is unchanged, and the energy step on R′ ∩ {t* ≤ t ≤ t* + θ/8} still uses no smallness of U_1 or
U_2. The word ϵ′ then no longer occurs in the proof.

### minor 1: the explicit formula for σ_A[V] lacks the sign of p_A(∂_z) (lines 282–283)

Current: "axis, and σ_A[V] at a point is 2|p_A^Σ| σ_L − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e_2, e_2)) for the leaf through it,
σ_L of / [[eq:class-leaf-volterra]] and e_r the unit tangent of the leaf in the meridional plane, which is".

What is wrong.
- σ_L of eq:class-leaf-volterra is taken "for the normal ν" of lem:class-leaf (b), the one pointing to increasing z.
- In eq:class-shear-leaf, k_r − k_φ is taken for the normal ∇_M3 u/|∇_M3 u|. With p_A in place of du, that normal is
  p_A^Σ/|p_A^Σ| = ±ν, with the sign of p_A(∂_z).
- So the first term must carry that sign, as H_L[V] in eq:loc-axis-hl does.
- The sign is negative for the ingoing family at axis 2 in the chart eq:loc-axis-time. Along a slice v increases with
  |y|, so p_in(∂_z) = −∂_z v < 0.
- As written, σ_A[Û] would not be the planar shear of the spheres whenever K_Σ(e_r, e_r) ≠ K_Σ(e_2, e_2). The identity
  of lem:loc-axis-system (d) would then fail.
- The clause "which is eq:class-shear-leaf with p_A in place of du" states the intended object, which is why this is
  graded minor.

Replacement for lines 282–283 (line 284 begins "[[eq:class-shear-leaf]] with p_A in place of du."):

    axis, and σ_A[V] at a point is ±2|p_A^Σ| σ_L − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e_2, e_2)) for the leaf through it, the sign
    that of p_A(∂_z), σ_L of [[eq:class-leaf-volterra]], taken for the normal ν of [[lem:class-leaf]] (b), and e_r the unit
    tangent of the leaf in the meridional plane, which is

### minor 2: def:loc-axis-data asks for "a smooth field", but the equivalence it states needs a Lorentzian metric (lines 67–68)

Current: "axes* if the field of symmetric forms [[eq:loc-double-null]] that they define at the points of D × S³ off the
axes / extends to a smooth field on D × S³."

What is wrong.
- A smooth extension as a field of symmetric forms may degenerate at the axes. For example, γ_ϑ = sin²ϑ and
  e^(2A_s) = sin⁴ϑ near ϑ = 0 make the planar part ρ2² |dx|², which is smooth but degenerate.
- With such fields Ω² may also tend to 0 there.
- So the stated "exactly when ln Ω extends to a smooth G-invariant function, γ to a smooth family … of G-invariant
  Riemannian metrics" is false in the forward direction.
- Non-degeneracy gives it: if γ had a kernel vector X at an axis point, then g(X, ·) = 0. Every later use needs γ
  Riemannian (Y > 0, the leaves, the chart).

Replacement for lines 67–68 (line 69 begins "spheres is γ := …"):

    axes* if the metric [[eq:loc-double-null]] that they define at the points of D × S³ off the axes extends to a smooth
    Lorentzian metric on D × S³. Since g(∂_u, ∂_v) = −2Ω², the restriction of g to the tangent spaces of the

### minor 3: lem:loc-axis-constraints (c) does not say that the extension keeps the data's localisation (lines 109, 150)

What is wrong.
- Part (d) of thm:loc-axis is proved by lem:loc-axis-angle, on its second half.
- That lemma's hypothesis concerns the cone data of the reduced problem: "let the cone data equal the background's at the
  points with ϑ < ϑ_a′". Those are the extended data on N_o and N_i.
- The theorem's hypothesis concerns the given data on {0} × [0, v_1] and [0, u_1] × {0} only.
- lem:loc-axis-constraints (c) states the size bound of the extension but not that the extension equals the background's
  where the given data do. The proof of the theorem therefore uses an unstated property.
- The property is true, as in lem:loc-cone-extension. At such points all h_j vanish, and the equations of (b) have the
  background's coefficients and initial values there.
- The first half of (d) is unaffected: it goes through (c).

Replacement for line 109 (line 110 begins "u_1, v_1, δ_1 and the background."):

    through the axes on N_o and N_i, in the normalised gauge, of size at most Cε in C^(m_0) and equal to the background's at
    the points of every G-invariant open set of S³ at which the given data are; ε_0 and C depend only on k,

Replacement for line 150 (line 151 begins "and are smooth through the axes;"):

    C^(p−3), and b is at most Cε in C^(p−3) = C^(m_0). At the points of a G-invariant open set of S³ at which the given data
    are the background's, every h_j vanishes, so f̃ = f̊ there, and the equations of (b) have the background's coefficients
    and initial values there, so that their solutions are the background's. The extended functions satisfy (i) and (ii) of
    [[def:loc-cone-data]]

### minor 4: the order of solution of the jet equations rests on an unstated decoupling (lines 227, 239–240)

What is wrong.
- On N_o the text solves "for (Z_Ω, Z_γ), … and then for Z_b, whose inhomogeneous term holds ∇̊Z_Ω and ∇̊Z_γ".
  This needs the first two components of 𝔏(Z) − 𝔏(0) to hold no Z_b.
- Otherwise ∇̊ of the first unknowns enters the third equation while Z_b enters the first two, and the system is no
  longer an ODE along each generator.
- The text says only that the first two components of 𝔪 are "free of ∇̊Z".
- On N_i, the third component of 𝔏′ is said to be −(4Ω²)⁻¹ γ(L̲Z_b, ·) "plus terms without derivatives of Z". Solving
  "first for Z_b" needs those terms to hold Z_b only.
- Both facts hold. Off the axes they are (Ψ1) and (Ψ3) of the proof of lem:loc-cone-jets: E′ other than E(L̲, ∂_ϑ) holds
  no ∂_u b, and Ψ_4 holds no ∂_v of ln Ω or of the ϰ_i. At the axes they follow by continuity of the coefficients.

The principal parts eq:loc-axis-principal themselves are correct; see section D.

Replacement for line 227 (line 228 begins "system of ordinary differential equations in v along the generators:"):

    with 𝔪 linear, with smooth G-invariant coefficients, its first two components free of ∇̊Z and of Z_b, since off the axes
    these two components of 𝐄 hold no u-derivative of b ((Ψ1) of the proof of [[lem:loc-cone-jets]]) and their coefficients
    are continuous. So 𝔏(Z) = 0 is a linear

Replacement for lines 239–240 (line 241 begins "∇̊Z_b. So 𝔏′(Z) = 0 consists"):

    in ∂_v² contribute only terms without derivatives of Z, and the third component of 𝔏′(Z) − 𝔏′(0) is −(4Ω²)⁻¹ γ(L̲Z_b, ·)
    plus terms in Z_b without derivatives, by (Ψ3) of the proof of [[lem:loc-cone-jets]] and continuity, the others being
    (2Ω²)⁻¹ L̲Z_γ and −2L̲Z_Ω − ½ tr_γ L̲Z_γ plus terms in Z and

### minor 5: rem:loc-axis-constants says smallness enters in "three places" (lines 814–818)

What is wrong.
- Two more uses of smallness are omitted. lem:loc-axis-gauge needs Ψ close to the identity ("for ε small") for its image
  to contain Q1 × S³.
- lem:loc-axis-unique needs ε and ε_2 small for its wave map.
- The remark states a count that is false.

Replacement for lines 814–818 (line 819 begins "the number δ and the leaf constants"):

    the constraints of [[lem:loc-axis-constraints]] (b) need only Y > 0. In the existence proof smallness enters in four
    places: Û must lie in the ball 𝔅′ about Ů, through ‖Δ‖_(C^(k+3)) ≤ Cε ([[lem:loc-axis-jets]] (c)); the solution must
    stay, over the whole interval [τ_init, s*], in the ball 𝒟_ρ about the background in H^k on which the term in σ_A is
    defined, which the bound of [[lem:loc-axis-system]] (e) gives ([[lem:loc-axis-cauchy]]); Ψ of [[lem:loc-axis-gauge]] must
    be close enough to the identity for its image to contain Q1 × S³; and the extension of the data beyond u_1 and v_1 must
    keep Y positive ([[lem:loc-axis-constraints]] (c)), as must the constraints in [[cor:loc-axis-cones]]. The uniqueness of
    [[lem:loc-axis-unique]] needs ε and ε_2 small for its wave map. The radius ρ,

### minor 6: Placement item 9 says "localised in an angular band away from the axes" and then "whether or not their band avoids the axes" (lines 997–1004)

What is wrong.
- The bullet of ch:theorems introduces its data as "localised in an angular band away from the axes". It then attaches
  the whole-rectangle development to the same data "whether or not their band avoids the axes". That contradicts itself.
- The new bullet should list the two kinds of data separately.
- Replacement for the new text, lines 997–1004. The old text (line 376) and the next chapter line ("  near the initial
  data …") are unchanged:

      construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge of
      data on the two null cones through the corner sphere of the explicit two-dust background of [[sec:bg-data]]: of data
      localised in an angular band away from the axes, with or without dust and without smallness, on a neighbourhood of
      the two cones that depends on the data, localised and unique in the gauge among solutions equal to the background
      near the axes ([[thm:civp-large]]), and, for such data near the background's, on an explicit neighbourhood with an
      estimate ([[thm:loc-cone-development]]); and of data near the background's, localised in angle or not, on the whole
      rectangle of the two cones in which the two dusts cross, [0, 7.2] × [0, 4.5], with an estimate and unique in the
      gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]); and exactly localised vacuum data

### minor 7: Placement item 3 merges a superseded Tier 1/2 text (lines 902–908)

What is wrong.
- The new text of item 3 replaces Tier 1's item 4 at the same site. Its clause on Tier 2 is the one Tier 1 carried at
  c7e724d3: "among them, when the background is defined on [0, u_1] × [0, v_1] for some v_1 > 4.5 and u_1 > 7.2, are
  every perturbation of the shell or of the packet of any amplitude for which e^ϕ stays positive and every density added
  in the band".
- The current Tier 1 item 4 (P-CIVP.md lines 1102–1107) reads otherwise, and so does Tier 2's rem:civp-large-beyond after
  df9a4c35: "with u_1 = 7.2 and v_1 = 4.5, which are admissible ([[lem:civp-large-rectangle]] (a))".
- The current Tier 1 text reads "among them, with v_1 = 4.5 and u_1 = 7.2, are every perturbation of the shell or of the
  packet, or of both, and every density added in the band, of any amplitude for which e^ϕ stays positive, and such
  perturbations exist of every amplitude ([[lem:civp-large-free]], [[lem:civp-large-rectangle]])".
- Merged as written, the chapter would contradict the Tier 2 section beside it.
- A word-level diff of items 2, 9 and 10 against Tier 1's current items 3, 6 and 7 shows only the intended Tier 3
  insertions.
- Replacement for the whole new text of item 3, lines 891–912:

    [[thm:loc-cone-development]] develops these cone data, completed on 𝒞_in by [[lem:loc-cone-in]], when they are near the
    background's and their band avoids the axes, with or without dust: on the explicit neighbourhood G_* of the two cones
    there is a class solution in the gauge [[eq:loc-double-null]] that induces them, with an estimate, equal to the
    background outside a slightly wider band and unique in the gauge near the background off the axes. Every small
    perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, and every small density
    added in the band, supported away from the axes, is of this kind, with v_1 = 4.5 and u_1 = 7.2
    ([[lem:loc-cone-strips]] (c)). Near the background's the restriction to a band can be dropped: cone data given as in
    [[prop:loc-cones]] and [[lem:loc-cone-in]] with no restriction of their supports in angle, their metrics on the spheres
    and their densities smooth through the axes, among them every small perturbation of the shell and of the packet at once
    and every small density added on either cone, the axes included, have a development in the gauge [[eq:loc-double-null]]
    on the whole rectangle [0, 7.2] × [0, 4.5] in which the two dusts cross, with an estimate, unique in that gauge among
    nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]). Without smallness, these cone data, completed on 𝒞_in in
    the gauge b = 0 ([[def:civp-large-data]]), have a development in the gauge [[eq:loc-double-null]] on a neighbourhood
    {min(u, v) ≤ δ} of the two cones whenever their band avoids the axes; among them, with v_1 = 4.5 and u_1 = 7.2, are
    every perturbation of the shell or of the packet, or of both, and every density added in the band, of any amplitude for
    which e^ϕ stays positive, and such perturbations exist of every amplitude ([[lem:civp-large-free]],
    [[lem:civp-large-rectangle]]). That development equals the background outside a slightly wider band and is unique in
    the gauge among solutions that equal the background near the axes ([[thm:civp-large]]); the number δ depends on the
    data. For vacuum data of any size, before the shell (v_1 < 3) and on 𝒞_in before the packet (u_1 < 5.7), a development
    near the two cones exists also by [CTG23, Theorem 1.1] ([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness
    in the gauge nor localisation. No development is asserted for cone data that are not near the background's at an axis,
    for data of finite regularity or for densities that are not smooth ([[rem:loc-axis-scope]]), and no other result of
    this paper uses these developments.

### Nits

Each nit gives the current lines and the replacement. A replacement ends where the following unchanged line takes
over.

1. *Δ is used outside 𝒮 (line 448).* Δ of lem:loc-axis-jets (c) is defined on 𝒮 × S³. Through χ_𝒰Δ it is used on
   supp χ ⊂ Q^♯, which contains points of F far from the cones. It should be said that it is extended by 0. Line 448
   becomes:

       *The system.* In case (I) of [[sec:loc-cone-reduced]] take Δ of [[lem:loc-axis-jets]] (c) with δ_e := δ_c/8, extended by
       0 to Q^♯, smoothly, as it vanishes outside {|u| ≤ 2δ_e} ∪ {|v| ≤ 2δ_e}, so that Δ

2. *Φ of lem:loc-axis-system (a) (line 491).* The formula omits Tier 1's local term (1 − χ) B_♭Z. It also leaves
   F_0(x, 𝐔) undefined at the evaluation just stated. Line 491 becomes:

       Put Φ(τ, Z) := χ (F_0(x, 𝐔) − A^μ(x, 𝐔̊ + ϒ(Z)) ∂_μ𝐔̊) + (1 − χ) B_♭Z + F̃, with F_0(x, 𝐔) the right side of 𝒜^ax
       evaluated as just stated. Its local part satisfies (F1)–(F3) and the linear bound,

3. *ů := U_1 in Lemma R (line 637).* lem:class-leaf-differences and lem:loc-axis-shear are stated for "a smooth class
   solution". U_1 solves the system on R′ only, and 𝒰_(2δ)(p) leaves R′ near its faces. Their proofs use of ů only what
   U_1 has on 𝒪, so it should be said. Line 637 becomes:

       constants of [[lem:class-leaf-differences]] and [[lem:loc-axis-shear]] for ů := U_1 in this chart (their proofs use of ů
       only that it is a smooth G-invariant state whose p_A are minus the differentials of null phases and whose Θ_A are div
       P_A, which U_1 is on 𝒪), uniform near the

4. *The face {α = ι} of lem:loc-axis-angle can touch the slices (line 725).*
   - On Q1, dτ_1 ∥ dτ exactly where u = v, when δ′ < δ_c. For δ′ = δ_c the face is a slice there.
   - So the hypothesis of lem:loc-cone-energy that the faces meet the slices transversally fails at those points.
   - The domains are still Lipschitz, which is all its proof uses. Line 725 becomes:

       ln((u + δ′)(v + δ′)), and 𝒲 := 𝔗(s*) ∩ {α ≥ ι, ϑ ≤ α}; τ_1 is smooth on F. In the (u, v)-plane {τ ≤ s} and {α ≥ ι} are
       the sets below the graphs of decreasing smooth functions of u, so every 𝒲 ∩ {τ ≤ s} lies below the graph of their
       minimum, a Lipschitz function, and is a Lipschitz domain, as the proof of [[lem:loc-cone-energy]] needs, also where the
       face {α = ι} touches a slice, as it does at the points of Q1 with u = v. Its lateral boundary consists of a piece of

5. *Display, lines 375–376.* The display is broken inside the bound, and its second line starts with "|". Replace the two
   lines by:

           |σ_A[U](x) − σ_A[U′](x)| ≤ C (|U − U′|(x) + |Δq(r)| + |q_(U′)(z0, r) − q_(U′)(z0′, r)|)
                                    ≤ C (|U − U′|(x) + |Δq(r)| + |Δh(r)|).

6. *"now" (line 689).* Replace "a wave map, now in the chart" by "a wave map, here in the chart".

7. *Line 429.* "for s > τ_c it meets both" is false for s beyond the range of τ on N. Replace it by "for τ_c < s ≤ s* + 1
   it meets both". The line then wraps as:

       most one sphere S_i(s); with τ_c := 2 ln δ_c the time of the corner sphere, for τ_c < s ≤ s* + 1 it meets both, for s =
       τ_c both

8. *Line 603.* lem:loc-cone-gauge finds the image of Ψ by a contraction, not a degree argument. Replace "the degree
   argument there" by "the contraction argument there". The line then wraps as:

       injective; and as Q1 ⊂ 𝔗(s* − 1) lies at positive distance from the slice of 𝔗(s*) in Σ_(s*), the contraction argument
       there

9. *Line 533.* The time interval is [τ_init, s*], so "gives τ_m > s*" should be "extends the solution to [τ_init, s*]".
   The line then wraps as:

       [[thm:class-kato]] (a) extends the solution to [τ_init, s*]. [[thm:class-kato-stability]] is not used: it needs ρ = ∞,
       while the term in σ_A

10. *Lines 359–360.* The C¹ norm of H_L[V] holds first derivatives of p_A and Θ_A and second derivatives of g. Line 360
    becomes:

        constants hold the C¹ norms of H_L[V], which hold first derivatives of p_A and Θ_A and second derivatives of the metric,
        and the C² norms of γ3,

11. *The letter w is used twice in lem:loc-axis-shear.* Step (1) sets w := ∂_(z0)h_V, and step (3) uses w for
    |U − U′| along the leaf. Step (1) also stops at r_0 of lem:class-volterra, while the leaves are used on [0, 2δ].
    Lines 362–364 become:

        z0) and a contraction uniformly in z0, and the equation is regular for r > 0, so z0 ↦ h_V(z0, ·) is C¹ on [0, 2δ],
        and ξ := ∂_(z0)h_V solves r ∂_r ξ(r) = ∫_0^r (∂_zG_V ξ + ∂_pG_V ∂_r ξ) dρ with ξ(0) = 1. So |∂_r ξ| ≤ C r sup |ξ| on
        [0, 2δ] and |ξ − 1| ≤ C δ² sup |ξ|, and after decreasing δ, ξ ∈ [1/2, 2] and |∂_(z0) q_V| = |∂_r ξ|/r ≤ C. Hence (z0,
        y) ↦ (h_V(z0, y), y), for |z0 − z(p)| < 3δ/2

    Line 365 then begins "and |y| < 2δ, is a C¹ diffeomorphism", and in line 371 "∂_(z0)h_(U′) ≥ 1/2" is unchanged.

12. *Lines 55–56.* "By (b) and (c) the solution on Q1′ × S³ depends only on the data on the two edges" applies (c) to
    another solution of (a). That needs Cε ≤ ε_2, which nothing arranges. The same holds for the comparison with
    thm:loc-cone-development in lines 57–60. Lines 55–56 become:

        Data with q_in = 0 and q_out = 0 are vacuum data, and their development is vacuum, the densities being transported.
        Decreasing ε_0 so that Cε_0 ≤ ε_2, by (b) and (c) the solution on Q1′ × S³ depends only on the data on the two edges of
        Q1′; in particular it does not depend

13. *Line 259.* γ̂ is Y^(−2)γ in lem:loc-axis-constraints and something else here. Ω̂ > 0 is automatic, ln Ω being the
    field. Line 259 becomes:

        through the axes, smooth by (a) and (b), and Lorentzian when its metric γ_e + Δ_γ on the spheres is positive definite,
        which

14. *Line 96.* Part (b) assumes q_in ≥ 0, but its proof does not use it, and (c) applies it to an extension whose q_in may
    be negative. Line 96 becomes:

        (b) Let ln Ω, a smooth family γ̂ of G-invariant Riemannian metrics on S³ with dvol_γ̂ = dvol_1, and q_in, of either sign,
        be given

15. *Lines 202–203.* The ∂_v² terms of 𝐄 cancel altogether. In E(L̲, ∂_v) they combine to
    ∂_v²(δg_uu + 2b^a δg_ua + b^a b^b δg_ab) = 0, and the symbolic check of section D confirms that the coefficient of
    ∂_v² is zero in all three components. The text's conclusion is right, but its description can be exact:

        and, collecting those with a derivative in v other than ∂_v² (the terms in ∂_v²δX cancel: they enter E(L̲, ∂_v) only,
        through ∂_v²(δg_uu + 2b^a δg_ua + b^a b^b δg_ab) = 0), up to terms with at most one derivative of δX,

16. *Placement item 4, line 929.* "Near the background's such data are developed on the whole rectangle" needs the
    condition that item 5 states. rem:loc-cone-scope concerns general u_1, v_1. Line 929 becomes:

        needs lateral boundaries adapted to the dust. Near the background's such data are developed on the whole rectangle when
        the background is defined on it with a margin,

17. *Placement item 2, line 874.* The rectangle of the chapter's background is that of cor:loc-axis-cones. Line 874
    becomes:

        spanned by the two cones, with an estimate, unique in the gauge among nearby solutions ([[thm:loc-axis]],
        [[cor:loc-axis-cones]]). On Σ_τ0 the

18. *Placement item 6, lines 960–961.* "its statement of dependence" calls the lemma a statement of the theorem. Replace
    them by:

        the dependence on the past faces of a double-null rectangle that its proof uses ([[lem:loc-axis-dependence]]), which
        needs no smallness, gives uniqueness and not existence.

19. *Line 339.* The proof of lem:loc-axis-shear decreases δ further ("after decreasing δ"), so the statement should say
    so. Line 339 becomes:

        [[def:class-adapted]] for ů at a point p of axis 2 with ρ1(p) > 0, δ decreased, depending only on 𝔅′ and the chart, so
        that 8C_Lδ ≤ 1, that ξ ∈ [1/2, 2] in step (1) of the proof, and that the A-leaves of

    This uses the name of nit 11. Without that nit, write w for ξ.

20. *Line 453.* The choice of δ and of balls common to finitely many axis points is made in step (4) of the proof of
    lem:loc-lens-dependence, not step (6). Replace "as in step (6) of the proof" by "as in step (4) of the proof".

---------------------------------------------------------------------------------------------------------------------

## B. Placement items to re-base after the Tier 1/2 round

State at head df9a4c35.
- The Tier 2 fix round has landed in P-CIVP2.md (e80ea7a4). Its markers are replaced, lem:civp-large-free and
  lem:civp-large-rectangle are added, and rem:civp-large-domain and rem:civp-large-beyond are revised.
- P-CIVP.md (f8a1e948) has changed since P-CIVP3 was written:
  - item 4's Tier 2 clause;
  - item 11, which now gives explicit texts;
  - Block B line 850 and prop:loc-cone-local;
  - η renamed ϖ in eq:loc-cone-quantities.
- Its nit round is still to come.

Every old text of P-CIVP3 occurs exactly once, as whole lines, at the current head (section C).

- **Item 3: re-base now.**
  - Its new text carries Tier 1's superseded Tier 2 clause (minor 7).
  - Re-base it on Tier 1's current item 4 new text. The replacement in minor 7 is that re-basing.
- **Item 7: turn it into an old/new pair now.** rem:civp-large-domain is revised, and its last sentence ends "bounded or
  measure-valued." as item 7 assumes. Old:

      from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
      or measure-valued.

  New:

      from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
      or measure-valued. Cone data near the background's that differ from it at the axes are developed on the whole
      rectangle by [[thm:loc-axis]].

- **Item 13: re-base now.**
  - Tier 1's item 11 no longer drops clauses. It gives full new texts for its items 3, 4, 6 and 7 without the Tier 2
    section.
  - The Tier 2 clauses now also cite lem:civp-large-free and lem:civp-large-rectangle.
  - Item 13 should therefore give full texts too. Drafts, built on Tier 1's item 11 texts with the Tier 3 sentences, are
    below. All lines are at most 121 characters.

  Item 2 without the Tier 2 section. New:

      Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators, and
      data localised in an angular band exist exactly ([[prop:loc-cones]], [[lem:loc-cone-in]]); near the background's data,
      with the band away from the axes, they have a development on a neighbourhood of the two cones, with or without dust,
      equal to the background outside a slightly wider band and unique in the gauge near the background off the axes
      ([[thm:loc-cone-development]]). Data near the background's need not be localised away from the axes: they have a
      development in the double-null gauge on the whole rectangle spanned by the two cones, with an estimate, unique in the
      gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]). On Σ_τ0 the constraints split, after Rácz

  Item 3 without the Tier 2 section. New:

      [[thm:loc-cone-development]] develops these cone data when they are near the background's and their band avoids the axes,
      with or without dust: on the neighbourhood G_* of the two cones there is a class solution in the gauge
      [[eq:loc-double-null]] that induces them, equal to the background outside a slightly wider band and unique in the gauge
      near the background off the axes. Every small perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in
      ∩ {5.7 < u < 7.2}, and every small density added in the band, supported away from the axes, is of this kind, with v_1 =
      4.5 and u_1 = 7.2 ([[lem:loc-cone-strips]] (c)). Near the background's the restriction to a band can be dropped: cone
      data given as in [[prop:loc-cones]] and [[lem:loc-cone-in]] with no restriction of their supports in angle, their metrics
      on the spheres and their densities smooth through the axes, among them every small perturbation of the shell and of the
      packet at once and every small density added on either cone, the axes included, have a development in the gauge
      [[eq:loc-double-null]] on the whole rectangle [0, 7.2] × [0, 4.5] in which the two dusts cross, with an estimate, unique
      in that gauge among nearby solutions ([[thm:loc-axis]], [[cor:loc-axis-cones]]). For vacuum data of any size, before the
      shell (v_1 < 3) and on 𝒞_in before the packet (u_1 < 5.7), a development near the two cones exists by [CTG23, Theorem
      1.1] ([[thm:std-ctg-neighbourhood]]); that theorem gives neither uniqueness in the gauge nor localisation. For cone data
      that carry dust and are not near the background's, for data of finite regularity and for densities that are not smooth,
      no development is asserted ([[rem:loc-cone-scope]], [[rem:loc-axis-scope]]). No result of the other chapters uses these
      developments.

  Item 9 without the Tier 2 section. New:

        construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge of
        data near the background's on the two null cones through the corner sphere of the explicit two-dust background of
        [[sec:bg-data]]: of data localised in an angular band away from the axes, with or without dust, on an explicit
        neighbourhood of the two cones, with an estimate, localised and unique in the gauge near the background off the axes
        ([[thm:loc-cone-development]]), and of data localised in angle or not on the whole rectangle of the two cones in which
        the two dusts cross, [0, 7.2] × [0, 4.5], with an estimate and unique in the gauge among nearby solutions
        ([[thm:loc-axis]], [[cor:loc-axis-cones]]); and exactly localised vacuum data

  Item 10 without the Tier 2 section. New:

      small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]). Data localised in
      angle on the two null cones exist exactly, and near the background's data, with the band away from the axes, they
      develop, dust included, on a neighbourhood of the cones, equal to the background outside a slightly wider band and unique
      in the gauge near the background off the axes ([[prop:loc-cones]], [[thm:loc-cone-development]]). Cone data near the
      background's, localised in angle or not, have a development on the whole rectangle of the two cones, [0, 7.2] × [0, 4.5],
      in which the two dusts cross, with an estimate and unique in the gauge among nearby solutions ([[thm:loc-axis]],
      [[cor:loc-axis-cones]]); developments of dust-carrying cone data that are not near the background's are not established
      ([[rem:loc-cone-scope]], [[rem:loc-axis-scope]]).

  These four lines start with "∩" or "4.5" in two places. Neither is a Markdown marker.

- **Items 2, 9 and 10: re-check after the Tier 1 nit round.** They are merged texts.
  - The word-level diff against Tier 1's current items 3, 6 and 7 shows only the Tier 3 insertions and the intended change
    of the last sentence of item 10.
  - Any change the Tier 1 nit round makes to those three new texts must be carried into them, and into item 3.
- **Items 4, 5 and 6: re-check after the Tier 1 nit round.** Their old texts quote rem:loc-cone-scope (ii) and (iv) and
  the last sentence of rem:loc-cone-local-scope as they stand now (P-CIVP.md lines 84–88, 93–95, 1016–1019).
- **The crosswalk.**
  - The new rows (scratchpad/pcivp3-crosswalk.tsv) are independent of Tiers 1 and 2.
  - The appended notes to the rows of rem:loc-cone-scope, rem:loc-cone-local-scope and rem:civp-large-domain must be
    applied to those rows as Tier 1's and Tier 2's crosswalk placements finally write them.
  - The lem:class-leaf-differences row source "P-CIVP3.md:969-989" is right for the current file.
- **Items 1, 8, 11 and 12** do not depend on the Tier 1/2 round. Item 11's "Tier 1's item 5 suffices" is still true.

---------------------------------------------------------------------------------------------------------------------

## C. Scratch merge and mechanical checks

The scratch copy is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpcivp3/,
the reader directory from HEAD df9a4c35 taken by git archive. The merge script is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpcivp3-cas/merge.py.
It stops if an old text does not occur exactly once as whole lines.

What was applied, in this order:
- Tier 1, as its current file places it:
  - Block A after the proof of prop:loc-cones;
  - Block B (lines 97–1038) before sec:loc-kid;
  - item 5 (introduction);
  - item 10 ([Ren90]).
  - Items 3, 4, 6 and 7 were not applied, because P-CIVP3's items 2, 3, 9 and 10 replace them.
- Tier 2, as its current file places it:
  - the section before sec:loc-kid;
  - item 4, first pair (ch:scope);
  - item 7 (Appendix A entries before thm:std-ctg-neighbourhood);
  - item 8 ([CCTW16]).
- Tier 3:
  - the section before sec:loc-kid;
  - items 2–6 and 8–10 as old/new pairs;
  - item 7 as the append, rewrapped. The last line becomes 103 characters long.

Results:
- Every old text was found exactly once, as whole lines, in the chapter or in the Tier 1/2 text it amends.
- python3 lint.py --chapters: "chapters: 62 file(s), 4766 label(s) defined, 0 hit(s)". The writer saw 10 hits; those
  were Tier 2's pending markers, now replaced.
- python3 assemble.py --check: "labels 4766, computations cited 0, problems 0".
- python3 assemble.py, run in the scratch copy only: "labels 4766, computations cited 0, problems 0". It wrote the
  scratch PAPER.md.
- python3 lint.py --paper: "PAPER.md: 0 hit(s)". This covers resolved line lengths and unresolved labels.
- P-CIVP3.md: the longest line is 121 characters, counted in characters. No wrapped prose line starts with "+ ", "- ",
  "* ", "> ", "#", "=" or "|". The one wrapped line that starts with "|" is inside the indented display at lines 375–376
  (nit 5).
- Crosswalk TSV: 31 rows, 4 tab-separated fields each.
  - The labels are in the order of the section, which is chapter order between the Tier 2 rows and sec:loc-kid.
  - Every row's line N equals the line of its label in P-CIVP3.md.
  - Every row equals the corresponding row text in the file.

---------------------------------------------------------------------------------------------------------------------

## D. What was checked and found correct

**Derivative counts and constants.**
- **m_0 = 6k + 18.**
  - lem:loc-cone-jets (iii) bounds a_j − å_j in C^(m_0 − 4j).
  - prop:loc-cone-formal uses r = k + 3 and needs a_j in C^(2r) for j ≤ r.
  - m_0 − 4(k + 3) ≥ 2(k + 3) holds exactly when m_0 ≥ 6k + 18. This gives ‖Δ‖_(C^(k+3)) ≤ Cε.
  - C^(k+3) is what the bounds of order k + 1 for the coefficients need (Ĝ enters with two derivatives), and what the C^k
    bound on R needs.
- **m_1 = 12k + 42 = 2p, p = m_0 + 3.** Data of size ε in C^(2p) extend with size Cε in C^(m_0):
  - The Borel terms of index j ≤ p have C^p norm ≤ C‖f − f̊‖_(C^(p+j)) ≤ Cε.
  - Y is in C^(p−1): the coefficient (1/12)|∂_vγ̂|² is in C^(p−1).
  - The W-equation has coefficients in C^(p−2) and 𝔯 is in C^(p−3), which holds second derivatives of γ.
  - So b is in C^(p−3) = C^(m_0).
- **cor:loc-axis-cones.** Free data in C^(m_1+3) give Y in C^(m_1+2), the W coefficients in C^(m_1+1), 𝔯 in C^(m_1), and
  so b in C^(m_1).
- **k ≥ 9.**
  - The competitor's fields are in C^(k−4), so the wave-map residual Γ[Ĝ] − Γ[g″] is in C^(k−5).
  - Bounds of order s for the coefficients and the forcing need g″ in C^(s+1).
  - So s = k − 5 is the largest admissible order, and s > d/2 + 1 = 3 gives k ≥ 9.
  - The exponent 1/(4s) is that of thm:class-kato-stability (a) with s′ = s − 1/4 > 3.
  - Uniqueness in C^(k−4) is the norm of the estimate (b), so the solution itself is a competitor.
- **The rest of the counts.**
  - The existence part works for k ≥ 6: lem:class-leaf-differences needs k ≥ 6, and the Sobolev order is k − 4 ≥ 2.
  - The C^(k−3) bounds follow from H^k ⊂ C^(k−3) in four dimensions.
  - The C^(k−4) estimate comes from g ∈ C^(k−2) and dΨ⁻¹ ∈ C^(k−4).

**No circularity in the smallness.**
- **ε_2 does not depend on Q1′.**
  - δ_2 is fixed by Q1, and the operators X_c have norms depending only on r and δ_2.
  - The cut-off β′ is fixed.
  - The Kato constants depend only on bounds of order s and on the fixed slab.
- **The angular localisation.**
  - It uses δ′ → 0 and ι → 0 inside one construction with δ_c fixed.
  - The energy argument on 𝒲 needs no smallness of 𝒲 or δ′: the leaf-wise constant does not depend on O, and Gronwall
    gives z = 0 for any constant.
- **Everything else.**
  - ρ, δ, 𝔅 and 𝔅′ are fixed about Ů before ε.
  - ε_0 depends on δ_c, β, ρ and C_2, all fixed in terms of k, u_1, v_1, δ_1 and the background.
  - In Lemma R the limit θ → 0 is local at a fixed t* (with Major 1's fix), and no other limit is taken.

**The axes.**
- **lem:loc-axis-constraints.**
  - (a): with Y = e^ϕ (sin ϑ cos ϑ)^(−1/3), γ̂ has the entries (sc)^(2/3) e^(2ℓ_i) and |∂_vγ̂|²_γ̂ = 4Σ(∂_vℓ_i)². The
    first line then equals the first line of eq:loc-cone.
  - The second line at X = ∂_ϑ equals the second line of eq:loc-cone: γ_ϑ 𝒱 = γ_ϑ^(3/2) e^(A_c+A_s) and
    2χ(W, ∂_ϑ) = 2γ_ϑ ∂_vϰ_1 ∂_vb. At X = K_i both sides vanish.
  - For the background, γ̂ = dΩ₃² and Y = R_e.
  - The equations of (b) are linear ODEs in v with coefficients smooth on S³, hence smooth through the axes.
- **lem:loc-axis-jets.**
  - The frame and the inverse metric of the double-null form were checked, including g^(va) = b^a g^(uv).
  - **eq:loc-axis-principal was checked by computer algebra (sympy).** Both lists hold exactly for a general constant
    3 × 3 metric γ, a vector b and Ω. The script is principal.py in the scratchpad's reader/rpcivp3-cas.
    - The first list holds: the terms with a u-derivative in E(∂_a, ∂_b), E(L̲, ∂_v) and E(L̲, ∂_a).
    - The second list holds, with L̲∂_v.
    - The ∂_v² terms vanish in all three components.
  - The derivation of 𝔏(Z) from the principal part was checked: 2c^uv ∂_vZ + 2c^ua ∂_aZ + (c^u + (j − 1)∂_u c^uu)Z.
  - The vanishing of the quadratic terms for j ≥ 2 by the factor u^(2j−2) was checked, and for j = 1 by (Ψ2) and (Ψ3).
  - The invertibility of (Z_Ω, Z_γ) ↦ ((2Ω²)⁻¹Z_γ, −2Z_Ω − ½ tr Z_γ) was checked.
  - The transport form on N_i was checked: the third component holds only L̲∂_v δb, and the ∂_v∂_cδγ terms cancel.
- **lem:loc-axis-leaf.**
  - (ii) was checked line by line:
    - the decomposition ∇_XY = ∇^S_XY − k(X,Y)ν + K_Σ(X,Y)n;
    - −p_A(∇_(e_1)e_1) = κ_A1 from ∇_(e_1)e_1 = −∇ψ_1;
    - θ_S = κ_A1 + p_A(ν)H_S − p_A(n) tr K_Σ|_(TΣ_S);
    - p_A(ν) = ±|p_A^Σ|, and Π = TΣ_S;
    - the Volterra integration from h_S′(0) = 0;
    - uniqueness by lem:class-volterra, and the converse.
  - (iii): the leaf equation along a curve uses p_A, Θ_A and the 1-jet of g only at its points.
  - For Ů and Û the spheres are a screen of P, so θ_S = −tr ∇²v = □(−v) = Θ̂_in. So the spheres are leaves in every slice
    of every time that is a function of (u, v), and not only on the faces. This makes σ_A[Û] local and the forcing F̃
    smooth without GN-T3's O(d^∞) argument, as the writer's departure 2 says.
- **lem:loc-axis-shear.**
  - Every step was checked:
    - |∂_zG| ≤ C(r + |p|) from E_L = (C3 r + A3 p)N_L²/det₂ − p + rB̃/a_L;
    - the C¹ foliation with Jacobian in [1/2, 2];
    - |z0 − z0′| ≤ 2|Δh|;
    - the two brackets;
    - the Gronwall bound |Δp| ≤ C(r𝒜w + ∫ρ𝒜w);
    - ‖Δq‖ + ‖Δh‖ ≤ C‖w‖ on 𝔻_R by ‖𝒜f‖_(L²) ≤ ‖f‖_(L²) for radial f (prop:class-flat-model (b) at j = 0, by density);
    - the change of variables in (4).
  - Only the first state's leaves need to stay in O. The second state's leaf from the same axis point is compared through
    w along the first state's leaf. So the one-sided hypothesis is sufficient, and the constant does not depend on O, in
    particular not on the width of the slice-triangles near τ_c. This answers GN-T3's GN2 without an extension operator.
- **The reduced problem.**
  - τ_u ≥ 1/(u + δ_c) and τ_v ≥ 1/(v + δ_c), and (τ, y) is a G-equivariant chart.
  - τ = 2 ln δ_c at the corner. Q1 ⊂ 𝔗(s* − 1), and τ ≥ s* + 1 where u ≥ l_u or v ≥ l_v, so 𝔗(s*) ⊂ [0, l_u) × [0, l_v)
    and F ∩ 𝒰^♯ = 𝔗(s*).
  - 𝒰^♯ is compact in the interior of Q^♯, and all the conormals are timelike.
  - Δ vanishes near Σ_init, and ψ_ax is smooth.
  - The closure eq:loc-axis-closure is Step 6 of thm:class-stability with κ_A⊥. The residual of Û is −E(P̂_A, P̂_A).
  - (F1)–(F3) hold on 𝒟_ρ.
  - In the Cauchy lemma, lem:class-kato-linear (c) with K_Z bounded gives a constant C independent of ε. It is right that
    thm:class-kato-stability is not used.
- **The past of the edges and propagation.**
  - The slices of P ∩ 𝒰^♯ are unions of Û-leaves. U = Û to all orders on N makes S_o(s) and S_i(s) leaves of U.
  - On 𝔗(s*) the U-leaves are ordered, the map z0 ↦ h(z0, y) having derivative in [1/2, 2]. So the leaf through a point
    of the slice between S_o(s) and S_i(s) stays between them.
  - The defect equation was re-derived: (1 − ψ_ax)(Θ + div P − 2κ_A1 − 2κ_A2) + ½ψ_ax(Θ + div P − 2κ_A⊥), the term
    −½ψ_ax(σ[U]² − σ[U′]²), and the gauge terms from prop:class-augmented (e).
  - The energy on 𝔗(s*) has no lateral boundary.
  - The signs of the densities follow by the argument of lem:loc-cone-constraints.
  - 𝒰′ = 𝒰^♯ is simply connected: it is the intersection of a down-set and an up-set of the quadrant, times S³.
- **The gauge, Lemma R and uniqueness.**
  - Ψ − id is Cε in C^(k−3). The inverse-metric computation gives the form eq:loc-double-null with fields smooth through
    the axes.
  - In Lemma R:
    - the chart x = e^(ṽ−μũ)ω̃ is G-equivariant, with ∂_t = (∂_ũ + μ∂_ṽ)/(1 + μ) future timelike exactly when
      4μΩ_1² > γ_1(b_1, b_1);
    - dũ(P_1^out) = 0 < dũ(P_1^in) on the far faces, so the boundary matrix there is nonnegative;
    - the level sets of a null phase in any slice are leaves, through lem:loc-axis-leaf (ii), so a genuine solution
      satisfies the axis closure in any slicing;
    - the comparison state W and the bound on 𝔫 are correct once Major 1 is fixed.
  - In lem:loc-axis-unique:
    - X_c is smooth and bounded on C^r (thm:std-ly-extension (i): it acts at fixed x′ and is bounded on every C^k), and
      f″ = 0 on P;
    - supp χ′ lies in the domain of g″;
    - φ = 0 on P;
    - Φ(F) ⊂ F and Φ(Q1′) ⊂ 𝔗(s*);
    - the hypotheses of Lemma R hold for (state of g̃, U) on R′ = Φ(Q1′);
    - the conclusion Ψ ∘ Φ = id on Q1′ is correct;
    - the competitor's densities need no smallness.
- **lem:loc-axis-angle.**
  - g_e⁻¹(ν, ν) = R_e⁻² − 2C_*²e^(−2σ_e) < 0, and ν(∂_τ), ν(P̊_A) and dτ_1 on the face {α = ι} are as stated.
  - The Ů-leaf arcs stay in O_s, because α depends on (u, v) only.
  - ψ_ax vanishes near axis 1 on 𝒲, because ρ1 ≥ ρ_-/√2 > δ/2.
  - Every point with ϑ < ϑ_a′ − 2C_*(uv)^(1/2) lies in some 𝒲.
  - The past P_out-curves stay in 𝒲. So the localisation reaches (uv)^(1/2), and the restriction ϑ_a′ ≤ π/4 keeps 𝒲
    away from the other axis.

**lem:loc-axis-rectangle: every number checked.**
- |R_u(7.2, 0)| ≤ 0.47 + 1.5 × 1.7/(3 × 2.25) = 0.8477…, which is ≤ 0.84778.
- f ≥ 1 − 0.8221253/2.25 = 0.634611…, which is ≥ 0.63461.
- R_v(7.2, 0) = f/(4|R_u|) ≥ 0.63461/3.39112 = 0.187139…, which is ≥ 0.18713.
- R(7.2, 3) ≥ 1.5 + 3 × 0.18713 = 2.06139.
- 1 − 3.6059/2.0613² = 0.15134 > 0.15.
- The steps: σ_v ≥ 0 from σ_uv > 0 and σ_v = 0 on 𝒞_out; e^(−2σ)R_v is constant in v on {v ≤ 3}; μ_u ≤ 0 while R_v ≥ 0;
  the continuity argument giving v′ = v*; v* = 4.5, from ∂G ⊂ {R = a}; the open set {p ∈ G : R > a}; and R_e > 0 on Q^♯
  after decreasing δ_1.
- The cited facts check: μ ≤ 3.6059 in region I (lem:margins-region-one (a)), μ(7.2, 0) = μ3 ≤ 0.8221253 and R > 1.5 on
  𝒞_in ∩ {u ≤ 7.2}.

**Cited results.**
Each cited result says what is used, at the hypotheses used:
- chapter 81: lem:class-gauss, lem:class-leaf, lem:class-volterra, lem:class-planar-shear step (1),
  lem:class-leaf-differences (a), (b) and its last sentence, prop:class-flat-model (b), prop:class-axis (d),
  prop:class-structure (b), (c), prop:class-augmented (b), (e), eq:class-gauge-wave, eq:class-identity, eq:class-x,
  eq:class-raychaudhuri, thm:class-kato (a), lem:class-kato-linear (a)–(c), thm:class-kato-stability (a),
  rem:class-kato-local, lem:class-composition, Steps 6, 9 and 10 and *Smoothness* of thm:class-stability;
- Tier 1: lem:loc-cone-borel, lem:loc-cone-jets (i)–(iv) and (Ψ1)–(Ψ3), prop:loc-cone-formal, lem:loc-cone-system,
  lem:loc-cone-energy and the paragraph after it, lem:loc-cone-past, lem:loc-cone-support, lem:loc-cone-constraints,
  lem:loc-cone-gauge, lem:loc-cone-unique, lem:loc-cone-extension, lem:loc-cone-strips;
- chapters 80 and 83, and Appendix A: lem:two-dust-identities (i), (iv), lem:two-dust-reparametrisation (b),
  prop:two-dust-background (b)–(d), lem:bg-reduction (a), lem:margins-region-one (a), thm:std-ly-extension (i).

The exceptions are those listed in the findings: ů := U_1 (nit 3), the energy lemma's transversality (nit 4) and the
lens step number (nit 20).

**Self-containedness.**
- Section text: no file or program names, no code, no AI or process language (lint 0 hits in the merged chapters), and no
  pending markers.
- Every statement is proved. The exceptions are the remark of minor 5 and the unstated property of minor 3.
- rem:loc-axis-scope (ii) is a description of the method's limits and asserts no result.
- The writer's departures from GN-T3 (items 1–9 of the report) were each checked and are sound:
  - the one-sided leaf-wise lemma in place of T3-2 (a)/(b);
  - the local residual of Û in place of the O(d^∞) argument;
  - the adapted time τ with the M β terms;
  - k ≥ 9 with uniqueness in C^(k−4), ε_2 independent of Q1′;
  - Lemma A (ii) with p_A vanishing as a hypothesis;
  - Lemma R by continuity without smallness (with Major 1's fix);
  - ϑ_a′ ≤ π/4;
  - the two families only;
  - the traced constants (with minor 5).

---------------------------------------------------------------------------------------------------------------------

## Confirmation (fix round)

File read: proofs/P-CIVP3.md, md5 d4c83116408265dc0c64406172842077, 1,102 lines. The section is lines 1–823, the
Placement starts at line 825 and the crosswalk rows at line 1057. Branch head was 4cce58ac, with Tiers 1–2 merged into
chapter 83 at f7b0cab8. Also read:
- the writer's fix report, notes/reports/P-CIVP3.md;
- chapter 83 as merged: lem:civp-large-free, lem:civp-large-rectangle, lem:loc-cone-energy and the paragraph after it,
  (Ψ1)–(Ψ3) of lem:loc-cone-jets, rem:loc-cone-scope, the paragraph after it, rem:loc-cone-local-scope and
  rem:civp-large-domain;
- chapter 01, line 192, and chapter 90, lines 210–218.

The section text was compared line by line with the reviewed version (1d196fae…) by diff, and every changed passage was
re-read in full.

**Verdict: CONFIRMED.** No Major, minor or nit is open.

### The first-round findings

- **Major 1 (Lemma R).** Resolved. Lines 649–674 carry the replacement.
  - 𝒦 := R′ ∩ {t ≤ t*} is convex in (ũ, ṽ), and Taylor's formula along segments to it bounds the derivatives of order at
    most k of U_2 − U_1 on 𝒩_θ by Cθ^(k+1).
  - So W − U_1 is at most Cθ in C^k, and W ∈ 𝔅′ for θ small.
  - The leaf of W and the level set of U_2's phase stay within Cθ² < θ/4, so both stay in 𝒩_(θ/2).
  - ϵ′ no longer occurs, the order of the quantifiers is right, and the energy step still uses no smallness.
  - The parenthesis of nit 3 is in place.
- **minor 1.** Resolved: ±2|p_A^Σ| σ_L, the sign that of p_A(∂_z), with σ_L taken for the normal ν of lem:class-leaf (b).
- **minor 2.** Resolved: "extends to a smooth field of Lorentzian forms on D × S³".
  - This is right for an edge D too. The forms act on the five-dimensional tangent spaces along D × S³.
  - Non-degeneracy is what the stated equivalence needs: a kernel vector of γ at an axis point would be a kernel vector
    of g.
- **minor 3.** Resolved in the statement of (c) and in its proof.
  - At such points every v-derivative of f − f̊ at v_1 vanishes, so every Borel term vanishes and f̃ = f̊.
  - γ̃ = dΩ₃² there, so the renormalisation factor is 1.
  - The equations of (b) have the background's coefficients and initial values on the open set, so their solutions are
    the background's.
  - lem:loc-axis-angle can now be applied to the extended data, as the proof of (d) needs.
- **minor 4.** Resolved. (Ψ1) and (Ψ3) of the merged lem:loc-cone-jets (83:1027–1032) say what the new text attributes
  to them.
- **minor 5.** Resolved: four places in the existence proof, plus the uniqueness wave map.
- **minors 6 and 7.** Resolved by the re-base.
  - Item 9 lists the two kinds of data separately.
  - Item 3 now only inserts a sentence and renames the next sentence's subject. The merged Tier 1/2 clause
    ("with v_1 = 4.5 and u_1 = 7.2 …, ([[lem:civp-large-free]], [[lem:civp-large-rectangle]])") stands untouched in the
    merged chapter.
- **Nits 1–20.** All resolved, and the writer's variants are correct:
  - nit 1 adds 2δ_e < δ_1, which is why the extension by 0 is smooth;
  - nit 2 states the evaluation of F_0 explicitly;
  - nits 3 and 5–20 apply as given, with the letter ξ in nits 11 and 19;
  - nits 16–18 are in the re-based items 4, 2 and 6.
- **Nit 4, the writer's extension.** The writer also drops the transversality of the faces from lem:loc-axis-energy, and
  this is correct. The proof of lem:loc-cone-energy uses of the boundary only:
  - the divergence theorem on the Lipschitz domains 𝒟_s;
  - the nonnegative boundary matrix on the smooth pieces of B_1;
  - z = 0 on B_0.

  lem:loc-axis-angle now cites lem:loc-axis-energy for its Lipschitz domains. These lie below the graph of the minimum of
  two decreasing smooth functions of u, times the angular condition.

### lem:loc-axis-rectangle removed: Tier 2's lem:civp-large-rectangle (a) gives everything the corollary uses

The removed lemma supplied one thing to the theorem: a background on Q1 with margin δ_1. That means σ_e and R_e > 0
smooth on Q^♯ = [−δ_1, u_1 + 2δ_1] × [−δ_1, v_1 + 2δ_1], solving eq:two-dust-limit on Q^♯ ∩ F, with
δ_1 ≤ min(u_1, v_1)/2. Its other conclusions, R ≥ 1.5 and R_v > 0, are used by no step of the section.

lem:civp-large-rectangle (a) gives, for every v_1 > 0 and δ ∈ (0, 1/2):
- [0, 7.2] × [0, v_1] ⊂ G;
- the background smooth on [0, 7.2 + 2δ] × [0, v_1 + 2δ], solving eq:two-dust-limit there, with R > a;
- σ and R extended by Borel sums to smooth functions, with R > 0 and Ω = e^σ/√2 > 0 on [−δ, 7.2 + δ] × [−δ, v_1 + δ].

The corollary's proof takes δ_1 := min(δ, v_1)/2, σ_e := ln(√2 Ω) = σ and R_e := R. Then:
- δ_1 ≤ v_1/2, and δ_1 < 1/4 < 7.2/2, so δ_1 ≤ min(u_1, v_1)/2;
- −δ_1 ≥ −δ and 7.2 + 2δ_1 ≤ 7.2 + δ, so Q^♯ ⊂ [−δ, 7.2 + δ] × [−δ, v_1 + δ], where σ_e and R_e > 0 are smooth;
- Q^♯ ∩ F ⊂ [0, 7.2 + δ] × [0, v_1 + δ], where the background solves the equations;
- the extended σ and R equal the background's on F.

So the hypothesis of thm:loc-axis holds for Q1 = [0, 7.2] × [0, v_1] and every v_1 > 0. C_* = sup over Q^♯ of
e^(σ_e)/R_e is finite.

The rest of the corollary's proof is unchanged and correct:
- Y is in C^(m_1+2), the W-coefficients in C^(m_1+1), 𝔯 in C^(m_1) and b in C^(m_1).
- The data have size Cε in C^(m_1) and nonnegative densities.
- The statement with v_1 = 4.5 gives the shell and the packet perturbed at once.

No file cites the removed label. The label sec:loc-axis-example keeps its heading, and the crosswalk row is rewritten to
match.

### The placement against HEAD

The scratch copy is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpcivp3-r2/,
a git archive of HEAD 4cce58ac. The script that parses and applies the placement is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpcivp3-cas/merge_r2.py.
It took the first new texts, the ones without the null-shell section. It inserted the section before sec:loc-kid and
applied items 2–10 in order. Every old text was found exactly once, as whole lines:

| item | chapter | line at HEAD |
|---|---|---|
| 2 | 83 | 13 |
| 3, first pair | 83 | 694 |
| 3, second pair | 83 | 704 |
| 4 | 83 | 676 |
| 5 | 83 | 685 |
| 6 | 83 | 1628 |
| 7 | 83 | 2369 |
| 8 | 81 | 1326 |
| 9 | 03 | 376 |
| 10 | 90 | 217 |

Item 7 is now an old/new pair, as asked. The line numbers in the table are those of HEAD; the script found the later
items shifted by the earlier ones.

Results:
- Before the merge, lint.py --chapters gave 0 hits on 4782 labels, and assemble.py --check gave 0 problems.
- After the merge, lint.py --chapters gave "chapters: 62 file(s), 4812 label(s) defined, 0 hit(s)".
- assemble.py --check gave "labels 4812, computations cited 0, problems 0".
- assemble.py, in the scratch copy only, gave 0 problems.
- lint.py --paper gave "PAPER.md: 0 hit(s)".
- In P-CIVP3.md no non-TSV line is over 121 characters, and no wrapped line starts with a Markdown marker. This includes
  the three null-shell variants.
- The crosswalk has 30 tab-separated rows of 4 fields each, one per label, in chapter order, with every PENDING:N
  equal to its label's line. The scratchpad copy pcivp3-crosswalk.tsv is identical to the file's rows.
- The changed row of lem:class-leaf-differences cites lines 975–997, which are the lines of item 8.

The merged texts read correctly in place (chapter 83, lines 8–16 and 660–718 of the scratch copy; chapter 90, lines
210–222):
- Item 2's sentence cites thm:loc-axis and cor:loc-axis-cones.
- Item 3 inserts the whole-rectangle sentence, for every [0, 7.2] × [0, v_1], and keeps the merged Tier 2 clause.
- Item 3's last sentence now excludes only data that are not near the background's at an axis, citing
  rem:loc-axis-scope.
- Item 4 qualifies the whole rectangle by the margin and ends on the line before the null-shell item 2's line.
- Item 5 cites lem:civp-large-rectangle (a) for every v_1.
- Items 6, 9 and 10 read as intended.
- Item 11 is right. Chapter 01, line 192, carries "localised data, their development from two null cones".

The null-shell variants of items 3, 7 and 10 were checked only for what Tier 3 adds:
- item 3: "and are not near the background's ([[rem:loc-axis-scope]])";
- item 7: the appended sentence on thm:loc-axis;
- item 10: the whole-rectangle sentence and the narrowed last sentence.

Each is present, unchanged from the first new text, and consistent with it.

Item 13 is dropped. The writer also notes that items 3 and 6 must be merged by hand if Tier 4's thm:civp-axes is
placed. Both need nothing now.

---------------------------------------------------------------------------------------------------------------------

## Final confirmation

File read: proofs/P-CIVP3.md, md5 dfa0b5519b02565e8586e46db00d12a4, 1,109 lines. Branch head was 0c8952c0, with the
null-shell section merged at 878e20e2.

**Verdict: CONFIRMED.** No finding is open.

### The section did not change

Lines 1–823 are byte-identical to the confirmed d4c83116 (checked by diff). The full diff, d4c83116 → dfa0b5, is 167
lines and identical to the coordinator's P-CIVP3.d4c831-to-dfa0b5.diff. Every change lies in the Placement and in the
crosswalk prose.

### Each changed item

- **Header.**
  - The variants "with the null-shell section" are gone, since that section is merged.
  - The header says that at items 3, 7 and 10 the null-shell wording is kept verbatim and only Tier 3's additions are
    made. This is true; see the word diff below.
- **Item 1.**
  - rem:civp-large-beyond ends at 83:2407 with "not explicit and no estimate of the solution is given.", and
    "### Null shells along the leaves {#sec:loc-shells}" is at 83:2409. Both were checked at HEAD.
  - In the assembled scratch paper the order is §53.5 (without smallness), §53.6 (through the axes), §53.7 (null shells).
- **Items 3 (first part), 4, 5 and 6.** Only the line numbers (707–708, 684–688, 698–700, 1644–1646) and item 4's note
  changed.
  - The note says (iii) begins on the next line and is unchanged, which is right.
  - The old texts are unchanged and found once.
- **Items 3 (continued), 7 and 10.** Word-level diffs of old against new give the following.
  - **Item 3, continued:** only "axis," → "axis and are not near the background's ([[rem:loc-axis-scope]]),". The
    null-shell wording, "with densities smooth in angle … where the metric functions are continuous …", is otherwise
    verbatim.
  - **Item 7:** only the appended sentence "Cone data near the background's that differ from it at the axes are developed
    on the whole rectangle by [[thm:loc-axis]].".
  - **Item 10:** only three changes, and the null-shell sentence is verbatim:
    - the inserted whole-rectangle sentence (thm:loc-axis, cor:loc-axis-cones);
    - "and are not near the background's";
    - "([[rem:loc-cone-scope]])" → "([[rem:loc-cone-scope]], [[rem:loc-axis-scope]])".
- **Item 13.** It is a rewrap only: the word sequences of old and new are identical.
  - It is needed. Merged without it, lint.py --paper reports one line of 122 characters ("in u (∂_uΨ = G < 0 since
    f > 0, Proposition 53.102) …"). With it there are 0 hits.
- **Crosswalk.**
  - The prose "before the row of sec:loc-shells" matches crosswalk/83-localised-data.tsv, where rem:civp-large-beyond is
    row 89 and sec:loc-shells row 90.
  - The changed row of lem:class-leaf-differences cites lines 965–987, which are the lines of item 8.
  - The 30 rows are unchanged: 4 fields each, with correct line numbers, identical to scratchpad/pcivp3-crosswalk.tsv.

### Only what is proved

Each new text claims only what the theorems prove.
- The additions say that data near the background's are developed on the whole rectangle when the background has a
  margin. That is thm:loc-axis, and cor:loc-axis-cones for [0, 7.2] × [0, v_1].
- The narrowed exclusions concern data that differ from the background's near an axis without being near them. That is
  rem:loc-axis-scope.
- Nothing about null shells is restated or widened.

### Scratch merge

The scratch copy is
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/rpcivp3-r3/,
a git archive of HEAD 0c8952c0. The script is rpcivp3-cas/merge_r3.py. It inserted the section before sec:loc-shells and
applied items 2–10 and 13. Every old text was found exactly once, as whole lines:

| item | chapter | line at HEAD |
|---|---|---|
| 2 | 83 | 13 |
| 3, first part | 83 | 707 |
| 3, continued | 83 | 717 |
| 4 | 83 | 684 |
| 5 | 83 | 698 |
| 6 | 83 | 1644 |
| 7 | 83 | 2385 |
| 8 | 81 | 1326 |
| 9 | 03 | 376 |
| 10 | 90 | 217 |
| 13 | 83 | 4707 |

Results:
- Before the merge, lint.py --chapters gave "4803 label(s) defined, 0 hit(s)".
- After the merge, lint.py --chapters gave "chapters: 62 file(s), 4833 label(s) defined, 0 hit(s)".
- assemble.py --check gave "labels 4833, computations cited 0, problems 0".
- assemble.py, in the scratch copy only, gave 0 problems.
- lint.py --paper gave "PAPER.md: 0 hit(s)".
- In P-CIVP3.md no line outside the crosswalk rows is over 121 characters, and no wrapped line starts with a Markdown
  marker.
