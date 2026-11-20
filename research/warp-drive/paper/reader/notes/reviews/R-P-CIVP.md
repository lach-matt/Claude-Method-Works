# R-P-CIVP: independent line-by-line reading of proofs/P-CIVP.md

File read: `research/warp-drive/paper/reader/proofs/P-CIVP.md`, md5 aa08312166da99581416a9753bad3c98, 1188 lines,
18 proofs. Every line was read. Also read: chapter 83 (sec:loc-setting, sec:loc-cones, sec:bg-data, lem:bg-reduction),
chapter 81 (def:class-system, sec:class-structure, sec:class-augmented, sec:class-kato in full, Steps 9-10 of
thm:class-stability-off-axes, cor:class-short-time), chapter 80 (eq:two-dust-metric, eq:two-dust-limit,
prop:two-dust-background, lem:two-dust-reparametrisation), chapter 02 (lem:warped-ricci, sec:gauge), chapter 03
(lem:gauge-propagation), Appendix A (sec:std-characteristic, the extension theorems), the writer's report
notes/reports/P-CIVP.md, the Tier 2 review notes/reviews/R-P-CIVP2.md, and the current proofs/P-CIVP2.md (md5
924a45ecfbef762ee34a500044e9414f, 796 lines; the review read an earlier 750-line version). Nothing under method/, drive/,
extracted/ or recovered/ was read; no chapter, crosswalk or proof file was edited. Private checks (sympy) and the
scratch merge are in the session scratchpad only.

