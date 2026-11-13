## Tame estimates and exact weights {#ch:s24}

This chapter proves two properties of the forward solutions of [[ch:s19]]–[[ch:s23]] that the nonlinear theorem of
[[ch:s27]] needs in order to apply the Nash–Moser theorem [[thm:ii-g-2-1]]. The first, in
[[sec:iii-j2-1]]–[[sec:iii-j2-4]], is tameness: the solution map of the forward problem with parameters
([[thm:iii-i14-3-1]]) and the right inverse of the linearised equation in the data ([[thm:iii-j1-2-1]]) satisfy
estimates linear in the highest norm, with a loss of b-regularity independent of the order, and the map
U ↦ P_5(Φ(U)) has tame bounds. [Hin26, Remark 11.13, p. 226] asserts that the tameness of the initial tame estimate
propagates through all the arguments; [Hin26, Corollary 11.66, pp. 294–295] and [Hin26, Theorem 12.8, p. 312] state the
tame estimates without proof, and [Hin26, Section 13.1, Step 3 (2)–(3), pp. 321–322] uses them. Here the propagation is
proved: a calculus of tame families ([[sec:iii-j2-1]]); the elementary families, with finite-order forms of the model
statements that [[ch:s16]]–[[ch:s23]] state at b-regularity ∞ ([[sec:iii-j2-2]]); the inventory of every construction
of [[ch:s19]]–[[ch:s23]] as a composition of these ([[sec:iii-j2-3]]); and the theorems ([[sec:iii-j2-4]]).

The second, in [[sec:iii-j3-1]]–[[sec:iii-j3-6]], is that the solution map of [[thm:iii-i14-3-1]] and the right inverse
of [[thm:iii-j1-2-1]] lose nothing in the weights. A right side at the fixed weights (ℓ_I + 1, 5 + ε_+, α) at
(𝓘⁺, ι⁺, K⁺) gives a solution at (ℓ_I, 3 + ε_+, α), with one fixed admissible α ([[thm:iii-j3-5-3]],
[[thm:iii-j3-5-5]]). This is how [Hin26] states its Corollary 11.66 (pp. 294–295) and Theorem 12.8 (p. 312), at the
weights (4 + ε_I, 5 + ε_+, 4 + ε_K) and (3 + ε_I, 3 + ε_+, 4 + ε_K). The Nash–Moser theorem asks for one pair of Banach
scales, and the forward map gains nothing in the weights ([[prop:iii-j2-4-3]]); with the exact weights the tame
estimates hold on one pair of scales ([[cor:iii-j3-6-6]]).

*Dimension 4 + 1.* (1) [Hin26] omits the intermediate tame statements; they are written out here. (2) One model map
loses b-regularity growing with the order: [[cor:ii-g1-4-5]] (high frequencies), with the loss ⌈kδ⌉ + ℓ,
δ = δ_Γ(−η). The operator 2L_b is strongly trapping admissible at every b near b_0 ([[prop:iii-h2-1-1]]), so for each
order k the trapping data can be taken with (k + 1)δ ≤ 1 ([[cor:iii-h2-1-2]]), and the loss is at most ℓ + 1 at every
k ([[lem:iii-j2-2-1]] (f)). (3) Choices that depend on the order (the trapping data, and the low-energy radius c_k of
[[cor:iii-h-4-2]]) enter only decompositions of a solution that does not depend on them, so they cost constants, not
derivatives ([[rem:iii-j2-2-2]]). (4) The losses in the weights are removed where they arise; nothing is improved after
the fact. Of the statements of [[ch:s19]]–[[ch:s23]] that take a right side at an exact weight and conclude an order
"w−", only those whose loss reaches a final weight matter: every other one feeds an open condition with fixed room. Those
losses have three roots. (a) At K⁺, [[cor:iii-g2-4-3]] writes the ι⁺-terms in powers of log t_*. At the corner
t_*⁻¹ = ρ_+ρ_K, so each log t_* hides a log ρ_K, and a logarithm times a conormal function of exact weight lies in no
weighted L²-b space of that weight. In that convention [[cor:iii-g2-4-3]] cannot be applied at the exact weight, the
two classes being incomparable ([[rem:iii-j3-3-1]]). Written in powers of log ρ_+, the convention of [Hin26, Definition
2.8, p. 48] in which the classes of [[ch:s19]]–[[ch:s23]] are defined, the same construction is exact
([[cor:iii-j3-3-2]]). (b) [[lem:iii-i12-2-2]] and [[lem:iii-i12-2-1]] bound their outputs pointwise, at K⁺ and at the
corner of ι⁺ and K⁺, which gives only the L²-weight w−; at the final weight they are proved in L² ([[lem:iii-j3-4-4]],
[[lem:iii-j3-4-5]] and [[lem:iii-j3-4-7]]). The Fourier characterisation [[prop:iii-a-4-2]] is itself exact and only
transmits the loss of (a) ([[prop:iii-j3-4-1]]). (c) At ι⁺, the level-2 margin η_2 < ε_+ of [[prop:iii-i11-3-1]] and
the 5ε of [[lem:iii-j1-1-1]] are choices, not losses of an estimate: at the closed endpoint of (G⁺) every map is exact
([[prop:iii-j3-4-3]]), as in Part 4 of the proof of [Hin26, Theorem 11.59, pp. 289–291]. At 𝓘⁺ every class and every
main statement is already exact. (5) The K⁺-weight is one fixed admissible α, not the number 4 + ε_K; α = 4 + ε_K itself
is admissible off a finite set of ε_K ([[def:iii-j3-1-3]], (A_K)). (6) The conditions (Ex2)–(Ex4) of [[def:iii-j3-1-3]],
each excluding finitely many values, are of the kind of (G⁺) and of admissibility, and are not in [Hin26]; (Ex1) is (G⁺)
at its closed endpoint. No condition on spec_ι⁺(L̄) beyond (G⁺) is needed, as no improvement after the fact is made.

*Base points.* Throughout, the base point has black hole parameter b ∈ ℬ̄_*, the neighbourhood of b_0 of
[[sec:iii-h2-0]], shrunk so that [[lem:iii-i15-1-2]] and [[prop:iii-i15-2-5]] hold on it. The results of
[[ch:s19]]–[[ch:s23]] are used at b, with constants uniform in b ([[sec:s23-base-points]] (1)–(3), and the statements
at b of [[ch:s19]]–[[ch:s22]]): L_(b_0), g_(b_0) near K⁺, the states, towers and companions at b_0 and the index set
ℰ_ind are replaced by those at b, derivatives in b are taken at b, and the v1 terms of exponent of real part at most 2
are the rotation rows with the assigned coordinates of [[def:iii-i15-2-3]]. At a rotating b the solution map of
[[thm:iii-i14-3-1]] is the one constructed in [[prop:iii-i15-2-5]], and those of [[thm:iii-i11-4-1]] and
[[prop:iii-i13-2-4]] are used only inside [[lem:iii-i15-2-4]] and [[prop:iii-i15-2-5]], the latter with q = 0 being
their form there.

*The inner radius.* Every result of the chapter holds with the inner radius r₀ = r_♭ ∈ (0, ½R₁] of [[def:s12-radii]]
as a parameter, with constants that depend on it. No result names the inner radius: all work on Ω_* = cl_M{t^♭_* ≥ 1}
([[sec:iii-i-1]]) with the spaces of [[ch:s04]], extendible at the inner boundary, and with the theorems of
[[ch:s04]]–[[ch:s10]], which hold at every such radius. The regions used are bounded by fixed radii that do not depend
on r_♭ ({r ≥ 1}, and {r ≥ 2} near the corner of ι⁺ and K⁺) or by multiples of t_* ({r ≤ t_*/8}, {t_*/8 < r < t_*/2}),
and the loops, levels and windows of [[sec:iii-j2-3]] are fixed by weights at infinity and at K⁺, not by the inner
radius.

*Notation.* As in [[ch:s23]]. In particular w_+ := 5 + ε_+; ρ_+ and ρ_K are the defining functions of ι⁺ and K⁺ near
their corner, ρ_+ = 1/r and ρ_K = R = r/t_*, so t_*⁻¹ = ρ_+ρ_K there ([[sec:iii-i2-1]]); μ runs over the indicial roots
of L̂_(b_0)(0) ([[prop:iii-f1-2-3]]), which do not depend on b ([[lem:iii-i15-1-1]] (P2)), and −μ is read as −Re μ; the
non-real roots have real part below −101 or above 1, outside every interval used. The neighbourhoods ℬ_1 ⊃ ℬ_* of b_0
and their closures are the B_1 ⊃ B_* of [[sec:iii-h2-0]]. The rows of the towers are indexed by ρ ∈ ℛ′, as in
[[ch:s23]] (Y_ρ, d_ρ, w_ρ, T_ρ); [[ch:s22]] writes ψ for this index.

### Tame families {#sec:iii-j2-1}

A *background* is β = (h, p⃗, q) with h ∈ 𝒳^∞, p⃗ ∈ 𝒫 and q ∈ 𝒬^∞ in the classes of the statement at hand
([[sec:iii-i-1]] for h alone; [[sec:iii-i14-1]], with 𝒫 enlarged by the rotation rows; for [[thm:iii-j1-2-1]],
β = Φ(U)), and

    ‖β‖_k := ‖h‖_(𝒳^k) + |p⃗| + ‖q‖_(𝒬^k).

The black hole parameter b of β is given by the component b − b_0 of p⃗. A *graded space* is a family of Banach spaces
E^k, k ∈ ℕ₀, with continuous inclusions E^(k+1) ↪ E^k of norm at most 1 ([[rem:ii-g-2-2]]), and E^∞ := ⋂_k E^k. The
spaces of [[ch:s19]]–[[ch:s23]] are of this kind: weighted b-Sobolev spaces of b-regularity k; partially polyhomogeneous
ones, normed by the order-k norms of their finitely many coefficients and of the remainder; finite-dimensional spaces
(E^k = E); and direct sums.

Several of those spaces carry orders read "w−" ([[sec:iii-i14-1]], [[def:iii-j-1-1]]): they are intersections over a
loss ε > 0, and their order-k spaces are Fréchet, not Banach. Such a space is taken here at a fixed loss: E^k_ε is the
Banach space with every order w− replaced by w − ε, and E^∞_ε := ⋂_k E^k_ε. For ε″ ≤ ε, E^k_(ε″) ⊂ E^k_ε continuously,
the weight being larger. A statement of [[ch:s19]]–[[ch:s23]] from a "w−" space to a "w−" space is a continuous linear
map between Fréchet spaces (closed graph theorem), so for every loss ε of the output and every order k there is a loss
ε′(ε, k) ∈ (0, ε] of the input at which it is bounded. Decreasing ε′(ε, k) keeps the bound, so ε′(ε, ·) is taken
non-increasing in k. Then the spaces E^k_(ε′(ε,k)), k ∈ ℕ₀, form a graded space (renormed as in [[rem:ii-g-2-2]]), the
input space of the statement at the output loss ε; in a composition the output of one statement is taken in the graded
input space of the next. For the statements whose proofs choose every margin from the loss the output is to have, ε′
can be taken independent of k: [[prop:iii-i2-5-1]], [[lem:iii-i6-1-2]]–[[lem:iii-i6-1-4]] and [[prop:iii-i6-2-1]], the
level-3 loop of [[prop:iii-i11-3-1]] (the margin ε_ind − ε), the levels β_k of [[thm:iii-i14-3-1]], [[lem:iii-j1-1-1]]
(η_2 := ε_+ − 3ε, which gives the ι⁺-order 3 + ε_+ − 5ε) and [[cor:ii-g1-4-5]] (β_scf := β′_I + ε); no margin there
depends on k. For the other statements the independence of k is not shown, and it is not needed: at the exact weights
of [[sec:iii-j3-1]] the input and the output are taken at the loss 0 for every k ([[cor:iii-j3-6-6]]).

Below, ε ∈ (0, ε_1] is fixed, where ε_1 > 0 satisfies

    5ε_1 < ε_+ − max(η^0_2, η_1, ε_K) = ε_+ − η^0_2,        ε_1 < α − 4,

with η_1 and η^0_2 the values of η_1 and η_2 fixed in [[sec:iii-i11-1]] and [[sec:iii-i12-1]]
(ε_K < η_1 < η^0_2 < ε_+), and is so small that every statement of [[ch:s19]]–[[ch:s23]] used below holds at every loss
ε ∈ (0, ε_1]. A statement proved for every small ε off a finite set ([[sec:iii-i11-1]]) holds at every
ε ∈ (0, ε_1], as its output space at the loss ε contains that at every smaller loss. By the first condition the choice
η_2 := ε_+ − 3ε of [[lem:iii-j1-1-1]] is admissible: η_2 ∈ (η^0_2, ε_+) and 2ε < 3ε = ε_+ − η_2. It also gives
1 + ε_+ − 5ε > 1 + ε_K, so the level-3 tf-weight τ_3 = 1 + ε_+ − 5ε of [[lem:iii-j1-1-1]] exceeds 1 + ℓ_3, and the
K⁺-weight 2 + ε_+ − 5ε of the level-3 pieces exceeds α − 2, as ℓ_3 ≤ ε_K and α ≤ 4 + ε_K. By the second, h_rem(q) has
the K⁺-order α − 2 − ε > 2 ([[lem:iii-j2-2-1]] (a)), and the zf-weight ℓ_3 = α − 4 − ε of level 3 in the proof of
[[prop:iii-i11-3-1]] is positive. [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] take their output at the loss ε and their
input in the graded space of the losses ε′(ε, k) that the statement they estimate assigns.

