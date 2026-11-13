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
