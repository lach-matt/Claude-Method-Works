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

*Notation.* Variable orders are written in sans-serif letters 𝗌, 𝗆, 𝗅, 𝗋, 𝖻, constant orders in italic. ℝ̄^N is the
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
Hence 𝒱_3b ⊂ 𝒱_b and ρ_K𝒱_b ⊂ 𝒱_3b (as ρ_K t∂_t = r∂_t), and [r∂_r, r∂_t] = r∂_t shows that 𝒱_3b is a Lie algebra. A
b-vector field V lies in 𝒱_3b if and only if Vt ∈ tρ_K C^∞ near K⁺ (the coefficient of t∂_t must lie in ρ_K C^∞). Away
from K⁺, 3b- and b-vector fields coincide, and ³ᵇTM̃ = ᵇTM̃ over M̃ ∖ (K⁺ ∪ ℐ⁺) [Hin26c, (2.21)].

**Lemma {#lem:ii-a-2-2}** (Commutators with time dilations; [Hin26c, Lemma 2.11].) Let V ∈ 𝒱_b(M̃_0) with
V − t∂_t ∈ ρ_K𝒱_b(M̃_0) near K⁺, and let W ∈ 𝒱_3b(M̃_0). Then [V, W] = ρ_K w^♭ V + ρ_K W^♯ with w^♭ ∈ C^∞(M̃_0) and
W^♯ ∈ 𝒱_3b(M̃_0); in particular [V, W] ∈ 𝒱_3b. If W ∈ ρ_sf^(−α_sf) ρ_K^(−α_K) Diff^m_3b(M̃_0), then [V, W] lies in the
same space; and if α_K = 0, then [V, W] = ρ_K W^♭ V + ρ_K W^♯ with W^♭ ∈ ρ_sf^(−α_sf) Diff^(m−1)_3b and
W^♯ ∈ ρ_sf^(−α_sf) Diff^m_3b. The same holds on a smooth vector bundle E, with V ∈ Diff¹_b and
V − ∇_(t∂_t) ∈ ρ_K Diff¹_b for a smooth connection ∇.

([Hin26c, Lemma 2.11] prints W^♯ ∈ Diff^m_3b in the weighted case; its proof gives the weighted class stated here.)

*Proof.* Only the corner K⁺ ∩ sf needs an argument; there take ρ_K = r/t, and note that Vf ∈ ρ_K C^∞ for f ∈ C^∞, since
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

*Proof.* Near K⁺, t∂_t is one by [[lem:ii-a-2-2]], and the ⟨x⟩∂_(z^μ) are trivially ones; their C^∞-span is 𝒱_b near
K⁺ by the spanning sets of [[sec:ii-a-2-1]]. Away from K⁺, 𝒱_3b = 𝒱_b. ∎

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
𝕊³), dual to dρ_+/ρ_+, dx_I/x_I, dω/x_I. Thus ḡ ∈ ρ_0⁻²x_I⁻²ρ_+⁻² C^∞(M̃ ∖ K⁺; S² ᵉᵇT*M̃), and ᵉᵇTM̃ = ᵇTM̃ away
from ℐ⁺.

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
M̃ ∖ K⁺, glued over M̃ ∖ (K⁺ ∪ ℐ⁺) by the identity of Tℝ^(1+4) (which is how both are identified with ᵇT there).
Equivalently, 𝒱_e3b(M̃) is the space of b-vector fields tangent to the fibres of ℐ⁺ with Vt ∈ tρ_K C^∞ near K⁺.
Diff^m_e3b is defined as before. On Ω, ḡ ∈ ρ_0⁻²x_I⁻²ρ_+⁻² C^∞(Ω; S² ᵉ³ᵇT*M̃) and
ḡ⁻¹ ∈ ρ_0²x_I²ρ_+² C^∞(Ω; S² ᵉ³ᵇTM̃).

