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
so that a neighbourhood of the boundary is [0, ρ₁)_ρ × 𝕊³_ω. Fix radii 0 < r₀ − 2δ₀ < r₀ < r₂ < r_h
[[pending:issue-1]] and set

    X̄ := {x : |x| ≥ r₀} ∪ ∂ℝ̄⁴,     ∂X := ∂ℝ̄⁴,     ∂_♯X := {|x| = r₀},     X̃ := {|x| > r₀ − 2δ₀} ∪ ∂X.

Write r := |x|. The radius r_h is that of the horizon in (H3), and ∂_♯X is the artificial boundary. All operators below
are defined on X̃. Every function space on X̄ is built from a space on ℝ⁴ through the extendible and supported
constructions at ∂_♯X of [[sec:i-a-6-1]], and every Schwartz kernel used has support in X̃ × X̃. The density is the
Euclidean one, |dx| = r³ dr dω = ρ⁻⁵ dρ dω near ∂X, where dω is the round density on 𝕊³.

The radii, and in particular the inner radius r₀ of the artificial boundary, are parameters. The results of this
chapter hold for every choice of them for which the hypotheses below hold, with constants that depend on the choice;
the cut-offs and dilations used near ∂_♯X ([[sec:i-a-6-1]]) are taken in proportion to r₀. The radii used for the
Myers–Perry metrics are fixed in [[ch:s12]].

#### The bundle {#sec:i-a-1-2}

Let E := X̃ × ℂ^N, N ≥ 1. The bundles of the later chapters are the restrictions to X̃ of T*M and S²T*M, for a
five-dimensional spacetime M, trivialised by dt_*, dx¹, …, dx⁴ and their symmetric products, with N = 5 and N = 15;
nothing below uses more than that E is trivial. (The letter N also denotes Sobolev orders, as in H^(−N), and in
[[sec:i-a-7-5]] it bounds a nilpotency index; the context separates them.) A *fibre inner product* is
h(x)(v, w) = ⟨H(x)v, w⟩_(ℂ^N), where H ∈ C^∞(ℝ̄⁴; End ℂ^N) is Hermitian, smooth on the compactification (that is,
smooth in (ρ, ω) up to ρ = 0), and satisfies c Id ≤ H ≤ C Id with c > 0. Let L²_h := L²(ℝ⁴; ℂ^N) with the norm
‖u‖²_h = ∫ h(u, u) |dx|, which is equivalent to the standard one. For an operator A, A^(*h) = H⁻¹A*H is its formal
adjoint in L²_h, and A* its adjoint in the standard L². We write Re_h A := ½(A + A^(*h)) and
Im_h A := (A − A^(*h))/2i.

#### The operator {#sec:i-a-1-3}

