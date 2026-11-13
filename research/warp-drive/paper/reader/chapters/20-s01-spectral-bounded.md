# Part. The stability theory, I: the spectral family on bundles {#part:stability}

## The spectral family at bounded nonzero frequencies {#ch:s01}

This chapter proves the Fredholm theory of the stationary spectral family on a trivial vector bundle over the exterior
of a black hole in dimension 4 + 1, at bounded real frequencies σ ≠ 0 and in the closed upper half plane near them. The
main result, [[thm:i-a-7-2]], is [Hin26c, Theorem 9.5] in dimension 4 + 1, for operators on a trivial bundle of any
rank and for a constant regularity order ([[rem:i-a-1-1]]). The spectral family is Fredholm between spaces of variable
decay order; its kernel and the annihilator of its range do not depend on the admissible orders; its index does not
depend on σ; its kernel elements are conormal at infinity with an explicit leading term; and its inverse, where it
exists, is regular in σ. Two changes are forced by the dimension: the term −(n − 1)/2 of the operator at infinity is
−3/2, and the weights 1 + S̄ and ρ^(1+S) of [Hin26c, (9.20)–(9.21)], which are their values at n = 3, are 3/2 + S̄ and
ρ^(3/2+S). A third change concerns the sign of a term in [Hin26c, (9.45)] ([[lem:i-a-4-8]]). Of the expansion
[Hin26c, (9.21)] the first step is proved ([[thm:i-a-7-2]] (5)). [[thm:i-a-8-1]] makes the constants uniform under
continuous perturbations of the operator.

The hypotheses (H1)–(H5) of [[sec:i-a-1-3]] are stated for the spectral family alone; every later chapter that uses
these results instantiates them. [[sec:i-a-2]] states the calculus. [[sec:i-a-3]] proves the one positive commutator
lemma used throughout, with its regularisation. [[sec:i-a-4]] proves the three radial point estimates and the
commutator lemma for b-regularity, [[sec:i-a-5]] the elliptic and propagation estimates, and [[sec:i-a-6]] the
estimates near an artificial boundary inside the horizon. [[sec:i-a-7]] proves the theorem and [[sec:i-a-8]] its
uniformity in the operator.

### Setting and hypotheses {#sec:i-a-1}

#### The space {#sec:i-a-1-1}

Let ℝ̄⁴ be the radial compactification of ℝ⁴, with boundary ∂ℝ̄⁴ ≅ 𝕊³. Near it we use ρ = |x|⁻¹ and ω = x/|x| ∈ 𝕊³,
so that a neighbourhood of the boundary is [0, ρ₁)_ρ × 𝕊³_ω. Fix radii 0 < r₀ − 2δ₀ < r₀ < r₀ + δ₀ < r₂ < r_h and set

    X̄ := {x : |x| ≥ r₀} ∪ ∂ℝ̄⁴,     ∂X := ∂ℝ̄⁴,     ∂_♯X := {|x| = r₀},     X̃ := {|x| > r₀ − 2δ₀} ∪ ∂X.

Write r := |x|. The radius r_h is that of the horizon in (H3), and ∂_♯X is the artificial boundary. All operators below
are defined on X̃. Every function space on X̄ is built from a space on ℝ⁴ through the extendible and supported
constructions at ∂_♯X of [[sec:i-a-6-1]], and every Schwartz kernel used has support in X̃ × X̃. The density is the
Euclidean one, |dx| = r³ dr dω = ρ⁻⁵ dρ dω near ∂X, where dω is the round density on 𝕊³.

The radii, and in particular the inner radius r₀ of the artificial boundary, are parameters. The results of this
chapter hold for every choice of them for which the hypotheses below hold, with constants that depend on the choice;
the cut-offs and dilations used near ∂_♯X ([[sec:i-a-6-1]]) are taken in proportion to r₀. The radii used for the
Myers–Perry metrics are fixed in [[ch:s12]].

The condition r₀ + δ₀ < r₂ costs nothing. Decreasing δ₀ shrinks X̃, on which (H1)–(H3) below continue to hold; it
leaves X̄ and every space below unchanged; and it only weakens (H4) and (H5): the region of (H4) on which G₀ is
Lorentzian shrinks, the set {r < r₀ − δ₀} that the curves of (H4) must reach grows, and the parameters at which they
reach it, bounded in (H5), can only decrease. So radii with 0 < r₀ − 2δ₀ < r₀ < r₂ < r_h for which (H1)–(H5) hold
satisfy the ordering above once δ₀ is replaced by min(δ₀, (r₂ − r₀)/2). The condition is used in
[[cor:i-a-6-5]], where it makes room for the radii b′ < b″ in (r₀, r₂ − δ₀).

#### The bundle {#sec:i-a-1-2}

Let E := X̃ × ℂ^N, N ≥ 1. The bundles of the later chapters are the restrictions to X̃ of T∗M and S²T∗M, for a
five-dimensional spacetime M, trivialised by dt_*, dx¹, …, dx⁴ and their symmetric products, with N = 5 and N = 15;
nothing below uses more than that E is trivial. (The letter N also denotes Sobolev orders, as in H^(−N), and in
[[sec:i-a-7-5]] it bounds a nilpotency index; the context separates them.) A *fibre inner product* is
h(x)(v, w) = ⟨H(x)v, w⟩_(ℂ^N), where H ∈ C^∞(ℝ̄⁴; End ℂ^N) is Hermitian, smooth on the compactification (that is,
smooth in (ρ, ω) up to ρ = 0), and satisfies c Id ≤ H ≤ C Id with c > 0. Let L²_h := L²(ℝ⁴; ℂ^N) with the norm
‖u‖²_h = ∫ h(u, u) |dx|, which is equivalent to the standard one. For an operator A, A^(∗h) = H⁻¹A∗H is its formal
adjoint in L²_h, and A∗ its adjoint in the standard L². We write Re_h A := ½(A + A^(∗h)) and
Im_h A := (A − A^(∗h))/2i.

#### The operator {#sec:i-a-1-3}

