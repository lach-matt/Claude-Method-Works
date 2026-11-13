## The augmented low-energy resolvent and 2-admissibility {#ch:s18}

This chapter proves two results on the linearised gauge-fixed Einstein operator L_b of [[ch:s15]], for Myers–Perry
parameters b near b_0. The first, in [[sec:iii-h-1]]–[[sec:iii-h-5]], is [Hin26, Section 10.1] (pp. 200–212) in
dimension 4 + 1. The spectral family L̂_b(σ) is augmented by the zero energy states of [[prop:iii-f3-4-1]], cut off near
future null infinity ℐ⁺. The Fourier transforms of the resulting forcing terms are described
([[lem:iii-h-2-2]]–[[lem:iii-h-2-5]]; [Hin26, Lemma 10.4 and (10.24)]), the augmented zero energy operator is invertible
([[prop:iii-h-3-2]]; [Hin26, Proposition 10.6]), the augmented operator satisfies estimates uniform as σ → 0
([[cor:iii-h-4-2]]; [Hin26, Proposition 10.7]), and the augmentation is built on the spectral side as well
([[sec:iii-h-5]]; [Hin26, Section 10.1.3]). The same analysis shows that L̂_b(σ) is invertible for 0 < |σ| < c_0 at
every b near b_0 ([[cor:iii-h-4-3]], [[cor:iii-h-4-4]]). This is the range of low frequencies that the perturbation
argument of [[prop:iii-f2-4-1]] does not reach for b ≠ b_0, and with it [Hin26, Proposition 8.8] holds in dimension
4 + 1 on a fixed neighbourhood of b_0.

The second result, in [[sec:iii-h1-1]]–[[sec:iii-h1-7]], is [Hin26, Theorem 10.1] (pp. 199–201), proved by the argument
of [Hin26, Section 10.2] (pp. 212–217). The forward solution of L_b u = f is a contour integral of L̂_b(σ)⁻¹
([[lem:iii-h1-2-1]]); it splits into high frequencies ([[lem:iii-h1-3-1]]), a regular low-frequency part
([[lem:iii-h1-4-1]]) and the contribution of the zero energy states ([[lem:iii-h1-5-1]]), and the last is controlled by
integrating twice in t_* ([[lem:iii-h1-6-2]]). The conclusion, [[thm:iii-h1-1-3]], is 2-admissibility with sf-weight
α_sf, α_sf + 2 ∈ (0, 1), margin 1 and sf-loss 0, for orders of a class 𝒪_c ([[def:iii-h1-1-1]]). It holds for every
k ∈ ℕ_0 at every b at which the trapped set satisfies a bound depending on k, and these bounds hold for every k on one
fixed neighbourhood of b_0 ([[rem:s18-every-k]]).

*Dimension 4 + 1.* In dimension 3 + 1 the mass and boost states decay like r⁻¹ and the naive columns [L_b, t_*]ġ^Υ_b
only like r⁻², which is not in the target space, so [Hin26] first improves its states at ι⁺ ([Hin26, Lemma 10.3], by
[Hin26, Proposition 9.11]). In dimension 4 + 1 the states decay one order faster ([[prop:iii-f3-4-1]]), the columns are
O(r⁻³) and lie in the target for every weight α with α + 2 ∈ (0, 1), and the states cut off near ℐ⁺ need no
correction. No logarithm enters, the cut-off forcing terms are supported in a cone inside ι⁺ ([[lem:iii-h-2-2]]), and
the window (0, ϵ_ind) of the weights of [Hin26] becomes (0, 1). [Hin26, Proposition 10.7] rests on [Hin26c, Theorem
9.41] with augmentation columns that depend on σ; [[thm:i-c-6-4]] allows only constant, compactly supported columns, and
[[thm:iii-h-4-1]] extends it. [Hin26, Lemma 10.5] (partial polyhomogeneity) is used in [Hin26] only in its Section 11.5
and is not needed here. In the proof of [Hin26, Theorem 10.1] in dimension 3 + 1, the derivatives ∂_(t_*)ġ and
∂²_(t_*)h_s1 of the contributions of the states have sf-weights −½ − ϵ and ½ − ϵ, and the two integrations in t_* end
at −3/2 − ϵ, below α_sf; this is the sf-loss δ > α_sf + 3/2 of [Hin26, Theorem 10.1]. In dimension 4 + 1 the
transforms of the cut-off states decay rapidly at scf ([[lem:iii-h-2-5]]), the derivatives have sf-weights below 0 and
1, which leaves room for α_sf + 1 and α_sf + 2, and the integrations return to α_sf itself ([[lem:iii-h1-5-1]] and
[[sec:iii-h1-7]]). No splitting at ℐ⁺ ([Hin26, (10.57)]) and no condition at the outgoing radial set ([Hin26, Remark
10.2], used in the proof of [Hin26, Lemma 10.12]) is needed. Several steps of [Hin26] need more than is stated there,
in dimension 3 + 1 as in 4 + 1; [[sec:s18-remarks]] collects them.

