### A weight in the transport along the curves, and the parts with ϱ over the second derivatives {#sec:tl5-hfe}

This section makes two changes. First, the Sobolev inequalities on the faces, and at level four the bound along the
curves in the products with no factor at a point, carry integrals over the leaves from the initial leaf along the curves
γ_ω; the derivative 2⟨B, ℒ_(∂_γ)B⟩₀ of |B|₀² along a curve is bounded there by |B|₀² + |ℒ_(∂_γ)B|₀². We bound it by
𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² with a positive function 𝔲, one for the steps of zeroth order, one for those of first order
and, at level four, one for the products with no factor at a point ([[lem:tl5-hfe-face]]). A bracket 𝔲X + 𝔲⁻¹Y with X,
Y > 0 has the least value 2(XY)^(1/2), at 𝔲 = (Y/X)^(1/2), against X + Y for 𝔲 = 1. In the bracket of the first-order
constant, X = (μ^(1/2) + ϖ′^(1/2))² comes from the first derivatives ℒ^J D̂Ψ_B, whose leading terms D̂Ψ_(JB) the weights
of the step bound with the factor μ^(1/2) over their energies, and Y from their derivatives D̂ℒ^J D̂Ψ_B, which carry the
recovery constant. Second, in the products with a factor at a point the part with ϱ comes only from the monomials whose
factor in the energies is a second derivative D̂²Ψ_C, through the residual of its recovery. These are among the
monomials of H₁^(λσ) D̂_λD̂_σh and H₂^(λσ) D̂_λD̂_σh in which the factor D̂²h gives its leading term, and a number 𝔠^ϱ_n
counts the latter in place of 𝔠^♮_n ([[lem:tl5-hfe-rho]]); when all Λ_k and Λ^R_k vanish, 𝔠^ϱ_n + 1 = 2^n against
𝔠^♮_n + 1 = 81 · 2^n, up to terms with the factor 𝔰_♭. Both changes enter the constants with index l
([[def:tl5-hfe-constants]], [[thm:tl5-hfe]]). The closing condition is [[eq:tl5-hfe-closing]]; with the weights equal to
1 every new constant is at most the one it replaces, and the earlier closing conditions remain valid. The notation is
that of [[sec:tl5-hfd]] and, for N = 4, of [[sec:tl5-hfu]].

