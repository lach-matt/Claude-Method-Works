# R-P-SHELL: independent line-by-line reading of proofs/P-SHELL.md

File read: `research/warp-drive/paper/reader/proofs/P-SHELL.md`, md5 cc81a1ade67f193e898240dee404db85, 759 lines (the
section, lines 1-629; the Placement, 631-733; the crosswalk rows, 735-759). Every line was read.

Also read: chapter 83 at HEAD (sec:loc-cones, eq:loc-double-null, lem:loc-cone-equations, prop:loc-cones, the opening),
chapter 80 (lem:two-dust-equations, eq:two-dust-mass, prop:two-dust-background with eq:two-dust-volterra), chapter 81
(eq:class-system), chapter 90 (the paragraph on localised data), chapter 98 (around [Rac16]), Appendix A (to see which
elementary results it quotes); the Tier 1 file proofs/P-CIVP.md in three states: as of the P-SHELL commit 80018e91 (md5
aa08312166da99581416a9753bad3c98, the version the writer used), and as now committed and in the working tree (md5
280a89e05902d035236edf531de3a5a5, revised after the review R-P-CIVP); the Tier 2 file proofs/P-CIVP2.md (md5
924a45ecfbef762ee34a500044e9414f, unchanged throughout); the writer's report notes/reports/P-SHELL.md, the scoping report
notes/reports/S-T6.md (section 3.2), the Tier 1 review notes/reviews/R-P-CIVP.md (sections A-C); Poisson, arXiv
gr-qc/0207101v1, pp. 1-7, through the alphaXiv paper reader. Nothing under method/, drive/, extracted/ or recovered/ was
read. No chapter, crosswalk or proof file was edited.

Private checks (sympy 1.14, in the session scratchpad under reader/pshell/ only): `ricci.py` computes the full Ricci
tensor of eq:loc-double-null with Ω, γ_ϑ, b, A_c, A_s arbitrary functions of (u, v, ϑ), and checks both identities of
lem:loc-shell-identities, their round case, and the δ-parts of lem:loc-shell-ricci (see section F). A scratch build
(reader/pshell/build/) inserts Tier 1's Blocks A and B, the Tier 2 section and this section into chapter 83, applies
items 2-6, assembles the paper and lints it.

**Verdict: NOT CONFIRMED.** 0 Major, 10 minor, 9 nits. The mathematics is correct. lem:loc-shell-ricci,
lem:loc-shell-identities and prop:loc-shell-junction re-derive exactly, by hand and in sympy. prop:loc-shell-cones, the
slab-by-slab proof of thm:loc-shells (a)-(c) and prop:loc-shell-crossing are sound under the two pending statements,
which are honest gaps stated in full. The minor findings are of three kinds:
- one derivative count in the proof of (d) that the text states inconsistently (minor 1);
- precision in the Poisson remark and in prop:loc-shell-crossing (minors 2-6);
- placement texts that no longer compose with the Tier 1 revision now in progress, plus one site the placement misses
  (minors 7-10).

Every replacement text below has been checked: at most 121 characters per line, also with labels replaced by resolved
numbers, and no wrapped line starts with a Markdown marker.

---------------------------------------------------------------------------------------------------------------------

## A. Findings

### minor 1: the derivative count after the change of angle back (proof of (d), lines 486-491 and 495)

Current (lines 487-491):

    b(0, c_k, ·). So the data have size at most Cε, and for ε small (T1) gives a solution on {0 ≤ u ≤ l_u, c_k ≤ v ≤ v_1,
    u(v − c_k) ≤ δ_*,k²}, which contains [0, λ_(k+1)^out] × [c_k, v_1] with λ_(k+1)^out := min(l_u, δ_*,k²/(v_1 − c_k)); it
    is within Cε of the background's with its derivatives of order at most k_k − 4 in the transformed angle, and k_k − 5 ≥ 1
    after the angle is changed back. Along 𝒞_in the same holds with l_v := (2/3) λ_j^in, l_u := u_1 − d_j and no change of
    angle.

and (line 495) "the rectangle of depth N − 1 giving k_(N−1) − 5 = 1".

What is wrong. The text says that changing the angle back costs one derivative: order k_k − 4 becomes k_k − 5. At the
next depth, though, it takes the N_i data from that solution "within Cε … with their derivatives of order at most
k_(k−1) − 4" (lines 483-484). For depth k − 1 ≥ 1 this is one more derivative than the text has established. Read
literally, the transformed data at depth k ≥ 2 are then in C^(k_(k−1) − 6) = C^(6k_k + 17), one short of the m_0 =
6k_k + 18 that (T1) needs. The cascade k_(i−1) = 6k_i + 23 is nevertheless right, because changing back costs nothing.
The inverse change composes the functions with Φ_k, multiplies γ_ϑ by (∂_ϑΦ_k)² and replaces b by
(b ∘ Φ_k − ∂_uΦ_k)/∂_ϑΦ_k. Φ_k − id is within Cε in C^(k_(k−1) − 4), so its first derivatives are within Cε in
C^(k_(k−1) − 5). Since k_(k−1) − 5 = 6k_k + 18 ≥ k_k − 4, the order k_k − 4 survives. The theorem's C¹ claim is
unaffected. Replacement for lines 487-491:

    b(0, c_k, ·). So the data have size at most Cε, and for ε small (T1) gives a solution on {0 ≤ u ≤ l_u, c_k ≤ v ≤ v_1,
    u(v − c_k) ≤ δ_*,k²}, which contains [0, λ_(k+1)^out] × [c_k, v_1] with λ_(k+1)^out := min(l_u, δ_*,k²/(v_1 − c_k)); it
    is within Cε of the background's with its derivatives of order at most k_k − 4 in the transformed angle, and also after
    the angle is changed back, which composes the functions with Φ_k, multiplies γ_ϑ by (∂_ϑΦ_k)² and replaces b by
    (b ∘ Φ_k − ∂_uΦ_k)/∂_ϑΦ_k: the first derivatives of Φ_k are within Cε of those of the identity in C^(k_(k−1) − 5), and
    k_(k−1) − 5 ≥ k_k − 4. Along 𝒞_in the same holds with l_v := (2/3) λ_j^in, l_u := u_1 − d_j and no change of angle.

and in line 495 "k_(N−1) − 5 = 1" by "k_(N−1) − 4 = 2". (Alternatively, keep the loss and set k_(i−1) := 6k_i + 24; the
replacement above is the smaller change.)

### minor 2: what Poisson describes (rem:loc-shell-poisson, lines 259-268)

Current: "Poisson's reformulation of the null-shell formalism of Barrabès and Israel describes the δ-part of the Ricci
tensor of a metric that is continuous across a null hypersurface by "a mass density, a mass current, and an isotropic
pressure" [Poi02, p. 1], through "S^(αβ) = …" [Poi02, (2.15), p. 4]"; and "such a jump is what [Poi02, p. 1] calls "an
independent impulsive tidal wave", a δ in the Weyl tensor."

What is wrong.
- The quoted words are verbatim on p. 1 of v1, and (2.15) is verbatim on p. 4. But in [Poi02] the triple describes the
  shell's surface stress-energy tensor, not the δ-part of the Ricci tensor. p. 1 reads "This construction provides the
  stress-energy tensor with a simple characterization in terms of a mass density, a mass current, and an isotropic
  pressure."
- S^(αβ) is formed from the singular part of the Einstein tensor ((3.7)-(3.8), p. 5). In four dimensions its trace is 2p,
  so the δ-part of Ric is not S^(αβ) when p ≠ 0.
- The comparison is still exact here, because 𝒮_k and 𝒮′_j are trace-free: g⁻¹(dv, dv) = g⁻¹(du, du) =
  g⁻¹(dv, dϑ − b du) = 0. So they are also the δ-parts of the Einstein tensor. The remark should say so.
- [Poi02] says that "the singularity in the Weyl tensor is interpreted as an independent impulsive tidal wave". It says
  nothing about jumps of the shear.

