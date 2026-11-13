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

The weight in (2) is the weight α_sf + 3/2 of [Hin26c] at n = 4: by [[lem:i-c-2-2]], ρ^α L²(|dx|) = ρ^(α+2)L²(μ_b), so
the spatial weight α of an L²(|dx|)-based space is the b-weight α + 2 at n = 4 (that is, α + n/2; see
[[sec:i-c-1-2]]). In particular α_sf + 2 lies in
an indicial gap of P̂₀(0). For the scalar wave operator the gap is (0, 2), the indicial roots of [[eq:ii-c-1-3]] at
ℓ = 0 being 0 and 2, so α_sf ∈ (−2, 0), where [Hin26c] has (−3/2, −1/2).

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
