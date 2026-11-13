## Base points near b₀ {#ch:s25}

The statement at b ([[def:s25-at-b]]), the model objects (P1)–(P5) of [[lem:iii-i15-1-1]], the ball ℬ_*
([[lem:s25a-ball]]), the rotation state at b ([[rem:iii-i15-1-2]]) and the results of [[ch:s19]] at b
([[prop:iii-i2-5-1-b]]) are in [[ch:s25a]]; the sixth property (P6) of the model at b, which uses [[ch:s21]]–[[ch:s23]],
is [[lem:s25-p6]] below.

This chapter proves that the linear theory of [[ch:s19]]–[[ch:s24]] holds at every base point whose black hole
parameter b lies in a fixed neighbourhood ℬ_* of b₀ = (m₀, 0), with constants and smallness conditions uniform in b
([[thm:iii-i15-3-1]] for [[ch:s19]]–[[ch:s23]], [[cor:s25-tame]] for [[ch:s24]]). That theory consists of the forward
solutions in the cone and their improvement at ι⁺ and K⁺, the boost parameter, almost boundedness, the extraction and
the elimination of the parameters, the centre-of-mass motions, the corrections of the fourth kind, the expansion at
the Kerr face, the augmentation by its coefficients, the parameterisation by data, the tame estimates and the exact
weights. With it, the right inverses that the Nash–Moser theorem ([[thm:ii-g-2-1]]) asks for exist at every base
point near the one of the iteration, with uniform bounds ([[cor:iii-i15-3-2]]). [Hin26] states its Sections 11.2–12
at base points with |b − b₀| small; [[thm:iii-i15-3-1]] and [[cor:s25-tame]] are that statement in dimension 4 + 1,
and the lemmas and propositions that prove them are new in this dimension.

Three ingredients are proved for this. The model objects at b are those of [[lem:iii-i15-1-1]] ([[ch:s25a]]): the forward
solutions; the ι⁺- and tf-normal operators and the indicial roots, which do not depend on b; the zero energy states,
towers and physical states at b, real and smooth in b and equivariant under the antipodal map; the augmented low-energy
theory; and the Killing time translation. [[sec:s25-rows]] adds the identity [[eq:iii-i15-1-1]], which compares the rows
built at b with the corrections built at b₀ ([[lem:s25-p6]]), and proves the joint injectivity of the states at b by
perturbation from b₀ ([[lem:iii-i15-1-2]]); the rotation state at b is a change of the black hole parameter alone
([[rem:iii-i15-1-2]]). [[sec:iii-i15-2]] treats the rotation terms: the v1 terms of exponent of real part at most 2 are
rotation rows whose coefficients are assigned from the construction that produces them ([[prop:iii-i15-2-2]],
[[def:iii-i15-2-3]]), and with them the decay theorem [[thm:iii-i14-3-1]] holds at b ([[prop:iii-i15-2-5]]).
[[sec:iii-i15-3]] states the theorem and its corollary for the tame and exact forms, and records where a step proved
at b₀ uses a property of b₀ that a general b need not have, and what replaces it at b. Three such steps need more
than a substitution: the boost identity, the parameter identities and the expansion at a rotating b. They are proved
at b, with direct bounds in place of continuity in b, in [[lem:iii-i15-2-7]] and [[prop:iii-i15-2-8]] ([[ch:s20]]),
[[lem:iii-i15-2-11]] and [[prop:iii-i15-2-12]] ([[ch:s21]]), and [[lem:iii-i15-2-9]] and [[cor:iii-i15-2-10]]
([[ch:s22]]).

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
R₁ = m₀^(1/2), and |b − b₀| is the norm of [[def:s12-radii]]. ℬ_1 and ℬ_*, with ℬ̄_* ⊂ ℬ_1, are the neighbourhoods of b₀
of [[sec:iii-h2-0]]; ℬ_* is the ball about b₀ of radius at most 1/(2C_B) of [[lem:s25a-ball]] ([[lem:s20-rows]]
takes its constant C_B as a supremum over that ball, which is at most the one of [[lem:s25a-ball]], so its condition on
the radius holds already and shrinks nothing), shrunk further in [[lem:iii-i15-1-2]] and [[prop:iii-i15-2-5]] (and in
[[prop:iii-i15-2-8]] and [[prop:iii-i15-2-12]]), each time to a smaller ball about b₀, and every statement below holds
on the final ℬ_*. (P1)–(P5) are the properties of [[lem:iii-i15-1-1]], and (P6) is that of [[lem:s25-p6]]. As in
[[ch:s16]], λ ∈ ℂ is an exponent at ι⁺; it is not the wavelength. The letter ε > 0 is small, and "order w−" means
order w − ε for every ε > 0 ([[sec:iii-i14-1]]). The types 𝒯 = {s1, v1, s0, s2, c0, c1}, the rows ν = (τ, λ, k) with
their K⁺-exponents e_ν and weights κ_ν, the index set 𝒩 = 𝒩_ι ⊔ 𝒩_σ, the coefficient spaces 𝒲_(τ,ℂ), the parameter space
𝒫, the operator P_4 and the classes of sources 𝒴_2(α), 𝒴(α) are those of [[sec:iii-i9-1]] and [[sec:iii-i9-2]] (with (G)
and the levels of [[ch:s22]]); ℳ, ℰ_(++), λ_♯ and the class 𝒴(α_1) of the levels below 3 are those of [[sec:iii-i8-1]];
ℰ_♯, ℰ^♮, 𝒴^♮_2(β), 𝒴^♮(β) and the spaces 𝒵_β are those of [[ch:s22]] ([[def:iii-i13-1-2]]); 𝒬, h_(b,rem), P_5, R_q, Δ_q,
𝒩_rot and ℳ_rot are those of [[def:iii-i14-1-1]]–[[def:iii-i14-1-3]]. The corrections of the first to fourth kinds are
those of [[def:iii-i4-2-1]], [[def:iii-i7-2-1]], [[def:iii-i8-2-1]] and [[def:iii-i9-2-1]], with their counterterms
ϑ_(ν,♯). L̂_b(0), its augmentation L̃_b(0) and the states ġ_b(ḃ), h_b(S) = h_(b,s1)(S), h̆_b(S) and h_(b,v1)(V) are those
of [[ch:s25a]].

*The inner radius.* Every result of the chapter holds with the inner radius r₀ = r_♭ ∈ (0, ½R₁] of [[def:s12-radii]]
as a parameter, with constants and neighbourhoods of b₀ that may depend on it. The chapter names no inner radius and
no fixed radius. It works on Ω_* = cl_M{t^♭_* ≥ 1} with the spaces of [[ch:s04]]–[[ch:s10]], extendible at the inner
boundary, and with the results of [[ch:s04]]–[[ch:s24]], which hold at every such r_♭; its levels and weights are fixed
by weights at infinity and at K⁺, not by the inner radius. The neighbourhoods ℬ_1 and ℬ_* are those chosen in
[[sec:iii-h2-0]] for the given r_♭.

### Rows at b and the joint injectivity {#sec:s25-rows}

**Lemma {#lem:s25-p6}** (Rows at b, corrections at b₀.) For b ∈ ℬ̄_*, uniformly in b, the model objects of
[[lem:iii-i15-1-1]] have the following sixth property.

(P6) *Rows at b, corrections at b₀.* The rows and towers are built at the base point's b (the towers T_(ψ,b) of
[[def:iii-i14-1-2]], smooth in b by [[lem:iii-i15-1-1]] (P3)); the corrections of the first to fourth kinds and their
counterterms are the tensors built from b₀-objects, as [Hin26, p. 275, Definition 11.55] builds them; the operator of
[Hin26, Definition 11.56] is at b. At a base point (h, p⃗) with parameter b,

    D_p⃗P_4(h, p⃗)(W_ν = W) = L_(h,p⃗)m_ν(W) + r^ν_(h,p⃗)(W) + E^ν_(h,p⃗)(W).                          {#eq:iii-i15-1-1}

Here f^ν_b := L_(h,p⃗)m_ν + r^ν_(h,p⃗), with r^ν_(h,p⃗) of [[lem:iii-i9-2-6]] (e), every object in it (rows,
corrections, counterterms) built at b, and r^ν_(h,p⃗) in the class of [[eq:iii-i9-2-5]] uniformly in b. And

    E^ν_(h,p⃗)(W) := L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W),

the difference between the corrections and counterterms built at b₀ and at b, lies in 𝒴^♮_2(α−) ∩ 𝒴(α_1), with norm
O(|b − b₀||W|). Its support is in supp χ_K, its K⁺-weight is κ_ν − ε > α, and its ι⁺-exponents below w_+ lie in
ℰ^♮ + 2 ([[def:iii-i13-1-2]]).

*Proof.* The identity [[eq:iii-i15-1-1]], with r^ν_(h,p⃗) in the class of [[eq:iii-i9-2-5]] uniformly in b, is
[[lem:iii-i9-2-6]] (e). Its errors near K⁺ are L_(h,p⃗) − L_b, which gains a_K there, as g_0 = g_b near K⁺
([[lem:iii-i-3-6]]); its objects are smooth in b (P3), so the bounds are uniform. For E^ν:

- The differences h^(b₀)_ν − h^b_ν and ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯) are b-differences of the 1-form towers and of their
  commutators with χ_K, so O(|b − b₀|) by (P3), and supported in supp χ_K.
- Near K⁺ the corrections vanish (they are supported in 𝒞), but the counterterms do not: there ϑ_(ν,♯) = ½□ω_ν
  ([[sec:iii-i9-2]]). Their difference has the K⁺-weight κ_ν of the tops of the towers ([[lem:iii-i9-2-2]] (a), (d),
  and (P3)). So E^ν has K⁺-weight κ_ν − ε > α.
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
[[eq:iii-i15-1-1]] is the identity of [[lem:iii-i9-2-6]] (c).

