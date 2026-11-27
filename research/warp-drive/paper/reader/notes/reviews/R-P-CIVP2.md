# R-P-CIVP2: independent line-by-line reading of proofs/P-CIVP2.md

File read: `research/warp-drive/paper/reader/proofs/P-CIVP2.md`, md5 775b987a80e56ec8ac91a5ebfad0bfe1 (750 lines; the
brief says 751, `wc -l` gives 750 because the file ends with one newline after line 750). Every line was read. Nothing
under method/, drive/, extracted/ or recovered/ was read; no chapter, crosswalk or proof file was edited.

**Verdict: NOT CONFIRMED.** No Major issue. Five minor issues and fourteen nits outside the pending-marker interface,
all with exact replacements below. The mathematics checked here is correct: the frame, the connection table, (F1)-(F5)
and their images, the box and dust formulas, the 23-unknown system, its doubly-null form, the data lemma, the energy
lemma, the cut-off and periodisation, the localisation, the identification by continuation in u + v, uniqueness and the
formula for δ. Existence (a) stands or falls with the statement Tier 1 must supply (item T1 below), which is
prop:civp-large-corner itself; its written proof is a description of three changes to an unwritten proof.

---------------------------------------------------------------------------------------------------------------------

## A. What Tier 1 must supply (the pending interface)

**T1. prop:civp-large-corner, exactly as stated (uses [[pending:civp-tier1-local]] and [[pending:civp-tier1-theorem]],
lines 393-418).** Tier 1 must state and prove, or the proof of lines 404-418 must be replaced by a full proof of:

