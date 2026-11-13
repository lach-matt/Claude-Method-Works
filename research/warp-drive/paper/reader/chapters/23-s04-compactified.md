# Part. The stability theory, II: analysis on the compactified spacetime {#part:stability-analysis}

## The compactified spacetime, its calculi and the standard estimates {#ch:s04}

This chapter sets up the geometry and the microlocal analysis on which the forward problems of the following chapters
rest. It writes out [Hin26c, Sections 2 and 3] in dimension 4 + 1: the compactified spacetime M with its faces ι⁺
(future timelike infinity), ℐ⁺ (null infinity), K⁺ (the Kerr face) and I⁰ (spacelike infinity); its Lie algebras of
b-, 3b-, eb- and e3b-vector fields; the e3b-calculus; the Fourier transform near K⁺ and the Mellin transform at ι⁺;
supported and extendible spaces; functions and operators of finite regularity; and the elliptic and real principal type
estimates on e3b-spaces, with b-regularity and in tame form.

*What changes in dimension 4 + 1.* The spacetime is ℝ^(1+4) and the sphere of directions is 𝕊³, so every construction
of [Hin26c, Section 2] is repeated with 𝕊³ in place of 𝕊², and the proofs do not use the dimension. The dimension enters
through the volume density |dt dx| of the L²-spaces. Near ι⁺, |dt dx| = t_*⟨x⟩⁴ times a b-density, and t_*⁻¹⟨x⟩⁻⁴ is a
smooth positive multiple of x_I⁸ ρ_+⁵ ρ_K. So the weights (2(α_I + 3/2), α_+ + 2, α_K + 1/2) of [Hin26c, (3.57), Lemma
3.14 and Lemma 3.22] become (2(α_I + 2), α_+ + 5/2, α_K + 1/2) ([[lem:ii-a-6-1]], [[lem:ii-a-6-2]] and [[lem:ii-a-8-8]]),
the weight α + 3/2 of [Hin26c, (3.72)] becomes α + 2 ([[eq:ii-a-8-4]]), and the line of the Mellin transform becomes
Im σ = α_+ + 5/2 ([[lem:ii-a-6-2]]). The Sobolev embeddings H^(d+3) ⊂ C^d and H³ ⊂ L^∞ hold on ℝ⁵ as on ℝ⁴ (3 > 5/2),
so no regularity threshold changes.

*Organisation.* [[sec:ii-a-1]] and [[sec:ii-a-2]] construct the compactified spacetime and its Lie algebras of vector
fields, with the commutator lemmas behind b-regularity. [[sec:ii-a-3]] lists the results of the calculus of [Hin26d] that
are used. [[sec:ii-a-4]] sets up the e3b-calculus and its spaces, [[sec:ii-a-5]] and [[sec:ii-a-6]] the Fourier transform
near K⁺ and the Mellin transform at ι⁺, [[sec:ii-a-7]] supported and extendible spaces, and [[sec:ii-a-8]] L^∞-spaces,
operators of limited regularity and Sobolev embedding. [[sec:ii-a1-1]] to [[sec:ii-a1-5]] prove the two standard
estimates without b-regularity, for coefficients of finite regularity and variable orders: the elliptic estimate
([[thm:ii-a1-3-1]]) and the real principal type propagation estimate ([[thm:ii-a1-5-4]]). [[sec:ii-a-9]] derives from
them the estimates with b-regularity and their tame versions.

*Notation.* Variable orders are written in sans-serif letters 𝗌, 𝗆, 𝗅, 𝗋, 𝖻, 𝗄, 𝗍, constant orders in italic; the
sans-serif 𝖧 is not an order but the rescaled Hamilton vector field of [[sec:ii-a1-5-1]]. ℝ̄^N is the
radial compactification of ℝ^N, g̸ the round metric on 𝕊³, and ⟨x⟩ = (1 + |x|²)^(1/2). The bundles of the various
structures are written ᵇT, ³ᵇT, ᵉᵇT, ᵉ³ᵇT, ˢᶜT, and their duals with a star. Constants C may change from line to line.

### Compactifications {#sec:ii-a-1}

Write z = (t, x) ∈ ℝ^(1+4), x = rω, r = |x|, ω ∈ 𝕊³, ρ := r⁻¹, and fix r_0 > 0. In applications r_0 is the radius of
the artificial boundary inside the horizon ([[sec:i-a-1-1]]); nothing in this chapter depends on its value.

*Radial compactification.* For N ≥ 1, ℝ̄^N := (ℝ^N ⊔ [0, ∞)_ϱ × 𝕊^(N−1))/∼, with Z = Rϖ ∼ (ϱ, ϖ) = (R⁻¹, ϖ) for Z ≠ 0
[Hin26c, (2.1)]. A linear isomorphism L of ℝ^N extends to a diffeomorphism of ℝ̄^N: in the coordinates (ϱ, ϖ) near the
boundary, L(ϖ/ϱ) = |Lϖ| ϖ′/ϱ with ϖ′ = Lϖ/|Lϖ|, so L acts by (ϱ, ϖ) ↦ (ϱ/|Lϖ|, Lϖ/|Lϖ|), which is smooth with smooth
inverse since |Lϖ| is bounded above and below on 𝕊^(N−1).

