## The model at a base point near b₀ {#ch:s25a}

The linear theory of [[ch:s19]] is written at the base point b₀ = (m₀, 0), and in the chapters that follow it is written
at a base point whose black hole parameter b lies in a fixed neighbourhood ℬ_* of b₀. This chapter collects what that
requires, using only [[ch:s11]]–[[ch:s19]]: the statement at b of a result proved at b₀ ([[def:s25-at-b]]); the model
objects at b, with bounds uniform in b ([[lem:iii-i15-1-1]]): the forward solutions, the ι⁺- and tf-normal operators and
the indicial roots, which do not depend on b, the zero energy states, towers and physical states at b, real and smooth in
b and equivariant under the antipodal map, the augmented low-energy theory, and the Killing time translation; the
rotation state at b ([[rem:iii-i15-1-2]]); and the results of [[ch:s19]] on null infinity and the almost linear bounds at
b, with constants uniform in b ([[prop:iii-i2-5-1-b]]). [Hin26] states its Sections 11.2–12 at base points with |b − b₀|
small; the results here are part of that statement in dimension 4 + 1.

*What changes in dimension 4 + 1.* At b₀ every rotation is Killing, and the rotation state h_(b₀,v1) vanishes. At a
rotating b only the rotations commuting with the spin are Killing, and h_(b,v1) is O(|b − b₀|) but not zero
([[sec:iii-e1-2]]). [[rem:iii-i15-1-2]] identifies it: h_(b,v1)(V) is the gauge-corrected linearised metric ġ_b(ḃ_V)
of a change ḃ_V of the black hole parameter, of size O(|b − b₀||V|); the boost part vanishes by the parity of the
states under x ↦ −x.

*Notation.* The notation is that of [[ch:s11]]–[[ch:s19]]. The black hole parameters are b = (m, A), with tangent space
𝔟 = ℝ ⊕ 𝔰𝔬(4), b₀ = (m₀, 0) and R₁ = m₀^(1/2), and |b − b₀| is the norm of [[def:s12-radii]]. We write ℬ_1 and ℬ_* for
the neighbourhoods B_1 and B_* of b₀ fixed in [[sec:iii-h2-0]], ℬ̄_* ⊂ ℬ_1. Shrinking ℬ_*, we take it to be an open ball
about b₀. It is shrunk finitely many times, here and in the chapters that follow, each time to a smaller ball about b₀,
and every statement holds on the final ℬ_*. Here it is shrunk once, in [[lem:s25a-ball]], to radius at most 1/(2C_B), so
that the matrix B(b) of the rows [[eq:iii-h-3-1]] on the states satisfies |B(b)⁻¹| ≤ 2 on ℬ̄_*. The letter ε > 0 is
small. For the zero energy operator of the gauge potential operator we write P_b := (□^Υ_b)^(0) ([[sec:iii-d2-1]]), as in
[[ch:s13]]; L̂_b(0) is the zero energy operator of L_b, L̃_b(0) its augmentation ([[prop:iii-h-3-2]]), and the states
ġ_b(ḃ), h_b(S) = h_(b,s1)(S), h̆_b(S) and h_(b,v1)(V) are those of [[sec:iii-h-1]], [[prop:iii-d2-3-1]] and
[[prop:iii-f3-2-2]]; ġ_b(ḃ) is the gauge-corrected state ġ^Υ_b(ḃ) of [[eq:iii-f3-2-1]].

*The inner radius.* Every result of the chapter holds with the inner radius r₀ = r_♭ ∈ (0, ½R₁] of [[def:s12-radii]]
as a parameter, with constants and neighbourhoods of b₀ that may depend on it. The chapter names no inner radius and
no fixed radius. It works on Ω_* = cl_M{t^♭_* ≥ 1} with the spaces of [[ch:s04]]–[[ch:s10]], extendible at the inner
boundary, and with the results of [[ch:s04]]–[[ch:s19]], which hold at every such r_♭. The neighbourhoods ℬ_1 and ℬ_*
are those chosen in [[sec:iii-h2-0]] for the given r_♭.