> Fix the regularity index m and η ∈ (0, π/8]. For every Λ > 0 there is σ > 0, depending only on Λ, η, m and the
> background on a neighbourhood of Q1 × S³, such that for **every** rectangle R = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂
> Q1 (corner anywhere in Q1, not only at S; any lengths) and every set of edge data — Ω > 0, γ_ϑ > 0, b, A_c, A_s,
> q_in ≥ 0 on N_o = {u_c} × [v_c, v_c + l_v] with **Ω and b arbitrary** (Ω not the background's), and Ω > 0, γ_ϑ > 0,
> A_c, A_s, q_out ≥ 0 on N_i = [u_c, u_c + l_u] × {v_c} with b = 0 — that agree on the corner sphere, satisfy
> Ric(∂_v, ∂_v) = q_in, Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(∂_u, ∂_u) = q_out on N_i, equal the background's off
> [2η, π/2 − 2η], and whose differences from the background's (ln Ω, ln γ_ϑ in place of Ω, γ_ϑ) have C^m norms ≤ Λ, with
> **no smallness**, there is a smooth class solution with N_f = 2 (phases v, u; densities q_in, q_out) in the gauge
> [[eq:loc-double-null]] on [u_c, u_c + min(l_u, σ)] × [v_c, v_c + min(l_v, σ)] × S³ that induces these functions on
> the two edges and equals (g0, q̊_in, q̊_out) off [η, π/2 − η].

Each feature in bold is used: arbitrary corner and uniform σ by the continuation in Step 4; arbitrary Ω on both edges
and arbitrary b on N_o because the edge data are formed from F on interior segments (after the change of angle only b
on N_i is zero; b on N_o becomes b − b(u_c, v_c, ·)); q ≥ 0 on interior edges (see minor 1). The written proof
(lines 404-418) names three steps of "that proof" that change; none can be checked until that proof exists, and "the
remaining steps of that proof apply unchanged" is an unverifiable assertion. For information only: the Tier 1 draft now
in proofs/P-CIVP.md (being written; read for the interface, not reviewed) states its theorem thm:loc-cone-development
for data from S on a fixed rectangle, with Ω kept the background's on 𝒞_out (as in prop:loc-cones), b = 0 on 𝒞_in, and
smallness ε ≤ ε0. That theorem does not by itself give T1; Tier 1 must cover a general corner, general Ω on both
edges, general b on N_o and σ = σ(Λ) uniform in the corner, or state T1 as its own result.

**T2. [[pending:civp-tier1-cin-cones]] (line 46, placement items 1 and 3).** The 𝒞_in analogue of prop:loc-cones in
the gauge b = 0: for free data (ℓ_1, ℓ_2, ℓ_3, q_out) on 𝒞_in ∩ {u ≤ u_1} agreeing with those on 𝒞_out at S and equal
to the background's outside a compact subset of (ϑ_a, ϑ_b) × [0, u_1], the constraint Ric(∂_u, ∂_u) = q_out determines
γ_ϑ, A_c, A_s (Ω the background's) on every generator on which e^ϕ stays positive, the result being the background's
at every ϑ outside the band. No step of the proof of thm:civp-large uses T2 (the theorem takes cone data as given in
def:civp-large-data); only the sentence at lines 46-49 and the placement prose do. (The draft's lem:loc-cone-in has
this form.)

**T3. [[pending:civp-tier1-theorem]] as a comparison (lines 4, 584-586, 599-601; placement items 2, 3, 4).** A theorem
giving, for cone data near the background's, a class solution in the gauge [[eq:loc-double-null]] on the explicit past
set {uv ≤ δ_*²} ∩ Q1 (times S³) that induces the data, **equals (g0, q̊_in, q̊_out) off [η′, π/2 − η′] for some η′ > 0**
(this is what lets thm:civp-large (c) give "the two developments agree where both are defined", line 586), and carries
an estimate of the solution; its uniqueness must be stated only near the background (line 600 contrasts it). Its data
(Ω the background's) must be cone data in the sense of def:civp-large-data, which they are.

**T4. The regularity index m** of [[pending:civp-tier1-local]] (line 394) must be defined there.

---------------------------------------------------------------------------------------------------------------------

## B. Findings

### minor 1 — nonnegativity of the densities of F is never shown (lines 250-255, 500, 505, 561)

lem:civp-large-reduction (line 190) assumes q_in, q_out ≥ 0, and def:class-system requires q_A ≥ 0; prop:civp-large-
system (b) (lines 250-255) has no such hypothesis, yet its proof ends "[[lem:civp-large-reduction]] concludes". Step 4
then says "Where F is geometric, (g_F, v, u, q_in, q_out) is a class solution" (line 505), feeds edge data formed from F
into prop:civp-large-corner, which requires q_in, q_out ≥ 0 (lines 396-397), and Step 5 concludes a class solution
(line 561). Nonnegativity of F's density components is true (homogeneous linear transport from nonnegative data) but is
stated nowhere.

Current (lines 252-255):

    (α, β, b), Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ, and Ric[h] equals the tensor with the frame components
    [[eq:civp-large-m]]. Then g := e^(−2ψ) h + e^(ψ−2ω) dφ1² + e^(ψ+2ω) dφ2², with v, u, q_in, q_out, is a solution of
    [[eq:class-system]] on U × T², of the form [[eq:loc-double-null]] with Ω = e^(α−ψ), γ_ϑ = e^(2β−2ψ), A_c = (ψ − 2ω)/2,
    A_s = (ψ + 2ω)/2.

Replace by:

    (α, β, b), Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ, and Ric[h] equals the tensor with the frame components
    [[eq:civp-large-m]]; and let q_in, q_out ≥ 0 on U. Then g := e^(−2ψ) h + e^(ψ−2ω) dφ1² + e^(ψ+2ω) dφ2², with v, u,
    q_in, q_out, is a solution of [[eq:class-system]] on U × T², of the form [[eq:loc-double-null]] with Ω = e^(α−ψ),
    γ_ϑ = e^(2β−2ψ), A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2.

Current (line 500):

    f₄-components are f̄₄ and its f₃-components the solution of [[lem:civp-large-data]] (b) (i), b vanishing there.

Replace by:

    f₄-components are f̄₄ and its f₃-components the solution of [[lem:civp-large-data]] (b) (i), b vanishing there. Its
    components q_in and q_out are nonnegative: they solve D_3q_in = −e^α χ̲ q_in and ∂_vq_out = −e^α χ q_out; 𝒮_δ is a
    past set, and the integral curves of D_3 = ∂_u + b∂_ϑ in a line {v = const} stay in (0, π/2), b vanishing off
    [ϑ_a − η0, ϑ_b + η0]; so q_in at a point is q_in at the point of {u = 0} on its integral curve, which is the data's and
    nonnegative, times a positive factor, and q_out is likewise the data's at v = 0 along {u = const, ϑ = const}.

### minor 2 — "smooth functions of (u, v, ϑ) on D × [0, π/2]" is false for A_c, A_s (lines 30-31, 33-35, 396-397)

For the background itself A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ) (line 23) are −∞ at ϑ = π/2 and ϑ = 0; no class metric
has A_c, A_s smooth on [0, π/2]. The same wording is used for cone data ("of (v, ϑ) on 𝒞_out ∩ (Q1 × S³)") and in
prop:civp-large-corner ("of (v, ϑ) on N_o × S³"). The intended meaning (smooth off the axes, metric regular at the axes)
should be said.

Current (lines 29-31):

    smooth class solution (g, v, u, q_in, q_out) of [[eq:class-system]] with N_f = 2, phases u_1 = v and u_2 = u and
    densities q_1 = q_in and q_2 = q_out, whose metric has the form [[eq:loc-double-null]] with Ω, γ_ϑ, b, A_c, A_s smooth
    functions of (u, v, ϑ) on D × [0, π/2] (the axes being regular points of the metric, as for g0).

Replace by (this also removes the u_1 clash of minor 3):

    smooth class solution (g, v, u, q_in, q_out) of [[eq:class-system]] with N_f = 2, the phase v carrying the density q_in
    and the phase u the density q_out, whose metric has the form [[eq:loc-double-null]] off the axes with Ω, γ_ϑ, b, A_c,
    A_s smooth functions of (u, v, ϑ) on D × (0, π/2), the metric extending smoothly to the axes, as g0 does.

Current (lines 33-35):

    **Definition {#def:civp-large-data}** (Cone data.) *Cone data* consist of smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s
    and q_in ≥ 0 of (v, ϑ) on 𝒞_out ∩ (Q1 × S³), and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) on 𝒞_in ∩ (Q1 × S³),
    with b = 0 on 𝒞_in, such that:

Replace by:

    **Definition {#def:civp-large-data}** (Cone data.) *Cone data* consist of smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s
    and q_in ≥ 0 of (v, ϑ) ∈ [0, v_1] × (0, π/2) on 𝒞_out, and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of
    (u, ϑ) ∈ [0, u_1] × (0, π/2) on 𝒞_in, with b = 0 on 𝒞_in, such that:

Current (lines 396-398, first part):

    × {v_c}. Let smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of (v, ϑ) on N_o × S³, and Ω > 0, γ_ϑ > 0, A_c,
    A_s and q_out ≥ 0 of (u, ϑ) on N_i × S³, with b = 0 on N_i, be given that agree on the corner sphere, satisfy

Replace by:

    × {v_c}. Let smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of (v, ϑ) ∈ [v_c, v_c + l_v] × (0, π/2), and
    Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) ∈ [u_c, u_c + l_u] × (0, π/2), with b = 0 on N_i, be given that agree
    on the corner sphere, satisfy

(The C^m norms of line 400 are of differences that vanish near the axes, so they are unaffected.)

### minor 3 — u1, v1 clash with the chapter's u1 = 5.7 and with the phase u_1 (lines 21-22 and passim)

The section is inserted into ch:localised-data, which fixes **u1 := 5.7** (sec:bg-data, "Put u1 := 5.7, u2 := 7.2";
sec:loc-setting "Region I is {u ≤ u1}, u1 = 5.7"; 45 occurrences in chapter 83). Line 21 redefines "We fix u1, v1 > 0".
Read in the chapter, rem:civp-large-beyond then says "when v1 > 4.5 and u1 > 7.2" (line 593) and "(v1 < 3 and u1 < 5.7"
(line 597), both meaningless with u1 = 5.7. Line 29 also writes the phases as "u_1 = v and u_2 = u", which renders as
u₁ next to the bound u1. prop:loc-cones and the chapter paragraph after it already write the cone length as **v_1**,
and the Tier 1 draft uses u_1, v_1.

Replacement: rename the bounds u1 → u_1 and v1 → v_1 everywhere in the section (lines 21, 22, 44, 48, 466, 467, 469,
470, 480-482, 486, 487, 489, 492, 508, 583, 593, 594, 597), e.g. line 22 "Q1 := [0, u_1] × [0, v_1]", line 466
"a0 := u_1, b0 := v_1", line 481 "s1 := min(a*, η0²/(2p1η0 + 4q1²v_1))", and remove "phases u_1 = v and u_2 = u" as in
the replacement of lines 29-31 under minor 2.

### minor 4 — "of any amplitude" omits the positivity of e^ϕ, and "when v1 > 4.5 and u1 > 7.2" presupposes an unproved
domain (lines 590-594; placement item 3, lines 656-658)

(i) Cone data from prop:loc-cones exist only on generators where e^ϕ stays positive; the section itself says so
(lines 47-48), but the remark and placement item 3 claim a development for "every perturbation of the shell ... of any
amplitude", although a large shell perturbation focuses e^ϕ to zero before v_1 and then there are no cone data on
[0, v_1]. (ii) The theorem needs the background defined in the gauge on a neighbourhood of Q1 × S³; nothing in the
section or the chapter shows that Q1 with u_1 > 7.2, v_1 > 4.5 is admissible (prop:two-dust-background (c)-(d) would
give it from R ≥ a at the far corner, which is not proved). A reader's numerical integration of the background's
characteristic problem (diamond scheme, h = 0.01 and 0.005, R agreeing to 10⁻⁴) gives R ≥ 1.338 and R_v > 0 on all of
[0, 7.5] × [0, 5], with μ(7.2, 0) ≈ 0.820-0.821 against the chapter's μ3 ∈ [0.8220998, 0.8221253], so the claim is
true; but the edition proves nothing numerically, and the remark should state it as a condition. (iii) Line 594 uses
𝒞_out^(v1), 𝒞_in^(u1), defined nowhere.

Current (lines 591-594):

    [[sec:loc-cones]] that are localised in a band away from the axes have developments without any smallness: among them
    every perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} and of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, of any amplitude,
    and every density added in the band, when v1 > 4.5 and u1 > 7.2. The development contains the strip {u ≤ δ} along all
    of 𝒞_out^(v1) and the strip {v ≤ δ} along all of 𝒞_in^(u1), so the dust on the cones lies in it; it is in the

Replace by:

    [[sec:loc-cones]] that are localised in a band away from the axes have developments without any smallness: among them,
    when the background is defined in the gauge on Q1 for some v_1 > 4.5 and u_1 > 7.2, every perturbation of the shell on
    𝒞_out ∩ {3 < v < 4.5} and of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, of any amplitude for which the factors e^ϕ stay
    positive on [0, v_1] and on [0, u_1], and every such density added in the band. The development contains the strip
    {u ≤ δ} along all of 𝒞_out ∩ {v ≤ v_1} and the strip {v ≤ δ} along all of 𝒞_in ∩ {u ≤ u_1}, so the dust on the cones
    lies in it; it is in the

Current (placement item 3, lines 656-658):

    With or without dust, the cone data of [[def:civp-large-data]], completed on 𝒞_in with b = 0 there, among them every
    perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} of any amplitude and
    every density added in the band, have a development in the gauge [[eq:loc-double-null]] on a neighbourhood {min(u, v) ≤

Replace by (this also fixes the muddled "the cone data of [[def:civp-large-data]], completed on 𝒞_in"):

    With or without dust, these cone data, completed on 𝒞_in in the gauge b = 0 ([[def:civp-large-data]]), among them,
    when v_1 > 4.5, 𝒞_in is taken on u ≤ u_1 with u_1 > 7.2 and the background is defined on [0, u_1] × [0, v_1], every
    perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} of any amplitude for
    which e^ϕ stays positive and every density added in the band, have a development in the gauge [[eq:loc-double-null]]
    on a neighbourhood {min(u, v) ≤

### minor 5 — placement item 4 makes the opening sentence of the chapter-90 paragraph false (lines 665-677)

Item 4 appends the cone result, "without smallness", to the paragraph of ch:scope whose first sentence (ch. 90,
lines 191-192) says the results on localised data concern data on Σ_τ0 or a bent slice and "invariant data near the
background's data". After the insertion that sentence no longer describes the paragraph. Add to item 4 a second old/new
pair (both old lines occur exactly once in chapters/90-scope.md, at lines 191-192):

Old:

    The results on localised data concern the explicit two-dust background of [[sec:bg-data]], on its slice Σ_τ0 or on a
    slice bent from it, and invariant data near the background's data ([[ch:localised-data]]). Data localised in angle away

New:

    The results on localised data concern the explicit two-dust background of [[sec:bg-data]]: invariant data near the
    background's data on its slice Σ_τ0 or on a slice bent from it, and data of any size on the two null cones through its
    corner sphere ([[ch:localised-data]]). Data localised in angle away

### nit 1 — "ten lines ... seven" (line 233)

The display eq:civp-large-system has nine lines: five with ∂_v, four with D_3 (ten and seven are the numbers of
equation forms), while line 264 says "line by line" of the display. Current: "The first ten lines have ∂_v and govern
f₄, the last seven have D_3 and govern f₃." Replace by: "The equations of the first five lines have ∂_v and govern f₄;
those of the last four have D_3 and govern f₃."

### nit 2 — "R² × Y" (line 236)

R² reads as the area radius squared (line 22 has γ_ϑ = R²); the (u, v)-plane is meant. Current: "A^ϑ∂_ϑf = G(f) on
R² × Y," Replace "R² × Y" by "ℝ² × Y" (same length).

### nit 3 — the description of the proof of [CCTW16, Theorem 5.3] (lines 16-18)

That proof (pp. 55-56, checked) builds the development up in t = u + v by solving Cauchy and mixed problems at t = t*
(their Figures 5.2-5.4, Theorems 5.1-5.2); it uses no corner developments. "shown as in the proof of [CCTW16, Theorem
5.3]: the development is built up ... from local developments near corner spheres" attributes the corner problems to
them. Current lines 16-18:

    cones. That this solution solves the Einstein equations is shown as in the proof of [CCTW16, Theorem 5.3]: the
    development is built up in the time u + v from local developments near corner spheres ([[prop:civp-large-corner]]),
    each of which coincides with the strip solution by an energy estimate ([[lem:civp-large-energy]]).