**Lemma {#lem:iii-i15-1-2}** (Joint injectivity at b.) Shrinking ℬ_*, [[lem:iii-i10-2-2]] and [[cor:iii-i10-2-3]] hold
at every b ∈ ℬ̄_*, for the states at b: if Σ_(τ≠v1) h_(b,τ)(W_τ) = 0 then every W_τ = 0; and a finite sum of rows
ν ≠ v1 at b with K⁺-weight above the largest of their rates has all its coefficients zero. Moreover, there are a compact
set 𝔎_0 ⊂ X° and c > 0, independent of b, with sup_(𝔎_0)|Σ_(τ≠v1) h_(b,τ)(W_τ)| ≥ c Σ_(τ≠v1) |W_τ|. For the s1 states
alone this is [[lem:s20-injective]].

*Proof.* The space 𝒲 := ⊕_(τ≠v1) 𝒲_(τ,ℂ) is finite-dimensional. At b₀ the map Θ_(b₀): W ↦ Σ_τ h_(b₀,τ)(W_τ) is
injective ([[lem:iii-i10-2-2]]). Each nonzero element of its range is a nonzero smooth tensor on X°, nonzero on an
open set, so by compactness of the unit sphere of 𝒲 there is a compact 𝔎_0 ⊂ X° on which
sup_(𝔎_0)|Θ_(b₀)W| ≥ 2c|W|. Θ_b depends continuously on b in C⁰(𝔎_0) (P3), so the bound with c holds for b near b₀.
The proof of [[cor:iii-i10-2-3]] uses only [[lem:iii-i10-2-2]] and [[lem:iii-i9-2-2]] (e), the K⁺-weight
Re e_ν + 1 − ε of m_ν(W) − χ_K r_ν h_τ(W), which follows from the tower relations alone and holds at b (P3). ∎

By [[rem:iii-i15-1-2]], h_(b,v1)(V) = ġ_b(ḃ_V) with |ḃ_V| = O(|b − b₀||V|). So v1 stays excluded from
[[lem:iii-i15-1-2]] at b, as at b₀, and for a quantitative reason: a K⁺-extraction that read a v1 coefficient beside the
b- and S-coefficients would invert a map that degenerates as b → b₀. This is why the v1 coefficients are assigned in
[[sec:iii-i15-2]], not read from the K⁺-expansion.

### The rotation rows at b {#sec:iii-i15-2}

Let 𝒩_rot, ℳ_rot = ℰ_♯ ∩ {Re ≤ 2} and the rotation rows m_ν, ν = (rot, λ, k), be those of [[def:iii-i14-1-1]] and
[[def:iii-i14-1-3]], built at the base point's b. With the v1 tower T_(v1,b) at b of [[sec:iii-i15-2-7]],

    m_ν(W) = χ_K T_(v1,b)(a_ν W),     a_ν = t_*^(−λ)(log t_*)^k,     W ∈ 𝒱_(1,ℂ),

up to the terms with a_ν^((3)) and a_ν^((4)), of K⁺-order Re λ + 3 − ε > α ([[lem:iii-i10-2-1]] (a): the tower of
[[def:iii-i14-1-3]] has the length K_v1 = 3 of [[sec:iii-i9-2]], and T_(v1,b) is its part j ≤ 2).

**Lemma {#lem:iii-i15-2-1}** (Rotation rows at b.) At b ∈ ℬ̄_*, m_ν(W) has K⁺-weight Re λ − ε (its bottom
a_ν h_(b,v1)(W), of size O(|b − b₀||W|)), and m_ν(W) − χ_K a_ν h_(b,v1)(W) has K⁺-weight Re λ + 1 − ε.
[[lem:iii-i9-2-2]] (a)–(e) and [[lem:iii-i9-2-4]]–[[lem:iii-i9-2-6]] hold for ν at b, with e_ν = λ and
κ_ν = Re λ + 4; in particular

    f^ν_(h,p⃗)(W) := D_p⃗P_4(h, p⃗)(W_ν = W) = f^ν_b(W) + E^ν_(h,p⃗)(W)

as in [[eq:iii-i15-1-1]], with f^ν_b(W) = L_(h,p⃗)m_ν(W) + r^ν_(h,p⃗)(W) ∈ 𝒴_2(α) uniformly in b, and
E^ν_(h,p⃗)(W) ∈ 𝒴^♮_2(α−) ∩ 𝒴(α_1) of size O(|b − b₀||W|).

*Proof.* As [[def:iii-i14-1-3]] states for b₀: the proofs of [[lem:iii-i9-2-2]] (a)–(e) and
[[lem:iii-i9-2-4]]–[[lem:iii-i9-2-6]] use the tower relations and not the coefficient space, and hold at b by (P3) and
(P6). The only change is the bottom, which at b₀ vanishes and at b is a_ν h_(b,v1)(W); it has K⁺-weight Re λ − ε and
is O(|b − b₀||W|) by (P3). The term L_(h,p⃗)m_ν(W) involves only the top of the tower, as T_(v1,b) solves L_b to its
length (the tower relations), so its K⁺-order is unchanged. ∎

**Proposition {#prop:iii-i15-2-2}** (The v1 terms are rotation rows with assigned coefficients.) Let b ∈ ℬ̄_* be the
black hole parameter of the base point.

(a) *The spacetime phase.* In [[prop:iii-i10-3-1]] at b, for each u-exponent λ₀ with Re λ₀ < 2 the graft's tower part
χ_K u^(j)_(b,0) ([[eq:iii-g2-4-3]] at b) equals

    Σ_(τ∈𝒯∖{v1}) m_((τ,λ₀,j))(W^(j)_τ) + m_((rot,λ₀,j))(V^(j))

up to K⁺-weight Re λ₀ + 1 − ε. Here V^(j) is the graft's v1 coefficient of t_*^(−λ₀)(log t_*)^j, read from the ι⁺-data
u_+ by [[thm:iii-g2-3-1]], in the normalisation of the rows of [[ch:s22]], in which a (log t_*)^j-term keeps the
prefactor of the term j = 0; for j = 0 it is −λ₀⁻¹V^(−1)_1, by a_v1 = −λ₀⁻¹t_*^(−λ₀) ([[eq:iii-g2-4-2]]). It is linear
and continuous in the forcing f of [[prop:iii-i10-3-1]], uniformly in b. (λ₀, j) ∈ ℳ ⊂ ℳ_rot, so the rotation row exists.
So [[prop:iii-i10-3-1]] (b) holds at b with the rows 𝒩_ι ⊔ 𝒩_(ι,rot), 𝒩_(ι,rot) the rotation rows (rot, λ₀, j) that arise
here, and these coefficients.

(b) *The spectral phase.* In [[prop:iii-i11-3-1]] at b, the v1 term c_v1(σ)T_(v1,b)(σ) of [[eq:iii-i11-2-2]]
([[lem:iii-i11-2-3]]) now has the bottom c_v1(σ)h_(b,v1)(Y), and its rate is α₀ (at b₀, α₀ + 1). At level 1
(2 ≤ Re α₀ < 2 + η_1) this is below α − 2 only for Re α₀ = 2 (by (G), no rate lies in (2, 2 + ε_K]). Those exponents
lie in ℰ_♯ ∩ {Re = 2} ⊂ ℳ_rot, and the term is, by [[lem:iii-i12-2-1]] (b), m_((rot,α₀,k))(Y′) up to K⁺-weight
Re α₀ + 1 − ε, with Y′ the coefficient that [[lem:iii-i11-2-3]] gives the v1 tower: Y times the constant of c_v1, read
from the tf-data. It is linear and continuous in the right-hand side, uniformly in b by (P2) and (P4). At level 2 the
v1 rate is α₀ + 1 ≥ 2 + η_1 > 2 + ε_K ≥ α − 2, as for the s0 and s2 towers there. So [[prop:iii-i11-3-1]] holds at b
with the rows 𝒩_σ ⊔ 𝒩_(σ,rot), 𝒩_(σ,rot) the rotation rows (rot, α₀, k) that arise here, and these coefficients.

(c) *No other v1 term.* Every v1 coefficient of the expansion has its exponents in ℰ_♯ ([[thm:iii-i12-3-1]], at b
[[cor:iii-i15-2-10]]: an ι⁺-exponent λ of u gives the coefficient t_*^(−λ+d_ψ), d_v1 = 0). So it either has real
part at most 2, and is one of (a)–(b), or real part above 2 + ε_K ≥ α − 2, and is carried by q ([[def:iii-i14-1-1]],
whose rates at a rotating b are Re z > 2 + ε_K).

*Proof.* (a) At b, [[thm:iii-g2-4-2]] gives the v1 term h^(≤2)_(b,v1)(a_v1 V^(−1)_1) of [[eq:iii-g2-4-3]], with
V^(−1)_1 from u_+, which does not depend on b ((P2): u_+ = N_ι⁺(λ)⁻¹(2f_+), and the decomposition of
[[thm:iii-g2-3-1]] is of u_+ on ι⁺). By [[eq:iii-g2-4-2]], a_v1 = −λ₀⁻¹t_*^(−λ₀), so
χ_K h^(≤2)_(b,v1)(a_v1 V) = m_((rot,λ₀,0))(−λ₀⁻¹V) up to the tower terms of order ≥ 3, of K⁺-weight
Re λ₀ + 3 − ε ([[def:iii-i14-1-3]], the rotation rows using h^(≤2) and the tower of [[sec:iii-i9-2]]). The other rows
are identified as in [[prop:iii-i10-3-1]] at b, by [[lem:iii-i10-2-1]] (c) at b (P3).

(b) The proof of [[lem:iii-i11-2-3]] at b is unchanged except that the v1 tower
T_(v1,b)(σ) = Σ_i (−iσ)^i h̆^i_(b,v1)(Y) has h̆^0_(b,v1) = h_(b,v1) ≠ 0. Its contribution with c_v1 is a piece of type
(b) of [[lem:iii-i12-2-1]], a tower with polyhomogeneous coefficient. Its rate is that of ℱ⁻¹(χc_v1), which at
level 1 is α₀ (the piece is σu_((α₀,k)), and c_v1 contributes |σ|^(α₀−1) to it). The level-2 count is that of
[[prop:iii-i11-3-1]], with the rate lowered by 1.

(c) As stated. ∎

**Definition {#def:iii-i15-2-3}** (The assigned rotation coordinates.) Let (h, p⃗) be a base point with parameter
b ∈ ℬ̄_*, β ∈ (3, 4 + ε_K] admissible, and G ∈ 𝒴^♮(β) such that the forward solution u of L_(h,p⃗)u = G satisfies the
hypothesis of [[lem:iii-i13-2-2]] with some w_0. The *assigned rotation coordinates* A_(b,ν)(G) ∈ 𝒱_(1,ℂ), ν ∈ 𝒩_rot,
are the coefficients of the rotation rows that [[prop:iii-i15-2-2]] (a)–(b) produces in u: the graft's v1 coefficients
at the exponents of ℳ (spacetime phase), and the spectral level-1 coefficients at the exponents of real part 2. They do
not depend on β or on ε, and neither does E^ν ((P6)). A_b commutes with complex conjugation: A_(b,ν̄)(Ḡ) is the complex
conjugate of A_(b,ν)(G), as L_(h,p⃗) is real and the objects of [[prop:iii-i15-2-2]] are real ((P3)). So for real G the
tuple (A_(b,ν)(G))_ν is conjugation-symmetric, as [[eq:iii-i15-2-2]] and [[def:iii-i14-1-3]] need. A_b := (A_(b,ν))_ν is
linear in G and has the bound of [[lem:iii-i13-2-2]]: for every w ∈ (0, w_0],

    |A_b(G)| ≤ C‖G‖_(𝒴^♮(β)) + C(‖h‖ + |p⃗|)‖u‖_(w),

with the seminorms of [[lem:iii-i13-2-2]] and C depending on w and uniform in b and in (h, p⃗) small. Indeed
[[prop:iii-i15-2-2]] reads A_b(G) from the forcing f′ := G − (L_(h,p⃗) − L_b)u = L_b u of the proof of
[[lem:iii-i13-2-2]], by maps linear and bounded uniformly in b ((P2), (P4)); and the count of Step 0 of the proof of
[[lem:iii-i11-3-2]], as in [[lem:iii-i13-2-2]], gives ‖f′‖_(𝒴^♮(β)) ≤ ‖G‖_(𝒴^♮(β)) + C(‖h‖ + |p⃗|)‖u‖_(w). This is
not a bound by G alone: the last term does not vanish at (0, p⃗_b), p⃗_b the parameter whose only nonzero component is
b − b₀, when b ≠ b₀ ([[lem:iii-i11-3-2]]). No continuity in b is claimed or needed (Step 3 of the proof of
[[prop:iii-i15-2-5]]). A_(b₀) is defined at b₀ by the same formulas.

**Lemma {#lem:iii-i15-2-4}** ([[lem:iii-i13-2-2]] and [[lem:iii-i13-2-3]] at b.) Let β ∈ (3, 4 + ε_K] be admissible,
(h, p⃗) a base point with parameter b ∈ ℬ̄_* and h ∈ 𝒳^∞ small, G ∈ 𝒴^♮(β), and let the forward solution u of
L_(h,p⃗)u = G satisfy the hypothesis of [[lem:iii-i13-2-2]]. Then

    u = Σ_(ν∈𝒩_β) m_ν(S_ν) + Σ_(ν∈𝒩^(<β)_rot) m_ν(A_(b,ν)(G)) + ũ,
        𝒩^(<β)_rot := {ν ∈ 𝒩_rot : Re λ_ν < β − 2},                                                 {#eq:iii-i15-2-1}

with ũ in the class of [[eq:iii-i13-2-2]] and S_ν = S^(h,p⃗,β)_ν(G) determined by
u − Σ_(𝒩^(<β)_rot) m_ν(A_(b,ν)(G)), conjugation-symmetric and linear in G, with the bound of [[lem:iii-i13-2-2]]: for
every w ∈ (0, w_0], w_0 that of the hypothesis,

    |S^(h,p⃗,β)_ν(G)| + |A_b(G)| ≤ C‖G‖_(𝒴^♮(β)) + C(‖h‖ + |p⃗|)‖u‖_(w),

with the seminorms of [[lem:iii-i13-2-2]] and C depending on w and uniform for (h, p⃗) small and b ∈ ℬ̄_*. This is not a
bound by G alone ([[def:iii-i15-2-3]]). At a fixed b: if (h_j, p⃗_j) → (0, p⃗_b), with p⃗_b the parameter whose only
nonzero component is b − b₀, and G_j → G in 𝒴^♮(β), with the hypothesis of [[lem:iii-i13-2-3]], then
S^(h_j,p⃗_j,β)_ν(G_j) → S^(0,p⃗_b,β)_ν(G). At b₀ the second sum in [[eq:iii-i15-2-1]] is absent (the rotation rows' rates
there are Re λ + 1 > α − 2 ≥ β − 2), and [[eq:iii-i15-2-1]] is [[eq:iii-i13-2-2]]. For β < 3 no rotation row has rate
below β − 2 (Re λ − ε > 1, [[lem:iii-i15-2-1]]), and [[lem:iii-i8-3-2]] holds at b as at b₀.

*Proof.* By [[lem:iii-i13-2-2]], which is stated at b, u = Σ_(ν∈𝒩_β) m_ν(S_ν) + u^rot_β + ũ with ũ in the class of
[[eq:iii-i13-2-2]], and the S_ν are determined by u − u^rot_β. There u^rot_β is the sum of the terms of u^rot_ι
([[prop:iii-i10-3-1]]) with Re λ₀ < β − 2 and of the spectral v1 terms v^rot_β ([[prop:iii-i13-2-1]]), and
[[prop:iii-i15-2-2]] (a) and (b) identify these two kinds of terms; the identifications do not involve the level, and
β − 2 ≤ α − 2. So the terms of u^rot_β are the rotation rows with the coefficients A_(b,ν)(G) of [[def:iii-i15-2-3]],

    u^rot_β = Σ_(ν∈𝒩^(<β)_rot) m_ν(A_(b,ν)(G))     up to K⁺-weight Re λ + 1 − ε > β − 2,

which goes into ũ. Indeed, for (λ, k) ∈ ℳ_rot, λ lies in Λ (π_1ℳ_rot ⊂ π_1ℰ_♯ ⊂ Λ), so λ + 1 ∈ Λ has real part at least
λ_♯ + 1 > 2 ([[lem:iii-i10-1-2]] (a)), hence above 2 + ε_K by (G), while β − 2 ≤ 2 + ε_K. As u^rot_β − Σ_(𝒩^(<β)_rot)
m_ν(A_(b,ν)(G)) has K⁺-weight above β − 2, the S_ν, read by [[cor:iii-i10-2-3]] at b ([[lem:iii-i15-1-2]]) from the rows
of rate below β − 2, are also determined by u − Σ_(𝒩^(<β)_rot) m_ν(A_(b,ν)(G)). They are the S_ν of [[lem:iii-i13-2-2]],
whose conjugation symmetry, linearity and bound they have; A_b has the same bound ([[def:iii-i15-2-3]]). The continuity
at fixed b is [[lem:iii-i13-2-3]]. Continuity across b is not claimed: the proofs perturb from a reference operator, and
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
the terms of Step 1. The rotation rows, of K⁺-weight Re λ − ε > 1 > α_1 − 2 ([[lem:iii-i15-2-1]]), lie above the base
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

- (r^ν_(h,p⃗) + E^ν_(h,p⃗))(W′_ν). At the base point (0, p⃗_b), [[lem:iii-i9-2-6]] (e) gives
  f^ν_b = L_(0,p⃗_b)m_ν + r^ν_(0,p⃗_b) with r^ν_(0,p⃗_b) = O(|b − b₀||W|). So r^ν_(h,p⃗) + E^ν_(h,p⃗) has norm
  O(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|) in 𝒴^♮_2(α−) (the bounds of [[lem:iii-i9-2-6]] (e), and (P6)).
- Δ_q(p⃗′) and R_q u(p⃗′), of norm O(‖q‖) ([[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]]).

The motion coordinates (S′, b′, S^(0)′_1) enter through f^S, f^b, f^(s1) in full: these are linear in their
finite-dimensional arguments, with values in 𝒴⁰(α), which lies in the class of every level as G′ does in Step 2
([[sec:iii-i10-1]]), and norms O(|S′|), O(|b′|), O(|S^(0)′_1|) ([[lem:iii-i7-3-1]] (c), [[lem:iii-i9-2-6]] (a)).
They lie at the base level, below every new row, and along 𝒫_k they change only by O(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)
times the change of the row coordinates; this is [[eq:s25-motions-small]] below.

*The induction bound.* Write ‖·‖_(𝒴,k) for the seminorm of 𝒴^♮(β_k) of [[lem:iii-i13-2-2]] (of 𝒴(β_k) of
[[sec:iii-i8-1]] when β_k < 3, and of 𝒴^♮(α − ε) when k = K, as in [[lem:iii-i14-2-5]]), and ‖F‖ for a seminorm of F
in 𝒴^♮(α − ε), of large enough regularity ([[sec:iii-i8-1]]). The induction carries a bound: on 𝒫_k the coordinates
and u(p⃗′) are affine in F and in the free coordinates W⃗_free, and |p⃗′| and the seminorms of u(p⃗′) in 𝒵_(β_k) that
are used below are at most C(‖F‖ + |W⃗_free|), C uniform in b and in (h, p⃗, q) small. At k = 0 this is
[[prop:iii-i8-4-1]] (i) at b (Step 1); the step from k to k + 1 is shown below.

*The motion coordinates.* Put h″ := h + h_(b,rem)(q), and write D_(W⃗)P_5(W⃗) for D_(p⃗)P_5(h, p⃗, q) in the direction
with motion components 0 and row components W⃗, as in Step 1. For Ψ ∈ 𝒴(α_1) let p⃗′_(α_1)(Ψ) ∈ 𝒫_(α_1) be the
parameter that [[prop:iii-i8-4-1]], for P_5 at (h, p⃗, q) (Step 1), assigns to the forcing Ψ: the unique one for which
the forward solution u_Ψ of L_(h″,p⃗)u_Ψ = Ψ − D_(p⃗)P_5(h, p⃗, q)(p⃗′_(α_1)(Ψ)) lies in 𝒵_(α_1). By (i) of that
proposition, Ψ ↦ p⃗′_(α_1)(Ψ) is linear and |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖_(𝒴(α_1)), with C uniform in b and in (h, p⃗, q) small.
A point of 𝒫 is p⃗′_< ⊕ W⃗, with p⃗′_< ∈ 𝒫_(α_1) (the motion coordinates and the motions of ℳ_(α_1)) and
W⃗ = (W_ν)_(ν∈𝒩′⊔𝒩_rot) the other row coordinates (Step 1). By [[eq:iii-i14-3-1]] and the linearity of
D_(p⃗)P_5(h, p⃗, q) in the direction, u(p⃗′_< ⊕ W⃗) is the forward solution of

    L_(h″,p⃗)u = (F − D_(W⃗)P_5(W⃗)) − D_(p⃗)P_5(h, p⃗, q)(p⃗′_<),

so the point of 𝒫_0 over W⃗ (Step 1) has the motion part

    p⃗′_<(W⃗) = p⃗′_(α_1)(F − D_(W⃗)P_5(W⃗)) = p⃗′_(α_1)(F) − p⃗′_(α_1)(D_(W⃗)P_5(W⃗)).

We show that, with C uniform in b and in (h, p⃗, q) small,

    |p⃗′_(α_1)(D_(W⃗)P_5(W⃗))| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|W⃗|.                     {#eq:s25-motions-small}

(1) *The decomposition.* By [[def:iii-i14-1-2]], D_(p⃗)P_5(h, p⃗, q) = D_(p⃗)P_4(h, p⃗) + Δ_q and
L_(h,p⃗) = L_(h″,p⃗) − R_q; by [[eq:iii-i15-1-1]] (for the rotation rows, [[lem:iii-i15-2-1]]),
D_(p⃗)P_4(h, p⃗)(W_ν = W) = L_(h,p⃗)m_ν(W) + r^ν_(h,p⃗)(W) + E^ν_(h,p⃗)(W). Summing over the rows ν ∈ 𝒩′ ⊔ 𝒩_rot, with
m_rows(W⃗) := Σ_ν m_ν(W_ν),

    D_(W⃗)P_5(W⃗) = L_(h″,p⃗)m_rows(W⃗) + e_rows(W⃗),
    e_rows(W⃗) := Σ_ν (r^ν_(h,p⃗) + E^ν_(h,p⃗))(W_ν) − R_q m_rows(W⃗) + Δ_q(W⃗).

(2) *The remainder is small.* The class 𝒴(α_1) contains the class 𝒴_2(α_1) of [[sec:iii-i8-1]], which holds every
section supported in supp χ_K ⊂ supp χ^♯_K ([[eq:iii-i-1-2]]) with K⁺-weight above α_1 and plain ι⁺-weight above 4;
the 𝒴(α_1)-norm of such a section is at most a seminorm of it in those weights. The four kinds of terms of e_rows(W⃗):

- r^ν_(h,p⃗)(W) is supported in supp χ_K and lies in the class [[eq:iii-i9-2-5]], of plain ι⁺-weight
  Re λ + 2 + λ_♯ − ε > 4 and K⁺-weight Re e_ν + a_K − ε > α_1, with norm at most C|W|(‖h‖ + |p⃗|), uniformly on ℬ̄_*
  ([[lem:iii-i9-2-6]] (e); for the rotation rows, [[lem:iii-i15-2-1]]).
- E^ν_(h,p⃗)(W) lies in 𝒴(α_1), with norm at most C|b − b₀||W| ((P6); for the rotation rows, [[lem:iii-i15-2-1]]).
- m_rows(W⃗) has K⁺-weight λ_♯ − 1 − ε, ι⁺-weight λ_♯ − ε > 3/2 (above every β′_+ < 3/2), vanishes near ℐ⁺ and for
  t^♭_* < 10, and has seminorms O(|W⃗|) ([[lem:iii-i9-2-2]], [[lem:iii-i15-2-1]]). So [[lem:iii-i14-2-3]] at b (*The
  augmentation at b* in the proof of [[thm:iii-i15-3-1]]), with w := λ_♯ − 1, applies: R_q m_rows(W⃗) is supported
  in supp χ_K, has
  K⁺-weight (λ_♯ + α − 3)− > α_1 (as λ_♯ > 1 and α_1 < α − 2) and plain ι⁺-weight above w_+ > 4 (the proof of that
  lemma), with seminorms at most C‖q‖|W⃗|.
- Δ_q(W⃗) = Σ_ν R_q(h_ν(W_ν)) is supported in supp χ_K, has K⁺-order ∞ and plain ι⁺-weight above w_+, with norm
  O(‖q‖|W⃗|) ([[lem:iii-i14-2-4]] (a), at b as in the same paragraph).

So, as |p⃗| ≤ |p⃗ − p⃗_b| + |p⃗_b| = |p⃗ − p⃗_b| + |b − b₀|,

    ‖e_rows(W⃗)‖_(𝒴(α_1)) ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|W⃗|,     C uniform in b.

(3) *The rows carry no parameter.* m_rows(W⃗) vanishes for t^♭_* < 10 ([[lem:iii-i9-2-2]] (c)), so it is the forward
solution of L_(h″,p⃗)u = L_(h″,p⃗)m_rows(W⃗) (Step 0). It lies in 𝒵_(α_1). Every row of 𝒩′ has K⁺-rate above
α_1 − 2: the s0, s2, c0 and c1 rows have rates at least λ_♯ > 1 > α_1 − 2, and an s1 row of 𝒩′ has rate at least
α_1 − 2 and, by admissibility, not equal to it (the paragraph *The map* of the proof of [[thm:iii-i11-4-1]], with α_1
in place of α′). So its m_ν(W_ν) has K⁺-weight α_1 − 2 − ε for every ε > 0 ([[lem:iii-i9-2-2]] (e)). A rotation row
has K⁺-weight Re λ − ε > 1 > α_1 − 2 ([[lem:iii-i15-2-1]]). Every m_ν(W) has ι⁺-weight λ_♯ − ε > 3/2 and vanishes
near ℐ⁺ ([[lem:iii-i9-2-2]] (b), (c)), which are the other conditions of [[eq:iii-i8-4-2]] at α_1. m_rows(W⃗) is
real, as W⃗ is conjugation-symmetric ([[def:iii-i9-2-1]]). Moreover L_(h″,p⃗)m_rows(W⃗) = D_(W⃗)P_5(W⃗) − e_rows(W⃗)
lies in 𝒴(α_1), by Step 1 and (2). So the parameter 0 has, for the
forcing L_(h″,p⃗)m_rows(W⃗), the property that defines p⃗′_(α_1), and by the uniqueness in [[prop:iii-i8-4-1]],
p⃗′_(α_1)(L_(h″,p⃗)m_rows(W⃗)) = 0. This is the argument of the paragraph *The level map* of the proof of
[[prop:iii-i8-4-1]], and of the paragraph *At (0, 0)* of the proof of [[thm:iii-i11-4-1]].

(4) *The bound.* By (1), (3) and the linearity of p⃗′_(α_1),
p⃗′_(α_1)(D_(W⃗)P_5(W⃗)) = p⃗′_(α_1)(e_rows(W⃗)), and the bound of (i) of [[prop:iii-i8-4-1]] with (2) gives
[[eq:s25-motions-small]].

Along 𝒫_k ⊂ 𝒫_0, with F fixed, a change δW⃗ of the row coordinates therefore changes the motion coordinates by
δp⃗′_< = −p⃗′_(α_1)(D_(W⃗)P_5(δW⃗)), of size at most C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|δW⃗|.

*The bound on A_k.* Let δW′ be a change of the new coordinates, those of higher rate being fixed, and let δp⃗′, δG′
and δu be the changes it causes along 𝒫_k. By the induction bound every coordinate changes by at most C|δW′|; in
particular the row coordinates change by δW⃗ with |δW⃗| ≤ C|δW′|, so, by the last paragraph, the motion coordinates
change by at most C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|δW′|. With δW′_ν the change of the row coordinate W′_ν for every
row ν ∈ 𝒩 ⊔ 𝒩_rot,

    δG′ = −f^S_(h,p⃗)(δS′) − f^b_(h,p⃗)(δb′) − f^(s1)_(h,p⃗)(δS^(0)′_1)
          − Σ_(ν∈𝒩⊔𝒩_rot) (r^ν_(h,p⃗) + E^ν_(h,p⃗))(δW′_ν) − Δ_q(δp⃗′) − R_q δu.

The motion terms are at most C(|δS′| + |δb′| + |δS^(0)′_1|) in ‖·‖_(𝒴,k+1), by their norms stated after the list at
the start of this step. By that list, the row terms are at most C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|)|δW′|, and Δ_q(δp⃗′)
and R_q δu at most C‖q‖|δW′|, with the induction bound for δu ([[lem:iii-i14-2-3]] with w = β_k − 2, as
β_(k+1) < β_k + α − 4). So

    ‖δG′‖_(𝒴,k+1) ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|)|δW′|.

The change of C^(k+1) on the new rows is −δW′ + A_kδW′, where A_kδW′ is the tuple of the S^(h,p⃗,β_(k+1))_ν(δG′) and
A_(b,ν)(δG′). The forward solution of L_(h,p⃗)δu_0 = δG′ is δu_0 = δu + Σ_(𝒩⊔𝒩_rot) m_ν(δW′_ν), δW′_ν here the change
of every row coordinate, and δu_0 satisfies the hypothesis of [[lem:iii-i13-2-2]] with w := min(β_k − 2, λ_♯ − 1), as
u_0 does (Step 2 of the proof of [[thm:iii-i14-3-1]]). So [[lem:iii-i15-2-4]] gives

    |A_kδW′| ≤ C‖δG′‖_(𝒴,k+1) + C(‖h‖ + |p⃗|)‖δu_0‖_(w),     C uniform in b.

The last term does not vanish at (0, p⃗_b) when b ≠ b₀; it is bounded as follows. ‖δu‖_(w) ≤ C|δW′| by the induction
bound, as ‖·‖_(w) is bounded by a seminorm of 𝒵_(β_k) (w ≤ β_k − 2); and ‖m_ν(W)‖_(w) ≤ C|W| for every row, m_ν(W)
having K⁺-weight at least λ_♯ − 1 − ε ≥ w − ε, ι⁺-weight λ_♯ − ε and support away from ℐ⁺ ([[lem:iii-i9-2-2]],
[[lem:iii-i15-2-1]]). So ‖δu_0‖_(w) ≤ C|δW′|, and, as |p⃗| ≤ |p⃗ − p⃗_b| + |p⃗_b| = |p⃗ − p⃗_b| + |b − b₀|,

    |A_k| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|),     C uniform in b,

by the direct bound. At the levels below 3 the same direct bound applies: there, for ν = (s1, λ, j), C^(k+1)_ν is
the K⁺-coefficient S^(h,p⃗)_(λ,j)(G′) of u_0 := u + Σ_(𝒩⊔𝒩_rot) m_ν(W′_ν) given by [[lem:iii-i8-3-2]], transferred to
P_4 as in Step 1 and applied from an admissible level α″ ∈ (2, 2 + w], whose hypothesis u_0 meets, minus W′_ν; and
‖δG′‖_(𝒴,k+1) has the bound above, the rows there being rows of [[eq:iii-i15-1-1]] and the motion coordinates changing
as [[eq:s25-motions-small]] gives. The bound of
[[lem:iii-i8-3-2]], C‖G′‖_(𝒴(β_(k+1))) + C(‖h‖ + |p⃗|)‖u_0‖_(α″), uniform in b by (P1)–(P4), has the same form, and
the estimate above holds with ‖·‖_(α″) in place of ‖·‖_(w). At the base level the new coordinates are the motion
parameters (S′, b′, S^(0)′_1), which enter G′ through f^S, f^b, f^(s1) in full. There the level map is that of
[[cor:iii-i7-4-6]], the composite of the maps of [[lem:iii-i7-4-3]] and [[lem:iii-i7-4-5]], and [[prop:iii-i15-2-12]]
bounds those directly, within C(‖h‖ + |p⃗ − p⃗_b| + |b − b₀|) of ±id, with ‖q‖ entering through Δ_q and R_q as above.
Their composite is block-triangular, not of the form −id + A_k; what the elimination uses is that its inverse is bounded
uniformly, which this gives. So |A_k| ≤ C(‖h‖ + |p⃗ − p⃗_b| + ‖q‖ + |b − b₀|) at every level above the base, the base
level's map has a uniformly bounded inverse, and the continuity statements that Step 3 of the proof of
[[thm:iii-i14-3-1]] cites are not needed.

So −id + A_k is invertible for (h, p⃗, q) small, and 𝒫_(k+1) is a graph.

*The induction bound at k + 1.* At the point of 𝒫_k whose new coordinates are 0, C^(k+1) on the new rows is the tuple of
the S^(h,p⃗,β_(k+1))_ν(G′) and A_(b,ν)(G′). By [[lem:iii-i15-2-4]] it is at most C‖G′‖_(𝒴,k+1) + C(‖h‖ + |p⃗|)‖u_0‖_(w)
(below 3, by [[lem:iii-i8-3-2]], with ‖·‖_(α″) in place of ‖·‖_(w)), and by the induction bound at k this is at most
C(‖F‖ + |W⃗_free|): G′ is G̃ = F − Δ_q(p⃗′) − R_q u less the terms of the list and of f^S, f^b, f^(s1), and
u_0 = u + Σ_(𝒩⊔𝒩_rot) m_ν(W′_ν). As (−id + A_k)⁻¹ is bounded, the new coordinates on 𝒫_(k+1), and so all the
coordinates, are at most C(‖F‖ + |W⃗_free|), W⃗_free the coordinates of higher rate. On 𝒫_(k+1) every coefficient in
[[eq:iii-i15-2-3]] vanishes, so u(p⃗′) = ũ. Like the coefficients, ũ is obtained from f′ := G′ − (L_(h,p⃗) − L_b)u_0 and
the W′_ν by maps linear and bounded uniformly in b, each level losing finitely many derivatives (the proofs of
[[prop:iii-i10-3-1]], [[prop:iii-i11-3-1]] and [[lem:iii-i11-3-2]], at the level β_(k+1) as in [[lem:iii-i13-2-2]]; below
3 the bound on ũ of [[lem:iii-i8-3-2]]); and ‖f′‖_(𝒴,k+1) ≤ ‖G′‖_(𝒴,k+1) + C(‖h‖ + |p⃗|)‖u_0‖_(w) by the count of Step 0
of the proof of [[lem:iii-i11-3-2]]. So the induction bound holds at k + 1.

At k = K every row has rate below α − 2 (the rotation rows at b: Re λ ≤ 2 < α − 2), so 𝒫_K is one point p⃗′. It satisfies
[[eq:iii-i15-2-2]], and u(p⃗′) ∈ 𝒵_α with no rotation-row content; by the induction bound, |p⃗′| ≤ C‖F‖ and the seminorms
of u(p⃗′) in 𝒵_α are at most C‖F‖, C uniform in b. The rest of the proof of [[thm:iii-i14-3-1]], the splitting
u = h_(b,rem)(q′) + h′ by [[thm:iii-i12-3-1]] at b ([[cor:iii-i15-2-10]], with G := G′(p⃗′),
u_0 := u(p⃗′) + Σ_(𝒩⊔𝒩_rot) m_ν(W′_ν) and the W′_ν as the W_ν there), then applies. The three terms of the bound of
[[cor:iii-i15-2-10]] are at most C‖F‖: ‖G′(p⃗′)‖_(𝒴,K) ≤ C‖F‖, by the terms of G′ and G̃ = F − Δ_q(p⃗′) − R_q u(p⃗′);
with w_0 := min(α − 2, λ_♯ − 1), ‖u_0‖_(w_0) ≤ ‖u(p⃗′)‖_(w_0) + C|p⃗′| ≤ C‖F‖, as w_0 < α − 2; and |W′_ν| ≤ |p⃗′| ≤ C‖F‖.
So the seminorms of q′ and h′ are at most C‖F‖, C uniform in b. The v1 coefficient of q′ has no term at ℳ_rot. p⃗′ is
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
the conditions u ∈ 𝒵_(β_k) alone are not shown to fix W′^rot. The results that use [[prop:iii-i15-2-5]] use only the
constructed map F ↦ (p⃗′, q′, h′) and its uniqueness together with [[eq:iii-i15-2-2]]:

- [[thm:iii-j1-2-1]] builds U′ from the constructed map; [[rem:iii-j1-2-2]] records that D_UΦ is not injective.
- A_b does not depend on the loss ε, being computed from ι⁺- and tf-data ([[def:iii-i15-2-3]]). So when F lies in a
  smaller class of right sides, which has the same ι⁺- and tf-data, a parameter found for F there that satisfies
  [[eq:iii-i15-2-2]] and gives u ∈ 𝒵_α is the p⃗′ of [[prop:iii-i15-2-5]], by that uniqueness.

### The linear theory at b {#sec:iii-i15-3}

**Theorem {#thm:iii-i15-3-1}** (The linear theory at base points near b₀.) For base points with black hole parameter
b ∈ ℬ̄_*, the statements at b ([[def:s25-at-b]]) of the following hold, the v1 terms of exponent of real part at most
2 being treated by [[sec:iii-i15-2]], with constants and smallness conditions uniform in b:

- the results below level 3 ([[lem:iii-i1-1-1]]–[[prop:iii-i1-3-1]], [[lem:iii-i2-2-1]]–[[prop:iii-i2-5-1]],
  [[lem:iii-i3-1-1]]–[[prop:iii-i3-2-1]], [[def:iii-i4-1-1]]–[[cor:iii-i4-4-3]], [[prop:iii-i5-2-1]],
  [[cor:iii-i5-2-2]] and [[lem:iii-i6-1-1]]–[[prop:iii-i6-2-1]]), the backgrounds g_0 := g_(b₀,b₀,−S) of
  [[sec:iii-i2-1]] and g_S of [[eq:iii-i4-1-1]] becoming g_(b₀,b,−S), and the correction of the first kind staying
  the tensor built at b₀ ((P6)), with [[prop:iii-i4-4-1]] (2), [[cor:iii-i4-4-3]] and [[cor:iii-i5-2-2]] in the form
  of [[prop:iii-i15-2-8]];
- [[lem:iii-i7-1-3]], [[lem:iii-i7-2-2]], [[lem:iii-i7-2-4]], [[lem:iii-i7-2-5]], [[lem:iii-i7-3-1]],
  [[lem:iii-i7-4-1]], [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]], [[def:iii-i7-4-4]] and [[cor:iii-i7-4-6]]:
  [[lem:iii-i7-2-2]] being independent of b, [[lem:iii-i7-3-1]] with p⃗ = (S, b − b₀, S^(0)_1) (its proof transfers,
  g_b being Ricci flat for every b and ġ_b given by (P3)), [[lem:iii-i7-2-4]] in the form of [[lem:iii-i15-2-11]],
  [[lem:iii-i7-4-1]] at fixed b only, and [[lem:iii-i7-4-3]], [[lem:iii-i7-4-5]] and [[cor:iii-i7-4-6]] in the form of
  [[prop:iii-i15-2-12]];
- [[prop:iii-i8-4-1]] and the lemmas it rests on ([[lem:iii-i8-2-2]]–[[lem:iii-i8-3-3]]), in the form of the direct
  bound of [[prop:iii-i15-2-5]], with the base step by [[prop:iii-i15-2-12]], [[lem:iii-i8-2-4]] in the form
  [[eq:iii-i15-1-1]], its rows being rows of the set 𝒩 of [[sec:iii-i9-1]], and [[prop:iii-i8-4-1]] (ii) and
  [[lem:iii-i8-3-3]] at fixed b only;
- [[sec:iii-i9-2]], with [[lem:iii-i9-2-4]] and [[lem:iii-i9-2-6]] (c) (r_(0,0) = 0) in the form [[eq:iii-i15-1-1]]
  of [[lem:iii-i9-2-6]] (e), and the identities [[eq:iii-i7-2-3]] that [[lem:iii-i9-2-4]] states for P_4 in the form
  [[eq:iii-i15-2-7]] of [[lem:iii-i15-2-11]], P_4 being P_2 on the directions of p⃗_≤0 at W = 0;
- [[def:iii-i10-1-1]], [[def:iii-i10-1-3]], [[lem:iii-i10-1-2]], [[lem:iii-i10-2-1]] (c) and [[prop:iii-i10-3-1]];
- [[prop:iii-i11-3-1]], [[lem:iii-i11-3-2]] and [[lem:iii-i11-3-3]] (stated at a fixed b),
  and [[thm:iii-i11-4-1]] only inside [[lem:iii-i15-2-4]] and [[prop:iii-i15-2-5]]: at a rotating b its parameter
  space lacks the rotation rows, and [[prop:iii-i15-2-5]] with q = 0 is its form there;
- [[lem:iii-i12-2-3]], [[lem:iii-i12-2-4]] and [[thm:iii-i12-3-1]], in the forms of [[lem:iii-i15-2-9]] and
  [[cor:iii-i15-2-10]];
- [[prop:iii-i13-2-1]], [[lem:iii-i13-2-2]] and [[lem:iii-i13-2-3]] in the form of [[lem:iii-i15-2-4]], and
  [[prop:iii-i13-2-4]] only inside [[prop:iii-i15-2-5]], as for [[thm:iii-i11-4-1]];
- [[def:iii-i14-1-2]] with [[eq:iii-i14-1-4]], [[lem:iii-i14-2-2]]–[[lem:iii-i14-2-5]], [[rem:iii-i14-3-2]] (2), and
  [[thm:iii-i14-3-1]] in the form of [[prop:iii-i15-2-5]] (unique among the p⃗′ with the assigned rotation
  coordinates);
- [[lem:iii-j-2-1]], [[lem:iii-j-2-2]], [[lem:iii-j-2-3]], [[thm:iii-j-2-4]] and [[rem:iii-j-2-5]], as written, with
  the rows built at b₀ ((viii) below);
- [[lem:iii-j1-1-1]], for the output of [[prop:iii-i15-2-5]], and [[thm:iii-j1-2-1]].

*Proof.* [[ch:s20]], [[ch:s21]] and [[ch:s22]] state and prove their results at a base point with parameter
b ∈ ℬ̄_*, with constants uniform in b: [[ch:s20]] from its own model at b, with [[lem:s20-rows]] and
[[lem:s20-injective]]; [[ch:s21]] and [[ch:s22]] from (P1)–(P6), [[lem:s25a-ball]], [[rem:iii-i15-1-2]],
[[prop:iii-i2-5-1-b]], [[lem:iii-i15-1-2]] and [[sec:iii-i15-2]], and from the results at b of the chapters before
them ([[lem:s20-injective]], [[lem:iii-i15-2-7]] and [[prop:iii-i15-2-8]] of [[ch:s20]] among them). The results of
[[ch:s19]] below level 3 hold at b by [[prop:iii-i2-5-1-b]]. The results of [[ch:s23]] stated at b₀ hold at b by
[[prop:iii-i15-2-5]] and by the paragraph *The augmentation at b* below. Items (i)–(xi) record where a step proved at
b₀ uses a property of b₀ that a general b ∈ ℬ̄_* need not have, or an object built at b₀, and what replaces it at b.
The three steps that need more than a substitution are proved at b in [[lem:iii-i15-2-7]] and [[prop:iii-i15-2-8]],
[[lem:iii-i15-2-11]] and [[prop:iii-i15-2-12]], and [[lem:iii-i15-2-9]] and [[cor:iii-i15-2-10]].

(i) *The forward solutions.* The results listed solve with L^(g,g_0) at the base point through [[thm:iii-i-5-3]] and its
corollaries ((P1)). The splitting L_(h,p⃗) = L_(b₀) + (L_(h,p⃗) − L_(b₀)) near K⁺, used to move a perturbation into the
right-hand side (in [[ch:s21]] and [[ch:s22]], for instance in Step 0 of the proof of [[thm:iii-i12-3-1]]), becomes
L_(h,p⃗) = L_b + (L_(h,p⃗) − L_b). This has the same K⁺-gain, as g_0 = g_b near K⁺ ([[lem:iii-i-3-6]]). The class
statement k_S ∈ 𝒦 of [[ch:s20]] reads k_S := g_(b₀,b,−S) − g_b ∈ 𝒦 at b, with differences taken from g_b; k′ := ∂_S k_S
is unchanged and vanishes near K⁺. At b, L_(h,S) := D_hP_1(·, S, b), and P_1(0, 0, b) need not vanish in 𝒞; the linear
theory uses only D_hP_1 and D_SP_1.

(ii) *The model at ι⁺ and at tf:* the results of [[ch:s16]] and [[ch:s17]], through (P2) and (P4).

(iii) *The states, towers and index sets.* The index sets of [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]],
[[prop:iii-f3-2-2]] and [[prop:iii-f3-4-1]], which [[ch:s20]] and [[ch:s21]] use, are independent of b ((P3)), so the
index sets ℰ_ind, ℰ_♯ and ℰ_+ serve at every b, and so does ℰ^♮ ([[def:iii-i13-1-2]]), built from ℰ_♯ and ℰ_ind. The
index set of the column terms ℰ_col ([[def:iii-i10-1-1]], [[lem:iii-i11-1-1]]), which generates Λ and through it ℰ_par,
𝒩, ℰ_♯, ℰ^♮, (G) and admissibility, is the b-independent set

    ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀

of [[lem:iii-i11-1-1]]. There F = r⁴f with f = [L_b, χ_K]w, and at every b the states w have the index sets (2, 0) ∪
(2 + ℰ_ind) (ġ_b(1, 0) and h̆_b(S), and t_*h_b(S), as t_* = sr) and (3, 0) ∪ (3 + ℰ_ind) (ġ_b(0, Ȧ)) ((P3);
[[eq:iii-f3-2-2]], [[eq:iii-d2-3-4]]); the commutator gains 2, the factor r⁴ loses 4, and the smooth coefficients of the
L_k ([[lem:iii-i3-1-1]] at b) add ℕ₀.

(iv) *The derivatives in b* ([[cor:iii-i7-4-6]], [[lem:iii-i14-2-4]] (c)) are taken at b: the b-column is ġ_b
((P3)). So is ġ = ∂_b g_b in [[ch:s19]] and [[ch:s20]], which enters through the columns and the singular part of
[[ch:s18]] ((P3), (P4)). The proof of [[lem:iii-i14-2-4]] (c) is written for every b near b₀, and the use of
L̂_(b₀)(0)∂_b h_(b,v1) = 0 in Step 1 of the proof of [[thm:iii-i14-3-1]] is replaced at b by the rates of the v1
coefficients of q, as [[sec:s23-base-points]] (1) shows.

(v) *The joint injectivity:* [[lem:iii-i10-2-2]] and [[cor:iii-i10-2-3]] hold at b by [[lem:iii-i15-1-2]]. Step 4′ of
the proof of [[thm:iii-i14-3-1]] is not used at b, [[prop:iii-i15-2-5]] replacing it. The injectivity of S ↦ h(S)
([[prop:iii-f3-4-1]] (1), proved at b₀ by symmetry), used in the proofs of [[prop:iii-i3-2-1]], [[prop:iii-i4-4-1]] and
[[prop:iii-i5-2-1]], holds at b by [[lem:s20-injective]].

(vi) *The v1 terms:* [[sec:iii-i9-1]] (𝒲_v1 = 𝒱′ = 0, kept at every b), [[lem:iii-i10-2-1]] and
[[prop:iii-i10-3-1]], [[lem:iii-i11-2-3]], [[sec:iii-i12-1]], [[lem:iii-i12-2-3]], [[lem:iii-i12-2-4]] and
[[thm:iii-i12-3-1]], and [[def:iii-i14-1-1]], [[def:iii-i14-1-3]] and Steps 2–3 and 4′ of the proof of
[[thm:iii-i14-3-1]]. These are [[sec:iii-i15-2]]: [[prop:iii-i15-2-2]], [[lem:iii-i15-2-4]], [[prop:iii-i15-2-5]],
[[lem:iii-i15-2-9]] and [[cor:iii-i15-2-10]]. At a rotating b, the rate of a v1 coefficient at z ([[def:iii-i14-1-1]],
[[lem:iii-i14-2-4]], and the construction of [[sec:iii-j-2]]) is at least Re z, and Re z + 1 on ker h_(b,v1), the
rotations commuting with the spin; only the lower bound is used. The a_v1 term in the proof of [[prop:iii-i5-2-1]] is
covered by [[lem:iii-i15-2-1]]: if present, its bottom a_ν h_(b,v1) has K⁺-weight Re λ₀ − ε ≥ Re λ₀ − 1, so the bound
used there survives.

(vii) *The time translation as a Killing field:* (P5).

(viii) *The data* ([[ch:s23]]). The base points U of [[ch:s23]] map by Φ to (h, p⃗, q) with parameter b
([[thm:iii-j-2-4]]), and the proofs there use [[thm:iii-i14-3-1]] and the maps of [[sec:iii-j-2]] at that base point,
by (i)–(vii). [[sec:iii-j-2]] builds its rows at b₀, and [[lem:iii-j-2-1]], [[lem:iii-j-2-2]], [[lem:iii-j-2-3]],
[[thm:iii-j-2-4]] and [[rem:iii-j-2-5]] hold as written at b ([[lem:iii-j-2-3]], the log count, has b-independent
exponents, log orders and index sets by (iii)), with the rows m^(b₀)_ν, the towers T_(ψ,b) and the corrections at b₀:
the rule of (P6), rows at b, is not applied there, and the pure gauge of [[rem:iii-j-2-6]] refers to g_(b₀). P_5 and
the coordinates W_ν do not depend on the convention ([[sec:s23-base-points]] (3)). [[lem:iii-j1-1-1]], whose proof
applies L̃_(b₀)(0)⁻¹, holds for the output of [[prop:iii-i15-2-5]]: at b its roots are those of (P2),
[[prop:iii-h-3-2]] holds by (P4), and neither A_b, which reads only ι⁺-data and level-1 tf-data ([[def:iii-i15-2-3]]),
nor E^ν, a fixed tensor ((P6)), depends on η_2.

(ix) *The boost column:* [[lem:iii-i4-2-4]], [[prop:iii-i4-4-1]] (2), [[cor:iii-i4-4-3]] and [[cor:iii-i5-2-2]] at b are
[[lem:iii-i15-2-7]] and [[prop:iii-i15-2-8]].

(x) *The parameter columns:* [[lem:iii-i7-2-4]] at b is [[lem:iii-i15-2-11]], and [[lem:iii-i7-4-3]],
[[lem:iii-i7-4-5]], [[cor:iii-i7-4-6]] and the base step of [[prop:iii-i8-4-1]] at b are [[prop:iii-i15-2-12]].

(xi) *The expansion:* [[lem:iii-i12-2-3]], [[lem:iii-i12-2-4]] and [[thm:iii-i12-3-1]] at b are [[lem:iii-i15-2-9]] and
[[cor:iii-i15-2-10]].

*The augmentation at b.* The results of [[ch:s23]] stated at b₀ use b₀ only as follows, and each use is supplied at b.

- [[sec:iii-i14-1]] and [[def:iii-i14-1-1]]–[[def:iii-i14-1-3]]: η_E = min Re ℰ_ind > 0, the inclusion
  ℰ_+ ⊃ (ℰ_♯ ∪ ℰ^♮) ∩ {Re < 3 + ε_+}, the sets ℰ^α_ψ and ℳ_rot are (iii) and (P3); the v1 rate Re z at a rotating b
  exceeds 2 + ε_K by (G), which does not depend on b; h_(b,rem), T_(ψ,b), h^(≤2)_(b,v1) and ġ_b are defined at b
  ((P3), (P6)); [[eq:iii-i14-1-3]] is defined at every b, so [[eq:iii-i14-1-4]] holds at b with h_(b,rem); at b,
  h_(b,rem)(q) is the χ_K u_exp of [[thm:iii-i12-3-1]] at b, with the towers T_(ψ,b) ([[cor:iii-i15-2-10]]); the
  corrections of the rotation rows are those of [[def:iii-i9-2-1]] at b₀ ((P6)); the rate of the rotation rows at b is
  [[lem:iii-i15-2-1]], and they become new rows ([[prop:iii-i15-2-5]]); [[thm:iii-i11-4-1]] is used only with the
  parameter in the non-rotation part of 𝒫, and v1 stays excluded from [[cor:iii-i10-2-3]] at b ([[rem:iii-i15-1-2]]);
  and f^ν = L m_ν + r^ν acquires E^ν ([[eq:iii-i15-1-1]]).
- [[lem:iii-i14-2-2]] (a), (c) and [[lem:iii-i14-2-3]]: the index sets are (P3), with the loss of (P4) absorbed by the
  orders "−"; h_(b,rem)(q) is real ((P3)); L_b h^(≤1)_(b,s1)(S) is computed by the stationarity of L_b ((P5)) and the
  tower relations at b ((P3)).
- [[lem:iii-i14-2-4]]: in (a), the corrections h_ν are built at b₀ and supported in 𝒞 ((P6)); in (b), g_0 depends on S
  only off χ_K, and ∂_S g_p⃗ ∈ ρ²C^∞ by [[lem:iii-i7-1-3]] at b; in (c), the derivative in b is taken at b, every
  coefficient of q having rate > 2 at every b ((iv)); ∂_b g_b has weight 2 ([[sec:iii-h-1]]), [[lem:iii-i7-2-2]] holds
  for every g_0, and the exponents of ∂_b h_(b,rem)(q) are those of [[lem:iii-i14-2-1]] ((P3)).
- [[lem:iii-i14-2-5]]: the thresholds, the roots and the tf-propositions [[prop:iii-g4-4-4]] and [[prop:iii-g4-5-1]]
  are (P2), (P4).
- [[thm:iii-i14-3-1]]: at b it is [[prop:iii-i15-2-5]]. Step 1 runs by (P1)–(P6) with E^ν ∈ 𝒴(α_1), and (iv) for the v1
  part; Step 2 by (P6) with E^ν; [[cor:iii-i10-2-3]] by [[lem:iii-i15-1-2]]; Step 3 by the direct bound; Step 4′ is not
  used ((v)); the v1 coefficient of q′ has no exponent in ℳ_rot by [[prop:iii-i15-2-5]] with the class of ũ in
  [[lem:iii-i15-2-4]]; and χ_K u_exp = h_(b,rem)(q′) with the towers T_(ψ,b) ((P6)). [[rem:iii-i14-3-2]] (2) does not
  involve b: the inputs at b use a_K only through strict inequalities.
- [[lem:iii-j1-1-1]] and [[thm:iii-j1-2-1]]: [[lem:iii-j1-1-1]] at b is as in (viii), its thresholds being on
  tf-exponents and so unaffected by the rate shift of [[prop:iii-i15-2-2]] (b), and the absence of indicial roots in
  (0, 1) being (P2). Step 0 of the proof of [[thm:iii-j1-2-1]] uses only the constructed map of [[prop:iii-i15-2-5]]
  ([[rem:iii-i15-2-6]]); h_(b,rem)(q′) takes the place of h_(b₀,rem)(q′), and of the rows m_ν only the rows at λ₀ enter,
  whose λ₀-terms do not depend on b ([[lem:iii-j-2-2]]); the order of [h′]_(λ₀) comes from u ∈ 𝒵_α
  ([[prop:iii-i15-2-5]]); the rates of q′ are below α ([[prop:iii-i15-2-5]], [[lem:iii-i15-2-4]]), the v1 part with
  Re z ≤ 3 by (G⁺); the independent injective leading terms of distinct rows are those of [[lem:iii-g2-1-2]] at the
  Minkowski model ((P2), (P3)); and the bounds of [[prop:iii-i15-2-5]] are uniform in b.

*The constants.* Every constant above is a finite combination of constants of (P1)–(P4) and (P6), of [[lem:iii-i15-1-2]],
of [[lem:iii-i15-2-1]], [[lem:iii-i15-2-4]], [[lem:iii-i15-2-7]], [[lem:iii-i15-2-9]] and [[lem:iii-i15-2-11]], of
[[prop:iii-i15-2-8]] and [[prop:iii-i15-2-12]], and of the maps of [[prop:iii-i15-2-2]], each uniform on ℬ̄_*. The
continuity statements ([[prop:iii-i8-4-1]] (ii) and [[lem:iii-i8-3-3]], [[lem:iii-i11-3-3]], [[lem:iii-i13-2-3]]) enter
[[lem:iii-i15-2-4]] at fixed b only and are not used for the bounds of the elimination. [[lem:iii-i4-4-2]] (b) and
[[lem:iii-i7-4-1]] are not used across b; the direct bounds of [[prop:iii-i15-2-8]] and [[prop:iii-i15-2-12]] replace
them. The smallness of the elimination, across b, comes from the direct bound of Step 3 of the proof of
[[prop:iii-i15-2-5]], through (P6) and [[def:iii-i15-2-3]]. ℬ_* is the ball of radius at most 1/(2C_B) of
[[lem:s25a-ball]] and [[lem:s20-rows]] (one ball: [[lem:s20-rows]] takes its C_B as a supremum over the ball of
[[lem:s25a-ball]], which is at most the C_B there, so its condition on the radius holds already), inside condition (B5)
of [[sec:iii-h2-0]], shrunk further so that the bound of [[lem:iii-i15-1-2]] holds and the maps −id + A_k of
[[prop:iii-i15-2-5]] are invertible on it. ∎

**Corollary {#cor:s25-tame}** (The tame and exact forms at b.) For base points with black hole parameter b ∈ ℬ̄_*, the
statements at b ([[def:s25-at-b]]) of the following hold, with constants, losses and smallness conditions uniform in
b:

- [[thm:iii-j2-4-1]], [[thm:iii-j2-4-2]] and [[prop:iii-j2-4-3]], the solution maps that [[thm:iii-j2-4-1]] estimates
  being, at a rotating b, those of [[prop:iii-i15-2-5]] and [[lem:iii-i15-2-4]];
- [[prop:iii-j3-3-4]], [[prop:iii-j3-4-3]], [[prop:iii-j3-4-6]], [[prop:iii-j3-5-2]], [[prop:iii-j3-5-4]],
  [[thm:iii-j3-5-3]], [[thm:iii-j3-5-5]] and [[cor:iii-j3-6-6]], [[thm:iii-j3-5-3]] in the form of
  [[prop:iii-i15-2-5]] at exact weights.

*Proof.* [[ch:s24]] states and proves these results at a base point with parameter b ∈ ℬ̄_*. Its proofs use, at b,
the model objects (P1)–(P6) ([[lem:iii-i15-1-1]], [[lem:s25-p6]]), [[lem:iii-i15-1-2]], [[sec:iii-i15-2]],
[[prop:iii-i2-5-1-b]], [[cor:iii-h2-5-1]], [[thm:iii-h2-2-1]], [[prop:iii-h2-1-1]] and [[cor:iii-h2-1-2]], the
results of [[ch:s20]]–[[ch:s22]] at b (among them [[prop:iii-i15-2-8]], [[prop:iii-i15-2-12]], [[lem:iii-i15-2-9]] and
[[cor:iii-i15-2-10]]), and the results of [[ch:s23]] at b, [[sec:s23-base-points]] (1)–(3). All of these hold on ℬ̄_*
with constants uniform in b: they are [[thm:iii-i15-3-1]] and the statements its proof rests on, and
[[thm:iii-h2-2-1]], [[prop:iii-h2-1-1]] and [[cor:iii-h2-1-2]] hold on ℬ̄_1 ⊃ ℬ̄_*, uniformly ((P4)). The following
records where a step of [[ch:s24]] uses a property of b₀ that a general b need not have, or an object built at b₀, and
what replaces it at b.

*The calculus, the classes and the inventory.* The tame calculus of [[ch:s24]] ([[def:iii-j2-1-1]]–[[lem:iii-j2-2-4]])
has constants that depend on the base point through finitely many seminorms, continuous in b, so bounded on the
compact ℬ̄_*; the exact classes and the conditions (Ex1)–(Ex4) and (A_K) of [[def:iii-j3-1-3]] do not involve b
((P2)–(P3): the exponents, roots and index sets are those at b₀), except that (Ex3), used also in (A_K), concerns the
K⁺-exponents at hand, among which at a rotating b are those of the v1 terms; (Ex3) at b is (Ex3) at b₀, by the
paragraph *(Ex3) at b* below. The solution maps of [[ch:s19]]–[[ch:s23]] in [[thm:iii-j2-4-1]] are read at b as in
[[lem:iii-i15-2-4]] and [[prop:iii-i15-2-5]]; in particular, at a rotating b the map of [[thm:iii-i14-3-1]] there is
the constructed map F ↦ (p⃗′, q′, h′) of [[prop:iii-i15-2-5]] ([[rem:iii-i15-2-6]]). The new objects enter the inventory
of [[lem:iii-j2-2-1]] (c): A_b is bounded by a fixed low seminorm of the right side f′ = G − (L_(h,p⃗) − L_b)u, from
which it reads the ι⁺-data u_+ and the tf-data ([[prop:iii-i15-2-2]]), so by fixed low seminorms of G and of the
solution u ([[def:iii-i15-2-3]]); E^ν is bounded by C|b − b₀||W| in a fixed seminorm ((P6)); the rotation rows
enter −id + A_k as the other rows do; and d_* includes their orders.

*(Ex3) at b.* At a rotating b the K⁺-exponents at hand are those at b₀ together with: the exponents λ + j, λ ∈ π_1ℳ_rot,
j ∈ ℕ₀, of the bottoms a_ν h_(b,v1)(W) of the rotation rows and their shifts ([[lem:iii-i15-2-1]], [[prop:iii-i15-2-2]]);
and the exponents z + j, j ∈ ℕ₀, of the v1 coefficients t_*^(−z) of q, whose rate is Re z at b and Re z + 1 at b₀
([[def:iii-i14-1-1]]), with z ∈ π_1ℰ_♯ and 2 < Re z < 3 + ε_+ < 4. All of these lie in Λ (π_1ℰ_♯ ⊂ Λ, [[sec:iii-i12-1]],
and Λ + 1 ⊂ Λ), so their real parts are at least λ_♯ ([[lem:iii-i10-1-2]] (a)). Since λ_♯ ∈ Λ ([[def:iii-i10-1-1]]), also
λ_♯ + 1 ∈ Λ, with real part above 2, so (G) gives λ_♯ + 1 > 2 + ε_K. For i ∈ {0, 1, 2}, α − 2 + i ∈ (2 + i, 2 + i + ε_K],
as α ∈ (4, 4 + ε_K]. Let λ ∈ π_1ℳ_rot, so Re λ ≤ 2, and j ∈ ℕ₀. If j ≤ i, then Re(λ + j) ≤ 2 + i < α − 2 + i; if
j ≥ i + 1, then Re(λ + j) ≥ λ_♯ + i + 1 > 2 + i + ε_K ≥ α − 2 + i. So no λ + j has real part α − 2, α − 1 or α. For the
v1 coefficients of q: by (G) no element of Λ has real part in (2, 2 + ε_K] ∪ (3, 3 + ε_K], which contain α − 2 and α − 1;
and Re(z + j) = α forces j ≥ 1, as Re z < 4 < α, so z + j = (z + 1) + (j − 1) is an exponent at hand at b₀, where (Ex3)
holds. So (Ex3) at b is (Ex3) at b₀.

*The losses, the smallness and the exact weights.* In [[lem:iii-j2-2-1]] (f), the loss at every order holds at b by
[[prop:iii-h2-1-1]], uniformly on ℬ̄_1, so the neighbourhood of b₀ does not shrink with the order. The continuity of
[[lem:iii-j2-2-3]] is read at b through [[lem:iii-i15-2-4]] at (0, p⃗_b) and the direct bound of [[prop:iii-i15-2-5]],
both in fixed seminorms, so d_* is unchanged; and [[thm:iii-j2-4-1]] at b takes its smallness δ_𝔹 at most the radius
of the final ℬ_* (*The constants* in the proof of [[thm:iii-i15-3-1]]). [[thm:iii-j3-5-3]] at b is
[[prop:iii-i15-2-5]] at the exact weights, as its proof shows: E^ν is exact there, A_b does not depend on the loss
([[rem:iii-i15-2-6]]), and the errors of the identification of the rotation rows have room. That proof cites Step 3 of
the proof of [[thm:iii-i14-3-1]] and its uniqueness, to identify the exact and the lossy solutions; at b, the
uniqueness of [[prop:iii-i15-2-5]] together with [[eq:iii-i15-2-2]] serves there ([[rem:iii-i15-2-6]]), A_b being the
same on both classes. In the proof of [[prop:iii-j3-4-6]] at b, the profiles of the level-3 towers are homogeneous of
degree d_ψ − j only in their leading parts, which do not depend on b ((P3)); the other terms are smaller by
min Re ℰ_ind ([[sec:iii-i12-1]]), so the profiles satisfy the bound |(r∂_r)^a ∂_ω^β p_j| ≲ r^(j−d_ψ) that
[[lem:iii-j3-4-7]] (a) asks. [[prop:iii-j3-3-4]] and [[prop:iii-j3-4-3]] carry the rotation rows of
[[prop:iii-i15-2-2]].

*The remaining results.* [[thm:iii-j2-4-2]] and [[thm:iii-j3-5-5]] apply [[thm:iii-j2-4-1]], respectively
[[thm:iii-j3-5-3]], at Φ(U), and then Steps 1–3 of the proof of [[thm:iii-j1-2-1]], which hold at b with the rows built
at b₀ and with [[lem:iii-j1-1-1]] for the output of [[prop:iii-i15-2-5]] (item (viii) of the proof of
[[thm:iii-i15-3-1]]); the black hole parameter of U is that of Φ(U) ([[def:iii-j-1-1]], [[thm:iii-j-2-4]]), so it lies
in ℬ_* for U small. [[prop:iii-j2-4-3]] and [[prop:iii-j3-5-4]] bound P_5 ∘ Φ through [[thm:iii-j-2-4]] and
[[eq:iii-j-2-5]], which hold at b by the same item, and through P_5(h, p⃗, q) = P_4(h + h_(b,rem)(q), p⃗), with
h_(b,rem) real and smooth in b ((P3)). [[prop:iii-j3-5-2]] uses h_(b,rem)(q) at b, the stationarity of L_b ((P5)), the
tower relations at b ((P3)) and the rates of the coefficients of q, which exceed 2 + ε_K at every b
([[def:iii-i14-1-1]] and (G)). [[cor:iii-j3-6-6]] composes the families of [[lem:iii-j2-2-1]] and the results above at
fixed weights; so it holds at b, with constants uniform in b, as the exact classes do not involve b. ∎

**Corollary {#cor:iii-i15-3-2}** (Right inverses at every base point.) [[thm:iii-j1-2-1]] and its tame and exact forms
([[thm:iii-j2-4-2]], [[cor:iii-j3-6-6]]) hold at every base point U ∈ 𝒟^∞ small in 𝒟^d, a point of the data space of
[[def:iii-j-1-1]] whose black hole parameter, that of Φ(U) ([[thm:iii-j-2-4]]), lies in ℬ_*, which the smallness of U in
𝒟^d ensures, with constants uniform in U; at a rotating b the right inverse is the one constructed by
[[prop:iii-i15-2-5]]. These are the right inverses that [[thm:ii-g-2-1]] (iii) asks for at every point of its
neighbourhood.

*Proof.* The black hole parameter of U is one of its components ([[def:iii-j-1-1]]) and is that of Φ(U)
([[thm:iii-j-2-4]]), so b ∈ ℬ_* for U small in 𝒟^d. At such U, [[thm:iii-j1-2-1]] holds in its statement at b by
[[thm:iii-i15-3-1]], and [[thm:iii-j2-4-2]] and [[cor:iii-j3-6-6]] hold in their statements at b by [[cor:s25-tame]],
with constants uniform in b; at a rotating b the solution map used in Step 0 of the proof of [[thm:iii-j1-2-1]] is that
of [[prop:iii-i15-2-5]] ([[rem:iii-i15-2-6]]). ∎
