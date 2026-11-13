## Forward solutions on e3b-spaces and their tame estimates {#ch:s09}

This chapter solves forward problems on the compactified spacetime M. The first half concerns the stationary model
P_0. Its normal operator N_ι⁺(P_0) at future timelike infinity is inverted on edge-b-edge spaces by the Mellin
transform ([[prop:ii-f-6-2]]); a modified operator P_+, equal to N_ι⁺(P_0) near the timelike curve of the spatial
origin and to P_0 near 𝓘⁺, is inverted on the same spaces ([[prop:ii-f-7-4]]); and the two are joined, with the
ℵ-admissibility of P_0 at K⁺, into forward solutions of P_0 on e3b-Sobolev spaces with decay at ι⁺ and the loss ℵ at
K⁺ ([[thm:ii-f-8-1]]). The second half solves forward problems for admissible wave-type operators P, perturbations of
P_0 that decay at 𝓘⁺, ι⁺ and K⁺, on b-Sobolev spaces, with estimates tame in the b-regularity ([[thm:ii-f1-1-1]],
[[cor:ii-f1-1-2]]). These results are [Hin26c, Proposition 10.12, Proposition 10.14, Theorem 10.1] and [Hin26c, Theorem
11.1] in dimension 4 + 1. The dimension enters through the constant c := (n − 1)/2 = 3/2 of the normal form of P_0
([[def:ii-c-1-1]]) and through the densities, which shift weights by n/2 = 2 and by (n + 1)/2 = 5/2.

The notation is that of [[ch:s04]]–[[ch:s08]]. In particular n = 4, c = 3/2, τ = t_*⁻¹, R = r/t_*, x_I = R^(−1/2) near
ι⁺ ∩ 𝓘⁺, ρ_K = R/(1 + R), the weights γ_I, γ_+, γ_cf of [[eq:ii-f-1-2]], the Mellin transform ℳ of [[eq:ii-f-1-3]],
the ι⁺-normal operator N_ι⁺(P_0) = τ² N⁰ and its family N⁰(σ) of [[def:ii-f-1-1]], the semiclassical family P_(ι,h,z)
of [[eq:ii-f-1-11]], the parameter sets [[eq:ii-f-3-2]], the orders and spaces [[eq:ii-f-3-3]] and the norms
[[eq:ii-f-4-1]]. Order functions are written in sans-serif type (𝗌, 𝗍, 𝖻). The defining function x_I of 𝓘⁺ is
R^(−1/2) near ι⁺ ∩ 𝓘⁺, r^(−1/2) at finite times ([[sec:ii-f-6-3]]) and (t_*/(t_* + r))^(1/2) on Ω ([[eq:ii-f1-1-1]]);
where two of these are defined near 𝓘⁺ they differ by a smooth positive factor, so the weighted spaces do not depend on
the choice. The radii 0 < r_0 − 2δ_0 < r_0 < r_2 of the artificial boundary are parameters of the setting. The constants
chosen from r_0 below (T_+ in [[def:ii-f-7-1]], the set Ω_♮ and the constants of [[lem:ii-f1-2-3]], the width κ of
[[sec:ii-f1-2-5]]) are chosen by inequalities that a smaller r_0 makes no harder, so every result holds for each choice
of the radii at which the hypotheses of [[ch:s05]] hold.

### Forward solutions of the ι⁺-normal operator {#sec:ii-f-6}

This section is [Hin26c, Section 10.1.4] in dimension 4 + 1. Throughout [[sec:ii-f-6]]–[[sec:ii-f-8]], P_0 is a
stationary wave-type operator as in [[def:ii-c-1-1]], in the setting of [[sec:ii-e-1-1]], with γ_I, γ_cf = −(α_+ + 2)
and (β_−, β_+) as in [[sec:ii-f-5]].

#### Edge-b-edge spaces {#sec:ii-f-6-1}

