#### The semiclassical 3b- and eb-calculi {#sec:iv5-calc}

This section constructs the calculi of [[def:iv5-0-1]] and [[sec:iv6-2]] as instances of the parameterised scaled
bounded geometry calculus of [[thm:std-sbg-calculus]], and proves the facts about them that the chapter uses
([[prop:np-10-65-a]]). The sharp Gårding inequality is not used. Its place is taken by two estimates with explicit
margins: a bound by the supremum of the principal symbol plus a margin ([[lem:iv5-calc-garding]]), and a lower bound for
a non-semiclassical operator with positive definite principal symbol ([[lem:iv5-calc-q0]]). The dimension enters only
through the cells. Throughout, A* is the adjoint of A for the pairing ⟨·, ·⟩ of the notation above, extended to
M₀° = ℝ_t × ℝ⁴_x with |dg| = |dt dx| and with B extended from M^♭ to a smooth field on M₀ that is uniformly positive
definite; all operators in this chapter have Schwartz kernels in Ω′ × Ω′ or are differential, so the extension does not
affect any statement. Below, (S1)–(S15) are the items of [[sec:ii-a-3]], which [[thm:std-sbg-calculus]] repeats with
quotations under the same numbers, and (S16) is the item of [[thm:std-sbg-calculus]].