**Verdict: NOT CONFIRMED.** 2 Major, 11 minor, 17 nits. The two Major findings concern the uniqueness statement
(d) and the sharp localisation (b) of thm:loc-cone-development; existence (a), the estimate (c), lem:loc-cone-in and
prop:loc-cone-local (Tier 2's T1) are sound up to the minor findings. All replacement texts below are at most 121
characters per line and start no wrapped line with a Markdown marker.

---------------------------------------------------------------------------------------------------------------------

## A. Findings

### Major 1: the uniqueness lemma's smallness depends on the point (lines 824-864; thm (d), lines 67-71)

Current (lines 834-837): "Fix a point p of G_* with 3η ≤ ϑ(p) ≤ π/2 − 3η, u(p) < u_1 and v(p) < v_1; the remaining
points follow by continuity. Take δ′ ∈ (0, δ_c/2] and κ′ > 0 so small that p lies in 𝒟′ := {(u, v) : u, v ≥ 0, (u +
δ′)(v + δ′) ≤ δ_*², u + κ′v ≤ u_1, v + κ′u ≤ v_1} × {…}"; and (line 826) "For ε and ε_2 small it equals the solution …".

What is wrong. (i) For p near the hyperbola uv = δ_*², p ∈ 𝒟′ forces δ′ → 0, and the wave-map Cauchy problem is posed
on the slab of the time τ′ = ln((u + δ′)(v + δ′)), whose length ln(4δ_*²/δ′²) and whose chart coefficients degenerate as
δ′ → 0; the ε0 of [[thm:class-kato-stability]] (a) therefore depends on δ′, hence on p. "For ε and ε_2 small" is then not
uniform in p, and "the remaining points follow by continuity" cannot repair this: for fixed ε, ε_2 equality is obtained
only on a set with a margin depending on ε, ε_2, whose closure is not G_* ∩ {3η ≤ ϑ ≤ π/2 − 3η}. The theorem claims
ε_2 independent of the point. (ii) 𝒟′ contains (u_1, 0) ∈ N_i (take v = 0 in u + κ′v ≤ u_1), so "a cut-off in (u, v)
equal to 1 near 𝒟′" has support meeting {u > u_1, v ≥ 0}, where g″ (= g′ on G_*, Ĝ on P ∩ 𝒰) is not defined.
(iii) Step (1) applies [[lem:loc-cone-jets]] (iv) on G_*, which does not contain a neighbourhood of N in F (see minor 9).

Fix: extend g′ beyond G_* (with C^k bounds), pose the wave-map problem once on the fixed slab of the construction, take
𝒟′ := G_* ∩ (angular wedge), and run the energy estimate on Φ(𝒟′) with the matrices of the competitor 𝐔̃, for which the
faces of Φ(𝒟′) (images of the null faces {u = u_1}, {v = v_1}, of the spacelike face {uv = δ_*²} and of the angular faces
of g′) are causal. Replacement for lines 826-827, last sentence of the statement:

    of order at most k at the points with 2η ≤ ϑ ≤ π/2 − 2η. For ε and ε_2 small, depending only on the background, u_1,
    v_1, the band and k, it equals the solution of [[lem:loc-cone-gauge]], in their coordinates, at the points of G_* with
    3η ≤ ϑ ≤ π/2 − 3η.

Replacement for lines 829-858 (steps (1)-(3); the wave-map display, line 841, is kept where marked):

    *Proof.* (1) *An extension of g′.* By [[lem:loc-cone-jets]] (iv), G_* being a past set, the functions of g′, like
    those of Ĝ, have the derivatives a_j, b_k across N ∩ G_*; so g′ − Ĝ vanishes to infinite order on N ∩ G_*. Let G_*^+
    be the set of the points of 𝒰 within distance δ_c/4 of G_*, and fix ψ smooth on [0, π/2], equal to 1 on [17η/8,
    π/2 − 17η/8] and supported in (2η, π/2 − 2η). The function f equal to ψ (g′ − Ĝ) on G_* and to 0 on P ∩ G_*^+ is
    smooth there; extend it to G_*^+, for each ϑ, by the operator of [[thm:std-sy-extension]] for a bounded Lipschitz
    domain that contains G_* ∪ (P ∩ G_*^+) and lies in G_* ∪ P, and put g″ := Ĝ + f on G_*^+. Then g″ is smooth, equals Ĝ
    on P ∩ G_*^+ and g′ at the points of G_* with 17η/8 ≤ ϑ ≤ π/2 − 17η/8, g″ − Ĝ vanishes to infinite order on
    N ∩ G_*^+, being smooth and zero on P there, and ‖g″ − Ĝ‖_(C^(k−1)) ≤ C (ε + ε_2), the operator being bounded on
    W^(k,∞).

    (2) *A wave map.* Let 𝒟′ be the set of the points of G_* with 9η/4 + 2C_* e^(τ/2) ≤ ϑ ≤ π/2 − 9η/4 − 2C_* e^(τ/2),
    τ of [[eq:loc-cone-time]]; as G_* ⊂ F ∩ 𝒰, 2C_* e^(τ/2) ≤ η/2 there, so 𝒟′ contains the points of G_* with
    3η ≤ ϑ ≤ π/2 − 3η, and g″ = g′ on 𝒟′. Seek Φ = id + φ with id: (𝒟′, (Φ⁻¹)^*g″) → Ĝ a wave map, that is

        [the display of line 841, unchanged]

    a semilinear wave system for φ whose principal part is that of g″. As in [[lem:loc-cone-system]] and
    [[lem:loc-cone-cauchy]], case (I), on the slab [τ_init, τ_+] × ℝ⁴, with a cut-off in ϑ equal to 1 on [9η/4, π/2 −
    9η/4] and supported in (17η/8, π/2 − 17η/8), a cut-off in (u, v) equal to 1 near G_* and supported in G_*^+, and the
    frozen part taken with the wave operator of g_e: φ := 0 satisfies the cut-off system on P exactly, as g″ = Ĝ there,
    and on F up to the residual 1_F g″^(μν)(Γ[Ĝ] − Γ[g″])^λ_(μν), which vanishes to infinite order on N and is at most
    C(ε + ε_2) in C^(k−2). [[thm:class-kato-stability]] (a) with s = k − 2 > 3 gives a smooth solution φ on the slab with
    φ small in W^(1,∞), the constants depending only on the background, u_1, v_1, the band, k and δ_c; φ = 0 on P, by
    the argument of [[lem:loc-cone-past]]; and on 𝒟′ it solves the wave map system, the cut-offs being 1 there.

    (3) *Comparison.* For ε, ε_2 small, Φ is a diffeomorphism near the identity, equal to it on P and so, with all
    derivatives, on N. Put g̃ := (Φ⁻¹)^*g″, ũ_A := u′_A ∘ Φ⁻¹ with u′_in := v, u′_out := u the phases of g′,
    p̃_A := −dũ_A, Θ̃_A := div_(g̃) P̃_A and q̃_A := q′_A ∘ Φ⁻¹ on Φ(𝒟′). Then D(g̃) = 0 relative to Ĝ, so (g̃, p̃_A, Θ̃_A,
    q̃_A) solves 𝒜 = 0 on Φ(𝒟′) (off the axes, with [[eq:class-raychaudhuri]] for (Aug3)), and so does U on
    F ∩ 𝒰 ∩ {η < ϑ < π/2 − η}, which contains Φ(𝒟′) ([[lem:loc-cone-constraints]]). Both equal Û, with all derivatives,
    on N. The difference z of their first-order variables satisfies A^μ(x, 𝐔̃) ∂_μ z = Mz on Φ(𝒟′), with the matrices
    of 𝐔̃, whose wave block has the inverse metric g̃ and whose transport fields are P̃_A. The faces of 𝒟′ other than N
    are {uv = δ_*²}, {u = u_1}, {v = v_1} and two angular faces. As g′ has the form [[eq:loc-double-null]] in these
    coordinates, the conormal v du + u dv of the first is timelike for it, g′⁻¹(v du + u dv, v du + u dv) =
    2uv g′^(uv) < 0; du and dv are null, du vanishes on −g′⁻¹du and is positive on −g′⁻¹dv, and dv vanishes on −g′⁻¹dv
    and is positive on −g′⁻¹du; the angular conormals are timelike as in [[lem:loc-cone-support]], g′ being C⁰-close
    to g_e there, and positive on −g′⁻¹du and −g′⁻¹dv. Φ carries g′ on 𝒟′ to g̃ and the phases of g′ to the ũ_A, so the
    outward conormals of the faces of Φ(𝒟′) other than N are future causal for g̃ and nonnegative on P̃_in and P̃_out.
    [[lem:loc-cone-energy]] on Φ(𝒟′), with B_0 := N ∩ 𝒟′ and B_1 its other faces, gives z = 0.

and in step (4), line 863: "So Ψ ∘ Φ is the identity near p, and the functions of g′ at p are those of the" →
"So Ψ ∘ Φ is the identity on 𝒟′, and the functions of g′ on 𝒟′ are those of the" (the next line ends "solution of
[[lem:loc-cone-gauge]]."; drop "at p"). The unused g_e′ of the old step (1) disappears with it.

### Major 2: the sharp localisation (b) is proved by a limit δ_c → 0 at fixed ε (lines 60-62, 1002-1007)

Current (lines 1005-1007): "The construction may be made with every smaller δ_c, and by (d) the solutions coincide on
G_*, all of them equalling the background where ϑ < 3η or ϑ > π/2 − 3η; letting δ_c → 0 gives (b)."

What is wrong. ε_0 depends on δ_c ([[lem:loc-cone-system]] (a) names δ_c among the dependences; the slab
[ln(δ_c²/4), ln c_+] grows and the chart degenerates as δ_c → 0), so for a fixed ε the construction exists only for
δ_c ≥ δ_c(ε) and δ_c → 0 is not available. Moreover (d) needs the competitor within ε_2 in C^k, while (c) gives only
C^(k−4), so (d) does not apply to the solution of another construction. Statement (b) as written is not proved; its
"in particular" clause, and every use of (b) (in (d) and in Tier 2's T3), only need a fixed margin. Replacement for
lines 60-62:

    (b) *Localisation.* The solution equals the background at the points of G_* × S³ with ϑ < ϑ_a′ − η/4 − 2C_0 (uv)^(1/2)
    or ϑ > ϑ_b′ + η/4 + 2C_0 (uv)^(1/2), and at those with u < u_K and v < v_K. In particular it equals the background
    where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η.

Replacement for lines 1000 (from "[[lem:loc-cone-cauchy]], case (I),") to 1007:

    u_K} (the constraints there have the background's coefficients and corner values). In case (I) take δ_c so small also
    that 2C_0 (δ_c(u_1 + v_1 + 1))^(1/2) ≤ η/4, a condition depending only on the background, u_1, v_1 and the band.
    [[lem:loc-cone-cauchy]], case (I), [[lem:loc-cone-past]], [[lem:loc-cone-support]], [[lem:loc-cone-constraints]] and
    [[lem:loc-cone-gauge]] give a solution with (a) and (c) on G_*. For (b): [[lem:loc-cone-support]] and the last part
    of [[lem:loc-cone-gauge]] give the background at the points of G_* with ϑ < ϑ_a′ − 2C_* ((u + δ_c)(v + δ_c))^(1/2),
    with ϑ > ϑ_b′ + 2C_* ((u + δ_c)(v + δ_c))^(1/2), or with u < u_K and v < v_K; on G_*, (u + δ_c)(v + δ_c) ≤ uv +
    δ_c(u_1 + v_1 + 1), so 2C_* ((u + δ_c)(v + δ_c))^(1/2) ≤ 2C_0 (uv)^(1/2) + η/4. As 2C_0 (uv)^(1/2) ≤ 2C_* δ_* ≤ η/4
    on G_*, ϑ_a′ > ϑ_a and ϑ_b′ < ϑ_b, the solution equals the background where ϑ < ϑ_a′ − η/2 or ϑ > ϑ_b′ + η/2, in
    particular where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η, and where ϑ < 3η or ϑ > π/2 − 3η. So (d) is [[lem:loc-cone-unique]]
    together with (b) for the solution of (a). ∎

(The first line repeats the end of line 999-1000 so that the block replaces whole lines.) The placement phrase "equal to
the background outside the domain of influence of the band" (items 3, 4, 6, 7) should then read "equal to the background
outside a slightly wider band" (minor 10).

### minor 1: G-invariance of the Cauchy solution is used but never shown (lines 708-710)

lem:loc-cone-gauge uses that g is T²-invariant (form [[eq:loc-double-null]] with functions of (u, v, ϑ), "by the
reflections, dφ1 and dφ2", "G-invariant" ϑ′, line 799) and calls the result a class solution; nothing proves that U is
G-invariant (Step 9 of [[thm:class-stability-off-axes]] has this argument; the file does not). Current lines 709-710:

    [[lem:class-kato-linear]] (c)), F̃ being smooth with compact support. The rows of (c) of [[lem:loc-cone-system]] hold at
    τ_init, where 𝐔 = 𝐔̊. ∎

Replace by:

    [[lem:class-kato-linear]] (c)), F̃ being smooth with compact support. The rows of (c) of [[lem:loc-cone-system]] hold at
    τ_init, where 𝐔 = 𝐔̊. The system is invariant under G: χ, θ, the reference states, h and P̄_A are G-invariant, and G
    acts on the components of 𝐔 in the chart (τ, y) by orthogonal maps fixing 𝐔_c, which preserve |𝐔 − 𝐔_c| ≤ r_0,
    where ϒ is the identity. So the image of the solution under an element of G is a solution with the same data, and by
    the uniqueness in [[thm:class-kato]] (a) it is the solution: U is G-invariant. ∎

### minor 2: (c) of lem:loc-cone-system is false where χ < 1 (lines 611-619, 629, 631-632, 645-647)

The frozen part (1 − χ) A^μ_♭ ∂_μ Z is a principal part only, so the first wave row of 𝔄_χ(𝐔) = F̃ is
χ(∂_τ g − g_τ) + (1 − χ) ∂_τ(g − g̊) = 0, not ∂_τ g − g_τ = 0, where χ < 1; "Both systems have these two rows" (line 645)
fails for the first row. The conclusion is only used where χ = 1 along the τ-lines from Σ_init (𝒪_1), where it holds,
but the lemma states it on the whole slab and lem:loc-cone-cauchy repeats it. Fix by giving the frozen part the
zeroth-order term of Step 9. After "on supp χ_𝒰, A^μ_♭ = A^μ(x, 𝐔̊)." (line 614) insert:

    Let B_♭ be the constant matrix with B_♭Z = (Z_(g_τ), 0, …, 0), Z_(g_τ) the component of Z in the place of g_τ, so
    that the first row of A^μ_♭ ∂_μ Z − B_♭Z is ∂_τ Z_g − Z_(g_τ), as in Step 9.

in [[eq:loc-cone-modified]] (line 616) replace "(1 − χ) A^μ_♭ ∂_μ Z," by "(1 − χ)(A^μ_♭ ∂_μ Z − B_♭Z),"; in (b) (line 629)
replace "𝔄_χ(𝐔) = A^μ(x, 𝐔̊) ∂_μ(𝐔 − 𝐔̊)" by "𝔄_χ(𝐔) = A^μ(x, 𝐔̊) ∂_μ(𝐔 − 𝐔̊) − B_♭(𝐔 − 𝐔̊)"; in the proof of (a) (line
642) replace "∂_μ𝐔̊) + F̃(x)" by "∂_μ𝐔̊) + (1 − χ) B_♭Z + F̃(x)". The proof of (b) stands, and Φ stays a local
forcing term. (The displayed line becomes 105 characters.)

### minor 3: "bounds of every order" (lines 626-627)

Current: "The bounds of every order of the A^μ_χ and of Φ, and c_1, depend only on Λ, η, k, δ_c and the background." The
derivatives of Δ of order above k + 3 are not controlled by the size (they depend on the cut-off scales chosen in
[[lem:loc-cone-borel]]), so this is false; only order-k bounds are used ([[rem:class-kato-local]], the paragraph after
it). Replace by:

    the sense of [[rem:class-kato-local]]. Every derivative of the A^μ_χ and of Φ is bounded on bounded sets of Z, and
    their bounds of order k + 1, and c_1, depend only on Λ, η, k, δ_c and the background.

(this replaces line 626 from "the sense of" and line 627).

### minor 4: case (II) of lem:loc-cone-gauge, the image containing [0, σ]² (lines 806-812)

"Ψ − id is small in C¹" gives |Ψ − id| ≤ C(Λ)σ^(1/(4k)), which is not smaller than the distance (about σ) from [0, σ]² to
the face {τ = ln((δ_c + 2σ)²)}; the step needs the bound that uses Ψ = id on N. After "in case (I) at most Cε in
C^(k−3)." (line 807) insert:

    In case (II), Ψ − id vanishes on N and every point of F ∩ 𝒰_σ ⊂ [0, 6σ]² is joined to N in it by a segment of
    length at most 6σ, so |Ψ − id| ≤ 6σ sup |d(Ψ − id)| ≤ C(Λ) σ^(1 + 1/(4k)), while the points within σ of [0, σ]² lie
    in 𝒰_σ, as (δ_c + 2σ)² bounds (u + δ_c)(v + δ_c) there.

### minor 5: a degree argument with no entry in Appendix A (lines 810-812)

"by the homotopy invariance of the degree of id + t(Ψ − id), 0 ≤ t ≤ 1, the image of Ψ contains these sets" uses a
published result (Brouwer degree) in a proof step; Appendix A has no entry, and item 9 says none is needed. A contraction
avoids it. Current lines 810-812, from "Ψ is" to "contains these sets.", replace by:

    Ψ is the identity on P ∩ 𝒰, where u_out = u, u_in = v and ϑ′ = ϑ, and on the sets of [[lem:loc-cone-support]]. Let y be
    a point of G_* (in case (II), of [0, σ]²) and B the closed ball about y of radius 2 sup |Ψ − id|, in the coordinates
    (u, v, ϑ), with Ψ = id where ϑ ∉ [η, π/2 − η]; B lies in 𝒰′ for ε (for σ) small, and x ↦ y − (Ψ(x) − x) maps B into B
    and is a contraction, sup |d(Ψ − id)| being less than 1/2. Its fixed point x satisfies Ψ(x) = y, and x lies in
    F ∩ 𝒰_σ, since Ψ fixes the points of P ∩ 𝒰. So the image of Ψ contains G_* (in case (II), [0, σ]²).

(In case (II) the radius is at most C(Λ)σ^(1 + 1/(4k)) by minor 4, so B lies in 𝒰′. Alternatively keep the degree argument and add the degree's homotopy invariance to Appendix A with a source and page.)

### minor 6: σ of prop:loc-cone-local is not shown uniform in the corner (lines 534-535, 591-593, 939, 955)

C_* := sup_𝒮 e^(σ_e)/R_e depends on the corner (𝒮 moves with it); δ_c := √c_+/8 (line 955) depends on C_*, and σ := σ_0
on δ_c; likewise δ_2 is an infimum and a supremum over 𝒮. So "Every choice above depends only on k, η, Λ, d and the
background on Q′" (line 971) is not justified as written. Every use of C_* needs only C_* ≥ sup_𝒮 e^(σ_e)/R_e. Replace
line 534-535 "Put C_* := sup_𝒮 e^(σ_e)/R_e (in case (I), C_* := C_0, which is at least that by
[[lem:loc-cone-strips]] (b))," by

    *Constants, coordinates and regions.* Fix a number C_* ≥ sup_𝒮 e^(σ_e)/R_e (in case (I), C_* := C_0, admissible by
    [[lem:loc-cone-strips]] (b); for [[prop:loc-cone-local]], C_* := sup_(Q′) e^(σ_e)/R_e), c_+ := (min(δ_1, η/C_*)/4)²,

(reflowing the rest of the paragraph); in lines 591-593 replace "δ_2 := (inf Ω̂²/(10 C_b² sup γ̂_ϑ))^(1/2), the infimum and
the supremum over the points of 𝒮 with 2η ≤ ϑ ≤ π/2 − 2η, where b̂ can be nonzero; by |X̂ − X̊| ≤ C_b, δ_2 depends only on
Λ, η and the background" by "δ_2 := (e^(−4C_b) inf Ω_e²/(10 C_b² sup R_e²))^(1/2), the infimum and the supremum over 𝒮
(for [[prop:loc-cone-local]], over Q′), which is at most (inf Ω̂²/(10 C_b² sup γ̂_ϑ))^(1/2) by |X̂ − X̊| ≤ C_b; δ_2 depends
only on Λ, k and the background"; and in line 939 replace "and C_* ≤ sup_(Q′) e^(σ_e)/R_e." by "and C_* := sup_(Q′)
e^(σ_e)/R_e is admissible." (C_b, through [[lem:loc-cone-jets]] (iii), also depends on k and on the edge lengths, at most
3d here; say "depending only on Λ, k and the background" at line 576.)

### minor 7: the data of the theorem on [v_1, v_1 + δ_1] (lines 150-153)

Current: "on 𝒞_out the functions of [[prop:loc-cones]], extended to v ≤ v_1 + δ_1 by the background's, and on 𝒞_in those
of [[lem:loc-cone-in]], extended likewise; the extensions are smooth, as K_out ⊂ …". Extending γ_ϑ, b, A_c, A_s by the
background's is wrong: at v_1 the factor e^ϕ and b differ from the background's, so the extension is neither smooth nor a
solution of the constraints. The proof of the theorem (lines 995-998) solves the constraints on [0, v_1 + δ_1]. Replace
lines 150-153 by:

    The data of [[thm:loc-cone-development]] are cone data at the corner S, with l_u = u_1, l_v = v_1: on 𝒞_out the
    functions that [[prop:loc-cones]] determines from the free data extended to v ≤ v_1 + δ_1 by the background's, and on
    𝒞_in those that [[lem:loc-cone-in]] determines from the free data extended likewise to u ≤ u_1 + δ_1; the extended free
    data are smooth, as K_out ⊂ [0, v_1) × (ϑ_a, ϑ_b) and K_in ⊂ [0, u_1) × (ϑ_a, ϑ_b). The background on 𝒮 is provided by
    the next lemma.

### minor 8: "smooth functions … of (v, ϑ)" including the axes (lines 129-132, 134-136, 373-374, 925-927)

A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ) are infinite at ϑ = π/2 and ϑ = 0, so no cone datum or class metric has ϰ_2, ϰ_3
smooth on [0, π/2]; the same point is minor 2 of R-P-CIVP2, which Tier 2 has repaired. Replacements: line 131-132 "with Ω,
γ_ϑ, b, A_c, A_s smooth functions of (u, v, ϑ), equal to the background's near the axes" → "with Ω, γ_ϑ, b, A_c, A_s
smooth functions of (u, v, ϑ) ∈ D × (0, π/2), equal to the background's near ϑ = 0 and ϑ = π/2"; line 135-136 "of (v, ϑ)
on N_o and … of (u, ϑ) on N_i" → "of (v, ϑ) ∈ [0, l_v + δ_1] × (0, π/2) on N_o and … of (u, ϑ) ∈ [0, l_u + δ_1] × (0, π/2)
on N_i"; line 374 "on [0, l_v + δ_1] × [0, π/2] and b_k (k ≥ 0) on [0, l_u + δ_1] × [0, π/2], with values in ℝ⁷" → "on
[0, l_v + δ_1] × (0, π/2) and b_k (k ≥ 0) on [0, l_u + δ_1] × (0, π/2), with values in ℝ⁷"; lines 925-926 "of (v, ϑ) on
N_o, and … of (u, ϑ) on N_i" → "of (v, ϑ) ∈ [v_c, v_c + λ_v] × (0, π/2), and … of (u, ϑ) ∈ [u_c, u_c + λ_u] × (0, π/2)"
(reflow each paragraph). The differences from the background's, which the norms measure, vanish near the axes and are
unaffected.

