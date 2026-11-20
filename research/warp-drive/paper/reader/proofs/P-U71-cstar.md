### The single-step losses at the computational point {#sec:cs}

[[thm:uc-integer]] bounds d_acc and d_R by D_e + M_c c_*, where c_* is the largest of the numbers c(β_k), c_b, c′_b and
c_0 defined before [[prop:ec-upper]] and of their counterparts c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]. Each
of these numbers is assigned by [[def:ec-accounted-loss]] to a finite composition of elementary families. This section
lists, step by step, the families that each of them composes, bounds the charge of every one of them at the choice of
[[def:uc-choice]], and adds the charges. Two counts of index sets dominate the result: the count n_ι of the Fourier
transform in Step 0 of the proof of [[prop:iii-i11-3-1]], at most N_ι by [[lem:uc-n-iota]], and the count n_K of the
K⁺-exponents of the inverse transform in its Step 7, at most N_ι + N_Λ ([[lem:cs-fourier]]). A level step below 3 is
charged at most 497, a round and a step of the base at most 469 and 466, a level step above 3 at most
C_lev = 2N_ι + N̄_Λ + 529, with the bound N̄_Λ ≥ N_Λ below ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound
counts three runs of the top level, less than 6N_ι + 1.74·10²⁸ ([[lem:cs-rest]]). So c_* < 6.4368·10³⁵
([[prop:cs-cstar]]).

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
sources s^i whose families are charged at most 11. Then e ↦ M(e) + Σ_i ℓ_i(e)v^i is assigned at most
max(A_ℓ, A_M + 11), where A_M and A_ℓ are the sums of the charges of the applications in M and in the maps that give
the ℓ_i; in particular at most A_M + 11 when each ℓ_i is a coefficient functional (charge 0) of the output of maps
whose applications are among those of M.

*Proof.* (a) By induction over the expression: a composition is assigned the sum of the numbers of its factors, and a
sum or an assembly the largest of the numbers of its parts, which is at most their sum, all numbers being non-negative.
(b) The map is a sum of M and of a finite-rank assembly; [[def:ec-accounted-loss]] assigns the assembly the largest of
the numbers of its parts, the functionals (at most A_ℓ by (a)) and the families v^i (at most A_M + 11 by (a)). So the
sum is assigned at most max(A_M, A_ℓ, A_M + 11) = max(A_ℓ, A_M + 11). In the particular case the maps that give the ℓ_i
are among those of M, so A_ℓ ≤ A_M. ∎

Every elimination of finitely many parameters in [[ch:s20]]–[[ch:s23]] has the form of (b): by linearity and the
uniqueness of forward solutions, the forward solution for the forcing F − D_(p⃗)P(p⃗′) is the solution for F plus
Σ_i p′_i times the solutions for the fixed directions −D_(p⃗)P(e_i), which are background sources
([[lem:iii-j2-2-1]] (b)), and p⃗′ is a finite-dimensional linear function of coefficients read from the expansion of
the solution, that is, of coefficient functionals of outputs of the maps that compose M. This is the way in which the
finite-dimensional data enter in the proof of [[prop:ec-upper]]. So, by the particular case of (b), each statement
whose proof eliminates parameters is charged at most the sum of the charges of the statements it applies, each counted
once, plus 11.