Replacement for lines 259-268:

    **Remark {#rem:loc-shell-poisson}** (Null shells in four dimensions.) In four dimensions, Poisson's reformulation of the
    null-shell formalism of Barrabès and Israel associates with the δ-part of the curvature of a metric that is continuous
    across a null hypersurface a surface stress-energy tensor, formed from the δ-part of the Einstein tensor, and gives it
    "a simple characterization in terms of a mass density, a mass current, and an isotropic pressure" [Poi02, p. 1]:
    "S^(αβ) = μk^α k^β + j^A (k^α e^β_A + e^α_A k^β) + p σ^(AB) e^α_A e^β_B" [Poi02, (2.15), p. 4], k tangent to the null
    generators. [[lem:loc-shell-ricci]] is the analogue in five dimensions and in the gauge of the class, proved directly.
    By its part (b), 𝒮_k and 𝒮′_j are trace-free, as g⁻¹(dv, dv) = g⁻¹(du, du) = g⁻¹(dv, dϑ − b du) = 0, so they are also
    the δ-parts of the Einstein tensor. On an ingoing leaf, whose generators are tangent to L̲ = −2Ω² g⁻¹dv, the term in
    dv ⊗ dv is the density, the term in [∂_v b] the current, and no pressure term occurs; a null-dust shell, whose stress is
    a multiple of dv ⊗ dv, is the case of zero current, (J1). A jump of the derivatives of the ϰ_i − ϕ across a leaf
    produces no δ in Ric; in four dimensions such a jump gives a δ in the Weyl tensor, which [Poi02, p. 1] interprets as "an
    independent impulsive tidal wave". No proof here uses [Poi02].

(The identifications themselves are right. In Poisson's terms, for the leaf {v = c} with generator L̲ and transverse
direction ∂_v: μ ∝ σ^(AB)[∂_v g_AB] = 2[tr χ]; j_ϑ ∝ [∂_v g](∂_ϑ, L̲) = −γ_ϑ[∂_v b]; and p ∝ [∂_v g](L̲, L̲) = 0.
Crosswalk row 752 needs no change.)

### minor 3: the definition and lemmas are applied on sets that are not past sets (prop:loc-shell-crossing (b)-(c))

Current: def:loc-shell-solution, lem:loc-shell-ricci and prop:loc-shell-junction are stated for "a past set D ⊂ Q1". But
(b) and (c) assert solutions with null shells on (𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s]) × S³ and on (𝔏 ∪ D″) × S³.
Their proofs apply prop:loc-shell-junction (a)-(d) "to the extended metric". Neither 𝔏 nor these unions is a past set:
[0, u] × [0, v] leaves 𝔏 at u < d_j − λ.

What is wrong. Strictly, the definition is used outside its domain. The proofs use of a past set only one property: it
meets the lines {u = const} and {v = const} in intervals. This is used in the integration by parts of lem:loc-shell-ricci
(a) and in the derivation of the shell laws in prop:loc-shell-junction (d). The exception is the last sentence of
prop:loc-shell-junction (a), where the curves start at u = 0. The three sets have that property. Replacement for lines
500-502 (the end of the opening paragraph of the proposition):

    a solution with null shells along the leaves on D × S³, and Z := {(d_j, c_k)} × S³ a crossing sphere in D. Number the
    four cells at Z by (±, ±), the first sign being that of u − d_j and the second that of v − c_k, and write F_(±±) for the
    value at a point of Z, from the cell (±, ±), of a cellwise smooth function F. For a set D′ ⊂ Q1 that meets every line
    {u = const} and {v = const} in an interval, a solution with null shells along the leaves on D′ × S³ is defined by
    [[def:loc-shell-solution]] with D′ in place of D, and [[lem:loc-shell-ricci]] and [[prop:loc-shell-junction]] hold for
    it with the same proofs, which use of a past set only this property, except that in (a) of the latter [∂_v b] vanishes
    along each integral curve of L̲ in the leaf that starts at a point where it vanishes. The sets 𝔏,
    𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s] and 𝔏 ∪ D″ of (b) and (c) have this property.

(The last clause is exactly what the proof of (c) uses at lines 592-593: [∂_v b] vanishes from Z on along the new part of
the leaf.)

### minor 4: the crossing rule needs all four cells (prop:loc-shell-crossing (a), lines 504-505)

Current: "Z := {(d_j, c_k)} × S³ a crossing sphere in D" and "(a) *The crossing rule.* At every point of Z, tr χ_(+−) =
…".

What is wrong. D is only a past set containing Z. If Z lies on its boundary, as in the situation of (b) and (c), the
values from the cells (+, +), (+, −) or (−, +) need not exist, and neither do the jumps on both sides of Z. Replacement
for lines 504-505:

    (a) *The crossing rule.* If D contains a neighbourhood of (d_j, c_k), then at every point of Z, tr χ_(+−) = tr χ_(−−),
    tr χ_(++) = tr χ_(−+), tr χ̲_(−+) = tr χ̲_(−−) and tr χ̲_(++) = tr χ̲_(+−), so that

(The proof of (a) and its uses after the extensions of (b) and (c) are unchanged. After an extension, Z has a
neighbourhood in the new domain.)

### minor 5: "continuous coefficients" through crossing spheres (proof of prop:loc-shell-junction (a), lines 204-206)

Current: "Along an integral curve of L̲ in the leaf, [[eq:loc-shell-torsion]] is a linear homogeneous ordinary
differential equation for [∂_v b] with continuous coefficients, so [∂_v b] vanishes along the curve if it vanishes at its
starting point."

What is wrong. The coefficient L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) holds ∂_u-derivatives, which jump across {u = d_j}.
Along a curve through a crossing sphere the coefficients are only piecewise continuous. The conclusion still holds:
[∂_v b] is continuous at the crossing spheres, which the sentence just before proves, and uniqueness holds piece by
piece. Replacement for lines 204-206 (from "u < d_j and from u > d_j." to "starting point."):

    u < d_j and from u > d_j. Along an integral curve of L̲ in the leaf, [[eq:loc-shell-torsion]] is a linear homogeneous
    ordinary differential equation for [∂_v b] whose coefficients are bounded and continuous off the crossing spheres, at
    which [∂_v b] is continuous; so [∂_v b] vanishes along the curve if it vanishes at its starting point.

(Line 206 continues "When b vanishes near the axes, …" unchanged. The same remark applies to (b), but there the
coefficient ∂_ϑ b is continuous everywhere, so the text of (b) is correct as it stands.)

### minor 6: the transverse densities on the restart edges come from (J3), not from continuity (lines 453 and 599-601)

Current (line 453): "g̃ induces the cone data on N_o ∩ D′ and, being continuous, the functions of g_(k−1)^out on N_i ∩
D′". The functions on N_i are Ω, γ_ϑ, b, A_c, A_s and q_out (Step 2, line 400). Likewise (line 600): "and, being
continuous, induces on N_o ∩ D″ and N_i ∩ D″ the functions of the given solution".

What is wrong. For a solution with null shells, continuity covers only the metric functions; q_out on N_i (q_in on N_o)
may a priori jump. Its continuity is (J3), which prop:loc-shell-junction (d) gives for every such solution. Replacement
for lines 453-454 (from "data on N_o ∩ D′" to "D′ ∩ 𝒮_k^out."):

    data on N_o ∩ D′ and the functions of g_(k−1)^out on N_i ∩ D′ ⊂ 𝒮_(k−1)^out: Ω, γ_ϑ, b, A_c and A_s by continuity,
    q_out by (J3) of [[prop:loc-shell-junction]] (d). After the change of angle Φ_k, which depends only on these functions,
    (T2) (c) gives g̃ = g_k^out on D′ ∩ 𝒮_k^out.

(the next words "In the same way g̃ = g_j^in on" then start the following line, reflowed), and for lines 600-602:

    in the gauge on a past set of 𝒬 that equals g0 near the axes and induces on N_o ∩ D″ and N_i ∩ D″ the functions of the
    given solution, the metric functions by continuity and q_in and q_out by (J3) of [[prop:loc-shell-junction]] (d); after
    the same change of angle, (T2) (c) shows that it equals the development on D″ ∩ 𝒬_δ.

### minor 7: item 2's old text is no longer in the Tier 1 text (Placement, lines 653-666)

Current old text (lines 655-656), two lines ending "… and near" / "… are not covered. For the".

What is wrong. It occurred exactly once in Block A of P-CIVP.md as of the P-SHELL commit (md5 aa083121…). Since then
Tier 1 has been revised after its review. In the version now committed and in the working tree (md5 280a89e0…),
rem:loc-cone-scope is reflowed, and the old text occurs 0 times. (Tier 1's revision also changes (i) of the same remark,
its minor 11, which does not touch (iii).) The placement must be re-based on Tier 1's final text. Against the current
text, Old (lines 88-89 of P-CIVP.md):

    the background there. (iii) *Regularity.* The data are smooth and near the background's in C^m, m = 6k + 21. Densities
    that are only bounded, or measures (shells), are not covered. For the 3 + 1 problem with two families of null dust,

