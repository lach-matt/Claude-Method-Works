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
[[eq:ii-f-4-1]]. Order functions are written in sans-serif type (𝗌, 𝗍, 𝖻). The radii 0 < r_0 − 2δ_0 < r_0 < r_2 of the
artificial boundary are parameters of the setting. The constants chosen from r_0 below (T_+ in [[def:ii-f-7-1]], the set
Ω_♮ and the constants of [[lem:ii-f1-2-3]], the width κ of [[sec:ii-f1-2-5]]) are chosen by inequalities that a smaller
r_0 makes no harder, so every result holds for each choice of the radii at which the hypotheses of [[ch:s05]] hold.

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

    χ(R) R∂_R,   χ(R) Z_a,   χ(R) Rτ∂_τ,      χ(v) v∂_v,   χ(v) √v Z_a,   χ(v) τ∂_τ,      v = R⁻¹,      {#eq:ii-f-6-1}

where Z_a, a = 1, …, 6, are the rotation fields Z_(ij) = x_i ∂_(x_j) − x_j ∂_(x_i), 1 ≤ i < j ≤ 4, of 𝕊³ ⊂ ℝ⁴, in
place of the coordinate fields ∂_ω of [Hin26c, (10.42)]. They span T𝕊³ at every point: for x ∈ 𝕊³ and w ∈ T_x𝕊³,

    Σ_(i<j) (x_i w_j − x_j w_i) Z_(ij)(x) = ½ Σ_(i,j) (x_i w_j − x_j w_i)(x_i e_j − x_j e_i) = |x|² w − (x·w) x = w,

since the summand is symmetric under the exchange of i and j and vanishes for i = j. By [[eq:ii-f-1-5]] and
N_ι⁺(P_0) = τ² N⁰ ([[def:ii-f-1-1]]), with R⁻¹ τ∂_τ = R⁻² (Rτ∂_τ) and R⁻¹ R∂_R near cf, and by [[eq:ii-f-1-6]] near 𝓘⁺,

    N_ι⁺(P_0) ∈ x_I² ρ_+² ρ_cf⁻² Diff²_ebe([0, ∞] × ι⁺),                                                  {#eq:ii-f-6-2}

which is [Hin26c, (10.43)]. The spaces of [Hin26c, (10.45)–(10.48)] are, in dimension 4 + 1,

    H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)
        := x_I^(2γ_I) τ^(γ_+) ρ_cf^(γ_cf) H^((𝗌;k))_(ebe;b)((0, ∞)_τ × ι⁺; |dτ/τ| μ_b),                    {#eq:ii-f-6-3}

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
                                         + Σ_± ∫_(±[1,∞)) ‖(ℳu)(ζ − iγ_+)‖²_(𝐨_±;k,+) dζ,              {#eq:ii-f-6-4}

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
    ‖u‖_(H^((𝗌;k),(2γ_I,γ_+,γ_cf))_(ebe;b)) ≤ C ‖f‖_(H^((𝗌−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)),           {#eq:ii-f-6-5}

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

The existence of solutions below uses one standard result on hyperbolic equations, which the appendix of results from the
literature states with its page.

*The Cauchy problem* ([Hö85, Section 23.2]). Let Q be a second-order operator with smooth coefficients on a vector
bundle over a manifold X, with principal symbol G Id, G the dual metric function of a Lorentzian metric on X, and let t
be a time function whose level sets are Cauchy hypersurfaces. For f ∈ H^(s−1)_loc(X) with supp f ⊂ {t ≥ t_0} there is
u ∈ H^(s)_loc(X) with Qu = f and supp u ⊂ {t ≥ t_0}.

**Lemma {#lem:ii-f-6-3}** (Control at 𝓘⁺ of the extension.) Let s′ ∈ ℝ, T ∈ ℝ, and g ∈ H^(s′−1)_c with support in
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

    (ℳu)(σ) := N⁰(σ)⁻¹ ℳ(τ⁻² f)(σ),                                                                     {#eq:ii-f-6-6}

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
[τ_1, τ_−] × 𝒦, 0 < τ_1 < τ_− < τ_0, 𝒦 ⊂ (ι⁺)° compact. Then F(σ) := ℳ(τ⁻² f)(σ) ∈ C_c^∞(𝒦) is entire in σ, and for
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

    ‖(ℳv)(σ)‖_(H^(m,(a,c))_(0,b)) ≤ C ⟨σ⟩^(|m|) max(τ_1^(Im σ), τ_2^(Im σ)) ‖v‖_(H^(m,(a,b,c))_ebe).    {#eq:ii-f-6-7}

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

The support lemma below uses the Paley–Wiener–Schwartz theorem [Hö83, Theorem 7.3.1], which the appendix of results
from the literature states with its page: *a distribution u on ℝ with compact support in an interval [a, b] has an
entire Fourier–Laplace transform û(ζ) = ∫ e^(−itζ) u(t) dt with |û(ζ)| ≤ C (1 + |ζ|)^ν e^(H(Im ζ)) for some C, ν, where
H(η) := sup_(t∈[a,b]) tη is the supporting function of [a, b]; conversely, an entire function with such a bound is the
Fourier–Laplace transform of a distribution supported in [a, b].*

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
the Paley–Wiener–Schwartz theorem the support lies in {t ≥ log T} = {t_* ≥ T}. As φ is arbitrary, supp w ⊂ {t_* ≥ T}. ∎

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
