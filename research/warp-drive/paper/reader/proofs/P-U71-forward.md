<!-- Placement: a new section at the end of ch:s09, after sec:ii-f1-7, or in the chapter of rem:ec-other-losses,
before that remark. It evaluates the loss d of thm:iii-i-5-3. The statements of other chapters that it cites with
explicit values are given in the comment at the end of this section. Both comments are deleted at placement. -->

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

The proof occupies the rest of the section and is completed after [[lem:fwd-increments]]. It uses the following
statements of other sections with explicit values: [[prop:ii-a1-2-4]] with M + 2 = 200T + 100 in the form of
[[prop:fwd-calculus]]; [[lem:ii-a-8-5]] (a), (b) with d_0 = 200T + 100 under the conditions there; the a priori order
N′ = 13 of [[ch:s06]]; the choice s_in = 11, s_out = −10 in [[sec:ii-c-5-2]]; and the uniqueness steps of the proofs
of [[prop:ii-e-4-3]] and [[prop:ii-e-5-6]] (a) taken at s′ = inf 𝗌 − 1 ([[lem:fwd-box]], (Sb)).

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
By [[lem:ec-theta-in]] (a), p_in − (S + S^(∗h)) = −2 Re_h(A + S) at ∂X for every fibre inner product h, so that
ϑ_in computed in h is −2 inf_(∂X) λ_min(Re_h(A + S)) ([[eq:i-a-1-5]]). We show that every eigenvalue of A + S on ∂X
is real and ≥ 0. A + S is homogeneous of degree 0 ([[lem:ec-theta-in]] (b)), so it suffices to take it at a point x
with |x| > 0, where ρ(A + S) = −Ē^C ι_(ḡ⁻¹ζ) Ḡ + (ζ ⊗_s ·) Ē^Υ Ḡ by [[eq:ec-theta-in-l]]. Use the frame
(dx̄⁰, dx̄¹, |x|e^a) of the proof of [[lem:iii-c-4-2]], in which ζ = dt̄ + d|x| = dt_* + 2d|x| = dx̄⁰ and dt_* = dx̄¹,
and let Π be the linear map of the tensors at x that exchanges the frame indices 0 and 1. The components of ḡ and of
ḡ⁻¹ in this frame do not change under the exchange (ḡ⁻¹(dx̄⁰, dx̄¹) = −2, ḡ⁻¹(dx̄⁰, dx̄⁰) = ḡ⁻¹(dx̄¹, dx̄¹) = 0, and no
mixed null-tangential components). So Π commutes with raising and lowering indices, with contractions and traces, with
⊗_s and with Ḡ; and Π dx̄⁰ = dx̄¹, Π dt̄ = dt̄ and ΠY = Y for Y := ḡ⁻¹dt̄, while Π maps
ĉ = ½(1 − v_C)dx̄⁰ + ½(1 + v_C)dx̄¹ to ĉ with v_C replaced by −v_C. In that proof Ē^C and Ē^ΥḠ are written through
ĉ, ḡ, dt̄ and Y alone: Ē^Cω = γ_Cρ(2ĉ ⊗_s ω − ⅔(1 − e_C)ḡ⟨ĉ, ω⟩) and Ē^ΥḠh = −γ_Υρ(2ι_Y h − e_Υ(tr h) dt̄). Hence
Π ρ(A + S) Π⁻¹ = −Ē^C_− ι_(ḡ⁻¹dt_*) Ḡ + (dt_* ⊗_s ·) Ē^Υ Ḡ, with Ē^C_− the operator Ē^C with v_C replaced by −v_C;
this is ρS̄ of [[eq:iii-f-2-2]] with v_C replaced by −v_C. The proof of [[lem:iii-c-4-2]] computes the matrix of that
expression in the frame for any real constant in place of v_C (it uses v_C only through a = ½(1 − v_C) and
b = ½(1 + v_C)). So Π(A + S)Π⁻¹ is lower triangular, with the diagonal [[eq:iii-c-4-3]] with v_C replaced by −v_C,

    2(1 + v_C)γ_C,  (1 + v_C)γ_C,  (1 − e_C)(1 + v_C)γ_C,  (1 − e_Υ)γ_Υ,  γ_Υ,  0,  2γ_Υ,

each entry acting on its slot as a multiple of the identity. These are the eigenvalues of A + S, with the ranks of
the slots as multiplicities. As v_C ∈ (0, 1) ([[def:iii-b-6-1]]), 0 < e_C < 1, γ_C > 0, 0 < e_Υ < 1 and γ_Υ > 0
([[sec:iii-c-1]], [[eq:iii-c-1-1]]), all are ≥ 0, and 0 is one of them: inf_(∂X) min Re spec(A + S) = 0.
[[lem:ii-c-2-5]], applied to a smooth extension of A + S to X̄ in place of S (only its values on ∂X enter), gives for
every ϵ > 0 a fibre inner product h with λ_min(Re_h(A + S)) ≥ −ϵ on ∂X. With ϵ = 1/8, ϑ_in ≤ ¼.

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
orders are (𝗌 + 1, 𝗌_0) = (12, 8) and 𝔩 = 0: d̃(13, 8) = 19, d̃(6, 6) = 12, d = 22. At the trapped set (11, 8),
𝔩 = 1: d̃(13, 8) = 19, d = 22. At ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out) the orders are (𝗌, 𝗌_0) = (−10, −13) and 𝔩 = 0:
d̃(−9, −13) = 0 + 26 + 6 = 32, d̃(−15, −15) = 36, d = 39. (𝔩 = 0 at the radial sets and 𝔩 = 1 at the trapped set,
[[sec:ii-d1-2]].)
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

