### The a priori estimate at level four {#sec:tl5-hf4}

[[thm:tl5-hf]] is proved at a level N ≥ 6: the energies of h = g − ĝ are commuted with the seven fields of Γ up to
order N. This section proves the same statement at level four, with N := 4 throughout. The results of [[sec:tl5-hf]]
up to [[lem:tl5-hf-reduced]], and [[lem:tl5-hf-quasilinear]], [[lem:tl5-hf-conversions]] and [[def:tl5-hf-norm]], do
not depend on the level, and are used here at N = 4 as they stand. [[def:tl5-hf-levels]], [[lem:tl5-hf-quadratic]] and
[[lem:tl5-hf-linfty]] are replaced by [[def:tl5-hf4-levels]], [[lem:tl5-hf4-quadratic]] and [[lem:tl5-hf4-linfty]], and
the proofs of [[prop:tl5-hf-bootstrap]] and [[thm:tl5-hf]] are used with these. What changes is the bound of the
quadratic terms. At level four two kinds of products have no factor bounded at a point ([[lem:tl5-hf4-quadratic]]); on
the future faces they are bounded by a Hölder inequality in mixed norms, the supremum over the leaves against the
supremum along the face ([[lem:tl5-hf4-face]], [[lem:tl5-hf4-mixed]]). The same inequality gives the persistence of
regularity at level four ([[lem:tl5-hf4-persistence]]), and [[thm:tl5-hf4]] collects the results.

#### The products at level four {#sec:tl5-hf4-products}