**Definition {#def:cs-choices}** (The free orders and inner products.) At the choice of [[def:uc-choice]] we take,
besides:

(a) at the incoming radial sets of (2L_b)^(σ) and of N_tf((2L_b)^(·), ±1), the fibre inner product of
[[lem:ec-theta-in-zero]], in which ϑ_in = 0; at the horizon the fixed fibre inner product of [[lem:iii-f2-1-1]] with
δ = ¼, the neighbourhood ℬ_* being taken inside the neighbourhood of b₀ that this lemma gives, so that
ϑ_ℋ < ϑ_L + ¼ < 9/4 on ℬ̄_*; and the regularity order s_c := 3 > ½ + 9/4;

(b) in [[prop:ii-g1-4-4]], as [[cor:ii-g1-4-5]] applies it, the incoming order 𝗋_in := −¼ and the semiclassical order
𝖻 ≡ 0, and in [[cor:ii-g1-4-5]] the weight β′_I := 3/2 − 2ε where it is applied with an ℐ⁺-weight below 3/2;

(c) in [[lem:iii-i2-4-1]] the weights N := 21/4 of u_hi at ι⁺ and K⁺;

(d) in the proofs of [[lem:iii-i1-2-2]] and [[prop:iii-i1-2-1]], at each step other than Step 2 of the proof of
[[lem:iii-i1-2-2]], an increment η ∈ [2/5, ½) off the finitely many excluded values, or the remaining distance to the
target weight when that is smaller;

(e) in every application of [[cor:iii-f1-3-4]], the choices of [[prop:uc-ltf]];

(f) in the proof of [[thm:iii-i11-4-1]], an admissible level α′ ∈ (2, 2 + ε_g − 2ε), and in the proof of
[[prop:iii-i8-4-1]] at α′ the levels α_0 < α′, with α_0 ∈ (2, α′) admissible;

(g) in each application of [[lem:iii-a-1-4]] in [[lem:iii-i11-2-1]], at each step of its proof, the decrease of γ and the
number δ′ with sum at most ¼.

These choices are allowed. (a): [[lem:ec-theta-in-zero]] gives the inner product at the incoming radial sets,
which (O3) of [[def:i-a-admissible]] chooses separately for each radial set; [[lem:iii-f2-1-1]] gives ϑ_ℋ < ϑ_L + δ on a
neighbourhood of b₀ with ϑ_L = max(0, 2 − 2x) < 2; and the proofs of [[cor:ii-g1-4-2]], [[prop:ii-g1-4-7]],
[[lem:iii-i2-4-2]] and [[cor:ii-g1-4-5]] ask only s_c > ½ + ϑ_ℋ ([[lem:ec-closed-forms]] (b)). (b): the admissible orders
before [[lem:ii-g1-4-3]] ask 𝗋_out < −½ + S̄ = −½ and 𝗋_in ≥ 𝗋_out with 𝗋_in > ½(−1 + ϑ_in) = −½, and 𝗋_out =
β_scf − 2 − ε/2 < −½ for β_scf < 3/2; [[cor:ii-g1-4-5]] allows every β′_I below min(β_I, 3/2). (c): [[lem:iii-i2-4-1]]
holds for every N; its proof reaches the weights (·, N, N) through [[prop:ii-g1-3-5]] (1) and (2) at the K⁺-weight N,
which asks N ∉ ℕ, as 21/4 is; and every use of u_hi below needs at ι⁺ and at K⁺ weights below 21/4 (the targets are at
most 3 + η_2 at ι⁺ and α − ε < 5 at K⁺). (d): each step there asks only η < ½, α_I + η below the target, and finitely
many exclusions. (e) is [[prop:uc-ltf]]. (f): that proof takes any admissible α′ ∈ (2, 3), and the admissible levels
are the points of (2, 3) off finitely many ([[sec:iii-i8-1]]), so they are dense; α_0 lies in
(2, min(a_K, 2 + ε_g, 5/2)), and α′ − α_0 < 1 < a_K − 2 for the background of [[thm:iii-i11-4-1]], whose K⁺-order
a_K is at least 4 + ε_K, so α_0 < α′ are levels as the proof of [[prop:iii-i8-4-1]] asks, with one level step. The
statements built on [[thm:iii-i11-4-1]] use α′ only as an admissible level in (2, 3), through
w_(α′) = min(α′ − 2, λ_♯ − 1) > 0 (Step 6 of the proof of [[thm:iii-i12-3-1]]); at a rotating b the elimination of
[[thm:iii-i11-4-1]] is [[prop:iii-i15-2-5]] with q = 0, whose base is at the level α_1 of [[def:uc-choice]]. (g): in
the proof of [[lem:iii-a-1-4]] the decrease of γ need only make γ avoid the real parts of spec_b(A) ∪ π₁F, which has
finitely many points in every strip, and δ′ > 0 is any small number; so both may be taken with sum at most ¼.

#### The elementary charges {#sec:cs-elem}

**Lemma {#lem:cs-elem}** (The charges of the elementary families.) At the choices of [[def:uc-choice]] and
[[def:cs-choices]], every application of the following families in the constructions of [[thm:iii-i14-3-1]],
[[thm:iii-j1-2-1]] and [[lem:iii-k-2-3]] is charged at most:

(a) 0: finite-dimensional maps, coefficient functionals and finite-rank maps with fixed sections, among them the
inverses and functionals of [[lem:iii-j2-2-1]] (c), the assigned rotation coordinates A_b and the states, rows and
towers; the integrations of [[lem:iii-a-1-2]], [[lem:iii-a-3-2]] and [[lem:iii-i2-2-1]];
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
the integrations of its (d), [[cor:iii-h-4-2]] of its (e) and [[lem:iii-i2-4-3]] of its (g)). Multiplications by
smooth functions with bounded b-derivatives, and by |σ|^z, σ^j, sgn σ (which shift weights only), keep the order k.
The Mellin inversion of
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
fixed section, and the proof of [[prop:uc-dbg]] applies to it. The errors
E^ν(W) = L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W) of [[lem:s25-p6]] are differential
operators of order at most two with coefficients polynomial in the background, applied to fixed sections and linear
in the finite-dimensional W; the proof of [[prop:uc-dbg]] applies to them, and they are charged at most 11.

(e) By [[thm:fwd-loss]], [[eq:iii-i-5-2]] holds with d = 20,180 for g = g_0 + h, g_0 = g_(b₀,b₀,−S). At a base point
with parameter b ∈ ℬ̄_* these operators are those of [[cor:iii-h2-5-1]] ([[lem:iii-j2-2-1]] (a)), for which
[[eq:iii-i-5-2]] holds with the same d = 20,180 by [[cor:fwd-near-b0]]. By [[lem:iii-j2-2-1]] (a), for the
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
is obtained by the iteration of the proof of [[lem:iii-a-1-4]] with A = ρ⁻²L̂_b(0) near ∂X. A step from a weight w
reaches the weight γ = min(q′ − 2, w + 1), decreased slightly unless it is the target q′ − 2, and the next step starts
at γ − δ′; so each step that does not reach the target raises the weight by at least ¾ when its two small numbers, the
decrease of γ and δ′, are taken with sum at most ¼ ([[def:cs-choices]] (g)). As the first weight is above 0 and the
target at most 3, a fourth step starts above 9/4 and reaches the target; so at most 4 steps occur, and each applies
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

(c) In [[lem:iii-i2-4-1]], (1 − χ′)w has every σ-weight, so δ may be taken 3/2, and
β′ = max(N, N − (3/2 − 2ε)) = 21/4; the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ is 0 + ⌈19/4⌉ = 5. In [[cor:ii-g1-4-5]],
δ = 1 and the output weights are (β′_I, N, N), so ℓ_3 = 1 + ⌈19/4⌉ = 6.

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
most 20. In [[lem:iii-i2-4-1]] the rest w is obtained by [[prop:ii-g1-3-3]] (1) and (2) (charges 1 and 3, on the two
frequency ranges of one sum, so at most 3), then [[cor:ii-g1-4-2]] (2) (charge 2 by (d)), then [[prop:ii-g1-3-5]] (1)
at the weights (3/2 − 2ε, N, N) (charge ⌈19/4 + ε⌉ = 5) or (2) (charge 5 by (c)); so at most 3 + 2 + 5 = 10, and
20 + 10 = 30.

