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

with β₀, β of (H3). So ∂R_(ℋ⁺) is a source for the flow within ³ᵇS*_((K⁺)°)M₀ (not only within ∂Σ⁺), ρ_∞ grows
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