**Lemma {#lem:tl5-hfe-face}** (The transport along the curves with a weight.) Let 𝔲 be a positive continuous function on
D̄, p ∈ D^κ, a := τ₁(p), b := τ₂(p), S_a, the curves γ_ω, ∂_γ and 𝔨₁ as in [[lem:tl5-hf-sobolev]], h₀, 𝔳₀ and 𝔴₀ as in
[[lem:tl5-hft-face]], and 𝔶₀, 𝔶₁ > 0, 𝔶₂ := 1 and C_(E,0)(𝔶) as in [[lem:tl5-hfd-leaf]].

(a) For every tensor field A of rank r on Q(a, b) of the regularity of [[lem:tl5-hf-sobolev]], the sums being over the
words J of length at most two in the six rotations,

    |A(p)|² ≤ C_(E,0)(𝔶)² 𝔴₀(p)^(2r) (Σ_(|J|≤2) 𝔶_(|J|) ∫_(Σ₁(a,b)) 𝔳₀^(2r) R⁻³ ((𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²) |ℒ^J A|²
              + 2𝔲⁻¹ |∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′)
              + sup_(S_a) 𝔳₀^(2r) Σ_(|J|≤2) 𝔶_(|J|) ∫_(S_a) |ℒ^J A|² dω).                             {#eq:tl5-hfe-face}

(b) For every symmetric 2-tensor field A as in [[lem:tl5-hf-sobolev]], the inequality of that lemma, in the form of
[[lem:tl5-hft-face]] (b) with the weights 𝔶_(|J|) on its sums over J and with C_(E,0)(𝔶)² in place of 6C_(E,2)², holds
with (𝔲 + 8𝔲⁻¹ |D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔲⁻¹ 𝔨₁ in place of (1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁ in C_S^E, C_(S,0)^E being
formed with C_(E,0)(𝔶)² in place of 6C_(E,2)² as well.

(c) In the setting of [[lem:tl5-hfu-face]], with [·]_t the supremum over Σ₁(t, v*), the second inequality of
[[eq:tl5-hfu-face]] holds with 𝔱_(r,0)(t; 𝔲) := [𝔳₀^(2r) R⁻³ (𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²)]_t and 𝔱_(r,1)(t; 𝔲) := [2𝔲⁻¹
𝔳₀^(2r) R⁻³ |∂_γ|²]_t in place of 𝔱_(r,0)(t) and 𝔱_(r,1)(t).

For 𝔲 = 1 these are the forms of [[eq:tl5-hf-cs-r]], of [[lem:tl5-hf-sobolev]] and of [[eq:tl5-hfu-face]] that
[[lem:tl5-hfp-abs]] (a), [[lem:tl5-hfu-face]] and [[lem:tl5-hfd-leaf]] give.

*Proof.* (a) Let v_p be the value of v at p. The points γ_ω(v_p), ω ∈ S³, fill the leaf of p, and the points γ_ω(1/2)
fill S_a. For a word J put g_J(v) := ∫_(S³) |ℒ^J A|₀²(γ_ω(v)) dω. By [[eq:tl5-hfd-leaf]] on the leaf of p, with the
weights 𝔶_(|J|), and |A| ≤ 𝔴₀^r |A|₀ ([[lem:tl5-hft-face]]),

    |A(p)|² ≤ 𝔴₀(p)^(2r) C_(E,0)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) g_J(v_p).

As in the proof of [[lem:tl5-hft-face]], h₀ has constant coefficients, so ℒ_(∂_γ) h₀ = 0 and along each curve, with B :=
ℒ^J A, (d/dv) |B|₀² = 2⟨B, ℒ_(∂_γ)B⟩₀, which is at most 𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² at each point, by 2xy ≤ 𝔲x² + 𝔲⁻¹y²
for x, y ≥ 0. Integrating over ω ∈ S³ and over v from 1/2 to v_p, with dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face, gives
g_J(v_p) ≤ g_J(1/2) + ∫_(Σ₁(a,b)) R⁻³ (𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀²) dμ dτ₂/(1 − κκ′), and g_J(1/2) ≤ sup_(S_a) 𝔳₀^(2r)
∫_(S_a) |ℒ^J A|² dω, as |·|₀ ≤ 𝔳₀^r |·|. As D̂ is torsion free, ℒ_(∂_γ)B = D̂_(∂_γ)B + Σ_(i=1)^r B(…, D̂∂_γ ·, …),
so |ℒ_(∂_γ)B| ≤ |∂_γ| |D̂B| + r |D̂∂_γ| |B| ([[lem:tl5-hf4-face]]), and with (x + y)² ≤ 2x² + 2y²

    𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² ≤ 𝔳₀^(2r) ((𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²) |B|² + 2𝔲⁻¹ |∂_γ|² |D̂B|²).

Summing over J with the weights gives [[eq:tl5-hfe-face]]. (b) Let r = 2 and B := ℒ^J A. As in (a), the left side is at
most 𝔴₀(p)⁴ C_(E,0)(𝔶)² Σ_J 𝔶_(|J|) g_J(v_p), and g_J(v_p) is at most g_J(1/2) plus the integral of R⁻³ 𝔳₀⁴ ((𝔲 +
8𝔲⁻¹ |D̂∂_γ|²) |B|² + 2𝔲⁻¹ |D̂_(∂_γ)B|²) over the face with dμ dτ₂/(1 − κκ′), by |ℒ_(∂_γ)B| ≤ |D̂_(∂_γ)B| + 2|D̂∂_γ| |B|
in place of the bound through |D̂B|. In the proof of [[lem:tl5-hf-sobolev]], |D̂_(∂_γ)B|² ≤ 𝔨₁ (e_o[B] + κ′ e_i[B])
and |B|² ≤ (e_o[B] + κ′ e_i[B])/(2Ω̂² z̲) at the points of the face, and (e_o + κ′ e_i)/(1 − κκ′) = ε₁; bounding the
coefficient of ε₁[B] by its supremum over the face gives (b). (c) In the proof of [[lem:tl5-hfu-face]], the second
inequality comes from (d/dv)|A|₀² = 2⟨A, ℒ_(∂_γ)A⟩₀ ≤ |A|₀² + |ℒ_(∂_γ)A|₀² along the curves, integrated as in
[[lem:tl5-hf4-face]] (a) with the factors e^(−φ). With 𝔲 |A|₀² + 𝔲⁻¹ |ℒ_(∂_γ)A|₀² in its place, the pointwise bound of
the proof of (a) with B := A, and the suprema over Σ₁(t, v*) of the two coefficients times 𝔳₀^(2r) R⁻³, give 𝔱_(r,0)(t;
𝔲) and 𝔱_(r,1)(t; 𝔲); the rest of that proof holds as written. For 𝔲 = 1 every step is that of the proofs cited. ∎

**Lemma {#lem:tl5-hfe-rho}** (The parts with ϱ, counted over the second derivatives.) In the setting of
[[lem:tl5-hfs-quadratic]], for ν′ ∈ (0, 1] let λ^♮_k(ν′) and b^♮_g(k, ν′) be λ^♮_k and b^♮_g(k) of
[[def:tl5-hfs-bounds]] formed with ν′^(a/2) Λ_a in place of Λ_a for every a, so that λ^♮_k(ν′) = ν′^(k/2) λ^♮_k and
b^♮_g(0, ν′) = 𝔤₀, and put, for 0 ≤ n ≤ N, with Σ^m_n as in [[def:tl5-hfg-graded]],

    𝔠^ϱ_n(ν′) := Σ⁴_n λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1
                 + 𝔰_♭ (Σ⁶_n b^♮_g(k₁, ν′) λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀).                            {#eq:tl5-hfe-rho}

(a) In the second expansion of [[lem:tl5-hfg-quadratic]], with n := |I|, every monomial of ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I
with a solution factor D̂²Ψ_C is a monomial of ℒ^I (H₁^(λσ) D̂_λD̂_σh) or of ℒ^I (H₂^(λσ) D̂_λD̂_σh) in which the Lie
derivative ℒ^K D̂²h of the factor D̂²h gives its term D̂²Ψ_K; and the sum of ν ν′^(b/2) 𝔰(p)^(q−2) over these monomials,
with the notation of [[eq:tl5-hfs-sum]], is at most 𝔠^ϱ_n(ν′).

(b) In [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and [[lem:tl5-hfq-theta]], and so in the parts 𝔡_n and 𝔡′_(j′)
of [[eq:tl5-hfd-words]], the terms with ϱ(p) hold with 𝔠^ϱ_n and 𝔠^ϱ_(|J|) in place of 𝔠^♮_n and 𝔠^♮_(|J|), at the same
argument: 1 in [[lem:tl5-hfs-products]], μ in [[lem:tl5-hft-products]] and ν in [[lem:tl5-hfq-theta]].

Moreover 0 ≤ 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′) − 𝔠^D_n(ν′), with 𝔠^D_n of [[lem:tl5-hfd-words]].

*Proof.* (a) The second expansion writes ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I as the sum of ℒ^I Q − H₁^(αβ) D̂_αD̂_βΨ_I and ℒ^I
R₃ − H₂^(αβ) D̂_αD̂_βΨ_I, and expands ℒ^I of each term of Q and R₃ by Leibniz's rule over its factors: ℒ^J h = Ψ_J; ℒ^J
D̂h, ℒ^J D̂²h and ℒ^J g⁻¹ by (ii), (iii) and (iv) of the proof of [[lem:tl5-hf-quadratic]]; ℒ^J R̂ and ℒ^K ĝ⁻¹ as
background factors. By (ii) the solution factors of the monomials of ℒ^J D̂h are D̂Ψ_J and factors Ψ_B; by (iv) and
[[lem:tl5-hfs-quadratic]] (a) the monomials of ℒ^J g⁻¹ have, besides factors g⁻¹ and background factors, solution
factors Ψ_B only; and by (iii), or [[lem:tl5-hfs-quadratic]] (a), ℒ^J D̂²h is D̂²Ψ_J, with the coefficient 1, plus
monomials whose solution factor is D̂Ψ_B or Ψ_B. So a solution factor D̂²Ψ_C comes only from a factor D̂²h, as its term
D̂²Ψ_K. The terms of Q and R₃ with a factor D̂²h are H₁^(λσ) D̂_λD̂_σh and H₂^(λσ) D̂_λD̂_σh; the others, 2𝔠(H₁)h,
2𝔠(H₂)h, 2𝔮̂ and 2𝔮 − 2𝔮̂, have the factors h, R̂, D̂h, g⁻¹, ĝ⁻¹ and H = −g⁻¹ h ĝ⁻¹. This is the first claim. In H₁^(λσ)
D̂_λD̂_σh, with the factors ĝ⁻¹, h, ĝ⁻¹, D̂²h carrying k₁, …, k₄ letters, the monomial with the term D̂²Ψ_(I₄) has q =
2, its factors ℒ^(I₁) ĝ⁻¹ and ℒ^(I₃) ĝ⁻¹ are background factors of norms at most λ^♮_(k₁) and λ^♮_(k₃), carrying k₁ and
k₃ letters, and the factors ĝ⁻¹ that carry no letter count λ^♮₀ = 1, as in the proof of [[lem:tl5-hfg-quadratic]]; so ν
ν′^(b/2) ≤ λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′), b = k₁ + k₃. Summing over the n!/(k₁! ⋯ k₄!) distributions of the letters for each
k, less the subtracted term H₁^(αβ) D̂_αD̂_βΨ_I, which is the one with k = (0, 0, 0, n) and the value 1, gives Σ⁴_n
λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1. In H₂^(λσ) D̂_λD̂_σh, with the factors g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h, the monomials of ℒ^(I₁)
g⁻¹ have, by [[lem:tl5-hfs-quadratic]] (a), background norms of total at most b^♮_g(k₁), a product of bounds Λ_a, each
for a factor carrying a letters, and of numbers that carry no letter, so at most b^♮_g(k₁, ν′) once each Λ_a is
multiplied by ν′^(a/2); the monomials have q ≥ 3, so 𝔰(p)^(q−2) ≤ 𝔰_♭; the factors ℒ^(I₃) ĝ⁻¹ and ℒ^(I₅) ĝ⁻¹ count
λ^♮_(k₃)(ν′) and λ^♮_(k₅)(ν′) as in H₁; and the subtracted term H₂^(αβ) D̂_αD̂_βΨ_I is the one with all letters on D̂²h,
of value b^♮_g(0) = 𝔤₀. This gives 𝔰_♭ (Σ⁶_n b^♮_g(k₁, ν′) λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀), and adding the two sums
gives the bound.

(b) In the proofs of these lemmas a monomial of 𝔑^L_I has a term with ϱ(p) only if its factor Φ₂ is a second derivative
D̂²Ψ_C, bounded by [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] or the bound of M_g^(j) of [[lem:tl5-hft-small]] (b); otherwise
Φ₂ is bounded by 𝔨_B 𝒥_g, as in the proof of [[lem:tl5-hfs-products]]. In each proof the term with ϱ(p) of such a
monomial is at most ν ν′^(b/2) 𝔰^(q−2) times a number that does not depend on the monomial, with ν′ = 1, μ or ν, namely
μ^(n/2) 2k₂ 𝔰 ϱ(p), μ^(−1/2) 2k₂ 𝔰 ϱ(p) or μ^((1−θ)n/2) ν^(−1/2) 2k₂ 𝔰 ϱ(p), and those proofs sum ν ν′^(b/2) 𝔰^(q−2)
over all the monomials by [[eq:tl5-hfs-sum]]. By (a) the sum over the monomials with a factor D̂²Ψ_C is at most
𝔠^ϱ_n(ν′), which gives the first inequality of each lemma with 𝔠^ϱ_n in its term with ϱ(p); the second follows from the
first for J and from the term H^(αβ) D̂_αD̂_βΨ_J, as there. The parts 𝔡_n and 𝔡′_(j′) of [[eq:tl5-hfd-words]] are those
of the lemma in use, so they take these forms.

For the last claim, the term with k = (0, 0, 0, n) of the first sum of [[eq:tl5-hfe-rho]] is 1 and that of the second
with all letters on the sixth factor is 𝔤₀, the other terms being nonnegative, so 𝔠^ϱ_n(ν′) ≥ 0. In 𝔠^♮_n(ν′) the
numbers β₁^♮ and β₂^♮ formed with the ν′^(a/2) Λ_a are at least 1 and the other sums of [[eq:tl5-hfs-cn]] are
nonnegative, so 𝔠^(2♮)_n(ν′) ≥ Σ⁴_n λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1 + 𝔠^D_n(ν′) and 𝔠^(3♮)_n(ν′) ≥ Σ⁶_n b^♮_g(k₁, ν′)
λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀, which gives 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′) − 𝔠^D_n(ν′). ∎

**Definition {#def:tl5-hfe-constants}** (The constants with index l.) Let 𝔲₀, 𝔲₁ and, for N = 4, 𝔲_M be positive
continuous functions on D̄, and let the setting be that of [[def:tl5-hfd-constants]], with its constants with index d.
For p ∈ D^κ, a := τ₁(p) and b := τ₂(p), with the suprema over Σ₁(a, b), a family 𝔚 and the numbers 𝔩_D(𝔚), 𝔩_J(𝔚), ϖ′,
𝔨₂ and 𝔨₂′ as in [[def:tl5-hfp-constants]], 𝔗(𝔶) that of the lemma in use, and 𝔱_(3,0)(t; 𝔲) and 𝔱_(3,1)(t; 𝔲) as in
[[lem:tl5-hfe-face]] (c), put

    C_S^l(p)² := C_(E,0)(𝔶)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ ((𝔲₀ + 8𝔲₀⁻¹ |D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁),
    C₁^(U,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) (μ^(1/2) + ϖ′^(1/2))²
                    + 2𝔲₁⁻¹ |∂_γ|² (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^(D,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂′ (μ (𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) + 2𝔲₁⁻¹ |∂_γ|² 𝔩_D(𝔚)²),
    C₁^(J,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) ϖ′
                    + 2𝔲₁⁻¹ |∂_γ|² (𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^l(𝔚) := min(C₁^(U,l)(𝔚), C₁^(D,l)(𝔚) + C₁^(J,l)(𝔚)),
    C_(1,ϱ)^l(p)² := 43 C_(E,0)(𝔶)² 𝔗(𝔶)² 𝔴₀(p)⁶ sup (𝔳₀⁶ R⁻³ 2𝔲₁⁻¹ |∂_γ|² (k₂^z)²/(1 − 𝔵^z)²)
                    · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),
    𝔜^l_(1,t) := (μ 𝔱_(3,0)(t; 𝔲_M) + 𝔱_(3,1)(t; 𝔲_M) [𝔩(𝔙₂)]_t²)^(1/2),
    𝔜′^l_(1,t) := 7 (μ/ν)^(3/2) 𝔱_(3,1)(t; 𝔲_M)^(1/2) ς_t,                                       {#eq:tl5-hfe-constants}

and let C₁^l be the largest of the C₁^l({B}), |B| ≤ N − 3, and, for N = 4, C₁^(Γ,l) := C₁^l(Γ). The constants with index
l are the constants with index d formed with C_S^l, C₁^l(𝔚), C₁^l, C₁^(Γ,l) and C_(1,ϱ)^l in place of C_S^p, C₁(𝔚),
C₁^p, C₁^Γ and C_(1,ϱ)^p in their forms with index d, wherever these enter, among them 𝔐_p^(m), 𝔨_rec^p, 𝔨_rec^(ϱ,p),
C_P^v, C_(P,ϱ)^v, C_(∞,μ)^(m) and C_((∞,ϱ),μ)^(m) with their forms, 𝔎, 𝔎_ϱ, 𝔎^D and 𝔎^D_ϱ; and, for N = 4, with
𝔜^l_(1,t) and 𝔜′^l_(1,t) in place of 𝔜^u_(1,t) and 𝔜′^u_(1,t) in S_M^u and 𝔯_M^u. With 𝔠^ϱ as in [[lem:tl5-hfe-rho]] put

    𝔤^l_(ϱ,s) := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(1) + 1))²)^(1/2),
    𝔤^l_(ϱ,t) := μ^(−1/2) (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(μ) + 1))²)^(1/2),
    𝔤^l_(ϱ,q) := ν^(−1/2) (Σ_(j≤4) (Σ_(j′≤j) μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(ν) + 1))²)^(1/2),

and let 𝔤_ϱ^l be 𝔤^l_(ϱ,s) for N ≥ 6 with option (a) of [[def:tl5-hft-constants]], 𝔤^l_(ϱ,t) with option (b), and
min(𝔤^l_(ϱ,q), 𝔤^l_(ϱ,t)) for N = 4, with θ and ν = μ^θ of [[def:tl5-hfq-constants]]. Let S_F^l, S_M^l, ε_M^l and 𝔯^l be
S_F^d, S_M^d, ε_M^d and 𝔯^d formed with the constants with index l (S_M^l = ε_M^l = 0 for N ≥ 6), and for N = 4 let
𝔯_M^l be 𝔯_M^u so formed, the part of 𝔯^l with the products with no factor at a point; put

    ε^l := 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^l k₂^z ϱ],      η_l := 1 − max(ϑ₁, ϑ₂) − 𝔯^l,
    A_l := η_l^(−1/2) δ_w + η_l⁻¹ (ε^l + ε_M^l),      B_l := η_l⁻¹ (S_F^l + S_M^l),

and let 𝔰_*^l be 𝔰_*^d formed with the constants with index l and with A_l in place of A_d.

**Theorem {#thm:tl5-hfe}** (Existence with a weight in the transport along the curves and the parts with ϱ over the
second derivatives.) In the setting of [[thm:tl5-hfd]], let 𝔲₀, 𝔲₁ and, for N = 4, 𝔲_M be positive continuous functions
on D̄, and the constants with index l be those of [[def:tl5-hfe-constants]]. Suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 −
ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_l > 0, 𝔰_*^l < 𝔰₁^v and the closing condition

    4 A_l B_l = 4 η_l^(−3/2) (δ_w + η_l^(−1/2) (ε^l + ε_M^l)) (S_F^l + S_M^l) < 1.                 {#eq:tl5-hfe-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_l and 𝔰_*^l in place of A_w (or
A_(w,4)) and 𝔰_*. For 𝔲₀ = 𝔲₁ = 𝔲_M = 1 each constant with index l is the one with index d it replaces, ε^l ≤ ε^z, η_l =
η_d, A_l ≤ A_d, B_l = B_d and 𝔰_*^l ≤ 𝔰_*^d; so the hypotheses of [[thm:tl5-hfd]] imply these with 𝔲₀ = 𝔲₁ = 𝔲_M = 1.

*Proof.* The proof of [[thm:tl5-hfd]] applies with the constants with index l, ε^l, η_l, A_l, B_l, 𝔰_*^l and
[[eq:tl5-hfe-closing]], with four changes.

*The steps of zeroth order.* In the proof of [[lem:tl5-hfp-abs]] (c), with the constants with index d, the step applies
[[lem:tl5-hf-sobolev]] in the form of [[lem:tl5-hft-face]] (b) with the weights 𝔶_(|J|) and C_(E,0)(𝔶); by
[[lem:tl5-hfe-face]] (b) with 𝔲 = 𝔲₀ this form holds with C_S^l(p) in place of C_S^p(p), the terms on S_a being the
same, so the step gives its bounds of Ψ_B(p) and of the families with C_S^l in place of C_S^p.

*The steps of first order.* In the proof of [[lem:tl5-hfp-c1]] use [[eq:tl5-hfe-face]] with r = 3 and 𝔲 = 𝔲₁ for each
A_B in place of [[eq:tl5-hf-cs-r]] in its intrinsic form with the weights. This replaces the functions f and W of that
proof by 𝔳₀⁶ R⁻³ (𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) and 2𝔲₁⁻¹ |∂_γ|² 𝔳₀⁶ R⁻³, and leaves its terms on S_a unchanged. The rest of
that proof uses f and W only as nonnegative continuous functions on the face, through Minkowski's inequalities and the
bounds ∫ g 𝒟_g² ≤ sup (g 𝔨₂′) ℰ_g(p) and ∫ g 𝒥_g² ≤ sup (g 𝔨₂) ℰ_g(p) for functions g ≥ 0; so it gives
[[eq:tl5-hfp-family]] with C₁^l(𝔚) and C_(1,ϱ)^l in place of C₁(𝔚) and C_(1,ϱ)^p, with the same E₀, and the first-order
step of the lemma in use gives its bound of D̂Ψ_B(p) with C₁^l and C_(1,ϱ)^l. The bounds of [[lem:tl5-hfp-rec]],
[[lem:tl5-hfp-low]] and [[lem:tl5-hfv-rec]], and the bounds at a point that the proofs of [[thm:tl5-hfp]] and
[[thm:tl5-hfu]] take from the lemma in use, are formed from these two steps, the recovery and the absorption, in the
same way for all values of these constants; so they hold with the constants with index l.

*The products with no factor at a point.* For N = 4, the step for μ^(3/2) Y₁ in the proof of [[lem:tl5-hfu-mixed]] uses
[[eq:tl5-hfu-face]] with r = 3. By [[lem:tl5-hfe-face]] (c) with 𝔲 = 𝔲_M it holds with 𝔱_(3,0)(t; 𝔲_M) and 𝔱_(3,1)(t;
𝔲_M), and the rest of that step gives μ^(3/2) Y₁ ≤ 𝔜^l_(1,t) 𝔍_g + 𝔜′^l_(1,t) ϱ + 𝔜″^u_(1,t) η₀; the other bounds of
that proof are unchanged. So the expansion in the proof of [[thm:tl5-hfu]] gives S_M^l Y_s³ + 𝔯_M^l Y_s² + ε_M^l Y_s in
place of S_M^u Y_s³ + 𝔯_M^u Y_s² + ε_M^u Y_s.

*The terms with ϱ.* By [[lem:tl5-hfe-rho]] (b), the parts with ϱ(p) of [[eq:tl5-hfd-words]] hold with 𝔠^ϱ in place of
𝔠^♮. In Step 2 the terms with ϱ of the family of level j are then bounded as in Step 2 of the proofs of
[[prop:tl5-hfs-bootstrap]] (option (a)), [[prop:tl5-hft-bootstrap]] (option (b)) and [[prop:tl5-hfq-bootstrap]] (N = 4),
with 𝔠^ϱ_(j′)(·) + 1 in place of 𝔠^♮_(j′)(·) + 1, which gives 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t) and, for N = 4, either of 𝔤^l_(ϱ,q)
and 𝔤^l_(ϱ,t), in place of 𝔤_(ϱ,s), μ^(−1/2) 𝔤_(𝒥,s) and 𝔤_(ϱ,q). With the bound 𝔰 ≤ 𝔰₁^v of Step 1 and the absorption,
as in the proofs of [[thm:tl5-hfw]], [[thm:tl5-hfy]] and [[thm:tl5-hfz]], this part together with the forcing term is
bounded by Y_s ε^l in place of Y_s ε^z. The rest of the proof holds as written.