Let ℂ ∋ σ ↦ P̂(σ) ∈ Diff²(X̃°; E) be of the form

    P̂(σ) = P̂(0) + σT + σ²P₂.                                                                         {#eq:i-a-1-1}

This is the form of the spectral family e^(iσt_*) P₀ e^(−iσt_*) of a t_*-translation-invariant second-order operator
P₀, with T = −i[P₀, t_*] and P₂ of order 0 (compare [Hin26c, (9.30)]). For an operator A, σ_m(A) or σ(A) denotes its
principal symbol, of order m; σ₀ and σ₁, written without an argument, are the real and imaginary parts of the spectral
parameter, σ = σ₀ + iσ₁. The hypotheses are these.

(H1) (*Principal symbol.*) σ_2(P̂(0)) = G₀ Id, where G₀ ∈ C^∞(T∗X̃°) is real, fibrewise quadratic and even in the
fibres, and σ_1(T) = τ₁ Id with τ₁ real and fibre-linear. P₂ = g₀₀ Id with g₀₀ a real function.

(H2) (*Structure at infinity*; [Hin26c, Definition 9.4 and (9.31)] at n = 4.) On {ρ < ρ₁},

    T = 2iρ(ρ∂_ρ − 3/2 − S) − iQ,     P̂(0) = ρ²P^(0),     g₀₀ ∈ ρ²C^∞(ℝ̄⁴),                             {#eq:i-a-1-2}

where S ∈ C^∞(ℝ̄⁴; End ℂ^N), Q ∈ ρ³Diff¹_b, and P^(0) ∈ Diff²_b with
P^(0) − ((ρD_ρ)² + Δ_(𝕊³)) Id ∈ Diff¹_b + ρ Diff²_b. All b-operators here have End ℂ^N-valued coefficients smooth on
the compactification, D = −i∂, and Δ_(𝕊³) ≥ 0 is the Laplacian of the round metric. The first equation in
[[eq:i-a-1-2]] is the form that the term −(n − 1)/2 of [Hin26c, (9.31)] takes at n = 4. Set

    S̄ := inf_(p ∈ ∂X) min Re spec S(0, p)     ([Hin26c, (5.2)]).

(H3) (*The horizon*; [Hin26c, Section 9.2.1, (1)–(4)].) Let ℋ := {r = r_h}. ℛ₊ is one of the two components of
N∗ℋ ∖ o, and ℛ₋ := −ℛ₊; both lie in Σ₀ := {G₀ = 0}. Let ρ_∞ be positive, homogeneous of degree −1 and even near N∗ℋ.
The *future-directed rescaled Hamilton vector field* on Σ₀ is 𝖧 := ±ρ_∞H_(G₀) on the component Σ₀^± containing ℛ_±.
Then for each sign

    β₀ := ρ_∞⁻¹𝖧ρ_∞ > 0 on ∂ℛ_±,     β := inf_(∂ℛ_±) (∓β₀⁻¹ρ_∞τ₁) > 0,                                 {#eq:i-a-1-3}

and there is a quadratic defining function q_± of ∂ℛ_± in ∂Σ₀ with 𝖧q_± ≥ c q_± near ∂ℛ_±, for some c > 0. Here ∂(·)
denotes the boundary at fibre infinity, viewed in S∗X̃°. For the spectral family of a t_*-translation-invariant
operator, ∓ρ_∞τ₁ = 𝖧t_*, since τ₁ = −H_G t_* [Hin26c, (9.30)]; so the second condition is the condition β > 0 of
[Hin26c].

(H4) (*Dynamics at fibre infinity.*) ∂Σ₀ = ∂Σ₀⁺ ⊔ ∂Σ₀⁻ lies over {r ≤ r_e} for some r_e > r_h. Every maximal integral
curve of 𝖧 in ∂Σ₀ ∖ (∂ℛ₊ ∪ ∂ℛ₋) tends to ∂ℛ₊ ∪ ∂ℛ₋ as its parameter tends to −∞, and reaches {r < r₀ − δ₀} at a
finite positive parameter. On {r₀ − 2δ₀ < r < r₂}, G₀ is a Lorentzian form (signature (1, 3)) on each fibre of T∗X̃,
dr is timelike for it (G₀(dr) < 0), and 𝖧r < 0 on ∂Σ₀ there: the future direction decreases r. (For a spectral family,
G₀ is g⁻¹ restricted to the annihilator of ∂_(t_*), and such a restriction of a Lorentzian form is Lorentzian wherever
it contains a timelike covector, as dr is inside the horizon.)

(H5) (*Uniformity data.*) P̂ may depend on a parameter b in a compact metric space ℬ, continuously into the
coefficient topology (every coefficient continuous in b into C^∞, and in the classes of (H2)). The objects ℋ, ρ_∞,
q_± and r_e in (H3)–(H4) may depend continuously on b, and the constants c, inf β₀ and β in (H3) and the lengths of
the curves in (H4) are bounded uniformly. [[sec:i-a-8]] uses (H5).

**Remark {#rem:i-a-hypotheses}** (On the hypotheses.) (a) By (H1) the principal symbol of P̂(σ), of order 2, is G₀ Id
for every σ. Since P̂(0) − P̂(0)^(∗h) has vanishing principal symbol, Im_h P̂(0) ∈ Diff¹, and near ∂X it lies in
ρ²Diff¹_b. Indeed P̂(0) ∈ ρ²Diff²_b by [[eq:i-a-1-2]], adjoints preserve ρ²Diff²_b for the density ρ⁻⁵dρ dω (the
adjoint of a b-vector field is a b-operator), and the b-principal symbols cancel.

(b) By (H1), for σ ∈ ℂ,

    σ_1(Im_h P̂(σ)) = σ_1(Im_h P̂(0)) + (Im σ) τ₁ Id.                                                  {#eq:i-a-1-4}

To see this, write Im_h(σT) = (σT − σ̄T^(∗h))/2i = (Re σ) Im_h T + (Im σ) Re_h T. Then Im_h T has order 0,
σ_1(Re_h T) = τ₁ Id, and σ²P₂ has order 0.

(c) (H3)–(H4) are the hypotheses of [Hin26c, Section 9.2.1] and the dynamics of [Hin26c, Section 9.1.1]. For the
operators of the later chapters, on the Schwarzschild–Tangherlini metric and the Myers–Perry metrics near it, the
dynamics in (H3)–(H4) is verified in [[ch:s12]], and the horizon threshold ϑ_ℋ of [[sec:i-a-1-4]] is evaluated where
each operator is studied ([[ch:s13]], [[ch:s14]]).

(d) P̂(σ)^(∗h) satisfies (H1)–(H4) as well, with τ₁, S and Q replaced by τ₁, −S^(∗h) and a suitable Q′, and with σ
replaced by σ̄. Only its principal symbol and its imaginary part enter below, and they are determined where they are
used.

#### Orders and thresholds {#sec:i-a-1-4}

The phase space is the scattering cotangent bundle ^(sc)T̄∗ℝ̄⁴, compactified in the fibres. Its boundary consists of
*fibre infinity*, ^(sc)S∗ℝ̄⁴, and the *boundary face* ^(sc)T̄∗_(∂X)ℝ̄⁴ over ∂X, meeting at a corner. Near ∂X we write
scattering covectors as ξ dr + r η, with ξ ∈ ℝ and η ∈ T∗𝕊³, so that (ρ, ω, ξ, η) are coordinates
([Hin26c, Section 9.2.2]; ξ and η are the ξ_sc and η_sc of [Hin26c]). For an h-self-adjoint endomorphism A, max spec A
and min spec A denote its largest and smallest eigenvalues.

**Definition {#def:i-a-admissible}** (Admissible orders.) An *order pair* is (s, 𝗋) with s ∈ ℝ a constant
(regularity; [[rem:i-a-1-1]]) and 𝗋 ∈ C^∞(^(sc)T̄∗_(∂X)ℝ̄⁴) (decay), each extended smoothly to a neighbourhood of its
face. For real σ₀ ≠ 0 it is *admissible for* σ₀ with weight α₊ ∈ ℝ if:

(O1) s = s_c, a constant ([[rem:i-a-1-1]]);

(O2) 𝗋 is constant near R_(σ₀,in) and near R_out (defined in [[eq:i-a-4-6]]), and on the characteristic set Σ^∂_(σ₀)
of [[eq:i-a-4-7]] it is monotone non-increasing along the future-directed flow (sgn(σ₀) 𝖧_(σ₀)𝗋 ≤ 0, in the notation
of [[sec:i-a-4-2]]);

(O3) the thresholds [Hin26c, (9.16a)–(9.16c)] hold with respect to some fibre inner products, chosen separately for
each radial set ([[sec:i-a-2-3]]):

    s_c > 1/2 + ϑ_ℋ,     𝗋 + α₊ > (−1 + ϑ_in)/2 at R_(σ₀,in),     𝗋 + α₊ < −1/2 + S̄ at R_out.         {#eq:i-a-1-5}

Here

    ϑ_ℋ := max_± sup_(∂ℛ_±) max spec(β₀⁻¹ p_(1,±)(0)),     p_(1,±)(σ) := ±ρ_∞ σ_1(Im_h P̂(σ)),

where p_(1,±)(σ) is an h-self-adjoint endomorphism; this is [Hin26c, (5.17)] ([[rem:i-a-4-3]]). Next,

    ϑ_in := sup_(∂X) max spec(p_in − (S + S^(∗h))),     p_in := σ(ρ⁻¹ Im_h P̂(0))|_(ξ = −2, η = 0)

([Hin26c, (9.32), (9.38b)]; [[prop:i-a-4-6]]). For complex σ = σ₀ + iσ₁ the orders used are those for σ₀.

The spaces are those of [Hin26c, Theorem 9.5]:

    H̄^(s,𝗋) := H̄^(s,𝗋)_sc(X̄; E),     Ḣ^(s,𝗋) := Ḣ^(s,𝗋)_sc(X̄; E),

extendible, respectively supported, at ∂_♯X ([[sec:i-a-6-1]]), built componentwise from the scattering Sobolev spaces
of [HJS, Definition 10.2] on ℝ⁴ (constant regularity order, variable decay order).

**Remark {#rem:i-a-1-1}** (Constant regularity order.) [Hin26c] lets the regularity order vary at fibre infinity over a
region {r > r_Γ}, r_Γ > r_e, where P̂(σ) is elliptic. The calculus of [HJS] used here takes the differential order
constant ([HJS, p. 77]: "we will take the differential order to be constant, and the spatial order to be variable"),
and every proof below uses only s ≡ s_c, so [[thm:i-a-7-2]] is stated and proved for constant s. The semiclassical
calculus of [[ch:s02]] has variable orders in all three senses; with the semiclassical parameter equal to 1 it supplies
the elliptic estimate at a variable s over {r > r_Γ}.

### The calculus {#sec:i-a-2}

#### The statements used {#sec:i-a-2-1}

The following statements of [HJS] are used as black boxes. They are stated in [HJS] on ℝⁿ for every n, so they hold at
n = 4; page numbers are those printed in [HJS]. Every operator below has Schwartz kernel supported in X̃ × X̃, and
X̄ ⊂ ℝ̄⁴, so the calculus on ℝ⁴ is the calculus used.

(C1) (Composition, [HJS, (2.1), p. 9]; principal symbol, [HJS, pp. 49–50].) Ψ^(m,ℓ)_sc ∘ Ψ^(m′,ℓ′)_sc ⊂
Ψ^(m+m′,ℓ+ℓ′)_sc. By [HJS, Proposition 7.4], "A ∈ Ψ^(m,l)_sc(M) ⇒ A∗ ∈ Ψ^(m,l)_sc(M)", and
"σ_(m₁+m₂,l₁+l₂)(AB) = σ_(m₁,l₁)(A) σ_(m₂,l₂)(B)" [HJS, (7.29)], the principal symbol taking values in
S^(m,l)_sc/S^(m−1,l−1)_sc [HJS, Definition 7.2].

(C2) (Commutators, [HJS, Proposition 7.5, p. 50].) "[A, B] ∈ Ψ^(m₁+m₂−1,l₁+l₂−1)_sc(M) and
σ(i[A, B]) = {σ(A), σ(B)}", the Poisson bracket being H_p a, with the scattering Hamilton vector field of
[HJS, (7.34)].

(C3) (Boundedness, [HJS, Proposition 3.11 and Remark 3.12, p. 20].) "If A ∈ Ψ^(m,l)_sc, then, for all s, r ∈ ℝ, A maps
A : H^(s,r)_sc → H^(s−m,r−l)_sc … and does so boundedly"; and "Op(a), viewed as an element of
L(H^(s,r)_sc, H^(s−m,r−l)_sc), depends continuously on a". Since a ↦ Op(a) is linear and continuous from the Fréchet
space S^(m,l)_sc to a Banach space, it is bounded by one seminorm: a family bounded in Ψ^(m,l) is uniformly bounded
H^(s,r) → H^(s−m,r−l).

(C4) (Compactness, [HJS, Proposition 3.13, p. 20]; duality, [HJS, Proposition 3.7, p. 19].) "For any s, s′, r, r′,
with s < s′ and r < r′, the embedding H^(s′,r′)_sc ↪ H^(s,r)_sc is compact." The L² pairing identifies (H^(s,r)_sc)∗
with H^(−s,−r)_sc.

(C5) (Ellipticity, [HJS, Propositions 2.3, 4.9, 4.10 and 10.1, pp. 12, 27–29, 79].) "Every elliptic element of the
scattering calculus has a parametrix" (Proposition 2.3). There is a microlocal parametrix at a closed subset of the
elliptic set (Proposition 4.10: "AB − 1, BA − 1 have WF′_sc disjoint from p. This also applies with p replaced by any
closed subset"), also for variable orders (Proposition 10.1). Microlocality (Proposition 4.9):
"WF^(s,r)_sc(Au) ⊆ WF^(s+m,r+l)_sc(u) ∩ WF′_sc(A)".

(C6) (Variable orders, [HJS, Sections 10.1–10.3, pp. 77–80].) The symbol classes S^(m,l)_sc with l variable are defined
with the vector fields ⟨x⟩^(−δ)𝒱_b [HJS, (10.3)–(10.4)], so that "the logarithmic factor" in derivatives of
⟨x⟩^(l(x,ξ)) costs an arbitrary δ > 0; composition and the principal symbol are as in [HJS, Section 10.2]; and the
spaces [HJS, Definition 10.2 and Section 10.3] are independent of the choices and Hilbert, with Ψ^(m,l)_sc bounded on
them.

(C7) (Bundles, [HJS, Section 7.5, pp. 52–53].) "Ψ^(m,l)_sc(M; E, F) := C^∞(X; Hom(E, F)) ⊗ Ψ^(m,l)_sc(M) …
Equivalently, an element in Ψ^(m,l)_sc(M; E, F) is a matrix with entries in Ψ^(m,l)_sc(M)."

(C8) (A regularising family, [HJS, Lemma 12.5, p. 95].) T_t := χ(t⟨z⟩) Op(χ(⟨tζ⟩)) ∈ Ψ^(−∞,−∞)_sc, t ∈ (0, t₀], with
T_t → Id strongly on each H^(s,r)_sc; the proof of [HJS, Lemma 12.5] records "T_r being uniformly bounded in
Ψ^(0,0)_sc and T_r → Id in the operator topology of Ψ^(δ,δ)_sc".

In the interior, at fibre infinity, the scattering calculus restricted to kernels supported in a compact set is the
classical calculus, and the scattering principal symbol there is the classical one: over a compact set ⟨x⟩ is bounded
above and below, so the scattering estimates of order (m, ℓ) for symbols supported over it are the Kohn–Nirenberg
estimates of order m.

#### Matrix-valued operators {#sec:i-a-2-2}

Write Ψ^(m,ℓ) := Ψ^(m,ℓ)_sc(ℝ⁴; ℂ^N) = M_N(Ψ^(m,ℓ)_sc(ℝ⁴)), by (C7), and H^(s,𝗋) := (H^(s,𝗋)_sc)^N. The principal
symbol of A = (A_ij) is the matrix (σ(A_ij)).

**Lemma {#lem:i-a-2-1}** (Matrix-valued operators.) (a) Ψ^(m,ℓ) ∘ Ψ^(m′,ℓ′) ⊂ Ψ^(m+m′,ℓ+ℓ′) and σ(AB) = σ(A)σ(B), a
matrix product.

(b) For a fibre inner product h, A^(∗h) ∈ Ψ^(m,ℓ) and σ(A^(∗h)) = σ(A)^(∗h) := H⁻¹σ(A)^†H.

(c) If A = ã Id with ã ∈ Ψ^(m,ℓ)_sc scalar, and B ∈ Ψ^(m′,ℓ′), then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) and
σ(i[A, B]) = H_a σ(B), entrywise. If A ∈ Ψ^(m,ℓ) has scalar principal symbol a Id, and B has scalar principal symbol
b Id, then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) and σ(i[A, B]) = (H_a b) Id. More generally, if A has scalar principal symbol,
then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) for every B ∈ Ψ^(m′,ℓ′): write A = ã Id + A′ with A′ ∈ Ψ^(m−1,ℓ−1) and use the first
statement and (a). This is what is meant below when a commutator with an operator of scalar principal symbol lowers
both orders.

(d) The statements (C3)–(C6) and (C8) hold for Ψ^(m,ℓ) and H^(s,𝗋), with T_t Id in (C8), ellipticity meaning that the
principal symbol is invertible with inverse bounded in the inverse orders.

*Proof.* (a) (AB)_ij = Σ_k A_ik B_kj, with (C1) entrywise. (b) (A∗)_ij = (A_ji)∗, so σ(A∗) = σ(A)^† by (C1).
Multiplication by H or H⁻¹ lies in Ψ^(0,0): a function smooth on ℝ̄⁴ is a symbol of order (0, 0), its x-derivatives of
order k being O(⟨x⟩^(−k)). Then (a) gives (b). (c) [ã Id, B]_ij = [ã, B_ij], with (C2). For the second statement
write A = ã Id + A′ and B = b̃ Id + B′, with A′ ∈ Ψ^(m−1,ℓ−1) and B′ ∈ Ψ^(m′−1,ℓ′−1). Then
[A′, B′] ∈ Ψ^(m+m′−2,ℓ+ℓ′−2) by (a); [ã Id, B′] and [A′, b̃ Id] lie there by the first statement; and [ã, b̃] gives
H_a b. (d) Boundedness, compactness and duality are statements about each entry. For an elliptic A, take
B₀ := Op(σ(A)⁻¹χ) for a cut-off χ, and run the Neumann series of [HJS, Proposition 2.3] with matrices: AB₀ = Id − R₁,
R₁ ∈ Ψ^(−1,−1) by (a), and the asymptotic sum Σ_j R₁^j exists entrywise. The microlocal versions are identical. ∎

**Lemma {#lem:i-a-2-2}** (Square roots.) Let 𝒦 be a compact set of h-self-adjoint endomorphisms with spectra in
[c, ∞), c > 0. Then Q ↦ Q^(1/2), the h-positive square root, is real-analytic on a neighbourhood of 𝒦 in End ℂ^N, with

    Q^(1/2) = (2πi)⁻¹ ∮_γ z^(1/2) (z − Q)⁻¹ dz,

γ a fixed contour in {Re z > 0} around [c/2, C]. Consequently, if q is an h-self-adjoint symbol in a bounded family in
S^(2μ,2ν) (possibly with variable orders), with q ≥ c⟨ξ⟩^(2μ)⟨x⟩^(2ν) on a set W of phase space, then on W, q^(1/2) is
an h-self-adjoint symbol, bounded in S^(μ,ν), and (q^(1/2))² = q.

*Proof.* The integral is Q^(1/2) for Q h-self-adjoint with spectrum inside γ: diagonalise Q in an h-orthonormal basis
and use Cauchy's formula. It is holomorphic in the entries of Q wherever γ avoids spec Q. For the symbols, set
Λ := ⟨ξ⟩^μ⟨x⟩^ν (or the variable-order elliptic weight of (C6)), so q^(1/2) = Λ(Λ⁻²q)^(1/2). Here Λ⁻²q is bounded in
S^(0,0) with values in a compact set of positive matrices; the chain rule gives the symbol estimates of (Λ⁻²q)^(1/2),
and the product rule those of q^(1/2). ∎

**Lemma {#lem:i-a-2-3}** (Microlocal square root.) Let K = K^(∗h) ∈ Ψ^(2μ,2ν) have principal symbol k with
k ≥ c⟨ξ⟩^(2μ)⟨x⟩^(2ν) on a neighbourhood W of a closed set W₀ of the boundary of phase space. Then there is
L ∈ Ψ^(μ,ν) with WF′(K − L^(∗h)L) ∩ W₀ = ∅. The construction depends continuously on K, and so is uniform for bounded
families with a uniform c.

*Proof.* Let χ ∈ C^∞ equal 1 near W₀ with support in W. Set L₀ := Op(χk^(1/2)), by [[lem:i-a-2-2]], and replace it by
(L₀ + L₀^(∗h))/2. Then K − L₀^(∗h)L₀ is h-self-adjoint, and by [[lem:i-a-2-1]] it lies in Ψ^(2μ−1,2ν−1) microlocally
near W₀, with h-self-adjoint principal symbol k₁. Given L₀, …, L_(j−1) with
K − (Σ_(i<j) L_i)^(∗h)(Σ_(i<j) L_i) ∈ Ψ^(2μ−j,2ν−j) near W₀, of principal symbol k_j, solve
k^(1/2)l_j + l_j k^(1/2) = k_j for l_j. This Lyapunov equation has a unique solution, which is h-self-adjoint, given by

    l_j = ∫_0^∞ e^(−τk^(1/2)) k_j e^(−τk^(1/2)) dτ,

because k^(1/2) ≥ c^(1/2) on W; it lies in S^(μ−j,ν−j) by the chain rule. With L_j := Op(χl_j), the error drops one
order near W₀. Then L ∼ Σ_j L_j (asymptotic sum, (C1)). ∎

#### Inner products near ∂X {#sec:i-a-2-3}

**Lemma {#lem:i-a-2-4}** (Adapted fibre inner products.) For every ε > 0 there is a fibre inner product h such that
½ min spec(S + S^(∗h)) ≥ S̄ − ε at every point of ∂X.

This is [Hin26c, Lemma 5.12] in dimension 4 + 1.

*Proof.* At one point p, let S(0, p) = V(D + J)V⁻¹ with D diagonal, Re D ≥ S̄ and J nilpotent upper triangular in
Jordan form. Let D_t := diag(1, t, t², …). Then D_t⁻¹(D + J)D_t = D + tJ, with ‖tJ‖ ≤ t. In the inner product
⟨u, v⟩_t := ⟨D_t⁻¹V⁻¹u, D_t⁻¹V⁻¹v⟩, S(0, p) is unitarily equivalent to D + tJ, so Re⟨Su, u⟩_t ≥ (S̄ − t)|u|²_t. Take
t = ε/2. The inequality Re h(Su, u) ≥ (S̄ − ε) h(u, u) is open in p, so it holds for this constant inner product on a
neighbourhood of p. It is also convex in h: if it holds for h₁, …, h_k, it holds for Σ χ_i h_i with χ_i ≥ 0 and
Σ χ_i = 1. Cover ∂X by finitely many such neighbourhoods, take a subordinate partition of unity, and extend the
resulting inner product smoothly to ℝ̄⁴. Since ½ min spec(S + S^(∗h)) = min_(h(u,u)=1) Re h(Su, u), this is the claim.
∎

Different estimates below use different fibre inner products. All L²_h norms are equivalent, so each estimate proved in
one inner product holds in any other with a changed constant. No single inner product needs to serve two radial sets.

### The positive commutator lemma {#sec:i-a-3}

Orders are pairs 𝐬 = (s, 𝗋), the decay order possibly variable (C6), with 𝟏 := (1, 1) and 𝐍 := (N, N). Inequalities
between orders hold componentwise and pointwise. For an operator family, *microsupported in K uniformly* means that the
full symbols are supported in the closed set K, modulo a family bounded in Ψ^(−∞,−∞). For a fibre inner product h and
P ∈ Ψ^𝐦, write

    P_R := Re_h P = ½(P + P^(∗h)),     P_I := Im_h P = (P − P^(∗h))/2i.

**Lemma {#lem:i-a-3-1}** (One step.) Let P ∈ Ψ^𝐦, let 𝐬 be an order, 𝐤 := 𝐬 − ½(𝐦 − 𝟏), and κ ∈ (0, ½]. Let K₁ ⊂ U
with K₁ closed and U open in the boundary of phase space, and let G ∈ Ψ^(0,0) be elliptic on Ū. Suppose that for
ε ∈ (0, 1] there are the following.

(i) Ǎ_ε = Ǎ_ε^(∗h), bounded in Ψ^𝐤, in Ψ^(𝐤−κ𝟏) for each ε, and microsupported in K₁ uniformly.

(ii) For a sign ς ∈ {1, −1}, the operator C_ε := i[P_R, Ǎ_ε²] + Ǎ_ε²P_I + P_IǍ_ε² satisfies

    ςC_ε = −B_ε^(∗h)B_ε − F_ε + E_ε^(∗h)E_ε + J_εP + R_ε.                                              {#eq:i-a-3-1}

The operators in [[eq:i-a-3-1]] are as follows. B_ε is bounded in Ψ^𝐬, lies in Ψ^(𝐬−κ𝟏) for each ε, and converges to
B₀ in Ψ^(𝐬+δ𝟏) for every δ > 0. Ǎ_ε = Z_εB_ε + Y_ε, with Z_ε bounded in Ψ^(−½(𝐦−𝟏)) and Y_ε bounded in Ψ^(𝐤−𝟏).
⟨F_εw, w⟩_h ≥ −C_F‖w‖²_(−𝐍) for every Schwartz w (F_ε is never paired with u itself, so it may have any order). E_ε
is bounded in Ψ^𝐬 and lies in Ψ^(𝐬−κ𝟏) for each ε, J_ε lies in Ψ^(2𝐬−𝐦), and R_ε in Ψ^(2𝐬−𝟏). All of these are
microsupported in K₁ uniformly, E_ε in a closed set K_E, and J_ε in a closed set K_J ⊂ Ell(P).

Let E ∈ Ψ^(0,0) be elliptic on K_E. Then there is C such that for every u ∈ H^(−𝐍) with Gu ∈ H^(𝐬−κ𝟏),
GPu ∈ H^(𝐬−𝐦+𝟏) and Eu ∈ H^𝐬, we have B₀u ∈ L² and

    ‖B₀u‖² ≤ C(‖GPu‖²_(𝐬−𝐦+𝟏) + ‖Eu‖²_𝐬 + ‖Gu‖²_(𝐬−½𝟏) + ‖u‖²_(−𝐍)).                                   {#eq:i-a-3-2}

C depends only on C_F, on bounds for the families in their classes, and on finitely many seminorms of P, G and E.

*Proof.* Norms are those of L²_h and of H^𝐭 (any fixed choice, (C6)); C changes from line to line.

*Step 0: microlocalisation.* By (C5) there is Φ ∈ Ψ^(0,0) with WF′(Φ) ⊂ Ell(G) and
WF′(Id − Φ) ∩ (K₁ ∪ K_E ∪ K_J) = ∅. Let v := Φu. The microlocal parametrix of G gives

    ‖v‖_𝐭 ≤ C(‖Gu‖_𝐭 + ‖u‖_(−𝐍))  (𝐭 ≤ 𝐬 − κ𝟏),     ‖ΦPu‖_(𝐬−𝐦+𝟏) ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖u‖_(−𝐍)),

and Pv = ΦPu + [P, Φ]u. Here WF′([P, Φ]) ⊂ WF′(Id − Φ), which is disjoint from K₁. So if W_ε is any family bounded in
some Ψ^𝐭 and microsupported in K₁ uniformly, then W_ε[P, Φ] and W_ε(Id − Φ) are bounded in Ψ^(−∞,−∞) (by the
composition formula (C1): the product of the symbols vanishes, and the remainders are bounded by seminorms). In
particular

    ‖Ǎ_εPv‖_(½(𝟏−𝐦)+κ𝟏) ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖u‖_(−𝐍)),                                                {#eq:i-a-3-3}

because Ǎ_ε ∈ Ψ^(𝐤−κ𝟏) maps H^(𝐬−𝐦+𝟏) to H^(𝐬−𝐦+𝟏−𝐤+κ𝟏) = H^(½(𝟏−𝐦)+κ𝟏). The bound [[eq:i-a-3-3]] holds for
each ε > 0, with a constant that may depend on ε. Likewise Ǎ_εv ∈ H^(½(𝐦−𝟏)) for each ε > 0, as v ∈ H^(𝐬−κ𝟏). Both
pairings below are therefore of H^𝐭 with H^(𝐭′), 𝐭 + 𝐭′ ≥ 0, and are defined by (C4).

*Step 1: the pairing.* For ε > 0 and Schwartz w,

    ⟨C_εw, w⟩ = 2 Im⟨Ǎ_εPw, Ǎ_εw⟩.                                                                    {#eq:i-a-3-4}

This is algebra: 2 Im⟨Ǎ_εPw, Ǎ_εw⟩ = (1/i)⟨(Ǎ_ε²P − P^(∗h)Ǎ_ε²)w, w⟩, and
Ǎ²P − P^(∗h)Ǎ² = [Ǎ², P_R] + i(Ǎ²P_I + P_IǍ²). Let w_t := T_tv with T_t from (C8). We show that the right side of
[[eq:i-a-3-4]] at w = w_t tends to its value at v; C_ε itself is never applied to v, since with an absorbing term of
top order it need not act on H^(𝐬−κ𝟏). As t → 0, w_t → v in H^(𝐬−κ𝟏), and Ǎ_εw_t → Ǎ_εv in H^(½(𝐦−𝟏)).

Write Pv = ΦPu + [P, Φ]u (Step 0), so that Ǎ_εPw_t = Ǎ_εT_tΦPu + Ǎ_εT_t[P, Φ]u + Ǎ_ε[P, T_t]v. (This avoids
[Ǎ_ε, T_t], which for a variable decay order is bounded only in ⋂_δ Ψ^(𝐤−κ𝟏−𝟏+(0,δ)) [HJS, p. 79].) The first term
tends to Ǎ_εΦPu in H^(½(𝟏−𝐦)+κ𝟏), since T_t → Id strongly on H^(𝐬−𝐦+𝟏) and Ǎ_ε ∈ Ψ^(𝐤−κ𝟏) for the fixed ε. The
second is bounded in Ψ^(−∞,−∞) uniformly in t, as Ǎ_ε and [P, Φ] have disjoint microsupports and T_t is bounded in
Ψ^(0,0), and it tends to Ǎ_ε[P, Φ]u. In the third, [P, T_t] is bounded in Ψ^(𝐦−𝟏) and tends to 0 in Ψ^(𝐦−𝟏+δ𝟏)
([[lem:i-a-2-1]] (c); P has constant orders), so the term is bounded in H^(½(𝟏−𝐦)), since v ∈ H^(𝐬−κ𝟏), and tends to
0 as distributions, hence weakly in H^(½(𝟏−𝐦)). A weakly null sequence paired with a strongly convergent one tends to
0. So ⟨Ǎ_εPw_t, Ǎ_εw_t⟩ → ⟨Ǎ_εPv, Ǎ_εv⟩.

*Step 2: the estimate.* By [[eq:i-a-3-1]] and [[eq:i-a-3-4]], for Schwartz w,

    ‖B_εw‖² ≤ −ς · 2 Im⟨Ǎ_εPw, Ǎ_εw⟩ + C_F‖w‖²_(−𝐍) + ‖E_εw‖² + ⟨J_εPw, w⟩ + ⟨R_εw, w⟩.

Take w = w_t := T_tv and let t → 0, with ε > 0 fixed. The left side tends to ‖B_εv‖², and ‖E_εw_t‖² to ‖E_εv‖², as
B_ε, E_ε ∈ Ψ^(𝐬−κ𝟏); ⟨R_εw_t, w_t⟩ → ⟨R_εv, v⟩, as R_ε ∈ Ψ^(2𝐬−𝟏) and 2κ ≤ 1; the first term converges by Step 1,
and the J-term by the splitting in (d) below. So the inequality holds with v in place of w, and F_ε has dropped out. We
bound each term uniformly in ε ∈ (0, 1].

(a) |⟨Ǎ_εPv, Ǎ_εv⟩| ≤ ‖Ǎ_εPv‖_(−½(𝐦−𝟏)) ‖Ǎ_εv‖_(½(𝐦−𝟏)). Since Ǎ_ε is bounded in Ψ^𝐤, Step 0 gives
‖Ǎ_εPv‖_(−½(𝐦−𝟏)) ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖u‖_(−𝐍)). Next,

    ‖Ǎ_εv‖_(½(𝐦−𝟏)) ≤ ‖Z_εB_εv‖_(½(𝐦−𝟏)) + ‖Y_εv‖_(½(𝐦−𝟏)) ≤ C‖B_εv‖ + C‖v‖_(𝐬−𝟏).

So twice the term is at most ½‖B_εv‖² + C(‖GPu‖²_(𝐬−𝐦+𝟏) + ‖v‖²_(𝐬−½𝟏) + ‖u‖²_(−𝐍)).

(b) C_F‖v‖²_(−𝐍) ≤ C‖u‖²_(−𝐍).

(c) E_εv = E_εu − E_ε(Id − Φ)u, and E_ε(Id − Φ) is bounded in Ψ^(−∞,−∞) (Step 0), so
‖E_εv‖ ≤ C(‖E_εu‖ + ‖u‖_(−𝐍)) ≤ C(‖Eu‖_𝐬 + ‖u‖_(−𝐍)), the last by the microlocal parametrix of E on K_E (the
commutator [E, Φ] is not residual, and is not used).

(d) Choose Φ_J ∈ Ψ^(0,0) microlocally the identity near K_J, with WF′(Φ_J) ⊂ Ell(P) and
WF′(Φ_J) ∩ WF′(Id − Φ) = ∅; this is possible as K_J is closed, lies in the open set Ell(P) and misses WF′(Id − Φ).
Then ⟨J_εPv, v⟩ = ⟨J_εPv, Φ_Jv⟩ plus a term bounded by C‖u‖²_(−𝐍), since (Id − Φ_J)^(∗h)J_ε is residual. The same
splitting at w_t gives the convergence used above, as Φ_JT_tv → Φ_Jv in H^(𝐬+κ𝟏) (the bound below puts Φ_Jv in
H^(𝐬+𝟏), and [Φ_J, T_t] is bounded in Ψ^(−1,−1) and tends to 0 strongly). Then
|⟨J_εPv, Φ_Jv⟩| ≤ ‖J_εPv‖_(−𝐬)‖Φ_Jv‖_𝐬, and the microlocal parametrix of P on WF′(Φ_J) gives
‖Φ_Jv‖_𝐬 ≤ C(‖ΦPu‖_(𝐬−𝐦) + ‖u‖_(−𝐍)).

(e) |⟨R_εv, v⟩| ≤ C‖v‖²_(𝐬−½𝟏), and ‖v‖_(𝐬−½𝟏) ≤ C(‖Gu‖_(𝐬−½𝟏) + ‖u‖_(−𝐍)).

Absorbing ½‖B_εv‖² and using Step 0,

    ‖B_εv‖² ≤ C(‖GPu‖²_(𝐬−𝐦+𝟏) + ‖Eu‖²_𝐬 + ‖Gu‖²_(𝐬−½𝟏) + ‖u‖²_(−𝐍))     for all ε ∈ (0, 1].

The left side is finite for each ε > 0 (as B_ε ∈ Ψ^(𝐬−κ𝟏)), so nothing is assumed about B₀v. The qualitative
hypothesis Gu ∈ H^(𝐬−κ𝟏) is used only for the limits t → 0 in Steps 1 and 2; the bound uses ‖Gu‖_(𝐬−½𝟏).

*Step 3: the limit.* B_εv is bounded in L² and tends to B₀v as distributions, since B_ε → B₀ in Ψ^(𝐬+δ𝟏). A weak
limit point in L² is therefore B₀v, with ‖B₀v‖ ≤ lim inf ‖B_εv‖. Finally B₀u = B₀v + B₀(Id − Φ)u, where
B₀(Id − Φ) ∈ Ψ^(−∞,−∞). ∎

**Lemma {#lem:i-a-3-2}** (Iteration.) Let Γ be a closed subset of the boundary of phase space, U₀ an open
neighbourhood of it, and 𝐬₀ = 𝐬 − τ𝟏 with τ > 0 a constant. Suppose that for every κ ∈ (0, ½], every order
𝐬′ = 𝐬₀ + τ′𝟏 with κ ≤ τ′ ≤ τ, and every open U with Γ ⊂ U ⊂ U₀, the hypotheses of [[lem:i-a-3-1]] hold with
(𝐬′, κ, U) for some closed K₁ ⊂ U. Suppose this holds with the E-terms microsupported in a closed set
K_E(U) ⊂ Ū₀ ∖ Γ (or with no E-term), and with B₀ elliptic on the closure of an open neighbourhood U′ of Γ. Let G be
elliptic on Ū₀. Then there are a neighbourhood U_* of Γ and a closed set K_E^∗ ⊂ Ū₀ ∖ Γ such that for every
E ∈ Ψ^(0,0) elliptic on K_E^∗, every B ∈ Ψ^(0,0) microsupported in U_* and every 𝐍,

    ‖Bu‖_𝐬 ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖Eu‖_𝐬 + ‖Gu‖_(𝐬₀) + ‖u‖_(−𝐍)),                                           {#eq:i-a-3-5}

in the strong sense: if the right side is finite, so is the left.

*Proof.* Let J be an integer with J ≥ 4τ, let κ := τ/J ≤ ¼, and let 𝐬_j := 𝐬₀ + jκ𝟏, so that 𝐬_j − κ𝟏 = 𝐬_(j−1).
Construct U₀ ⊃ U₁ ⊃ … ⊃ U_J ⊃ Γ inductively, U_j being the U′ of the hypothesis for (𝐬_j, κ, U_(j−1)), with B₀^(j)
elliptic on Ū_j, and let K_E^∗ := ⋃_(j=1)^J K_E(U_(j−1)), a finite union of closed sets missing Γ (the sets move with
U, so one K_E need not serve every step). Let 𝒢₀ := G and, for j ≥ 1, let 𝒢_j ∈ Ψ^(0,0) be elliptic on Ū_j with
WF′(𝒢_j) ⊂ Ell(B₀^(j)), so that ‖𝒢_ju‖_(𝐬_j) ≤ C(‖B₀^(j)u‖ + ‖u‖_(−𝐍)) by (C5). [[lem:i-a-3-1]] with
(𝐬_j, κ, U_(j−1), 𝒢_(j−1)) needs 𝒢_(j−1)u ∈ H^(𝐬_j−κ𝟏) = H^(𝐬_(j−1)) and gives

    ‖B₀^(j)u‖ ≤ C(‖𝒢_(j−1)Pu‖_(𝐬_j−𝐦+𝟏) + ‖Eu‖_(𝐬_j) + ‖𝒢_(j−1)u‖_(𝐬_(j−1)) + ‖u‖_(−𝐍)).

Here ‖𝒢_(j−1)Pu‖ ≤ C(‖GPu‖ + ‖u‖_(−𝐍)), since U_(j−1) ⊂ U₀, and ‖Eu‖_(𝐬_j) ≤ ‖Eu‖_𝐬. Inducting on j gives
[[eq:i-a-3-5]] with U_* := U_J, using ‖Bu‖_𝐬 ≤ C(‖B₀^(J)u‖ + ‖u‖_(−𝐍)). The strong sense holds because the
qualitative hypothesis of each step, 𝒢_(j−1)u ∈ H^(𝐬_(j−1)), is the conclusion of the previous step. ∎

**Remark {#rem:i-a-3-3}** (Logarithmic losses.) With variable orders, symbols of the commutants carry factors log ϱ
(C6). Suppose, in [[lem:i-a-3-1]], that B_ε is only bounded in Ψ^(𝐬+δ𝟏) for every δ > 0, and R_ε only in
Ψ^(2𝐬−𝟏+δ𝟏), while the other hypotheses hold as stated, κ < ½, and B₀ has principal symbol bounded below by c > 0
times an elliptic weight of order 𝐬. Then the conclusion holds with the a priori term ‖Gu‖_(𝐬−κ𝟏). The proof is
unchanged, except that (e) is bounded by C‖v‖²_(𝐬−½𝟏+δ𝟏) ≤ C‖v‖²_(𝐬−κ𝟏) for δ ≤ ½ − κ, and
‖Bu‖_𝐬 ≤ C(‖B₀u‖ + ‖u‖_(−𝐍)) for B microsupported in Ell(B₀): b₀⁻¹ is bounded by the inverse weight, so it is a
symbol of order −𝐬 in the class of (C6). [[lem:i-a-3-2]] holds with this variant, since its steps have κ ≤ ¼. For
fixed ε, B_ε lies only in Ψ^(𝐬−κ𝟏+δ𝟏), so in Step 2 the left side is not known to converge. Instead,
B_εw_t → B_εv in H^(−δ𝟏), and ‖B_εw_t‖² is bounded by the right side at w_t, which converges to the right side at v;
so B_εv ∈ L² and, by weak lower semicontinuity, ‖B_εv‖² ≤ lim inf ‖B_εw_t‖² is bounded by the right side at v.
Likewise Y_ε is bounded only in Ψ^(𝐤−𝟏+2δ𝟏), which is harmless in (a).

**Definition {#def:i-a-cutoff}** (The cut-off.) Fix once and for all ψ ∈ C_c^∞((−1, 1)), even, with ψ = 1 on
[−½, ½], ψ′ ≤ 0 on [0, ∞) and √(−xψ(x)ψ′(x)) ∈ C^∞([0, ∞)) [Hin26c, (9.25)].

Such a ψ exists. Let ν ∈ C^∞([0, 1)) vanish on [0, ½], be positive on (½, 1) and equal (1 − x)⁻¹ near 1, and set
ψ(x) := exp(−∫_0^(|x|) ν²) for |x| < 1 and ψ := 0 otherwise. Then ψ is smooth, since ∫_0^x ν² → ∞ like (1 − x)⁻¹;
−ψ′ = ν²ψ for x ≥ 0; and √(−xψψ′) = √x νψ, which is smooth because ν = 0 on [0, ½] and νψ is smooth (flat at 1).

**Definition {#def:i-a-regulariser}** (The regulariser.) For κ ∈ (0, ½] and a defining function ϱ of a boundary face
of phase space, let φ_ε(ϱ) := (1 + εϱ⁻¹)^(−κ), ε ∈ (0, 1], and θ_ε := εϱ⁻¹(1 + εϱ⁻¹)⁻¹ ∈ [0, 1).

For any vector field V,

    V(φ_ε²) = 2κ θ_ε (ϱ⁻¹Vϱ) φ_ε²,     V(ϱ^(−a)φ_ε²) = −(a − 2κθ_ε)(ϱ⁻¹Vϱ) ϱ^(−a)φ_ε².                    {#eq:i-a-3-6}

Indeed φ_ε² = ϱ^(2κ)(ϱ + ε)^(−2κ), so V log φ_ε² = 2κ(1 − ϱ(ϱ + ε)⁻¹)ϱ⁻¹Vϱ = 2κθ_εϱ⁻¹Vϱ. The same formula shows that
φ_ε is bounded in S⁰ (in ϱ), lies in S^(−κ) for each ε > 0, and tends to 1 in S^δ for every δ > 0, and that θ_ε is
bounded in S⁰. So regularising a commutant of weight ϱ^(−a), a = 2𝗌′ − 1, replaces 𝗌′ by an effective order
𝗌′_ε := 𝗌′ − κθ_ε ∈ (𝗌′ − κ, 𝗌′] in the component the regulariser acts on. In [[lem:i-a-3-2]] that interval is
(𝗌_(j−1), 𝗌_j] ⊂ [𝗌₀, 𝗌].

### Radial point estimates {#sec:i-a-4}

#### At the horizon {#sec:i-a-4-1}

This section is [Hin26c, Proposition 9.9] in dimension 4 + 1. Fix a sign and write ℛ := ℛ_±, 𝖧 := ±ρ_∞H_(G₀) near
∂ℛ, p₁(σ) := p_(1,±)(σ) = ±ρ_∞σ_1(Im_h P̂(σ)), and

    ϑ_± := sup_(∂ℛ_±) max spec(β₀⁻¹p₁(0))     (with respect to h).

By [[eq:i-a-1-4]], p₁(σ) = p₁(0) ± (Im σ)ρ_∞τ₁ Id. So by [[eq:i-a-1-3]], for Im σ ≥ 0,

    β₀⁻¹p₁(σ) ≤ (ϑ_± − β Im σ) Id     at ∂ℛ.                                                             {#eq:i-a-4-1}

**Lemma {#lem:i-a-4-1}** (A defining function in S∗X̃°.) There are M, c′ > 0 and a neighbourhood W of ∂ℛ in S∗X̃° such
that q̃ := q_ext + M(ρ_∞²G₀)² is a quadratic defining function of ∂ℛ in S∗X̃° and 𝖧q̃ ≥ c′q̃ on W. Here
q_ext := q_± ∘ π for a smooth retraction π of a neighbourhood of ∂ℛ onto ∂Σ₀, an extension with dq_ext = 0 on ∂ℛ (an
arbitrary extension may carry a term linear in ρ_∞²G₀, and then q̃ need not be a defining function), and 𝖧 is given
near ∂ℛ by the same formula off Σ₀.

*Proof.* At ∂ℛ, 𝖧ρ_∞ = β₀ρ_∞ ≠ 0, so H_(G₀) ≠ 0 and dG₀ ≠ 0; hence y := ρ_∞²G₀ defines ∂Σ₀ near ∂ℛ. Since 𝖧G₀ = 0,
𝖧y = 2β₀y, with β₀ := ρ_∞⁻¹𝖧ρ_∞ extended as a smooth function, ≥ b₀ > 0 near ∂ℛ. 𝖧 vanishes on ∂ℛ, which consists of
radial points. So q_ext and 𝖧q_ext vanish to second order at ∂ℛ, and so does Z := 𝖧q_ext − (c/2)q_ext. In local
coordinates (y, z, w) near a point of ∂ℛ, with ∂ℛ = {y = 0, z = 0}: Z(0, z, w) ≥ (c/2)q_± ≥ c₁|z|²;
∂_yZ(0, z, w) = O(|z|), since ∂_yZ(0, 0, w) = 0; so Z ≥ c₁|z|² − C|y||z| − Cy² ≥ (c₁/2)|z|² − C′y². Then

    𝖧q̃ = Z + (c/2)q_ext + 4Mβ₀y² ≥ (c₁/2)|z|² + (4Mb₀ − C′)y²,

while q̃ ≤ C″(|z|² + y²) + My² and q̃ ≥ c″(|z|² + y²) near ∂ℛ. Take M ≥ max(C′/(2b₀), 2C₂), where by Taylor's formula
q_ext ≥ c₁|z|² − C|y||z| − Cy² ≥ (c₁/2)|z|² − C₂y², because q_ext = q_± on {y = 0} and dq_ext = 0 on ∂ℛ; so
q̃ ≥ (c₁/2)|z|² + (M/2)y². Take c′ small; finitely many coordinate patches cover the compact set ∂ℛ. ∎

**Proposition {#prop:i-a-4-2}** (Radial estimate at the horizon.) Let 𝒟 ⊂ {Im σ ≥ 0} be compact, U a neighbourhood of
∂ℛ in ^(sc)S∗ℝ̄⁴, and N ∈ ℝ.

(1) (*Direct.*) Let s > s₀ > ½ + ϑ_±. There are B, G ∈ Ψ^(0,0), microsupported in U, with kernels supported near ℋ and
B elliptic at ∂ℛ, such that for σ ∈ 𝒟, in the strong sense,

    ‖Bu‖_(H^s) ≤ C(‖GP̂(σ)u‖_(H^(s−1)) + ‖Gu‖_(H^(s₀)) + ‖u‖_(H^(−N))).                                  {#eq:i-a-4-2}

(2) (*Adjoint.*) Let s > ½ + ϑ_±. There are B, G, E ∈ Ψ^(0,0) as in (1), with WF′(E) ∩ ∂ℛ = ∅, such that for σ ∈ 𝒟,
in the strong sense,

    ‖Bu‖_(H^(1−s)) ≤ C(‖GP̂(σ)^(∗h)u‖_(H^(−s)) + ‖Eu‖_(H^(1−s)) + ‖u‖_(H^(−N))).                         {#eq:i-a-4-3}

The same holds with P̂(σ)^(∗h′) for any fibre inner product h′. Indeed P̂^(∗h′) = Θ⁻¹P̂^(∗h)Θ with Θ := H⁻¹H′ invertible
of order (0, 0), and conjugation by Θ preserves microsupports and Sobolev spaces.

*Proof.* (1) We verify the hypotheses of [[lem:i-a-3-2]] with Γ = ∂ℛ, 𝐦 = (2, 0), and orders in the regularity
component only (the kernels are compactly supported, so the decay order is immaterial). Fix s′ ∈ [s₀, s] and a
neighbourhood U of ∂ℛ. Let χ_∞ := χ(ρ_∞), where χ ∈ C^∞ equals 1 near 0 and is supported in [0, ρ_*), and let
ψ_R := ψ(ς_Rq̃) for a large parameter ς_R, extended homogeneously of degree 0. Set

    ǎ_ε := ρ_∞^(−s′+½) φ_ε(ρ_∞) χ_∞ ψ_R,     Ǎ_ε := ½(Op(ǎ_ε)Id + (Op(ǎ_ε)Id)^(∗h)).

Ǎ_ε is h-self-adjoint with principal symbol ǎ_ε Id. It is bounded in Ψ^(s′−1/2), lies in Ψ^(s′−1/2−κ) for ε > 0, and
is microsupported in supp ψ_R, which lies in U for ς_R large. This is (i), with 𝐤 = s′ − ½.

By [[lem:i-a-2-1]] (c), P̂(σ)_R has principal symbol G₀ Id and P̂(σ)_I ∈ Ψ¹ has principal symbol σ_1(Im_h P̂(σ)), so

    σ_(2s′)(C_ε) = H_(G₀)(ǎ_ε²) Id + 2ǎ_ε² σ_1(Im_h P̂(σ)) = ±ρ_∞⁻¹[𝖧(ǎ_ε²) Id + 2ǎ_ε² p₁(σ)].

By [[eq:i-a-3-6]] with ϱ = ρ_∞, a = 2s′ − 1, V = 𝖧 (so ϱ⁻¹Vϱ = β₀) and the regulariser of the step
(κ = s_j − s_(j−1)),

    𝖧(ǎ_ε²) = ρ_∞^(−2s′+1) φ_ε² χ_∞² [−β₀(2s′_ε − 1)ψ_R² + 2ς_R ψ_Rψ_R′ 𝖧q̃] + r_ε,     s′_ε := s′ − κθ_ε,

where r_ε collects the terms with χ_∞′. These are supported at bounded frequencies over a compact set, so r_ε is bounded
in S^(−∞). Let Q_ε := β₀(2s′_ε − 1) Id − 2p₁(σ). In [[lem:i-a-3-2]] the order is s′ = s_j with κ = s_j − s_(j−1),
so s′_ε ∈ (s_(j−1), s_j] ⊂ [s₀, s]. With s′_ε ≥ s₀, [[eq:i-a-4-1]] gives, at ∂ℛ,

    Q_ε ≥ 2β₀(s′_ε − ½ − ϑ_± + β Im σ) Id ≥ 2β₀(s₀ − ½ − ϑ_±) Id.

Since β₀ > 0 near ∂ℛ and s′_ε ≥ s₀, Q_ε ≥ Q^(0) := β₀(2s₀ − 1) Id − 2p₁(σ) there, for every ε. The endomorphism Q^(0)
does not depend on ε, is continuous in the base point and in σ ∈ 𝒟, and is at least 2β₀(s₀ − ½ − ϑ_±) Id at ∂ℛ by
[[eq:i-a-4-1]]. (Q_ε itself is not equicontinuous in ε at ρ_∞ = 0, since θ_ε is not.) So there are a neighbourhood
W′ ⊂ W ∩ U of ∂ℛ and c_Q > 0 with Q_ε ≥ c_Q Id on W′. Choose ς_R so large that supp ψ_R ⊂ W′, so that also
𝖧q̃ ≥ c′q̃ ≥ 0 on supp ψ_R by [[lem:i-a-4-1]]. Let χ̃ equal 1 on supp ψ_R with support in W′, and set
Q̃_ε := χ̃Q_ε + (1 − χ̃)c_Q Id ≥ c_Q Id. Define

    b_ε := ρ_∞^(−s′) φ_ε χ_∞ ψ_R Q̃_ε^(1/2),
    b_(R,ε) := ρ_∞^(−s′) φ_ε χ_∞ (2𝖧q̃/q̃)^(1/2) √(−xψ(x)ψ′(x)) |_(x = ς_Rq̃).

Both are smooth: the first by [[lem:i-a-2-2]]; the second because ψ′(ς_Rq̃) ≠ 0 only where q̃ ≥ (2ς_R)⁻¹, on which
𝖧q̃/q̃ ≥ c′. They satisfy b_ε^(∗h) = b_ε and

    ±ρ_∞ σ_(2s′)(C_ε) = −ρ_∞(b_ε² + b_(R,ε)² Id) + r_ε,

using 2ς_Rψ_Rψ_R′𝖧q̃ = −2(𝖧q̃/q̃)(−xψψ′)|_(x = ς_Rq̃). Let B_ε := ½(Op(b_ε) + Op(b_ε)^(∗h)) and
B_(R,ε) := Op(b_(R,ε))Id. By [[lem:i-a-2-1]], ±C_ε = −B_ε^(∗h)B_ε − B_(R,ε)^(∗h)B_(R,ε) + R_ε with R_ε bounded in
Ψ^(2s′−1) and microsupported in supp ψ_R. This is [[eq:i-a-3-1]] with ς = ±, F_ε := B_(R,ε)^(∗h)B_(R,ε) ≥ 0, and no
E- or J-term.

B_ε is bounded in Ψ^(s′), lies in Ψ^(s′−κ) for ε > 0, and tends in Ψ^(s′+δ) to B₀, the same operator with φ_ε
replaced by 1 and s′_ε by s′; B₀ is elliptic where ψ_R = 1 near fibre infinity, a neighbourhood of ∂ℛ. With
z_ε := ρ_∞^(1/2)Q̃_ε^(−1/2), bounded in S^(−1/2) = S^(−½(𝐦−𝟏)), we have z_εb_ε = ǎ_ε Id, so Ǎ_ε − Op(z_ε)B_ε is
bounded in Ψ^(s′−3/2). All constants are uniform in σ ∈ 𝒟: every symbol depends polynomially on σ, and c_Q, W′ and ς_R
do not depend on σ. [[lem:i-a-3-2]] gives [[eq:i-a-4-2]].

(2) For P̂(σ)^(∗h): Re_h(P̂^(∗h)) = P̂_R and Im_h(P̂^(∗h)) = −P̂_I. Take the target order s̃ := 1 − s′ (s′ ≥ s) and the
same commutant with s̃ in place of s′. The same symbol calculus gives

    ±ρ_∞σ(C_ε) = ρ_∞^(−2s̃+1)φ_ε²χ_∞²[ψ_R²Q^♭_ε + 2ς_Rψ_Rψ_R′𝖧q̃] + r_ε,

where

    Q^♭_ε := β₀(1 − 2s̃_ε) Id − 2p₁(σ) ≥ 2β₀(s′ − ½ − ϑ_± + β Im σ) Id ≥ c_Q Id

at and near ∂ℛ, because s̃_ε ≤ s̃ = 1 − s′. So ∓C_ε = −B_ε^(∗h)B_ε + B_(R,ε)^(∗h)B_(R,ε) + R_ε with
b_ε := ρ_∞^(−s̃)φ_εχ_∞ψ_R(Q̃^♭_ε)^(1/2) and b_(R,ε) as before. This is [[eq:i-a-3-1]] with ς = ∓ and E_ε := B_(R,ε),
which is microsupported in supp ψ′(ς_Rq̃), a closed set disjoint from ∂ℛ. The regulariser only lowers s̃_ε, which
increases Q^♭_ε, so the iteration of [[lem:i-a-3-2]] runs from 𝐬₀ = −N with no threshold. Choose E elliptic on the set
K_E^∗ of [[lem:i-a-3-2]], a finite union of such sets, closed and disjoint from ∂ℛ. ∎

**Remark {#rem:i-a-4-3}** (The threshold is that of [Hin26c].) [Hin26c, (5.17)] takes
ϑ_(ℋ⁺) := sup_(N∗ℋ⁺∖o) spec[β₀⁻¹ρ_∞σ_1((P₀ − P₀∗)/2i)] with ρ_∞ := ξ₀⁻¹. That function is odd in the fibres, and β₀⁻¹ is
the ϱ²/(2(r₊ − m)) of [Hin26c, (4.28)]. At covectors annihilating ∂_(t_*), σ_1((P₀ − P₀∗)/2i) = σ_1(Im P̂(0)). So on ℛ₊
the quantity of [Hin26c] is β₀⁻¹p_(1,+)(0), and on ℛ₋ it is β₀⁻¹p_(1,−)(0); hence ϑ_ℋ = max_± ϑ_± is the ϑ_(ℋ⁺) of
[Hin26c]. For the operators of the later chapters ϑ_ℋ is evaluated in [[ch:s13]] and [[ch:s14]].

#### The geometry over ∂X {#sec:i-a-4-2}

**Lemma {#lem:i-a-4-4}** (Symbols at the boundary face.) Assume (H1)–(H2), and write σ = σ₀ + iσ₁.

(a) At the boundary face, P̂(σ) ∈ Ψ^(2,0) has principal symbol G_σ Id with G_σ := 2σξ + ξ² + |η|², |η| the round
norm. T ∈ Ψ^(1,0) has principal symbol 2ξ Id there.

(b) Im_h T = −ρ(S + S^(∗h)) + T₂ with T₂ ∈ Ψ^(1,−2), and Im_h P̂(0) ∈ ρ²Diff¹_b ⊂ Ψ^(1,−1). At ρ = 0,
ρ⁻¹Im_h P̂(0) has a principal symbol that is linear in (ξ, η) and h-self-adjoint.

(c) For a symbol p(ω, ξ, η) at the boundary face, the scattering Hamilton vector field satisfies H_p = ρ𝖵_p, with 𝖵_p
a b-vector field. At ρ = 0,

    𝖵_p = −(∂_ξp)(ρ∂_ρ + η·∂_η) + (η·∂_ηp)∂_ξ + H^(𝕊³)_p,                                                  {#eq:i-a-4-4}

where H^(𝕊³)_p is the Hamilton vector field of p(ω, ξ, ·) on T∗𝕊³.

*Proof.* (a) ρ²∂_ρ = −∂_r, whose symbol is −iξ, so 2iρ²∂_ρ has symbol 2ξ. The rest of T lies in
ρC^∞ + ρ³Diff¹_b ⊂ Ψ^(1,−1). The operators ρ²(ρD_ρ)² and ρ²Δ_(𝕊³) have symbols ξ² and |η|² at ρ = 0, since ρD_ρ has
symbol −ρ⁻¹ξ and a covector rη has length |η|. The remainder of P̂(0), in ρ²(Diff¹_b + ρDiff²_b) ⊂ Ψ^(2,−1),
vanishes at ρ = 0, and σ²g₀₀ ∈ Ψ^(0,−2).

(b) Let A := 2iρ(ρ∂_ρ − 3/2) act componentwise. For the density ρ⁻⁵dρ dω, integration by parts gives
(ρ²∂_ρ)^† = −ρ²∂_ρ + 3ρ, so A^† = A. Then A^(∗h) = H⁻¹AH = A + 2iρ²H⁻¹(∂_ρH), and
Im_h A = −ρ²H⁻¹∂_ρH ∈ ρ²C^∞ ⊂ Ψ^(0,−2). Next, Im_h(−2iρS) = −ρ(S + S^(∗h)), and
Im_h(−iQ) = −Re_h Q ∈ ρ³Diff¹_b ⊂ Ψ^(1,−2). The statement on Im_h P̂(0) is [[rem:i-a-hypotheses]] (a), and
ρ²Diff¹_b = ρ · ρDiff¹_b with ρDiff¹_b ⊂ Diff¹_sc. The symbol of ρDiff¹_b at ρ = 0 is linear in (ξ, η): its
zeroth-order part lies in ρC^∞. Self-adjointness follows from [[lem:i-a-2-1]] (b).

(c) By [HJS, (7.33)–(7.34), p. 50], for covectors τ dx/x² + μ·dy/x,

    H_p = ∂_τp (x²∂_x) + ∂_μp (x∂_y) − (x²∂_xp + xμ·∂_μp)∂_τ − (x∂_yp − x(∂_τp)μ)·∂_μ.

Here x = ρ and y = ω. From dr = −dρ/ρ² we get ξ dr + rη = −ξ dρ/ρ² + η·dω/ρ, so τ = −ξ and μ = η. Dividing by ρ and
setting ρ = 0, with ∂_τ = −∂_ξ, gives [[eq:i-a-4-4]]. ∎

So the face symbol of Re_h P̂(σ) is g_(σ₀) := 2σ₀ξ + ξ² + |η|². Write 𝖧_(σ₀) := 𝖵_(g_(σ₀)). By [[eq:i-a-4-4]],

    𝖧_(σ₀) = −2(σ₀ + ξ)(ρ∂_ρ + η·∂_η) + 2|η|²∂_ξ + H_(|η|²),
    ρ⁻¹𝖧_(σ₀)ρ = −2(σ₀ + ξ),     𝖧_(σ₀)g_(σ₀) = 0.                                                       {#eq:i-a-4-5}

(This is [Hin26c, p. 166].) For σ₀ ≠ 0 define

    R_(σ₀,in) := {ρ = 0, ξ = −2σ₀, η = 0},     R_out := {ρ = 0, ξ = 0, η = 0},                          {#eq:i-a-4-6}

    Σ^∂_(σ₀) := {ρ = 0, g_(σ₀) = 0}.                                                                     {#eq:i-a-4-7}

R_out is the zero section over ∂X.

**Lemma {#lem:i-a-4-5}** (The flow over ∂X.) Let σ₀ ≠ 0 and ε₀ := sgn σ₀. The characteristic set Σ^∂_(σ₀) is compact
and lies at finite frequencies. 𝖧_(σ₀) is tangent to it and vanishes exactly on R_(σ₀,in) ∪ R_out there. Every maximal
integral curve of ε₀𝖧_(σ₀) in Σ^∂_(σ₀) ∖ (R_(σ₀,in) ∪ R_out) is defined for all times, tends to R_(σ₀,in) as t → −∞
and to R_out as t → +∞, uniformly on compact subsets. Moreover ε₀ρ⁻¹𝖧_(σ₀)ρ = 2|σ₀| at R_(σ₀,in) and −2|σ₀| at R_out.

*Proof.* On Σ^∂_(σ₀), |η|² = −ξ(ξ + 2σ₀). So ξ lies between −2σ₀ and 0, and η = 0 exactly at the two endpoints. By
[[eq:i-a-4-5]], ε₀𝖧_(σ₀)ξ = 2ε₀|η|² = −2ε₀ξ(ξ + 2σ₀), and 𝖧_(σ₀) vanishes at η = 0. Along the flow, ξ solves the
logistic equation ξ̇ = −2ε₀ξ(ξ + 2σ₀) on the open interval between −2σ₀ and 0. Its solutions exist for all time and
tend monotonically to 0 as t → ∞ and to −2σ₀ as t → −∞. Then |η|² = −ξ(ξ + 2σ₀) → 0, and the convergence is
exponential, so ∫|ω̇| dt ≤ ∫2|η| dt < ∞ and ω converges as well. The last statement is [[eq:i-a-4-5]] at ξ = −2σ₀ and
at ξ = 0. ∎

#### At R_in {#sec:i-a-4-3}

This section is [Hin26c, Proposition 9.10] in dimension 4 + 1. Let p_in := σ(ρ⁻¹Im_h P̂(0))|_(ρ = 0, ξ = −2, η = 0).
By the linearity in [[lem:i-a-4-4]] (b), σ(ρ⁻¹Im_h P̂(0)) = σ₀p_in at R_(σ₀,in), for either sign of σ₀. Recall
ϑ_in = sup_(∂X) max spec(p_in − (S + S^(∗h))).

**Proposition {#prop:i-a-4-6}** (Radial estimate at R_in.) Let I ⊂ ℝ ∖ 0 be compact, ν ≥ 0, U a neighbourhood of
⋃_(σ₀∈I) R_(σ₀,in), and s, N ∈ ℝ. For σ ∈ I + i[0, ν] the radial set is R_(Re σ,in).

(1) (*Direct.*) Let 𝗋 > 𝗋₀ > (−1 + ϑ_in)/2 (constants). There are B, G ∈ Ψ^(0,0) microsupported in U and at finite
frequencies, with B elliptic at R_(Re σ,in), such that for σ ∈ I + i[0, ν], in the strong sense,

    ‖Bu‖_(s,𝗋) ≤ C(‖GP̂(σ)u‖_(s−2,𝗋+1) + ‖Gu‖_(−N,𝗋₀) + ‖u‖_(−N,−N)).                                      {#eq:i-a-4-8}

(2) (*Adjoint.*) Let 𝗋 > (−1 + ϑ_in)/2. There are B, G, E as in (1), with WF′(E) ∩ R_(Re σ,in) = ∅, such that, in the
strong sense,

    ‖Bu‖_(−s+2,−𝗋−1) ≤ C(‖GP̂(σ)^(∗h)u‖_(−s,−𝗋) + ‖Eu‖_(−s+2,−𝗋−1) + ‖u‖_(−N,−N)).                        {#eq:i-a-4-9}

The regularity orders are immaterial, the operators being microsupported at finite frequencies. As with
[[prop:i-a-4-2]], the adjoint may be taken in any fibre inner product. B, G and E depend on σ₀, the commutant being
centred at R_(σ₀,in); their bounds in Ψ^(0,0), the ellipticity of B at R_(σ₀,in) and C are uniform in σ ∈ I + i[0, ν].

*Proof.* Write P := P̂(σ) and fix h, the inner product in which ϑ_in is evaluated. Then

    P_I = P_I^(0) + σ₁ Re_h T,     P_I^(0) := Im_h P̂(0) + σ₀ Im_h T + Im(σ²) g₀₀ ∈ Ψ^(1,−1),

by Im_h(σT) = σ₀ Im_h T + σ₁ Re_h T and [[lem:i-a-4-4]] (b). Its symbol at ρ = 0 is ρp̂ with
p̂ := σ(ρ⁻¹Im_h P̂(0)) − σ₀(S + S^(∗h)), so p̂ = σ₀(p_in − (S + S^(∗h))) at R_(σ₀,in). Let ε₀ := sgn σ₀ and
K := −ε₀ Re_h T; K is h-self-adjoint with principal symbol −2ε₀ξ Id, which equals 4|σ₀| at R_(σ₀,in).

*Commutant.* For an order 𝗋′ and a regulariser φ_ε(ρ) of exponent κ, let

    ǎ_ε := ρ^(−𝗋′−½) φ_ε ψ_∂ ψ_Σ ψ_R,     ψ_∂ := ψ(ς_∂ρ),  ψ_Σ := ψ(ς_Σ g_(σ₀)²),  ψ_R := ψ(ς_Rq),
    q := (ξ + 2σ₀)² + |η|²,

with g_(σ₀) and q extended independently of ρ, and let Ǎ_ε be the h-symmetrisation of Op(ǎ_ε)Id. This is (i) of
[[lem:i-a-3-1]] with 𝐦 = (2, 0) and decay order 𝗋′ + ½; the regularity order is −∞. Using the identity
XǍ² + Ǎ²X = 2ǍXǍ + [ [X, Ǎ], Ǎ],

    C_ε = i[P_R, Ǎ_ε²] + 2Ǎ_εP_I^(0)Ǎ_ε − 2ε₀σ₁Ǎ_εKǍ_ε + R′_ε,
    R′_ε := [ [P_I^(0), Ǎ_ε], Ǎ_ε] + σ₁[ [Re_h T, Ǎ_ε], Ǎ_ε],

where R′_ε is bounded in Ψ^(−∞,2𝗋′−1): each commutator with Ǎ_ε, whose principal symbol is scalar, lowers both orders
by one ([[lem:i-a-2-1]] (c)).

*Symbol.* P_R has face symbol g_(σ₀) Id. Its lower-order part, which is matrix-valued and depends on σ₁, enters
i[P_R, Ǎ²] one order lower. The decay-2𝗋′ symbol of i[P_R, Ǎ_ε²] + 2Ǎ_εP_I^(0)Ǎ_ε is
ρ𝖧_(σ₀)(ǎ_ε²) Id + 2ρǎ_ε²p̂ at ρ = 0. Terms with an extra factor ρ lie in Ψ^(−∞,2𝗋′−1), and the derivatives of ψ_∂,
supported at ρ ∈ [(2ς_∂)⁻¹, ς_∂⁻¹] and at finite frequencies, are in Ψ^(−∞,−∞). By [[eq:i-a-3-6]] and
[[eq:i-a-4-5]], 𝖧_(σ₀)ψ_Σ = 0 and

    𝖧_(σ₀)q = −2(σ₀ + ξ) · 2|η|² + 2|η|² · 2(ξ + 2σ₀) = 4σ₀|η|²,

so at ρ = 0

    ε₀ρ^(2𝗋′)[ρ𝖧_(σ₀)(ǎ_ε²) + 2ρǎ_ε²p̂] = −φ_ε²ψ_Σ²[ψ_R²Q_ε − 8|σ₀|ς_R|η|²ψ_Rψ_R′],
    Q_ε := ε₀[(2𝗋′_ε + 1)(ρ⁻¹𝖧_(σ₀)ρ) Id − 2p̂],     𝗋′_ε := 𝗋′ − κθ_ε.

At R_(σ₀,in), ε₀ρ⁻¹𝖧_(σ₀)ρ = 2|σ₀| ([[lem:i-a-4-5]]) and ε₀p̂ = |σ₀|(p_in − (S + S^(∗h))). So

    Q_ε = 2|σ₀|[(2𝗋′_ε + 1) Id − (p_in − S − S^(∗h))] ≥ 2|σ₀|(2𝗋₀ + 1 − ϑ_in) Id > 0     at R_(σ₀,in),

for 𝗋′_ε ≥ 𝗋₀. In [[lem:i-a-3-2]] the orders are 𝗋_j ∈ [𝗋₀, 𝗋] and 𝗋′_ε ∈ (𝗋_(j−1), 𝗋_j]. Near R_(σ₀,in), where
ε₀ρ⁻¹𝖧_(σ₀)ρ > 0, Q_ε ≥ Q^(0) := ε₀[(2𝗋₀ + 1)(ρ⁻¹𝖧_(σ₀)ρ) Id − 2p̂], which does not involve ε. By continuity of Q^(0),
uniformly in σ₀ ∈ I and σ₁ ∈ [0, ν] (Q^(0) does not involve σ₁), there are a neighbourhood W ⊂ U and c_Q > 0 with
Q_ε ≥ c_Q and with the symbol of K at least 2|σ₀| on W.

*The cut-off term.* On supp ψ_Σψ_R′ at ρ = 0, write ξ = −2σ₀ + y. Then q = y² + |η|² ∈ [(2ς_R)⁻¹, ς_R⁻¹], and
|g_(σ₀)| ≤ γ := ς_Σ^(−1/2), with g_(σ₀) = y(y − 2σ₀) + |η|². So 2|σ₀||y| ≤ γ + q. Take ς_Σ with γ ≤ (2ς_R)⁻¹ ≤ q.
Then y² ≤ q²/σ₀² ≤ q/2 once ς_R ≥ 2/min_I σ₀², and |η|² ≥ q/2. Hence

    b_(R,ε) := ρ^(−𝗋′) φ_ε ψ_∂ ψ_Σ (8|σ₀||η|²/q)^(1/2) √(−xψ(x)ψ′(x)) |_(x = ς_Rq)

is smooth, the factor (|η|²/q)^(1/2) ≥ 2^(−1/2) being needed only on the support of the last factor. Moreover
−8|σ₀|ς_R|η|²ψ_Rψ_R′ = b_(R,ε)² ρ^(2𝗋′) φ_ε⁻² ψ_∂⁻² ψ_Σ⁻². Choose ς_R (then ς_Σ, then ς_∂) so large that
supp ǎ_ε ⊂ W.

*Decomposition.* With Q̃_ε as in [[prop:i-a-4-2]], b_ε := ρ^(−𝗋′)φ_εψ_∂ψ_Σψ_RQ̃_ε^(1/2), and B_ε, B_(R,ε) their
quantisations,

    ε₀C_ε = −B_ε^(∗h)B_ε − B_(R,ε)^(∗h)B_(R,ε) − 2σ₁Ǎ_εKǍ_ε + R_ε,

with R_ε bounded in Ψ^(−∞,2𝗋′−1). By [[lem:i-a-2-3]], K = L^(∗h)L + K′ with WF′(K′) ∩ W̄ = ∅. So

    2σ₁Ǎ_εKǍ_ε = 2σ₁(LǍ_ε)^(∗h)(LǍ_ε) + 2σ₁Ǎ_εK′Ǎ_ε,

the last term bounded in Ψ^(−∞,−∞), and F_ε := B_(R,ε)^(∗h)B_(R,ε) + 2σ₁Ǎ_εKǍ_ε satisfies
⟨F_εw, w⟩ ≥ −C‖w‖²_(−𝐍) for Schwartz w, as σ₁ ≥ 0. This is [[eq:i-a-3-1]] with ς = ε₀. The remaining hypotheses (Z_ε,
Y_ε, convergence) are verified as in [[prop:i-a-4-2]], with z_ε := ρ^(−1/2)Q̃_ε^(−1/2), bounded in
S^(−∞,1/2) = S^(−½(𝐦−𝟏)), as 𝐦 − 𝟏 = (1, −1). [[lem:i-a-3-2]] in the decay component gives [[eq:i-a-4-8]].

(2) For P^(∗h) the imaginary part is −P_I. With target decay order 𝗋̃ := −𝗋′ − 1, the same commutant and symbol calculus
give, at R_(σ₀,in),

    ε₀ρ^(2𝗋̃)σ(C^♭_ε) = 2|σ₀|φ_ε²(ψ_∂ψ_Σψ_R)²[−(2𝗋̃_ε + 1) Id − (p_in − S − S^(∗h))] + (cut-off term).

Since −(2𝗋̃_ε + 1) ≥ 2𝗋′ + 1 and 2𝗋′ + 1 − ϑ_in > 0, the bracket is positive definite. The cut-off term is −b_(R,ε)².
The σ₁-term is +2σ₁ǍKǍ here, of the sign of the bracket. So
−ε₀C^♭_ε = −B_ε^(∗h)B_ε − 2σ₁Ǎ_εKǍ_ε + B_(R,ε)^(∗h)B_(R,ε) + R_ε: this is [[eq:i-a-3-1]] with ς = −ε₀ and
E_ε := B_(R,ε), microsupported in supp ψ′(ς_Rq), which is disjoint from R_(σ₀,in); E is taken elliptic on the set
K_E^∗ of [[lem:i-a-3-2]]. The regulariser lowers 𝗋̃_ε, which keeps the bracket positive, so [[lem:i-a-3-2]] runs
from −N. ∎

#### Sums of squares, and commutators with b-vector fields {#sec:i-a-4-4}

This section is [Hin26c, (9.49) and Lemma 9.13] in dimension 4 + 1. Near ∂X let V₁ := ρ∂_ρ and
V_jk := ω_j∂_(ω_k) − ω_k∂_(ω_j) (1 ≤ j < k ≤ 4), the rotation fields of 𝕊³ ⊂ ℝ⁴. They span 𝒱_b near ∂X over C^∞,
and Σ_(j<k) V_jk^†V_jk = Δ_(𝕊³): the V_jk are Killing, hence anti-adjoint for dω, and −Σ_(j<k) V_jk² is the Casimir
of 𝔰𝔬(4) acting on functions on 𝕊³, which is Δ_(𝕊³). All act componentwise.

**Lemma {#lem:i-a-4-7}** (Sum of squares; [Hin26c, (9.49)] on E.) Near ∂X,
Re_h P̂(0) = Σ_j W_j^(∗h)W_j + R₁ + R₂, with W_j ∈ ρDiff¹_b acting componentwise, R₁ ∈ ρ²Diff¹_b and
R₂ ∈ ρ³Diff²_b, both h-self-adjoint. The σ-independent symbols r₁ := σ(ρ⁻¹R₁) and r₂ := σ(ρ⁻¹R₂) at ρ = 0 are
homogeneous of degrees 1 and 2 in (ξ, η), and so vanish at R_out.

*Proof.* Re_h P̂(0) = P̂(0) − i Im_h P̂(0) with Im_h P̂(0) ∈ ρ²Diff¹_b. So by (H2),

    ρ⁻¹ Re_h P̂(0) ρ⁻¹ = P^(0) + ρ[P^(0), ρ⁻¹] + ρ⁻¹(ρ²Diff¹_b)ρ⁻¹ ≡ (ρD_ρ)² + Δ_(𝕊³)

modulo Diff¹_b + ρDiff²_b. For the density ρ⁻⁵dρ dω, (ρD_ρ)^† = ρD_ρ + 4i, so (ρD_ρ)² = (ρD_ρ)^†(ρD_ρ) − 4iρD_ρ.
Hence ρ⁻¹ Re_h P̂(0) ρ⁻¹ = Σ_j Y_j^†Y_j + D₁ + ρD₂, with Y_j ∈ {ρD_ρ, V_jk}, D₁ ∈ Diff¹_b and D₂ ∈ Diff²_b. Multiply
by ρ on both sides. Since ρY^†Yρ = (Yρ)^†(Yρ), setting W_j := Y_jρ ∈ ρDiff¹_b gives
Re_h P̂(0) = Σ_j W_j^†W_j + ρD₁ρ + ρ²D₂ρ. Next, W^(∗h)W = W^†W + H⁻¹[W^†, H]W, and [W^†, H] ∈ ρC^∞ (a b-vector field
times ρ, applied to H), so the difference lies in ρ²Diff¹_b. Thus Re_h P̂(0) = Σ_j W_j^(∗h)W_j + R₁′ + R₂′ in the
stated classes. The left side and Σ_j W_j^(∗h)W_j are h-self-adjoint, so R₁′ + R₂′ = Re_h R₁′ + Re_h R₂′, and the
h-adjoint preserves both classes. The degrees follow as in [[lem:i-a-4-4]] (b). ∎

**Lemma {#lem:i-a-4-8}** (The commuted system; compare [Hin26c, Lemma 9.13].) Let V = (V₁, V₁₂, …, V₃₄), and for a
multi-index α let V^α be the ordered product, α₁ the number of factors V₁, |α| = k and A_k := {|α| = k}. If
P̂(σ)u = f near ∂X, then u^(k) := (V^αu)_(α∈A_k) satisfies

    P̂(σ)V^αu + Σ_(β∈A_k) P̃_αβ V^βu = V^αf − α₁V^(α′)f + Σ_(|β|≤k−1) R_αβ V^βu,                           {#eq:i-a-4-10}

where α′ := α − (1, 0, …, 0) (the term is absent if α₁ = 0), P̃_αβ ∈ ρ²Diff¹_b (so ρ⁻¹P̃_αβ ∈ Diff¹_sc has symbol 0
at R_out), and R_αβ ∈ ρDiff²_sc, all with End ℂ^N-valued coefficients depending polynomially on σ. The diagonal term
is P̂(σ) alone.

*Proof.* V^αf = P̂V^αu + [V^α, P̂]u. Split P̂ = 2iσρV₁ + 𝒫, with 𝒫 := −2iσρ(3/2 + S) + P̂(0) − iσQ + σ²g₀₀. Since
[V₁, ρ] = ρ, [V_jk, ρ] = 0 and [V₁, V_jk] = 0, we get [V^α, 2iσρV₁] = 2iα₁σρV^α modulo ρDiff^(k−1)_b. ([Hin26c] has
this commutator equal to 0 unless α = (k, 0, …, 0); it is 0 only for α₁ = 0.) Hence

    V^αf = (P̂ + 2iα₁σρ)V^αu + [V^α, 𝒫]u     modulo ρDiff^(k−1)_b u.

The diagonal term is +2iα₁σρ, where [Hin26c, (9.45)] has −2ikσρ. We do not keep it on the diagonal. With
V^α = V^(α′)V₁ (the V₁ commute with the V_jk),

    2iα₁σρV^αu = α₁V^(α′)(2iσρV₁u) − α₁[V^(α′), 2iσρ]V₁u = α₁V^(α′)(f − 𝒫u)     modulo ρDiff^(k−1)_b u.

Next, V^(α′)𝒫u = 𝒫V^(α′)u + [V^(α′), 𝒫]u, and [V^α, 𝒫], 𝒫V^(α′) and [V^(α′), 𝒫] are sorted by class as follows.
Terms from the ρC^∞ parts of 𝒫 give ρDiff^(k−1)_b. Terms from P̂(0) ∈ ρ²Diff²_b give ρ²Diff¹_b ∘ V^β with |β| ≤ k
(reorder products of V's modulo Diff^(k−1)_b). Terms from Q ∈ ρ³Diff¹_b and g₀₀ ∈ ρ²C^∞ give ρ²Diff¹_b ∘ V^β with
|β| ≤ k. Terms with |β| ≤ k − 1 are of the form R_αβV^β with R_αβ ∈ ρ²Diff¹_b + ρDiff⁰_b ⊂ ρDiff²_sc; those with
|β| = k form P̃_αβ. Collecting gives [[eq:i-a-4-10]]. That ρ⁻¹P̃_αβ ∈ ρDiff¹_b ⊂ Diff¹_sc has symbol 0 at the zero
section follows as in [[lem:i-a-4-4]] (b). ∎

**Remark {#rem:i-a-4-8-sign}** (The sign of the diagonal term.) With the sign of [Hin26c, (9.45)], the diagonal term
−2ikσρ contributes Im(σ⁻¹ · (−2ikσρ)) = −2kρ to the imaginary part, of the good sign at R_out. With the sign +2iα₁σρ
of [[lem:i-a-4-8]] it would contribute +2α₁ρ, which moves the threshold for u^(k) to 𝗋 < −½ + S̄ − α₁; Step 2 of the
proof of [Hin26c, Proposition 9.11] (p. 171) would then fail for 𝗋 ∈ [−3/2 + S̄, −½ + S̄). Rewriting the term through
the equation, as in [[eq:i-a-4-10]], removes it, so [Hin26c, (9.44)] holds with its threshold unchanged
([[prop:i-a-4-9]] (3)).

#### At R_out {#sec:i-a-4-5}

This section is [Hin26c, Proposition 9.11] in dimension 4 + 1. For σ ≠ 0 let P̃(σ) := σ⁻¹P̂(σ), and write
κ_σ := Re(σ⁻¹) = σ₀/|σ|² and ι_σ := −Im(σ⁻¹) = σ₁/|σ|² ≥ 0. By [[lem:i-a-4-4]], Re_h P̃ has face symbol
g̃ := 2ξ + κ_σ(ξ² + |η|²), and with 𝖧̃ := 𝖵_(g̃), [[eq:i-a-4-4]] gives

    𝖧̃ = −2(1 + κ_σξ)(ρ∂_ρ + η·∂_η) + 2κ_σ|η|²∂_ξ + κ_σH_(|η|²),
    ρ⁻¹𝖧̃ρ = −2(1 + κ_σξ),     𝖧̃(ξ² + |η|²) = −4|η|²,                                                    {#eq:i-a-4-11}

and 𝖧̃g̃ = 0. By Im_h(cA) = (Re c) Im_h A + (Im c) Re_h A, [[lem:i-a-4-4]] (b) and [[lem:i-a-4-7]],

    Im_h P̃ = P̃_I^(0) − ι_σ Σ_j W_j^(∗h)W_j,
    P̃_I^(0) := Im_h T + κ_σ Im_h P̂(0) − ι_σ(R₁ + R₂) + σ₁g₀₀ ∈ Ψ^(2,−1).                                 {#eq:i-a-4-12}

(Here Im_h(σ⁻¹σ²g₀₀) = σ₁g₀₀.) P̃_I^(0) has symbol ρp̃ at ρ = 0, with p̃ := −(S + S^(∗h)) + κ_σr₃ − ι_σ(r₁ + r₂) and
r₃ := σ(ρ⁻¹Im_h P̂(0)). The last three terms vanish at R_out, so p̃ = −(S + S^(∗h)) there.

**Proposition {#prop:i-a-4-9}** (Radial estimate at R_out.) Let 𝒟 be a compact subset of {σ ≠ 0, Im σ ≥ 0}, U a
neighbourhood of R_out, s, N ∈ ℝ, and h a fibre inner product.

(1) (*Direct.*) Let 𝗋 < −½ + ½ inf_(∂X) min spec(S + S^(∗h)). There are B, E, G ∈ Ψ^(0,0) microsupported in U at
finite frequencies, with B elliptic at R_out and WF′(E) ∩ R_out = ∅, such that for σ ∈ 𝒟, in the strong sense,

    ‖Bu‖_(s,𝗋) ≤ C(‖GP̂(σ)u‖_(s−2,𝗋+1) + ‖Eu‖_(s,𝗋) + ‖u‖_(−N,−N)).                                        {#eq:i-a-4-13}

(2) (*Adjoint.*) Let 𝗋 < 𝗋₀ < −½ + ½ inf_(∂X) min spec(S + S^(∗h)). There are B, G as in (1) such that, in the strong
sense,

    ‖Bu‖_(−s+2,−𝗋−1) ≤ C(‖GP̂(σ)^(∗h)u‖_(−s,−𝗋) + ‖Gu‖_(−N,−𝗋₀−1) + ‖u‖_(−N,−N)).                          {#eq:i-a-4-14}

(3) (*b-regularity*; [Hin26c, (9.44)].) In the setting of (1), for every k ∈ ℕ₀, with the norms of [[sec:i-a-4-6]],

    ‖Bu‖_((s;k),𝗋) ≤ C(‖GP̂(σ)u‖_((s−2;k),𝗋+1) + ‖Eu‖_((s;k),𝗋) + ‖u‖_(−N,−N)).                            {#eq:i-a-4-15}

With [[lem:i-a-2-4]], ½ inf min spec(S + S^(∗h)) can be taken within any ε > 0 of S̄. So every 𝗋 < −½ + S̄ is
admissible in (1) and (3), and every 𝗋₀ < −½ + S̄ in (2), for a suitable h; this is the threshold [Hin26c, (9.16c)].
As in [[prop:i-a-4-6]], B, E and G depend on σ, through κ_σ in ψ_Σ, with bounds and constants uniform on 𝒟.

*Proof.* (1) P̂(σ)u = f is equivalent to P̃u = σ⁻¹f, and |σ|⁻¹ is bounded on 𝒟. The commutant is
ǎ_ε := ρ^(−𝗋′−½)φ_εψ_∂ψ_Σψ_R with ψ_Σ := ψ(ς_Σg̃²), ψ_R := ψ(ς_Rq) and q := ξ² + |η|², and Ǎ_ε is the
h-symmetrisation of Op(ǎ_ε)Id, as in [[sec:i-a-4-3]], so that [[lem:i-a-3-1]] (i) holds. Using [[eq:i-a-4-12]], and
with R′_ε (double commutators) bounded in Ψ^(−∞,2𝗋′−1),

    C_ε = i[P̃_R, Ǎ_ε²] + 2Ǎ_εP̃_I^(0)Ǎ_ε − 2ι_σ Σ_j (W_jǍ_ε)^(∗h)(W_jǍ_ε) + R′_ε.

The third term is ≤ 0 exactly. At ρ = 0, by [[eq:i-a-3-6]], [[eq:i-a-4-11]], 𝖧̃ψ_Σ = 0 and 𝖧̃q = −4|η|²,

    ρ^(2𝗋′)[ρ𝖧̃(ǎ_ε²) + 2ρǎ_ε²p̃] = −φ_ε²ψ_Σ²[ψ_R²Q_ε − 8ς_R|η|²(−ψ_Rψ_R′)],
    Q_ε := (2𝗋′_ε + 1)(ρ⁻¹𝖧̃ρ) Id − 2p̃.

At R_out, Q_ε = −2(2𝗋′_ε + 1) Id + 2(S + S^(∗h)) ≥ 2(min spec(S + S^(∗h)) − 2𝗋′ − 1) > 0, since 𝗋′_ε ≤ 𝗋′ ≤ 𝗋.
Near R_out, ρ⁻¹𝖧̃ρ = −2(1 + κ_σξ) < 0, so Q_ε ≥ (2𝗋′ + 1)(ρ⁻¹𝖧̃ρ) Id − 2p̃, which does not involve ε and whose
remaining terms vanish at R_out and are bounded uniformly in σ ∈ 𝒟. So Q_ε ≥ c_Q on a neighbourhood W of R_out,
uniformly. The cut-off term is +8ς_R|η|²(−ψ_Rψ_R′) ≥ 0. On supp ψ_Σψ_R′ we have 2ξ = g̃ − κ_σq, so, with
γ := ς_Σ^(−1/2) as in [[sec:i-a-4-3]], |ξ| ≤ ½(γ + |κ_σ|q) ≤ ½(1 + |κ_σ|)q when γ ≤ q. Then ξ² ≤ q/2 for
ς_R ≥ (1 + sup_𝒟 |κ_σ|)², hence |η|² ≥ q/2, and

    e_(R,ε) := ρ^(−𝗋′)φ_εψ_∂ψ_Σ(8|η|²/q)^(1/2) √(−xψ(x)ψ′(x)) |_(x = ς_Rq)

is smooth. So C_ε = −B_ε^(∗h)B_ε + E_ε^(∗h)E_ε − F_ε + R_ε, with b_ε := ρ^(−𝗋′)φ_εψ_∂ψ_Σψ_RQ̃_ε^(1/2),
E_ε := Op(e_(R,ε))Id, F_ε := 2ι_σ Σ_j (W_jǍ_ε)^(∗h)(W_jǍ_ε) ≥ 0, and R_ε bounded in Ψ^(−∞,2𝗋′−1). E_ε is
microsupported in supp ψ′(ς_Rq), a closed set disjoint from R_out; let E be elliptic on the union K_E^∗ of these sets
over the steps of [[lem:i-a-3-2]], closed and disjoint from R_out. This is [[eq:i-a-3-1]] with ς = 1. Regularising
lowers 𝗋′_ε and keeps Q_ε > 0, so [[lem:i-a-3-2]] runs from −N.

(2) For P̃^(∗h) the imaginary part is −Im_h P̃. With target 𝗋̃ := −𝗋′ − 1 and a priori order −𝗋₀ − 1, the bracket at
R_out is 2(2𝗋̃_ε + 1) Id + 2(S + S^(∗h)). This is positive definite when 𝗋̃_ε > −½ − ½ min spec(S + S^(∗h)), which
holds for 𝗋̃_ε ≥ −𝗋₀ − 1, that is, in the range of effective orders of [[lem:i-a-3-2]] from the a priori order up.
The cut-off term −e_(R,ε)² and the term +2ι_σ Σ_j (W_jǍ)^(∗h)(W_jǍ) both carry the sign of −b_ε² in −C^♭_ε. So
−C^♭_ε = −B_ε^(∗h)B_ε − F_ε + R_ε, with no E-term. [[lem:i-a-3-2]] from 𝐬₀ = (−N, −𝗋₀ − 1) gives [[eq:i-a-4-14]];
this is an above-threshold estimate.

(3) By induction on k, the case k = 0 being (1). Apply (1) to the system [[eq:i-a-4-10]] for u^(k), with the inner
product h^(⊕A_k). Its principal part at the face is g̃ Id, and its decay-0 imaginary part is
−ι_σ Σ_j W_j^(∗h)W_j ⊗ Id, the same as before. Its decay-(−1) imaginary part has symbol p̃ ⊗ Id plus the symbols of
σ⁻¹P̃_αβ divided by ρ, which vanish at R_out by [[lem:i-a-4-8]]. So the proof of (1) applies verbatim, with the same
threshold. The right side of [[eq:i-a-4-10]], divided by σ, contains V^αf − α₁V^(α′)f, bounded in H^(s−2,𝗋+1) by
‖Gf‖_((s−2;k),𝗋+1), and R_αβV^βu with R_αβ ∈ ρDiff²_sc ⊂ Ψ^(2,−1) and |β| ≤ k − 1. The latter is bounded in
H^(s−2,𝗋+1) by C‖G̃u‖_((s;k−1),𝗋), plus C‖u‖_(−N,−N), for a microlocaliser G̃ elliptic on WF′(G). This uses that a
b-vector field lies in Ψ^(1,1) (it is ρ⁻¹ times a scattering vector field), so that its commutator with any
A ∈ Ψ^(m,l) lies in Ψ^(m,l) by [[lem:i-a-2-1]] (c). The induction hypothesis bounds ‖G̃u‖_((s;k−1),𝗋). The term
‖Eu^(k)‖_(s,𝗋) is bounded by ‖E′u‖_((s;k),𝗋) for E′ elliptic on WF′(E). Finally ‖Bu^(k)‖_(s,𝗋) controls
‖B′u‖_((s;k),𝗋) for B′ microsupported in Ell(B), since [V^α, B] lowers the module order. ∎

#### b-regularity spaces {#sec:i-a-4-6}

For k ∈ ℕ₀ let H^((s;k),𝗋) := {u ∈ H^(s,𝗋) : (⟨x⟩D_x)^αu ∈ H^(s,𝗋), |α| ≤ k}, normed by the sum, and H̄^((s;k),𝗋)
the extendible version ([[sec:i-a-6-1]]). The fields ⟨x⟩∂_(x_j) span 𝒱_b(ℝ̄⁴) over C^∞(ℝ̄⁴), so near ∂X the norm is
equivalent to the one defined with the V^α of [[sec:i-a-4-4]]. This is the space [Hin26c, (3.42)], which
[Hin26c, p. 106] uses with the fields (r∂_x)^α.

**Lemma {#lem:i-a-4-10}** (b-regularity away from the zero section; [Hin26c, Remark 9.14 and (9.53)].) Let
o_(∂X) = R_out be the zero section over ∂X. If B ∈ Ψ^(0,0) is microsupported away from o_(∂X), then for every k,
‖Bu‖_((s;k),𝗋) ≤ C(‖Bu‖_(s+k,𝗋+k) + ‖u‖_(−N,−N)), and conversely.

*Proof.* ⟨x⟩D_(x_j) ∈ Ψ^(1,1), and Σ_j (⟨x⟩D_(x_j))∗(⟨x⟩D_(x_j)) has principal symbol ⟨x⟩²|ζ|² in terms of the
Euclidean frequency ζ. This is elliptic in Ψ^(2,2) off the zero section of the boundary face, including at fibre
infinity. Ellipticity (C5) gives both inequalities, inductively in k. ∎

### Elliptic and propagation estimates {#sec:i-a-5}

**Proposition {#prop:i-a-5-1}** (Elliptic estimate.) Let 𝒟 ⊂ ℂ be compact and B ∈ Ψ^(0,0) microsupported in a closed
set K of the boundary of phase space on which P̂(σ) is elliptic in Ψ^(2,0) for every σ ∈ 𝒟, with a uniform lower bound
on its principal symbol. Then for G elliptic on K, all orders 𝐬 and all N, uniformly in σ ∈ 𝒟, in the strong sense,

    ‖Bu‖_𝐬 ≤ C(‖GP̂(σ)u‖_(𝐬−(2,0)) + ‖u‖_(−𝐍)).

*Proof.* By [[lem:i-a-2-1]] (d) and (C5) there is a microlocal parametrix Q_σ ∈ Ψ^(−2,0) with
Q_σP̂(σ) = Id + R_σ, where WF′(R_σ) ∩ K = ∅. Then

    Bu = BQ_σΦP̂(σ)u − BR_σu + BQ_σ(Id − Φ)P̂(σ)u,

with Φ microlocally the identity near K and microsupported in Ell(G). The construction is continuous in the symbol, so
its seminorms are uniform on 𝒟; the last two terms are residual. ∎

**Proposition {#prop:i-a-5-2}** (Propagation.) Let P ∈ Ψ^𝐦 and let h be a fibre inner product. Let F be one of the
two boundary faces of phase space, with defining function ϱ (ρ_∞ at fibre infinity, ρ at the boundary face over ∂X).
Suppose the following.

(a) Near a compact set Λ ⊂ F, P_R = Re_h P has principal symbol p Id with p real. Then H_p = μ𝖵 near Λ, where μ > 0
is a weight of order 𝐦 − 𝟏 and 𝖵 is a smooth vector field tangent to F ([HJS, (7.34)]; at fibre infinity 𝖵 = ρ_∞H_p
for 𝐦 = 2, and over ∂X it is given by [[eq:i-a-4-4]]). Fix a sign ε_f and set 𝖧_f := ε_f𝖵, the *forward* field.

(b) P_I = P_I^sub + P_I^abs, where P_I^sub ∈ Ψ^(𝐦−𝟏) is h-self-adjoint and ε_fP_I^abs = −c L^(∗h)L + K′ with c ≥ 0
a constant, L of order ½𝐦 and WF′(K′) ∩ W̄ = ∅ for a neighbourhood W of Λ.

(c) γ : [0, t₁] → F ∩ {p = 0} is an integral curve of 𝖧_f, injective, with 𝖧_f ≠ 0 on it, and γ([0, t₁]) ⊂ Λ.

(d) 𝐬 is an order whose component 𝗄_F on F satisfies 𝖧_f𝗄_F ≤ 0 near γ.

Let E ∈ Ψ^(0,0) be elliptic at γ(0). Then there are B, elliptic on γ([0, t₁]), and G, both microsupported in any given
neighbourhood of γ([0, t₁]), such that in the strong sense

    ‖Bu‖_𝐬 ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖Eu‖_𝐬 + ‖u‖_(−𝐍)).                                                          {#eq:i-a-5-1}

*Proof.* *Coordinates.* Since γ is injective and 𝖧_f ≠ 0 on it, there are coordinates
(z, y) ∈ (−2δ, t₁ + 2δ) × {|y| < 2δ₁} on a neighbourhood O of γ([0, t₁]) in F, in which 𝖧_f = ∂_z and γ(t) = (t, 0)
(flow out a small transversal disc through γ(−δ), the integral curve continued backward). Extend z and y off F
independently of ϱ. Choose δ and δ₁ so small that O ⊂ W and {z ∈ [−δ, 0], |y| ≤ δ₁} ⊂ Ell(E).

*Cut-offs.* Let χ_s(z) := ψ(−z/δ) for z ≤ 0 and χ_s(z) := 1 for z ≥ 0, smooth as ψ = 1 on [−½, ½]. So χ_s = 1 for
z ≥ 0 and χ_s = 0 for z ≤ −δ, and ∂_z(χ_s²) = (2/δ)(−ψψ′)(−z/δ) ≥ 0, supported in [−δ, −δ/2]. Let
χ_e(z) := ψ((z − t₁)/δ) for z ≥ t₁ and χ_e(z) := 1 for z ≤ t₁. So χ_e = 1 for z ≤ t₁, and
−∂_z(χ_e²) = (2/δ)(−ψψ′)((z − t₁)/δ) ≥ 0, supported in [t₁ + δ/2, t₁ + δ]. (Since ψ is even, ψ(−z/δ) alone would
vanish for z ≥ δ, and ∂_z(χ_s²) would be negative on [δ/2, δ].) Since −ψψ′ = (νψ)² on [0, ∞) ([[def:i-a-cutoff]]),
both derivatives are squares of smooth functions. Let ψ_y := ψ(|y|²/δ₁²).

*Commutant.* With 𝐤 = 𝐬 − ½(𝐦 − 𝟏), its component 𝗄 := 𝗄_F, a regulariser φ_ε(ϱ) of exponent κ and a large
constant M, let

    ǎ_ε := ϱ^(−𝗄) φ_ε e^(−Mz) χ_s(z) χ_e(z) ψ_y,

multiplied by a cut-off to a neighbourhood of F whose derivatives are residual. As in [[sec:i-a-4]], the operator is
Ǎ_ε := ½(Op(ǎ_ε)Id + (Op(ǎ_ε)Id)^(∗h)), h-self-adjoint as [[lem:i-a-3-1]] (i) requires, so that the identity
[[eq:i-a-3-4]] holds. At F, by [[eq:i-a-3-6]] and since 𝖧_fψ_y = 0 there,

    𝖧_f(ǎ_ε²) = ϱ^(−2𝗄)φ_ε²ψ_y²e^(−2Mz)[χ_s²χ_e²(−2M − 2𝗄_ε(ϱ⁻¹𝖧_fϱ) − 2(𝖧_f𝗄) log ϱ)
                  + χ_e²∂_z(χ_s²) + χ_s²∂_z(χ_e²)],

with 𝗄_ε := 𝗄 − κθ_ε. Here 𝖧_f(ϱ^(−2𝗄)) = ϱ^(−2𝗄)(−2𝗄ϱ⁻¹𝖧_fϱ − 2(𝖧_f𝗄) log ϱ); the logarithmic term
−2(𝖧_f𝗄) log ϱ is ≤ 0, since 𝖧_f𝗄 ≤ 0 and log ϱ < 0 near F. Let p′ := μ⁻¹ε_f σ(P_I^sub), an h-self-adjoint symbol
bounded on O (it has order 0 relative to μ), and

    Q_ε := (2M + 2𝗄_ε(ϱ⁻¹𝖧_fϱ)) Id − 2p′ + 2(𝖧_f𝗄) log ϱ Id.

Choose M ≥ 1 + sup_O (2|𝗄_εϱ⁻¹𝖧_fϱ| + 2‖p′‖), uniformly in ε since 𝗄_ε ∈ (𝗄 − κ, 𝗄]. Then Q_ε ≥ M Id. It is a
symbol of the logarithmic class of (C6), and so is Q_ε^(1/2). To see this, write Q_ε = Q₀ + Λ_ϱ Id with
Q₀ := (2M + 2𝗄_εϱ⁻¹𝖧_fϱ) Id − 2p′ ≥ M Id, bounded, and Λ_ϱ := 2(𝖧_f𝗄) log ϱ ≥ 0, scalar. By Cauchy's formula as in
[[lem:i-a-2-2]], ∂_Λ^j(Q₀ + Λ)^(1/2) = O((M + Λ)^(½−j)), and the derivatives of Q₀ and of Λ_ϱ along the vector fields
⟨x⟩^(−δ)𝒱_b of (C6) are bounded; by the chain rule Q_ε^(1/2) lies in the class for every δ > 0. ([[lem:i-a-2-2]] does
not apply to Q_ε/(1 + |log ϱ|), which is not bounded below where 𝖧_f𝗄 = 0; [HJS, p. 81] notes the point.)

*Decomposition.* As in [[sec:i-a-4]], σ(ε_fC_ε) = μ[𝖧_f(ǎ_ε²) Id + 2ǎ_ε²p′] + ε_fσ(Ǎ²P_I^abs + P_I^absǍ²), and

    μ[𝖧_f(ǎ_ε²) + 2ǎ_ε²p′] = −b_ε² − b_(e,ε)² + e_ε²,

with

    b_ε := μ^(1/2)ϱ^(−𝗄)φ_εψ_ye^(−Mz)χ_sχ_eQ̃_ε^(1/2),
    b_(e,ε) := μ^(1/2)ϱ^(−𝗄)φ_εψ_ye^(−Mz)χ_s(−∂_z(χ_e²))^(1/2),
    e_ε := μ^(1/2)ϱ^(−𝗄)φ_εψ_ye^(−Mz)χ_e(∂_z(χ_s²))^(1/2).

Here Q̃_ε is Q_ε cut off as in [[prop:i-a-4-2]]. The symbol e_ε is supported in {z ∈ [−δ, 0]}, inside Ell(E). As U
shrinks in [[lem:i-a-3-2]], δ and δ₁ shrink with it, and the E-set of every step lies in
{z ∈ [−δ, −δ/2], |y| ≤ δ₁} ⊂ Ell(E), which misses γ([0, t₁]); so the given E is elliptic on K_E^∗. By (b) and
[[lem:i-a-2-3]], ε_f(Ǎ²P_I^abs + P_I^absǍ²) = −2c(LǍ)^(∗h)(LǍ) plus a double commutator in Ψ^(2𝐬−𝟏) plus a residual
term. So ε_fC_ε = −B_ε^(∗h)B_ε − F_ε + E_ε^(∗h)E_ε + R_ε, with F_ε := B_(e,ε)^(∗h)B_(e,ε) + 2c(LǍ_ε)^(∗h)(LǍ_ε) and
R_ε bounded in Ψ^(2𝐬−𝟏). The orders are right: μϱ^(−2𝗄) is the weight of order 2𝐬 on F. Also ǎ_ε = z_εb_ε with
z_ε := μ^(−1/2)Q̃_ε^(−1/2), of order −½(𝐦 − 𝟏). B₀ is elliptic on γ([0, t₁]), where χ_s = χ_e = ψ_y = 1. The factor
(𝖧_f𝗄) log ϱ makes b_ε bounded only in Ψ^(𝐬+δ𝟏) for every δ > 0, while z_ε stays bounded since Q_ε ≥ M; this is the
case of [[rem:i-a-3-3]]. There is no threshold, so [[lem:i-a-3-2]] runs from 𝐬₀ = 𝐬 − τ𝟏 with τ large, giving
[[eq:i-a-5-1]] with ‖Gu‖_(𝐬₀) ≤ ‖u‖_(−𝐍). ∎

**Remark {#rem:i-a-5-2-uses}** (The two uses of [[prop:i-a-5-2]].) (i) At fibre infinity over X̃°: P = P̂(σ), p = G₀,
𝖵 = ρ_∞H_(G₀), ε_f = ± on ∂Σ₀^±, P_I = P_I^sub ∈ Ψ¹, and c = 0; the order is s_c, constant (O1).

(ii) At the boundary face, for σ = σ₀ + iσ₁ with σ₁ ≥ 0: p = g_(σ₀), 𝖵 = 𝖧_(σ₀), ε_f = ε₀,
P_I^sub = P_I^(0) ∈ Ψ^(1,−1) and P_I^abs = σ₁Re_h T. Then ε₀P_I^abs = −σ₁K with K := −ε₀Re_h T, whose principal
symbol −2ε₀ξ is positive on Σ^∂_(σ₀) ∖ R_out (there ε₀ξ < 0 by [[lem:i-a-4-5]]). So (b) holds on any neighbourhood W
of a compact subset of Σ^∂_(σ₀) ∖ R_out on which −2ε₀ξ > 0, by [[lem:i-a-2-3]]. For the adjoint P̂(σ)^(∗h), use the
backward field −𝖧_f: then P_I^abs becomes −σ₁Re_h T, and (−ε₀)(−σ₁Re_h T) = −σ₁K again. Condition (d) for the adjoint
asks for monotonicity along −𝖧_f of the dual order, which is minus the order: the same condition.

### The artificial boundary {#sec:i-a-6}

#### Extendible and supported spaces {#sec:i-a-6-1}

Let Ω := {|x| > r₀}. For an order pair whose regularity component is constant near ∂_♯X (true by (O1)) define

    H̄^(s,𝗋) := {u|_Ω : u ∈ H^(s,𝗋)(ℝ⁴; ℂ^N)} (quotient norm),     Ḣ^(s,𝗋) := {u ∈ H^(s,𝗋) : supp u ⊂ Ω̄}.

On a slab Ω_(a,b) := {a < r < b}, with r₀ − 2δ₀ < a < b < r₂, let H^s(Ω_(a,b))^(•,−) be the space of restrictions to
{r > a} of elements of H^s(ℝ⁴) supported in {r ≤ b}: supported at b, extendible at a. H^s(Ω_(a,b))^(−,•) is the space
with the roles of a and b exchanged, and H^s(Ω_(a,b))^(•,•) the space supported at both ends. On compact sets the
decay order is immaterial.

**Lemma {#lem:i-a-6-1}** (Extendible and supported spaces.) (a) Ḣ^(s,𝗋) is the closure of C_c^∞(Ω).

(b) The L² pairing identifies (H̄^(s,𝗋))^∗ with Ḣ^(−s,−𝗋).

(c) The same holds on slabs: (H^s(Ω_(a,b))^(•,−))^∗ = H^(−s)(Ω_(a,b))^(−,•), and C_c^∞(Ω_(a,b)) is dense in
H^s(Ω_(a,b))^(•,•).

(d) A differential operator L of order m maps each of these spaces to the corresponding space of order s − m. For L of
orders (m, ℓ), u ∈ H̄^(s,𝗋) and v ∈ Ḣ^(−s+m,−𝗋+ℓ), the pairing ⟨Lu, v⟩ is well defined, and it equals ⟨u, L^∗v⟩ for
u ∈ C_c^∞(ℝ⁴)|_Ω.

*Proof.* (a) Let u ∈ Ḣ^(s,𝗋), and write u = χu + (1 − χ)u, with χ ∈ C_c^∞({|x| < 2r₀}) equal to 1 on
{|x| ≤ (3/2)r₀}. Then (1 − χ)u is supported in {|x| ≥ (3/2)r₀}. Let χ̃ ∈ C_c^∞({|x| < (5/4)r₀}) equal 1 on
{|x| ≤ (9/8)r₀}. Then (1 − χ̃)(1 − χ) = 1 − χ, multiplication by 1 − χ̃ is bounded on H^(s,𝗋), and T_t → Id strongly
(C8). So the Schwartz functions (1 − χ̃)T_t(1 − χ)u, which are supported in Ω, tend to (1 − χ)u. A Schwartz function
supported in Ω is approximated by its products with χ₀(t|x|), χ₀ ∈ C_c^∞ equal to 1 near 0, as t → 0. The function χu
has compact support, so only the constant regularity order s matters. For μ > 1 let (D_μw)(x) := w(x/μ). Then
supp D_μ(χu) ⊂ {|x| ≥ μr₀} ⊂ Ω. The dilation D_μ is bounded on H^s uniformly for μ ∈ [1, 2]: ‖D_μw‖_(L²) = μ²‖w‖_(L²),
and D_μ f(D) D_μ⁻¹ = f(μD), so ⟨D⟩^s D_μ ⟨D⟩^(−s) D_μ⁻¹ is the Fourier multiplier ⟨ζ⟩^s⟨μζ⟩^(−s), bounded uniformly.
Also D_μ → Id strongly as μ → 1: this holds on C_c^∞, which is dense, and D_μ is uniformly bounded. Finally mollify
with a mollifier of radius less than (μ − 1)r₀.

(b) H̄^(s,𝗋) = H^(s,𝗋)/Z with Z := {u : supp u ⊂ ℝ⁴ ∖ Ω}, so (H̄^(s,𝗋))^∗ = Z^⊥ ⊂ H^(−s,−𝗋) (C4). If f ∈ Z^⊥, then f
annihilates C_c^∞({|x| < r₀}) ⊂ Z, so supp f ⊂ Ω̄. Conversely, if supp f ⊂ Ω̄ and z ∈ Z, approximate z in H^(s,𝗋) by
elements of C_c^∞({|x| < r₀}), which is (a) for the ball, with μ < 1; each pairs to 0 with f, so ⟨f, z⟩ = 0.

(c) Separate the two boundary spheres by a partition of unity and apply (a) and (b) at each.

(d) Locality of L, and (b). ∎

#### The energy estimate {#sec:i-a-6-2}

On {r₀ − 2δ₀ < r < r₂} let 𝔤 be the Lorentzian metric on X̃ whose inverse is the bilinear form of G₀. Its signature
is (1, 3) there, by (H4). Let X := 𝔤⁻¹(dr, ·) = ∇r, a 𝔤-timelike vector field, and time-orient 𝔤 so that X is future
directed. Then dr(V) = 𝔤(X, V) < 0 for V future timelike: r decreases to the future, as in (H4). Let
□ := −|𝔤|^(−1/2)∂_i|𝔤|^(1/2)𝔤^(ij)∂_j act componentwise, with principal symbol G₀ Id, and for u valued in ℂ^N (standard
inner product) let

    T[u](Y, Z) := Re(⟨Yu, Zu⟩ − ½𝔤(Y, Z)𝔤^(ij)⟨∂_iu, ∂_ju⟩),     ^((Y))K[u] := ½T[u]^(ij)(ℒ_Y𝔤)_ij.

**Lemma {#lem:i-a-6-2}** (Energy identity.) For smooth u and a smooth vector field W,
div_𝔤(T[u](W, ·)^♯) = −Re⟨□u, Wu⟩ + ^((W))K[u], and for w > 0, ^((wX))K[u] = w ^((X))K[u] + T[u](∇w, X).

*Proof.* Componentwise, with T_ij = Re(∂_iu ∂_jū − ½𝔤_ij ∂^ku ∂_kū) summed over components,

    ∇^iT_ij = Re(∇^i∂_iu ∂_jū + ∂^iu ∇_i∂_jū − ∂^ku ∇_j∂_kū) = −Re(□u ∂_jū),

since the Hessian of a function is symmetric and □ = −∇^i∂_i. Then ∇^i(T_ijW^j) = −Re(□u Wū) + T_ij∇^iW^j and
T_ij∇^iW^j = ½T^(ij)(ℒ_W𝔤)_ij by symmetry of T. For W = wX, T_ij∇^i(wX^j) = wT_ij∇^iX^j + T(∇w, X). ∎

**Proposition {#prop:i-a-6-3}** (The H¹ estimate.) Let L be a differential operator of order 2 on {r₀ − 2δ₀ < r < r₂}
with principal symbol G₀ Id, and let r₀ − 2δ₀ < a < b < r₂. There is C, depending on bounds for the coefficients of L
and on inf(−G₀(dr)) over the slab, such that

    ‖u‖_(H¹(Ω_(a,b))) ≤ C‖Lu‖_(L²(Ω_(a,b)))

for u ∈ H²(Ω_(a,b))^(•,−) (forward), and likewise for u ∈ H²(Ω_(a,b))^(−,•) (backward).

*Proof.* By density ([[lem:i-a-6-1]] (c), and smooth approximation up to the extendible side) take u smooth on
Ω̄_(a,b), vanishing near r = b (forward case). Write L = □ + L₁ with L₁ ∈ Diff¹. Fix a Riemannian metric R and a
density, and use coordinates (r, ω) on the slab (r = |x|). On the compact slab there are constants with
T[u](X, X) ≥ c₀|du|²_R (in a 𝔤-orthonormal frame with e₀ = X/|X|, T(e₀, e₀) = ½Σ_α |e_αu|²), |^((X))K[u]| ≤ C₀|du|²_R
and |L₁u| ≤ C₁(|du|_R + |u|).

Let w := e^(γr), so that ∇w = γwX, and J := T[u](wX, ·)^♯. By Stokes' formula (d(ι_J|d𝔤|) = div J |d𝔤|; the outward
conormal at r = a is −dr) and since u = 0 near b,

    ∫_(Ω_(a,b)) (−Re⟨□u, wXu⟩ + ^((wX))K[u]) |d𝔤| = −∫_({r = a}) dr(J) μ_a = −∫_({r = a}) w T[u](X, X) μ_a ≤ 0,

where μ_a is the induced density, and dr(J) = T(wX, ∇r). So, by [[lem:i-a-6-2]],

    ∫ w(γc₀ − C₀)|du|²_R ≤ ∫ w|□u||Xu| ≤ ∫ w|Lu||Xu| + C∫ w(|du|²_R + |u||du|_R).

*Weighted Poincaré inequality.* Since u(r, ω) = −∫_r^b ∂_su(s, ω) ds, with ℓ := b − a,

    ∫_a^b e^(γr)|u(r)|² dr ≤ ℓ∫_a^b |∂_su(s)|² ∫_a^s e^(γr) dr ds ≤ (ℓ/γ)∫_a^b e^(γs)|∂_su(s)|² ds.

Integrating over ω with bounded Jacobians, ∫ w|u|² ≤ (C_P/γ)∫ w|du|²_R. Hence C∫ w|u||du| ≤ C(C_P/γ)^(1/2)∫ w|du|².
For γ large (depending on c₀, C₀, C₁ and C_P) we get

    (γc₀/2)∫ w|du|² ≤ ∫ w|Lu||Xu| ≤ (γc₀/4)∫ w|du|² + (C/γ)∫ w|Lu|².

So ∫ w|du|² ≤ Cγ⁻²∫ w|Lu|², and with e^(γa) ≤ w ≤ e^(γb) and the Poincaré inequality once more, ‖u‖_(H¹) ≤ C‖Lu‖_(L²).

In the backward case u = 0 near a; take w := e^(−γr). The flux is at r = b, with sign +, and
^((wX))K = w(^((X))K − γT(X, X)). So ∫ w(γT(X, X) − ^((X))K) ≤ ∫ w|□u||Xu|, and the Poincaré inequality runs from
r = a, where w is largest. ∎

Thus the forward estimate uses the weight e^(γr) and the backward one e^(−γr), and the zeroth-order terms are
controlled by the Poincaré inequality.

**Proposition {#prop:i-a-6-4}** (All orders.) Let L be as in [[prop:i-a-6-3]] on {r₀ − 2δ₀ < r < r₂}, with L^∗ also of
that form (true for P̂(σ) and its adjoints). For every s ∈ ℝ and every slab Ω_(a,b) with
r₀ − δ₀ < a < b < r₂ − δ₀, the following hold.

(i) For every u ∈ H^s(Ω_(a,b))^(•,−), ‖u‖_(H^s(Ω_(a,b))^(•,−)) ≤ C‖Lu‖_(H^(s−1)(Ω_(a,b))^(•,−)).

(ii) For every u ∈ H^s(Ω_(a,b))^(−,•), ‖u‖_(H^s(Ω_(a,b))^(−,•)) ≤ C‖Lu‖_(H^(s−1)(Ω_(a,b))^(−,•)).

(iii) L : H^s(Ω_(a,b))^(•,−) → H^(s−1)(Ω_(a,b))^(•,−) is invertible, and so is the backward map.

C depends only on bounds for the coefficients and on inf(−G₀(dr)).

*Proof.* Fix a′ < a with a′ > r₀ − δ₀, and let Ω′ := Ω_(a′,b). We prove (i); (ii) is the same with the roles of the
ends exchanged.

*Uniqueness.* Let d ∈ H^t(Ω_(a,b))^(•,−) for some t, with Ld = 0. Let D ∈ H^t(ℝ⁴) be supported in {r ≤ b} with
D|_({r>a}) = d. Then LD = 0 on {a < r < r₂}, L being defined there, and D = 0 on {r > b}. By (H4) and
[[sec:i-a-6-2]], every null bicharacteristic of G₀ over {a < r < b + δ₀} moves monotonically in r, and its backward
direction (increasing r) reaches {r > b}, where D vanishes. [[prop:i-a-5-2]], in the use (i) of [[rem:i-a-5-2-uses]], at every order gives D ∈ C^∞({r > a}), as D is
smooth off the characteristic set by [[prop:i-a-5-1]]. So d|_([a+ε,b]) is smooth up to r = b and vanishes to infinite
order there; extended by 0 it lies in H²(Ω_(a+ε,b))^(•,−), and [[prop:i-a-6-3]] on Ω_(a+ε,b) gives d = 0 there, for
every ε > 0.

*Existence for s ≥ 0.* Let f ∈ H^(s−1)(Ω′)^(•,−) ⊂ H^(−1)(Ω′)^(•,−) = (H¹(Ω′)^(−,•))^∗. On
{L^∗φ : φ ∈ H²(Ω′)^(−,•)} ⊂ L²(Ω′), the functional L^∗φ ↦ ⟨f, φ⟩ is well defined. It is bounded, by
C‖f‖_(H^(−1))‖L^∗φ‖_(L²), by [[prop:i-a-6-3]] (backward) for L^∗. By the Hahn–Banach and Riesz theorems there is
w ∈ L²(Ω′), with ‖w‖ ≤ C‖f‖_(H^(−1)), such that ⟨w, L^∗φ⟩ = ⟨f, φ⟩ for all such φ. Taking
φ ∈ C_c^∞({a′ < r < b + δ₀}), restricted, shows that the extension W of w by 0 beyond b satisfies LW = F on
{a′ < r < b + δ₀}, where F is the supported extension of f; both sides vanish on {b < r < r₂}, so LW = F on
{a′ < r < r₂}. So w ∈ L²(Ω′)^(•,−) = L²(Ω′) solves Lw = f.

*Regularity.* W ∈ L², W = 0 on {r > b}, and LW ∈ H^(s−1) on {a′ < r < r₂}. [[prop:i-a-5-2]] at order s, propagating from
{r > b} along the monotone bicharacteristics, together with [[prop:i-a-5-1]], gives W ∈ H^s on {r > a}, with

    ‖w‖_(H^s(Ω_(a,b))) ≤ C(‖f‖_(H^(s−1)(Ω′)) + ‖w‖_(L²(Ω′))) ≤ C‖f‖_(H^(s−1)(Ω′)).

Here the error term ‖W‖_(−N) of [[eq:i-a-5-1]] is bounded by ‖w‖_(L²) for N ≥ 0.

*The case s ≥ 0 of (i) and (iii).* Given u ∈ H^s(Ω_(a,b))^(•,−), extend f := Lu to f′ ∈ H^(s−1)(Ω′)^(•,−) with
‖f′‖ ≤ 2‖f‖, and let w solve Lw = f′ on Ω′. By uniqueness on Ω_(a,b), w|_(Ω_(a,b)) = u. So ‖u‖_(H^s) ≤ C‖f‖_(H^(s−1)),
and L is onto with this bound. It is injective by uniqueness.

*The case s < 0.* By the case 1 − s > 0 of (ii) for L^∗, ‖φ‖_(H^(1−s)) ≤ C‖L^∗φ‖_(H^(−s)) for
φ ∈ H^(1−s)(Ω′)^(−,•). The Hahn–Banach argument with these spaces produces, for
f ∈ H^(s−1)(Ω′)^(•,−) = (H^(1−s)(Ω′)^(−,•))^∗, a solution w ∈ (H^(−s)(Ω′)^(−,•))^∗ = H^s(Ω′)^(•,−) with ‖w‖ ≤ C‖f‖,
using [[lem:i-a-6-1]] (c). Uniqueness and the extension step finish (i) and (iii). ∎

**Corollary {#cor:i-a-6-5}** (The estimates used near ∂_♯X.) Let r₀ < b′ < b″ < r₂ − δ₀ (such radii exist since
r₀ + δ₀ < r₂, [[sec:i-a-1-1]]), and let χ₁ ∈ C_c^∞({b′ < r < b″}) equal 1 on a neighbourhood of supp dχ, where χ = 1 on
{r ≤ b′} and χ = 0 near {r ≥ b″}.
Let 𝒟 ⊂ ℂ be compact. Then for σ ∈ 𝒟,

    ‖χu‖_(H̄^s) ≤ C(‖P̂(σ)u‖_(H̄^(s−1)({r₀ < r < b″})) + ‖χ₁u‖_(H^s)),     u ∈ H̄^s,                        {#eq:i-a-6-1}

    ‖u|_(Ω_(r₀,b″))‖_(H^(1−s)(Ω_(r₀,b″))^(−,•)) ≤ C‖(P̂(σ)^(∗h)u)|_(Ω_(r₀,b″))‖_(H^(−s)(Ω_(r₀,b″))^(−,•)),
                                                                                      u ∈ Ḣ^(1−s).     {#eq:i-a-6-2}

*Proof.* The slab Ω_(r₀,b″) satisfies r₀ − δ₀ < r₀ < b″ < r₂ − δ₀, as [[prop:i-a-6-4]] requires. For
[[eq:i-a-6-1]]: χu ∈ H^s(Ω_(r₀,b″))^(•,−), and P̂(χu) = χP̂u + [P̂, χ]u, with [P̂, χ] ∈ Diff¹ supported in supp dχ.
Apply [[prop:i-a-6-4]] (i). For [[eq:i-a-6-2]]: the restriction of u to Ω_(r₀,b″) lies in
H^(1−s)(Ω_(r₀,b″))^(−,•) (supported at r₀, extendible at b″); apply [[prop:i-a-6-4]] (ii) to L = P̂(σ)^(∗h). The
constants are uniform in σ ∈ 𝒟 since the coefficients are polynomial in σ. ∎

### The spectral family at bounded nonzero frequencies {#sec:i-a-7}

**Lemma {#lem:i-a-7-1}** (Admissible orders exist, locally uniformly.) Let σ_* ≠ 0 be real. Fix constants
𝗋_in > (−1 + ϑ_in)/2 − α₊ and 𝗋_out < −½ + S̄ − α₊ with 𝗋_in ≥ 𝗋_out, and s_c > ½ + ϑ_ℋ. Then there is an order pair
(s, 𝗋) admissible for every σ₀ in a neighbourhood J of σ_*, with weight α₊ and a margin independent of σ₀ ∈ J.

*Proof.* Take s ≡ s_c. Let ε_* := sgn σ_* and J := {σ₀ : |σ₀ − σ_*| < |σ_*|/4}. Let Θ ∈ C^∞(ℝ) satisfy ε_*Θ′ ≤ 0,
Θ = 1 on {ε_*ξ ≤ −(3/2)|σ_*|} and Θ = 0 on {ε_*ξ ≥ −½|σ_*|}. Let χ_c ∈ C_c^∞ equal 1 on {ξ² + |η|² ≤ (3|σ_*|)²},
which contains Σ^∂_(σ₀) for σ₀ ∈ J ([[lem:i-a-4-5]]: |ξ| ≤ 2|σ₀| and |η| ≤ |σ₀| there). On the boundary face set

    𝗋 := 𝗋_out + (𝗋_in − 𝗋_out) Θ(ξ) χ_c(ξ² + |η|²),

and extend it smoothly. Every R_(σ₀,in), σ₀ ∈ J, has ε_*ξ = −2|σ₀| < −(3/2)|σ_*|, where 𝗋 = 𝗋_in; and R_out has
ξ = 0, where 𝗋 = 𝗋_out. By [[eq:i-a-4-5]], 𝖧_(σ₀)ξ = 2|η|² at ρ = 0. So on Σ^∂_(σ₀),

    ε_*𝖧_(σ₀)𝗋 = (𝗋_in − 𝗋_out) ε_*Θ′(ξ) · 2|η|² ≤ 0,

which is (O2). The thresholds [[eq:i-a-1-5]] hold with the margins of the constants. ∎

Fix a fibre inner product h for the adjoints. For orders (s, 𝗋) and σ set

    𝒴_σ := H̄^(s−1,𝗋+α₊+1),     𝒳_σ := {u ∈ H̄^(s,𝗋+α₊) : P̂(σ)u ∈ 𝒴_σ},
    𝒳^∗_σ := {v ∈ Ḣ^(1−s,−𝗋−α₊−1) : P̂(σ)^(∗h)v ∈ Ḣ^(−s,−𝗋−α₊)},

the first two being the target and the domain of [Hin26c, (9.18)]. These are Hilbert spaces with the graph norms.

**Theorem {#thm:i-a-7-2}** (The spectral family at bounded nonzero frequencies.) Assume (H1)–(H4), and let α₊ ∈ ℝ.

(1) (*Fredholm estimates, I.*) Let I ⊂ (0, ∞) or I ⊂ (−∞, 0) be compact, ν ≥ 0 and N ∈ ℝ. Let I ∋ σ₀ ↦ (s, 𝗋_(σ₀))
be order pairs, continuous into C^∞, each admissible for σ₀ with weight α₊, with margins and constancy neighbourhoods
uniform in σ₀. There is C such that for σ = σ₀ + iσ₁ with σ₀ ∈ I and σ₁ ∈ [0, ν], writing 𝗋 := 𝗋_(σ₀),

    ‖u‖_(H̄^(s,𝗋+α₊)) ≤ C(‖P̂(σ)u‖_(H̄^(s−1,𝗋+α₊+1)) + ‖u‖_(H̄^(−N,−N))),     u ∈ 𝒳_σ,                      {#eq:i-a-7-1}

    ‖v‖_(Ḣ^(−s+1,−𝗋−α₊−1)) ≤ C(‖P̂(σ)^(∗h)v‖_(Ḣ^(−s,−𝗋−α₊)) + ‖v‖_(Ḣ^(−N,−N))),     v ∈ 𝒳^∗_σ.            {#eq:i-a-7-2}

(2) (*Fredholm estimates, II.*) Let I ⊂ ℝ be compact and 0 < ν^♭ ≤ ν. Let s satisfy (O1) with s_c > ½ + ϑ_ℋ, and let
𝗋 be constant near R_out with 𝗋 + α₊ < −½ + S̄ there. Then [[eq:i-a-7-1]] and [[eq:i-a-7-2]] hold uniformly for
σ ∈ I + i[ν^♭, ν].

(3) (*Fredholm property.*) In the settings of (1) and (2), P̂(σ) : 𝒳_σ → 𝒴_σ is Fredholm. Its kernel and the
annihilator of its range do not depend on the admissible orders. Its index is independent of
σ ∈ {σ ≠ 0, Im σ ≥ 0}. Under the hypotheses of [[thm:i-b-1-3]] the index is 0, since by [[thm:i-b-1-3]] (3) the
operator P̂(σ) is invertible for Im σ ≥ 0 and |σ| large.

(4) (*Higher b-regularity.*) If u ∈ 𝒳_σ and P̂(σ)u ∈ H̄^((s−1;k),𝗋+α₊+1) for some k ∈ ℕ₀, then
u ∈ H̄^((s;k),𝗋+α₊) and

    ‖u‖_(H̄^((s;k),𝗋+α₊)) ≤ C(‖P̂(σ)u‖_(H̄^((s−1;k),𝗋+α₊+1)) + ‖u‖_(H̄^(s,𝗋+α₊))).                          {#eq:i-a-7-3}

(5) (*Kernel elements.*) In the settings of (1) and (2), every u ∈ H̄^(s,𝗋+α₊) with P̂(σ)u = 0 lies in

    𝒜^(3/2+S̄−ε)(X̄; E) := ρ^(3/2+S̄−ε) C^∞_b(X̄; E)     for every ε > 0.                                   {#eq:i-a-7-4}

Here C^∞_b means smooth up to ∂_♯X and conormal at ∂X. Conversely, ⋂_(ε>0) 𝒜^(3/2+S̄−ε) ⊂ 𝒳_σ. If moreover S(0, ·)
has constant spectrum on ∂X, then

    u = ρ^(3/2+S(0,·))u₀ + ũ,     u₀ ∈ C^∞(∂X; E),     ũ ∈ 𝒜^(5/2+S̄−ε) for all ε > 0,                      {#eq:i-a-7-5}

where ρ^(3/2+S(0,·)) = ρ^(3/2) exp(S(0, ·) log ρ). This is the first step of [Hin26c, (9.21)] in dimension 4 + 1; the
weights 1 + S̄ and ρ^(1+S) of [Hin26c] are the values at n = 3.

(6) (*Regularity in σ.*) Suppose P̂(σ_*) : 𝒳_(σ_*) → 𝒴_(σ_*) is invertible. Then for σ near σ_*, with orders fixed
near σ_* as in [[lem:i-a-7-1]], the estimates [[eq:i-a-7-1]] and [[eq:i-a-7-3]] hold without their last terms,
uniformly, and P̂(σ) is invertible. For each j ∈ ℕ₀ and ε > 0, σ ↦ P̂(σ)⁻¹ is j times continuously differentiable
near σ_* in the strong operator topology, as a map H̄^((s+ε−1;j),𝗋+ε+α₊+1) → H̄^((s−ε;0),𝗋−ε+α₊) (orders those at σ_*).
If Im σ_* > 0, it is holomorphic near σ_* as a map H̄^(s−1,𝗋+α₊+1) → H̄^(s,𝗋+α₊−1). Finally, for k ∈ ℕ₀,

    ∂_σ^j P̂(σ_*)⁻¹ : H̄^((s−1;k+j),𝗋+α₊+1) → H̄^((s+j;k),𝗋+α₊)     boundedly.                              {#eq:i-a-7-6}

This is [Hin26c, Theorem 9.5] in dimension 4 + 1, on the bundle E, for a constant regularity order.

**Remark {#rem:i-a-7-3}** (Strong estimates; [Hin26c, Remark 9.6].) Each microlocal estimate used below holds in the
strong sense. Hence [[eq:i-a-7-1]] holds in the strong sense with the error term replaced by ‖u‖_(H̄^(s₀,𝗋₀+α₊)) for
orders s₀ < s and 𝗋₀ < 𝗋 that are still above the thresholds at ∂ℛ_± and at R_in: if the right side is finite, so is
the left. Likewise for [[eq:i-a-7-2]], with an a priori order at R_out.

#### The Fredholm estimates {#sec:i-a-7-1}

*Proof of (1).* Fix σ = σ₀ + iσ₁ as in (1), and write 𝐬 := (s, 𝗋 + α₊) and 𝐬′ := 𝐬 − (1, −1). All constants below are
uniform over σ₀ ∈ I and σ₁ ∈ [0, ν], for three reasons. The component estimates are uniform over compact parameter
sets. The order family is continuous. And the finite coverings chosen below for one σ₀ serve for σ₀′ near it, by
continuity of the flows and of the characteristic sets, so compactness of I leaves finitely many.

*The pieces.* Let χ, χ₁ and b′ < b″ be as in [[cor:i-a-6-5]], and χ_far := 1 − χ, supported in {r ≥ b′} ⊂ X̄°. Then
‖u‖_(H̄^𝐬) ≤ C(‖χu‖_(H̄^s) + ‖χ_far u‖_(H^𝐬)). Choose a finite microlocal partition of unity
χ_far = Σ_k Q_k + Q_res, with Q_k ∈ Ψ^(0,0), Q_res ∈ Ψ^(−∞,−∞) and kernels supported in {r > r₀ + ½(b′ − r₀)}².
Each Q_k is microsupported in one of the following open sets of the boundary of phase space, over the support of χ_far.

(A) A neighbourhood U_ℋ of ∂ℛ₊ ∪ ∂ℛ₋.

(B) A neighbourhood of a compact subset of ∂Σ₀ ∖ U′_ℋ, where Ū′_ℋ ⊂ U_ℋ.

(C) A neighbourhood U_in of R_(σ₀,in).

(D) A neighbourhood of a compact subset of Σ^∂_(σ₀) ∖ (U′_in ∪ U′_out).

(E) A neighbourhood U_out of R_out.

(F) The elliptic set of P̂(σ), uniformly in σ: fibre infinity off ∂Σ₀, including the corner over ∂X, where the symbol
is comparable to ξ² + |η|², and the boundary face off a neighbourhood of Σ^∂_(σ₀), where |G_σ| ≥ |g_(σ₀)| is bounded
below.

For each k choose B_k elliptic on WF′(Q_k) from the corresponding estimate, so that
‖Q_ku‖_𝐬 ≤ C(‖B_ku‖_𝐬 + ‖u‖_(−𝐍)). Let δ_in > 0 be the margin of the threshold at R_in in [[eq:i-a-1-5]], so that
𝗋 + α₊ ≥ (−1 + ϑ_in)/2 + δ_in there.

*The estimates, in order.* (A): [[prop:i-a-4-2]] (1), with s_c > s₀ > ½ + ϑ_ℋ, gives
‖B_Au‖_(s_c) ≤ C(‖GP̂u‖_(s_c−1) + ‖Gu‖_(s₀) + ‖u‖_(−N)). (B): by (H4) every point of ∂Σ₀ over {r ≥ b′} outside U′_ℋ
lies on a curve of 𝖧 whose backward continuation enters U′_ℋ in finite time. [[prop:i-a-5-2]], in the use (i) of
[[rem:i-a-5-2-uses]], with E microsupported in Ell(B_A), applies along it. By compactness finitely many curves
suffice. (Near r = b′ such a curve stays over {r > r₀} backward, since r increases backward.) (C): [[prop:i-a-4-6]]
(1), with 𝗋₀ := 𝗋 − δ_in/2 at R_in. (D): by [[lem:i-a-4-5]] every point of Σ^∂_(σ₀) outside U′_in ∪ U′_out lies on a
curve of ε₀𝖧_(σ₀) whose backward continuation enters U′_in. [[prop:i-a-5-2]], in the use (ii), applies, with E in
Ell(B_C) and the order monotone by (O2). (E): [[prop:i-a-4-9]] (1), with E elliptic on the set K_E^∗ of
[[lem:i-a-3-2]] and microsupported near it, U′_out being chosen disjoint from K_E^∗; the part of K_E^∗ on Σ^∂_(σ₀)
lies in the region (D), and its part off Σ^∂_(σ₀) lies in (F). (F): [[prop:i-a-5-1]]. Each E-term is bounded by the
estimates of earlier pieces. Each ‖GP̂(σ)u‖ is at most C‖P̂(σ)u‖_(H̄^(𝐬′)), since G has kernel supported in X̄°. The
orders used are those of 𝐬, through (O1)–(O3): at fibre infinity over the compact region only s_c matters, at the
boundary face only 𝗋 + α₊, and at the corner both, by ellipticity.

*The artificial boundary.* By [[eq:i-a-6-1]], ‖χu‖_(H̄^s) ≤ C(‖P̂(σ)u‖_(H̄^(s−1)) + ‖χ₁u‖_(H^s)). The function χ₁u
is compactly supported in {b′ < r < b″}, so ‖χ₁u‖_(H^s) is bounded by the pieces (B) and (F) over that region, at
order s_c.

*Absorbing the a priori terms.* Adding up,

    ‖u‖_(H̄^𝐬) ≤ C(‖P̂(σ)u‖_(H̄^(𝐬′)) + ‖u‖_(H̄^(𝐬−τ𝟏)) + ‖u‖_(H̄^(−𝐍))),     τ := min(s_c − s₀, δ_in/2) > 0.

The embedding H̄^𝐬 ↪ H̄^(𝐬−τ𝟏) is compact: take extensions, multiply by a fixed cut-off, and use (C4). Ehrling's lemma
then gives ‖u‖_(𝐬−τ𝟏) ≤ δ‖u‖_𝐬 + C_δ‖u‖_(−𝐍). For u ∈ H̄^𝐬 the left side is finite, so taking δ small and absorbing
proves [[eq:i-a-7-1]].

*The adjoint estimate.* For v ∈ Ḣ^(1−s,−𝗋−α₊−1), run the chain in the reverse order with the adjoint estimates.
(E∗): [[prop:i-a-4-9]] (2) at R_out, above threshold, with an a priori order −𝗋₀′ − α₊ − 1, where 𝗋 < 𝗋₀′ and
𝗋₀′ + α₊ < −½ + S̄ at R_out, which is possible by the margin in [[eq:i-a-1-5]]. (D∗): [[prop:i-a-5-2]] for P̂^(∗h) with
the backward field, propagating from U′_out; the order is −𝗋 − α₊ − 1, monotone along the backward field. (C∗):
[[prop:i-a-4-6]] (2), with E in the region (D∗). At fibre infinity: [[eq:i-a-6-2]] bounds v on {r₀ ≤ r ≤ b″} by
P̂^(∗h)v alone. (B∗): [[prop:i-a-5-2]] with the backward field, from that region toward ∂ℛ_±, since backward curves of
𝖧 starting near r₀ reach every point of ∂Σ₀ outside U′_ℋ. (A∗): [[prop:i-a-4-2]] (2), with E in the region (B∗). (F)
as before. The a priori term at R_out is absorbed as above, which proves [[eq:i-a-7-2]]. ∎

#### Away from the real axis {#sec:i-a-7-2}

*Proof of (2).* For σ₁ ≥ ν^♭ > 0, G_σ = g_(σ₀) + 2iσ₁ξ vanishes on the boundary face only where ξ = 0 = |η|, that is
on R_out. On the complement of a neighbourhood of R_out, |G_σ| is bounded below uniformly for σ ∈ I + i[ν^♭, ν],
including near fibre infinity. So the boundary face contributes only (E) and (F) (and (E∗) and (F) for the adjoint).
[[prop:i-a-4-9]] holds on the compact set I + i[ν^♭, ν] ⊂ {σ ≠ 0, Im σ ≥ 0}, and its E-term lies in (F). Fibre infinity
and the artificial boundary are as in (1). No condition on 𝗋 is used except at R_out. ∎

#### The Fredholm property {#sec:i-a-7-3}

**Lemma {#lem:i-a-7-green}** (Green's formula.) In the settings of [[thm:i-a-7-2]] (1) and (2), for u ∈ 𝒳_σ and
v ∈ 𝒳^∗_σ, ⟨P̂(σ)u, v⟩_h = ⟨u, P̂(σ)^(∗h)v⟩_h, where ⟨·, ·⟩_h are the pairings of [[lem:i-a-6-1]] (b) with the weight
H inserted, for which P̂^(∗h) is the adjoint.

*Proof.* With 𝐬 and 𝐬′ as in [[sec:i-a-7-1]], let f := P̂u, and extend χu beyond r₀ as a solution. With
a′ ∈ (r₀ − δ₀, r₀), let f′ extend P̂(χu) to Ω_(a′,b″), and let w solve P̂w = f′ there ([[prop:i-a-6-4]] (iii)); by
uniqueness w = χu on Ω_(r₀,b″). Then ũ := χ′(w + (1 − χ)u), with χ′ a cut-off equal to 1 on
{r ≥ r₀ − ½(r₀ − a′)} and supported in {r > a′}, lies in H^𝐬(ℝ⁴), restricts to u, and has P̂ũ ∈ H^(𝐬′)(ℝ⁴). With T_t
from (C8), u_t := T_tũ is Schwartz, u_t → ũ in H^𝐬, and P̂u_t = T_tP̂ũ + [P̂, T_t]ũ → P̂ũ in H^(𝐬′). This uses that
[P̂, T_t] is bounded in Ψ^(1,−1), maps H^𝐬 to H^(𝐬′), and tends to 0 strongly (as in [[lem:i-a-3-1]], Step 1). For
Schwartz u_t the identity is the definition of P̂^(∗h)v as a distribution. Pass to the limit, using that v and
P̂^(∗h)v are supported in X̄, so that the pairings see only u and P̂u. ∎

*Proof of (3).* *Fredholm.* The embedding 𝒳_σ ↪ H̄^(−N,−N) is compact for N > max(−s, sup(−𝗋 − α₊)), so
[[eq:i-a-7-1]] gives a finite-dimensional kernel and closed range (Peetre's lemma). Likewise [[eq:i-a-7-2]] for
P̂^(∗h) on 𝒳^∗_σ.

*Cokernel.* An element v ∈ Ḣ^(1−s,−𝗋−α₊−1) = (𝒴_σ)^∗ annihilates the range if and only if v ∈ ker_(𝒳^∗_σ) P̂^(∗h).
Indeed, C_c^∞(ℝ⁴)|_(X̄) ⊂ 𝒳_σ, so an annihilator satisfies ⟨φ, P̂^(∗h)v⟩ = 0 for all φ ∈ C_c^∞(ℝ⁴); the converse is
[[lem:i-a-7-green]]. Symmetrically, w ∈ H̄^(s,𝗋+α₊) = (Ḣ^(−s,−𝗋−α₊))^∗ annihilates P̂^(∗h)(𝒳^∗_σ) if and only if
w ∈ ker_(𝒳_σ) P̂, testing with C_c^∞(X̄°) ⊂ 𝒳^∗_σ. Hence ind(P̂^(∗h)|_(𝒳^∗_σ)) = −ind(P̂|_(𝒳_σ)).

*Independence of the orders.* By (5), whose proof uses only (1), (2) and (4), kernel elements lie in
⋂_ε 𝒜^(3/2+S̄−ε), which is contained in 𝒳_σ for every admissible order. For the adjoint: if v lies in the kernel for
one admissible order, the strong forms of the adjoint estimates place it in the space of any other. At R_out the
adjoint estimate is above threshold, with the a priori order given by the space of v itself (whose order is above the
threshold, by (O3)). Elsewhere the adjoint estimates are below threshold or propagation estimates, with no a priori
condition.

*Local constancy of the index.* Let σ_* be in one of the settings, and fix orders admissible for all σ near σ_*:
[[lem:i-a-7-1]] if σ_* is real, any 𝗋 as in (2) if Im σ_* > 0. Let 𝒩 := ker P̂(σ_*). Let 𝒲 ⊂ C_c^∞(X̄°; E) be a
complement of the closed, finite-codimensional range in 𝒴_(σ_*); it exists because C_c^∞(X̄°) is dense in 𝒴_(σ_*).
Let E₀₁ : ℂ^(dim 𝒲) → 𝒲 be an isomorphism and E₁₀u := (⟨u, v_j⟩)_j with v_j ∈ C_c^∞(X̄°) chosen so that E₁₀|_𝒩 is an
isomorphism. Then the operator

    P^♯(σ) := ( P̂(σ)   E₀₁ )
              ( E₁₀     0  )

has index ind P̂(σ) + dim 𝒲 − dim 𝒩, and is invertible at σ_*.

*Injectivity.* P^♯(σ) is injective for σ near σ_*. Otherwise there are σ_j → σ_* and (u_j, c_j) ≠ 0 in the kernel,
normalised by ‖u_j‖_(−𝐍) + |c_j| = 1. By [[eq:i-a-7-1]], ‖u_j‖_𝐬 ≤ C(|c_j| + ‖u_j‖_(−𝐍)) ≤ C. Pass to a subsequence
with u_j ⇀ u in H̄^𝐬, hence u_j → u in H̄^(−𝐍) (compactness), and c_j → c. Then ‖u‖_(−𝐍) + |c| = 1. Moreover
P̂(σ_j)u_j → P̂(σ_*)u as distributions, so P̂(σ_*)u = −E₀₁c and u ∈ 𝒳_(σ_*), and E₁₀u = lim E₁₀u_j = 0. This
contradicts the invertibility of P^♯(σ_*).

So ind P̂(σ) ≤ dim 𝒩 − dim 𝒲 = ind P̂(σ_*) near σ_*. The same argument for the adjoint family, with [[eq:i-a-7-2]],
gives ind P̂^(∗h)(σ) ≤ ind P̂^(∗h)(σ_*), that is ind P̂(σ) ≥ ind P̂(σ_*). So the index is locally constant, and by
independence of the orders it does not depend on the local choice of orders. The set {σ ≠ 0, Im σ ≥ 0} is connected
and covered by these neighbourhoods, so the index is constant. ∎

#### Higher b-regularity {#sec:i-a-7-4}

*Proof of (4).* Run the chain of [[sec:i-a-7-1]] with the orders 𝐬 + k𝟏 away from R_out, and with [[prop:i-a-4-9]]
(3) at R_out. By [[lem:i-a-4-10]], away from the zero section of the boundary face (and at fibre infinity)
H^((s;k),𝗋) and H^(s+k,𝗋+k) are microlocally the same, uniformly. The shifted orders still satisfy (O1)–(O3) at ∂ℛ_±
and R_in (they are larger there) and (O2) (shifted by a constant). Over compact subsets of X̄°, (s;k)-regularity is
H^(s+k), and [[cor:i-a-6-5]] holds at order s + k. The a priori terms are bounded by ‖u‖_(H̄^(s,𝗋+α₊)) because
u ∈ 𝒳_σ. ∎

#### Kernel elements {#sec:i-a-7-5}

**Lemma {#lem:i-a-7-4}** (Conormal functions and scattering spaces.) Let a ∈ ℝ.

(a) 𝒜^a ⊂ H̄^(s,𝗋′) for every s and every order 𝗋′ with 𝗋′ < a − 2 on a neighbourhood of the zero section o_(∂X) of
the boundary face.

(b) Conversely, if u ∈ H̄^((s;k),𝗋′) for every k, with 𝗋′ ≡ 𝗋_* constant near o_(∂X), then u ∈ ρ^(𝗋_*+2)C^∞_b
near ∂X.

*Proof.* Near ∂X, |dx| = ρ⁻⁵dρ dω, and μ_b := ρ⁴|dx| = ρ⁻¹dρ dω is the b-density. So
H^(0,𝗋_*)_sc = ρ^(𝗋_*)L²(|dx|) = ρ^(𝗋_*+2)L²(μ_b). Also H^((s;k),𝗋′) ⊂ H^(s+k,𝗋′). For k = 1: if u ∈ H^((s;1),𝗋′)
then ∂_ju = ⟨x⟩⁻¹(⟨x⟩∂_ju) ∈ H^(s,𝗋′+1) ⊂ H^(s,𝗋′), and u, ∂u ∈ H^(s,𝗋′) give u ∈ H^(s+1,𝗋′) by ellipticity of
⟨D⟩ ∈ Ψ^(1,0); induct on k. By [[lem:i-a-4-10]], microlocally away from o_(∂X), H^((s;k),𝗋′) is H^(s+k,𝗋′+k).

(a) For u = ρ^aw with V^αw bounded for all α, ∫ |V^αu|²ρ^(−2𝗋_*)|dx| < ∞ near ∂X if and only if
2a − 2𝗋_* − 5 > −1, that is 𝗋_* < a − 2. So u ∈ H^((0;k),𝗋_*) for all k, near o_(∂X) at order 𝗋_*, and away from it at
every order. Hence u ∈ H^(s,𝗋′) for every s and every 𝗋′ as stated.

(b) Let Q ∈ Ψ^(0,0) be microlocally the identity near o_(∂X), microsupported where 𝗋′ = 𝗋_*. Then
(Id − Q)u ∈ H^(∞,∞) by the last remark, and Qu ∈ H^((0;∞),𝗋_*), so ρ^(−𝗋_*−2)Qu ∈ H^∞_b(μ_b) near ∂X, as
[V, ρ^c] ∈ ρ^cC^∞. In t := −log ρ, the map (ρ, ω) ↦ (t, ω) takes b-vector fields to vector fields on the half-cylinder
(t₁, ∞) × 𝕊³ spanned by ∂_t and 𝒱(𝕊³), and μ_b to dt dω. Sobolev embedding on the unit cylinders (t₀, t₀ + 1) × 𝕊³,
with k > 2 and constants independent of t₀, gives H^∞_b(μ_b) ⊂ C^∞_b. ∎

*Proof of (5).* Let u ∈ H̄^(s,𝗋+α₊) with P̂(σ)u = 0. By [[rem:i-a-7-3]], u lies in H̄^(s′,𝗋′+α₊) for every admissible
(s′, 𝗋′), since the a priori terms are given by the space of u itself. In particular this holds for every s′ ≥ s and
for decay orders whose value at R_out is any number less than −½ + S̄ − α₊ ([[lem:i-a-7-1]], with [[lem:i-a-2-4]] for
the inner product at R_out). By (4) with f = 0, u ∈ H̄^((s′;k),𝗋′+α₊) for all k. [[lem:i-a-7-4]] (b), with
𝗋_* = (𝗋′ + α₊)(R_out) arbitrarily close to −½ + S̄, gives u ∈ ρ^(3/2+S̄−ε)C^∞_b near ∂X. Away from ∂X,
u ∈ H̄^(s′) for all s′, which is smoothness up to ∂_♯X. This proves [[eq:i-a-7-4]].

Conversely, let u ∈ ⋂_ε 𝒜^(3/2+S̄−ε). Since 𝗋 + α₊ is constant and less than −½ + S̄ near R_out = o_(∂X),
[[lem:i-a-7-4]] (a) with a = 3/2 + S̄ − ε (ε small) gives u ∈ H̄^(s,𝗋+α₊). Each part of P̂(σ) maps 𝒜^a to 𝒜^(a+1):
ρDiff¹_b, ρ²Diff²_b, ρ³Diff¹_b and ρ²C^∞ do. So P̂(σ)u ∈ 𝒜^(a+1) ⊂ H̄^(s−1,𝗋+α₊+1), again by [[lem:i-a-7-4]] (a).
Hence u ∈ 𝒳_σ.

*The leading term.* Let S₀ := S(0, ·), with constant spectrum. For an eigenvalue e of S₀, the Riesz projection
Π_e(ω) = (2πi)⁻¹ ∮_(|z−e|=δ) (z − S₀)⁻¹ dz is smooth, the contours being fixed. It commutes with S₀, and
N_e := (S₀ − e)Π_e is nilpotent and smooth. Let a := 3/2 + S̄ − ε. Near ∂X, P̂(σ)u = 0 and [[eq:i-a-1-2]] give

    (ρ∂_ρ − 3/2 − S₀)u = F′ := −(2iσρ)⁻¹(P̂(0) − iσQ + σ²g₀₀)u + (S − S₀)u ∈ 𝒜^(a+1),

because P̂(0)u ∈ 𝒜^(a+2), Qu ∈ 𝒜^(a+3), g₀₀u ∈ 𝒜^(a+2) and S − S₀ ∈ ρC^∞. Let v := Π_eu, μ := 3/2 + e and
g := Π_eF′; then (ρ∂_ρ − μ − N_e)v = g. Equivalently ∂_ρ(ρ^(−μ−N_e)v) = ρ^(−μ−N_e−1)g, and
‖τ^(μ+N_e)‖ ≤ Cτ^(Re μ)(1 + |log τ|)^(N−1), as N_e is nilpotent on ℂ^N.

Case Re μ < a + 1. Then ∫_0^(ρ₁) ‖s^(−μ−N_e−1)g(s)‖ ds < ∞, so

    v = ρ^(μ+N_e)c_e + ρ^(μ+N_e)∫_0^ρ s^(−μ−N_e−1)g(s) ds,     c_e ∈ C^∞(∂X; ran Π_e).

The integral term is bounded by Cρ^(a+1)∫_0^1 τ^(a−Re μ)(1 + |log τ|)^(N−1) dτ ≤ Cρ^(a+1). The same holds for its
V^α-derivatives: ρ∂_ρ of it is (μ + N_e) times it plus g, and angular derivatives fall on smooth factors. So it lies
in 𝒜^(a+1).

Case Re μ ≥ a + 1. Write v = ρ^(μ+N_e)ρ₁^(−μ−N_e)v(ρ₁) − ρ^(μ+N_e)∫_ρ^(ρ₁) s^(−μ−N_e−1)g ds. Both terms are
O(ρ^(a+1)|log ρ|^N) with their derivatives, hence in 𝒜^(a+1−ε′).

Summing over the eigenvalues e,

    u = Σ_(Re e < S̄+1−ε) ρ^(3/2+e+N_e)c_e + 𝒜^(5/2+S̄−ε−ε′).

This is ρ^(3/2+S₀)u₀ with u₀ := Σ_e c_e (the terms with Re e ≥ S̄ + 1 − ε being absorbed into the remainder), which
is [[eq:i-a-7-5]]. No condition on integer differences of the spectrum is needed for this step. ∎

#### Regularity in the spectral parameter {#sec:i-a-7-6}

*Proof of (6).* Fix orders admissible near σ_* ([[lem:i-a-7-1]], or (2)), and let 𝐬 = (s, 𝗋 + α₊) and
𝐬′ = 𝐬 − (1, −1) as in [[sec:i-a-7-1]].

*Estimates without error terms.* If [[eq:i-a-7-1]] without its last term failed uniformly near σ_*, there would be
σ_j → σ_* and u_j with ‖u_j‖_𝐬 = 1 and ‖P̂(σ_j)u_j‖_(𝐬′) → 0. By [[eq:i-a-7-1]], ‖u_j‖_(−𝐍) ≥ c > 0. A weak limit in
H̄^𝐬, which is a norm limit in H̄^(−𝐍), is nonzero and lies in ker P̂(σ_*). That is a contradiction. The same argument
applies to [[eq:i-a-7-3]].

*Invertibility.* By the above, P̂(σ) is injective near σ_*; by (3) its index equals that at σ_*, which is 0. So it is
invertible, with ‖P̂(σ)⁻¹‖_(𝒴_σ→H̄^𝐬) ≤ C uniformly.

*Continuity.* Let f ∈ H̄^(𝐬′+ε𝟏) and u(σ) := P̂(σ)⁻¹f. The orders 𝐬 ± (ε/2)𝟏 are admissible for ε small (the
margins), so u(σ) is bounded in H̄^(𝐬+(ε/2)𝟏). For σ_j → σ, a subsequence converges weakly there, hence in norm in
H̄^(𝐬−ε𝟏), to some u₀ with P̂(σ)u₀ = f. By uniqueness in 𝒳_σ at the orders 𝐬 − ε𝟏 (admissible), u₀ = u(σ), so the
whole sequence converges.

*Differentiability.* P̂(σ) − P̂(σ_*) = (σ − σ_*)(T + (σ + σ_*)P₂), so

    (P̂(σ)⁻¹ − P̂(σ_*)⁻¹)/(σ − σ_*) = −P̂(σ)⁻¹(T + (σ + σ_*)P₂)P̂(σ_*)⁻¹.

T ∈ ρDiff¹_b near ∂X (by [[eq:i-a-1-2]]) and P₂ ∈ ρ²C^∞. So T maps H̄^((t;q),𝗍) to H̄^((t;q−1),𝗍+1), trading one
b-derivative for one order of decay; away from ∂X it is a first-order operator, and (t;q)-regularity is H^(t+q) there.
Hence f ∈ H̄^((s+ε−1;1),𝗋+ε+α₊+1) maps under P̂(σ_*)⁻¹ to H̄^((s+ε;1),𝗋+ε+α₊) by (4), and then under T + (σ + σ_*)P₂
to H̄^(s+ε,𝗋+ε+α₊+1). By continuity, P̂(σ)⁻¹ of that tends to P̂(σ_*)⁻¹ of it in H̄^(𝐬−ε𝟏). So the difference
quotients converge strongly, to −P̂⁻¹(T + 2σ_*P₂)P̂⁻¹. For j ≥ 2 the same argument runs at b-regular levels. First,
for q ∈ ℕ₀ and f ∈ H̄^((s+ε−1;q),𝗋+ε+α₊+1), σ ↦ P̂(σ)⁻¹f is continuous into H̄^((s−ε;q),𝗋−ε+α₊): the argument for
continuity applies with [[eq:i-a-7-3]], uniform near σ_* by the first paragraph, in place of [[eq:i-a-7-1]], since
H̄^((t;q),𝗍) ↪ H̄^((t′;q),𝗍′) is compact for t′ < t and 𝗍′ < 𝗍 ((C4) for each b-derivative up to order q). Then
∂^j_σP̂⁻¹, a finite sum of products as in the proof of [[eq:i-a-7-6]] below, is obtained from ∂^(j−1)_σP̂⁻¹ as
∂_σP̂⁻¹ was from P̂⁻¹: the difference quotient of a product splits into terms in which one factor P̂⁻¹ is differenced,
handled by the case j = 1 at a b-regular level, and terms in which a factor D_i is differenced, polynomial in σ. Every
factor is uniformly bounded and strongly continuous between the spaces of [[eq:i-a-7-6]] with ε-losses, so the
products are strongly continuous. This spends j b-derivatives and jε in orders; renaming ε gives the C^j statement.

*Holomorphy.* For Im σ_* > 0 the orders in (2) may have any decay order below the threshold at R_out, so 𝗋 − 1 is
admissible. The operator T + (σ + σ_*)P₂ ∈ Ψ^(1,0) maps H̄^(s,𝗋+α₊) to H̄^(s−1,𝗋+α₊), and P̂(σ)⁻¹ maps that to
H̄^(s,𝗋+α₊−1), uniformly near σ_*. So ‖P̂(σ)⁻¹ − P̂(σ′)⁻¹‖ ≤ C|σ − σ′| for σ, σ′ near σ_*, as maps
𝔄 := H̄^(s−1,𝗋+α₊+1) → 𝔅 := H̄^(s,𝗋+α₊−1), and likewise at the orders (s, 𝗋 − 1). A Lipschitz bound does not by itself
make difference quotients converge, so we argue as follows. The difference quotient is D(σ) := −P̂(σ)⁻¹M(σ)P̂(σ_*)⁻¹,
where M(σ) := T + (σ + σ_*)P₂, and

    D(σ) − D(σ′) = −(P̂(σ)⁻¹ − P̂(σ′)⁻¹)M(σ)P̂(σ_*)⁻¹ − (σ − σ′)P̂(σ′)⁻¹P₂P̂(σ_*)⁻¹.

By the Lipschitz bound at the orders (s, 𝗋 − 1), both terms are O(|σ − σ′|) as maps 𝔄 → 𝔅′ := H̄^(s,𝗋+α₊−2). So D(σ)
is Cauchy in L(𝔄, 𝔅′) as σ → σ_*, and the same holds at every point near σ_*: P̂⁻¹ is holomorphic into L(𝔄, 𝔅′). It is
norm-continuous into L(𝔄, 𝔅) by the Lipschitz bound. Cauchy's integral formula over a small circle holds in L(𝔄, 𝔅′),
and its integrand is continuous into L(𝔄, 𝔅); so it represents P̂⁻¹ as a holomorphic L(𝔄, 𝔅)-valued function.

*The mapping property [[eq:i-a-7-6]].* ∂_σ^j(P̂⁻¹) is a sum of products P̂⁻¹D₁P̂⁻¹D₂ ⋯ D_mP̂⁻¹ with
D_i ∈ {∂_σP̂, ∂²_σP̂} = {T + 2σP₂, 2P₂} and Σ_i (order of the derivative in D_i) = j. Each D_i maps H̄^((t;q),𝗍) to
H̄^((t;q−1),𝗍+1) (and 2P₂ even to H̄^((t;q),𝗍+2)). Each P̂⁻¹ maps H̄^((t−1;q),𝗋+α₊+1) to H̄^((t;q),𝗋+α₊) for t = s + ℓ,
ℓ ≥ 0. That is (4) and invertibility at the orders (s + ℓ, 𝗋), which are admissible since raising s by a constant
preserves (O1)–(O3). Starting from H̄^((s−1;k+j),𝗋+α₊+1), each pair D_iP̂⁻¹ raises t by one and spends one
b-derivative, which ends in H̄^((s+j;k),𝗋+α₊). This is [Hin26c, (9.57)] in dimension 4 + 1; the formula
σ∂_σP̂(σ) = 2iσρ(ρ∂_ρ − 3/2 − S) − iσQ + 2σ²g₀₀ is [Hin26c, (9.56)] at n = 4. The count treats every D_i as spending
one b-derivative; the factors 2P₂ spend none, which only helps, since H̄^((t;q+1),𝗍) ⊂ H̄^((t+1;q),𝗍). ∎

### Uniformity in the operator {#sec:i-a-8}

**Theorem {#thm:i-a-8-1}** (Uniformity in the operator.) Assume (H1)–(H5). Then the constants in [[prop:i-a-4-2]],
[[prop:i-a-4-6]], [[prop:i-a-4-9]], [[prop:i-a-5-1]], [[prop:i-a-5-2]], [[prop:i-a-6-3]], [[prop:i-a-6-4]] and
[[thm:i-a-7-2]] (1), (2) and (4) can be chosen uniform in b ∈ ℬ, for fixed orders admissible at every b (with uniform
margins). The index in [[thm:i-a-7-2]] (3) is constant on connected subsets of {(σ, b)}. If P̂^(b_*)(σ_*) is
invertible, then P̂^b(σ) is invertible for (σ, b) near (σ_*, b_*), with uniformly bounded inverses that depend
continuously on (σ, b) in the strong operator topology, and the statements of [[thm:i-a-7-2]] (6) hold jointly in
(σ, b).

*Proof.* Every constant above is produced by finitely many seminorms of the coefficients of the operator, which depend
continuously on b by (H5). It is also produced by positivity margins: c_Q in each radial estimate, M in
[[prop:i-a-5-2]], and c₀ and C_P in [[prop:i-a-6-3]]. These margins depend continuously on the data ℋ, ρ_∞ and q_± and
on the order functions, so a choice made at b₁ serves for b near b₁ with halved margins. So does the finite covering of
the characteristic sets by flow boxes in [[sec:i-a-7-1]], with the flow-box coordinates of [[prop:i-a-5-2]] rebuilt at
each b from the flow of 𝖧_f^b through the same transversals, so that 𝖧_f^b = ∂_z exactly: the flows are continuous in b
in C^∞, and the backward entry times into the neighbourhoods of the radial sets are bounded by (H5), so the same
covering serves nearby. The commutants are built from these data and are bounded in their symbol classes uniformly in b
near b₁. Compactness of ℬ gives finitely many b₁. The index and invertibility statements follow by the arguments of
[[sec:i-a-7-3]] and [[sec:i-a-7-6]], run with sequences (σ_j, b_j) → (σ_*, b_*) in place of σ_j → σ_*: the uniform
estimates supply the bounds, and P̂^(b_j)(σ_j)u_j → P̂^(b_*)(σ_*)u as distributions supplies the limit. ∎

**Remark {#rem:i-a-comparison}** (Comparison with [Hin26c].) Besides the changes forced by the dimension and the sign of
the term in [Hin26c, (9.45)] ([[rem:i-a-4-8-sign]]), the proofs above differ from those of [Hin26c, Sections 9.1–9.2]
as follows. (a) At R_in and R_out [Hin26c, Propositions 9.10–9.11], the inequality 𝖧q ≥ cq holds only near the
characteristic set, so the symbol b_R is a smooth square root only after a cut-off to that set; the commutants here
carry ψ_Σ = ψ(ς_Σg²) with 𝖧g = 0, so that the cut-off costs nothing. At the horizon, [[lem:i-a-4-1]] replaces the
cut-off and the G₀-term of [Hin26c] by a defining function in S∗X̃°. (b) The regularisation and quantisation of the
commutants, which [Hin26c, p. 165] does not give, are [[lem:i-a-3-1]] and [[lem:i-a-3-2]], with steps κ ≤ ¼ so that
the effective order never leaves the admissible range. (c) [Hin26c, (9.39) and (9.50)] pair the commutator with u
itself. Where the absorbing term has top decay order (σ₁Re_h T at R_in, −ι_σ Σ_j W_j^(∗h)W_j at R_out), that pairing is
not defined for u in the a priori space; [[lem:i-a-3-1]] pairs only Schwartz approximants and passes to the limit in the
other terms. (d) Over ∂X, H_(Re G_σ)q = 4σ₀|η|² in the proof of [Hin26c, Proposition 9.10] (p. 167), which prints
2σ₀|η|²; only the sign is used ([[sec:i-a-4-3]]). (e) The estimates near the artificial boundary at every order
([[prop:i-a-6-4]]) are proved here; [Hin26c] cites [Hin25a, Corollary 9.38] for them.
