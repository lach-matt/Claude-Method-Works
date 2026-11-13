## Base points near b₀ {#ch:s25}

This chapter proves that the linear theory of [[ch:s19]]–[[ch:s24]] holds at every base point whose black hole
parameter b lies in a fixed neighbourhood ℬ_* of b₀ = (m₀, 0), with constants and smallness conditions uniform in b
([[thm:iii-i15-3-1]]). That theory consists of the forward solutions in the cone and their improvement at ι⁺ and K⁺,
the boost parameter, almost boundedness, the extraction and the elimination of the parameters, the centre-of-mass
motions, the corrections of the fourth kind, the expansion at the Kerr face, the augmentation by its coefficients,
the parameterisation by data, the tame estimates and the exact weights. With it, the right inverses that the
Nash–Moser theorem [[thm:ii-g-2-1]] asks for exist at every base point near the one of the iteration, with uniform
bounds ([[cor:iii-i15-3-2]]). [Hin26] states its Sections 11.2–12 at base points with |b − b₀| small; Theorem
[[thm:iii-i15-3-1]] is that statement in dimension 4 + 1, and the lemmas and propositions that prove it are new in
this dimension.

Three ingredients are proved for this. [[sec:iii-i15-1]] collects the model objects at b ([[lem:iii-i15-1-1]]): the
forward solutions; the ι⁺- and tf-normal operators and the indicial roots, which do not depend on b; the zero energy
states, towers and physical states at b, real and smooth in b and equivariant under the antipodal map; the augmented
low-energy theory; the Killing time translation; and the identity [[eq:iii-i15-1-1]], which compares the rows built at
b with the corrections built at b₀. It proves the joint injectivity of the states at b by perturbation from b₀
([[lem:iii-i15-1-2]]), and it identifies the rotation state at b as a change of the black hole parameter alone
([[rem:iii-i15-1-2]]). [[sec:iii-i15-2]] treats the rotation terms: the v1 terms of exponent of real part at most 2
are rotation rows whose coefficients are assigned from the construction that produces them ([[prop:iii-i15-2-2]],
[[def:iii-i15-2-3]]), and with them the decay theorem [[thm:iii-i14-3-1]] holds at b ([[prop:iii-i15-2-5]]).
[[sec:iii-i15-3]] states the theorem and gives, for every step of the theory whose justification uses a property of b₀
that a general b need not have, what supplies it at b. Three such steps need more than a substitution: the boost
identity, the parameter identities and the expansion at a rotating b. They are proved at b, with direct bounds in
place of continuity in b, in [[lem:iii-i15-2-7]] and [[prop:iii-i15-2-8]] ([[ch:s20]]), [[lem:iii-i15-2-11]] and
[[prop:iii-i15-2-12]] ([[ch:s21]]), and [[lem:iii-i15-2-9]] and [[cor:iii-i15-2-10]] ([[ch:s22]]).

*What changes in dimension 4 + 1.* At b₀ every rotation is Killing. At a rotating b only the rotations commuting with
the spin are, and the rotation state h_(b,v1) is O(|b − b₀|) but not zero ([[sec:iii-e1-2]]). The v1 terms of
exponent of real part at most 2 then decay at K⁺ one order less than at b₀, below the levels' target α − 2. An
elimination through their K⁺-coefficients would invert V ↦ h_(b,v1)(V), a map that degenerates as b → b₀. As in
[Hin26, pp. 279–280] ("for a suitable V^(1,0)′ ≈ V̇"), they are assigned directly: the coefficient of the rotation row
is read from the construction that produced the term, the ι⁺-data of the graft or the tf-data of the spectral pieces.
No K⁺-coefficient is inverted ([[prop:iii-i15-2-2]]). The rotation rows of [[def:iii-i14-1-3]], whose coefficient
space is all of 𝒱_1, are what makes this possible, and they are introduced there for the same reason. The rest
transfers by continuity in b, and the joint injectivity of the states, proved at b₀ by spherical symmetry, transfers by
perturbation ([[lem:iii-i15-1-2]]).

*Notation.* The notation is that of [[ch:s19]]–[[ch:s24]]. The black hole parameters are b = (m, A), b₀ = (m₀, 0) and
R₁ = m₀^(1/2), and |b − b₀| is the norm of [[def:s12-radii]]. ℬ_1 and ℬ_*, with ℬ̄_* ⊂ ℬ_1, are the neighbourhoods
of b₀ of [[sec:iii-h2-0]]; ℬ_* is shrunk in [[lem:iii-i15-1-2]] and [[prop:iii-i15-2-5]] (and in [[prop:iii-i15-2-8]]
and [[prop:iii-i15-2-12]]), and every statement below holds on the final ℬ_*. As in [[ch:s16]], λ ∈ ℂ is an exponent
at ι⁺; it is not the wavelength. The letter ϵ > 0 is small, and "order w−" means order w − ϵ for every ϵ > 0
([[sec:iii-i14-1]]). The types 𝒯 = {s1, v1, s0, s2, c0, c1}, the rows ν = (τ, λ, k) with their K⁺-exponents e_ν and
weights κ_ν, the index set 𝒩 = 𝒩_ι ⊔ 𝒩_σ, the coefficient spaces 𝒲_(τ,ℂ), the parameter space 𝒫, the operator P_4 and
the classes of sources 𝒴_2(α), 𝒴(α) are those of [[sec:iii-i9-1]] and [[sec:iii-i9-2]] (with (G) and the levels of
[[ch:s22]]); ℳ, ℰ_(++), λ_♯ and the class 𝒴(α_1) of the levels below 3 are those of [[sec:iii-i8-1]]; ℰ_♯, ℰ^♮,
𝒴^♮_2(β), 𝒴^♮(β) and the spaces 𝒵_β are those of [[ch:s22]] ([[def:iii-i13-1-2]]); 𝒬, h_(b,rem), P_5, R_q, Δ_q,
𝒩_rot and ℳ_rot are those of [[def:iii-i14-1-1]]–[[def:iii-i14-1-3]]. The corrections of the first to fourth kinds
are those of [[def:iii-i4-2-1]], [[def:iii-i7-2-1]], [[def:iii-i8-2-1]] and [[def:iii-i9-2-1]], with their
counterterms ϑ_(ν,♯). For the zero energy operator of the gauge potential operator we write P_b := (□^Υ_b)^(0)
([[sec:iii-d2-1]]); L̂_b(0) is the zero energy operator of L_b, L̃_b(0) its augmentation ([[prop:iii-h-3-2]]), and the
states ġ_b(ḃ), h_b(S) = h_(b,s1)(S), h̆_b(S) and h_(b,v1)(V) are those of [[sec:iii-h-1]], [[prop:iii-d2-3-1]] and
[[prop:iii-f3-2-2]].