Replace by:

    cones. That this solution solves the Einstein equations is shown by the device of the proof of [CCTW16, Theorem 5.3,
    pp. 55–56], which builds the development up in the time u + v; where that proof solves Cauchy and mixed problems, the
    local developments here are those near corner spheres ([[prop:civp-large-corner]]), each of which coincides with the
    strip solution by an energy estimate ([[lem:civp-large-energy]]).

### nit 4 — the cited form (4.47)-(4.50) has a misprint the reader will meet (lines 277-278)

[CCTW16] p. 47 prints ℓ(ϕ0) = ψ0 in (4.48) and ω(ψ0) = ϕ0 in (4.50) (and ψ0, ϕ0 in (4.56), p. 48), with ϕ0 = ψ0 = h set
in (4.47); they must read ℓ(ϕ0) = ψ₋, ω(ψ0) = ϕ₊ — the forms D_3Ψ° = e^αΨ_3, ∂_vΨ = e^αΨ_4 used here (confirmed against
the arXiv v2 text). Current lines 277-278:

    equations, through M_44 and M_33. The wave block is the first-order form of [CCTW16, (4.47)–(4.50), p. 47], with their
    ℓ and ω in the roles of e3 and e4. The equations (F4), (F5), their images and the relations of

Replace by:

    equations, through M_44 and M_33. The wave block is the first-order form of [CCTW16, (4.47)–(4.50), p. 47], with their
    ℓ and ω in the roles of e3 and e4; there the first equations of (4.48) and (4.50) are misprinted, and with ϕ0 = ψ0 = h
    they read ℓ(ϕ0) = ψ₋ and ω(ψ0) = ϕ₊, the forms used here. The equations (F4), (F5), their images and the relations of