New:

    the background there. (iii) *Regularity.* The data are smooth and near the background's in C^m, m = 6k + 21. Densities
    that are only bounded, and measure-valued densities in general, are not covered. Finitely many null shells along leaves
    {v = c} of 𝒞_out and {u = d} of 𝒞_in, with densities smooth in angle and supported in the band, and data that are smooth
    except across finitely many such leaves, are covered by [[thm:loc-shells]]: their development is continuous, smooth
    between the leaves and a solution in the sense of distributions ([[def:loc-shell-solution]]), and near the background's
    data it exists on a neighbourhood of the two cones that does not depend on the data ([[thm:loc-shells]] (d)). For the
    3 + 1 problem with two families of null dust,

(The words are the writer's, reflowed. The old text occurs exactly once in the current P-CIVP.md.)

### minor 8: item 5 does not compose as it says (Placement, lines 701-714)

Current: "The Tier 1 placement (its item 7) and the Tier 2 placement (its item 4) each append text to this line; the text
below is appended after theirs, at the end of the paragraph as they leave it." The Old is the line "small amplitude when
the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]])." The New is that line followed by
"Cone data with finitely many null shells …".

What is wrong.
- Applied as given, the pair puts the new sentence directly after "([[thm:charge-sign]])." That is before the Tier 1 and
  Tier 2 text that follows on the same line, not after it.
- Once those placements are in, the old line is no longer a whole line, so "every old text occurs exactly once" (line
  635) does not hold in the sense the convention uses.
- The current Tier 1 revision has merged the two: its item 7 now replaces both its own old item 7 and the second pair of
  Tier 2's item 4. The paragraph therefore ends with the line "not established ([[rem:loc-cone-scope]])."

