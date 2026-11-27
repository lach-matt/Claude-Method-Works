### The sharpened constants {#sec:tl5-hfg}

This section sharpens the constants of [[thm:tl5-hf]] and [[thm:tl5-hf4]] in three ways and proves both theorems with
the sharpened constants. First, each background factor of a quadratic term is bounded by a bound for the derivatives of
ĝ of its own order, instead of the uniform bound Λ, and the constant of the recovery of second derivatives is taken at
the level where it is used ([[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]]). Second, in Step 2 of the proof of
[[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again; here each factor is bounded by the energies of
the lowest level that controls it, and in every term of level n the two levels used add up to at most n + 3, so that
the factor becomes μ^(−3/2) at every level N ≥ 4 ([[lem:tl5-hfg-products]]). Third, the quadratic part of N(h) is
expanded with its own coefficients, the terms of higher order carrying a factor 𝔰 ([[lem:tl5-hfg-quadratic]]), and the
factor bounded at a point is never a second derivative of a word of length two or more ([[lem:tl5-hfg-products]]). The
closing conditions are [[eq:tl5-hfg-closing]] at level N ≥ 6 and [[eq:tl5-hf4g-closing]] at level four
([[thm:tl5-hfg]], [[thm:tl5-hf4g]]); those of [[thm:tl5-hf]] and [[thm:tl5-hf4]] remain valid, and either may be used.
Throughout, N ≥ 4 and μ ∈ (0, 1]; for N = 4 the quantities 𝔰, 𝔧 and 𝔭_M are those of [[def:tl5-hf4-levels]], and
[[lem:tl5-hf4-linfty]] takes the place of [[lem:tl5-hf-linfty]].

**Definition {#def:tl5-hfg-graded}** (Graded quantities.) Let h be a C^(N+2) symmetric 2-tensor field with g = ĝ + h
Lorentzian. At a point let Λ₀ ≤ Λ₁ ≤ ⋯ ≤ Λ_N be nonnegative numbers such that Λ_k bounds the norms of ℒ^B R̂ for |B| ≤
k and, if k ≥ 1, those of ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] for |B| ≤ k − 1 and Z ∈ Γ; for k ≥ 1
let λ_k bound the norms of ℒ^K ĝ⁻¹ for the words K with |K| = k; and put Λ̄_k := max(Λ_k, Λ_k²), λ₀ := 1, λ̂₀ := √5
and λ̂_k := λ_k for k ≥ 1. A background factor ℒ^B R̂ carries the |B| letters of B, and ℒ^B π^Z, ℒ^B Γ′[π^Z],
ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] carry the |B| + 1 letters of B and Z; so a factor of these kinds that carries k letters
has norm at most Λ_k. For m ≥ 1 and a function f on ℕ^m write

    Σ^m_n f := Σ_(k∈ℕ^m, k₁+⋯+k_m=n) (n!/(k₁! ⋯ k_m!)) f(k),

and put, with 𝔤₀ and the ordered Bell numbers F_k of [[def:tl5-hf-levels]],

    β₁^g(0) := β₂^g(0) := 1,   β₁^g(k) := 1 + (2^(k+1) − 2) Λ_k,   β₂^g(k) := 1 + (7/3)(4^k − 1) Λ̄_k,
    b_g^g(0) := 𝔤₀,   b_g^g(k) := F_k 𝔤₀^(k+1) (Λ_k + 1)^k,   b_H^g(0) := 1,   b_H^g(k) := (2k + 1) b_g^g(k),
    𝔠^g_n := Σ²_n b_H^g(k₁) β₂^g(k₂) − 1 + 5 Σ³_n b_H^g(k₁) Λ_(k₂) + 16 Σ⁴_n b_g^g(k₁) b_g^g(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^Q_n := Σ⁴_n λ_(k₁) λ_(k₃) β₂^g(k₄) − 1 + 5 Σ⁵_n λ_(k₁) λ_(k₃) Λ_(k₄) + 16 Σ⁴_n λ̂_(k₁) λ̂_(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^(3)_n := Σ⁶_n b_g^g(k₁) λ_(k₃) λ_(k₅) β₂^g(k₆) − 𝔤₀ + 5 Σ⁷_n b_g^g(k₁) λ_(k₃) λ_(k₅) Λ_(k₆)
               + 16 Σ⁶_n b_g^g(k₁) λ_(k₃) (b_g^g(k₄) + λ̂_(k₄)) β₁^g(k₅) β₁^g(k₆),                        {#eq:tl5-hfg-cn}

k ≥ 1 where not stated. Fix 𝔰_♭ ∈ (0, 1/8] and one of the two choices 𝔠^⋆_n := 𝔠^g_n, the first expansion, or 𝔠^⋆_n :=
𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n, the second expansion, for all n ≤ N; with the first choice let 𝔰_♭ := 1/8. Finally put

    𝒥_g := (Σ_(|C|≤N) μ^|C| (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),      M_g^(j) := max_(|C|≤j) μ^((|C|+1)/2) |D̂²Ψ_C|,
    𝔰_g^(m) := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2), μ^((|B|+3)/2) |D̂Ψ_B| (|B| ≤ N − 3),
               μ^((|B|+4)/2) |D̂²Ψ_B| (|B| ≤ m)),
    𝔷 := max_(Z∈Γ) (|Z|² + 4|D̂Z|²)^(1/2),      m_P := min(1, N − 4),

for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4, the maxima over words B and C in Γ, M_g := M_g^(N−1), and for p ∈ D^κ, with a :=
τ₁(p) and b := τ₂(p),

    ℰ_g(p) := Σ_(|I|≤N) μ^|I| ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂.

The order of a solution factor H, Ψ_B, D̂Ψ_B or D̂²Ψ_B is 0, |B|, |B| + 1 or |B| + 2, as in [[def:tl5-hf4-levels]]; a
low quantity of order o enters 𝔰_g^(m) with the weight μ^((o+2)/2), and o + 2 ≤ N, so 𝔰_g^(N−4) ≤ 𝔰 ≤ μ^(−N/2)
𝔰_g^(N−4). For μ = 1, 𝒥_g, M_g, 𝔰_g^(N−4) and ℰ_g(p) are 𝒥₁, M₂, 𝔰 and ℰ⁰_N(p) of [[lem:tl5-hf-linfty]].

Every Λ as in [[def:tl5-hf-levels]] or [[def:tl5-hf4-levels]] may be taken for every Λ_k, as it bounds the five kinds
of factors for words of length at most N; so 𝔠^g_n ≤ 𝔠_n, by Λ ≥ 1 and Σ_(j≤n−k) C(n − k, j) Λ_j ≤ 2^(n−k) Λ, with the
binomial coefficients C(·, ·). And λ_k := Σ_(r=1)^k r! S(k, r) 5^((r+1)/2) Λ_k^r may be taken, S(k, r) the Stirling
numbers of the second kind: by (iv) of the proof of [[lem:tl5-hf-quadratic]] with h = 0, ℒ^K ĝ⁻¹ is a sum of r! S(k, r)
products of r + 1 factors ĝ⁻¹, of norm √5, and r factors ℒ^(B′) π^Z, each carrying at most k letters.

**Lemma {#lem:tl5-hfg-quadratic}** (The quadratic terms with graded background bounds.) Let h be as in
[[def:tl5-hfg-graded]], p a point with 𝔰(p) ≤ 𝔰_♭, and I a word with n := |I| ≤ N. Then ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I
is a sum of monomials, each a contraction of background factors and of q ≥ 2 solution factors of the forms and orders
of [[lem:tl5-hf4-quadratic]] (a), whose background norms ν, with the coefficients, satisfy

    Σ ν 𝔰(p)^(q−2) ≤ 𝔠^⋆_n,                                                                                {#eq:tl5-hfg-sum}

the sum over the monomials. Consequently [[eq:tl5-hf-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N ≥ 5, and
[[eq:tl5-hf4-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N = 4, 𝔑^L_I and 𝔑^M_I being formed from the chosen
expansion.

*Proof.* *The first expansion.* It is that of the proof of [[lem:tl5-hf-quadratic]]. In (i) there, ℒ^J R̂ carries
the |J| letters of J, so its norm is at most Λ_(|J|). In (ii), with k := |J|, each monomial of R′_J has one coefficient
ℒ^B Γ′[π^Z] whose letters are among those of J, so its norm is at most Λ_k, and ℒ^J D̂h is a sum of monomials of total
background norm at most β₁^g(k). In (iii) each monomial of R_J has at most two background factors, carrying letters of
J, so their product is at most Λ̄_k, and the total is at most β₂^g(k). In (iv) each factor ℒ^B ĝ = ℒ^(B′) π^Z carries
the |B| ≤ k letters of B, so ℒ^J g⁻¹ has total background norm at most b_g^g(k) and ℒ^J H at most b_H^g(k), the
number of factors in the telescoping sums being 2r + 1 ≤ 2k + 1 as there. Summing as in that proof, over the
distributions of the letters of I over the factors of each term of N(h), gives the three sums of 𝔠^g_n: Σ²_n from
H^(λσ) D̂_λD̂_σ h, the letters going to H and to D̂²h, less 1 for the subtracted term H^(αβ) D̂_αD̂_βΨ_I; Σ³_n from the
five terms of 2𝔠(H)h, the letters going to H, R̂ and h; Σ⁴_n from the sixteen units of coefficient of 2𝔮. Every
monomial has q ≥ 2 solution factors and 𝔰(p) ≤ 1, which gives [[eq:tl5-hfg-sum]].

*The second expansion.* Let H₁ := −ĝ⁻¹ h ĝ⁻¹, that is H₁^(αβ) = −ĝ^(αμ) h_μν ĝ^(νβ), and H₂ := H − H₁. Since g⁻¹ −
ĝ⁻¹ = −g⁻¹ h ĝ⁻¹, applied twice, H₂ = g⁻¹ h ĝ⁻¹ h ĝ⁻¹. By [[lem:tl5-hf-reduced]], 2𝔮 = Σ_m c_m 𝒯_m(g⁻¹, g⁻¹, D̂h, D̂h)
with Σ_m |c_m| = 16, each 𝒯_m a contraction, linear in each argument; let 2𝔮̂ := Σ_m c_m 𝒯_m(ĝ⁻¹, ĝ⁻¹, D̂h, D̂h). Then
2𝔮 − 2𝔮̂ = Σ_m c_m (𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹, H, D̂h, D̂h)) with H = −g⁻¹ h ĝ⁻¹, and, 𝔠 being linear in its first
argument, N(h) = Q + R₃ with

    Q := H₁^(λσ) D̂_λD̂_σ h − 2𝔠(H₁)h − 2𝔮̂,      R₃ := H₂^(λσ) D̂_λD̂_σ h − 2𝔠(H₂)h − (2𝔮 − 2𝔮̂).

So ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I is the sum of ℒ^I Q − H₁^(αβ) D̂_αD̂_βΨ_I and ℒ^I R₃ − H₂^(αβ) D̂_αD̂_βΨ_I. Expand
ℒ^I of each term by Leibniz's rule over its factors, as in the proof of [[lem:tl5-hf-quadratic]]: ℒ^J h = Ψ_J;
ℒ^J D̂h, ℒ^J D̂²h and ℒ^J g⁻¹ by (ii), (iii) and (iv) there, with the bounds β₁^g, β₂^g and b_g^g of the first part;
ℒ^J R̂ with norm at most Λ_(|J|); and ℒ^K ĝ⁻¹, for K ≠ ∅, as one background factor of norm at most λ_(|K|). The factors
ĝ⁻¹ that carry no letter in H₁, in H₂ and in H = −g⁻¹ h ĝ⁻¹ join an index of h to an index of another factor; in the
frame F, where ĝ^MN = η^MN, such a contraction is bounded by the product of the norms of the two factors, by the
Cauchy–Schwarz inequality, so these factors count λ₀ = 1. A factor ĝ⁻¹ of 𝒯_m that carries no letter may join two
indices of one factor, and counts |ĝ⁻¹| = √5 = λ̂₀. A full contraction of the factors is bounded by the product of
their norms. Summing over the distributions of the letters gives, for the terms of Q, the three sums of 𝔠^Q_n: Σ⁴_n
over the factors ĝ⁻¹, h, ĝ⁻¹, D̂²h of H₁^(λσ) D̂_λD̂_σ h, less 1 for the subtracted term H₁^(αβ) D̂_αD̂_βΨ_I; Σ⁵_n over
ĝ⁻¹, h, ĝ⁻¹, R̂, h for the five terms of 2𝔠(H₁)h; and Σ⁴_n over ĝ⁻¹, ĝ⁻¹, D̂h, D̂h for 2𝔮̂. Likewise the terms of R₃
give the three sums of 𝔠^(3)_n: Σ⁶_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h, less b_g^g(0) = 𝔤₀ for H₂^(αβ) D̂_αD̂_βΨ_I;
Σ⁷_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, R̂, h; and Σ⁶_n over g⁻¹, h, ĝ⁻¹, X, D̂h, D̂h with X = g⁻¹ or X = ĝ⁻¹. In the terms of
Q each of the two factors among h, D̂h and D̂²h keeps exactly one solution factor in its expansion, and the factors ĝ⁻¹
and R̂ none, so q = 2; in the terms of R₃ three such factors keep one each, so q ≥ 3, and 𝔰(p)^(q−2) ≤ 𝔰_♭. This gives
[[eq:tl5-hfg-sum]].

*The forms and the consequences.* In both expansions every term of N(h) carries at most two derivatives D̂ on its
solution factors, the expansions (ii)–(iv) do not increase this number, and the letters of I are distributed over
distinct factors; so the argument of [[lem:tl5-hf4-quadratic]] (a) applies: the orders of the solution factors of a
monomial add up to at most n + 2, and each is at most n + 1, the factor D̂²Ψ_I occurring only in the subtracted terms.
A solution factor is high, in the sense of [[lem:tl5-hf-quadratic]] (N ≥ 5) or of [[lem:tl5-hf4-quadratic]] (N = 4),
exactly when its order is at least N − 1. If N ≥ 5, two high factors would have orders adding up to at least 2N − 2 >
N + 2; so each monomial has at most one, and is bounded by ν 𝔰^(q−1) 𝔧 at p, which by [[eq:tl5-hfg-sum]] gives
[[eq:tl5-hf-g]] with 𝔠^⋆_n. If N = 4, two high factors have orders 3 and 3 and n = 4; with at most two derivatives D̂
and at most four letters they are D̂Ψ_B and D̂Ψ_(B′) with |B| = |B′| = 2, or Ψ_B and D̂²Ψ_Z with |B| = 3 and Z ∈ Γ, and
the other solution factors carry no letter and no derivative, so they are H or h, of norm at most 𝔰(p). With 𝔑^M_I the
sum of these monomials, each is bounded by ν 𝔰^(q−2) times one of the products whose squares are the terms of 𝔭_M²,
and the others by ν 𝔰^(q−1) 𝔧; [[eq:tl5-hfg-sum]] gives [[eq:tl5-hf4-g]] with 𝔠^⋆_n, and 𝔑^M_I = 0 if n ≤ 3. ∎

**Lemma {#lem:tl5-hfg-linfty}** (The low quantities, graded.) Let g be a solution of the reduced problem on D^κ_s, h :=
g − ĝ and p ∈ D^κ_s, with ϱ(p), η₀(p), k₂, C_S, C_(S,0), C_(0,0), C_(1,ϱ), 𝔯₀ and 𝔐 as in [[lem:tl5-hf-linfty]]. Put,
for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4,

    α_𝔄^(j) := √2 max_(|C|≤j) Σ_J ‖𝔄_CJ‖,
    k₁^(j) := (6/5) ((√3 + 8/3) K_rec (1 + √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + 𝔯₀ + (4/3) α_𝔄^(j)),
    k₃^⋆ := (8/5) max_(|C|≤N−1) (𝔠^⋆_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠^⋆_(|J|) + 1)),      𝔐^(m) := Σ_(j≤m+1) 7^j,
    C_∞^(m) := 2 max(2C_S, C₁^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_S, C₁^g)),
    C_(∞,ϱ)^(m) := 2 max(C_(1,ϱ), k₁^(m) (2𝔐^(m))^(1/2) C_(1,ϱ) + k₂),
    C_(∞,0)^(m) := 2 max(2C_(0,0), C_(1,0)^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_(0,0), C_(1,0)^g)),          {#eq:tl5-hfg-cinf}

with the maps of [[def:tl5-hf-coupling]] and their norms as in [[lem:tl5-hf-linfty]], C₁^g and C_(1,0)^g the constants
C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂ in place of Λ, and the Λ_k evaluated at the point of the supremum in
C₁^g; so k₁^(N−1) = k₁, 𝔐^(N−4) = 𝔐 and k₃^⋆ ≤ k₃ when 𝔠^⋆_n ≤ 𝔠_n. If 𝔰 ≤ 𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^⋆))
on Q(a, b), a := τ₁(p), b := τ₂(p), then at every point of Q(a, b)

    M_g^(j) ≤ 2(k₁^(j) + 1) 𝒥_g + 2k₂ ϱ(p)      (0 ≤ j ≤ N − 1),                                         {#eq:tl5-hfg-m2}

and at p

    𝔰_g^(m)(p) ≤ C_∞^(m)(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(m)(p) ϱ(p) + C_(∞,0)^(m)(p) η₀(p)      (0 ≤ m ≤ N − 4).   {#eq:tl5-hfg-linfty}

*Proof.* We follow the proof of [[lem:tl5-hf-linfty]], multiplying each bound by the weight of the quantity it bounds;
for N = 4 that proof applies as in [[lem:tl5-hf4-linfty]]. The bounds of [[lem:tl5-hf-quadratic]] it uses, for words of
length at most N − 1, hold with 𝔠^⋆ by [[lem:tl5-hfg-quadratic]], as 𝔰 ≤ 𝔰_♭ and 𝔑^M_J = 0 for |J| ≤ 3; so its
inequalities hold with k₃^⋆ in place of k₃, and k₃^⋆ 𝔰 ≤ 1/2. By [[lem:tl5-hfg-quadratic]] the solution factors of a
monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J are H, Ψ_C or D̂Ψ_C with |C| ≤ |J|, or D̂²Ψ_C with |C| ≤ |J| − 1.

*Second derivatives.* Let q ∈ Q(a, b), j ≤ N − 1 and |C| ≤ j, and multiply the bound of [[lem:tl5-hf-recovery]] for
Ψ_C, as used in that proof, by μ^((|C|+1)/2). The words ZC have length |C| + 1, so μ^((|C|+1)/2) (Σ_Z |D̂Ψ_(ZC)|²)^(1/2)
≤ 𝒥_g. The terms with D̂Ψ_C and Ψ_C, and those of the maps 𝔄_CJ, |J| ≤ |C|, are bounded by the multiples of 𝒥_g that
bound them by 𝒥₁ there, as μ^((|C|+1)/2) ≤ μ^(|J|/2), with α_𝔄^(j) in place of α_𝔄 as |C| ≤ j; the residual terms by
k₂ ϱ(p), as μ ≤ 1. In the nonlinear terms, each monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, has at most one
high factor, the others being at most 𝔰, and the factor Φ bounded by 𝔧 there satisfies μ^((|C|+1)/2) |Φ| ≤ 2𝒥_g +
M_g^(j): for Φ = H as |H| ≤ 2|h|, for Ψ_(C′) and D̂Ψ_(C′), |C′| ≤ |J|, as μ^((|C|+1)/2) ≤ μ^(|C′|/2), and for
D̂²Ψ_(C′), |C′| ≤ |J| − 1 ≤ j, as μ^((|C|+1)/2) ≤ μ^((|C′|+1)/2). Likewise μ^((|C|+1)/2) |H| |D̂²Ψ_J| ≤ 𝔰 M_g^(j) for
|J| < |C|. So μ^((|C|+1)/2) |D̂²Ψ_C| ≤ k₁^(j) 𝒥_g + k₂ ϱ(p) + k₃^⋆ 𝔰 (2𝒥_g + M_g^(j)), and taking the maximum over C,
with k₃^⋆ 𝔰 ≤ 1/2, M_g^(j)/2 ≤ (k₁^(j) + 1) 𝒥_g + k₂ ϱ(p).

*Zeroth order.* For |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] with A := Ψ_B involves the words JB, |J| ≤ 2, of length at
most |B| + 2, so μ^(|B|+2) Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂ ≤ ℰ_g(p); with μ ≤ 1 in the term on S_a, μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S
ℰ_g(p)^(1/2) + C_(0,0) η₀(p). And μ |H(p)| ≤ 2μ |h(p)|.

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] to A := D̂Ψ_B, as in that proof. For a word J of rotations with
|J| ≤ 2 the coefficients of the remainder R′ in ℒ^J A = D̂Ψ_(JB) + R′ carry at most two letters, so their norms and those
of their derivatives D̂ are at most Λ₂. The words JB have length at most |B| + 2 ≤ N − 1, and the factors Ψ_(C′) of the
remainders have |C′| ≤ |B| + 1, so the bounds |ℒ^J A| ≤ (1 + 6Λ) 𝒥₁ and |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁ there become
μ^((|B|+3)/2) |ℒ^J A| ≤ (1 + 6Λ₂) 𝒥_g and μ^((|B|+3)/2) |D̂ℒ^J A| ≤ M_g + 6√2 Λ₂ 𝒥_g. By [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], ∫_(Σ₁(a,b)) 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g(p), 𝔨₂ as in [[lem:tl5-hf-linfty]], and
[[eq:tl5-hfg-m2]] with j = N − 1 replaces the bound for M₂; the term on S_a is as there, with μ ≤ 1 and Λ₂ in place of
Λ. The computation of that proof then gives μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^g ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^g η₀(p).

*Second order at low levels.* Let |B| ≤ m and multiply the bound at p of that proof by μ^((|B|+4)/2). Its first-order
terms involve Ψ_C and D̂Ψ_C with |C| ≤ |B| + 1 ≤ m + 1 ≤ N − 3, which by the two previous steps are bounded with the
weights μ^((|C|+2)/2) and μ^((|C|+3)/2); so L is replaced by L_g := (Σ_(|C|≤m+1) (μ^(|C|+2) |Ψ_C|² + μ^(|C|+3)
|D̂Ψ_C|²))^(1/2) ≤ (2𝔐^(m))^(1/2) (max(C_S, C₁^g) ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)^g) η₀(p)), there
being 𝔐^(m) words of length at most m + 1, and k₁ by k₁^(m), as |B| ≤ m. Its nonlinear terms come from the words J with
|J| ≤ |B|: in each monomial the factor of largest order o ≤ |B| + 1 is H, Ψ_C or D̂Ψ_C with |C| ≤ |B|, or D̂²Ψ_C with
|C| ≤ |B| − 1, and in H^(αβ) D̂_αD̂_βΨ_J, |J| < |B|, the factor D̂²Ψ_J; each enters 𝔰_g^(m) with a weight at least
μ^((|B|+4)/2), and bounding it by 𝔰_g^(m) and the others by 𝔰 gives at most k₃^⋆ 𝔰(p) 𝔰_g^(m)(p) ≤ 𝔰_g^(m)(p)/2. So
μ^((|B|+4)/2) |D̂²Ψ_B(p)| ≤ k₁^(m) L_g + k₂ ϱ(p) + 𝔰_g^(m)(p)/2.

Taking the largest of the four bounds and absorbing 𝔰_g^(m)(p)/2 gives [[eq:tl5-hfg-linfty]]. ∎

**Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] let I be a
word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I if N ≥ 5, 𝔑^L_I as in
[[lem:tl5-hfg-quadratic]] if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2) and 𝔰_P := 𝔰_g^(m_P). Then at every point of Q(a, b)

    μ^(n/2) |𝔑^L_I| ≤ 𝔠^⋆_n (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p)),
    μ^(n/2) |ℒ^J N(h)| ≤ (𝔠^⋆_(|J|) + 1) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p))      for |J| < n.       {#eq:tl5-hfg-products}

*Proof.* For a low solution factor Φ of order o put ℓ_P(Φ) := o + 2. For any solution factor Φ let ℓ_E(Φ) be 0 for
H and h, |C| − 1 for Ψ_C with |C| ≥ 1, |C| for D̂Ψ_C and |C| + 1 for D̂²Ψ_C. For every factor Φ of a monomial of
ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ n, and for Φ = D̂²Ψ_J with |J| < n,

    μ^(ℓ_E(Φ)/2) |Φ| ≤ 𝔨_g 𝒥_g + 2k₂ ϱ(p).                                                               (∗)

Indeed |H| ≤ 2|h| ≤ 2𝒥_g and |h| ≤ 𝒥_g; for Ψ_C = ℒ_Z Ψ_(C′) with |C| ≥ 1, by [[eq:tl5-hf-lie]], |Ψ_C| ≤ |Z| |D̂Ψ_(C′)| +
2|D̂Z| |Ψ_(C′)| ≤ 𝔷 (|D̂Ψ_(C′)|² + |Ψ_(C′)|²)^(1/2), so μ^((|C|−1)/2) |Ψ_C| ≤ 𝔷 𝒥_g, as |C′| = |C| − 1 ≤ N;
μ^(|C|/2) |D̂Ψ_C| ≤ 𝒥_g; and D̂²Ψ_C has |C| ≤ N − 1 by [[lem:tl5-hfg-quadratic]], so μ^((|C|+1)/2) |D̂²Ψ_C| ≤ M_g,
which [[eq:tl5-hfg-m2]] with j = N − 1 bounds.

Take a monomial of 𝔑^L_I, with solution factors of orders o_i, q ≥ 2 of them; by [[lem:tl5-hfg-quadratic]] it has at
most one high factor, and at most one factor is a second derivative, as there are at most two derivatives D̂ on the
solution factors. Let Φ₂ be the high factor if there is one; otherwise a factor D̂²Ψ_C if there is one; and otherwise a
factor of largest order. Let Φ₁ be another factor, not a second derivative if there is such a choice. By
[[lem:tl5-hfg-quadratic]], o₁ + o₂ ≤ n + 2 and o₂ ≤ n + 1. If o₂ ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1; if o₂ = 0, Φ₂ is neither high
nor a second derivative, so all factors have order 0 and o₁ = 0. In both cases

    ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3,      ℓ_E(Φ₂) ≤ n.                                                      {#eq:tl5-hfg-count}

Φ₁ is low. If Φ₁ = D̂²Ψ_B, then Φ₂ is high and not a second derivative, and it is not D̂Ψ_C either, as the derivatives
D̂ would then number three; so Φ₂ = Ψ_C with |C| ≥ N − 1, every other factor would offer another choice, so q = 2, and
|B| + 2 + N − 1 ≤ o₁ + o₂ ≤ N + 2 gives |B| ≤ 1; with |B| ≤ N − 4, as Φ₁ is low, |B| ≤ m_P. So Φ₁ is one of the
quantities of 𝔰_P, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P. With |Φ_i| ≤ 𝔰 ≤ 1 for the other factors, (∗) for Φ₂, and |Φ₁|
bounded by μ^(−ℓ_P(Φ₁)/2) 𝔰_P in the term with 𝒥_g and by 𝔰 in the term with ϱ(p), the monomial times μ^(n/2) is at
most ν 𝔰^(q−2) times

    μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔨_g 𝔰_P 𝒥_g + μ^((n − ℓ_E(Φ₂))/2) 2k₂ 𝔰 ϱ(p) ≤ μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p),

ν its background norm with the coefficient. By [[eq:tl5-hfg-sum]] this gives the first inequality. For |J| < n,
ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J, and 𝔑_J = 𝔑^L_J also for N = 4, as |J| ≤ 3; the first inequality for J, with
μ^(n/2) ≤ μ^(|J|/2), bounds μ^(n/2) |𝔑_J|. In the last term ℓ_P(H) = 2, H is a quantity of 𝔰_P, ℓ_E(D̂²Ψ_J) = |J| + 1
≤ n and 2 + |J| + 1 ≤ n + 2; the same splitting bounds μ^(n/2) |H| |D̂²Ψ_J| by μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p). ∎

