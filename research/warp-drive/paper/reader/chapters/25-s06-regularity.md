## Global microlocal regularity {#ch:s06}

This chapter proves the global regularity estimate for wave-type operators on the compactified spacetime: a
distribution supported to the future of an initial hypersurface is controlled in a weighted edge-3b Sobolev space by its
image under the operator, at the cost of one derivative, which the trapped set takes. It is [Hin26c, Section 7] in
dimension 4 + 1. The first half ([[sec:ii-d-1]]–[[sec:ii-d-5]]) proves the estimate without b-regularity: the radial
point estimates at the horizon, over ∂K⁺ and at ℐ⁺, the estimate at the trapped set with its loss, and their
combination along the null-bicharacteristic flow of [[ch:s05]]. The second half ([[sec:ii-d1-1]]–[[sec:ii-d1-7]]) adds k
degrees of b-regularity, by commuting b-vector fields through the operator, and proves the estimate also in a form tame
in k.

*Method.* Every estimate here is a positive commutator estimate. [[sec:ii-a1-4]] provides the machinery with coefficients
of finite regularity: one step with a regulariser ([[lem:ii-a1-4-1]]) and the iteration in the order
([[lem:ii-a1-4-2]]). Two additions are made in [[sec:ii-d-2]]: a term JL in the commutator inequality, which a cut-off
to the characteristic set produces ([[lem:ii-d-2-1]]), and bounds of microlocal norms through symbols
([[lem:ii-d-2-4]], [[lem:ii-d-2-5]]), with which the norms produced by different commutators are compared. With these,
each radial estimate is a calculation of symbols at a radial set of [[ch:s05]]. Weights and fibre inner products enter
through the subprincipal symbol of a conjugated operator ([[lem:ii-d-1-1]]), and the thresholds are those of
[[sec:ii-c-2-3]] and [[eq:i-a-1-5]]. At ℐ⁺ the subprincipal symbol is calculated in [[lem:ii-d-3-4]], which is [Hin26c,
(7.22)] in dimension 4 + 1: the constant 3 = n − 1 of [[lem:ii-c-3-4]] is exactly the one that makes the leading part of
the operator symmetric for |dt dx|. [Hin26c] quotes its estimate at the trapped set from [Hin21, Theorem 3.9], whose
proof writes out the regularisation of its first step and sketches that of the others. [[sec:ii-d-4]] proves that
estimate in full in the present calculus, from the hypersurfaces of [[prop:ii-c1-3-4]]: an equation with damping for
the unstable defining function, two quantitative propagation estimates, and their combination, all with one regulariser
and by induction on the order in half steps.

*Notation.* Orders that may vary on phase space are written in sans-serif (𝗌, 𝗍), constant orders in italic (s, t).
For a matrix 𝔞 that is self-adjoint for some fibre inner product, max spec 𝔞 is its largest eigenvalue. N′ is a fixed
large integer; every a priori term ‖χu‖_(−N′) below is with respect to it, and N_E is the rank of the bundle E = ℂ^(N_E)
of [[sec:ii-c-1-1]].

### The setting and the global estimate {#sec:ii-d-1}

#### The operators {#sec:ii-d-1-1}

g_0 is the stationary metric of [[sec:ii-b-1-1]], which satisfies (K1)–(K4) together with the hypotheses (H1)–(H8) of
[[sec:i-a-1-3]], [[sec:i-b-1-2]] and [[sec:i-b-1-5]], and P_0 is a stationary wave-type operator for g_0
([[def:ii-c-1-1]]). The radii r_0 − 2δ_0 < r_0 < r_2 < r_h that enter those hypotheses are arbitrary, subject to the
hypotheses: nothing below uses their values, and the radii chosen from them below (r_1, r_1⁺, r^♮) are chosen again
with them. Fix ℓ_I ∈ (0, ½], ℓ_+ ∈ (0, 1] and ℓ_K > 0. P is a weakly admissible wave-type operator relative to P_0 of
class ((d_0; 0), (2ℓ_I, ℓ_+, ℓ_K)) ([[def:ii-c-3-3]]), and ε_P := ‖P − P_0‖_((d_0;0),(2ℓ_I,ℓ_+,ℓ_K))
([[def:ii-c-3-6]]). Only ℓ_I ∈ (0, ½], ℓ_+ > 0, ℓ_K > 0 are used: the conditions [Hin26c, (5.23)] play no part in
microlocal regularity ([Hin26c, p. 115]). The metric g = g_0 + h of P has ‖h‖ ≤ Cε_P ([[lem:ii-c-3-7]]). So, for ε_P
small, the time function t_*^♭ of [[lem:ii-c-3-2]] and the domain Ω_* := cl_M{t_*^♭ ≥ 1} ([[sec:ii-c-3]]), the global
dynamics of [[sec:ii-c-4]] and the hypersurfaces of [[prop:ii-c1-3-4]] are available (the norm of h in
𝒢̃^(d_0,(0,0,ℓ_K))_e3b is at most a constant times ε_P). Over ℐ⁺, t_*^♭ = t_* ([[lem:ii-c-3-2]] (a)). d_0 is taken large
where needed, depending only on the orders.

Put W := x_I² ρ_+² and L := W⁻¹P. By [[lem:ii-c-1-4]] (b) and [[eq:ii-c-3-2]], L = L_0 + L_1 + L_2 is of the form of
[[sec:ii-a1-5-1]] with m = 2: L_0 is the scalar part of W⁻¹P_0, L_1 the second-order part of W⁻¹P̃, whose coefficients
lie in C^(d_0,(2ℓ_I,ℓ_+,ℓ_K))_e3b, and L_2 is of first order. L_2 contains the first-order part of W⁻¹P_0, the terms
χ_I (p̃_1 (x_I ∂_(x_I) − 2ρ_+ ∂_(ρ_+)) + ½ p_0) of [[eq:ii-c-3-2]], whose coefficients need not decay at ℐ⁺, and the
rest of W⁻¹P̃. The principal symbol of L is ℓ := W⁻¹G = G_e3b, real and scalar, and 𝖧 := ρ_∞ H_ℓ is the field 𝖧_G of
[[eq:ii-c-4-2]].

Near a set O where another positive weight W′ has W/W′ and W′/W smooth with bounded e3b-derivatives, we use L′ := W′⁻¹P
= (W/W′) L in place of L. For G microsupported over O, ‖G L′u‖_𝗍 and ‖G Lu‖_𝗍 then differ by lower-order terms only.
We take W′ = 1 near the horizon and the trapped set, over (K⁺)°, where W is smooth and positive; W′ = ρ_+² = r⁻² near
∂K⁺, where x_I is smooth and positive; and W′ = W near ℐ⁺. The rescaled fields ρ H_(W′⁻¹G) are then those of
[[ch:s05]]: ρ_∞ H_G with ρ_∞ of (H3) near the horizon ([[sec:ii-b-4]]), σ⁻¹ H_G near the trapped set
([[sec:ii-b-5]]), −σ_3b⁻¹ H_(G_3b) near ∂K⁺ ([[eq:ii-b-3-3]], [[eq:ii-b-3-4]]), and σ_eb⁻¹ H_(G_eb) near ℐ⁺
([[eq:ii-b-7-3]], [[eq:ii-b-7-4]]).

#### Weights, inner products and the conjugated operator {#sec:ii-d-1-2}

For weights (α_I, α_+, α_K) put w := x_I^(2α_I) ρ_+^(α_+) ρ_K^(α_K); then H^(𝗌,(2α_I,α_+,α_K))_e3b = w H^𝗌_e3b, with
H^𝗌_e3b based on L²(|dt dx|) ([[sec:ii-a-4-2]]). Near ∂K⁺ we use ρ_K = r/t_* and ρ_+ = r⁻¹, near (K⁺)° ρ_K = t_*⁻¹,
and near ℐ⁺ ρ_+ = t_*⁻¹ ([[sec:ii-b-3-1]]). A fibre inner product h on ℂ^(N_E) over a set O, smooth with bounded
e3b-derivatives, is written h(v, v′) = ⟨A⁻¹v, A⁻¹v′⟩ with A := 𝖦^(−1/2), 𝖦 the Gram matrix of h. Adjoints and Im_h are
taken for |dt dx| ([[sec:ii-c-1-1]]).