### nit 5 — (3.100)-(3.101) are not "the restrictions of" the whole system (lines 460-461)

(3.100) is the ϕ-block on {v = 0}, (3.101) the ψ-block on {u = 0}; the restriction of the whole system to {v = 0}
would contain the transversal ∂_v of f₄. Current:

    (3.100)–(3.101)] of [[thm:std-cctw-existence]] for this system are the restrictions of [[eq:civp-large-localised]] to
    {v = 0} and {u = 0}. They have global solutions: on J0 take the solutions of [[lem:civp-large-data]] (b) (i), and on

Replace by:

    (3.100)–(3.101)] of [[thm:std-cctw-existence]] for this system are its f₃-equations restricted to {v = 0} and its
    f₄-equations restricted to {u = 0}. They have global solutions: on J0 take the solutions of [[lem:civp-large-data]]
    (b) (i), and on

### nit 6 — δ is not uniquely defined by (d) (lines 436-439; also rem line 583)

a*, b* are existential constants (any smaller ones also work), and s1, s2 also depend on the choice of ϱ and f̊_e in
Step 1. Current lines 437-439 ("they are given by the constants a*, b* of [[thm:std-cctw-strips]] for the localised
system [[eq:civp-large-localised]] / with the data of [[lem:civp-large-data]] and by three suprema of its solution, and
they depend on the cone data through / these."). Replace by:

    they are given by constants a*, b* that [[thm:std-cctw-strips]] provides for the localised system
    [[eq:civp-large-localised]] with the data of [[lem:civp-large-data]], for any choice of the cut-off and the extension in
    its definition, and by three suprema of its solution, and they depend on the cone data through these. No lower bound
    for δ in terms of norms of the cone data is asserted.

(replacing lines 437-439 entirely).

### nit 7 — "independent of ℓ" is not in the quoted Corollary 3.11 (line 581)

Corollary 3.11 (p. 35) does not say ℓ-independent; Theorem 3.9 does, for a*. Current: "theorem asserts their existence,
independent of ℓ, and gives no bound for them." Replace by: "theorem asserts their existence and gives no bound for
them (a* does not depend on ℓ by [[thm:std-cctw-existence]], nor b* by that theorem with u and v exchanged)." (reflow
lines 580-583).