### minor 9: lem:loc-cone-jets (iv) is applied on G_*, outside its hypothesis (lines 390-392; used at 829-830)

(iv) assumes D contains a neighbourhood of N in F; G_* does not contain one of N_o ∩ {v > v_1}, of N_i ∩ {u > u_1}, or of
(u_1, 0), (0, v_1). The proof is local along the generators, so a past-set version holds. Replace lines 390-391:

    (iv) every class solution in the gauge on D × S³, where D ⊂ F is a past set (with each (u, v) it contains
    [0, u] × [0, v]) whose interior is dense in it, smooth up to N ∩ D, whose functions on N_o ∩ D and N_i ∩ D are the cone
    data, has ∂_u^j X = a_j on N_o ∩ D and ∂_v^k X = b_k on N_i ∩ D; in particular å_j and

and in the proof (line 485) "on N" → "on N ∩ D" (twice).

### minor 10: the placement texts state uniqueness without the smallness of the competitor (lines 1045, 1064, 1096, 1107)

"unique in the gauge off the axes" (items 3, 4, 6, 7) is stronger than thm (d), which compares only solutions within ε_2
of the background in C^k; Tier 2's T3 requires exactly that the uniqueness be stated "near the background only". In each
of the four sites replace "unique in the gauge off the axes" by "unique in the gauge near the background off the axes",
and, after Major 2, "equal to the background outside the domain of influence of the band" by "equal to the background
outside a slightly wider band" (reflow). The merged texts of section C do this.