*The inner radius.* Every result of the chapter holds with the inner radius r₀ = r_♭ ∈ (0, ½R₁] of [[def:s12-radii]]
as a parameter, with constants and neighbourhoods of b₀ that may depend on it. The chapter names no inner radius. It
works on Ω_* = cl_M{t^♭_* ≥ 1} with the spaces of [[ch:s04]]–[[ch:s10]], extendible at the inner boundary, and with
the results of [[ch:s04]]–[[ch:s24]], which hold at every such r_♭; its fixed radii are scale-free ({r ≤ 2}, {r ≥ 1})
or far out, and its levels and weights are fixed by weights at infinity and at K⁺, not by the inner radius. The
neighbourhoods ℬ_1 and ℬ_* are those chosen in [[sec:iii-h2-0]] for the given r_♭.

**Definition {#def:s25-at-b}** (Base points and the statement at b.) A *base point* is a pair (h, p⃗) of
[[ch:s20]]–[[ch:s22]] (h ∈ 𝒳^∞ small, p⃗ ∈ 𝒫), a triple (h, p⃗, q) of [[ch:s23]] (q ∈ 𝒬), or a point U of the data space
of [[def:iii-j-1-1]]. Its *black hole parameter* is the b with p⃗_≤0 = (S, b − b₀, S^(0)_1), the component of p⃗ of
[[sec:iii-i7-1]], and for U that of Φ(U) ([[thm:iii-j-2-4]]). For a statement of the linear theory made at the base
points with parameter b₀, *the statement at b* is obtained as follows: L_(b₀), g_(b₀) near K⁺, the states, towers and
companions at b₀, and the index set ℰ_ind are replaced by those at b; derivatives in b are taken at b; and the v1 terms
are treated by [[sec:iii-i15-2]].

### The model at b {#sec:iii-i15-1}

**Lemma {#lem:iii-i15-1-1}** (The model objects at b.) For b ∈ ℬ̄_*, uniformly in b:

(P1) [[thm:iii-i-5-3]] holds at b, with continuity in (b, S, h) ([[cor:iii-h2-5-1]]), and so do [[prop:iii-i-3-3]],
[[prop:iii-i-3-4]], [[prop:iii-i-4-1]], [[cor:iii-i-4-2]], [[cor:iii-i-5-2]], [[lem:iii-i-3-2]] and [[lem:iii-i-3-6]],
which are stated for g_0 = g_(b₀,b,−S) of [[eq:iii-i-1-1]] with |b − b₀| small, and for the translated backgrounds
g_p⃗ of [[def:iii-i7-1-2]] at b, which the proof of [[cor:iii-h2-5-1]] covers with [[lem:iii-i7-1-3]] (a).

(P2) N_ι⁺(2L_b) = N_ι⁺(2L̄) ([[lem:iii-h2-3-2]]), so the boundary spectrum spec_ι⁺ ([[def:iii-g1-4-1]]),
[[thm:iii-g1-3-1]] and the resonant states of [[sec:iii-g3-3]] do not depend on b; [[thm:iii-g2-4-2]] and
[[cor:iii-g2-4-3]] are stated for general b (with the K⁺-towers of L_b); the tf-normal operator does not depend on b
([[lem:iii-g4-1-1]]); and the indicial roots of [[prop:iii-f1-2-3]] do not depend on b, the normal operator of L̂_b(0)
at ∂X being that of 2L̄ ([[lem:iii-f-2-1]] (3)).

(P3) The zero energy states of L_b listed in [[sec:iii-g2-1]], their companions, the 1-form towers of
[[prop:iii-d3-3-1]], the physical states of [[prop:iii-f4-5-1]] and ġ_b are real and smooth in b, with index sets in
(μ − j) + ℰ_ind, ℰ_ind independent of b, and, except for ġ_b, with leading terms at ∂X that do not depend on b. Those
of ġ_b may depend on b through the mass (as in the proof of [[lem:iii-i14-2-1]]), and only the index sets of ġ_b and
its smoothness in b are used. The rotation state h_(b,v1) ∈ 𝒜³ is smooth in b and vanishes at b₀
([[lem:iii-i14-2-1]]). The element −1 of SO(4), x ↦ −x on the spatial factor, is an isometry of every g_b: it commutes
with the spin matrix, and the metric [[eq:iii-b-3-2]] is even in x ([[lem:iii-e1-2-1]] with O = −1). It preserves
t_* = t − ψ(|x|) ([[eq:iii-b-3-6]]), the cut-offs and the gauge 1-forms c_Υ, c_(Υ,H) and c_C, which are
O(4)-invariant ([[lem:vii-3-1]]: c_Υ = ζ_∞(|x|)|x|⁻¹dt and c_(Υ,H) = −½χ(|x|)d|x| by [[sec:iii-d2-1]], and c_C, of
[[sec:iv4-0]], is a combination of dt and d|x| with coefficients that depend on |x| only). So it commutes with L_b,
□^Υ_b, P_b and L̂_b(0). The states are equivariant under it: h_b(S) is odd, ġ_b(ḃ) and h_(b,v1)(V) are even.

(P4) [[cor:iii-h-4-2]]–[[cor:iii-h-4-4]] and [[thm:iii-h1-1-3]] hold at b ([[thm:iii-h2-2-1]] and the compactness
argument of its proof), and so do the other statements of [[ch:s18]] that the linear theory uses: [[def:iii-h-2-1]],
[[def:iii-h-3-1]], [[lem:iii-h-2-3]]–[[lem:iii-h-2-5]], [[prop:iii-h-3-2]] and [[thm:iii-h-4-1]], which are stated for
b near b₀, and [[lem:iii-h1-2-1]], [[eq:iii-h1-4-1]]–[[eq:iii-h1-5-2]] and [[sec:iii-h1-5]]. [[thm:iii-h2-2-1]] reruns
[[sec:iii-h1-2]]–[[sec:iii-h1-7]] at b, and its compactness argument covers [[prop:iii-h-3-2]]. The states' bounds are
uniform in 𝒜^(q−δ) for every δ > 0 ([[rem:iii-h-2-6]]), a loss that the linear theory absorbs, each of its results
using its weights with room. [[prop:iii-h2-1-1]] bounds the high-frequency loss at every order k at every
b ∈ ℬ̄_1, with constants independent of b (by the argument of its proof). The propositions of [[ch:s17]] on the
tf-normal operator and [[lem:iii-g4-4-3]] (used in [[lem:iii-i6-1-4]]) hold at b, their inputs being the tf-normal
operator (P2), the zero energy states (P3) and [[ch:s18]].

(P5) The time translation ∂_(t_*) is Killing for g_b, so every statement that uses only that the s0 gauge 1-form
ω^(0)_(b,s0) is Killing (as [[sec:iii-i9-2]] and [[lem:iii-i10-2-1]] do) holds at b.

(P6) *Rows at b, corrections at b₀.* The rows and towers are built at the base point's b (the towers T_(ρ,b) of
[[def:iii-i14-1-2]], smooth in b by (P3)); the corrections of the first to fourth kinds and their counterterms are
the tensors built from b₀-objects, as [Hin26, p. 275, Definition 11.55] builds them; the operator of [Hin26,
Definition 11.56] is at b. At a base point (h, p⃗) with parameter b,

    D_p⃗P_4(h, p⃗)(W_ν = W) = L_(h,p⃗)m_ν(W) + r^ν_(h,p⃗)(W) + E^ν_(h,p⃗)(W).                          {#eq:iii-i15-1-1}

Here f^ν_b := L_(h,p⃗)m_ν + r^ν_(h,p⃗) is [[lem:iii-i9-2-6]] (c) at b, with every object (rows, corrections,
counterterms) built at b, in the classes of [[eq:iii-i9-2-5]] uniformly in b. And

    E^ν_(h,p⃗)(W) := L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W),

the difference between the corrections and counterterms built at b₀ and at b, lies in 𝒴^♮_2(α−) ∩ 𝒴(α_1), with norm
O(|b − b₀||W|). Its support is in supp χ_K, its K⁺-weight is κ_ν − ϵ > α, and its ι⁺-exponents below w_+ lie in
ℰ^♮ + 2 ([[def:iii-i13-1-2]]).

*Proof.* (P1)–(P4) are the cited statements. (P5): g_b is stationary. The reality in (P3) holds as at b₀: L_b,
δ*_(g_b) and □_(g_b) are real, and [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]], [[prop:iii-f4-5-1]] and the normalisation
of [[lem:iii-i14-2-1]] are real constructions. The parity in (P3) follows from the constructions of the states. Write
φ for the pullback by −1. P_b is invertible on the b-spaces of [[sec:iii-d2-1]] with weights in the gap (0, ι^Υ_(s1,2))
of decaying sections, which φ preserves. Since φ commutes with P_b, it commutes with P_b⁻¹ there, and it commutes with
δ*_(g_b). [[prop:iii-d2-3-1]] builds

    ω_(b,s1)(S) = ω̄_s1(S) − P_b⁻¹□^Υ_b ω̄_s1(S)