For the last claim, let 𝔲₀ = 𝔲₁ = 𝔲_M = 1. Then C_S^l, C₁^(U,l)(𝔚), C₁^(D,l)(𝔚), C₁^(J,l)(𝔚), C_(1,ϱ)^l, 𝔜^l_(1,t) and
𝔜′^l_(1,t) are C_S^p, C₁^U(𝔚), C₁^D(𝔚), C₁^J(𝔚) and C_(1,ϱ)^p with index d and 𝔜^u_(1,t) and 𝔜′^u_(1,t), so every
constant with index l other than ε^l is the one with index d, and S_F^l, S_M^l, ε_M^l, 𝔯^l, η_l and B_l are S_F^d,
S_M^d, ε_M^d, 𝔯^d, η_d and B_d. By [[lem:tl5-hfe-rho]], 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′), so each term of 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t) and
𝔤^l_(ϱ,q) is at most the corresponding one of 𝔤_(ϱ,s), μ^(−1/2) 𝔤_(𝒥,s) and 𝔤_(ϱ,q), and 𝔤_ϱ^l ≤ 𝔤_ϱ^v and ε^l ≤ ε^z. As
A_d and 𝔰_*^d are nondecreasing in ε^z, A_l ≤ A_d and 𝔰_*^l ≤ 𝔰_*^d. ∎

