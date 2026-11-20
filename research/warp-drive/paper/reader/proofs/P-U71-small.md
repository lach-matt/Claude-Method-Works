#### The smallness orders and the loss of the Nash–Moser step {#sec:cs-small}

The proof of [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] with d the largest of the d's of [[lem:iii-k-2-2]],
[[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]]. Each of these d's is at least the loss of the estimate of its result and at
least the orders at which its proof asks U small. For [[lem:iii-k-2-3]] one of these orders is the order d′_0 at which
the proof of [[thm:iii-j2-4-2]] asks U small, and d′_0 ≥ d_0 + d_Φ with d_0 = d_* + D (*The constants* in the proof of
[[lem:iii-k-2-3]], and [[lem:iii-j2-2-3]]), where d_* is the order of the smallness conditions of
[[ch:s19]]–[[ch:s23]] and D is the d of [[thm:iii-j2-4-1]]. This subsection sums the second line of [[eq:ec-upper]]
level by level ([[lem:cs-sharp]]), evaluates the orders of the smallness conditions and d_* ([[lem:uc-small-orders]]),
and bounds the d of [[thm:iii-k-3-2]] ([[prop:uc-d-small]]).

Throughout, the point, the index sets and the choices are those of [[thm:uc-integer]]; N_ι, N̄_Λ, k̄_max, C_lev, R_b,
I_lev, I_base, X_12, T_11 and T_12 are the numbers of [[sec:cs]]; d_T = 20,180 is the loss of [[thm:iii-i-5-3]] at
every b ∈ ℬ̄_* ([[thm:fwd-loss]], [[cor:fwd-near-b0]]); ‖β‖_j = ‖h‖_(𝒳^j) + |p⃗| + ‖q‖_(𝒬^j) is the background norm of
[[sec:iii-j2-1]]; and

    K̄ := 122,076,389,376,829,     R_base := 20,183 + 1,914 + I_base = 1,435,970,471,299,470,597,059.

A *base* is [[prop:iii-i8-4-1]], with its forward solution, at a level in (2, 3) that it reaches from its α_0 by one
level step without transition face round, for a background of K⁺-order at least a♭_K. The bases used are that of
Step 1 of the proof of [[thm:iii-i14-3-1]] at α_1, at b also in [[prop:iii-i15-2-5]]; that of the proof of
[[thm:iii-i11-4-1]] at the α′ of [[def:cs-choices]] (f); and those of the proofs of [[lem:iii-i11-3-3]] and
[[lem:iii-i13-2-3]], whose admissible α′ we take below 2 + ε_g − 2ε, with one level step from an admissible
α_0 ∈ (2, α′), as those proofs and that of [[prop:iii-i8-4-1]] allow. Each of these levels is below
τ_0 = 2 + ε_g − 2ε, so its level step has no transition face round ((6) of Step 1 in the proof of [[lem:cs-rest]]). By
[[lem:cs-iterations]] (b), with the count of Step 1 in the proof of [[lem:cs-rest]], a base with all its rounds, steps
and windows charged is charged at most R_base along every chain.