from the Minkowski translation 1-form ω̄_s1(S), which is odd, and

    ω_(b,v1)(V) = V − P_b⁻¹□^Υ_b V

from the rotation 1-form V, which is even (the proof of [[prop:iii-d2-3-1]]). So ω_(b,s1)(S) and
h_b(S) = δ*_(g_b)ω_(b,s1)(S) are odd, and ω_(b,v1)(V) and h_(b,v1)(V) = δ*_(g_b)ω_(b,v1)(V) are even. φ fixes g_(b′)
for every b′, so ∂_b g_b(ḃ) is even; so are

    η_b(ḃ) = 2δ_(g_b,E_Υ)G_(g_b)∂_b g_b(ḃ)     and     ω̇_b(ḃ) = −P_b⁻¹η_b(ḃ),

and so is ġ_b(ḃ) = ġ^Υ_b(ḃ) = ∂_b g_b(ḃ) + δ*_(g_b)ω̇_b(ḃ), the gauge-corrected state of [[eq:iii-f3-2-1]]
([[prop:iii-f3-2-2]]), which is what ġ_b means here, as in [[def:iii-i14-1-2]] and in the basis of [[sec:iii-h-1]].
The reparametrisation by the leading coefficients in the proof of [[lem:iii-i14-2-1]] is linear in the parameter and
keeps each family's parity.

(P6): f^ν_b is the expression of [[lem:iii-i9-2-6]] (c), derived at b. Its errors near K⁺ are L_(h,p⃗) − L_b,
which gains a_K there, as g_0 = g_b near K⁺ ([[lem:iii-i-3-6]]); its objects are smooth in b (P3), so the bounds are
uniform. For E^ν:

- The differences h^(b₀)_ν − h^b_ν and ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯) are b-differences of the 1-form towers and of their
  commutators with χ_K, so O(|b − b₀|) by (P3), and supported in supp χ_K.
- Near K⁺ the corrections vanish (they are supported in 𝒞), but the counterterms do not: there ϑ_(ν,♯) = ½□ω_ν
  ([[sec:iii-i9-2]]). Their difference has the K⁺-weight κ_ν of the tops of the towers ([[lem:iii-i9-2-2]] (a), (d),
  and (P3)). So E^ν has K⁺-weight κ_ν − ϵ > α.