**Lemma {#lem:ii-a-2-9}** (Good spanning sets; [Hin26c, Lemma 2.18].) 𝒱_b(M̃) is spanned over C^∞ by the
e3b-commutator b-vector fields 𝒱_(b,[e3b]). More precisely, there is a *good spanning set*: a set
𝒱 = {V_1, …, V_N} ⊂ 𝒱_(b,[e3b]) spanning 𝒱_b, with bounded weights w_j ∈ C^∞(M̃), such that V_(0,j) := w_jV_j ∈ 𝒱_e3b
and {V_(0,j)} spans 𝒱_e3b over C^∞.

*Proof.* The spanning statement combines [[cor:ii-a-2-3]] and [[cor:ii-a-2-7]], the two regions being disjoint up to the
region where both algebras equal 𝒱_b. A good spanning set: finitely many e3b-vector fields spanning 𝒱_e3b (weights 1),
together with χ_K t∂_t = ρ_K⁻¹χ_K r∂_t (w = ρ_K = r/t) and, for a spanning set of vector fields ∂_ω on 𝕊³,
χ_I∂_ω = x_I⁻¹χ_I x_I∂_ω (w = x_I), where χ_K and χ_I localise near K⁺ and ℐ⁺; these are commutator fields by
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
M′_+ := [[0, ∞)_τ × ι⁺; {0} × v⁻¹(∞)]. The map (t, r, ω) ↦ (τ, v, ω), τ = 1/t_*, v = t_*/r, induces a diffeomorphism
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
following results of that paper, as stated there; they hold on smooth manifolds of every dimension n. The notation
inside the list is that of [Hin26d]. Later chapters cite them as (S1)–(S11).

(S1) [Hin26d, Definition 1.1, p. 2; Definition 1.3 and (1.6), p. 5.] A *b.g. structure* on an n-manifold M without
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

(S4) [Hin26d, Definitions 3.7 and 3.8, p. 31; Definition 3.31, p. 44; Definition 3.34, p. 46; Definition 3.43, p. 51.]
The 𝒱-cotangent bundle ^𝒱T*M has the trivialisations U_α × ℝ^n ∋ (p, ξ) ↦ Σ ξ_i dx^i_α/ρ_(α,i). S^m(^𝒱T*M) consists of
the functions a whose local expressions satisfy |∂_x^β ∂_ξ^γ a| ≤ C_(βγ)⟨ξ⟩^(m−|γ|) uniformly in α.
Op_𝒱(a) := Σ_α φ_α^* Op_α((φ_α)_*(χ_α a)), with Op_α the quantization with phase Σ (x^j − x′^j)ξ_j/ρ_(α,j) and a
cut-off ψ(x − x′). The residual operators wρ^∞Ψ^(−∞)_𝒱 are those which, together with their adjoints, map
w′ρ^(−N)H^((−N;k))_(𝒱;𝒲) to ww′ρ^N H^((N;k))_(𝒱;𝒲) for all w′, N and k. Finally
wΨ^m_𝒱(M) := {Op_𝒱(a) + R : a ∈ wS^m, R residual}.

(S5) [Hin26d, Theorem 3.44, p. 51; Remark 3.47, p. 52; Theorem 3.51, p. 55; Theorem 3.52, p. 56; Proposition 3.55,
p. 57.] A ∈ wΨ^m_𝒱 maps w′H^((s;k))_(𝒱;𝒲) to ww′H^((s−m;k))_(𝒱;𝒲) boundedly, with norm bounded by a seminorm of A
(Remark 3.47). The classes wρ^(−l)Ψ^m_𝒱 are closed under adjoints (σ(A*) is the complex conjugate of σ(A)) and
compositions (σ(A_1A_2) = σ(A_1)σ(A_2)); σ(i[A_1, A_2]) = H_(σ(A_1))σ(A_2); WF′(A_1A_2) ⊂ WF′(A_1) ∩ WF′(A_2); and
these operations are continuous. Microlocal elliptic regularity: if WF′(B) ⊂ Ell(A), A ∈ w′Ψ^(m′), then
‖Bu‖_(wρ^l H^m) ≤ C_N(‖Au‖_(ww′ρ^l H^(m−m′)) + ‖u‖_(wρ^(−N)H^(−N))). Elliptic operators are Fredholm when 𝒱 is fully
symbolic.

(S6) [Hin26d, Remark 3.33, p. 45; Lemma 3.5, p. 30.] The boundedness
Op_𝒱(a) : w′H^((s;k))_(𝒱;𝒲) → ww′H^((s−m;k))_(𝒱;𝒲) requires only uniform bounds ⟨ξ⟩^(m−|γ|) on
(ρ_α∂_x)^β ∂_x^(β′) ∂_ξ^γ a_α for |β′| ≤ k (𝒱-regular symbols with x-derivatives up to order k); the proof gives
operator norms bounded by finitely many such seminorms, their number depending on s and m in a compact set.

(S7) [Hin26d, Definitions 3.58 and 3.59, p. 59.] For a parameterised scaled b.g. structure (ℬ^(p,×))_(p∈P), with all
bounds uniform in p, the above holds uniformly in p; operators are families with uniformly bounded symbols and residual
parts, bounded uniformly on the p-dependent spaces.

(S8) [Hin26d, Definition 4.6 and the paragraph after it, p. 66; Section 4.2.] Variable orders 𝗆, 𝗅 ∈ S⁰: the symbols
ρ^(−𝗅)λ^(−𝗆)a_0 with a_0 ∈ ⋂_(δ∈(0,1/2)) S⁰_(1−δ,δ), contained in ⋂_δ ρ^(−sup 𝗅) S^(sup 𝗆)_(1−δ,δ), and the corresponding
operators and Sobolev spaces (variable decay orders when the scaling weight tends to 0). The paper states that orders
are additive under composition and that its Theorem 3.44 "remains valid, mutatis mutandis, in the variable order case",
the principal symbol being taken modulo ⋂_δ ρ^(−𝗅+1−2δ) S^(𝗆−1+2δ). Theorem 3.44 there is the boundedness theorem; the
statement concerns composition, and we read it as including the calculus of its Theorem 3.51. It also states that the
operators map H^(𝗆′,𝗅′) to H^(𝗆′−𝗆,𝗅′−𝗅), by the proof of its Proposition 4.2. The factor a_0 need not lie in S⁰: its
derivatives may carry logarithmic factors, as those of λ^(−𝗆) do.

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
max_k |ω_k| ≥ 1/2; any finite cover by charts gives an equivalent structure [Hin26d, Proposition 3.2]):

    U_(2,ijk±) := (2^(−i−2), 2^(−i+2))_τ × (2^(−j−2), 2^(−j+2))_(ρ_K) × 𝕊³_(k±),     j ≥ i,

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
with A_j ∈ C^∞_b Ψ^(𝗌−1)_e3b.

