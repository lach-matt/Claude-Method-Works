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
D^κ_s, h := g − ĝ, t ∈ [−10, u*] and b ∈ [1/2, s] with Σ := Σ₁(t, b) not empty, and suppose that 𝔰 ≤ 𝔰₀ on Q(t, b),
with 𝔰₀ as in [[lem:tl5-hf4-linfty]]. Let ϱ ≥ max_(|J|≤3) |ℒ^J(2R̂ic)| on Q(t, b), and η₀ ≥ max(𝔰, |Ψ_C| (|C| ≤ 4),
|D̂Ψ_C| (|C| ≤ 3)) on N₀ ∩ Q(t, b). With the notation of [[lem:tl5-hf4-face]], 𝒥₁, k₁ and k₂ as in [[lem:tl5-hf-linfty]]
and 𝔨₂ := (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²), put 𝔍 := ‖𝒥₁‖_Σ and

    λ_t := 2([k₁]_t + 1),      ς_t := 2[k₂]_t (∫_(Σ₁(t,v*)) dμ dτ₂/(1 − κκ′))^(1/2),
    𝔵_t := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ]_t²),
               (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),
    𝔶_t := max(𝔱₃(t)^(1/2) (1 + 7λ_t), 7 𝔱₃(t)^(1/2) ς_t, 𝔱₂(t)^(1/2), π (98 [𝔳⁶]_t)^(1/2), π (686 [𝔳⁴]_t)^(1/2)).

Then

    ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔵_t 𝔶_t (𝔍 + ϱ) (𝔍 + ϱ + η₀),
    𝔍² ≤ [𝔨₂]_t Σ_(|I|≤4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                                      {#eq:tl5-hf4-mixed}

*Proof.* On Σ, |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) = 𝔨₂ (1 − κκ′) ε₁[Ψ_C] by [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], which gives the second inequality. By [[eq:tl5-hf4-m2]] at the points of Σ, with e^(−φ) ≤ 1
and Σ ⊂ Σ₁(t, v*), ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ.

The function 𝔭_M² is a sum of products |X|² |Y|² over the pairs (X, Y) := (D̂Ψ_B, D̂Ψ_(B′)), |B| = |B′| = 2, of ranks
3 and 3, and (X, Y) := (D̂²Ψ_Z, Ψ_B), |B| = 3, Z ∈ Γ, of ranks 4 and 2. So ‖𝔭_M‖_Σ² is the sum of ‖|X| |Y|‖_Σ² over
these pairs, and by [[eq:tl5-hf4-holder]] it is at most e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²), with

    X₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(2,∞)²,   Y₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(∞,2)²,
    X₂² := Σ_(Z∈Γ) ⟦D̂²Ψ_Z⟧_(2,∞)²,   Y₂² := Σ_(|B|=3) ⟦Ψ_B⟧_(∞,2)².

*X₁.* By (ii) of the proof of [[lem:tl5-hf-quadratic]], applied with Ψ_B in place of h, for a word J of rotations with
|J| ≤ 2, ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′ with R′ a sum of at most m′_(|J|) monomials, m′₀ = 0, m′₁ = 2, m′₂ = 6, each the
contraction of a coefficient of norm at most Λ with some Ψ_C, |C| ≤ 3; so |R′| ≤ m′_(|J|) Λ 𝒥₁. The words JB are
distinct and of length at most 4, there are 49 words B of length 2, and Σ_(|J|≤2) m′_(|J|)² = 6 · 4 + 36 · 36 = 1320;
so Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥₁² + 2 · 49 · 1320 Λ² 𝒥₁² at every point, and by [[lem:tl5-hf4-face]] (b) with r = 3,
X₁ ≤ (𝔭₃ 𝔵₃(t) (1 + 64680 [Λ]_t²))^(1/2) 𝔍.

