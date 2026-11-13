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

