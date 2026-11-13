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

*Notation.* Orders that may vary on phase space are written in sans-serif (𝗌, 𝗍); an order written s, s_0 or s′ is a
constant. For a matrix 𝔞 that is self-adjoint for some fibre inner product, max spec 𝔞 is its largest eigenvalue. N′
is a fixed large integer; every a priori term ‖χu‖_(−N′) below is with respect to it (such terms are written ‖χu‖_(−N)
in [[ch:s04]]), and N_E is the rank of the bundle E = ℂ^(N_E) of [[sec:ii-c-1-1]]. ϕ^u, ϕ^s and ϕ_u, ϕ_s denote the
defining functions of hypersurfaces at the trapped set that [[ch:s02]] and [[ch:s05]] write φ^(u/s), φ_(u/s); here
φ_ε is the regulariser of [[sec:ii-d-2]]. β_0 is the constant of (H3) at the horizon ([[eq:i-a-1-3]],
[[eq:ii-b-4-1]]); the constant ½ min_Γ |q_1| > 0 of condition (Γ.4) of (H7) at the trapped set, which [[ch:s02]] and
[[ch:s05]] also write β_0, is written β_Γ here.

### The setting and the global estimate {#sec:ii-d-1}

#### The operators {#sec:ii-d-1-1}

g_0 is the stationary metric of [[sec:ii-b-1-1]], which satisfies (K1)–(K4) together with the hypotheses (H1)–(H8) of
[[sec:i-a-1-3]], [[sec:i-b-1-2]] and [[sec:i-b-1-5]], and P_0 is a stationary wave-type operator for g_0
([[def:ii-c-1-1]]). The radii r_0 − 2δ_0 < r_0 < r_2 < r_h that enter those hypotheses are arbitrary, subject to the
hypotheses: nothing below uses their values, and the radii chosen from them below (r_1, r_1⁺, r^♮) are chosen again
with them. Fix ℓ_I ∈ (0, ½], ℓ_+ ∈ (0, 1] and ℓ_K > 0. P is a weakly admissible wave-type operator relative to P_0 of
class ((d_0; 0), (2ℓ_I, ℓ_+, ℓ_K)) ([[def:ii-c-3-3]]), and ε_P := ‖P − P_0‖_((d_0;0),(2ℓ_I,ℓ_+,ℓ_K))
([[def:ii-c-3-6]]). Only ℓ_I ∈ (0, ½], ℓ_+ > 0, ℓ_K > 0 are used: the conditions [Hin26c, (5.23)] play no part in
microlocal regularity ([Hin26c, p. 115]). The bound ℓ_+ ≤ 1 is no restriction: as ρ_+ ≤ 1 on Ω, ρ_+^(ℓ_+−1) is
bounded with its b-derivatives for ℓ_+ > 1, so a class with ℓ_+ > 1 lies in the class with ℓ_+ = 1, with norm at most
a constant times its own. Of [[def:ii-c-3-3]], only conditions (1) and (2) are used, together with
[[def:ii-c-3-5]] and [[def:ii-c-3-6]]; condition (3), the triangular structure of p_1 and p_0, is not assumed anywhere in
this chapter. Indeed p_1 and p_0 enter only through [[eq:ii-c-3-1]]–[[eq:ii-c-3-2]] and [[lem:ii-c-3-4]], which follows
from (2); through p̄_1; and through fibre inner products built by Jordan scalings at points, continuity and a partition
of unity, as in [[lem:ii-c-2-5]], which need no triangular structure. Below, "weakly admissible" and "of class" are
meant in this sense. The metric g = g_0 + h of P has ‖h‖ ≤ Cε_P ([[lem:ii-c-3-7]]). So, for ε_P
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

for P = P_0, in the strong sense: if the right side is finite, so is the left, and [[eq:ii-d-1-4]] holds. There is d_0,
depending only on 𝗌_0 and 𝗌, such that [[eq:ii-d-1-4]] holds also for every operator P relative to P_0 satisfying
conditions (1)–(2) of [[def:ii-c-3-3]] with ℓ_I ∈ (0, ½], ℓ_+ > 0, ℓ_K > 0 (condition (3) not assumed) and with ε_P
small, with C uniform.

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
φ_ε has the properties stated after it. [[sec:ii-a1-2]] states both for κ ∈ (0, ½]; they hold for every κ > 0 with the
same proof, the identity being exact for every κ and |1 − φ_ε| ≤ min(1, κερ⁻¹) as in the proof of [[lem:ii-a1-2-3]]
(b). δ_c ∈ [0, ¼] is the constant in the a priori term of [[lem:ii-a1-4-1]] (an
inequality with δ_c = 0 implies the same inequality with every δ_c > 0), and ς ∈ {1, −1} the sign there.