**Lemma {#lem:tl5-hfg-mixed}** (The products of level four, graded.) Let N = 4, and let g, h, t, b, Σ, ϱ and η₀ be as
in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b). With the notation of that lemma, 𝔍_g := ‖𝒥_g‖_Σ and

    𝔛_t^g := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ̄₂]_t),
                 (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),

    μ^(7/2) ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔛_t^g 𝔜_t (𝔍_g + ϱ) (𝔍_g + ϱ + η₀),
    𝔍_g² ≤ [𝔨₂]_t Σ_(|I|≤4) μ^|I| ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                          {#eq:tl5-hfg-mixed}

*Proof.* The second inequality follows from [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], as in the proof of
[[lem:tl5-hf4-mixed]]. By [[eq:tl5-hfg-m2]] with j = 3 at the points of Σ, ‖M_g‖_Σ ≤ λ_t 𝔍_g + ς_t ϱ. In the proof of
[[lem:tl5-hf4-mixed]], ‖𝔭_M‖_Σ² ≤ e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²); we bound μ² X₁, μ² X₂, μ^(3/2) Y₁ and
μ^(3/2) Y₂. The coefficients of the remainders R′ and R there belong to words J of rotations with |J| ≤ 2, so they and
the products of two of them are at most [Λ₂]_t and [Λ̄₂]_t on Σ.