*Proof.* B := Σ_j V_(0,j)^* V_(0,j) ∈ Diff²_e3b is elliptic, so I = QB + R with Q ∈ C^∞_b Ψ^(−2)_e3b and
R ∈ C^∞_b Ψ^(−1)_e3b: take Q := Op(q) with q ∈ S^(−2) equal to σ(B)⁻¹ outside a compact subset of each fibre,
uniformly; then R := I − QB has principal symbol 0 at order 0, so it has order −1 by the principal symbol sequence
(S5). (This is the first step of [[lem:ii-a-8-4]] (b), which does not use the present lemma; a parametrix to this
finite order suffices.) Then A = Σ_j AQV_(0,j)^* w_jV_j + ARV_0, and A_j := AQV_(0,j)^* w_j ∈ C^∞_b Ψ^(𝗌−1)_e3b,
A_0 := AR ∈ C^∞_b Ψ^(𝗌−1)_e3b. ∎

Passing to the secondary structure (subdividing the cells into ρ-cuboids) gives the larger classes
Ψ̃_e3b = C^∞_e3b Ψ_e3b with e3b-regular coefficients ([Hin26d, Remark 3.48]: Ψ_𝒱 ⊂ Ψ_(𝒱′)), still bounded on the same
spaces.

#### Bundles {#sec:ii-a-4-3}

Operators on the trivial bundle ℂ^N (the bundles of [[sec:i-a-1-2]]) are N × N matrices of scalar operators; all
statements above and below hold for them with matrix-valued symbols, the principal symbols multiplying as matrices
([Hin26d, Remark 3.13] for differential operators; for pseudodifferential operators, matrices of scalar ones). Where a
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

By (S9), the Fourier transform in t, û(σ) = ∫ e^(−iσt) u dt, leads to the parameterised scaled b.g. structure on
X̃ = ℝ̄⁴ with the b-cells and the scalings ρ_(σ,α,i) = (1 + |σ|⟨x⟩)⁻¹ [Hin26c, Section 3.2.2], with coefficient Lie
algebra C^∞_b 𝒱_b(X̃) for all σ, and the following operator Lie algebras and spaces.

(1) At σ = 0: C^∞_b 𝒱_b(X̃) (the b-setting).

(2) At fixed σ ≠ 0: C^∞_b 𝒱_sc(X̃).

