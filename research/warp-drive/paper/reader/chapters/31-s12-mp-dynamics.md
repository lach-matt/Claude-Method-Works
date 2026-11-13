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
For c ∈ [0, 1] let g_c := η + cH_(m,A) k_A ⊗ k_A. As k_A is null for η ([[lem:iii-b-3-3]] (a)), the argument of
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

    G^s := fξ² + r⁻²C − f⁻¹,                                                                      {#eq:s12-static-symbol}

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
field V, d(Vφ)_p = dφ_p ∘ DV_p. Here dφ_(s/u) = dξ ± ν dr at p, as f(r_ph) = ½ and (r − r_ph) vanishes at p.
The linearisation maps (δr, δξ) to (δξ, ν²δr), as 16r_ph⁻² = ν², and dξ ± ν dr applied to (δξ, ν²δr) gives
ν²δr ± νδξ = ±ν(δξ ± νδr). On Σ₁, ∂_ξC = −2r²fξ = 0 and
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

*Proof.* On {|x| ≤ 2R₁}, T_m of [[eq:iii-b-3-3]] is constant, so g_b is g^KS_b in a translated time coordinate, and r₀ −
2δ₀ ≥ ½r_♭; so g_b is smooth and Lorentzian of signature (1, 4) there, smoothly in b, by [[lem:s12-ks-domain]]. On {|x|
≥ ½R₁}, [[prop:iii-b-3-6]] gives smoothness and g_b − η ∈ |x|⁻²C^∞, smoothly in b. *The time function.* In the
coordinates (t_KS, x) = Φ_m(t, x), t_* = t − ψ(|x|) has differential dt_KS − β d|x| with β := ψ′ − T_m′ = 1 −
χ_∞(ρ)(8m₀ρ⁻² − 2m(ρ² − m)⁻¹), ρ := |x| ([[eq:iii-b-3-3]], [[eq:iii-b-3-6]]). Off supp χ_∞, in particular on [r₀ − 2δ₀,
2R₁], β = 1. On supp χ_∞ ⊂ [2R₁, ∞), ρ² ≥ 4m₀ and m < 3m₀/2, so (8m₀ − 2m)ρ² − 8m₀m > 20m₀² − 12m₀² > 0, the bracket is
positive and β < 1; and β ≥ 1 − 8m₀ρ⁻² ≥ −1, with equality only at ρ = 2R₁, where χ_∞ = 0. So β ∈ (−1, 1] on [r₀ − 2δ₀,
∞), as in the proof of [[lem:iii-b-3-7]] (a), and [[lem:iii-b-3-3]] (e), valid there by [[lem:s12-ks-domain]], makes
dt_* timelike: g₀₀ < 0. The components of g_b in the frame dt_*, dx^i do not depend on t_*, as t_* − t is a function of
|x|. The inequality t_* ≤ t of [[lem:iii-b-3-7]] (a) is not claimed on the collar, where ψ < 0.

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
only for invariant radial sets with the stated rates, is proved by perturbation in [[sec:vi-b-2]].

### The trapped set {#sec:vi-a-3}

On {r > r_h} we use static variables ([[lem:vi-a-0-1]]). Put u(r) := 1 − 2m r⁻² and, near Γ and on
Σ^s := {G^s = 0},

    φ₁ := fξ − u,     φ₂ := fξ + u,     Γ := {r = r_ph, ξ = 0} ∩ Σ^s = {r = r_ph, ξ = 0, C = 4m}.          {#eq:vi-a-3-1}

**Proposition {#prop:vi-a-3-1}** ((Γ.1)–(Γ.3) at b₀.) For z₀ ∈ {1, −1}, with the future field 𝖧^♭ = z₀H_(G^s) on
Σ^s:

(a) Γ is compact and invariant, and it lies in T*{r₂ < r < ρ₁⁻¹} for the ρ₁ of (H2) provided ρ₁⁻¹ > r_ph = √2 R₁, as
holds for the operators used, whose (H2) is set on {r > 3R₁};

(b) on Σ^s near Γ, exactly,

    𝖧^♭φ₁ = −ν₁φ₁,     𝖧^♭φ₂ = ν₂φ₂,     ν_(1,2) = 2z₀(r⁴ ± ξ(r² − m)(r² − 2m)) / (r³(r² − m)),        {#eq:vi-a-3-2}

with ν₁ = ν₂ = 4z₀(2m)^(−1/2) on Γ;

(c) {φ₁, φ₂} = (2/m)^(1/2) > 0 on Γ, and dG^s ≠ 0 there.

So (Γ.1)–(Γ.3) hold. For z₀ = 1 take φ_u := φ₁ and φ_s := φ₂; for z₀ = −1 take φ_u := φ₂ and φ_s := −φ₁. Then
ν_min = 4(2m)^(−1/2) for both signs, and Γ_(u/s) = {φ_(u/s) = 0} ∩ Σ^s are the two branches of {C = 4m} ∩ Σ^s.

*Proof.* On Σ^s, C = r²(f⁻¹ − fξ²), so (fξ)² = 1 − CW with W := f r⁻² and C conserved, and W′ = 2(2m − r²) r⁻⁵
([[prop:np-10-19-iv]]). W has the single critical point r_ph on (r_h, ∞), a maximum W = (4m)⁻¹.

(a) 𝖧^♭r = 2z₀fξ vanishes on Γ, and 𝖧^♭ξ = −z₀∂_rG^s = −z₀(f′f⁻² + f′ξ² − 2C r⁻³) vanishes there by
[[prop:np-10-19-ii]] (a). C and the flow on 𝕊³ preserve Γ, and Γ ≅ {(ω, η) : |η|² = 4m} is compact. Finally
r₂ = 7R₁/8 < r_ph.

(b) On Σ^s, (fξ)² = 1 − CW, and 1 − 4mW = 1 − 4m r⁻² + 4m² r⁻⁴ = u². So (fξ)² − u² = (4m − C)W, and
{φ₁φ₂ = 0} ∩ Σ^s = {C = 4m} ∩ Σ^s. Each branch is a union of orbits, by the identities derived next. Write X := fξ
and H := H_(G^s), with Hr = 2fξ and Hξ = −∂_rG^s. Then

    H(fξ) = 2ff′ξ² − f(f′ξ² − 2C r⁻³ + f′f⁻²) = ff′ξ² + 2fC r⁻³ − f′f⁻¹,

and on Σ^s, 2fC r⁻³ = 2r⁻¹(1 − f²ξ²). Since f′ − 2f r⁻¹ = (4m − 2r²) r⁻³ = −2u r⁻¹ and
2r⁻¹ − f′f⁻¹ = 2(r²f − m)/(r³f) = 2u (rf)⁻¹ (as r²f = r² − m), this gives H(fξ) = 2u (rf)⁻¹(1 − X²). Moreover
1 − u² = (1 − u)(1 + u) = 4m f r⁻², and Hu = u′·2fξ = 8m r⁻³X. Hence

    H(fξ) = 8m u r⁻³ − 2u (rf)⁻¹ (X − u)(X + u),
    Hφ₁ = H(fξ) − Hu = −(X − u) (8m r⁻³ + 2u (rf)⁻¹ (X + u)),
    Hφ₂ = H(fξ) + Hu = (X + u) (8m r⁻³ − 2u (rf)⁻¹ (X − u)).

With rf = (r² − m) r⁻¹ and u = (r² − 2m) r⁻²,

    8m r⁻³ + 2u² (rf)⁻¹ = 2((r² − 2m)² + 4m(r² − m)) / (r³(r² − m)) = 2r⁴ / (r³(r² − m)),
    2u (rf)⁻¹ · fξ = 2uξ r⁻¹ = 2ξ(r² − m)(r² − 2m) / (r³(r² − m)),

so the two brackets are ν₁/z₀ and ν₂/z₀ of [[eq:vi-a-3-2]]. Multiplying by z₀ gives [[eq:vi-a-3-2]] on Σ^s. On Γ,
ξ = 0 and r² = 2m, so ν₁ = ν₂ = 2z₀ r_ph (r_ph² − m)⁻¹ = 2z₀(2m)^(1/2) m⁻¹ = 4z₀(2m)^(−1/2), the rate of
[[prop:np-10-19-ii]] (b).

(c) {φ₁, φ₂} = ∂_ξφ₁ ∂_rφ₂ − ∂_rφ₁ ∂_ξφ₂ = f(f′ξ + u′) − (f′ξ − u′)f = 2fu′, which at r_ph is
2·½·4m r_ph⁻³ = (2/m)^(1/2). ∂_η G^s = 2r⁻²η^♯ ≠ 0, as |η|² = 4m. For z₀ = −1 the roles of φ₁ and φ₂ are exchanged,
and the sign of φ_s restores {φ_u, φ_s} = {φ₂, −φ₁} = {φ₁, φ₂} > 0 without changing (Γ.2). (Γ.1): φ₁ and φ₂ are
functions of (r, ξ) with dφ₁ ∧ dφ₂ = −2fu′ dr ∧ dξ ≠ 0 (u′ = 4m r⁻³), while on Γ, ∂_rG^s = ∂_ξG^s = 0, so dG^s ≠ 0
has no dr or dξ component there. So dφ₁, dφ₂ and dG^s are independent along Γ, and Γ_u, Γ_s are smooth hypersurfaces
of Σ^s near Γ, meeting transversally in Γ, to which 𝖧^♭ is tangent by [[eq:vi-a-3-2]]. Γ, Γ_(u/s), the flow and
(Γ.1)–(Γ.3) transfer to t_* by [[lem:vi-a-0-1]] (a)–(b), and the function q of (Γ.4) on Γ by [[lem:vi-a-0-1]] (c). ∎

This is [Hin26c, (Γ.1)–(Γ.3)] for Tangherlini; for Kerr it is [Hin26c, Lemma 4.16].

### r-normal hyperbolicity {#sec:vi-a-4}

**Proposition {#prop:vi-a-4-1}** ((K3) at b₀.) (K3) holds at b₀: Γ is eventually absolutely r-normally hyperbolic for
every r, for 𝖵 := q_(*,1)⁻¹ H_(G₁) on Σ^♭₁, with q_(*,1) and G₁ those of t_*.

*Proof.* First take the field of the static time, 𝖵_s := q_(s,1)⁻¹ H_(G^s), in static variables
([[lem:vi-a-0-1]] (a)). Here q_(s,1) = 2f⁻¹, so 𝖵_s = (f/2) H_(G^s), and on Γ, 𝖵_s = ¼H_(G^s), as f(r_ph) = ½. Use the
coordinates (r, ξ, ω, η) on Σ^s, where C is determined by (r, ξ). On Γ the flow is ṙ = ξ̇ = 0, and (ω, η) moves by
¼r_ph⁻² H^(𝕊³)_C, the geodesic flow of the round 𝕊³ on the cosphere bundle {|η|² = 4m}, reparametrised by a constant.
Its orbits are periodic, so De^(s𝖵_s)|_(TΓ) is bounded uniformly in s, and the tangential bound of (K3) holds with
C_ϵ = C for every ϵ > 0. Normal directions: the linearisation of 𝖵_s at Γ is block triangular. The (δr, δξ)-block is
autonomous, with eigenvalues ±¼ν, ν = 4(2m)^(−1/2), by [[eq:vi-a-3-2]] at z₀ = 1: on ker dφ₂, tangent to Γ_s, dφ₁
decays forward at the rate ¼ν, and on ker dφ₁, tangent to Γ_u, dφ₂ decays backward. The (δω, δη)-block is driven by
(δr, δξ), through r and C, which enter the speed of the spray. As the homogeneous tangential solutions are bounded and
the normal ones grow or decay at the rate ¼ν ≠ 0, each normal eigensolution e^(±νs/4)v_± has a unique tangential
correction e^(±νs/4)w_±, obtained by solving the driven equation with the variation-of-constants integral over
(−∞, s] or [s, ∞). This gives the invariant splitting [[eq:ii-b-1-1]], with N̄^u and N̄^s spanned by these solutions,
continuous along Γ, and the rate μ = ¼ν of (K3).

*Transport by T_F.* Transported by T_F ([[lem:vi-a-0-1]] (a)), 𝖵 = a𝖵_s with a := q_(s,1)/q_(*,1), smooth and positive
near Γ, as both time differentials are timelike there, and a = 1 on Γ by [[lem:vi-a-0-1]] (c). Hence e^(s𝖵) = e^(s𝖵_s)
on the invariant set Γ, and along Γ, D(a𝖵_s) = D𝖵_s + 𝖵_s ⊗ da. Here 𝖵_s is tangent to Γ and da vanishes on TΓ, so
the added term maps the normal directions into TΓ and annihilates TΓ. The normal block, its rates and the homogeneous
tangential equation are unchanged, and the added driving term is absorbed by the same variation-of-constants step. ∎

This is [Hin26c, Proposition 4.19] for Tangherlini.

### The global dynamics {#sec:vi-a-5}

On Σ^(z₀)_(z₀) the future integral curves of G_(z₀) project to future null geodesics of g_(b₀) with velocity
2z₀ν^♯, ν = −z₀ dτ + ζ, whose energy −g(2z₀ν^♯, ∂_t) = −2z₀ν(∂_t) = 2 is positive for both signs of z₀. On
Σ^(−z₀)_(z₀), which occurs only inside the horizon, the velocity is −2z₀ν^♯ and the energy −2, which is allowed there
since ∂_t is spacelike. C is the squared angular momentum. By [[lem:vi-a-0-1]] each statement below may be checked in
the time function named; ξ_s and ξ_* denote ξ in the t_s and in the t_* variables. Near infinity, t_* = t_s − F(r)
with F = t_s − t_* = r − r_* − T_m + ψ ([[eq:iii-b-3-3]], [[eq:iii-b-3-6]]), so that on {r ≥ 3R₁}

    F′ = 1 − f⁻¹ − T_m′ + ψ′ = 1 + m(r² − m)⁻¹ − 8m r⁻² = 1 + O(r⁻²),                                     {#eq:s12-shift}

and ξ_* = ξ_s − z₀F′ by [[lem:vi-a-0-1]] (a).

**Proposition {#prop:vi-a-5-1}** ((H8) at b₀.) (H8) (a) and (b) hold at b₀ for z₀ ∈ {1, −1}, with
Γ̄_u = {φ_u = 0} ∩ Σ^s ∩ {r > r_h}, Γ̄_s = {φ_s = 0} ∩ Σ^s ∩ {r > r_h}, and every neighbourhood O ⊂ {r > r_h} of Γ.

*Proof.* *Outside the horizon* (static variables). Along 𝖧^♭, ṙ = 2z₀fξ, C is conserved and (fξ)² = 1 − CW(r), so
the radial motion is that of a particle in the potential CW, which has a single maximum C/(4m) at r_ph and tends to 0
at r_h and at ∞ ([[prop:np-10-19-iv]]). There are three cases.

- C < 4m: fξ ≠ 0 throughout, so r is strictly monotone.
- C > 4m: {CW > 1} is an interval (r′, r″) ∋ r_ph with r_h < r′. A curve stays in (r_h, r′] or in [r″, ∞), with
  exactly one turning point, where ξ = 0 and ξ̇ ≠ 0.
- C = 4m: the curve lies on Γ or on one of the four branches of {fξ = ±u}, along which r is monotone and tends to r_ph
  at one end.

In the first two cases the curve meets neither Γ̄_u nor Γ̄_s, and r tends, at each end, to r_h or to ∞. In the third,
the branches with φ_u = 0 are backward asymptotic to Γ and those with φ_s = 0 are forward asymptotic, by
[[eq:vi-a-3-2]]. This identifies Γ̄_(u/s) outside the horizon. Inside the horizon no curve tends to Γ, as shown below.

*At infinity.* If r → ∞ forward, then (fξ_s)² → 1 and ṙ > 0 give ξ_s → z₀. By [[eq:s12-shift]], ξ_* → 0; and
|η|/r = C^(1/2) r⁻¹ → 0, as C is conserved. So the curve converges in the scattering phase space ([[sec:i-a-4]]) to
{ξ_* = 0, η = 0} over ∂X, which is R_out ([[eq:i-a-4-6]]). Backward with r → ∞, ξ_s → −z₀, so ξ_* → −2z₀ and
η/r → 0: the curve converges to R_(z₀,in) = {ξ_* = −2z₀, η = 0} over ∂X ([[eq:i-a-4-6]]).

*At the horizon* (v variables, regular across r = r_h; v is a chart, and the components are those of t_*,
[[sec:vi-a-0]]). On {G^(0)_(z₀) = 0}, fξ² − 2z₀ξ + r⁻²C = 0, with the roots ξ = (z₀ ± (1 − fC r⁻²)^(1/2))/f. One root
is regular at f = 0, where it tends to C/(2z₀r_h²); the other is ∼ 2z₀/f. A future null covector with
ν(∂_t) = −z₀ ≠ 0 is not a multiple of dr, so ν^♯ is not tangent to the null generator ∂_v of ℋ. At r = r_h,
g⁻¹(dr, ·) = ∂_v + f∂_r = ∂_v is future directed null ([[prop:np-10-19-iv]] (d)), so dr(γ̇) = g(∂_v, γ̇) < 0 for the
future causal velocity γ̇: on the regular root a curve crosses ℋ inward in finite parameter. Inside, dr is timelike
(G(dr) = f < 0) and ṙ < 0 strictly. On compact subsets of Σ_(z₀) ∩ {r₀ − δ₀ ≤ r ≤ r_h − ϵ}, compactified at fibre
infinity, ṙ is bounded above by a negative constant, including at fibre infinity by [[prop:vi-a-2-1]] (𝖧r = 2f). So
the curve reaches {r < r₀ − δ₀} in finite parameter. On the singular root, which near ℋ is the component
Σ^(−z₀)_(z₀) inside and the outgoing branch outside, |ξ| → ∞ as r → r_h with C fixed. So η/ξ → 0 and the curve tends
backward to ∂ℛ₊ ∪ ∂ℛ₋, reaching r_h only asymptotically in the parameter of the rescaled field, ρ_∞ times the future
field. For the unrescaled future field, |ṙ| → 2 and the curve reaches fibre infinity at a finite parameter; (H8) is
read for the rescaled field, whose integral curves are the same up to parametrisation.

So every curve not in Γ̄_u tends backward to ∂ℛ_± or R_(z₀,in), and every curve not in Γ̄_s tends forward to R_out or
reaches {r < r₀ − δ₀} in finite time.

*Uniformity on compact sets.* Let 𝖪 ⊂ Σ_(z₀) ∩ T*{r > r₀ − 2δ₀} be compact and disjoint from Γ̄_s. C is conserved,
and C ≤ C_𝖪 on 𝖪. For ϵ ∈ (0, ¼) and R large given C_𝖪, put 𝒜_out := {r > R, |ξ_*| < ϵ}. While z₀ξ_s > 0 and r > R:
𝖧^♭r = 2z₀fξ_s = 2(1 − Cf r⁻²)^(1/2) ≥ 1, and (fξ_s)² = 1 − Cf r⁻² gives z₀ξ_* = |ξ_s| − F′, hence
|ξ_*| ≤ c₁(C + 1) r⁻² and |η|/r = C^(1/2) r⁻¹, with c₁ depending only on m. Take R with c₁(C_𝖪 + 1) R⁻² < ϵ/2 and
F′ > ½ on {r > R}. A curve from 𝖪 that enters 𝒜_out has z₀ξ_s = z₀ξ_* + F′ > 0 there, and on the maximal parameter
interval after entry on which z₀ξ_s > 0, r increases (𝖧^♭r ≥ 1), so r > R persists and |ξ_*| < ϵ/2, hence
z₀ξ_s > ¼; that interval is therefore closed as well as open, and contains every later parameter. So the curve stays
in 𝒜_out, with r ≥ R + s at parameter s after entry, and converges to R_out at rates independent of its initial point.
For T > 0 let U_T be the set of points of 𝖪 whose forward curve enters 𝒜_out or {r < r₀ − δ₀} before parameter T. Each
U_T is open, as both target sets are open and the flow is continuous; the U_T increase with T; and they cover 𝖪 by the
pointwise statement, since a curve tending to R_out has r → ∞ and ξ_* → 0. So 𝖪 ⊂ U_T for one T, and the forward
convergence is uniform on 𝖪.

Backward, for 𝖪 disjoint from Γ̄_u, the same argument applies with 𝒜_in := {r > R, |ξ_* + 2z₀| < ϵ} for R_(z₀,in),
with R also so large that F′ < 3/2 on {r > R}: on 𝒜_in, z₀ξ_s = z₀(ξ_* + 2z₀) − 2 + F′ < −¼, and
|ξ_* + 2z₀| = ||ξ_s| − (2 − F′)| ≤ c₁(C + 1) r⁻²; and with 𝒰_H := {|r − r_h| < δ, ρ_∞ < δ′, C < C_𝖪 + 1} near the
horizon, where δ, δ′ are so small, given C_𝖪, that 𝒰_H meets only the singular root. 𝒰_H is backward invariant, as
|r − r_h| decreases backward on both of its branches and ρ_∞ with it, and on 𝒰_H, ρ_∞ ≤ c|f| and
|η/ξ| ≤ c C_𝖪^(1/2)|f|. In the rescaled parameter, |dr/ds| = ρ_∞|ṙ| = |f|(1 + O(C_𝖪 f)) on 𝒰_H, and
|f| = β₀|r − r_h|(1 + O(r − r_h)), so |r − r_h| decays backward exponentially at a rate close to β₀, uniformly on 𝒰_H.
With the cover argument this makes the backward convergence to ∂ℛ_± and to R_(z₀,in) uniform on 𝖪.

(b) Γ̄_u is the union of Γ and the two branches of {φ_u = 0}, on each of which r is monotone. So
Γ̄_u ∩ O = {φ_u = 0} ∩ Σ^s ∩ O = Γ_u for every O ⊂ {r > r_h}, and likewise for Γ̄_s. ∎

This is [Hin26c, Proposition 4.24] and the paragraph after [Hin26c, (9.5)], for Tangherlini.

**Lemma {#lem:vi-a-5-2}** (An escape function.) On Σ^s, ℱ := (r² − 2m)ξ satisfies

    H_(G^s)ℱ = 2r(ξ²(r² − m)² + (r² − 2m)²) / (r² − m)²  ≥ 0,                                              {#eq:vi-a-5-1}

with equality exactly on Γ.

*Proof.* For ℱ = a(r)ξ, H_(G^s)ℱ = a′·2fξ·ξ − a(f′ξ² − 2C r⁻³ + f′f⁻²). On Σ^s, 2C r⁻³ = 2r⁻¹(f⁻¹ − fξ²), so

    H_(G^s)ℱ = ξ²(2fa′ − a(f′ + 2f r⁻¹)) + a f⁻¹(2r⁻¹ − f′f⁻¹).

Here f′ + 2f r⁻¹ = 2r⁻¹, so the first term is 2ξ² r⁻²((r² − m)a′ − ra), using r²f = r² − m; and
2r⁻¹ − f′f⁻¹ = 2u(rf)⁻¹ (proof of [[prop:vi-a-3-1]]), so the second is 2ua(rf²)⁻¹ = 2r(r² − 2m)(r² − m)⁻²a. At
a = r² − 2m, (r² − m)a′ − ra = 2r(r² − m) − r(r² − 2m) = r³, and [[eq:vi-a-5-1]] follows. It vanishes exactly when
ξ = 0 and r² = 2m, and on Σ^s these give C = r²f⁻¹ = 4m: the set Γ. ∎

[[lem:vi-a-5-2]] is not needed at b₀, where [[prop:vi-a-5-1]] uses the conserved C. At b ≠ b₀, where C is not
conserved, [[sec:vi-b1-4]] uses the separation of [[sec:vi-b1-0]] instead. Exactly, φ₂² − φ₁² = 4fξu, so
ℱ = (r²/(4f))(φ₂² − φ₁²); with the choices of [[prop:vi-a-3-1]], z₀ℱ = (r²/(4f))(φ_s² − φ_u²) for both signs of z₀,
while 𝖧^♭(z₀ℱ) = H_(G^s)ℱ ≥ 0.

### The theorem at b₀ {#sec:vi-a-6}

**Theorem {#thm:vi-a-6-1}** ((Dyn) at b₀.) For g_(b₀) with the time function t_* and the radii of [[def:s12-radii]]:
(H6) and (K1) hold ([[lem:vi-a-1-1]], for every b ∈ ℬ_♭); the dynamical parts of (H3) and all of (H4) hold
([[prop:vi-a-2-1]]); (Γ.1)–(Γ.3) hold with ν_min = 4(2m₀)^(−1/2) ([[prop:vi-a-3-1]]); on Γ, q_(z₀) is the same in t_*
as in t_s ([[lem:vi-a-0-1]] (c)), where it is 2z₀f(r_ph)⁻¹ = 4z₀, so q^Γ := z₀q_(z₀) = 4 on Γ and
β₀ = ½ min_Γ |q_(z₀)| = 2; (K3) holds ([[prop:vi-a-4-1]]); and (H8) holds ([[prop:vi-a-5-1]]). These hold for every
operator with principal symbol G Id.

*Proof.* Each item is the result cited for it. ∎

**Remark {#rem:s12-two-beta}** (Two constants named β₀.) The β₀ of (H3), f′(r_h) = 2m₀^(−1/2), is twice the surface
gravity; the β₀ of (Γ.4), ½ min_Γ |q_(z₀)| = 1/f(r_ph) = 2, belongs to the trapped set. They are different quantities,
named by the same letter in [[sec:i-a-1-3]] and [[sec:i-b-1-5]].

### The horizon near b₀ {#sec:vi-b-1}

This section and the next carry the horizon hypotheses, the dynamical parts of (H3) and all of (H4), from b₀ to every
b near b₀, uniformly in b as (H5) asks. (H6), (K1) and the first clause of (K4) hold for every b ∈ ℬ_♭ by
[[lem:vi-a-1-1]]. The one new fact is that the Myers–Perry horizon is the null hypersurface {r_A = r₊} of the
Kerr–Schild form ([[lem:vi-b-1-1]]); it is proved by an exact identity. The rest is continuity on compact sets, after a
diffeomorphism that fixes the horizon ([[lem:vi-b-1-2]]).

For b = (m, A) ∈ ℬ_♭ let s, p, r_A, P, 𝖬, ℓ_A, F_A and H_(m,A) be as in [[lem:iii-b-3-1]] and [[def:iii-b-3-2]].
In a frame in which A = aJ₁₂ + bJ₃₄ (here b is the second spin, not the parameter), P(r) = (r² + a²)(r² + b²), since
s = a² + b² and p² = a²b² ([[lem:iii-b-3-1]]). Let r₊(b) be the largest positive root of

    Δ_b(r) := P(r) − m r² = 0.                                                                             {#eq:vi-b-1-1}

At b₀, Δ_(b₀) = r²(r² − m₀), so r₊(b₀) = m₀^(1/2) = r_h, and ∂_rΔ_(b₀)(r_h) = 4r_h³ − 2m₀r_h = 2m₀^(3/2) ≠ 0. So r₊
is a simple root, smooth in b near b₀ by the implicit function theorem, as P depends on A only through s and p², which
are smooth functions of A ([[lem:iii-b-3-1]]); the other roots of Δ_b stay near 0 and −r_h.

**Lemma {#lem:s12-spheroidal}** (The spheroidal form of the radius.) Let A ∈ 𝔰𝔬(4), |x|² > s, r := r_A(x),
N := (r²I − A²)^(1/2), which is symmetric, positive definite and commutes with A, and ω := N⁻¹x. Then |ω| = 1, and
with

    ϱ² := r² + s + ωᵀA²ω                                                                                 {#eq:s12-varrho}

the following hold.

(a) P(r) · xᵀN⁻⁴x = ϱ², and ϱ² ≥ r² > 0.

(b) F_A = r² xᵀN⁻⁴x; so P(r)F_A = r²ϱ² and H_(m,A) = m/ϱ².

(c) The Euclidean gradient of r_A is ∇r_A = N⁻²x/(r xᵀN⁻⁴x), so |∇r_A|² = P(r)/(r²ϱ²), and ℓ_A(∇r_A) = 1.

(d) In a frame in which A = aJ₁₂ + bJ₃₄, and with ω = (sin ϑ e^(iφ), cos ϑ e^(iψ)) in ℂ² ≅ ℝ⁴,
x = ((r² + a²)^(1/2) sin ϑ e^(iφ), (r² + b²)^(1/2) cos ϑ e^(iψ)) and ϱ² = r² + a² cos²ϑ + b² sin²ϑ.

*Proof.* By [[lem:iii-b-3-1]] (a), (r²I − A²)𝖬(r) = P(r)I, so N⁻² = 𝖬(r)/P(r). Then
|ω|² = xᵀN⁻²x = xᵀ𝖬(r)x/P(r) = 1, as Q(r, x) = P(r) − xᵀ𝖬(r)x = 0 at r = r_A(x).
(a) xᵀN⁻⁴x = ωᵀN⁻²ω = ωᵀ𝖬(r)ω/P(r), and ωᵀ𝖬(r)ω = (r² + s)|ω|² + ωᵀA²ω = ϱ². In a frame,
sI + A² = diag(b², b², a², a²) ≥ 0, so ϱ² ≥ r².
(b) By [[def:iii-b-3-2]], F_A = 1 + xᵀA²𝖬²x/P² = 1 + xᵀA²N⁻⁴x = 1 + ωᵀA²N⁻²ω, as N commutes with A. So
F_A = ωᵀ(N² + A²)N⁻²ω = r² ωᵀN⁻²ω = r² xᵀN⁻⁴x, and P F_A = r²ϱ² by (a). Hence H_(m,A) = m r²/(P F_A) = m/ϱ².
(c) The function φ_A(r, x) := xᵀ(r²I − A²)⁻¹x − 1 = −Q(r, x)/P(r) has, for fixed x, the zeros of Q(·, x) in (0, ∞), so
r_A(x) is its only positive zero; and ∂_rφ_A = −2r xᵀ(r²I − A²)⁻²x < 0. By the implicit function theorem,
∇r_A = −∇_xφ_A/∂_rφ_A = N⁻²x/(r xᵀN⁻⁴x), and |∇r_A|² = 1/(r² xᵀN⁻⁴x) = P/(r²ϱ²) by (a). The coefficient vector of ℓ_A
is 𝖬(rI + A)x/P = N⁻²(rI + A)x, so

    ℓ_A(∇r_A) = xᵀ(rI − A)N⁻⁴x/(r xᵀN⁻⁴x) = 1,

since AN⁻⁴ is antisymmetric (A is antisymmetric and commutes with the symmetric N⁻⁴), so xᵀAN⁻⁴x = 0.
(d) In the frame, A² = −diag(a², a², b², b²), N = diag((r² + a²)^(1/2), (r² + a²)^(1/2), (r² + b²)^(1/2),
(r² + b²)^(1/2)), s = a² + b² and ωᵀA²ω = −a² sin²ϑ − b² cos²ϑ. ∎

**Lemma {#lem:vi-b-1-1}** (The horizon is null.) For b = (m, A) ∈ ℬ_♭, on {|x|² > s},

    (g^KS_(m,A))⁻¹(dr_A, dr_A) = Δ_b(r_A) / (r_A² ϱ²),                                                     {#eq:vi-b-1-2}

with ϱ² of [[eq:s12-varrho]]. Hence ℋ_b := {r_A = r₊(b)} is a smooth null hypersurface invariant under ∂_t. dr_A is
spacelike just outside it and timelike just inside, where Δ_b < 0.

*Proof.* By [[lem:iii-b-3-3]] (d), (g^KS_(m,A))⁻¹ = η⁻¹ − H_(m,A) k_A^♯ ⊗ k_A^♯ with k_A^♯ = −∂_t + ℓ_A^♯, ℓ_A^♯ the
Euclidean dual of ℓ_A. As r_A does not depend on t, dr_A(k_A^♯) = ℓ_A(∇r_A) = 1 by [[lem:s12-spheroidal]] (c), and
η⁻¹(dr_A, dr_A) = |∇r_A|². So, by [[lem:s12-spheroidal]] (b)–(c),

    (g^KS_(m,A))⁻¹(dr_A, dr_A) = |∇r_A|² − H_(m,A) = P/(r_A²ϱ²) − m/ϱ² = (P − m r_A²)/(r_A²ϱ²).

dr_A ≠ 0 everywhere by [[lem:s12-spheroidal]] (c), so ℋ_b is a smooth hypersurface; its conormal dr_A is null there, as
Δ_b(r₊) = 0, so ℋ_b is null. It is invariant under ∂_t, as g^KS_(m,A) has t-independent components and r_A does not
depend on t. Δ_b has a simple zero at its largest root r₊, so Δ_b > 0 on (r₊, ∞) and Δ_b < 0 just below r₊. ∎

[[eq:vi-b-1-2]] is the component g^(rr) of the Myers–Perry metric [MP86] in Boyer–Lindquist coordinates ([ER08]),
written in the Kerr–Schild coordinates of [[ch:s11]]; the radius r_A of the Kerr–Schild form is the Boyer–Lindquist
radius. Nothing below uses the Boyer–Lindquist form.

**Lemma {#lem:vi-b-1-2}** (Fixing the horizon.) There are ε_H > 0 and diffeomorphisms Ψ_b of {|x| ≥ r₀ − 2δ₀}, for
|b − b₀| < ε_H, smooth in (b, x), with Ψ_(b₀) = Id, Ψ_b = Id on {|x| ≤ 5R₁/8} and on {|x| ≥ 7R₁/4}, and
Ψ_b({|x| = r_h}) = ℋ_b. Its spacetime lift is (t, x) ↦ (t, Ψ_b(x)).

*Proof.* Let χ_H ∈ C_c^∞((5R₁/8, 7R₁/4)) equal 1 near [3R₁/4, 3R₁/2], an interval that contains r_h = R₁. Put

    r̃_b(x) := χ_H(|x|) (r_h/r₊(b)) r_A(x) + (1 − χ_H(|x|)) |x|.

Then r̃_(b₀) = |x|, as r_A = |x| at A = 0 ([[lem:iii-b-3-1]] (b)); r̃_b − |x| is supported in {|x| ∈ supp χ_H} and
tends to 0 in C^∞ as b → b₀; and ℋ_b = {r̃_b = r_h} near {|x| = r_h}. Define Ψ_b(x) := κ x̂, with κ = κ_b(x) > 0
solving r̃_b(κx̂) = |x|. As ∂_κ r̃_b(κx̂) = 1 + O(|b − b₀|), the map κ ↦ r̃_b(κx̂) is strictly increasing on
[r₀ − 2δ₀, ∞) and equal to κ off supp χ_H (in particular for κ ≤ 5R₁/8, which contains r₀ − 2δ₀, and for large κ),
so it is a bijection of [r₀ − 2δ₀, ∞); κ_b is defined globally and is smooth by the implicit function theorem, and
Ψ_b is a diffeomorphism. It is the identity where χ_H(|x|) = 0, and it maps {|x| = r_h} onto {r̃_b = r_h}, which is
ℋ_b: on {χ_H = 1}, {r̃_b = r_h} = {r_A = r₊}, and on the transition region, where
|x| ∈ (5R₁/8, 3R₁/4) ∪ (3R₁/2, 7R₁/4), r̃_b is C^∞-close to |x| and so differs from r_h = R₁. For b near b₀,
{r_A = r₊} lies in {χ_H = 1}, since r_A is close to |x| and r₊ to R₁. ∎

Where χ_H(|Ψ_b(x)|) = 1, in particular near {|x| = r_h}, the definition of Ψ_b gives Ψ_b^* r_A = (r₊(b)/r_h)|x|, so
Ψ_b^* dr_A = (r₊(b)/r_h) dr there.

Below, g̃_b := Ψ_b^* g_b, with the time function Ψ_b^* t_*; its differential Ψ_b^* dt_* is timelike for g̃_b. The
spectral families of g_b and g̃_b are conjugate: on the bundles of [[sec:i-a-1-2]], trivialised by dt_*, dx^i, pulling
back by Ψ_b conjugates each operator by the smooth bundle map B_b taking the frame Ψ_b^* dt_*, Ψ_b^* dx^i to dt_*,
dx^i, smooth in b, with B_(b₀) = Id. The hypotheses (H1)–(H8) and (K1)–(K4) are invariant under this conjugation. The
scalar principal symbol is preserved. With the transported fibre inner product h′ := |det DΨ_b| B_b^*(h ∘ Ψ_b)B_b,
under which the pull-back by Ψ_b followed by B_b⁻¹ is an isometry from L²(|dy|; h) to L²(|dx|; h′), y = Ψ_b(x), the
h′-imaginary part of the conjugated operator is the conjugate of Im_h P, exactly; without the Jacobian it would acquire
the term ½H_G log|det DΨ_b|. h′ is a fibre inner product as in [[sec:i-a-1-2]] (Hermitian, bounded above and below,
smooth in b), equal to h where Ψ_b = Id. So the subprincipal endomorphisms that enter the threshold of (H3) and
condition (Γ.4) ([[sec:i-a-1-4]], [[sec:i-b-1-5]]) are conjugate, with the same spectra and thresholds. Ψ_b is the
identity on {|x| ≤ 5R₁/8} and on {|x| ≥ 7R₁/4}, so the artificial boundary, the extendible and supported spaces there,
(H2), (K1) and the structure at infinity are untouched, and smoothness in b gives norms equivalent uniformly in b. The
conjugated family is Ψ_b^* of the family that [[ch:s13]], [[ch:s14]] and [[ch:s15]] build from g_b, gauge 1-forms
included; where those chapters evaluate a threshold at N*ℋ_b in the coordinates of g_b ([[lem:iii-d-5-1]]), that is
the threshold of the conjugated family at N*{r = r_h}. We write G̃_(0,b) and τ̃_(1,b) for the symbols of g̃_b, and keep
the radii of [[def:s12-radii]], ρ_∞ = |ξ|⁻¹ and ℛ_± = {r = r_h, η = 0, ±ξ > 0}, which are fixed sets, independent of b.

### (H3) and (H4) near b₀ {#sec:vi-b-2}

**Lemma {#lem:vi-b-2-1}** For |b − b₀| < ε_H, N*{r = r_h} ∖ o ⊂ {G̃_(0,b) = 0}, and H_(G̃_(0,b)) is tangent to it.

*Proof.* The change of time Φ_m of [[eq:iii-b-3-3]] fixes x, so g_b⁻¹(dr_A, dr_A) = (g^KS_b)⁻¹(dr_A, dr_A), which
vanishes on ℋ_b by [[lem:vi-b-1-1]]. By the remark after [[lem:vi-b-1-2]], for c ∈ ℝ, G̃_(0,b)(c dr) = c² g̃_b⁻¹(dr, dr)
= c²(r_h/r₊(b))² g_b⁻¹(dr_A, dr_A) ∘ Ψ_b = 0 on {r = r_h}. So the Lagrangian submanifold N*{r = r_h} lies in the level
set {G̃_(0,b) = 0}. For v tangent to it and Ω the symplectic form, Ω(H_(G̃_(0,b)), v) = dG̃_(0,b)(v) = 0, so
H_(G̃_(0,b)) lies in the symplectic orthogonal of the tangent space, which is the tangent space itself. ∎

**Proposition {#prop:vi-b-2-2}** ((H3) and (H4) near b₀.) There is ε₁ ∈ (0, ε_H] such that for |b − b₀| < ε₁, and so
on the compact ball |b − b₀| ≤ ½ε₁ (as (H5) asks for a compact parameter space), the dynamical conditions of (H3) and
all of (H4) hold for g̃_b with the radii of [[def:s12-radii]], the sets ℛ_±, ρ_∞, and q_(±,b) := |η/ξ|²_g̸ restricted
to ∂Σ̃_(0,b). Moreover β₀(b) ≥ ½β₀(b₀), β(b) ≥ ½β(b₀), 𝖧_b q_(±,b) ≥ ½β₀(b₀) q_(±,b) near ∂ℛ_±, and the lengths in
(H4) are bounded, all uniformly in b. So the uniformity of (H5) holds for these data.

*Proof.* All symbols depend smoothly on b with values in C^∞, as Ψ_b does. By the first step of (H4) below,
∂Σ̃_(0,b) lies over {r < r_h + ½δ₀}. At b₀, on ∂Σ₀ (over r ≤ r_h), C/ξ² = −fr² = m₀ − r² ≤ m₀ − (r₀ − 2δ₀)² < ∞ on
[r₀ − 2δ₀, r_h], so |ξ| ≥ c|ζ| there; by compactness of S*{r₀ − 2δ₀ ≤ r ≤ r_h + ½δ₀} this persists for b near b₀. So
ξ ≠ 0 on ∂Σ̃_(0,b), sgn ξ splits it into two open and closed parts, and ρ_∞ = |ξ|⁻¹ and the future-directed rescaled
field 𝖧_b := sgn(ξ) ρ_∞ H_(G̃_(0,b)) are defined on all of it.

*(H3).* By [[lem:vi-b-2-1]], ∂ℛ_± are invariant compact sets for every b. β₀(b) = ρ_∞⁻¹𝖧_bρ_∞ and
∓β₀⁻¹ρ_∞τ̃_(1,b) are continuous functions on the fixed compact set ∂ℛ_±, continuous in b, and their infima at b₀ are
2m₀^(−1/2) and m₀^(1/2) ([[prop:vi-a-2-1]]). So they are at least half of that for b near b₀. Next, dG̃_(0,b) ≠ 0 at
∂ℛ_± (at b₀, ∂_r(fξ²) ≠ 0 there), so near ∂ℛ_±, ∂Σ̃_(0,b) is a smooth hypersurface of S*X̃, a graph
r = r_b(ω, η̂) over the coordinates (ω, η̂ := η/ξ), smooth in b (implicit function theorem). In these coordinates
∂ℛ_± = {η̂ = 0} for every b, and q_(±,b) = |η̂|² is a quadratic defining function. 𝖧_b is tangent to {η̂ = 0}, so
𝖧_b q_(±,b) = Q_b(ω)(η̂, η̂) + O(|η̂|³), with the quadratic form Q_b continuous in b and the remainder uniform. At b₀,
Q_(b₀) = 2β₀(b₀)|η̂|² ([[prop:vi-a-2-1]]: 𝖧q = 2q(f′ − 2r⁻³q)). So Q_b ≥ (3/2)β₀(b₀)|η̂|² for b near b₀, and
𝖧_b q_(±,b) ≥ ½β₀(b₀) q_(±,b) on {q_(±,b) < ϵ_q} for a fixed ϵ_q > 0.

*(H4).* At b₀, ∂Σ₀ lies over {r ≤ r_h}, and G̃_(0,b₀) ≥ c > 0 on S*{r_h + ½δ₀ ≤ r ≤ ρ₁⁻¹}. On {r ≥ ρ₁⁻¹},
G̃_(0,b) is elliptic uniformly for b near b₀: at b₀ it is fξ² + r⁻²C, g_b − g_(b₀) is small in ρ²C^∞
([[eq:iii-b-3-5]]), and Ψ_b = Id there. So for b near b₀, ∂Σ̃_(0,b) lies over {r < r_h + ½δ₀} ⊂ {r ≤ r_e}. On
{r₀ − 2δ₀ ≤ r ≤ r₂} the conditions "G̃_(0,b) is Lorentzian of signature (1, 3)", "G̃_(0,b)(dr) < 0" and "𝖧_b r < 0 on
∂Σ̃_(0,b)" are strict and hold at b₀ on a compact set, so they persist. For the flow, let U := {q_(±,b) < ϵ_q} near
∂ℛ_±. At b₀, ∂Σ₀ ∖ U lies over {r ≤ r_h − d₁} for some d₁ > 0 (q = −fr² there), where 𝖧r = 2f ≤ −c′. By continuity,
for b near b₀, ∂Σ̃_(0,b) ∖ U lies over {r ≤ r_h − ½d₁}, where 𝖧_b r ≤ −½c′. Let γ be a maximal curve of 𝖧_b in
∂Σ̃_(0,b) ∖ ∂ℛ_±. In U, q_(±,b) grows forward at the rate ≥ ½β₀(b₀), so γ leaves U forward in finite time. Since
𝖧_b q_(±,b) ≥ ½β₀(b₀) q_(±,b) > 0 on the closure of U, in particular on {q_(±,b) = ϵ_q}, the complement of U in
∂Σ̃_(0,b) is forward invariant, and γ does not re-enter U. Outside U, r decreases at the rate ≥ ½c′, so γ reaches
{r < r₀ − δ₀} within the time 2(r_h − r₀ + 2δ₀)/c′ after leaving U. Backward, r increases outside U, so γ enters U in
finite time. In U, q_(±,b) decreases exponentially backward, so γ(s) → ∂ℛ_± as s → −∞. The times are bounded uniformly
in b on compact sets of initial points away from ∂ℛ_±. ∎

This is the non-degenerate radial point structure at the conormal bundle of the event horizon that
[Hin26, Remark 1.4 (b)] describes, for the Myers–Perry metrics near Tangherlini.

### Spheroidal coordinates and the separation {#sec:vi-b1-0}

This section and the next five prove the remaining dynamical hypotheses for g_b, b near b₀: the normally hyperbolic
trapping (Γ.1)–(Γ.3) of (H7), the r-normal hyperbolicity (K3) with the uniformity (K4), and the global dynamics (H8),
with the uniformity of (H5) extended to them ([[sec:i-b-1-5]]). With [[sec:vi-a-1]] ((H6), (K1), and (Dyn) at b₀) and
[[sec:vi-b-2]] ((H3)–(H4) near b₀) this completes (Dyn) near b₀ ([[thm:vi-b1-5-1]]).

*Notation.* In these sections b is the parameter and, in a frame, the second spin; Ψ is a momentum in a frame and Ψ_b
the diffeomorphism of [[lem:vi-b-1-2]]; β is the coefficient of [[lem:vi-b1-0-1]] (c) and β₀ the rate of (H3); ψ is an
azimuth; and ℛ_c, 𝒮 are the functions of [[lem:vi-b1-2-1]].

Let b = (m, A) with |b − b₀| small, and use the notation of [[ch:s11]]: s = −½ tr(A²), P(r) = r⁴ + sr² + p²,
Δ_b = P − m r², r_A, ℓ_A and H_(m,A) ([[lem:iii-b-3-1]], [[def:iii-b-3-2]]), and r₊(b), the largest root of Δ_b
([[eq:vi-b-1-1]]). On {|x| ≥ r₀ − 2δ₀}, which lies in {|x|² > s} by [[lem:s12-ks-domain]], write

    x = (r²I − A²)^(1/2) ω,     r > 0,     ω ∈ 𝕊³ ⊂ ℝ⁴.                                                   {#eq:vi-b1-0-1}

By [[lem:s12-spheroidal]], r = r_A(x) and ω = (r_A²I − A²)^(−1/2)x; conversely, for x given by [[eq:vi-b1-0-1]] with
|x|² > s, xᵀ(r²I − A²)⁻¹x = |ω|² = 1, so r is the unique positive zero of Q(·, x) ([[lem:iii-b-3-1]]), r = r_A(x). So
[[eq:vi-b1-0-1]] is a diffeomorphism (r, ω) ↦ x onto {|x|² > s}, smooth in A, with no frame chosen. Write
N := (r²I − A²)^(1/2). Differentiating N² = r²I − A², with N and ∂_rN commuting (both are functions of A²),
∂_rN = rN⁻¹; so dx = rN⁻¹ω dr + N dω, with ⟨rN⁻¹ω, N dω⟩ = r⟨ω, dω⟩ = 0 and |rN⁻¹ω|² = r² xᵀN⁻⁴x = r²ϱ²/P by
[[lem:s12-spheroidal]] (a). Hence

    |dx|² = (r²ϱ²/P) dr² + ⟨(r²I − A²) dω, dω⟩,     ϱ² = r² + s + ωᵀA²ω,

with ϱ² of [[eq:s12-varrho]]. Write a covector as ν = −E dt + p_r dr + η, η ∈ T*_ω𝕊³, with t the Kerr–Schild time,
|η|²_(𝕊³) its round norm and |η|²_(e,r) its norm for the second term of |dx|². Put Y_r := (r²I − A²)⁻¹A, which is
antisymmetric, so that Y_rω ∈ T_ω𝕊³; Ẽ := E + η(Y_rω); 𝒯 := |η|²_(𝕊³) − ϱ²|η|²_(e,r); and

    𝔄 := (P/r²) p_r² − r²E² − 𝒯 − m(Ẽ + p_r)²,     𝒦 := |η|²_(𝕊³) − (s + ωᵀA²ω) E².                       {#eq:vi-b1-0-2}

*A frame.* Rotating, A = aJ₁₂ + bJ₃₄ with J₁₂ = e₁e₂ᵀ − e₂e₁ᵀ and J₃₄ = e₃e₄ᵀ − e₄e₃ᵀ, and
ω = (sin ϑ e^(iφ), cos ϑ e^(iψ)). Put Φ := η(J₁₂ω) and Ψ := η(J₃₄ω), the generators of the two rotations; as
J₁₂ω = −∂_φ and J₃₄ω = −∂_ψ, they are minus the momenta conjugate to φ and ψ. Then ϱ² = r² + a² cos²ϑ + b² sin²ϑ and

    𝒦 = p_ϑ² + Φ²/sin²ϑ + Ψ²/cos²ϑ − (a² cos²ϑ + b² sin²ϑ) E²,     η(Y_rω) = aΦ/(r² + a²) + bΨ/(r² + b²),
    𝒯 = (a² − b²)(Φ²/(r² + a²) − Ψ²/(r² + b²)).                                                          {#eq:vi-b1-0-3}

So 𝔄 depends on (r, p_r, E, Φ, Ψ) only, and 𝒦 on (ϑ, p_ϑ, E, Φ, Ψ) only. The frame is used only to compute; every
statement below is about the frame-free functions [[eq:vi-b1-0-2]].

**Lemma {#lem:vi-b1-0-1}** (Separation.) On T*(ℝ_t × {|x| ≥ r₀ − 2δ₀}), with 𝒢 := 𝔄 + 𝒦 and g_b written in the
Kerr–Schild time t (that is, g^KS_b):

(a) ϱ² g_b⁻¹(ν, ν) = 𝒢.

(b) E, 𝒦 and, in any frame, Φ and Ψ are constant along the flow of H_𝒢, and they Poisson-commute with each other.

(c) 𝔄 = αp_r² + 2βp_r + γ with α := Δ_b/r², β := −mẼ and γ := −r²E² − 𝒯 − mẼ². With p̃ := αp_r + β and the
*radial function* ℛ := β² − α(γ + 𝒦), α𝒢 = p̃² − ℛ.

(d) H_𝒢 r = 2p̃ and H_𝒢 p̃ = ∂_rℛ + (α′/α)(p̃² − ℛ), where ∂_r is taken at fixed (ω, η). In a frame, ℛ, α, β and p̃
depend on (ω, η) only through (Φ, Ψ, 𝒦), and H_𝒢 f = 0 for every function f of (E, Φ, Ψ, 𝒦).

*Proof.* (a) By [[lem:iii-b-3-3]] (d), g_b⁻¹ = η_M⁻¹ − H_(m,A) k_A^♯ ⊗ k_A^♯ with η_M := −dt² + dx² the Minkowski
metric and k_A^♯ = −∂_t + ℓ_A^♯. From the formula for |dx|², η_M⁻¹(ν, ν) = −E² + (P/(r²ϱ²)) p_r² + |η|²_(e,r). The
coefficient vector of ℓ_A is N⁻²(rI + A)x = rN⁻²x + N⁻¹Aω ([[lem:s12-spheroidal]]). At fixed ω, ∂_r x = rN⁻¹ω = rN⁻²x,
and the vector N⁻¹Aω = N(Y_rω) is the image of Y_rω ∈ T_ω𝕊³ under (r, ω) ↦ x at fixed r. So ℓ_A^♯ = ∂_r + Y_rω in
the coordinates (r, ω), and ν(k_A^♯) = E + p_r + η(Y_rω) = Ẽ + p_r. By [[lem:s12-spheroidal]] (b), H_(m,A) = m/ϱ².
Hence

    ϱ² g_b⁻¹(ν, ν) = (P/r²) p_r² − ϱ²E² + ϱ²|η|²_(e,r) − m(Ẽ + p_r)²,

and ϱ²E² = r²E² + (s + ωᵀA²ω)E² and ϱ²|η|²_(e,r) = |η|²_(𝕊³) − 𝒯 give (a).

*The frame formulas [[eq:vi-b1-0-3]].* In the frame, r²I − A² = diag(r² + a², r² + a², r² + b², r² + b²) and
dω = (cos ϑ e^(iφ) dϑ + i sin ϑ e^(iφ) dφ, −sin ϑ e^(iψ) dϑ + i cos ϑ e^(iψ) dψ), so

    ⟨(r²I − A²) dω, dω⟩ = ϱ² dϑ² + (r² + a²) sin²ϑ dφ² + (r² + b²) cos²ϑ dψ²,

since (r² + a²) cos²ϑ + (r² + b²) sin²ϑ = ϱ². The round metric is dϑ² + sin²ϑ dφ² + cos²ϑ dψ². With p_φ = −Φ and
p_ψ = −Ψ, |η|²_(𝕊³) = p_ϑ² + Φ²/sin²ϑ + Ψ²/cos²ϑ and |η|²_(e,r) = p_ϑ²/ϱ² + Φ²/((r² + a²) sin²ϑ) +
Ψ²/((r² + b²) cos²ϑ). Writing ϱ² = r² + a² − (a² − b²) sin²ϑ in the second term and ϱ² = r² + b² + (a² − b²) cos²ϑ in
the third,

    ϱ²|η|²_(e,r) = |η|²_(𝕊³) − (a² − b²) Φ²/(r² + a²) + (a² − b²) Ψ²/(r² + b²),

which is the formula for 𝒯. Next, s + ωᵀA²ω = a² + b² − a² sin²ϑ − b² cos²ϑ = a² cos²ϑ + b² sin²ϑ gives 𝒦. Finally
(r²I − A²)⁻¹ is (r² + a²)⁻¹ on span(e₁, e₂) and (r² + b²)⁻¹ on span(e₃, e₄), which contain J₁₂ω and J₃₄ω, so
Y_rω = aJ₁₂ω/(r² + a²) + bJ₃₄ω/(r² + b²) and η(Y_rω) is as stated. The proof of (a) chose no frame; the frame enters
only these formulas.

(b) E is the momentum of the Killing field ∂_t. In a frame, where sin 2ϑ ≠ 0, the coordinates (t, r, ϑ, φ, ψ) and
their conjugate momenta (−E, p_r, p_ϑ, −Φ, −Ψ) are canonical, and by [[eq:vi-b1-0-3]] 𝔄 and 𝒦 share only the momenta
E, Φ, Ψ, whose coordinates t, φ, ψ appear in neither. So {𝔄, 𝒦} = 0, hence {𝒢, 𝒦} = 0, and E, Φ, Ψ Poisson-commute
with 𝔄, 𝒦 and with each other. These identities hold on a dense open set and so everywhere, by continuity; E and 𝒦 are
defined without a frame.

(c) is algebra: P/r² − m = Δ_b/r² = α, so 𝔄 = αp_r² − 2mẼp_r − r²E² − 𝒯 − mẼ², and
α𝔄 = (αp_r + β)² − β² + αγ. Adding α𝒦 gives α𝒢 = p̃² − ℛ.

(d) In a frame, 𝒦 does not involve (r, p_r), and α, β and p̃ are functions of (r, p_r, E, Φ, Ψ); so
H_𝒢 r = ∂_(p_r)𝒢 = ∂_(p_r)𝔄 = 2αp_r + 2β = 2p̃. Since E, Φ and Ψ are conserved, H_𝒢 p̃ = ∂_(p_r)𝒢 · ∂_r p̃ −
∂_r𝒢 · ∂_(p_r)p̃ = 2p̃ ∂_r p̃ − α ∂_r𝒢, with ∂_r at fixed (p_r, ϑ, p_ϑ, Φ, Ψ, E), that is at fixed (ω, η). From
𝒢 = α⁻¹(p̃² − ℛ), α∂_r𝒢 = −(α′/α)(p̃² − ℛ) + 2p̃ ∂_r p̃ − ∂_rℛ. Hence H_𝒢 p̃ = ∂_rℛ + (α′/α)(p̃² − ℛ). The last claim
is (b). ∎

So on the characteristic set Σ = {𝒢 = 0} over {r > r₊}, where α > 0, p̃² = ℛ(r), with ℛ evaluated at the constant
values of (E, Φ, Ψ, 𝒦) along the curve, and the pair (r, p̃) moves as a particle in the potential −ℛ:
H_𝒢 r = 2p̃, H_𝒢 p̃ = ∂_rℛ. For a covector ν = −z₀ dt + ζ as in [[sec:vi-a-0]], E = z₀; the Hamilton vector field of
G_(z₀) = ϱ⁻²𝒢 on Σ is ϱ⁻²H_𝒢, and the future field on Σ^±_(z₀) is ±ϱ⁻²H_𝒢. This is [Hin26c, (4.30)–(4.32)] and
Carter's constant, for Myers–Perry.

### The radial function {#sec:vi-b1-1}

Put Λ := 𝒦 + sE² = |η|²_(𝕊³) + E²|Aω|² ≥ |η|²_(𝕊³), using −ωᵀA²ω = |Aω|². In a frame, with u := r², the function
𝒫(u) := uPℛ is

    𝒫 = m(PE + aΦ(u + b²) + bΨ(u + a²))² + Δ_b(uPE² + (a² − b²)(Φ²(u + b²) − Ψ²(u + a²)) − 𝒦P),           {#eq:vi-b1-1-1}

a polynomial of degree 5 in u whose coefficients are polynomials in (m, a, b, E, Φ, Ψ, Λ). Indeed, with α = Δ_b/u,
β = −mẼ and m + Δ_b/u = P/u, ℛ = m²Ẽ² + (Δ_b/u)(uE² + 𝒯 + mẼ² − 𝒦) = mẼ²P/u + (Δ_b/u)(uE² + 𝒯 − 𝒦); and
P = (u + a²)(u + b²), so PẼ = PE + aΦ(u + b²) + bΨ(u + a²) and P𝒯 = (a² − b²)(Φ²(u + b²) − Ψ²(u + a²)), by
[[eq:vi-b1-0-3]]. Multiplying by uP gives [[eq:vi-b1-1-1]]; its terms have degrees at most 4, 5, 3 and 4 in u, the
coefficient of u⁵ is E², and 𝒦 = Λ − (a² + b²)E². Then 𝒬(w) := w⁵𝒫(w⁻¹) is a polynomial in w with 𝒬(0) = E², and at
A = 0, where P = u², Δ_b = u² − mu, Ẽ = E, 𝒯 = 0 and 𝒦 = Λ, 𝒫 = u⁵E² − Λu⁴ + mΛu³, so

    𝒬 = E² − Λw + mΛw².                                                                                   {#eq:vi-b1-1-2}

ℛ(r) = r⁸𝒬(r⁻²)/P(r), so ℛ and 𝒬(r⁻²) have the same sign and the same zeros, with multiplicity, as P > 0. ℛ and 𝒬 are
homogeneous of degree 2 in (E, Φ, Ψ, Λ^(1/2)), so their signs and zeros depend only on the normalised values in

    𝒩 := {(E, Φ, Ψ, Λ) : E² + Λ/m₀ = 1, (|Φ| + |Ψ|)² ≤ Λ},

a compact set. Every covector with E ≠ 0 (as in every use below, where E = z₀) has its normalised values in 𝒩:
by the Cauchy–Schwarz inequality, |η|²_(𝕊³) ≥ Φ²/sin²ϑ + Ψ²/cos²ϑ ≥ (|Φ| + |Ψ|)², and Λ ≥ |η|²_(𝕊³).

**Lemma {#lem:vi-b1-1-1}** (Convexity.) There is ε_R > 0 such that for |b − b₀| ≤ ε_R, in any frame, and every point
of 𝒩, on [0, 2/m₀]: if Λ ≥ m₀/6, then 𝒬″ ≥ m₀²/12; if Λ < m₀/6, then 𝒬 ≥ ½.

*Proof.* At A = 0 and |m − m₀| ≤ ½m₀, [[eq:vi-b1-1-2]] gives 𝒬″ = 2mΛ ≥ m₀²/6 when Λ ≥ m₀/6, and
𝒬 ≥ E² − Λ/(4m) ≥ 5/6 − 1/12 = 3/4 when Λ < m₀/6. The coefficients of 𝒬 at (m, A) minus those at (m, 0) are
polynomials in (m, a, b, E, Φ, Ψ, Λ) vanishing at a = b = 0, hence bounded by C‖A‖ on the compact set
𝒩 × {|m − m₀| ≤ ½m₀}, with C independent of the frame, as |a|, |b| ≤ ‖A‖. So the difference is at most C′‖A‖ in
C²([0, 2/m₀]), which is below min(m₀²/12, ¼) for ‖A‖ small. ∎

**Corollary {#cor:vi-b1-1-2}** (The radial structure.) Let ε_R also be so small that r₊(b)⁻² < 2/m₀, and let
|b − b₀| ≤ ε_R and E ≠ 0. Then on (r₊, ∞):

(a) ℛ > 0 near ∞, and {r > r₊ : ℛ(r) < 0} is an interval, possibly empty.

(b) A double zero r_c of ℛ in (r₊, ∞) has ∂_r²ℛ(r_c) > 0, and then ℛ > 0 on (r₊, ∞) ∖ {r_c}.

(c) For every δ > 0 there is ε(δ) ≤ ε_R such that for |b − b₀| ≤ ε(δ) every double zero has |r_c − (2m)^(1/2)| < δ and
|Λ − 4mE²| < δE².

*Proof.* In w = r⁻² ∈ (0, w₊), w₊ := r₊⁻², 𝒬(0) = E² > 0, and 𝒬 is either positive on [0, w₊] or strictly convex
there ([[lem:vi-b1-1-1]], after normalising). A strictly convex function is negative on an interval and has a double
zero only at its minimum, with 𝒬″ > 0; it is then positive elsewhere. As ℛ = r⁸𝒬(r⁻²)/P and dw/dr ≠ 0, this gives
(a) and (b), with ∂_r²ℛ(r_c) = (r_c⁸/P) 𝒬″(w_c)(dw/dr)² > 0, the other terms vanishing with 𝒬(w_c) and 𝒬′(w_c).
(c) Suppose b_n → b₀ and normalised double zeros (π_n, w_n) ∈ 𝒩 × [0, 2/m₀] have a limit (π, w). By continuity it is a
double zero of [[eq:vi-b1-1-2]] at m = m₀: E² − Λw(1 − m₀w) = 0 = −Λ(1 − 2m₀w). Λ = 0 would give E² = 1 and
𝒬(w) = 1, so w = 1/(2m₀) and Λ = 4m₀E². Compactness gives (c). ∎

This is [Hin26c, Lemmas 4.11–4.12] near b₀. [Hin26c, Lemma 4.12] proves its convexity for all subextremal Kerr metrics;
here the convexity of 𝒬 in w = r⁻² is proved by perturbation from [[eq:vi-b1-1-2]], which suffices near b₀.

### The trapped set near b₀ {#sec:vi-b1-2}

Fix z₀ ∈ {1, −1}, so E = z₀ and E² = 1. Let I_Γ := ((1.2m₀)^(1/2), (3m₀)^(1/2)), which contains r_ph = (2m₀)^(1/2)
and lies in (r_h, 7R₁/4), and 𝒲 := {(ω, η) ∈ T*𝕊³ : 3m₀ < |η|²_(𝕊³) < 5m₀}.

**Lemma {#lem:vi-b1-2-1}** (The critical radius.) There is ε_Γ ∈ (0, ε_R] such that for |b − b₀| < ε_Γ: ∂_r²ℛ > 0 on
Ī_Γ × 𝒲̄; ∂_rℛ(·; ω, η) has a unique zero r_c(ω, η) ∈ I_Γ; and with ℛ_c := ℛ(r_c) and 𝒮 := (ℛ − ℛ_c)/(r − r_c)², the
functions r_c, ℛ_c on 𝒲̄ and 𝒮 on Ī_Γ × 𝒲̄ are smooth in (b, ·), 𝒮 > 0, and dℛ_c ≠ 0 on
{ℛ_c = 0} ∩ 𝒲̄ ⊂ {3.5m₀ < |η|² < 4.5m₀}. In a frame they depend on (ω, η) only through (Φ, Ψ, 𝒦). At b₀, with
C = |η|²: r_c² = C/2, ℛ_c = C(m₀ − C/4) and 𝒮 = (r + r_c)².

*Proof.* At b₀, ℛ = r⁸𝒬(r⁻²)/r⁴ = r⁴ − C(r² − m₀) by [[eq:vi-b1-1-2]] with Λ = C, so ∂_rℛ = 2r(2r² − C) vanishes at
r² = C/2 ∈ (1.5m₀, 2.5m₀), and ∂_r²ℛ = 12r² − 2C ≥ 14.4m₀ − 10m₀ > 0 on Ī_Γ × 𝒲̄. Then ℛ_c = C(m₀ − C/4) vanishes on
𝒲̄ only at C = 4m₀, where dℛ_c = (m₀ − C/2) dC = −m₀ dC ≠ 0, and ℛ − ℛ_c = r⁴ − Cr² + C²/4 = (r² − C/2)², so
𝒮 = (r² − r_c²)²/(r − r_c)² = (r + r_c)². ℛ is smooth in (b, r, ω, η) and Ī_Γ × 𝒲̄ is compact, so ℛ_b → ℛ_(b₀) in C³
there. Hence for b near b₀, ∂_r²ℛ > 0, ∂_rℛ has exactly one zero in I_Γ, smooth in (b, ω, η) by the implicit function
theorem, and the statements on ℛ_c persist. 𝒮 = ∫₀¹ (1 − τ) ∂_r²ℛ(r_c + τ(r − r_c)) dτ is smooth and positive. The
frame statement holds because it holds for ℛ ([[lem:vi-b1-0-1]] (d)). ∎

On O := {(r, ω; p_r, η) : r ∈ I_Γ, (ω, η) ∈ 𝒲} define

    φ_± := p̃ ∓ (r − r_c)√𝒮,     T_Γ := ∂_r((r − r_c)√𝒮),     Γ_b := Σ_(z₀) ∩ {φ₊ = φ₋ = 0} ∩ O.         {#eq:vi-b1-2-1}

**Proposition {#prop:vi-b1-2-2}** ((Γ.1)–(Γ.3) near b₀.) Let |b − b₀| < ε_Γ. In the variables of the Kerr–Schild
time:

(a) Γ_b = {r = r_c, p̃ = 0, ℛ_c = 0} ∩ O. It is a compact submanifold of codimension 2 of Σ_(z₀), invariant under the
flow, and Γ_(b₀) is the set Γ of [[eq:vi-a-3-1]].

(b) On Σ_(z₀) ∩ O, φ₊φ₋ = ℛ_c, and the future field 𝖧 := z₀ϱ⁻²H_𝒢 satisfies

    𝖧φ₊ = −2z₀ϱ⁻²T_Γ φ₊,     𝖧φ₋ = 2z₀ϱ⁻²T_Γ φ₋,                                                         {#eq:vi-b1-2-2}

with T_Γ = √𝒮 > 0 on Γ_b.

(c) (Γ.1)–(Γ.3) hold with (φ_u, φ_s) := (φ₊, φ₋) for z₀ = 1 and (φ₋, −φ₊) for z₀ = −1, ν_u = ν_s = 2ϱ⁻²T_Γ, and
{φ_u, φ_s} = 2α√𝒮 > 0 on Γ_b. At b₀, ν_u = ν_s = 4(2m₀)^(−1/2) on Γ.

(d) The same holds for g̃_b with the time function Ψ_b^* t_*, after the fibre translation of [[lem:vi-a-0-1]] from t
to t_* and the cotangent lift of the diffeomorphism Ψ_b of [[lem:vi-b-1-2]]. All the data are smooth in b with values in
C^∞, Γ̃_b ⊂ T*{r₂ < r < ρ₁⁻¹}, and ν_min(b), β₀(b) := ½ min_(Γ̃_b) |q_(z₀)| and max_(Γ̃_b) |q^Γ − 4| tend to
4(2m₀)^(−1/2), 2 and 0 as b → b₀.

*Proof.* (a) φ₊ = φ₋ = 0 means p̃ = 0 and (r − r_c)√𝒮 = 0, so r = r_c; on Σ, [[lem:vi-b1-0-1]] (c) then gives
0 = p̃² − ℛ = −ℛ_c. Conversely, r = r_c, p̃ = 0 and ℛ_c = 0 give 𝒢 = α⁻¹(p̃² − ℛ) = 0. By [[lem:vi-b1-2-1]], (ω, η)
ranges over the compact set {ℛ_c = 0} ∩ 𝒲̄, which lies inside 𝒲, and (r, p_r) is a smooth function of (ω, η) on it
(r = r_c, p_r = −β/α). So Γ_b is compact, and it is smooth of codimension 2 in Σ by (c) below. It is invariant: on Γ_b,
H_𝒢 r = 2p̃ = 0 and H_𝒢 p̃ = ∂_rℛ(r_c) = 0, while r_c and ℛ_c are constant along the flow ([[lem:vi-b1-0-1]] (d)). At
b₀, p̃ = (r² − m₀)p_r − m₀E, and the static time t_s = t − F_s, F_s′ = m₀/(r² − m₀), moves p_r to ξ_s = p_r − z₀F_s′
([[lem:vi-a-0-1]] (a)). So p̃ = (r² − m₀)ξ_s, and {r = r_ph, p̃ = 0, C = 4m₀} is the set of [[eq:vi-a-3-1]].

(b) On Σ ∩ O, φ₊φ₋ = p̃² − (r − r_c)²𝒮 = ℛ − (r − r_c)²𝒮 = ℛ_c. By [[lem:vi-b1-0-1]] (d), on Σ: H_𝒢 r = 2p̃;
H_𝒢 p̃ = ∂_rℛ = 2(r − r_c)𝒮 + (r − r_c)²∂_r𝒮, as ℛ_c does not depend on r; and H_𝒢 annihilates r_c and ℛ_c and acts on
𝒮 through r only. Hence H_𝒢((r − r_c)√𝒮) = 2p̃ T_Γ. Since 2√𝒮 ∂_r√𝒮 = ∂_r𝒮,

    2(r − r_c)√𝒮 T_Γ = 2(r − r_c)𝒮 + (r − r_c)² ∂_r𝒮 = ∂_rℛ,

so H_𝒢 p̃ = 2(r − r_c)√𝒮 T_Γ, and H_𝒢φ_± = 2(r − r_c)√𝒮 T_Γ ∓ 2p̃ T_Γ = ∓2T_Γ(p̃ ∓ (r − r_c)√𝒮) = ∓2T_Γφ_±
exactly. Multiplying by z₀ϱ⁻² gives [[eq:vi-b1-2-2]]. On Γ_b, r = r_c, so T_Γ = √𝒮.

(c) (Γ.2) is [[eq:vi-b1-2-2]], the sign choices making φ_u decay and φ_s grow along 𝖧; ν_(u/s) are smooth and positive
near Γ_b. For (Γ.1) and (Γ.3): at Γ_b, d𝒢 = α⁻¹(2p̃ dp̃ − dℛ) = −α⁻¹dℛ_c, as p̃ = 0, ∂_rℛ = 0, and
d_((ω,η))ℛ = dℛ_c at r = r_c (since ∂_rℛ(r_c) = 0). So dG_(z₀) = ϱ⁻²d𝒢 ≠ 0. At Γ_b, dφ_± = dp̃ ∓ √𝒮(dr − dr_c). Of
the three covectors dφ₊, dφ₋, dℛ_c, only dp̃ has a dp_r component (it is α ≠ 0), only dr − dr_c has a dr component, and
dℛ_c ≠ 0 has neither; so they are independent. Hence Γ_u and Γ_s are smooth hypersurfaces of Σ near Γ_b, meeting
transversally in Γ_b, and 𝖧 is tangent to both by [[eq:vi-b1-2-2]]. For the bracket,
{φ₊, φ₋} = 2{p̃, (r − r_c)√𝒮}, which at r = r_c is 2√𝒮({p̃, r} − {p̃, r_c}) = 2α√𝒮. Here {p̃, r} = ∂_(p_r)p̃ = α,
and {p̃, r_c} = 0 because, in a frame, p̃ is a function of (r, p_r, Φ, Ψ) and r_c of (Φ, Ψ, 𝒦), which Poisson-commute
([[lem:vi-b1-0-1]] (b)). α > 0 on I_Γ, as I_Γ ⊂ (r₊, ∞). For z₀ = −1, {φ₋, −φ₊} = {φ₊, φ₋}. At b₀, ϱ² = r_ph² = 2m₀
and √𝒮 = 2r_ph on Γ, so ν = 4r_ph/(2m₀) = 4(2m₀)^(−1/2), the rate of [[prop:vi-a-3-1]].

(d) dt and dt_* are timelike for g_b ([[lem:iii-b-3-3]] (e) with β = 0, valid by [[lem:s12-ks-domain]], and
[[lem:vi-a-1-1]]). They are co-oriented: g_b⁻¹(dt, dt_*) cannot vanish where both are timelike, the region is
connected, and near infinity it is close to η_M⁻¹(dt, dt − d|x|) = −1. The difference t − t_* is a function of |x|
([[eq:iii-b-3-3]], [[eq:iii-b-3-6]]). So [[lem:vi-a-0-1]] (a)–(b) carries Γ_b, φ_(u/s), (Γ.1)–(Γ.3) and the future
field to t_*, and the cotangent lift of Ψ_b, a symplectomorphism intertwining the Hamilton vector fields, carries them
to g̃_b. Everything in [[eq:vi-b1-2-1]] is built from frame-free functions smooth in (b, ·), and so are the two maps.
At b₀, Γ ⊂ {r = r_ph} and r₂ < r_ph < 3R₁ = ρ₁⁻¹; by continuity Γ̃_b stays in T*{r₂ < r < ρ₁⁻¹}. q_(z₀) is continuous
in b and the point, and on Γ_(b₀) it is 4z₀ in t_* ([[thm:vi-a-6-1]]); so β₀(b) → 2 and q^Γ → 4 uniformly. In
particular, after shrinking O uniformly in b, z₀q_(z₀) > 0 on Σ_(z₀) ∩ O, so there Σ_(z₀) agrees with the set
Σ^♭_(z₀) = Σ^(z₀)_(z₀) = Σ_(z₀) ∩ {z₀q_(z₀) > 0} of (H7), and the Γ_(u/s) of [[eq:vi-b1-2-1]] are those of (H7). For
the continuity in b that (H5) asks, φ_(u/s) are taken on a fixed neighbourhood of Γ̃_(b₀) contained in the transported
O_b for every b near b₀. ∎

This is [Hin26c, Lemmas 4.14–4.18 and Definitions 4.13, 4.15, 4.17] for Myers–Perry near Tangherlini. The separation
gives the separatrices in closed form, smooth in b; the persistence of normally hyperbolic manifolds would give them
only in C^k for each k, on neighbourhoods shrinking with k.

### r-normal hyperbolicity near b₀ {#sec:vi-b1-3}

(K3) concerns z₀ = 1 and 𝖵 := q₁⁻¹H_(G₁) on Σ^♭₁ near Γ. Its tangential bound, for every ϵ > 0, is the substance;
[Hin26c, Proposition 4.19 (3)] proves it for Kerr from the integrable structure of the flow on the trapped set, and so
does this section, for the flow of 𝒦 on T*𝕊³. At b ≠ b₀ that flow is not periodic.

**Lemma {#lem:vi-b1-3-1}** (The flow on Γ_b.) Let |b − b₀| < ε_Γ and z₀ = 1. The projection
π : (r, ω; p_r, η) ↦ (ω, η) restricts to a diffeomorphism of Γ_b onto Γ^𝕊_b := {ℛ_c = 0} ∩ 𝒲, and
π_*(H_𝒢|_(Γ_b)) = H_𝔥 on Γ^𝕊_b, where 𝔥 := 𝒦 + 𝔄(r_c, p_r^c; ·) on 𝒲 and p_r^c := −β(r_c)/α(r_c). In a frame, 𝔥 is
a smooth function of (𝒦, Φ, Ψ), so H_𝔥 = c₀H_𝒦 + c₁H_Φ + c₂H_Ψ, with c₀, c₁, c₂ the partial derivatives of that
function, constant along each orbit.

*Proof.* The inverse is (ω, η) ↦ (r_c, ω; p_r^c, η) ([[prop:vi-b1-2-2]] (a)). The (ω, η)-components of
H_𝒢 = H_𝔄 + H_𝒦 are those of the Hamilton vector field on T*𝕊³ of 𝒦 + 𝔄(r, p_r; ·) with (r, p_r) frozen. This differs
from H_𝔥 by (∂_r𝔄)H_(r_c) + (∂_(p_r)𝔄)H_(p_r^c). On Γ_b, ∂_(p_r)𝔄 = 2p̃ = 0, and ∂_r𝔄 = −H_𝒢 p_r = 0, because
p_r = p_r^c there is a function of the conserved (Φ, Ψ, 𝒦) and Γ_b is invariant. In a frame, 𝔄(r, p_r; ·) depends on
(ω, η) through (Φ, Ψ), and r_c, p_r^c through (Φ, Ψ, 𝒦) ([[lem:vi-b1-2-1]]). The Hamilton vector fields of 𝒦, Φ and
Ψ commute ([[lem:vi-b1-0-1]] (b)), so the c_i are constant along orbits. ∎

Let 𝒴 := {(ω, η) : 3m₀ ≤ 𝒦 ≤ 5m₀} ⊂ T*𝕊³ (with E² = 1), compact and invariant under H_𝒦, H_Φ and H_Ψ; for b near b₀
it contains Γ^𝕊_b. Fix any Riemannian metric on T*𝕊³ for the norms.

**Lemma {#lem:vi-b1-3-2}** (The flow of 𝒦.) Let ‖A‖² ≤ m₀/100. For every p ∈ 𝒴 there is C_p with
|D_p e^(sH_𝒦) v| ≤ C_p(1 + |s|)|v| for all v and all s ∈ ℝ.

*Proof.* Work in a frame, with Π := (Π₀, Π₁, Π₂) := (𝒦, Φ, Ψ) and X₀ := H_𝒦, X₁ := H_Φ, X₂ := H_Ψ, which commute.
With Φ, Ψ fixed, write U(ϑ) := Φ²/sin²ϑ + Ψ²/cos²ϑ − a² + (a² − b²) sin²ϑ, so that 𝒦 = p_ϑ² + U (with E² = 1). Then

    U″ ≥ 2Φ²/sin²ϑ + 2Ψ²/cos²ϑ − 2|a² − b²|,                                                              {#eq:vi-b1-3-1}

since (sin⁻²ϑ)″ = 2 sin⁻²ϑ + 6 cos²ϑ sin⁻⁴ϑ ≥ 2 sin⁻²ϑ, (cos⁻²ϑ)″ = 2 cos⁻²ϑ + 6 sin²ϑ cos⁻⁴ϑ ≥ 2 cos⁻²ϑ, and
(sin²ϑ)″ = 2 cos 2ϑ ≥ −2. On 𝒴, wherever p_ϑ = 0, Φ²/sin²ϑ + Ψ²/cos²ϑ = 𝒦 + a² − (a² − b²) sin²ϑ ≥ 3m₀ − 2‖A‖², so
U″ ≥ 6m₀ − 6‖A‖² > 0 there.

*The singular set.* Let Z := {p ∈ 𝒴 : dΠ₀, dΠ₁, dΠ₂ are dependent at p}. Where sin 2ϑ ≠ 0, (ϑ, φ, ψ) and their momenta
are canonical coordinates, dΦ and dΨ are independent, and d𝒦 = 2p_ϑ dp_ϑ + U′ dϑ + (…) dΦ + (…) dΨ. So p ∈ Z there
if and only if p_ϑ = 0 = U′(ϑ). If Φ = 0, then U′ = 2 sin ϑ cos ϑ (Ψ²/cos⁴ϑ + a² − b²) > 0, since
Ψ²/cos⁴ϑ ≥ Ψ²/cos²ϑ ≥ 3m₀ − 2‖A‖² > |a² − b²| there; likewise for Ψ = 0. So these points of Z have ΦΨ ≠ 0 and lie on
Z₁ := {p_ϑ = 0, ϑ = ϑ₀(Φ, Ψ)}, ϑ₀ a critical point of U: a family of invariant 2-tori, one for each (Φ, Ψ) and ϑ₀.
Near ω₁ = 0 use y := ω₁ ∈ ℂ ≅ ℝ², ω = (y, (1 − |y|²)^(1/2) e^(iψ)), with momenta (η_y, η_ψ). The round metric is
|dy|² + (y·dy)²/(1 − |y|²) + (1 − |y|²) dψ², whose inverse on the y-block is I − yyᵀ, and |y| = sin ϑ; so

    𝒦 = |η_y|² − (y·η_y)² + η_ψ²/(1 − |y|²) − a² + (a² − b²)|y|²,                                         {#eq:vi-b1-3-2}

Ψ = −η_ψ and Φ = −(y₁η₂ − y₂η₁). At y = 0, dΦ = −(η₂ dy₁ − η₁ dy₂), dΨ = −dη_ψ and d𝒦 = 2η_y·dη_y + 2η_ψ dη_ψ. These
are independent if η_y ≠ 0. If η_y = 0, the point lies on Z₂ := {y = 0, η_y = 0}, a family of invariant circles, one
for each η_ψ (by [[eq:vi-b1-3-2]], ẏ = η̇_y = 0 there). The same holds near ω₂ = 0, with a, b and Φ, Ψ exchanged,
giving the family of circles Z₂′. So Z = Z₁ ∪ Z₂ ∪ Z₂′.

*The singular levels.* Every local maximum ϑ_m of U has U″(ϑ_m) ≤ 0. By [[eq:vi-b1-3-1]],
Φ²/sin²ϑ_m + Ψ²/cos²ϑ_m ≤ |a² − b²| there, so U(ϑ_m) ≤ 2‖A‖² < 3m₀. Hence for ΦΨ ≠ 0 and k ∈ [3m₀, 5m₀], {U ≤ k} is an
interval, as U → ∞ at both ends and every local maximum lies below k. If k = U(ϑ₀) is a critical value, then
U″(ϑ₀) > 0, ϑ₀ is the unique minimum, and Π⁻¹(Π(p)) for p ∈ Z₁ is the torus through p. For p ∈ Z₂,
Π(p) = (Ψ₀² − a², 0, Ψ₀). A point with Φ = 0, Ψ = Ψ₀ and ϑ > 0 has 𝒦 ≥ U(ϑ), and
U(ϑ) − (Ψ₀² − a²) = Ψ₀² tan²ϑ + (a² − b²) sin²ϑ > 0 because Ψ₀² ≥ 3m₀ − ‖A‖² > |a² − b²|. So Π⁻¹(Π(p)) is the circle
of Z₂ through p; likewise for Z₂′. Consequently every fibre of Π that meets Z lies in Z, and for p ∈ 𝒴 ∖ Z the
connected component L of Π⁻¹(Π(p)) ∩ 𝒴 containing p is compact and disjoint from Z.

*Regular orbits.* Let p ∉ Z and let V be a compact neighbourhood of L in 𝒴 ∖ Z. On V the X_i are independent and span
⋂_j ker dΠ_j: each X_i annihilates every Π_j, and both spaces have dimension 3. Let Y_i := Σ_j (𝔊⁻¹)_ij ∇Π_j, with
𝔊_ij := ⟨∇Π_i, ∇Π_j⟩, so that dΠ_j(Y_i) = δ_ij; the X_i and Y_i form a bounded frame on V. Since dΠ_k is closed and
X₀Π_k = 0, dΠ_k([X₀, Y_i]) = X₀(dΠ_k(Y_i)) − Y_i(X₀Π_k) = 0, so [X₀, Y_i] = Σ_j d_ij X_j with d_ij bounded on V. Let
q_s := e^(sX₀)p. Then De^(sX₀) X_i(p) = X_i(q_s), and W_i(s) := De^(−sX₀) Y_i(q_s) satisfies
W_i′ = Σ_j d_ij(q_s) X_j(p), so De^(sX₀) Y_i(p) = Y_i(q_s) − Σ_j c_ij(s) X_j(q_s) with
c_ij(s) = ∫₀^s d_ij(q_σ) dσ, |c_ij| ≤ C|s|. Hence |D_p e^(sX₀)| ≤ C_p(1 + |s|).

*The tori Z₁.* On Z₁, sin 2ϑ₀ ≠ 0. Along the orbit the linearised equations, in the canonical coordinates, are
δΦ̇ = δΨ̇ = 0 and

    d/ds (δϑ, δp_ϑ) = (2δp_ϑ, −U″(ϑ₀) δϑ − ∂_Φ U′ δΦ − ∂_Ψ U′ δΨ),

with constant coefficients, and δφ̇, δψ̇ linear in (δϑ, δΦ, δΨ) with constant coefficients. As U″(ϑ₀) > 0 the matrix
of the (δϑ, δp_ϑ)-system is invertible with imaginary eigenvalues, so (δϑ, δp_ϑ) is bounded and (δφ, δψ) grows at most
linearly. *The circles Z₂, Z₂′.* By [[eq:vi-b1-3-2]], the Hessian of 𝒦 at Z₂ has no terms mixing (y, η_y) with
(ψ, η_ψ), so the linearisation splits: δẏ = 2δη_y and δη̇_y = −2(Ψ₀² + a² − b²) δy, an oscillator since
Ψ₀² + a² − b² > 0; and δη̇_ψ = 0, δψ̇ = 2δη_ψ. So the growth is at most linear. ∎

The singular orbits are the 2-tori of Z₁ and the circles of Z₂ and Z₂′, where Kerr has its equatorial set; all are
elliptic near b₀.

**Lemma {#lem:vi-b1-3-3}** (Reparametrisation; compare [Hin26c, Lemma 4.20].) Let V₁ be a smooth vector field, a > 0
smooth, V₂ := aV₁, and let the V₂-orbit of p lie in a compact set on which a, 1/a, |da| ≤ c_a. If
|D_p e^(sV₁)| ≤ c(1 + |s|)^k for s ∈ ℝ, then |D_p e^(sV₂)| ≤ c′(1 + |s|)^(k+1).

*Proof.* e^(sV₂)p = e^(τ(s)V₁)p with τ′ = a(e^(sV₂)p), τ(0) = 0, so |τ| ≤ c_a|s|. Then
D_p e^(sV₂) = D_p e^(τV₁) + V₁ ⊗ D_pτ, and ∂_s D_pτ = da(D_p e^(τV₁)) + (V₁a) D_pτ. Along the orbit,
V₁a = ∂_s log a(e^(sV₂)p), so ∂_s(D_pτ/a) = da(D_p e^(τV₁))/a and
|D_pτ(s)| ≤ c_a³ ∫₀^(|s|) c(1 + c_aσ)^k dσ. As V₁ is bounded on the compact set, the bound follows. ∎

**Proposition {#prop:vi-b1-3-4}** ((K3) and (K4) near b₀.) There is ε_K ∈ (0, ε_Γ] such that for |b − b₀| ≤ ε_K, (K3)
holds for g̃_b with Ψ_b^* t_*, and the splitting [[eq:ii-b-1-1]] and the constants μ, C, C_ϵ can be chosen continuous in
b and uniform, as (K4) asks.

*Proof.* *Tangential bound.* By [[prop:vi-b1-2-2]] (d) it suffices to work in the Kerr–Schild variables of g_b. There,
on Σ^♭₁ near Γ_b, the field 𝖵 of t_*, transported by T_F, is aH_𝒢 with a := (ϱ²q_*)⁻¹, where q_* > 0 is the q₁ of t_*; a
is smooth and positive. Let p ∈ Γ_b. By [[lem:vi-b1-3-1]], e^(sH_𝒢)|_(Γ_b) is conjugate by π to e^(sH_𝔥) = e^(sc₀X₀)
e^(sc₁X₁) e^(sc₂X₂), the c_i being constant along the orbit. Differentiating, D_(πp) e^(sH_𝔥) = De^(sc₀X₀) De^(sc₁X₁)
De^(sc₂X₂) + s Σ_i X_i ⊗ dc_i. Here e^(tX₁) and e^(tX₂) are cotangent lifts of rotations of 𝕊³ (by the frame's J₁₂ and
J₃₄), with derivatives bounded uniformly in t on 𝒴. [[lem:vi-b1-3-2]] enters at the rotated point e^(sc₁X₁) e^(sc₂X₂)
πp; the rotations commute with X₀ and have derivatives bounded on 𝒴, so its constant there is at most C·C_(πp). Hence
|D_p e^(sH_𝒢)|_(TΓ_b)| ≤ C_p(1 + |s|)², and by [[lem:vi-b1-3-3]], |D_p e^(s𝖵)|_(TΓ_b)| ≤ C′_p(1 + |s|)³. Now let ϵ > 0.
Identify Γ_b with Γ_(b₀) smoothly in b by ι_b(ω, η) := (ω, κ_b(ω, η)η) on Γ^𝕊_(b₀), where κ_b, near 1, solves ℛ_c(ω,
κ_bη) = 0 with ℛ_c taken at b ([[lem:vi-b1-2-1]]: the radial derivative η·∂_ηℛ_c is −8m₀² ≠ 0 at b₀, from ℛ_c = C(m₀ −
C/4) at C = 4m₀), followed by π⁻¹. The set 𝒮_K := {(b, p) : |b − b₀| ≤ ε_K, p ∈ Γ_b} ≅ {|b − b₀| ≤ ε_K} × Γ_(b₀) is
compact. For each (b, p) ∈ 𝒮_K the polynomial bound gives T ≥ 1 with |D_p e^(±T𝖵_b)|_(TΓ_b)| ≤ e^(ϵT/2). By continuity
in (b, p), read through ι_b, the same T gives e^(ϵT) on a neighbourhood. Finitely many such neighbourhoods cover 𝒮_K,
with times T_j ≤ T_max. Composing the flow over successive times T_j chosen at the current point gives |D_p
e^(s𝖵_b)|_(TΓ_b)| ≤ C_ϵ e^(ϵ|s|) for all (b, p) ∈ 𝒮_K and s ∈ ℝ, with C_ϵ := sup{|De^(t𝖵_b)| : |t| ≤ T_max, (b, p) ∈
𝒮_K}.

*Splitting and normal rates.* On Γ_b, [[eq:vi-b1-2-2]] gives 𝖵φ_s = (ν_s/q₁)φ_s and 𝖵φ_u = −(ν_u/q₁)φ_u, so
dφ_s(De^(s𝖵)v) = Θ_s dφ_s(v) for v ∈ TΓ_u|_(Γ_b), with Θ_s := exp ∫₀^s (ν_s/q₁)(e^(σ𝖵)p) dσ ≥ e^(ν′s) for s ≥ 0.
Here ν′ := inf ν_s/q₁ > 0 is uniform in b. Fix ϵ := ν′/4. Let n_u be a smooth section of TΓ_u|_(Γ_b) with
dφ_s(n_u) = 1, which exists by transversality. Write De^(s𝖵) n_u(p) = Θ_s(p) n_u(e^(s𝖵)p) + w_s(p) with
w_s(p) ∈ TΓ_b. An invariant line N^u = span(n_u + h), h a section of TΓ_b, is a fixed point of
(𝒞_t h)(e^(t𝖵)p) := Θ_t(p)⁻¹(De^(t𝖵) h(p) + w_t(p)). For t so large that C_ϵ e^(ϵt) e^(−ν′t) ≤ ½, 𝒞_t is a
contraction on bounded continuous sections, uniformly in b. So h exists, is unique and continuous in (b, p), and
𝒞_s h = h for all s by uniqueness. On N^u, De^(s𝖵) is multiplication by Θ_s, so |De^(s𝖵)v| ≤ Ce^(−ν′|s|)|v| for
s ≤ 0. N^s ⊂ TΓ_s is the same with time reversed. TΓ_b, N^u and N^s span T_(Γ_b)Σ^♭₁: the dimensions are 5 + 1 + 1,
N^u ⊄ TΓ_s as dφ_s(n_u + h) = 1, and TΓ_u ∩ TΓ_s = TΓ_b. This is [[eq:ii-b-1-1]] with μ := ν′, continuous in b, with
uniform constants. ∎

This is [Hin26c, Proposition 4.19 and Lemma 4.20] for Myers–Perry near Tangherlini.

### The global dynamics near b₀ {#sec:vi-b1-4}

**Proposition {#prop:vi-b1-4-1}** ((H8) near b₀.) There is ε₈ ∈ (0, ε_K] such that for |b − b₀| ≤ ε₈ and
z₀ ∈ {1, −1}, (H8) (a) and (b) hold for g̃_b with Ψ_b^* t_*, the radii of [[def:s12-radii]] and the trapped set of
[[prop:vi-b1-2-2]], with Γ̄_(u/s) the global backward and forward trapped sets. The convergence in (a) is uniform on
compact sets of (b, initial point), as the extension of (H5) asks.

*Proof.* All the sets named in (H8) are carried by the cotangent lift of Ψ_b to the corresponding sets for g_b (∂ℛ_± to
the conormal of ℋ_b at fibre infinity), and Ψ_b is the identity on {|x| ≤ 5R₁/8} ⊃ {r < r₀ − δ₀} and on
{|x| ≥ 7R₁/4} ([[lem:vi-b-1-2]]; r₀ − δ₀ < r_♭ ≤ ½R₁). So it suffices to prove (H8) for g_b, where the separation
holds. The time function only translates fibres ([[lem:vi-a-0-1]]), so the projected curves, r, and the limits at fibre
infinity do not depend on it. Limits over ∂X are read in t_*. Write γ for a maximal integral curve of the future field
in Σ_(z₀) ∩ T*{r > r₀ − 2δ₀}, parametrised by the rescaled field near fibre infinity ([[sec:vi-a-5]]).

*Outside the horizon.* On {r_A > r₊}, (r, p̃) moves with p̃² = ℛ(r), ṙ = ±2ϱ⁻²p̃ and (p̃)˙ = ±ϱ⁻²∂_rℛ
([[lem:vi-b1-0-1]] (d)), the conserved values of (Φ, Ψ, 𝒦) fixed. By [[cor:vi-b1-1-2]], either ℛ has no double zero,
or it has exactly one, r_c, and then ℛ_c = 0. In the first case r is strictly monotone except at most at one simple
turning point, where p̃ = 0 ≠ ∂_rℛ. Indeed r cannot converge to a point r̄ > r₊: p̃² = ℛ(r̄) > 0 would keep |ṙ| bounded
below, and a simple zero is passed in finite time. So at each end r → r₊ or r → ∞, or the curve leaves {r_A > r₊}. In
the second case ℛ > 0 off r_c, the curve is Γ_b or lies on {φ₊φ₋ = 0}, and r is monotone, tending to r_c at one end
and to r₊ or ∞ at the other. By [[cor:vi-b1-1-2]] (c), with ε₈ ≤ ε(δ) for a δ that places r_c in I_Γ and (ω, η) in 𝒲
(|η|²_(𝕊³) = Λ − |Aω|²E²), and [[lem:vi-b1-2-1]] (uniqueness of r_c in I_Γ, with {ℛ_c = 0} ∩ 𝒲̄ ⊂ 𝒲), every double
zero lies in O, so these curves are exactly those through {φ_u = 0} ∩ Σ ∩ O (backward asymptotic to Γ_b) or
{φ_s = 0} ∩ Σ ∩ O (forward asymptotic), extended by the flow.

*At infinity.* As r → ∞, ℛ = r⁴E² + O(r²(1 + Λ)) and α = r² + O(1), so p_r = (p̃ − β)/α = sgn(p̃) + O((1 + Λ) r⁻²); and
r_A = |x|(1 + O(|x|⁻²)) ([[lem:iii-b-3-1]] (b)) gives ξ_t = p_r + O((1 + Λ^(1/2)) r⁻²) for the coefficient ξ_t of d|x|,
while |η|/r ≤ Λ^(1/2) r⁻¹. Forward with r → ∞, ṙ > 0 forces sgn p̃ = z₀, so ξ_t → z₀; and with t_* = t − F(|x|), F := t
− t_* a function of |x| with F′ = 1 + O(r⁻²) ([[eq:iii-b-3-3]], [[lem:iii-b-3-5]] (a), [[eq:iii-b-3-6]]), ξ_* = ξ_t −
z₀F′ → 0. Backward, ξ_* → −2z₀. The bounds are uniform for Λ ≤ Λ_𝖪, the bound of Λ on a compact set 𝖪 of initial points,
so the argument at infinity of [[prop:vi-a-5-1]] applies verbatim with C replaced by Λ. This gives convergence to R_out
and R_(z₀,in), and the absorbing sets 𝒜_out = {r > R, |ξ_*| < ϵ} and 𝒜_in = {r > R, |ξ_* + 2z₀| < ϵ}.

*Near the radial sets.* (H3), as proved in [[prop:vi-b-2-2]], gives 𝖧_b q ≥ ½β₀q on ∂Σ₀ ∩ {q < ϵ_q} near ∂ℛ_±
and ρ_∞⁻¹𝖧_bρ_∞ ≥ ½β₀ at ∂ℛ_±, with β₀ := β₀(b₀). By continuity there is a neighbourhood U_R of ∂ℛ_± in the
compactified Σ, with compact closure and the same for all b near b₀, on which 𝖧_b q ≥ ¼β₀q − cρ_∞ and
𝖧_bρ_∞ ≥ ¼β₀ρ_∞, with q extended as |η/ξ|². So L := q + (8c/β₀)ρ_∞ satisfies
𝖧_bL ≥ ¼β₀q + cρ_∞ ≥ ⅛β₀L on U_R. Shrinking it, take U_R with closure inside a neighbourhood with these properties, so
that what follows holds on the boundary of U_R too. L vanishes on ∂ℛ_± and is positive on the rest of U_R: ρ_∞ > 0 at
finite covectors, and at fibre infinity near ∂ℛ_±, q = |η̂|² vanishes only on ∂ℛ_± ([[prop:vi-b-2-2]]: there ∂Σ₀ is a
graph over (ω, η̂) and ∂ℛ_± = {η̂ = 0}). Fix 0 < δ_L < min L over the boundary of U_R, and let 𝒰_L := {L < δ_L} ∩ U_R,
an open neighbourhood of ∂ℛ_±. Backward along a curve in U_R, L does not increase; so a curve in 𝒰_L never reaches
{L ≥ δ_L}, which contains the boundary of U_R, and it stays in 𝒰_L backward, with L decaying backward exponentially at
the uniform rate ⅛β₀.

*At the horizon.* ℋ_b is a null hypersurface ([[lem:vi-b-1-1]]), and dr_A(w) < 0 for every future-directed causal w at
ℋ_b not tangent to its null generators. Indeed this set of w is connected, dr_A(w) vanishes on it only for w tangent to
the generators, and the sign is that at b₀ ([[sec:vi-a-5]]), by continuity. The velocity of γ is a nonzero multiple of
ν^♯, and ν^♯ tangent to a generator would make ν a multiple of dr_A, so ν(∂_t) = 0, against E = z₀. So a curve meeting
ℋ_b at a finite covector crosses it inward, transversally, and by continuity each finite covector p₀ over ℋ_b has
δ, T > 0 such that the curve through any point within δ of p₀ is in {r_A < r₊} a parameter T later and in
{r_A > r₊} a parameter T earlier. Let γ stay in {r_A > r₊} on a forward or a backward half-line, with r → r₊ along
it, and let 𝓛 be its limit set at that end, in the compactified characteristic set: compact, invariant, over ℋ_b, and
approached by γ. 𝓛 contains no finite covector p₀: γ comes within δ of p₀ arbitrarily far along the half-line, and is
then in {r_A < r₊} a parameter T later, still on the half-line. So 𝓛 ⊂ ∂Σ₀. A point of ∂Σ₀ ∖ ∂ℛ_± reaches
{r < r_h − d₁} forward in finite time ([[prop:vi-b-2-2]], (H4)), which an invariant set over ℋ_b cannot contain; so
𝓛 ⊂ ∂ℛ_±, and γ lies in 𝒰_L near that end. Forward this is impossible: L > 0 along γ does not decrease forward in
𝒰_L, so it cannot tend to 0. Hence an exterior curve with r → r₊ forward leaves {r_A > r₊}, so meets ℋ_b and crosses
it inward; one with r → r₊ backward tends backward to ∂ℛ_±. Inside, read for g̃_b (Ψ_b carries {r < r_h} to the inside
of ℋ_b, [[lem:vi-b-1-2]]): on {r₀ − 2δ₀ ≤ r < r_h}, dr is timelike ([[lem:vi-b-1-1]] and [[prop:vi-b-2-2]]), so r
decreases strictly along γ. On compact subsets of the compactified Σ_(z₀) ∩ {r₀ − δ₀ ≤ r ≤ r₁}, r₁ < r_h, the rescaled
ṙ is bounded above by a negative constant, so γ reaches {r < r₀ − δ₀} in finite time. Backward, r increases strictly
along an interior curve. If the curve meets ℋ_b backward, it crossed it inward there, and its earlier part is an
exterior curve, treated above. Otherwise, with s₀ a parameter at which γ is inside, r → r̄ ≤ r_h as s → −∞. The case
r̄ < r_h is impossible: on the compact part of the compactified Σ_(z₀) over
{r(γ(s₀)) ≤ r ≤ r̄} ⊂ {r₀ − 2δ₀ ≤ r < r_h}, where dr is timelike, the rescaled ṙ is at most a negative constant −c, so
r would exceed r̄ within the backward parameter (r̄ − r(γ(s₀)))/c. If r̄ = r_h, a finite covector p₀ in the backward
limit set is impossible, since γ would be outside ℋ_b a parameter T before passing within δ of p₀, still on the
backward half-line; so the limit set lies in ∂Σ₀ over ℋ_b, hence in ∂ℛ_± as above, and γ tends backward to ∂ℛ_±.

*(a).* Combining: a curve not in Γ̄_u tends backward to ∂ℛ_± or R_(z₀,in), and a curve not in Γ̄_s tends forward to
R_out or reaches {r < r₀ − δ₀} in finite time. *Uniformity.* With the absorbing sets 𝒜_out, 𝒜_in, 𝒰_L (in which L
decays backward at the uniform rate) and {r < r₀ − δ₀}, the cover argument of [[prop:vi-a-5-1]] applies on compact
subsets of {(b, p)}: the set of (b, p) whose curve enters the relevant absorbing set before parameter T is open and
increases with T, and these sets cover by the pointwise statement.

*(b).* Within O, a point with φ_u = 0 has ℛ_c = 0 and lies on the branch on which r → r_c and p̃ → 0 backward, so its
curve tends to Γ_b backward. A point with φ_s = 0 ≠ φ_u moves away from r_c backward, and a point with ℛ_c ≠ 0 has no
double zero. So Γ̄_u ∩ O = {φ_u = 0} ∩ Σ ∩ O = Γ_u, and likewise for Γ̄_s. ∎

This is [Hin26c, Proposition 4.24] for Myers–Perry near Tangherlini.

### The theorem near b₀ {#sec:vi-b1-5}

**Theorem {#thm:vi-b1-5-1}** ((Dyn) near b₀.) There is ε_VI > 0 such that on the compact parameter set
ℬ_VI := {|b − b₀| ≤ ε_VI}, the metrics g̃_b = Ψ_b^* g_b with the time function Ψ_b^* t_* and the radii of
[[def:s12-radii]] satisfy: the dynamical conditions of (H3), and (H4) ([[prop:vi-b-2-2]]); (H6) and (K1)
([[lem:vi-a-1-1]]); (Γ.1)–(Γ.3), with ν_min → 4(2m₀)^(−1/2), β₀ → 2 and q^Γ → 4 as b → b₀ ([[prop:vi-b1-2-2]]); (K3)
and (K4) ([[prop:vi-b1-3-4]]); and (H8) ([[prop:vi-b1-4-1]]). All the data depend continuously on b into C^∞, with the
constants uniform, as (H5), its extension in [[sec:i-b-1-5]], and (K4) ask. These hold for every operator with
principal symbol g̃_b⁻¹ ⊗ Id. The operator hypotheses, the threshold in (H3) and condition (Γ.4), are verified in
[[ch:s13]], [[ch:s14]] and [[ch:s15]], read through Ψ_b ([[sec:vi-b-1]]).

*Proof.* Take ε_VI := min(ε₁/2, ε₈), with ε₁ from [[prop:vi-b-2-2]] and ε₈ from [[prop:vi-b1-4-1]]; the results cited
hold on ℬ_VI. ∎

For every r_♭ ∈ (0, ½R₁], ε_VI may be taken so small that ℬ_VI ⊂ ℬ_♭; ε_VI and the constants of the theorem depend
on r_♭.