### minor 11: two sentences become false when Tier 2 is merged (line 79; item 7, lines 1107-1108)

rem:loc-cone-scope (i): "For cone data that carry dust and are not small nothing is asserted." and item 7: "developments
of dust-carrying cone data that are not small, or whose perturbation reaches an axis, are not established". With
[[thm:civp-large]] in the same chapter both are false. Replace in line 79 by "For cone data that carry dust and are not
small the theorem asserts nothing; [[thm:civp-large]] develops them on a neighbourhood that depends on the data." (reflow
lines 78-81), and replace item 7 by the merged text D of section C. If Tier 2 is not merged, keep the current wording.

### Nits

1. Line 38: "a = 0.70 the inner radius of [[sec:loc-setting]]" — a = q0 − δ0 is the inner radius of [[sec:domain]];
   [[sec:loc-setting]] gives its value. Replace by "a = q0 − δ0 = 0.70 the inner radius of [[sec:domain]]
   ([[sec:loc-setting]])".
2. Lines 32-34: "the two cones carry one metric, … with the background's ϕ, so the free data … agree" reads as a
   deduction; it is the requirement. Replace by "the two cones must induce one metric, γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s)
   dφ2²; as ϕ is the background's on S on both cones, this holds exactly when the free data of [[prop:loc-cones]] at
   v = 0 and those of [[lem:loc-cone-in]] at u = 0 agree".
3. Line 125: "with σ_e, R_e > 0 smooth on 𝒮" says σ_e > 0, false for the background (e^(2σ) = 1/2 on the cones).
   Replace by "with σ_e and R_e smooth on 𝒮 and R_e > 0"; likewise line 920-921 "with σ_e and R_e > 0 smooth on 𝒪" →
   "with σ_e and R_e smooth on 𝒪 and R_e > 0".