### nit 8 — "a vacuum development of any size" (line 598)

[CTG23, Theorem 1.1] is about data of any size; the development is a neighbourhood. Replace "gives a vacuum development
of any size;" by "gives a vacuum development for data of any size;".

### nit 9 — placement item 6 refers to "the two cones" before any cone or background is named in ch. 3 (lines 696-699)

Current:

      construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge
      of cone data localised in an angular band away from the axes, with or without dust and without smallness, on a
      neighbourhood of the two cones that depends on the data, localised and unique in the gauge among solutions equal to
      the background near the axes ([[thm:civp-large]]); and exactly localised vacuum data

Replace by:

      construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge
      of data on the two null cones through the corner sphere of the explicit two-dust background of [[sec:bg-data]],
      localised in an angular band away from the axes, with or without dust and without smallness, on a neighbourhood of
      the two cones that depends on the data, localised and unique in the gauge among solutions equal to the background
      near the axes ([[thm:civp-large]]); and exactly localised vacuum data

### nit 10 — placement item 9 forgets the appendix crosswalk (lines 748-750)

crosswalk/95-standard-results.tsv has one row per label (e.g. thm:std-ctg-neighbourhood, row 29); the two new labels
need rows. Current lines 749-750 end "The crosswalk of / [[ch:localised-data]] receives one row for each label listed
in item 1." Replace by:

    uses the cone developments, and the section uses only results those chapters state. The crosswalk of
    [[ch:localised-data]] receives one row for each label listed in item 1, and that of [[app:standard-results]] one row
    each for thm:std-cctw-existence and thm:std-cctw-strips.

### nit 11 — a full stop inserted inside the quotation of Theorem 3.9 (line 716)

The source (p. 32) has the display "Ω0 = [0, a0] × [0, b0] × Y" with no punctuation, followed by "Consider". Current
"× Y. Consider" — replace by "× Y Consider" (verbatim; the line becomes 120 characters).

### nit 12 — data lemma (a): "given by [[eq:civp-large-coefficients]] in the functions on N_o" (lines 290-292)