**Definition {#def:ii-a-1-1}** (The spatial manifold; [Hin26c, Definition 2.1] in dimension 4 + 1.) X̃ := ℝ̄⁴ and
X := {r ≥ r_0} ⊂ X̃, with boundary hypersurfaces ∂_♯X := {r = r_0} and ∂X := {ρ = 0}. This is the manifold X̄ of
[[sec:i-a-1-1]].

**Definition {#def:ii-a-1-2}** (Spacetime compactifications; [Hin26c, Definition 2.2].) Let k_± ∈ ∂ℝ̄^(1+4) be the
limit points of (±t, 0) as t → ∞ (in the projective coordinates 1/(±t), x/(±t) near k_±, k_± = {1/(±t) = 0,
x/(±t) = 0}), and let Y⁺ := {1/t = 0, (r − t)/t = 0} ⊂ ∂ℝ̄^(1+4), the light cone at future infinity, a smooth
submanifold diffeomorphic to 𝕊³.

(1) M̃_0 := [ℝ̄^(1+4); k_+, k_−], with boundary hypersurfaces sf (the lift of ∂ℝ̄^(1+4)) and K^± (the lifts of k_±).

(2) M̃_1 := [M̃_0; Y⁺], with boundary hypersurfaces ℐ⁺_1 (the front face), K^±, ι⁺_1 (the closure of {r/t ∈ (0, 1),
1/t = 0}) and I⁰_1 (the closure of {t/r < 1, 1/r = 0}); and M̃ := [M̃_1; ℐ⁺_1, 1/2], the square root blow-up of ℐ⁺_1
(a square root of a defining function of ℐ⁺_1 is declared a defining function of its lift). The boundary hypersurfaces
of M̃ are null infinity ℐ⁺, the Kerr faces K^± (the name is that of [Hin26c]; here they are the faces of the black hole
region), future timelike infinity ι⁺ and spacelike infinity I⁰, with (local) defining functions x_I, ρ_K, ρ_+, ρ_0;
ρ_I := x_I² is a defining function of ℐ⁺_1.

(3) M_0, M_1 and M are the closures of {r ≥ r_0} in M̃_0, M̃_1 and M̃.

**Definition {#def:ii-a-1-3}** (Domains; [Hin26c, Definition 2.3].) Ω̃^♯ := cl_M̃ {t ≥ 0}, Ω^♯ := Ω̃^♯ ∩ M, and
Ω := cl_M {t − r ≥ 1}.

*Coordinates* [Hin26c, (2.8)–(2.12)]. Put t_* := t − r and v := (t − r)/r = ρ t_*.

(A) In M°: (t, x), (t, r, ω) or (t_*, r, ω).

(B) Near the interiors: of K⁺, (1/t, x) or (1/t_*, x); of ι⁺, (v, ρ_+ = 1/t_*, ω) or (v, 1/r, ω); of ℐ⁺,
(t − r, r^(−1/2), ω); of I⁰ ∩ {t ≥ 0}, ((r − t)/r, 1/r, ω).

(C) Near the corners: at I⁰ ∩ ℐ⁺ (where t − r < 2), ρ_0 = 1/(r − t + 2) and x_I = ((r − t + 2)/r)^(1/2); at ℐ⁺ ∩ ι⁺
(where t − r > 0), ρ_+ = 1/(t − r) and x_I = ((t − r)/r)^(1/2) = √v; at ι⁺ ∩ K⁺, ρ_+ = 1/r and ρ_K = r/t; always with
ω ∈ 𝕊³.

These are the projective coordinates of the blow-ups. For instance, near k_+ the functions s := 1/t and y := x/t are
coordinates on ℝ̄^(1+4), with k_+ = {s = 0, y = 0}; on [ℝ̄^(1+4); k_+] the projective coordinates (s, y/s) = (1/t, x)
cover the interior of the front face K⁺, and (|y|, s/|y|, y/|y|) = (r/t, 1/r, ω) cover its corner with sf. Near Y⁺ in
sf°, (1/r, (t − r)/r = v, ω) are coordinates and Y⁺ = {1/r = 0, v = 0}; the projective coordinates of [M̃_0; Y⁺] near
the corner of ℐ⁺_1 with ι⁺_1 are (v, 1/(rv) = 1/(t − r), ω), and the square root blow-up replaces v by x_I = √v. The
other charts are obtained in the same way.

The blow-down map realises ℐ⁺ as the total space of a fibration ℝ̄ → ℐ⁺ → Y⁺ = 𝕊³, the fibres having interiors
{t − r ∈ ℝ, r^(−1/2) = 0, ω = ω_0} [Hin26c, (2.13)].

*Explicit defining functions on Ω* [Hin26c, Remark 2.4]:

    x_I = (t_*/(t_* + r))^(1/2),     ρ_+ = (t_* + r)/(t_* r),     ρ_K = r/(t_* + r).          {#eq:ii-a-defining}

Indeed, on Ω, t_* ∼ ρ_+⁻¹ρ_K⁻¹, r ∼ x_I⁻²ρ_+⁻¹ and t_* + r ∼ x_I⁻²ρ_+⁻¹ρ_K⁻¹ (the quotients being positive and smooth),
and the stated expressions solve these relations.

### Lie algebras of vector fields {#sec:ii-a-2}

This section introduces the Lie algebras of vector fields on the compactifications: the scattering and b-vector fields
([[sec:ii-a-2-1]]), the 3b-vector fields at K⁺ ([[sec:ii-a-2-2]]), the edge-b-vector fields at ℐ⁺ ([[sec:ii-a-2-3]]),
and the e3b-vector fields which combine the two ([[sec:ii-a-2-4]]); then Hamiltonian vector fields
([[sec:ii-a-2-5]]) and the two product structures on which the normal operators are defined ([[sec:ii-a-2-6]]).

#### Scattering and b-structures {#sec:ii-a-2-1}
The scattering tangent bundle ˢᶜTℝ̄^N is ℝ̄^N × ℝ^N, identified with Tℝ^N over ℝ^N by (z, v) ↦ v^μ ∂_(z^μ), and
𝒱_sc(ℝ̄^N) := C^∞(ℝ̄^N; ˢᶜTℝ̄^N). In the projective chart ρ_1 = 1/z¹, ẑ^i = z^i/z¹ (z¹ > 0),
∂_(z¹) = ρ_1(−ρ_1∂_(ρ_1) − Σ_(i≥2) ẑ^i ∂_(ẑ^i)) and ∂_(z^i) = ρ_1 ∂_(ẑ^i); so 𝒱_sc(ℝ̄^N) = ρ𝒱_b(ℝ̄^N), with ρ a
boundary defining function, where 𝒱_b is the space of smooth vector fields tangent to the boundary, spanned by ∂_(z^μ)
and z^μ ∂_(z^ν). On a manifold with corners, 𝒱_b is the space of smooth vector fields tangent to every boundary
hypersurface. The Minkowski metric ḡ = −dt² + dx² lies in C^∞(ℝ̄^(1+4); S² ˢᶜT*ℝ̄^(1+4)). We write 𝒯 → M̃_0, M̃_1, M̃
for the pullback of ˢᶜTℝ̄^(1+4) along the blow-down maps [Hin26c, Definition 2.6]. 𝒱_b(M̃) and 𝒱_sc are Lie algebras,
and Diff^m_b, Diff^m_sc are the spaces of sums of up to m-fold compositions of their elements, with smooth coefficients.
For a boundary hypersurface H with a collar [0, ε)_(ρ_H) × H, the b-normal field ρ_H ∂_(ρ_H) is independent of the collar
modulo ρ_H 𝒱_b.

*Spanning sets* [Hin26c, Example 2.9]. Near (K⁺)° (coordinates ρ_K = 1/t, x): t∂_t = −ρ_K∂_(ρ_K) and ∂_x. Near K⁺ ∩ ι⁺
(ρ_+ = 1/r, ρ_K = r/t): −ρ_+∂_(ρ_+) = t∂_t + r∂_r, −ρ_K∂_(ρ_K) = t∂_t, and ∂_ω. Near ℐ⁺_1 ∩ ι⁺_1 (ρ_+ = 1/(t − r),
ρ_I = (t − r)/r): −ρ_+∂_(ρ_+) = t∂_t + r∂_r, ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+) = (t − r)∂_t, and ∂_ω; one may use
−ρ_I∂_(ρ_I) = r(∂_t + ∂_r) in place of the first. On Ω, r∂_x and t_*∂_(t_*) form a global frame (in the coordinates
(t_*, x)). Each of these follows from the chain rule in the charts of [[sec:ii-a-1]].

#### 3b-structures {#sec:ii-a-2-2}
**Definition {#def:ii-a-2-1}** ([Hin26c, Definition 2.10].) ³ᵇTM̃_0 := M̃_0 × ℝ⁵, identified with Tℝ^(1+4) over
ℝ^(1+4) by (z, v) ↦ v^μ ⟨x⟩ ∂_(z^μ) (over M_0 equivalently v^μ r∂_(z^μ)); 𝒱_3b(M̃_0) is its space of smooth sections, and
Diff^m_3b(M̃_0) the space of sums of up to m-fold compositions of its elements, with smooth coefficients.

The Minkowski metric is

    ḡ = r²(−(dt/r)² + (dr/r)² + g̸) ∈ r² C^∞(M̃_0; S² ³ᵇT*M̃_0),     ḡ⁻¹ = r⁻²(−(r∂_t)² + (r∂_r)² + g̸⁻¹)

[Hin26c, (2.20)]. Near K⁺ ∩ sf, with ρ_K = r/t and ρ_+ = 1/r, r∂_t = −ρ_K²∂_(ρ_K) and r∂_r = ρ_K∂_(ρ_K) − ρ_+∂_(ρ_+).
Hence 𝒱_3b ⊂ 𝒱_b and ρ_K𝒱_b ⊂ 𝒱_3b (as ρ_K t∂_t = r∂_t), and [r∂_r, r∂_t] = r∂_t shows that 𝒱_3b is a Lie algebra. The
map t ↦ −t exchanges K⁺ and K⁻, fixes t∂_t and changes the sign of r∂_t, so near K⁻ all of this holds with
ρ_K := r/|t|; below, ρ_K denotes a defining function of K⁺ ∪ K⁻ of this form near the corners with sf. A
b-vector field V lies in 𝒱_3b if and only if Vt ∈ tρ_K C^∞ near K⁺ ∪ K⁻ (the coefficient of t∂_t must lie in
ρ_K C^∞). Away from K⁺ ∪ K⁻, 3b- and b-vector fields coincide, and ³ᵇTM̃ = ᵇTM̃ over M̃ ∖ (K⁺ ∪ K⁻ ∪ ℐ⁺).
([Hin26c, (2.21)] and the sentence before it state this away from K⁺ ∪ ℐ⁺; near K⁻, ⟨x⟩∂_t degenerates as it does
near K⁺, so K⁻ must be removed too.)

**Lemma {#lem:ii-a-2-2}** (Commutators with time dilations; [Hin26c, Lemma 2.11].) Let V ∈ 𝒱_b(M̃_0) with
V − t∂_t ∈ ρ_K𝒱_b(M̃_0) near K⁺ ∪ K⁻, and let W ∈ 𝒱_3b(M̃_0). Then [V, W] = ρ_K w^♭ V + ρ_K W^♯ with w^♭ ∈ C^∞(M̃_0) and
W^♯ ∈ 𝒱_3b(M̃_0); in particular [V, W] ∈ 𝒱_3b. If W ∈ ρ_sf^(−α_sf) ρ_K^(−α_K) Diff^m_3b(M̃_0), then [V, W] lies in the
same space; and if α_K = 0, then [V, W] = ρ_K W^♭ V + ρ_K W^♯ with W^♭ ∈ ρ_sf^(−α_sf) Diff^(m−1)_3b and
W^♯ ∈ ρ_sf^(−α_sf) Diff^m_3b. The same holds on a smooth vector bundle E, with V ∈ Diff¹_b and
V − ∇_(t∂_t) ∈ ρ_K Diff¹_b for a smooth connection ∇.

([Hin26c, Lemma 2.11] prints W^♯ ∈ Diff^m_3b in the weighted case; its proof gives the weighted class stated here.)

*Proof.* Only the corners K^± ∩ sf need an argument, and K⁻ ∩ sf is K⁺ ∩ sf after t ↦ −t, which fixes t∂_t and maps
3b-vector fields to 3b-vector fields. At K⁺ ∩ sf take ρ_K = r/t, and note that Vf ∈ ρ_K C^∞ for f ∈ C^∞, since
by hypothesis V ≡ −ρ_K∂_(ρ_K) modulo ρ_K𝒱_b, which is t∂_t, and t∂_t f = −ρ_K∂_(ρ_K) f ∈ ρ_K C^∞. If the claim holds for
W, it holds for fW: [V, fW] = f[V, W] + (Vf)W, and (Vf)W ∈ ρ_K𝒱_3b. So it suffices to take W ∈ {r∂_t, r∂_r, ∂_ω}, which
span 𝒱_3b there. For V = t∂_t: [t∂_t, r∂_t] = −r∂_t = −ρ_K t∂_t, [t∂_t, r∂_r] = 0 and [t∂_t, ∂_ω] = 0; this is the
claim with w^♭ ∈ {−1, 0} and W^♯ = 0. In general V = t∂_t + ρ_K(a t∂_t + V′) with a ∈ C^∞ and V′ in the C^∞-span of
r∂_r, ∂_ω (so V′ ∈ 𝒱_3b). Then

    [V, W] = (1 + ρ_K a)[t∂_t, W] − (W(ρ_K a)) t∂_t + [ρ_K V′, W].

The last term lies in ρ_K𝒱_3b, as Wρ_K ∈ ρ_K C^∞ for W ∈ 𝒱_3b ⊂ 𝒱_b (ρ_K being a defining function of a face to which W
is tangent). The middle term is ρ_K f t∂_t with f ∈ C^∞, which equals ρ_K f V modulo ρ_K²𝒱_b ⊂ ρ_K𝒱_3b. The first is
(1 + ρ_K a)(ρ_K w^♭ t∂_t + ρ_K W^♯), and replacing t∂_t by V costs ρ_K²𝒱_b ⊂ ρ_K𝒱_3b.

For operators, write W = wW_0 with w = ρ_sf^(−α_sf) ρ_K^(−α_K) and W_0 ∈ Diff^m_3b. Then [V, W_0] ∈ Diff^m_3b by
expanding W_0 into products of 3b-vector fields, and [V, w] ∈ wC^∞ for every b-vector field V, so
[V, W] = w[V, W_0] + [V, w]W_0 ∈ w Diff^m_3b. If α_K = 0, take ρ_sf = ⟨x⟩⁻¹, and first V = t∂_t; then V commutes with
ρ_sf, so [V, W] = w[V, W_0], and commuting V through each product of 3b-vector fields to the right, using the vector
field case and [V, f] ∈ ρ_K C^∞, gives the form claimed, with W^♭ ∈ w Diff^(m−1)_3b and W^♯ ∈ w Diff^m_3b. For general
V = (1 + ρ_K a)t∂_t + ρ_K V′ as above,

    [V, W] = (1 + ρ_K a)[t∂_t, W] − [W, ρ_K a] t∂_t + [ρ_K V′, W].

Here [W, ρ_K a] ∈ ρ_K w Diff^(m−1)_3b, as 3b-vector fields map ρ_K C^∞ to itself, and
[ρ_K V′, W] = ρ_K[V′, W] − [W, ρ_K]V′ ∈ ρ_K w Diff^m_3b, as 𝒱_3b is a Lie algebra and V′w ∈ wC^∞. Substituting
t∂_t = (1 + ρ_K a)⁻¹(V − ρ_K V′) in the first two terms, with the case V = t∂_t for [t∂_t, W], gives the form claimed.
(The inclusion [ρ_K𝒱_b, w Diff^m_3b] ⊂ ρ_K w Diff^m_3b, on which the proof in [Hin26c] rests, fails: [r∂_t, r∂_r] =
−r∂_t = −ρ_K t∂_t. The argument above does not use it.) For bundles, in a local trivialisation ∇_(t∂_t) is t∂_t
componentwise plus a term in ρ_K C^∞(End E) (as t∂_t = −ρ_K∂_(ρ_K)), whose commutators with w Diff^m_3b lie in
ρ_K w Diff^(m−1)_3b. ∎

The field V in [[lem:ii-a-2-2]] can be taken to be t_*∂_(t_*) in the coordinates (t_*, r), which equals (1 − ρ_K)t∂_t.

**Corollary {#cor:ii-a-2-3}** ([Hin26c, Corollary 2.12].) The 3b-commutator b-vector fields, that is, the
W ∈ 𝒱_b(M̃_0) with [W, V] ∈ 𝒱_3b for all V ∈ 𝒱_3b, span 𝒱_b(M̃_0) over C^∞.

*Proof.* Near K⁺ ∪ K⁻, t∂_t is one by [[lem:ii-a-2-2]], and the ⟨x⟩∂_(z^μ) are trivially ones; their C^∞-span is 𝒱_b
near K^± by the spanning sets of [[sec:ii-a-2-1]] (with t replaced by −t near K⁻). Away from K⁺ ∪ K⁻, 𝒱_3b = 𝒱_b. ∎

#### Edge-b-structures {#sec:ii-a-2-3}
In ρ_+ = 1/t_* and x_I = (t_*/r)^(1/2) near ℐ⁺ ∩ ι⁺ we have t_* = ρ_+⁻¹ and r = ρ_+⁻¹x_I⁻², so

    dt_* = −ρ_+⁻¹ dρ_+/ρ_+,     dr = −ρ_+⁻¹x_I⁻²(dρ_+/ρ_+ + 2 dx_I/x_I),
    ∂_(t_*) = ρ_+(−ρ_+∂_(ρ_+) + (1/2)x_I∂_(x_I)),     ∂_r = −(1/2)ρ_+x_I² · x_I∂_(x_I),

and ḡ = −dt_*² − 2dt_* dr + r²g̸ becomes

    ḡ = 2x_I⁻²ρ_+⁻²(−(dρ_+/ρ_+) ⊗_s [(1 + (1/2)x_I²) dρ_+/ρ_+ + 2 dx_I/x_I] + g̸/(2x_I²)),

as r = ρ_+⁻¹x_I⁻². These are dimension-free calculations, g̸ the round metric on 𝕊³ (they are [Hin26c, (2.26)–(2.27)],
where the angular term in the bracket is printed g̸/x_I²).

**Definition {#def:ii-a-2-4}** ([Hin26c, Definition 2.13].) 𝒱_eb(M̃) is the space of b-vector fields on M̃ tangent to the
fibres of the fibration of ℐ⁺ ([[sec:ii-a-1]]); ᵉᵇTM̃ is the bundle with 𝒱_eb = C^∞(M̃; ᵉᵇTM̃), and Diff^m_eb is defined
as before. A local frame near ℐ⁺ ∩ ι⁺ is ρ_+∂_(ρ_+), x_I∂_(x_I), x_I∂_ω (with ∂_ω the coordinate fields of a chart of
𝕊³), dual to dρ_+/ρ_+, dx_I/x_I, dω/x_I. Thus ḡ ∈ ρ_0⁻²x_I⁻²ρ_+⁻² C^∞(M̃ ∖ (K⁺ ∪ K⁻); S² ᵉᵇT*M̃), and ᵉᵇTM̃ = ᵇTM̃
away from ℐ⁺. ([Hin26c, (2.29)] states this on M̃ ∖ K⁺. Near (K⁻)°, in the coordinates (1/|t|, x), ḡ = −t²(dt/t)² + dx²
has the unbounded coefficient t² while ρ_0, x_I and ρ_+ stay near 1: ḡ grows like t² there, as near K⁺.)

**Lemma {#lem:ii-a-2-5}** ([Hin26c, Lemma 2.14].) Near ℐ⁺ (writing dω for a 1-form on 𝕊³),
ρ_0⁻²x_I⁻²ρ_+⁻² C^∞(M̃; S² ᵉᵇT*M̃) is spanned by x_I⁻²dt_*², dt_* ⊗_s dr, x_I⁻¹dt_* ⊗_s r dω, x_I²dr²,
x_I dr ⊗_s r dω and r dω ⊗_s r dω; and, with x⁰ = t + r and x¹ = t − r, by x_I²(dx⁰)², dx⁰ ⊗_s dx¹,
x_I dx⁰ ⊗_s r dω, x_I⁻²(dx¹)², x_I⁻¹dx¹ ⊗_s r dω and r dω ⊗_s r dω.

*Proof.* By the formulas above, x_I⁻¹dt_*, x_I dr and r dω span ρ_+⁻¹x_I⁻¹ C^∞(U; ᵉᵇT*M̃) on a neighbourhood U of ℐ⁺
away from K⁺ and r = 0, and so do x_I dx⁰, x_I⁻¹dx¹ and r dω: using dx⁰ = dt_* + 2dr,

    x_I dx⁰ = −ρ_+⁻¹x_I⁻¹((2 + x_I²) dρ_+/ρ_+ + 4 dx_I/x_I),     x_I⁻¹dx¹ = −ρ_+⁻¹x_I⁻¹ dρ_+/ρ_+,
    r dω = ρ_+⁻¹x_I⁻¹ · x_I⁻¹dω.

Take symmetric products. Near ℐ⁺ ∩ I⁰ the same calculation applies with ρ_0 in place of ρ_+. ∎

**Lemma {#lem:ii-a-2-6}** ([Hin26c, Lemma 2.15].) Let W ∈ 𝒱_eb(M̃). Near ℐ⁺ ∩ ι⁺, [W, ρ_+∂_(ρ_+)], [W, x_I∂_(x_I)] and
[W, ∂_ω] lie in 𝒱_eb. More generally, if V ∈ 𝒱_b(M̃) is such that, for each ω ∈ 𝕊³, the pushforward to T_ω𝕊³ of V at
the point (t_*, 0, ω) of ℐ⁺ does not depend on t_*, then [V, W] ∈ 𝒱_eb for all W ∈ 𝒱_eb, and [V, W] ∈ Diff^m_eb
(weighted: in the same weighted space) for W ∈ Diff^m_eb.

*Proof.* 𝒱_eb is a Lie algebra containing ρ_+∂_(ρ_+) and x_I∂_(x_I), so only [∂_ω, W] needs proof. It lies in 𝒱_eb for
W = ρ_+∂_(ρ_+), x_I∂_(x_I) and for W = x_I W′ with W′ a vector field on 𝕊³; and [fW, ∂_ω] = f[W, ∂_ω] − (∂_ω f)W. For
the second part, write V = aρ_+∂_(ρ_+) + bx_I∂_(x_I) + c∂_ω with c|_(ℐ⁺) constant on fibres, so Wc ∈ x_I C^∞ for
W ∈ 𝒱_eb (which is tangent to the fibres), and [W, c∂_ω] = (Wc)∂_ω + c[W, ∂_ω] ∈ 𝒱_eb since x_I∂_ω ∈ 𝒱_eb. For
operators expand into products. ∎

**Corollary {#cor:ii-a-2-7}** ([Hin26c, Corollary 2.16].) The eb-commutator b-vector fields 𝒱_(b,[eb])(M̃), that is,
the W ∈ 𝒱_b with [V, W] ∈ 𝒱_eb for all V ∈ 𝒱_eb, span 𝒱_b(M̃) over C^∞.

*Proof.* Near ℐ⁺ the fields of [[lem:ii-a-2-6]] span 𝒱_b; away from ℐ⁺, 𝒱_eb = 𝒱_b. ∎

#### e3b-structures {#sec:ii-a-2-4}
**Definition {#def:ii-a-2-8}** ([Hin26c, Definition 2.17].) ᵉ³ᵇTM̃ is ³ᵇTM̃_0 over M̃ ∖ ℐ⁺ = M̃_0 ∖ Y⁺ and ᵉᵇTM̃ over
M̃ ∖ (K⁺ ∪ K⁻), glued over M̃ ∖ (K⁺ ∪ K⁻ ∪ ℐ⁺) by the identity of Tℝ^(1+4) (which is how both are identified with ᵇT
there). Equivalently, 𝒱_e3b(M̃) is the space of b-vector fields tangent to the fibres of ℐ⁺ with Vt ∈ tρ_K C^∞ near
K⁺ ∪ K⁻.
Diff^m_e3b is defined as before. On Ω, ḡ ∈ ρ_0⁻²x_I⁻²ρ_+⁻² C^∞(Ω; S² ᵉ³ᵇT*M̃) and
ḡ⁻¹ ∈ ρ_0²x_I²ρ_+² C^∞(Ω; S² ᵉ³ᵇTM̃).

**Lemma {#lem:ii-a-2-9}** (Good spanning sets; [Hin26c, Lemma 2.18].) 𝒱_b(M̃) is spanned over C^∞ by the
e3b-commutator b-vector fields 𝒱_(b,[e3b]). More precisely, there is a *good spanning set*: a set
𝒱 = {V_1, …, V_N} ⊂ 𝒱_(b,[e3b]) spanning 𝒱_b, with bounded weights w_j ∈ C^∞(M̃), such that V_(0,j) := w_jV_j ∈ 𝒱_e3b
and {V_(0,j)} spans 𝒱_e3b over C^∞.

*Proof.* The spanning statement combines [[cor:ii-a-2-3]] and [[cor:ii-a-2-7]], the two regions being disjoint up to the
region where both algebras equal 𝒱_b. A good spanning set: finitely many e3b-vector fields spanning 𝒱_e3b (weights 1),
together with χ_K t∂_t = ρ_K⁻¹χ_K r∂_t (w = ρ_K = r/t) and, for a spanning set of vector fields ∂_ω on 𝕊³,
χ_I∂_ω = x_I⁻¹χ_I x_I∂_ω (w = x_I), where χ_K and χ_I localise near K⁺ ∪ K⁻ and ℐ⁺; these are commutator fields by
[[lem:ii-a-2-2]] and [[lem:ii-a-2-6]], and together with the e3b-vector fields they span 𝒱_b. ∎

#### Hamiltonian vector fields {#sec:ii-a-2-5}
For p ∈ C^∞(³ᵇT*M̃_0), writing 3b-covectors near K⁺ ∩ ι⁺ as σ_3b dt_*/r + ξ_3b dr/r + η_3b, η_3b ∈ T*𝕊³, the change of
variables to −σ dt_* + ξ dr + η gives [Hin26c, (2.35)]

    H_p = (∂_(σ_3b)p) r∂_(t_*) + (∂_(ξ_3b)p)(r∂_r + σ_3b∂_(σ_3b)) + (∂_(η_3b)p) ∂_ω
          − (r∂_(t_*)p) ∂_(σ_3b) − ((r∂_r + σ_3b∂_(σ_3b))p) ∂_(ξ_3b) − (∂_ω p) ∂_(η_3b),                   {#eq:ii-a-2-1}

and for p ∈ C^∞(ᵉ³ᵇT*M̃) near ℐ⁺ ∩ ι⁺, with covectors σ_eb dρ_+/ρ_+ + ξ_eb dx_I/x_I + η_eb dω/x_I [Hin26c, (2.38)],

    H_p = (∂_(σ_eb)p) ρ_+∂_(ρ_+) + (∂_(ξ_eb)p)(x_I∂_(x_I) + η_eb∂_(η_eb)) + (∂_(η_eb)p) x_I∂_ω
          − (ρ_+∂_(ρ_+)p) ∂_(σ_eb) − ((x_I∂_(x_I) + η_eb∂_(η_eb))p) ∂_(ξ_eb) − (x_I∂_ω p) ∂_(η_eb).
                                                                                              {#eq:ii-a-2-2}

Both follow by writing the canonical symplectic form in these fibre coordinates; the dimension of 𝕊³ does not enter.
Structurally, the canonical 1-form α is a smooth section of ᵉ³ᵇT*(ᵉ³ᵇT*M̃), so ω = −dα is a smooth e3b-2-form and
H_p ∈ 𝒱_e3b(ᵉ³ᵇT*M̃), with p ↦ H_p a first-order e3b-operator [Hin26c, (2.39)].

#### Product compactifications {#sec:ii-a-2-6}
**Lemma {#lem:ii-a-2-10}** (Slicing by X; [Hin26c, Lemma 2.19].) Let M′_1 := [ℝ̄_(t_*) × X; ∂ℝ̄ × ∂X]. The identity
of ℝ^(1+4) in the coordinates (t_*, r, ω) = (t − r, r, ω) induces a diffeomorphism
M_1 ∩ cl{t ≥ 0} → M′_1 ∩ cl{t_* ≥ −r} identifying K⁺, ι⁺_1, ℐ⁺_1 and I⁰_1 ∩ {t/r ≥ 0} with the lift of {+∞} × X, the
lift of {+∞} × ∂X, the lift of ℝ × ∂X, and the part of the lift of {−∞} × ∂X in {ρ_I ≤ 1}.

*Proof.* Coordinates on M′_1: in the interior (t_*, x); near ∂ℝ̄ × X°, (ρ_K = 1/(±t_*), x), which are also coordinates
near (K⁺)°; near ℝ × ∂X, (t_*, ρ, ω), which are also coordinates near (ℐ⁺_1)°; near the front face over {+∞} × ∂X:
adjacent to {+∞} × X, (ρ, (1/t_*)/ρ = r/(t − r), ω), and r/(t − r) = (r/t)(1 − r/t)⁻¹ matches the coordinates near
ι⁺ ∩ K⁺; adjacent to ℝ × ∂X, (1/t_*, ρt_* = v, ω), the coordinates near ℐ⁺_1 ∩ ι⁺_1; near the front face over
{−∞} × ∂X adjacent to ℝ × ∂X, (ρ_0 = 1/(r − t + 2), ρ_I = (r − t + 2)/r, ω), those near I⁰_1 ∩ ℐ⁺_1, in which {t = 0}
is {ρ_I(1 − 2ρ_0) = 1}. Each chart of one space is thus a chart of the other. ∎

*The T-normal operator* [Hin26c, (2.41)]. For A ∈ Diff^m_3b(M_0), write near K⁺, in t_*, r, ω and the defining
functions ρ_K, ρ_+ = r⁻¹,

    A = Σ_(j+k+|α|≤m) a_(jkα)(ρ_+, ρ_K, ω)(r∂_(t_*))^j (r∂_r)^k ∂_ω^α;

then A_0 := Σ a_(jkα)(r⁻¹, 0, ω)(r∂_(t_*))^j (r∂_r)^k ∂_ω^α is the unique t_*-translation-invariant operator with
χ(A − A_0) ∈ ρ_K Diff^m_3b, χ a collar cut-off of K⁺. (Uniqueness: a translation-invariant operator in ρ_K Diff^m_3b
near K⁺ vanishes, its coefficients being independent of t_* and vanishing as t_* → ∞.)

**Lemma {#lem:ii-a-2-11}** (Slicing by ι⁺; [Hin26c, Lemma 2.20].) ι⁺ = ([0, 2)_(√v) ∪ (1, ∞]_v) × 𝕊³. Let
M′_+ := [ [0, ∞)_τ × ι⁺; {0} × v⁻¹(∞) ]. The map (t, r, ω) ↦ (τ, v, ω), τ = 1/t_*, v = t_*/r, induces a diffeomorphism
M ∩ cl{t_* ≥ 1, r ≥ 1} → M′_+ ∩ cl{τ ≤ 1, τv ≤ 1} identifying ι⁺, K⁺ ∩ {r ≥ 1} and ℐ⁺ ∩ {t_* ≥ 1} with the lift of
{0} × ι⁺, the front face of M′_+ intersected with {τv ≤ 1}, and [0, 1] × v⁻¹(0).

*Proof.* In v < 2, the functions (√v, τ) on M′_+ are (x_I, ρ_+) on M. In v⁻¹ < 2, use (1/v, τ) on [0, ∞) × ι⁺; after
blowing up {τ = 0, 1/v = 0}, the projective coordinates near the corner of the front face with the lift of {0} × ι⁺ are
1/v = r/t_* = (r/t)(1 − r/t)⁻¹ and τ/(1/v) = 1/r, which are coordinates near ι⁺ ∩ K⁺ on M by [[sec:ii-a-1]]. ∎

*The ι⁺-normal operator* [Hin26c, (2.44)]. For A ∈ Diff^m_e3b(M̃) there is a unique dilation-invariant operator A_0 on
(0, ∞)_τ × ι⁺ with χ(A − A_0) ∈ ρ_+ Diff^m_e3b, χ a collar cut-off of ι⁺. Near ι⁺ ∩ ℐ⁺, in x_I = √v, ρ_+ = 1/t_*, ω,
write A = Σ a_(jkα)(x_I, ρ_+, ω)(x_I∂_(x_I))^j (ρ_+∂_(ρ_+))^k (x_I∂_ω)^α and freeze ρ_+ = 0. Near ι⁺ ∩ K⁺, with
R = r/t_* = ρ_K and τ = 1/t_* (so r∂_(t_*) = −R(R∂_R + τ∂_τ) and r∂_r = R∂_R), write
A = Σ a_(jkα)(ρ_+, ρ_K, ω)(Rτ∂_τ)^j (R∂_R)^k ∂_ω^α and freeze ρ_+ = 0. The coordinates used are product coordinates on
[0, ∞)_τ × ι⁺, and Rτ∂_τ, R∂_R, ∂_ω form a local frame of 𝒱_3b near ι⁺ ∩ K⁺.

### The scaled bounded geometry calculus {#sec:ii-a-3}

The pseudodifferential calculus used in this chapter and the following ones is that of [Hin26d] (pseudodifferential
operators on manifolds with scaled bounded geometry; the pages cited are those of its arXiv version 1). We use the
following results of that paper (and, in (S6), one of [Hin26c]), as stated there; they hold on smooth manifolds
of every dimension n. The notation inside the list is that of [Hin26d]. Later chapters cite them as (S1)–(S15).

(S1) [Hin26d, Definition 1.1, p. 2; Definition 1.3 and (1.6), pp. 5–6.] A *b.g. structure* on an n-manifold M without
boundary is a collection ℬ = {(U_α, φ_α)} of charts φ_α : U_α → (−2, 2)^n of finite multiplicity, with
M = ⋃ φ_α⁻¹((−1, 1)^n) and transition maps τ_(βα) = φ_β ∘ φ_α⁻¹ uniformly bounded in C^∞. A *scaled b.g. structure*
ℬ^× = {(U_α, φ_α, ρ_α)} adds scalings ρ_α ∈ (0, 1]^n with |∂^γ(ρ_(α,i) ∂_i τ^j_(βα)(x))| ≤ C_γ ρ_(β,j). Then:
ρ̄_α := max_i ρ_(α,i); the *coefficient Lie algebra* 𝒲 := C^∞_(uni,ℬ)(M; TM) (coefficients uniformly bounded in C^∞ in
the charts); and the *operator Lie algebra* 𝒱 ⊂ 𝒲 of those V with (φ_α)_*V = Σ V^i_α ρ_(α,i) ∂_i, the V^i_α uniformly
bounded in C^∞.

(S2) [Hin26d, Definition 3.4, p. 29; Definition 3.6, p. 30.] A *weight* is a function 0 < w ∈ C^∞(M) with
Ww/w ∈ C^∞_(uni,ℬ) for W ∈ 𝒲; a *scaling weight* ρ is a weight equivalent to {ρ̄_α}.

(S3) [Hin26d, Definition 3.14, p. 34; Definition 3.17, p. 36; Proposition 3.19, p. 37; Theorem 3.21, p. 38;
Proposition 3.22, p. 39.] With χ_α = φ_α^*χ and S_α(x) = (x¹/ρ_(α,1), …, x^n/ρ_(α,n)),
‖u‖²_(wH^s_𝒱(M)) := Σ_α ‖w_α⁻¹(S_α)_*(φ_α)_*(χ_α u)‖²_(H^s(ℝ^n)), and wH^((s;k))_(𝒱;𝒲)(M) is the space of
u ∈ wH^s_𝒱 with W_1⋯W_j u ∈ wH^s_𝒱 for j ≤ k and W_i ∈ 𝒲. Every P ∈ w Diff^m_𝒱 maps w′H^((s;k))_(𝒱;𝒲) to
ww′H^((s−m;k))_(𝒱;𝒲) boundedly. For weights with w/w′ → 0 at infinity and s > s′ (or s ≥ s′ and k ≥ k′, one of them
strictly), the inclusion wH^((s;k))_(𝒱;𝒲) ↪ w′H^((s′;k′))_(𝒱;𝒲) is compact. For a uniformly positive 𝒱-density μ, the
L²(μ) pairing identifies (wH^s_𝒱)* with w⁻¹H^(−s)_𝒱.

(S4) [Hin26d, Definitions 3.7 and 3.8, p. 31; the cut-off ψ and (3.26), p. 43; (3.27)–(3.28) and Definition 3.31,
p. 44; Definition 3.34, p. 46; Definition 3.43, p. 51.] The 𝒱-cotangent bundle ^𝒱T*M has the trivialisations
U_α × ℝ^n ∋ (p, ξ) ↦ Σ ξ_i dx^i_α/ρ_(α,i). S^m(^𝒱T*M) consists of the functions a whose local expressions satisfy
|∂_x^β ∂_ξ^γ a| ≤ C_(βγ)⟨ξ⟩^(m−|γ|) uniformly in α. Fix ψ ∈ C_c^∞((−1/4, 1/4)^n) with ψ = 1 near 0. For a symbol a
on T*ℝ^n with x-support in (−5/4, 5/4)^n, the local quantization has the Schwartz kernel

    Op_α(a)(x, x′) = (2π)^(−n) ∫ exp(i Σ_j (x^j − x′^j)ξ_j/ρ_(α,j)) ψ(x − x′) a(x, ξ) dξ |dx′|/(ρ_(α,1)⋯ρ_(α,n)).

With χ ∈ C_c^∞((−5/4, 5/4)^n) nonnegative and equal to 1 on [−1, 1]^n, and χ_α := φ_α^*χ/Σ_β φ_β^*χ, Op_𝒱(a) := Σ_α φ_α^*
Op_α((φ_α)_*(χ_α a)). The residual operators wρ^∞Ψ^(−∞)_𝒱 are those which, together with their adjoints, map
w′ρ^(−N)H^((−N;k))_(𝒱;𝒲) to ww′ρ^N H^((N;k))_(𝒱;𝒲) for all w′, N and k. Finally wΨ^m_𝒱(M) := {Op_𝒱(a) + R : a ∈ wS^m, R
residual}.

(S5) [Hin26d, Theorem 3.44, p. 51; Remark 3.47, p. 52; Theorem 3.51, p. 55; Theorem 3.52, p. 56; Proposition 3.55,
p. 57.] A ∈ wΨ^m_𝒱 maps w′H^((s;k))_(𝒱;𝒲) to ww′H^((s−m;k))_(𝒱;𝒲) boundedly, with norm bounded by a seminorm of A
(Remark 3.47). The classes wρ^(−l)Ψ^m_𝒱 are closed under adjoints (σ(A*) is the complex conjugate of σ(A)) and
compositions (σ(A_1A_2) = σ(A_1)σ(A_2)); σ(i[A_1, A_2]) = H_(σ(A_1))σ(A_2); WF′(A_1A_2) ⊂ WF′(A_1) ∩ WF′(A_2); and
these operations are continuous. Microlocal elliptic regularity: if B ∈ Ψ⁰_𝒱, A ∈ w′Ψ^(m′)_𝒱 and
WF′(B) ⊂ Ell(A), then ‖Bu‖_(wρ^l H^m) ≤ C_N(‖Au‖_(ww′ρ^l H^(m−m′)) + ‖u‖_(wρ^(−N)H^(−N))). Elliptic operators are
Fredholm when 𝒱 is *fully symbolic*, that is, when for every ε > 0 the scaling weight ρ is smaller than ε outside a
compact subset of M [Hin26d, Definition 3.27, p. 41].

(S6) [Hin26d, Remark 3.33, p. 45]; [Hin26c, Lemma 3.5, p. 49]. The boundedness
Op_𝒱(a) : w′H^((s;k))_(𝒱;𝒲) → ww′H^((s−m;k))_(𝒱;𝒲) requires only uniform bounds ⟨ξ⟩^(m−|γ|) on
(ρ_α∂_x)^β ∂_x^(β′) ∂_ξ^γ a_α for |β′| ≤ k (𝒱-regular symbols with x-derivatives up to order k) [Hin26d, Remark 3.33].
[Hin26c, Lemma 3.5] states: given a compact interval I ⊂ ℝ, there exist d_0 ∈ ℕ and C such that for all s, m ∈ I and
all symbols a of order m with d_0 bounded 𝒱-derivatives, ‖Op_𝒱(a)‖_(ℒ(H^s_𝒱, H^(s−m)_𝒱)) ≤ C‖a‖_(C^(d_0)_𝒱 S^m), and,
for the same d_0 and all k, the same bound between H^((s;k))_(𝒱;𝒲) and H^((s−m;k))_(𝒱;𝒲) with the norm of a in
C^((d_0;k))_(𝒱;𝒲) S^m. Neither statement is used below: the bounds of this kind that the chapter needs are proved in
[[sec:ii-a-8]] and [[sec:ii-a1-2]].

(S7) [Hin26d, Definitions 3.58 and 3.59, p. 59.] For a parameterised scaled b.g. structure (ℬ^(p,×))_(p∈P), with all
bounds uniform in p, the above holds uniformly in p; operators are families with uniformly bounded symbols and residual
parts, bounded uniformly on the p-dependent spaces.

(S8) [Hin26d, Definition 4.6 and the paragraph after it, p. 66; Section 4.2.] Variable orders 𝗆, 𝗅 ∈ S⁰: the symbols
ρ^(−𝗅)λ^(−𝗆)a_0 with a_0 ∈ ⋂_(δ∈(0,1/2)) S⁰_(1−δ,δ), λ being an *elliptic weight*, a positive symbol of order −1 whose
reciprocal is a symbol of order 1 [Hin26d, Lemma 3.24 (2), p. 40]. They are contained in ⋂_δ ρ^(−sup 𝗅) S^(sup
𝗆)_(1−δ,δ), and the corresponding operators and Sobolev spaces (variable decay orders when the scaling weight tends to
0). The paper states that orders are additive under composition and that its Theorem 3.44 "remains valid, mutatis
mutandis, in the variable order case", the principal symbol being taken modulo ⋂_δ ρ^(−𝗅+1−2δ) S^(𝗆−1+2δ). Theorem 3.44
there is the boundedness theorem; the statement concerns composition, and we read it as including the calculus of its
Theorem 3.51. It also states that the operators map H^(𝗆′,𝗅′) to H^(𝗆′−𝗆,𝗅′−𝗅), and that (wH^(𝗆,𝗅)_𝒱)* = w⁻¹H^(−𝗆,−𝗅)_𝒱,
by the proof of its Proposition 4.2; the duality is that of the L²-pairing of a uniformly positive 𝒱-density, as in (S3).
The factor a_0 need not lie in S⁰: its derivatives may carry logarithmic factors, as those of λ^(−𝗆) do.

(S9) [Hin26d, Definition 4.11, p. 68; Definition 4.14, p. 69; Proposition 4.15, p. 70; Proposition 4.17, p. 71;
Proposition 4.18, p. 73; (4.24a)–(4.24b), pp. 73–74.] On M = ℝ_t × X with the product structure built from a scaled
b.g. structure on X and weight families ρ_(α,0) ≤ 1 and τ_α (unit cells ((j − 2)τ_α/ρ_(α,0), (j + 2)τ_α/ρ_(α,0)) × U_α,
scalings (ρ_(α,0), ρ_α)), the Fourier transform in t is an isomorphism

    wH^s_𝒱(ℝ × X) → L²(ℝ_σ; w⟨τσ⟩^(−s) H^s_(𝒱̂_σ)(X)),

with 𝒱̂_σ the operator Lie algebra of the scalings ρ_(α,i)/⟨τ_ασ⟩. The spectral family Â(σ)u = e^(−iσt)A(e^(iσt)u)|_(t=0)
of a translation-invariant A ∈ w Diff^m_𝒱 lies in w⟨τσ⟩^m Diff^m_(𝒱̂) with principal symbol a(σ dt + ·); for
pseudodifferential A, Â(σ) = Op_(𝒱̂_σ)(a|_(σ dt + T*X)) plus a residual family. (The sign convention of [Hin26d, (4.15)]
is e^(−iσt)Ae^(iσt); [Hin26c, (3.17)] and the spectral families of [[ch:s01]] use e^(iσt)Ae^(−iσt), that is, σ ↦ −σ.)
For variable orders 𝗌, 𝗅 invariant under translations in t, the Fourier transform is an isomorphism from
wρ_X^𝗅 H^𝗌_𝒱(ℝ × X) onto the space of L² functions of σ with values in wρ_X^(𝗅̂_σ)⟨τσ⟩^(−𝗌̂_σ) H^(𝗌̂_σ)_(𝒱̂_σ)(X), with
the restricted orders 𝗌̂_σ := 𝗌|_(σ dt + T*X) and 𝗅̂_σ := 𝗅|_(σ dt + T*X); that space is the set of elements of
L²(ℝ_σ; wρ_X^(l_0)⟨τσ⟩^(−s_0) H^(s_0)_(𝒱̂_0)(X)), l_0 ≤ inf 𝗅, s_0 ≤ inf 𝗌, whose image under a fixed elliptic operator
of the spectral class of orders (𝗌̂, 𝗅̂) lies in L²(ℝ_σ; L²(X)) ([Hin26d, (4.24a)–(4.24b)], stated there with the remark
that the proof is that of Proposition 4.18; [Hin26c] cites them as (4.25a–b)). [[sec:ii-a-5]] to [[sec:ii-a-7]] use it in
this form for variable orders.

(S10) [Hin26d, Definition 4.20, p. 74; Proposition 4.22, p. 75.] 𝒲_([𝒱]) is the set of W ∈ 𝒲 with [W, V] ∈ 𝒱 for all
V ∈ 𝒱. If it spans 𝒲 over C^∞_(uni,ℬ), there is a subalgebra Ψ_(𝒱,[ ]) ⊂ Ψ_𝒱, closed under compositions and adjoints
and containing all quantizations Op_𝒱(a), with ad_(W_1)⋯ad_(W_k)A ∈ Ψ_(𝒱,[ ]) for W_i ∈ 𝒲_([𝒱]); likewise with weights
and variable orders. The operators of [Hin26c] are taken in this subalgebra [Hin26c, p. 48], and so are those of this
chapter and the following ones.

(S11) [Hin26d, Proposition 4.2, p. 63.] For phase space weights w, w′, Ψ^w_𝒱 maps H^(w′)_𝒱 to H^(ww′)_𝒱, and
(H^w_𝒱)* = H^(w⁻¹)_𝒱.

(S12) [Hin26d, Proposition 3.2, p. 28.] Two scaled b.g. structures on M have the same operator Lie algebra if and only
if they are compatible, and then they also have the same coefficient and large operator Lie algebras. Since the
calculus and the spaces depend only on these algebras ([Hin26d, pp. 32, 36 and 52]), they do not change when the cells
are replaced by a compatible family (for instance, when a cover of 𝕊³ by charts is replaced by another finite one).

(S13) [Hin26d, p. 28; Proposition 3.3, p. 29; p. 36; Remark 3.48, p. 52.] Subdividing each cell of ℬ^× into cuboids of
side lengths comparable to the scalings (p. 28) gives, for a large enough subdivision constant, a b.g. structure ρℬ, the
*secondary structure*, whose coordinate vector fields span the large operator Lie algebra: 𝒱′ = C^∞_(uni,ρℬ)(M; TM) = 𝒱
⊗_(C^∞_(uni,ℬ)) C^∞_(uni,ρℬ). The Sobolev spaces of the two structures coincide, H^s_(𝒱′) = H^s_𝒱 (p. 36). With all
scalings equal to 1, ρℬ defines a calculus Ψ_(𝒱′), and wΨ^m_𝒱(M) ⊂ wΨ^m_(𝒱′)(M); the residual operators of Ψ_(𝒱′) are
not required to be localised near the diagonal.

(S14) [Hin26d, Remark 3.13, p. 34; (3.8), p. 32; Remark 3.46, p. 52.] On vector bundles of bounded geometry
(trivialisations over the U_α with transition functions uniformly bounded in C^∞), 𝒱-differential operators are those
which, in the charts and trivialisations, are matrices of scalar 𝒱-differential operators of the form (3.8) with
uniformly bounded coefficients; their principal symbols are the matrices of the principal symbols. 𝒱-pseudodifferential
operators on such bundles are the sums of matrices of quantizations of symbols in the local charts and of residual
operators (Remark 3.46).

(S15) [Hin26d, Proposition 2.3 with (2.3) and (2.5), pp. 19–20; Lemma 3.42 and its proof, p. 51; p. 52; proof of
Proposition 4.22, p. 75.] There are a metric d_ℬ on M (written d in Proposition 2.3) and constants δ_0 ∈ (0, 1) and
C ≥ 1 such that C⁻¹d_ℬ(p, q) ≤ |φ_α(p) − φ_α(q)| ≤ Cd_ℬ(p, q) for all α and all p, q ∈ U′_α := φ_α⁻¹((−3/2, 3/2)^n)
(this is (2.3)). The proof defines it by (2.5): d_ℬ(p, q) is the infimum of L(γ, T, I) := Σ_i L(φ_(α_i) ∘ γ|_([t_i,t_(i+1)])) over the
piecewise smooth curves γ : [0, 1] → M from p to q and the tuples T = (t_0, …, t_k), I = (α_0, …, α_(k−1)) with
0 = t_0 < t_1 < ⋯ < t_k = 1 and γ|_([t_i,t_(i+1)]) smooth and contained in U_(α_i), where L(β) is the Euclidean length of
a curve β in (−2, 2)^n. Lemma 3.42 (Off-diagonal behavior of quantizations): "Let ϵ > 0, and let
η ∈ C^∞_(uni,ℬ×ℬ)(M × M) be 1 in the ϵ-neighborhood {(p, q) ∈ M × M : d_ℬ(p, q) < ϵ} of the diagonal in M × M. Let w
be a weight, and let a ∈ wS^m(^𝒱T*M). With Op_𝒱(a) denoting the Schwartz kernel, we then have
(1 − η) Op_𝒱(a) ∈ wρ^∞Ψ^(−∞)_𝒱(M)." Its proof treats the local kernels with the factor
ψ(x′_α − x_α)(1 − η_0(x_α − x′_α)), η_0 ∈ C_c^∞(ℝ^n) equal to 1 near 0, and shows by integration by parts in ξ that
they are quantizations of residual symbols, to which [Hin26d, Proposition 3.39] applies. On p. 52: "by Lemma 3.42, we
may furthermore localize the Schwartz kernels of such local quantizations to a neighborhood |x_α − x′_α| < ϵ for any
fixed α-independent ϵ > 0." In the proof of Proposition 4.22, under the spanning condition of (S10) (p. 75): "the
conclusion in Proposition 3.39 can be strengthened to membership in wρ^∞Ψ^(−∞)_(𝒱,[ ])(M) (which then implies an
analogous strengthening of Lemma 3.42)".

The sharp Gårding inequality is not among these statements and is not used: the real principal type estimate
([[thm:ii-a1-5-4]]) is proved without it.

### The e3b-calculus in dimension 4 + 1 {#sec:ii-a-4}

This section sets up the e3b-calculus as an instance of the calculus of [[sec:ii-a-3]]: its unit cells, its operators
and Sobolev spaces, and operators on bundles.

#### Unit cells {#sec:ii-a-4-1}

The scaled b.g. structure is that of [Hin26c, Section 3.2.1] with ℝ⁴_x and 𝕊³ in place of ℝ³_x and 𝕊². Its coefficient
and operator Lie algebras are 𝒲 = C^∞_b 𝒱_b(M̃) and 𝒱 = C^∞_b 𝒱_e3b(M̃), where C^∞_b denotes the functions that remain
bounded under any finite number of b-vector fields (conormal functions). On Ω ∩ M° there are four families of cells,
which are compatible on their overlaps: each family's charts are related to the others' by coordinate changes that are
uniformly bounded together with the scalings, as one checks from the expressions of the spanning fields below.

(1) Near K⁺: U_(1,i) := (2^(i−2) − 1, 2^(i+2) − 1)_t × (−2, 2)⁴_x, with scalings ρ_t = 2^(−i) and ρ_(x^q) = 1; and, for
j ∈ {1, …, 4}, a sign ±, k ∈ ℕ_0, i ≥ k + 10 and l ∈ ℤ³ with |l| ≤ 2,

    U_(1,i,±jkl) := {2^(i−2) − 1 < t < 2^(i+2) − 1,  ±x^j ∈ (2^(k−2), 2^(k+2)),  x̂_j/x^j ∈ (−2, 2)³ + l}

(x̂_j the other three coordinates), with scalings ρ_t = 2^(k−i) and ρ_(x^q) = 1. In U_(1,i), 𝒲 and 𝒱 are spanned by
⟨t⟩∂_t, ∂_x and by ∂_(t_*), ∂_x respectively; in U_(1,i,±jkl) by t_*∂_(t_*), r∂_x and by r∂_(t_*), r∂_x respectively.

(2) Near ι⁺ ∩ {ρ_K ≤ 3}, with τ = 1/t_* and ρ_K = r/t_*, and the eight chart domains
𝕊³_(k±) := {ω ∈ 𝕊³ : ±ω_k > 1/4}, k = 1, …, 4, each a graph over the other three coordinates (they cover 𝕊³, as
max_k |ω_k| ≥ 1/2; any finite cover by charts gives an equivalent structure, (S12)):

    U_(2,ijk±) := (2^(−i−2), 2^(−i+2))_τ × (2^(−j−2), 2^(−j+2))_(ρ_K) × 𝕊³_(k±),     i ≥ j,

with scalings ρ_τ = 2^(−j) and ρ_(ρ_K) = ρ_ω = 1; 𝒱 is spanned by ρ_Kτ∂_τ, ρ_K∂_(ρ_K), ∂_ω (equivalently r∂_(t_*), r∂_r,
∂_ω), and 𝒲 by τ∂_τ, ρ_K∂_(ρ_K), ∂_ω.

(3) Near ι⁺ ∩ {x_I ≤ 3}, with x_I = (t_*/r)^(1/2):

    U_(3,ijk±) := (2^(−i−2), 2^(−i+2))_τ × (2^(−j−2), 2^(−j+2))_(x_I) × 𝕊³_(k±),

with scalings ρ_τ = ρ_(x_I) = 1 and ρ_ω = 2^(−j); 𝒱 is spanned by τ∂_τ, x_I∂_(x_I), x_I∂_ω, and 𝒲 by the b-vector
fields.

(4) One cell covering the remaining compact part of Ω ∩ M°; and analogous families for t_* ≤ 1.

#### Operators and spaces {#sec:ii-a-4-2}

With these cells, the calculus of [[sec:ii-a-3]] gives [Hin26c, (3.23)–(3.24)] the weighted e3b-pseudodifferential
operators

    C^∞_b Ψ^(𝗌,(2α_I,α_+,α_K))_e3b(M̃) = x_I^(−2α_I) ρ_+^(−α_+) ρ_K^(−α_K) Ψ^𝗌_e3b(M̃),     𝗌 ∈ C^∞(ᵉ³ᵇS*M̃),

which contain C^∞_b Diff^m_e3b; the spaces

    H^(𝗌,(2α_I,α_+,α_K))_e3b = x_I^(2α_I) ρ_+^(α_+) ρ_K^(α_K) H^𝗌_e3b(M̃, |dt dx|);

and H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b), with k b-derivatives (the spaces H^((s;k))_(𝒱;𝒲) of (S3)). The microlocalisation
locus is ᵉ³ᵇS*M̃. The density |dt dx| is a uniformly positive 𝒱-density times a weight, so (S3) applies with that weight
absorbed. The operators are taken in the subalgebra Ψ_(𝒱,[ ]) of (S10), which is possible because
𝒲_([𝒱]) ⊃ 𝒱_(b,[e3b]) spans 𝒲 ([[lem:ii-a-2-9]]). Hence, by (S10),

    A ∈ C^∞_b Ψ^𝗌_e3b,  V ∈ 𝒱_(b,[e3b])   ⟹   [V, A] ∈ C^∞_b Ψ^𝗌_e3b,   WF′_e3b([V, A]) ⊂ WF′_e3b(A).  {#eq:ii-a-4-1}

(The wave front set inclusion holds because, if A is microlocally residual near a point, so is [V, A], by (S10)
applied to the localised operator.)

**Lemma {#lem:ii-a-4-1}** ([Hin26c, Lemma 3.6].) Let V_1, …, V_N ∈ 𝒱_b(M̃) and let w_j ∈ C^∞(M̃) be bounded, with
V_(0,j) := w_jV_j ∈ 𝒱_e3b spanning 𝒱_e3b over C^∞, and put V_0 := I. Then every A ∈ C^∞_b Ψ^𝗌_e3b is Σ_(j=0)^N A_jV_j
with A_j ∈ C^∞_b Ψ^(𝗌−1)_e3b. If A is localized near the diagonal ([[sec:ii-a-8-3]]) and ϵ > 0, the A_j may be taken
with kernel ranges at most that of A plus ϵ.

*Proof.* B := Σ_j V_(0,j)^* V_(0,j) ∈ Diff²_e3b is elliptic, so I = QB + R with Q ∈ C^∞_b Ψ^(−2)_e3b and
R ∈ C^∞_b Ψ^(−1)_e3b: take Q := Op(q) with q ∈ S^(−2) equal to σ(B)⁻¹ outside a compact subset of each fibre,
uniformly; then R := I − QB has principal symbol 0 at order 0, so it has order −1 by the principal symbol sequence
(S5). (This is the first step of [[lem:ii-a-8-4]] (b), which does not use the present lemma; a parametrix to this
finite order suffices.) Then A = Σ_j AQV_(0,j)^* w_jV_j + ARV_0, and A_j := AQV_(0,j)^* w_j ∈ C^∞_b Ψ^(𝗌−1)_e3b,
A_0 := AR ∈ C^∞_b Ψ^(𝗌−1)_e3b. For the last statement, truncate Q to range ϵ ([[sec:ii-a-8-3]]; [Hin26d, Lemma 3.42,
p. 51]). This changes Q by a residual operator, which goes into R, and R = I − QB then has kernel range at most ϵ, B
being a differential operator. Kernel supports add under composition, so the kernel ranges of the A_j, j ≥ 1, and of
A_0 = AR are at most that of A plus ϵ. ∎

Passing to the secondary structure (subdividing the cells into ρ-cuboids) gives the larger classes
Ψ̃_e3b = C^∞_e3b Ψ_e3b with e3b-regular coefficients ((S13): Ψ_𝒱 ⊂ Ψ_(𝒱′)), still bounded on the same
spaces.

#### Bundles {#sec:ii-a-4-3}

Operators on the trivial bundle ℂ^N (the bundles of [[sec:i-a-1-2]]) are N × N matrices of scalar operators; all
statements above and below hold for them with matrix-valued symbols, the principal symbols multiplying as matrices
((S14), for differential and for pseudodifferential operators). Where a
scalar principal symbol is needed (commutators lowering the order), it is assumed and said.

### The Fourier transform near K⁺ {#sec:ii-a-5}

This section identifies the 3b-spaces near K⁺ with spaces of their Fourier transforms in t, and the low-energy spaces of
[[ch:s03]] with the spectral spaces of this calculus.

#### The 3b-structure and its spectral side {#sec:ii-a-5-1}

Near K⁺ the secondary structure of [[sec:ii-a-4-1]] has the cells U_i := (i − 2, i + 2)_t × (−2, 2)⁴_x and

    U_(i,±jkl) := {(i − 2)2^k < t < (i + 2)2^k,  ±x^j ∈ (2^(k−2), 2^(k+2)),  x̂_j/x^j ∈ (−2, 2)³ + l},

i ∈ ℤ, k ∈ ℕ_0, l ∈ ℤ³, |l| ≤ 2. These are of the product form (S9) over the b-structure on ℝ⁴ (cells (−2, 2)⁴ and
{±x^j ∈ (2^(k−2), 2^(k+2)), x̂_j/x^j ∈ (−2, 2)³ + l}, scalings 1), with τ_(±jkl) = 2^k ∼ ⟨x⟩ and ρ_0 = 1. Their Lie
algebra is C^∞_3b 𝒱_3b(M̃_0), and the spaces are Ψ̃^(𝗌,(α_sf,α_K))_3b = ρ_sf^(α_sf) ρ_K^(α_K) Ψ̃^𝗌_3b and

    H^(𝗌,(α_sf,α_K))_3b(M̃_0) = ρ_sf^(α_sf) ρ_K^(α_K) H^𝗌_3b(M̃_0, |dt dx|)

[Hin26c, (3.27)], the weights meaning decay.

We use the Fourier transform in t

    û(σ) = ℱu(σ) := ∫ e^(iσt) u dt,

as in [Hin26c] and in [[ch:s01]], where the spectral families are e^(iσt)Ae^(−iσt). (S9) is stated for ∫ e^(−iσt) u dt,
which is û(−σ); so (S9) applies to û after σ ↦ −σ, and the orders it restricts to σ dt + T*X are, for û at σ, those
restricted to −σ dt + T*X. This transform leads to the parameterised scaled b.g. structure on
X̃ = ℝ̄⁴ with the b-cells and the scalings ρ_(σ,α,i) = (1 + |σ|⟨x⟩)⁻¹ [Hin26c, Section 3.2.2], with coefficient Lie
algebra C^∞_b 𝒱_b(X̃) for all σ, and the following operator Lie algebras and spaces.

(1) At σ = 0: C^∞_b 𝒱_b(X̃) (the b-setting).

(2) At fixed σ ≠ 0: C^∞_b 𝒱_sc(X̃).

(3) For ±σ ∈ [0, 1]: the scattering-b-transition algebra C^∞_b 𝒱_(sc-b)(X̃) on
X̃_(sc-b) := [ [0, 1]_ς × X̃; {0} × ∂X̃ ], ς = ±σ, with faces scf, tf and zf, where
𝒱_(sc-b) = {V ∈ ρ_scf 𝒱_b(X̃_(sc-b)) tangent to the level sets of ς}, ρ_scf = (1 + ς⟨x⟩)⁻¹, spanned by ρ_scf⟨x⟩∂_x;
and the spaces H^(𝗌,(𝗋,l,q))_(sc-b,σ) := ρ_scf^𝗋 ρ_tf^l ρ_zf^q H^𝗌_(sc-b,σ) [Hin26c, (3.32)].

(4) For ±σ ∈ [1, ∞): the semiclassical scattering algebra with h = |σ|⁻¹, and the spaces
H^(𝗌,𝗋,𝖻)_(sc,h) = ρ^𝗋 h^𝖻 H^𝗌_(sc,h) [Hin26c, (3.35)], the semiclassical microlocalisation locus being identified with
the compactified scattering cotangent bundle ˢᶜT̄*X̃ [Hin26c, (3.36)].

All L²-spaces use |dx|. With k further b-derivatives (⟨x⟩∂_x) these spaces are H^((𝗌;k),(𝗋,l,q))_((sc-b,σ);b) and
H^((𝗌;k),𝗋,𝖻)_((sc,|σ|⁻¹);b) [Hin26c, (3.40)–(3.41)].

For a t-translation-invariant A_0 ∈ ρ_sf^(−l) Diff^m_3b(M̃_0), written near r = ∞ as
A_0 = Σ a_(jkα)(r⁻¹, 0, ω)(r∂_t)^j (r∂_r)^k ∂_ω^α, the spectral family is
Â_0(σ) = Σ a_(jkα)(r⁻¹, 0, ω)(−iσr)^j (r∂_r)^k ∂_ω^α ([Hin26c, (3.28)], with the convention e^(iσt)A_0e^(−iσt)), and
[Hin26c, (3.37)]

    (Â_0(σ̂|σ|))_(|σ|∈[0,1]) ∈ ρ_scf^(−l−m) ρ_tf^(−l) Diff^m_(sc-b)(ℝ̄⁴),
    (Â_0(iν ± h⁻¹))_(h∈(0,1]) ∈ ρ^(−l−m) h^(−m) Diff^m_(sc,h)(ℝ̄⁴),                                  {#eq:ii-a-5-1}

for |σ̂| = 1 and ν ∈ ℝ. Indeed, each factor −iσr = −iσ̂ · (|σ|r) is ρ_scf⁻¹ρ_tf⁰ times a bounded sc-b-transition
multiplier, and r∂_r, ∂_ω are b-vector fields, which are ρ_scf⁻¹ times sc-b-transition vector fields; the weight
ρ_sf^(−l) = ⟨x⟩^l is ρ_scf^(−l) ρ_tf^(−l), as ⟨x⟩⁻¹ ∼ ρ_scf ρ_tf. Likewise in the semiclassical regime, with h in place
of |σ|⁻¹.

#### Plancherel {#sec:ii-a-5-2}

**Lemma {#lem:ii-a-5-1}** ([Hin26c, Lemma 3.7] in dimension 4 + 1.) Let 𝗌 ∈ C^∞(³ᵇS*M̃_0) be translation-invariant,
let 𝗌_σ be the induced orders ([Hin26c, (3.18)]: the restriction of 𝗌 to −σ dt + T*X̃), and let α_sf ∈ ℝ. For u
supported where the 3b-cells of [[sec:ii-a-5-1]] apply,

    ‖u‖²_(H^(𝗌,(α_sf,0))_3b(M̃_0,|dt dx|))
       ∼ Σ_± ∫_(±[0,1]) ‖û(σ)‖²_(H^(𝗌_σ,(𝗌_σ+α_sf,α_sf,0))_(sc-b,σ)(X̃,|dx|)) dσ
         + Σ_± ∫_(±[1,∞)) ‖û(σ)‖²_(H^(𝗌_σ,𝗌_σ+α_sf,𝗌_σ)_(sc,|σ|⁻¹)(X̃,|dx|)) dσ.

*Proof.* (S9) ([Hin26d, Proposition 4.18], with the variable-order version referred to in [Hin26c] after (3.16)),
applied after σ ↦ −σ ([[sec:ii-a-5-1]]), so that the order at σ is 𝗌 restricted to −σ dt + T*X̃, gives the
isomorphism onto L²(ℝ_σ; ρ_sf^(α_sf)⟨τσ⟩^(−𝗌_σ) H^(𝗌_σ)_(𝒱̂_σ)) with τ ∼ ⟨x⟩, and |dt dx| on one side, |dx|
on the other (the t-factor is unitary). It remains to name the spaces. For |σ| ≤ 1, 𝒱̂_σ is the sc-b-transition
algebra, ⟨τσ⟩⁻¹ ∼ (1 + |σ|⟨x⟩)⁻¹ ∼ ρ_scf and ρ_sf = ⟨x⟩⁻¹ ∼ ρ_scf ρ_tf (with ρ_zf⁰), giving the weights
(𝗌_σ + α_sf, α_sf, 0). For |σ| ≥ 1, 𝒱̂_σ is the semiclassical scattering algebra with h = |σ|⁻¹, and
⟨τσ⟩⁻¹ ∼ h⟨x⟩⁻¹, giving ρ^(𝗌_σ+α_sf) h^(𝗌_σ). The dimension does not enter: both sides use Euclidean densities. ∎

**Lemma {#lem:ii-a-5-2}** ([Hin26c, Lemma 3.9] in dimension 4 + 1.) Let

    H^((𝗌;k))_(3b;b)(M̃_0) := {u ∈ H^𝗌_3b : ∂_t^(j_1)(t∂_t)^(j_2)(⟨x⟩∂_x)^α u ∈ H^𝗌_3b,  j_1 + j_2 + |α| ≤ k}

[Hin26c, (3.39)]. Then

    ‖u‖²_(H^((𝗌;k),(α_sf,0))_(3b;b))
       ∼ Σ_± Σ_(j=0)^k ∫_(±[0,1]) ‖(σ∂_σ)^j û(σ)‖²_(H^((𝗌_σ;k−j),(𝗌_σ+α_sf,α_sf,0))_((sc-b,σ);b)) dσ
         + Σ_± Σ_(j_1+j_2≤k) ∫_(±[1,∞)) ‖σ^(j_1)(σ∂_σ)^(j_2) û(σ)‖²_(H^((𝗌_σ;k−j),𝗌_σ+α_sf,𝗌_σ)_((sc,|σ|⁻¹);b)) dσ,

with j = j_1 + j_2 in the second sum.

*Proof.* Spatial b-derivatives commute with the Fourier transform ℱ. ℱ(∂_t u) = −iσû, ℱ(tu) = −i∂_σû, and
ℱ(t∂_t u) = −∂_σ(σû) = −(1 + σ∂_σ)û. So, for |σ| ≤ 1, ∂_t costs a factor σ, which is bounded, and t∂_t becomes
−(1 + σ∂_σ); for |σ| ≥ 1, ∂_t gives σ^(j_1). Apply [[lem:ii-a-5-1]] to each ∂_t^(j_1)(t∂_t)^(j_2)(⟨x⟩∂_x)^α u, expand
(1 + σ∂_σ)^(j_2), and use that the (𝗌;k)-norms are sums of 𝗌-norms of up to k b-derivatives. The two sides are sums of
equivalent terms, by induction on k. ∎

#### The low-energy norm {#sec:ii-a-5-3}

**Lemma {#lem:ii-a-5-3}** (The norms of [[def:i-c-6-1]]; [Hin26c, (3.46)] in dimension 4 + 1.) Let χ_zf, χ_tf ∈
C^∞(X̃_(sc-b)) equal 1 near zf and tf respectively, and be supported near them. Uniformly in ς = |σ| ∈ (0, ς_1],

    ‖χ_zf u‖_(H^(𝗌,(𝗋,l,q))_(sc-b,σ)) ∼ ς^(−q) ‖χ_zf u‖_(H̄^(𝗌,l−q)_b),
    ‖χ_tf u‖_(H^(𝗌,(𝗋,l,q))_(sc-b,σ)) ∼ ς^(−2−l) ‖S_ς(χ_tf u)‖_(H^(𝗌,(𝗋,q−l))_(sc,b)(tf)),

the latter with the order 𝗋 read on tf ([[sec:i-c-6-1]]); likewise with k b-derivatives. In particular
H^((s;k),(𝗋,l,q))_((sc-b,ς);b), on functions supported in {ρ < ρ_1} or in the interior, is the space ℋ^((s;k),(𝗋,l,q))_ς
of [[def:i-c-6-1]], with uniformly equivalent norms. (In dimension 3 + 1 the power in the second equivalence is
|σ|^(−3/2−l); [Hin26c, (3.46)] prints |σ|^(3/2−l).)

*Proof.* Both norms are defined by sums over cells, (S3). The sc-b-transition cells at ς are the b-cells of ℝ⁴ (at
radius r ∼ 2^k) with scalings (1 + ς2^k)⁻¹. Where ς2^k ≤ 1 (near zf) the scalings lie in [1/2, 1], so the cells are
b-cells up to a uniformly compatible change (S12), and the weight ρ_scf^𝗋 ρ_tf^l ρ_zf^q is there
∼ ρ^(l−q)ς^q (ρ_scf ∼ 1, ρ_tf ∼ ρ + ς ∼ ρ, ρ_zf ∼ ς/ρ): this is the first equivalence. Where ς2^k ≥ 1 the scalings are
∼ (ς2^k)⁻¹ = r̂⁻¹; under S_ς ([[sec:i-c-6-1]]) the cell at r ∼ 2^k goes to the cell at r̂ = ς2^k with scaling r̂⁻¹, a
scattering cell of tf near sctf, and the cells at r̂ ≲ 1 go to b-cells of tf near ztf; the weights become
ρ_sctf^𝗋 ρ_ztf^(q−l) ς^l (ρ_tf ∼ ς there, and ρ_zf/ρ_tf is the ztf weight); and
‖w‖_(L²(|dx|)) = ς^(−2)‖S_ς w‖_(L²(|dx̂|)), as |dx̂| = ς⁴|dx|. The frequencies match as in [[lem:i-c-6-2]] (c). This
gives the second equivalence, with ς^(−2−l). ∎

So the low-energy estimates of [[thm:i-c-6-4]] are estimates on the spaces H^((s;k),(𝗋+α_+,α,0))_((sc-b,|σ|);b) of
[Hin26c, (9.119)] in dimension 4 + 1, which is the form in which they are used at future timelike infinity
([[ch:s08]]).

### The Mellin transform at ι⁺ {#sec:ii-a-6}

This section identifies the e3b-spaces near ι⁺ with spaces of Mellin transforms in τ = 1/t_*.

#### Near a conic end {#sec:ii-a-6-1}

The Mellin transform near ∂ℝ̄⁴ and the normal operator estimate are those of [[sec:i-c-2]] ([[lem:i-c-2-2]] to
[[lem:i-c-2-7]]), with the transform ℳv(λ) = ∫ e^(λt) v dt, t = −log ϱ, for which the line of the b-weight c is
Re λ = c ([[eq:i-c-2-2]]). In the convention (ℳu)(σ) = ∫ ϱ^(iσ) u dϱ/ϱ of [Hin26c], that is λ = −iσ, this line is
Im σ = c.

#### At ι⁺ {#sec:ii-a-6-2}

ι⁺ = ([0, 2)_(x_I) ∪ (1, ∞]_v) × 𝕊³ ([[lem:ii-a-2-11]]) has the cells U_(2,jk±) = (2^(−j−2), 2^(−j+2))_(ρ_K) × 𝕊³_(k±)
(scalings 1) and U_(3,jk±) = (2^(−j−2), 2^(−j+2))_(x_I) × 𝕊³_(k±) (scalings 1 in x_I and 2^(−j) in ω), the spatial parts
of the cells of [[sec:ii-a-4-1]]. The coefficient Lie algebra is C^∞_b 𝒱_b(ι⁺), and the operator Lie algebra is
C^∞_b 𝒱_(b,e)(ι⁺) (the b-vector fields tangent to the fibres of ι⁺ ∩ ℐ⁺). With t = −log_2 τ the cells (2)–(3) of
[[sec:ii-a-4-1]] are of the product form (S9) [Hin26c, (3.49)], so the Fourier transform in t is the Mellin transform
in τ,

    (ℳu)(σ, p) = ∫_0^∞ τ^(iσ) u(τ, p) dτ/τ.

As τ^(iσ) = e^(−i(σ log 2)t), this is (log 2) times the transform ∫ e^(−iσ′t) u dt of (S9) at σ′ = σ log 2; so (S9)
applies to ℳ directly, the order at σ being 𝗌 restricted to −σ dτ/τ + T*ι⁺.

The spectral side is the parameterised structure on (ι⁺)° with scalings (1 + ρ_K|σ|)⁻¹ near K⁺ and ⟨σ⟩⁻¹, x_I⟨σ⟩⁻¹
near ℐ⁺ [Hin26c, Section 3.2.4]. For fixed σ it is the 0,b-structure C^∞_b 𝒱_(0,b)(ι⁺) (0-vector fields x_I∂_(x_I),
x_I∂_ω at ι⁺ ∩ ℐ⁺, b-vector fields at ι⁺ ∩ K⁺), with the spaces H^(𝗌,(2α_I,γ))_(0,b)(ι⁺) = x_I^(2α_I) ρ_K^γ H^𝗌_(0,b).
For ±σ ∈ [1, ∞) and h = |σ|⁻¹ it is the semiclassical 0- and cone structure on
ι⁺_(0ℏ,cℏ) := [ [0, 1)_h × ι⁺; {0} × (ι⁺ ∩ K⁺) ], with faces cf, tf, sf and 0f, and the spaces

    H^(𝗌,(2α_I,α_cf,l,𝖻))_(0ℏ,cℏ) = ρ_0f^(2α_I) ρ_cf^(α_cf) ρ_tf^l ρ_sf^𝖻 H^𝗌_(0ℏ,cℏ)

[Hin26c, (3.50)–(3.56)]; all of them use a b-density μ_b on ι⁺. The spectral family of a dilation-invariant operator
A_0 is [Hin26c, (3.52)], with −iσ in place of ρ_+∂_(ρ_+).

**Lemma {#lem:ii-a-6-1}** (The density in dimension 4 + 1.) Let χ be a cut-off to cl{r ≥ 1, t_* ≥ 1}. On supp χ, the
density |dt dx| is a smooth positive multiple of x_I⁻⁸ρ_+⁻⁵ρ_K⁻¹|dτ/τ| μ_b; so

    H^(0,(2α_I,α_+,α_K))_e3b(M̃, |dt dx|) = H^(0,(2(α_I+2),α_+ + 5/2,α_K + 1/2))_e3b(M̃, |dτ/τ| μ_b)

there.

*Proof.* |dτ/τ| μ_b is a b-density on [0, ∞) × ι⁺, hence on its blow-up, hence ([[lem:ii-a-2-11]]) on M̃ near ι⁺, so
it is a smooth positive multiple of |dt_*/t_* · dx/⟨x⟩⁴|. Thus |dt dx| = |dt_* dx| is t_*⟨x⟩⁴ times it. Near ι⁺ ∩ ℐ⁺,
t_* ∼ ρ_+⁻¹ and r ∼ x_I⁻²ρ_+⁻¹, so t_*⁻¹⟨x⟩⁻⁴ ∼ ρ_+ · x_I⁸ρ_+⁴ = x_I⁸ρ_+⁵; near ι⁺ ∩ K⁺, t_* ∼ ρ_+⁻¹ρ_K⁻¹ and
r ∼ ρ_+⁻¹, so t_*⁻¹⟨x⟩⁻⁴ ∼ ρ_+⁵ρ_K; in the interior of ι⁺ both are ∼ ρ_+⁵. Hence t_*⁻¹⟨x⟩⁻⁴ ∼ x_I⁸ρ_+⁵ρ_K on supp χ.
Taking square roots, L²(|dt dx|) = x_I⁴ρ_+^(5/2)ρ_K^(1/2) L²(|dτ/τ| μ_b). ∎

In dimension 3 + 1 the same calculation gives x_I⁶ρ_+⁴ρ_K, the weights (2(α_I + 3/2), α_+ + 2, α_K + 1/2) of [Hin26c].

**Lemma {#lem:ii-a-6-2}** ([Hin26c, Lemma 3.14] in dimension 4 + 1.) Let χ be as in [[lem:ii-a-6-1]], let
𝗌 ∈ C^∞(ᵉ³ᵇS*M̃) be invariant on supp χ under the dilations (t_*, v, ω) ↦ (νt_*, v, ω), ν ≥ 1, let 𝗌_σ be the induced
orders, and let α_I, α_+, α_K ∈ ℝ and k ∈ ℕ_0. Put β_+ := α_+ + 5/2. Then

    ‖χu‖²_(H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b)(|dt dx|))
       ∼ ∫_(−1)^1 ‖ℳ(χu)(σ + iβ_+)‖²_(H^((𝗌_σ;k),(2(α_I+2),α_K−α_+−2))_(0,b;b)(ι⁺,μ_b)) dσ
         + Σ_± ∫_(±[1,∞)) Σ_(j=0)^k |σ|^(2j) ‖ℳ(χu)(σ + iβ_+)‖²_(H^((𝗌_σ;k−j),𝒲_σ)_((0ℏ,cℏ,|σ|⁻¹);b)(ι⁺,μ_b)) dσ,

where 𝒲_σ := (2(α_I + 2), α_K − α_+ − 2, α_K − α_+ − 2, 𝗌_σ) is the tuple of weights of the semiclassical spaces.
([Hin26c, Lemma 3.14] prints the line, in dimension 3 + 1, as σ − i(α_+ + 2); with the transform ∫ τ^(iσ) u dτ/τ the
Plancherel line of the weight τ^β is Im σ = +β.)

*Proof.* By [[lem:ii-a-6-1]] the left side is the norm with the b-density and the weights
(2(α_I + 2), α_+ + 5/2, α_K + 1/2). Near ι⁺, τ ∼ ρ_+ρ_K ([[lem:ii-a-2-11]]), so
ρ_+^(β_+) ρ_K^(α_K+1/2) = τ^(β_+) ρ_K^(α_K+1/2−β_+) = τ^(β_+) ρ_K^(α_K−α_+−2). With t = −log_2 τ, the factor τ^(β_+) is
e^(−β_+ t log 2), and for u = τ^(β_+) v, (ℳu)(ζ + iβ_+) = ∫ τ^(iζ) τ^(−β_+) u dτ/τ = (ℳv)(ζ), ζ ∈ ℝ. Now apply (S9) to v
(unweighted in t). The b-regularity splits: the b-vector field τ∂_τ = −(log 2)⁻¹∂_t becomes multiplication by −iσ on
the transform side, as ℳ(τ∂_τ u) = −iσ ℳu, which is bounded for |σ| ≤ 1 and gives the factors |σ|^(2j) for |σ| ≥ 1;
the spatial b-vector fields of ι⁺ commute with ℳ and give the k − j b-derivatives of the spectral spaces. (Under the
conjugation by τ^(β_+), τ∂_τ changes by the constant β_+, which is harmless.) The identification of the spectral spaces
with the 0,b- and 0ℏ,cℏ-spaces is by their definition as the spaces of the spectral scaled b.g. structure
[Hin26c, (3.50)–(3.56)], and the weights x_I^(2(α_I+2)) and ρ_K^(α_K−α_+−2) are functions on ι⁺, hence pass through.
For |σ| ≥ 1, the factor ⟨τσ⟩^(−𝗌) of (S9) is ρ_sf^(𝗌_σ), the last index. ∎

*The tf-normal operator at ι⁺* [Hin26c, (3.58)–(3.60)]. Near ι⁺ ∩ K⁺, with ρ̂_K := ρ_K/h, the 0ℏ,cℏ-vector fields
(h/(h + ρ_K))ρ_K∂_(ρ_K) and (h/(h + ρ_K))∂_ω become (1 + ρ̂_K)⁻¹ρ̂_K∂_(ρ̂_K) and (1 + ρ̂_K)⁻¹∂_ω, the b,sc-vector fields
of tf = [0, ∞]_(ρ̂_K) × 𝕊³. Restriction of the coefficients gives N_tf(A) ∈ Diff^(m,(α_c,𝖻))_(b,sc)(tf) for
A ∈ Diff^(m,(2α_I,α_c,0,𝖻))_(0ℏ,cℏ), and for χ_tf supported near tf,

    ‖χ_tf u‖_(H^(𝗌,(2α_I,α_cf,l,𝖻))_(0ℏ,cℏ,h)) ∼ h^(−l) ‖χ_tf u‖_(H^(𝗌,(α_cf,𝖻−l))_(b,sc)(tf)),

uniformly. Here no power of h comes from the density: both sides use b-densities, which are invariant under
ρ_K ↦ ρ_K/h, so this statement does not depend on the dimension. The proof is the comparison of cells, as for
[[lem:ii-a-5-3]].

### Supported and extendible spaces {#sec:ii-a-7}

Let (𝒱_σ)_σ be the operator Lie algebra of a parameterised scaled b.g. structure on M (possibly a single σ), and fix a
uniformly positive 𝒱-density for L²_(𝒱_σ).

**Lemma {#lem:ii-a-7-1}** ([Hin26c, Lemma 3.15]; uniform duality.) Let 𝗌 be a constant or variable order.

(1) The pairing ⟨u, v⟩ extends to H^𝗌_(𝒱_σ) × H^(−𝗌)_(𝒱_σ) with |⟨u, v⟩| ≤ C‖u‖_(H^𝗌)‖v‖_(H^(−𝗌)), C independent
of σ.

(2) c‖u‖_(H^𝗌) ≤ sup_(‖v‖_(H^(−𝗌)) = 1) |⟨u, v⟩| ≤ C‖u‖_(H^𝗌), uniformly in σ. Moreover every bounded linear functional
λ on H^(−𝗌)_(𝒱_σ) is λ(v) = ⟨v, u⟩ for a unique u ∈ H^𝗌_(𝒱_σ), and ‖u‖_(H^𝗌) ≤ C‖λ‖, uniformly in σ.

*Proof.* For 𝗌 = 0 this is the Cauchy–Schwarz inequality and the Riesz representation theorem. In general take an
elliptic A ∈ Ψ^𝗌_𝒱 and a two-sided parametrix to finite order: B ∈ Ψ^(−𝗌)_𝒱 with BA = I − R_1 and AB = I − R_2, where
R_1, R_2 ∈ Ψ^(−J)_𝒱 and J ≥ sup |𝗌|, all uniformly in σ. It is built as in [[lem:ii-a-8-4]] (b), with I in place of B
there, by (S5), (S7) and (S8). That gives B_L A = I − R_1, and the same for A* gives AB_R = I − R′_2. Then B_L − B_R =
B_L R′_2 − R_1 B_R has order −𝗌 − J, so B := B_L satisfies AB = I − R_2 with R_2 of order −J. (A parametrix to finite
order suffices; (S5) does not state a full parametrix.) As J ≥ sup |𝗌|, R_1 maps H^𝗌 and R_1^* maps H^(−𝗌) into L², and
R_2, R_2^* map L² into H^(−𝗌) and H^𝗌 respectively.

(1) For u, v ∈ C_c^∞, ⟨u, v⟩ = ⟨Au, B^*v⟩ + ⟨R_1u, v⟩, and, as v = A^*B^*v + R_1^*v, ⟨R_1u, v⟩ = ⟨AR_1u, B^*v⟩ + ⟨R_1u,
R_1^*v⟩; so ⟨u, v⟩ = ⟨A(I + R_1)u, B^*v⟩ + ⟨R_1u, R_1^*v⟩, each factor bounded into L² from H^𝗌 or H^(−𝗌) respectively.
C_c^∞ is dense in both spaces (the proof of [[lem:ii-a1-2-3]] (a) applies here, as it uses only (S8)), so the pairing
extends, with the bound.

(2) The map j : L² ⊕ L² ∋ (v_0, v_1) ↦ Av_0 + R_2v_1 ∈ H^(−𝗌) is bounded, A having order 𝗌 and R_2 order −J ≤ −sup 𝗌.
For v ∈ H^(−𝗌), the pair (B(I + R_2)v, R_2v) lies in L² ⊕ L², with norm at most C‖v‖_(H^(−𝗌)): B has order −𝗌, and
R_2v ∈ H^(J−𝗌) ⊂ L² as J ≥ sup |𝗌|. (The pair (Bv, v) would not do: v need not lie in L² where 𝗌 > 0.) And
j(B(I + R_2)v, R_2v) = AB(I + R_2)v + R_2²v = (I − R_2)(I + R_2)v + R_2²v = v. Given λ ∈ (H^(−𝗌))*, write
λ ∘ j = ⟨·, u_0⟩ + ⟨·, u_1⟩ (Riesz) with ‖u_0‖ + ‖u_1‖ ≤ C‖λ‖. Then

    λ(v) = ⟨B(I + R_2)v, u_0⟩ + ⟨R_2v, u_1⟩ = ⟨v, u⟩,     u := (I + R_2^*)B^*u_0 + R_2^*u_1,

first for v ∈ C_c^∞ and then by density and (1). Here B^*u_0 ∈ H^𝗌 (B^* has order −𝗌), R_2^* maps H^𝗌 and L² into H^𝗌
(J ≥ sup |𝗌|), so u ∈ H^𝗌 and ‖u‖_(H^𝗌) ≤ C′‖λ‖. u is unique, since ⟨φ, u⟩ = λ(φ) for φ ∈ C_c^∞ fixes u as a
distribution. Finally, for a given u ∈ H^𝗌, apply this to λ := ⟨·, u⟩, whose norm is the supremum in (2) and is at
most C‖u‖_(H^𝗌) by (1): uniqueness gives ‖u‖_(H^𝗌) ≤ C′‖λ‖, which is the lower bound. All constants are uniform
in σ. ∎

**Definition {#def:ii-a-7-2}** ([Hin26c, Definition 3.16].) For Ω ⊂ M open,
Ḣ^𝗌_(𝒱_σ)(Ω̄) := {u ∈ H^𝗌_(𝒱_σ)(M) : supp u ⊂ Ω̄}, and H̄^𝗌_(𝒱_σ)(Ω) := {u|_Ω : u ∈ H^𝗌_(𝒱_σ)(M)} with the quotient
norm, that is, the norm of the minimal extension.

For u ∈ H̄^𝗌(Ω) and v ∈ Ḣ^(−𝗌)(Ω̄) the pairing is defined through an extension ũ ∈ H^𝗌(M) of u, as ⟨ũ, v⟩. It does not
depend on ũ when v ∈ C_c^∞(Ω), since ũ − ũ′ vanishes on Ω; for general v this needs a property of Ω. We say that Ω
has *property (D)* for 𝗌 if C_c^∞(Ω) is dense in Ḣ^(−𝗌)_(𝒱_σ)(Ω̄) for each σ. Then ⟨ũ, v⟩ does not depend on ũ, by
continuity in v. Property (D) fails for some open sets (a domain slit along a hypersurface, whose two sides may carry
different extensions); [[lem:ii-a-7-d]] gives it for the domains used.

**Lemma {#lem:ii-a-7-3}** ([Hin26c, Lemma 3.17].) Let Ω ⊂ M be open, u ∈ H̄^𝗌(Ω) with an extension ũ ∈ H^𝗌(M), and
v ∈ Ḣ^(−𝗌)(Ω̄). All constants below are uniform in σ.

(1) |⟨ũ, v⟩| ≤ C‖ũ‖_(H^𝗌)‖v‖_(H^(−𝗌)); if Ω has property (D) for 𝗌, then |⟨ũ, v⟩| ≤ C‖u‖_(H̄^𝗌(Ω))‖v‖_(H^(−𝗌)).

(2) c‖u‖_(H̄^𝗌(Ω)) ≤ sup_(‖v‖_(Ḣ^(−𝗌)(Ω̄)) = 1) |⟨ũ, v⟩|, for every extension ũ.

(3) Every λ ∈ Ḣ^(−𝗌)(Ω̄)* is λ(v) = ⟨v, ũ⟩ for some ũ ∈ H^𝗌(M) with ‖ũ‖ ≤ C‖λ‖. Every λ ∈ H̄^𝗌(Ω)* is
λ(u) = ⟨ũ, w⟩ for every extension ũ of u, for some w ∈ Ḣ^(−𝗌)(Ω̄) with ‖w‖ ≤ C‖λ‖.

The same holds with 𝗌 and −𝗌, and the roles of the two kinds of spaces, exchanged.

*Proof.* (1) The first bound is [[lem:ii-a-7-1]] (1). Under (D), ⟨ũ, v⟩ is the same for every extension, in particular
for the minimal one, whose norm is ‖u‖_(H̄^𝗌(Ω)). (3) Ḣ^(−𝗌)(Ω̄) is a closed subspace of H^(−𝗌)(M); extend λ by 0 on its
orthogonal complement to λ̃ of the same norm and represent λ̃ by ũ ([[lem:ii-a-7-1]] (2)). For the second statement, λ
composed with the restriction to Ω is a functional on H^𝗌(M) of norm at most ‖λ‖; represent it by w ∈ H^(−𝗌)(M)
([[lem:ii-a-7-1]] (2), with −𝗌 for 𝗌). It vanishes on C_c^∞(M ∖ Ω̄), whose elements restrict to 0 on Ω; so w is supported
in Ω̄. (2) Apply the first part of (3) to λ(v) := ⟨v, ũ⟩, v ∈ Ḣ^(−𝗌)(Ω̄), whose norm is the supremum in (2): there is ũ′
∈ H^𝗌(M) with ⟨v, ũ − ũ′⟩ = 0 for all such v and ‖ũ′‖ ≤ C‖λ‖. Taking v ∈ C_c^∞(Ω) shows ũ′|_Ω = u, so ‖u‖_(H̄^𝗌(Ω)) ≤
‖ũ′‖ ≤ C‖λ‖, the claim. The exchanged case is the same. ∎

**Lemma {#lem:ii-a-7-d}** (Property (D) at a compact boundary.) Let Ω ⊂ M be open, and suppose that ∂Ω is a compact
smooth hypersurface in M. Then Ω has property (D) for every variable order 𝗌.

*Proof.* Fix σ; the property is qualitative. Let v ∈ Ḣ^(−𝗌)(Ω̄), and let ψ, ψ′ ∈ C_c^∞(M) equal 1 near ∂Ω, with
supp ψ′ in the interior of {ψ = 1}.

*Away from ∂Ω.* Let θ be 1 − ψ′ on Ω and 0 on M ∖ Ω; it is smooth, as ψ′ = 1 near ∂Ω, and θ = 1 on the support of
(1 − ψ)v. Multiplication by θ is bounded on H^(−𝗌). Take φ_j ∈ C_c^∞(M) tending to (1 − ψ)v in H^(−𝗌) (C_c^∞ is dense,
by (S8), as in the proof of [[lem:ii-a1-2-3]] (a)). Then θφ_j ∈ C_c^∞(Ω) tends to θ(1 − ψ)v = (1 − ψ)v.

*Near ∂Ω.* Cover a neighbourhood of ∂Ω by finitely many coordinate patches in which Ω = {x_1 > 0} and in which
H^(−𝗌), for distributions supported in the patch, is the variable order Sobolev space of ℝ^n, and write
ψv = Σ_i ψ_iv with ψ_i ∈ C_c^∞ of the patches. Fix ϱ ∈ C_c^∞(ℝ^n) with ∫ϱ = 1 and supp ϱ ⊂ {x_1 ≥ 1}, and put
ϱ_ε(x) := ε^(−n)ϱ(x/ε), ε ∈ (0, 1]. Convolution with ϱ_ε maps a distribution supported in {x_1 ≥ 0} to a smooth
function supported in {x_1 ≥ ε}. It is the Fourier multiplier ϱ̂(εξ). As ϱ̂ ∈ 𝒮 and ε^(|γ|)⟨εξ⟩^(−|γ|) ≤ C⟨ξ⟩^(−|γ|)
for ε ≤ 1, these symbols are bounded in S⁰, so the multipliers are uniformly bounded on H^(−𝗌) (S8). They converge to I
on C_c^∞ in every H^t, as ϱ̂(εξ) → ϱ̂(0) = 1, hence strongly on H^(−𝗌). So ϱ_ε ∗ (ψ_iv), which for small ε lies in
C_c^∞ of the part of the patch in Ω, tends to ψ_iv in H^(−𝗌). ∎

For the domains of the forward problems, the spatial domain {r > r_0} ⊂ X̃ has a compact smooth boundary in the
interior of X̃, so it has property (D) for every order. Pairings of an extendible distribution with an element of
C_c^∞(Ω) need no property of Ω.

**Proposition {#prop:ii-a-7-4}** ([Hin26c, Proposition 3.18].) In the setting of (S9) with Ω ⊂ X open, the Fourier
transform in t is an isomorphism (in the extendible case, for Ω with property (D) for 𝗌 at every σ, for instance Ω
with a compact smooth boundary, [[lem:ii-a-7-d]])

    Ḣ^𝗌_𝒱(ℝ × Ω̄) → L²(ℝ_σ; ⟨τσ⟩^(−𝗌) Ḣ^𝗌_(𝒱̂_σ)(Ω̄))     and     H̄^𝗌_𝒱(ℝ × Ω) → L²(ℝ_σ; ⟨τσ⟩^(−𝗌) H̄^𝗌_(𝒱̂_σ)(Ω)).

*Proof.* The supported case is (S9) restricted to the closed subspace of distributions supported in ℝ × Ω̄, whose
transforms are supported in Ω̄ for each σ. For the extendible case, let ũ be the minimal extension of u. By
[[lem:ii-a-7-3]] (2) (without parameter), the supported case, [[lem:ii-a-7-3]] (1) at each σ (which uses property (D)
of Ω, the transform of ũ at σ being an extension of û(σ) but not the minimal one), and the Cauchy–Schwarz inequality,

    ‖u‖²_(H̄^𝗌) ≤ C sup_(‖v‖_(Ḣ^(−𝗌)) = 1) |∫ ⟨û(σ), v̂(σ)⟩ dσ|² ≤ C′ ‖û‖²_(L²(⟨τσ⟩^(−𝗌) H̄^𝗌_(𝒱̂_σ)));

the converse inequality follows by applying (S9) to the minimal extension. ∎

Hence [[lem:ii-a-5-1]], [[lem:ii-a-5-2]] and [[lem:ii-a-6-2]] hold for supported and extendible distributions. For the
domain Ω of [[def:ii-a-1-3]], H^𝗌_e3b(Ω)^(•,−) denotes the space of restrictions to {r > r_0} of elements of
H^𝗌_e3b(M̃) supported in {t − r ≥ 1}, and H^((𝗌;k))_(e3b;b)(Ω)^(•,−) likewise, with weights [Hin26c, (3.65)]: these are
the spaces of the spacetime domain of forward problems.

### L^∞-spaces, operators of limited regularity, Sobolev embedding {#sec:ii-a-8}

Fix a good spanning set V_1, …, V_N ∈ 𝒱_(b,[e3b])(M̃) with weights w_j ([[lem:ii-a-2-9]]), and put V_(0,j) := w_jV_j and
V_0 := I. For a word J = (j_1, …, j_p) in {1, …, N} write V^J := V_(j_1)⋯V_(j_p) and |J| := p, and likewise
V_0^I := V_(0,i_1)⋯V_(0,i_q). Then Diff^k_b(M̃) is the C^∞(M̃)-span of the V^J with |J| ≤ k, and Diff^d_e3b(M̃) that of
the V_0^I with |I| ≤ d. Write w_((α)) := x_I^(2α_I) ρ_+^(α_+) ρ_K^(α_K) for α = (α_I, α_+, α_K), with the defining
functions of [[sec:ii-a-1]]. For every b-vector field V, V w_((α)) ∈ w_((α)) C^∞(M̃). On the mixed spaces of
[[sec:ii-a-4-2]] we use the norm

    ‖u‖_(H^((𝗌;k))_(e3b;b)) := Σ_(|J|≤k) ‖V^J u‖_(H^𝗌_e3b),                                               {#eq:ii-a-8-1}

which is equivalent to the norm of (S3). Indeed 𝒲 = C^∞_b 𝒱_b is spanned over C^∞_b by the V_j ([[lem:ii-a-2-9]]). A
product of j elements of 𝒲 is a C^∞_b-combination of the V^J with |J| ≤ j, since b-derivatives of C^∞_b-functions are
in C^∞_b. And multiplication by C^∞_b-functions is bounded on H^𝗌_e3b, these functions being symbols of order 0 ((S4),
(S5)). Weights are suppressed in [[sec:ii-a-8-3]], [[sec:ii-a-8-4]] and [[sec:ii-a-9]], as in [Hin26c]. Every
statement there holds on weighted spaces. To see this, apply it to w⁻¹u and to the conjugated operators w⁻¹Aw,
w = w_((α)). These lie in the same classes, with the same principal symbols and wave front sets: w is a weight in the
sense of (S2) ((S5) for the composition w⁻¹ · A · w), and for coefficients w⁻¹aw = a.

#### e3b-continuous functions {#sec:ii-a-8-1}

**Definition {#def:ii-a-8-1}** ([Hin26c, Definition 3.19].) Let d_0 ∈ ℕ_0 and α_I, α_+, α_K ∈ ℝ. Then
C^(d_0,(2α_I,α_+,α_K))_e3b(M̃) is the space of C^(d_0)-functions u on M̃° = ℝ^(1+4) with w_((α))⁻¹Au ∈ L^∞ for all
A ∈ Diff^(d_0)_e3b(M̃). For k ∈ ℕ_0, the space C^((d_0;k),(2α_I,α_+,α_K))_(e3b;b)(M̃) is defined by the same condition
for all products A_1A_2 with A_1 ∈ Diff^k_b and A_2 ∈ Diff^(d_0)_e3b. For d_0 = 0 it is written
C^(k,(2α_I,α_+,α_K))_b(M̃). The norm is

    ‖u‖_(C^((d_0;k),(2α_I,α_+,α_K))_(e3b;b)) := Σ_(|J|≤k, |I|≤d_0) sup |w_((α))⁻¹ V^J V_0^I u|.

This norm dominates sup |w_((α))⁻¹A_1A_2u| for all A_1, A_2 as above. Write A_1 = Σ f_J V^J and A_2 = Σ g_I V_0^I with
f_J, g_I ∈ C^∞(M̃). By the Leibniz rule A_1A_2 is a combination of products V^(J′)V_0^I, |J′| ≤ k, with coefficients
that are b-derivatives of the g_I times the f_J. These are bounded, as M̃ is compact and b-vector fields preserve
C^∞(M̃). The space is a Banach space. On a compact set K ⊂ M̃° the V_(0,j) span the tangent space with smooth
coefficients, and w_((α)) is bounded above and below there, so the norm dominates the C^(d_0)(K)-norm. A Cauchy sequence
therefore converges in C^(d_0)_loc, and the weighted suprema pass to the limit.

**Lemma {#lem:ii-a-8-2}** (a) Replacing A_1A_2 by A_2A_1 in [[def:ii-a-8-1]] gives the same space with an equivalent
norm. (b) For |J| ≤ k, ‖V^J u‖_(C^((d_0;k−|J|),(α))) ≤ C‖u‖_(C^((d_0;k),(α))). (c)
‖uv‖_(C^((d_0;k),(α+β))) ≤ C_k Σ_(j≤k) ‖u‖_(C^((d_0;j),(α))) ‖v‖_(C^((d_0;k−j),(β))). (d) For f ∈ C^∞(M̃),
‖fu‖_(C^((d_0;k),(α))) ≤ C_(f,k)‖u‖_(C^((d_0;k),(α))); and C^((d_0;k),(2δ,δ,δ)) ⊂ C^((d_0;k)) continuously for δ ≥ 0.

*Proof.* (a) Each V_j is an e3b-commutator vector field, so [V_j, V_(0,i)] ∈ 𝒱_e3b = Σ_l C^∞(M̃) V_(0,l). As [V_j, ·]
is a derivation, [V_j, A_2] ∈ Diff^(d_0)_e3b for A_2 ∈ Diff^(d_0)_e3b. Induction on |J| gives V^J A_2 = Σ A_2′ V^(J′)
and A_2 V^J = Σ V^(J′) A_2″, with A_2′, A_2″ ∈ Diff^(d_0)_e3b and |J′| ≤ |J|. The coefficients are smooth on M̃, hence
bounded with bounded derivatives. (b) V^(J″)V_0^I V^J u with |J″| ≤ k − |J| is, by (a), a combination of
V^(J‴)V_0^(I′) u with |J‴| ≤ k and |I′| ≤ d_0. (c) The Leibniz rule: V^J V_0^I(uv) is a sum of products
(V^(J_1)V_0^(I_1)u)(V^(J_2)V_0^(I_2)v) with |J_1| + |J_2| = |J| and |I_1| + |I_2| = |I|, the subwords keeping their
order. (d) The Leibniz rule again, and w_((2δ,δ,δ)) ≤ C for δ ≥ 0. ∎

#### Operators of limited regularity {#sec:ii-a-8-2}

**Definition {#def:ii-a-8-3}** ([Hin26c, Definition 3.20].) For m, 𝗌 and d_0, k ∈ ℕ_0,
C^((d_0;k))_(e3b;b) Diff^m_e3b(M̃), resp. C^((d_0;k))_(e3b;b) Ψ^𝗌_e3b(M̃), is the space of finite sums Σ a_jP_j with
a_j ∈ C^((d_0;k))_(e3b;b) and P_j ∈ Diff^m_e3b, resp. P_j ∈ C^∞_b Ψ^𝗌_e3b; weighted versions are defined likewise. For a
finite set 𝒫 = {P_1, …, P_N}, the C^((d_0;k))_(e3b;b)-span of 𝒫 is written C^((d_0;k))_(e3b;b) 𝒫. A *representation*
of A ∈ C^((d_0;k))_(e3b;b) 𝒫 is a tuple 𝐚 = (a_1, …, a_N) with A = Σ a_jP_j, and we write
‖𝐚‖_((d_0;k)) := max_j ‖a_j‖_(C^((d_0;k))_(e3b;b)). [Hin26c, (3.68)–(3.69)] uses the infimum of ‖𝐚‖_((d_0;k)) over
representations.

Statements below whose constants depend on A only through a bound for ‖𝐚‖_((d_0;k)) hold equally with the infimum
norm. If ‖A′ − A‖ < ε in that norm, then A′ has a representation with ‖𝐚′‖ ≤ ‖A‖ + 2ε. The tame estimates of
[[sec:ii-a-9-3]] bound one quantity by a low norm of the coefficients times a high norm of u, plus a high norm of the
coefficients times a low norm of u. They are stated for a given representation, whose low and high norms both enter.
With the infimum norm, the low and the high norm may be nearly attained by different representations, and the argument
does not combine them. (This is how the tame estimates are used: an operator arrives with its coefficients.)

#### Smooth operators on mixed spaces {#sec:ii-a-8-3}

*Cut-offs.* [Hin26d, Definition 3.34] calls an operator *localized near the diagonal* when its Schwartz kernel is
supported within a finite d_ℬ-distance of the diagonal. Here d_ℬ is the metric of [Hin26d, Proposition 2.3, p. 19]:
d_ℬ(p, q) is the infimum of the lengths L(γ, T, I) of the chains from p to q, that is, of piecewise smooth curves cut
into pieces each of which lies in one chart of ℬ, L being the sum of the Euclidean lengths of the pieces in their charts
[Hin26d, (2.5)]. Being localized near the diagonal is a property an operator of the calculus may or may not have, and
residual operators need not have it [Hin26d, Remark 3.48]. Here the operators of 𝒫 and all auxiliary operators are
taken localized near the diagonal. The *kernel range* of such an operator is the supremum of d_ℬ(p, q) over the
support of its Schwartz kernel. Quantizations are localized near the diagonal, by the cut-off ψ(x − x′) of [Hin26d,
(3.26)] and the chart cut-offs of [Hin26d, Definition 3.31]. Their kernel ranges may be made as small as we please:
[Hin26d, Lemma 3.42, p. 51] states that (1 − η̃)Op_𝒱(a) is residual for a ∈ wS^m whenever η̃ ∈ C^∞_(uni,ℬ×ℬ)(M × M)
equals 1 within d_ℬ-distance ϵ of the diagonal, and its proof shows the same when, in each local quantization,
ψ(x − x′) is replaced by ψ(x − x′)η_0(x − x′) with η_0 ∈ C_c^∞(ℝ^n) equal to 1 near 0 (the form used on p. 52). If
supp η_0 ⊂ {|x| < ϵ/C}, C the constant of [Hin26d, (2.3)], the new kernel has range at most ϵ. We call this
*truncating* the quantization to range ϵ. It changes the operator by a residual one, so it changes no principal symbol,
wave front set or elliptic set, and it commutes with multiplication on the left by functions. For the quantizations Op
of Ψ̃ ([[sec:ii-a-4-2]]) the same holds with ρℬ in place of ℬ: its charts are boxes in those of ℬ, magnified by factors
at least 1, so d_ℬ ≤ d_(ρℬ). The class is closed under compositions and adjoints, since kernel supports add or are
reflected, and under commutators with vector fields, which do not enlarge kernel supports. It contains the finite-order
parametrices of [[lem:ii-a-8-4]] (b), which are quantizations.

Cut-offs are real functions in C^∞(M̃). For such a χ, an operator A is *carried by* χ if A = χ′Aχ′ for some
χ′ ∈ C^∞(M̃) such that χ = 1 within d_ℬ-distance D of supp χ′. Here D bounds the kernel ranges of the finitely many
operators of the statement at hand; for differential operators χ = 1 on supp χ′ suffices. Then Aχ = A = χA, and
AP = APχ for each operator P of the statement. [Hin26c] writes B = χBχ, and its estimates are read with this convention.
[Hin26c, p. 48] does not require the localization near the diagonal.

*Room inside the carriers.* The choices made in the proofs need room, and it is found inside the carriers χ′, not
between χ′ and χ. Let A_1, …, A_r ≠ 0 be the operators of a statement carried by χ, through χ′_1, …, χ′_r, and put
ϑ := Σ_i |χ′_i|² and c := min_i (sup |χ′_i|)^(−2) ≤ 1. As A_i = χ′_iA_iχ′_i, the Schwartz kernel of A_i vanishes where
χ′_i(p)χ′_i(q) ≠ 1, so both base points of its support lie in {ϑ ≥ c}. Hence A_i = ωA_i = A_iω for every ω ∈ C^∞(M̃)
equal to 1 near {ϑ ≥ c}, and WF′(A_i) ⊂ WF′(ω) by (S5): the wave front sets and elliptic sets of the A_i lie over
{ϑ ≥ c}. The coordinate vector fields of the charts of ℬ are uniformly bounded combinations of b-vector fields ((S1),
[[sec:ii-a-4-1]]), so the derivatives of ϑ in these charts are bounded by some Λ_ϑ. Summing over the pieces of a chain
gives |ϑ(p) − ϑ(q)| ≤ Λ_ϑ L(γ, T, I), hence |ϑ(p) − ϑ(q)| ≤ Λ_ϑ d_ℬ(p, q). Put ϵ_ϑ := c/(64Λ_ϑ), and fix f, f̂,
f_* ∈ C^∞(ℝ) with f = 1 on [3c/4, ∞), f = 0 on (−∞, c/2], f̂ = 1 on [c/4, ∞), f̂ = 0 on (−∞, c/8], f_* = 1 on
[c/16, ∞) and f_* = 0 on (−∞, c/32]. Three rules govern the choices.

(R1) *Auxiliary operators* are taken with Schwartz kernels supported in {(p, q) : d_ℬ(p, q) ≤ ϵ_ϑ, max(ϑ(p), ϑ(q)) ≥
c/2}. Such are the quantizations of symbols f(ϑ)ã, ã ∈ C^∞(ᵉ³ᵇT̄*M̃), truncated to range ϵ_ϑ, their adjoints, and their
products with differential operators. As f(ϑ) = 1 near {ϑ ≥ c}, they may be chosen elliptic, or microlocally equal to
I, on any compact subset of ᵉ³ᵇS*M̃ over {ϑ ≥ c}, with wave front sets in any given neighbourhood of it. Both base
points of the kernel of an auxiliary operator or of an A_i lie in {ϑ ≥ c/2 − Λ_ϑϵ_ϑ} ⊂ {ϑ > c/4}, where φ̂ := f̂(ϑ)
equals 1. So every such operator T, and every operator whose kernel lies in the support of the kernel of T (its
commutators with vector fields, for instance), equals φ̂Tφ̂. Let p be at d_ℬ-distance less than
D + 8ϵ_ϑ = D + c/(8Λ_ϑ) from supp φ̂ ⊂ {ϑ ≥ c/8}, and take a chain from a point of supp φ̂ to p of length ℓ below
D + c/(8Λ_ϑ). Cut it where its initial part has length max(0, ℓ − D) < c/(8Λ_ϑ). Along the initial part ϑ stays
positive, and the rest has length at most D. So p is within D of {ϑ > 0} ⊂ ⋃_i supp χ′_i, where χ = 1. Hence these
operators are carried by χ through φ̂, in statements whose operators have kernel ranges up to D + 7ϵ_ϑ.

(R2) *The cut-off χ_*.* Put χ_* := f_*(ϑ). It equals 1 within d_ℬ-distance ϵ_ϑ of supp φ̂, where
ϑ > c/8 − c/64 > c/16, and χ = 1 within D of supp χ_* ⊂ ⋃_i supp χ′_i. So Tχ_* = T for the operators T of (R1);
they are carried by χ_* through φ̂ in statements whose operators have kernel ranges at most ϵ_ϑ; χ_*P = χ_*Pχ for every
P of kernel range at most D; and χ_* is carried by χ, through a function of ϑ equal to 1 on [c/32, ∞) and to 0 on
(−∞, c/64].

(R3) *Inner cut-offs.* Fix h_♭ ∈ C^∞(ℝ) with h_♭ = 0 near 0 and h_♭(1) = 1, and put χ_1 := h_♭(χ), so that
supp χ_1 ⊂ supp χ. As χ_1 = 1 wherever χ = 1, every operator carried by χ is carried by χ_1, through the same function
and for the same D. The function χ_1, and each of its derivatives along b-vector fields, is χ times a function in
C^∞(M̃), the functions h_♭^(j)(s)/s being smooth. For a word V^J in the V_i, the identity fVw = V(fw) − (Vf)w, applied
repeatedly, writes χ_1V^Ju as a sum of terms ±V^(J′)((V^(J″)χ_1)u), with J′ and J″ complementary subwords of J, and
(V^(J″)χ_1)u = h(χu) with h ∈ C^∞(M̃). By [[eq:ii-a-8-1]] and [[lem:ii-a-8-4]] (a) for the multiplication by h,

    ‖χ_1V^Ju‖_(H^((𝗍;q))_(e3b;b)) ≤ C‖χu‖_(H^((𝗍;q+|J|))_(e3b;b))     for all 𝗍, q and J.

So the nested cut-offs of an induction over k levels, χ, h_♭(χ), h_♭(h_♭(χ)), …, need no room at all, and only the
constants depend on k. The auxiliary operators of a proof are those of (R1) for the operators of its statement carried
by χ. When an induction applies the statement at a lower level with χ_1 in place of χ, the rules are applied anew
there, to the operators of that statement.

**Lemma {#lem:ii-a-8-4}** Let A ∈ C^∞_b Ψ^(m′)_e3b, m′ ∈ ℝ, and let 𝗌 be a variable order.

(a) A maps H^((𝗌;k))_(e3b;b) to H^((𝗌−m′;k))_(e3b;b) boundedly for every k. For V ∈ 𝒱_(b,[e3b]),
[V, A] ∈ C^∞_b Ψ^(m′)_e3b with WF′_e3b([V, A]) ⊂ WF′_e3b(A); the iterated commutators ad_(V_(j_1))⋯ad_(V_(j_q))A
likewise.

(b) (Microlocal parametrix.) Let B ∈ C^∞_b Ψ^(m_B)_e3b with WF′_e3b(B) ⊂ Ell_e3b(A), and J ∈ ℕ. Then B = QA + R with
Q ∈ C^∞_b Ψ^(m_B−m′)_e3b and R ∈ C^∞_b Ψ^(m_B−J)_e3b.

(c) In (b), if Aχ = A and Bχ = B (for instance, if both are carried by χ), then for all 𝗌, N and k,

    ‖Bu‖_(H^((𝗌−m_B;k))_(e3b;b)) ≤ C(‖Au‖_(H^((𝗌−m′;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))).

(b) and (c) hold, with the same proof, for A and B in the classes Ψ̃ of [[sec:ii-a-4-2]], (S5) applying to ρℬ ((S13)).

(d) H^((𝗌;k))_(e3b;b) ⊂ H^((𝗌+1;k−1))_(e3b;b) continuously for k ≥ 1; hence H^((𝗌;k))_(e3b;b) ⊂ H^(𝗌+k)_e3b, and
H^(s̄)_b = H^((0;s̄))_(e3b;b) ⊂ H^(s̄)_e3b for s̄ ∈ ℕ_0.

*Proof.* (a) The mapping property is (S5), with (S8) for variable orders. The operators are taken in the subalgebra of
(S10) ([[sec:ii-a-4-2]]), and the V_j lie in 𝒲_([𝒱]). The commutator statement is [[eq:ii-a-4-1]], and the iterated
one follows by induction.

(b) Let a and b be principal symbols of A and B. Choose symbols χ̃_0, …, χ̃_(J−1) ∈ S⁰, each equal to 1 near the support
of the previous one, with χ̃_0 = 1 near WF′_e3b(B), and all supported in a closed subset of Ell_e3b(A) on which
|a| ≥ cλ^(−m′) (λ the elliptic weight of (S8)). Put Q_0 := Op(χ̃_0 b/a) ∈ C^∞_b Ψ^(m_B−m′)_e3b. Then R_1 := B − Q_0A has
principal symbol (1 − χ̃_0)b. This lies in S^(−∞), since χ̃_0 = 1 near the essential support of b. So
R_1 ∈ C^∞_b Ψ^(m_B−1)_e3b by the principal symbol sequence (S5), and WF′_e3b(R_1) ⊂ supp χ̃_0. Inductively, given
R_j ∈ C^∞_b Ψ^(m_B−j)_e3b with wave front set in supp χ̃_(j−1), put Q_j := Op(χ̃_j σ(R_j)/a) and
R_(j+1) := R_j − Q_jA ∈ C^∞_b Ψ^(m_B−j−1)_e3b. Then B = (Σ_(j<J) Q_j)A + R_J. Only finitely many steps are taken, so no
asymptotic summation is needed.

(c) Bu = B(χu) = QAχu + R_Jχu = QAu + R_Jχu, because Aχ = A and Bχ = B. Take J ≥ sup 𝗌 + N and use (a).

(d) By [[lem:ii-a-4-1]] (with (S8) for variable orders), an elliptic Λ ∈ C^∞_b Ψ^(𝗌+1)_e3b is Σ_(l=0)^N Λ_lV_l with
Λ_l ∈ C^∞_b Ψ^𝗌_e3b. Microlocal elliptic regularity (S5), with I in place of B, gives
‖v‖_(H^(𝗌+1)) ≤ C(‖Λv‖_(L²) + ‖v‖_(H^(−N))) ≤ C Σ_l ‖V_lv‖_(H^𝗌). Apply this to v = V^J u, |J| ≤ k − 1, and sum, using
[[eq:ii-a-8-1]]. Iterating gives the second claim. For the third, H^(s̄)_b is by definition the space of u with
V^J u ∈ L² for |J| ≤ s̄. ∎

#### Multiplication and pseudolocality {#sec:ii-a-8-4}

**Lemma {#lem:ii-a-8-5}** (Multiplication and pseudolocality; the part of [Hin26c, Lemma 3.5] that is used, and the
pseudolocality in the proof of [Hin26c, Proposition 3.28].) Let 𝗌 and 𝗌_0 be variable orders.

(a) There are d_0 ∈ ℕ, depending only on 𝗌, and C with ‖ℓu‖_(H^𝗌_e3b) ≤ C‖ℓ‖_(C^(d_0)_e3b)‖u‖_(H^𝗌_e3b) for all
ℓ ∈ C^(d_0)_e3b. Moreover, for every k, ‖ℓu‖_(H^((𝗌;k))_(e3b;b)) ≤ C_k Σ_(j≤k) ‖ℓ‖_(C^((d_0;j))_(e3b;b))
‖u‖_(H^((𝗌;k−j))_(e3b;b)), with the same d_0.

(b) There is d_0 ∈ ℕ, depending only on 𝗌 and 𝗌_0, with the following property. Let B, B^♯ ∈ C^∞_b Ψ⁰_e3b with
WF′_e3b(I − B^♯) ∩ WF′_e3b(B) = ∅. Then there is C, depending on B and B^♯, with
‖Bℓ(I − B^♯)u‖_(H^𝗌_e3b) ≤ C‖ℓ‖_(C^(d_0)_e3b)‖u‖_(H^(𝗌_0)_e3b) for all ℓ ∈ C^(d_0)_e3b.

*Proof.* *Smooth coefficients.* Let C^∞_e3b be the space of functions all of whose e3b-derivatives are bounded. With the
seminorms ‖·‖_(C^d_e3b) it is a Fréchet space. Such a function ℓ is a symbol of order 0, independent of the fibre
variable, for the secondary b.g. structure ρℬ. In its charts the e3b-vector fields are the uniformly bounded
combinations of the coordinate vector fields ((S13)). Its quantization is multiplication by ℓ:
in the local quantization of [Hin26d, (3.26)] the cut-off ψ(x − x′) equals 1 near x = x′, so a fibre-independent symbol
is quantized to multiplication by itself, and the cut-offs χ_α of [Hin26d, Definition 3.31] sum to 1. Hence
multiplication by ℓ lies in Ψ̃⁰_e3b, which is bounded on H^𝗌_e3b ([[sec:ii-a-4-2]], with (S8)). Consider
T : ℓ ↦ (u ↦ ℓu), from C^∞_e3b to ℒ(H^𝗌_e3b). Its graph is closed. Suppose ℓ_n → ℓ in C^∞_e3b and Tℓ_n → T′. For
u ∈ H^𝗌_e3b (a distribution on ℝ^(1+4), locally in H^(inf 𝗌)), ℓ_nu → ℓu in 𝒟′. So T′u = ℓu. By the closed graph
theorem (from a Fréchet space to a Banach space), T is continuous, that is, ‖Tℓ‖ ≤ C‖ℓ‖_(C^(d_*)_e3b) for some d_*.
The map T does not involve any auxiliary operator, so d_* depends only on 𝗌.

*Finite regularity.* Let d_* be the number just found, let K := max(0, ⌈−inf 𝗌⌉), and put d_0 := d_* + K + 1. Let
ℓ ∈ C^(d_0)_e3b. In the charts ψ_β of ρℬ, with a uniformly smooth partition of unity θ_β and a mollifier η_ε, put
ℓ_ε := Σ_β ((θ_βℓ) ∘ ψ_β⁻¹ ∗ η_ε) ∘ ψ_β. Derivatives commute with convolution, the charts have uniformly bounded
transitions and finite multiplicity, and e3b-derivatives are uniformly equivalent to coordinate derivatives in these
charts. Hence ‖ℓ_ε‖_(C^d_e3b) ≤ C‖ℓ‖_(C^d_e3b) for d ≤ d_0, and ℓ_ε ∈ C^∞_e3b. Moreover ℓ_ε → ℓ in C^K on compact sets.
For u ∈ H^𝗌_e3b, ℓ_εu → ℓu in 𝒟′, while ‖ℓ_εu‖_(H^𝗌) ≤ C‖ℓ‖_(C^(d_*)_e3b)‖u‖_(H^𝗌). A subsequence converges weakly in
the Hilbert space H^𝗌_e3b, which embeds continuously in 𝒟′, so its limit is ℓu. The norm is weakly lower
semicontinuous, which gives the first claim of (a). Write d_a(𝗌) for the number d_0 so obtained.

*b-regularity.* By [[eq:ii-a-8-1]] and the Leibniz rule, V^J(ℓu) = Σ (V^(J_1)ℓ)(V^(J_2)u) over splittings of J, and
‖V^(J_1)ℓ‖_(C^(d_0)_e3b) ≤ C‖ℓ‖_(C^((d_0;|J_1|))_(e3b;b)) by [[lem:ii-a-8-2]] (a).

*(b): a commutator expansion.* As a symbol of the secondary structure ρℬ, ℓ is independent of the fibre variable, of
order 0 and index 0, with ‖ℓ‖_((M);0,0) ≤ C‖ℓ‖_(C^M_e3b) for every M ([[def:ii-a1-1-3]]; e3b-derivatives are the
rescaled coordinate derivatives in the charts of ρℬ, as after [[eq:ii-a1-1-2]]), and Op(ℓ) is multiplication by ℓ, as
shown above for smooth ℓ and, for ℓ of finite regularity, by the extension in [[prop:ii-a1-2-4]] (a). WF′(B) and
WF′(I − B^♯) are disjoint compact subsets of ᵉ³ᵇS*M̃, so B and I − B^♯ are microsupported in disjoint closed sets K_1,
K_2 of the compactified bundle ([[sec:ii-a1-1-2]]). Choose y ∈ C^∞(ᵉ³ᵇT̄*M̃) with y = 1 near K_1 and y = 0 near K_2,
and put Y := Op(y) ∈ Ψ̃⁰ ([[lem:ii-a1-1-1]]). Then WF′(B) ∩ WF′(I − Y) = ∅ = WF′(Y) ∩ WF′(I − B^♯), and
R_1 := B(I − Y) and R_2 := Y(I − B^♯) lie in Ψ̃^(−∞) ([[lem:ii-a1-1-2]]; I − Y = Op(1 − y) by [[eq:ii-a1-1-1]]).
For every operator T, with ad_Y T := YT − TY,

    BT(I − B^♯) = B(I − Y)T(I − B^♯) + BTY(I − B^♯) + B(ad_Y T)(I − B^♯),                         {#eq:ii-a-comm-split}

as the right side is B(T − YT + TY + YT − TY)(I − B^♯). Let T_0 be multiplication by ℓ, T_j := ad_Y^j T_0, and
J := max(0, ⌈sup 𝗌 − inf 𝗌_0⌉). Applying [[eq:ii-a-comm-split]] to T_0, T_1, …, T_(J−1) in turn,

    Bℓ(I − B^♯) = Σ_(j=0)^(J−1) (R_1T_j(I − B^♯) + BT_jR_2) + BT_J(I − B^♯).

For j ≥ 1, T_j is the operator ad_(Op(y_1))⋯ad_(Op(y_j))Op(ℓ) at y_1 = ⋯ = y_j = y, an expression in the j + 1 symbols
y_1, …, y_j, ℓ in the sense of [[prop:ii-a1-2-4]] (f). For smooth symbols it has order −j, each commutator with an
operator of order 0 lowering the order by one ((S5)); all its symbols have constant order 0 and index 0. So by
[[prop:ii-a1-2-4]] (f), for every order 𝗍, T_j is bounded from H^𝗍_e3b to H^(𝗍+j)_e3b with norm at most
C‖y‖_((M_j(𝗍));0,0)^j ‖ℓ‖_(C^(M_j(𝗍)+2)_e3b), where M_j(𝗍) is the number that (f) gives for this expression and the order
𝗍: it depends only on j and 𝗍. For j = 0, (a) bounds T_0 on H^𝗍 with the index d_a(𝗍). The terms are bounded as
follows.

(i) R_1T_j(I − B^♯): I − B^♯ is bounded on H^(𝗌_0), T_j is bounded on H^(𝗌_0) (index M_j(𝗌_0), or d_a(𝗌_0) for
j = 0), and R_1 maps H^(𝗌_0) to H^𝗌.

(ii) BT_jR_2: R_2 maps H^(𝗌_0) to H^𝗌, and T_j and B are bounded on H^𝗌 (index M_j(𝗌), or d_a(𝗌) for j = 0).

(iii) BT_J(I − B^♯): T_J maps H^(𝗌_0) to H^(𝗌_0+J) ⊂ H^𝗌, as 𝗌_0 + J ≥ 𝗌 (index M_J(𝗌_0), or d_a(𝗌_0) when J = 0).

Hence (b) holds with

    d_0 := max(d_a(𝗌), d_a(𝗌_0), max_(1≤j≤J) (M_j(𝗌), M_j(𝗌_0)) + 2),

which depends only on 𝗌 and 𝗌_0. B, B^♯ and y enter only the constant, through the norms of B, I − B^♯, R_1 and R_2
and through ‖y‖_((M_j(𝗍));0,0). [[prop:ii-a1-2-4]] is proved in [[sec:ii-a1-2]] without using (b). ∎

[Hin26c] states (a) as a consequence of its Lemma 3.5, whose proof is by inspection of [Hin26d, Proposition 3.32], and
uses (b) in the proof of its Proposition 3.28 for smooth ℓ, applying it to ℓ of finite regularity, with "a finite
seminorm of ℓ" for each pair (B, B^♯). A closed graph argument for a fixed pair gives such a bound with an index that
may depend on the pair. The commutator expansion [[eq:ii-a-comm-split]] makes the auxiliary symbol y an argument of a
fixed multilinear map, so that only constants depend on B and B^♯. This uniformity is what the inductions of
[[sec:ii-a-9]] need: they apply (b), and the results built on it, to new pairs of operators at every order k.

**Lemma {#lem:ii-a-8-6}** (Operators of limited regularity.) Let 𝗌, m and N be given. There is d_0 = d_0(𝗌, m, N) such
that the following holds for every k ∈ ℕ_0, every finite 𝒫 ⊂ C^∞_b Ψ^m_e3b and every A ∈ C^((d_0;k))_(e3b;b) 𝒫 with a
representation 𝐚; d_0 depends neither on k and 𝒫 nor on the operators G, G′ and the cut-off χ in (b):

(a) ‖Au‖_(H^((𝗌−m;k))_(e3b;b)) ≤ C_k‖𝐚‖_((d_0;k))‖u‖_(H^((𝗌;k))_(e3b;b));

(b) if G, G′ ∈ C^∞_b Ψ⁰_e3b, both carried by χ, with WF′_e3b(G) ⊂ Ell_e3b(G′), then

    ‖GAu‖_(H^((𝗌−m;k))_(e3b;b)) ≤ C_k‖𝐚‖_((d_0;k))(‖G′u‖_(H^((𝗌;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))).

*Proof.* (a) [[lem:ii-a-8-5]] (a) at the order 𝗌 − m, and [[lem:ii-a-8-4]] (a) for the P_j.

(b) First k = 0. Choose auxiliary operators G″, G‴ ∈ C^∞_b Ψ⁰_e3b ((R1) of [[sec:ii-a-8-3]], for G and G′), carried by
χ, microlocally equal to I near WF′_e3b(G), with
WF′_e3b(G″) ⊂ Ell_e3b(G′) and WF′_e3b(G‴) ∩ WF′_e3b(I − G″) = ∅. By the support convention, GAu = GAχu. Then

    Ga_jP_jχu = Ga_jP_jG″χu + Ga_j(I − G‴)P_j(I − G″)χu + Ga_jG‴P_j(I − G″)χu.

By [[lem:ii-a-8-5]] (a) and [[lem:ii-a-8-4]] (c), the first term is bounded by
C‖a_j‖_(C^(d_0))(‖G′u‖_(H^𝗌) + ‖χu‖_(H^(−N))). The second is bounded by C‖a_j‖_(C^(d_0))‖χu‖_(H^(−N)), by
[[lem:ii-a-8-5]] (b) with 𝗌_0 = −N − m, applied to the pair (G, G‴). In the third, G‴P_j(I − G″) ∈ C^∞_b Ψ^(−∞)_e3b,
since the wave front sets are disjoint (S5), and multiplication by a_j is bounded on H^(𝗌−m) by [[lem:ii-a-8-5]] (a).
So the case k = 0 holds with d_0 the larger of the numbers of [[lem:ii-a-8-5]] (a) at the order 𝗌 − m and of
[[lem:ii-a-8-5]] (b) at the orders (𝗌 − m, −N − m). Neither depends on G, G′, G″, G‴, 𝒫 or χ.

For k ≥ 1, argue by induction. By [[eq:ii-a-8-1]] it suffices to bound ‖V_iGAu‖_(H^((𝗌−m;k−1))), and

    V_iGa_jP_ju = [V_i, G]a_jP_ju + G(V_ia_j)P_ju + Ga_j[V_i, P_j]u + Ga_jP_jV_iu.

The first three terms are of the form treated at level k − 1: they involve [V_i, G] (wave front set in that of G), or
the coefficients V_ia_j ∈ C^((d_0;k−1)) ([[lem:ii-a-8-2]] (b)), or the finite set 𝒫 ∪ {[V_i, P_j]}. For the last,
choose an auxiliary operator G_♭ ((R1) of [[sec:ii-a-8-3]]) with WF′(G) ⊂ Ell(G_♭) and WF′(G_♭) ⊂ Ell(G′). The level
k − 1 bounds it by C‖𝐚‖(‖G_♭V_iu‖_((𝗌;k−1)) + ‖χ_1V_iu‖_((−N;k−1))), with the inner cut-off χ_1 := h_♭(χ) of (R3),
which carries G, [V_i, G] and G_♭. Next, ‖G_♭V_iu‖_((𝗌;k−1)) ≤ ‖G_♭u‖_((𝗌;k)) + ‖[G_♭, V_i]u‖_((𝗌;k−1)), and both
are bounded by C(‖G′u‖_((𝗌;k)) + ‖χu‖_((−N;k))) ([[lem:ii-a-8-4]] (c)). Finally ‖χ_1V_iu‖_((−N;k−1)) ≤ C‖χu‖_((−N;k)),
by (R3). The step from k − 1 to k applies the statement at k − 1 to the operators [V_i, G] and G_♭, to the cut-off χ_1
and to the finite set 𝒫 ∪ {[V_i, P_j]}, all chosen anew at each k, with the same d_0; this is possible because the d_0 of
the case k = 0 depends on none of them. So d_0 does not depend on k. ∎

#### Sobolev embedding {#sec:ii-a-8-5}

**Lemma {#lem:ii-a-8-7}** ([Hin26c, Lemma 3.21].) Let 𝗌 be a variable e3b-order, s̲ := max(0, ⌈−inf 𝗌⌉), and k ≥ s̲.
Then H^((𝗌;k))_(e3b;b) ⊂ H^(k−s̲)_b, continuously and with weights.

*Proof.* If s̲ = 0 then 𝗌 ≥ 0 and H^((𝗌;k)) ⊂ H^((0;k)) = H^k_b. Otherwise let A_j := V_(0,j)^(s̲), j = 1, …, N. The
symbols ξ ↦ ξ(V_(0,j)) vanish simultaneously only at ξ = 0, as the V_(0,j) span ᵉ³ᵇTM̃. So
Σ_j A_jA_j^* ∈ Diff^(2s̲)_e3b is elliptic, with a parametrix Q ∈ C^∞_b Ψ^(−2s̲)_e3b and Σ A_jA_j^*Q = I − R,
R ∈ C^∞_b Ψ^(−J)_e3b for any fixed J ≥ 0: [[lem:ii-a-8-4]] (b) with I in place of B and J large gives a left
parametrix, Q′Σ_jA_jA_j^* = I − R′, and taking adjoints, Σ_jA_jA_j^* being formally self-adjoint, Q := Q′^* and
R := R′^* give the right one. With B_j := A_j^*Q ∈ C^∞_b Ψ^(−s̲)_e3b,
u = Σ_j A_jB_ju + Ru. Here B_ju ∈ H^((𝗌+s̲;k)) ⊂ H^((0;k)) = H^k_b ([[lem:ii-a-8-4]] (a); 𝗌 + s̲ ≥ 0), and
A_j ∈ Diff^(s̲)_b maps H^k_b to H^(k−s̲)_b. Also Ru ∈ H^((𝗌+J;k)) ⊂ H^k_b for J ≥ s̲. ∎

**Lemma {#lem:ii-a-8-8}** ([Hin26c, Lemma 3.22] in dimension 4 + 1.) Let d ∈ ℕ_0 and α_I, α_+, α_K ∈ ℝ. Then for u
supported in Ω ([[def:ii-a-1-3]]),

    ‖u‖_(C^(d,(2(α_I+2),α_+ + 5/2,α_K + 1/2))_b) ≤ C‖u‖_(H^(d+3,(2α_I,α_+,α_K))_b(M̃;|dt dx|)).            {#eq:ii-a-8-2}

For an unweighted b-density μ_b on M̃ and all γ_I, γ_+, γ_K,
‖u‖_(C^(d,(2γ_I,γ_+,γ_K))_b) ≤ C‖u‖_(H^(d+3,(2γ_I,γ_+,γ_K))_b(M̃,μ_b)), and, for u supported in Ω and every δ > 0,

    ‖u‖_(H^(d,(2γ_I,γ_+,γ_K))_b(M̃,μ_b)) ≤ C_δ‖u‖_(C^(d,(2γ_I+δ,γ_+ + δ,γ_K + δ))_b).                      {#eq:ii-a-8-3}

*Proof.* *The density.* With the explicit defining functions [[eq:ii-a-defining]] on Ω,

    x_I⁸ρ_+⁵ρ_K = (t_*/(t_* + r))⁴ ((t_* + r)/(t_* r))⁵ (r/(t_* + r)) = 1/(t_* r⁴).

The density μ_b := |dt_* dx|/(t_*⟨x⟩⁴) is a smooth positive b-density on M̃ near Ω̄. Near ι⁺ this is [[lem:ii-a-6-1]].
Near the interior of K⁺, where t_* ∼ t and r is bounded, it is ⟨x⟩⁻⁴|dt/t dx|. Near the interior of ℐ⁺, where
t_* ∈ [1, T], it is t_*⁻¹|dt_* dr/r dω| times a smooth positive function, and dr/r is −2 dx_I/x_I there. Since ⟨x⟩ ∼ r on
Ω (r ≥ r_0 > 0), |dt dx| = |dt_* dx| = c x_I⁻⁸ρ_+⁻⁵ρ_K⁻¹μ_b with c smooth and positive. Thus
L²(|dt dx|) = x_I⁴ρ_+^(5/2)ρ_K^(1/2) L²(μ_b), and b-derivatives commute with the weights up to bounded factors. So
H^(d+3,(2α_I,α_+,α_K))_b(|dt dx|) = H^(d+3,(2(α_I+2),α_+ + 5/2,α_K + 1/2))_b(μ_b) for u supported in Ω, and
[[eq:ii-a-8-2]] follows from the second claim. In dimension 3 + 1 the same product is x_I⁶ρ_+⁴ρ_K = t_*⁻¹r⁻³, which
gives the weights (2(α_I + 3/2), α_+ + 2, α_K + 1/2) of [Hin26c].

*The embedding.* Writing u = w_((γ))v reduces to γ = 0, again because b-derivatives of w_((γ)) are w_((γ)) times smooth
functions. Cover the compact manifold with corners M̃ by finitely many charts [0, 1)^q_x × ℝ^(5−q)_y, with a
subordinate partition of unity {ψ_i}. In logarithmic coordinates z_j = −log x_j the b-vector fields are ∂_(z_j), ∂_y,
and μ_b is |dz dy| times a smooth positive bounded function. ψ_iu, extended by 0, is a function on ℝ⁵_(z,y) with
‖ψ_iu‖_(H^(d+3)(ℝ⁵)) ≤ C‖u‖_(H^(d+3)_b). The Sobolev embedding H^(d+3)(ℝ⁵) ↪ C^d(ℝ⁵) holds since 3 > 5/2: for
|β| ≤ d,

    ‖∂^β f‖_(L^∞) ≤ ∫ |ζ^β f̂| dζ ≤ ‖f‖_(H^(d+3)) (∫ ⟨ζ⟩^(2|β|−2d−6) dζ)^(1/2),

the last integral being finite as 2|β| − 2d − 6 ≤ −6 < −5. The sup norms of z, y-derivatives are the C^d_b-norm. Sum
over i. At the artificial boundary r = r_0 the spaces are extendible: apply the embedding to an extension of comparable
norm and restrict.

*The converse* [[eq:ii-a-8-3]]. Write w := w_((γ)) and w′ := w x_I^δ ρ_+^δ ρ_K^δ. Then
‖w⁻¹V^J u‖_(L²(μ_b)) ≤ ‖w′⁻¹V^J u‖_(L^∞) ‖(x_Iρ_+ρ_K)^δ‖_(L²(μ_b;Ω)). The last factor is finite: on Ω̄ the only boundary
faces are ℐ⁺, ι⁺ and K⁺, with defining functions among x_I, ρ_+ and ρ_K, and in logarithmic coordinates the integrand is
e^(−2δ(z_1+⋯+z_q)) over z_j ≥ z_0, with y in a compact set. ∎

The last claim needs the support in Ω: near a face where no weight decays (for instance I⁰), μ_b has infinite mass.

In dimension 4 + 1, as a variant with the same proof ([[lem:i-c-2-9]] (c)),

    H^(d+3,α)_b(ℝ̄⁴, |dx|) ↪ C^(d,α+2)_b(ℝ̄⁴).                                                             {#eq:ii-a-8-4}

Here |dx| = r⁴μ_b near infinity, so L²(|dx|) = ρ² L²(μ_b), and the embedding H^(d+3)(ℝ⁴) ⊂ C^d(ℝ⁴) (as 3 > 2) applies in
the coordinates (log r, ω), ω ∈ 𝕊³. ([Hin26c, (3.72)], in dimension 3 + 1, has α + 3/2.)

### The standard estimates: setting and statements {#sec:ii-a1-1}

This section and the next four prove the two estimates on which the estimates with b-regularity of [[sec:ii-a-9]]
rest: the elliptic estimate and the real principal type propagation estimate on e3b-spaces without b-regularity, for
operators whose coefficients have finite regularity, with variable orders and constants locally uniform in the
operator. They are [Hin26c, Propositions 3.23 and 3.24] at k = 0 (pp. 69–71), which [Hin26c] proves by citation to the
standard arguments; the hypotheses of the second are those of [[thm:ii-a1-5-4]] (see [[rem:ii-a1-hypotheses]]).

*Method.* Nothing here depends on the dimension. The smooth calculus is that of [[sec:ii-a-3]]. Its operations are
continuous on Fréchet spaces of symbols, so each of them is bounded by finitely many seminorms ([[sec:ii-a1-2-1]]). A
bound that holds for smooth symbols with finitely many seminorms passes to symbols of finite regularity by mollification
in the charts of the secondary structure and weak lower semicontinuity ([[sec:ii-a1-2-2]], as in [[lem:ii-a-8-5]]).
This gives a calculus for symbols of finite regularity with explicit remainder bounds ([[prop:ii-a1-2-4]]). The elliptic
estimate then follows from a parametrix of finite regularity ([[sec:ii-a1-3]]). The propagation estimate follows from a
positive commutator argument ([[sec:ii-a1-4]]), whose commutant is built in flow-box coordinates of the exact Hamilton
field, which has finite regularity ([[sec:ii-a1-5]]). Every square that the argument needs is an exact square of a
symbol of finite regularity, so no Gårding inequality is used.

*Indices.* Each estimate below requires finitely many derivatives of the coefficients, and the number required (the
index) depends only on the orders, never on the auxiliary operators and cut-offs chosen in a proof; these enter the
constants only. This is what the inductions of [[sec:ii-a-9]] need, as they choose new auxiliary operators at every
order of b-regularity. Two rules secure it. First, the multilinear maps to which the closed graph theorem and
[[lem:ii-a1-2-1]] are applied never depend on supports: a relation between supports is used only through an exact
identity of symbols, such as φa = a when φ = 1 on the support of a. Second, a product of operators with disjoint
microsupports is estimated only when a smooth operator stands on each side, by the commutator expansion of
[[prop:ii-a1-2-4]] (e), in which the auxiliary symbol is an argument of the multilinear map.

#### The calculi {#sec:ii-a1-1-1}

M̃ is the compactified spacetime of [[sec:ii-a-1]], with its scaled bounded geometry structure ℬ^× of
[[sec:ii-a-4-1]] and the secondary bounded geometry structure ρℬ obtained by subdividing the unit cells into ρ-cuboids
([Hin26c, (3.26)]; [Hin26d, Section 3.2]). ρℬ is a scaled bounded geometry structure with all scalings equal to 1, so
everything stated in [[sec:ii-a-3]] holds for it. Its operator Lie algebra, which is also its coefficient Lie algebra,
is the large operator Lie algebra 𝒱′ = C^∞_e3b 𝒱_e3b of ℬ^× ((S13)). It defines the
same Sobolev spaces as 𝒱 = C^∞_b 𝒱_e3b: an elliptic element of Ψ^𝗌_𝒱 lies in Ψ^𝗌_(𝒱′) [Hin26d, Remark 3.48] and is
elliptic there, and each space is the set of u that a fixed elliptic operator maps into L². We write:

S̃^m for the symbols of ρℬ of order m. In each chart of ρℬ, with fibre coordinates dual to the coordinate frame, these
are the functions with |∂_x^β ∂_ξ^γ a| ≤ C_(βγ)⟨ξ⟩^(m−|γ|) uniformly ((S4)). This is a Fréchet space with the
seminorms ‖a‖_(M;m), the largest of these constants over |β| + |γ| ≤ M. By (S1)–(S4), S̃^m is the class C^∞_e3b S^m of
[Hin26c, (3.26)]: the symbols whose coefficients are bounded under any number of e3b-derivatives.

Ψ̃^m := Ψ^m_(ρℬ), Op := Op_(ρℬ), and Ψ̃^(−∞) for its residual operators ((S4)). C^∞_b Ψ^m_e3b ⊂ Ψ̃^m
((S13); [[sec:ii-a-4-2]]). The Sobolev spaces of ρℬ are therefore the spaces H^𝗌_e3b of
[[sec:ii-a-4-2]].

The properties used are these: (S5) for mapping properties, with operator norms bounded by a seminorm, and for
compositions, adjoints, principal symbols and commutators; the continuity of Op : S̃^m → Ψ̃^m, of composition as a
bilinear map and of the adjoint ([Hin26d, Remark 3.47], in (S5)); the principal symbol sequence: an A ∈ Ψ̃^m with
vanishing principal symbol lies in Ψ̃^(m−1); (S8) for variable orders; (S10) for commutators with 𝒱_(b,[e3b]); and (S11)
for weights.

*Left quantization.* In the charts of ρℬ (all scalings 1) the local quantization of (S4) is

    (Op_β(b)u)(x) = (2π)^(−n) ∫ e^(i(x−x′)·ξ) ψ(x − x′) b(x, ξ) u(x′) dx′ dξ.

Since ψ = 1 near 0 and the partition χ_α of (S4) sums to 1, Op(f) is multiplication by f
for a function f of the base alone; in particular Op(1) = I. The symbol is evaluated at the left variable, so for every
function f of the base

    f · Op(a) = Op(fa).                                                                                  {#eq:ii-a1-1-1}

*Variable orders.* Fix ρ_∞ ∈ S̃^(−1), positive, equal to (Σ_j ξ(V_(0,j))²)^(−1/2) for |ξ| ≥ 1 (the V_(0,j) of
[[lem:ii-a-2-9]]), so that ρ_∞ is a defining function of fibre infinity ᵉ³ᵇS*M̃. Variable orders are functions
𝗄 ∈ C^∞(ᵉ³ᵇS*M̃), extended homogeneously of degree 0 near fibre infinity. The class of (S8) is that of
[Hin26d, Definition 4.6] (p. 66): for variable 𝗄,

    S̃^𝗄 := ρ_∞^(−𝗄) ⋂_(δ∈(0,1/2)) S̃⁰_(1−δ,δ),     contained in     ⋂_δ S̃^(sup 𝗄)_(1−δ,δ);

the defining function of fibre infinity used there may be replaced by ρ_∞, their quotient being a positive symbol of
order 0. Its operators map H^𝗍_e3b to H^(𝗍−𝗄)_e3b for every variable order 𝗍, without loss, and the calculus of
[Hin26d, Theorem 3.51] (adjoints, compositions, commutators) holds for them, with the principal symbols of compositions
taken modulo ⋂_δ S̃^(𝗄_1+𝗄_2−1+2δ). [Hin26d] states that orders are additive under composition, gives this class of
principal symbols in its (4.10), and says that "Theorem 3.44 remains valid, mutatis mutandis"; we read this as in (S8).
Derivatives of ρ_∞^(−𝗄) carry factors log ρ_∞, as in [[rem:i-a-3-3]], and the symbols of finite regularity below carry
a counted number of such factors ([[def:ii-a1-1-3]]). The class ρ_∞^(−𝗄) S̃⁰, with bounded derivatives, is too small for
them. We write "of order 𝗄 − 1 + 0" for "of order 𝗄 − 1 + δ for every δ > 0", with constants depending on δ.

#### Classical symbols and the locus of microlocalisation {#sec:ii-a1-1-2}

Let ᵉ³ᵇT̄*M̃ be the radial compactification of the fibres of ᵉ³ᵇT*M̃ over the compact manifold with corners M̃. It is a
compact manifold with corners, whose boundary at fibre infinity is ᵉ³ᵇS*M̃.

**Lemma {#lem:ii-a1-1-1}** (Classical symbols.) Let a ∈ C^∞(ᵉ³ᵇT̄*M̃). Then a ∈ C^∞_b S⁰ ⊂ S̃⁰. Consequently
ρ_∞^(−m)a ∈ C^∞_b S^m and ρ_∞^(−𝗄)a ∈ S̃^𝗄.

*Proof.* Use the global fibre coordinates ζ_j := ξ(V_(0,j)), in which ᵉ³ᵇT*M̃ = M̃ × ℝ^N (a vector bundle map onto its
image, of full rank, [[lem:ii-a-2-9]]). In a cell of ℬ^× with coordinates x and scalings ρ_α, the fibre coordinates of
(S4) are the ξ with ξ · dx/ρ_α. They are related to ζ by ζ_j = Σ_i v^i_(α,j)(x)ξ_i, where
(φ_α)_*V_(0,j) = Σ_i v^i_(α,j) ρ_(α,i)∂_i with v_α uniformly bounded in C^∞ ((S1)). This map has a uniformly bounded
inverse on its range, the V_(0,j) spanning 𝒱 uniformly in each cell ([[sec:ii-a-4-1]]). A smooth function on the
compactified bundle has, in the coordinates (x, ζ), x-derivatives along b-vector fields of M̃ bounded, and
ζ-derivatives of order γ bounded by C⟨ζ⟩^(−|γ|) (radial compactification). The coordinate vector fields ∂_(x^i) of a
cell are uniformly bounded combinations of b-vector fields, as the coefficient Lie algebra is C^∞_b 𝒱_b ((S1)). The
chain rule through ζ = v_α(x)ξ then gives the estimates of (S4) uniformly in α, with 𝒲-derivatives, so a ∈ C^∞_b S⁰.
The rest follows from (S8). ∎

*Microsupport, ellipticity.* An operator A ∈ Ψ̃^m is *microsupported* in a closed set K ⊂ ᵉ³ᵇT̄*M̃ if A = Op(a) + R with
a ∈ S̃^m, supp a ⊂ K and R ∈ Ψ̃^(−∞). Following [Hin26c, p. 54], the locus of microlocal analysis is ᵉ³ᵇS*M̃. If
WF′_e3b(A) ⊂ O with O ⊂ ᵉ³ᵇS*M̃ open, then A is microsupported in any closed neighbourhood K of WF′_e3b(A) in the
compactified bundle with K ∩ ᵉ³ᵇS*M̃ ⊂ O. Indeed, if χ̃ ∈ C^∞(ᵉ³ᵇT̄*M̃) equals 1 near WF′(A) and is supported in K, then
A = Op(χ̃a) + Op((1 − χ̃)a) + R, and Op((1 − χ̃)a) is residual, by the definition of the operator wave front set ((S5)).
For L as in [[sec:ii-a1-1-3]] with principal symbol ℓ, Ell(L) ⊂ ᵉ³ᵇS*M̃ is the set of points with a neighbourhood U in
the compactified bundle on which ℓ is invertible with |ℓ⁻¹| ≤ Cρ_∞^m for |ξ| ≥ 1. It is open, and Char(L) is its
complement.

**Lemma {#lem:ii-a1-1-2}** (Disjoint microsupports.) Let K_1, K_2 ⊂ ᵉ³ᵇT̄*M̃ be disjoint closed sets. Then the distance
between K_1 and K_2 in the coordinates (x, ζ/|ζ|, log |ζ|) of each chart of ρℬ, for |ζ| ≥ 1, is bounded below
uniformly. For a_i ∈ S̃^(m_i) supported in K_i, Op(a_1)Op(a_2) ∈ Ψ̃^(−∞). Hence A_1A_2 ∈ Ψ̃^(−∞) whenever
A_1, A_2 ∈ Ψ̃ are microsupported in K_1 and K_2.

*Proof.* The charts of ρℬ are, uniformly, rescalings of charts of the compact manifold with corners in which cells near
the boundary are magnified. Distances therefore do not shrink: a smooth metric on the compact ᵉ³ᵇT̄*M̃ is bounded by a
constant times the Euclidean metric of each chart. So the symbols have disjoint essential supports in the sense of
[Hin26d], being uniformly separated. The wave front set of the composition is empty ((S5)), so it is residual. For
A_i = Op(a_i) + R_i with supp a_i ⊂ K_i and R_i ∈ Ψ̃^(−∞), the other products have a residual factor. ∎

The symbols here are smooth, and no bound in terms of their seminorms is claimed. A closed graph argument on the
subspaces of symbols supported in K_1 and K_2 would bound Op(a_1)Op(a_2) in Ψ̃^(−N) by seminorms whose number may
depend on K_1 and K_2; it is not used. Products of operators of finite regularity with disjoint microsupports are
estimated by [[prop:ii-a1-2-4]] (e) instead, with indices that depend only on the orders.

#### The operators and the statements {#sec:ii-a1-1-3}

**Definition {#def:ii-a1-1-3}** Derivatives are taken in the coordinates (x, ω, τ) = (x, ζ/|ζ|, log |ζ|) of
[[lem:ii-a1-2-2]] (for |ζ| ≥ 1, and (x, ζ) near the zero section) in the charts of ρℬ, and
⟨log ρ_∞⟩ := (1 + (log ρ_∞)²)^(1/2). For M, ν ∈ ℕ_0 and a variable order 𝗆, C^((M))_ν S̃^𝗆 is the space of the
a = ρ_∞^(−𝗆)a_0 with a_0 a function on ᵉ³ᵇT*M̃ whose derivatives of order j ≤ M are bounded by C⟨log ρ_∞⟩^(νj),
uniformly in the charts; the norm ‖a‖_((M);ν,𝗆) is the least such C. S̃^𝗆_ν is the space of smooth a with
‖a‖_((M);ν,𝗆) < ∞ for every M, a Fréchet space with these seminorms. The index ν is dropped when ν = 0.

A class of index ν lies in those of larger index; products satisfy
‖ab‖_((M);ν,𝗆_1+𝗆_2) ≤ C‖a‖_((M);ν,𝗆_1)‖b‖_((M);ν,𝗆_2) by Leibniz's rule. As ∂_ζ is e^(−τ) times bounded combinations
of ∂_ω, ∂_τ ([[lem:ii-a1-2-2]]) and ⟨log ρ_∞⟩^(νj) ≤ C_δ ρ_∞^(−δj), S̃^𝗆_ν is contained, continuously, in the class
ρ_∞^(−𝗆) ⋂_δ S̃⁰_(1−δ,δ) of (S8), also when 𝗆 is constant; for constant 𝗆 = m, S̃^m_0 is the class S̃^m of (S4). The
derivatives of log ρ_∞ of positive order are bounded, as log ρ_∞ = −τ near fibre infinity.

For a finite set 𝒫 = {P_1, …, P_J} ⊂ C^∞_b Ψ^m_e3b of operators localized near the diagonal ([[sec:ii-a-8-3]]), with
P_j = Op(p_j) + R_j, p_j ∈ C^∞_b S^m, R_j ∈ Ψ̃^(−∞), and a_j ∈ C^(d_0)_e3b ([[def:ii-a-8-1]]), the operator L = Σ a_jP_j
satisfies, by [[eq:ii-a1-1-1]],

    L = Op(ℓ_f) + Σ_j a_jR_j,     ℓ_f := Σ_j a_jp_j ∈ C^((d_0)) S̃^m,                                    {#eq:ii-a1-1-2}

with ‖ℓ_f‖_((d_0);m) ≤ C max_j ‖a_j‖_(C^(d_0)_e3b), as e3b-derivatives of the a_j are the rescaled coordinate
derivatives in the charts. Its principal symbol is ℓ := Σ_j a_jσ(P_j), with σ(P_j) a representative of order m of the
principal symbol. On ℂ^(N′)-valued functions everything is matrix-valued.

Two statements are proved: the elliptic estimate [[thm:ii-a1-3-1]], and the real principal type estimate
[[thm:ii-a1-5-4]] for the operators of [[sec:ii-a1-5-1]]. In both, B, E and G are carried by χ in the sense of
[[sec:ii-a-8-3]], and the estimates hold in the strong sense: the left side is finite when the right side is. In the
second, the elements of 𝒫_m are taken with principal symbols that are smooth and homogeneous near fibre infinity
(classical), so that the Hamilton vector field is continuous on ᵉ³ᵇS*M̃.

### The calculus of finite regularity {#sec:ii-a1-2}

This section extends the calculus of [[sec:ii-a-3]] to symbols of finite regularity, with explicit bounds on the
remainders.

#### Seminorm bounds {#sec:ii-a1-2-1}

**Lemma {#lem:ii-a1-2-1}** Let X_1, …, X_r and Y be Fréchet spaces and T : X_1 × ⋯ × X_r → Y continuous and
multilinear. For every continuous seminorm q on Y there are continuous seminorms p_i on X_i and C with
q(T(x_1, …, x_r)) ≤ C ∏_i p_i(x_i). A multilinear map between Fréchet spaces that is continuous in each variable
separately is continuous.

*Proof.* By continuity at 0 there are p_i with q(T(x)) < 1 whenever p_i(x_i) < 1 for all i. For general x with
p_i(x_i) ≠ 0, apply this to x_i/(2p_i(x_i)) and use multilinearity, which gives C = 2^r. If some p_i(x_i) = 0, then
tx_i satisfies p_i(tx_i) < 1 for all t, so q(T(x)) = 0. The second statement is the theorem of Banach and Steinhaus for
separately continuous bilinear maps on Fréchet spaces, extended to r factors by induction. ∎

A linear map from a Fréchet space X to a Banach space Z with closed graph is continuous (the closed graph theorem). It is
then bounded by C times a seminorm of X. The seminorms of S̃^m are increasing in M, so such a bound has the form
C‖x‖_(M;m).

#### Mollification {#sec:ii-a1-2-2}

**Lemma {#lem:ii-a1-2-2}** Let a ∈ C^((M))_ν S̃^𝗆, M ≥ 1. There are a_ε ∈ S̃^𝗆_ν, ε ∈ (0, 1], such that:

(i) ‖a_ε‖_((M′);ν,𝗆) ≤ C‖a‖_((M′);ν,𝗆) for M′ ≤ M;

(ii) a_ε → a pointwise, with |a_ε − a| ≤ Cε‖a‖_((1);ν,𝗆)⟨log ρ_∞⟩^ν ρ_∞^(−𝗆), and
‖a_ε − a‖_((M−1);ν,𝗆+δ) ≤ C_δ ε‖a‖_((M);ν,𝗆) for every δ > 0;

(iii) if a is supported in a closed set K of the compactified bundle, then a_ε is supported in the ε-neighbourhood of K
in the coordinates of [[lem:ii-a1-1-2]].

*Proof.* Write a = ρ_∞^(−𝗆)a_0 and mollify a_0. In each chart ψ_β of ρℬ, with a uniformly smooth partition of unity
θ_β ([[lem:ii-a-8-5]]), use the coordinates (x, ω, τ) := (x, ζ/|ζ|, log |ζ|) for |ζ| ≥ 1, and (x, ζ) near the zero
section, glued by a fixed partition of unity in ζ. The estimates of S̃⁰ for a_0 are equivalent, uniformly, to bounded
derivatives in (x, ω, τ): ∂_ζ is e^(−τ) times a combination of ∂_ω and ∂_τ with bounded coefficients. Put
a_(0,ε) := Σ_β (θ_βa_0) ∗ η_ε, the convolution taken in (x, ω, τ) (on the sphere, in a fixed finite atlas). Derivatives
commute with convolution; the charts have uniformly bounded transitions and finite multiplicity; and ⟨log ρ_∞⟩ changes by
at most a bounded factor over a unit ball in these coordinates, as log ρ_∞ = −τ. Hence (i). A derivative of a_(0,ε) of
order j > M puts j − M derivatives on η_ε, so a_(0,ε) satisfies the bounds of every order, with constants depending on
ε: a_ε ∈ S̃^𝗆_ν. (ii) is the mean value theorem: a derivative of order j ≤ M − 1 of a_(0,ε) − a_0 is bounded by
Cε⟨log ρ_∞⟩^(ν(j+1)), the factor ρ_∞^δ⟨log ρ_∞⟩^ν is bounded, and the derivatives of ρ_∞^δ are ρ_∞^δ times bounded
functions. (iii) is the support of η_ε. ∎

#### Quantization and remainders {#sec:ii-a1-2-3}

**Lemma {#lem:ii-a1-2-3}** (Density, and a regularising family.) (a) C_c^∞(M̃°) is dense in H^𝗌_e3b for every variable
order 𝗌. (b) Let K ∈ ℕ and T_t := Op(τ_t), τ_t := (1 + tρ_∞⁻¹)^(−K), t ∈ (0, 1]. Then T_t is bounded in Ψ̃⁰, lies in
Ψ̃^(−K) for each t, and T_t → I strongly on every H^𝗌_e3b as t → 0.

*Proof.* (a) If not, there is 0 ≠ w in the dual space H^(−𝗌) ((S8), the duality for variable orders) annihilating C_c^∞;
then w = 0 as a distribution, a contradiction. (b) τ_t is bounded in S̃⁰: ρ_∞∂_(ρ_∞) of it is Ktρ_∞⁻¹(1 + tρ_∞⁻¹)⁻¹τ_t,
which is bounded, and the other derivatives act on ρ_∞ only through such factors. It lies in S̃^(−K) for fixed t > 0.
Moreover |1 − τ_t| ≤ min(1, Ktρ_∞⁻¹) ≤ K(tρ_∞⁻¹)^δ, and likewise for its derivatives, so τ_t → 1 in S̃^δ for every δ > 0.
So ‖(T_t − I)v‖_(H^𝗌) → 0 for v ∈ H^(𝗌+δ), by (S5). T_t is uniformly bounded on H^𝗌, and C_c^∞ ⊂ H^(𝗌+δ) is dense by (a),
so the convergence holds on all of H^𝗌. ∎

For a ∈ C^((M))_ν S̃^𝗆 and u ∈ C_c^∞(M̃°), Op(a)u is defined by the formulae of (S4). The local quantization is
(2π)^(−n) ∫ e^(ix·ξ) b(x, ξ) ℱ(ψ(x − ·)u)(ξ) dξ, where the Fourier transform is rapidly decreasing in ξ, locally
uniformly in x. So the integral converges absolutely for any b of polynomial growth, and only finitely many charts meet
the support of u.

**Proposition {#prop:ii-a1-2-4}** (Finite regularity.) Let 𝗍 be a variable order, ν ∈ ℕ_0, and 𝗆, 𝗆_1, 𝗆_2 orders,
constant or variable. There are M and C, depending on these orders, on ν and on δ > 0, with the following properties,
for symbols in C^((M+2))_ν S̃ of the stated orders (symbols of different indices are taken in the largest). Throughout,
"order 𝗋" means bounded from H^𝗍 to H^(𝗍−𝗋).

(a) Op(a) extends from C_c^∞ to a bounded operator of order 𝗆, without loss, with norm at most C‖a‖_((M);ν,𝗆).

(b) Op(a_1)Op(a_2) − Op(a_1a_2) has order 𝗆_1 + 𝗆_2 − 1 + δ, with norm at most C‖a_1‖_((M);ν,𝗆_1)‖a_2‖_((M);ν,𝗆_2).

(c) Op(a)* − Op(ā) has order 𝗆 − 1 + δ, with norm at most C‖a‖_((M);ν,𝗆). Here the adjoint is with respect to
L²(|dt dx|), and matrix-valued symbols use the conjugate transpose. |dt dx| is a weight w times an e3b-density, so this
adjoint is w⁻¹A^⋆w with A^⋆ the adjoint for that density, and conjugation by a weight preserves the classes ((S11)).

(d) i[Op(a_1), Op(a_2)] − Op(H_(a_1)a_2) has order 𝗆_1 + 𝗆_2 − 2 + δ, with norm at most
C‖a_1‖_((M+1);ν,𝗆_1)‖a_2‖_((M+1);ν,𝗆_2). If one of a_1, a_2 is scalar and the other matrix-valued, H_(a_1)a_2 is taken
entrywise.

(e) (Disjoint microsupports.) Let T(a_1, …, a_r) be an expression as in (f), of order μ for smooth symbols, and let
B_1, B_2 ∈ Ψ̃⁰ be microsupported in disjoint closed sets K_1, K_2 of the compactified bundle ([[sec:ii-a1-1-2]]). Then
for every N, B_1T(a_1, …, a_r)B_2 has order −N, with norm at most C ∏_i ‖a_i‖_((M);ν,𝗆_i), where M depends only on N,
𝗍, μ, the expression, its orders 𝗆_i, ν and δ; B_1 and B_2 enter only the constant C. The same holds for
S_1B_1TB_2S_2 with expressions S_1, S_2 as in (f), and a product of bounded operators one of which lies in Ψ̃^(−∞) has
every order.

(f) (General principle.) Let T(a_1, …, a_r) be a finite expression in the operators Op(a_i), Op of products and of
complex conjugates of the a_i, and their adjoints, formed by sums and compositions. Suppose that for smooth symbols it
lies in the class of order μ, by (S5) and (S8): a difference of operators with the same principal symbol is one order
lower, and a commutator is one order lower than the
product. This is to hold for all symbols of the stated orders, the expression being fixed; a relation between the
symbols, such as one being 1 on the support of another, is not allowed to enter. Then for symbols of finite regularity
the operator given by the same expression has order μ + δ, or μ when all orders are constant and ν = 0. Its norm is at
most C ∏_i ‖a_i‖_((M);ν,𝗆_i), with M depending only on the expression, the orders 𝗆_i and 𝗍, ν and δ. In particular,
for a of constant order m with ν = 0 and a real symbol ǎ of order 𝗄 and any index: D_a := Op(a)* − Op(a*) has order
m − 1, and [D_a, Op(ǎ)] and
[ [D_a, Op(ǎ)], Op(ǎ) ] have orders m + 𝗄 − 2 + δ and m + 2𝗄 − 3 + δ.

The constants are uniform for symbols bounded in the stated norms. In (e) they depend in addition on B_1 and B_2,
while M does not.

*Proof.* *Smooth symbols.* (a) For smooth a ∈ S̃^𝗆_ν, Op(a) is bounded of order 𝗆, without loss ((S8) and
[[def:ii-a1-1-3]]). The linear map a ↦ Op(a) from the Fréchet space S̃^𝗆_ν to the bounded operators H^𝗍 → H^(𝗍−𝗆) has
closed graph: if a_j → a and Op(a_j) → T, then Op(a_j)u → Op(a)u pointwise for u ∈ C_c^∞, by the integral above, so
T = Op(a) on the dense set C_c^∞ ([[lem:ii-a1-2-3]] (a)). So it is continuous, and bounded by C‖a‖_((M);ν,𝗆)
([[sec:ii-a1-2-1]]). (b) By (S5) and (S8), Op(a_1)Op(a_2) has principal symbol a_1a_2, as does Op(a_1a_2), so the
difference lies in the class of order 𝗆_1 + 𝗆_2 − 1 + δ. The bilinear map into that class is separately continuous by
the closed graph theorem: it is continuous into the class of order 𝗆_1 + 𝗆_2 + δ, by the continuity of composition, and
convergence in the smaller class implies convergence in the larger one, so its graph in the smaller class is closed.
[[lem:ii-a1-2-1]] then applies. (c) is the same, with σ(A*) the complex conjugate of σ(A). (d) By (S5),
i[Op(a_1), Op(a_2)] has order 𝗆_1 + 𝗆_2 − 1 + δ and principal symbol H_(a_1)a_2. Then H_(a_1)a_2 is a symbol of that
order, and Op(H_(a_1)a_2) has full symbol H_(a_1)a_2. So the difference has order one lower; continuity is as in (b).
Its norm involves one more derivative of each symbol, through H_(a_1)a_2. (e) is proved after (f).

*Finite regularity.* For each item, let a_(i,ε) be the mollifications of [[lem:ii-a1-2-2]], with uniformly bounded
norms. For u ∈ C_c^∞, Op(a_(i,ε))u → Op(a_i)u pointwise and boundedly on compact sets, by dominated convergence in the
integral above; this is all (a) needs. In (b)–(f), (a) is available, M being taken large enough that (a) applies at the
finitely many orders raised by 2δ: as a_i ∈ C^((M+2))_ν, [[lem:ii-a1-2-2]] (ii) gives a_(i,ε) → a_i in
C^((M+1))_ν S̃^(𝗆_i+δ), so a_(1,ε)a_(2,ε), ā_(i,ε) and H_(a_(1,ε))a_(2,ε) converge in the (M)-norms at orders raised by
2δ, and by (a) every factor of every item converges in operator norm, with a loss of 2δ in the order. (The factors
vary with ε, so the convergence of the outer factors is needed, and this gives it.) So for u ∈ C_c^∞ the composite
operators applied to u converge in a Sobolev space of lower order, hence in 𝒟′. The smooth bounds hold uniformly in ε.
A bounded sequence in the Hilbert space H^(𝗍−𝗋) has weakly convergent subsequences, whose limits are identified in 𝒟′,
and the norm is weakly lower semicontinuous. So the bounds hold for u ∈ C_c^∞ with the limit operators, and extend by
density ([[lem:ii-a1-2-3]] (a)). In (a) this defines the extension. (f) is proved as (b): for smooth symbols the
multilinear map is continuous into the class of order μ + δ. It is continuous into a larger class because compositions
and adjoints are continuous, and its graph in the smaller class is closed. Then [[lem:ii-a1-2-1]] and the passage to
finite regularity apply. The multilinear map is defined on the whole spaces of symbols of the stated orders and is
determined by the expression, so the seminorms that [[lem:ii-a1-2-1]] produces, and hence M, depend only on the
expression and the orders. When all orders are constant and ν = 0, the classes are those of (S5) without loss, and the
same argument gives order μ. ∎

*Proof of (e).* Choose y ∈ C^∞(ᵉ³ᵇT̄*M̃) with y = 1 near K_1 and y = 0 near K_2, and put Y := Op(y) ∈ Ψ̃⁰
([[lem:ii-a1-1-1]]). Then B_1(I − Y) and YB_2 lie in Ψ̃^(−∞) by [[lem:ii-a1-1-2]], I − Y being Op(1 − y)
([[eq:ii-a1-1-1]]) and supp(1 − y), supp y being disjoint from K_1, K_2. By [[eq:ii-a-comm-split]] (with B_1, B_2 for B,
I − B^♯), applied to T_0 := T, T_1, …, T_(J−1), where T_j := ad_Y^j T,

    B_1TB_2 = Σ_(j=0)^(J−1) (B_1(I − Y)T_jB_2 + B_1T_jYB_2) + B_1T_JB_2.

T_j is the expression ad_(Op(y_1))⋯ad_(Op(y_j))T(a_1, …, a_r) in the r + j symbols y_1, …, y_j, a_1, …, a_r, at y_1 = ⋯ =
y_j = y. For smooth symbols it has order μ − j: y_i is scalar of order 0, and each commutator with Op(y_i) lowers the
order by one ((S5), (S8)). By (f), T_j has order μ − j + δ, with norm at most C‖y‖^j_((M);0,0) ∏_i ‖a_i‖_((M);ν,𝗆_i), M
being the number of (f) for this expression. Take δ ≤ 1, J := ⌈sup μ⌉ + N + 1 and 𝗍′ := 𝗍 + N + ⌈sup μ⌉ + 1. B_1 and B_2
are bounded on every H^𝗍_e3b ((S5), (S8)). So B_1T_JB_2 has order −N, as μ − J + δ ≤ −N. B_1(I − Y)T_jB_2 maps H^𝗍 to
H^(𝗍−sup μ−1) by T_j (j − δ ≥ −1), and then to H^(𝗍+N) by the residual factor. B_1T_jYB_2 maps H^𝗍 to H^(𝗍′) by the
residual factor YB_2, and then to H^(𝗍′−sup μ−1) ⊂ H^(𝗍+N) by T_j, as j − δ ≥ −1. Hence the bound, with M the largest of
the numbers of (f) for T_0, …, T_J at the orders 𝗍 and 𝗍′. It depends only on N, 𝗍, μ, the expression, its orders, ν and
δ; B_1, B_2 and y enter only the constant. For S_1B_1TB_2S_2, the factors S_1 and S_2 are bounded by (f) at the orders
involved, with indices of the same kind. ∎

**Lemma {#lem:ii-a1-2-5}** (Square roots.) Let Q be a Hermitian matrix-valued function on a set W of phase space with
Q ≥ c Id, c > 0. Derivatives are taken in the coordinates of [[lem:ii-a1-2-2]].

(i) If |∂^β Q| ≤ C_0⟨log ρ_∞⟩^(ν|β|) for |β| ≤ M, then Q^(1/2) and Q^(−1/2) satisfy the same bounds, with constants
depending on c, C_0, M and ν.

(ii) Let Q = Q_0 + λ Id, where Q_0 ≥ c satisfies the bounds of (i) and λ ≥ 0 is scalar with
|∂^β λ| ≤ C_0⟨log ρ_∞⟩^(1+ν|β|) for |β| ≤ M. Then for |β| ≤ M, with C depending on c, C_0, M and ν,

    |∂^β Q^(−1/2)| ≤ C⟨log ρ_∞⟩^((ν+1)|β|),     |Q^(1/2)| ≤ C⟨log ρ_∞⟩^(1/2),
    |∂^β Q^(1/2)| ≤ C⟨log ρ_∞⟩^((ν+1)|β|)  (β ≠ 0).

So Q^(−1/2) is in the class of index ν + 1 and order 0, and Q^(1/2) in that of index ν + 1 and order δ for every
δ > 0.

The index ν + 1 cannot be lowered to ν. Let f ≥ 0 be smooth with f′ compactly supported (so that yf′(y) is bounded and
the τ-derivatives of Q stay in the class) and f(y) = y² near 0, and put Q := c + ⟨log ρ_∞⟩ f(x⟨log ρ_∞⟩^ν), which
satisfies (ii) with index ν; then ∂_x² Q^(1/2) = c^(−1/2)⟨log ρ_∞⟩^(1+2ν) at x = 0, beyond the bound ⟨log ρ_∞⟩^(2ν) of
index ν.

*Proof.* (i) Q^(±1/2) = (2πi)⁻¹ ∮_γ z^(±1/2)(z − Q)⁻¹ dz for a fixed contour γ in {Re z > 0} around [c, C_0], at
distance at least c/2 from it. A derivative ∂^β(z − Q)⁻¹ is a sum of products
(z − Q)⁻¹ ∂^(β_1)Q (z − Q)⁻¹ ⋯ ∂^(β_k)Q (z − Q)⁻¹ with β_1 + ⋯ + β_k = β and |β_i| ≥ 1, each bounded on γ by
C⟨log ρ_∞⟩^(ν|β|).

(ii) By the spectral theorem, Q^(−1/2) = π⁻¹ ∫_0^∞ s^(−1/2)(s + Q)⁻¹ ds and Q^(1/2) = π⁻¹ ∫_0^∞ s^(−1/2) Q(s + Q)⁻¹ ds.
As Q(s + Q)⁻¹ = I − s(s + Q)⁻¹, for β ≠ 0 this gives ∂^β Q^(1/2) = −π⁻¹ ∫_0^∞ s^(1/2) ∂^β(s + Q)⁻¹ ds. Now
Q ≥ (c + λ)Id, so ‖(s + Q)⁻¹‖ ≤ (s + c + λ)⁻¹, and |∂^(β_i)Q| ≤ 2C_0⟨log ρ_∞⟩^(1+ν|β_i|). Expanding ∂^β(s + Q)⁻¹ as in
(i), a product with k factors ∂^(β_i)Q is bounded by C(s + c + λ)^(−k−1)⟨log ρ_∞⟩^(k+ν|β|), with 1 ≤ k ≤ |β|. Since
∫_0^∞ s^(∓1/2)(s + c + λ)^(−k−1) ds = C_k(c + λ)^(∓1/2−k) ≤ C_k c^(∓1/2−k) for k ≥ 1 (the exponent ∓1/2 − k being
negative), both derivative bounds follow.
Finally |Q^(−1/2)| ≤ c^(−1/2) and |Q^(1/2)| ≤ |Q|^(1/2) ≤ (C_0 + C_0⟨log ρ_∞⟩)^(1/2). ∎

**Lemma {#lem:ii-a1-2-6}** (The supremum bound.) Let z ∈ C^((M))_ν S̃⁰, possibly matrix-valued, with M large, and
η > 0. Then for every δ > 0,

    ‖Op(z)v‖² ≤ (sup |z|² + η)‖v‖² + C_(η,δ)‖v‖²_(−1/2+δ),

where sup |z| is the supremum of the operator norm of z over phase space.

*Proof.* Let r := (sup |z|² + η − z^*z)^(1/2), a Hermitian symbol in C^((M))_ν S̃⁰ by [[lem:ii-a1-2-5]] (i), as
sup |z|² + η − z^*z ≥ η. By [[prop:ii-a1-2-4]] (b), (c), Op(z)*Op(z) + Op(r)*Op(r) = Op(z^*z + r^*r) + R =
(sup |z|² + η)I + R, with R of order −1 + 2δ and Op(1) = I ([[sec:ii-a1-1-1]]). Pair with v:
|⟨Rv, v⟩| ≤ C‖v‖²_(−1/2+δ). ∎

*The regulariser.* For κ ∈ (0, 1/2] put φ_ε := (1 + ερ_∞⁻¹)^(−κ) and θ_ε := ερ_∞⁻¹(1 + ερ_∞⁻¹)⁻¹, ε ∈ (0, 1]. For any
vector field V,

    V(ρ_∞^(−2𝗄)φ_ε²) = ρ_∞^(−2𝗄)φ_ε²(−2(𝗄 − κθ_ε)ρ_∞⁻¹Vρ_∞ − 2(V𝗄) log ρ_∞).                             {#eq:ii-a1-2-1}

This is [[eq:i-a-3-6]] with the variable exponent. φ_ε is bounded in S̃⁰, lies in S̃^(−κ) for each ε, and tends to 1 in
S̃^δ for every δ > 0 (proof of [[lem:ii-a1-2-3]] (b)). θ_ε is bounded in S̃⁰ with values in [0, 1).

### The elliptic estimate {#sec:ii-a1-3}

**Theorem {#thm:ii-a1-3-1}** (The elliptic estimate; [Hin26c, Proposition 3.23] at k = 0.) Let 𝗌 and N be given. There
is d_0 = d_0(m, 𝗌, N) such that the following holds for every finite 𝒫 ⊂ C^∞_b Ψ^m_e3b, every N′ and every
L ∈ C^(d_0)_e3b 𝒫 on ℂ^(N′)-valued functions; d_0 does not depend on 𝒫, N′, L, B, G or χ. Let B, G ∈ C^∞_b Ψ⁰_e3b be
carried by χ, with WF′(B) ⊂ Ell(G) ∩ Ell(L). If χu ∈ H^(−N)_e3b and GLu ∈ H^(𝗌−m)_e3b, then Bu ∈ H^𝗌_e3b and

    ‖Bu‖_(H^𝗌_e3b) ≤ C(‖GLu‖_(H^(𝗌−m)_e3b) + ‖χu‖_(H^(−N)_e3b)).

C depends on L only through max_j ‖a_j‖_(C^(d_0)_e3b) and a lower bound for the ellipticity of ℓ near WF′(B); so it is
uniform for L in a neighbourhood in C^(d_0)_e3b 𝒫 on which WF′(B) ⊂ Ell(L) holds with a uniform bound.

([Hin26c, Proposition 3.23] states the scalar case; with matrix-valued principal symbols the proof is the same.)

*Proof.* Let K := WF′(B), compact in the open set O := Ell(G) ∩ Ell(L). Fix J ∈ ℕ, to be chosen, and closed sets
K_0 ⊂ K_1 ⊂ ⋯ ⊂ K_(J+2) of the compactified bundle, each a neighbourhood of the previous one, with K ⊂ K_0° and
K_(J+2) ∩ ᵉ³ᵇS*M̃ ⊂ O. They lie over {ϑ ≥ 3c/4}, ϑ and c being those of [[sec:ii-a-8-3]] for B and G (K lies over
{ϑ ≥ c}), and in {|ξ| ≥ 1} near fibre infinity: choose them inside a set {ρ_∞ ≤ r_1} on which ℓ is invertible with
|ℓ⁻¹| ≤ C_ℓ ρ_∞^m, as Ell(L) is defined by such a bound on a neighbourhood. Fix χ̃_i ∈ C^∞(ᵉ³ᵇT̄*M̃) with χ̃_i = 1 near
K_(i−1) and supp χ̃_i ⊂ K_i, and let G_i, i ≥ 1, be Op(χ̃_i) truncated to range ϵ_ϑ. As χ̃_i = f(ϑ)χ̃_i, the G_i are
auxiliary operators ((R1) of [[sec:ii-a-8-3]]), carried by χ; and G_i is Op(χ̃_i) up to a residual operator. By
[[sec:ii-a1-1-2]], B is microsupported in K_0: B = Op(b) + R_B with supp b ⊂ K_0.

*One step.* Let A ∈ Ψ̃^𝗋 be microsupported in K_i, A = Op(a) + R_A with a ∈ S̃^𝗋 (smooth) supported in K_i, and i ≤ J.
Put q := χ̃_(i+1) a ℓ⁻¹ ∈ C^((d_0)) S̃^(𝗋−m), which is defined since ℓ is invertible on K_(i+1); writing ℓ = ρ_∞^(−m)ℓ_0,
its norms are bounded by those of ℓ and by C_ℓ, by ∂(ℓ_0⁻¹) = −ℓ_0⁻¹(∂ℓ_0)ℓ_0⁻¹. By [[eq:ii-a1-1-2]],

    Op(q)L = Op(q)Op(ℓ_f) + Op(q) Σ_j a_jR_j = Op(qℓ_f) + D_1 + Op(q) Σ_j a_jR_j,

where D_1 := Op(q)Op(ℓ_f) − Op(qℓ_f) has order 𝗋 − 1 + δ by [[prop:ii-a1-2-4]] (b). Next, qℓ_f = χ̃_(i+1)a +
χ̃_(i+1)aℓ⁻¹(ℓ_f − ℓ), and ℓ_f − ℓ = Σ_j a_j(p_j − σ(P_j)) ∈ C^((d_0)) S̃^(m−1). Also χ̃_(i+1)a = a. These are exact
identities of symbols, χ̃_(i+1) being 1 on supp a. So

    A = Op(q)L − E_A,     E_A := D_1 + Op(χ̃_(i+1)aℓ⁻¹(ℓ_f − ℓ)) + Op(q) Σ_j a_jR_j − R_A.                {#eq:ii-a1-3-1}

E_A has order 𝗋 − 1 + δ. The term Op(q) Σ a_jR_j has every order, by [[prop:ii-a1-2-4]] (a) and [[lem:ii-a-8-5]] (a)
for the multiplications, R_j being residual. Below, A is B or one of the G_i, so Aχ = A, and Au = Aχu. Apply
[[eq:ii-a1-3-1]] to χu ∈ H^(−N): L maps it to H^(−N−m) ([[lem:ii-a-8-6]] (a)), and all terms make sense once d_0 is
large for the finitely many orders involved. Let χ_* be the cut-off of (R2) of [[sec:ii-a-8-3]]. Then Gχ_* = G and
G_iχ_* = G_i, which is all that [[lem:ii-a-8-4]] (c) asks of the cut-off: χ_* needs no margin of its own. And χ = 1
within D of supp χ_*, so ‖χ_*Lu‖_(−N−m) = ‖χ_*Lχu‖_(−N−m) ≤ C‖χu‖_(−N) by [[lem:ii-a-8-6]] (a).

*Localisation.* G_(i+1), which is Op(χ̃_(i+1)) up to a residual operator, is microsupported in K_(i+1), and
1 − χ̃_(i+1) vanishes near K_i ⊃ supp a, so (I − G_(i+1))A ∈ Ψ̃^(−∞) ([[lem:ii-a1-1-2]]). I − G_(i+2), which is
Op(1 − χ̃_(i+2)) up to a residual operator, is microsupported in the support of 1 − χ̃_(i+2), which is disjoint from
K_(i+1). Hence, writing A = G_(i+1)A + (I − G_(i+1))A and inserting
I = G_(i+2) + (I − G_(i+2)) after Op(q) and after E_A,

    A = G_(i+1)Op(q)G_(i+2)L − G_(i+1)E_AG_(i+2) + G_(i+1)Op(q)(I − G_(i+2))L − G_(i+1)E_A(I − G_(i+2))
        + (I − G_(i+1))A.

By [[prop:ii-a1-2-4]] (e), with B_1 = G_(i+1), B_2 = I − G_(i+2) and the expressions Op(q) and E_A (whose terms with a
residual factor R_j or R_A have every order directly), the third and fourth operators have every order; so has the
fifth. The identity is applied to χu, as Au = Aχu: the third operator then acts on Lχu ∈ H^(−N−m), and the fourth and
fifth on χu, so these three terms are bounded by C‖χu‖_(−N). In the first two, G_(i+2)Lχu = G_(i+2)Lu and
G_(i+2)χu = G_(i+2)u, as G_(i+2) is carried by χ. Hence, for every order 𝗋′,

    ‖Au‖_(𝗋′) ≤ C‖G_(i+2)Lu‖_(𝗋′+𝗋−m) + C‖G_(i+2)u‖_(𝗋′+𝗋−1+δ) + C‖χu‖_(−N),

Op(q) having order 𝗋 − m without loss ([[prop:ii-a1-2-4]] (a)) and G_(i+1)E_A order 𝗋 − 1 + δ. Further,
‖G_(i+2)Lu‖_(𝗋′+𝗋−m) ≤ C(‖GLu‖_(𝗋′+𝗋−m) + ‖χ_*Lu‖_(−N−m)) by [[lem:ii-a-8-4]] (c), as K_(i+2) ∩ ᵉ³ᵇS*M̃ ⊂ Ell(G),
and the last term is at most C‖χu‖_(−N).

*Iteration.* Take δ = 1/2, 𝗋 = 0 and 𝗋′ = 𝗌 for A = B; then A = G_(i+2) and 𝗋′ = 𝗌 − j/2 at step j, with i = 2j.
After J′ steps the remaining term is ‖G_(2J′)u‖_(𝗌−J′/2) ≤ C‖χu‖_(−N) once J′/2 ≥ sup 𝗌 + N. Take J := 2J′. Summing,

    ‖Bu‖_𝗌 ≤ C(‖GLu‖_(𝗌−m) + ‖χu‖_(−N)).

The identities [[eq:ii-a1-3-1]] hold for every u with χu ∈ H^(−N), and each term on the right is finite when the right
side of the estimate is. So the estimate holds in the strong sense. The constants depend on finitely many norms of the
a_j, through ℓ_f, ℓ and q, and on C_ℓ, the bound for ℓ⁻¹ on K_(J+2). For a perturbation of L that is small in these
norms, ℓ stays invertible on K_(J+2) with a comparable bound. On ℂ^(N′), ℓ⁻¹ is the inverse matrix, and nothing else
changes. Variable orders enter only through the spaces, on which the operators of constant order act by
[[prop:ii-a1-2-4]] (a).

*The index.* The regularity used is that of [[prop:ii-a1-2-4]] (a), (b) and (e), for the finitely many expressions and
orders of the steps above (determined by m, 𝗌, N and J′, with δ = 1/2); that of [[lem:ii-a-8-5]] (a), for the
multiplications by the a_j in Op(q) Σ_j a_jR_j, at the finitely many orders so determined; and that of
[[lem:ii-a-8-6]] (a) at (−N, m, N). By [[prop:ii-a1-2-4]], [[lem:ii-a-8-5]] and [[lem:ii-a-8-6]], none of these numbers
depends on B, G, L, 𝒫, N′, χ or the auxiliary K_i, χ̃_i, χ_*, which enter only the constants. So d_0 depends only on
m, 𝗌 and N. ∎

### The positive commutator lemma {#sec:ii-a1-4}

Let L be of the form [[eq:ii-a1-1-2]], possibly on ℂ^(N′), with real scalar principal symbol ℓ, so that
ℓ_f − ℓ ∈ C^((d_0)) S̃^(m−1) (matrix-valued). Put L_R := (L + L*)/2 and L_I := (L − L*)/(2i). By [[prop:ii-a1-2-4]] (c),
L_I has order m − 1 + δ. For an operator Ǎ, which need not be self-adjoint (below, Ǎ = Op(ǎ)Φ_0 with ǎ a real scalar
symbol and Φ_0 a smooth localiser, as in [[lem:ii-a1-4-1]]),

    C_ǎ := i(L*Ǎ*Ǎ − Ǎ*ǍL) = i[L_R, Ǎ*Ǎ] + L_IǍ*Ǎ + Ǎ*ǍL_I,     ⟨C_ǎw, w⟩ = 2 Im⟨ǍLw, Ǎw⟩                {#eq:ii-a1-4-1}

for w ∈ H^(K′)_e3b with K′ as in [[lem:ii-a1-4-1]] (iii). (The algebra: L = L_R + iL_I with L_R and L_I formally
self-adjoint.) In [[eq:i-a-3-4]] the commutant is self-adjoint and Ǎ*Ǎ = Ǎ²; here it is not, and Ǎ² in place of Ǎ*Ǎ
would make the identity false. Let 𝗌 be a variable order and 𝗄 := 𝗌 − (m − 1)/2.

**Lemma {#lem:ii-a1-4-1}** (One step.) Let κ ∈ (0, 1/4], δ_0 ∈ (0, 1/4], ς ∈ {1, −1}, and let G and E be carried by χ.
Suppose that for ε ∈ (0, 1] there are real scalar symbols ǎ_ε and symbols b_ε, e_ε and z_ε with the following
properties.

(i) ǎ_ε is bounded in C^((M))_ν S̃^𝗄, lies in C^((M))_ν S̃^(𝗄−κ) for each ε, and is supported in a closed set K_1 with
K_1 ∩ ᵉ³ᵇS*M̃ ⊂ Ell(G). Here ν ∈ ℕ_0 is fixed, all classes below have index ν, and M is large for the orders involved.

(ii) b_ε is bounded in C^((M))_ν S̃^(𝗌+δ) for every δ > 0, lies in C^((M))_ν S̃^(𝗌−κ+δ) for each ε, and tends to b_0
pointwise with these bounds. e_ε is bounded in C^((M))_ν S̃^𝗌, lies in C^((M))_ν S̃^(𝗌−κ) for each ε, and is supported in
a closed set K_E ⊂ K_1 with K_E ∩ ᵉ³ᵇS*M̃ ⊂ Ell(E). z_ε is bounded in C^((M))_ν S̃^(−(m−1)/2), and ǎ_ε = z_εb_ε.

Fix smooth localisers Φ_0 = Op(φ_0) and Φ_E = Op(φ_E), carried by χ, with φ_0, φ_E ∈ C^∞(ᵉ³ᵇT̄*M̃), φ_0 = 1 near K_1,
φ_E = 1 near K_E, supp φ_0 ∩ ᵉ³ᵇS*M̃ ⊂ Ell(G) and supp φ_E ∩ ᵉ³ᵇS*M̃ ⊂ Ell(E) ∩ Ell(G), and put

    Ǎ_ε := Op(ǎ_ε)Φ_0,     B_ε := Op(b_ε)Φ_0,     E_ε := Op(e_ε)Φ_E.

(iii) For every w ∈ H^(K′)_e3b, where K′ ≥ sup |𝗌| + m + 2 is a fixed integer,

    ς⟨C_(ǎ_ε)w, w⟩ ≤ −‖B_εw‖² + ‖E_εw‖² + C_0‖w‖²_(𝗌−1/2+δ_0),                                           {#eq:ii-a1-4-2}

with C_(ǎ_ε) the operator [[eq:ii-a1-4-1]] for Ǎ = Ǎ_ε and C_0 independent of ε.

Then for every u with χu ∈ H^(−N), Gu ∈ H^(𝗌−κ), GLu ∈ H^(𝗌−m+1) and Eu ∈ H^𝗌, we have B_0u ∈ L², B_0 := Op(b_0)Φ_0, and

    ‖B_0u‖² ≤ C(‖GLu‖²_(𝗌−m+1) + ‖Eu‖²_𝗌 + ‖Gu‖²_(𝗌−1/2+δ_0) + ‖χu‖²_(−N)).                            {#eq:ii-a1-4-3}

*Proof.* Norms are those of L² and of H^𝗍_e3b; C changes from line to line and does not depend on ε or t. The
localisers make every product with disjoint microsupports below have a smooth factor on each side, as
[[prop:ii-a1-2-4]] (e) requires.

*Step 0: microlocalisation.* Choose an auxiliary operator Φ = Op(φ) ((R1) of [[sec:ii-a-8-3]], for G, E, Φ_0 and Φ_E),
carried by χ, with φ = 1 near (supp φ_0 ∪ supp φ_E) ∩ ᵉ³ᵇS*M̃, a compact subset of Ell(G), and supp φ in a closed set
whose intersection with fibre infinity lies in Ell(G). Φ_0 and Φ_E are microsupported in closed neighbourhoods of their
wave front sets on which φ = 1 ([[sec:ii-a1-1-2]]). Put v := Φu. By [[lem:ii-a-8-4]] (c),
‖v‖_𝗍 ≤ C(‖Gu‖_𝗍 + ‖χu‖_(−N)) for 𝗍 ≤ 𝗌 − κ, and ‖ΦLu‖_(𝗌−m+1) ≤ C(‖GLu‖_(𝗌−m+1) + ‖χ_*Lu‖_(−N−m)) with χ_* of
(R2) of [[sec:ii-a-8-3]], for which Φχ_* = Φ and Gχ_* = G; by [[lem:ii-a-8-6]] (a), ‖χ_*Lu‖_(−N−m) ≤ C‖χu‖_(−N). Now
Lv = ΦLu + [L, Φ]u, and [L, Φ]u = [L, Φ]χu by the support convention. Further

    Ǎ_ε[L, Φ] = Op(ǎ_ε)(Φ_0(I − Φ))L − Op(ǎ_ε)(Φ_0L(I − Φ)).

Φ_0(I − Φ) ∈ Ψ̃^(−∞) ([[lem:ii-a1-1-2]]; I − Φ is Op(1 − φ) up to a residual operator, by [[eq:ii-a1-1-1]]), and
Φ_0L(I − Φ) has every order by [[prop:ii-a1-2-4]] (e), Φ_0 and I − Φ being microsupported in disjoint closed sets, a
neighbourhood of WF′(Φ_0) on which φ = 1 and supp(1 − φ), with
L = Op(ℓ_f) + Σ_j a_jR_j ([[eq:ii-a1-1-2]]). Op(ǎ_ε) is bounded of order 𝗄 uniformly in ε ([[prop:ii-a1-2-4]] (a)),
and L maps H^(−N) to H^(−N−m) ([[lem:ii-a-8-6]] (a)). Hence

    ‖Ǎ_εLv‖_((1−m)/2) ≤ C(‖GLu‖_(𝗌−m+1) + ‖χu‖_(−N)).                                                    {#eq:ii-a1-4-4}

*Step 1: the pairing at v.* Let w_t := T_tv, with T_t from [[lem:ii-a1-2-3]] (b) and K ≥ K′ + sup |𝗌| + 1, so that
w_t ∈ H^(𝗌−κ+K) ⊂ H^(K′) for t > 0. We show ⟨Ǎ_εLw_t, Ǎ_εw_t⟩ → ⟨Ǎ_εLv, Ǎ_εv⟩ as t → 0, for fixed ε > 0.
Symbols of C^((M))_ν S̃^𝗄 act with exact orders ([[prop:ii-a1-2-4]] (a)), and only remainders lose δ. So Ǎ_ε has
order 𝗄 − κ for this ε, and as v ∈ H^(𝗌−κ), Ǎ_εw_t → Ǎ_εv strongly in H^((m−1)/2). Next, Ǎ_εLw_t = Ǎ_εT_tLv +
Ǎ_ε[L, T_t]v. The first term tends to Ǎ_εLv in H^((1−m)/2): T_t → I strongly on H^(𝗌−m+1), applied to ΦLu; the part
with [L, Φ]u is handled as in Step 0, uniformly in t, with Φ_0T_t(I − Φ) and Φ_0T_tL(I − Φ) in place of Φ_0(I − Φ)
and Φ_0L(I − Φ) ([[prop:ii-a1-2-4]] (e) with the expressions T_t and T_tL, τ_t being bounded in S̃⁰). For the second,
L and T_t have the constant orders m and 0. So [[prop:ii-a1-2-4]] (d), with a_1 = ℓ_f and a_2 = τ_t bounded in S̃⁰,
shows that [L, T_t] is bounded of order m − 1, uniformly in t; and it tends to 0 as an operator of order m − 1 + δ,
since τ_t → 1 in S̃^δ. Hence Ǎ_ε[L, T_t]v is bounded in H^((1−m)/2) uniformly in t and tends to 0 in 𝒟′, so weakly in
H^((1−m)/2). A weakly null sequence paired with a strongly convergent one tends to 0.

*Step 2: the inequality at v.* Apply [[eq:ii-a1-4-2]] at w = w_t and let t → 0. The pairing converges by Step 1. The
other terms converge: E_ε has order at most 𝗌 − κ, 𝗌 − 1/2 + δ_0 ≤ 𝗌 − κ, and T_t → I strongly on H^(𝗌−κ).
B_εw_t → B_εv in H^(−δ), B_ε having order 𝗌 − κ + δ for this ε. Since ‖B_εw_t‖² is bounded by the convergent right
side, B_εv ∈ L², and by weak lower semicontinuity

    ‖B_εv‖² ≤ −2ς Im⟨Ǎ_εLv, Ǎ_εv⟩ + ‖E_εv‖² + C_0‖v‖²_(𝗌−1/2+δ_0).

(a) Ǎ_ε = Op(z_ε)B_ε + D_ε with D_ε := (Op(z_εb_ε) − Op(z_ε)Op(b_ε))Φ_0, by the exact identity ǎ_ε = z_εb_ε; by
[[prop:ii-a1-2-4]] (b), D_ε is bounded of order 𝗄 − 1 + 2δ. As Op(z_ε) is bounded of
order −(m − 1)/2 without loss ([[prop:ii-a1-2-4]] (a)), ‖Ǎ_εv‖_((m−1)/2) ≤ C‖B_εv‖ + C‖v‖_(𝗌−1+2δ). With
[[eq:ii-a1-4-4]],

    2|⟨Ǎ_εLv, Ǎ_εv⟩| ≤ (1/2)‖B_εv‖² + C(‖GLu‖²_(𝗌−m+1) + ‖v‖²_(𝗌−1/2) + ‖χu‖²_(−N)).

(b) E_εv = E_εu − Op(e_ε)(Φ_E(I − Φ))χu, and Φ_E(I − Φ) ∈ Ψ̃^(−∞) ([[lem:ii-a1-1-2]]), so the second term is bounded by
C‖χu‖_(−N), uniformly. For the first, E is elliptic on the essential support of φ_E, so the parametrix construction of
[[lem:ii-a-8-4]] (b), carried out in the smooth calculus Ψ̃ of ρℬ, to which (S5) applies, gives Φ_E = Q_EE + R_E with
Q_E ∈ Ψ̃⁰ and R_E ∈ Ψ̃^(−J), J ≥ sup 𝗌 + N. Then R_Eχ = R_E, as Φ_Eχ = Φ_E and Eχ = E, the two being carried by χ;
no property of the kernel of Q_E is used. As Op(e_ε) is bounded of order 𝗌 uniformly,
‖E_εu‖ ≤ ‖Op(e_ε)Q_EEu‖ + ‖Op(e_ε)R_Eχu‖ ≤ C(‖Eu‖_𝗌 + ‖χu‖_(−N)).

(c) ‖v‖_(𝗌−1/2+δ_0) ≤ C(‖Gu‖_(𝗌−1/2+δ_0) + ‖χu‖_(−N)), by [[lem:ii-a-8-4]] (c).

Absorbing (1/2)‖B_εv‖², which is finite,

    ‖B_εv‖² ≤ C(‖GLu‖²_(𝗌−m+1) + ‖Eu‖²_𝗌 + ‖Gu‖²_(𝗌−1/2+δ_0) + ‖χu‖²_(−N))     for all ε ∈ (0, 1].

*Step 3: the limit.* B_εv → B_0v in 𝒟′ ([[prop:ii-a1-2-4]] (a) and the proof of its finite regularity part, as
b_ε → b_0 pointwise with uniform bounds in the class of order 𝗌 + δ). B_εv is bounded in L², so B_0v ∈ L² with the same
bound. Finally B_0u = B_0v + Op(b_0)(Φ_0(I − Φ))χu, and Φ_0(I − Φ) ∈ Ψ̃^(−∞). ∎

The a priori hypothesis Gu ∈ H^(𝗌−κ) is used only for the limits t → 0; the bound uses ‖Gu‖_(𝗌−1/2+δ_0).

**Lemma {#lem:ii-a1-4-2}** (Iteration.) Let Γ ⊂ ᵉ³ᵇS*M̃ be compact and U_0 an open neighbourhood of it. Suppose that for
every κ ∈ (0, 1/4], every order 𝗌′ = 𝗌 − τ′ with 0 ≤ τ′ ≤ τ (τ > 0 a constant), and every open U with Γ ⊂ U ⊂ U_0, the
hypotheses of [[lem:ii-a1-4-1]] hold for (𝗌′, κ), for some localisers Φ_0, Φ_E as there, with K_1, supp φ_0 and
supp φ_E inside U (near fibre infinity), with e_ε and φ_E supported in a closed set K_E(U) whose intersection with fibre
infinity lies in U ∖ Γ, and with b_0 elliptic of order 𝗌′ on an open
neighbourhood U′ of Γ: b_0⁻¹ ∈ C^((M))_ν S̃^(−𝗌′) on U′ near fibre infinity. Let G be elliptic on Ū_0. Then there are
a neighbourhood U_* of Γ and a closed set K_E^* missing Γ such that, for E elliptic on K_E^* and B ∈ C^∞_b Ψ⁰_e3b
carried by χ and microsupported in U_*, in the strong sense,

    ‖Bu‖_𝗌 ≤ C(‖GLu‖_(𝗌−m+1) + ‖Eu‖_𝗌 + ‖Gu‖_(𝗌−τ) + ‖χu‖_(−N)).                                         {#eq:ii-a1-4-5}

*Proof.* As in the proof of [[lem:i-a-3-2]]. Take an integer J > 4τ, κ := τ/J < 1/4, and 𝗌_j := 𝗌 − τ + jκ. Construct
open sets U_0 ⊃ U_1 ⊃ ⋯ ⊃ U_J ⊃ Γ with Ū_j ⊂ U′_j ∩ U_(j−1), where U′_j is the U′ for (𝗌_j, κ, U_(j−1)), and let
K_E^* := ⋃_j K_E(U_(j−1)). Let G_0 := G and G_j := Op(g_j), carried by χ, with g_j smooth on the compactified bundle,
equal to 1 near Ū_j and supported in U′_j ∩ U_(j−1), where b_0^((j)) is elliptic and G_(j−1) is elliptic; so
WF′(G_j) ⊂ U_0 ⊂ Ell(G), which the step from ‖G_(j−1)Lu‖ to ‖GLu‖ and the next step need. Then
‖G_ju‖_(𝗌_j) ≤ C(‖B_0^((j))u‖ + ‖χu‖_(−N)). This is the parametrix argument of the proof of [[thm:ii-a1-3-1]], with
B_0^((j)) = Op(b)Φ_0, b := b_0^((j)) and Φ_0 := Φ_0^((j)), of order 𝗌_j + δ, in place of L, and q := χ̃ab⁻¹ in place of
χ̃aℓ⁻¹. As φ_0 = 1 on supp b ⊃ U′_j ⊃ supp χ̃, the identity qbφ_0 = χ̃a = a of symbols is exact, so

    Op(q)B_0^((j)) − A = (Op(q)Op(b) − Op(qb))Φ_0 + (Op(qb)Φ_0 − Op(qbφ_0)) − R_A

has order 𝗋 − 1 + 2δ by [[prop:ii-a1-2-4]] (b). Op(q) has order 𝗋 − 𝗌_j without loss ([[prop:ii-a1-2-4]] (a)), so
with δ = 1/4 the iteration closes as there, with the localisation by G_(i+1) and I − G_(i+2) and [[prop:ii-a1-2-4]] (e)
for the remainders; B_0^((j))u ∈ L² enters without localization. (With an operator of order −𝗌_j + δ in place of the
parametrix, the conclusion would be H^(𝗌_j−δ) only.) [[lem:ii-a1-4-1]] at step j needs G_(j−1)u ∈ H^(𝗌_(j−1)), the
conclusion of step j − 1, and gives

    ‖B_0^((j))u‖ ≤ C(‖G_(j−1)Lu‖_(𝗌_j−m+1) + ‖Eu‖_(𝗌_j) + ‖G_(j−1)u‖_(𝗌_j−1/2+δ_0) + ‖χu‖_(−N)).

Take δ_0 ≤ 1/4 − κ, which is positive as J > 4τ, so that 𝗌_j − 1/2 + δ_0 ≤ 𝗌_(j−1). [[lem:ii-a1-4-1]] at step j
applies with G_(j−1) in the role of G, which is elliptic on Ū_(j−1) ⊃ K_1 ∪ supp φ_0 ∪ supp φ_E near fibre infinity,
and with E, which is elliptic on K_E^* ⊃ K_E(U_(j−1)) ⊃ supp φ_E near fibre infinity. Induction on j
bounds ‖G_Ju‖_𝗌, and [[eq:ii-a1-4-5]] follows for B microsupported in U_* := U_J by [[lem:ii-a-8-4]] (c). ∎

### Real principal type propagation {#sec:ii-a1-5}

This section constructs the commutant of [[sec:ii-a1-4]] along a single integral curve of the Hamilton vector field,
in flow-box coordinates of finite regularity, and assembles the global estimate.

#### The operator and its Hamilton vector field {#sec:ii-a1-5-1}

Let m ∈ ℕ_0, and let L = L_0 + L_1 + L_2 on ℂ^(N′), where L_0 ∈ Diff^m_e3b ⊗ Id, L_1 = Σ_q a_qP_q ⊗ Id with
a_q ∈ C^(d_0,(2δ_w,δ_w,δ_w))_e3b, δ_w > 0, and P_q ∈ 𝒫_m with classical principal symbols, and
L_2 ∈ C^(d_0)_e3b 𝒫_(m−1) ⊗ End ℂ^(N′); here 𝒫_(m−j) ⊂ C^∞_b Ψ^(m−j)_e3b, j = 0, 1, are finite. The scalar principal
symbol ℓ = ℓ_0 + ℓ_1 is real, with ℓ_0 := σ(L_0) and ℓ_1 := Σ_q a_qσ(P_q) homogeneous of degree m. Put
𝖧 := ρ_∞^(m−1)H_ℓ, homogeneous of degree 0, and μ := ρ_∞^(−(m−1)), so that H_ℓ = μ𝖧 on functions homogeneous of
degree 0.

**Lemma {#lem:ii-a1-5-1}** (a) 𝖧 induces a vector field on ᵉ³ᵇS*M̃, tangent to its boundary faces, that is continuous
over M̃ ∖ (I⁰ ∪ K⁻). Over ℐ⁺ ∪ ι⁺ ∪ K⁺ it equals ρ_∞^(m−1)H_(ℓ_0).

(b) In the charts of ρℬ, with coordinates (x, ω) on the cosphere bundle, its coefficients have derivatives up to order
d_0 − 1 bounded uniformly.

(c) Over the interior its integral curves are unique and exist for all times. Over M̃ ∖ (I⁰ ∪ K⁻) its integral curves
are unique and preserve the boundary faces, and its flow is continuous and depends continuously on the field: if such
fields 𝖧_n converge to 𝖧 uniformly on compact sets there, their integral curves from points converging to β converge to
that of 𝖧 from β, uniformly on compact time intervals on which it stays there. For |t| ≤ T_0, the flow maps have
derivatives up to order d_0 − 1 bounded in these charts, uniformly.

*Proof.* (a), (b). ρ_∞^(m−1)H_(ℓ_0) is smooth on ᵉ³ᵇS*M̃ and tangent to its faces: ℓ_0 is classical, and Hamilton
vector fields of e3b-symbols are b-vector fields on the compactified bundle ([Hin26c, p. 71 and (2.39)];
[[sec:ii-a-2-5]]). Write ℓ_1 = wℓ̃_1 with w := x_I^(2δ_w) ρ_+^(δ_w) ρ_K^(δ_w) and ℓ̃_1 := Σ_q ã_qσ(P_q),
ã_q := w⁻¹a_q ∈ C^(d_0)_e3b. Then H_(ℓ_1) = wH_(ℓ̃_1) + ℓ̃_1H_w. Here H_w is w times a fibre vector field whose
coefficients are e3b-derivatives of log w, which are smooth on M̃. In the charts of ρℬ the coordinate vector fields are,
uniformly, bounded combinations of b-vector fields of the compact manifold. They are lifts of e3b-vector fields and
fibre vector fields, magnified at the boundary as in [[lem:ii-a1-1-2]]. So ρ_∞^(m−1)H_(ℓ_1) is w times a combination of
b-vector fields of ᵉ³ᵇS*M̃ with coefficients that are bounded with d_0 − 1 derivatives in those charts. As w → 0 at ℐ⁺,
ι⁺ and K⁺, this part tends to 0 there, and b-vector fields are tangent to the faces. At I⁰ and K⁻ the weight need not
vanish, and 𝖧 need not be continuous there.

(c) In the charts of ρℬ the field is uniformly C^(d_0−1), hence uniformly Lipschitz, so its integral curves over the
interior are unique. They exist for all times, since in logarithmic coordinates the faces lie at infinity and the field
is bounded there. On the faces ℐ⁺, ι⁺ and K⁺ the field is the smooth tangent field above. A curve γ through a point of
such a face F stays in F: for a defining function ρ_F, 𝖧ρ_F = βρ_F with β bounded near F, both parts of 𝖧 being
combinations of b-vector fields with bounded coefficients; so f := ρ_F ∘ γ satisfies |f′| ≤ C|f| and f(0) = 0, whence
f ≡ 0 by Gronwall's inequality. Within F, and within each corner, the field is smooth, so curves through boundary points
are unique too. The fields are bounded and continuous over M̃ ∖ (I⁰ ∪ K⁻). By the theorem of Arzelà and Ascoli, integral
curves of fields 𝖧_n as in (c), from points β_n → β, have subsequences converging uniformly on compact time intervals,
and the limits are integral curves of 𝖧 from β. They equal the unique one, so the whole sequence converges. The bounds on
derivatives of the flow maps follow from Gronwall's inequality applied to the variational equations, uniformly in the
charts. ∎

**Lemma {#lem:ii-a1-5-2}** (Flow box.) Let γ : [a, b] → ᵉ³ᵇS*M̃ be an injective integral curve of 𝖧 with 𝖧 ≠ 0 on it.
There are a neighbourhood O of γ([a, b]) and functions z, y_1, …, y_8 on O with the following properties. (z, y) maps O
homeomorphically onto (a − 3δ′, b + 3δ′) × B, where B is a neighbourhood of 0 in ℝ⁸, intersected with a closed quadrant
when γ lies in boundary faces. 𝖧z = 1, 𝖧y_i = 0 and γ(t) = (t, 0). On O ∩ ᵉ³ᵇS*M̃°, z and y have derivatives up to
order d_0 − 1 bounded in the charts of ρℬ, uniformly. (ᵉ³ᵇS*M̃ has dimension 2 · 5 − 1 = 9.)

*Proof.* γ extends to an integral curve on [a − 4δ′, b + 4δ′]. Choose a smooth function σ near p_0 := γ(a − 2δ′) with
σ(p_0) = 0 and 𝖧σ(p_0) ≠ 0, and smooth ỹ_1, …, ỹ_8 such that (σ, ỹ) is a chart of the compact manifold with corners at
p_0, adapted to its faces. For p near γ, let z(p) be the time t near the expected value with
σ(exp(−(t − a + 2δ′)𝖧)p) = 0, and y(p) := ỹ(exp(−(z(p) − a + 2δ′)𝖧)p). By continuity 𝖧σ ≥ c > 0 near p_0, and the
implicit function theorem gives z locally. The derivative of z is (dσ · D exp · ∂)/(dσ · 𝖧), and similarly for y. In
the charts of ρℬ, dσ and dỹ are bounded with all derivatives (smooth functions on the compact manifold, as in
[[lem:ii-a1-1-1]]), and D exp is bounded with d_0 − 2 further derivatives ([[lem:ii-a1-5-1]] (c)). So z and y have
d_0 − 1 bounded derivatives. Faces are invariant, so y maps them to coordinate faces. Injectivity of (z, y) on a
neighbourhood follows from the injectivity of γ and of ỹ on the slice {σ = 0}, by the usual compactness argument for a
curve that meets the slice once. 𝖧z = 1 and 𝖧y = 0 hold by construction. ∎

#### Propagation along one curve {#sec:ii-a1-5-2}

**Proposition {#prop:ii-a1-5-3}** Let ς ∈ {1, −1} and 𝖧_f := ς𝖧 (the forward field). Let γ : [0, T] → ᵉ³ᵇS*M̃ be an
injective integral curve of 𝖧_f with 𝖧_f ≠ 0 on it (it need not lie in Char(L); the proof does not use it). Let 𝗌 be a
variable order with 𝖧_f𝗌 ≤ 0 on a neighbourhood of γ([0, T]) in ᵉ³ᵇS*M̃, and let E be elliptic at γ(0). Then there are
B ∈ C^∞_b Ψ⁰_e3b, elliptic on γ([0, T]), and G, both microsupported in any given neighbourhood of γ([0, T]) (near fibre
infinity, and carried by χ), such that in the strong sense

    ‖Bu‖_𝗌 ≤ C(‖GLu‖_(𝗌−m+1) + ‖Eu‖_𝗌 + ‖χu‖_(−N)).                                                       {#eq:ii-a1-5-1}

C depends on L only through finitely many norms of its coefficients and the geometry of the flow near γ. It is uniform
for perturbations of L small in those norms, for which the hypotheses hold with the same neighbourhood of γ.

*Proof.* Apply [[lem:ii-a1-5-2]] to the curve t ↦ γ(ςt) of 𝖧, or equivalently use coordinates with 𝖧_f = ∂_z and
γ(t) = (t, 0) on a neighbourhood O of γ([−4δ′, T + 4δ′]). Extend z and y to a conic neighbourhood in ᵉ³ᵇT*M̃,
homogeneously of degree 0. Let ψ be the cut-off of [[sec:i-a-3]]: ψ is even, supported in (−1, 1), equal to 1 on
[−1/2, 1/2], nonincreasing on [0, ∞), and −ψψ′ is the square of a smooth function on [0, ∞). Put χ_s(z) := ψ(−z/δ) for
z ≤ 0 and χ_s(z) := 1 for z ≥ 0, and χ_e(z) := ψ((z − T)/δ) for z ≥ T and χ_e(z) := 1 for z ≤ T. These are smooth, as
ψ = 1 near 0, and χ_s = χ_e = 1 on [0, T]. So ∂_z(χ_s²) = (2/δ)(−ψψ′)(−z/δ) ≥ 0 is supported in [−δ, −δ/2], and
−∂_z(χ_e²) ≥ 0 in [T + δ/2, T + δ]; both are squares of smooth functions of z. (With ψ even, ψ(−z/δ) alone vanishes for
z ≥ δ, and neither statement would hold.) Put ψ_y := ψ(|y|²/δ_1²). Choose δ ≤ δ′/2 and δ_1 so small that
{z ∈ [−2δ, T + 2δ], |y| ≤ 2δ_1} lies in the given neighbourhood, in O and in the set where 𝖧_f𝗌 ≤ 0, and that
{z ∈ [−2δ, 0], |y| ≤ 2δ_1} ⊂ Ell(E) (the margin serves the uniformity below). Let χ_∞ be a function of ρ_∞ equal to 1
near fibre infinity and supported where (z, y) are defined and in {ρ_∞ < 1}, so that log ρ_∞ < 0 on its support. Its
derivatives are supported in a set compact in the fibres, where every symbol has order −∞.

*Commutant.* With 𝗄 := 𝗌 − (m − 1)/2 (the restriction to fibre infinity), the regulariser φ_ε of [[sec:ii-a1-2-3]] with
exponent κ, and a large constant M, put

    ǎ_ε := χ_∞ ρ_∞^(−𝗄) φ_ε e^(−Mz) χ_s(z) χ_e(z) ψ_y.

Its factors other than ρ_∞^(−𝗄)φ_ε have d_0 − 1 bounded derivatives ([[lem:ii-a1-5-2]]), so ǎ_ε is bounded in
C^((d_0−1)) S̃^𝗄 (index 0), and lies in C^((d_0−1)) S̃^(𝗄−κ) for each ε. Since 𝖧_fz = 1 and 𝖧_fψ_y = 0,
[[eq:ii-a1-2-1]] gives, where χ_∞ = 1,

    𝖧_f(ǎ_ε²) = ρ_∞^(−2𝗄) φ_ε² ψ_y² e^(−2Mz) [−χ_s²χ_e² Q_ε + χ_e² ∂_z(χ_s²) + χ_s² ∂_z(χ_e²)],
    Q_ε := 2M + 2𝗄_ε ρ_∞⁻¹ 𝖧_fρ_∞ + 2(𝖧_f𝗄) log ρ_∞,     𝗄_ε := 𝗄 − κθ_ε.

On the support, 𝖧_f𝗄 = 𝖧_f𝗌 ≤ 0 and log ρ_∞ < 0, so the last term of Q_ε is nonnegative. These two signs hold on the
set W where (z, y) are defined, 𝖧_f𝗌 ≤ 0 and ρ_∞ < 1, a neighbourhood of the box
{z ∈ [−2δ, T + 2δ], |y| ≤ 2δ_1} ∩ supp χ_∞; off W, Q_ε need not be positive, nor even defined. Fix
ζ ∈ C^∞(ᵉ³ᵇT̄*M̃) with values in [0, 1], equal to 1 near that box and supported in W, and choose
M ≥ 1 + sup_(supp ζ) |2𝗄_ε ρ_∞⁻¹ 𝖧_fρ_∞|, uniformly in ε as 𝗄_ε ∈ (𝗄 − κ, 𝗄]. Then Q_ε ≥ M on supp ζ; M will be enlarged
once more below. Put

    Q̃_ε := ζQ_ε + (1 − ζ)M = Q̃_(0,ε) + ζλ,     Q̃_(0,ε) := ζQ_(0,ε) + (1 − ζ)M,

with Q_(0,ε) := 2M + 2𝗄_ε ρ_∞⁻¹ 𝖧_fρ_∞ and λ := 2(𝖧_f𝗄) log ρ_∞. Then Q̃_ε is defined on all of phase space,
Q̃_(0,ε) ≥ M and ζλ ≥ 0 everywhere, so Q̃_ε ≥ M everywhere, and Q̃_ε = Q_ε near the box. Q̃_(0,ε) has d_0 − 2 bounded
derivatives, and ζλ has d_0 − 2 derivatives bounded by C⟨log ρ_∞⟩, uniformly in ε ([[lem:ii-a1-5-1]] (b),
[[def:ii-a1-1-3]], and [[lem:ii-a1-1-1]] for ζ). By [[lem:ii-a1-2-5]] (ii) with ν = 0, Q̃_ε^(−1/2) is bounded in
C^((d_0−2))_1 S̃⁰ and Q̃_ε^(1/2) in C^((d_0−2))_1 S̃^δ for every δ > 0. Put

    b_ε := μ^(1/2) ρ_∞^(−𝗄) φ_ε ψ_y e^(−Mz) χ_s χ_e Q̃_ε^(1/2) χ_∞,
    b_(e,ε) := μ^(1/2) ρ_∞^(−𝗄) φ_ε ψ_y e^(−Mz) χ_s (−∂_z(χ_e²))^(1/2) χ_∞,
    e_ε := μ^(1/2) ρ_∞^(−𝗄) φ_ε ψ_y e^(−Mz) χ_e (∂_z(χ_s²))^(1/2) χ_∞,
    z_ε := μ^(−1/2) Q̃_ε^(−1/2).

Then ςH_ℓ(ǎ_ε²) = μ𝖧_f(ǎ_ε²) = −b_ε² − b_(e,ε)² + e_ε² modulo symbols of order −∞ (from χ_∞), as Q̃_ε = Q_ε on the
supports, and ǎ_ε = z_εb_ε exactly, on all of phase space. The factor μρ_∞^(−2𝗄) has order 2𝗌. So, all with index 1
and d_0 − 2 derivatives, b_ε is bounded in the class of order 𝗌 + δ for every δ > 0 (the factor Q̃_ε^(1/2)), e_ε and
b_(e,ε) in that of order 𝗌, and z_ε, a global symbol, in that of order −(m − 1)/2, on which it acts without loss
([[prop:ii-a1-2-4]] (a)). e_ε is supported in {z ∈ [−δ, −δ/2]}, inside Ell(E) and away from γ([0, T]). b_0 is elliptic
on γ([0, T]), where χ_s = χ_e = ψ_y = 1 and Q̃_0 ≥ M: on the open set U′ := {z ∈ (−δ/2, T + δ/2), |y|² < δ_1²/2}, near
fibre infinity, b_0⁻¹ = ρ_∞^𝗌 e^(Mz) Q̃_0^(−1/2) lies in C^((d_0−2))_1 S̃^(−𝗌).

*Localisers.* The symbols ǎ_ε, b_ε and b_(e,ε) are supported in the closed set
K_1 := {z ∈ [−δ, T + δ], |y| ≤ δ_1} ∩ supp χ_∞, and e_ε in K_E := {z ∈ [−δ, −δ/2], |y| ≤ δ_1} ∩ supp χ_∞. Choose
localisers Φ_0 = Op(φ_0) and Φ_E = Op(φ_E) as in [[lem:ii-a1-4-1]], carried by χ, with φ_0 = 1 near the box
{z ∈ [−2δ, T + 2δ], |y| ≤ 2δ_1} ∩ supp χ_∞, and φ_E = 1 near {z ∈ [−3δ/2, −δ/4], |y| ≤ 3δ_1/2} ∩ supp χ_∞ and
supported, near fibre infinity, in {z ∈ [−7δ/4, −δ/8], |y| ≤ 7δ_1/4}. Both are supported, near fibre infinity, in the
given neighbourhood of γ([0, T]) and in Ell(G), and φ_E also in Ell(E), as {z ∈ [−2δ, 0], |y| ≤ 2δ_1} ⊂ Ell(E); and
supp φ_E misses γ([0, T]) ⊂ {z ≥ 0} (the margins serve the uniformity below). Put

    Ǎ := Ǎ_ε := Op(ǎ_ε)Φ_0,     B_ε := Op(b_ε)Φ_0,     B_(e,ε) := Op(b_(e,ε))Φ_0,     E_ε := Op(e_ε)Φ_E.

Then φ_0ǎ_ε = ǎ_ε, φ_0b_ε = b_ε, φ_0b_(e,ε) = b_(e,ε) and φ_Ee_ε = e_ε exactly. Every operator identity below is an
instance of [[prop:ii-a1-2-4]] (b)–(d), (f) for a fixed expression, combined with these exact identities of symbols; so
its remainder has the stated order, with an index that depends only on the orders ([[sec:ii-a1-1]], *Indices*).

*The commutator.* Write L = Op(ℓ_f) + R_L by [[eq:ii-a1-1-2]], with R_L of every order. Let ℓ_R := (ℓ_f + ℓ_f^*)/2 and
ℓ_I := (ℓ_f − ℓ_f^*)/(2i). Since ℓ is real and scalar, ℓ_R − ℓ Id and ℓ_I have order m − 1. Then L_R = Op(ℓ_R) + D_R and
L_I = Op(ℓ_I) + D_I, where D_R and D_I are ±1/2 and ±1/(2i) times D_(ℓ_f) of [[prop:ii-a1-2-4]] (f), plus the parts of
R_L. So L_I has exact order m − 1, and [D_R, Ǎ], [D_I, Ǎ] have order m + 𝗄 − 2 + δ, uniformly in ε. Now
i[L_R, Ǎ²] = i[L_R, Ǎ]Ǎ + Ǎ i[L_R, Ǎ], and by [[prop:ii-a1-2-4]] (d) and the above, i[L_R, Ǎ] = Op(H_(ℓ_R)ǎ) plus order
m + 𝗄 − 2 + δ (the principal symbol of i[Op(ℓ_R), Op(ǎ)Φ_0] being H_(ℓ_R)(ǎφ_0) = H_(ℓ_R)ǎ). Next,
H_(ℓ_R)ǎ = (H_ℓǎ) Id + H_(ℓ_R−ℓ)ǎ, where the second term has
order m + 𝗄 − 2. With [[prop:ii-a1-2-4]] (b), i[L_R, Ǎ²] is Op(H_ℓ(ǎ²)) plus order 2𝗌 − 1 + δ. Further,
Ǎ*Ǎ = Ǎ² + D_ǎǍ with D_ǎ := Ǎ* − Ǎ of order 𝗄 − 1 + δ ([[prop:ii-a1-2-4]] (c), ǎ real), and i[L_R, D_ǎǍ] has order
2𝗌 − 1 + δ by [[prop:ii-a1-2-4]] (f). So

    i[L_R, Ǎ*Ǎ] = Op(H_ℓ(ǎ²)) + R_1,     R_1 of order 2𝗌 − 1 + δ.

For L_I, formally self-adjoint,

    ⟨(L_IǍ*Ǎ + Ǎ*ǍL_I)w, w⟩ = 2 Re⟨ǍL_Iw, Ǎw⟩ = 2 Re⟨L_IǍw, Ǎw⟩ + 2 Re⟨Ǎ*[Ǎ, L_I]w, w⟩,

and Ǎ*[Ǎ, L_I] has order 2𝗌 − 1 + δ, by [[prop:ii-a1-2-4]] (d) for Op(ℓ_I) and (f) for D_I. Collecting, by
[[eq:ii-a1-4-1]], for w ∈ H^(K′),

    ς⟨C_ǎw, w⟩ = Re⟨Op(ςH_ℓ(ǎ²))w, w⟩ + 2ς Re⟨L_IǍw, Ǎw⟩ + Re⟨R_2w, w⟩,

where R_2 has order 2𝗌 − 1 + δ, so that |⟨R_2w, w⟩| ≤ C‖w‖²_(𝗌−1/2+δ). No microlocalisation of the remainders is
needed, the error term of [[eq:ii-a1-4-2]] being a global norm.

*Positivity.* By [[prop:ii-a1-2-4]] (b), (c), Φ_0^*Op(b_ε)^*Op(b_ε)Φ_0 − Op(φ_0b_ε²φ_0) has order 2𝗌 − 1 + 2δ, and
φ_0b_ε²φ_0 = b_ε²; so Op(b_ε²) = B_ε^*B_ε + (order 2𝗌 − 1 + 2δ). Likewise for b_(e,ε) with Φ_0 and for e_ε with Φ_E.
The symbol ςH_ℓ(ǎ²) + b_ε² + b_(e,ε)² − e_ε² is supported where χ_∞ is not locally constant, a set compact in the
fibres, so its quantization has every order. So

    Re⟨Op(ςH_ℓ(ǎ²))w, w⟩ ≤ −‖B_εw‖² + ‖E_εw‖² + C‖w‖²_(𝗌−1/2+δ),

dropping −‖B_(e,ε)w‖² ≤ 0. For the L_I term, fix elliptic operators Λ_± of orders ±(m − 1)/2 defining the norms of
H^(±(m−1)/2), and let C_I be the norm of L_I between these spaces. It depends on finitely many norms of the coefficients
and not on M or ε. Take Λ_+ := Op(λ_+) with λ_+ classical. Then Λ_+Ǎ = Op(λ_+z_ε)B_ε + (order 𝗌 − 1 + 2δ)
([[prop:ii-a1-2-4]] (b), with ǎ_ε = z_εb_ε), where λ_+z_ε ∈ C^((d_0−2))_1 S̃⁰. Its supremum is at most C_ΛM^(−1/2), with
C_Λ := sup |λ_+μ^(−1/2)|, as Q̃_ε ≥ M on all of phase space. [[lem:ii-a1-2-6]] with η := M⁻¹ and δ/2 in place of
δ, applied to B_εw, and (a + b)² ≤ 2a² + 2b² give

    ‖Ǎw‖²_((m−1)/2) ≤ 2(C_Λ² + 1)M⁻¹‖B_εw‖² + C‖w‖²_(𝗌−1/2+δ),

where ‖B_εw‖_(−1/2+δ/2) ≤ C‖w‖_(𝗌−1/2+δ), b_ε being bounded in the class of order 𝗌 + δ/2. Enlarge M so that
4C_I(C_Λ² + 1)M⁻¹ ≤ 1/2. Then

    ς⟨C_(ǎ_ε)w, w⟩ ≤ −(1/2)‖B_εw‖² + ‖E_εw‖² + C‖w‖²_(𝗌−1/2+δ).

This is [[eq:ii-a1-4-2]] for 2^(−1/2)b_ε, e_ε and 2^(1/2)z_ε, with δ_0 := δ. The other hypotheses of [[lem:ii-a1-4-1]]
hold by the construction, with d_0 large enough that the norms used are among those available: d_0 − 2 ≥ M′ + 2 for the
M of [[prop:ii-a1-2-4]] at the orders involved and index 1, called M′ here.

*Conclusion.* The hypotheses of [[lem:ii-a1-4-2]] hold with Γ := γ([0, T]). For each U ⊃ Γ shrink δ and δ_1, and the
supports of the localisers, so that the supports lie in U. Take K_E(U) := K_E ∪ supp φ_E, which contains the supports of
the e_ε and of φ_E: its intersection with fibre infinity lies in {z ∈ [−2δ, −δ/8], |y| ≤ 2δ_1} ⊂ Ell(E) ∩ U, which
misses Γ. There is no threshold, so τ is arbitrary. Take τ ≥ sup 𝗌 + N; then ‖Gu‖_(𝗌−τ) ≤ C‖χu‖_(−N), and
[[eq:ii-a1-4-5]] is [[eq:ii-a1-5-1]], with any B ∈ C^∞_b Ψ⁰_e3b carried by χ, microsupported in U_* and elliptic on Γ. On
ℂ^(N′) the commutant is scalar and L_I is matrix-valued; nothing above used a scalar L_I.

The uniformity: all constants are bounded by finitely many norms of the coefficients, by the bounds of
[[lem:ii-a1-5-2]], and by M, δ and δ_1. Let L′ be a perturbation small in C^(d_0), with field 𝖧′, let γ′ be the
integral curve of 𝖧′_f with γ′(T) = γ(T), and build the coordinates (z′, y′) of [[lem:ii-a1-5-2]] for 𝖧′ with the same
slice {σ = 0} and the same ỹ, shifted so that γ′(t) = (t, 0). As 𝖧′ → 𝖧, the integral curves of 𝖧′ from points of the
slice near p_0 converge to those of 𝖧 uniformly on the compact time interval ([[lem:ii-a1-5-1]] (c)). So the
compactness argument for the injectivity in [[lem:ii-a1-5-2]] (a curve meets the slice once) holds uniformly: for 𝖧′
close to 𝖧, (z′, y′) is defined and injective on a fixed neighbourhood of γ([−3δ′, T + 3δ′]), with the derivative bounds
of [[lem:ii-a1-5-2]] uniform, and (z′, y′) → (z, y) uniformly there. The box {z′ ∈ [−δ, T + δ], |y′| ≤ δ_1} then lies in
the box of 𝖧 with 2δ and 2δ_1, which has the properties required above by the choice of the margin, given that
𝖧′_f𝗌 ≤ 0 on the same neighbourhood. With M chosen with a margin too, as the bounds it must exceed depend continuously on
the coefficients, the same δ, δ_1 and M serve, and so do the same ζ and the same localisers once (z′, y′) is within
min(δ/16, δ_1/2) of (z, y). Indeed φ_0 and ζ are 1 near the box of 𝖧 with 2δ and 2δ_1. φ_E is 1 near
{z ∈ [−3δ/2, −δ/4], |y| ≤ 3δ_1/2}, which contains the E-set {z′ ∈ [−δ, −δ/2], |y′| ≤ δ_1} of 𝖧′, as there
z ∈ (−17δ/16, −7δ/16) and |y| < 3δ_1/2. And supp φ_E ⊂ {z ≤ −δ/8} misses γ′([0, T]) ⊂ {z > −δ/16}. ∎

#### The global estimate {#sec:ii-a1-5-3}

**Theorem {#thm:ii-a1-5-4}** (Real principal type propagation; [Hin26c, Proposition 3.24] at k = 0, with the
hypotheses of [[rem:ii-a1-hypotheses]].) Let m ∈ ℕ_0, 𝗌 a variable order and N ∈ ℝ. There is d_0 = d_0(m, 𝗌, N) with
the following property; d_0 does not depend on δ_w, 𝒫_m, 𝒫_(m−1), N′, L, B, E, G or χ. Let L be as in
[[sec:ii-a1-5-1]] with this d_0, for any δ_w > 0, any finite 𝒫_m and 𝒫_(m−1) (the elements of 𝒫_m having classical
principal symbols) and any N′. Let B, E, G ∈ C^∞_b Ψ⁰_e3b be carried by χ, with
supp χ disjoint from I⁰ ∪ K⁻ and WF′(B) ⊂ Ell(G). Suppose:

(A) for every α ∈ WF′(B) ∩ Char(L), the backward integral curve of 𝖧 from α reaches Ell(E) in a time at most T_0,
remaining in Ell(G);

(B) 𝖧𝗌 ≤ 0 on a neighbourhood in ᵉ³ᵇS*M̃ of the union of these backward segments, up to their first entry into
Ell(E).

If χu ∈ H^(−N), GLu ∈ H^(𝗌−m+1) and Eu ∈ H^𝗌, then Bu ∈ H^𝗌 and

    ‖Bu‖_𝗌 ≤ C(‖GLu‖_(𝗌−m+1) + ‖Eu‖_𝗌 + ‖χu‖_(−N)),

with C locally uniform: uniform for perturbations of L small in the norms of [[sec:ii-a1-5-1]] (that is, of L_0, L_1 and
L_2 in Diff^m_e3b, C^(d_0,(2δ_w,δ_w,δ_w))_e3b 𝒫_m and C^(d_0)_e3b 𝒫_(m−1)), with real principal symbols, for which (B)
holds on the same neighbourhood. The proof uses (A) and (B) for L only, and (B) on the same neighbourhood for the
perturbed operator; the perturbed backward curves reach Ell(E) within a slightly larger time, by the continuity of the
flow in the field ([[lem:ii-a1-5-1]] (c)), as in (O) of [[sec:ii-a-9]].

*Proof.* Let α ∈ WF′(B) ∩ Char(L) and t_α := inf{t ≥ 0 : exp(−t𝖧)α ∈ Ell(E)} ≤ T_0. 𝖧 ≠ 0 along the backward curve,
for a stationary point outside Ell(E) would never reach it. Take t′_α slightly larger than t_α with
exp(−t′_α𝖧)α ∈ Ell(E). The curve γ_α(t) := exp((t − t′_α)𝖧)α, t ∈ [0, t′_α], is injective, with t′_α taken below the
infimum of periods if the orbit is periodic. Indeed, a self-intersection would make the orbit periodic with period at
most t′_α, and then the backward curve would have entered Ell(E) at an earlier time. It lies in Char(L), as ℓ is
constant along the flow, and in Ell(G). As the neighbourhood in (B) is open, t′_α can be chosen so that (B) holds on a
neighbourhood of γ_α([0, t′_α]). [[prop:ii-a1-5-3]] with ς = 1 gives B_α ∈ C^∞_b Ψ⁰_e3b elliptic on γ_α([0, t′_α]), in
particular near α, and G_α microsupported in a neighbourhood inside Ell(G). It also gives
‖B_αu‖_𝗌 ≤ C(‖G_αLu‖_(𝗌−m+1) + ‖Eu‖_𝗌 + ‖χu‖_(−N)), and ‖G_αLu‖ ≤ C(‖GLu‖ + ‖χ_*Lu‖_(−N−m)) ≤ C(‖GLu‖ + ‖χu‖_(−N)),
with χ_* of (R2) of [[sec:ii-a-8-3]] for B, E and G, by [[lem:ii-a-8-4]] (c) and [[lem:ii-a-8-6]] (a); here G_α and
the operators G_j of the proof of [[lem:ii-a1-4-2]] are taken as auxiliary operators of (R1) for B, E and G, so that
G_αχ_* = G_α. For α ∈ WF′(B) ∖ Char(L), [[thm:ii-a1-3-1]] gives any B_α ∈ C^∞_b Ψ⁰_e3b elliptic near α and
microsupported in Ell(G) ∩ Ell(L) with ‖B_αu‖_𝗌 ≤ C(‖GLu‖_(𝗌−m) + ‖χu‖_(−N)). By compactness of WF′(B), finitely many
B_(α_i) are jointly elliptic on it: Σ_i B_(α_i)^* B_(α_i) ∈ C^∞_b Ψ⁰_e3b is elliptic of order 0 there, the B_(α_i)
being smooth, as [[lem:ii-a-8-4]] (c) requires. The elliptic estimate ([[lem:ii-a-8-4]] (c), or [[thm:ii-a1-3-1]])
bounds ‖Bu‖_𝗌 by C Σ_i ‖B_(α_i)u‖_𝗌 + C‖χu‖_(−N). The strong sense and the uniformity are those of
[[prop:ii-a1-5-3]] and [[thm:ii-a1-3-1]].

For a small perturbation L′ the same α_i serve. If α_i ∉ Char(L), it lies in Ell(L′) with a comparable bound. If
α_i ∈ Char(L), [[prop:ii-a1-5-3]], which does not ask its curve to be characteristic, applies to the integral curve of
𝖧′ ending at α_i, with the same δ, δ_1 and M and the same shrinkings in [[lem:ii-a1-4-2]] (the last paragraph of the
proof of [[prop:ii-a1-5-3]]). By [[lem:ii-a1-5-1]] (c) that curve stays close to γ_(α_i), and the sets on which its
b_0^((j)) are elliptic contain fixed neighbourhoods of γ_(α_i)([0, t′_(α_i)]); a B_(α_i) microsupported in these serves
for L′ too. The resulting operators remain jointly elliptic on WF′(B), once the B_(α_i) are chosen elliptic on open sets
that still cover WF′(B) when shrunk slightly.

*The index.* The regularity used is that of [[thm:ii-a1-3-1]], of [[lem:ii-a-8-6]] (a) and of [[prop:ii-a1-5-3]]. In
the last, d_0 − 2 ≥ M′ + 2, with M′ the number of [[prop:ii-a1-2-4]] for index 1 at the orders 𝗌, 𝗄 = 𝗌 − (m − 1)/2,
m and those of [[lem:ii-a1-4-2]], whose τ, J and κ are fixed by 𝗌 and N (τ := max(1, sup 𝗌 + N), J the least integer
above 4τ, κ := τ/J); the flow box of [[lem:ii-a1-5-2]] has d_0 − 1 derivatives whatever the curve; [[lem:ii-a1-2-5]]
and [[lem:ii-a1-2-6]] keep the number of derivatives. The curves γ_α, the localisers, the cut-offs and the operators
B_α, G_α, B, E, G enter only through [[prop:ii-a1-2-4]] (e) and exact identities of symbols, hence only the constants.
So d_0 depends only on m, 𝗌 and N. ∎

**Remark {#rem:ii-a1-hypotheses}** (The hypotheses of [[thm:ii-a1-5-4]].) [Hin26c, Proposition 3.24] asks for 𝖧𝗌 ≤ 0
only "in a neighborhood of WF′_e3b(B) ∩ Char_e3b(L) within Char_e3b(L)" (p. 70). That does not suffice. Take L = D_t in
one unit cell, so that 𝖧 = ∂_t, and 𝗌 = 𝗌(t) equal to s_0 near Ell(E) at t ≈ −2 and to s_0 + 10 near WF′(B) at t ≈ 0,
so that 𝖧𝗌 = 0 near WF′(B). Let u = χ(t)v(x), with χ = 1 near the segments and v ∈ H^(s_0) ∖ H^(s_0+ε) microlocally at
a point of {τ = 0}. Every hypothesis of that statement holds and its right side is finite, but Bu ∉ H^𝗌: propagation
does not gain regularity. [[thm:ii-a1-5-4]] asks for 𝖧𝗌 ≤ 0 on a neighbourhood in phase space of the whole backward
segments, the standard form of the hypothesis ([Vas18, Theorem 5.3]; [[prop:i-a-5-2]] (d)). The Hamilton vector field of
[Hin26c] is taken on ᵉ³ᵇS*M̃ ([Hin26c, pp. 54 and 71]), which presupposes principal symbols with a continuous extension
there; so the elements of 𝒫_m are taken classical ([[thm:ii-a1-3-1]] needs no such restriction). [Hin26c, p. 71] takes 𝖧
continuous on all of ᵉ³ᵇS*M̃ because the coefficients of L_1 vanish at ∂M̃; they vanish at the faces ℐ⁺, ι⁺ and K⁺, which
carry the weight, and need not vanish at I⁰ and K⁻. So χ is taken supported away from these two faces, as it is near Ω̄
([[sec:ii-a-1]]), and [[lem:ii-a1-5-1]] (c) supplies the uniqueness of integral curves at the faces, on which the
continuity of the flow rests.

### Estimates on mixed spaces, and their tame versions {#sec:ii-a-9}

Orders: m, N ∈ ℝ, and 𝗌, 𝗌_0 ∈ C^∞(ᵉ³ᵇS*M̃) variable orders; wave front sets, elliptic and characteristic sets are those
of the e3b-calculus, in ᵉ³ᵇS*M̃. Cut-offs are as in [[sec:ii-a-8-3]], and weights are suppressed (see the beginning of
[[sec:ii-a-8]]). For an operator L = Σ a_jP_j of limited regularity, Ell_e3b(L) is the set where its principal symbol
ℓ = Σ a_jσ(P_j) is invertible with inverse bounded by a constant times λ^m, λ the elliptic weight of (S8); on
ℂ^(N′)-valued functions, σ(P_j) is matrix-valued ([[sec:ii-a-4-3]]).

*Choosing auxiliary operators.* Let K ⊂ ᵉ³ᵇS*M̃ be compact and O ⊃ K open, and let K lie over {ϑ ≥ c}, with ϑ, c and
the rules (R1)–(R3) of [[sec:ii-a-8-3]] for the operators of the statement at hand carried by χ (K = WF′(B), for
instance). Then there are auxiliary operators B_1, B_2, … ∈ C^∞_b Ψ⁰_e3b in the sense of (R1), carried by χ and by
χ_1 := h_♭(χ), with K ⊂ Ell(B_1), WF′(B_i) ⊂ Ell(B_(i+1)) and all wave front sets in O. Some B_i may be chosen
microlocally equal to I near K, that is, with WF′(I − B_i) ∩ K = ∅: quantize the symbols f(ϑ)χ̃_i, with
χ̃_i ∈ C^∞(ᵉ³ᵇT̄*M̃), χ̃_1 = 1 near K, χ̃_i = 1 near the support of χ̃_(i−1), and supp χ̃_i ∩ ᵉ³ᵇS*M̃ ⊂ O, and truncate
to range ϵ_ϑ. Every finite chain of such operators fits: only the supports in the fibres are nested, inside the fixed
open set O, while the base factor f(ϑ) and the room ϵ_ϑ are the same for all of them.

The hypotheses of the propagation estimates are open. Let T be the union of the backward segments of the integral
curves of 𝖧 from WF′(B) ∩ Char(L) up to their first entry into Ell(E), and suppose that they reach Ell(E) within a time
T_0, remaining in Ell(G). Then T ⊂ Ell(G) is compact: it is the image under the flow of the set of (α, t) with
0 ≤ t ≤ t_α, t_α the first entry time, and this set is closed because α ↦ t_α is upper semicontinuous, Ell(E) being
open. Moreover:

(O) For every neighbourhood U ⊂ Ell(G) of T there are a neighbourhood U_T ⊂ Ell(G) of T ∪ WF′(B), with
U_T ∩ Char(L) ⊂ U, and compact sets K_E ⊂ Ell(E) and K_U ⊂ U, such that the backward curve from every point of
U_T ∩ Char(L) reaches K_E within time T_0 + 1 and stays in K_U until then. U_T may be replaced by any smaller
neighbourhood of T ∪ WF′(B).

For α ∈ WF′(B) ∩ Char(L) choose t′_α ∈ (t_α, t_α + 1) with exp(−t′_α𝖧)α ∈ Ell(E) and the curve on [0, t′_α] in U,
which is possible as U is open. By the continuity of the flow, every point near exp(−t𝖧)α, 0 ≤ t ≤ t_α, has a backward
curve that stays in a fixed compact neighbourhood in U of exp(−[t, t′_α]𝖧)α up to the time t′_α − t, and then lies in a
fixed compact neighbourhood of exp(−t′_α𝖧)α in Ell(E). Finitely many such neighbourhoods cover the compact set T. Their
union, together with a neighbourhood in Ell(G) of the compact set WF′(B) ∖ U disjoint from Char(L), is U_T. The flow is
continuous although 𝖧 is only continuous at ∂M̃: its integral curves are unique, and limits of integral curves are
integral curves ([[lem:ii-a1-5-1]] (c)). When 𝖧𝗌 ≤ 0 on U, the hypotheses of (L4) below therefore hold for (B′, E′, G′)
whenever WF′(B′) ⊂ U_T, E′ is elliptic on K_E and G′ is elliptic on K_U ∪ WF′(B′). Below, "slightly larger" and
"slightly smaller" operators refer to such choices.

#### The standard estimates {#sec:ii-a-9-1}

The two estimates without b-regularity are [Hin26c, Propositions 3.23 and 3.24] for k = 0 (pp. 69–71), in dimension
4 + 1; their statements do not use the dimension. [Hin26c] proves them by the standard elliptic parametrix and positive
commutator arguments. For variable orders it cites [Vas18, Theorem 5.3], with the sharp Gårding inequality on each unit
cell and a commutant as in [dHUV15], and it takes the coefficient regularity d_0 finite because the arguments use the
boundedness of finitely many operators on a fixed range of spaces. [Hin26d] does not treat propagation (its Section 3.6
says so), and [HJS] has constant differential orders. In this edition the two estimates are [[thm:ii-a1-3-1]] and
[[thm:ii-a1-5-4]], proved in [[sec:ii-a1-1]] to [[sec:ii-a1-5]] without the sharp Gårding inequality. We refer to them
as (L3) and (L4) and recall their content.

(L3) (Elliptic estimate, k = 0; [[thm:ii-a1-3-1]].) There is d_0 = d_0(m, 𝗌, N) such that the following holds for every
finite 𝒫 ⊂ C^∞_b Ψ^m_e3b, every N′ and every L ∈ C^(d_0)_e3b 𝒫 on ℂ^(N′)-valued functions; d_0 depends neither on 𝒫,
N′ and L nor on B, G and χ. Let B, G ∈ C^∞_b Ψ⁰_e3b be carried by χ, with WF′(B) ⊂ Ell(G) ∩ Ell(L). If
χu ∈ H^(−N)_e3b and GLu ∈ H^(𝗌−m)_e3b, then Bu ∈ H^𝗌_e3b and

    ‖Bu‖_(H^𝗌_e3b) ≤ C(‖GLu‖_(H^(𝗌−m)_e3b) + ‖χu‖_(H^(−N)_e3b)),

with C uniform for L in a neighbourhood in C^(d_0)_e3b 𝒫 on which WF′(B) ⊂ Ell(L) holds with a uniform bound.

(L4) (Real principal type propagation, k = 0; [[thm:ii-a1-5-4]].) Let m ∈ ℕ_0. There is d_0 = d_0(m, 𝗌, N) such that
the following holds for every δ > 0, all finite sets 𝒫_(m−j) ⊂ C^∞_b Ψ^(m−j)_e3b, j = 0, 1, the elements of 𝒫_m having
classical principal symbols, every N′, all B, E, G and χ as below, and operators on ℂ^(N′) of the form

    L = L_0 + L_1 + L_2,   L_0 ∈ Diff^m_e3b ⊗ Id,   L_1 ∈ C^(d_0,(2δ,δ,δ))_e3b 𝒫_m ⊗ Id,
    L_2 ∈ C^(d_0)_e3b 𝒫_(m−1) ⊗ End ℂ^(N′),

with the scalar principal symbol ℓ of L real. Let ρ_∞ ∈ S^(−1)_hom be a fixed positive elliptic symbol and
𝖧 := ρ_∞^(m−1)H_ℓ. Let B, E, G ∈ C^∞_b Ψ⁰_e3b be carried by χ, with supp χ disjoint from I⁰ ∪ K⁻, as on a neighbourhood
of Ω̄, which meets ∂M̃ only in ℐ⁺, ι⁺ and K⁺ ([[sec:ii-a-1]]). Over M̃ ∖ (I⁰ ∪ K⁻), 𝖧 is a continuous vector field on
ᵉ³ᵇS*M̃, as the coefficients of L_1 vanish at ℐ⁺, ι⁺ and K⁺ ([Hin26c, p. 71]; [[lem:ii-a1-5-1]]). Suppose that
WF′(B) ⊂ Ell(G), that the backward integral curves of 𝖧 from WF′(B) ∩ Char(L) reach Ell(E) in uniformly finite time
while remaining in Ell(G), and that 𝖧𝗌 ≤ 0 on a neighbourhood in ᵉ³ᵇS*M̃ of the union T of these backward segments, up
to their first entry into Ell(E). If χu ∈ H^(−N), GLu ∈ H^(𝗌−m+1) and Eu ∈ H^𝗌, then Bu ∈ H^𝗌 and

    ‖Bu‖_(H^𝗌_e3b) ≤ C(‖GLu‖_(H^(𝗌−m+1)_e3b) + ‖Eu‖_(H^𝗌_e3b) + ‖χu‖_(H^(−N)_e3b)),

with C locally uniform for perturbations of L_0, L_1, L_2 in Diff^m_e3b, C^(d_0,(2δ,δ,δ))_e3b 𝒫_m and
C^(d_0)_e3b 𝒫_(m−1) with real principal symbols, for which 𝖧′𝗌 ≤ 0 on the same neighbourhood of T; the proof uses the
other hypotheses for L only, and the perturbed backward curves reach Ell(E) within a slightly larger time, by the
continuity of the flow in the field ([[lem:ii-a1-5-1]] (c)).

In (L3) and (L4) the number d_0 depends only on m, 𝗌 and N, not on the operators B, E, G, the cut-off χ, the finite
sets of operators or the rank N′ ([[thm:ii-a1-3-1]], [[thm:ii-a1-5-4]]). The inductions below apply (L3) and (L4) to
auxiliary operators, cut-offs, finite sets and systems chosen anew at every order of b-regularity k; this is why the
indices they give do not depend on k.

Everything else in [[sec:ii-a-8]] and [[sec:ii-a-9]] is proved from (L3), (L4) and the calculus of [[sec:ii-a-3]].

#### Estimates with b-regularity {#sec:ii-a-9-2}

**Proposition {#prop:ii-a-9-1}** ([Hin26c, Proposition 3.23].) There is d_0 = d_0(m, 𝗌, N) such that the following
holds for all k ∈ ℕ_0 and L ∈ C^((d_0;k))_(e3b;b) 𝒫, 𝒫 ⊂ C^∞_b Ψ^m_e3b finite; d_0 depends neither on k and 𝒫 nor on
B, G and χ, which enter only the constant. Let B, G be carried by χ, with
WF′(B) ⊂ Ell(G) ∩ Ell(L). If χu ∈ H^((−N;k)) and GLu ∈ H^((𝗌−m;k)), then Bu ∈ H^((𝗌;k)) and

    ‖Bu‖_(H^((𝗌;k))_(e3b;b)) ≤ C(‖GLu‖_(H^((𝗌−m;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))).                 {#eq:ii-a-9-1}

The constant is locally uniform for L in C^((d_0;k))_(e3b;b) 𝒫: it depends on L through a bound for ‖𝐚‖_((d_0;k)) for
some representation, and through (L3).

*Proof.* Let d_0 be the largest of the numbers of (L3) and of [[lem:ii-a-8-6]] for the orders (𝗌, m, N) and
(−N, m, N). Induction on k; k = 0 is (L3). Let k ≥ 1 and assume [[eq:ii-a-9-1]] at k − 1 for all admissible B, G and χ.
Put χ_1 := h_♭(χ), the inner cut-off of (R3) of [[sec:ii-a-8-3]], which carries B, and choose auxiliary operators
G_1, G_2, G_3 ((R1) of [[sec:ii-a-8-3]], for B and G), carried by χ and by χ_1, with WF′(B) ⊂ Ell(G_1),
WF′(G_1) ⊂ Ell(G_2), WF′(G_2) ⊂ Ell(G_3) and WF′(G_3) ⊂ Ell(G) ∩ Ell(L). By [[eq:ii-a-8-1]],
‖Bu‖_((𝗌;k)) ≤ ‖Bu‖_((𝗌;k−1)) + Σ_j ‖V_jBu‖_((𝗌;k−1)). The first term is bounded by [[eq:ii-a-9-1]] at k − 1. Write
V_jBu = BV_ju + [V_j, B]u. Here [V_j, B] is carried by χ_1 with wave front set in that of B ([[lem:ii-a-8-4]] (a)), so
‖[V_j, B]u‖_((𝗌;k−1)) is bounded by [[eq:ii-a-9-1]] at k − 1. For BV_ju, apply [[eq:ii-a-9-1]] at k − 1 to V_ju, with
G_1 in place of G:

    ‖BV_ju‖_((𝗌;k−1)) ≤ C(‖G_1LV_ju‖_((𝗌−m;k−1)) + ‖χ_1V_ju‖_((−N;k−1))).

The last term is at most C‖χu‖_((−N;k)), by (R3). Write LV_ju = V_jLu − [V_j, L]u.
First,

    ‖G_1V_jLu‖_((𝗌−m;k−1)) ≤ ‖G_1Lu‖_((𝗌−m;k)) + ‖[G_1, V_j]Lu‖_((𝗌−m;k−1)) ≤ C(‖GLu‖_((𝗌−m;k)) + ‖χ_*Lu‖_((−N−m;k)))

by [[lem:ii-a-8-4]] (c), since WF′(G_1) ⊂ Ell(G), with the cut-off χ_* of (R2) of [[sec:ii-a-8-3]]: G_1χ_* = G_1,
[G_1, V_j]χ_* = [G_1, V_j] and Gχ_* = G. As χ_*L = χ_*Lχ, [[lem:ii-a-8-6]] (a) at the order −N gives
‖χ_*Lu‖_((−N−m;k)) ≤ C‖𝐚‖_((d_0;k))‖χu‖_((−N;k)). Second,
[V_j, L] = Σ_q ((V_ja_q)P_q + a_q[V_j, P_q]) lies in C^((d_0;k−1))_(e3b;b) 𝒫′, 𝒫′ := 𝒫 ∪ {[V_j, P_q]}, with a
representation of norm at most C‖𝐚‖_((d_0;k)) ([[lem:ii-a-8-2]] (b)). By [[lem:ii-a-8-6]] (b),

    ‖G_1[V_j, L]u‖_((𝗌−m;k−1)) ≤ C‖𝐚‖_((d_0;k))(‖G_2u‖_((𝗌;k−1)) + ‖χu‖_((−N;k−1))).

Since WF′(G_2) ⊂ Ell(G_3) ∩ Ell(L), [[eq:ii-a-9-1]] at k − 1 bounds ‖G_2u‖_((𝗌;k−1)) by
C(‖G_3Lu‖_((𝗌−m;k−1)) + ‖χu‖_((−N;k−1))). [[lem:ii-a-8-4]] (c) bounds ‖G_3Lu‖ by
C(‖GLu‖_((𝗌−m;k−1)) + ‖χ_*Lu‖_((−N−m;k−1))), and the last term is treated as before. Each step shows that the quantity
bounded is finite when the right side of [[eq:ii-a-9-1]] is: the step at k − 1 applied to V_ju has finite right side.
So V_jBu ∈ H^((𝗌;k−1)) for every j, that is, Bu ∈ H^((𝗌;k)), with [[eq:ii-a-9-1]]. The constants depend on L through
‖𝐚‖_((d_0;k)), the constants at k − 1 and those of (L3). The step from k − 1 to k applies (L3), [[lem:ii-a-8-6]] and the
statement at k − 1 to operators G_1, G_2, G_3, [V_j, B], cut-offs χ_1, χ_* and a finite set 𝒫′ chosen anew at each k.
The d_0 of (L3) and of [[lem:ii-a-8-6]] depends only on the orders and not on these choices ([[thm:ii-a1-3-1]],
[[lem:ii-a-8-6]]), so the same d_0 serves at every k: d_0 does not depend on k. ∎

**Proposition {#prop:ii-a-9-2}** ([Hin26c, Proposition 3.24].) There is d_0 = d_0(m, 𝗌, N) such that the following
holds for all δ > 0, k ∈ ℕ_0 and operators on ℂ^(N′) of the form below; d_0 depends neither on k, δ, N′ and the finite
sets nor on B, E, G and χ, which enter only the constant. The operators are

    L = L_0 + L_1 + L_2,   L_0 ∈ Diff^m_e3b ⊗ Id,   L_1 ∈ C^((d_0;k),(2δ,δ,δ))_(e3b;b) 𝒫_m ⊗ Id,
    L_2 ∈ C^((d_0;k))_(e3b;b) 𝒫_(m−1) ⊗ End ℂ^(N′),                                                      {#eq:ii-a-9-2}

under the hypotheses of (L4) on ℓ, B, E, G and 𝗌. If χu ∈ H^((−N;k)), GLu ∈ H^((𝗌−m+1;k)) and Eu ∈ H^((𝗌;k)), then
Bu ∈ H^((𝗌;k)) and

    ‖Bu‖_(H^((𝗌;k))_(e3b;b))
       ≤ C(‖GLu‖_(H^((𝗌−m+1;k))_(e3b;b)) + ‖Eu‖_(H^((𝗌;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))),         {#eq:ii-a-9-3}

with C locally uniform for perturbations as in (L4), at the regularity (d_0; k).

*Proof.* Let d_0 be the largest of the numbers of (L4), of [[lem:ii-a-8-6]] (a) at (−N, m, N), and 2. Induction
on k; k = 0 is (L4). Let k ≥ 1. By [[lem:ii-a-4-1]], [L_0, V_j] = Σ_(l=0)^N A^0_(j,l)V_l with A^0_(j,l) ∈ C^∞_b
Ψ^(m−1)_e3b fixed operators; here [L_0, V_j] ∈ Diff^m_e3b, by [[eq:ii-a-4-1]]. For L_1 = Σ a_qP_q,

    [a_qP_q, V_j] = a_q[P_q, V_j] − (V_ja_q)P_q = Σ_l (a_qA′_(qjl) − (V_ja_q)A″_(ql))V_l,

with A′_(qjl), A″_(ql) ∈ C^∞_b Ψ^(m−1)_e3b fixed ([[lem:ii-a-4-1]] for [P_q, V_j] and for P_q). Likewise for L_2, with
operators of order m − 2. Hence

    [L, V_j] = Σ_(l=0)^N A_(j,l)V_l,
    A_(j,l) ∈ C^∞_b Ψ^(m−1)_e3b + C^((d_0;k−1),(2δ,δ,δ))_(e3b;b) Ψ^(m−1)_e3b + C^((d_0;k−1))_(e3b;b) Ψ^(m−2)_e3b,

each in the span of a fixed finite set, with coefficient norms at most C times those of L at (d_0; k). Here
[[lem:ii-a-4-1]] is applied with ϵ := ϵ_ϑ, the room of (R1) of [[sec:ii-a-8-3]] for B, E and G. So, D bounding the
kernel ranges of the operators of 𝒫_m and 𝒫_(m−1), the fixed operators A^0_(j,l), A′_(qjl), A″_(ql), and those for L_2,
have kernel ranges at most D + ϵ_ϑ. Put u^((1)) := (V_ju)_(j=0)^N and f := Lu. Then LV_ju − Σ_l A_(j,l)V_lu = V_jf,
that is,

    L^((1))u^((1)) = f^((1)) := (V_jf)_(j=0)^N,     L^((1)) := (Lδ_(jl) − A_(j,l))_(j,l=0,…,N).

L^((1)) acts on ℂ^(N′(N+1)), and is of the form [[eq:ii-a-9-2]] at the regularity (d_0; k − 1). Its parts are
L_0 ⊗ Id and L_1 ⊗ Id, and a part of order m − 1 that collects L_2 ⊗ Id and the A_(j,l); the weighted coefficients lie
in the unweighted class by [[lem:ii-a-8-2]] (d). Its principal symbol is ℓ Id, so the hypotheses on ℓ, 𝖧 and 𝗌 are those
for L. Choose B_1 slightly larger than B, with WF′(B) ⊂ Ell(B_1), and E_1, G_1 slightly smaller than E, G, with
WF′(E_1) ⊂ Ell(E) and WF′(G_1) ⊂ Ell(G), such that the hypotheses hold for (B_1, E_1, G_1) (the beginning of
[[sec:ii-a-9]]): auxiliary operators of (R1) for B, E and G. Put χ_1 := h_♭(χ) ((R3)). By (R1) and (R3), B_1, E_1 and
G_1 are carried by χ_1 with the margin D + 7ϵ_ϑ, which bounds the kernel ranges of the operators of L^((1)) and of
B_1, E_1, G_1. So the inductive hypothesis, [[eq:ii-a-9-3]] at k − 1 for L^((1)) with these operators and χ_1, gives

    ‖B_1u^((1))‖_((𝗌;k−1)) ≤ C(‖G_1f^((1))‖_((𝗌−m+1;k−1)) + ‖E_1u^((1))‖_((𝗌;k−1)) + ‖χ_1u^((1))‖_((−N;k−1))).

Here ‖G_1V_jf‖_((𝗌−m+1;k−1)) ≤ ‖G_1f‖_((𝗌−m+1;k)) + ‖[G_1, V_j]f‖_((𝗌−m+1;k−1)). Both terms are bounded by
C(‖GLu‖_((𝗌−m+1;k)) + ‖χu‖_((−N;k))), by [[lem:ii-a-8-4]] (c) and [[lem:ii-a-8-6]] (a) for the error term, as in
[[prop:ii-a-9-1]]. Similarly ‖E_1V_ju‖_((𝗌;k−1)) ≤ C(‖Eu‖_((𝗌;k)) + ‖χu‖_((−N;k))), by [[lem:ii-a-8-4]] (c), and
‖χ_1u^((1))‖_((−N;k−1)) ≤ C‖χu‖_((−N;k)), by (R3). On the left,
‖Bu‖_((𝗌;k)) ≤ C Σ_j (‖BV_ju‖_((𝗌;k−1)) + ‖[V_j, B]u‖_((𝗌;k−1))), and both are bounded by
C(‖B_1u^((1))‖_((𝗌;k−1)) + ‖χu‖_((−N;k))). For the first, [[lem:ii-a-8-4]] (c) applies with WF′(B) ⊂ Ell(B_1). For the
second, the wave front set lies in that of B, and the j = 0 component of u^((1)) is u. The finiteness statements follow
as in [[prop:ii-a-9-1]]. At each k the step applies the statement at k − 1, and through it (L4), to a new system
L^((1)), of rank N′(N + 1), with finite sets enlarged by the A_(j,l), and to new operators B_1, E_1, G_1 and a new
cut-off χ_1; it applies [[lem:ii-a-8-6]] (a) with a new cut-off χ_*. The kernel ranges do not accumulate over the k
levels. The statement at k − 1 holds for all admissible data, whatever bound D their kernel ranges have, and its proof
finds its room anew in the carriers of B_1, E_1 and G_1 ((R1)); each level adds one truncated parametrix, of range at
most the room of that level. The truncations change operators by residual ones and so change only constants. Neither
index depends on these choices ([[thm:ii-a1-5-4]], [[lem:ii-a-8-6]]), so d_0 does not depend on k. ∎

#### Tame estimates {#sec:ii-a-9-3}

**Lemma {#lem:ii-a-9-3}** ([Hin26c, Lemma 3.25].) Let R be a ring, ad_A := [A, ·], and P, X_1, …, X_N ∈ R. Then

    [X_1⋯X_N, P] = Σ_(q=1)^N Σ_(i_1<⋯<i_q) (ad_(X_(i_1))⋯ad_(X_(i_q))P) ∏_(j∉{i_1,…,i_q}) X_j              {#eq:ii-a-9-4}
                 = Σ_(q=1)^N (−1)^(q−1) Σ_(i_1<⋯<i_q) (∏_(j∉{i_1,…,i_q}) X_j)(ad_(X_(i_q))⋯ad_(X_(i_1))P), {#eq:ii-a-9-5}

the products taken in increasing order of j.

*Proof.* N = 1 is the definition. For [[eq:ii-a-9-4]], assume it for N and let X_(N+1) ∈ R. Then

    [X_1⋯X_(N+1), P] = [X_1⋯X_N, P]X_(N+1) + (ad_(X_(N+1))P)X_1⋯X_N + [X_1⋯X_N, ad_(X_(N+1))P],

because X_1⋯X_N Q = QX_1⋯X_N + [X_1⋯X_N, Q] with Q := ad_(X_(N+1))P. The inductive hypothesis applies to the first and
third terms. The first gives the terms of [[eq:ii-a-9-4]] for N + 1 whose index set omits N + 1. The second gives the
set {N + 1}. The third gives the sets containing N + 1 and some i_1 < ⋯ < i_q ≤ N, with ad_(X_(N+1)) innermost, as
[[eq:ii-a-9-4]] requires. Each subset occurs exactly once. For [[eq:ii-a-9-5]], assume it for the N elements
X_2, …, X_(N+1). Then

    [X_1⋯X_(N+1), P] = X_1[X_2⋯X_(N+1), P] + X_2⋯X_(N+1)(ad_(X_1)P) − [X_2⋯X_(N+1), ad_(X_1)P].

The first term gives the sets omitting 1, with X_1 first in the product. The second gives {1}. The third gives the sets
{1} ∪ S, with sign −(−1)^(|S|−1) = (−1)^|S| and with ad_(X_1) innermost. ∎

**Definition {#def:ii-a-9-4}** (Notation; [Hin26c, Notation 3.26].) Fix a finite set 𝒱^♯ spanning 𝒱_b(M̃) over
C^∞(M̃), and the good spanning set V_1, …, V_N. D^j_b, resp. D^j_([b]), denotes the vector of all j-fold compositions of
elements of 𝒱^♯, resp. of the V_i, and D^(≤j) those of order at most j. Each component of D^j_b is a combination, with
coefficients in C^∞(M̃), of components of D^(≤j)_([b]), and conversely; the coefficients' derivatives produce terms of
lower order. All the norms below are therefore unchanged up to constants when D_b is replaced by D_([b]). By
[[lem:ii-a-9-3]], for |J| = q, schematically,

    [D^q_([b]), P] = Σ_(q′=1)^q (ad^(q′)_(D_([b]))P) D^(q−q′)_([b]) = Σ_(q′=1)^q D^(q−q′)_([b]) (ad^(q′)_(D_([b]))P).
                                                                                                           {#eq:ii-a-9-6}

**Lemma {#lem:ii-a-9-5}** ([Hin26c, Lemma 3.27], with C³_b in the first term.) For a, b ∈ ℕ_0 there is C_(a,b) with

    ‖(D^a_bℓ)(D^b_bu)‖_(L²(M̃)) ≤ C_(a,b)(‖ℓ‖_(C³_b)‖u‖_(H^(a+b)_b) + ‖ℓ‖_(C^(a+b+3)_b)‖u‖_(H³_b)).

*Proof.* In each chart φ_α of [[sec:ii-a-4-1]], the b-vector fields are uniformly bounded combinations of the
coordinate vector fields of (−2, 2)⁵, and the density is a constant c_α times a uniformly smooth positive multiple of
|dx|. The coefficient Lie algebra is C^∞_b 𝒱_b ((S1)). Hence ‖v‖²_(L²) and ‖v‖²_(H^q_b) are equivalent, uniformly, to
Σ_α c_α‖χ(φ_α)_*v‖²_(L²(ℝ⁵)) and to the same sum with the H^q(ℝ⁵)-norms of χ̃(φ_α)_*v, χ̃ = 1 on supp χ. And
‖χ̃(φ_α)_*ℓ‖_(C^q) ≤ C‖ℓ‖_(C^q_b) uniformly. It therefore suffices to show, for f ∈ C^(K+3) and g ∈ H^K supported in
(−2, 2)⁵, K := a + b, and |β| ≤ a, |γ| ≤ b, that

    ‖∂^βf ∂^γg‖_(L²(ℝ⁵)) ≤ C(‖f‖_(C³)‖g‖_(H^K) + ‖f‖_(C^(K+3))‖g‖_(H³)),

and to sum over α (finite multiplicity). If |γ| < 3, the left side is at most ‖f‖_(C^K)‖g‖_(H²). If β = 0, it is at
most ‖f‖_(C⁰)‖g‖_(H^K). Otherwise |β| ≥ 1, |γ| ≥ 3 and K′ := |β| + |γ| ≥ 4. Sobolev embedding on ℝ⁵ (3 > 5/2) gives
‖∂^βf‖_(L^∞) ≤ C‖f‖_(H^(|β|+3)). On the Fourier side, Hölder's inequality gives
‖h‖_(H^((1−θ)t_0+θt_1)) ≤ ‖h‖^(1−θ)_(H^(t_0))‖h‖^θ_(H^(t_1)). With θ := |β|/K′ for f (t_0 = 3, t_1 = K′ + 3) and
θ′ := (|γ| − 3)/(K′ − 3) for g (t_0 = 3, t_1 = K′),

    ‖∂^βf ∂^γg‖_(L²) ≤ C ‖f‖^(1−θ)_(H³)‖f‖^θ_(H^(K′+3))‖g‖^(1−θ′)_(H³)‖g‖^(θ′)_(H^(K′)).

Now θ′ ≤ 1 − θ, as K′(|γ| − 3) ≤ |γ|(K′ − 3), and ‖g‖_(H³) ≤ ‖g‖_(H^(K′)). So
‖g‖^(1−θ′)_(H³)‖g‖^(θ′)_(H^(K′)) ≤ ‖g‖^θ_(H³)‖g‖^(1−θ)_(H^(K′)), and the right side is at most
C(‖f‖_(H³)‖g‖_(H^(K′)))^(1−θ)(‖f‖_(H^(K′+3))‖g‖_(H³))^θ ≤ C(‖f‖_(H³)‖g‖_(H^(K′)) + ‖f‖_(H^(K′+3))‖g‖_(H³)) by Young's
inequality. Finally ‖f‖_(H^q) ≤ C‖f‖_(C^q) for f supported in (−2, 2)⁵, and K′ ≤ K. ∎

[Hin26c] uses the Moser estimate in place of the interpolation above, with ‖ℓ‖_(C⁰_b) in the first term. The three
derivatives lost here are absorbed in the thresholds of [[prop:ii-a-9-6]].

**Proposition {#prop:ii-a-9-6}** ([Hin26c, Proposition 3.28].) Let 𝗌 and 𝗌_0 be variable orders,
s̄ := max(0, ⌈sup 𝗌⌉), s̲ := max(0, ⌈−inf 𝗌⌉) and s̲_0 := max(0, ⌈−inf 𝗌_0⌉). There are d_0, d̃ ∈ ℕ, depending only on 𝗌
and 𝗌_0, such that the following holds for all B, B^♯ ∈ C^∞_b Ψ⁰_e3b carried by χ with WF′(B) ⊂ Ell(B^♯). For all k
there is C_k, depending also on B, B^♯ and χ, such that, for
all 0 ≤ j ≤ k,

    ‖B(D^j_([b])ℓ)(D^(k−j)_([b])u)‖_(H^𝗌_e3b)
       ≤ C_k(‖ℓ‖_(C^((d_0;d̃))_(e3b;b))(‖B^♯u‖_(H^((𝗌;k))_(e3b;b)) + ‖χu‖_(H^((𝗌_0;k))_(e3b;b)))
             + ‖ℓ‖_(C^((d_0;k))_(e3b;b))(‖B^♯u‖_(H^((𝗌;d̃))_(e3b;b)) + ‖χu‖_(H^((𝗌_0;d̃))_(e3b;b)))).      {#eq:ii-a-9-7}

One can take d_1 := s̄ + max(s̲, s̲_0) + 3, d̃ := d_1 + max(s̲, s̲_0) + 3, and d_0 the larger of the numbers of
[[lem:ii-a-8-5]] (a) at 𝗌 and (b) at (𝗌, 𝗌_0), which do not depend on B, B^♯ or the operators B_1, B_2 of the proof.

*Proof.* Choose auxiliary operators B_1, B_2 ((R1) of [[sec:ii-a-8-3]], for B and B^♯), carried by χ, with
WF′(I − B_1) ∩ WF′(B) = ∅, WF′(B_1) ⊂ Ell(B_2) and WF′(B_2) ⊂ Ell(B^♯). By [[lem:ii-a-8-4]] (c),
‖B_iv‖_((𝗌;q)) ≤ C(‖B^♯v‖_((𝗌;q)) + ‖χv‖_((𝗌_0;q))), taking N ≥ −inf 𝗌_0 there. It therefore suffices to prove
[[eq:ii-a-9-7]] with B_2 in place of B^♯. By the support convention, u may be replaced by χu.

*The case k = 0.* Bℓu = BℓB_1u + Bℓ(I − B_1)u. [[lem:ii-a-8-5]] (a) and the boundedness of B bound the first term by
C‖ℓ‖_(C^(d_0)_e3b)‖B_1u‖_(H^𝗌), and [[lem:ii-a-8-5]] (b), applied to the pair (B, B_1), bounds the second by
C‖ℓ‖_(C^(d_0)_e3b)‖χu‖_(H^(𝗌_0)).
Finally ‖B_1u‖_(H^𝗌) ≤ C(‖B_2u‖_(H^𝗌) + ‖χu‖_(H^(𝗌_0))).

*The case k ≤ d̃.* Apply the case k = 0 to D^jℓ and D^(k−j)u. By [[lem:ii-a-8-2]] (b),
‖D^jℓ‖_(C^(d_0)_e3b) ≤ C‖ℓ‖_(C^((d_0;j))) ≤ C‖ℓ‖_(C^((d_0;d̃))). By [[eq:ii-a-9-6]],
B_1D^(k−j) = Σ_q D^(k−j−q)(ad^q_(D_([b]))B_1), where ad^qB_1 ∈ C^∞_b Ψ⁰_e3b has wave front set in
WF′(B_1) ⊂ Ell(B_2) ([[lem:ii-a-8-4]] (a)). So, by [[lem:ii-a-8-4]] (c),

    ‖B_1D^(k−j)u‖_(H^𝗌) ≤ C(‖B_2u‖_((𝗌;k−j)) + ‖χu‖_((𝗌_0;k−j))).                                       {#eq:ii-a-9-8}

Also ‖χD^(k−j)u‖_(H^(𝗌_0)) ≤ C‖χu‖_((𝗌_0;k−j)), as in [[prop:ii-a-9-1]]. This is [[eq:ii-a-9-7]].

*The case k > d̃.* If j ≤ d̃, the argument just given bounds the left side by the first line of [[eq:ii-a-9-7]]. If
j ≥ k − d̃, it bounds it by ‖D^jℓ‖_(C^(d_0)_e3b) ≤ C‖ℓ‖_(C^((d_0;k))) times ‖B_2u‖_((𝗌;d̃)) + ‖χu‖_((𝗌_0;d̃)), the
second line. Let d̃ < j < k − d̃. By [[lem:ii-a-8-4]] (d),
‖v‖_(H^𝗌_e3b) ≤ ‖v‖_(H^(s̄)_e3b) ≤ C‖v‖_(H^(s̄)_b) ≤ C Σ_(l≤s̄) ‖D^l_([b])v‖_(L²). By [[eq:ii-a-9-6]],
D^l_([b])B = Σ_(l′≤l) (ad^(l−l′)_(D_([b]))B)D^(l′)_([b]), with ad^(l−l′)B bounded on L². By the Leibniz rule,
D^(l′)((D^jℓ)(D^(k−j)u)) is a sum of terms (D^(j+l_1)ℓ)(D^(k−j+l_2)u), l_1 + l_2 = l′. So it suffices to bound, for
l_1 + l_2 ≤ s̄ and v ∈ {B_1u, (I − B_1)u},

    ‖(D^(j+l_1)ℓ)(D^(k−j+l_2)v)‖_(L²).                                                                  {#eq:ii-a-9-9}

Apply [[lem:ii-a-9-5]] to D^(d_1)ℓ and D^(d_1)v, with a := j + l_1 − d_1 and b := k − j + l_2 − d_1. Both are
positive, since j > d̃ ≥ d_1 and k − j > d̃. Then a + b + d_1 = k + l_1 + l_2 − d_1 ≤ k + s̄ − d_1, and
[[eq:ii-a-9-9]] is at most

    C(‖ℓ‖_(C^(d_1+3)_b)‖v‖_(H^(k+s̄−d_1)_b) + ‖ℓ‖_(C^(k+s̄−d_1+3)_b)‖v‖_(H^(d_1+3)_b)).

Here ‖ℓ‖_(C^(d_1+3)_b) ≤ ‖ℓ‖_(C^((d_0;d̃))), as d_1 + 3 ≤ d̃, and ‖ℓ‖_(C^(k+s̄−d_1+3)_b) ≤ ‖ℓ‖_(C^((d_0;k))), as
d_1 ≥ s̄ + 3. For v = B_1u, [[lem:ii-a-8-7]] and [[lem:ii-a-8-4]] (c) give
‖B_1u‖_(H^(k+s̄−d_1)_b) ≤ C‖B_1u‖_((𝗌;k+s̄−d_1+s̲)) ≤ C(‖B_2u‖_((𝗌;k)) + ‖χu‖_((𝗌_0;k))), as d_1 ≥ s̄ + s̲. Likewise
‖B_1u‖_(H^(d_1+3)_b) ≤ C(‖B_2u‖_((𝗌;d̃)) + ‖χu‖_((𝗌_0;d̃))), as d_1 + 3 + s̲ ≤ d̃. For v = (I − B_1)u, the same with 𝗌_0
for 𝗌 and s̲_0 for s̲ gives ‖χu‖_((𝗌_0;k)) and ‖χu‖_((𝗌_0;d̃)), as I − B_1 is bounded on the mixed spaces. The products
are those of [[eq:ii-a-9-7]]. ∎

**Corollary {#cor:ii-a-9-7}** (Tame bound for operators of limited regularity.) Let 𝒫 ⊂ C^∞_b Ψ^m_e3b be finite,
A ∈ C^((d_0;k))_(e3b;b) 𝒫 with a representation 𝐚, and χ′, χ cut-offs with χ′ carried by χ. With d_0 and d̃ of
[[prop:ii-a-9-6]] for 𝗌 = 𝗌_0 = 𝗍 − m, which depend only on 𝗍 and m (not on k, 𝒫, χ′ or χ), and with C_k depending on
𝒫, χ′ and χ,

    ‖χ′Au‖_((𝗍−m;k)) ≤ C_k(‖𝐚‖_((d_0;d̃))‖χu‖_((𝗍;k)) + ‖𝐚‖_((d_0;k))‖χu‖_((𝗍;d̃))).

*Proof.* Let χ‴ ∈ C^∞(M̃) carry χ′: χ′ = χ‴χ′χ‴, and χ = 1 within d_ℬ-distance D of supp χ‴, D bounding the kernel
ranges of the operators of 𝒫. Then χ‴²χ′ = χ′, so |χ‴| = 1 on supp χ′. Put χ″ := F″(|χ‴|²) and χ_c := F_c(|χ‴|²),
with F″, F_c ∈ C^∞(ℝ), F″ = 1 on [3/4, ∞), F″ = 0 on (−∞, 1/2], F_c = 1 on [1/4, ∞) and F_c = 0 on (−∞, 1/8]. Then
χ″ = 1 near supp χ′, χ_c = 1 near supp χ″, and supp χ_c ⊂ supp χ‴. By [[eq:ii-a-8-1]] and the Leibniz rule, for
|J| ≤ k, V^J(χ′a_qP_qu) is a sum of products (V^(J_0)χ′)(V^(J_1)a_q)(V^(J_2)P_qu), with J_0, J_1, J_2 complementary
subwords of J. Apply [[eq:ii-a-9-7]] with the cut-off χ_c in place of χ, to B := V^(J_0)χ′ and B^♯ := χ″, which are
multiplication operators carried by χ_c (as χ_c = 1 near supp χ″ ⊃ supp χ′) with WF′(B) ⊂ Ell(B^♯), to ℓ := a_q, to
P_qu in place of u, and to (|J_1|, |J_1| + |J_2|) in place of (j, k). Its error terms are ‖χ″P_qu‖_((𝗍−m;q′)) and
‖χ_cP_qu‖_((𝗍−m;q′)), with q′ = |J_1| + |J_2| ≤ k or q′ = d̃. As χ = 1 within D of supp χ_c ⊃ supp χ″, these are
‖χ″P_qχu‖_((𝗍−m;q′)) and ‖χ_cP_qχu‖_((𝗍−m;q′)), which are at most C‖χu‖_((𝗍;q′)) by [[lem:ii-a-8-4]] (a). The
coefficient norms are ‖a_q‖_((d_0;d̃)) and ‖a_q‖_((d_0;|J_1|+|J_2|)) ≤ ‖a_q‖_((d_0;k)). Summing over the finitely many
J and q gives the bound. ∎

**Proposition {#prop:ii-a-9-8}** ([Hin26c, Proposition 3.29].) Let 𝒫 ⊂ C^∞_b Ψ^m_e3b be finite. There are d_0, d ∈ ℕ,
depending only on 𝗌, m and N, such that the following holds for all k and L ∈ C^((d_0;d))_(e3b;b) 𝒫 with a
representation 𝐋. Let B, G be carried by
χ with WF′(B) ⊂ Ell(G) ∩ Ell(L). If 𝐋 is a representation at (d_0; k), then

    ‖Bu‖_((𝗌;k)) ≤ C_k(‖GLu‖_((𝗌−m;k)) + ‖χu‖_((−N;k)) + ‖𝐋‖_((d_0;k))(‖GLu‖_((𝗌−m;d)) + ‖χu‖_((−N;d)))), {#eq:ii-a-9-10}

with the finiteness statement of [[prop:ii-a-9-1]]. C_k depends on L only through a bound for ‖𝐋‖_((d_0;d)) and the
ellipticity margin of (L3), and so is locally uniform in C^((d_0;d))_(e3b;b) 𝒫 for all k at once.

*Proof.* Take d := d̃ + 1, with d_0 and d̃ those of [[prop:ii-a-9-6]] for (𝗌 − m, −N − m), enlarged to serve also
[[prop:ii-a-9-1]] and [[cor:ii-a-9-7]]. All of these depend only on 𝗌, m and N. The induction below applies (L3),
[[prop:ii-a-9-1]], [[prop:ii-a-9-6]] and [[cor:ii-a-9-7]] to operators G_1, G_2, G_3 and cut-offs chosen anew at each
k; as their indices do not depend on these choices, d_0 and d do not depend on k. For k ≤ d, [[eq:ii-a-9-10]] is
[[prop:ii-a-9-1]], whose constant depends on
‖𝐋‖_((d_0;k)) ≤ ‖𝐋‖_((d_0;d)). Let k > d and assume [[eq:ii-a-9-10]] at all orders below k, for all admissible B and G.
Choose G_1, G_2, G_3 as in [[prop:ii-a-9-1]], with WF′(G_3) ⊂ Ell(G) ∩ Ell(L), and let χ_1 := h_♭(χ) and χ_* be the
cut-offs of (R3) and (R2) of [[sec:ii-a-8-3]]. For a word J of length k, [[eq:ii-a-9-4]] gives

    LV^Ju = V^JLu − Σ_(∅≠S⊂J) (ad_(V_S)L)V^(J∖S)u,                                                        {#eq:ii-a-9-11}

with ad_(V_S) the iterated commutator in the order of S and J ∖ S in its order. (L3), applied to V^Ju with G_1 and the
cut-off χ_1, which carries B and G_1, has a constant depending only on ‖𝐋‖_((d_0;0)):

    ‖BV^Ju‖_(H^𝗌) ≤ C(‖G_1V^JLu‖_(H^(𝗌−m)) + Σ_S ‖G_1(ad_(V_S)L)V^(J∖S)u‖_(H^(𝗌−m)) + ‖χ_1V^Ju‖_(H^(−N))).

*The left side.* ‖Bu‖_((𝗌;k)) is at most the sum of ‖Bu‖_((𝗌;k−1)) and the ‖V^JBu‖_(H^𝗌), |J| = k. By
[[eq:ii-a-9-4]], V^JB = BV^J + Σ_S (ad_(V_S)B)V^(J∖S). The operators ad_(V_S)B are carried by χ with wave front set in
that of B, and each term with S ≠ ∅ has at most k − 1 factors V. Moving them to the left by [[eq:ii-a-9-5]] bounds these
terms by finitely many ‖B′u‖_((𝗌;k−1)), with WF′(B′) ⊂ WF′(B). These, and ‖Bu‖_((𝗌;k−1)), are bounded by
[[eq:ii-a-9-10]] at k − 1, which is at most the right side of [[eq:ii-a-9-10]] at k.

*The first two terms on the right.* ‖χ_1V^Ju‖_(H^(−N)) ≤ C‖χu‖_((−N;k)), by (R3). By [[eq:ii-a-9-6]],
‖G_1V^JLu‖_(H^(𝗌−m)) ≤ ‖G_1Lu‖_((𝗌−m;k)) + Σ ‖G′Lu‖_((𝗌−m;k−1)), with WF′(G′) ⊂ WF′(G_1) and the kernel of G′ in that
of G_1. By [[lem:ii-a-8-4]] (c) both are at most C(‖GLu‖_((𝗌−m;k)) + ‖χ_*Lu‖_((−N−m;k))). [[cor:ii-a-9-7]], with χ_* in
place of χ′ (χ_* is carried by χ, (R2)), bounds the error term tamely by
C_k(‖𝐋‖_((d_0;d̃))‖χu‖_((−N;k)) + ‖𝐋‖_((d_0;k))‖χu‖_((−N;d̃))).

*The commutator terms.* Let |S| = j ≥ 1. With L = Σ_q ℓ_qA_q, iterating ad_V(ℓA) = (Vℓ)A + ℓ ad_VA gives
ad_(V_S)L = Σ_q Σ_(S′⊂S) (V_(S′)ℓ_q)(ad_(V_(S∖S′))A_q). Here ad_(V_(S∖S′))A_q ∈ C^∞_b Ψ^m_e3b is fixed, by (S10). By
[[eq:ii-a-9-5]], (ad A_q)V^(J∖S) = Σ V^(J′)A′ with |J′| ≤ k − j and A′ ∈ C^∞_b Ψ^m_e3b fixed. So the terms to bound are
‖G_1(V_(S′)ℓ_q)V^(J′)(A′u)‖_(H^(𝗌−m)), with j′ := |S′| ≤ j and |J′| ≤ k − j ≤ k − 1. If j′ ≥ 1, write
V_(S′)ℓ_q = V_(S′_2)(V_(s_1)ℓ_q), with s_1 the last letter of S′ (the field applied first) and S′_2 the other letters,
and apply [[eq:ii-a-9-7]] with 𝗌 − m for 𝗌, −N − m for 𝗌_0, and the cut-off χ_* in place of χ. Use
(B, B^♯) = (G_1, G_2), which are carried by χ_* ((R2)), ℓ := V_(s_1)ℓ_q, A′u for u, and (j′ − 1, j′ − 1 + |J′|) for
(j, k). Note j′ − 1 + |J′| ≤ k − 1. The bound is

    C_k(‖V_(s_1)ℓ_q‖_((d_0;d̃))(‖G_2A′u‖_((𝗌−m;k−1)) + ‖χ_*A′u‖_((−N−m;k−1)))
        + ‖V_(s_1)ℓ_q‖_((d_0;k−1))(‖G_2A′u‖_((𝗌−m;d̃)) + ‖χ_*A′u‖_((−N−m;d̃)))).

Now ‖V_(s_1)ℓ_q‖_((d_0;d̃)) ≤ C‖𝐋‖_((d_0;d)) and ‖V_(s_1)ℓ_q‖_((d_0;k−1)) ≤ C‖𝐋‖_((d_0;k)) ([[lem:ii-a-8-2]] (b); this
is why d = d̃ + 1). Next, A′ is a commutator of an operator of 𝒫 with vector fields, so its kernel range is at most D,
and χ_*A′ = χ_*A′χ ((R2)): ‖χ_*A′u‖_((−N−m;q)) = ‖χ_*A′χu‖_((−N−m;q)) ≤ C‖χu‖_((−N;q)) by [[lem:ii-a-8-4]] (a). And
‖G_2A′u‖_((𝗌−m;q)) ≤ C(‖G_3u‖_((𝗌;q)) + ‖χu‖_((−N;q))) by [[lem:ii-a-8-4]] (c). By [[eq:ii-a-9-10]] at the order
k − 1, with G_3 in place of B, ‖G_3u‖_((𝗌;k−1)) is bounded by the right side of [[eq:ii-a-9-10]] at k. Its constant
depends only on ‖𝐋‖_((d_0;d)), and its high norm ‖𝐋‖_((d_0;k−1)) multiplies low norms only. By [[prop:ii-a-9-1]] at the
order d̃ < d, ‖G_3u‖_((𝗌;d̃)) ≤ C(‖GLu‖_((𝗌−m;d)) + ‖χu‖_((−N;d))). If j′ = 0, the coefficient is ℓ_q itself and
|J′| ≤ k − 1, and [[eq:ii-a-9-7]] with ℓ := ℓ_q and (0, |J′|) gives the same bounds, with ‖ℓ_q‖_((d_0;d̃)) and
‖ℓ_q‖_((d_0;k−1)). Collecting the terms gives [[eq:ii-a-9-10]]. ([Hin26c] treats only the term with the most
derivatives on the coefficient; the others are bounded in the same way.) ∎

**Proposition {#prop:ii-a-9-9}** ([Hin26c, Proposition 3.30], with 𝗌 − m + 1.) There are d_0, d ∈ ℕ, depending only on
𝗌, m and N, such that the following holds for all δ > 0, all k, finite sets 𝒫_(m−j), j = 0, 1, and
L = L_0 + L_1 + L_2. Here L_0 ∈ Diff^m_e3b,
L_1 ∈ C^((d_0;d),(2δ,δ,δ))_(e3b;b) 𝒫_m and L_2 ∈ C^((d_0;d))_(e3b;b) 𝒫_(m−1), with representations 𝐋_1 and 𝐋_2, under
the hypotheses of (L4). If the representations are at (d_0; k), then

    ‖Bu‖_((𝗌;k)) ≤ C_k(‖GLu‖_((𝗌−m+1;k)) + ‖Eu‖_((𝗌;k)) + ‖χu‖_((−N;k))
                       + ‖𝐋‖_((d_0;k))(‖GLu‖_((𝗌−m+1;d)) + ‖Eu‖_((𝗌;d)) + ‖χu‖_((−N;d)))),              {#eq:ii-a-9-12}

with ‖𝐋‖ := ‖𝐋_1‖ + ‖𝐋_2‖. C_k depends on L only through bounds at (d_0; d), and is locally uniform for perturbations of
L_0, L_1, L_2 in Diff^m_e3b, C^((d_0;d),(2δ,δ,δ))_(e3b;b) 𝒫_m and C^((d_0;d))_(e3b;b) 𝒫_(m−1). ([Hin26c, (3.85)] prints
𝗌 − m for 𝗌 − m + 1 in both places; the real principal type estimate gives 𝗌 − m + 1, which the proof of [Hin26c,
Proposition 3.30] uses, and 𝗌 − m would be false, as propagation loses one derivative.)

*Proof.* Take d := d̃ + 2, with d_0 and d̃ of [[prop:ii-a-9-6]] for (𝗌 − m + 1, −N − m), enlarged to serve
[[prop:ii-a-9-2]] and [[cor:ii-a-9-7]]. All of these depend only on 𝗌, m and N. The induction below applies (L4) to the
system L^((k)), whose rank (N + 1)^k N′ grows with k, and applies (L4), [[prop:ii-a-9-2]], [[prop:ii-a-9-6]] and
[[cor:ii-a-9-7]] to operators B_1, E_1, G_1, G_2, G_3 and cut-offs χ_1, χ_* chosen anew at each k. As their indices
depend on none of these,
d_0 and d do not depend on k. For k ≤ d, [[eq:ii-a-9-12]] is [[prop:ii-a-9-2]]. Let k > d and assume
[[eq:ii-a-9-12]] below k. Let 𝒲_k be the set of words of length k in the letters 0, …, N, with V_0 = I, and put
u^((k)) := (V^αu)_(α∈𝒲_k). By [[eq:ii-a-9-4]], LV^αu = V^αLu − Σ_(S≠∅) (ad_(V_S)L)V^(α∖S)u. For |S| = 1, S = {i},
[[lem:ii-a-4-1]], with ϵ := ϵ_ϑ, the room of (R1) of [[sec:ii-a-8-3]] for B, E and G, and the calculation in the proof
of [[prop:ii-a-9-2]] give ad_(V_(α_i))L = Σ_ν L_(α_i,ν)V_ν. Here

    L_(α_i,ν) ∈ C^∞_b Ψ^(m−1)_e3b + C^((d_0;d−1),(2δ,δ,δ))_(e3b;b) Ψ^(m−1)_e3b + C^((d_0;d−1))_(e3b;b) Ψ^(m−2)_e3b,

in the span of a fixed finite set. Its coefficients carry at most one b-derivative of those of L, so their
C^(d_0)_e3b-norms are bounded by C‖𝐋‖_((d_0;1)). And V_νV^(α∖{i}) is again a word of length k. Hence

    L^((k))u^((k)) = f^((k)) + f̃^((k)),     f^((k)) := (V^αLu)_α,     f̃^((k)) := (−Σ_(|S|≥2) (ad_(V_S)L)V^(α∖S)u)_α,

where (L^((k))w)_α := Lw_α + Σ_i Σ_ν L_(α_i,ν)w_(ν·(α∖{i})). L^((k)) is a system of the form of (L4), built from
commutators of the fixed operators with the V_j. Its principal symbol is ℓ Id and its coefficients have
C^(d_0)-norms bounded by C‖𝐋‖_((d_0;1)). If D bounds the kernel ranges of the operators of 𝒫_m and 𝒫_(m−1), those of
its operators are at most D + ϵ_ϑ, once and for all: L^((k)) is built from the fixed L_(α_i,ν) at every k. Apply (L4)
to it, with the cut-off χ_1 := h_♭(χ) of (R3) and with operators chosen as follows. Let T be as at the
beginning of [[sec:ii-a-9]], and U ⊂ Ell(G) a neighbourhood of T on which 𝖧𝗌 ≤ 0. Apply (O) to U, giving U_T, K_E and
K_U, and again to U_T ∩ U in place of U, giving U′_T ⊂ U_T, K′_E and K′_U ⊂ U_T. Take B_1 with WF′(B) ⊂ Ell(B_1) and
WF′(B_1) ⊂ U′_T, E_1 elliptic on K′_E with WF′(E_1) ⊂ Ell(E), and G_1, G_2, G_3 microsupported in U_T, with G_1 elliptic
on K′_U ∪ WF′(B_1), WF′(G_1) ⊂ Ell(G_2) and WF′(G_2) ⊂ Ell(G_3), all auxiliary operators of (R1) for B, E and G. They
are carried by χ, and by χ_1 with the margin D + 7ϵ_ϑ, which bounds the kernel ranges of the operators of L^((k)). By
(O) the hypotheses of (L4) hold for (B_1, E_1, G_1), and for (G_2, E, G) and (G_3, E, G). (Taking G_1 slightly
smaller than G would not do: then WF′(G_3) contains T and may reach where the hypotheses fail.) The constant depends on k
through the size of the system, and on L only through low norms:

    ‖B_1u^((k))‖_(H^𝗌) ≤ C_k(‖G_1f^((k))‖_(H^(𝗌−m+1)) + ‖G_1f̃^((k))‖_(H^(𝗌−m+1)) + ‖E_1u^((k))‖_(H^𝗌)
                              + ‖χ_1u^((k))‖_(H^(−N))).

The left side controls ‖Bu‖_((𝗌;k)) up to terms ‖B′u‖_((𝗌;k−1)), WF′(B′) ⊂ WF′(B), which are bounded by
[[eq:ii-a-9-12]] at k − 1 (as in [[prop:ii-a-9-8]]). The terms with f^((k)), E_1 and χ_1 are bounded as in
[[prop:ii-a-9-8]], the error term of G_1f^((k)) by [[cor:ii-a-9-7]]. It remains to bound G_1f̃^((k)). Its terms are
G_1(ad_(V_S)L)V^(α∖S)u with |S| = j ≥ 2, so at most k − 2 factors V act on u.

For L_0, ad_(V_S)L_0 ∈ Diff^m_e3b is fixed, and by [[lem:ii-a-8-4]] (c) and (d),

    ‖G_1(ad_(V_S)L_0)V^(α∖S)u‖_(H^(𝗌−m+1)) ≤ C(‖G_2u‖_((𝗌+1;k−2)) + ‖χu‖_((−N;k)))
                                           ≤ C(‖G_2u‖_((𝗌;k−1)) + ‖χu‖_((−N;k))).                     {#eq:ii-a-9-13}

The second inequality is [Hin26c, (3.87)], here [[lem:ii-a-8-4]] (d). For L_1 and L_2,
ad_(V_S)(ℓA) = Σ_(S′⊂S) (V_(S′)ℓ)(ad_(V_(S∖S′))A) with A of order m or m − 1. Commute the fixed operator through the
V's by [[eq:ii-a-9-5]]. If j′ := |S′| ≥ 2, apply [[eq:ii-a-9-7]] at the order 𝗌 − m + 1, with (B, B^♯) = (G_1, G_2),
the cut-off χ_* of (R2) in place of χ, ℓ replaced by V_(S″)ℓ, S″ the last two letters of S′ (the fields applied first),
and (j′ − 2, ·) for (j, ·). The coefficient norms are ‖ℓ‖_((d_0;d̃+2)) ≤ C‖𝐋‖_((d_0;d)) and ‖ℓ‖_((d_0;k)). The
u-norms are bounded by
‖G_2A′u‖_((𝗌−m+1;k−2)) ≤ C(‖G_3u‖_((𝗌+1;k−2)) + ‖χu‖_((−N;k))) ≤ C(‖G_3u‖_((𝗌;k−1)) + ‖χu‖_((−N;k)))
([[lem:ii-a-8-4]] (c), (d)), and the same at d̃; the error terms ‖χ_*A′u‖ are at most C‖χu‖, as in
[[prop:ii-a-9-8]]. If j′ ≤ 1, the coefficient carries at most one derivative, and [[eq:ii-a-9-7]] with ℓ replaced by
V_(S′)ℓ and (0, ·) gives the same bounds, with ‖V_(S′)ℓ‖_((d_0;d̃)) ≤ C‖𝐋‖_((d_0;d)). Here ‖G_3u‖_((𝗌;k−1)), and
‖G_2u‖_((𝗌;k−1)) in [[eq:ii-a-9-13]], are bounded by [[eq:ii-a-9-12]] at k − 1 with G_3, resp. G_2, in place of B, for
which the hypotheses hold by the choice above. And ‖G_3u‖_((𝗌;d̃+1)) is bounded by [[prop:ii-a-9-2]] at the order
d̃ + 1 < d, with constant depending on ‖𝐋‖_((d_0;d)). This gives [[eq:ii-a-9-12]]. The local uniformity follows from
that of (L4) and [[prop:ii-a-9-2]]. ∎