**Remark {#rem:tl5-hfe-what}** (What changes.) In [[lem:tl5-hft-face]], [[lem:tl5-hfp-abs]] (a) and [[lem:tl5-hfu-face]]
the derivative 2⟨B, ℒ_(∂_γ)B⟩₀ of |B|₀² along the curves is bounded by |B|₀² + |ℒ_(∂_γ)B|₀², which fixes the balance
between the two parts of each bracket; with 2xy ≤ 𝔲x² + 𝔲⁻¹y² it is free. A bracket 𝔲X + 𝔲⁻¹Y with X, Y > 0 has the
least value 2(XY)^(1/2) at 𝔲 = (Y/X)^(1/2), and 2(XY)^(1/2) ≤ X + Y, its value for 𝔲 = 1, with a large gain where X and
Y differ much. In the bracket of C₁^(U,l)(𝔚)², X = (μ^(1/2) + ϖ′^(1/2))²: its part μ comes from the leading terms
D̂Ψ_(JB) of the first derivatives ℒ^J D̂Ψ_B, whose words JB have length at most |B| + 2, so that the weights 𝔶_(|J|)
μ^(|B|+3) ≤ μ μ^(|JB|) of the step leave the factor μ over their energies, and its part ϖ′ from their remainders. And
Y = 18|D̂∂_γ|² X + 2|∂_γ|² 𝔩′², 𝔩′ := 𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2), carries the second derivatives, with the recovery
constant k₁^D = 𝔨_♯ K_rec ≥ √5 K_rec in 𝔩_D(𝔚). The least value at a point is at most 2^(3/2) |∂_γ| 𝔩′ X^(1/2) +
6√2 |D̂∂_γ| X, where the value for 𝔲₁ = 1 is at least 2|∂_γ|² 𝔩′²; the ratio of the leading parts is 2^(1/2)
X^(1/2)/(|∂_γ| 𝔩′), with X^(1/2) = μ^(1/2) + ϖ′^(1/2). The same holds in 𝔜^l_(1,t), whose first part carries μ against
𝔩(𝔙₂)² in its second. In C_S^l both parts are bounded through the densities of the same words, X = 1/(2Ω̂² z̲) and Y =
8|D̂∂_γ|²/(2Ω̂² z̲) + 2𝔨₁, and 𝔲₀ gains as far as these differ. Each weight is one function for all the faces and all
the families of words of its steps, and the parts of one step with ℰ_g, ϱ and η₀ share it; the part with ϱ of the
first-order step lies in Y and carries 𝔲₁⁻¹ in C_(1,ϱ)^l², and the parts with η₀ come from the leaf S_a and do not carry
the weight. In the products with a factor at a point the part with ϱ comes from the residual of the recovery of a second
derivative, and only the monomials of H₁^(λσ) D̂_λD̂_σh and H₂^(λσ) D̂_λD̂_σh with the term D̂²Ψ_K of ℒ^K D̂²h have one:
the monomials of 2𝔮̂ and 2𝔮 − 2𝔮̂ have first derivatives, those of 2𝔠(H₁)h and 2𝔠(H₂)h none, and the other monomials of
the Lie derivatives of D̂²h first derivatives or none. When all Λ_k and Λ^R_k vanish, the first sum of 𝔠^ϱ_n is 2^n, so
𝔠^ϱ_n + 1 = 2^n and 𝔠^♮_n + 1 = 81 · 2^n up to terms with the factor 𝔰_♭, and each term of 𝔤_ϱ^l is about 1/81 times the
corresponding one of 𝔤_ϱ^v; in general 𝔠^ϱ_n ≤ 𝔠^♮_n − 𝔠^D_n. The counts 𝔠^Mq₁ and 𝔠^Mq₂ of the products with no factor
at a point, the leaf constant C_(E,0)(𝔶), 𝔨₂, K_rec, 𝔨_♯, 𝔵^z and the thresholds are unchanged. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfe]] are established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 16fb423f, where sec:tl5-hfd is merged (Section 57.27,
merge cee5c801). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfe) through the last line of
[[rem:tl5-hfe-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfd-what]] (line 7266,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfd-what]] (lines 7264–7265).* Old:

monomials keep the count 7^(j′/2), and the parts with ϱ keep 𝔤_(ϱ,s). As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfd]] are established in this paper for no background at 10 l5.

New (one line added, of 117 characters; the two old lines are unchanged):

monomials keep the count 7^(j′/2), and the parts with ϱ keep 𝔤_(ϱ,s). As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfd]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfe]] gives the transport along the curves a weight and the parts with ϱ their own count ([[thm:tl5-hfe]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfe acts at every level, on thm:tl5-hfd: at N ≥ 6 on its form from thm:tl5-hfp, at N = 4 on
its form from thm:tl5-hfu. It makes two changes. For 𝔲₀ = 𝔲₁ = 𝔲_M = 1 every factor is the one with index d except the
coefficient 𝔤_ϱ of ϱ in ε, which is at most it; so the theorem contains thm:tl5-hfd, and through it every earlier
theorem of the chapter in the range where thm:tl5-hfd contains it.

Unchanged: the leaf constant C_(E,0)(𝔶); 𝔨₂, 𝔨₂′, 𝔨₁; K_rec, 𝔨_♯, k₁^D, k₂^z, 𝔵^z; the recovery and family numbers
𝔩_D, 𝔩_J, 𝔩(𝔙), 𝔞_𝔄; the counts 𝔠^♮ − 𝔠^D and 𝔠^(D,7) of the parts with 𝒥_g in 𝔎^D, and 𝔠^Mq₁, 𝔠^Mq₂ in S_M; the
parts on S_a, that is C_(S,0), C_(1,0)^p, C_(0,0)^p, E₀ and 𝔜″^u; 𝔛^u_(1,t), 𝔛^u_(2,t), 𝔛′^u_(2,t) and 𝔜_(2,t); the
thresholds 𝔰₀, 𝔰₁^v and the cap; the rates.

1. The transport weights (lem:tl5-hfe-face). In each step whose face inequality carries the leaf integrals along the
   curves, 2⟨B, ℒ_(∂_γ)B⟩₀ ≤ 𝔲|B|₀² + 𝔲⁻¹|ℒ_(∂_γ)B|₀² replaces the bound |B|₀² + |ℒ_(∂_γ)B|₀², so the coefficients
       1 + 2r²|D̂∂_γ|² (of |ℒ^J A|²)   and   2|∂_γ|² (of |D̂ℒ^J A|²)
   become
       𝔲 + 2r²𝔲⁻¹|D̂∂_γ|²            and   2𝔲⁻¹|∂_γ|².
   The factors, old → new (the suprema over Σ₁(a, b) unless marked [·]_t):
   - zeroth order, 𝔲 = 𝔲₀ (rank 2):
       C_S^p² = C_(E,0)(𝔶)²𝔴₀⁴ sup 𝔳₀⁴R⁻³((1 + 8|D̂∂_γ|²)/(2Ω̂²z̲) + 2𝔨₁)
       C_S^l² = C_(E,0)(𝔶)²𝔴₀⁴ sup 𝔳₀⁴R⁻³((𝔲₀ + 8𝔲₀⁻¹|D̂∂_γ|²)/(2Ω̂²z̲) + 2𝔲₀⁻¹𝔨₁)
   - first order, 𝔲 = 𝔲₁ (rank 3), with 𝔩′ := 𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^½:
       C₁^U(𝔚)² = C_(E,0)(𝔶)²𝔴₀⁶ sup 𝔳₀⁶R⁻³𝔨₂((1 + 18|D̂∂_γ|²)(μ^½ + ϖ′^½)² + 2|∂_γ|²𝔩′²)
       C₁^(U,l)(𝔚)² = C_(E,0)(𝔶)²𝔴₀⁶ sup 𝔳₀⁶R⁻³𝔨₂((𝔲₁ + 18𝔲₁⁻¹|D̂∂_γ|²)(μ^½ + ϖ′^½)² + 2𝔲₁⁻¹|∂_γ|²𝔩′²)
       C₁^D(𝔚)² = … 𝔨₂′(μ(1 + 18|D̂∂_γ|²) + 2|∂_γ|²𝔩_D²)
           →  C₁^(D,l)(𝔚)² = … 𝔨₂′(μ(𝔲₁ + 18𝔲₁⁻¹|D̂∂_γ|²) + 2𝔲₁⁻¹|∂_γ|²𝔩_D²)
       C₁^J(𝔚)² = … 𝔨₂((1 + 18|D̂∂_γ|²)ϖ′ + 2|∂_γ|²(𝔩_J + (2ϖ′)^½)²)
           →  C₁^(J,l)(𝔚)² = … 𝔨₂((𝔲₁ + 18𝔲₁⁻¹|D̂∂_γ|²)ϖ′ + 2𝔲₁⁻¹|∂_γ|²(𝔩_J + (2ϖ′)^½)²)
       C₁(𝔚) = min(C₁^U, C₁^D + C₁^J)  →  C₁^l(𝔚) = min(C₁^(U,l), C₁^(D,l) + C₁^(J,l)); C₁^p → C₁^l, C₁^Γ → C₁^(Γ,l)
       C_(1,ϱ)^p² = 43C_(E,0)(𝔶)²𝔗²𝔴₀⁶ sup(𝔳₀⁶R⁻³2|∂_γ|²(k₂^z)²/(1 − 𝔵^z)²)∫dμdτ₂/(1 − κκ′)
           →  C_(1,ϱ)^l² = the same with 2𝔲₁⁻¹|∂_γ|²
   - level four, the products with no factor at a point, 𝔲 = 𝔲_M (rank 3, the step for Y₁):
       𝔱_(3,0)(t) = [𝔳₀⁶R⁻³(1 + 18|D̂∂_γ|²)]_t, 𝔱_(3,1)(t) = [2𝔳₀⁶R⁻³|∂_γ|²]_t
           →  𝔱_(3,0)(t; 𝔲_M) = [𝔳₀⁶R⁻³(𝔲_M + 18𝔲_M⁻¹|D̂∂_γ|²)]_t, 𝔱_(3,1)(t; 𝔲_M) = [2𝔲_M⁻¹𝔳₀⁶R⁻³|∂_γ|²]_t
       𝔜^u_(1,t) = (μ𝔱_(3,0) + 𝔱_(3,1)[𝔩(𝔙₂)]_t²)^½ → 𝔜^l_(1,t), the same with 𝔱(t; 𝔲_M)
       𝔜′^u_(1,t) = 7(μ/ν)^(3/2)𝔱_(3,1)^½ς_t → 𝔜′^l_(1,t), the same with 𝔱_(3,1)(t; 𝔲_M)
       S_M^u, 𝔯_M^u → S_M^l, 𝔯_M^l; ε_M^u unchanged (it carries 𝔜″^u_(2,t), not 𝔜^u_(1,t)).
   These enter, through C_S^l, C₁^l(𝔚), C₁^l, C₁^(Γ,l) and C_(1,ϱ)^l, the numbers 𝔐_p^(m), 𝔨_rec^p, 𝔨_rec^(ϱ,p), C_P^v,
   C_(P,ϱ)^v, C_(∞,μ)^(m), C_((∞,ϱ),μ)^(m) and their forms with ν, 𝔎, 𝔎_ϱ, 𝔎^D, 𝔎^D_ϱ, S_F, 𝔯 and 𝔰_*. C_(P,0)^v,
   𝔨_rec^(0,p), C_((∞,0),·)^(m), 𝔎₀ and 𝔎^D₀ contain none of them and are unchanged.
   The choice of the weights, for the evaluation. A bracket 𝔲X + 𝔲⁻¹Y, X, Y > 0, is least at 𝔲 = (Y/X)^½, where it is
   2(XY)^½; against X + Y (𝔲 = 1) its square root falls by (2(XY)^½/(X + Y))^½ ≤ 2^½ (X/Y)^¼ when X ≤ Y.
   - C₁^(U,l)(𝔚): X = (μ^½ + ϖ′^½)², Y = 18|D̂∂_γ|²X + 2|∂_γ|²𝔩′². At a point X, Y do not depend on the point p of the
     bound, and the common factor 𝔳₀⁶R⁻³𝔨₂ (with the per-face h₀) does not move the optimum; so 𝔲₁ := (Y/X)^½,
     formed with the family that leads (Γ at level four, for 𝔨_rec^p), is one continuous function that is pointwise
     optimal for that family on every face. The other families, and C₁^(D,l), C₁^(J,l), take the same 𝔲₁; at
     𝔲 = r𝔲* a bracket is (r + 1/r)/2 times its least value.
   - C_S^l: X = 1/(2Ω̂²z̲), Y = 8|D̂∂_γ|²/(2Ω̂²z̲) + 2𝔨₁; 𝔲₀ := (Y/X)^½ likewise.
   - 𝔜^l_(1,t): the two coefficients have separate suprema [·]_t; any positive continuous 𝔲_M is admissible, for example
     a function of τ₁ that is constant on each Σ₁(t, v*) and minimises μ𝔱_(3,0)(t; 𝔲) + 𝔱_(3,1)(t; 𝔲)[𝔩(𝔙₂)]_t² there.
   - One weight serves all the parts of its step: C_(1,ϱ)^l falls with larger 𝔲₁ (𝔲₁⁻¹ under the root), the parts with η₀
     do not move.
   - The face weights α : β : ρ of h₀ are searched per face and per constant in the evaluation (G0f: a grid of ±6 in ln
     about the seed, refined in steps of 0.05, objective max 𝔴₀(p)^k sup(𝔳₀^k g)); with the weights the face function g
     of each constant changes, and the search should take the new g. No lever is claimed for 𝔴₀, 𝔳₀ themselves.
2. The parts with ϱ (lem:tl5-hfe-rho). In ε's coefficient of ϱ,
       𝔠^ϱ_n(ν′) = Σ⁴_n λ^♮_(k₁)(ν′)λ^♮_(k₃)(ν′) − 1 + 𝔰_♭(Σ⁶_n b^♮_g(k₁, ν′)λ^♮_(k₃)(ν′)λ^♮_(k₅)(ν′) − 𝔤₀)
   replaces
       𝔠^♮_n(ν′) = Σ⁴_n λλβ₂ − 1 + 5Σ⁵_n λλΛ^R + 16Σ⁴_n λ̂λ̂β₁β₁ + 𝔰_♭𝔠^(3♮)_n(ν′),
   in
       𝔤_(ϱ,s) → 𝔤^l_(ϱ,s) (N ≥ 6, option (a); argument 1),
       μ^(−½)𝔤_(𝒥,s) → 𝔤^l_(ϱ,t) (N ≥ 6, option (b), and N = 4; argument μ),
       𝔤_(ϱ,q) → 𝔤^l_(ϱ,q) (N = 4; argument ν = μ^θ),
   each term 7^(j′/2)(𝔠^♮_(j′)(·) + 1) becoming 7^(j′/2)(𝔠^ϱ_(j′)(·) + 1), and
       ε^z = 𝒮[s_N[2R̂ic] + 𝔰₁^v(1 − 𝔵^z)⁻¹𝔤_ϱ^v k₂^z ϱ]  →  ε^l = 𝒮[s_N[2R̂ic] + 𝔰₁^v(1 − 𝔵^z)⁻¹𝔤_ϱ^l k₂^z ϱ].
   The parts with 𝒥_g (𝔎^D in S_F) keep their counts. Proved: 0 ≤ 𝔠^ϱ_n ≤ 𝔠^♮_n − 𝔠^D_n.
   At Λ_k = Λ^R_k = 0 (the floor), summed exactly:
       n                         0      1       2       3       4         5        6
       𝔠^♮_n + 1, 𝔰_♭ = 10⁻⁴     81.02  162.07  324.28  649.35  1304.14
       𝔠^ϱ_n + 1, 𝔰_♭ = 10⁻⁴     1      2.0006  4.0029  8.0132  16.070
       𝔠^♮_n + 1, 𝔰_♭ = 10⁻⁶     81.00  162.00  324.00  648.01  1296.08   2592.61  5189.65
       𝔠^ϱ_n + 1, 𝔰_♭ = 10⁻⁶     1      2.0000  4.0000  8.0001  16.0007   32.005   64.038
       ratio                     0.0123 in every column (−1.91 decades)
   The 𝔠^♮₄ + 1 = 1304.1 at 𝔰_♭ = 10⁻⁴ is the floor 1303 of G0n. At G0o's medians (n = 4), 𝔠^♮₄ − 𝔠^D₄ + 1 = 55–117
   bounds 𝔠^ϱ₄ + 1 from above, against 𝔠^♮₄ + 1 = 1338–1402: the j′ = 4 terms fall by at least −1.06 to −1.40 decades,
   and by −1.91 where the Λ-parts are at the floor. The parts of 𝔠^♮ − 𝔠^D above the floor that 𝔠^ϱ drops are those of
   5Σ⁵λλΛ^R (whose terms with k₄ = 0 carry Λ^R₀ = |R̂| undamped by ν′), of the β₁ − 1 and λ̂_(k≥1) in 16Σ⁴λ̂λ̂β₁β₁, and
   of β₂ − 1.
3. The closing condition eq:tl5-hfe-closing is eq:tl5-hfd-closing with the constants with index l.

What it gives, deduced, not evaluated. At G0o's optima. Assumptions:
- 𝔨_rec^p leads C_P^v, 1.29 / 1.37 / 1.44 / 1.55 decades above 2C_S, and the C_P^v levers transfer 1:1 (G0o.1);
- at the supremum of C₁, the part with 2|∂_γ|²𝔩′² is at least 13: G0l measured the k-part of C₁^z's bracket at 93–95.5 %
  and the rest (1 + 18|D̂∂_γ|²)(1 + ϖ′^½)² ≥ 1 at 4.5–7 %, so Y ≥ 0.93/0.07 ≈ 13; 𝔩′ for the seven fields Γ carries
  301^½𝔵^z where that 𝔩 carried 43^½𝔵^z;
- X = (μ^½ + ϖ′^½)² ≈ μ, as ϖ′^½ ≈ 24μΛ₁ is small against μ^½ at μ ≤ 10⁻⁴;
- μ = 10⁻⁵ / 10⁻⁴ / 10⁻⁶ / 10⁻⁵ (seed 1 D_A / seed 2 D_A / seed 1 D* / seed 2 D*), and μ fixed.
Level 4:
- 𝔲₁: C₁ is multiplied by at most (2(μ/13)^½)^½, that is −1.38 / −1.13 / −1.63 / −1.38 decades or more, at the
  supremum.
  - C_P^v falls with 𝔨_rec^p until 2C_S leads: −1.29 / −1.13 to −1.37 / −1.44 / −1.38 to −1.55.
  - At 1:1 that is up to +1.29 / +1.13–1.37 / +1.44 / +1.38–1.55 on min(f, ϱ), if 𝔰_* keeps binding.
  - The closing then also moves: S_F falls with C_P^v (𝔎^D's C_P part, and 𝔎 = max(2C_S𝔨_A, C_P𝔨_B) until 2C_S𝔨_A leads).
    Without 𝔲_M, S_M (1.29 / 1.10 / 1.69 / 1.67 below S_F) would cap the D_A cases at about +1.09 (seed 1) and +0.94–1.03
    (seed 2), counting the closing's spare 0.08 / 0.09; the D* cases are not capped.
  - 𝔲_M: the term of S_M with 𝔠^Mq₁ (480 + …) carries 𝔜^l_(1,t), whose first part has μ against 𝔩(𝔙₂)² in the second,
    the same shape; its term with 𝔠^Mq₂ (4 + …) is unchanged. So S_M falls, by the factor of its first term while
    that term leads; the split of S_M between its two terms is not reported, so this is not priced.
- 𝔲₀: C_S falls by (2(XY)^½/(X + Y))^½ with X = 1/(2Ω̂²z̲), Y = 8|D̂∂_γ|²/(2Ω̂²z̲) + 2𝔨₁. Not reported. With G0j's
  𝔨₂ = 10^2.57–2.72, 1/z̲ about three quarters of its numerator, so X ≈ 280–390, and Y between 2𝔨₁ ≥ 6 and 50, C_S
  falls about 0.07–0.3 decades. It acts once 2C_S leads C_P^v, until C₁ or 𝔨_rec leads again.
- 𝔠^ϱ at level 4: ε's coefficient of ϱ, min(𝔤^l_(ϱ,q), 𝔤^l_(ϱ,t)), falls by about −1.06 to −1.9 decades. G0o prices
  × 0.1 at +0.15 / +0.23 / +0.08 / +0.20; with ϱ 0.03–0.11 above f, this moves the share of ε.
Level 6 (G0m's optima: μ = 10⁻⁵ / 10⁻⁴ / 3 × 10⁻⁶ / 10⁻⁵; option (b)):
- 𝔠^ϱ: 𝔤^l_(ϱ,t) falls −1.91 decades at the floor, every j′. ϱ binds there and its coefficient was priced × 0.1 at
  +0.99 / +0.97 / +1.00 / +0.85 (G0o.3), so up to about +0.85 to +1.9, until f binds (f is 0.12–0.51 above ϱ, and
  rises with the share of ε it is given) or the 𝔯 budget of ϱ.
- 𝔲₁: ϱ ∝ 1/(sup C_(∞,μ)^(2) k₂^z), whose leading term is C₁'s (𝔐_p^(2)); C₁ falls −1.38 / −1.13 / −1.51 / −1.38
  decades or more at these μ, on the same assumptions. It acts until the parts with C_S lead C_(∞,μ)^(2); that
  margin is not reported.
The two changes act on different factors (C_P^v and C_(∞,μ) against 𝔤_ϱ), so at level 6 they add while ϱ binds.

Not done.
- Target 3, the word sums for the other monomials (H₁D̂²h, the terms with R̂, the terms of 2𝔮̂ with a background letter
  inside β₁, R₃). Not attempted. G0o bounds it by +0.21 (seed 2 D_A) and +0.34 (seed 2 D*), 0 in the other two, capped
  by 𝔰_*, before the family costs 𝔩(𝔙_k) ≤ 7^(k/2)𝔨_A (Φ₂ = D̂²Ψ) and (Σ_Z𝔷_Z²)^½ ≤ √7𝔷 (Φ₂ = Ψ_C). These costs fall on
  𝔨_A and 𝔨_B, the factors left in 𝔎 = max(2C_S𝔨_A, C_P𝔨_B) once the transport weight has lowered C_P; whether a gain
  remains needs thm:tl5-hfe evaluated first.
- Minkowski's inequality for |ℒ_(∂_γ)B| ≤ |∂_γ||D̂B| + r|D̂∂_γ||B| in place of (x + y)² ≤ 2x² + 2y². At the optimal 𝔲₁ it
  halves the part 2|∂_γ|²𝔩′² of Y and so lowers C₁ by at most 2^(−¼) (−0.075 decades), and nothing once 2C_S leads,
  which the weight reaches at seed 1 D_A and seed 1 D* on these assumptions and may reach at the other two. Not done.
- 𝔨₂: the 1/z̲ split (𝒟_g) was worth 0.00 at the supremum (G0m); not redone.
- The √7 on 𝔞_𝔄(Γ): ≤ 0.03 (G0n); skipped.
- The weight in 𝔜_(2,t) (rank 2, the 343 words of length three): both parts have the weight μ³ of the step and are
  bounded together by 𝒥_g², so the balance gives nothing there; and in the steps with a leaf only (𝔛^u, the parts on
  S_a) there is no transport. Not done.
- k₁^D = 𝔨_♯K_rec → √5K_rec: sharp in this argument (sec:tl5-hfz, sec:tl5-hfp).

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfe	paper/reader/proofs/P-GRD13.md@PENDING:1	P-GRD13, section	new; at the end of ch:ten-l5, after rem:tl5-hfd-what; a weight u in the transport along the curves, 2<B, L B> <= u|B|^2 + u^-1 |L B|^2, and the parts with rho of the products counted over the second derivatives
    lem:tl5-hfe-face	paper/reader/proofs/P-GRD13.md@PENDING:20	P-GRD13, Lemma	the transport along the curves with a positive continuous weight u: eq:tl5-hf-cs-r, lem:tl5-hf-sobolev and eq:tl5-hfu-face with u + 2r^2 u^-1 |D d_gamma|^2 and 2u^-1 |d_gamma|^2 in place of 1 + 2r^2 |D d_gamma|^2 and 2|d_gamma|^2
    eq:tl5-hfe-face	paper/reader/proofs/P-GRD13.md@PENDING:29	P-GRD13, display	new
    lem:tl5-hfe-rho	paper/reader/proofs/P-GRD13.md@PENDING:69	P-GRD13, Lemma	the monomials with a second derivative are those of H_1 D^2 h and H_2 D^2 h with the term D^2 Psi_K, counted by c^rho_n; the parts with rho of the products hold with c^rho_n in place of c_n; 0 <= c^rho_n <= c_n - c^D_n
    eq:tl5-hfe-rho	paper/reader/proofs/P-GRD13.md@PENDING:75	P-GRD13, display	new
    def:tl5-hfe-constants	paper/reader/proofs/P-GRD13.md@PENDING:126	P-GRD13, Definition	constants with index l: C_S^l (weight u_0), C_1^l(W) and C_(1,rho)^l (u_1), Y^l_(1,t) and Y'^l_(1,t) (u_M); g^l_(rho,s), g^l_(rho,t), g^l_(rho,q) with c^rho; eps^l, eta_l, A_l, B_l, s_*^l
    eq:tl5-hfe-constants	paper/reader/proofs/P-GRD13.md@PENDING:142	P-GRD13, display	new
    thm:tl5-hfe	paper/reader/proofs/P-GRD13.md@PENDING:164	P-GRD13, Theorem	thm:tl5-hfd with the constants with index l; for u_0 = u_1 = u_M = 1 its hypotheses imply these
    eq:tl5-hfe-closing	paper/reader/proofs/P-GRD13.md@PENDING:169	P-GRD13, display	closing condition: 4 eta_l^(-3/2)(delta_w + eta_l^(-1/2)(eps^l + eps_M^l))(S_F^l + S_M^l) < 1
    rem:tl5-hfe-what	paper/reader/proofs/P-GRD13.md@PENDING:215	P-GRD13, Remark	what changes