**Lemma {#lem:cs-sharp}** (The single-step losses summed level by level.) The number K of the levels β_1, …, β_K of
[[thm:iii-i14-3-1]] satisfies K ≤ K̄, and

    d_acc ≤ D_♭,     d_R ≤ D_♭,     D_♭ := D_e + K̄ C_lev + 469R_b + 466(R_b + 1) + C_*,
    D_♭ = 26,192,562,436,215,872,034,699,391,908,492,342,632,997,875,951,546 < 2.6193·10⁴⁹,          {#eq:cs-sharp}

with D_e and C_* of [[thm:uc-integer]].

*Proof.* *The levels.* At the choice of [[def:uc-choice]], α_1 = β_0 < β_1 < ⋯ < β_K = α, and every spacing
β_(k+1) − β_k is at least Δβ_0 ([[lem:uc-admissible]]); so KΔβ_0 ≤ α − α_1 < 2 + ε_K, as α ≤ 4 + ε_K and α_1 > 2.
With ε_K = 16,416·10⁻¹⁸ and Δβ_0 = 16,383,184,416·10⁻²⁴ ([[eq:uc-deltas]]), (2 + ε_K)/Δβ_0 is
2,000,000,000,000,016,416,000,000/16,383,184,416, and

    16,383,184,416 · 122,076,389,376,829 = 2,000,000,000,000,012,824,296,864,
    16,383,184,416 · 122,076,389,376,830 = 2,000,000,000,000,029,207,481,280;

so K < 122,076,389,376,830, that is, K ≤ K̄.

*The bound.* By [[lem:uc-admissible]] and [[lem:uc-gaps]], [[prop:ec-upper]] holds with the T_2 and W of
[[eq:uc-t2-w]], and its first line is less than D_e ([[prop:uc-explicit]]). Its second line is
Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0. There every c(β_k) is at most max(497, C_lev) = C_lev ([[lem:cs-levels]]),
c_b ≤ 469 and c′_b ≤ 466 ([[lem:cs-base]]), and c_0 is at most the integer of [[eq:cs-cstar]], which is less than C_*
([[lem:cs-rest]], [[prop:cs-cstar]]). The number N_b of [[lem:ec-counts]] (f) is at most 1/Δβ_0 + 1
([[eq:ec-upper-counts]]), and 16,383,184,416 · 61,038,194,688,415 > 10²⁴, so N_b < 61,038,194,688,416 < R_b. Hence
the second line is at most K̄C_lev + 469R_b + 466(R_b + 1) + C_*, and d_acc ≤ D_♭. By [[lem:uc-dr]], d_R satisfies
[[eq:ec-upper]] with the same first line and with c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 in place of c(β_k), c_b, c′_b and
c_0; these satisfy the same bounds ([[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-rest]]), so d_R ≤ D_♭.

*The integer.* K̄C_lev = 26,192,562,436,215,228,354,699,390,649,792,285,562,280,875,951,080, and
469R_b + 466(R_b + 1) = 28,626,915,800,000,000 + 28,443,801,200,000,466 = 57,070,717,000,000,466. Adding these,
D_e = 1,258,700,000,000,000,000,000,000 and C_* = 643,680,000,000,000,000,000,000,000,000,000,000 gives the integer of
[[eq:cs-sharp]], whose leading digits are 2.619256. ∎

*Orders.* We say that a condition on the background β = (h, p⃗, q) has *order j* if it holds whenever ‖β‖_j is less than
one positive number and ‖β‖_(j+D) is less than another, D being the d of [[thm:iii-j2-4-1]]. As the norms are
non-decreasing in the order, a condition of order j has order j′ for every j′ ≥ j; and as d_0 = d_* + D
([[lem:iii-j2-2-3]]), every condition of order at most d_* holds on the ball ‖β‖_(d_0) < δ_𝔹 of [[thm:iii-j2-4-1]] once
δ_𝔹 is small. The bound at the order j + D is the one that the proof of [[lem:iii-j2-2-3]] uses when it asks the
solutions u_j entering a comparison to be bounded at a fixed order.

**Lemma {#lem:uc-small-orders}** (The orders of the smallness conditions.) At the computational point, with the index
sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]]:

(a) the conditions of [[thm:iii-i-5-3]] and [[cor:iii-h2-5-1]], at the backgrounds of [[lem:iii-j2-2-1]] (a), have
order d_T + 3 = 20,183;

(b) in [[eq:s20-d]] one may take k_1 = 10 and k_0 = k̄_0 := 20,602 + 466R_b = 28,443,801,200,020,602, and so the d of
[[eq:s20-d]] equal to k̄_0 + 2; the conditions of [[ch:s20]] then have order k̄_0 + 2, and k̄_0 + 5 at the backgrounds
h + h_rem(q) + h_tot(p⃗);

(c) the conditions that [[ch:s20]], [[ch:s21]] and [[prop:iii-i8-4-1]] place on the background of a base, at a base
point with parameter b ∈ ℬ̄_* included ([[prop:iii-i15-2-8]], [[prop:iii-i15-2-12]]), have order 2R_base + 16;

(d) let the fixed seminorm of the forcing class of a level β of [[thm:iii-i14-3-1]] (in [[lem:iii-i8-3-2]],
[[lem:iii-i11-3-2]], [[lem:iii-i13-2-2]], [[def:iii-i15-2-3]], [[lem:iii-i15-2-4]] and Step 3 of the proof of
[[prop:iii-i15-2-5]]), and the seminorm in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0, be taken at the
regularity ρ at which the maps that read the coefficients from the forcing of the step are bounded. Then
ρ ≤ C_lev − 11 + I_lev at the levels, and ρ < T_12 in Steps 4′ and 4; and every condition of Steps 2–4′ of the proofs
of [[thm:iii-i14-3-1]] and [[prop:iii-i15-2-5]] has order ρ + 14, or ρ + R_base + 16 when it is read at a reference
point (0, p⃗_b) with b ≠ b₀;

(e) hence every condition named in the proof of [[lem:iii-j2-2-3]] has order at most

    D_* := T_12 + 14 = 214,558,790,360,104,032,305,147,901,608,827,158 < 2.14559·10³⁵,               {#eq:uc-small}

so the largest of these orders, d_*, satisfies d_* ≤ D_*, and the order m of the proof of [[lem:iii-k-2-3]]
satisfies m + 14 ≤ d_*.

*Proof.* *Three facts.* (F1) Let A be one of the families of [[lem:iii-j2-2-1]] (b), its sources and its operators
applied to a fixed section or to a solution, and let β, β′ be backgrounds with ‖β‖_14 and ‖β′‖_14 small. Then for
every k

    ‖(A_β − A_β′)u‖_k ≤ C_k ‖β − β′‖_(k+11) ‖u‖_(k+2),                                            {#eq:uc-small-diff}

with C_k depending only on upper bounds for ‖β‖_(k+14) and ‖β′‖_(k+14). Indeed, the proof of [[prop:uc-dbg]] writes
A_β = A′_(p⃗) + Σ_(|γ|≤2) Φ_γ(x, p⃗, w)D^γ_b with w = (h̃, D_bh̃, D²_bh̃), h̃ := h + h_tot(p⃗) + h_(b,rem)(q),
‖h̃‖_m ≤ C_m‖β‖_(m+3), A′_(p⃗) with coefficients smooth in (x, p⃗), and Φ_γ smooth with Φ_γ(x, p⃗, 0) = 0. The
coefficients of A′_(p⃗) − A′_(p⃗′) are O(|p⃗ − p⃗′|) with all their derivatives, and Φ_γ(x, p⃗, w) − Φ_γ(x, p⃗′, w′) is
the integral over the segment of ∂_(p⃗)Φ_γ·(p⃗ − p⃗′) + ∂_wΦ_γ·(w − w′). Here ∂_(p⃗)Φ_γ vanishes at w = 0, and ∂_wΦ_γ is
a function smooth in (x, p⃗) plus one vanishing at w = 0; so [[lem:ii-g-4-1]] (2)–(3) with d = 3 bound the difference at
the order j by C_j(‖w − w′‖_j + |p⃗ − p⃗′| + ‖w_s‖_(j+6)(‖w − w′‖_0 + |p⃗ − p⃗′|)), w_s on the segment. The product with
D^γ_bu is bounded by [[lem:ii-g-4-1]] (2), which reads the coefficient at the orders 3 and k + 3. As
‖w − w′‖_j ≤ C_j‖β − β′‖_(j+5), with C_j depending on a bound for ‖q′‖_(𝒬^(j+5)), as h_(b,rem)(q) is linear in q and
smooth in b and h_tot(p⃗) is smooth in p⃗, and ‖w_s‖_j ≤ C_j(‖β‖_(j+5) + ‖β′‖_(j+5)), this gives [[eq:uc-small-diff]].
The weights and the coefficients at the faces are treated as in the proof of [[prop:uc-dbg]].

(F2) In each comparison below, a solution u of an earlier entry of [[sec:iii-j2-3]] enters only through terms (A_β −
A_β′)u, at a rotating b also through (L_(b₀) − L_b)u, whose coefficients are O(|b − b₀|), and is needed at the order ρ +
2, ρ the regularity of the seminorm. By the induction in the proof of [[thm:iii-j2-4-1]], over the entries of
[[sec:iii-j2-3]] in their order and, in [[thm:iii-i14-3-1]], over its levels, the solution maps of the earlier entries
are tame with losses at most D. Their forcings are F, which lies in every order, and background sources times
finite-dimensional coordinates, of order-j norm at most C_j(1 + ‖β‖_(j+11)) per unit coordinate ([[prop:uc-dbg]]). So
‖u‖_(ρ+2) is bounded by the data of the step once ‖β‖_(ρ+13+D) is bounded.

(F3) At b₀ and the background 0, L_(0,0) = L_(b₀) ([[lem:iii-i7-2-5]] (a), [[lem:iii-i11-3-2]]), so the forcing
f′ = G − (L − L_b)u of Step 0 of the proofs of [[lem:iii-i8-3-2]], [[lem:iii-i11-3-2]] and [[lem:iii-i13-2-2]] is G
itself, and the coefficients at (0, 0) are the maps that read them from the forcing, applied to G. With the seminorm at
the regularity ρ of (d), |S^(0,0)_ν(G)| ≤ C‖G‖_ρ.

*(a)* The proof of [[thm:iii-i-5-3]], in (iii), asks ‖P − P_0‖_((0;d)) small for the d of [[thm:ii-f1-1-1]], with
d + 5 = d_T, through ‖P − P_0‖_((0;d)) ≤ C(|S| + ‖h‖_(𝒳^(d_T))), and [[eq:s19-time-hyp]] asks |S| + ‖h‖_(𝒳³) small;
[[cor:iii-h2-5-1]] adds |b − b₀|, a component of p⃗. At the backgrounds h̃ of [[lem:iii-j2-2-1]] (a),
‖h̃‖_(𝒳^m) ≤ C_m‖β‖_m, and ‖h̃‖_(𝒳^m) ≤ C_m‖β‖_(m+3) at h + h_rem(q) + h_tot(p⃗). So these conditions are smallness of
‖β‖_(d_T+3), and d_T + 3 = 20,183 ([[thm:fwd-loss]], [[cor:fwd-near-b0]]).

*(b)* *k_1.* The proof of [[lem:iii-i4-4-2]] writes Ṡ = Π_bf′, with Π_bf′ the 𝒮_1-component of
L̃_b(0)⁻¹(f̂^♭(0), 0, 0), where f^♭ = f′ − L_bu_I and u_I is the construction of [[prop:iii-i1-3-1]] for L_b applied to
f′. These maps are fixed. By [[lem:cs-sum]] (a), [[lem:cs-null]] (a) and [[lem:cs-elem]] (a)–(c), f′ ↦ f^♭ is charged
at most 6 + 2 = 8, f^♭ ↦ f̂^♭(0) at most 1 ([[prop:ii-g1-3-3]] (1)), L̃_b(0)⁻¹ at most 1 and the component 0. So Π_b
has loss 10 at the weights of that proof, and it is bounded from the order 10 into 𝒮_1: k_1 = 10 serves. *k_0.* The
proof of (a) there bounds ‖f′‖_(k_1) ≤ ‖f‖_(k_1) + ‖(L − L_b)u‖_(k_1) ≤ ‖f‖_(k_1) + C‖u‖_(k_1+2), by
[[eq:iii-i-4-2]], and bounds u in [[eq:iii-i2-5-2]] by f through [[prop:iii-i2-5-1]]; so k_0 = k_1 + 2 + L_u, with L_u
the loss of f ↦ u. That map is the forward solution operator, charged at most 20,183 at every background of the class
([[lem:cs-elem]] (e)), [[prop:iii-i1-2-1]] at its start (407, [[lem:cs-null]] (b)), and its steps, each charged at
most c′_b ≤ 466 ([[lem:cs-base]], whose count does not depend on where the step is run). The steps raise α′_K from ½ to
α_K < 1 by min(a_K − 2, α_K − α′_K) (the proof of [[lem:ec-counts]] (f)), and a_K − 2 ≥ a♭_K − 2 ≥ Δβ_0 at every
background at which the base is run ([[def:uc-choice]], [[lem:uc-admissible]]); so they number at most
1/(2Δβ_0) + 1 < R_b. Hence L_u ≤ 20,183 + 407 + 466R_b and k_0 ≤ 12 + 20,590 + 466R_b = k̄_0. Then [[eq:s20-d]] asks
d ≥ max(20,180, k̄_0 + 2, 10 + 20,180 + 7) = k̄_0 + 2. The conditions of [[ch:s20]] are smallness of |S| and of
h + h^(−1)(S), or h + h_tot(p⃗) ([[lem:iii-i7-2-5]] (b)), in 𝒳^d, which is smallness of ‖β‖_(k̄_0+2), and of
‖β‖_(k̄_0+5) at h + h_rem(q) + h_tot(p⃗) ([[lem:iii-j2-2-1]] (a)).

*(c)* The proofs of [[lem:iii-i4-4-2]], [[prop:iii-i15-2-8]], [[lem:iii-i7-4-1]], [[prop:iii-i15-2-12]],
[[cor:iii-i7-4-6]], [[lem:iii-i8-3-2]], [[lem:iii-i8-3-3]] and [[prop:iii-i8-4-1]] ask their smallness conditions in
fixed norms of forcing classes (the norm of [[lem:iii-i4-4-2]] (a), ‖·‖_𝒴 and ‖·‖_(𝒴^S_(α,α_+)) of [[sec:iii-i7-4]],
‖·‖_(𝒴(α)) of [[sec:iii-i8-1]]), in which a map of the base reads coefficients, boost parameters or the parameters Q
from the forcing. Each such map is the part of a base that follows the forcing, so it is charged at most R_base, and it
is bounded from the order R_base into its finite-dimensional target, the coefficient functionals being bounded by the
order 0 ([[lem:cs-elem]] (a)). At a reference point (0, p⃗_b) with b ≠ b₀ the read carries also a term
C|p⃗_b|‖u_j − u‖, which the proof of [[lem:iii-i11-3-3]] bounds by (i) of [[prop:iii-i8-4-1]] at a level below 3, a
base map, from the forcing at the order of the seminorm plus 2 + R_base. So these norms are needed at regularities at
most 2R_base + 2. The bounds of (i) of [[prop:iii-i8-4-1]] and of (2) of the proof of [[prop:iii-i15-2-12]] are taken in
second norms, ‖·‖^+_(𝒴(α)) of [[sec:iii-i8-1]] and ‖·‖^+_𝒴, whose regularity exceeds that of a norm above by at most
2 + R_base: 2 for the count of Step 0, and R_base for the base map that bounds the solution. So they too are needed at
regularities at most 2R_base + 2. These bounds, and those of [[lem:iii-i7-2-5]] (c), enter the conditions only as bounds
of solutions and parameters by the data of the step, which (F2) supplies. In these norms, the second ones included, the
proofs ask: bounds of background terms by ‖h‖ + |p⃗ − p⃗_b| (or by ‖h‖), as in [[lem:iii-i8-2-6]] (b),
[[lem:s21-motions-at-b]], [[lem:iii-i15-2-7]] and (1) of the proof of [[prop:iii-i15-2-12]], and with ‖q‖ added in the
bound by which the proof of [[prop:iii-i15-2-5]] obtains [[eq:s25-motions-small]]; the counts
‖(L − L′)u‖ ≤ C(‖h‖ + |p⃗ − p⃗′|)‖u‖ of Step 0 of the proof of [[lem:iii-i8-3-2]], of the proofs of [[lem:iii-i7-4-1]]
and [[prop:iii-i15-2-8]], and of (2) of the proof of [[prop:iii-i15-2-12]], with u bounded; and the conditions of (a)
and (b). By (F1) at a regularity ρ ≤ 2R_base + 2, the first two kinds are bounds by ‖β − β′‖_(ρ+11), β′ being
(0, p⃗_b, 0) or (0, 0, 0), so that ‖β − β′‖_j ≤ 2‖β‖_j; their constants and the bounds of u need ‖β‖_(ρ+14+D) bounded
((F2)). So they have order at most 2R_base + 16, as have those of (a) and (b), since 20,183 and k̄_0 + 5 are less than
R_base.

*(d)* *The reads.* At a level β ∈ (3, α], [[lem:iii-i11-3-2]] and [[lem:iii-i13-2-2]] read the coefficients S_ν and
u^rot (at b also A_b, [[def:iii-i15-2-3]]) from the forcing f′ of Step 0 of their proofs by maps fixed by L_b. These
are the applications of the level step after its Step 0, with its iterations, so by [[lem:cs-iterations]] (a) they are
charged at most C_lev − 11 + I_lev, and with the coefficient functionals they are bounded from that order into the
coordinates. At a level β ∈ (2, 3), [[lem:iii-i8-3-2]] is charged at most 497 ([[lem:cs-levels]] (a)), and its
iterations, a window loop of at most 1,470,302 windows charged at most 16 and fewer than 1/Δτ + 1 < 6,847,261,002
transition face rounds charged at most 3 ([[lem:ec-counts]] (b), (e), [[lem:ec-round-charges]], [[prop:uc-explicit]]),
are charged at most 23,524,832 + 20,541,783,006 < I_lev; so ρ ≤ C_lev − 11 + I_lev there too. In Step 4′, C^rot is read
through [[thm:iii-i12-3-1]] at (0, 0) and p⃗′_0 through [[thm:iii-i11-4-1]], charged at most C_lev − 11 + I_lev + X_12
and T_11 ([[lem:cs-rest]]), both less than T_12; Step 4 applies [[thm:iii-i12-3-1]] again.

*The comparisons.* Each condition of Steps 2–4′ that the proof of [[lem:iii-j2-2-3]] names compares reads at a
background β and at a reference β_r, which is (0, 0, 0) or, at a base point with parameter b, (0, p⃗_b, 0). It does so
either through S^β_ν(G) − S^(β_r)_ν(G_r) = S^(β_r)_ν(R) with R = G − G_r − (L_β − L_(β_r))u (the display in the proof of
[[lem:iii-j2-2-3]], and the proofs of [[lem:iii-i8-3-3]], [[lem:iii-i11-3-3]] and [[lem:iii-i13-2-3]]), or through the
direct bounds |S^β_ν(G)| + |A_b(G)| ≤ C‖G‖_ρ + C(‖h‖ + |p⃗|)‖u‖ of [[lem:iii-i13-2-2]], [[def:iii-i15-2-3]] and
[[lem:iii-i15-2-4]], whose last term is the count of ‖(L_(h,p⃗) − L_b)u‖_ρ, as in Step 3 of the proof of
[[prop:iii-i15-2-5]]. The forcings compared, and R, consist of: background terms (r^ν, E^ν, f^S, f^b, f^s1, f^ν, Δ_q
and R_q, and for ℛ(U) also e_S and e_(S⁰)) applied to fixed sections times finite-dimensional coordinates or to bounded
solutions; their differences at β and β_r; the terms (L_β − L_(β_r))u; and the finite-dimensional coordinates fixed at
the lower levels and at the base, which tend to their values at β_r by the same argument at those levels, an induction
over the levels that ends at the base, (c). A_k is the coefficient of the new coordinates in such an expression, and
the derivative of C^rot is read in the same way. By (F1) at the order ρ, every background contribution is bounded by
‖β − β_r‖_(ρ+11) times the coordinates or times ‖u‖_(ρ+2), which (F2) bounds once ‖β‖_(ρ+13+D) is bounded. The factor
‖h‖ + |p⃗| of the direct bounds is such a bound, as |p⃗| ≤ ‖β‖_0, its component |b − b₀| being also made small by the
choice of ℬ_*; R_q and Δ_q are bounded by C‖q‖ in this way ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]), q being a
component of β; and the bounds of [[lem:iii-i9-2-6]] are of this kind, its continuity asking h ∈ 𝒳^k with k ≥ 5 only.
At b₀ the reference read is bounded on the order ρ by (F3), so the condition has order at most ρ + 14. At a reference
point (0, p⃗_b) with b ≠ b₀ the read carries also C|p⃗_b|‖u_j − u‖_(w), which the proof of [[lem:iii-i11-3-3]] bounds by
(i) of [[prop:iii-i8-4-1]] at a level α′ < 3, a base map, from R_j at the order ρ + 2 + R_base; so such a condition has
order at most ρ + R_base + 16.

*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,871,940,942,598,941,194,134, which is less than T_12. Those of
(d) are at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point
(0, p⃗_b) with b ≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]],
at b₀, and at a rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates
being the A_b read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as
X_12 = 51,246,486,662,857,739,996,772 exceeds R_base. The convention "h small" of [[sec:iii-i7-1]], kept in
[[sec:iii-i8-1]], in [[sec:iii-i9-1]] and so at the base points of [[ch:s22]], and the convention "q small" of
[[sec:iii-i14-1]] each fix one order for all their uses: the largest of the orders that those uses ask. The uses lie
in the bases, at the levels and in Steps 4′ and 4, and each asks an order that (a)–(d) bound, by (F1) at the
regularity of its seminorm. So every order is at most D_*, and so is their largest, d_*. The order m of the proof of
[[lem:iii-k-2-3]] is the largest regularity ρ of the seminorms in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0,
and the condition asked in that seminorm has an order at least m + 14 by (c) and (d); so m + 14 ≤ d_*. The integer:
T_12 = C_lev + I_lev + X_12 = 214,558,790,360,104,032,305,147,901,608,827,144, and D_* = T_12 + 14. ∎