- At ι⁺, the b-differences of the towers have exponents λ_ν + ℰ_ind (for v1 also λ_ν + 3; [[lem:iii-i14-2-1]]), with
  λ_ν the row's ι⁺-exponent in ℰ_par ∩ {Re ≤ 3} ⊂ ℰ_♯. L and δ* add 2 and increments, and the parts of L_(h,p⃗) − L_b
  from h and h_tot gain ρ_+^(λ_♯). So below w_+ the exponents lie in ℰ^♮ + 2 ([[def:iii-i13-1-2]]), with log orders
  bounded by [[lem:iii-i13-1-3]] (a), and above it the plain weight is Re λ + 2 + λ_♯ > w_+.
- So E^ν ∈ 𝒴^♮_2(α−), and E^ν ∈ 𝒴(α_1) as ℰ^♮ ∩ {Re < 2} ⊂ ℰ_(++) ([[lem:iii-i13-1-3]] (a)). ∎

**Remark {#rem:s25-rows-at-b}** (Rows at b and corrections at b₀.) [Hin26] makes the same choice: its corrections are
built at b₀, its operator is at b ([Hin26, Definition 11.56]), and the towers of its expansion are those of L_b
([Hin26, Theorem 11.59]). Rows built at b₀ would leave (L_b − L_(b₀))m^(b₀)_ν near K⁺, of K⁺-order only Re e_ν + 2.
Rows at b move the mismatch into the b-differences of the corrections and counterterms, which near K⁺ enter only
through the counterterms, at the weight κ_ν. The corrections of the first and second kinds are commutator terms in
supp dχ_K ([[def:iii-i4-2-1]], [[def:iii-i7-2-1]]), so f^S, f^b and f^(s1) vanish near K⁺, and their b₀/b mismatch lies
at ι⁺ only, with the gain ρ_+² of g_b − g_(b₀). For f^S of [[ch:s20]] that mismatch is the error E^S_b of
[[lem:iii-i15-2-7]], carried by [[prop:iii-i15-2-8]]; for f^S, f^b and f^(s1) of [[ch:s21]] it is the error E^mot_b of
[[lem:iii-i15-2-11]], carried by [[prop:iii-i15-2-12]]. The corrections of the third kind are not commutators, and
their counterterms do not vanish near K⁺ ([[lem:iii-i8-2-2]]); their rows (s1, λ, k) are rows of the set 𝒩 of
[[sec:iii-i9-1]] ([[def:iii-i9-2-1]]), so they enter through [[eq:iii-i15-1-1]]. At b₀, E^ν = 0 and
[[eq:iii-i15-1-1]] is the identity of [[lem:iii-i9-2-6]].

**Lemma {#lem:iii-i15-1-2}** (Joint injectivity at b.) Shrinking ℬ_*, [[lem:iii-i10-2-2]] and [[cor:iii-i10-2-3]] hold
at every b ∈ ℬ̄_*, for the states at b: if Σ_(τ≠v1) h_(b,τ)(W_τ) = 0 then every W_τ = 0; and a finite sum of rows
ν ≠ v1 at b with K⁺-weight above the largest of their rates vanishes. Moreover, there are a compact set 𝔎_0 ⊂ X° and
c > 0, independent of b, with sup_(𝔎_0)|Σ_τ h_(b,τ)(W_τ)| ≥ c Σ_τ |W_τ|.

*Proof.* The space 𝒲 := ⊕_(τ≠v1) 𝒲_(τ,ℂ) is finite-dimensional. At b₀ the map Θ_(b₀): W ↦ Σ_τ h_(b₀,τ)(W_τ) is
injective ([[lem:iii-i10-2-2]]). Each nonzero element of its range is a nonzero smooth tensor on X°, nonzero on an
open set, so by compactness of the unit sphere of 𝒲 there is a compact 𝔎_0 ⊂ X° on which
sup_(𝔎_0)|Θ_(b₀)W| ≥ 2c|W|. Θ_b depends continuously on b in C⁰(𝔎_0) (P3), so the bound with c holds for b near b₀.
The proof of [[cor:iii-i10-2-3]] uses only [[lem:iii-i10-2-2]] and [[lem:iii-i9-2-2]] (e), the K⁺-weight
Re e_ν + 1 − ϵ of m_ν(W) − χ_K r_ν h_τ(W), which follows from the tower relations alone and holds at b (P3). ∎

**Remark {#rem:iii-i15-1-2}** (The rotation state at b.) For b ∈ ℬ̄_* and V ∈ 𝒱_1 there is ḃ_V, linear in V, with
|ḃ_V| = O(|b − b₀||V|) and

    h_(b,v1)(V) = ġ_b(ḃ_V),     ker h_(b,v1) = {V : ḃ_V = 0}.

So v1 stays excluded from [[lem:iii-i15-1-2]] at b, as at b₀, and for a quantitative reason: a K⁺-extraction that read
a v1 coefficient beside the b- and S-coefficients would invert a map that degenerates as b → b₀. This is why the v1
coefficients are assigned in [[sec:iii-i15-2]], not read from the K⁺-expansion.

*Proof.* At b, h_(b,v1)(V) is δ*_(g_b) of a 1-form in ker □^Υ_b ([[eq:iii-d2-3-4]]), so it lies in ker L̂_b(0) in the
space 𝒳_0 of [[sec:iii-h-1]], and it is O(|b − b₀||V|) (P3). Near b₀ that nullspace has the dimension it has at b₀,
with the continuous basis ġ_b(ḃ), the gauge-corrected state of [[eq:iii-f3-2-1]], and h_b(S) (the proof of
[[prop:iii-h-3-2]]: the matrix B(b) of the rows [[eq:iii-h-3-1]] in these bases is
invertible). So h_(b,v1)(V) = ġ_b(ḃ_V) + h_b(S_V) with
|ḃ_V| + |S_V| = O(|b − b₀||V|). Moreover S_V = 0: the pullback by −1 fixes h_(b,v1)(V) and ġ_b(ḃ_V) and reverses
h_b(S_V) ((P3)), so h_b(S_V) = 0, and S_V = 0 by the injectivity of S ↦ h_b(S) ([[lem:iii-i15-1-2]]). So
h_(b,v1)(V) = ġ_b(ḃ_V), and ker h_(b,v1) = {V : ḃ_V = 0}, the ġ_b(ḃ) being part of a basis. ∎

### The rotation rows at b {#sec:iii-i15-2}

Let 𝒩_rot, ℳ_rot = ℰ_♯ ∩ {Re ≤ 2} and the rotation rows m_ν, ν = (rot, λ, k), be those of [[def:iii-i14-1-1]] and
[[def:iii-i14-1-3]], with the v1 tower T_(v1,b) at the base point's b:

    m_ν(W) = χ_K T_(v1,b)(a_ν W),     a_ν = t_*^(−λ)(log t_*)^k,     W ∈ 𝒱_(1,ℂ).

**Lemma {#lem:iii-i15-2-1}** (Rotation rows at b.) At b ∈ ℬ̄_*, m_ν(W) has K⁺-weight Re λ − ϵ (its bottom
a_ν h_(b,v1)(W), of size O(|b − b₀||W|)), and m_ν(W) − χ_K a_ν h_(b,v1)(W) has K⁺-weight Re λ + 1 − ϵ.
[[lem:iii-i9-2-2]] (a)–(e) and [[lem:iii-i9-2-4]]–[[lem:iii-i9-2-6]] hold for ν at b, with e_ν = λ and
κ_ν = Re λ + 4; in particular

    f^ν_(h,p⃗)(W) := D_p⃗P_4(h, p⃗)(W_ν = W) = f^ν_b(W) + E^ν_(h,p⃗)(W)

as in [[eq:iii-i15-1-1]], with f^ν_b(W) = L_(h,p⃗)m_ν(W) + r^ν_(h,p⃗)(W) ∈ 𝒴_2(α) uniformly in b, and
E^ν_(h,p⃗)(W) ∈ 𝒴^♮_2(α−) ∩ 𝒴(α_1) of size O(|b − b₀||W|).

*Proof.* As [[def:iii-i14-1-3]] states for b₀: the proofs of [[lem:iii-i9-2-2]] (a)–(e) and
[[lem:iii-i9-2-4]]–[[lem:iii-i9-2-6]] use the tower relations and not the coefficient space, and hold at b by (P3) and
(P6). The only change is the bottom, which at b₀ vanishes and at b is a_ν h_(b,v1)(W); it has K⁺-weight Re λ − ϵ and
is O(|b − b₀||W|) by (P3). The term L_(h,p⃗)m_ν(W) involves only the top of the tower, as T_(v1,b) solves L_b to its
length (the tower relations), so its K⁺-order is unchanged. ∎

**Proposition {#prop:iii-i15-2-2}** (The v1 terms are rotation rows with assigned coefficients.) Let b ∈ ℬ̄_* be the
black hole parameter of the base point.

(a) *The spacetime phase.* In [[prop:iii-i10-3-1]] at b, for each u-exponent λ₀ with Re λ₀ < 2 the graft's tower part
χ_K u^(j)_(b,0) ([[eq:iii-g2-4-3]] at b) equals

    Σ_(τ∈𝒯∖{v1}) m_((τ,λ₀,j))(W^(j)_τ) + m_((rot,λ₀,j))(V^(j))

up to K⁺-weight Re λ₀ + 1 − ϵ. Here V^(j) is the graft's v1 coefficient of t_*^(−λ₀)(log t_*)^j, read from the
ι⁺-data u_+ by [[thm:iii-g2-3-1]], in the normalisation of the rows of [[ch:s22]], in which a (log t_*)^j-term keeps
the prefactor of the term j = 0; for j = 0 it is −λ₀⁻¹V^(−1)_1, by a_v1 = −λ₀⁻¹t_*^(−λ₀) ([[eq:iii-g2-4-2]]). It is
linear and continuous in f, uniformly in b. (λ₀, j) ∈ ℳ ⊂ ℳ_rot, so the rotation row exists. So
[[prop:iii-i10-3-1]] (b) holds at b with the rows 𝒩_ι ⊔ 𝒩_(ι,rot), 𝒩_(ι,rot) the rotation rows (rot, λ₀, j) that
arise here, and these coefficients.

(b) *The spectral phase.* In [[prop:iii-i11-3-1]] at b, the v1 term c_v1(σ)T_(v1,b)(σ) of [[eq:iii-i11-2-2]]
([[lem:iii-i11-2-3]]) now has the bottom c_v1(σ)h_(b,v1)(Y), and its rate is α₀ (at b₀, α₀ + 1). At level 1
(2 ≤ Re α₀ < 2 + η_1) this is below α − 2 only for Re α₀ = 2 (by (G), no rate lies in (2, 2 + ϵ_K]). Those exponents
lie in ℰ_♯ ∩ {Re = 2} ⊂ ℳ_rot, and the term is, by [[lem:iii-i12-2-1]] (b), m_((rot,α₀,k))(Y′) up to K⁺-weight
Re α₀ + 1 − ϵ, with Y′ the coefficient that [[lem:iii-i11-2-3]] gives the v1 tower: Y times the constant of c_v1, read
from the tf-data. It is linear and continuous in the right-hand side, uniformly in b by (P2) and (P4). At level 2 the
v1 rate is α₀ + 1 ≥ 2 + η_1 > 2 + ϵ_K ≥ α − 2, as for the s0 and s2 towers there. So [[prop:iii-i11-3-1]] holds at b
with the rows 𝒩_σ ⊔ 𝒩_(σ,rot), 𝒩_(σ,rot) the rotation rows (rot, α₀, k) that arise here, and these coefficients.

(c) *No other v1 term.* Every v1 coefficient of the expansion has its exponents in ℰ_♯ ([[thm:iii-i12-3-1]], at b
[[cor:iii-i15-2-10]]: an ι⁺-exponent λ of u gives the coefficient t_*^(−λ+d_ρ), d_v1 = 0). So it either has real
part at most 2, and is one of (a)–(b), or real part above 2 + ϵ_K ≥ α − 2, and is carried by q ([[def:iii-i14-1-1]],
whose rates at a rotating b are Re z > 2 + ϵ_K).

*Proof.* (a) At b, [[thm:iii-g2-4-2]] gives the v1 term h^(≤2)_(b,v1)(a_v1 V^(−1)_1) of [[eq:iii-g2-4-3]], with
V^(−1)_1 from u_+, which does not depend on b ((P2): u_+ = N_ι⁺(λ)⁻¹(2f_+), and the decomposition of
[[thm:iii-g2-3-1]] is of u_+ on ι⁺). By [[eq:iii-g2-4-2]], a_v1 = −λ₀⁻¹t_*^(−λ₀), so
χ_K h^(≤2)_(b,v1)(a_v1 V) = m_((rot,λ₀,0))(−λ₀⁻¹V) up to the tower terms of order ≥ 3, of K⁺-weight
Re λ₀ + 3 − ϵ ([[def:iii-i14-1-3]], the rotation rows using h^(≤2) and the tower of [[sec:iii-i9-2]]). The other rows
are identified as in [[prop:iii-i10-3-1]] at b, by [[lem:iii-i10-2-1]] (c) at b (P3).

(b) The proof of [[lem:iii-i11-2-3]] at b is unchanged except that the v1 tower
T_(v1,b)(σ) = Σ_i (−iσ)^i h̆^i_(b,v1)(Y) has h̆^0_(b,v1) = h_(b,v1) ≠ 0. Its contribution with c_v1 is a piece of type
(b) of [[lem:iii-i12-2-1]], a tower with polyhomogeneous coefficient. Its rate is that of ℱ⁻¹(χc_v1), which at
level 1 is α₀ (the piece is σu_((α₀,k)), and c_v1 contributes |σ|^(α₀−1) to it). The level-2 count is that of
[[prop:iii-i11-3-1]], with the rate lowered by 1.

(c) As stated. ∎

**Definition {#def:iii-i15-2-3}** (The assigned rotation coordinates.) Let (h, p⃗) be a base point with parameter
b ∈ ℬ̄_*, and G ∈ 𝒴^♮(β), β > 3. The *assigned rotation coordinates* A_(b,ν)(G) ∈ 𝒱_(1,ℂ), ν ∈ 𝒩_rot, are the
coefficients of the rotation rows that [[prop:iii-i15-2-2]] (a)–(b) produces in the forward solution of
L_(h,p⃗)u = G: the graft's v1 coefficients at the exponents of ℳ (spacetime phase), and the spectral level-1
coefficients at the exponents of real part 2. They do not depend on β or on ϵ, and neither does E^ν ((P6)). A_b
commutes with complex conjugation: A_(b,ν̄)(Ḡ) is the complex conjugate of A_(b,ν)(G), as L_(h,p⃗) is real and the
objects of [[prop:iii-i15-2-2]] are real ((P3)). So for real G the tuple (A_(b,ν)(G))_ν is conjugation-symmetric, as
[[eq:iii-i15-2-2]] and [[def:iii-i14-1-3]] need. A_b := (A_(b,ν))_ν is linear and continuous on 𝒴^♮(β), uniformly in
b and in (h, p⃗) small ([[prop:iii-i15-2-2]], (P2), (P4)). No continuity in b is claimed or needed (Step 3 of the proof
of [[prop:iii-i15-2-5]]). A_(b₀) is defined at b₀ by the same formulas.

**Lemma {#lem:iii-i15-2-4}** ([[lem:iii-i13-2-2]] and [[lem:iii-i13-2-3]] at b.) Let β ∈ (3, 4 + ϵ_K] be admissible,
(h, p⃗) a base point with parameter b ∈ ℬ̄_* and h ∈ 𝒳^∞ small, G ∈ 𝒴^♮(β), and let the forward solution u of
L_(h,p⃗)u = G satisfy the hypothesis of [[lem:iii-i13-2-2]]. Then

    u = Σ_(ν∈𝒩_β) m_ν(S_ν) + Σ_(ν∈𝒩^(<β)_rot) m_ν(A_(b,ν)(G)) + ũ,
        𝒩^(<β)_rot := {ν ∈ 𝒩_rot : Re λ_ν < β − 2},                                                 {#eq:iii-i15-2-1}

with ũ in the class of [[eq:iii-i13-2-2]] and S_ν = S^(h,p⃗,β)_ν(G) determined by
u − Σ_(𝒩^(<β)_rot) m_ν(A_(b,ν)(G)), conjugation-symmetric, linear and continuous in G, uniformly. At a fixed b: if
(h_j, p⃗_j) → (0, p⃗_b), with p⃗_b the parameter whose only nonzero component is b − b₀, and G_j → G in 𝒴^♮(β), with
the hypothesis of [[lem:iii-i13-2-3]], then S^(h_j,p⃗_j,β)_ν(G_j) → S^(0,p⃗_b,β)_ν(G). At b₀ the second sum in
[[eq:iii-i15-2-1]] is absent (the rotation rows' rates there are Re λ + 1 > α − 2 ≥ β − 2), and [[eq:iii-i15-2-1]] is
[[eq:iii-i13-2-2]]. For β < 3 no rotation row has rate below β − 2 (Re λ − ϵ > 1, [[lem:iii-i15-2-1]]), and
[[lem:iii-i8-3-2]] holds at b as at b₀.

*Proof.* The proof of [[lem:iii-i13-2-2]] builds the expansion from the pieces of [[prop:iii-i10-3-1]] (the spacetime
phase), [[prop:iii-i11-3-1]] and [[thm:iii-i11-4-1]] (the spectral phase), [[thm:iii-i12-3-1]] (at b,
[[cor:iii-i15-2-10]]) and [[prop:iii-i13-2-1]], and reads the coefficients by [[cor:iii-i10-2-3]]. At b these hold
with the model objects at b ((P1)–(P6)), except the v1 pieces of exponent in ℳ_rot. By [[prop:iii-i15-2-2]] (a)–(c)
those are the rotation rows with the coefficients A_(b,ν)(G), up to K⁺-weight Re λ + 1 − ϵ > β − 2, which goes into
ũ. The rows other than v1 are then read from u − Σ m_ν(A_(b,ν)(G)), uniquely, by [[cor:iii-i10-2-3]] at b
([[lem:iii-i15-1-2]]). For the continuity at fixed b, the proof of [[lem:iii-i13-2-3]] runs with L_(0,p⃗_b) in place of
L_(b₀). Its remainder (L_(h_j,p⃗_j) − L_(0,p⃗_b))u_j gains a_K near K⁺, where both backgrounds equal g_b
([[lem:iii-i-3-6]]). Continuity across b is not claimed: the proofs perturb from a reference operator, and
L_b − L_(b₀) gains only 2 at K⁺. ∎

**Proposition {#prop:iii-i15-2-5}** ([[thm:iii-i14-3-1]] at b.) Let h ∈ 𝒳^∞, p⃗ ∈ 𝒫 with parameter b ∈ ℬ̄_*, and
q ∈ 𝒬 be small, and F ∈ 𝒴^♮(α−). For p⃗′ ∈ 𝒫, with motion components (S′, b′, S^(0)′_1) and row components W′_ν, let
u(p⃗′) be the forward solution of [[eq:iii-i14-3-1]], and (as in Step 2 of the proof of [[thm:iii-i14-3-1]], with
[[eq:iii-i15-1-1]])

    G′(p⃗′) := G̃ − f^S_(h,p⃗)(S′) − f^b_(h,p⃗)(b′) − f^(s1)_(h,p⃗)(S^(0)′_1)
              − Σ_(ν∈𝒩⊔𝒩_rot) (r^ν_(h,p⃗) + E^ν_(h,p⃗))(W′_ν),          G̃ := F − Δ_q(p⃗′) − R_q u(p⃗′).

There is a unique p⃗′ ∈ 𝒫 with

    W′_ν = A_(b,ν)(G′(p⃗′))     (ν ∈ 𝒩_rot)                                                         {#eq:iii-i15-2-2}

such that u(p⃗′) satisfies the conclusions of [[thm:iii-i14-3-1]]: [[eq:iii-i14-3-1]]–[[eq:iii-i14-3-2]], and
u = h_(b,rem)(q′) + h′ with q′ ∈ 𝒬. p⃗′, q′ and h′ are linear in F, with bounds uniform for (h, p⃗, q) small, b
included. At b₀, [[eq:iii-i15-2-2]] is the condition C^rot = 0 of Step 4′ of the proof of [[thm:iii-i14-3-1]], and p⃗′
is that of [[thm:iii-i14-3-1]].

*Proof.* *Steps 0–1* are those of the proof of [[thm:iii-i14-3-1]] at b, by (P1)–(P6). E^ν ∈ 𝒴(α_1), by (P6), joins
the terms of Step 1. The rotation rows, of K⁺-weight Re λ − ϵ > 1 > α_1 − 2 ([[lem:iii-i15-2-1]]), lie above the base
level.

*Step 2 at b.* Let u := u(p⃗′) ∈ 𝒵_(β_k). As in Step 2 of the proof of [[thm:iii-i14-3-1]], by [[eq:iii-i15-1-1]],
u_0 := u + Σ_(𝒩⊔𝒩_rot) m_ν(W′_ν) solves L_(h,p⃗)u_0 = G′(p⃗′) ∈ 𝒴^♮(β_(k+1)) (resp. 𝒴^♮(α−) for k + 1 = K).
[[lem:iii-i15-2-4]] gives, for β_(k+1) > 3 (below 3, [[lem:iii-i8-3-2]], as in Step 2 of the proof of
[[thm:iii-i14-3-1]]),

    u = Σ_(ν∈𝒩_(β_(k+1))⊔𝒩^(<β_(k+1))_rot) m_ν(C^(k+1)_ν(p⃗′)) + ũ,     ũ ∈ 𝒵_(β_(k+1)),            {#eq:iii-i15-2-3}

with C^(k+1)_ν := S^(h,p⃗,β_(k+1))_ν(G′(p⃗′)) − W′_ν for ν ∈ 𝒩_(β_(k+1)), and C^(k+1)_ν := A_(b,ν)(G′(p⃗′)) − W′_ν for
ν ∈ 𝒩^(<β_(k+1))_rot. The m_ν(W′_ν) of the other rows, of K⁺-weight above β_(k+1) − 2, are part of ũ. The *new rows*
of the level are those of 𝒩_(β_(k+1)) of rate in [β_k − 2, β_(k+1) − 2), as at b₀, and the rotation rows of
𝒩^(<β_(k+1))_rot ∖ 𝒩^(<β_k)_rot. If the conditions of the lower levels hold, then the coefficients of the old rows
vanish. For a rotation row, C^(k+1)_ν is the same function of p⃗′ at every level, A_b not depending on β. For the other
rows, Σ_(𝒩_(β_k)) m_ν(C^(k+1)_ν) ∈ 𝒵_(β_k), so they vanish by [[lem:iii-i15-1-2]]. Hence u ∈ 𝒵_(β_(k+1)) if
C^(k+1)_ν(p⃗′) = 0 for the new rows. The converse is not claimed for the rotation rows ([[rem:iii-i15-2-6]]).

*Step 3 at b.* Let 𝒫_k be the set of p⃗′ ∈ 𝒫_0 with C^j_ν(p⃗′) = 0 for the new rows of every level j ≤ k; by Step 2,
u(p⃗′) ∈ 𝒵_(β_k) on 𝒫_k. As in Step 3 of the proof of [[thm:iii-i14-3-1]], 𝒫_k is, by induction, the graph of an
affine map from the coordinates of the rows of rate ≥ β_k − 2 to the others. The rotation rows enter by their rates
Re λ at b. On 𝒫_k, C^(k+1) restricted to the new coordinates is −id + A_k, with A_k → 0 as (h, p⃗, q) → (0, 0, 0),
the parameter of p⃗ tending to b₀. The bound on A_k is direct, with no continuity in b. By Step 2,
C^(k+1)_ν(p⃗′) = S^(h,p⃗,β_(k+1))_ν(G′(p⃗′)) − W′_ν, resp. A_(b,ν)(G′(p⃗′)) − W′_ν, and G′ is affine in p⃗′. Its
dependence on the coordinates W′_ν of the rows of 𝒩 ⊔ 𝒩_rot is through:

- (r^ν_(h,p⃗) + E^ν_(h,p⃗))(W′_ν). At the base point (0, p⃗_b) the identity [[lem:iii-i9-2-4]] at b gives
  f^ν_b = L_(0,p⃗_b)m_ν up to the O(|b − b₀|) mixing of g_(b₀,b,0) in 𝒞. So r^ν_(h,p⃗) + E^ν_(h,p⃗) has norm
  O(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|) in 𝒴^♮_2(α−) (the bounds of [[lem:iii-i9-2-6]] at b, and (P6)).
- Δ_q(p⃗′) and R_q u(p⃗′), of norm O(‖q‖) ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]).

The motion coordinates enter through f^S, f^b, f^(s1), but they lie at the base level, below every new row. On 𝒫_k the
lower coordinates are, by the induction, affine functions of the free ones with coefficients of the same smallness.
S^(h,p⃗,β) and A_b are bounded uniformly in b and (h, p⃗) small ([[lem:iii-i15-2-4]], [[def:iii-i15-2-3]]). So in the
new coordinates C^(k+1) = −id + A_k with |A_k| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|), C uniform in b, by the direct
bound. At the levels below 3 the same direct bound applies: there C^(k+1) is the K⁺-coefficient of
u = u_0 − Σ m(W′) given by [[lem:iii-i8-3-2]], a bounded functional of G′, uniform in b by (P1), minus W′, and G′
depends on the new W′ only through the small terms listed above, the rows there being rows of [[eq:iii-i15-1-1]]. At
the base level the new coordinates are the motion parameters (S′, b′, S^(0)′_1), which enter G′ through f^S, f^b,
f^(s1) in full. There the level map is that of [[cor:iii-i7-4-6]], the composite of the maps of [[lem:iii-i7-4-3]] and
[[lem:iii-i7-4-5]], and [[prop:iii-i15-2-12]] bounds those directly, within C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|) of ±id,
with ‖q‖ entering through Δ_q and R_q as above. Their composite is block-triangular, not of the form −id + A_k; what
the elimination uses is that its inverse is bounded uniformly, which this gives. So
|A_k| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|) at every level above the base, the base level's map has a uniformly
bounded inverse, and the continuity statements that Step 3 of the proof of [[thm:iii-i14-3-1]] cites are not needed.

So −id + A_k is invertible for (h, p⃗, q) small, and 𝒫_(k+1) is a graph. At k = K every row has rate below α − 2 (the
rotation rows at b: Re λ ≤ 2 < α − 2), so 𝒫_K is one point p⃗′. It satisfies [[eq:iii-i15-2-2]], and u(p⃗′) ∈ 𝒵_α
with no rotation-row content. The rest of the proof of [[thm:iii-i14-3-1]], the splitting u = h_(b,rem)(q′) + h′ by
[[thm:iii-i12-3-1]] at b ([[cor:iii-i15-2-10]]), then applies. The v1 coefficient of q′ has no term at ℳ_rot. p⃗′ is
affine in F, which enters through G̃ only, and linear since it vanishes at F = 0. Uniqueness: any p⃗″ satisfying
[[eq:iii-i15-2-2]] with u(p⃗″) ∈ 𝒵_α lies in 𝒫_0 (the uniqueness in Step 1 of the proof of [[thm:iii-i14-3-1]]). Its
non-rotation coefficients vanish level by level by [[lem:iii-i15-1-2]], since [[eq:iii-i15-2-2]] removes the rotation
rows from [[eq:iii-i15-2-3]]. So p⃗″ ∈ 𝒫_K.

*At b₀.* Write W′^rot := (W′_ν)_(ν∈𝒩_rot). At b₀ the v1 coefficient of u = u_0 − Σ m_ν(W′_ν) at ℳ_rot is
A_(b₀)(G′) − W′^rot. The v1 pieces of u_0 are the construction's, with the coefficients A_(b₀)(G′)
([[prop:iii-i15-2-2]] at b₀). On 𝒫_K the coefficients of the rows of 𝒩 vanish, and the functional ℓ of Step 4′ of the
proof of [[thm:iii-i14-3-1]], applied to u = u_0 − Σ m_ν(W′_ν), returns its v1 coefficient uniquely; by
[[prop:iii-i15-2-2]] (c) and [[def:iii-i15-2-3]] it is A_(b₀)(G′) − W′^rot, and m_ν(W), ν ∈ 𝒩_rot, has v1
coefficient a_ν W. So C^rot = 0 is [[eq:iii-i15-2-2]] (with the sign of the derivative −id of Step 4′). The p⃗′ of
[[thm:iii-i14-3-1]] satisfies the level conditions and [[eq:iii-i15-2-2]], so it is the point 𝒫_K. ∎

**Remark {#rem:iii-i15-2-6}** (Uniqueness at b.) At a rotating b, the p⃗′ of [[prop:iii-i15-2-5]] is unique only
together with [[eq:iii-i15-2-2]]. The bottom of m_ν(W), ν ∈ 𝒩_rot, is a_ν h_(b,v1)(W) = a_ν(ġ_b(ḃ_W) + h_b(S_W)), with
coefficients O(|b − b₀||W|) ([[rem:iii-i15-1-2]]). The K⁺-expansion does not separate it from the b- and S-rows, so
the conditions u ∈ 𝒵_(β_k) alone are not shown to fix W′^rot. The later results use only the constructed map
F ↦ (p⃗′, q′, h′):

- [[thm:iii-j1-2-1]] builds U′ from it; [[rem:iii-j1-2-2]] records that D_UΦ is not injective.
- [[thm:iii-j2-4-1]] estimates it.
- The proof of [[thm:iii-j3-5-3]] cites Step 3 of the proof of [[thm:iii-i14-3-1]] and its uniqueness, to identify the
  exact and the lossy solutions. At b, the constrained uniqueness of [[prop:iii-i15-2-5]] serves there: A_b does not
  depend on the loss, being computed from ι⁺- and tf-data, which the exact and the lossy classes share.