(3) For ±σ ∈ [0, 1]: the scattering-b-transition algebra C^∞_b 𝒱_(sc-b)(X̃) on
X̃_(sc-b) := [[0, 1]_ς × X̃; {0} × ∂X̃], ς = ±σ, with faces scf, tf and zf, where
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

*Proof.* (S9) ([Hin26d, Proposition 4.18], with the variable-order version referred to in [Hin26c] after (3.16))
gives the isomorphism onto L²(ℝ_σ; ρ_sf^(α_sf)⟨τσ⟩^(−𝗌_σ) H^(𝗌_σ)_(𝒱̂_σ)) with τ ∼ ⟨x⟩, and |dt dx| on one side, |dx|
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

*Proof.* Spatial b-derivatives commute with the Fourier transform ℱ. ℱ(∂_t u) = iσû and
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
b-cells up to a uniformly compatible change [Hin26d, Proposition 3.2], and the weight ρ_scf^𝗋 ρ_tf^l ρ_zf^q is there
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

The spectral side is the parameterised structure on (ι⁺)° with scalings (1 + ρ_K|σ|)⁻¹ near K⁺ and ⟨σ⟩⁻¹, x_I⟨σ⟩⁻¹
near ℐ⁺ [Hin26c, Section 3.2.4]. For fixed σ it is the 0,b-structure C^∞_b 𝒱_(0,b)(ι⁺) (0-vector fields x_I∂_(x_I),
x_I∂_ω at ι⁺ ∩ ℐ⁺, b-vector fields at ι⁺ ∩ K⁺), with the spaces H^(𝗌,(2α_I,γ))_(0,b)(ι⁺) = x_I^(2α_I) ρ_K^γ H^𝗌_(0,b).
For ±σ ∈ [1, ∞) and h = |σ|⁻¹ it is the semiclassical 0- and cone structure on
ι⁺_(0ℏ,cℏ) := [[0, 1)_h × ι⁺; {0} × (ι⁺ ∩ K⁺)], with faces cf, tf, sf and 0f, and the spaces

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

(2) c‖u‖_(H^𝗌) ≤ sup_(‖v‖_(H^(−𝗌)) = 1) |⟨u, v⟩| ≤ C‖u‖_(H^𝗌), uniformly in σ.

*Proof.* For 𝗌 = 0 this is the Cauchy–Schwarz inequality and the Riesz representation theorem. In general take an
elliptic A ∈ Ψ^𝗌_𝒱 and a two-sided parametrix to finite order: B ∈ Ψ^(−𝗌)_𝒱 with BA = I − R_1 and AB = I − R_2, where
R_1, R_2 ∈ Ψ^(−J)_𝒱 and J ≥ sup |𝗌|, all uniformly in σ. It is built as in [[lem:ii-a-8-4]] (b), with I in place of B
there, by (S5), (S7) and (S8). That gives B_L A = I − R_1, and the same for A* gives AB_R = I − R′_2. Then B_L − B_R =
B_L R′_2 − R_1 B_R has order −𝗌 − J, so B := B_L satisfies AB = I − R_2 with R_2 of order −J. (A parametrix to finite
order suffices; (S5) does not state a full parametrix.) As J ≥ sup |𝗌|, R_1 maps H^𝗌 and R_1^* maps H^(−𝗌) into L², and
R_2, R_2^* map L² into H^(−𝗌) and H^𝗌 respectively.

(1) For u, v ∈ C_c^∞, ⟨u, v⟩ = ⟨Au, B^*v⟩ + ⟨R_1u, v⟩, and, as v = A^*B^*v + R_1^*v,
⟨R_1u, v⟩ = ⟨AR_1u, B^*v⟩ + ⟨R_1u, R_1^*v⟩; so ⟨u, v⟩ = ⟨A(I + R_1)u, B^*v⟩ + ⟨R_1u, R_1^*v⟩, each factor bounded into
L² from H^𝗌 or H^(−𝗌) respectively.

(2) Given λ ∈ (H^(−𝗌))*, the map j : L² ⊕ L² ∋ (v_0, v_1) ↦ Av_0 + R_2v_1 ∈ H^(−𝗌) is bounded and onto, as v = j(Bv, v).
Write λ ∘ j = ⟨·, u_0⟩ + ⟨·, u_1⟩ with ‖u_0‖ + ‖u_1‖ ≤ C‖λ‖. Then λ(v) = ⟨Bv, u_0⟩ + ⟨R_2v, u_1⟩ = ⟨v, u⟩ with
u := B^*u_0 + R_2^*u_1 ∈ H^𝗌 and ‖u‖_(H^𝗌) ≤ C′‖λ‖. ∎

