## The dynamics of the Myers–Perry metrics near Tangherlini {#ch:s12}

This chapter verifies, for the Myers–Perry metrics g_b of [[ch:s11]] with b near the Schwarzschild–Tangherlini
parameter b₀ = (m₀, 0) and with the time function t_* of [[eq:iii-b-3-6]], the hypotheses on the metric that
[[ch:s01]], [[ch:s02]] and [[ch:s05]] leave open. They are: the radial structure of the horizon in (H3) and (H4)
([[sec:i-a-1-3]]); the Lorentzian structure and the time function (H6) ([[sec:i-b-1-2]]); the normally hyperbolic
trapping (Γ.1)–(Γ.3) of (H7) and the global dynamics (H8) ([[sec:i-b-1-5]]); the decay (K1) and the r-normal
hyperbolicity (K3) of [[sec:ii-b-1-1]]; and the uniformity in b that (H5), its extension in [[sec:i-b-1-5]], and (K4)
ask. We write (Dyn) for all of them together. They concern the metric alone, and every operator whose principal symbol
is g_b⁻¹ ⊗ Id has them. The threshold in (H3) and the condition (Γ.4) of (H7) involve the subprincipal symbol; they are
hypotheses on the operator and are verified for each operator in [[ch:s13]], [[ch:s14]] and [[ch:s15]].

[[sec:vi-a-0]]–[[sec:vi-a-6]] treat g_(b₀), five-dimensional Schwarzschild–Tangherlini, where everything is explicit;
(H6) and (K1) are proved there for every b. [[sec:vi-a-0]] also proves three facts about the photon sphere and the
interior of Tangherlini ([[prop:np-10-19-iv]], [[prop:np-10-17-ii]], [[prop:np-10-19-ii]]) that the theory of the
gauge potential operator uses as well. [[sec:vi-b-1]]–[[sec:vi-b-2]] carry the horizon hypotheses to b near b₀; the
one new fact is that the horizon of g_b is a level set of the Kerr–Schild radius r_A, null by an exact identity.
[[sec:vi-b1-0]]–[[sec:vi-b1-5]] treat the trapped set and the global dynamics near b₀. The tool is the separability
of the null geodesic flow of five-dimensional Myers–Perry, which holds in the Kerr–Schild coordinates of [[ch:s11]]
written in spheroidal form; it plays the part of Carter's constant in [Hin26c, Section 4.2.3], and it gives the trapped
set and its stable and unstable hypersurfaces in closed form, smooth in b. Every object near b₀ is defined from A
directly, without an eigenframe of A, which is not continuous in A at A = 0 nor where the two spins have equal
modulus; frames are used only to compute.

The inner radius of the spacetime is a parameter r_♭ ∈ (0, ½R₁], and the radii of [[sec:i-a-1-1]] are fixed in terms
of it in [[def:s12-radii]]. Every result of the chapter holds for every such r_♭, with constants that depend on it.

*Notation.* The black-hole mass is m, as in [[ch:s05]]: b = (m, A), b₀ = (m₀, 0), R₁ = m₀^(1/2). Some letters keep
the meaning they have in [[ch:s11]] and carry a second one here, separated by context: H_(m,A) is the Kerr–Schild
function of [[def:iii-b-3-2]], while H_p is the Hamilton vector field of p, with H_p f = ∂_ζ p ∂_z f − ∂_z p ∂_ζ f;
ψ is the profile of t_* in [[sec:vi-a-0]]–[[sec:vi-a-6]] and an azimuth in [[sec:vi-b1-0]]–[[sec:vi-b1-5]]; Φ is a
momentum in [[sec:vi-b1-0]] and Φ_m the change of time of [[eq:iii-b-3-3]]; E is a momentum, not a bundle. The
Poisson bracket is {a, b} := H_a b. The polar angle on 𝕊³ is ϑ.

### The radii {#sec:s12-radii}