**Lemma {#lem:ii-d-1-1}** (The conjugated operator.) Let W′ be a weight as in [[sec:ii-d-1-1]] on O, L′ := W′⁻¹P,
ℓ′ := W′⁻¹G, and L″ := A⁻¹w⁻¹L′wA. (a) L″ is of the form of [[sec:ii-a1-5-1]] on O, with principal symbol ℓ′ and
coefficient norms bounded by those of L′ times constants depending only on w and A. (b) σ_1(Im L″) = A⁻¹(σ_1(Im_h L′)
− H_ℓ′ log w) A, where Im is taken for the standard inner product. (c) σ_1(Im_h L′) = W′⁻¹ σ_1(Im_h P) − ½ H_ℓ′ log W′.
Hence, for any positive ρ homogeneous of degree −1, with 𝖧′ := ρ H_ℓ′ and 𝔭′ := ρ W′⁻¹ σ_1(Im_h P),

    ρ σ_1(Im L″) = A⁻¹ (𝔭′ − ½ 𝖧′ log W′ − 𝖧′ log w) A.                                                 {#eq:ii-d-1-1}

*Proof.* (a) w⁻¹Vw = V + V(log w) for a vector field V, and for V ∈ 𝒱_e3b ⊂ 𝒱_b, V log w is smooth with bounded
e3b-derivatives, w being a product of powers of boundary defining functions; likewise for A. So the coefficients of L″
are those of L′ multiplied and differentiated as stated, and its second-order part is that of L′. (b) w⁻¹L′w = L′ +
w⁻¹[L′, w], and [L′, w] is of first order with principal symbol −i H_ℓ′ w; so w⁻¹L′w = L′ − iX modulo order 0, with X
of real principal symbol H_ℓ′ log w. As w is real and scalar, (w⁻¹L′w)^(*h) = w L′^(*h) w⁻¹ = L′^(*h) + iX′ modulo
order 0, with σ(X′) = H_ℓ′ log w, since σ([L′^(*h), w⁻¹]) = −i H_ℓ′ w⁻¹ = i w⁻² H_ℓ′ w. Hence σ_1(Im_h(w⁻¹L′w)) =
σ_1(Im_h L′) − H_ℓ′ log w. Next, for any operator M, M^(*h) = 𝖦⁻¹M*𝖦 with 𝖦 = A^(−*) A⁻¹, so A⁻¹ M^(*h) A = A* M*
A^(−*) = (A⁻¹MA)*, and Im(A⁻¹MA) = A⁻¹ (Im_h M) A exactly. (c) Im_h(fP) = f Im_h P − (1/(2i)) [P^(*h), f] for a real
function f, and σ([P^(*h), f]) = −i H_G f, so σ_1(Im_h(fP)) = f σ_1(Im_h P) + ½ H_G f. With f = W′⁻¹, ½ H_G W′⁻¹ =
−½ W′⁻¹ H_G log W′, and W′⁻¹ H_G log W′ = H_ℓ′ log W′ exactly, as H_ℓ′ = W′⁻¹ H_G + G H_(W′⁻¹) and the Hamilton field
of a function of the base annihilates functions of the base. [[eq:ii-d-1-1]] follows on multiplying by ρ. ∎

The estimates for L″ on ũ := A⁻¹w⁻¹u in unweighted spaces are estimates for u in the weighted spaces: for B ∈
C_b^∞Ψ^0_e3b, w⁻¹Bw and A⁻¹BA differ from B by operators of order −1 ((S11) of [[sec:ii-a-3]], and
[[prop:ii-a1-2-4]]), and A⁻¹w⁻¹W′⁻¹Pu = L″ũ.

#### The radial sets and the standing choices {#sec:ii-d-1-3}

On ∂Σ⁺ the future field is 𝖧, on ∂Σ⁻ it is −𝖧 ([[sec:ii-c-2-3]]). We use the sets of [[ch:s05]]: the horizon radial
set ∂R_(𝓗⁺) ([[def:ii-b-4-1]]), the radial sets ∂R_(∂K⁺,in/out) over ∂K⁺ ([[def:ii-b-3-1]]), ∂R_(ℐ⁺,in,+) and
∂R_(ℐ⁺,out) ([[def:ii-b-7-1]]), the trapped set ∂Γ_(K⁺) and the stable and unstable sets Γ^(u/s)_(K⁺), ∂Γ̄^(u/s)_(K⁺)
([[def:ii-b-5-1]]), and ∂W_(in/out) over ι⁺ ([[lem:ii-b-3-2]], [[lem:ii-b-3-3]]). By [[lem:ii-c-4-1]], the
characteristic set and 𝖧 of P agree with those of P_0 over ∂M, and near it 𝖧_G − 𝖧_(G_0) ∈ ε_P w C^(d_0−1) 𝒱_b with
w = x_I^(2ℓ_I) ρ_+^(ℓ_+) ρ_K^(ℓ_K).

Fix, as in [Hin26c, (7.1)–(7.2)], radii r_0 < r_1 < r_1⁺ < r^♮, with r^♮ = ½(r_0 + r_2) of [[lem:ii-c-3-2]], so that
dr is future timelike on {r_0 ≤ r ≤ r^♮}, and χ ∈ C^∞(Ω_*) with

    χ = 0 on (t_*^♭)⁻¹([1, 2]) ∪ r⁻¹([r_0, r_1]),       χ = 1 on {t_*^♭ ≥ 3} ∩ {r ≥ r_1⁺}.                 {#eq:ii-d-1-2}

Fix weights ([Hin26c, (7.3)])

    α_I < −½ + p̄_1,       α_+ < α_I − ½,       α_K ∈ ℝ,                                                  {#eq:ii-d-1-3}

with p̄_1 of [[def:ii-c-3-5]], and order functions 𝗌_0 < 𝗌, admissible for P_0 with weights α_+, α_K and margin 0
([[def:ii-c-5-2]], produced by [[prop:ii-c-5-1]]). In particular 𝗌 and 𝗌_0 are constant near each radial set and near
the trapped set ([[def:ii-c-2-4]] (3)–(6) and [[prop:ii-c-5-1]] (5)), and they satisfy there the thresholds of
[[def:ii-c-2-4]] with margin 0.

**Theorem {#thm:ii-d-1-2}** (The global regularity estimate.) There is C such that

    ‖χu‖_(H^(𝗌,(2α_I,α_+,α_K))_e3b)
        ≤ C (‖Pu‖_(H^(𝗌,(2α_I+2,α_++2,α_K))_e3b(Ω_*;E)^(•,−))
              + ‖u‖_(H^(𝗌_0,(2α_I,α_+,α_K))_e3b(Ω_*;E)^(•,−)))                                             {#eq:ii-d-1-4}

for P = P_0, in the strong sense: if the right side is finite, so is the left, and [[eq:ii-d-1-4]] holds. There is
d_0, depending only on 𝗌_0 and 𝗌, such that [[eq:ii-d-1-4]] holds also for every weakly admissible wave-type operator P
relative to P_0 with ε_P small, with C uniform.

This is [Hin26c, Proposition 7.1] in dimension 4 + 1. The estimate loses one derivative: Pu is measured in H^𝗌, where
real principal type propagation would need only H^(𝗌−1). The loss comes from the trapped set ([[prop:ii-d-4-2]]). The
spaces are those of [[sec:ii-a-7]]: u is supported at the initial hypersurface {t_*^♭ = 1} and extendible at the final
one in {r = r_0}. Extended by zero, u is a distribution on M supported in {t_*^♭ ≥ 1}, and so is Pu. The proof is in
[[sec:ii-d-5]].

**Remark {#rem:ii-d-1-3}** (Uniformity in the model.) The constants below depend on the stationary model only through
finitely many norms of its coefficients and through the dynamical constants of [[ch:s05]], which are uniform for the
stationary models of parameters b near b_0 ([[rem:ii-b-8-3]], [[prop:ii-c-5-1]] (4), [[prop:ii-c1-3-4]]). So
[[eq:ii-d-1-4]] holds uniformly also when P_0 is replaced by those models, or perturbed within the stationary wave-type
operators. This is [Hin26c, Remark 7.2]. The statement on large perturbations of P_0 in [Hin26c, Remark 7.3] is not
used and not proved here.

### Commutator lemmas {#sec:ii-d-2}

In this section L is any operator of the form of [[sec:ii-a1-5-1]], possibly on a vector bundle of another rank, with
real scalar principal symbol ℓ of order m. L_R, L_I and C_ǎ are those of [[eq:ii-a1-4-1]], ℓ_I is the principal symbol
of L_I (an Hermitian matrix of order m − 1), norms are those of H^𝗍_e3b, and B, E, G, J are carried by χ
([[sec:ii-a-8-3]]). For a positive symbol ρ, homogeneous of degree −1 near fibre infinity, and κ > 0, the regulariser is
φ_ε := (1 + ερ⁻¹)^(−κ), ε ∈ (0, 1], and θ_ε := ερ⁻¹(1 + ερ⁻¹)⁻¹; [[eq:ii-a1-2-1]] holds with ρ in place of ρ_∞, and
φ_ε has the properties stated after it. δ_c ∈ (0, ¼] is the constant of [[lem:ii-a1-4-1]] (the gain in its a priori
term), and ς ∈ {1, −1} the sign there.

**Lemma {#lem:ii-d-2-1}** (One step with a characteristic cut-off.) Let (i)–(ii) of [[lem:ii-a1-4-1]] hold, and in place
of its (iii) the following: there are real scalar symbols j_ε, bounded in C^(M)_ν S̃^(2𝗌−m) and, for each ε, in
C^(M)_ν S̃^(2𝗌−m−2κ), supported in K_1, such that for every w ∈ H^(K′)_e3b carried by χ, with J_ε := Op(j_ε),

    ς⟨C_(ǎ_ε) w, w⟩ ≤ −‖B_ε w‖² + ‖E_ε w‖² + 2 Re⟨J_ε L w, w⟩
                       + C_0 (‖G′w‖²_(𝗌−½+δ_c) + ‖χw‖²_(−N′)).                                             {#eq:ii-d-2-1}

Then the conclusion [[eq:ii-a1-4-3]] of [[lem:ii-a1-4-1]] holds.

*Proof.* As for [[lem:ii-a1-4-1]], with two additions. In Step 1, for fixed ε, ⟨J_ε L w_t, w_t⟩ → ⟨J_ε L v, v⟩ as t →
0: w_t → v in H^(𝗌−κ), so L w_t → L v in H^(𝗌−κ−m), and J_ε* w_t → J_ε* v in H^(−𝗌+m+κ), J_ε* having order 2𝗌 − m − 2κ
for this ε without loss ([[prop:ii-a1-2-4]] (a), (c)). In Step 2 the new term is bounded at v = Φu: Lv = ΦLu + [L, Φ]u,
and J_ε[L, Φ] has every order uniformly, by [[prop:ii-a1-2-4]] (e), as in Step 0; and |⟨ΦLu, J_ε* v⟩| ≤ ‖ΦLu‖_(𝗌−m+1)
‖J_ε* v‖_(−𝗌+m−1). J_ε* is uniformly of order 2𝗌 − m + δ for every δ > 0 and microsupported in K_1, so ‖J_ε* v‖_(−𝗌+m−1)
≤ C(‖Gu‖_(𝗌−1+δ) + ‖χu‖_(−N′)). With δ ≤ ½ and Step 0, 2|⟨J_ε L v, v⟩| ≤ C(‖GLu‖²_(𝗌−m+1) + ‖Gu‖²_(𝗌−½+δ_c) +
‖χu‖²_(−N′)), which is of the form of the right side of [[eq:ii-a1-4-3]]. ∎

**Lemma {#lem:ii-d-2-2}** (Iteration.) [[lem:ii-a1-4-2]] holds with [[lem:ii-d-2-1]] in place of [[lem:ii-a1-4-1]].

*Proof.* The proof of [[lem:ii-a1-4-2]] uses [[lem:ii-a1-4-1]] only through its conclusion [[eq:ii-a1-4-3]] at each
step, which [[lem:ii-d-2-1]] supplies under its hypotheses; the proof therefore applies without change. ∎

**Lemma {#lem:ii-d-2-3}** (From a symbol identity to [[eq:ii-d-2-1]].) Let s be a constant order, k := s − ½(m − 1),
ǎ ∈ C^(M+2) S̃^k real and scalar, supported in a compact set K_1 near fibre infinity, and ǎ_ε := φ_ε ǎ. Suppose that
near fibre infinity

    ς (H_ℓ(ǎ_ε²) + 2ǎ_ε² ℓ_I) = −b_ε* b_ε − Σ_j b′_(j,ε)* b′_(j,ε) + Σ_i e_(i,ε)* e_(i,ε) + j_ε ℓ + f_ε,   {#eq:ii-d-2-2}

with matrix symbols b_ε, b′_(j,ε), e_(i,ε) bounded in C^(M+2) S̃^s and lying in C^(M+2) S̃^(s−κ) for each ε, scalar j_ε
as in [[lem:ii-d-2-1]] (with ν = 0), and f_ε bounded in C^(M+2) S̃^(2s−1), all supported in K_1. Then [[eq:ii-d-2-1]]
holds with B_ε := Op(b_ε), E_ε := Op(e_ε) for the column e_ε of the e_(i,ε), J_ε := ½ Op(j_ε) and δ_c = 0; C_0
depends on finitely many norms of the symbols.

*Proof.* With constant orders and index 0, the remainders of [[prop:ii-a1-2-4]] (b)–(f) have exact orders. As in the
paragraph on the commutator in the proof of [[prop:ii-a1-5-3]], i[L_R, Ǎ_ε* Ǎ_ε] = Op(H_ℓ(ǎ_ε²)) + R_1 with R_1 of
order 2s − 1. The operator L_I Ǎ_ε* Ǎ_ε + Ǎ_ε* Ǎ_ε L_I − Op(2ǎ_ε² ℓ_I) is an expression in quantisations whose
principal symbol vanishes at order 2s, ǎ_ε being scalar. So by [[prop:ii-a1-2-4]] (f) it has order 2s − 1. Hence
ς C_(ǎ_ε) is the quantisation of the right side of [[eq:ii-d-2-2]] plus an operator of order 2s − 1. By
[[prop:ii-a1-2-4]] (b), (c), Op(b*b) = Op(b)* Op(b) modulo order 2s − 1, and Op(jℓ) = Op(j) L modulo order 2s − 1, as
L = Op(ℓ_f) + R_L with ℓ_f − ℓ of order m − 1. All remainders are uniform in ε and have a factor supported in K_1, so
paired with w they are at most C(‖G′w‖²_(s−½) + ‖χw‖²_(−N′)) ([[prop:ii-a1-2-4]] (e)). ⟨C_(ǎ_ε) w, w⟩ is real, so
taking real parts and dropping −Σ_j ‖Op(b′_j) w‖² gives [[eq:ii-d-2-1]]. ∎

**Lemma {#lem:ii-d-2-4}** (Norms through symbols.) Let q ∈ C^(M) S̃^0 be matrix-valued and supported in a compact set
K_1 near fibre infinity, and M_q := sup|q|, the supremum of the operator norm. For every η > 0 there is C_η, depending
on q through finitely many norms, such that for w ∈ L² carried by χ

    ‖Op(q) w‖ ≤ (M_q + η) ‖w‖ + C_η (‖G′w‖_(−½) + ‖χw‖_(−N′)),                                             {#eq:ii-d-2-3}

with G′ elliptic on K_1.

*Proof.* (M_q + η)² − q*q ≥ η², so its positive square root c lies in C^(M) S̃^0 ([[lem:ii-a1-2-5]] (i), for positive
definite matrices), and c − (M_q + η) is supported in K_1. By [[prop:ii-a1-2-4]] (b), (c), Op(c)* Op(c) = (M_q + η)² −
Op(q)* Op(q) + R, with R of order −1 and microsupported in K_1, as every symbol involved is constant off K_1 and the
quantisation of a constant is the identity modulo operators of every order. Hence ‖Op(q) w‖² ≤ (M_q + η)² ‖w‖² +
|⟨Rw, w⟩|, and |⟨Rw, w⟩| ≤ C_η(‖G′w‖²_(−½) + ‖χw‖²_(−N′)). ∎

The pairing identities used below hold at the distributions considered: if G′v ∈ H^(s−½), G′Lv ∈ H^(s−m+½) for G′
elliptic on K_1 and χv ∈ H^(−N′), and κ ≥ 2, then ⟨C_(ǎ_ε) v, v⟩ = 2 Im⟨Ǎ_ε L v, Ǎ_ε v⟩ for each ε > 0, by Step 1 of
the proof of [[lem:ii-a1-4-1]] (the regularised commutant has order k − κ ≤ k − 2).

**Lemma {#lem:ii-d-2-5}** (Comparison of norms.) Let 𝗍 be a constant and z, x_1, …, x_m ∈ C^(M) S̃^0 matrix-valued and
supported in a compact set K_1 near fibre infinity, and suppose that z = Σ_i q_i x_i on a neighbourhood of supp z, with
q_i ∈ C^(M) S̃^0 and M_i := sup|q_i|. This holds with M_i = c_*^(−1/2) if |z| ≤ 1 and Σ_i x_i* x_i ≥ c_* > 0 on a
neighbourhood V of supp z. Then for every η > 0 there is C_η, independent of ε ∈ (0, 1] and depending on the symbols
through finitely many norms, such that for w ∈ H^(K′)_e3b carried by χ

    ‖Op(ρ^(−𝗍) φ_ε z) w‖ ≤ Σ_i (M_i + η) ‖Op(ρ^(−𝗍) φ_ε x_i) w‖ + C_η (‖G′w‖_(𝗍−½) + ‖χw‖_(−N′)),       {#eq:ii-d-2-4}

with G′ elliptic on K_1. If κ ≥ ½, [[eq:ii-d-2-4]] holds also for w with G′w ∈ H^(𝗍−½) and χw ∈ H^(−N′): for fixed ε
both sides are then finite and continuous in w, and [[lem:ii-a1-2-3]] (b) approximates w.

*Proof.* Replacing q_i by ζ q_i, with ζ equal to 1 near supp z and supported in the neighbourhood, z = Σ_i q_i x_i
everywhere. By [[prop:ii-a1-2-4]] (b), Op(ρ^(−𝗍) φ_ε z) = Σ_i Op(q_i) Op(ρ^(−𝗍) φ_ε x_i) + R_ε, with R_ε uniformly of
order 𝗍 − 1 and microsupported in K_1. [[lem:ii-d-2-4]] applied to Op(q_i) and Op(ρ^(−𝗍) φ_ε x_i) w gives
[[eq:ii-d-2-4]], as ‖G′ Op(ρ^(−𝗍) φ_ε x_i) w‖_(−½) ≤ C(‖G″w‖_(𝗍−½) + ‖χw‖_(−N′)). In the particular case put X :=
Σ_j x_j* x_j and q_i := ζ z X⁻¹ x_i* with ζ supported in V. Then Σ_i q_i x_i = ζz = z and Σ_i q_i q_i* = ζ² z X⁻¹ z* ≤
c_*⁻¹, so |q_i| ≤ c_*^(−1/2). ∎

In [[lem:ii-d-2-3]] and in [[lem:ii-a1-4-1]] and [[lem:ii-a1-4-2]], L enters only through L = Op(ℓ_f) + R_L, with ℓ_f
∈ C^(d_0) S̃^m (matrix-valued, with real scalar principal part ℓ) and R_L bounded of every order. So they hold for
operators of that form, such as L plus the quantisation of a first-order symbol of finite regularity. We use this in
[[sec:ii-d-4]].

The iteration of [[lem:ii-a1-4-2]] uses its hypotheses only at the orders 𝗌_j = 𝗌 − τ + jκ with the exponent κ = τ/J,
for which the effective orders 𝗌_j − κθ_ε of the regularised commutant lie in [𝗌 − τ, 𝗌]. So in [[lem:ii-d-2-2]] it
suffices that the hypotheses hold for orders 𝗌′ and exponents κ with 𝗌 − τ ≤ 𝗌′ − κ and 𝗌′ ≤ 𝗌. This is what makes
thresholds compatible with the regularisation.

### Radial point estimates {#sec:ii-d-3}

Each estimate below is proved by the same steps; we write them once.

*The pattern.* (1) Near the radial set R, a local operator L′ := W′⁻¹P ([[sec:ii-d-1-1]]) is conjugated to L″ :=
A⁻¹w⁻¹L′wA ([[lem:ii-d-1-1]]), acting on ũ := A⁻¹w⁻¹u, with A the frame of a fibre inner product chosen for R. (2) The
commutant is ǎ := ρ^(−s+½) Ψ χ_∞, with s the (constant) order, ρ the function of [[sec:ii-d-1-1]] for R, Ψ a product of
cut-offs, and χ_∞ a function of ρ equal to 1 near fibre infinity and supported where the coordinates are defined, whose
derivatives are of order −∞ and are put into f_ε; it is regularised by φ_ε with the same ρ. (3) With s_ε := s − κθ_ε
∈ [s − κ, s], [[eq:ii-a1-2-1]] and [[eq:ii-d-1-1]] give, where χ_∞ = 1,

    H_ℓ(ǎ_ε²) + 2ǎ_ε² ℓ_I = ρ^(−2s) φ_ε² (−Ψ² Q_ε + 𝖧(Ψ²)),
    Q_ε := (2s_ε − 1) ρ⁻¹𝖧ρ − 2A⁻¹ (𝔭′ − ½ 𝖧 log W′ − 𝖧 log w) A,                                    {#eq:ii-d-3-1}

with ℓ = W′⁻¹G, 𝖧 = ρH_ℓ and 𝔭′ = ρW′⁻¹ σ_1(Im_h P). Indeed H_ℓ = ρ⁻¹𝖧, 𝖧(ρ^(−2s+1) φ_ε²) = −(2s_ε − 1) ρ^(−2s+1)
φ_ε² ρ⁻¹𝖧ρ, and 2ρℓ_I = 2A⁻¹(⋯)A by [[eq:ii-d-1-1]]. (4) At R, Q_ε ≥ 2c for some c > 0 and all s_ε in the range of
the iteration, by the threshold; so Q_ε ≥ c on supp Ψ once the cut-offs are localised close to R, and −Ψ² Q_ε ρ^(−2s)
φ_ε² = −b_ε* b_ε with b_ε := ρ^(−s) φ_ε Ψ Q_ε^(1/2) ([[lem:ii-a1-2-5]] (i)), and ǎ_ε = z_ε b_ε, z_ε := ρ^(1/2)
Q_ε^(−1/2) (with Q_ε replaced by c, smoothly, off a neighbourhood of supp Ψ). (5) 𝖧(Ψ²) is a sum of terms 2𝔐 ψψ′(𝔐f)
𝖧f · (other factors)², one for each factor ψ(𝔐f) of Ψ, where ψ is the cut-off of [[sec:ii-a1-5-2]]: even, supported in
(−1, 1), equal to 1 on [−½, ½], non-increasing on [0, ∞), with −ψψ′ the square of a smooth function on [0, ∞). Where 𝖧f
> 0 on the support of ψ′(𝔐f) the term is −b′*b′; where 𝖧f < 0 it is +e*e, and its support determines E. A factor
ψ(𝔐_Σ ρ²ℓ), a cut-off to the characteristic set, contributes j_ε ℓ, since 𝖧(ρ²ℓ) = 2(ρ⁻¹𝖧ρ) ρ²ℓ, 𝖧ℓ being 0. (6)
[[lem:ii-d-2-3]] gives [[eq:ii-d-2-1]] for L″, [[lem:ii-d-2-1]] and [[lem:ii-d-2-2]] give the estimate for ũ with Γ :=
R and τ := s − s_0, and [[sec:ii-d-1-2]] returns it to u.

The constants depend on P through finitely many norms of the coefficients of L″, and through c and the signs in (5).
These hold with margins at R, where the quantities are those of the normal form of P (the second-order part of P − P_0
vanishes at the face containing R), and near R they change by O(ε_P) ([[lem:ii-c-4-1]]). So the cut-offs chosen for P_0
serve for every P with ε_P small, and the estimates hold uniformly, with d_0 fixed by the regularity that
[[lem:ii-d-2-1]]–[[lem:ii-d-2-3]] and [[prop:ii-a1-2-4]] need at the orders involved. We prove the estimates on ∂Σ⁺. On
∂Σ⁻ the future field is −𝖧, ς = −1, and the antipodal map exchanges the two components. G is even, and σ_1(Im_h P) is
odd in the covector, so ς𝔭′ and every threshold are the same there. Throughout, B, E, G ∈ C_b^∞Ψ^0_e3b are carried by
χ, and "strong sense" means: if the right side is finite, so is the left, and the estimate holds.

**Proposition {#prop:ii-d-3-1}** (The horizon.) There are B, E, G such that (1) their operator wave front sets lie in
any fixed neighbourhood U of ∂R_(𝓗⁺); (2) their Schwartz kernels are supported in K × K for any fixed compact
neighbourhood K ⊂ M of 𝓗⁺ ∩ K⁺ = {r = r_h, ρ_K = 0}; (3) B is elliptic at ∂R_(𝓗⁺); (4) the Schwartz kernel of E is
supported in (K ∖ K⁺)²; and such that for all constants s > s_0 > ½ + ϑ_𝓗 ([[eq:i-a-1-5]]), α_K ∈ ℝ, and χ̃ ∈ C^∞(M)
supported near K and equal to 1 near K,

    ‖Bu‖_(H^(s,α_K)) ≤ C (‖GPu‖_(H^(s−1,α_K)) + ‖Eu‖_(H^(s,α_K)) + ‖χ̃u‖_(H^(s_0,α_K)))                  {#eq:ii-d-3-2}

in the strong sense, for P = P_0 and every P with ε_P small, with d_0 depending only on s, s_0. Here H^(s,α_K) :=
H^(s,(2α_I,α_+,α_K))_e3b over K, where x_I and ρ_+ are smooth and positive, so that α_I, α_+ do not matter.

This is [Hin26c, Proposition 7.4] in dimension 4 + 1.

*Proof.* W′ := 1, ρ the function of (H3) (extended positive, even and homogeneous of degree −1), 𝖧 = ρH_G, w :=
ρ_K^(α_K) with ρ_K = t_*⁻¹, and A the frame of an inner product for which ϑ_𝓗 of [[eq:i-a-1-5]] is attained (ϑ_𝓗 is
the supremum of max spec(β_0⁻¹ p_(1,+)(0)) over ∂ℛ_+, with p_(1,+)(0) = ρ σ_1(Im_h P̂(0))). ∂R_(𝓗⁺) lies over K⁺ in {σ
= 0}, where σ_1(Im_h P_0) = σ_1(Im_h P̂(0)) ([[sec:ii-c-2-3]]), and P − P_0 has coefficients vanishing at K⁺; so 𝔭′ =
p_(1,+)(0) there. By [[eq:ii-b-4-1]], ρ⁻¹𝖧ρ = β_0 and ρ_K⁻¹𝖧ρ_K = ρ_K(ρ_K⁻²𝖧ρ_K) = 0 at ∂R_(𝓗⁺). So at ∂R_(𝓗⁺), as
A⁻¹𝔭′A has the eigenvalues of the h-self-adjoint 𝔭′,

    Q_ε = (2s_ε − 1)β_0 − 2A⁻¹𝔭′A ≥ (2s_ε − 1 − 2ϑ_𝓗)β_0 ≥ (2s_0 − 1 − 2ϑ_𝓗) inf β_0 =: 2c > 0

for s_ε ≥ s_0, which is the range of the iteration ([[lem:ii-d-2-2]] and the remark after [[lem:ii-d-2-5]]).

Let F be the quadratic defining function of [[lem:ii-b-4-2]], with 𝖧F ≥ c_F F on a neighbourhood W of ∂R_(𝓗⁺) in
³ᵇS*_((K⁺)°) M_0. F does not depend on t_*, and the field of P_0 is invariant under t_*-translations, so 𝖧_(P_0)F ≥
c_F F on W × {ρ_K ≤ ρ_0}. For P, 𝖧 − 𝖧_(P_0) = O(ε_P ρ_K^(ℓ_K)) in C^(d_0−1), and |dF| ≤ CF^(1/2), so 𝖧F ≥ ½c_F F where
F ≥ (2𝔐_R)⁻¹ and ρ_K ≤ 𝔐⁻¹, for 𝔐 large given 𝔐_R. As F is defined only on W, extend it to a smooth t_*-independent
function bounded below by a positive constant outside a smaller t_*-invariant neighbourhood W′ of ∂R_(𝓗⁺) with closure
in W; for 𝔐_R large, ψ(𝔐_R F) is then a symbol supported in W′. Put Ψ := ψ(𝔐_R F) ψ(𝔐ρ_K). Then

    𝖧(Ψ²) = 2𝔐_R (ψψ′)(𝔐_R F) 𝖧F ψ(𝔐ρ_K)² + 2𝔐 (ψψ′)(𝔐ρ_K) 𝖧ρ_K ψ(𝔐_R F)².

The first term is ≤ 0 and is −b′*b′ with b′ := ρ^(−s) φ_ε θ(𝔐_R F) (2𝔐_R 𝖧F)^(1/2) ψ(𝔐ρ_K), θ := (−ψψ′)^(1/2), smooth
as 𝖧F ≥ c_F/(4𝔐_R) on the support of θ(𝔐_R F). In the second, 𝖧ρ_K = ρ_K²(ρ_K⁻²𝖧ρ_K) ≤ −½ββ_0ρ_K² < 0 near
∂R_(𝓗⁺) ([[eq:ii-b-4-1]]), so it is +e*e with e := ρ^(−s) φ_ε θ(𝔐ρ_K) (−2𝔐𝖧ρ_K)^(1/2) ψ(𝔐_R F), supported in {ρ_K ≥
(2𝔐)⁻¹}, away from K⁺; so E can be chosen with Schwartz kernel in (K ∖ K⁺)², as (4) requires. Choosing 𝔐_R and then 𝔐
large, supp Ψ lies in U, in W and in {Q_ε ≥ c}. No cut-off to the characteristic set is needed, as the signs hold on a
full neighbourhood of ∂R_(𝓗⁺) ([[lem:ii-b-4-2]]); so [[eq:ii-d-2-2]] holds with j_ε = 0. The pattern (6) gives
[[eq:ii-d-3-2]], with ‖χũ‖_(−N′) ≤ C‖χ̃u‖_(H^(s_0,α_K)). ∎

**Proposition {#prop:ii-d-3-2}** (The incoming radial set over ∂K⁺.) There are B, E, G with (1) operator wave front
sets in any fixed neighbourhood of ∂R_(∂K⁺,in); (2) Schwartz kernels in K × K for any fixed compact neighbourhood K of
∂K⁺; (3) B elliptic at ∂R_(∂K⁺,in); (4) the Schwartz kernel of E supported in (K ∖ K⁺)²; such that for all constants s
> s_0, α_+, α_K with

    s_0 + α_+ > ½(−1 + ϑ^3b_in) + α_K                                                                    {#eq:ii-d-3-3}

([[eq:ii-c-2-1]]), and χ̃ as before,

    ‖Bu‖_(H^(s,(α_+,α_K))) ≤ C (‖GPu‖_(H^(s−1,(α_++2,α_K))) + ‖Eu‖_(H^(s,(α_+,α_K)))
                               + ‖χ̃u‖_(H^(s_0,(α_+,α_K))))                                               {#eq:ii-d-3-4}

in the strong sense, for P = P_0 and every P with ε_P small, d_0 depending only on s, s_0. Near ∂K⁺, x_I is smooth and
positive, so the weights are (α_+, α_K).

This is [Hin26c, Proposition 7.6] in dimension 4 + 1.

*Proof.* W′ := ρ_+², with ρ_+ = r⁻¹ and ρ_K = r/t_*; ℓ = ρ_+⁻²G = G_3b ([[eq:ii-b-3-2]]); ρ := −σ_3b⁻¹, ξ̂, η̂ as in
[[eq:ii-b-3-3]], so 𝖧 is the field of [[eq:ii-b-3-4]]; w := ρ_+^(α_+) ρ_K^(α_K); A the frame of an inner product
attaining ϑ^3b_in. Then 𝔭′ = ρ σ^1_3b(r² Im_h P), which at R := ∂R_(∂K⁺,in) is that of P_0, the coefficients of P − P_0
vanishing at ∂K⁺ (and the terms with χ_I in [[eq:ii-c-3-2]] vanishing near ∂K⁺). At R, 𝖧 = 0 and, by [[eq:ii-b-3-4]]
and its linearisation, ρ⁻¹𝖧ρ = 2, ρ_+⁻¹𝖧ρ_+ = 2, ρ_K⁻¹𝖧ρ_K = −2. So, at R,

    Q_ε = 2(2s_ε − 1) − 2A⁻¹𝔭′A + 2·2 + 2(2α_+ − 2α_K) ≥ 4(s_ε + α_+ − α_K − ½(−1 + ϑ^3b_in)),

which is at least 2c > 0 for s_ε ≥ s_0, by [[eq:ii-d-3-3]].

Put q := |η̂|² + (ξ̂ − 2)² and Ψ := ψ(𝔐_R q) ψ(𝔐ρ_+) ψ(𝔐ρ_K). Over ι⁺, where 𝖧 = 𝖧̄, [[eq:ii-b-3-4]] gives 𝖧̄ξ̂ =
−2(2 − ξ̂)ξ̂ and 𝖧̄|η̂|² = −4(1 − ξ̂)|η̂|² (the terms with ∂_ω|η̂|² and 𝖧̄ω cancel, the Hamilton field of |η̂|² on T*𝕊³
preserving it). Hence ([Hin26c, p. 120])

    𝖧̄q = 4(ξ̂ − 1)|η̂|² + 4ξ̂(ξ̂ − 2)² ≥ 2q     for |ξ̂ − 2| ≤ ½,

on the full phase space over ι⁺, not only on the characteristic set. 𝖧 − 𝖧̄ ∈ ρ_+² 𝒱_b plus O(ε_P ρ_+^(ℓ_+)
ρ_K^(ℓ_K)) ([[sec:ii-b-3-1]], [[lem:ii-c-4-1]]), so 𝖧q ≥ (2𝔐_R)⁻¹ on supp ψ′(𝔐_R q) ∩ supp ψ(𝔐ρ_+)ψ(𝔐ρ_K) for 𝔐
large given 𝔐_R. Near R, ρ_+⁻¹𝖧ρ_+ ≥ 1 and ρ_K⁻¹𝖧ρ_K ≤ −1. So in (5) of the pattern, the factors ψ(𝔐_R q) and
ψ(𝔐ρ_+) give −b′*b′ terms, and ψ(𝔐ρ_K) gives +e*e, supported in {ρ_K ≥ (2𝔐)⁻¹}, away from K⁺, as (4) requires; j_ε =
0. The pattern gives [[eq:ii-d-3-4]]. ∎

**Proposition {#prop:ii-d-3-3}** (The outgoing radial set over ∂K⁺.) There are B, E, G with (1)–(3) as in
[[prop:ii-d-3-2]] with ∂R_(∂K⁺,out) in place of ∂R_(∂K⁺,in), and (4) the operator wave front set of E disjoint from
∂W_out = {ρ_+ = 0, ξ̂ = 0, η̂ = 0}, the unstable manifold of ∂R_(∂K⁺,out) over ι⁺ ([[lem:ii-b-3-3]] (4)); such that for
all constants s > s_0, α_+, α_K with

    s + α_+ < ½(−1 + ϑ_out) + α_K                                                                        {#eq:ii-d-3-5}

([[eq:ii-c-2-1]]), [[eq:ii-d-3-4]] holds in the strong sense, for P = P_0 and every P with ε_P small.

This is [Hin26c, Proposition 7.7] in dimension 4 + 1.

*Proof.* As for [[prop:ii-d-3-2]], with A the frame of the inner product of [[lem:ii-c-2-5]], for which −A⁻¹𝔭′A ≥
ϑ_out at R := ∂R_(∂K⁺,out) ([[lem:ii-c-2-6]]: there −𝔭′ = S + S^(*h)). At R, ρ⁻¹𝖧ρ = −2, ρ_+⁻¹𝖧ρ_+ = −2, ρ_K⁻¹𝖧ρ_K
= 2 ([[eq:ii-b-3-4]] at ξ̂ = 0). So at R

    Q_ε = −2(2s_ε − 1) − 2A⁻¹𝔭′A − 4 + 2(−2α_+ + 2α_K) ≥ 4(½(−1 + ϑ_out) + α_K − α_+ − s_ε),

at least 2c > 0 for s_ε ≤ s, by [[eq:ii-d-3-5]]: the threshold is an upper bound, met by every order of the iteration.
Put q := |η̂|² + ξ̂²; by [[eq:ii-b-3-4]], over ι⁺,

    𝖧̄q = −4(1 − ξ̂)|η̂|² − 4(2 − ξ̂)ξ̂² ≤ −2q     for |ξ̂| ≤ ½,

which is [Hin26c, (7.18)]. With Ψ := ψ(𝔐_R q) ψ(𝔐ρ_+) ψ(𝔐ρ_K), now ψ(𝔐ρ_K) gives a −b′*b′ term (ρ_K⁻¹𝖧ρ_K ≥ 1 near
R), while ψ(𝔐_R q) and ψ(𝔐ρ_+) give +e*e terms (𝖧q < 0 on supp ψ′(𝔐_R q), ρ_+⁻¹𝖧ρ_+ ≤ −1). These are supported in
{q ≥ (2𝔐_R)⁻¹}, disjoint from {ξ̂ = η̂ = 0} ⊃ ∂W_out, and in {ρ_+ ≥ (2𝔐)⁻¹}, away from ι⁺ ⊃ ∂W_out. So E can be chosen
elliptic on both with WF′(E) ∩ ∂W_out = ∅, and these sets meet fibre infinity in U ∖ R, as [[lem:ii-d-2-2]] requires. ∎

**Lemma {#lem:ii-d-3-4}** (The subprincipal symbol at ℐ⁺.) Near ℐ⁺ ∩ Ω, with ρ_+ = t_*⁻¹, x_I = (t_*/r)^(1/2), ω, the
eb-momenta of [[sec:ii-b-7]] and ρ := σ_eb⁻¹, ξ̂ := ξ_eb/σ_eb, 𝖧 := ρH_(G_eb), let h be a smooth fibre inner product
with Gram matrix 𝖦, and 𝔭 := ρ x_I⁻² ρ_+⁻² σ_1(Im_h P). Then over ℐ⁺

    𝔭 = (Re_h p_1)(ξ̂ − 2) + ½ 𝖦⁻¹ 𝖧 𝖦,       Re_h p_1 := ½(p_1 + p_1^(*h)),                             {#eq:ii-d-3-6}

with p_1 = S|_(∂X) + p̃_1 of [[def:ii-c-3-3]]. In particular 𝔭 = 0 at ∂R_(ℐ⁺,in,+) and 𝔭 = −2 Re_h p_1 at
∂R_(ℐ⁺,out), where 𝖧 = 0.

This is [Hin26c, (7.22)] in dimension 4 + 1.

*Proof.* *The density.* With t_* = ρ_+⁻¹ and r = ρ_+⁻¹ x_I⁻², |dt dx| = r³|dt_* dr dω| = 2ρ_+⁻⁵ x_I⁻⁸ |(dρ_+/ρ_+)
(dx_I/x_I) dω|, dω the round density of 𝕊³ (as |dt_* ∧ dr| = 2ρ_+⁻³ x_I⁻³ |dρ_+ ∧ dx_I|; [[lem:ii-a-6-1]]). For it,
(x_I ∂_(x_I))* = −x_I ∂_(x_I) + 8, (ρ_+ ∂_(ρ_+))* = −ρ_+ ∂_(ρ_+) + 5, Δ_𝕊³ is symmetric, and so are multiplications by
real functions.

*The operator.* Put X_1 := x_I ∂_(x_I) − 2ρ_+ ∂_(ρ_+), X_2 := x_I ∂_(x_I), W := x_I² ρ_+². By [[lem:ii-c-3-4]], P =
P_s + W p_1 X_1 + ½W(p_0 + R) with P_s := ½W(−(X_2 − 3)X_1 + 2x_I² Δ_𝕊³) ⊗ Id and R ∈ C^((d_0;0),(2ℓ_I,0))_(eb;b)
Diff²_eb.

(i) P_s is symmetric for the standard inner product. X_1* = −X_1 − 2 and (X_2 − 3)* = −(X_2 − 5), so (W(X_2 − 3)X_1)* =
(X_1 + 2)(X_2 − 5)W. As X_2 W = W(X_2 + 2) and X_1 W = W(X_1 − 2), this is W X_1 (X_2 − 3) = W(X_2 − 3)X_1, X_1 and
X_2 commuting. And (W x_I² Δ)* = Δ x_I² W = W x_I² Δ. With h, P_s^(*h) = 𝖦⁻¹P_s𝖦 = P_s + 𝖦⁻¹[P_s, 𝖦], so
σ_1(Im_h P_s) = ½ 𝖦⁻¹ H_(σ_2(P_s)) 𝖦. Here σ_2(P_s) = W(G_eb + O(x_I^(2ℓ_I))), and H_(W G_eb) 𝖦 = W H_(G_eb) 𝖦 as 𝖦
and W are functions of the base.

(ii) (W p_1 X_1)^(*h) = 𝖦⁻¹ X_1* p_1* W 𝖦, and σ(X_1) = i(ξ_eb − 2σ_eb), so σ_1(Im_h(W p_1 X_1)) = W (Re_h p_1)
(ξ_eb − 2σ_eb), as 𝖦⁻¹ p_1* 𝖦 = p_1^(*h).

(iii) p_0 is of order 0. R has real scalar principal symbol and coefficients in x_I^(2ℓ_I) C^((d_0;0))_(eb;b), a class
preserved by eb-derivatives, so σ_1(Im_h R) is O(x_I^(2ℓ_I)).

Multiplying by ρW⁻¹ and setting x_I = 0 gives [[eq:ii-d-3-6]]. ∎

In dimension 3 + 1 the density is r²|dt_* dr dω₂| = 2ρ_+⁻⁴ x_I⁻⁶ |⋯|, dω₂ the round density of 𝕊², for which ½ x_I²
ρ_+² (x_I ∂_(x_I) − 2)(x_I ∂_(x_I) − 2ρ_+ ∂_(ρ_+)) is symmetric. In dimension 4 + 1 the density r³ and the constant 3
of [[lem:ii-c-3-4]] match in the same way, so [[eq:ii-d-3-6]] has the same form as [Hin26c, (7.22)]. With a varying
inner product, the term ½𝖦⁻¹𝖧𝖦 appears, and it vanishes at the radial sets.

**Proposition {#prop:ii-d-3-5}** (The incoming radial set at ℐ⁺ ∩ ι⁺.) There are B, E, G with (1) operator wave front
sets in any fixed neighbourhood of ∂R_(ℐ⁺,in,+); (2) Schwartz kernels in K × K for any fixed compact neighbourhood K of
ℐ⁺ ∩ ι⁺; (3) B elliptic at ∂R_(ℐ⁺,in,+); (4) the Schwartz kernel of E supported in (K ∖ ι⁺)²; such that for all
constants s > s_0 and α_I, α_+ with

    α_+ < α_I − ½,                                                                                         {#eq:ii-d-3-7}

and χ̃ as before,

    ‖Bu‖_(H^(s,(2α_I,α_+))) ≤ C (‖GPu‖_(H^(s−1,(2α_I+2,α_++2))) + ‖Eu‖_(H^(s,(2α_I,α_+)))
                                + ‖χ̃u‖_(H^(s_0,(2α_I,α_+))))                                             {#eq:ii-d-3-8}

in the strong sense, for P = P_0 and every P with ε_P small. Near ℐ⁺ ∩ ι⁺, ρ_K is smooth and positive, so the weights
are (2α_I, α_+).

This is [Hin26c, Proposition 7.8] in dimension 4 + 1.

*Proof.* W′ := W = x_I² ρ_+², ℓ = G_eb, ρ := σ_eb⁻¹, 𝖧 the field of [[eq:ii-b-7-3]]–[[eq:ii-b-7-4]], w := x_I^(2α_I)
ρ_+^(α_+), A := Id. At R := ∂R_(ℐ⁺,in,+) = {ρ_+ = x_I = 0, ξ̂ = 2, η̂ = 0}, 𝖧 = 0, and by [[eq:ii-b-7-4]], ρ⁻¹𝖧ρ = 0,
x_I⁻¹𝖧x_I = ξ̂ − 1 = 1, ρ_+⁻¹𝖧ρ_+ = −ξ̂ = −2; and 𝔭′ = 0 by [[lem:ii-d-3-4]]. So at R, independently of s_ε,

    Q_ε = 0 + 𝖧 log W + 2𝖧 log w = 2·1 + 2·(−2) + 2(2α_I·1 + α_+·(−2)) = 4(α_I − α_+ − ½) ≥ 2c > 0

by [[eq:ii-d-3-7]]. Near R, ρ⁻¹𝖧ρ = O(x_I²) + O(ε_P x_I^(2ℓ_I)), as 𝖧^0 ρ = 0 exactly for the field 𝖧^0 of
[[eq:ii-b-7-4]]; so the term (2s_ε − 1)ρ⁻¹𝖧ρ is small on supp Ψ, uniformly for s_ε in the range of the iteration, and
Q_ε ≥ c there.

Put q := (ξ̂ − 2)² + |η̂|² and Ψ := ψ(𝔐_Σ ρ²ℓ) ψ(𝔐_R q) ψ(𝔐x_I) ψ(𝔐ρ_+). Over ℐ⁺, 𝖧 = 𝖧^0, with 𝖧^0 ξ̂ = −2|η̂|² and
𝖧^0|η̂|² = 2(ξ̂ − 1)|η̂|² (the angular motion stops at x_I = 0). On the characteristic set over ℐ⁺, |η̂|² = ½ξ̂(2 −
ξ̂) ([[lem:ii-b-7-2]] (1)), so

    𝖧^0 q = −4(ξ̂ − 2)|η̂|² + 2(ξ̂ − 1)|η̂|² = 2ξ̂(2 − ξ̂)² + 2(ξ̂ − 1)|η̂|² ≥ q     for |ξ̂ − 2| ≤ ½,

which is [Hin26c, (7.21)]. Off the characteristic set, |η̂|² = ½ξ̂(2 − ξ̂) + ρ² G^0_eb, and ρ²(ℓ − G^0_eb) = O(x_I²) +
O(ε_P x_I^(2ℓ_I)); so 𝖧q ≥ (4𝔐_R)⁻¹ on supp ψ′(𝔐_R q) within the support of the other factors, for 𝔐_Σ, 𝔐 large
given 𝔐_R. Near R, x_I⁻¹𝖧x_I ≥ ½ and ρ_+⁻¹𝖧ρ_+ ≤ −1, on the full phase space. So in (5) of the pattern: ψ(𝔐_R q) and
ψ(𝔐x_I) give −b′*b′; ψ(𝔐ρ_+) gives +e*e, supported in {ρ_+ ≥ (2𝔐)⁻¹}, away from ι⁺, as (4) requires; ψ(𝔐_Σ ρ²ℓ)
gives j_ε ℓ, with j_ε of order 2s − 2. The pattern gives [[eq:ii-d-3-8]]. ∎

**Proposition {#prop:ii-d-3-6}** (The outgoing radial set over ℐ⁺.) Let t_(*,−) ∈ ℝ. There are B, E, G with (1)
operator wave front sets in any fixed neighbourhood of ∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥ t_(*,−)}; (2) Schwartz kernels in K × K
for any fixed compact neighbourhood K ⊂ M̃ of cl(ℐ⁺ ∩ {t_* ≥ t_(*,−)}); (3) B elliptic at ∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥
t_(*,−)}; (4) WF′(E) ∩ ∂R_(ℐ⁺,out) ⊂ {t_*^♭ ≤ t_(*,−) − ¼}; such that for all constants s > s_0 and α_I, α_+ with

    α_I < −½ + p̄_1                                                                                        {#eq:ii-d-3-9}

(p̄_1 of [[def:ii-c-3-5]], for P), [[eq:ii-d-3-8]] holds in the strong sense, for P = P_0 and every P with ε_P small.

This is [Hin26c, Proposition 7.9] in dimension 4 + 1, with t_(*,+) = ∞ and with property (4) in the form stated (see
[[sec:s06-remarks]]).

*Proof.* W′, ℓ, ρ, 𝖧, w as in [[prop:ii-d-3-5]]. Let δ′ := ¼(p̄_1 − ½ − α_I) > 0, and let h_I be a smooth fibre inner
product near cl(ℐ⁺ ∩ Ω) with Re_(h_I) p_1 ≥ p̄_1 − δ′ there. It is constructed as in [[lem:ii-c-2-5]]: p_1 is continuous
on the compact closure of ℐ⁺ ∩ Ω (with p̃_1 ∈ ρ_+^(ℓ_+) C_b tending to 0 at ι⁺), so Jordan scalings at points,
continuity and a smooth partition of unity apply verbatim; h_I is extended independently of x_I. A is its frame. At R
:= ∂R_(ℐ⁺,out) = {x_I = 0, ξ̂ = 0, η̂ = 0}, over all of ℐ⁺, 𝖧 = 0; ρ⁻¹𝖧ρ = 0, x_I⁻¹𝖧x_I = −1, ρ_+⁻¹𝖧ρ_+ = −ξ̂ = 0
([[eq:ii-b-7-4]]); and 𝔭′ = −2 Re_(h_I) p_1 ([[lem:ii-d-3-4]]). So at R

    Q_ε = 4A⁻¹(Re_(h_I) p_1)A − 2 + 2·2α_I·(−1) ≥ 4(p̄_1 − δ′ − ½ − α_I) = 12δ′ =: 2c > 0,

by [[eq:ii-d-3-9]], independently of s_ε; near R, ρ⁻¹𝖧ρ is small as before.

Put q := ξ̂² + |η̂|², fix η_t ∈ C^∞(ℝ) with η_t = 0 on (−∞, −½], η_t = 1 on [−¼, ∞), η_t′ ≥ 0 and (η_t η_t′)^(1/2)
smooth, and ψ_− := η_t(t_*^♭ − t_(*,−)), which equals 1 for t_*^♭ ≥ t_(*,−) − ¼. Put Ψ := ψ(𝔐_Σ ρ²ℓ) ψ(𝔐_R q)
ψ(𝔐x_I) ψ_−. On the characteristic set over ℐ⁺, with |η̂|² = ½ξ̂(2 − ξ̂),

    𝖧^0 q = −4ξ̂|η̂|² + 2(ξ̂ − 1)|η̂|² = −2(2 − ξ̂)ξ̂² − 2(1 − ξ̂)|η̂|² ≤ −q     for |ξ̂| ≤ ½,

and off it, as in [[prop:ii-d-3-5]], 𝖧q ≤ −(4𝔐_R)⁻¹ on supp ψ′(𝔐_R q) within the support of the other factors. Near
R, x_I⁻¹𝖧x_I ≤ −½. So ψ(𝔐_R q) and ψ(𝔐x_I) give +e*e terms, supported in {q ≥ (2𝔐_R)⁻¹} and {x_I ≥ (2𝔐)⁻¹}, both
disjoint from R; ψ(𝔐_Σ ρ²ℓ) gives j_ε ℓ. The factor ψ_− gives 2η_t η_t′ 𝖧t_*^♭ · (other factors)². Whatever its sign,
with C_t := 1 + sup|𝖧t_*^♭| over the support, it is e_−*e_− − b′_−*b′_− with e_−² := 2C_t η_t η_t′ (⋯)² and b′_−² :=
2(C_t − 𝖧t_*^♭) η_t η_t′ (⋯)², both smooth squares. Its support lies in {t_*^♭ ∈ [t_(*,−) − ½, t_(*,−) − ¼]}, which
gives (4); so it misses ∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥ t_(*,−)}, where B is to be elliptic, as [[lem:ii-d-2-2]] requires of the
E-sets. (With η_t = 1 only on [0, ∞) the two sets could touch at t_*^♭ = t_(*,−).) On the characteristic set over Ω°,
𝖧t_*^♭ > 0 ([[lem:ii-c-3-2]] (2)), and e_− is the a priori term at earlier times; off it the sign of 𝖧t_*^♭ is not
used. The other E-sets are disjoint from R. The pattern gives [[eq:ii-d-3-8]]. Here supp Ψ is not compact in t_*^♭,
but it is compact in M̃, its closure meeting ℐ⁺ ∩ ι⁺, where [[eq:ii-b-7-4]] holds uniformly. ∎

In both uses below, t_(*,−) ≤ ½. The kernel of E near its e_−-set can then be supported in {t_*^♭ < 1}², where the u of
[[thm:ii-d-1-2]] vanishes, so that this part of ‖Eu‖ is zero. [Hin26c, Proposition 7.9] states the estimate for t_* ∈
[t_(*,−), t_(*,+)] with t_(*,+) ≤ ∞. For finite t_(*,+) its proof uses H_G t_* ≥ 0 on the support of the commutant,
which fails off the characteristic set near R: at x_I = 0, 𝖧t_*^♭ = t_* ξ̂, and ξ̂ < 0 occurs there. The case t_(*,+) <
∞ serves in [Hin26c] only for control near R at finite times, in Step 1 of its proof of Proposition 7.1, which
[[sec:ii-d-5]] does without.

**Remark {#rem:ii-d-3-7}** (First-order perturbations.) [[prop:ii-d-3-1]]–[[prop:ii-d-3-6]] hold for P + P̃, with P̃ a
first-order operator of the form Op(p̃), p̃ ∈ C^(d_0) S̃^1 (or a finite combination of C^(d_0)_e3b coefficients and
smooth first-order operators). The thresholds are then calculated with σ_1(Im_h(P + P̃)) at R, where this symbol is
continuous. The proofs use P̃ only through ℓ_I in Q_ε, and [[lem:ii-d-2-1]]–[[lem:ii-d-2-3]] hold for such operators
(the remark after [[lem:ii-d-2-5]]). The constants are locally uniform in p̃. This is [Hin26c, Remark 7.5]; it is used
in [[sec:ii-d1-2]].
