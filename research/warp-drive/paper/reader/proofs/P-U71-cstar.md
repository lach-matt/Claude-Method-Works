### The single-step losses at the computational point {#sec:cs}

[[thm:uc-integer]] bounds d_acc and d_R by D_e + M_c c_*, where c_* is the largest of the numbers c(β_k), c_b, c′_b and
c_0 defined before [[prop:ec-upper]] and of their counterparts c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]. Each
of these numbers is assigned by [[def:ec-accounted-loss]] to a finite composition of elementary families. This section
lists, step by step, the families that each of them composes, bounds the charge of every one of them at the choice of
[[def:uc-choice]], and adds the charges. Two counts of index sets dominate the result: the count n_ι of the Fourier
transform in Step 0 of the proof of [[prop:iii-i11-3-1]], at most N_ι by [[lem:uc-n-iota]], and the count n_K of the
K⁺-exponents of the inverse transform in its Step 7, at most N_ι + N_Λ ([[lem:cs-fourier]]). A level step below 3 is
charged at most 497, a round and a step of the base at most 469 and 466, a level step above 3 at most 2N_ι + N_Λ + 529
([[lem:cs-levels]], [[lem:cs-base]]), and c_0, which contains three runs of the top level, less than
6N_ι + 1.74·10²⁸ ([[lem:cs-rest]]). So c_* < 6.4368·10³⁵ ([[prop:cs-cstar]]).

Throughout we write

    N̄_Λ := 16,747,199,999,999,     k̄_max := 3 + 765,000,816 · N̄_Λ = 12,811,621,665,714,434,999,187,

so that N_Λ ≤ N̄_Λ and k̄(λ) ≤ k̄_max for every λ ∈ Λ with Re λ < 3 + ε_+ ([[lem:uc-lambda]] (a), (c)), and N_ι is the
number of [[eq:uc-n-iota]]. Weights, levels and the loss ε are those of [[def:uc-choice]]; in particular
3 + ε_+ < ℓ_I < 3.5, α ≤ 4 + ε_K, and ε ≤ 10⁻³ε_g < 10⁻¹².

#### The rule of addition and the free choices {#sec:cs-rules}