4. Line 342: "and C^r norm at most C(r, j) ‖h‖_(C^r)" holds for j ≥ r or for fixed ε only (derivatives of order i > j
   carry ε^(j−i)); the terms of index ≤ r have ε = ε_0, as used. Replace by "and, for ε = ε_0 or j ≥ r, C^r norm at
   most C(r, j, ε_0) ‖h‖_(C^r)".
5. Notation overloads in Block B: η is ∂_ϑ ln Ω ([[eq:loc-cone-quantities]]) and the band margin (sec:loc-cone-reduced
   onward), both in force in lem:loc-cone-system; ε_0 is the theorem's threshold and the cut-off scale of
   [[lem:loc-cone-borel]] (line 577 "with ε_0 = δ_e"); a_0 is the first jet and the extension length of
   [[lem:loc-cone-extension]] (and a = E(∂_v, ∂_v), a = 0.70); R is the area radius and the rectangle of
   [[prop:loc-cone-local]] (Tier 2 renamed its rectangle 𝒬); σ is the rectangle size beside σ_e; u_1 = 7.2 (line 75)
   sits beside the chapter's u1 = 5.7, u2 = 7.2 (line 183 uses both). Suggested: the frame coefficient η → ϖ (unused in
   the file), the Borel scale ε_0 → ε_B, the extension length a_0 → λ_e, the rectangle R → 𝒬.
6. Line 902: "Then y ≥ y(l_v′)/2 > 0 on [0, l_v + δ_1]" → "Then y > 0 on [0, l_v + δ_1], and y ≥ y(l_v′)/2 on
   [l_v′, l_v + δ_1]".
7. Line 669: "and 𝔄_χ(Ů) = 0 on a neighbourhood of each point of F ∩ 𝒰 ∖ K" is false at points of ∂F (Ů solves nothing
   on P); the pointwise statement suffices. Replace by "and 𝔄_χ(Ů) = 0 at each point of F ∩ 𝒰 ∖ K, where Ĝ = g_e on a
   neighbourhood and Ů solves its own system on F ∩ 𝒮".
8. Line 831: g_e′ is defined and never used (removed by Major 1's replacement).
9. Placement line numbers have drifted: item 5's old text is now lines 191-193 of chapter 01 (not 189-191), item 6's
   lines 381-382 of chapter 03 (not 373-374), item 7's line 208 of chapter 90 (not 200). Items 1-4 are exact.
10. Crosswalk rows: the source field "P-CIVP:6" departs from the table's convention "paper/reader/proofs/P-CIVP.md:6"
    (as for P-K83b, P-B-morawetz); and the "Notes for existing rows" give no exact new cell texts.
11. Line 169: Q = [0, ∞) × [0, V1′] must contain the segment 𝒞_out ∩ {v ≤ v_1 + δ_1}; add "with V1 chosen so large
    that V1′ > v_1 + 1" (prop:two-dust-background allows every V1 above its bound).
12. Line 183: "R = 5 − 0.47u … ([[lem:bg-reduction]] (a))" — (a) gives R″ = −ℬ/(3R²) with R(u1) = 2.321, R′(u1) = −0.47;
    add "as ℬ = 0 there" so the linear form is read off.
13. Line 981-982: "for three reasons, which are the only places where the proof uses the background" — the proof uses
    the background throughout (sizes are differences from it, X̂ = X̊ + Δ, the constants of
    [[lem:loc-cone-extension]]). Replace by "for three reasons, which are why the proof needs a background and not
    only bounds on the data".
14. Lines 45-46, 61 and 489: if K_in meets {u = 0} then u_K = 0 and the last clause of (b) is empty, while
    [[prop:loc-cone-formal]] takes u_K, v_K > 0; add "(that clause being empty when u_K = 0 or v_K = 0)" in (b).
15. Line 920-922 (suggestion): prop:loc-cone-local needs the equations only on 𝒮 ∩ F for each corner, so on
    𝒪 ∩ {u ≥ inf_Q u, v ≥ inf_Q v}; requiring them on all of 𝒪 asks for a background beyond the cones, which the
    chapter does not construct (line 186-187 "for instance the one of this chapter on a neighbourhood of a rectangle"
    is not established for rectangles touching u = 0 or v = 0). Weakening the hypothesis to "σ_e, R_e smooth on 𝒪,
    solving [[eq:two-dust-limit]] on 𝒪 ∩ {u ≥ inf_Q u, v ≥ inf_Q v}" (with the extension of
    [[lem:loc-cone-strips]] (b)) would let Tier 2 apply it to the chapter's background on Q1 itself.
16. Line 100-101, [Ren90, p. 221]: the quoted words are the first part of the abstract's first sentence, which continues
    "and examples are given of how it can be used in practice"; acceptable as a partial quotation, or close it with " …".
17. lem:loc-cone-jets (iii): C_j also depends on the lengths of the edges (Gronwall along N); add "the lengths of the
    edges" to "depending only on j, Λ and the background".

---------------------------------------------------------------------------------------------------------------------

## B. The Tier 2 interface (T1-T4)

**T1 against prop:loc-cone-local.** Tier 2's prop:civp-large-corner (current lines 415-425) is prop:loc-cone-local with
Q := Q1, η := κ, (λ_u, λ_v) := (l_u, l_v), m := m_1 = 12k + 42 for a fixed k ≥ 6, and the background g0 written as
−2e^(2σ) du dv + R² dΩ₃² with e^(2σ) = 2Ω², R² = γ_ϑ. Every feature Tier 2 lists is provided: corner anywhere in Q, any
λ_u, λ_v; Ω arbitrary on both edges; b arbitrary on N_o and zero on N_i; densities ≥ 0 on the given edges (checked: the
sign lemma transports them with a positive factor and P_A(u_A) = 0); no smallness; σ depending only on k, η, Λ, d and
bounds of the background on Q′, independent of λ_u, λ_v — and of the corner once minor 6 is applied. On the factor 2:
Tier 2 bounds ln γ_ϑ − ln γ̊_ϑ = 2(ϰ_1 − ϰ̊_1) by Λ, so Tier 2's hypothesis implies Tier 1's with the same Λ; no change of
Λ is needed in the citation (the factor 2 matters only in the converse direction). Tier 2's hypothesis "the background is
defined … on a neighbourhood of Q1 × S³" supplies the open set 𝒪 and d; see nit 15 for a weaker hypothesis that the
chapter's background meets without an extension beyond the cones.

**T2 against lem:loc-cone-in.** Matches. lem:loc-cone-in also fixes the corner values of ϕ and ∂_uϕ as the background's;
Tier 2's restatement (lines 56-60) omits them.