*The inner radius.* Every result of the chapter holds with the inner radius r_0 = r_♭ ∈ (0, ½R_1] of [[def:s12-radii]]
as a parameter, with constants that depend on it. The radius enters only through r ≥ r_0 > 0 on X, through the spaces,
which are extendible at {r = r_0}, through the radii of [[sec:i-a-1-1]] in (C2) of [[def:iii-h1-1-1]], and through the
constancy of the orders over {r ≤ r_0 + δ_1} and the extension across {r = r_0} in the proof of [[lem:iii-h1-6-2]].

*Notation.* The black-hole parameter is b = (m, A), with mass m, and b_0 = (m_0, 0). The letter h denotes a zero energy
state (h(S), h̆(S)) or, as an index (⟨·, ·⟩_h, h_Γ), a fibre inner product; the semiclassical parameter of [[ch:s02]]
is written |σ|⁻¹. Large exponents of decay are written M. The Fourier transform is (ℱu)(σ) := ∫ e^(iσt_*) u dt_*
([[eq:iii-a-2-2]]), under which ∂_(t_*) becomes −iσ.

### Setting {#sec:iii-h-1}

*Parameters.* They are those of [[sec:iii-f3-1]] and [[sec:iii-f4-1]]: b = (m, A) near b_0, the modification
parameters with (Dyn), (C1) and γ_Υ small, and a constant regularity s > ½ + ϑ_L ([[lem:iii-f2-1-1]]). The pairing is
⟨u, v⟩ := ∫_X ⟨u, v⟩_(g_b) |dx|. On X we write r := |x|, so r ≥ r_0 > 0, and ρ is the boundary defining function of
[[sec:i-c-6]], ρ = 1/r; [[sec:ii-g1-4-3]] uses ⟨x⟩⁻¹, which on {r ≥ 1} differs from 1/r by a smooth factor with values
in [2^(−1/2), 1].

