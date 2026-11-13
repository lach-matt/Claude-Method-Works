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

    𝗌′ := χ(R) 𝗌_I + (1 − χ(R)) 𝗌      on ᵉᵇᵉS*([0, T_+⁻¹) × ι⁺).                                         {#eq:ii-f-7-1}

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
(2)). Let ψ_q ∈ C^∞(ℝ), 0 ≤ ψ_q ≤ 1, vanish on (−∞, 1/32] and equal 1 on [1/16, ∞), and

    Θ := t_* + q(r),      q(r) := (19/10) ∫_0^r ψ_q(r′/t_(*,0)) dr′.

Θ is non-decreasing along future causal curves of g_aux for t_(*,0) large. Where ψ_q = 0, dΘ = dt_* ([[lem:ii-f-1-4]]
(a)). Where r ≥ t_(*,0)/32, dΘ = dt_* + q′ dr with q′ ∈ [0, 19/10], so Ḡ(dΘ) = −q′(2 − q′) ≤ −q′/10, while G_0(dΘ) ≤
G_0(dt_*) − q′(2 − q′) + C r⁻² q′(2 + q′) < 0 for r large, by [[lem:ii-b-1-1]] (dt_* is past timelike, and g_0⁻¹ −
ḡ⁻¹ ∈ r⁻² C^∞(M; S²𝒯)); dΘ, which deforms continuously to dt_* through such covectors, is past causal for G_0 and Ḡ,
hence for G_0 + a(Ḡ − G_0) (the cone argument of [[lem:ii-f-1-4]]). For r ≥ t_(*,0)/16, q(r) = (19/10) r − κ t_(*,0)
with κ := (19/10) ∫_0^(1/16) (1 − ψ_q) ∈ [0, 19/160]. On supp f_1 ⊂ {R ≥ 1, t_* ≥ t_(*,0)}, r ≥ t_* ≥ t_(*,0), so
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
        ≤ C (‖P^ε_+ u‖_((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2)) + ‖u‖_((𝗌_(♭,I);k),(2γ_I,γ_+,γ_cf))).               {#eq:ii-f-7-2}

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
        ≤ C (‖P^ε_+ u‖_((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2)) + ‖u‖_((𝗌′;k),(2γ_I,γ_+−1,γ_cf))).                 {#eq:ii-f-7-3}

*Absorption.* Multiplication by χ_0(τ/δ_1) maps H^((𝗌′;k),(2γ_I,γ_+,γ_cf)) to H^((𝗌′;k),(2γ_I,γ_+−1,γ_cf)) with norm ≤
Cδ_1, as it equals τχ_0(τ/δ_1) times the identity of weights, and τχ_0(τ/δ_1) = δ_1·(τ/δ_1)χ_0(τ/δ_1) has
C^∞_b-seminorms O(δ_1). Fix δ_1 with C·Cδ_1 ≤ 1/2 in [[eq:ii-f-7-3]]. For ε < δ_1/2, P^ε_+ = P_+ on {τ ≥ δ_1}, and (1 −
χ_0(τ/δ_1))u is controlled by [[lem:ii-f-7-5]] for P^ε_+, with T := 2δ_1⁻¹ and ψ_T ∈ C_c^∞((−∞, T)) equal to 1 on (−∞,
δ_1⁻¹], with constants independent of ε: the support of 1 − χ_0(τ/δ_1) lies in {t_* ≤ δ_1⁻¹}, where ψ_T = 1 and u is the
finite-time solution by uniqueness. Hence, for u in the space of [[lem:ii-f-7-7]] and ε < δ_1/2,

    ‖u‖_(Ḣ^((𝗌′;k),(2γ_I,γ_+,γ_cf))_(ebe;b)) ≤ C ‖P^ε_+ u‖_(Ḣ^((𝗌′−1;k),(2γ_I+2,γ_++2,γ_cf−2))_(ebe;b)),            {#eq:ii-f-7-4}

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