**T3 against thm:loc-cone-development.** Matches for the use Tier 2 makes (comparison only): G_* = {uv ≤ δ_*²} ∩ Q1 is a
past set; the solution equals (g0, q̊_in, q̊_out) where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η, η = ¼ min(ϑ_a, π/2 − ϑ_b), so off
[3η, π/2 − 3η] (this needs only the "in particular" of (b), which Major 2's replacement keeps); estimate (c); uniqueness
near the background only. Two differences from Tier 2's wording (lines 21-26): the theorem keeps Ω the background's on
both cones, not only on 𝒞_out; and it needs K_out ⊂ [0, v_1) × (ϑ_a, ϑ_b) (open at v_1), while def:civp-large-data allows
[0, v_1].

**T4.** m_1 := 2m_0 + 6 = 12k + 42 is defined in prop:loc-cone-local; for k = 6, m = 114.

**What Tier 2's text must change to cite these** (line numbers of the current P-CIVP2.md):

1. Lines 3-4: "for data near the background's the development is [[pending:civp-tier1-theorem]]." → "for data near the
   background's the development is that of [[thm:loc-cone-development]]."
2. Lines 21-26 (the paragraph *The small-data theorem.*), replace by:

       *The small-data theorem.* [[thm:loc-cone-development]] is used only for comparison, in [[rem:civp-large-domain]]
       and [[rem:civp-large-beyond]]. Its data are cone data in the sense of [[def:civp-large-data]], with Ω the
       background's on both cones, obtained by [[prop:loc-cones]] and [[lem:loc-cone-in]] from free data within ε_0 of the
       background's in C^(6k+21) that equal the background's outside compact subsets of [0, v_1) × (ϑ_a, ϑ_b) and
       [0, u_1) × (ϑ_a, ϑ_b), with u_1, v_1 as in that theorem; it gives a class solution in the gauge
       [[eq:loc-double-null]] on the explicit past set {uv ≤ δ_*²} ∩ Q1, times S³, that induces the data and equals (g0,
       q̊_in, q̊_out) where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η, η := (1/4) min(ϑ_a, π/2 − ϑ_b), with an estimate of the solution,
       and its uniqueness in the gauge is stated near the background only.

3. Line 54: "([[pending:civp-tier1-cin-cones]])" → "([[lem:loc-cone-in]])"; and delete the sentence of lines 56-60 "The
   analogue on 𝒞_in is the statement: … outside the band." (it restates lem:loc-cone-in without the corner condition on ϕ,
   ∂_uϕ).
4. Lines 407-413: delete the paragraph "*What is required of [[pending:civp-tier1-local]].* … lengths of the edges."
5. Lines 415-416: "Let m be the regularity index of [[pending:civp-tier1-local]] and κ ∈ (0, π/8]." → "Let m := 114, the
   regularity index m_1 = 12k + 42 of [[prop:loc-cone-local]] for k = 6, and κ ∈ (0, π/8]." (reflow).
6. Lines 426-440 (the proof by "three changes"), replace by:

       *Proof.* Choose d ∈ (0, 1] such that the background is defined, in the gauge [[eq:loc-double-null]], on an open set
       𝒪 that contains the points within 4d of Q1 in each coordinate. In the notation of [[prop:loc-cone-local]], with
       Q := Q1, k := 6, η := κ, λ_u := l_u and λ_v := l_v, the background is g0 = −2e^(2σ) du dv + R² dΩ₃² with
       e^(2σ) = 2Ω² and R² = γ_ϑ, solving [[eq:two-dust-limit]] on 𝒪, and the given functions are data of that
       proposition, with ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s: the C^m norm of ϰ_1 − ϰ̊_1 is half that of
       ln γ_ϑ − ln γ̊_ϑ, so each difference has C^m norm at most Λ. That proposition gives the solution, with σ depending
       only on κ, Λ, d and the background on that set. ∎

7. Lines 612 and 629: "[[pending:civp-tier1-theorem]]" → "[[thm:loc-cone-development]]".
8. Placement (lines 638-645): the opening paragraph's references to the Tier 1 section become [[sec:loc-cone-proof]],
   [[thm:loc-cone-development]], [[lem:loc-cone-in]] and [[prop:loc-cone-local]]; item 1 "after the section of
   [[pending:civp-tier1-theorem]], which follows [[sec:loc-cones]]," → "after [[sec:loc-cone-proof]], which follows
   [[sec:loc-cones]],". Items 2, 3, 4 (second pair), 5 and 6 are replaced by the merged texts of section C.
9. Two terms are defined twice in the merged chapter: "class solution in the gauge" (Tier 1 line 129-132, with equality
   to the background near the axes; Tier 2 lines 30-33, with only smooth extension to the axes) and "cone data"
   (def:loc-cone-data and def:civp-large-data). Tier 2's definition sentence should refer to Tier 1's, e.g. "A *class
   solution in the gauge* on D × S³ is as in [[sec:loc-cone-setting]], with D ⊂ Q1 and the condition at the axes
   relaxed: Ω, γ_ϑ, b, A_c, A_s are smooth on D × (0, π/2) and the metric extends smoothly to the axes, as g0 does.", and
   def:civp-large-data be titled "(Cone data on Q1.)" with its term "*cone data on Q1*".

---------------------------------------------------------------------------------------------------------------------

## C. Placement: occurrence check and merged texts

Every old text occurs exactly once, as whole lines: item 3 at chapter 83 lines 8-9, item 4 at chapter 83 lines 593-600,
item 5 at chapter 01 lines 191-193, item 6 at chapter 03 lines 381-382, item 7 at chapter 90 line 208. Item 1's anchor
(chapter 83 line 591, "background's by uniqueness. ∎") and item 2's (line 602, the heading of sec:loc-kid) are exact.

Overlaps with Tier 2: chapter 83 lines 8-9 (Tier 1 item 3, Tier 2 item 2) and lines 593-600 (Tier 1 item 4, Tier 2
item 3) are replaced by both; also chapter 01 lines 192-193 (Tier 2 item 5 replaces two of the three lines of Tier 1 item
5), chapter 90 line 208 (Tier 1 item 7 and the second pair of Tier 2 item 4 have the same old text), and chapter 03, where
the two items change different lines of the same bullet "More families" and would describe the developments twice. One
merged text for each site (old texts as in the items; all lines ≤ 121; they assume Major 2 and minor 10 applied):

**A. Chapter 83, lines 8-9** (replaces Tier 1 item 3 and Tier 2 item 2):

    Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
    and data localised in an angular band exist exactly ([[prop:loc-cones]], [[lem:loc-cone-in]]); when the band avoids the
    axes they have a development in the double-null gauge on a neighbourhood of the two cones, with or without dust, equal
    to the background outside a slightly wider band: without smallness, on a neighbourhood that depends on the data and
    unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]), and, for data near the
    background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). On Σ_τ0 the
    constraints split, after Rácz

**B. Chapter 83, lines 593-600** (after Block A; replaces Tier 1 item 4 and Tier 2 item 3):

    [[thm:loc-cone-development]] develops these cone data, completed on 𝒞_in by [[lem:loc-cone-in]], when they are near the
    background's and their band avoids the axes, with or without dust: on the explicit neighbourhood G_* of the two cones
    there is a class solution in the gauge [[eq:loc-double-null]] that induces them, with an estimate, equal to the
    background outside a slightly wider band and unique in the gauge near the background off the axes. Every small
    perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, and every small density
    added in the band, supported away from the axes, is of this kind, with v_1 = 4.5 and u_1 = 7.2
    ([[lem:loc-cone-strips]] (c)). Without smallness, these cone data, completed on 𝒞_in in the gauge b = 0
    ([[def:civp-large-data]]), have a development in the gauge [[eq:loc-double-null]] on a neighbourhood {min(u, v) ≤ δ} of
    the two cones whenever their band avoids the axes; among them, when the background is defined on [0, u_1] × [0, v_1] for
    some v_1 > 4.5 and u_1 > 7.2, are every perturbation of the shell or of the packet of any amplitude for which e^ϕ stays
    positive and every density added in the band. That development equals the background outside a slightly wider band
    and is unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]); the number δ
    depends on the data. For vacuum data of any size, before the shell (v_1 < 3) and on 𝒞_in before the packet (u_1 < 5.7),
    a development near the two cones exists also by [CTG23, Theorem 1.1] ([[thm:std-ctg-neighbourhood]]), which gives
    neither uniqueness in the gauge nor localisation. No development is asserted for cone data that differ from the
    background's near an axis, for data of finite regularity or for densities that are not smooth, and no other result of
    this paper uses these developments.