**Definition {#def:s25-at-b}** (Base points and the statement at b.) A *base point with black hole parameter b* is a
background of the linear theory, in the chapters that follow, that equals g_b near K⁺; for a pair (h, S), with
h ∈ 𝒳^∞ small and S ∈ 𝒮_1 small, b is the black hole parameter of its background g_(b₀,b,−S) of [[eq:iii-i-1-1]]. For
a statement of the linear theory made at the base points with parameter b₀, *the statement at b* is obtained as
follows: L_(b₀), g_(b₀) near K⁺, the states, towers and companions at b₀, and the index set ℰ_ind are replaced by those
at b; and derivatives in b are taken at b. At a rotating b the v1 terms of exponent of real part at most 2 need more
than this substitution; they are treated with the rotation rows.

### The model at b {#sec:iii-i15-1}

**Lemma {#lem:iii-i15-1-1}** (The model objects at b.) For b ∈ ℬ̄_*, uniformly in b:

(P1) [[thm:iii-i-5-3]] holds at b, with continuity in (b, S, h) ([[cor:iii-h2-5-1]]), and so do [[prop:iii-i-3-3]],
[[prop:iii-i-3-4]], [[prop:iii-i-4-1]], [[cor:iii-i-4-2]], [[cor:iii-i-5-2]], [[lem:iii-i-3-2]] and [[lem:iii-i-3-6]],
which are stated for g_0 = g_(b₀,b,−S) of [[eq:iii-i-1-1]] with |b − b₀| small.

(P2) N_ι⁺(2L_b) = N_ι⁺(2L̄) ([[lem:iii-h2-3-2]]), so the boundary spectrum spec_ι⁺ ([[def:iii-g1-4-1]]),
[[thm:iii-g1-3-1]] and the resonant states of [[sec:iii-g3-3]] do not depend on b; [[thm:iii-g2-4-2]] and
[[cor:iii-g2-4-3]] are stated for general b (with the K⁺-towers of L_b); the tf-normal operator does not depend on b
([[lem:iii-g4-1-1]]); and the indicial roots of [[prop:iii-f1-2-3]] do not depend on b, the normal operator of L̂_b(0)
at ∂X being that of 2L̄ ([[lem:iii-f-2-1]] (3)).

(P3) The zero energy states of L_b listed in [[sec:iii-g2-1]] and their companions, the 1-form towers of
[[prop:iii-d3-3-1]], the physical states of [[prop:iii-f4-5-1]] and ġ_b are chosen real and smooth in b, equal at b₀ to
those at b₀, with index sets in (μ − j) + ℰ_ind, ℰ_ind independent of b, and, except for ġ_b, with leading terms at ∂X
that do not depend on b. The leading terms of ġ_b may depend on b through the mass, and the linear theory uses the index
sets of ġ_b and its smoothness in b. The rotation state h_(b,v1) ∈ 𝒜³ is smooth in b and vanishes at b₀. The element −1
of SO(4), x ↦ −x on the spatial factor, is an isometry of every g_b: it commutes with the spin matrix, and the metric
[[eq:iii-b-3-2]] is even in x ([[lem:iii-e1-2-1]] with O = −1). It preserves t_* = t − ψ(|x|) ([[eq:iii-b-3-6]]), the
radial functions ψ, ζ_∞ and χ, and the gauge 1-forms c_Υ = ζ_∞(|x|)|x|⁻¹dt and c_(Υ,H) = −½χ(|x|)d|x| of [[sec:iii-d2-1]]
and c_C of [[sec:iv4-0]], a combination of dt and d|x| with coefficients that depend on |x| only. So it commutes with
L_b, □^Υ_b, P_b and L̂_b(0). The states are equivariant under it: h_b(S) is odd, ġ_b(ḃ) and h_(b,v1)(V) are even.

(P4) [[cor:iii-h-4-2]]–[[cor:iii-h-4-4]] and [[thm:iii-h1-1-3]] hold at b ([[thm:iii-h2-2-1]] and the compactness
argument of its proof), and so do the other statements of [[ch:s18]] that the linear theory uses: [[def:iii-h-2-1]],
[[def:iii-h-3-1]], [[lem:iii-h-2-3]]–[[lem:iii-h-2-5]], [[prop:iii-h-3-2]] and [[thm:iii-h-4-1]], which are stated for
b near b₀, and [[lem:iii-h1-2-1]], [[eq:iii-h1-4-1]]–[[eq:iii-h1-5-2]] and [[sec:iii-h1-5]]. [[thm:iii-h2-2-1]] reruns
[[sec:iii-h1-2]]–[[sec:iii-h1-7]] at b, and its compactness argument covers [[prop:iii-h-3-2]]. The states' bounds are
uniform in 𝒜^(q−δ) for every δ > 0 ([[rem:iii-h-2-6]]), a loss that the linear theory absorbs, each of its results
using its weights with room. The high-frequency loss is bounded at every order k at every b ∈ ℬ̄_1, with constants
independent of b: [[prop:iii-h2-1-1]] holds with C independent of η and b, and [[cor:iii-h2-1-2]] gives, for every k,
δ_Γ(0) < 1/(2(k + 1)) at every b ∈ ℬ̄_1. The propositions of [[ch:s17]] on the tf-normal operator and
[[lem:iii-g4-4-3]] hold at b, their inputs being the tf-normal operator (P2), the zero energy states (P3) and
[[ch:s18]].

(P5) The time translation ∂_(t_*) is Killing for g_b, so every statement that uses only that the s0 gauge 1-form
ω^(0)_(b,s0) is Killing holds at b.

*Proof.* (P1), (P2) and (P4) are the cited statements. (P5): g_b is stationary.

*The choice in (P3).* The pure gauge states and their companions are δ*_(g_b)ω^(≤k)_b with ω^(≤k)_b ∈ ker □^Υ_b
polynomial in t_* and smooth in b ([[prop:iii-d3-3-1]]). By the remark closing [[lem:iii-d3-2-1]] their leading terms
at ∂X are the Minkowski model solutions, which do not depend on b and which (R4) of [[sec:iii-d3-1]] fixes uniquely, no
root lying at μ − k. The physical states at −2 are those of [[prop:iii-f4-5-1]], smooth in b with the b-independent
leading term h̄_τ(Y). Composing each family with the inverse of the smooth invertible map Y ↦ (its leading
coefficient), normalised to be the identity at b₀, keeps everything at b₀ and makes the leading terms independent of
b. The corrections lie in 𝒜^((μ−j)+ℰ_ind) with ℰ_ind independent of b ([[sec:iii-g2-2]], [[prop:iii-d3-3-1]],
[[prop:iii-f4-5-1]]). The rotation state h_(b,v1)(V) = δ*_(g_b)ω^(−1)_(b,v1)(V) lies in 𝒜³ ([[eq:iii-d2-3-4]]), is
smooth in b, and vanishes at b₀, where every rotation is Killing ([[prop:iii-d2-3-1]] (3)). ġ_b = ġ^Υ_b is the
gauge-corrected derivative of the Myers–Perry family ([[prop:iii-f3-2-2]]), smooth in b; its leading term may depend on
b through the mass.

*Reality.* The reality in (P3) holds as at b₀: L_b, δ*_(g_b) and □_(g_b) are real, and [[prop:iii-d2-3-1]],
[[prop:iii-d3-3-1]], [[prop:iii-f4-5-1]] and the normalisation by the leading coefficients are real constructions.

*Parity.* The parity in (P3) follows from the constructions of the states. Write φ for the pullback by −1. P_b is
invertible on the b-spaces of decaying sections of [[sec:iii-d2-1]] (weights in the gap (0, ι^Υ_(s1,2))), which φ
preserves. Since φ commutes with P_b, it commutes with P_b⁻¹ there, and it commutes with δ*_(g_b).
[[prop:iii-d2-3-1]] builds

    ω_(b,s1)(S) = ω̄_s1(S) − P_b⁻¹□^Υ_b ω̄_s1(S)

from the Minkowski translation 1-form ω̄_s1(S), which is odd, and

    ω_(b,v1)(V) = V − P_b⁻¹□^Υ_b V

from the rotation 1-form V, which is even (the proof of [[prop:iii-d2-3-1]]). So ω_(b,s1)(S) and
h_b(S) = δ*_(g_b)ω_(b,s1)(S) are odd, and ω_(b,v1)(V) and h_(b,v1)(V) = δ*_(g_b)ω_(b,v1)(V) are even. φ fixes g_(b′)
for every b′, so ∂_b g_b(ḃ) is even; so are

    η_b(ḃ) = 2δ_(g_b,E_Υ)G_(g_b)∂_b g_b(ḃ)     and     ω̇_b(ḃ) = −P_b⁻¹η_b(ḃ),

and so is ġ_b(ḃ) = ġ^Υ_b(ḃ) = ∂_b g_b(ḃ) + δ*_(g_b)ω̇_b(ḃ), the gauge-corrected state of [[eq:iii-f3-2-1]]
([[prop:iii-f3-2-2]]), which is what ġ_b means here, as in the basis of [[sec:iii-h-1]]. The reparametrisation by the
leading coefficients in the choice above is linear in the parameter and keeps each family's parity. ∎

**Lemma {#lem:s25a-ball}** (The ball ℬ_*.) Fix the bases of 𝔟 and 𝒮_1 in which [[eq:iii-h-3-1]] is written, with the
Euclidean norms in these bases and the operator norm on matrices, and for b ∈ ℬ̄_* let

    B(b)(ḃ, S) := (⟨ġ_b(ḃ) + h_b(S), f*_1⟩, ⟨ġ_b(ḃ) + h_b(S), f*_2⟩),

with the rows f*_1, f*_2 of [[eq:iii-h-3-1]] and the pairing of [[sec:iii-h-1]] at b. Then B(b₀) = I and B is of class
C¹ in b, so C_B := sup_(ℬ̄_*)|∂_bB| is finite. After shrinking ℬ_* to a ball about b₀ of radius at most 1/(2C_B),

    |B(b) − I| ≤ ½,     |B(b)⁻¹| ≤ 2     for every b ∈ ℬ̄_*.

In particular (ḃ, S) ↦ ġ_b(ḃ) + h_b(S) is injective for every b ∈ ℬ̄_*.

*Proof.* B(b₀) = I is [[eq:iii-h-3-1]]. The pairing ⟨u, f*_j⟩ = ∫_X ⟨u, f*_j⟩_(g_b)|dx| is an integral over the
compact set supp f*_1 ∪ supp f*_2 ⊂ X°, and g_b is smooth in b. The states are of class C¹ in b with values in
continuous sections over that set ((P3); [[prop:iii-d2-3-1]] and [[prop:iii-f3-2-2]] (3) construct them smooth in b).
So B is of class C¹, and C_B is finite, ℬ̄_* being compact. Shrinking ℬ_* does not increase C_B. The mean value theorem
along the segment from b₀ to b, which lies in the ball ℬ̄_*, gives |B(b) − I| ≤ C_B|b − b₀| ≤ ½, and the Neumann series
B(b)⁻¹ = Σ_(n≥0)(I − B(b))^n gives |B(b)⁻¹| ≤ Σ_(n≥0) 2^(−n) = 2. If ġ_b(ḃ) + h_b(S) = 0, then B(b)(ḃ, S) = 0, so
(ḃ, S) = 0. ∎

**Lemma {#rem:iii-i15-1-2}** (The rotation state at b.) For b ∈ ℬ̄_* and V ∈ 𝒱_1 there is ḃ_V ∈ 𝔟, linear in V,
with |ḃ_V| = O(|b − b₀||V|) and

    h_(b,v1)(V) = ġ_b(ḃ_V),     ker h_(b,v1) = {V : ḃ_V = 0}.

*Proof.* At b, h_(b,v1)(V) is δ*_(g_b) of a 1-form in ker □^Υ_b ([[eq:iii-d2-3-4]]), so it lies in ker L̂_b(0) in the
space 𝒳_0 of [[sec:iii-h-1]], and it is O(|b − b₀||V|) (P3). Near b₀ that nullspace has the dimension it has at b₀, with
the continuous basis ġ_b(ḃ), the gauge-corrected state of [[eq:iii-f3-2-1]], and h_b(S) (the proof of [[prop:iii-h-3-2]],
with [[lem:s25a-ball]]). So h_(b,v1)(V) = ġ_b(ḃ_V) + h_b(S_V), with
(ḃ_V, S_V) = B(b)⁻¹(⟨h_(b,v1)(V), f*_1⟩, ⟨h_(b,v1)(V), f*_2⟩); as |B(b)⁻¹| ≤ 2 and the pairings are bounded by the
supremum of h_(b,v1)(V) on the compact support of the rows, |ḃ_V| + |S_V| = O(|b − b₀||V|). Moreover S_V = 0: the pullback by −1 fixes h_(b,v1)(V) and ġ_b(ḃ_V) and
reverses h_b(S_V) ((P3)), so h_b(S_V) = 0, and S_V = 0 by [[lem:s25a-ball]]. So h_(b,v1)(V) = ġ_b(ḃ_V), and
ker h_(b,v1) = {V : ḃ_V = 0} by the injectivity in [[lem:s25a-ball]]. ∎

### Null infinity and the almost linear bounds at b {#sec:s25a-s19-at-b}

**Proposition {#prop:iii-i2-5-1-b}** (Null infinity and the almost linear bounds at b.) Let b ∈ ℬ̄_*, let L_b be the
operator at b, and put g_0 := g_(b₀,b,−S), g := g_0 + h and L := L^(g,g_0), with |S| < ε_0, h ∈ 𝒳^∞ and ‖h‖_(𝒳^d) < ε_0,
where ε_0 and d are those of [[cor:iii-h2-5-1]], independent of b. Then [[lem:iii-i1-1-1]], [[prop:iii-i1-2-1]],
[[lem:iii-i1-2-2]], [[prop:iii-i1-3-1]], [[lem:iii-i2-2-1]], [[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]]
and [[prop:iii-i2-5-1]] hold with these L_b, g_0, g and L, and with the states ġ_b(ḃ), h_b(S), h̆_b(S) at b in place of
those at b₀, with constants and smallness conditions uniform in b ∈ ℬ̄_*. In particular, for ℓ_I with [[eq:iii-i2-5-1]],
α_K ∈ [½, 1), α_+ > α_K, β_+ < min(α_+, 3/2, min Re ℰ_+) and f as in [[prop:iii-i2-5-1]], the forward solution u of
Lu = f lies in the space [[eq:iii-i2-5-2]]; and, at fixed b, u depends continuously on (S, h) in that space with every
weight lowered by ς, for every ς > 0.

*Proof.* The results on null infinity are stated for L = L^(g,g_0) with g_0 = g_(b₀,b,−S) ([[sec:iii-i1-1]]), with
[[prop:iii-i-3-3]] and [[prop:iii-i-3-4]] for general b ((P1)). The structure of L_b at ℐ⁺ is [[lem:iii-i-3-2]], which is
stated for L_b at every b, and S̄ and Ā do not depend on b ((P2), [[lem:iii-h2-3-2]]). The index sets ℰ^C_I, ℰ_+ and
ℰ^tot_I at ℐ⁺ and ι⁺ are data of the classes of [[def:iii-i-1-1]], fixed independently of b. So
[[lem:iii-i1-1-1]]–[[prop:iii-i1-3-1]] hold at b, uniformly.

For the almost linear bounds, the steps of [[sec:iii-i2-1]]–[[sec:iii-i2-5]] that use b₀ are supplied as follows.

- *The setting.* ε_0 and d are uniform in b ((P1)). X = {r ≥ r_0} is the same at every b, and [[thm:iii-h2-2-1]] runs
  the second result of [[ch:s18]] on it for b ∈ ℬ̄_1 ((P4)). L̂_b(σ) is invertible for real σ ≠ 0
  ([[cor:iii-h-4-4]]) and L̃_b(σ) for 0 < |σ| ≤ c_k ([[cor:iii-h-4-2]]), with c_k uniform ((P4)). No indicial root of
  L̂_b(0) has real part in (0, 1] ((P2)), so the window (0, 1) is the same at every b.
- [[lem:iii-i2-2-1]] and [[lem:iii-i2-3-1]] use no property of the base point. In [[sec:iii-i2-4]] the constants
  c ≤ c_k′ of [[cor:iii-h-4-2]] and c_(j,k′) of [[thm:iii-h-4-1]] (3) are those at b, uniform by (P4).
- *The three frequency ranges.* The Fourier transform in t_* uses only that g_b is stationary. The splitting
  u = u_hi + u_reg + u_sing of [[lem:iii-h1-2-1]] and [[eq:iii-h1-4-1]]–[[eq:iii-h1-5-2]], with u_sing = ġ + h_s1,
  holds at b ((P4): [[thm:iii-h2-2-1]] reruns [[sec:iii-h1-2]]–[[sec:iii-h1-7]] at b), with ġ = ġ_b and
  h_s1 = h_(b,s1) the states at b ((P3), the derivative in b being taken at b). The forward map is continuous
  ([[thm:iii-i-5-3]] at b, (P1)). [[lem:iii-i2-4-1]] and [[lem:iii-i2-4-2]] use [[cor:ii-g1-4-5]] with the hypotheses of
  [[ch:s02]] for 2L_b, which hold at b by (P4) ([[thm:iii-h2-2-1]]), and S̄ = 0, which does not depend on b ((P2),
  [[lem:iii-h2-3-2]]); [[lem:iii-i2-4-2]] uses [[cor:iii-h-4-2]] and [[thm:iii-h-4-1]] (3) for L̃_b ((P4)). In
  [[lem:iii-i2-4-3]], ġ_b(ḃ) ∈ 𝒜² (in the mass) and 𝒜³ (in the rotation), h_b(S) ∈ 𝒜³ and h̆_b(S) ∈ 𝒜², and the map
  Ψ of [[lem:iii-h-2-5]], are those at b ((P3)), the leading terms not depending on b; uniformly in b,
  [[rem:iii-h-2-6]] gives these memberships in 𝒜^(q−δ), and the loss δ < ε is absorbed by the ε of [[eq:iii-i2-4-3]].
- [[prop:iii-i2-5-1]]. Its start is [[thm:iii-i-5-3]] at b ((P1)). The K⁺-gain of (L − L_b)u in [[eq:iii-i-4-2]] holds
  with L_b the base point's operator, as g_0 = g_b near K⁺ ([[lem:iii-i-3-6]]). [[prop:iii-i1-3-1]] for L_b and
  [[prop:ii-e-3-4]] hold at every b. The holomorphy of F(v), with at most a pole at 0, is [[sec:iii-h1-5]] at b
  ((P4)). The continuity in (S, h) is that of (P1) at fixed b.

Each supply is uniform on ℬ̄_*, which gives the uniform constants. ∎