**Definition {#def:tl5-hf4-levels}** (Level four.) Let N := 4. For a C⁶ symmetric 2-tensor field h with g = ĝ + h
Lorentzian, let 𝔰, 𝔧, Λ and 𝔠_n (n ≤ 4) be given by the formulas of [[def:tl5-hf-levels]] with N = 4:

    𝔰 = max(|H|, |Ψ_B| (|B| ≤ 2), |D̂Ψ_B| (|B| ≤ 1), |D̂²h|),
    𝔧 = max(𝔰, |Ψ_B|, |D̂Ψ_B| (|B| ≤ 4), |D̂²Ψ_B| (|B| ≤ 3)),

Λ ≥ 1 being a bound at the point for the norms of ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z], D̂ℒ^B Γ′[π^Z] and ℒ^B R̂ for
all words B with |B| ≤ 4 and all Z ∈ Γ, and 𝔠_n being given by [[eq:tl5-hf-cn]]. The order of a solution factor H,
Ψ_B, D̂Ψ_B or D̂²Ψ_B is 0, |B|, |B| + 1 or |B| + 2. Put, at each point,

    𝔭_M² := Σ_(|B|=|B′|=2) |D̂Ψ_B|² |D̂Ψ_(B′)|² + Σ_(|B|=3) Σ_(Z∈Γ) |Ψ_B|² |D̂²Ψ_Z|²,                    {#eq:tl5-hf4-pm}

the sums over the words B, B′ in Γ of the lengths shown.

**Lemma {#lem:tl5-hf4-quadratic}** (The quadratic terms at level four.) Let h be a smooth symmetric 2-tensor field with
g = ĝ + h Lorentzian, p a point with |h(p)| ≤ 1/8, and I a word in Γ.

(a) In the expansion of ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I of the proof of [[lem:tl5-hf-quadratic]], every monomial has at
least two solution factors; these carry disjoint sets of the letters of I, and the numbers of derivatives D̂ on them add
up to at most two. So their orders add up to at most |I| + 2, and each of them has order at most |I| + 1.

(b) Let |I| ≤ 4 and 𝔰(p) ≤ 1/8. Then at p

    ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I = 𝔑^L_I + 𝔑^M_I,      |𝔑^L_I| ≤ 𝔠_(|I|) 𝔰 𝔧,      |𝔑^M_I| ≤ 𝔠_(|I|) 𝔭_M,  {#eq:tl5-hf4-g}

where 𝔑^M_I is the sum of the monomials with at least two high factors, in the sense of the proof below, and 𝔑^L_I the
sum of the others; and 𝔑^M_I = 0 if |I| ≤ 3.

*Proof.* (a) The expansion in the proof of [[lem:tl5-hf-quadratic]] distributes the letters of I over the factors of
each term of N(h), each letter going to one factor, and expands the Lie derivatives of the factors by (i)–(iv) there;
it does not use the level, nor does the statement there that every monomial has at least two solution factors. Each
term of N(h) carries at most two derivatives D̂ on its solution factors (H and D̂²h, H and h, D̂h and D̂h, the factors g⁻¹
carrying none), and the expansions (i)–(iv) do not increase this number: in (ii) and (iii) the solution factors of the
remainders carry fewer derivatives than D̂h and D̂²h, and in (iv) the solution factors are H and Ψ_B. The order of a
factor is the number of its letters plus the number of its derivatives D̂, which gives the bound |I| + 2 for the sum. A
factor of order |I| + 2 carries all letters and two derivatives, so it is D̂²Ψ_I, which occurs only in H^(αβ) D̂_αD̂_βΨ_I
and is subtracted; so every factor has order at most |I| + 1.

(b) As |h(p)| ≤ 1/8, |H| ≤ 1/4 and |g⁻¹| ≤ 𝔤₀ at p, as in the proof of [[lem:tl5-hf-quadratic]], and the total
background norm of the monomials, with the coefficients, is at most 𝔠_(|I|) by that proof. Call a solution factor high
if it is not a low quantity of [[def:tl5-hf4-levels]]: Ψ_B with |B| ≥ 3, D̂Ψ_B with |B| ≥ 2, or D̂²Ψ_B with |B| ≥ 1. A
monomial with at most one high factor and q solution factors is bounded by its background norm times 𝔰^(q−1) 𝔧 ≤ 𝔰𝔧,
the high factor, or any one, being bounded by 𝔧 and the others by 𝔰 ≤ 1; this gives the bound for 𝔑^L_I. Consider a
monomial with two high factors. In the terms from 2𝔮 the solution factors are of the forms Ψ_B and D̂Ψ_B, and two high
ones carry at least four letters; with four, they are D̂Ψ_B and D̂Ψ_(B′) with |B| = |B′| = 2, as a high factor Ψ_B
carries three. In the terms from H^(λσ)D̂_λD̂_σh the solution factors from the expansion of H are of the forms H and
Ψ_B, high only for |B| ≥ 3, and the one factor from the expansion of D̂²h is of the form D̂²Ψ_B, D̂Ψ_B or Ψ_B, high only
for |B| ≥ 1, 2 or 3; two high factors carry at least four letters, and with four they are Ψ_B with |B| = 3 and D̂²Ψ_Z
with Z ∈ Γ. In the terms from 2𝔠(H)h the solution factors are of the forms H and Ψ_B, and two high ones carry at least
six letters. So 𝔑^M_I = 0 if |I| ≤ 3. If |I| = 4, the two high factors of a monomial of 𝔑^M_I form one of the two pairs
of [[eq:tl5-hf4-pm]] and carry all four letters; its other solution factors carry no letter and, by (a), no derivative,
so they are H or h, bounded by 𝔰 ≤ 1. The product of the two high factors is the square root of one term of 𝔭_M², so
the monomial is bounded by its background norm times 𝔭_M, and summing gives the bound for 𝔑^M_I. ∎

**Lemma {#lem:tl5-hf4-face}** (A Hölder inequality in mixed norms on a face.) Let t ∈ [−10, u*] and b ∈ [1/2, v*] be
such that Σ := Σ₁(t, b) is not empty, and let γ_ω(v) := (t − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_Σ, ω ∈ S³, be the curves
of the proof of [[lem:tl5-hf-sobolev]] that fill Σ, starting on the leaf S_t := {t} × {1/2} × S³ of N₀. Let φ be as in
[[prop:tl5-hf-linear]]. For a tensor field A on Q(t, b), with A_e as in [[def:tl5-hf-component]], put

    ‖A‖_Σ² := ∫_Σ e^(−φ) |A|² dμ dτ₂/(1 − κκ′),
    ⟦A⟧_(2,∞)² := ∫_(1/2)^(v_Σ) e^(−φ) sup_(ω∈S³) |A_e(γ_ω(v))|² dv,
    ⟦A⟧_(∞,2)² := sup_(1/2≤v≤v_Σ) e^(−φ) ∫_(S³) |A_e(γ_ω(v))|² dω,

φ being evaluated on the leaf through γ_ω(v), on which it is constant. For a function f on D^κ let [f]_t be its
supremum over Σ₁(t, v*), and put, with 𝔭_r := 1 + 12r² + 144r⁴ as in [[eq:tl5-hf-cs-r]],

    𝔵_r(t) := [𝔳^(2r) R⁻³]_t,   𝔱_r(t) := [𝔳^(2r) R⁻³ max(1 + 2r² |D̂∂_γ|², 2|∂_γ|²)]_t,   𝔪(t) := [max(1, 𝔴)⁶ R^(3/2)]_t.

Then for every smooth covariant tensor field A of rank r ≤ 4 on Q(t, b):

(a) ⟦A⟧_(∞,2)² ≤ [𝔳^(2r)]_t ∫_(S_t) |A|² dω + 𝔱_r(t) (‖A‖_Σ² + ‖D̂A‖_Σ²);

(b) ⟦A⟧_(2,∞)² ≤ (1/2) 𝔭_r 𝔵_r(t) Σ_(|J|≤2) ‖ℒ^J A‖_Σ², J ranging over the words in the six rotations;

(c) if X and Y are smooth covariant tensor fields on Q(t, b) of ranks r_X and r_Y with r_X + r_Y ≤ 6, and f is a
function on Σ with |f| ≤ |X| |Y| at every point, then, with φ(t, b) := Φ_o(t) + Φ_i(b),

    ‖f‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) ⟦X⟧_(2,∞) ⟦Y⟧_(∞,2).                                                   {#eq:tl5-hf4-holder}

*Proof.* Along γ_ω, τ₁ = t and dτ₂/dv = 1 − κκ′ > 0, so φ = Φ_o(t) + Φ_i(τ₂) is nondecreasing in v, as a_i ≥ 0, and at
most φ(t, b) on Σ; it depends only on (u, v), so it is constant on each leaf. On Σ, dμ dτ₂/(1 − κκ′) = R³ dω dv, as in
the proof of [[lem:tl5-hf-sobolev]].

(a) Fix ω. Since ∂_γ := ∂_v − κ′∂_u commutes with the fields of 𝒱 ([[lem:tl5-hf-components]]),
(d/dv)|A_e|²(γ_ω(v)) = 2⟨A_e, (ℒ_(∂_γ)A)_e⟩ ≤ |A_e|² + |(ℒ_(∂_γ)A)_e|². Integrate over S³ and from 1/2 to v, and use
e^(−φ(v)) ≤ e^(−φ(v′)) for v′ ≤ v and e^(−φ) ≤ 1:

    e^(−φ(v)) ∫ |A_e|²(γ_ω(v)) dω ≤ ∫_(S_t) |A_e|² dω + ∫_(1/2)^v e^(−φ) ∫ (|A_e|² + |(ℒ_(∂_γ)A)_e|²) dω dv′.

By [[lem:tl5-hf-components]], |B_e| ≤ 𝔳^r |B| for every tensor B of rank r. As D̂ is torsion free, ℒ_(∂_γ)A =
D̂_(∂_γ)A + Σ_(i=1)^r A(…, D̂∂_γ ·, …), the i-th slot receiving D̂∂_γ; so |ℒ_(∂_γ)A| ≤ |∂_γ| |D̂A| + r |D̂∂_γ| |A|, and
|A_e|² + |(ℒ_(∂_γ)A)_e|² ≤ 𝔳^(2r) ((1 + 2r²|D̂∂_γ|²)|A|² + 2|∂_γ|²|D̂A|²). With dω dv = R⁻³ dμ dτ₂/(1 − κκ′), this
gives (a).

(b) Fix v. By [[lem:tl5-hf-sphere]], with 6C_(S³)² = 1/2, applied to each component of A_e on the leaf through
γ_ω(v), sup_ω |A_e|² is at most 1/2 times the integral over the leaf of the sum over the components of f² + Σ (K f)² +
Σ (K′K f)². By [[lem:tl5-hf-components]], with r slots, |K(B_e)| ≤ |(ℒ_K B)_e| + r|B_e| and |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K
B)_e| + r|(ℒ_K B)_e| + r|(ℒ_(K′)B)_e| + r²|B_e|, the index actions being constant; squaring, with (x + y)² ≤ 2(x² + y²)
and (x + y + z + w)² ≤ 4(x² + y² + z² + w²), and summing over the six K and the 36 pairs (K, K′), the sum is at most 𝔭_r
Σ_(|J|≤2) |(ℒ^J A)_e|², the coefficients being 1 + 12r² + 144r⁴, 2 + 48r² and 4. With |(ℒ^J A)_e| ≤ 𝔳^r |ℒ^J A|,
multiply by e^(−φ), constant on the leaf, integrate over v and use dω dv = R⁻³ dμ dτ₂/(1 − κκ′).

(c) By [[lem:tl5-hf-components]], |f| ≤ |X| |Y| ≤ 𝔴^(r_X + r_Y) |X_e| |Y_e| ≤ max(1, 𝔴)⁶ |X_e| |Y_e|, so ‖f‖_Σ² ≤
𝔪(t)² ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv. Writing e^(−φ) = e^φ e^(−φ) e^(−φ), with e^φ ≤ e^(φ(t,b)) on Σ,

    ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv ≤ e^(φ(t,b)) ∫ (e^(−φ) sup_ω |X_e|²) (e^(−φ) ∫ |Y_e|² dω) dv
      ≤ e^(φ(t,b)) ⟦X⟧_(2,∞)² ⟦Y⟧_(∞,2)².                                                              ∎