**C. Chapter 01, lines 191-193** (Tier 1 item 5's old text; drop Tier 2 item 5, which says the same):

    [[part:further]] treats two crossing dusts ([[ch:two-dusts]]), the class Einstein–null-dust system
    ([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data, their development from two
    null cones and the sign of the charge ([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]],
    [[ch:equality-edge]]), the threshold λ0 at a

**D. Chapter 90, line 208** (replaces Tier 1 item 7 and the second pair of Tier 2 item 4; Tier 2's first pair, on the
opening sentence of the paragraph, stands):

    small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]). On the two null
    cones through the corner sphere, data localised in an angular band exist exactly, with or without dust
    ([[prop:loc-cones]], [[lem:loc-cone-in]]); when the band avoids the axes they have a development in the double-null
    gauge on a neighbourhood {min(u, v) ≤ δ} of the cones, without smallness, equal to the background outside a slightly
    wider band and unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]); δ
    depends on the data, and for data near the background's the neighbourhood is explicit and the solution carries an
    estimate ([[thm:loc-cone-development]]). Developments of cone data that differ from the background's near an axis are
    not established ([[rem:loc-cone-scope]]).

**E. Chapter 03, bullet "More families"**: keep Tier 2 item 6's site (old text "  construction of that background does
not decide ([[cor:vlasov-two-dust]]); and exactly localised vacuum data") with this new text, and drop Tier 1 item 6:

      construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge
      of data on the two null cones through the corner sphere of the explicit two-dust background of [[sec:bg-data]],
      localised in an angular band away from the axes, with or without dust and without smallness, on a neighbourhood of
      the two cones that depends on the data, localised and unique in the gauge among solutions equal to the background
      near the axes ([[thm:civp-large]]), and, for data near the background's, on an explicit neighbourhood with an
      estimate ([[thm:loc-cone-development]]); and exactly localised vacuum data

If Tier 2 is not merged, Tier 1's items 3, 4, 6, 7 stand with the two phrase changes of minor 10.

**Typography on a scratch merge.** chapters/, crosswalk/, assemble.py, lint.py (and OUTLINE.md) were copied to
scratchpad/rpcivp/; Block A was inserted after chapter 83 line 591, Block B (heading without "Block B.") before line
602, items 3-7 applied, and the 36 crosswalk rows appended. Before: lint 0 hits, 4627 labels; after:
`python3 lint.py --chapters` 0 hits, 4663 labels (36 new, none duplicated); `python3 assemble.py --check` 0 problems;
the assembled PAPER.md has no line over 121 characters (the new region, assembled lines 74531-75545, has maximum 121),
`python3 lint.py --paper` 0 hits, and no wrapped line in the new region starts with "+ ", "- ", "* ", "> ", "#", "=" or
"|". In the proof file itself: maximum line 121, no such wrapped line, all 36 labels lowercase, and every crosswalk row's
line number is the line of its label.

---------------------------------------------------------------------------------------------------------------------

## D. Literature

- **[Ren90]**: A. D. Rendall, *Reduction of the characteristic initial value problem to the Cauchy problem and its
  applications to the Einstein equations*, Proc. Roy. Soc. London Ser. A 427 (1990), no. 1872, 221–239,
  doi:10.1098/rspa.1990.0009 — confirmed (Semantic Scholar record with the DOI, volume 427, pages 221–239; zbMATH
  0701.35149 via MaRDI and the reference lists of arXiv:1107.0898 and arXiv:1203.4534 give no. 1872). The abstract's
  first sentence is "A method is described by means of which the characteristic initial value problem can be reduced to
  the Cauchy problem and examples are given of how it can be used in practice"; the quoted part matches word for word
  (nit 16), and the abstract is on p. 221. Alphabetical place after [Rac16] and before [RS1] is right, and the entry's
  format matches the list.
- **[LR20, Theorem 4.6, p. 29]** (arXiv:2009.08968v1): the running head "HIGH-FREQUENCY LIMITS AND NULL DUST SHELLS 29"
  precedes Theorem 4.6, so the page is right. Source: "Given a strongly angularly regular reduced characteristic initial
  data set (Ω, Φ, γ̂, …) as in Definition 4.5, there exists ϵ > 0 sufficiently small such that whenever u_∗ ∈ (0, I] and
  u̲_∗ ∈ (0, ϵ], there exists a unique angularly regular weak solution to the Einstein–null dust system in the sense of
  Definition 2.37 in the domain [0, u_∗] × [0, u̲_∗] × S² which achieves the prescribed initial data." The quotation in
  rem:loc-cone-scope (iii) matches, with "…" for the hextuple with "as in Definition 4.5" and for "in the sense of
  Definition 2.37" (ϵ printed ε).
