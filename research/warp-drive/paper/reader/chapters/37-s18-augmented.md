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
and is not needed here. In the proof of [Hin26, Theorem 10.1] in dimension 3 + 1, the derivatives ∂_(t_*)v_ġ and
∂²_(t_*)v_h of the contributions of the states ([[eq:iii-h1-5-1]]) have sf-weights −½ − ϵ and ½ − ϵ, and the two
integrations in t_* end at −3/2 − ϵ, below α_sf; this is the sf-loss δ > α_sf + 3/2 of [Hin26, Theorem 10.1]. In
dimension 4 + 1 the transforms of the cut-off states decay rapidly at scf ([[lem:iii-h-2-5]]), the derivatives have
sf-weights below 0 and 1, which leaves room for α_sf + 1 and α_sf + 2, and the integrations return to α_sf itself
([[lem:iii-h1-5-1]] and [[sec:iii-h1-7]]). No splitting at ℐ⁺ ([Hin26, (10.57)]) and no condition at the outgoing
radial set ([Hin26, Remark 10.2], used in the proof of [Hin26, Lemma 10.12]) is needed. Several steps of [Hin26] need
more than is stated there, in dimension 3 + 1 as in 4 + 1; [[sec:s18-remarks]] collects them.

*The inner radius.* Every result of the chapter holds with the inner radius r_0 = r_♭ ∈ (0, ½R_1] of [[def:s12-radii]]
as a parameter, with constants that depend on it. The radius enters only through r ≥ r_0 > 0 on X, through the spaces,
which are extendible at {r = r_0}, through the radii of [[sec:i-a-1-1]] in (C2) of [[def:iii-h1-1-1]], and through the
constancy of the orders over {r ≤ r_0 + δ_1} and the extension across {r = r_0} in the proof of [[lem:iii-h1-6-2]].

*Notation.* The black-hole parameter is b = (m, A), with mass m, and b_0 = (m_0, 0). The letter h denotes a zero energy
state (h(S), h̆(S)) or, as an index (⟨·, ·⟩_h, h_Γ), a fibre inner product; the semiclassical parameter of [[ch:s02]]
is written |σ|⁻¹. Large exponents of decay are written M. The Fourier transform is (ℱu)(σ) := ∫ e^(iσt_*) u dt_*
([[eq:iii-a-2-2]]), under which ∂_(t_*) becomes −iσ.

### Setting {#sec:iii-h-1}

*Parameters.* They are those of [[sec:iii-f3-1]] and [[sec:iii-f4-1]]: b = (m, A) near b_0, the modification parameters
with (Dyn), condition (C1) of [[sec:iii-f1-1]] and γ_Υ small, and a constant regularity s > ½ + ϑ_L
([[lem:iii-f2-1-1]]). (The conditions (C1)–(C3) of [[def:iii-h1-1-1]] below are different ones.) The pairing is
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
stationary sections L_0 = L̂_b(0), L_1 = [L_b, t_*] and L_2 = ½[ [L_b, t_*], t_* ], and

    L̂_b(σ) = L_0 − iσL_1 − σ²L_2.

Near ∂X, L_0 ∈ ρ²Diff_b^2, L_1 ∈ ρ Diff_b^1 and L_2 ∈ ρ²C^∞ ([[eq:iii-g4-1-2]] and the proof of [[lem:iii-g4-1-2]],
which rest on [[lem:iii-f-2-1]]; [[eq:i-c-1-1]]). On compact subsets of X the L_j have smooth coefficients.

*The states.* Let 𝔟 := ℝ ⊕ 𝔰𝔬(4). For ḃ = (ṁ, Ȧ) ∈ 𝔟 put

    ġ(ḃ) := ṁ ġ^Υ_b(1, 0) + ġ^Υ_b(0, Ȧ),

with ġ^Υ_b of [[prop:iii-f3-2-2]], and for S ∈ 𝒮_1 let h(S) := h_(b,s1)(S) and h̆(S) := h̆¹_(b,s1)(S)
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
|(r∂_r)^(a′)∂_ω^β(G(σr, x) − G(0, x))| ≤ C|σ|r there; the b-derivatives of φ(ρ/ς) are bounded uniformly in ς. So
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
continuous on {Im σ ≥ 0} ∖ 0, pointwise in x (the right side by [[lem:iii-h-2-4]] (d), the left by (b) above, L̂_b(σ)
being polynomial in σ), so (c) extends to real σ ≠ 0.

(d) For r ≤ R, ∂_(t_*)χ_K(·, x) is supported in [1, max(2, 4R)] and integrates to 1; so
Ψ − 1 = ∫(e^(iσt_*) − 1)∂_(t_*)χ_K dt_* and ∂_σΨ = ∫ it_*e^(iσt_*)∂_(t_*)χ_K dt_*, with |e^(iσt_*)| ≤ 1. ∎

So, as σ → 0, ĝ^aug(σ) ∼ iσ⁻¹ġ and ĥ^aug(σ) ∼ −σ⁻²h + iσ⁻¹h̆ on compact sets. These are the naive columns of
[Hin26, (10.5)], whose spacetime counterparts are H(t_*)ġ and H(t_*)(t_*h + h̆), H the Heaviside function.