Replacement for item 5 (the item's wording, then Old and New):

    *5. [[ch:scope]], the paragraph on localised data, its last lines as the Tier 1 placement leaves them (its item 7, which
    replaces also the second pair of the Tier 2 placement's item 4).* The text is appended at the end of the paragraph.
    Old:

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

(The old text occurs exactly once in the current Tier 1 merged text. The ch:scope line is now at line 210 of HEAD, not
208, after the P-ADM merge.)

### minor 9: one site the placement misses: the paragraph after prop:loc-cones (Placement item 8, line 732)

Current item 8: "No other change."

What is wrong. The new paragraph after [[prop:loc-cones]] in chapter 83 ends with a sentence that thm:loc-shells makes
false. Both versions of it carry the sentence: Tier 1's merged item 4 (current P-CIVP.md, lines 1110-1112) and Tier 2's
item 3 (P-CIVP2.md, lines 694-695). The sentence reads "No development is asserted for cone data that differ from the
background's near an axis, for data of finite regularity or for densities that are not smooth, and no other result of
this paper uses these developments." A density with atoms along leaves is not smooth, and thm:loc-shells develops it.
Add an item, against the Tier 1 merged text (which replaces Tier 2's). Old:

    neither uniqueness in the gauge nor localisation. No development is asserted for cone data that differ from the
    background's near an axis, for data of finite regularity or for densities that are not smooth, and no other result of
    this paper uses these developments.

New:

    neither uniqueness in the gauge nor localisation. No development is asserted for cone data that differ from the
    background's near an axis, for data of finite regularity or for densities that are not smooth, except finitely many
    null shells along leaves of the two cones and data that are smooth except across such leaves ([[thm:loc-shells]]), and
    no other result of this paper uses these developments.

If Tier 2's item 3 is used instead, the same words go at its last sentence (P-CIVP2.md line 694, "the solution. No
development …", through line 695), reflowed. Item 8's "No other change" then names this item as the exception.

### minor 10: the connection coefficient η is being renamed in Tier 1 (lem:loc-shell-identities, lines 126, 135, 143, 159)

Current: line 126 "let L̲, 𝒱, η, χ_i, χ̲_i, tr χ and tr χ̲ be as in [[eq:loc-cone-quantities]]"; line 135 "− 2γ_ϑ⁻¹
(∂_ϑη + η² − ∂_ϑϰ_1 η)"; line 143 "r̲ is built from η = ∂_ϑ ln Ω"; line 159 "For a round metric η = 0".

What is wrong. The current Tier 1 text (P-CIVP.md line 200, and lem:loc-cone-frame and eq:loc-cone-frame-ricci) renames
η := ∂_ϑ ln Ω to ϖ. That removes its clash with the angle η of thm:loc-cone-development, a clash this section shares,
since it uses η for an angle at lines 340, 461 and 527-598. Once that revision is merged, "η … as in
[[eq:loc-cone-quantities]]" names nothing. Replace η by ϖ at these four places:
- line 126: "let L̲, 𝒱, ϖ, χ_i, χ̲_i, tr χ and tr χ̲ be as in [[eq:loc-cone-quantities]]";
- line 135: "− 2γ_ϑ⁻¹ (∂_ϑϖ + ϖ² − ∂_ϑϰ_1 ϖ)";
- line 143: "r̲ is built from ϖ = ∂_ϑ ln Ω";
- line 159: "For a round metric ϖ = 0".

The lengths are unchanged. If the Tier 1 rename is not merged, keep η.

### Nits

1. Line 391 ends "(i)–" and line 392 begins "(iii)", which renders as "(i)– (iii)". Replacement for lines 390-395:

        *Step 1: the corner rectangle.* The restrictions of the cone data to {0} × [0, c_1] and [0, d_1] × {0} are cone data in
        the sense of [[def:civp-large-data]] with d_1 and c_1 in place of u_1 and v_1: they are smooth up to the ends, and
        (i)–(iii) hold by [[def:loc-shell-data]]. [[thm:civp-large]] gives a class solution in the gauge on {(u, v) ∈ 𝒫_0 :
        min(u, v) ≤ δ} for some δ > 0, inducing these data and equal to (g0, q̊_in, q̊_out) at the points with ϑ ∉ [ϑ_a − η0,
        ϑ_b + η0], so off (ϑ_a^(1), ϑ_b^(1)), and unique in the sense of its part (c). Let δ_0 := min(δ, min(c_1, d_1)/2),
        𝒮_0 := {(u, v) ∈ 𝒫_0 : min(u, v) ≤ δ_0} and g_0 the restriction of that solution to 𝒮_0 × S³.

2. Placement line numbers. Item 4 says "(lines 20–21)"; the old text is at lines 21-22 of chapter 83. Item 5 says "(line
   208)"; the old line is at 210 since the P-ADM merge (07c2aaff). The numbers only locate; replace them by "lines 21–22"
   and "line 210".
3. Notation. 𝒮_k, 𝒮′_j (the singular tensors of lem:loc-shell-ricci) share a letter with the domains 𝒮_0, 𝒮_k^out,
   𝒮_j^in and 𝒮_δ of the proof of thm:loc-shells, and with the collar 𝒮 of Tier 1. In prop:loc-shell-crossing (b),
   line 560, Chapter 80's D[σ] appears beside the past set D. And k is both the index of a leaf and, in (d) and (T1), the
   regularity index ("the index k_k"). Suggest naming the singular tensors 𝔖_k, 𝔖′_j: lines 72-73, 76, 81, 83, 102, 117,
   119, 229, 235-236 and 606-607, and the replacement text of minor 2. The other two are readable as they stand.
4. prop:loc-shell-cones, lines 301-303: "keep Ω the background's" is said only for 𝒞_out, and the sentence "The same holds
   on 𝒞_in …" does not list Ω. Part (d) applies thm:loc-cone-development, which needs Ω to be the background's on 𝒞_in
   as well (lem:loc-cone-in). Replacement for lines 301-305:

        background's at every ϑ outside the band. The same holds on 𝒞_in in the gauge b = 0, with Ω the background's there, with
        the free data there, q_out, the n_j, the points d_j, u and [[eq:loc-cone-in]] in place of the free data on 𝒞_out, q_in,
        the m_k, the points c_k, v and the first line of [[eq:loc-cone]], the corner values of ϕ and ∂_uϕ being the background's;
        then [∂_uϕ] = −n_j/3. No smallness is used; for free data near the background's and small m_k and n_j, e^ϕ stays
        positive on [0, v_1] and on [0, u_1].

5. Proof of (d), line 482: "R > a on N_i once λ_1 is small, R being continuous and > a on the cones". (T1) also needs
   R > a on N_o = {0} × [c_k, v_1 + δ_1], which reaches beyond v_1, and g0 defined near the rectangle. Both hold once
   δ_e is small too. Replace by "R > a on N_i and on N_o once λ_1 and δ_e are small, R being continuous and > a on the
   cones".
6. thm:loc-shells, line 351: "Put c_1 := v_1 if p = 0 and d_1 := u_1 if q = 0" repeats the convention c_(p+1) := v_1,
   d_(q+1) := u_1 of line 18. It can be dropped. Line 379: "depending also on N" is implied by "the leaves".
7. "Class solution in the gauge." Tier 1 (sec:loc-cone-setting) defines it with "equal to the background's near ϑ = 0 and
   ϑ = π/2"; Tier 2 (sec:civp-large) defines it with smooth extension to the axes only. R-P-CIVP nit 9 notes the double
   definition. This section needs Tier 2's sense: in lines 62-65 a general solution with shells, and in
   prop:loc-shell-crossing (b) (line 572) the round extension, need not equal g0 near the axes. Suggest inserting, after
   "continuous and cellwise smooth." (line 34):

        continuous and cellwise smooth. Here and below a class solution in the gauge is meant in the sense of
        [[sec:civp-large]]: its functions are smooth off the axes and the metric extends smoothly to them; it need not equal g0
        near the axes. Charts (u, v, y), with y = (y¹, y², y³) a chart of S³, cover D × S³, the axes included.

   (This replaces line 34; reflow the paragraph.)
8. Tier 2's item 1 allows its prefix civp-large- to become loc-. If that is done, this section's references to
   thm:civp-large, def:civp-large-data, eq:civp-large-band, sec:civp-large, rem:civp-large-domain and
   rem:civp-large-beyond, and items 1 and 3 of the Placement, follow.
9. Optional. The round rule of (a), f_(++) f_(−−) = f_(+−) f_(−+), is the five-dimensional form of the four-dimensional
   relation for crossing spherical null shells known from the literature on colliding shells. A sentence in
   rem:loc-shell-poisson would place it. No proof needs it, and any citation would first have to be checked against its
   source and entered in the references.

---------------------------------------------------------------------------------------------------------------------

## B. The pending interface

Both markers are stated in full in the paragraph "*The smooth theorems at other corners.*". Both are real cross-chapter
gaps: Tier 1 and Tier 2 state their theorems at the corner sphere S only. Neither hides a problem in this section.

**[[pending:civp-large-at-a-corner]] (T2).** It must supply [[thm:civp-large]] (a), (b) and (c) with these changes:
- the corner is any (u_c, v_c), and the rectangle is any 𝒬 = [u_c, u′] × [v_c, v′] ⊂ Q1 and any band;
- the data are on N_o = {u_c} × [v_c, v′] and N_i = [u_c, u′] × {v_c}, smooth up to the ends, with the properties of
  def:civp-large-data: Ω arbitrary on both edges, b arbitrary on N_o and b = 0 on N_i, q_in, q_out ≥ 0, agreeing on the
  corner sphere, satisfying the constraints, and equal to g0's outside compact subsets of the band.

The three parts then give:
- (a) a class solution in the gauge on 𝒬_δ = {min(u − u_c, v − v_c) ≤ δ} that induces the data;
- (b) the solution equals (g0, q̊_in, q̊_out) off [ϑ_a − η0, ϑ_b + η0];
- (c) uniqueness among class solutions on past sets of 𝒬 relative to its corner that induce the data and equal g0 near
  the axes.

It is used at the corners (0, c_k) and (d_j, 0) in thm:loc-shells (a)-(c), and at (d_j, c_k) in prop:loc-shell-crossing
(c). For the uses checked:
- in Step 2 the data on N_i come from the previous slab, with Ω and b not the background's, and b is removed by Φ_k;
- in Step 3 b = 0 on N_i already;
- the band at depth k is (ϑ_a^(k), ϑ_b^(k)), and (b) then gives g0 off (ϑ_a^(k+1), ϑ_b^(k+1)), since w_k = (3/2)η0^(k)
  > η0^(k).

Translating u and v makes 𝒬 a rectangle with corner at the origin. Tier 2's proof uses Q1 only through such a rectangle,
and its corner step and lem:civp-large-data already work at any corner. So (T2) is a restatement, as the paragraph says.

**[[pending:loc-cone-development-at-a-corner]] (T1).** It must supply three parts of [[thm:loc-cone-development]] at a
corner (0, c) or (d, 0): existence on {(u − u_c)(v − v_c) ≤ δ_*²}, the "in particular" clause of its localisation (b),
with η = (1/4) min(ϑ_a, π/2 − ϑ_b), and the estimate (c) to order k − 4. It applies to cone data in the sense of
def:loc-cone-data in the normalised gauge, with Ω arbitrary on both edges, of size ε in C^(6k+18). δ_* must depend only
on g0 near the rectangle, l_u, l_v and η, and ε_0 and C also on k.

It is used only in thm:loc-shells (d). Two points about the Tier 1 revision:
- Major 2 of R-P-CIVP changes the sharp localisation (b) but keeps its "in particular" clause (current P-CIVP.md line 62),
  which is all that (T1) and (d) use.
- Major 1 concerns Tier 1's uniqueness (d), which neither (T1) nor this section uses. Part (d) of thm:loc-shells obtains
  agreement with the solution of (a) through (c), that is through (T2) (c).

So the revision leaves (T1) as stated.

**Labels used of Tier 1 and Tier 2.** Every reference resolves in one of: the chapters at HEAD, P-CIVP.md (current and as
of the P-SHELL commit) or P-CIVP2.md. These labels were checked, each with the content used:

| Label | Content used | Status |
|---|---|---|
| lem:loc-cone-ricci (b) | √\|det g\| = 2Ω²𝒱 and the two divergences, which give X = −𝒱∂_u − b𝒱∂_ϑ and X′ = −𝒱∂_v | ✓ |
| eq:loc-cone-frame-ricci | E(L̲, ∂_ϑ), E(K_i, K_i) = −e^(2ϰ_(i+1)) □ϰ_(i+1), □_g and E(∂_ϑ, ∂_ϑ) | ✓, confirmed independently in sympy through the two identities |
| eq:loc-cone-quantities | the quantities themselves | ✓, with minor 10 |
| def:loc-cone-data (ii) | Ric(L̲, L̲) on N_i holds derivatives along N_i only | ✓ |
| lem:loc-cone-strips (b) | as stated | ✓ |
| sec:loc-cone-reduced case (I), with lem:loc-cone-cauchy, -past, -support, -constraints, -gauge | as stated | ✓ |
| prop:loc-cone-local | the hypotheses: corner anywhere in Q, any λ_u, λ_v, Ω arbitrary, b = 0 on N_i, data equal to the background's off [2η, π/2 − 2η], C^(m_1) size Λ; the conclusion: off [η, π/2 − η] | ✓, also in its revised form, whose background hypothesis on 𝒪 ∩ {u ≥ u_Q, v ≥ v_Q} g0 meets |
| rem:loc-cone-scope (ii)-(iv) | as stated | ✓ |
| rem:loc-cone-local-scope | as stated | ✓ |
| thm:civp-large (a)-(c) | as stated | ✓ |
| def:civp-large-data | as stated | ✓ |
| eq:civp-large-band | η0 = (1/3) min | ✓ |
| rem:civp-large-domain | its last sentence | ✓ |
| rem:civp-large-beyond | ends the Tier 2 section | ✓ |
| lem:loc-cone-in / eq:loc-cone-in | "holds for every Ω when b = 0" | ✓ |

---------------------------------------------------------------------------------------------------------------------

## C. Placement

| Item | Old text found | Composition |
|---|---|---|
| 1 | Anchor "### The static Killing field and the charge {#sec:loc-kid}": once, at line 602 of chapter 83 (HEAD 07c2aaff) | The order sec:loc-cones (+ Block A), Block B, Tier 2 section, this section, sec:loc-kid agrees with both tiers' item 1. The list of nineteen defined labels matches the {#…} in lines 1-629 exactly. None is defined in any chapter, in P-CIVP.md, in P-CIVP2.md or in OUTLINE.md. |
| 2 | Once in Tier 1 as of the P-SHELL commit; 0 times now | See minor 7. |
| 3 | Once in P-CIVP2.md (unchanged); in no chapter, as expected | Composes; the Tier 1 revision does not touch rem:civp-large-domain. |
| 4 | Once in chapter 83 (lines 21-22) | Neither tier changes this paragraph; the tiers change lines 8-9. Composes. |
| 5 | Once in chapter 90 as a line (now line 210) | Does not compose as described; see minor 8. |
| 6 | Once in chapter 98 (line 157) | Tier 1's item 10 adds [Ren90] after [Rac16]. The order [Poi02], [Rac16], [Ren90] is alphabetical, and Tier 2's change to [CCTW16] does not interact. |
| 7 | — | Correct: [Poi02] is used for comparison only, and no proof in the section uses a published result. The elementary tools (Fubini's theorem, integration by parts, the contraction principle, linear ordinary differential equations) are used throughout the edition without Appendix A entries; chapter 80's proof of prop:two-dust-background does the same. |
| 8 | — | Incomplete; see minor 9. |

Reference entry ([Poi02], item 6). The title matches the title page of v1 ("A reformulation of the Barrabès-Israel
null-shell formalism", E. Poisson, dated July 5, 2002, arXiv 25 Jul 2002). The edition's en dash is its house style. No
journal reference was found; arxiv.org itself is not reachable from this session, and OpenAlex was refused by the proxy.
"preprint (2002). arXiv:gr-qc/0207101v1" follows the style of the other preprint entries.

Crosswalk rows (lines 741-759):
- 19 rows, one per defined label, in the order of definition;
- each has four tab-separated fields, as in crosswalk/83-localised-data.tsv;
- each row's line number points at the line that carries its label.

---------------------------------------------------------------------------------------------------------------------

## D. Typography

- Proof file: no line longer than 121 characters, by a Unicode count (lines 1-733). Note that awk counts bytes.
- Assembled paper of the scratch build: no line of the section, nor of the placed texts of items 2-6, exceeds 121
  characters after label resolution. The section is numbered 53.6 there, and its theorem is Theorem 53.46.
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The only "- " line start is the reference list
  item of item 6, which is meant. Line 511 starts with "−2e^(−2σ)", the minus sign U+2212, which is not a list marker.
- All labels are lowercase.
- `lint.py --chapters` on the build: the only hits in this section are the two pending markers. The other hits are Tier
  2's own pending markers and its Appendix A labels, which the build did not insert.
- The section contains no file, program or process words.

---------------------------------------------------------------------------------------------------------------------

## E. Literature

[Poi02], read in v1 through the alphaXiv paper reader:
- p. 1: "This construction provides the stress-energy tensor with a simple characterization in terms of a mass density, a
  mass current, and an isotropic pressure". The quoted words are verbatim.
- p. 1: "the singularity in the Weyl tensor is interpreted as an independent impulsive tidal wave". Verbatim.
- p. 4, (2.15): "S^αβ = μk^αk^β + j^A(k^αe^β_A + e^α_Ak^β) + pσ^AB e^α_Ae^β_B". Verbatim, up to the edition's
  parentheses for raised index pairs.
- k^α = (∂x^α/∂λ) is tangent to the generators (p. 2).
- S^αβ is formed from the singular part of the Einstein tensor ((3.7)-(3.8), p. 5); see minor 2.

[LR20, Theorem 4.6] (rem:loc-shell-scope (i)) is the entry Tier 1 already quotes in rem:loc-cone-scope (iii); its
description here, "angularly regular measures in 3 + 1 dimensions", agrees with that quotation.

---------------------------------------------------------------------------------------------------------------------

## F. Checked and found correct

- **"Leaves and cells" and def:loc-shell-solution.**
  - The jumps, and the continuity of tangential derivatives.
  - The distributional Ricci tensor in charts (u, v, y): bounded Christoffel symbols, products taken pointwise.
  - g^(vv) = g^(uu) = 0 in every such chart. So the fields of eq:loc-shell-dust have no ∂_v- or ∂_u-component, and their
    products with the δ's are products of continuous functions with distributions.
  - Away from the leaves the equations are the class system with two families.
- **lem:loc-shell-ricci (a).**
  - The integration by parts along v-intervals of a past set gives ∂_vF = {∂_vF} + Σ[F]δ(v − c_k), with the sign right.
  - [∂_e g_ab] = δ^v_e h_ab and [Γ^a_bd] as stated. [Γ^v_bd] = ½(δ^v_bY_d + δ^v_dY_b), using g^(vv) = 0, and
    [Γ^a_ab] = ½δ^v_b tr h.
  - The coefficient [Γ^v_bd] − δ^v_d[Γ^a_ab] = 𝒮_k, by hand.
  - In sympy, the coefficient of the second transverse derivatives of the classical Ricci tensor, contracted with the
    jumps, equals ½(dv⊗Y + Y⊗dv) − ½(tr h) dv⊗dv identically.
- **lem:loc-shell-ricci (b).**
  - Every component of h, every component of Y, g⁻¹dv = −(2Ω²)⁻¹L̲, and tr h = 4[∂_v ln Ω] + 2[tr χ].
  - The final 𝒮_k, including the −b du part.
  - Across {u = d_j}: h′(∂_v, ∂_d) = 0 for d ≠ u, Y′ = 2[∂_u ln Ω] du, 𝒮′_j = −[∂_u ln 𝒱] du⊗du, and [∂_u ln 𝒱] =
    [tr χ̲].
  - sympy confirms 𝒮_k and 𝒮′_j identically, with Ω, γ_ϑ, b, A_c, A_s arbitrary. It also confirms that 𝒮′_j contains
    neither [∂_u b] nor [∂_u ln Ω], and that 𝒮_k contains no [∂_v ln Ω] and no jump of the ϰ_i − ϕ: "no condition across
    outgoing leaves" holds.
  - Also in sympy: tr_g 𝒮_k = 0, used in minor 2.
- **lem:loc-shell-identities.**
  - The first identity equals Ric(L̲, ∂_ϑ) of the metric identically (sympy, from the metric, not from Tier 1's formula).
  - eq:loc-shell-trace holds identically with the stated 𝔞 (sympy).
  - The proof's steps were checked by hand: the sums give tr χ tr χ̲ and 𝒱⁻¹∂_ϑ(𝒱∂_v b), ∂_v(𝒱 tr χ̲), and the
    commutator ∂_vL̲ = L̲∂_v + (∂_v b)∂_ϑ.
  - The round case: both sides equal (6e^(−2σ)/R²)(R R_uv + 2R_uR_v + e^(2σ)), and 𝔞 = 6/R² (sympy and by hand). This is
    R⁻² γ̂^(AB) Ric_AB of lem:two-dust-equations.
  - r̲ holds derivatives along L̲ and ∂_ϑ only, and 𝔞 along ∂_ϑ only.
- **prop:loc-shell-junction (a)-(c).**
  - (a): the jump of the first identity, the continuity of [∂_v b] at crossing spheres, and the integral curves of L̲
    filling the leaf when b vanishes near the axes.
  - (b): every term of the jump of the trace identity, [(∂_v b)²] = 0 under (J1), and L̲F + (∂_ϑ b)F = ∂_uF + ∂_ϑ(bF),
    giving eq:loc-shell-conservation.
  - (c): the displayed formula for ∂_v∂_u𝒱 follows from eq:loc-shell-trace with vanishing left side (checked by hand),
    its right side is tangential to {u = d_j}, and [∂_u𝒱] = 𝒱[tr χ̲]. Continuity at crossing spheres in all three.
- **prop:loc-shell-junction (d), both directions.**
  - The coefficients localise leaf by leaf, and continuity up to the axes reduces the conditions to off-axis ones.
    "𝒮_k = 𝔪_k dv² iff (J1) and 𝔪_k = −[tr χ]".
  - The dust equations: X^v = 0 and X′^u = X′^A = 0 in every chart (u, v, y). The distributional divergence produces the
    three conditions. X = −𝒱∂_u − b𝒱∂_ϑ and X′ = −𝒱∂_v off the axes. Given (J1) and (J2), the shell laws are (b) and
    (c), and the conditions [q_in] = 0 and [q_out] = 0 are (J3).
  - So the proposition is necessary and sufficient as stated.
- **rem:loc-shell-poisson, the identifications** (see minor 2): μ ↔ [tr χ], j ↔ [∂_v b], p ↔ h(L̲, L̲) = 0.
- **def:loc-shell-data and prop:loc-shell-cones.**
  - The δ-part of the first constraint is −Σ[∂_vϰ_i] = −3[∂_vϕ] = m_k, since Σℓ_i = 0, and the jump condition on y′ is
    right.
  - The ODE is solved interval by interval, and smoothness in ϑ follows by induction.
  - In the second line the only δ is (γ_ϑ/(4Ω²))[∂_v b]: r holds ∂_v∂_ϑϰ_i only as ∂_v of the continuous ∂_ϑϰ_i. So
    [∂_v b] = 0 is automatic.
  - Localisation outside the band, by uniqueness; [tr χ̲] = 3[∂_uϕ] = −n_j on 𝒞_in.
- **thm:loc-shells (a), Step 1.** thm:civp-large on 𝒫_0 with (d_1, c_1) in place of (u_1, v_1) needs no pending
  statement.
- **thm:loc-shells (a), Step 2.**
  - λ_k^out = δ_(k−1)^out keeps 𝒫_k^out in the cell Q_0k and N_i inside 𝒮_(k−1)^out.
  - The corner values agree.
  - The change of angle: the identity off the support of b on N_i; dϑ − b du transforms as stated; Ω, A_c, A_s are
    unchanged, γ_ϑ ↦ γ_ϑ/(∂_ϑΦ_k)², b ↦ ∂_uΦ_k + b∂_ϑΦ_k, so b = 0 on N_i and b ↦ b − b(0, c_k, ·) on N_o, where ∂_ϑΦ_k
    = 1.
  - ∂_v, L̲ = −2Ω²g⁻¹dv, and ∂_ϑ on N_o are unchanged, so the constraints carry over. The bands are as needed for (T2).
- **thm:loc-shells (a), Steps 3-5.**
  - Step 3: no change of angle is needed.
  - Step 4: δ < min(c_1, d_1) prevents crossings, since a point with v ≥ c_1 has u ≤ δ < d_1. The decomposition of 𝒮_δ
    into the four kinds of pieces is right; the glued metric is continuous, and (J3) holds by construction.
  - Step 5: [∂_v b] = 0 at (0, c_k) from the cone data, then on the leaf by (a). 𝔪_k = m_k ≥ 0 at u = 0, carried with its
    sign by (b), and likewise 𝔫_j by (c).
- **thm:loc-shells (b).** The bands increase, and ϑ_a^(N) ≥ 2^(−N)ϑ_a.
- **thm:loc-shells (c).**
  - Each restriction is smooth, a cell being closed. Past sets relative to the corners.
  - The induction through 𝒫_0, 𝒫_k^out and 𝒫_j^in, with Φ_k determined by data that the competitor shares; the shell
    densities follow from (J2). This is up to minor 6.
- **thm:loc-shells (d).**
  - The cascade k_(N−1) = 6, k_(i−1) = 6k_i + 23, m_* = 6k_0 + 21. Index k_0 at depth 0 with m = m_*.
  - The extended data in C^(m_* − 3) = C^(6k_0 + 18), which suffices for every depth, as k_i ≤ k_0.
  - δ_1 ≤ λ_k^out/3 ≤ δ_e puts N_i inside the previous solution. λ_(k+1)^out = min(l_u, δ_*,k²/(v_1 − c_k)) is
    independent of the data.
  - The localisation with η = w_i/2; agreement with (a) through (c).
  - Up to minor 1 and nit 5.
- **prop:loc-shell-crossing (a).**
  - The four equalities: ∂_v is tangent to {u = d_j}; L̲ and ∂_ϑ are tangent to {v = c_k}.
  - The product rule.
  - The round case: tr χ = 3R_v/R, tr χ̲ = 3R_u/R, f = −(R²/(9Ω²)) tr χ tr χ̲ = −2e^(−2σ)R_uR_v, and the mass form.
  - R²[R_v] constant through Z. [μ] = 2e^(−2σ)R²R_u[R_v], with R_u continuous across {v = c_k}, and its sign.
- **prop:loc-shell-crossing (b).**
  - q_in = 𝒜(v)/R³ and q_out = ℬ(u)/R³ for round class solutions.
  - The data of eq:two-dust-volterra on the two edges, and C_v = 0 on N_o and C_u = 0 on N_i along the edges.
  - The ball B maps into itself under s(M_0 + M_1) + s²M_1 ≤ r_0/2: each single integral is bounded by sM_0 or sM_1 and
    the double one by s²M_1.
  - Contraction under s(1 + 2L_1) + s²L_1 ≤ 1/2, which is more than enough.
  - Smoothness and the constraints as in prop:two-dust-background (d); uniqueness of continuous solutions with R > 0.
  - The glued metric is continuous: R and σ agree on both edges, Q̄(u, 0) need not equal the lower cell's R_v, which is
    the shell. (J1), (J3) and the continuation of the shells. Uniqueness among round extensions; 𝔉 and ℌ do not contain
    𝒜 and ℬ, so the profiles do not enter.
- **prop:loc-shell-crossing (c).**
  - 𝒬 lies in the cell Q_jk and in Q1, because 𝔏 ⊂ D. prop:loc-cone-local applies with Q := Q1 and data equal to g0 off
    [2η, π/2 − 2η] after the change of angle; s = min(λ, σ).
  - [∂_v b] = 0 propagates from Z; the shells continue with their signs.
  - Under (T2): the band (3η/2, π/2 − 3η/2) has η0′ = η/2 and gives g0 off [η, π/2 − η]. Uniqueness on D″ ∩ 𝒬_δ, up to
    minor 6.
- **prop:loc-shell-crossing (d).** tr χ and tr χ̲ are expansions along fields that are smooth on each closed cell up to
  the axes. Nothing is asserted at an axis for non-round shells; (b) and (c) are correctly confined to round solutions
  and to solutions equal to g0 near the axes.
- **rem:loc-shell-scope (i)-(vi).** Each item agrees with what the section proves and does not prove.
- **The section is self-contained.** Every proof is written out, and no step rests on a computation or on "as in the
  source".

---------------------------------------------------------------------------------------------------------------------

## Confirmation (after the fix rounds)

**File read.** `proofs/P-SHELL.md`, md5 93003d07312398b58c9557abb5354dc8, 969 lines:
- section 1-819;
- Placement 821-941;
- Crosswalk 943-969.

Every line was read.

**Texts it was read against.**
- The writer's reports F-P-SHELL.md, all three rounds.
- The merged chapter 83 at HEAD (commit f700baf0; Tier 1 at 83:598-1648, Tier 2 at 83:1650-2389, sec:loc-kid at
  83:2391), and chapters 90 and 98.

All of these were taken from a `git archive` of HEAD in the session scratchpad (reader/pshell2/). For chapters 83, 90 and
98 the working tree agrees with HEAD. No repository file was edited, and assemble.py was run only in the scratch copy.

**Verdict: NOT CONFIRMED — 0 Major, 1 minor, 3 nits.** The minor concerns the text of placement items 8, 2 and 3: the
exception they make for null shells says more than is proved. Everything else is resolved or correct, including both new
lemmas.

### C1. The 19 findings of the first reading

All 19 are resolved. For the four applied with changes, and for nit 9, the judgement is as follows.

- **minor 1 (applied in full, lines 627-659).** Correct, and better than my replacement.
  - Φ_k(u, ·) is the inverse of the flow of b(u, c_k, ·)∂_ϑ, so Φ_k − id and its inverse are within Cε in
    C^(k_(k−1) − 4).
  - The forward transform lands in C^(k_(k−1) − 5) = C^(6k_k + 18) = m_0 of index k_k.
  - The paragraph "Changing the angle back loses no derivative" is right:
    - F ∘ Φ_k − F̊ = (F − F̊) ∘ Φ_k + (F̊ ∘ Φ_k − F̊);
    - the second term is (Φ_k − ϑ) times a mean value, vanishing off the compact set K that Φ_k maps onto itself;
    - the added factors (∂_ϑΦ_k)², ∂_uΦ_k, 1/∂_ϑΦ_k and ln ∂_ϑΦ_k lie in C^(k_(k−1) − 5) ⊃ C^(k_k − 4);
    - the formula b ↦ (b ∘ Φ_k − ∂_uΦ_k)/∂_ϑΦ_k inverts b̃ = ∂_uΦ_k + b∂_ϑΦ_k.
  - The 𝒞_in order k_(j−1) − 4 ≥ 6k_j + 18 and the closing "k_i − 4 ≥ k_(N−1) − 4 = 2" are right. The C¹ claim is kept.
- **minor 3 (applied, lines 670-675 and 715-729).** Correct, and sharper than mine.
  - The exception now says what (c) needs: the curves start at any sphere {(u′, c_k)} × S³ in D′ and fill the part of the
    leaf with u ≥ u′.
  - I checked the three interval computations, for 𝔏, for 𝔏 ∪ [d_j, d_j + s] × [c_k, c_k + s] and for 𝔏 ∪ D″, D″ a past
    set of 𝒬 relative to its corner.
  - I checked that no other step uses more of a past set: lem:loc-shell-ricci (a), the ODEs of prop:loc-shell-junction,
    and the rule for derivatives in its part (d).
- **minor 5 (applied, lines 212-215).** Correct. "Locally bounded along the curve and continuous off the crossing
  spheres" is all that uniqueness for the linear equation needs.
- **nit 5 (applied, lines 610-612 and 631-633).** Correct.
  - δ_e is now chosen so that 𝒪 contains [−δ_e, 3δ_e] × [−δ_e, v_1 + δ_e] and [−δ_e, u_1 + δ_e] × [−δ_e, 3δ_e].
  - At depth k the collar of lem:loc-shell-corner-small at (0, c_k) lies in the first of these sets, since
    l_u + δ_1 ≤ λ_k^out ≤ λ_1 ≤ 3δ_e, v_1 + δ_1 ≤ v_1 + δ_e and c_k − δ_1 ≥ −δ_e. The collar at (d_j, 0) lies in the
    second.
  - The old "R > a" is no longer needed, as lem:loc-shell-corner-small asks only that the collar lie in 𝒪.
- **nit 9 (not applied).** Agreed. The remark was optional, and a citation that has not been checked against its source
  must not enter the edition.

The others are applied as proposed:
- minor 2: lines 268-279;
- minor 4: line 677;
- minor 6: lines 599-602 and 789-792, the q_in clause added at the first site;
- minors 7-9: items 2, 5 and 8, now against HEAD; see C4;
- minor 10: ϖ at lines 133, 142, 150 and 166, which matches chapter 83 (83:810, 83:857);
- nits 1-4 and 6: lines 536-538, the item line numbers, 𝔖_k and 𝔖′_j, line 312, and line 497 with line 524;
- nit 7: superseded by the decision of C2;
- nit 8: void, as the Tier 2 prefix is unchanged.

### C2. "Class solution in double-null form" against Tier 1's sense

The definition (lines 34-39) and its sites are right. Tier 1's sense (83:731-734, which Tier 2 adopts at 83:1690-1692)
requires the functions to equal the background's near the axes. "Class solution in double-null form" drops only that
requirement.

The five sites that need the broader sense use it, and each needs it:
1. Lines 69-72. A general solution with null shells has cells of this kind, and for p = q = 0 it is "a class solution in
   the gauge if it equals g0 near the axes".
2. Line 174, the hypothesis of prop:loc-shell-junction. prop:loc-shell-crossing (a), (b) and (d) apply the proposition to
   solutions that need not equal g0 near the axes.
3. Lines 742 and 761, the round solutions in the proof of prop:loc-shell-crossing (b).

Every other use keeps Tier 1's sense, and at each of them the solution does equal g0 near the axes:
- lem:loc-shell-corner-large (a) and (c), by its (b);
- lem:loc-shell-corner-small, by its localisation;
- Steps 1-4 of thm:loc-shells (lines 538, 558, 568, 577), by the bands;
- thm:loc-shells (c), line 596, by hypothesis;
- prop:loc-shell-crossing (c), lines 777, 779-780 and 789: on 𝔏 by hypothesis, and on the new cell by
  prop:loc-cone-local.

Where a site in Tier 1's sense feeds prop:loc-shell-junction (Step 4, and (c) of the crossing proposition), this is
legitimate, since a class solution in the gauge is in particular one in double-null form.

### C3. The two new lemmas, read as a first reading against the merged chapter

**lem:loc-shell-corner-large (lines 340-417): correct.** It is a faithful transcription of the proof of thm:civp-large
(83:2209-2359). I went through the cited proof step by step against each replacement.

- **The statement.**
  - Cone data on 𝒬 are (i)-(iii) of def:civp-large-data at the corner, with Ω free on both edges and b free on N_o and
    zero on N_i. def:civp-large-data already leaves Ω free on both cones, so nothing is lost.
  - (a)-(c) are thm:civp-large (a)-(c) with S_𝒬, the edges, the past sets of 𝒬 and 𝒬_δ.
- **The results that proof uses.**
  - lem:civp-large-energy and prop:civp-large-corner are stated for arbitrary rectangles. prop:civp-large-corner is
    stated in Q1, with 𝒪 ⊃ Q1, and κ = η0′ ≤ π/12 < π/8, as it requires.
  - lem:civp-large-data (a) is general (83:2057-2068). Its (b) is a set of ODEs along the edges from the corner: b = 0 on
    N_i makes them ODEs along {ϑ = const} on N_i, and the f₄-equations have no ∂_ϑ of an f₄-unknown on N_o.
  - The frame, reduction and system results are pointwise.
- **Its Step 1.** J0′ = [ϑ_a′ − 2η0′, ϑ_b′ + 2η0′] ⊂ [η0′, π/2 − η0′], since ϑ_a′ ≥ 3η0′.
- **Its Step 2.** The CCTW16 theorems apply in the translated coordinates, with a0 = u′ − u_c and b0 = v′ − v_c.
- **Its Step 3.**
  - In eq:civp-large-delta, η0′, v′ − v_c and u′ − u_c replace η0, v_1 and u_1, and the energy lemma is applied on the
    translated strips.
  - |b| ≤ β1(v − v_c) follows from b = 0 on N_i.
  - The sign argument uses the segments from u_c and v_c.
- **Its Step 4.**
  - 𝒯₁ and 𝒯₂ are the two strips at the corner. The constants come with η0′; [ϑ_a′ − η0′, ϑ_b′ + η0′] ⊂
    [2η0′, π/2 − 2η0′].
  - In the corner step the edges at u = u_c or v = v_c are N_o or N_i.
  - D_t and Γ are taken in (u − u_c) + (v − v_c). The first rectangle has its corner at S_𝒬, where f̄ is geometric to
    first order. The rectangles about Γ have their corners clipped at (u_c, v_c).
  - The rename that avoids the clash with Tier 2's u_c, v_c is handled consistently.
- **Its Steps 5 and 6.** Step 6 uses z₃ = 0 at u = u_c and z₄ = 0 at v = v_c, with η″ = min(η′, η0′).
- **The uses.**
  - Steps 2 and 3 of thm:loc-shells, the bands of depth k.
  - thm:loc-shells (c).
  - prop:loc-shell-crossing (c): band (3η/2, π/2 − 3η/2), η0′ = η/2, data equal to g0 off [2η, π/2 − 2η] ⊂
    (3η/2, π/2 − 3η/2), and 𝒬 ⊂ Q1 since 𝔏 ⊂ D.

  Each use meets the hypotheses.

**lem:loc-shell-corner-small (lines 419-494): correct.** It is checked against sec:loc-cone-setting (83:728-755),
sec:loc-cone-reduced (83:1143-1240), lem:loc-cone-system, -cauchy, -past, -support, -constraints and -gauge
(83:1241-1450), and the proof of thm:loc-cone-development (83:1632-1648).

- **The background.** g0 restricted to the collar, with e^(2σ_e) = 2Ω² and R_e = R, is a background on 𝒮 in Tier 1's
  sense: it is smooth with R_e > 0 on 𝒮_c ⊂ 𝒪, and 𝒮_c ∩ F lies in 𝒪 ∩ {u, v ≥ 0}, where g0 solves eq:two-dust-limit
  (83:1680-1684).
  - Tier 1's paragraph at 83:749-753 states that the later proofs use only these properties and a number
    C_* ≥ sup e^(σ_e)/R_e. Here e^(σ_e)/R_e = √2Ω/R, so the lemma's C_* is admissible; lem:loc-cone-support needs exactly
    this inequality.
  - lem:loc-cone-strips is used only to supply the background and C_0, which this replaces.
- **The data.** The least interval [ϑ_a″, ϑ_b″] ⊂ (ϑ_a′, ϑ_b′) ⊂ [4η, π/2 − 4η] gives agreement off [2η, π/2 − 2η], with
  η ≤ π/16 < π/8. These are case (I) data.
- **The steps reused.**
  - δ_c ≤ √c_+/8 and δ_c(l_u + l_v + 1) ≤ c_+/2 come from case (I).
  - 2C_*(δ_c(l_u + l_v + 1))^(1/2) ≤ η/4 comes from the proof of the theorem.
  - δ_c ≤ 1 is added, rightly: with arbitrary l_u, l_v, δ_1 and hence √c_+ may exceed 32. It is what gives
    (u + δ_c)(v + δ_c) ≤ uv + δ_c(l_u + l_v + 1) on G_c, and with it G_c ⊂ F ∩ 𝒰. The far cuts hold because κ l_v ≤ δ_1/4.
  - The existence and the C^(k−4) estimate are the last sentence of lem:loc-cone-gauge (83:1418-1420).
- **The localisation.**
  - lem:loc-cone-support gives the background where ϑ < ϑ_a″ − 2C_* e^(τ/2), with e^(τ/2) = ((u + δ_c)(v + δ_c))^(1/2).
  - On G_c, 2C_*(uv)^(1/2) ≤ 2C_*δ_* ≤ η/4, as δ_* = √c_+/2 ≤ η/(8C_*).
  - Adding the δ_c condition gives η/2, and so the background where ϑ ≤ ϑ_a′ − η or ϑ ≥ ϑ_b′ + η.
- **The constants.** δ_* depends only on δ_1, η and C_*. ε_0 and C depend on k, η, l_u, l_v and g0 on 𝒮_c, through
  lem:loc-cone-system (a) with Λ = ε ≤ 1 and through 𝒰. None depends on the data. Not using lem:loc-cone-unique, nor the
  u_K, v_K clause, is right.
- **The use in thm:loc-shells (d), lines 627-659.**
  - The edges: N_o = {0} × [c_k, v_1 + δ_1] carries the extended data, and N_i ⊂ [0, λ_k^out] × {c_k}.
  - The corner values agree, the metric functions being continuous at c_k, and b = 0 at the corner on both edges after
    the change of angle.
  - The size is in C^(6k_k + 18) on both edges, η = w_k/2, and G_c contains [0, λ_(k+1)^out] × [c_k, v_1].

### C4. Placement at HEAD

Every Old text occurs exactly once in its chapter at HEAD, as whole lines:

| Item | Site | Lines |
|---|---|---|
| 2 | chapter 83, rem:loc-cone-scope (iii), its second line | 681 |
| 3 | chapter 83, rem:civp-large-domain, its last sentence | 2369-2371 |
| 4 | chapter 83, the opening | 26-27 |
| 5 | chapter 90, the paragraph on localised data | 217-218 |
| 6 | chapter 98, [Rac16] | 157-158 |
| 8 | chapter 83, the paragraph on the developments | 704-705 |

- Item 1's anchor sec:loc-kid is at 83:2391, directly after rem:civp-large-beyond. Its list of 21 labels equals the
  labels the section defines, and none is defined elsewhere.
- The 21 crosswalk rows each point at their label.
- **Scratch build** (HEAD chapters, the section inserted before sec:loc-kid, items 2-6 and 8 applied):
  - `assemble.py` reports 0 problems;
  - `lint.py --chapters` reports 0 hits in 62 files;
  - no line of PAPER.md is longer than 121 characters;
  - the section is 53.6, the lemmas 53.48 and 53.49, the theorem 53.50.
- The proof file has no line over 121 characters and no wrapped line starting with a marker. Its new lists sit between
  blank lines, and no pending marker remains.
- Item 8's narrowed clause, "no result of the other chapters uses these developments", is true. Outside chapter 83,
  thm:civp-large and thm:loc-cone-development are cited only in the descriptive texts of chapter 03 (lines 380-381) and
  chapter 90 (lines 215-217), and no chapter outside 83 cites prop:loc-cone-local or any loc-shell label.

### C5. Finding

**minor C-1: the exception in items 8, 2 and 3 says more than is proved (lines 934-937, 850-855, 868-869).**

Item 8's New (83:704-705) reads: "except finitely many null shells along leaves of the two cones and data that are smooth
except across such leaves, which [[thm:loc-shells]] develops …". thm:loc-shells covers less than that, in two ways:
- **Angular regularity.** It covers shells whose densities m_k and n_j are smooth in ϑ (def:loc-shell-data). Item 8 drops
  the "with densities smooth in angle" that items 2 and 3 carry. Shells with merely bounded or measure-valued angular
  densities are not covered.
- **Continuity.** It covers data whose metric functions are continuous across the leaves. def:loc-shell-data has Ω, γ_ϑ,
  b, A_c, A_s "continuous and smooth on each [c_k, c_(k+1)]", and prop:loc-shell-cones requires the free data continuous.
  The densities q_in and q_out may jump. "Data that are smooth except across such leaves" also reads as allowing jumps of
  the conformal data, and those make the metric discontinuous, which no result here treats.

Replacement for item 8's New (lines 934-937):

    asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
    that are not smooth, except finitely many null shells along leaves of the two cones with densities smooth in angle and
    data that are smooth except across such leaves, where the metric functions are continuous, which [[thm:loc-shells]]
    develops slab by slab with [[thm:civp-large]] and [[thm:loc-cone-development]]; no result of the other chapters uses
    these developments.

For the same reason, item 2's New (lines 850-855) becomes:

    that are only bounded, and measure-valued densities in general, are not covered. Finitely many null shells along leaves
    {v = c} of 𝒞_out and {u = d} of 𝒞_in, with densities smooth in angle and supported in the band, and data that are smooth
    except across finitely many such leaves, where the metric functions are continuous, are covered by [[thm:loc-shells]]:
    their development is continuous, smooth between the leaves and a solution in the sense of distributions
    ([[def:loc-shell-solution]]), and near the background's data it exists on a neighbourhood of the two cones that does not
    depend on the data ([[thm:loc-shells]] (d)). For the 3 + 1 problem with two families of null dust,

and the last two lines of item 3's New (lines 868-869) become:

    angle; those, and data that are smooth except across finitely many leaves, where the metric functions are continuous,
    are developed slab by slab with [[thm:civp-large]] in [[thm:loc-shells]].

Each replacement replaces whole lines of the current file exactly once. It is at most 121 characters per line, also after
label resolution, and starts no wrapped line with a marker.

### C6. Nits

1. **rem:loc-shell-scope (i), lines 804-806**, for the same reason as C-1. "breaks on finitely many leaves" does not say
   that the metric functions stay continuous; only the later "a jump of the derivatives" implies it. Replacement:

        ([[rem:loc-cone-scope]] (iii)). Data that are only piecewise smooth, with breaks on finitely many leaves across which the
        metric functions are continuous, and no atoms, are covered by [[thm:loc-shells]] with every m_k and n_j zero; a jump of
        the derivatives of the free data across a leaf gives no singular part of Ric ([[lem:loc-shell-ricci]] (b)).
        (ii) *Domains.* The development of [[thm:loc-shells]] lies

2. **rem:loc-shell-scope (ii), lines 807-809.** "continues a solution through one crossing sphere, on a small square and
   on a neighbourhood of the two leaves beyond it". The neighbourhood holds only for solutions equal to the background
   near the axes (prop:loc-shell-crossing (c)); a round one continues on a small square only ((b)). Line 808 is also a
   stray short line. Replacement:

        in a neighbourhood of the cones on which no two shells cross. [[prop:loc-shell-crossing]] continues a solution through
        one crossing sphere: a round one on a small square, and one that equals the background near the axes also on a
        neighbourhood of the two leaves beyond it; a development on the whole rectangle Q1, where the shells cross away from the
        cones, is not asserted, as for smooth data

3. **Line 443 is a stray short line** ("edges nor an estimate. So we"). Replacement for lines 442-445:

        width that depends on the data only through a bound for their norms, but it gives neither a neighbourhood of the whole
        edges nor an estimate. So we prove it from the proof of [[thm:loc-cone-development]], that is from case (I) of
        [[sec:loc-cone-reduced]], at the corner (u_c, v_c).

With C-1 applied, and the nits at the writer's discretion, the file is confirmed.

---------------------------------------------------------------------------------------------------------------------

## Second confirmation (round 4)

**Verdict: CONFIRMED.** No Major, minor or nit remains open.

**File read.** `proofs/P-SHELL.md`, md5 0dbc56e0d7f13174376f7e7180142946, 971 lines. Its HEAD copy (commit 71185786) has
the same md5.

**Diff.** It was taken against the confirmed version (md5 93003d07…, from commit f700baf0). It contains exactly the
four changes and nothing else:
- **C-1.** The text is as I gave it:
  - item 8's New, at lines 935-939, carries "with densities smooth in angle" and "where the metric functions are
    continuous";
  - item 2's New, at lines 851-856;
  - the last two lines of item 3's New, at lines 869-870.
- **nit 1** (lines 803-806): as given.
- **nit 2** (lines 807-810): as given, except "a round one" becomes "a round solution". The meaning is the same, and the
  phrase is clearer.
- **nit 3** (lines 442-444): as given. The file is therefore one line shorter above line 495.
- **Crosswalk.** Five rows are renumbered by −1 (thm:loc-shells 495, eq:loc-shell-bands 500, prop:loc-shell-crossing
  666, eq:loc-shell-crossing-rule 687, rem:loc-shell-scope 799). All 21 rows point at their labels.

**Checks.**
- The file has no line longer than 121 characters and no wrapped line that starts with a marker. Line 695 has "round
  ones", which does not match the lint rule `round (one|two|three)`, because "ones" continues the word.
- Scratch build from a git archive of HEAD 71185786: the section was inserted before sec:loc-kid (83:2391), and all six
  Old texts occurred once and were applied. `assemble.py` reports 0 problems, `lint.py --chapters` reports 0 hits in 62
  files, and PAPER.md has no line longer than 121 characters.