Only ϖ, η̲ (on N_o) and ϖ̲ (on N_i) come from eq:civp-large-coefficients; q_in, Ψ°, Ψ_4, Ψ_1 (resp. α, β, b, q_out, Ψ,
Ψ_3, Ψ′_1) are the functions and their tangential derivatives. Replace "on N_o the f₃-components other than χ̲ are given
by [[eq:civp-large-coefficients]] in the functions on N_o" by "on N_o the f₃-components other than χ̲ are the functions
on N_o and their derivatives along N_o, ϖ and η̲ through [[eq:civp-large-coefficients]]", and "on N_i the f₄-components
other than η and χ are given by [[eq:civp-large-coefficients]] in the functions on N_i" by "on N_i the f₄-components
other than η and χ are the functions on N_i and their derivatives along N_i, ϖ̲ through [[eq:civp-large-coefficients]]".
Also, in "η and χ solve (F5) and (F4)" (line 292) the linearity in η needs η̲ = 2e1α − η, which (b) writes out (line
305) but (a) leaves implicit; add "(with η̲ = 2e1α − η)" after "(F5)".

### nit 13 — CCTW's fixed connection ∇̊ must also preserve the splitting (lines 244, 468)

(2.8) is followed by "the connections ∇ and ∇̊ preserve the splitting"; the text names one connection. Replace "the
scalar product and the connection preserving the splitting" (line 244) and "with the scalar product and the flat
connection preserving the splitting" (line 468) by "with the scalar product, and the flat connection as both ∇ and ∇̊,
preserving the splitting".

### nit 14 — overloaded letters

(i) R is the area radius (line 22), the curvature operator R(X, Y) (line 134) and a rectangle (lines 284, 353, 395,
518): rename the rectangle 𝒬 (unused in the section). (ii) η is a connection coefficient and a component of F, and also
the band margin of prop:civp-large-corner (line 394, "η ∈ (0, π/8]") with "η := η0" in Step 4 (line 516), where F's η
is in play: rename the margin κ. (iii) k is e^(α−β) (line 214) and the spread k(u, v) of the energy lemma (line 362),
both in Step 3 (q1 := sup e^(α−β), "k = c1u + c2v"): rename the spread w(u, v). (iv) q1 (a supremum, line 481) sits
beside q_1 = q_in (line 30, removed by the replacement under minor 2). (v) In ch. 83, f = 1 − μ/R² and ψ = ln q are the
background's chart functions (sec:loc-setting, sec:bg-data); here f is the 23-vector and ψ = A_c + A_s. (v) is
acceptable with the explicit definitions; (i)-(iii) cost a reader effort in one proof.

---------------------------------------------------------------------------------------------------------------------

## C. Checked and found correct