with ϰ := 1/(32𝔐(T)). By Leibniz's rule |pq|^(𝗆_1+𝗆_2)_K ≤ C|p|^(𝗆_1)_K |q|^(𝗆_2)_K; and the seminorm of order 𝗆
of ⟨ξ⟩^(𝗆(x,ξ)) is at most C_K for every K, its derivatives carrying factors log⟨ξ⟩ ≤ C⟨ξ⟩^ϰ. A symbol of
[[def:ii-a1-1-3]] of any
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
the bound |∂_(x_l)^j p(x, ξ)| ≤ A⟨ξ⟩^μ for l = 1, …, n and j ≤ N, where N is an integer with N > n + |s − μ|. Then
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
    |∂_x^β ρ_J(x, η)| ≤ CA⟨η⟩^(μ−J+½),   |β| ≤ B,                                                 {#eq:fwd-reduction}

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

**Lemma {#lem:fwd-far}** (Away from the diagonal.) Let μ be a constant, let b vanish for x ∉ Q_4 and satisfy the
bounds |∂_x^β ∂_ξ^γ b| ≤ A⟨ξ⟩^(μ−|γ|) for |β| ≤ B and |γ| ≤ 2K, and let w ∈ C_c^∞(ℝⁿ) vanish near 0. The operator
with the kernel (2π)^(−n) ∫ e^(i(x−y)·ξ) w(x − y) b(x, ξ) dξ is Op(b_w) with |∂_x^β b_w| ≤ CA⟨ξ⟩^(μ−2K) for
every |β| ≤ B. It consumes 2K ξ-derivatives and B x-derivatives of b, and none in the other directions. Also
Op_ψ(b) = Op(b_ψ) with b_ψ(x, ξ) := (2π)^(−n) ∫ ψ̂(ζ) b(x, ξ − ζ) dζ, and |b_ψ|^𝗆_K ≤ C|b|^𝗆_K for every K and every
order function 𝗆 with values in [−3T, 3T]: the cut-off ψ consumes no derivative.

*Proof.* On supp w, |z|^(−2K)(−Δ_ξ)^K e^(iz·ξ) = e^(iz·ξ), z = x − y, so the kernel is that of the amplitude
w_K(x − y)(−Δ_ξ)^K b(x, ξ), w_K(z) := w(z)|z|^(−2K) ∈ C_c^∞. Multiplication of a kernel by a function of x − y is
convolution of the symbol in ξ with its Fourier transform: the operator is Op(b_w), b_w(x, ξ) = (2π)^(−n)
∫ ŵ_K(ζ)(−Δ_ξ)^K b(x, ξ − ζ) dζ. x-derivatives commute with the convolution, ŵ_K is rapidly decreasing, and Peetre's
inequality gives the bound. The same identity with ψ in place of w_K gives b_ψ. For the variable weight: if
the length of ζ is at most ⟨ξ⟩/2, then 𝗆(x, ξ − ζ) − 𝗆(x, ξ) is at most C|ζ|/⟨ξ⟩ in modulus, so
⟨ξ − ζ⟩^(𝗆(x,ξ−ζ)) ≤ C⟨ξ⟩^(𝗆(x,ξ)) when moreover |ζ| ≤ ⟨ξ⟩^(1/2), and ≤ C⟨ξ⟩^(𝗆(x,ξ))⟨ζ⟩^(C′) otherwise; for
larger ζ, both ⟨ξ⟩ and ⟨ξ − ζ⟩ are at most 3⟨ζ⟩, and the quotient of the weights ⟨·⟩^(𝗆+ϰk−|γ|) of
[[eq:fwd-seminorm]] at ξ − ζ and at ξ, k ≤ K and |γ| ≤ K, is at most C⟨ζ⟩^(6T+K+1). These polynomial factors are
integrable against ψ̂. ∎

*Near and far parts.* Fix ε ∈ (0, 1/8], depending only on the constants of (S1) and (S15), as below, and
η_0 ∈ C_c^∞((−ε, ε)ⁿ) equal to 1 near 0. Split O_β(g) = O^ε_β(g) + O^far_β(g), the near part having the kernel of
Op_ψ(g_β) multiplied by η_0(x − y), and split the adjoint O_β(g)^* likewise. By [[lem:fwd-far]] with
w := ψ(1 − η_0) and μ := sup 𝗆 + ¼ (which bounds 𝗆 plus the loss ϰ(B + 2K) of [[eq:fwd-seminorm]]), O^far_β(g) is
φ_β^* Op(b_w) (φ_β)_* with b_w of order sup 𝗆 + ¼ − 2K, at the cost of 2K ξ-derivatives and B x-derivatives of g;
(O^far_β(g))^* is its adjoint, bounded by duality between the dual spaces ((S3), (S8)), at the same cost. The near
kernels have ranges at most Cε in d_ℬ ((S15)).

**Lemma {#lem:fwd-transport}** (Change of chart, term by term.) Let α, β be charts, κ := φ_β ∘ φ_α⁻¹ (defined where
both are), θ ∈ C_c^∞((−13/8, 13/8)ⁿ), and g a symbol of order 𝗆 with values in [−T, T]. In the chart α the operators
θ O^ε_β(g) and θ O^ε_β(g)^* (the factor θ read in the chart α) are R_c for the amplitudes

    c(x, y, η) = θ(x) η̃(x, y) g_β(κ(x), Φ(x, y)^(−T) η) |det Φ(x, y)|⁻¹ |det Dκ(y)|,
    c^*(x, y, η) = θ(x) η̃^*(x, y) (μ_α(y)/μ_α(x)) g_β(κ(y), Φ(x, y)^(−T) η)^* |det Φ(x, y)|⁻¹
                   × |det Dκ(x)|,                                                                     {#eq:fwd-transport}

where Φ(x, y) := ∫_0^1 Dκ(y + t(x − y)) dt, so that κ(x) − κ(y) = Φ(x, y)(x − y), the star on g is the conjugate
transpose, and η̃(x, y) := (ψη_0)(Φ(x, y)(x − y)), η̃^*(x, y) := \overline{(ψη_0)(Φ(x, y)(y − x))}. Each derivative of
c or c^* in (x, y, η) costs at most one derivative of g, and the bounds of [[lem:fwd-reduction]] hold with μ := sup 𝗆
and A := C|g|^𝗆_(K_c). The transition map κ is differentiated at most K_c + 1 times. The term of σ_J of index 0 is
θ (χ_β g)_α, resp. θ ((χ_β g)^*)_α, the same function on phase space read in the chart α; the term of index γ has the
pointwise order 𝗆 − |γ| and consumes 2|γ| derivatives of g, the variable order being carried exactly, as every term is
evaluated at y = x, that is, at the point of phase space with the chart-α coordinates (x, η).

*Proof.* Let ε be so small that every pair (x, y) with x ∈ supp θ, |x − y| ≤ Cε and x or y in φ_α(supp χ_β) has the
segment from y to x inside the domain of κ and inside (−7/4, 7/4)ⁿ, and that ‖Φ(x, y) − Dκ(x)‖ ≤ ½‖Dκ(x)⁻¹‖⁻¹ for
these pairs; this is possible uniformly in (α, β), as supp χ_β ⊂ φ_β⁻¹([−5/4, 5/4]ⁿ) and by (S1), (S15). (For c^*
the symbol is evaluated at κ(y), with y in φ_α(supp χ_β).) The kernel of θO^ε_β(g) in the chart α is
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

Let b vanish for x ∉ [−7/4, 7/4]ⁿ and have order 𝗆 with values in [−B, B], and let 𝗍 be an order function with values
in [−A, A]. Then ‖Op(b)w‖_(H^(𝗍−𝗆)(ℝⁿ)) ≤ C|b|^𝗆_(K(A,B)) ‖w‖_(H^𝗍(ℝⁿ)). For A = B = T, K(T, T) = 10T + 15.

*Proof.* Let λ := ⟨ξ⟩^(𝗍(x,ξ)−𝗆(x,ξ)), Λ := Op(⟨ξ⟩^(𝗍)) and λ′ ∈ S^(−𝗍) a smooth symbol with Op(λ′)Λ = I + R_∞,
R_∞ of order −∞ (smooth calculus). Norm H^(𝗍−𝗆) with N_0 := A + B + 1. Then
Op(λ)Op(b)w = QΛw − Op(λ)Op(b)R_∞w with Q := Op(λ)Op(b)Op(λ′). The x-derivatives of b of order j ≤ K(A, B) are
bounded by |b|^𝗆_(K(A,B))⟨ξ⟩^(B+¼), the loss ϰj being at most ¼; so [[lem:fwd-crude]] applies to b with μ := B + ¼ and
N := n + 1 + A + B whenever |s − μ| < A + B + 1.
Step 1. Fix θ_1 ∈ C_c^∞((−2, 2)ⁿ) equal to 1 on [−15/8, 15/8]ⁿ and θ_2 ∈ C_c^∞((−29/16, 29/16)ⁿ) equal to 1 on
[−7/4, 7/4]ⁿ. As Op(b) = θ_2Op(b), Op(λ)Op(b) = Op(θ_1λ)Op(b) + Op((1 − θ_1)λ)θ_2Op(b). The kernel of
Op((1 − θ_1)λ)θ_2 is k(x, y) := (2π)^(−n) ∫ e^(i(x−y)·ξ)(1 − θ_1(x))λ(x, ξ) dξ θ_2(y). On its support the distance
of x and y is at least 1/16, so that |x − y| ≥ c⟨x⟩ and |x − y|^(−2L)(−Δ_ξ)^L e^(i(x−y)·ξ) = e^(i(x−y)·ξ). Let
M ∈ ℕ. After L integrations by parts in ξ, 2L ≥ A + B + n + M + 2, the y-derivatives of k of order at most M are
bounded by C⟨x⟩^(−n) and vanish for y ∉ supp θ_2. So the value of Op((1 − θ_1)λ)θ_2w at x is at most
‖k(x, ·)‖_(H^M)‖w‖_(H^(−M)) ≤ C⟨x⟩^(−n)‖w‖_(H^(−M)) in modulus, for w ∈ 𝒮, and Op((1 − θ_1)λ)θ_2 maps H^(−M) to
L², with a norm that depends on λ and M only. With M := A + B + 1, as Op(λ′) maps L² to H^𝗍 ⊂ H^(−A) and Op(b) maps
H^(−A) to H^(−A−B−1) ([[lem:fwd-crude]], s = −A), the operator Op((1 − θ_1)λ)θ_2Op(b)Op(λ′) is bounded on L², at
the cost n + 1 + A + B.
[[lem:fwd-composition]] with p := θ_1λ (order with values in [−A − B, A + B]), q := b (vanishing off Q_4), J := J_1
and 6 x-derivatives of the remainder gives Op(θ_1λ)Op(b) = Op(c_1) + Op(r_1). Here c_1 = λ ♯_(J_1) b, as θ_1 = 1 near
the x-support of b, and r_1 vanishes for x ∉ Q_4, as p does, and has order at most (A + B) + B − J_1 + ½ = −A − ½.
Op(λ′) maps L² to H^𝗍 ⊂ H^(−A), and [[lem:fwd-crude]] (s = −A, μ = −A, N = 6) maps H^(−A) to L². Cost on b:
J_1 + 6 + 2L′ with 2L′ = 𝔢(n + 1 + J_1 + A + B), as |sup(𝗍 − 𝗆) − J_1| ≤ J_1 + A + B; this is K(A, B).
Step 2. [[lem:fwd-composition]] with p := c_1 (order 𝗍, values in [−A, A]), q := λ′ (not compactly supported), J := J_2
and 6 x-derivatives gives Op(c_1)Op(λ′) = Op(c) + Op(r_2), r_2 of order at most 2A − J_2 + ½ = −½ and vanishing for
x ∉ Q_4, as c_1 does; it is bounded on L² by [[lem:fwd-crude]] (N = 6). Cost on c_1: J_2 + 12, on b:
J_2 + 12 + (J_1 − 1) = 4A + 2B + 13 ≤ K(A, B).
Step 3. c = Σ ∂_ξ^(α′)(∂_ξ^α λ · D_x^α b) D_x^(α′) λ′/(α!α′!) has the pointwise order (𝗍 − 𝗆) + 𝗆 − 𝗍 − |α| − |α′|,
the variable orders cancelling at every point; [[lem:fwd-l2]] bounds Op(c) on L² by C|c|^0_12, at a cost on b of
12 + (J_1 − 1) + (J_2 − 1) = 4A + 2B + 12.
Step 4. ‖Op(b)w‖_(H^(−A−B−1)) ≤ C‖w‖_(H^(−A)), and ‖Op(λ)Op(b)R_∞w‖ ≤ C‖Op(b)R_∞w‖_(H^(A+B)) ≤
C‖R_∞w‖_(H^(A+2B+1)) ≤ C‖w‖_(H^(−N_0)), by [[lem:fwd-crude]] with μ := B + ¼ (s = −A, resp. s = A + 2B + 1), at most
n + 1 + A + B x-derivatives of b. Together with Steps 1–3 and ‖Λw‖ ≤ ‖w‖_(H^𝗍) this is the claim.
The largest count is that of Step 1. For A = B = T: J_1 = 4T + 1, 2L′ = 𝔢(6T + 7) = 6T + 8, K = 10T + 15. ∎

**Lemma {#lem:fwd-norms}** (Localisation of the norms.) Let 𝗋 be an order function, θ̃ ∈ C_c^∞((−13/8, 13/8)ⁿ) equal
to 1 on [−3/2, 3/2]ⁿ, and θ̃_α := φ_α^*θ̃. There is C such that, for all u and all functions v_α supported in
[−5/4, 5/4]ⁿ,

    ‖Σ_α φ_α^* v_α‖²_𝗋 ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)(ℝⁿ)),       Σ_α ‖(φ_α)_*(θ̃_α u)‖²_(H^(𝗋_α)(ℝⁿ)) ≤ C ‖u‖²_𝗋.

*Proof.* Only smooth symbols occur. The lemmas above apply to them with N_0 in place of T, every seminorm
[[eq:fwd-seminorm]] being finite, and no derivative is counted; the constants depend on 𝗋, on the cut-offs and on
(S1), (S15), never on the charts. Here N_0 is a fixed integer with N_0 ≥ sup |𝗋|. By (S1) ([Hin26d, Definition
1.1 (1), p. 2]) there is m_ℬ ∈ ℕ such that no point lies in more than m_ℬ of the sets U_α. Fix ℓ ∈ (7/4, 2) such
that the supports of the cut-offs χ° and θ̌ below lie in [−ℓ, ℓ]ⁿ, and let A_α be the set of the β with
φ_α⁻¹([−ℓ, ℓ]ⁿ) ∩ φ_β⁻¹([−ℓ, ℓ]ⁿ) ≠ ∅; so β ∈ A_α exactly when α ∈ A_β.

*The count.* There is N_ℬ ≥ m_ℬ with |A_α| ≤ N_ℬ for every α. Indeed, let C_1 ≥ 1 bound the norms of the first
derivatives of the transition maps τ_(βα) = φ_β ∘ φ_α⁻¹, uniformly in (α, β) ((S1)), and put r := (2 − ℓ)/(2C_1).
Let β ∈ A_α, p a point of φ_α⁻¹([−ℓ, ℓ]ⁿ) ∩ φ_β⁻¹([−ℓ, ℓ]ⁿ), x := φ_α(p), and W := φ_α(U_α ∩ U_β), an open set
that contains x, on which τ_(βα) is defined. Let x_t := x + tv for 0 ≤ t ≤ t_1, with |v| = 1 and t_1 < r. Each
coordinate of x_t differs from that of x by less than r < 2 − ℓ, so x_t ∈ (−2, 2)ⁿ. Suppose that some x_t lies
outside W, and let t_* be the least such t (it exists as W is open, and t_* > 0 as x ∈ W). For t, t′ < t_*, the
segment from x_t to x_(t′) lies in W, so that |τ_(βα)(x_t) − τ_(βα)(x_(t′))| ≤ C_1|t − t′|; with t′ = 0, as
τ_(βα)(x_0) = φ_β(p), the distance of τ_(βα)(x_t) from φ_β(p) is at most C_1t_* < C_1r = (2 − ℓ)/2. So τ_(βα)(x_t)
converges, as t ↑ t_*, to a point y whose coordinates have modulus at most ℓ + (2 − ℓ)/2 = (2 + ℓ)/2 < 2, that is,
y ∈ (−2, 2)ⁿ. The points φ_α⁻¹(x_t) = φ_β⁻¹(τ_(βα)(x_t)) then converge on the manifold both to φ_α⁻¹(x_(t_*)) and
to φ_β⁻¹(y) ∈ U_β. As the manifold is Hausdorff, φ_α⁻¹(x_(t_*)) lies in U_α ∩ U_β, that is, x_(t_*) ∈ W, a
contradiction. So the segment stays in W, and the ball of radius r about x lies in W. Cover [−ℓ, ℓ]ⁿ by N_1 balls
of radius r/2, N_1 depending only on n, ℓ and C_1. If A_α had more than m_ℬN_1 elements, then, choosing p and x as
above for each β ∈ A_α, the points x of m_ℬ + 1 of these β would lie in one of the balls. Its centre c lies within r/2
of each of these points x, hence in φ_α(U_α ∩ U_β) for each of these m_ℬ + 1 values of β, and the point φ_α⁻¹(c)
lies in m_ℬ + 1 of the sets U_β, against the choice of m_ℬ. So N_ℬ := m_ℬN_1 serves.

*Integer orders.* Let k ∈ ℤ, K ⊂ [−ℓ, ℓ]ⁿ compact, ϑ ∈ C_c^∞((−2, 2)ⁿ) with supp ϑ ⊂ [−ℓ, ℓ]ⁿ, and
ϑ_α := φ_α^*ϑ. We show

    ‖Σ_α φ_α^* w_α‖²_k ≤ C Σ_α ‖w_α‖²_(H^k(ℝⁿ))  (supp w_α ⊂ K),      Σ_α ‖(φ_α)_*(ϑ_α u)‖²_(H^k(ℝⁿ)) ≤ C ‖u‖²_k.

They are used below with K = [−5/4, 5/4]ⁿ or K = supp θ̃, and with ϑ = θ̃ or ϑ = θ̌; these lie in [−ℓ, ℓ]ⁿ, as
13/8 < ℓ and by the choice of ℓ. By (S3), ‖u‖²_k = Σ_β ‖(φ_β)_*(χ°_βu)‖²_(H^k(ℝⁿ)) with χ°_β := φ_β^*χ°,
where χ° ∈ C_c^∞((−2, 2)ⁿ) equals 1 on [−1, 1]ⁿ ([Hin26d, Definition 3.14, p. 34]) and is taken with 0 ≤ χ° ≤ 1,
which changes the norm only up to equivalence ([Hin26d, p. 36]); as the sets φ_β⁻¹((−1, 1)ⁿ) cover ((S1)) and no
point lies in more than m_ℬ ≤ N_ℬ of the U_β, 1 ≤ Σ_β χ°_β ≤ N_ℬ. For charts α, β and a function ϕ on (−2, 2)ⁿ that
vanishes outside φ_α(F), with F ⊂ U_α ∩ U_β compact, put T^ϕ_(βα)w := (ϕw) ∘ φ_α ∘ φ_β⁻¹ on φ_β(U_α ∩ U_β),
extended by 0. If the derivatives of ϕ of order at most |k| are bounded, then ‖T^ϕ_(βα)w‖_(H^k) ≤ C‖w‖_(H^k). For
k ≥ 0 this is Leibniz's rule, the chain rule and the change of variables, the transition maps and their inverses
having bounded derivatives ((S1)). For k < 0 it follows by duality, the L²-adjoint of T^ϕ_(βα) being T^(ϕ′)_(αβ) with ϕ′ := (ϕ̄ |det D(φ_β ∘ φ_α⁻¹)|) ∘ φ_α ∘ φ_β⁻¹, a
function of the same kind. Now (φ_β)_*(χ°_βφ_α^*w_α) = T^ϕ_(βα)w_α with ϕ := χ̌ · (χ° ∘ φ_β ∘ φ_α⁻¹), where
χ̌ ∈ C_c^∞((−2, 2)ⁿ) equals 1 on K and χ° ∘ φ_β ∘ φ_α⁻¹, extended by 0, is smooth, as φ_β⁻¹(supp χ°) is compact;
and it vanishes unless α ∈ A_β. So the left side of the first bound is at most Σ_β N_ℬ Σ_(α∈A_β) C‖w_α‖², which is
at most CN_ℬ² Σ_α ‖w_α‖². For the second, ϑ_αu = Σ_(β∈A_α) ϑ_αζχ°_βu with ζ := (Σ_γ χ°_γ)⁻¹, whose derivatives in
the charts are bounded, and (φ_α)_*(ϑ_αζχ°_βu) = T^ϕ_(αβ)(φ_β)_*(χ°_βu) with ϕ := χ̌′ · ((ϑ_αζ) ∘ φ_β⁻¹), where
χ̌′ ∈ C_c^∞((−2, 2)ⁿ) equals 1 on supp χ°; summing as before gives the second bound.

*Two facts.* Put Λ := Op(ρ_∞^(−𝗋)) ∈ Ψ̃^𝗋 and Λ′_0 := Op(ρ_∞^𝗋). By (S5) and (S8), Λ′_0Λ = I − R_1 with R_1 of
order −½, as the principal symbols multiply to 1 and Op(1) = I ([[eq:ii-a1-1-1]]). So Λ′ := Σ_(j<4N_0) R_1^jΛ′_0
satisfies Λ′Λ = I + R with R := −R_1^(4N_0) of order −2N_0, and Λ′ = Op(λ′) + R′, where λ′ is a smooth symbol of
order −𝗋 and R′ ∈ Ψ̃^(−∞) ((S4), (S8)). H^𝗋 is the space of the u ∈ H^(−N_0) with Λu ∈ L² ([[sec:ii-a1-1-1]],
(S8)), normed by ‖u‖_𝗋 := ‖Λu‖ + ‖u‖_(−N_0). On ℝⁿ, ‖w‖_(H^(𝗋_α)) ≤ C‖w‖_(H^(N_0)), as Op(⟨ξ⟩^(𝗋_α))⟨D⟩^(−N_0) is
Op(⟨ξ⟩^(𝗋_α−N_0)), bounded on L² by [[lem:fwd-l2]]. Let θ̌ ∈ C_c^∞((−2, 2)ⁿ) equal 1 on [−7/4, 7/4]ⁿ and
θ̌_α := φ_α^*θ̌. For a smooth symbol g of order 𝗆 with values in [−N_0, N_0], Op(g) = Σ_β O^ε_β(g) + Σ_β O^far_β(g)
([[eq:fwd-chart-op]] and the near and far parts above).

(P1) Σ_β O^far_β(g) maps H^(−N_0) to H^(N_0). Indeed, by [[lem:fwd-far]] with 2K ≥ 3N_0 + 1, and as the kernel of
O_β(g) joins points within ¼ in the chart β, O^far_β(g)u = φ_β^*Op(b^β)(φ_β)_*(θ̌_βu), with b^β vanishing for
x ∉ (−5/4, 5/4)ⁿ and of order at most −2N_0. By [[lem:fwd-crude]] (s = −N_0, μ = −2N_0) and the integer bounds at
the orders N_0 and −N_0, ‖Σ_β O^far_β(g)u‖²_(N_0) ≤ C Σ_β ‖(φ_β)_*(θ̌_βu)‖²_(H^(−N_0)) ≤ C‖u‖²_(−N_0).

(P2) For charts α, β, (φ_α)_*(θ̃_αO^ε_β(g)f) = (Op(σ) + Op(ρ))(φ_α)_*(θ̌_αf), where σ and ρ vanish for x ∉ supp θ̃
and unless β ∈ A_α, σ has order 𝗆_α, and every x-derivative of ρ is bounded by C⟨ξ⟩^(−2N_0). Indeed, by
[[lem:fwd-transport]] with θ := θ̃, the left side is R_c applied to (φ_α)_*f, whose amplitude c contains the factor
θ̃(x) and vanishes unless y ∈ (−7/4, 7/4)ⁿ (the choice of ε in that proof), so that θ̌_α may be inserted. As g_β
vanishes for x ∉ (−5/4, 5/4)ⁿ, c contains the factor θ̃(x)g_β(κ(x), ·), which vanishes unless φ_α⁻¹(x) lies in
φ_α⁻¹(supp θ̃) ∩ φ_β⁻¹([−5/4, 5/4]ⁿ); so c vanishes identically, and with it the σ and ρ below, unless β ∈ A_α. (In
other words, θ̃_α is supported in φ_α⁻¹(supp θ̃), and O^ε_β(g)f in φ_β⁻¹([−5/4, 5/4]ⁿ) by left quantization.) Then
[[lem:fwd-reduction]] with J := 3N_0 + 1 gives σ := σ_J, of order 𝗆_α as its terms of index γ have the pointwise
order 𝗆_α − |γ|, and ρ := ρ_J, of order at most N_0 − J + ½ < −2N_0. So,
for every order 𝗍 with values in [−N_0, N_0], Op(σ) maps H^(𝗍_α) to H^(𝗍_α−𝗆_α) by [[lem:fwd-local]], as σ vanishes
for x ∉ [−7/4, 7/4]ⁿ, and Op(ρ) maps H^(−N_0) to H^(N_0) by [[lem:fwd-crude]]; both uniformly in (α, β).

*The first bound.* Let u := Σ_α φ_α^*v_α, first with finitely many v_α ≠ 0, and λ_0 := ρ_∞^(−𝗋), so that
Λ = Op(λ_0). By the integer bound at −N_0, ‖u‖²_(−N_0) ≤ C Σ_α ‖v_α‖²_(H^(−N_0)) ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)), and by
(P1), ‖Σ_β O^far_β(λ_0)u‖ ≤ C‖u‖_(−N_0). The kernel of O^ε_β(λ_0) joins points within Cε in d_ℬ ((S15)), so for ε
small O^ε_β(λ_0)φ_α^*v_α is supported where θ̃_α = 1. By (P2) with 𝗍 := 𝗋, as θ̌ = 1 on supp v_α,
Σ_β O^ε_β(λ_0)φ_α^*v_α = φ_α^*V_α with V_α := Σ_(β∈A_α) (Op(σ_(αβ)) + Op(ρ_(αβ)))v_α, which vanishes outside
supp θ̃ and has ‖V_α‖ ≤ CN_ℬ‖v_α‖_(H^(𝗋_α)). The integer bound at the order 0 with K := supp θ̃ gives
‖Σ_α φ_α^*V_α‖² ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)). So ‖u‖²_𝗋 ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)). For infinitely many v_α, the partial
sums converge in H^(−N_0), by the integer bound, and are Cauchy in H^𝗋, by this bound; their limit is u.