(f) By [[eq:ec-moment-loss]] the loss is max(⌈(β_K + ½ + ε)_+⌉, ⌈γ + ½⌉) with γ ≤ β_ι − β_I. The three applications
have (β_I, β_ι, β_K) = (3/2, γ_+ + 1, α̃_K − 1) with γ_+ < 3/2 and α̃_K < 1; (3/2, α^♯_+ + 1, α_K − 1) with
α^♯_+ < 7/4 and α_K < 3/2; and (3/2, α^♯_+ + 1, α̃_K − 1) with α^♯_+ < 2 and α̃_K < 2. In each, β_K + ½ + ε < 2 and
γ + ½ ≤ β_ι − β_I + ½ < 2, so the loss is at most 2. ∎

#### Null infinity and the Fourier steps {#sec:cs-null}

**Lemma {#lem:cs-null}** (The constructions at null infinity.) (a) Every application of [[prop:iii-i1-3-1]] in the
constructions is charged at most 6. (b) An application of [[prop:iii-i1-2-1]] with ℓ_+ < 3/2 whose a priori
ℐ⁺-weight α_I is at least −3/2 is charged at most 37 · 11 = 407. Every application below has α_I > ½.

*Proof.* (a) The operator of [[prop:iii-i1-3-1]] is L_b, with ρ_I⁻¹ρ_+⁻²L_b = L_0 + L̃ fixed ([[lem:iii-i1-1-1]]).
Step 1 of its proof solves for u^♭ by [[lem:iii-a-1-2]] and a fixed scalar (charge 0) and subtracts L_b v (charge 2).
Step 2 treats the windows [m_j, m_j + 1), m_j = min Re ℰ^C_I + j − 1 = 1 + j ([[prop:is-ci-pp]] (a): the least
exponent of ℰ^C_I is 2), with Re z ≤ ℓ_I < 3.5; so j ∈ {1, 2}. ℰ^C_I has logarithmic order 0 ([[prop:is-ci-pp]] (a)),
so k(F_I, z) = 0 at every z, and each term is solved once, by (z − 3/2 − Ā)⁻¹ and [[lem:iii-a-1-2]] (charge 0); the
terms of one window are independent, as L̃ moves the exponents by positive integers, out of the window. Each window
passes f − L_b(Σ_z χρ_I^z u^((z,0))) to the next (charge 2). So a chain is charged at most 2 + 2 · 2 = 6.

(b) Each step of the proofs of [[lem:iii-i1-2-2]] and [[prop:iii-i1-2-1]] applies L̃ of L = L^(g,g_0) once (charge 11,
[[lem:cs-elem]] (d)), the products ρ_I⁻¹ρ_+⁻²f and the integrations of [[lem:iii-a-1-2]] and [[lem:iii-a-3-2]]
costing nothing; so it suffices to count the steps, with the increments of [[def:cs-choices]] (d). Step 1 of the proof
of [[lem:iii-i1-2-2]] is run until the weight exceeds 1 + η₂, η₂ < (1 − e_Υ)γ_Υ < 0.01 being the number of its Step 2
(Step 2 needs L̃u at the weight 3/2 + η₂, and L̃ gains any η′ < ½); from α_I ≥ −3/2 this takes at most
⌈2.51/0.4⌉ = 7 steps. Step 2 is one step. Step 3 goes from 3/2 + η₂ to ℓ_I < 3.5 in at most ⌈2/0.4⌉ = 5 steps.
Step 1 of the proof of [[prop:iii-i1-2-1]] goes from α_I to below ℓ_+ < 3/2 in at most ⌈3/0.4⌉ = 8 steps, and its
Step 2 from there to ℓ_I in at most ⌈5/0.4⌉ = 13 steps. In all 7 + 1 + 5 + 8 + 13 = 34 ≤ 37 steps. At the
applications below the a priori ℐ⁺-weights are: β^(0)_I > ½ at the start of [[prop:iii-i2-5-1]] (the weight of
[[thm:iii-i-5-3]]), γ_+ − ε > ½ in its Step 3, and at least 1 − 5ε in [[prop:iii-i3-2-1]], [[prop:iii-i6-2-1]],
[[lem:iii-i8-3-2]] and [[prop:iii-i11-3-1]], whose remainders are sums of pieces of ℐ⁺-weight at least
min(3/2, α^♯_+) − 5ε > 1 − 5ε and of u_I, which has the ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I). ∎