**Remark {#rem:uc-small-reading}** (Fixed seminorms that also bound the remainders.) [[sec:iii-i8-1]] takes the
regularity of its fixed seminorm so large that the maps from the forcing to the coefficients and to the remainder are
bounded in it, and [[lem:iii-i11-3-2]] chooses its seminorms in the same way. If this is required at every level, the
regularities grow downwards through the levels, and d_* is still bounded. Let ρ_k be the regularity of the fixed
seminorm of the forcing class of the step from β_(k−1) to β_k. The step maps the forcing to the remainder ũ ∈ 𝒵_(β_k),
which is measured in the seminorm of the hypothesis of the next step, and that seminorm must bound (L − L_b)u and R_qu
in the seminorm of the next forcing class, two orders lower. The remainder map is part of the step, so by
[[lem:cs-iterations]] (a), and the count in the proof of [[lem:uc-small-orders]] (d) for the levels below 3,
ρ_k ≤ ρ_(k+1) + 2 + C_lev − 11 + I_lev, and ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev,
Step 4′ reading the solution at α at an order below T_12 + 2. So ρ_k ≤ T_12 + K̄(C_lev + I_lev − 9) for every k, by
[[lem:cs-sharp]]. The norms of the base must bound its maps into the seminorm of the hypothesis of the first step, so
they are needed at regularities at most ρ_1 + 2 + R_base, and at most ρ_1 + 2R_base + 4 with the terms at a reference
point (0, p⃗_b). By (F1)–(F3) and the proofs of (c)–(e), every order is then at most

    D′_* := T_12 + 18 + K̄(C_lev + I_lev − 9) + 2R_base
         = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207 < 2.6193·10⁴⁹,

and d_* ≤ D′_*. Here K̄(C_lev + I_lev − 9) = 26,192,562,436,215,228,354,699,394,833,207,300,964,646,683,858,927, to which
T_12 + 18 and 2R_base = 2,871,940,942,598,941,194,118 are added.

**Proposition {#prop:uc-d-small}** (The loss with which the Nash–Moser theorem is applied.) At the computational point,
with the index sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]], let d_F be the number
that [[def:ec-accounted-loss]] assigns to the construction of [[thm:iii-j2-4-1]] at the base point Ψ(U) of the proof of
[[lem:iii-k-2-3]], with which that proof obtains [[eq:iii-j2-4-1]], and let d_* be the largest of the orders of the
smallness conditions named in the proof of [[lem:iii-j2-2-3]], the fixed seminorms being those of
[[lem:uc-small-orders]] (d) or those of [[rem:uc-small-reading]]. Then:

(a) [[lem:iii-k-2-3]] holds with d := max(d_R, d_* + d_F + d_Φ), and [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] hold
with d := d_Φ + 8. So the proof of [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] with

    d_NM = max(d_R, d_* + d_F + d_Φ),     d_F ≤ d_R,     d_acc ≤ d_R ≤ d_NM;                          {#eq:uc-d-small}

(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + 1,038,326,399,999,940 =
26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644, so d_NM < 2.6193·10⁴⁹, and N_NM = 21d_NM + 6 ≤
550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 < 5.5005·10⁵⁰;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + 1,038,326,399,999,940 =
52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693 < 5.2386·10⁴⁹, and N_NM < 1.10009·10⁵¹;

(d) in either case d_NM < D_acc and N_NM < 21D_acc + 6, with D_acc of [[thm:uc-integer]]; and every lower bound for
d_acc and N_NM in this chapter holds for d_NM and N_NM.

*Proof.* (a) *[[lem:iii-k-2-3]].* By *The constants* in its proof, its d must be at least d_R, d′_0, d_BG and m + 5,
where d′_0 is the order at which the proof of [[thm:iii-j2-4-2]], run in β^Ψ, asks U small. That proof asks: the
smallness of ‖β̂‖_(d_0), with d_0 = d_* + d_F ([[lem:iii-j2-2-3]], the d of [[thm:iii-j2-4-1]] being d_F there), which
(i) of *The constants* bounds by C‖β^Ψ‖_(d_0+d_Φ); the smallness of ‖β^Ψ‖ at the order that [[lem:iii-j2-1-2]] (b), (e)
asks of the compositions in β^Ψ, whose total loss is d_R; and, for D_UΦ in Steps 1–3, only |U_0| small, as D_UΦ is
smooth in U_0 and affine in U_1 ([[rem:iii-j-2-5]]), and the proof of [[thm:iii-j-2-4]] asks only |U_0| < ε_0, the order
d_Φ of its statement being below d′_0 in any case. So d′_0 := max(d_* + d_F + d_Φ, d_R) serves. Also d_BG = 11 < d_* and
m + 5 < d_* ([[lem:uc-small-orders]] (e)). So d := max(d_R, d_* + d_F + d_Φ) serves, and [[eq:s27-rinv]] holds with it,
as it holds with d_R and the norms are non-decreasing in the order. *The other two.* Their losses d_Ψ and d_FM are at
most d_Φ + 8 ([[lem:uc-phi-loss]]). Their proofs ask U small through |U_0| ([[thm:iii-j-2-4]]); through the smallness in
H³ of w = (h″, D_bh″, D²_bh″) that [[lem:ii-g-4-1]] (3) asks, and through [[lem:iii-j2-2-4]] at the faces, whose d_1 = 3
serves, its proof using [[lem:ii-g-4-1]] with d = 3 only, both of which ‖Φ(U)‖_8 ≤ C‖U‖_(𝒟^(8+d_Φ)) controls (the proof
of [[lem:uc-phi-loss]]); and at ℐ⁺ through [[cor:iii-i-4-2]] for Φ(U) ([[thm:iii-j-2-4]]), which asks the order 3 of
h + h_rem(q) + h_tot(p⃗), and through [[cor:iii-c-5-3]] for Ψ(U) ([[lem:iii-k-2-2]] (c)), whose smallness is read at
an order at most 5 ([[prop:iii-c-4-4]]).
Besides, [[prop:iii-j2-4-3]] states its bounds for ‖U‖_(𝒟^(3d)) < ε_0, which the domain |U|_(3d) < δ of the proof of
[[thm:iii-k-3-2]] provides. So d := d_Φ + 8 serves for both. The largest of the three d's is max(d_R, d_* + d_F + d_Φ),
as d_* ≥ 8. Finally, the construction of ℛ(U) applies that of [[thm:iii-j2-4-1]] at Ψ(U) and assembles U′ from its
output by maps of non-negative charge (the proof of [[lem:iii-k-2-3]]), so d_F ≤ d_R; and d_acc ≤ d_R by the proof of
[[thm:loss-d]].

(b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ 1,038,326,399,999,940
([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + 1,038,326,399,999,940, the
integer printed: D_♭ + D_* = 26,192,562,436,216,086,593,489,752,012,524,647,780,899,484,778,704, and adding
1,038,326,399,999,940 gives it. Its leading digits are 2.619256, and 21 times it plus 6 is the integer printed, with
leading digits 5.500438.

(c) is (b) with D′_*: D_♭ + D′_* = 52,385,124,872,431,314,948,189,146,848,603,889,688,145,109,831,753, and adding
1,038,326,399,999,940 gives the integer printed, with leading digits 5.238512; 21 times it plus 6 has the leading
digits 1.100087.

(d) D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 exceeds the integer of (c) by
104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307, so d_NM < D_acc in either case, and
N_NM = 21d_NM + 6 < 21D_acc + 6. The lower bounds of [[thm:loss-d]] (ii), [[cor:uc-two-offsets]] and
[[thm:uc-integer]] are bounds for d_acc, carried to d_NM and N_NM by d_NM ≥ d_acc and N_NM = 21d_NM + 6; by (a) they
hold for the d_NM of [[eq:uc-d-small]]. ∎

The bound (b) rests on [[lem:uc-small-orders]] (d), in which the fixed seminorms are those of the reads; (c) holds
under the larger reading of [[rem:uc-small-reading]]. The integer bound of [[thm:uc-integer]] for d_NM and N_NM holds
under both.

### Placement, and the texts that change

*Placement.* The subsection above, from its heading through the paragraph after [[prop:uc-d-small]], is inserted in
[[ch:explicit-constants]] at the end of [[sec:cs]], after [[rem:cs-sharpness]] and before the heading of
[[sec:ec-linear]]. It defines the labels sec:cs-small, lem:cs-sharp, eq:cs-sharp, lem:uc-small-orders, eq:uc-small,
eq:uc-small-diff, rem:uc-small-reading, prop:uc-d-small and eq:uc-d-small, none of which is defined elsewhere. Every
number of [[ch:explicit-constants]] stands, among them D_acc, 21D_acc + 6 and the lower bounds. The definition of d_NM
changes from the largest of the losses of the three results to the largest of their d's, which [[prop:uc-d-small]]
bounds, and the following sentences of [[ch:explicit-constants]] change with it; [[rem:uc-missing]] gains one sentence
(text 14). No sentence of the title page,
[[ch:introduction]], [[ch:theorems]], [[ch:s27]] or [[ch:scope]] needs to change: each states its bounds for the loss d
with which the settling proof applies the Nash–Moser theorem, which is d_NM, and they hold for it by
[[prop:uc-d-small]] (d).

*1. In [[sec:ec-accounted]],* replace the paragraph that begins "[[thm:ii-g-2-1]] is applied in the proof of" and ends
"([[thm:loss-d]])." by:

[[thm:ii-g-2-1]] is applied in the proof of [[thm:iii-k-3-2]] with N_NM = 21d_NM + 6, where d_NM is the largest of
the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], as [[prop:uc-d-small]] fixes them. Each of
these is at least the loss of the estimate of its result, that of [[lem:iii-k-2-3]], a construction, accounted by
[[def:ec-accounted-loss]] and the other two as their proofs fix them, and at least the orders at which its proof asks U
small; for [[lem:iii-k-2-3]] these include the order d′_0 ≥ d_* + D + d_Φ of its proof, with d_* of [[lem:iii-j2-2-3]],
D the d of [[thm:iii-j2-4-1]] and d_Φ the loss of U ↦ Φ(U). As (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]] of the
right inverse of [[lem:iii-k-2-3]], whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc ([[thm:loss-d]]).

*2. In [[thm:loss-d]],* replace the four lines from "[[def:ec-accounted-loss]], and d_NM the loss with which" through
"d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:" by:

[[def:ec-accounted-loss]], and d_NM the loss with which the proof of [[thm:iii-k-3-2]] applies the Nash–Moser theorem
[[thm:ii-g-2-1]]: the largest of the d's of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]] that
[[prop:uc-d-small]] fixes, each at least the loss of its estimate, that of [[lem:iii-k-2-3]] accounted by
[[def:ec-accounted-loss]], and the orders at which its proof asks U small. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]
hold with d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:

*3. In the paragraph after (iii) of [[thm:loss-d]],* replace the two lines from "the index sets. At the computational
point [[thm:uc-integer]] evaluates" through "at most one below 3.30029 × 10⁵¹." by:

the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc
and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.

*4. In the proof of [[thm:loss-d]],* replace the three lines from "([[eq:ii-g-2-5]]). *d_NM ≥ d_acc.* Hypothesis (iii)"
through "is one of the three whose largest is d_NM. By" by:

([[eq:ii-g-2-5]]). *d_NM ≥ d_acc.* Hypothesis (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]], with the loss d_NM, of the
right inverse Zℛ(U) of the proof of [[thm:iii-k-3-2]], where ℛ(U) is that of [[lem:iii-k-2-3]] and the multiplication Z
loses nothing; so d_NM, the largest of the d's of the three results, is at least the loss of ℛ(U), the loss of
[[eq:iii-j2-4-2]] for it. By

*5. In [[prop:ec-delta-cap]],* replace the line "d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]]
(d ≥ d_acc, [[thm:loss-d]]), and let the Nash–Moser" by:

d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] (d ≥ d_R ≥ d_acc, [[thm:loss-d]], [[prop:uc-d-small]]),
and let the Nash–Moser

