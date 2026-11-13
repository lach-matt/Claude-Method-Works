<!-- New section, proposed placement: at the end of chapter 28 (ch:s09), after sec:ii-f1-7, or in chapter 71 before
rem:ec-other-losses. It evaluates the loss d of thm:iii-i-5-3. Statements to strengthen elsewhere are listed in the
report; this text cites only results stated in the edition, with the explicit values added there. -->

### The loss of the forward solution operators, evaluated {#sec:fwd}

[[thm:iii-i-5-3]] asserts a loss d ∈ ℕ. Its proof takes the d of [[thm:ii-f1-1-1]] in the relaxed form of
[[rem:ii-f1-7-1]] with d_ℵ = 1 and raises it by 5, so that

    d = D_0 + D_1 + d′ + d″ + 1 + 5,                                                                   {#eq:fwd-split}

with D_0, D_1, d′, d″ of [[eq:ii-f1-3-2]]–[[eq:ii-f1-3-3]] taken for the orders of [[rem:ii-f1-7-1]]. This section
evaluates each term. The orders d′, d″ and the tame loss D_1 follow from closed forms already in the edition; D_0, the
number of coefficient derivatives, rests on the calculus of finite regularity of [[sec:ii-a1-2]], whose indices are
made explicit in [[prop:fwd-calculus]].

**Theorem {#thm:fwd-loss}** (The forward loss.) In [[thm:iii-i-5-3]] one may take d = 20,180, for every
β_+ ∈ (½, 3/2) and β_I ∈ (β_+, 3/2). More precisely d′ = 10, d″ = 11, D_1 = 49 and D_0 ≤ 20,104 in [[eq:fwd-split]].

The proof occupies the rest of the section and is completed after [[lem:fwd-increments]].

#### The orders {#sec:fwd-orders}

**Lemma {#lem:fwd-orders}** (The orders.) For P_0 = 2L_(b₀), the weights α_+ = β_+ − 5/2, α_I = β_I − 2, ℵ = 2, δ = 0
of the proof of [[thm:iii-i-5-3]] and the margin m_0 + 2d̄_ℵ = 7 of [[rem:ii-f1-7-1]], the construction of
[[sec:ii-c-5-2]] can be carried out with s_in = 11 and s_out = −10, for every β_+ ∈ (½, 3/2). Hence inf 𝗌 = −10,
sup 𝗌 = 11, 𝗌_0 = 𝗌 − 3 has inf 𝗌_0 = −13, s_u = inf 𝗌 − 2 = −12, and

    d′ = max(0, ⌈−inf 𝗌⌉) = 10,        d″ = s_in = 11.                                                {#eq:fwd-dprime}

*Proof.* The construction allows every s_in ∈ ℕ with s_in ≥ 4 + d̄_ℵ = 5 and

    s_in > max(½ + ϑ_ℋ + η, ½(−1 + ϑ^(3b)_in) + α_K + η − α_+) + 1,
    s_out < min(s_in, ½(−1 + ϑ_out) + α_K − η − α_+) − 1,

with η = 7 and α_K = −2, each threshold in a fibre inner product chosen for its radial set ([[sec:ii-c-5-2]],
[[rem:ii-f1-7-1]]). We bound the three thresholds.

*The horizon.* By [[eq:iii-f2-1-1]] and the paragraph after it, ϑ_L = max(0, 2 − 2x) < 2 with x = a_v γ_C r_h > 0, and
for δ = ¼ there is a fixed fibre inner product with ϑ_ℋ < ϑ_L + ¼ < 9/4 at b₀.

*The incoming radial set over ∂K⁺.* By [[lem:ii-c-2-6]], ϑ^(3b)_in = ϑ_in, the threshold of [[eq:i-a-1-5]] at R_in.
By [[lem:ec-theta-in]] (a), p_in − (S + S^(∗h)) = −2 Re_h(A + S) at ∂X for every fibre inner product h, and by its
part (b) the eigenvalues of A + S at ∂X have real parts ≥ 0. The construction in the proof of [[lem:ii-c-2-5]], applied
to the endomorphism A + S in place of S (it uses only the Jordan form at each point and a partition of unity), gives
for every ϵ > 0 a fibre inner product h with λ_min(Re_h(A + S)) ≥ −ϵ on ∂X. With ϵ = 1/8, ϑ_in ≤ ¼.

*The outgoing radial set.* By [[lem:ii-c-2-6]] with the inner product of [[lem:ii-c-2-5]] at ϵ = 1/8,
ϑ_out ≥ 2S̄ − ¼ = −¼, as S̄ = 0 for 2L_(b₀) ([[eq:iii-c-4-3]]).

*The values.* With α_+ ∈ (−2, −1), the first condition reads s_in > max(½ + ϑ_ℋ + 7, −½ + ½ϑ_in + 5 − α_+) + 1, and
½ + 9/4 + 7 + 1 = 43/4 while −½ + 1/8 + 5 + 2 + 1 = 61/8 < 43/4. So s_in = 11 serves for every β_+. The second reads
s_out < min(11, ½(−1 − ¼) − 9 − α_+) − 1 = −85/8 − α_+, whose right side exceeds −77/8 for every α_+ < −1. So
s_out = −10 serves. As 𝗌 = s_in − (s_in − s_out)χ with 0 ≤ χ ≤ 1 taking both values 0 and 1 ([[sec:ii-c-5-2]]),
inf 𝗌 = −10 and sup 𝗌 = 11, and [[eq:fwd-dprime]] follows from [[eq:ii-f1-3-3]]. ∎

The error order used below is N := 13, the least integer with −N ≤ inf 𝗌_0, which is what the global estimates need of
their a priori term ‖χu‖_((−N;k)) ≤ ‖u‖_((𝗌_0;k)) ([[sec:ii-d1-7]]).

#### The tame losses {#sec:fwd-tame}

For variable orders 𝗍, 𝗍_0 write

    d̃(𝗍, 𝗍_0) := s̄ + 2 max(s̲, s̲_0) + 6,     s̄ := max(0, ⌈sup 𝗍⌉),  s̲ := max(0, ⌈−inf 𝗍⌉),
    s̲_0 := max(0, ⌈−inf 𝗍_0⌉),                                                                          {#eq:fwd-dtilde}

the d̃ of [[prop:ii-a-9-6]] at (𝗍, 𝗍_0) (there d_1 = s̄ + max(s̲, s̲_0) + 3 and d̃ = d_1 + max(s̲, s̲_0) + 3).

**Lemma {#lem:fwd-tame}** (The tame loss.) With the orders of [[lem:fwd-orders]] and N = 13, D_1 = 49 in
[[eq:ii-f1-3-2]].

*Proof.* D_1 = max(d^E, d^S, d̃), and every one of these is a closed form in [[eq:fwd-dtilde]] fixed by its proof.

(i) d̃ of [[lem:ii-f1-2-8]] for 𝗍 = 𝗌 is that of [[prop:ii-a-9-6]] at (𝗌 − 2, 𝗌 − 2) ([[cor:ii-a-9-7]] with m = 2):
s̄ = 9, s̲ = s̲_0 = 12, so d̃ = 9 + 24 + 6 = 39.

(ii) d^S. [[prop:ii-e-4-4]] at a slab order 𝗍 has d = d̃ + 3 with d̃ the larger of those of [[lem:ii-e-4-1]] (b) at
𝗍 + 1 and 𝗍 − 1, which is [[prop:ii-a-9-6]] at (𝗍 ± 1, 𝗍 ± 1). At 𝗍 = 𝗌: d̃(𝗌 + 1, 𝗌 + 1) = 12 + 18 + 6 = 36 and
d̃(𝗌 − 1, 𝗌 − 1) = 10 + 22 + 6 = 38, so d = 41. At 𝗍 = 𝗌 + 2 (the slab order 𝗌 + d̄_ℵ + 1 of [[rem:ii-f1-7-1]]):
d̃(𝗌 + 3, 𝗌 + 3) = 14 + 14 + 6 = 34 and d̃(𝗌 + 1, 𝗌 + 1) = 36, so d = 39. [[prop:ii-e-4-3]] and [[prop:ii-e-3-4]] carry
no tame loss. So d^S = 41.

(iii) d^E, the d of [[thm:ii-e-6-1]] at (𝗌_0, 𝗌) = (𝗌 − 3, 𝗌), is the largest of those of its pieces (A)–(C).
(A) [[prop:ii-e-4-4]] at 𝗌: 41. (C) [[prop:ii-e-5-6]] (b): d = d̃ + 3 with d̃ as in [[prop:ii-e-4-4]] at 𝗌: at most 41.
(B) [[thm:ii-d1-1-1]]: d is the largest of the d of [[lem:ii-d1-2-4]] for Steps 2–6 of [[sec:ii-d1-7]] and of
[[prop:ii-a-9-8]]–[[prop:ii-a-9-9]] at the orders 𝗌 + 1 and 𝗌, with error order −N.
[[lem:ii-d1-2-4]] has d = d̃ + 3 with d̃ the larger of [[prop:ii-a-9-6]] at (𝗍 + 1 + 𝔩, 𝗍_0) and (𝗍_0 − 2, 𝗍_0 − 2),
𝗍, 𝗍_0 the constant values of the orders at the set, 𝔩 ≤ 1. At the horizon, at ∂R_(ℐ⁺,in,+) and at ∂R_(∂K⁺,in) the
orders are (𝗌 + 1, 𝗌_0) = (12, 8): d̃(14, 8) = 20, d̃(6, 6) = 12, d = 23. At the trapped set (11, 8): d = 22. At
∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out) the orders are (𝗌, 𝗌_0) = (−10, −13): d̃(−8, −13) = 0 + 26 + 6 = 32,
d̃(−15, −15) = 36, d = 39.
[[prop:ii-a-9-9]] at the order 𝗍 has d = d̃ + 2 with [[prop:ii-a-9-6]] at (𝗍 − m + 1, −N − m), m = 2: at 𝗍 = 𝗌 + 1,
(𝗌, −15) gives s̄ = 11, max(s̲, s̲_0) = 15, d̃ = 47, d = 49; at 𝗍 = 𝗌, d̃ = 46, d = 48. [[prop:ii-a-9-8]] at
𝗍 ≤ 𝗌 + 1 has d = d̃ + 1 with (𝗍 − m, −N − m): d̃(𝗌 − 1, −15) = 46, d = 47. So d^E = 49.

Hence D_1 = max(49, 41, 39) = 49. ∎

#### A quantitative calculus of finite regularity {#sec:fwd-calculus}

The indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]] come from the closed graph theorem and carry no value. We prove
them again, every derivative counted. Throughout, n = 5, T ∈ ℕ and 𝔐(T) := 200T + 100; Op denotes the left
quantization on ℝⁿ, Op(p)u(x) = (2π)^(−n) ∫ e^(ix·ξ) p(x, ξ) û(ξ) dξ; Q_4 := [−2, 2]ⁿ; and for an integer x, 𝔢(x)
denotes the least even integer above x (so 𝔢(x) = x + 1 for odd x and x + 2 for even x). For an order function 𝗆
(smooth in (x, ξ), with |∂_x^β ∂_ξ^γ 𝗆| ≤ C_(βγ)⟨ξ⟩^(−|γ|), as the variable orders of [[sec:ii-a1-1-1]] are in the
charts of ρℬ) and K ∈ ℕ_0 put

    |p|^𝗆_K := max_(|β|+|γ|≤K) sup ⟨ξ⟩^(−𝗆(x,ξ)−ϰ(|β|+|γ|)+|γ|) |∂_x^β ∂_ξ^γ p(x, ξ)|,          {#eq:fwd-seminorm}

with ϰ := 1/(32𝔐(T)). By Leibniz's rule |pq|^(𝗆_1+𝗆_2)_K ≤ C|p|^(𝗆_1)_K |q|^(𝗆_2)_K; and ⟨ξ⟩^(𝗆(x,ξ)) has
|·|^𝗆_K ≤ C_K for every K, its derivatives carrying factors log⟨ξ⟩ ≤ C⟨ξ⟩^ϰ. A symbol of [[def:ii-a1-1-3]] of any
index ν, written in a chart of ρℬ, satisfies |a|^𝗆_M ≤ C‖a‖_((M);ν,𝗆): by [[lem:ii-a1-2-2]], ∂_ξ is e^(−τ) times
bounded combinations of ∂_ω, ∂_τ, and ⟨log ρ_∞⟩^(νj) ≤ C⟨ξ⟩^(ϰj). The constants depend on ϰ, ν and K, never on the
symbol beyond the seminorm; in particular the index ν enters no count. Every product estimated below is a product of at
most eight symbols (six factors of an expression and two auxiliary symbols λ, λ′), each differentiated at most 𝔐(T)
times (the counts of [[prop:fwd-calculus]]), so that the total loss ϰ·8𝔐(T) in any exponent is at most ¼. Every
statement below holds with the same counts for every smaller ϰ, which is how "order 𝗋 + δ for every δ > 0" is obtained.
A symbol "has order 𝗆" with "values in [−A, A]" when |𝗆| ≤ A; constant orders are included.

*The charts.* Let (U_α, φ_α) be the charts of ρℬ, onto (−2, 2)ⁿ, of finite multiplicity, with transition maps
φ_α ∘ φ_β⁻¹ bounded in C^j uniformly in (α, β) for every j ((S1), (S13)), and χ_α the partition of unity of (S4). As
all scalings of ρℬ equal 1, (S4) gives

    Op(a) = Σ_α O_α(a),     O_α(a) := φ_α^* Op_ψ(a_α) (φ_α)_*,     a_α := (φ_α)_*(χ_α a),             {#eq:fwd-chart-op}

where Op_ψ(b) has the kernel (2π)^(−n) ∫ e^(i(x−y)·ξ) ψ(x − y) b(x, ξ) dξ, ψ ∈ C_c^∞((−¼, ¼)ⁿ) equals 1 near 0, and
a_α vanishes for x ∉ (−5/4, 5/4)ⁿ. The adjoint is that of L²(|dt dx|), which in the chart α is the adjoint of
L²(μ_α dx), μ_α a positive function whose quotients μ_α(x)/μ_α(y) are bounded in C^j on (−2, 2)ⁿ × (−2, 2)ⁿ uniformly in
α ((S2), (S11)). For an order function 𝗆 on the bundle, 𝗆_α denotes its expression in the chart α, extended to
ℝⁿ × ℝⁿ with values in the same interval and with the same bounds; the variable-order Sobolev space H^(𝗆_α)(ℝⁿ) is
normed by ‖Op(⟨ξ⟩^(𝗆_α))w‖ + ‖w‖_(H^(−N_0)) for a fixed N_0 ≥ sup |𝗆_α|, different such N_0 giving equivalent norms
((S8); elliptic regularity of the smooth calculus).

**Lemma {#lem:fwd-crude}** (Boundedness from x-derivatives.) Let p vanish for x ∉ Q_4, let μ, s ∈ ℝ, and suppose that
the bound |∂_(x_l)^j p(x, ξ)| ≤ A⟨ξ⟩^μ for l = 1, …, n and j ≤ N, where N ≥ n + 1 + |s − μ|. Then
‖Op(p)u‖_(H^(s−μ)) ≤ C A ‖u‖_(H^s), C depending on n, s − μ and N.

*Proof.* Let θ ∈ C_c^∞((−3, 3)ⁿ) equal 1 on Q_4 and e_k(x) := e^(iπk·x/3), k ∈ ℤⁿ. On [−3, 3]ⁿ,
p(x, ξ) = Σ_k e_k(x) p̂_k(ξ) with p̂_k(ξ) := 6^(−n) ∫ e_(−k)(x) p(x, ξ) dx, and integrating by parts N times in the
coordinate x_l with |k_l| = max_i |k_i| ≥ |k|/√n gives |p̂_k(ξ)| ≤ C⟨k⟩^(−N) A⟨ξ⟩^μ. So the series converges absolutely
(N > n) and Op(p)u = θ Σ_k e_k p̂_k(D)u, both sides vanishing off Q_4 by the choice of θ. The Fourier multiplier p̂_k(D)
maps H^s to H^(s−μ) with norm sup_ξ |p̂_k(ξ)|⟨ξ⟩^(−μ), and multiplication by θe_k has norm at most C⟨k⟩^(|s−μ|) on
H^(s−μ) (Peetre's inequality, as in [[ch:s03]]). The sum Σ_k ⟨k⟩^(|s−μ|−N) is finite as N − |s − μ| > n. ∎

**Lemma {#lem:fwd-l2}** (Boundedness on L² without loss.) Suppose that, for l = 1, …, n and j ≤ 12,
the pure derivatives satisfy |∂_(x_l)^j p| ≤ A⟨ξ⟩^(ϰj) and |∂_(ξ_l)^j p| ≤ A⟨ξ⟩^(−(1−ϰ)j). Then
‖Op(p)‖_(L²→L²) ≤ CA. In particular ‖Op(p)‖ ≤ C|p|^0_12.

*Proof.* Let ψ_0 + Σ_(j≥1) ψ_j = 1 be a dyadic partition, ψ_j supported in {2^(j−1) ≤ |ξ| ≤ 2^(j+1)} for j ≥ 1,
with derivatives bounded by C2^(−j|γ|). For the shell j put a_j := 2^(−ϰj) and b_j := 2^((1−ϰ)j), so a_jb_j ≥ 1.
With θ, Θ ∈ C_c^∞((−1, 1)ⁿ) such that Σ_m θ(· − m) = Σ_i Θ(· − i) = 1, let I = (j, m, i), p_I(x, ξ) :=
θ(x/a_j − m)Θ(ξ/b_j − i)ψ_j(ξ)p(x, ξ) and T_I := Op(p_I). On supp ψ_j, ⟨ξ⟩ ≤ 2^(j+2), so the hypotheses give
the bounds CAa_j^(−k) for ∂_(x_l)^k p_I and CAb_j^(−k) for ∂_(ξ_l)^k p_I, k ≤ 12. Op(p)u = Σ_I T_I u for u ∈ 𝒮, the sum
converging pointwise, so by the lemma of Cotlar and Stein it suffices to show
sup_I Σ_(I′) ‖T_I^*T_(I′)‖^(1/2) ≤ CA and sup_I Σ_(I′) ‖T_I T_(I′)^*‖^(1/2) ≤ CA.

*T_I T_(I′)^*.* The Fourier transform of T_(I′)^*v is supported in the ξ-support of p_(I′), and T_I w depends only on
ŵ there; so T_I T_(I′)^* = 0 unless the ξ-supports meet, which forces |j − j′| ≤ 1, comparable boxes and boundedly many
i′ for given I. Its kernel is K(x, y) = (2π)^(−n) ∫ e^(i(x−y)·ξ) p_I(x, ξ) \overline{p_(I′)(y, ξ)} dξ. Integrating by
parts twelve times in ξ_l, (x_l − y_l)^12 K is bounded by CA²b^(n−12), b := b_j; with 1 + Σ_l (b|x_l − y_l|)^12 ≥
c(1 + b|x − y|)^12 this gives |K| ≤ CA²bⁿ(1 + b|x − y|)^(−12), K vanishing unless x and y lie in the x-boxes of I and
I′ (side 2a, a := a_j). Schur's test gives ‖T_I T_(I′)^*‖ ≤ CA² when the boxes are within distance 3a, and
≤ CA²(ab)^(n−12)⟨m − m′⟩^(−12) ≤ CA²⟨m − m′⟩^(−12) otherwise. Since 12/2 > n, the sum over I′ is at most CA.

*T_I^*T_(I′).* On the Fourier side its kernel is L(ξ, η) = ∫ e^(ix·(η−ξ)) \overline{p_I(x, ξ)} p_(I′)(x, η) dx, which
vanishes unless the x-boxes meet. Integrating by parts twelve times in x_l, with a̲ := min(a_j, a_(j′)), we obtain the
bound CA²a̲ⁿ(1 + a̲|ξ − η|)^(−12) for |L|. If |j − j′| ≤ 2 the scales are comparable and Schur's test over the
ξ-boxes gives, as before, a bound CA²⟨i − i′⟩^(−12), summable to CA. If |j − j′| ≥ 3, |ξ − η| ≥
2^(J−2) with J := max(j, j′), so |L| ≤ CA²2^(−ϰJn)2^(−12(1−ϰ)J) and ‖T_I^*T_(I′)‖ ≤ CA²2^(−ϰJn)2^(−(1−ϰ)J(12−n)); the
number of I′ in the shell j′ meeting the x-box of I is at most C2^(2ϰJn). The contribution of the shell j′ is therefore
at most CA2^(J(2ϰn − (1−ϰ)(12−n)/2)) ≤ CA2^(−J), as 2ϰn ≤ 5/4 and (1 − ϰ)(12 − n)/2 ≥ 49/16. Summed over j′ this is
at most CA. ∎

**Lemma {#lem:fwd-composition}** (Composition with remainder.) Let p, q be symbols whose seminorms
[[eq:fwd-seminorm]] at the orders 𝗆_1, 𝗆_2 and the regularities K_1, K_2 are finite, μ_i := sup 𝗆_i, J ≥ 1 and B ≥ 0.
Then Op(p)Op(q) = Op(p ♯_J q) + Op(r_J) with

    p ♯_J q := Σ_(|α|<J) (α!)⁻¹ ∂_ξ^α p · D_x^α q,
    |∂_x^β r_J(x, ξ)| ≤ C|p|^(𝗆_1)_(K_1)|q|^(𝗆_2)_(K_2) ⟨ξ⟩^(μ_1+μ_2−J+½),   |β| ≤ B,         {#eq:fwd-remainder}

provided K_1 ≥ J + B + 6 and K_2 ≥ J + B + 2L′, where 2L′ := 𝔢(n + 1 + X) for an integer X ≥ |μ_1 − J|; if q
vanishes for x ∉ Q_4 the condition on K_1 is K_1 ≥ J + B. The term of p ♯_J q of index α has the pointwise order
𝗆_1 + 𝗆_2 − |α|, and its derivatives of order K are bounded by C|p|^(𝗆_1)_(K+|α|)|q|^(𝗆_2)_(K+|α|) with the loss
ϰ(K + 2|α|).

*Proof.* Op(p)Op(q) = Op(c) with c(x, ξ) = (2π)^(−n) ∫∫ e^(−iy·η) p(x, ξ + η) q(x + y, ξ) dy dη. Taylor's formula in η
to order J and η^α e^(−iy·η) = (i∂_y)^α e^(−iy·η), integrated by parts onto q, give the terms of p ♯_J q and

    r_J = Σ_(|α|=J) (J/α!) ∫_0^1 (1 − θ)^(J−1) r_(α,θ) dθ,
    r_(α,θ)(x, ξ) := (2π)^(−n) ∫∫ e^(−iy·η) ∂_ξ^α p(x, ξ + θη) D_x^α q(x + y, ξ) dy dη.

Apply ∂_x^β. Insert ⟨η⟩^(−2L′)(1 − Δ_y)^(L′) and ⟨y⟩^(−6)(1 − Δ_η)^3 (the latter only when q is not compactly supported
in x) acting on e^(−iy·η), and integrate by parts. The η-derivatives fall on ∂_ξ^α ∂_x^(β_1) p, at most J + 6 + B
derivatives, each bounded by C|p|⟨ξ + θη⟩^(μ_1 − J + ¼); the y-derivatives fall on ∂_x^(α+β_2) q, at most J + B + 2L′
derivatives, each bounded by C|q|⟨ξ⟩^(μ_2 + ¼). Peetre's inequality ⟨ξ + θη⟩^t ≤ 2^(|t|/2)⟨ξ⟩^t⟨η⟩^(|t|) and
2L′ > n + |μ_1 − J + ¼| make the η-integral at most C⟨ξ⟩^(μ_1−J+¼), and the y-integral is finite (over a bounded set
when q vanishes for x ∉ Q_4, and by ⟨y⟩^(−6), 6 > n, otherwise). This is [[eq:fwd-remainder]]. The statement on the
terms is Leibniz's rule. ∎

**Lemma {#lem:fwd-reduction}** (Reduction of an amplitude.) Let c(x, y, η) vanish unless x ∈ Q_4 and |x − y| ≤ 1, let
μ be a constant, and suppose |∂_x^β ∂_y^(β′) ∂_η^γ c| ≤ A⟨η⟩^(μ−|γ|+ϰ(|β|+|β′|+|γ|)) for |β| + |β′| + |γ| ≤ K_c.
Let R_c be the operator with the kernel (2π)^(−n) ∫ e^(i(x−y)·η) c(x, y, η) dη. For J ≥ 0 and B ≥ 0,

    R_c = Op(σ_J) + Op(ρ_J),     σ_J(x, η) := Σ_(|γ|<J) (γ!)⁻¹ ∂_η^γ D_y^γ c(x, y, η)|_(y=x),
    |∂_x^β ρ_J(x, η)| ≤ CA⟨η⟩^(μ−J+½),   |β| ≤ B,                                                      {#eq:fwd-reduction}

provided K_c ≥ 2J + B + 2L′ with 2L′ := 𝔢(n + 1 + X), X ≥ |μ − J| an integer. The term of σ_J of index γ is a sum of
products of derivatives of c of total order 2|γ|, evaluated at y = x; its derivatives of order K involve derivatives of
c of total order at most K + 2|γ|. If c vanishes near {x = y}, then σ_J = 0.

*Proof.* R_c u(x) = ∫ e^(ix·η) σ(x, η) û(η) dη with σ(x, η) = (2π)^(−n) ∫∫ e^(−iz·ζ) c(x, x + z, η + ζ) dz dζ, the
z-integral being over |z| ≤ 1. Taylor's formula in ζ to order J and ζ^γ e^(−iz·ζ) = (i∂_z)^γ e^(−iz·ζ), integrated by
parts in z, give σ = σ_J + ρ_J with

    ρ_J = Σ_(|γ|=J) (J/γ!) ∫_0^1 (1 − θ)^(J−1) (2π)^(−n) ∫∫ e^(−iz·ζ) ∂_η^γ D_z^γ [c(x, x + z, η + θζ)] dz dζ dθ.

Apply ∂_x^β, which falls on both arguments x and x + z, and insert ⟨ζ⟩^(−2L′)(1 − Δ_z)^(L′) acting on e^(−iz·ζ). In
all, c is differentiated J times in η, J + 2L′ times in z (that is, in its second argument) and |β| ≤ B times in its
first two arguments: at most 2J + B + 2L′ derivatives, each term bounded by CA⟨η + θζ⟩^(μ−J+¼) on |z| ≤ 1. Peetre's
inequality and 2L′ − |μ − J + ¼| > n bound the ζ-integral by C⟨η⟩^(μ−J+¼). The last claim: every term of σ_J contains
derivatives of c at y = x. ∎

The reduction serves three purposes below: the adjoint, the change of chart, and the parts of a kernel away from the
diagonal. In each, the derivatives of c that it consumes are counted as derivatives of the symbol from which c is built.

**Lemma {#lem:fwd-far}** (Away from the diagonal.) Let b vanish for x ∉ Q_4, with |∂_x^j ∂_ξ^γ b| ≤ A⟨ξ⟩^(μ−|γ|) for
j ≤ B and |γ| ≤ 2K, μ a constant, and let w ∈ C_c^∞(ℝⁿ) vanish near 0. The operator with the kernel
(2π)^(−n) ∫ e^(i(x−y)·ξ) w(x − y) b(x, ξ) dξ is Op(b_w) with |∂_x^j b_w| ≤ CA⟨ξ⟩^(μ−2K) for j ≤ B. It consumes 2K
ξ-derivatives and B x-derivatives of b, and none in the other directions. Also Op_ψ(b) = Op(b_ψ) with
b_ψ(x, ξ) := (2π)^(−n) ∫ ψ̂(ζ) b(x, ξ − ζ) dζ, and |b_ψ|^𝗆_K ≤ C|b|^𝗆_K for every K and every order function 𝗆 with
values in [−3T, 3T]: the cut-off ψ consumes no derivative.

*Proof.* On supp w, |z|^(−2K)(−Δ_ξ)^K e^(iz·ξ) = e^(iz·ξ), z = x − y, so the kernel is that of the amplitude
w_K(x − y)(−Δ_ξ)^K b(x, ξ), w_K(z) := w(z)|z|^(−2K) ∈ C_c^∞. Multiplication of a kernel by a function of x − y is
convolution of the symbol in ξ with its Fourier transform: the operator is Op(b_w), b_w(x, ξ) = (2π)^(−n)
∫ ŵ_K(ζ)(−Δ_ξ)^K b(x, ξ − ζ) dζ. x-derivatives commute with the convolution, ŵ_K is rapidly decreasing, and Peetre's
inequality gives the bound. The same identity with ψ in place of w_K gives b_ψ. For the variable weight, if
|ζ| ≤ ⟨ξ⟩/2 then |𝗆(x, ξ − ζ) − 𝗆(x, ξ)| ≤ C|ζ|/⟨ξ⟩, so ⟨ξ − ζ⟩^(𝗆(x,ξ−ζ)) ≤ C⟨ξ⟩^(𝗆(x,ξ)) when
|ζ| ≤ ⟨ξ⟩^(1/2) and ≤ C⟨ξ⟩^(𝗆(x,ξ))⟨ζ⟩^(C′) when ⟨ξ⟩^(1/2) < |ζ| ≤ ⟨ξ⟩/2; if |ζ| > ⟨ξ⟩/2 both ⟨ξ⟩ and ⟨ξ − ζ⟩
are at most 3⟨ζ⟩, and the quotient is at most C⟨ζ⟩^(6T). These polynomial factors are integrable against ψ̂. ∎

*Near and far parts.* Fix ε ∈ (0, 1/8], depending only on the constants of (S1) and (S15), as below, and
η_0 ∈ C_c^∞((−ε, ε)ⁿ) equal to 1 near 0. Split O_β(g) = O^ε_β(g) + O^far_β(g), the near part having the kernel of
Op_ψ(g_β) multiplied by η_0(x − y), and split the adjoint O_β(g)^* likewise. By [[lem:fwd-far]] with
w := ψ(1 − η_0), O^far_β(g) is φ_β^* Op(b_w) (φ_β)_* with b_w of order sup 𝗆 − 2K, at the cost of 2K ξ-derivatives and
B x-derivatives of g; (O^far_β(g))^* is its adjoint, bounded by duality between the dual spaces ((S3), (S8)), at the
same cost. The near kernels have ranges at most Cε in d_ℬ ((S15)).

**Lemma {#lem:fwd-transport}** (Change of chart, term by term.) Let α, β be charts, κ := φ_β ∘ φ_α⁻¹ (defined where
both are), θ ∈ C_c^∞((−13/8, 13/8)ⁿ), and g a symbol of order 𝗆 with values in [−T, T]. In the chart α the operators
θ O^ε_β(g) and θ O^ε_β(g)^* (the factor θ read in the chart α) are R_c for the amplitudes

    c(x, y, η) = θ(x) η̃(x, y) g_β(κ(x), Φ(x, y)^(−T) η) |det Φ(x, y)|⁻¹ |det Dκ(y)|,
    c^*(x, y, η) = θ(x) η̃^*(x, y) (μ_α(y)/μ_α(x)) g_β(κ(y), Φ(x, y)^(−T) η)^* |det Φ(x, y)|⁻¹ |det Dκ(x)|,  {#eq:fwd-transport}

where Φ(x, y) := ∫_0^1 Dκ(y + t(x − y)) dt, so that κ(x) − κ(y) = Φ(x, y)(x − y), the star on g is the conjugate
transpose, and η̃(x, y) := (ψη_0)(Φ(x, y)(x − y)), η̃^*(x, y) := \overline{(ψη_0)(Φ(x, y)(y − x))}. Each derivative of
c or c^* in (x, y, η) costs at most one derivative of g, and the bounds of [[lem:fwd-reduction]] hold with μ := sup 𝗆
and A := C|g|^𝗆_(K_c). The transition map κ is differentiated at most K_c + 1 times. The term of σ_J of index 0 is
θ (χ_β g)_α, resp. θ ((χ_β g)^*)_α, the same function on phase space read in the chart α; the term of index γ has the
pointwise order 𝗆 − |γ| and consumes 2|γ| derivatives of g, the variable order being carried exactly, as every term is
evaluated at y = x, that is, at the point of phase space with the chart-α coordinates (x, η).

*Proof.* Let ε be so small that every point within Cε of supp θ ∩ φ_α(supp χ_β) has its segment to x inside the
domain of κ and inside (−7/4, 7/4)ⁿ, and that ‖Φ(x, y) − Dκ(x)‖ ≤ ½‖Dκ(x)⁻¹‖⁻¹ there; this is possible uniformly in
(α, β), as supp χ_β ⊂ φ_β⁻¹([−5/4, 5/4]ⁿ) and by (S1), (S15). The kernel of θO^ε_β(g) in the chart α is
θ(x)K(κ(x), κ(y))|det Dκ(y)| with K that of Op_(ψη_0)(g_β); substituting ξ = Φ(x, y)^(−T)η, as
(κ(x) − κ(y))·ξ = (x − y)·Φ^Tξ, gives c. For the adjoint of O^ε_β(g), the kernel is μ_α(x)⁻¹ \overline{K^#(y, x)}
μ_α(y) with K^#(y, x) = K(κ(y), κ(x))|det Dκ(x)|; as κ(y) − κ(x) = −Φ(x, y)(x − y), the same substitution gives c^*
after multiplication by θ(x). The variable η enters c and c^* only through the second argument of g. So a derivative
in η is a ξ-derivative of g times an entry of Φ^(−T) (one order lower); a derivative in x or y falls on θ, η̃, the
Jacobians and the quotient of densities (smooth, with derivatives of κ), on the first argument of g (an x-derivative of
g times an entry of Dκ), or on Φ^(−T)η (a ξ-derivative of g times a factor linear in η and in a derivative of Φ, which
leaves the order unchanged). By induction, a derivative of order K_c of c or c^* is a sum of products of one derivative
of g of order at most K_c with derivatives of κ of order at most K_c + 1 (k derivatives of Φ involve those of Dκ of
order k), and its bound is that of [[lem:fwd-reduction]] with A := C|g|^𝗆_(K_c), the constant depending on bounds of κ
in C^(K_c+1), uniform by (S1). At y = x, Φ(x, x) = Dκ(x), η̃ = 1 and the Jacobians cancel, which gives the term of
index 0. A term of index γ has |γ| derivatives in η and |γ| in y: 2|γ| derivatives of g, and the order 𝗆 − |γ| by the
count of orders just given, at the point (κ(x), Dκ(x)^(−T)η). ∎

Each change of chart thus consumes, of the transition map, one derivative more than it consumes of the symbol, and
of the symbol: 2|γ| derivatives in the term of index γ, K + 2|γ| when that term is differentiated K times later, and
2J + B + 2L′ in the remainder ρ_J of [[lem:fwd-reduction]]. The same holds for the adjoint in its own chart (α = β,
κ = id), where it is the reduction of the amplitude c^*.

**Lemma {#lem:fwd-local}** (Boundedness in a chart.) Let A, B ∈ ℕ_0 and put J_1 := 2A + 2B + 1, J_2 := 2A + 1 and

    K(A, B) := J_1 + 6 + 𝔢(n + 1 + J_1 + A + B).                                                       {#eq:fwd-local}

Let b vanish for x ∉ Q_4 and have order 𝗆 with values in [−B, B], and let 𝗍 be an order function with values in
[−A, A]. Then ‖Op(b)w‖_(H^(𝗍−𝗆)(ℝⁿ)) ≤ C|b|^𝗆_(K(A,B)) ‖w‖_(H^𝗍(ℝⁿ)). For A = B = T, K(T, T) = 10T + 15.

*Proof.* Let λ := ⟨ξ⟩^(𝗍(x,ξ)−𝗆(x,ξ)), Λ := Op(⟨ξ⟩^(𝗍)) and λ′ ∈ S^(−𝗍) a smooth symbol with Op(λ′)Λ = I + R_∞,
R_∞ of order −∞ (smooth calculus). Norm H^(𝗍−𝗆) with N_0 := A + B. Then
Op(λ)Op(b)w = QΛw − Op(λ)Op(b)R_∞w with Q := Op(λ)Op(b)Op(λ′).
Step 1. [[lem:fwd-composition]] with p := λ (order with values in [−A − B, A + B]), q := b (vanishing off Q_4), J := J_1
and B := 6 gives Op(λ)Op(b) = Op(c_1) + Op(r_1), r_1 of order at most (A + B) + B − J_1 + ¾ = −A − ¼. Op(λ′) maps L² to
H^𝗍 ⊂ H^(−A), and [[lem:fwd-crude]] (s = −A, μ = −A, N = 6) maps H^(−A) to L². Cost on b: J_1 + 6 + 2L′ with
2L′ = 𝔢(n + 1 + J_1 + A + B), as |sup(𝗍 − 𝗆) − J_1| ≤ J_1 + A + B; this is K(A, B).
Step 2. [[lem:fwd-composition]] with p := c_1 (order 𝗍, values in [−A, A]), q := λ′ (not compactly supported), J := J_2
and B := 6 gives Op(c_1)Op(λ′) = Op(c) + Op(r_2), r_2 of order at most 2A − J_2 + ¾ < 0, bounded on L² by
[[lem:fwd-crude]] (N = 6). Cost on c_1: J_2 + 12, on b: J_2 + 12 + (J_1 − 1) = 4A + 2B + 13 ≤ K(A, B).
Step 3. c = Σ ∂_ξ^(α′)(∂_ξ^α λ · D_x^α b) D_x^(α′) λ′/(α!α′!) has the pointwise order (𝗍 − 𝗆) + 𝗆 − 𝗍 − |α| − |α′|,
the variable orders cancelling at every point; [[lem:fwd-l2]] bounds Op(c) on L² by C|c|^0_12, at a cost on b of
12 + (J_1 − 1) + (J_2 − 1) = 4A + 2B + 12.
Step 4. ‖Op(b)w‖_(H^(−A−B)) ≤ C‖w‖_(H^(−A)) and ‖Op(λ)Op(b)R_∞w‖ ≤ C‖Op(b)R_∞w‖_(H^(A+B)) ≤ C‖w‖_(H^(−N_0)) by
[[lem:fwd-crude]], at most n + 1 + A + B x-derivatives of b.
The largest count is that of Step 1. For A = B = T: J_1 = 4T + 1, 2L′ = 𝔢(6T + 7) = 6T + 8, K = 10T + 15. ∎

**Lemma {#lem:fwd-norms}** (Localisation of the norms.) For an order function 𝗋 with values in [−8T, 8T], cut-offs
θ̃_α := φ_α^*θ̃ (θ̃ ∈ C_c^∞((−15/8, 15/8)ⁿ) equal to 1 on [−7/4, 7/4]ⁿ) and functions v_α supported in [−15/8, 15/8]ⁿ,

    ‖Σ_α φ_α^* v_α‖²_𝗋 ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)(ℝⁿ)),       Σ_α ‖(φ_α)_*(θ̃_α u)‖²_(H^(𝗋_α)(ℝⁿ)) ≤ C ‖u‖²_𝗋.

Both statements concern the smooth calculus only, (S3) for constant orders and (S8), (S13), (S15) for variable ones,
and involve no symbol of finite regularity.

**Lemma {#lem:fwd-expansion}** (A product in a chart.) Let r ∈ {1, …, 6}, S ≥ 0 an integer, and F_1, …, F_r each of
the form Op(g_j) or Op(g_j)^*, the symbol g_j of order 𝗆_j with values in [−T, T] (smooth symbols, such as those of
localisers, are allowed). Put

    R := S + rT,   B := n + 1 + max((r + 1)T, S + (r − 1)T),   J_R := T + R + 1,   J_C := rT + R + 1,
    2K := the least even integer ≥ T + R + 1.                                                         {#eq:fwd-expansion}

For each chart α let s_j be the sum over β of the terms of index < J_R of the reductions of θ^(j) O^ε_β(g_j) (resp. of
the adjoints) in the chart α ([[lem:fwd-transport]]), θ^(1) := χ_α and θ^(j) := θ̂ for j ≥ 2, θ̂ ∈ C_c^∞((−13/8, 13/8)ⁿ)
equal to 1 on [−3/2, 3/2]ⁿ, and let t_α := s_1 ♯_(J_C) s_2 ♯_(J_C) ⋯ ♯_(J_C) s_r, computed from the left. Then

    F_1 ⋯ F_r = Σ_α φ_α^* Op(t_α) (φ_α)_* θ̃_α + E,                                                  {#eq:fwd-product}

where E maps H^𝗍 to H^S, for every order 𝗍 with values in [−T, T], with norm at most C ∏_j |g_j|^(𝗆_j)_(K_j), and the
derivatives of each g_j consumed in E are at most

    max( 2J_R + B + 𝔢(n + 1 + J_R + T),  2K + B,  B + 2(J_R − 1),
         (J_C + B) + (r − 2)(J_C − 1) + 2(J_R − 1),  J_C + B + 𝔢(n + 1 + J_C + (r − 1)T) + 2(J_R − 1) ),      {#eq:fwd-ecount}

the last two only if r ≥ 2. A derivative of order K′ of t_α consumes at most K′ + (r − 1)(J_C − 1) + 2(J_R − 1)
derivatives of each g_j. Each term of t_α is a product of derivatives of the terms of the s_j at one point (x, η); its
grade, the sum of the indices |γ| of the reductions and of the indices |α| of the compositions that produced it, lowers
the pointwise order Σ_j 𝗆_j by exactly that number.

*Proof.* Write F_j = F^ε_j + F^far_j, the sums over β of the near and far parts. The product of the near parts is
Σ_α χ_α F^ε_1 ⋯ F^ε_r, and the kernel of χ_α F^ε_1 ⋯ F^ε_r joins points within rCε ≤ 1/8 in d_ℬ of supp χ_α, inside
φ_α⁻¹([−3/2, 3/2]ⁿ) for ε small; so inserting θ̂ in front of F^ε_j, j ≥ 2, and θ̃_α on the right changes nothing. In the
chart α, by [[lem:fwd-reduction]] and [[lem:fwd-transport]] with J := J_R, each θ^(j)F^ε_j is Op(s_j) + Op(ρ_j), ρ_j of
order at most T − J_R + ½ = −R − ½. Expanding, the product is Op(s_1)⋯Op(s_r) plus terms with a factor Op(ρ_j). By
[[lem:fwd-composition]] (q vanishing off Q_4) with J := J_C applied r − 1 times from the left,
Op(s_1)⋯Op(s_r) = Op(t_α) + Σ_(j≥2) Op(r_j) Op(s_(j+1)) ⋯ Op(s_r), r_j of order at most jT − J_C + ¾ ≤ −R − ¼. The far
terms are products with at least one factor F^far_j, of order at most T − 2K + ½ ≤ −R − ½ ([[lem:fwd-far]]).

So every term of E is a product of at most r operators, one of order at most −R (the gaining factor) and the others of
order at most T, which we bound between Sobolev spaces of constant order by [[lem:fwd-crude]], chart by chart, and on
the manifold by (S3); adjoints by duality. Start from H^𝗍 ⊂ H^(−T). The factors to the right of the gaining factor lower
the order by at most T each, the gaining factor raises it by R, the others lower it by at most T: the result lies in
H^(−T−(r−1)T+R) = H^S. The input orders s of the factors of order at most T lie in [−rT, R − T], so |s − T| ≤
max((r + 1)T, R − 2T); that of the gaining factor lies in [−rT, −T], so |s + R| ≤ R − T = S + (r − 1)T. So B
x-derivatives suffice in every application of [[lem:fwd-crude]].

The counts, all derivatives of g_j: ρ_j costs 2J_R + B + 2L′ with 2L′ = 𝔢(n + 1 + J_R + T) ([[lem:fwd-reduction]], as
|sup 𝗆_j − J_R| ≤ J_R + T); a far part costs 2K + B ([[lem:fwd-far]]); a factor Op(s_j) bounded by [[lem:fwd-crude]]
costs B + 2(J_R − 1) ([[lem:fwd-transport]]). In the composition of t_(j−1) := s_1 ♯ ⋯ ♯ s_(j−1) with s_j, the left
symbol needs J_C + B derivatives and the right one J_C + B + 2L′_C, 2L′_C = 𝔢(n + 1 + J_C + (j − 1)T), since
|sup ord t_(j−1) − J_C| ≤ J_C + (j − 1)T. The symbol t_(j−1) already contains, on s_i, at most (j − 2)(J_C − 1)
derivatives (ξ-derivatives from the j − 2 compositions in which it stood on the left, or x-derivatives from the one in
which it stood on the right and ξ-derivatives from the later ones), and s_i contains 2(J_R − 1) derivatives of g_i. With
j ≤ r this gives the last two entries of [[eq:fwd-ecount]], and the statement on t_α. The grades are those of
[[lem:fwd-composition]] and [[lem:fwd-transport]]. ∎

**Proposition {#prop:fwd-calculus}** (Explicit indices.) Let T ∈ ℕ and put 𝔐(T) := 200T + 100. For orders 𝗍, 𝗆,
𝗆_i (constant or variable) with values in [−T, T], index ν ≤ 2, and expressions in at most six quantizations,
[[prop:ii-a1-2-4]] (a)–(f) hold with M + 2 = 𝔐(T), and [[lem:ii-a-8-5]] (a) and (b) hold with d_0 = 𝔐(T). In (e) the
number N of that item may be any N ≤ T.

*Proof.* *Reduction to charts.* By (S3)–(S5), (S8) and (S13), for a fixed elliptic Λ_𝗍 ∈ Ψ̃^𝗍 with symbol ρ_∞^(−𝗍),
‖v‖_𝗍 is equivalent to ‖Λ_𝗍v‖ + ‖v‖_(−3T), and the norms localise to the charts of ρℬ: Λ_𝗍 restricted to functions
supported in a chart is the chart quantization of a smooth symbol plus a residual operator, uniformly over the charts,
and sums over the charts are controlled by their finite multiplicity. These are statements of the smooth calculus and
enter only constants. Op(a) is the sum over the charts of local quantizations Op_β((ψ_β)_*(χ_β a)), with x-support in
(−5/4, 5/4)ⁿ, and the cut-off ψ(x − x′) of (S4) turns each into Op of a symbol with the same seminorms
[[eq:fwd-seminorm]] (convolution in ξ with the Schwartz function ψ̂/(2π)ⁿ; the variable order is handled by
⟨ξ − η⟩^(𝗆(x,ξ−η)) ≤ C⟨ξ⟩^(𝗆(x,ξ))⟨η⟩^(2T+1)). Smooth operators, cut-offs and residual operators are moved between
charts freely; only the finite-regularity factors are counted.

*(a).* In one chart, with smooth symbols λ of order 𝗍 − 𝗆 and λ′ of order −𝗍 (a parametrix of Λ_𝗍), consider
Q := Op(λ)Op(a)Op(λ′) on L². By [[lem:fwd-composition]] with J_1 := 4T + 1 and B = n + 1 = 6, Op(λ)Op(a) = Op(c_1) +
Op(r_1), and the order of r_1 is at most 3T − J_1 + ½ < −T; here a is the factor q, with compact x-support, and needs
J_1 + 6 + 2L′_1 derivatives, 2L′_1 = 6T + 8, that is 10T + 15. Op(r_1)Op(λ′) is bounded on L² by [[lem:fwd-crude]]
(from H^(−T) to L², N = 6), as Op(λ′) maps L² to H^𝗍 ⊂ H^(−T). Next Op(c_1)Op(λ′) = Op(c) + Op(r_2) with J_2 :=
2T + 1; r_2 has order ≤ sup 𝗍 − inf 𝗍 − J_2 + ½ < 0 and is bounded on L² by [[lem:fwd-crude]], at a cost of
J_2 + 12 derivatives of c_1, that is 6T + 13 of a. The main symbol c = Σ ∂_ξ^(α′)(∂_ξ^α λ · D_x^α a) D_x^(α′)λ′/(α!α′!)
has pointwise order (𝗍 − 𝗆) + 𝗆 − 𝗍 − |α| − |α′| ≤ 0, the variable orders cancelling at every point, so that the
seminorm of c of order 0 and regularity 12 is at most C|a|^𝗆_(J_1+J_2+10), and [[lem:fwd-l2]] bounds Op(c) on L²
without loss. The terms with residual factors and the low norm ‖Op(a)u‖_(−3T) are bounded by [[lem:fwd-crude]] at
constant orders in [−3T, 3T], with at most 3T + 7 derivatives. So (a) holds with 10T + 15 derivatives, without
loss. Multiplication by ℓ is Op(ℓ) ((S4), [[eq:ii-a1-1-1]]), so [[lem:ii-a-8-5]] (a) holds with
d_0 = 10T + 15, and its b-regularity part follows by Leibniz's rule as there.

*(b)–(d).* Op(a_1)Op(a_2) − Op(a_1a_2) is a sum over pairs of charts. In a pair, the local operator of a_2 is
expressed in the chart of a_1: with κ the transition and κ(x) − κ(x′) = Φ(x, x′)(x − x′), the substitution
ξ = Φ^(−T)η and the reduction of the amplitude to a left symbol, expanded to J_T := 6T + 2 terms with a remainder of
order ≤ −5T, give the symbol of the transported operator as q̂ + q_1, where q̂ is a_2 at the image point under the
canonical transformation (the same function on phase space) and q_1 has order 𝗆_2 − 1 + ¼ϰ′ for every small ϰ′, at a
cost of at most 2J_T + 2L′ + 12 ≤ 30T + 30 derivatives of a_2; the part of the kernel cut-off away from the diagonal
has order ≤ −5T at a cost of 5T + 7 ξ-derivatives. Then [[lem:fwd-composition]] with J := 6T + 2 gives the terms
Σ_(1≤|α|<J), of exact variable order 𝗆_1 + 𝗆_2 − |α| up to the factor ⟨ξ⟩^(2ϰ|α|), which (a) bounds as one symbol of
order 𝗆_1 + 𝗆_2 − 1 + δ at regularity 10(2T + 1) + 15 + J, and a remainder of order ≤ −4T − 1, which
[[lem:fwd-crude]] bounds from H^(−T) to H^(3T+1) with 3T + 7 derivatives. Each a_i needs at most 26T + 27 derivatives
here, and at most 30T + 30 with the transport. (c) is the same with the adjoint expansion, the density factor and the
weight being smooth; (d) is (b) to one more term, the scalar factor H_(a_1)a_2 being the second term exactly.

*(e), (f).* An expression T(a_1, …, a_r), r ≤ 6, is expanded factor by factor: each composition by
[[lem:fwd-composition]] with J := 2(r + 2)T + 2, each adjoint likewise, each transport as in (b). The formal symbol
t is a finite sum of products of derivatives of the a_i, and T − Op(t) has order ≤ −(r + 2)T; it is bounded by
[[lem:fwd-crude]]. In (f) the hypothesis is used in the following form: the terms of t of formal order above μ cancel
identically, as polynomials in the derivatives of the a_i. This holds for the expressions to which (f) is applied in
the edition, which are commutators with scalar symbols, differences of an adjoint and the quantization of the
conjugate symbol, and their composites, whose leading terms cancel by commutativity of scalar products and by
Op(a)^* = Op(ā) + (order m − 1). The remaining terms are bounded by (a) as one symbol of order μ + δ, with box
(r + 1)T + 1. In (e), every term of t is a product containing a derivative of the symbol of B_1 and one of B_2 at the
same point, so t = 0 by the disjointness of the supports, and only the remainder, of order ≤ −N, is left. The
derivative counts are at most 10((r + 1)T + 1) + 15 + r(2(r + 2)T + 2) ≤ 166T + 37 for r ≤ 6. [[lem:ii-a-8-5]] (b) is
(e) with the expression B ℓ (I − B^♯) and N ≤ T.

In every case the count is at most 166T + 37 ≤ 𝔐(T) − 2 and the number of derivatives taken of any symbol is at most
D_max = 400T + 200, which justifies the choice of ϰ. ∎

#### The orders that occur, and the increments {#sec:fwd-box}

**Lemma {#lem:fwd-box}** (The order box.) In the proofs of the results that fix D_0 for the operator of
[[thm:iii-i-5-3]], namely [[thm:ii-e-6-1]] at (𝗌_0, 𝗌), [[prop:ii-e-3-4]], [[prop:ii-e-4-3]] and [[prop:ii-e-4-4]] at
the slab orders 𝗌, 𝗌 + 1, 𝗌 + 2, 𝗌 + 3, [[prop:ii-e-3-4]] (i) at s′ = s_u, and [[lem:ii-f1-2-8]], together with the
results of [[ch:s04]] and [[ch:s06]] they invoke, every Sobolev order and every symbol order at which
[[prop:ii-a1-2-4]], [[lem:ii-a-8-5]] or [[lem:ii-a-8-6]] is applied lies in [−100, 100], every index is at most 2,
and every expression has at most six factors.

*Proof.* The orders of the estimates themselves lie in [−15, 15]: 𝗌 ∈ [−10, 11], shifts by at most 3 above and the
order 𝗌_0 = 𝗌 − 3 and s_u − 3 = −15 below ([[lem:fwd-orders]]); the error orders are −N with N ≤ 15 (N = 13 in the
global estimates, s_u − 3 ≥ −15 in the uniqueness and duality steps of [[prop:ii-e-3-4]]). In [[thm:ii-a1-3-1]] at
(m, 𝗌, N) the Sobolev orders are 𝗌 − j/2 ≥ −N − 1 and the symbol orders lie in [−(sup 𝗌 + N) − m − 1, m]. In
[[thm:ii-a1-5-4]], [[lem:ii-a1-4-2]] runs over 𝗌_j ∈ [𝗌 − τ, 𝗌] with τ = max(1, sup 𝗌 + N) ≤ 30, so |𝗌_j| ≤ 45; the
commutant of [[prop:ii-a1-5-3]] has order 𝗄 = 𝗌_j − (m − 1)/2, and the symbols that occur (ǎ², H_ℓ(ǎ²), b_ε², the
operators C_ǎ, with factors of order m or m − 1) have orders in [2𝗄 − 1, 2𝗄 + m] ⊂ [−94, 94]; the Sobolev orders are
𝗌_j − ½ + δ, ±(m − 1)/2 and K′ ≤ sup |𝗌_j| + m + 2 ≤ 49, the regularisers T_t being smooth. The radial and
trapped-set estimates of [[ch:s06]] and [[prop:ii-e-3-2]] use constant orders in [s_0 − 3, s + 3] with s, s_0 among
the orders above, commutants of order k = s − (m − 1)/2 lowered by κ ≤ 2, and the iteration of [[lem:ii-d-2-2]],
which is that of [[lem:ii-a1-4-2]]; their orders lie in the same ranges. The indices are 0 or 1, raised by one at most
by [[lem:ii-a1-2-5]] (ii). The longest expressions are those of the commutator paragraph of [[prop:ii-a1-5-3]] and of
[[lem:ii-d-2-3]], such as i[L_R, D_ǎǍ] and Ǎ^*[Ǎ, L_I], with at most six quantizations after the localisers are
counted. ∎

**Lemma {#lem:fwd-increments}** (The increments.) Every coefficient index entering D_0 is at most 𝔐(100) + 4.

*Proof.* Every such index is, by its proof, a maximum of indices of [[prop:ii-a1-2-4]] (as M + 2),
[[lem:ii-a-8-5]] and [[lem:ii-a-8-6]] at orders in the box of [[lem:fwd-box]], raised by at most 4: by 2 in
[[thm:ii-a1-5-4]] (the flow box has d_0 − 1 derivatives and the commutant symbols d_0 − 2, so d_0 − 2 ≥ M′ + 2), by 4
at the trapped set of [[ch:s06]] (symbols in C^(d_0−4) S̃^0), by 2 in [[lem:ii-d1-2-4]] and [[prop:ii-e-4-4]]
(d_0 ≥ d_1 + 2, d_1 the index of [[prop:ii-a-9-6]], which is that of [[lem:ii-a-8-5]] (a) and (b)), and by 0 in
[[thm:ii-a1-3-1]], [[prop:ii-a-9-1]], [[prop:ii-a-9-2]] and [[lem:ii-a-8-6]], which take maxima. The energy estimates of
[[ch:s07]] need d_0 = 2 ([[lem:ii-e-2-5]], [[prop:ii-e-2-7]]). [[lem:ii-d-4-1]] asks d_0 ≥ 5. All are at most
𝔐(100) + 4 by [[prop:fwd-calculus]] with T = 100. ∎

*Proof of [[thm:fwd-loss]].* By [[lem:fwd-increments]], D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) ≤ 𝔐(100) + 4 =
20,104. By [[lem:fwd-orders]] and [[lem:fwd-tame]], d′ = 10, d″ = 11 and D_1 = 49. So by [[eq:fwd-split]]
d ≤ 20,104 + 49 + 10 + 11 + 1 + 5 = 20,180, and the theorem holds with any larger d, in particular with d = 20,180. ∎

**Remark {#rem:fwd-sharpness}** (Sharpness.) Only the term D_0 is crude. It is driven by the uniform box of
[[lem:fwd-box]] and by the generous expansion lengths of [[prop:fwd-calculus]]; counting each application of the
calculus at its own orders would lower it by more than an order of magnitude. The terms d′, d″ and D_1 are the exact
values that the proofs of [[sec:ii-f1-3-1]], [[thm:ii-e-6-1]] and [[prop:ii-e-4-4]] fix for these orders.