*X₂.* By (iii) of that proof, applied with Ψ_Z in place of h, ℒ^J D̂²Ψ_Z = D̂²Ψ_(JZ) + R with R a sum of at most m_(|J|)
monomials, m₁ = 7, m₂ = 35, each with at most two background factors of norm at most Λ and one solution factor D̂Ψ_C or
Ψ_C with |C| ≤ 2; so |R| ≤ m_(|J|) Λ² 𝒥₁, while |D̂²Ψ_(JZ)| ≤ M₂ as |JZ| ≤ 3. There are 7 fields Z and 43 words J, and
Σ_(|J|≤2) m_(|J|)² = 6 · 49 + 36 · 35² = 44394; so Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M₂² + 621516 Λ⁴ 𝒥₁², and by
[[lem:tl5-hf4-face]] (b) with r = 4 and √621516 < 789, X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 ‖M₂‖_Σ + 789 [Λ]_t² 𝔍).

*Y₁ and Y₂.* On S_t ⊂ N₀ ∩ Q(t, b), |D̂Ψ_B| ≤ η₀ for |B| ≤ 3 and |Ψ_B| ≤ η₀ for |B| ≤ 4, and ∫_(S_t) dω = 2π². By
[[lem:tl5-hf4-face]] (a) with r = 3 and r = 2, as Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M₂² and Σ_(|B|=2) |D̂Ψ_B|² ≤ 𝒥₁²,

    Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍² + 49 ‖M₂‖_Σ²),      Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍²,

there being 343 words of length 3.

With ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ these give X_i ≤ 𝔵_t (𝔍 + ϱ) and Y_i ≤ 𝔶_t (𝔍 + ϱ + η₀) for i = 1, 2, and (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ X₁ Y₁ + X₂ Y₂ gives the first inequality. ∎

#### The bootstrap at level four {#sec:tl5-hf4-bootstrap}

**Definition {#def:tl5-hf4-constants}** (The constants at level four.) Fix μ ∈ (0, 1], weights z, z̲, admissible rates
a_o, a_i for (𝔅₄, E_o⁴, E_i⁴) and φ as in [[prop:tl5-hf-linear]], and let Y_σ be the norm of [[def:tl5-hf-norm]], whose
definition and properties do not use N ≥ 5, with N = 4. Let G^♯ be data in the wave gauge, and let δ_w, ε_w, 𝔤₄, ϰ₀,
𝔞_o, 𝔞_i, S_F, 𝔯_w, 𝔰₀, 𝔰_θ and 𝔰₁ be given by the formulas of [[def:tl5-hf-constants]] with N = 4, the quantities of
[[def:tl5-hf4-levels]] and the constants of [[lem:tl5-hf4-linfty]], ϱ and η₀ being those of [[lem:tl5-hf-linfty]] for a
point p with τ₁(p) = u*, τ₂(p) = v*. Put, with the notation of [[lem:tl5-hf4-face]] and [[lem:tl5-hf4-mixed]] and with
[𝔠₄]_t the number 𝔠₄ formed with [Λ]_t in place of Λ,

    m_t := 98 e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t [𝔠₄]_t 𝔪(t) 𝔵_t 𝔶_t,
    S_M := μ^(−2) ∫_(−10)^(u*) m_t [𝔨₂]_t dt,      𝔯_M := ∫_(−10)^(u*) m_t [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_M := μ² ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t dt,
    S_(F,4) := S_F + S_M,      𝔯_(w,4) := 𝔯_w + 𝔯_M,      ε_(w,4) := ε_w + ε_M,
    A_(w,4) := √2 δ_w + 2ε_(w,4),      B_(w,4) := 2 S_(F,4),                                             {#eq:tl5-hf4-constants}

and let 𝔰_* be given by the formula of [[def:tl5-hf-constants]] with N = 4 and A_(w,4) in place of A_w:

    𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−2) e^(φ(p)/2) A_(w,4) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).

As in [[def:tl5-hf-constants]], δ_w contains the fluxes of the Ψ_I and of 𝔟[Ψ_I], |I| ≤ 4, through N₀ and through N₁,
and η₀ and these fluxes are computed from the derivatives of G^♯ − ĝ on N of order at most 4, and of order 5 in the
terms 𝔟 on N₁.

**Proposition {#prop:tl5-hf4-bootstrap}** (The a priori estimate at level four.) In the setting of
[[def:tl5-hf4-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴) and that

    𝔯_(w,4) ≤ 1/4,      η₀ < 𝔰₁,      𝔰_* < 𝔰₁.                                                    {#eq:tl5-hf4-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_(w,4) for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_* on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_(w,4) + B_(w,4) Y_s(g)².                                                                {#eq:tl5-hf4-h1}

*Proof.* Step 1 of the proof of [[prop:tl5-hf-bootstrap]] holds as written with N = 4, A_(w,4) in place of A_w and
[[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]]: it gives 𝔰 ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, |h|_k̂ < κ_m/2 and
θ_H ≤ ϑ.

Step 2 of that proof holds with N = 4, [[lem:tl5-hf4-quadratic]] and [[lem:tl5-hf4-linfty]] in place of
[[lem:tl5-hf-quadratic]] and [[lem:tl5-hf-linfty]], except at one place: |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ 3, as
there, but for |I| = 4 only |𝔑_I − 𝔑^M_I| ≤ 𝔠₄ 𝔰 𝔧. With 𝔑_I − 𝔑^M_I in place of 𝔑_I that step goes through, and the
terms 𝔑^M_I add to the bulk of the weighted sum over I, by the proof of the second inequality of
[[lem:tl5-hf-pointwise]], at most

    ∫_(Q(a′,b′)) e^(−φ) μ⁴ Σ_(|I|=4) 2Ω̂² |𝔑^M_I| (√e_o[Ψ_I] + √c √e_i[Ψ_I]) dμ du dv.

By the Cauchy–Schwarz inequality, √e_o + √c √e_i ≤ (1 + c/κ′)^(1/2) (e_o + κ′ e_i)^(1/2) = (1 + c/κ′)^(1/2) ((1 −
κκ′) ε₁)^(1/2). Foliate Q(a′, b′) by the faces Σ₁(t, b′), −10 ≤ t ≤ a′, with du dv = dτ₁ dτ₂/(1 − κκ′), and apply the
Cauchy–Schwarz inequality on each nonempty face Σ := Σ₁(t, b′) and over I: the term is at most

    ∫_(−10)^(a′) [2Ω̂² (1 + c/κ′)^(1/2)]_t μ⁴ (Σ_(|I|=4) ‖𝔑^M_I‖_Σ²)^(1/2) (Σ_(|I|=4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂)^(1/2) dt.

By [[eq:tl5-hf4-g]], ‖𝔑^M_I‖_Σ ≤ [𝔠₄]_t ‖𝔭_M‖_Σ, and there are 7⁴ = 49² words of length 4. The last factor is at most
μ^(−2) Y_s. By Step 1, 𝔰 ≤ 𝔰₀ on D^κ_s, so [[lem:tl5-hf4-mixed]] applies, with the ϱ and η₀ of
[[def:tl5-hf4-constants]], and with 𝔍² ≤ [𝔨₂]_t μ^(−4) Y_s², as Σ_(|I|≤4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂ ≤ μ^(−4) Y_s². With
e^(φ(t,b′)) ≤ e^(φ(t,v*)), the term is at most

    ∫_(−10)^(u*) m_t μ² (𝔍 + ϱ)(𝔍 + ϱ + η₀) Y_s dt ≤ S_M Y_s³ + 𝔯_M Y_s² + ε_M Y_s,

by μ²(𝔍 + ϱ)(𝔍 + ϱ + η₀) ≤ [𝔨₂]_t μ^(−2) Y_s² + [𝔨₂]_t^(1/2) (2ϱ + η₀) Y_s + μ² ϱ (ϱ + η₀).

Step 3 of that proof, with this term added, gives for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s ε_(w,4) + 𝔯_(w,4) Y_s² + S_(F,4) Y_s³,

and, as there, with ϑ ≤ 1/4 and 𝔯_(w,4) ≤ 1/4, Y_s² ≤ 2δ_w² + 2Y_s ε_(w,4) + 2S_(F,4) Y_s³, whence
[[eq:tl5-hf4-h1]]. ∎