**Definition {#def:ii-a-7-2}** ([Hin26c, Definition 3.16].) For Ω ⊂ M open,
Ḣ^𝗌_(𝒱_σ)(Ω̄) := {u ∈ H^𝗌_(𝒱_σ)(M) : supp u ⊂ Ω̄}, and H̄^𝗌_(𝒱_σ)(Ω) := {u|_Ω : u ∈ H^𝗌_(𝒱_σ)(M)} with the quotient
norm, that is, the norm of the minimal extension.

**Lemma {#lem:ii-a-7-3}** ([Hin26c, Lemma 3.17].) The L² pairing extends to H̄^𝗌(Ω) × Ḣ^(−𝗌)(Ω̄) with a uniform bound,
and c‖u‖_(H̄^𝗌(Ω)) ≤ sup_(‖v‖_(Ḣ^(−𝗌)(Ω̄)) = 1) |⟨u, v⟩| ≤ C‖u‖_(H̄^𝗌(Ω)), uniformly; likewise with the roles of the two
spaces exchanged.

*Proof.* With ũ the minimal extension, |⟨u, v⟩| = |⟨ũ, v⟩| ≤ C‖ũ‖‖v‖. For the lower bound, extend
λ ∈ Ḣ^(−𝗌)(Ω̄)* by 0 on the orthogonal complement to λ̃ of the same norm, represent it by ũ ([[lem:ii-a-7-1]] (2)), and
put u := ũ|_Ω; then λ(v) = ⟨v, u⟩ for v supported in Ω̄, and ‖u‖_(H̄^𝗌) ≤ ‖ũ‖ ≤ C‖λ‖. The other case is the same with
the roles of the spaces exchanged. ∎

**Proposition {#prop:ii-a-7-4}** ([Hin26c, Proposition 3.18].) In the setting of (S9) with Ω ⊂ X open, the Fourier
transform in t is an isomorphism

    Ḣ^𝗌_𝒱(ℝ × Ω̄) → L²(ℝ_σ; ⟨τσ⟩^(−𝗌) Ḣ^𝗌_(𝒱̂_σ)(Ω̄))     and     H̄^𝗌_𝒱(ℝ × Ω) → L²(ℝ_σ; ⟨τσ⟩^(−𝗌) H̄^𝗌_(𝒱̂_σ)(Ω)).

*Proof.* The supported case is (S9) restricted to the closed subspace of distributions supported in ℝ × Ω̄, whose
transforms are supported in Ω̄ for each σ. For the extendible case, by [[lem:ii-a-7-3]] (without parameter), the
supported case, [[lem:ii-a-7-3]] (1) at each σ, and the Cauchy–Schwarz inequality,

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
supported within a finite d_ℬ-distance of the diagonal. This is a property an operator of the calculus may or may not
have, and residual operators need not have it [Hin26d, Remark 3.48]. Here the operators of 𝒫 and all auxiliary
operators are taken localized near the diagonal. Quantizations are, by the cut-off ψ(x − x′) of [Hin26d, (3.26)] and
the chart cut-offs of [Hin26d, Definition 3.31]. The class is closed under compositions and adjoints, since kernel
supports add or are reflected, and under commutators with vector fields, and it contains the finite-order parametrices
of [[lem:ii-a-8-4]] (b), which are quantizations. For χ ∈ C^∞(M̃), an operator A is *carried by* χ if A = χ′Aχ′ for
some χ′ ∈ C^∞(M̃) such that χ = 1 within d_ℬ-distance D of supp χ′. Here D bounds the kernel ranges of the finitely many
operators of the statement at hand; for differential operators χ = 1 on supp χ′ suffices. Then Aχ = A = χA, and
AP = APχ for each operator P of the statement. [Hin26c] writes B = χBχ, and its estimates are read with this convention.
[Hin26c, p. 48] does not require the localization near the diagonal. Auxiliary operators chosen in a proof are carried
by cut-offs nested between χ′ and χ.

**Lemma {#lem:ii-a-8-4}** Let A ∈ C^∞_b Ψ^(m′)_e3b, m′ ∈ ℝ, and let 𝗌 be a variable order.

(a) A maps H^((𝗌;k))_(e3b;b) to H^((𝗌−m′;k))_(e3b;b) boundedly for every k. For V ∈ 𝒱_(b,[e3b]),
[V, A] ∈ C^∞_b Ψ^(m′)_e3b with WF′_e3b([V, A]) ⊂ WF′_e3b(A); the iterated commutators ad_(V_(j_1))⋯ad_(V_(j_q))A
likewise.

(b) (Microlocal parametrix.) Let B ∈ C^∞_b Ψ^(m_B)_e3b with WF′_e3b(B) ⊂ Ell_e3b(A), and J ∈ ℕ. Then B = QA + R with
Q ∈ C^∞_b Ψ^(m_B−m′)_e3b and R ∈ C^∞_b Ψ^(m_B−J)_e3b.

(c) In (b), if B and A are carried by χ, then for all 𝗌, N and k,

    ‖Bu‖_(H^((𝗌−m_B;k))_(e3b;b)) ≤ C(‖Au‖_(H^((𝗌−m′;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))).

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

(c) Bu = B(χu) = QAχu + R_Jχu = QAu + R_Jχu, because Aχ = A and Bχ = B for operators carried by χ. Take J ≥ sup 𝗌 + N
and use (a).

(d) By [[lem:ii-a-4-1]] (with (S8) for variable orders), an elliptic Λ ∈ C^∞_b Ψ^(𝗌+1)_e3b is Σ_(l=0)^N Λ_lV_l with
Λ_l ∈ C^∞_b Ψ^𝗌_e3b. Microlocal elliptic regularity (S5), with I in place of B, gives
‖v‖_(H^(𝗌+1)) ≤ C(‖Λv‖_(L²) + ‖v‖_(H^(−N))) ≤ C Σ_l ‖V_lv‖_(H^𝗌). Apply this to v = V^J u, |J| ≤ k − 1, and sum, using
[[eq:ii-a-8-1]]. Iterating gives the second claim. For the third, H^(s̄)_b is by definition the space of u with
V^J u ∈ L² for |J| ≤ s̄. ∎

#### Multiplication and pseudolocality {#sec:ii-a-8-4}

**Lemma {#lem:ii-a-8-5}** (Multiplication and pseudolocality; the part of [Hin26c, Lemma 3.5] that is used, and the
pseudolocality in the proof of [Hin26c, Proposition 3.28].) Let 𝗌 and 𝗌_0 be variable orders.

(a) There are d_0 ∈ ℕ and C with ‖ℓu‖_(H^𝗌_e3b) ≤ C‖ℓ‖_(C^(d_0)_e3b)‖u‖_(H^𝗌_e3b) for all ℓ ∈ C^(d_0)_e3b. Moreover, for
every k, ‖ℓu‖_(H^((𝗌;k))_(e3b;b)) ≤ C_k Σ_(j≤k) ‖ℓ‖_(C^((d_0;j))_(e3b;b)) ‖u‖_(H^((𝗌;k−j))_(e3b;b)), with the same d_0.

(b) Let B, B^♯ ∈ C^∞_b Ψ⁰_e3b with WF′_e3b(I − B^♯) ∩ WF′_e3b(B) = ∅. Then there are d_0 and C with
‖Bℓ(I − B^♯)u‖_(H^𝗌_e3b) ≤ C‖ℓ‖_(C^(d_0)_e3b)‖u‖_(H^(𝗌_0)_e3b).

*Proof.* *Smooth coefficients.* Let C^∞_e3b be the space of functions all of whose e3b-derivatives are bounded. With the
seminorms ‖·‖_(C^d_e3b) it is a Fréchet space. Such a function ℓ is a symbol of order 0, independent of the fibre
variable, for the secondary b.g. structure ρℬ. In its charts the e3b-vector fields are the uniformly bounded
combinations of the coordinate vector fields ((S6), [Hin26d, Remark 3.33]). Its quantization is multiplication by ℓ:
in the local quantization of [Hin26d, (3.26)] the cut-off ψ(x − x′) equals 1 near x = x′, so a fibre-independent symbol
is quantized to multiplication by itself, and the cut-offs χ_α of [Hin26d, Definition 3.31] sum to 1. Hence
multiplication by ℓ lies in Ψ̃⁰_e3b, which is bounded on H^𝗌_e3b ([[sec:ii-a-4-2]], with (S8)). Consider
T : ℓ ↦ (u ↦ ℓu), from C^∞_e3b to ℒ(H^𝗌_e3b). Its graph is closed. Suppose ℓ_n → ℓ in C^∞_e3b and Tℓ_n → T′. For
u ∈ H^𝗌_e3b (a distribution on ℝ^(1+4), locally in H^(inf 𝗌)), ℓ_nu → ℓu in 𝒟′. So T′u = ℓu. By the closed graph
theorem (from a Fréchet space to a Banach space), T is continuous, that is, ‖Tℓ‖ ≤ C‖ℓ‖_(C^(d_0)_e3b) for some d_0.
Likewise ℓ ↦ Bℓ(I − B^♯) ∈ ℒ(H^(𝗌_0)_e3b, H^𝗌_e3b) is well defined, as Bℓ(I − B^♯) ∈ Ψ̃⁰_e3b has empty wave front set
((S5)) and so lies in Ψ̃^(−∞)_e3b. Its graph is closed by the same argument, the convergence holding in
ℒ(H^(𝗌_0), H^(𝗌_0)). So it is bounded by C‖ℓ‖_(C^(d_0)_e3b).

*Finite regularity.* Let d_* be the largest of the numbers just found, for (a) at the orders 𝗌 and 𝗌_0 and for (b),
let K := max(0, ⌈−inf 𝗌⌉, ⌈−inf 𝗌_0⌉), and put d_0 := d_* + K + 1. Let ℓ ∈ C^(d_0)_e3b. In the charts ψ_β of ρℬ, with
a uniformly smooth partition of unity θ_β and a mollifier η_ε, put
ℓ_ε := Σ_β ((θ_βℓ) ∘ ψ_β⁻¹ ∗ η_ε) ∘ ψ_β. Derivatives commute with convolution, the charts have uniformly bounded
transitions and finite multiplicity, and e3b-derivatives are uniformly equivalent to coordinate derivatives in these
charts. Hence ‖ℓ_ε‖_(C^d_e3b) ≤ C‖ℓ‖_(C^d_e3b) for d ≤ d_0, and ℓ_ε ∈ C^∞_e3b. Moreover ℓ_ε → ℓ in C^K on compact sets.
For u ∈ H^𝗌_e3b, ℓ_εu → ℓu in 𝒟′, while ‖ℓ_εu‖_(H^𝗌) ≤ C‖ℓ‖_(C^(d_*)_e3b)‖u‖_(H^𝗌). A subsequence converges weakly in
the Hilbert space H^𝗌_e3b, which embeds continuously in 𝒟′, so its limit is ℓu. The norm is weakly lower
semicontinuous, which gives the first claim of (a). For (b), ℓ_ε(I − B^♯)u → ℓ(I − B^♯)u weakly in H^(𝗌_0), by the
first claim and the same argument. B is weakly continuous on H^(𝗌_0), and the bound holds uniformly in ε. So the limit
Bℓ(I − B^♯)u lies in H^𝗌, with the bound.

*b-regularity.* By [[eq:ii-a-8-1]] and the Leibniz rule, V^J(ℓu) = Σ (V^(J_1)ℓ)(V^(J_2)u) over splittings of J, and
‖V^(J_1)ℓ‖_(C^(d_0)_e3b) ≤ C‖ℓ‖_(C^((d_0;|J_1|))_(e3b;b)) by [[lem:ii-a-8-2]] (a). ∎

[Hin26c] states (a) as a consequence of its Lemma 3.5, whose proof is by inspection of [Hin26d, Proposition 3.32], and
uses (b) in the proof of its Proposition 3.28 for smooth ℓ, applying it to ℓ of finite regularity. Here both are proved
from (S5), (S6), (S8) and the closed graph theorem.

**Lemma {#lem:ii-a-8-6}** (Operators of limited regularity.) Let 𝒫 ⊂ C^∞_b Ψ^m_e3b be finite and
A ∈ C^((d_0;k))_(e3b;b) 𝒫, with a representation 𝐚. Let 𝗌 and N be given. There is d_0 = d_0(𝗌, m, N), independent of
k, such that:

(a) ‖Au‖_(H^((𝗌−m;k))_(e3b;b)) ≤ C_k‖𝐚‖_((d_0;k))‖u‖_(H^((𝗌;k))_(e3b;b));

(b) if G, G′ ∈ C^∞_b Ψ⁰_e3b, both carried by χ, with WF′_e3b(G) ⊂ Ell_e3b(G′), then

    ‖GAu‖_(H^((𝗌−m;k))_(e3b;b)) ≤ C_k‖𝐚‖_((d_0;k))(‖G′u‖_(H^((𝗌;k))_(e3b;b)) + ‖χu‖_(H^((−N;k))_(e3b;b))).

*Proof.* (a) [[lem:ii-a-8-5]] (a) at the order 𝗌 − m, and [[lem:ii-a-8-4]] (a) for the P_j.

(b) First k = 0. Choose G″, G‴ ∈ C^∞_b Ψ⁰_e3b carried by χ, microlocally equal to I near WF′_e3b(G), with
WF′_e3b(G″) ⊂ Ell_e3b(G′) and WF′_e3b(G‴) ∩ WF′_e3b(I − G″) = ∅. By the support convention, GAu = GAχu. Then

    Ga_jP_jχu = Ga_jP_jG″χu + Ga_j(I − G‴)P_j(I − G″)χu + Ga_jG‴P_j(I − G″)χu.

By [[lem:ii-a-8-5]] (a) and [[lem:ii-a-8-4]] (c), the first term is bounded by
C‖a_j‖_(C^(d_0))(‖G′u‖_(H^𝗌) + ‖χu‖_(H^(−N))). The second is bounded by C‖a_j‖_(C^(d_0))‖χu‖_(H^(−N)), by
[[lem:ii-a-8-5]] (b) with 𝗌_0 = −N − m. In the third, G‴P_j(I − G″) ∈ C^∞_b Ψ^(−∞)_e3b, since the wave front sets are
disjoint (S5).

For k ≥ 1, argue by induction. By [[eq:ii-a-8-1]] it suffices to bound ‖V_iGAu‖_(H^((𝗌−m;k−1))), and

    V_iGa_jP_ju = [V_i, G]a_jP_ju + G(V_ia_j)P_ju + Ga_j[V_i, P_j]u + Ga_jP_jV_iu.

The first three terms are of the form treated at level k − 1: they involve [V_i, G] (wave front set in that of G), or
the coefficients V_ia_j ∈ C^((d_0;k−1)) ([[lem:ii-a-8-2]] (b)), or the finite set 𝒫 ∪ {[V_i, P_j]}. For the last,
choose G_♭ carried by χ with WF′(G) ⊂ Ell(G_♭) and WF′(G_♭) ⊂ Ell(G′). The level k − 1 bounds it by
C‖𝐚‖(‖G_♭V_iu‖_((𝗌;k−1)) + ‖χ_1V_iu‖_((−N;k−1))), with an inner cut-off χ_1 carrying G and G_♭. Next,
‖G_♭V_iu‖_((𝗌;k−1)) ≤ ‖G_♭u‖_((𝗌;k)) + ‖[G_♭, V_i]u‖_((𝗌;k−1)), and both are bounded by
C(‖G′u‖_((𝗌;k)) + ‖χu‖_((−N;k))) ([[lem:ii-a-8-4]] (c)). Finally
‖χ_1V_iu‖_((−N;k−1)) ≤ ‖V_i(χ_1u)‖ + ‖(V_iχ_1)χu‖ ≤ C‖χu‖_((−N;k)), as χ = 1 on supp χ_1. ∎

#### Sobolev embedding {#sec:ii-a-8-5}

**Lemma {#lem:ii-a-8-7}** ([Hin26c, Lemma 3.21].) Let 𝗌 be a variable e3b-order, s̲ := max(0, ⌈−inf 𝗌⌉), and k ≥ s̲.
Then H^((𝗌;k))_(e3b;b) ⊂ H^(k−s̲)_b, continuously and with weights.

*Proof.* If s̲ = 0 then 𝗌 ≥ 0 and H^((𝗌;k)) ⊂ H^((0;k)) = H^k_b. Otherwise let A_j := V_(0,j)^(s̲), j = 1, …, N. The
symbols ξ ↦ ξ(V_(0,j)) vanish simultaneously only at ξ = 0, as the V_(0,j) span ᵉ³ᵇTM̃. So
Σ_j A_jA_j^* ∈ Diff^(2s̲)_e3b is elliptic, with a parametrix Q ∈ C^∞_b Ψ^(−2s̲)_e3b and Σ A_jA_j^*Q = I − R,
R ∈ C^∞_b Ψ^(−J)_e3b for any fixed J ≥ 0 ([[lem:ii-a-8-4]] (b) with J large). With B_j := A_j^*Q ∈ C^∞_b Ψ^(−s̲)_e3b,
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

