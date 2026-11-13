## Null-bicharacteristic dynamics, wave-type operators and trapping of perturbed metrics {#ch:s05}

This chapter studies the null-bicharacteristic flow of a stationary model in the e3b-phase space of the compactified
spacetime of [[ch:s04]], introduces the classes of wave-type operators on which the forward problem is posed, and
proves that the stable and unstable hypersurfaces of the trapped set persist under perturbations of the metric that
decay in time. It is [Hin26c, Sections 4–6] in dimension 4 + 1.

In [Hin26c] the stationary model is a subextremal Kerr metric, and its dynamics is computed from the explicit metric:
Carter's constant, the potential of the radial motion, the expansion rates, and Dyatlov's proof of r-normal
hyperbolicity. Here no explicit metric is used. The stationary model is any metric satisfying the hypotheses (H1)–(H8)
of [[ch:s01]] and [[ch:s02]] together with the hypotheses (K1)–(K4) of [[sec:ii-b-1-1]], and the dynamics is read off
from the spectral hypotheses, which describe the flow at each frequency. The link is [[sec:ii-b-2]]: over the interior
of the Kerr face the 3b-phase space is the stationary phase space with the frequency σ as a conserved variable, and a
map Φ_(z₀) identifies the semiclassical phase space 𝒫 of [[sec:i-b-2-4]] at frequency sign z₀ with the part of the
3b-cosphere bundle over K⁺ where z₀σ ≥ 0, flows included. Near ι⁺, ℐ⁺ and the corner ∂K⁺ the metric is Minkowski to
second order by (K1), and there the flows are solved in closed form ([[sec:ii-b-3]] and [[sec:ii-b-7]]). The r-normal
hyperbolicity of the trapped set is the hypothesis (K3); for the Myers–Perry metrics near Tangherlini it is verified,
with the other dynamical hypotheses, in [[ch:s12]].

The operators are treated in [[sec:ii-c-1]]–[[sec:ii-c-5]]: stationary wave-type operators are exactly the operators
whose spectral families satisfy (H1), (H2) and (H6); admissibility at the trapped set, at the transition face and at the
radial sets fixes the thresholds; asymptotically stationary metrics come with a time function t^♭_* that is explicit;
and order functions monotone along the flow of every nearby metric are constructed. The persistence of the stable and
unstable hypersurfaces ([[sec:ii-c1-1]]–[[sec:ii-c1-3]]) is proved by a graph transform, quantitatively, from the
defining functions of the trapped set and the tangential growth bound of (K3).

The radii 0 < r₀ − 2δ₀ < r₀ < r₂ < r_h are those of [[sec:i-a-1-1]]. Nothing in this chapter depends on them beyond
these inequalities: they enter as the domains of the hypotheses, and every constant chosen from them below (the radius
r^♮ and the constant c₁ of [[lem:ii-c-3-2]], the radius r_Γ of [[sec:ii-c-5-2]]) is chosen by an inequality that a
smaller r₀ does not make harder. The inner radius r₀ is therefore a free parameter of every result of this chapter.

### The stationary model {#sec:ii-b-1}

This section fixes the stationary model, its decay at infinity and the hypotheses on its dynamics that are not part of
the spectral theory, and describes the metric and its characteristic set on the compactifications of [[ch:s04]].

### The metric and the hypotheses {#sec:ii-b-1-1}

Let P̂, E, X̃ and g be as in [[sec:i-a-1]] and [[sec:i-b-1-2]], satisfying (H1)–(H8). Thus g is a Lorentzian metric of
signature (1, 4) on ℝ_(t_*) × X̃°, X̃° = {r > r₀ − 2δ₀}, with t_*-independent components, dt_* is past timelike, and
G(ζ) := g⁻¹(ζ, ζ) satisfies G(−σ dt_* + ζ) = G₀(ζ) + στ₁(ζ) + σ²g₀₀ for ζ ∈ T*X̃° ([[eq:i-b-1-1]]). We write t_* for
the time function t of [[sec:i-b-1-2]]. Points (t_*, x) are identified with points of ℝ^(1+4) by t := t_* + r, as in
[Hin26c, p. 80], so that t_* = t − r is the function t_* of [[sec:ii-a-1]] and g becomes a metric on
M̃° ∩ {r > r₀ − 2δ₀}. The Minkowski metric is ḡ := −dt² + dx² = −dt_*² − 2 dt_* dr + r² g_(𝕊³), with g_(𝕊³) the round
metric on 𝕊³. The further hypotheses are these.