**Lemma {#lem:cs-sum}** (Charges add.) (a) Let an expression be built by compositions, sums and finite-rank
assemblies from applications of elementary families, each charged a non-negative integer. The number that
[[def:ec-accounted-loss]] assigns to it is at most the sum of the charges of the applications it contains.

(b) Let M be a map built in this way, ℓ_1, …, ℓ_m functionals computed by maps built in this way, and v^i = M(s^i) for
sources s^i whose families are charged at most 11. Then e ↦ M(e) + Σ_i ℓ_i(e)v^i is assigned at most A_M + A_ℓ + 11,
where A_M and A_ℓ are the sums of the charges of the applications in M and in the computation of the ℓ_i.

*Proof.* (a) By induction over the expression: a composition is assigned the sum of the numbers of its factors, and a
sum or an assembly the largest of the numbers of its parts, which is at most their sum, all numbers being non-negative.
(b) The map is a sum of M and of a finite-rank assembly; [[def:ec-accounted-loss]] assigns the assembly the largest of
the numbers of its parts, the functionals (at most A_ℓ by (a)) and the families v^i (at most A_M + 11 by (a)). So the
sum is assigned at most max(A_M, A_ℓ, A_M + 11) ≤ A_M + A_ℓ + 11. ∎

Every elimination of finitely many parameters in [[ch:s20]]–[[ch:s23]] has the form of (b): the forward solution for
the forcing F − D_(p⃗)P(p⃗′) is the solution for F plus Σ_i p′_i times the solutions for the fixed directions
−D_(p⃗)P(e_i), which are background sources ([[lem:iii-j2-2-1]] (b)), and p⃗′ is a finite-dimensional linear function
of coefficients read from the expansion of the solution. This is the way in which the finite-dimensional data enter
in the proof of [[prop:ec-upper]]. So each statement whose proof eliminates parameters is charged at most the sum of
the charges of the statements it applies, each counted once, plus 11.

**Definition {#def:cs-choices}** (The free orders and inner products.) At the choice of [[def:uc-choice]] we take,
besides:

(a) at the incoming radial sets of (2L_b)^(σ) and of N_tf((2L_b)^(·), ±1), the fibre inner product of
[[lem:ec-theta-in-zero]], in which ϑ_in = 0; at the horizon the fixed fibre inner product of [[lem:iii-f2-1-1]] with
δ = ¼, the neighbourhood ℬ_* being taken inside the neighbourhood of b₀ that this lemma gives, so that
ϑ_ℋ < ϑ_L + ¼ < 9/4 on ℬ̄_*; and the regularity order s_c := 3 > ½ + 9/4;

(b) in [[prop:ii-g1-4-4]], as [[cor:ii-g1-4-5]] applies it, the incoming order 𝗋_in := −¼ and the semiclassical order
𝖻 ≡ 0, and in [[cor:ii-g1-4-5]] the weight β′_I := 3/2 − 2ε where it is applied with an ℐ⁺-weight below 3/2;

(c) in [[lem:iii-i2-4-1]] the weights N := 5 of u_hi at ι⁺ and K⁺;

(d) in the proofs of [[lem:iii-i1-2-2]] and [[prop:iii-i1-2-1]], at each step other than Step 2 of the proof of
[[lem:iii-i1-2-2]], an increment η ∈ [2/5, ½) off the finitely many excluded values, or the remaining distance to the
target weight when that is smaller;

(e) in every application of [[cor:iii-f1-3-4]], the choices of [[prop:uc-ltf]].

These choices are allowed. (a): [[lem:ec-theta-in-zero]] gives the inner product at the incoming radial sets,
which (O3) of [[def:i-a-admissible]] chooses separately for each radial set; [[lem:iii-f2-1-1]] gives ϑ_ℋ < ϑ_L + δ on a
neighbourhood of b₀ with ϑ_L = max(0, 2 − 2x) < 2; and the proofs of [[cor:ii-g1-4-2]], [[prop:ii-g1-4-7]],
[[lem:iii-i2-4-2]] and [[cor:ii-g1-4-5]] ask only s_c > ½ + ϑ_ℋ ([[lem:ec-closed-forms]] (b)). (b): the admissible orders
before [[lem:ii-g1-4-3]] ask 𝗋_out < −½ + S̄ = −½ and 𝗋_in ≥ 𝗋_out with 𝗋_in > ½(−1 + ϑ_in) = −½, and 𝗋_out =
β_scf − 2 − ε/2 < −½ for β_scf < 3/2; [[cor:ii-g1-4-5]] allows every β′_I below min(β_I, 3/2). (c): [[lem:iii-i2-4-1]]
holds for every N, and every use of u_hi below needs at ι⁺ and at K⁺ weights below 5 (the targets are at most
3 + η_2 at ι⁺ and α − ε at K⁺). (d): each step there asks only η < ½, α_I + η below the target, and finitely many
exclusions. (e) is [[prop:uc-ltf]].

#### The elementary charges {#sec:cs-elem}

**Lemma {#lem:cs-elem}** (The charges of the elementary families.) At the choices of [[def:uc-choice]] and
[[def:cs-choices]], every application of the following families in the constructions of [[thm:iii-i14-3-1]],
[[thm:iii-j1-2-1]] and [[lem:iii-k-2-3]] is charged at most:

(a) 0: finite-dimensional maps, coefficient functionals and finite-rank maps with fixed sections, among them the
inverses and functionals of [[lem:iii-j2-2-1]] (c), the assigned rotation coordinates A_b and the states, rows and
towers; the integrations of [[lem:iii-a-1-2]], [[lem:iii-a-3-2]], [[lem:iii-a-3-3]] and [[lem:iii-i2-2-1]];
[[cor:iii-h-4-2]] and [[lem:iii-i2-4-3]]; multiplication by smooth functions, by cut-offs and by powers of σ, |σ| and
sgn σ; the Mellin inversion of an elliptic dilation-invariant operator on a line free of indicial roots; Cauchy
integrals and residues over fixed circles; the expansions of [[thm:iii-g4-3-1]] and of Step 2 of the proof of
[[prop:iii-g4-5-1]]; the tails of [[lem:iii-i10-2-4]]; [[lem:iii-i12-2-1]] (b); and the subtractions of
[[lem:iii-i12-2-4]];

(b) 1: [[prop:ii-g1-3-3]] (1), [[prop:iii-h-3-2]] (L̃_b(0)⁻¹) and [[cor:iii-f1-3-4]];

(c) 2: the fixed second-order operators L_b, L̂_b(σ) and L̃_b at the background 0, their parts L_0, L_1, L_2, and their
commutators with cut-offs;

(d) 11: the families of [[lem:iii-j2-2-1]] (b) applied to a solution or to a fixed section, among them the sources
f^S, f^b, f^s1, f^ν, r^ν, Δ_q, R_q, the errors E^ν, the differences (L − L_b)u, the remainder L̃ of [[lem:iii-i1-1-1]]
for L = L^(g,g_0), and the sources e_S, e_(S⁰) of the proof of [[lem:iii-k-2-3]];

(e) 20,183: the forward solution operators of [[lem:iii-j2-2-1]] (a);

(f) 3: [[prop:iii-g4-4-4]], for the solution and for the remainder; 2(⌊ℓ_zf⌋ − k₀ + 1)_+ + 3 ≤ 9:
[[prop:iii-g4-5-1]]; 1: [[thm:iii-g4-3-1]];

(g) 8: the expansion of [[lem:iii-a-1-4]] as [[lem:iii-i11-2-1]] applies it; so [[lem:iii-i11-2-1]] is charged at
most 9, and the map g ↦ g^(+1) of [[lem:iii-i11-2-2]] at most 2;

(h) 30: the right inverse of [[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1).

*Proof.* (a) These are the losses 0 of [[rem:ec-other-losses]] (the finite-dimensional maps of [[lem:iii-j2-2-1]] (c),
the integrations of its (d), [[cor:iii-h-4-2]] of its (e) and [[lem:iii-i2-4-3]] of its (g)); [[lem:iii-a-3-3]] is an
integration of the kind of [[lem:iii-a-1-2]], one factor at a time. Multiplications by smooth functions with bounded
b-derivatives, and by |σ|^z, σ^j, sgn σ (which shift weights only), keep the order k. The Mellin inversion of
[[eq:iii-g4-5-3]] and of [[lem:iii-a-1-4]] gains, by (E1)–(E2) of [[sec:iii-a-1-1]], as many orders as the operator
has, jointly in the Mellin variable and on the boundary. A Cauchy integral over a fixed circle on which a family is
holomorphic and bounded at each order keeps the order. The expansions of [[thm:iii-g4-3-1]] and of Step 2 of the proof
of [[prop:iii-g4-5-1]] cost nothing, by the first fact in the proof of [[lem:ec-round-charges]]. [[lem:iii-i10-2-4]],
[[lem:iii-i12-2-1]] (b) and [[lem:iii-i12-2-4]] read coefficients and subtract finitely many terms, each a function of
t_* with finite-dimensional coefficients times a fixed profile; in [[lem:iii-i12-2-1]] (b) the remainder R is a sum of
explicit kernels e_(j,r) times the profiles, with the b-derivatives of the profiles at the same order.

(b) and (c) are the losses 1 and 2 of [[rem:ec-other-losses]], and ℓ_tf = 1 is [[prop:uc-ltf]].

(d) By [[prop:uc-dbg]], these families have split loss (2; 11, 2), so they are tame with loss 11, which is the charge
max(2, d_BG) = 11 of [[rem:ec-other-losses]]. The sources e_S and e_(S⁰) are differences of the sources f^S, f^s1 at
the two base points Φ(U) and Ψ(U), and D_hP_5(Ψ(U)) applied to the fixed sections χ_−∂_S H(S′), χ_−∂_(S⁰) H(S⁰′);
each is a coefficient polynomial in the metric, its inverse and their derivatives of order at most two applied to a
fixed section, and the proof of [[prop:uc-dbg]] applies to it. The errors E^ν are bounded by C|b − b₀||W| in a fixed
seminorm ([[lem:s25-p6]]), so they are charged at most 11 as well.

(e) By [[thm:fwd-loss]], [[eq:iii-i-5-2]] holds with d = 20,180 for g = g₀ + h. By [[lem:iii-j2-2-1]] (a), for the
backgrounds h̃ = h + h^(−1)(S), h + h_tot(p⃗) and h + h_rem(q) + h_tot(p⃗) it holds with ‖h̃‖_(𝒳^(k+d)) in place of
‖h‖_(𝒳^(k+d)), the backgrounds g₀ and h_tot(p⃗) adding coefficients smooth in p⃗. By [[lem:iii-i4-2-5]],
[[lem:iii-i9-2-5]] and the first paragraph of the proof of [[prop:uc-dbg]], ‖h̃‖_(𝒳^m) ≤ C_m(‖h‖_(𝒳^m) + |S| + |p⃗| +
‖q‖_(𝒬^(m+3))). So these families satisfy [[eq:iii-j2-1-1]] with the loss 20,180 + 3 = 20,183.

(f) For [[prop:iii-g4-4-4]] this is the proof of [[lem:ec-round-charges]] (b), which uses nothing particular to the
levels 1 and 2: the solution costs at most ℓ_tf = 1 and the remainder ℓ_tf + 2 = 3, and the derivatives in α₀ of
Step 2 of its proof are Cauchy integrals. In the proof of [[prop:iii-g4-5-1]], Step 1 runs for
j = k₀, …, ⌊ℓ_zf⌋, at most 3 values, as ℓ_zf < 3. Each v_j solves [[eq:iii-g4-5-3]] at no cost, by (a), from
f^((j)), which is a coefficient of f minus g_j; g_(j+1), the terms of the second kind and the commutators apply to U_j
operators of order at most 2, the parts of L̂_b(σ) − L̄̂(σ), ρ(ρ∂_ρ − 3/2 − S̄) and the commutators with the cut-offs
(charge 2 by (c)); f₁ collects them. In Step 2, u₁ = N_tf⁻¹(|σ|^(−α)f₁) costs 1 by (b), its expansion
[[eq:iii-g4-5-5]] and u₂ cost nothing by (a), and f₁ − L̂_b(σ)u₂ costs 2. Along a chain these add to at most
2(⌊ℓ_zf⌋ − k₀ + 1)_+ + 1 + 2. [[thm:iii-g4-3-1]] composes [[cor:iii-f1-3-4]] with its expansion.

(g) In [[lem:iii-i11-2-1]], [[prop:iii-h-3-2]] costs 1. The expansion from the conormal order q − 2 > 0 to q′ − 2 ≤ 3
is obtained by the iteration of the proof of [[lem:iii-a-1-4]] with A = ρ⁻²L̂_b(0) near ∂X, each step of which raises
the weight by at least ¾ when its small number is taken at most ¼; so at most 4 steps occur, and each applies
A − N(A), of order 2 (charge 2), followed by N(A, ·)⁻¹ and a contour shift (charge 0 by (a)). This gives 8, and
1 + 8 = 9. In [[lem:iii-i11-2-2]], g^(+1) is the explicit sum of that lemma: L_0, L_1, L_2 and commutators applied to
û (charge 2), and divisions by σ and the column terms, of charge 0.

(h) is [[lem:ec-closed-forms]] (f) at 3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ_ι < 3.5 − ℓ_I, which
[[def:uc-choice]] imposes, with the bound 2 + sup d_ι < l′ for the right inverse given in its proof. ∎

**Lemma {#lem:cs-transforms}** (Transforms and stationary inverses.) At the choices of [[def:uc-choice]] and
[[def:cs-choices]]:

(a) [[prop:ii-g1-3-3]] (2), applied to a forcing of weights (β^f_I + 1, β_ι + 2, β_K) with β^f_I ≤ ℓ_I, β_ι ≥ ½ and
β_K > 0, is charged at most 3;

(b) [[prop:ii-g1-3-5]] (1), and the transform bound (T3) inside [[prop:iii-a-4-2]], are charged
ℓ_F = ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉, which is at most 5 when β_ι − β_scf ≤ 5 and β_K ≤ 5;

(c) [[prop:ii-g1-3-5]] (2) is charged at most 5 in [[lem:iii-i2-4-1]], and 6 in [[cor:ii-g1-4-5]] there;

(d) [[cor:ii-g1-4-2]] (2) at β_scf = 3/2 − ε, and [[prop:ii-g1-4-7]] and [[lem:iii-i2-4-2]] at β_scf ∈ [3/2 − 3ε, 3/2),
are charged 2;

(e) [[cor:ii-g1-4-5]], as [[lem:iii-i2-4-1]] applies it, is charged at most 20, and [[lem:iii-i2-4-1]] at most 30;

(f) [[lem:iii-i2-3-1]], at its applications in the proofs of [[prop:iii-i2-5-1]], [[prop:iii-i3-2-1]] and
[[prop:iii-i5-2-1]], is charged at most 2.

*Proof.* (a) The loss of [[prop:ii-g1-3-3]] (2) printed in [[rem:ec-other-losses]] is
⌈(½ − min(β_K, β_ι + 1 − β^f_I))_+⌉ for a forcing of weights (β^f_I + 1, β_ι + 2, β_K). Here β_ι + 1 − β^f_I ≥
½ + 1 − 3.5 = −2 and β_K > 0, so it is at most ⌈5/2⌉ = 3.

(b) is the loss printed in [[rem:ec-other-losses]] and [[lem:ec-closed-forms]] (g); under the two conditions its
argument is at most 5 + ε − ½ < 5.

(c) In [[lem:iii-i2-4-1]], (1 − χ′)w has every σ-weight, so δ may be taken 3/2, and β′ = max(N, N − (3/2 − 2ε)) = 5;
the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ is 0 + 5. In [[cor:ii-g1-4-5]], δ = 1 and the output weights are
(β′_I, N, N), so ℓ_3 = 1 + ⌈(5 − ½)_+⌉ = 6.

(d) By [[lem:ec-closed-forms]] (b), (c) with ϑ_in = 0 and s_c = 3, the losses are max(⌈(3 − β_scf)_+⌉, 2) and
max(⌈(5/2 + ε/2 − β_scf)_+⌉, 2). At the stated β_scf the first ceilings are ⌈3/2 + ε⌉ = 2 and at most
⌈1 + 7ε/2⌉ = 2.

(e) By the proof of [[cor:ii-g1-4-5]] its loss is ℓ + 1 with ℓ = 2ℓ_3 + ℓ_4 + ℓ_5 (⌈kδ⌉ ≤ 1 by
[[lem:iii-j2-2-1]] (f)). ℓ_3 = 6 by (c). ℓ_5 is the loss of [[prop:ii-g1-3-3]] (2) at the weights of the forcing,
at most 3 by (a): [[lem:iii-i2-4-1]] states β_ι > ½ at its applications, and β^f_I = ℓ_I there. ℓ_4 is the loss
ℓ_1 + ℓ_2 + 2ν + ⌈(δ_2 − δ_1)_+⌉ of [[prop:ii-g1-4-4]] with δ_1 = δ_2 = 0. In [[lem:ii-g1-4-3]],
ℓ_1 = max(⌈(s_c − 1)_+⌉, ⌈sup 𝗋 − 𝗋_out⌉) with sup 𝗋 − 𝗋_out = 𝗋_in − 𝗋_out = −¼ − (β_scf − 2 − ε/2) =
¼ + 3ε/2 at β_scf = β′_I + ε = 3/2 − ε, so ℓ_1 = 2; ℓ_2 = max(⌈(−s_c)_+⌉, ⌈𝗋_out − inf 𝗋⌉) = 0; and with 𝖻 ≡ 0 the
numbers ν_0 = ⌈(−min(𝖻_out, inf 𝖻))_+ + 1⌉, ν_1 = ⌈(−inf 𝖻)_+⌉ and their counterparts ⌈(max(𝖻_out, sup 𝖻))_+ + 1⌉,
⌈(sup 𝖻)_+⌉ for [[eq:ii-g1-4-3a]] are 1, 0, 1, 0, so ν = 1. Hence ℓ_4 = 4, ℓ ≤ 12 + 4 + 3 = 19 and the loss is at
most 20. In [[lem:iii-i2-4-1]] the rest w is obtained by [[prop:ii-g1-3-3]] (1) and (2) (charges 1 and 3), then
[[cor:ii-g1-4-2]] (2) (charge 2 by (d)), then [[prop:ii-g1-3-5]] (1) at the weights (3/2 − 2ε, N, N) (charge
⌈N − ½ + ε⌉ = 5) or (2) (charge 5 by (c)); so at most 3 + 2 + 5 = 10, and 20 + 10 = 30.

(f) By [[eq:ec-moment-loss]] the loss is max(⌈(β_K + ½ + ε)_+⌉, ⌈γ + ½⌉) with γ ≤ β_ι − β_I. The three applications
have (β_I, β_ι, β_K) = (3/2, γ_+ + 1, α̃_K − 1) with γ_+ < 3/2 and α̃_K < 1; (3/2, α^♯_+ + 1, α_K − 1) with
α^♯_+ < 7/4 and α_K < 3/2; and (3/2, α^♯_+ + 1, α̃_K − 1) with α^♯_+ < 2 and α̃_K < 2. In each, β_K + ½ + ε < 2 and
γ + ½ ≤ β_ι − β_I + ½ < 2, so the loss is at most 2. ∎