**Frame and transport (lem:civp-large-frame), re-derived by hand and by an independent sympy script**
(`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/civp2-check/
frame_check.py`, built from the coordinate Christoffel symbols and Ricci tensor of h for arbitrary α, β, b(u, v, ϑ),
not from the writer's scripts): the products of e3, e4, e1 (line 64-65); every coefficient formula of
eq:civp-large-coefficients, and ξ = ξ̲ = 0, from the definitions (zero residual); the whole connection table
eq:civp-large-table and its exchange invariance; the three commutators, coordinate and frame (lines 120-131), giving
ζ = −¼e^(β−2α)∂_vb and η − η̲ = 2ζ; the frame Ricci relations Ric_44, Ric_41, Ric_11 = −L and Ric_34 + Ric_11 = K/2
(pair symmetry and antisymmetries suffice); (F1)-(F5) and all five images (zero residual each), and every intermediate
coefficient in the written derivations of (F1)-(F5) (lines 145-170); □_h in both forms (eq:civp-large-box and its
image); both dust divergences eq:civp-large-dust (zero residual); (d) div_g(q g⁻¹du) = e^(2ψ) div_h(q h⁻¹du) (by hand:
√|g| = e^ψ√|g3|, √|h| = e^(3ψ)√|g3|, g⁻¹du = e^(2ψ)h⁻¹du). The writer's claim that with h the dust laws carry no e^ψ
weight is correct. Statement at lines 100-101 correct.

**lem:civp-large-reduction:** correct from prop:reduction (R11 = R22 = 0 ⇔ both waves, then Ric[h]_ab = T_ab +
(3/2)dψ² + 2dω²), lem:warped-ricci for the mixed components, g^(uu) = g^(vv) = 0 for the gauge, and (d); frame
components of T (lines 204-205) correct.

**The 23-unknown system and its form:** every one of the 23 equation forms of eq:civp-large-system was checked by sympy
to equal, identically, e^α times the corresponding defect (Ric_ij − M_ij, −□_hΨ, or the dust divergence), or zero for the
coefficient and commutator equations; so prop:civp-large-system (a) holds and (b) is its converse. Counts 10 + 13 = 23;
A^u = diag(I₁₀, 0), A^v = diag(0, I₁₃), A^ϑ = (bI₁₀, Q; Qᵀ, 0) with Q four entries −e^(α−β) in distinct rows and
columns at the stated pairs (so |Q| = e^(α−β)), f₄f₄ block zero; coefficients and G polynomial in f, e^(±α), e^(±β).
This is exactly the form (2.7)-(2.8) of [CCTW16] with A^u_ϕϕ = I, A^v_ψψ = I. The wave block matches (4.47)-(4.50) with
ℓ ↔ e3, ω ↔ e4 (ϕ+ ↔ Ψ_4, ψ₋ ↔ Ψ_3, ϕ_A ↔ Ψ_1, ψ_A ↔ Ψ′_1), up to the misprint of nit 4. The proof of (a) "line by line"
matches the display line by line.

**lem:civp-large-data:** (a) tangency on N_o, N_i, the linear ODEs (F4′), (F5), (F4) with the corner values, uniqueness;
(b) every definition of f̄₃, f̄₄ and every initial value at S (χ̲ = e^(−α)∂_uβ since ∂_ϑb = 0 on 𝒞_in; η = ζ + e1α;
χ = e4β); (b)(i) on 𝒞_out: α, β, b, Ψ, Ψ′_1 equations by definition and the commutator, χ by (F1) with Ric_44 = M_44
from Ric(∂_v, ∂_v) = q_in and prop:reduction (g3(∂_v, ∂_v) = 0), η by (F2) with Ric_41 = M_41, then the linear Ψ_3, ϖ̲,
q_out; on 𝒞_in: χ̲ by (F1′) with Ric(∂_u, ∂_u) = q_out (g3(∂_u, ∂_u) = γ_ϑb² = 0, and Ric_33 tangential since b ≡ 0 on
𝒞_in), the η̲ identity D_3η̲ = −e^α(M_31 + χ̲(η̲ − η)) re-derived from 2e3e1α = −4e1ϖ̲ − (2ϖ̲ + χ̲)(η + η̲) and the defining
(F5), then Ψ_4, ϖ, q_in; (ii) locality in ϑ and uniqueness; (iii). The omission of the 𝒞_in momentum constraint from
def (ii) is correct: with b = 0 on 𝒞_in it is a transport equation for ∂_vb there, which (F5) encodes.

**lem:civp-large-energy:** divergence identity; C₁ finite; W is a convex polytope (k linear), so the divergence theorem
applies; the signs of all six face terms, including the conormals ±dϑ + c1du + c2dv; the completed square
(c1 − p)|z₃|² − 2q|z₃||z₄| + c2|z₄|² = (√t|z₃| − q|z₄|/√t)² with c1 = p + t, c2 = q²/t; part (b).

**Cut-off and periodisation (Step 1):** (2.8) stays exact (ϱ multiplies only A^ϑ and G; A^u, A^v unchanged); ϱA^ϑ(f)
symmetric and smooth in (f, u, v, ϑ); f̊_e solves the localised system at every point (ϱ = 0, or ϑ in the interior of J0
where f̊_e = f̊); data smooth because f̄ = f̊ near the ends of J0; (3.100)-(3.101) are ODEs (A^v_ϕϕ = 0, b = 0 at v = 0,
A^ϑ_ψψ = 0) and the glued solutions are global and smooth.

**Hypotheses of [CCTW16, Theorem 3.9] (Step 2):** Y = ℝ/πℤ compact without boundary, n = 2, ℓ ≥ 6 > 11/2; trivial
bundle, Euclidean product, flat ∇ compatible and splitting-preserving (and ∇̊, nit 13); A^μ self-adjoint, smooth in f
and coordinates; G = G(f, ·); (2.7)-(2.8); smooth data in (3.99); global solvability of (3.100)-(3.101); a0 = u_1,
b0 = v_1; N₋ = {u = 0} carries ϕ̄ = f₃, N₊ = {v = 0} carries ψ̄ = f₄, as CCTW require. Smoothness and C¹ uniqueness on
both strips (Theorem 3.9 with u, v exchanged).

**Localisation and δ (Step 3):** the z-equation and its B; z's data vanish on I = Y ∖ (ϑ_a, ϑ_b); on [0, s1] × [0, v_1]
with t = 2q1²v_1/η0: c2 = η0/(2v_1), c1s1 ≤ η0/2 from s1 ≤ η0²/(2p1η0 + 4q1²v_1), so k ≤ η0; on [0, u_1] × [0, s2]:
b = 0 at v = 0 on all of Y, |b| ≤ β1s2 ≤ η0/(4u_1), t = η0/(4u_1), c1u ≤ η0/2, c2s2 ≤ η0/2 from s2 ≤ η0²/(8q1²u_1); the
arc I has length > 2η0; 𝒮 ⊂ 𝒰; F smooth, equal to f̊ off [ϑ_a − η0, ϑ_b + η0], solving the unlocalised system (at the two
end angles by continuity); F's cone values. (b) of the theorem follows.

**Identification (Step 4):** "geometric" is a pointwise condition on F and its derivatives, so the geometric set is
closed; the Constants paragraph (Λ fixed before σ; the change of angle's derivatives are bounded independently of σ);
η0 < π/12 ≤ π/8; the change of angle: dϑ − b du = (dΦ − (∂_uΦ + b∂_ϑΦ)du)/∂_ϑΦ, γ_ϑ → γ_ϑ/(∂_ϑΦ)², b → ∂_uΦ + b∂_ϑΦ,
zero on N_i, identity map on N_o and off [ϑ_a − η0, ϑ_b + η0] (note b on N_o becomes b − b(u_c, v_c, ·), consistent
with "applies to the transformed functions"); constraints are invariant; corner values of all reduced fields involve
only derivatives tangent to N_o or N_i, so "geometric to first order" at the corner suffices; the two cases of an edge
(geometric set, or 𝒞_out/𝒞_in with f̄) give the same linear ODEs; the z-system for f_c − F and lem (b) on
[η0/2, π/2 − η0/2]. Continuation: t* ≥ min(L, l1, l2) > 0 (the first corner is S, where f̄ has the coefficient values);
u_c + v_c < t* always, so the corner of R_p is geometric; N_i ⊂ {u + v ≤ t*} when v_c > 0, N_o likewise; sides ≤ L < σ;
every point with t* ≤ u + v < t* + L/4 lies in some R_p (both cases, including the boundary case, checked); the case
t* + L/4 > l1 + l2; closure gives the far corner. The argument is sound given T1.

**Steps 5-6, (c), (d):** the induced cone data via eq:civp-large-h; extension to the axes; uniqueness via lem (b)(iii),
η″ = min(η′, η0), past sets, lem (b) on [η″/2, π/2 − η″/2]; (c) does not need Step 4 (it compares g′ with g_F); 𝒮_δ is a
past set and contains {uv ≤ δ²}.

**Cited labels** (each checked to be the result the text says): eq:loc-double-null, lem:loc-cone-equations,
prop:loc-cones, sec:loc-cones (ch. 83); eq:class-system, def:class-system (q_A ≥ 0), thm:class-kato (a) (T* depends on
a bound for ‖u0‖ and ρ; with ρ = ∞ by rem:class-kato-local), thm:class-kato-stability (a), rem:class-kato-local
(ch. 81); prop:reduction, lem:warped-ricci (ch. 2); eq:two-dust-limit (ch. 80; q̊_in = 𝒜/R³, q̊_out = ℬ/R³ in the
chapter's double-null coordinates, Ω² = e^(2σ)/2); thm:std-ctg-neighbourhood, sec:std-characteristic (ch. 95);
cor:vlasov-two-dust; ch: and part: labels of the placement items. All 30 labels of item 1 are defined in the file and
nowhere else; the file also defines thm:std-cctw-existence, thm:std-cctw-strips (item 7).

**[CCTW16], against arXiv:1406.3009v2 (page-located text via alphaXiv; the writer's extraction agrees):** (2.1)-(2.2) and
the quoted sentences on the bundle, scalar product, connection, self-adjoint A^μ, Y, ∇̊ on p. 6; (2.7)-(2.9) and the
quoted sentences on p. 7; N₋, N₊ and the overline convention, (3.2) G_i = G(f_i, ·) on p. 11; N₋, N₊ again and Theorem 3.9
on p. 32, ending on p. 33 with "where ℓ1 is ... The solution f is unique within the class of C¹ solutions, and is smooth
if ϕ̄ and ψ̄ are" (the omitted sentence is the ℓ > (n + 12)/2 regularity (3.102)); every quoted phrase of Theorem 3.9
matches except the inserted full stop (nit 11); Corollary 3.11 and the "symmetry of the problem under the interchange
of u and v" sentence on p. 35, quoted exactly; (4.47)-(4.50) on p. 47 with the misprint the writer reports (confirmed,
also in (4.56) on p. 48); Theorem 5.3 on p. 54 (Theorems 5.1 Rendall and 5.2 on pp. 53-54), its proof on pp. 55-56 with
t := u + v (5.21) and t* (5.22).

**Bibliography:** the publisher's page (impan.pl, reached through doi:10.4064/dm732-7-2015) gives "Dissertationes
Mathematicae 515 (2016), 1-67", citation_volume 515, firstpage 1, lastpage 67; the edition's current entry (98-
references, lines 26-28) prints "(2016), 1–72" and no volume; item 8's old text matches the file exactly and its new
text is correct; the appendix (ch. 95, line 7) does state that pages are those of the arXiv versions.

**Placement:** every old text occurs exactly once, at the stated lines of the current sources: ch. 83 lines 8-9 and
593-600, ch. 90 line 200, ch. 1 lines 190-191, ch. 3 line 367, ch. 98 lines 26-28; each is a whole line or run of
lines; each new text joins the following line grammatically (ch. 83 line 10 "[Rac16] ...", ch. 1 line 192 "numerical
point ...", ch. 3 line 368 "near the initial data ..."). Item 7's insertion point (sec:std-characteristic, before
thm:std-ctg-neighbourhood) exists and the alphabetical order is kept. Item 1's insertion point (before sec:loc-kid, ch.
83 line 602) exists. Content of the new texts correct apart from minor 4, minor 5, nit 9.

**Typography:** maximum line length 121 (no line longer), and label resolution only shortens lines (every resolved form
is shorter than its label; equation tags replace "  {#eq:...}" by "    (n.m)"); no wrapped line begins with "+ ", "- ",
"* ", "> ", "#", "=" or "|" (the two "- [CCTW16]" lines are list items after blank lines); all label keys lowercase;
lint.py reports only the pending markers and the cross-file labels a single-file run cannot see. All replacement texts
above are at most 121 characters per line.