*μ² X₁.* The factors of Σ_B Σ_J |ℒ^J D̂Ψ_B|² there are D̂Ψ_(JB), |JB| ≤ 4, and Ψ_C, |C| ≤ 3, and μ⁴ ≤ μ^(|JB|), μ^(|C|);
so μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2 · 49 · 1320 [Λ₂]_t² 𝒥_g², and μ² X₁ ≤ (𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2) 𝔍_g.

*μ² X₂.* The factors of Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² there are D̂²Ψ_(JZ), |JZ| ≤ 3, with μ² ≤ μ^((|JZ|+1)/2), and D̂Ψ_C, Ψ_C
with |C| ≤ 2; so μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 621516 [Λ̄₂]_t² 𝒥_g², and μ² X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602
‖M_g‖_Σ + 789 [Λ̄₂]_t 𝔍_g).

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* In the bounds of Y₁² and Y₂² there, μ³ Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M_g², μ³ Σ_(|B|=2) |D̂Ψ_B|²
≤ 𝒥_g², μ³ Σ_(|B|=3) (|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², and μ³ ≤ 1 in the terms with η₀; so

    μ³ Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍_g² + 49 ‖M_g‖_Σ²),      μ³ Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍_g².

As there, μ² X_i ≤ 𝔛_t^g (𝔍_g + ϱ) and μ^(3/2) Y_i ≤ 𝔜_t (𝔍_g + ϱ + η₀) for i = 1, 2, and μ^(7/2) (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ μ² X₁ μ^(3/2) Y₁ + μ² X₂ μ^(3/2) Y₂ gives the first inequality. ∎