On [0, ∞]_τ × ι⁺, τ = t_*⁻¹, we write ι⁺ for the face {0} × ι⁺, 𝓘⁺ for [0, ∞] × (ι⁺ ∩ 𝓘⁺), and cf := [0, ∞] × (ι⁺ ∩
K⁺), with defining functions ρ_+ = τ/(1 + τ) (or τ), x_I, and ρ_cf = R/(1 + R). The face cf = {R = 0} = {r = 0} is the
timelike curve of the spatial origin, at each time; it is not K⁺. The *ebe-vector fields* ([Hin26c, Definition 10.11])
are the b-vector fields of [0, ∞] × ι⁺ tangent to the fibres of 𝓘⁺ → 𝕊³ and of cf → [0, ∞]_τ. With χ ∈ C_c^∞([0, 3))
equal to 1 on [0, 2] they are spanned over C^∞ by

    χ(R) R∂_R,   χ(R) Z_a,   χ(R) Rτ∂_τ,      χ(v) v∂_v,   χ(v) √v Z_a,   χ(v) τ∂_τ,      v = R⁻¹,       {#eq:ii-f-6-1}

where Z_a, a = 1, …, 6, are the rotation fields Z_(ij) = x_i ∂_(x_j) − x_j ∂_(x_i), 1 ≤ i < j ≤ 4, of 𝕊³ ⊂ ℝ⁴, in
place of the coordinate fields ∂_ω of [Hin26c, (10.42)]. They span T𝕊³ at every point: for x ∈ 𝕊³ and w ∈ T_x𝕊³,

    Σ_(i<j) (x_i w_j − x_j w_i) Z_(ij)(x) = ½ Σ_(i,j) (x_i w_j − x_j w_i)(x_i e_j − x_j e_i) = |x|² w − (x·w) x = w,

since the summand is symmetric under the exchange of i and j and vanishes for i = j. By [[eq:ii-f-1-5]] and
N_ι⁺(P_0) = τ² N⁰ ([[def:ii-f-1-1]]), with R⁻¹ τ∂_τ = R⁻² (Rτ∂_τ) and R⁻¹ R∂_R near cf, and by [[eq:ii-f-1-6]] near 𝓘⁺,

    N_ι⁺(P_0) ∈ x_I² ρ_+² ρ_cf⁻² Diff²_ebe([0, ∞] × ι⁺),                                                 {#eq:ii-f-6-2}

which is [Hin26c, (10.43)]. The spaces of [Hin26c, (10.45)–(10.48)] are, in dimension 4 + 1,

    H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)
        := x_I^(2γ_I) τ^(γ_+) ρ_cf^(γ_cf) H^((𝗌;k))_(ebe;b)((0, ∞)_τ × ι⁺; |dτ/τ| μ_b),                  {#eq:ii-f-6-3}

the Sobolev spaces of the product structure of [[sec:ii-a-6-2]] (cells: unit intervals in t = −log₂ τ times the cells
U_(2,jk±), U_(3,jk±) of ι⁺), with k further b-derivatives along τ∂_τ and the fields W_i of [[sec:ii-f-4-1]]. The order
𝗌 may be variable, the weights are constant, and all densities are b-densities. Ḣ(… [0, τ_0] × ι⁺) denotes the subspace
of distributions supported in {τ ≤ τ_0}; there τ^(γ_+) and ρ_+^(γ_+) give equivalent norms. As in [Hin26c, footnote
99], ũ ∈ H^(𝗌,γ_cf)_(e,loc)((0, ∞)_τ × {R < R_0}) means that χũ ∈ H^(𝗌,(2γ_I,γ_+,γ_cf))_ebe for all χ ∈ C_c^∞((0, ∞) ×
{R < R_0}), the orders at 𝓘⁺ and ι⁺ being irrelevant there.

*Orders.* As in [Hin26c, (10.12)], let 𝗌 be admissible for P_0 with weights α_+, 0 and margin 0 ([[def:ii-c-5-2]]).
Its restriction to ᵉ³ᵇS*_ι⁺M, extended to be invariant under τ-dilations, is an order on ᵉᵇᵉS*((0, ∞) × ι⁺), again
written 𝗌 (the identification of the phase spaces over ι⁺ is [Hin26c, Section 10.1.1], with [Hin26c, (10.44)] near cf).
Its induced orders are those of [[sec:ii-f-1-3]]: 𝗌_(0,b) at fibre infinity for bounded frequencies, and, for ±Re σ ≥ 1,
𝗌_(0ħ,cħ) at fibre infinity and 𝖻_± at sf.

**Lemma {#lem:ii-f-6-1}** (Plancherel.) For u in [[eq:ii-f-6-3]], with ℳ of [[eq:ii-f-1-3]] and
𝐨_± := (𝗌_(0ħ,cħ); 2γ_I, γ_cf, γ_cf; 𝖻_±),

    ‖u‖²_(H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)) ∼ ∫_(−1)^1 ‖(ℳu)(ζ − iγ_+)‖²_(H^((𝗌_(0,b);k),(2γ_I,γ_cf))_(0,b;b)) dζ
                                         + Σ_± ∫_(±[1,∞)) ‖(ℳu)(ζ − iγ_+)‖²_(𝐨_±;k,+) dζ,                {#eq:ii-f-6-4}

with h = |ζ|⁻¹ in the norm [[eq:ii-f-4-1]]. This is [Hin26c, (10.47)] in dimension 4 + 1.

*Proof.* This is the proof of [[lem:ii-a-6-2]] with b-densities throughout (so without the shifts of [[lem:ii-a-6-1]]):
property (S9) of the calculus ([[sec:ii-a-3]]) for the product structure, after writing u = τ^(γ_+) w, for which
(ℳu)(ζ − iγ_+) = (ℳw)(ζ) by [[eq:ii-f-1-3]]. The weights x_I^(2γ_I) ρ_cf^(γ_cf) are functions on ι⁺ and pass through,
the weight at tf being that at cf (the spaces of [[lem:ii-a-6-2]]). The b-field τ∂_τ becomes multiplication by iσ
(ℳ(τ∂_τ u) = iσ ℳu), bounded for |ζ| ≤ 1 and giving the factors |ζ|^j = h^(−j) of ‖·‖_(𝐨;k,+) for |ζ| ≥ 1; the spatial
b-fields commute with ℳ. For |ζ| ≥ 1 the spectral orders are 𝗌_(0ħ,cħ) at fibre infinity and the restriction of 𝗌 at
sf, which is 𝖻_± ([[sec:ii-f-1-3]]); for |ζ| ≤ 1 the spectral structure is the 0,b-structure, in which only the fibre
order 𝗌_(0,b) enters. ∎

#### The statement {#sec:ii-f-6-2}

**Proposition {#prop:ii-f-6-2}** (Forward solutions of the ι⁺-normal operator.) Let 𝗌 be as above, γ_I < 3/2 + S̄,
γ_+ < min(γ_I, 1 + β_+), γ_cf := −(α_+ + 2), τ_0 ∈ (0, 1] and k ∈ ℕ₀.

(1) (*Existence.*) For every f ∈ Ḣ^((𝗌−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)([0, τ_0] × ι⁺) there is a unique
u ∈ Ḣ^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)([0, τ_0] × ι⁺) with

    N_ι⁺(P_0) u = f,
    ‖u‖_(H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)) ≤ C ‖f‖_(H^((𝗌−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)),         {#eq:ii-f-6-5}

C independent of τ_0 and f. Uniqueness holds in H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)((0, ∞) × ι⁺).

(2) (*Strong uniqueness.*) Let ũ ∈ 𝒟′((0, ∞) × (ι⁺)°) be supported in {τ ≤ τ_0}, with N_ι⁺(P_0) ũ = 0 and ũ ∈
H^(𝗌,γ_cf)_(e,loc)((0, ∞) × {R < R_0}) for some R_0 > 0. Then ũ = 0.

This is [Hin26c, Proposition 10.12] in dimension 4 + 1. [Hin26c] states (1) with f of order 𝗌 − 2; its proof gives
𝗌 − 1 ([Hin26c, (10.50)]), which is also the order [[prop:ii-f-7-4]] feeds it. The loss of one order is the loss at the
radial sets over sf, where the semiclassical estimates [[eq:ii-f-3-4]] and [[eq:ii-f-4-4]] lose one power of h. The
conditions on γ_+ make the line Im σ = −γ_+ lie in the region of [[prop:ii-f-5-1]] where N⁰(σ) is invertible:
−γ_+ > −γ_I and −γ_+ > −1 − β_+.

#### Solutions near 𝓘⁺ at finite times {#sec:ii-f-6-3}

The proof of (2) needs control at 𝓘⁺ of solutions with compactly supported right-hand sides. Near 𝓘⁺ at finite times
we use (t_*, x_I, ω) with x_I = r^(−1/2), the edge fields ∂_(t_*), x_I∂_(x_I), x_I∂_ω, and the spaces H^(s,2γ)_e with
the b-density |dt_* (dx_I/x_I) dω|. On a finite t_*-range these are the spaces [[eq:ii-f-6-3]] near 𝓘⁺: the ebe-fields
τ∂_τ, v∂_v, √v Z_a are combinations of the edge fields with bounded coefficients and conversely, and (t_*/r)^(1/2) and
r^(−1/2) differ by a smooth positive factor. In the notation of [[ch:s07]], with the metric density |dg| a smooth
positive multiple of x_I⁻⁸ |dt_* (dx_I/x_I) dω|, the weight 2α there is 2(α + 2) here ([[lem:ii-a-6-1]]): x_I^(2α)
L²(|dg|) = x_I^(2(α+2)) L²(|dt_* (dx_I/x_I) dω|). So the threshold α < −1/2 + p̄_1 of [[ch:s07]], with p̄_1 = S̄ for P_0
and for the operators below ([[def:ii-c-3-5]]; [Hin26c, Remark 10.2]), is γ < 3/2 + S̄.

The existence of solutions below uses one standard result on hyperbolic equations, [[thm:std-hormander-cauchy]], in
the following case.

*The Cauchy problem* ([[thm:std-hormander-cauchy]] on ℝ^(1+4) with the Minkowski metric). Let Q be a second-order
operator on ℂ^N-valued functions on ℝ^(1+4), with principal symbol Ḡ Id, Ḡ the dual metric function of the Minkowski
metric ḡ, and with smooth lower-order coefficients, and let t be the Minkowski time. For s ∈ ℤ, t_0 ∈ ℝ and
f ∈ H^(s−1)_loc(ℝ^(1+4)) with supp f ⊂ {t ≥ t_0} there is u ∈ H^(s)_loc(ℝ^(1+4)) with Qu = f and supp u ⊂ {t ≥ t_0}.

**Lemma {#lem:ii-f-6-3}** (Control at 𝓘⁺ of the extension.) Let s′ ∈ ℤ, T ∈ ℝ, and g ∈ H^(s′−1)_c with support in
{T ≤ t_* ≤ T + 2, 2 ≤ r ≤ 3}. There is a unique u on {t_* < T + 2}, vanishing for t_* < T and for r < 1, with
N_ι⁺(P_0) u = g and u ∈ H^(s′)_loc; and for every χ ∈ C_c^∞((−∞, T + 2)) and γ < 3/2 + S̄, χ(t_*) u ∈ H^(s′,2γ)_e near
𝓘⁺.

*Proof.* *Existence and support.* By [[eq:ii-f-1-7]] the principal symbol of N_ι⁺(P_0) is the dual Minkowski metric Ḡ,
and its coefficients are smooth on {r > 0}. Let Ñ be a second-order operator on ℝ^(1+4) with smooth coefficients and
principal symbol Ḡ Id, equal to N_ι⁺(P_0) on {r > 1/2}, and let t = t_* + r be the Minkowski time. By the solvability
of the Cauchy problem above, with the Minkowski time t, there is ũ ∈ H^(s′)_loc(ℝ^(1+4)) with Ñũ = g vanishing on
{t < T + 2}, which contains no point of supp g. It vanishes on A_1 := {t_* < T} and on A_2 := {t_* + 2r < T + 4}.
Indeed, g = 0 on each (on supp g, t_* ≥ T and t_* + 2r ≥ T + 4); t_* and t + r = t_* + 2r are non-decreasing along
future causal curves ([[lem:ii-f-1-4]] (c)), so for p ∈ A_j the Minkowski causal past J⁻(p) lies in A_j, and J⁻(p) ∩
{t ≥ T + 1} is compact; and supp ũ ⊂ {t ≥ T + 2}. So [[lem:ii-f-1-3]] applies on A_j, with the time function t,
c := T + 1 and L_p := J⁻(p) ∩ {t ≥ T + 1}. Hence a point of supp ũ has t_* ≥ T and t_* + 2r ≥ T + 4, and if
t_* < T + 2 then r > 1. So u := ũ|_({t_*<T+2}) vanishes for t_* < T and for r < 1, and solves N_ι⁺(P_0) u = g (on
{r > 1/2}, Ñ = N_ι⁺(P_0); on {r < 1} both sides vanish). If u′ is another such solution, w := u − u′, extended by 0
across {r = 0}, solves Ñw = 0 on {t_* < T + 2} and vanishes on {t < T}, and [[lem:ii-f-1-3]] on {t_* < T + 2} with the
time function t, c := T − 1 and L_p := J⁻(p) ∩ {t ≥ T − 1} gives w = 0. In particular u does not depend on the choice
of Ñ.

*Control at 𝓘⁺.* By t_*-translation invariance we may take T ≥ 8/C′, with C′ of [[lem:ii-c-3-2]] (b). By the
homogeneity of N_ι⁺(P_0) ([[sec:ii-f-1-2]]), (D_Λ u)(t_*, x) := u(t_*/Λ, x/Λ) satisfies N_ι⁺(P_0) D_Λ u = Λ⁻² D_Λ g.
D_Λ preserves the spaces H^(s′,2γ)_e near 𝓘⁺ at finite times: it maps the edge fields to constant multiples of
themselves and x_I^(2γ) to Λ^γ x_I^(2γ). So we may replace g by D_Λ g, supported in {T′ ≤ t_* ≤ T′ + 2Λ, 2Λ ≤ r ≤
3Λ}, T′ := ΛT, with Λ ≥ 1 to be chosen; ũ by D_Λ ũ; and Ñ by its rescaling Ñ_Λ, equal to N_ι⁺(P_0) on {r > Λ/2}. By
the support argument above, ũ vanishes on {t_* < T′} and on {t_* + 2r < T′ + 4Λ}. Let ψ ∈ C^∞(ℝ) vanish on (−∞, 1/2]
and equal 1 on [1, ∞), ψ̃ ∈ C^∞(ℝ) equal 1 on (−∞, T + 2] and 0 on [T + 3, ∞), and on Ω put

    P_Λ := P_0 + ψ(r/Λ) ψ̃(t_*/Λ) (N_ι⁺(P_0) − P_0).

Both cut-offs are scaled with Λ, so their b-derivatives are bounded uniformly in Λ: t_*∂_(t_*) ψ̃(t_*/Λ) = (t_*/Λ)
ψ̃′(t_*/Λ) with t_*/Λ ≤ T + 3 on the support of ψ̃′, and likewise for ψ(r/Λ); an unscaled ψ̃(t_*) would have
b-derivatives of size Λ. The second term is supported in {r ≥ Λ/2, t_* ≤ (T + 3)Λ}, where ρ_K = r/(t_* + r) ≥
(2T + 7)⁻¹, uniformly in Λ ≥ 1 (T being fixed): near 𝓘⁺ ∪ (ι⁺)°, away from K⁺. There the terms (i)–(iv) of the proof
of [[lem:ii-f-1-2]], times t_*⁻², are τ³R⁻² times polynomials of degree at most 2 in the e3b-fields τ∂_τ, x_I∂_(x_I),
x_I∂_ω ([[sec:ii-a-2-4]]) with coefficients bounded with all their b-derivatives, uniformly in Λ; and τ³R⁻² = x_I² ρ_+²
(t_* + r)⁻¹ for the e3b defining functions x_I² = t_*/(t_* + r), ρ_+ = (t_* + r)/(t_* r) of [[sec:ii-a-1]], x_I² ρ_+²
being the normalisation of P_0 ([[lem:ii-c-1-4]] (b)). Let ℓ_I := 1/2, ℓ_+ ∈ [1/2, 1) ∩ (δ, 1) and ℓ_K := ℵ + 1, a
class of [[def:ii-c-3-3]] (which presupposes δ < 1). On the support, (t_* + r)⁻¹ ≤ x_I ρ_+^(ℓ_+) (t_* + r)^(−(1−ℓ_+)),
as ℓ_+ ≥ 1/2, and ρ_K is bounded below. So P_Λ is weakly admissible relative to P_0 ([[def:ii-c-3-3]], with p_0 = p̃_1
= 0, p_1 = S|_(∂X) as for P_0) of class ((d_0;0),(2ℓ_I,ℓ_+,ℓ_K)) for every d_0, with ‖P_Λ − P_0‖ ≤ C_(d_0)
Λ^(−(1−ℓ_+)), and its metric g_Λ is in 𝒢 with ‖g_Λ − g_0‖ ≤ C Λ^(−(1−ℓ_+)). Fix Λ so large that Λ/2 ≥ r′_0 + 1 and
P_Λ satisfies the smallness hypotheses of [[sec:ii-e-1-1]]. Then t^♭ is a time function for g_Λ ([[lem:ii-c-3-2]] (2)),
and [[lem:ii-f-1-4]] (a) applies to g_Λ, whose dual metric is G_0 + ψ(r/Λ) ψ̃(t_*/Λ)(Ḡ − G_0), the interpolating
function vanishing on {r ≤ Λ/2} ⊃ {r ≤ r′_0 + 1}.

Let T_0 := C′T′ ≥ 8 and T_1 := T′ + 2Λ. D_Λ g is supported in {t_* ≥ T′} ⊂ {t^♭ ≥ T_0} ([[lem:ii-c-3-2]] (b)) and
compactly in M°, so it lies in every weighted space on the slab Ω′ := Ω_(T_0,T_1), and [[prop:ii-e-3-4]] (ii), with the
constant (slab) order s′ and α := γ − 2 < −1/2 + S̄, gives the forward solution u_Λ ∈ H^(s′,2α)(Ω′)^(•,−) of P_Λ u_Λ =
D_Λ g. Let X := Ω° ∩ {t_* < T_1, t^♭ < T_1, r > r_0}, on which u_Λ is defined, and w := ũ − u_Λ on X. On X, P_Λ ũ =
D_Λ g: the open sets X ∩ {r > Λ} and X ∩ {t_* + 2r < T′ + 4Λ} cover X, as t_* < T′ + 2Λ on X; on the first, P_Λ =
N_ι⁺(P_0) = Ñ_Λ (ψ̃(t_*/Λ) = 1 there), and on the second ũ and D_Λ g both vanish. So P_Λ w = 0 on X, and supp w ⊂
{t^♭ ≥ T_0} (ũ vanishes on {t_* < T′} ⊃ {t^♭ < T_0}, and u_Λ by its space). For p ∈ X with t^♭(p) > c := T_0/2,
J⁻_X(p) ∩ {t^♭ ≥ c} lies in

    L_p := {c ≤ t^♭ ≤ t^♭(p),  t_* ≤ t_*(p),  B ≤ B(p),  r ≥ min(r(p), r^♮)}

([[lem:ii-f-1-4]] (a), and t^♭ is increasing), which is compact (B bounds r) and contained in X (t_* ≥ t^♭ ≥ c ≥ 4).
By [[lem:ii-f-1-3]] with the time function t^♭, w = 0: ũ = u_Λ on X. Near 𝓘⁺, t^♭ ≤ t_*, so X contains a neighbourhood
of 𝓘⁺ ∩ {1 < t_* < T′ + 2Λ}. Hence χ(t_*) ũ ∈ H^(s′,2γ)_e near 𝓘⁺ for χ ∈ C_c^∞((−∞, T′ + 2Λ)) (with the weight shift
of [[lem:ii-a-6-1]]), and undoing D_Λ gives the claim. ∎

#### Proof of the existence statement {#sec:ii-f-6-4}

*Proof of [[prop:ii-f-6-2]] (1).* *The equation on the Mellin side.* By [[def:ii-f-1-1]], N_ι⁺(P_0) u = f is N⁰u =
τ⁻² f, and τ⁻² f lies in H^((𝗌−1;k),(2γ_I+2,γ_+,γ_cf−2))_(ebe;b) with the same norm as f in the space of
[[eq:ii-f-6-5]], the τ-weight being τ^(γ_+). For σ on the line Im σ = −γ_+, which lies in {Im σ > max(−γ_I, −1 − β_+)},
define

    (ℳu)(σ) := N⁰(σ)⁻¹ ℳ(τ⁻² f)(σ),                                                                      {#eq:ii-f-6-6}

which is well defined by [[cor:ii-f-5-9]].

*Bounds on the line.* Write σ = ζ − iγ_+. (i) For |ζ| ≥ h_0⁻¹ put h := |ζ|⁻¹ and z := hσ = ±1 − ihγ_+ ∈ 𝒵^±_h. By
[[prop:ii-f-4-3]] (the second estimate of [[eq:ii-f-4-4]]) and P_(ι,h,z) = h² N⁰(σ),

    ‖(ℳu)(σ)‖_(𝐨_±;k,+) ≤ C_k ‖h² ℳ(τ⁻² f)(σ)‖_(Y_(𝐨_±);k,+)
                         = C_k ‖ℳ(τ⁻² f)(σ)‖_((𝗌_(0ħ,cħ)−2; 2γ_I+2, γ_cf−2, γ_cf−2; 𝖻_±−1);k,+),

since multiplication by h² = ρ_tf² ρ_sf² lowers the tf- and sf-orders by 2, and Y_𝐨 = H^((𝗌′−2; 2γ_I+2, γ_cf−2, γ_cf;
𝖻+1)) ([[eq:ii-f-3-3]]). The last norm is at most C times the norm with the fibre order 𝗌_(0ħ,cħ) − 1, which is the
spectral norm of [[lem:ii-f-6-1]] for the order 𝗌 − 1 and the weights (2γ_I + 2, γ_+, γ_cf − 2) of τ⁻² f: its sf-order
is 𝖻_± − 1, and its tf-order equals its cf-weight γ_cf − 2. (ii) For |ζ| ≤ h_0⁻¹, σ ↦ N⁰(σ)⁻¹ ∈ ℒ(𝒴^(𝗌_(0,b)−2)_k,
𝒳^(𝗌_(0,b))_k) is continuous ([[cor:ii-f-5-9]]), hence bounded on this compact segment; for 1 ≤ |ζ| ≤ h_0⁻¹ the norms
‖·‖_(𝐨;k,+) at h = |ζ|⁻¹ ∈ [h_0, 1] are equivalent to the 0,b-norms uniformly ([[sec:ii-f-2-1]]), and
𝒴^(𝗌_(0,b)−2)_k ⊃ H^((𝗌_(0,b)−1;k),(2γ_I+2,γ_cf−2))_(0,b;b) continuously. Squaring, integrating in ζ and using
[[eq:ii-f-6-4]] for u (at the order 𝗌) and for τ⁻² f (at the order 𝗌 − 1): the function u with Mellin transform
[[eq:ii-f-6-6]] on the line lies in H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)((0, ∞) × ι⁺), and [[eq:ii-f-6-5]] holds. Since
ℳ(N⁰u)(σ) = N⁰(σ)(ℳu)(σ) = ℳ(τ⁻² f)(σ) on the line (by [[eq:ii-f-1-6]] for u ∈ C_c^∞, and by continuity), N⁰u = τ⁻² f.
Conversely, if N_ι⁺(P_0) u = 0 with u in this space, then N⁰(σ)(ℳu)(σ) = 0 for almost every σ on the line, so ℳu = 0
and u = 0: this is the uniqueness.

*Support (Paley–Wiener).* The solution map f ↦ u is bounded by [[eq:ii-f-6-5]]. The functions f ∈ C_c^∞((0, τ_0) ×
(ι⁺)°) are dense in the space of [[eq:ii-f-6-5]] on [0, τ_0] × ι⁺: the dilations f ↦ f(Λ·, ·), Λ ↓ 1, are
translations in t, strongly continuous on [[eq:ii-f-6-3]] as 𝗌 is dilation-invariant, and move the support into
{τ ≤ τ_0/Λ}; then multiply approximations in C_c^∞((0, ∞) × (ι⁺)°) by a cut-off in τ equal to 1 on [0, τ_0/Λ] and
supported in [0, τ_0). As supp u ⊂ {τ ≤ τ_0} is a closed condition, it suffices to take f ∈ C_c^∞ with supp f ⊂
[τ_1, τ_−] × 𝒞, 0 < τ_1 < τ_− < τ_0, 𝒞 ⊂ (ι⁺)° compact. Then F(σ) := ℳ(τ⁻² f)(σ) ∈ C_c^∞(𝒞) is entire in σ, and for
Im σ ≥ −γ_+ and L ∈ ℕ₀, as ℳ((1 + (τD_τ)²)^L g) = (1 + σ²)^L ℳg and |τ^(−iσ)| = τ^(Im σ) ≤ max(τ_−^(Im σ),
τ_1^(−γ_+)) on the support,

    ‖F(σ)‖_(H^ν) ≤ C_(ν,L) |1 + σ²|^(−L) max(τ_−^(Im σ), τ_1^(−γ_+)).

Let φ ∈ C_c^∞((ι⁺)°). By [[cor:ii-f-5-9]], σ ↦ ⟨(ℳu)(σ), φ⟩, defined by [[eq:ii-f-6-6]] with N⁰(σ)⁻¹, is holomorphic
on {Im σ > max(−γ_I, −1 − β_+)} ⊃ {Im σ ≥ −γ_+}. There is ν_1 with

    |⟨(ℳu)(σ), φ⟩| ≤ C ⟨σ⟩^(ν_1) ‖F(σ)‖_(H^(ν_1)),      Im σ ≥ −γ_+.

Indeed, for |σ| ≥ √2 h_0⁻¹, σ = h⁻¹ z with z in one of the families [[eq:ii-f-3-2]] ([[sec:ii-f-3-1]]), and
[[eq:ii-f-3-4]] bounds (ℳu)(σ) in H^𝐨 by h² F(σ) in Y_𝐨; on compact subsets of (ι⁺)° the semiclassical norms of H^𝐨
and Y_𝐨 are bounded above and below by standard Sobolev norms times powers of h (the orders are bounded, and the weights
are bounded above and below there), and ⟨(ℳu)(σ), φ⟩ only sees supp φ. For |σ| ≤ √2 h_0⁻¹, Im σ ≥ −γ_+, a compact
set, use the continuity of [[cor:ii-f-5-9]]. Fix L with ν_1 − 2L < −1. By Mellin inversion, ⟨u(τ, ·), φ⟩ = (2π)⁻¹
∫_(Im σ = −γ) τ^(iσ) ⟨(ℳu)(σ), φ⟩ dσ for γ = γ_+. The integrand is holomorphic on {Im σ ≥ −γ_+} and
O(⟨σ⟩^(ν_1−2L)) uniformly on {|Re σ| ≥ 2} in each horizontal strip (|1 + σ²| ≥ |σ|²/2 there), so the contour may be
moved to Im σ = γ for every γ ≥ max(2, −γ_+). There |τ^(iσ)| = τ^(−γ), and for τ > τ_− the integral is at most
C (τ_−/τ)^γ → 0 as γ → ∞. So ⟨u(τ, ·), φ⟩ = 0 for τ > τ_−, for every φ: supp u ⊂ {τ ≤ τ_−}. ∎

#### A support lemma, and the proof of strong uniqueness {#sec:ii-f-6-5}

*Fixed-σ transforms.* Let m ∈ ℤ and v ∈ H^(m,(a,b,c))_ebe with τ-support in a compact interval [τ_1, τ_2] ⊂ (0, ∞).
Then σ ↦ (ℳv)(σ) is entire with values in H^(m,(a,c))_(0,b)(ι⁺), and

    ‖(ℳv)(σ)‖_(H^(m,(a,c))_(0,b)) ≤ C ⟨σ⟩^(|m|) max(τ_1^(Im σ), τ_2^(Im σ)) ‖v‖_(H^(m,(a,b,c))_ebe).     {#eq:ii-f-6-7}

Indeed, the spatial fields among [[eq:ii-f-6-1]] (R∂_R, Z_a near cf; v∂_v, √v Z_a near 𝓘⁺) are the 0,b-fields of ι⁺ at
bounded frequency and commute with ℳ, while τ∂_τ and Rτ∂_τ become iσ and iσR. For m ≥ 0, [[eq:ii-f-6-7]] without the
factor ⟨σ⟩^(|m|) follows from the Cauchy–Schwarz inequality in τ on [τ_1, τ_2]. For m < 0 write v = Σ_(|α|≤|m|)
V^α v_α with V^α products of the fields [[eq:ii-f-6-1]] and v_α ∈ H^(0,(a,b,c)) supported in a slightly larger compact
τ-interval, Σ ‖v_α‖ ≤ C‖v‖; the weights commute with the fields up to bounded factors.

*Comparison of norms at fixed h.* For constant orders and h ∈ (0, 1], the norms of H^((m;a,c,l;𝖻))_((0ħ,cħ,h)) and of
H^(m,(a,c))_(0,b) are equivalent with constants C h^(−ν) and C⁻¹ h^ν, ν depending on |m|, |a|, |c|, |l| and sup|𝖻|.
Indeed, the cells of the structure at parameter h are those of the 0,b-structure rescaled by factors in [h, 1] (the
scalings (1 + ρ_K|σ|)⁻¹, ⟨σ⟩⁻¹, x_I⟨σ⟩⁻¹ of [[sec:ii-a-6-2]] against 1, 1, x_I), and the weights ρ_cf^c ρ_tf^l ρ_sf^𝖻
differ from ρ_K^c by factors in [h^ν, h^(−ν)], as ρ_tf = h + ρ_K, ρ_sf = h/(h + ρ_K) and ρ_cf = ρ_K/(h + ρ_K)
([[sec:ii-f-2-1]]).

The support lemma below uses the Paley–Wiener–Schwartz theorem, [[thm:std-paley-wiener]], in dimension one: *a
distribution u on ℝ with compact support in an interval [a, b] has an entire Fourier–Laplace transform û(ζ) =
∫ e^(−itζ) u(t) dt with |û(ζ)| ≤ C (1 + |ζ|)^ν e^(H(Im ζ)) for some C, ν, where H(η) := sup_(t∈[a,b]) tη is the
supporting function of [a, b]; conversely, an entire function with such a bound is the Fourier–Laplace transform of a
distribution supported in [a, b].*

**Lemma {#lem:ii-f-6-4}** (Support.) Let m ∈ ℤ, T > 0, and let w ∈ H^(m,(2γ_I,γ_+,γ_cf))_ebe have τ-support in a
compact subset of (0, ∞), with N_ι⁺(P_0) w ∈ H^(m−1,(2γ_I+2,γ_++2,γ_cf−2))_ebe supported in {t_* ≥ T}. Then w is
supported in {t_* ≥ T}.

*Proof.* Let f := N_ι⁺(P_0) w, so that N⁰w = τ⁻² f, and let supp w ⊂ {τ_1 ≤ τ ≤ τ_2}. W(σ) := (ℳw)(σ) and
F(σ) := ℳ(τ⁻² f)(σ) are entire, N⁰(σ) W(σ) = F(σ) by [[eq:ii-f-1-6]], and by [[eq:ii-f-6-7]], as τ ≤ T⁻¹ on supp f,

    ‖F(σ)‖_(H^(m−1,(2γ_I+2,γ_cf−2))_(0,b)) ≤ C ⟨σ⟩^(|m−1|) T^(−Im σ),      Im σ ≥ 0.

For Im σ ≥ −γ_+, W(σ) ∈ 𝒳^m, and [[prop:ii-f-5-1]] (invertibility on 𝒳^m; any order) gives W(σ) = N⁰(σ)⁻¹ F(σ). Let
φ ∈ C_c^∞((ι⁺)°) and η_0 := max(0, −γ_+). For |σ| ≥ √2 h_0⁻¹, Im σ ≥ η_0, write σ = h⁻¹ z with z in one of the families
[[eq:ii-f-3-2]] ([[sec:ii-f-3-1]]). At this fixed h, W(σ) ∈ H^𝐨 with the fibre order m (any order is allowed there)
and the sf-orders of [[sec:ii-f-3-1]], and [[eq:ii-f-3-4]] gives ‖W(σ)‖_𝐨 ≤ C ‖h² F(σ)‖_(Y_𝐨); with the comparison of
norms and the compact support of φ in (ι⁺)°, |⟨W(σ), φ⟩| ≤ C h^(−ν) ‖F(σ)‖_(H^(m−1,(2γ_I+2,γ_cf−2))_(0,b)). On the
compact set {|σ| ≤ √2 h_0⁻¹, Im σ ≥ η_0} use the continuity of [[cor:ii-f-5-9]]. Hence |⟨W(σ), φ⟩| ≤ C ⟨σ⟩^(ν_1)
T^(−Im σ) for Im σ ≥ η_0. In the strip 0 ≤ Im σ ≤ η_0, which is empty unless γ_+ < 0 and where the families
[[eq:ii-f-3-2]] and the invertibility are not available, [[eq:ii-f-6-7]] alone gives |⟨W(σ), φ⟩| ≤ C ⟨σ⟩^(|m|)
τ_2^(Im σ), and τ_2^(Im σ) and T^(−Im σ) are bounded above and below there. Taking ν_1 ≥ |m|,

    |⟨W(σ), φ⟩| ≤ C ⟨σ⟩^(ν_1) T^(−Im σ),      Im σ ≥ 0.

In t := −log τ, the Mellin transform [[eq:ii-f-1-3]] of the compactly supported distribution τ ↦ ⟨w(τ, ·), φ⟩ is its
Fourier transform ∫ e^(iσt) ⟨w, φ⟩ dt, as τ^(−iσ) = e^(iσt). It is entire and, the support lying in t ∈ [−log τ_2,
−log τ_1], it is bounded by C ⟨σ⟩^(ν_1) e^((log τ_1) Im σ) for Im σ ≤ 0 (|e^(iσt)| = e^(−t Im σ), largest at t =
−log τ_1). With the last bound for Im σ ≥ 0 it is bounded by C ⟨σ⟩^(ν_1) e^(H(Im σ)), H(η) := sup{−tη : t ∈ [log T,
−log τ_1]}; this is the supporting function of that interval for the transform σ ↦ û(−σ), û(ζ) = ∫ e^(−itζ) u dt. By
the Paley–Wiener–Schwartz theorem ([[thm:std-paley-wiener]]) the support lies in {t ≥ log T} = {t_* ≥ T}. As φ is
arbitrary, supp w ⊂ {t_* ≥ T}. ∎

*Proof of [[prop:ii-f-6-2]] (2).* The proof uses only the integer order s″ := ⌊inf 𝗌⌋, and not part (1).

*Reduction.* Work in (t_*, r, ω), in which N_ι := N_ι⁺(P_0) is [[eq:ii-f-1-7]]: translation-invariant in t_* and
homogeneous under D_Λ ([[sec:ii-f-6-3]]). ũ is a distribution on {t_* > 0, r > 0}, supported in {t_* ≥ τ_0⁻¹}, and on
{r < R_0 t_*} it lies locally in the edge space of order s″ with weight γ_cf at r = 0. Pick Λ ≥ 1 with Λτ_0⁻¹ ≥ 4R_0⁻¹,
replace ũ by D_Λ ũ (with the same properties, τ_0/Λ in place of τ_0, as {R < R_0} is D_Λ-invariant), and then translate
t_* by 1 − Λτ_0⁻¹. The new ũ solves N_ι ũ = 0 on {r > 0}, vanishes for t_* < 1, and on {t_* ≥ 1, r < 4}, which lies in
the old {R < R_0} because the old t_* is ≥ Λτ_0⁻¹ ≥ 4R_0⁻¹ there, it is locally of edge order s″ with weight γ_cf at
r = 0. We show ũ = 0 on {t_* < 2}. The same argument after a further translation by 1 (the properties persist, the
region {t_* ≥ 1, r < 4} moving into itself) then gives ũ = 0 on {t_* < j} for every j, so ũ = 0.

*The extension.* Let χ_(t_*) ∈ C^∞(ℝ) equal 1 near (−∞, 2] and 0 near [3, ∞), χ_r ∈ C_c^∞([0, 3)) equal 1 near
[0, 2], and χ^♭_(t_*) ∈ C^∞(ℝ) equal 1 on (−∞, 2] and supported in {χ_(t_*) = 1}. Then g := χ_(t_*)[N_ι, χ_r] ũ ∈
H^(s″−1)_c is supported in {1 ≤ t_* ≤ 3, 2 ≤ r ≤ 3}; let u_ext be the solution of N_ι u_ext = g on {t_* < 3} of
[[lem:ii-f-6-3]] (T = 1, s′ = s″), which vanishes where t_* + 2r < 5 (the support argument there) and satisfies
χ^♭_(t_*) u_ext ∈ H^(s″,2γ_I)_e near 𝓘⁺. Put

    w := χ_(t_*) χ_r ũ − χ^♭_(t_*) u_ext,
    f := N_ι w = [N_ι, χ_(t_*)](χ_r ũ) + χ_(t_*)(1 − χ^♭_(t_*))[N_ι, χ_r] ũ − [N_ι, χ^♭_(t_*)] u_ext.

w is supported in {1 ≤ t_* ≤ 3}, that is τ ∈ [1/3, 1], and lies in H^(s″,(2γ_I,γ_+,γ_cf))_ebe (any τ-weight): near
r = 0 it is χ_(t_*) ũ, near 𝓘⁺ it is −χ^♭_(t_*) u_ext, and in between it is in H^(s″)_loc. Each term of f is supported in
{2 ≤ t_* ≤ 3}, that is τ ∈ [1/3, 1/2], and f ∈ H^(s″−1,(2γ_I+2,γ_+,γ_cf−2))_ebe by [[eq:ii-f-6-2]] (the commutators are
first-order ebe-operators with the weights of N_ι, or better).

*Support.* By [[lem:ii-f-6-4]] with m = s″ and T = 2, w is supported in {t_* ≥ 2}.

*Conclusion.* On {t_* < 2}, χ_(t_*) = χ^♭_(t_*) = 1, so χ_r ũ = u_ext there, and u_ext = 0 where t_* + 2r < 5, which
contains {t_* < 2, r < 3/2}. Hence ũ = 0 on {t_* < 2, r < 3/2}. Let ū be ũ on X := {t_* < 2} ⊂ ℝ^(1+4), extended by 0
across {r = 0} and to {t_* ≤ 0}; as ũ vanishes on {t_* < 2, r < 3/2} and on {t_* < 1}, ū ∈ 𝒟′(X), and Ñū = 0 on X, with
Ñ of [[lem:ii-f-6-3]] (Ñ = N_ι on {r > 1/2}, and ū = 0 on {r < 3/2}). t is a time function for ḡ, supp ū ⊂ {t_* ≥ 1}
⊂ {t ≥ 1}, and for p ∈ X the Minkowski causal past J⁻(p) lies in X (t_* is non-decreasing along future causal curves,
[[lem:ii-f-1-4]] (c)) and meets {t ≥ 1/2} in a compact set. [[lem:ii-f-1-3]] with the time function t, c := 1/2 and
L_p := J⁻(p) ∩ {t ≥ 1/2} gives ū = 0, so ũ = 0 on {t_* < 2}. ∎

[Hin26c] proves part (2) by solving N_ι w′ = f with part (1) and comparing w with w′ by uniqueness. That needs f in the
space of part (1), with the variable admissible order 𝗌 near 𝓘⁺, where the extension u_ext is controlled only at a
constant order; [[lem:ii-f-6-4]] avoids this, using only [[prop:ii-f-5-1]] at a constant order and the high-energy
estimate [[eq:ii-f-3-4]].

### The modified operator P_+ {#sec:ii-f-7}

This section is [Hin26c, Section 10.2] in dimension 4 + 1.

#### Definition and structure {#sec:ii-f-7-1}

**Definition {#def:ii-f-7-1}** (The modified operator.) Let χ ∈ C_c^∞([0, 2)), 0 ≤ χ ≤ 1, equal 1 near [0, 1], and
write χ = χ(R). Let T_+ := max(2, 2r_0). On {t_* > T_+} × ι⁺, that is on (0, T_+⁻¹)_τ × ι⁺,

    P_+ := χ N_ι⁺(P_0) + (1 − χ) P_0.

On supp(1 − χ), R ≥ 1, so r = R t_* > T_+ ≥ 2r_0 lies in the domain of P_0 ([[def:ii-c-1-1]]); N_ι⁺(P_0) is defined on
{r > 0} by [[eq:ii-f-1-7]]. This is [Hin26c, Definition 10.13] in dimension 4 + 1; [Hin26c] takes {t_* > 1}, and T_+
only keeps the domain of P_0 in view.

**Lemma {#lem:ii-f-7-2}** (Structure of P_+.) (a) P_+ ∈ x_I² τ² ρ_cf⁻² Diff²_ebe([0, T_+⁻¹) × ι⁺).
(b) P_+ − N_ι⁺(P_0) ∈ x_I² τ³ ρ_cf⁻² Diff²_ebe: N_ι⁺(P_0) is the normal operator of P_+ at τ = 0 ([Hin26c, (10.51)]).
(c) P_+ is principally scalar with principal symbol G_χ := χḠ + (1 − χ)G_0, the dual metric function of g_χ⁻¹ := χḡ⁻¹ +
(1 − χ)g_0⁻¹, which is Lorentzian on {τ < τ_1} for some τ_1 > 0; dt_* is past causal for g_χ; and g_χ = ḡ on {R ≤ 1}.

*Proof.* (a) On {R < 1}, P_+ = N_ι⁺(P_0) and [[eq:ii-f-6-2]] applies. On {R > 1/2}, (τ, R, ω) ↦ (t_* = τ⁻¹, r = Rτ⁻¹,
ω) identifies [0, T_+⁻¹) × ι⁺ with a neighbourhood of ι⁺ ∩ {R > 1/2} in M, away from K⁺. There the ebe-fields
[[eq:ii-f-6-1]] are the e3b-fields ([[sec:ii-a-2-4]]: b-fields over (ι⁺)°, eb-fields near ι⁺ ∩ 𝓘⁺), ρ_+ ∼ τ, and P_0 ∈
x_I² ρ_+² Diff²_e3b ([[lem:ii-c-1-4]] (b)), as is N_ι⁺(P_0) by [[lem:ii-f-1-2]]. (b) P_+ − N_ι⁺(P_0) = (1 − χ)(P_0 −
N_ι⁺(P_0)) is supported in {R ≥ 1}, and [[eq:ii-f-1-9]] applies. (c) The principal symbols are Ḡ Id for N_ι⁺(P_0)
([[eq:ii-f-1-7]]–[[eq:ii-f-1-8]]) and G_0 Id for P_0 ([[def:ii-c-1-1]]). By [[eq:ii-b-1-2]] of [[lem:ii-b-1-1]], for the
inverses, ρ_0⁻² x_I⁻² ρ_+⁻² (g_0⁻¹ − ḡ⁻¹) ∈ ρ_0² x_I² ρ_+² C^∞(M; S² ᵉ³ᵇTM), and ρ_0, x_I are bounded below on
{1 ≤ R ≤ 2} near ι⁺. So on supp χ ∩ supp(1 − χ) ⊂ {1 ≤ R ≤ 2} the normalised difference x_I⁻² ρ_+⁻² (g_χ⁻¹ − g_0⁻¹) =
χ x_I⁻² ρ_+⁻² (ḡ⁻¹ − g_0⁻¹) is O(ρ_+²), and the convex combination is Lorentzian for τ small, as in [[def:ii-c-3-1]],
remark (b). In dimension 4 + 1 the relative decay of g_0 − ḡ at (ι⁺)° is ρ_+², the mass term being O(r⁻²). Finally
Ḡ(dt_*) = 0 (dt_* is null for ḡ, [[sec:ii-f-1-2]]) and G_0(dt_*) < 0 with dt_* past directed on {r ≥ T_+}
([[lem:ii-b-1-1]], [Hin26c, Lemma 4.4]), so G_χ(dt_*) ≤ 0, past directed. ∎

#### Orders {#sec:ii-f-7-2}

Let 𝗌 be admissible for P_0 with weights α_+, 0 and margin 0 ([[def:ii-c-5-2]]), and let it meet the lower thresholds
(4) and (6) of [[def:ii-c-2-4]] with margin 1. An order admissible with margin 1 does, and so does its sum with 1, which
has margin 0 at the upper threshold (5); [[sec:ii-f-8]] uses both. Let 𝗌_I be the τ-dilation-invariant extension of
𝗌|_(ᵉ³ᵇS*_ι⁺M) ([[sec:ii-f-6-1]]), and

    𝗌′ := χ(R) 𝗌_I + (1 − χ(R)) 𝗌      on ᵉᵇᵉS*([0, T_+⁻¹) × ι⁺).                                        {#eq:ii-f-7-1}

Fix η_1 > 0 so small that 𝗌_♭ := 𝗌 − 1 − η_1 is admissible with weights α_+, 0 and margin 0. This is possible: the
threshold conditions (4)–(6) of [[def:ii-c-2-4]] are strict inequalities for the constant values of 𝗌 near finitely
many radial sets, 𝗌 meets the lower ones (4), (6) with margin 1, and lowering 𝗌 only helps at the upper one (5); and
(1)–(3) of [[def:ii-c-2-4]] and (2)–(5) of [[prop:ii-c-5-1]] are unaffected by subtracting a constant. Let 𝗌_(♭,I) be
its τ-dilation-invariant extension.

**Lemma {#lem:ii-f-7-3}** (The orders near ι⁺.) There is τ_1 ∈ (0, T_+⁻¹), not larger than that of [[lem:ii-f-7-2]] (c)
and with τ_1⁻¹ at least the t_1 of [[lem:ii-f-1-4]] (b), such that on {τ ≤ τ_1}:

(a) 𝗌′ = 𝗌_I on {R ≤ 10}, 𝗌′ = 𝗌 on {R ≥ 1}, and 𝗌_(♭,I) + 1 ≤ 𝗌′.

(b) 𝗌′ is non-increasing along the future null-bicharacteristic flow of every principally scalar operator whose dual
metric is g⁻¹ = g_χ⁻¹ + k with k supported in {τ ≤ τ_1} ∩ {R ≥ 1} and small in the norm of [[prop:ii-c-5-1]] (2), or
with k = 0.

(c) 𝗌′ is constant near the radial sets R_(𝓘⁺,in,+), R_(𝓘⁺,out) (over ι⁺ ∩ 𝓘⁺; [[def:ii-b-7-1]]) and near R_(cf,in),
R_(cf,out), the τ-invariant extensions over cf of ∂R_(∂K⁺,in), ∂R_(∂K⁺,out) under the identification ᵉᵇᵉT*_(ι⁺∩cf) =
³ᵇT*_(ι⁺∩K⁺)M_0 of [Hin26c, (10.44)], and satisfies there the thresholds (5)–(6) of [[def:ii-c-2-4]] with α_sf = α_+,
α_K = 0, margin 0. The same holds for 𝗌_(♭,I) in place of 𝗌′ near R_(cf,in/out) and R_(𝓘⁺,in,+).

*Proof.* (a) By [[prop:ii-c-5-1]] (3), 𝗌 is invariant under (t_*, r, ω) ↦ (Λt_*, Λr, ω) on a neighbourhood of
ι⁺ ∩ {R ∈ [1, 10]}, which contains {τ ≤ τ_1, R ∈ [1, 10]} for τ_1 small; there 𝗌 = 𝗌_I, which gives the first two
claims (on {1 ≤ R ≤ 2}, 𝗌′ = χ𝗌 + (1 − χ)𝗌). For the third: on {R ≤ 10}, 𝗌_(♭,I) + 1 = 𝗌_I − η_1 < 𝗌_I = 𝗌′; on
{R ≥ 1}, 𝗌′ = 𝗌, and 𝗌 is uniformly continuous on the compact set ᵉᵇᵉS*_({τ ≤ T_+⁻¹/2, R ≥ 1}) (where it is a smooth
function on ᵉ³ᵇS*M) and equals 𝗌_I at τ = 0, so |𝗌 − 𝗌_I| ≤ η_1 there for τ_1 small, and 𝗌_(♭,I) + 1 = 𝗌_I − η_1 ≤ 𝗌.

(b) On {R ≤ 1} the metric is ḡ (also for g, as k vanishes there) and 𝗌′ = 𝗌_I. Ḡ and 𝗌_I are invariant under
τ-dilations, so the rescaled Hamilton derivative 𝖧_Ḡ 𝗌_I is dilation-invariant; at τ = 0 it equals 𝖧_(G_0) 𝗌 over ι⁺,
since N_ι⁺(P_0) is the normal operator of P_0 at ι⁺ and their principal symbols agree there ([[lem:ii-f-1-2]],
[[eq:ii-f-1-9]]), and ±𝖧_(G_0) 𝗌 ≤ 0 on ∂Σ^± ([[def:ii-c-2-4]] (1), [[prop:ii-c-5-1]] (2) with h = 0). Every point is a
limit of its dilates towards τ = 0, so ±𝖧_Ḡ 𝗌_I ≤ 0 everywhere. On {R ≥ 1}, 𝗌′ = 𝗌 by (a), and g⁻¹ − g_0⁻¹ = χ(ḡ⁻¹ −
g_0⁻¹) + k. Let ψ(τ/τ_1) be a cut-off in time (ψ = 1 on [0, 1], supported in [0, 2)) and φ ∈ C^∞(ℝ) equal to 0 on
(−∞, 1/2] and 1 on [3/4, ∞). The dual metric g_0⁻¹ + ψ(τ/τ_1) φ(R) (χ(ḡ⁻¹ − g_0⁻¹) + k) on Ω equals g⁻¹ on {τ ≤ τ_1,
R ≥ 3/4}, and its difference from g_0⁻¹ has norm in 𝒢̃^(1,(2ℓ_I,ℓ_+,ℓ_K)) (ℓ_+ ≤ 1) at most C τ_1^(2−ℓ_+) plus that of k:
on its support R ≥ 1/2, so that ρ_+ ≤ 3τ and ρ_K ≥ 1/3, and on supp χ, where ρ_0 and x_I are bounded below, ḡ − g_0 has
relative decay ρ_0² x_I² ρ_+² ([[eq:ii-b-1-2]]). Without φ the modified metric would be ḡ near ι⁺ ∩ K⁺, where it is not
close to g_0. For τ_1 and k small, [[prop:ii-c-5-1]] (2) gives ±𝖧_G 𝗌 ≤ 0 on ∂Σ^±.

(c) Near ι⁺ ∩ 𝓘⁺, 𝗌′ = 𝗌, constant near those radial sets by [[prop:ii-c-5-1]] (5). Near cf, 𝗌′ = 𝗌_I, the
dilation-invariant extension of 𝗌 restricted to the phase space over ι⁺ ∩ K⁺ identified by [Hin26c, (10.44)]; 𝗌 is
constant near ∂R_(∂K⁺,in/out) with the thresholds (5)–(6) of [[def:ii-c-2-4]] ([[prop:ii-c-5-1]] (1)), and so is 𝗌_I
near their τ-invariant extensions, with the same values. For 𝗌_(♭,I) the same holds, by the choice of η_1. ∎

#### The statement {#sec:ii-f-7-3}

Fix τ_0 ∈ (0, C′τ_1/2), with C′ < 1 of [[lem:ii-c-3-2]] (b), to be decreased in [[sec:ii-f-7-6]]; then τ_0 < 1/4 and
τ_0 < C′/(1 + C′). Spaces are those of [[eq:ii-f-6-3]] on [0, τ_0] × ι⁺.

**Proposition {#prop:ii-f-7-4}** (Forward solutions of P_+.) Let 𝗌, 𝗌′ be as in [[sec:ii-f-7-2]]. There is τ_0 ∈
(0, C′τ_1/2) such that, for all γ_I < 3/2 + S̄, γ_+ < min(γ_I, 1 + β_+), γ_cf := −(α_+ + 2) and k ∈ ℕ₀:

(1) (*Existence.*) For every f ∈ Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)([0, τ_0] × ι⁺) there is a forward solution
u ∈ Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b)([0, τ_0] × ι⁺) of P_+ u = f, with ‖u‖ ≤ C‖f‖ in these norms.

(2) (*Strong uniqueness.*) If ũ ∈ 𝒟′((0, ∞) × (ι⁺)°) is supported in {τ ≤ τ_0}, P_+ ũ = 0, and ũ ∈
H^(𝗌′,γ_cf)_(e,loc)((0, ∞)_τ × {R < R_0}) for some R_0 > 0, then ũ = 0.

τ_0 depends on 𝗌 and P_0 only through [[sec:ii-f-7-6]]; the dependence on the weights is only through the constants.
The hypotheses on (γ_I, γ_+) are those of [[prop:ii-f-6-2]]. This is [Hin26c, Proposition 10.14] in dimension 4 + 1.

#### Strong uniqueness {#sec:ii-f-7-4}

*Proof of [[prop:ii-f-7-4]] (2).* As for [[prop:ii-f-6-2]] (2), only the region near r = 0 is non-standard. Let
s″ := ⌊inf 𝗌′⌋ and μ := min(1, R_0τ_0⁻¹/3), and work in (t_*, r, ω). As τ_0 < 1/3, for t_* ≥ τ_0⁻¹ we have {r ≤ 3μ} ⊂
{R < 1}, where P_+ = N_ι := N_ι⁺(P_0), and {r < 3μ} ⊂ {r < R_0 t_*}, where the hypothesis gives ũ edge order s″ with
weight γ_cf at r = 0; no rescaling of P_+ is needed. N_ι is t_*-translation invariant and homogeneous, so
[[lem:ii-f-6-3]] holds with its lengths multiplied by μ (apply it to D_(1/μ) g and rescale, Ñ becoming Ñ_μ, equal to N_ι
on {r > μ/2}): for g ∈ H^(s′−1)_c supported in {T ≤ t_* ≤ T + 2μ, 2μ ≤ r ≤ 3μ} there is a unique u on {t_* < T + 2μ},
vanishing for t_* < T and where t_* + 2r < T + 4μ, with N_ι u = g and χ(t_*) u ∈ H^(s′,2γ)_e near 𝓘⁺ for χ ∈
C_c^∞((−∞, T + 2μ)). Let t_(*,0) ≥ τ_0⁻¹ be such that ũ = 0 on {t_* < t_(*,0)}; t_(*,0) = τ_0⁻¹ is one, by the support
condition. We show ũ = 0 on {t_* < t_(*,0) + μ/2}; iterating in steps of μ/2 gives ũ = 0.

Let χ_r ∈ C_c^∞([0, 3μ)) equal 1 near [0, 2μ]. Then N_ι(χ_r ũ) = P_+(χ_r ũ) = [P_+, χ_r] ũ =: g on {t_* ≥ t_(*,0)},
with g supported in {2μ ≤ r ≤ 3μ} and in H^(s″−1)_loc. Let χ_g ∈ C^∞(ℝ) equal 1 on (−∞, t_(*,0) + μ] and 0 on
[t_(*,0) + 3μ/2, ∞), and let u_mid solve N_ι u_mid = −χ_g g on {t_* < t_(*,0) + 2μ} as above (T = t_(*,0), s′ = s″): it
vanishes for t_* < t_(*,0) and where t_* + 2r < t_(*,0) + 4μ, and is in H^(s″,2γ_I)_e near 𝓘⁺ for t_* < t_(*,0) + 2μ.
Then N_ι(χ_r ũ + u_mid) = 0 on {t_* ≤ t_(*,0) + μ}. Let χ_(t_*) ∈ C^∞(ℝ) equal 1 on (−∞, t_(*,0) + μ/2] and 0 on
[t_(*,0) + μ, ∞), and w := χ_(t_*)(χ_r ũ + u_mid). w has compact τ-support, lies in H^(s″,(2γ_I,γ_+,γ_cf))_ebe (near
r = 0 by hypothesis, near 𝓘⁺ by [[lem:ii-f-6-3]], in between H^(s″)_loc), and N_ι w = [N_ι, χ_(t_*)](χ_r ũ + u_mid) is
supported in {t_* ≥ t_(*,0) + μ/2}. By [[lem:ii-f-6-4]], w is supported in {t_* ≥ t_(*,0) + μ/2}. So on {t_* < t_(*,0) +
μ/2}, χ_r ũ = −u_mid, which vanishes where t_* + 2r < t_(*,0) + 4μ, in particular on {t_* < t_(*,0) + μ/2, r < 7μ/4};
hence ũ = 0 there.

On the rest of {t_* < t_(*,0) + μ/2} we use [[lem:ii-f-1-3]]. Let X := {τ_1⁻¹ < t_* < t_(*,0) + μ/2}, in the
coordinates (t, x) of ℝ^(1+4), t = t_* + r; let ū be the distribution on X equal to ũ on {r > 0} and to 0 on
{r < 7μ/4}, which is consistent; and let P̃ be the operator equal to P_+ on {r > μ/2} and to Ñ_μ on {r < μ}, both being
N_ι on X ∩ {μ/2 < r < μ} ⊂ {R < 1}. P̃ has smooth coefficients and principal symbol G_χ ([[lem:ii-f-7-2]] (c); G_χ = Ḡ
on {R ≤ 1}), and P̃ū = 0 on X. By [[lem:ii-f-1-4]] (b) (τ_1⁻¹ ≥ t_1, [[lem:ii-f-7-3]]), t_* is non-decreasing along
future causal curves of g_χ in X, and t and t^♭_+ are time functions, with C′t_* ≤ t^♭_+ ≤ t_*. supp ū ⊂ {t_* ≥
t_(*,0)} ⊂ {t^♭_+ ≥ C′t_(*,0)}. Take the time function t^♭_+ and c := C′t_(*,0)/2, which exceeds τ_1⁻¹, as t_(*,0) ≥
τ_0⁻¹ and τ_0 < C′τ_1/2. For p ∈ X with t^♭_+(p) > c, J⁻_X(p) ∩ {t^♭_+ ≥ c} lies in L_p := {c ≤ t^♭_+ ≤ t^♭_+(p),
t_* ≤ t_*(p), t ≤ t(p)}, which is compact (r ≤ t(p) − c there) and contained in X (t_* ≥ t^♭_+ ≥ c > τ_1⁻¹).
[[lem:ii-f-1-3]] gives ū = 0, so ũ = 0 on {t_* < t_(*,0) + μ/2}. ∎

#### Finite-time solvability {#sec:ii-f-7-5}

**Lemma {#lem:ii-f-7-5}** (Forward solutions on finite intervals.) Let f be as in [[prop:ii-f-7-4]] (1) and T ≥ τ_0⁻¹.
There is a unique u on {τ_0⁻¹ ≤ t_* < T}, vanishing near t_* = τ_0⁻¹, with P_+ u = f there and ψ_T u ∈
Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b) for every ψ_T ∈ C_c^∞((−∞, T)) (a function of t_*), with ‖ψ_T u‖ ≤ C_(T,ψ_T) ‖f‖.
The same holds for the operators P^ε_+ of [[sec:ii-f-7-6]], ε ∈ (0, τ_0], in place of P_+, with constants independent
of ε.

*Proof.* *Uniqueness* follows from [[prop:ii-f-7-4]] (2), proved above: the difference of two solutions, cut off by ψ_T
near t_* = T, solves P_+ v = 0 on {t_* < T′} for T′ < T, and the argument of [[sec:ii-f-7-4]] is local in time.

*Existence, one step.* Let t_(*,0) ≥ τ_0⁻¹ and f_0 ∈ Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b), supported in {t_* ≥
t_(*,0)}. By [[lem:ii-f-7-3]] (a), 𝗌′ = 𝗌_I on {R ≤ 10}, so χf_0 ∈ Ḣ^((𝗌_I−1;k),(∞,γ_++2,γ_cf−2)), and
[[prop:ii-f-6-2]] (1) gives the forward solution u_cf of N_ι u_cf = χf_0, with χu_cf ∈ Ḣ^((𝗌_I;k),(∞,γ_+,γ_cf)). Let
χ^♭ = χ^♭(R) equal 1 near [0, 1], supported in χ⁻¹(1). As P_+ = N_ι on {χ = 1}°,

    f_1 := f_0 − P_+(χ^♭ u_cf) = (1 − χ^♭) f_0 − [N_ι, χ^♭](χ u_cf) ∈ Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,∞)),

supported in {R ≥ 1} ∩ {t_* ≥ t_(*,0)}, with norm ≤ C‖f_0‖. Next we solve P_+ u_mid = f_1 on {t_* ≤ 2t_(*,0)}. Let ψ,
ψ̃ ∈ C^∞(ℝ), ψ = 0 on (−∞, 1/2], ψ = 1 on [1, ∞), ψ̃ = 1 on (−∞, 2], ψ̃ = 0 on [3, ∞), and on Ω

    P_aux := P_0 + ψ(8r/t_(*,0)) ψ̃(t_*/t_(*,0)) (P_+ − P_0).

P_+ − P_0 = χ(N_ι − P_0) is supported in {R ≤ 2}. On the support of the cut-offs, r ≥ t_(*,0)/16 and t_* ≤ 3t_(*,0),
and as χ(R) = 0 for R ≥ 2, also t_* ≥ t_(*,0)/32; so the second term lives where ρ_+ ∼ t_(*,0)⁻¹ and R ∈ [1/48, 2],
near (ι⁺)°. There N_ι − P_0 ∈ x_I² ρ_+³ Diff²_e3b ([[lem:ii-f-1-2]]) and the principal symbols differ by O(ρ_+²)
relative to G_0 ([[eq:ii-b-1-2]]); the cut-offs, functions of r/t_(*,0) and t_*/t_(*,0) with r ∼ t_* ∼ t_(*,0) on
their supports, have e3b-derivatives bounded uniformly in t_(*,0). Hence P_aux is weakly admissible relative to P_0
([[def:ii-c-3-3]], p_0 = p̃_1 = 0) with ε_P ≤ C t_(*,0)^(−(1−ℓ_+)) (ℓ_+ < 1), and its metric is close to g_0; for
t_(*,0) large (that is, τ_0 small), the hypotheses of [[sec:ii-e-1-1]] and of [[prop:ii-c-5-1]] (2) hold for P_aux, so 𝗌
is a slab order for it. Let Ω′ = Ω_(T_0,T_1) be a slab containing {t_(*,0) ≤ t_* ≤ 2t_(*,0), r ≥ t_(*,0)/4} and with
f_1 supported in {t^♭ ≥ T_0} there. Then f_1 ∈ H^((𝗌−1;k),2α+2)(Ω′)^(•,−), α := γ_I − 2 < −1/2 + S̄ (𝗌′ = 𝗌 on
{R ≥ 1}, and the weight shift is [[lem:ii-a-6-1]], as in [[sec:ii-f-6-3]]), and [[prop:ii-e-4-3]] gives the forward
solution u_aux ∈ H^((𝗌;k),2α)(Ω′)^(•,−) of P_aux u_aux = f_1, with norm ≤ C‖f_1‖.

*Support and order of u_aux.* u_aux vanishes on {t_* < 2t_(*,0), r < t_(*,0)/4}. To see this, note that the dual metric
of P_aux is G_0 + a(Ḡ − G_0) with a := ψ(8r/t_(*,0)) ψ̃(t_*/t_(*,0)) χ(R) ∈ [0, 1], supported in {r ≥ t_(*,0)/16}, so
[[lem:ii-f-1-4]] (a) applies to it for t_(*,0) ≥ 16(r′_0 + 1), and t^♭ is a time function for it ([[lem:ii-c-3-2]]
(2)). Let ψ_Φ ∈ C^∞(ℝ), 0 ≤ ψ_Φ ≤ 1, vanish on (−∞, 1/32] and equal 1 on [1/16, ∞), and

    Θ := t_* + Φ(r),      Φ(r) := (19/10) ∫_0^r ψ_Φ(r′/t_(*,0)) dr′.

Θ is non-decreasing along future causal curves of g_aux for t_(*,0) large. Where ψ_Φ = 0, dΘ = dt_* ([[lem:ii-f-1-4]]
(a)). Where r ≥ t_(*,0)/32, dΘ = dt_* + Φ′ dr with Φ′ ∈ [0, 19/10], so Ḡ(dΘ) = −Φ′(2 − Φ′) ≤ −Φ′/10, while G_0(dΘ) ≤
G_0(dt_*) − Φ′(2 − Φ′) + C r⁻² Φ′(2 + Φ′) < 0 for r large, by [[lem:ii-b-1-1]] (dt_* is past timelike, and g_0⁻¹ −
ḡ⁻¹ ∈ r⁻² C^∞(M; S²𝒯)); dΘ, which deforms continuously to dt_* through such covectors, is past causal for G_0 and Ḡ,
hence for G_0 + a(Ḡ − G_0) (the cone argument of [[lem:ii-f-1-4]]). For r ≥ t_(*,0)/16, Φ(r) = (19/10) r − κ t_(*,0)
with κ := (19/10) ∫_0^(1/16) (1 − ψ_Φ) ∈ [0, 19/160]. On supp f_1 ⊂ {R ≥ 1, t_* ≥ t_(*,0)}, r ≥ t_* ≥ t_(*,0), so
Θ ≥ (29/10 − κ) t_(*,0) =: a_Θ; on {t_* < 2t_(*,0), r < t_(*,0)/4}, Θ < (2 + 19/40 − κ) t_(*,0) < a_Θ. Let U′ be the
interior of the slab Ω′ ([[sec:ii-e-1-1]]), on which u_aux is defined, and X := U′ ∩ {Θ < a_Θ}. Then P_aux u_aux = f_1 =
0 on X, and supp u_aux ⊂ {t^♭ ≥ T_0}, with T_0 > 2 (enlarging t_(*,0)). For p ∈ X with t^♭(p) > c := T_0/2, J⁻_X(p) ∩
{t^♭ ≥ c} lies in

    L_p := {c ≤ t^♭ ≤ t^♭(p),  Θ ≤ Θ(p),  B ≤ B(p),  r ≥ min(r(p), r^♮)},

which is compact (B bounds t_* and r) and contained in X (t_* ≥ t^♭ ≥ c > 1). By [[lem:ii-f-1-3]], u_aux = 0 on X,
which contains U′ ∩ {t_* < 2t_(*,0), r < t_(*,0)/4}. So on {t_* < 2t_(*,0)}, u_aux solves P_+ u_aux = f_1, as P_aux =
P_+ on {t_* ≤ 2t_(*,0), r ≥ t_(*,0)/8}. Its order is 𝗌; on {R ≥ 1} that is 𝗌′. On {t_(*,0)/4 ≤ r, R ≤ 1, t_* ≤
2t_(*,0)}, an interior region where P_+ = N_ι has smooth coefficients, we upgrade to the order 𝗌′ by real principal
type propagation ([[thm:ii-a1-5-4]]; in the interior b-regularity is regularity, and the k b-derivatives are handled by
the commuted systems of [[lem:ii-d1-2-1]] and [[lem:ii-d1-2-5]]): 𝗌′ is non-increasing along the future flow
([[lem:ii-f-7-3]] (b)), P_+ u_aux = f_1 ∈ H^((𝗌′−1;k)), there are no radial points over the interior, and every backward
null bicharacteristic from a point of this region reaches, within {t_* ≤ 2t_(*,0)}, either {r < t_(*,0)/4} (where
u_aux = 0) or {R ≥ 1} (where it is of order 𝗌 = 𝗌′): radially outgoing ones keep t_* and decrease r backward, the
others leave every compact subset of {t_* ≥ t_(*,0)} backward. With χ_(t_*) equal to 1 for t_* ≤ 3t_(*,0)/2 and 0 for
t_* ≥ 2t_(*,0), u_mid := χ_(t_*) u_aux ∈ Ḣ^((𝗌′;k),(2γ_I,∞,∞))_(ebe;b) with norm ≤ C_(t_(*,0)) ‖f_0‖ (near 𝓘⁺ by
[[lem:ii-a-6-1]] and the identification of e3b- and ebe-spaces there), and

    f_2 := f_1 − P_+ u_mid = −[P_+, χ_(t_*)] u_aux

is supported in {t_* ≥ 3t_(*,0)/2}, with norm ≤ C_(t_(*,0)) ‖f_0‖ in the space of f_0. Thus χ^♭ u_cf + u_mid solves
P_+ u = f_0 on {t_* < 3t_(*,0)/2}, with an error f_2 supported in {t_* ≥ 3t_(*,0)/2}.

*Iteration.* Apply the step to f_2 with 3t_(*,0)/2 in place of t_(*,0), and so on; after j steps the sum of the partial
solutions solves P_+ u = f on {t_* < (3/2)^j τ_0⁻¹}, and (3/2)^j → ∞. The bounds follow step by step. The same argument
applies to P^ε_+ of [[sec:ii-f-7-6]], which equals N_ι on {R ≤ 1} and differs from P_+ only on {τ ≤ 2ε} by a term of
the class [[eq:ii-f-7-6]], so that P_aux built from it satisfies the same smallness uniformly in ε. ∎

#### The a priori estimate, and the proof of existence {#sec:ii-f-7-6}

*Radial estimates at cf.* Near cf, by [Hin26c, (10.44)], the ebe-phase space over {τ = 0, R = 0} is the 3b-phase space
over ∂K⁺ = ι⁺ ∩ K⁺, and P_+ = N_ι is τ-dilation-invariant on {R < 1}. Its rescaled Hamilton field is the
dilation-invariant extension of 𝖧̄ over ∂K⁺ ([[sec:ii-b-3]]), with radial sets R_(cf,in), R_(cf,out) over all of cf:
R_(cf,in) is a saddle whose stable manifold lies over {R > 0} (radially infalling null geodesics) and whose unstable
manifold lies over {R = 0}, which is the stable manifold of R_(cf,out), whose unstable manifold lies over {R > 0}
(radially outgoing null geodesics) ([Hin26c, p. 223]; [[lem:ii-b-3-3]] over ι⁺, extended by invariance). With τ̃ :=
(t_* + r)⁻¹ = τ/(1 + R), whose differential is timelike for ḡ, let ψ_+ ∈ C^∞([0, ∞)) equal 1 near [0, τ_2], vanish on
[2τ_2, ∞), be non-increasing, and have √(−ψ_+ψ′_+) smooth.

**Lemma {#lem:ii-f-7-6}** (Radial estimates at cf.) Let 𝗍 be an order on ᵉᵇᵉS*, τ-dilation-invariant and constant near
R_(cf,in) (resp. R_(cf,out)), with the threshold [[eq:ii-d-3-3]] of [[prop:ii-d-3-2]] (resp. [[eq:ii-d-3-5]] of
[[prop:ii-d-3-3]]) there for α_K = 0. Then [[prop:ii-d-3-2]] and [[prop:ii-d-3-3]], and their b-regular versions
[[prop:ii-d1-5-2]], hold for L = N_ι, P_+ or P^ε_+ near R_(cf,in) (resp. R_(cf,out)) over cf ∩ {τ ≤ τ_2}, with the
ebe-weights (γ_+, γ_cf) for (α_+, α_K) (via α_+ − α_K = −γ_cf − 2, [[lem:ii-a-6-2]]), for u vanishing on {τ̃ ≥ τ_2}. In
place of condition (4) of [[prop:ii-d-3-2]]: at R_(cf,in) the Schwartz kernel of E is supported away from cf; at
R_(cf,out), WF′(E) is disjoint from the unstable manifold of R_(cf,out) (the τ-invariant extension of ∂W_out =
{ξ̂ = 0, η̂ = 0}, over {R > 0}); in both cases there is an additional term microsupported over supp ψ′_+(τ̃), which
vanishes for such u. This is the estimate of [Hin26c, p. 223].

*Proof.* These are the proofs of [[prop:ii-d-3-2]] and [[prop:ii-d-3-3]] with Ψ := ψ(𝔐_R q) ψ_+(τ̃) ψ(𝔐ρ_cf) in place of
ψ(𝔐_R q) ψ(𝔐ρ_+) ψ(𝔐ρ_K). The quantities at the radial set are unchanged: 𝖧 is the dilation-invariant extension of 𝖧̄,
so ρ⁻¹𝖧ρ, 𝖧q and the imaginary part 𝔭′ (that of N_ι, which at R = 0 is that of P_0 at ∂K⁺, its coefficients being those
of P_0 frozen) take the values used there at every τ. The weight w = τ^(γ_+) ρ_cf^(γ_cf) = ρ_+^(α_+) ρ_K^(α_K)·(smooth
positive) under [Hin26c, (10.44)] gives the same contribution, τ being dilation-invariant (τ⁻¹𝖧τ = 0 at the radial set,
as ρ_+⁻¹𝖧ρ_+ + ρ_K⁻¹𝖧ρ_K = 2 − 2 there). The factor ψ(𝔐ρ_cf) plays the role of ψ(𝔐ρ_K), with the same signs. The factor
ψ_+(τ̃) replaces ψ(𝔐ρ_+): 𝖧(ψ_+²) = 2ψ_+ψ′_+ 𝖧τ̃, and on the future characteristic set 𝖧τ̃ ≤ 0 (τ̃ decreases along
future causal curves), so this is (√(−ψ_+ψ′_+))² · 2(−𝖧τ̃) ≥ 0, a term +e*e microsupported over supp ψ′_+(τ̃) ⊂ {τ̃ ≥
τ_2}, where u = 0. For P_+ and P^ε_+ on {R < 1} the operator is N_ι. ∎

**Lemma {#lem:ii-f-7-7}** (The symbolic estimate.) For τ_0 ≤ τ_2/2 small and every ε ∈ (0, τ_0], with C independent of
ε, every u ∈ Ḣ^((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf))_(ebe;b)([0, τ_0] × ι⁺) with P^ε_+ u ∈
Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b) lies in Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b) and

    ‖u‖_((𝗌′;k),(2γ_I,γ_+,γ_cf))
        ≤ C (‖P^ε_+ u‖_((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2)) + ‖u‖_((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf))).            {#eq:ii-f-7-2}

Here P^ε_+ := χ_0(τ/ε) N_ι + (1 − χ_0(τ/ε)) P_+, with χ_0 ∈ C_c^∞([0, 2)) equal to 1 on [0, 1]. This is [Hin26c,
(10.54)–(10.55)] in dimension 4 + 1.

*Proof.* P^ε_+ − P_+ = −χ_0(τ/ε)(P_+ − N_ι), and by [[lem:ii-f-7-2]] (b)

    {P^ε_+ − N_ι : ε ∈ (0, 1]} is bounded in x_I² τ³ ρ_cf⁻² C^∞_b Diff²_ebe,
    P^ε_+ → P_+ in x_I² τ² ρ_cf⁻² C^∞_b Diff²_ebe,                                                       {#eq:ii-f-7-6}

as χ_0(τ/ε) is bounded in C^∞_b([0, ∞)_τ) and τχ_0(τ/ε) = O(ε) there ([Hin26c, (10.56)]). The dual metric of P^ε_+ is
g_χ⁻¹ + k_ε, k_ε = χ_0(τ/ε)(1 − χ)(ḡ⁻¹ − g_0⁻¹), supported in {τ ≤ 2ε, R ≥ 1} and small; so [[lem:ii-f-7-3]] (b)
applies to it. Now combine, in the ebe-phase space over [0, τ_0] × ι⁺, the following estimates, each valid for P^ε_+
uniformly in ε, in the strong sense, with the orders 𝗌′ (target) and 𝗌_(♭,I) (a priori), and with k b-derivatives:

(i) elliptic estimates off the characteristic set of G_χ ([[thm:ii-a1-3-1]]);

(ii) real principal type propagation along the future flow ([[thm:ii-a1-5-4]]; with k b-derivatives through the
commuted systems of [[lem:ii-d1-2-1]] and [[lem:ii-d1-2-5]]), using [[lem:ii-f-7-3]] (b);

(iii) at R_(𝓘⁺,in,+), the radial saddle estimate [[prop:ii-d-3-5]] ([[prop:ii-d1-3-2]]), where P^ε_+ = P_0 (on
{R ≥ 2}) up to a term vanishing at ι⁺ in the class allowed there, with control on its stable manifold from (ii) along
𝓘⁺ ([[lem:ii-b-7-2]] (3));

(iv) at R_(cf,in), [[lem:ii-f-7-6]] (in), with control on its stable manifold (over {R > 0}: radially infalling null
bicharacteristics, which come backward from {t_* < τ_0⁻¹} or, over ι⁺, from the unstable manifold of R_(𝓘⁺,in,+))
from (ii) and (iii);

(v) at R_(cf,out), [[lem:ii-f-7-6]] (out);

(vi) at R_(𝓘⁺,out), the radial sink estimate [[prop:ii-d-3-6]] ([[prop:ii-d1-3-2]]).

The thresholds hold for 𝗌′ and 𝗌_(♭,I) by [[lem:ii-f-7-3]] (c) (at the incoming sets the a priori order 𝗌_(♭,I) is
above threshold, at the outgoing sets the target order 𝗌′ is below it), and with γ_I < 3/2 + S̄ at 𝓘⁺ ([[prop:ii-d-3-5]]
and [[prop:ii-d-3-6]] at the weight α_I = γ_I − 2). The flow over ι⁺ is that of [[prop:ii-b-8-1]] (pulled back by
τ-invariance near cf), and t_* is non-decreasing along the future flow ([[lem:ii-f-7-2]] (c)). So every point of the
characteristic set over [0, τ_0] × ι⁺ is reached, backward along the flow, either from {t_* < τ_0⁻¹}, where u = 0, or
from one of the radial sets, in the order (iii)–(vi) ([Hin26c, Figure 10.3]). The constants depend on finitely many
seminorms of P^ε_+ in the class of [[eq:ii-f-7-6]] and on the margins, so they are uniform in ε; τ_0 ≤ τ_2/2 makes the
ψ_+-terms of [[lem:ii-f-7-6]] vanish for u supported in {τ ≤ τ_0} (there τ̃ ≤ τ < τ_2). ∎

*Inversion of the normal operator.* For u as in [[lem:ii-f-7-7]], u ∈ Ḣ^((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf)) and

    N_ι u = P^ε_+ u − (P^ε_+ − N_ι) u,
    ‖(P^ε_+ − N_ι) u‖_((𝗌_(♭,I)−1;k),(2γ_I+2,γ_++2,γ_cf−2)) ≤ C ‖u‖_((𝗌_(♭,I)+1;k),(2γ_I,γ_+−1,γ_cf))

by [[eq:ii-f-7-6]] (the factor τ³ against τ² shifts the τ-weight by one). As 𝗌_(♭,I) is the dilation-invariant
extension of an order admissible with weights α_+, 0 and margin 0, the uniqueness and the estimate of
[[prop:ii-f-6-2]] (1) at the order 𝗌_(♭,I) give

    ‖u‖_((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf)) ≤ C ‖N_ι u‖_((𝗌_(♭,I)−1;k),(2γ_I+2,γ_++2,γ_cf−2))
        ≤ C (‖P^ε_+ u‖_((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2)) + ‖u‖_((𝗌′;k),(2γ_I,γ_+−1,γ_cf))),

using 𝗌_(♭,I) + 1 ≤ 𝗌′ ([[lem:ii-f-7-3]] (a)). With [[eq:ii-f-7-2]],

    ‖u‖_((𝗌′;k),(2γ_I,γ_+,γ_cf))
        ≤ C (‖P^ε_+ u‖_((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2)) + ‖u‖_((𝗌′;k),(2γ_I,γ_+−1,γ_cf))).               {#eq:ii-f-7-3}

*Absorption.* Multiplication by χ_0(τ/δ_1) maps H^((𝗌′;k),(2γ_I,γ_+,γ_cf)) to H^((𝗌′;k),(2γ_I,γ_+−1,γ_cf)) with norm ≤
Cδ_1, as it equals τχ_0(τ/δ_1) times the identity of weights, and τχ_0(τ/δ_1) = δ_1·(τ/δ_1)χ_0(τ/δ_1) has
C^∞_b-seminorms O(δ_1). Fix δ_1 with C·Cδ_1 ≤ 1/2 in [[eq:ii-f-7-3]]. For ε < δ_1/2, P^ε_+ = P_+ on {τ ≥ δ_1}, and (1 −
χ_0(τ/δ_1))u is controlled by [[lem:ii-f-7-5]] for P^ε_+, with T := 2δ_1⁻¹ and ψ_T ∈ C_c^∞((−∞, T)) equal to 1 on (−∞,
δ_1⁻¹], with constants independent of ε: the support of 1 − χ_0(τ/δ_1) lies in {t_* ≤ δ_1⁻¹}, where ψ_T = 1 and u is the
finite-time solution by uniqueness. Hence, for u in the space of [[lem:ii-f-7-7]] and ε < δ_1/2,

    ‖u‖_(Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b))
        ≤ C ‖P^ε_+ u‖_(Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)),                                      {#eq:ii-f-7-4}

C independent of ε ([Hin26c, (10.58)]); the absorbed term is finite because [[lem:ii-f-7-7]] places u in the space of
order 𝗌′.

*Proof of [[prop:ii-f-7-4]] (1).* Let f be as in [[prop:ii-f-7-4]] (1) and ε < δ_1/2. Let u^ε_ini be the finite-time
solution of P^ε_+ u = f on {t_* < 2ε⁻¹} ([[lem:ii-f-7-5]] for P^ε_+), and χ_(ε/2) := χ_0(2τ/ε). As P^ε_+ = N_ι on
supp χ_(ε/2) ⊂ {τ ≤ ε},

    u^ε := (1 − χ_(ε/2)) u^ε_ini + N_ι⁻¹(χ_(ε/2) f + [N_ι, χ_(ε/2)] u^ε_ini),

with N_ι⁻¹ the forward solution operator of [[prop:ii-f-6-2]] (1), solves P^ε_+ u^ε = f ([Hin26c, (10.59)]): on
{τ ≤ ε}, P^ε_+ u^ε = N_ι((1 − χ_(ε/2)) u^ε_ini) + χ_(ε/2) f + [N_ι, χ_(ε/2)] u^ε_ini = (1 − χ_(ε/2)) f + χ_(ε/2) f, and
on {τ ≥ ε}, u^ε = u^ε_ini. [[prop:ii-f-6-2]] (1) is applied at the order 𝗌_I − η_1, the dilation-invariant extension of
𝗌 − η_1, which is admissible with margin 0: on {τ ≤ τ_1}, 𝗌′ ≥ 𝗌_I − η_1 by the proof of [[lem:ii-f-7-3]] (a), so the
right-hand side lies in its space. So u^ε ∈ Ḣ^((𝗌_I−η_1;k),(2γ_I,γ_+,γ_cf)) ⊂ Ḣ^((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf)), and
[[lem:ii-f-7-7]] places u^ε in the space of order 𝗌′. By [[eq:ii-f-7-4]], ‖u^ε‖ ≤ C‖f‖ uniformly in ε. A subsequence
u^(ε_j), ε_j → 0, converges weakly to some u ∈ Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b)([0, τ_0] × ι⁺) with ‖u‖ ≤ C‖f‖.
Since P^ε_+ = P_+ on {τ ≥ 2ε}, P_+ u = f on {τ > 2ε_j} for every j, hence on {τ > 0}. ∎

### Forward solutions of P_0 on e3b-spaces {#sec:ii-f-8}

**Theorem {#thm:ii-f-8-1}** (Forward solutions of the stationary model.) Let P_0 be a stationary wave-type operator
([[def:ii-c-1-1]]), in the setting of [[sec:ii-e-1-1]], with Ω_* = cl_M{t^♭ ≥ 1} and its slabs Ω_(1,T). Let α_I,
α_+ ∈ ℝ with

    α_I < −1/2 + S̄,      α_+ < α_I − 1/2.                                                               {#eq:ii-f-8-1}

Assume that P_0 is ℵ-admissible with sf-weight α_+ and sf-loss δ ([[def:ii-c-2-7]]), and let 𝗌 ∈ C^∞(ᵉ³ᵇS*M) be
admissible with weights α_+, −ℵ and margin 0, and with weights α_+, 0 and margin 1 ([[def:ii-c-5-2]]). Let k ∈ ℕ₀ and
f ∈ H^((𝗌;k),(2α_I+2,α_++2,0))_(e3b;b)(Ω_*; E)^(•,−), the space of restrictions to {r > r_0} of elements supported in
{t^♭ ≥ 1}, with the quotient norm ([[sec:ii-a-7]]). The *forward solution* of P_0 u = f on Ω_* is the distribution u on
Ω_*° ∩ {r > r_0} whose restriction to every slab Ω_(1,T) is the forward solution there of [[prop:ii-e-3-4]]: the
restrictions of f lie in the slab spaces, the weights at ι⁺ and K⁺ being bounded above and below at bounded times, and
the solutions on two slabs agree on the smaller by [[prop:ii-e-3-4]] (i). Then there is C_k, independent of f, with

    ‖u‖_(H^((𝗌;k),(2α_I,α_+−δ,−ℵ))_(e3b;b)(Ω_*;E)^(•,−))
        ≤ C_k ‖f‖_(H^((𝗌;k),(2α_I+2,α_++2,0))_(e3b;b)(Ω_*;E)^(•,−)).                                     {#eq:ii-f-8-2}

This is [Hin26c, Theorem 10.1] in dimension 4 + 1. [Hin26c] states it on Ω = {t_* ≥ 1}; it is stated and proved here
on Ω_*, where the slab theory of [[ch:s07]] lives and where [[thm:ii-f1-1-1]] uses it.

The thresholds [[eq:ii-f-8-1]] are those of [Hin26c] at every n. In the b-density weights of [[eq:ii-f-1-2]] they read
γ_I = α_I + 2 < 3/2 + S̄ = c + S̄ and γ_+ = α_+ + 5/2 < γ_I. Indeed, in (τ, R, ω) with t_* = τ⁻¹ and r = Rτ⁻¹, the map
(τ, R) ↦ (t_*, r) has Jacobian determinant −τ⁻³, and |dx| = r³ |dr dω|, |dt dx| = |dt_* dx|; so

    |dt dx| = τ⁻³ (R/τ)³ |dτ dR dω| = R⁴ τ⁻⁵ |(dτ/τ)(dR/R) dω| = 2 x_I⁻⁸ τ⁻⁵ |(dτ/τ)(dx_I/x_I) dω|,

using R = x_I⁻² near ι⁺ ∩ 𝓘⁺. Hence x_I^(2α_I) τ^(α_+) L²(|dt dx|) = x_I^(2(α_I+2)) τ^(α_++5/2) L²(|(dτ/τ)(dx_I/x_I)
dω|): the shifts are n/2 = 2 at 𝓘⁺ and (n + 1)/2 = 5/2 at ι⁺. So α_I < −1/2 + S̄ is γ_I < 3/2 + S̄, and α_+ < α_I − 1/2
is α_+ + 5/2 < α_I + 2, that is γ_+ < γ_I. [Hin26c, Remark 10.2] applies: for P = P_0, p_1 = S|_(∂X), so p̄_1 = S̄,
and [[eq:ii-f-8-1]] is the threshold [[eq:ii-d-1-3]] at 𝓘⁺.

#### The weights {#sec:ii-f-8-1}

With the metric density |dt dx| on Ω and the b-densities of [[sec:ii-f-6-1]], [[lem:ii-a-6-1]] identifies near ι⁺

    H^(0,(2α_I,α_+,α_K))_e3b(|dt dx|) = H^(0,(2(α_I+2),α_++5/2,α_K+1/2))_e3b(|dτ/τ| μ_b),

and, on functions supported away from K⁺ (near 𝓘⁺ and (ι⁺)°), the e3b-spaces are the ebe-spaces of [[eq:ii-f-6-3]] with
the weights

    γ_I := α_I + 2,      γ_+ := α_+ + 5/2,      γ_cf := −(α_+ + 2)                                       {#eq:ii-f-8-3}

(the orders transported by the identification of [[lem:ii-f-7-2]] (a); near ι⁺, τ ∼ ρ_+ on {R ≥ 1/2}). They satisfy the
hypotheses of [[prop:ii-f-6-2]] and [[prop:ii-f-7-4]]: γ_I < 3/2 + S̄ and γ_+ < γ_I by [[eq:ii-f-8-1]]; and γ_+ − 1/2 =
α_+ + 2 = −γ_cf lies in (β_−, β_+), as P_0 is tf-admissible with the weight α_+ + 2 ([[def:ii-c-2-7]] (2)), so γ_+ <
β_+ + 1/2 < 1 + β_+. The buffer 1/2 is explained in [Hin26c, footnote 100]: pointwise decay at ι⁺ is governed by the
resonances, excluded in Im σ > −1 − β_+ ([[prop:ii-f-5-1]]), whereas the 3b-regularity order limits the decay
obtainable by Sobolev embedding.

#### Proof {#sec:ii-f-8-2}

*Proof of [[thm:ii-f-8-1]].* *Step 0: late right-hand sides.* Let τ_0 be as in [[prop:ii-f-7-4]], for the orders 𝗌 and
𝗌 + 1 (both meet its hypotheses: 𝗌 + 1 is admissible with weights α_+, 0 and margin 0 and meets the lower thresholds
with margin 2, as 𝗌 has margin 1); τ_0 < C′τ_1/2 < C′/(1 + C′) ([[sec:ii-f-7-3]]). Let T := τ_0⁻¹ and ψ_T ∈ C^∞(ℝ)
equal 1 on (−∞, T] and 0 on [T + 1, ∞), a function of t_*. 𝗌 + 1 is a slab order ([[sec:ii-e-3-2]]: admissible orders
are, and adding a constant preserves the conditions), so [[prop:ii-e-4-3]], with P = P_0, the slab order 𝗌 + 1 and the
weight α_I < −1/2 + S̄, gives on the slab Ω_(1,T+2) the forward solution u_0 of P_0 u_0 = f, with

    ‖u_0‖_(H^((𝗌+1;k),2α_I)(Ω_(1,T+2))^(•,−)) ≤ C ‖f‖_(H^((𝗌;k),2α_I+2)(Ω_(1,T+2))^(•,−)) ≤ C ‖f‖,

the last norm that of [[eq:ii-f-8-2]]: on Ω_* ∩ {t^♭ ≤ T + 2}, t_* ≤ (T + 2)/C′, so the weights at ι⁺ and K⁺ are bounded
above and below there. As t^♭ ≤ t_*, supp ψ_T ⊂ {t^♭ ≤ T + 1}, inside the slab, so ψ_T u_0, extended by 0, lies in the
spaces on Ω_* of order 𝗌 + 1 with any weights at ι⁺ and K⁺, with norm ≤ C‖f‖, and P_0(ψ_T u_0) = ψ_T f + [P_0, ψ_T]
u_0. So f_1 := f − P_0(ψ_T u_0) = (1 − ψ_T) f − [P_0, ψ_T] u_0 is supported in {t_* ≥ T}, and, [P_0, ψ_T] ∈ x_I² ρ_+²
Diff¹_e3b having coefficients supported in {T ≤ t_* ≤ T + 1}, ‖f_1‖ ≤ C‖f‖ in the space of [[eq:ii-f-8-2]]. The forward
solution of P_0 u = f on Ω_* is ψ_T u_0 + u_1, u_1 that of P_0 u_1 = f_1 (on each slab, by [[prop:ii-e-3-4]] (i)). So it
suffices to prove [[eq:ii-f-8-2]] when supp f ⊂ {t_* ≥ τ_0⁻¹}, which we assume.

For j = 1, 2, 3, 4 let χ_j ∈ C_c^∞([0, j + 1)) equal 1 near [0, j], regarded as functions of R = r/t_* on Ω, with
χ_1 = χ of [[def:ii-f-7-1]].

*Step 1: a solution near 𝓘⁺.* (1 − χ_2) f is supported in {R ≥ 2} and defines a function on [0, ∞)_τ × ι⁺ vanishing
near cf; by [[sec:ii-f-8-1]],

    (1 − χ_2) f ∈ Ḣ^((𝗌;k),(2γ_I+2,γ_++2,∞))_(ebe;b)([0, τ_0] × ι⁺),

with norm ≤ C‖f‖. Apply [[prop:ii-f-7-4]] (1) at the order 𝗌 + 1, for which (𝗌 + 1)′ = 𝗌′ + 1 equals 𝗌 + 1 on {R ≥ 1}
([[lem:ii-f-7-3]] (a)), so that (1 − χ_2) f lies in the space of its right-hand side: the forward solution u_I of
P_+ u_I = (1 − χ_2) f satisfies

    u_I ∈ Ḣ^((𝗌′+1;k),(2γ_I,γ_+,γ_cf))_(ebe;b)([0, τ_0] × ι⁺),      ‖u_I‖ ≤ C ‖f‖.                       {#eq:ii-f-8-4}

On supp(1 − χ_3) ⊂ {R ≥ 3}, P_0 = P_+ and χ_2 = 0, so

    f′ := f − P_0((1 − χ_3) u_I) = f − (1 − χ_3) f + [P_0, χ_3] u_I = χ_3 f + [P_0, χ_3] u_I.

f′ is supported in {R ≤ 4}, away from 𝓘⁺, so it is a function on M̃_0 near ι⁺ ∪ K⁺. [P_0, χ_3] is a first-order
e3b-operator with the weight ρ_+² of P_0 ([[lem:ii-c-1-4]]), supported in {3 ≤ R ≤ 4}, and u_I has order 𝗌 + 1 there;
so, with the identification of e3b- and 3b-spaces away from 𝓘⁺,

    f′ ∈ H^((𝗌;k),(α_++2,0))_(3b;b)(Ω)^(•,−),      supp f′ ⊂ {t_* ≥ τ_0⁻¹, R ≤ 4},      ‖f′‖ ≤ C ‖f‖.    {#eq:ii-f-8-5}

*Step 2: the solution with right-hand side f′.* f, supported in {t^♭ ≥ 1} ⊂ {t_* ≥ 1}, lies in the corresponding space
on Ω with no larger norm, the quotient there being over more extensions; so [[eq:ii-f-8-5]] holds on Ω. By
ℵ-admissibility ([[def:ii-c-2-7]] (3), [[eq:ii-c-2-2]]), for the order 𝗌, which over K⁺ is stationary-P_0-admissible
with weights α_+, −ℵ and margin 0 ([[prop:ii-c-5-1]] (1)), the forward solution u′ of P_0 u′ = f′ on Ω satisfies

    u′ ∈ H^((𝗌;k),(α_+−δ,−ℵ))_(3b;b)(Ω)^(•,−),      ‖u′‖ ≤ C ‖f′‖.                                       {#eq:ii-f-8-6}

u′ is the restriction to {r > r_0} of a distribution ũ′ supported in {t_* ≥ 1}, and P_0 u′ = f′ on {r > r_0} as such
distributions. So on Y := {1/2 < t_* < τ_0⁻¹, r > r_0}, P_0 u′ = 0, and u′ = 0 on {t_* < 1}. t_* is a time function for
g_0 ([[lem:ii-b-1-1]]), and for p ∈ Y, J⁻_Y(p) ∩ {t_* ≥ 3/4} lies in L_p := {3/4 ≤ t_* ≤ t_*(p), B ≤ B(p), r ≥
min(r(p), r^♮)} ([[lem:ii-f-1-4]] (a) for the metric g_0 itself), which is compact and contained in Y;
[[lem:ii-f-1-3]] with the time function t_* and c := 3/4 gives u′ = 0 on Y. Let φ ∈ C^∞(ℝ) equal 0 on
(−∞, τ_0⁻¹ − 1] and 1 on [τ_0⁻¹, ∞), a function of t_*. Then φũ′ extends u′, is supported in {t_* ≥ τ_0⁻¹ − 1} ⊂
{t^♭ ≥ C′(τ_0⁻¹ − 1)} ⊂ {t^♭ ≥ 1}, as τ_0 < C′/(1 + C′), and has norm at most C‖ũ′‖. So u′ lies in
H^((𝗌;k),(α_+−δ,−ℵ))_(3b;b)(Ω_*)^(•,−), with ‖u′‖ ≤ C‖f′‖ there.

*Step 3: u′ near 𝓘⁺.* We show that (1 − χ_4) u′, regarded on M, is e3b-regular near 𝓘⁺. As (1 − χ_4) f′ = 0,

    P_0((1 − χ_4) u′) = −[P_0, χ_4] u′ =: f″,

supported in {4 ≤ R ≤ 5}, away from 𝓘⁺ and from cf; on [0, ∞) × ι⁺, by [[eq:ii-f-8-6]] and [[sec:ii-f-8-1]] with
α_+ − δ for α_+,

    f″ ∈ Ḣ^((𝗌−1;k),(∞,γ_+−δ+2,∞))_(ebe;b)([0, τ_0] × ι⁺).

On supp(1 − χ_4) ⊂ {R ≥ 4}, P_0 = P_+. Let u″ be the forward solution of P_+ u″ = f″ given by [[prop:ii-f-7-4]] (1) at
the order 𝗌 and with γ_+ − δ in place of γ_+ (allowed, δ ≥ 0; 𝗌′ = 𝗌 on supp f″):

    u″ ∈ Ḣ^((𝗌′;k),(2γ_I,γ_+−δ,γ_cf))_(ebe;b)([0, τ_0] × ι⁺),      ‖u″‖ ≤ C ‖f″‖ ≤ C ‖f‖.

ũ := u″ − (1 − χ_4) u′, extended by 0 to {τ > τ_0}, is a distribution on (0, ∞) × (ι⁺)° supported in {τ ≤ τ_0} with
P_+ ũ = f″ − f″ = 0; near cf it equals u″, as (1 − χ_4) u′ vanishes on {R ≤ 4}, so ũ ∈ H^(𝗌′,γ_cf)_(e,loc)((0, ∞) ×
{R < 4}). By [[prop:ii-f-7-4]] (2), ũ = 0. Hence, as 𝗌′ = 𝗌 on {R ≥ 1} and by [[sec:ii-f-8-1]],

    (1 − χ_4) u′ = u″ ∈ H^((𝗌;k),(2α_I,α_+−δ,∞))_(e3b;b)(Ω_*)^(•,−),      ‖(1 − χ_4) u′‖ ≤ C ‖f‖.        {#eq:ii-f-8-7}

*Step 4: conclusion.* On Ω_* ∩ {r > r_0}, P_0((1 − χ_3) u_I + u′) = (f − f′) + f′ = f. Both terms lie in the spaces on
Ω_*: (1 − χ_3) u_I by [[eq:ii-f-8-4]], its support lying in {t_* ≥ τ_0⁻¹} ⊂ {t^♭ ≥ 1}, and u′ by Step 2; their
restrictions to each slab Ω_(1,T′) lie in its slab spaces, the weights at ι⁺ and K⁺ being bounded above and below at
bounded times. By [[prop:ii-e-3-4]] (i) on each slab, their sum is the forward solution of P_0 u = f on Ω_*:

    u = (1 − χ_3) u_I + χ_4 u′ + (1 − χ_4) u′.

By [[eq:ii-f-8-4]], (1 − χ_3) u_I ∈ H^((𝗌+1;k),(2α_I,α_+,∞))_(e3b;b)(Ω_*)^(•,−) ⊂
H^((𝗌;k),(2α_I,α_+−δ,∞))_(e3b;b)(Ω_*)^(•,−) (𝗌′ + 1 = 𝗌 + 1 on {R ≥ 1}); by Step 2, χ_4 u′ ∈
H^((𝗌;k),(∞,α_+−δ,−ℵ))_(e3b;b)(Ω_*)^(•,−), as χ_4 u′ is supported in {R ≤ 5}, away from 𝓘⁺, where 3b- and e3b-spaces
agree; and [[eq:ii-f-8-7]] holds. The three bounds give [[eq:ii-f-8-2]]. ∎

In the last display of the proof of [Hin26c, Theorem 10.1] the term u′ carries the sign −; the sign is +, as above.

**Remark {#rem:ii-f-8-2}** (Relaxed ℵ-admissibility.) If P_0 is ℵ-admissible with margin d_ℵ (the relaxed version
after [[def:ii-c-2-7]]), then [[eq:ii-f-8-2]] holds with 𝗌 − d_ℵ in place of 𝗌 on the left, when 𝗌 is admissible with
weights α_+, −ℵ and margin d_ℵ, and with weights α_+, 0 and margin 1 + d_ℵ. Indeed, ℵ-admissibility enters only
[[eq:ii-f-8-6]], which then gives the order 𝗌 − d_ℵ, and the loss persists through Steps 3–4 ([[prop:ii-f-7-4]] is
applied in Step 3 at the order 𝗌 − d_ℵ, which meets its hypotheses). This is [Hin26c, Remark 10.17] in dimension 4 + 1.

### Forward solutions of admissible wave-type operators: setting and statement {#sec:ii-f1-1}

The rest of the chapter is [Hin26c, Section 11] in dimension 4 + 1. The forward solution of Pu = f is the weak limit
of the forward solutions of operators P_ε that equal P up to a time of order ε⁻¹ and the stationary model P_0 after it.
The a priori estimate for P_ε, uniform in ε, joins the global estimate [[thm:ii-e-6-1]] to the forward solution estimate
[[thm:ii-f-8-1]] for P_0. The error (P_ε − P_0)u is small near ι⁺ ∪ K⁺, where the weights gain, and is controlled at
bounded times by the energy estimates on slabs of [[ch:s07]]. Three points need care. The order function
is taken with margin 3 + δ + ℵ ([[lem:ii-f1-2-3]]); the cut-offs are functions of the time function t^♭ of
[[lem:ii-c-3-2]], whose level sets carry the slabs on which forward solutions are unique ([[sec:ii-f1-2-6]]); and the
tame bound on the error uses a single extension across the artificial boundary {r = r_0} that is bounded at every order
of b-regularity at once, constructed where the order function is a constant integer ([[sec:ii-f1-2-4]],
[[sec:ii-f1-2-5]]).

#### Domains, weights and spaces {#sec:ii-f1-1-1}

P_0 is a stationary wave-type operator on the bundle E ([[def:ii-c-1-1]]), in the setting of [[sec:ii-d-1-1]], with
S̄ = inf_(∂X) min Re spec S ([Hin26c, (5.2)]; [[def:ii-c-3-5]] with p̃_1 = 0). t^♭ := t^♭_* is the time function of
[[lem:ii-c-3-2]], defined on Ω° and, by [[lem:ii-e-1-2]] (iv), on {r ≥ r^♯, t_* ≥ 1/2}, and

    Ω_* := cl_M{t^♭ ≥ 1} ⊂ Ω = cl_M{t_* ≥ 1, r ≥ r_0}

([[lem:ii-c-3-2]] (b): C′t_* ≤ t^♭ ≤ t_*). For T > 1 the *slab* Ω_(1,T) := Ω_* ∩ {t^♭ ≤ T} is that of
[[sec:ii-e-1-1]]. On Ω we use the defining functions of [[sec:ii-a-1]] ([[lem:ii-a-8-8]]),

    x_I² = ρ_I = t_*/(t_* + r),    ρ_+ = (t_* + r)/(t_* r),    ρ_K = r/(t_* + r),    ρ_+ ρ_K = t_*⁻¹,   {#eq:ii-f1-1-1}

of 𝓘⁺, ι⁺ and K⁺. The formulae define smooth positive functions on {r > 0, t_* > 0}, and we use them also on the
extension region {r^♯ ≤ r ≤ r_0}. For an order function 𝗍, k ∈ ℕ₀ and weights, H^((𝗍;k),(2α_I,α_+,α_K))_(e3b;b)(Ω_*;
E)^(•,−) is the space of restrictions to {r > r_0} of elements of H^((𝗍;k),(2α_I,α_+,α_K))_(e3b;b) ([[sec:ii-a-4-2]])
supported in {t^♭ ≥ 1}, with the quotient norm ([[sec:ii-a-7]], [[sec:ii-d-1-1]]). As in [Hin26c, (11.1)], the
*b-spaces* carry powers of ρ_I = x_I² at 𝓘⁺:

    H^(k,(α_I,α_+,α_K))_b := ρ_I^(α_I) ρ_+^(α_+) ρ_K^(α_K) H^k_b = H^((0;k),(2α_I,α_+,α_K))_(e3b;b)     {#eq:ii-f1-1-2}

([[lem:ii-a-8-4]] (d)), with the density |dt dx|, and H^(k,(α_I,α_+,α_K))_b(Ω_*; E)^(•,−) likewise. On Ω, t_*∂_(t_*)
and r∂_x span 𝒱_b ([[sec:ii-c-2-4]]). C^∞_b denotes the functions on a neighbourhood of Ω_* in M that are bounded with
all their b-derivatives. Multiplication by an element of C^∞_b is bounded on every H^((𝗍;k),w)_(e3b;b), with norm bounded
by finitely many of its C^∞_b-seminorms ([[eq:ii-a-8-1]] and the remark after it): the e3b-vector fields are
combinations of b-vector fields with smooth coefficients ([[lem:ii-a-2-9]]), so b-smoothness gives uniform smoothness on
the e3b unit cells, and the b-derivatives of an element of C^∞_b lie in C^∞_b. By acting on extensions it is bounded on
the spaces (Ω_*)^(•,−). Powers ρ^a, a ≥ 0, of the functions [[eq:ii-f1-1-1]] lie in C^∞_b.

#### The statement {#sec:ii-f1-1-2}

**Theorem {#thm:ii-f1-1-1}** (Forward solutions of admissible operators, with tame estimates.) Let P_0 be ℵ-admissible
with sf-weight α_+ and sf-loss δ ([[def:ii-c-2-7]]), let

    α_I < −1/2 + S̄,      α_+ < α_I − 1/2,                                                              {#eq:ii-f1-1-3}

and let ℓ_I ∈ (0, 1/2], ℓ_+ ∈ (δ, 1], ℓ_K > ℵ. There are ε_0 > 0 and d ∈ ℕ such that the following holds for every
k ∈ ℕ₀ and every P admissible relative to P_0 of class ((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)) ([[def:ii-c-3-3]]) with
‖P − P_0‖_((0;d),(2ℓ_I,ℓ_+,ℓ_K)) < ε_0 ([[def:ii-c-3-6]], over Ω_*). For every

    f ∈ H^(k+d,(α_I+1,α_++2,0))_b(Ω_*; E)^(•,−)                                                         {#eq:ii-f1-1-4}

there is exactly one u in ⋃_(s′ ≥ s_u, β_+, β_K ∈ ℝ) H^(s′,(2α_I,β_+,β_K))_e3b(Ω_*; E)^(•,−) with Pu = f, the *forward
solution*; here s_u := inf 𝗌 − 2 for the order 𝗌 of [[lem:ii-f1-2-3]], which depends only on P_0 and the weights. It
lies in H^(k,(α_I,α_+−δ,−ℵ))_b(Ω_*; E)^(•,−), and

    ‖u‖_(H^(k,(α_I,α_+−δ,−ℵ))_b)
        ≤ C_k (‖f‖_(H^(k+d,(α_I+1,α_++2,0))_b)
               + ‖P − P_0‖_((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)) ‖f‖_(H^(d,(α_I+1,α_++2,0))_b)),                     {#eq:ii-f1-1-5}

the norms over Ω_*, with C_k independent of P and f. For k ≥ 1 the map (P, f) ↦ u is continuous from the set of such P,
with the norm ‖P − P_0‖_((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)), times the space [[eq:ii-f1-1-4]], to
H^(k−1,(α_I−ς,α_+−δ−ς,−ℵ−ς))_b(Ω_*; E)^(•,−), for every ς > 0.

In the theorem, as throughout this chapter, "admissible" may be read as conditions (1) and (2) of [[def:ii-c-3-3]]
alone: the proof does not use condition (3) ([[lem:ii-f1-2-1]] and the convention after it). So the theorem applies to
every P with (1) and (2) of that class and the stated smallness. Only the restriction of P to Ω_* enters, over which the
smallness is measured: the proof applies the results of [[ch:s07]], which concern an operator on Ω with its norms over
Ω, to the operator P^♭ of [[lem:s09-off-star]], which equals P on Ω_*, acts as P on the spaces of the theorem, and has
its norms over Ω bounded by those of P over Ω_*. So P may also be given on Ω_* only, with (1), (2) and its norms over
Ω_*; Pu then means P^♭u.

This is [Hin26c, Theorem 11.1] in dimension 4 + 1. [Hin26c] states it with ℓ_+ > δ; the class of [[def:ii-c-3-1]] has
ℓ_+ ≤ 1. The conditions of [Hin26c] are those of [[eq:ii-f1-1-3]], and the dimension enters through the densities
([[cor:ii-f1-1-2]]) and through the indicial gap ([[rem:ii-f1-7-3]]). In the theorem the time function t^♭ is built
with the exponent ℓ = ℓ_I, the weight of the class; [[rem:ii-f1-7-4]] allows any exponent in [ℓ_I, ½], under one
further smallness condition on the metric of P.

**Corollary {#cor:ii-f1-1-2}** (The estimate with unweighted b-densities.) Put μ_b := |dt_* dx|/(t_* ⟨x⟩⁴), a smooth
positive b-density on M̃ near Ω̄ ([[lem:ii-a-8-8]]), and

    b_I := α_I + 2,      b_+ := α_+ + 5/2.                                                              {#eq:ii-f1-1-6}

Then [[eq:ii-f1-1-3]] reads b_I < 3/2 + S̄ and b_+ < b_I, and P_0 is ℵ-admissible with sf-weight b_+ − 5/2. With μ_b,
[[eq:ii-f1-1-5]] reads

    ‖u‖_(H^(k,(b_I,b_+−δ,−ℵ+1/2))_b(Ω_*,μ_b))
        ≤ C_k (‖f‖_(H^(k+d,(b_I+1,b_++2,1/2))_b(Ω_*,μ_b))
               + ‖P − P_0‖_((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)) ‖f‖_(H^(d,(b_I+1,b_++2,1/2))_b(Ω_*,μ_b))).          {#eq:ii-f1-1-7}

In terms of integrals, the square of the left side of [[eq:ii-f1-1-7]] is equivalent to

    ∬_(Ω_*) |ρ_I^(−b_I) ρ_+^(−b_++δ) ρ_K^(ℵ−1/2) (t_*∂_(t_*), r∂_x)^(≤k) u|² dt_* dx/(t_* r⁴),

the power meaning all products of at most k of the fields, with the weights [[eq:ii-f1-1-1]]; the norms of f likewise.
This is [Hin26c, (11.6b)], with r⁴ for r³. Pointwise, for k ≥ 3, on Ω_* ∩ {r > r_0},

    |(t_*∂_(t_*), r∂_x)^(≤k−3) u|
        ≤ C_k (right side of [[eq:ii-f1-1-5]]) ρ_I^(b_I) ρ_+^(b_+−δ) ρ_K^(−ℵ+1/2).                      {#eq:ii-f1-1-8}

This is [Hin26c, (11.4)–(11.7)] in dimension 4 + 1; in dimension 3 + 1 [Hin26c] has b_I = α_I + 3/2, b_+ = α_+ + 2, the
density |dt_* dx|/(t_* r³) and the conditions b_I < 1 + S̄, b_+ < b_I.

#### What is not proved in this chapter {#sec:ii-f1-1-3}

Two further statements of [Hin26c, Theorem 11.1] are not proved here: (a) is not used; (b) is proved later for the
stationary models that are used.

(a) [Hin26c] adds that, if the principal part of P is that of P_0, the theorem holds with Ω = cl_M{t_* ≥ 1} in place
of Ω_*, by local solvability between {t_* = 1} and {t^♭ = 1}. That region meets 𝓘⁺ only at {t_* = 1}, where its two
boundary hypersurfaces meet, and the energy estimates of [[ch:s07]] are not proved on it. The later chapters do not use
the statement, as their operators are quasilinear (their principal parts vary).

(b) [Hin26c] allows P_0 to vary among small stationary perturbations of an ℵ-admissible P_1, and among the stationary
models of nearby parameters, with uniform constants. [[thm:ii-e-6-1]] is uniform in this sense (its last sentence), but
[[thm:ii-f-8-1]] and the ℵ-admissibility estimate [[eq:ii-c-2-2]] are proved, resp. assumed, for one P_0. Here P_0 is
fixed. For the stationary models 2L_b, b near b_0, which the later chapters use, the uniform version of
[[thm:ii-f-8-1]] is [[thm:iii-h2-3-1]] and that of [[thm:ii-f1-1-1]] is [[thm:iii-h2-4-1]].

### Preliminaries {#sec:ii-f1-2}

Throughout, α_I, α_+, ℓ_I, ℓ_+, ℓ_K, ℵ and δ are as in [[thm:ii-f1-1-1]], and

    δ′ := min(ℓ_+ − δ, ℓ_K − ℵ) > 0.                                                                    {#eq:ii-f1-2-1}

For an order function 𝗍 and k ∈ ℕ₀ we write, all over Ω_* with the spaces (Ω_*; E)^(•,−) of [[sec:ii-f1-1-1]],

    X(𝗍;k) := H^((𝗍;k),(2α_I,α_+−δ,−ℵ))_(e3b;b),        Y(𝗍;k) := H^((𝗍;k),(2α_I+2,α_++2,0))_(e3b;b),
    Y′(𝗍;k) := H^((𝗍;k),(2α_I+2,α_+−δ+2,−ℵ))_(e3b;b),   Z(𝗍;k) := H^((𝗍;k),(2α_I,α_+−ℓ_+,−ℓ_K))_(e3b;b).  {#eq:ii-f1-2-2}

As ρ_+, ρ_K are bounded on Ω, ‖·‖_(Y′) ≤ C‖·‖_Y and ‖·‖_Z ≤ C‖·‖_X (the weights of Y and X are the larger at every face,
δ < ℓ_+ and ℵ < ℓ_K). These are Hilbert spaces: each is a quotient of a closed subspace of a Hilbert space, the norm
([[eq:ii-a-8-1]]) being equivalent to the Hilbert norm of property (S3) of [[sec:ii-a-3]].

#### The threshold for perturbations {#sec:ii-f1-2-1}

**Lemma {#lem:ii-f1-2-1}** (The threshold at 𝓘⁺.) Let δ_S := (S̄ − 1/2 − α_I)/4 > 0. Let h_S be a fibre inner product
on E over ∂X such that the smallest eigenvalue of ½(S + S^(*h_S)) is at least S̄ − δ_S/2 on ∂X ([[lem:ii-c-2-5]]),
pulled back to 𝓘⁺ along its fibration over ∂X and extended independently of x_I, as the data of [[def:ii-c-3-3]] (2)
are. There is ε_1 > 0 with the following property. Let P be an operator with (1) and (2) of [[def:ii-c-3-3]], condition
(3) of [[def:ii-c-3-3]] not being assumed; put p_1 := S|_(∂X) + p̃_1 over 𝓘⁺, with p̃_1 of [[eq:ii-c-3-1]] and S|_(∂X)
pulled back as in [[def:ii-c-3-3]]; and let sup_(𝓘⁺∩Ω) |p̃_1|_(h_S) ≤ ε_1 (in particular, this holds if
‖P − P_0‖_((0;0),(2ℓ_I,ℓ_+,ℓ_K)) is small). Then for every α ≤ α_I:

(a) Re_(h_S) p_1 ≥ S̄ − δ_S on cl(𝓘⁺ ∩ Ω), and the same holds for the extension P^ext of [[lem:ii-e-1-2]] on
t_* ∈ [1 − η_0, 1]; hence p̄_1 ≥ S̄ − δ_S and α < −1/2 + p̄_1;

(b) the results of [[ch:s06]] and [[ch:s07]] that assume the threshold α < −1/2 + p̄_1 at the weight α at 𝓘⁺, namely
those resting on [[eq:ii-d-1-3]] and [[eq:ii-d-3-9]] and [[lem:ii-e-2-5]], [[prop:ii-e-2-7]], [[prop:ii-e-3-2]],
[[prop:ii-e-3-4]], [[prop:ii-e-4-3]], [[prop:ii-e-4-4]] and [[thm:ii-e-6-1]], hold for P, with constants depending on P
only through the norms named in them, h_S and δ_S.

*Proof.* (a) S|_(∂X) is independent of t_* and of x_I in the extension, so Re_(h_S) S ≥ S̄ − δ_S/2 on a neighbourhood
of cl(𝓘⁺ ∩ Ω). As p_1 = S|_(∂X) + p̃_1, |Re_(h_S) p̃_1| ≤ |p̃_1|_(h_S), and the Seeley extension of
[[lem:ii-e-1-2]] multiplies sup norms by at most c_Σ := Σ_l |c_l|, ε_1 := δ_S/(2 + 2c_Σ) gives both claims. Every
eigenvalue μ of p_1 has an eigenvector v, and Re μ h_S(v, v) = Re h_S(p_1 v, v) ≥ (S̄ − δ_S) h_S(v, v); so p̄_1 ≥ S̄ −
δ_S, and p̄_1 − 1/2 − α ≥ S̄ − δ_S − 1/2 − α_I = 3δ_S > 0.

(b) These results are stated in [[ch:s06]] and [[ch:s07]] for operators with (1) and (2) of [[def:ii-c-3-3]],
condition (3) not being assumed: this is the standing hypothesis of [[ch:s06]] ([[sec:ii-d-1-1]], and [[sec:ii-d1-1]]
with b-regularity) and of [[ch:s07]] ([[sec:ii-e-1-1]]), and [[sec:ii-e-1-3]] records how p_1 and p_0 enter the energy
estimates. So they hold for P, and it remains to show how their constants depend on the data of P at 𝓘⁺. Their
proofs use p̄_1 only through a fibre inner product h_I with Re_(h_I) p_1 ≥ p̄_1 − δ′_I,
δ′_I := (p̄_1 − 1/2 − α)/4 ([[prop:ii-d-3-6]]; [[eq:ii-e-1-2]], with [[lem:ii-e-1-2]] (iii) for 2δ′_I), and they use
that inequality only through its consequence

    4 Re_(h_I) p_1 − 2 − 4α ≥ 12δ′_I > 0                                                                {#eq:ii-f1-2-3}

at the radial set R = ∂R_(𝓘⁺,out): in [[prop:ii-d-3-6]], where Q_ε ≥ 4(p̄_1 − δ′_I − 1/2 − α_I) = 12δ′_I; in
[[lem:ii-e-2-5]], where the coefficient of τ_0² is −2(2α + 1) + 4(p̄_1 − δ′_I) = 12δ′_I; and in [[prop:ii-e-3-2]], where
4A⁻¹(Re_(h_I) p_1)A − 2 − 4α ≥ 8δ′_I with 2δ′_I. The remaining first-order terms, Im p_1 and p_0, enter those proofs
without any smallness: they are kept as quadratic forms in the edge derivatives, absorbed by the exponential weight in
time, and p_0 by the Poincaré inequality ([[sec:ii-e-1-3]], [[lem:ii-e-2-5]]). The commuted systems of [[ch:s06]] and
of [[sec:ii-e-4]] have the same p_1 ([[eq:ii-e-4-1]] and the paragraph after it), at the weights α − j/2 ≤ α. By (a),
h_S in place of h_I and δ_S in place of δ′_I satisfy [[eq:ii-f1-2-3]] with 12δ_S, for every α ≤ α_I, so the proofs run
verbatim with (h_S, δ_S), and their constants depend on these instead of on (h_I, δ′_I). ∎

In [Hin26c], condition (3) of [[def:ii-c-3-3]], the triangular structure of p_1 and p_0, serves one purpose: a
block-diagonal fibre inner product making Im p_1 and p_0 small ([Hin26c, (8.4)]), a smallness which, as the proof of
(b) shows, is not used here.

Below, "admissible" for P and for the operators P_ε of [[sec:ii-f1-2-6]] means (1) and (2) of [[def:ii-c-3-3]] together
with the smallness of [[lem:ii-f1-2-1]], and every result of [[ch:s06]] or [[ch:s07]] is used in the sense of
[[lem:ii-f1-2-1]] (b). Moreover, from here on P stands for the operator P^♭ of [[lem:s09-off-star]] built from the P of
[[thm:ii-f1-1-1]], whose norms are taken over Ω_*. P^♭ is given on Ω; its norms over Ω are at most C_j times those of P
over Ω_*, with one representation at every j ([[eq:s09-off-star-bound]]), and these factors enter the constants below;
and P^♭u = Pu for u in every space of [[thm:ii-f1-1-1]], whose orders s′ ≥ s_u satisfy s′ ≥ 2 − d, as s_u ≥ −d′ − 2 and
d ≥ d′ + d″ with d″ = s_in ≥ 4 ([[eq:ii-f1-3-3]], [[lem:ii-f1-2-3]]). So P^♭ has the forward solutions of P.

#### The operator off Ω_* {#sec:s09-off-star}

[[thm:ii-f1-1-1]] measures P − P_0 over Ω_*, while [[ch:s07]] works with an operator on Ω, its norms over Ω and its
extension from Ω ([[lem:ii-e-1-2]]). The proof therefore replaces P on Ω ∖ Ω_* = Ω ∩ {t^♭ < 1}, a set of bounded times,
by an extension from Ω_*.

*Coordinates.* At fixed x, t^♭ is strictly increasing in t_* on {t_* ≥ ½, r ≥ r^♯}. Indeed t^♭ = C′(t_* + R̃(r)) on
{r ≤ Ct_*/2}; on {r ≥ r′_0 + 1}, the formula for d(t_*F(ρ_I)) in the proof of [[lem:ii-c-3-2]], with
d(t_*F₁) = A dt_* + B dr and d(t_*F₂) = C′(dt_* + dr), gives ∂_(t_*)t^♭ = F(θA/F₁ + (1 − θ)C′/F₂) > 0, as A > 0 where
θ > 0; and the two sets cover {t_* ≥ ½}, as C ≥ 4(r′_0 + 1) ([[lem:ii-e-1-2]] (iv)). As t^♭ ≥ C′t_*, (t^♭, x) are
coordinates on Ω, in which Ω_* = {t^♭ ≥ 1} and Ω ∖ Ω_* = {τ_1(x) ≤ t^♭ < 1}, τ_1(x) := t^♭|_(t_*=1). Put
Ω_2 := Ω ∩ {t_* ≤ 2/C′}, which contains Ω ∩ {t^♭ ≤ 2}. On Ω_2 the functions ∂_(t_*)t^♭, 1/∂_(t_*)t^♭ and V t^♭, for V a
b-vector field, lie in C^∞_b: near 𝓘⁺, t^♭ = t_*(1 − (t_*/r)^ℓ) with (t_*/r)^ℓ conormal and ∂_(t_*)t^♭ ≥ ½ (as in the
proof of [[lem:ii-f1-2-6]] (a)), and the rest of Ω_2 is compact. As ∂_(t_*) = (∂_(t_*)t^♭)∂_(t^♭), and a vector field
V in x taken at fixed t_* is the same field taken at fixed t^♭ plus (V t^♭)∂_(t^♭), the b-vector fields over Ω_2 are
spanned over C^∞_b by ∂_(t^♭) and the r∂_(x^i), and the e3b-vector fields by ∂_(t^♭) and
fields whose coefficients in (t^♭, x) depend on x only: near 𝓘⁺ the fields r∂_r = −½x_I∂_(x_I) and r^(−1/2)Z_(ij),
which span the x_I∂_ω (with x_I = r^(−1/2) as in [[sec:ii-e-1-1]], and the rotation fields Z_(ij) of
[[sec:ii-f-6-1]]), and the ∂_(x^i) elsewhere; here and below, fields in x are taken at fixed t^♭. On Ω_2, x_I²(1 + r),
ρ_+ and ρ_K are positive functions which, with their inverses, lie in C^∞_b ([[eq:ii-f1-1-1]], t_* lying in
[1, 2/C′]); so each weight x_I^(2a)ρ_+^bρ_K^c is (1 + r)^(−a) times a function of that kind.

*Seeley's operator in t^♭.* Let c_l, ε_l = 3^(−l) be the constants of Seeley's operator in the proof of
[[lem:ii-e-1-3]] (b), so that Σ_l |c_l| ε_l^(−q) < ∞ and Σ_l c_l (−ε_l⁻¹)^q = 1 for q ∈ ℕ_0 ([[sec:ii-f1-2-5]]), and
c_Σ := Σ_l |c_l| as in the proof of [[lem:ii-f1-2-1]]; let χ_♭ ∈ C^∞(ℝ), 0 ≤ χ_♭ ≤ 1, equal 1 on [0, ¼] and 0 on
[½, ∞). For a function q on Ω_* put E_♭q := q on Ω_* and, in the coordinates (t^♭, x),

    (E_♭q)(1 − τ, x) := Σ_(l≥0) c_l χ_♭(τ/ε_l) q(1 + τ/ε_l, x)      on Ω ∖ Ω_*  (τ > 0).                  {#eq:s09-seeley}

E_♭q uses q only on Ω_* ∩ {t^♭ ≤ 3/2} ⊂ Ω_2, at the same x, and it commutes with multiplication by functions of x and
with vector fields in x whose coefficients depend on x only. At (1 − τ, x), ∂^j_(t^♭)E_♭q is
Σ_l c_l (−ε_l⁻¹)^j ∂^j_(τ′)(χ_♭(τ′) q(1 + τ′, x)) taken at τ′ = τ/ε_l; as χ_♭ = 1 near 0, it tends to ∂^j_(t^♭)q(1, x)
as τ ↓ 0, so E_♭q is C^j on Ω when q is C^j up to {t^♭ = 1}, and it is at most Σ_l |c_l| ε_l^(−j) times the supremum
over τ′ ∈ [0, ½] of |∂^j_(τ′)(χ_♭(τ′) q(1 + τ′, x))|. With the description of the b-vector fields and of the weights on
Ω_2, this gives, for every j and every weight w,

    ‖E_♭q‖_(C^((0;j),w)_b(Ω)) ≤ C_j ‖q‖_(C^((0;j),w)_b(Ω_*)),      |(E_♭q)(1 − τ, x)| ≤ c_Σ sup_(1≤t′≤3/2) |q(t′, x)|,
                                                                                                    {#eq:s09-seeley-bound}

with C_j depending only on j, w, t^♭ and χ_♭. For an operator Q = Σ_(|β|≤2) q_β ∂^β on Ω_*, ∂^β the derivatives in
the coordinates (t^♭, x), put E_♭Q := Σ_β (E_♭q_β)∂^β. If Q = Σ_γ q′_γ V^γ, the V^γ being products of at most two
vector fields whose coefficients in (t^♭, x) depend on x only, then E_♭Q = Σ_γ (E_♭q′_γ)V^γ, as E_♭ commutes with
multiplication by functions of x; and the principal symbol of E_♭Q is E_♭ applied to that of Q, at fixed components
of the covector in the coordinates (t^♭, x).

**Lemma {#lem:s09-off-star}** (The operator off Ω_*.) Let k ≥ 2, and let P be an operator on Ω_* with (1) and (2) of
[[def:ii-c-3-3]] there, of class ((0;k),(2ℓ_I,ℓ_+,ℓ_K)), with data p_0, p̃_1 on 𝓘⁺ ∩ Ω_* = 𝓘⁺ ∩ Ω (t^♭ = t_* on 𝓘⁺),
with P̃ as in [[eq:ii-c-3-2]], and with ‖P − P_0‖_((0;0)), over Ω_*, small. Put P^♭ := P on Ω_* and

    P^♭ := P_0 + χ_I ½x_I²ρ_+²(2p̃_1 A + p_0) + E_♭P̃   on Ω ∖ Ω_*,      A := x_I∂_(x_I) − 2ρ_+∂_(ρ_+).     {#eq:s09-off-star}

(a) P^♭ has (1) and (2) of [[def:ii-c-3-3]] on Ω, with the data p_0, p̃_1, and for every j ≤ k

    ‖P^♭ − P_0‖_((0;j),(2ℓ_I,ℓ_+,ℓ_K)) ≤ C_j ‖P − P_0‖_((0;j),(2ℓ_I,ℓ_+,ℓ_K)),                            {#eq:s09-off-star-bound}

the left side over Ω and the right over Ω_*, with C_j depending only on j, t^♭ and the weights. The representation of
P̃^♭ := P^♭ − P_0 − χ_I ½x_I²ρ_+²(2p̃_1A + p_0) built below is linear in that of P̃, so [[eq:s09-off-star-bound]]
holds at every j with one representation.

(b) For a metric g′ write 𝗀′ for the matrix of x_I²ρ_+²g′ in a fixed e3b-frame, and |·| for the operator norm; let 𝗀,
𝗀^♭ and 𝗀_0 be those of the metrics g, g^♭ and g_0 of P, P^♭ and P_0. For every a ∈ [0, ½],

    sup_Ω x_I^(−2a)|(𝗀^♭)⁻¹ − 𝗀_0⁻¹| ≤ c_♭ sup_(Ω_*) x_I^(−2a)|𝗀⁻¹ − 𝗀_0⁻¹|,

with c_♭ ≥ 1 depending only on t^♭ and the frame.

(c) If P is given on Ω°, of class ((0;k)) there, then P^♭v = Pv on Ω° for every distribution v on Ω° supported in
{t^♭ ≥ 1} and lying in H^(s′)_loc, s′ ≥ 2 − k.

*Proof.* Ω ∖ Ω_* lies in Ω_2, as t_* ≤ t^♭/C′ < 1/C′ there.

(a) Let P̃ = Σ_j a_jP_j be the representation of [[def:ii-c-3-6]] ([[def:ii-a-8-3]]), the set of the P_j enlarged, with
coefficients 0, by the products of at most two fields of a fixed e3b-frame. Let the V^γ be the products of at most two
of ∂_(t^♭) and the fields of x above (the empty product being 1). By the description of the e3b-vector fields on Ω_2,
there P_j = Σ_γ n_(jγ)V^γ and V^γ = Σ_j m_(γj)P_j with n_(jγ), m_(γj) ∈ C^∞_b, the derivatives of C^∞_b-functions by
e3b-vector fields lying in C^∞_b. So P̃ = Σ_γ q′_γV^γ on Ω_* ∩ Ω_2, q′_γ := Σ_j a_j n_(jγ), and
E_♭P̃ = Σ_γ (E_♭q′_γ)V^γ. Let ψ ∈ C^∞(ℝ) equal 0 on (−∞, 3/2] and 1 on [2, ∞); ψ(t^♭) ∈ C^∞_b by
[[lem:ii-f1-2-6]] (a). Then

    a^♭_j := ψ(t^♭) a_j + (1 − ψ(t^♭)) Σ_γ m_(γj) E_♭q′_γ

is a representation of P̃^♭ on Ω: on Ω_* it gives ψP̃ + (1 − ψ)Σ_γ q′_γV^γ = P̃, and on Ω ∖ Ω_*, where ψ = 0, it gives
Σ_γ (E_♭q′_γ)V^γ = E_♭P̃. The derivatives of order at most k of E_♭q′_γ are continuous across {t^♭ = 1}, so
[[eq:s09-seeley-bound]], with the weight x_I²ρ_+² times that of the class, and [[lem:ii-a-8-2]] (c)–(d) for the products
with C^∞_b-functions give ‖a^♭_j‖_((0;j′)) ≤ C_(j′) max_i ‖a_i‖_((0;j′)) for j′ ≤ k. With the unchanged data p_0, p̃_1,
this is (2) and [[eq:s09-off-star-bound]]. For (1): the χ_I-term is of first order, so on Ω ∖ Ω_*
σ_2(P^♭) = G_0 + σ_2(E_♭P̃) = G_0 + E_♭(G − G_0). The metric g^♭ of P^♭ is therefore given there by
(g^♭)⁻¹ = g_0⁻¹ + E_♭(g⁻¹ − g_0⁻¹), E_♭ acting on the components in the coordinates (t^♭, x), or in any local frame whose
coefficients depend on x only. By [[eq:s09-seeley-bound]], (g^♭)⁻¹ − g_0⁻¹ lies in
x_I²ρ_+²C^((0;k),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b)(Ω; S² ᵉ³ᵇT) with norm at most C_k times that of g⁻¹ − g_0⁻¹ over Ω_*, and the
Neumann series of the proof of [[lem:ii-c-3-7]] gives g^♭ ∈ 𝒢^((0;k),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b) on Ω, as
‖P − P_0‖_((0;0)) is small.

(b) On Ω ∖ Ω_*, in a local frame whose coefficients depend on x only, the components of (𝗀^♭)⁻¹ − 𝗀_0⁻¹, the matrix of
x_I⁻²ρ_+⁻²((g^♭)⁻¹ − g_0⁻¹), are x_I⁻²ρ_+⁻² times E_♭ of x_I²ρ_+² times those of 𝗀⁻¹ − 𝗀_0⁻¹. The second bound of
[[eq:s09-seeley-bound]], the comparability on Ω_2 of x_I, ρ_+ and the weight x_I^(−2a) at (1 − τ, x) and at the points
(t′, x), t′ ∈ [1, 3/2], at which E_♭ evaluates, and the change to the fixed e3b-frame, by a matrix bounded on Ω_2 with
its inverse, give (b).

(c) In the coordinates (t^♭, x), P^♭ − P = Σ_(|β|≤2) q_β∂^β on Ω°, with q_β of class C^k vanishing on {t^♭ ≥ 1}, hence
with their derivatives of order at most k there. For φ ∈ C_c^∞(Ω°), q_βφ vanishes on {t^♭ ≥ 1}; its translates
(q_βφ)(t^♭ + δ, x), δ > 0 small, have compact support in Ω° ∩ {t^♭ ≤ 1 − δ} and tend to q_βφ in C^k, hence in
H^k ⊂ H^(2−s′), as δ ↓ 0. As ∂^βv ∈ H^(s′−2)_loc is supported in {t^♭ ≥ 1}, it pairs to 0 with each translate, so
⟨(P^♭ − P)v, φ⟩ = Σ_β ⟨∂^βv, q_βφ⟩ = 0. ∎

#### Uniqueness {#sec:ii-f1-2-2}

**Lemma {#lem:ii-f1-2-2}** (Uniqueness on Ω_*.) Let P be P_0, or admissible with ‖P − P_0‖_((d_0;0)) small
([[lem:ii-f1-2-1]], and the smallness of [[prop:ii-e-3-4]], d_0 depending on s′), and let α ≤ α_I and s′, β_+,
β_K ∈ ℝ. If u ∈ H^(s′,(2α,β_+,β_K))_e3b(Ω_*; E)^(•,−) and Pu = 0, then u = 0. The same holds on a slab Ω_(1,T) for u
in its space H^(s′,2α)(Ω_(1,T))^(•,−) ([[sec:ii-e-1-1]]).

*Proof.* The second claim is [[prop:ii-e-3-4]] (i), with [[lem:ii-f1-2-1]] (b). For the first, let T > 2 and φ =
φ(t^♭) ∈ C^∞(ℝ) equal to 1 on (−∞, T + 1] and to 0 on [T + 2, ∞). Then φ(t^♭) = φ̃(1/t^♭) with φ̃(y) := φ(1/y),
φ̃′ ∈ C_c^∞((0, ∞)), so φ(t^♭) ∈ C^∞_b by [[lem:ii-f1-2-6]] (a) (with ε = 1; its proof uses nothing from this
section); the same holds for every function of t^♭ used below. If ũ extends u with support in {t^♭ ≥ 1}, then φũ is
supported in {1 ≤ t^♭ ≤ T + 2}, where t_* ≤ (T + 2)/C′, so ρ_+, ρ_K are bounded below there by [[eq:ii-f1-1-1]], and
φũ ∈ H^(s′,(2α,0,0))_e3b. It extends u|_(Ω_(1,T)), which therefore lies in H^(s′,2α)(Ω_(1,T))^(•,−) and solves Pu = 0
there. So u = 0 on {t^♭ < T, r > r_0}, for every T. ∎

#### The orders {#sec:ii-f1-2-3}

Write T_ℋ := 1/2 + ϑ_ℋ, T_out := (−1 + ϑ_out)/2 and T_in := (−1 + ϑ^(3b)_in)/2 for the thresholds of
[[def:ii-c-2-4]], each in the fibre inner product chosen for its radial set. An order function is admissible for P_0
with weights a_+, a_K and margin η ([[def:ii-c-5-2]]) if it has (2)–(5) of [[prop:ii-c-5-1]], which do not involve the
weights, and, near the three radial sets over K⁺,

    𝗍 > T_ℋ + η,      𝗍 + a_+ − a_K < T_out − η,      𝗍 + a_+ − a_K > T_in + η,                         {#eq:ii-f1-2-4}

by (1)–(6) of [[def:ii-c-2-4]] with α_sf = a_+, α_K = a_K (the order being constant near each radial set).

**Lemma {#lem:ii-f1-2-3}** (The orders.) Let m_0 := 3 + δ + ℵ. There is 𝗌 ∈ C^∞(ᵉ³ᵇS*_ΩM), admissible for P_0 with
weights α_+ − δ, −ℵ and margin m_0, and an integer s_in ≥ 4, such that 𝗌 = s_in over

    Ω_♮ := {t_* ≥ 1/2, r_0 − 2δ_0 < r ≤ r_0 + 4}                                                        {#eq:ii-f1-2-5}

(with the extension of [[sec:ii-e-3-2]] below r = r_0), and 𝗌 ≤ s_in everywhere. Put 𝗌_0 := 𝗌 − 2. Then:

(a) 𝗌_0 < 𝗌 are admissible for P_0 with weights α_+ − δ, −ℵ and margin 0 (the hypothesis of [[thm:ii-e-6-1]] at the
weights α_+ − δ, −ℵ);

(b) 𝗌_0 and 𝗌 are each admissible for P_0 with weights α_+, −ℵ and margin 0, and with weights α_+, 0 and margin 1 (the
hypotheses of [[thm:ii-f-8-1]]);

(c) 𝗌 and 𝗌 + 1 are slab orders ([[sec:ii-e-3-2]]).

*Proof.* [[prop:ii-c-5-1]] with η := m_0 and the weights α_+ − δ, −ℵ is proved by the construction of [[sec:ii-c-5-2]],
𝗌 = s_in − (s_in − s_out)χ with 0 ≤ χ ≤ 1, in which s_in is any constant above a stated bound and the small constants
ε_I, ε_ι may be decreased before the others are chosen. Take s_in ∈ ℕ, s_in ≥ 4, and ε_I² < (2r_0 + 9)⁻¹,
(ε_ι δ_ι)⁻¹ > r_0 + 4, where δ_ι is the constant called δ in [[sec:ii-c-5-2]]. Then 𝗌 ≤ s_in. On Ω_♮ ∩ {r ≥ r_0},
x_I² = t_*/(t_* + r) ≥ (1/2)/(1/2 + r_0 + 4) > ε_I², so ψ_0(x_I) = 0, and r < (ε_ι δ_ι)⁻¹, so χ_ι = 0 there (χ_ι is
supported in {ϱ < ε_ι δ_ι}, ϱ = r⁻¹); hence χ = 0 and 𝗌 = s_in. Below r = r_0, 𝗌 = s_in by its extension
([[sec:ii-c-5-2]], the last lines of its definition of the values; [[sec:ii-e-3-2]]).

(a), (b): (2)–(5) of [[prop:ii-c-5-1]] hold for 𝗌 − j, j ∈ ℤ, as for 𝗌 (a constant shift changes no derivative and no
constancy). For [[eq:ii-f1-2-4]], let 𝗌 satisfy it with (a_+, a_K) = (α_+ − δ, −ℵ) and η = m_0. Then 𝗌 − j satisfies it
with weights (a′_+, a′_K) and the margins

    m_0 − j at ℋ⁺,      m_0 + j − (a′_+ − α_+ + δ) + (a′_K + ℵ) at R_out,
    m_0 − j + (a′_+ − α_+ + δ) − (a′_K + ℵ) at R_in.

For (a′_+, a′_K) = (α_+ − δ, −ℵ) these are m_0 − j, m_0 + j, m_0 − j, all ≥ 0 for j ∈ {0, 2}: this is (a). For
(α_+, −ℵ) they are m_0 − j, m_0 + j − δ = 3 + ℵ + j, m_0 − j + δ, all ≥ 0 for j ∈ {0, 2}. For (α_+, 0) they are m_0 − j
= 3 + δ + ℵ − j, m_0 + j − δ + ℵ = 3 + 2ℵ + j and m_0 − j + δ − ℵ = 3 + 2δ − j, all ≥ 1 for j ∈ {0, 2}: this is (b).

(c) Admissible order functions are slab orders, and 𝗌 + 1 has the same monotonicity and constancy ([[sec:ii-e-3-2]]). ∎

The margin 2 + δ + max(1, ℵ) taken in the proof of [Hin26c, Theorem 11.1] gives for 𝗌_0 the last margin max(1, ℵ) − ℵ
+ 2δ, which is less than 1 when ℵ ≥ 1 and δ < 1/2; the margin m_0 = 3 + δ + ℵ suffices in every case.

Fix 𝗌, s_in and 𝗌_0 as in [[lem:ii-f1-2-3]]. Only 𝗌_0, 𝗌 and 𝗌 + 1 occur below; over Ω_♮ they equal the integers
s_in − 2 ≥ 2, s_in ≥ 4 and s_in + 1; in particular they are constant and positive integers near {r ≤ r_0}, which is the
hypothesis of the tame estimates [[eq:ii-e-6-2]] and [[eq:ii-e-4-4]].

#### Variable orders that agree on a set {#sec:ii-f1-2-4}

**Lemma {#lem:ii-f1-2-4}** (Pseudolocality of the order.) Let 𝗍_1, 𝗍_2 be order functions (property (S8) of
[[sec:ii-a-3]]) and U ⊂ M̃ open with 𝗍_1 = 𝗍_2 over U, and let 𝒞 ⊂ U be closed and φ ∈ C^∞_b with supp φ ⊂ U and φ = 1
near 𝒞. For every j ∈ ℕ₀, ν and weight w there is C with

    ‖v‖_(H^((𝗍_2;j),w)_(e3b;b)) ≤ C (‖v‖_(H^((𝗍_1;j),w)_(e3b;b)) + ‖v‖_(H^((−ν;j),w)_(e3b;b)))

for every v supported in 𝒞.

*Proof.* Weights are removed by conjugation ([[eq:ii-a-8-1]] and the remark after it). Let A_i ∈ Ψ^(𝗍_i)_e3b be
elliptic, so that ‖v‖_((𝗍_i;j)) is equivalent to ‖A_i v‖_((0;j)) + ‖v‖_((−ν;j)) ((S8); for the b-derivatives, (S10)
and [[lem:ii-a-8-4]] (a)). Let B ∈ Ψ^(−𝗍_1)_e3b with BA_1 = I − R, R ∈ Ψ^(−ν′)_e3b, ν′ large (the finite parametrix of
the proof of [[lem:ii-a-7-1]], at variable orders by (S8)). As v = φv,

    A_2 v = (A_2 φ B) A_1 v + A_2 φ R v.

Q := A_2 φ B ∈ Ψ^(𝗍_2−𝗍_1)_e3b has WF′(Q) ⊂ WF′(φ), over supp φ ((S5)). Let φ_1 ∈ C^∞_b with supp φ_1 ⊂ U and φ_1 = 1
near supp φ. Then (1 − φ_1)Q has empty operator wave front set, so it is residual; and φ_1 Q is the left quantization
multiplied by φ_1, whose symbol is φ_1 q with q the symbol of Q, of order 𝗍_2 − 𝗍_1 = 0 on supp φ_1, so φ_1 q ∈
⋂_δ S^0_(1−δ,δ) ((S8)), and φ_1 Q is bounded on H^((0;j)) ((S8), (S10)). Hence ‖A_2 v‖_((0;j)) ≤ C‖A_1 v‖_((0;j)) +
C‖v‖_((−ν;j)), A_2 φ R being of order sup 𝗍_2 − ν′ ≤ −ν. ∎

#### An extension across {r = r_0} at every order of b-regularity {#sec:ii-f1-2-5}

The quotient norm of H^((𝗍;k))(Ω_*)^(•,−) is attained by an extension that depends on k. A tame estimate bounds a low
and a high norm of one function, and so needs one extension that is nearly minimal for both. Away from {r = r_0} a
cut-off provides it ([[lem:ii-e-4-1]] (b)); at {r = r_0}, where Ω_* ends and no room is available, the following lemma
does.

Fix κ ∈ (0, 1/4] with r_0 − 2κ > r^♯ and r_0 + 4κ ≤ r^♮ ([[lem:ii-e-1-2]], [[eq:ii-d-1-2]]). On N_κ := {t_* > 1/2,
r_0 − 2κ < r < r_0 + 4κ}, t^♭ = C′(t_* + R̃(r)) with R̃ = r′_0 or R̃′ ∈ [0, 1] ([[lem:ii-c-3-2]] (c) and its proof;
[[lem:ii-e-1-2]] (iv)), so (t^♭, r, ω) are coordinates on N_κ, and C′t_* ≤ t^♭ ≤ t_* there. In them the e3b-vector
fields over N_κ are spanned by ∂_(t^♭), ∂_r, ∂_ω and the b-vector fields by t^♭∂_(t^♭), ∂_r, ∂_ω, with coefficients in
C^∞_b. Indeed, near K⁺ the e3b-fields are spanned by ∂_(t_*), ∂_x and the b-fields by t_*∂_(t_*), ∂_x
([[sec:ii-e-5-1]]), and ∂_(t_*) = C′∂_(t^♭), ∂_r|_(t_*) = ∂_r|_(t^♭) + C′R̃′∂_(t^♭), t_*∂_(t_*) = (C′t_*/t^♭)
t^♭∂_(t^♭), with C′t_*/t^♭ = t_*/(t_* + R̃) and C′R̃′/t^♭ in C^∞_b (b-derivatives in t^♭∂_(t^♭) of functions of t_*/t^♭
and of (t^♭)⁻¹ are bounded). On N_κ the weights x_I^(2a) ρ_+^b ρ_K^c are (t^♭)^(−c) times smooth positive functions with
bounded b-derivatives, and |dt dx| is a smooth positive multiple of |dt^♭ dr dω|.

Let c_l, ε_l = 3^(−l) be the constants of Seeley's operator in the proof of [[lem:ii-e-1-3]] (b): sin(πs/2) =
Σ_l c_l s^l, so that Σ_l |c_l| ε_l^(−q) < ∞ and Σ_l c_l ε_l^(−q) = sin(π3^q/2) = (−1)^q, that is Σ_l c_l (−ε_l⁻¹)^q = 1,
for all q ∈ ℕ₀. For w on {r > r_0} ∩ N_κ supported in {r < r_0 + 2κ} put ℰ_r w := w on {r > r_0} and

    (ℰ_r w)(t^♭, r, ω) := Σ_l c_l w(t^♭, r_0 + (r_0 − r)/ε_l, ω),      r < r_0,                         {#eq:ii-f1-2-6}

which vanishes for r ≤ r_0 − 2κ.

**Lemma {#lem:ii-f1-2-5}** (A simultaneous extension.) Let 𝗍 be an order function equal to a constant m ∈ ℕ₀ over Ω_♮
(as 𝗌 + j, j ≥ −s_in, is), and w a weight x_I^(2a) ρ_+^b ρ_K^c. There is a linear map ℰ, defined on
⋃_j H^((𝗍;j),w)(Ω_*; E)^(•,−), with ℰu supported in {t^♭ ≥ 1}, ℰu = u on {r > r_0}, and, for every j ∈ ℕ₀,

    ‖ℰu‖_(H^((𝗍;j),w)_(e3b;b)) ≤ C_j ‖u‖_(H^((𝗍;j),w)(Ω_*;E)^(•,−)).                                    {#eq:ii-f1-2-7}

*Proof.* Let ψ = ψ(r) equal 1 for r ≤ r_0 + κ and 0 for r ≥ r_0 + 2κ, and ψ_− = ψ_−(r) equal 1 for r ≥ r_0 and 0 for
r ≤ r_0 − κ. For u with an extension ũ supported in {t^♭ ≥ 1} put

    ℰu := (1 − ψ) ũ + ℰ_r(ψu).

The first term does not depend on ũ: two extensions differ by a distribution supported in {r ≤ r_0}, where 1 − ψ = 0.
The second uses only u on {r > r_0}. So ℰ is well defined and linear, and ℰu = (1 − ψ)u + ψu = u on {r > r_0}.
Supports: (1 − ψ)ũ is supported in {t^♭ ≥ 1}; ψu is supported in {t^♭ ≥ 1} ∩ N_κ (as t^♭ ≥ 1 implies t_* ≥ 1), and
ℰ_r acts at fixed t^♭, so ℰ_r(ψu) is supported in {t^♭ ≥ 1, r_0 − 2κ ≤ r ≤ r_0 + 2κ}.

*The first term.* ‖(1 − ψ)ũ‖_((𝗍;j),w) ≤ C_j ‖ũ‖_((𝗍;j),w) for every extension ũ; the left side being independent of
ũ, it is at most C_j ‖u‖_((𝗍;j),w), at every j at once.

*The second term.* For v supported in the set 𝒞_κ := {t^♭ ≥ 1, r_0 − 2κ ≤ r ≤ r_0 + 2κ}, compact in r,
[[lem:ii-f1-2-4]] (with U the interior of Ω_♮, which contains 𝒞_κ with a neighbourhood φ as required, and 𝗍 against
the constant m, both ways) gives ‖v‖_((𝗍;j),w) ∼ ‖v‖_((m;j),w), the terms ‖v‖_((−ν;j)) being bounded by either side as
m ≥ 0 ≥ −ν. As m ∈ ℕ₀, the norm of (S3) is, on such v, equivalent to the differential norm

    D_(m,j)(v) := Σ_(i+|α|≤j) Σ_(p+|β|≤m) ‖(t^♭)^c (t^♭∂_(t^♭))^i ∂^α_(r,ω) ∂^p_(t^♭) ∂^β_(r,ω) v‖_(L²(|dt^♭ dr dω|)):

the H^m(ℝ⁵)-norm in each scaled chart is the sum of the L²-norms of up to m derivatives, the scaled coordinate fields and
the frame above span the same module over C^∞_b, the derivatives falling on the partition functions χ_α give
lower-order terms with bounded coefficients, and the weight and density are as described above (the mixed norm being
[[eq:ii-a-8-1]]). ℰ_r commutes with ∂_(t^♭), t^♭∂_(t^♭), ∂_ω and with multiplication by functions of t^♭; ∂_r^q ℰ_r w =
Σ_l c_l (−ε_l⁻¹)^q (∂_r^q w)(t^♭, r_0 + (r_0 − r)/ε_l, ω) on {r < r_0}, whose L²-norm there is at most Σ_l |c_l|
ε_l^(1/2−q) ‖∂_r^q w‖_(L²({r>r_0})); and for w smooth up to {r = r_0} the derivatives of ℰ_r w of every order match
across {r = r_0}, since Σ_l c_l (−ε_l⁻¹)^q = 1, so that ℰ_r w has no distributional jump terms there. By density of
such w in the norm D_(m,j) on {r > r_0},

    D_(m,j)(ℰ_r w) ≤ C_(m,j) D⁺_(m,j)(w),

D⁺_(m,j) denoting D_(m,j) with the integrals over {r > r_0}. For any extension ũ, ψ_−ψũ = ψu on {r > r_0} and ψ_−ψũ is
supported in 𝒞_κ, so

    D⁺_(m,j)(ψu) ≤ D_(m,j)(ψ_−ψũ) ≤ C ‖ψ_−ψũ‖_((m;j),w) ≤ C ‖ψ_−ψũ‖_((𝗍;j),w) ≤ C_j ‖ũ‖_((𝗍;j),w).

Taking the infimum over ũ at each j separately, and using ‖ℰ_r(ψu)‖_((𝗍;j),w) ≤ C ‖ℰ_r(ψu)‖_((m;j),w) ≤
C D_(m,j)(ℰ_r(ψu)), gives [[eq:ii-f1-2-7]]. ∎

The tame estimates [[eq:ii-e-4-4]] and [[eq:ii-e-6-2]] of [[ch:s07]] use this construction at the face {r = r_0}, at
every level of b-regularity at once, for right-hand sides whose order is constant and in ℕ₀ near {r ≤ r_0}.

#### The family P_ε {#sec:ii-f1-2-6}

Fix χ_0 ∈ C_c^∞([0, 2)) with 0 ≤ χ_0 ≤ 1 and χ_0 = 1 on [0, 3/2]. For ε ∈ (0, 1] put

    χ_ε := χ_0(1/(ε t^♭)),      χ̃_ε := 1 − χ_ε,      P_ε := χ_ε P_0 + χ̃_ε P = P_0 + χ̃_ε (P − P_0),   {#eq:ii-f1-2-8}

on {r ≥ r^♯, t_* ≥ 1/2} (with P^ext of [[lem:ii-e-1-2]] for P there).

**Lemma {#lem:ii-f1-2-6}** (The family.) (a) χ_ε = 0 on {t^♭ ≤ 1/(2ε)} and χ_ε = 1 on {t^♭ ≥ 2/(3ε)}. So P_ε = P on
{t^♭ < 1/(2ε)} and P_ε = P_0 on {t^♭ > 2/(3ε)}, open sets. Every function φ(1/(ε t^♭)) with φ ∈ C^∞(ℝ), φ′ ∈
C_c^∞((0, ∞)), lies in C^∞_b with seminorms bounded uniformly in ε ∈ (0, 1]; in particular χ_ε, χ̃_ε do.

(b) P_ε satisfies (1) and (2) of [[def:ii-c-3-3]], and for all d_0, j

    ‖P_ε − P_0‖_((d_0;j),(2ℓ_I,ℓ_+,ℓ_K)) ≤ C_j ‖P − P_0‖_((d_0;j),(2ℓ_I,ℓ_+,ℓ_K)),
    sup|p̃^ε_1| ≤ sup|p̃_1|,                                                                            {#eq:ii-f1-2-9}

with C_j independent of ε and P (and depending on d_0). In particular P_ε is admissible in the sense of
[[sec:ii-f1-2-1]] when P is, with the same bounds.

*Proof.* (a) The first claims are 1/(εt^♭) ≥ 2, resp. ≤ 3/2. Let V be a b-vector field and ς := 1/(εt^♭); then Vς =
−ς V log t^♭. On {r ≥ r^♯, t_* ≥ 1/2}, log t^♭ = log t_* + log(t^♭/t_*), log t_* = −log ρ_+ − log ρ_K by
[[eq:ii-f1-1-1]], and t^♭/t_* ∈ [C′, 1] has bounded b-derivatives: near 𝓘⁺ it is 1 − (t_*/r)^(ℓ_I) with (t_*/r)^(ℓ_I) =
(x_I²/(1 − x_I²))^(ℓ_I) conormal, in the transition region a smooth function of t_*/r on a compact range, and near K⁺ it
is C′(1 + R̃(r) ρ_+ρ_K) ([[lem:ii-c-3-2]] and its proof). So V log t^♭ ∈ C^∞_b, and by induction V_1 ⋯ V_q ς is ς times
an element of C^∞_b independent of ε. The b-derivatives of φ(ς) are sums of φ^((i))(ς) ς^i times such elements, i ≥ 1,
and φ^((i))(ς) ς^i is bounded as φ^((i)) has compact support in (0, ∞).

(b) *The metric.* σ_2(P_ε) = χ_ε G_0 + χ̃_ε G, so g_ε⁻¹ := g_0⁻¹ + χ̃_ε (g⁻¹ − g_0⁻¹), with g⁻¹ − g_0⁻¹ ∈ x_I² ρ_+²
C^((d_0;j),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b) of norm ≤ C‖P − P_0‖ (proof of [[lem:ii-c-3-7]]). By (a) and [[lem:ii-a-8-2]]
(c)–(d), χ̃_ε (g⁻¹ − g_0⁻¹) has norm ≤ C_j ‖P − P_0‖_((d_0;j)), and the Neumann series of [[lem:ii-c-3-7]] gives g_ε ∈
𝒢^((d_0;j),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b) with ‖g_ε − g_0‖ ≤ C_j ‖P − P_0‖_((d_0;j)): this is (1).

*The data at 𝓘⁺.* On 𝓘⁺, t^♭ = t_* ([[lem:ii-c-3-2]] (a)), and χ̃_ε|_(𝓘⁺) is bounded in C^∞_b(𝓘⁺ ∩ Ω) uniformly in
ε. Put p^ε_0 := χ̃_ε|_(𝓘⁺) p_0 and p̃^ε_1 := χ̃_ε|_(𝓘⁺) p̃_1, in ρ_+^(ℓ_+) C^(j+d_0)_b(𝓘⁺ ∩ Ω) with norms ≤ C_j times
those of p_0, p̃_1; and |p̃^ε_1| ≤ |p̃_1| as 0 ≤ χ̃_ε ≤ 1. Let π be the projection of the product structure
[0, ε_π)_(x_I) × 𝓘⁺ in which [[def:ii-c-3-3]] (2) extends the data independently of x_I; near 𝓘⁺ ∩ ι⁺ it is compatible
with the corner, the coordinates on 𝓘⁺ including ρ_+, so that ρ_+ ∘ π/ρ_+ is smooth and positive. Then

    P_ε − [P_0 + χ_I ½ x_I² ρ_+² (2p̃^ε_1 A + p^ε_0)] = χ̃_ε P̃ + χ_I ½ x_I² ρ_+² δ_ε (2p̃_1 A + p_0),
    δ_ε := χ̃_ε − χ̃_ε|_(𝓘⁺) ∘ π,                                                                      {#eq:ii-f1-2-10}

with A := x_I∂_(x_I) − 2ρ_+∂_(ρ_+) and P̃ as in [[eq:ii-c-3-2]]. We show δ_ε ∈ x_I^(2ℓ_I) C^∞_b uniformly in ε. Let L :=
−log t^♭ and L_I := L|_(𝓘⁺) ∘ π. With ς_υ := ε⁻¹ e^(L_I + υ(L − L_I)), υ ∈ [0, 1],

    δ_ε = χ_0(ε⁻¹ e^(L_I)) − χ_0(ε⁻¹ e^L) = −(L − L_I) ∫_0^1 χ_0′(ς_υ) ς_υ dυ,

and the integral lies in C^∞_b uniformly in ε, by the argument of (a). Near 𝓘⁺, −L = log t_* + log(1 − (t_*/r)^(ℓ_I));
the second term is (t_*/r)^(ℓ_I) times an element of C^∞_b, so it lies in x_I^(2ℓ_I) C^∞_b. The first is −log ρ_+ −
log(1 − x_I²) near 𝓘⁺ ∩ ι⁺ (by [[eq:ii-f1-1-1]], ρ_K = 1 − x_I²) and a smooth function at finite times; so log t_* −
(log t_*)|_(𝓘⁺) ∘ π is smooth (as log(ρ_+/ρ_+ ∘ π) is) and vanishes at x_I = 0, hence lies in x_I C^∞_b ⊂ x_I^(2ℓ_I)
C^∞_b, as 2ℓ_I ≤ 1. So δ_ε ∈ x_I^(2ℓ_I) C^∞_b uniformly. A is an e3b-vector field near 𝓘⁺: it is a b-vector field
tangent to the fibres of 𝓘⁺, the curves of constant ω ([[def:ii-a-2-8]]). The extended p̃_1, p_0 lie in ρ_+^(ℓ_+)
C^((d_0;j))_(e3b;b) near 𝓘⁺, b-regularity of order j + d_0 giving e3b-regularity of order d_0 and b-regularity of order
j ([[lem:ii-a-2-9]]), and χ_I is supported where ρ_K is bounded below. By [[lem:ii-a-8-2]] (c)–(d), the right side of
[[eq:ii-f1-2-10]] lies in x_I² ρ_+² C^((d_0;j),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b) Diff²_e3b, with a representation of norm ≤ C_j
‖P − P_0‖_((d_0;j)): this is (2) and [[eq:ii-f1-2-9]]. ∎

Condition (3) of [[def:ii-c-3-3]] may fail for P_ε: the diagonal blocks of S|_(∂X) + χ̃_ε p̃_1 need not have real
spectrum when those of S|_(∂X) and S|_(∂X) + p̃_1 do. By [[lem:ii-f1-2-1]] (b) it is not needed.

#### Cut-offs, slabs and the weights at late times {#sec:ii-f1-2-7}

**Lemma {#lem:ii-f1-2-7}** (Cut-offs.) (a) Let T ≥ 2, φ ∈ C^∞_b with φ = 0 on {t^♭ ≥ T − 1}, and 𝗍, α, β_+, β_K
given. For u in the slab space H^((𝗍;k),2α)(Ω_(1,T); E)^(•,−), φu (extended by 0 to {t^♭ ≥ T}) lies in
H^((𝗍;k),(2α,β_+,β_K))_(e3b;b)(Ω_*; E)^(•,−), with norm at most C ‖u‖_(H^((𝗍;k),2α)(Ω_(1,T))^(•,−)), C depending on T, φ
and the orders and weights.

(b) For u ∈ H^((𝗍;k),(2α,β_+,β_K))_(e3b;b)(Ω_*; E)^(•,−), ‖u|_(Ω_(1,T))‖_(H^((𝗍;k),2α)(Ω_(1,T))^(•,−)) ≤ C_T
‖u‖_(H^((𝗍;k),(2α,β_+,β_K))_(e3b;b)(Ω_*)^(•,−)).

(c) For η ∈ (0, 1] let χ_η := χ_0(1/(η t^♭)) as in [[eq:ii-f1-2-8]]. Then ‖χ_η v‖ ≤ C‖v‖ in each of the spaces
[[eq:ii-f1-2-2]], and

    ‖χ_η u‖_(Z(𝗍;k)) ≤ C_k η^(δ′) ‖u‖_(X(𝗍;k)),                                                        {#eq:ii-f1-2-11}

with C, C_k independent of η.

*Proof.* (a) Let ṽ extend u, supported in {t^♭ ≥ 1}, in H^((𝗍;k))_(e3b;b) with the weight x_I^(2α) only
([[sec:ii-e-1-1]]). Then φṽ is supported in {1 ≤ t^♭ ≤ T − 1}, where t_* ≤ (T − 1)/C′, so by [[eq:ii-f1-1-1]]
ρ_+^(−β_+) ρ_K^(−β_K) φ lies in C^∞_b and φṽ lies in the weighted space with norm ≤ C‖ṽ‖. On {r > r_0}, φṽ = φu: the
difference of ṽ and any extension of u to Ω_* vanishes on {t^♭ < T, r > r_0}, and φ vanishes on a neighbourhood of
{t^♭ ≥ T}. Take the infimum over ṽ. (b) Multiply an extension by φ(t^♭) equal to 1 on {t^♭ ≤ T + 1} and 0 on {t^♭ ≥
T + 2}, as in [[lem:ii-f1-2-2]]. (c) The first claim is [[lem:ii-f1-2-6]] (a). For [[eq:ii-f1-2-11]]: with the weights
[[eq:ii-f1-1-1]], ‖v‖_(Z(𝗍;k)) = ‖m_Z v‖_(X(𝗍;k)) for m_Z := ρ_+^(ℓ_+−δ) ρ_K^(ℓ_K−ℵ), as the weights of Z and X differ by
these powers. On supp χ_η, t^♭ ≥ 1/(2η), and by [[eq:ii-f1-1-1]], ρ_+ρ_K = t_*⁻¹,

    m_Z χ_η = η^(δ′) · ρ_+^(ℓ_+−δ−δ′) ρ_K^(ℓ_K−ℵ−δ′) · (η t_*)^(−δ′) χ_η.

The exponents are ≥ 0 by [[eq:ii-f1-2-1]], so the middle factor is in C^∞_b; and (η t_*)^(−δ′) χ_η is in C^∞_b
uniformly in η: η t_* ≥ η t^♭ ≥ 1/2 on its support, V(η t_*)^(−δ′) = −δ′ (η t_*)^(−δ′) V log t_* with V log t_* ∈
C^∞_b, and χ_η is as in [[lem:ii-f1-2-6]] (a). ∎

#### The tame bound for P_ε − P_0 on Ω_* {#sec:ii-f1-2-8}

By [[def:ii-c-3-6]] and [[sec:ii-a-8-2]], P − P_0 = χ_I ½ x_I² ρ_+² (2p̃_1 A + p_0) + P̃ with P̃ = x_I² ρ_+² Σ_q b_q Q_q,
Q_q in a fixed finite subset of Diff²_e3b and b_q ∈ C^((d_0;j),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b). Dropping the factor x_I^(2ℓ_I)
of the b_q (bounded) and dividing by ρ_K^(ℓ_K) on supp χ_I (where ρ_K is bounded below),

    P_ε − P_0 = x_I² ρ_+^(2+ℓ_+) ρ_K^(ℓ_K) Σ_q (χ̃_ε a_q) Q′_q,
    ‖χ̃_ε a_q‖_(C^((d_0;j))_(e3b;b)) ≤ C_j e_j,      e_j := ‖P − P_0‖_((d_0;j),(2ℓ_I,ℓ_+,ℓ_K)),        {#eq:ii-f1-2-12}

with Q′_q in a fixed finite subset of C^∞_b Diff²_e3b (the Q_q, χ_I A and χ_I), C_j independent of ε ([[lem:ii-a-8-2]]
(c), [[lem:ii-f1-2-6]] (a)).

**Lemma {#lem:ii-f1-2-8}** (The tame bound.) Let 𝗍 be an order function equal to an integer m ≥ 2 over Ω_♮. There are
d_0 and d̃, depending only on 𝗍, such that for all k, ε and v ∈ Z(𝗍;k),

    ‖(P_ε − P_0)v‖_(Y(𝗍−2;k)) ≤ C_k (e_(d̃) ‖v‖_(Z(𝗍;k)) + e_k ‖v‖_(Z(𝗍;d̃))),
    ‖(P_ε − P_0)v‖_(Y(𝗍−2;k)) ≤ C_k e_k ‖v‖_(Z(𝗍;k)),                                                  {#eq:ii-f1-2-13}

with e_j of [[eq:ii-f1-2-12]] and C_k independent of ε and P.

*Proof.* Extend each a_q across {r = r_0} by Seeley's operator in r − r_0 (with (t_*, ω) as parameters), which is
bounded on C^((d_0;j))_(e3b;b) for every d_0, j at once ([[lem:ii-e-1-2]] (ii) and the proof of [[lem:ii-e-4-1]] (a)),
and multiply by ψ_Ω ∈ C^∞_b equal to 1 near {t^♭ ≥ 1, r ≥ r_0 − 2κ} and supported in {t_* > 1/2, r > r^♯}; call the
result a^♯_q, and A^♯ := x_I² ρ_+^(2+ℓ_+) ρ_K^(ℓ_K) Σ_q (χ̃_ε a^♯_q) Q′_q, an operator on M̃. With ℰ of
[[lem:ii-f1-2-5]] for the weights of Z, A^♯ℰv is supported in {t^♭ ≥ 1} and equals (P_ε − P_0)v on {r > r_0}, so it is
an extension of it. The weight x_I² ρ_+^(2+ℓ_+) ρ_K^(ℓ_K) takes the weights (2α_I, α_+ − ℓ_+, −ℓ_K) of Z to (2α_I + 2,
α_+ + 2, 0), those of Y. [[cor:ii-a-9-7]], on M̃ with χ′ = χ = 1 and on weighted spaces ([[eq:ii-a-8-1]] and the remark
after it), with d_0, d̃ of [[prop:ii-a-9-6]] for the orders 𝗍 − 2, gives

    ‖A^♯ℰv‖_((𝗍−2;k)) ≤ C_k (max_q ‖χ̃_ε a^♯_q‖_((d_0;d̃)) ‖ℰv‖_((𝗍;k)) + max_q ‖χ̃_ε a^♯_q‖_((d_0;k)) ‖ℰv‖_((𝗍;d̃))),

the norms of ℰv with the weights of Z. By [[eq:ii-f1-2-7]] at j = k and j = d̃ and by [[eq:ii-f1-2-12]], this is the
first bound of [[eq:ii-f1-2-13]]. The second is the same with [[lem:ii-a-8-6]] (a) in place of [[cor:ii-a-9-7]] (no tame
structure being needed, any extension of v may be used). ∎

#### Forward solutions of P_ε {#sec:ii-f1-2-9}

**Lemma {#lem:ii-f1-2-9}** (Forward solutions of the family.) Let k ∈ ℕ₀, ε ∈ (0, 1] and f ∈ Y(𝗌;k), and let P be
admissible, of class ((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) with ‖P − P_0‖_((d_0;d)) below the threshold of [[prop:ii-e-4-4]] for the
slab order 𝗌 + 1 (d_0, d being its constants; by [[eq:ii-f1-2-9]] the same then holds for P_ε). There is u_ε ∈ X(𝗌;k)
with P_ε u_ε = f; by [[lem:ii-f1-2-2]] it is the forward solution.

*Proof.* Let T := 4/ε and χ′ := χ_(ε/4) = χ_0(4/(ε t^♭)), which is 0 on {t^♭ ≤ 2/ε} and 1 on {t^♭ ≥ 8/(3ε)}. By
[[lem:ii-f1-2-7]] (b), f|_(Ω_(1,T+1)) ∈ H^((𝗌;k),2α_I+2)(Ω_(1,T+1))^(•,−). By [[prop:ii-e-4-4]] for P_ε at the slab
order 𝗌 + 1 ([[lem:ii-f1-2-3]] (c), [[lem:ii-f1-2-6]] (b); its smallness condition is on ‖P_ε − P_0‖_((d_0;d)) only),
with the right-hand side f given on the larger slab Ω_(1,T+1), the forward solution u_ini of P_ε u_ini = f on Ω_(1,T)
lies in H^((𝗌+1;k),2α_I)(Ω_(1,T))^(•,−). As 1 − χ′ = 0 on
{t^♭ ≥ T − 1}, [[lem:ii-f1-2-7]] (a) puts (1 − χ′)u_ini in H^((𝗌+1;k),(2α_I,α_+−δ,−ℵ))_(e3b;b)(Ω_*)^(•,−) ⊂ X(𝗌;k). The
commutator [P_0, χ′] = x_I² ρ_+² [L_0, χ′] (L_0 := x_I⁻² ρ_+⁻² P_0 ∈ Diff²_e3b on Ω, [[lem:ii-c-1-4]] (b)) is a
first-order e3b-operator whose coefficients are e3b-derivatives of χ′, in C^∞_b and supported in {2/ε ≤ t^♭ ≤
8/(3ε)}; by [[lem:ii-f1-2-7]] (a) (with φ equal to 1 there and 0 on {t^♭ ≥ T − 1}),

    g := χ′f + [P_0, χ′] u_ini ∈ Y(𝗌;k),      supp g ⊂ {t^♭ ≥ 2/ε}.

By [[thm:ii-f-8-1]] at the order 𝗌 ([[lem:ii-f1-2-3]] (b)), the forward solution v of P_0 v = g on Ω_* lies in X(𝗌;k).
On the slab Ω_(1,2/ε), P_0 v = g = 0, so v = 0 on {t^♭ < 2/ε} by [[lem:ii-f1-2-2]]. As P_ε − P_0 = χ̃_ε(P − P_0) has
coefficients vanishing on the open set {t^♭ > 2/(3ε)}, which contains supp v, P_ε v = P_0 v = g. On {t^♭ < T}, P_ε u_ini
= f, and [P_ε, χ′] = [P_0, χ′] as supp dχ′ ⊂ {t^♭ > 2/(3ε)}; so

    P_ε((1 − χ′)u_ini) = (1 − χ′)f − [P_0, χ′] u_ini,

and u_ε := (1 − χ′)u_ini + v ∈ X(𝗌;k) satisfies P_ε u_ε = f. ∎

### Small b-regularity orders {#sec:ii-f1-3}

This section is Step 1 of the proof of [Hin26c, Theorem 11.1] in dimension 4 + 1.

#### The constants {#sec:ii-f1-3-1}

b-regularity controls e3b-regularity: as Diff^(d_0)_e3b ⊂ C^∞(M̃) Diff^(d_0)_b ([[lem:ii-a-2-9]]) and by
[[lem:ii-a-8-2]] (a), ‖a‖_(C^((d_0;j))_(e3b;b)) ≤ C ‖a‖_(C^((0;j+d_0))_(e3b;b)), with weights; the data p_0, p̃_1 carry
j + d_0 b-derivatives in both classes. Hence, for P of class ((0;j+d_0),·),

    e_j = ‖P − P_0‖_((d_0;j),(2ℓ_I,ℓ_+,ℓ_K)) ≤ C ‖P − P_0‖_((0;j+d_0),(2ℓ_I,ℓ_+,ℓ_K)).                  {#eq:ii-f1-3-1}

Let d^E_0, d^E be the d_0 and d of [[thm:ii-e-6-1]] for (𝗌_0, 𝗌) at the weights α_+ − δ, −ℵ; d^S_0, d^S the largest of
those of [[prop:ii-e-3-4]], [[prop:ii-e-4-3]] and [[prop:ii-e-4-4]] for the slab orders 𝗌 and 𝗌 + 1; d^T_0, d̃ those
of [[lem:ii-f1-2-8]] for 𝗍 = 𝗌; and d^U_0 the d_0 of [[prop:ii-e-3-4]] (i) at s′ = s_u := inf 𝗌 − 2. Put

    D_0 := max(d^E_0, d^S_0, d^T_0, d^U_0),      D_1 := max(d^E, d^S, d̃),
    e_j := ‖P − P_0‖_((D_0;j),(2ℓ_I,ℓ_+,ℓ_K)),                                                          {#eq:ii-f1-3-2}

    d := D_0 + D_1 + d′ + d″,      d′ := max(0, ⌈−inf 𝗌⌉),      d″ := s_in (= max(0, ⌈sup 𝗌⌉)).         {#eq:ii-f1-3-3}

Choose ε_0 > 0 so small that ‖P − P_0‖_((0;d)) < ε_0, for the operator of [[thm:ii-f1-1-1]] over Ω_*, makes e_j,
j ≤ D_1, for P^♭ over Ω ([[eq:s09-off-star-bound]]), and hence (by [[eq:ii-f1-2-9]]) the corresponding norms of every
P_ε, smaller than the thresholds of [[lem:ii-f1-2-1]], of [[lem:ii-c-3-2]] (through
[[lem:ii-c-3-7]]), of [[thm:ii-e-6-1]] at k ≤ D_1 and at d^E, of [[prop:ii-e-3-4]] and [[prop:ii-e-4-3]] at k ≤ D_1 and
[[prop:ii-e-4-4]] at d^S, and of [[prop:ii-e-3-4]] (i) at s′ = s_u ([[lem:ii-f1-2-2]]). Then e_(D_1) ≤ Cε_0 ≤ 1 for
every such P. All constants below depend on P only through ε_0, unless e_k appears explicitly.

#### The uniform a priori estimate {#sec:ii-f1-3-2}

**Proposition {#prop:ii-f1-3-1}** (The uniform estimate.) For every k ≤ D_1 there are η_k ∈ (0, 1] and C_k such that
for every ε ∈ (0, η_k/8] and every u ∈ X(𝗌;k) with P_ε u ∈ Y(𝗌;k),

    ‖u‖_(X(𝗌;k)) ≤ C_k ‖P_ε u‖_(Y(𝗌;k)).                                                                {#eq:ii-f1-3-4}

This is [Hin26c, (11.15)] in dimension 4 + 1.

*Proof.* *(i) The global estimate.* By [[eq:ii-e-6-1]] of [[thm:ii-e-6-1]], for P_ε at the weights α_+ − δ, −ℵ with the
orders 𝗌_0 < 𝗌 ([[lem:ii-f1-2-3]] (a); [[lem:ii-f1-2-1]] and [[lem:ii-f1-2-6]] (b) for the hypotheses on P_ε; [Hin26c,
(11.10)]),

    ‖u‖_(X(𝗌;k)) ≤ C_k (‖P_ε u‖_(Y′(𝗌;k)) + ‖u‖_(X(𝗌_0;k))) ≤ C_k (‖P_ε u‖_(Y(𝗌;k)) + ‖u‖_(X(𝗌_0;k))).  {#eq:ii-f1-3-5}

*(ii) Inversion of P_0.* By [[lem:ii-f1-2-8]], second bound of [[eq:ii-f1-2-13]] with 𝗍 = 𝗌, (P_ε − P_0)u ∈ Y(𝗌_0;k),
as u ∈ X(𝗌;k) ⊂ Z(𝗌;k) and 𝗌 − 2 = 𝗌_0. So P_0 u = P_ε u − (P_ε − P_0)u ∈ Y(𝗌_0;k). Let v be the forward solution of
P_0 v = P_0 u given by [[thm:ii-f-8-1]] at the order 𝗌_0 ([[lem:ii-f1-2-3]] (b)); u − v ∈ X(𝗌_0;k) and P_0(u − v) = 0,
so u = v by [[lem:ii-f1-2-2]], and ([Hin26c, (11.11)])

    ‖u‖_(X(𝗌_0;k)) ≤ C_k ‖P_0 u‖_(Y(𝗌_0;k)) ≤ C_k (‖P_ε u‖_(Y(𝗌;k)) + ‖(P_ε − P_0)u‖_(Y(𝗌_0;k))).       {#eq:ii-f1-3-6}

*(iii) The error near ι⁺ ∪ K⁺.* With χ_η of [[lem:ii-f1-2-7]] (c), by [[eq:ii-f1-2-13]] and [[eq:ii-f1-2-11]] ([Hin26c,
(11.13)–(11.14)]),

    ‖(P_ε − P_0) χ_η u‖_(Y(𝗌_0;k)) ≤ C_k e_k ‖χ_η u‖_(Z(𝗌;k)) ≤ C^((1))_k ε_0 η^(δ′) ‖u‖_(X(𝗌;k)),      {#eq:ii-f1-3-7}

with C^((1))_k independent of η and ε.

*(iv) The error at bounded times.* Let T_η := 2/η. 1 − χ_η vanishes on {t^♭ ≥ 2/(3η)} ⊃ {t^♭ ≥ T_η − 1}. For ε ≤ η/8,
1/(2ε) ≥ 4/η > T_η, so P_ε = P on Ω_(1,T_η) ([[lem:ii-f1-2-6]] (a)), and u|_(Ω_(1,T_η)), which lies in the slab space by
[[lem:ii-f1-2-7]] (b), is the forward solution of Pu = P_ε u there ([[lem:ii-f1-2-2]]). By [[eq:ii-f1-2-13]],
[[lem:ii-f1-2-7]] (a), [[prop:ii-e-4-3]] for P at the slab order 𝗌 ([Hin26c, Proposition 8.6]) and [[lem:ii-f1-2-7]]
(b),

    ‖(P_ε − P_0)(1 − χ_η)u‖_(Y(𝗌_0;k)) ≤ C_k ‖(1 − χ_η)u‖_(Z(𝗌;k)) ≤ C_(k,η) ‖u‖_(H^((𝗌;k),2α_I)(Ω_(1,T_η)))
        ≤ C_(k,η) ‖P_ε u‖_(Y(𝗌;k)).                                                                     {#eq:ii-f1-3-8}

*(v) Absorption.* Inserting [[eq:ii-f1-3-6]]–[[eq:ii-f1-3-8]] in [[eq:ii-f1-3-5]],

    ‖u‖_(X(𝗌;k)) ≤ C^((2))_k ε_0 η^(δ′) ‖u‖_(X(𝗌;k)) + C_(k,η) ‖P_ε u‖_(Y(𝗌;k)),

C^((2))_k independent of η. Fix η_k ∈ (0, 1] with C^((2))_k ε_0 η_k^(δ′) ≤ 1/2. As ‖u‖_(X(𝗌;k)) < ∞, it is absorbed. ∎

#### The forward solution at small orders {#sec:ii-f1-3-3}

**Proposition {#prop:ii-f1-3-2}** (Existence at small orders.) Let k ≤ D_1 and f ∈ Y(𝗌;k). The forward solution u of
Pu = f exists, lies in X(𝗌;k), and ‖u‖_(X(𝗌;k)) ≤ C_k ‖f‖_(Y(𝗌;k)). This is [Hin26c, (11.16)–(11.17)] in dimension
4 + 1.

*Proof.* For ε ∈ (0, η_k/8] let u_ε ∈ X(𝗌;k) be the forward solution of P_ε u_ε = f ([[lem:ii-f1-2-9]]). By
[[eq:ii-f1-3-4]], ‖u_ε‖_(X(𝗌;k)) ≤ C_k ‖f‖_(Y(𝗌;k)). X(𝗌;k) is a Hilbert space ([[sec:ii-f1-2]]), so a sequence
u_(ε_j), ε_j ↓ 0, converges weakly to some u ∈ X(𝗌;k), and ‖u‖ ≤ C_k ‖f‖ (weak lower semicontinuity of the Hilbert
norm, equivalent to the norm used). For φ ∈ C_c^∞(M° ∩ {r > r_0}), w ↦ ⟨w, φ⟩ is continuous on X(𝗌;k) (pair any
extension with φ; the result does not depend on the extension, [[lem:ii-a-7-3]]). supp φ is compact in M°, so t^♭ is
bounded on it, and P_(ε_j)* φ = P* φ for j large ([[lem:ii-f1-2-6]] (a)), P* the formal adjoint, whose coefficients
involve at most two derivatives of those of P (d ≥ 2). Hence

    ⟨u, P*φ⟩ = lim_j ⟨u_(ε_j), P_(ε_j)* φ⟩ = lim_j ⟨P_(ε_j) u_(ε_j), φ⟩ = ⟨f, φ⟩,

so Pu = f on {r > r_0}, both sides supported in {t^♭ ≥ 1}. By [[lem:ii-f1-2-2]], u is the forward solution. ∎

### Large b-regularity orders and the tame estimate {#sec:ii-f1-4}

This section is Step 2 of the proof of [Hin26c, Theorem 11.1] in dimension 4 + 1.

**Proposition {#prop:ii-f1-4-1}** (The tame a priori estimate.) For every k ∈ ℕ₀ there are η_k ∈ (0, 1] and C_k such
that for every ε ∈ (0, min(η_k, η_(D_1))/8], every P as in [[thm:ii-f1-1-1]] and every u ∈ X(𝗌;k) with P_ε u ∈ Y(𝗌;k),

    ‖u‖_(X(𝗌;k)) ≤ C_k (‖P_ε u‖_(Y(𝗌;k)) + e_k ‖P_ε u‖_(Y(𝗌;D_1))),                                     {#eq:ii-f1-4-1}

with e_k of [[eq:ii-f1-3-2]]. This is [Hin26c, (11.19)] in dimension 4 + 1.

*Proof.* For k ≤ D_1 this is [[eq:ii-f1-3-4]]. Let k > D_1, and write A_j := ‖u‖_(X(𝗌;j)), B_j := ‖P_ε u‖_(Y(𝗌;j));
A_k, B_k are finite. By [[prop:ii-f1-3-1]] at D_1 (as ε ≤ η_(D_1)/8), A_j ≤ A_(D_1) ≤ C B_(D_1) for j ≤ D_1.

*(i) The tame global estimate.* By [[eq:ii-e-6-2]] of [[thm:ii-e-6-1]], for P_ε (its d = d^E ≤ D_1, and ‖P_ε −
P_0‖_((d^E_0;d^E)) small), with [[eq:ii-f1-2-9]] and ‖·‖_(Y′) ≤ C‖·‖_Y,

    A_k ≤ C_k (B_k + ‖u‖_(X(𝗌_0;k)) + e_k (B_(D_1) + A_(D_1)))
        ≤ C_k (B_k + ‖u‖_(X(𝗌_0;k)) + e_k B_(D_1)).                                                     {#eq:ii-f1-4-2}

*(ii) Inversion of P_0.* As in [[prop:ii-f1-3-1]] (ii), ‖u‖_(X(𝗌_0;k)) ≤ C_k (B_k + ‖(P_ε − P_0)u‖_(Y(𝗌_0;k))).

*(iii) The error, tamely.* With χ_η of [[lem:ii-f1-2-7]] (c), the first bound of [[eq:ii-f1-2-13]] (with e_(d̃) ≤
e_(D_1) ≤ Cε_0) and [[eq:ii-f1-2-11]],

    ‖(P_ε − P_0) χ_η u‖_(Y(𝗌_0;k)) ≤ C_k (ε_0 η^(δ′) A_k + e_k ‖χ_η u‖_(Z(𝗌;d̃)))
        ≤ C^((1))_k ε_0 η^(δ′) A_k + C_k e_k B_(D_1),

using ‖χ_η u‖_(Z(𝗌;d̃)) ≤ C A_(d̃) ≤ C B_(D_1). With T_η := 2/η as in [[prop:ii-f1-3-1]] (iv), and [[prop:ii-e-4-4]]
for P on Ω_(1,T_η) ([Hin26c, Proposition 8.9]) in place of [[prop:ii-e-4-3]], with the right-hand side Pu = P_ε u given
on the larger slab Ω_(1,T_η+1) (P_ε = P on {t^♭ < 1/(2ε)}, and 1/(2ε) ≥ 2T_η ≥ T_η + 2, as ε ≤ η/8 and η ≤ 1),

    ‖(1 − χ_η)u‖_(Z(𝗌;j)) ≤ C_(j,η) ‖u‖_(H^((𝗌;j),2α_I)(Ω_(1,T_η))) ≤ C_(j,η) (B_j + e_j B_(D_1))

for every j ([[lem:ii-f1-2-7]], and ‖P_ε u‖_(H^((𝗌−1;d^S),2α_I+2)(Ω_(1,T_η+1))) ≤ C B_(D_1)); so, by
[[eq:ii-f1-2-13]],

    ‖(P_ε − P_0)(1 − χ_η)u‖_(Y(𝗌_0;k)) ≤ C_k (ε_0 ‖(1 − χ_η)u‖_(Z(𝗌;k)) + e_k ‖(1 − χ_η)u‖_(Z(𝗌;d̃)))
        ≤ C_(k,η) (B_k + e_k B_(D_1)).

*(iv) Absorption.* Collecting,

    A_k ≤ C^((2))_k ε_0 η^(δ′) A_k + C_(k,η) (B_k + e_k B_(D_1)),

with C^((2))_k independent of η; fix η_k with C^((2))_k ε_0 η_k^(δ′) ≤ 1/2 and absorb. ∎

**Proposition {#prop:ii-f1-4-2}** (Existence with the tame bound.) For every k ∈ ℕ₀, every P as in [[thm:ii-f1-1-1]]
and every f ∈ Y(𝗌;k), the forward solution u of Pu = f lies in X(𝗌;k), and

    ‖u‖_(X(𝗌;k)) ≤ C_k (‖f‖_(Y(𝗌;k)) + e_k ‖f‖_(Y(𝗌;D_1))).                                             {#eq:ii-f1-4-3}

*Proof.* As for [[prop:ii-f1-3-2]], with [[lem:ii-f1-2-9]] at the level k (which needs only the smallness of ‖P_ε −
P_0‖_((d^S_0;d^S))) and [[eq:ii-f1-4-1]] for ε ≤ min(η_k, η_(D_1))/8; the right side of [[eq:ii-f1-4-1]] with P_ε u_ε =
f does not depend on ε. ∎

### Pure b-estimates, and the proofs of the theorem and its corollary {#sec:ii-f1-5}

This section is Step 3 of the proof of [Hin26c, Theorem 11.1] in dimension 4 + 1.

*The embeddings.* By [[lem:ii-a-8-7]], with weights, H^((𝗌;j+d′))_(e3b;b) ⊂ H^j_b, d′ = max(0, ⌈−inf 𝗌⌉). By
[[lem:ii-a-8-4]] (d), applied d″ times, and 𝗌 ≤ s_in = d″, H^(j+d″)_b = H^((0;j+d″))_(e3b;b) ⊂ H^((d″;j))_(e3b;b) ⊂
H^((𝗌;j))_(e3b;b), with weights. Both inclusions preserve supports, so they hold for the spaces (Ω_*)^(•,−) with the
same constants (an extension in the smaller space is one in the larger). With [[eq:ii-f1-1-2]],

    ‖u‖_(H^(k,(α_I,α_+−δ,−ℵ))_b(Ω_*)) ≤ C ‖u‖_(X(𝗌;k+d′)),
    ‖f‖_(Y(𝗌;j)) ≤ C ‖f‖_(H^(j+d″,(α_I+1,α_++2,0))_b(Ω_*)).                                             {#eq:ii-f1-5-1}

*Proof of [[thm:ii-f1-1-1]].* Let ε_0, d be as in [[eq:ii-f1-3-3]] and [[sec:ii-f1-3-1]], k ∈ ℕ₀, and P and f as in
the theorem. By [[eq:ii-f1-5-1]], f ∈ Y(𝗌;k+d′), as k + d′ + d″ ≤ k + d. By [[prop:ii-f1-4-2]] at the level k + d′ (for
which P is of class ((D_0;k+d′),·), as k + d′ + D_0 ≤ k + d), the forward solution u lies in X(𝗌;k+d′) and

    ‖u‖_(H^(k,(α_I,α_+−δ,−ℵ))_b) ≤ C ‖u‖_(X(𝗌;k+d′)) ≤ C_k (‖f‖_(Y(𝗌;k+d′)) + e_(k+d′) ‖f‖_(Y(𝗌;D_1)))
        ≤ C_k (‖f‖_(H^(k+d)_b) + ‖P − P_0‖_((0;k+d)) ‖f‖_(H^d_b)),

the b-norms with the weights of [[eq:ii-f1-1-5]], by [[eq:ii-f1-5-1]] (D_1 + d″ ≤ d), [[eq:ii-f1-3-1]] (k + d′ +
D_0 ≤ k + d) and [[eq:s09-off-star-bound]], the last bounding the norm of P^♭ over Ω by that of P over Ω_*. Uniqueness in the stated class is [[lem:ii-f1-2-2]] at s′ = s_u, whose smallness is among those fixing ε_0
([[sec:ii-f1-3-1]]): an element of the class lies in the space with s′ = s_u, and P, of class ((d^U_0;0),·) by
[[eq:ii-f1-3-1]] as k + d ≥ D_0 ≥ d^U_0, acts on it as [[prop:ii-e-3-4]] (i) at s′ = s_u requires. Below s_u the
smallness of [[prop:ii-e-3-4]] (i), whose d_0 depends on s′, is not implied by that of ‖P − P_0‖_((0;d)), and Pu need
not be defined; this is why the uniqueness class is restricted to s′ ≥ s_u. The continuity is proved in
[[sec:ii-f1-6]]. ∎

*Proof of [[cor:ii-f1-1-2]].* By [[eq:ii-f1-1-1]],

    x_I⁻⁸ ρ_+⁻⁵ ρ_K⁻¹ = ((t_* + r)/t_*)⁴ (t_* r/(t_* + r))⁵ ((t_* + r)/r) = t_* r⁴,

and |dt dx| = |dt_* dx| = t_* ⟨x⟩⁴ μ_b; so |dt dx| = c x_I⁻⁸ ρ_+⁻⁵ ρ_K⁻¹ μ_b near Ω with c = ⟨x⟩⁴/r⁴ smooth and positive
(the identity of the proof of [[lem:ii-a-8-8]]). Hence L²(|dt dx|) = ρ_I² ρ_+^(5/2) ρ_K^(1/2) L²(μ_b) and
H^(k,(a_I,a_+,a_K))_b(|dt dx|) = H^(k,(a_I+2,a_++5/2,a_K+1/2))_b(μ_b) with equivalent norms (b-derivatives of the
weights being the weights times smooth functions). This turns [[eq:ii-f1-1-5]] into [[eq:ii-f1-1-7]]; α_I < −1/2 + S̄ is
b_I < 3/2 + S̄, and α_+ < α_I − 1/2 is b_+ < b_I. Writing out the norms with the frame t_*∂_(t_*), r∂_x of 𝒱_b on Ω, and
⟨x⟩ ∼ r on Ω, gives the integrals. For [[eq:ii-f1-1-8]], let ũ be an extension of u supported in {t^♭ ≥ 1}, of at
most twice the norm of u in the space on the left of [[eq:ii-f1-1-7]]; it reaches {r < r_0}, so [[eq:ii-a-8-2]], stated
for functions supported in Ω, does not apply to it, but the statement of [[lem:ii-a-8-8]] for the unweighted b-density
μ_b has no support condition. With d = k − 3 and the weights (2b_I, b_+ − δ, −ℵ + 1/2) it bounds the C^(k−3)_b-norm of
ũ with the weight x_I^(2b_I) ρ_+^(b_+−δ) ρ_K^(−ℵ+1/2) = ρ_I^(b_I) ρ_+^(b_+−δ) ρ_K^(−ℵ+1/2) by C times the norm of ũ in
H^(k,(b_I,b_+−δ,−ℵ+1/2))_b(M̃, μ_b), which is at most twice the left side of [[eq:ii-f1-1-7]]; restricting to
{r > r_0} gives [[eq:ii-f1-1-8]]. ∎

### Continuous dependence {#sec:ii-f1-6}

This section is Step 4 of the proof of [Hin26c, Theorem 11.1] in dimension 4 + 1.

**Lemma {#lem:ii-f1-6-1}** (Compactness.) Let k ≥ 1, w = (α_I, α_+, α_K), ς > 0 and w′ := (α_I − ς, α_+ − ς, α_K − ς).
The inclusion H^(k,w)_b(Ω_*; E)^(•,−) ↪ H^(k−1,w′)_b(Ω_*; E)^(•,−) is compact.

*Proof.* Extend w to the other boundary hypersurfaces of M̃ by the exponent 0, and let w″ be w lowered by ς at every
boundary hypersurface; near 𝓘⁺ ∪ ι⁺ ∪ K⁺ it is w′. The b-Sobolev spaces are those of the bounded geometry structure of
b-vector fields on M̃°, with the weights ρ^w as weight functions, and ρ^w/ρ^(w″) = ρ_tot^ς → 0 at infinity (ρ_tot a total
boundary defining function); so H^(k,w)_b(M̃) ↪ H^(k−1,w″)_b(M̃) is compact by (S3) of [[sec:ii-a-3]]. Given a bounded
sequence u_j in H^(k,w)_b(Ω_*)^(•,−), take extensions ũ_j supported in {t^♭ ≥ 1} with ‖ũ_j‖ ≤ 2‖u_j‖. A subsequence
converges in H^(k−1,w″)_b(M̃). The closure of {t^♭ ≥ 1} meets ∂M̃ only in 𝓘⁺ ∪ ι⁺ ∪ K⁺ ([[sec:ii-e-1-1]]); multiplying by
a cut-off in C^∞_b equal to 1 near {t^♭ ≥ 1, r ≥ r_0} and supported where w″ = w′, the restrictions converge in
H^(k−1,w′)_b(Ω_*)^(•,−). ∎

*Proof of the continuity in [[thm:ii-f1-1-1]].* Let k ≥ 1, let P^((j)) → P and f^((j)) → f in the stated norms, with
‖P^((j)) − P_0‖_((0;d)) < ε_0 and ‖P − P_0‖_((0;d)) < ε_0, and let u^((j)), u be the forward solutions. Write
X := X(𝗌;k+d′) and H := H^(k,(α_I,α_+−δ,−ℵ))_b(Ω_*; E)^(•,−).

*Bounds.* By the proof of [[thm:ii-f1-1-1]] ([[prop:ii-f1-4-2]] at the level k + d′, with [[eq:ii-f1-5-1]] and
[[eq:ii-f1-3-1]]), u^((j)) ∈ X and

    ‖u^((j))‖_X ≤ C_k (‖f^((j))‖_(H^(k+d)_b) + ‖P^((j)) − P_0‖_((0;k+d)) ‖f^((j))‖_(H^d_b)),

the b-norms with the weights of [[eq:ii-f1-1-5]], with C_k independent of j, as the constants depend on the operator
only through ε_0 ([[sec:ii-f1-3-1]]). The right side is bounded in j, as f^((j)) converges in the space [[eq:ii-f1-1-4]]
and ‖P^((j)) − P_0‖_((0;k+d)) ≤ ‖P^((j)) − P‖_((0;k+d)) + ‖P − P_0‖_((0;k+d)) is bounded. So the u^((j)) are bounded in
the Hilbert space X ([[sec:ii-f1-2]]).

*The limit equation.* Let a subsequence u^((j_m)) converge weakly in X to some ũ ∈ X. The inclusion X ⊂ H of
[[eq:ii-f1-5-1]] is continuous, so u^((j_m)) ⇀ ũ also in H. Let φ ∈ C_c^∞(M° ∩ {r > r_0}). For ψ ∈ L² supported in
supp φ, w ↦ ⟨w, ψ⟩ is continuous on H (pair any extension with ψ; the weights are bounded above and below on supp φ,
which is compact in M°), and the u^((j)) are bounded in L² on supp φ. P^((j))* φ → P* φ in L², as the coefficients
converge in C² on supp φ (k + d ≥ 2). So

    ⟨ũ, P*φ⟩ = lim_m ⟨u^((j_m)), P^((j_m))* φ⟩ = lim_m ⟨f^((j_m)), φ⟩ = ⟨f, φ⟩,

and Pũ = f on {r > r_0}.

*Identification.* As 𝗌 ≥ inf 𝗌 > s_u = inf 𝗌 − 2,

    ũ ∈ X ⊂ H^(𝗌,(2α_I,α_+−δ,−ℵ))_e3b(Ω_*; E)^(•,−) ⊂ H^(s_u,(2α_I,α_+−δ,−ℵ))_e3b(Ω_*; E)^(•,−),

so ũ lies in the class in which [[thm:ii-f1-1-1]] asserts uniqueness, and so does u. Both solve Pv = f, so ũ = u by that
uniqueness, which is [[lem:ii-f1-2-2]] at s′ = s_u for P, whose smallness holds as ‖P − P_0‖_((0;d)) < ε_0 (the proof
of [[thm:ii-f1-1-1]]).

*Convergence.* Every subsequence of (u^((j))) is bounded in X, so it has a further subsequence converging weakly in X,
and by what was just shown its limit is u. Hence u^((j)) ⇀ u in X, and so in H. By [[lem:ii-f1-6-1]], the inclusion of
H in H^(k−1,(α_I−ς,α_+−δ−ς,−ℵ−ς))_b(Ω_*; E)^(•,−) is compact, so u^((j)) → u in norm there (each subsequence has a
norm-convergent subsequence, whose limit is the weak limit u). ∎

### Four remarks {#sec:ii-f1-7}

**Remark {#rem:ii-f1-7-1}** (Relaxed ℵ-admissibility.) Let P_0 be ℵ-admissible with margin d_ℵ ≥ 0 (the relaxed version
after [[def:ii-c-2-7]]), and put d̄_ℵ := ⌈d_ℵ⌉ ∈ ℕ₀. Then [[thm:ii-f1-1-1]] holds with d increased by d̄_ℵ, that is,
with d := D_0 + D_1 + d′ + d″ + d̄_ℵ in [[eq:ii-f1-3-3]], the constants of [[sec:ii-f1-3-1]] being taken for the orders
below, and those of the slab propositions (d^S_0, d^S) for the slab orders 𝗌 and 𝗌 + d̄_ℵ + 1.

Indeed, P_0 is then ℵ-admissible with margin d̄_ℵ: an order admissible with margin d̄_ℵ is admissible with margin d_ℵ,
so (1)–(2) of [[def:ii-c-2-7]] hold for it, and (3) bounds u at the order 𝗌 − d_ℵ, hence at the order 𝗌 − d̄_ℵ ≤ 𝗌 − d_ℵ.
The orders are shifted by the integer d̄_ℵ, and not by d_ℵ, because the tame estimates [[eq:ii-e-6-2]] and
[[eq:ii-e-4-4]] and the extension of [[lem:ii-f1-2-5]] need orders that are constant integers near {r ≤ r_0}. Take 𝗌 as
in [[lem:ii-f1-2-3]] with the margin m_0 + 2d̄_ℵ and with s_in ≥ 4 + d̄_ℵ (its proof allows every integer s_in above a
bound), and 𝗌_0 := 𝗌 − 2 − d̄_ℵ. Over Ω_♮ the orders 𝗌_0, 𝗌 − 2, 𝗌, 𝗌 + d̄_ℵ and 𝗌 + d̄_ℵ + 1 used below equal the
integers s_in − 2 − d̄_ℵ ≥ 2, s_in − 2, s_in, s_in + d̄_ℵ and s_in + d̄_ℵ + 1. The margins of [[sec:ii-f1-2-3]] (with
m_0 + 2d̄_ℵ for m_0) show: 𝗌_0 < 𝗌 meet the hypotheses of [[thm:ii-e-6-1]]; 𝗌 − 2 = 𝗌_0 + d̄_ℵ is admissible with
weights α_+, −ℵ and margin d̄_ℵ and with weights α_+, 0 and margin 1 + d̄_ℵ, so [[rem:ii-f-8-2]] with margin d̄_ℵ gives
‖u‖_(X(𝗌_0;k)) ≤ C ‖P_0 u‖_(Y(𝗌−2;k)), which replaces [[eq:ii-f1-3-6]], the error (P_ε − P_0)u lying in Y(𝗌 − 2;k) by
[[eq:ii-f1-2-13]]; and 𝗌 + d̄_ℵ is admissible with the same two pairs of weights and margins d̄_ℵ, 1 + d̄_ℵ (its upper
margin at R_out with weights α_+, 0 being m_0 + 2d̄_ℵ − d̄_ℵ − δ + ℵ ≥ 1 + d̄_ℵ), so [[lem:ii-f1-2-9]] holds for
f ∈ Y(𝗌 + d̄_ℵ;k), with u_ini of order 𝗌 + d̄_ℵ + 1 and v ∈ X(𝗌;k) by [[rem:ii-f-8-2]]. The absorption in
[[prop:ii-f1-3-1]] is unchanged, as 𝗌_0 + d̄_ℵ + 2 = 𝗌. In [[sec:ii-f1-5]], f ∈ Y(𝗌 + d̄_ℵ;k+d′) needs
k + d′ + d″ + d̄_ℵ ≤ k + d, as 𝗌 + d̄_ℵ ≤ d″ + d̄_ℵ.

This is [Hin26c, Remark 11.2] in dimension 4 + 1. [Hin26c] raises the margin by d_ℵ only; the second shift is needed in
the existence step ([[lem:ii-f1-2-9]], [Hin26c, (11.16)]), where [[thm:ii-f-8-1]] loses d_ℵ.

**Remark {#rem:ii-f1-7-2}** (No loss of b-regularity.) The absorption in [[prop:ii-f1-3-1]] and [[prop:ii-f1-4-1]] uses
that [[thm:ii-e-6-1]] is lossless in the b-regularity: both u and P_ε u carry k b-derivatives. If it needed k + 1 on
P_ε u, the error (P_ε − P_0)χ_η u would be needed in Y(𝗌_0;k+1), which [[eq:ii-f1-2-13]] bounds by u in Z(𝗌;k+1), and
[[eq:ii-f1-3-7]] could not be absorbed. Once [[eq:ii-f1-1-5]] holds, b-regularity alone describes the solution, which is
how the later chapters use it. This is [Hin26c, Remark 11.3].

**Remark {#rem:ii-f1-7-3}** (The indicial gap.) [[eq:ii-f1-1-3]] gives α_+ < α_I − 1/2 < −1 + S̄, and tf-admissibility
puts α_+ + 2 in the indicial gap (β_−, β_+) of P̂_0(0) ([[def:ii-c-2-7]] (2); in dimension 3 + 1 [Hin26c] has α_+ +
3/2). So [[thm:ii-f1-1-1]] requires β_− < α_+ + 2 < 1 + S̄, in particular β_− < 1 + S̄ (the β_− < 1/2 + S̄ of [Hin26c,
Remark 11.4] in dimension 3 + 1). For the scalar wave operator, S = 0 and the gap is (0, 2) ([[sec:ii-c-2-4]]), so α_+ ∈
(−2, −1) and α_I ∈ (α_+ + 1/2, −1/2): α_I = −1/2 − ε_I, α_+ = −1 − ε_+ with 0 < ε_I < ε_+ < 1. In dimension 3 + 1
[Hin26c, (12.7)] prints 0 < ε_+ < ε_I < 1/2, which contradicts α_+ < α_I − 1/2; with α_I = −1/2 − ε_I and α_+ = −1 −
ε_+ the condition is ε_+ > ε_I. This is [Hin26c, Remark 11.4] in dimension 4 + 1.

**Remark {#rem:ii-f1-7-4}** (The exponent of the time function.) Let ℓ_♭ ∈ [ℓ_I, ½], let t^♭ be the function of
[[lem:ii-c-3-2]] built for g_0 with ℓ = ℓ_♭ in place of ℓ_I, and ϵ_G its threshold; let Ω_*, its slabs, the spaces of
[[sec:ii-f1-1-1]] and the cut-offs of this chapter be built from this t^♭. There are C_♭ ≥ 1, depending only on upper
bounds for x_I²ρ_+²g_0 and its inverse, and ε_♭ > 0, depending only on g_0 and ℓ_♭, such that [[thm:ii-f1-1-1]], also
in the form of [[rem:ii-f1-7-1]], and [[cor:ii-f1-1-2]] hold, with ε_0, d and C_k depending also on ℓ_♭, for every P
as there whose metric g satisfies in addition

    ‖g − g_0‖_(𝒢̃^(0,(2ℓ_♭,0,0))_(e3b)) < ε_♭,                                                        {#eq:ii-f1-7-1}

the norm being taken over Ω_* as in [[thm:ii-f1-1-1]]; the continuity statement holds on the set of such P. For
ℓ_♭ = ℓ_I, [[eq:ii-f1-7-1]] follows from ‖P − P_0‖_((0;d)) < ε_0 for ε_0 small ([[lem:ii-c-3-7]]), and the remark is
the theorem. Moreover, the proof applies [[lem:ii-c-3-2]] (1)–(2) only to g_0, to g, to metrics g′ with
‖g′ − g_0‖ ≤ C_♭‖g − g_0‖, and to metrics g′ that the proof of [[thm:ii-f-8-1]] takes within any prescribed distance
of g_0, all distances in the norm of [[eq:ii-f1-7-1]]; its other uses of t^♭ concern the function alone.

*Proof.* In [[ch:s05]]–[[ch:s09]] and in [[rem:ii-g-3-2]] the time function enters in two ways only, and ℓ_I is
otherwise the weight of the class.

(A) Through the hypothesis of [[lem:ii-c-3-2]]: for a metric g′ within ϵ_G of g_0 in the norm of [[eq:ii-f1-7-1]],
dr is future timelike on {r_0 ≤ r ≤ r^♮} and dt^♭ is past timelike. The settings of [[sec:ii-c-4]], of [[ch:s06]]
and of [[sec:ii-e-1-1]] ask this of the metric of an operator, and [[lem:ii-e-1-2]] (iv) carries it over to P^ext;
those settings obtain it from the smallness of ε_P through [[lem:ii-c-3-7]], which gives it at the exponent ℓ_I only.

(B) Through the form of t^♭ given by [[lem:ii-c-3-2]] (a)–(c) and its proof, and through the constant C′ of (b).

*The metrics of (A).* For a metric g′ write G := x_I²ρ_+²g′ in a fixed e3b-frame, and |·| for pointwise norms. G_0
and G_0⁻¹ are bounded on Ω ([[rem:s05-metric-class]] (b)), and the norm of g′ − g_0 in [[eq:ii-f1-7-1]] is
equivalent to sup x_I^(−2ℓ_♭)|G − G_0|. From

    (G_0 + H)⁻¹ − G_0⁻¹ = −(G_0 + H)⁻¹ H G_0⁻¹,

|(G_0 + H)⁻¹ − G_0⁻¹| ≤ 2|G_0⁻¹|²|H| where |G_0⁻¹||H| ≤ ½, and likewise with G_0⁻¹ in place of G_0. So, while they are
small, sup x_I^(−2ℓ_♭)|G − G_0| and sup x_I^(−2ℓ_♭)|G⁻¹ − G_0⁻¹| bound each other up to factors depending only on upper
bounds for G_0 and G_0⁻¹. The metrics to which the proof of [[thm:ii-f1-1-1]] applies (A), itself or through the
results of [[ch:s05]]–[[ch:s08]] that it cites, are the following.

(i) g_0, and the metric g of P, by [[eq:ii-f1-7-1]].

(ii) The metric g_ε of P_ε ([[eq:ii-f1-2-8]]): g_ε⁻¹ = (1 − χ̃_ε)g_0⁻¹ + χ̃_ε g⁻¹ with 0 ≤ χ̃_ε ≤ 1 (the proof of
[[lem:ii-f1-2-6]] (b)), so |G_ε⁻¹ − G_0⁻¹| ≤ |G⁻¹ − G_0⁻¹| pointwise, for every ε.

(iii) The metrics of P^ext ([[lem:ii-e-1-2]]) and of P_ε^ext = χ_ε P_0 + χ̃_ε P^ext ([[sec:ii-f1-2-6]]). Near 𝓘⁺ on
{t_* ≥ ½}, (ii) of [[lem:ii-e-1-2]], whose proof preserves every weight in the parameters, taken with d_0 = k = 0 and
the weight 2ℓ_♭ at 𝓘⁺, bounds the second-order coefficients of P^ext − P_0, and so G_ext⁻¹ − G_0⁻¹, by a constant
times the bound for G⁻¹ − G_0⁻¹; for P_ε^ext the convex combination of (ii) gives the same. In the proof of
[[lem:ii-e-1-2]] (iv), the bound C(ε_P + ρ_I^(1−ℓ_I))ρ_I^(ℓ_I) of the coefficients of g⁻¹ − ḡ⁻¹ near 𝓘⁺ is then used
with ℓ_♭ in place of ℓ_I and C‖g − g_0‖ in place of ε_P; elsewhere that proof uses (A) for g on Ω_*, and the closeness
of the extended metric to g_0 in supremum at bounded times near {r = r_0}, which involves no weight at 𝓘⁺.

(iv) In the proof of [[thm:ii-f-8-1]], (A) is used for g_0 and for metrics that differ from g_0 by an amount small in
𝒢̃^(0,(1,0,0))_(e3b) once the parameters of that proof are chosen (Λ and t_(*,0) large, τ_1 and ε small): the metrics
of P_Λ ([[sec:ii-f-6-3]], whose class has the weight 1 at 𝓘⁺), of P_aux ([[sec:ii-f-7-5]]), and the modified metrics
of [[sec:ii-f-7-2]] and [[sec:ii-f-7-6]]. There ḡ − g_0 has the relative decay ρ_0²x_I²ρ_+² ([[eq:ii-b-1-2]]), and the
other differences are supported where x_I is bounded below. The metrics G_θ of [[lem:ii-f-1-4]] enter (A) only where
they equal G_0. As x_I ≤ 1 and 2ℓ_♭ ≤ 1, x_I ≤ x_I^(2ℓ_♭), so smallness in 𝒢̃^(0,(1,0,0))_(e3b) gives smallness in
the norm of [[eq:ii-f1-7-1]]: these metrics lie within any prescribed distance of g_0 in that norm.

Let C_♭ ≥ 1 bound the factors of (ii) and (iii), so that the metrics there lie within C_♭‖g − g_0‖ of g_0, and let
ε_♭ be so small that C_♭ε_♭ < ϵ_G and that the identity above applies to every metric of (i)–(iii). Then (A) holds for
the metrics of (i)–(iii) by [[eq:ii-f1-7-1]], and for those of (iv) when the prescribed distance is ϵ_G.

*(B).* (a) gives t^♭ = t_* on 𝓘⁺ for every ℓ, which is all that [[sec:ii-c-4]], [[ch:s06]], [[sec:ii-e-1-1]] and
[[lem:ii-f1-2-6]] use of t^♭ at 𝓘⁺. In (b), C′ = (1 − C^(−ℓ))/(1 + C) depends on ℓ; every constant chosen from it
(T_♭ = 2/C′ in [[sec:ii-c1-3-2]], the bounds t_* ≤ T/C′ on slabs, T ≥ 8/C′ in [[sec:ii-f-6-3]], τ_0 < C′τ_1/2 in
[[sec:ii-f-7-3]]) is chosen with the C′ of ℓ_♭, and no condition relates C′ to ℓ_I. (c) and the gluing on
{r ≤ r′_0 + 1} involve ℓ only through C′. Near 𝓘⁺, t^♭ = t_*(1 − (t_*/r)^(ℓ_♭)), and
(t_*/r)^(ℓ_♭) = (x_I²/(1 − x_I²))^(ℓ_♭) is conormal: its b-derivatives, and at bounded t_* its edge derivatives, are
bounded, and it tends to 0 at 𝓘⁺. Only these properties are used: in the collar of [[sec:ii-e-1-5]]
(∂_(t_*)t^♭ = 1 − (1 + ℓ_♭)(t_*/r)^(ℓ_♭) ≥ ½ for r large, and t^♭ − t_* = −t_*^(1+ℓ_♭)x_I^(2ℓ_♭), with x_I = r^(−1/2)
there, has bounded edge derivatives), in the proof
of [[lem:ii-e-3-3]] (t^♭ ≤ t_*, and t_*^(1+ℓ_♭)x_I^(2ℓ_♭) < ω_0/4 near a compact part of 𝓘⁺), in [[lem:s07-extension]],
in [[lem:ii-f1-2-6]] (a) and through it in [[lem:ii-f1-2-2]] and [[lem:ii-f1-2-7]], and in (T2)–(T3) of
[[rem:ii-g-3-2]], with ε = ℓ_♭ there. The one comparison of ℓ_♭ with ℓ_I is in [[lem:ii-f1-2-6]] (b), which shows
δ_ε ∈ x_I^(2ℓ_I)C^∞_b: near 𝓘⁺ the term log(1 − (t_*/r)^(ℓ_♭)) of −L is (t_*/r)^(ℓ_♭) times an element of C^∞_b, so it
lies in x_I^(2ℓ_♭)C^∞_b ⊂ x_I^(2ℓ_I)C^∞_b, as x_I^(2(ℓ_♭−ℓ_I)) ∈ C^∞_b for ℓ_♭ ≥ ℓ_I; and the term
log t_* − (log t_*)|_(𝓘⁺) ∘ π lies in x_I C^∞_b ⊂ x_I^(2ℓ_I)C^∞_b, as there. This is where ℓ_♭ ≥ ℓ_I is needed.

*Constants.* With (A) and (B), the proof of [[thm:ii-f1-1-1]] runs as written: the threshold of [[lem:ii-c-3-2]] in
[[sec:ii-f1-3-1]] is met by [[eq:ii-f1-7-1]] and (i)–(iii) instead of through [[lem:ii-c-3-7]], and [[lem:ii-f1-2-2]]
is applied to P_0, P and P_ε, which satisfy (A). The constants depend on t^♭, so on ℓ_♭, and on P only through ε_0 and
ε_♭. [[rem:ii-f1-7-1]] changes only the orders, and [[cor:ii-f1-1-2]] only the densities, so they hold in the same
way. ∎
