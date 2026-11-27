### The a priori estimate at level four {#sec:tl5-hf4}

[[thm:tl5-hf]] is proved at a level N ≥ 6: the energies of h = g − ĝ are commuted with the seven fields of Γ up to
order N. This section proves its counterpart at level four, with N := 4 throughout. The results of [[sec:tl5-hf]]
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

    ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I = 𝔑^L_I + 𝔑^M_I,
    |𝔑^L_I| ≤ 𝔠_(|I|) 𝔰 𝔧,      |𝔑^M_I| ≤ 𝔠_(|I|) 𝔭_M,                                                    {#eq:tl5-hf4-g}

where 𝔑^M_I is the sum of the monomials with at least two high factors, in the sense of the proof below, and 𝔑^L_I the
sum of the others; and 𝔑^M_I = 0 if |I| ≤ 3.

*Proof.* (a) The expansion in the proof of [[lem:tl5-hf-quadratic]] distributes the letters of I over the factors of each
term of N(h), each letter going to one factor, and expands the Lie derivatives of the factors by (i)–(iv) there; it does
not use the level, nor does the statement there that every monomial has at least two solution factors. Each term of N(h)
carries at most two derivatives D̂ on its solution factors (H and D̂²h, H and h, D̂h and D̂h, the factors g⁻¹ carrying
none), and the expansions (i)–(iv) do not increase this number: in (ii) and (iii) the solution factors of the remainders
carry fewer derivatives than D̂h and D̂²h, and in (iv) the solution factors are H and Ψ_B. The order of a factor is the
number of its letters plus the number of its derivatives D̂, which gives the bound |I| + 2 for the sum. A factor of
order |I| + 2 carries all letters and two derivatives, so it is D̂²Ψ_I, which occurs only in H^(αβ) D̂_αD̂_βΨ_I and is
subtracted; so every factor has order at most |I| + 1.

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
such that Σ := Σ₁(t, b) is not empty, and let γ_ω(v) := (t − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_Σ, ω ∈ S³, with v_Σ the
largest value of v on Σ, be the curves of the proof of [[lem:tl5-hf-sobolev]] that fill Σ, with velocity
∂_γ := ∂_v − κ′∂_u, starting on the leaf S_t := {t} × {1/2} × S³ of N₀. Let φ be as in
[[prop:tl5-hf-linear]]. For a tensor field A on Q(t, b), with A_e as in [[def:tl5-hf-component]], put

    ‖A‖_Σ² := ∫_Σ e^(−φ) |A|² dμ dτ₂/(1 − κκ′),
    ⟦A⟧_(2,∞)² := ∫_(1/2)^(v_Σ) e^(−φ) sup_(ω∈S³) |A_e(γ_ω(v))|² dv,
    ⟦A⟧_(∞,2)² := sup_(1/2≤v≤v_Σ) e^(−φ) ∫_(S³) |A_e(γ_ω(v))|² dω,

φ being evaluated on the leaf through γ_ω(v), on which it is constant. For a function f on D^κ let [f]_t be its
supremum over Σ₁(t, v*), and put, with 𝔭_r := 1 + 12r² + 144r⁴ as in [[eq:tl5-hf-cs-r]],

    𝔵_r(t) := [𝔳^(2r) R⁻³]_t,      𝔪(t) := [max(1, 𝔴)⁶ R^(3/2)]_t,
    𝔱_r(t) := [𝔳^(2r) R⁻³ max(1 + 2r² |D̂∂_γ|², 2|∂_γ|²)]_t.

Then for every smooth covariant tensor field A of rank r with 1 ≤ r ≤ 4 on Q(t, b):

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

By [[lem:tl5-hf-components]], |B_e| ≤ 𝔳^r |B| for every tensor B of rank r. As D̂ is torsion free, ℒ_(∂_γ)A = D̂_(∂_γ)A +
Σ_(i=1)^r A(…, D̂∂_γ ·, …), the i-th slot receiving D̂∂_γ; so |ℒ_(∂_γ)A| ≤ |∂_γ| |D̂A| + r |D̂∂_γ| |A|,
and |A_e|² + |(ℒ_(∂_γ)A)_e|² ≤ 𝔳^(2r) ((1 + 2r²|D̂∂_γ|²)|A|² + 2|∂_γ|²|D̂A|²). With dω dv = R⁻³ dμ dτ₂/(1 − κκ′), this
gives (a).

(b) Fix v. By [[lem:tl5-hf-sphere]], with 6C_(S³)² = 1/2, applied to each component f of A_e on the leaf through
γ_ω(v), sup_ω |A_e|² is at most 1/2 times the integral over the leaf of the sum over the components of
f² + Σ (K f)² + Σ (K′K f)². By [[lem:tl5-hf-components]], with r slots, |K(B_e)| ≤ |(ℒ_K B)_e| + r|B_e|
and |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K B)_e| + r|(ℒ_K B)_e| + r|(ℒ_(K′)B)_e| + r²|B_e|, the index actions being constant. Squaring,
with (x + y)² ≤ 2(x² + y²) and (x + y + z + w)² ≤ 4(x² + y² + z² + w²), and summing over the six K and the 36 pairs
(K, K′), the sum is at most 𝔭_r Σ_(|J|≤2) |(ℒ^J A)_e|², the coefficients being 1 + 12r² + 144r⁴, 2 + 48r² and 4.
With |(ℒ^J A)_e| ≤ 𝔳^r |ℒ^J A|, multiply by e^(−φ), constant on the leaf, integrate over v and use
dω dv = R⁻³ dμ dτ₂/(1 − κκ′).

(c) By [[lem:tl5-hf-components]], |f| ≤ |X| |Y| ≤ 𝔴^(r_X + r_Y) |X_e| |Y_e| ≤ max(1, 𝔴)⁶ |X_e| |Y_e|, so ‖f‖_Σ² ≤
𝔪(t)² ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv. Writing e^(−φ) = e^φ e^(−φ) e^(−φ), with e^φ ≤ e^(φ(t,b)) on Σ,

    ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv ≤ e^(φ(t,b)) ∫ (e^(−φ) sup_ω |X_e|²) (e^(−φ) ∫ |Y_e|² dω) dv
      ≤ e^(φ(t,b)) ⟦X⟧_(2,∞)² ⟦Y⟧_(∞,2)²,

which is (c). ∎

**Lemma {#lem:tl5-hf4-linfty}** (The low quantities at level four.) Let g be a solution of the reduced problem on
D^κ_s, h := g − ĝ, p ∈ D^κ_s, and let 𝔰₀ and the other quantities of [[lem:tl5-hf-linfty]] be formed with N = 4 and the
quantities of [[def:tl5-hf4-levels]]. If 𝔰 ≤ 𝔰₀ on Q(τ₁(p), τ₂(p)), then [[eq:tl5-hf-linfty]] holds at p, and at every
point of Q(τ₁(p), τ₂(p))

    M₂ ≤ 2(k₁ + 1) 𝒥₁ + 2k₂ ϱ(p),      M₂ = max_(|C|≤3) |D̂²Ψ_C|.                                      {#eq:tl5-hf4-m2}

*Proof.* The proof of [[lem:tl5-hf-linfty]] uses the level only through [[lem:tl5-hf-quadratic]], which it applies to
the words of length at most N − 1 = 3 and, in its last step, to the word of length N − 4 = 0, whose monomials have only
low solution factors. For these words [[lem:tl5-hf4-quadratic]] (b) gives the bounds used there, as 𝔑^M vanishes on
them. Every other step holds for N = 4 as written, and its step on second derivatives gives [[eq:tl5-hf4-m2]], ϱ(p)
bounding |ℒ^J(2R̂ic)|, |J| ≤ 3, on Q(τ₁(p), τ₂(p)). ∎

**Lemma {#lem:tl5-hf4-mixed}** (The products with no factor at a point.) Let g be a solution of the reduced problem on
D^κ_s, h := g − ĝ, t ∈ [−10, u*] and b ∈ [1/2, s] with Σ := Σ₁(t, b) not empty, and suppose that 𝔰 ≤ 𝔰₀ on Q(t, b), with
𝔰₀ as in [[lem:tl5-hf4-linfty]]. Let ϱ ≥ max_(|J|≤3) |ℒ^J(2R̂ic)| on Q(t, b), and η₀ ≥ max(𝔰, |Ψ_C| (|C| ≤ 4), |D̂Ψ_C|
(|C| ≤ 3)) on N₀ ∩ Q(t, b). With the notation of [[lem:tl5-hf4-face]], 𝒥₁, k₁ and k₂ as in [[lem:tl5-hf4-linfty]] and 𝔨₂
:= (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²), put 𝔍 := ‖𝒥₁‖_Σ and

    λ_t := 2([k₁]_t + 1),      ς_t := 2[k₂]_t (∫_(Σ₁(t,v*)) dμ dτ₂/(1 − κκ′))^(1/2),
    𝔛_t := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ]_t²),
               (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),
    𝔜_t := max(𝔱₃(t)^(1/2) (1 + 7λ_t), 7 𝔱₃(t)^(1/2) ς_t, 𝔱₂(t)^(1/2), π (98 [𝔳⁶]_t)^(1/2), π (686 [𝔳⁴]_t)^(1/2)).

Then

    ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔛_t 𝔜_t (𝔍 + ϱ) (𝔍 + ϱ + η₀),
    𝔍² ≤ [𝔨₂]_t Σ_(|I|≤4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                                  {#eq:tl5-hf4-mixed}

*Proof.* On Σ, |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) = 𝔨₂ (1 − κκ′) ε₁[Ψ_C] by [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], which gives the second inequality. By [[eq:tl5-hf4-m2]] at the points of Σ, with e^(−φ) ≤ 1
and Σ ⊂ Σ₁(t, v*), ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ.

The function 𝔭_M² is a sum of products |X|² |Y|² over the pairs (X, Y) := (D̂Ψ_B, D̂Ψ_(B′)), |B| = |B′| = 2, of ranks
3 and 3, and (X, Y) := (D̂²Ψ_Z, Ψ_B), |B| = 3, Z ∈ Γ, of ranks 4 and 2. So ‖𝔭_M‖_Σ² is the sum of ‖|X| |Y|‖_Σ² over
these pairs, and by [[eq:tl5-hf4-holder]] it is at most e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²), with

    X₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(2,∞)²,   Y₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(∞,2)²,
    X₂² := Σ_(Z∈Γ) ⟦D̂²Ψ_Z⟧_(2,∞)²,   Y₂² := Σ_(|B|=3) ⟦Ψ_B⟧_(∞,2)².

*X₁.* By (ii) of the proof of [[lem:tl5-hf-quadratic]], applied with Ψ_B in place of h, for a word J of rotations
with |J| ≤ 2, ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′ with R′ a sum of at most m′_(|J|) monomials, m′₀ = 0, m′₁ = 2, m′₂ = 6, each the
contraction of a coefficient of norm at most Λ with some Ψ_C, |C| ≤ 3; so |R′| ≤ m′_(|J|) Λ 𝒥₁. The words JB are distinct
and of length at most 4, there are 49 words B of length 2, and Σ_(|J|≤2) m′_(|J|)² = 6 · 4 + 36 · 36 = 1320; so Σ_B
Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥₁² + 2 · 49 · 1320 Λ² 𝒥₁² at every point, and by [[lem:tl5-hf4-face]] (b) with r = 3, X₁ ≤ (𝔭₃ 𝔵₃(t)
(1 + 64680 [Λ]_t²))^(1/2) 𝔍.

*X₂.* By (iii) of that proof, applied with Ψ_Z in place of h, ℒ^J D̂²Ψ_Z = D̂²Ψ_(JZ) + R with R a sum of at most m_(|J|)
monomials, m₁ = 7, m₂ = 35, each with at most two background factors of norm at most Λ and one solution factor D̂Ψ_C or
Ψ_C with |C| ≤ 2; so |R| ≤ m_(|J|) Λ² 𝒥₁, while |D̂²Ψ_(JZ)| ≤ M₂ as |JZ| ≤ 3. There are 7 fields Z and 43 words J, and
Σ_(|J|≤2) m_(|J|)² = 6 · 49 + 36 · 35² = 44394; so Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M₂² + 621516 Λ⁴ 𝒥₁², and by
[[lem:tl5-hf4-face]] (b) with r = 4 and √621516 < 789, X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 ‖M₂‖_Σ + 789 [Λ]_t² 𝔍).

*Y₁ and Y₂.* On S_t ⊂ N₀ ∩ Q(t, b), |D̂Ψ_B| ≤ η₀ for |B| ≤ 3 and |Ψ_B| ≤ η₀ for |B| ≤ 4, and ∫_(S_t) dω = 2π². By
[[lem:tl5-hf4-face]] (a) with r = 3 and r = 2, as Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M₂² and Σ_(|B|=2) |D̂Ψ_B|² ≤ 𝒥₁²,

    Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍² + 49 ‖M₂‖_Σ²),      Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍²,