**Remark {#rem:iii-h-2-6}** (Uniformity in b.) [[lem:iii-h-2-2]]–[[lem:iii-h-2-4]] are stated at fixed b; near b_0 their
bounds hold uniformly with a loss δ > 0. The states depend continuously on b with values in H̄_b^(p,a) for every p and
every a below their weights minus 2: for ġ(ḃ) by [[prop:iii-f3-2-2]] (3), at every regularity; for h(S) and h̆(S) by
[[prop:iii-d2-3-1]] and [[lem:iii-d2-2-2]], the 1-forms ω^(0)_(b,s1)(S) and ω̆^((0),1)_(b,s1)(S) being continuous in b
in H̄_b^(s,α) below their weight and δ*_(g_b) gaining one order of decay. And H̄_b^(∞,a) ⊂ 𝒜^(a+2) (b-Sobolev embedding,
as H̄_b^(p,a) = ρ^(a+2)H̄_b^p(μ_b)). So for every δ > 0 the states are bounded in 𝒜^(2−δ) (ġ(1, 0) and h̆(S)), resp.
𝒜^(3−δ) (ġ(0, Ȧ) and h(S)), and in C^∞ on compact subsets of X, locally uniformly in b; and the coefficients of L_b
depend smoothly on b. The proofs then give, uniformly for b near b_0: [[eq:iii-h-2-1]] with r^(−4+δ); f̂(0) bounded in
𝒜^(3−δ) and w in 𝒜^(1−δ); [[eq:iii-h-2-3]] with |G| ≤ Cr^δ⟨ζ⟩^(−M), together with its derivatives; [[lem:iii-h-2-4]] (b)
for β_tf < 3 − δ; [[eq:iii-h-2-5]] with |σ|^(1−a−δ); and the bounds in the proof of [[lem:iii-h-5-2]] (b) with ρ^(3−δ).
By [[eq:iii-h-2-2]], f̂(0) depends continuously on b in H̄_b^(∞,a) for every a < 1. Where uniformity in b is used (the
bound of [[prop:iii-h-3-2]], [[cor:iii-h-4-2]], [[cor:iii-h-4-3]] and [[lem:iii-h-5-2]]) the weights leave room for the
loss: with δ := ϵ_0 := ¼(1 − (α + 2)), α + 2 + ϵ_0 < 1 − δ and 1 − (α + 2) − δ ≥ ϵ_0.

### The augmented zero energy operator {#sec:iii-h-3}

This section is [Hin26, Proposition 10.6] in dimension 4 + 1.

*The rows.* Fix real f*_1 ∈ C_c^∞(X°; S²T*X) ⊗ 𝔟* and f*_2 ∈ C_c^∞(X°; S²T*X) ⊗ 𝒮_1* such that, at b_0,

    ⟨ġ(ḃ), f*_1⟩ = ḃ,     ⟨h(S), f*_1⟩ = 0,     ⟨ġ(ḃ), f*_2⟩ = 0,     ⟨h(S), f*_2⟩ = S,                {#eq:iii-h-3-1}

after fixing bases; ⟨·, f*_j⟩ is taken componentwise. They exist: the eleven states are independent
([[prop:iii-f3-4-1]] (1)) and smooth on X°, and the restriction map C_c^∞(X°) → W* is onto for every
finite-dimensional W ⊂ 𝒟′(X°) (proof of [[cor:iii-f3-4-2]]). By the continuity of the states in b (the last step of
the proof of [[prop:iii-f3-4-1]]), the matrix B(b) := (⟨·, f*⟩) of the nullspace in these bases is invertible near b_0,
with B(b_0) = I. [[eq:iii-h-3-1]] contains [Hin26, (10.6b)] and more. [Hin26, (10.6b)] asks only that the
block-diagonal map (ḃ, S) ↦ (⟨ġ(ḃ), f*_1⟩, ⟨h(S), f*_2⟩) be an isomorphism, while the proof of [Hin26, Proposition
10.6] uses that u ↦ (⟨u, f*_1⟩, ⟨u, f*_2⟩) is injective on the nullspace; under [Hin26, (10.6b)] alone the conclusion
of [Hin26, Proposition 10.6] can fail ([[rem:s18-rows]]).

**Definition {#def:iii-h-3-1}** ([Hin26, (10.26)] in dimension 4 + 1.) For Im σ ≥ 0, acting on (u, ḃ, S) with u a
section over X, ḃ ∈ 𝔟_ℂ and S ∈ 𝒮_(1,ℂ),

    L̃_b(σ)(u, ḃ, S) := (L̂_b(σ)u + f̂_ḃ(σ) + f̂_S(σ), ⟨u, f*_1⟩, ⟨u, f*_2⟩).                           {#eq:iii-h-3-2}

By [[lem:iii-h-2-5]] (c), for σ ≠ 0 the column terms are L̂_b(σ)ĝ^aug(σ)(ḃ) and L̂_b(σ)ĥ^aug(σ)(S), the form they have
in [Hin26].

**Proposition {#prop:iii-h-3-2}** ([Hin26, Proposition 10.6] in dimension 4 + 1.) For b near b_0 and α as in
[[eq:iii-h-1-1]],

    L̃_b(0) : 𝒳_0 ⊕ 𝔟_ℂ ⊕ 𝒮_(1,ℂ) → 𝒴_0 ⊕ 𝔟_ℂ ⊕ 𝒮_(1,ℂ),
    𝒳_0 = {u ∈ H̄_b^(s,α) : L̂_b(0)u ∈ 𝒴_0},     𝒴_0 = H̄_b^(s−1,α+2),

is invertible, with inverse bounded uniformly near b_0. (The column terms lie in 𝒴_0, so the domain is that of
[Hin26, (10.27)].)

*Proof.* f̂(0) ∈ 𝒜³ ⊂ H̄_b^(∞,α+2) by [[lem:iii-h-2-3]], as α + 2 < 1.

*Index.* By [[prop:iii-f3-4-1]] at the b-weight α + 2 ∈ (0, 1], L̂_b(0) : 𝒳_0 → 𝒴_0 is Fredholm of index 0. So
L̃_b(0), a finite rank perturbation of L̂_b(0) ⊕ 0_(ℂ¹¹→ℂ¹¹), has index 0.

*Injectivity.* Let L̃_b(0)(u, ḃ, S) = 0. By [[eq:iii-h-2-2]],

    L_0(u + w_ḃ + w_S) + L_1ġ(ḃ) + L_2h(S) + L_1h̆(S) = 0.

Here w := w_ḃ + w_S is smooth on X and lies in 𝒜¹ ⊂ H̄_b^(∞,α) near ∂X (as α < −1), and L_0w ∈ 𝒜³ ⊂ 𝒴_0; so
u + w ∈ 𝒳_0, and L_0(u + w) lies in the range of [[eq:iii-f3-4-1]], which the dual states [[eq:iii-f3-4-3]] annihilate
([[prop:iii-f3-4-1]] (2)). Pairing with them,

    ⟨L_1ġ(ḃ) + L_2h(S) + L_1h̆(S), h*⟩ = 0,     h* ∈ {h*_(b,s0), h*_(b,s1)(S′), h*_(b,v1)(V)}.

By [[lem:iii-f4-3-1]] (1)–(4) this is a linear system in (ṁ, S, Ȧ) whose 11 × 11 matrix is block upper triangular with
determinant 3π²(3π²m/2)⁴(2π²m)⁶ ≠ 0. So ḃ = 0 and S = 0, hence w = 0, and u lies in the nullspace, which the states
span ([[prop:iii-f3-4-1]] (1)). As ⟨u, f*_1⟩ = 0, ⟨u, f*_2⟩ = 0 and B(b) is invertible, u = 0.

*Uniform bound.* We show ‖u‖_(H̄_b^(s,α)) + |ḃ| + |S| ≤ C‖L̃_b(0)(u, ḃ, S)‖ with C uniform near b_0; this is the
argument of [[cor:iii-f3-4-2]] (1). The coefficients of L̂_b(0) depend smoothly on b, the columns f̂_ḃ(0), f̂_S(0)
depend continuously on b in H̄_b^(∞,α+2) ([[rem:iii-h-2-6]]), and [[eq:i-c-3-2]] holds with a constant uniform near b_0
([[thm:i-c-7-1]] (2)). If the bound fails, there are b_j → b_0 and (u_j, ḃ_j, S_j) with
‖u_j‖_(H̄_b^(s,α)) + |ḃ_j| + |S_j| = 1 and L̃_(b_j)(0)(u_j, ḃ_j, S_j) → 0 in 𝒴_0 ⊕ 𝔟_ℂ ⊕ 𝒮_(1,ℂ). The columns at b_j
are bounded in 𝒴_0, so L̂_(b_j)(0)u_j is bounded in 𝒴_0, and by [[eq:i-c-3-2]] a subsequence converges weakly in
H̄_b^(s,α) and strongly in H̄_b^(−M,−M) ([[lem:i-c-2-9]] (b)) to some u, with ḃ_j → ḃ and S_j → S. As
L̂_(b_j)(0) − L̂_(b_0)(0) → 0 as maps H̄_b^(s,α) → H̄_b^(s−2,α+2), and the columns converge in 𝒴_0, the first component
of L̃_(b_0)(0)(u, ḃ, S) vanishes; so L̂_(b_0)(0)u ∈ 𝒴_0, that is u ∈ 𝒳_0, and ⟨u, f*_1⟩ = 0, ⟨u, f*_2⟩ = 0, the rows
being test sections. By the injectivity at b_0, (u, ḃ, S) = 0. Then ḃ_j, S_j → 0, so
‖L̂_(b_j)(0)u_j‖_(H̄_b^(s−1,α+2)) → 0, and ‖u_j‖_(H̄_b^(−M,−M)) → 0; by [[eq:i-c-3-2]], ‖u_j‖_(H̄_b^(s,α)) → 0. This
contradicts the normalisation. ∎

Of s the proof uses only s > ½ + ϑ_L, through [[prop:iii-f3-4-1]], [[thm:i-c-3-1]] and [[thm:i-c-7-1]]. So
[[prop:iii-h-3-2]] holds at every such constant s, with 𝒳_0 and 𝒴_0 at that regularity; in particular at the
regularities s + k and s + i at which the proof of [[thm:iii-h-4-1]] inverts 𝒫(0).

[Hin26] pairs with h*_(b,s0), then with h*_(b,v1), then with h*_(b,s1), and handles its error term L̂_b(0)h′ by an
integration by parts against the decay of the dual states. Here the error L_0w lies in the range of L̂_b(0) on the
domain itself, as w ∈ 𝒜¹ and α < −1, so no integration by parts is needed; and the pairings are taken in the order of
the triangular matrix of [[lem:iii-f4-3-1]] (4) (rows ṁ, S, Ȧ), in which the entries that the leading terms do not
determine drop out.

**Remark {#rem:s18-rows}** (The rows in [Hin26].) [Hin26, (10.6b)] asks that (ḃ, S) ↦ (⟨ġ(ḃ), f*_1⟩, ⟨h(S), f*_2⟩)
be an isomorphism. The proof of [Hin26, Proposition 10.6] uses that u ↦ (⟨u, f*_1⟩, ⟨u, f*_2⟩) is injective on the
nullspace, which [Hin26, (10.6b)] does not imply, because of the cross terms ⟨h(S′), f*_1⟩ and ⟨ġ(ḃ′), f*_2⟩. The
choice [[eq:iii-h-3-1]] gives both. Under [Hin26, (10.6a)–(10.6b)] alone, the conclusion of [Hin26, Proposition 10.6]
fails for some rows. Indeed, since the restriction map C_c^∞(X°) → W* is onto, every matrix of pairings of the states
with the rows is realised by some rows. Among them is the matrix with diagonal blocks I and off-diagonal blocks
⟨h(S), f*_1⟩ = τS and ⟨ġ(ḃ), f*_2⟩ = τ^T ḃ, where τ : 𝒮_1 → 𝔟 is isometric in the fixed bases (dim 𝒮_1 = 4 ≤ 7 =
dim 𝔟; in dimension 3 + 1 the dimensions are 3 ≤ 4). For it [Hin26, (10.6b)] holds, and for S ≠ 0 the state
u := ġ(−τS) + h(S) ≠ 0 lies in the nullspace with ⟨u, f*_1⟩ = −τS + τS = 0 and ⟨u, f*_2⟩ = −τ^TτS + S = 0. So
(u, 0, 0) lies in the kernel of [Hin26, (10.26)] at σ = 0.

### Uniform low-energy estimates {#sec:iii-h-4}

This section is [Hin26, Proposition 10.7] in dimension 4 + 1. [Hin26] extends [Hin26c, Theorem 9.41] to augmentation
columns that depend on σ and are not compactly supported ([Hin26, p. 209]). [[thm:i-c-6-4]] is stated for constant,
compactly supported columns, and [[thm:iii-h-4-1]] is the extension. Its hypotheses (A1)–(A4) ask that the values of
the columns at zero frequency be better than the target by ϵ_0 at tf, that the columns be bounded uniformly, Hölder
continuous of order ϵ_0 at zf and smooth in σ. The invertibility follows from the index, as there are as many columns
as rows, and the derivatives in σ from a Schur complement.

**Theorem {#thm:iii-h-4-1}** ([[thm:i-c-6-4]] with columns depending on σ.) Assume (H1)–(H4), (G) and (TF) as in
[[thm:i-c-6-4]], with s > ½ + ϑ_ℋ constant, the weight α (α + 2 in the gap of (G)) and α_+ ∈ ℝ, and assume that
P̂(σ) : 𝒳_σ → 𝒴_σ has index 0 for σ ∈ Σ_0. Let Σ′ be Σ_0 or Σ_0 ∩ ℝ, J ∈ ℕ, φ_1, …, φ_J ∈ C_c^∞(X°; E) and
ϵ_0 ∈ (0, 1], and let F_1, …, F_J be sections over X depending on σ ∈ Σ′ ∪ {0} such that, for all k, j ∈ ℕ_0, every
constant s′ and every η′ ∈ [0, ϵ_0]:

(A1) F_i(0) ∈ H̄_b^(∞,α+2+ϵ_0);

(A2) sup_(σ∈Σ′, |σ|≤ς_1) ‖(σ∂_σ)^j F_i(σ)‖_((s′;k),(𝗋+α_++1,α+2+η′,0),|σ|) < ∞, with ς_1 that of
[[eq:ii-g1-4-5a]];

(A3) ‖χ_zf(F_i(σ) − F_i(0))‖_(H̄_b^(s′+k,α+2)) ≤ C|σ|^(ϵ_0) for σ ∈ Σ′, with χ_zf the cut-off of
[[sec:i-c-6-4]];

(A4) σ ↦ F_i(σ) is smooth on Σ′ (along Σ′) with values in H̄^((s′;j),𝗋_(ς_*)+M) near each σ_* ∈ Σ′, for every M.

Put

    𝒫(σ)(u, c) := (P̂(σ)u + Σ_i c_i F_i(σ), (⟨u, φ_(i′)⟩_h)_(i′))

on 𝒳_σ ⊕ ℂ^J → 𝒴_σ ⊕ ℂ^J (on 𝒳_0 ⊕ ℂ^J → 𝒴_0 ⊕ ℂ^J at σ = 0), and assume that 𝒫(0) is invertible ((Z_𝒫)). Then:

(1) (*Uniform estimates.*) For every k there are c_k ∈ (0, ς_1], non-increasing in k, and C_k such that for σ ∈ Σ′
with |σ| ≤ c_k and 𝒫(σ)(u, c) = (f, e), (u, c) ∈ 𝒳_σ ⊕ ℂ^J,

    ‖u‖_((s;k),(𝗋+α_+,α,0),ς) + |c| ≤ C_k(‖f‖_((s−1;k),(𝗋+α_++1,α+2,0),ς) + |e|),                       {#eq:iii-h-4-1}

in the strong sense.

(2) (*Invertibility.*) For σ ∈ Σ′ with |σ| ≤ c_0, 𝒫(σ) is invertible.

(3) (*Derivatives in σ.*) If moreover P̂(σ) is invertible for σ ∈ Σ′, |σ| ≤ c_0, then for j, k ∈ ℕ_0 there are
c_(j,k) ∈ (0, c_0] and C with

    ‖(σ∂_σ)^j 𝒫(σ)⁻¹(f, e)‖_((s+j;k),(𝗋+α_+,α,0),ς) ≤ C(‖f‖_((s−1;k+j),(𝗋+α_++1,α+2,0),ς) + |e|)          {#eq:iii-h-4-2}

for σ ∈ Σ′, |σ| ≤ c_(j,k), the norm on the left being that of the first component plus the modulus of the second.
Here (σ∂_σ)^j 𝒫(σ)⁻¹ is the derivative on the spaces of [[thm:i-a-7-2]] (6), extended by [[eq:iii-h-4-2]].

*Proof.* We use two facts on the norms of [[def:i-c-6-1]]. First, for l, q ∈ ℝ and η ≥ 0,

    ‖u‖_((s;k),(𝗋,l,q−η),ς) = ς^η ‖u‖_((s;k),(𝗋,l+η,q),ς),                                              {#eq:iii-h-4-3}

as both squares equal ς^(−2(q−η))‖(1 − χ_∂)u‖² + ς^(−2(l+2))‖S_ς(χ_∂u)‖²_((𝗋,q−η−l)). Second, for
v ∈ H̄_b^(p,a+ϵ_0) independent of σ,

    ‖(1 − χ_zf)v‖_(H̄_b^(p,a)) ≤ Cς^(ϵ_0) ‖v‖_(H̄_b^(p,a+ϵ_0)),                                           {#eq:iii-h-4-4}

as 1 − χ_zf is supported in {ρ ≤ 4ς} and ρ^(ϵ_0)(1 − χ_zf) has b-derivatives bounded by Cς^(ϵ_0).

(1) This is the proof of [[thm:i-c-6-4]] (1) in [[sec:i-c-6-4]], with the following changes; the notation is that of
[[sec:i-c-6-4]], with ‖·‖_(l,q) := ‖·‖_((s;k),(𝗋+α_+,l,q),ς) and ‖·‖′_(l,q) := ‖·‖_((s−1;k),(𝗋+α_++1,l,q),ς), and
P̂(σ) = P̂(0) + σT + σ²P_2.

*Finiteness.* P̂(σ)u = f − Σ c_iF_i(σ), which lies in H̄^((s−1;k),𝗋_ς+α_++1) by (A2) and [[lem:i-c-6-2]] (c).

*Step 1.* The bounded inverse of 𝒫(0) at the regularity s + k exists as there, since 𝒫(0) is P̂(0) ⊕ 0 plus a finite
rank operator whose columns lie in 𝒴_0 at every regularity by (A1). From χ_zf(P̂(σ)u + Σ c_iF_i(σ)) = χ_zf f the
identity becomes

    P̂(0)(χ_zf u) + Σ c_iF_i(0) = χ_zf f − χ_zf(σT + σ²P_2)u + [P̂(0), χ_zf]u
                                  + Σ c_i((1 − χ_zf)F_i(0) − χ_zf(F_i(σ) − F_i(0))).

The two new terms are bounded in H̄_b^(s+k−1,α+2) by Cς^(ϵ_0)|c|, by [[eq:iii-h-4-4]] with (A1), and by (A3). So
[[eq:i-c-6-9]] holds with the extra term Cς^(ϵ_0)|c| on the right.

*Step 2.* Fix η as there and moreover η ≤ ϵ_0. Now χ_tf P̂(σ)u = χ_tf(f − Σ c_iF_i(σ)), so ς²N_tf(σ̂)w gains the term
−S_ς(Σ c_iχ_tf F_i(σ)). After the multiplication by ς^(−(α+2))ς^(−2) it contributes at most

    C|c| max_i ‖χ_tf F_i(σ)‖_((s−2;k),(𝗋+α_++1,α+2,−η),ς)
        = Cς^η|c| max_i ‖χ_tf F_i(σ)‖_((s−2;k),(𝗋+α_++1,α+2+η,0),ς) ≤ Cς^η|c|,

by [[eq:iii-h-4-3]], [[lem:i-c-6-2]] (b), (d) and (A2). The conclusion of Step 2 becomes

    ‖u‖_(α,−η) ≤ C‖f‖′_(α+2,0) + C_(ρ_c)ς^η‖u‖_(α,0) + Cς^η|c|,

and inserted in the modified [[eq:i-c-6-9]],

    ‖u‖_(α,0) + |c| ≤ C(‖f‖′_(α+2,0) + |e|) + C′_(ρ_c)ς^η(‖u‖_(α,0) + |c|) + Cς^(ϵ_0)|c|;

the last two terms are absorbed for ς small.

(2) 𝒫(σ) is P̂(σ) ⊕ 0_(ℂ^J→ℂ^J), of index 0, plus a finite rank operator, as its columns lie in 𝒴_σ by (A2). So it
has index 0, and by [[eq:iii-h-4-1]] at k = 0 it is injective.

(3) Let R(σ) := P̂(σ)⁻¹. For σ ∈ Σ′ with |σ| ≤ c_0, and (f, e),

    𝒫(σ)⁻¹(f, e) = (R(σ)(f − Σ_i c_iF_i(σ)), c),     c = Ξ(σ)⁻¹((⟨R(σ)f, φ_(i′)⟩_h)_(i′) − e),
    Ξ(σ)_(i′i) := ⟨R(σ)F_i(σ), φ_(i′)⟩_h,

where Ξ(σ) is invertible because 𝒫(σ) is: if Ξ(σ)c = 0, then (−R(σ)Σ c_iF_i(σ), c) lies in the kernel of 𝒫(σ). Fix
σ_* ∈ Σ′ with |σ_*| ≤ c_0 and ϵ > 0 below the margins of the orders, and let, as in the proof of [[thm:i-c-6-4]] (4)
for this j,

    D := H̄^((s+ϵ−1;j),𝗋_(ς_*)+ϵ+α_++1),     Z := H̄^((s−ϵ;0),𝗋_(ς_*)−ϵ+α_+).

By [[thm:i-a-7-2]] (6), R(σ) : D → Z is strongly C^j near σ_*: for f ∈ D, σ ↦ R(σ)f is j times differentiable in Z,
with derivatives R^((i))(σ)f continuous in σ. The columns enter with an argument that depends on σ, which is the point
of [[rem:i-c-6-7]] (c). Each R^((i))(σ) : D → Z, i ≤ j, being strongly continuous, is bounded locally uniformly in σ
(Banach–Steinhaus), and σ ↦ F_l(σ) is C^j in norm into D by (A4), with M ≥ ϵ + α_+ + 1 and s′ ≥ s + ϵ − 1. Splitting
difference quotients as

    R(σ′)(F_l(σ′) − F_l(σ))/(σ′ − σ) + ((R(σ′) − R(σ))/(σ′ − σ)) F_l(σ)

gives the Leibniz rule, and by induction σ ↦ R(σ)F_l(σ) is C^j into Z. As ⟨·, φ_(i′)⟩_h is continuous on Z, Ξ(σ) is
C^j, hence so is Ξ(σ)⁻¹, and σ ↦ 𝒫(σ)⁻¹(f, e) is j times differentiable near σ_* in Z ⊕ ℂ^J for (f, e) ∈ D ⊕ ℂ^J.
Applying (σ∂_σ)^i to 𝒫(σ)𝒫(σ)⁻¹ = I gives [[eq:i-c-6-11]] with 𝒫 in place of P̂, and the argument of
[[sec:i-c-6-6]] applies. The entries of A_i := (σ∂_σ)^i 𝒫(σ) are those of [[lem:i-c-6-5]] in the first column and the
columns (σ∂_σ)^iF_l(σ), which map ℂ^J boundedly into ℋ^((s′;k),(𝗋+α_++1,α+2,0))_ς for every s′ by (A2); the rows are
constant. ∎

For the operator L̂_b, (Z_𝒫) is [[prop:iii-h-3-2]]. The index 0 at σ ≠ 0 takes the place of the adjoint estimate
[[eq:i-c-6-7]] in the proof of invertibility, since 𝒫 has as many columns as rows; [[thm:i-c-6-4]] needs
[[eq:i-c-6-7]] because there the numbers of columns and rows may differ.

**Corollary {#cor:iii-h-4-2}** ([Hin26, Proposition 10.7] in dimension 4 + 1.) Let b be near b_0, α as in
[[eq:iii-h-1-1]], α_+ ∈ ℝ, and the orders those of [[sec:i-c-6]] for L̂_b. For every k there are c_k > 0,
non-increasing in k, and C_k, uniform for b near b_0, such that for σ ∈ Σ_0 with |σ| ≤ c_k the operator
L̃_b(σ) : 𝒳_σ ⊕ 𝔟_ℂ ⊕ 𝒮_(1,ℂ) → 𝒴_σ ⊕ 𝔟_ℂ ⊕ 𝒮_(1,ℂ) is invertible, and

    ‖u‖_((s;k),(𝗋+α_+,α,0),ς) + |ḃ| + |S| ≤ C_k ‖L̃_b(σ)(u, ḃ, S)‖_((s−1;k),(𝗋+α_++1,α+2,0),ς),           {#eq:iii-h-4-5}

the norm on the right being that of the first component plus the moduli of the others. This is [Hin26, (10.28)].

*Proof.* Apply [[thm:iii-h-4-1]] with P̂ = L̂_b, Σ′ = Σ_0 and J = 11, with the components of f*_1 and f*_2 (converted
to ⟨·, ·⟩_h by a smooth bundle map) as rows, with the columns F_i := f̂_ḃ, f̂_S for basis elements, and with
ϵ_0 := ¼(1 − (α + 2)). The hypotheses on L̂_b are those of [[sec:iii-h-1]].

(A1): f̂(0) ∈ 𝒜³ ⊂ H̄_b^(∞,a) for a < 1 ([[lem:iii-h-2-3]]), and α + 2 + ϵ_0 < 1.

(A2): [[lem:iii-h-2-4]] (b), with l + 2 = α + 2 + η′ < 1 and ς_1 of [[eq:iii-h-2-4]], for the orders of
[[sec:i-c-6]]. These are of the kind of [[lem:ii-g1-4-6]]: s is constant, and 𝗋 equals a constant near the zero
section over sctf ([[sec:i-c-4-3]] and [[lem:i-a-7-1]]), as the proof of [[prop:ii-g1-4-7]] uses them.

(A3): [[lem:iii-h-2-4]] (c) with a = α + 2 and φ = φ_z of [[sec:i-c-6-4]], as |σ|^(1−(α+2)) ≤ |σ|^(ϵ_0).

(A4): [[lem:iii-h-2-4]] (d).

(Z_𝒫): [[prop:iii-h-3-2]].

*Uniformity in b.* The constants of the proof of [[thm:i-c-6-4]] (1) are uniform near b_0 ([[thm:i-c-7-1]] (2)); the
tf-normal operator does not depend on b ([[lem:iii-g4-1-1]]); the inverse of L̃_b(0) is bounded uniformly
([[prop:iii-h-3-2]]); and (A1)–(A3) hold uniformly by [[rem:iii-h-2-6]] with δ = ϵ_0, as α + 2 + ϵ_0 < 1 − δ and
|σ|^(1−(α+2)−δ) ≤ |σ|^(ϵ_0). ∎

**Corollary {#cor:iii-h-4-3}** (The low-energy range of [Hin26, Proposition 8.8], and [Hin26, (10.48)], in dimension
4 + 1.) After shrinking c_0 of [[cor:iii-h-4-2]], uniformly near b_0: for b near b_0 and σ ∈ Σ_0 with |σ| ≤ c_0, the
operator L̂_b(σ) : 𝒳_σ → 𝒴_σ is invertible, and for f ∈ 𝒴_σ, with (u, ḃ, S) := L̃_b(σ)⁻¹(f, 0, 0),

    L̂_b(σ)⁻¹f = u + ĝ^aug(σ)(ḃ) + ĥ^aug(σ)(S).                                                         {#eq:iii-h-4-6}

So [[thm:iii-h-4-1]] (3) applies to L̃_b on Σ_0, which gives [Hin26, (10.29)].

*Proof.* *Injectivity.* Let L̂_b(σ)v = 0 with v ∈ 𝒳_σ. For (ḃ, S) to be chosen put

    v′ := v − ĝ^aug(σ)(ḃ) − ĥ^aug(σ)(S) ∈ 𝒳_σ

([[lem:iii-h-2-5]] (b)). By [[lem:iii-h-2-5]] (c), L̃_b(σ)(v′, ḃ, S) = (0, ⟨v, f*⟩ − B̂(σ)(ḃ, S)), with

    B̂(σ)(ḃ, S) := ⟨ĝ^aug(σ)(ḃ) + ĥ^aug(σ)(S), f*⟩.

Let R be such that supp f* ⊂ {r ≤ R}. By [[lem:iii-h-2-5]] (d), on supp f*,

    ĝ^aug(σ)(ḃ) = iσ⁻¹(1 + O(σ))ġ(ḃ),     ĥ^aug(σ)(S) = (−σ⁻²(1 + O(σ)) + O(σ⁻¹))h(S) + O(σ⁻¹)h̆(S).

So with D(σ) := diag(σ I_𝔟, σ² I_(𝒮_1)) and [[eq:iii-h-3-1]],

    B̂(σ)D(σ) = diag(i I_𝔟, −I_(𝒮_1)) + O(|σ|) + O(|b − b_0|),

which is invertible for σ small and b near b_0. Choosing (ḃ, S) := B̂(σ)⁻¹⟨v, f*⟩ gives L̃_b(σ)(v′, ḃ, S) = 0, so
v′ = 0, ḃ = 0 and S = 0 ([[cor:iii-h-4-2]]), and v = 0.

*Invertibility.* L̂_b(σ) has index 0 ([[sec:iii-h-1]]).

*The formula [[eq:iii-h-4-6]].* By [[eq:iii-h-3-2]] and [[lem:iii-h-2-5]] (c),
L̂_b(σ)(u + ĝ^aug(σ)(ḃ) + ĥ^aug(σ)(S)) = f, and the left side of [[eq:iii-h-4-6]] is the unique solution in 𝒳_σ. ∎

**Corollary {#cor:iii-h-4-4}** ([Hin26, Proposition 8.8] in dimension 4 + 1 near b_0.) There is a neighbourhood ℬ of
b_0 such that for b ∈ ℬ and every σ ≠ 0 with Im σ ≥ 0, L̂_b(σ) : 𝒳_σ → 𝒴_σ is invertible and has trivial kernel on
every 𝒜^a.

*Proof.* For |σ| ≤ c_0 this is [[cor:iii-h-4-3]], on a neighbourhood of b_0 independent of σ; for |σ| ≥ c_0 it is
[[prop:iii-f2-4-1]] with this c_0, on its neighbourhood ℬ(c_0). Take ℬ to be the intersection. The kernel on 𝒜^a is
treated by [[lem:iii-f2-1-3]]. ∎

**Remark {#rem:s18-modes}** (Mode stability at low frequencies near b_0.) [[prop:iii-f2-4-1]] gives the invertibility of
L̂_b(σ) for |σ| ≥ c_0 on a neighbourhood ℬ(c_0) of b_0 that shrinks as c_0 → 0, so for b ≠ b_0 it does not cover the
range 0 < |σ| < c_0 ([[sec:iii-f2-5]]). [Hin26] takes this range from [AHW24, Theorem 6.1 (1)], which is proved on
Kerr from the Teukolsky equation and has no counterpart for the five-dimensional Myers–Perry family.
[[cor:iii-h-4-3]] and [[cor:iii-h-4-4]] cover the range in dimension 4 + 1, from the zero energy structure near b_0
([[prop:iii-h-3-2]]) through the uniform low-energy estimate; the perturbation does not degenerate, because c_0 is
uniform in b. With [[prop:iii-f2-4-1]] this gives [Hin26, Proposition 8.8] in dimension 4 + 1 on the fixed
neighbourhood ℬ of b_0.

### The spectral-side augmentation {#sec:iii-h-5}

This section is [Hin26, Section 10.1.3] in dimension 4 + 1. Fix φ_s ∈ C^∞([0, ∞)) equal to 0 on [0, 1] and to 1 on
[2, ∞), and for real σ ≠ 0 put χ_s := φ_s(ρ/|σ|); it is 1 near zf and 0 near scf.

**Definition {#def:iii-h-5-1}** ([Hin26, (10.38b), (10.39b)] in dimension 4 + 1.) For 0 ≠ σ ∈ [−1, 1] put

    ġ^sing(σ)(ḃ) := iσ⁻¹χ_s ġ(ḃ),     h^sing(σ)(S) := χ_s(−σ⁻²h(S) + iσ⁻¹h̆(S)),
    F′_ḃ(σ) := L̂_b(σ)ġ^sing(σ)(ḃ),     F′_S(σ) := L̂_b(σ)h^sing(σ)(S),
    F′_ḃ(0) := L_1ġ(ḃ),     F′_S(0) := L_2h(S) + L_1h̆(S),

and let L̃′_b(σ) be [[eq:iii-h-3-2]] with F′ in place of f̂ ([Hin26, (10.41)]).

**Lemma {#lem:iii-h-5-2}** (a) F′_ḃ(σ) = χ_s(L_1ġ − iσL_2ġ) + iσ⁻¹[L̂_b(σ), χ_s]ġ and
F′_S(σ) = χ_s(L_2h + L_1h̆ − iσL_2h̆) + [L̂_b(σ), χ_s](−σ⁻²h + iσ⁻¹h̆).

(b) The F′ satisfy (A1)–(A4) of [[thm:iii-h-4-1]] on Σ′ = Σ_0 ∩ ℝ, with ϵ_0 = ¼(1 − (α + 2)), uniformly near b_0
([[rem:iii-h-2-6]]).

(c) L̃′_b(0) is invertible, as in [[prop:iii-h-3-2]]. So the conclusions of [[cor:iii-h-4-2]] hold for L̃′_b(σ),
0 ≠ σ ∈ [−c_k, c_k], and, L̂_b(σ) being invertible there ([[cor:iii-h-4-3]]), so do those of [[thm:iii-h-4-1]] (3).

*Proof.* (a) L̂_b(σ)(χ_sv) = χ_sL̂_b(σ)v + [L̂_b(σ), χ_s]v, with L̂_b(σ) = L_0 − iσL_1 − σ²L_2, L_0ġ = 0, L_0h = 0 and
L_1h + L_0h̆ = 0. So L̂_b(σ)(iσ⁻¹ġ) = L_1ġ − iσL_2ġ, and

    L̂_b(σ)(−σ⁻²h + iσ⁻¹h̆) = −σ⁻²L_0h + iσ⁻¹(L_1h + L_0h̆) + L_2h + L_1h̆ − iσL_2h̆ = L_2h + L_1h̆ − iσL_2h̆.

(b) [L̂_b(σ), χ_s] = [L_0, χ_s] − iσ[L_1, χ_s] has coefficients supported in {ς ≤ ρ ≤ 2ς}, with
[L_0, χ_s] ∈ ρ²Diff_b^1 and [L_1, χ_s] ∈ ρC^∞, their coefficients bounded with their b-derivatives uniformly in ς. As
ρ ∼ ς there, each commutator term is O(ρ³) with its b-derivatives: ς⁻¹ρ²ρ² and ρρ² for ġ (weight 2; ρ³ for ġ(0, Ȧ)),
and ς⁻²ρ²ρ³, ς⁻¹ρρ³, ς⁻¹ρ²ρ² and ρρ² for h and h̆. The main terms are χ_s times 𝒜³ (the terms free of σ, by
[[eq:iii-h-2-2]]) and ςχ_s𝒜⁴. Hence F′(σ) is supported in {ρ ≥ ς}, that is, where ρ̂ ≥ c, where ρ_scf ≥ c′ and
ρ_tf ∼ ρ; and it is O(ρ³) there, together with its b-derivatives and its σ∂_σ-derivatives (σ∂_σ falls on φ_s(ρ/ς),
giving a bounded function supported where ρ ∼ ς, and on the powers of σ). As in [[lem:iii-h-2-4]] (b), its
H^(k,(M,β_tf,0))_(b,ς)-norms are bounded for β_tf < 3, and (A2) follows by [[eq:ii-g1-4-5a]]. (A1): F′(0) ∈ 𝒜³ by
[[eq:iii-h-2-2]]. (A3): on supp χ_zf ⊂ {ρ ≥ 2ς}, χ_s = 1 and dχ_s = 0, so χ_zf(F′(σ) − F′(0)) equals
−iσχ_zfL_2ġ, resp. −iσχ_zfL_2h̆, of norm O(|σ|) in H̄_b^(p,α+2), as L_2ġ, L_2h̆ ∈ 𝒜⁴. (A4): for σ ≠ 0, F′(σ) is
supported in {ρ ≥ ς}, which is compact in X for fixed σ, and is smooth in σ.

(c) F′(0) is [[eq:iii-h-2-2]] without the terms L_0w, and the proof of [[prop:iii-h-3-2]] used [[eq:iii-h-2-2]] only
through them; the index argument is unchanged. ∎

**Remark {#rem:iii-h-5-3}** ([Hin26, Remark 10.8] in dimension 4 + 1.) σġ^sing(σ) = iχ_sġ and
σ²h^sing(σ) = χ_s(−h + iσh̆). There are no correction terms ([Hin26, (10.38a), (10.39a)], which [Hin26] obtains from
its Proposition 9.30) and no logarithmic terms σ log|σ|, since the naive columns are already of tf-order 3 (they are
O(ρ_tf³)), above the tf-weight α + 4 < 3 of the target for μ_b ([[lem:iii-h-2-4]] (b)). The spacetime counterparts
behave alike: by [[lem:iii-h-2-5]] (b), ℱ(∂_(t_*)ġ^aug)(σ) = −iσĝ^aug(σ) = Φ(σr)ġ for r ≥ 1, which equals ġ at
σ = 0 and carries no logarithm (the t_*⁻¹- and log t_*-terms of [Hin26, (10.13)] do not arise).

### 2-admissibility: setting, orders and the statement {#sec:iii-h1-1}

*Spaces.* M̃_0 is the 3b-compactification of ℝ_(t_*) × ℝ⁴ of [[sec:ii-a-5]] (the space [ℝ̄⁴; k⁺, k⁻] of [Hin26] in
dimension 4 + 1), with boundary hypersurfaces sf and K^±; M_0 := cl_(M̃_0){r ≥ r_0}, with X = {r ≥ r_0} as in
[[sec:iii-h-1]]; and ([Hin26, (10.2)] in dimension 4 + 1)

    Ω := cl_(M_0){t_* ≥ 1},     Ω_− := cl_(M_0){t_* ≤ 1}.

On M_0, ρ_sf = r⁻¹ and, near K⁺, ρ_K = r/(t_* + r) are defining functions, and r∂_(t_*), r∂_r, ∂_ω span 𝒱_3b over
C_b^∞ (equivalently ⟨x⟩∂_(t_*), ⟨x⟩∂_(x_i): the scaled bounded geometry of (S9) in [[sec:ii-a-3]] with the scale ⟨x⟩
in all directions). We write

    H^((𝗌;k),(β,γ))_(3b;b) := ρ_sf^β ρ_K^γ H^((𝗌;k))_(3b;b),

with H^((𝗌;k))_(3b;b) of [[lem:ii-a-5-2]] (tested with up to k of ∂_(t_*), t_*∂_(t_*), ⟨x⟩∂_x), on L²(|dt_* dx|). On Ω
the spaces are supported at {t_* = 1} and extendible at {r = r_0} (superscript •,−); on M_0 they are extendible at
{r = r_0}; on Ω_− they are extendible (bar). As ρ_K ≤ 1, H^((𝗌;k),(β,0))_(3b;b) ⊂ H^((𝗌;k),(β,−ℓ))_(3b;b) for ℓ ≥ 0,
and ∂_(t_*) = ρ_sf · r∂_(t_*) maps H^((𝗌;k),(β,γ))_(3b;b) to H^((𝗌−1;k),(β+1,γ))_(3b;b).

*The operator and the weight.* L_b is the operator of [[sec:iii-h-1]], b near b_0, and throughout

    α_sf ∈ ℝ,     α_sf + 2 ∈ (0, 1),                                                                     {#eq:iii-h1-1-1}

the weight α of [[eq:iii-h-1-1]]. By [[lem:ii-a-5-1]] a spacetime sf-weight β with K-weight 0 is the spectral weight
(· + β, β, 0), so the spectral weight α of [[sec:iii-h-1]] is α_sf; the tf-weight α_sf + 2 of [[def:ii-c-2-7]] is the
weight α_sf + 3/2 of [Hin26]. In this half of the chapter 𝒫 denotes the compactified phase space of [[sec:i-b-2-4]]
(the augmented operator 𝒫(σ) of [[thm:iii-h-4-1]] is not used here), and Φ_(z_0) : 𝒫 → ³ᵇS*_(K⁺)M_0, always written
with its subscript, the map of [[def:ii-b-2-2]], under which characteristic sets and flows correspond
([[lem:ii-b-2-3]]) and fibre infinity of 𝒫 goes to {σ = 0}; it is not the function Φ of [[lem:iii-h-2-5]].

**Definition {#def:iii-h1-1-1}** (The orders.) 𝒪_c = 𝒪_c(α_sf) is the set of t_*-translation-invariant
𝗌 ∈ C^∞(³ᵇS*M̃_0) that are stationary-L_b-admissible with weights α_sf, −2 and margin 1 ([[def:ii-c-2-4]]) and
moreover satisfy:

(C1) 𝗌 is constant, =: s_c, on {σ = 0} = Φ_(z_0)(fibre infinity of 𝒫);

(C2) 𝗌 is constant over {r ≤ r_2 − δ_0}, with the radii r_2, δ_0 of [[sec:i-a-1-1]] that [[sec:i-b-1-4]] uses;

(C3) the monotonicity of [[def:ii-c-2-4]] (1) holds on a neighbourhood of the characteristic set, not only on it.

(C2) follows from [[def:ii-c-2-4]] (3), as r_Γ > r_h > r_2; it is listed because [[sec:i-b-1-4]] uses it. 𝒪_c is a
restriction of the orders of [[def:ii-c-2-7]], which asks its (3) for all admissible orders; the orders with which
this 2-admissibility is used lie in 𝒪_c ([[lem:iii-i-5-1]]).

For 𝗌 ∈ 𝒪_c and z_0 = ±1 put S_(z_0) := 𝗌 ∘ Φ_(z_0) on 𝒫. The order induced at σ ∈ ℝ ∖ 0 (by [[lem:ii-a-5-1]], the
restriction of 𝗌 to −σ dt_* + T*X̃) is 𝗌_σ(x, ξ) = S_(z_0)(x, ξ/|σ|), with z_0 the sign fixed by the conventions of
[[lem:ii-a-5-1]] and [[def:ii-b-2-2]] (by [[def:ii-c-2-4]] (2) the choice is immaterial): 𝗌 is homogeneous of degree 0
in the 3b covector (σ_3b, ξ_3b, η_3b) = (−rσ, rξ, rη) (proof of [[lem:ii-c-2-6]]). By (C1), 𝗌_σ = s_c at fibre
infinity, and its decay order is 𝗋_σ := 𝗌_σ on the face over ∂X.

**Lemma {#lem:iii-h1-1-2}** (The induced orders.) Let 𝗌 ∈ 𝒪_c, let 𝗋 := S_(z_0) on the face over ∂X, and let
𝖻 := S_(z_0).

(a) For real σ ≠ 0 the order pairs (s_c, 𝗋_σ) and (s_c + 1, 𝗋_σ + 1) are admissible for σ in the sense of (O1)–(O3)
of [[def:i-a-admissible]], with the weights α_sf + 1 and α_sf respectively, that is, with the decay order
𝗌_σ + α_sf + 1 in both cases, and with margin at the thresholds.

(b) 𝗋 (with the weight α_sf + 1) and 𝖻 are admissible for z_0 in the sense of [[sec:i-b-1-4]], and
𝗋_σ(x, ξ) = 𝗋(x, ξ/|σ|) is the order of [[sec:i-b-8-4]] at the semiclassical parameter |σ|⁻¹.

(c) 𝗋_σ is the dilated order 𝗋_ς of [[sec:i-c-6-1]], ς = |σ|; and (s_c + 1, 𝗋 + 1) with the weight α_+ := α_sf is
admissible at σ_0 = ±1. This is what [[cor:iii-h-4-2]] and [[thm:iii-h-4-1]] (3) use on Σ′ = Σ_0 ∩ ℝ, where the
rescaled frequency σ/|σ| is ±1. Off the real axis the orders of [[sec:i-c-6]], admissible for |σ_0 ∓ 1| < ¼, are
used, and only through pairings ([[sec:iii-h1-4]]).

*Proof.* Under Φ_(z_0) the radial sets correspond: ∂R_(ℋ⁺) (at fibre infinity, inside {σ = 0}), ∂R_(∂K⁺,in) and
∂R_(∂K⁺,out) are the images of ∂ℛ_±, R_(z_0,in) and R_out, as sources and sinks of corresponding flows
([[lem:ii-b-2-3]]); and the thresholds agree: ϑ^(3b)_in = ϑ_in and ϑ_out ≤ 2S̄ ([[lem:ii-c-2-6]]).

*Constancy.* Near ∂ℛ_± by (C1); near Γ_(z_0) and over {r_0 − δ_0 ≤ r ≤ r_2 − δ_0} by [[def:ii-c-2-4]] (3) and (C2);
near R_(z_0,in) and R_out by [[def:ii-c-2-4]] (5)–(6).

*Monotonicity on a neighbourhood of the characteristic set.* This is (C3). As 𝗌 is t_*-invariant and G is
t_*-independent, 𝖧_G𝗌 at σ = z_0 is 𝖧_(G_(z_0))S_(z_0) identically, and the fields of [[eq:ii-b-1-4]] and of
[[sec:i-b-1-4]] are, up to terms vanishing on the characteristic set (which shrink the neighbourhood), positive
multiples of these Hamilton fields. So (C3) transfers to a neighbourhood in 𝒫 ([[lem:ii-b-2-3]] relates the fields on
Σ_(z_0)).

*Thresholds.* By [[def:ii-c-2-4]] (4)–(6) with α_K = −2 and margin 1: s_c > 3/2 + ϑ_ℋ;
𝗋 + α_sf > ½(−1 + ϑ_in) − 1 at R_(z_0,in); and 𝗋 + α_sf < ½(−1 + ϑ_out) − 3 ≤ −½ + S̄ − 3 at R_out. Hence 𝗋 + α_sf + 1
lies above ½(−1 + ϑ_in) at R_(z_0,in) and below −½ + S̄ at R_out, with margin, and s_c, s_c + 1 > ½ + ϑ_ℋ. So (O3) and
the thresholds of [[sec:i-b-1-4]] hold.

(b) is then [[sec:i-b-1-4]], and the identification of 𝗋_σ is [[sec:i-b-8-4]]. (a): [[sec:i-b-1-4]] asks more than (O2),
and (s_c, 𝗋_σ) is admissible for σ_0 = z_0|σ| for every |σ| > 0 ([[sec:i-b-1-4]]), that is, for every real σ ≠ 0.
(c): [[lem:i-c-6-2]] (c), 𝗋 being admissible for z_0 and constant near R_out with the threshold there. ∎

*Neighbourhoods.* ℬ is the neighbourhood of b_0 of [[cor:iii-h-4-4]] (invertibility of L̂_b(σ) for all σ ≠ 0 with
Im σ ≥ 0), on which [[cor:iii-h-4-2]] and [[cor:iii-h-4-3]] hold. For k ∈ ℕ_0, ℬ_k is the set of b ∈ ℬ at which (Γ.4)
of [[sec:i-b-1-5]] holds for 2L_b, for z_0 = ±1, with a stationary fibre inner product h_Γ such that
δ_Γ(0) < 1/(2(k + 1)) ([[eq:i-b-1-4]]). By [[prop:iii-f-4-1]], which gives δ_Γ(0) as small as wished on a neighbourhood
of b_0 and at b_0 for every bound, b_0 ∈ ℬ_k and ℬ_k contains a neighbourhood of b_0, for every k.

**Theorem {#thm:iii-h1-1-3}** ([Hin26, Theorem 10.1] in dimension 4 + 1.) Let α_sf be as in [[eq:iii-h1-1-1]], let
k ∈ ℕ_0, b ∈ ℬ_k and 𝗌 ∈ 𝒪_c. For f ∈ H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω, |dt_* dx|; S²T*)^(•,−) the forward solution u of
L_bu = f satisfies

    ‖u‖_(H^((𝗌−1;k),(α_sf,−2))_(3b;b)(Ω)^(•,−)) ≤ C‖f‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).           {#eq:iii-h1-1-2}

So, in the relaxed form of [[def:ii-c-2-7]] with margin d_ℵ = 1, L_b is 2-admissible with sf-weight α_sf, sf-loss 0
and margin 1, for orders in 𝒪_c, at every b ∈ ⋂_k ℬ_k, in particular at b = b_0: (1) of [[def:ii-c-2-7]] holds by the
definition of ℬ_k (at b_0 by [[prop:iii-f-4-1]]), (2) by [[prop:iii-f1-3-3]] at the weight α_sf + 2, and (3) by
[[eq:iii-h1-1-2]].

[Hin26, (10.3)] has 𝗌 − 1 and the weights (α_sf − δ, −2) with δ > α_sf + 3/2; [[eq:iii-h1-1-2]] has δ = 0. The proof
is in [[sec:iii-h1-7]].

**Remark {#rem:s18-every-k}** (Every k on a fixed neighbourhood.) By [[prop:iii-f-4-1]] alone, ℬ_k contains a
neighbourhood of b_0 that may shrink as k grows. By [[cor:iii-h2-1-2]], which rests on the trapping bound of
[[prop:iii-h2-1-1]] at every b of a fixed neighbourhood, from a frame built from the null geometry alone, the fixed
neighbourhood B̄_1 of b_0 of [[sec:iii-h2-0]] satisfies B̄_1 ⊂ ℬ_k for every k ∈ ℕ_0. So [[thm:iii-h1-1-3]] holds for
every k at every b ∈ B̄_1, and L_b is 2-admissible with sf-weight α_sf, sf-loss 0 and margin 1 at every b ∈ B̄_1. By
[[thm:iii-h2-2-1]], for the order 𝗌 of (B4) of [[sec:iii-h2-0]] the constant C of [[eq:iii-h1-1-2]] can moreover be
taken independent of b ∈ B̄_1. For the other orders of 𝒪_c no uniformity in b is claimed: 𝒪_c is defined relative to
L_b, and an order of 𝒪_c at one b need not lie in 𝒪_c at another.

### The representation of the forward solution {#sec:iii-h1-2}

By density ([Hin26, p. 212]) it suffices to take for f the restriction to {r ≥ r_0} of a smooth section of S²T* with
compact support in {t_* > 1}, so that f is smooth up to {r = r_0} and t_* ≥ t_1 > 1 on supp f. (An element of the
space is the restriction of a distribution F supported in {t_* ≥ 1}; the translates of F by τ > 0 in t_*, supported in
{t_* ≥ 1 + τ}, converge to F as τ ↓ 0, and each is approximated by smooth sections with compact support in {t_* > 1}.
Sections that vanish near {r = r_0} would not do: they are not dense, the spaces being extendible there.) Then
f̂(σ) := ∫ e^(iσt_*) f dt_* is entire with values in the smooth sections on X supported in a fixed compact subset
of X̄ ∖ ∂X, and ‖f̂(σ)‖ ≤ C_M⟨σ⟩^(−M)e^(−t_1 Im σ) in every norm, for Im σ ≥ 0. Fix k, b ∈ ℬ_k and 𝗌 ∈ 𝒪_c. Let
c ∈ (0, ς_1], with ς_1 of [[eq:ii-g1-4-5a]], be at most the constants c_(j,k′) of [[thm:iii-h-4-1]] (3) for L̃_b on
Σ′ = Σ_0 ∩ ℝ, with the orders (s_c + 1, 𝗋 + 1) of [[lem:iii-h1-1-2]] (c), for j + k′ ≤ k ([[cor:iii-h-4-3]]); and fix
χ ∈ C_c^∞([0, c)) with χ = 1 on [0, c/2]. Put

    𝒞_− := (−∞, −c/2],     𝒞_0 := (c/2)e^(i[π,0]),     𝒞_+ := [c/2, ∞).

**Lemma {#lem:iii-h1-2-1}** ([Hin26, (10.4)].) The forward solution u of L_bu = f satisfies
û(σ) = L̂_b(σ)⁻¹f̂(σ) for Im σ > 0, and

    u(t_*, ·) = (2π)⁻¹ ∫_(𝒞_−∪𝒞_0∪𝒞_+) e^(−iσt_*) L̂_b(σ)⁻¹ f̂(σ) dσ                                   {#eq:iii-h1-2-1}

as distributions on ℝ_(t_*) × X°.

*Proof.* We follow the proof of [Hin26c, Theorem 12.2], as [Hin26, p. 200] does, with the following inputs.

*High energy.* For |σ| ≥ C_0 with Im σ ≥ 0, L̂_b(σ) is invertible ([[thm:i-b-1-3]] (3)), and
‖L̂_b(σ)⁻¹g‖ ≤ C|σ|^(−1+δ)‖g‖ in the norms of [[eq:i-b-1-8]] (j = k = 0), with δ = δ_Γ(Im σ − ϵ) ≤ 1, uniformly for
Im σ in compact sets, and δ = 0 for Im σ large. At fixed |σ| the semiclassical norms are equivalent to the fixed ones,
with constants polynomial in |σ|.

*Paley–Wiener.* Let γ ≥ C_0 be large and ũ(t_*) := (2π)⁻¹∫_(Im σ=γ) e^(−iσt_*)L̂_b(σ)⁻¹f̂(σ) dσ, absolutely
convergent by the decay of f̂. By holomorphy on {Im σ ≥ γ} and the bounds there, the integral does not depend on
γ′ ≥ γ; for t_* < t_1 the integrand is O(⟨σ⟩^(−M)e^((t_*−t_1)γ′)), so letting γ′ → ∞ gives ũ = 0 for t_* < t_1. As
∂_(t_*) becomes −iσ ([[eq:iii-a-2-2]]), L_bũ = f by Fourier inversion on Im σ = γ. L̂_b(σ)⁻¹f̂(σ) lies in 𝒳_σ for
every admissible choice of orders ([[thm:i-a-7-2]] (3): the kernel and the range do not depend on them), so ũ is
smooth, with growth e^(γt_*). ũ − u solves L_b(ũ − u) = 0 and vanishes for t_* < 1, so ũ = u by the uniqueness of
[[prop:ii-e-3-4]] on each slab {t_* ≤ T}.

*Shifting the contour.* L̂_b(σ)⁻¹ exists for every σ ≠ 0 with Im σ ≥ 0 ([[cor:iii-h-4-4]]), is holomorphic in
Im σ > 0 ([[thm:i-a-7-2]] (6)), and is polynomially bounded for |Re σ| ≥ C_0, uniformly in Im σ ∈ [0, γ]. With the
decay of f̂, Cauchy's theorem moves the contour to Im σ = γ″ ∈ (0, γ), and then to 𝒞_− ∪ 𝒞_0 ∪ 𝒞_+: on
|Re σ| ≥ c/2, L̂_b(σ)⁻¹ is continuous up to the real axis ([[thm:i-a-7-2]] (6) at each real σ_* ≠ 0, where it is
invertible), with the polynomial bounds above for dominated convergence. ∎

### High frequencies {#sec:iii-h1-3}

This section is [Hin26, Lemma 10.9] in dimension 4 + 1.

**Lemma {#lem:iii-h1-3-1}** Let

    u_hi(t_*, ·) := (2π)⁻¹ ∫_(ℝ∖[−c/2,c/2]) e^(−iσt_*)(1 − χ(|σ|)) L̂_b(σ)⁻¹ f̂(σ) dσ.

Then, for every ϵ > 0 below the margins of [[lem:iii-h1-1-2]] (a),

    ‖u_hi‖_(H^((𝗌;k),(α_sf+1−2ϵ,0))_(3b;b)(M_0)) ≤ C_ϵ ‖f‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).       {#eq:iii-h1-3-1}

This is [Hin26, (10.44)] with α_sf + 1 − 2ϵ in place of α_sf; the weight α_sf would need a stronger threshold at the
incoming radial set ([[sec:s18-remarks]]).

*Proof.* Write β := α_sf + 1. The transform û_hi is supported in |σ| ≥ c/2, and on c/2 ≤ |σ| ≤ 1 the sc-b norm at σ
and the semiclassical norm at the semiclassical parameter |σ|⁻¹ are both equivalent to the fixed norm, uniformly on this
compact set (the parameterised calculus, (S7) in [[sec:ii-a-3]]). So by [[lem:ii-a-5-2]],

    ‖u_hi‖² ∼ Σ_(j_1+j_2≤k) ∫_(|σ|≥c/2) ‖σ^(j_1)(σ∂_σ)^(j_2) û_hi(σ)‖²_((𝗌_σ;k−j_1−j_2),𝗌_σ+β,𝗌_σ) dσ,

in the semiclassical norms of [[lem:ii-a-5-2]] at the semiclassical parameter |σ|⁻¹. By Leibniz, (σ∂_σ)^(j_2)û_hi is a
combination of bounded functions of σ (from 1 − χ) times ((σ∂_σ)^(j′)L̂_b⁻¹)(σ)(σ∂_σ)^(j_3)f̂(σ), j′ + j_3 ≤ j_2.

*|σ| ≥ C_0.* Apply [[thm:i-b-1-3]] (5) with the orders of [[lem:iii-h1-1-2]] (b), the weight β, j′ and k − j_1 − j_2,
and with a parameter ϵ′ > 0 in place of the ϵ there: with δ := δ_Γ(−ϵ′),

    ‖(σ∂_σ)^(j′) L̂_b(σ)⁻¹ g‖_((s_c;k−j_1−j_2),𝗋+β,𝖻;+) ≤ C|σ|^(−1+(j′+1)δ) ‖g‖_((s_c−1;k−j_1−j_2+j′),𝗋+β+1,𝖻;+),

the left side bounding the norm above (s_c + j′ ≥ s_c, and the subscript + only adds terms). The norm with subscript +
on the right is at most C Σ_(j_4≤k−j_1−j_2+j′) |σ|^(j_4) ‖g‖_((s_c−1;k−j_1−j_3−j_4),𝗋+β+1,𝖻), since it tests in
addition with multiplication by |σ|; and (s_c − 1)-norms are bounded by s_c-norms. As δ_Γ is continuous and
δ_Γ(0) < 1/(2(k + 1)) at b ∈ ℬ_k, ϵ′ > 0 can be fixed with (k + 1)δ ≤ 1. (ϵ′ is not the ϵ of the statement.) Then
|σ|^(2(j_1−1+(j′+1)δ+j_4)) ≤ |σ|^(2(j_1+j_4)), and the integrand is bounded by

    C Σ |σ|^(2(j_1+j_4)) ‖(σ∂_σ)^(j_3) f̂(σ)‖²_((𝗌_σ;k−j_1−j_3−j_4),𝗌_σ+β+1,𝗌_σ),     j_1 + j_4 + j_3 ≤ k.

*c/2 ≤ |σ| ≤ C_0.* L̂_b(σ) is invertible there ([[cor:iii-h-4-4]]). The induced pairs (s_c, 𝗋_σ), σ in this compact
set, depend continuously on σ in C^∞ and are admissible at σ with the weight β ([[lem:iii-h1-1-2]] (a)), with margins
and constancy neighbourhoods uniform, as 𝗋_σ(x, ξ) = S_(z_0)(x, ξ/|σ|) with |σ| in a compact subset of (0, ∞). So
[[thm:i-a-7-2]] (1) gives [[eq:i-a-7-1]] uniformly at these orders, and [[eq:i-a-7-3]] holds likewise, since the proof
of [[thm:i-a-7-2]] (4) gives constants that are uniform for such families. The last terms drop uniformly. Otherwise
there are σ_n → σ_* and u_n of norm 1 at the orders 𝗋_(σ_n) with ‖L̂_b(σ_n)u_n‖ → 0. As 𝗋_(σ_n) → 𝗋_(σ_*)
uniformly, the u_n are bounded in the fixed space of order 𝗋_(σ_*) − ϵ for n large, and a subsequence converges weakly
there and strongly in H̄^(−M,−M). The limit is nonzero by the uniform [[eq:i-a-7-1]], and it lies in the kernel of
L̂_b(σ_*) on a space of an admissible order (𝗋_(σ_*) − ϵ, the margins exceeding ϵ); this contradicts the invertibility
([[cor:iii-h-4-4]]; the kernel does not depend on the orders, [[thm:i-a-7-2]] (3)). For [[eq:i-a-7-3]] the argument is
that of the proof of [[thm:i-a-7-2]] (6). Then [[eq:i-a-7-6]] holds at each σ with the orders (s_c, 𝗋_σ), uniformly,
the inverse bound being obtained as above at each raised order (s_c + l, 𝗋_σ), l ≤ j′, that the product formula uses:
∂_σ^(j′)L̂_b⁻¹ is a sum of products of L̂_b⁻¹ and σ-derivatives of L̂_b (on test sections, σ ↦ L̂_b(σ)⁻¹g is smooth in
the fixed spaces of the orders of [[lem:i-a-7-1]], by [[thm:i-a-7-2]] (6)), each factor is bounded uniformly between
the spaces at σ, and a σ-derivative of L̂_b costs one b-derivative. So the output is bounded in the decay order
𝗋_σ + β by the input in 𝗋_σ + β + 1. (σ∂_σ)^(j′) is a combination of σ^i∂_σ^i, i ≤ j′, with bounded coefficients.
The integrand is bounded as before, without powers of |σ|.

*Conclusion.* By [[lem:ii-a-5-2]] again, with the weight β + 1 = α_sf + 2, the integral is at most
C‖f‖²_(H^((𝗌;k),(α_sf+2,0))_(3b;b)). This bounds u_hi in H^((𝗌;k),(β,0))_(3b;b)(M_0), hence in
H^((𝗌;k),(β−2ϵ,0))_(3b;b)(M_0), as ρ_sf = r⁻¹ ≤ r_0⁻¹ on M_0. ∎

u_hi is not supported in Ω, so its norm is taken on M_0 ([Hin26, footnote 100]). The loss of derivatives (regularity
𝗌 for f and for u_hi) is the loss at the trapped set.

### Low frequencies: the regular part {#sec:iii-h1-4}

This section is [Hin26, Lemmas 10.10–10.11] in dimension 4 + 1. For |σ| ≤ c with σ ≠ 0 and Im σ ≥ 0 put
([[def:iii-h-3-1]], [[cor:iii-h-4-2]])

    (û_(reg,1)(σ), b̂_1(σ), Ŝ_1(σ)) := L̃_b(σ)⁻¹(f̂(σ), 0, 0).                                           {#eq:iii-h1-4-1}

By [[eq:iii-h-4-6]], for these σ,

    L̂_b(σ)⁻¹ f̂(σ) = û_(reg,1)(σ) + ĝ^aug(σ)(b̂_1(σ)) + ĥ^aug(σ)(Ŝ_1(σ)).                               {#eq:iii-h1-4-2}

*Properties.* By the formula in the proof of [[thm:iii-h-4-1]] (3), with e = 0,
(b̂_1, Ŝ_1) = Ξ(σ)⁻¹(⟨R(σ)f̂(σ), φ_(i′)⟩_h)_(i′), with R = L̂_b⁻¹ and Ξ(σ)_(i′i) = ⟨R(σ)F_i(σ), φ_(i′)⟩_h. R is
holomorphic in Im σ > 0 ([[thm:i-a-7-2]] (6)), the columns F_i = f̂_ḃ, f̂_S are holomorphic there with values in every
H̄_b^(p,M) ([[lem:iii-h-2-4]] (d)), and f̂ is entire. So b̂_1, Ŝ_1 and
û_(reg,1) = R(σ)(f̂(σ) − Σ_i (b̂_1(σ), Ŝ_1(σ))_i F_i(σ)), with (b̂_1, Ŝ_1)_i the coefficient of the column F_i (paired
with any φ ∈ C_c^∞(X°)), are holomorphic in Im σ > 0, continuous down to [−c, c] ∖ 0 ([[thm:i-a-7-2]] (6) at real
σ_*), and bounded uniformly by [[eq:iii-h-4-5]]. Here any orders of [[sec:i-c-6]] may be used, since these are
statements about pairings with test sections, which do not depend on the orders; and
‖f̂(σ)‖_((s_c;k),(𝗋+α_sf+2,α_sf+2,0),|σ|) is bounded for |σ| ≤ 1, as f̂(σ) is supported in a fixed compact subset of
X̄ ∖ ∂X ([[lem:i-c-6-2]] (a)).

**Lemma {#lem:iii-h1-4-1}** (The regular part.)
u_reg(t_*, ·) := (2π)⁻¹ ∫_(𝒞_−∪𝒞_0∪𝒞_+) e^(−iσt_*) χ(|σ|) û_(reg,1)(σ) dσ satisfies

    ‖u_reg‖_(H^((𝗌+1;k),(α_sf,0))_(3b;b)(M_0)) ≤ C‖f‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).            {#eq:iii-h1-4-3}

[Hin26] has 𝗌 on the left and 𝗌 − 1 on the right; here f is used at its regularity 𝗌, and the gain is the elliptic
one ([[sec:s18-remarks]]).

*Proof.* As χ = 1 on [0, c/2] and the integrand is bounded near 0 and holomorphic inside 𝒞_0, Cauchy's theorem moves
𝒞_0 to [−c/2, c/2] (pairing with test sections; the small semicircle around 0 contributes o(1)). So
û_reg = χû_(reg,1) on ℝ, supported in [−c, c]. By [[lem:ii-a-5-2]] with the order 𝗌 + 1 and the weight α_sf, and
[[lem:ii-a-5-3]] (the norms of [[def:i-c-6-1]]),

    ‖u_reg‖² ∼ Σ_(j≤k) ∫_(−c)^c ‖(σ∂_σ)^j(χû_(reg,1))‖²_((s_c+1;k−j),(𝗋+1+α_sf,α_sf,0),|σ|) dσ.

By [[lem:iii-h1-1-2]] (c) and [[cor:iii-h-4-3]], [[thm:iii-h-4-1]] (3) applies to L̃_b on Σ′ = Σ_0 ∩ ℝ with the orders
(s_c + 1, 𝗋 + 1) and α_+ = α = α_sf. By Leibniz and [[eq:iii-h-4-2]], for |σ| ≤ c,

    ‖(σ∂_σ)^j(χû_(reg,1))‖_((s_c+1;k−j),(𝗋+1+α_sf,α_sf,0),|σ|)
        ≤ C Σ_(j_2≤j) ‖(σ∂_σ)^(j_2) f̂(σ)‖_((s_c;k−j_2),(𝗋+1+α_sf+1,α_sf+2,0),|σ|),

where j_2 counts the derivatives that fall on f̂; each derivative that falls on L̃_b⁻¹ costs one order of b-regularity
of f̂. The decay order 𝗋 + α_sf + 2 and the regularity s_c are those of 𝗌 + α_sf + 2 and 𝗌, so by [[lem:ii-a-5-2]] with
the weight α_sf + 2 the integral is at most C‖f‖²_(H^((𝗌;k),(α_sf+2,0))_(3b;b)). ∎

**Lemma {#lem:iii-h1-4-2}** (The coefficients.)

    Σ_(j≤k) ∫_(−c)^c (|(σ∂_σ)^j b̂_1(σ)|² + |(σ∂_σ)^j Ŝ_1(σ)|²) dσ ≤ C‖f‖²_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).

*Proof.* As for [[lem:iii-h1-4-1]], with the moduli of the second and third components in [[eq:iii-h-4-2]]. ∎

### The singular part {#sec:iii-h1-5}

This section is [Hin26, Lemma 10.12] in dimension 4 + 1. With ĝ^aug, ĥ^aug of [[eq:iii-h-2-6]] and
𝒞 := 𝒞_− ∪ 𝒞_0 ∪ 𝒞_+ put

    v_ġ(t_*, ·) := (2π)⁻¹ ∫_𝒞 e^(−iσt_*) χ(|σ|) ĝ^aug(σ)(b̂_1(σ)) dσ,
    v_h(t_*, ·) := (2π)⁻¹ ∫_𝒞 e^(−iσt_*) χ(|σ|) ĥ^aug(σ)(Ŝ_1(σ)) dσ.                                     {#eq:iii-h1-5-1}

By [[lem:iii-h1-2-1]], [[eq:iii-h1-4-2]] and χ(|σ|) = 1 on 𝒞_0,

    u = u_hi + u_reg + u_sing,     u_sing := v_ġ + v_h.                                                  {#eq:iii-h1-5-2}

On 𝒞_0, |e^(−iσt_*)| = e^(t_* Im σ), so [[eq:iii-h1-5-1]] grows at most like e^(ct_*/2); the poles of ĝ^aug and ĥ^aug
at 0 prevent moving 𝒞_0 to the real axis. Their t_*-derivatives do not have these poles.

**Lemma {#lem:iii-h1-5-1}** (Bounds for derivatives.) For every p ∈ ℕ_0, with k and c as in [[sec:iii-h1-2]],

    ∂_(t_*)v_ġ ∈ H^((p;k),(α_sf+1,0))_(3b;b)(M_0),     ∂²_(t_*)v_h ∈ H^((p;k),(α_sf+2,0))_(3b;b)(M_0),   {#eq:iii-h1-5-3}

with norms at most C_p‖f‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).

[Hin26, (10.51)–(10.52)] have the sf-weights −½ − ϵ and ½ − ϵ and the regularity 𝗌 only, under the condition
𝗌′ + α′ < −½ at R_out. Here every constant regularity is allowed and no condition at R_out is needed, as the transforms
decay rapidly at scf.

*Proof.* *The transforms.* Differentiating [[eq:iii-h1-5-1]] under the integral, ∂_(t_*) brings a factor −iσ, and by
[[eq:iii-h-2-6]], −iσĝ^aug(σ)(ḃ) = Ψ(σ, ·)ġ(ḃ) and

    −σ²ĥ^aug(σ)(S) = (Ψ − σ∂_σΨ)h(S) − iσΨ h̆(S),                                                       {#eq:iii-h1-5-4}

with Ψ(σ, x) = ∫ e^(iσt_*)∂_(t_*)χ_K dt_*, entire in σ for each x (the support of ∂_(t_*)χ_K(·, x) is compact). So
∂_(t_*)v_ġ = (2π)⁻¹∫ e^(−iσt_*)χΨġ(b̂_1) dσ over the same contour, and the integrand is bounded near 0 and holomorphic
inside 𝒞_0; as in [[lem:iii-h1-4-1]], 𝒞_0 moves to [−c/2, c/2], and ℱ(∂_(t_*)v_ġ) = χΨġ(b̂_1) on ℝ. Likewise
ℱ(∂²_(t_*)v_h) is χ times [[eq:iii-h1-5-4]] at S = Ŝ_1.

*Uniform bounds.* For r ≥ 1, Ψ = Φ(σr) ([[lem:iii-h-2-5]] (b)), with Φ entire and |∂^j_ζΦ| ≤ C_(j,M)⟨ζ⟩^(−M) on
{Im ζ ≥ 0}. So, with ζ = σr,

    Ψġ = r⁻²Φ(ζ)(r²ġ),     −σ²ĥ^aug(σ)(S) = r⁻³((Φ(ζ) − ζΦ′(ζ))r³h − iζΦ(ζ)r²h̆),

where r²ġ, r³h and r²h̆ are bounded with all their b-derivatives (the weights are 2 or 3, 3 and 2; [[sec:iii-h-1]]).
Each is r^(−q)G(σr, x) with q = 2, resp. 3, and G smooth with |(ζ∂_ζ)^j(r∂_r)^a∂_ω^βG| ≤ C⟨ζ⟩^(−M) for ζ real;
σ∂_σ acts as ζ∂_ζ. The proof of [[lem:iii-h-2-4]] (b), with r⁻³ replaced by r^(−q), gives
sup_(0<|σ|≤1) ‖(σ∂_σ)^j(·)‖_(H^(k′,(M,β_tf,0))_(b,|σ|)) < ∞ for every k′, M and β_tf < q, since the bound
ρ_tf^(q−β_tf) is square integrable for μ_b uniformly if and only if β_tf < q. For r ≤ 1, Ψ and its σ- and
x-derivatives are bounded uniformly for |σ| ≤ 1 (proof of [[lem:iii-h-2-5]] (d):
∂^j_σΨ = ∫ (it_*)^j e^(iσt_*)∂_(t_*)χ_K dt_*). By [[eq:ii-g1-4-5a]] with l + 4 = β_tf, for every constant order pair and
|σ| ≤ ς_1 (and c ≤ ς_1, [[sec:iii-h1-2]]),

    sup_(0<|σ|≤c) Σ_(j≤k) (‖(σ∂_σ)^j(Ψġ(e_i))‖_((p;k),(p+β′,β′,0),|σ|)
                            + ‖(σ∂_σ)^j(σ²ĥ^aug(σ)(e′_i))‖_((p;k),(p+β″,β″,0),|σ|)) < ∞

for basis elements e_i, e′_i, every p, β′ < 0 and β″ < 1. Take β′ := α_sf + 1 < 0 and β″ := α_sf + 2 < 1, by
[[eq:iii-h1-1-1]].

*Inverse transform.* By [[lem:ii-a-5-2]] with the constant order p and the weight β′, and Leibniz,

    ‖∂_(t_*)v_ġ‖² ∼ Σ_(j≤k) ∫_(−c)^c ‖(σ∂_σ)^j(χΨġ(b̂_1))‖²_((p;k−j),(p+β′,β′,0),|σ|) dσ
                 ≤ C Σ_(j≤k) ∫_(−c)^c |(σ∂_σ)^j b̂_1|² dσ,

and [[lem:iii-h1-4-2]] bounds the right side; likewise for ∂²_(t_*)v_h, with β″ and Ŝ_1. ∎

The same holds uniformly for b near b_0, by [[rem:iii-h-2-6]], as β′ < 0 and β″ < 1 hold with room.

### Integration in t_* {#sec:iii-h1-6}

This section is [Hin26, Lemma 10.13] in dimension 4 + 1, for variable orders.

**Lemma {#lem:iii-h1-6-1}** (Translation-invariant elliptic operators.) Let 𝗌 ∈ C^∞(³ᵇS*M̃_0) be
t_*-translation-invariant, d ∈ ℕ and ν_0 > 0. There are t_*-translation-invariant operators A ∈ Ψ̃^𝗌_3b, elliptic,
Q′ ∈ Ψ̃^(−𝗌)_3b and R ∈ Ψ̃^(−d)_3b with

    I = Q′A + R²,                                                                                       {#eq:iii-h1-6-1}

whose Schwartz kernels are supported in {|t_* − t′_*| ≤ ν_0⟨x⟩, |x − x′| ≤ ν_0⟨x⟩}. They act on H^(𝗌′,(β,γ))_3b
with the orders shifted by their own, for all β and γ. (Only b-order k = 0 is claimed: for variable orders,
commutators with b-vector fields carry logarithmic factors, and [[lem:iii-h1-6-2]] reduces to k = 0 first.)

*Proof.* In the frame ⟨x⟩∂_(t_*), ⟨x⟩∂_(x_i), which is t_*-invariant, a 3b covector has fibre coordinates ζ ∈ ℝ⁵, and
a t_*-translation-invariant function on the 3b-cotangent bundle is a function of (x, ζ); in particular 𝗌 = 𝗌(x, ζ). For
a symbol a(x, ζ) of variable order (in the symbol classes of [[sec:ii-a-3]]) put, with ψ ∈ C_c^∞(ℝ⁵) equal to 1 near
0 and supported in {|y| ≤ ν_1},

    Op(a)u(t_*, x) := (2π)⁻⁵ ∫ e^(i((t_*−t′_*)τ+(x−x′)·ξ)) ψ((t_* − t′_*, x − x′)/⟨x⟩)
                          × a(x, ⟨x⟩(τ, ξ)) u(t′_*, x′) dt′_* dx′ dτ dξ.

In a unit cell of the scaled bounded geometry ((S9) in [[sec:ii-a-3]]; cells of size ⟨x_α⟩), after rescaling by ⟨x_α⟩,
this is the quantization with the cut-off of [Hin26d, (3.26)] ([[sec:ii-a-8-3]]) of the symbol
a(x, (⟨x⟩/⟨x_α⟩)ζ̃), which lies in the same class, since ⟨x⟩/⟨x_α⟩ is bounded above and below with bounded scaled
derivatives; the cut-off is rescaled by the same factor. A change of cut-off changes the operator by one with smooth
kernel, supported within bounded cell distance and rapidly decaying in the scaled variables: a residual operator
localized near the diagonal. So Op(a) ∈ Ψ̃^(ord a)_3b, localized near the diagonal, with kernel range ν_1⟨x⟩. Its
kernel depends on (t_* − t′_*, x, x′), so Op(a) commutes with t_*-translations; compositions of such operators commute
with them and have kernel ranges that add. Take a := ⟨ζ⟩^𝗌, A := Op(a) and Q_0 := Op(a⁻¹). Then Q_0A = I − R_1 with
R_1 ∈ Ψ̃^(−(1−2δ))_3b translation-invariant (the calculus with variable orders loses δ > 0 in the remainder). With
d′(1 − 2δ) ≥ d, Q := Σ_(j<d′) R_1^j Q_0 gives QA = I − R_1^(d′) =: I − R, and I = QA + R = (Q + RQ)A + R², so
Q′ := Q + RQ. All of these are translation-invariant, with kernel range at most 4d′(1 + ν_1)ν_1⟨x⟩ ≤ ν_0⟨x⟩ for ν_1
small (compositions add ranges, with ⟨x′⟩ ≤ (1 + ν_1)⟨x⟩ on them). For the weights w = ρ_sf^β ρ_K^γ, w⁻¹Aw has kernel
K_A(z, z′)w(z′)/w(z), and on the support of the kernel w(z′)/w(z) is smooth and bounded with bounded scaled
derivatives, as the logarithmic 3b-derivatives of ρ_sf and ρ_K are bounded: an operator of the same class. ∎

**Lemma {#lem:iii-h1-6-2}** ([Hin26, Lemma 10.13] in dimension 4 + 1.) Let 𝗌 be a t_*-translation-invariant 3b order,
constant over {r ≤ r_0 + δ_1} for some δ_1 ∈ (0, 1] (as the orders in 𝒪_c are, by [[def:ii-c-2-4]] (3): constant over
{r ≤ r_Γ}, r_Γ > r_2 > r_0), and let k ∈ ℕ_0, β ∈ ℝ and ℓ > ½. If u is a distribution on M_0° with

    u|_(Ω_−) ∈ H̄^((𝗌;k),(β−1,−ℓ))_(3b;b)(Ω_−),     ∂_(t_*)u ∈ H^((𝗌;k),(β,−ℓ+1))_(3b;b)(M_0),

then u ∈ H^((𝗌;k),(β−1,−ℓ))_(3b;b)(M_0), with norm at most C times the sum of those two norms. The density is |dt_*|
times any weighted b-density on X; a change of density is a shift of β.

*Proof.* *Cut-off.* Let χ ∈ C^∞(ℝ) equal 1 on [−¼, ∞) and 0 on (−∞, −½], and put u′ := χ(t_*/r)u. Then u − u′ is
supported in {t_* ≤ −r/4} ⊂ Ω_−, away from {t_* = 1}, so it lies in H^((𝗌;k),(β−1,−ℓ))_(3b;b)(M_0); χ(t_*/r) is
homogeneous of degree 0, a 3b multiplier; and ∂_(t_*)u′ = χ(t_*/r)∂_(t_*)u + r⁻¹χ′(t_*/r)u, whose last term is
supported in Ω_− away from {t_* = 1} and from K^±, and lies in H^((𝗌;k),(β,−ℓ+1))_(3b;b), as r⁻¹ = ρ_sf there. So we
may assume u = 0 for t_* ≤ −r/2, and then only ∂_(t_*)u =: f enters.

*b-regularity.* ∂_(t_*) and ⟨x⟩∂_x commute with ∂_(t_*), and ∂_(t_*)(t_*∂_(t_*)u) = t_*∂_(t_*)f + f, which preserves
the support condition; by induction it suffices to take k = 0.

*The case 𝗌 = 0.* Let r_1 > 0, c ≥ 0 and ν ∈ (0, 1), put t := t_* + r + c, and let v be a distribution on M̃_0,
supported in {r ≥ r_1}, with v = 0 for t ≤ νr and g := ∂_(t_*)v ∈ H^(0,(β,−ℓ+1))_3b. Then v ∈ H^(0,(β−1,−ℓ))_3b, with
norm at most C‖g‖, C depending on r_1, c and ν. Indeed, on {r ≥ r_1, t ≥ νr}, ρ_sf and ρ_K are r⁻¹ and r/t up to
bounded factors. As ∂_(t_*) commutes with powers of r we may take β = 0. Dropping the angular variables (the density
is |dt dr| after the shift of β), g = ρ_K^(1−ℓ)g_0 = r^(1−ℓ)t^(ℓ−1)g_0 with g_0 ∈ L²(|dt dr|), and
v(t, r) = ∫_(νr)^t g(t′, r) dt′. Fix a ∈ (−½, ℓ − 1), which is possible as ℓ > ½. Then

    ‖ρ_sf ρ_K^ℓ v‖² ≤ C ∫_(r_1)^∞ ∫_(νr)^∞ t^(−2ℓ) |∫_(νr)^t t′^(ℓ−1) g_0(t′, r) dt′|² dt dr
                   ≤ C ∫∫ t^(−2ℓ) (t^(2a+1)/(2a + 1)) ∫_(νr)^t t′^(2ℓ−2−2a) |g_0|² dt′ dt dr,

by Cauchy–Schwarz with t′^(ℓ−1) = t′^a · t′^(ℓ−1−a). Exchanging the integrals and using
∫_(t′)^∞ t^(−2ℓ+2a+1) dt = t′^(−2ℓ+2a+2)/(2ℓ − 2a − 2), the right side is at most
C‖g_0‖²_(L²) = C‖g‖²_(H^(0,(0,1−ℓ))_3b).
Nothing here depends on the dimension.

*Extension across {r = r_0}.* The spaces on M_0 are the restrictions to {r ≥ r_0} of the spaces on M̃_0, with the
quotient norms ([[def:ii-a-7-2]]), 𝗌 being extended to M̃_0 by its constant value s_0 over {r < r_0}. Let F̃ be an
extension of f with ‖F̃‖_(H^(𝗌,(β,−ℓ+1))_3b(M̃_0)) ≤ 2‖f‖_(H^(𝗌,(β,−ℓ+1))_3b(M_0)), and put

    F := χ_1(r) χ_2(t_*/⟨x⟩) F̃,

where χ_1 ∈ C^∞(ℝ) equals 0 on (−∞, r_0/2] and 1 on [r_0, ∞), and χ_2 ∈ C^∞(ℝ) equals 0 on (−∞, −¾] and 1 on
[−½, ∞). Both factors are bounded together with all their derivatives along ⟨x⟩∂_(t_*) and ⟨x⟩∂_x (where a derivative
of χ_2(t_*/⟨x⟩) is nonzero, |t_*| ≤ ⟨x⟩), so multiplication by them is bounded on the 3b spaces ((S3), (S8) in
[[sec:ii-a-3]]), and ‖F‖ ≤ C‖f‖. On {r > r_0}, F = f: there χ_1 = 1, and χ_2(t_*/⟨x⟩) ≠ 1 only where
t_* < −⟨x⟩/2 ≤ −r/2, where f vanishes. F is supported in {r ≥ r_0/2, t_* ≥ −¾⟨x⟩}. Let U be the primitive of F in t_*
that vanishes for t_* < −⟨x⟩ (the convolution in t_* with the Heaviside function). Then ∂_(t_*)U = F, U is supported
in {r ≥ r_0/2, t_* ≥ −¾⟨x⟩}, and U = u on {r > r_0}, as both are primitives of f there that vanish for t_* < −⟨x⟩.
Restriction to {r ≥ r_0} being bounded, it suffices to prove ‖U‖_(H^(𝗌,(β−1,−ℓ))_3b(M̃_0)) ≤ C‖F‖. No extension
operator is used: f is extended through the definition of the quotient norm, at its own order, and U is obtained by
integration in t_*.

*General 𝗌.* Take A, Q′ and R of [[lem:iii-h1-6-1]] for the extended order, with d ≥ sup|𝗌| + |inf 𝗌| and
ν_0 ≤ min(1/16, r_0/8). Let z = (t_*, x) lie in supp K_A or in supp K_R, as a function of its first variable, with its
second variable z′ = (t′_*, x′) in supp U, and write r′ := |x′|. Then r ≥ r′ − ν_0⟨x⟩ ≥ r_0/2 − ν_0(1 + r), so
r ≥ r_0/3. And ⟨x′⟩ ≤ (1 + ν_0)⟨x⟩, so t_* ≥ −¾⟨x′⟩ − ν_0⟨x⟩ ≥ −(¾ + 2ν_0)(1 + r), and t := t_* + r + 1 satisfies
t ≥ (¼ − 2ν_0)(1 + r) > r/8. The operators are localized near the diagonal, hence act on all distributions, and
[[eq:iii-h1-6-1]] holds on them. So AU and RU are supported in {r ≥ r_0/3} and vanish for t ≤ r/8, and
∂_(t_*)(AU) = AF lies in H^(0,(β,−ℓ+1))_3b and ∂_(t_*)(RU) = RF in H^(𝗌+d,(β,−ℓ+1))_3b ⊂ H^(0,(β,−ℓ+1))_3b. By the
case 𝗌 = 0 with r_1 = r_0/3, c = 1 and ν = 1/8, AU, RU ∈ H^(0,(β−1,−ℓ))_3b, and
U = Q′(AU) + R(RU) ∈ H^(𝗌,(β−1,−ℓ))_3b, with the estimate. ∎

[Hin26] proves the case 𝗌 = 0 and refers the rest to [Hin26c, Lemma 14.6], whose proof applies the case 𝗌 = 0 to Au.
This needs A translation-invariant, so that ∂_(t_*)Au = Af, and localized near the diagonal, so that Au keeps a support
condition; [[lem:iii-h1-6-1]] supplies both, by a translation-invariant quantization in the calculus of [[ch:s04]].

### Proof of the 2-admissibility {#sec:iii-h1-7}

*Proof of [[thm:iii-h1-1-3]].* Let f be as in [[sec:iii-h1-2]], and u = u_hi + u_reg + u_sing as in
[[eq:iii-h1-5-2]]. Write ‖f‖ := ‖f‖_(H^((𝗌;k),(α_sf+2,0))_(3b;b)(Ω)^(•,−)).

(i) By [[lem:iii-h1-3-1]] (with ϵ < ½) and [[lem:iii-h1-4-1]], u_hi + u_reg ∈ H^((𝗌;k),(α_sf,0))_(3b;b)(M_0) with norm
at most C‖f‖, as α_sf < α_sf + 1 − 2ϵ and 𝗌 < 𝗌 + 1.

(ii) u = 0 for t_* < t_1, where t_1 > 1, so u_sing = −(u_hi + u_reg) on Ω_−:

    u_sing|_(Ω_−) ∈ H̄^((𝗌;k),(α_sf,0))_(3b;b)(Ω_−),     ∂_(t_*)u_sing|_(Ω_−) ∈ H̄^((𝗌−1;k),(α_sf+1,0))_(3b;b)(Ω_−).

(iii) By [[lem:iii-h1-5-1]] with p ≥ sup 𝗌, ∂²_(t_*)u_sing = ∂_(t_*)(∂_(t_*)v_ġ) + ∂²_(t_*)v_h lies in
H^((𝗌−1;k),(α_sf+2,0))_(3b;b)(M_0).

(iv) [[lem:iii-h1-6-2]] for ∂_(t_*)u_sing, with the order 𝗌 − 1, β = α_sf + 2 and ℓ = 1 (the data (ii) lie in
(α_sf + 1, 0) ⊂ (β − 1, −1)), gives ∂_(t_*)u_sing ∈ H^((𝗌−1;k),(α_sf+1,−1))_(3b;b)(M_0).

(v) [[lem:iii-h1-6-2]] for u_sing, with 𝗌 − 1, β = α_sf + 1 and ℓ = 2 (the data (ii) lie in (α_sf, 0) ⊂ (β − 1, −2),
at the regularity 𝗌 ≥ 𝗌 − 1), gives u_sing ∈ H^((𝗌−1;k),(α_sf,−2))_(3b;b)(M_0).

(vi) So u ∈ H^((𝗌−1;k),(α_sf,−2))_(3b;b)(M_0) with norm at most C‖f‖, every bound being linear in ‖f‖. As u is
supported in Ω, this is [[eq:iii-h1-1-2]]. For general f, [[eq:iii-h1-1-2]] follows by density and the uniqueness of
forward solutions ([[prop:ii-e-3-4]]). ∎

Each step needed only the weights of [[eq:iii-h1-1-1]]: α_sf + 1 < 0 in (iii), through β′, and α_sf + 2 < 1, through
β″. In dimension 3 + 1 the same steps stop at β′ = −½ − ϵ, below α_sf + 1, and this is the loss in [Hin26, Theorem
10.1].

### Remarks on [Hin26, Section 10] {#sec:s18-remarks}

The following points compare the argument of this chapter with that of [Hin26, Section 10].

(a) *The rows.* [Hin26, (10.6b)] does not make the augmented zero energy operator injective; [[rem:s18-rows]] gives a
choice of rows satisfying it for which [Hin26, Proposition 10.6] fails, and [[eq:iii-h-3-1]] is the condition the proof
uses.

(b) *The incoming threshold.* [[def:ii-c-2-4]] (6) with α_K = −2 and margin 1 gives 𝗌 + α_sf > ½(−1 + ϑ_in) − 1 at
the incoming radial set (ϑ^(3b)_in = ϑ_in by [[lem:ii-c-2-6]]), while the spectral estimates for
u ∈ H^(𝗌,(α_sf,0))_3b need 𝗌 + α_sf > ½(−1 + ϑ_in) ([[eq:i-a-1-5]], [[sec:i-b-1-4]]). [Hin26, Lemmas 10.9–10.10]
measure u_hi and u_reg at the weight α_sf and the regularity 𝗌, which the hypothesis does not cover where
𝗌 + α_sf ≤ ½(−1 + ϑ_in). [Hin26, Remark 10.2] checks only the outgoing radial set, where the condition of
[[def:ii-c-2-4]] (5) is 𝗌 + α_sf < ½(−1 + ϑ_out) + α_K − 1 = ½(−1 + ϑ_out) − 3; the remark states −½ − 1 there,
without α_K. Here u_hi is measured at the weight α_sf + 1 − 2ϵ, with ϵ below the margin ([[lem:iii-h1-3-1]]), and
u_reg at the regularity 𝗌 + 1
([[lem:iii-h1-4-1]]); both use the margin, and nothing is lost in [[thm:iii-h1-1-3]].

(c) *The neighbourhood of b_0.* The high-energy estimate with k orders of b-regularity needs (k + 1)δ_Γ(−ϵ′) ≤ 1 for some
ϵ′ > 0 ([[lem:iii-h1-3-1]]). [[prop:iii-f-4-1]] gives strong trapping admissibility at b_0, and, near b_0, the smallness
of δ_Γ(0) only on a neighbourhood that shrinks as the bound decreases. [Hin26] states its Theorem 10.1 for b near b_0
with its Proposition 8.3 (strong trapping admissibility near b_0 in dimension 3 + 1). [[thm:iii-h1-1-3]] is therefore
stated on the sets ℬ_k, and [[rem:s18-every-k]] gives one neighbourhood for every k.

(d) *The class of orders.* 𝒪_c adds to [[def:ii-c-2-4]] the conditions (C1)–(C3), under which the induced spectral
orders satisfy the hypotheses of [[ch:s01]]–[[ch:s03]]: a constant regularity order ((O1) of [[def:i-a-admissible]]
and [[rem:i-a-1-1]]; [[ch:s03]]), the constancy of the semiclassical order over {r ≤ r_2 − δ_0}, and the monotonicity
on a neighbourhood of the characteristic set ([[sec:i-b-1-4]]; [Hin26c, footnote 78]). [Hin26] applies
[Hin26c, Theorems 9.16 and 9.41] to the induced orders without stating these conditions.

(e) *Bounded frequencies.* On c/2 ≤ |σ| ≤ C_0, [Hin26] cites only [Hin26c, Theorem 9.16 (5)], a high-energy
statement; here [[thm:i-a-7-2]] (6) and [[eq:i-a-7-6]], with the invertibility of [[cor:iii-h-4-4]], cover them
([[lem:iii-h1-3-1]]).

(f) *Variable orders in [Hin26, Lemma 10.13].* Its reduction to 𝗌 = 0 through [Hin26c, Lemma 14.6] needs an elliptic
operator that commutes with ∂_(t_*) and is localized near the diagonal, so that Au keeps a forward support condition,
for which the case 𝗌 = 0 is proved with t ≥ νr for any ν > 0; [[lem:iii-h1-6-1]] constructs it.