The proof of [[prop:ec-delta-cap]] uses only d ≥ d_acc and stands unchanged.

*6. In (4) of [[rem:ec-upper-open]],* replace the three lines from "through the charge max(2, d_BG). For d_NM, and so
for N_NM," through "so that d_NM equals it ([[thm:uc-integer]]). Given ε_K, the explicit part" by:

through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are
at most 62N_Λ + 10 < 1.04·10¹⁵ ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of [[lem:iii-k-2-3]] satisfies
[[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at
which these results ask U small, and with them d_NM ([[thm:uc-integer]]). Given ε_K, the explicit part

*7. In the opening of [[sec:uc-close]],* replace the line "loss of the map Φ of [[thm:iii-j-2-4]], which governs the
two other components of d_NM ([[lem:uc-phi-loss]]). Memberships" by:

loss of the map Φ of [[thm:iii-j-2-4]], which governs the other two losses ([[lem:uc-phi-loss]]). Memberships

and replace the two lines from "and d_NM are at most an integer D_acc < 1.57157·10⁵⁰, the largest single-step loss
being below 6.4368·10³⁵" through "against the lower bound 1.2497·10²⁴; [[rem:uc-missing]] states what the bound rests
on. Throughout" by:

and d_NM are at most an integer D_acc < 1.57157·10⁵⁰, the largest single-step loss being below 6.4368·10³⁵
([[prop:cs-cstar]]) and the orders of smallness being bounded in [[sec:cs-small]], against the lower bound
1.2497·10²⁴; [[rem:uc-missing]] states what the bound rests on. Throughout

*8. In [[lem:uc-phi-loss]],* replace its title "(The loss of Φ and the two other components of d_NM.)" by "(The loss
of Φ and the losses of the other two results.)", and replace the line "[[lem:ii-g-4-1]], are at most d_Φ + 8 =
62N_Λ + 10, and d_NM = max(d_R, d_FM, d_Ψ), with d_R ≥ d_acc the accounted loss" by:

[[lem:ii-g-4-1]], are at most d_Φ + 8 = 62N_Λ + 10, and d_NM ≥ max(d_R, d_FM, d_Ψ), with d_R ≥ d_acc the accounted loss

In its proof, replace the three lines from "[[prop:iii-j3-5-4]] follows the proof of [[thm:iii-j-2-4]] step by step;
so d_Ψ ≤ d_Φ + 8 as well. d_NM is the largest" through "21d_NM + 6 is the regularity of" by:

[[prop:iii-j3-5-4]] follows the proof of [[thm:iii-j-2-4]] step by step; so d_Ψ ≤ d_Φ + 8 as well. d_NM is at least
each of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of [[lem:iii-k-2-3]]
accounted by [[def:ec-accounted-loss]] and at least d_acc ([[thm:loss-d]]), and N_NM = 21d_NM + 6 is the regularity of

*9. In (ii) of [[thm:uc-reduction]],* replace "(ii) d_NM = max(d_R, d_FM, d_Ψ) with" by "(ii) d_NM ≥ max(d_R, d_FM,
d_Ψ) with"; the line keeps its length.