*Weights.* All weights below are those of [[ch:s03]], defined with the density |dx| (the density |dg_b|_X| of [Hin26]):
H̄_b^(p,a) is the space of [[def:i-c-2-8]], and the b-weights of [[sec:iii-f3-1]], defined with the density
μ_b = |dx|/|x|⁴, are these plus 2. Thus 𝒜^q ⊂ H̄_b^(∞,a) near ∂X for a < q − 2. Here ∂X is the boundary at infinity
(ρ = 0) of X̄, and "smooth on X" says nothing at ∂X, where only conormality is claimed. Throughout,

    α ∈ ℝ,     α + 2 ∈ (0, 1),                                                                           {#eq:iii-h-1-1}

which is the weight α_sf of [Hin26] (in dimension 3 + 1, α_sf + 3/2 ∈ (0, ϵ_ind)). Then [[prop:iii-f3-4-1]] applies at
its b-weight α + 2 ∈ (0, 1]; L̂_b satisfies (G) of [[sec:i-c-1-2]] at the weight α, since α + 2 lies in the gap
(0, β^L_+) and β^L_+ > 1 ([[prop:iii-f1-2-3]]); it satisfies (TF) with the weight α + 2 ([[prop:iii-f1-3-3]]); and it
satisfies (H1)–(H5) of [[sec:i-a-1]], with index 0 at σ ≠ 0 ([[cor:iii-f2-1-2]]). The spaces 𝒳_σ, 𝒴_σ (σ ≠ 0), 𝒳_0,
𝒴_0, the norms ‖·‖_((s;k),(𝗋,l,q),ς) with ς = |σ| ([[def:i-c-6-1]]), the orders 𝗋 and α_+, and the cut-offs χ_zf,
χ_tf are those of [[sec:i-c-6]] for P̂ = L̂_b at the weight α. We put

    Σ_0 := {σ ∈ ℂ : 0 < |σ| ≤ 1, Im σ ≥ 0}.

*The operator.* By [[sec:iii-f4-2]], L_b = L_0 + L_1∂_(t_*) + L_2∂²_(t_*) with stationary operators L_j on X: on
stationary sections L_0 = L̂_b(0), L_1 = [L_b, t_*] and L_2 = ½[[L_b, t_*], t_*], and

    L̂_b(σ) = L_0 − iσL_1 − σ²L_2.

Near ∂X, L_0 ∈ ρ²Diff_b^2, L_1 ∈ ρ Diff_b^1 and L_2 ∈ ρ²C^∞ ([[eq:iii-g4-1-2]] and the proof of [[lem:iii-g4-1-2]],
which rest on [[lem:iii-f-2-1]]; [[eq:i-c-1-1]]). On compact subsets of X the L_j have smooth coefficients.

*The states.* Let 𝔟 := ℝ ⊕ 𝔰𝔬(4). For ḃ = (ṁ, Ȧ) ∈ 𝔟 put

    ġ(ḃ) := ṁ ġ^Υ_b(1, 0) + ġ^Υ_b(0, Ȧ),

with ġ^Υ_b of [[prop:iii-f3-2-2]], and for S ∈ 𝒮_1 let h(S) := h_(b,s1)(S) and h̆(S) := h̆^1_(b,s1)(S)
([[eq:iii-f3-4-2]]; [[prop:iii-d2-3-1]], which is [Hin26, Proposition 6.15] in dimension 4 + 1). These sections are
smooth on X and conormal at ∂X. Their weights (the largest q with the state in 𝒜^q) are 2 for ġ(1, 0), 3 for ġ(0, Ȧ),
3 for h(S) and 2 for h̆(S) ([[sec:iii-f4-1]]). The generalised state is

    h^(≤1)(S) := t_* h(S) + h̆(S) = δ*_(g_b)(t_* ω^(0)_(b,s1)(S) + ω̆^((0),1)_(b,s1)(S))

([[prop:iii-d2-3-1]]), where the 1-form lies in the kernel of □^Υ_b. Since D_(g_b)Ric ∘ δ*_(g_b) = 0 and
2δ_(g_b,E_Υ)G_(g_b)δ*_(g_b) = □^Υ_b (proof of [[prop:iii-f3-4-1]]), L_b h^(≤1)(S) = 0, that is,

    L_0 h(S) = 0,     L_1 h(S) + L_0 h̆(S) = 0,

as [[lem:iii-f4-3-1]] (3) uses. Likewise L_b ġ(ḃ) = L_0 ġ(ḃ) = 0.

*Cut-offs.* Fix χ_c ∈ C^∞(ℝ) equal to 1 on (−∞, ¼] and to 0 on [½, ∞), and χ_+ ∈ C^∞(ℝ) equal to 0 on (−∞, 1] and
to 1 on [2, ∞), and put

    χ_K(t_*, x) := χ_+(t_*) χ_c(|x|/t_*)  (t_* > 0),          χ_K := 0  (t_* ≤ 0).                    {#eq:iii-h-1-2}

Then χ_K is smooth on ℝ × X. It vanishes for t_* ≤ 1 and for |x| ≥ t_*/2, so near ℐ⁺, where |x|/t_* → ∞; and it
equals 1 on {t_* ≥ 2, |x| ≤ t_*/4}, so near K⁺. These are the properties [Hin26, p. 203] asks of its χ_K. For
|x| ≥ 1, χ_K(t_*, x) = χ_c(|x|/t_*) for all t_* > 0, as both sides vanish for t_* ≤ 2|x|.

### The cut-off states and their Fourier transforms {#sec:iii-h-2}

This section is [Hin26, Lemma 10.4 and (10.24)] in dimension 4 + 1.

**Definition {#def:iii-h-2-1}** (The cut-off states.) For ḃ ∈ 𝔟 and S ∈ 𝒮_1 put

    ġ^aug(ḃ) := χ_K ġ(ḃ),     h^aug(S) := χ_K h^(≤1)(S),     f_ḃ := L_b ġ^aug(ḃ),     f_S := L_b h^aug(S).

These are [Hin26, (10.10)–(10.11) and (10.24a)] without the correction u_b there; in dimension 4 + 1 none is needed.

**Lemma {#lem:iii-h-2-2}** (The forcing terms.) Let h be ġ(ḃ) or h^(≤1)(S), and f := L_b(χ_K h).

(a) f = [L_b, χ_K]h, and f vanishes outside {1 ≤ t_* ≤ 2, |x| ≤ t_*/2} ∪ {t_* ≥ 2, t_*/4 ≤ |x| ≤ t_*/2}.

(b) Fix ψ ∈ C_c^∞([0, 2)) equal to 1 on [0, 1], and put f_c := ψ(r)f and f_∞ := (1 − ψ(r))f. Then f_c is smooth on
ℝ × X with support in {1 ≤ t_* ≤ 8, r ≤ 2}, f_∞ is supported in {r ≥ 1, 2r ≤ t_* ≤ 4r}, and for all j, a ∈ ℕ_0 and
multi-indices β on 𝕊³,

    |(t_*∂_(t_*))^j (r∂_r)^a ∂_ω^β f_∞| ≤ C r⁻⁴.                                                         {#eq:iii-h-2-1}

In the notation of [Hin26], f ∈ 𝒜^(∞,4,∞)(Ω) (orders at ℐ⁺, ι⁺ and K⁺), against 𝒜^(3,3+ϵ_ind−ϵ,4+ϵ_ind−ϵ) in
dimension 3 + 1 ([Hin26, (10.12)]).

*Proof.* (a) Since L_b h = 0 ([[sec:iii-h-1]]), f = L_b(χ_K h) − χ_K L_b h = [L_b, χ_K]h, and

    [L_b, χ_K]h = [L_0, χ_K]h + L_1((∂_(t_*)χ_K)h) + [L_1, χ_K]∂_(t_*)h
                  + L_2((∂²_(t_*)χ_K)h + 2(∂_(t_*)χ_K)∂_(t_*)h),

L_2 being a multiplication. Every coefficient contains a derivative of χ_K of order at least 1. For t_* ≥ 2,
χ_K = χ_c(|x|/t_*), whose derivatives vanish unless |x|/t_* ∈ [¼, ½]; for t_* ∈ [1, 2], χ_K vanishes unless
|x| ≤ t_*/2 ≤ 1; and for t_* < 1 it vanishes.

(b) On supp f ∩ {r ≤ 2}, t_* ≤ max(2, 4r) ≤ 8. The first set of (a) meets {r ≥ 1} only where r = 1 and t_* = 2, so
on supp f ∩ {r ≥ 1}, 2r ≤ t_* ≤ 4r. There χ_K = χ_c(r/t_*), which is homogeneous of degree 0 in (t_*, x); so
∂^p_(t_*)∂^q_x χ_K is homogeneous of degree −p − |q| and bounded by C r^(−p−|q|) on the cone {2r ≤ t_* ≤ 4r}, and so
are its derivatives along t_*∂_(t_*), r∂_r and ∂_ω, which preserve homogeneity. On the cone the states satisfy, with
these derivatives, |ġ| ≤ C r⁻² and ∂_(t_*)ġ = 0; |t_*h(S)| ≤ 4r · C r⁻³, t_*∂_(t_*)(t_*h) = t_*h and
|∂_(t_*)(t_*h)| = |h| ≤ C r⁻³; |h̆| ≤ C r⁻² and ∂_(t_*)h̆ = 0. As L_0 ∈ ρ²Diff_b^2, [L_0, χ_K] is ρ² times a
first-order b-operator in x whose coefficients are bounded on the cone, together with their b-derivatives and their
t_*∂_(t_*)-derivatives; so [L_0, χ_K]h = O(r⁻² · r⁻²). Likewise L_1((∂_(t_*)χ_K)h) = O(r⁻¹ · r⁻¹r⁻²),
[L_1, χ_K]∂_(t_*)h = O(r⁻¹ · r⁻³) ([L_1, χ_K] is ρ times a bounded multiplication), and the L_2 terms are
O(r⁻²(r⁻²r⁻² + r⁻¹r⁻³)). The same bounds hold after applying (t_*∂_(t_*))^j(r∂_r)^a∂_ω^β, which commute with the
stationary b-operators up to b-operators of the same class. ∎

**Lemma {#lem:iii-h-2-3}** (Zero frequency; [Hin26, Lemma 10.4 (1) and (10.24c)].) Let f̂(0) := ∫ f dt_*, pointwise
in x (f(·, x) has compact support). Then f̂(0) is smooth on X and lies in 𝒜³ near ∂X, and

    f̂_ḃ(0) = L_1 ġ(ḃ) + L_0 w_ḃ,     f̂_S(0) = L_2 h(S) + L_1 h̆(S) + L_0 w_S,                          {#eq:iii-h-2-2}

with w_ḃ := −κ(r)ġ(ḃ) and w_S := −κ′(r)h(S) − (κ(r) + κ_2)h̆(S), where

    κ(r) := ∫ χ_+(t)(1 − χ_c(r/t)) dt,     κ′(r) := ∫ χ_+(t)(1 − χ_c(r/t)) t dt,     κ_2 := ∫ t χ_+′(t) dt.

For r ≥ 1, κ(r) = κ_0 r − κ_1 and κ′(r) = κ′_0 r² − κ′_1, with

    κ_0 = ∫_0^4 (1 − χ_c(1/s)) ds,     κ′_0 = ∫_0^4 s(1 − χ_c(1/s)) ds,
    κ_1 = ∫_0^2 (1 − χ_+(t)) dt,     κ′_1 = ∫_0^2 t(1 − χ_+(t)) dt.

So w_ḃ and w_S are smooth on X, linear in ḃ and S, and lie in 𝒜¹ near ∂X.

*Proof.* Write χ_K = χ_+ + (χ_K − χ_+), with χ_+ = χ_+(t_*). For each x, (χ_K − χ_+)(·, x) = χ_+(t_*)(χ_c(r/t_*) − 1)
is smooth with support in [1, max(2, 4r)], locally uniformly in x. So for h′ := (χ_K − χ_+)h, differentiating under the
integral,

    ∫ L_b h′ dt_* = L_0 ∫ h′ dt_* + L_1 ∫ ∂_(t_*)h′ dt_* + L_2 ∫ ∂²_(t_*)h′ dt_* = L_0 ∫ h′ dt_*,

and ∫ h′ dt_* equals −κ(r)ġ for h = ġ, and −κ′(r)h − κ(r)h̆ for h = h^(≤1). Next,
L_b(χ_+ġ) = χ_+′L_1ġ + χ_+″L_2ġ has compact support in t_* and integrates to L_1ġ. And, using L_0 h = 0,

    L_b(χ_+(t_*h + h̆)) = χ_+(L_1h + L_0h̆) + t_*χ_+′L_1h + (t_*χ_+)″L_2h + χ_+′L_1h̆ + χ_+″L_2h̆,

whose first term vanishes. The rest has compact support in t_* and integrates to κ_2L_1h + L_2h + L_1h̆, as
∫(t_*χ_+)″ = 1, ∫χ_+′ = 1 and ∫χ_+″ = 0; and κ_2L_1h = L_0(−κ_2h̆). Since f = L_b(χ_+h) + L_bh′,
[[eq:iii-h-2-2]] follows. For r ≥ 1, 1 − χ_c(r/t) = 1 for t ≤ 2r, in particular on supp(1 − χ_+) ⊂ (−∞, 2]; so

    κ(r) = ∫_0^∞ (1 − χ_c(r/t)) dt − ∫_0^2 (1 − χ_+) dt = κ_0 r − κ_1,

substituting t = rs and using that 1 − χ_c(1/s) vanishes for s ≥ 4; κ′(r) is treated likewise. Then w ∈ 𝒜¹ (as
r𝒜² ⊂ 𝒜¹ and r²𝒜³ ⊂ 𝒜¹), and f̂(0) ∈ 𝒜³ by [[eq:iii-h-2-2]], since L_1𝒜² ⊂ 𝒜³, L_0𝒜¹ ⊂ 𝒜³ and L_2𝒜³ ⊂ 𝒜⁵. ∎

**Lemma {#lem:iii-h-2-4}** (Fourier transforms of the forcing terms; [Hin26, Lemma 10.4 (2)–(4)].) For Im σ ≥ 0 let
f̂(σ, x) := ∫ e^(iσt_*) f(t_*, x) dt_*.

(a) (*Structure.*) f̂ = f̂_c + f̂_∞, where f̂_c is entire in σ with values in the smooth sections supported in
{r ≤ 2}, and, on {r ≥ 1},

    f̂_∞(σ, x) = r⁻³G(σr, x),     G(ζ, x) := ∫_2^4 e^(iζs)F(s, x) ds,     F(s, x) := r⁴f_∞(sr, x),   {#eq:iii-h-2-3}

where for Im ζ ≥ 0 and all j, a, β and M, |(ζ∂_ζ)^j(r∂_r)^a∂_ω^β G(ζ, x)| ≤ C⟨ζ⟩^(−M); G is entire in ζ.

(b) (*Uniform bounds.*) For k, j ∈ ℕ_0, M ∈ ℝ and β_tf < 3,
sup_(σ∈Σ_0) ‖(σ∂_σ)^j f̂(σ)‖_(H^(k,(M,β_tf,0))_(b,|σ|)) < ∞, with the norm of [[sec:ii-g1-4-3]] (density μ_b). Hence,
by [[eq:ii-g1-4-5a]], for every order pair (s′, 𝗋′) as in [[lem:ii-g1-4-6]] and every l < −1, with ς_1 as there,

    sup_(σ∈Σ_0, |σ|≤ς_1) ‖(σ∂_σ)^j f̂(σ)‖_((s′−1;k),(𝗋′+1,l+2,0),|σ|) < ∞.                             {#eq:iii-h-2-4}

(c) (*Regularity at zero frequency.*) Let φ ∈ C^∞([0, ∞)) vanish on [0, 2] and be bounded with its derivatives. For
a ∈ (0, 1) and p ∈ ℕ_0 there is C with

    ‖φ(ρ/|σ|)(f̂(σ) − f̂(0))‖_(H̄_b^(p,a)) ≤ C|σ|^(1−a),     σ ∈ Σ_0.                                  {#eq:iii-h-2-5}

(d) (*Continuity, holomorphy.*) σ ↦ f̂(σ) is continuous on {Im σ ≥ 0, |σ| ≤ 1} with values in H̄_b^(p,a) for every p
and every a < 1. It is smooth on {Im σ ≥ 0} ∖ 0 and holomorphic on {Im σ > 0} with values in H̄_b^(p,M) for every p
and M.

*Proof.* (a) f_c is smooth with compact support, so f̂_c is entire. For r ≥ 1, by [[lem:iii-h-2-2]] (b) and t_* = sr,
f̂_∞(σ, x) = r∫_2^4 e^(iσrs)f_∞(sr, x) ds = r⁻³G(σr, x). F is smooth and supported in s ∈ [2, 4], so it vanishes with
all its s-derivatives at s = 2 and s = 4; and it is bounded together with all its derivatives along s∂_s, r∂_r (at
fixed s) and ∂_ω, since s∂_sF = r⁴(t_*∂_(t_*)f_∞)(sr, x) and r∂_rF = r⁴((4 + t_*∂_(t_*) + r∂_r)f_∞)(sr, x) are bounded
by [[eq:iii-h-2-1]]. For Im ζ ≥ 0 and s > 0, |e^(iζs)| ≤ 1. Integrating by parts M times with
e^(iζs) = (iζ)⁻¹∂_s e^(iζs) gives the decay; and ζ∂_ζ e^(iζs) = s∂_s e^(iζs) gives
(ζ∂_ζ)^jG = ∫ e^(iζs)(−∂_s s)^jF ds, of the same kind. Derivatives in x pass under the integral.

(b) By [[sec:ii-g1-4-3]], with ς := |σ| and ρ̂ := ⟨x⟩⁻¹/ς, ρ_scf = ρ̂/(1 + ρ̂), ρ_tf = ς(1 + ρ̂) and
ρ_zf = (1 + ρ̂)⁻¹, and ‖u‖_(H^(k,β)_(b,ς)) = ‖w_β(ς)⁻¹u‖_(H̄^k_b(X̄,μ_b)) with
w_β = ρ_scf^(β_scf) ρ_tf^(β_tf) ρ_zf^(β_zf). Since σ∂_σ acts on [[eq:iii-h-2-3]] as ζ∂_ζ on G, it suffices to take
j = 0 with G replaced by (ζ∂_ζ)^jG. On {r ≥ 1}, |ζ| = ςr is comparable to ρ̂⁻¹, and r⁻³ to
⟨x⟩⁻³ = (ρ_scf ρ_tf)³; so, for every M′,

    |w_β⁻¹ f̂_∞| ≤ C ρ_scf^(3−M) ρ_tf^(3−β_tf) ⟨ρ̂⁻¹⟩^(−M′).

Where ρ̂ ≥ 1, ρ_scf ∈ [½, 1] and ρ_tf ∈ [⟨x⟩⁻¹, 2⟨x⟩⁻¹], and the bound is C⟨x⟩^(−(3−β_tf)), square integrable for μ_b
on {⟨x⟩ ≥ 1} uniformly in ς, as β_tf < 3. Where ρ̂ ≤ 1, ρ_scf ∈ [ρ̂/2, ρ̂] and ρ_tf ∈ [ς, 2ς], and the bound is
Cρ̂^(3−M+M′), square integrable for μ_b = |dρ̂/ρ̂| dω when M′ > M − 3. The b-derivatives along r∂_r and ∂_ω fall on
r⁻³, on ζ = σr (giving ζ∂_ζG) and on the x-dependence of G, with the same bounds; and w_β has bounded logarithmic
b-derivatives ([[sec:ii-g1-4-3]]). f̂_c is bounded in C^∞, uniformly for |σ| ≤ 1, with support in {r ≤ 2}, where
ρ̂ ≥ c/ς ≥ c, so w_β⁻¹ is bounded there. Then [[eq:iii-h-2-4]] is [[eq:ii-g1-4-5a]] with l + 4 = β_tf and
M = 𝗋′_out + 3 + ϵ.

(c) On supp φ(ρ/ς) ⊂ {ρ ≥ 2ς}, |σr| ≤ ½, and by (a) and Taylor's formula
|(r∂_r)^a∂_ω^β(G(σr, x) − G(0, x))| ≤ C|σ|r there; the b-derivatives of φ(ρ/ς) are bounded uniformly in ς. So
|f̂_∞(σ) − f̂_∞(0)| ≤ Cςρ² there, together with b-derivatives. As H̄_b^(p,a) = ρ^(a+2)H̄_b^p(μ_b), the part of the left
side of [[eq:iii-h-2-5]] over {r ≥ 1} is at most

    C‖ςρ^(−a)‖_(L²({2ς≤ρ≤1}, μ_b)) = Cς(∫_(2ς)^1 ρ^(−2a−1) dρ)^(1/2) ≤ Cς^(1−a),

as a > 0. And f̂_c(σ) − f̂_c(0) = O(|σ|) in C^∞, with support in {r ≤ 2}.

(d) f̂_c is entire. For σ ≠ 0, by (a), f̂_∞(σ) and ∂^j_σ f̂_∞(σ) = r^(j−3)(∂^j_ζG)(σr, x) are O(r^(j−3)(|σ|r)^(−M))
for every M, locally uniformly in σ, together with their b-derivatives; this gives smoothness in every H̄_b^(p,M), and,
G being entire, holomorphy in {Im σ > 0}. At σ = 0: on {ρ ≥ 2ς} the difference is bounded as in (c); on {ρ ≤ 2ς},
|f̂(σ)| and |f̂(0)| are at most Cρ³, whose H̄_b^(p,a)-norm there is O(ς^(1−a)). ∎

**Lemma {#lem:iii-h-2-5}** (The cut-off states on the spectral side.) For Im σ ≥ 0, σ ≠ 0, let
Ψ(σ, x) := ∫ e^(iσt_*)∂_(t_*)χ_K(t_*, x) dt_* and

    ĝ^aug(σ)(ḃ) := iσ⁻¹Ψ(σ, ·)ġ(ḃ),     ĥ^aug(σ)(S) := ∂_σ(σ⁻¹Ψ(σ, ·))h(S) + iσ⁻¹Ψ(σ, ·)h̆(S).          {#eq:iii-h-2-6}

(a) For Im σ > 0 these are the absolutely convergent Fourier transforms of ġ^aug(ḃ) and h^aug(S).

(b) For r ≥ 1, Ψ(σ, x) = Φ(σr) with Φ(ζ) := ∫_2^4 e^(iζs)∂_s[χ_c(1/s)] ds, an entire function with Φ(0) = 1 and
|∂^j_ζΦ(ζ)| ≤ C_(j,M)⟨ζ⟩^(−M) on {Im ζ ≥ 0}. Hence [[eq:iii-h-2-6]] is smooth on X and lies in H̄_b^(p,M) for every p
and M, smoothly in σ ∈ {Im σ ≥ 0} ∖ 0 and holomorphically in the interior; in particular it lies in 𝒳_σ.

(c) L̂_b(σ)ĝ^aug(σ)(ḃ) = f̂_ḃ(σ) and L̂_b(σ)ĥ^aug(σ)(S) = f̂_S(σ).

(d) For R ≥ 1 there is C with |Ψ(σ, x) − 1| ≤ C|σ| and |∂_σΨ(σ, x)| ≤ C for r ≤ R and σ ∈ Σ_0.

*Proof.* (a) For Im σ > 0, ∫ e^(iσt_*)χ_K dt_* converges absolutely, as χ_K is bounded and vanishes for t_* ≤ 1, and
integrating by parts, the boundary term at ∞ vanishing,

    ∫ e^(iσt_*)χ_K dt_* = −(iσ)⁻¹∫ e^(iσt_*)∂_(t_*)χ_K dt_* = iσ⁻¹Ψ;

and ∫ e^(iσt_*)t_*χ_K dt_* = −i∂_σ(iσ⁻¹Ψ) = ∂_σ(σ⁻¹Ψ). The states are stationary.

(b) For r ≥ 1, χ_K(t_*, x) = χ_c(r/t_*) for t_* > 0 ([[sec:iii-h-1]]), so ∂_(t_*)χ_K is supported in 2r ≤ t_* ≤ 4r,
and with t_* = rs, Ψ = ∫ e^(iσrs)∂_s[χ_c(1/s)] ds = Φ(σr). The function ∂_s[χ_c(1/s)] is smooth with support in
[2, 4] and integral χ_c(¼) − χ_c(½) = 1, and the bounds follow by integration by parts as in [[lem:iii-h-2-4]] (a). So
for σ ≠ 0, Ψ, ∂_σΨ = rΦ′(σr) and their σ- and b-derivatives are each O(r^q(|σ|r)^(−M)) for every M, with q ∈ ℕ_0
depending on the number of σ-derivatives, locally uniformly in σ; with the conormal bounds of the states this gives
the memberships. For r ≤ 1, ∂_(t_*)χ_K(·, x) is supported in [1, 4], and Ψ is entire in σ and smooth in x. A section
that lies in H̄_b^(p,M) for all p and M lies in 𝒳_σ, since L̂_b(σ) maps it into the same class.

(c) For Im σ > 0, integrating by parts in t_* (there are no boundary terms: χ_Kh vanishes for t_* ≤ 1 and grows at most
linearly, and e^(iσt_*) decays), ℱ(L_bv)(σ) = L̂_b(σ)ℱ(v)(σ) for v = χ_Kh; so (c) holds there by (a). Both sides are
continuous on {Im σ ≥ 0} ∖ 0, pointwise in x ([[lem:iii-h-2-4]] (d) and (b)), so (c) extends to real σ ≠ 0.

(d) For r ≤ R, ∂_(t_*)χ_K(·, x) is supported in [1, max(2, 4R)] and integrates to 1; so
Ψ − 1 = ∫(e^(iσt_*) − 1)∂_(t_*)χ_K dt_* and ∂_σΨ = ∫ it_*e^(iσt_*)∂_(t_*)χ_K dt_*, with |e^(iσt_*)| ≤ 1. ∎

So, as σ → 0, ĝ^aug(σ) ∼ iσ⁻¹ġ and ĥ^aug(σ) ∼ −σ⁻²h + iσ⁻¹h̆ on compact sets. These are the naive columns of
[Hin26, (10.5)], whose spacetime counterparts are H(t_*)ġ and H(t_*)(t_*h + h̆), H the Heaviside function.

**Remark {#rem:iii-h-2-6}** (Uniformity in b.) [[lem:iii-h-2-2]]–[[lem:iii-h-2-4]] are stated at fixed b; near b_0
their bounds hold uniformly with a loss δ > 0. The states depend continuously on b with values in H̄_b^(p,a) for every
p and every a below their weights minus 2: for ġ(ḃ) by [[prop:iii-f3-2-2]] (3), at every regularity; for h(S) and
h̆(S) by [[lem:iii-d2-2-2]], the continuity of the 1-forms ω′_b, ω̆′_b in H̄_b^(s,α) below their weight, δ*_(g_b)
gaining one order of decay. And H̄_b^(∞,a) ⊂ 𝒜^(a+2) (b-Sobolev embedding, as H̄_b^(p,a) = ρ^(a+2)H̄_b^p(μ_b)). So for
every δ > 0 the states are bounded in 𝒜^(2−δ) (ġ(1, 0) and h̆(S)), resp. 𝒜^(3−δ) (ġ(0, Ȧ) and h(S)), and in C^∞ on
compact subsets of X, locally uniformly in b; and the coefficients of L_b depend smoothly on b. The proofs then give,
uniformly for b near b_0: [[eq:iii-h-2-1]] with r^(−4+δ); f̂(0) bounded in 𝒜^(3−δ) and w in 𝒜^(1−δ);
[[eq:iii-h-2-3]] with |G| ≤ Cr^δ⟨ζ⟩^(−M), together with its derivatives; [[lem:iii-h-2-4]] (b) for β_tf < 3 − δ;
[[eq:iii-h-2-5]] with |σ|^(1−a−δ); and the bounds in the proof of [[lem:iii-h-5-2]] (b) with ρ^(3−δ). By
[[eq:iii-h-2-2]], f̂(0) depends continuously on b in H̄_b^(∞,a) for every a < 1. Where uniformity in b is used (the bound
of [[prop:iii-h-3-2]], [[cor:iii-h-4-2]], [[cor:iii-h-4-3]] and [[lem:iii-h-5-2]]) the weights leave room for the loss:
with δ := ϵ_0 := ¼(1 − (α + 2)), α + 2 + ϵ_0 < 1 − δ and 1 − (α + 2) − δ ≥ ϵ_0.