**Definition {#def:iii-j2-1-1}** (Tame families.) Let E, G be graded spaces, d_0, d ∈ ℕ, δ_𝔹 > 0, and
𝔹 := {β : ‖β‖_(d_0) < δ_𝔹}. A family (T_β)_(β∈𝔹) of linear maps E^∞ → G^∞ is *tame with loss d* if for every
k ∈ ℕ₀ there is C_k with

    ‖T_β e‖_(G^k) ≤ C_k (‖e‖_(E^(k+d)) + ‖β‖_(k+d) ‖e‖_(E^d)),        β ∈ 𝔹,  e ∈ E^∞.            {#eq:iii-j2-1-1}

A family (v_β) in G^∞ is *tame with loss d* if ‖v_β‖_(G^k) ≤ C_k (1 + ‖β‖_(k+d)) for every k.

**Lemma {#lem:iii-j2-1-2}** (Closure.) Let δ_𝔹 ≤ 1.

(a) Sums of families tame with loss d are tame with loss d; a family tame with loss d is tame with every loss d′ ≥ d.

(b) If (T_β), E → G, is tame with loss d, (S_β), G → H, with loss d′, and d_0 ≥ d + d′, then (S_β T_β) is tame with
loss d + d′.

(c) (*Finite rank.*) If ℓ_β : E^∞ → ℂ^m satisfies |ℓ_β e| ≤ C ‖e‖_(E^d) on 𝔹, and v¹_β, …, v^m_β are tame with loss d,
then e ↦ Σ_i (ℓ_β e)_i v^i_β is tame with loss d. In particular a family of linear maps between finite-dimensional
spaces, bounded on 𝔹, is tame with loss 0.

(d) (*Fixed maps.*) A linear map T independent of β that is bounded E^(k+d) → G^k for every k is tame with loss d.

(e) A composition of m families, each tame with loss at most d, is tame with loss md if d_0 ≥ md; here m is fixed,
independent of k.

(f) (*Regularity statements.*) If a statement takes e ∈ E and an a priori solution u in a space E′ to u ∈ G, and the
family (e, u) ↦ u, E ⊕ E′ → G, is tame with loss d, then for (S_β), E → E′, tame with loss d′, the map e ↦ u = S_β e
into G is tame with loss d + d′. A statement of this kind independent of β that is a membership statement between
Banach spaces at each order k has, by the closed graph theorem, the bound ‖u‖_(G^k) ≤ C_k (‖e‖_(E^(k+d)) +
‖u‖_(E′^(k+d))), and is then tame with loss d.

(g) [[def:iii-j2-1-1]] asks one bound for each k: a family whose order-k bound is proved with choices made for the
order k ([[rem:iii-j2-2-2]]) is tame with loss d if each of these bounds has the loss at most d.

*Proof.* (a) is immediate, the norms being non-decreasing in k. (b) By [[eq:iii-j2-1-1]] for S and then for T,

    ‖S_β T_β e‖_k ≤ C_k (‖T_β e‖_(k+d′) + ‖β‖_(k+d′) ‖T_β e‖_(d′))
                 ≤ C_k (‖e‖_(k+d+d′) + ‖β‖_(k+d+d′) ‖e‖_d + ‖β‖_(k+d′) (‖e‖_(d+d′) + ‖β‖_(d+d′) ‖e‖_d)),

and ‖β‖_(d+d′) ≤ ‖β‖_(d_0) < 1, ‖β‖_(k+d′) ≤ ‖β‖_(k+d+d′) and ‖e‖_d ≤ ‖e‖_(d+d′) give [[eq:iii-j2-1-1]] with loss
d + d′. (c) ‖Σ_i (ℓ_β e)_i v^i_β‖_k ≤ C ‖e‖_d Σ_i ‖v^i_β‖_k ≤ C_k ‖e‖_d (1 + ‖β‖_(k+d)), which is at most the right
side of [[eq:iii-j2-1-1]]. (d) is [[eq:iii-j2-1-1]] without its second term. (e) follows from (b) by induction. (f) The
map e ↦ (e, S_β e) is tame with loss d′ by (a), and (b) applies. (g) is [[def:iii-j2-1-1]]. ∎

### The elementary families {#sec:iii-j2-2}

**Lemma {#lem:iii-j2-2-1}** (The elementary tame families.) For d_0 large and δ_𝔹 small the following are tame, with
losses independent of k, and with constants that depend on the base point through finitely many seminorms, continuous
in b ∈ ℬ̄_*.

(a) (*Forward solutions.*) The forward solution operators of the operators L^(g,g_0), g = g_0 + h̃, used in
[[ch:s19]]–[[ch:s23]]: h̃ = h ([[thm:iii-i-5-3]], at b with continuity in (b, S, h) by [[cor:iii-h2-5-1]]);
h̃ = h + h^(−1)(S) and h + h_tot(p⃗) (the operators L_(h,S) of [[ch:s20]] and L_(h,p⃗) of [[ch:s21]]; the gauge
modifications δ*_(g_0,E_C) ϑ_tot(p⃗) do not enter them, D_h removing them, [[lem:iii-i4-2-5]] and [[lem:iii-i7-2-5]]
(a)); and h̃ = h + h_rem(q) + h_tot(p⃗) (Step 0 of the proof of [[thm:iii-i14-3-1]], and of [[prop:iii-i15-2-5]]),
between the spaces of [[eq:iii-i-5-1]] and its target. For h̃ = h this is [[eq:iii-i-5-2]]. In general h̃ lies in the
class of [[thm:iii-i-5-3]] (h_rem(q) has K⁺-order (α − 2)− > 2, [[rem:iii-i14-3-2]] (1)), with ‖h̃‖_(𝒳^k) ≤
C_k ‖β‖_(k+d) ([[lem:iii-i4-2-5]], [[lem:iii-i7-2-5]], [[lem:iii-i8-2-5]], [[lem:iii-i9-2-5]], and [[def:iii-i14-1-2]]
with the towers fixed), and the background g_0 (g_S, or g_p⃗, smooth in p⃗) and h_tot(p⃗) add to P − P_0 coefficients
smooth in p⃗; so the proof of [[thm:iii-i-5-3]] gives ‖P − P_0‖_((0;k+d)) ≤ C_k ‖β‖_(k+d+5), and [[eq:iii-i-5-2]] with
‖β‖ in place of ‖h‖.

(b) (*Background coefficients.*) u ↦ (L^(g,g_0) − L_b)u, u ↦ R_q u, Δ_q, the sources f^S_(h,p⃗), f^b_(h,p⃗),
f^s1_(h,p⃗), f^ν_(h,p⃗), r^ν_(h,p⃗), L_b h_rem(q) and the remainder L̃ of [[lem:iii-i1-1-1]], between the weighted spaces
of [[eq:iii-i-4-2]], [[lem:iii-i9-2-6]] and [[lem:iii-i14-2-2]]–[[lem:iii-i14-2-4]]; and the errors E^ν_(h,p⃗) of
(P6) in [[lem:iii-i15-1-1]], bounded by C|b − b_0||W| in a fixed seminorm. Each is a b-differential operator of order
at most 2 whose coefficients are polynomial in the background, g⁻¹ and their derivatives (or such a coefficient applied
to a fixed section); by [[cor:ii-a-9-7]] and [[lem:ii-a-9-5]], with [[lem:ii-g-4-1]] for the nonlinear functions of the
background,

    ‖Au‖_k ≤ C_k (‖u‖_(k+2) + ‖β‖_(k+d) ‖u‖_d)

for ‖β‖_(d_0) small, the weights adding as in the cited membership statements ([[lem:iii-j2-2-4]] in the partially
polyhomogeneous spaces).

(c) (*Finite-dimensional algebra and coefficients.*) The inverses (S^(−1)_(h,S))⁻¹ ([[cor:iii-i4-4-3]], at b with
the bound of [[prop:iii-i15-2-8]]), (S^(−1)_(h,p⃗))⁻¹ ([[cor:iii-i7-4-6]], at b with the bound of
[[prop:iii-i15-2-12]]), T_(h,p⃗)⁻¹ ([[prop:iii-i8-4-1]], [[thm:iii-i11-4-1]]), the inverses
(−id + A_k)⁻¹ of the elimination (Step 3 of the proofs of [[thm:iii-i14-3-1]] and [[prop:iii-i15-2-5]]), at b_0 the
inverse of C^rot in W⃗′^rot (Step 4′ of the proof of [[thm:iii-i14-3-1]]), and (z − 3/2 − Ā)⁻¹ ([[prop:iii-i1-3-1]]):
bounded on 𝔹 by the cited statements (close to ±id, or fixed). The coefficient functionals (Ṡ, S_ν, C^(k+1)_ν, C^rot,
the dual functionals of Step 4′ of the proof of [[thm:iii-i14-3-1]], the t_*-coefficients at K⁺), and at a rotating b
the assigned rotation coordinates A_b of [[def:iii-i15-2-3]], which read the ι⁺-data and the tf-data of the right side
([[prop:iii-i15-2-2]]): bounded by a fixed low norm of the solution or right side they are applied to, by the cited
statements and [[lem:iii-i12-2-3]] (a). The finite-dimensional states, the rows m_ν (the rotation rows among them), the
towers T_(ρ,b) and the states of [[lem:iii-i14-2-1]] they are paired with are fixed smooth sections, smooth in b
([[lem:iii-i15-1-1]] (P3)). So, composed with tame families, they give tame families by [[lem:iii-j2-1-2]] (b)–(c).
The conormal components Ṡ_rem, ḃ_rem, Ẏ_ρ of q′ are not finite-dimensional: they are functions of t_* that Step 4 of
the proof of [[thm:iii-i12-3-1]] assembles (Ṡ_rem := A + A_5 + a_s, ḃ_rem := B + a_b, Ẏ_ρ := a_ρ + Y^c_ρ) from the
outputs of its Steps 1–3, so they are outputs of a composition of the families of its entry in [[sec:iii-j2-3]], tame
with a fixed loss by [[lem:iii-j2-1-2]] (e).

(d) (*Integrations along faces.*) [[lem:iii-a-1-2]] and [[lem:iii-a-3-2]] (membership statements, which take the a
priori norm of the solution as an input: [[lem:iii-j2-1-2]] (f)) and [[lem:iii-i2-2-1]]: order k to order k (loss 0);
[[lem:iii-i2-3-1]]: loss ℓ, independent of k, as stated.

(e) (*Transforms, and the low and middle frequencies.*) [[prop:iii-a-4-2]] (1) (Fourier transform, loss l),
[[prop:ii-g1-3-3]] (1) (loss 1), [[prop:ii-g1-3-5]] (loss ℓ) and [[cor:ii-g1-4-2]] ((1): loss j + ℓ for ∂^j_σ, j fixed
by the weights; (2): loss ℓ), [[prop:iii-h-3-2]] (L̃_b(0)⁻¹, loss 1), [[cor:iii-h-4-2]] (on |σ| < c_k, no loss) and
[[lem:iii-i2-4-2]] (loss ℓ): as stated, at every order with the loss independent of the order.

(f) (*High frequencies.*) [[cor:ii-g1-4-5]] loses ⌈kδ⌉ + ℓ, δ = δ_Γ(−η) ([[eq:i-b-1-4]]), where ℓ = 2ℓ_3 + ℓ_4 + ℓ_5
depends only on the orders and the weights, not on η, the trapping data or the constant C_0. At every b ∈ ℬ̄_1 ⊃ ℬ̄_*
the operator 2L_b is strongly trapping admissible ([[prop:iii-h2-1-1]]), and for every k the fibre inner product of
(Γ.4) in [[sec:i-b-1-5]] and η can be chosen with (k + 1)δ_Γ(−η) ≤ 1, uniformly in b ∈ ℬ̄_1 ([[cor:iii-h2-1-2]]);
then the loss at the order k is at most ℓ + 1, with constants uniform in b. [[lem:iii-i2-4-1]] composes this with (e)
and the invertibility of [[cor:iii-h-4-4]] on the middle frequencies; it has loss at most ℓ + 1 plus the losses of (e).

(g) (*Model inverses stated at order ∞.*) Each of the following holds at every order k with a loss independent of k, by
its own proof, read at the order k:

- [[thm:iii-g1-3-1]] (2): N_ι⁺(λ)⁻¹ has the loss d at every k, as stated, finite-meromorphic in λ with principal parts
  independent of k. [[thm:iii-g2-4-2]] and [[cor:iii-g2-4-3]] compose it with a contour integral over a fixed circle on
  which λ ∉ spec_ι⁺(L̄) (bounded at each order, uniformly on the circle), with the towers at b (fixed sections paired
  with finitely many coefficients) and with L_b (loss 2): loss d + 2. The same holds for [[cor:iii-g3-3-1]],
  [[prop:iii-g3-2-4]] and [[prop:iii-g3-3-7]], whose losses are fixed, as the proof of [[thm:iii-j-2-4]] records (the
  loss l of [[prop:iii-g3-3-7]]).

- [[cor:iii-f1-3-4]]: N_tf(L̂_b, ±1)⁻¹ has the loss ℓ at every k, as stated. [[thm:iii-g4-3-1]],
  [[prop:iii-g4-4-4]] and [[prop:iii-g4-5-1]] compose it with L̃_b(0)⁻¹ ((e)), cut-offs, a Mellin inversion on a fixed
  vertical line not crossing a root (bounded at each order), and finitely many rounds whose number is fixed by the
  weights (each raises the order by at least ε_ind − ε): fixed loss.

- [[prop:iii-i1-2-1]] and [[prop:iii-i1-3-1]]: compositions of (d), of (z − 3/2 − Ā)⁻¹ ((c)) and of L̃ ((b), loss 2,
  its coefficients depending on h); [[prop:iii-i1-2-1]] is a regularity statement, the family (f, u) ↦ u with the a
  priori norm of u as an input ([[lem:iii-j2-1-2]] (f)), as is [[lem:iii-a-3-2]] within it; in finitely many steps whose
  number is fixed by ℓ_I, ℓ_+ and the index sets: fixed loss.

- [[lem:iii-i2-4-3]]: b̂ ↦ χG_1(b̂) and Ŝ ↦ χG_2(Ŝ) multiply finite-dimensional data by fixed sections built from the
  states: loss 0.

*Proof.* (a)–(c) are proved in their statements; the continuity in b of the constants is that of the objects at b
([[lem:iii-i15-1-1]] (P1)–(P4) and (P6)), and the bound on E^ν is (P6) there. (d) and (e) are the cited statements, each
of which is stated at every order with the loss independent of it, and with constants uniform in b ([[lem:iii-i15-1-1]]
(P1), (P4)). (f) That ℓ depends only on the orders and the weights is read off from the proof of [[cor:ii-g1-4-5]]:
ℓ_4 = ℓ_1 + ℓ_2 + 2ν + ⌈(δ_2 − δ_1)_+⌉ is the loss of [[prop:ii-g1-4-4]], with ℓ_1, ℓ_2 and ν from [[lem:ii-g1-4-3]], and
ℓ_3, ℓ_5 are the losses of [[prop:ii-g1-3-5]] (2) and [[prop:ii-g1-3-3]] (2). For δ: [[cor:iii-h2-1-2]] gives, for every k, an
inner product and ε_k > 0 with δ_Γ(−η) ≤ 1/(k + 1) for η ∈ (0, ε_k] and every b ∈ ℬ̄_1; its proof bounds γ_+ by the bound
[[eq:iii-h2-1-1]] of [[prop:iii-h2-1-1]] and γ_+ − γ_− from below by ν_min/(2 sup_Γ q^Γ), where β_0, ν_min and q^Γ do not
depend on the inner product and are continuous and positive on ℬ̄_1. So (k + 1)δ ≤ 1 and ⌈kδ⌉ ≤ 1. The constants of
[[cor:ii-g1-4-5]] at the order k, with the inner product h_(η_k,b) of [[cor:iii-h2-1-2]], are uniform in b ∈ ℬ̄_1. Indeed
[[lem:ii-g1-4-3]], [[prop:ii-g1-3-3]] and [[prop:ii-g1-3-5]] do not involve the operator, and [[prop:ii-g1-4-4]] takes
its constants and C_0 from [[thm:i-b-1-3]] (3) and (5), whose constants are uniform in b by [[sec:i-b-9]]: (H5)–(H8) hold
continuously in b ((B1) in [[sec:iii-h2-0]]), and h_(η_k,b) is smooth in b ([[prop:iii-h2-1-1]]). This is (ii) of the
proof of [[thm:iii-h2-2-1]] ([[lem:iii-i15-1-1]] (P4)). The remark after [[prop:ii-g1-4-4]] treats only γ_+ ≤ 0 and is
not used. (g) Each statement is a finite composition of maps of (b)–(e) and of the two face inverses cited, at a fixed
number of steps; [[lem:iii-j2-1-2]] (e)–(f) applies, β entering only through the families of (b) (in [[prop:iii-i1-2-1]]
and [[prop:iii-i1-3-1]], through L̃). ∎

**Remark {#rem:iii-j2-2-2}** (Choices that depend on the order.) In [[lem:iii-j2-2-1]] (e)–(f) two choices depend on k:
the radius c_k of the low-energy cut-off, and the trapping data. Both enter only decompositions u = u_hi + u_reg +
u_sing (and their analogues) of a solution u that does not depend on them, used to show that u lies in a
better-weighted space; at the order k the decomposition made with the order-k choices gives the order-k bound. So the
choices change the constants C_k, which may depend on k, and not the losses ([[lem:iii-j2-1-2]] (g)).

**Lemma {#lem:iii-j2-2-3}** (Smallness in one norm.) There is d_* such that every smallness condition on the background
in [[ch:s19]]–[[ch:s23]] is smallness of ‖h‖_(𝒳^(d_*)) + |S| + |p⃗| + ‖q‖_(𝒬^(d_*)), and every statement there that a
finite-dimensional map is close to ±id, or that a family is continuous at the background 0, holds in the topology of
this norm. Hence [[lem:iii-j2-2-1]] and [[sec:iii-j2-3]] hold with d_0 := d_* + D, D the total loss of the compositions
of [[sec:iii-j2-3]] (the d of [[thm:iii-j2-4-1]]), and one d_0 serves every order k.

*Proof.* [[thm:iii-i-5-3]] asks ‖h‖_(𝒳^(d_T)) < ε_0, d_T fixed, and [[thm:ii-f1-1-1]] asks
‖P − P_0‖_((0;d),(2ℓ_I,ℓ_+,ℓ_K)) < ε_0, which [[lem:iii-j2-2-1]] (a) bounds by C‖β‖_(d+d′+5). The proof of
[[lem:iii-i4-4-2]] (b) gives the continuity of (h, S) ↦ Ṡ_(h,S) with h in the 𝒳^d-topology, d ≥ k_1 + d_T + 7, whence
S^(−1)_(h,S) is close to the identity. [[ch:s21]] fixes "h small" as small in 𝒳^d, d fixed, for [[lem:iii-i7-2-5]],
[[lem:iii-i7-3-1]] (c), [[lem:iii-i7-4-1]], [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]] and [[cor:iii-i7-4-6]], and takes the
same convention for [[prop:iii-i8-4-1]] and T_(h,p⃗); [[thm:iii-i11-4-1]] takes the continuity of T_(h,p⃗) from
[[prop:iii-i8-4-1]] (ii). [[ch:s23]] fixes "q small" as small in one fixed seminorm of large order, so that
h + h_rem(q) is small in that 𝒳^d. Steps 3 and 4′ of the proof of [[thm:iii-i14-3-1]] take A_k → 0 and the derivative
of C^rot at 0 also from [[lem:iii-i8-3-3]], [[lem:iii-i9-2-6]], [[lem:iii-i11-3-3]], [[lem:iii-i13-2-3]] and
[[lem:iii-i14-2-3]]–[[lem:iii-i14-2-4]]. Of these, [[lem:iii-i9-2-6]] is continuous with h ∈ 𝒳^k, k ≥ 5, under the
same convention for "small"; [[lem:iii-i14-2-3]]–[[lem:iii-i14-2-4]] bound R_q and Δ_q by C‖q‖ in the one fixed
seminorm of q; and [[lem:iii-i8-3-3]], [[lem:iii-i11-3-3]] and [[lem:iii-i13-2-3]] (by the proof of
[[lem:iii-i11-3-3]]) state (h_j, p⃗_j) → (0, 0) without naming a topology, but their proofs give

    S^(h_j,p⃗_j)_ν(G_j) − S^(0,0)_ν(G) = S^(0,0)_ν(R_j),        R_j := G_j − G − (L_j − L_(b_0)) u_j,

with S^(0,0)_ν bounded by one fixed seminorm ([[lem:iii-j2-2-1]] (c)), so they need R_j → 0 only in that seminorm:
G_j → G there, and (L_j − L_(b_0)) u_j → 0 there, which holds for h_j → 0 in 𝒳^(d′), d′ fixed ([[lem:iii-j2-2-1]] (b)
at that order), with u_j bounded at a fixed order. Step 4′ needs R → 0 only at one loss ε and one order. At a base point
with parameter b, the continuity is read at b through [[lem:iii-i15-2-4]] at (0, p⃗_b), p⃗_b the parameter whose only
nonzero component is b − b_0, and through the direct bound |A_k| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b_0|) of Step 3 of
the proof of [[prop:iii-i15-2-5]], both in fixed seminorms; the orders of the rotation rows are among those just named.
None of these orders depends on k, and d_* is their maximum. For [[thm:iii-j1-2-1]],
‖Φ(U)‖_(d_*) ≤ C‖U‖_(𝒟^(d_*+d)) ([[thm:iii-j-2-4]]). ∎

**Lemma {#lem:iii-j2-2-4}** (Tame products in partially polyhomogeneous spaces.) Let E, E′ be partially polyhomogeneous
spaces of [[sec:iii-j2-1]] at one or more faces, at the loss ε, and G the space that the membership statements
([[lem:iii-c-2-1]]) give to products. There is d_1 with

    ‖uv‖_(G^k) ≤ C_k (‖u‖_(E^k) ‖v‖_(E′^(d_1)) + ‖u‖_(E^(d_1)) ‖v‖_(E′^k));

and if the exponents of E have positive real parts, as those of the background do, then for a smooth Θ, depending also
on the point (through g_0, g_0⁻¹ and their derivatives), with Θ(·, 0) = 0 and ‖u‖_(E^(d_1)) ≤ 1,
‖Θ(u)‖_(G^k) ≤ C_k ‖u‖_(E^k), G the space of Θ(u) by the same statements.

*Proof.* The coefficient of uv at an exponent is a finite sum of products of coefficients of u and of v, functions on
the face bounded by [[lem:ii-g-4-1]] (2) there; a product with a remainder factor is bounded by [[lem:ii-g-4-1]] (2) in
the weighted b-Sobolev space, the weights adding ([[cor:ii-a-9-7]]); a term whose exponent lies beyond the remainder's
weight is put in the remainder with the same bound. For Θ: Taylor's formula to an order M, fixed by the weights, at
which M times the least real part of the exponents exceeds the remainder's weight; the polynomial part is bounded by
the product bound, and the Taylor remainder by [[lem:ii-g-4-1]] in the weighted b-Sobolev space. ∎

### The inventory {#sec:iii-j2-3}

Each construction of [[ch:s19]]–[[ch:s23]] is a composition, in a fixed number of steps, of the families of
[[lem:iii-j2-2-1]]. We write FWD for the families of [[lem:iii-j2-2-1]] (a), BG for (b), FIN for (c), INT for (d) and
MOD for (e)–(g). The list gives, for each statement, the families it uses and the number of its steps; the length of a
loop is fixed by the weights and orders of the statement, never by k. At a base point with parameter b each statement
is used in its form at b, named in the entry where it differs from the form at b_0.

- [[thm:iii-i-5-3]] (at b, [[cor:iii-h2-5-1]]): FWD ([[cor:ii-f1-1-2]]); one step.
- [[rem:iii-i-5-5]]: FWD, BG ([[eq:iii-i-4-2]]), MOD (the stationary inverses below); the rewritings
  L_b u = f − (L^(g,g_0) − L_b)u, finitely many.
- [[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]]: INT, FIN, BG (L̃); finitely many steps, their number fixed by ℓ_I and ℓ_+.
- [[prop:iii-i2-5-1]]: FWD ([[thm:iii-i-5-3]]), BG, MOD ([[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]]; [[lem:iii-i2-2-1]],
  [[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]]; [[prop:ii-g1-3-3]], [[prop:ii-g1-3-5]];
  [[lem:iii-a-1-2]]); steps raising α′_K by min(a_K − 2, α_K − α′_K).
- [[prop:iii-i3-2-1]]: FWD ([[prop:iii-i2-5-1]]), BG, MOD ([[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]];
  [[prop:iii-h-3-2]]; [[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]]), FIN (the coefficient S_0); one step.
- [[prop:iii-i4-4-1]], [[lem:iii-i4-4-2]], [[cor:iii-i4-4-3]] (at b, in the form of [[prop:iii-i15-2-8]]): FWD
  ([[prop:iii-i3-2-1]]), BG (h^(−1)(S), f_(h,S)), FIN (Ṡ = Πf′, (S^(−1)_(h,S))⁻¹); one step.
- [[prop:iii-i5-2-1]], [[cor:iii-i5-2-2]] (at b, in the form of [[prop:iii-i15-2-8]]): FWD ([[cor:iii-i4-4-3]]), BG,
  MOD ([[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]]; [[cor:iii-g2-4-3]]; [[prop:iii-h-3-2]]), FIN; exponents in a window,
  and steps raising α′_K to α_K.
- [[lem:iii-i6-1-2]]–[[lem:iii-i6-1-4]], [[prop:iii-i6-2-1]]: FWD ([[cor:iii-i5-2-2]]), BG ((L − L_b)u,
  [[eq:iii-i-4-2]]), MOD ([[prop:iii-a-4-2]]; L̃_b(σ)⁻¹ by [[lem:iii-i2-4-2]]; [[lem:iii-i2-2-1]], [[lem:iii-i2-4-1]],
  [[lem:iii-i2-4-3]]; [[prop:iii-i1-2-1]]; [[lem:iii-i3-1-3]]; [[prop:iii-h-3-2]]; [[cor:iii-g2-4-3]];
  [[prop:iii-g4-5-1]]; [[prop:ii-g1-3-3]], [[prop:ii-g1-3-5]] (1)), FIN; one step.
- [[lem:iii-i7-4-1]], [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]], [[cor:iii-i7-4-6]] (at b, in the form of
  [[prop:iii-i15-2-12]]): FWD, BG, FIN; one step.
- [[lem:iii-i8-3-1]]–[[lem:iii-i8-3-3]], [[prop:iii-i8-4-1]] (at b, with the base step of [[prop:iii-i15-2-12]]): FWD,
  BG, MOD ([[prop:iii-i1-2-1]], [[prop:iii-i1-3-1]]; [[cor:iii-g2-4-3]]; [[prop:iii-g4-5-1]]; [[prop:iii-h-3-2]]), FIN;
  finitely many levels α_0 < α_1 < ⋯, their number fixed by α and a_K, and the tf steps i_0.
- [[def:iii-i9-2-1]], [[lem:iii-i9-2-4]], [[lem:iii-i9-2-6]] (at b, in the form [[eq:iii-i15-1-1]]): FIN (m_ν, h_ν,
  ϑ_ν: fixed sections times W), BG (f^ν, r^ν, and at b the errors E^ν), FWD of L_b; no loop.
- [[lem:iii-i10-2-1]], [[cor:iii-i10-2-3]], [[prop:iii-i10-3-1]]: MOD ([[prop:iii-i1-3-1]], the formal solutions for
  L_b; [[cor:iii-g2-4-3]]), FIN (at a rotating b, the rotation rows with the coefficients of [[prop:iii-i15-2-2]] (a));
  windows, at most N_*.
- [[lem:iii-i11-2-1]]–[[lem:iii-i11-2-5]], [[prop:iii-i11-3-1]], [[lem:iii-i11-3-2]], [[lem:iii-i11-3-3]],
  [[thm:iii-i11-4-1]] (at a rotating b, [[thm:iii-i11-4-1]] only inside [[lem:iii-i15-2-4]] and [[prop:iii-i15-2-5]],
  the latter with q = 0 being its form there): MOD (L̃_b(0)⁻¹; [[prop:iii-g4-4-4]], [[prop:iii-g4-5-1]];
  [[lem:iii-i2-4-2]]; [[prop:iii-a-4-2]]), BG (the columns), FIN (at a rotating b, the coefficients of
  [[prop:iii-i15-2-2]] (b)), FWD; steps rising by ε_ind, and the level-3 loop.
- [[lem:iii-i12-2-1]]–[[lem:iii-i12-2-4]], [[thm:iii-i12-3-1]] (at b, in the forms of [[lem:iii-i15-2-9]] and
  [[cor:iii-i15-2-10]]): FWD, MOD (as in the preceding entry), BG, FIN; pairs removed, finitely many.
- [[prop:iii-i13-2-1]], [[lem:iii-i13-2-2]], [[lem:iii-i13-2-3]], [[prop:iii-i13-2-4]] (at b, the first three in the
  form of [[lem:iii-i15-2-4]]; at a rotating b, [[prop:iii-i13-2-4]] only inside [[prop:iii-i15-2-5]], the latter with
  q = 0 being its form there): as in the two preceding entries, at each level β; as there.
- [[thm:iii-i14-3-1]]: FWD (L_(h+h_rem(q),p⃗)), BG (R_q, Δ_q), FIN, and the entries of [[prop:iii-i8-4-1]] and of
  [[ch:s22]]; levels β_0 < ⋯ < β_K, their number fixed by α and α_1.
- [[prop:iii-i15-2-5]] ([[thm:iii-i14-3-1]] at a rotating b): as [[thm:iii-i14-3-1]], and FIN (A_b, of finite rank,
  [[lem:iii-j2-1-2]] (c)), BG (E^ν, (P6) of [[lem:iii-i15-1-1]]); as there.
- [[thm:iii-j1-2-1]]: [[thm:iii-i14-3-1]], or at a rotating b [[prop:iii-i15-2-5]], at Φ(U); MOD
  ([[prop:iii-g3-3-7]]; the t_*^(−λ_0)-terms); BG (D_UΦ); the exponents of Λ_*, finitely many.

### The tame theorems {#sec:iii-j2-4}

**Theorem {#thm:iii-j2-4-1}** (The tame form of the forward problem with parameters.) Let ε ∈ (0, ε_1], and let
ε′(ε, j) ∈ (0, ε], j ∈ ℕ₀, non-increasing in j, be the input losses that [[thm:iii-i14-3-1]] assigns to the output
loss ε ([[sec:iii-j2-1]]; independent of j for the statements listed there). There are d, d_0 ∈ ℕ and δ_𝔹 > 0
such that for (h, p⃗, q) with ‖h‖_(𝒳^(d_0)) + |p⃗| + ‖q‖_(𝒬^(d_0)) < δ_𝔹 the maps F ↦ (h′, p⃗′, q′) of
[[thm:iii-i14-3-1]] (at a rotating black hole parameter, of [[prop:iii-i15-2-5]]) satisfy, for every k ∈ ℕ₀,

    ‖h′‖_k + |p⃗′| + ‖q′‖_k ≤ C_k (‖F‖_(k+d) + (‖h‖_(k+d) + |p⃗| + ‖q‖_(k+d)) ‖F‖_d),                  {#eq:iii-j2-4-1}

with ‖h′‖_k and ‖q′‖_k the norms of the order-k spaces of [[eq:iii-i14-3-2]] and of 𝒬^k ([[eq:iii-i14-1-1]]) at the loss
ε, the background norms at the loss ε, and ‖F‖_j the norm of the order-j space of 𝒴^♮(α−) at the loss ε′(ε, j). On the
exact scales of [[sec:iii-j3-1]] it holds with ε′(ε, j) = ε = 0 for every j ([[cor:iii-j3-6-6]]). Here δ_𝔹 is at most the
radius of a ball about b_0 in ℬ_*, so the black hole parameter b of p⃗ lies in ℬ_*, and d, d_0, δ_𝔹 and the C_k do not
depend on b. The same holds for the solution maps of [[ch:s19]]–[[ch:s22]] in their spaces (at a rotating b, those of
[[thm:iii-i11-4-1]] and [[prop:iii-i13-2-4]] read as in [[lem:iii-i15-2-4]] and [[prop:iii-i15-2-5]], with q = 0), and
for [[thm:iii-i14-3-1]] with η_2 replaced by ε_+ ([[lem:iii-j1-1-1]]).

This is the tame estimate that [Hin26, Corollary 11.66, pp. 294–295] states.

*Proof.* By induction over the entries of [[sec:iii-j2-3]] in their order. Each solution map is, by [[sec:iii-j2-3]], a
composition of a fixed number of the families of [[lem:iii-j2-2-1]] and of the solution maps of earlier entries, which
are tame by the induction; each loop has a length fixed independently of k. [[lem:iii-j2-1-2]] (b)–(g) gives a tame
family with a loss d equal to the sum of the losses, independent of k, for d_0 ≥ d and δ_𝔹 small
([[lem:iii-j2-2-3]]); the weights compose in the same way, each family taking its input in the graded space of the
losses its statement assigns ([[sec:iii-j2-1]]). For [[thm:iii-i14-3-1]] the background is β = (h, p⃗, q), and
[[eq:iii-j2-1-1]] is [[eq:iii-j2-4-1]]. At a base point with parameter b the entries are used in their forms at b; the
constants of [[lem:iii-j2-2-1]] are uniform on ℬ̄_*, and d_* of [[lem:iii-j2-2-3]] does not depend on b; so neither do
d, d_0 and the C_k. ∎

**Theorem {#thm:iii-j2-4-2}** (The tame form of the right inverse.) Let ε ∈ (0, ε_1], and let ε′(ε, j), non-increasing in
j, be the input losses that [[thm:iii-j1-2-1]] assigns, as in [[thm:iii-j2-4-1]]. There are d, d_0 ∈ ℕ and ε_0 > 0 such
that for U ∈ 𝒟^∞_ε with ‖U‖_(𝒟^(d_0)_ε) < ε_0, whose black hole parameter then lies in ℬ_*, the solution U′ of
[[eq:iii-j1-2-1]] satisfies, for every k,

    ‖U′‖_(𝒟^k_ε) ≤ C_k (‖f‖_(ℱ^(k+d)_(ε′(ε,k+d))) + ‖U‖_(𝒟^(k+d)_ε) ‖f‖_(ℱ^d_(ε′(ε,d)))),          {#eq:iii-j2-4-2}

with C_k independent of U. On the exact scales of [[sec:iii-j3-1]] it holds with ε′(ε, j) = ε = 0 for every j
([[cor:iii-j3-6-6]]). At a rotating black hole parameter, U′ is built from the solution map of [[prop:iii-i15-2-5]]. The
smallness is in one norm for every k ([[lem:iii-j2-2-3]]), which replaces the orders d_k of [[thm:iii-j1-2-1]].

This is the estimate of [Hin26, Theorem 12.8, p. 312].

*Proof.* Step 0 of the proof of [[thm:iii-j1-2-1]] applies [[thm:iii-j2-4-1]] at the background Φ(U), with ‖Φ(U)‖_k ≤ C_k
‖U‖_(𝒟^(k+d)) ([[thm:iii-j-2-4]]) and ‖Φ(U)‖_(d_0) small for ‖U‖_(𝒟^(d_0+d)) small; composed with U ↦ Φ(U),
[[eq:iii-j2-4-1]] has the form [[eq:iii-j2-1-1]] in the background U. At a rotating black hole parameter b,
[[lem:iii-j1-1-1]] holds for the output of [[prop:iii-i15-2-5]]: the indicial roots are those at b_0 ([[lem:iii-i15-1-1]]
(P2)), [[prop:iii-h-3-2]] holds at b ((P4) there), and neither A_b, which reads only ι⁺-data and level-1 tf-data
([[def:iii-i15-2-3]]), nor E^ν, a fixed tensor ((P6) there), depends on η_2. Steps 1–3, which hold at b with the rows
built at b_0 ([[sec:s23-base-points]] (3)), subtract D_UΦ(U′_•) for finitely many U′_•: the finite-dimensional data of
Step 1 (bounded by a low norm of (h′, p⃗′, q′), [[lem:iii-j2-2-1]] (c)); the data of Case B of Step 2,
f_(λ_0) ∈ Poly^(K_ι(λ_0))(ℂ; H^(k,…)) and G′(λ_0) ∈ Res^k, which are not finite-dimensional and are mapped by the right inverse of
[[prop:iii-g3-3-7]], independent of U with the loss l, on the finitely many λ_0 ∈ Λ_* ([[lem:iii-j2-2-1]] (g),
[[lem:iii-j2-1-2]] (d)); and the conormal remainders of Step 3 (the conormal components of q′, [[lem:iii-j2-2-1]] (c)).
By [[rem:iii-j-2-5]],

    D_UΦ(U′) = DΦ_0(U_0)U′_0 + (DA(U_0)U′_0)U_1 + A(U_0)U′_1:

the first and third terms are tame in U′, uniformly in U_0 small ([[thm:iii-j-2-4]]), and the second is bounded by
C|U′_0| ‖U_1‖_(𝒟^(k+d)), of the form [[eq:iii-j2-1-1]], as |U′_0| is bounded by a low norm of f. [[lem:iii-j2-1-2]]
gives [[eq:iii-j2-4-2]]. ∎

**Proposition {#prop:iii-j2-4-3}** (The forward map.) There are d and ε_0 such that for b near b_0, ε ∈ (0, ε_1] and
U ∈ 𝒟^∞_ε with ‖U‖_(𝒟^(3d)_ε) < ε_0,

    ‖P_5(Φ(U))‖_(ℱ^k_ε) ≤ C_k (1 + ‖U‖_(𝒟^(k+d)_ε)),        k ≥ d,

and the first and second derivatives of U ↦ P_5(Φ(U)) satisfy [[eq:ii-g-2-3]] with the norms of 𝒟^(3d)_ε and
ℱ^(2d)_ε. The map gains nothing in the weights: it takes 𝒟_ε to ℱ_ε.

This is [Hin26, Section 13.1, Step 3 (2), p. 322] in dimension 4 + 1.

*Proof.* Φ is affine in U_1 with coefficients smooth in the finite-dimensional U_0, and tame ([[thm:iii-j-2-4]]).
P_5(h, p⃗, q) = P_4(h + h_(b,rem)(q), p⃗) is Ric − δ*Υ of a metric that is a smooth function of p⃗ plus
h + h_(b,rem)(q), so a smooth function of (h, ∂h, ∂²h) and of q with coefficients smooth in p⃗; [[lem:ii-g-4-1]] (with
[[lem:ii-a-9-5]]) bounds it and its first two derivatives tamely in the b-Sobolev norms. The weights are those of
[[eq:iii-j-2-5]], which holds at every b near b_0 ([[thm:iii-j-2-4]]). The cancellation enters only qualitatively: the
terms of u-exponent below 3 + ε_+ cancel identically ([[eq:iii-j-2-3]]), so P_5(Φ(U)) lies in the partially
polyhomogeneous space with exponents in Λ + 2 whose coefficients below 5 + ε_+ vanish, and its ℱ^k_ε-norm is the sum of
the norms of the remaining coefficients and of the remainder, each a finite sum of products bounded by
[[lem:iii-j2-2-4]], the weights adding as in the proof of [[eq:iii-j-2-5]]. The linear terms L_b h keep the loss of h,
which is why no weight is gained. The second derivative is bilinear with two factors at the low norm. ∎

**Remark {#rem:iii-j2-4-4}** (The hypotheses of the Nash–Moser theorem.) In the notation of [[thm:ii-g-2-1]], with the
map U ↦ P_5(Φ(U)) in the role of the map there and the right inverses of [[thm:iii-j2-4-2]] in the role of Ψ(u),
[[thm:ii-g-2-1]] asks, on one pair of Banach scales: (i) smoothing operators on the spaces of 𝒟 ([[prop:ii-g-3-1]];
[Hin26, p. 322]); (ii) the tame forward map ([[prop:iii-j2-4-3]]), mapping U ∩ B^∞_η into F^∞_η; and (iii) tame right
inverses ([[thm:iii-j2-4-2]]) at every point of a neighbourhood of 0, so at b ≠ b_0 too, with Ψ(u)F^∞_η ⊂ B^∞_η for
u ∈ U ∩ B^∞_η. [Hin26, Section 13.1, Step 3 (3), p. 322] meets these support conditions by finite speed of
propagation. The pair of scales is that of [[cor:iii-j3-6-6]], on which [[prop:iii-j2-4-3]] maps 𝒟 to ℱ and the right
inverse maps ℱ to 𝒟, both without loss in the weights; the right inverses at b ≠ b_0 are those of [[thm:iii-j2-4-2]]
and [[thm:iii-j3-5-5]], stated at every b ∈ ℬ_*. The support conditions, the smoothing operators on the exact spaces
𝒟_ex and the exterior family h_(−S) of [[ch:s26]] are supplied with the nonlinear theorem in [[ch:s27]].

### The exact classes and the exactness conditions {#sec:iii-j3-1}

Throughout [[sec:iii-j3-1]]–[[sec:iii-j3-6]], α is a fixed K⁺-weight, admissible in the sense of [[def:iii-i10-1-3]],
with α ∈ (4 + ε_K − ε′_0, 4 + ε_K], satisfying (A_J) of [[def:iii-j-a-j]] and [[def:iii-j3-1-3]] below. The exact
classes and the conditions of [[def:iii-j3-1-3]] do not involve the black hole parameter b of the base point: the
exponents, indicial roots and index sets in them are those at b_0, which serve at every b ∈ ℬ̄_*
([[lem:iii-i15-1-1]] (P2)–(P3)).

**Definition {#def:iii-j3-1-1}** (Exact classes.) Each class below is the class named after it with every order "w−"
replaced by w and every index set unchanged:

- 𝒳^k_(J,ex) := H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,3+ε_+),α)_b(Ω_*; S²T*)^(•,−) (the class 𝒳^k_J of [[def:iii-j-classes]]);
- ℱ^k_ex := H^(k,(⟨ℰ^C_I+1⟩′,ℓ_I+1),w_+,α)_b(Ω_*; S²T*)^(•,−), a plain weight at ι⁺ (the class ℱ^k of
  [[def:iii-j-classes]]);
- 𝒴^0_ex(β) and 𝒴^♮_ex(β): the classes 𝒴^0(β) of [[sec:iii-i10-1]] and 𝒴^♮(β) of [[def:iii-i13-1-2]] with the
  ι⁺-weight w_+ − ε replaced by w_+ (their K⁺-weight β is exact already);
- 𝒬_ex: the class 𝒬 of [[eq:iii-i14-1-1]] with S_rem ∈ Ḣ^(∞,α−2)_b, b_rem ∈ Ḣ^(∞,α−1)_b and
  Y_ρ ∈ Ḣ^(∞,𝒬(ℰ^α_ρ,3+ε_+−d_ρ))_b;
- 𝒟^k_ex: the class of [[def:iii-j-1-1]] with S_rem ∈ Ḣ^(k,α−2)_b, b_rem ∈ Ḣ^(k,α−1)_b,
  Y_(ρ,rem) ∈ Ḣ^(k,3+ε_+−d_ρ)_b and h̃ ∈ H^(k,(⟨ℰ^C_I⟩,ℓ_I),3+ε_+,α)_b, normed by the norms of its components at these
  fixed weights.

These are the classes of [Hin26, (11.226), p. 292; (11.227b), p. 293; (11.233), p. 294; (12.12c)–(12.12d), p. 301;
(12.31), p. 310], with (3 + ε_I, 4 + ε_I) read as (ℓ_I, ℓ_I + 1) and 4 + ε_K as α. Each 𝒟^k_ex and ℱ^k_ex is a Banach
space.

**Remark {#rem:iii-j3-1-2}** (Inclusions.) Each exact class is continuously embedded in its "w−" class: the index sets
are the same and the weight is larger. And ℱ_ex ⊂ 𝒴^0_ex(α): a plain weight w_+ is the class (ℰ^0_src + 2, w_+) with
vanishing coefficients, as Step 0 of the proof of [[thm:iii-j1-2-1]] argues for the "w−" classes. So every statement of
[[ch:s19]]–[[ch:s23]] applies to exact inputs. Only statements whose output must lie in an exact class are proved anew
below.

**Definition {#def:iii-j3-1-3}** (The exactness conditions.) Besides admissibility and (A_J):

- (Ex1) (G⁺) of [[def:iii-j-g-plus]], used with its closed endpoint: no λ ∈ Λ has real part in (3, 3 + ε_+], that is,
  ε_+ < min{Re λ − 3 : λ ∈ Λ, Re λ > 3}, a smallness condition. With [[lem:iii-i10-1-2]] (c) (every exponent produced
  with real part in [2, 3 + ε_+] lies in Λ), no exponent produced has u-exponent of real part 3 + ε_+.
- (Ex2) 3 + ε_+ ∉ Re π_1ℰ^tot_I ∪ {λ_♯}: the exclusions of [[prop:iii-i1-3-1]] (Re π_1ℰ^C_I and λ_♯) and of
  [[prop:iii-i1-2-1]] (Re π_1ℰ^tot_I) at the ι⁺-weight 3 + ε_+; here ℰ^tot_I ⊃ ℰ^C_I ([[eq:iii-c-3-1]]).
- (Ex3) No K⁺-exponent at hand (of the coefficients of the pieces, of the rows, and their ℕ₀-shifts, as in
  [[lem:iii-i14-2-5]]) has real part α − 2, α − 1 or α. The first and the last are contained in admissibility (the
  proof of [[lem:iii-i14-2-5]]); the middle one is an additional condition.
- (Ex4) α − Re α_0 ≠ −μ and α − 1 − Re α_0 ≠ −μ for every root μ and the finitely many tf-exponents α_0 of levels 1–2
  of [[prop:iii-i11-3-1]]: the conditions [[eq:iii-g4-4-2]] at ℓ_zf = α − 2 and α − 3.
- (A_K) (Optional.) α := 4 + ε_K is admissible and satisfies (A_J), (Ex3) and (Ex4).

No condition is needed for the final zero-energy solve: [[lem:iii-i2-4-2]] excludes no real part and asks only
β_tf − β_zf = α_sf + 2, where α_sf denotes the weight α of [[eq:iii-h-1-1]] (not the K⁺-weight α of this chapter), and
α_sf + 2 ∈ (0, 1).

**Lemma {#lem:iii-j3-1-4}** (The conditions are generic.) (Ex1) is a smallness condition on ε_+, (Ex2) excludes finitely
many ε_+ in any bounded range, (Ex3)–(Ex4) exclude finitely many α, and (A_K) excludes finitely many ε_K at fixed ε_+. So
admissible α with (Ex3)–(Ex4) exist in (4 + ε_K − ε′_0, 4 + ε_K], and ε_+, ε_K may be decreased to meet (Ex1)–(Ex2) and
(A_K), as (G⁺) and (G) already permit.

*Proof.* The excluded numbers are built from finitely many numbers that do not depend on α, ε_+ or ε_K within the ranges
used: the roots μ, discrete with finitely many in any bounded set ([[prop:iii-f1-2-3]]); Λ and the tf-exponents α_0 of
levels 1–2, Λ-valued below 3 and finitely many ([[lem:iii-i10-1-2]]); the exponents at hand below α + 1, finitely many
and Λ-generated (the proof of [[lem:iii-i14-2-5]]); λ_♯; and Re π_1ℰ^tot_I, an index set, finite below any bound. Each
of (Ex2)–(Ex4) and (A_K) removes the values of α, ε_+ or ε_K equal to one of finitely many such numbers; (Ex1) is (G⁺)
itself, an upper bound on ε_+. ∎

### Two elementary lemmas {#sec:iii-j3-2}

**Lemma {#lem:iii-j3-2-1}** (Diagonal terms at ι⁺ ∩ K⁺.) Near the corner let a = t_*^(−c) G(t_*) with
G ∈ H_b([1, ∞), |dt_*/t_*|), and let P be homogeneous of degree −m in r. Then aP ∈ ρ_+^(c+m−η) ρ_K^c H_b and
aP ∈ ρ_+^(c+m) ρ_K^(c−η) H_b for every η > 0, while in general aP ∉ ρ_+^(c+m) ρ_K^c L²_b.

*Proof.* With t_*⁻¹ = ρ_+ρ_K and r⁻¹ = ρ_+,

    ρ_+^(−a_+) ρ_K^(−a_K) aP = ρ_+^(c+m−a_+) ρ_K^(c−a_K) G(1/(ρ_+ρ_K)) P_0,

with P_0 smooth on the sphere. In s := −log ρ_+ and σ := −log ρ_K the squared L²_b-norm at (a_+, a_K) = (c + m, c) is
∫_0^∞ T |G(e^T)|² dT, T = s + σ, which G ∈ L²(dT) does not bound; with the extra factor e^(−2ηs) or e^(−2ησ) it is at
most (2η)⁻¹ ‖G‖², as ∫_0^T e^(−2ηs) ds ≤ (2η)⁻¹. Derivatives are treated in the same way. ∎

**Lemma {#lem:iii-j3-2-2}** (Circle integrals of bounded families.) Let Z ↪ Z_− be a continuous injection of Hilbert
spaces, γ a circle, and F : γ → Z_− continuous with sup_γ ‖F‖_Z ≤ M. Then I := ∫_γ F dλ (in Z_−) lies in Z, and
‖I‖_Z ≤ |γ|M.

*Proof.* The Riemann sums S_n converge to I in Z_− and satisfy ‖S_n‖_Z ≤ |γ|M. A subsequence converges weakly in Z to
some I′; the injection is weakly continuous, so the subsequence converges weakly in Z_− to I′. Hence I = I′ and
‖I‖_Z ≤ liminf ‖S_n‖_Z. ∎

### The graft at the exact K⁺-weight {#sec:iii-j3-3}

Fix φ ∈ C^∞((0, ∞)), positive, with φ(R) = R for R ≤ 1/2 and φ = 1 for R ≥ 2, and put ρ_+ := (t_* φ(R))⁻¹ near ι⁺.
Near ι⁺ ∩ K⁺ it is 1/r, near ι⁺ ∩ 𝓘⁺ it is 1/t_* ([[sec:iii-i2-1]]); so it is a boundary defining function of ι⁺. The
expansions of [Hin26, Definition 2.8, p. 48], in which the classes of [[ch:s19]]–[[ch:s23]] are defined ([[ch:s11]]),
are in powers of ρ_+ and log ρ_+, with coefficients on ι⁺ that carry the weights of the adjacent faces. Near the corner
log ρ_+ = −log t_* − log ρ_K, so

    ρ_+^z (log ρ_+)^ℓ a = t_*^(−z) Σ_(j≤ℓ) (ℓ choose j) (−1)^ℓ (log t_*)^j (log ρ_K)^(ℓ−j) ρ_K^(−z) a. {#eq:iii-j3-3-1}

**Remark {#rem:iii-j3-3-1}** (The two conventions at the exact weight.) [[cor:iii-g2-4-3]] takes

    f = Σ_(j≤k) χ_ι t_*^(−λ_0−2) (log t_*)^j f^(j)_+ + f′,        f^(j)_+ ∈ ⋂_ε H^(∞,ℓ_I+1,ℓ_K−2−ε)_b(ι⁺),

and concludes [[eq:iii-g2-4-5]] at the K⁺-weight λ_0 + ℓ_K − ε. By [[eq:iii-j3-3-1]] a right side of exact K⁺-weight α
in the sense of [Hin26, Definition 2.8] has t_*-coefficients containing (log R)^(ℓ−j) R^(−z) a_ℓ, which lie in
H^(α−Re z−ε) for every ε > 0 but in general not at ε = 0:

    ‖R^(−w+ε) (log R)^k g‖ ≤ (k/(eε))^k ‖R^(−w) g‖,

as sup_(0<R<1) R^ε |log R|^k = (k/(eε))^k, and this is sharp. Conversely, for k = 1, f^(0) = 0 and f^(1) = g generic in
H^(ℓ_K−2), the coefficient of ρ_+^(λ_0+2) in the expansion of [Hin26, Definition 2.8] is −(log φ) φ^(λ_0+2) g, as
log t_* = −log ρ_+ − log φ, and it is not in H^α. So for k ≥ 1 the two classes at the exact weight are incomparable (for
k = 0 they coincide), and [[cor:iii-g2-4-3]] cannot be applied at ε = 0 to a right side of the class of [Hin26,
Definition 2.8]; in its own convention it is stated with the loss, with constants of order ε^(−k). Whether an exact
statement exists in that convention is not decided here; none is needed. [Hin26, Corollary 9.12, p. 179] has the same
loss; [Hin26, Proposition 11.34] states the exact weight after the same step ([Hin26, (11.120b), p. 254]), which
[[cor:iii-j3-3-2]] justifies.

**Corollary {#cor:iii-j3-3-2}** ([[cor:iii-g2-4-3]] at the exact K⁺-weight.) Let Re λ_0 > 1, let l_0 be the order of the
pole of N_ι⁺(L̄, ·)⁻¹ at λ_0 (0 if none), let ℓ_I be as in [[thm:iii-g2-4-2]] with Re λ_0 < ℓ_I, and let α ∈ ℝ with
ℓ_K := α − Re λ_0 ∈ (−1, ℓ^max_K), ℓ_K ≠ −μ for every root μ, and ℓ_K ∉ Re π_1ℰ_K. Let k ∈ ℕ₀ and

    f = Σ_(j≤k) χ_ι ρ_+^(λ_0+2) (log ρ_+)^j a_j + f′,
    a_j ∈ H^(∞,ℓ_I+1,α)_b(ι⁺),        f′ ∈ H^(∞,ℓ_I+1,∞,α)_b(Ω_*; S²T*)^(•,−),                {#eq:iii-j3-3-2}

the weight α of a_j being at ι⁺ ∩ K⁺, as [Hin26, Definition 2.8] prescribes for a right side of K⁺-weight α. Then
there are u^(j)_(b,0) of the form [[eq:iii-g2-4-3]], with λ_0 for λ and a factor (log t_*)^j, and
v_m ∈ H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),α)_b(ι⁺), m ≤ k + l_0, all linear in (a_j, f′), such that
u := Σ_j χ_K u^(j)_(b,0) + Σ_m χ_ι ρ_+^(λ_0) (log ρ_+)^m v_m satisfies

    f − L_b u ∈ H^(∞,(ℰ^tot_(ι⁺,𝓘)+2,ℓ_I+1), λ_0+2+ℰ_ind+(0,k+l_0), α)_b(Ω_*; S²T*)^(•,−),      {#eq:iii-j3-3-3}

the ι⁺-index set taken with respect to ρ_+. For each k′ there are d and C bounding every order-k′ seminorm of u and of
f − L_b u by C(Σ_j ‖a_j‖_(k′+d) + ‖f′‖_(k′+d)). By [[eq:iii-j3-3-1]], [[eq:iii-j3-3-2]] implies the hypotheses of
[[cor:iii-g2-4-3]] and [[eq:iii-j3-3-3]] implies [[eq:iii-g2-4-5]]. For k = l_0 = 0 it is [[thm:iii-g2-4-2]] at
λ = λ_0.

This is [Hin26, Corollary 9.12, p. 179] in the convention of [Hin26, Definition 2.8], and the exact form of
[[cor:iii-g2-4-3]] in dimension 4 + 1. The proof uses a lemma on the family of [[thm:iii-g2-4-2]] along a circle.

*The circle.* Choose δ ∈ (0, 1/4) with δ < min(Re λ_0 − 1, ℓ_I − Re λ_0, ℓ^max_K − ℓ_K), such that
D̄ := {|λ − λ_0| ≤ δ} meets spec_ι⁺(L̄) at most in λ_0, and J := [ℓ_K − 3δ, ℓ_K + δ] ⊂ (−1, ℓ^max_K) contains no −μ and
no point of Re π_1ℰ_K. This is possible, as the spectrum has finitely many points in each half plane
([[lem:iii-g1-4-2]] (a)) and the roots and ℰ_K are discrete. On ∂D, ℓ_K(λ) := α − Re λ ∈ J, λ ≠ 1,
1 < Re λ < ℓ_I, and the window 𝒲(ℓ) of [[thm:iii-g1-3-1]] is the same for every ℓ ∈ J. For a ∈ H^(∞,ℓ_I+1,α)_b(ι⁺)
put f_+(λ) := φ^(−λ−2) a. Near R = 0, |R^(−λ−2)| = R^(−Re λ−2) and (R∂_R)^i R^(−λ−2) = (−λ − 2)^i R^(−λ−2), and φ = 1
near 𝓘⁺; so ‖f_+(λ)‖_(H^(k′,ℓ_I+1,ℓ_K(λ)−2)) ≤ C ‖a‖_(H^(k′,ℓ_I+1,α)) uniformly on D̄. [[thm:iii-g2-4-2]] at λ ∈ ∂D,
with ℓ_K(λ) and the right side f_+(λ), gives u(λ) = χ_K u_(b,0)(λ) + χ_ι t_*^(−λ) ũ(λ) and the remainder
r(λ) := χ_ι t_*^(−λ−2) f_+(λ) − L_b u(λ), whose K⁺-weight in [[eq:iii-g2-4-4]] is Re λ + ℓ_K(λ) = α for every λ. By
the choice of ρ_+, χ_ι t_*^(−λ−2) f_+(λ) = χ_ι ρ_+^(λ+2) a and t_*^(−λ) ũ(λ) = ρ_+^λ U(λ) with U(λ) := φ^λ ũ(λ). Since
∂_λ brings the factor −log φ and R^δ |log R| is bounded, f_+ is holomorphic near D̄ with values in
H^(ℓ_I+1,ℓ_K−3δ−2); at that fixed weight the family of [[thm:iii-g2-4-2]] is holomorphic off the spectrum ([Hin26,
(9.42), p. 178]), so u(λ) and r(λ) are holomorphic near ∂D and meromorphic in D, with at most a pole at λ_0, in spaces
Z_− of K⁺-weight α − 4δ.

**Lemma {#lem:iii-j3-3-3}** (Exact bounds on the circle.) There are d and C such that for every λ ∈ ∂D

    ‖U(λ)‖_(H^(k′,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),α)_b(ι⁺)) + Σ |Y^(μ)_τ(λ)| ≤ C ‖a‖_(k′+d),

and r(λ) = Σ_((e,p)) χ ρ_+^(λ+2+e) (log ρ_+)^p c_(e,p)(λ) + r_M(λ), a finite sum over (e, p) ∈ ℰ_ind with Re e < M,
with each c_(e,p)(λ) bounded by C‖a‖_(k′+d) in H^(k′,(ℰ^tot_(ι⁺,𝓘)+2,ℓ_I+1),α)_b(ι⁺) and r_M(λ) in the space of plain
ι⁺-weight Re λ_0 + 2 + M − δ and K⁺-weight α.

*Proof.* (i) *At the lower weight.* [[thm:iii-g1-3-1]] (2) bounds N_ι⁺(λ)⁻¹ at the fixed weight ℓ_K^− := ℓ_K − 3δ,
locally uniformly in λ off the poles, hence uniformly on the compact circle ∂D; and the coefficients Y^(μ)_τ are
continuous linear functionals of (u, f) there. So Y(λ) and ũ(λ) are bounded in H^(ℓ_K^−) uniformly on ∂D.

(ii) *Up to the exact weight, uniformly.* Near R = 0, [[eq:iii-g1-1-3]] gives R²N_ι⁺(λ) = A_0 + RA_1(λ) with
A_0 = L̃(0)(ω, −R∂_R, ∂_ω) independent of λ, b-elliptic, with boundary spectrum {−μ}. With ũ = u_+ − χ_K u_0 and
N_ι⁺(λ)u_+ = 2f_+,

    A_0(χũ) = χ[2R² f_+(λ) − RA_1(λ)ũ − R² N_ι⁺(λ)(χ_K u_0(λ))] + [A_0, χ]ũ =: g(λ).

Its terms lie in R^(ℓ_K(λ)) H_b (the first), in R^(ℓ_K^−+1) H_b ⊂ R^(ℓ_K(λ)) H_b (the second, as 4δ ≤ 1), in
R^(−μ+k_μ+1) C^∞ ⊂ R³ C^∞ (the third, by the form of u_0, [[eq:iii-g2-2-6]] and [[lem:iii-g2-2-6]]), and have compact
support in R > 0 (the last); all uniformly on ∂D, bounded by C‖a‖. The strip {Re ζ ∈ J} avoids {−μ}, so

    C_J := sup_(Re ζ∈J) Σ_(i≤2) |ζ|^(2−i) ‖N(A_0, ζ)⁻¹‖_(H^s→H^(s+i)) < ∞,

by the elliptic estimate with parameter of [[sec:iii-a-1-1]] for |Im ζ| large and by continuity on the compact rest of
the strip. Then the Mellin transform of χũ is N(A_0, ·)⁻¹ applied to that of g; it continues holomorphically from
Re ζ < ℓ_K^− to Re ζ ≤ ℓ_K(λ) with no pole in the strip; moving the line as in the proof of [[lem:iii-a-1-4]] and using
Plancherel on Re ζ = ℓ_K(λ) gives

    ‖χũ(λ)‖_(R^(ℓ_K(λ)) H^(k′)_b) ≤ C′_J ‖g(λ)‖_(R^(ℓ_K(λ)) H^(k′−2)_b) + C ‖ũ(λ)‖_(R^(ℓ_K^−) H^(k′)_b),

with C′_J depending only on C_J and J. This is [[lem:iii-a-1-4]] with its constant uniform over the weights in J, which
its Mellin proof gives. As φ^λ is b-smooth with |R^λ| = R^(Re λ), ‖U(λ)‖_α ≤ C ‖ũ(λ)‖_(ℓ_K(λ)).

(iii) *The remainder.* Near the corner, where χ_K = χ_ι = 1, [[lem:iii-g2-4-1]] for t_*^(−λ) ũ gives

    r(λ) = ½ t_*^(−λ−2) N_ι⁺(λ)u_0 − L_b u_(b,0) − ½ t_*^(−λ−4) v² B ũ.

The explicit part has K⁺-exponents ≥ λ − μ + k_μ + 1 ≥ λ + 3 and ι⁺-exponents in λ + 2 + ℰ_ind, with coefficients
polynomial in λ times Y(λ); since Re λ + 3 − α ≥ 3 − ℓ_K − δ > 0 it lies at K⁺-weight α with uniform bounds, its
log ρ_K powers sitting strictly above α. In the last term t_*^(−λ−4) v² = ρ_+^(λ+4) φ^(λ+2) ψ², ψ := φ/R; Taylor
expansion of the coefficients of B in 1/r = ρ_+ψ gives terms ρ_+^(λ+4+m) ψ^(m+2) φ² B^λ_m U(λ) with
B^λ_m := φ^λ B_m φ^(−λ) polynomial in λ and coefficients in H^(α+2) ⊂ H^α at R = 0. Near K⁺ with r bounded,
r(λ) = χ_ι ρ_+^(λ+2) a − L_b(ρ_+^λ U(λ)) − L_b u_(b,0) with ρ_+ = 1/r smooth, and L_b ∈ Diff_b there
([[sec:iii-i2-1]]), so every term is at weight α uniformly. Away from K⁺, the proof of [[thm:iii-g2-4-2]] applies
verbatim with u_+(λ) uniformly bounded. This exhibits the decomposition of r(λ) with the stated bounds. ∎

*Proof of [[cor:iii-j3-3-2]].* Since ∂^j_λ ρ_+^(λ+2) = (log ρ_+)^j ρ_+^(λ+2), Cauchy's formula gives

    χ_ι ρ_+^(λ_0+2) (log ρ_+)^j a_j = (j!/(2πi)) ∮_(∂D) (λ − λ_0)^(−j−1) χ_ι t_*^(−λ−2) f_(+,j)(λ) dλ,
                                                                          f_(+,j)(λ) := φ^(−λ−2) a_j.

Let Φ_(ι,b)(λ) be the map f_+ ↦ u of [[thm:iii-g2-4-2]] at λ, and put
u := Σ_j (j!/(2πi)) ∮ (λ − λ_0)^(−j−1) Φ_(ι,b)(λ) f_(+,j)(λ) dλ, an integral in Z_−, with which L_b commutes. With
U_j and r_j the functions U and r of the circle for a := a_j,

    f − L_b u = f′ + Σ_j (j!/(2πi)) ∮ (λ − λ_0)^(−j−1) r_j(λ) dλ.

Expanding ρ_+^(λ+c) = ρ_+^(λ_0+c) Σ_m (log ρ_+)^m (λ − λ_0)^m/m! pointwise, the ι⁺-part of u is
χ_ι ρ_+^(λ_0) Σ_m (log ρ_+)^m v_m with

    v_m = Σ_j (j!/m!) (1/(2πi)) ∮ (λ − λ_0)^(m−j−1) U_j(λ) dλ,

which vanish for m > k + l_0 (the order of the Laurent series); the coefficients of the remainder are circle integrals
of the c_(e,p)(λ), which are polynomial in λ, Y(λ) and U(λ), hence meromorphic in D with pole order at most l_0, so the
same Laurent cut-off applies to them, and its rest is the circle integral of r_M(λ). [[lem:iii-j3-2-2]], with Z the
space at the exact weight α (the coefficient spaces on ι⁺, and the space of plain ι⁺-weight Re λ_0 + 2 + M − δ) and
Z_− the same at α − 4δ, with [[lem:iii-j3-3-3]] bounding the integrands, gives v_m ∈ H^((⟨ℰ^C⟩,ℓ_I),α)(ι⁺), the
coefficients of f − L_b u in H^((ℰ^tot+2,ℓ_I+1),α)(ι⁺) with exponents in λ_0 + 2 + ℰ_ind + (0, k + l_0), and the rest
at K⁺-weight α. As M is arbitrary, this is [[eq:iii-j3-3-3]]. The u_(b,0)-part becomes Σ_j χ_K u^(j)_(b,0) with the
Laurent coefficients of Y(λ) (the form [[eq:iii-g2-4-3]]). The linearity and the bounds, with constants
Cδ^(−k−l_0−1), follow from [[lem:iii-j3-3-3]]. ∎

**Proposition {#prop:iii-j3-3-4}** (The uses of the graft at the top level.) Let f ∈ 𝒴^0_ex(α), with (Ex1)–(Ex3). Then
[[prop:iii-i10-3-1]] holds with: (a) u_I of ι⁺-data (ℰ_I, 3 + ε_+); (b) K⁺-weight α − 2 in place of α − 2 − ε;
(c) f^♭ ∈ H^(∞,ℓ_I+1,(ℰ^♭+2,w_+),α)_b. And the piece (ii) of [[thm:iii-i12-3-1]], the graft remainder, has K⁺-order
exactly α.

*Proof.* (a) Step 1 of the proof of [[prop:iii-i10-3-1]] takes ℓ̆_+ := w_+ − 2 − ε off its exclusions, for all but
finitely many ε; the exclusions are those of [[prop:iii-i1-3-1]] (Re π_1ℰ^C_I and λ_♯) and of [[prop:iii-i1-2-1]]
(Re π_1ℰ^tot_I), and by (Ex2) ℓ̆_+ := w_+ − 2 = 3 + ε_+ is allowed. [[prop:iii-i1-2-1]] and [[prop:iii-i1-3-1]] are
exact at an allowed weight; (Ex2) is used again in the removals at 𝓘⁺ of Step 2 and in the regularity at 𝓘⁺ in
[[prop:iii-j3-4-3]] ([[prop:iii-i1-2-1]] at ℓ_+ = 3 + ε_+).

(c) At K⁺: Step 2 takes c_K := α and applies the graft to the coefficients of the current right side, which lie in
H^(∞,ℓ_I+1,α)_b(ι⁺) with respect to ρ_+ (𝒴^0(α) is a class of [Hin26, Definition 2.8], exact at K⁺);
[[cor:iii-j3-3-2]] replaces [[cor:iii-g2-4-3]], and each graft error has the exact K⁺-weight α by [[eq:iii-j3-3-3]], so
the iteration closes at α. The part of the right side that does not reach ι⁺ near the corner (the difference between
the cut-off of [Hin26, Definition 2.8] and χ_ι) goes into f′. The K⁺-weight α − ε of Step 1 is a free weakening (f_1
has K⁺-weight α). At ι⁺: f^♭ = f − L_b(u_I + u_ι) with f at (ℰ^♭ + 2, w_+), L_b u_I at (ℰ_I + 2, w_+) by (a), and u_ι
a finite sum of single ι⁺-terms; by (Ex1) no exponent has real part w_+, so the integrations of [[lem:iii-a-1-2]] and
[[lem:iii-a-1-4]], which are exact at weights that are not exponents, are applied at such a weight (the class of
[Hin26, Definition 2.8] itself expands every exponent of real part at most the weight).

(b) Its K⁺-ingredients are the ι⁺-part of u_λ, of K⁺-weight α > α − 2; the rows, identified up to K⁺-weight
Re λ_0 + 1 − ε > 5/2 > α − 2; and the c-rows of rate > 2 + ε_K ≥ α − 2, of weight their rate minus ε, which exceeds
α − 2 for ε small; each inequality is strict. At a rotating b the v1 terms of exponent of real part below 2 are the
rotation rows with the coefficients of [[prop:iii-i15-2-2]] (a), read from the ι⁺-data of the graft, which do not
depend on the loss; they are identified up to K⁺-order Re λ_0 + 1 − ε > α − 2, with room. The piece (ii) of
[[thm:iii-i12-3-1]] is the graft remainder χ_ι ρ_+^(λ_0) (log ρ_+)^m v_m of [[cor:iii-j3-3-2]], of K⁺-order exactly α.
∎

### The spectral construction at exact weights {#sec:iii-j3-4}

**Proposition {#prop:iii-j3-4-1}** ([[prop:iii-a-4-2]] is exact at K and zf.) For
β_K ∈ (0, ∞) ∖ (ℕ ∪ Re π_1E_K), [[prop:iii-a-4-2]] (1) maps the exact K-weight β_K to the exact zf-weight β_K − 1
([[eq:iii-a-4-3]]) and (2) maps it back ([[eq:iii-a-4-5]]); the losses ε there sit at 𝓘 and scf only. The constants are
bounded for β_K in compact subsets of (0, ∞) ∖ (ℕ ∪ Re π_1E_K), the other data fixed.

*Proof.* The chain below [[prop:iii-a-4-2]] is: [[lem:ii-g1-2-2]], Plancherel as an equivalence of norms at every
weight; [[prop:ii-g1-2-8]], which converts H^(β−1/2) into |σ|^(β−1) L²(|dσ/σ|) modulo the Taylor polynomial, in both
directions, for β ∈ (0, ∞) ∖ ℕ, losing derivatives only, through the Hardy inequalities of [[lem:ii-g1-2-3]] (b)–(c),
whose constants are built from 2^(±(θ−1/2)), θ the fractional part of β − 1/2, and are bounded for |θ − 1/2| ≥ c,
that is, for β away from ℕ; and [[prop:ii-g1-3-3]] (1) and [[prop:ii-g1-3-5]] (1), exact at K, whose loss ε is at scf.
The proof of [[prop:iii-a-4-2]] raises its auxiliary weight β̃_K back to β_K, with the full weight β_K at K, and
integrates at zf by [[lem:iii-a-1-2]] at weights different from the exponents, with the constant of [[eq:iii-a-1-2]],
the reciprocal of the distance of the weight from the exponent, bounded away from them. The losses of derivatives are
piecewise constant in the weights. ∎

At the weights used below, α, α − 1 and α − 2, the fractional part of β − 1/2 differs from 1/2 by
α − 4 ≥ ε_K − ε′_0 > 0.

**Lemma {#lem:iii-j3-4-2}** ([[lem:iii-i10-2-4]] (b) without δ.) Under the hypotheses of [[lem:iii-i10-2-4]], (b) holds
with O(t^(−β−1)) in place of O(t^(−β−1+δ)), also after applying (t∂_t)^l.

*Proof.* ∫_(|σ|<1/|t|) |σ|^β dσ = (2/(β + 1)) |t|^(−β−1) (β > −1). On (1/|t|, c), integrate by parts m := ⌈β⌉ + 1
times, using |∂^j_σ(χ r^±)| ≤ C|σ|^(β−j) (from the hypothesis and ∂^j_σ = σ^(−j) Σ_(i≤j) a_(ji) (σ∂_σ)^i): the boundary
terms at |σ| = 1/|t| are O(|t|^(−β−1)), and the integral is at most

    |t|^(−m) ∫_(1/|t|)^c σ^(β−m) dσ ≤ |t|^(−β−1)/(⌈β⌉ − β),

with ⌈β⌉ − β > 0 as β ∉ ℕ₀. And t∂_t ℱ⁻¹v = ℱ⁻¹(−(1 + σ∂_σ)v) preserves the hypothesis. ∎

**Proposition {#prop:iii-j3-4-3}** ([[prop:iii-i11-3-1]] at exact weights.) Let α satisfy [[def:iii-j3-1-3]], and let
f^♭ and u_I be as in [[prop:iii-j3-3-4]]. Run [[prop:iii-i11-3-1]] with the zf-parameter 0 (zf-weights
ℓ_j := α − 1 − j, ℓ_3 := α − 4 ∈ (0, ε_K]), the level-2 threshold Re α_0 < 2 + ε_+, μ_2 := 2 + η^0_2 (the value fixed
in [[sec:iii-i11-1]]), μ′ := 2 + ε_+, and the first level-3 tf-weight τ_3 := 1 + ε_+. Then [[eq:iii-i11-3-1]] holds
with ι⁺-data (ℰ_ι, 3 + ε_+) for v_low minus the constant columns and with K⁺-weight α − 2, with the same S_ν;
[[eq:iii-i11-3-2]] of [[lem:iii-i11-3-2]] and [[eq:iii-i11-4-2]] of [[thm:iii-i11-4-1]] hold at K⁺-weight α − 2; and
all tensors are those of the construction of [[prop:iii-i11-3-1]].

*Proof.* We follow the steps of the proof of [[prop:iii-i11-3-1]]; only the weights change.

*Step 0.* [[lem:iii-i2-4-1]] with β_K = α ∈ (4, 5), then [[prop:iii-a-4-2]] (1) with β_ι = w_+, E_ι = ℰ^♭ + 2,
E_I = ∅, β_K = α, E_K = ∅; its hypotheses hold (w_+ ∉ Re π_1E_ι by (Ex1); ℓ_I + 1 > w_+ − 1 by (H4) of
[[sec:iii-i10-1]]). By [[prop:iii-j3-4-1]], g_0 ∈ H^(∞,(5/2−ε,(ℰ^♭+1,w_+−1),((0,0),α−1)))_b.

*Levels 0–1.* [[lem:iii-i11-2-1]] at μ′ = w_+ − 1 and 3 + ε_+ rests on [[lem:iii-a-1-4]] at β = μ′ − 2 = 2 + ε_+,
resp. 1 + ε_+: not the real part of a root, since these numbers are not integers and the non-integer roots with
|μ| ≤ 50 have d(Re μ, ℤ) ≥ ε_ind > ε_+ ([[eq:iii-f1-2-2]]). [[lem:iii-i11-2-2]] lowers the tf-weight by 1 and the
zf-weight ((0,0), z) to ((0,0), z − 1) exactly. [[prop:iii-g4-4-4]] at level 1 with ℓ_zf = α − 2: its conditions
[[eq:iii-g4-4-2]] hold (−ε_ind < α − Re α_0; α − 2 − min(Re α_0 − 2, 0) < 3 = ℓ^max_K under (C5) of
[[sec:iii-i10-1]]; α − 2 ∉ ℕ₀; the root condition is (Ex4)), and its remainder keeps zf ((0,0), α − 2) exactly. So g_1,
g_2 have tf-weights 3 + ε_+, 2 + ε_+ and zf-weights α − 2, α − 3.

*Level 2.* The tf-exponents of the level-2 right sides are u-exponents minus 1, (Λ − 1)-valued; by (Ex1) none has real
part in (2, 2 + ε_+], so the threshold 2 + ε_+ treats the same (α_0, k) as 2 + η^0_2, and the conditions of
[[prop:iii-g4-4-4]] are those already met (with (Ex4) at ℓ_zf = α − 3). After the rounds the zf-coefficient F of the
level-2 right side lies in H^(∞,(E,2+ε_+))_b(X̄) with min Re E > 2 + ε_+. [[lem:iii-i11-2-1]] with μ = μ_2 and
μ′ = 2 + ε_+: μ_2 ∈ (2, 3), μ′ ∈ (μ_2, 5], min Re E > μ; [[prop:iii-h-3-2]] at the interior weight
μ_2 − 2 = η^0_2 ∈ (0, 1); [[lem:iii-a-1-4]] up to μ′ − 2 = ε_+, not a root, as no root has real part in (0, 1]
([[prop:iii-f1-2-3]] (a)). So û_2 ∈ H^(∞,ε_+)_b, and [[lem:iii-i11-2-2]] gives g_3 of tf-weight exactly 1 + ε_+, with no
tf-exponent of real part ≤ 1 + ε_+ (the exponents of E − 1 exceed 1 + ε_+; those of 2 + ℰ_col are ≥ 2), and zf
((0,0), ℓ_3).

*Level 3.* [[prop:iii-g4-5-1]] at α_τ = 1 + ε_+, ℓ_zf = ℓ_3: α_τ ∈ (1, 2); w := ℓ_3 − α_τ + 2 = ℓ_3 + 1 − ε_+ ∈
(1 − ε_+, 1), as 0 < ℓ_3 ≤ ε_K < ε_+ ([[eq:iii-i9-1-1]]), so −ε_ind < w < ℓ^max_K; ℓ_3 ∉ ℕ₀; w ≠ −μ and
2 − α_τ = 1 − ε_+ ≠ −μ, as both lie within ε_+ < ε_ind of the integer 1 without being integers ([[eq:iii-f1-2-2]]).
Its proof uses the conditions
2 − α_τ + j ≠ −μ only for j ≤ ⌊ℓ_zf⌋ = 0. The output is exact at tf and zf: the piece σ³u has tf-weight 2 + ε_+ and
zf ((0,0), ℓ_3). Later rounds start from tf-weights ≥ 1 + ε_+ + ε_ind − ε, with fixed room above 2 + ε_+ − 1; their α_τ
may be lowered freely, so their conditions hold off a finite set of α_τ, and their zf-weight ℓ_3 is kept. The final
zero-energy solve: [[lem:iii-i2-4-2]] with β_zf := ℓ_3 ([[lem:iii-i2-4-2]] puts no condition on β_zf) and
β_tf − β_zf ∈ (0, 1) gives ḃ_f, S_f ∈ H^(∞,ℓ_3)_b and û_f with zf-weight ℓ_3.

*Step 5.* [[lem:iii-j3-4-2]] with β := α − 3 ∉ ℕ₀: the exponents with Re z < α − 3 are in E, those above in r^±, none
at α − 3 by (Ex3); r^± = O(|σ|^(α−3)) follows from the zf-weight α − 3 of σ³ĥ^aug(S_f) by the one-dimensional
b-Sobolev embedding in log|σ|. This gives O(t_*^(−α+2)) in {r ≤ R}; Step 6 needs only o(t_*^(−2)).

*Step 7.* The pieces have zf-data ((0,0) ∪̄ (E_K − 1), α − 3) and tf-data (E_tf, 2 + ε_+) with E_tf + 1 Λ-valued below
3 + ε_+: the zero-energy pieces σ^j χ_zf û_j (j ≤ 2) at tf 2 + ε_+; the tf-model pieces, polyhomogeneous at tf; the
first level-3 round at 2 + ε_+ and the later ones above. [[prop:iii-a-4-2]] (2) with β_ι := 3 + ε_+ (not in
Re π_1E_ι by (Ex1)) and β_K := α − 2 (not in ℕ ∪ Re π_1E_K by admissibility) gives v_low minus the constant columns in
H^(∞,3/2−4ε,(E_ι,3+ε_+),(E_K,α−2))_b; the constant columns are polyhomogeneous at ι⁺ with Λ-valued exponents, none at
3 + ε_+. The matching and the identification of the coefficients are as in the proof of [[prop:iii-i11-3-1]].
[[lem:iii-i11-3-2]] and [[thm:iii-i11-4-1]] need only the count of Step 0, which has room (w_0 + a_K > α).

*At a rotating b.* The v1 terms of the spectral phase at level 1 and real part 2 are the rotation rows with the
coefficients of [[prop:iii-i15-2-2]] (b), read from the tf-data, which do not depend on the loss; the argument above is
unchanged.

*Same tensors.* Moving μ′ only moves where [[lem:iii-a-1-4]] stops; the level-2 solve is at μ_2 as before (the inverses
of [[prop:iii-h-3-2]] at two such weights agree); the threshold treats the same exponents; and [[prop:iii-g4-5-1]]
solves by Mellin inversion on Re λ = α_τ − 2, and moving that line from η^0_2 − 1 − 2ε to ε_+ − 1 crosses no root (a
root in (−1, −1 + ε_+] would lie within ε_+ < ε_ind of −1). ∎

**Lemma {#lem:iii-j3-4-4}** ([[lem:iii-i12-2-2]] in L².) In [[lem:iii-i12-2-2]] let a > −1 with a + 2, a + 3 ∉ ℕ. Then
A ∈ Ḣ^(∞,a+2)_b, B ∈ Ḣ^(∞,a+3)_b, and the remainders R_S, R_b have K⁺-order a + 4 in the L²-b sense:
χ_({r≤t_*/8}) R_S ∈ t_*^(−a−4) r⁻¹ H^∞_b (L² in |dt_*/t_*|, locally in x, with b-derivatives), and likewise R_b.

*Proof.* A and B are exact by [[prop:ii-g1-2-8]] (2) at the non-integer weights a + 2, a + 3 (zf-weights a + 1, a + 2
of −χσS and iχσ²ḃ, zero Taylor polynomial). With a_0 := ℱ⁻¹[−χσS] ∈ H^(∞,a+2)_b(ℝ) and ∂_t = t⁻¹(t∂_t) on t ≥ 1,
a_0″ ∈ t^(−a−4) H^∞_b([1, ∞), |dt/t|). The remainder is

    −h(S) ∫∫_0^1 τ² θ a_0″(t − θτ) dθ φ_x(τ) dτ

plus the h̆-term with τa_0″. On {r ≤ t/8, t ≥ 8}, supp φ_x ⊂ [0, 4 max(r, 1)] ⊂ [0, t/2], so t − θτ ∈ [t/2, t],
t^(a+4) ≤ C(t − θτ)^(a+4) and dt/t ≤ 2 d(t − θτ)/(t − θτ); Minkowski's inequality in (θ, τ) bounds
‖t^(a+4) ·‖_(L²(|dt/t|)) by C max(r, 1)² ‖a_0‖_(H^(2,a+2)_b). The field t∂_t commutes with the translation up to the
factor t/(t − θτ) ∈ [1, 2] and its derivatives, and the x-derivatives fall on φ_x, h and h̆; with |h| ≲ r⁻³ and
|h̆| ≲ r⁻² this is t^(−a−4) r⁻¹ in L². ∎

The same applies to the Taylor remainder of the piece (vii) of [[thm:iii-i12-3-1]] (of K⁺-order at least α): taking the
Taylor order one higher makes its pointwise order strictly greater than α, hence its L²-order at least α.

**Lemma {#lem:iii-j3-4-5}** ([[lem:iii-i12-2-1]] (a) in L².) In [[lem:iii-i12-2-1]] (a), if moreover w + 1 ∉ ℕ, then
χ_+ y ∈ Ḣ^(∞,w+1)_b exactly.

*Proof.* The coefficient is χ_+ ℱ⁻¹(χc) with c of zf-weight w; [[prop:ii-g1-2-8]] (2), with zero Taylor polynomial and
β = w + 1 ∉ ℕ, gives the exact weight. A proof by symbol estimates is pointwise and gives only the L²-weight (w + 1)−.
∎

**Proposition {#prop:iii-j3-4-6}** ([[thm:iii-i12-3-1]] at exact weights.) Let α satisfy [[def:iii-j3-1-3]] and let the
right sides be as in [[prop:iii-j3-3-4]] and [[prop:iii-j3-4-3]]. Then [[thm:iii-i12-3-1]] holds with
Ṡ_rem ∈ Ḣ^(∞,α−2)_b, ḃ_rem ∈ Ḣ^(∞,α−1)_b, w_ρ := 3 + ε_+ − d_ρ with
Ẏ_ρ ∈ Ḣ^(∞,𝒬(ℰ_♯−d_ρ,3+ε_+−d_ρ))_b, and ũ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_♯,3+ε_+),α)_b.

*Proof.* *Step 0.* f′ has K⁺-weight α: G(W⃗) ∈ 𝒴^0_ex(α); (L − L_b)u_0 has K⁺-weight w_0 − ε + a_K > α for small ε (the
weight α − ε there is a free weakening); the graft by [[prop:iii-j3-3-4]]; and L_b m_ν is of order > 9/2 > α.

*Step 1.* (ii) by [[prop:iii-j3-3-4]]. (vi), (viii): the zf-remainders have weight ℓ_zf + j = α − 1 by
[[prop:iii-j3-4-3]], and [[prop:iii-a-4-2]] (2) at β_K = α (its Taylor coefficients below α − 1 vanish on both sides)
gives K⁺-order α. (vii): after [[lem:iii-j3-4-4]]. (ix): σ³û_f has zf-weight ℓ_3 + 3 = α − 1, so K⁺-order α, and
[[lem:iii-j3-4-4]] with a = ℓ_3 gives A ∈ Ḣ^(∞,α−2), B ∈ Ḣ^(∞,α−1) and R_S, R_b of L²-order α.

*Step 2.* u has K⁺-order α − 2 ([[prop:iii-j3-4-3]]); χ_K C has order ≥ α − 2; the coefficient sections at exponents
with real part < α − 2 vanish as before, none at α − 2 by (Ex3).

*Step 3.* [[lem:iii-i12-2-4]] at β := α, as it allows (β ∈ (α − 1, α]): its three meetings of an exponent with the
weight, at α, α − 2 and α − 1, are excluded by (Ex3). It gives w″ of K⁺-order α and a_s, a_b with exponents of real
part > α − 2, resp. > α − 1.

*Step 4.* Ṡ_rem = A + A_5 + a_s ∈ Ḣ^(∞,α−2) (A_5 at 2 + ε_+ > α − 2, exactly by [[lem:iii-j3-4-5]] as
2 + ε_+ ∉ ℕ); ḃ_rem = B + a_b ∈ Ḣ^(∞,α−1); ũ = w″ + w′ of K⁺-order α.

*The ι⁺-side.* The conormal tower coefficients Y^c_ρ (μ_ρ ∈ (−1, 0]) come from σ³|σ|^(α_τ−2−μ) Y(σ),
Y ∈ H^(∞,0)_b, of zf-weight 2 + ε_+ − μ; [[lem:iii-j3-4-5]] gives Ḣ^(∞,3+ε_+−μ) exactly, as 3 + ε_+ − μ ∈ ℕ would need
μ = ε_+ − 1, excluded as at level 3 in the proof of [[prop:iii-j3-4-3]]. No polyhomogeneous coefficient sits at w_ρ.
Let z be an exponent of a_ρ. If d_ρ lies below the degree of the conormal part of every profile whose coefficient at z
is nonzero, z falls under the clause of [[lem:iii-i12-2-4]] on exponents, so z + d_ρ is Λ-valued and ≠ 3 + ε_+ by
(Ex1). Otherwise some such profile has a conormal part of degree d′ ≤ d_ρ. That profile is a conormal profile at the
edge: û_j, j ≤ 2, of degree d′ = μ′_j − 2 ∈ {2 + ε_+, 1 + ε_+, ε_+}, or v_0, of degree d′ = ε_+ − 1; and
z + d′ = 3 + ε_+. As d_ρ ∈ {μ, 0, 1} differs from each of these degrees (μ = ε_+ − 1 being excluded as above), d′ < d_ρ,
so z + d_ρ > 3 + ε_+.

*The corner.* Near 𝓘⁺ and on {r ≥ t_*/2}, χ_K = 0 and ũ = u, exact at ι⁺ by [[prop:iii-j3-4-3]] (with u_I of
[[prop:iii-j3-3-4]]). On the transition region {t_*/8 < r < t_*/2}, away from the corner, ũ = u − χ_K u_exp with both
terms exact at ι⁺: u by [[prop:iii-j3-4-3]], and u_exp as a sum of coefficients of exact order times homogeneous or
exact-degree profiles, exact at ι⁺ where r ∼ t_*. Near the corner of ι⁺ and K⁺, ũ is the sum over the pieces of Step 1
of the proof of [[thm:iii-i12-3-1]] of each piece minus its part in χ_K u_exp. Two kinds of piece reach ι⁺-order
exactly 3 + ε_+. The first is the conormal parts of (v), and of the pieces of type (v) inside (vi) and (viii). These
come from [[lem:iii-i12-2-1]] (b) with c = σ^j |σ|^k sgn(σ)^δ (m = 0) and a single profile, whose conormal part lies in
the exact space of its degree ([[prop:iii-j3-4-3]]). The second is the level-3 towers of (viii). These come from
[[lem:iii-i12-2-1]] (a) with w = α_τ + 1 − μ and the profiles of the tower, homogeneous of degree d_ρ − j
([[sec:iii-i12-1]]), so w + 1 + d_ρ = α_τ + 2 = 3 + ε_+. For each, the part in χ_K u_exp is the main term
χ_K Σ_j (χ_+ y)^(j) p_j of [[eq:iii-i12-2-1]], and what is left in ũ is its R. This is literal for the conormal towers.
For the pieces of type (v) the main terms are reorganised by [[lem:iii-i12-2-4]] (Step 3), and the coefficient sections
at exponents below α are exactly sums of states ([[lem:iii-i12-2-3]] (a)), so again what is left is R and terms of the
kinds below; so the dichotomy below is exhaustive. [[lem:iii-j3-4-7]] puts R in ρ_+^(3+ε_+) ρ_K^κ H^∞_b near the
corner, for every κ. Every other term of ũ there is exact at one face with room at the other ([[lem:iii-j3-2-1]]): it
has K⁺-order ≥ α (Steps 0–4) and either ι⁺-order > 3 + ε_+, or is polyhomogeneous at ι⁺ with exponents in ℰ_♯, none of
real part 3 + ε_+ (Ex1). So ũ has (ℰ_♯, 3 + ε_+) at ι⁺ jointly with α at K⁺. ∎

**Lemma {#lem:iii-j3-4-7}** ([[lem:iii-i12-2-1]] at the corner, in L².) In [[lem:iii-i12-2-1]], near the corner of ι⁺
and K⁺, on {r ≥ 2, t_* ≥ 8r} with ρ_+ = 1/r and ρ_K = r/t_*, and in the b-Sobolev spaces of the density
(dt_*/t_*)(dr/r) dω (that of μ_b there):

(a) in case (a), if |(r∂_r)^a ∂_ω^β p_j| ≲ r^(j−d) on {r ≥ 1} for all a, β (degree exactly d − j, without logarithms),
then R ∈ ρ_+^(w+1+d) ρ_K^κ H^∞_b for every κ;

(b) in case (b) with m = 0, if r^(d−j) p_j ∈ H^∞_b near ∂X for the density |(dr/r) dω|, then
R ∈ ρ_+^(Re z+1+d) ρ_K^κ H^∞_b for every κ. Moreover, on {r ≥ 2} the left side of [[eq:iii-i12-2-1]] is
Σ_j r^(−1−j−z) F_j(t_*/r) p_j(x), with

    F_j(s) := (1/(2π)) ∫ e^(−iζs) χ_0(|ζ|) (−iζ)^j |ζ|^z sgn(ζ)^δ dζ

smooth and bounded with all its s∂_s-derivatives on bounded sets.

*Proof.* Put s := t_*/r ≥ 8. Then (dt_*/t_*)(dr/r) = (ds/s)(dr/r), and the b-vector fields t_*∂_(t_*), r∂_r are s∂_s
and r∂_r|_s − s∂_s. So it suffices to bound r^a s^κ R, a the stated ι⁺-weight, in L²((ds/s)(dr/r) dω), and likewise
after applying s∂_s, r∂_r|_s and ∂_ω. As in the proof of [[lem:iii-i12-2-1]], R = Σ_j e_(j,r)(t_*) p_j(x) there, and
σ = ζ/r gives

    e_(j,r)(t_*) = r^(−1−j) (1/(2π)) ∫ e^(−iζs) (−iζ)^j (χc)(ζ/r) (χ_0(|ζ|) − 1) dζ.

The amplitude vanishes for |ζ| ≤ c_0 and for |ζ| ≥ r. Integrating by parts M times gives s^(−M) times the integral of
the M-th ζ-derivative of the amplitude. A derivative falling on (χc)(ζ/r) gives ζ⁻¹((σ∂_σ)(χc))(ζ/r), and one falling
on χ_0(|ζ|) − 1 gives a factor supported in {c_0 ≤ |ζ| ≤ 1}.

(a) Write (σ∂_σ)^l (χc) = |σ|^w c̃_l with c̃_l ∈ H^∞_b(±(0, 1), |dσ/σ|). Then

    |e_(j,r)(t_*)| ≤ C r^(−1−j−w) s^(−M) Σ_l ∫_(|ζ|≥c_0) |ζ|^(w+j−M) |c̃_l(ζ/r)| dζ.

By Minkowski's inequality and the dilation invariance of dr/r,

    ‖∫_(|ζ|≥c_0) |ζ|^(w+j−M) |c̃_l(ζ/r)| dζ‖_(L²(dr/r)) ≤ ‖c̃_l‖_(L²(dσ/σ)) ∫_(|ζ|≥c_0) |ζ|^(w+j−M) dζ < ∞

for M > w + j + 1, uniformly in s. As |r^(d−j) p_j| ≤ C,
‖r^(w+1+d) s^κ R‖_(L²) ≤ C(∫_8^∞ s^(2(κ−M)) ds/s)^(1/2) < ∞ for M > κ. The field s∂_s acting on e^(−iζs) is ζ∂_ζ,
moved onto the amplitude by parts; r∂_r|_s acting on (χc)(ζ/r) gives −((σ∂_σ)(χc))(ζ/r). Both keep the form above,
and (r∂_r)^a ∂_ω^β p_j keeps the bound.

(b) Here (χc)(ζ/r) = r^(−z) |ζ|^z sgn(ζ)^δ χ(ζ/r), and the derivatives of the amplitude are O(|ζ|^(Re z+j−M)) uniformly
in r (a derivative of χ(ζ/r) gives r⁻¹ ≤ |ζ|⁻¹ on its support). So e_(j,r)(t_*) = r^(−1−j−z) E_j(s, r) with
|(s∂_s)^a (r∂_r|_s)^b E_j| ≤ C_(ab) s^(−M) for M > Re z + j + 1, and

    ‖r^(Re z+1+d) s^κ R‖_(L²) ≤ C Σ_j (∫_8^∞ s^(2(κ−M)) ds/s)^(1/2) ‖r^(d−j) p_j‖_(L²((dr/r)dω)),

likewise with b-derivatives. For r ≥ 2, χ = 1 on the support of χ_0(|σ|r), so the left side of [[eq:iii-i12-2-1]] is
Σ_j (y^(j) ∗ k_r)(t_*) p_j(x), with

    (y^(j) ∗ k_r)(t_*) = r^(−1−j) (1/(2π)) ∫ e^(−iζs) χ_0(|ζ|) (−iζ)^j c(ζ/r) dζ = r^(−1−j−z) F_j(s).

F_j is the inverse Fourier transform of a compactly supported integrable function, as Re z + j > −1, so it is smooth;
and s∂_s F_j is the same transform of −∂_ζ(ζ ·) applied to the amplitude, again integrable. ∎

### The theorems at exact weights {#sec:iii-j3-5}

**Lemma {#lem:iii-j3-5-1}** (The step at λ_0 of the construction of [[thm:iii-j-2-4]] at the exact K⁺-weight.) For
each λ_0 ∈ Λ_* fix δ_(λ_0) ∈ (0, δ_1], δ_1 := min(min_ν(κ_ν − ε), Re λ_0 + 3) − α > 0, such that no −μ and no point of
Re π_1ℰ_K lies in (ℓ_K(λ_0), ℓ′_K], ℓ′_K := ℓ_K(λ_0) + δ_(λ_0) < 3. Then the t_*^(−λ_0)-term [h]_(λ_0) of the
construction has K⁺-order exactly α (with room), in place of α−.

*Proof.* The right side f = −F_0(λ_0) − L̄T(λ_0) of the step has room: F_0 is compactly supported in (ι⁺)°
([[lem:iii-j-2-1]]), and the coefficients of L̄T(λ_0) have K⁺-order ≥ min(κ_ν − ε, Re λ_0 + 3) > α, as κ_ν − ε > 9/2
and Re λ_0 + 3 ≥ λ_♯ + 3 > 9/2; so its coefficients lie in H^(∞,ℓ′_K−2)_b at R = 0. [[cor:iii-g3-3-1]] (2) and
[[rem:iii-g3-3-3]], for every solution of the form [[eq:iii-g3-3-2]] and every ℓ_K < ℓ^max_K, apply at ℓ′_K to the same
v = u_(λ_0) + 𝒮_(λ_0)(f) (to u_(λ_0) by [[lem:iii-j-1-2]]), giving v = χ_K v′_0 + ṽ′ with
ṽ′ ∈ Σ_j t_*^(−λ_0) (log t_*)^j H^(∞,ℓ′_K)(ι⁺). By the choice of δ_(λ_0), v′_0 has the same formal solutions as v_0, all
of rate < α, which the rows and towers of [[thm:iii-j-2-4]] remove. So [h]_(λ_0) = ṽ′ plus terms of order
≥ Re λ_0 + 3 > α; and a term t_*^(−λ_0) (log t_*)^j w, w ∈ ρ_K^(ℓ′_K) H_b, lies in ρ_K^(α+δ_(λ_0)−η) H_b for every
η > 0, hence in ρ_K^α H_b, its ι⁺-factor being an index-set term. Here the room is real, so no circle family is needed.
∎

**Proposition {#prop:iii-j3-5-2}** ([[lem:iii-i14-2-2]]–[[lem:iii-i14-2-4]] with q ∈ 𝒬_ex.) (a) h_rem(q) has K⁺-order
exactly α − 2; (b) L_b h_(b,rem)(q) has K⁺-order exactly α, smoothly in b; (c) at the top level of
[[thm:iii-i14-3-1]], R_q u ∈ 𝒴^0_(ex,2)(α) and Δ_q(b′) ∈ 𝒴^♮_(ex,2)(α).

*Proof.* (a) h^(≤1)(S_rem) and ġ(b_rem) are linear in S_rem, b_rem and their t_*-derivatives with stationary tensors,
and ∂_(t_*) = t_*⁻¹(t_*∂_(t_*)) shifts an exact weight by exactly 1; the polyhomogeneous Y_ρ-terms have
rates > 2 + ε_K ≥ α − 2 and Y^c_ρ the rate 3 + ε_+ − d_ρ > α − 2 (room). (b) L_b h^(≤1)(S) = S″(L_2h + L_1h̆¹) + S‴L_2h̆¹
and L_b ġ(b) = b′L_1ġ + b″L_2ġ (the proof of [[lem:iii-i14-2-2]]), with S″, b′ exact at α; the ι⁺-weights of the
profiles have room ([[lem:iii-j3-2-1]]) and the towers give rates ≥ λ_♯ + 3 > α. (c) R_q u: the "every β < w + α − 2"
of [[lem:iii-i14-2-3]] is used at the top level with w > 2, so β = α is admitted strictly; its ι⁺-weight
β′_+ + 2 + λ_♯ − ε > w_+ has room. Δ_q(b′): its first term is (b), exact at α; its products have factors of K⁺-order
α − 2 (exact) or α, times ∂_b h_(b,rem)(q)b′ of order > 2 strictly (rates of q: α − 2 > 2, α − 1, and > 2 + ε_K), so
each is at K⁺-order > α; at ι⁺ the exponents are in Λ, none at 3 + ε_+ by (Ex1), and the conormal parts at
3 + ε_+ + η_E have room. ∎

**Theorem {#thm:iii-j3-5-3}** (The forward problem with parameters at exact weights.) Assume [[def:iii-j3-1-3]], (H2)
of [[sec:iii-i9-1]] read as a_K = α and (H5) of [[sec:iii-i14-1]] as a_+ ≤ 3 + ε_+. Let h ∈ 𝒳^∞_(J,ex), p⃗ ∈ 𝒫 with
black hole parameter b ∈ ℬ̄_*, and q ∈ 𝒬_ex be small, and F ∈ 𝒴^♮_ex(α). Then the p⃗′ of [[thm:iii-i14-3-1]] (at a
rotating b, of [[prop:iii-i15-2-5]]) is unchanged, the forward solution u has K⁺-weight α − 2 and every ι⁺-weight
β_+ < min(3/2, min Re ℰ_+), and u = h_rem(q′) + h′ with q′ ∈ 𝒬_ex and

    h′ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_♯,3+ε_+),α)_b(Ω_*; S²T*)^(•,−).                                          {#eq:iii-j3-5-1}

The maps F ↦ (p⃗′, q′, h′) are linear and bounded between these fixed-weight spaces, uniformly for small background and
in b.

This is [Hin26, Corollary 11.66, pp. 294–295] with [Hin26, (11.234)], in dimension 4 + 1.

*Proof.* Steps 0–1 of the proof of [[thm:iii-i14-3-1]], and its Step 2 at the levels below α, are unchanged: their
inputs lie in the "w−" classes ([[rem:iii-j3-1-2]]) and their outputs feed only open conditions. At the top level,
G̃ = F − Δ_q(p⃗′) − R_q u ∈ 𝒴^♮_ex(α) by [[prop:iii-j3-5-2]]; G′ adds f^S, f^b, f^s1, linear in h with stationary
coefficients and so exact at a_K = α ([[lem:iii-i9-2-6]] (a)), and r^ν at Re e_ν + α − ε > α. [[prop:iii-i13-2-1]] at the
level α runs the constructions of [[prop:iii-i11-3-1]]–[[thm:iii-i12-3-1]] at that level, which [[prop:iii-j3-3-4]],
[[prop:iii-j3-4-3]] and [[prop:iii-j3-4-6]] make exact. Step 3 and its uniqueness are unchanged (𝒵_ex ⊂ 𝒵); Step 4′
uses G̃_0 ∈ 𝒴^♮_ex(α), and its comparisons have room (δ′ = ½ min(ε_K, α − 4)); Step 4 is [[prop:iii-j3-4-6]]. The
coefficients killed by "rate ≤ 2 < α − 2" are killed as before. The tensors are those of [[thm:iii-i14-3-1]]; only the
weights in which they are estimated change.

At a rotating b the same argument applies to [[prop:iii-i15-2-5]]. The errors E^ν are exact there, having K⁺-weight
κ_ν − ε > α and ι⁺-exponents in ℰ^♮ + 2, which (Ex1) covers ([[lem:iii-i13-1-3]] (a)); A_b does not depend on the loss,
being computed from ι⁺- and tf-data ([[rem:iii-i15-2-6]]); and the errors of the identification of the rotation rows
have K⁺-order Re λ_0 + 1 − ε > α − 2, with room. Step 4′ is not used at b, the condition [[eq:iii-i15-2-2]] of
[[prop:iii-i15-2-5]] replacing it; the uniqueness of [[prop:iii-i15-2-5]] together with [[eq:iii-i15-2-2]] identifies the
exact and the "w−" solutions, as A_b is the same on both classes. [[prop:iii-j3-3-4]] and [[prop:iii-j3-4-3]] carry the
rotation rows of [[prop:iii-i15-2-2]]. ∎

**Proposition {#prop:iii-j3-5-4}** ([[thm:iii-j-2-4]] and [[eq:iii-j-2-5]] at exact weights.) For U ∈ 𝒟^∞_ex small,
Φ(U) ∈ 𝒳^∞_(J,ex) × 𝒫 × 𝒬_ex, and P_5(Φ(U)) ∈ ℱ^(k−2)_ex for U ∈ 𝒟^(k+d)_ex; the same holds for D_UΦ and
D_(Φ(U))P_5 ∘ D_UΦ; and the tame bounds of [[thm:iii-j-2-4]] and [[prop:iii-j2-4-3]] hold with these norms. The forward
map gains nothing in the weights.

*Proof.* We follow the proof of [[thm:iii-j-2-4]].

*h.* At 𝓘⁺ as before. At ι⁺ the exponents lie in ℰ_♯ ⊂ ℰ_+ ([[lem:iii-j-2-3]]) and h̃ is at the plain weight
3 + ε_+; no exponent sits at 3 + ε_+ (Ex1). At K⁺, each χ_ι[h]_(λ_0) has order α by [[lem:iii-j3-5-1]], and h̃ by
hypothesis.

*q.* Its components are S_rem, b_rem, Y_(ρ,rem), exact, plus polyhomogeneous coefficients with real parts below
3 + ε_+ − d_ρ ([[lem:iii-j-2-3]]).

*[[eq:iii-j-2-5]] at 𝓘⁺:* [[cor:iii-i-4-2]] as before; [[eq:iii-i-4-1]] is exact.

*At ι⁺:* the terms of u-exponent below 3 + ε_+ vanish by the identity [[eq:iii-j-2-3]]; the quadratic part is at
(5 + 2δ_♯)− > w_+; L_(0,p⃗_≤0) h̃ is exact at w_+ by [[eq:iii-i-4-1]]; the terms of the rows of u-exponent ≥ 3 + ε_+ are
in Λ, so above 3 + ε_+ by (Ex1), with defects at a_+ + Re λ + 2 − ε ≥ 2λ_♯ + 2 − ε > w_+; the conormal parts T_ρ(Y^c_ρ)
of the towers are diagonal terms of [[lem:iii-j3-2-1]] (c = 3 + ε_+ − d_ρ, m = d_ρ), exact at ι⁺ with K⁺-weight
c − η > α − 2, and vanish near 𝓘⁺; S_rem, b_rem give ι⁺-orders above 3 + ε_+ ([[lem:iii-j3-2-1]] with their profiles);
P_4(0, p⃗_≤0) is compactly supported in (ι⁺)°. So the result has the plain weight w_+.

*At K⁺:* L_b h has order α (L_b is stationary and a b-operator there, [[sec:iii-i-4]]); the nonlinear part is ≥ 2α;
P_5 − P_4 = L_b h_(b,rem)(q) + ∫(…), the first exact at α ([[prop:iii-j3-5-2]] (b)), the integral ≥ 2α − 4 > α; the
rows enter through ϑ_(ν,♯) at κ_ν − ε > α, the rotation rows at Re λ + 4 > α. Products of exact weights are exact
([[lem:ii-g-4-1]] (2), ρ^a ρ^b = ρ^(a+b)).

*Linearisation and tameness.* Φ = Φ_0(U_0) + A(U_0)U_1 ([[eq:iii-j-2-4]]), and the δ_(λ_0) depend only on λ_0, so D_UΦ
is the same construction with the same classes; the proof of [[prop:iii-j2-4-3]] is unchanged with fixed weights. ∎

**Theorem {#thm:iii-j3-5-5}** (The right inverse at exact weights.) There is d such that for U ∈ 𝒟^∞_ex, small in
𝒟^d_ex, whose black hole parameter then lies in ℬ_*, and f ∈ ℱ^∞_ex, there is U′ ∈ 𝒟^∞_ex with [[eq:iii-j1-2-1]],
linear in f, with ‖U′‖_(𝒟^k_ex) ≤ C_k ‖f‖_(ℱ^(k+d)_ex), C_k independent of U. At a rotating black hole parameter, U′ is
built from the solution map of [[prop:iii-i15-2-5]].

This is [Hin26, Theorem 12.8, p. 312] in dimension 4 + 1.

*Proof.* Step 0: Φ(U) is admissible in [[thm:iii-j3-5-3]] ([[prop:iii-j3-5-4]]), and f ∈ ℱ_ex ⊂ 𝒴^0_ex(α)
([[rem:iii-j3-1-2]]); [[thm:iii-j3-5-3]] gives (h′, p⃗′, q′) in the exact classes, with (H5) satisfied as a_+ = 3 + ε_+.
Steps 1–2 of the proof of [[thm:iii-j1-2-1]], which hold at b with the rows built at b_0 ([[sec:s23-base-points]] (3)),
subtract values of D_UΦ, which lie in the exact classes and whose images under D_(Φ(U))P_5 lie in ℱ_ex
([[prop:iii-j3-5-4]]); Step 2 reads g_j at ℓ_K(λ_0) − ε, a loss it tolerates, as it needs only the formal solutions of
rate < α to be visible below ℓ_K. Step 3: after the subtractions h′ has no ι⁺-term below 3 + ε_+, so its class
(ℰ_♯, 3 + ε_+) with vanishing coefficients is the plain weight 3 + ε_+, and its K⁺-weight is α; so h′ is in the exact class of h̃,
and the conormal parts of q′ have the exact orders. The bounds compose finitely many bounded maps; the order d is fixed
by [[lem:iii-j2-2-3]]. ∎

The ι⁺-order of [[lem:iii-j1-1-1]] is thus exactly 3 + ε_+ under (Ex1); its choice η_2 := ε_+ − 3ε and the resulting
loss 5ε are not needed.

### Tame estimates on one pair of scales {#sec:iii-j3-6}

**Corollary {#cor:iii-j3-6-6}** (The tame theorems without loss in the weights.) Let 𝒟^k := 𝒟^k_ex and ℱ^k := ℱ^k_ex.
Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with the input and the output at the same fixed weights
(ε′ = ε = 0 in [[sec:iii-j2-1]]), and [[prop:iii-j2-4-3]] maps 𝒟 to ℱ on these scales: the right inverse and the forward
map act on one pair of Banach scales. This holds at every base point U small in 𝒟^d_ex, whose black hole parameter
then lies in ℬ_*, with constants uniform in U.

*Proof.* The calculus of [[sec:iii-j2-1]] and [[lem:iii-j2-2-3]] are statements about graded Banach spaces; take the
exact spaces. The elementary families of [[lem:iii-j2-2-1]] are tame between fixed-weight spaces: the forward solutions
([[thm:iii-i-5-3]], exact), the background coefficients (products of exact weights, [[lem:iii-j2-2-4]]), the
finite-dimensional maps, the integrations ([[lem:iii-a-1-2]] and [[lem:iii-a-3-2]], without loss at weights that are
not exponents), and the model inverses, all stated at fixed weights. The statements of [[sec:iii-j3-1]]–[[sec:iii-j3-5]]
are finite compositions of these families at fixed weights with fixed losses: [[cor:iii-j3-3-2]] is
[[thm:iii-g2-4-2]] on a fixed circle with the Mellin inverse of [[lem:iii-j3-3-3]] and the Cauchy integrals of
[[lem:iii-j3-2-2]] (constants Cδ^(−k−l_0−1), δ fixed); [[prop:iii-j3-3-4]], [[prop:iii-j3-4-3]] and
[[prop:iii-j3-4-6]] replace weights, not maps, in the entries of [[sec:iii-j2-3]]; [[lem:iii-j3-4-2]],
[[lem:iii-j3-4-4]] and [[lem:iii-j3-4-5]] are fixed maps; [[lem:iii-j3-5-1]], [[prop:iii-j3-5-2]] and
[[prop:iii-j3-5-4]] are compositions of the maps of [[thm:iii-j-2-4]].

The statements that are not proved anew here run at "w−" weights, with the input losses ε′(ε, k) of the closed graph
theorem ([[sec:iii-j2-1]]); among them are [[prop:iii-i2-5-1]], [[prop:iii-i3-2-1]], [[prop:iii-i5-2-1]],
[[lem:iii-i8-3-1]]–[[lem:iii-i8-3-3]] below the top level, Steps 1–2 of the proof of [[thm:iii-i14-3-1]] below α, the
spaces 𝒵_β, and the weights β_+ < 3/2 of [[lem:iii-i11-3-2]]. Their losses feed open conditions with room. Every chain
of the inventory starts from exact data (the right side in ℱ_ex and the background in its exact class), which lies in
every lossy class, and ends in a statement of [[sec:iii-j3-1]]–[[sec:iii-j3-5]] at an exact weight. So for each k the
intermediate margins can be chosen backwards from the output. This changes C_k but not the loss of derivatives d, as
these losses are ceilings of continuous functions of the weights and stay bounded as the margins shrink. So the
induction of the proof of [[thm:iii-j2-4-1]] runs from exact inputs to exact outputs, with losses independent of k, and
the input loss ε′ is 0 for every k and every statement of the inventory. The exactness of the outputs rests on
[[prop:iii-j3-4-6]], with [[lem:iii-j3-4-7]]. The proof of [[thm:iii-j2-4-2]] then gives [[eq:iii-j2-4-2]] with
ℱ^(k+d)_ex and 𝒟^k_ex, and [[prop:iii-j3-5-4]] gives [[prop:iii-j2-4-3]] on the same scales. At a base point with black
hole parameter b the results used are stated at b ([[thm:iii-j2-4-1]], [[thm:iii-j2-4-2]], [[thm:iii-j3-5-3]],
[[thm:iii-j3-5-5]]), with constants uniform in b, and the exact classes do not involve b ([[sec:iii-j3-1]]). ∎