*10. In [[lem:uc-dr]],* replace "If d_R > 62N_Λ + 10, then d_NM = d_R." by "If d_R > 62N_Λ + 10, then
d_R = max(d_R, d_FM, d_Ψ)."; and in the last sentence of its proof replace "d_NM = max(d_R, d_FM, d_Ψ) with
d_FM, d_Ψ ≤ 62N_Λ + 10." by "d_FM, d_Ψ ≤ 62N_Λ + 10." Both lines become shorter.

*11. In [[thm:uc-integer]],* replace the display line of [[eq:uc-integer]] by:

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM := D_acc,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,                 {#eq:uc-integer}

replace the line "The two other components of d_NM satisfy d_FM, d_Ψ ≤ 1,038,326,399,999,948. At a level β ∈ (3, α],"
by the two lines:

The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 1,038,326,399,999,948, and the finer bounds
d_acc, d_R < 2.6193·10⁴⁹ and d_NM < 5.2386·10⁴⁹ hold ([[lem:cs-sharp]], [[prop:uc-d-small]]). At a level β ∈ (3, α],

and in its proof replace the three lines from "c_* < C_*. As d_R ≥ d_acc ≥ 3R > 1.2497·10²⁴" through "d_FM and d_Ψ are
[[lem:uc-lambda]] (d). N_NM = 21d_NM + 6 by [[thm:loss-d]]. The statements at the levels above 3 are" by:

c_* < C_*; and d_R ≥ d_acc ([[thm:loss-d]]). By [[prop:uc-d-small]] (d), d_NM < D_acc, so d_NM ≤ D_NM, and the finer
bounds are [[lem:cs-sharp]] and (b), (c) there; the bounds for d_FM and d_Ψ are [[lem:uc-lambda]] (d).
N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The statements at the levels above 3 are

*12. In [[rem:cs-sharpness]],* replace its last three lines, from "K < 1.22077·10¹⁴ ([[rem:ec-upper-point]]), instead
of by M_c C_*," through "constructions produce are bounded in this paper only by k̄(λ).", by:

K < 1.22077·10¹⁴ ([[rem:ec-upper-point]]), instead of by M_c C_*, gives d_acc, d_R < 2.62·10⁴⁹ ([[lem:cs-sharp]]). The
bound is crude in another way as well: n_ι and n_K count every pair (λ, k) with k ≤ k̄(λ), while the logarithmic
orders that the constructions produce are bounded in this paper only by k̄(λ).

*13. In the opening of the chapter,* replace the two lines from "products ([[def:uc-choice]], [[def:cs-choices]]),
d_acc and d_NM are at most" through "most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies
outside the set on which [[thm:settling]]" by:

products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]

*14. In [[rem:uc-missing]],* replace its last line, "the logarithmic orders that the level steps produce, which this
paper bounds only by k̄(λ) ([[rem:cs-sharpness]]).", by:

the logarithmic orders that the level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]). The
bound for d_NM rests in addition on the orders of the smallness conditions, which [[lem:uc-small-orders]] bounds for
the fixed seminorms of its (d), and [[rem:uc-small-reading]] for the larger ones that [[sec:iii-i8-1]] describes
([[prop:uc-d-small]]).
