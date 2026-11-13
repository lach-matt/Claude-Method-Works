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