- **Appendix A.** [Ren90] is cited for the method only, [LR20] and [CTG23] in remarks only. Within proofs: chapter 81's
  results (cited by label), elementary tools the edition already uses without entries (Gronwall, the divergence theorem
  on Lipschitz domains, Sobolev bounds from sec:class-kato, linear ordinary differential equations, Taylor's formula), and
  one published result without an entry: the homotopy invariance of the degree (minor 5). Major 1's replacement uses
  [[thm:std-sy-extension]], already in Appendix A.

---------------------------------------------------------------------------------------------------------------------

## E. Checked and found correct

- **Frame and equations** (lem:loc-cone-frame, lem:loc-cone-ricci (a)), by hand and by a private sympy computation of the
  Christoffel symbols and Ricci tensor of [[eq:loc-double-null]] for arbitrary ln Ω, ϰ_1, ϰ_2, ϰ_3, b of (u, v, ϑ): every
  entry of the connection table (zero residual), □_g, E(K_i, K_i), E(∂_ϑ, ∂_ϑ), E(L̲, ∂_v), E(L̲, ∂_ϑ) with r̲, E(L̲, L̲),
  and the chapter's Ric(∂_v, ∂_v), Ric(∂_v, ∂_ϑ); also the five intermediate curvature components printed in the proof
  (lines 289-301) and the two summing identities (lines 294, 303-304). The coordinate change ϑ̃ with L̲ϑ̃ = 0 (b̃ = −w/J,
  L̲J = J∂_ϑb, L̲b̃ = −J⁻¹∂_vb) is right.
- **lem:loc-cone-ricci (b), (c)**: √|det g| = 2Ω²𝒱, both dust divergences, tr_g T = 0; the trace and every a-, β-, c-term
  of [[eq:loc-cone-bianchi]] recomputed from the connection table (including the β-coefficient
  2η − 2ζ + ∂_ϑ(ϰ_2 + ϰ_3 − ϰ_1) and 2γ_ϑ⁻¹ζ = (2Ω²)⁻¹∂_vb).
- **lem:loc-cone-in**: Γ^u_uu, Γ^v_uu, Γ^ϑ_uu at b = 0, the null second fundamental form, Raychaudhuri, the y-equation
  with (ln Ω)′ = 0; the transport equation for ∂_vb on 𝒞_in. Block A's corner compatibility (def (i)).
- **The formal solution**: lem:loc-cone-borel (Steps 1-3, (a), (b), the γ_0 := min(1, size) correction, needed for
  γ_0 ≤ 1 and giving ‖Δ‖ ≤ C·size); (Ψ1)-(Ψ3) read off the verified formulas; the Goursat form; the N_o and N_i
  recursions (linearity in the top jet, order of solution, initial values); vanishing to infinite order; corner
  compatibility by induction on j + k (each factor of the right sides carries at most one u- or one v-derivative, so
  only j′ + k′ ≤ n − 1 enter), including the densities; (ii); the loss of 3 (stated 4) derivatives per order in (iii);
  m_0 − 4(k + 3) = 2(k + 3), so m_0 = 6k + 18 is the least count for ‖Δ‖_(C^(k+3)); the propagation of a, β, c to all
  orders on N_o and N_i through [[eq:loc-cone-bianchi]].
- **The reduced problem**: the chart (τ, y) and ∂_τ; 𝒰 compact in the chart and in the interior of 𝒮; faces spacelike
  for g_e and for every double-null metric; 2C_* e^(τ/2) ≤ η/2; G_* ⊂ F ∩ 𝒰 in case (I) ((u + δ_c)(v + δ_c) ≤ 3c_+/4,
  u + κv ≤ l_u + δ_1/4); [0, σ]² ⊂ F ∩ 𝒰_σ ⊂ [0, 6σ]² and (−2σ, 10σ)² ⊂ 𝒰; Δ = 0 near Σ_init; P̂_out = (2Ω̂²)⁻¹∂_v,
  P̂_in = (2Ω̂²)⁻¹L̲.
- **The reference metric in case (II)**: |b̂| ≤ C_b(|u| + |v|), |b̂| ≤ C_b|v| for u ≥ 2δ_e, constants free of δ_e and δ_c
  (each Borel term bounded by |u| or |v| times a supremum, |χ| ≤ 1, 2ε_j ≤ 1, d_0 = 0); γ̂_ϑb̂²(u + δ_c) ≤
  20γ̂_ϑC_b²δ_1²(v + δ_c) in both regions; 4Ĝ(∂_τ, ∂_τ) ≤ −2Ω̂²(u + δ_c)(v + δ_c) for δ_1 ≤ δ_2; positivity of A^0 at 𝐔̂
  (ω^♯ ⟂ ∂_τ spacelike, dτ timelike, P̂_A(τ) > 0). The writer's identification of this gap and of the reason for b = 0 on
  N_i in T1 is right.
- **The modified system and chapter 81**: 𝔄_χ(Û) = χ𝒜(Û) on supp θ and its residuals ((Aug1) gives E since D(Ĝ) = 0;
  (Aug2) exact; (Aug3) gives −E(P̂_A, P̂_A) by [[eq:class-raychaudhuri]]; (Aug4) the conservation law); smoothness of
  θ1_F𝔄_χ(Û); R_I = O(ε) and R_II = O(σ) in H^k (Taylor's formula and Leibniz); the hypotheses of
  [[thm:class-kato-stability]] (a) (ρ = ∞, s = k > d/2 + 1 = 3, (F1)-(F3), (F1′) via [[rem:class-kato-local]], ū = 0,
  R ∈ C([0, T]; L²) with ‖R‖_(H^s) ≤ 1, smallness in L²), the H^(s′) bound with 1 − s′/s = 1/(4k), the H^k bound via
  [[lem:class-kato-linear]] and [[lem:class-composition]] (b), smoothness via step (4) of [[cor:class-kato-sphere]].
  Chapter 81 never uses the sign of the densities in the results used ([[thm:class-kato]], [[thm:class-kato-stability]],
  [[lem:class-kato-linear]], [[lem:class-composition]], [[rem:class-kato-local]], [[prop:class-augmented]] (b)-(e),
  [[prop:class-structure]] (c), Step 9's first-order form, [[lem:gauge-propagation]]'s identity): the claim of
  def:loc-cone-data and of the report holds. [[cor:class-short-time]] is not used and need not be.
- **lem:loc-cone-energy** and the boundary sign rule (Step 9: ν(∂_τ) ≥ 0, h⁻¹(ν, ν) ≤ 0, ν(P) ≥ 0; convex combinations);
  lem:loc-cone-past (Lipschitz near S_c; du, dv null for Ĝ and g_e with the right signs on the transports; the top face
  in case (II) handled as a slice); lem:loc-cone-support (g_e⁻¹(ν, ν) = R_e⁻² − 2C_*²e^(−2σ_e) < 0, ν(P̊_A) > 0; the set
  {u < u_K, v < v_K}).
- **lem:loc-cone-constraints**: propagation of ν_A and dp_A along past P_A-curves to N; exactness on the simply connected
  𝒰′; the D-Δ system from [[prop:class-augmented]] (d), (e) and its energy on F ∩ 𝒰_σ; Ric(g) = Σ q_A p_A ⊗ p_A; the
  signs (positive factor along P_A, P_A(u_A) = 0, q_in on N_i a positive multiple of its corner value).
- **lem:loc-cone-gauge**: ϑ′ well defined; injectivity from the down-set path bound; the inverse of the (u′, v′, ϑ′)
  block (checked) and −2Ω² = 1/c, γ_ϑ = 1/f, b = e/c; the induced data on N; the C^(k−4) count.
- **lem:loc-cone-extension**: (∗) for any Ω; Borel extension of the free functions at l_v′ with scale 1/4 and the bound
  Λ_2; the Gronwall bound |w′| ≤ (1 + C_1)w and the choice of a_0; positivity of y; the ∂_vb equation's coefficients and
  source orders (C^(p−2), C^(p−3) = C^(m_0)); size ≤ C; p = m_0 + 3 and 2p = 2m_0 + 6 = m_1 = 12k + 42.
- **prop:loc-cone-local**: Steps 1-4 (𝒮 ⊂ translate of Q′ for δ_1 ≤ d; 3δ_1 ≤ a_0 ≤ l′ + a_0; sizes ≤ Λ_1; δ_c, σ := σ_0;
  nonnegativity on the given edges via u_in = v, u_out = u), apart from minor 6. rem:loc-cone-local-scope's change of
  angle: γ_ϑ → γ_ϑ/(∂_ϑΦ)², b → ∂_uΦ + b∂_ϑΦ, zero on N_i and b − b(0, 0, ϑ) on N_o.
- **thm:loc-cone-development**: m = m_0 + 3 = 6k + 21 (y ∈ C^(m−1), b ∈ C^(m−3) = C^(m_0)); δ_* = √c_+/2 with
  2C_0δ_* ≤ η/4; (a), (c), the strips claim; lem:loc-cone-strips (a), (b) (Borel with r = 0, gluing across N), (c)
  (R_v ≥ 0.428 on 𝒞_out; R = 5 − 0.47u ≥ 2.321; R > 1.5 on [5.7, 7.2]).