**Definition {#def:s12-radii}** (The radii and the parameters.) Let m₀ > 0, R₁ := m₀^(1/2) and b₀ := (m₀, 0) be as
in [[sec:iii-b-2]], and fix an *inner radius* r_♭ ∈ (0, ½R₁]. The radii of [[sec:i-a-1-1]] are

    r₀ := r_♭,     δ₀ := min(R₁/16, r_♭/4),     r₂ := 7R₁/8,     r_e := 17R₁/16,                         {#eq:s12-radii}

and r_h := R₁ is the radius of the horizon of g_(b₀). The *collar* is {r₀ − 2δ₀ ≤ |x| ≤ r₀}, and
X̃° = {|x| > r₀ − 2δ₀}. The parameter set is

    ℬ_♭ := {b = (m, A) : |m − m₀| < ½m₀, ‖A‖ < ε_♭R₁},     ε_♭ := min(1/20, r_♭/(4R₁)),

with ‖A‖ the operator norm of A ∈ 𝔰𝔬(4), and |b − b₀| denotes a fixed norm on ℝ × 𝔰𝔬(4). The time function is
t_* := t − ψ(|x|) of [[eq:iii-b-3-6]] with ψ(ρ) := ∫_(r_♭)^ρ (1 − χ_∞(s) 8m₀ s⁻²) ds on [r₀ − 2δ₀, ∞); a different
lower limit changes t_* by a constant, which changes none of the statements below.

These radii are ordered:

    ½r_♭ ≤ r₀ − 2δ₀ < r₀ − δ₀ < r₀ < r₂ < r_h < r_h + δ₀ ≤ r_e,

since δ₀ ≤ r_♭/4, r_♭ ≤ ½R₁ < 7R₁/8 and δ₀ ≤ R₁/16. Since χ_∞ = 0 on (−∞, 2R₁], ψ′ = 1 on [r₀ − 2δ₀, 2R₁]. At
r_♭ = ½R₁ the radii are r₀ − 2δ₀ = 3R₁/8, r₀ − δ₀ = 7R₁/16, r₀ = ½R₁, r₂ = 7R₁/8 and r_e = 17R₁/16, and r₀ is the
inner radius of [[sec:iii-b-2]]. Every constant and every neighbourhood of b₀ chosen below may depend on r_♭; nothing is
claimed uniform in r_♭.

**Lemma {#lem:s12-ks-domain}** (The Kerr–Schild form on the collar.) Let b = (m, A) with m > 0 and ‖A‖ < r_♭/4; this
holds for every b ∈ ℬ_♭, and, when r_♭ = ½R₁, for every b in the parameter set ℬ of [[sec:iii-b-3-1]]. On
{|x| ≥ ½r_♭}: |x|² > s, the condition ‖A‖²(r_A² + ‖A‖²) < r_A⁴ of [[lem:iii-b-3-3]] (c) holds, and
g^KS_b := g^KS_(m,A) of [[def:iii-b-3-2]] is a smooth Lorentzian metric of signature (1, 4) on ℝ_t × {|x| ≥ ½r_♭},
with H_(m,A) > 0, depending smoothly on b.

*Proof.* In a frame in which A = aJ₁₂ + bJ₃₄ ([[lem:iii-b-3-1]]), s = a² + b² ≤ 2 max(a², b²) = 2‖A‖², and
‖A‖² < r_♭²/16. So |x|² ≥ r_♭²/4 > r_♭²/8 > 2‖A‖² ≥ s. By [[lem:iii-b-3-1]] (b),
r_A² ≥ |x|² − ‖A‖² > r_♭²/4 − r_♭²/16 = 3r_♭²/16 > 3‖A‖². Hence

    ‖A‖²(r_A² + ‖A‖²) < (r_A²/3)(r_A² + r_A²/3) = (4/9) r_A⁴ < r_A⁴,

which is the condition of [[lem:iii-b-3-3]] (c); so F_A ∈ (0, 1] and H_(m,A) > 0. By [[lem:iii-b-3-1]] (b), r_A is
smooth in (x, A) on {|x|² > s}, and P(r_A) > 0, so ℓ_A, F_A and H_(m,A) are smooth in (x, b), and g^KS_b is smooth.
For c ∈ [0, 1] let g_c := η + cH_(m,A) k_A ⊗ k_A. As k_A is null for η ([[lem:iii-b-3-3]] (a)), the computation of
[[lem:iii-b-3-3]] (d) with cH_(m,A) for H_(m,A) gives g_c⁻¹ = η⁻¹ − cH_(m,A) k_A^♯ ⊗ k_A^♯; so every g_c is
non-degenerate. A continuous path of non-degenerate symmetric forms has constant signature, and g₀ = η has signature
(1, 4). So g₁ = g^KS_b has signature (1, 4). ∎

The ratio r_♭/4 is all the lemma uses of the parameter set. At r_♭ = ½R₁ it is R₁/8, while the parameter set of
[[sec:iii-b-3-1]] has ‖A‖ < R₁/10; so on that set the lemma holds on {|x| ≥ R₁/4}.

### Schwarzschild–Tangherlini: coordinates and the spectral symbols {#sec:vi-a-0}

In [[sec:vi-a-0]]–[[sec:vi-a-6]], b = b₀, and we write m := m₀, f := 1 − m r⁻², r_h := m^(1/2) = R₁,
r_ph := (2m)^(1/2) = √2 R₁ and g̸ for the round metric of 𝕊³. By [[eq:iii-b-3-3]] and [[lem:iii-b-3-5]],
g_(b₀) = Φ_m^* g^KS_(m,0), where Φ_m changes the time coordinate by a function of r = |x|, and
g^KS_(m,0) = η + m r⁻²(dt + dr)² ([[prop:iii-b-3-4]]). With t_KS the time coordinate of g^KS_(m,0) and v := t_KS + r,

    g_(b₀) = −f dv² + 2 dv dr + r² g̸     on ℝ_v × {r > 0},                                                {#eq:vi-a-0-1}

as a direct expansion shows: with H := m r⁻², −f dv² + 2 dv dr = −(1 − H) dt_KS² + 2H dt_KS dr + (1 + H) dr², and
this is η + H(dt_KS + dr)² − r²g̸. Every time function used here has the form τ = v − F(r) with F smooth: t_* is one,
since t_* − t_KS is a function of r ([[eq:iii-b-3-3]], [[eq:iii-b-3-6]]); and on {r > r_h} so is the static time
t_s := v − r_*, r_*′ = f⁻¹, in which g_(b₀) = −f dt_s² + f⁻¹ dr² + r² g̸.

*The symbols.* For a time function τ with dτ timelike, [[eq:i-b-1-1]] defines G₀, τ₁ and g₀₀ by
G(−σ dτ + ζ) = G₀(ζ) + στ₁(ζ) + σ²g₀₀, with G := g⁻¹ and ζ ∈ T*X̃, and for z₀ ∈ {1, −1} we put
G_(z₀)(ζ) := G(−z₀ dτ + ζ). Write ζ = ξ dr + η with η ∈ T*𝕊³, and C := |η|²_g̸. From [[eq:vi-a-0-1]],
G^(vv) = 0, G^(vr) = 1, G^(rr) = f and G = r⁻²g̸⁻¹ on T*𝕊³; and dτ = dv − F′dr, so that −σ dτ + ζ =
−σ dv + (ξ + σF′) dr + η. Expanding,

    G₀ = fξ² + r⁻²C,     τ₁ = −2(1 − F′f)ξ,     g₀₀ = F′²f − 2F′,                                         {#eq:vi-a-0-2}

    G^(F)_(z₀) = fξ² + r⁻²C − 2z₀(1 − F′f)ξ + F′²f − 2F′.

At F = 0 this is fξ² − 2z₀ξ + r⁻²C, regular for all r > 0. At F = r_*, on {r > r_h}, it is

    G^s := fξ² + r⁻²C − f⁻¹,                                                                                {#eq:s12-static-symbol}

the static form, which does not depend on z₀ ∈ {1, −1}.

**Lemma {#lem:vi-a-0-1}** (Change of time function.) Let τ and τ′ = τ − F(r) be functions on a region U, and define
G_(z₀)(ζ) := G(−z₀ dτ + ζ) and G′_(z₀) likewise with τ′, whether or not the differentials are timelike.

(a) G′_(z₀)(ζ) = G_(z₀)(ζ + z₀ dF). The fibre translation T_F : (x, ζ) ↦ (x, ζ + z₀ dF(x)) is a symplectomorphism of
T*U that maps {G′_(z₀) = 0} onto {G_(z₀) = 0} and intertwines the Hamilton vector fields. It preserves fibre infinity
and C, and it moves ξ by z₀F′(r).

(b) If dτ and dτ′ are timelike with the same time orientation, T_F preserves the components Σ^±_(z₀) of
[[lem:i-b-1-1]] (e), and so the future fields on corresponding components.

(c) At one covector ν = −z₀ dτ′ + ζ = −z₀ dτ + (ζ + z₀ dF), the functions q′_(z₀) := 2G(ν, dτ′) and
q_(z₀) := 2G(ν, dτ) satisfy q′_(z₀) = q_(z₀) − 2F′(r) G(ν, dr), and 2G(ν, dr) = H_(G_(z₀)) r. So q′_(z₀) = q_(z₀)
wherever H_(G_(z₀)) r = 0, in particular on an invariant set on which r is constant.

*Proof.* (a) −z₀ dτ′ + ζ = −z₀ dτ + ζ + z₀ dF. Translation by a closed 1-form is symplectic, and
G′_(z₀) = G_(z₀) ∘ T_F, so T_F maps Hamilton vector fields to Hamilton vector fields; no causal hypothesis enters.
(b) The covector is the same spacetime covector. For a null ν ≠ 0, G(ν, dτ) and G(ν, dτ′) are nonzero with the same
sign, since dτ and dτ′ are timelike with the same orientation. That sign fixes the component ([[lem:i-b-1-1]] (e)).
(c) dτ′ = dτ − F′dr, and H_(G_(z₀)) r = ∂_ξ G_(z₀) = 2G(−z₀ dτ + ζ, dr). ∎

So every statement about the flow of G_(z₀) over a range of r may be proved in whichever coordinates are convenient
there: v near and inside the horizon, t_s on {r > r_h}, t_* near infinity. The components Σ^±_(z₀) are always those of
t_*; on {r > r_h} they are the same as those of t_s by (b), as dt_s and dt_* are co-oriented there:
G(dt_s, dt_*) = −f⁻¹ < 0. The differential of v is null (G^(vv) = 0), and v is used only as a symplectic chart, by (a).
Near ℋ, t_* = v − F with F′ > 0, since g₀₀ = F′²f − 2F′ < 0 at f = 0; so G(dv, dt_*) = −F′ < 0, dv lies in the closed
causal cone of dt_*, and q_v := 2G(ν, dv) = 2ξ has the sign of t_*'s q_(z₀) wherever it is nonzero. The future field
on Σ^±_(z₀) is ±H_(G_(z₀)) ([[sec:i-b-1-3]]). On {r > r_h}, in static variables, q_(z₀) = 2G(−z₀ dt_s + ζ, dt_s) =
2z₀f⁻¹, so only Σ^(z₀)_(z₀) occurs there, with future field 𝖧^♭ := z₀H_(G^s).

#### The photon sphere and the interior {#sec:s12-static}

The next three propositions hold for five-dimensional Schwarzschild–Tangherlini of any mass m > 0, with f, r_h and
r_ph as above. They are stated in the static variables of [[eq:s12-static-symbol]] outside the horizon and in the
ingoing chart [[eq:vi-a-0-1]] inside it. For functions of (r, ξ, C) and covectors ζ = −σ dt_s + ξ dr + η the Hamilton
vector field acts on functions of (r, ξ) as H_p = ∂_ξp ∂_r − ∂_rp ∂_ξ, C and σ being conserved by every Hamilton
vector field of a function of (r, ξ, C, σ).

**Proposition {#prop:np-10-19-iv}** (The radial potential and the interior.)

(a) On {r > r_h}, at points of {G^s = 0}, f²ξ² = 1 − CW with W := f r⁻².

(b) W′ = 2(2m − r²) r⁻⁵. On (r_h, ∞), W has exactly one critical point, a maximum W = (4m)⁻¹ at r² = 2m; W(r_h) = 0
and W → 0 as r → ∞.

(c) f is increasing on (0, ∞) and vanishes exactly at r_h. So g(∂_(t_s), ∂_(t_s)) = −f < 0 on {r > r_h}, and, in the
chart [[eq:vi-a-0-1]], g⁻¹(dr, dr) = f < 0 on {0 < r < r_h}: there dr is timelike.

(d) In the chart [[eq:vi-a-0-1]], g_(vr) = 1, −∂_r is a nowhere vanishing null vector field and g(∂_v, −∂_r) = −1.
For the time orientation in which ∂_v is future directed on {r > r_h}, −∂_r is future directed on all of {r > 0}, and
on {0 < r < r_h} the vector field g⁻¹(dr, ·) is future directed timelike, with dr(g⁻¹(dr, ·)) = f < 0: r decreases
along future causal curves there. The time orientation of [[sec:i-b-1-2]], in which −∇t_* is future directed, is this
one.

*Proof.* (a) G^s = 0 means fξ² = f⁻¹ − r⁻²C; multiply by f. (b) W = r⁻² − m r⁻⁴, so W′ = −2r⁻³ + 4m r⁻⁵ =
2(2m − r²)r⁻⁵, which is positive on (r_h, r_ph) and negative on (r_ph, ∞). At r² = 2m, W = ½(2m)⁻¹ = (4m)⁻¹;
W(r_h) = 0 as f(r_h) = 0, and 0 < W < r⁻² for r > r_h. (c) f′ = 2m r⁻³ > 0, and f(r) = 0 iff r² = m. By
[[eq:vi-a-0-2]] at F = r_*, g_(t_s t_s) = −f. In the chart [[eq:vi-a-0-1]], g⁻¹(dr, dr) = G^(rr) = f. (d) The
coefficients are read off [[eq:vi-a-0-1]]: g(∂_r, ∂_r) = 0 and g(∂_v, ∂_r) = 1. On {r > r_h}, ∂_v is timelike
(g(∂_v, ∂_v) = −f < 0), and a null vector with negative product with a future timelike vector is future directed;
−∂_r is null and nowhere zero on the connected chart, so it stays future directed by continuity. On {0 < r < r_h},
X := g⁻¹(dr, ·) has g(X, X) = f < 0 and g(X, −∂_r) = dr(−∂_r) = −1 < 0, so X lies in the cone of −∂_r. A future
causal V then has dr(V) = g(X, V) < 0. Finally, on {r > r_h}, g(∂_v, −∇t_*) = −dt_*(∂_v) = −1 < 0 with −∇t_* future
timelike, so ∂_v is future directed in the orientation of [[sec:i-b-1-2]]. ∎

**Proposition {#prop:np-10-17-ii}** (The trapped set at frequency σ.) Let σ ∈ ℝ ∖ {0} and, on {r > r_h},
G(ζ) := g⁻¹(ζ, ζ) = fξ² + r⁻²C − σ²f⁻¹ for ζ = −σ dt_s + ξ dr + η.

(a) At points of {G = 0, ξ = 0}, H_G ξ = 2C(r² − 2m)/(f r⁵).

(b) The trapped set {ξ = 0, H_G ξ = 0} ∩ {G = 0} over {r > r_h} ([Hin26c, Definition 4.13]) is
{r² = 2m, ξ = 0, C = 4mσ²}, and C > 0 there.

(c) At every point of that set, dξ, d(H_G ξ) and dG are linearly independent.

(d) There H_G t_s = 2σ/f = 4σ, and the linearisation of the (r, ξ)-component of the vector field H_G/(H_G t_s), at
fixed C and σ, has the eigenvalues ±ν with ν := (2m)^(−1/2) = 1/r_ph.

*Proof.* We have H_G r = ∂_ξG = 2fξ and

    H_G ξ = −∂_r G = −f′ξ² + 2C r⁻³ − σ²f′f⁻²,     f′ = 2m r⁻³.                                             {#eq:s12-hxi}

(a) At ξ = 0, G = 0 gives σ² = fC r⁻². Substituting, H_G ξ = C r⁻³(2 − r f′f⁻¹) = C(2f − r f′)/(f r³), and
2f − rf′ = 2 − 4m r⁻² = 2(r² − 2m)r⁻². (b) For r > r_h, f > 0, and C > 0 on {G = 0, ξ = 0} since σ ≠ 0 and
C = σ²r²f⁻¹. So H_G ξ = 0 there exactly when r² = 2m, where f = ½ and C = σ²·2m·2 = 4mσ². (c) Differentiating
[[eq:s12-hxi]] in r at fixed (ξ, C, σ),

    ∂_r(H_G ξ) = −f″ξ² − 6C r⁻⁴ − σ²(f″f⁻² − 2f′²f⁻³),     f″ = −6m r⁻⁴.

At r² = 2m, ξ = 0, C = 4mσ² = 2r²σ²: f = ½, f′ = r⁻¹, f″ = −3r⁻², so f″f⁻² = −12r⁻², 2f′²f⁻³ = 16r⁻², and
∂_r(H_G ξ) = −12σ²r⁻² + 28σ²r⁻² = 16σ²r⁻² ≠ 0. dξ has no dr component; dG has neither a dr nor a dξ component there,
as ∂_rG = −H_Gξ = 0 and ∂_ξG = 2fξ = 0, while ∂_C G = r⁻² ≠ 0. If a dξ + b d(H_Gξ) + c dG = 0, the dr component gives
b = 0, the dξ component a = 0, and then c = 0. (d) With ζ_t := −σ the dt_s-component of ζ, G contains −ζ_t²f⁻¹, so
H_G t_s = ∂_(ζ_t)G = −2ζ_t f⁻¹ = 2σf⁻¹ = 4σ at r² = 2m. The (r, ξ)-component of H_G, (2fξ, H_Gξ), vanishes at the set,
so the linearisation of the field divided by H_G t_s is the linearisation of (2fξ, H_Gξ) divided by 4σ. At fixed C and
σ that linearisation is δṙ = 2f δξ = δξ and δξ̇ = ∂_r(H_Gξ) δr = 16σ²r⁻² δr (the dξ-derivative of H_Gξ is −2f′ξ = 0),
with eigenvalues ±4|σ|r⁻¹. Divided by 4σ they are ±r_ph⁻¹. ∎

**Proposition {#prop:np-10-19-ii}** (The trapped set of the semiclassical family at z₀ = 1.) On {r > r_h} let
G₁ := G^s = fξ² + r⁻²C − f⁻¹ and Σ₁ := {G₁ = 0}.

(a) The only point (r, ξ, C) of Σ₁ over {r > r_h} at which H_(G₁) r = H_(G₁) ξ = 0 is r² = 2m, ξ = 0, C = 4m.

(b) Fix C = 4m. The linearisation at (r_ph, 0) of the (r, ξ)-component of H_(G₁) has the eigenvalues ±ν,
ν := 4(2m)^(−1/2). The functions φ_(s/u) := ξ ± (ν/(2f))(r − r_ph) vanish at (r_ph, 0), and their differentials there
are left eigenvectors: d(H_(G₁)φ_s) = ν dφ_s and d(H_(G₁)φ_u) = −ν dφ_u at (r_ph, 0). The same holds on Σ₁ near the
point, with C = r²(f⁻¹ − fξ²), whose differential in (r, ξ) vanishes there.

(c) {φ_u, φ_s} = ν/f = 2ν > 0 at (r_ph, 0), and ∂_C G₁ = r⁻² ≠ 0.

(d) With q₁ := 2g⁻¹(−dt_s + ζ, dt_s), ½q₁ = f⁻¹, which is 1/f(r_ph) = 2 at the point; for a time function t_s − F(r)
the value at the point is the same. So the constant β₀ = ½ min_Γ |q₁| of (Γ.4) is 2, and ν/(4β₀) = (8m)^(−1/2), half the
rate (2m)^(−1/2) of [[prop:np-10-17-ii]] (d).

*Proof.* (a) H_(G₁) r = 2fξ vanishes for r > r_h only at ξ = 0; there G₁ = 0 gives C = r²f⁻¹, and
H_(G₁) ξ = −∂_rG₁ = −f′f⁻² + 2Cr⁻³ = (2f − rf′)/(f r) = 2(r² − 2m)/(f r³), which vanishes only at r² = 2m; then
C = 2m·2 = 4m. This is [[prop:np-10-17-ii]] (a)–(b) at σ = 1. (b) By [[prop:np-10-17-ii]] at σ = 1, the linearisation
is δṙ = δξ, δξ̇ = 16 r_ph⁻² δr, with eigenvalues ±4r_ph⁻¹ = ±ν. For a function φ vanishing at the zero p of a vector
field V, d(Vφ)_p = dφ_p ∘ DV_p. Here dφ_(s/u) = dξ ± ν dr at p, as f(r_ph) = ½ and (r − r_ph) vanishes at p, and
(dξ ± ν dr)(δξ̇, δṙ) = 16r_ph⁻² δr ± ν δξ = ν²δr ± νδξ = ±ν(δξ ± νδr). On Σ₁, ∂_ξC = −2r²fξ = 0 and
∂_rC = r(2f − rf′)f⁻² = 0 at p, so the linearisation on Σ₁ in the coordinates (r, ξ) is the one at fixed C.
(c) At p, ∂_ξφ_(s/u) = 1 and ∂_rφ_(s/u) = ±ν/(2f), the term with the derivative of f⁻¹ vanishing with r − r_ph. So
{φ_u, φ_s} = ∂_ξφ_u ∂_rφ_s − ∂_rφ_u ∂_ξφ_s = ν/(2f) + ν/(2f) = ν/f = 2ν. ∂_CG₁ = r⁻² by inspection. (d) In static
variables g⁻¹(dt_s, dt_s) = −f⁻¹ and g⁻¹(dt_s, dr) = 0 = g⁻¹(dt_s, η), so q₁ = 2·(−1)(−f⁻¹) = 2f⁻¹. For t_s − F(r),
[[lem:vi-a-0-1]] (c) gives the same value where H_(G₁) r = 0, in particular at p. Finally ν/8 = ½(2m)^(−1/2) =
(8m)^(−1/2). ∎

The functions φ_(s/u) of [[prop:np-10-19-ii]] are linearisations at Γ. The hypotheses (Γ.1)–(Γ.2) ask for exact
invariant hypersurfaces; for Tangherlini they are the two branches fξ = ±(1 − 2m r⁻²) of {C = 4m} ∩ Σ₁, with the
exact rates of [[eq:vi-a-3-2]] below.

### The Lorentzian structure and the decay {#sec:vi-a-1}

**Lemma {#lem:vi-a-1-1}** ((H6) and (K1) for every b.) Let b = (m, A) with |m − m₀| < ½m₀ and ‖A‖ < r_♭/4; in
particular b ∈ ℬ_♭ is allowed. With τ = t_*: g_b is a smooth Lorentzian metric of signature (1, 4) on
ℝ × {|x| ≥ r₀ − 2δ₀} (the closure of X̃°; (H6) uses X̃° = {r > r₀ − 2δ₀}) with t_*-independent components,
g₀₀ = g_b⁻¹(dt_*, dt_*) < 0, and G₀, τ₁, g₀₀ given by [[eq:i-b-1-1]]. On {r > 3R₁} the components of g_b − ḡ in the
frame dt_*, dx^i lie in ρ²C^∞(X̄), uniformly and smoothly in b. So (H6), (K1) and the first clause of (K4) hold.

*Proof.* On {|x| ≤ 2R₁}, T_m of [[eq:iii-b-3-3]] is constant, so g_b is g^KS_b in a translated time coordinate, and
r₀ − 2δ₀ ≥ ½r_♭; so g_b is smooth and Lorentzian of signature (1, 4) there, smoothly in b, by [[lem:s12-ks-domain]].
On {|x| ≥ ½R₁}, [[prop:iii-b-3-6]] gives smoothness and g_b − ḡ_η ∈ |x|⁻²C^∞, smoothly in b, where ḡ_η := η.
*dt_* is timelike.* As in the proof of [[lem:iii-b-3-7]] (a): in the coordinates (t_KS, x) = Φ_m(t, x), a function
t − φ(|x|) has differential dt_KS − β d|x| with β := φ′ − T_m′. For φ = ψ, β = 1 off supp χ_∞, that is on
[r₀ − 2δ₀, 2R₁], where ψ′ = 1 and T_m′ = 0; and on supp χ_∞ ⊂ [2R₁, ∞) the computation of [[lem:iii-b-3-7]] (a), which
does not involve the inner radius, gives β ∈ (−1, 1). So β ∈ (−1, 1] on [r₀ − 2δ₀, ∞), and [[lem:iii-b-3-3]] (e),
valid there by [[lem:s12-ks-domain]], makes dt_* timelike: g₀₀ < 0. The components of g_b in the frame dt_*, dx^i
do not depend on t_*, as t_* − t is a function of |x|. The inequality t_* ≤ t of [[lem:iii-b-3-7]] (a) is not claimed
on the collar, where ψ < 0.

*Decay.* Here ḡ is the Minkowski metric of [[sec:ii-b-1-1]] in t̄ := t_* + r, ḡ = −(dt_* + dr)² + dx², not
η = −dt² + dx². With t = t_* + ψ(|x|) ([[eq:iii-b-3-6]]),

    η − ḡ = −2(ψ′ − 1) dt_* dr + (1 − ψ′²) dr²,

and ψ′ − 1 = −8m₀|x|⁻² on {|x| ≥ 3R₁}, the same function for every b, so ψ′ − 1 and 1 − ψ′² lie in ρ²C^∞(X̄) there;
dr = x̂·dx with x̂ smooth on X̄ near ∂X. And g_b − η ∈ |x|⁻²C^∞ in the frame dt, dx^i, which differs from the frame
dt_*, dx^i by dt = dt_* + ψ′x̂·dx, smooth on X̄. Adding the two gives g_b − ḡ ∈ ρ²C^∞(X̄) in the frame dt_*, dx^i, and
smoothness in b is that of [[prop:iii-b-3-6]]. ∎

### The horizon {#sec:vi-a-2}

With the radii of [[def:s12-radii]], let ℋ := {r = r_h}, ρ_∞ := |ξ|⁻¹ near N*ℋ, and ℛ_± := {r = r_h, η = 0, ±ξ > 0}.

**Proposition {#prop:vi-a-2-1}** ((H3) and (H4) at b₀.) With τ = t_*, (H3) holds at b₀ with
β₀ = f′(r_h) = 2m^(−1/2), β = 2/β₀ = m^(1/2), q_± := |η/ξ|²_g̸ restricted to ∂Σ₀, and c = β₀. (H4) holds with the
radii of [[def:s12-radii]].

*Proof.* By [[eq:vi-a-0-2]], G₀ = fξ² + r⁻²C does not depend on F. Its Hamilton vector field is

    H_(G₀) = 2fξ ∂_r − (f′ξ² − 2r⁻³C) ∂_ξ + r⁻² H^(𝕊³)_C,                                                {#eq:vi-a-2-1}

with H^(𝕊³)_C the geodesic spray of g̸, which preserves C. At fibre infinity, {G₀ = 0} requires f ≤ 0, and ξ ≠ 0
there. So ∂Σ₀ lies over {r ≤ r_h} ⊂ {r ≤ r_e}. It has the two components ±ξ > 0, it is invariant under the dilations,
and N*ℋ ∖ o ⊂ Σ₀. The future-directed rescaled field is 𝖧 := sgn(ξ) ρ_∞ H_(G₀): then 𝖧r = 2f < 0 for r < r_h, the
future direction decreasing r inside the horizon, as (H4) requires. On ∂ℛ_±,
𝖧ρ_∞ = sgn(ξ)|ξ|⁻¹(−f′ξ²) ∂_ξ|ξ|⁻¹ = f′|ξ|⁻¹, so β₀ = ρ_∞⁻¹𝖧ρ_∞ = f′(r_h) = 2m r_h⁻³ > 0. By [[eq:vi-a-0-2]],
τ₁ = −2ξ at r = r_h for every F, so ∓β₀⁻¹ρ_∞τ₁ = 2/β₀ on ∂ℛ_±, which gives β. On ∂Σ₀, |η/ξ|² = −fr², so
(ω, η̂ := η/ξ) are coordinates there with ∂ℛ_± = {η̂ = 0}, and q := |η̂|² is a quadratic defining function. As
H_(G₀)C = 0, [[eq:vi-a-2-1]] gives

    𝖧q = sgn(ξ)|ξ|⁻¹ · C · (−2ξ⁻³)(−f′ξ² + 2r⁻³C) = 2q (f′(r) − 2r⁻³q),

which is ≥ β₀q near ∂ℛ_±, where f′(r) → f′(r_h) and q → 0.

(H4): every maximal integral curve of 𝖧 in ∂Σ₀ ∖ ∂ℛ_± lies in {r < r_h}, where 𝖧r = 2f < 0. Backward, r increases,
is bounded by r_h, and converges to a zero of f, as ṙ = 2f; so r → r_h. On ∂Σ₀, q = −fr² → 0, so the curve tends to
∂ℛ_±. Forward, r decreases, and |ṙ| = 2|f(r(s))| ≥ 2|f(r(s₀))| > 0 for s ≥ s₀, as |f| increases as r decreases
below r_h; so the curve reaches {r < r₀ − δ₀} at a finite parameter. On {r₀ − 2δ₀ < r < r₂}, f < 0: G₀ = fξ² + r⁻²C
is Lorentzian of signature (1, 3), G₀(dr) = f < 0, and 𝖧r < 0 on ∂Σ₀. ∎

This is [Hin26c, Section 9.2.1, (1)–(4)] for Tangherlini. At b₀ the flow on ∂ℛ_± is the fibre dilation alone; at
b ≠ b₀ the Killing field normal to the horizon is not ∂_t, the flow on N*ℋ moves the base point, and (H3), which asks
only for an invariant source set with the stated rates, is proved by perturbation in [[sec:vi-b-2]].