*The second bound.* Let f := Λu, so ‖f‖ ≤ ‖u‖_𝗋, and u = Λ′f − Ru = Σ_β O^ε_β(λ′)f + h with
h := Σ_β O^far_β(λ′)f + R′f − Ru. By (P1), and as R′ is residual and R has order −2N_0,
‖h‖_(N_0) ≤ C(‖f‖ + ‖u‖_(−N_0)) ≤ C‖u‖_𝗋, and the integer bound at N_0 with ϑ := θ̃ gives
Σ_α ‖(φ_α)_*(θ̃_αh)‖²_(H^(𝗋_α)) ≤ C Σ_α ‖(φ_α)_*(θ̃_αh)‖²_(H^(N_0)) ≤ C‖u‖²_𝗋. By (P2) with g := λ′, of order −𝗋, and
𝗍 := 0, ‖(φ_α)_*(θ̃_αO^ε_β(λ′)f)‖_(H^(𝗋_α)) ≤ C‖(φ_α)_*(θ̌_αf)‖, and the left side vanishes unless β ∈ A_α. So, by
the integer bound at the order 0 with ϑ := θ̌, the sum over α of ‖(φ_α)_*(θ̃_α Σ_β O^ε_β(λ′)f)‖²_(H^(𝗋_α)) is at most
CN_ℬ² Σ_α ‖(φ_α)_*(θ̌_αf)‖² ≤ C‖f‖² ≤ C‖u‖²_𝗋. As θ̃_αu = θ̃_α Σ_β O^ε_β(λ′)f + θ̃_αh, the second bound follows. ∎

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

    max( 2J_R + B + 𝔢(n + 1 + J_R + T),  2K + B,  B + 2(J_R − 1),  (J_C + B) + (r − 2)(J_C − 1) + 2(J_R − 1),
         J_C + B + 𝔢(n + 1 + J_C + (r − 1)T) + 2(J_R − 1) ),                                         {#eq:fwd-ecount}

the last two only if r ≥ 2. A derivative of order K′ of t_α consumes at most K′ + (r − 1)(J_C − 1) + 2(J_R − 1)
derivatives of each g_j. Each term of t_α is a product of derivatives of the terms of the s_j at one point (x, η); its
grade, the sum of the indices |γ| of the reductions and of the indices |α| of the compositions that produced it, lowers
the pointwise order Σ_j 𝗆_j by exactly that number.

*Proof.* Write F_j = F^ε_j + F^far_j, the sums over β of the near and far parts. The product of the near parts is
Σ_α χ_α F^ε_1 ⋯ F^ε_r, and the kernel of χ_α F^ε_1 ⋯ F^ε_r joins points within rCε ≤ 1/8 in d_ℬ of supp χ_α, inside
φ_α⁻¹([−3/2, 3/2]ⁿ) for ε small; so inserting θ̂ in front of F^ε_j, j ≥ 2, and θ̃_α on the right changes nothing. In the
chart α, by [[lem:fwd-reduction]] and [[lem:fwd-transport]] with J := J_R, each θ^(j)F^ε_j is Op(s_j) + Op(ρ_j), ρ_j of
order at most T − J_R + ½ = −R − ½. Only the β ∈ A_α of the proof of [[lem:fwd-norms]], at most N_ℬ of them,
contribute to s_j and ρ_j: the amplitude contains θ^(j)(x) and g_β at κ(x), resp. at κ(y) with y ∈ (−7/4, 7/4)ⁿ
([[eq:fwd-transport]] and the choice of ε there), and g_β vanishes for x ∉ (−5/4, 5/4)ⁿ. Expanding, the product is
Op(s_1)⋯Op(s_r) plus terms with a factor Op(ρ_j). By [[lem:fwd-composition]] (q vanishing off Q_4) with J := J_C
applied r − 1 times from the left,
Op(s_1)⋯Op(s_r) = Op(t_α) + Σ_(j≥2) Op(r_j) Op(s_(j+1)) ⋯ Op(s_r), r_j of order at most jT − J_C + ¾ ≤ −R − ¼. The far
terms are products with at least one factor F^far_j, of order at most T − 2K + ½ ≤ −R − ½ ([[lem:fwd-far]]).

So every term of E is a product of at most r operators, one of order at most −R (the gaining factor) and the others of
order at most T, which we bound between Sobolev spaces of constant order by [[lem:fwd-crude]], chart by chart, and on
the manifold by [[lem:fwd-norms]] at constant orders (not integers in general); adjoints by duality. Start from
H^𝗍 ⊂ H^(−T). The factors to the right of the gaining factor lower
the order by at most T each, the gaining factor raises it by R, the others lower it by at most T: the result lies in
H^(−T−(r−1)T+R) = H^S. The input orders s of the factors of order at most T lie in [−rT, R − T], so |s − T| ≤
max((r + 1)T, R − 2T); that of the gaining factor lies in [−rT, −T], so |s + R| ≤ R − T = S + (r − 1)T. So B
x-derivatives suffice in every application of [[lem:fwd-crude]]. The bounds that [[lem:fwd-crude]] needs carry the loss
ϰ. A factor of order at most T satisfies them with μ := T + 1/32, as its symbol is differentiated at most 𝔐(T) times
(the counts below) and ϰ𝔐(T) = 1/32. The bounds [[eq:fwd-reduction]], [[eq:fwd-remainder]] and those of
[[lem:fwd-far]] include the loss, so the gaining factor satisfies them with μ := −R − ¼. The at most five shifts by
1/32 lower the final order by less than ¼ and change each |s − μ| by less than 1; so the result lies in H^S, and
N := B satisfies N > n + |s − μ| in every application.

The counts, all derivatives of g_j: ρ_j costs 2J_R + B + 2L′ with 2L′ = 𝔢(n + 1 + J_R + T) ([[lem:fwd-reduction]], as
the distance from sup 𝗆_j to J_R is at most J_R + T); a far part costs 2K + B ([[lem:fwd-far]]); a factor Op(s_j)
bounded by [[lem:fwd-crude]] costs B + 2(J_R − 1) ([[lem:fwd-transport]]). In the composition of
t_(j−1) := s_1 ♯ ⋯ ♯ s_(j−1) with s_j, the left symbol needs J_C + B derivatives and the right one J_C + B + 2L′_C,
2L′_C = 𝔢(n + 1 + J_C + (j − 1)T), since the order of t_(j−1) has supremum within J_C + (j − 1)T of J_C. The symbol
t_(j−1) already contains, on s_i, at most (j − 2)(J_C − 1)
derivatives (ξ-derivatives from the j − 2 compositions in which it stood on the left, or x-derivatives from the one in
which it stood on the right and ξ-derivatives from the later ones), and s_i contains 2(J_R − 1) derivatives of g_i. With
j ≤ r this gives the last two entries of [[eq:fwd-ecount]], and the statement on t_α. The grades are those of
[[lem:fwd-composition]] and [[lem:fwd-transport]]. ∎

**Proposition {#prop:fwd-calculus}** (Explicit indices.) Let T ∈ ℕ. Let 𝗍 (the order of the space on which an item is
applied) and the orders 𝗆, 𝗆_1, 𝗆_2 of the symbols have values in [−T, T], of any index ν. Then [[prop:ii-a1-2-4]]
holds with M + 2 = 𝔐(T) = 200T + 100 in the following form.

(a)–(d) as stated there, with at most 10T + 15, 34T + 24, 18T + 23 and 34T + 32 derivatives of each symbol.

(e) For every N ≤ T and every expression S_1B_1𝒯B_2S_2 with at most six quantizations in each of its products (the
localisers and B_1, B_2 included), each quantized symbol of order with values in [−T, T]: at most 95T + 7 derivatives.

(f) For every expression 𝒯 with at most six quantizations in each product, each quantized symbol (a product of the a_i
included) of order with values in [−T, T], and every order function μ with values in [−6T − 3, 6T + 3] such that, in
every chart α, the symbol t_α of 𝒯 ([[lem:fwd-expansion]], the signed sum over the products of 𝒯) is a sum of products
of derivatives of pointwise order at most μ (up to the loss ϰ times the number of derivatives): 𝒯 has order μ + δ,
with at most 158T + 52 derivatives.

Here 𝒯 denotes an expression, and T the integer bounding the orders. [[lem:ii-a-8-5]] (a) holds with d_0 = 𝔐(T) when
𝗌 has values in [−T, T] (10T + 15 derivatives), and (b) when 𝗌_0 has values in [−T, T] and sup 𝗌 − inf 𝗌_0 ≤ T
(34T + 15 derivatives). For T = 100 the largest count is 15,852 ≤ 𝔐(100) − 2.

In this form the hypothesis of (f) is an identity of symbols, and it is checked at each use in [[lem:fwd-box]]: there
the terms above the order μ cancel because the leading terms of an adjoint and of the conjugate symbol agree, because
scalar symbols commute with all others, and by exact identities such as φ_0ǎ = ǎ.

*Proof.* Every symbol below is read in the charts of ρℬ, where |a_α|^𝗆_K ≤ C‖a‖_((K);ν,𝗆) (the beginning of this
section); the constants C depend on ϰ, ν, the orders, the bounds of (S1) for the transition maps (differentiated at
most 𝔐(T) + 1 times, by [[lem:fwd-transport]] and the counts below), and on the smooth symbols involved, never on
their supports beyond the identities used. The global estimate is assembled in the same way in every item: if
𝒯 = Σ_α φ_α^* Op(t_α)(φ_α)_*θ̃_α + E with t_α vanishing for x ∉ [−5/4, 5/4]ⁿ, |t_α|^(μ+δ)_(K(T,B_G)) ≤ C uniformly in
α, μ with values in [−B_G, B_G], and E bounded from H^𝗍 to H^S with S ≥ sup(𝗍 − μ), then by [[lem:fwd-local]] (with
A := T, B := B_G) and [[lem:fwd-norms]] (twice)

    ‖𝒯u‖_(𝗍−μ−δ) ≤ C(Σ_α ‖Op(t_α)(φ_α)_*(θ̃_αu)‖²_(H^((𝗍−μ−δ)_α)))^(1/2) + ‖Eu‖_S ≤ C‖u‖_𝗍.        {#eq:fwd-assembly}

So each item reduces to: the parameters (S, B_G) of [[lem:fwd-expansion]] and [[lem:fwd-local]], the check that t_α has
the stated order, and the counts. The integers in brackets are those for T = 100.

*(a).* By [[eq:fwd-chart-op]] and [[lem:fwd-far]], Op(a)u = Σ_α φ_α^* Op((a_α)_ψ)(φ_α)_*(θ̃_α u), the kernel of
Op_ψ(a_α) joining points within ¼, and |(a_α)_ψ|^𝗆_K ≤ C|a_α|^𝗆_K: no change of chart and no expansion is needed.
[[lem:fwd-local]] with A = B = T and [[lem:fwd-norms]] give (a) without loss, with K(T, T) = 10T + 15 [1,015]
derivatives: J_1 = 4T + 1 [401], 2L′ = 6T + 8 [608]. Multiplication by ℓ is Op(ℓ) ((S4), [[eq:ii-a1-1-1]]), with
𝗆 = 0 and ‖ℓ‖_((K);0,0) ≤ C‖ℓ‖_(C^K_e3b); so [[lem:ii-a-8-5]] (a) holds with d_0 = 10T + 15 [1,015], and its
b-regularity part follows by Leibniz's rule as there.

*The symbols of one operator in a chart.* For a symbol g let s^α_j(g), resp. s^α_j(g^*), be the symbol s_j of
[[lem:fwd-expansion]] for F_j = Op(g), resp. Op(g)^*, with the left cut-off θ^(j). By [[lem:fwd-transport]] its term
of index 0 is θ^(j) Σ_β χ_β g = θ^(j)g, resp. θ^(j)g^*, read in the chart α, and its term of index 1 is θ^(j)V_α(g),
resp. θ^(j)V^*_α(g), with V_α(g) the sum over β of the terms of index 1 of the reductions of the amplitudes of
[[eq:fwd-transport]] without the factor θ: a linear expression in g and its first and second derivatives with scalar
coefficients, so that V_α(g) is scalar when g is, and commutes with every matrix when g is scalar. Every term of
s^α_j(g) vanishes where all derivatives of g vanish, that is, outside the support of g read in the chart α.

*(b).* Here 𝒯 := Op(a_1)Op(a_2) − Op(a_1a_2). [[lem:fwd-expansion]] applies to Op(a_1)Op(a_2) with r = 2, and to
Op(a_1a_2) with r = 1 and T replaced by 2T (its symbol has order 𝗆_1 + 𝗆_2 with values in [−2T, 2T], and the
order 𝗍 has values in [−2T, 2T]), both with S := 3T + 1 [301] ≥ sup(𝗍 − 𝗆_1 − 𝗆_2 + 1). Then
t_α = s^α_1(a_1) ♯ s^α_2(a_2) − s^α_1(a_1a_2), and its terms of grade 0 are χ_αa_1 · θ̂a_2 − χ_αa_1a_2 = 0, as θ̂ = 1
on supp χ_α. So t_α is a sum of terms of grade at least 1, of pointwise order at most 𝗆_1 + 𝗆_2 − 1 up to the loss:
μ := 𝗆_1 + 𝗆_2 − 1, B_G := 2T + 1. Counts for Op(a_1)Op(a_2), from [[eq:fwd-expansion]]: R = 5T + 1 [501],
B = 4T + 7 [407], J_R = 6T + 2 [602], 2K = 6T + 2 [602], J_C = 7T + 2 [702]; by [[eq:fwd-ecount]] the remainder of
the reductions costs 2J_R + B + 𝔢(7T + 8) ≤ 23T + 21 [2,321], the far parts 10T + 9 [1,009], a factor Op(s_j)
16T + 9 [1,609], the compositions at most J_C + B + 𝔢(8T + 8) + 2(J_R − 1) ≤ 31T + 21 [3,121]; the main symbol costs
K(T, 2T + 1) + (J_C − 1) + 2(J_R − 1) ≤ (15T + 21) + (7T + 1) + (12T + 2) = 34T + 24 [3,424], with
K(T, 2T + 1) = J_1 + 6 + 𝔢(9T + 10), J_1 = 6T + 3 [603]. For Op(a_1a_2) (T replaced by 2T): R = 5T + 1, B = 4T + 6,
J_R = 7T + 2, the remainders cost at most 27T + 20 [2,720], 11T + 9 and 18T + 8, and the main symbol at most
K(T, 2T + 1) + 2(J_R − 1) ≤ 29T + 23 [2,923]; derivatives of a_1a_2 are derivatives of a_1 and a_2 in equal number.
So (b) holds with 34T + 24 [3,424] derivatives, by [[eq:fwd-assembly]].

*(c).* Here 𝒯 := Op(a)^* − Op(a^*), a^* the conjugate transpose (the conjugate for scalar a). [[lem:fwd-expansion]]
with r = 1 for both, S := 2T + 1 [201]. The terms of grade 0 of t_α = s^α_1(a^*) − s^α_1(a^*) (the first for the
adjoint, the second for the quantization of a^*) are χ_αa^* − χ_αa^* = 0 by [[lem:fwd-transport]]. μ := 𝗆 − 1,
B_G := T + 1. Counts: R = 3T + 1 [301], B = 2T + 7 [207], J_R = 4T + 2 [402]; the remainders cost at most
2J_R + B + 𝔢(5T + 8) ≤ 15T + 21 [1,521], 6T + 9 [609] and 10T + 9 [1,009]; the main symbol
K(T, T + 1) + 2(J_R − 1) = (10T + 21) + (8T + 2) = 18T + 23 [1,823], K(T, T + 1) = (4T + 3) + 6 + (6T + 12).

*(d).* Here 𝒯 := i[Op(a_1), Op(a_2)] − Op(H_(a_1)a_2), one of a_1, a_2 scalar. [[lem:fwd-expansion]] with r = 2 for
the two products and r = 1, T replaced by 2T + 1, for Op(H_(a_1)a_2), whose symbol consumes one derivative of each a_i;
S := 3T + 2 [302]. In t_α the terms of grade 0 are iχ_α(a_1a_2 − a_2a_1) = 0. The terms of grade 1 are, as θ̂ = 1 and
D_xθ̂ = 0 on supp χ_α and ∂_ξχ_α = 0,

    iχ_α(a_1V_α(a_2) − V_α(a_2)a_1 + V_α(a_1)a_2 − a_2V_α(a_1)) + χ_α Σ_j (∂_(ξ_j)a_1 ∂_(x_j)a_2 − ∂_(ξ_j)a_2 ∂_(x_j)a_1)
        − χ_α H_(a_1)a_2.

The first group vanishes as one of a_1, a_2, and then also its V_α, is scalar. The second is χ_α times the principal
symbol of i[Op(a_1), Op(a_2)] in the chart α, which is H_(a_1)a_2 by (S5) (entrywise when one symbol is a matrix). So
t_α has terms of grade at least 2 only: μ := 𝗆_1 + 𝗆_2 − 2, B_G := 2T + 2. Counts for the products: R = 5T + 2,
B = 4T + 8, J_R = 6T + 3, 2K ≤ 6T + 4, J_C = 7T + 3; remainders at most 23T + 25, 10T + 12, 16T + 12, 31T + 25; main
K(T, 2T + 2) + (J_C − 1) + 2(J_R − 1) ≤ (15T + 26) + (7T + 2) + (12T + 4) = 34T + 32 [3,431]. For Op(H_(a_1)a_2):
R = 5T + 3, B = 4T + 8, J_R = 7T + 5, counts at most 27T + 33, 11T + 15, 18T + 17 and 29T + 35, each including the
derivative taken by H. So (d) holds with 34T + 32 [3,431] ≤ M + 1 derivatives.

*(e).* Write B_i = Op(b_i) + R_i with supp b_i ⊂ K_i and R_i ∈ Ψ̃^(−∞) ([[sec:ii-a1-1-2]]), and expand the expression
into products. A product containing R_1 or R_2 is a product of at most six operators, R_i of every order and the others
of order at most T, bounded from H^𝗍 to H^(T+N) by [[lem:fwd-crude]] as in the proof of [[lem:fwd-expansion]], at the
cost B + 2(J_R − 1) below. For a product containing Op(b_1) and Op(b_2), [[lem:fwd-expansion]] applies with r ≤ 6 and
S := T + N ≤ 2T. Every term of its t_α contains a derivative of a term of s^α(b_1), which vanishes outside K_1 read in
the chart α, and one of a term of s^α(b_2), which vanishes outside K_2, both at the same point (x, η); as K_1 ∩ K_2 = ∅,
t_α = 0. So the operator is E of [[eq:fwd-product]], bounded from H^𝗍 to H^(T+N) ⊂ H^(𝗍+N): it has order −N. The counts
are largest for r = 6 and S = 2T: R = 8T [800], B = 7T + 6 [706], J_R = 9T + 1 [901], 2K ≤ 9T + 2 [902],
J_C = 14T + 1 [1,401]. By [[eq:fwd-ecount]]: 2J_R + B + 𝔢(10T + 7) = 35T + 16 [3,516]; 16T + 8 [1,608]; 25T + 6
[2,506]; (J_C + B) + 4(J_C − 1) + 2(J_R − 1) = 95T + 7 [9,507]; J_C + B + 𝔢(19T + 7) + 2(J_R − 1) ≤ 58T + 16 [5,815].
So (e) holds with 95T + 7 [9,507] derivatives. No auxiliary symbol y and no commutator expansion is needed: the
operators B_1, B_2 enter only the constants, through their symbols and the sets K_1, K_2.

*(f).* [[lem:fwd-expansion]] for each product, r ≤ 6, S := 7T + 3 [703] ≥ sup(𝗍 − μ), and [[eq:fwd-assembly]] with
B_G := 6T + 3, which the hypothesis on t_α allows. The counts are largest for r = 6: R = 13T + 3 [1,303],
B = 12T + 9 [1,209], J_R = 14T + 4 [1,404], 2K = 14T + 4 [1,404], J_C = 19T + 4 [1,904]; the remainders cost at most
2J_R + B + 𝔢(15T + 10) ≤ 55T + 29 [5,529], 26T + 13 [2,613], 40T + 15 [4,015],
(J_C + B) + 4(J_C − 1) + 2(J_R − 1) = 135T + 31 [13,531] and J_C + B + 𝔢(24T + 10) + 2(J_R − 1) ≤ 83T + 31
[8,331]; the main symbol K(T, 6T + 3) + 5(J_C − 1) + 2(J_R − 1) ≤ (35T + 31) + (95T + 15) + (28T + 6) = 158T + 52
[15,852], with K(T, 6T + 3) = (14T + 7) + 6 + 𝔢(21T + 16).

*[[lem:ii-a-8-5]] (b).* By [[sec:ii-a1-1-2]], B and I − B^♯ are microsupported in disjoint closed sets, near fibre
infinity. So Bℓ(I − B^♯), a product of three quantizations of order 0 (ℓ = Op(ℓ) as in (a)), is the case r = 3 of (e)
at the constant order 𝗍 := inf 𝗌_0 with N := max(0, ⌈sup 𝗌 − inf 𝗌_0⌉) ≤ T: it maps H^(𝗌_0) ⊂ H^(inf 𝗌_0) to
H^(inf 𝗌_0 + N) ⊂ H^𝗌. With S = 2T: R = 5T, B = 4T + 6, J_R = 6T + 1, J_C = 8T + 1, and the counts of
[[eq:fwd-ecount]] are at most 23T + 17, 10T + 8, 16T + 6, 32T + 7 and 34T + 15 [3,415]. So d_0 = 34T + 15 serves in
(b), and d_0 = 𝔐(T) a fortiori. The index does not depend on B and B^♯.

In every item the number of derivatives of any symbol is at most 158T + 52 ≤ 𝔐(T) − 2, and every product estimated
has at most eight factors, which justifies the choice of ϰ. ∎

#### The sites, the orders that occur, and the increments {#sec:fwd-box}

By [[eq:ii-f1-3-2]] and [[rem:ii-f1-7-1]] with d̄_ℵ = 1, D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) with: d^E_0 the d_0 of
[[thm:ii-e-6-1]] at (𝗌_0, 𝗌) = (𝗌 − 3, 𝗌); d^S_0 the largest d_0 of [[prop:ii-e-3-4]], [[prop:ii-e-4-3]] and
[[prop:ii-e-4-4]] at the slab orders 𝗌 and 𝗌 + 2; d^T_0 that of [[lem:ii-f1-2-8]] at 𝗍 = 𝗌; d^U_0 that of
[[prop:ii-e-3-4]] (i) at s′ = s_u = −12. By [[lem:fwd-orders]], 𝗌 has values in [−10, 11], equals 11 near the
horizon, the trapped set, ∂R_(∂K⁺,in) and ∂R_(ℐ⁺,in,+), and −10 near ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out); 𝗌_0 has values in
[−13, 8]. The a priori order of [[ch:s06]] is N′ := 13 = −inf 𝗌_0, which is all that its a priori terms
‖χu‖_(−N′) ≤ ‖u‖_(𝗌_0) require. A *site* is a result of [[ch:s04]] and [[ch:s06]]–[[ch:s09]] whose proof applies a
closed-graph index (an index of [[prop:ii-a1-2-4]] or of [[lem:ii-a-8-5]], directly or through another site), or
raises one. For s an order function write s⁺ := sup s and s⁻ := inf s. [[prop:fwd-calculus]] with T = 100 applies at
a site when (B1) every quantized symbol has order with values in [−100, 100], (B2) every Sobolev order on which an
item is applied has values in [−100, 100], (B3) every N in (e) and in [[lem:ii-a-8-5]] (b) is at most 100, (B4) every
product in (e), (f) has at most six quantizations, and (B5) each use of (f) has the form required there.