(K1) (*Decay.*) There is R > r₂ such that on {r > R} the components of g − ḡ in the frame dt_*, dx¹, …, dx⁴ lie in
ρ²C^∞(X̄), ρ = r⁻¹.

(K2) (*The spectral hypotheses.*) (H1)–(H8) hold for the spectral family P̂ of an operator whose principal symbol is G
([[sec:i-b-1-2]]).

(K3) (*r-normal hyperbolicity.*) Let Γ = Γ₁ ⊂ Σ^♭₁ be the trapped set of (H7) for z₀ = 1, let
q₁ = 2g⁻¹(−dt_* + ζ, dt_*) as in [[lem:i-b-1-1]], and let 𝖵 := q₁⁻¹ H_(G₁) on Σ^♭₁ near Γ, where
G₁(ζ) = G(−dt_* + ζ). Then Γ is eventually absolutely r-normally hyperbolic for every r for the flow of 𝖵 within Σ^♭₁,
in the sense of [HPS77, Definition 4]: there is a continuous splitting

    T_Γ Σ^♭₁ = TΓ ⊕ N̄^u ⊕ N̄^s                                                                        {#eq:ii-b-1-1}

preserved by De^(s𝖵) for all s ∈ ℝ, and there are constants μ, C > 0 and, for every ϵ > 0, a constant C_ϵ, with
|De^(s𝖵) v| ≤ C e^(−μ|s|) |v| for v ∈ N̄^u, s ≤ 0, and for v ∈ N̄^s, s ≥ 0, and |De^(s𝖵) v| ≤ C_ϵ e^(ϵ|s|) |v| for
v ∈ TΓ, s ∈ ℝ. Here |·| is any fixed fibre metric.

(K4) (*Parameters.*) When P̂ depends on b ∈ ℬ as in (H5), so does g, and ρ⁻²(g − ḡ) is bounded in C^∞(X̄ ∩ {r ≥ R})
uniformly and continuously in b; the splitting [[eq:ii-b-1-1]] depends continuously on b, and μ, C, C_ϵ are uniform.

**Remark {#rem:s05-hypotheses-k}** (a) (K1) is [Hin26c, (4.4) and Lemma 4.4] in dimension 4 + 1, with the rate r⁻²
that the mass term of a five-dimensional metric gives; Kerr has r⁻¹. For the five-dimensional Schwarzschild–Tangherlini
metric with mass parameter m, written with t_* = t − T(r), T′ = (1 + T̃)(1 − m r⁻²)⁻¹ and T̃ vanishing quadratically at
r⁻¹ = 0, the components of g − ḡ are m r⁻² (in dt_*²), −2T̃ (in dt_* dr) and −(2 + T̃)T̃(1 − m r⁻²)⁻¹ (in dr²), all in
ρ²C^∞. Unlike in four dimensions, no logarithm enters T. (b) (K3) is [Hin26c, Proposition 4.19], which is proved there
for Kerr from Carter's integrability. The splitting and the normal rates follow from (H7) as in the proof of parts
(1)–(2) of [Hin26c, Proposition 4.19]; the tangential bound is the substance of the hypothesis. (c) (K4) is
[Hin26c, Remark 4.25].

### The metric on the compactifications {#sec:ii-b-1-2}

**Lemma {#lem:ii-b-1-1}** (The metric on the compactifications.) dt_* is everywhere past timelike. Moreover:

(1) g ∈ C^∞(M; S²𝒯*) is non-degenerate on M ∩ {r > r₀ − 2δ₀}, and g − ḡ ∈ r⁻²C^∞(M; S²𝒯*) near ∂M, where 𝒯 is the
pullback of the scattering tangent bundle ([[sec:ii-a-2-1]]).

(2) g ∈ ρ_sf⁻² C^∞(M₀; S² ³ᵇT*M₀) is non-degenerate, and ρ_sf²(g − ḡ) ∈ ρ_sf² C^∞(M₀; S² ³ᵇT*M₀).

(3) g ∈ ρ₀⁻²x_I⁻²ρ₊⁻² C^∞(M; S² ᵉ³ᵇT*M) is non-degenerate, and

    ρ₀²x_I²ρ₊²(g − ḡ) ∈ ρ₀²x_I²ρ₊² C^∞(M; S² ᵉ³ᵇT*M).                                              {#eq:ii-b-1-2}

The same holds for the inverses: g⁻¹ − ḡ⁻¹ ∈ r⁻²C^∞(M; S²𝒯), and
ρ₀⁻²x_I⁻²ρ₊⁻²(g⁻¹ − ḡ⁻¹) ∈ ρ₀²x_I²ρ₊² C^∞(M; S² ᵉ³ᵇTM).

This is [Hin26c, Lemma 4.4] in dimension 4 + 1.

*Proof.* dt_* is past timelike by (H6) ([[sec:i-b-1-2]]). (1) The components of g in the frame dt_*, dx are
t_*-independent and, by (K1), smooth functions on X̄; by [[lem:ii-a-2-10]] a t_*-independent function that is smooth on
X̄ is smooth on M₁, and the blow-down M → M₁ is smooth. The forms dt_* = dt − dr, dr = ω·dx and dx are smooth sections
of 𝒯* (with ω = x/|x| smooth on X̄ near ∂X). This gives (1); on {r ≤ R} there is nothing to prove, r⁻² being bounded
there. (2) By [[def:ii-a-2-1]], ³ᵇTM₀ is spanned by r∂_t, r∂_x over M₀, so 𝒯* = r ³ᵇT*M₀ and
C^∞(M₀; S²𝒯*) = r²C^∞(M₀; S² ³ᵇT*M₀) near sf. Hence g − ḡ ∈ C^∞(M₀; S² ³ᵇT*M₀), and r⁻¹ is a defining function of
sf. Non-degeneracy: ρ_sf² ḡ is non-degenerate ([[sec:ii-a-2-2]]) and the perturbation vanishes at sf; over M₀°, g is
Lorentzian. (3) Near K⁺ away from ℐ⁺ this is (2), ρ₊ and ρ_sf being comparable there and x_I, ρ₀ positive. Near ℐ⁺,
[[lem:ii-a-2-5]] shows that C^∞(M; S²𝒯*), spanned by dt_*², dt_* dr, dr², dt_* r dω, dr r dω and r dω r dω, lies in
ρ₀⁻²x_I⁻⁴ρ₊⁻² C^∞(M; S² ᵉ³ᵇT*M), the worst term being dr² = x_I⁻² · x_I² dr². Near ℐ⁺ ∩ ι⁺, r = ρ₊⁻¹x_I⁻², and near
ℐ⁺ ∩ I⁰, r = ρ₀⁻¹x_I⁻² ([[sec:ii-a-1]]). So r⁻² ∈ ρ₀²x_I⁴ρ₊² C^∞ near ℐ⁺, and g − ḡ ∈ C^∞(M; S² ᵉ³ᵇT*M) there,
which is [[eq:ii-b-1-2]]. Non-degeneracy follows as in (2), with ρ₀²x_I²ρ₊² ḡ non-degenerate ([[def:ii-a-2-8]]). The
inverses: ḡ has constant components in the frame dt, dx, so g⁻¹ = ḡ⁻¹ − ḡ⁻¹hḡ⁻¹ + …, h := g − ḡ, converges for r
large, and its terms after the first lie in r⁻²C^∞(M; S²𝒯). In e3b-terms, 𝒯 ⊂ ρ₊ ᵉ³ᵇTM near ℐ⁺ ∩ ι⁺ by
∂_(t_*) = ρ₊(−ρ₊∂_(ρ₊) + ½x_I∂_(x_I)), ∂_r = −½ρ₊x_I² · x_I∂_(x_I) and r⁻¹∂_ω = ρ₊x_I · x_I∂_ω ([[sec:ii-a-2-3]]),
and likewise with ρ₀ near ℐ⁺ ∩ I⁰; so g⁻¹ − ḡ⁻¹ ∈ r⁻²ρ₀²ρ₊² C^∞(S² ᵉ³ᵇTM) = ρ₀⁴x_I⁴ρ₊⁴ C^∞ near ℐ⁺, and near K⁺
the same follows from (2). ∎

In [Hin26c, (4.9)] the factor on the right of [[eq:ii-b-1-2]] is ρ₀x_I²ρ₊; the gain is the rate r⁻² of (K1). Nothing
below needs more than the rate of [Hin26c], except that errors vanish to second order at ι⁺ and ∂K⁺, which shortens two
proofs.

### Characteristic sets {#sec:ii-b-1-3}

Following [Hin26c, (4.11)], put g⁻¹_(e3b) := ρ₀⁻²x_I⁻²ρ₊⁻² g⁻¹ and

    Σ := {ζ ∈ ᵉ³ᵇT*M ∖ o : g⁻¹_(e3b)(ζ, ζ) = 0} = Σ⁺ ⊔ Σ⁻,                                         {#eq:ii-b-1-3}

where ζ ∈ Σ⁺ ∩ T*M° if and only if g⁻¹(ζ, ·) is a future directed null vector; Σ⁻ = −Σ⁺, and Σ^± are the closures in
ᵉ³ᵇT*M ∖ o. Their boundaries at fibre infinity are ∂Σ^± ⊂ ᵉ³ᵇS*M. Fix defining functions ρ_∞ of ᵉ³ᵇS*M and x_I, ρ₊ of
ℐ⁺, ι⁺, and put, as in [Hin26c, (4.71)],

    𝖧_G := ρ_∞ x_I⁻²ρ₊⁻² H_G,                                                                        {#eq:ii-b-1-4}

an e3b-vector field on ᵉ³ᵇT*_Ω M tangent to ᵉ³ᵇS*M; on Σ it equals ρ_∞ H_(x_I⁻²ρ₊⁻²G). Near K⁺ it is, on Σ, a positive
smooth multiple of the rescaled 3b-fields of [[sec:ii-b-2]]–[[sec:ii-b-6]], and near ℐ⁺ of the eb-field of
[[sec:ii-b-7]]. Positive multiples of a vector field have the same integral curves up to an increasing
reparametrisation, and all statements below are invariant under such a change.

**Lemma {#lem:ii-b-1-2}** (Future covectors.) (a) For every ζ ∈ Σ⁺ ∩ T*M°, H_G t_* > 0. (b) There is R₁ ≥ R such that
∂_(t_*) is future directed timelike on {r ≥ R₁}; there, every −σ dt_* + ζ ∈ Σ⁺ has σ > 0. (c) For a null covector
ν = −σ dt_* + ζ over X̃°, ν ∈ Σ⁺ if and only if g⁻¹(ν, dt_*) > 0.

*Proof.* (c) −∇t_* is future directed timelike ([[sec:i-b-1-2]]), and a future directed null vector has negative inner
product with it; so ν^♯ is future directed if and only if g(ν^♯, −∇t_*) < 0, that is, g⁻¹(ν, dt_*) > 0. (a) At ν,
H_G t_* = 2g⁻¹(ν, dt_*); use (c). (b) By (K1), g(∂_(t_*), ∂_(t_*)) = −1 + O(r⁻²), so ∂_(t_*) is timelike for r large;
it is future directed, since g(∂_(t_*), −∇t_*) = −dt_*(∂_(t_*)) = −1. For ν ∈ Σ⁺ there, ν(∂_(t_*)) = g(ν^♯, ∂_(t_*))
< 0, and ν(∂_(t_*)) = −σ. ∎

By (c), in the notation of [[lem:i-b-1-1]], Σ⁺ ∩ {σ = z₀} is the component Σ⁺_(z₀) = Σ_(z₀) ∩ {q_(z₀) > 0}, on which
the future field is +H_(G_(z₀)) ([[sec:i-b-1-3]]), and the future component of the characteristic set at fibre infinity
of T*X̃° is ∂Σ₀⁺, the one containing ∂ℛ₊, with future field +ρ_∞ H_(G₀) ((H3) and [[lem:i-b-1-1]] (e)).

### The Kerr face and the stationary phase space {#sec:ii-b-2}

Over the Kerr face K⁺ the Hamilton vector field of G preserves the frequency σ, and at each fixed σ it is the Hamilton
vector field of the stationary symbol. This section identifies the 3b-cosphere bundle over K⁺ with the compactified
phase spaces of [[ch:s02]], flows included.

### The 3b-phase space over K⁺ {#sec:ii-b-2-1}

Over M₀ ∩ {r > r₀ − 2δ₀} write 3b-covectors as −σ dt_* + ζ, ζ ∈ T*X̃°. By [[def:ii-a-2-1]] the 3b-fibre coordinates
are r(−σ, ζ) in the frame dual to r∂_(t_*), r∂_x, so (σ, ζ) are fibre coordinates up to the positive factor r, smooth
over M₀°. Near (K⁺)°, with ρ_K := t_*⁻¹, the 3b-vector fields are spanned by ∂_(t_*) = −ρ_K²∂_(ρ_K) and ∂_x
([[sec:ii-a-2-2]]; [Hin26c, Section 6.1]).

**Lemma {#lem:ii-b-2-1}** (The field over K⁺.) The Hamilton vector field H_G on ³ᵇT*M₀ over {r > r₀ − 2δ₀} is tangent
to ³ᵇT*_(K⁺)M₀ and annihilates σ, and its restriction to ³ᵇT*_((K⁺)°)M₀ = ℝ_σ × T*X̃° is, at each fixed σ, the
Hamilton vector field of ζ ↦ G(−σ dt_* + ζ) on T*X̃°.

*Proof.* In canonical coordinates (t_*, x; τ, ζ), τ = −σ,
H_G = (∂_τ G)∂_(t_*) + (∂_ζ G)∂_x − (∂_(t_*)G)∂_τ − (∂_x G)∂_ζ. G is t_*-independent, so the ∂_τ-component vanishes
and H_G σ = 0, and ∂_(t_*) = −ρ_K²∂_(ρ_K) vanishes at ρ_K = 0. The remaining components are those of the Hamilton
field of G(τ, ·) on T*X̃° at fixed τ. ∎

### The identification {#sec:ii-b-2-2}

The 3b-cosphere bundle over K⁺ is ³ᵇS*_(K⁺)M₀ = K⁺ × 𝕊⁴: [[def:ii-a-2-1]] trivialises ³ᵇTM₀ globally, and
K⁺ ≅ ℝ̄⁴ (the radial compactification of ℝ⁴; [[lem:ii-a-2-10]]), with boundary ∂K⁺ = K⁺ ∩ ι⁺, defined within K⁺ by
ρ₊ = r⁻¹. In the trivialisation the class of −σ dt_* + ζ is [σ : ζ] (homogeneous coordinates, up to positive
multiples), since the trivialisation differs from (σ, ζ) by the positive factor r and the smooth fibre-linear map from
dt to dt_* (dt = dt_* + ω·dx, smooth on X̄). Recall 𝒫 = ℝ̄⁴ × ℝ̄⁴ ([[sec:i-b-2-4]]), with fibre infinity
ℝ̄⁴ × ∂ℝ̄⁴ and the face over ∂X.

**Definition {#def:ii-b-2-2}** For z₀ ∈ {1, −1}, Φ_(z₀) : 𝒫 → ³ᵇS*_(K⁺)M₀ is Φ_(z₀)(x, ζ) := (x, [z₀ : ζ]), the class
of the covector −z₀ dt_* + ζ, extended to fibre infinity by Φ_(z₀)(x, θ∞) := (x, [0 : θ]).

**Lemma {#lem:ii-b-2-3}** (a) Φ_(z₀) is a diffeomorphism of manifolds with corners onto
K⁺ × {[σ : ζ] : z₀σ ≥ 0}, mapping fibre infinity onto {σ = 0} and the face over ∂X onto the part over ∂K⁺.

(b) Put G_(3b) := r²G, which near sf is a smooth fibre-quadratic function on ³ᵇT*M₀ ([[lem:ii-b-1-1]] (2)), and let
ρ̃_∞ := r⁻¹(σ² + |ζ|²)^(−1/2), a defining function of 3b-fibre infinity over K⁺. Then
ρ̃_∞² G_(3b) ∘ Φ_(z₀) = a Ĝ_(z₀) with a smooth and positive on 𝒫 and Ĝ_(z₀) = ρ_∞² G_(z₀) as in [[lem:i-b-4-1]]. So
Φ_(z₀) maps Σ_(z₀) ⊂ 𝒫 onto the characteristic set of G_(3b) in K⁺ × {z₀σ ≥ 0}.

(c) On Σ_(z₀), (Φ_(z₀))_* 𝖧_(z₀) = a′ ρ̃_∞ H_(G_(3b)) with a′ smooth and positive, where 𝖧_(z₀) = μ⁻¹H_(G_(z₀)) is the
field of [[eq:i-b-4-1]].

(d) Φ_(z₀) maps Σ⁺_(z₀) ∩ T*X̃° onto Σ⁺ ∩ ³ᵇT*_((K⁺)°) ∩ {z₀σ > 0} (classes), and ∂Σ₀⁺ onto Σ⁺ ∩ {σ = 0} at fibre
infinity. Over ∂K⁺, Σ⁺ lies in {σ > 0}, and Φ₁ maps Σ₁ ∩ {ρ = 0}, the characteristic set of [[eq:i-a-4-7]] at
σ₀ = 1, onto it. Σ⁺ ∩ {σ ≤ 0} lies over {r < R₁}.

*Proof.* (a) ℝ̄⁴_ζ is diffeomorphic to the closed hemisphere {z₀σ ≥ 0} ⊂ 𝕊⁴ by ζ ↦ [z₀ : ζ]: this is the standard
model of the radial compactification, whose boundary {|ζ| = ∞} goes to the equator {σ = 0}, smoothly with smooth
inverse ([z₀ : ζ] = [z₀|ζ|⁻¹ : ζ/|ζ|] near the equator, and |ζ|⁻¹ is a boundary defining function of ℝ̄⁴). In the
base it is the identity of X̄ ≅ K⁺, which maps ∂X to ∂K⁺. (b) G_(3b)(−z₀ dt_* + ζ) = r²G_(z₀)(x, ζ) and
ρ̃_∞ = r⁻¹⟨ζ⟩⁻¹ at σ = ±1, so ρ̃_∞² G_(3b) = ⟨ζ⟩⁻² G_(z₀) = Ĝ_(z₀) with the choice ρ_∞ = ⟨ζ⟩⁻¹ of [[ch:s02]]; for
another choice of ρ_∞ the quotient is smooth and positive. Both sides are homogeneous of degree 0 in (σ, ζ), so the
identity extends to fibre infinity and to the face over ∂X by continuity. (c) By the Leibniz rule,
H_(G_(3b)) = r²H_G + G H_(r²), and on the characteristic set G = 0, so H_(G_(3b)) = r²H_G there. H_G at a covector
with σ = z₀ is tangent to {σ = z₀} and, in the coordinates (x, ζ) there, is H_(G_(z₀)) ([[lem:ii-b-2-1]]); and Φ_(z₀)
restricted to {σ = z₀} is the projection to the cosphere bundle. Since H_G is homogeneous of degree 1 in the fibre,
ρ̃_∞ H_(G_(3b)) descends to the cosphere bundle, and at points of Φ_(z₀)(Σ_(z₀) ∩ T*X̃°)

    ρ̃_∞ H_(G_(3b)) = r⁻¹⟨ζ⟩⁻¹ r² H_(G_(z₀)) = r⟨ζ⟩⁻¹ μ 𝖧_(z₀).

With μ = ⟨ζ⟩⟨x⟩⁻¹ ([[lem:i-b-4-1]] (c): H_p ∈ μ ρ_∞^(2−k) 𝒱_b for order (k, 0)), a′ = ⟨x⟩r⁻¹, smooth and positive on
𝒫. The identity extends by continuity to the faces of 𝒫, both sides being smooth vector fields there
([[lem:i-b-4-1]] (c); [[lem:ii-b-1-1]] (2)). (d) The first two statements are [[lem:ii-b-1-2]] (c) and the paragraph
after it, with (H3) at fibre infinity. Over ∂K⁺, ρ₊ = 0 and G_(3b) is the Minkowski function
Ḡ_(3b) = −2σ_(3b)ξ_(3b) + ξ_(3b)² + |η_(3b)|² of [[sec:ii-b-3-1]], on whose characteristic set σ_(3b) < 0 on Σ⁺
([Hin26c, p. 81]: dt_* is past causal for ḡ), with σ_(3b) = −rσ ([[sec:ii-b-3-1]]), so σ > 0. The last statement is
[[lem:ii-b-1-2]] (b). ∎

Hence the future 3b-flow over K⁺ splits into three invariant pieces: {σ > 0}, the image under Φ₁ of the future
component Σ^♭₁ = Σ⁺₁ of [[sec:i-b-1-5]] together with its face over ∂X; {σ = 0}, the image of ∂Σ₀⁺ at fibre infinity;
and {σ < 0}, the image under Φ₋₁ of Σ⁺₋₁, which lies over {r < R₁}. On each, the rescaled future 3b-field is a positive
multiple of the future field of [[ch:s01]] and [[ch:s02]]: +𝖧₁, +ρ_∞ H_(G₀), resp. +𝖧₋₁ ([[lem:ii-b-2-3]] (c),
[[lem:ii-b-1-2]] and the paragraph after it).
