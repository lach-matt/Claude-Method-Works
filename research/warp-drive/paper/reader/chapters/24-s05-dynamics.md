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

#### The metric and the hypotheses {#sec:ii-b-1-1}

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

#### The metric on the compactifications {#sec:ii-b-1-2}

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

#### Characteristic sets {#sec:ii-b-1-3}

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

#### The 3b-phase space over K⁺ {#sec:ii-b-2-1}

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

#### The identification {#sec:ii-b-2-2}

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

### The 3b-dynamics near ∂K⁺ and over ι⁺ {#sec:ii-b-3}

Near the corner ∂K⁺ = K⁺ ∩ ι⁺ and over ι⁺ the metric is Minkowski to second order, and the rescaled Hamilton vector
field is, up to an error vanishing to second order at ρ₊ = 0, an explicit field whose flow is solved in closed form.

#### The Minkowski model {#sec:ii-b-3-1}

Near K⁺ ∩ ι⁺ use ρ_K := r/t_*, ρ₊ := r⁻¹ and ω. (In [[sec:ii-b-2]] and [[sec:ii-b-4]], ρ_K is t_*⁻¹, a defining
function of K⁺ away from ι⁺, and in [[sec:ii-b-7]] and [[sec:ii-b-8]], ρ₊ is t_*⁻¹, a defining function of ι⁺ near ℐ⁺;
the two meanings of each meet only over ι⁺, where both vanish.) Write 3b-covectors as

    ζ = σ_(3b) dt_*/r + ξ_(3b) dr/r + η_(3b),        η_(3b) ∈ T*𝕊³,                                  {#eq:ii-b-3-1}

so that −σ dt_* + ξ dr + η has σ_(3b) = −rσ, ξ_(3b) = rξ, η_(3b) = η. In the scattering coordinates ξ dr + r η_sc of
[[sec:i-a-1-4]], η_sc = r⁻¹η. The Minkowski function is

    Ḡ_(3b) := r² ḡ⁻¹(ζ, ζ) = −2σ_(3b)ξ_(3b) + ξ_(3b)² + |η_(3b)|²                                    {#eq:ii-b-3-2}

([Hin26c, (4.13)], with |·| the round norm on 𝕊³; it follows from ḡ⁻¹ = −2∂_(t_*) ⊗_s ∂_r + ∂_r² + r⁻² g_(𝕊³)⁻¹). By
[[lem:ii-b-1-1]] (the inverses) and 𝒯 = r⁻¹ ³ᵇTM₀, g⁻¹ − ḡ⁻¹ ∈ r⁻⁴C^∞(S² ³ᵇTM₀), so
G_(3b) − Ḡ_(3b) ∈ ρ₊² P^[2](³ᵇT*M₀) near K⁺ ∩ ι⁺, where G_(3b) := r²G and P^[2] denotes the fibrewise quadratic
polynomials with smooth coefficients. By [[eq:ii-a-2-1]], with r∂_(t_*) = −ρ_K²∂_(ρ_K) and
r∂_r = ρ_K∂_(ρ_K) − ρ₊∂_(ρ₊),

    H_(Ḡ_(3b)) = 2(ξ_(3b) − σ_(3b))(ρ_K∂_(ρ_K) − ρ₊∂_(ρ₊) + σ_(3b)∂_(σ_(3b))) + 2σ_(3b)ξ_(3b)∂_(ξ_(3b))
                 + 2ξ_(3b)ρ_K²∂_(ρ_K) + H_(|η_(3b)|²).

The error H_(G_(3b) − Ḡ_(3b)) lies in ρ₊² 𝒱_b(³ᵇT*M₀): for p = ρ₊²q, H_p = ρ₊²H_q + 2qρ₊H_(ρ₊), and
H_(ρ₊) = −((r∂_r)ρ₊)∂_(ξ_(3b)) = ρ₊∂_(ξ_(3b)) by [[eq:ii-a-2-1]].

Since Ḡ_(3b) = (ξ_(3b) − σ_(3b))² + |η_(3b)|² − σ_(3b)², σ_(3b) ≠ 0 on Σ over ι⁺, and σ_(3b) < 0 on Σ⁺ there
([Hin26c, p. 81]). Near ∂Σ⁺ over a neighbourhood of ι⁺ use

    ρ_∞ := −σ_(3b)⁻¹,        ξ̂ := ξ_(3b)/σ_(3b),        η̂ := η_(3b)/σ_(3b).                          {#eq:ii-b-3-3}

Then ρ_∞² Ḡ_(3b) = ξ̂² − 2ξ̂ + |η̂|², and 𝖧̄ := ρ_∞ H_(Ḡ_(3b)) satisfies, exactly,

    𝖧̄ρ_K = 2(1 − ξ̂)ρ_K − 2ξ̂ρ_K²,     𝖧̄ρ₊ = −2(1 − ξ̂)ρ₊,     𝖧̄ρ_∞ = −2(1 − ξ̂)ρ_∞,
    𝖧̄ξ̂ = −2(2 − ξ̂)ξ̂,     𝖧̄η̂ = −2(1 − ξ̂)η̂ + ∂_ω|η̂|²,     𝖧̄ω = −∂_(η̂)|η̂|²,                       {#eq:ii-b-3-4}

which is [Hin26c, (4.15)]. For instance H_(Ḡ_(3b))ξ_(3b) = 2σ_(3b)ξ_(3b) and
H_(Ḡ_(3b))σ_(3b) = 2(ξ_(3b) − σ_(3b))σ_(3b) give H_(Ḡ_(3b))ξ̂ = 2σ_(3b)ξ̂(2 − ξ̂), and ρ_∞ = −σ_(3b)⁻¹. The full
rescaled field 𝖧 := ρ_∞ H_(G_(3b)) is 𝖧̄ + 𝖧̃ with 𝖧̃ ∈ ρ₊²𝒱_b, tangent to ³ᵇS*M₀ and to the boundary faces. In
particular 𝖧̃ρ₊ ∈ ρ₊³C^∞ and 𝖧̃ρ_K ∈ ρ₊²ρ_K C^∞, and over ι⁺ the flow of 𝖧 is that of 𝖧̄. None of this depends on
the dimension.

**Definition {#def:ii-b-3-1}** (The radial sets over ∂K⁺; [Hin26c, Definition 4.5].)
∂R_(∂K⁺,in) := {ρ_K = ρ₊ = 0, ξ̂ = 2, η̂ = 0} and ∂R_(∂K⁺,out) := {ρ_K = ρ₊ = 0, ξ̂ = 0, η̂ = 0}, subsets of ∂Σ⁺ over
∂K⁺. Their conic extensions are {ξ_(3b) = 2σ_(3b) < 0, η_(3b) = 0} and {ξ_(3b) = 0, σ_(3b) < 0, η_(3b) = 0} over ∂K⁺.

Under Φ₁ these are R_(1,in) and R_out of [[eq:i-a-4-6]] at σ₀ = 1: there ξ = −2σ₀, η = 0, resp. ξ = 0, η = 0, and
ξ̂ = ξ_(3b)/σ_(3b) = −ξ/σ.

*Linearisation* ([Hin26c, (4.16)]). 𝖧 vanishes on both sets. On ∂Σ⁺, ξ̂ is near each of them a smooth function of
(ρ_K, ρ₊, η̂), and by [[eq:ii-b-3-4]] and the error bounds, the linearisation of 𝖧 on the conormal spaces is
dρ_K ↦ −2dρ_K, dρ₊ ↦ 2dρ₊, dη̂ ↦ 2dη̂ at ∂R_(∂K⁺,in), and dρ_K ↦ 2dρ_K, dρ₊ ↦ −2dρ₊, dη̂ ↦ −2dη̂ at ∂R_(∂K⁺,out)
(the term ∂_ω|η̂|² is quadratic in η̂, and 𝖧̃ vanishes to second order at ρ₊ = 0). Also ρ_∞⁻¹𝖧ρ_∞ = 2, resp. −2,
there.

#### The flow over ι⁺ and over ∂K⁺ in closed form {#sec:ii-b-3-2}

**Lemma {#lem:ii-b-3-2}** (a) (*Over ∂K⁺.*) On ∂Σ⁺ over ∂K⁺, ξ̂ ∈ [0, 2], and every maximal integral curve of 𝖧 not
contained in ∂R_(∂K⁺,in) ∪ ∂R_(∂K⁺,out) is, after a shift of the parameter, ξ̂(s) = 2/(1 + e^(4s)), defined for all
s, tending to ∂R_(∂K⁺,in) as s → −∞ and to ∂R_(∂K⁺,out) as s → ∞.

(b) (*Over ι⁺.*) On ∂Σ⁺ over (ι⁺)°, use u := t_*/r = ρ_K⁻¹ ∈ (0, ∞). Along a maximal integral curve of 𝖧,

    ξ̂′ = −2(2 − ξ̂)ξ̂,        u′ = −2(1 − ξ̂)u + 2ξ̂,        |η̂|² = ξ̂(2 − ξ̂).                       {#eq:ii-b-3-5}

Exactly one of the following holds. (i) ξ̂ ≡ 0, η̂ ≡ 0, u = u₀e^(−2s): the curve lies in
∂W_out := {ρ₊ = 0, ξ̂ = 0, η̂ = 0}, tends to ∂R_(∂K⁺,out) (u → ∞) as s → −∞ and to ℐ⁺ (u → 0) as s → ∞. (ii) ξ̂ ≡ 2,
η̂ ≡ 0, u = Ae^(2s) − 2 with A > 0 and s > ½ log(2/A): the curve lies in ∂W_in := {ρ₊ = 0, ξ̂ = 2, η̂ = 0}, tends to
∂R_(∂K⁺,in) as s → ∞, and reaches u = 0 as s decreases to ½ log(2/A). (iii) After a shift of the parameter,
ξ̂ = 2/(1 + e^(4s)) and

    u = (C − e^(−2s))/cosh 2s,        C > 0,        s > −½ log C;                                       {#eq:ii-b-3-6}

u → 0 both as s ↓ −½ log C and as s → ∞, and u has one interior maximum.

(c) The angular coordinates converge at each end of each curve in (a) and (b).

*Proof.* Over ι⁺, 𝖧 = 𝖧̄ and ρ_∞² G_(3b) = ξ̂² − 2ξ̂ + |η̂|² there, so on ∂Σ⁺, |η̂|² = ξ̂(2 − ξ̂) and ξ̂ ∈ [0, 2].
[[eq:ii-b-3-5]] is [[eq:ii-b-3-4]] with u = ρ_K⁻¹: u′ = −ρ_K⁻²ρ_K′ = −2(1 − ξ̂)u + 2ξ̂. The logistic equation for ξ̂
has the constant solutions 0, 2 and, on (0, 2), the solutions 2/(1 + e^(4(s − s₁))). (a) Over ∂K⁺ (ρ_K = ρ₊ = 0) only
ξ̂, η̂, ω move; ξ̂ ∈ {0, 2} forces η̂ = 0, a zero of 𝖧, so a non-constant curve has ξ̂ ∈ (0, 2). (b) Consider the
linear equation for u. If ξ̂ ≡ 0, u′ = −2u; if ξ̂ ≡ 2, u′ = 2u + 4. Otherwise, with ξ̂ = 2/(1 + e^(4s)),
1 − ξ̂ = tanh 2s, the homogeneous solution is exp(−2∫tanh 2s ds) = (cosh 2s)⁻¹, and p := −e^(−2s)/cosh 2s is a
particular solution: p′ and −2(1 − ξ̂)p + 2ξ̂ both equal 2/cosh² 2s, by cosh 2s + sinh 2s = e^(2s) and
2ξ̂ = 4/(1 + e^(4s)) = 2e^(−2s)/cosh 2s. So u = (C − e^(−2s))/cosh 2s, positive if and only if C > e^(−2s); C ≤ 0 is
excluded. In case (iii), u ∼ 2Ce^(−2s) → 0 as s → ∞, and u = 0 at s = −½ log C. As u > 0 on the open interval and
u → 0 at both ends, u has an interior maximum, unique by [[lem:ii-b-3-3]] (3) below. In cases (i) and (ii) the limits
are read off. (c) By [[eq:ii-b-3-4]], |ω′| ≤ 2|η̂| in the round metric, and |η̂|² = ξ̂(2 − ξ̂) decays exponentially at
each infinite end (ξ̂ ∼ 2e^(−4s) or 2 − ξ̂ ∼ 2e^(4s)) and is bounded on the finite ends, so ω converges. ∎

The finite end in (b) (ii) and (iii) is not a limit point in ᵉ³ᵇS*M: as u = x_I² → 0 the 3b-coordinates degenerate,
and the curve continues over ℐ⁺ ∩ ι⁺ in the eb-coordinates of [[sec:ii-b-7]], where the end is reached only as the
eb-parameter tends to −∞ ([[lem:ii-b-7-3]]).

#### Convexity and invariant manifolds {#sec:ii-b-3-3}

**Lemma {#lem:ii-b-3-3}** The flow of 𝖧 on ∂Σ⁺ over K⁺ ∪ ι⁺ near ∂K⁺ has the following properties.

(1) (*Convexity in K⁺.*) There is ϵ > 0 such that over K⁺, if 𝖧ρ₊ = 0 and 0 < ρ₊ < ϵ, then 𝖧²ρ₊ < 0.

(2) (*Curves over K⁺.*) Let γ : I → ∂Σ⁺ be a maximal integral curve over K⁺, not contained in
∂R_(∂K⁺,in) ∪ ∂R_(∂K⁺,out), with ρ₊(γ(0)) < ϵ. If (d/ds)ρ₊(γ(s)) ≤ 0 at s = 0, then γ(s) → ∂R_(∂K⁺,out) as s → ∞; if
it is ≥ 0, then γ(s) → ∂R_(∂K⁺,in) as s → −∞.

(3) (*Convexity in ι⁺.*) Over ι⁺, if 𝖧ρ_K = 0 and ρ_K > 0, then 𝖧²ρ_K > 0.

(4) (*Invariant manifolds over ι⁺.*) ∂W_out is the unstable manifold of ∂R_(∂K⁺,out) and ∂W_in the stable manifold
of ∂R_(∂K⁺,in) over ι⁺ ([[lem:ii-b-3-2]] (b)). Their conic extensions are, within Σ⁺, the characteristic sets of r∂_r
and of 2r∂_(t_*) − r∂_r over ι⁺.

This is [Hin26c, Lemma 4.6] in dimension 4 + 1.

*Proof.* (1) Over K⁺ (ρ_K = 0), 𝖧ρ₊ = −2(1 − ξ̂)ρ₊ + ρ₊³a with a smooth, by [[sec:ii-b-3-1]]. So 𝖧ρ₊ = 0 with
ρ₊ > 0 gives 1 − ξ̂ = ½ρ₊²a, and on ∂Σ⁺, ξ̂² − 2ξ̂ + |η̂|² = O(ρ₊²), so ξ̂ = 1 + O(ρ₊²). Then

    𝖧²ρ₊ = 2ρ₊𝖧ξ̂ − 2(1 − ξ̂)𝖧ρ₊ + 𝖧(ρ₊³a) = 2ρ₊(−2(2 − ξ̂)ξ̂ + O(ρ₊²)) + O(ρ₊³) = −4ρ₊ + O(ρ₊³),

using 𝖧ρ₊ = 0 at the point and 𝖧̃ξ̂ = O(ρ₊²). This is negative for ρ₊ < ϵ, ϵ small.

(2) If ρ₊(γ(0)) = 0, γ lies over ∂K⁺ (the face is invariant, 𝖧ρ₊ ∈ ρ₊C^∞), and [[lem:ii-b-3-2]] (a) applies. Let
ρ₊(γ(0)) ∈ (0, ϵ) and f := ρ₊ ∘ γ, with f′(0) ≤ 0. Then f > 0 throughout, {ρ₊ = 0} being invariant. At any s with
f′(s) = 0 and f(s) < ϵ, f″(s) < 0 by (1). Hence f′ < 0 on (0, sup I): if f′(0) < 0, or f′(0) = 0 and then
f″(0) < 0, then f′ < 0 on some (0, δ); at a first zero s₁ > 0 of f′, f(s₁) < f(0) < ϵ, so f″(s₁) < 0, while f′ < 0
on (0, s₁) forces f″(s₁) ≥ 0. So f is strictly decreasing for s > 0, γ stays in the compact set {ρ₊ ≤ ϵ} ∩ ∂Σ⁺ over
K⁺, sup I = ∞, and f → L ∈ [0, ϵ). The ω-limit set Ω_γ is non-empty, compact and invariant, and ρ₊ = L on it. If
L > 0, the curve through a point of Ω_γ has ρ₊ ≡ L, so 𝖧ρ₊ = 𝖧²ρ₊ = 0 there, against (1). So L = 0. For s > 0,
𝖧ρ₊ < 0, that is 1 − ξ̂ > ½ρ₊²a, so ξ̂ ≤ 1 + Cϵ² along γ and on Ω_γ. Ω_γ lies over ∂K⁺, where the flow is that of
[[lem:ii-b-3-2]] (a). If Ω_γ contained a point with ξ̂ ∈ (0, 2), it would contain its backward orbit, on which ξ̂ → 2,
against ξ̂ ≤ 1 + Cϵ². So ξ̂ = 0, hence η̂ = 0, on Ω_γ: Ω_γ ⊂ ∂R_(∂K⁺,out), which is the claim. The case f′(0) ≥ 0 is
the same with −𝖧, for which (1) holds as well since (−𝖧)² = 𝖧², and with the roles of ξ̂ = 0 and ξ̂ = 2 exchanged.

(3) Over ι⁺, 𝖧 = 𝖧̄. If 𝖧ρ_K = 0, then 1 − ξ̂ = ξ̂ρ_K and

    𝖧²ρ_K = −2ρ_K(1 + ρ_K)𝖧ξ̂ + (2(1 − ξ̂) − 4ξ̂ρ_K)𝖧ρ_K = 4ρ_K(1 + ρ_K)ξ̂(2 − ξ̂) = 4ρ_K(1 + ρ_K)|η̂|².

If η̂ = 0, then ξ̂ ∈ {0, 2} and 𝖧ρ_K = 2ρ_K, resp. −2ρ_K − 4ρ_K², which is not zero for ρ_K > 0. So 𝖧²ρ_K > 0.

(4) By [[lem:ii-b-3-2]] (b), the curves over ι⁺ that tend to ∂R_(∂K⁺,out) as s → −∞ are those of (i), and those that
tend to ∂R_(∂K⁺,in) as s → ∞ are those of (ii). The conic extensions are {ξ_(3b) = 0, η_(3b) = 0, σ_(3b) < 0} and
{ξ_(3b) = 2σ_(3b), η_(3b) = 0, σ_(3b) < 0} over ι⁺. These are the intersections with Σ⁺ of the characteristic sets of
r∂_r and of 2r∂_(t_*) − r∂_r (on Σ, ξ_(3b) = 0 and ξ_(3b) = 2σ_(3b) each force η_(3b) = 0 by [[eq:ii-b-3-2]]), with
which a 3b-covector [[eq:ii-b-3-1]] pairs to ξ_(3b), resp. 2σ_(3b) − ξ_(3b). In the coordinates (t, r), t = t_* + r,
these fields are r(∂_t + ∂_r) and r(∂_t − ∂_r), the outgoing and incoming null fields of ḡ: ∂_t|_r = ∂_(t_*) and
∂_r|_t = ∂_r − ∂_(t_*). ∎

The uniqueness of the interior maximum of u in [[lem:ii-b-3-2]] (b) (iii) is (3): u = ρ_K⁻¹, and at a zero of 𝖧ρ_K,
𝖧²u = −ρ_K⁻²𝖧²ρ_K < 0, so every critical point of u is a strict local maximum, and there is at most one.

### The horizon at K⁺ {#sec:ii-b-4}

**Definition {#def:ii-b-4-1}** (The horizon radial set; [Hin26c, Definition 4.8].)
R_(ℋ⁺) := {ρ_K = 0, σ = 0, ζ ∈ ℛ₊} ⊂ ³ᵇT*_((K⁺)°)M₀ ∖ o, with ℛ₊ the component of N*ℋ ∖ o of (H3), and ∂R_(ℋ⁺) is its
boundary at fibre infinity, which is Φ_(±1)(∂ℛ₊).

Near ∂R_(ℋ⁺) let ρ_∞ be the function of (H3), positive and homogeneous of degree −1 in ζ, put σ̂ := σρ_∞ and
𝖧 := ρ_∞H_G; on Σ this is a positive multiple of [[eq:ii-b-1-4]]. As ζ ≠ 0 there, (x, [ζ], σ̂), [ζ] ∈ S*X̃°, are
coordinates on ³ᵇS*_((K⁺)°)M₀ near ∂R_(ℋ⁺), in which ∂R_(ℋ⁺) = {σ̂ = 0} × ∂ℛ₊.

**Lemma {#lem:ii-b-4-2}** Let q̃ be the function of [[lem:i-a-4-1]] for ℛ = ℛ₊, regarded as a function of (x, [ζ]).
There are C_F, c > 0 and a neighbourhood W of ∂R_(ℋ⁺) in ³ᵇS*_((K⁺)°)M₀ such that F := q̃ + C_F σ̂² is a quadratic
defining function of ∂R_(ℋ⁺) and 𝖧F ≥ cF on W. At ∂R_(ℋ⁺),

    ρ_∞⁻¹𝖧ρ_∞ = β₀ > 0,        ρ_K⁻²𝖧ρ_K = ρ_∞τ₁ ≤ −ββ₀ < 0,                                         {#eq:ii-b-4-1}

with β₀, β of (H3). So ∂R_(ℋ⁺) is a repeller for the flow within ³ᵇS*_((K⁺)°)M₀ (not only within ∂Σ⁺), ρ_∞ grows
along the flow near it, and ρ_K decays. This is [Hin26c, Lemma 4.9 and (4.28)].

*Proof.* For a function f(x, [ζ]), independent of σ and t_* and homogeneous of degree 0 in ζ, [[lem:ii-b-2-1]] and
G = G₀ + στ₁ + σ²g₀₀ give

    𝖧f = 𝖧₀f + σ̂ H_(τ₁)f + σ̂² ρ_∞⁻¹H_(g₀₀)f,        𝖧₀ := ρ_∞H_(G₀),                                  {#eq:ii-b-4-2}

where H_(τ₁)f and ρ_∞⁻¹H_(g₀₀)f = −ρ_∞⁻¹(∂_x g₀₀)·∂_ζ f are homogeneous of degree 0 and smooth near ∂ℛ₊. 𝖧₀ is the
field of (H3), extended off Σ₀ by the same formula, as in [[lem:i-a-4-1]], which gives 𝖧₀q̃ ≥ c′q̃ on a neighbourhood
of ∂ℛ₊ in S*X̃°. As q̃ is smooth and vanishes quadratically at ∂ℛ₊, with q̃ ≥ c″dist², |dq̃| ≤ Cq̃^(1/2), so
|H_(τ₁)q̃| ≤ Cq̃^(1/2). Hence 𝖧q̃ ≥ c′q̃ − C|σ̂|q̃^(1/2) − Cσ̂² ≥ (c′/2)q̃ − C₁σ̂². Next, 𝖧σ = 0 ([[lem:ii-b-2-1]]), so
𝖧σ̂ = σ̂ρ_∞⁻¹𝖧ρ_∞, and

    ρ_∞⁻¹𝖧ρ_∞ = H_Gρ_∞ = β₀ + σ̂ρ_∞⁻¹H_(τ₁)ρ_∞ + σ̂²ρ_∞⁻²H_(g₀₀)ρ_∞,        β₀ := ρ_∞⁻¹𝖧₀ρ_∞,

the last two coefficients being homogeneous of degree 0. By (H3), β₀ ≥ c_β > 0 near ∂ℛ₊ for some constant c_β, so on
{|σ̂| ≤ δ}, ρ_∞⁻¹𝖧ρ_∞ ≥ c_β/2 and 𝖧(σ̂²) ≥ c_βσ̂². With C_F ≥ 2(C₁ + 1)/c_β,

    𝖧F ≥ (c′/2)q̃ + (C_F c_β − C₁)σ̂² ≥ (c′/2)q̃ + (C_F c_β/2)σ̂² ≥ min(c′/2, c_β/2) F.

In the coordinates (x, [ζ], σ̂), q̃ is a quadratic defining function of ∂ℛ₊ in S*X̃° ([[lem:i-a-4-1]]), so F is one of
{σ̂ = 0} × ∂ℛ₊. For [[eq:ii-b-4-1]]: at σ̂ = 0, ρ_∞⁻¹𝖧ρ_∞ = β₀. With τ := −σ the dual variable of t_*,
H_G t_* = ∂_τG = −τ₁ − 2σg₀₀, so 𝖧t_* = −ρ_∞τ₁ at σ = 0, and 𝖧ρ_K = −ρ_K²𝖧t_*. By (H3), −β₀⁻¹ρ_∞τ₁ ≥ β on ∂ℛ₊. ∎

In the Kerr coordinates of [Hin26c], F corresponds to σ̂₀² + ρ_∞²𝒞 of [Hin26c, Lemma 4.9].

### The trapped set at K⁺ {#sec:ii-b-5}

**Definition {#def:ii-b-5-1}** (The trapped set at K⁺; [Hin26c, (4.63)].) ∂Γ_(K⁺) := Φ₁(Γ), with Γ = Γ₁ the trapped
set of (H7) at z₀ = 1, and ∂Γ̄^(u/s)_(K⁺) := Φ₁(Γ̄_(u/s)), with Γ̄_(u/s) ⊂ Σ^♭₁ the global backward and forward trapped
sets of (H8); Γ^(u/s)_(K⁺) := Φ₁(Γ_(u/s)) for the local sets of (H7) in O.

**Lemma {#lem:ii-b-5-2}** (a) ∂Γ_(K⁺) is a compact invariant subset of ∂Σ⁺ ∩ ³ᵇS*_((K⁺)°)M₀, lying over
{r₂ < r < ρ₁⁻¹} and in {σ > 0}: σ is positive, hence elliptic, there ([Hin26c, (4.64)]). (b) ∂Γ̄^(u/s)_(K⁺) are
invariant, and consist of the points whose integral curves tend to ∂Γ_(K⁺) backward, resp. forward. Near ∂Γ_(K⁺),
Γ^u_(K⁺) and Γ^s_(K⁺) are smooth hypersurfaces of ∂Σ⁺ ∩ {σ > 0}, tangent to the flow, meeting transversally in
∂Γ_(K⁺), and, after shrinking O, ∂Γ̄^(u/s)_(K⁺) ∩ Φ₁(O) = Γ^(u/s)_(K⁺). (c) No integral curve tends to ∂Γ_(K⁺) in both
directions unless it lies in ∂Γ_(K⁺). (d) Under Φ₁, the field 𝖵 of (K3) is the projection of H_G/(H_G t_*) at σ = 1,
so (K3) is [Hin26c, Proposition 4.19] for the stationary model, with the quotient by t_*-translations and fibre
dilations realised by the slice {σ = 1} of ³ᵇT*_((K⁺)°)M₀.

*Proof.* (a), (b): Φ₁ is a diffeomorphism onto its image which maps Σ⁺₁ = Σ^♭₁ into ∂Σ⁺ ∩ {σ > 0} and the future
field to a positive multiple of the future field ([[lem:ii-b-2-3]] (c), (d)); (H7) and (H8) (b) transfer, and
Γ ⊂ T*{r₂ < r < ρ₁⁻¹} is compact by (H7). (c) Let γ tend to ∂Γ_(K⁺) in both directions. Then
γ ⊂ ∂Γ̄^u_(K⁺) ∩ ∂Γ̄^s_(K⁺), and for |s| large γ(s) ∈ Φ₁(O), so γ(s) ∈ Γ^u_(K⁺) ∩ Γ^s_(K⁺) = ∂Γ_(K⁺) by (b) and (H7)
(Γ_u ∩ Γ_s = Γ within O). ∂Γ_(K⁺) is invariant, so γ ⊂ ∂Γ_(K⁺). (d) At σ = 1, H_G t_* = −τ₁ − 2g₀₀ = q₁ (proof of
[[lem:ii-b-4-2]]; [[lem:i-b-1-1]] (b)), and by [[lem:ii-b-2-1]] the restriction of H_G to {σ = 1} acts on (x, ζ) as
H_(G₁). ∎

### The dynamics over the Kerr face {#sec:ii-b-6}

**Proposition {#prop:ii-b-6-1}** (Dynamics over the Kerr face.) Let γ : I → ∂Σ⁺ ∩ ³ᵇS*_(K⁺)M₀, over
{r > r₀ − 2δ₀}, be a maximal integral curve of the field [[eq:ii-b-1-4]], not contained in ∂R_(∂K⁺,in),
∂R_(∂K⁺,out), ∂R_(ℋ⁺) or ∂Γ_(K⁺). Then:

(1) as s increases, γ tends to ∂Γ_(K⁺) or to ∂R_(∂K⁺,out), or reaches {r < r₀ − δ₀} at a finite parameter;

(2) as s → −∞, γ tends to ∂Γ_(K⁺), to ∂R_(∂K⁺,in) or to ∂R_(ℋ⁺);

(3) γ does not tend to ∂Γ_(K⁺) in both directions.

Moreover, γ tends to ∂Γ_(K⁺) forward (backward) if and only if it lies in ∂Γ̄^s_(K⁺) (∂Γ̄^u_(K⁺)); a curve over ∂K⁺
goes from ∂R_(∂K⁺,in) to ∂R_(∂K⁺,out); and a curve in {σ ≤ 0} goes from ∂R_(ℋ⁺) to {r < r₀ − δ₀}.

"Tends to A" means that every limit point lies in A; for a set A of fixed points this is the convergence of [Hin26c].
This is [Hin26c, Proposition 4.21] in dimension 4 + 1.

*Proof.* The sign of σ is constant along γ ([[lem:ii-b-2-1]], the rescaling being positive), and the faces ∂K⁺ and
(K⁺)° are invariant. A curve in a compact set has a non-empty, compact, connected and invariant ω-limit set, and
likewise α-limit set; so "tends to A ∪ B", with A and B disjoint compact sets, means "tends to A or tends to B".

*σ > 0.* By [[lem:ii-b-2-3]], γ = Φ₁ ∘ γ̃ up to an increasing reparametrisation, with γ̃ a maximal integral curve of the
future field 𝖧₁ in Σ⁺₁ = Σ^♭₁, finite or over ∂X. Over ∂X (that is, γ over ∂K⁺), [[lem:i-a-4-5]] at σ₀ = 1, or
[[lem:ii-b-3-2]] (a), gives the claim. Otherwise γ̃ lies in Σ₁ ∩ T*{r > r₀ − 2δ₀}, and (H8) (a) applies. If
γ̃ ⊄ Γ̄_u, it tends backward to ∂ℛ₊ ∪ ∂ℛ₋ or to R_(1,in); not to ∂ℛ₋, since at fibre infinity q̂₁ = −ρ_∞τ₁ is negative
near ∂ℛ₋ by (H3), while q₁ > 0 along γ̃. Under Φ₁, ∂ℛ₊ is ∂R_(ℋ⁺) and R_(1,in) is ∂R_(∂K⁺,in) ([[def:ii-b-3-1]]). If
γ̃ ⊄ Γ̄_s, it tends forward to R_out, which is ∂R_(∂K⁺,out), or reaches {r < r₀ − δ₀}. If γ̃ ⊂ Γ̄_u (resp. Γ̄_s), it
tends to Γ backward (forward), by the definition of these sets. (3) is [[lem:ii-b-5-2]] (c).

*σ = 0.* γ lies in Φ_(±1)(∂Σ₀⁺) at fibre infinity of the stationary phase space, with the future field +ρ_∞H_(G₀) up to
a positive factor ([[lem:ii-b-2-3]]). By (H4) it tends backward to ∂ℛ₊ ∪ ∂ℛ₋, hence to ∂ℛ₊, the components ∂Σ₀^± being
disjoint, compact and invariant; and it reaches {r < r₀ − δ₀} forward at a finite parameter.

*σ < 0.* γ = Φ₋₁ ∘ γ̃ with γ̃ a maximal integral curve of the future field in Σ⁺₋₁, which lies over {r < R₁}
([[lem:ii-b-2-3]] (d)), so its limit points are not over ∂X. Γ₋₁ ⊂ Σ^♭₋₁ = Σ⁻₋₁, and q₋₁ ≤ −2β₀ < 0 near Γ₋₁ by
(Γ.4), while q₋₁ > 0 on γ̃; so γ̃ lies in neither Γ̄_u nor Γ̄_s. By (H8) (a), γ̃ tends backward to ∂ℛ₊ (not to ∂ℛ₋,
as before, nor to R_(−1,in), which lies over ∂X), and reaches {r < r₀ − δ₀} forward (not R_out, over ∂X). ∎

### The eb-dynamics near ℐ⁺ {#sec:ii-b-7}

Near ℐ⁺ ∩ ι⁺ use ρ₊ = t_*⁻¹, x_I = (t_*/r)^(1/2) and ω ([[sec:ii-a-1]]) and eb-covectors
σ_(eb) dρ₊/ρ₊ + ξ_(eb) dx_I/x_I + η_(eb) dω/x_I ([[def:ii-a-2-4]]), and put G_(eb) := x_I⁻²ρ₊⁻²G. Since
dρ₊/ρ₊ = −ρ₊ dt_* and dx_I/x_I = ½ρ₊(dt_* − x_I² dr), the covector is
ν = ρ₊(½ξ_(eb) − σ_(eb)) dt_* − ½ρ₊x_I²ξ_(eb) dr + x_I⁻¹η_(eb) dω, and ḡ⁻¹(ν, ν) = −2ν_(t_*)ν_r + ν_r² + r⁻²|ν_ω|²
with r⁻² = ρ₊²x_I⁴ gives

    Ḡ_(eb) = ½ξ_(eb)(ξ_(eb) − 2σ_(eb)) + |η_(eb)|² + ¼x_I²ξ_(eb)².                                     {#eq:ii-b-7-1}

This is the inverse of the form of ḡ near ℐ⁺ ∩ ι⁺ of [[sec:ii-a-2-3]], whose angular term is g_(𝕊³)/(2x_I²). By
[[lem:ii-b-1-1]] (the inverses), G_(eb) − Ḡ_(eb) ∈ x_I²ρ₊² P^[2](ᵉᵇT*M), so

    G_(eb) ≡ G⁰_(eb) := ½ξ_(eb)(ξ_(eb) − 2σ_(eb)) + |η_(eb)|²        modulo x_I² P^[2],

and as H_(x_I) = −x_I∂_(ξ_(eb)) by [[eq:ii-a-2-2]], H_(G_(eb)) ≡ H_(G⁰_(eb)) modulo x_I²𝒱_eb(ᵉᵇT*M), where, by
[[eq:ii-a-2-2]],

    H_(G⁰_(eb)) = −ξ_(eb)ρ₊∂_(ρ₊) + (ξ_(eb) − σ_(eb))(x_I∂_(x_I) + η_(eb)∂_(η_(eb))) − 2|η_(eb)|²∂_(ξ_(eb))
                  + x_I H_(|η_(eb)|²)                                                                  {#eq:ii-b-7-2}

([Hin26c, p. 96], here on T*𝕊³).

*The sign of σ_(eb).* σ_(eb) = ν(ρ₊∂_(ρ₊)), and at fixed x_I, ρ₊∂_(ρ₊) = −(t_*∂_(t_*) + r∂_r) = −(t∂_t + r∂_r). The
vector field V := t∂_t + r∂_r has ḡ(V, V) = −t_*² − 2t_*r, and by (K1),
|g(V, V) − ḡ(V, V)| ≤ Cr⁻²(t_* + r)² ≤ ½(t_*² + 2t_*r) on Ω ∩ {r ≥ R₂} for R₂ large (t_* ≥ 1). So V is timelike there,
and future directed: g(V, −∇t_*) = −dt_*(V) = −t_* < 0. For ν ∈ Σ⁺ over M° there, ν(V) < 0, so σ_(eb) = −ν(V) > 0; on
Σ over ℐ⁺, σ_(eb) = 0 would force ½ξ_(eb)² + |η_(eb)|² = 0, so σ_(eb) > 0 on Σ⁺ near ℐ⁺ ∩ ι⁺ ([Hin26c, p. 96]). Put

    ρ_∞ := σ_(eb)⁻¹,     ξ̂ := ξ_(eb)/σ_(eb),     η̂ := η_(eb)/σ_(eb),     𝖧 := ρ_∞H_(G_(eb)).             {#eq:ii-b-7-3}

Then ρ_∞²G⁰_(eb) = ½ξ̂(ξ̂ − 2) + |η̂|², and 𝖧⁰ := ρ_∞H_(G⁰_(eb)) satisfies, exactly (H_(G⁰_(eb))σ_(eb) = 0),

    𝖧⁰ρ₊ = −ξ̂ρ₊,     𝖧⁰x_I = (ξ̂ − 1)x_I,     𝖧⁰ρ_∞ = 0,     𝖧⁰ξ̂ = −2|η̂|²,
    𝖧⁰η̂ = (ξ̂ − 1)η̂ − x_I∂_ω|η̂|²,                                                                      {#eq:ii-b-7-4}

which is [Hin26c, (4.67)]; 𝖧 − 𝖧⁰ ∈ x_I²𝒱_eb, tangent to ᵉᵇS*M.

**Definition {#def:ii-b-7-1}** (The radial sets at ℐ⁺; [Hin26c, Definition 4.22].)
∂R_(ℐ⁺,out) := {x_I = 0, ξ̂ = 0, η̂ = 0} over ℐ⁺ (all ρ₊), and ∂R_(ℐ⁺,in,+) := {ρ₊ = 0, x_I = 0, ξ̂ = 2, η̂ = 0} over
ℐ⁺ ∩ ι⁺; their conic extensions lie in {σ_(eb) > 0}.

By [[eq:ii-b-7-4]], with ξ̂ a function of (ρ₊, x_I, η̂) on ∂Σ⁺ near each set, the linearisation of 𝖧 is
dx_I ↦ −dx_I, dη̂ ↦ −dη̂ at ∂R_(ℐ⁺,out), and dρ₊ ↦ −2dρ₊, dx_I ↦ dx_I, dη̂ ↦ dη̂ at ∂R_(ℐ⁺,in,+) ([Hin26c, (4.69)]);
the error vanishes to second order at x_I = 0. So the first set is a sink transversally to its ρ₊-fibres, and the
second a saddle.

**Lemma {#lem:ii-b-7-2}** (1) (*Over ℐ⁺.*) On ∂Σ⁺ over ℐ⁺, ξ̂ ∈ [0, 2] and |η̂|² = ½ξ̂(2 − ξ̂), and along integral
curves

    ξ̂′ = −ξ̂(2 − ξ̂),        ρ₊′ = −ξ̂ρ₊.                                                              {#eq:ii-b-7-5}

A maximal integral curve over ℐ⁺ ∩ Ω not contained in ∂R_(ℐ⁺,out) ∪ ∂R_(ℐ⁺,in,+) is one of the following.
(i) ξ̂ = 2/(1 + e^(2s)), ρ₊ = A(1 + e^(−2s)) with 0 < A < 1: forward it tends to ∂R_(ℐ⁺,out) (at ρ₊ = A), backward it
reaches {t_* = 1} at a finite parameter. (ii) The same with A = 0, over ℐ⁺ ∩ ι⁺: from ∂R_(ℐ⁺,in,+) to ∂R_(ℐ⁺,out).
(iii) ξ̂ ≡ 2, η̂ ≡ 0, ρ₊ = ρ₊(0)e^(−2s), ρ₊(0) > 0: forward it tends to ∂R_(ℐ⁺,in,+), backward it reaches {t_* = 1}.

(2) (*Convexity in ι⁺.*) Over ι⁺, if 𝖧x_I = 0 and x_I > 0, then 𝖧²x_I < 0.

(3) (*Invariant manifolds.*) ∂W_(ℐ⁺) := {ξ̂ = 2, η̂ = 0} over ℐ⁺ is the stable manifold of ∂R_(ℐ⁺,in,+) within ∂Σ⁺
over ℐ⁺; in the present coordinates, ∂W_out of [[lem:ii-b-3-3]] (4) is {ρ₊ = 0, ξ̂ = 0, η̂ = 0}.

This is [Hin26c, Lemma 4.23] in dimension 4 + 1.

*Proof.* (1) Over ℐ⁺, 𝖧 = 𝖧⁰ and ρ_∞²G_(eb) = ½ξ̂(ξ̂ − 2) + |η̂|², so on ∂Σ⁺, |η̂|² = ½ξ̂(2 − ξ̂), and
[[eq:ii-b-7-4]] gives [[eq:ii-b-7-5]]. If ξ̂(0) ∈ {0, 2} then η̂ = 0; ξ̂ ≡ 0 gives a point of ∂R_(ℐ⁺,out), and ξ̂ ≡ 2
gives (iii) or, at ρ₊ = 0, a point of ∂R_(ℐ⁺,in,+). Otherwise ξ̂ = 2/(1 + e^(2s)) after a shift,
ρ₊′/ρ₊ = −2/(1 + e^(2s)), and ρ₊ = A(1 + e^(−2s)). On Ω, ρ₊ ≤ 1, so A < 1 if A > 0, and ρ₊ increases as s decreases
and reaches 1 at a finite parameter. The angular coordinates do not move: |ω′| ≤ 2x_I|η̂| = 0 over ℐ⁺. The limits of
ξ̂, η̂ and ρ₊ are read off. (2) Over (ι⁺)°, x_I² = u = ρ_K⁻¹, and by [[lem:ii-b-7-3]] below 𝖧 is a positive multiple
c𝖧^(3b) of the field of [[sec:ii-b-3]] on Σ. At a zero of 𝖧x_I, 𝖧^(3b)ρ_K = 0, and
𝖧²x_I = c²(𝖧^(3b))²x_I = −½c²ρ_K^(−3/2)(𝖧^(3b))²ρ_K < 0 by [[lem:ii-b-3-3]] (3). (3) ∂W_(ℐ⁺) is invariant by
[[eq:ii-b-7-5]] and consists of the curves (iii) and the points of ∂R_(ℐ⁺,in,+); curves over ℐ⁺ with ξ̂ ≠ 2 tend to
∂R_(ℐ⁺,out) by (1). The last statement is [[lem:ii-b-7-3]] at ξ̂_(3b) = 0. ∎

**Lemma {#lem:ii-b-7-3}** (3b and eb over ι⁺.) Over (ι⁺)°, with u = x_I² = t_*/r and the 3b-coordinates
[[eq:ii-b-3-1]], [[eq:ii-b-3-3]], σ_(eb) = −σ_(3b)(u + ξ̂_(3b)), ξ_(eb) = −2ξ_(3b) and η_(eb) = x_Iη_(3b); hence

    ξ̂_(eb) = 2ξ̂_(3b)/(u + ξ̂_(3b)),     η̂_(eb) = −x_Iη̂_(3b)/(u + ξ̂_(3b)),     𝖧 = (u/(u + ξ̂_(3b))) 𝖧^(3b) on Σ,
                                                                                                        {#eq:ii-b-7-6}

with 𝖧^(3b) := −σ_(3b)⁻¹H_(G_(3b)) as in [[sec:ii-b-3]]. Consequently, in [[lem:ii-b-3-2]] (b), the curves (ii) and (iii)
tend to ∂R_(ℐ⁺,in,+) as the eb-parameter tends to −∞, and the curves (i) and (iii) tend to ∂R_(ℐ⁺,out) as s → ∞.

*Proof.* The identity −σ dt_* + ξ dr + η = σ_(3b) dt_*/r + ξ_(3b) dr/r + η_(3b) and the formula for ν above give
σ_(eb) = σt_* − ξr = −σ_(3b)u − ξ_(3b), ξ_(eb) = −2ξr = −2ξ_(3b) and η_(eb) = x_Iη_(3b). On Σ⁺ over ι⁺, σ_(3b) < 0 and
ξ̂_(3b) ∈ [0, 2], so u + ξ̂_(3b) > 0. Also G_(eb) = x_I⁻²ρ₊⁻²G = rt_*G = uG_(3b), so H_(G_(eb)) = uH_(G_(3b)) on Σ,
and σ_(eb)⁻¹ = −σ_(3b)⁻¹(u + ξ̂_(3b))⁻¹. For the limits: in (ii) and (iii) the 3b-parameter reaches the end s₀ with
u → 0 and ξ̂_(3b) → ξ̂₀ ∈ (0, 2]; by [[eq:ii-b-3-5]], u′ = 2ξ̂₀ + O(u) there, so u ∼ 2ξ̂₀(s − s₀), and the eb-parameter
∫(u + ξ̂_(3b))u⁻¹ ds diverges to −∞; along the way ξ̂_(eb) → 2 and η̂_(eb) → 0 by [[eq:ii-b-7-6]], and ω converges
([[lem:ii-b-3-2]] (c)): the limit lies in ∂R_(ℐ⁺,in,+). As s → ∞ in (iii), ξ̂_(3b) ∼ 2e^(−4s), |η̂_(3b)| ∼ 2e^(−2s) and
u ∼ 2Ce^(−2s), so ξ̂_(eb) ∼ (2/C)e^(−2s) → 0 and |η̂_(eb)| ≲ e^(−s) → 0; in (i), ξ̂_(3b) = 0 and ξ̂_(eb) = η̂_(eb) = 0
while u → 0. In both cases ρ₊ = 0 and x_I → 0: the limit lies in ∂R_(ℐ⁺,out). ∎

### The global dynamics in e3b-phase space {#sec:ii-b-8}

**Proposition {#prop:ii-b-8-1}** (Curves over the boundary.) Let γ be a maximal integral curve of [[eq:ii-b-1-4]] in
∂Σ⁺ over ∂M̃ ∩ Ω ∩ {r > r₀ − 2δ₀}, that is, over (ℐ⁺ ∩ Ω) ∪ ι⁺ ∪ K⁺. Say that γ is of type (A, B) if it tends to A
backward (or reaches A at a finite parameter, for A = {t_* = 1}) and to B forward (or reaches B, for
B = {r < r₀ − δ₀}). Write R^K_(in/out) := ∂R_(∂K⁺,in/out), R^I_in := ∂R_(ℐ⁺,in,+), R^I_out := ∂R_(ℐ⁺,out),
R_ℋ := ∂R_(ℋ⁺), Γ_K := ∂Γ_(K⁺) and r₋ := {r < r₀ − δ₀}. Then γ lies in one of ∂R_(ℋ⁺), ∂R_(ℐ⁺,in,+),
∂R_(∂K⁺,in), ∂Γ_(K⁺), ∂R_(∂K⁺,out), ∂R_(ℐ⁺,out), or it is of one of the following types.

| over | A | B |
|---|---|---|
| (ℐ⁺)° ∩ Ω | {t_* = 1} | R^I_in, R^I_out |
| ℐ⁺ ∩ ι⁺ | R^I_in | R^I_out |
| (ι⁺)° | R^I_in | R^K_in, R^I_out |
| (ι⁺)° | R^K_out | R^I_out |
| ∂K⁺ | R^K_in | R^K_out |
| (K⁺)° | R_ℋ, R^K_in | r₋, Γ_K, R^K_out |
| (K⁺)° | Γ_K | r₋, R^K_out |

In the order {t_* = 1}, ∂R_(ℋ⁺), ∂R_(ℐ⁺,in,+), ∂R_(∂K⁺,in), ∂Γ_(K⁺), ∂R_(∂K⁺,out), {r < r₀ − δ₀}, ∂R_(ℐ⁺,out), every
curve goes from an earlier set to a later one, as in [Hin26c, Figure 4.3]; with [[prop:ii-b-8-2]] this holds for every
curve over Ω. This is [Hin26c, Proposition 4.24] in dimension 4 + 1, for the curves over the boundary.

*Proof.* [[eq:ii-b-1-4]] is a b-vector field on ᵉ³ᵇS*M, so it is tangent to every boundary hypersurface, and each open
stratum of the boundary is invariant: (ℐ⁺)°, ℐ⁺ ∩ ι⁺, (ι⁺)°, ∂K⁺ = K⁺ ∩ ι⁺ and (K⁺)° (within Ω). Over (K⁺)° and ∂K⁺
the claim is [[prop:ii-b-6-1]]. Over (ι⁺)° it is [[lem:ii-b-3-2]] (b), with the ends at u = 0 identified by
[[lem:ii-b-7-3]]; case (i) of [[lem:ii-b-3-2]] (b) is the fourth row, cases (ii) and (iii) the third. Over ℐ⁺ it is
[[lem:ii-b-7-2]] (1). ∎

**Proposition {#prop:ii-b-8-2}** (Curves over the interior.) Let γ be a maximal integral curve of [[eq:ii-b-1-4]] in
∂Σ⁺ over M° ∩ Ω ∩ {r > r₀ − δ₀}, extended maximally within {r > r₀ − 2δ₀} ∩ Ω. Then γ reaches {t_* = 1} backward at
a finite parameter, and forward either reaches {r < r₀ − δ₀} at a finite parameter or tends to the e3b-cosphere bundle
over (ℐ⁺ ∩ Ω) ∪ ι⁺ ∪ K⁺: over ι⁺ ∪ K⁺ if t_* → ∞ along γ, over ℐ⁺ otherwise. This is [Hin26c, Proposition 6.1] for
the stationary model.

*Proof.* On ∂Σ⁺ over M°, ρ_∞H_G t_* = 2ρ_∞g⁻¹(ν, dt_*) > 0 for the null covectors ν there ([[lem:ii-b-1-2]] (c)), so
[[eq:ii-b-1-4]] increases t_*, at a rate bounded below by a positive constant on compact subsets of ∂Σ⁺ over
M° ∩ {r > r₀ − 2δ₀}. On {r < r₂}, H_G r = 2g⁻¹(ν, dr) < 0 for future null ν, as dr is future timelike there ((H4) and
[[sec:i-b-1-2]]: ∇r is future timelike, so ν(∇r) < 0); so backward r increases while r < r₂, and γ cannot leave
through {r = r₀ − 2δ₀} backward. The faces at infinity are invariant, so γ is defined until it reaches {t_* = 1} or
{r < r₀ − δ₀}.

*Forward.* If t_* → ∞, every limit point lies over {t_* = ∞} ∩ Ω = ι⁺ ∪ K⁺. If t_* stays bounded and γ does not reach
{r < r₀ − δ₀}, then sup I = ∞, and a limit point p over M° would be visited infinitely often, each visit to a fixed
small neighbourhood of p lasting a parameter time bounded below (the field is bounded) and increasing t_* by a fixed
amount: so t_* → ∞, a contradiction. The limit points therefore lie over ∂M̃ at finite t_* ≥ 1, which within Ω is ℐ⁺.

*Backward.* Suppose that γ does not reach {t_* = 1}; then inf I = −∞ and t_* ↓ L ≥ 1. As above, no limit point lies
over M°, so the α-limit set 𝒜 lies over ℐ⁺ ∩ {t_* = L}; it is non-empty, compact and invariant, and ρ₊ = L⁻¹ on it.
A curve in 𝒜 has ρ₊ constant, hence ξ̂ = 0 by [[eq:ii-b-7-5]] (ρ₊ > 0), hence η̂ = 0: 𝒜 ⊂ ∂R_(ℐ⁺,out). Near
∂R_(ℐ⁺,out), 𝖧x_I = (ξ̂ − 1)x_I + O(x_I³) ≤ −½x_I, so on a tail (−∞, s₁] of γ the function x_I ∘ γ > 0 increases as s
decreases and cannot tend to 0, a contradiction. ∎

**Remark {#rem:ii-b-8-3}** The sets of [[prop:ii-b-8-1]] and [[prop:ii-b-8-2]] that depend on the stationary model are
∂R_(ℋ⁺), through ℛ₊, and ∂Γ_(K⁺), through Γ. Under (H5), extended to (H6)–(H8) in [[sec:i-b-1-5]], and (K4), both
depend continuously on the parameter b, with the constants of [[lem:ii-b-4-2]] and of (K3) uniform; the radial sets
over ∂K⁺ and ℐ⁺ do not depend on b. This is [Hin26c, Remark 4.25].

### Stationary wave-type operators {#sec:ii-c-1}

This section and the four that follow are [Hin26c, Sections 5–6] in dimension 4 + 1, except [Hin26c, Proposition 6.3],
which is [[prop:ii-c1-3-4]]. The definitions are restated at n = 4: the constant 1 of [Hin26c, (5.1a)] becomes
3/2 = (n − 1)/2, the weight α_sf + 3/2 of the tf-admissibility of [Hin26c] becomes α_sf + 2, and the stationary model
is that of [[sec:ii-b-1]], a metric satisfying (K1)–(K4) together with (H1)–(H8), in place of Kerr. [Hin26c,
Proposition 6.4], which [Hin26c] proves by reference to the construction of [Hin23c, Lemma 5.8 and Appendix C], is
proved by that construction, written out in the coordinates of [[sec:ii-b-3]] and [[sec:ii-b-7]] and with the error
terms of the present class.

#### The class {#sec:ii-c-1-1}

Throughout, g is the stationary metric of [[sec:ii-b-1-1]], which satisfies (K1)–(K4), E_X := X̃ × ℂ^N is the trivial
bundle of [[sec:i-a-1-2]], and E := π_X^*E_X is its pullback along π_X(t_*, x) := x. Sections of E are ℂ^N-valued
functions, and ∂_(t_*) and ρ∂_ρ act componentwise; the connection of [Hin26c, Remark 5.3], needed for non-trivial
bundles, is not needed here. We write G(ζ) := g⁻¹(ζ, ζ) and ρ := r⁻¹, and ρ₁ is that of [[sec:i-a-1-1]]. The density is
|dt_* dx| = |dt dx|, the Euclidean density of [[sec:i-a-1-1]] times |dt_*|, and for a fibre inner product h
([[sec:i-a-1-2]]), A^(*h) and Im_h A := (A − A^(*h))/2i are taken with respect to it.

**Definition {#def:ii-c-1-1}** (Stationary wave-type operators; [Hin26c, Definition 5.1] at n = 4.) A
t_*-translation-invariant P₀ ∈ Diff²(ℝ_(t_*) × X̃°; E) is a *stationary wave-type operator* (for g) if (1)
σ₂(P₀) = G Id, and (2) on {ρ < ρ₁},

    P₀ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S) + P̂₀(0) + Q∂_(t_*) − g₀₀∂_(t_*)²,                                 {#eq:ii-c-1-1}

with g₀₀ := g⁻¹(dt_*, dt_*) and, all t_*-independent, P̂₀(0) ∈ ρ²Diff²_b(X̄; E), S ∈ C^∞(X̄; End ℂ^N) and
Q ∈ ρ³Diff¹_b(X̄; E). Put ([Hin26c, (5.2)])

    S̄ := inf_(p∈∂X) min Re spec S(p).

**Remark {#rem:s05-p0-representation}** (a) g₀₀ ∈ ρ²C^∞(X̄) by (K1): ḡ⁻¹(dt_*, dt_*) = 0, and the components of
g⁻¹ − ḡ⁻¹ in the frame ∂_(t_*), ∂_x lie in ρ²C^∞(X̄) ([[lem:ii-b-1-1]], the inverses). (b) The representation
[[eq:ii-c-1-1]] is not unique: a zeroth-order term may be moved between 2ρS∂_(t_*) and Q∂_(t_*) ([Hin26c, Remark 5.2]).
But S|_(∂X) is determined by P₀. Indeed, if (S, Q) and (S′, Q′) both represent P₀, the parts linear in σ of the spectral
families ([[lem:ii-c-1-2]]) give 2ρ(S − S′) = −(Q − Q′); the left side is of order 0, so Q − Q′ is a multiplication by
an element of ρ³C^∞, and S − S′ ∈ ρ²C^∞.

**Lemma {#lem:ii-c-1-2}** (The spectral family; [Hin26c, (5.10)].) Let P₀ be a stationary wave-type operator. Then
P̂(σ) := e^(iσt_*)P₀e^(−iσt_*) = P̂₀(0) + σT + σ²g₀₀ with T := 2iρ(ρ∂_ρ − 3/2 − S) − iQ on {ρ < ρ₁}, and P̂ satisfies
(H1) and (H2) of [[sec:i-a-1-3]] and (H6) of [[sec:i-b-1-2]], with this g. Conversely, if a family
P̂(σ) = P̂(0) + σT + σ²P₂ satisfies (H1), (H2) and (H6), then P₀ := P̂(0) + T i∂_(t_*) − P₂∂_(t_*)²
([[sec:i-b-1-2]]) is a stationary wave-type operator for the metric of (H6).

*Proof.* e^(iσt_*)∂_(t_*)e^(−iσt_*) = ∂_(t_*) − iσ acts as −iσ on t_*-independent sections, which gives the form and T;
and P₀ = P̂(0) + T i∂_(t_*) − g₀₀∂_(t_*)². The principal symbol of P₀ at −σ dt_* + ζ is
σ₂(P̂(0))(ζ) + σ σ₁(T)(ζ) + σ²g₀₀, as σ₁(i∂_(t_*))(−σ dt_* + ζ) = i · i · (−σ) = σ. By [[eq:i-b-1-1]],
G(−σ dt_* + ζ) = G₀(ζ) + στ₁(ζ) + σ²g₀₀, so condition (1) of [[def:ii-c-1-1]] is equivalent to the three identities of
(H1) (σ₂(P̂(0)) = G₀ Id, σ₁(T) = τ₁ Id, P₂ = g₀₀ Id), the parts of different degree in σ being separate. (H2): the
first two equations of [[eq:i-a-1-2]] are the form of T and P̂(0) = ρ²P^(0) with P^(0) ∈ Diff²_b, and g₀₀ ∈ ρ²C^∞ is
[[rem:s05-p0-representation]] (a). For the normalisation of P^(0), write spatial covectors as
ξ dr + η = ξ_b dρ/ρ + η, so ξ_b = −rξ; then σ₂(ρ²((ρD_ρ)² + Δ_(𝕊³))) = ρ²(ξ_b² + |η|²) = ξ² + r⁻²|η|² = ḡ⁻¹(ζ, ζ)
for ζ = ξ dr + η. The components of ζ in the frame dt_*, dx are bounded by C(|ξ| + r⁻¹|η|), so by
[[rem:s05-p0-representation]] (a), G₀(ζ) − ḡ⁻¹(ζ, ζ) ∈ ρ² · ρ²P^[2](ᵇT*X̄), P^[2] the fibrewise quadratic polynomials
with smooth coefficients. Hence σ₂(P^(0)) − (ξ_b² + |η|²) ∈ ρ²P^[2], and
P^(0) − ((ρD_ρ)² + Δ_(𝕊³))Id ∈ Diff¹_b + ρ²Diff²_b. (H6) is a hypothesis on g, which (K2) includes. The converse
reads the same identities backwards: the form of T in (H2) gives [[eq:ii-c-1-1]]. ∎

So the stationary wave-type operators for g are the operators whose spectral families satisfy (H1), (H2) and (H6), and
(K2) asks (H3)–(H5) and (H7)–(H8) of them in addition.

#### Tensor wave operators {#sec:ii-c-1-2}

**Lemma {#lem:ii-c-1-3}** (Tensor wave operators; [Hin26c, Example 5.4] at n = 4.) Identify (p, q)-tensors on ℝ^(1+4)
with ℂ^N-valued functions, N = 5^(p+q), by the coordinate frame of (t_*, x¹, …, x⁴) (for 1-forms, the frame dt_*, dx^i
of [[sec:i-a-1-2]]). Let ∇ be the Levi-Civita connection of g and □_g^((p,q)) := −g^(μν)∇_μ∇_ν. Then □_g^((p,q)) is a
stationary wave-type operator for g with S = 0, so S̄ = 0, and

    (□_g^((p,q)))^∧(0) − (□_ḡ^((p,q)))^∧(0) ∈ ρ⁴Diff²_b(X̄; E),                                       {#eq:ii-c-1-2}

where ^∧(0) denotes the spectral family at σ = 0. For the scalar operator,

    □_ḡ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2) + ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_(𝕊³)).                                     {#eq:ii-c-1-3}

*Proof.* [[eq:ii-c-1-3]]: □_ḡ = ∂_t² − ∂_r² − 3r⁻¹∂_r + r⁻²Δ_(𝕊³) (Δ_(𝕊³) ≥ 0). In (t_*, r), ∂_t = ∂_(t_*) and
∂_r|_t = ∂_r − ∂_(t_*), so □_ḡ = 2∂_(t_*)∂_r + 3r⁻¹∂_(t_*) − ∂_r² − 3r⁻¹∂_r + r⁻²Δ_(𝕊³); with ∂_r = −ρ(ρ∂_ρ),
2∂_(t_*)∂_r + 3ρ∂_(t_*) = −2∂_(t_*)ρ(ρ∂_ρ − 3/2), and
−∂_r² − 3r⁻¹∂_r = −r⁻²((r∂_r)² + 2r∂_r) = ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ).

In the coordinates z = (t_*, x), ḡ = −dt_*² − 2ω_i dt_* dx^i + (δ_(ij) − ω_iω_j)dx^i dx^j, ω := x/|x|, from
dt = dt_* + ω_i dx^i. Write D_j := ∂_(x^j)|_(t_*); as D_j = ω_j∂_r + r⁻¹Y_j with Y_j smooth vector fields on 𝕊³,
D_j ∈ ρ𝒱_b(X̄), and D_j maps ρ^kC^∞(X̄) into ρ^(k+1)C^∞(X̄). The metric components of ḡ are functions of ω
(homogeneous of degree 0), so the Christoffel symbols Γ̄ lie in ρC^∞(X̄), and by (K1) and [[lem:ii-b-1-1]] those of g
satisfy Γ − Γ̄ ∈ ρ³C^∞ on {ρ < ρ₁} (on the compact set {R⁻¹ ≤ ρ ≤ ρ₁}, if it is non-empty, every smooth function lies
in ρ^kC^∞ for every k, so the restriction r > R in (K1) costs nothing), and g^(μν) − ḡ^(μν) ∈ ρ²C^∞. In the frame,
∇_μ = ∂_μ + A_μ on the tensor indices, A_μ linear in Γ, and

    □_g^((p,q)) = −g^(μν)((∂_μ + A_μ)(∂_ν + A_ν) − Γ^λ_(μν)(∂_λ + A_λ)).

The terms without A form the scalar operator □_g acting componentwise.

*The model.* For ḡ, ω^μΓ̄_(κμν) = 0 for all κ, ν, where ω^μ∂_μ = ∂_r (ω⁰ := 0). In
Γ̄_(κμν) = ½(∂_μḡ_(κν) + ∂_νḡ_(κμ) − ∂_κḡ_(μν)), the first term gives ω^μ∂_μḡ_(κν) = 0, the components being
homogeneous of degree 0 in x. For the others, ω^μḡ_(κμ) = −δ_(κ0) is constant, so ω^μ∂_νḡ_(κμ) = −T_(κν) with
T_(κν) := (∂_νω^μ)ḡ_(κμ), which is r⁻¹(δ_(κν) − ω_κω_ν) for spatial κ, ν and 0 otherwise, as
∂_νω^μ = r⁻¹(δ^μ_ν − ω_νω^μ); likewise ω^μ∂_κḡ_(μν) = −T_(νκ). T is symmetric, so
ω^μΓ̄_(κμν) = ½(−T_(κν) + T_(νκ)) = 0. Hence ω^μĀ_μ = 0. The ∂_(t_*)-coefficient of −2ḡ^(μν)Ā_μ∂_ν is
−2ḡ^(μt_*)Ā_μ = 2ω^iĀ_i = 0, since ḡ⁻¹(dt_*, dt_*) = 0 and ḡ⁻¹(dt_*, dx^i) = −ω^i. The remaining terms with Ā are
−2ḡ^(μj)Ā_μD_j ∈ ρ²Diff¹_b and zeroth-order terms in ρ²C^∞. So □_ḡ^((p,q)) is [[eq:ii-c-1-3]] componentwise plus an
element of ρ²Diff¹_b, which is [[eq:ii-c-1-1]] with S = 0, Q = 0 and g₀₀ = 0.

*The difference.* □_g^((p,q)) − □_ḡ^((p,q)) is a sum of −(g^(μν) − ḡ^(μν))∂_μ∂_ν; of first-order terms B^λ∂_λ with
B^λ ∈ ρ³C^∞ (from (g − ḡ)⁻¹Γ̄, ḡ⁻¹(Γ − Γ̄), (g − ḡ)⁻¹A and ḡ⁻¹(A − Ā), where (g − ḡ)⁻¹ stands for g⁻¹ − ḡ⁻¹); and of
zeroth-order terms in ρ⁴C^∞. With ∂_μ ∈ {∂_(t_*), D_j}: the ∂_(t_*)²-term is
−(g⁻¹ − ḡ⁻¹)(dt_*, dt_*)∂_(t_*)² = −g₀₀∂_(t_*)²; the mixed terms ρ²C^∞ · ∂_(t_*)D_j lie in ρ³Diff¹_b ∂_(t_*);
B^(t_*)∂_(t_*) ∈ ρ³C^∞∂_(t_*); together they form Q∂_(t_*) with Q ∈ ρ³Diff¹_b. The spatial terms lie in
ρ²(ρ𝒱_b)² + ρ³ρ𝒱_b + ρ⁴C^∞ ⊂ ρ⁴Diff²_b, which gives [[eq:ii-c-1-2]]. Finally σ₂ = G Id holds for every connection
Laplacian. ∎

In [Hin26c, Example 5.4], S ∈ ρC^∞ and the remainder in [[eq:ii-c-1-2]] has the weight ρ³; both come from the rate r⁻¹
of Kerr, and the rate r⁻² of (K1) gives S = 0 and ρ⁴.

#### P₀ on the compactifications {#sec:ii-c-1-3}

**Lemma {#lem:ii-c-1-4}** ([Hin26c, Lemma 5.7] at n = 4.) Let P₀ be a stationary wave-type operator.
(a) P₀ ∈ ⟨x⟩⁻²Diff²_(3b)(M̃₀; E) over {r > r₀ − 2δ₀}. (b) On Ω, P₀ ∈ x_I²ρ₊²Diff²_(e3b)(M; E). (c) Near ℐ⁺ ∩ Ω, in
the coordinates ρ₊ = t_*⁻¹ ∈ (0, 1], x_I = (t_*/r)^(1/2), ω of [[sec:ii-a-1]],

    2x_I⁻²ρ₊⁻²P₀ ≡ −(x_I∂_(x_I) − 3 − 2S)(x_I∂_(x_I) − 2ρ₊∂_(ρ₊)) + 2x_I²Δ_(𝕊³)    mod x_I Diff²_(eb).  {#eq:ii-c-1-4}

The weight ρ₀² of [Hin26c, Lemma 5.7] is omitted: Ω does not meet I⁰, and ρ₀ is bounded below on it ([[sec:ii-a-1]]).

*Proof.* (a) ³ᵇTM̃₀ is spanned by ⟨x⟩∂_t, ⟨x⟩∂_(x^i) ([[def:ii-a-2-1]]). Near K⁺ away from sf, ⟨x⟩ is bounded above
and below, and P₀ is a t_*-independent differential operator with smooth coefficients in x, a combination of products
of ∂_(t_*) = ∂_t and ∂_(x^i)|_(t_*) = ∂_(x^i)|_t + ω^i∂_t. Near sf, r∂_(t_*), r∂_r = −ρ∂_ρ and ∂_ω are 3b-vector
fields, so 𝒱_b(X̄) ⊂ 𝒱_(3b) and ρ²Diff²_b(X̄) ⊂ r⁻²Diff²_(3b). In [[eq:ii-c-1-1]],
∂_(t_*)ρ(ρ∂_ρ − 3/2 − S) = r⁻²(r∂_(t_*))(−r∂_r − 3/2 − S), Q∂_(t_*) ∈ ρ³Diff¹_b · r⁻¹(r∂_(t_*)) ⊂ r⁻⁴Diff²_(3b) and
g₀₀∂_(t_*)² ∈ ρ²r⁻²(r∂_(t_*))². (b), (c) Away from ℐ⁺, (b) is (a), x_I being bounded below there and ρ₊ comparable to
⟨x⟩⁻¹ near K⁺ ∩ ι⁺. Near ℐ⁺, by [[sec:ii-a-2-3]], ∂_(t_*) = ρ₊(−ρ₊∂_(ρ₊) + ½x_I∂_(x_I)) and
∂_r = −½ρ₊x_I² · x_I∂_(x_I), and ρ = ρ₊x_I². Hence

    ρ∂_(t_*) = ½x_I²ρ₊²(x_I∂_(x_I) − 2ρ₊∂_(ρ₊)),     ρ∂_ρ = −r∂_r = ½x_I∂_(x_I),     ρ²∂_ω = x_I³ρ₊² · x_I∂_ω,

each in x_I²ρ₊²𝒱_eb or better ([Hin26c, (5.6)]). As ∂_(t_*) commutes with ρ, the first term of [[eq:ii-c-1-1]] is
−2(ρ∂_(t_*))(ρ∂_ρ − 3/2 − S) = −½x_I²ρ₊²A(x_I∂_(x_I) − 3 − 2S) with A := x_I∂_(x_I) − 2ρ₊∂_(ρ₊). Since Aρ = 2ρ − 2ρ = 0,
A commutes with S, a function of (ρ, ω), and A(x_I∂_(x_I) − 3 − 2S) = (x_I∂_(x_I) − 3 − 2S)A. Next, P̂₀(0) = ρ²P^(0)
with P^(0) ≡ (ρD_ρ)² + Δ_(𝕊³) modulo Diff¹_b + ρDiff²_b ([[lem:ii-c-1-2]]):
2x_I⁻²ρ₊⁻²ρ²Δ_(𝕊³) = 2x_I²Δ_(𝕊³), while 2x_I⁻²ρ₊⁻²ρ²(ρD_ρ)² = −½x_I²(x_I∂_(x_I))², and
2x_I⁻²ρ₊⁻²ρ²Diff¹_b = 2x_I²Diff¹_b(X̄) ⊂ x_I Diff¹_(eb) (as x_I²∂_ω = x_I · x_I∂_ω), and likewise
2x_I²ρDiff²_b(X̄) ⊂ x_I²Diff²_(eb). Finally 2x_I⁻²ρ₊⁻²Q∂_(t_*) ∈ x_I³ρ₊²Diff²_(eb) and
2x_I⁻²ρ₊⁻²g₀₀∂_(t_*)² ∈ x_I²ρ₊²Diff²_(eb). This is [[eq:ii-c-1-4]], uniformly on {ρ₊ ≤ 1}, and
x_I²Δ_(𝕊³) ∈ Diff²_(eb) gives (b) near ℐ⁺. ∎

The constant 3 in [[eq:ii-c-1-4]] is the 2 of the factor 2(1 + S) of [Hin26c, (5.7)], at n = 4.

### Admissibility of the stationary model {#sec:ii-c-2}

Admissibility collects the conditions under which the forward problem for P₀ is solved in [[ch:s09]]: a threshold at
the trapped set, tf-admissibility at the transition face, thresholds at the radial sets, and the solvability estimate
[[eq:ii-c-2-2]].

#### Trapping {#sec:ii-c-2-1}

**Definition {#def:ii-c-2-1}** (Trapping admissibility; [Hin26c, Definition 5.8] at n = 4.) P₀ is *trapping
admissible* if, for z₀ = 1 and z₀ = −1, (Γ.4) of [[sec:i-b-1-5]] holds with γ₋ < 0: there is a fibre inner product
h_Γ over Γ_(z₀) with sup_(Γ_(z₀)) λ_max(p₁^Γ) < ½ν_min. It is *strongly trapping admissible* if, for each z₀ and every
ϵ > 0, there is such an h_Γ with sup_(Γ_(z₀)) λ_max(p₁^Γ) < ϵ.

**Lemma {#lem:ii-c-2-2}** (a) Under (K2), P₀ is trapping admissible. (b) At a point −σ dt_* + ζ with σ > 0 and
(x, ζ/σ) ∈ Γ₁, and with ρ_∞ := σ⁻¹, ρ_∞σ₁(Im_h P₀)(−σ dt_* + ζ) = p₁(1)(x, ζ/σ), with p₁ as in [[lem:i-b-1-1]]. So
the case z₀ = 1 of [[def:ii-c-2-1]] is the condition [Hin26c, (5.8)] at the stationary extension of Γ₁, with Im taken
for the density |dt_* dx| and the inner product h_Γ extended to be stationary and homogeneous of degree 0.

*Proof.* (a) (H7) assumes γ₋ < 0 in (Γ.4). (b) The density |dt_* dx| is t_*-invariant, so
(T i∂_(t_*))^(*h) = i∂_(t_*)T^(*h), and i∂_(t_*) commutes with T^(*h); hence Im_h(T i∂_(t_*)) = (Im_h T) i∂_(t_*),
while g₀₀∂_(t_*)² is h-symmetric. So σ₁(Im_h P₀)(−σ dt_* + ζ) = σ₁(Im_h P̂(0))(ζ) + σ σ₀(Im_h T), homogeneous of
degree 1 in (σ, ζ); at σ = 1 it is p₁(1)(ζ) by [[lem:i-b-1-1]] (b). ∎

[Hin26c, (5.9)], a conjugation by an elliptic operator realising [Hin26c, (5.8)] for a fixed inner product
([Hin17, Proposition 3.12]), corresponds to [[lem:i-b-6-0]]: for h_Γ on phase space, [[sec:i-b-6]] conjugates by
Q = Op_h(b̃^(1/2)) near Γ and carries its estimates back. [Hin26c, (5.8)] uses the density |dg|. A change of density by
a smooth factor f changes Im P₀ by a first-order term with principal symbol ½f⁻¹H_G f, so the two conditions need not
coincide pointwise; [[def:ii-c-2-1]] is the one that the trapping estimate of [[ch:s02]] uses.

#### The transition face {#sec:ii-c-2-2}

**Definition {#def:ii-c-2-3}** (tf-admissibility; [Hin26c, Definition 5.10] at n = 4.) P₀ is *tf-admissible with
weight* β if its spectral family is tf-admissible with weight β in the sense of [[def:i-c-5-1]].

By [[cor:i-c-5-2]] (c), tf-admissibility with one weight in an indicial gap implies it for every weight in that gap.
[[sec:i-c-5-1]] relates [[def:ii-c-2-3]] to [Hin26c, Definition 5.10].

#### Orders {#sec:ii-c-2-3}

Over K⁺ the phase space is the 3b-cosphere bundle of the stationary model, ³ᵇS*M̃₀ ([[sec:ii-b-2]]), and
t_*-translations act on it. On ∂Σ^± the future field is ±𝖧, with 𝖧 the field [[eq:ii-b-1-4]]. The radial sets
∂R_(ℋ⁺) and ∂R_(∂K⁺,in/out) are those of [[def:ii-b-4-1]] and [[def:ii-b-3-1]]. For a fibre inner product h on E_X,

    ϑ_out := inf_(R^K_out) λ_min(−ρ_∞σ¹_(3b)(r² Im_h P₀)),     ϑ^(3b)_in := sup_(R^K_in) λ_max(ρ_∞σ¹_(3b)(r² Im_h P₀)),
                                                                                                        {#eq:ii-c-2-1}

with R^K_(in/out) := ∂R_(∂K⁺,in/out) ([[prop:ii-b-8-1]]) and ρ_∞ := −σ_(3b)⁻¹ ([Hin26c, (5.18)] and after). Here
r² Im_h P₀ ∈ Diff¹_(3b) near sf by [[lem:ii-c-1-4]] (a), as its principal symbol of order 2 vanishes, and its
principal symbol σ¹_(3b)(r² Im_h P₀) is an h-self-adjoint endomorphism, homogeneous of degree 1 in the fibres. The
threshold ϑ_ℋ is that of [[eq:i-a-1-5]] at the horizon: ∂R_(ℋ⁺) lies in {σ = 0}, where
σ₁(Im_h P₀) = σ₁(Im_h P̂(0)) by the identity in the proof of [[lem:ii-c-2-2]].

**Definition {#def:ii-c-2-4}** (Stationary admissible orders; [Hin26c, Definition 5.11] at n = 4.) A
t_*-translation-invariant 𝗌 ∈ C^∞(³ᵇS*M̃₀), over {r > r₀ − 2δ₀}, is *stationary-P₀-admissible with weights* α_sf,
α_K *and margin* η ≥ 0 if:

(1) (*Monotonicity.*) ±𝖧𝗌 ≤ 0 on ∂Σ^±: 𝗌 is non-increasing along the future flow.

(2) (*Evenness.*) 𝗌(−ζ) = 𝗌(ζ).

(3) (*Black hole and trapping.*) 𝗌 is constant over {r ≤ r_Γ}, for some r_Γ > r_h with Γ_(±1) ⊂ T*{r < r_Γ}.

(4) (*Horizon.*) 𝗌 is constant near ∂R_(ℋ⁺), and 𝗌 > ½ + ϑ_ℋ + η there.

(5) (*Outgoing radial set.*) 𝗌 is constant near ∂R_(∂K⁺,out), and 𝗌 + α_sf < ½(−1 + ϑ_out) + α_K − η there.

(6) (*Incoming radial set.*) 𝗌 is constant near ∂R_(∂K⁺,in), and 𝗌 + α_sf > ½(−1 + ϑ^(3b)_in) + α_K + η there.

Each threshold is computed in a fibre inner product chosen for its radial set.

**Lemma {#lem:ii-c-2-5}** (Inner products adapted to S.) Let S ∈ C^∞(X̄; End ℂ^N) and ϵ > 0. There is a fibre inner
product h on E_X with λ_min(½(S + S^(*h))) ≥ S̄ − ϵ on ∂X. For every fibre inner product,
inf_(∂X) λ_min(½(S + S^(*h))) ≤ S̄. This is [Hin23c, Proposition B.1].

*Proof.* For p ∈ ∂X write S(p) = A(D + N)A⁻¹ in Jordan form, D diagonal and N with entries 0 or 1 on the first
superdiagonal. With Λ := diag(1, δ⁻¹, …, δ^(1−N)), ΛNΛ⁻¹ = δN. Put h_p(v, w) := ⟨ΛA⁻¹v, ΛA⁻¹w⟩_(ℂ^N); for
u := ΛA⁻¹v, Re h_p(S(p)v, v) = Re⟨(D + δN)u, u⟩ ≥ (min Re spec S(p) − δ)|u|² ≥ (S̄ − δ)h_p(v, v). As
λ_min(½(S + S^(*h))) = min_(h(v,v)=1) Re h(Sv, v), the constant inner product h_p gives λ_min ≥ S̄ − 2δ on a
neighbourhood U_p of p, by continuity of (q, v) ↦ Re h_p(S(q)v, v) on {h_p(v, v) = 1}. Take a finite cover of ∂X by
such U_(p_k), a subordinate partition of unity χ_k on a neighbourhood of ∂X, and h := Σ_k χ_k h_(p_k) there, extended
to X̄ by a convex combination with a fixed inner product away from ∂X. Then
Re h(Sv, v) = Σ_k χ_k Re h_(p_k)(Sv, v) ≥ (S̄ − 2δ)h(v, v) on ∂X; take δ := ϵ/2. Conversely, the eigenvalues of S(p)
depend continuously on p, so S̄ is attained: S(p_*)v = μv with Re μ = S̄. Then Re h(S(p_*)v, v) = S̄ h(v, v) for
every h. ∎

**Lemma {#lem:ii-c-2-6}** ([Hin26c, Lemma 5.12] at n = 4.) For every fibre inner product h,
ϑ_out = 2 inf_(∂X) λ_min(½(S + S^(*h))) ≤ 2S̄, and for the h of [[lem:ii-c-2-5]], ϑ_out ≥ 2S̄ − 2ϵ. Moreover
ϑ^(3b)_in = ϑ_in, the threshold of [[eq:i-a-1-5]] at R_in.

*Proof.* Use the 3b-covectors [[eq:ii-b-3-1]], σ_(3b) dt_*/r + ξ_(3b) dr/r + η_(3b), so that σ₁(r∂_(t_*)) = iσ_(3b),
σ₁(r∂_r) = iξ_(3b), and −σ dt_* + ξ dr + η has σ_(3b) = −rσ, ξ_(3b) = rξ. We compute σ¹_(3b)(r² Im_h P₀) at sf term by
term in [[eq:ii-c-1-1]].

(i) −2∂_(t_*)ρ(ρ∂_ρ − 3/2) is symmetric for |dt_* dx| = ρ⁻⁵|dt_* dρ dω|: (ρ∂_ρ)* = −ρ∂_ρ + 4 for ρ⁻⁵dρ and
∂_(t_*)* = −∂_(t_*), so (∂_(t_*)ρ(ρ∂_ρ − c))* = −(−ρ∂_ρ + 4 − c)ρ∂_(t_*) = ∂_(t_*)ρ(ρ∂_ρ − 3 + c), which equals
∂_(t_*)ρ(ρ∂_ρ − c) exactly for c = 3/2. With h, the adjoint acquires terms H⁻¹[·, H]. As H is t_*-independent and
ρ∂_ρH ∈ ρC^∞, they lie in ρ · ρ ∂_(t_*)C^∞ ⊂ r⁻³Diff¹_(3b), which vanish at sf after the factor r².

(ii) 2∂_(t_*)ρS = 2ρS∂_(t_*) has Im_h = (1/i)ρ(S + S^(*h))∂_(t_*), as (2ρS∂_(t_*))^(*h) = −2ρS^(*h)∂_(t_*). Its symbol
at −σ dt_* + ζ is (1/i)ρ(S + S^(*h))(−iσ) = −ρσ(S + S^(*h)) = ρ²σ_(3b)(S + S^(*h)), so r² times it is
σ_(3b)(S + S^(*h)), and ∓ρ_∞ times that is ±(S + S^(*h)).

(iii) r² Im_h P̂₀(0) ∈ Diff¹_b(X̄) (the remark after (H5) in [[sec:i-a-1-3]]). Its 3b-principal symbol is that of a
spatial operator, linear in (ξ_(3b), η_(3b)). At ∂R_(∂K⁺,out), where ξ_(3b) = η_(3b) = 0, it vanishes. At
∂R_(∂K⁺,in), where ξ_(3b) = 2σ_(3b) and η_(3b) = 0, write the scattering symbol of
ρ⁻¹Im_h P̂₀(0) ∈ ρDiff¹_b = Diff¹_sc at ∂X, at ξ dr, as ξa; then σ(r² Im_h P̂₀(0))(ξ dr) = rξa = ξ_(3b)a at sf, and
ρ_∞ξ_(3b)a = −ξ̂a = −2a, which is p_in = σ(ρ⁻¹Im_h P̂(0))|_(ξ=−2, η=0) of [[eq:i-a-1-5]].

(iv) Q∂_(t_*), g₀₀∂_(t_*)² ∈ r⁻⁴Diff²_(3b) ([[lem:ii-c-1-4]]), so r² Im_h of them lies in r⁻²Diff¹_(3b) and vanishes at
sf.

Hence −ρ_∞σ¹_(3b)(r² Im_h P₀) = S + S^(*h) at ∂R_(∂K⁺,out), whose base is all of ∂K⁺ ∩ sf ≅ ∂X, and
ρ_∞σ¹_(3b)(r² Im_h P₀) = p_in − (S + S^(*h)) at ∂R_(∂K⁺,in). The first gives ϑ_out by [[lem:ii-c-2-5]], the second
ϑ^(3b)_in = sup λ_max(p_in − (S + S^(*h))) = ϑ_in. ∎

So the thresholds of [[def:ii-c-2-4]] at ∂K⁺ are those of [[eq:i-a-1-5]] and [[sec:i-b-1-4]] written in 3b-terms:
½(−1 + ϑ_out) ≈ −½ + S̄ and ½(−1 + ϑ_in).

#### The spaces and ℵ-admissibility {#sec:ii-c-2-4}

For an order 𝗌, k ∈ ℕ₀ and weights, H^((𝗌;k),(α_sf,α_K))_(3b;b)(Ω; E)^(•,−) is the space of [[sec:ii-a-7]] (the
restrictions to {r > r₀} of elements of the weighted mixed 3b-space supported in {t_* ≥ 1}), with local defining
functions ρ_sf = r⁻¹ and ρ_K = r/(t_* + r) on Ω ([Hin26c, (5.21)]). On Ω, r∂_x and t_*∂_(t_*) form a global frame of
𝒱_b ([[sec:ii-a-2-1]]), so b-regularity is tested by (t_*∂_(t_*))^j(r∂_x)^α.

**Definition {#def:ii-c-2-7}** (ℵ-admissibility; [Hin26c, Definition 5.13] at n = 4.) Let ℵ, δ ≥ 0 and α_sf ∈ ℝ. P₀
is *ℵ-admissible with sf-weight α_sf and sf-loss δ* if, for every stationary-P₀-admissible order 𝗌 with weights α_sf,
−ℵ and margin 0: (1) P₀ is trapping admissible; (2) P₀ is tf-admissible with weight α_sf + 2; (3) for every k ∈ ℕ₀
and f ∈ H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω; E)^(•,−), the forward solution of P₀u = f lies in
H^((𝗌;k),(α_sf−δ,−ℵ))_(3b;b)(Ω; E)^(•,−), with

    ‖u‖_(H^((𝗌;k),(α_sf−δ,−ℵ))_(3b;b)) ≤ C_k ‖P₀u‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)).                      {#eq:ii-c-2-2}

The relaxed version with margin d_ℵ ≥ 0 ([Hin26c, Remark 5.14]) asks (1)–(2) for orders with margin d_ℵ and (3) with
𝗌 − d_ℵ in place of 𝗌 on the left.

The weight in (2) is the weight α_sf + 3/2 of [Hin26c] at n = 4. Since |dx| = ρ⁻⁵dρ dω = ρ⁻⁴μ_b, with μ_b := ρ⁻¹dρ dω
the b-density, ρ^α L²(|dx|) = ρ^(α+2)L²(μ_b): the spatial weight α of an L²(|dx|)-based space is the b-weight α + 2 at
n = 4 (that is, α + n/2; see [[sec:i-c-1-2]]). In particular α_sf + 2 lies in an indicial gap of P̂₀(0). For the scalar
wave operator the gap is (0, 2), the indicial roots of [[eq:ii-c-1-3]] at ℓ = 0 being 0 and 2, so α_sf ∈ (−2, 0), where
[Hin26c] has (−3/2, −1/2).

### Asymptotically stationary metrics and wave-type operators {#sec:ii-c-3}

From here on the stationary metric of [[sec:ii-c-1]] is written g₀, and G₀(ζ) := g₀⁻¹(ζ, ζ) on spacetime covectors (on
spatial covectors, G₀ of [[sec:i-a-1-3]] is its restriction). On Ω we use the e3b-structure of [[sec:ii-a-2-4]], the
weight w_(α) = x_I^(2α_I)ρ₊^(α₊)ρ_K^(α_K) and the spaces C^((d₀;k),(·))_(e3b;b) of [[def:ii-a-8-1]], for sections of a
bundle in a fixed smooth frame.

**Definition {#def:ii-c-3-1}** (Asymptotically stationary metrics; [Hin26c, Definition 5.15] at n = 4.) Let
ℓ_I ∈ [0, ½], ℓ₊ ∈ [0, 1], ℓ_K ≥ 0 and d₀, k ∈ ℕ₀. Put

    𝒢̃^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b) := x_I⁻²ρ₊⁻² C^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b)(Ω; S² ᵉ³ᵇT*_Ω M),
    𝒢^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b) := g₀ + 𝒢̃^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b),

with the norm of C^((d₀;k),(2ℓ_I+2,ℓ₊+2,ℓ_K))_(e3b;b) on the first and the induced metric on the second. Subscripts are
dropped for d₀ = 0 ("e3b") or k = 0 ("b").

**Remark {#rem:s05-metric-class}** (a) g₀ − ḡ ∈ x_I⁻²ρ₊⁻² C^(∞,(2,2,0))(Ω; S² ᵉ³ᵇT*_Ω M) by [[eq:ii-b-1-2]], as ρ₀ is
bounded below on Ω, so g₀ − ḡ lies in 𝒢̃^(∞,(2ℓ_I,ℓ₊,0)) for all admissible ℓ_I, ℓ₊; for Kerr the weights are
(1, 0, 0) ([Hin26c, Remark 5.17]). (b) If h ∈ 𝒢̃^(0,(0,0,0))_(e3b) has small norm, then x_I²ρ₊²(g₀ + h) is a
non-degenerate section of S² ᵉ³ᵇT*_Ω M of Lorentzian signature, and g₀ + h is a Lorentzian metric on Ω°. Indeed
x_I²ρ₊²g₀ is non-degenerate of signature (1, 4) and continuous up to the boundary on the compact closure of Ω in
ᵉ³ᵇT*M ([[lem:ii-b-1-1]] (3)), so its inverse is bounded, and x_I²ρ₊²h is small in C⁰. g₀ + h is time-oriented by
[[lem:ii-c-3-2]], which makes dt^♭_* past timelike when h is small in 𝒢̃^(0,(2ℓ_I,0,0)), ℓ_I > 0.

**Lemma {#lem:ii-c-3-2}** (The time function; [Hin26c, Lemma 5.16] at n = 4.) Let ℓ := ℓ_I ∈ (0, ½] and
r^♮ := ½(r₀ + r₂). There are ϵ_G > 0, C′ ∈ (0, 1), r′₀ > r₂ and t^♭_* ∈ C^∞(Ω°) with

(a) t^♭_* = t_*(1 − (t_*/r)^ℓ) where t_*/r is small;

(b) C′t_* ≤ t^♭_* ≤ t_*;

(c) t^♭_* = C′t_* + C′r′₀ for r ≤ r′₀ − 1;

such that for every g = g₀ + h with ‖h‖_(𝒢̃^(0,(2ℓ,0,0))_(e3b)) < ϵ_G: (1) dr is future timelike for g on
{r₀ ≤ r ≤ r^♮}; (2) dt^♭_* is past timelike for g on Ω°.

*Proof.* *Bounds on g⁻¹.* By [[lem:ii-a-2-5]], near ℐ⁺ the covectors x_I⁻¹dt_*, x_I dr and r dω span
ρ₊⁻¹x_I⁻¹C^∞(ᵉᵇT*), so the pointwise dual vectors x_I∂_(t_*), x_I⁻¹∂_r, r⁻¹∂_ω span ρ₊x_I C^∞(ᵉᵇT), and the
symmetric products

    ρ_I∂_(t_*)²,   ∂_(t_*) ⊗_s ∂_r,   x_I∂_(t_*) ⊗_s r⁻¹∂_ω,   ρ_I⁻¹∂_r²,   x_I⁻¹∂_r ⊗_s r⁻¹∂_ω,
    r⁻¹∂_ω ⊗_s r⁻¹∂_ω,        ρ_I := x_I² = t_*/r,

span x_I²ρ₊² C^∞(S² ᵉᵇT). As x_I²ρ₊²g₀ has a bounded inverse, g⁻¹ − g₀⁻¹ (by a Neumann series) lies in
x_I²ρ₊² · x_I^(2ℓ) C⁰(S² ᵉ³ᵇT) with norm ≤ C‖h‖; and g₀⁻¹ − ḡ⁻¹ ∈ x_I⁴ρ₊⁴C^∞(S² ᵉ³ᵇT) ([[lem:ii-b-1-1]], the
inverses). Since ρ₊ ≤ 1 on Ω, the coefficients of g⁻¹ − ḡ⁻¹ in the basis above are bounded by
C₁(ϵ_G + ρ_I^(1−ℓ))ρ_I^ℓ. Away from ℐ⁺, where x_I is bounded below, the same membership gives
|(g⁻¹ − g₀⁻¹)(α, α)| ≤ Cϵ_G(|α_t| + |α_r| + r⁻¹|α_ω|)² for α = α_t dt + α_r dr + α_ω: near K⁺ ∩ ι⁺ the 3b-vectors r∂_t,
r∂_x span ³ᵇT and x_I²ρ₊² ∼ r⁻² there; near K⁺ away from sf, ∂_t, ∂_x span it and x_I, ρ₊ are bounded below; near
ι⁺ ∩ ℐ⁺ with x_I ≥ c, dt and dr evaluated on the eb-frame are O(t + r) = O(ρ₊⁻¹x_I⁻²).

*The function near ℐ⁺.* With ρ := ρ_I and F₁(ρ) := 1 − ρ^ℓ, d(t_*F₁(ρ_I)) = A dt_* + B dr with A = 1 − (1 + ℓ)ρ^ℓ and
B = ℓρ^(ℓ+1), as dρ_I = ρ_I(dt_*/t_* − dr/r). Since ḡ⁻¹(dt_*, dt_*) = 0, ḡ⁻¹(dt_*, dr) = −1 and ḡ⁻¹(dr, dr) = 1, the
covector A dt_* + B dr has ḡ⁻¹-square −2AB + B², and −2AB ≤ −2ℓρ^(ℓ+1)(1 − 2ρ^ℓ) as 1 + ℓ ≤ 2. The basis elements
evaluated on (A dt_* + B dr)^(⊗2) give ρA², O(|AB|), 0, ρ⁻¹B², 0, 0, all at most ρ in size for ρ ≤ 1. So

    g⁻¹(d(t_*F₁), d(t_*F₁)) ≤ −2ℓρ^(ℓ+1)(1 − 2ρ^ℓ) + ρ^(2ℓ+2) + C₂(ϵ_G + ρ^(1−ℓ))ρ^(ℓ+1) ≤ −ℓρ^(ℓ+1)

for ρ ≤ ρ_a and ϵ_G ≤ ϵ_a, with ρ_a, ϵ_a small depending on ℓ and C₂ (the error is of the order of the main term,
which is why ϵ_G must be small). This is timelike. It is past directed: V := t∂_t + r∂_r is future timelike for g on
{r ≥ R₂} ∩ Ω ([[sec:ii-b-7]] for g₀; for g, |h(V, V)| ≤ Cϵ_G x_I^(2ℓ) r t_* against |g₀(V, V)| ≥ ½(t_*² + 2t_*r), and
the orientation is continuous along g₀ + τh), and d(t_*F₁)(V) = At_* + Br > 0, as Vt_* = t_* and Vr = r; a timelike
covector that is positive on a future timelike vector is past timelike.

*The function away from ℐ⁺.* dt = dt_* + dr has ḡ⁻¹(dt, dt) = −1, |(g₀⁻¹ − ḡ⁻¹)(dt, dt)| ≤ Cr⁻² by (K1), and
|(g⁻¹ − g₀⁻¹)(dt, dt)| ≤ Cϵ_G where x_I ≥ c, by the bounds above. So g⁻¹(dt, dt) ≤ −½ on {r ≥ r′₀ − 1, x_I ≥ c} for r′₀
large and ϵ_G small, and dt is past timelike there (dt(V) = t > 0). On {r₀ ≤ r ≤ r′₀ + 1},
g₀⁻¹(dt_*, dt_*) = g₀₀ ≤ −c₀ < 0 by (H6) and compactness, so g⁻¹(dt_*, dt_*) ≤ −½c₀ for ϵ_G small, and dt_* is past
timelike there, for g₀ by (H6) and for g by continuity.

*Gluing.* Fix C large (below), C′ := (1 − C^(−ℓ))/(1 + C) and F₂(ρ) := C′(1 + ρ⁻¹), so that
t_*F₂(ρ_I) = C′(t_* + r) = C′t and F₁ = F₂ at ρ = 1/C. The function φ(ρ) := F₂(ρ) − F₁(ρ) satisfies φ(1/C) = 0 and
φ′(ρ) = −C′ρ⁻² + ℓρ^(ℓ−1) < 0 on (0, 2/C] for C large (as C′ ≥ (4C)⁻¹ and ℓρ^(ℓ+1) ≤ ℓ(2/C)^(ℓ+1)), and
F₁/F₂ ≥ 3/2 at ρ = 2/C. Let m_κ be smooth, even and convex, with m_κ(y) = |y| for |y| ≥ κ, and
M(a, b) := ½(a + b − m_κ(a − b)), a smooth minimum: M = min(a, b) when |a − b| ≥ κ, and ∂_aM, ∂_bM ∈ [0, 1] with
∂_aM + ∂_bM = 1. Put F := exp M(log F₁, log F₂) with κ ≤ ¼ small; then F = F₁ on (0, ρ₋] and F = F₂ on [ρ⁺, ∞) for some
ρ₋ < 1/C < ρ⁺ < 2/C, and F′/F = θF₁′/F₁ + (1 − θ)F₂′/F₂ with θ ∈ [0, 1]. Hence

    d(t_*F(ρ_I)) = F[(1 + ρF′/F)dt_* − ρ²(F′/F)dr] = F[θ d(t_*F₁)/F₁ + (1 − θ) d(t_*F₂)/F₂],

a positive combination of two past timelike covectors, hence past timelike, wherever both are. On the transition
interval [ρ₋, ρ⁺], with κ so small that ρ₋ ≥ 1/(2C), d(t_*F₁) is past timelike as ρ⁺ ≤ 2/C ≤ ρ_a, and d(t_*F₂) = C′dt
is past timelike by the previous paragraph with c := (2C)^(−1/2) (so that x_I = ρ_I^(1/2) ≥ c) and ϵ_G small depending
on C. Let R̃(r) be a smooth maximum of r and r′₀, equal to r′₀ for r ≤ r′₀ − 1 and to r for r ≥ r′₀ + 1, with
R̃′ ∈ [0, 1]. Define

    t^♭_* := C′(t_* + R̃(r)) on {r ≤ Ct_*/2},        t^♭_* := t_*F(t_*/r) on {r ≥ r′₀ + 1}.

For C > 2(r′₀ + 1) and t_* ≥ 1 the overlap {r′₀ + 1 ≤ r ≤ Ct_*/2} is where both are defined, and there both equal
C′(t_* + r), as ρ_I ≥ 2/C gives F = F₂. On {r ≤ Ct_*/2}, dt^♭_* = C′((1 − R̃′)dt_* + R̃′dt), a positive combination of
dt_* (past timelike for r ≤ r′₀ + 1) and dt (past timelike for r ≥ r′₀ − 1, x_I ≥ c, as ρ_I ≥ 2/C there). On
{r ≥ r′₀ + 1} the previous paragraph applies. This proves (2), and (a), (c) hold by construction. (b):
t_*F₁ ∈ [(1 − C^(−ℓ))t_*, t_*] for ρ ≤ 1/C, and t_*F₂ = C′t_*(1 + ρ⁻¹) ∈ [C′t_*, (1 − C^(−ℓ))t_*] for ρ ≥ 1/C. A smooth
convex even m_κ equal to |y| for |y| ≥ κ satisfies |y| ≤ m_κ ≤ κ on [−κ, κ], so
e^(−κ/2)min(F₁, F₂) ≤ F ≤ min(F₁, F₂); on the transition interval min(F₁, F₂) ≥ C′(1 + C/2) (for C large, F₁ ≥ ½
there, and C′(1 + C/2) ≤ ½ as C^ℓ ≤ 2 + C for ℓ ≤ 1), and e^(−1/8)(1 + C/2) ≥ 1, so C′ ≤ F ≤ 1. And
C′(t_* + R̃) ≤ C′(t_* + r′₀ + r) ≤ t_* where r ≤ Ct_*/2 and r′₀ ≤ C/2. (1): g₀⁻¹(dr, dr) = G₀(dr) < 0 on
{r₀ − 2δ₀ < r < r₂} by (H4), so G₀(dr) ≤ −c₁ < 0 on the compact set {r₀ ≤ r ≤ r^♮}; the perturbation is O(ϵ_G) there,
and dr is future timelike for g₀ (∇r is future timelike, [[sec:i-b-1-2]]) and for g by continuity. ∎

By (b), Ω_* := cl_M{t^♭_* ≥ 1} ⊂ Ω ([Hin26c, (6.2)]).

**Definition {#def:ii-c-3-3}** (Admissible operators; [Hin26c, Definition 5.18] at n = 4.) Let ℵ, δ ≥ 0 and
ℓ_I ∈ (0, ½], ℓ₊ > δ, ℓ_K > ℵ ([Hin26c, (5.23)]). Let P₀ be ℵ-admissible with sf-weight α_sf and sf-loss δ. An
operator P ∈ Diff²(Ω°; E) is *admissible* (relative to P₀) *of class* ((d₀;k), (2ℓ_I, ℓ₊, ℓ_K)) if:

(1) σ₂(P) = G Id, G(ζ) = g⁻¹(ζ, ζ), for some g ∈ 𝒢^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b);

(2) with a cut-off χ_I = χ_I(x_I), equal to 1 near 0 and supported in {x_I < 1}, there are

    p₀, p̃₁ ∈ ρ₊^(ℓ₊)C^(k+d₀)_b(ℐ⁺ ∩ Ω; End ℂ^N)                                                       {#eq:ii-c-3-1}

(extended to supp χ_I independently of x_I) with

    P̃ := P − [P₀ + χ_I ½x_I²ρ₊²(2p̃₁(x_I∂_(x_I) − 2ρ₊∂_(ρ₊)) + p₀)]
         ∈ x_I²ρ₊² C^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b) Diff²_(e3b)(Ω; E);                                  {#eq:ii-c-3-2}

(3) there is a splitting ℂ^N = ⊕_(j=1)^J E_j, over ∂X, in which p₁ := S|_(∂X) + p̃₁ is lower triangular with diagonal
blocks of real spectrum, and p₀ is strictly lower triangular.

P is *weakly admissible* if only ℓ_I ∈ (0, ½], ℓ₊ > 0 and ℓ_K > 0 are assumed ([Hin26c, (5.26)]).

Here S|_(∂X) is pulled back to ℐ⁺ along its fibration over ∂X ≅ Y⁺ ([[sec:ii-a-1]]), and the operators in
[[eq:ii-c-3-2]] are those of [[sec:ii-a-8-2]] with coefficients in the stated space.

**Lemma {#lem:ii-c-3-4}** ([Hin26c, (5.27)] at n = 4.) For P as in [[def:ii-c-3-3]], near ℐ⁺ ∩ {ρ₊ ≤ 1},

    2x_I⁻²ρ₊⁻²P − [−(x_I∂_(x_I) − 3 − 2p₁)(x_I∂_(x_I) − 2ρ₊∂_(ρ₊)) + 2x_I²Δ_(𝕊³) + p₀]
        ∈ C^((d₀;k),(2ℓ_I,0))_(eb;b) Diff²_(eb).                                                         {#eq:ii-c-3-3}

The characteristic exponents of x_I∂_(x_I) − 3 − 2p₁ are 3 + 2μ, μ ∈ spec p₁ (2(1 + μ) in [Hin26c]).

*Proof.* Where χ_I = 1,
2x_I⁻²ρ₊⁻²P = 2x_I⁻²ρ₊⁻²P₀ + 2p̃₁(x_I∂_(x_I) − 2ρ₊∂_(ρ₊)) + p₀ + 2x_I⁻²ρ₊⁻²P̃. Insert [[eq:ii-c-1-4]];
S − S|_(∂X) ∈ ρC^∞ = x_I²ρ₊C^∞, so replacing S by S|_(∂X) costs x_I Diff¹_(eb), and
−(x_I∂_(x_I) − 3 − 2S|_(∂X))A + 2p̃₁A = −(x_I∂_(x_I) − 3 − 2p₁)A with A = x_I∂_(x_I) − 2ρ₊∂_(ρ₊). The remainders are
x_I Diff²_(eb) ⊂ C^(∞,(2ℓ_I,0))Diff²_(eb) (as 2ℓ_I ≤ 1) and
2x_I⁻²ρ₊⁻²P̃ ∈ x_I^(2ℓ_I)ρ₊^(ℓ₊)C^((d₀;k))_(e3b;b) Diff²_(eb) (near ℐ⁺ the e3b- and eb-structures agree). ∎

**Definition {#def:ii-c-3-5}** ([Hin26c, Definition 5.20].) p̄₁ := inf_(p∈ℐ⁺) min Re spec p₁(p).

The lower bounds on ℓ₊ and ℓ_K in [Hin26c, (5.23)] matter only when estimates for P are closed with the mapping
properties of P₀ ([Hin26c, Remark 5.21]); the regularity of p₀, p̃₁ in [[eq:ii-c-3-1]] follows [Hin26c, Remark 5.22].

**Definition {#def:ii-c-3-6}** ([Hin26c, Definition 5.23].) ‖P − P₀‖_((d₀;k),(2ℓ_I,ℓ₊,ℓ_K)) is the sum of the norms of
p₀, p̃₁ in [[eq:ii-c-3-1]] and of a representation of P̃ in [[eq:ii-c-3-2]] ([[sec:ii-a-8-2]]); on Ω′ ⊂ Ω the suprema
are taken over Ω′.

**Lemma {#lem:ii-c-3-7}** ‖g − g₀‖_(𝒢̃^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b)) ≤ C‖P − P₀‖_((d₀;k),(2ℓ_I,ℓ₊,ℓ_K)) when the
right side is small, and likewise on subsets.

*Proof.* The bracket in [[eq:ii-c-3-2]] has the principal symbol of P₀, the χ_I-terms being of first order. So
G − G₀ = σ₂(P̃), and g⁻¹ − g₀⁻¹ ∈ x_I²ρ₊²C^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b)(S² ᵉ³ᵇT) with norm ≤ C‖P̃‖. Then
g − g₀ = −g₀(g⁻¹ − g₀⁻¹)g₀ + …, a convergent Neumann series in x_I⁻²ρ₊⁻²C^((d₀;k),(2ℓ_I,ℓ₊,ℓ_K))_(e3b;b), by
[[lem:ii-a-8-2]] (c)–(d). ∎

### The global dynamics of perturbed metrics {#sec:ii-c-4}

Fix ℓ_I ∈ (0, ½], ℓ₊ ∈ (0, 1], ℓ_K > 0 ([Hin26c, (6.1)]) and d₀ ≥ 2, and consider

    g = g₀ + h,      h ∈ 𝒢̃^(d₀,(2ℓ_I,ℓ₊,ℓ_K))_(e3b)(Ω_*),      ‖h‖ < ϵ_G ≤ 1,                        {#eq:ii-c-4-1}

with ϵ_G at most that of [[lem:ii-c-3-2]]. Write w := x_I^(2ℓ_I)ρ₊^(ℓ₊)ρ_K^(ℓ_K), G(ζ) := g⁻¹(ζ, ζ),
G_(e3b) := x_I⁻²ρ₊⁻²G and, with ρ_∞ a defining function of fibre infinity,

    𝖧_G := ρ_∞H_(G_(e3b)),                                                                              {#eq:ii-c-4-2}

which on the characteristic set equals ρ_∞x_I⁻²ρ₊⁻²H_G, the field [[eq:ii-b-1-4]] ([Hin26c, (6.4b)]). Put
Σ := {G_(e3b) = 0} ⊂ ᵉ³ᵇT*_(Ω_*)M ∖ o; Σ⁺ is the closure of the set of null covectors ν over Ω_*° with
g⁻¹(ν, dt^♭_*) > 0, that is, with ν^♯ future directed, as dt^♭_* is past timelike ([[lem:ii-c-3-2]]); and Σ⁻ := −Σ⁺.

**Lemma {#lem:ii-c-4-1}** (a) G_(e3b) − G_(0,e3b) ∈ ϵ_G w C^(d₀) P^[2](ᵉ³ᵇT*_(Ω_*)M), and 𝖧_G − 𝖧_(G₀) is a
C^(d₀−1) b-vector field on ᵉ³ᵇT̄*_(Ω_*)M in ϵ_G w C^(d₀−1)𝒱_b, tangent to fibre infinity. In particular Σ and 𝖧_G agree
with those of g₀ over Ω_* ∩ ∂M, and 𝖧_G is C¹, so its integral curves are unique. (b) Σ⁺ ∩ Σ⁻ = ∅, and Σ^± agree with
those of g₀ over ∂M.

*Proof.* (a) g⁻¹ − g₀⁻¹ ∈ x_I²ρ₊²ϵ_G w C^(d₀)(S² ᵉ³ᵇT) (Neumann series, as in the proof of [[lem:ii-c-3-7]]), which is
the first statement. For p ∈ wC^(d₀)P^[2], H_p is a first-order e3b-differential operator applied to p
([[sec:ii-a-2-5]]); b-vector fields preserve wC⁰, so H_p ∈ wC^(d₀−1)𝒱_b(ᵉ³ᵇT*M), and ρ_∞H_p is tangent to fibre
infinity by homogeneity. w vanishes on ℐ⁺, ι⁺ and K⁺ as ℓ_I, ℓ₊, ℓ_K > 0. (b) Over Ω_*° a nonzero null covector is not
orthogonal to the timelike dt^♭_*. Over ∂M, use (a) and [[sec:ii-b-1-3]]. ∎

**Proposition {#prop:ii-c-4-2}** (Global dynamics of perturbed metrics; [Hin26c, Proposition 6.1] at n = 4.) Let
γ : I → ∂Σ⁺ be a maximal integral curve of 𝖧_G over Ω_* ∩ {r ≥ r₀}. Then either γ lies over
(Ω_* ∩ ℐ⁺) ∪ ι⁺ ∪ K⁺, where it is an integral curve of 𝖧_(G₀) and is described by [[prop:ii-b-8-1]]; or γ reaches
{t^♭_* = 1} backward at a finite parameter, and forward either reaches {r = r₀} at a finite parameter, where
𝖧_G r < 0, or tends to ᵉ³ᵇS*M over (Ω_* ∩ ℐ⁺) ∪ ι⁺ ∪ K⁺.

*Proof.* The boundary faces are invariant, as 𝖧_G is a b-vector field; over them 𝖧_G = 𝖧_(G₀) ([[lem:ii-c-4-1]]). Let
γ lie over M°. At ν ∈ Σ⁺ over M°, H_G t^♭_* = 2g⁻¹(ν, dt^♭_*) > 0, and 𝖧_G t^♭_* is bounded below by a positive
constant on each compact subset of ∂Σ⁺ over Ω_* ∩ M°, by continuity.

*Forward.* If t^♭_* ∘ γ is unbounded, its limit points lie over {t^♭_* = ∞} ∩ Ω_* = ι⁺ ∪ K⁺. Otherwise, either γ reaches
{r = r₀}, or sup I = ∞ and a limit point over M° would be visited infinitely often, each visit to a fixed small
neighbourhood lasting a parameter time bounded below and raising t^♭_* by a fixed amount, so t^♭_* → ∞; hence the limit
points lie over ∂M at bounded t_*, which in Ω_* is ℐ⁺. At {r = r₀}, H_G r = 2g⁻¹(ν, dr) < 0 for future null ν, as dr
is future timelike there ([[lem:ii-c-3-2]] (1)), so γ leaves {r ≥ r₀} there.

*Backward.* Suppose that γ does not reach {t^♭_* = 1}. As 𝖧_G r < 0 at {r = r₀}, r increases backward there, so γ
does not leave through {r = r₀} backward. Then inf I = −∞ and t^♭_* ∘ γ ↓ L ≥ 1, and as before the α-limit set 𝒜 lies
over ℐ⁺ ∩ {t^♭_* = L}. Over ℐ⁺, t^♭_* = t_* by [[lem:ii-c-3-2]] (a), so ρ₊ = L⁻¹ on 𝒜. 𝒜 is non-empty, compact and
invariant under 𝖧_(G₀), and every curve in it has ρ₊ constant, so by [[eq:ii-b-7-5]] ξ̂ = 0 and then η̂ = 0:
𝒜 ⊂ ∂R_(ℐ⁺,out). Near ∂R_(ℐ⁺,out), by [[eq:ii-b-7-4]] and [[lem:ii-c-4-1]] (a),
σ_(eb)⁻¹H_(G_(eb))x_I = (ξ̂ − 1)x_I + O(x_I^(1+2ℓ_I)) ≤ −½x_I for x_I small (with σ_(eb) > 0 on Σ⁺ there,
[[lem:ii-c-5-3]] below, for ϵ_G small). So on a tail (−∞, s₁], x_I ∘ γ > 0 increases as s decreases and cannot tend
to 0, a contradiction. ∎

The backward statement for g₀ is [[prop:ii-b-8-2]], and the argument carries over by [[lem:ii-c-4-1]].

### Order functions {#sec:ii-c-5}

**Proposition {#prop:ii-c-5-1}** (Order functions; [Hin26c, Proposition 6.4] at n = 4.) Let P₀ be a stationary
wave-type operator for g₀, η ≥ 0 and α₊, α_K ∈ ℝ, and let ℓ_I, ℓ₊, ℓ_K be as in [[sec:ii-c-4]]. There are
𝗌 ∈ C^∞(ᵉ³ᵇS*_Ω M) and ϵ_G > 0 such that:

(1) 𝗌 over K⁺, identified with a t_*-translation-invariant function on ³ᵇS*M̃₀ (over K⁺ the e3b- and 3b-cosphere
bundles agree), is stationary-P₀-admissible with margin η and α_sf = α₊;

(2) for every g = g₀ + h with ‖h‖_(𝒢̃^(1,(2ℓ_I,ℓ₊,ℓ_K))_(e3b)(Ω)) < ϵ_G, ±𝖧_G𝗌 ≤ 0 on ∂Σ^± over Ω_*;

(3) 𝗌 is invariant under the dilations (t_*, r, ω) ↦ (at_*, ar, ω), a > 0, in a neighbourhood of
ι⁺ ∩ {r/t_* ∈ [1, 10]};

(4) (1) holds also for every stationary wave-type operator P₁ near P₀ (coefficients close in C¹), and (1)–(2) hold for
the stationary models of nearby parameters b ((K4));

(5) 𝗌 is constant near ∂R_(ℐ⁺,out) and near ∂R_(ℐ⁺,in,+) ([[def:ii-b-7-1]]).

**Definition {#def:ii-c-5-2}** ([Hin26c, Definition 6.5].) Order functions with (1)–(5) of [[prop:ii-c-5-1]] are
*admissible* for P₀ with weights α₊, α_K and margin η.

Item (5) is part of [Hin23c, Lemma 5.8 (3)]; it is included because the radial estimates at ℐ⁺ in [[ch:s06]] use it.
The proof of [[prop:ii-c-5-1]] occupies [[sec:ii-c-5-1]] (the characteristic set near ℐ⁺ and ι⁺, for every g as in (2))
and [[sec:ii-c-5-2]] (the construction).

#### The characteristic set near ℐ⁺ and near ι⁺ {#sec:ii-c-5-1}

*Near ℐ⁺.* Let Ω_I := Ω ∩ {x_I ≤ ϵ_I}, with the eb-coordinates of [[sec:ii-b-7]]: ρ₊ = t_*⁻¹ ∈ (0, 1],
x_I = (t_*/r)^(1/2), covectors ν = σ_(eb) dρ₊/ρ₊ + ξ_(eb) dx_I/x_I + η_(eb) dω/x_I,
|ν|_(eb)² := σ_(eb)² + ξ_(eb)² + |η_(eb)|² and G_(eb) := x_I⁻²ρ₊⁻²G. Let Ḡ_(eb) be [[eq:ii-b-7-1]] and
G⁰_(eb) := ½ξ_(eb)(ξ_(eb) − 2σ_(eb)) + |η_(eb)|². For g as in [[prop:ii-c-5-1]] (2), with ϵ_G ≤ 1, [[sec:ii-b-7]] and
[[lem:ii-c-4-1]] (a) at d₀ = 1 (its first assertion holds verbatim at d₀ = 1 and over Ω, its proof being the Neumann
series) give

    G_(eb) − G⁰_(eb) = ¼x_I²ξ_(eb)² + (G_(eb) − Ḡ_(eb)) ∈ x_I^(2ℓ_I) C¹ P^[2],                            {#eq:ii-c-5-1}

with norm bounded independently of g, as x_I² ≤ x_I^(2ℓ_I) and ρ₊ ≤ 1.

*Near ι⁺.* Let Ω_ι := Ω ∩ {ρ_K ≤ C_ι, ϱ ≤ ϵ_ι}, with the 3b-coordinates of [[sec:ii-b-3]]: ρ_K := r/t_*, ϱ := r⁻¹,
ν = σ_(3b) dt_*/r + ξ_(3b) dr/r + η_(3b), |ν|_(3b)² := σ_(3b)² + ξ_(3b)² + |η_(3b)|², G_(3b) := r²G, and Ḡ_(3b) of
[[eq:ii-b-3-2]]. (In [[sec:ii-b-3]], ρ₊ stands for ϱ.) On Ω_ι, x_I² = ρ_K⁻¹ ≥ C_ι⁻¹, so the e3b-defining function of ι⁺
is comparable to ϱ, and [[sec:ii-b-3]] and [[lem:ii-c-4-1]] (a) give

    G_(3b) − Ḡ_(3b) ∈ w_ι C¹ P^[2],        w_ι := ϱ^(ℓ₊),                                                {#eq:ii-c-5-2}

with norm bounded in terms of C_ι, as ϱ² ≤ ϱ^(ℓ₊) and ρ_K^(ℓ_K)x_I^(2ℓ_I) is bounded on Ω.

**Lemma {#lem:ii-c-5-3}** For ϵ_I small, ϵ_ι small (depending on C_ι), and every g as in [[prop:ii-c-5-1]] (2) with
ϵ_G ≤ ϵ₁ small: on Σ over Ω_I, |σ_(eb)| ≥ 0.3|ν|_(eb), and σ_(eb) > 0 on Σ⁺; on Σ over Ω_ι,
|σ_(3b)| ≥ 0.3|ν|_(3b), and σ_(3b) < 0 on Σ⁺.

*Proof.* 2Ḡ_(eb) = (ξ_(eb) − σ_(eb))² − σ_(eb)² + 2|η_(eb)|² + ½x_I²ξ_(eb)². If |σ_(eb)| < 0.3|ν|_(eb), then
(ξ − σ)² ≥ ½ξ² − σ² (omitting the subscripts) gives
2Ḡ_(eb) ≥ ½(|ν|² − σ²) − 2σ² ≥ (½ − 2.5 · 0.09)|ν|² > ¼|ν|², while |2G_(eb) − 2Ḡ_(eb)| ≤ Cϵ_I^(2ℓ_I)|ν|² < ¼|ν|² by
[[eq:ii-c-5-1]] for ϵ_I small: so G_(eb) ≠ 0. The 3b case is the same, with
Ḡ_(3b) = (ξ_(3b) − σ_(3b))² + |η_(3b)|² − σ_(3b)² and [[eq:ii-c-5-2]].

*Signs.* σ_(eb) = ν(ρ₊∂_(ρ₊)) = −ν(V) with V := t∂_t + r∂_r ([[sec:ii-b-7]]). On Ω_I, r = t_*x_I⁻² ≥ ϵ_I⁻² ≥ R₂, so V
is future timelike for g₀, and also for g: V = −ρ₊∂_(ρ₊) ∈ 𝒱_eb and h ∈ x_I⁻²ρ₊⁻²ϵ_G x_I^(2ℓ_I)C⁰(S² ᵉᵇT*) give
|h(V, V)| ≤ Cϵ_G x_I^(2ℓ_I)x_I⁻²ρ₊⁻² = Cϵ_G x_I^(2ℓ_I) r t_*, small against |g₀(V, V)| ≥ ½(t_*² + 2t_*r), and the
orientation is continuous along g₀ + τh. For ν ∈ Σ⁺ over M°, ν(V) = g(ν^♯, V) < 0, so σ_(eb) > 0, and by the first part
and continuity also over ∂M. Likewise σ_(3b) = rν(∂_(t_*)), and ∂_(t_*) is future timelike for g₀ on {r ≥ R₁}
([[lem:ii-b-1-2]] (b)) and for g, as |h(∂_(t_*), ∂_(t_*))| ≤ Cϵ_G on Ω_ι (r∂_(t_*) is a 3b-vector field and
x_I⁻²ρ₊⁻² ∼ r² there). ∎

On Σ⁺ over Ω_I put ξ̂ := ξ_(eb)/σ_(eb), η̂ := η_(eb)/σ_(eb) and 𝖧^(eb) := σ_(eb)⁻¹H_(G_(eb)); over Ω_ι put
ξ̂_(3b) := ξ_(3b)/σ_(3b), η̂_(3b) := η_(3b)/σ_(3b) and 𝖧^(3b) := −σ_(3b)⁻¹H_(G_(3b)). On Σ⁺ each is a positive
multiple of 𝖧_G, as G_(eb) and G_(3b) are positive multiples of G_(e3b) there (x_I being bounded below on Ω_ι); signs of
derivatives along them agree with those along 𝖧_G. By [[lem:ii-c-5-3]], |ξ̂| + |η̂| ≤ 7 on Σ over Ω_I, and likewise in
the 3b-coordinates over Ω_ι.

**Lemma {#lem:ii-c-5-4}** (Near ℐ⁺.) For ϵ_I small, on Σ⁺ over Ω_I ∩ {|ξ̂| ≤ ½}: (a) ξ̂ ≥ −1/8 and |η̂|² ≤ 3/2; (b)
𝖧^(eb)ξ̂ ≤ −¼ where ξ̂ ∈ [¼, ½]; (c) 𝖧^(eb)x_I ≤ −¼x_I.

*Proof.* By [[eq:ii-c-5-1]], 𝖧^(eb) = 𝖧⁰ + 𝖧^e with 𝖧⁰ := σ_(eb)⁻¹H_(G⁰_(eb)), given exactly by [[eq:ii-b-7-4]], and
𝖧^e := σ_(eb)⁻¹H_(G_(eb) − G⁰_(eb)). By [[eq:ii-a-2-2]], 𝖧^e applied to ξ̂ is O(x_I^(2ℓ_I)) and applied to x_I is
(∂_(ξ_(eb))(G_(eb) − G⁰_(eb)))σ_(eb)⁻¹x_I = O(x_I^(1+2ℓ_I)), uniformly where |ξ̂| + |η̂| ≤ 7. On Σ,
σ_(eb)⁻²G_(eb) = 0 gives |η̂|² = ½ξ̂(2 − ξ̂) + E with |E| ≤ C₃ϵ_I^(2ℓ_I). (a) For ξ̂ ∈ [−½, −1/8),
½ξ̂(2 − ξ̂) ≤ −1/8, so |η̂|² < 0 once C₃ϵ_I^(2ℓ_I) < 1/8, which is impossible; and for |ξ̂| ≤ ½,
|η̂|² ≤ 3/8 + C₃ϵ_I^(2ℓ_I) ≤ 3/2. (b) For ξ̂ ∈ [¼, ½], |η̂|² ≥ 7/32 − C₃ϵ_I^(2ℓ_I) ≥ 3/16, and
𝖧⁰ξ̂ = −2|η̂|² ≤ −3/8. (c) 𝖧⁰x_I = (ξ̂ − 1)x_I ≤ −½x_I. The errors are absorbed for ϵ_I small. ∎

**Lemma {#lem:ii-c-5-5}** (Near ι⁺; [Hin23c, (C.8)–(C.9)].) Put f_T := ϱ⁻¹(1 − ξ̂_(3b)) and f_W := −ξ̂_(3b). Let
δ ∈ (0, 1]. For ϵ_ι small depending on δ and C_ι, on Σ⁺ over Ω_ι ∩ {|ξ̂_(3b)| ≤ δ/2}: (a) 𝖧^(3b)f_T ≥ ϱ⁻¹;
(b) ξ̂_(3b) ≥ −δ/8, |η̂_(3b)|² ≥ |ξ̂_(3b)| − δ/8 and |η̂_(3b)|² ≤ 3δ; (c) 𝖧^(3b)f_W ≥ δ/8 where
ξ̂_(3b) ∈ [δ/4, δ/2].

*Proof.* Write 𝖧^(3b) = 𝖧̄ + 𝖧^e, with 𝖧̄ := −σ_(3b)⁻¹H_(Ḡ_(3b)) given exactly by [[eq:ii-b-3-4]] (with ρ₊ = ϱ) and
𝖧^e := −σ_(3b)⁻¹H_(G_(3b) − Ḡ_(3b)), which by [[eq:ii-c-5-2]] is a b-vector field with coefficients O(w_ι); it maps ϱ
into ϱO(w_ι) and ξ̂_(3b) into O(w_ι). We write ξ̂ for ξ̂_(3b) and η̂ for η̂_(3b). (a) By [[eq:ii-b-3-4]],
𝖧̄ϱ⁻¹ = 2(1 − ξ̂)ϱ⁻¹ and 𝖧̄ξ̂ = −2(2 − ξ̂)ξ̂, so

    𝖧̄f_T = 2ϱ⁻¹((1 − ξ̂)² + (2 − ξ̂)ξ̂) = 2ϱ⁻¹

exactly; and |𝖧^e f_T| ≤ Cϱ⁻¹w_ι, so 𝖧^(3b)f_T ≥ (2 − Cϵ_ι^(ℓ₊))ϱ⁻¹ ≥ ϱ⁻¹. (b) On Σ,
σ_(3b)⁻²G_(3b) = ξ̂² − 2ξ̂ + |η̂|² + O(w_ι) = 0, so |η̂|² = ξ̂(2 − ξ̂) + E with |E| ≤ Cϵ_ι^(ℓ₊) ≤ δ/16. For
ξ̂ ∈ [−δ/2, −δ/8), ξ̂(2 − ξ̂) ≤ 2ξ̂ < −δ/4, which is impossible. For ξ̂ ∈ [0, δ/2], ξ̂(2 − ξ̂) ≥ ξ̂; for ξ̂ ∈ [−δ/8, 0),
|η̂|² ≥ 0 ≥ |ξ̂| − δ/8. And ξ̂(2 − ξ̂) ≤ 3|ξ̂| for |ξ̂| ≤ ½, so |η̂|² ≤ 3|ξ̂| + δ/16 ≤ 3δ. (c) For ξ̂ ∈ [δ/4, δ/2],
𝖧̄f_W = 2(2 − ξ̂)ξ̂ ≥ 2ξ̂ ≥ δ/2, so 𝖧^(3b)f_W ≥ δ/2 − Cϵ_ι^(ℓ₊) ≥ δ/8. ∎

#### The construction {#sec:ii-c-5-2}

*Proof of [[prop:ii-c-5-1]].* Fix the following functions, all with values in [0, 1]: φ ∈ C^∞_c((−½, ½)) even, with
φ = 1 on [−¼, ¼] and φ′ ≤ 0 on [0, ∞); ψ ∈ C^∞_c((−3, 3)) with ψ = 1 on [−2, 2]; ψ̃ ∈ C^∞(ℝ) with ψ̃ = 0 on (−∞, 4],
ψ̃ = 1 on [5, ∞) and ψ̃′ ≥ 0; ψ₀ ∈ C^∞([0, ∞)) with ψ₀ = 1 on [0, ½ϵ_I], ψ₀ = 0 on [ϵ_I, ∞) and ψ₀′ ≤ 0; and
Ψ ∈ C^∞(ℝ) with Ψ = 0 on (−∞, 0.04] and Ψ = 1 on [0.09, ∞). Choose, in this order: ϵ_I ([[lem:ii-c-5-3]] and
[[lem:ii-c-5-4]], and ϵ_I² < 1/10, used in (3)); C_ι := 8ϵ_I⁻²; δ := ϵ_I²/32; and ϵ_ι ([[lem:ii-c-5-3]] and
[[lem:ii-c-5-5]]) so small that also 1/(ϵ_ιδ) > r_Γ for some r_Γ as in [[def:ii-c-2-4]] (3), and 1/(ϵ_ιδ) > r_h + 1.
Define

    χ_I := φ(ξ̂) ψ(|η̂|²) Ψ(σ_(eb)²/|ν|_(eb)²),
    χ_ι := φ(f_W/δ) ψ̃(ϵ_ιδ f_T) ψ(|η̂_(3b)|²/(2δ)) Ψ(σ_(3b)²/|ν|_(3b)²),
    χ := ψ₀(x_I)χ_I + (1 − ψ₀(x_I))χ_ι,        𝗌 := s_in − (s_in − s_out)χ,                               {#eq:ii-c-5-3}

with constants s_out ≤ s_in chosen below.

*Smoothness.* χ_I is smooth on ᵉᵇS* over {x_I < ϵ_I} ⊃ supp ψ₀(x_I), the ratios being smooth where Ψ ≠ 0, that is,
where |σ_(eb)| ≥ 0.2|ν|_(eb). χ_ι is a function of t_*, r and the 3b-fibre coordinates, which are smooth on ³ᵇS* away
from ℐ⁺; on supp(1 − ψ₀(x_I)), x_I ≥ ½ϵ_I, so ρ_K = x_I⁻² ≤ 4ϵ_I⁻² < C_ι. Where φ(f_W/δ) ≠ 0, |ξ̂_(3b)| < δ/2 ≤ ½, so
ϵ_ιδf_T ≥ ½ϵ_ιδϱ⁻¹ → ∞ as ϱ → 0, and ψ̃(ϵ_ιδf_T) = 1 near ϱ = 0. Where ψ̃(ϵ_ιδf_T) ≠ 0 as well, f_T > 4/(ϵ_ιδ) and
ϱ = (1 − ξ̂_(3b))/f_T < (5/16)ϵ_ιδ, inside Ω_ι. Near a point with ϱ = 0 and |ξ̂_(3b)| ≥ δ/2, φ(f_W/δ) vanishes on a
neighbourhood, supp φ being a compact subset of (−½, ½). So (1 − ψ₀)χ_ι is smooth and supported in
Ω_ι ∩ {ϱ < ϵ_ιδ}, and χ ∈ C^∞(ᵉ³ᵇS*_Ω M), 0 ≤ χ ≤ 1. Every factor is even under ν ↦ −ν.

*Monotonicity.* Let g be as in (2) with ϵ_G ≤ ϵ₁, and work on ∂Σ⁺. On Σ over Ω_I ∩ supp φ(ξ̂), |η̂|² ≤ 3/2 and
|σ_(eb)| ≥ 0.3|ν|_(eb) ([[lem:ii-c-5-3]] and [[lem:ii-c-5-4]]), so ψ(|η̂|²) = 1 and Ψ = 1 on a neighbourhood of these
points in ∂Σ⁺, and 𝖧χ_I = φ′(ξ̂)𝖧ξ̂ there. Where φ′(ξ̂) ≠ 0, |ξ̂| ∈ [¼, ½], so ξ̂ ∈ [¼, ½] by [[lem:ii-c-5-4]] (a),
φ′ ≤ 0 and 𝖧^(eb)ξ̂ < 0 ([[lem:ii-c-5-4]] (b)): 𝖧χ_I ≥ 0. Likewise on Σ over Ω_ι the factors ψ and Ψ of χ_ι equal 1
near supp φ(f_W/δ) ([[lem:ii-c-5-5]] (b): |η̂_(3b)|²/(2δ) ≤ 3/2), and

    𝖧^(3b)χ_ι = δ⁻¹φ′(f_W/δ)ψ̃ 𝖧^(3b)f_W + ϵ_ιδ φ ψ̃′ 𝖧^(3b)f_T.

Where φ′(f_W/δ) ≠ 0, |ξ̂_(3b)| ∈ [δ/4, δ/2], hence ξ̂_(3b) ∈ [δ/4, δ/2] ([[lem:ii-c-5-5]] (b)), so
f_W/δ ∈ [−½, −¼], where φ′ ≥ 0, and 𝖧^(3b)f_W > 0 ([[lem:ii-c-5-5]] (c)). The second term is ≥ 0 by
[[lem:ii-c-5-5]] (a). So 𝖧χ_ι ≥ 0 on ∂Σ⁺ over supp(1 − ψ₀).

*Gluing.* 𝖧χ = ψ₀𝖧χ_I + (1 − ψ₀)𝖧χ_ι + ψ₀′(x_I)(𝖧x_I)(χ_I − χ_ι), and the last term lives on
U := {½ϵ_I ≤ x_I ≤ ϵ_I}. Two facts hold on ∂Σ⁺ over U.

(U1) Where χ_ι ≠ 0, χ_I = 1. Indeed there |ξ̂_(3b)| < δ/2 = ϵ_I²/64 and u := x_I² = t_*/r ∈ [¼ϵ_I², ϵ_I²]. The two
systems of fibre coordinates are related by σ_(eb) = −σ_(3b)(u + ξ̂_(3b)), ξ_(eb) = −2ξ_(3b) and η_(eb) = x_Iη_(3b),
an identity of coordinates proved in [[lem:ii-b-7-3]] that holds wherever both are defined. So
ξ̂ = 2ξ̂_(3b)/(u + ξ̂_(3b)), and u + ξ̂_(3b) ≥ ϵ_I²/8 gives |ξ̂| ≤ ¼: φ(ξ̂) = 1, and ψ = Ψ = 1 as before.

(U2) Where χ_I ≠ 0, 𝖧x_I < 0: there |ξ̂| < ½, and [[lem:ii-c-5-4]] (c) applies.

Where χ_I = 0, (U1) gives χ_ι = 0 and the last term vanishes. Where χ_I > 0, ψ₀′𝖧x_I ≥ 0 by (U2), and χ_I − χ_ι ≥ 0,
since either χ_ι = 0 or χ_I = 1 ≥ χ_ι. Hence 𝖧χ ≥ 0 on ∂Σ⁺, and 𝖧𝗌 = −(s_in − s_out)𝖧χ ≤ 0. On ∂Σ⁻: the antipodal map
A : ν ↦ −ν maps Σ⁺ onto Σ⁻, G is even, so H_G and 𝖧_G are odd (A_*𝖧_G = −𝖧_G), and 𝗌 ∘ A = 𝗌; hence
𝖧_G𝗌(Aν) = −𝖧_G𝗌(ν) ≥ 0, which is −𝖧_G𝗌 ≤ 0 on ∂Σ⁻. This proves (2), with ϵ_G := ϵ₁; the case h = 0 restricted to K⁺
is [[def:ii-c-2-4]] (1).

*Values.* Over K⁺, x_I = (t_*/r)^(1/2) = ∞, so ψ₀(x_I) = 0 and χ = χ_ι, a function of ϱ and the 3b-fibre coordinates,
hence t_*-translation-invariant there; it vanishes over {ϱ ≥ ϵ_ιδ}, a set containing {r ≤ r_Γ} and a neighbourhood of
the horizon: 𝗌 = s_in there. Near ∂R_(∂K⁺,in) (ξ̂_(3b) = 2), φ(f_W/δ) = 0, so 𝗌 = s_in. Near
∂R_(∂K⁺,out) = {ρ_K = ϱ = 0, ξ̂_(3b) = 0, η̂_(3b) = 0}: φ(f_W/δ) = 1 for |ξ̂_(3b)| ≤ δ/4, ψ̃ = 1 for ϱ small, ψ = 1 for
η̂_(3b) small, and Ψ = 1 as |σ_(3b)| = |ν|_(3b) at the set: 𝗌 = s_out on a neighbourhood. Near ∂R_(ℐ⁺,out) (x_I = 0,
ξ̂ = 0, η̂ = 0), ψ₀ = 1 and χ_I = 1: 𝗌 = s_out. Near ∂R_(ℐ⁺,in,+) (ξ̂ = 2), ψ₀ = 1 and χ_I = 0: 𝗌 = s_in. Choose

    s_in > max(½ + ϑ_ℋ + η, ½(−1 + ϑ^(3b)_in) + α_K + η − α₊) + 1,
    s_out < min(s_in, ½(−1 + ϑ_out) + α_K − η − α₊) − 1,

each threshold in a fibre inner product chosen for its radial set (for ϑ_out, that of [[lem:ii-c-2-5]]). Then, with
𝗌 := s_in over {r₀ − 2δ₀ < r < r₀} (where nothing else is defined), (1)–(6) of [[def:ii-c-2-4]] hold, which is (1),
and (5) holds.

*(3).* In a neighbourhood of ι⁺ ∩ {ρ_K ∈ [1, 10]}, x_I² = ρ_K⁻¹ ≥ 1/10 > ϵ_I², so ψ₀(x_I) = 0, and ϱ is small, so
ψ̃(ϵ_ιδf_T) = 1 on supp φ(f_W/δ): χ = φ(−ξ̂_(3b)/δ)ψ(|η̂_(3b)|²/(2δ))Ψ(σ_(3b)²/|ν|_(3b)²) there. The 3b-covectors
dt_*/r, dr/r and dω are invariant under the dilations, and so are the ratios of their coefficients and |ν|_(3b)² (with
the round metric on 𝕊³).

*(4).* The thresholds ϑ_ℋ, ϑ^(3b)_in and ϑ_out are extreme eigenvalues of endomorphisms depending continuously on the
coefficients, over compact sets, so they move by less than 1 for P₁ near P₀ (with fixed inner products), and the
margins of 1 above keep (4)–(6) of [[def:ii-c-2-4]]. Conditions (1)–(3) of that definition do not depend on the
operator beyond its metric. For nearby parameters b, the stationary metrics satisfy (K1) with uniform constants (K4),
so [[eq:ii-c-5-1]], [[eq:ii-c-5-2]] and [[lem:ii-c-5-3]]–[[lem:ii-c-5-5]] hold uniformly; the horizon radius and Γ
vary continuously ([[rem:ii-b-8-3]]), so {ϱ ≥ ϵ_ιδ} still contains them after shrinking ϵ_ι. ∎

**Remark {#rem:s05-construction}** [Hin23c, Appendix C] also multiplies χ_I by a localisation χ_t in a time function,
with a further small parameter ρ_(+,lo), because its error term in 𝖧x_I is Cρ₊^(ℓ₊)x_I. Here the error carries
x_I^(2ℓ_I) by [[eq:ii-c-5-1]] (the rate x_I² of the stationary part, [[sec:ii-b-7]], and the weight x_I^(2ℓ_I) of the
perturbation), so [[lem:ii-c-5-4]] (c) holds at all ρ₊ ≤ 1 and χ_t is not needed. [Hin26c, p. 114] refers to that
construction and adds that only the dynamics over ι⁺ matter; the construction above confirms this, the trapped set and
the horizon lying where 𝗌 is constant.

### The persistence theorem {#sec:ii-c1-1}

For a metric that decays in time to the stationary model, the null-bicharacteristic flow is tangent to hypersurfaces
that are close to the stable and unstable manifolds of the stationary trapped set and converge to them
([[prop:ii-c1-3-4]]; [Hin26c, Proposition 6.3] in dimension 4 + 1). This section states the theorem on decaying
perturbations of a flow with normally hyperbolic trapping from which this follows. It is proved quantitatively, from
the defining functions of (Γ.1)–(Γ.3) with their exact equations (Γ.2) and the tangential growth bound of (K3).

**Theorem {#thm:ii-c1-1-1}** (Persistence of the stable and unstable hypersurfaces.) Let Y be a smooth manifold with a
Riemannian metric, V₀ a smooth vector field on Y, Γ ⊂ Y a compact smooth submanifold, O ⊂ Y an open neighbourhood of Γ
with compact closure, and φ_u, φ_s, ν_u, ν_s ∈ C^∞(Ō) real, such that:

(i) Γ = {φ_u = φ_s = 0} ∩ O, and dφ_u, dφ_s are linearly independent at every point of Γ;

(ii) V₀φ_u = −ν_uφ_u and V₀φ_s = ν_sφ_s on O, with ν_u, ν_s ≥ ν > 0 on O;

(iii) Γ is invariant under the flow of V₀, and for every ε > 0 there is C_ε with |De^(sV₀)v| ≤ C_ε e^(ε|s|)|v| for
v ∈ TΓ, s ∈ ℝ.

Let k ≥ 2, ℓ > 0, T₀ ≥ 1 and ρ(t) := t^(−ℓ). Then there are a neighbourhood O′ ⊂ O of Γ, ϵ₀ > 0 and C such that the
following holds for every vector field Ṽ on [T₀, ∞) × O, tangent to the slices {t} × O, of class C^k in (t, y) jointly,
with

    ‖Ṽ‖ := sup_(t≥T₀) ρ(t)⁻¹ ‖Ṽ‖_(C^k([t,t+1]×O)) ≤ ϵ ≤ ϵ₀.                                               {#eq:ii-c1-1-1}

The vector field V := ∂_t + V₀ + Ṽ is tangent to the hypersurfaces

    W^u := {φ_u + ψ_u = 0},        W^s := {φ_s + ψ_s = 0}        of [T₀, ∞) × O′,                         {#eq:ii-c1-1-2}

where ψ_u ∈ C^k, ψ_s ∈ C^(k−1), |∂^αψ_u(t, y)| ≤ Cϵρ(t) for |α| ≤ k and |∂^αψ_s(t, y)| ≤ Cϵρ(t) for |α| ≤ k − 1,
derivatives in (t, y) in fixed charts. W^u meets {t = T₀} in {φ_u = 0}. The constants O′, ϵ₀ and C depend only on k,
ℓ, ν, C_ε for ε := ν/(2k), the C^(k+1)-norms of V₀, φ_u, φ_s, ν_u, ν_s on O in a fixed finite atlas, and the choices
of [[sec:ii-c1-2-1]]; they depend neither on T₀ nor on Ṽ.

C^k-norms on [t, t + 1] × O are taken in the charts of a fixed finite atlas of a neighbourhood of Ō, in which the
metric is uniformly comparable to the Euclidean one.

**Remark {#rem:s05-persistence}** (a) (iii) is the tangential half of r-normal hyperbolicity for every r
([HPS77, Definition 4]); the normal half is (ii), in which the normal dynamics is linear in φ_u, φ_s. No invariant
splitting of T_ΓY is used. (b) W^s is the analogue of the stable manifold and is determined by V; W^u, the analogue of
the unstable manifold, depends on its initial slice, here {φ_u = 0} at t = T₀ ([Hin21, footnote 1]). In the
application, with time running forward, W^u is the backward-trapped hypersurface and W^s the forward-trapped one.

### Proof of the persistence theorem {#sec:ii-c1-2}

*Proof of [[thm:ii-c1-1-1]].* The proof is a graph transform. The hypersurfaces have codimension one and (ii) gives the
normal dynamics in closed form, so each step of the transform solves one scalar equation by monotonicity; the
tangential dynamics enters only through the norm of a time-T map, which is made small against the normal rates by
taking T large. The proof occupies [[sec:ii-c1-2-1]]–[[sec:ii-c1-2-6]].

#### Coordinates {#sec:ii-c1-2-1}

Let π : O₁ → Γ be a smooth retraction of a neighbourhood O₁ ⊂ O of Γ (π|_Γ = id; for instance the projection of a
tubular neighbourhood), and Ψ₀ := (π, φ_u, φ_s) : O₁ → Γ × ℝ².

*Ψ₀ is a local diffeomorphism near Γ.* At p ∈ Γ, ker dφ_u ∩ ker dφ_s has codimension 2 by (i) and contains T_pΓ (as
φ_(u/s) = 0 on Γ), which has codimension 2; so they are equal. If dΨ₀(v) = 0, then v ∈ T_pΓ and dπ(v) = v = 0.
*It is injective near Γ.* Otherwise there are p_n ≠ q_n with Ψ₀(p_n) = Ψ₀(q_n) and dist(p_n, Γ), dist(q_n, Γ) → 0;
for a subsequence p_n → p and q_n → q in Γ, and Ψ₀(p) = Ψ₀(q) gives p = q (Ψ₀(p) = (p, 0, 0) on Γ), contradicting
injectivity near p (inverse function theorem). So Ψ₀ is a diffeomorphism from a neighbourhood of Γ onto an open set
containing Γ × {0}, hence, Γ being compact, containing Γ × [−δ₁, δ₁]² for some δ₁ > 0. Put
O₂ := Ψ₀⁻¹(Γ × (−δ₁, δ₁)²).

In the coordinates (y, a, b) := Ψ₀ on O₂, by (ii),

    V₀ = Y₀(y, a, b) − ν_u(y, a, b) a ∂_a + ν_s(y, a, b) b ∂_b,                                          {#eq:ii-c1-2-1}

with Y₀ tangent to Γ (the y-component) and Y₀(·, 0, 0) = V₀|_Γ, and Ṽ = (Ỹ, Ã, B̃) with C^k-norms bounded by Cϵρ(t).
Fix a finite atlas of Γ, charts κ_i : U_i → ℝ^m, compact sets 𝒦_i ⊂ U_i covering Γ and a Lebesgue number d_L > 0
(every ball of radius d_L lies in some U_i), and let C_at ≥ 1 bound the factor by which the norm of a linear map
between tangent spaces of Γ × ℝ² can change when its domain and its codomain are read in two of the charts. For
functions on Γ × I, I an interval, ‖D^j f‖_∞ is the supremum over i and over 𝒦_i × I of the j-th derivatives in the
chart κ_i × id.

#### Time-T maps {#sec:ii-c1-2-2}

Let Φ⁰_τ be the time-τ map of V₀ and, for t ≥ T₀, let Φ_(t,τ) be the spatial part of the time-τ map of V from the
slice {t} (τ of either sign). By [[eq:ii-c1-2-1]], along an integral curve of V₀ in O₂,
a(τ) = a(0)exp(−∫₀^τ ν_u) and b(τ) = b(0)exp(∫₀^τ ν_s); so for τ ≥ 0

    Φ⁰_τ(y, a, b) = (f_τ(y, a, b), a m^u_τ(y, a, b), b m^s_τ(y, a, b)),     m^u_τ ≤ e^(−ντ),     m^s_τ ≥ e^(ντ),
                                                                                                        {#eq:ii-c1-2-2}

with m^(u/s)_τ ∈ [e^(−C_ντ), e^(C_ντ)], C_ν := sup_O(ν_u + ν_s), as long as the curve stays in O₂; and similarly for
τ ≤ 0 with the roles of a and b exchanged.

Fix T ≥ 1, to be chosen below, and then δ ∈ (0, ¼δ₁] with e^(2C_νT)δ ≤ ¼δ₁, and put B := Γ × [−δ, δ]². For ϵ₀ small
(depending on T and δ), Φ_(t,τ) is defined on B for |τ| ≤ 2T with t + τ ≥ T₀, with values in
Γ × (−½δ₁, ½δ₁)², and:

(T1) {|a| ≤ δ} is forward invariant and {|b| ≤ δ} backward invariant for V within O₂: (d/dτ)|a| ≤ −ν|a| + |Ã| < 0 at
|a| = δ when Cϵ₀ < νδ, and likewise for b backward.

(T2) ‖Φ_(t,τ) − Φ⁰_τ‖_(C^k) ≤ C_Tϵρ(t) on B, derivatives in (t, τ, y, a, b) (for ∂_τ:
∂_τ(Φ_(t,τ) − Φ⁰_τ) = V₀(Φ_(t,τ)) − V₀(Φ⁰_τ) + Ṽ, which is O(ϵρ)), and ‖Φ_(t,τ)‖_(C^k) ≤ C_T. This is Grönwall's
inequality for the equation and its variational equations up to order k, whose inhomogeneous terms are Ṽ and its
derivatives at the times between t and t + τ. By [[eq:ii-c1-1-1]] these are at most ϵρ(s) on each window [s, s + 1]
with s ≥ min(t, t + τ) ≥ T₀ ≥ 1, and ρ(s) ≤ ρ(min(t, t + τ)) ≤ (1 + 2T)^ℓρ(t), because t/(t + τ) ≤ 1 + 2T when τ < 0
and t + τ ≥ 1; the factor (1 + 2T)^ℓ and the number 4T + 1 of windows go into C_T.

(T3) (*The tangential rate.*) With ε := ν/(2k), |Df_τ(y, 0, 0)|_(T_yΓ)| ≤ C_ε e^(ε|τ|) by (iii), as f_τ(·, 0, 0) is the
flow of V₀|_Γ.

(T4) (*The cross terms.*) |∂_a f_τ(y, 0, 0)| ≤ C_*C_ε e^(ετ) for τ ≥ 0, and |∂_b f_τ(y, 0, 0)| ≤ C_*C_ε e^(ε|τ|) for
τ ≤ 0, with C_* := ν⁻¹ sup|∂_(a,b)Y₀|. Indeed, linearising [[eq:ii-c1-2-1]] at (y, 0, 0) in the direction ∂_a gives
δb ≡ 0, δa(σ) = m^u_σ(y, 0, 0) ≤ e^(−νσ) and δy′ = D_yY₀ δy + ∂_aY₀ δa, so
δy(τ) = ∫₀^τ J(τ, σ)∂_aY₀ δa(σ) dσ with J(τ, σ) = De^((τ−σ)V₀)|_(TΓ) at f_σ(y, 0, 0), bounded by C_ε e^(ε(τ−σ)); hence
|δy(τ)| ≤ C_ε sup|∂_aY₀| ∫₀^τ e^(ε(τ−σ)−νσ) dσ ≤ C_*C_ε e^(ετ). Backward, b contracts and the same estimate applies.

(T5) On B, every first derivative of Φ⁰_τ differs from its value at (y, 0, 0) by at most C_Tδ; and ∂_y(am^u_τ),
∂_b(am^u_τ), ∂_y(bm^s_τ) and ∂_a(bm^s_τ) are O(C_Tδ) on B, carrying the factor a or b.

Let Λ_τ := C_at(C_* + 2)C_ε e^(ε|τ|). By (T3)–(T5) and (T2), for 0 ≤ τ ≤ 2T the block D_((y,a))(Φ_y, Φ_a) of DΦ_(t,τ)
has norm at most Λ_τ + C_T(δ + ϵ₀) in the chart norms (|(v, s)| := |v| + |s|), and for −2T ≤ τ ≤ 0 the block
D_((y,b))(Φ_y, Φ_b) likewise. We use C_T for constants depending on T and the data, and fix T so large that

    e^(−νT)(2Λ_T)^k(1 + 2T)^ℓ ≤ ¼,                                                                       {#eq:ii-c1-2-3}

which is possible as kε = ν/2 < ν; then δ as above, small also against C_T where stated; and finally ϵ₀ small
against δ and C_T.

#### One step of the graph transform {#sec:ii-c1-2-3}

For t ≥ T₀ and τ ∈ [0, 2T] let Φ := Φ_(t,τ), and 𝒦_a := Γ × [−δ, δ]_a. For β : 𝒦_a → ℝ with |β| ≤ ¼δ and
Lip β ≤ θ₀ := δ (in the chart norms) define 𝒮_Φβ : 𝒦_a → ℝ by

    Φ_b(y, a, 𝒮_Φβ(y, a)) = β(Φ_y(y, a, 𝒮_Φβ(y, a)), Φ_a(y, a, 𝒮_Φβ(y, a))):                              {#eq:ii-c1-2-4}

graph(𝒮_Φβ) is the set of points of B that Φ maps into graph(β).

**Lemma {#lem:ii-c1-2-1}** (One step.) For (y, a) ∈ 𝒦_a, [[eq:ii-c1-2-4]] has exactly one solution b ∈ [−δ, δ], and:

(G1) |𝒮_Φβ| ≤ e^(−ντ)(|β|_∞ + C_Tϵρ(t));

(G2) |𝒮_Φβ − 𝒮_Φβ̃|_∞ ≤ e^(−ντ)(1 − 3C_Tδ)⁻¹|β − β̃|_∞ for two such β, β̃;

(G3) if β ∈ C^k and ‖D^jβ‖_∞ ≤ M_jϵρ(t) for 0 ≤ j ≤ k (the case j = 0 included), then 𝒮_Φβ ∈ C^k and, for
1 ≤ i ≤ k,

    ‖D^i𝒮_Φβ‖_∞ ≤ e^(−ντ)(1 − 3C_Tδ)⁻¹(2Λ_τ)^i‖D^iβ‖_∞ + C(T, M₀, …, M_(i−1)) ϵρ(t).                     {#eq:ii-c1-2-5}

*Proof.* Fix (y, a) and put h(b) := Φ_b(y, a, b) − β(Φ_y, Φ_a)(y, a, b). By (T1) the point (Φ_y, Φ_a) lies in 𝒦_a, so
h is defined on [−δ, δ]. By [[eq:ii-c1-2-2]], (T2) and (T5),
∂_bΦ_b = m^s_τ + b ∂_bm^s_τ + O(C_Tϵρ) ≥ e^(ντ)(1 − C_Tδ) − C_Tϵ₀, and |∂_b(Φ_y, Φ_a)| ≤ C_T with
Lip β ≤ θ₀ = δ, so h′(b) ≥ e^(ντ)(1 − C_Tδ) − C_Tϵ₀ − C_Tδ ≥ e^(ντ)(1 − 3C_Tδ) > 0, as e^(ντ) ≥ 1 and ϵ₀ ≤ δ. At
b = ±δ, ±Φ_b ≥ δm^s_τ(1 − C_Tδ) − C_Tϵρ ≥ ¾δ > |β|, so h changes sign: it has a unique zero. (G1): at the zero,
b m^s_τ(y, a, b) = β(⋯) − (Φ_b − Φ⁰_(τ,b)), and m^s_τ ≥ e^(ντ). (G2): with b and b̃ the two zeros,
h(b̃) = h(b̃) − h̃(b̃) = −(β − β̃)(⋯), so |b − b̃| ≤ |β − β̃|_∞/inf h′. (G3): 𝒮_Φβ ∈ C^k by the implicit function
theorem, H(w, b) := Φ_b(w, b) − β((Φ_y, Φ_a)(w, b)), w = (y, a), being C^k with ∂_bH ≥ e^(ντ)(1 − 3C_Tδ). Fix
p ∈ 𝒦_i × [−δ, δ]; as (Φ_y, Φ_a) has Lipschitz constant at most 2Λ_τ, it maps the ball of radius d_L/(2Λ_(2T)) about p
into a ball of radius d_L, which lies in some chart U_l; differentiate H(w, 𝒮_Φβ(w)) = 0 i times at p in the charts i
and l. For i = 1 the result is ∂_bH · D𝒮_Φβ = Dβ · D_w(Φ_y, Φ_a) − D_wΦ_b, and for i ≥ 2 it is

    ∂_bH · D^i𝒮_Φβ = D^iβ[(D_w(Φ_y, Φ_a) + ∂_b(Φ_y, Φ_a)D𝒮_Φβ)^(⊗i)] + R_i,

the term Dβ · ∂_b(Φ_y, Φ_a)D^i𝒮_Φβ being part of ∂_bH · D^i𝒮_Φβ. Here R_i (and −D_wΦ_b at i = 1) is a sum of products
of derivatives of order ≤ i of β and of order ≤ i − 1 of 𝒮_Φβ, and of derivatives of order ≤ i of Φ (bounded by
C_T). Every product in R_i contains a factor O(ϵρ(t)): either D^jβ with j ≥ 1; or D^j𝒮_Φβ with 1 ≤ j ≤ i − 1, bounded
inductively; or a pure w-derivative of Φ_b, which is b D^j_w m^s_τ + D^j_w(Φ_b − Φ⁰_(τ,b)) at b = 𝒮_Φβ = O(ϵρ) by
(G1) and (T2). In the leading term, |D_w(Φ_y, Φ_a)| ≤ Λ_τ + C_T(δ + ϵ₀) and
|∂_b(Φ_y, Φ_a)D𝒮_Φβ| ≤ C_T · Cϵ₀, together at most 2Λ_τ. Dividing by ∂_bH gives [[eq:ii-c1-2-5]]. ∎

*The backward step.* For τ ∈ [0, 2T] and t ≥ T₀ + τ let Φ⁻ := Φ_(t,−τ), the map back to the slice t − τ, and
𝒦_b := Γ × [−δ, δ]_b. For α : 𝒦_b → ℝ with |α| ≤ ¼δ and Lip α ≤ θ₀, define 𝒰_(Φ⁻)α by
Φ⁻_a(y, 𝒰α(y, b), b) = α(Φ⁻_y, Φ⁻_b)(y, 𝒰α(y, b), b): graph(𝒰α) is the set of points of B that the backward map sends
into graph(α), which is the image of graph(α) under the forward map, within B. [[lem:ii-c1-2-1]] holds verbatim for
𝒰, with (a, b) exchanged, Φ replaced by Φ⁻, and with ρ(t) as it stands in (G1) and [[eq:ii-c1-2-5]], the factor
(1 + 2T)^ℓ for the backward window being part of C_T in (T2): backward, a is multiplied by (m^u)⁻¹ ≥ e^(ντ), {|b| ≤ δ}
is invariant by (T1), and the block D_((y,b))(Φ⁻_y, Φ⁻_b) is bounded by Λ_τ + C_T(δ + ϵ₀) by (T3)–(T5).

#### The stable hypersurface {#sec:ii-c1-2-4}

Let t_j := T₀ + jT, j ≥ 0, and 𝒮_j := 𝒮_(Φ_(t_j,T)). Choose M₀ := 2C_T and then, inductively,
M_i ≥ 2C(T, M₀, …, M_(i−1)), 1 ≤ i ≤ k, and let ϵ₀ be so small that M₀ϵ₀ ≤ ¼δ and M₁ϵ₀ ≤ θ₀. Let 𝔅 be the set of
sequences β = (β_j)_(j≥0) of C^k functions on 𝒦_a with ‖D^iβ_j‖_∞ ≤ M_iϵρ(t_j) for 0 ≤ i ≤ k, and put
(ℱβ)_j := 𝒮_jβ_(j+1).

*ℱ maps 𝔅 into itself.* As ρ(t_(j+1)) ≤ ρ(t_j), (G1) gives
|𝒮_jβ_(j+1)| ≤ e^(−νT)(M₀ + C_T)ϵρ(t_j) ≤ M₀ϵρ(t_j), and [[eq:ii-c1-2-5]] with [[eq:ii-c1-2-3]] gives
‖D^i𝒮_jβ_(j+1)‖_∞ ≤ ½M_iϵρ(t_j) + C(T, M₀, …, M_(i−1))ϵρ(t_j) ≤ M_iϵρ(t_j).

*ℱ is a contraction* for d(β, β̃) := sup_j ρ(t_j)⁻¹|β_j − β̃_j|_∞, by (G2) and ρ(t_j)⁻¹ ≤ ρ(t_(j+1))⁻¹, with factor
e^(−νT)(1 − 3C_Tδ)⁻¹ ≤ ½.

So β^(n) := ℱ^n(0) ∈ 𝔅 is Cauchy for d, and β^(n)_j → β_j uniformly. Bounded in C^k on the compact set 𝒦_a, the
D^(k−1)β^(n)_j are equicontinuous, so (Arzelà–Ascoli) every subsequence has a further subsequence converging in C^(k−1),
necessarily to β_j: β^(n)_j → β_j in C^(k−1), ‖D^iβ_j‖_∞ ≤ M_iϵρ(t_j) for i ≤ k − 1, and D^(k−1)β_j is Lipschitz with
constant ≤ CM_kϵρ(t_j). By (G2), ℱ is continuous for d on sequences with |β_j| ≤ ¼δ and Lip β_j ≤ θ₀, so ℱβ = β:
β_j = 𝒮_jβ_(j+1) for all j.

*All times.* For t ∈ [t_j, t_(j+1)] put β(t, ·) := 𝒮_(Φ_(t,t_(j+1)−t))β_(j+1); at t = t_(j+1) (Φ = id) this is
β_(j+1), and at t = t_j it is 𝒮_jβ_(j+1) = β_j. For t ∈ [t_(j−1), t_j], by the cocycle property
Φ_(t,t_(j+1)−t) = Φ_(t_j,T) ∘ Φ_(t,t_j−t) and uniqueness in [[lem:ii-c1-2-1]] (applied with τ = t_(j+1) − t ≤ 2T, and
with (T1)), 𝒮_(Φ_(t,t_j−t))β_j = 𝒮_(Φ_(t,t_(j+1)−t))β_(j+1): a point is mapped into graph(β_j) at time t_j if and only if
it is mapped into graph(β_(j+1)) at time t_(j+1). So on [t_(j−1), t_(j+1)], β(t, ·) is given by the single equation

    H(t, w, b) := Φ_(t,t_(j+1)−t,b)(w, b) − β_(j+1)(Φ_(t,t_(j+1)−t,ya)(w, b)) = 0,

with H ∈ C^(k−1) in (t, w, b) (the flow map from time t to t_(j+1) is C^k in (t, w, b), and β_(j+1) ∈ C^(k−1)) and
∂_bH ≥ ½. By the implicit function theorem, β ∈ C^(k−1)([t_(j−1), t_(j+1)] × 𝒦_a), and differentiating the equation as
in (G3) bounds its derivatives of order ≤ k − 1 by Cϵρ(t_(j−1)) ≤ C(1 + 2T)^ℓϵρ(t). Hence
β ∈ C^(k−1)([T₀, ∞) × 𝒦_a) with |∂^αβ| ≤ Cϵρ(t) for |α| ≤ k − 1.

*Tangency.* Let W^s := {(t, y, a, b) : b = β(t, y, a)} ⊂ [T₀, ∞) × B, a C^(k−1) hypersurface. If (t, x) ∈ W^s with
t ∈ [t_(j−1), t_(j+1)), then for small σ > 0, Φ_(t+σ,t_(j+1)−t−σ)(Φ_(t,σ)(x)) = Φ_(t,t_(j+1)−t)(x) ∈ graph(β_(j+1)),
and Φ_(t,σ)(x) ∈ B by (T1) and |b| ≤ Cϵ₀ < δ along W^s; so Φ_(t,σ)(x) ∈ W^s(t + σ), and the integral curve of V through
(t, x) stays in W^s for small forward times. Hence V is tangent to W^s.

#### The unstable hypersurface {#sec:ii-c1-2-5}

Put α₀ := 0 on 𝒦_b and α_(j+1) := 𝒰_(Φ_(t_(j+1),−T))α_j: graph(α_(j+1)) is the image of graph(α_j) under Φ_(t_j,T),
within B. With M′₀ := 2C_T(1 + 2T)^ℓ and M′_i ≥ 2C(T, M′₀, …, M′_(i−1))(1 + 2T)^ℓ, and ϵ₀ so small that also
M′₀ϵ₀ ≤ ¼δ and M′₁ϵ₀ ≤ θ₀, so that [[lem:ii-c1-2-1]] applies to each α_j, induction on j gives
‖D^iα_j‖_∞ ≤ M′_iϵρ(t_j) for i ≤ k: by the backward form of (G1) and [[eq:ii-c1-2-5]], with
ρ(t_j) ≤ (1 + T)^ℓρ(t_(j+1)) and [[eq:ii-c1-2-3]],

    ‖D^iα_(j+1)‖_∞ ≤ e^(−νT)(2Λ_T)^i(1 − 3C_Tδ)⁻¹M′_iϵρ(t_j) + Cϵρ(t_j) ≤ ½M′_iϵρ(t_(j+1)) + ½M′_iϵρ(t_(j+1)).

No limit is taken, and α_j ∈ C^k. For t ∈ [t_j, t_(j+1)] put α(t, ·) := 𝒰_(Φ_(t,−(t−t_j)))α_j, whose graph is the
image of graph(α_j) under Φ_(t_j,t−t_j); on [t_j, t_(j+2)] the same formula with α_j holds by the cocycle property, so
α ∈ C^k([T₀, ∞) × 𝒦_b) by the implicit function theorem (now with C^k data), with |∂^αα| ≤ Cϵρ(t) for |α| ≤ k. The
set W^u := {a = α(t, y, b)} is a union of forward orbit segments of V starting on {t = T₀, a = 0}, within B; so V is
tangent to it, as in [[sec:ii-c1-2-4]].

#### The defining functions {#sec:ii-c1-2-6}

Let O′ := Ψ₀⁻¹(Γ × (−δ, δ)²) and, for (t, x) ∈ [T₀, ∞) × O′,

    ψ_s(t, x) := −β(t, π(x), φ_u(x)),        ψ_u(t, x) := −α(t, π(x), φ_s(x)).

Then {φ_s + ψ_s = 0} = W^s and {φ_u + ψ_u = 0} = W^u in [T₀, ∞) × O′, and the bounds follow by the chain rule, π and
φ_(u/s) being smooth. W^u ∩ {t = T₀} = {φ_u = 0} as α(T₀, ·) = α₀ = 0. The constants depend only on the quantities
listed in [[thm:ii-c1-1-1]]. ∎

### The stable and unstable hypersurfaces of perturbed metrics {#sec:ii-c1-3}

This section applies [[thm:ii-c1-1-1]] to the null-bicharacteristic flow of a metric g = g₀ + h that decays in time to
the stationary model g₀ of [[sec:ii-c-3]]: the perturbed characteristic set near the trapped set is written as a graph
over the stationary one, the flow is pulled back to it, and the theorem gives the hypersurfaces.

#### The stationary data {#sec:ii-c1-3-1}

Let Γ := Γ₁ ⊂ Σ^♭₁ ⊂ T*X̃° be the trapped set of (H7) at z₀ = 1, with O, φ_u, φ_s, ν_u, ν_s as there, let
q₁ = 2g₀⁻¹(−dt_* + ζ, dt_*) ([[lem:i-b-1-1]] and (K3)), and let 𝖵 := q₁⁻¹H_(G₁) on Σ^♭₁ near Γ, where
G₁(x, ζ) := G₀(−dt_* + ζ) and G₀(ν) = g₀⁻¹(ν, ν). By (Γ.3), dG₁ ≠ 0 near Γ, so Y := Σ^♭₁ ∩ O₀, for a small
neighbourhood O₀ of Γ, is a smooth hypersurface of T*X̃°; q₁ ≥ 2β₀ > 0 on Γ by (Γ.4), hence q₁ ≥ β₀ on O₀. Wherever
injectivity on (−c, c) × Y is used below, Y is replaced by a relatively compact open neighbourhood of Γ in it.

**Lemma {#lem:ii-c1-3-1}** Y, V₀ := 𝖵, Γ and the restrictions to Y of φ_u, φ_s and of ν_u/q₁, ν_s/q₁ satisfy
(i)–(iii) of [[thm:ii-c1-1-1]], after shrinking O₀, with ν := ν_min/(4 sup_(O₀) q₁); and the constants are uniform in
the parameter b of (H5) and (K4).

*Proof.* (ii): (Γ.2) gives H_(G₁)φ_u = −ν_uφ_u and H_(G₁)φ_s = ν_sφ_s on Σ^♭₁ ∩ O, so 𝖵φ_u = −(ν_u/q₁)φ_u and
𝖵φ_s = (ν_s/q₁)φ_s; and ν_(u/s) ≥ ½ν_min near Γ by continuity. (i): Γ = Γ_u ∩ Γ_s within O by (Γ.1). Suppose that at
p ∈ Γ, a dφ_u + b dφ_s vanishes on T_pY for some (a, b) ≠ 0; as T_pY = ker dG₁, a dφ_u + b dφ_s = c dG₁ at p. The
Poisson bracket with φ_s gives a{φ_u, φ_s} = c{G₁, φ_s} = c H_(G₁)φ_s = c ν_sφ_s = 0 at p, so a = 0 by (Γ.3); with φ_u,
likewise b = 0. (iii): Γ is invariant, 𝖵 being tangent to Γ_u and Γ_s (Γ.1); the bound is the tangential part of (K3)
for 𝖵. Uniformity: (H5), extended to (H6)–(H8) in [[sec:i-b-1-5]], and (K4) give continuity in b of Γ, φ_(u/s),
ν_(u/s) and q₁ into C^∞, and uniform ν_min, β₀ and C_ε; the choices of [[sec:ii-c1-2-1]] can then be made uniformly for
b near any b₀, and ℬ is compact. ∎

#### The slice and the projected flow {#sec:ii-c1-3-2}

Let T_♭ := 2/C′, with C′ of [[lem:ii-c-3-2]], and let [r_(Γ,−), r_(Γ,+)] ⊂ (r₂, ρ₁⁻¹) contain the projection of Γ. By
[[lem:ii-c-3-2]] (b), Ω_* ⊃ {t_* ≥ 1/C′}, a neighbourhood of {t_* ≥ T_♭} on which g is defined with its d₀
derivatives, so what is stated below for t_* > T_♭ holds on the closed set where t_* ≥ T_♭, as [[thm:ii-c1-1-1]]
requires. Over D := {t_* > T_♭, r_(Γ,−) < r < r_(Γ,+)}, near (K⁺)°, the e3b-structure is spanned by ∂_(t_*), ∂_x
([[sec:ii-a-2-2]] and [[sec:ii-b-2-1]]), and ᵉ³ᵇT*_D M = T*D with covectors −σ dt_* + ζ. On {σ > 0} use the slice
coordinates (t_*, x, z), z := ζ/σ, which identify {σ > 0} ∩ ᵉ³ᵇS*_D M with (T_♭, ∞) × T*{r_(Γ,−) < r < r_(Γ,+)}; at
ρ_K = t_*⁻¹ = 0 this is the map Φ₁ of [[def:ii-b-2-2]]. Let g = g₀ + h with h ∈ 𝒢̃^(d₀,(0,0,ℓ_K))_(e3b), d₀ ≥ 3,
ℓ_K > 0 and ‖h‖ ≤ ϵ. Over D, x_I and ρ₊ are bounded above and below and ρ_K ∼ t_*⁻¹, so the components of
g⁻¹ − g₀⁻¹ in the frame ∂_(t_*), ∂_x have derivatives of order ≤ d₀ along ∂_(t_*), ∂_x bounded by Cϵt_*^(−ℓ_K)
(Neumann series, [[lem:ii-a-8-2]]). Put

    p₁(t_*, x, z) := G(t_*, x; −dt_* + z),        g̃ := p₁ − G₁ = (g⁻¹ − g₀⁻¹)(−dt_* + z, −dt_* + z),     {#eq:ii-c1-3-1}

so g̃ is quadratic in z, with |∂^αg̃| ≤ Cϵt_*^(−ℓ_K), |α| ≤ d₀, on compact z-sets.

**Lemma {#lem:ii-c1-3-2}** (The projected field.) For p := G (homogeneous of degree 2 on T*D), σ⁻¹H_p descends to
{σ > 0} ∩ ᵉ³ᵇS*_D M, and in the slice coordinates

    Ŵ := σ⁻¹H_p = (z·∂_zp₁ − 2p₁)∂_(t_*) + ∂_zp₁·∂_x − ∂_xp₁·∂_z − (∂_(t_*)p₁) z·∂_z.                     {#eq:ii-c1-3-2}

Ŵ is tangent to {p₁ = 0}, and on {p₁ = 0} it is a positive multiple of the field 𝖧_G of [[eq:ii-c-4-2]].

*Proof.* With τ := −σ, p = τ²p₁(t_*, x, −ζ/τ), so ∂_τp = σ(z·∂_zp₁ − 2p₁), ∂_ζp = σ∂_zp₁, ∂_(t_*)p = σ²∂_(t_*)p₁ and
∂_xp = σ²∂_xp₁; and for f = f(t_*, x, z), ∂_τf = σ⁻¹z·∂_zf and ∂_ζf = σ⁻¹∂_zf. Inserting these into
H_p = ∂_τp ∂_(t_*) + ∂_ζp·∂_x − ∂_(t_*)p ∂_τ − ∂_xp·∂_ζ gives [[eq:ii-c1-3-2]]. Next, Ŵp₁ = −2p₁∂_(t_*)p₁, which
vanishes on {p₁ = 0}. On the characteristic set, 𝖧_G = ρ_∞H_(G_(e3b)) = ρ_∞fH_G with f = x_I⁻²ρ₊⁻² > 0, so
𝖧_G = ρ_∞fσŴ. ∎

For g = g₀, [[eq:ii-c1-3-2]] on {G₁ = 0} is q₁∂_(t_*) + H_(G₁), as z·∂_zG₁ = q₁ there ([[lem:ii-b-5-2]] (d)): the
stationary field of [[sec:ii-b-2]].

#### Graphing the perturbed characteristic set {#sec:ii-c1-3-3}

Let N be a smooth vector field on a neighbourhood O_N of Γ in T*X̃° with NG₁ = 1 there (N := ∇G₁/|∇G₁|² for a
Riemannian metric, as dG₁ ≠ 0). After shrinking, Ψ̂₀(f, w) := e^(fN)(w) is a diffeomorphism from (−c, c) × Y onto a
neighbourhood of Y, and G₁(e^(fN)w) = f, as (d/df)G₁(e^(fN)w) = (NG₁)(e^(fN)w) = 1. Write w(x, z) and f(x, z) for the
inverse.

**Lemma {#lem:ii-c1-3-3}** (The graph.) For ϵ small there is F ∈ C^(d₀)((T_♭, ∞) × Y) with |∂^αF| ≤ Cϵt_*^(−ℓ_K) for
|α| ≤ d₀ and {p₁(t_*, ·) = 0} ∩ Ψ̂₀((−c, c) × Y) = {e^(F(t_*,w)N)w : w ∈ Y}. The map
Ψ̂(t_*, f, w) := (t_*, e^((f+F(t_*,w))N)w) is a C^(d₀) diffeomorphism onto a neighbourhood of the perturbed
characteristic set near Γ, with ‖Ψ̂ − Ψ̂₀‖_(C^(d₀)) ≤ Cϵt_*^(−ℓ_K) (where Ψ̂₀(t_*, f, w) := (t_*, e^(fN)w)), and it maps
{f = 0} onto the perturbed characteristic set.

*Proof.* At e^(fN)w, p₁ = f + g̃(t_*, e^(fN)w). The map f ↦ −g̃(t_*, e^(fN)w) sends [−c/2, c/2] into itself and has
Lipschitz constant sup|Ng̃| ≤ Cϵ < 1, so it has a unique fixed point F(t_*, w), with |F| ≤ Cϵt_*^(−ℓ_K). Since
∂_f(f + g̃(t_*, e^(fN)w)) = 1 + Ng̃ ≥ ½, F ∈ C^(d₀) by the implicit function theorem, and each derivative of order ≤ d₀
of the identity F + g̃(t_*, e^(FN)w) = 0 expresses ∂^αF through derivatives of g̃, each O(ϵt_*^(−ℓ_K)), and lower
derivatives of F. Ψ̂ is then C^(d₀)-close to Ψ̂₀, hence a diffeomorphism near f = 0. ∎

Near Γ, Ŵt_* = z·∂_zp₁ − 2p₁, which is ≥ ½β₀ near Γ for ϵ small: at ϵ = 0 it is exactly q₁, as
z·∂_zG₁ = 2g₀⁻¹(−dt_* + z, z) = 2G₁ + q₁. Put V^h := Ŵ/(Ŵt_*), a C^(d₀−1) vector field near (T_♭, ∞) × Γ with
V^ht_* = 1, tangent to {p₁ = 0} ([[lem:ii-c1-3-2]]), and V⁰ := Ŵ₀/(Ŵ₀t_*) = ∂_(t_*) + H_(G₁)/q₁ for g₀ (where
∂_(t_*)G₁ = 0). By [[eq:ii-c1-3-1]] and [[eq:ii-c1-3-2]], V^h − V⁰ has coefficients with derivatives of order ≤ d₀ − 1
bounded by Cϵt_*^(−ℓ_K). Let V := Ψ̂^*V^h restricted to {f = 0} = (T_♭, ∞) × Y, which is tangent to it since V^h is
tangent to the characteristic set; Vt_* = 1, as Ψ̂ preserves t_*. As Ψ̂₀^*V⁰ restricted to {f = 0} is
∂_(t_*) + q₁⁻¹H_(G₁) = ∂_(t_*) + 𝖵, and Ψ̂ − Ψ̂₀ and V^h − V⁰ are O(ϵt_*^(−ℓ_K)) in C^(d₀), resp. C^(d₀−1),

    V = ∂_(t_*) + 𝖵 + Ṽ,     Ṽ(t_*, ·) tangent to Y,     |∂^αṼ| ≤ Cϵt_*^(−ℓ_K),  |α| ≤ d₀ − 1.            {#eq:ii-c1-3-3}

#### The statement {#sec:ii-c1-3-4}

**Proposition {#prop:ii-c1-3-4}** (The stable and unstable hypersurfaces; [Hin26c, Proposition 6.3] at n = 4.) Let
d₀ ≥ 3, ℓ_K > 0 and g = g₀ + h with h ∈ 𝒢̃^(d₀,(0,0,ℓ_K))_(e3b) of sufficiently small norm ϵ. With T_♭ of
[[sec:ii-c1-3-2]], let ∂Γ₀ := {t_* > T_♭} × Γ in the slice coordinates (the stationary extension of ∂Γ_(K⁺),
[[def:ii-b-5-1]]), and U a small conic neighbourhood of it in ᵉ³ᵇS*_D M. There are functions φ₀^(u/s) ∈ C^∞(U),
independent of t_*, with φ₀^(u/s) = φ_(u/s)(x, z) on the stationary characteristic set, and φ̃^u ∈ C^(d₀−1)(U),
φ̃^s ∈ C^(d₀−2)(U), with

    |∂^αφ̃^u| ≤ Cϵt_*^(−ℓ_K)  (|α| ≤ d₀ − 1),        |∂^αφ̃^s| ≤ Cϵt_*^(−ℓ_K)  (|α| ≤ d₀ − 2),

derivatives along ∂_(t_*), ∂_x and the fibres, such that, with φ^(u/s) := φ₀^(u/s) + φ̃^(u/s), the field 𝖧_G is tangent
to Γ^(u/s) := ∂Σ⁺ ∩ U ∩ (φ^(u/s))⁻¹(0). For ϵ ≤ ϵ₁ the norms are at most 1. The same holds, with uniform constants, for
the stationary models of parameters b near b₀ ((K4)).

*Proof.* By [[lem:ii-c1-3-1]] and [[eq:ii-c1-3-3]], [[thm:ii-c1-1-1]] applies on Y with V₀ = 𝖵, k := d₀ − 1 ≥ 2,
ℓ := ℓ_K and T₀ := T_♭ (the metric is defined on Ω_* by [[eq:ii-c-4-1]], and Ω_* ⊃ {t_* ≥ T_♭} because t^♭_* ≥ C′t_*
by [[lem:ii-c-3-2]] (b)). It gives ψ_u ∈ C^(d₀−1) and ψ_s ∈ C^(d₀−2) on (T_♭, ∞) × O′ with V tangent to
W^(u/s) = {φ_(u/s) + ψ_(u/s) = 0}. For (t_*, x, z) in U, write (x, z) = e^(fN)w (w = w(x, z) ∈ Y) and put

    φ₀^(u/s)(x, z) := φ_(u/s)(w(x, z)),        φ̃^(u/s)(t_*, x, z) := ψ_(u/s)(t_*, w(x, z)),

extended homogeneously of degree 0 in (σ, ζ). On the perturbed characteristic set, (x, z) = e^(F(t_*,w)N)w
([[lem:ii-c1-3-3]]) and w(x, z) = w, so φ^(u/s)(t_*, x, z) = (φ_(u/s) + ψ_(u/s))(t_*, w), and
Γ^(u/s) = Ψ̂({f = 0} ∩ W^(u/s)). Since V is tangent to W^(u/s), V^h = Ψ̂_*V is tangent to Ψ̂(W^(u/s)); and Ŵ and 𝖧_G
are positive multiples of V^h on the characteristic set ([[lem:ii-c1-3-2]] and Ŵt_* > 0). The bounds follow by the
chain rule, w(x, z) being smooth and t_*-independent. Uniformity follows from [[lem:ii-c1-3-1]] and the explicit
dependence of the constants in [[thm:ii-c1-1-1]]. ∎

**Remark {#rem:s05-trapped-hypersurfaces}** (a) φ₀^(u/s) agrees with φ_(u/s) of (H7) on the stationary characteristic
set; off it the two may differ, which is immaterial for Γ^(u/s). (b) The intersections of Γ^(u/s) with the stationary
face {t_* = ∞} are the sets Γ^(u/s)_(K⁺) of [[def:ii-b-5-1]] (within U), as φ̃^(u/s) → 0. (c) W^u at t_* = T_♭ is the
stationary unstable hypersurface; [Hin26c, p. 113] makes the same choice at its slice {ρ_K = 1} ("Γ^u = ⋃_(s≥0)
e^(sV)(Γ^u₀ ∩ {ρ_K = 1})"). The slice is immaterial in the sequel: [[ch:s06]] uses Γ^(u/s) only where ρ_K is small.

### Remarks on [Hin26c] and [Hin21] {#sec:s05-literature}

The following points compare this chapter with the texts it writes out in dimension 4 + 1.

- *The stationary model.* The arguments of [Hin26c, Lemmas 4.1–4.3, 4.7, 4.10–4.18 and Proposition 4.19] from the
  explicit Kerr metric are replaced by the hypotheses (H3), (H4), (H7), (H8) and (K3), from which [[sec:ii-b-2]]
  recovers the dynamics over the Kerr face. [Hin26c, Lemma 4.20] serves in [Hin26c] only to prove part (3) of [Hin26c,
  Proposition 4.19] from the Carter flow, and is not needed here, (K3) being assumed for 𝖵 itself. The first row of
  [Hin26c, (4.72)], the curves over M°, is replaced by [[prop:ii-b-8-2]], the form that [Hin26c] states as its
  Proposition 6.1 and uses later ([Hin26c, p. 111]).
- *Rates.* (K1) has r⁻² where Kerr has r⁻¹, and no logarithm enters the hyperboloidal time. Accordingly
  [[eq:ii-b-1-2]] has ρ₀²x_I²ρ₊² for ρ₀x_I²ρ₊, H_(G_(3b)) − H_(Ḡ_(3b)) ∈ ρ₊²𝒱_b where [Hin26c] has ρ₊,
  G_(eb) − Ḡ_(eb) ∈ x_I²ρ₊²P^[2], S = 0 in [[lem:ii-c-1-3]], and the remainder of [[eq:ii-c-1-2]] carries ρ⁴. Nothing
  uses more than the rates of [Hin26c], except the shortened proofs of [[lem:ii-b-3-3]] (1)–(2).
- *The constants at n = 4.* The 1 of [Hin26c, (5.1a)] is 3/2; the factor 2(1 + S) of [Hin26c, (5.7)] is 3 + 2S; the
  characteristic exponents 2(1 + μ) are 3 + 2μ; the tf-weight α_sf + 3/2 is α_sf + 2; the sf-weights (−3/2, −1/2) of the
  scalar wave operator are (−2, 0). The symmetry of −2∂_(t_*)ρ(ρ∂_ρ − c) for the density ρ^(−n−1)dρ forces
  c = (n − 1)/2, and with it [[lem:ii-c-2-6]].
- *Misprints in [Hin26c].* In the proof of [Hin26c, Lemma 4.6 (2)], ρ₊ ∘ γ is strictly decreasing for s > 0 (a critical
  point is a strict local maximum), where the text says "strictly increasing"; the argument is otherwise as in
  [[lem:ii-b-3-3]] (2), which also shows why ρ₊ → 0. In [Hin26c, Lemma 4.6 (4)], the conic extension of
  {ξ̂_(3b) = 2} is {ξ_(3b) = 2σ_(3b)}, printed as ξ_(3b) = −2σ_(3b), and within Σ⁺ it is the characteristic set of
  2r∂_(t_*) − r∂_r = r(∂_t − ∂_r), printed as r∂_(t_*) − 2r∂_r; the (t, r)-form r(∂_t − ∂_r) given there is the right
  one. [Hin26c, (4.18)] has the factor −2 in place of −4; only the sign is used. The angular coefficient 1 in G⁰_(eb)
  ([[eq:ii-b-7-1]]) comes from the angular term g_(𝕊³)/(2x_I²) of ḡ near ℐ⁺ ∩ ι⁺ ([[sec:ii-a-2-3]]); the term
  g_(𝕊³)/x_I² printed in [Hin26c, (2.27)] would give ½|η_(eb)|², and [Hin26c, (4.67)] agrees with the former. On
  [Hin26c, p. 107], after Definition 5.15, the section x_I⁻²ρ₊⁻²(g_(m,a) + h) should read x_I²ρ₊²(g_(m,a) + h)
  ([[rem:s05-metric-class]] (b)). [Hin26c, Definition 5.11 (1)] says "monotonically non-decreasing along the future
  null-bicharacteristic flow", which contradicts its own condition ±H_G𝗌 ≤ 0 on ∂Σ^± and [Hin26c, Section 6.2]: the
  order is non-increasing, high at the radial sets that the future flow leaves and low at those it approaches
  ([[def:ii-c-2-4]] (1)). In [Hin26c, (6.5)], a covector ζ ∈ Σ lies in Σ⁺ if and only if g⁻¹(ζ, dt^♭_*) > 0, not ≤ 0,
  since dt^♭_* is past timelike.
- *Proofs written out.* [Hin26c, Lemma 5.16] takes "a smoothing" of a piecewise function; a smoothing preserves
  timelikeness only if its differential stays in the past cone, and [[lem:ii-c-3-2]] glues by a smooth minimum in log
  and a smooth maximum in r, whose differentials are convex combinations of those of the pieces; the comparison of the
  pieces at r = Ct_* is the inequality φ′ < 0 there. The backward statement of [Hin26c, Proposition 6.1] is proved in
  [[prop:ii-c-4-2]] by the repulsion of ∂R_(ℐ⁺,out) in x_I backward. [Hin26c, Proposition 6.4] is proved by the
  construction it cites ([[sec:ii-c-5-2]]), with item (5) added and the localisation χ_t of [Hin23c] unnecessary in
  this class; the bound on the characteristic set stated as [Hin23c, (C.1)] is replaced by [[lem:ii-c-5-3]].
- *Changes of statement.* [[def:ii-c-2-1]] takes the threshold of trapping admissibility from (Γ.4), for the density of
  [[ch:s01]], in place of [Hin26c, (5.8)] for |dg|, and realises [Hin26c, (5.9)] as [[lem:i-b-6-0]];
  [[def:ii-c-2-3]] is the tf-admissibility of [[def:i-c-5-1]]. [[prop:ii-c-4-2]] is stated over {r ≥ r₀}, where the
  perturbation is defined, with "reaches {r = r₀}" for "crosses {r = m}".
- *The persistence of the trapped hypersurfaces.* The proof of [Hin26c, Proposition 6.3] rests on
  [Hin21, Theorem 2.6]. That theorem is stated for a closed manifold, a C^∞ invariant splitting (the relaxation to
  continuous splittings is [Hin21, footnote 8]) and a fixed perturbation, and the uniformity in the perturbation that
  [Hin26c] asserts is a reading of its proof. [[thm:ii-c1-1-1]] proves what is needed directly, with explicit
  dependence of the constants, from (Γ.1)–(Γ.3) and the tangential half of (K3), so the continuous splitting of (K3) is
  enough and is not used. [Hin26c] states φ̃^(u/s) ∈ C^(d₀−1,ℓ_K)_cu on all of the cosphere bundle over D; here
  φ̃^u ∈ C^(d₀−1) and φ̃^s ∈ C^(d₀−2), on a neighbourhood U of ∂Γ₀: the stable hypersurface is obtained as a limit and
  loses one derivative. d₀ is a free parameter, taken large wherever [[prop:ii-c1-3-4]] is used ([[ch:s06]]), and only
  a neighbourhood of the trapped set enters the trapping estimates. The graphing of the characteristic set on
  [Hin26c, p. 113] is [[lem:ii-c1-3-3]], with the projected field computed in [[lem:ii-c1-3-2]]; the space ℝ⁵ there is
  the five-dimensional characteristic set of Kerr at fibre infinity over (K⁺)°, which at n = 4 is seven-dimensional.