**Definition {#def:iv5-calc-cells}** (The cells and the calculi.) Let ℬ be the following set of charts of M₀°, each with
values in (−2, 2)⁵.

(1) U_((1),j) := (j − 2, j + 2)_t × (−2, 2)⁴_x, with φ := (t − j, x), for j ∈ ℤ.

(2) U_((2),i,±,j,k,m) := {2^k(j − 2) < t < 2^k(j + 2), 2^(k−2) < ±x^i < 2^(k+2), x^a/x^i − m_a ∈ (−2, 2) for a ≠ i},
with φ := (2^(−k)t − j, log₂(±x^i) − k, (x^a/x^i − m_a)_(a≠i)), for i ∈ {1, …, 4}, a sign ±, j ∈ ℤ, k ∈ ℕ₀ and
m = (m_a)_(a≠i) ∈ {−2, …, 2}³.

The *3b-structure* is ℬ with all scalings 1, and the *semiclassical 3b-structure* is the family (ℬ^×_h)_(h∈(0,1]), where
ℬ^×_h is ℬ with all scalings equal to h. Its operator Lie algebra is denoted 𝒱_h, and the coefficient Lie algebra of ℬ
is 𝒲. On M° = ℝ_t × (ℝ⁴_x ∖ 0), the interior of M := [ℝ̄^(1+4); {r = 0}] of [[sec:iv6-0]], fix finitely many charts
ϑ_β : U̸_β → (−2, 2)³ of 𝕊³ such that the sets ϑ_β⁻¹((−1, 1)³) cover 𝕊³, and let ℬ_eb consist of the charts

    U_(j,k,β) := (2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β,    φ := (2^(−j)t − k, log₂ r − j, ϑ_β(x/r)),

for j, k ∈ ℤ; the *eb-* and *semiclassical eb-structures* are ℬ_eb with scalings 1, respectively h.

For a countable set P′ ⊂ (0, 1] let N_(P′) := P′ × M₀°, with the scaled bounded geometry structure whose charts are
{h} × U_α → (−2, 2)⁵, (h, p) ↦ φ_α(p), with scalings h, for h ∈ P′ and U_α ∈ ℬ. A family of operators
A = (A_h)_(h∈(0,1]) on ℂ⁵-valued functions on M₀° (sections of 𝒯* in the frame dt, dx¹, …, dx⁴) restricts to the
operator A_(P′) := (A_h)_(h∈P′) on N_(P′). For a weight w on (M₀°, ℬ) and m ∈ ℝ, wΨ^m_(3b,ħ) is the space of the
families A such that A_(P′) ∈ wΨ^m_𝒱(N_(P′)) for every countable P′ ([[thm:std-sbg-calculus]], (S4), (S14)). This is
the device by which [Hin26d] proves the uniform boundedness in parameterised settings
((S7), with [Hin26d, footnote 13]). The seminorms of A_(P′) ((S5)) are suprema over h ∈ P′ of seminorms of the A_h; so
they are bounded independently of P′, for otherwise the union of countably many P′ on which some seminorm exceeds 1, 2,
3, … would be a countable set on which it is infinite. We write whΨ^m_(3b,ħ) := {hA : A ∈ wΨ^m_(3b,ħ)} and
wh^∞Ψ^(−∞)_(3b,ħ) := ⋂_N wh^NΨ^(−N)_(3b,ħ); a family of symbols a = (a_h) lies in wS^m if its restriction to every
N_(P′) lies in wS^m(^𝒱T*N_(P′)); and Op(a) := (Op_(𝒱_h)(a_h))_h. The principal symbol of A is the class of the symbols
of the A_(P′), an element of wS^m/whS^(m−1). The classes wΨ^m_3b of the 3b-structure, and wΨ^m_(eb,ħ), wΨ^m_eb on M°,
are defined in the same way (for the structures with scalings 1, P′ is a single point and h is absent).

The Sobolev spaces are wH^s_(3b,h) := w⟨x⟩^(−5/2)H^s_(𝒱_h)(M₀°; ℂ⁵), normed by
‖u‖_(wH^s_(3b,h)) := h^(5/2)‖⟨x⟩^(5/2)u‖_(wH^s_(𝒱_h)) ((S3)); wH^s_3b is the case h = 1; wH^s_(eb,h) and wH^s_eb are
defined with r for ⟨x⟩. For w = ρ_sf^(β_sf)ρ_K^(β_K) these are the spaces H^(s,(β_sf,β_K))_(3b,h) of [[def:iv5-0-1]].

**Lemma {#lem:iv5-calc-structure}** (The structures.)

(a) ℬ and ℬ_eb are bounded geometry structures, and (ℬ^×_h)_h and the semiclassical eb-structure are parameterised
scaled bounded geometry structures ((S1), (S7)). The coefficient Lie algebra 𝒲 of ℬ consists of the vector fields
Σ_μ f^μ⟨x⟩∂_(z^μ) with f^μ ∈ C^∞_(uni,ℬ)(M₀°), and 𝒱_h = h𝒲; the same holds for ℬ_eb with r∂_(z^μ). Restriction to M₀°
maps C^∞(M₀) into C^∞_(uni,ℬ)(M₀°), and restriction to M° maps C^∞(M) into C^∞_(uni,ℬ_eb)(M°).

(b) ⟨x⟩ is a weight for ℬ, and so is every product of real powers of boundary defining functions of M₀ and of a positive
element of C^∞(M₀); in particular ρ_sf^(β_sf)ρ_K^(β_K), with ρ_sf and ρ_K defining functions of 𝗌𝖿 and K⁺ in M₀ ((S2)).
Being independent of h, these are weights for (ℬ^×_h)_h ((S7)). The same holds for ℬ_eb, with r and the boundary
defining functions of M.

(c) There is C, independent of h, with C⁻¹‖u‖_(L²(M₀°, |dt dx|; B)) ≤ ‖u‖_(H⁰_(3b,h)) ≤ C‖u‖_(L²(M₀°, |dt dx|; B)), and
likewise for the eb-spaces on M°.

(d) Identify ³ᵇT*M₀ with M₀ × ℝ⁵ through ζ ↦ Σ_μ ζ_μ dz^μ/⟨x⟩, let ³ᵇT̄*M₀ be its fibrewise radial compactification,
𝒫 := [0, 1]_h × ³ᵇT̄*M₀ and 𝒫° := (0, 1] × ³ᵇT*M₀, and identify (h, z, ζ) ∈ 𝒫° with the covector
h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ ∈ ^(𝒱_h)T*_zM₀° = T*_zM₀°. Put ρ_∞ := ⟨ζ⟩⁻¹, |ζ| being the Euclidean norm of (ζ_μ). Then for
a ∈ C^∞(𝒫; End ℂ⁵), m ∈ ℝ and a weight w as in (b), the family (wρ_∞^(−m)a(h, ·))_h lies in wS^m. The same holds for
𝒫_eb := [0, 1] × ^(eb)T̄*M, with ^(eb)T*M ≅ M × ℝ⁵ through ζ ↦ Σ_μ ζ_μ dz^μ/r.

*Proof.* (a) *Cover and multiplicity.* A point with max_q |x^q| < 1 lies in φ⁻¹((−1, 1)⁵) for the chart U_((1),j) with
j an integer nearest to t. Otherwise let |x^i| = max_q |x^q| ≥ 1, and take the sign of x^i, the integer k ≥ 0 nearest
to log₂|x^i|, the integer j nearest to 2^(−k)t and m_a ∈ {−1, 0, 1} nearest to x^a/x^i ∈ [−1, 1]; then every
coordinate of φ has absolute value at most ½. A point lies in at most four charts U_((1),j), and, for each i and sign,
in charts U_((2)) for at most four values of k, then of j, and of each m_a. So ℬ has finite multiplicity.

*Transitions.* On U_((2),i,±,j,k,m) write (T, X, Ω) for the coordinates and Ω̃_a := Ω_a + m_a = x^a/x^i, Ω̃_i := 1. Then
t = 2^k(T + j), x^i = ±2^(k+X) and x^a = x^iΩ̃_a, and |x^i| ≤ |x| < 7|x^i| as |Ω̃_a| < 4. If this chart meets
U_((2),i′,±′,j′,k′,m′), then 2^(k′−2) < |x^(i′)| < 7·2^(k+2) and symmetrically, so |k − k′| ≤ 7, and the second chart
has the coordinates

    T′ = 2^(k−k′)T + (2^(k−k′)j − j′),     X′ = X + k − k′ + log₂|Ω̃_(i′)|,     Ω̃′_b = Ω̃_b/Ω̃_(i′),

with |Ω̃_(i′)| = |x^(i′)|/|x^i| ≥ 2^(k′−k−4) on the closure of the overlap. As |T|, |T′| < 2 there, the number
2^(k−k′)j − j′ ∈ 2^(−7)ℤ is bounded, so it takes finitely many values. Hence these transition maps are restrictions of
finitely many smooth maps, each defined near the closure of the corresponding overlap. A chart U_((1),j) meets charts
U_((2)) only with k ≤ 2, and two charts U_((1)) differ by an integer translation in t of length at most 3. So all
transition maps are uniformly bounded in C^∞, and ℬ is a bounded geometry structure ((S1)). With constant scalings h,
condition [Hin26d, (1.6)] is the uniform C^∞ bound of the transition maps, uniformly in h; so (ℬ^×_h)_h is the
semiclassical case of [Hin26d, Definition 1.9] ((S7)).

*Lie algebras.* On the charts U_((2)),

    ∂_T = 2^(−X)|x^i|∂_t,     ∂_X = (ln 2)(x^i∂_(x^i) + Σ_(a≠i) x^a∂_(x^a)),     ∂_(Ω_a) = x^i∂_(x^a),

and conversely |x^i|∂_t = 2^X∂_T, |x^i|∂_(x^a) = ±∂_(Ω_a) and |x^i|∂_(x^i) = ±((ln 2)⁻¹∂_X − Σ_(a≠i) Ω̃_a∂_(Ω_a)).
Moreover ⟨x⟩/|x^i| = (2^(−2(k+X)) + 1 + Σ_(a≠i) Ω̃_a²)^(1/2) lies in [1, 11] and has bounded derivatives of all orders,
as 2^(k+X) > ¼. On the charts U_((1)) the coordinate fields are ∂_t, ∂_x, and 1 ≤ ⟨x⟩ ≤ √17. So in every chart the
coordinate vector fields and the fields ⟨x⟩∂_(z^μ) are combinations of each other with coefficients bounded with all
derivatives, uniformly in the chart. This is the description of 𝒲, and 𝒱_h = h𝒲 because all scalings equal h ((S1)).

*Smooth functions.* The fields ⟨x⟩∂_(z^μ) extend to smooth vector fields on M₀ tangent to its boundary hypersurfaces.
Near 𝗌𝖿 away from K^±, in the coordinates 1/r, t/r and x/r, one has r∂_t = ∂_(t/r) and r∂_r = −(1/r)∂_(1/r) −
(t/r)∂_(t/r), the angle being fixed. Near the interior of K⁺, in the coordinates s := 1/t and x, ⟨x⟩∂_t = −⟨x⟩s·s∂_s,
and the ⟨x⟩∂_(x^q) are tangent to K⁺. Near K⁺ ∩ 𝗌𝖿, in (ρ_K, ρ_sf) := (r/t, 1/r) and the angle, r∂_t = −ρ_K·ρ_K∂_(ρ_K)
and r∂_r = ρ_K∂_(ρ_K) − ρ_sf∂_(ρ_sf). In all cases r∂_(x^q) = (x^q/r)r∂_r plus vector fields tangent to the spheres
with coefficients smooth in the angle, and ⟨x⟩/r is smooth near r = ∞; K⁻ is the same with −t for t. So every iterated
derivative of f ∈ C^∞(M₀) along the ⟨x⟩∂_(z^μ) is bounded, and by the previous paragraph f is bounded with all
derivatives in the charts, uniformly.

*The eb-structure.* On U_(j,k,β), with coordinates (T, X, θ), r∂_t = 2^X∂_T, r∂_r = (ln 2)⁻¹∂_X, and the r∂_(x^q) are
(x^q/r)r∂_r plus combinations of the ∂_θ with coefficients bounded with all derivatives (finitely many charts of 𝕊³).
Cover, multiplicity and transitions are checked as above, with T′ = 2^(j−j′)T + (2^(j−j′)k − k′), X′ = X + j − j′ and
the transition maps of the charts of 𝕊³. The fields r∂_(z^μ) are smooth on M and tangent to its boundary: near 𝖼𝖿
they are r∂_t, r∂_r and fields tangent to the spheres; near 𝗌𝖿 they are as above; and near 𝖼𝖿 ∩ 𝗌𝖿, in
(ρ_sf, ρ_cf) := (1/t, r/t) for t > 0 and the angle, r∂_t = −ρ_cf(ρ_sf∂_(ρ_sf) + ρ_cf∂_(ρ_cf)) and r∂_r = ρ_cf∂_(ρ_cf).

(b) By (S2), w > 0 is a weight if Ww/w is bounded with all derivatives in the charts for W ∈ 𝒲. Now
⟨x⟩∂_(x^q)⟨x⟩/⟨x⟩ = x^q/⟨x⟩ and ∂_t⟨x⟩ = 0. If ρ_H defines a boundary hypersurface of M₀ and V is a smooth vector field
on M₀ tangent to the boundary, then Vρ_H/ρ_H ∈ C^∞(M₀); with (a) this gives the claim for the products. As the weights
and the charts do not depend on h, the ratios of the weight across overlapping charts of the parameterised structure are
those for ℬ, which are bounded ((S7), the sufficient condition after [Hin26d, Definition 3.58]).

(c) On U_((2),i,±,j,k,m), dt = 2^k dT, dx^i = (ln 2)x^i dX and dx^a = Ω̃_a dx^i + x^i dΩ_a, so the density |dt dx|
equals (ln 2)2^k|x^i|⁴|dT dX dΩ|; as 2^k/|x^i| ∈ (¼, 4) and ⟨x⟩/|x^i| ∈ [1, 11], ⟨x⟩^(−5)|dt dx| is the Lebesgue
measure of the chart times a function lying between two positive constants. On U_((1)) this is clear. By
[Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) at s = 0, where S_α is the dilation by h⁻¹, ‖v‖²_(H⁰_(𝒱_h)) = Σ_α
‖(S_α)_*(φ_α)_*(χ_αv)‖²_(L²) = h^(−5) Σ_α ∫ |(φ_α)_*(χ_αv)|² dx. As Σ_α χ_α² lies between two positive constants
(finite multiplicity, and χ_α = 1 on the sets φ_α⁻¹([−1, 1]⁵), which cover), this is uniformly equivalent to
h^(−5)‖v‖²_(L²(⟨x⟩^(−5)|dt dx|)). Put v := ⟨x⟩^(5/2)u; the factor h^(5/2) in the norm gives the claim for the Euclidean
inner product of ℂ⁵, and B is uniformly equivalent to it. On U_(j,k,β), |dt dx| = r³|dt dr dω|, and dt = 2^j dT,
dr = (ln 2)r dX, so r⁻⁵|dt dx| is the Lebesgue measure of the chart times a function between two positive constants.

(d) In a chart U_α of ℬ, with coordinates y and the fibre coordinates ξ of (S4), the covector Σ_i ξ_i dy^i/h equals
h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ exactly when ξ = C_α(y)ζ, where C_α(y)_(iμ) := ⟨x⟩⁻¹∂z^μ/∂y^i are the coefficients of ∂_(y^i) in
terms of the ⟨x⟩∂_(z^μ). By (a), C_α and C_α⁻¹ are bounded with all derivatives, uniformly in α, and they do not
depend on h; so ⟨ξ⟩/⟨ζ⟩ lies between two positive constants. A smooth function on ³ᵇT̄*M₀ has bounded derivatives of
all orders along the fields ⟨x⟩∂_(z^μ), acting at fixed ζ (smooth vector fields on ³ᵇT̄*M₀ by (a)), and its
ζ-derivatives of order γ are bounded by C⟨ζ⟩^(−|γ|), by the radial compactification. By the chain rule through ζ =
C_α(y)⁻¹ξ, the function (y, ξ) ↦ a(h, y, C_α(y)⁻¹ξ) satisfies |∂_y^β∂_ξ^γ ·| ≤ C_(βγ)⟨ξ⟩^(−|γ|), uniformly in α and h:
a y-derivative at fixed ξ adds a ζ-derivative times (∂_yC_α⁻¹)ξ, and |ξ| ≤ C⟨ζ⟩. The function ρ_∞⟨ξ⟩ and its inverse
satisfy the same estimates, so ρ_∞^(−m) ∈ S^m with uniform bounds; this gives the claim, w being a weight. The eb-case
is the same. ∎

**Definition {#def:iv5-calc-micro}** (Microsupport and elliptic set.) Let ∂_ħ := ({0} × ³ᵇT̄*M₀) ∪ ([0, 1] × ³ᵇS*M₀)
⊂ 𝒫, where ³ᵇS*M₀ is fibre infinity. In statements about WF′ and Ell, a subset S of ³ᵇT̄*M₀, such as the zero section o
or the set ∂Σ of the notation above, or a set described by a condition |ζ| < 1, stands for
({0} × S) ∪ ([0, 1] × (S ∩ ³ᵇS*M₀)) ⊂ ∂_ħ. A family of symbols a is *supported in* a closed set K ⊂ 𝒫 if a vanishes on
𝒫° ∖ K. An operator B ∈ wΨ^m_(3b,ħ) is *microsupported in* a closed set K ⊂ 𝒫 if Op(1 − y)B and BOp(1 − y) lie in
wh^∞Ψ^(−∞)_(3b,ħ) for every real y ∈ C^∞(𝒫) equal to 1 on a neighbourhood of K; here Op(1 − y) ∈ Ψ⁰_(3b,ħ) by
[[lem:iv5-calc-structure]] (d). For A ∈ wΨ^m_(3b,ħ) with principal symbol represented by a, the *elliptic set*
Ell(A) = Ell_(3b,ħ)(A) is the set of p ∈ ∂_ħ having a neighbourhood 𝒰 in 𝒫 such that a is invertible on 𝒰 ∩ 𝒫°,
with |a⁻¹| ≤ Cw⁻¹ρ_∞^m there for some C, |·| being the operator norm for B. It is open in ∂_ħ, and it does not depend on
the representative: a changes by whρ_∞^(1−m)e with e bounded, and hρ_∞ is continuous on 𝒫 and vanishes on ∂_ħ. For
S ⊂ ∂_ħ, *WF′(B) ⊂ S* (WF′ = WF′_(3b,ħ)) means that B is microsupported in a closed set K with K ∩ ∂_ħ ⊂ S, and
*WF′(B) ∩ S = ∅* means that B is microsupported in a closed set K with K ∩ S = ∅. B has *compact operator wave front set*
if it is microsupported in a closed set disjoint from [0, 1] × ³ᵇS*M₀. The same definitions are made with 𝒫_eb for the
eb-calculus.

**Lemma {#lem:iv5-calc-disjoint}** (Disjoint supports.) Let c_1 ∈ w_1S^(m_1) and c_2 ∈ w_2S^(m_2) be supported in closed
sets K_1, K_2 ⊂ 𝒫 with K_1 ∩ K_2 = ∅, and let T ∈ w_3Ψ^(m_3)_(3b,ħ). Then Op(c_1)TOp(c_2) ∈ w_1w_2w_3h^∞Ψ^(−∞)_(3b,ħ).
Consequently:

(a) if c ∈ wS^m is supported in K and R ∈ wh^∞Ψ^(−∞)_(3b,ħ), then Op(c) + R is microsupported in K;

(b) if B is microsupported in K, then so is T_1BT_2 for all T_1, T_2 in the calculus;

(c) if B is microsupported in K_1 and in K_2, then it is microsupported in every closed neighbourhood of K_1 ∩ K_2; and
if K_1 ∩ K_2 = ∅, then B ∈ h^∞Ψ^(−∞)_(3b,ħ);

(d) a symbol c ∈ wS^m supported in a closed set disjoint from ∂_ħ lies in ⋂_N wh^NS^(−N), and Op(c) ∈ wh^∞Ψ^(−∞)_(3b,ħ).

The same holds for the eb-calculus.

*Proof.* Fix a countable P′ ⊂ (0, 1], write N := N_(P′), and denote restrictions to P′ by the same letters; the scaling
weight of N is ρ̄ = h ≤ 1. By (S14) the entries of Op(c_1)TOp(c_2) are sums of operators of the same form with scalar
symbols supported in K_1 and K_2 and scalar T, so we may assume c_1, c_2 and T scalar. Choose a real y ∈ C^∞(𝒫) with
y = 1 near K_1 and y = 0 near K_2. By [[lem:iv5-calc-structure]] (d), y lies in S⁰(^𝒱T*N) = C^∞_(uni,ℬ*)(^𝒱T*N)
([Hin26d, Lemma 3.24 (1)], (S16)), so its continuous extension j(y) to the uniform compactification of ^𝒱T*N is defined
([Hin26d, Definition 3.25], (S16)); as ^𝒱T*N is dense there, j is linear and j(1) = 1. Let ϖ be a point of the
microlocalisation locus of N. If j(y)(ϖ) ≠ 1, then χ := 1 − y has j(χ)(ϖ) ≠ 0 and χc_1 = 0, so ϖ is not in the essential
support of c_1. If j(y)(ϖ) = 1, then χ := y has j(χ)(ϖ) ≠ 0 and χc_2 = 0, so ϖ is not in the essential support of c_2.
Hence the essential supports E_1 of c_1 and E_2 of c_2 are disjoint; they are the operator wave front sets of Op(c_1)
and Op(c_2) ([Hin26d, Definition 3.43], (S16)).

Put w := w_1w_2w_3, m := m_1 + m_2 + m_3 and X := Op(c_1)TOp(c_2). Then X ∈ wΨ^m_𝒱(N) ([Hin26d, Theorem 3.51], (S5)),
and X maps C_c^∞(N) to itself, as quantisations and residual operators do ([Hin26d, p. 44 and Definition 3.34], (S16)).
Let w′ be a weight on N, L ≥ |m| and u ∈ w′ρ̄^(−L)H^(−L)_𝒱(N). For all σ, l ∈ ℝ, the microlocality of
[Hin26d, Proposition 3.55 (2)] ((S16)), applied to Op(c_2), to T and to Op(c_1) in turn, gives
WF^(σ−m_2,w_2w′,l)_𝒱(Op(c_2)u) ⊂ E_2, then WF^(σ−m_2−m_3,w_3w_2w′,l)_𝒱(TOp(c_2)u) ⊂ E_2, and
WF^(σ−m,ww′,l)_𝒱(Xu) ⊂ E_2 ∩ E_1 = ∅; so Xu ∈ ww′ρ̄^lH^(σ−m)_𝒱(N) by [Hin26d, Proposition 3.55 (1)]. Thus X maps
w′ρ̄^(−L)H^(−L)_𝒱(N) into Y := ww′ρ̄^LH^L_𝒱(N). As a map into Z := ww′ρ̄^(−L)H^(−L−m)_𝒱(N) it is bounded
([Hin26d, Theorem 3.44], (S5)), and Y ⊂ Z with a continuous inclusion, by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) and
ρ̄ ≤ 1; so X, as a map into Y, has closed graph and is bounded. Next let w″ be a weight on N, put w′ := (ww″)⁻¹, and let
X* ∈ wΨ^m_𝒱(N) be the formal adjoint of X for a uniformly positive 𝒱-density ([Hin26d, Theorem 3.51]). For u,
v ∈ C_c^∞(N), ⟨X*v, u⟩ = ⟨v, Xu⟩ and |⟨v, Xu⟩| ≤ C‖v‖_(w″ρ̄^(−L)H^(−L))‖Xu‖_(ww′ρ̄^LH^L), as w″ = (ww′)⁻¹. The duality
of [Hin26d, Proposition 3.22] ((S16)) identifies ww″ρ̄^LH^L_𝒱(N) = w′⁻¹ρ̄^LH^L_𝒱(N) with the dual of
w′ρ̄^(−L)H^(−L)_𝒱(N), with equivalent norms by the open mapping theorem; with the density of C_c^∞(N)
([Hin26d, Lemma 3.20], (S16)) and the bound for X, this gives ‖X*v‖_(ww″ρ̄^LH^L) ≤ C‖v‖_(w″ρ̄^(−L)H^(−L)) for
v ∈ C_c^∞(N), and so for all v ∈ w″ρ̄^(−L)H^(−L)_𝒱(N), by density and the continuity of X* into the larger space
ww″ρ̄^(−L)H^(−L−m)_𝒱(N) ([Hin26d, Theorem 3.44]). The spaces decrease as L grows ([Hin26d, (3.14)], ρ̄ ≤ 1), so these
bounds for L ≥ |m| give them for every L ∈ ℝ.

Finally, every chart of N in {h} × M₀° has all scalings equal to h = ρ̄, so ρ̄W ∈ 𝒱 for W ∈ 𝒲 ((S1)), and ρ̄ is constant
on each {h} × M₀°. With the norm of wH^(s;k)_(𝒱;𝒲)(N) of [Hin26d, p. 37] ((S16)), [Hin26d, Proposition 3.19] ((S3)),
applied to the operators (ρ̄W_1)⋯(ρ̄W_j) ∈ Diff^j_𝒱 for j ≤ k, and [Hin26d, (3.14)] give
‖f‖_(w′H^s) ≤ ‖f‖_(w′H^(s;k)) ≤ C‖f‖_(w′ρ̄^kH^(s+k)) for every weight w′. So the bounds above, with N + k for L, give
those of [Hin26d, Definition 3.34] ((S16)) for all N and k, and X ∈ wρ̄^∞Ψ^(−∞)_𝒱(N). For the weight wρ̄^L the
conditions of that definition are those for w, N ranging over ℝ; so X = Op_𝒱(0) + X lies in wρ̄^LΨ^(−L)_𝒱(N) for every L
([Hin26d, Definition 3.43], (S16)), that is, h^(−L)Op(c_1)TOp(c_2) restricted to P′ lies in wΨ^(−L)_𝒱(N). As P′ is
arbitrary, Op(c_1)TOp(c_2) ∈ wh^LΨ^(−L)_(3b,ħ) for every L.

(a) If y = 1 on a neighbourhood V of K, then 1 − y is supported in 𝒫 ∖ V, which is closed and disjoint from K; so
Op(1 − y)Op(c) and Op(c)Op(1 − y) lie in h^∞Ψ^(−∞) (T = I). Products of R with elements of the calculus stay in
wh^∞Ψ^(−∞), by [Hin26d, Theorem 3.51] on each N_(P′).

(b) Let y = 1 near K, and choose a real y′ ∈ C^∞(𝒫) with y′ = 1 near K and y = 1 near supp y′. Then
B = Op(y′)B + Op(1 − y′)B, the second term lying in h^∞Ψ^(−∞), and Op(1 − y)T_1Op(y′) ∈ h^∞Ψ^(−∞) by the first part;
so Op(1 − y)T_1BT_2 ∈ h^∞Ψ^(−∞). On the right, write B = BOp(y′) + BOp(1 − y′) and use Op(y′)T_2Op(1 − y).

(c) Let K be a closed neighbourhood of K_1 ∩ K_2 and y = 1 near K. By compactness there are real y_1, y_2 ∈ C^∞(𝒫) with
y_i = 1 near K_i and supp y_1 ∩ supp y_2 contained in the interior of {y = 1}. Then
1 − y = (1 − y)(1 − y_1) + (1 − y)y_1(1 − y_2), the remaining term (1 − y)y_1y_2 being 0. Choose a real y′_1 equal to 1
near K_1 with supp y′_1 inside the interior of {y_1 = 1}; then B = Op(y′_1)B + Op(1 − y′_1)B, and
Op((1 − y)(1 − y_1))Op(y′_1) ∈ h^∞Ψ^(−∞) by the first part, so Op((1 − y)(1 − y_1))B ∈ h^∞Ψ^(−∞). In the same way
Op((1 − y)y_1(1 − y_2))B ∈ h^∞Ψ^(−∞), using K_2. On the right the argument is the same. If K_1 ∩ K_2 = ∅, the same
argument with y := 0 and supp y_1 ∩ supp y_2 = ∅ gives B = Op(1)B ∈ h^∞Ψ^(−∞).

(d) The function hρ_∞ is continuous on 𝒫 and vanishes exactly on ∂_ħ, so it is at least some δ > 0 on a closed set
disjoint from ∂_ħ; there h ≥ δ and ⟨ζ⟩ ≤ δ⁻¹. Hence c satisfies the estimates of wh^LS^(−L) for every L, as h^(−L)⟨ξ⟩^L
is bounded on its support ([[lem:iv5-calc-structure]] (d)), and Op(c) ∈ wh^LΨ^(−L) for every L.

The eb-case is the same. ∎

**Lemma {#lem:iv5-calc-d}** (Property (D) at X_0 and at Σ^♯.) Each of the open sets Ω₁ := {t > 0} and
Ω₃ := {t > 0, r < r_♯} of M₀°, and {t > 0} ⊂ M°, has property (D) of [[sec:ii-a-7]] for every s ∈ ℝ and every
h ∈ (0, 1]: C_c^∞ of the set is dense in the subspace of H^s_(𝒱_h) of the elements supported in its closure.

*Proof.* Fix h; the property is qualitative. For fixed h, H^s_(𝒱_h) is the space H^s of ℬ with scalings 1, with an
equivalent norm, by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]): the maps S_α are dilations by h⁻¹, which are
isomorphisms of H^s(ℝ⁵). By (S12) we may also replace ℬ by a compatible bounded geometry structure. For Ω₁ we keep ℬ.
For Ω₃, let R₀ := r_♯ + 1 and R₁ := 200R₀, take finitely many charts κ_ℓ : V_ℓ → (−2, 2)⁴ of ℝ⁴ such that the sets
κ_ℓ⁻¹((−1, 1)⁴) cover {|x| ≤ R₁}, each V_ℓ either disjoint from {|x| = r_♯} or such that
κ_ℓ(V_ℓ ∩ {|x| < r_♯}) = {y_1 < 0}, and replace the charts of ℬ that meet {|x| ≤ R₀} by the charts
(j − 2, j + 2)_t × V_ℓ, (t − j, κ_ℓ(x)), j ∈ ℤ. The charts of ℬ that are kept still cover {|x| > R₁}: a chart U_((2))
whose set φ⁻¹((−1, 1)⁵) contains a point with |x| > R₁ has 2^(k−2) > R₁/56 > R₀. The charts of ℬ that meet {|x| ≤ R₁}
have k ≤ log₂R₁ + 2, so all transition maps between the two families are translates in t of finitely many smooth maps;
the result is a bounded geometry structure compatible with ℬ. In each chart of the structure so obtained that meets ∂Ω
(Ω = Ω₁ or Ω₃), with coordinates (T, y), the set Ω is {T > a} or {T > a, y_1 < 0} for some a ∈ ℝ, because the charts are
products in t with T an affine function of t with positive slope; a chart not meeting ∂Ω lies in Ω or in its complement,
being connected.

Let e := (1, −1, 0, 0, 0)/√2 in the coordinates (T, y_1, …), and Γ := {Y ∈ ℝ⁵ : Y·e ≥ ¾|Y|}; every Y ∈ Γ ∖ 0 has
positive T-component and negative y_1-component. Fix ϱ ∈ C_c^∞(ℝ⁵) with ∫ϱ = 1 and supp ϱ ⊂ Γ ∩ {½ ≤ |Y| ≤ 1}, and put
ϱ_ε(Y) := ε^(−5)ϱ(Y/ε), ε ∈ (0, ¼]. If a distribution f on ℝ⁵ is supported in the closure of {T > a} or of
{T > a, y_1 < 0}, then ϱ_ε ∗ f is smooth and supported in {T ≥ a + cε} or in {T ≥ a + cε, y_1 ≤ −cε}, c > 0 depending
only on ϱ.

Let χ ∈ C_c^∞((−5/4, 5/4)⁵) be nonnegative and equal to 1 on [−1, 1]⁵, and χ_α := φ_α^*χ/Σ_β φ_β^*χ. For v in H^s
supported in Ω̄ put w_α := (φ_α)_*(χ_αv) and v_ε := Σ_α φ_α^*(ϱ_ε ∗ w_α); ϱ_ε ∗ w_α is supported in (−3/2, 3/2)⁵. Then
v_ε is smooth and supported in Ω, at distance at least cε from ∂Ω in every chart. By [Hin26d, (3.14)], the norm of an
element of H^s is the square root of Σ_β ‖(φ_β)_*(φ_β^*χ ·)‖²_(H^s(ℝ⁵)); hence ‖Σ_α g_α‖² ≤ L Σ_α ‖g_α‖² for any g_α
supported in U_α, L being a bound for the number of charts that meet a given chart (finite by the description of the
transitions), since each term (φ_β)_*(φ_β^*χ Σ_α g_α) involves at most L of the g_α, and since Σ_β
‖(φ_β)_*(φ_β^*χ g_α)‖² is ‖g_α‖². Moreover, for f ∈ H^s(ℝ⁵) supported in (−3/2, 3/2)⁵, ‖φ_α^*f‖_(H^s) ≤ C‖f‖_(H^s(ℝ⁵)),
and Σ_α ‖w_α‖²_(H^s(ℝ⁵)) ≤ C‖v‖²_(H^s), with C independent of α: H^s(ℝ⁵), for distributions supported in a fixed compact
set, is invariant under multiplication by functions bounded in C^∞ and under diffeomorphisms bounded in C^∞ together
with their inverses, and the transition maps and the functions Σ_β φ_β^*χ are so bounded ((S1)). Convolution with
ϱ_ε − δ_0 is the Fourier multiplier ϱ̂(εξ) − 1, bounded by C uniformly in ε and tending to 0 pointwise; so ‖(ϱ_ε − δ_0)
∗ w_α‖_(H^s(ℝ⁵)) ≤ C‖w_α‖_(H^s(ℝ⁵)), and it tends to 0 for each α. As Σ_α χ_α = 1, ‖v_ε − v‖²_(H^s) ≤ LC Σ_α
‖(ϱ_ε − δ_0) ∗ w_α‖²_(H^s(ℝ⁵)), which tends to 0 by dominated convergence for the series.

Finally let ψ ∈ C_c^∞(ℝ) equal 1 near 0 and ψ_R(t, x) := ψ(t/R)ψ(|x|/R), R ≥ 1. The ψ_R are bounded in C^∞_(uni,ℬ)
uniformly in R, since ⟨x⟩ ≤ CR on supp ψ(|x|/R); so multiplication by ψ_R is bounded on H^s uniformly in R ((S3), (S7)
with parameter R), and ψ_Rf → f in H^s for f ∈ C_c^∞, hence for every f ∈ H^s, C_c^∞ being dense ([Hin26d, Lemma
3.20], (S16)). Now ψ_Rv_ε ∈ C_c^∞(Ω), and it tends to v as R → ∞ and then ε → 0. The case of M° is the same, with the
charts of ℬ_eb, in which {t > 0} is {T > −k}, and with ψ_R(t, x) := ψ(t/R)ψ(|x|/R)(1 − ψ(R|x|)), which has compact
support in M° and is bounded in C^∞_(uni,ℬ_eb) uniformly in R, as |x| ≤ CR on supp ψ(|x|/R) and R|x| ≤ C on
supp ψ′(R|x|). ∎

**Lemma {#lem:iv5-calc-dual}** (Supported and extendible spaces.) Let w be a weight as in [[lem:iv5-calc-structure]] (b),
s ∈ ℝ, Ω₁ := {t > 0} and Ω₂ := {r > r_♯} in M₀°, so that Ω° = Ω₁ ∩ Ω₂. Define:

- wH^s_(3b,h)(Ω)^(•,−) := {ũ|_(Ω₂) : ũ ∈ wH^s_(3b,h), supp ũ ⊂ cl Ω₁}, normed by the infimum of ‖ũ‖_(wH^s_(3b,h)) over
such ũ (supported at X_0, extendible at Σ^♯);

- wH^s_(3b,h)(Ω)^(−,•) := {v ∈ wH̄^s_(3b,h)(Ω₁) : supp v ⊂ {r ≥ r_♯}}, with the norm of wH̄^s_(3b,h)(Ω₁), the infimum of
the norms of the extensions of v to M₀° (extendible at X_0, supported at Σ^♯);

- wH̄^s_(3b,h)(Ω) := {ũ|_(Ω°) : ũ ∈ wH^s_(3b,h)}, with the infimum norm (extendible at both).

Then, with constants independent of h:

(a) for u ∈ wH^s(Ω)^(•,−) and v ∈ w⁻¹H^(−s)(Ω)^(−,•) the number ⟨u, v⟩ := ⟨ũ, ṽ⟩ does not depend on the choice of ũ as
above and of ṽ ∈ w⁻¹H^(−s)_(3b,h) with ṽ|_(Ω₁) = v; |⟨u, v⟩| ≤ C‖u‖‖v‖; and ⟨u, v⟩ is the pairing of distributions
when u or v lies in C_c^∞(Ω°);

(b) every bounded linear functional λ on w⁻¹H^(−s)(Ω)^(−,•) is λ(v) = ⟨v, u⟩ := ⟨ṽ, ũ⟩ for some u ∈ wH^s(Ω)^(•,−) with
‖u‖ ≤ C‖λ‖, and every bounded linear functional λ on wH^s(Ω)^(•,−) is λ(u) = ⟨u, v⟩ for some
v ∈ w⁻¹H^(−s)(Ω)^(−,•) with ‖v‖ ≤ C‖λ‖; conjugate-linear functionals are treated by taking complex conjugates.

For the eb-spaces on M° and Ω = {t ≥ 0}, the same holds with Ω₂ := M°: the supported space wḢ^s_(eb,h)(Ω) and the
extendible space w⁻¹H̄^(−s)_(eb,h)(Ω°) are dual in the same sense.

*Proof.* Let Iu := h^(5/2)⟨x⟩^(5/2)u. By definition I is an isometry of wH^s_(3b,h) onto wH^s_(𝒱_h), and it preserves
supports. With μ_h := h^(−5)⟨x⟩^(−5)|dt dx|, a uniformly positive 𝒱_h-density by the proof of
[[lem:iv5-calc-structure]] (c), one has ⟨u, v⟩ = ∫ (B̂Iu)·(Iv)‾ μ_h, B̂ being the matrix of B in the frame.
Multiplication by B̂ and by B̂⁻¹ is bounded on every wH^s_(𝒱_h), uniformly in h (differential operators of order 0 with
coefficients independent of h, (S3), (S7)), and multiplication by w is an isomorphism of H^s_(𝒱_h) onto wH^s_(𝒱_h), with
bounds independent of h ((S3), (S7)), that preserves supports. So [[lem:ii-a-7-1]] and [[lem:ii-a-7-3]], which are
stated for parameterised scaled bounded geometry structures with a uniformly positive density ([[sec:ii-a-7]]), hold for
the pairing ⟨·, ·⟩ and the spaces wH^s_(3b,h), w⁻¹H^(−s)_(3b,h), with constants independent of h. The open sets Ω₁ and
Ω₃ := {t > 0, r < r_♯} have property (D) for every order ([[lem:iv5-calc-d]]).

(a) Let ũ, ũ′ be two choices for u, and ṽ, ṽ′ two for v. Then ũ − ũ′ is supported in cl Ω₁ ∖ Ω₂ = cl Ω₃, so it is the
limit in wH^s_(3b,h) of elements of C_c^∞(Ω₃), by property (D) of Ω₃; these pair to 0 with ṽ, since ṽ = v vanishes on
Ω₃ ⊂ Ω₁ ∩ {r < r_♯}. So ⟨ũ − ũ′, ṽ⟩ = 0, by the bound of [[lem:ii-a-7-1]] (1). Next, ṽ − ṽ′ vanishes on Ω₁, and ũ′ is the
limit of elements of C_c^∞(Ω₁), by property (D) of Ω₁, which pair to 0 with ṽ − ṽ′; so ⟨ũ′, ṽ − ṽ′⟩ = 0. Hence
⟨ũ, ṽ⟩ = ⟨ũ′, ṽ′⟩. The bound follows from [[lem:ii-a-7-1]] (1) by taking infima over ũ and ṽ. If u or v lies in
C_c^∞(Ω°), it is its own choice of ũ or ṽ.

(b) w⁻¹H^(−s)(Ω)^(−,•) is the kernel of the restriction from w⁻¹H̄^(−s)(Ω₁) to Ω₁ ∩ {r < r_♯}, a closed subspace with
the norm of w⁻¹H̄^(−s)(Ω₁). Extend λ to w⁻¹H̄^(−s)(Ω₁) with the same norm (Hahn–Banach). By [[lem:ii-a-7-3]] (3), second
statement, with −s for 𝗌 and Ω₁ for Ω, there is ũ ∈ wH^s_(3b,h) supported in cl Ω₁ with ‖ũ‖ ≤ C‖λ‖ and λ(v) = ⟨ṽ, ũ⟩
for every v and every extension ṽ of v. Then u := ũ|_(Ω₂) lies in wH^s(Ω)^(•,−), with ‖u‖ ≤ ‖ũ‖ ≤ C‖λ‖ and
λ(v) = ⟨v, u⟩. Conversely, let λ be bounded on wH^s(Ω)^(•,−). Then λ̃(ũ) := λ(ũ|_(Ω₂)) is bounded on the space of the
elements of wH^s_(3b,h) supported in cl Ω₁, with norm at most ‖λ‖. By the first statement of [[lem:ii-a-7-3]] (3), with
−s for 𝗌 and Ω₁ for Ω, λ̃(ũ) = ⟨ũ, ṽ⟩ for some ṽ ∈ w⁻¹H^(−s)_(3b,h) with ‖ṽ‖ ≤ C‖λ‖. As λ̃
vanishes on C_c^∞(Ω₃), whose elements restrict to 0 on Ω₂, ṽ vanishes on Ω₃. So v := ṽ|_(Ω₁) is supported in
{r ≥ r_♯}, v ∈ w⁻¹H^(−s)(Ω)^(−,•), ‖v‖ ≤ ‖ṽ‖, and λ(u) = ⟨u, v⟩.

For the eb-spaces, [[lem:ii-a-7-3]] applies directly with Ω := {t > 0} ⊂ M°, which has property (D) by
[[lem:iv5-calc-d]], with the isometry I defined with r for ⟨x⟩. ∎

**Lemma {#lem:iv5-calc-reg}** (A regularising family.) Let K ∈ ℕ, j_ε := ⟨εζ⟩^(−K) for ε ∈ (0, 1], and J_ε := Op(j_ε).

(a) J_ε ∈ Ψ^(−K)_(3b,ħ) for each ε, and the family (J_ε)_(ε) is bounded in Ψ⁰_(3b,ħ): for every countable set P″ of
pairs (ε, h), the family (J_ε)_((ε,h)∈P″) lies in Ψ⁰_𝒱 of P″ × M₀° with the charts of ℬ and scalings h. In particular
J_ε is bounded on every wH^s_(3b,h), uniformly in (ε, h).

(b) For fixed h, J_εu → u in wH^s_(3b,h) as ε → 0, for every u ∈ wH^s_(3b,h).

(c) For p ∈ wS^m, H_pj_ε = ϑ_εj_εe_p, where e_p := −(K/2)⟨ζ⟩^(−2)H_p(|ζ|²) ∈ wS^(m−1) does not depend on ε and
ϑ_ε := ε²⟨ζ⟩²⟨εζ⟩^(−2) takes values in [0, 1] and is bounded in S⁰ uniformly in ε. For P ∈ wΨ^m_(3b,ħ),
h⁻¹i[P, J_ε] is bounded in wΨ^(m−1)_(3b,ħ) uniformly in ε, with principal symbol H_pj_ε, p the principal symbol of P,
computed entrywise. Here H_p is the Hamilton vector field of [[prop:np-10-65-a]] (b).

*Proof.* (a) In a chart, j_ε = f(εC_α(y)⁻¹ξ) with f(η) := ⟨η⟩^(−K) ∈ S⁰(ℝ⁵) ([[lem:iv5-calc-structure]] (d)). A
derivative ∂_y^β∂_ξ^γ of it is a sum of terms (∂^κf)(εC_α⁻¹ξ) times ε^(|κ|) times polynomials in ξ of degree at
most |κ| − |γ| with coefficients bounded uniformly. As |∂^κf(η)| ≤ C⟨η⟩^(−|κ|), and ε⟨ξ⟩ ≤ ⟨εξ⟩ ≤ C⟨εC_α⁻¹ξ⟩ for ε ≤ 1,
each term is at most Cε^(|κ|)⟨ξ⟩^(|κ|−|γ|)⟨εξ⟩^(−|κ|) ≤ C⟨ξ⟩^(−|γ|); so the family is bounded in S⁰, uniformly in (ε,
h). For fixed ε, j_ε ≤ ε^(−K)⟨ζ⟩^(−K), and likewise for the derivatives, so j_ε ∈ S^(−K). The structure with
parameters (ε, h) is parameterised ((S7)), and the boundedness follows from (S5), (S7) as in [[def:iv5-calc-cells]].

(b) For δ ∈ (0, 1], |∂_y^β∂_ξ^γ(j_ε − 1)| ≤ C_δε^δ⟨ξ⟩^(δ−|γ|), since |1 − f(η)| ≤ C min(1, |η|) ≤ C|η|^δ and the terms
of (a) with |κ| ≥ 1 are at most C(ε⟨ξ⟩⟨εξ⟩⁻¹)^(|κ|)⟨ξ⟩^(−|γ|) ≤ C(ε⟨ξ⟩)^δ⟨ξ⟩^(−|γ|). So ε^(−δ)(j_ε − 1) is bounded in
S^δ, and ‖(J_ε − I)u‖_(wH^s_(3b,h)) ≤ Cε^δ‖u‖_(wH^(s+δ)_(3b,h)), by Op(1) = I ([[prop:np-10-65-a]] (a)) and (S5). As
C_c^∞ is dense in wH^s_(3b,h) ([Hin26d, Lemma 3.20], (S16)), so is wH^(s+δ)_(3b,h); with the uniform bound of (a), J_ε
→ I strongly.

(c) By the chain rule, H_pj_ε = −(K/2)(1 + ε²|ζ|²)^(−K/2−1)ε²H_p(|ζ|²) = ϑ_εj_εe_p. The Poisson bracket H_p(|ζ|²) of
p ∈ wS^m and |ζ|² ∈ S² lies in wS^(m+1), by the estimates in the coordinates (y, ξ) of a chart, in which the bracket is
Σ_i (∂_(ξ_i)p ∂_(y^i) − ∂_(y^i)p ∂_(ξ_i)) applied to |ζ|² ([[lem:iv5-calc-structure]] (d)); so e_p ∈ wS^(m−1). Further
ϑ_ε = 1 − (1 − ε²)⟨εζ⟩^(−2), and ⟨εζ⟩^(−2) is bounded in S⁰ uniformly in ε, as in (a). The statement on h⁻¹i[P, J_ε]
is [[prop:np-10-65-a]] (b), applied in the calculus with parameters (ε, h), J_ε being the quantisation of the scalar
symbol j_ε. ∎

**Proposition {#prop:np-10-65-a}** (The calculi.) Let w, w′, w_1, w_2 be weights as in [[lem:iv5-calc-structure]] (b).
All constants below are independent of h ∈ (0, 1].

(a) (*Contents.*) For a ∈ wS^m, Op(a) ∈ wΨ^m_(3b,ħ) has principal symbol a. For a function f on M₀° bounded with all
derivatives in the charts, Op(f) is multiplication by f, Op(1) = I and f·Op(a) = Op(fa). A differential operator
Σ_(|γ|≤k) a_γ(h⟨x⟩∂_z)^γ whose coefficients a_γ, 5 × 5 matrices, are w times elements of C^∞(M₀) lies in wΨ^k_(3b,ħ),
its principal symbol being the class of its semiclassical principal symbol; this applies to h²□_g, L_h, P_h, P_h*, 𝓛_h
and 𝓛_h* (with the weight ρ_sf²), to the products χ_(τ,j)χ_(r,j′) of the cut-offs, to χ_(r,j) and to the weights. For an
h-independent Q ∈ wDiff^k_3b, h^kQ ∈ wΨ^k_(3b,ħ), with principal symbol the principal symbol of Q evaluated at ζ. The
same holds for wΨ_3b, without h.

(b) (*Algebra.*) Let A_i ∈ w_iΨ^(m_i)_(3b,ħ) have principal symbols a_i. Then A_1A_2 ∈ w_1w_2Ψ^(m_1+m_2)_(3b,ħ) with
principal symbol a_1a_2, and A_1* ∈ w_1Ψ^(m_1)_(3b,ħ) with principal symbol a_1^(*_B), the B-adjoint. An element of
wΨ^m_(3b,ħ) with principal symbol 0 lies in whΨ^(m−1)_(3b,ħ). If a_1a_2 = a_2a_1, then h⁻¹i[A_1, A_2] ∈
w_1w_2Ψ^(m_1+m_2−1)_(3b,ħ); if moreover A_1 = Op(a_1) + hE with a_1 scalar and E ∈ w_1Ψ^(m_1−1)_(3b,ħ) of principal
symbol e (every A_1 with scalar principal symbol a_1 has this form), its principal symbol is H_(a_1)a_2 + i[e, a_2],
where H_(a_1)a_2 is computed entrywise and H_(a_1) is the Hamilton vector field of a_1 for the symplectic structure of
T*M₀°, functions on 𝒫° being regarded as functions of the covector Σ_μ ζ_μ dz^μ/⟨x⟩. In particular it is H_(a_1)a_2
when a_2 is scalar.

(c) (*Self-adjoint quantisations.*) Let a ∈ wS^m be real and scalar, or B-self-adjoint, supported in a closed set
K_a ⊂ 𝒫; let K be a closed neighbourhood of K_a, and ψ ∈ C^∞(M₀) real and equal to 1 near the projection of K_a to M₀.
Then there is A = A* ∈ wΨ^m_(3b,ħ) with principal symbol a and A − Op(a) ∈ whΨ^(m−1)_(3b,ħ), microsupported in K, whose
Schwartz kernel is supported in supp ψ × supp ψ. In particular WF′(A) ⊂ K ∩ ∂_ħ.

(d) (*Boundedness.*) A ∈ w_1Ψ^m_(3b,ħ) maps w_2H^s_(3b,h) to w_1w_2H^(s−m)_(3b,h) with norm bounded independently of h.
An element of w_1h^∞Ψ^(−∞)_(3b,ħ) maps w_2H^(−N)_(3b,h) to w_1w_2H^N_(3b,h) with norm O(h^N), for every N.

(e) (*Elliptic estimate.*) Let A ∈ w′Ψ^m_(3b,ħ), G ∈ Ψ⁰_(3b,ħ), and let B ∈ Ψ⁰_(3b,ħ) be microsupported in a closed set
K ⊂ 𝒫 with K ∩ ∂_ħ ⊂ Ell(A) ∩ Ell(G), that is, WF′(B) ⊂ Ell(A) ∩ Ell(G). Then for all s and N there is C such that for
h ∈ (0, 1] and every u ∈ wH^(−N)_(3b,h) with GAu ∈ ww′H^(s−m)_(3b,h), Bu lies in wH^s_(3b,h) and

    ‖Bu‖_(wH^s_(3b,h)) ≤ C(‖GAu‖_(ww′H^(s−m)_(3b,h)) + h^N‖u‖_(wH^(−N)_(3b,h))).                    {#eq:iv5-calc-ell}

(f) (*Square roots.*) Let w be real, q ∈ w²S^(2k) B-self-adjoint, W ⊂ 𝒫 open and c > 0, with
B(qv, v) ≥ cw²ρ_∞^(−2k)B(v, v) on W ∩ 𝒫° for all v. Then the B-self-adjoint square roots q^(±1/2), positive definite,
satisfy on W ∩ 𝒫° the estimates of w^(±1)S^(±k), uniformly. So φq^(±1/2) ∈ w^(±1)S^(±k) for real φ ∈ C^∞(𝒫) supported in
W, and Op(φq^(1/2))*Op(φq^(1/2)) ∈ w²Ψ^(2k)_(3b,ħ) has principal symbol φ²q. If q = fq′, with 0 ≤ f ∈ C^∞(𝒫) scalar,
f^(1/2) ∈ C^∞(𝒫) and q′ as above, then q^(1/2) = f^(1/2)q′^(1/2).

(g) (*Supported and extendible spaces.*) The conclusions of [[lem:iv5-calc-dual]] hold.

(h) (*Regularisation.*) The family of [[lem:iv5-calc-reg]] has the properties stated there.

(i) (*The eb-calculus.*) (a)–(h) hold for wΨ_(eb,ħ) on M°, with r∂_(z^μ) for ⟨x⟩∂_(z^μ), the frame dz^μ/r of
^(eb)T*M, r for ⟨x⟩ and 𝒫_eb for 𝒫; and (a), (b), (d), (f) hold for wΨ_3b and wΨ_eb.

(j) (*Further parameters.*) Let U be a set, and let the operators and symbols above depend on b ∈ U, such that the
families indexed by (b, h) ∈ U × (0, 1] lie in the classes defined as in [[def:iv5-calc-cells]] with the parameter set
U × (0, 1] in place of (0, 1], the charts and scalings not depending on b. If the ellipticity and positivity bounds in
the hypotheses of (e), (f), [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]] hold uniformly in b, then the constants in
their conclusions, and in (d), (g), (h), are uniform in b. The same holds for the calculi with scalings 1 and the
parameter set U.

*Proof.* *Reduction.* A statement about families, restricted to a countable P′ ⊂ (0, 1], is a statement about the
scaled bounded geometry structure N_(P′), to which [Hin26d] applies ((S1)–(S6), (S16)). A membership that holds on every
N_(P′) holds for the family, by [[def:iv5-calc-cells]]. A bound that holds on every N_(P′) holds uniformly in h: if it
failed along a sequence h_ℓ, it would fail on N_(P′) for P′ := {h_ℓ}. This is the argument of [Hin26d, p. 59] ((S7)).

(a) Each chart of N_(P′) lies in one slice {h} × M₀°, so the quantisation of (S4) on N_(P′) is the family of the
quantisations Op_(𝒱_h), and Op(a) restricted to P′ is Op_𝒱(a) ∈ wΨ^m_𝒱(N_(P′)), with principal symbol a
([Hin26d, Definition 3.43], (S16)). In the local quantisation of (S4) the symbol is evaluated at the left variable and
ψ = 1 near 0, and the χ_α of (S4) sum to 1; so for a function f of the base Op_α(χ_αf) has the Schwartz kernel
χ_α(x)f(x)δ(x − x′), which gives Op(f) = f, Op(1) = I and f·Op(a) = Op(fa). By [[lem:iv5-calc-structure]] (a), each
h⟨x⟩∂_(z^μ) is, in every chart, a combination of the fields h∂_(y^i) with coefficients bounded with all derivatives, and
C^∞(M₀) ⊂ C^∞_(uni,ℬ); so the operator is, in every chart, Σ_(|β|≤k) w a′_β(y)(h∂_y)^β with a′_β bounded with all
derivatives uniformly. This characterises wDiff^k within the parameterised calculus ((S7), [Hin26d, p. 59]). Modulo
whS^(k−1), only the terms of order k without a further power of h remain, which gives the principal symbol. The
memberships listed follow from [[lem:iv5-0-2]] (a), (d) and [[eq:iv5-2-1]], the coefficients of P_h, given on
{r ≥ ½r_♯}, being extended to elements of C^∞(M₀). For h^kQ, a term of Q of order j < k carries the factor h^(k−j).

(b) Compositions, adjoints, principal symbols and Poisson brackets are [Hin26d, Theorem 3.51] on N_(P′) ((S5), (S16)),
and the exact sequence is [Hin26d, Definition 3.43] with ρ̄ = h. Operators on ℂ⁵ are 5 × 5 matrices of scalar operators
((S14)), so compositions and principal symbols multiply as matrices. The adjoint of [Hin26d, Theorem 3.51] is taken for
a uniformly positive 𝒱-density, such as μ_h of the proof of [[lem:iv5-calc-dual]], and the Euclidean inner product of
ℂ⁵; call it A^⋆. Then A* = (⟨x⟩⁵B̂)⁻¹A^⋆(⟨x⟩⁵B̂), with B̂ the matrix of B; as ⟨x⟩⁵ is a weight and B̂^(±1) ∈ Ψ⁰ by (a),
A* ∈ w_1Ψ^(m_1) with principal symbol B̂⁻¹a_1^⋆B̂ = a_1^(*_B). If a_1a_2 = a_2a_1, then [A_1, A_2] has principal symbol 0
and lies in hΨ by the exact sequence. If A_1 = Op(a_1) + hE with a_1 scalar, then [Op(a_1), A_2] is the matrix of the
scalar commutators [Op(a_1), (A_2)_(kl)], and [Hin26d, Theorem 3.51] gives the principal symbol of i[Op(a_1), (A_2)_(kl)]
as the Poisson bracket of T*M₀°. In terms of the covector h⁻¹Σ_μ ζ_μ dz^μ/⟨x⟩ of [[lem:iv5-calc-structure]] (d), this
is h times the Poisson bracket of a_1 and (a_2)_(kl) for the covector Σ_μ ζ_μ dz^μ/⟨x⟩, that is hH_(a_1)(a_2)_(kl).
Finally h⁻¹[hE, A_2] = [E, A_2] has principal symbol [e, a_2].

(c) Choose a real y ∈ C^∞(𝒫) with y = 1 near K_a and supp y in the interior of K. Put
A_0 := Op(y)·½(Op(a) + Op(a)*)·Op(y)*, which is self-adjoint, and A := ψA_0ψ, which is self-adjoint as ψ is real and
scalar, and whose Schwartz kernel is supported in supp ψ × supp ψ. By (b), A has principal symbol ψ²yay = a, so
A − Op(a) ∈ whΨ^(m−1). Op(y) is microsupported in supp y ([[lem:iv5-calc-disjoint]] (a)), hence so is A
([[lem:iv5-calc-disjoint]] (b)), and so A is microsupported in K.

(d) This is [Hin26d, Theorem 3.44] on N_(P′) ((S5)) and the reduction, after conjugation by the weight ⟨x⟩^(5/2) ((b));
the factor h^(5/2) of the norms appears on both sides. An element of w_1h^(2N)Ψ^(−2N) maps w_2H^(−N) to w_1w_2H^N with
norm O(h^(2N)).

(e) Let a, g be representatives of the principal symbols of A and G. Every point of K ∩ ∂_ħ has a neighbourhood in 𝒫
on which a and g are invertible with the bounds of [[def:iv5-calc-micro]]. As K ∩ ∂_ħ is compact, there are an open set
O′ ⊃ K ∩ ∂_ħ whose closure is covered by finitely many of these neighbourhoods, and C₀, such that ga is invertible on
cl O′ ∩ 𝒫° with |(ga)⁻¹| ≤ C₀w′⁻¹ρ_∞^m.

*Reduction to K ⊂ O′.* Choose a real y ∈ C^∞(𝒫) with y = 1 near K, whose support meets ∂_ħ only inside O′ (possible by
compactness, as K ∩ ∂_ħ ⊂ O′), and a real ψ ∈ C^∞(𝒫) with ψ = 1 near supp y ∩ ∂_ħ and supp ψ ⊂ O′. Then
B = BOp(yψ) + BOp(y(1 − ψ)) + BOp(1 − y). The last term lies in h^∞Ψ^(−∞) by the definition of microsupport, and
y(1 − ψ) is supported in a closed set disjoint from ∂_ħ, so the second lies in h^∞Ψ^(−∞) by [[lem:iv5-calc-disjoint]]
(d). And BOp(yψ) is microsupported in K′ := supp(yψ) ⊂ O′ ([[lem:iv5-calc-disjoint]] (a), (b)).

*One step.* Let B′ ∈ Ψ⁰ be microsupported in a closed set K′ ⊂ O′, and let K″ ⊂ O′ be closed with K′ in its interior.
Choose real φ_1, φ_2, φ_3 ∈ C^∞(𝒫) with φ_1 = 1 near K′, φ_2 = φ_3 = 1 near supp φ_1, and supp φ_2, supp φ_3 ⊂ K″. Put
q := φ_2(ga)⁻¹ ∈ w′⁻¹S^(−m), by [[lem:iv5-calc-structure]] (d) and the formula ∂(e⁻¹) = −e⁻¹(∂e)e⁻¹ applied to
e := w′⁻¹ρ_∞^m ga. By (b), Op(φ_1q)GA has principal symbol φ_1qga = φ_1φ_2 = φ_1, so
R_1 := h⁻¹(Op(φ_1) − Op(φ_1q)GA) ∈ Ψ^(−1). Both Op(φ_1) and Op(φ_1q)GA are microsupported in supp φ_1
([[lem:iv5-calc-disjoint]] (a), (b)), hence so is R_1. Therefore

    B′ = B′Op(φ_1) + B′Op(1 − φ_1) = B′Op(φ_1q)GA + hB′R_1Op(φ_3) + R′,

with R′ ∈ h^∞Ψ^(−∞), as B′Op(1 − φ_1) and B′R_1Op(1 − φ_3) are. By (d), for every σ and N,

    ‖B′u‖_(wH^σ) ≤ C(‖GAu‖_(ww′H^(σ−m)) + h‖Op(φ_3)u‖_(wH^(σ−1)) + h^N‖u‖_(wH^(−N))),

and Op(φ_3) is microsupported in K″ ⊂ O′ ([[lem:iv5-calc-disjoint]] (a)).

*Iteration.* Let J be an integer with J ≥ N + max(s, 0), and choose closed sets K′ = K_0 ⊂ K_1 ⊂ ⋯ ⊂ K_J ⊂ O′, each in
the interior of the next. Apply the step to BOp(yψ) with σ = s and K″ = K_1, then to the operator Op(φ_3) so obtained
with σ = s − 1 and K″ = K_2, and so on. After J steps the remaining term is at most
Ch^J‖u‖_(wH^(s−J)) ≤ Ch^N‖u‖_(wH^(−N)), as J ≥ N and s − J ≤ −N. This gives [[eq:iv5-calc-ell]]. Each identity
B′u = B′Op(φ_1q)GAu + hB′R_1Op(φ_3)u + R′u holds for u ∈ wH^(−N), all terms being defined by (d); if GAu ∈ ww′H^(s−m),
then, going back from the last step, each Op(φ_3)u lies in wH^(σ−1), and so Bu ∈ wH^s.

(f) Put q̂ := w⁻²ρ_∞^(2k)q ∈ S⁰. It is B-self-adjoint, and its spectrum lies in [c, C₁] on W ∩ 𝒫°, C₁ := sup|q̂|. With
γ a fixed contour in {Re z > 0} around [c, C₁], at distance at least c/2 from it, q̂^(±1/2) = (2πi)⁻¹∮_γ z^(±1/2)(z −
q̂)⁻¹dz on W ∩ 𝒫°; this is the B-self-adjoint, positive definite square root and its inverse, as q̂ is diagonalisable
with real eigenvalues in [c, C₁] for B. For z ∈ γ, |(z − q̂)⁻¹| ≤ 2/c in the norm of B, and a derivative ∂_y^β∂_ξ^γ(z
− q̂)⁻¹ in the coordinates of a chart is a sum of products of (z − q̂)⁻¹ and derivatives of q̂, each bounded with the
weights ⟨ξ⟩^(−|γ|) of S⁰, uniformly. So q̂^(±1/2) satisfies the estimates of S⁰ on W ∩ 𝒫°, and q^(±1/2) =
w^(±1)ρ_∞^(∓k)q̂^(±1/2) those of w^(±1)S^(±k). The principal symbol of Op(φq^(1/2))*Op(φq^(1/2)) is
(φq^(1/2))^(*_B)φq^(1/2) = φ²q by (b). If q = fq′ as stated, f^(1/2)q′^(1/2) is B-self-adjoint, positive semidefinite,
and squares to q.

(g) and (h) are [[lem:iv5-calc-dual]] and [[lem:iv5-calc-reg]].

(i) The proofs are the same, with [[lem:iv5-calc-structure]] and [[lem:iv5-calc-disjoint]] for ℬ_eb, |dt dx| = r⁵ times
the eb-density of [[lem:iv5-calc-structure]] (c), and 𝒫_eb. For the calculi with scalings 1, P′ is a single point and ρ̄
is 1, so the exact sequence lowers the order without a factor h.

(j) The family (ℬ^×_h)_((b,h)∈U×(0,1]) is a parameterised scaled bounded geometry structure ((S7)), and the proofs above,
and those of [[lem:iv5-calc-disjoint]]–[[lem:iv5-calc-reg]], [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]], apply
verbatim with countable subsets of U × (0, 1] in place of countable subsets of (0, 1]. ∎

**Lemma {#lem:iv5-calc-garding}** (A supremum bound with a margin.) (a) Let T ∈ Ψ⁰_(3b,ħ) have principal symbol
represented by t, put t_R := ½(t + t^(*_B)), and suppose that B(t_Rv, v) ≤ M B(v, v) on 𝒫° for all v, for some M ≥ 0.
Then for every η > 0 there is C such that for h ∈ (0, 1] and v ∈ L²

    Re⟨Tv, v⟩ ≤ (M + η)‖v‖² + Ch‖v‖²_(H^(−1/2)_(3b,h)).                                            {#eq:iv5-calc-garding}

(b) If w is a real weight and T ∈ w²Ψ⁰_(3b,ħ) has principal symbol w²t with t as in (a), then
Re⟨Tv, v⟩ ≤ (M + η)‖wv‖² + Ch‖wv‖²_(H^(−1/2)_(3b,h)) whenever wv ∈ L².

(c) The same holds in the eb-calculus.

The constant C depends only on M, η and on bounds for T and t in their classes; by [[prop:np-10-65-a]] (j) it is
uniform for families depending on a parameter b with such bounds uniform in b.

*Proof.* (a) The symbol M + η − t_R is B-self-adjoint and B((M + η − t_R)v, v) ≥ ηB(v, v) on 𝒫°. By
[[prop:np-10-65-a]] (f), with k = 0, w = 1, W = 𝒫 and φ = 1, θ_η := (M + η − t_R)^(1/2) ∈ S⁰, and Θ_η := Op(θ_η) is such
that Θ_η*Θ_η has principal symbol M + η − t_R. The operator ½(T + T*) has principal symbol t_R, and Op(1) = I
([[prop:np-10-65-a]] (a), (b)). So R := (M + η)I − ½(T + T*) − Θ_η*Θ_η ∈ Ψ⁰_(3b,ħ) has principal symbol 0, and
R ∈ hΨ^(−1)_(3b,ħ) ([[prop:np-10-65-a]] (b)). Pairing with v,

    (M + η)‖v‖² − Re⟨Tv, v⟩ = ‖C₀v‖² + ⟨Rv, v⟩ ≥ −Ch‖v‖²_(H^(−1/2)_(3b,h)),

by [[prop:np-10-65-a]] (d) and the bound of [[lem:ii-a-7-1]] (1), transferred as in the proof of [[lem:iv5-calc-dual]].

(b) Apply (a) to w⁻¹Tw⁻¹ ∈ Ψ⁰_(3b,ħ), which has principal symbol t by [[prop:np-10-65-a]] (b), and to wv:
⟨Tv, v⟩ = ⟨w⁻¹Tw⁻¹(wv), wv⟩, as w is real and scalar.

(c) The proof is the same ([[prop:np-10-65-a]] (i)). ∎

[[lem:iv5-calc-garding]] is a semiclassical analogue of [[lem:ii-a1-2-6]], stated for Re⟨Tv, v⟩ rather than for
‖Op(z)v‖²: the remainder of order −1 + 2δ there becomes a remainder of size O(h) here.

**Lemma {#lem:iv5-calc-q0}** (A lower bound for a non-semiclassical operator.) Let w be a real weight, and let
Q ∈ w²Diff²_3b(M₀°; ℂ⁵) be independent of h, with ⟨Qu, v⟩ = ⟨u, Qv⟩ for u, v ∈ C_c^∞(M₀°). Let 𝒪 ⊂ M₀ be open and K ⊂ 𝒪
closed, and suppose that a representative q of the principal symbol of w⁻¹Qw⁻¹, homogeneous of degree 2, satisfies
B(q(z, ζ)v, v) ≥ c|ζ|²B(v, v) for z ∈ 𝒪 ∩ M₀°, all ζ and all v, for some c > 0. Then there is C such that

    ⟨Qv, v⟩ ≥ −C‖wv‖²_(L²)   for every v with wv ∈ H¹_3b and supp v ⊂ K.                              {#eq:iv5-calc-q0}

The same holds in the eb-calculus. By [[prop:np-10-65-a]] (j), C is uniform for families depending on a parameter b,
when the coefficients are bounded and c is bounded below uniformly in b.

*Proof.* Put u := wv and Q̃ := w⁻¹Qw⁻¹ ∈ Diff²_3b. Then ⟨Qv, v⟩ = ⟨Q̃u, u⟩, Q̃ is symmetric, and its principal symbol
is represented by q, which is B-self-adjoint ([[prop:np-10-65-a]] (a), (b)). Choose φ ∈ C^∞(M₀) with 0 ≤ φ ≤ 1, φ = 1
near K and supp φ ⊂ 𝒪, and put q_* := φ²q + (1 − φ²)|ζ|², where |ζ|² denotes |ζ|² times the identity. Then q_* is
B-self-adjoint and B((q_* + 1)v, v) ≥ min(c, 1)⟨ζ⟩²B(v, v). By [[prop:np-10-65-a]] (f), (i) (non-semiclassical, with
k = 1 and W the whole compactified bundle ³ᵇT̄*M₀), θ := (q_* + 1)^(1/2) ∈ S¹ and θ⁻¹ ∈ S^(−1). Put Θ := Op(θ) and Θ′ :=
Op(θ⁻¹). By [[prop:np-10-65-a]] (b), Θ*Θ − I − Op(q_*) and Q̃ − Op(q) lie in Ψ¹_3b, and Θ′Θ − I ∈ Ψ^(−1)_3b. By
[[prop:np-10-65-a]] (a), Op(q_*) = φ²Op(q) + (1 − φ²)Op(|ζ|²). As φu = u and multiplication by a real scalar function
is symmetric for ⟨·, ·⟩, ⟨φ²Op(q)u, u⟩ = ⟨Op(q)u, u⟩ and ⟨(1 − φ²)Op(|ζ|²)u, u⟩ = 0. Hence

    ⟨Q̃u, u⟩ = ‖Θu‖² − ‖u‖² + ⟨Ru, u⟩,     R ∈ Ψ¹_3b.

Now |⟨Ru, u⟩| ≤ C₁‖u‖²_(H^(1/2)_3b) by [[prop:np-10-65-a]] (d) and [[lem:ii-a-7-1]] (1). For ε > 0,
‖u‖²_(H^(1/2)_3b) ≤ ε‖u‖²_(H¹_3b) + C_ε‖u‖², by [Hin26d, (3.14)] ([[rem:std-sbg-sobolev]]) with scalings 1, the norms
being sums of norms on ℝ⁵ of the same functions and ⟨ξ⟩ ≤ ε⟨ξ⟩² + (4ε)⁻¹. And
‖u‖_(H¹_3b) ≤ ‖Θ′Θu‖_(H¹_3b) + ‖(Θ′Θ − I)u‖_(H¹_3b) ≤ C₂(‖Θu‖ + ‖u‖), by [[prop:np-10-65-a]] (d). With ε := (4C₁C₂²)⁻¹
this gives ⟨Q̃u, u⟩ ≥ ½‖Θu‖² − C‖u‖² ≥ −C‖u‖², which is [[eq:iv5-calc-q0]]. The eb-case is the same. ∎

[[lem:iv5-calc-q0]] is applied to h-independent operators of the form h⁻²Re(□_h + CL_h*ρ_sf⁻²L_h), whose principal
symbol G + Cρ_sf⁻²ℓ² is controlled by [[lem:iv5-0-4]]; only this lower bound is used, not a factorisation of the
operator.

## Placement

This section and the two after it are instructions for the merge, not text of the edition. Each old text is copied from
the chapter as it stands at HEAD (commit fb87f2fc; chapter 33 md5 9571426c902bea231329690543c17455, chapter 95 md5
66591dd9e2c8ea3b473734520ba92b4a, chapter 23 md5 58661f3220bae91f567080b61ae42d3d, chapter 98 md5
636613260a16fe478f9e06a7e27cacd4), as whole lines between the fences, and occurs exactly once in its chapter. Each new
text replaces its old text as a whole, with the line breaks shown; no rewrapping is needed, and every line has at most
121 characters, also after the labels resolve. Line numbers are those of these files and serve only to find the place.
P-G1 is merged before P-G24b; see the section on the merge order.

### Chapter 33

**C33-1. The calculus sentence of def:iv5-0-1** (lines 1275–1277).

Old (3 lines):

```text
The semiclassical 3b-pseudodifferential calculus Ψ_(3b,ħ)(M^♭) carries with it its principal symbols, the operator wave
front set WF′_(3b,ħ), the elliptic set Ell_(3b,ħ), elliptic parametrices, the sharp Gårding inequality and the Sobolev
spaces H^s_(3b,h); it exists in this dimension by [[prop:np-10-65-a]]. Write
```

New (4 lines):

```text
The semiclassical 3b-pseudodifferential calculus Ψ_(3b,ħ)(M^♭), with its principal symbols, operator wave front sets
WF′_(3b,ħ), elliptic sets Ell_(3b,ħ) and Sobolev spaces H^s_(3b,h), is that of [[sec:iv5-calc]]. It is built from the
cells of [[def:iv5-calc-cells]], with four spatial coordinates, and the facts used about it are those of
[[prop:np-10-65-a]], [[lem:iv5-calc-garding]] and [[lem:iv5-calc-q0]]. Write
```

**C33-2. The spaces on Ω, end of def:iv5-0-1** (lines 1281–1284).

Old (4 lines):

```text
([Hin26a, (5.19)]), normed with the density |dg| and the fibre inner product B of [[lem:iv5-0-4]]. On Ω there are three
kinds of space: H^(s,(·))_(3b,h)(Ω)^(•,−), restrictions to Ω° of elements with support in {t ≥ 0}, so supported at X_0
and extendible at Σ^♯; (·)^(−,•), extendible at X_0 and supported at Σ^♯; and H̄, extendible at both ([Hin26a,
Section 2.3]). In all of these constructions the dimension enters only as the number of coordinates.
```

New (4 lines):

```text
([Hin26a, (5.19)]), normed with the density |dg| and the fibre inner product B of [[lem:iv5-0-4]]. On Ω there are three
kinds of space, defined in [[lem:iv5-calc-dual]]: H^(s,(·))_(3b,h)(Ω)^(•,−), restrictions to {r > r_♯} of elements with
support in {t ≥ 0}, so supported at X_0 and extendible at Σ^♯; (·)^(−,•), extendible at X_0 and supported at Σ^♯; and
H̄, extendible at both. In all of these constructions the dimension enters only as the number of coordinates.
```

**C33-3. Delete the old prop:np-10-65-a** (lines 1286–1293).

Old (8 lines):

```text
**Proposition {#prop:np-10-65-a}** (The calculus in every dimension.) The semiclassical 3b-calculus of [Hin26a,
Section 2.3] is constructed on ℝ_t × ℝ^(N−1)_x for every N ([Hin23d, pp. 3, 7, 10–12, and Proposition 5.10, p. 109],
N the spacetime dimension), as bounded geometry pseudodifferential operators in the sense of [Shu92] ([Hin23d, p. 12]),
and its bounded geometry construction is that of [Hin26d] for a smooth manifold of any dimension ([Hin26d, Definitions
1.3 and 1.9 and Section 3], with the 3b-algebra among its examples in every dimension, [Hin26d, p. 14, example (10)]).
At N = 5 it is the calculus of the compactification M^♭ of [[def:iv5-0-1]], with fibres 𝕊³.

*Proof.* These are the cited results, stated there for every dimension. ∎
```

New: none.

The lines are deleted together with the blank line that follows them (line 1294), so that one blank line remains between
the paragraph that ends at line 1284 and **Lemma {#lem:iv5-0-2}**. The label moves to the new section (C33-4).

**C33-4. Insert the new section** (before line 1396).

Insert lines 1–575 of this file, from the heading of [[sec:iv5-calc]] through the remark that follows
[[lem:iv5-calc-q0]] (the paragraph ending "not a factorisation of the operator."), followed by one blank line,
immediately before the line

```text
#### Elliptic estimates and the characteristic set at fibre infinity {#sec:iv5-1}
```

that is, after the paragraph *Notation* ([Hin26a, (5.19)]) and before [[sec:iv5-1]].

**C33-5. Proof of prop:iv5-1-2** (lines 1419–1421).

Old (3 lines):

```text
χ_(τ,2)χ_(r,2)ω = χ_(τ,2)χ_(r,2)ω′. By [[lem:iv5-1-1]], ρ_sf⁻²P_h is elliptic on WF′(B_1). A microlocal parametrix in
the calculus of [[def:iv5-0-1]] gives the estimate; the weights only add terms of lower order, since
w⁻¹[P_h, w] ∈ hρ_sf²Diff¹_3b for w = ρ_sf^β ρ_K^(β′). ∎
```

New (5 lines):

```text
χ_(τ,2)χ_(r,2)ω = χ_(τ,2)χ_(r,2)ω′. By [[lem:iv5-1-1]], ρ_sf⁻²P_h is elliptic on WF′(B_1), and B_1χ_(τ,1)χ_(r,1) is
elliptic on WF′(B_0χ_(τ,2)χ_(r,2)), as χ_(•,1) = 1 near supp χ_(•,2) ([[lem:iv5-calc-disjoint]] (b), (c)). So
[[prop:np-10-65-a]] (e), applied to ω′ with A := P_h ∈ ρ_sf²Ψ²_(3b,ħ), G := B_1χ_(τ,1)χ_(r,1) and
B := B_0χ_(τ,2)χ_(r,2), gives the estimate, in the weighted spaces and in the strong sense. For P_h* the proof is the
same, its principal symbol being G + iℓ. ∎
```

**C33-6. Proof of prop:iv5-1-3, first sentence** (lines 1438–1439). The rest of the paragraph, from line 1440, is
unchanged.

Old (2 lines):

```text
*Proof.* We prove [Hin26a, (5.21)] for ω ∈ H^(s,(α_sf,α_K))_(3b,h); the strong sense follows by the standard
regularisation ([Hin26a, p. 45]). By [[prop:iv5-1-2]] it suffices to work in an h-independent neighbourhood of ∂Σ_±;
```

New (10 lines):

```text
*Proof.* We prove [Hin26a, (5.21)] for ω ∈ H^(s,(α_sf,α_K))_(3b,h). The strong sense follows by running the same
argument with the commutant aj_ε, j_ε := ⟨εζ⟩^(−K) as in [[lem:iv5-calc-reg]] with K so large that every pairing below
is finite when the right side of [[eq:iv5-fib]] is. By [[lem:iv5-calc-reg]] (c), H_G(aj_ε) = j_εH_Ga + ϑ_εj_εae_G, so
the terms in which j_ε is differentiated are bounded multiples of a²j_ε², uniformly in ε, like the terms in which the
weights are differentiated; they join the term hAB̃_2A below and are absorbed in the same way. The estimate then holds,
by the argument below with [[prop:np-10-65-a]] (e) and the same iteration, with B_0χ_(τ,2)χ_(r,2)ω replaced by
J_εB_0χ_(τ,2)χ_(r,2)ω, J_ε := Op(j_ε), and with a constant independent of ε. As ε → 0, J_εB_0χ_(τ,2)χ_(r,2)ω tends to
B_0χ_(τ,2)χ_(r,2)ω in H^(−N,(α_sf,α_K))_(3b,h) ([[lem:iv5-calc-reg]] (b)) and is bounded in H^(s,(α_sf,α_K))_(3b,h); a
weakly convergent subsequence identifies the limit, which therefore lies in H^(s,(α_sf,α_K))_(3b,h) and satisfies the
estimate. By [[prop:iv5-1-2]] it suffices to work in an h-independent neighbourhood of ∂Σ_±;
```

**C33-7. The commutant of prop:iv5-1-3** (line 1445).

Old (1 line):

```text
and a quantisation A = A* with WF′(A) = supp a. Then [Hin26a, (5.25)] holds:
```

New (2 lines):

```text
and a quantisation A = A* of a ([[prop:np-10-65-a]] (c)), microsupported in a closed neighbourhood of supp a as small as
needed below. Then [Hin26a, (5.25)] holds:
```

**C33-8. (5.26)** (line 1452).

Old (1 line):

```text
subprincipal, □_h having real scalar principal symbol. This gives [Hin26a, (5.26)]:
```

New (2 lines):

```text
subprincipal, □_h having real scalar principal symbol. With the square roots of [[prop:np-10-65-a]] (f) and the rules of
[[prop:np-10-65-a]] (b), this gives [Hin26a, (5.26)], with E microsupported near supp a ([[lem:iv5-calc-disjoint]] (b)):
```

**C33-9. The absorption in prop:iv5-1-3** (line 1464).

Old (1 line):

```text
of the main term, and absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + h^N‖ω‖². Iterate in h^(1/2) on the error term
```

New (2 lines):

```text
of the main term, and absorb h⟨B̃_2Aω, Aω⟩ ≤ Ch‖B̃_0Aω‖² + h^N‖ω‖², which holds by [[prop:np-10-65-a]] (e), B̃_0 being
elliptic on a neighbourhood of supp a in which A is microsupported. Iterate in h^(1/2) on the error term
```

**C33-10. The commutant of prop:iv5-2-1 (1)** (line 1506).

Old (1 line):

```text
a = ρ_K^(−α_K)ψ(r)χ_K(𝔛ρ_K)χ_0(𝔛|ζ|), and A = A*. The pairing is [Hin26a, (5.37)–(5.38)]:
```

New (2 lines):

```text
a = ρ_K^(−α_K)ψ(r)χ_K(𝔛ρ_K)χ_0(𝔛|ζ|), and A = A* a quantisation of a as in [[prop:np-10-65-a]] (c), with Schwartz kernel
supported in K × K. The pairing is [Hin26a, (5.37)–(5.38)]:
```

**C33-11. The Q-terms of prop:iv5-2-1 (1)** (lines 1525–1529).

Old (5 lines):

```text
For Q: Q_0 has the positive definite principal symbol G + Cρ_sf⁻²ℓ² ([[lem:iv5-0-4]]), so Q_0 = Θ*Θ + R with
R ∈ Ψ^(−∞)_3b, which is [Hin26a, (5.44)]; the symbol of h⁻¹h³Q_1 vanishes quadratically at o, so it is O(𝔛⁻²) on
supp a, which gives [Hin26a, (5.45)] by Gårding; and the double commutator lies in hΨ and gives [Hin26a, (5.46)].
Collecting, fix 𝔛 large and then h small to absorb ‖Aω‖². Then [Hin26a, (5.47)], with WF′(F) ⊂ Ell(𝓛_h), gives
[Hin26a, (5.48)], and finitely many iterations in h^(1/2) give [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

New (30 lines):

```text
For Q, write −h⁻¹⟨AQAω, ω⟩ = −h⟨Q_0Aω, Aω⟩ − ⟨h²Q_1Aω, Aω⟩, A being self-adjoint.

*The term with Q_0* ([Hin26a, (5.44)]). Q_0 ∈ ρ_sf²Diff²_3b is independent of h and symmetric, and its principal symbol
G + Cρ_sf⁻²ℓ² satisfies B(ρ_sf⁻²(G + Cρ_sf⁻²ℓ²)v, v) ≥ c|ζ|²B(v, v) over a neighbourhood of Ω, by [[lem:iv5-0-4]] and
continuity from Ω; near K, ρ_sf lies between two positive constants. As the Schwartz kernel of A lies in K × K,
[[lem:iv5-calc-q0]], with w = 1, gives −h⟨Q_0Aω, Aω⟩ ≤ Ch‖Aω‖².

*The term with Q_1* ([Hin26a, (5.45)]). T := h²Q_1 ∈ ρ_sf²Ψ²_(3b,ħ) is self-adjoint, and its principal symbol q₁₀ is the
principal symbol of Q_1 evaluated at ζ, homogeneous of degree 2 ([[prop:np-10-65-a]] (a)). So |q₁₀(z, ζ)| ≤ C₂|ζ|² over
a fixed neighbourhood V of K, where C₂ is the supremum of |q₁₀| over the unit sphere bundle above V, independent of 𝔛.
Let ã := χ̃(𝔛|ζ|)φ(z), with χ̃ ∈ C_c^∞((−3, 3)), 0 ≤ χ̃ ≤ 1, χ̃ = 1 on [−5/2, 5/2], and φ ∈ C^∞(M₀), 0 ≤ φ ≤ 1, equal to
1 near K and supported in V; put Ã := Op(ã). As χ_0 is supported in (−2, 2), A may be taken microsupported in a closed
set near which ã = 1; then (I − Ã)A = Op(1 − ã)A lies in h^∞Ψ^(−∞)_(3b,ħ) ([[def:iv5-calc-micro]]). The self-adjoint
operator Ã*TÃ has principal symbol ã²q₁₀, and |ã²q₁₀| ≤ 9C₂𝔛⁻² everywhere. [[lem:iv5-calc-garding]] (a), applied with
η := 𝔛⁻² to Ã*TÃ and to −Ã*TÃ, gives |⟨Ã*TÃAω, Aω⟩| ≤ ((9C₂ + 1)𝔛⁻² + C_𝔛h)‖Aω‖². The difference
⟨TAω, Aω⟩ − ⟨Ã*TÃAω, Aω⟩ is a sum of three terms, each containing (I − Ã)Aω = (I − Ã)Aχω, whose norm in every H^k_(3b,h)
is O(h^N‖χω‖_(ρ_K^(α_K)H^(−N)_(3b,h))) ([[prop:np-10-65-a]] (d)); so it is at most
𝔛⁻²‖Aω‖² + C_(𝔛,N)h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h)). Hence

    |Re h⁻¹⟨Ah³Q_1Aω, ω⟩| ≤ ((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² + C_(𝔛,N)h^(2N)‖χω‖²_(ρ_K^(α_K)H^(−N)_(3b,h)),

which is [Hin26a, (5.45)] with 9C₂ + 2 for 2C and an additional term of the form of the last term in (1).

*The double commutator* (1/(2h))[A, [A, Q]] lies in hΨ_(3b,ħ), the principal symbol of A being scalar
([[prop:np-10-65-a]] (b)), and gives [Hin26a, (5.46)].

Collecting, the Q-terms add at most (9C₂ + 2)𝔛⁻² + C′_𝔛h to the coefficient −c_0 of ‖Aω‖², where C₂ does not depend
on 𝔛 and C′_𝔛 does not depend on h: fix 𝔛 large
and then h small to absorb ‖Aω‖². Then [Hin26a, (5.47)], with WF′(F) ⊂ Ell(𝓛_h) and [[prop:np-10-65-a]] (e), gives
[Hin26a, (5.48)], and finitely many iterations in h^(1/2) give [Hin26a, (5.33)], with δ := 𝔛⁻¹.
```

The last two lines of this new text are the old text of variant A of T41 in P-G24b, unchanged.

**C33-12. prop:iv5-2-1 (2)** (line 1534).

Old (1 line):

```text
[[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound by [Hin26a, (5.44)–(5.45)], and the iteration is the same. ∎
```

New (3 lines):

```text
[[lem:iv5-0-5]] (6) on supp ψ′. Q enters with a lower bound, the adjoint pairing containing +h⁻¹⟨AQAω, ω⟩:
h⟨Q_0Aω, Aω⟩ ≥ −Ch‖Aω‖² by [[lem:iv5-calc-q0]], and ⟨h²Q_1Aω, Aω⟩ ≥ −((9C₂ + 2)𝔛⁻² + C_𝔛h)‖Aω‖² − C_(𝔛,N)h^(2N)‖χω‖² as
in (1), by [[lem:iv5-calc-garding]] applied to −Ã*h²Q_1Ã. The iteration is the same. ∎
```

The new text keeps "[[lem:iv5-0-5]] (6) on supp ψ′." at the start of its first line, so the old text of T7 in P-G24b,
which ends with these words, is still found once after this change.

**C33-13. prop:iv5-3-1** (lines 1572–1573).

Old (2 lines):

```text
c_0⁻¹h⁻²‖ρ_sf⁻¹A𝓛_hω‖² + ¼c_0‖ρ_sfAω‖² produces the weights of [Hin26a, (5.51)]. The rest is the proof of
[[prop:iv5-2-1]], with δ := 𝔛⁻¹.
```

New (6 lines):

```text
c_0⁻¹h⁻²‖ρ_sf⁻¹A𝓛_hω‖² + ¼c_0‖ρ_sfAω‖² produces the weights of [Hin26a, (5.51)]. The Q-terms are estimated as in the
proof of [[prop:iv5-2-1]], with the weight ρ_sf: [[lem:iv5-calc-q0]] applies to Q_0 with w = ρ_sf, as
ρ_sf⁻²(G + Cρ_sf⁻²ℓ²) = ρ_sf⁻²G + C(ρ_sf⁻²ℓ)² is positive definite over Ω ([[lem:iv5-0-4]]), and
[[lem:iv5-calc-garding]] (b) applies to Ã*h²Q_1Ã ∈ ρ_sf²Ψ⁰_(3b,ħ), with C₂ the supremum of |ρ_sf⁻²q₁₀| over the unit
sphere bundle above a neighbourhood of K; so ‖Aω‖ is replaced by ‖ρ_sfAω‖ in these bounds. The rest is the proof of
[[prop:iv5-2-1]], with δ := 𝔛⁻¹.
```

**C33-14. prop:iv5-4-1 (1)** (lines 1610–1611).

Old (2 lines):

```text
e₁ and e₂ are supported away from {|(r/t)/v − 1| ≤ δ_sf, ρ_sf ≤ 𝔛⁻¹} and give ‖Eω‖. The rest is the proof of
[[prop:iv5-2-1]].
```

New (2 lines):

```text
e₁ and e₂ are supported away from {|(r/t)/v − 1| ≤ δ_sf, ρ_sf ≤ 𝔛⁻¹} and give ‖Eω‖. The rest is the proof of
[[prop:iv5-2-1]], with the weighted Q-terms of [[prop:iv5-3-1]].
```

**C33-15. prop:iv5-5-2** (line 1708).

Old (1 line):

```text
is the proof of [[prop:iv5-2-1]]: 𝓛_h, the Q-terms [Hin26a, (5.44)–(5.46)], and the iteration.
```

New (2 lines):

```text
is the proof of [[prop:iv5-2-1]]: 𝓛_h, the Q-terms ([[lem:iv5-calc-q0]] and [[lem:iv5-calc-garding]], with the weight
ρ_sf as in [[prop:iv5-3-1]] in (b)–(c)), the double commutator, and the iteration.
```

**C33-16. Strong sense in prop:iv5-7-1** (line 2038).

Old (1 line):

```text
[[sec:iv5-1]]–[[sec:iv5-5]] hold for every s in the strong sense; near the zero section the order is irrelevant. They
```

New (3 lines):

```text
[[sec:iv5-1]]–[[sec:iv5-5]] hold for every s in the strong sense: near the zero section the operators have compact
operator wave front sets and the order is irrelevant, and at fibre infinity the regularisation in the proof of
[[prop:iv5-1-3]] applies. They
```

**C33-17. Duality in thm:iv5-7-3 (a)** (line 2107).

Old (1 line):

```text
H^(s,(α_sf,α_K))(Ω)^(•,−) and H^(−s,(−α_sf,−α_K))(Ω)^(−,•) ([Hin26a, Section 2.3]). So the Hahn–Banach theorem gives
```

New (2 lines):

```text
H^(s,(α_sf,α_K))(Ω)^(•,−) and H^(−s,(−α_sf,−α_K))(Ω)^(−,•), with constants independent of h ([[lem:iv5-calc-dual]]). So
the Hahn–Banach theorem gives
```

**C33-18. lem:iv5-8-1** (lines 2158–2160).

Old (3 lines):

```text
hence independently of b. The calculus estimates used (composition, elliptic parametrices, the sharp Gårding
inequality, L²-boundedness) have constants depending on finitely many seminorms of the symbols involved, which depend
continuously on b. Each absorption step needs h below a threshold determined by these quantities. So each h_0 and C is
```

New (7 lines):

```text
hence independently of b. The calculus facts used ([[prop:np-10-65-a]], [[lem:iv5-calc-garding]] and
[[lem:iv5-calc-q0]]) hold with constants uniform in b by [[prop:np-10-65-a]] (j): the coefficients of P_h and of Q_0,
Q_1, the symbols of the commutants, of their square roots and of the auxiliary operators, the ellipticity bounds and the
positivity margins are bounded uniformly for b ∈ U. In particular the constant 9C₂ + 2 in the proof of [[prop:iv5-2-1]]
is uniform, C₂ being the supremum of a symbol continuous in b over a compact set, and for each fixed 𝔛 the constant C_𝔛
is uniform, the square root in [[lem:iv5-calc-garding]] having the margin η = 𝔛⁻² for every b. Each absorption step
needs h below a threshold determined by these quantities. So each h_0 and C is
```

**C33-19. The eb-structure, sec:iv6-2** (lines 2431–2432).

Old (2 lines):

```text
(2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β, with U̸_β charts of 𝕊³, give the parameterised scaled bounded
geometry ([[prop:np-10-65-a]]). On it P_h := h²□^C = □_h − iL_h ∈ r⁻²Diff²_(eb,ħ)(M; 𝒯*) has principal symbol G − iℓ
```

New (3 lines):

```text
(2^j(k − 2), 2^j(k + 2))_t × (2^(j−2), 2^(j+2))_r × U̸_β, with U̸_β charts of 𝕊³, give the parameterised scaled bounded
geometry of [[def:iv5-calc-cells]], and [[prop:np-10-65-a]] (i) gives the semiclassical eb-calculus. On it
P_h := h²□^C = □_h − iL_h ∈ r⁻²Diff²_(eb,ħ)(M; 𝒯*) has principal symbol G − iℓ
```

**C33-20. The cone face in the proof of thm:iv6-2-1** (before line 2486).

Insert the paragraph

```text
The Q-terms are those of the proof of [[prop:iv5-2-1]] with r⁻¹ for ρ_sf: [[lem:iv5-calc-q0]] in the eb-calculus with
w = r⁻¹, the constant C being such that r²G + C(r²ℓ)² is positive definite on the model, as in [[lem:iv5-0-4]]; and
[[lem:iv5-calc-garding]] (b), (c) for the term with Q_1.
```

followed by one blank line, immediately before the line

```text
This gives [Hin26a, (B.39)], whose a priori term lies in τ ≤ (2.75/10)T, covered by [Hin26a, (B.34)]; and
```

which begins a paragraph. If T34 of P-G24b has already replaced that paragraph, insert before the first line of T34's new
text instead ("This gives, by the proof of [[prop:iv5-3-1]] (1), …").

No other site of chapter 33 changes. The display numbers [Hin26a, (5.44)–(5.48)] and [Hin26a] itself remain as
attributions.

### Chapter 23

**C23-1 (optional). The paraphrase (S7) in sec:ii-a-3** (lines 367–369).

Old (3 lines):

```text
(S7) [Hin26d, Definitions 3.58 and 3.59, p. 59.] For a parameterised scaled b.g. structure (ℬ^(p,×))_(p∈P), with all
bounds uniform in p, the above holds uniformly in p; operators are families with uniformly bounded symbols and residual
parts, bounded uniformly on the p-dependent spaces.
```

New (5 lines):

```text
(S7) [Hin26d, Definitions 3.58 and 3.59 and the text after them, with footnote 13, p. 59.] For a parameterised scaled
b.g. structure (ℬ^(p,×))_(p∈P), with all bounds uniform in p, operators are families with uniformly bounded symbols and
residual parts; they are bounded uniformly on the p-dependent spaces, and the properties of adjoints, compositions,
commutators and principal symbols in [Hin26d, Theorem 3.51] carry over verbatim. The boundedness is
[Hin26d, Theorem 3.44] for the scaled b.g. structure on P′ × M, P′ ⊂ P countable.
```

(S7) is cited at 23:778 (the proof of [[lem:ii-a-7-1]]: compositions, principal symbols and boundedness, covered by the
new text), at 27:444 (the proof of [[lem:ii-f-2-2]]: its (a) is covered, while its (c), an elliptic estimate asserted
uniformly in h and proved at 27:460, used the old words "the above holds uniformly in p") and at 37:824
(uniform equivalence of norms on a compact set of parameters, not a statement of p. 59). C23-1 is to be applied only
together with a check of 27:460 and 37:824. The uniformity there can be obtained by the reduction in the proof of
[[prop:np-10-65-a]] (statements on P′ × M for countable P′).

### Chapter 27

No change. [Hin23d, Lemma 2.25] (27:1256 and 27:1529) is the same lemma, "Fourier transform of symbols: conormal case",
with the same statement, in arXiv version 1 (p. 41) and in the published version, arXiv version 2 (p. 43). Neither site
cites a page.

### Appendix A (chapter 95)

**C95-1. The header of thm:std-sbg-calculus** (lines 851–853).

Old (3 lines):

```text
**Theorem {#thm:std-sbg-calculus}** ([Hin26d, Definitions 1.1–4.20, Lemmas 3.24 and 3.42, Propositions 2.3–4.22,
Remarks 3.13–3.48, Theorems 3.21–3.52, (1.6), (2.3), (2.5), (3.2), (3.26), (3.28), (4.24a–b), (4.27), (4.28),
pp. 2–75].) On a smooth manifold M of any dimension n, without boundary, the following hold.
```

New (4 lines):

```text
**Theorem {#thm:std-sbg-calculus}** ([Hin26d, Definitions 1.1–4.20, Lemmas 3.18, 3.20, 3.24 and 3.42,
Propositions 2.3–4.22, Remarks 3.13–3.56, Theorems 3.21–3.52, footnote 13, (1.6), (2.3), (2.5), (3.2), (3.19), (3.26),
(3.28), (3.30), (4.24a–b), (4.27), (4.28), pp. 2–75].) On a smooth manifold M of any dimension n, without boundary, the
following hold.
```

**C95-2. (S7)** (line 893).

Old (1 line):

```text
(S7) Parameterised structures [Hin26d, Definitions 3.58–3.59, p. 59].
```

New (34 lines):

```text
(S7) Parameterised structures [Hin26d, Definition 1.9, p. 9; p. 58 and Remark 3.56, p. 58; Definitions 3.58 and 3.59 and
the text after them, with footnote 13, p. 59]. Definition 1.9 defines a parameterized scaled bounded geometry structure
on (M, P) as a collection {𝓑_(p,×)} of scaled b.g. structures 𝓑_(p,×) = {(U_(α_p), φ_(α_p), ρ_(α_p))}, p ∈ P, "so that
the quantities A and the C^∞ bounds on transition functions in Definition 1.1 as well as the constants C_γ in (1.6) are
uniform also in p ∈ P", and two sentences later states: "Furthermore, it includes semiclassical bounded geometry
settings when P = (0, 1]_h if all 𝓑_(h,×) feature the same b.g. structure {(U_α, φ_α)}, and the scalings are
ρ_(α_h,i) = h for h ∈ (0, 1]." On p. 58 the space P × M = ⊔_(p∈P) {p} × M is considered "with P given the discrete
topology". Remark 3.56 (Subsets of P): "In applications, one often only works with operators defined for
(typically countable) subsets of parameters p ∈ P (e.g. in the semiclassical setting: sequences of semiclassical
parameters h_j ↘ 0). Since one can implement this simply by replacing P by such a subset
(and then defining the microlocalization locus as in (3.40) for the new set P), we do not explicitly allow for symbols
to be defined only on subsets of P here." Definition 3.58: "Let w = (w_p)_(p∈P) be a weight on (P × M, 𝓑^×). Let m ∈ ℝ.
Then we say that a family a = (a_p)_(p∈P) lies in wS^m(𝒱T*M) if a_p ∈ w_pS^m(𝒱_pT*M) for all p ∈ P, with uniformly
bounded symbol seminorms. …" After it: for w to be a weight, "a sufficient additional condition is that the ratios
w_(p,α)/w_(p,β) for α, β ∈ 𝒜_p with U_(p,α) ∩ U_(p,β) ≠ ∅ are uniformly bounded." Definition 3.59: "In the notation of
Definition 3.58, a 𝒱-pseudodifferential operator A ∈ wΨ^m_𝒱(M) is a family A = (A_p)_(p∈P) of operators
A_p = Op_(𝒱_p)(a_p) + R_p where the quantization map Op_(𝒱_p) is defined as in Definition 3.31,
(a_p)_(p∈P) ∈ wS^m(𝒱T*M), and (R_p)_(p∈P) is a family of residual operators R_p on (M, 𝓑_(p,×)) for which the conditions
in Definition 3.34 hold with uniform constants and operator norm bounds for all weights w′ in (3.30). The principal
symbol of A is the equivalence class of a in wS^m(𝒱T*M)/wρS^(m−1)(𝒱T*M). …" The text after it: "An operator
A = (A_p)_(p∈P) ∈ wΨ^m_𝒱(M) defines a uniformly bounded family of operators A_p :
w′_pH^s_(𝒱_p)(M) → w_pw′_pH^(s−m)_(𝒱_p)(M), and more generally A_p :
w′_pH^(s;k)_(𝒱_p;𝒲_p)(M) → w_pw′_pH^(s−m;k)_(𝒱_p;𝒲_p)(M). (This is in fact a special case of Theorem 3.44, applied to
the scaled b.g. structure (P × M, 𝓑^×) and the input u = (u_p)_(p∈P) where u_p = 0 for all p ≠ p_0 ∈ P and
u_(p_0) ∈ w′_(p_0)H^s_(𝒱_(p_0))(M) with norm ≤ 1, since then Au = (A_pu_p)_(p∈P) has norm ≤ C for some constant C only
depending on A; but the norm of Au is bounded from below by the w_pw′_pH^(s−m)_(𝒱_p)(M)-norm of A_(p_0)u_(p_0).) The
properties of adjoints, compositions, commutators, and principal symbols in Theorem 3.51 carry over verbatim."
(In the parenthesis, the subscripts p of the norm that bounds the norm of Au from below stand for p_0.) Footnote 13:
"Strictly speaking, one needs to apply this argument for all countable subsets P′ ⊂ P of parameters
(so that P′ × M is second countable and the total index set ⊔_(p′∈P′) 𝒜_(p′) is countable, as required in
Definition 1.1); but the uniform bound on the operators A_(p′) is independent of P′." And: "The membership
A = (A_p)_(p∈P) ∈ wDiff^m_𝒱(M) is characterized by requiring that each A_p is a differential operator, and
(φ_(p,α))_*A_p = Σ_(|β|≤m) w_(p,α)a_(p,α,β)(x)(ρ_(p,α)∂_x)^β where the C^∞((−2, 2)^n)-seminorms of the coefficients
a_(p,α,β) are uniformly (in p ∈ P, α ∈ 𝒜_p, β ∈ ℕ^n_0) bounded."
```

**C95-3. New item (S16)**, inserted after line 995, the last line of the paragraph of (S15), and before
[[rem:std-sbg-sobolev]].

The last line of (S15):

```text
analogous strengthening of Lemma 3.42)."
```

Insert after it, with one blank line before and after (49 lines):

```text
(S16) Residual operators, essential supports and wave front sets [Hin26d, Lemma 3.18 and the norm after it, p. 37;
Lemma 3.20, p. 38; Proposition 3.22, p. 39; Lemma 3.24 (1), p. 40; Definition 3.25, p. 41; the text after
Definition 3.31, p. 44; Definition 3.34, p. 46; Definition 3.43, p. 51; Theorem 3.51, p. 55; Definition 3.54 and
Proposition 3.55, p. 57]. Lemma 3.18 (Towards a norm): "There exists a finite subset W ⊂ 𝒲 which spans 𝒲 over
C^∞_(uni,𝓑)(M)." After it: "We can now define a norm on wH^(s;k)_(𝒱;𝒲)(M) by setting ‖u‖²_(wH^(s;k)_(𝒱;𝒲)) := Σ_(j=0)^k
Σ_(W_1,…,W_j∈W) ‖W_1 ⋯ W_ju‖²_(wH^s_𝒱)." Lemma 3.20 (Density): "The space C_c^∞(M) is dense in wH^s_𝒱(M) for all weights
w ∈ C^∞(M) on (M, 𝓑) and s ∈ ℝ, and also in wH^(s;k)_(𝒱;𝒲)(M) for all k ∈ ℕ₀." Proposition 3.22 (Duality): "Fix a
uniformly positive 𝒱-density μ on M, by which we mean that (φ_α)_*μ = μ_α(x)|dx¹_α/ρ_(α,1) ⋯ dxⁿ_α/ρ_(α,n)| where
μ_α ∈ C^∞((−2, 2)ⁿ) is uniformly bounded and inf_α inf_((−2,2)ⁿ) μ_α > 0. Let w ∈ C^∞(M) be a weight on (M, 𝓑), and let
s ∈ ℝ. Then the L²(M; μ)-pairing (u, v) ↦ ⟨u, v⟩ := ∫_M u v̄ dμ extends from C_c^∞(M) × C_c^∞(M) → ℂ to a nondegenerate
pairing wH^s_𝒱(M) × w⁻¹H^(−s)_𝒱(M) → ℂ, and thus (wH^s_𝒱(M))* = w⁻¹H^(−s)_𝒱(M). (3.19)" Lemma 3.24 (1):
"S⁰(𝒱T*M) = C^∞_(uni,𝓑*)(𝒱T*M)", 𝓑* being the phase space b.g. structure of (S8). Definition 3.25 uses the uniform
compactification u𝒱T*M of (𝒱T*M, 𝓑*) and "the continuous extension map j : C⁰_(uni,𝓑*)(𝒱T*M) → C⁰(u𝒱T*M)": "The
microlocalization locus of (M, 𝓑^×) is then the set 𝔐 := u𝒱T*M ∩ {j(λρ) = 0}", ρ and λ being the scaling weight (S2) and
an elliptic weight (S8), and "The essential support ess supp^w_𝔐 a ⊂ 𝔐 of a ∈ ⋃_(l,m) wρ^(−l)S^m(𝒱T*M) is defined by
𝔐 ∋ ϖ ∉ ess supp^w_𝔐 a ⟺ ∃ χ ∈ S⁰(𝒱T*M), χ(ϖ) ≠ 0 s.t. χa ∈ wρ^∞S^(−∞)(𝒱T*M), where we write wρ^∞S^(−∞) = ⋂_(m,l)
wρ^lS^m"; here χ(ϖ) is the value of j(χ). After Definition 3.31 (the quantization Op_𝒱 of (S4)): "By property (1) from
Definition 1.1, and using the standard mapping properties of quantizations of symbols on ℝⁿ, such quantizations Op_𝒱(a)
define bounded maps on C_c^∞(M), C^∞(M), and indeed w′C^∞_(uni,𝓑)(M) → ww′C^∞_(uni,𝓑)(M) for any weight w′.
(Thus, they can be composed.)" Definition 3.34 (Residual operators): "Let w ∈ C^∞(M) be a weight on (M, 𝓑); recall the
scaling weight ρ ∈ C^∞(M) from Definition 3.6. Then the space wρ^∞Ψ^(−∞)_𝒱(M) of residual operators consists of all
linear operators R : C_c^∞(M) → C_c^∞(M) with the following properties. (1) For all weights w′ ∈ C^∞(M) on (M, 𝓑) and
for all N ∈ ℝ, k ∈ ℕ₀, the operator R : w′ρ^(−N)H^(−N;k)_(𝒱;𝒲)(M) → ww′ρ^NH^(N;k)_(𝒱;𝒲)(M). (3.30) is bounded. (2) Let
μ ∈ C^∞_(uni,𝓑)(M; ^𝒱ΩM) be a uniformly positive 𝒱-density. Then also the formal L²(M; μ)-adjoint R* of R is bounded as
a map (3.30) for all w′, N, k." Definition 3.43: "Let m ∈ ℝ, and let w ∈ C^∞(M) be a weight on (M, 𝓑). Then the space of
weighted 𝒱-pseudodifferential operators (of order m with weight w) is defined by wΨ^m_𝒱(M) := {Op_𝒱(a) + R :
a ∈ wS^m(𝒱T*M), R ∈ wρ^∞Ψ^(−∞)_𝒱(M)}. In the notation of Definition 3.25, the principal symbol of A = Op_𝒱(a) + R is
σ^(m,w)_𝒱(A) := [a] ∈ wS^m(𝒱T*M)/wρS^(m−1)(𝒱T*M), and its operator wave front set is WF′^w_𝒱(A) := ess supp^w_𝔐 a." and
"Directly from the definition, we have a short exact sequence 0 → wρΨ^(m−1)_𝒱(M) ↪ wΨ^m_𝒱(M) →^(σ^m_𝒱)
wS^m(𝒱T*M)/wρS^(m−1)(𝒱T*M) → 0." Theorem 3.51, whose first part is stated in (S5), is stated for "a uniformly positive
𝒱-density" and continues: "The principal symbol of i[A_1, A_2] ∈ wρ^(−(l_1+l_2−1))Ψ^(m_1+m_2−1)_𝒱(M) is the Poisson
bracket of the principal symbols of A_1, A_2." Definition 3.54 (𝒱-Sobolev wave front set): "Let w ∈ C^∞(M) be a weight
on (M, 𝓑), recall the scaling weight ρ ∈ C^∞(M) from Definition 3.6, and recall the microlocalization locus 𝔐 from
Definition 3.25. Let u ∈ wρ^(−∞)H^(−∞)_𝒱(M) = ⋃_(m,l) wρ^lH^m_𝒱(M). Then WF^(m,w,l)_𝒱(u) ⊂ 𝔐 is the complement of the
set of all ϖ ∈ 𝔐 for which there exists an operator A ∈ Ψ⁰_𝒱(M) which is elliptic at ϖ and for which Au ∈ wρ^lH^m_𝒱(M)."
Proposition 3.55 (Properties of the 𝒱-Sobolev wave front set): "Let u ∈ wρ^(−∞)H^(−∞)_𝒱(M) and A ∈ w′Ψ^(m′)_𝒱(M),
B ∈ Ψ⁰_𝒱(M). (1) u ∈ wρ^lH^m_𝒱(M) if and only if WF^(m,w,l)_𝒱(u) = ∅. (2) (Microlocality.)
WF^(m−m′,ww′,l)_𝒱(Au) ⊂ WF^(m,w,l)_𝒱(u) ∩ WF′^(w′)_𝒱(A). …"

The numbers and pages in (S1)–(S16) are those of arXiv version 1 of [Hin26d]. In the published version, Definitions 1.1,
1.3 and 1.9 and (1.6) are Definitions 1.2, 1.4 and 1.10 and (1.11); Proposition 2.3 is Proposition 2.4, with (2.3) and
(2.6) for (2.3) and (2.5); in Section 3 the displays and the items up to Definition 3.34 keep their numbers, and from
Lemma 3.36 to Definition 3.61 each number is increased by one, so that Proposition 3.39, Lemma 3.42, Definition 3.43,
Theorems 3.44, 3.51 and 3.52, Remarks 3.46–3.48, Definition 3.54, Proposition 3.55, Remark 3.56 and Definitions 3.58 and
3.59 are Proposition 3.40, Lemma 3.43, Definition 3.44, Theorems 3.45, 3.52 and 3.53, Remarks 3.47–3.49,
Definition 3.55, Proposition 3.56, Remark 3.57 and Definitions 3.59 and 3.60 there; footnote 13 is footnote 22; and in
Section 4, Proposition 4.2 and Definition 4.6 keep their numbers, Definitions 4.11, 4.14 and 4.20 and Propositions 4.15,
4.17, 4.18 and 4.22 are Definitions 4.12, 4.15 and 4.21 and Propositions 4.16, 4.18, 4.19 and 4.23, and each display
(4.n) is (4.n + 1).
```

### Bibliography (chapter 98)

**C98-1. [Hin23d]** (lines 76–77).

Old (2 lines):

```text
- [Hin23d] P. Hintz, *Microlocal analysis of operators with asymptotic translation- and dilation-invariances*, preprint
  (2023). arXiv:2302.13803v1
```

New (2 lines):

```text
- [Hin23d] P. Hintz, *Microlocal analysis of operators with asymptotic translation- and dilation-invariances*, Ars
  Inven. Anal. 2026, Paper No. 5, 159 pp. doi:10.15781/yw47vq75 arXiv:2302.13803v2
```

[Hin26d] and [Hin26a] are unchanged; after these changes [Hin23d] is cited only in chapter 27, and [Hin26a] in chapter 33
only as an attribution of statements and display numbers.

## Merge order with P-G24b

P-G1 is merged first, then P-G24b. P-G24b copied its old texts from chapter 33 with md5 007858d84d3f7b2ba03c0c84d0338749,
before the merge of P-T49; the current file differs from it by one line added near line 115 and by the new section at the
end, so from line 116 on its line numbers are one less than those above. The old texts of the two files were compared in
the current chapter:

- C33-11 contains the old text of T41. After C33-11, use variant A of T41: its old text is the last two lines of the new
  text of C33-11, which this revision keeps unchanged.
- C33-12 and T7 share the words "[[lem:iv5-0-5]] (6) on supp ψ′." at the start of line 1534: the old text of T7 ends with
  them and that of C33-12 begins with them. The new text of C33-12 keeps them at the start of its first line, so after
  C33-12 the old text of T7 is found exactly once, and T7 replaces it without touching the rest of the line.
- C33-20 inserts a paragraph before the line that begins the old text of T34 and changes no character of it; after both,
  the paragraph of C33-20 stands before the new text of T34, as P-G24b asks.
- Adjacent lines, no shared character: T42 (line 1463) and C33-9 (line 1464); T5 (line 1505) and C33-10 (line 1506).
- No other old text of one file shares a character with an old text of the other.

Checked by script on a scratch copy. In the current chapter each of the 43 old texts of P-G24b occurs exactly once. After
all texts of this file are applied, each of them other than T41 still occurs exactly once, the old text of variant A of
T41 occurs exactly once, and the old text of T41 itself no longer occurs, as intended. Applying P-G24b after that
(T41 by its variant A) leaves the chapters with no lint hit, no assembly problem and no line over 121 characters.

## Crosswalk rows (chapter 33)

Delete the row of prop:np-10-65-a (after the row of def:iv5-0-1), and insert the fourteen rows below, in this order,
after the row of lem:iv5-0-5 and before the row of sec:iv5-1, with the four tab-separated columns of the chapter's rows.
PIN stands for the commit that holds this version of this file; the merge pins it, as for the other proof files. The line
ranges are those of this file.

```text
sec:iv5-calc	paper/reader/proofs/P-G1.md@PIN:1-575	proof G1, the calculi	new section; replaces preprint citations
def:iv5-calc-cells	paper/reader/proofs/P-G1.md@PIN:14-48	proof G1, cells	4 + 1 cells; classes via P' x M
lem:iv5-calc-structure	paper/reader/proofs/P-G1.md@PIN:50-143	proof G1, structures	structures, weights, symbols
def:iv5-calc-micro	paper/reader/proofs/P-G1.md@PIN:145-158	proof G1, microsupport	two-sided microsupport, Ell, WF'
lem:iv5-calc-disjoint	paper/reader/proofs/P-G1.md@PIN:160-233	proof G1, disjoint supports	[Hin26d] Prop. 3.55, Def. 3.34
lem:iv5-calc-d	paper/reader/proofs/P-G1.md@PIN:235-279	proof G1, property (D)	at X_0 and Sigma^#
lem:iv5-calc-dual	paper/reader/proofs/P-G1.md@PIN:281-333	proof G1, duality	supported/extendible spaces
lem:iv5-calc-reg	paper/reader/proofs/P-G1.md@PIN:335-366	proof G1, regulariser	J_eps = Op(<eps zeta>^(-K))
prop:np-10-65-a	paper/reader/proofs/P-G1.md@PIN:368-512	proof G1, the calculi	replaces NP 10.65 (a); (a)-(j) proved
eq:iv5-calc-ell	paper/reader/proofs/P-G1.md@PIN:400	proof G1, elliptic estimate	new display
lem:iv5-calc-garding	paper/reader/proofs/P-G1.md@PIN:514-541	proof G1, margin bound	replaces the sharp Gårding step
eq:iv5-calc-garding	paper/reader/proofs/P-G1.md@PIN:518	proof G1, margin bound	new display
lem:iv5-calc-q0	paper/reader/proofs/P-G1.md@PIN:546-571	proof G1, bound for Q_0	replaces Q_0 = Theta*Theta + R
eq:iv5-calc-q0	paper/reader/proofs/P-G1.md@PIN:551	proof G1, bound for Q_0	new display
```

Notes to append to existing rows, each after "; " (or as the note, where the note is empty):

```text
def:iv5-0-1	G1: the calculus is that of sec:iv5-calc; the spaces on Omega defined in lem:iv5-calc-dual (C33-1, C33-2)
prop:iv5-1-2	G1: proof by prop:np-10-65-a (e) with the cut-offs (C33-5)
prop:iv5-1-3	G1: regulariser lem:iv5-calc-reg; commutant, (5.26), absorption by prop:np-10-65-a (C33-6 to C33-9)
prop:iv5-2-1	G1: (5.44) by lem:iv5-calc-q0, (5.45) by lem:iv5-calc-garding, 9C_2 + 2 for 2C (C33-10 to C33-12)
prop:iv5-3-1	G1: Q-terms with the weight rho_sf (C33-13)
prop:iv5-4-1	G1: weighted Q-terms of prop:iv5-3-1 (C33-14)
prop:iv5-5-2	G1: Q-terms by lem:iv5-calc-q0 and lem:iv5-calc-garding (C33-15)
prop:iv5-7-1	G1: strong sense at fibre infinity by the regularisation in prop:iv5-1-3 (C33-16)
thm:iv5-7-3	G1: duality of the supported and extendible spaces, uniform in h, by lem:iv5-calc-dual (C33-17)
lem:iv5-8-1	G1: uniformity in b by prop:np-10-65-a (j) (C33-18)
sec:iv6-2	G1: eb-structure of def:iv5-calc-cells, calculus by prop:np-10-65-a (i) (C33-19)
thm:iv6-2-1	G1: Q-terms at the cone face by lem:iv5-calc-q0 and lem:iv5-calc-garding (C33-20)
```