**Lemma {#lem:fwd-derived}** (The sites of [[ch:s04]].) Each site of [[ch:s04]] uses the items of
[[prop:fwd-calculus]] as follows, and satisfies (B1)–(B5) under the stated condition.

(D1) [[lem:ii-a-8-5]] (a) at 𝗌: item (a), 𝗆 = 0, 𝗍 = 𝗌. Condition |s^±| ≤ 100.

(D2) [[lem:ii-a-8-5]] (b) at (𝗌, 𝗌_0): (e), three factors, 𝗍 = s_0⁻, N = max(0, ⌈s⁺ − s_0⁻⌉). Condition |s_0⁻| ≤ 100,
s⁺ − s_0⁻ ≤ 100.

(D3) [[lem:ii-a-8-6]] at (𝗌, m, N): (D1) at 𝗌 − m and (D2) at (𝗌 − m, −N − m). Condition |𝗌 − m|, |N + m|,
s⁺ + N ≤ 100.

(D4) [[thm:ii-a1-3-1]] at (m, 𝗌, N), with J′ = ⌈2(s⁺ + N)⌉ steps of ½: (a) for Op(q) (order −m) and for the symbol of
order −1 in E_A; (b) for Op(q)Op(ℓ_f) − Op(qℓ_f) (orders −m, m); (e) for G_(i+1)Op(q)(I − G_(i+2))L and
G_(i+1)E_A(I − G_(i+2)), at most four factors, N ≤ s⁺ + N + |m| + 1, at 𝗍 = −N − |m|; (D1) for the a_j; (D3) (a) at
(−N, m, N). Symbol orders in [−|m| − 1, |m|]; Sobolev orders 𝗌 − j/2 − ½, 𝗌 − j/2 − m, j ≤ J′, in
[s⁻ − s⁺ − N − |m| − 2, s⁺ + |m|]. Condition s⁺ + N + |m| + 2 ≤ 100 and s⁺ − s⁻ + N + |m| + 2 ≤ 100.

(D5) [[thm:ii-a1-5-4]] at (m, 𝗌, N), with [[prop:ii-a1-5-3]], [[lem:ii-a1-4-1]], [[lem:ii-a1-4-2]], [[lem:ii-a1-2-6]]:
τ := max(1, s⁺ + N), 𝗌_j ∈ [s⁻ − τ, s⁺], σ_* := max(|s⁻ − τ|, |s⁺|), K′ := ⌈σ_*⌉ + m + 2. Symbols ǎ (order
𝗌_j − (m − 1)/2), b_ε, e_ε (𝗌_j + δ), b_ε², H_ℓ(ǎ²), φ_0b_ε²φ_0 (2𝗌_j + 2δ), ℓ_f (m), z_ε, λ_+, λ_+z_ε, τ_t,
localisers, and in the parametrix step q = χ̃ab⁻¹ (−𝗌_j): orders in [−2σ_* − m − 1, 2σ_* + m + 1]. Sobolev orders
𝗌_j − κ, 𝗌_j − ½ + δ_0, 𝗌_j − m + 1, ±(m − 1)/2, −N, −N − m, −δ, K′, and those of the parametrix iteration from 𝗌_j
down to −N − σ_* − 1: all in [−σ_* − N − m − 2, K′]. (e): Φ_0L(I − Φ), Φ_0T_t(I − Φ), Φ_0T_tL(I − Φ) and those of the
parametrix step, at most four factors, N ≤ s⁺ + N + σ_* + m + 2. (f): the expressions (F1)–(F4) of [[lem:fwd-box]],
at most five factors. With (D4) at (m, 𝗌, N) and (D3) (a) at (−N, m, N). Condition 2σ_* + m + 1 ≤ 100,
σ_* + N + m + 2 ≤ 100, K′ ≤ 100, s⁺ + N + σ_* + m + 2 ≤ 100.

(D6) [[prop:ii-a-9-1]] at (m, 𝗌, N): (D4) at (m, 𝗌, N), (D3) at (𝗌, m, N) and (−N, m, N). (D7) [[prop:ii-a-9-2]]:
(D5) at (m, 𝗌, N), (D3) (a) at (−N, m, N), and 2. (D8) [[prop:ii-a-9-6]] at (𝗌, 𝗌_0): (D1) at 𝗌, (D2) at (𝗌, 𝗌_0).
(D9) [[cor:ii-a-9-7]] at (𝗍, m): (D8) at (𝗍 − m, 𝗍 − m). (D10) [[prop:ii-a-9-8]] at (𝗌, m, N): (D8) at
(𝗌 − m, −N − m), (D6), (D9) at (−N, m). (D11) [[prop:ii-a-9-9]] at (𝗌, m, N): (D8) at (𝗌 − m + 1, −N − m), (D7),
(D9) at (−N, m). Conditions: those of the sites invoked.

[[lem:ii-a-8-4]], [[lem:ii-a1-1-1]], [[lem:ii-a1-1-2]], [[lem:ii-a1-2-3]], [[lem:ii-a1-2-5]], [[lem:ii-a-8-7]] and
[[lem:ii-a-9-5]] concern smooth operators or functions, or have explicit regularity, and are not sites. No index of
these results depends on k, on the auxiliary operators, on the cut-offs or on the finite sets of operators.

*Proof.* The lists are read from the proofs cited: for (D4) the steps *One step*, *Localisation* and *Iteration* of
[[thm:ii-a1-3-1]] with 𝗋 = 0, 𝗋′ = 𝗌 − j/2, δ = ½; for (D5) the steps 0–3 of [[lem:ii-a1-4-1]], the iteration of
[[lem:ii-a1-4-2]] over 𝗌_j = 𝗌 − τ + jκ with its parametrix step (q := χ̃ab⁻¹, B_0^((j)) of order 𝗌_j + δ in place
of L), the commutant, commutator and positivity paragraphs of [[prop:ii-a1-5-3]], and *The index* of
[[thm:ii-a1-5-4]], whose τ is max(1, s⁺ + N); for (D6)–(D11) the first sentences of their proofs, which take maxima.
The ranges follow from the orders listed, as 𝗌_j and 𝗌 − j/2 have values in [s⁻ − τ, s⁺], resp.
[s⁻ − s⁺ − N − 1, s⁺]. In (D2) the case (e) applies by [[sec:ii-a1-1-2]] (proof of [[prop:fwd-calculus]]). ∎

**Lemma {#lem:fwd-box}** (The sites of [[ch:s06]]–[[ch:s09]], and the orders that occur.) The sites of
[[ch:s06]]–[[ch:s09]] that enter D_0, the sites of [[ch:s04]] they invoke with their parameters, and their increments
are the following. The increment of a site is the number by which its own regularity requirement exceeds the index of
the items of [[prop:fwd-calculus]] and [[lem:ii-a-8-5]] that it applies; its index is the larger of that requirement
and the indices of the sites it invokes. [[ch:s08]] contains no site: its operators (the ι⁺-normal operator and its
Mellin family) have smooth coefficients, and no class C^((d_0;k)) occurs in it. In [[ch:s09]], [[sec:ii-f-6]]–
[[sec:ii-f-8]] apply [[thm:ii-a1-3-1]] and [[thm:ii-a1-5-4]] to the smooth operators P_+, P^ε_+ and P_0 only, and
[[lem:s09-off-star]], [[lem:ii-f1-2-5]] are explicit (Seeley's extension); they are not sites.

(R) The radial estimates [[prop:ii-d-3-1]], [[prop:ii-d-3-2]], [[prop:ii-d-3-3]], [[prop:ii-d-3-5]], [[prop:ii-d-3-6]]
at constant (s, s_0), with [[lem:ii-d-2-1]]–[[lem:ii-d-2-5]] and the localised form of [[sec:ii-d-2]]: the pattern is
(D5) at (2, s, N′) with τ := s − s_0 ≤ s + N′ and constant orders; increment 1, as the symbols b_ε, e, j_ε, f_ε of the
pattern lie in C^(d_0−1) (they contain ρ⁻¹𝖧ρ and σ_1(Im_h P), with one derivative of the coefficients). (F3), (F4).

(Γ) The trapped set [[prop:ii-d-4-2]] at (s, s_0): commutants of orders in [s_0 − 3, s + 3] (as stated there), the
symbol ã of order 2s′ + 1 ≤ 2s + 1, products of order at most 2s + 7: symbol orders in [2s_0 − 7, 2s + 7]; Sobolev
orders in [−N′ − 3, |s| + 6]; (e) for G_1R_2^♭, G″R_2^♭, Φ_0(I − Φ′), Φ_0L(I − Φ′), (I − Φ′)^*Op(j_ε)Φ_0, at most four
factors, N ≤ s + N′ + 3; (f) as (F3), (F4) and [Φ_u, A_ε] (four factors). Increment 4: the symbols lie in C^(d_0−4)
([[lem:ii-d-4-1]], from ϕ^u ∈ C^(d_0−1), ϕ^s ∈ C^(d_0−2) of [[prop:ii-c1-3-4]]), and [[lem:ii-d-4-1]] asks d_0 ≥ 5.

(G) [[thm:ii-d-1-2]] at (𝗌_0, 𝗌): (D4) and (D5) at (2, 𝗍, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}; (R) at (12, 8) (horizon,
∂R_(ℐ⁺,in,+), ∂R_(∂K⁺,in)) and (−10, −13) (∂R_(∂K⁺,out), ∂R_(ℐ⁺,out)); (Γ) at (11, 8). Increment 0.

(I) [[lem:ii-d1-2-3]] at (𝗍, 𝗍_0, 𝔩) and [[lem:ii-d1-2-5]]: (R), resp. (Γ), at (𝗍, 𝗍_0) for the systems L^(k), whose
coefficients keep d_0 e3b-derivatives ([[lem:ii-d1-2-1]]); (D1) at 𝗍_0 − 2; (D2) at (𝗍 − 1 + 𝔩, 𝗍_0 − 2); (D3) (b) at
(𝗍 + 1 + 𝔩, 2, −𝗍_0). Increment 0. (Tm) [[lem:ii-d1-2-4]]: (D8) at (𝗍 + 1 + 𝔩, 𝗍_0) and (𝗍_0 − 2, 𝗍_0 − 2), (D9) at
(𝗍_0, 2); increment 2 (d_0 ≥ d_1 + 2). Used at (12, 8, 0), (11, 8, 1), (−10, −13, 0) by [[prop:ii-d1-3-2]],
[[prop:ii-d1-4-2]], [[prop:ii-d1-5-2]], [[prop:ii-d1-6-2]].

(B) [[thm:ii-d1-1-1]] at (𝗌_0, 𝗌): (G); (D6) and (D7) at (2, 𝗍, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}; (I), (Tm) at the three triples
above; (D10) and (D11) at (𝗍, 2, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}. Increment 0.

(Sl) [[lem:ii-e-3-3]] (a) at slab orders (𝗌_0, 𝗌), (b) at constants (s_0, s): (D4), (D5) at (2, 𝗌, −s_0⁻) and
[[prop:ii-e-3-2]] at the values near R, which is (R) with increment 2 (h̃_F ∈ C^(d_0−2), [[lem:ii-e-3-1]]).

(Sv) [[prop:ii-e-3-4]] at a slab order 𝗌 and s′: (i) is (Sl) (a) at the constants (s′, 2); (ii) is (Sl) (a) at
(min(0, s⁻) − 1, 𝗌) (Step 2) and at (−m, 𝗌), m the least integer with m > 1 − s⁻ (Step 4), and (Sl) (b) at (0, m + 1)
(Step 3). The energy estimates need d_0 = 2 ([[lem:ii-e-2-5]], [[prop:ii-e-2-7]]). Increment 0.

(W) [[lem:ii-e-4-1]] (a) at (𝗌, m): (D1) at 𝗌 − m; (b) at 𝗌: (D8) at (𝗌, 𝗌). (Sb) [[prop:ii-e-4-3]] at 𝗌: (Sv) at 𝗌 for
the systems P^(j), with (i) at s′ = s⁻ − 1, and (W) (a) at (𝗌, 1). The uniqueness step of the induction is taken at
s′ = s⁻ − 1 ([[prop:ii-e-4-3]], [[prop:ii-e-5-6]] (a)).

(St) [[prop:ii-e-4-4]] at 𝗌: (Sb), and (W) (b) at 𝗌 + 1 and 𝗌 − 1; increment 2 (d_0 ≥ d_1 + 2).

(K) [[lem:ii-e-5-3]], [[prop:ii-e-5-4]] and [[prop:ii-e-5-6]] at 𝗌 and s′: as (Sl), (Sv), (Sb), (St), with no radial
set; [[prop:ii-e-5-6]] (b) has increment 2.

(E) [[thm:ii-e-6-1]] at (𝗌_0, 𝗌): (Sv) (i) and (K) (i) at s′ = s_0⁻ = −13, (Sb) and (St) at 𝗌, (B) at (𝗌_0, 𝗌), (K) at
𝗌 with s′ = −13. Increment 0.

(T) [[lem:ii-f1-2-8]] at 𝗍: (D9) at (𝗍, 2), (D1) at 𝗍 − 2. (U) [[lem:ii-f1-2-2]]: (Sv) (i) at s′. (F) [[lem:ii-f1-2-9]]:
(St) at 𝗌 + 2, and [[thm:ii-f-8-1]] for the smooth P_0. Increment 0.

The expressions to which (f) is applied, each with at most five quantizations in a product, and the reason why its
symbol t_α in every chart has no term above the order stated: (F1) [D_a, Op(ǎ)] and [[D_a, Op(ǎ)], Op(ǎ)],
D_a = Op(a)^* − Op(a^*), orders m + 𝗄 − 2 and m + 2𝗄 − 3: the terms of index 0 of D_a cancel ((c)), and ǎ is scalar, so
the terms of the commutators that are not of positive grade in each commutator vanish. (F2) [D_R, Ǎ], [D_I, Ǎ],
Ǎ = Op(ǎ)Φ_0, i[L_R, D_ǎǍ] and Ǎ^*[Ǎ, D_I] in [[prop:ii-a1-5-3]], order m + 𝗄 − 2, resp. 2𝗌 − 1: as (F1), with
φ_0ǎ = ǎ, and the terms of positive index of the symbol of Φ_0 vanish near supp ǎ, as each carries a ξ-derivative of
φ_0 (η enters the amplitude only through φ_0, [[lem:fwd-transport]]) and φ_0 = 1 there. (F3)
L_IǍ_ε^*Ǎ_ε + Ǎ_ε^*Ǎ_εL_I − Op(2ǎ_ε²ℓ_I) and i[L_R, Ǎ_ε^*Ǎ_ε] − Op(H_ℓ(ǎ_ε²)) in [[lem:ii-d-2-3]], order 2s − 1:
ǎ_ε is scalar, φ_0ǎ_ε = ǎ_ε, and ℓ_I, the principal symbol of L_I, is in every chart the part of order m − 1 of the
symbol of L_I: for smooth coefficients this is (S5), and both sides are the same polynomial in finitely many
derivatives of the coefficients and of the transition maps, so the identity persists in finite regularity
([[lem:ii-a1-2-2]]); likewise H_ℓ(ǎ_ε²) is the principal symbol of i[L_R, Ǎ_ε^*Ǎ_ε] ((d)).
(F4) Op(ρ^(−𝗍)φ_εz)Φ_z − Op(ρ^(−𝗍)φ_εzφ_z) and the products of [[lem:ii-d-2-5]], [[lem:ii-a1-2-6]], [[lem:ii-d-2-4]],
order one below the sum: φ_zz = z and the terms of index 0 agree ((b)). [Φ_u, A_ε] in [[prop:ii-d-4-2]] is (b), (d)
for scalar symbols.

At the parameters of the operator of [[thm:iii-i-5-3]], (B1)–(B5) hold at every site, and the indices satisfy:
every symbol order lies in [−71, 71], every Sobolev order in [−51, 38], every N of (e) is at most 63.

*Proof.* The lists are read from the proofs cited, for (Sb) and (K) with the uniqueness step at s′ = s⁻ − 1 as said
there. The parameters at which (D4), (D5) are used:
(G), (B): (2, 𝗌 + 1, 13) with s⁺ = 12, s⁻ = −9, τ = 25, σ_* = 34; (2, 𝗌, 13) with τ = 24, σ_* = 34. (Sv) at 𝗌:
Step 2 at (2, 𝗌, 11), τ = 22, σ_* = 32; Step 4, m = 12, at (2, 𝗌, 12), τ = 23, σ_* = 33; Step 3 at (2, 13, 0), σ_* = 13;
(i) at (2, 2, −s′) with s′ ∈ {−9, −11, −12, −13}, σ_* ≤ 13. (Sv) at 𝗌 + 2 (s⁺ = 13, s⁻ = −8): Step 2 at (2, 𝗌 + 2, 9),
τ = 22, σ_* = 30; Step 4, m = 10, τ = 23, σ_* = 31; Step 3 at (2, 11, 0). (K): as (Sv) at 𝗌. (R) at constant
s ∈ {12, −10, 13, 2, ≤ 13}: σ_* ≤ 13. So σ_* ≤ 34, and (D5) gives symbol orders in [−2·34 − 3, 2·34 + 3] =
[−71, 71], Sobolev orders in [−34 − 13 − 4, 34 + 4] = [−51, 38], and N ≤ 12 + 13 + 34 + 4 = 63; (D4) gives
N ≤ 12 + 13 + 3 = 28 and Sobolev orders down to −9 − 12 − 13 − 4 = −38. (Γ) at (11, 8): symbol orders in [9, 29],
Sobolev orders in [−16, 17], N ≤ 27. The (D2)-instances: (D8) at (13, 8), (−9, −13), (6, 6), (−15, −15) and (𝗋, 𝗋)
for 𝗋 ∈ {𝗌 − 2, 𝗌 − 1, 𝗌 + 1, 𝗌 + 3} (N ≤ 21, s_0⁻ ≥ −15); (D10), (D11) at (𝗍, 2, 13): (D8) at (𝗌 − 2, −15),
(𝗌 − 1, −15), (𝗌, −15) with N ≤ 26; (I): (D2) at (11, 6) and (−11, −15), N ≤ 5; (D3) at (𝗍, 2, 13),
𝗍 ∈ {𝗌, 𝗌 + 1}: N ≤ 25. All lie in the box, and the expressions have at most five quantizations. ∎

**Lemma {#lem:fwd-increments}** (The increments.) Every coefficient index entering D_0 is at most 𝔐(100) + 4.

*Proof.* By [[lem:fwd-box]] and [[lem:fwd-derived]], every index entering D_0 is a maximum over sites, and each site's
index is the larger of 𝔐(100) plus its increment and the indices of the sites it invokes, ending at the items of
[[prop:fwd-calculus]] (index M + 2 = 𝔐(100) for [[prop:ii-a1-2-4]], d_0 = 𝔐(100) for [[lem:ii-a-8-5]]) at orders that
satisfy (B1)–(B5). The increments, site by site: (D1)–(D4), (D6), (D8)–(D11) have increment 0 (they take maxima);
(D5) has 2 ([[thm:ii-a1-5-4]], *The index*: the flow box of [[lem:ii-a1-5-2]] has d_0 − 1 derivatives, the commutant
symbols d_0 − 2, so d_0 − 2 ≥ M′ + 2, that is d_0 ≥ 𝔐(100) + 2); (D7) has 0 beyond (D5); (R) has 1; (Γ) has 4; (Sl),
through [[prop:ii-e-3-2]], has 2; (Tm), (St) and [[prop:ii-e-5-6]] (b) have 2 (d_0 ≥ d_1 + 2, d_1 = 𝔐(100) being the
index of (D8)); (G), (I), (B), (Sv), (W), (Sb), (K), (E), (T), (U), (F) have 0. Increments do not add along a chain:
(D5), (R), (Γ) and (Sl) raise the regularity required of the symbols they quantize, and (Tm), (St) the regularity of the
coefficients of P − P_0 above that of (D8), each above the index of the items it applies, and the site above takes the
maximum. So, by induction over the sites, every index is at most 𝔐(100) + 4, attained only at (Γ). The energy
estimates need d_0 = 2 ([[lem:ii-e-2-5]], [[prop:ii-e-2-7]]) and [[lem:ii-d-4-1]] asks d_0 ≥ 5. ∎

*Proof of [[thm:fwd-loss]].* By [[lem:fwd-increments]], D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) ≤ 𝔐(100) + 4 =
20,104. By [[lem:fwd-orders]] and [[lem:fwd-tame]], d′ = 10, d″ = 11 and D_1 = 49. So by [[eq:fwd-split]]
d ≤ 20,104 + 49 + 10 + 11 + 1 + 5 = 20,180, and the theorem holds with any larger d, in particular with d = 20,180. ∎

**Remark {#rem:fwd-sharpness}** (Sharpness.) Only the term D_0 is crude. The counts of [[prop:fwd-calculus]] at T = 100
are at most 15,852 (item (f) with six quantizations), so the same proof gives D_0 ≤ 15,858 and d ≤ 15,934; the value
𝔐(100) = 20,100 keeps a margin. Counting each application of the calculus at its own orders (symbol orders at most 71,
Sobolev orders in [−51, 38], at most five quantizations, by [[lem:fwd-box]]) would lower D_0 further. The terms d′, d″
and D_1 are the exact values that the proofs of [[sec:ii-f1-3-1]], [[thm:ii-e-6-1]] and [[prop:ii-e-4-4]] fix for
these orders.

<!-- Statements of other chapters that this section cites with explicit values (texts 7 to 12). Each is placed in its
chapter, and this comment is deleted at placement.

Text 7. In prop:ii-a1-2-4 (ch:s04), after the sentence that ends with
  Throughout, "order 𝗋" means bounded from H^𝗍 to H^(𝗍−𝗋).
add (Θ in place of T, as T(a_1, …, a_r) denotes an expression there):
  For Θ ∈ ℕ, when 𝗍 and the orders of all quantized symbols have values in [−Θ, Θ] (of any index ν), M := 200Θ + 98
  serves in (a)–(d); in (e) for N ≤ Θ and expressions with at most six quantizations in each product (B_1, B_2 and the
  localisers included); and in (f) for expressions with at most six quantizations in each product whose formal symbol
  in every chart is a sum of terms of pointwise order at most μ, an order function with values in [−6Θ − 3, 6Θ + 3]
  ([[prop:fwd-calculus]] with T := Θ, which proves (e) without the commutator expansion).

Text 8. In the notation paragraph at the start of ch:s06, replace
  N′ is a fixed large integer;
by
  N′ is a fixed integer with N′ ≥ −inf 𝗌_0 for every order 𝗌_0 (or s_0) of an a priori term below (N′ = 13 for the
  operator of [[thm:iii-i-5-3]]);

Texts 9 to 11. ch:s07 already reads as follows, which is what lem:fwd-box uses; nothing is to be placed.
  In the proof of prop:ii-e-4-3: "so a priori u″^(j) ∈ H^(𝗌−1,2α−1)(Ω″)^(•,−). The threshold holds also for the weight
  α − 1/2, so by [[prop:ii-e-3-4]] (i) for P^(j) at that weight and at s′ = inf 𝗌 − 1, …".
  In the proof of prop:ii-e-5-6 (a): "a priori v″^(j) ∈ H^(𝗌−1,α_K−1)(Ω″)^(•,−). By [[prop:ii-e-5-4]] (i) for P^(j)
  at the weight α_K − 1, with inf 𝗌 − 1 for its s′, …".
  In prop:ii-e-5-4: "There are d_0, depending only on 𝗌 (and, in (i) and (iii), on s′), and C, …".
  In prop:ii-e-5-6: "… 𝗌 a slab order and s′ ∈ ℝ. (a) There is d_0, depending only on 𝗌 and s′, such that …
  every u ∈ H^((s′;k),α_K)(Ω^K_([a,b]))^• with f := Pu satisfies …".

Text 12. In lem:ii-a-8-5 (ch:s04), after (b), add (Θ in place of T, as T denotes a map in the proof there):
  For Θ ∈ ℕ, d_0 = 200Θ + 100 serves in (a) when 𝗌 has values in [−Θ, Θ], and in (b) when 𝗌_0 has values in
  [−Θ, Θ] and sup 𝗌 − inf 𝗌_0 ≤ Θ ([[prop:fwd-calculus]] with T := Θ, which proves (b) without the commutator
  expansion).
-->