Let ℂ ∋ σ ↦ P̂(σ) ∈ Diff²(X̃°; E) be of the form

    P̂(σ) = P̂(0) + σT + σ²P₂.                                                                         {#eq:i-a-1-1}

This is the form of the spectral family e^(iσt_*) P₀ e^(−iσt_*) of a t_*-translation-invariant second-order operator
P₀, with T = −i[P₀, t_*] and P₂ of order 0 (compare [Hin26c, (9.30)]). For an operator A, σ_m(A) or σ(A) denotes its
principal symbol, of order m; σ₀ and σ₁, written without an argument, are the real and imaginary parts of the spectral
parameter, σ = σ₀ + iσ₁. The hypotheses are these.

(H1) (*Principal symbol.*) σ_2(P̂(0)) = G₀ Id, where G₀ ∈ C^∞(T*X̃°) is real, fibrewise quadratic and even in the
fibres, and σ_1(T) = τ₁ Id with τ₁ real and fibre-linear. P₂ = g₀₀ Id with g₀₀ a real function.

(H2) (*Structure at infinity*; [Hin26c, Definition 9.4 and (9.31)] at n = 4.) On {ρ < ρ₁},

    T = 2iρ(ρ∂_ρ − 3/2 − S) − iQ,     P̂(0) = ρ²P^(0),     g₀₀ ∈ ρ²C^∞(ℝ̄⁴),                             {#eq:i-a-1-2}

where S ∈ C^∞(ℝ̄⁴; End ℂ^N), Q ∈ ρ³Diff¹_b, and P^(0) ∈ Diff²_b with
P^(0) − ((ρD_ρ)² + Δ_(𝕊³)) Id ∈ Diff¹_b + ρ Diff²_b. All b-operators here have End ℂ^N-valued coefficients smooth on
the compactification, D = −i∂, and Δ_(𝕊³) ≥ 0 is the Laplacian of the round metric. The first equation in
[[eq:i-a-1-2]] is the form that the term −(n − 1)/2 of [Hin26c, (9.31)] takes at n = 4. Set

    S̄ := inf_(p ∈ ∂X) min Re spec S(0, p)     ([Hin26c, (5.2)]).

(H3) (*The horizon*; [Hin26c, Section 9.2.1, (1)–(4)].) Let ℋ := {r = r_h}. ℛ₊ is one of the two components of
N*ℋ ∖ o, and ℛ₋ := −ℛ₊; both lie in Σ₀ := {G₀ = 0}. Let ρ_∞ be positive, homogeneous of degree −1 and even near N*ℋ.
The *future-directed rescaled Hamilton vector field* on Σ₀ is 𝖧 := ±ρ_∞H_(G₀) on the component Σ₀^± containing ℛ_±.
Then for each sign

    β₀ := ρ_∞⁻¹𝖧ρ_∞ > 0 on ∂ℛ_±,     β := inf_(∂ℛ_±) (∓β₀⁻¹ρ_∞τ₁) > 0,                                 {#eq:i-a-1-3}

and there is a quadratic defining function q_± of ∂ℛ_± in ∂Σ₀ with 𝖧q_± ≥ c q_± near ∂ℛ_±, for some c > 0. Here ∂(·)
denotes the boundary at fibre infinity, viewed in S*X̃°. For the spectral family of a t_*-translation-invariant
operator, ∓ρ_∞τ₁ = 𝖧t_*, since τ₁ = −H_G t_* [Hin26c, (9.30)]; so the second condition is the condition β > 0 of
[Hin26c].

(H4) (*Dynamics at fibre infinity.*) ∂Σ₀ = ∂Σ₀⁺ ⊔ ∂Σ₀⁻ lies over {r ≤ r_e} for some r_e > r_h. Every maximal integral
curve of 𝖧 in ∂Σ₀ ∖ (∂ℛ₊ ∪ ∂ℛ₋) tends to ∂ℛ₊ ∪ ∂ℛ₋ as its parameter tends to −∞, and reaches {r < r₀ − δ₀} at a
finite positive parameter. On {r₀ − 2δ₀ < r < r₂}, G₀ is a Lorentzian form (signature (1, 3)) on each fibre of T*X̃,
dr is timelike for it (G₀(dr) < 0), and 𝖧r < 0 on ∂Σ₀ there: the future direction decreases r. (For a spectral family,
G₀ is g⁻¹ restricted to the annihilator of ∂_(t_*), and such a restriction of a Lorentzian form is Lorentzian wherever
it contains a timelike covector, as dr is inside the horizon.)

(H5) (*Uniformity data.*) P̂ may depend on a parameter b in a compact metric space ℬ, continuously into the
coefficient topology (every coefficient continuous in b into C^∞, and in the classes of (H2)). The objects ℋ, ρ_∞,
q_± and r_e in (H3)–(H4) may depend continuously on b, and the constants c, inf β₀ and β in (H3) and the lengths of
the curves in (H4) are bounded uniformly. [[sec:i-a-8]] uses (H5).

**Remark {#rem:i-a-hypotheses}** (On the hypotheses.) (a) By (H1) the principal symbol of P̂(σ), of order 2, is G₀ Id
for every σ. Since P̂(0) − P̂(0)^(*h) has vanishing principal symbol, Im_h P̂(0) ∈ Diff¹, and near ∂X it lies in
ρ²Diff¹_b. Indeed P̂(0) ∈ ρ²Diff²_b by [[eq:i-a-1-2]], adjoints preserve ρ²Diff²_b for the density ρ⁻⁵dρ dω (the
adjoint of a b-vector field is a b-operator), and the b-principal symbols cancel.

(b) By (H1), for σ ∈ ℂ,

    σ_1(Im_h P̂(σ)) = σ_1(Im_h P̂(0)) + (Im σ) τ₁ Id.                                                  {#eq:i-a-1-4}

To see this, write Im_h(σT) = (σT − σ̄T^(*h))/2i = (Re σ) Im_h T + (Im σ) Re_h T. Then Im_h T has order 0,
σ_1(Re_h T) = τ₁ Id, and σ²P₂ has order 0.

(c) (H3)–(H4) are the hypotheses of [Hin26c, Section 9.2.1] and the dynamics of [Hin26c, Section 9.1.1]. For the
operators of the later chapters, on the Schwarzschild–Tangherlini metric and the Myers–Perry metrics near it, the
dynamics in (H3)–(H4) is verified in [[ch:s12]], and the horizon threshold ϑ_ℋ of [[sec:i-a-1-4]] is evaluated where
each operator is studied ([[ch:s13]], [[ch:s14]]).

(d) P̂(σ)^(*h) satisfies (H1)–(H4) as well, with τ₁, S and Q replaced by τ₁, −S^(*h) and a suitable Q′, and with σ
replaced by σ̄. Only its principal symbol and its imaginary part enter below, and they are determined where they are
used.

#### Orders and thresholds {#sec:i-a-1-4}

The phase space is the scattering cotangent bundle ^(sc)T̄*ℝ̄⁴, compactified in the fibres. Its boundary consists of
*fibre infinity*, ^(sc)S*ℝ̄⁴, and the *boundary face* ^(sc)T̄*_(∂X)ℝ̄⁴ over ∂X, meeting at a corner. Near ∂X we write
scattering covectors as ξ dr + r η, with ξ ∈ ℝ and η ∈ T*𝕊³, so that (ρ, ω, ξ, η) are coordinates
([Hin26c, Section 9.2.2]; ξ and η are the ξ_sc and η_sc of [Hin26c]). For an h-self-adjoint endomorphism A, max spec A
and min spec A denote its largest and smallest eigenvalues.

**Definition {#def:i-a-admissible}** (Admissible orders.) An *order pair* is (s, 𝗋) with s ∈ ℝ a constant
(regularity; [[rem:i-a-1-1]]) and 𝗋 ∈ C^∞(^(sc)T̄*_(∂X)ℝ̄⁴) (decay), each extended smoothly to a neighbourhood of its
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

    ϑ_in := sup_(∂X) max spec(p_in − (S + S^(*h))),     p_in := σ(ρ⁻¹ Im_h P̂(0))|_(ξ = −2, η = 0)

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
Ψ^(m+m′,ℓ+ℓ′)_sc. By [HJS, Proposition 7.4], "A ∈ Ψ^(m,l)_sc(M) ⇒ A* ∈ Ψ^(m,l)_sc(M)", and
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
with s < s′ and r < r′, the embedding H^(s′,r′)_sc ↪ H^(s,r)_sc is compact." The L² pairing identifies (H^(s,r)_sc)*
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

(b) For a fibre inner product h, A^(*h) ∈ Ψ^(m,ℓ) and σ(A^(*h)) = σ(A)^(*h) := H⁻¹σ(A)^†H.

(c) If A = ã Id with ã ∈ Ψ^(m,ℓ)_sc scalar, and B ∈ Ψ^(m′,ℓ′), then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) and
σ(i[A, B]) = H_a σ(B), entrywise. If A ∈ Ψ^(m,ℓ) has scalar principal symbol a Id, and B has scalar principal symbol
b Id, then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) and σ(i[A, B]) = (H_a b) Id. More generally, if A has scalar principal symbol,
then [A, B] ∈ Ψ^(m+m′−1,ℓ+ℓ′−1) for every B ∈ Ψ^(m′,ℓ′): write A = ã Id + A′ with A′ ∈ Ψ^(m−1,ℓ−1) and use the first
statement and (a). This is what is meant below when a commutator with an operator of scalar principal symbol lowers
both orders.

(d) The statements (C3)–(C6) and (C8) hold for Ψ^(m,ℓ) and H^(s,𝗋), with T_t Id in (C8), ellipticity meaning that the
principal symbol is invertible with inverse bounded in the inverse orders.

*Proof.* (a) (AB)_ij = Σ_k A_ik B_kj, with (C1) entrywise. (b) (A*)_ij = (A_ji)*, so σ(A*) = σ(A)^† by (C1).
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

**Lemma {#lem:i-a-2-3}** (Microlocal square root.) Let K = K^(*h) ∈ Ψ^(2μ,2ν) have principal symbol k with
k ≥ c⟨ξ⟩^(2μ)⟨x⟩^(2ν) on a neighbourhood W of a closed set W₀ of the boundary of phase space. Then there is
L ∈ Ψ^(μ,ν) with WF′(K − L^(*h)L) ∩ W₀ = ∅. The construction depends continuously on K, and so is uniform for bounded
families with a uniform c.

*Proof.* Let χ ∈ C^∞ equal 1 near W₀ with support in W. Set L₀ := Op(χk^(1/2)), by [[lem:i-a-2-2]], and replace it by
(L₀ + L₀^(*h))/2. Then K − L₀^(*h)L₀ is h-self-adjoint, and by [[lem:i-a-2-1]] it lies in Ψ^(2μ−1,2ν−1) microlocally
near W₀, with h-self-adjoint principal symbol k₁. Given L₀, …, L_(j−1) with
K − (Σ_(i<j) L_i)^(*h)(Σ_(i<j) L_i) ∈ Ψ^(2μ−j,2ν−j) near W₀, of principal symbol k_j, solve
k^(1/2)l_j + l_j k^(1/2) = k_j for l_j. This Lyapunov equation has a unique solution, which is h-self-adjoint, given by

    l_j = ∫_0^∞ e^(−τk^(1/2)) k_j e^(−τk^(1/2)) dτ,

because k^(1/2) ≥ c^(1/2) on W; it lies in S^(μ−j,ν−j) by the chain rule. With L_j := Op(χl_j), the error drops one
order near W₀. Then L ∼ Σ_j L_j (asymptotic sum, (C1)). ∎

#### Inner products near ∂X {#sec:i-a-2-3}

**Lemma {#lem:i-a-2-4}** (Adapted fibre inner products.) For every ε > 0 there is a fibre inner product h such that
½ min spec(S + S^(*h)) ≥ S̄ − ε at every point of ∂X.

This is [Hin26c, Lemma 5.12] in dimension 4 + 1.

*Proof.* At one point p, let S(0, p) = V(D + J)V⁻¹ with D diagonal, Re D ≥ S̄ and J nilpotent upper triangular in
Jordan form. Let D_t := diag(1, t, t², …). Then D_t⁻¹(D + J)D_t = D + tJ, with ‖tJ‖ ≤ t. In the inner product
⟨u, v⟩_t := ⟨D_t⁻¹V⁻¹u, D_t⁻¹V⁻¹v⟩, S(0, p) is unitarily equivalent to D + tJ, so Re⟨Su, u⟩_t ≥ (S̄ − t)|u|²_t. Take
t = ε/2. The inequality Re h(Su, u) ≥ (S̄ − ε) h(u, u) is open in p, so it holds for this constant inner product on a
neighbourhood of p. It is also convex in h: if it holds for h₁, …, h_k, it holds for Σ χ_i h_i with χ_i ≥ 0 and
Σ χ_i = 1. Cover ∂X by finitely many such neighbourhoods, take a subordinate partition of unity, and extend the
resulting inner product smoothly to ℝ̄⁴. Since ½ min spec(S + S^(*h)) = min_(h(u,u)=1) Re h(Su, u), this is the claim.
∎

Different estimates below use different fibre inner products. All L²_h norms are equivalent, so each estimate proved in
one inner product holds in any other with a changed constant. No single inner product needs to serve two radial sets.

### The positive commutator lemma {#sec:i-a-3}

Orders are pairs 𝐬 = (s, 𝗋), the decay order possibly variable (C6), with 𝟏 := (1, 1) and 𝐍 := (N, N). Inequalities
between orders hold componentwise and pointwise. For an operator family, *microsupported in K uniformly* means that the
full symbols are supported in the closed set K, modulo a family bounded in Ψ^(−∞,−∞). For a fibre inner product h and
P ∈ Ψ^𝐦, write

    P_R := Re_h P = ½(P + P^(*h)),     P_I := Im_h P = (P − P^(*h))/2i.

**Lemma {#lem:i-a-3-1}** (One step.) Let P ∈ Ψ^𝐦, let 𝐬 be an order, 𝐤 := 𝐬 − ½(𝐦 − 𝟏), and κ ∈ (0, ½]. Let K₁ ⊂ U
with K₁ closed and U open in the boundary of phase space, and let G ∈ Ψ^(0,0) be elliptic on Ū. Suppose that for
ε ∈ (0, 1] there are the following.

(i) Ǎ_ε = Ǎ_ε^(*h), bounded in Ψ^𝐤, in Ψ^(𝐤−κ𝟏) for each ε, and microsupported in K₁ uniformly.

(ii) For a sign ς ∈ {1, −1}, the operator C_ε := i[P_R, Ǎ_ε²] + Ǎ_ε²P_I + P_IǍ_ε² satisfies

    ςC_ε = −B_ε^(*h)B_ε − F_ε + E_ε^(*h)E_ε + J_εP + R_ε.                                              {#eq:i-a-3-1}

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

This is algebra: 2 Im⟨Ǎ_εPw, Ǎ_εw⟩ = (1/i)⟨(Ǎ_ε²P − P^(*h)Ǎ_ε²)w, w⟩, and
Ǎ²P − P^(*h)Ǎ² = [Ǎ², P_R] + i(Ǎ²P_I + P_IǍ²). Let w_t := T_tv with T_t from (C8). We show that the right side of
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
Then ⟨J_εPv, v⟩ = ⟨J_εPv, Φ_Jv⟩ plus a term bounded by C‖u‖²_(−𝐍), since (Id − Φ_J)^(*h)J_ε is residual. The same
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
elliptic on Ū₀. Then there are a neighbourhood U_* of Γ and a closed set K_E^* ⊂ Ū₀ ∖ Γ such that for every
E ∈ Ψ^(0,0) elliptic on K_E^*, every B ∈ Ψ^(0,0) microsupported in U_* and every 𝐍,

    ‖Bu‖_𝐬 ≤ C(‖GPu‖_(𝐬−𝐦+𝟏) + ‖Eu‖_𝐬 + ‖Gu‖_(𝐬₀) + ‖u‖_(−𝐍)),                                           {#eq:i-a-3-5}

in the strong sense: if the right side is finite, so is the left.

*Proof.* Let J be an integer with J ≥ 4τ, let κ := τ/J ≤ ¼, and let 𝐬_j := 𝐬₀ + jκ𝟏, so that 𝐬_j − κ𝟏 = 𝐬_(j−1).
Construct U₀ ⊃ U₁ ⊃ … ⊃ U_J ⊃ Γ inductively, U_j being the U′ of the hypothesis for (𝐬_j, κ, U_(j−1)), with B₀^(j)
elliptic on Ū_j, and let K_E^* := ⋃_(j=1)^J K_E(U_(j−1)), a finite union of closed sets missing Γ (the sets move with
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

    V(φ_ε²) = 2κ θ_ε (ϱ⁻¹Vϱ) φ_ε²,     V(ϱ^(−a)φ_ε²) = −(a − 2κθ_ε)(ϱ⁻¹Vϱ) ϱ^(−a)φ_ε².                       {#eq:i-a-3-6}

Indeed φ_ε² = ϱ^(2κ)(ϱ + ε)^(−2κ), so V log φ_ε² = 2κ(1 − ϱ(ϱ + ε)⁻¹)ϱ⁻¹Vϱ = 2κθ_εϱ⁻¹Vϱ. The same formula shows that
φ_ε is bounded in S⁰ (in ϱ), lies in S^(−κ) for each ε > 0, and tends to 1 in S^δ for every δ > 0, and that θ_ε is
bounded in S⁰. So regularising a commutant of weight ϱ^(−a), a = 2𝗌′ − 1, replaces 𝗌′ by an effective order
𝗌′_ε := 𝗌′ − κθ_ε ∈ (𝗌′ − κ, 𝗌′] in the component the regulariser acts on. In [[lem:i-a-3-2]] that interval is
(𝗌_(j−1), 𝗌_j] ⊂ [𝗌₀, 𝗌].