there being 343 words of length 3.

With ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ these give X_i ≤ 𝔛_t (𝔍 + ϱ) and Y_i ≤ 𝔜_t (𝔍 + ϱ + η₀) for i = 1, 2, and (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ X₁ Y₁ + X₂ Y₂ gives the first inequality. ∎

#### The bootstrap at level four {#sec:tl5-hf4-bootstrap}

**Definition {#def:tl5-hf4-constants}** (The constants at level four.) Fix μ ∈ (0, 1], weights z, z̲, admissible rates
a_o, a_i for (𝔅₄, E_o⁴, E_i⁴) and φ as in [[prop:tl5-hf-linear]], and let Y_σ be the norm of [[def:tl5-hf-norm]], whose
definition and properties do not use N ≥ 5, with N = 4. Let G^♯ be data in the wave gauge, and let δ_w, ε_w, 𝔤₄, ϰ₀,
𝔞_o, 𝔞_i, S_F, 𝔯_w, 𝔰₀, 𝔰_θ and 𝔰₁ be given by the formulas of [[def:tl5-hf-constants]] with N = 4, the quantities of
[[def:tl5-hf4-levels]] and the constants of [[lem:tl5-hf4-linfty]], ϱ and η₀ being those of [[lem:tl5-hf4-linfty]] for a
point p with τ₁(p) = u*, τ₂(p) = v*. Put, with the notation of [[lem:tl5-hf4-face]] and [[lem:tl5-hf4-mixed]] and with
[𝔠₄]_t the number 𝔠₄ formed with [Λ]_t in place of Λ,

    m_t := 98 e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t [𝔠₄]_t 𝔪(t) 𝔛_t 𝔜_t,
    S_M := μ^(−2) ∫_(−10)^(u*) m_t [𝔨₂]_t dt,      𝔯_M := ∫_(−10)^(u*) m_t [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_M := μ² ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t dt,
    S_(F,4) := S_F + S_M,      𝔯_(w,4) := 𝔯_w + 𝔯_M,      ε_(w,4) := ε_w + ε_M,
    A_(w,4) := √2 δ_w + 2ε_(w,4),      B_(w,4) := 2 S_(F,4),                                      {#eq:tl5-hf4-constants}

and let 𝔰_* be given by the formula of [[def:tl5-hf-constants]] with N = 4 and A_(w,4) in place of A_w:

    𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−2) e^(φ(p)/2) A_(w,4) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).

As in [[def:tl5-hf-constants]], δ_w contains the fluxes of the Ψ_I and of 𝔟[Ψ_I], |I| ≤ 4, through N₀ and through N₁,
and η₀ and these fluxes are computed from the derivatives of G^♯ − ĝ on N of order at most 4, and of order 5 in the
terms 𝔟, which vanish where H does.

**Proposition {#prop:tl5-hf4-bootstrap}** (The a priori estimate at level four.) In the setting of
[[def:tl5-hf4-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴) and that

    𝔯_(w,4) ≤ 1/4,      η₀ < 𝔰₁,      𝔰_* < 𝔰₁.                                                   {#eq:tl5-hf4-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_(w,4) for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_* on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_(w,4) + B_(w,4) Y_s(g)².                                                                {#eq:tl5-hf4-h1}

*Proof.* The first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]] hold as written with N = 4, A_(w,4)
in place of A_w and [[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]]: g is vacuum and has on N ∩ D^κ_s the
derivatives of G^♯, so that the quantities on N₀ bounded by η₀ are those of g; and 𝔰 ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, so
that |h|_k̂ < κ_m/2 and θ_H ≤ ϑ.

Step 2 of that proof holds with N = 4, [[lem:tl5-hf4-quadratic]] and [[lem:tl5-hf4-linfty]] in place of
[[lem:tl5-hf-quadratic]] and [[lem:tl5-hf-linfty]], except at one place: |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ 3, as
there, but for |I| = 4 only |𝔑_I − 𝔑^M_I| ≤ 𝔠₄ 𝔰 𝔧. With 𝔑_I − 𝔑^M_I in place of 𝔑_I that step goes through, and the
terms 𝔑^M_I add to the bulk of the weighted sum over I, by the proof of the second inequality of
[[lem:tl5-hf-pointwise]], at most

    ∫_(Q(a′,b′)) e^(−φ) μ⁴ Σ_(|I|=4) 2Ω̂² |𝔑^M_I| (√e_o[Ψ_I] + √c √e_i[Ψ_I]) dμ du dv.

By the Cauchy–Schwarz inequality, √e_o + √c √e_i ≤ (1 + c/κ′)^(1/2) (e_o + κ′ e_i)^(1/2), and
e_o + κ′ e_i = (1 − κκ′) ε₁. Foliate Q(a′, b′) by the faces Σ₁(t, b′), −10 ≤ t ≤ a′, with du dv = dτ₁ dτ₂/(1 − κκ′),
and apply the Cauchy–Schwarz inequality on each nonempty face Σ := Σ₁(t, b′) and over I: the term is at most

    ∫_(−10)^(a′) [2Ω̂² (1 + c/κ′)^(1/2)]_t μ⁴ (Σ_(|I|=4) ‖𝔑^M_I‖_Σ²)^(1/2)
        × (Σ_(|I|=4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂)^(1/2) dt.

By [[eq:tl5-hf4-g]], ‖𝔑^M_I‖_Σ ≤ [𝔠₄]_t ‖𝔭_M‖_Σ, and as there are 7⁴ = 49² words of length 4, the second factor is at
most 49 [𝔠₄]_t ‖𝔭_M‖_Σ. The last factor is at most μ^(−2) Y_s. By Step 1, 𝔰 ≤ 𝔰₀ on D^κ_s, so [[lem:tl5-hf4-mixed]]
applies, with the ϱ and η₀ of [[def:tl5-hf4-constants]], and with 𝔍² ≤ [𝔨₂]_t μ^(−4) Y_s², as Σ_(|I|≤4) ∫_Σ e^(−φ)
ε₁[Ψ_I] dμ dτ₂ ≤ μ^(−4) Y_s². With e^(φ(t,b′)) ≤ e^(φ(t,v*)), the term is at most

    ∫_(−10)^(u*) m_t μ² (𝔍 + ϱ)(𝔍 + ϱ + η₀) Y_s dt ≤ S_M Y_s³ + 𝔯_M Y_s² + ε_M Y_s,

by μ²(𝔍 + ϱ)(𝔍 + ϱ + η₀) ≤ [𝔨₂]_t μ^(−2) Y_s² + [𝔨₂]_t^(1/2) (2ϱ + η₀) Y_s + μ² ϱ (ϱ + η₀).

Step 3 of that proof, with this term added, gives for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s ε_(w,4) + 𝔯_(w,4) Y_s² + S_(F,4) Y_s³,

and, as there, with ϑ ≤ 1/4 and 𝔯_(w,4) ≤ 1/4, Y_s² ≤ 2δ_w² + 2Y_s ε_(w,4) + 2S_(F,4) Y_s³, whence
[[eq:tl5-hf4-h1]]. ∎

**Lemma {#lem:tl5-hf4-persistence}** (Persistence of regularity at level four.) Suppose the hypotheses of
[[prop:tl5-hf4-bootstrap]] hold. For every k ≥ 0 there is C_k, depending only on k, ĝ, G^♯, κ, κ′, μ, ϑ, z, z̲, the rates
and A_(w,4), such that every solution g of the reduced problem on a D^κ_s with Y_σ(g) ≤ 2A_(w,4) for all σ ∈ [1/2, s] has
its components and their partial derivatives of order at most k, and the components of g⁻¹, bounded by C_k on D^κ_s, in
the coordinates (u, v, y) of a fixed finite atlas of S³.

*Proof.* By [[prop:tl5-hf4-bootstrap]], 𝔰 ≤ 𝔰_* on D^κ_s; in particular |H| ≤ 1/8, which bounds g⁻¹ = ĝ⁻¹ + H, and
θ_H ≤ ϑ. A constant is a number depending only on the data listed, Λ here bounding the quantities of
[[def:tl5-hf4-levels]] for words of every length that occurs. A face is a nonempty Σ := Σ₁(t, b) with t ≤ u* and b ≤
s; for a weight φ as in [[prop:tl5-hf-linear]] we use the norms of [[lem:tl5-hf4-face]], and write ‖·‖_(Σ,0) and
⟦·⟧⁰ for those with φ replaced by 0, to which that lemma applies with zero rates. For m ≥ 4 let P(m) be the statement:
there is a constant E_m such that on every face

    Σ_(|I|≤m) ∫_Σ ε₁[Ψ_I] dμ dτ₂ + Σ_(|B|≤m−1) ‖D̂²Ψ_B‖²_(Σ,0) ≤ E_m,

and |Ψ_B| (|B| ≤ m − 2), |D̂Ψ_B| (|B| ≤ m − 3) and |D̂²Ψ_B| (|B| ≤ m − 4) are at most E_m on D^κ_s. P(4) holds: the
face energies are at most μ^(−4) e^(Φ_o(u*) + Φ_i(v*)) 4A_(w,4)²; by [[eq:tl5-hf4-m2]] each |D̂²Ψ_B|, |B| ≤ 3, is at
most 2(k₁ + 1)𝒥₁ + 2k₂ϱ at every point, and ∫_Σ 𝒥₁² dμ dτ₂/(1 − κκ′) is at most [𝔨₂]_t times the face energy, as in
the proof of [[lem:tl5-hf4-mixed]]; and 𝔰 ≤ 𝔰_*.

Let m ≥ 5 and assume P(m − 1). Then every solution factor of order at most m − 3 is bounded at every point by a
constant, and every solution factor of order at most m has its norm ‖·‖_(Σ,0) bounded by a constant on every face:
Ψ_B and D̂Ψ_B with |B| ≤ m − 1 by [[eq:tl5-hf-coercive]], Ψ_B with |B| = m by |ℒ_ZΨ| ≤ |Z| |D̂Ψ| + 2|D̂Z| |Ψ|
([[eq:tl5-hf-lie]]), and D̂²Ψ_B with |B| ≤ m − 2 by P(m − 1). For a face and a weight φ let U_φ(Σ) be the sum of the
norms ‖Φ‖_Σ of the solution factors Φ of order m + 1: D̂Ψ_C with |C| = m, Ψ_C with |C| = m + 1 and D̂²Ψ_C with |C| =
m − 1.

*(i) The monomials.* Let |I| = n ≤ m and take a monomial of ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, with its solution factors
ordered by their orders. By [[lem:tl5-hf4-quadratic]] (a) these orders add up to at most n + 2 and each is at most n + 1.
If at most one factor has order at least m − 2, the others are bounded at every point, and the norm ‖·‖_Σ of the monomial
is at most a constant times ‖Φ‖_Σ, Φ the factor of largest order; this is at most a constant if Φ has order at most m,
and otherwise at most a constant times U_φ(Σ). If two factors have orders o ≤ o′ with o ≥ m − 2, then 2(m − 2) ≤ o + o′ ≤
m + 2, so m ≤ 6 and o, o′ ≤ 4; a third factor of order at least m − 2 would need 3(m − 2) ≤ m + 2, which fails, so the
other factors are bounded at every point. At most one of the two is of the form D̂²Ψ_C, as there are at most two
derivatives D̂ in all. Let Y be one that is not, the one of larger order if neither is, and X the other; then o_X ≤ 4 and
o_Y ≤ 4, and 4 ≤ m − 1. By [[eq:tl5-hf4-holder]], with the weight on one of the two factors, the norm ‖·‖_Σ of the
monomial is at most a constant times ⟦X⟧_(2,∞) ⟦Y⟧⁰_(∞,2) and at most a constant times ⟦X⟧⁰_(2,∞) ⟦Y⟧_(∞,2); for this,
the proof of (c) of that lemma is used with e^(−φ) |X_e|² |Y_e|² bounded by (e^(−φ) sup_ω |X_e|²) ∫ |Y_e|² dω, or by
sup_ω |X_e|² (e^(−φ) ∫ |Y_e|² dω), after integration over the leaf. By [[lem:tl5-hf4-face]] (b), and (ii), (iii) of the
proof of [[lem:tl5-hf-quadratic]] for the words JX, |J| ≤ 2, ⟦X⟧_(2,∞) is at most a constant times the norms of factors
of order at most o_X + 2 ≤ m + 1; and by (a) of that lemma ⟦Y⟧_(∞,2) is at most a constant times the norms of factors of
order at most o_Y + 1 ≤ m + 1 plus the integral of |Y|² over S_t, a derivative of G^♯ − ĝ on N₀ of order at most m and so
a constant. Factors of order m + 1 occur on both sides only if o_X + 2 = o_Y + 1 = m + 1, that is if o_X + o_Y = 2m − 1,
which exceeds m + 2; so, taking the weight on the side where they occur, the norm ‖·‖_Σ of the monomial is at most a
constant times 1 + U_φ(Σ).

*(ii) Second derivatives.* For |B| = m − 1 apply [[lem:tl5-hf-recovery]] at every point of a face, with the tensor H of
g, as in the proof of [[lem:tl5-hf-linfty]]: |D̂²Ψ_B| is at most a constant times Σ_Z |D̂Ψ_(ZB)| + |D̂Ψ_B| + |Ψ_B|
plus |𝔣_B|, 𝔣_B := L̂Ψ_B + H^(αβ)D̂_αD̂_βΨ_B being given by [[def:tl5-hf-coupling]] with 𝔤 = 2R̂ic − N(h) as there. Its
nonlinear part consists of the monomials of (i) for the words of length n ≤ m − 1, and of the terms H^(αβ)D̂_αD̂_βΨ_J
with |J| ≤ m − 2. These have norms ‖·‖_(Σ,0) bounded by constants: in the first case of (i) the factor of largest order
has order at most n + 1 ≤ m, and in the second case 2(m − 2) ≤ o + o′ ≤ n + 2 ≤ m + 1 forces m = 5 and o = o′ = 3, so
that o_X + 2 = 5 = m and o_Y + 1 = 4. The linear part is bounded by constants times the jets of level at most m − 1 and
the residual. So, for every weight, ‖D̂²Ψ_B‖_Σ is at most a constant times 1 + (Σ_(|C|=m) ‖D̂Ψ_C‖_Σ²)^(1/2), and
U_φ(Σ) ≤ c_m (1 + 𝔈_φ(Σ)^(1/2)) with a constant c_m and 𝔈_φ(Σ) := Σ_(|I|≤m) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂, by
[[eq:tl5-hf-coercive]] and [[eq:tl5-hf-lie]].

*(iii) The energies.* By [[lem:tl5-hf-allocation]] there are constant rates A, A′ admissible for
((1 − ϑ)⁻¹ 𝔅_m, E_o^m, E_i^m), all entries being bounded on D^κ; for a constant Ã ≥ 0 take a_o := A + Ã and a_i := A′,
which are admissible too, as [[eq:tl5-hf-admissible]] is monotone in the rates, and the weight
φ := (A + Ã)(τ₁ + 10) + A′(τ₂ − 1/2). For |I| ≤ m apply [[lem:tl5-hf-identity]] to J̃ := J[Ψ_I] − 𝔟[Ψ_I] on
Q(a′, b′) ⊂ D^κ_s, with weights 1 and with 𝔅_m formed with μ = 1, as in Step 2 of the proof of
[[prop:tl5-hf-bootstrap]] at level m, which uses [[def:tl5-hf-coupling]] and the argument of [[prop:tl5-hf-linear-n]]
at level m. The face densities are at least 1 − ϑ times ε₁ and ε₂; the terms on N₁ and N₀ are fluxes of derivatives
of G^♯ − ĝ of order at most m + 1 ([[thm:tl5-wg]] (F4_W)), and so constants; and the linear bulk, with the weight and
the terms 𝔟 in it, is at most −(1 − ϑ) Ã (e_o + κ′ e_i) plus the forcing term of the residual. Indeed, as there,
2Ω̂² dφ(J) = (a_o + κa_i) e_o + (a_i + κ′a_o) e_i and 2Ω̂² |dφ(𝔟)| is at most ϑ times this; and of (1 − ϑ) times
this, the part with the rates A, A′ dominates ñᵀ𝔅_m ñ by their admissibility, and the rest is
(1 − ϑ) Ã (e_o + κ′ e_i). The term 𝔮_H is at most a constant times e_o + e_i ≤ (1 + 1/κ′)(e_o + κ′e_i), as in Step 2
of that proof. The nonlinear terms of L̂Ψ_I + H^(αβ)D̂_αD̂_βΨ_I are the monomials of (i) and the terms 𝔔_IJ ℒ^J N(h)
with |J| < |I|, whose terms H^(αβ)D̂_αD̂_βΨ_J are bounded by (ii); foliating by the faces Σ₁(t, b′) as in the proof of
[[prop:tl5-hf4-bootstrap]], their contribution is at most ∫ dt c (1 + 𝔈_φ(Σ₁(t, b′))) with a constant c, by (i), (ii)
and 2x ≤ 1 + x². The term −(1 − ϑ) Ã (e_o + κ′ e_i) contributes −(1 − ϑ) Ã ∫ dt 𝔈_φ(Σ₁(t, b′)), since
∫_Q e^(−φ) (e_o + κ′ e_i) dμ du dv = ∫ dt ∫_(Σ₁(t,b′)) e^(−φ) ε₁ dμ dτ₂. With Ã so large that (1 − ϑ) Ã exceeds c and
the constant of 𝔮_H, and with the residual bounded as in [[prop:tl5-hf-linear]], the supremum Y_m² of the weighted
level-m energies over the corner regions in D^κ_s satisfies Y_m² ≤ c′ + 𝒮_m Y_m with constants c′ and 𝒮_m. So Y_m is
bounded by a constant, and so are the unweighted energies, which are at most e^((A+Ã)(u*+10) + A′(v*−1/2)) Y_m², and
by (ii) the norms ‖D̂²Ψ_B‖_(Σ,0), |B| = m − 1.

*(iv) Bounds at a point.* [[lem:tl5-hf-sobolev]] and [[eq:tl5-hf-cs-r]], whose terms on S_a are derivatives of G^♯ − ĝ on
N₀ of order at most m, bound |Ψ_B| (|B| ≤ m − 2) and |D̂Ψ_B| (|B| ≤ m − 3) at every point by the face energies of level m
and the face norms of D̂²Ψ_C, |C| ≤ m − 1. [[lem:tl5-hf-recovery]] at the point, in order of increasing |B| ≤ m − 4,
bounds |D̂²Ψ_B|: its nonlinear terms come from words of length at most m − 4, whose solution factors have orders at most
m − 3 by [[lem:tl5-hf4-quadratic]] (a) and are bounded at the point by the bounds just obtained, by P(m − 1) and by the
induction on |B|, besides H^(αβ)D̂_αD̂_βΨ_B, which the lemma absorbs. So P(m) holds for every m ≥ 4.

The last paragraph of the proof of [[lem:tl5-hf-persistence]] uses only the bounds at a point of the statements P(m),
for all m, and gives the claim. ∎

**Theorem {#thm:tl5-hf4}** (Existence close to an explicit background, at level four.) Let ĝ be a background with
u* < −1, κ and κ′ as in [[def:tl5-wg-domains]], g_N smooth characteristic data in the gauge on N⁺ satisfying the
constraints, G^♯ data in the wave gauge for g_N, μ ∈ (0, 1], ϑ ∈ (0, 1/4], z, z̲ and rates a_o, a_i as in
[[def:tl5-hf4-constants]], and suppose:

(a) the quantity η₀ of [[def:tl5-hf4-constants]], computed from the derivatives of G^♯ − ĝ of order at most 4 on N₀,
satisfies η₀ < 𝔰₁;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴);

(c) the constants of [[def:tl5-hf4-constants]] satisfy 𝔯_(w,4) ≤ 1/4, 𝔰_* < 𝔰₁ and the closing condition

    4 A_(w,4) B_(w,4) = 8 (√2 δ_w + 2ε_w + 2ε_M) (S_F + S_M) < 1.                                   {#eq:tl5-hf4-closing}

Then there is a solution g of the reduced problem on D^κ, and Y_σ(g) ≤ 2A_(w,4) for every σ ∈ [1/2, v*]. It is a
G-invariant vacuum metric in the wave gauge, with |g − ĝ|_k̂ < κ_m/2 and 𝔰 ≤ 𝔰_* on D^κ, and the quantity ε of
[[eq:tl5-dn-eps]] for g_σ and ĝ_σ on B ∩ M_σ, B as in [[thm:tl5-dn]], satisfies ε ≤ ε_𝔰 𝔰_*. If moreover the
hypotheses of [[thm:tl5-dn]] hold for this ε, then the metric g̃ that theorem gives on D′ is a smooth G-invariant vacuum
metric of the class in the gauge of [[sec:cone-constraint]], equal to g_N at every point of N ∩ D′.

*Proof.* The proof of [[thm:tl5-hf]] applies with A_(w,4), B_(w,4), [[prop:tl5-hf4-bootstrap]], [[eq:tl5-hf4-h1]],
[[lem:tl5-hf4-persistence]] and [[eq:tl5-hf4-closing]] in place of A_w, B_w, [[prop:tl5-hf-bootstrap]],
[[eq:tl5-hf-h1]], [[lem:tl5-hf-persistence]] and [[eq:tl5-hf-closing]]; if A_(w,4) = 0, then δ_w = ε_w = 0, and ĝ is
the solution as there. The bound for ε is [[eq:tl5-hf-eps]], as |h|, |D̂h| and |D̂²h| are at most 𝔰 at level four
([[def:tl5-hf4-levels]]). ∎

**Remark {#rem:tl5-hf4-level}** (Level four and level six.) The constants of [[thm:tl5-hf4]] are those of
[[thm:tl5-hf]] at N = 4, with the terms S_M, 𝔯_M and ε_M of the products of [[lem:tl5-hf4-mixed]] added. They are
explicit in the jets of ĝ of order at most N + 3 = 7, against 9 at N = 6; they involve the Σ_(j≤4) 7^j = 2801 words of
length at most 4, against 137,257 at N = 6, the derivatives of R̂ic along Γ of order at most 4, against 6, and the
factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2). On N₀ they involve the derivatives of
G^♯ − ĝ of order at most 4, through η₀ and the fluxes in δ_w, and of order 5 in the terms 𝔟 of δ_w, which carry the
factor H; all of these vanish when G^♯ − ĝ vanishes together with its partial derivatives of order at most 4 at the
points of N₀. At the first stage of the problem at 10 l5, by
[[lem:tl5-xt-order]] (c) with m = 5, this holds when (X) holds and the components of ĝ − g′ and their partial
derivatives of order at most 5 vanish at the points of N₀⁺, g′ being the metric of [[thm:tl5-wg-data]] as in
[[sec:tl5-xt]]. By [[lem:tl5-xt-seed-jets]], the partial derivatives of g′ of order at most 3 at those points are the
seed's, and the fourth derivatives in v of its leaf metric differ from the seed's at every point with −1 < x < 1 off
at most one torus {x = c}. So this condition asks the background to carry the derivatives in v of g′ of orders 4 and
5 on N₀⁺, and a background with the seed's jets there does not satisfy it. At level three the face energies give no
bound of |D̂²h| at a point ([[rem:tl5-hf-level]]), which the passage to the double-null gauge needs. As for
[[thm:tl5-hf]] ([[rem:tl5-beyond]]), the hypotheses of [[thm:tl5-hf4]] are established in this paper for no background
at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The level-six section sec:tl5-hf stays as it is (the author's decision of 2026-11-27: level 4 is added beside level 6,
not in its place). Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD f99f4a13 (unchanged at 60527421),
where sec:tl5-hf and sec:tl5-xt are merged; line numbers serve only to find the place. Each new text replaces its old
text as a whole, with the line breaks shown.

*1. Where the section goes.* The section above, from its heading ("The a priori estimate at level four", label
sec:tl5-hf4) through the last line of [[rem:tl5-hf4-level]], is inserted at the end of [[ch:ten-l5]], after the last
line of [[rem:tl5-hf-level]] (line 4609, "H² of a four-dimensional manifold does not embed in L^∞; so they give no
bound of |D̂²h| at a point."), with one blank line before it. It is a sibling of sec:tl5-hf (a "###" heading) and comes
after it. It cites, as they stand, results of sec:tl5-hf (the level-independent ones, and the proofs of
prop:tl5-hf-bootstrap, lem:tl5-hf-persistence and thm:tl5-hf with the replacements it states), of sec:tl5-wg,
sec:tl5-dn and sec:tl5-xt (lem:tl5-xt-order, lem:tl5-xt-seed-jets), and def:tl5-wg-domains, thm:tl5-wg-data,
sec:cone-constraint. It defines the 22 labels listed in the crosswalk rows, none defined elsewhere. No number already
printed changes.

*2. The last sentence of [[rem:tl5-hf-level]] (lines 4608–4609).* Old:

[[lem:tl5-hf-conversions]] (b). The face energies of level 3 control D̂²h only in H² of the four-dimensional faces, and
H² of a four-dimensional manifold does not embed in L^∞; so they give no bound of |D̂²h| at a point.

New:

[[lem:tl5-hf-conversions]] (b). The face energies of level 3 control D̂²h only in H² of the four-dimensional faces, and
H² of a four-dimensional manifold does not embed in L^∞; so they give no bound of |D̂²h| at a point. With another
bound of the products, [[sec:tl5-hf4]] proves the counterpart [[thm:tl5-hf4]] of [[thm:tl5-hf]] at level four, where two
kinds of products have no factor bounded at a point; it bounds them on the faces by a Hölder inequality in mixed norms.

*3. Nothing else changes.* No other text of the chapters changes. In particular the opening paragraph of sec:tl5-hf,
rem:tl5-beyond and lem:tl5-continuation need no change: [[thm:tl5-hf4]] gives (H1), (H2) and (H4) of
[[lem:tl5-continuation]] and reduces (H3) to [[eq:tl5-hf4-closing]], exactly as [[thm:tl5-hf]] does at level six.

### Comparison with level 6

Not chapter text. Formulas are those of the two theorems as written: thm:tl5-hf at N = 6 (Theorem 57.145 in the
assembled paper) and thm:tl5-hf4 (Theorem 57.155). "Computed" marks the numbers I evaluated; everything else is read off
the definitions.

*The closing conditions.*

    level 6:  8 (√2 δ_w + 2ε_w) S_F < 1,                 δ_w, ε_w, S_F of def:tl5-hf-constants at N = 6;
    level 4:  8 (√2 δ_w + 2ε_w + 2ε_M) (S_F + S_M) < 1,   δ_w, ε_w, S_F of the same formulas at N = 4.

The smallness conditions have the same form (𝔯 ≤ 1/4, η₀ < 𝔰₁, 𝔰_* < 𝔰₁), with 𝔯_(w,4) = 𝔯_w + 𝔯_M at level 4.

*Powers of μ.* In def:tl5-hf-constants every level is bounded by the top one: the low quantity 𝔰 through the
unweighted face energy of level N (μ^(−N/2) in S_F and in 𝔰_*), and the high factor through 𝒥₁ (μ^(−N/2) in 𝔞_o, 𝔞_i).
So:

    term                                   level 6        level 4
    S_F, part with 𝔤_N (2Ω̂𝔤_N(2k₁+4)…)     μ^(−6)          μ^(−4)
    S_F, part with ϰ₀ and 𝒞_(·0)            μ^(−3)          μ^(−2)
    S_M (products of lem:tl5-hf4-mixed)     —               μ^(−2)
    𝔰_*, data term 2C_∞ e^(φ/2) A           μ^(−3)          μ^(−2)
    ε_M = μ² ϱ(ϱ + η₀) ∫ m_t                —               μ²
    s_N, 𝔤_N: Σ_(j≤N) μ^j (…)²              j ≤ 6           j ≤ 4

At μ = 10⁻⁴ the leading factor of S_F is 10^24 at level 6 and 10^16 at level 4 (computed): 8 decades in the closing
condition, which is linear in S_F. Against G0b's level-3 scoping, which priced the level weights as μ^(−3/2) (about 6
decades at μ = 10⁻⁴), the level-4 theorem as written costs μ^(−4) (16 decades). The difference is the bookkeeping, not
the level. Deduced, and not part of any proof in the file: for every monomial of level n the two norms used in its bound
(the factor at a point and the factor in the energy, or the two mixed norms) need energies of levels ℓ₁ + ℓ₂ ≤ n + 3,
so a graded count, bounding each factor by the lowest level that controls it and weighting the source of level n by
μ^(n/2), would put at most μ^(−3/2) in front of every quadratic term, at level 4 and at level 6 alike. That needs graded
versions of lem:tl5-hf-linfty and of Step 2 of the bootstrap, which are not written; until then the scoping should
use μ^(−N) for S_F.

*Cross-level couplings and the linear estimate.* The bulk matrix 𝔅_N has size 4(N + 1): 28 at level 6, 20 at level 4.
Its coupling blocks 𝔒_((j,σ),(j′,ϰ)) = √c Ω̂³ μ^((j−j′)/2) ℭ_(jj′ϰ) run over 0 ≤ j′ ≤ j ≤ N: 28 level pairs against 15.
The maps 𝔄_IJ, 𝔔_IJ (hence ℭ_(jj′ϰ), 𝔮_(jj′), α_𝔄, q₁, k₁, k₂, k₃) are built from the jets of ĝ and of Γ of order at
most N + 3 (9 against 7) and from 𝔏-iterates of 𝒦[π^Z] with at most N − 1 Lie derivatives (5 against 3); Λ bounds
ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z], D̂ℒ^B Γ′[π^Z] and ℒ^B R̂ for |B| ≤ N. The rates must be admissible for
(1 − ϑ)⁻¹ 𝔅_N; at level 4 the larger couplings μ^((j−j′)/2) ℭ with j − j′ = 5, 6 are absent.

*Word counts and term counts (computed).*

    quantity                                    level 6       level 4
    words of length ≤ N, Σ_(j≤N) 7^j             137,257       2,801
    words of length N, 7^N                       117,649       2,401
    𝔐 = Σ_(j≤N−3) 7^j (in C_∞, C_(∞,ϱ), C_(∞,0))  400           8
    ordered Bell number F_N in 𝔠_N               4,683         75
    𝔠_N at Λ = 1                                 9.75 × 10^10  4.44 × 10^7
    𝔠_N at Λ = 3                                 8.54 × 10^12  9.64 × 10^8

with 𝔠₀, …, 𝔠₆ = 1.04 × 10², 1.82 × 10³, 4.14 × 10⁴, 1.22 × 10⁶, 4.44 × 10⁷, 1.93 × 10⁹, 9.75 × 10^10 at Λ = 1
(computed from eq:tl5-hf-cn, floating point). 𝔠_n enters 𝔤_N and k₃ (so 𝔰₀) for n ≤ N, and, at level 4, m_t through
[𝔠₄]_t.

*Constants only at level 4 (the products of lem:tl5-hf4-mixed).* m_t = 98 e^(φ(t,v*)/2) [2Ω̂²(1 + c/κ′)^(1/2)]_t
[𝔠₄]_t 𝔪(t) 𝔵_t 𝔶_t, with 𝔵_t, 𝔶_t built from the face suprema of 𝔳^(2r) R⁻³ (r = 2, 3, 4), 𝔳⁴ and 𝔳⁶ on the leaf
S_t, max(1, 𝔴)⁶ R^(3/2), |∂_γ|, |D̂∂_γ|, k₁, k₂ and Λ, and the numbers 𝔭₃ = 11,773, 𝔭₄ = 37,057, 64,680, √602 ≈ 24.5,
789, π√98 ≈ 31.1 and π√686 ≈ 82.3 (computed). These come from counting monomials and from the Cauchy–Schwarz
inequality over words, and are crude; they enter S_M, 𝔯_M and ε_M linearly. C_(S³)² = 1/12 exactly (proved in
lem:tl5-hf-sphere), so 6C_(S³)² = 1/2 in lem:tl5-hf4-face (b).

*Data.* δ_w contains, at level N, the fluxes of Ψ_I, |I| ≤ N, through N₁ and N₀ and the terms 𝔟[Ψ_I], which contain
D̂Ψ_I: derivatives of G^♯ − ĝ of order at most N + 1 (7 against 5), the transverse ones on N₁ being ∂_u-derivatives
of the data computed by transport along N₁. η₀ uses derivatives of order at most N on N₀ (6 against 4).

*Order of vanishing on N₀ and the jets carried by the background.* η₀ and the N₀ terms of δ_w vanish when G^♯ − ĝ
vanishes to order N on N₀ (the 𝔟-terms with H). By lem:tl5-xt-order (c) this holds when ĝ − g′ vanishes to order N + 1
on N₀⁺, and by lem:tl5-xt-seed-jets the background must carry g′'s v-jets of orders 4, …, N + 1: orders 4–7 at level 6
(contact order κ = N + 2 = 8 in N-APP1's terms) against orders 4–5 at level 4 (κ = 6). Any enclosure error of these jets
enters through η₀ < 𝔰₁ and through the N₀ fluxes in δ_w, beside the N₁ data error.

*Derivatives of the residual to enclose.* ε_w uses s_N[2R̂ic], that is ℒ^J(2R̂ic) for |J| ≤ N (6 against 4), and
(1/4)𝔤_N k₂ ϱ with ϱ = sup over D^κ of |ℒ^J(2R̂ic)|, |J| ≤ N − 1 (5 against 3); ϱ also enters 𝔯_w, 𝔰_* and, at level
4, 𝔯_M and ε_M.

*The double-null step.* At both levels ε ≤ ε_𝔰 𝔰_*, |D̂²h| being a low quantity for N ≥ 4. Level 3 cannot give it
(rem:tl5-hf-level), so level 4 is the lowest level for the theorem in this form.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:

    sec:tl5-hf4	paper/reader/proofs/P-HF34.md@PENDING:1	P-HF34, section	new; at the end of ch:ten-l5, after rem:tl5-hf-level, beside sec:tl5-hf (author 2026-11-27: keep level 6, add level 4); the level-4 estimate
    sec:tl5-hf4-products	paper/reader/proofs/P-HF34.md@PENDING:14	P-HF34, section	new
    def:tl5-hf4-levels	paper/reader/proofs/P-HF34.md@PENDING:16	P-HF34, Definition	low and high quantities at N = 4 by the formulas of def:tl5-hf-levels; orders of factors; p_M of the two products without a factor at a point
    eq:tl5-hf4-pm	paper/reader/proofs/P-HF34.md@PENDING:26	P-HF34, display	new
    lem:tl5-hf4-quadratic	paper/reader/proofs/P-HF34.md@PENDING:30	P-HF34, Lemma	Lemma G at level 4: one high factor except D Psi_2 . D Psi_2 and Psi_3 . D^2 Psi_1 at |I| = 4 (R-P-HF level question (d)); order count for persistence
    eq:tl5-hf4-g	paper/reader/proofs/P-HF34.md@PENDING:40	P-HF34, display	new
    lem:tl5-hf4-face	paper/reader/proofs/P-HF34.md@PENDING:71	P-HF34, Lemma	mixed-norm Hoelder on the faces, L2_v Linf_omega against Linf_v L2_omega, with the value at v = 1/2; uses lem:tl5-hf-sphere (C^2 = 1/12) and the trace only
    eq:tl5-hf4-holder	paper/reader/proofs/P-HF34.md@PENDING:95	P-HF34, display	new
    lem:tl5-hf4-linfty	paper/reader/proofs/P-HF34.md@PENDING:129	P-HF34, Lemma	lem:tl5-hf-linfty holds at N = 4 (it uses Lemma G only below the top level); pointwise recovery bound M2
    eq:tl5-hf4-m2	paper/reader/proofs/P-HF34.md@PENDING:134	P-HF34, display	new
    lem:tl5-hf4-mixed	paper/reader/proofs/P-HF34.md@PENDING:142	P-HF34, Lemma	face bound of p_M with explicit constants x_t, y_t
    eq:tl5-hf4-mixed	paper/reader/proofs/P-HF34.md@PENDING:156	P-HF34, display	new
    sec:tl5-hf4-bootstrap	paper/reader/proofs/P-HF34.md@PENDING:192	P-HF34, section	new
    def:tl5-hf4-constants	paper/reader/proofs/P-HF34.md@PENDING:194	P-HF34, Definition	constants of def:tl5-hf-constants at N = 4 plus S_M, r_M, eps_M; A_(w,4) = sqrt2 delta_w + 2 eps_(w,4), B_(w,4) = 2 S_(F,4)
    eq:tl5-hf4-constants	paper/reader/proofs/P-HF34.md@PENDING:206	P-HF34, display	new
    prop:tl5-hf4-bootstrap	paper/reader/proofs/P-HF34.md@PENDING:216	P-HF34, Proposition	(H1) at level 4: proof of prop:tl5-hf-bootstrap with the mixed term added in Step 2
    eq:tl5-hf4-smallness	paper/reader/proofs/P-HF34.md@PENDING:219	P-HF34, display	new
    eq:tl5-hf4-h1	paper/reader/proofs/P-HF34.md@PENDING:224	P-HF34, display	new
    lem:tl5-hf4-persistence	paper/reader/proofs/P-HF34.md@PENDING:261	P-HF34, Lemma	(H2) from level 4, qualitative; face-norm induction with the mixed Hoelder at m = 5, 6; N0 fluxes and traces carried as data (R-P-HF M2 respected)
    thm:tl5-hf4	paper/reader/proofs/P-HF34.md@PENDING:350	P-HF34, Theorem	thm:tl5-hf at level 4; (a) eta0 < s1 (M1 form), N0 flux in delta_w; double-null step via thm:tl5-dn as at level 6
    eq:tl5-hf4-closing	paper/reader/proofs/P-HF34.md@PENDING:362	P-HF34, display	closing condition at level 4: 8 (sqrt2 delta_w + 2 eps_w + 2 eps_M)(S_F + S_M) < 1
    rem:tl5-hf4-level	paper/reader/proofs/P-HF34.md@PENDING:376	P-HF34, Remark	level 4 against level 6 (jets, words, residual derivatives, mu powers); background carries the v-jets 4..5 of g' on N0+ (lem:tl5-xt-order, lem:tl5-xt-seed-jets)

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hf-level, add "; points to sec:tl5-hf4,
the level-4 version (P-HF34 item 2)".