**Lemma {#lem:ii-d-2-1}** (One step with a characteristic cut-off.) Let (i)–(ii) of [[lem:ii-a1-4-1]] hold, and in place
of its (iii) the following: there are real scalar symbols j_ε, bounded in C^(M)_ν S̃^(2𝗌−m) and, for each ε, in
C^(M)_ν S̃^(2𝗌−m−2κ), supported in K_1, such that for every w ∈ H^(K′)_e3b carried by χ, with J_ε := Op(j_ε),

    ς⟨C_(ǎ_ε) w, w⟩ ≤ −‖B_ε w‖² + ‖E_ε w‖² + 2 Re⟨J_ε L w, w⟩
                       + C_0 (‖G′w‖²_(𝗌−½+δ_c) + ‖χw‖²_(−N′)).                                             {#eq:ii-d-2-1}

Then the conclusion [[eq:ii-a1-4-3]] of [[lem:ii-a1-4-1]] holds.

*Proof.* As for [[lem:ii-a1-4-1]], with two additions to the steps of that proof. In Step 1, for fixed ε, ⟨J_ε L w_t,
w_t⟩ → ⟨J_ε L v, v⟩ as t → 0: w_t → v in H^(𝗌−κ), so L w_t → L v in H^(𝗌−κ−m), and J_ε* w_t → J_ε* v in H^(−𝗌+m+κ), J_ε*
having order 2𝗌 − m − 2κ for this ε without loss ([[prop:ii-a1-2-4]] (a), (c)). In Step 2 the new term is bounded at v =
Φu: Lv = ΦLu + [L, Φ]u, and J_ε[L, Φ] has every order uniformly, by [[prop:ii-a1-2-4]] (e), as in Step 0; and |⟨ΦLu,
J_ε* v⟩| ≤ ‖ΦLu‖_(𝗌−m+1) ‖J_ε* v‖_(−𝗌+m−1). J_ε* is uniformly of order 2𝗌 − m + δ for every δ > 0 and microsupported in
K_1, so ‖J_ε* v‖_(−𝗌+m−1) ≤ C(‖Gu‖_(𝗌−1+δ) + ‖χu‖_(−N′)). With δ ≤ ½ and Step 0, 2|⟨J_ε L v, v⟩| ≤ C(‖GLu‖²_(𝗌−m+1) +
‖Gu‖²_(𝗌−½+δ_c) + ‖χu‖²_(−N′)), which is of the form of the right side of [[eq:ii-a1-4-3]]. ∎

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
(−1, 1), equal to 1 on [−½, ½], non-increasing on [0, ∞), with −ψψ′ the square of a smooth function on [0, ∞). Where
𝖧f > 0 on the support of ψ′(𝔐f) the term is −b′*b′; where 𝖧f < 0 it is +e*e, and its support determines E. A factor
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
at least the supremum of max spec(β_0⁻¹ p_(1,+)(0)) over ∂ℛ_+, with p_(1,+)(0) = ρ σ_1(Im_h P̂(0))). ∂R_(𝓗⁺) lies over K⁺ in {σ
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
∂K⁺; (3) B elliptic at ∂R_(∂K⁺,in); (4) the Schwartz kernel of E supported in (K ∖ K⁺)²; such that for all constants
s > s_0, α_+, α_K with

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
ψ(𝔐ρ_+) give −b′*b′ terms, and ψ(𝔐ρ_K) gives +e*e, supported in {ρ_K ≥ (2𝔐)⁻¹}, away from K⁺, as (4) requires; j_ε
= 0. The pattern gives [[eq:ii-d-3-4]]. ∎

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

### The estimate at the trapped set {#sec:ii-d-4}

*Setting.* Near the trapped set W′ = 1 ([[sec:ii-d-1-1]]). Over D = {t_* > T_♭, r_(Γ,−) < r < r_(Γ,+)} of
[[sec:ii-c1-3-2]] (T_♭ = 2/C′ there) the e3b-structure is spanned by ∂_(t_*) and ∂_x, and ᵉ³ᵇT*_D M = T*D with
covectors −σ dt_* + ζ. There ρ_K = t_*⁻¹, while x_I and ρ_+ are smooth and positive, so only the weight α_K enters, and
we write H^(𝗍,α_K) := H^(𝗍,(2α_I,α_+,α_K))_e3b. We work on ∂Σ⁺, near the trapped set Γ = Γ_1 ⊂ Σ^♭_1 of (H7) at z_0 =
1, where σ > 0. The slice coordinates (t_*, x, z), z = ζ/σ, of [[sec:ii-c1-3-2]] identify ᵉ³ᵇS*_D M ∩ {σ > 0} with (T_♭,
∞) × T*{r_(Γ,−) < r < r_(Γ,+)}, and ∂Γ_0 := {t_* > T_♭} × Γ. Put ρ := σ⁻¹ there, extended to a positive symbol of
degree −1 near fibre infinity ([[sec:ii-d-2]]). Then 𝖧 := ρH_G is the field Ŵ of [[eq:ii-c1-3-2]] with p = G, and ρ²G =
G(t_*, x; −dt_* + z). Three facts are used throughout.

(T1) 𝖧t_* ≥ ½β_Γ on a neighbourhood of ∂Γ_0 in the full phase space, for ε_P small (the paragraph after
[[lem:ii-c1-3-3]]), with β_Γ = ½ min_Γ |q_1| the constant of (Γ.4), not the horizon constant β_0. So 𝖧ρ_K = −ρ_K²
𝖧t_* < 0 there.

(T2) ρ⁻¹𝖧ρ = H_G(σ⁻¹) = −σ⁻² ∂_(t_*)G, as H_G σ = ∂_(t_*)G, σ being minus the momentum of t_*. It vanishes for P_0,
and for P it is O(ε_P ρ_K^(ℓ_K)) near ∂Γ_0, by the bounds on g⁻¹ − g_0⁻¹ before [[eq:ii-c1-3-1]].

(T3) Let h_Γ be a fibre inner product as in [[def:ii-c-2-1]] for z_0 = 1 (it exists by [[lem:ii-c-2-2]] (a)), extended
to be stationary and homogeneous of degree 0, and 𝔭′ := ρ σ_1(Im_(h_Γ) P). At ∂Γ_(K⁺), 𝔭′ = p_1(1), by
[[lem:ii-c-2-2]] (b), the coefficients of P − P_0 vanishing at K⁺. So ϑ_Γ := sup over ∂Γ_(K⁺) of max spec 𝔭′ satisfies
ϑ_Γ < ½ν_min.

**Lemma {#lem:ii-d-4-1}** (The hypersurfaces as defining functions.) Let d_0 ≥ 5, let ϕ^u, ϕ^s be the functions of
[[prop:ii-c1-3-4]] for the metric g of P, on the neighbourhood U of ∂Γ_0 there, let O be as in (H7) and O′ ⋐ O an open
neighbourhood of Γ. For δ > 0 let

    U(δ) := {ρ_K ≤ δ, |ϕ^u| ≤ δ, |ϕ^s| ≤ δ, |ρ²G| ≤ δ, (x, z) ∈ Ō′},

a subset of fibre infinity over {σ > 0}, closed in the compactified bundle, which includes ρ_K = 0. There is δ_U ∈ (0,
½C′), with C′ of [[lem:ii-c-3-2]], such that the following hold (ρ_K ≤ δ < ½C′ places U(δ) over {t_* > T_♭}, where
ϕ^(u/s) are defined, [[prop:ii-c1-3-4]]).

(a) For δ ≤ δ_U, U(δ) is a compact neighbourhood of ∂Γ_(K⁺), contained in {(x, z) ∈ O″} for an open O″ ⋐ O′
independent of δ, and ⋂_(δ>0) U(δ) = ∂Γ_(K⁺). Moreover Γ^u_(K⁺) ∩ U(δ_U) = U(δ_U) ∩ {ρ_K = 0, ϕ^u = 0, ρ²G = 0}.

(b) On a neighbourhood of U(δ_U) there are real functions w_u, r_u ∈ C^(d_0−3) and w_s, r_s ∈ C^(d_0−4), homogeneous of
degree 0, with bounded derivatives along ∂_(t_*), ∂_x and the fibres up to these orders, and continuous up to ρ_K = 0,
such that

    𝖧ϕ^u = −w_u ϕ^u + r_u ρ²G,       𝖧ϕ^s = w_s ϕ^s + r_s ρ²G.                                           {#eq:ii-d-4-1}

(c) w_u = ν_u and w_s = ν_s on ∂Γ_(K⁺), so w_(u/s) ≥ ν_min there.

(d) c_us := ρ⁻¹{ϕ^u, ϕ^s} is continuous up to ρ_K = 0, and on ∂Γ_(K⁺) it equals {ϕ_u, ϕ_s} > 0, the bracket of T*X̃°
in condition (Γ.3) of (H7).

*Proof.* At ρ_K = 0 every function involved is that of the stationary model: ϕ̃^(u/s) → 0 with their derivatives
([[prop:ii-c1-3-4]]); ρ²G − G_1 = g̃ = O(ε_P ρ_K^(ℓ_K)) with d_0 derivatives ([[eq:ii-c1-3-1]]); and ϕ_0^(u/s) =
ϕ_(u/s) ∘ π_Y is independent of t_* and equal to ϕ_(u/s) on Y = {G_1 = 0} ∩ O_0, π_Y being the projection along the
transversal field N_Y of [[sec:ii-c1-3-3]].

(a) On {G_1 = 0} ∩ O, ϕ_0^(u/s) = ϕ_(u/s), and Γ_u ∩ Γ_s = Γ by (Γ.1); so {ϕ_0^u = ϕ_0^s = G_1 = 0} ∩ Ō′ = Γ. By
compactness of Ō′ there are O″ ⋐ O′ and δ′ > 0 with {|ϕ_0^u|, |ϕ_0^s|, |G_1| ≤ 2δ′} ∩ Ō′ ⊂ O″, and these sets shrink to
Γ as δ′ → 0. For ρ_K ≤ δ the functions defining U(δ) differ from these by O(δ^(ℓ_K)). So for δ ≤ δ_U small, U(δ) ⊂
{(x, z) ∈ O″} and ⋂_δ U(δ) = {ρ_K = 0} × Γ = ∂Γ_(K⁺). U(δ) contains the set where the four inequalities are strict,
which is open and contains ∂Γ_(K⁺). The last assertion is [[prop:ii-c1-3-4]] with [[rem:s05-trapped-hypersurfaces]]
(b), as ∂Σ⁺ = {ρ²G = 0} near ∂Γ_0.

(b) dϕ_u, dϕ_s and dG_1 are linearly independent at Γ (the proof of [[lem:ii-c1-3-1]] (i)). On Y, d(ϕ_(u/s) ∘ π_Y) =
dϕ_(u/s) − (N_Y ϕ_(u/s)) dG_1, as d(ϕ ∘ π_Y) vanishes on N_Y and equals dϕ on TY = ker dG_1. So dϕ_0^u, dϕ_0^s, dG_1
are independent at Γ, hence near it, and together with dt_* near ∂Γ_0 for the stationary model. For ρ_K ≤ δ_U the
perturbations are O(δ_U^(ℓ_K)) in C¹, so the independence persists, with uniform bounds. Near each point of U(δ_U) we
can therefore complete y_1 := ϕ^u, y_2 := ρ²G by t_* and smooth t_*-independent functions y″ to coordinates of class
C^(d_0−1), with bounds uniform in t_*. f := 𝖧ϕ^u lies in C^(d_0−2), as 𝖧 has coefficients in C^(d_0−1), and f = 0 on
{y_1 = y_2 = 0}, as 𝖧 is tangent to Γ^u = ∂Σ⁺ ∩ U ∩ {ϕ^u = 0} ([[prop:ii-c1-3-4]]). Taylor's formula

    f(y) = Σ_(i=1,2) y_i ∫_0^1 (∂_(y_i) f)(τy_1, τy_2, y″) dτ,

in coordinate boxes convex in (y_1, y_2), gives f = −w_u y_1 + r_u y_2 locally with w_u, r_u ∈ C^(d_0−3), and a
partition of unity in (x, z), independent of t_*, patches them. The integral formula preserves the bounds along
∂_(t_*), ∂_x and the fibres, and the convergence as ρ_K → 0. For ϕ^s ∈ C^(d_0−2) the same argument loses one more
derivative.

(c) At ρ_K = 0, on {y_2 = 0} = {G_1 = 0}, 𝖧 = q_1 ∂_(t_*) + H_(G_1) ([[sec:ii-c1-3-2]], after [[lem:ii-c1-3-2]]) and
ϕ^u = ϕ_u, so f = H_(G_1) ϕ_u = −ν_u ϕ_u by (Γ.2). Thus w_u = ν_u on {y_2 = 0} where ϕ_u ≠ 0, hence on all of it by
continuity, as dϕ_u ≠ 0 there. Likewise w_s = ν_s.

(d) For functions F, F′ of (x, z) = (x, ζ/σ) alone, not depending on t_*, {F, F′} = σ⁻¹{F, F′}_(x,z), the terms with
t_* vanishing. ϕ^u and ϕ^s depend on t_* off ρ_K = 0, through ϕ̃^(u/s), and the formula is used only at ρ_K = 0, where
ϕ̃^(u/s) and its derivatives vanish; so there c_us = {ϕ_0^u, ϕ_0^s}_(x,z). At Γ, by the formula for d(ϕ ∘ π_Y), this is
{ϕ_u, ϕ_s} − (N_Y ϕ_s){ϕ_u, G_1} − (N_Y ϕ_u){G_1, ϕ_s}, and {ϕ_u, G_1} = −H_(G_1) ϕ_u = ν_u ϕ_u = 0, {G_1, ϕ_s} = ν_s
ϕ_s = 0 on Γ. Continuity up to ρ_K = 0 is as in (b). ∎

**Proposition {#prop:ii-d-4-2}** (The trapped set.) There are B, E, G ∈ C_b^∞Ψ^0_e3b such that (1) their operator wave
front sets lie in any fixed neighbourhood U_Γ of ∂Γ_(K⁺) in ᵉ³ᵇS*M; (2) their Schwartz kernels are supported in K × K
for any fixed compact neighbourhood K ⊂ M of the base projection of U_Γ; (3) B is elliptic at ∂Γ_(K⁺); (4) WF′(E) ∩
Γ^u_(K⁺) = ∅; and such that for all constants s > s_0 and α_K ∈ ℝ, and χ̃ ∈ C^∞(M) supported near K and equal to 1
near K,

    ‖Bu‖_(H^(s,α_K)) ≤ C (‖GPu‖_(H^(s,α_K)) + ‖Eu‖_(H^(s+1,α_K)) + ‖χ̃u‖_(H^(s_0,α_K)))                    {#eq:ii-d-4-2}

in the strong sense, for P = P_0 and every P with ε_P small, with d_0 depending only on s, s_0. Here ∂Γ_(K⁺) and
Γ^u_(K⁺) have one component over each of ∂Σ^±, and within Φ_1(O) ([[def:ii-b-2-2]]), which contains U_Γ when U_Γ is
small, Γ^u_(K⁺) is the global unstable set ∂Γ̄^u_(K⁺) ([[lem:ii-b-5-2]] (b)).

This is [Hin26c, Proposition 7.10] in dimension 4 + 1. Against [[prop:ii-d-3-1]]–[[prop:ii-d-3-6]] the estimate loses
one derivative: Pu is measured in H^s, not H^(s−1), and the a priori term in H^(s+1). The proof is the positive
commutator form of [[sec:i-b-6-4]], whose defect measures are replaced by commutators with a common regulariser: an
equation with damping for Φ_u u (Step 1, the counterpart of [[eq:i-b-6-8]]), a commutator with Φ_u that bounds u near
{ϕ^s = 0} by √δ (Step 2, the counterpart of [[eq:i-b-6-9]]), a propagation estimate with the weight |ϕ^s|^(−β) (Step
3, the counterpart of Step 3 of the proof in [[sec:i-b-6-4]]), and their combination, which closes because β < ½ (Step
4).

*Proof.* We prove the estimate at the component over ∂Σ⁺; over ∂Σ⁻ the proof is the same with z_0 = −1, ς = −1 and the
future field −𝖧 ([[sec:ii-d-3]]); c_us > 0 there too, as (Γ.3) holds for both z_0 = ±1. After Step 0 (a) norms are
those of H^𝗍_e3b without weights. C denotes constants independent of ε and, from Step 2 on, of δ; C_δ may depend on δ.
Neither depends on u.

*Step 0: reductions and choices.* (a) As in [[sec:ii-d-1-2]] with W′ = 1, w := ρ_K^(α_K) and A the frame of h_Γ, we
replace P by L″ = A⁻¹w⁻¹PwA and u by A⁻¹w⁻¹u, and keep the names P, u. The principal symbol is G, and by
[[eq:ii-d-1-1]] and (T1)

    𝔭 := ρ σ_1(Im P) = A⁻¹ (𝔭′ + α_K ρ_K 𝖧t_*) A,

as 𝖧 log w = α_K ρ_K⁻¹𝖧ρ_K = −α_K ρ_K 𝖧t_*. 𝔭 is Hermitian and continuous up to ρ_K = 0, and max spec 𝔭 ≤ ϑ_Γ on
∂Γ_(K⁺), since A⁻¹𝔭′A has the eigenvalues of the h_Γ-self-adjoint 𝔭′.

(b) Constants. Fix β < ½ with max(ϑ_Γ, 0) < βν_min, possible by (T3), and η_0 ∈ (0, ν_min/10] with c_0 := β(ν_min −
η_0) − ϑ_Γ − 2η_0 > 0. By [[lem:ii-d-4-1]], (T1)–(T2) and continuity there is δ_1 ∈ (0, δ_U] such that on U(δ_1): w_u,
w_s ≥ ν_min − η_0; max spec 𝔭 ≤ ϑ_Γ + η_0; c_us ≥ c_Γ := ½ min_Γ {ϕ_u, ϕ_s}; (T1) holds; and |2𝗍 − 1| |ρ⁻¹𝖧ρ| ≤ η_0
for all 𝗍 ∈ [s_0 − 3, s + 3]. Then on U(δ_1), for such 𝗍, as Hermitian matrices,

    (2𝗍 − 1)ρ⁻¹𝖧ρ − 2(𝔭 − w_u) ≥ ½ν_min,       (2𝗍 − 1)ρ⁻¹𝖧ρ − 2𝔭 + 2βw_s ≥ 2c_0:                      {#eq:ii-d-4-3}

the left side of the first is at least 2(ν_min − ϑ_Γ) − 5η_0 > ν_min − 5η_0, and that of the second at least 2(c_0 +
η_0) − η_0.

(c) Cut-offs and regulariser. ψ is the cut-off of the pattern (5) in [[sec:ii-d-3]], and θ := (−ψψ′)^(1/2) on [0, ∞),
extended evenly; so ψψ′(y) y = −θ(y)²|y|. All cut-offs below are functions of ϕ^u, ϕ^s, ρ²G, ρ_K on {(x, z) ∈ O′},
and their products are supported in some U(δ) with δ ≤ δ_1, hence in {(x, z) ∈ O″} by [[lem:ii-d-4-1]] (a); extended by
zero, they are symbols in C^(d_0−4) S̃^0, after multiplication by the function χ_∞ of the pattern (2), whose derivatives
are of order −∞ and are put into the remainders without comment. The regulariser is φ_ε of [[sec:ii-d-2]] with κ := 2,
and Λ_ε := ½(Op(φ_ε) + Op(φ_ε)*), bounded of order 0 uniformly and of order −2 for each ε. For a symbol x of order 𝗍,
Op(x)Λ_ε − Op(xφ_ε) is uniformly of order 𝗍 − 1 ([[prop:ii-a1-2-4]] (b)); this is used without comment.

(d) Half steps. Let J_0 := 5, the number of steps that [[lem:ii-a1-4-2]] takes for τ = 1 with κ ≤ ¼. For δ_2 ∈ (0,
2^(−J_0−6) δ_1], so that 2^(J_0+4) δ_2 ≤ δ_1/4, let 𝒜(δ_2) := U(2^(J_0+2) δ_2) ∩ ({|ϕ^u| ≥ δ_2/16} ∪ {ρ_K ≥
δ_2/16}), a closed set disjoint from Γ^u_(K⁺) by [[lem:ii-d-4-1]] (a). As U(δ) lies in the interior of U(2δ) for δ ≤
δ_U ([[lem:ii-d-4-1]] (a)), an operator elliptic on U(2^(J_0+3) δ_2) can be microsupported in U(2^(J_0+4) δ_2) ⊂
U(δ_1/4), and an operator microsupported in U(2^(J_0+3) δ_2) is microsupported in the interior of U(δ_1/2), where r^♭
of [[eq:ii-d-4-4]] vanishes. We show:

(★) Let s′ ∈ [s_0, s] and δ_2 be as above, G′ elliptic on U(2^(J_0+3) δ_2) and microsupported in U(δ_1/4), and E′
elliptic on 𝒜(δ_2) and microsupported in U(δ_1/4) ∩ ({|ϕ^u| ≥ δ_2/32} ∪ {ρ_K ≥ δ_2/32}). If G′u ∈ H^(s′−½), G′Pu ∈
H^(s′), E′u ∈ H^(s′+1) and χu ∈ H^(−N′), then B′u ∈ H^(s′) for every B′ microsupported in U(2δ_2), and

    ‖B′u‖_(s′) ≤ C𝒦,       𝒦 := ‖G′Pu‖_(s′) + ‖E′u‖_(s′+1) + ‖G′u‖_(s′−½) + ‖χu‖_(−N′).

[[prop:ii-d-4-2]] follows. Let 𝔫 := ⌈2(s − s_0)⌉ and s_j := s_0 + j(s − s_0)/𝔫, so s_j − s_(j−1) ≤ ½. Choose δ_2⁽¹⁾ ≤
2^(−J_0−6) δ_1 so small that U(2^(J_0+4) δ_2⁽¹⁾) ⊂ U_Γ, lies in the region where χ̃ = 1 and W′ = 1, and the kernels
are carried by χ in K × K; and δ_2⁽ʲ⁾ := 2^(−J_0−3) δ_2⁽ʲ⁻¹⁾, so that U(2^(J_0+4) δ_2⁽ʲ⁾) ⊂ U(2δ_2⁽ʲ⁻¹⁾). Step j of
(★), at the order s_j, is taken with G′ elliptic on U(2^(J_0+3) δ_2⁽ʲ⁾) and microsupported in U(2^(J_0+4) δ_2⁽ʲ⁾),
which lies in U(δ_1/4) as δ_2⁽ʲ⁾ ≤ 2^(−J_0−6) δ_1; it has its hypothesis G′u ∈ H^(s_j−½) from step j − 1 (from χ̃u ∈
H^(s_0) for j = 1), as s_j − ½ ≤ s_(j−1). Take B := B′ of step 𝔫, G elliptic on U(2^(J_0+4) δ_2⁽¹⁾) and
microsupported in U_Γ, and E elliptic on ⋃_j WF′(E′⁽ʲ⁾), a closed
set disjoint from Γ^u_(K⁺), with WF′(E) still disjoint from it. The norms of each step are bounded by the right side
of [[eq:ii-d-4-2]], with ‖χu‖_(−N′) ≤ C‖χ̃u‖_(s_0), and [[sec:ii-d-1-2]] returns the estimate to the weighted spaces.
The constants depend on P only through finitely many norms and the constants of (b) and of [[prop:ii-c1-3-4]], which
are uniform for ε_P small ([[rem:ii-d-1-3]]); d_0 is fixed by the regularity the symbol classes need at the orders in
[s_0 − 3, s + 3], plus 4 for [[lem:ii-d-4-1]].

It remains to prove (★). Fix s′, δ_2, G′, E′ and u as there.

*Step 1: the equation for Φ_u u.* Let χ_1 be a cut-off equal to 1 on U(δ_1/2) and supported in U(δ_1), and Φ_u :=
½(Op(χ_1ϕ^u) + Op(χ_1ϕ^u)*), scalar, self-adjoint and of order 0. Put W_u := Op(χ_1 w_u ρ⁻¹) and R_u := Op(χ_1 r_u ρ).
By [[prop:ii-a1-2-4]] (b), (d), (f), [P, Φ_u] has order 1 and principal symbol −iH_G(χ_1ϕ^u) = −iρ⁻¹𝖧(χ_1ϕ^u), the
commutator of the matrix-valued first-order part of P with the scalar Φ_u having order 0. By [[eq:ii-d-4-1]] this
equals the principal symbol of iW_uΦ_u − iR_uP on U(δ_1/2). Hence

    [P, Φ_u] = iW_uΦ_u − iR_uP + R_2 + R_2^♭,                                                              {#eq:ii-d-4-4}

with R_2 of order 0 and R_2^♭ = Op(r^♭), r^♭ ∈ C^(d_0−4) S̃^1 vanishing on U(δ_1/2). With f := Pu,

    P′Φ_u u = (Φ_u − iR_u) f + R_2 u + R_2^♭ u,       P′ := P − iW_u.                                      {#eq:ii-d-4-5}

P′ is P plus the quantisation of a first-order symbol (the remark after [[lem:ii-d-2-5]]), and ρ σ_1(Im P′) = 𝔭 −
χ_1w_u. So for P′ the quantity Q_ε of [[eq:ii-d-3-1]], with W′ = 1, w = 1, A = Id and 𝔭 for A⁻¹(⋯)A, is Q′_ε = (2𝗍_ε −
1)ρ⁻¹𝖧ρ − 2(𝔭 − w_u) ≥ ½ν_min on U(δ_1/2), for every order whose regularised values 𝗍_ε lie in [s_0 − 3, s + 3], by
[[eq:ii-d-4-3]]. There is no threshold: the damping W_u makes ∂Γ_(K⁺) behave for P′ like a radial set above threshold
at every order.

(1a) For ε′ ∈ (0, δ_1/2] let Ψ_(ε′) := ψ(ϕ^u/ε′) ψ(ϕ^s/ε′) ψ(ρ²G/ε′) ψ(ρ_K/ε′), supported in U(ε′) and equal to 1 on
U(ε′/2). We apply the pattern of [[sec:ii-d-3]] to P′ with ǎ := ρ^(−𝗍+½) Ψ_(ε′) at an order 𝗍. In 𝖧(Ψ_(ε′)²) the
factor in ϕ^u gives, by [[eq:ii-d-4-1]], 2θ(ϕ^u/ε′)² w_u |ϕ^u|/ε′ ≥ 0 times the squares of the other factors, plus a
multiple of ρ²G; it is a term +e*e, supported in {|ϕ^u| ≥ ε′/2}. The factor in ϕ^s gives −2θ(ϕ^s/ε′)² w_s |ϕ^s|/ε′
times the same, plus a multiple of ρ²G: a term −b′*b′. The factor in ρ²G gives a multiple of G, as 𝖧(ρ²G) =
2(ρ⁻¹𝖧ρ)ρ²G. The factor in ρ_K gives 2θ(ρ_K/ε′)²(−𝖧ρ_K)/ε′ times the same, ≥ 0 by (T1): a term +e*e, supported in {ρ_K
≥ ε′/2}. Multiples of G are j_ε ℓ. So [[eq:ii-d-2-2]] holds with b_ε := ρ^(−𝗍) φ_ε Ψ_(ε′) Q′_ε^(1/2) and E-symbols
supported in {|ϕ^u| ≥ ε′/2} ∪ {ρ_K ≥ ε′/2}. [[lem:ii-d-2-1]]–[[lem:ii-d-2-3]], and [[lem:ii-d-2-2]] with the interiors
of the sets U(2^(−j)·2^(J_0+2) δ_2), 0 ≤ j ≤ J_0, in the proof of [[lem:ii-a1-4-2]] (which needs open sets), and with
ε′ := 2^(J_0+3−j) δ_2 at its step j ≥ 1, so that the commutant is supported in the (j − 1)st set and equals 1 on the
jth while its E-sets, in {|ϕ^u| ≥ 4δ_2} ∪ {ρ_K ≥ 4δ_2}, miss U(2δ_2), give, in the strong sense,

    ‖B_1v‖_𝗍 ≤ C (‖G_1P′v‖_(𝗍−1) + ‖E_1v‖_𝗍 + ‖G_1v‖_(𝗍−1) + ‖χv‖_(−N′)),

with B_1 elliptic on U(2δ_2), G_1 elliptic on U(2^(J_0+2) δ_2) and microsupported in U(2^(J_0+3) δ_2), and E_1
microsupported in 𝒜(δ_2), where |ϕ^u| ≥ δ_2 or ρ_K ≥ δ_2 on the E-sets used. Apply this with v := Φ_u u and 𝗍 := s′ +
½. By [[eq:ii-d-4-5]], G_1R_2^♭ having every order, ‖G_1P′v‖_(s′−½) ≤ C(‖G′f‖_(s′) + ‖G′u‖_(s′−½) + ‖χu‖_(−N′));
‖G_1v‖_(s′−½) ≤ C(‖G′u‖_(s′−½) + ‖χu‖_(−N′)); and ‖E_1v‖_(s′+½) ≤ ‖Φ_uE_1u‖_(s′+½) + ‖[E_1, Φ_u]u‖_(s′+½) ≤
C(‖E′u‖_(s′+1) + ‖χu‖_(−N′)), the commutator having order −1 and E′ being elliptic on WF′(E_1). Hence

    ‖B_1Φ_u u‖_(s′+½) ≤ C𝒦.                                                                                {#eq:ii-d-4-6}

(1b) Now take ε′ := δ_2, Ψ := Ψ_(δ_2), 𝗍 := s′ + 1 and the regulariser: ǎ_ε := φ_ε ρ^(−s′−½) Ψ, b_ε := ρ^(−s′−1) φ_ε
Ψ Q′_ε^(1/2), B_ε := Op(b_ε). [[lem:ii-d-2-3]] gives [[eq:ii-d-2-1]] for P′ at the order s′ + 1. By [[eq:ii-d-4-6]] and
[[eq:ii-d-4-5]], G″v ∈ H^(s′+½) and G″P′v ∈ H^(s′−½) for G″ elliptic on U(δ_2) and microsupported in U(2δ_2). So
[[eq:ii-d-2-1]] holds at v = Φ_u u, by the approximation of Steps 1–2 of the proof of [[lem:ii-a1-4-1]] (for fixed ε
every operator in [[eq:ii-d-2-1]] has its order lowered by κ = 2), and the pairing identity at the end of
[[sec:ii-d-2]] applies. Thus

    ‖B_εv‖² ≤ 2|⟨Ǎ_εP′v, Ǎ_εv⟩| + ‖E_εv‖² + 2|⟨J_εP′v, v⟩| + C(‖G″v‖²_(s′+½) + ‖χv‖²_(−N′)).

We bound the terms. (i) As in (a) of Step 2 of the proof of [[lem:ii-a1-4-1]], ‖Ǎ_εv‖_(½) ≤ C‖B_εv‖ +
C‖G″v‖_(s′+½). (ii) Ǎ_ε − Op(ρ^(−s′−½)Ψ)Λ_ε is uniformly of order s′ − ½, so ‖Ǎ_εP′v‖_(−½) ≤ C(‖G″Λ_εP′v‖_(s′) +
‖G″P′v‖_(s′−1) + ‖χu‖_(−N′)). In [[eq:ii-d-4-5]], Λ_εR_2 = R_2Λ_ε + [Λ_ε, R_2] with the commutator uniformly of order
−1 ([[prop:ii-a1-2-4]] (d)), and G″R_2^♭ has every order. So

    ‖G″Λ_εP′v‖_(s′) ≤ C (‖G′f‖_(s′) + X_ε + ‖G′u‖_(s′−½) + ‖χu‖_(−N′)),       X_ε := ‖Op(ρ^(−s′) φ_ε g_0)u‖,

with g_0 a cut-off equal to 1 on U(2δ_2) and supported in U(4δ_2). (iii) ‖E_εv‖ ≤ C(‖E′u‖_(s′+1) + ‖χu‖_(−N′)) as in
(b) there, the E-symbols being supported in {|ϕ^u| ≥ δ_2/2} ∪ {ρ_K ≥ δ_2/2}, inside 𝒜(δ_2). (iv) J_ε is uniformly of
order 2s′, so |⟨J_εP′v, v⟩| ≤ C‖G″P′v‖_(s′−½) ‖G″v‖_(s′+½) + C‖χu‖²_(−N′) ≤ C𝒦² by [[eq:ii-d-4-6]]. (v) The last term
is at most C𝒦² by [[eq:ii-d-4-6]]. Absorbing ½‖B_εv‖², which is finite for ε > 0,

    ‖B_εΦ_u u‖ ≤ C (X_ε + 𝒦)     for all ε ∈ (0, 1].                                                       {#eq:ii-d-4-7}

*Step 2: concentration at {ϕ^s = 0}.* Let δ_4 := δ_2/4 and δ ∈ (0, δ_4/16], fixed in Step 4. Let Θ ∈ C^∞(ℝ) be
non-decreasing, with Θ = 0 on (−∞, −8], Θ = 1 on [8, ∞), Θ′ > 0 on (−8, 8), Θ(y) = c_1 e^(−1/(y+8)) near −8 and 1 −
Θ(y) = c_2 e^(−1/(8−y)) near 8. Such Θ exist for c_1 + c_2 < e: with T_∓ the two prescribed tails, put Θ′ := ϰ_−
T_−′ + m ϰ_0 + ϰ_+ T_+′ on (−8, 8), for a partition of unity ϰ_− + ϰ_0 + ϰ_+ = 1 there with ϰ_∓ = 1 near ∓8 and supported
within distance 1 of ∓8, and m > 0 fixed by ∫Θ′ = 1, possible as the two tail terms contribute at most (c_1 + c_2)e⁻¹
< 1; and Θ̌ := Θ^(1/2) and θ_Θ := Θ′^(1/2) are smooth. Let c_Θ := min_[−4,4] Θ′ > 0. Put

    ψ_δ(y) := Θ(y/δ) ψ(y/δ_4)²,       χ̄ := ψ(ϕ^u/δ_4) ψ(ρ²G/δ_4) ψ(ρ_K/δ_4),

ã := ρ^(−2s′−1) ψ_δ(ϕ^s) χ̄², Ã := ½(Op(ã) + Op(ã)*) and A_ε := Λ_ε Ã Λ_ε. ψ_δ(ϕ^s)χ̄ is supported in U(δ_4) ∩ {ϕ^s ≥
−8δ}, where χ_1 = 1 and Ψ = 1. As δ ≤ δ_4/16, ψ(y/δ_4) = 1 on supp Θ′(·/δ) ⊂ [−8δ, 8δ], and on supp ψ′(·/δ_4) ⊂ {½δ_4
≤ |y| ≤ δ_4}, Θ(y/δ) is 1 for y > 0 and 0 for y < 0. Hence

    ψ_δ′(y) = δ⁻¹ θ_Θ(y/δ)² − 2δ_4⁻¹ θ(y/δ_4)² 𝟙_(y>0).                                                    {#eq:ii-d-4-8}

*The identity.* For fixed ε, A_ε has order 2s′ − 3, so both sides of 2 Im⟨Φ_u u, A_ε u⟩ = ⟨i[Φ_u, A_ε]u, u⟩ are
continuous for u with G′u ∈ H^(s′−½) and χu ∈ H^(−N′), and the identity, which holds for smooth u as Φ_u and A_ε are
self-adjoint, holds at our u. By [[prop:ii-a1-2-4]] (b), (d), i[Φ_u, A_ε] = Op(H_(ϕ^u)(φ_ε² ã)) + R_(ε,δ), with
R_(ε,δ) uniformly of order 2s′ − 1. By [[eq:ii-a1-2-1]] with V = H_(ϕ^u), by H_(ϕ^u)ϕ^u = 0 and by [[eq:ii-d-4-8]],
near fibre infinity,

    H_(ϕ^u)(φ_ε² ã) = ρ^(−2s′) φ_ε² (δ⁻¹ θ_Θ(ϕ^s/δ)² c_us χ̄² + ψ_δ(ϕ^s) k_ε)
                      + ρ^(−2s′) φ_ε² (−2δ_4⁻¹ θ(ϕ^s/δ_4)² 𝟙_(ϕ^s>0) c_us χ̄²),                            {#eq:ii-d-4-9}

with k_ε := ρ⁻¹H_(ϕ^u)(χ̄²) − (2s′ + 1 − 2κθ_ε)(ρ⁻²H_(ϕ^u)ρ) χ̄². k_ε is bounded with its derivatives independently
of ε and δ, ρ⁻²H_(ϕ^u)ρ being homogeneous of degree 0; in ρ⁻¹H_(ϕ^u)(χ̄²) only the factors in ρ²G and ρ_K are
differentiated. Let

    B_δ^ε := Op(ρ^(−s′) φ_ε θ_Θ(ϕ^s/δ) c_us^(1/2) χ̄),
    E_2^ε := Op(ρ^(−s′) φ_ε θ(ϕ^s/δ_4) 𝟙_(ϕ^s>0) c_us^(1/2) χ̄),
    Z^ε := Op(ρ^(−s′) φ_ε Θ̌(ϕ^s/δ) ψ(ϕ^s/δ_4) g_1),

with g_1 a cut-off equal to 1 on supp χ̄, supported in {|ϕ^u|, |ρ²G|, ρ_K ≤ 2δ_4}. Quantising [[eq:ii-d-4-9]] by
[[prop:ii-a1-2-4]] (b), (c), with ψ_δ k_ε = (Θ̌ψ)² g_1 k_ε g_1,

    δ⁻¹‖B_δ^ε u‖² = 2 Im⟨Φ_u u, A_ε u⟩ + 2δ_4⁻¹‖E_2^ε u‖² − ⟨Op(k_ε)Z^ε u, Z^ε u⟩ + O(C_δ𝒦²),            {#eq:ii-d-4-10}

the remainders being uniformly of order 2s′ − 1 and so bounded by C_δ(‖G′u‖²_(s′−½) + ‖χu‖²_(−N′)).

*The pairing.* Ã = Op(ρ^(−s′−1) Θ̌ψχ̄)* Op(ρ^(−s′) Θ̌ψχ̄) + R, with R of order 2s′ (here Θ̌ψ is evaluated at ϕ^s, with
the arguments of the definition). As Λ_ε is self-adjoint, ⟨Φ_u u, A_ε u⟩ = ⟨Λ_εΦ_u u, ÃΛ_ε u⟩, and |⟨Λ_εΦ_u u,
RΛ_ε u⟩| ≤ C_δ‖G″Φ_u u‖_(s′+½) ‖G′u‖_(s′−½) + C‖χu‖²_(−N′) ≤ C_δ𝒦² by [[eq:ii-d-4-6]]. So

    2|⟨Φ_u u, A_ε u⟩| ≤ 2‖Op(ρ^(−s′−1) φ_ε Θ̌ψχ̄) Φ_u u‖ ‖Op(ρ^(−s′) φ_ε Θ̌ψχ̄) u‖ + C_δ𝒦².

On the support of Θ̌ψχ̄, Ψ = 1 and Q′_ε ≥ ½ν_min, so [[lem:ii-d-2-5]] with [[eq:ii-d-4-6]] and [[eq:ii-d-4-7]] bounds
the first factor by C‖B_εΦ_u u‖ + C_δ𝒦 ≤ C(X_ε + 𝒦) + C_δ𝒦, and, with q_1 := χ̄, it bounds the second by 2‖Z^ε u‖ +
C_δ𝒦. The product of the two bounds is at most C(X_ε + 𝒦)‖Z^ε u‖ + C_δ𝒦X_ε + C_δ𝒦‖Z^ε u‖ + C_δ𝒦², and
δC_δ𝒦‖Z^ε u‖ ≤ δ‖Z^ε u‖² + C_δ𝒦². [[eq:ii-d-2-3]] gives |⟨Op(k_ε)Z^ε u, Z^ε u⟩| ≤ C‖Z^ε u‖² + C_δ𝒦². With
[[eq:ii-d-4-10]], multiplied by δ ≤ 1,

    ‖B_δ^ε u‖² ≤ Cδ ((X_ε + 𝒦)‖Z^ε u‖ + ‖E_2^ε u‖² + ‖Z^ε u‖²) + C_δ𝒦X_ε + C_δ𝒦².                         {#eq:ii-d-4-11}

This is the commutator form of [[eq:i-b-6-9]]: u is small near {ϕ^s = 0}, by the factor √δ, because Φ_u u is one
order smoother than u (Step 1) and H_(ϕ^u) crosses {ϕ^s = 0} transversally, at the rate c_us.

*Step 3: propagation away from {ϕ^s = 0}.* Let R_3 := δ_3 := 16δ_2, and for t ≥ 0 let F(t) := Υ(t/δ) ψ(t/R_3) with
Υ(τ) := Θ(32τ − 24): Υ = 0 on [0, ½], Υ = 1 on [1, ∞), and ΥΥ′ = 32(Θ̌θ_Θ)²(32τ − 24). Let χ̄_3 := ψ(ϕ^u/δ_3)
ψ(ρ²G/δ_3) ψ(ρ_K/δ_3) and ǎ := ρ^(−s′+½) Ψ_3, Ψ_3 := |ϕ^s|^(−β) F(|ϕ^s|) χ̄_3, which is smooth because F(|ϕ^s|)
vanishes for |ϕ^s| ≤ δ/2. We apply the pattern [[eq:ii-d-3-1]] to P at the order s′, with W′ = 1, w = 1, A = Id, so
Q_ε = (2s′_ε − 1)ρ⁻¹𝖧ρ − 2𝔭. By [[eq:ii-d-4-1]], off {ϕ^s = 0}, 𝖧(|ϕ^s|^(−2β)) = −2β|ϕ^s|^(−2β)(w_s + r_s ρ²G/ϕ^s)
and 𝖧(F(|ϕ^s|)²) = 2FF′(|ϕ^s|)(|ϕ^s| w_s + sgn(ϕ^s) r_s ρ²G). As δ < R_3/2, ψ(·/R_3) = 1 on supp Υ′(·/δ) ⊂ [δ/2,
δ], and Υ(·/δ) = 1 on supp ψ′(·/R_3); so 2FF′(t) t w_s = e_3(t)² − b_3(t)² with

    e_3(t)² := 64 (t/δ) (Θ̌θ_Θ)²(32t/δ − 24) w_s,       b_3(t)² := 2 (t/R_3) θ(t/R_3)² w_s.

Hence

    −Ψ_3² Q_ε + 𝖧(Ψ_3²) = −Ψ_3² (Q_ε + 2βw_s) + χ̄_3² |ϕ^s|^(−2β) (e_3² − b_3²)(|ϕ^s|)
                           + F² |ϕ^s|^(−2β) 𝖧(χ̄_3²) + j ρ²G,

with j smooth, and Q_ε + 2βw_s ≥ 2c_0 on the support by [[eq:ii-d-4-3]]. In 𝖧(χ̄_3²), as in Step 1, the factor in ϕ^u
gives a nonnegative square supported in {|ϕ^u| ≥ δ_3/2} plus a multiple of ρ²G, the factor in ρ_K a nonnegative square
supported in {ρ_K ≥ δ_3/2}, and the factor in ρ²G a multiple of G. So [[eq:ii-d-2-2]] holds with b_ε := ρ^(−s′) φ_ε
Ψ_3 (Q_ε + 2βw_s)^(1/2), one b′-term ρ^(−s′) φ_ε |ϕ^s|^(−β) χ̄_3 b_3(|ϕ^s|), the e-term ρ^(−s′) φ_ε |ϕ^s|^(−β) χ̄_3
e_3(|ϕ^s|), e-terms supported in {|ϕ^u| ≥ δ_3/2} ∪ {ρ_K ≥ δ_3/2}, and j_ε collecting the multiples of G. By
[[lem:ii-d-2-3]], [[eq:ii-d-2-1]] holds, and it holds at u by the approximation of Step 1, as G′u ∈ H^(s′−½) and G′Pu ∈
H^(s′). In it, Ǎ_ε is uniformly of order s′ − ½, so 2|⟨Ǎ_εPu, Ǎ_εu⟩| ≤ 2‖Ǎ_εPu‖_(½) ‖Ǎ_εu‖_(−½) ≤
C_δ(‖G′Pu‖_(s′) ‖G′u‖_(s′−1) + ‖χu‖²_(−N′)). This is where Pu ∈ H^(s′), one order more than real principal type needs,
is used. |⟨J_εPu, u⟩| ≤ C_δ𝒦², as J_ε is uniformly of order 2s′ − 2. The e-terms in {|ϕ^u| ≥ δ_3/2} ∪ {ρ_K ≥ δ_3/2}
lie in 𝒜(δ_2) and are at most C_δ(‖E′u‖_(s′) + ‖χu‖_(−N′)). So, with B_3^ε := Op(b_ε) and E_3^ε := Op(ρ^(−s′) φ_ε
|ϕ^s|^(−β) χ̄_3 e_3(|ϕ^s|)),

    ‖B_3^ε u‖² ≤ ‖E_3^ε u‖² + C_δ𝒦².                                                                      {#eq:ii-d-4-12}

Let M^ε := Op(ρ^(−s′) φ_ε F(|ϕ^s|) χ̄_3). After the factor ρ^(−s′) φ_ε its symbol is z := F(|ϕ^s|) χ̄_3, and that of
B_3^ε is x_1 := Ψ_3 (Q_ε + 2βw_s)^(1/2). Let ζ be a cut-off equal to 1 near supp z and supported in {δ/4 < |ϕ^s| <
2R_3} and in a neighbourhood of supp χ̄_3 ∩ {|ϕ^s| ≤ 2R_3} inside the interior of U(δ_1), where [[eq:ii-d-4-3]] holds,
so that Q_ε + 2βw_s ≥ c_0 on supp ζ, and q_1 := ζ |ϕ^s|^β (Q_ε + 2βw_s)^(−1/2). Then z = q_1 x_1 near supp z, and
sup|q_1| ≤ (2R_3)^β c_0^(−1/2), independently of δ and ε; so [[lem:ii-d-2-5]] in its general form gives ‖M^ε u‖ ≤
CR_3^β ‖B_3^ε u‖ + C_δ𝒦, δ entering through the derivatives of |ϕ^s|^β near |ϕ^s| = δ/4. Its particular case does not
apply, as x_1 vanishes where z does. The symbol of E_3^ε is supported in {δ/2 ≤ |ϕ^s| ≤ δ} ∩ supp χ̄_3, where
|ϕ^s|^(−β) e_3 ≤ Cδ^(−β): the propagation runs from the shell |ϕ^s| ∼ δ outward, along which |ϕ^s| grows, and the
weight |ϕ^s|^(−β) costs δ^(−β).

*Step 4: conclusion.* Put 𝒩_ε := ‖B_δ^ε u‖ + ‖M^ε u‖, finite for each ε > 0, as for fixed ε these operators have
order s′ − 2. The symbol of B_δ^ε is at least (c_Θ c_Γ)^(1/2) ρ^(−s′) φ_ε on 𝒰_B := {|ϕ^s| ≤ 4δ, |ϕ^u|, |ρ²G|, ρ_K ≤
δ_4/2}, and that of M^ε equals ρ^(−s′) φ_ε on 𝒰_M := {δ ≤ |ϕ^s| ≤ 8δ_2, |ϕ^u|, |ρ²G|, ρ_K ≤ 8δ_2}. E′ is elliptic on
𝒜(δ_2), which contains U(16δ_2) ∩ ({|ϕ^u| ≥ δ_4/4} ∪ {ρ_K ≥ δ_4/4}), and P is elliptic on {|ρ²G| ≥ δ_4/4}. A point of
U(16δ_2) with |ϕ^s| ≥ δ and |ϕ^s|, |ϕ^u|, |ρ²G|, ρ_K ≤ 8δ_2 lies in 𝒰_M; one with |ϕ^s| < 2δ lies in 𝒰_B or has one
of |ϕ^u|, ρ_K, |ρ²G| above δ_4/2. So these four sets cover, with room, U(8δ_2) and U(16δ_2) ∩ {|ϕ^s| ≤ δ}, and on each
the corresponding symbol is bounded below independently of δ. [[lem:ii-d-2-5]], with the elliptic estimates
‖Op(ρ^(−s′) φ_ε e′)u‖ ≤ C(‖E′u‖_(s′) + ‖χu‖_(−N′)) for e′ supported in Ell(E′), and ‖Op(ρ^(−s′) φ_ε e″)u‖ ≤
C(‖G′Pu‖_(s′−2) + ‖G′u‖_(s′−1) + ‖χu‖_(−N′)) for e″ supported in Ell(P) ([[thm:ii-a1-3-1]] for Λ_ε u, [P, Λ_ε] being
uniformly of order 1), gives

    ‖Op(ρ^(−s′) φ_ε z)u‖ ≤ C(𝒩_ε + 𝒦) + C_δ𝒦                                                              {#eq:ii-d-4-13}

for every symbol z with |z| ≤ 1 supported in U(4δ_2), with C independent of δ; and, for z supported in U(16δ_2) ∩
{|ϕ^s| ≤ δ}, which needs only 𝒰_B and the last two sets, the same with ‖B_δ^ε u‖ in place of 𝒩_ε. The first form
applies to X_ε, to Z^ε and to E_2^ε (supported in U(δ_2/2)), the second to δ^β E_3^ε. So X_ε, ‖Z^ε u‖ and
‖E_2^ε u‖ are at most C(𝒩_ε + 𝒦) + C_δ𝒦. In [[eq:ii-d-4-11]] the term with the factor Cδ is then at most Cδ(𝒩_ε +
𝒦)² + C_δ𝒦², and, by Young's inequality, C_δ𝒦X_ε ≤ C_δ𝒦 · C(𝒩_ε + 𝒦) + C_δ𝒦² ≤ δ(𝒩_ε + 𝒦)² + C_δ𝒦². Taking the
square root, ‖B_δ^ε u‖ ≤ Cδ^(1/2)(𝒩_ε + 𝒦) + C_δ𝒦. By the second form, ‖E_3^ε u‖ ≤ Cδ^(−β)(‖B_δ^ε u‖ + 𝒦) + C_δ𝒦, so by Step 3
and [[eq:ii-d-4-12]], ‖M^ε u‖ ≤ CR_3^β ‖B_3^ε u‖ + C_δ𝒦 ≤ CR_3^β δ^(−β) ‖B_δ^ε u‖ + C_δ𝒦. Together,

    𝒩_ε ≤ C_9 (δ^(1/2) + R_3^β δ^(1/2−β)) (𝒩_ε + 𝒦) + C_δ𝒦,

with C_9 independent of δ and ε. Since β < ½, we can fix δ ∈ (0, δ_4/16] with C_9(δ^(1/2) + R_3^β δ^(1/2−β)) ≤ ½,
and then 𝒩_ε ≤ C𝒦 for all ε ∈ (0, 1]. By [[eq:ii-d-4-13]] with z = g_0, X_ε ≤ C𝒦 for all ε. As in Step 3 of the
proof of [[lem:ii-a1-4-1]], Op(ρ^(−s′) φ_ε g_0)u → Op(ρ^(−s′) g_0)u in 𝒟′ while staying bounded in L², so
Op(ρ^(−s′) g_0)u ∈ L² with norm at most C𝒦. g_0 = 1 on U(2δ_2), so the elliptic estimate gives (★) for B′
microsupported in U(2δ_2). ∎

The constant ϑ_Γ < ½ν_min enters twice, as in [[sec:i-b-6-4]]: in Step 1, through ν_min − ϑ_Γ > 0, and in Step 4,
through β < ½ with βν_min > ϑ_Γ, which is what lets the loss δ^(−β) of Step 3 be paid by the gain δ^(1/2) of Step 2.

### Proof of the global estimate {#sec:ii-d-5}

*Proof of [[thm:ii-d-1-2]].* Let u be as in [[thm:ii-d-1-2]] with the right side of [[eq:ii-d-1-4]] finite, and write
ℛ for that right side. Extended by zero, u and Pu are supported in {t_*^♭ ≥ 1} ([[sec:ii-d-1-1]]). Below, ‖·‖_𝗍 is the
norm of H^(𝗍,(2α_I,α_+,α_K))_e3b, and Pu is measured in H^(𝗍,(2α_I+2,α_++2,α_K))_e3b, which is the measure of Lu =
W⁻¹Pu in H^𝗍 with the weights of u ([[sec:ii-d-1-1]]). We say u is *controlled at order* 𝗍 on an open set V ⊂ ᵉ³ᵇS*M
if ‖Bu‖_𝗍 ≤ Cℛ, in the strong sense, for every B ∈ C_b^∞Ψ^0_e3b carried by χ with WF′(B) ⊂ V. Off the characteristic
set u is controlled at every order up to 𝗌 + 1 ([[thm:ii-a1-3-1]]), so only ∂Σ^± matter. We treat ∂Σ⁺; on ∂Σ⁻ the
future field is −𝖧, and the same steps apply to the antipodal images of the sets below, for which [[sec:ii-d-3]] and
[[sec:ii-d-4]] prove the same estimates.

Three facts are used throughout. (P1) *Propagation.* [[thm:ii-a1-5-4]], for L and with the weights put into the
operator as in [[sec:ii-d-1-2]]: control at order 𝗍 on an open set V gives control at order 𝗍 at every ϖ whose
backward 𝖧-curve enters V in finite time, provided 𝖧𝗍 ≤ 0 along it and Pu is in H^(𝗍−1) near it; for a compact set of
such ϖ the entrance times are bounded, the flow being continuous on the compactified bundle. The orders 𝗌 and 𝗌 + 1
are non-increasing along the future flow on ∂Σ⁺ for P ([[prop:ii-c-5-1]] (2)). (P2) *Initial surface.* As u = 0 in
{t_*^♭ < 1}, u is controlled at every order there. (P3) *Dynamics.* Over M° every backward curve in ∂Σ⁺ reaches {t_*^♭
= 1} at a finite parameter ([[prop:ii-c-4-2]]); over ∂M the curves are those of P_0 ([[lem:ii-c-4-1]]), described by
[[prop:ii-b-8-1]], whose table we use with its notation R_𝓗, R^I_in, R^K_in, Γ_K, R^K_out, R^I_out.

*Step 1: finite times.* Let t^♯ ∈ (1, ∞) and 𝒱_out a neighbourhood of ∂R_(ℐ⁺,out). Then u is controlled at order 𝗌 + 1
on a neighbourhood of every compact subset of ∂Σ⁺ over Ω_* ∩ {t_*^♭ ≤ t^♯} disjoint from 𝒱_out, with C depending on
t^♯ and 𝒱_out. Indeed, a point over M° has its backward curve reach {t_*^♭ < 1} by (P3). A point over ℐ⁺ at finite t_*,
not in ∂R_(ℐ⁺,out), lies on a curve of the first row of the table, which reaches {t_* = 1} backward, and t_*^♭ = t_*
there ([[lem:ii-c-3-2]] (a)). (P1) at order 𝗌 + 1, with Pu ∈ H^𝗌, and (P2) give the claim. Points of ∂R_(ℐ⁺,out) are
fixed by the flow and are left to Step 6. ([Hin26c] propagates into them already here, by its Proposition 7.9 with
finite t_(*,+); see [[sec:s06-remarks]].)

*Step 2: the horizon and ∂R_(ℐ⁺,in,+).* [[prop:ii-d-3-1]] with the orders (𝗌 + 1, 𝗌_0), which are constant near
∂R_(𝓗⁺), with 𝗌_0 > ½ + ϑ_𝓗 as 𝗌_0 is admissible ([[def:ii-c-2-4]] (4)), and [[prop:ii-d-3-5]] with the same orders,
whose condition [[eq:ii-d-3-7]] is [[eq:ii-d-1-3]], have their E supported at finite times: in {ρ_K ≥ (2𝔐)⁻¹}, resp.
{ρ_+ ≥ (2𝔐)⁻¹}. The E of [[prop:ii-d-3-5]] is microsupported near ξ̂ = 2, so away from ∂R_(ℐ⁺,out) = {ξ̂ = 0}, and that
of [[prop:ii-d-3-1]] lies over a neighbourhood of the horizon, away from ℐ⁺. So Step 1, with t^♯ large and 𝒱_out small,
bounds ‖Eu‖_(𝗌+1), and u is controlled at order 𝗌 + 1 on neighbourhoods V_𝓗 of ∂R_(𝓗⁺) and V_I of ∂R_(ℐ⁺,in,+).

*Step 3: ∂R_(∂K⁺,in).* [[prop:ii-d-3-2]] with the orders (𝗌 + 1, 𝗌_0), where [[eq:ii-d-3-3]] holds as 𝗌_0 is
admissible ([[def:ii-c-2-4]] (6)). Its E has kernel supported away from K⁺, near ∂K⁺, and is microsupported in a small
neighbourhood of ∂R_(∂K⁺,in) where ρ_K⁻¹𝖧ρ_K ≤ −1. Let ϖ ∈ WF′(E) ∩ ∂Σ⁺. Over M°, its backward curve reaches {t_*^♭ <
1} (P3). Over (ι⁺)°, ρ_K increases backward from ϖ, and it keeps increasing: a backward critical point of ρ_K with
ρ_K > 0 would be a local maximum along the curve, against 𝖧²ρ_K > 0 there ([[lem:ii-b-3-3]] (3)). So the curve does not
tend to R^K_out backward, where ρ_K = 0, and by the table over (ι⁺)° it tends to R^I_in, entering V_I. Points over ℐ⁺
do not occur, ∂K⁺ being away from ℐ⁺. (P1) at order 𝗌 + 1 from V_I and (P2) bound ‖Eu‖_(𝗌+1), and u is controlled at
order 𝗌 + 1 on a neighbourhood V_K of ∂R_(∂K⁺,in).

*Step 4: the trapped set.* [[prop:ii-d-4-2]] with the orders (𝗌, 𝗌_0), constant over {r ≤ r_Γ} ([[def:ii-c-2-4]]
(3)), with U_Γ ⊂ Φ_1(O) small and Pu ∈ H^𝗌. Let ϖ ∈ WF′(E) ∩ ∂Σ⁺. Over M°, its backward curve reaches {t_*^♭ < 1}.
Over (K⁺)°, ϖ ∉ Γ^u_(K⁺), so ϖ is not in the global unstable set ∂Γ̄^u_(K⁺), as ∂Γ̄^u_(K⁺) ∩ Φ_1(O) = Γ^u_(K⁺)
([[lem:ii-b-5-2]] (b), from the no-return condition (H8) (b)); by [[prop:ii-b-6-1]] (2) its curve tends backward to
∂R_(𝓗⁺) or ∂R_(∂K⁺,in), entering V_𝓗 ∪ V_K. As WF′(E) is compact and the entrance times are locally bounded, (P1) at
order 𝗌 + 1 and (P2) bound ‖Eu‖_(𝗌+1). So u is controlled at order 𝗌 on a neighbourhood V_Γ of ∂Γ_(K⁺). This is the
step that needs Pu in H^𝗌, and the reason Steps 1–3 work at the order 𝗌 + 1.

*Step 5: ∂R_(∂K⁺,out).* [[prop:ii-d-3-3]] with the orders (𝗌, 𝗌_0), with [[eq:ii-d-3-5]] from [[def:ii-c-2-4]] (5),
at the order 𝗌 itself, the threshold being an upper bound. Its E is microsupported near ∂R_(∂K⁺,out) with WF′(E) ∩
∂W_out = ∅. Let ϖ ∈ WF′(E) ∩ ∂Σ⁺. Over ∂K⁺ its curve is of type (R^K_in, R^K_out) and enters V_K backward. Over (K⁺)°,
of type (A, R^K_out) with A ∈ {R_𝓗, R^K_in, Γ_K}, it enters V_𝓗 ∪ V_K ∪ V_Γ. Over (ι⁺)°, A ≠ R^K_out as ϖ ∉ ∂W_out,
the unstable manifold of ∂R_(∂K⁺,out) over ι⁺ ([[lem:ii-b-3-3]] (4)), so by the table A = R^I_in, and the curve enters
V_I. Over M°, it reaches {t_*^♭ < 1}. (P1) at order 𝗌 bounds ‖Eu‖_𝗌, and u is controlled at order 𝗌 on a neighbourhood
V_(K,out) of ∂R_(∂K⁺,out).

*Step 6: ∂R_(ℐ⁺,out).* [[prop:ii-d-3-6]] with t_(*,−) := ½, the orders (𝗌, 𝗌_0), constant near ∂R_(ℐ⁺,out)
([[prop:ii-c-5-1]] (5)), and [[eq:ii-d-3-9]] from [[eq:ii-d-1-3]]. Its B is elliptic on ∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥ ½},
which contains all of it over Ω_*. The part of E from the cut-off ψ_− has kernel in {t_*^♭ < 1}², where u = 0 (the
paragraph after [[prop:ii-d-3-6]]). The rest of E is microsupported in a punctured neighbourhood of ∂R_(ℐ⁺,out). Let ϖ
be a point of it in ∂Σ⁺. Over (ℐ⁺)°, its curve reaches {t_* = 1} backward (first row of the table). Over ℐ⁺ ∩ ι⁺ it is
of type (R^I_in, R^I_out), and over (ι⁺)° of type (R^I_in, ·) or (R^K_out, R^I_out); it enters V_I ∪ V_(K,out). Over
M°, it reaches {t_*^♭ < 1}. (P1) at order 𝗌 bounds ‖Eu‖_𝗌, and u is controlled at order 𝗌 on a neighbourhood V_(I,out)
of ∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥ ½}.

*Conclusion.* Let ϖ ∈ ∂Σ⁺ over supp χ. If ϖ lies over M° or over ℐ⁺ at finite t_*, it is controlled at order 𝗌 by Step
1 when ϖ ∉ 𝒱_out, with t^♯ > t_*^♭(ϖ), and by Step 6 when ϖ ∈ V_(I,out), choosing 𝒱_out inside V_(I,out). If ϖ lies
over K⁺ ∪ ι⁺, it lies in one of the sets of Steps 2–6 or on a curve of the table, whose backward end A is {t_* = 1} or
one of R_𝓗, R^I_in, R^K_in, Γ_K, R^K_out, each of which has a controlled neighbourhood. This includes the curves inside
the black hole, from ∂R_(𝓗⁺) to {r < r_0 − δ_0} ([[prop:ii-b-6-1]]), which reach supp χ ⊂ {r ≥ r_1}; (P1) at order 𝗌
applies. By compactness of the cosphere bundle over supp χ, finitely many such B, with elliptic estimates off Σ, are
jointly elliptic there, and the elliptic estimate ([[lem:ii-a-8-4]] (c)), with the a priori term ‖χu‖_(−N′) ≤
‖u‖_(𝗌_0), gives [[eq:ii-d-1-4]], in the strong sense since every step propagates regularity.

*Uniformity.* Each estimate used holds uniformly for P with ε_P small ([[prop:ii-d-3-1]]–[[prop:ii-d-3-6]],
[[prop:ii-d-4-2]], [[thm:ii-a1-3-1]] and [[thm:ii-a1-5-4]]). The flow of P agrees with that of P_0 over ∂M, and over
M° it differs by O(ε_P) in C¹ ([[lem:ii-c-4-1]] (a)), so the finitely many backward segments used above, which enter
open sets in bounded times, have nearby segments for P with the same properties. d_0 is the largest of those required
by the steps, at the orders 𝗌_0, 𝗌 and 𝗌 + 1. With [[rem:ii-d-1-3]] this proves [[thm:ii-d-1-2]]. ∎

### Regularity with b-derivatives: the setting {#sec:ii-d1-1}

b-regularity is tested by commuting b-vector fields through P. For the elliptic and real principal type estimates,
[[sec:ii-a-9]] commutes a spanning set of b-vector fields; the commutators enter the commuted system below principal
order, where those estimates do not see them. At a radial set or at the trapped set the subprincipal symbol of the
commuted system enters the threshold. There one uses families of commutator fields whose commutators with P either
decay at the face carrying the set, or contribute with the favourable sign, so that the commuted system has the
threshold of P. [[sec:ii-d1-2]] writes the commuted system for an arbitrary family and proves, once, that the estimate
for it gives the estimate with b-regularity, and its tame version ([[lem:ii-d1-2-3]], [[lem:ii-d1-2-4]]). The estimates
of [[sec:ii-d-3]] and [[sec:ii-d-4]] hold for the commuted systems ([[lem:ii-d1-2-5]]). [[sec:ii-d1-3]]–[[sec:ii-d1-6]]
supply the families: near ℐ⁺, at the horizon, over ∂K⁺ and at the trapped set. [[sec:ii-d1-7]] proves the global
estimate. This is [Hin26c, Section 7.2] in dimension 4 + 1.

The setting is that of [[sec:ii-d-1]], now with k degrees of b-regularity. P is a weakly admissible wave-type operator
relative to P_0 of class ((d_0; k), (2ℓ_I, ℓ_+, ℓ_K)) ([[def:ii-c-3-3]]), with ℓ_I ∈ (0, ½], ℓ_+, ℓ_K > 0, and ε_(P,k)
:= ‖P − P_0‖_((d_0;k),(2ℓ_I,ℓ_+,ℓ_K)) ([[def:ii-c-3-6]]). The bundle E is the trivial bundle ℂ^(N_E)
([[sec:ii-c-1-1]]), and b-vector fields act on its sections componentwise, so no connection is needed. As in
[[sec:ii-d-1-1]], "of class" means conditions (1)–(2) of [[def:ii-c-3-3]]; condition (3) is not used here either: the
proofs below use p_1 and p_0 only through [[lem:ii-c-3-4]] and the thresholds of [[sec:ii-d-3]].
H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b) are the mixed spaces of [[eq:ii-a-8-1]], with their supported and extendible versions
as in [[sec:ii-a-7]], and ‖·‖_(𝗌;k) their norms, weights suppressed where they are fixed. D^j_b is the schematic
notation of [[sec:ii-a-9-3]]. Weights do not interfere with commutators: for a b-vector field V and a weight w (a
product of powers of boundary defining functions), w⁻¹Vw = V + (V log w) with V log w smooth. Two facts are used
throughout.

(F1) ‖v‖_(𝗍+1;k−1) ≤ C‖v‖_(𝗍;k), and microlocally ‖Gv‖_(𝗍+1;k−1) ≤ C(‖G′v‖_(𝗍;k) + ‖χv‖_(−N′;k)) for G′ elliptic on
WF′(G) ([[lem:ii-a-8-4]] (c)–(d)): an e3b-vector field is a b-vector field.

(F2) For elements X_1, …, X_q and P of a ring, [X_1 ⋯ X_q, P] = Σ_(∅≠S) (ad_(X_S) P) X^({1..q}∖S), the sum over subsets
S of the positions, ad_(X_S) the iterated commutator and the remaining factors in their order ([[lem:ii-a-9-3]],
[[eq:ii-a-9-4]]).

**Theorem {#thm:ii-d1-1-1}** (The global estimate with b-regularity.) Let α_I, α_+, α_K, 𝗌_0 < 𝗌 and χ be as in
[[thm:ii-d-1-2]]. For every k ∈ ℕ_0 there is C_k such that

    ‖χu‖_(H^((𝗌;k),(2α_I,α_+,α_K))_(e3b;b))
        ≤ C_k (‖Pu‖_(H^((𝗌;k),(2α_I+2,α_++2,α_K))_(e3b;b)(Ω_*;E)^(•,−))
                + ‖u‖_(H^((𝗌_0;k),(2α_I,α_+,α_K))_(e3b;b)(Ω_*;E)^(•,−)))                                  {#eq:ii-d1-1-1}

for P = P_0, in the strong sense, and for every P satisfying conditions (1)–(2) of [[def:ii-c-3-3]] at the class
((d_0; k), (2ℓ_I, ℓ_+, ℓ_K)) (condition (3) not assumed) with ε_(P,k) small, with C_k
uniform; d_0 depends only on 𝗌_0 and 𝗌. Moreover there is d ∈ ℕ such that for every k and every P of class ((d_0; k),
(2ℓ_I, ℓ_+, ℓ_K)) with ε_(P,d) small,

    ‖χu‖_(𝗌;k) ≤ C_k (‖Pu‖_(𝗌;k) + ‖u‖_(𝗌_0;k) + ε_(P,k) (‖Pu‖_(𝗌;d) + ‖u‖_(𝗌_0;d))),                     {#eq:ii-d1-1-2}

with the spaces and weights of [[eq:ii-d1-1-1]], and C_k depending on P only through a bound for ε_(P,d).

This is [Hin26c, Proposition 7.11] in dimension 4 + 1, with the weights of u in the last norm of [[eq:ii-d1-1-2]] (see
[[sec:s06-remarks]]). [[eq:ii-d1-1-2]] is used for k ≥ d, and [[eq:ii-d1-1-1]] for k < d. The proof is in
[[sec:ii-d1-7]].

### The commuted system {#sec:ii-d1-2}

Throughout this section Γ ⊂ ᵉ³ᵇS*M is one of the sets of [[sec:ii-d-3]]–[[sec:ii-d-4]] (a radial set or the trapped set,
over one of ∂Σ^±), U_0 an open neighbourhood of Γ near fibre infinity, and L the operator that the corresponding
estimate there treats (L = W′⁻¹P, [[sec:ii-d-1-1]]). 𝔩 ∈ {0, 1} is the loss: 𝔩 = 0 at the radial sets and 𝔩 = 1 at
the trapped set, where the estimate loses one derivative. A *family* is 𝒳 = (X_1, …, X_J) with X_i ∈ Diff¹_b(M) acting
componentwise and X_J := I. For k ≥ 1, 𝒲_k := {1, …, J}^k is the set of words of length k, X^α := X_(α_1) ⋯ X_(α_k),
and for a position i and a letter j, j·(α∖i) is the word obtained by deleting the i-th letter of α and putting j in
front. The order of factors matters, as the X_i need not commute; words take care of it.

*Operators of limited regularity.* "Q is of class 𝒬^m_q" means that Q is a finite sum Σ a_l A_l with A_l ∈ C_b^∞Ψ^m_e3b
fixed and a_l ∈ C^∞ + C^((d_0;k−q))_(e3b;b), carried by the cut-off χ of the estimate, as in [[sec:ii-a-8-2]]: q
b-derivatives of the coefficients of P have been spent. Its *decaying part* is the sum of the terms whose coefficients
vanish at the face carrying Γ, at a rate ρ_Γ^ℓ for a defining function ρ_Γ of that face and some ℓ > 0. The hypotheses
on a family are:

(C) For each i < J, [L, X_i] = Σ_(j=1)^J Q_(ij) X_j + R_i, with Q_(ij) of class 𝒬^1_1 and R_i of class 𝒬^2_1 with
WF′(A_l) ∩ Ū_0 = ∅ for all its terms. For i = J put Q_(Jj) := 0 and R_J := 0, as [L, X_J] = [L, I] = 0.

(C2) (Only if 𝔩 = 1.) For i, i′ < J, [X_(i′), [X_i, L]] = Σ_(j,j′=1)^J Q^(2)_(i′i,jj′) X_j X_(j′) + R^(2)_(i′i), with
Q^(2)_(i′i,jj′) of class 𝒬^0_2 and R^(2)_(i′i) = R′ + Σ_j R″_j X_j with R′ of class 𝒬^2_2 and R″_j of class 𝒬^1_2, all
microsupported off Ū_0 as in (C). If i = J or i′ = J, put Q^(2)_(i′i,jj′) := 0 and R^(2)_(i′i) := 0, as the double
commutator then vanishes.

(M) Over a neighbourhood of the base projection of Ū_0, the X_i together with 𝒱_e3b span 𝒱_b over C^∞; and either the
X_i alone span 𝒱_b there, or there are i_0 < J and a bounded weight w, a product of non-negative powers of boundary
defining functions, with wX_(i_0) ∈ Diff¹_e3b elliptic on Ū_0. Each X_i, i < J, is a commutator field there:
[X_i, 𝒱_e3b] ⊂ 𝒱_e3b ([[lem:ii-a-2-2]], [[lem:ii-a-2-6]], [[cor:ii-a-2-3]]). The four families of
[[sec:ii-d1-3]]–[[sec:ii-d1-6]] extend to global elements of 𝒱_b that are commutator fields everywhere (∂_r and r∂_r
are e3b-fields, t_*∂_(t_*) is a commutator field everywhere, and the Ω_ab are 3b-fields near K⁺ and eb-commutator
fields near ℐ⁺), which is what the global statements of [[lem:ii-a-2-2]] and [[lem:ii-a-8-4]] (a) use.

*Parametrix remainders.* [[lem:ii-a-8-4]] (b) gives microlocal parametrices of a finite order J′; a remainder said
below to be microsupported off Ū_0 is the sum of such a term and of one of order −J′ near Ū_0. Every use needs only J′
large, depending on the orders, and we write as if the second term were absent.

**Lemma {#lem:ii-d1-2-1}** (The commuted system.) Assume (C), and (C2) if 𝔩 = 1. For k ≥ 1 put u^(k) := (X^α
u)_(α∈𝒲_k) and f := Lu. Then

    L^(k) u^(k) = f^(k) + f̃^(k) + f̃^(k)_♭,       f^(k) := (X^α f)_α,                                    {#eq:ii-d1-2-1}

where L^(k) acts on (ℂ^(N_E))^(𝒲_k) by

    (L^(k) w)_α := L w_α − Σ_(i=1)^k Σ_(j=1)^J Q_(α_i j) w_(j·(α∖i))
                   + 𝔩 Σ_(i<i′) Σ_(j,j′) Q^(2)_(α_i α_i′, jj′) w_(jj′·(α∖{i,i′}))                         {#eq:ii-d1-2-2}

(the last sum over pairs of positions, with jj′·(α∖{i,i′}) the word with those two letters deleted and j, j′ put in
front), f̃^(k)_α := −Σ_(|S|≥2+𝔩) (ad_(X_S) L) X^(α∖S) u, the sum over sets S of positions, and f̃^(k)_(♭,α) := Σ_i
R_(α_i) X^(α∖i) u − 𝔩 Σ_(i<i′) R^(2)_(α_i α_i′) X^(α∖{i,i′}) u.

This is [Hin26c, (7.32), (7.43), (7.61)] in dimension 4 + 1, written with words (see [[sec:s06-remarks]]).

*Proof.* L X^α u = X^α f − [X^α, L]u, and (F2) expands [X^α, L] over the sets S of positions. For S = {i},
ad_(X_(α_i)) L = −[L, X_(α_i)] = −Σ_j Q_(α_i j) X_j − R_(α_i) by (C), and X_j X^(α∖i) = X^(j·(α∖i)). So −(ad_(X_(α_i))
L) X^(α∖i) u = Σ_j Q_(α_i j) u^(k)_(j·(α∖i)) + R_(α_i) X^(α∖i) u. If 𝔩 = 1, for S = {i, i′}, i < i′, (F2) gives
ad_(X_(α_i)) ad_(X_(α_i′)) L = [X_(α_i), [X_(α_i′), L]], which (C2) writes as Σ Q^(2) X_j X_(j′) + R^(2), with the
indices of [[eq:ii-d1-2-2]] after relabelling; its contribution is moved to the left in the same way. ∎

*Commuting letters.* If a letter j < J commutes with every X_i, then for a word α and a position i, X_j X^(α∖i) =
X^(α[i→j]), where α[i→j] is α with its i-th letter replaced by j. So in [[eq:ii-d1-2-2]] the term Q_(α_i j)
w_(j·(α∖i)) may be replaced by Q_(α_i j) w_(α[i→j]); the operator so modified is

    (L^(k) w)_α := L w_α − Σ_(i=1)^k Σ_(j=1)^J Q_(α_i j) w_(α⟨i,j⟩)
                   + 𝔩 Σ_(i<i′) Σ_(j,j′) Q^(2)_(α_i α_i′, jj′) w_(jj′·(α∖{i,i′})),                  {#eq:ii-d1-2-2-prime}

where α⟨i,j⟩ := α[i→j] if j < J and the letter j commutes with every X_i, and α⟨i,j⟩ := j·(α∖i) otherwise.
[[eq:ii-d1-2-1]] holds for it with the same proof, since only L^(k) u^(k) enters, and [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]]
use of L^(k) only that it is L ⊗ Id minus a coupling whose coefficients carry at most 1 + 𝔩 b-derivatives of those of
P, so they hold for [[eq:ii-d1-2-2-prime]]. For a letter 1 with α_i = 1, α[i→1] = α: the coupling through that letter
is diagonal. This is what the horizon needs ([[lem:ii-d1-4-1]] (c)). With [[eq:ii-d1-2-2]] the word 1·(α∖i) differs
from α in general (for instance α = (2, 1), i = 2), and for k ≥ 2 the Hermitian part of the coupling is indefinite. At
the horizon Q_(1j) = 0 for j ≠ 1, and Q_(21), Q_(22) decay at K⁺ ([[lem:ii-d1-4-1]] (b) and its proof); so at
∂R_(𝓗⁺), on the two components (1, 2, …, 2) and (2, 1, 2, …, 2), the principal symbol of Im(L^(k) − L ⊗ Id) for
[[eq:ii-d1-2-2]] is σ_1(Im(−Q_11)) ≠ 0 times the matrix with rows (1, ½) and (½, 0), whose determinant is −¼.

The coefficients of L^(k) − L ⊗ Id carry at most 1 + 𝔩 b-derivatives of those of P, whatever k is; this is what makes
the tame estimate possible.

**Lemma {#lem:ii-d1-2-2}** (Mixed norms.) Assume (M). Let B, B̃ ∈ C_b^∞Ψ^0_e3b be carried by χ, with operator wave
front sets in U_0 and B̃ elliptic on WF′(B), and χ̃ a cut-off equal to 1 near the base projection of Ū_0. Then for all
orders 𝗍, 𝗍_0 and k ∈ ℕ_0,

    ‖Bu‖_(𝗍;k) ≤ C (‖B̃u‖_(𝗍;k−1) + Σ_(α∈𝒲_k) ‖BX^α u‖_𝗍 + ‖χ̃u‖_(𝗍_0;k)),                                {#eq:ii-d1-2-3}

    Σ_(α∈𝒲_k) ‖BX^α u‖_𝗍 ≤ C (‖B̃u‖_(𝗍;k) + ‖χ̃u‖_(𝗍_0;k)).                                               {#eq:ii-d1-2-4}

[[eq:ii-d1-2-4]] holds without (M), for any family of b-differential operators of order 1. This is [Hin26c, Lemmas 7.15
and 7.19] in dimension 4 + 1.

*Proof.* [[eq:ii-d1-2-4]]: BX^α u = X^α Bu − [X^α, B]u. The first term has H^𝗍-norm at most C‖Bu‖_(𝗍;k), as the X_i
are b-differential operators. By (F2), [X^α, B] is a sum of terms (ad_(X_S) B) X^(α∖S) with ad_(X_S) B ∈ C_b^∞Ψ^0_e3b
microsupported in WF′(B) ([[lem:ii-a-8-4]] (a)); moving the remaining factors to the left by [[eq:ii-a-9-5]] bounds
them by C‖B̃u‖_(𝗍;k) + C‖χ̃u‖_(𝗍_0;k), using an elliptic parametrix of B̃ ([[lem:ii-a-8-4]] (c)). ‖Bu‖_(𝗍;k) ≤
C(‖B̃u‖_(𝗍;k) + ‖χ̃u‖_(𝗍_0;k)) in the same way. [[eq:ii-d1-2-3]]: by (M) and the notation of [[sec:ii-a-9-3]],
‖Bu‖_(𝗍;k) is equivalent to the sum of ‖AX^β Bu‖_𝗍 over A ∈ Diff^(k−|β|)_e3b from a fixed finite set and words β in
the X_i with |β| ≤ k. If the X_i span 𝒱_b, only A = I, |β| = k is needed (words with the letter J give the lower
orders). Otherwise, let Q_q ∈ C_b^∞Ψ^(−q)_e3b be a microlocal parametrix of (wX_(i_0))^q on Ū_0, I =
Q_q (wX_(i_0))^q + R′_q with WF′(R′_q) ∩ Ū_0 = ∅ (with (wX_(i_0))^q = w^q X_(i_0)^q + Σ_(q′<q) w_(q′) X_(i_0)^(q′),
w_(q′) bounded, as X_(i_0) w ∈ wC^∞). Then for A of order q := k − |β|,

    AX^β Bu = AQ_q w^q X_(i_0)^q X^β Bu + Σ_(q′<q) AQ_q w_(q′) X_(i_0)^(q′) X^β Bu + AR′_q X^β Bu.

AQ_q w^q and AQ_q w_(q′) lie in C_b^∞Ψ^0_e3b (as w^q, w_(q′) are bounded and A has order q), so the first term is
bounded by ‖X^(i_0^q β) Bu‖_𝗍, a word of length k, and the second by words of length < k with letters J added. The
third is microsupported off Ū_0 after commuting X^β through B, and is at most C‖χ̃u‖_(𝗍_0;k). Finally X^γ Bu = BX^γ
u + [X^γ, B]u, and the commutator terms carry at most k − 1 factors and are at most C‖B̃u‖_(𝗍;k−1) + C‖χ̃u‖_(𝗍_0;k), as
in [[eq:ii-d1-2-4]]. ∎

In the estimates below, the operators B, E, G of an estimate of [[sec:ii-d-3]]–[[sec:ii-d-4]] come with properties
(1)–(4) listed there (wave front sets in a given neighbourhood, Schwartz kernels in a given set, B elliptic at Γ, and a
condition on E). A finite union of closed sets each satisfying (4) satisfies (4); and an operator elliptic on such a
union, with wave front set in a small neighbourhood of it, can be chosen to satisfy (4) again; for [[prop:ii-d-3-6]] it
satisfies (4) with t_(*,−) + δ′ in place of t_(*,−), for any δ′ > 0, and since t_(*,−) is arbitrary there, starting the
inductions below from t_(*,−) − kδ′ gives (4) as stated at the order k. We use this without comment.

*The estimate for systems.* We say (E_𝔩) holds for a family on U_0 if, for every k ≥ 1, every neighbourhood U ⊂ U_0 of
Γ and every χ̃ as in [[lem:ii-d1-2-2]], there are B_k, E_k, G_k with properties (1)–(4), wave front sets in U and B_k
elliptic at Γ, such that in the strong sense

    ‖B_k w‖_𝗍 ≤ C (‖G_k L^(k) w‖_(𝗍−1+𝔩) + ‖E_k w‖_(𝗍+𝔩) + ‖χ̃w‖_(𝗍_0))                                   {#eq:ii-d1-2-5}

for ℂ^(N_E |𝒲_k|)-valued w, with weights as in the estimate of [[sec:ii-d-3]]–[[sec:ii-d-4]], and with C depending on k
and on P only through bounds for finitely many C^(d_0)-norms of the coefficients of L^(k). [[lem:ii-d1-2-5]] gives
(E_𝔩) in each case below.

**Lemma {#lem:ii-d1-2-3}** (The induction.) Assume (C), (M), (C2) if 𝔩 = 1, and (E_𝔩), at the constant orders 𝗍 > 𝗍_0,
and that P is of class ((d_0; k), …) with d_0 large depending on 𝗍, 𝗍_0. Then for every k ∈ ℕ_0 and every
neighbourhood U ⊂ U_0 of Γ there are B, E, G with properties (1)–(4), wave front sets in U and B elliptic at Γ, such
that in the strong sense

    ‖Bu‖_(𝗍;k) ≤ C_k (‖GLu‖_(𝗍−1+𝔩;k) + ‖Eu‖_(𝗍+𝔩;k) + ‖χ̃u‖_(𝗍_0;k)).                                    {#eq:ii-d1-2-6}

For k = 0 this is the estimate of [[sec:ii-d-3]]–[[sec:ii-d-4]] itself. This is the induction in [Hin26c, proofs of
Propositions 7.17 and 7.22].

*Proof.* Induction on k. Let k ≥ 1 and assume [[eq:ii-d1-2-6]] at k − 1 for every neighbourhood of Γ. Let U_(k−1) ⊂ U
be a neighbourhood of Γ on which the conclusion at k − 1 holds for operators B′ microsupported in U_(k−1), with
operators E′, G′ (the union of the sets of two applications, for B′ and a slightly larger one). Apply (E_𝔩) with
U_(k−1) in place of U, to w := u^(k), giving B_k, E_k, G_k microsupported in U_(k−1); choose G^♯_1, G^♯_2 with
WF′(G_k) ⊂ Ell(G^♯_1), WF′(G^♯_1) ⊂ Ell(G^♯_2) and WF′(G^♯_2) ⊂ U_(k−1), and B with WF′(B) ⊂ Ell(B_k), B elliptic at
Γ. By [[lem:ii-d1-2-1]], ‖G_k L^(k) u^(k)‖ ≤ ‖G_k f^(k)‖ + ‖G_k f̃^(k)‖ + ‖G_k f̃^(k)_♭‖, all norms of order 𝗍 − 1 + 𝔩.
We bound each term of [[eq:ii-d1-2-5]] at w = u^(k).

*The left side.* By [[eq:ii-d1-2-3]] with B̃ := G^♯_1, ‖Bu‖_(𝗍;k) ≤ C(‖G^♯_1 u‖_(𝗍;k−1) + Σ_α ‖BX^α u‖_𝗍 +
‖χ̃u‖_(𝗍_0;k)), and ‖BX^α u‖_𝗍 ≤ C(‖B_k u^(k)‖_𝗍 + ‖χ̃u‖_(𝗍_0;k)), as B_k is elliptic on WF′(B) and ‖χ̃X^α u‖_(𝗍_0) ≤
C‖χ̃′u‖_(𝗍_0;k), χ̃′ slightly larger. The first term is bounded by [[eq:ii-d1-2-6]] at k − 1.

*The a priori terms.* By [[eq:ii-d1-2-4]], ‖E_k X^α u‖_(𝗍+𝔩) ≤ C(‖Eu‖_(𝗍+𝔩;k) + ‖χ̃u‖_(𝗍_0;k)) for E elliptic on
WF′(E_k), and ‖χ̃u^(k)‖_(𝗍_0) ≤ C‖χ̃′u‖_(𝗍_0;k).

*The term f^(k).* By [[eq:ii-d1-2-4]] for f, ‖G_k X^α f‖_(𝗍−1+𝔩) ≤ C(‖G^♯_1 f‖_(𝗍−1+𝔩;k) + ‖χ̃f‖_(𝗍_0−2;k)). Here
‖χ̃f‖_(𝗍_0−2;k) = ‖χ̃Lχ̃′u‖_(𝗍_0−2;k) ≤ C‖χ̃′u‖_(𝗍_0;k), as L is bounded on the mixed spaces with coefficients of
class (d_0; k) ([[lem:ii-a-8-6]] (a)), and ‖G^♯_1 f‖ ≤ C(‖GLu‖_(𝗍−1+𝔩;k) + ‖χ̃f‖_(𝗍_0−2;k)) for G elliptic on
WF′(G^♯_1).

*The term f̃^(k)_♭.* G_k R_i and G_k R^(2) have every order, the wave front sets being disjoint ([[lem:ii-a-8-5]] (b),
with the coefficient regularity (d_0; k − 2)); for the terms R″_j X_j X^(α∖{i,i′}) u of (C2) the word X_j
X^(α∖{i,i′}) has k − 1 letters. So ‖G_k f̃^(k)_♭‖_(𝗍−1+𝔩) ≤ C‖χ̃u‖_(𝗍_0;k−1).

*The term f̃^(k).* Let |S| = q ≥ 2 + 𝔩. ad_(X_S) L is a second-order operator of class 𝒬^2_q: each commutator with a
b-vector field preserves Diff²_e3b up to the coefficients ([[lem:ii-a-4-1]], and [[lem:ii-a-2-2]] near K⁺,
[[lem:ii-a-2-6]] near ℐ⁺), and differentiates the coefficients once. So by [[lem:ii-a-8-6]] (b) and [[eq:ii-d1-2-4]],

    ‖G_k (ad_(X_S) L) X^(α∖S) u‖_(𝗍−1+𝔩) ≤ C (‖G^♯_2 u‖_(𝗍+1+𝔩;k−q) + ‖χ̃u‖_(𝗍_0;k)).

As q − 1 ≥ 1 + 𝔩, q − 1 applications of (F1) bound ‖G^♯_2 u‖_(𝗍+1+𝔩;k−q) by C(‖G^♯_3 u‖_(𝗍;k−1) + ‖χ̃u‖_(−N′;k)),
with G^♯_3 slightly larger than G^♯_2 and still microsupported in U_(k−1); this is bounded by [[eq:ii-d1-2-6]] at k
− 1. This is where 𝔩 = 1 needs (C2): a term with q = 2 would need ‖G^♯_2 u‖_(𝗍+2;k−2), which (F1) bounds only by the
norm at (𝗍 + 1; k − 1), one order above what the induction controls.

Collecting the terms gives [[eq:ii-d1-2-6]] at k, with E elliptic on the union of WF′(E_k) and the E-sets of the step k
− 1. Each quantity bounded is finite when the right side of [[eq:ii-d1-2-6]] is, by [[eq:ii-d1-2-5]] in the strong
sense and the inductive hypothesis, so the estimate holds in the strong sense. ∎

**Lemma {#lem:ii-d1-2-4}** (Tame version.) Under the hypotheses of [[lem:ii-d1-2-3]] there is d ∈ ℕ, depending only on
𝗍, 𝗍_0, such that for all k and P of class ((d_0; k), …), with the operators of [[lem:ii-d1-2-3]],

    ‖Bu‖_(𝗍;k) ≤ C_k (ℛ_k + ε_(P,k) ℛ_d),       ℛ_q := ‖GLu‖_(𝗍−1+𝔩;q) + ‖Eu‖_(𝗍+𝔩;q) + ‖χ̃u‖_(𝗍_0;q),    {#eq:ii-d1-2-7}

with C_k depending on P only through a bound for ε_(P,d). This is [Hin26c, (7.52), (7.68)] in dimension 4 + 1.

*Proof.* Let d_1 and d̃ be the larger of the numbers d_0, resp. d̃, of [[prop:ii-a-9-6]] for the orders (𝗍 + 1 + 𝔩,
𝗍_0) and (𝗍_0 − 2, 𝗍_0 − 2); take d_0 ≥ d_1 + 2, enlarged to serve [[lem:ii-d1-2-3]], and d := d̃ + 3. For k ≤ d,
[[eq:ii-d1-2-7]] is [[eq:ii-d1-2-6]], whose constant depends on ε_(P,k) ≤ ε_(P,d). Let k > d and assume
[[eq:ii-d1-2-7]] below k. In the proof of [[lem:ii-d1-2-3]] the coefficients of P enter with more than 2 b-derivatives
in two places only. The constant of [[eq:ii-d1-2-5]] involves the coefficients of L^(k), which carry at most 1 + 𝔩
derivatives ([[lem:ii-d1-2-1]]), so it depends on ε_(P,3) ≤ ε_(P,d). (a) ‖χ̃Lχ̃′u‖_(𝗍_0−2;k): write L = L_0 + (L −
L_0), L_0 the operator of P_0; L_0 contributes C‖χ̃′u‖_(𝗍_0;k), and [[cor:ii-a-9-7]] bounds the rest by C_k(ε_(P,d̃)
‖χ̃″u‖_(𝗍_0;k) + ε_(P,k) ‖χ̃″u‖_(𝗍_0;d̃)). (b) ‖G_k (ad_(X_S) L) X^(α∖S) u‖_(𝗍−1+𝔩), |S| = q ≥ 2 + 𝔩: the coefficients
of ad_(X_S)(L − L_0) are sums of (D^(q′)_[b] p) times fixed operators, q′ ≤ q, p a coefficient of L − L_0; the part
with q′ ≤ 2 + 𝔩 is bounded as in [[lem:ii-d1-2-3]] with constant depending on ε_(P,3). For q′ ≥ 3 + 𝔩, commute the
second-order factor to the front and G_k through it, as in [Hin26c, (7.55)–(7.56)]; it remains to bound
‖G̃ (D^(q′)_[b] D^(≤2)_e3b p)(D^(k−q)_[b] u)‖_(𝗍+1+𝔩) with G̃ microsupported in U_(k−1). [[prop:ii-a-9-6]], with
D^(2+𝔩)_[b] D^(≤2)_e3b p for its ℓ and (q′ − 2 − 𝔩, k′) for its (j, k), k′ := k − q + q′ − 2 − 𝔩 ≤ k − 2 − 𝔩, bounds
it, after enlarging k′ to k − 2 − 𝔩 in the norms of u (and the constant C_(k′) to C_k), by

    C_k (‖p‖_(d_1+2;d̃+2+𝔩) (‖G^♯u‖_(𝗍+1+𝔩;k−2−𝔩) + ‖χ̃u‖_(𝗍_0;k))
          + ‖p‖_(d_1+2;k) (‖G^♯u‖_(𝗍+1+𝔩;d̃) + ‖χ̃u‖_(𝗍_0;d̃))),

as ‖D^(2+𝔩)_[b] D^(≤2)_e3b p‖_(d_1;q) ≤ C‖p‖_(d_1+2;q+2+𝔩) and k′ + 2 + 𝔩 ≤ k. By (F1), ‖G^♯u‖_(𝗍+1+𝔩;k−2−𝔩) ≤
C‖G^♯_1 u‖_(𝗍;k−1), bounded by [[eq:ii-d1-2-7]] at k − 1, whose high norm ε_(P,k−1) multiplies ℛ_d only; and
‖G^♯u‖_(𝗍+1+𝔩;d̃) ≤ C‖G^♯_1 u‖_(𝗍;d̃+1+𝔩), bounded by [[eq:ii-d1-2-6]] at the order d̃ + 1 + 𝔩 < d. Here
‖p‖_(d_1+2;d̃+2+𝔩) ≤ Cε_(P,d) and ‖p‖_(d_1+2;k) ≤ Cε_(P,k), as d_1 + 2 ≤ d_0, the coefficients of L − L_0 being those
of P − P_0 up to fixed smooth factors ([[def:ii-c-3-6]]). The other terms of the proof of [[lem:ii-d1-2-3]] involve no
coefficient with more than two derivatives. This gives [[eq:ii-d1-2-7]]. ∎

**Lemma {#lem:ii-d1-2-5}** (The estimates of [[sec:ii-d-3]]–[[sec:ii-d-4]] for systems.) Let m ∈ ℕ and L̃ := L ⊗ Id_m −
Q on (ℂ^(N_E))^m, with Q of class 𝒬^1_2 (with the regularity (d_0; 0) for its coefficients). Let Γ be one of the sets
of [[prop:ii-d-3-1]]–[[prop:ii-d-3-6]] and [[prop:ii-d-4-2]], with the fibre inner product h used there, and suppose
that at Γ, as Hermitian matrices for h^(⊕m),

    ς ρ σ_1(Im_(h^(⊕m)) (−Q)) ≤ 0,                                                                        {#eq:ii-d1-2-8}

with ρ the function used at Γ in [[sec:ii-d-3]]–[[sec:ii-d-4]] and ς = ±1 on ∂Σ^±. Then the estimate of
[[sec:ii-d-3]]–[[sec:ii-d-4]] at Γ holds for L̃ in place of L, with the same orders, weights and thresholds, and with
constants depending on finitely many norms of the coefficients of Q.

*Proof.* L ⊗ Id_m is L for the bundle E^(⊕m) = ℂ^(N_E m), an operator of the same class with the same thresholds in the
inner product h^(⊕m), as all quantities are block diagonal. *Radial sets.* By [[rem:ii-d-3-7]], the estimates hold for
L ⊗ Id + P̃ with P̃ first order of the form stated there, with the thresholds calculated from σ_1(Im_(h^(⊕m)) L̃) at Γ.
By [[eq:ii-d1-2-8]] this differs from that of L ⊗ Id by a non-positive Hermitian matrix (times ς). In each quantity Q_ε
of [[sec:ii-d-3]] it enters as −2A⁻¹(·)A (the term −2A⁻¹𝔭′A, and at ∂R_(ℐ⁺,out) the term 4A⁻¹(Re_h p_1)A =
−2A⁻¹𝔭′A), so it only increases Q_ε, and every lower bound of [[sec:ii-d-3]] persists. *The trapped set.* In the proof
of [[prop:ii-d-4-2]] the operator enters through its principal symbol G Id, unchanged; through 𝔭 at ∂Γ_(K⁺), now 𝔭 −
ρσ_1(Im Q) after the conjugation of Step 0, whose largest eigenvalue is at most ϑ_Γ by [[eq:ii-d1-2-8]], so (T3) and
[[eq:ii-d-4-3]] hold as stated; through the form Op(ℓ_f) + R_L of the remark after [[lem:ii-d-2-5]], which L̃ has; and
through the commutator [[eq:ii-d-4-4]], where [Q, Φ_u] has order 0 and joins R_2. Nothing else in [[sec:ii-d-2]] and
[[sec:ii-d-4]] uses the operator. ∎

In [[sec:ii-d1-3]]–[[sec:ii-d1-6]], [[eq:ii-d1-2-8]] holds because the first-order part of Q either decays at the face
carrying Γ, so that its principal symbol vanishes at Γ, or is diagonal with a non-positive contribution (at the
horizon). The part of Q of order 0 does not enter [[eq:ii-d1-2-8]].

### Near ℐ⁺ {#sec:ii-d1-3}

Near ℐ⁺ ∩ Ω we use the coordinates ρ_+ = t_*⁻¹, x_I = (t_*/r)^(1/2), ω ∈ 𝕊³ of [[sec:ii-c-5-1]], W := x_I² ρ_+² and L
:= W⁻¹P, as in [[prop:ii-d-3-5]] and [[prop:ii-d-3-6]]. Put

    V_1 := x_I ∂_(x_I) − 2ρ_+ ∂_(ρ_+) = 2t_* ∂_(t_*),       V_2 := x_I ∂_(x_I) = −2r ∂_r,

the second at fixed t_*, and let Ω_ab, 1 ≤ a < b ≤ 4, be the six rotation fields y_a ∂_(y_b) − y_b ∂_(y_a) of 𝕊³ ⊂ ℝ⁴,
extended independently of (x_I, ρ_+). The family is 𝒳_I := (V_1, V_2, Ω_12, …, Ω_34, I), J = 9.

**Lemma {#lem:ii-d1-3-1}** (Commutators near ℐ⁺.) (a) [V_1, V_2] = [V_i, Ω_ab] = 0, the Ω_ab span 𝔰𝔬(4), and
Σ_(a<b) Ω_ab² is the Laplace–Beltrami operator of 𝕊³, so Δ_𝕊³ of [[lem:ii-c-3-4]] is ±Σ_(a<b) Ω_ab² and commutes with
every Ω_ab. (b) The family 𝒳_I satisfies (C) on Ω_I = Ω ∩ {x_I ≤ ε_I} with R_i = 0, and each Q_(ij) is the sum of an
operator of order 0 and a first-order eb-operator whose coefficients lie in x_I C^∞ + x_I^(2ℓ_I) C^((d_0;k−1))_(eb;b).
(c) 𝒳_I spans 𝒱_b near ℐ⁺, and its elements are eb-commutator fields ([[lem:ii-a-2-6]]), so (M) holds. (d) At
∂R_(ℐ⁺,in,+) and ∂R_(ℐ⁺,out), which lie over x_I = 0, the first-order part of each Q_(ij) has vanishing principal
symbol, so [[eq:ii-d1-2-8]] holds with equality.

This is [Hin26c, Lemma 7.12] in dimension 4 + 1: there are six rotation fields on 𝕊³, Δ_𝕊³ is exactly ±Σ_(a<b) Ω_ab²,
the constant 3 = n − 1 of [[lem:ii-c-3-4]] replaces 2, and, the bundle being trivial with b-vector fields acting
componentwise, the fields V_1, V_2, Ω_ab commute with one another exactly where [Hin26c, (7.31)] has commutators in
x_I C^∞. None of this changes the structure of (C).

*Proof.* (a) V_1, V_2 are coordinate vector fields of the product coordinates (log x_I, log ρ_+), up to constant linear
combinations, and the Ω_ab act on ω alone. The Ω_ab are the generators of the action of SO(4) on 𝕊³, and Σ_(a<b) Ω_ab²
is the Casimir operator of this action on functions, which is the Laplace–Beltrami operator of the round metric (the
identity Σ_(a<b) (y_a ∂_b − y_b ∂_a)² = |y|² Δ_ℝ⁴ − (y·∂)² − 2 y·∂ restricted to |y| = 1, functions extended
homogeneously of degree 0). (b) By [[lem:ii-c-3-4]], near ℐ⁺,

    2L = −(V_2 − 3 − 2p_1) V_1 ± 2x_I² Σ_(a<b) Ω_ab² + p_0 + R̃,       R̃ ∈ C^((d_0;k),(2ℓ_I,0))_(eb;b) Diff²_eb,

with p_0, p_1 = S|_(∂X) + p̃_1 functions on ℐ⁺ extended independently of x_I, so V_2 p_0 = V_2 p_1 = 0. We calculate
[2L, X] for X ∈ 𝒳_I, X ≠ I, using [AB, X] = A[B, X] + [A, X]B and (a).

[−(V_2 − 3 − 2p_1)V_1, X] = 2[p_1, X]V_1 = −2(Xp_1)V_1: an operator of order 0 times V_1; it vanishes for X = V_2.
[±2x_I² Σ Ω_ab², X] = ∓2(X x_I²) Σ Ω_ab², which is ∓4x_I² Σ Ω_ab² for X = V_1, V_2 (as V_1 x_I² = V_2 x_I² = 2x_I²) and
0 for X = Ω_cd. Now x_I² Ω_ab² = x_I (x_I Ω_ab) ∘ Ω_ab with x_I Ω_ab ∈ 𝒱_eb: a first-order eb-operator with coefficient
in x_I C^∞, times Ω_ab. [p_0, X] = −(Xp_0), of order 0 (a term Q_(iJ) X_J). Finally [R̃, X] ∈
C^((d_0;k−1),(2ℓ_I,0))_(eb;b) Diff²_eb, as X is an eb-commutator field and differentiates the coefficients once
([[lem:ii-a-2-6]] and [[lem:ii-a-8-2]] (b)). 𝒱_eb is spanned over C^∞ by V_1, V_2 and x_I Ω_ab, so every element of
x_I^(2ℓ_I) C^((d_0;k−1))_(eb;b) Diff²_eb is a sum Σ_j A_j X_j with A_j ∈ x_I^(2ℓ_I) C^((d_0;k−1))_(eb;b) Diff¹_eb (for j
a rotation, the factor x_I of x_I Ω_ab joins A_j; the first-order part of the operator is A_J X_J). Collecting, [L, X_i]
= Σ_j Q_(ij) X_j with Q_(ij) as stated. (c) Near ℐ⁺, 𝒱_b is spanned by ρ_+ ∂_(ρ_+), x_I ∂_(x_I) and the vector fields on
𝕊³, which V_1, V_2 and the Ω_ab span. (d) The principal symbol of a first-order eb-operator with coefficients in x_I
C^∞ + x_I^(2ℓ_I) C^0 vanishes over x_I = 0. ∎

**Proposition {#prop:ii-d1-3-2}** (The radial sets at ℐ⁺ with b-regularity.) [[prop:ii-d-3-5]] and [[prop:ii-d-3-6]]
hold with H^((𝗍;k))_(e3b;b) in place of H^𝗍_e3b for every k ∈ ℕ_0:

    ‖Bu‖_((s;k),(2α_I,α_+)) ≤ C_k (‖GPu‖_((s−1;k),(2α_I+2,α_++2)) + ‖Eu‖_((s;k),(2α_I,α_+))
                                    + ‖χ̃u‖_((s_0;k),(2α_I,α_+))),                                        {#eq:ii-d1-3-1}

with B, E, G having the properties (1)–(4) stated there, in the strong sense, for P = P_0 and P of class ((d_0; k), …)
with ε_(P,k) small, d_0 depending only on s, s_0; and in the tame form [[eq:ii-d1-2-7]], with ε_(P,k) times the right
side of [[eq:ii-d1-3-1]] at the order d.

This is the analogue of [Hin26c, Propositions 7.8–7.9] in [Hin26c, Section 7.2.3], in dimension 4 + 1.

*Proof.* [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]] with 𝔩 = 0, the family 𝒳_I and [[lem:ii-d1-3-1]];
‖GLu‖_((s−1;k),(2α_I,α_+)) and ‖GPu‖_((s−1;k),(2α_I+2,α_++2)) are equivalent up to a microlocal error, W being a weight.
The thresholds ([[eq:ii-d-3-7]] and [[eq:ii-d-3-9]]) concern the weights only and are unchanged by [[lem:ii-d1-3-1]]
(d). ∎

### The horizon {#sec:ii-d1-4}

Near 𝓗⁺ ∩ K⁺ = {r = r_h, ρ_K = 0} use the coordinates (t_*, r, ω), ρ_K = t_*⁻¹, with covectors −σ dt_* + ξ_0 dr + η;
W′ = 1 and L = P, as in [[prop:ii-d-3-1]]. ∂R_(𝓗⁺) lies in {σ = 0, η = 0} with ξ_0 ≠ 0 ([[def:ii-b-4-1]]: it is the
boundary of the conormal bundle of {r = r_h}), so we take U_0 ⊂ {|ξ_0| ≥ c(|σ| + |ξ_0| + |η|)}, a small neighbourhood
of ∂R_(𝓗⁺). The family is 𝒳_𝓗 := (∂_r, t_* ∂_(t_*), I).

**Lemma {#lem:ii-d1-4-1}** (Commutators at the horizon.) (a) (M) holds: 𝒱_b near 𝓗⁺ ∩ K⁺ is spanned by 𝒱_3b and t_*
∂_(t_*) ([[cor:ii-a-2-3]]); ∂_r ∈ 𝒱_3b is elliptic on Ū_0 (with w = 1); both are e3b-commutator fields
([[lem:ii-a-2-2]]). (b) (C) holds on U_0. (c) The system L^(k) = P ⊗ Id − Q of [[lem:ii-d1-2-1]] in the form
[[eq:ii-d1-2-2-prime]], all letters commuting ([∂_r, t_* ∂_(t_*)] = 0), satisfies, at ∂R_(𝓗⁺),

    ς ρ σ_1(Im(−Q)) = −diag(j_α)_(α∈𝒲_k) β_0 ≤ 0,                                                         {#eq:ii-d1-4-1}

with j_α the number of letters 1 (that is, of factors ∂_r) in α, ρ the function of (H3) and β_0 > 0 of
[[eq:ii-b-4-1]]. So [[eq:ii-d1-2-8]] holds, and the threshold of [[prop:ii-d-3-1]] for L^(k) is at most ϑ_𝓗.

This is [Hin26c, Lemmas 7.15–7.16] in dimension 4 + 1, with the sign at the horizon calculated from β_0 rather than
from the Kerr formula [Hin26c, (7.48)].

*Proof.* (b) Write P = Σ_l p_l A_l near 𝓗⁺ ∩ K⁺, with A_l ∈ Diff²_3b fixed and independent of t_* (products of
∂_(t_*), ∂_r, ∂_ω), and p_l = p^♯_l + p̃_l, p^♯_l the coefficients of P_0, independent of t_*, and p̃_l ∈ ρ_K^(ℓ_K)
C^((d_0;k))_(3b;b) ([[def:ii-c-3-3]]). Let Q_r ∈ C_b^∞Ψ^(−1)_3b be a microlocal parametrix of ∂_r on Ū_0: I = Q_r
∂_r + R_r, WF′(R_r) ∩ Ū_0 = ∅.

*The letter X_1 = ∂_r.* [P, ∂_r] is a second-order operator of class 𝒬^2_1. Put Q_11 := [P, ∂_r] Q_r, R_1 := [P,
∂_r] R_r, and Q_(1j) := 0 for j ≠ 1; then [P, ∂_r] = Q_11 ∂_r + R_1. The principal symbol of [P, ∂_r] is (1/i){G,
iξ_0} = H_G ξ_0, as ∂_r has symbol iξ_0. So Q_11 has principal symbol H_G ξ_0/(iξ_0) = −i(H_G ξ_0)/ξ_0, a purely
imaginary scalar, and σ_1(Im(−Q_11)) = (H_G ξ_0)/ξ_0. Its lower-order part (from the first-order part of P, composed
with Q_r) has order 0 and does not enter.

*The letter X_2 = t_* ∂_(t_*).* t_* ∂_(t_*) p^♯_l = 0, and by [[lem:ii-a-2-2]], [t_* ∂_(t_*), A_l] = ρ_K A^♭_l t_*
∂_(t_*) + ρ_K A^♯_l with A^♭_l ∈ Diff¹_3b, A^♯_l ∈ Diff²_3b. Hence

    [P, X_2] = −Σ_l ((X_2 p̃_l) A_l + p_l ρ_K A^♭_l X_2 + p_l ρ_K A^♯_l),

and with I = Q_r ∂_r + R_r on the second-order terms, Q_22 := −Σ_l p_l ρ_K A^♭_l, Q_21 := −Σ_l ((X_2 p̃_l) A_l + p_l
ρ_K A^♯_l) Q_r, R_2 := −Σ_l ((X_2 p̃_l) A_l + p_l ρ_K A^♯_l) R_r. Their coefficients carry a factor ρ_K or ρ_K^(ℓ_K)
(X_2 p̃_l ∈ ρ_K^(ℓ_K) C^((d_0;k−1))_(3b;b)), so they decay at K⁺.

(c) By (b) and [[eq:ii-d1-2-2-prime]], −Q has, at ∂R_(𝓗⁺) ⊂ {ρ_K = 0}, first-order principal symbol diag(j_α) i(H_(G_0)
ξ_0)/ξ_0: each letter 1 of α couples the component α to itself through Q_11, as α[i→1] = α, and the couplings through
Q_21, Q_22 decay; G = G_0 there. Let ρ̃ := |ξ_0|⁻¹ on U_0 and 𝖧 := ρH_G. Then ρ(H_G ξ_0)/ξ_0 = −ρρ̃⁻¹ H_G ρ̃ = −ρ̃⁻¹𝖧ρ̃.
At the radial set ∂R_(𝓗⁺) the vector field 𝖧 on the cosphere bundle vanishes, so ρ̃⁻¹𝖧ρ̃ = ρ⁻¹𝖧ρ + (ρ̃/ρ)⁻¹𝖧(ρ̃/ρ)
= ρ⁻¹𝖧ρ = β_0 there ([[eq:ii-b-4-1]], as in the proof of [[prop:ii-d-3-1]]), ρ̃/ρ being homogeneous of degree 0. This
gives [[eq:ii-d1-4-1]] on ∂Σ⁺, where ς = 1; on ∂Σ⁻ the quantity (H_G ξ_0)/ξ_0 is odd (H_G ξ_0 even, ξ_0 odd), the
future field is −𝖧, whose ρ⁻¹(−𝖧)ρ is β_0, so ρ⁻¹𝖧ρ = −β_0 there, and ς = −1 restores [[eq:ii-d1-4-1]]. The threshold
of [[prop:ii-d-3-1]] for L^(k) is then sup max spec(β_0⁻¹(𝔭 − j_α β_0)) ≤ ϑ_𝓗, in the inner product h^(⊕𝒲_k). ∎

The non-positive sign in [[eq:ii-d1-4-1]] is the red shift: commuting with ∂_r lowers the threshold, so the minimal
regularity s_0 > ½ + ϑ_𝓗 of [[prop:ii-d-3-1]] does not rise with k.

**Proposition {#prop:ii-d1-4-2}** (The horizon with b-regularity.) Let s > s_0 > ½ + ϑ_𝓗 and k ∈ ℕ_0. There are B, E,
G with the properties (1)–(4) of [[prop:ii-d-3-1]] such that for all α_K ∈ ℝ and χ̃ as there

    ‖Bu‖_((s;k),α_K) ≤ C_k (‖GPu‖_((s−1;k),α_K) + ‖Eu‖_((s;k),α_K) + ‖χ̃u‖_((s_0;k),α_K)),                {#eq:ii-d1-4-2}

in the strong sense, uniformly for P = P_0 and P of class ((d_0; k), (0, 0, ℓ_K)) near K⁺ with ε_(P,k) small, d_0
depending only on s, s_0; and the tame estimate [[eq:ii-d1-2-7]] holds, with d depending only on s, s_0 and C_k on P
only through ε_(P,d).

This is [Hin26c, Proposition 7.17] in dimension 4 + 1.

*Proof.* [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]] with 𝔩 = 0 and [[lem:ii-d1-4-1]]. ∎

### Over ∂K⁺ {#sec:ii-d1-5}

Near ∂K⁺ use ρ_K := r/t_*, ρ_+ := r⁻¹, ω ([[sec:ii-b-3-1]]), W′ = ρ_+² and L := ρ_+⁻²P, as in [[prop:ii-d-3-2]] and
[[prop:ii-d-3-3]]. The family is 𝒳_K := (t_* ∂_(t_*), I), and U_0 is a small neighbourhood of ∂R_(∂K⁺,in) or of
∂R_(∂K⁺,out).

**Lemma {#lem:ii-d1-5-1}** (Commutators over ∂K⁺.) (a) (M) holds with i_0 = 1, w = ρ_K: 𝒱_b near ∂K⁺ is spanned by
𝒱_3b and t_* ∂_(t_*) ([[cor:ii-a-2-3]]), and t_* ∂_(t_*) is a commutator field ([[lem:ii-a-2-2]]), and ρ_K t_*
∂_(t_*) = r ∂_(t_*) ∈ 𝒱_3b has principal symbol a non-zero multiple of σ_3b, which is elliptic at both radial sets
(σ_3b < 0 there, [[def:ii-b-3-1]]). (b) (C) holds on U_0, with Q_11 of class 𝒬^1_1 whose coefficients carry a factor
ρ_K or ρ_K^(ℓ_K), so [[eq:ii-d1-2-8]] holds with equality at both radial sets, which lie over K⁺.

This is [Hin26c, Lemmas 7.19–7.20] in dimension 4 + 1.

*Proof.* (b) Write L = Σ_l p_l A_l with A_l ∈ Diff²_3b fixed and independent of t_*, p^♯_l the coefficients of
ρ_+⁻²P_0, independent of t_* in the coordinates (t_*, r, ω), and p̃_l ∈ ρ_+^(ℓ_+) ρ_K^(ℓ_K) C^((d_0;k))_(3b;b), the
coefficients of ρ_+⁻²(P − P_0) ([[def:ii-c-3-3]]). t_* ∂_(t_*) commutes with ρ_+ and annihilates p^♯_l.
[[lem:ii-a-2-2]] gives [X_1, A_l] = ρ_K A^♭_l X_1 + ρ_K A^♯_l, as in [[lem:ii-d1-4-1]]. Let Q_K ∈ C_b^∞Ψ^(−1)_3b be a
microlocal parametrix of ρ_K X_1 on Ū_0, I = Q_K ρ_K X_1 + R_K. Then

    [L, X_1] = −Σ_l (p_l ρ_K A^♭_l + ((X_1 p̃_l) A_l + p_l ρ_K A^♯_l) Q_K ρ_K) X_1
               − Σ_l ((X_1 p̃_l) A_l + p_l ρ_K A^♯_l) R_K,

which is (C) with Q_11 the first sum and R_1 the second; the factors ρ_K, ρ_K^(ℓ_K) appear in every coefficient of
Q_11. ∎

**Proposition {#prop:ii-d1-5-2}** (The radial sets over ∂K⁺ with b-regularity.) [[prop:ii-d-3-2]] and
[[prop:ii-d-3-3]] hold with H^((𝗍;k))_(e3b;b) in place of H^𝗍_e3b, with their thresholds [[eq:ii-d-3-3]] and
[[eq:ii-d-3-5]] unchanged, in the strong sense, uniformly for P with ε_(P,k) small, and in the tame form
[[eq:ii-d1-2-7]].

This is the analogue of [Hin26c, Propositions 7.6–7.7] in [Hin26c, Section 7.2.3], in dimension 4 + 1.

*Proof.* [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]] with 𝔩 = 0 and [[lem:ii-d1-5-1]]. The threshold [[eq:ii-d-3-5]] at
∂R_(∂K⁺,out) is an upper bound on the order, which every order of the iteration in [[lem:ii-d1-2-3]] meets, as there the
order s is fixed and only k increases. ∎

### The trapped set {#sec:ii-d1-6}

Over D near ∂Γ_0 ([[sec:ii-d-4]]) use (t_*, x), ρ_K = t_*⁻¹, W′ = 1, L = P. The family is 𝒳_Γ := (t_* ∂_(t_*), I),
and U_0 is a small neighbourhood of the component of ∂Γ_(K⁺) over ∂Σ⁺ or ∂Σ⁻; on it σ ≠ 0 ([[lem:ii-b-5-2]] (a)).

**Lemma {#lem:ii-d1-6-1}** (Commutators at the trapped set.) (a) (M) holds with i_0 = 1, w = ρ_K: t_* ∂_(t_*) is a
commutator field ([[lem:ii-a-2-2]]), and ρ_K t_* ∂_(t_*) = ∂_(t_*), whose principal symbol is a non-zero multiple of σ,
elliptic on Ū_0. (b) (C) holds with Q_11 decaying at K⁺, and (C2) holds with Q^(2) of order 0. So [[eq:ii-d1-2-8]]
holds with equality at ∂Γ_(K⁺).

This is [Hin26c, Lemma 7.21] in dimension 4 + 1.

*Proof.* (b) (C): as in [[lem:ii-d1-5-1]], with L = P = Σ_l p_l A_l, A_l ∈ Diff²_3b (cusp operators over D) independent
of t_*, p^♯_l independent of t_* and p̃_l ∈ ρ_K^(ℓ_K) C^((d_0;k))_(3b;b), and Q_K a microlocal parametrix of ∂_(t_*) on
Ū_0. (C2): from the formula for [L, X_1],

    [X_1, [X_1, L]] = Σ_l ((X_1² p̃_l) A_l + (X_1 p̃_l)[X_1, A_l] + (X_1 p_l) ρ_K (A^♭_l X_1 + A^♯_l)
                      − p_l ρ_K (A^♭_l X_1 + A^♯_l) + p_l ρ_K ([X_1, A^♭_l] X_1 + [X_1, A^♯_l])),

using X_1 ρ_K = −ρ_K. By [[lem:ii-a-2-2]] again, [X_1, A^♭_l] and [X_1, A^♯_l] are of the form ρ_K(·)X_1 + ρ_K(·), and
[X_1, A_l] = ρ_K A^♭_l X_1 + ρ_K A^♯_l. So every term is a second-order operator D, or a first-order operator D′
followed by X_1 (the terms p_l ρ_K² c X_1 X_1, c smooth, from p_l ρ_K [X_1, A^♭_l] X_1 are already of the form Q^(2)
X_1 X_1 with Q^(2) of order 0), with coefficients in ρ_K C^∞ + ρ_K^(ℓ_K) C^((d_0;k−2))_(3b;b). Let Q′ ∈ C_b^∞Ψ^(−2)_3b
be a microlocal parametrix of (ρ_K X_1)² = ∂_(t_*)² on Ū_0, I = Q′(ρ_K X_1)² + R′, and note (ρ_K X_1)² = ρ_K² X_1² −
ρ_K² X_1. Then

    D = (DQ′ρ_K²) X_1 X_1 − (DQ′ρ_K²) X_1 X_J + DR′,       D′X_1 = (D′Q_K ρ_K) X_1 X_1 + D′R_K X_1,

with DQ′ρ_K² and D′Q_K ρ_K of order 0 and class 𝒬^0_2, DR′ of class 𝒬^2_2, and D′R_K X_1 of the form R″X_1 with R″ :=
D′R_K of class 𝒬^1_2, both microsupported off Ū_0. This is (C2). ∎

**Proposition {#prop:ii-d1-6-2}** (The trapped set with b-regularity.) There are B, E, G with the properties (1)–(4) of
[[prop:ii-d-4-2]] such that for all s > s_0, k ∈ ℕ_0, α_K ∈ ℝ and χ̃ as there

    ‖Bu‖_((s;k),α_K) ≤ C_k (‖GPu‖_((s;k),α_K) + ‖Eu‖_((s+1;k),α_K) + ‖χ̃u‖_((s_0;k),α_K)),                {#eq:ii-d1-6-1}

in the strong sense, uniformly for P = P_0 and P of class ((d_0; k), (0, 0, ℓ_K)) with ε_(P,k) small, d_0 depending
only on s, s_0; and the tame estimate [[eq:ii-d1-2-7]] holds.

This is [Hin26c, Proposition 7.22] in dimension 4 + 1.

*Proof.* [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]] with 𝔩 = 1 and [[lem:ii-d1-6-1]]. [[lem:ii-d1-2-5]] gives (E_1) from
[[prop:ii-d-4-2]] for the systems L^(k), whose first-order part differs from P ⊗ Id by terms decaying at K⁺, so that
the condition ϑ_Γ < ½ν_min at ∂Γ_(K⁺) is that of P. ∎

### Proof of the global estimate with b-regularity {#sec:ii-d1-7}

*Proof of [[thm:ii-d1-1-1]].* For k = 0, [[eq:ii-d1-1-1]] is [[thm:ii-d-1-2]]. Let k ∈ ℕ, let u be as in
[[thm:ii-d1-1-1]], and for q ∈ ℕ_0 write

    ℛ_q := ‖Pu‖_((𝗌;q),(2α_I+2,α_++2,α_K)) + ‖u‖_((𝗌_0;q),(2α_I,α_+,α_K)),

the norms being those of [[eq:ii-d1-1-1]] on Ω_*, so that the right side of [[eq:ii-d1-1-1]] is ℛ_k and that of
[[eq:ii-d1-1-2]] is ℛ_k + ε_(P,k) ℛ_d. As in [[sec:ii-d-5]], u and Pu, extended by zero, are supported in {t_*^♭ ≥ 1};
below ‖·‖_(𝗍;k) carries the weights of u, and Pu is measured with the weights of [[eq:ii-d1-1-1]], which is the measure
of Lu = W⁻¹Pu with the weights of u. We say u is *controlled at order* (𝗍; k) on an open set V ⊂ ᵉ³ᵇS*M if ‖Bu‖_(𝗍;k)
≤ C_k ℛ_k, in the strong sense, for every B ∈ C_b^∞Ψ^0_e3b carried by χ with WF′(B) ⊂ V; and *tamely controlled* if
moreover, for every P as in the second half of [[thm:ii-d1-1-1]], ‖Bu‖_(𝗍;k) ≤ C_k(ℛ_k + ε_(P,k) ℛ_d), with C_k
depending on P only through a bound for ε_(P,d).

The proof is that of [[sec:ii-d-5]], step for step, with each estimate replaced by its version with b-regularity. The
flow is that of P, unchanged, so the backward curves are those used there; only the estimates change. The replacements
are these.

(P0_k) *Elliptic estimate.* Off the characteristic set, [[prop:ii-a-9-1]] with m = 2 controls u at every order (𝗍; k)
with 𝗍 ≤ 𝗌 + 1, and its tame version, [[prop:ii-a-9-8]], tamely.

(P1_k) *Propagation.* [[prop:ii-a-9-2]], and its tame version [[prop:ii-a-9-9]], replace [[thm:ii-a1-5-4]] in (P1) of
[[sec:ii-d-5]]. Their hypotheses on the flow, on the orders and on B, E, G are those of [[thm:ii-a1-5-4]], which (P1)
uses, and they give: control at order (𝗍; k) on V gives control at order (𝗍; k) at every ϖ whose backward 𝖧-curve
enters V in finite time, provided 𝖧𝗍 ≤ 0 along it and Pu is in H^((𝗍−1;k)) near it. The weights are put into the
operator as for k = 0 ([[sec:ii-d-1-2]]): the conjugation by a weight w adds to L terms whose coefficients are those of
L times the functions w⁻¹Vw and w⁻¹VV′w, V, V′ ∈ 𝒱_e3b, which are smooth with smooth b-derivatives
([[sec:ii-d1-1]]), so the conjugated operator has the form [[eq:ii-a-9-2]] at the regularity (d_0; k).

(P2), (P3) are unchanged: as u = 0 in {t_*^♭ < 1}, u is controlled there at every order (𝗍; k).

(R_k) *Radial sets and the trapped set.* [[prop:ii-d-3-1]], [[prop:ii-d-3-2]], [[prop:ii-d-3-3]], [[prop:ii-d-3-5]],
[[prop:ii-d-3-6]] and [[prop:ii-d-4-2]] are replaced by [[prop:ii-d1-4-2]], [[prop:ii-d1-5-2]], [[prop:ii-d1-5-2]],
[[prop:ii-d1-3-2]], [[prop:ii-d1-3-2]] and [[prop:ii-d1-6-2]]. Each is used with the orders of [[sec:ii-d-5]], which
are constant near the set, with the threshold conditions there, and with operators B, E, G having the properties
(1)–(4) of the proposition it replaces. The thresholds do not change with k: at the horizon by [[lem:ii-d1-4-1]] (c),
elsewhere by [[lem:ii-d1-3-1]] (d), [[lem:ii-d1-5-1]] (b) and [[lem:ii-d1-6-1]] (b).

*Step 1: finite times.* Let t^♯ and 𝒱_out be as in Step 1 of [[sec:ii-d-5]]. Along the backward curves used there,
(P1_k) at order (𝗌 + 1; k), with Pu ∈ H^((𝗌;k)), and (P2) control u at order (𝗌 + 1; k) near every compact subset of
∂Σ⁺ over Ω_* ∩ {t_*^♭ ≤ t^♯} disjoint from 𝒱_out.

*Step 2: the horizon and ∂R_(ℐ⁺,in,+).* [[prop:ii-d1-4-2]] and [[prop:ii-d1-3-2]] (for [[prop:ii-d-3-5]]), with the
orders (𝗌 + 1, 𝗌_0), 𝗌_0 > ½ + ϑ_𝓗 near ∂R_(𝓗⁺) and [[eq:ii-d-3-7]] from [[eq:ii-d-1-3]]. Their E have property (4),
so they lie at finite times, away from K⁺, resp. ι⁺, and operator wave front sets in small neighbourhoods of the two
sets, the second away from ∂R_(ℐ⁺,out); this is what Step 2 of [[sec:ii-d-5]] uses. So Step 1 bounds ‖Eu‖_(𝗌+1;k), and
u is controlled at order (𝗌 + 1; k) on neighbourhoods V_𝓗 of ∂R_(𝓗⁺) and V_I of ∂R_(ℐ⁺,in,+).

*Step 3: ∂R_(∂K⁺,in).* [[prop:ii-d1-5-2]] (for [[prop:ii-d-3-2]]), with the orders (𝗌 + 1, 𝗌_0) and [[eq:ii-d-3-3]].
Its E has property (4) and operator wave front set in a small neighbourhood of ∂R_(∂K⁺,in); the backward curves from it
are those of Step 3 of [[sec:ii-d-5]], which reach {t_*^♭ < 1} or enter V_I. (P1_k) at order (𝗌 + 1; k) and (P2) bound
‖Eu‖_(𝗌+1;k), and u is controlled at order (𝗌 + 1; k) on a neighbourhood V_K of ∂R_(∂K⁺,in).

*Step 4: the trapped set.* [[prop:ii-d1-6-2]] with the orders (𝗌, 𝗌_0), U_Γ small and Pu ∈ H^((𝗌;k)). Its E has
WF′(E) ∩ Γ^u_(K⁺) = ∅, and by Step 4 of [[sec:ii-d-5]] the backward curves from WF′(E) ∩ ∂Σ⁺ reach {t_*^♭ < 1} or
enter V_𝓗 ∪ V_K in locally bounded times. (P1_k) at order (𝗌 + 1; k) and (P2) bound ‖Eu‖_(𝗌+1;k), and u is controlled
at order (𝗌; k) on a neighbourhood V_Γ of ∂Γ_(K⁺).

*Step 5: ∂R_(∂K⁺,out).* [[prop:ii-d1-5-2]] (for [[prop:ii-d-3-3]]), with the orders (𝗌, 𝗌_0) and [[eq:ii-d-3-5]] at
the order 𝗌. Its E has WF′(E) ∩ ∂W_out = ∅, and by Step 5 of [[sec:ii-d-5]] the backward curves from it enter V_𝓗 ∪
V_K ∪ V_Γ ∪ V_I or reach {t_*^♭ < 1}. (P1_k) at order (𝗌; k) bounds ‖Eu‖_(𝗌;k), and u is controlled at order (𝗌; k)
on a neighbourhood V_(K,out) of ∂R_(∂K⁺,out).

*Step 6: ∂R_(ℐ⁺,out).* [[prop:ii-d1-3-2]] (for [[prop:ii-d-3-6]]), with t_(*,−) := ½, the orders (𝗌, 𝗌_0) and
[[eq:ii-d-3-9]] from [[eq:ii-d-1-3]]. By its property (4), WF′(E) ∩ ∂R_(ℐ⁺,out) lies over {t_*^♭ ≤ ½}, where u = 0,
and (P2) controls u at every order near it. The rest of WF′(E) lies in a punctured neighbourhood of ∂R_(ℐ⁺,out), from
which, by Step 6 of [[sec:ii-d-5]], the backward curves reach {t_* = 1} or {t_*^♭ < 1} or enter V_I ∪ V_(K,out).
(P1_k) at order (𝗌; k) bounds ‖Eu‖_(𝗌;k), and u is controlled at order (𝗌; k) on a neighbourhood V_(I,out) of
∂R_(ℐ⁺,out) ∩ {t_*^♭ ≥ ½}.

*Conclusion.* As in [[sec:ii-d-5]], every point of ∂Σ⁺ over supp χ has a neighbourhood on which u is controlled at
order (𝗌; k), by Step 1 or Step 6, or by (P1_k) at order (𝗌; k) from one of the sets of Steps 2–6 or from {t_*^♭ < 1};
the same holds on ∂Σ⁻ with the antipodal sets, for which [[sec:ii-d1-3]]–[[sec:ii-d1-6]] prove the same estimates.
Finitely many such B, with (P0_k) off Σ, are jointly elliptic over supp χ, and [[lem:ii-a-8-4]] (c) at (𝗌; k), with
‖χu‖_(−N′;k) ≤ ‖u‖_(𝗌_0;k), gives [[eq:ii-d1-1-1]], in the strong sense.

*Uniformity.* Each estimate used holds uniformly for P with ε_(P,k) small: [[prop:ii-d1-3-2]], [[prop:ii-d1-4-2]],
[[prop:ii-d1-5-2]] and [[prop:ii-d1-6-2]], and [[prop:ii-a-9-1]]–[[prop:ii-a-9-2]], whose constants are locally
uniform at the regularity (d_0; k). The backward segments are those of [[sec:ii-d-5]], whose persistence under
perturbation is shown there. d_0 is the largest of the numbers required by the steps at the orders 𝗌_0, 𝗌 and 𝗌 + 1
and by [[lem:ii-d1-2-3]]–[[lem:ii-d1-2-5]], and it does not depend on k. With [[rem:ii-d-1-3]], which applies here
because the constants of [[sec:ii-d1-3]]–[[sec:ii-d1-6]] depend on the model only through finitely many norms of its
coefficients and through the dynamical constants of [[ch:s05]], this proves [[eq:ii-d1-1-1]].

*The tame estimate [[eq:ii-d1-1-2]].* Let d be the largest of the numbers d of [[lem:ii-d1-2-4]] for the families and
orders of Steps 2–6 and of [[prop:ii-a-9-8]]–[[prop:ii-a-9-9]] at the orders 𝗌 + 1 and 𝗌. A tame estimate proved with
some d′ ≤ d holds with d, as ℛ_(d′) ≤ ℛ_d and ε_(P,d′) ≤ ε_(P,d). If ε_(P,d) is small, then P is of class ((d_0; d),
…) and ε_(P,q) ≤ ε_(P,d) for q ≤ d, so for k ≤ d [[eq:ii-d1-1-2]] follows from [[eq:ii-d1-1-1]]. Let k > d. Run Steps
1–6 and the conclusion with the tame versions: (P0_k) and (P1_k) with [[prop:ii-a-9-8]] and [[prop:ii-a-9-9]], and
(R_k) with [[eq:ii-d1-2-7]]. Each turns tame control on the sets where its E lies into tame control on a neighbourhood
of its own set. In its right side, the terms at k are at most C_k(ℛ_k + ε_(P,k) ℛ_d), by tame control, and those at d
at most C_d ℛ_d, by Steps 1–6 run at k = d without the tame versions, which control u on each E-set at the orders used
there (among them (𝗌 + 1; d)), with a constant depending on P only through ε_(P,d) ([[eq:ii-d1-1-1]] at d bounds only
the order 𝗌). The coefficient norm that multiplies the terms at d is ε_(P,k) in [[eq:ii-d1-2-7]]; in
[[prop:ii-a-9-8]]–[[prop:ii-a-9-9]] it is ‖𝐋‖_((d_0;k)), which is at most C′_k + Cε_(P,k) with C′_k depending only on
P_0, and the part C′_k C_d ℛ_d ≤ C′_k C_d ℛ_k joins the terms at k. The constants of those propositions depend on L
only through bounds at (d_0; d), that is, through ε_(P,d). [[lem:ii-a-8-4]] (c) has no coefficients of limited
regularity, so the conclusion is linear in the bounds of the steps. This gives [[eq:ii-d1-1-2]], with C_k depending on
P only through a bound for ε_(P,d). ∎

### Remarks on [Hin26c, Section 7] {#sec:s06-remarks}

The statements above differ from those of [Hin26c, Section 7] at the following places; each difference is accounted
for in the proofs given here.

(1) In [Hin26c, Proposition 7.9] the time cut-offs ψ_− = η(𝔐(t_(*,−) − t_*)) and ψ_+ = η(𝔐(t_* − t_(*,+))) have their
arguments reversed: with η = 0 on (−∞, −½] and η = 1 on [0, ∞) they equal 1 before t_(*,−) and after t_(*,+). Its
property (4), WF′(E) ∩ ∂R_(ℐ⁺,out) = ∅, does not hold as stated, as the term e_− lies on ∂R_(ℐ⁺,out) near t_* =
t_(*,−); [[prop:ii-d-3-6]] (4) restricts it to {t_*^♭ ≤ t_(*,−) − ¼}. For finite t_(*,+) the proof there needs H_G t_*
≥ 0 on the support of the commutant, for the symbol b_+ to be real. The cut-off to the characteristic set localises only
to a neighbourhood of it, and off it, at x_I = 0, 𝖧t_*^♭ = t_* ξ̂ takes negative values, as ξ̂ < 0 occurs there.
[[prop:ii-d-3-6]] is therefore stated for t_(*,+) = ∞ only. The case of finite t_(*,+) serves in Step 1 of the proof of
[Hin26c, Proposition 7.1], and [[sec:ii-d-5]] does without it: finite times are controlled away from ∂R_(ℐ⁺,out), and
Step 6 controls all of it at once.

(2) In the proof of [Hin26c, Proposition 7.9] the equality −4|η̂|²ξ̂ = −4(2 − ξ̂)ξ̂² should read −4|η̂|²ξ̂ = −2(2 −
ξ̂)ξ̂², as |η̂|² = ½ξ̂(2 − ξ̂) on the characteristic set; and in [Hin26c, (7.21)] the middle expression −2|η̂|²(ξ̂ − 2)
should read −4|η̂|²(ξ̂ − 2). In both, the final inequality, ≤ −q resp. ≥ q, holds as printed ([[prop:ii-d-3-5]],
[[prop:ii-d-3-6]]).

(3) In the proofs of [Hin26c, Propositions 7.17 and 7.22], the inclusions H^((s+1;k−2))_(3b;b) ⊂ H^((s;k−1))_(3b;b)
([Hin26c, (7.57)]) and H^((s+2;k−3))_(cu;b) ⊂ H^((s;k−1))_(cu;b) are false as inclusions. For k = 2 the first reads
H^(s+1)_3b ⊂ H^((s;1))_(3b;b), and over (K⁺)°, where ∂_(t_*) and ∂_x are 3b-vector fields and t_* ∂_(t_*) is a
b-vector field, v := a(x) b(t_*) e^(it_*) t_*^(−α_K−1), with a ∈ C_c^∞ and b a cut-off to {t_* ≥ 2}, lies in
H^(∞,α_K)_3b, while t_* ∂_(t_*) v = i a b e^(it_*) t_*^(−α_K) + (terms in H^(∞,α_K)_3b) lies in no H^(s,α_K)_3b, its
restrictions to the slabs {T ≤ t_* ≤ T + 1} having norms bounded below. What the arguments use is the estimate
‖v‖_(s+1;k−2) ≤ C‖v‖_(s;k−1), the reverse inclusion, which holds ((F1) of [[sec:ii-d1-1]]); [[lem:ii-d1-2-3]] and
[[lem:ii-d1-2-4]] use it in this direction.

(4) [Hin26c, (7.28)] prints the weights (2α_I + 2, α_+ + 2, α_K) on the last norm of u, ‖u‖_(s_0;d). The proof gives
the weights of u in [Hin26c, (7.27)], (2α_I, α_+, α_K), and [[eq:ii-d1-1-2]] states them. The printed weights demand
more decay of u, which an application with u at the weights of [Hin26c, (7.27)] does not supply.

(5) [Hin26c, Section 7.2] writes X⃗^α = X_1^(α_1) ⋯ X_(J−1)^(α_(J−1)) for multi-indices α and expands [X⃗^α, P] by
[Hin26c, Lemma 3.25] (which is [[lem:ii-a-9-3]]) as Σ_(β+γ=α) c_(βγ) (ad^β_X⃗ P) X⃗^γ ([Hin26c, (7.37), (7.43),
(7.61)]). Near ℐ⁺ the fields do not commute: the rotation fields, and in dimension 3 + 1 also [X_1, X_2] ∈ x_I C^∞
([Hin26c, (7.31)]). The expansion (7.37) is exact even so, as deleting positions from an ordered power leaves an
ordered power. But X_j X⃗^γ is not X⃗^(γ+e_j), and the argument there needs it to read Q_(ij) X_j X⃗^γ u as a component
of u^(k); so that system closes only modulo reordering commutators, which lie in the span of the family and can be
absorbed. With words ([[sec:ii-d1-2]]) the expansion (F2) is exact and the commuted system closes without reordering.
At the horizon, over ∂K⁺ and at the trapped set the fields commute, and words and multi-indices agree up to counting,
with the coupling [[eq:ii-d1-2-2-prime]], whose horizon coupling is diagonal.

(6) [Hin26c, Section 7.2] applies its Propositions 7.4, 7.6–7.9 and 7.10 to the commuted equations, operators with
off-diagonal first-order terms; for the radial point estimates it refers to its Remark 7.5, and for the trapping
estimate it gives no argument. [[lem:ii-d1-2-5]] proves the estimates for such systems under the sign condition
[[eq:ii-d1-2-8]], and [[sec:ii-d1-3]]–[[sec:ii-d1-6]] verify that condition; at the trapped set this rests on the form
of the proof of [[prop:ii-d-4-2]], in which the operator enters only through its principal symbol, through 𝔭 and
through one commutator.

(7) [Hin26c, Section 6] states the regularity C^(d_0−1,ℓ_K)_cu for the perturbed stable and unstable hypersurfaces.
[[sec:ii-d-4]] uses only ϕ^u ∈ C^(d_0−1) and ϕ^s ∈ C^(d_0−2) ([[prop:ii-c1-3-4]]), and chooses d_0 accordingly.