**Lemma {#lem:cs-fourier}** (The Fourier steps of a level above 3.) Let β ∈ (3, α] be a level of Step 2 of the proof of
[[thm:iii-i14-3-1]], and consider the proof of [[prop:iii-i11-3-1]] at β (through [[prop:iii-i13-2-1]] when β < 4).

(a) The application of [[prop:iii-a-4-2]] (1) in its Step 0 is charged at most 9 + N_ι.

(b) In the application of [[prop:iii-a-4-2]] (2) in its Step 7, n_ι = 0 and n_K ≤ N_ι + N_Λ, and it is charged at most
N_ι + N̄_Λ + 2.

(c) The inverse transforms of the column pieces in its Step 5 ([[lem:iii-i11-2-4]]) are charged at most 5 each.

*Proof.* (a) is [[lem:uc-n-iota]] with [[lem:uc-fourier-count]] (with β_K = β − ε when β < 4): the charge is
1 + n_ι + 2⌊β − ε⌋ ≤ 1 + N_ι + 8. For a forcing in 𝒴^♮(β), [[prop:iii-i10-3-1]] (c) and [[lem:iii-i13-1-3]] (b) give
ℰ^♭ the hypothesis of [[lem:uc-n-iota]].

(b) Step 7 applies [[prop:iii-a-4-2]] (2) on each half with β_scf = 3/2 − 3ε, the tf-data (E_tf, β′_+ − 1), so
E_ι = E_tf + 1 and β_ι = β′_+ < 3/2, and the zf-data ((0, 0) ∪̄ (E_K − 1), β − 3 − ε), so β_K = β − 2 − ε. By
[[eq:ec-fourier-loss]] (2) its charge is n_ι + n_K + ℓ_F, where n_ι counts the pairs of E_tf of real part at most
β′_+ − 1 < ½, and n_K the pairs (d, m) of E_K − 1 with Re d ≤ β − 3 − ε < 1 + ε_K; E_tf and E_K − 1 are the smallest
index sets containing the tf-terms, resp. the zf-terms below these weights, of the pieces other than the columns with
constant coefficients.

*tf.* The pieces at zero energy are σ^jχ_zf û_j. By [[lem:iii-i11-2-1]], û_0 has at ∂X the exponents of
(ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·) and their ℕ₀-shifts, of real part at least 1, as ℰ^♭ ⊂ {Re ≥ 2} and
ℰ_col ⊂ {Re ≥ 0} ([[lem:iii-i11-1-1]]); for j ≥ 1, û_j has exponents of real part at least η_1 > 0 (Step 2), and the
factor σ^j adds j at tf. The pieces σ^ju_((α_0,k)) of [[prop:iii-g4-4-4]] have tf-exponents in
α_0 − 2 + j + ((0, 0) ∪ ℰ_ind) and, from the term with G^exc_(s1), in 2 + j and α_0 + j with ℰ_ind added (Step 1.1 of
the proof of [[prop:iii-g4-4-4]]), all of real part at least 1 (level 1: Re α_0 ≥ 2; level 2: Re α_0 ≥ 1 + η_1;
min Re ℰ_ind > 0). The pieces of level 3 and of the last level
are conormal at tf, of tf-weight above 2, and so are the column pieces with non-constant coefficients
([[lem:iii-i2-4-3]]: tf-weight at least ℓ_3 + 2 − ε plus the powers of σ they carry). So E_tf ⊂ {Re ≥ 1} and n_ι = 0.

*zf.* By Step 5 (i), (ii) and (iv) of the proof of [[prop:iii-i11-3-1]], and [[lem:iii-i11-2-3]], the zf-terms of the
pieces are: terms of integer degree without log|σ| (the zero energy pieces, the column pieces and σ^jP_int); and, for
an application of [[prop:iii-g4-4-4]] at a tf-exponent (α_0, k) at the level j ∈ {1, 2}, the terms
σ^jc_τ(σ)(−iσ)^ih̆^i_τ of degree α_0 − 3 + j + i (s1), α_0 − 2 + j + i (v1) and α_0 − 2 − μ + j + i (the other rows,
μ a root of the table of [[eq:iii-g4-3-5]], Re μ ≤ 0), i ≥ 0, with logarithmic order at most k + 1 (the derivatives in
α_0 give log|σ| up to the power k, and a critical α_0 or β_μ one power more). At level 1, Re α_0 ∈ [2, 2 + η_1) and
α_0 ∈ Λ is the u-exponent; at level 2, Re α_0 ∈ [1 + η_1, 2 + η_2) and α_0 + 1 ∈ Λ is the u-exponent; and the
logarithmic order k at the tf-exponent is at most k̄ of the u-exponent ([[lem:iii-i10-1-2]] (c),
[[lem:iii-i13-1-3]] (b)). As Λ ∩ {Re ≤ 3 + ε_+} is real ([[prop:is-lambda]]) and meets (2, 2 + ε_K] in no point ((G)),
and as the roots of the table are real, and those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K by [[eq:iii-f1-2-2]]
([[sec:iii-g4-1]], [[eq:iii-i9-1-1]]), a term of real part below
1 + ε_K is one of: at level 1, the s1 term with i = 0, of degree α_0 − 2; at level 1 with α_0 = 2, the s1 term with
i = 1, the v1 term with i = 0 and the terms of the rows with μ = 0 and i = 0, all of degree 1 = 3 − 2; at level 2, the
s1 term with i = 0, of degree α_0 − 1 = (α_0 + 1) − 2; and the integer degrees 0 = 2 − 2 and 1 = 3 − 2. So every pair
of E_K − 1 of real part below 1 + ε_K is (λ − 2, m) with λ ∈ Λ, 2 ≤ λ < 3 + ε_+, and m ≤ k̄(λ) + 1, where at degree 1
we use k̄(2) ≤ k̄(3) and 2, 3 ∈ Λ. The ℕ₀-shifts add nothing below 1 + ε_K except at the degree 0 + 1 = 1, as every other
degree has real part above ε_K. Hence, with λ_1 < ⋯ < λ_(N_Λ) as in [[lem:uc-lambda]] (c),

    n_K ≤ Σ_(i≤N_Λ) (k̄(λ_i) + 2) = N_Λ + 4N_Λ + 765,000,816 · N_Λ(N_Λ + 1)/2 ≤ N_Λ + N_ι

by the proof of [[lem:uc-n-iota]]. Finally ℓ_F = ⌈(max(β′_+ − 3/2 + 3ε, β − 2 − ε) + ε − ½)_+⌉ ≤ ⌈3/2 + ε_K⌉ = 2.

(c) By [[lem:iii-i11-2-4]], these are [[prop:iii-a-4-2]] (2) with E_ι = E_K = ∅ and the weights 3/2 − ε at ι⁺ and at
most α at K⁺, so their charge is ℓ_F ≤ ⌈α + ε − ½⌉ = 4 ([[lem:cs-transforms]] (b)). ∎

#### The level steps and the base {#sec:cs-steps}

**Lemma {#lem:cs-levels}** (The level steps.) Let 1 ≤ k ≤ K. (a) If β_k < 3, then c(β_k) ≤ 497. (b) If β_k > 3, then

    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 214,558,790,360,052,785,818,485,009,600,000,520.            {#eq:cs-clev}

The same bounds hold at a rotating black hole parameter and for c^Ψ(β_k).

*Proof.* By [[lem:cs-sum]] we add the charges of the applications of each step, the windows, the transition face
rounds, the applications of [[prop:iii-g4-4-4]] at the levels 1 and 2 and the level-3 rounds being charged 0.

*The background terms of Step 2 of the proof of [[thm:iii-i14-3-1]].* The forcing G′ of [[eq:iii-i14-3-4]] is F minus
Δ_q(p⃗′), R_q u and the defects f^S(S′), f^b(b′), f^s1(S^(0)′_1) and r^ν(W′_ν); u_0 adds the rows m_ν(W′_ν). These are
summands, each a family of [[lem:cs-elem]] (d) or a finite-rank map with such sections; so they are charged at most 11
beyond the steps that compute u and p⃗′, which are other steps of the chain. At a rotating b, [[prop:iii-i15-2-5]] adds
the errors E^ν (charge 11) to the same sum and the coordinates A_b (charge 0); for ℛ(U), [[lem:iii-k-2-3]] adds the
sources e_S(S′) + e_(S⁰)(S⁰′) (charge 11) to it. In every case this sum is charged at most 11.

(a) The step is [[lem:iii-i8-3-2]] at β_k. Its Step 0 applies (L − L_b)u (11). Steps 1–2 apply [[prop:iii-i1-3-1]] (6,
[[lem:cs-null]] (a)) and L_b u_I (2), the windows being charged 0. Step 3 runs Steps 3–3.3 of the proof of
[[prop:iii-i6-2-1]] with α − ε′ for α_K: [[lem:iii-i2-4-1]] at β_ι = 2 − ε (30, [[lem:cs-transforms]] (e)),
[[prop:ii-g1-3-3]] (1) (1), L̃_b(0)⁻¹ (1), the terms of f̂_2, which apply [L̂_b(0), χ_zf], L̂_b(σ) − L̂_b(0) and the
columns (2), the division by σ (0), [[prop:iii-g4-5-1]] (9, [[lem:cs-elem]] (f)), [[lem:iii-i6-1-4]] (0), f̂_4 (2),
L̃_b(0)⁻¹ (1) and f̂_5 (2). Step 3.4′ runs its rounds (charged 0) and applies [[lem:iii-i2-4-2]] at β_scf = 3/2 − 2ε (2,
[[lem:cs-transforms]] (d)); the row terms U^((i)), B^((i)), Σ^((i))_r of [[lem:iii-i6-1-3]] are fixed sections
L̃_b(σ)⁻¹(0, E_k) times the coefficients of the row functional (0), and [[eq:iii-i8-3-3]] is a sum; so is
[[eq:iii-i6-2-8]] of Step 3.5′, whose row term (U_r, B_r, Σ_r) of Step 3.5 is of the same kind (0). Steps 4–5 of the
proof of [[prop:iii-i6-2-1]] apply [[prop:ii-g1-3-5]] (1) twice, at the output weights (3/2 − 4ε, 2 − 2ε, α_K − 1) and
(3 − 2ε, 3 − ε, α_K − 1) (5 each, [[lem:cs-transforms]] (b)), [[lem:iii-i3-1-3]], [[lem:iii-i2-4-3]] and
[[lem:iii-i2-2-1]] (0). Steps 6–7 read coefficients (0). Step 8 applies [[prop:iii-i1-2-1]] (407, [[lem:cs-null]]
(b)). With the background terms,

    11 + 11 + 6 + 2 + (30 + 1 + 1 + 2 + 9 + 2 + 1 + 2) + 2 + (5 + 5) + 407 = 497.

(b) The step is [[lem:iii-i13-2-2]] (at a rotating b [[lem:iii-i15-2-4]], which adds the coordinates A_b, charge 0),
whose proof is that of [[lem:iii-i11-3-2]]. Its Step 0 applies (L − L_b)u (11). Steps 1–2 are [[prop:iii-i10-3-1]] at
β_k: its Step 1 applies [[prop:iii-i1-3-1]] (6) and L_b u⁽⁰⁾_I (2); its Step 2 is a window loop (0); the rows are read
by [[lem:iii-i10-2-1]] (c) (0). Step 3 is [[prop:iii-i11-3-1]] at β_k (through [[prop:iii-i13-2-1]] when β_k < 4). Its
Step 0 applies [[lem:iii-i2-4-1]] at β_ι = 3 + ε_+ − ε (30) and [[prop:iii-a-4-2]] (1) (9 + N_ι,
[[lem:cs-fourier]] (a)). Steps 1, 2 and 3 each apply [[lem:iii-i11-2-1]] (9) and [[lem:iii-i11-2-2]] (2), the
applications of [[prop:iii-g4-4-4]] being charged 0. Step 4 applies, besides its rounds, [[lem:iii-i11-2-1]] (9; only
when β_k > 4), the subtraction that forms g_J (2) and [[lem:iii-i2-4-2]] at β_scf = 3/2 − 2ε (2). Step 5 reads the
tails by [[lem:iii-i10-2-4]] (0) and transforms the column pieces back (5, in parallel, [[lem:cs-fourier]] (c)). Step 6
reads coefficients (0). Step 7 applies [[prop:iii-a-4-2]] (2) (N_ι + N̄_Λ + 2, [[lem:cs-fourier]] (b)) and, near ℐ⁺,
[[prop:iii-i1-2-1]] (407). With the background terms,

    11 + 11 + 6 + 2 + 30 + (9 + N_ι) + 3 · (9 + 2) + (9 + 2 + 2) + 5 + (N_ι + N̄_Λ + 2) + 407
        = 2N_ι + N̄_Λ + 529,

and 2N_ι + N̄_Λ + 529 is the integer of [[eq:cs-clev]]. ∎

**Lemma {#lem:cs-base}** (The base.) c′_b ≤ 466 and c_b ≤ 469, also at a rotating black hole parameter and for ℛ(U).

*Proof.* *One step of [[prop:iii-i2-5-1]].* Step 1 applies (L − L_b)u (11). Step 2a applies [[prop:iii-i1-3-1]] (6) and
L_b u_I (2). Step 2b applies [[prop:ii-g1-3-3]] (1) (1), [[lem:iii-i2-4-1]] at β_ι = γ_+ > ½ (30), [[lem:iii-i2-4-2]]
at β_scf = 3/2 − ε (2), [[prop:ii-g1-3-5]] (1) at the output weights (γ_+ − ε, γ_+, α̃_K) (at most 5),
[[lem:iii-i2-4-3]] (0), [[lem:iii-i2-3-1]] (2, [[lem:cs-transforms]] (f)) and [[lem:iii-i2-2-1]] (0). Step 3 applies
[[prop:iii-i1-2-1]] (407). So c′_b ≤ 11 + 6 + 2 + 1 + 30 + 2 + 5 + 2 + 407 = 466.

*One round of [[prop:iii-i5-2-1]].* Step 0 applies (L − L_b)u (11). Step 1 applies [[prop:iii-i1-3-1]] (6) and
L_b u_I (2). Step 2 is the window loop (0). Step 3 runs Steps 2–3 of the proof of [[prop:iii-i3-2-1]]:
[[lem:iii-i2-4-1]] at β_ι = α^♯_+ > 1 (30), [[prop:ii-g1-3-3]] (1) (1), L̃_b(0)⁻¹ (1), the terms of f̂_2 (2),
[[lem:iii-i2-4-2]] at β_scf = 3/2 − ε (2), [[prop:ii-g1-3-5]] (1) at the output weights
(min(3/2, α^♯_+) − 3ε, α^♯_+, α̃_K) (at most 5), [[lem:iii-i3-1-3]], [[lem:iii-i2-4-3]] and the multiplication by
−iσ (0), [[lem:iii-i2-3-1]] (2) and [[lem:iii-i2-2-1]] (0); the coefficient S_0 is read at no cost. Step 4 applies
[[prop:iii-i1-2-1]] (407). So c_b ≤ 11 + 6 + 2 + 30 + 1 + 1 + 2 + 2 + 5 + 2 + 407 = 469.

At a rotating b the statements are those at b ((BP1)–(BP5), [[prop:iii-i2-5-1-b]]), with the same families; for ℛ(U)
the base point is Ψ(U), which the base sees only through the class of its background ([[lem:iii-k-2-3]]). ∎

#### The remaining steps {#sec:cs-rest}

c_0 contains, besides finitely many steps of the kinds above, the iterations of the top level and of one further base,
which the definition before [[prop:ec-upper]] charges in full. We bound these first.

**Lemma {#lem:cs-iterations}** (Iterations charged in full.) Put R_b := 61,038,200,000,000 and

    I_lev := 16 · 1,470,302 + 3 + 3 · 3,000,004 + 5 · 6,847,261,001 = 34,268,829,852,
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 1,435,970,471,299,470,574,962.                                                          {#eq:cs-iterations}

(a) A level step at β ∈ (3, α] ([[lem:iii-i13-2-2]] or [[lem:iii-i11-3-2]] at β), with its window loop, its
applications of [[prop:iii-g4-4-4]] at the levels 1 and 2 and its level-3 rounds charged as well, is charged at most
C_lev − 11 + I_lev along every chain.

(b) A base, that is, [[prop:iii-i8-4-1]] at a level in (2, 3) for a background of K⁺-order above a♭_K, with all its
rounds of [[prop:iii-i5-2-1]], steps of [[prop:iii-i2-5-1]] and windows charged as well, is charged at most
B + I_base along every chain, where B is the sum of the charges of its other applications.

*Proof.* (a) [[lem:cs-levels]] (b), without the 11 of the background terms of [[thm:iii-i14-3-1]], bounds the other
applications. By [[lem:ec-counts]] (e), [[lem:uc-gaps]] and [[prop:uc-explicit]], the window loop has at most 1,470,302
windows, each charged at most r_ι ≤ 16 ([[lem:ec-round-charges]] (c), [[lem:uc-admissible]]). By [[lem:ec-counts]] (d)
and the paragraph on the levels 1 and 2 in the proof of [[prop:ec-upper]], a chain meets at most one application at
level 1 and at most (1 + η_2 − η_1)/𝔡₁ + 1 < 3,000,004 at level 2 ([[prop:uc-explicit]]: (1 + η_2 − η_1)/𝔡₁ + 2 <
3.000005·10⁶), each charged at most ℓ⁺_tf + 2 = 3 ([[lem:ec-round-charges]] (b)). By [[lem:ec-counts]] (c) there are
fewer than 1/Δτ + 2 level-3 rounds, and 1/Δτ ≤ 1/Δτ_0 < 6.847261·10⁹ ([[prop:uc-explicit]]), so at most
6,847,261,001; each is charged at most ℓ⁺_tf + 4 = 5 ([[lem:ec-round-charges]] (a)).

(b) By [[lem:ec-counts]] (f) and [[prop:uc-explicit]], the rounds number at most N_b < R_b and the steps at most
N_b + 1, charged at most 469 and 466 by [[lem:cs-base]]; the window loops of the base are one per round and three more
(the proof of [[prop:ec-upper]]), each of at most 1,470,302 windows charged at most 16. For a background of larger
K⁺-order the rounds are fewer. The values in [[eq:cs-iterations]] are the products and sums written out. ∎

**Lemma {#lem:cs-rest}** (The remaining steps.) Put X_12 := 4k̄_max + 24 and

    T_11 := 20,183 + 1,914 + I_base + 22 + C_lev + I_lev,     T_12 := C_lev + I_lev + X_12.

Then

    c_0 ≤ 20,183 + 1,914 + T_11 + 2T_12 + 11 + d_Φ + (N̄_Λ + 2)(d_Φ + 30)                              {#eq:cs-c0}

with d_Φ = 62N_Λ + 2 ≤ 1,038,326,399,999,940, and the same bound holds for c^Ψ_0 and at a rotating black hole parameter.

*Proof.* c_0 is the largest charge along a chain of the remaining steps of the larger construction, that of
[[thm:iii-j2-4-2]]; we add the charges of all their applications, each statement counted once ([[lem:cs-sum]] and the
paragraph after it).

*Step 0* is one forward solution operator (20,183, [[lem:cs-elem]] (e)).

*Step 1, the base, its iterations of [[lem:ec-counts]] (f) and windows charged 0.* (1) The start of the proof of
[[prop:iii-i2-5-1]] applies [[prop:iii-i1-2-1]] to the forward solution (407). (2) [[prop:iii-i3-2-1]], outside the
steps of [[prop:iii-i2-5-1]] in its Step 0: (L − L_b)u (11), [[prop:iii-i1-3-1]] and L_b u_I (6 + 2), Steps 2–3 (the
43 of the round in the proof of [[lem:cs-base]]) and Step 4 (407): 469. (3) [[prop:iii-i4-4-1]] (1) and
[[cor:iii-i4-4-3]]: the parameter S″ (0), the forcing term f_(h,S)(S″) (11) and the recentring of [[lem:iii-i4-1-2]] (0):
11. (4) [[lem:iii-i8-3-1]], that is [[prop:iii-i6-2-1]] with its Steps 0–2 changed: Step 0 applies (L − L_b)u_F and
(L − L_b)u (22), its windows and the rounds of [[prop:iii-i5-2-1]] being charged 0; Steps 1–2 apply
[[prop:iii-i1-3-1]] and L_b u_I (8); Step 3 applies the 48 of Step 3 in the proof of [[lem:cs-levels]] (a); Step 3.4
applies [[lem:iii-i2-4-2]] (2), the row term being of finite rank (0); Steps 4 and 5 apply [[prop:ii-g1-3-5]] (1)
(5 + 5); Step 6 applies [[prop:iii-i1-2-1]] (407): 497. (5) [[sec:iii-i7-4]]: the parameters (0) and the sources f^S,
f^b, f^s1 (11): 11. (6) [[prop:iii-i8-4-1]] at α_1, whose levels are α_0 < α_1 (α_1 − α_0 < a♭_K − 2): the sources
f^ν and D_(p⃗)P_3 (11), the inverse T⁻¹ (0), and [[lem:iii-i8-3-2]] from α_0 to α_1, at most 497 by the proof of
[[lem:cs-levels]] (a) (its windows charged 0; it has no transition face round, as τ_0 = 2 + ε_g − 2ε exceeds
α_1 − ε′, α_1 − 2 < ε_K < ε_g − 2ε): 508. (7) Step 1 of the proof of [[thm:iii-i14-3-1]]: the terms by which P_5
differs from P_3, D_(W⃗)P_5 and Δ_q (11). In all 407 + 469 + 11 + 497 + 11 + 508 + 11 = 1,914.

*Steps 3, 4′ and 4, every step charged.* Step 3 inverts finite-dimensional maps (0). Step 4′ forms
G̃_0 = F − Δ_q(p⃗′) − R_q u − Σ_(ν∈𝒩_rot) f^ν(W′_ν), a sum of background terms (11), identifies p⃗′_0 through
[[thm:iii-i11-4-1]] and expands u by [[thm:iii-i12-3-1]]; Step 4 applies [[thm:iii-i12-3-1]] again. We charge each in
full. G̃_0 is affine in the finite-dimensional W⃗′^rot, and [[thm:iii-i11-4-1]] and [[thm:iii-i12-3-1]] are linear in
F; so the applications in Step 4 are those of Step 4′, with W⃗′^rot entering by a finite-rank assembly, and no further
application of [[thm:iii-i11-4-1]] lies on a chain. [[thm:iii-i11-4-1]] applies [[prop:iii-i8-4-1]] at the level α′ of
[[def:cs-choices]] (f), a base whose level step α_0 → α′ has no transition face round (τ_0 = 2 + ε_g − 2ε exceeds
α′ − ε′, as in (6) of Step 1), at most 20,183 + 1,914 + I_base by [[lem:cs-iterations]] (b) (its forward solution,
and the 1,914 of the base with the forward solutions at (h, p⃗)), the sources of F(W⃗) and G(W⃗) (11 + 11), and
[[lem:iii-i11-3-2]] at α, at most C_lev − 11 + I_lev by [[lem:cs-iterations]] (a); this is at most T_11.
[[thm:iii-i12-3-1]] applies, in its Step 0, the decomposition of the proof of [[lem:iii-i11-3-2]] at α (at most
C_lev − 11 + I_lev), and beyond it at most X_12, as follows. In Step 1, the pieces (i)–(v) and (vii) are read by
[[lem:iii-i12-2-1]] (b) and Taylor's formula with fixed moments (0). In (vi) the zf-expansion of
σ^jχ_tfρ_tf^(α_0−2)u_tf costs nothing, and its zf-remainder is transformed back by [[prop:iii-a-4-2]] (2) with E_K = ∅
and with E_ι the tf-index set plus 1, counted up to the ι⁺-order 3 + η_2 − 2ε: these are the exponents α_0 − 1 + j + m,
m ∈ ℕ₀, with logarithmic order at most k ≤ k̄_max, and at most 4 of them lie below 3 + η_2 (Re α_0 ≥ 2 at level 1,
Re α_0 ≥ 1 + η_1 at level 2); so n_ι ≤ 4(k̄_max + 1) and the charge is at most 4k̄_max + 4 + 5 (ℓ_F ≤ 5 by
[[lem:cs-transforms]] (b), the output weights being at most 3 + η_2 at ι⁺ and α − ε at K⁺). In (viii) the conormal
coefficients are transformed by [[lem:iii-i12-2-1]] (a), that is [[prop:ii-g1-3-5]] (1) (5), and the zf-remainder by
[[prop:iii-a-4-2]] (2) with plain tf-weight (5). In (ix), σ³û_f is transformed back with plain weights (5), and the
columns by [[lem:iii-i12-2-2]], whose A and B are [[prop:ii-g1-3-5]] (1) (5) and whose convolutions cost nothing.
Steps 2–5 assemble, subtract by [[lem:iii-i12-2-4]] and read coefficients (0). The pieces (i)–(ix) are summands of u,
so by [[def:ec-accounted-loss]] they are charged the largest of these charges, 4k̄_max + 9 < X_12; so
[[thm:iii-i12-3-1]] is charged at most C_lev − 11 + I_lev + X_12 = T_12. In all, Steps 3, 4′ and 4 are charged at most
11 + T_11 + 2T_12.

*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most 1,038,326,399,999,940 ([[lem:uc-lambda]] (d)).

*Steps 1–3 of the proof of [[thm:iii-j1-2-1]].* Step 1 subtracts D_UΦ(U′_0 ⊕ 0), whose loss is at most d_Φ, Φ being
affine in U_1 with the loss d_Φ and smooth in U_0 ([[thm:iii-j-2-4]], [[rem:iii-j-2-5]]). Step 2 treats the exponents
of Λ_* in increasing real part, those of equal real part independently; at each it reads G′(λ₀) from the current
(h′, p⃗′, q′) (0), applies the right inverse of [[prop:iii-g3-3-7]] (30) in Case B, and subtracts D_UΦ(U′_(λ₀)) (at most
d_Φ), and the next exponent is read from the result. So a chain through Step 2 meets at most N_Λ exponents, each
charged at most d_Φ + 30. Step 3 subtracts D_UΦ(U′_c) (at most d_Φ). So Steps 1–3 are charged at most
(N_Λ + 2)(d_Φ + 30) ≤ (N̄_Λ + 2)(d_Φ + 30).

Adding gives [[eq:cs-c0]]. For ℛ(U) the base point is Ψ(U) and U ↦ Ψ(U) replaces U ↦ Φ(U); Ψ(U) − Φ(U) =
(χ_−h_(−S,−S⁰), 0, 0) is a smooth function of the finite-dimensional components (S, S⁰) of U ([[lem:iii-k-2-3]]), so
U ↦ Ψ(U) has the loss of U ↦ Φ(U), and D_UΨ(U′) − D_UΦ(U′) is a finite-rank map with fixed sections; the sources
e_S(S′) + e_(S⁰)(S⁰′) enter the forcings of Steps 1 and 2 as summands charged 11 ([[lem:cs-elem]] (d)), beside the
sources counted there. At a rotating b, [[prop:iii-i15-2-5]] adds the coordinates A_b (0) and the errors E^ν (11) as
summands of the same sums. So the bound holds for c^Ψ_0 and at every b ∈ ℬ̄_*. ∎

#### The bound {#sec:cs-bound}

**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the index sets as
constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ 6N_ι + 3N̄_Λ + 17,389,163,815,025,371,354,557,103,786
        = 643,676,388,469,322,172,480,826,383,357,103,759
        < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵.                        {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469,
c′_b, c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With
C_lev = 2N_ι + N̄_Λ + 529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        = 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 102,492,973,325,715,479,993,544
          + 1,435,970,471,299,470,574,962 + 1,038,326,399,999,940 + 17,389,059,886,080,535,910,399,999,970,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 102,492,973,325,715,479,993,544 and
(N̄_Λ + 2)(d_Φ + 30) ≤ 16,747,200,000,001 · 1,038,326,399,999,970 = 17,389,059,886,080,535,910,399,999,970. The seven
numbers after 6N_ι + 3N̄_Λ add up to 17,389,163,815,025,371,354,557,103,786, and with
6N_ι = 643,676,371,080,158,357,455,404,787,199,999,976 and 3N̄_Λ = 50,241,599,999,997 the sum is the integer of
[[eq:cs-cstar]], which is less than C_*. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of C_*, all but less than 1.74·10²⁸ is 6N_ι: two counts of
the logarithmic terms of Λ below 3 + ε_+ in each of the three runs of the top level that c_0 contains, each count
being taken at the bound k̄(λ) of [[def:iii-i10-1-1]] for the logarithmic orders. The next term,
(N̄_Λ + 2)(d_Φ + 30) < 1.739·10²⁸, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes through
every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev ≈ C_*/3, and c_0
enters the second line of [[eq:ec-upper]] once; bounding that line by K·C_lev + 469N_b + 466(N_b + 1) + C_*, with
K < 1.22077·10¹⁴ ([[rem:ec-upper-point]]), instead of by M_c C_*, gives d_acc < 2.62·10⁴⁹. The bound is crude in
another way as well: n_ι and n_K count every pair (λ, k) with k ≤ k̄(λ), while the logarithmic orders that the
constructions produce are bounded in this paper only by k̄(λ).
