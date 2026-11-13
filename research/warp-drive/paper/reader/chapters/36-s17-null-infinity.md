## Null infinity, resonant states and the transition face {#ch:s17}

This chapter studies the linearised gauge-fixed Einstein operator L_b of [[ch:s15]] near future null infinity and at
the transition face, for Myers–Perry parameters b near b₀, in three steps.

The first, [[sec:iii-c-1]]–[[sec:iii-c-5]], concerns the exterior region near spatial and future null infinity. It
introduces corner coordinates there, the classes of metric perturbations with partial expansions at ℐ⁺, the structure
of the gauge-fixed operator at ℐ⁺ ([[prop:iii-c-4-4]]) and its mapping properties on these classes
([[prop:iii-c-5-2]], [[cor:iii-c-5-3]]). This is [Hin26, Definitions 5.1–5.4 and 5.13, Remark 5.5, Proposition 5.11
with (5.40)–(5.41a), Proposition 5.14 and Corollary 5.15] (pp. 84–99) in dimension 4 + 1, with the parts of [Hin26,
Lemmas 5.6–5.8, Corollaries 5.9–5.10] that these use. [Hin26, Sections 5.4–5.7] (Lemma 5.16, Theorems 5.17, 5.21 and
5.23, Proposition 5.25) and the edge-b form (5.26b) that their energy estimates use are carried to dimension 4 + 1 in
[[ch:s26]].

The second, [[sec:iii-g3-1]]–[[sec:iii-g3-3]], extends the inverse of the ι⁺-normal operator of [[ch:s16]] to sources
with partial expansions at ℐ⁺ ∩ ι⁺, locates the incoming poles this creates ([[cor:iii-g3-2-6]]), and describes the
quasi-homogeneous solutions and resonant states at ι⁺ ([[prop:iii-g3-3-7]]). This is [Hin26, Section 9.1.3]
(pp. 180–186) in dimension 4 + 1: Lemmas 9.13–9.14, Proposition 9.15, Definition 9.16 with (9.49), Remark 9.17,
Corollary 9.18, Definition 9.19, Remark 9.20, Lemma 9.21, (9.54)–(9.55), Proposition 9.22 and Remarks 9.23–9.24.
[Hin26] uses this material only in its Section 12.

The third, [[sec:iii-g4-1]]–[[sec:iii-g4-5]], is [Hin26, Section 9.2] (pp. 186–199) in dimension 4 + 1: the formal
solutions at the corner ztf of the transition face ((9.57)–(9.61), Definition 9.25), the expansion at r̂ = 0 of the
inverse of the tf-normal operator (Lemma 9.26, Remarks 9.27–9.28), the grafting of tf-solutions into the low-energy
space (Definition 9.29, (9.72), Proposition 9.30, Remarks 9.31–9.34) and its conormal version (Proposition 9.35).
[Hin26] uses these results from its Section 11.5 on.

Two further sections complete the chapter. [[sec:s17-radiative]], after the second step, collects in
[[prop:np-10-38]] the operator at null infinity in dimension 4 + 1, entry by entry, and what it gives for the order at
which a radiative term at null infinity reaches future timelike infinity. [[sec:s17-exterior]], at the end, gives in
[[prop:np-10-64]] the quantities through which the spatial dimension enters [Hin23a, Section 3], the energy estimates
near null and spatial infinity that [[ch:s26]] carries to dimension 4 + 1; [[ch:s26]] uses them.

The notation is that of [[ch:s11]]–[[ch:s16]]. In particular n = 4, D = 5; the family g_b, b = (m, A) ∈ ℬ, of
[[sec:iii-b-3]], with m₀, R₁ = m₀^(1/2), the compactification M and its faces I₀, ℐ⁺, ι⁺, K⁺ ([[def:iii-b-2-1]]); the
gauge-fixed operator of [[sec:iii-b-6]]; the linearised operator L_b and its Minkowski model L̄ of [[ch:s15]], with the
endomorphism S̄ of [[lem:iii-f-2-1]] and its spectrum [[eq:iii-f-3-1]]; and the index sets and partially polyhomogeneous
spaces of [[sec:iii-a-1]]. We write the spectral families of [[ch:s15]] with a hat: L̂_b(σ) := L_b^(σ) and
L̄̂(σ) := L̄^(σ), so that 2L̄̂(0) = (2L̄)^(0) and L̂_b(0) is the zero energy operator. No step of this chapter involves
the inner radius r₀ of the spaces of [[ch:s01]]: the exterior region below is a neighbourhood of I₀ ∪ ℐ⁺ of radius at
least 4R₁, and the results at ι⁺ and at the transition face concern faces at infinity and meet the inner radius only
through the results of [[ch:s15]] and [[ch:s16]] that they use.

### Hypotheses, the exterior region, and its coordinates {#sec:iii-c-1}

**Remark {#rem:s17-dimension}** (What dimension 4 + 1 changes at null infinity.) Three things change against [Hin26,
Section 5], and together they make the structure simpler.

(a) Radiation fields at null infinity decay like r^(−3/2), so the index sets at ℐ⁺ start at 3/2 where those of [Hin26]
start at 1 (as at ι⁺ ∩ ℐ⁺, [[def:iii-g1-1-2]]).

(b) The mass of Myers–Perry enters at |x|⁻² ([[prop:iii-b-3-6]]). At the corner I₀ ∩ ℐ⁺ it lies in the error class
ρ₀²ρ_I²C^∞, so the leading part there is that of Minkowski space, where [Hin26] carries the Schwarzschild terms.

(c) The contributions of the perturbation to the operator, the terms A^h − A₀ and B^h of [Hin26, (5.28)], carry at least
ρ_I^(1/2) relative to the constant matrix A₀, where in [Hin26] they are of the same order. They join the error, at the
cost of the index set ℰ_I^tot in place of ℰ_I^C in its perturbation part. So the structure theorem
([[prop:iii-c-4-4]]) has a constant lower-triangular matrix Ā and no leading part depending on h. The coupling of the
radiation field of π̸₀h into π₁₁h through the (7, 6) entry of [Hin26, (5.28)] is half an order lower and lands in ℰ_I^C,
so π₁₁h carries no radiation field ([[rem:s17-no-radiation]]). The last index condition of [Hin26, Definition 5.3] is
strengthened to ℰ_I^tot + (ℰ_I^tot − 1) ⊂ ℰ_I^C ([[def:iii-c-3-1]]), which needs γ_Υ < 1/4.

Throughout this chapter we use, besides the notation fixed above, the time functions t_* = t − ψ(|x|) and t_IVP
([[eq:iii-b-3-6]], [[lem:iii-b-3-7]]), with t_* = t − |x| + C′ − 8m₀|x|⁻¹ on {|x| ≥ 3R₁}, and the gauge parameters of
[[sec:iii-f-1]], with, in addition,

    0 < γ_Υ < 1/4,     0 < e_Υ < 1.                                                                     {#eq:iii-c-1-1}

(The conditions [Hin26, (5.42)], v_C < 1, 0 < e_C < 1, γ_C > 0, 0 < e_Υ < 1, γ_Υ > 0, hold under the choices of
[[sec:iii-f-1]].) Let η := −dt² + dx² in the coordinates of [[sec:iii-b-2]], and

    x⁰ := t + |x|,     x¹ := t − |x|,     ρ₀ := 1/(2 − x¹),     ρ_I := (2 − x¹)/|x|,                      {#eq:iii-c-1-2}

the last two being the coordinates [[eq:iii-b-2-2]] near I₀ ∩ ℐ⁺. (Here x⁰ is that of Minkowski space; the x⁰ of
[[eq:iii-b-4-1]] for g_m is t + |x| − T_m(|x|), and the two null frames differ by I + ρ²C^∞, [[lem:iii-c-1-3]].) Fix
T₀ := C′ + 1 − 2R₁ and set

    Ω_ext := cl_M{t_* ≤ T₀},     U := Ω_ext ∩ {|x| ≥ 4R₁}.                                               {#eq:iii-c-1-3}

([Hin26, (5.1)] fixes T and shifts it to 1; the choice of T₀ only makes [[eq:iii-c-1-2]] global on U.) On U,
x¹ = t_* − C′ + 8m₀|x|⁻¹ ≤ T₀ − C′ + 2R₁ = 1, since m₀ = R₁².

**Lemma {#lem:iii-c-1-1}** (The corner coordinates.) (1) (ρ₀, ρ_I, ω), ω = x/|x|, are coordinates on all of U, smooth
up to I₀ and ℐ⁺: ρ₀ ∈ [0, 1], ρ₀ = 0 exactly at I₀, ρ_I = 0 exactly at ℐ⁺, and ρ₀ρ_I = |x|⁻¹. (2) With
X₀ := ρ₀∂_(ρ₀), X_I := ρ_I∂_(ρ_I) (at fixed ω and the other coordinate), exactly on U,

    ∂_(t_*)|_(ρ,ω) = ρ₀(X₀ − X_I),     ρ∂_ρ|_(t_*,ω) = X_I + 8m₀ρ₀²ρ_I(X₀ − X_I),     ρ := |x|⁻¹,         {#eq:iii-c-1-4}

    ∂₀ = −½ρ₀ρ_I X_I,     ∂₁ = ρ₀(X₀ − X_I + ½ρ_I X_I),                                                 {#eq:iii-c-1-5}

with ∂₀, ∂₁ the coordinate fields of (x⁰, x¹, ω). In particular ∂_t, ∂_(x^i), ∂₀, ∂₁ and |x|⁻¹∂_ω lie in ρ₀𝒱_b(U), and
∂₀, |x|⁻¹∂_ω ∈ ρ₀ρ_I𝒱_b(U).

*Proof.* (1) (x¹, |x|) ↦ (ρ₀, ρ_I) is a diffeomorphism of {x¹ < 2, |x| > 0} onto (0, ∞)², with inverse x¹ = 2 − ρ₀⁻¹,
|x| = (ρ₀ρ_I)⁻¹. Near I₀ ∩ ℐ⁺ these are the coordinates [[eq:iii-b-2-2]]. Near the interior of I₀, [[sec:iii-b-2]] uses
(τ, ρ) = (t/|x|, |x|⁻¹) with τ ∈ [−½, 1 − δ]; there ρ_I = 1 − τ + 2ρ and ρ₀ = ρ/ρ_I, smooth with smooth inverse
ρ = ρ₀ρ_I, τ = 1 − ρ_I + 2ρ₀ρ_I, as ρ_I ≥ δ. Near the interior of ℐ⁺, [[sec:iii-b-2]] uses (t₀, ρ) = (x¹, |x|⁻¹); there
ρ₀ = (2 − t₀)⁻¹ and ρ_I = (2 − t₀)ρ, smooth with smooth inverse for t₀ ≤ 1. These charts cover a neighbourhood of
(I₀ ∪ ℐ⁺) ∩ Ω_ext, and U meets no other face at infinity (it meets Σ^past and {t_* = T₀}, where the spaces are
extendible).

(2) A vector field aX₀ + bX_I is determined by its action on two functions of (ρ₀, ρ_I). With
t_* = 2 − ρ₀⁻¹ + C′ − 8m₀ρ₀ρ_I and ρ = ρ₀ρ_I: X₀t_* = ρ₀⁻¹ − 8m₀ρ, X_I t_* = −8m₀ρ, X₀ρ = X_Iρ = ρ. So ρ₀(X₀ − X_I) maps
t_* ↦ 1, ρ ↦ 0; and X_I + α(X₀ − X_I) with α := 8m₀ρ₀²ρ_I maps ρ ↦ ρ and t_* ↦ −8m₀ρ + αρ₀⁻¹ = 0. For
[[eq:iii-c-1-5]]: ∂₀|x| = ½, ∂₁|x| = −½, ∂₀x¹ = 0, ∂₁x¹ = 1; so ∂₀ρ₀ = 0, ∂₀ρ_I = −½ρ₀ρ_I², ∂₁ρ₀ = ρ₀²,
∂₁ρ_I = −ρ₀ρ_I + ½ρ₀ρ_I², which is [[eq:iii-c-1-5]]. The memberships: ∂_t = ∂₀ + ∂₁, ∂_(|x|) = ∂₀ − ∂₁,
∂_(x^i) = ω^i∂_(|x|) + |x|⁻¹(…)∂_ω, and |x|⁻¹∂_ω = ρ₀ρ_I∂_ω with ∂_ω (at fixed ρ₀, ρ_I) a b-vector field. ∎

For the null coordinates of the Tangherlini metric of mass m ([[eq:iii-b-4-1]]–[[eq:iii-b-4-2]]), with ρ₀, ρ_I defined by
[[eq:iii-c-1-2]] from their x¹ and |x|, the same calculation with ∂₀|x| = f/2, ∂₁|x| = −f/2, f := 1 − m|x|⁻², gives
∂₀ = −(f/2)ρ₀ρ_I X_I and ∂₁ = ρ₀(X₀ − X_I + (f/2)ρ_I X_I); [[eq:iii-c-1-5]] is the case f = 1.

*The splitting.* On U, in the rescaled frame (dx⁰, dx¹, |x|e^a), e^a a local orthonormal coframe of 𝕊³, the splitting
[Hin26, (5.27)] reads

    S²T* = ⟨(dx⁰)²⟩ ⊕ (2dx⁰ ⊗_s |x|T*𝕊³) ⊕ ⟨|x|²g̸⟩ ⊕ ⟨2dx⁰dx¹⟩ ⊕ (2dx¹ ⊗_s |x|T*𝕊³)
           ⊕ |x|² ker tr̸ ⊕ ⟨(dx¹)²⟩,                                                                   {#eq:iii-c-1-6}

of ranks 1 + 3 + 1 + 1 + 3 + 5 + 1 = 15: the splitting [[eq:iii-b-4-4]] for η, reordered. Here 2dx⁰dx¹ :=
dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰ and 2dx^i ⊗_s w := dx^i ⊗ w + w ⊗ dx^i. A symmetric 2-tensor h has rescaled components
h₀₀ = h(∂₀, ∂₀), h_(0ā) (the tangential part of h(∂₀, ·)), h₀₁ = h(∂₀, ∂₁), h_(1ā), h₁₁ = h(∂₁, ∂₁) and h_(āb̄) (the
tangential block, in the frame |x|e^a), as in [[sec:iii-b-4]], and its *slot coordinates* are, in the order of
[[eq:iii-c-1-6]],

    (h₀₀, h_(0ā), ⅓tr̸h, h₀₁, h_(1ā), π̸₀h, h₁₁),     tr̸h := g̸^(ab)h_(āb̄),                          {#eq:iii-c-1-7}

the third being the coefficient of |x|²g̸. Each of these is the coefficient of the basis element of the corresponding
summand: for instance the element 2dx⁰dx¹ of the fourth summand has h₀₁ = 1, as dx⁰(∂₀) = dx¹(∂₁) = 1 and
dx⁰(∂₁) = dx¹(∂₀) = 0.

**Definition {#def:iii-c-1-2}** ([Hin26, Definition 5.2] in dimension 4 + 1.) π_C h := (h₀₀, h_(0ā), tr̸h),
π₀₁h := h₀₁, π_(1/)h := h_(1ā), π̸₀h := h_(āb̄) − ⅓(tr̸h)g̸_(ab), π₁₁h := h₁₁. (The factor ⅓ replaces the ½ of [Hin26]:
π̸₀h is the trace-free part on 𝕊³.)

**Lemma {#lem:iii-c-1-3}** (Frames.) Three smooth frames of S²T* on U are used: the products of the Cartesian dt, dx^i;
those of dt_*, dx^i ([[ch:s15]]); and the rescaled null frame of [[eq:iii-c-1-6]]. Each is related to the next by a
smooth bundle map with smooth inverse, of the form F₀(ω)(I + ρ²C^∞(U)) with F₀ depending on ω alone.

*Proof.* dt_* = dt − ψ′(|x|)d|x| with ψ′ = 1 − 8m₀|x|⁻² on U, so dt_* = dx¹ + 8m₀|x|⁻²d|x|. Further d|x| = ω_i dx^i,
and |x|e^a is the orthonormal tangential projection of dx; both depend on ω alone. Finally dx⁰ = dt + d|x| and
dx¹ = dt − d|x|. ∎

So the spaces below, which are defined slot by slot in [[eq:iii-c-1-6]], do not depend on which of the null frames of
η, of g_m ([[eq:iii-b-4-2]]) or of ḡ ([[ch:s15]]) is used: these differ by I + ρ²C^∞, and ρ² = ρ₀²ρ_I² moves the index
sets of a component by 2 at both faces, into ℰ_I^C ([[lem:iii-c-3-2]] (c)).

### Function spaces, products {#sec:iii-c-2}

We use the notions of [[sec:iii-a-1]] without change: index sets, (z, k) for the smallest index set containing (z, k),
sums ℰ + ℱ, and the partially polyhomogeneous spaces H^(k,(ℰ₀,α₀),(ℰ_I,α_I))_b of [Hin26, Definition 2.8 and Notation
2.9], with the faces listed as I₀, ℐ⁺. On Ω_ext these are spaces of restrictions (extendible at {t_* = T₀}, Σ^past and
Σ^int), as [Hin26, (5.2)] has them; dim Ω_ext = 5. Sections of the summands of [[eq:iii-c-1-6]] are taken in local
trivialisations by e^a.

**Lemma {#lem:iii-c-2-1}** (Products.) Let Z be a manifold with corners of dimension d, compact or a relatively compact
domain in one, with boundary hypersurfaces H; let k > d/2, k′ ≥ k, u ∈ H^(k,(ℰ⃗,α⃗))_b(Z),
v ∈ H^(k′,(ℱ⃗,β⃗))_b(Z). Let γ_H ≤ α_H + β_H, γ_H < α_H + min Re ℱ_H and γ_H < β_H + min Re ℰ_H for every H
(min Re ∅ := +∞). Then uv ∈ H^(k,(ℰ⃗+ℱ⃗,γ⃗))_b(Z), and (u, v) ↦ uv is continuous.

*Proof.* (i) *No expansions.* H^k_b is H^k for a b-metric, which in logarithmic coordinates s_i = −log x_i near a corner
is uniformly equivalent to the Euclidean metric on a cover by unit cubes Q_m of bounded overlap. On one cube
‖fg‖_(H^k(Q)) ≤ C‖f‖_(H^k(Q))‖g‖_(H^(k′)(Q)) for k > d/2, k′ ≥ k (Sobolev embedding and the Leibniz rule), with C the
same for every cube. Summing, ‖fg‖²_(H^k) ≤ C² Σ_m ‖f‖²_(H^k(Q_m))‖g‖²_(H^(k′)(Q_m)) ≤ C′‖f‖²_(H^k)‖g‖²_(H^(k′)).
Weights multiply: ρ^α H^k_b · ρ^β H^(k′)_b ⊂ ρ^(α+β)H^k_b.

(ii) *Expansions.* Induct on the number of pairs (face, factor) at which a factor carries an expansion. Pick such a face
H and write, in a collar, u = χ Σ ρ_H^z (log ρ_H)^l u_((z,l)) + u′ (as in [Hin26, Definition 2.8, (2.3)]), and the same
for v (with no sum if v has none at H). The products of the sums give χ²ρ_H^(z+w)(log ρ_H)^(l+m)u_((z,l))v_((w,m))
(χ² − χ is supported where ρ_H ≥ ε/2 and goes to the remainder), with (z + w, l + m) ∈ ℰ_H + ℱ_H. The coefficient
u_((z,l))v_((w,m)) lies in the space on H that [Hin26, Definition 2.8] requires, by the lemma on H (dimension d − 1,
k > (d − 1)/2). Terms with Re(z + w) ≤ γ_H are kept; the others are ρ_H^(γ_H) times ρ_H^ε(log ρ_H)^(l+m), ε > 0, and go
to the remainder. A cross term χρ_H^z(log ρ_H)^l u_((z,l))v′ has weight Re z + β_H − ε′ at H for every ε′ > 0, which
exceeds γ_H by hypothesis, and fewer expansions, so the induction applies to it. The same holds for u′v and u′v′, the
last of weight α_H + β_H ≥ γ_H. Continuity follows from the same bounds. ∎

We use with it property (F1) of [[sec:iii-a-1]]: a b-vector field maps H^(k,(ℰ⃗,α⃗))_b to H^(k−1,(ℰ⃗,α⃗))_b.
Multiplication by C^∞ preserves the spaces, as index sets are closed under + ℕ₀, and multiplication by ρ_H^c shifts ℰ_H
and α_H by c.

### Metric perturbations {#sec:iii-c-3}

This section is [Hin26, Definitions 5.3–5.4, Remark 5.5] in dimension 4 + 1. Write

    σ_Υ := {0, (1 − e_Υ)γ_Υ, γ_Υ, 2γ_Υ} ⊂ [0, ½),

the eigenvalues of S̄ on the slots 4–7 ([[lem:iii-f-3-1]], [[lem:iii-c-4-2]]).

**Definition {#def:iii-c-3-1}** ([Hin26, Definition 5.3] in dimension 4 + 1.) Let ℰ₀, ℰ_I^C ⊂ ℂ × ℕ₀ be index sets
such that

(1) min Re ℰ₀ > 0 and jℰ₀ ⊂ ℰ₀ for all j ∈ ℕ;

(2) min Re ℰ_I^C > 3/2 + 2γ_Υ;

(3) with

    ℰ_I^tot := ℰ_I^C ∪ ⋃_(s∈σ_Υ) (3/2 + s, 0),                                                         {#eq:iii-c-3-1}

ℰ_I^tot + (ℰ_I^tot − 1) ⊂ ℰ_I^C.

This strengthens the condition ℰ_I^C + (ℰ_I^tot − 1) ⊂ ℰ_I^C of [Hin26, Definition 5.3], and it implies the condition
jℰ_I^tot ⊂ ℰ_I^C, j ≥ 2, there ([[lem:iii-c-3-2]] (b)). It is needed for [[prop:iii-c-5-2]]. Under the counterparts
of the conditions of [Hin26] alone, ℰ_I^C + (ℰ_I^tot − 1) ⊂ ℰ_I^C and jℰ_I^tot ⊂ ℰ_I^C for j ≥ 2, the conclusion of
[[lem:iii-c-3-2]] (b) fails. Indeed, let z₀ ∈ (3/2 + 2γ_Υ, 2) and let ℰ_I^C be the smallest index set containing (z₀, 0)
with these two properties. Every element it acquires beyond (z₀, 0) is z + j with z an element and j ≥ 1 (real part at
least z₀ + 1 > 2), or lies in ℰ_I^C + (ℰ_I^tot − 1) (real part at least z₀ + ½ > 2) or in jℰ_I^tot, j ≥ 2 (real part
at least 3). So (2, 0) ∉ ℰ_I^C, while
(3, 0) = 2(3/2, 0) ∈ 2ℰ_I^tot; and (3, 0) ∈ ℰ_I^C + 1 would need (2, 0) ∈ ℰ_I^C. Hence 2ℰ_I^tot ⊄ ℰ_I^C + 1.

Set

    ℰ_(I,01) := ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0),     ℰ_(I,1/) := ℰ_I^C ∪ (3/2 + γ_Υ, 0),
    ℰ̸_(I,0) := ℰ_I^C ∪ (3/2, 0),
    ℰ_(I,11) := ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0) ∪ (3/2 + 2γ_Υ, 0).                                      {#eq:iii-c-3-2}

Let k ≥ 5, ℓ₀ > 0 and ℓ_I > 3/2. Then H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_ext) ⊂ H^(k,0,0)_b(Ω_ext; S²T*) is the space of
real symmetric 2-tensors h whose restriction to U satisfies

    π_C h ∈ H^(k,(ℰ₀,ℓ₀),(ℰ_I^C,ℓ_I))_b,     π₀₁h ∈ H^(k,(ℰ₀,ℓ₀),(ℰ_(I,01),ℓ_I))_b,
    π_(1/)h ∈ H^(k,(ℰ₀,ℓ₀),(ℰ_(I,1/),ℓ_I))_b,     π̸₀h ∈ H^(k,(ℰ₀,ℓ₀),(ℰ̸_(I,0),ℓ_I))_b,
    π₁₁h ∈ H^(k,(ℰ₀,ℓ₀),(ℰ_(I,11),ℓ_I))_b.                                                            {#eq:iii-c-3-3}

If 0 < ℓ₀ < min Re ℰ₀ we write ℓ₀ for (ℰ₀, ℓ₀), and if 3/2 < ℓ_I < min Re ℰ_I^C we write (−, ℓ_I) for (⟨ℰ_I^C⟩, ℓ_I).

So π_C h decays strongly at ℐ⁺; π₀₁h and π_(1/)h decay like |x|^(−3/2−(1−e_Υ)γ_Υ) and |x|^(−3/2−γ_Υ); π̸₀h has a
radiation field at |x|^(−3/2); and π₁₁h carries the exponents 3/2 + 2γ_Υ (its own) and 3/2 + (1 − e_Υ)γ_Υ (from π₀₁h
through the entry (7, 4) of Ā), but no radiation field, unlike the exponent 1 of [Hin26]
([[rem:s17-no-radiation]]). The condition k ≥ 5 gives k − 2 > 5/2 = ½ dim Ω_ext, so [[lem:iii-c-2-1]] applies to
H^(k−2) factors.

**Lemma {#lem:iii-c-3-2}** (Consequences of [[def:iii-c-3-1]].) Under [[eq:iii-c-1-1]] and [[def:iii-c-3-1]]:

(a) ℰ_I^C + ½ ⊂ ℰ_I^C and ℰ_I^tot + ½ ⊂ ℰ_I^C; so ℰ_I^C + 1, ℰ_I^tot + 1 ⊂ ℰ_I^C, and (2, 0), (3, 0) ⊂ ℰ_I^C.

(b) jℰ_I^tot ⊂ ℰ_I^C + (j − 1) for j ≥ 2; in particular 2ℰ_I^tot ⊂ ℰ_I^C + 1.

(c) ℰ_I^tot + 2 ⊂ ℰ_I^C + 1, and every component index set of [[eq:iii-c-3-3]] lies in ℰ_I^tot.

(d) The intersections of ℰ_(I,01), ℰ_(I,1/), ℰ̸_(I,0), ℰ_(I,11) with {Re z > 3/2 + 2γ_Υ} equal that of ℰ_I^C ([Hin26,
remark (iii) after Definition 5.3]).

(e) For every index set ℰ̃ with min Re ℰ̃ > 3/2 + 2γ_Υ there is a smallest ℰ_I^C ⊇ ℰ̃ satisfying (2)–(3) of
[[def:iii-c-3-1]] ([Hin26, remark (ii) after Definition 5.3]).

*Proof.* (a) (3/2, 0) ⊂ ℰ_I^tot, so ½ ∈ ℰ_I^tot − 1, and (3) gives
ℰ_I^C + ½ ⊂ ℰ_I^tot + (ℰ_I^tot − 1) ⊂ ℰ_I^C, and likewise ℰ_I^tot + ½ ⊂ ℰ_I^C. Iterating gives + 1.
(2, 0) = (3/2, 0) + (½, 0) and (3, 0) = 2(3/2, 0).

(b) 2ℰ_I^tot = (ℰ_I^tot + (ℰ_I^tot − 1)) + 1 ⊂ ℰ_I^C + 1, using only (3); and
(j + 1)ℰ_I^tot ⊂ ℰ_I^C + (j − 1) + ℰ_I^tot = (ℰ_I^C + (ℰ_I^tot − 1)) + j ⊂ ℰ_I^C + j.

(c) From (a): ℰ_I^tot + 1 ⊂ ℰ_I^C. The component sets are unions of ℰ_I^C with some (3/2 + s, 0).

(d) The added sets are {3/2 + s + j}. For j = 0, 3/2 + s ≤ 3/2 + 2γ_Υ; for j ≥ 1,
3/2 + s + j ∈ ℰ_I^tot + 1 ⊂ ℰ_I^C by (a).

(e) Put Σ := ⋃_s (3/2 + s, 0), ℰ_((0)) := ℰ̃, and let ℰ_((m+1)) be the smallest index set containing ℰ_((m)) and
ℰ′_m + (ℰ′_m − 1), ℰ′_m := ℰ_((m)) ∪ Σ. Each new element has real part at least ½ more than an element it is built
from, and the generators in {Re z < C} are finitely many; so in each half plane {Re z < C} only finitely many elements
arise, after at most 2C steps, with bounded logarithmic orders. The union ℰ_I^C is an index set; it satisfies (3) by
construction, and (2) since new elements have real part at least 3/2 + ½ = 2 > 3/2 + 2γ_Υ by [[eq:iii-c-1-1]]. Every
set satisfying (2)–(3) and containing ℰ̃ contains each ℰ_((m)). ∎

**Definition {#def:iii-c-3-3}** ([Hin26, Definition 5.4] in dimension 4 + 1.) For ℰ₀ as in [[def:iii-c-3-1]] (1),
k ≥ 5, ℓ₀ > 0, ℓ_I > 3/2, H^(k,(ℰ₀,ℓ₀),⟨(3,0)⟩₀,ℓ_I)_b(Ω_ext) is the space of h with
π_C h, π₀₁h, π_(1/)h, π̸₀h ∈ H^(k,(ℰ₀,ℓ₀),((3,0),ℓ_I))_b and π₁₁h ∈ H^(k,(ℰ₀,ℓ₀),((2,0),ℓ_I))_b on U. By
[[lem:iii-c-3-2]] (a) it lies in H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b for every ℰ_I^C of [[def:iii-c-3-1]].

The class ⟨(2, 0)⟩₀ of [Hin26] has (1, 0) for π̸₀ and π₁₁. For π₁₁ that is the mass order, (2, 0) here. For π̸₀ it is the
radiation order; the class above contains no radiation field of π̸₀, and with (3/2, 0) in slot 6 the mapping property
[[eq:iii-c-5-3]] below would fail as soon as ℓ_I ≥ 5/2: the error term ρ₀²ρ_I²C^∞Diff²_b of [[eq:iii-c-4-4]] maps
ρ_I^(3/2) to ρ_I^(7/2), a term that (4, 0) does not contain and that does not lie in ρ_I^(ℓ_I+1)H^(k−2)_b, as
7/2 ≤ ℓ_I + 1. (For ℓ_I < 5/2 that term lies in the remainder; the backgrounds of [[def:iii-c-3-4]] and
[[lem:iii-c-3-5]] lie in the class with ℓ_I = ∞.) [Hin26] uses ⟨(2, 0)⟩₀ to subtract the radiation fields in
[Hin26, Theorem 5.21, Step 2] ((5.64), p. 104). In dimension 4 + 1 that subtraction is not needed ([[rem:iii-c1-3-2]]).

**Definition {#def:iii-c-3-4}** (The background class.) 𝒢 is the set of Lorentzian metrics g₀ on Ω_ext, smooth on M,
with

    g₀ − η ∈ ρ₀²ρ_I²C^∞(U; S²T*),     π(g₀ − η) ∈ ρ₀²ρ_I³C^∞(U)     (π ∈ {π_C, π₀₁, π_(1/), π̸₀}),        {#eq:iii-c-3-4}

equivalently g₀ − η ∈ H^(∞,(2,0),⟨(3,0)⟩₀,∞)_b(U) ([Hin26, footnote 55], in dimension 4 + 1 and with η in place of
g_m). [[prop:iii-c-4-4]] uses only the first condition; the second matters for perturbations measured from g_b.

**Lemma {#lem:iii-c-3-5}** ([Hin26, Remark 5.5] in dimension 4 + 1.) (1) g_b ∈ 𝒢 for every b ∈ ℬ. (2) For S ∈ 𝒮₁
small as in [[lem:iii-b-5-2]], φ_S^*g_b − g_b ∈ H^(∞,(2,0),⟨(3,0)⟩₀,∞)_b on U ∩ {χ_IVP(1 − χ_K) = 1}, so φ_S^*g_b
agrees there with an element of 𝒢.

*Proof.* (1) By [[prop:iii-b-3-6]], g_b − g_m ∈ |x|⁻³C^∞ = ρ₀³ρ_I³C^∞, and on {|x| ≥ 3R₁},
g_m − η = m|x|⁻²(dt − d|x|)² = mρ₀²ρ_I²(dx¹)², which has only the slot π₁₁. (2) By [[lem:iii-b-5-2]], there
φ_S^*g_b − g_b = |x|⁻²h_S(ω)(dx¹)² + ρ₀²ρ_I³C^∞, with h_S ∈ C^∞(𝕊³). ∎

Outside {χ_IVP(1 − χ_K) = 1} near I₀, φ_S is the flow of a cut-off boost, and φ_S^*η − η is of size O(1) there:
ℒ_(V(S))η = dχ ⊗_s X_w^♭, with dχ of size |x|⁻¹ and X_w^♭ of size |x|. So [Hin26, Remark 5.5] holds where φ_S is the
boost. [Hin26, Section 5.6] modifies the gauge near I₀ by a cut-off χ₀ ((5.76) there); this is carried to dimension
4 + 1 in [[ch:s26]].

### The structure at null infinity {#sec:iii-c-4}

This section is [Hin26, Proposition 5.11 and (5.40)–(5.41a)] in dimension 4 + 1. The operator is that of
[[eq:iii-b-6-8]]: for metrics g, g₀,

    L^(g,g₀) := L_(g,g₀) = ½□_g + E^C_(g₀)δ_gG_g + (δ^*_(g₀) − δ^*_g)δ_gG_g + R_g
                           + δ^*_(g₀,E_C)(C_(g,g₀) − Y_(g,g₀) + E^Υ_(g₀)G_(g₀)),                          {#eq:iii-c-4-1}

the derivative D₁|_((g,g₀))P of [Hin26], with L^(g_b,g_b) = L_b of [[eq:iii-f-1-1]].

**Lemma {#lem:iii-c-4-1}** (The background at the corner.) On U, in the frame of products of dt_*, dx^i,

    L_b = −ρ₀²ρ_I(X_I − 3/2 − S̄)(X₀ − X_I) + R̃_b,     R̃_b ∈ ρ₀²ρ_I²Diff²_b(U; S²T*),                   {#eq:iii-c-4-2}

with S̄ the endomorphism of [[lem:iii-f-2-1]] (2), and R̃_b with coefficients in C^∞(U).

*Proof.* By [[eq:iii-f-2-2]]–[[eq:iii-f-2-3]], on {|x| > 3R₁},
2L_b = −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S̄) + 2L̄̂(0) − g_b^(00)∂²_(t_*) + Q_b∂_(t_*) + R_b, where 2L̄̂(0), the spectral
family of 2L̄ at σ = 0, is its stationary part, with 2L̄̂(0) ∈ ρ²Diff²_b, g_b^(00) ∈ ρ²C^∞(X̄), Q_b ∈ ρ³Diff¹_b,
R_b ∈ ρ⁴Diff²_b, all stationary b-operators on X̄: polynomials in ρ∂_ρ|_(t_*) and ∂_ω with coefficients in C^∞(X̄).
By [[eq:iii-c-1-4]]
these vector fields are b-vector fields on U (∂_ω at fixed t_*, ρ is ∂_ω at fixed ρ₀, ρ_I, as t_* and ρ do not depend on
ω), and ρ = ρ₀ρ_I, ∂_(t_*) = ρ₀(X₀ − X_I). So the last four terms lie in ρ₀²ρ_I²Diff²_b(U); for instance
g_b^(00)∂²_(t_*) ∈ ρ₀⁴ρ_I²Diff²_b. For the first, (X₀ − X_I)ρ = 0, so

    −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S̄)
        = −2ρ₀²ρ_I(X₀ − X_I)(X_I − 3/2 − S̄) − 2ρ₀²ρ_I(X₀ − X_I) 8m₀ρ₀²ρ_I(X₀ − X_I),

and the second term lies in ρ₀⁴ρ_I²Diff²_b. S̄ is homogeneous of degree 0, a function of ω in this frame, so it
commutes with X₀ − X_I. Halving gives [[eq:iii-c-4-2]]. ∎

The leading part can be checked on radial functions on Minkowski space without [[lem:iii-f-2-1]]. With □ = −tr ∇²,
u := x¹ and v := x⁰, a radial function f satisfies ½□f = ½(∂_t² − ∂²_(|x|) − 3|x|⁻¹∂_(|x|))f
= 2∂_u∂_v f + (3/2)|x|⁻¹(∂_u − ∂_v)f, since ∂_t = ∂_u + ∂_v and ∂_(|x|) = ∂_v − ∂_u. By [[eq:iii-c-1-5]], with
X_Iρ₀ = 0, X_Iρ_I = ρ_I and |x|⁻¹ = ρ₀ρ_I,

    2∂_v∂_u = −ρ₀²ρ_I X_I(X₀ − X_I) − ½ρ₀²ρ_I X_I ρ_I X_I,
    (3/2)|x|⁻¹∂_u = (3/2)ρ₀²ρ_I(X₀ − X_I) + ¾ρ₀²ρ_I² X_I,     (3/2)|x|⁻¹∂_v = −¾ρ₀²ρ_I² X_I,

so ½□ = −ρ₀²ρ_I(X_I − 3/2)(X₀ − X_I) modulo ρ₀²ρ_I²Diff²_b with polynomial coefficients (X_I and X₀ − X_I commute).
With |x|⁻¹ in place of (3/2)|x|⁻¹, as for the radial wave operator in dimension 3 + 1, the same lines give 1 in place of
3/2, which is [Hin26, (5.40)].

**Lemma {#lem:iii-c-4-2}** (The matrix Ā.) In the rescaled null frame (dt_* + 2d|x|, dt_*, |x|e^a) of ḡ, the image of
the products of (dt_*, dx^i) under a map F₀(ω), S̄ has a constant matrix Ā; in the frame [[eq:iii-c-1-6]] of η its
matrix is Ā modulo ρ₀²ρ_I²C^∞ ([[lem:iii-c-1-3]]). It is lower triangular, with diagonal

    2(1 − v_C)γ_C,  (1 − v_C)γ_C,  (1 − e_C)(1 − v_C)γ_C,  (1 − e_Υ)γ_Υ,  γ_Υ,  0,  2γ_Υ,                 {#eq:iii-c-4-3}

and off-diagonal entries exactly at (3, 1), (4, 1), (4, 3), (5, 2), (7, 3), (7, 4), with Ā₇₄ = 2(1 − e_Υ)γ_Υ and
Ā₇₆ = 0. Each summand of [[eq:iii-c-1-6]] is mapped to summands of its own type.

*Proof.* *The frame.* The model metric of [[sec:iii-f-2]] is ḡ = −(dt_* + d|x|)² + Σ_i(dx^i)², the Minkowski metric
with time t̄ := t_* + |x|. Its null coordinates are x̄⁰ := t̄ + |x| and x̄¹ := t̄ − |x| = t_*, so dx̄⁰ = dt_* + 2d|x|,
dx̄¹ = dt_*, and ḡ = −½(dx̄⁰ ⊗ dx̄¹ + dx̄¹ ⊗ dx̄⁰) + |x|²g̸. Let ∂̄₀, ∂̄₁ be the dual null vectors and take the slot
coordinates [[eq:iii-c-1-7]] in the frame (dx̄⁰, dx̄¹, |x|e^a). So ḡ(∂̄₀, ∂̄₁) = −½, ḡ⁻¹(dx̄⁰, dx̄¹) = −2 and
ḡ⁻¹(dx̄⁰, dx̄⁰) = ḡ⁻¹(dx̄¹, dx̄¹) = 0. For a 1-form α write α = α₀dx̄⁰ + α₁dx̄¹ + α_T with α₀ = α(∂̄₀), α₁ = α(∂̄₁) and
α_T tangential; then ⟨α, β⟩ := ḡ⁻¹(α, β) = −2(α₀β₁ + α₁β₀) + α_T·β_T, and tr h = −4h₀₁ + tr̸h for a symmetric
2-tensor h. For a symmetric product, (α ⊗_s β)(∂̄_i, ∂̄_j) = ½(α_iβ_j + α_jβ_i).

*The ingredients.* By [[eq:iii-f-2-2]], ρS̄ = −Ē^C ι_X Ḡ + (dt_* ⊗_s ·)Ē^Υ Ḡ with X := ḡ⁻¹dt_*. Here X = −2∂̄₀ and
ι_Xḡ = dx̄¹. By [[def:iii-b-6-1]] and [[eq:iii-b-6-5]], with v := v_C, c̄_C = ρĉ and
ĉ := ½(1 − v)dx̄⁰ + ½(1 + v)dx̄¹, which is dt̄ − v d|x| in these coordinates,

    Ē^Cω = γ_Cρ(2ĉ ⊗_s ω − ⅔(1 − e_C)ḡ⟨ĉ, ω⟩),     Ē^ΥḠh = −γ_Υρ(2ι_Y h − e_Υ(tr h) dt̄),

with dt̄ = ½(dx̄⁰ + dx̄¹) and Y := ḡ⁻¹dt̄ = −∂̄₀ − ∂̄₁. Hence

    S̄h = −γ_C(2ĉ ⊗_s ω − ⅔(1 − e_C)ḡ⟨ĉ, ω⟩) − γ_Υ dx̄¹ ⊗_s β,
    ω := ι_XḠh = −2h(∂̄₀, ·) − ½(tr h)dx̄¹,     β := 2ι_Y h − e_Υ(tr h) dt̄.                             {#eq:s17-sbar}

In components, with h(∂̄₀, ·) = h₀₀dx̄⁰ + h₀₁dx̄¹ + h_(0ā),

    ω₀ = −2h₀₀,     ω₁ = −2h₀₁ − ½(−4h₀₁ + tr̸h) = −½tr̸h,     ω_T = −2h_(0ā),
    β₀ = −2(h₀₀ + h₀₁) − ½e_Υ tr h,     β₁ = −2(h₀₁ + h₁₁) − ½e_Υ tr h,     β_T = −2(h_(0ā) + h_(1ā)).

*The slots.* Put a := ½(1 − v), b := ½(1 + v) and s₃ := ⅓tr̸h, so ⟨ĉ, ω⟩ = −2(aω₁ + bω₀) and
aω₁ + bω₀ = −(3a/2)s₃ − 2b h₀₀. The tensor 2ĉ ⊗_s ω has no tangential block, and dx̄¹ ⊗_s β has components only at
(∂̄₀, ∂̄₁), (∂̄₁, ∂̄₁) and (∂̄₁, tangential), equal to ½β₀, β₁ and ½β_T. Reading off the slot coordinates of S̄h:

- slot 1: S̄h(∂̄₀, ∂̄₀) = −2aγ_Cω₀ = 2(1 − v)γ_C h₀₀;
- slot 2: the tangential part of S̄h(∂̄₀, ·) is −aγ_Cω_T = (1 − v)γ_C h_(0ā);
- slots 3 and 6: the tangential block is ⅔(1 − e_C)γ_C⟨ĉ, ω⟩|x|²g̸, a multiple of g̸, so slot 6 of S̄h vanishes and
  slot 3 is −(4/3)(1 − e_C)γ_C(aω₁ + bω₀) = (1 − e_C)(1 − v)γ_C s₃ + (4/3)(1 − e_C)(1 + v)γ_C h₀₀;
- slot 4: S̄h(∂̄₀, ∂̄₁) = −γ_C(aω₁ + bω₀)(1 − ⅔(1 − e_C)) − ½γ_Υβ₀, which with tr h = −4h₀₁ + 3s₃ is
  ((1 + 2e_C)(1 + v)γ_C/3 + γ_Υ)h₀₀ + ¼((1 + 2e_C)(1 − v)γ_C + 3e_Υγ_Υ)s₃ + (1 − e_Υ)γ_Υ h₀₁;
- slot 5: the tangential part of S̄h(∂̄₁, ·) is −bγ_Cω_T − ½γ_Υβ_T = ((1 + v)γ_C + γ_Υ)h_(0ā) + γ_Υ h_(1ā);
- slot 7: S̄h(∂̄₁, ∂̄₁) = −2bγ_Cω₁ − γ_Υβ₁ = (3/2)((1 + v)γ_C + e_Υγ_Υ)s₃ + 2(1 − e_Υ)γ_Υ h₀₁ + 2γ_Υ h₁₁.

The coefficients are constants, so the matrix Ā of S̄ in this frame is constant. Slot j of S̄h involves only slots
i ≤ j of h, so Ā is lower triangular; its diagonal is [[eq:iii-c-4-3]], and its off-diagonal entries are the nonzero
coefficients above, at (3, 1), (4, 1), (4, 3), (5, 2), (7, 3) and (7, 4), with Ā₇₄ = 2(1 − e_Υ)γ_Υ. The slot π̸₀h
enters no slot of S̄h, so Ā₇₆ = 0. The scalar slots 1, 3, 4, 7 are mapped into scalar slots, the vector slots 2, 5 into
vector slots, and slot 6 to 0. The diagonal is [[eq:iii-f-3-1]] with its multiplicities, as the triangular form
requires. The frame (dx̄⁰, dx̄¹, |x|e^a) is the image of the products of (dt_*, dx^i) under the map that fixes dt_* and
sends dx^i to its tangential part plus ω^i(dx̄⁰ − dx̄¹)/2, which depends on ω alone; and it differs from the frame of η
by I + ρ²C^∞ ([[lem:iii-c-1-3]]). ∎

Independently of the calculation: S̄ commutes with the rotations of ℝ⁴, which preserve ḡ, t_*, c_C and c_Υ near
infinity ([[def:iii-b-6-1]]), and [[eq:iii-c-1-6]] is rotation-equivariant. The stabiliser SO(3) of ω acts on the rank-1
summands trivially, on the two rank-3 summands by its standard representation, and on |x|²ker tr̸ by the irreducible
5-dimensional one. By Schur's lemma S̄ maps each summand to the summands of the same type by scalars, and these do not
depend on ω, as SO(4) acts transitively on 𝕊³.

The trace couplings (3, 1), (4, 1), (4, 3), (7, 3) differ from the values of [Hin26, (5.28)] in dimension 3 + 1
([[prop:np-10-38]] (1)); only the support of Ā enters below.

**Lemma {#lem:iii-c-4-3}** (Counting coefficients.) Let g, g′, g₀, g₀′ be Lorentzian metrics on U whose Cartesian
components are bounded with bounded inverses. In the Cartesian frame, L^(g,g₀) − L^(g′,g₀′) is a second-order operator
Σ a^(μν)∂_μ∂_ν + Σ b^μ∂_μ + c whose coefficients are sums of products of: polynomials in the components of g, g′, g₀,
g₀′ and their inverses; at most two factors from {∂g, ∂g′, ∂g₀, ∂g₀′, c_C, c_Υ, c_(Υ,H)}, or one second derivative of
one of the metrics or one derivative of a c; and at least one factor δ from {g − g′, g₀ − g₀′} or a Cartesian
derivative of it of order at most 2. Second-order coefficients contain no derivative; first-order ones at most one
derivative of order one or one c; and the δ factor counts towards these limits.

*Proof.* Each term of [[eq:iii-c-4-1]] is, in Cartesian coordinates, of the stated form for a single pair (g, g₀): □_g
has principal part −g^(μν)∂_μ∂_ν, first-order part with one Christoffel symbol and zeroth-order part with one derivative
of a Christoffel symbol or two of them; E^C_(g₀) and E^Υ_(g₀) contain one c and no derivative ([[eq:iii-b-6-1]],
[[eq:iii-b-6-2]]); δ_g, δ^*_g, δ^*_(g₀) are first order with one Christoffel symbol in the zeroth-order part; C_(g,g₀)
and Y_(g,g₀) are zeroth order with one first derivative of g or g₀ ([[lem:iii-b-6-3]]); R_g is zeroth order with one
second derivative or two first derivatives. Each coefficient of [[eq:iii-c-4-1]] is a polynomial in g, g⁻¹, g₀, g₀⁻¹,
their derivatives and the c's. The difference of a polynomial expression at two arguments is a sum of terms each with
one difference factor, by ab − a′b′ = (a − a′)b + a′(b − b′) and g⁻¹ − g′⁻¹ = −g⁻¹(g − g′)g′⁻¹. ∎

**Proposition {#prop:iii-c-4-4}** ([Hin26, Proposition 5.11 and (5.41a)] in dimension 4 + 1.) Let k ≥ 5, ℰ₀ as in
[[def:iii-c-3-1]] (1), ℓ₀ > 0, ℓ_I > 0, and let ℱ be an index set with min Re ℱ > 0 and 2ℱ ⊂ ℱ. Let g₁, g₀ ∈ 𝒢 and
h ∈ H^(k,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b(U; S²T*) (every component), with ‖h‖_(H^(k,a₀,a_I)_b) < ε₀ for some a₀, a_I > 0 with
h ∈ H^(k,a₀,a_I)_b, ε₀ > 0 small depending on k, a₀, a_I and on g₁. Then g := g₁ + h satisfies, on U, in the splitting
[[eq:iii-c-1-6]],

    L^(g,g₀) ≡ −ρ₀²ρ_I(X_I − 3/2 − Ā)(X₀ − X_I)
               mod (ρ₀²ρ_I²C^∞ + H^(k−2,(ℰ₀+2,ℓ₀+2),(ℱ,ℓ_I))_b) Diff²_b(U; S²T*).                       {#eq:iii-c-4-4}

In particular this holds with ℱ = ℰ_I^tot for h ∈ H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b ([[lem:iii-c-3-2]] (b)–(c)), and with
ℱ = (2, 0) for h ∈ H^(k,(ℰ₀,ℓ₀),⟨(3,0)⟩₀,ℓ_I)_b.

*Proof.* *The background.* By [[lem:iii-c-4-1]] and [[lem:iii-c-1-3]], conjugate by the frame change
F = F₀(ω)(I + E), E ∈ ρ₀²ρ_I²C^∞. F₀ commutes with X₀ and X_I, so F₀⁻¹L_bF₀ has a leading part with F₀⁻¹S̄F₀ = Ā
([[lem:iii-c-4-2]]); and (I + E)⁻¹P(I + E) − P = (I + E)⁻¹[P, E], which for P ∈ ρ₀²ρ_I Diff²_b lies in
ρ₀⁴ρ_I³Diff¹_b, as 𝒱_b preserves ρ₀²ρ_I²C^∞. So [[eq:iii-c-4-4]] holds for (g, g₀) = (g_b, g_b) with remainder in
ρ₀²ρ_I²C^∞Diff²_b.

*Counting.* Apply [[lem:iii-c-4-3]] to the difference of L^(g,g₀) and L_b, with the conversion to b-operators: every
Cartesian derivative lies in ρ₀𝒱_b(U) ([[lem:iii-c-1-1]]); c_C, c_Υ ∈ |x|⁻¹C^∞ = ρ₀ρ_I C^∞ on U ([[def:iii-b-6-1]]),
and c_(Υ,H) is supported in {|x| < 5R₁}, a compact subset of U away from I₀ ∪ ℐ⁺; the Cartesian components of g_b, g₁,
g₀ and their inverses are smooth on U, and their Cartesian derivatives lie in ρ₀C^∞. A term with second-order
derivatives is a∂_μ∂_ν ∈ aρ₀²Diff²_b; a first-order term has its b^μ containing one first derivative or one c, both in
ρ₀(·), times ∂_μ ∈ ρ₀𝒱_b; a zeroth-order term contains two such factors or one second derivative. So each term is ρ₀²
times a product of the δ factor, or of 𝒱_b-derivatives of it of order at most 2, with smooth bounded functions and with
other δ factors, applied through Diff²_b.

*The backgrounds.* For (g₁, g₀) against (g_b, g_b): δ ∈ {g₁ − g_b, g₀ − g_b} ⊂ ρ₀²ρ_I²C^∞ ([[def:iii-c-3-4]],
[[lem:iii-c-3-5]] (1)), which 𝒱_b preserves; the terms lie in
ρ₀⁴ρ_I²C^∞Diff²_b ⊂ ρ₀²ρ_I²C^∞Diff²_b.

*The perturbation.* For (g₁ + h, g₀) against (g₁, g₀): δ = h, and
(g₁ + h)⁻¹ − g₁⁻¹ = Σ_(j≥1)(−1)^j g₁⁻¹(hg₁⁻¹)^j. By [[lem:iii-c-2-1]] with γ = (ℓ₀, ℓ_I) (the strict inequalities
hold, as min Re ℰ₀, min Re ℱ, ℓ₀, ℓ_I > 0), the j-th term lies in
H^(k,(jℰ₀,ℓ₀),(jℱ,ℓ_I))_b ⊂ H^(k,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b. For j so large that ja₀ ≥ ℓ₀ and ja_I ≥ ℓ_I, it lies in
H^(k,ℓ₀,ℓ_I)_b with norm at most C(Cε₀)^j (part (i) of the proof of [[lem:iii-c-2-1]]); so the series converges for
Cε₀ < 1. Every coefficient of the difference is then ρ₀² times an element of H^(k−2,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b
([[lem:iii-c-2-1]] with k − 2 > 5/2, and (F1)); that is, an element of H^(k−2,(ℰ₀+2,ℓ₀+2),(ℱ,ℓ_I))_b. The frame change
F preserves both classes. ∎

The form [Hin26, (5.26a)] of this statement in dimension 4 + 1 is
L^(g,g₀) ≡ (2|x|^(−3/2)∂₀|x|^(3/2) + |x|⁻¹Ā)∂₁ modulo the same class, by [[eq:iii-c-1-5]]:
2∂₀∂₁ + (3/2)|x|⁻¹∂₁ ≡ −ρ₀²ρ_I(X_I − 3/2)(X₀ − X_I) and |x|⁻¹Ā∂₁ ≡ ρ₀²ρ_IĀ(X₀ − X_I).

**Remark {#rem:iii-c-4-5}** (The terms A^h, B^h of [Hin26], and [Hin26, Lemmas 5.6–5.8] in dimension 4 + 1.) [Hin26]
keeps A^h − A₀ ∈ C^∞ + H^(k−1,(ℰ₀,ℓ₀),(ℰ_I^tot−1,ℓ_I−1))_b and B^h in the leading part because in dimension 3 + 1,
min Re(ℰ_I^tot − 1) = 0: they are of the same order as A₀. In dimension 4 + 1 the same classes have min Re = ½, and
[[prop:iii-c-4-4]] places them in the error, in the form ρ₀²ρ_I · ρ_I^(ℰ_I^tot−1) = ρ₀²ρ_I^(ℰ_I^tot). [Hin26, Lemmas
5.6–5.8 and Corollaries 5.9–5.10] calculate the entries of A^h, B^h and the edge-b form; in dimension 4 + 1 the b-form
needs only the memberships used in the proof above, which are their counterparts:
g⁻¹ − g₁⁻¹ ≡ −g₁⁻¹hg₁⁻¹ modulo H^(k,(2ℰ₀,ℓ₀),(2ℱ,ℓ_I))_b ([Hin26, (5.11)]); the Cartesian Christoffel symbols satisfy
Γ(g) − Γ(g₁) ∈ ρ₀H^(k−1,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b ([Hin26, (5.12)]); and
Riem(g) − Riem(g₁) ∈ ρ₀²H^(k−2,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b ([Hin26, Lemma 5.8]). The edge-b form (5.26b) is in [[ch:s26]]. Taking
ℱ = ℰ_I^tot for every component discards the component structure (for instance the ∂₁² coefficient g^(11) is tied to
h₀₀, of index ℰ_I^C); the b-form does not need it, but (5.26b) and the energy estimates of [[ch:s26]] do. At the level
of tensors the drop by half an order is the counting of [[lem:iii-c-4-3]]. For comparison, item (7) of
[[prop:np-10-64]] gives four of the h-dependent entries (A(7, 1), B(7, 1), A(4, 7), B(4, 1)) of the closely related
operator of [Hin23a] in dimensions 3 + 1 and 4 + 1, and those of dimension 4 + 1 are r^(−1/2) times those of dimension
3 + 1; that operator omits the γ_Υ term, which carries one c and obeys the same counting.

### Forward mapping {#sec:iii-c-5}

This section is [Hin26, Definition 5.13, Proposition 5.14, Corollary 5.15] in dimension 4 + 1.

**Definition {#def:iii-c-5-1}** ([Hin26, Definition 5.13] in dimension 4 + 1.) Let ℰ₀, ℰ_I^C be as in
[[def:iii-c-3-1]], k ≥ 3, ℓ₀ > 0, ℓ_I > 3/2.

(1) Set

    ℱ_(I,11) := 1 + (ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0)).                                                {#eq:iii-c-5-1}

H^(k,(ℰ₀+2,ℓ₀+2),⟨ℰ_I^C+1⟩′,ℓ_I+1)_b(Ω_ext) is the space of real symmetric 2-tensors f with, on U,
π_C f, π₀₁f, π_(1/)f, π̸₀f ∈ H^(k,(ℰ₀+2,ℓ₀+2),(ℰ_I^C+1,ℓ_I+1))_b and π₁₁f ∈ H^(k,(ℰ₀+2,ℓ₀+2),(ℱ_(I,11),ℓ_I+1))_b.

(2) If ℓ₀ < min Re ℰ₀ we write ℓ₀ + 2 for (ℰ₀ + 2, ℓ₀ + 2), and if ℓ_I < min Re ℰ_I^C we write (−′, ℓ_I + 1) for
(⟨ℰ_I^C + 1⟩′, ℓ_I + 1).

(3) H^(k,(ℰ₀+2,ℓ₀+2),⟨(4,0)⟩′,ℓ_I+1)_b(Ω_ext) is the space of f with π_C f, π₀₁f, π_(1/)f, π̸₀f in ((4, 0), ℓ_I + 1)
and π₁₁f in ((3, 0), ℓ_I + 1) at ℐ⁺, and in (ℰ₀ + 2, ℓ₀ + 2) at I₀.

The set ℱ_(I,11) of [Hin26, (5.43)] also contains 1 + (1, 0), from the radiation field of π̸₀ through the h-dependent
(7, 6) entry of A^h. In dimension 4 + 1 that entry is part of the error of [[eq:iii-c-4-4]], and what it produces lies
in ℰ_I^C + 1 ([[rem:s17-no-radiation]]).

**Proposition {#prop:iii-c-5-2}** ([Hin26, Proposition 5.14] in dimension 4 + 1.) Let g = g₁ + h, g₁, g₀ ∈ 𝒢, with
h ∈ H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_ext) small as in [[prop:iii-c-4-4]], k ≥ 5. Then

    L^(g,g₀) : H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_ext) → H^(k−2,(ℰ₀+2,ℓ₀+2),⟨ℰ_I^C+1⟩′,ℓ_I+1)_b(Ω_ext)         {#eq:iii-c-5-2}

continuously. If h ∈ H^(k,(ℰ₀,ℓ₀),⟨(3,0)⟩₀,ℓ_I)_b (small), then

    L^(g,g₀) : H^(k,(ℰ₀,ℓ₀),⟨(3,0)⟩₀,ℓ_I)_b(Ω_ext) → H^(k−2,(ℰ₀+2,ℓ₀+2),⟨(4,0)⟩′,ℓ_I+1)_b(Ω_ext).         {#eq:iii-c-5-3}

*Proof.* Away from U the spaces impose nothing beyond H^k and H^(k−2), and L^(g,g₀) is a second-order operator with
coefficients in H^(k−2); by property (F2) of [[sec:iii-a-1]] it suffices to work on U. Let ġ be in the domain of
[[eq:iii-c-5-2]]. Every slot of ġ lies in H^(k,(ℰ₀,ℓ₀),(ℰ_I^tot,ℓ_I))_b ([[lem:iii-c-3-2]] (c)). Split L^(g,g₀) by
[[eq:iii-c-4-4]] with ℱ = ℰ_I^tot.

*The C^∞ error.* ρ₀²ρ_I²C^∞Diff²_b maps ġ into H^(k−2,(ℰ₀+2,ℓ₀+2),(ℰ_I^tot+2,ℓ_I+2))_b in every slot, and
ℰ_I^tot + 2 ⊂ ℰ_I^C + 1 ⊂ ℱ_(I,11) ([[lem:iii-c-3-2]] (c)).

*The perturbation.* H^(k−2,(ℰ₀+2,ℓ₀+2),(ℰ_I^tot,ℓ_I))_b Diff²_b maps ġ, by [[lem:iii-c-2-1]] and (F1), into
H^(k−2,(2ℰ₀+2,γ₀),(2ℰ_I^tot,γ_I))_b with γ₀ = ℓ₀ + 2 and γ_I = ℓ_I + 1. The strict inequalities of [[lem:iii-c-2-1]]
hold: ℓ₀ + 2 < ℓ₀ + 2 + min Re ℰ₀; ℓ_I + 1 < ℓ_I + 3/2 = ℓ_I + min Re ℰ_I^tot; and ℓ_I + 1 < 2ℓ_I as ℓ_I > 3/2.
And 2ℰ₀ + 2 ⊂ ℰ₀ + 2, 2ℰ_I^tot ⊂ ℰ_I^C + 1 ([[lem:iii-c-3-2]] (b)).

*The leading part.* u := (X₀ − X_I)ġ has the slot index sets of ġ (F1). Then w := (X_I − 3/2 − Ā)u has, in slot j,
(X_I − 3/2 − Ā_(jj))u_j − Σ_(i<j) Ā_(ji)u_i. In a slot with index set ℰ_I^C ∪ (3/2 + s, 0) and Ā_(jj) = s, the term
ρ_I^(3/2+s)a(ρ₀, ω) is annihilated: X_I − 3/2 − s kills it, and the terms ρ_I^(3/2+s+j), j ≥ 1, lie in ℰ_I^C
([[lem:iii-c-3-2]] (d)). This holds in slot 4 (s = (1 − e_Υ)γ_Υ), slot 5 (s = γ_Υ) and slot 6 (s = 0), and for the
term 3/2 + 2γ_Υ of slot 7. By [[lem:iii-c-4-2]] the couplings are (3, 1), (4, 1), (4, 3), (5, 2) and (7, 3), from
π_C slots with index set ℰ_I^C, and (7, 4), which brings ℰ_(I,01) into slot 7. So w_j ∈ (ℰ_I^C, ℓ_I) at ℐ⁺ for
j ≤ 6, and w₇ ∈ (ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0), ℓ_I): the term 3/2 + (1 − e_Υ)γ_Υ of slot 7 itself is not
annihilated, nor is that of slot 4 brought by (7, 4). Multiplying by −ρ₀²ρ_I gives ℰ_I^C + 1, resp. ℱ_(I,11), at
weight ℓ_I + 1, and ℰ₀ + 2 at weight ℓ₀ + 2 at I₀. Regularity: H^(k−2).

[[eq:iii-c-5-3]]: the slots of ġ have index sets (3, 0) (slots 1–6) and (2, 0) (slot 7). The leading part does not
annihilate ρ_I² in slot 7 (2 ≠ 3/2 + 2γ_Υ) and gives (2, 0) there, (3, 0) elsewhere; the couplings into slot 7 come
from slots with (3, 0); after the factor ρ_I this is (3, 0) in slot 7 and (4, 0) in the others. The error gives
(2, 0) + 2 = (4, 0), and the perturbation, with ℱ = (2, 0), gives (2, 0) + (2, 0) = (4, 0). Continuity follows from
that of the products in [[lem:iii-c-2-1]]. ∎

**Corollary {#cor:iii-c-5-3}** ([Hin26, Corollary 5.15] in dimension 4 + 1.) Let g₀ ∈ 𝒢 with Ric(g₀) = 0, and
h ∈ H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_ext) small as in [[prop:iii-c-4-4]], k ≥ 5. Then

    P(g₀ + h, g₀) ∈ H^(k−2,(ℰ₀+2,ℓ₀+2),⟨ℰ_I^C+1⟩′,ℓ_I+1)_b(Ω_ext),                                      {#eq:iii-c-5-4}

and for h ∈ H^(k,(ℰ₀,ℓ₀),⟨(3,0)⟩₀,ℓ_I)_b small, P(g₀ + h, g₀) ∈ H^(k−2,(ℰ₀+2,ℓ₀+2),⟨(4,0)⟩′,ℓ_I+1)_b.

*Proof.* P(g₀, g₀) = Ric(g₀) − δ^*_(g₀,E_C)Υ^(E_Υ)(g₀, g₀) = 0, since Υ⁰(g₀, g₀) = 0 and
E^Υ_(g₀)G_(g₀)(g₀ − g₀) = 0 ([[eq:iii-b-6-3]]–[[eq:iii-b-6-4]]). So

    P(g₀ + h, g₀) = ∫₀¹ L^(g₀+sh,g₀) h ds,                                                              {#eq:iii-c-5-5}

and [[prop:iii-c-5-2]] with g₁ = g₀ and the perturbation sh applies for each s ∈ [0, 1], with bounds uniform in s. The
integrand is continuous in s with values in the target space (the coefficients are polynomial in s and in the Neumann
series of (g₀ + sh)⁻¹), so the integral converges there. ∎

[Hin26] states Corollary 5.15 with g = g_b + h and writes P(g_b + h, g₀) through h̃ = h − (g₀ − g_b) ([Hin26, (5.48)]).
When g₀ ≠ g_b, L(g₀ − g_b) has I₀-index set (2, 0) + 2 in dimension 4 + 1, which lies in ℰ₀ + 2 only if
(2, 0) ⊂ ℰ₀. The statement is used with the perturbation measured from g₀ ([Hin26, (5.77a)]), which is the form above;
measured from g_b with g₀ ≠ g_b the conclusion needs (2, 0) ⊂ ℰ₀ in dimension 4 + 1 ((1, 0) in dimension 3 + 1).

**Remark {#rem:s17-no-radiation}** (The 11-component carries no radiation field.) In [Hin26] the sets ℰ_(I,11) and
ℱ_(I,11) contain (1, 0), from the coupling of the radiation field of π̸₀h into the 11-component by the h-dependent
(7, 6) entry of A^h ([Hin26, p. 98], and [Hin26, p. 169]: "this coupling is absent when h = 0"), and from the mass
term. In dimension 4 + 1, Ā₇₆ = 0 ([[lem:iii-c-4-2]]), the h-dependent coupling is part of the error of
[[eq:iii-c-4-4]] and lands at 3/2 + ½ = 2 ∈ ℰ_I^C ([[lem:iii-c-3-2]] (a)), and the mass term m|x|⁻²(dx¹)² has index
(2, 0) ([[lem:iii-c-3-5]]). So in the exterior region the radiation field of π̸₀h reaches the 11-component of the
operator only at the order 2, in ℰ_I^C. At ι⁺ this matches [[def:iii-g1-1-2]], where the index set at ι⁺ ∩ ℐ⁺ that
[Hin26] calls ℰ_(ι⁺,ℐ,11) is the union of those for 2γ_Υ and (1 − e_Υ)γ_Υ.

[Hin26] uses the Sobolev algebra property of H^(k−2)_b, k − 2 > ½ dim Ω_ext, without proof ([Hin26, Section 5, remark
(vii)]), and with it the products of partially polyhomogeneous functions; [[lem:iii-c-2-1]] proves the form used, with
its strict inequalities on the weights, and every use above has room to spare.

### The setting at ι⁺ {#sec:iii-g3-1}

The next three sections extend the inverse of the ι⁺-normal operator of [[thm:iii-g1-3-1]] to sources with partial
expansions at ι⁺ ∩ ℐ⁺. Against [Hin26, Section 9.1.3], dimension 4 + 1 changes five things. (a) The condition
1 < ℓ_I < 1 + (1 − e_C)(1 − v_C)γ_C of [Hin26, (9.44)] becomes 3/2 < ℓ_I < 3/2 + s_C, with
s_C := γ_C(1 − e_C)(1 − v_C) (and ℓ_I off the real parts of ℰ_I^tot). (b) The sources of [Hin26] carry two
exceptional exponents in their (dx¹)²-component, at 1 + 1 and 1 + 1 + (1 − e_Υ)γ_Υ. In dimension 4 + 1 they carry one,
at 1 + λ_♯, with

    λ_♯ := 3/2 + (1 − e_Υ)γ_Υ,                                                                           {#eq:iii-g3-0-1}

since π₁₁h carries no radiation field ([[rem:s17-no-radiation]]). So the incoming pole that [Hin26] has at λ = 1 has no
counterpart, and the least pole is λ_♯ ([[cor:iii-g3-2-6]]). (c) The pure ι⁺ resonances have real part at least 2
([[lem:iii-g1-4-2]] (a)), where those of [Hin26] exceed 1. (d) [[thm:iii-g1-3-1]] (2) loses d derivatives with d
depending on Re λ, so the statements at finite regularity hold on strips. (e) The expansion at K⁺ is that of
[[thm:iii-g2-3-1]], below ℓ_K^max = min(3, 2 + 2γ_C v_C). The harmonic degrees there are at most 4 (5 in [Hin26]).

We use the setting of [[sec:iii-g1-1]]: ι⁺ = [0, ∞]_v × 𝕊³ with the faces {v = 0} = ℐ⁺ ∩ ι⁺ and
{R = 0} = K⁺ ∩ ι⁺, R = v⁻¹; the defining functions ρ_I = v/(1 + v), ρ_K = R/(1 + R); the operator

    N_(ι⁺)(λ) = −2v(v∂_v − λ)(v∂_v − 3/2 − S̄) + v²L̃(0)(ω, v∂_v, ∂_ω),
    2L̄(t_*^(−λ)w) = t_*^(−λ−2)N_(ι⁺)(λ)w                                                                {#eq:iii-g3-1-1}

([[eq:iii-g1-1-1]]; [[lem:iii-g-1-2]] (c)); the index set ℰ_K at K⁺ ∩ ι⁺ ([[def:iii-g1-1-2]] (3), [[lem:iii-g1-1-3]]);
the sets ℰ^tot_(ι⁺,ℐ), ℰ^C_(ι⁺,ℐ) and ℰ_s, s ∈ σ_Υ, of [[eq:iii-g1-1-5]]; and spec_(ι⁺)(L̄), Spec_(ι⁺)(L̄)
([[def:iii-g1-4-1]]). From [[ch:s16]] we use further ℓ_K^max, the roots 𝒲(ℓ_K), the formal solutions of
[[lem:iii-g2-2-4]] and [[thm:iii-g2-3-1]] with their conventions for the types s1 and v1, and [[cor:iii-g2-3-2]]. The
parameters are those of [[thm:iii-g1-3-1]], with γ_Υ < min(½s_C, ¼) (this is [[eq:iii-c-1-1]] together with the
condition of [[lem:iii-g1-1-1]]). Let ℰ_I^C be an index set as in [[def:iii-c-3-1]], with its sets [[eq:iii-c-3-2]] and
ℱ_(I,11) of [[eq:iii-c-5-1]]. Fix

    3/2 < ℓ_I < 3/2 + s_C,     ℓ_I ∉ Re π₁ℰ_I^tot,                                                       {#eq:iii-g3-1-2}

the form of [Hin26, (9.44)] in dimension 4 + 1; it includes ℓ_I ∉ Re π₁ℰ^tot_(ι⁺,ℐ), as ℰ^tot_(ι⁺,ℐ) ⊂ ℰ_I^tot. And
ℓ_K ∈ (−1, ℓ_K^max), with ℓ_K ∉ Re π₁ℰ_K and ℓ_K ≠ −Re μ for every root μ of [[prop:iii-f1-2-3]].

*Slots on ι⁺.* Near v = 0, ι⁺ lies in {|x| ≥ 3R₁}, where the rescaled null frame of [[eq:iii-c-1-6]] is a smooth frame
of S²T*. Its slots, with the slot coordinates [[eq:iii-c-1-7]] and the projections π_C, π₀₁, π_(1/), π̸₀, π₁₁ of
[[def:iii-c-1-2]], are used on ι⁺ near v = 0. The null frames of η, g_m and ḡ agree on ι⁺: [[lem:iii-c-1-3]] is stated
on the region U, which ι⁺ does not meet, but its proof uses only |x| ≥ 4R₁ and shows that the frames differ by
F₀(ω)(I + E) with E ∈ |x|⁻²C^∞; near ι⁺ ∩ ℐ⁺, |x|⁻¹ = v/t_* vanishes at ι⁺. So the frames restrict to ι⁺ identically,
and there S̄ has the constant matrix Ā of [[lem:iii-c-4-2]] (constant in the frame of ḡ). Let e₇ be the basis section
of ⟨(dx¹)²⟩.

**Definition {#def:iii-g3-1-1}** ([Hin26, (9.45)] in dimension 4 + 1.) H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺; S²T*) is
the space of h with h ∈ H^(k,(ℰ_K,ℓ_K))_b near R = 0 and, near v = 0, π_C h ∈ (ℰ_I^C, ℓ_I), π₀₁h ∈ (ℰ_(I,01), ℓ_I),
π_(1/)h ∈ (ℰ_(I,1/), ℓ_I), π̸₀h ∈ (ℰ̸_(I,0), ℓ_I), π₁₁h ∈ (ℰ_(I,11), ℓ_I), each with regularity k.
H^(k,(⟨ℰ_I^C+1⟩′,ℓ_I+1),ℓ_K−2)_b(ι⁺; S²T*) is the space of f with f ∈ H^(k,ℓ_K−2)_b near R = 0 and, near v = 0,
π_C f, π₀₁f, π_(1/)f, π̸₀f ∈ (ℰ_I^C + 1, ℓ_I + 1) and π₁₁f ∈ (ℱ_(I,11), ℓ_I + 1). The same names without the second
order denote the spaces on [0, 1)_v × 𝕊³ defined by the conditions at v = 0.

**Lemma {#lem:iii-g3-1-2}** (The spaces of [[ch:s16]] lie in these.) (1) The eigenvectors of Ā for 2γ_Υ, γ_Υ, 0 and
(1 − e_Υ)γ_Υ are supported in the slots {7}, {5}, {6} and {4, 7}, and those for the elements of σ_C have no component
in slot 6. (2) The space H^(k,(⟨ℰ^C_(ι⁺,ℐ)⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺) of [[def:iii-g1-1-2]] is contained in
H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺).

*Proof.* (1) Ā is lower triangular ([[lem:iii-c-4-2]]), so an eigenvector for a diagonal entry a_(jj) distinct from
every other diagonal entry (all seven are distinct, as 2γ_Υ < s_C) has x_i = 0 for i < j, x_j = 1, and x_i for i > j
determined by (a_(ii) − a_(jj))x_i = −Σ_(j≤m<i) a_(im)x_m. By the support of Ā in [[lem:iii-c-4-2]], rows 5 and 6 have no
entry in column 4, rows 6 and 7 none in column 5, row 7 none in column 6, and a₇₄ ≠ 0; this gives the supports. For
c ∈ σ_C, slot 6 gives (0 − c)x₆ = 0 (row 6 has only its diagonal entry, which is 0).

(2) ℰ^C_(ι⁺,ℐ) = ℰ^tot_(ι⁺,ℐ) + 1 ⊂ ℰ_I^tot + 1 ⊂ ℰ_I^C ([[lem:iii-c-3-2]] (a)). By (1), slot 4 of h is the slot-4 part
of Π_((1−e_Υ)γ_Υ)h and of Π_C h, in ℰ_((1−e_Υ)γ_Υ) ∪ ℰ^C_(ι⁺,ℐ) ⊂ ℰ_(I,01). In the same way slot 5 lies in
ℰ_(γ_Υ) ∪ ℰ^C_(ι⁺,ℐ) ⊂ ℰ_(I,1/), slot 6 in the set ℰ_s of [[eq:iii-g1-1-5]] with s = 0, which lies in ℰ̸_(I,0), slot 7
in ℰ_(2γ_Υ) ∪ ℰ_((1−e_Υ)γ_Υ) ∪ ℰ^C_(ι⁺,ℐ) ⊂ ℰ_(I,11), and slots 1–3, which only Π_C reaches, in
ℰ^C_(ι⁺,ℐ) ⊂ ℰ_I^C. ∎

### Partially polyhomogeneous inputs {#sec:iii-g3-2}

This section is [Hin26, Lemmas 9.13–9.14, Proposition 9.15, Definition 9.16, Remark 9.17] in dimension 4 + 1.

**Lemma {#lem:iii-g3-2-1}** ([Hin26, Lemma 9.13]; no dimension enters.) Let ℰ ⊂ ℂ × ℕ₀ be an index set, α ∈ ℝ, and
(R(λ)f)(x) := x^λ ∫₀^x t^(−λ)f(t) dt/t for f ∈ Ċ^∞([0, 1]), a right inverse of x∂_x − λ. Then R(λ) extends from
Re λ < min(α, min Re ℰ) to a finite-meromorphic family R(λ) : H̄^(k,(ℰ,α))_b([0, 1)) → H̄^(k+1,(ℰ,α))_b([0, 1)) on
{Re λ < α}, with divisor {(z, k(ℰ, z)) : z ∈ π₁ℰ, Re z < α}. The same holds with values in a Hilbert space ℋ (for
instance H^m(𝕊³)), except that the residues are then not of finite rank.

*Proof.* (i) ℰ = ∅. With s := t/x, x^(−α)R(λ)f(x) = ∫₀¹ s^(α−λ)(xs)^(−α)f(xs) ds/s, a multiplicative convolution of
t^(−α)f with s^(α−λ)1_((0,1))(s), whose L¹(ds/s)-norm is (α − Re λ)⁻¹. By Young's inequality on the group
((0, ∞), ·), ‖R(λ)f‖_(x^αL²(dx/x)) ≤ (α − Re λ)⁻¹‖f‖_(x^αL²(dx/x)), with f extended by 0 to (1, ∞) and R(λ)f
restricted to (0, 1). From x∂_xR(λ)f = λR(λ)f + f, by induction (x∂_x)^jR(λ)f is bounded in x^αL² by ‖f‖_(H̄^(j−1,α)_b)
for j ≤ k + 1. The family is holomorphic in λ, and Ċ^∞ is dense.

(ii) General ℰ. Write f = χ Σ x^z(log x)^j f_((z,j)) + f′ ([Hin26, Definition 2.8]), f′ ∈ H̄^(k,α)_b, and treat f′ by
(i). For Re λ < Re z, R(λ)x^z = (z − λ)⁻¹x^z, and differentiating in z, R(λ)(x^z(log x)^j) = ∂_z^j((z − λ)⁻¹x^z)
([Hin26, (9.46)]). This is meromorphic in λ ∈ ℂ, with a pole of order j + 1 at λ = z, and lies in
H̄^(∞,((z,j),α))_b. And R(λ)((1 − χ)x^z(log x)^j) vanishes near x = 0 and is entire in λ. The residue at λ = z depends
only on the coefficients f_((z,i)), so it has finite rank in the scalar case. ∎

**Lemma {#lem:iii-g3-2-2}** ([Hin26, Lemma 9.14] in dimension 4 + 1.) Let ℓ_I satisfy [[eq:iii-g3-1-2]],
l := 2⌈ℓ_I⌉ + 10, and f ∈ H^(k+l,(⟨ℰ_I^C+1⟩′,ℓ_I+1))_b([0, 1)_v × 𝕊³; S²T*). There is
u(λ) ∈ H^(k+2,(⟨ℰ_I^C⟩,ℓ_I))_b([0, 1)_v × 𝕊³), linear and continuous in f, a finite sum
χ_I Σ v^z(log v)^j c_(z,j)(λ, ω) supported in {v < 1}, such that:

(1) u is meromorphic in λ ∈ ℂ, with divisor contained in {(z, k(ℰ^C_(I,♯), z)) : z ∈ π₁ℰ^C_(I,♯), Re z < ℓ_I}, where

    ℰ^C_(I,♯) := (λ_♯, 0) ∪ ℰ_I^C ⊂ ℰ_I^tot;                                                             {#eq:iii-g3-2-1}

(2) away from the poles, f − N_(ι⁺)(λ)u(λ) ∈ H^(k,ℓ_I+1)_b([0, 1)_v × 𝕊³).

Here χ_I ∈ C_c^∞([0, 1)_v) equals 1 on [0, ½].

*Proof.* By [[eq:iii-g3-1-1]], N_(ι⁺)(λ)u = f is (v∂_v − λ)(v∂_v − 3/2 − Ā)u + Ñu = g, with g := −(1/(2v))f and
Ñ := −(v/2)L̃(0) ∈ v Diff²_b. Near v = 0, g has, at weight ℓ_I, the index set ℰ_I^C in slots 1–6 and
ℰ_I^C ∪ (λ_♯, 0) in slot 7 ([[def:iii-c-5-1]]). Of the latter, only the term v^(λ_♯) itself lies outside ℰ_I^C, since
λ_♯ + j ∈ ℰ_I^C for j ≥ 1 ([[lem:iii-c-3-2]] (d)). If f has no expansion at v = 0, take u = 0.

*The exceptional term.* Let g_exc := χ_I v^(λ_♯)g_♯(ω)e₇. As e₇ is an eigenvector of Ā for 2γ_Υ
([[lem:iii-g3-1-2]] (1)), w♭_exc := (λ_♯ − 3/2 − 2γ_Υ)⁻¹v^(λ_♯)g_♯e₇ = −((1 + e_Υ)γ_Υ)⁻¹v^(λ_♯)g_♯e₇ solves
(v∂_v − 3/2 − Ā)w♭_exc = v^(λ_♯)g_♯e₇. (On all of S²T*, λ_♯ − 3/2 − Ā is not invertible, as
λ_♯ − 3/2 = (1 − e_Υ)γ_Υ ∈ spec Ā; only its restriction to the line of e₇ is used.) Let
w_exc(λ) := (λ_♯ − λ)⁻¹w♭_exc ([[lem:iii-g3-2-1]]), with a simple pole at λ_♯.

*The terms of ℰ_I^C.* For (z, j) ∈ ℰ_I^C with Re z < ℓ_I: Re z − 3/2 ∈ (2γ_Υ, s_C) ([[def:iii-c-3-1]] (2) and
[[eq:iii-g3-1-2]]), and spec Ā ⊂ [0, 2γ_Υ] ∪ [s_C, ∞) ([[eq:iii-f-3-1]]). So z − 3/2 − Ā is invertible, and
w♭ := ∂_z^j(v^z(z − 3/2 − Ā)⁻¹)c solves (v∂_v − 3/2 − Ā)w♭ = v^z(log v)^j c for a coefficient c(ω) held fixed. Let
w(λ) := (v∂_v − λ)⁻¹w♭, calculated term by term by [[lem:iii-g3-2-1]] (ii): meromorphic, with poles only at λ = z, of
order at most j + 1.

*Iteration.* Solving away a term T at exponent z by χ_I w leaves −Ñ(χ_I w) and terms supported in {½ ≤ v < 1}. As
L̃(0) is a b-operator in (v∂_v, ∂_ω) with smooth coefficients, Ñ(χ_I w) has the exponents z + 1, with the same
logarithmic orders and coefficients with the same poles in λ, and two fewer derivatives in ω. Treat the exponents in
order of increasing real part. Each new exponent lies in ℰ^C_(I,♯) + ℕ ⊂ ℰ_I^C and has real part in
(3/2 + 2γ_Υ, ℓ_I) while it is to be solved away, so the invertibility above applies. There are finitely many such
exponents, since ℰ^C_(I,♯) is an index set, and none has real part ℓ_I, by [[eq:iii-g3-1-2]]. A chain from the least
exponent to ℓ_I has at most ⌈ℓ_I⌉ steps, losing at most 2⌈ℓ_I⌉ < l − 2 derivatives. The remaining terms have real part
above ℓ_I and lie in H^(k,ℓ_I)_b at the level of g, so in H^(k,ℓ_I+1)_b at that of f. The poles: at each z, the solving
step contributes order at most j + 1 ≤ k(ℰ^C_(I,♯), z) + 1, and the coefficients carried from lower exponents z′ have
poles only at those z′. So the divisor is as stated. u lies in ⟨ℰ_I^C⟩: the exceptional term sits in slot 7 at
λ_♯ ∈ ℰ_(I,11), and all other exponents are in ℰ_I^C. ∎

**Lemma {#lem:iii-g3-2-3}** (Uniqueness below the least exponent.) Let h ∈ H^(k,(⟨ℰ_I^C⟩,ℓ_I),β)_b(ι⁺) with
β ∈ (−1, 0) and k ≥ k₀(Re z), the regularity that [[thm:iii-g1-3-1]] (2) needs at z (it depends on Re z through the
loss d there). Then N_(ι⁺)(z)h ∈ H^(k−2,(⟨ℰ_I^C+1⟩′,ℓ_I+1),β−2)_b for every z. Let w₀ be a lower bound for the real
parts of the exponents of h at v = 0, let Re z < ℓ′ ≤ w₀, let z not be a pole of the inverse of [[thm:iii-g1-3-1]]
(all uses below have Re z < 2, where it has none, [[lem:iii-g1-4-2]] (a)), and suppose N_(ι⁺)(z)h lies in the domain
H^(k−2,ℓ′+1,β−2)_b of [[thm:iii-g1-3-1]] (2) with ℓ′ for its ℓ_I. Then N_(ι⁺)(z)⁻¹N_(ι⁺)(z)h = h, with the inverse of
[[thm:iii-g1-3-1]]. For h as above, w₀ = 3/2 and any ℓ′ ∈ (Re z, 3/2) serve when Re z < 3/2, the exponents of
N_(ι⁺)(z)h being at least λ_♯ + 1 > 5/2.

*Proof.* The mapping property near v = 0 is the calculation of the leading part in the proof of [[prop:iii-c-5-2]], with
v∂_v in place of X_I and the factor (v∂_v − z) preserving index sets, together with v²L̃(0) mapping ℰ_I^tot into
ℰ_I^tot + 2 ⊂ ℰ_I^C + 1 ([[lem:iii-c-3-2]] (c)). Near R = 0, N_(ι⁺)(z) ∈ R⁻²Diff²_b ([[eq:iii-g1-1-3]]). For the
identity: every exponent w of h at v = 0 has Re w ≥ w₀ > Re z. So R^z h = v^(−z)h, extended by 0 to {v < 0}, is a sum of
terms v₊^(w−z)c(ω) (powers of log allowed), Re(w − z) > 0, and a remainder of positive order; these lie in H^s near
v = 0 for every s < ½ + Re(w − z), and are b-regular there. With the admissible choice s = min(½, 2 − Re z) − δ and μ of
the proof of [[thm:iii-g1-3-1]] (its Step 5 (ii), with ℓ_K = β > −1), R^z h lies in the space on which N_sf(z) is
invertible ([[thm:iii-g-5-1]]). Since v₊^(w−z) is continuous at v = 0, the derivative across v = 0 creates no term
supported there, so N_sf(z)(R^z h) is the extension by 0 of R^(2+z)N_(ι⁺)(z)h. By [[eq:iii-g1-3-1]],
N_(ι⁺)(z)⁻¹N_(ι⁺)(z)h = R^(−z)N_sf(z)⁻¹N_sf(z)R^z h = h. ∎

**Proposition {#prop:iii-g3-2-4}** ([Hin26, Proposition 9.15] in dimension 4 + 1.) Let ℓ_I, ℓ_K be as in
[[sec:iii-g3-1]]. The map N_(ι⁺)(λ)⁻¹ of [[thm:iii-g1-3-1]], on the space of [[def:iii-g3-1-1]], extends from
{Re λ < λ_♯} to a meromorphic family

    N_(ι⁺)(λ)⁻¹ : H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),ℓ_K−2)_b(ι⁺) → H^(∞,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺),
    Re λ < ℓ_I,                                                                                          {#eq:iii-g3-2-2}

which inverts N_(ι⁺)(λ) (N_(ι⁺)(λ)N_(ι⁺)(λ)⁻¹f = f). Its poles lie in spec_(ι⁺)(L̄) ∪ π₁ℰ^C_(I,♯), and the order of a
pole λ₀ is at most m_ι(λ₀) + m_♯(λ₀), where m_ι is the order of the pole of [[eq:iii-g1-3-3]] at λ₀ (0 if none)
and m_♯(λ₀) := k(ℰ^C_(I,♯), λ₀) + 1 (0 if λ₀ ∉ π₁ℰ^C_(I,♯)). At finite regularity: for every ε > 0 and
λ₋ < ℓ_I − ε there is l′ such that [[eq:iii-g3-2-2]] holds from H^(k+l′) to H^k on {λ₋ < Re λ < ℓ_I − ε} for every k.

*Proof.* Given f, let u(λ) be as in [[lem:iii-g3-2-2]] for f near v = 0 (it already carries the cut-off χ_I; the second
cut-off below changes nothing, χ_I² having the same properties), and set f′(λ) := f − N_(ι⁺)(λ)(χ_I u(λ)). Near v = 0
this is [[lem:iii-g3-2-2]] (2), up to terms supported in {½ ≤ v < 1}; for v ≥ 1 it equals f. So
f′(λ) ∈ H^(∞,ℓ_I+1,ℓ_K−2)_b(ι⁺), meromorphic with the poles of u. Let u′(λ) := N_(ι⁺)(λ)⁻¹f′(λ) by
[[thm:iii-g1-3-1]] (2), finite-meromorphic on {Re λ < ℓ_I}, in H^(∞,(⟨ℰ^C_(ι⁺,ℐ)⟩,ℓ_I),(ℰ_K,ℓ_K))_b, which lies in
the target by [[lem:iii-g3-1-2]] (2). Then N_(ι⁺)(λ)(χ_I u + u′) = f, and χ_I u + u′ is in the target space. The poles
are those of u ([[lem:iii-g3-2-2]] (1)) and those of u′, which come from f′ and from the inverse of
[[thm:iii-g1-3-1]]; at λ₀ the Laurent orders add, giving the bound.

*Agreement below λ_♯.* For Re λ < λ_♯ all exponents of f at v = 0 are at least λ_♯ + 1, so f lies in the domain of
[[thm:iii-g1-3-1]] (2) with ℓ′ := λ_♯ − δ, and u(λ) is holomorphic there. By [[lem:iii-g3-2-3]] with w₀ = λ_♯, the
least exponent of χ_I u, and ℓ′ ∈ (Re λ, λ_♯), N⁻¹N(χ_I u) = χ_I u, so χ_I u + u′ = N⁻¹(Nχ_I u + f′) = N⁻¹f.

*Finite regularity.* The loss d of [[thm:iii-g1-3-1]] depends on λ only through Re λ: through the regularity s and the
number of steps, at most ⌈ℓ_I − Re λ⌉ + 2, each losing two derivatives (Step 5 (ii)–(iii) of its proof). Near each
value of Re λ one s serves, its condition s < min(½, 2 − Re λ) being open; so d is locally bounded in Re λ, hence
bounded on [λ₋, ℓ_I − ε], and l′ := l + sup d serves. ∎

**Definition {#def:iii-g3-2-5}** ([Hin26, Definition 9.16].) spec^(<ℓ_I)_(ι⁺)(L̄, ℰ_I^C) ⊂ {Re λ < ℓ_I} is the set of
poles of [[eq:iii-g3-2-2]], and Spec^(<ℓ_I)_(ι⁺)(L̄, ℰ_I^C) the set of (λ, k) with λ a pole of order k + 1.

**Corollary {#cor:iii-g3-2-6}** ([Hin26, (9.49)] in dimension 4 + 1.) If λ_♯ < ℓ_I, then
(λ_♯, 0) ∈ Spec^(<ℓ_I)_(ι⁺)(L̄, ℰ_I^C). Every other element of spec^(<ℓ_I)_(ι⁺)(L̄, ℰ_I^C) has real part greater than
3/2 + 2γ_Υ, and none has real part below λ_♯.

*Proof.* spec_(ι⁺)(L̄) ⊂ {Re ≥ 2} ([[lem:iii-g1-4-2]] (a)), and
π₁ℰ^C_(I,♯) ⊂ {λ_♯} ∪ {Re > 3/2 + 2γ_Υ}, with λ_♯ < 3/2 + 2γ_Υ < 2. The order at λ_♯ is at most 0 + 1, as
λ_♯ ∉ π₁ℰ_I^C. It is a pole: take f with only the exceptional term, g_♯ ≠ 0. The residue of χ_I u at λ_♯ has the term
−χ_I w♭_exc, a non-zero multiple of v^(λ_♯)g_♯e₇, and its other terms have exponents λ_♯ + j, j ≥ 1. The residue of u′
is N_(ι⁺)(λ_♯)⁻¹ of the residue of f′ (the inverse of [[thm:iii-g1-3-1]] is holomorphic at λ_♯ < 2), so it lies in the
space of [[def:iii-g1-1-2]], where its Π_(2γ_Υ)-component has index set ℰ_(2γ_Υ) = ℰ^C_(ι⁺,ℐ) ∪ (3/2 + 2γ_Υ, 0), which
does not contain λ_♯ (ℰ^C_(ι⁺,ℐ) starts at 5/2). As Π_(2γ_Υ)e₇ = e₇, the Π_(2γ_Υ)-component of the residue of
χ_I u + u′ has a non-zero v^(λ_♯)-term. (Slot 7 alone would not do: it also receives the component along the
eigenvector for (1 − e_Υ)γ_Υ, [[lem:iii-g3-1-2]] (1).) ∎

At the exponent λ_♯ itself the agreement of [[prop:iii-g3-2-4]] with the inverse of [[thm:iii-g1-3-1]] fails:
R^(λ_♯)(v^(λ_♯)e₇) extended by 0 is v₊⁰e₇, and N_sf(λ_♯) = −2∂_v(v∂_v + λ_♯ − 3/2 − S̄) + … applied to it produces
−2δ(v)(λ_♯ − 3/2 − 2γ_Υ)e₇ ≠ 0 at the light cone. So v^(λ_♯)e₇ is not in the range of the inverse of
[[thm:iii-g1-3-1]], whose outputs carry no incoming term ([[thm:iii-g1-3-1]] (1)).

**Remark {#rem:s17-exceptional}** (When the pole at λ_♯ is excited.) In [Hin26, (9.49)] the boundary spectrum contains
(1, 0), from the coupling of the radiation field into the (dx¹)²-component and from the mass term; in dimension 4 + 1
both land in ℰ_I^C ([[rem:s17-no-radiation]]) and give no pole. The pole at λ_♯ < 2 is excited only by sources with an
exceptional term v^(1+λ_♯)e₇ at ℐ⁺ ∩ ι⁺. For f = N_(ι⁺)(λ)h with h as in [[def:iii-g3-1-1]], such a term arises exactly
when Π_(2γ_Υ)h carries a v^(λ_♯)-term, that is, when the v^(λ_♯)-coefficients c₄, c₇ of slots 4 and 7 of h are not in
the ratio of the eigenvector of Ā for (1 − e_Υ)γ_Υ ([[lem:iii-g3-1-2]] (1)): by the calculation of the leading part in
the proof of [[prop:iii-c-5-2]], slot 7 of (v∂_v − 3/2 − Ā)h at v^(λ_♯) is −(1 + e_Υ)γ_Υc₇ − Ā₇₄c₄, which vanishes
along that eigenvector. The set ℰ_(I,11) allows such a term, and the space of [[def:iii-g1-1-2]] does not. In
[[ch:s23]] the right-hand sides of the steps have no expansion at ℐ⁺, so the pole at λ_♯ enters only through a datum
at that frequency, and the index sets at ι⁺ contain (λ_♯, 0). The identification of [[prop:iii-g3-2-4]] with the
inverse of [[thm:iii-g1-3-1]] below λ_♯ holds by uniqueness in the admissible spaces of [[thm:iii-g-5-1]]: the
extension by zero of v₊^(w−λ), Re(w − λ) > 0, lies in them and creates no term at the light cone ([[lem:iii-g3-2-3]]);
at the incoming exponent itself the extension by zero creates δ(v), which is why λ_♯ is a pole.

**Remark {#rem:iii-g3-2-7}** ([Hin26, Remark 9.17] in dimension 4 + 1.) Let (α, 0) ∈ ℰ_I^C with
3/2 + 2γ_Υ < α < ℓ_I, α ∉ spec_(ι⁺)(L̄) and α ∉ π₁ℰ^C_(ι⁺,ℐ) ∪ (3/2 + σ_Υ + ℕ₀), and f := χ_I v^(α+1)f₀(ω),
f₀ ≠ 0. Then N_(ι⁺)(λ)⁻¹f has a simple pole at λ = α: as in [[cor:iii-g3-2-6]], the v^α-term of the residue, a
non-zero multiple of (α − 3/2 − Ā)⁻¹f₀, cannot be cancelled by the residue of u′, whose exponents lie in
π₁ℰ^C_(ι⁺,ℐ) ∪ (3/2 + σ_Υ + ℕ₀). In the language of scattering, the residue solves the problem at frequency α with
incoming data v^α u₀, u₀ = (α − 3/2 − Ā)⁻¹(½f₀) (the residue of (α − λ)⁻¹w♭ is −w♭, and g = −(1/(2v))f), and its
outgoing data are its radiation fields at 3/2 + spec Ā. So ℰ_I^C specifies the frequencies at which incoming data are
allowed.

### Quasi-homogeneous solutions and resonant states {#sec:iii-g3-3}

This section is [Hin26, Corollary 9.18 to Remark 9.24] in dimension 4 + 1.

**Corollary {#cor:iii-g3-3-1}** ([Hin26, Corollary 9.18] in dimension 4 + 1.) Let Re λ₀ < ℓ_I, J ∈ ℕ₀, and

    f = Σ_(j=0)^J t_*^(−λ₀−2)(log t_*)^j f^((λ₀+2,j))(R, ω),
    f^((λ₀+2,j)) ∈ H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),ℓ_K−2)_b(ι⁺).                                                 {#eq:iii-g3-3-1}

Let K be the order of the pole of [[eq:iii-g3-2-2]] at λ₀ (0 if none). Then:

(1) (*Existence.*) There is a solution of 2L̄u = f, linear in f, of the form

    u = Σ_(j=0)^(J+K) t_*^(−λ₀)(log t_*)^j u^((λ₀,j))(R, ω),
    u^((λ₀,j)) ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺).                                                   {#eq:iii-g3-3-2}

(2) (*Expansion at R = 0.*) u = χ_K u₀ + ũ, with χ_K the cut-off of [[sec:iii-g2-4]] restricted to ι⁺ (the formal
solutions grow as R → ∞), u₀ a sum of the formal solutions of [[ch:s16]] ([[eq:iii-g2-3-1]] and [[lem:iii-g2-2-4]] (b),
with the conventions for s1 and v1) with t_*^(−λ) replaced by t_*^(−λ₀)(log t_*)^j, j ≤ J + K, and ũ a sum of terms
t_*^(−λ₀)(log t_*)^j H^(∞,(⟨ℰ_I^C⟩,ℓ_I),ℓ_K)_b(ι⁺). This holds for every solution of the form [[eq:iii-g3-3-2]] of
2L̄u = f with f as in [[eq:iii-g3-3-1]] (with J + K for J).

*Proof.* (1) After scalar factors, f = (1/(2πi)) ∮ t_*^(−λ−2) Σ_j (λ − λ₀)^(−j−1)f^((λ₀+2,j)) dλ over a small circle
around λ₀, and u := (1/(2πi)) ∮ t_*^(−λ) Σ_j (λ − λ₀)^(−j−1)N_(ι⁺)(λ)⁻¹f^((λ₀+2,j)) dλ is defined by
[[prop:iii-g3-2-4]], with a pole of the integrand of order at most J + 1 + K at λ₀. By [[eq:iii-g3-1-1]],
2L̄(t_*^(−λ)w) = t_*^(−λ−2)N_(ι⁺)(λ)w, so 2L̄u = f, and the residue expands into [[eq:iii-g3-3-2]].

(2) As in [Hin26]. Near R = 0 the top term satisfies N_(ι⁺)(λ₀)u^((λ₀,J)) ∈ H^(∞,ℓ_K−2)_b, so by [[thm:iii-g2-3-1]] it
is a sum of formal solutions modulo H^(∞,ℓ_K)_b. Each such term is removed by subtracting its (log t_*)^J-version, the
formal solution of [[thm:iii-g2-3-1]] with argument t_*^(−λ₀+μ)(log t_*)^J Y. Since
t_*^(−λ)(log t_*)^J = (−∂_λ)^J t_*^(−λ) and the errors of the formal solutions of [[thm:iii-g2-3-1]],
t_*^(−λ−2)R^(−μ+k_μ−1)C^∞ (its proof), depend holomorphically on λ, the error of the subtracted term lies in
Σ_(j≤J) t_*^(−λ₀−2)(log t_*)^j H^(∞,ℓ_K−2)_b near R = 0, as −μ + k_μ − 1 ≥ 1 > ℓ_K − 2. Then induct downwards on j: if
u^((λ₀,j)) ∈ H^(∞,ℓ_K)_b for j > j₀, the coefficient of t_*^(−λ₀−2)(log t_*)^(j₀) in 2L̄u gives
N_(ι⁺)(λ₀)u^((λ₀,j₀)) − (j₀ + 1)∂_λN_(ι⁺)(λ₀)u^((λ₀,j₀+1)) ∈ H^(∞,ℓ_K−2)_b, as N_(ι⁺) is linear in λ. Here
∂_λN_(ι⁺) = 2v(v∂_v − 3/2 − S̄) ∈ R⁻¹Diff¹_b, so the second term lies in H^(∞,ℓ_K−1)_b, and the first step applies to
u^((λ₀,j₀)). ∎

**Definition {#def:iii-g3-3-2}** ([Hin26, Definition 9.19] in dimension 4 + 1.) For Re λ < ℓ_I and k ∈ ℕ₀ ∪ {∞},

    Res^k_(ι⁺)(L̄, ℰ_I^C, λ) := {u = Σ_(j=0)^K t_*^(−λ)(log t_*)^j u^((λ,j))(v, ω) : L̄u = 0,
                                u^((λ,j)) ∈ H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺), K ∈ ℕ₀}.                {#eq:iii-g3-3-3}

So the solution of [[cor:iii-g3-3-1]] is unique modulo Res^∞_(ι⁺)(L̄, ℰ_I^C, λ₀).

**Remark {#rem:iii-g3-3-3}** ([Hin26, Remark 9.20] in dimension 4 + 1.) The proof of [[cor:iii-g3-3-1]] (2) applies to
the elements of [[eq:iii-g3-3-3]], for every ℓ_K < ℓ_K^max allowed in [[sec:iii-g3-1]]: it describes their asymptotics
as R → 0 modulo O(R^(ℓ_K)). By [[rem:iii-g3-2-7]], [[eq:iii-g3-3-3]] depends on ℰ_I^C, and it is infinite-dimensional,
the incoming data being sections over 𝕊³ ([[def:iii-g3-3-6]] and [[prop:iii-g3-3-7]]).

**Lemma {#lem:iii-g3-3-4}** (Left inverse.) Let β ∈ (−1, 0). For h ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),β)_b(ι⁺),
N_(ι⁺)(z)⁻¹N_(ι⁺)(z)h = h as meromorphic functions on {Re z < ℓ_I}, with [[eq:iii-g3-2-2]] for ℓ_K = β. For finite k
the same holds on every strip {λ₋ < Re z < ℓ_I − ε}, λ₋ < 3/2, when h has b-regularity k ≥ l′(λ₋, ε) + 2, with l′
of [[prop:iii-g3-2-4]].

*Proof.* β is admissible in [[sec:iii-g3-1]]: ℰ_K ⊂ {Re ≥ 0}, and no root of [[prop:iii-f1-2-3]] has real part in
(0, 1). So (ℰ_K, β) is the weight β alone, and N_(ι⁺)(z)h lies in the domain of [[eq:iii-g3-2-2]] by the mapping
property of [[lem:iii-g3-2-3]]. Both sides are meromorphic in z. For Re z < 3/2 they agree by [[lem:iii-g3-2-3]], as
N(z)h then has exponents above 5/2 at v = 0, so it lies in the domain of [[thm:iii-g1-3-1]] with some
ℓ′ ∈ (Re z, 3/2), and [[eq:iii-g3-2-2]] agrees there with the inverse of [[thm:iii-g1-3-1]] ([[prop:iii-g3-2-4]]). By
the identity theorem they agree on the connected set {Re z < ℓ_I} off the poles; at finite k, on the strip, which off
the poles is connected and meets {Re z < 3/2}. ∎

**Lemma {#lem:iii-g3-3-5}** ([Hin26, Lemma 9.21] in dimension 4 + 1.) Res^k_(ι⁺)(L̄, ℰ_I^C, λ) does not depend on the
choice of ℓ_K. For k = ∞ it is the space of the tensors

    res_(z=λ)(t_*^(−z)N_(ι⁺)(z)⁻¹f(z)),                                                                {#eq:iii-g3-3-4}

f a polynomial in z with values in H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),β−2)_b(ι⁺), β ∈ (−1, 0) arbitrary. For finite k it is
contained in (resp. contains) the space of such tensors with f of b-regularity k − l′ (resp. k + l′), l′ as in
[[prop:iii-g3-2-4]] on a strip containing λ.

*Proof.* Independence of ℓ_K: by [[rem:iii-g3-3-3]] the elements have the expansion of [[cor:iii-g3-3-1]] (2) at R = 0
for every allowed ℓ_K. The tensor [[eq:iii-g3-3-4]] is annihilated by 2t_*²L̄: writing the residue as (1/(2πi))∮, this
gives (1/(2πi))∮ t_*^(−z)f(z) dz = 0, f being holomorphic; and by [[eq:iii-g3-2-2]] it has the form
[[eq:iii-g3-3-3]]. Conversely let u = Σ_(j≤K) t_*^(−λ)(log t_*)^j u^((λ,j)) be in [[eq:iii-g3-3-3]]. After scalar
factors, u = (1/(2πi))∮ t_*^(−z)ũ(z) dz with ũ(z) := Σ_j (z − λ)^(−j−1)u^((λ,j)), and L̄u = 0 says that
res_(z=λ)(t_*^(−z−2)N_(ι⁺)(z)ũ(z)) = 0 for all t_*, so N_(ι⁺)(z)ũ(z) is holomorphic at λ. Let f(z) be its Taylor
polynomial at λ of degree K(λ), the order of the pole of [[eq:iii-g3-2-2]] at λ. By the independence just shown, take
ℓ_K ∈ (0, ℓ_K^max). Then near R = 0, u^((λ,j)) ∈ H^(k,−ε)_b for every ε > 0 (ℰ_K ∩ {Re = 0} = {(0, 0)},
[[lem:iii-g1-1-3]] (b)), so with β := −ε and the mapping property of [[lem:iii-g3-2-3]], f takes values in
H^(k−2,(⟨ℰ_I^C+1⟩′,ℓ_I+1),β−2)_b. By [[lem:iii-g3-3-4]] (for finite k, on a strip containing λ),
N(z)⁻¹N(z)ũ(z) = ũ(z), and N(z)⁻¹(N(z)ũ(z) − f(z)) is holomorphic at λ, its argument vanishing to order K(λ) + 1
there. So u = res_(z=λ)(t_*^(−z)ũ(z)) = res_(z=λ)(t_*^(−z)N(z)⁻¹f(z)). ∎

**Definition {#def:iii-g3-3-6}** ([Hin26, (9.54)–(9.55)] in dimension 4 + 1.) For Re λ < ℓ_I, Res_(ι⁺)(L̄, λ) is the
space of tensors [[eq:iii-g3-3-4]] with f a polynomial with values in H^(k,ℓ_I+1,β−2)_b. By the finite-meromorphy of
[[thm:iii-g1-3-1]] (2) it is finite-dimensional, consists of tensors of infinite b-regularity, and does not depend on k;
it lies in Res^∞_(ι⁺)(L̄, ℰ_I^C, λ). The quotient H^(k,(⟨ℰ_I^C+1⟩′,ℓ_I+1),β−2)_b / H^(k,ℓ_I+1,β−2)_b is identified with

    H^(k,(⟨ℰ_I^C+1⟩′,≤ℓ_I+1))_b := {χ_I(f₁₁^((λ_♯+1,0))v^(λ_♯+1)e₇
                                    + Σ_((ν,j)∈ℰ_I^C+1, Re ν≤ℓ_I+1) v^ν(log v)^j f^((ν,j))(ω))},         {#eq:iii-g3-3-5}

f₁₁^((λ_♯+1,0)) ∈ H^k(𝕊³), f^((ν,j)) ∈ H^k(𝕊³; S²T*): finitely many copies of H^k(𝕊³). The first term is present only
if λ_♯ < ℓ_I; otherwise v^(λ_♯+1)e₇ lies in H^(k,ℓ_I+1)_b. [Hin26, (9.55)] has two exceptional terms, v² and
v^(2+(1−e_Υ)γ_Υ) in the (dx¹)²-component; here there is one.

**Proposition {#prop:iii-g3-3-7}** ([Hin26, Proposition 9.22] in dimension 4 + 1.) Let Re λ < ℓ_I, K(λ) the order of
the pole of [[eq:iii-g3-2-2]] at λ, and Poly^K(ℂ_z; X) the polynomials of degree at most K with coefficients in X. There
is l = l(ℓ_I, λ) such that for k ≥ l the map

    Res_(ι⁺)(L̄, λ) ⊕ Poly^(K(λ))(ℂ_z; H^(k,(⟨ℰ_I^C+1⟩′,≤ℓ_I+1))_b) → Res^(k−l)_(ι⁺)(L̄, ℰ_I^C, λ),
    (u₀, f) ↦ u₀ + res_(z=λ)(t_*^(−z)N_(ι⁺)(z)⁻¹f(z)),                                                   {#eq:iii-g3-3-6}

defined independently of k, is well defined and continuous, and Res^k_(ι⁺)(L̄, ℰ_I^C, λ) lies in the range of the map
for k − l in place of k. There is a right inverse for k = ∞ which is continuous from Res^k to the domain with k − l for
every k.

*Proof.* Well-definedness and continuity: [[prop:iii-g3-2-4]] on a strip containing λ, and [[eq:iii-g3-3-5]] as a
subspace of the domain of [[eq:iii-g3-2-2]]. The proof of [[lem:iii-g3-3-5]] gives a map
u ↦ f ∈ Poly^(K(λ))(ℂ; H^(k−l,(⟨ℰ_I^C+1⟩′,ℓ_I+1),β−2)_b) with u = res(t_*^(−z)N⁻¹f), β ∈ (−1, 0) fixed, defined
independently of k. Split f = f₁ + f₂ uniquely, f₁ with values in H^(k−l,ℓ_I+1,β−2)_b and f₂ in [[eq:iii-g3-3-5]]: f₂
is the finite expansion of f at v = 0 cut off by χ_I. The right inverse is u ↦ (res(t_*^(−z)N⁻¹f₁), f₂), the first
component in Res_(ι⁺)(L̄, λ) by [[def:iii-g3-3-6]]. ∎

So [[eq:iii-g3-3-6]] parametrises the quasi-homogeneous nullspace by a finite-dimensional piece of pure resonant states
(no incoming data) and an infinite-dimensional piece of finite description that encodes incoming data through the
sources.

**Remark {#rem:iii-g3-3-8}** ([Hin26, Remark 9.23] in dimension 4 + 1.) [[eq:iii-g3-3-6]] over-parametrises. At
λ = λ_♯ (when λ_♯ < ℓ_I), the counterpart of λ = 1 in [Hin26]: Res_(ι⁺)(L̄, λ_♯) = {0}, as λ_♯ < 2
([[lem:iii-g1-4-2]] (a)), and N_(ι⁺)(z)⁻¹f has no pole at z = λ_♯ unless f₁₁^((λ_♯+1,0)) ≠ 0 in [[eq:iii-g3-3-5]]: the
other terms of [[eq:iii-g3-3-5]] have exponents in ℰ_I^C + 1, whose poles lie in π₁ℰ_I^C ([[lem:iii-g3-2-2]]), and
λ_♯ ∉ π₁ℰ_I^C.

**Remark {#rem:iii-g3-3-9}** ([Hin26, Remark 9.24] in dimension 4 + 1.) Let
λ ∈ spec^(<ℓ_I)_(ι⁺)(L̄, ℰ_I^C) ∖ spec_(ι⁺)(L̄) (for instance λ = λ_♯) and let u ≠ 0 be the image of (0, f) under the map
[[eq:iii-g3-3-6]]. N_(ι⁺) is SO(4)-equivariant, so it preserves the components of each harmonic
degree ([[sec:iii-a1-1]]). The formal solutions at R = 0 below ℓ_K^max occur only at the roots of the table of
[[sec:iii-g2-1]], whose types have degree at most 4 (s4 at −2). So if f has only harmonic components of degree ≥ 5, the
expansion of u at R = 0 is trivial modulo O(R^(ℓ_K)) for every ℓ_K < ℓ_K^max. Even an arbitrarily high finite order of
vanishing at R = 0 thus leaves an infinite-dimensional space of resonant states that are not pure. ([Hin26]: degree at
most 5, l ≥ 6.)

### The operator at null infinity and the radiative order at ι⁺ {#sec:s17-radiative}

This section collects what the preceding sections give for the gauge-fixed operator at null infinity, entry by entry,
and for the order at which a radiative term reaches future timelike infinity.

**Proposition {#prop:np-10-38}** (The operator at null infinity, and the radiative order at ι⁺.) Let the parameters be
as in [[sec:iii-c-1]] and [[sec:iii-g3-1]].

(1) (*The matrix at null infinity.*) In the splitting [[eq:iii-c-1-6]], the matrix Ā of [[lem:iii-c-4-2]] is lower
triangular with the diagonal [[eq:iii-c-4-3]] and the off-diagonal entries

    Ā₃₁ = (4/3)(1 − e_C)(1 + v_C)γ_C,              Ā₄₁ = (1 + 2e_C)(1 + v_C)γ_C/3 + γ_Υ,
    Ā₄₃ = ((1 + 2e_C)(1 − v_C)γ_C + 3e_Υγ_Υ)/4,    Ā₅₂ = (1 + v_C)γ_C + γ_Υ,
    Ā₇₃ = (3/2)((1 + v_C)γ_C + e_Υγ_Υ),            Ā₇₄ = 2(1 − e_Υ)γ_Υ,                                {#eq:s17-abar}

all other entries being 0. In spatial dimension 3 the same construction, with the factor 1 in place of ⅔ in E^C and
½tr̸h as the coordinate of the third slot, gives [Hin26, (5.28)] at h = 0: the same diagonal and the same entries
(5, 2) and (7, 4), and Ā₃₁ = 2(1 − e_C)(1 + v_C)γ_C, Ā₄₁ = e_C(1 + v_C)γ_C + γ_Υ,
Ā₄₃ = (e_C(1 − v_C)γ_C + e_Υγ_Υ)/2, Ā₇₃ = (1 + v_C)γ_C + e_Υγ_Υ.

(2) (*The exponents at null infinity, type by type.*) Let τ be one of the types s0, v1, v2, t2 ([[sec:iii-a1-1]]) and
Y a harmonic of that type (Y ∈ 𝒮_0, 𝒱_1, 𝒱_2, 𝒯_2 respectively). The symmetric 2-tensors of type τ given by Y have, in
the splitting [[eq:iii-c-1-6]], components only in the slots

    J_s0 := {1, 3, 4, 7},     J_v1 := {2, 5},     J_v2 := {2, 5, 6},     J_t2 := {6},

with one dimension for each slot of J_τ, and Ā maps their span to itself, acting by its submatrix (Ā_ij)_(i,j∈J_τ).
Near v = 0 on ι⁺, S̄ has the matrix Ā in the slots ([[sec:iii-g3-1]]), and for a section φ over 𝕊³

    N_(ι⁺)(λ)(v^xφ) = −2v^(x+1)(x − λ)(x − 3/2 − Ā)φ + v^(x+2)L̃(0)(ω, x, ∂_ω)φ,

so the indicial family of v⁻¹N_(ι⁺)(λ) at ℐ⁺ ∩ ι⁺ is −2(x − λ)(x − 3/2 − Ā). On the type-τ tensors given by Y its
determinant is the product of −2(x − λ)(x − 3/2 − Ā_jj) over j ∈ J_τ. Over the four types its roots are λ, the
constraint exponents 3/2 + σ_C (slots 1–3, σ_C of [[eq:iii-g1-1-4]]) and the radiative
exponents 3/2 + σ_Υ (slots 4–7): 3/2 + (1 − e_Υ)γ_Υ, 3/2 + γ_Υ, 3/2 and 3/2 + 2γ_Υ, the exponents of the index sets
[[eq:iii-c-3-2]].

(3) (*Couplings through the perturbation.*) For g = g₁ + h as in [[prop:iii-c-4-4]], every coupling through h lies in
the error term of [[eq:iii-c-4-4]], a factor ρ_I^(1/2) below Ā at ℐ⁺ when ℱ = ℰ_I^tot. The entry Ā₇₄ couples the
leading term of π₀₁ into the 11-component at the exponent λ_♯ = 3/2 + (1 − e_Υ)γ_Υ; the radiation field of π̸₀ reaches
the 11-component only at the order 2, which lies in ℰ_I^C: ℱ_(I,11) = 1 + (ℰ_I^C ∪ (λ_♯, 0)).

(4) (*The radiative order at ι⁺.*) spec_(ι⁺)(L̄) ⊂ {Re λ ≥ 2}. In particular no radiative exponent 3/2 + s, s ∈ σ_Υ,
lies in spec_(ι⁺)(L̄): there is no pure resonant state at a radiative exponent (Res_(ι⁺)(L̄, 3/2 + s) = {0} whenever
3/2 + s < ℓ_I). Nor is there an outgoing solution there, or at any other λ with Re λ < min(ℓ_I, 2): if h lies in the
space H^(∞,(⟨ℰ^C_(ι⁺,ℐ)⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺) of [[def:iii-g1-1-2]] (2), the target of [[thm:iii-g1-3-1]] (2), and
N_(ι⁺)(λ)h = 0 with Re λ < min(ℓ_I, 2), then h = 0. On the spaces of [[def:iii-g3-1-1]], if λ_♯ < ℓ_I, the only
pole of [[eq:iii-g3-2-2]] with real part at most 3/2 + 2γ_Υ is λ_♯; it is simple, and it is a pole of N_(ι⁺)(z)⁻¹f
only if f has the exceptional term f₁₁^((λ_♯+1,0))v^(λ_♯+1)e₇ ≠ 0 of [[eq:iii-g3-3-5]]. If ℓ_I ≤ λ_♯, there is no
such pole. The radiative exponents 3/2, 3/2 + γ_Υ and 3/2 + 2γ_Υ are not poles.

*Proof.* (1) The proof of [[lem:iii-c-4-2]] gives the slots of S̄h in terms of those of h; their coefficients are
[[eq:s17-abar]]. In spatial dimension n the same calculation applies with ⅔ replaced by 2/(n − 1) in Ē^C, with the
coordinate s := tr̸h/(n − 1) of the third slot, and with tr h = −4h₀₁ + (n − 1)s; the formula for Ē^ΥḠ is the same in
every dimension, by the calculation that gives [[eq:iii-b-6-5]] (the trace weight 2/(n − 1) is chosen for this). Then
ω₁ = −((n − 1)/2)s, the factor 1 − ⅔(1 − e_C) of slot 4 becomes (n − 3 + 2e_C)/(n − 1), and the calculation gives the
same diagonal, Ā₅₂ and Ā₇₄, and

    Ā₃₁ = (4/(n − 1))(1 − e_C)(1 + v_C)γ_C,         Ā₄₁ = ((n − 3 + 2e_C)/(n − 1))(1 + v_C)γ_C + γ_Υ,
    Ā₄₃ = ((n − 3 + 2e_C)(1 − v_C)γ_C + (n − 1)e_Υγ_Υ)/4,         Ā₇₃ = ((n − 1)/2)((1 + v_C)γ_C + e_Υγ_Υ).

At n = 4 these are [[eq:s17-abar]]; at n = 3, where 2/(n − 1) = 1 and s = ½tr̸h, they are the values stated, which are
those printed in [Hin26, (5.28)] at h = 0.

(2) A symmetric 2-tensor of scalar type given by S ∈ 𝒮_l has its slots 1, 3, 4, 7 multiples of S, its slots 2, 5
multiples of dS and its slot 6 a multiple of δ̸*₀dS; one of vector type given by V ∈ 𝒱_l has its slots 2, 5 multiples
of V and its slot 6 a multiple of δ̸*V; one of tensor type given by T ∈ 𝒯_l has only its slot 6, a multiple of T
([[def:iii-a1-1-3]], and the list [[eq:iii-a1-2-10]], whose splitting differs from [[eq:iii-c-1-6]] only by changes of
frame within the scalar and within the vector components). For S ∈ 𝒮_0, dS = 0; for V ∈ 𝒱_1, δ̸*V = 0
([[eq:iii-a1-1-3]]); and for 0 ≠ V ∈ 𝒱_2, δ̸*V ≠ 0, as δ̸δ̸*V = (5/2)V ([[eq:iii-a1-1-2]] with ν = 3, k² = 8). This
gives the sets J_τ, with one dimension per slot. By the proof of [[lem:iii-c-4-2]] the entries of Ā act between scalar
slots and between vector slots as scalars, and the off-diagonal entries of [[eq:s17-abar]] connect slots within
{1, 3, 4, 7} or within {2, 5}; row and column 6 of Ā vanish off the diagonal. So Ā maps the type-τ tensors given by Y to
themselves, by its submatrix on J_τ, which is lower triangular, and the determinant of −2(x − λ)(x − 3/2 − Ā) there is
the product of its diagonal entries; the diagonal is [[eq:iii-c-4-3]]. The display in (2) is [[eq:iii-g3-1-1]] applied
to v^xφ: (v∂_v − λ)v^x = (x − λ)v^x, S̄ does not depend on v, and L̃(0)(ω, v∂_v, ∂_ω)v^xφ = v^xL̃(0)(ω, x, ∂_ω)φ.

(3) This is [[prop:iii-c-4-4]] with [[lem:iii-c-3-2]] (b)–(c), [[rem:iii-c-4-5]], the calculation of the leading part in
the proof of [[prop:iii-c-5-2]], [[def:iii-c-5-1]] and [[rem:s17-no-radiation]].

(4) The first statement is [[lem:iii-g1-4-2]] (a). As γ_Υ < ¼, every radiative exponent is at most 3/2 + 2γ_Υ < 2. An
element of Res_(ι⁺)(L̄, λ) is a residue at λ of t_*^(−z) times the inverse of [[thm:iii-g1-3-1]] applied to a
polynomial ([[def:iii-g3-3-6]]), and that inverse is holomorphic off spec_(ι⁺)(L̄); so Res_(ι⁺)(L̄, λ) = {0} for
Re λ < 2.

*No outgoing solution.* Let h and λ be as in (4). By [[lem:iii-g1-1-1]], Π_s commutes with v∂_v and with S̄, and
S̄Π_s = sΠ_s. Near v = 0, by [[eq:iii-g1-1-5]], Π_sh (s ∈ σ_Υ) is a term v^(3/2+s)c_s(ω) with Π_sc_s = c_s, plus terms
with exponents in ℰ^C_(ι⁺,ℐ) and a remainder of weight ℓ_I, and Π_Ch has only terms of the latter two kinds. As
(v∂_v − 3/2 − S̄)(v^(3/2+s)c_s) = v^(3/2+s)(s − S̄)c_s = 0, the section

    f := 2v(v∂_v − 3/2 − S̄)h

has near v = 0 only exponents in ℰ^C_(ι⁺,ℐ) + 1, of real part at least 7/2, and a remainder of weight ℓ_I + 1. Near
R = 0, h ∈ H^(∞,β)_b for every β < min(0, ℓ_K), as ℰ_K ⊂ {Re ≥ 0} ([[lem:iii-g1-1-3]] (b)); fix
β ∈ (−1, min(0, ℓ_K)). As 2v(v∂_v − 3/2 − S̄) ∈ R⁻¹Diff¹_b there, f ∈ H^(∞,β−2)_b near R = 0. Fix
ℓ′ ∈ (Re λ, min(ℓ_I, 2)) with ℓ′ ∉ Re π₁ℰ^tot_(ι⁺,ℐ). Then f ∈ H^(∞,ℓ′+1,β−2)_b(ι⁺), and by [[thm:iii-g1-3-1]] (2),
with ℓ′ and β in place of ℓ_I and ℓ_K, and [[lem:iii-g1-4-2]] (a)–(b), F(z) := N_(ι⁺)(z)⁻¹f, with the inverse
[[eq:iii-g1-3-3]], is holomorphic on the half plane {Re z < ℓ′}, which contains λ. As N_(ι⁺) is linear in its parameter,
with ∂_λN_(ι⁺) = 2v(v∂_v − 3/2 − S̄),

    N_(ι⁺)(z)h = N_(ι⁺)(λ)h + (z − λ)f = (z − λ)f.

Let Re z < min(3/2, ℓ′) and ℓ″ ∈ (Re z, min(3/2, ℓ′)). By [[lem:iii-g3-1-2]] (2), h ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),β)_b(ι⁺),
its exponents at v = 0 have real part at least 3/2, and (z − λ)f ∈ H^(∞,ℓ″+1,β−2)_b; so [[lem:iii-g3-2-3]] (with
w₀ = 3/2 and ℓ″ for its ℓ′) gives h = N_(ι⁺)(z)⁻¹N_(ι⁺)(z)h = (z − λ)F(z). Here the inverses of
[[thm:iii-g1-3-1]] (2) for ℓ″ and for ℓ′ agree on H^(∞,ℓ′+1,β−2)_b, as both extend [[eq:iii-g1-3-1]] by continuity
from the dense subspace Ċ^∞(ι⁺). Both sides of h = (z − λ)F(z) are holomorphic on {Re z < ℓ′}, so the identity holds
there, and at z = λ it gives h = 0.

*The poles.* By [[prop:iii-g3-2-4]] the poles of [[eq:iii-g3-2-2]] lie in spec_(ι⁺)(L̄) ∪ π₁ℰ^C_(I,♯), and
π₁ℰ^C_(I,♯) = {λ_♯} ∪ π₁ℰ_I^C with min Re ℰ_I^C > 3/2 + 2γ_Υ ([[def:iii-c-3-1]] (2)). So the only possible pole with
real part at most 3/2 + 2γ_Υ is λ_♯. When λ_♯ < ℓ_I it is a simple pole by [[cor:iii-g3-2-6]], excited only by the
exceptional term by [[rem:iii-g3-3-8]]. When ℓ_I ≤ λ_♯ it does not lie in {Re λ < ℓ_I}, where [[eq:iii-g3-2-2]] is
defined, and there is no pole with real part at most 3/2 + 2γ_Υ. As 0 < e_Υ < 1, λ_♯ differs from 3/2, 3/2 + γ_Υ and
3/2 + 2γ_Υ. ∎

In dimension 3 + 1 the radiative order and the Coulombic order of the mass coincide, both at 1, and the incoming pole
of [Hin26, (9.49)] at 1 records both. In dimension 4 + 1 the radiation fields sit at 3/2 + σ_Υ and the mass at 2, and
the only incoming pole below 3/2 + 2γ_Υ is λ_♯ (when λ_♯ < ℓ_I), which requires the exceptional term of
[[rem:s17-exceptional]].

### Setting at the transition face {#sec:iii-g4-1}

The remaining sections are [Hin26, Section 9.2] in dimension 4 + 1. As there, only infinite b-regularity is stated;
finite b-regularity loses fixed amounts.

*Two constants.* ε_ind ∈ (0, 1] is the constant of [[eq:iii-f1-2-2]], the counterpart of [Hin26, (8.13)]:
d(Re μ, ℤ) ≥ ε_ind for every non-integer root μ of L̂_b(0) with |μ| ≤ 50. It enters the windows [[eq:iii-g4-3-1]] and
[[eq:iii-g4-4-2]] and that of [[prop:iii-g4-5-1]], and the separation of roots and poles in the proof of
[[lem:iii-g4-3-4]]. ε_Υ ∈ (0, ½) is the constant of [[sec:iii-d2-1]], fixed by the indicial roots of □^Υ_b alone, and
ℰ_ind denotes, as there, an index set with min Re ℰ_ind ≥ ε_Υ. It bounds the corrections of the states, and so the
gains at tf in [[prop:iii-g4-4-4]] and [[prop:iii-g4-5-1]]. The two constants are different.

Against [Hin26], dimension 4 + 1 changes the following. (a) The tf-normal operator carries −r̂∂_r̂ − 3/2 − S̄ in its
first-order part, and its inverse is [[cor:iii-f1-3-4]], with the sctf weight below 3/2 (1 in [Hin26]) and the ztf
weight in [−1, 0) ((−ε_ind, 0) in [Hin26]). (b) The expansion at r̂ = 0 runs over
the window (−3, 0] of the table of [[sec:iii-g2-1]], with its states and their companions: the class roots are
2 − λ^Υ_(sl,l+j) with l + j ≤ 4, the physical roots at −2 include the tensor type t2, and no root at −3 enters. (c) So
the window w₀ < ℓ_K^max ≤ 3 ([[sec:iii-g4-3]]) replaces 3 + ε_ind of [Hin26]. (d) The spectral family differs from the
tf model by ρ_scf²ρ_tf⁴Diff²_b ([[lem:iii-g4-1-2]]), where [Hin26] has ρ_tf³, as the mass enters at ρ². (e) Three
points of [Hin26] are corrected: [Hin26, (9.59)] prints ρ^(−λ−j) for ρ^(−λ+j) ([[def:iii-g4-2-1]]); the operator of
[Hin26, (9.58)] is the one of 2L̄, not of L̄ ([[lem:iii-g4-1-1]] (3)); and the first step of the proof of [Hin26,
Proposition 9.35] needs a dilation-invariant inverse in place of a pointwise one ([[prop:iii-g4-5-1]]).

*The space.* For σ ∈ ±[0, 1], X^±_(sc-b) := [±[0, 1]_σ × X̄; {0} × ∂X̄], with faces scf, tf, zf and the defining
functions of [[eq:ii-g1-3-2]],

    ρ_scf = ρ/(ρ + |σ|),     ρ_tf = ρ + |σ|,     ρ_zf = |σ|/(ρ + |σ|),                                   {#eq:iii-g4-1-1}

ρ = r⁻¹ near ∂X̄ = 𝕊³, X the spatial slice of [[sec:iii-b-2]]. All spaces on X^±_(sc-b) are b-Sobolev and partially
polyhomogeneous spaces for a b-density (|dσ/σ| times a b-density on X; [[sec:iii-a-1]], [Hin26, Definitions 2.6–2.8]),
with orders listed for scf, tf, zf. Let r̂ := |σ|r = |σ|/ρ. Then tf = [0, ∞]_r̂ × 𝕊³ with faces
ztf = {r̂ = 0} = tf ∩ zf and sctf = {r̂ = ∞} = tf ∩ scf, ρ_sctf := (1 + r̂)⁻¹, ρ_ztf := r̂/(1 + r̂), the b-density
|(dr̂/r̂)dg̸| and H^(k,a,c)_b(tf) := ρ_sctf^a ρ_ztf^c H^k_b(tf) ([[sec:i-c-4-1]]; [[cor:iii-f1-3-4]]). On {ρ < ρ₀} the
functions (σ, r̂, ω) are coordinates, in which ρ_scf = ρ_sctf and ρ_zf = ρ_ztf are functions of r̂ alone,
|σ| = ρ_tf ρ_zf, and the b-vector fields are spanned by σ∂_σ|_r̂, r̂∂_r̂|_σ and ∂_ω (from
σ∂_σ|_x = σ∂_σ|_r̂ + r̂∂_r̂ and ρ∂_ρ|_σ = −r̂∂_r̂). Near tf ∩ zf also (ρ, r̂, ω) are coordinates, with ρ_tf ∼ ρ and
ρ_zf ∼ r̂. Fix χ₁ ∈ C^∞([0, ∞)) equal to 1 on [0, 1/8] and 0 on [1/4, ∞), χ_zf := χ₁(r̂) (1 near zf, 0 near scf; as in
[[ch:s10]]), χ_ztf := χ_zf|_tf, and χ_tf := χ₂(ρ + |σ|) with χ₂ ∈ C_c^∞([0, ½ρ₀)) equal to 1 near 0.

*The operator.* L_b is the linearised gauge-fixed Einstein operator of [[ch:s15]], with the parameters and hypotheses of
[[sec:iii-g2-1]]; in particular z_Υ ∉ Z_exc, so that every indicial root of L̂_b(0) is simple ([[prop:iii-f1-2-3]] (e)).
With (ℱu)(σ) = ∫ e^(iσt_*)u dt_* ([[eq:iii-a-2-2]]), so that ∂_(t_*) becomes −iσ, [[lem:iii-f-2-1]] (2) gives exactly

    L̄̂(σ) = iσρ(ρ∂_ρ − 3/2 − S̄) + ρ²𝒩,     𝒩 := ρ⁻²L̄̂(0),                                         {#eq:iii-g4-1-2}

where L̄̂(σ) denotes the spectral family of L̄, 𝒩 is a dilation-invariant b-operator in (ρ∂_ρ, ∂_ω)
([[sec:iii-f1-1]]) and S̄ a bundle endomorphism depending on ω alone. Write 𝒩(λ) for its indicial family,
𝒩(ρ^λφ) = ρ^λ𝒩(λ)φ; its roots are the indicial roots of L̂_b(0) ([[prop:iii-f1-2-3]]). For ±σ > 0 the tf-normal
operator is

    N_tf := N_tf(L̂_b, ±1) = r̂⁻²N₀ + r̂⁻¹N₁,     N₀ := 𝒩(−r̂∂_r̂),     N₁ := ±i(−r̂∂_r̂ − 3/2 − S̄),    {#eq:iii-g4-1-3}

on sections over tf of π_tf^*(S²T*X|_(∂X)); P := r̂²N_tf = N₀ + r̂N₁ is a b-operator at ztf.

**Lemma {#lem:iii-g4-1-1}** (The tf model.) (1) For σ = ±|σ| ≠ 0, L̄̂(σ) = |σ|²N_tf on {ρ < ρ₀}, in the coordinates
(σ, r̂, ω) (with N_tf acting at fixed σ). (2) N₀(r̂^zφ) = r̂^z𝒩(−z)φ. So the Mellin family of N₀ (with
û(λ) := ∫ r̂^(−λ)u dr̂/r̂) is N₀(λ) = 𝒩(−λ), its roots are −μ for the roots μ of L̂_b(0), and at each −μ the inverse
N₀(λ)⁻¹ has a simple pole whose residue Π_μ has range ker 𝒩(μ). (3) N_tf(2L̂_b, ±1) = 2N_tf ([[eq:i-c-4-1]]).

*Proof.* (1) Both sides are b-operators in (ρ∂_ρ, ∂_ω) whose coefficients depend on ω alone, so it suffices to compare
them on ρ^aφ(ω), a ∈ ℂ. By [[eq:iii-g4-1-2]], L̄̂(σ)(ρ^aφ) = iσρ^(a+1)(a − 3/2 − S̄)φ + ρ^(a+2)𝒩(a)φ, and with
ρ = |σ|r̂⁻¹, iσ = ±i|σ|, this is |σ|^(a+2)(±i r̂^(−a−1)(a − 3/2 − S̄) + r̂^(−a−2)𝒩(a))φ. And
|σ|²N_tf(|σ|^a r̂^(−a)φ) is the same, as −r̂∂_r̂ r̂^(−a) = a r̂^(−a).

(2) The first statement is the definition. The roots are simple, so on each isotypic component (type and harmonic) the
determinant of the matrix polynomial 𝒩(λ) has a simple zero at μ, and 𝒩(λ)⁻¹ = adj 𝒩(λ)/det 𝒩(λ) has a simple pole
with residue adj 𝒩(μ)/(det 𝒩)′(μ). Its range lies in ker 𝒩(μ), as 𝒩(μ) adj 𝒩(μ) = 0, and it is non-zero, as the
kernel is one-dimensional, so adj 𝒩(μ) ≠ 0; hence its range is the kernel. Only finitely many components have μ as a
root ([[prop:iii-f1-2-3]] (f)). Then Π_μ = −res_(x=μ)𝒩(x)⁻¹.

(3) [[eq:i-c-4-1]] at σ̂ = ±1 for the spectral family of 2L_b, with S₀ = S̄ and N(P⁽⁰⁾) = 2𝒩. ∎

**Lemma {#lem:iii-g4-1-2}** ([Hin26, (8.2b), (8.4), (8.15)] in dimension 4 + 1.) On {ρ < ρ₀},
L̂_b(σ) ∈ ρ_scf ρ_tf² Diff²_b(X^±_(sc-b)) and L̂_b(σ) − L̄̂(σ) ∈ ρ_scf² ρ_tf⁴ Diff²_b(X^±_(sc-b)). On all of X,
L̂_b(σ) is a differential operator polynomial in σ (of degree 2) with smooth stationary coefficients.

*Proof.* ρ∂_ρ at fixed σ and ∂_ω lift to b-vector fields (see *The space* above), and smooth functions of (ρ, ω) to
smooth functions. In [[eq:iii-g4-1-2]], σρ = ρ_scf ρ_tf² ρ_zf (up to sign) and ρ² = ρ_scf²ρ_tf². By
[[lem:iii-f-2-1]] (3), 2(L_b − L̄) = −g_b^(00)∂²_(t_*) + Q_b∂_(t_*) + R_b with g_b^(00) ∈ ρ²C^∞, Q_b ∈ ρ³Diff¹_b,
R_b ∈ ρ⁴Diff²_b, so 2(L̂_b(σ) − L̄̂(σ)) = σ²g_b^(00) − iσQ_b + R_b, and σ²ρ², σρ³, ρ⁴ are ρ_scf²ρ_tf⁴ times
ρ_zf², ρ_scf ρ_zf, ρ_scf². The last statement is [[lem:iii-f-2-1]] (1). ∎

*The window and the states.* For w < ℓ_K^max ([[eq:iii-g2-1-1]]) let 𝒲(w) be the set of roots μ of L̂_b(0) with
−w < μ ≤ 0 (all real, [[lem:iii-g1-1-3]] (c)); they and their states are those of the table of [[sec:iii-g2-1]]. For
μ ∈ 𝒲 at a type τ (harmonics 𝒴_τ) the tower (h̆^((μ),j)_(b,τ)(Y))_(j≤K_μ) of the table has the Minkowski leading terms
h̆̄^((μ),j)_τ(Y) = ρ^(μ−j)φ^((μ,τ))_j(ω; Y) ([[sec:iii-g2-2-2]]), and Y ↦ φ^((μ,τ))_0(Y) maps 𝒴_τ isomorphically onto
the type-τ part of ker 𝒩(μ) ([[lem:iii-g2-1-2]]). For the types s1 and v1 at μ = −1 we re-index, with
φ^((−1,s1))_j := (ρ^(1+j)h̆̄^(j+2)_(s1))|_(∂X) and φ^((−1,v1))_j := (ρ^(1+j)h̆̄^(j+1)_(v1))|_(∂X), j ≥ 0; these chains
then satisfy [[eq:iii-g2-2-4]] as the generic ones do with μ = −1 ([[lem:iii-g2-2-2]]). Let

    c_μ := 2 − ⌊−μ⌋,     {−μ} := −μ − ⌊−μ⌋.                                                             {#eq:iii-g4-1-4}

So c_μ = 2 + μ at the integer roots, and c_μ = 2, 1, 0 at the class roots in (−¼, 0), (−5/4, −1), (−9/4, −2); these
are the numbers k_μ of the table of [[sec:iii-g2-1]] (for s1 and v1, c₋₁ + 2 = 3 and c₋₁ + 1 = 2), so c_μ ≤ K_μ,
resp. c₋₁ + 2 ≤ 4 and c₋₁ + 1 ≤ 3. And ⌊−μ⌋ + c_μ + 1 = 3. The fractional part {−μ} is 0 at the integer roots. At a
class root μ = 2 − λ^Υ_(sl,l+j), −μ ∈ (l + j − 2, l + j − 7/4) (the ranges of [[lem:iii-d-4-1]], as [[sec:iii-g2-1]]
uses them; (0, z_Υ/3] for (l, l + j) = (0, 2)), so {−μ} ∈ (0, ¼), and {−μ} ≥ ε_ind by [[eq:iii-f1-2-2]].

### Formal solutions at ztf {#sec:iii-g4-2}

This section is [Hin26, (9.57)–(9.61) and Definition 9.25] in dimension 4 + 1.

**Definition {#def:iii-g4-2-1}** (Formal solutions at ztf.) For μ ∈ 𝒲, a type τ at which μ is a root, Y ∈ 𝒴_τ and k ≤
K_μ (resp. K − 2, K − 1 for s1, v1),

    h̄^((μ),≤k)_τ(±r̂, Y) := Σ_(j=0)^k (∓ir̂)^j r̂^(−μ) φ^((μ,τ))_j(ω; Y),                               {#eq:iii-g4-2-1}

a function on tf with values in π_tf^*(S²T*X|_(∂X)), and H_(μ,τ)(Y) := h̄^((μ),≤c_μ)_τ(±r̂, Y). For s1 and v1 these
are, in the indexing of [Hin26],
h̄^(≤3)_(s1)(±r̂, S) = Σ_(j=0)^1 (∓ir̂)^j r̂ (ρ^(1+j)h̆̄^(2+j)_(s1)(S))|_(∂X) and
h̄^(≤2)_(v1)(±r̂, V) = Σ_(j=0)^1 (∓ir̂)^j r̂ (ρ^(1+j)h̆̄^(1+j)_(v1)(V))|_(∂X).

[Hin26, (9.59)] prints ρ^(−λ−j)h̄^((λ),j); the companions have degree λ − j ([Hin26, (9.37) and (9.57)], where
ρ^j h̆̄^((0),j) appears), so the restriction to ∂X needs ρ^(−λ+j).

**Lemma {#lem:iii-g4-2-2}** ([Hin26, (9.57), (9.60)] in dimension 4 + 1.) (1) For σ = ±|σ| ≠ 0 and r̂ = |σ|r,
Σ_(j=0)^k (−iσ)^j h̆̄^((μ),j)_τ(Y) = |σ|^μ h̄^((μ),≤k)_τ(±r̂, Y), with the re-indexed chains for s1 and v1. (2) Exactly,

    N_tf h̄^((μ),≤k)_τ(±r̂, Y) = (∓i)^(k+1) r̂^(k−1−μ) ψ^((μ,τ))_k(ω; Y),
    ψ_k := −(μ − k − 3/2 − S̄)φ_k.                                                                      {#eq:iii-g4-2-2}

In particular PH_(μ,τ)(Y) = (∓i)^(c_μ+1) r̂^(3+{−μ}) ψ_(c_μ), as c_μ + 1 − μ = 3 + {−μ}.

*Proof.* (1) (−iσ)^jρ^(μ−j) = (∓i)^j|σ|^jρ^(μ−j) = (∓i)^j|σ|^μ r̂^(j−μ).

(2) By [[lem:iii-g2-2-4]] (a) with a = e^(−iσt_*),
L̄(e^(−iσt_*) Σ_(j≤k) (−iσ)^j h̆̄^j) = (−iσ)^(k+1)e^(−iσt_*)[L̄, t_*]h̆̄^k, and [L̄, t_*] = −ρ(ρ∂_ρ − 3/2 − S̄)
([[sec:iii-g2-2-1]], after [[eq:iii-g2-2-3]]) gives [L̄, t_*](ρ^(μ−k)φ_k) = ρ^(μ−k+1)ψ_k. So by (1),
L̄̂(σ)(|σ|^μ h̄^(≤k)) = (−iσ)^(k+1)ρ^(μ−k+1)ψ_k = (∓i)^(k+1)|σ|^(μ+2) r̂^(k−1−μ)ψ_k, and [[lem:iii-g4-1-1]] (1) divides
by |σ|^(μ+2). For s1 and v1, [[lem:iii-g2-2-4]] (a) is stated with a^((k−1)) and a^((k)) in the indexing of [Hin26],
which is the same statement after the re-indexing. ∎

[[eq:iii-g4-2-2]] is an identity; [Hin26, (9.60)] records the membership in r̂^(−λ+k−1)C^∞. It is exact because L̄ is
homogeneous and the chains are those of Minkowski space.

**Definition {#def:iii-g4-2-3}** ([Hin26, (9.61)].) l_β(r̂) := (r̂^β − 1)/β for β ≠ 0, and l₀(r̂) := log r̂.

**Lemma {#lem:iii-g4-2-4}** (The functions l_β.) (1) [r̂∂_r̂, l_β(r̂)] = r̂^β. For a polynomial p of degree d with
coefficients in Diff(𝕊³),
[p(r̂∂_r̂), l_β] = r̂^β q_β(r̂∂_r̂), with q_β of degree d − 1 and coefficients polynomial in β. (2) For C₀ ∈ ℝ and
χ ∈ C_c^∞([0, 1)), β ↦ χl_β is holomorphic on {Re β > C₀} with values in H^(∞,c)_b([0, 1)_r̂) for every
c < min(0, C₀), including at β = 0. (3) For t > 0, l_β(r̂) − l_β(t) = t^β l_β(r̂/t). (4) (r̂^z − r̂^m)/(z − m) =
r̂^m l_(z−m)(r̂).

*Proof.* (1) r̂∂_r̂ l_β = r̂^β for every β. With D := r̂∂_r̂, D(l_β g) = l_β Dg + r̂^β g and D(r̂^β g) = r̂^β(D + β)g, so
by induction D^m(l_β g) = l_β D^m g + r̂^β Σ_(i<m) (D + β)^(m−1−i)D^i g.

(2) l_β(r̂) = log r̂ ∫₀¹ r̂^(sβ) ds is entire in β for r̂ > 0, and |r̂^(sβ)| ≤ r̂^(min(0,Re β)) for r̂ ≤ 1, s ∈ [0, 1].
Differentiating under the integral, |∂_β^p l_β| ≤ C_p|log r̂|^(p+1) r̂^(min(0,Re β)), and for m ≥ 1,
D^m l_β = β^(m−1)r̂^β, whose β-derivatives are bounded by C|log r̂|^p r̂^(Re β)(1 + |β|)^m. These bounds are locally
uniform on {Re β > C₀}, and χ|log r̂|^N r̂^(min(0,C₀)) ∈ H^(0,c)_b for c < min(0, C₀); so difference quotients
converge in H^(∞,c)_b by dominated convergence.

(3) l_β(r̂) − l_β(t) = (r̂^β − t^β)/β = t^β((r̂/t)^β − 1)/β, and likewise for β = 0. (4) r̂^m(r̂^(z−m) − 1)/(z − m). ∎

The coefficients ±β⁻¹ of r̂^β and r̂⁰ in l_β have a pole at β = 0, while l_β itself, as a conormal function, does not:
this is why the expansions below are written with l_β.

### The expansion at r̂ = 0 {#sec:iii-g4-3}

This section is [Hin26, Lemma 9.26 and Remarks 9.27–9.28] in dimension 4 + 1.

*Hypotheses.* Let α₀ ∈ ℂ and ℓ_scf, ℓ_zf ∈ ℝ with

    Re α₀ ∈ (1, 2 + ε_ind),     ℓ_scf < 3/2,     w₀ := ℓ_zf − Re α₀ + 2 ∈ (−ε_ind, ℓ_K^max),
    ℓ_zf ∉ ℕ₀,     w₀ ≠ −μ                                                                              {#eq:iii-g4-3-1}

for every root μ of L̂_b(0), with ε_ind of [[eq:iii-f1-2-2]]. No upper bound on ℓ_zf is needed
([[lem:iii-g4-3-3]]). The condition ℓ_zf ∉ ℕ₀ keeps a Taylor term r̂^(2−α+ℓ_zf) of the smooth remainders below off the
last contour of [[lem:iii-g4-3-4]]. A use at an integer ℓ_zf takes ℓ_zf − δ in its place, or first removes the term with
j = ℓ_zf as a term of type (ii) of the proof of [[lem:iii-g4-3-4]]. For α near α₀ put w(α) := ℓ_zf − Re α + 2 and

    β_μ(α) := 2 − α − {−μ},     z_j(α) := 2 − α + j,     j ∈ ℕ₀,                                         {#eq:iii-g4-3-2}

so that z_(⌊−μ⌋)(α) + μ = β_μ(α).

*Holomorphic families.* For a disc D around α₀, a family a(α) ∈ H^(∞,((0,0),ℓ))_b([0, 1)_r̂ × 𝕊³) is holomorphic if
a = Σ_(j<ℓ) χ_ztf r̂^j a_j(α) + a′(α) with a_j holomorphic in C^∞(𝕊³) and a′ holomorphic in H^(∞,ℓ)_b. Here and below
the spaces on [0, 1)_r̂ × 𝕊³ impose their conditions near r̂ = 0 only: u belongs if u ∈ H^∞_loc on (0, 1) × 𝕊³ and χu
belongs to the b-space for one, hence every, χ ∈ C_c^∞([0, 1)) equal to 1 near 0; so functions smooth on (0, 1) and
vanishing near 0 lie in all of them. Let 𝔉_D be the space of r̂^(2−α)a(α) with a such a family for ℓ = ℓ_zf.

**Theorem {#thm:iii-g4-3-1}** ([Hin26, Lemma 9.26] in dimension 4 + 1.) Assume [[eq:iii-g4-3-1]]. Let
f₀ ∈ H^(∞,ℓ_scf+1,((0,0),ℓ_zf))_b(tf) and, for α near α₀, u_α := N_tf⁻¹(ρ_ztf^(−α)f₀) by [[cor:iii-f1-3-4]], with
β_sctf = ℓ_scf and β_ztf ∈ (−1, min(0, 2 − Re α₀, w₀)). Then u_α does not depend on the choice of β_ztf, is
holomorphic in α with values in H^(∞,ℓ_scf−ε,β_ztf)_b(tf) for every ε > 0, and

    u_α = χ_ztf(u_(α,0) + r̂^(2−α)u_(α,1)) + (1 − χ_ztf)u_(α,∞),                                         {#eq:iii-g4-3-3}

where u_(α,∞) ∈ H^(∞,ℓ_scf−ε,0)_b(tf) and u_(α,1) ∈ H^(∞,0,((0,0),ℓ_zf))_b(tf) are holomorphic in α near α₀ (the
latter in the sense above, its remainder at exactly ℓ_zf for every α), and

    u_(α,0) = Σ_(μ∈𝒲(w₀)) Σ_τ l_(β_μ(α))(r̂) H_(μ,τ)(Y^((μ))_τ(α))                                       {#eq:iii-g4-3-4}

with Y^((μ))_τ(α) ∈ 𝒴_τ holomorphic in α. Written out, with the terms with −μ ≥ w₀ omitted, [[eq:iii-g4-3-4]] is

    u_(α,0) = l_(2−α)(r̂)(h̄^(≤3)_(s1)(±r̂, S^((−1))_1) + h̄^(≤2)_(v1)(±r̂, V^((−1))_1)
                        + h̄^((0),≤2)_(s0)(±r̂, S^((0))_0) + h̄^((0),≤2)_(s2)(±r̂, S^((0))_2)
                        + h̄^((−1),≤1)_(s3)(±r̂, S^((−1))_3) + h̄^((−1),≤1)_(v2)(±r̂, V^((−1))_2)
                        + h̄^((−2))_(s4)(±r̂, S^((−2))_4) + h̄^((−2))_(v3)(±r̂, V^((−2))_3)
                        + h̄^((−2))_(s2,ph)(±r̂, S^((−2))_2) + h̄^((−2))_(v2,ph)(±r̂, V^((−2))_2)
                        + h̄^((−2))_(t2)(±r̂, T^((−2))_2))
              + Σ_((l,l+j)) l_(2−α−{λ^Υ_(sl,l+j)})(r̂) h̄^((2−λ^Υ_(sl,l+j)),≤c)_(sl)(±r̂, S_(l,l+j)),    {#eq:iii-g4-3-5}

the last sum over (l, l + j) ∈ {(0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)} with c = 2, 2, 1, 1, 0, 0; "ph" marks
the physical states of [[prop:iii-f4-5-1]], and the other terms at 0, −1, −2 are the states of □^Υ and the boosts and
rotations of the table of [[sec:iii-g2-1]].

The proof uses three lemmas, with P = N₀ + r̂N₁ of [[eq:iii-g4-1-3]].

**Lemma {#lem:iii-g4-3-2}** (The class 𝔉_D.) P maps 𝔉_D into 𝔉_D.

*Proof.* P(r̂^z a) = r̂^z P_z a with P_z := r̂^(−z)Pr̂^z, a b-operator with smooth coefficients polynomial in z, and
b-operators with smooth coefficients preserve H^(∞,((0,0),ℓ))_b with holomorphic dependence (property (F1) of
[[sec:iii-a-1]]; the coefficient maps are polynomial in z = 2 − α). ∎

**Lemma {#lem:iii-g4-3-3}** (The formal terms.) Let μ ∈ 𝒲(w₀), τ a type at which μ is a root and Y(α) holomorphic.
Then P(l_(β_μ(α))H_(μ,τ)(Y(α))) ∈ 𝔉_D for a small disc D.

*Proof.* P(l_βH) = l_βPH + [P, l_β]H. By [[lem:iii-g4-2-2]] (2), l_βPH = (∓i)^(c_μ+1)l_β r̂^(3+{−μ})ψ_(c_μ).

*If Re α₀ ≤ 2,* then ℓ_zf = w₀ + Re α₀ − 2 ≤ w₀ < ℓ_K^max ≤ 3, and by [[lem:iii-g4-2-4]] (2) this term is holomorphic
in H^(∞,c)_b for every c < 3 + {−μ} + min(0, Re β_μ) = min(3 + {−μ}, 5 − Re α). Both exceed w(α) for D small, as
w(α) < 3 and 5 − Re α − w(α) = 3 − ℓ_zf > 0; so for D small this term is r̂^(2−α) times a holomorphic family in
H^(∞,ℓ_zf+δ)_b, δ > 0.

*If Re α₀ > 2,* then Re β_μ(α₀) = 2 − Re α₀ − {−μ} < 0, so β := β_μ is bounded away from 0 on a small D and
l_β = β⁻¹(r̂^β − 1); as β + 3 + {−μ} = 5 − α,
l_β r̂^(3+{−μ})ψ = β⁻¹r̂^(2−α)r̂³ψ − β⁻¹r̂^(2−α)r̂^(1+α+{−μ})ψ. The first is r̂^(2−α) times a holomorphic smooth term (a
coefficient a₃ if ℓ_zf > 3, part of a′ if ℓ_zf < 3), the second r̂^(2−α) times a holomorphic family in H^(∞,ℓ_zf+δ)_b,
as 1 + Re α + {−μ} − ℓ_zf = 3 + {−μ} − w(α) > 0; both lie in 𝔉_D. (This is the split of the proof of [Hin26, Lemma
9.26], its Case 1.)

By [[lem:iii-g4-2-4]] (1), [P, l_β] = r̂^β Q_β with Q_β a b-operator of order 1 polynomial in β, and
H ∈ r̂^(−μ)C^∞([0, 1) × 𝕊³) is a polynomial in r̂; so [P, l_β]H ∈ r̂^(β_μ−μ)C^∞ = r̂^(2−α+⌊−μ⌋)C^∞, holomorphically,
which lies in 𝔉_D as ⌊−μ⌋ ∈ ℕ₀. ∎

**Lemma {#lem:iii-g4-3-4}** (One step.) Let b ∈ (−1, w₀), with b not the real part of a root −μ or of a z_j(α₀), and
b + 1 ≠ w₀. Let R(α) ∈ H^(∞,b)_b([0, 1) × 𝕊³) be holomorphic on a disc D, with PR ∈ 𝔉_D. Let b̃ := min(w₀, b + 1),
decreased slightly when b̃ < w₀ so that it is not the real part of a root or of a z_j(α₀). Then, after shrinking D,

    R = Σ_(μ: b<−μ<b̃) Σ_τ l_(β_μ)H_(μ,τ)(Y_(μ,τ)) + U + R̃,                                             {#eq:iii-g4-3-6}

with Y_(μ,τ)(α) holomorphic, U ∈ 𝔉_D, and R̃ holomorphic in H^(∞,b̃)_b. If b̃ = w₀, the remainder may be taken with
r̂^(α−2)R̃ holomorphic in H^(∞,ℓ_zf)_b.

*Proof.* We use the Mellin transform ℳ and the contour shift exactly as in the proof of [[lem:iii-a-1-4]], with the
facts (M1)–(M2) on the Mellin transforms of b-Sobolev and polyhomogeneous functions and (E1)–(E2) on the inverse of an
elliptic indicial family of [[sec:iii-a-1-1]] (P is elliptic, [[sec:i-c-4-1]]); all bounds there are locally uniform in
the holomorphic parameter α. Fix χ ∈ C_c^∞([0, 1)) equal to 1 near 0; then (1 − χ)R vanishes near 0 and is smooth, and
P(χR) = χPR + [P, χ]R ∈ 𝔉_D, so we may replace R by χR, supported in [0, 1), and put (1 − χ)R into R̃ at the end. Write
PR = r̂^(2−α)(Σ_(j<ℓ_zf) χ_ztf r̂^j a_j + a′). Since ∫ r̂^(−ζ)χ_ztf dr̂/r̂ = ζ⁻¹∫ r̂^(−ζ)χ′_ztf dr̂ = −ζ⁻¹ + (entire),

    ℳ(PR)(λ) = −Σ_j a_j(α)/(λ − z_j(α)) + G(λ),                                                       {#eq:iii-g4-3-7}

with G holomorphic in {Re λ < w(α)} (G collects the entire parts and ℳ(r̂^(2−α)a′)(λ) = (ℳa′)(λ + α − 2)). From
N₀R = PR − r̂N₁R and ℳ(r̂N₁R)(λ) = N₁(λ − 1)ℳR(λ − 1), with N₁(λ) = ±i(−λ − 3/2 − S̄) and ℳR holomorphic in
{Re λ < b} (M1),

    ℳR(λ) = N₀(λ)⁻¹Φ(λ),     Φ(λ) := ℳ(PR)(λ) − N₁(λ − 1)ℳR(λ − 1),                                   {#eq:iii-g4-3-8}

continues ℳR meromorphically to {Re λ < b̃}. In the strip {b < Re λ < b̃}, of width at most 1, the poles are at the
roots −μ in it ([[lem:iii-g4-1-1]] (2)) and at the at most one z_j(α) in it, all simple; for D small none is on the
boundary lines. Moving the contour from {Re λ = b − δ} to {Re λ = b̃},

    R = −Σ_p res_(λ=p)(r̂^λℳR(λ)) + R̃,     R̃ := (1/(2πi)) ∫_(Re λ=b̃) r̂^λℳR(λ) dλ ∈ H^(∞,b̃)_b,       {#eq:iii-g4-3-9}

holomorphic in α, as the integrand is and the bounds are locally uniform.

*The pairing.* If z_j(α₀) = −μ for a root, then 2 − α₀ = −μ − j ∈ (−ε_ind, 1); as {−μ} is 0 or in
[ε_ind, 1 − ε_ind] ([[eq:iii-f1-2-2]]), this forces j = ⌊−μ⌋ and β_μ(α₀) = 0. Indeed, with x := Re(2 − α), for
j ≥ ⌊−μ⌋ + 1 one has Re(z_j(α) + μ) = x + j − ⌊−μ⌋ − {−μ} ≥ x + 1 − {−μ} ≥ x + ε_ind, and for j ≤ ⌊−μ⌋ − 1 one has
Re(z_j(α) + μ) ≤ x − 1, so |z_j(α) + μ| ≥ min(1 − x, x + ε_ind) > 0 for j ≠ ⌊−μ⌋ when x ∈ (−ε_ind, 1). So at most one
root of the strip, −μ_*, can meet the pole z := z_(⌊−μ_*⌋) as α varies, and the other roots and z_j stay apart on D
small.

*The residues.* (i) At a root −μ apart from the z_j: −res = −r̂^(−μ)Π_μΦ(−μ), a kernel term
r̂^(−μ) Σ_τ φ^((μ,τ))_0(Y_τ) with Y_τ(α) holomorphic ([[lem:iii-g4-1-1]] (2) and the isomorphism Y ↦ φ₀(Y)). (ii) At a
z_j apart from the roots: −res = r̂^(z_j)N₀(z_j)⁻¹a_j, of the form r̂^(2−α+j)c(α) with c holomorphic in C^∞(𝕊³)
(N₀(z_j) is invertible and elliptic for α ∈ D). (iii) At the pair: near −μ_* write N₀(λ)⁻¹ = Π/(λ + μ_*) + Ĩ(λ) and
Φ(λ) = −a/(λ − z) + Φ̃(λ), with Ĩ, Φ̃ holomorphic and a = a_(⌊−μ_*⌋). By partial fractions,
Πa/((λ + μ_*)(λ − z)) = (Πa/(z + μ_*))(1/(λ − z) − 1/(λ + μ_*)), and the residues of r̂^λN₀⁻¹Φ at −μ_* and z sum to
−Πa(r̂^z − r̂^(−μ_*))/(z + μ_*) + r̂^(−μ_*)ΠΦ̃(−μ_*) − r̂^zĨ(z)a. By [[lem:iii-g4-2-4]] (4) and z + μ_* = β_(μ_*), the
contribution to R is

    Πa r̂^(−μ_*) l_(β_(μ_*))(r̂) − r̂^(−μ_*)ΠΦ̃(−μ_*) + r̂^zĨ(z)a,                                      {#eq:iii-g4-3-10}

each term holomorphic in α ∈ D, also where β_(μ_*) = 0 (z = −μ_*, a double pole, giving log r̂). For z ≠ −μ_*,
[[eq:iii-g4-3-10]] is the sum of (i) and (ii), so it holds on all of D.

*Normal form.* A kernel term is converted by [[lem:iii-g4-2-4]] (4) with z = β_μ − μ:
r̂^(−μ)φ₀(Y) = l_(β_μ)r̂^(−μ)φ₀(−β_μY) + r̂^(2−α+⌊−μ⌋)φ₀(Y), the second term of the form (ii). So
R = Σ_μ l_(β_μ)r̂^(−μ)Σ_τ φ₀(Y_(μ,τ)) + U₀ + R̃ with U₀ a finite sum of terms (ii) and Y_(μ,τ) holomorphic. Now replace
r̂^(−μ)φ₀ by H_(μ,τ): H_(μ,τ) − r̂^(−μ)φ₀ = Σ_(1≤i≤c_μ) (∓ir̂)^i r̂^(−μ)φ_i. If μ = μ_*, l_β r̂^(i−μ) lies in
H^(∞,c)_b for c < min(i − μ, i + Re z) ([[lem:iii-g4-2-4]] (2)), and −μ, Re z > b give c up to b + 1 ≥ b̃ with room;
otherwise β_μ stays away from 0 on D and l_β r̂^(i−μ) = β⁻¹(r̂^(2−α+⌊−μ⌋+i) − r̂^(i−μ)), a term (ii) plus an element of
H^(∞,c)_b with c < i − μ, and i − μ > b + 1 ≥ b̃. This gives [[eq:iii-g4-3-6]] on (0, 1), with U the sum of U₀ and
these parts of type (ii), in 𝔉_D.

*The last step.* If b̃ = w₀, then b + 1 > w₀ (as b + 1 ≥ w₀ and b + 1 ≠ w₀), so Φ, and with it ℳR, is meromorphic on
{Re λ < b + 1}, which contains {Re λ ≤ w(α)} for D small. Shift the contour instead to {Re λ = w(α)}, which depends on
α: for D small no root lies near it (w₀ ≠ −μ), and the z_j with j < ℓ_zf have Re z_j ≤ w(α) − δ_ℓ,
δ_ℓ := ℓ_zf − max{j ∈ ℕ₀ : j < ℓ_zf} > 0. With λ = ζ + 2 − α,
r̂^(α−2)R̃ = (1/(2πi)) ∫_(Re ζ=ℓ_zf) r̂^ζ ℳR(ζ + 2 − α) dζ, an integral over a fixed line of an integrand holomorphic in
α, with values in H^(∞,ℓ_zf)_b by (M1). ∎

*Proof of [[thm:iii-g4-3-1]].* *The hypotheses of [[cor:iii-f1-3-4]].* At sctf, ρ_ztf ∼ 1 and ρ_ztf^(−α)f₀ has weight
ℓ_scf + 1 = β_sctf + 1. At ztf, f₀ ∈ H^(∞,c)_b for c < min(0, ℓ_zf), so ρ_ztf^(−α)f₀ has every weight below
min(−Re α, ℓ_zf − Re α), which exceeds β_ztf − 2 for α near α₀; and β_ztf ∈ [−1, 0). The map α ↦ ρ_ztf^(−α)f₀ is
holomorphic into that domain, so u_α is holomorphic. Two choices of β_ztf give two solutions in the space with the
smaller weight, on which N_tf is injective ([[cor:iii-f1-3-4]]); so they agree.

*Away from ztf.* (1 − χ_ztf)u_α = (1 − χ_ztf)u_(α,∞) with u_(α,∞) := χ′u_α, χ′ equal to 1 on supp(1 − χ_ztf) and 0
near ztf; it is in H^(∞,ℓ_scf−ε,0)_b, holomorphically.

*Near ztf.* Let v := u_α on (0, 1)_r̂, in H^(∞,b₀)_b([0, 1) × 𝕊³), b₀ := β_ztf. Then
Pv = r̂²ρ_ztf^(−α)f₀ = r̂^(2−α)(1 + r̂)^α f₀ ∈ 𝔉_D. Put R₀ := v, T₀ := U₀ := 0. Inductively, if v = T_i + U_i + R_i with
T_i a sum of terms l_(β_μ)H_(μ,τ)(Y) over the roots with −μ < b_i, U_i ∈ 𝔉_D and R_i ∈ H^(∞,b_i)_b, then
PR_i ∈ 𝔉_D by [[lem:iii-g4-3-2]]–[[lem:iii-g4-3-3]], and [[lem:iii-g4-3-4]] (with b_i decreased slightly if it is a
forbidden real part or if b_i + 1 = w₀, H^(∞,b)_b ⊂ H^(∞,b−δ)_b) gives the data at b_(i+1) := b̃_i. Each step raises the
weight by almost 1, so after at most five steps b_i = w₀, the last step taken as in the last paragraph of the proof of
[[lem:iii-g4-3-4]]. As b₀ < 0 and no root has −μ ∈ [−1, 0) ([[prop:iii-f1-2-3]] (a)), the roots met are exactly those
with 0 ≤ −μ < w₀, that is 𝒲(w₀), each in one step. On supp χ_ztf ⊂ {r̂ < 1}, u_α = v; so [[eq:iii-g4-3-3]] holds with
u_(α,0) := Σ l_(β_μ)H_(μ,τ)(Y) and u_(α,1) := r̂^(α−2)(U + R) near ztf. [[eq:iii-g4-3-5]] is [[eq:iii-g4-3-4]] written
out over the rows of the table of [[sec:iii-g2-1]] with c_μ of [[eq:iii-g4-1-4]]; the multiplicities are one per type,
as each root is simple. ∎

**Remark {#rem:iii-g4-3-5}** ([Hin26, Remark 9.27] in dimension 4 + 1.) (1) Expanding l_β, the coefficients of
r̂^(z_(⌊−μ⌋)) and r̂^(−μ) in u_(α,0) are ±β_μ(α)⁻¹φ₀(Y): meromorphic, with simple poles where β_μ(α) = 0, that is at
2 − α = 0 (the integer roots) and at 2 − α = λ^Υ_(sl,l+j) − (l + j) for the six class roots of [[eq:iii-g4-3-5]]. These
are exactly the α at which an exponent 2 − α + j of the right-hand side meets a root −μ of N₀ (the pairing in the proof
of [[lem:iii-g4-3-4]]), and there u_(α,0) has log r̂ terms. (2) For other α one may replace l_(β_μ)H by −β_μ⁻¹H, the term
β_μ⁻¹r̂^(β_μ)H = β_μ⁻¹r̂^(2−α+⌊−μ⌋)(…) being absorbed into r̂^(2−α)u_(α,1); this is not regular as β_μ → 0.
(3) χ_ztf u_(α,0) is holomorphic in α with values in H^(∞,c)_b near ztf for every c < min(0, 2 − Re α₀): by
[[lem:iii-g4-2-4]] (2), l_(β_μ)H_(μ,τ) has every weight below
−μ + min(0, Re β_μ) = min(−μ, 2 − Re α + ⌊−μ⌋) ≥ min(0, 2 − Re α).

**Remark {#rem:iii-g4-3-6}** ([Hin26, Remark 9.28] in dimension 4 + 1.) For α₀ = 2 the right-hand side f₀ may have a
non-trivial
smooth expansion at r̂ = 0, unlike the right-hand sides of [[thm:iii-g2-3-1]], which have none at R = 0. Such f₀ arise as
restrictions to tf of Fourier transforms of functions with good decay at K⁺, which is high regularity, not vanishing,
at zf ([[prop:iii-a-4-2]], which is [Hin26, Proposition 2.25] in dimension 4 + 1).

### Grafting into the low-energy space {#sec:iii-g4-4}

This section is [Hin26, Definition 9.29, (9.72), Proposition 9.30, Remarks 9.31–9.34] in dimension 4 + 1.

**Definition {#def:iii-g4-4-1}** ([Hin26, Definition 9.29] in dimension 4 + 1.) For a generic row (μ, τ) of 𝒲,
Y ∈ 𝒴_τ and k ≤ K_μ, h^((μ),≤k)_(b,τ)(σ, Y) := Σ_(j=0)^k (−iσ)^j h̆^((μ),j)_(b,τ)(Y), h̆^((μ),0)_b being the state.
For s1 and v1, in the indexing of [Hin26], h̆^(≤k)_(b,s1)(σ, S) := Σ_(j=1)^k (−iσ)^(j−1)h̆^j_(b,s1)(S) (without
h_(b,s1), as in [Hin26, (9.71)]) and h^(≤k)_(b,v1)(σ, V) := h_(b,v1)(V) + Σ_(j=1)^k (−iσ)^j h̆^j_(b,v1)(V). These are
polynomials in σ with smooth stationary coefficients.

**Lemma {#lem:iii-g4-4-2}** ([Hin26, (9.72)] in dimension 4 + 1.) With the stationary tensors
E_k := [L_b, t_*]h̆^((μ),k)_b + ½[[L_b, t_*], t_*]h̆^((μ),k−1)_b and E′_k := ½[[L_b, t_*], t_*]h̆^((μ),k)_b
(h̆^((μ),−1)_b := 0),

    L̂_b(σ)h^((μ),≤k)_(b,τ)(σ, Y) = (−iσ)^(k+1)E_k(Y) + (−iσ)^(k+2)E′_k(Y),                              {#eq:iii-g4-4-1}

and the same holds for h_(b,s1)(S) − iσh̆^(≤k)_(b,s1)(σ, S) and for h^(≤k)_(b,v1)(σ, V), with the towers of
[[def:iii-g2-2-5]]. So each lies in |σ|^(k+1)C^∞(±[0, 1)_σ × X°); for s1 with k = 4 this is [Hin26, (9.72)].

*Proof.* By [[lem:iii-g2-2-6]], L_bh^(≤k)_b(a) is given by [[eq:iii-g2-2-2]]. Take a = e^(−iσt_*), so
a^((j)) = (−iσ)^j e^(−iσt_*), and use L_b(e^(−iσt_*)w) = e^(−iσt_*)L̂_b(σ)w for stationary w. For s1,
h^(≤k)_(b,s1)(e^(−iσt_*)S) = e^(−iσt_*)(h_(b,s1)(S) − iσh̆^(≤k)_(b,s1)(σ, S)). ∎

**Lemma {#lem:iii-g4-4-3}** (Restrictions to tf.) For a generic row let G_(μ,τ)(σ, Y) := |σ|^(−μ)h^((μ),≤c_μ)_(b,τ)(σ,
Y); for v1, G_(v1)(σ, V) := |σ|iσ⁻¹h^(≤2)_(b,v1)(σ, V); for s1, G_(s1)(σ, S) := |σ|iσ⁻¹h̆^(≤3)_(b,s1)(σ, S) and
G^exc_(s1)(σ, S) := −|σ|σ⁻²h_(b,s1)(S). Near tf each is polyhomogeneous, with tf-index set (0, 0) ∪ ℰ_ind, where ℰ_ind
collects the index sets of the corrections of the states (min Re ℰ_ind ≥ ε_Υ, with the convention of [[sec:iii-d2-1]] for
ℰ_ind) and (2, 0), and G|_tf = H_(μ,τ)(Y), h̄^(≤2)_(v1)(±r̂, V), h̄^(≤3)_(s1)(±r̂, S) respectively; G^exc_(s1) vanishes
at tf to order 2.

*Proof.* Write h̆^((μ),j)_b = χh̆̄^((μ),j) + e_j with e_j ∈ 𝒜^(μ−j+ℰ_ind) ([[sec:iii-g2-2-2]]). By [[lem:iii-g4-2-2]]
(1), |σ|^(−μ)(−iσ)^j h̆̄^((μ),j) = (∓ir̂)^j r̂^(−μ)φ_j, a function of (r̂, ω) alone, so smooth at tf. And
|σ|^(−μ)(−iσ)^j e_j is r̂^(j−μ) times ρ^(−μ+j)e_j, polyhomogeneous with index set ℰ_ind in ρ = ρ_scf ρ_tf, so it
vanishes at tf. For v1, h_(b,v1) ∈ 𝒜^((3,0)∪…) ([[eq:iii-d2-3-4]]) gives |σ|σ⁻¹ρ³, of tf-order 3, and the terms j ≥ 1
give |σ|iσ⁻¹(−iσ)^j ρ^(−j)φ^((−1,v1))_(j−1) = (∓ir̂)^(j−1) r̂ φ^((−1,v1))_(j−1) (as i(−i) = 1), that is h̄^(≤2)_(v1).
For s1, h̆¹_(b,s1) ∈ 𝒜^((2,0)∪…) gives |σ|σ⁻¹ρ², of tf-order 2, and the terms j ≥ 2 give
|σ|iσ⁻¹(−iσ)^(j−1)ρ^(1−j)φ^((−1,s1))_(j−2) = (∓ir̂)^(j−2) r̂ φ^((−1,s1))_(j−2), that is h̄^(≤3)_(s1); and
|σ|σ⁻²h_(b,s1) ∈ |σ|⁻¹ρ³𝒜⁰ = ρ_tf²ρ_zf⁻¹ρ_scf³𝒜⁰. ∎

*Hypotheses.* Let α₀ ∈ ℂ with Re α₀ ∈ (1, 2 + ε_ind), k ∈ ℕ₀, ℓ_scf < 3/2, and

    −ε_ind < ℓ_zf − Re α₀ + 2,     ℓ_zf − min(Re α₀ − 2, 0) < ℓ_K^max,     ℓ_zf ∉ ℕ₀,
    ℓ_zf − Re α₀ + 2 ≠ −μ                                                                               {#eq:iii-g4-4-2}

for every root μ. These imply [[eq:iii-g4-3-1]], as w₀ ≤ ℓ_zf − min(Re α₀ − 2, 0). They also give ℓ_zf < 3 (if
Re α₀ ≥ 2, ℓ_zf < ℓ_K^max ≤ 3; if Re α₀ < 2, ℓ_zf < ℓ_K^max + Re α₀ − 2 < 3), which Step 1.2 (iii) below uses through
the bound 3 of its zf-orders. That use could be removed by the split of the second case of [[lem:iii-g4-3-3]] (the term
it splits off carries |σ|³, which is smooth); we keep [[eq:iii-g4-4-2]].

**Proposition {#prop:iii-g4-4-4}** ([Hin26, Proposition 9.30] in dimension 4 + 1.) Assume [[eq:iii-g4-4-2]] and let
f ∈ H^(∞,ℓ_scf+1,(α₀,k),((0,0),ℓ_zf))_b(X^±_(sc-b); S²T*X).

(1) There is u ∈ ⋂_(ε>0) H^(∞,ℓ_scf−ε,Re α₀−2−ε,min(−1,Re α₀−3)−ε)_b(X^±_(sc-b)), smooth in the Myers–Perry
parameters b near b₀, with

    f − L̂_b(σ)u ∈ H^(∞,ℓ_scf+1,ℰ_(α₀,k),((0,0),ℓ_zf))_b(X^±_(sc-b)),
    ℰ_(α₀,k) := ((α₀, k) + ℰ_ind) ∪ ((4, k + 1) + ((0, 0) ∪ ℰ_ind)),                                     {#eq:iii-g4-4-3}

where ℰ_ind, an index set with min Re ℰ_ind ≥ ε_Υ not depending on b, α₀, k, is that of [[lem:iii-g4-4-3]] together
with (1, 0). The exponents at 4 come from the term l_(2−α₀)(|σ|)G^exc_(s1) (Step 1.1); their real part exceeds
Re α₀ + ε_Υ. [Hin26, (9.74), (9.81)] state the index set (α₀, k) + ℰ_ind without them.

(2) For k = 0 one can take u = χ_zf|σ|^(α₀−2)u_b + χ_tf ρ_tf^(α₀−2)u_tf with
u_tf ∈ H^(∞,ℓ_scf−ε,((0,0),ℓ_zf))_b(tf) and

    u_b = l_(2−α₀)(|σ|)G^exc_(s1)(σ, S^((−1))_1) + l_(2−α₀)(r̂)(G_(s1)(σ, S^((−1))_1) + G_(v1)(σ, V^((−1))_1))
          + Σ′_(μ,τ) l_(β_μ(α₀))(r̂)G_(μ,τ)(σ, Y^((μ))_τ),                                               {#eq:iii-g4-4-4}

the primed sum over the other rows of 𝒲(w₀), as in [[eq:iii-g4-3-5]]; that is, in the notation of [Hin26],
−l_(2−α₀)(|σ|)|σ|σ⁻²h_(b,s1)(S) + l_(2−α₀)(r̂)|σ|iσ⁻¹(h̆^(≤3)_(b,s1)(σ, S) + h^(≤2)_(b,v1)(σ, V)) + …, and
l_(β_μ)(r̂)|σ|^(−μ)h^((μ),≤c_μ)_(b,τ)(σ, Y) for the others. For general k, u is a sum of terms of this form and of up to
k-fold derivatives of such terms in α₀.

*Proof.* It suffices to solve away one term χ_tf ρ_tf^(α₀)(log ρ_tf)^k f₀(r̂, ω),
f₀ ∈ H^(∞,ℓ_scf+1,((0,0),ℓ_zf))_b(tf), of the expansion of f at tf: f is a sum of k + 1 such terms (with coefficients in
that space, the restrictions to tf of the coefficients of its partial expansion) and a remainder of tf-index set
(α₀ + 1, k) ⊂ (α₀, k) + ℰ_ind, as (1, 0) ∈ ℰ_ind; and terms with lower powers of the logarithm are treated in the same
way.

*Step 1: no logarithms.* For α near α₀ let u_(tf,α) := N_tf⁻¹(ρ_ztf^(−α)f₀), written as [[eq:iii-g4-3-3]] by
[[thm:iii-g4-3-1]] (with χ_ztf = χ_zf|_tf), and let u_(b,α) be [[eq:iii-g4-4-4]] with α in place of α₀ and the
coefficients of [[thm:iii-g4-3-1]]. Put

    u_α := |σ|^(α−2)W_α,     W_α := χ_zf u_(b,α) + χ_tf(χ_zf r̂^(2−α)u_(α,1) + (1 − χ_zf)u_(α,∞)).       {#eq:iii-g4-4-5}

The functions l_β(r̂), l_β(|σ|) and |σ|^(α−2) are holomorphic in α with values in the conormal spaces of
[[lem:iii-g4-2-4]] (2), and the states do not depend on α; so u_α is holomorphic in α with values in
H^(∞,ℓ_scf−ε,Re α₀−2−ε,min(−1,Re α₀−3)−ε)_b. The zf-weight comes from l_(2−α)(|σ|)|σ|^(α−3)h_(b,s1), of order
Re α − 3 + min(0, 2 − Re α); every other term is better: the generic rows, as
Re α − 2 − μ + min(0, Re β_μ) ≥ min(Re α − 2, 0), and the s1 and v1 terms G_(s1), G_(v1), which carry |σ|⁰, have the
order Re α − 2 + min(0, 2 − Re α) = min(Re α − 2, 0) directly.

In [[eq:iii-g4-4-5]], as |σ|^(α−2)r̂^(2−α) = ρ^(α−2), ρ = ρ_scf ρ_tf and |σ| = ρ_tf ρ_zf, the second part of u_α is
χ_tf ρ_tf^(α−2)u_tf with u_tf := ρ_scf^(α−2)χ₁u_(α,1) + ρ_zf^(α−2)(1 − χ₁)u_(α,∞), a function of (r̂, ω) in
H^(∞,ℓ_scf−ε,((0,0),ℓ_zf))_b(tf) (ρ_scf, ρ_zf and χ_zf = χ₁(r̂) being functions of r̂); at α = α₀ this is the form of
(2) (as in the paragraph of [Hin26] after (9.80)).

*Step 1.1: the restriction.* W_α is polyhomogeneous at tf with index set (0, 0) ∪ ℰ_ind, apart from the term
χ_zf l_(2−α)(|σ|)G^exc_(s1), and W_α|_tf = u_(tf,α). As l_(2−α)(|σ|) = ((ρ_tf ρ_zf)^(2−α) − 1)/(2 − α), that term has
the tf-exponents 2 and 4 − α (with 2 + ℰ_ind, 4 − α + ℰ_ind), merging into a logarithm at α = 2; equivalently,
|σ|^(α−2)l_(2−α)(|σ|)G^exc_(s1) = (2 − α)⁻¹(1 − |σ|^(α−2))G^exc_(s1) has the tf-exponents 2 and α. Indeed
χ_zf|_tf = χ_ztf, χ_tf = 1 near tf, the functions of (r̂, ω) are smooth at tf, and by [[lem:iii-g4-4-3]]
(χ_zf u_(b,α))|_tf = χ_ztf u_(α,0): the term l_(2−α)(|σ|)G^exc_(s1) vanishes at tf, to order
2 + min(0, 2 − Re α) − ε > 1.

*Step 1.2: the error.* Let F_α := χ_tf ρ_tf^α f₀ − L̂_b(σ)u_α. We show
F_α ∈ H^(∞,ℓ_scf+1,ℰ_α,((0,0),ℓ_zf))_b with ℰ_α := (α + ℰ_ind) ∪ (4 + ((0, 0) ∪ ℰ_ind)) for α ≠ 2 (the exponents 4
and α + 2 merging into a logarithm at α = 2), holomorphically in α as an element of
H^(∞,ℓ_scf+1,Re α₀+ε_Υ−ε,((0,0),ℓ_zf))_b.

(i) *tf.* As L̂_b(σ) has no σ-derivatives, L̂_b(σ)u_α = |σ|^(α−2)L̂_b(σ)W_α. View u_(tf,α) as a function of (r̂, ω) near
tf. By [[lem:iii-g4-1-1]] (1), |σ|^(α−2)L̄̂(σ)u_(tf,α) = |σ|^αN_tf u_(tf,α) = |σ|^α ρ_ztf^(−α)f₀ = ρ_tf^α f₀, since
ρ_zf = ρ_ztf as functions of r̂ and |σ| = ρ_tf ρ_zf. So near tf,

    F_α = −|σ|^(α−2)L̄̂(σ)(W_α − u_(tf,α)) − |σ|^(α−2)(L̂_b(σ) − L̄̂(σ))W_α.

By [[lem:iii-g4-1-2]] and Step 1.1, the first term has tf-index set α − 2 + 2 + ℰ_ind (b-operators preserve index sets,
property (F1) of [[sec:iii-a-1]]) and the second α + 2 + ((0, 0) ∪ ℰ_ind) ⊂ α + ℰ_ind, as (2, 0) ∈ ℰ_ind, apart from
the term of G^exc_(s1), which by Step 1.1 gives the exponents 4 and α + 2 (from L̄̂(σ) ∈ ρ_tf²Diff_b) and 6 and α + 4
(from [[lem:iii-g4-1-2]]), each with ℰ_ind: in ℰ_α. Away from tf there is nothing to show at tf.

(ii) *scf.* Near scf, χ_zf = 0 and W_α = χ_tf u_(α,∞), with sctf-weight ℓ_scf − ε; near sctf, u_(tf,α) = u_(α,∞).
Where χ_tf = 1, (i) gives F_α = −|σ|^(α−2)(L̂_b − L̄̂)u_(α,∞), of scf-order ℓ_scf + 2 − ε by [[lem:iii-g4-1-2]].
Elsewhere add −|σ|^(α−2)[L̂_b(σ), χ_tf]u_(α,∞): ρ∂_ρχ₂(ρ + |σ|) = ρχ₂′ carries ρ = ρ_scf ρ_tf, so the commutator lies
in ρ_scf²ρ_tf³Diff¹_b, and this term too has scf-order ℓ_scf + 2 − ε ≥ ℓ_scf + 1.

(iii) *zf.* We read the zf-index sets at zf°, where |σ| defines zf and x ranges over compact sets of X°. Near tf ∩ zf
every term of F_α is a finite sum of products of jointly polyhomogeneous factors (powers of |σ|, ρ, r̂, the functions
l_β(r̂), l_β(|σ|), and the expansions of the states at ρ = 0) and of the remainder r̂^(2−α)u_(α,1) with its own
zf-structure; for such a product the zf-exponents do not depend on the point of zf, so they are those read at zf°. There
χ_zf = 1, and F_α is χ_tf ρ_tf^α f₀ (whose zf-structure is that of f₀ at ztf, as r̂ = |σ|r) minus the following.
(a) L̂_b(σ)(|σ|^(α−2)χ_tf r̂^(2−α)u_(α,1)) = L̂_b(σ)(ρ^(α−2)χ_tf u_(α,1)(|σ|r, ω)), of zf-class ((0, 0), ℓ_zf), as
L̂_b(σ) is a differential operator in x polynomial in σ. (b) A generic term:
L̂_b(σ)(|σ|^(α−2−μ)l_β(r̂)h^(≤c_μ)_b) = |σ|^(α−2−μ)(l_βL̂_b(σ)h^(≤c_μ)_b + [L̂_b(σ), l_β]h^(≤c_μ)_b). As
l_β(|σ|r) ∈ 𝒜^(min(0,Re β)−ε) in |σ| and [[lem:iii-g4-4-2]] gives |σ|^(c_μ+1), the first part has zf-order
Re α − 2 − μ + min(0, Re β_μ) + c_μ + 1 − ε = min(Re α + 1 + {−μ}, 3) − ε > ℓ_zf, by [[eq:iii-g4-4-2]] and α near α₀.
For the second, ∂_x(l_β(|σ|r)) = (|σ|r)^β∂_x log r ([Hin26, (9.82)]), so [L̂_b(σ), l_β(r̂)] = r̂^βD_β(σ) with D_β(σ) a
first-order operator on X° with coefficients smooth in x (r is bounded below on X), polynomial in σ and β; and
|σ|^(α−2−μ)r̂^(β_μ) = |σ|^(⌊−μ⌋)r^(β_μ), so this part is smooth in σ at σ = 0, of zf-class (0, 0). (c) The s1 terms,
[Hin26, (9.83)]: with β := 2 − α,

    |σ|^(α−2)L̂_b(σ)(−l_β(|σ|)|σ|σ⁻²h_(b,s1) + l_β(r̂)|σ|iσ⁻¹h̆^(≤3)_(b,s1))
      = −|σ|^(α−2)l_β(|σ|)|σ|σ⁻²L̂_b(σ)(h_(b,s1) − iσh̆^(≤3)_(b,s1))
        + |σ|^(α−2)(l_β(r̂) − l_β(|σ|))|σ|iσ⁻¹L̂_b(σ)h̆^(≤3)_(b,s1) + |σ|^(α−2)[L̂_b(σ), l_β(r̂)]|σ|iσ⁻¹h̆^(≤3)_(b,s1).

By [[lem:iii-g4-4-2]] the first line on the right has zf-order
Re α − 2 + min(0, Re β) + 1 − 2 + 4 − ε = min(Re α + 1, 3) − ε > ℓ_zf. By [[lem:iii-g4-2-4]] (3),
l_β(r̂) − l_β(|σ|) = |σ|^β l_β(r), so the second term is ±i l_β(r)L̂_b(σ)h̆^(≤3)_(b,s1), smooth in σ; and the third is
±i r^βD_β(σ)h̆^(≤3)_(b,s1), smooth in σ. (d) The v1 term in the same way: [[lem:iii-g4-4-2]] gives zf-order
Re α − 2 + min(0, Re β) + 3 − ε = min(Re α + 1, 3) − ε, and its commutator part is smooth in σ. (e) The commutators with
the cut-offs: χ_zf = 1 near zf°; [L̂_b(σ), χ_tf] acts only on the term of (a) (χ_tf does not multiply u_(b,α) in
[[eq:iii-g4-4-5]]), with the same conclusion. So F_α has zf-class ((0, 0), ℓ_zf). Holomorphy in α holds term by term.

*Step 2: logarithms.* The term is ∂_α^k(χ_tf ρ_tf^α f₀)|_(α₀). Let u := ∂^k_α u_α|_(α₀). By the holomorphy in Step 1.2,
χ_tf ρ_tf^(α₀)(log ρ_tf)^k f₀ − L̂_b(σ)u = ∂^k_αF_α|_(α₀) lies in H^(∞,ℓ_scf+1,Re α₀+ε_Υ−ε,((0,0),ℓ_zf))_b, and
differentiating [[eq:iii-g4-4-5]] term by term shows that it is polyhomogeneous at tf with index set ℰ_(α₀,k) of
[[eq:iii-g4-4-3]] (the k-th α-derivative of the exponents 4 and α + 2 of the term of G^exc_(s1), which merge at
α₀ = 2, carries at most k + 1 logarithms at 4). The membership of u is that of u_α, with logarithmic factors absorbed by
ε.

*Parameters.* N_tf does not depend on b, the states depend smoothly on b ([[ch:s13]], [[ch:s15]]), and so does u. ∎

**Remark {#rem:iii-g4-4-5}** ([Hin26, Remarks 9.31–9.33] in dimension 4 + 1.) (1) u solves f away to leading order at
tf without creating zf-error terms worse than those of f. For Re α₀ ≤ 2 the restriction of f to zf (k = 0) is of class
𝒜^(α₀)(X), and [Hin26] notes that this weight lies outside the range where the zero energy operator (or an augmentation
of it) is inverted, which is why the tf-model is inverted instead; in dimension 4 + 1 the range is that of
[[cor:iii-f3-4-2]]. (2) The weaker the tf-order of f, the more singular u at zf: the dominant term is
|σ|^(α₀−2)l_(2−α₀)(|σ|)G^exc_(s1), of zf-order min(−1, Re α₀ − 3) (without the factor |σ|^(α₀−2),
min(−1, 1 − Re α₀)). The time translation term contributes |σ|^(α₀−2)h^((0),≤2)_(b,s0) and, for α₀ ≠ 2, a smooth term
h^((0),≤2)_(b,s0); as α₀ → 2 they combine into (log |σ|)h^((0),≤2)_(b,s0), and likewise |σ|²h^((−2))_(b,s2,ph). The
mechanism is the indicial root 0 of the tf-model, as for the flat Laplacian, in any dimension. (3) A tf-order α₀
corresponds to an ι⁺-order α₀ + 1 ([[prop:iii-a-4-2]]), and the term t_*^(−α₀+1)h^((0))_(b,s0) of [[thm:iii-g2-4-2]]
is, on the Fourier side, essentially |σ|^(α₀−2)h^((0))_(b,s0).

**Remark {#rem:iii-g4-4-6}** ([Hin26, Remark 9.34] in dimension 4 + 1.) Had l_(2−α₀)(r̂) been used for the term of
h_(b,s1), the calculation for s1 would gain
−|σ|^(α₀−2)[L̂_b(σ), l_(2−α₀)(r̂)]|σ|σ⁻²h_(b,s1) = −|σ|⁻¹r^(2−α₀)D_(2−α₀)(σ)h_(b,s1) (Step 1.2 (b)), of class
|σ|⁻¹C^∞, singular at σ = 0.

The exceptional term G^exc_(s1) = −|σ|σ⁻²h_(b,s1) vanishes at tf to order 2 (order 1 in [Hin26]), as h_(b,s1) ∈ 𝒜³ in
dimension 4 + 1 ([[eq:iii-d2-3-4]]); its zf-order, which sets min(−1, Re α₀ − 3) in [[prop:iii-g4-4-4]] (1), is
unchanged. The factor l_(2−α)(|σ|) of the term l_(2−α)(|σ|)G^exc_(s1) carries the tf-exponent 2 − α, so the grafting
error has tf-exponents at 4 (and 6) besides α₀ + ℰ_ind, which is the index set ℰ_(α₀,k) of [[eq:iii-g4-4-3]]; the
weights are unaffected, as 4 > Re α₀ + ε_Υ.

### Conormal sources at tf {#sec:iii-g4-5}

This section is [Hin26, Proposition 9.35] in dimension 4 + 1.

**Proposition {#prop:iii-g4-5-1}** ([Hin26, Proposition 9.35] in dimension 4 + 1.) Let α ∈ (1, 2), ℓ_scf < 3/2, and
−ε_ind < w := ℓ_zf − α + 2 < ℓ_K^max, ℓ_zf ∉ ℕ₀, with 2 − α + j ≠ −μ and w ≠ −μ for all j ∈ ℕ₀ and all roots μ of
L̂_b(0). Let k₀ ∈ ℕ₀ and f ∈ H^(∞,ℓ_scf+1,α,((k₀,0),ℓ_zf))_b(X^±_(sc-b); S²T*X). Then there is
u ∈ ⋂_(ε>0) H^(∞,ℓ_scf−ε,α−2,α−3)_b(X^±_(sc-b)) with

    f − L̂_b(σ)u ∈ ⋂_(ε>0) H^(∞,ℓ_scf+1,α+ε_Υ−ε,((k₀,0),ℓ_zf))_b(X^±_(sc-b)).                            {#eq:iii-g4-5-1}

One can take u = χ_zf u_b + χ^♯_tf ũ, with χ^♯_tf a cut-off of the kind of χ_tf (fixed in the proof),
ũ ∈ H^(∞,ℓ_scf−ε,α−2,((k₀,0),ℓ_zf))_b and

    u_b = h^(≤3)_(b,s1)(σ, |σ|^(α−3)S^((−1))_1(σ)) + h^(≤2)_(b,v1)(σ, |σ|^(α−2)V^((−1))_1(σ))
          + Σ′_(μ,τ) h^((μ),≤c_μ)_(b,τ)(σ, |σ|^(α−2−μ)Y^((μ))_τ(σ)),                                     {#eq:iii-g4-5-2}

where h^(≤3)_(b,s1)(σ, S) := h_(b,s1)(S) − iσh̆^(≤3)_(b,s1)(σ, S) and the coefficients lie in
H^(∞,0)_b(±[0, 1)_σ, |dσ/σ|; 𝒴_τ). As α < 2, ℓ_zf = w + α − 2 < 3. The point is that [[eq:iii-g4-5-1]] vanishes to
higher order at tf than f.

*Proof.* Replacing f by χ_tf f costs (1 − χ_tf)f, which is supported away from tf and has zf-class ((k₀, 0), ℓ_zf), so
it is of the form [[eq:iii-g4-5-1]].

*Step 1: the zf-expansion near the corner.* Near tf ∩ zf, in (ρ, r̂, ω), the partial expansion of f at zf reads
χ_zf χ_tf f = χ_zf χ_tf(Σ_(k₀≤j<ℓ_zf) |σ|^j ρ^(α−j)f^((j))(ρ, ω) + f′) (cut off by χ_zf, as its terms have scf-weight
α − j < ℓ_scf + 1 for j ≥ 1), and (1 − χ_zf)χ_tf f, which vanishes near zf, is of the form of f₁ below; here
f^((j)) ∈ H^(∞,0)_b([0, ρ₀)_ρ × 𝕊³) and f′ is of zf-weight ℓ_zf: the coefficients are functions on zf ≅ X̄, and
|σ|^jρ^(α−j) = ρ_tf^α ρ_zf^j ρ_scf^(α−j) carries the tf-weight of f. Each term is |σ|^j times a stationary function.
For j = k₀, k₀ + 1, …, ⌊ℓ_zf⌋ in turn, let v_j solve

    𝒩v_j = ρ^(α−2−j)χ₃(ρ)f^((j)) on (0, ∞)_ρ × 𝕊³,     v_j ∈ H^(∞,α−2−j)_b,                              {#eq:iii-g4-5-3}

(χ₃ ∈ C_c^∞([0, ρ₀)) equal to 1 near supp χ_tf): 𝒩 is elliptic and dilation invariant, and α − 2 − j is not the real
part of a root (2 − α + j ≠ −μ, the roots being real), so its Mellin family is invertible on that line, with the bounds
(E1) of [[sec:iii-a-1-1]], and [[eq:iii-g4-5-3]] is solved by Mellin inversion on {Re λ = α − 2 − j} (Plancherel).
Then U_j := χ_zf χ_tf|σ|^j v_j satisfies, by [[eq:iii-g4-1-2]] and [[lem:iii-g4-1-2]],
L̂_b(σ)U_j = χ_zf χ_tf|σ|^jρ^(α−j)f^((j)) + e_j on supp χ_tf (where χ₃ = 1), where e_j consists of three kinds of
terms. First, χ_zf χ_tf|σ|^(j+1)ρ^(α−j−1)g_(j+1) with g_(j+1) := ±iρ^(j+1−α)ρ(ρ∂_ρ − 3/2 − S̄)v_j ∈ H^(∞,0)_b, from
the term iσρ(·) of [[eq:iii-g4-1-2]]: a term of the same form at j + 1. Second, terms of tf-order α + 2, from
L̂_b(σ) − L̄̂(σ) ([[lem:iii-g4-1-2]]), of zf-class (k₀, 0). Third, commutators with χ_zf χ_tf; those with χ_tf are
supported away from tf and have zf-class (k₀, 0), and those with χ_zf = χ₁(r̂) are supported in {1/8 ≤ r̂ ≤ ¼}, away
from zf and scf. Subtracting g_(j+1) from f^((j+1)) (or setting f^((j+1)) := −g_(j+1) when j + 1 ≥ ℓ_zf) and
proceeding, we obtain u₀ := Σ_j U_j ∈ H^(∞,∞,α−2,(k₀,0))_b with

    χ_tf f − L̂_b(σ)u₀ = f₁ + f₂,     f₁ ∈ H^(∞,ℓ_scf+1,α,ℓ_zf)_b,                                       {#eq:iii-g4-5-4}

with f₂ the sum of an element of H^(∞,ℓ_scf+1,α+2,((k₀,0),ℓ_zf))_b and of terms supported away from tf of zf-class
((k₀, 0), ℓ_zf), so of the form [[eq:iii-g4-5-1]]; f₁ collects χ_zf χ_tf f′, (1 − χ_zf)χ_tf f, the commutators with
χ_zf, and the term of the form at j = ⌊ℓ_zf⌋ + 1, of zf-order > ℓ_zf.

The proof of [Hin26, Proposition 9.35] takes instead u⁽⁰⁾₀(ρ, ·) := L̃(0)(ω, α − 2, ∂_ω)⁻¹f⁽⁰⁾₀(ρ, ·) pointwise in ρ
and asserts that the terms in which r̂∂_r̂ falls on u⁽⁰⁾₀(|σ|/r̂, ω) carry a factor ρ. They carry ρ∂_ρu⁽⁰⁾₀, which for a
conormal f⁽⁰⁾₀ is of the size of u⁽⁰⁾₀. For f⁽⁰⁾₀ = ρ^(iξ)φ, ξ ∈ ℝ, the pointwise choice u = 𝒩(α − 2)⁻¹ρ^(iξ)φ gives
ρ^(−α)ρ²𝒩(ρ∂_ρ)(ρ^(α−2)u) = 𝒩(α − 2 + iξ)𝒩(α − 2)⁻¹ρ^(iξ)φ, so the error is
(𝒩(α − 2 + iξ)𝒩(α − 2)⁻¹ − 1)ρ^(iξ)φ, with no factor ρ, while [[eq:iii-g4-5-3]], which inverts 𝒩(α − 2 + iξ) on each
Mellin frequency, leaves no error. The pointwise choice is correct for f⁽⁰⁾₀ smooth in ρ: for f⁽⁰⁾₀ = φ₀ + ρφ₁ the same
calculation gives the error ρ(𝒩(α − 1)𝒩(α − 2)⁻¹ − 1)φ₁, which carries the factor ρ.

*Step 2: solving away f₁.* Let χ^♯_tf be a cut-off of the same kind, equal to 1 on the supports in Step 1, so
f₁ = χ^♯_tf f₁. In (σ, r̂, ω), with ρ_scf = (1 + r̂)⁻¹ and ρ_zf = r̂/(1 + r̂) on {ρ < ρ₀} ([[sec:iii-g4-1]]), and the
b-density |dσ/σ||(dr̂/r̂)dg̸|, |σ|^(−α)f₁ lies in H^(∞,0)_b(±[0, 1)_σ; H^(∞,ℓ_scf+1,ℓ_zf−α)_b(tf)), extended by 0 to
{r̂ ≤ |σ|/ρ₀}. Let u₁(σ) := N_tf⁻¹(|σ|^(−α)f₁(σ)) by [[cor:iii-f1-3-4]], with β_sctf = ℓ_scf and
β_ztf ∈ (−1, min(0, w)): as N_tf does not depend on σ (only on its sign), it commutes with σ∂_σ, and
u₁ ∈ H^(∞,0)_b(±[0, 1)_σ; H^(∞,ℓ_scf−ε,β_ztf)_b(tf)). Its expansion at ztf follows as in [[thm:iii-g4-3-1]], with σ as a
parameter and without terms from the right-hand side (Pu₁ has no expansion at ztf, its weight being w):
[[lem:iii-g4-3-4]] with no z_j gives only kernel terms r̂^(−μ)φ₀(Y(σ)), replaced by H_(μ,τ)(Y(σ)) at the cost of terms
of weight 1 − μ > b̃, and PH_(μ,τ) = (∓i)^(c_μ+1)r̂^(3+{−μ})ψ has weight 3 + {−μ} > w. So

    u₁ = χ_ztf Σ_(μ∈𝒲(w)) Σ_τ H_(μ,τ)(Y^((μ))_τ(σ)) + ũ₁,
    ũ₁ ∈ H^(∞,0)_b(±[0, 1)_σ; H^(∞,ℓ_scf−ε,w)_b(tf)),                                                    {#eq:iii-g4-5-5}

the coefficients Y(σ) continuous linear functionals of the data (the residues Π_μ applied to Mellin transforms), hence
in H^(∞,0)_b in σ. Put

    u₂ := |σ|^(α−2)χ_zf(G^exc_(s1) + G_(s1) + G_(v1) + Σ′G_(μ,τ))(σ, Y(σ))
          + |σ|^(α−2)χ^♯_tf ũ₁(σ, |σ|/ρ, ω),                                                            {#eq:iii-g4-5-6}

which is [Hin26, (9.92)] in dimension 4 + 1, with no functions l_β (no exponent of the right-hand side meets a root).
*tf.* By [[lem:iii-g4-4-3]], |σ|^(2−α)u₂ = u₁ + e near tf, with e of tf-weight ε_Υ (the coefficients Y(σ) are
conormal of weight 0), so by [[lem:iii-g4-1-1]]–[[lem:iii-g4-1-2]],
L̂_b(σ)u₂ = |σ|^αN_tf u₁ + |σ|^(α−2)(L̂_b − L̄̂)u₁ + |σ|^(α−2)L̂_b(σ)e = f₁ + O(ρ_tf^(α+2)) + O(ρ_tf^(α+ε_Υ−ε)) there.
*scf.* As in Step 1.2 (ii) of the proof of [[prop:iii-g4-4-4]]: scf-order ℓ_scf + 2 − ε. *zf.* |σ|^(α−2)ũ₁ has zf-weight
α − 2 + w = ℓ_zf,
preserved by L̂_b(σ); at zf°, by [[lem:iii-g4-4-2]], the generic terms give |σ|^(α−2−μ)|σ|^(c_μ+1)Y(σ), of zf-weight
α + 1 + {−μ}, and the s1 and v1 terms |σ|^(α+1); all exceed ℓ_zf, as ℓ_zf < α + 1 (w < 3). So f₁ − L̂_b(σ)u₂ is of the
form [[eq:iii-g4-5-1]]. With u := u₀ + u₂ and ũ := |σ|^(α−2)ũ₁ + χ_zf χ_tf Σ|σ|^j v_j (so that
u = χ_zf u_b + χ^♯_tf ũ, as χ^♯_tf = 1 on supp χ_tf), [[eq:iii-g4-5-1]]–[[eq:iii-g4-5-2]] hold, the powers of |σ| of
[[eq:iii-g4-5-2]] absorbing the signs and factors ±i; the zf-weight α − 3 of [[eq:iii-g4-5-2]] is that of
|σ|^(α−3)h_(b,s1). ∎

### The dimension in the exterior estimates of [Hin23a] {#sec:s17-exterior}

[Hin23a, Section 3] proves energy estimates near future null infinity and spatial infinity in dimension 3 + 1, for the
gauge-fixed Einstein operator of [Hin23a, Section 2]; [[ch:s26]] carries them to dimension 4 + 1, for the operator of
[[sec:iii-c-4]]. The spatial dimension n enters that section through the quantities collected in
[[prop:np-10-64]], which we give for n = 3, where they are the values printed in [Hin23a], and for n = 4.

*Notation.* Throughout this section k := (n − 1)/2 and □ = −tr ∇². On ℝ^(1+n) we use r := |x|, x⁰ := t + r,
x¹ := t − r, the coordinate fields ∂₀, ∂₁ of (x⁰, x¹, ω) as in [[eq:iii-c-1-5]], and the Minkowski metric
η := −dt² + dx² of ℝ^(1+n), that of [[sec:iii-c-1]] when n = 4: η = −½(dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰) + r²g̸, so
η(∂₀, ∂₁) = −½ and η⁻¹(dx⁰, dx¹) = −2. The splitting of [Hin23a, (2.9)]
is the splitting [[eq:iii-c-1-6]] with the summands in the order (00, 01, 0a, 11, 1a, tr, tf), numbered 1 to 7 in this
section: the slot coordinates are U₀₀ = U(∂₀, ∂₀), U₀₁, the tangential part U_(0a) of U(∂₀, ·), U₁₁, U_(1a), the
coordinate t_U := tr̸U/(n − 1) of r²g̸, and the trace-free tangential part. The modified operators of [Hin23a,
Definition 2.2, (2.4)–(2.5)] are, with c_C = c_Υ = r⁻¹dt near infinity,

    δ^*_(η,E_C) := δ^*_η + γ_C(2c_C ⊗_s (·) − η ι_(η⁻¹c_C)(·)),     δ_(η,E_Υ) := δ_η + γ_Υ(2ι_(η⁻¹c_Υ) − c_Υ tr_η).

The first-order coefficient at ℐ⁺ of the gauge terms of the operator is the endomorphism A_(E_C,E_Υ) of [Hin23a,
(2.10)]: with G := I − ½η tr_η, δ₁U := −ι_(η⁻¹dx¹)U and δ₁^*w := dx¹ ⊗_s w the ∂₁-coefficients of δ_η and δ^*_η, and
c := dt,

    A_(E_C,E_Υ)U := γ_C(2c ⊗_s w − η⟨c, w⟩) + δ₁^*(γ_Υ(2ι_(η⁻¹c)GU − c tr GU)),     w := δ₁GU.         {#eq:s17-hin23a-a}

The b-structure is that of [Hin23a, Section 3]: with the Tangherlini metric g_m of mass m in dimension 4 + 1 (the
Schwarzschild metric of mass m in dimension 3 + 1) and its tortoise coordinate r*, x⁰ := t + r*, x¹ := t − r*,
ρ₀ := 1/(r* − t), ρ_I := (r* − t)/r and x_I := ρ_I^(1/2); on Minkowski space r* = r. The conjugated operator of
[Hin23a, Proposition 3.17] is L := 2ρ_Iρ^(−(2+k))P′ρ^k, ρ := r⁻¹, with P′ the linearisation of the gauge-fixed
Einstein operator P.

**Proposition {#prop:np-10-64}** (The dimension in [Hin23a, Section 3].) For n = 3 and n = 4:

(1) On functions of (x⁰, x¹), for η, r^k□r^(−k) = 4∂₀∂₁ + ((n − 1)(n − 3)/4)r⁻², with no first-order term: the added
term is 0 at n = 3 ([Hin23a, (3.34)]) and ¾r⁻² at n = 4. For the Tangherlini metric of mass m in dimension 4 + 1, with
f := 1 − m/r², the tortoise coordinate r* := r + (√m/2)log((r − √m)/(r + √m)) satisfies dr*/dr = 1/f and

    r* − r = −Σ_(j≥0) m^(j+1)r^(−(2j+1))/(2j + 1) = −m/r − m²/(3r³) − m³/(5r⁵) − …,                       {#eq:s17-rstar}

a series in 1/r without the logarithm of the Schwarzschild coordinate r* = r + 2m log(r − 2m) of [Hin23a, (1.1)].

(2) On Minkowski space, with ρ₀ = 1/(r − t) and ρ_I = (r − t)/r, ρ₀^(n+1)ρ_I^n|dη| = |(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸| exactly.
So μ_b := ρ₀^(n+1)ρ_I^n|dg_m| is ρ₀⁴ρ_I³|dg_m| at n = 3 ([Hin23a, proof of Proposition 3.17, p. 16]) and
ρ₀⁵ρ_I⁴|dg_m| at n = 4, and L = 2ρ_Iρ^(−(2+k))P′ρ^k is symmetric on L²(μ_b) whenever P′ is symmetric on L²(|dg_m|).

(3) Let L₀ := −2ρ_I∂_(ρ_I)(ρ₀∂_(ρ₀) − ρ_I∂_(ρ_I)) + x_I²(Δ̸ + q_n), q_n := (n − 1)(n − 3)/4, Δ̸ ≥ 0 the Laplacian of
𝕊^(n−1), and W := w²V with w² := ρ₀^(−2α₀)ρ_I^(−2α_I) and V := ρ₀∂_(ρ₀) − (1 + c)ρ_I∂_(ρ_I) (the multiplier of
[Hin23a, (3.22)]), the divergence taken with respect to |(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|. With Δ̸ replaced by its eigenvalue λ,
the part of [L₀, W] − (div W)L₀ of second order in (ρ₀∂_(ρ₀), ρ_I∂_(ρ_I)), together with its angular term, has the
symbol

    w²(−4α_I(ξ₀ − ξ_I)² + 4c(α₀ − α_I)ξ_I² + (1 + 2(α₀ − α_I) + c(1 − 2α_I))x_I²(λ + q_n)),         {#eq:s17-energy-form}

with ξ₀, ξ_I dual to log ρ₀, log ρ_I (ρ₀∂_(ρ₀) ↦ iξ₀, ρ_I∂_(ρ_I) ↦ iξ_I): [Hin23a, (3.25)] with Δ̸ + q_n in place of
Δ̸. The constant
q_n enters only with the angular operator: on functions of ω alone, [L₀, W] − (div W)L₀ is
w²(1 + 2(α₀ − α_I) + c(1 − 2α_I))x_I²(Δ̸ + q_n).

(4) In the splitting (00, 01, 0a, 11, 1a, tr, tf), the matrix of [[eq:s17-hin23a-a]] (rows the output slots, columns
the input slots) is, with γ_C, γ_Υ written C, U,

    n = 3:   ( 2C   0     0    0     0    0          0 )       n = 4:   ( 2C   0      0    0     0    0          0 )
             ( −U   −U    0    0     0    0          0 )                ( −U   −3U/2  0    0     0    3U/8       0 )
             ( 0    0     C    0     0    0          0 )                ( 0    0      C    0     0    0          0 )
             ( 0    −2U   0    −2U   0    C          0 )                ( 0    −3U    0    −2U   0    3C/2+3U/4  0 )
             ( 0    0     C−U  0     −U   0          0 )                ( 0    0      C−U  0     −U   0          0 )
             ( 2C   0     0    0     0    C          0 )                ( 2C   0      0    0     0    3C/2       0 )
             ( 0    0     0    0     0    0          0 )                ( 0    0      0    0     0    0          0 )

the matrix at n = 3 being [Hin23a, (2.11)]. In both dimensions π_C A_(E_C,E_Υ) = π_C A_(E_C,E_Υ)π_C, with
π_C := (00, 0a, tr): the rows 00, 0a, tr involve only the columns 00, 0a, tr. The matrix is block lower triangular with
respect to ran π_CΥ ⊕ ran π̸₀ ⊕ ran π₁₁, π_CΥ := (00, 01, 0a, 1a, tr); the eigenvalues on π_CΥ are 2C, C, C, −U, −U
at n = 3 ([Hin23a, (2.15a)–(2.15b)]) and 2C, C, 3C/2, −3U/2, −U at n = 4, that on π̸₀ is 0 and that on π₁₁ is −2U.
With the adjoint taken for the fibre inner products of η,

    G⁻¹A^*_(E_C,E_Υ)G = −A_(E_Υ,E_C),                                                                   {#eq:s17-duality}

A_(E_Υ,E_C) denoting [[eq:s17-hin23a-a]] with γ_C and γ_Υ exchanged: [Hin23a, Remark 2.3], where G⁻¹ = G, at n = 3;
at n = 4, G⁻¹ = I − ⅓η tr_η ≠ G.

(5) For g := −½(dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰) + r²(g̸ + r^(−k)χ(x¹)T), T a trace-free symmetric 2-tensor on 𝕊^(n−1) with
|T|²_g̸ = 2 (for instance dθ₁² − sin²θ₁ dθ₂²), the part of R₁₁(g) quadratic in χ′ is ½r^(−2k)χ′(x¹)²: r⁻² at n = 3,
r⁻³ at n = 4. The first-order terms r⁻¹A∂₁ of P′ applied to r^(−k)h, h a frame component of size 1 with ∂₁h of size
1, are of size r^(−(1+k)); relative to these the quadratic term has the factor r^(1−k): 1 at n = 3, where
−½|∂₁π̸₀h|² enters the leading term of h₁₁ ([Hin23a, (3.47), Remark 3.38]), and r^(−1/2) at n = 4.

(6) The least integer above ½ dim M = (n + 1)/2 is 3 at n = 3 and at n = 4 (the Sobolev order 3 of [Hin23a,
Notation 3.22]: H^l_b ⊂ L^∞ for l ≥ 3); the least integer above (dim M − 1)/2, the number d_(dim M−1) of [Hin23a,
Lemma 3.33], is 2 at n = 3 and 3 at n = 4.

(7) Let P(g) := Ric(g) − δ^*_(η,E_C)Υ(g; η), Υ(g; η)_m := g_(mq)g^(ab)(Γ(g)^q_(ab) − Γ(η)^q_(ab)), the operator of
[Hin23a, (3.30)] but for its γ_Υ term, which is linear in g − η and so has no part bilinear in the perturbation. For g
:= η + r^(−k)h + r^(−k)f(x¹)U, with h one of the frame components
h_(ab) = χ(x¹)T_(ab) or h₁₁ = ζ(x¹) and U a frame component of size 1, let L₂(h, u) be the part of 2r^(k+1)P(g) (in
frame components) bilinear in (h, u), u := f U, in which both derivatives fall on the profiles χ, ζ, f. Then, with T̂
the frame components of T:

- U = (dx⁰)², h_(ab) = χT_(ab), output tf: L₂ = 4r^(1−k)(χ′f′ + χ″f)T̂;
- U = T, h_(ab) = χT_(ab), output 11: L₂ = −2r^(1−k)χ′f′, with no term χ″f;
- U = (dx⁰)², h₁₁ = ζ, output 11: L₂ = 4r^(1−k)ζ″f, with no term ζ′f′.

These are the entries A(7, 1) (on ∂₁u) and B(7, 1) (on u), A(4, 7) and B(4, 1) of [Hin23a, Proposition 3.29] in this
normalisation. At n = 3 they are independent of r, and they are twice the entries printed there, A(7, 1) = 2∂₁h_(ab),
B(7, 1) = 2ρ₀⁻¹∂₁²h_(ab), A(4, 7) = −½∂₁h_(ab) and B(4, 1) = 2ρ₀⁻¹∂₁²h₁₁, the entry A(4, 7), which maps the trace-free
block to the 11-block, being read as acting by contraction, −½∂₁h_(ab)u^(ab) with |T|² = 2. At n = 4 they are the same
numbers times r^(1−k) = r^(−1/2). Each is linear in h.

(8) ([Hin23a, Lemma 3.6] at n = 4.) Let f := 1 − m/r², r* as in (1), and x⁰ = t + r*, x¹ = t − r*,
ρ₀ = 1/(r* − t), ρ_I = (r* − t)/r (the tortoise coordinates of [Hin23a], which differ from those of
[[eq:iii-c-1-2]]) for the Tangherlini metric g_m = −(f/2)(dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰) + r²g̸. Then dρ₀ = ρ₀²dx¹ is null,
and

    g_m⁻¹(r dρ_I, r dρ_I) = (2x¹/r)(1 + x¹f/(2r)),                                                    {#eq:s17-hin23a-38}

[Hin23a, (3.8)] with f in place of 1 − 2m/r. With x̄_I := min(√3/2, 1/(2m^(1/4))) in place of the min(√3/2, 1/√(8m)) of
[Hin23a], on {ρ₀ < 2, 0 < x_I < x̄_I} one has r = ρ₀⁻¹x_I⁻² > ½x̄_I⁻² ≥ 2√m, twice the horizon radius √m, as 4m is twice
the Schwarzschild horizon radius 2m: there r* is defined, f > ¾ (½ in [Hin23a]), x¹/r = −x_I² < 0 and |x¹f/(2r)| < 3/8,
so [[eq:s17-hin23a-38]] is negative.

*Proof.* (1) For η, √|η| = ½r^(n−1)√|g̸| and η⁻¹ has the entries η^(01) = η^(10) = −2 and r⁻²g̸⁻¹. For u = u(x⁰, x¹),
□u = −|η|^(−1/2)∂_i(|η|^(1/2)η^(ij)∂_ju) = 2r^(1−n)(∂₀(r^(n−1)∂₁u) + ∂₁(r^(n−1)∂₀u)), and with ∂₀r = ½, ∂₁r = −½,

    □u = 4∂₀∂₁u + (n − 1)r⁻¹(∂₁u − ∂₀u).

For u = r^(−k)v: ∂₀u = r^(−k)(∂₀v − (k/2)r⁻¹v), ∂₁u = r^(−k)(∂₁v + (k/2)r⁻¹v), and
4∂₀∂₁u = r^(−k)(4∂₀∂₁v + 2kr⁻¹(∂₀v − ∂₁v) − (k² + k)r⁻²v). Adding (n − 1)r^(−k−1)(∂₁v − ∂₀v + kr⁻¹v),

    r^k□r^(−k)v = 4∂₀∂₁v + (2k − (n − 1))r⁻¹(∂₀v − ∂₁v) + (k(n − 1) − k² − k)r⁻²v.

As 2k = n − 1 the first-order term vanishes, and k(n − 1) − k² − k = k(k − 1) = (n − 1)(n − 3)/4. For r*:
d/dr (√m/2)(log(r − √m) − log(r + √m)) = (√m/2)·2√m/(r² − m) = m/(r² − m), and 1 + m/(r² − m) = 1/f. For r > √m,
log((r − √m)/(r + √m)) = log((1 − s)/(1 + s)) = −2Σ_(j≥0) s^(2j+1)/(2j + 1) with s := √m/r < 1, which gives
[[eq:s17-rstar]].

(2) With r = (ρ₀ρ_I)⁻¹ and t = r − ρ₀⁻¹: ∂r/∂ρ₀ = −ρ₀⁻²ρ_I⁻¹, ∂r/∂ρ_I = −ρ₀⁻¹ρ_I⁻², ∂t/∂ρ₀ = ∂r/∂ρ₀ + ρ₀⁻² and
∂t/∂ρ_I = ∂r/∂ρ_I. The Jacobian determinant of (t, r) in (ρ₀, ρ_I) is (∂t/∂ρ₀)(∂r/∂ρ_I) − (∂t/∂ρ_I)(∂r/∂ρ₀) =
ρ₀⁻²∂r/∂ρ_I = −ρ₀⁻³ρ_I⁻². So |dη| = r^(n−1)|dt dr dg̸| = r^(n−1)ρ₀⁻²ρ_I⁻¹|(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|
= ρ₀^(−(n+1))ρ_I^(−n)|(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|. For the symmetry: ρ_Iρ^(−(2+k))ρ₀^(n+1)ρ_I^n = ρ^(n+1−2−k) = ρ^k, as
ρ₀ρ_I = ρ and n − 1 = 2k; so ⟨Lu, v⟩_(L²(μ_b)) = 2∫ P′(ρ^ku)(ρ^kv)|dg_m|, which is symmetric in u and v when P′ is.

(3) Write s₀ := log ρ₀, s_I := log ρ_I, D₀ := ∂_(s₀) = ρ₀∂_(ρ₀), D_I := ∂_(s_I), Λ := Δ̸ + q_n, so
L₀ = −2D_I(D₀ − D_I) + e^(s_I)Λ, V = D₀ − (1 + c)D_I and w² = e^φ, φ := −2α₀s₀ − 2α_Is_I. The density ds₀ ds_I dg̸ is
invariant under the constant-coefficient field V, so div W = V(w²) = w²(−2α₀ + 2(1 + c)α_I). Next
[L₀, W] = [L₀, w²]V + w²[L₀, V]. Since V(e^(s_I)) = −(1 + c)e^(s_I) and Λ commutes with D₀, D_I,
[L₀, V] = (1 + c)e^(s_I)Λ. From D₀w² = −2α₀w², D_Iw² = −2α_Iw²,

    [D_I(D₀ − D_I), w²] = w²(−2α_ID₀ + (4α_I − 2α₀)D_I + 4α_I(α₀ − α_I)),

so [L₀, w²] = w²(4α_ID₀ + (4α₀ − 8α_I)D_I − 8α_I(α₀ − α_I)). Hence

    [L₀, W] − (div W)L₀ = w²((4α_ID₀ + (4α₀ − 8α_I)D_I − 8α_I(α₀ − α_I))V + (1 + c)e^(s_I)Λ
                              − (−2α₀ + 2(1 + c)α_I)(−2D_I(D₀ − D_I) + e^(s_I)Λ)).

Collecting the terms of order two: D₀² has the coefficient 4α_I; D₀D_I has −4α_I(1 + c) + 4α₀ − 8α_I − 4α₀ +
4(1 + c)α_I = −8α_I; D_I² has −(1 + c)(4α₀ − 8α_I) + 4α₀ − 4(1 + c)α_I = 4α_I − 4c(α₀ − α_I). So the second-order part
in (D₀, D_I) is 4α_I(D₀ − D_I)² − 4c(α₀ − α_I)D_I², and the angular part is
(1 + c + 2α₀ − 2(1 + c)α_I)e^(s_I)Λ = (1 + 2(α₀ − α_I) + c(1 − 2α_I))x_I²Λ. With D₀ ↦ iξ₀, D_I ↦ iξ_I and
Λ ↦ λ + q_n this is [[eq:s17-energy-form]]. On functions of ω alone, VD-terms and L₀'s first term vanish, which gives
the last statement.

(4) Let t_U := tr̸U/(n − 1), so tr_ηU = −4U₀₁ + (n − 1)t_U. Then (GU)₀₀ = U₀₀, (GU)₀₁ = (n − 1)t_U/4,
(GU)_(0a) = U_(0a), (GU)₁₁ = U₁₁, (GU)_(1a) = U_(1a), and tr GU = −((n − 1)/2)tr U. Since η⁻¹dx¹ = −2∂₀,
w = δ₁GU = 2GU(∂₀, ·): w₀ = 2U₀₀, w₁ = (n − 1)t_U/2, w_a = 2U_(0a). With c = ½(dx⁰ + dx¹) and
⟨c, w⟩ = −(w₀ + w₁), the first term of [[eq:s17-hin23a-a]] has the components (00) γ_Cw₀ = 2γ_CU₀₀,
(01) γ_C(½(w₀ + w₁) − ½(w₀ + w₁)) = 0, (11) γ_Cw₁, (0a) and (1a) γ_CU_(0a), and tangential block
γ_C(w₀ + w₁)r²g̸, so its trace coordinate is γ_C(2U₀₀ + (n − 1)t_U/2) and its trace-free part 0. In the second term,
η⁻¹c = −∂₀ − ∂₁ and β := γ_Υ(2ι_(η⁻¹c)GU − c tr GU) has β₀ = γ_Υ(−2U₀₀ − (n − 1)U₀₁ + ((n − 1)(n − 3)/4)t_U),
β₁ = γ_Υ(−2U₁₁ − (n − 1)U₀₁ + ((n − 1)(n − 3)/4)t_U), β_a = −2γ_Υ(U_(0a) + U_(1a)); and δ₁^*β = dx¹ ⊗_s β has the
components (01) ½β₀, (11) β₁, (1a) ½β_a and no others. Altogether

    (00) 2γ_CU₀₀,   (01) −γ_ΥU₀₀ − ((n − 1)/2)γ_ΥU₀₁ + ((n − 1)(n − 3)/8)γ_Υt_U,   (0a) γ_CU_(0a),
    (11) −(n − 1)γ_ΥU₀₁ − 2γ_ΥU₁₁ + ((n − 1)/2)(γ_C + ((n − 3)/2)γ_Υ)t_U,   (1a) (γ_C − γ_Υ)U_(0a) − γ_ΥU_(1a),
    (tr) 2γ_CU₀₀ + ((n − 1)/2)γ_Ct_U,   (tf) 0,

which at n = 3 and n = 4 are the two matrices. The block statements and eigenvalues are read off them: the rows 00,
0a, tr have entries only in the columns 00, 0a, tr; the rows of π_CΥ have no entries in the columns tf and 11; and the
blocks are triangular. For [[eq:s17-duality]]: write e(w) := 2c ⊗_s w − η⟨c, w⟩ and d(U) := 2ι_(η⁻¹c)U − c tr U.
For the fibre inner products, ⟨2c ⊗_s w, U⟩ = 2U(η⁻¹c, η⁻¹w) and ⟨η, U⟩ = tr U, so ⟨e(w), U⟩ = ⟨w, d(U)⟩: d = e^*.
Likewise ⟨dx¹ ⊗_s w, U⟩ = ⟨w, ι_(η⁻¹dx¹)U⟩, so (δ₁^*)^* = −δ₁, and G is symmetric. With
A_(E_C,E_Υ) = γ_C eδ₁G + γ_Υ δ₁^*e^*G, A^*_(E_C,E_Υ) = −γ_C Gδ₁^*e^* − γ_Υ Geδ₁, and
G⁻¹A^*_(E_C,E_Υ)G = −(γ_Cδ₁^*e^*G + γ_Υeδ₁G) = −A_(E_Υ,E_C). G is invertible: as tr_ηη = n + 1,
(I − (1/(n − 1))η tr)(I − ½η tr) = I, so G⁻¹ = I − (1/(n − 1))η tr, which is G exactly when n = 3.

(5) For a metric g = g_(AB)dx^Adx^B + q_(ab)dθ^adθ^b with g_(AB) constant (A, B ∈ {0, 1}, g^(11) = 0), the field ∂₁ is
null and geodesic, Γ^a_(11) = 0, Γ^a_(1a) = ½q^(ab)∂₁q_(ab), and Γ^a_(1b) = ½q^(ac)∂₁q_(cb) on the angular indices, so

    R₁₁ = −∂₁Γ^a_(1a) − Γ^a_(1b)Γ^b_(1a) = −½q^(ab)∂₁²q_(ab) + ¼q^(ac)q^(bd)∂₁q_(ab)∂₁q_(cd).

For q = r²(g̸ + εT), ε := r^(−k)χ(x¹), the terms quadratic in χ′ come only from the last term, whose part quadratic in
∂₁ε is ¼r⁻⁴r⁴(∂₁ε)²|T|²_g̸ = ½(∂₁ε)², with ∂₁ε = r^(−k)χ′ + (k/2)r^(−k−1)χ; this gives ½r^(−2k)χ′². The rest is
arithmetic: ½r^(−2k) = r^(1−k) · ½r^(−(1+k)).

(6) (n + 1)/2 is 2 at n = 3 and 5/2 at n = 4; n/2 is 3/2 at n = 3 and 2 at n = 4.

(7) *Reduction.* Each term of P(g) has two derivatives in all. A term bilinear in (h, u) with both derivatives on the
profiles receives none on the weights r^(−k), on the components of η or on the angular frame. The γ_C part of
δ^*_(η,E_C) is of order zero on Υ, which has one derivative, so it contributes no such term; neither do the Christoffel
symbols of η. As the profiles depend on x¹ alone, only ∂₁ acts on them. So L₂ is 2r^(k+1) times the part bilinear in
(h, u) of P for the model in which η has constant frame components, η = −½(dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰) + Σ_a(e^a)², and the
perturbation κ = εr^(−k)h + s r^(−k)u depends on x¹ alone (r frozen), with Γ(η) = 0. In this model,
Γ_(d,ij) = ½(δ_(i1)κ′_(dj) + δ_(j1)κ′_(di) − δ_(d1)κ′_(ij)), Γ^a_(ij) = g^(ad)Γ_(d,ij), Γ^p_(pi) = ½δ_(i1)τ′ with
τ′ := tr_g κ′, Υ_m = g^(ab)Γ_(m,ab) = g^(1b)κ′_(mb) − ½δ_(m1)τ′, (δ^*Υ)_(ij) = ½(δ_(i1)Υ′_j + δ_(j1)Υ′_i), and
R_(ij) = ∂₁Γ¹_(ij) − δ_(j1)∂₁Γ^p_(pi) + Γ^p_(pq)Γ^q_(ij) − Γ^p_(jq)Γ^q_(pi).

*U = (dx⁰)², h_(ab) = χT_(ab).* Put φ := κ₀₀ and A_(ab) := κ_(ab). For angular a, b, Γ_(d,ab) = −½δ_(d1)A′_(ab), so
Γ¹_(ab) = −½g^(11)A′_(ab), and g^(11) = −4φ + O(κ²); hence ∂₁Γ¹_(ab) = 2(φA′_(ab))′ + O(κ³). The second term of R_(ab)
vanishes (b is angular), the third is cubic (Γ¹_(ab) is quadratic), and in the fourth the factors linear in κ involve
only A, so it has no part bilinear in (φ, A). The gauge term (δ^*Υ)_(ab) vanishes. So the bilinear part of P_(ab) is
2φ′A′_(ab) + 2φA″_(ab).

*U = T, h_(ab) = χT_(ab).* Now κ is purely angular, κ = A + B with A ∝ χ and B ∝ f, so g^(11) = 0, g^(10) = −2 and
Γ_(d,11) = 0. Then Γ^a_(1b) = ½(q⁻¹κ′)^a_b on the angular indices (q := δ + κ there), R₁₁ = −½τ″ − ¼tr((q⁻¹κ′)²),
Υ₁ = −½τ′ (as g^(1b)κ′_(1b) = −2κ′_(10) = 0), and (δ^*Υ)₁₁ = −½τ″. So P₁₁ = −¼tr((q⁻¹κ′)²), whose part bilinear in
(A, B) is −½Σ_(ab)A′_(ab)B′_(ab).

*U = (dx⁰)², h₁₁ = ζ.* Put a := κ₁₁, φ := κ₀₀. The (x⁰, x¹)-block of g is ((φ, −½), (−½, a)), so
g^(11) = −4φ, g^(00) = −4a and g^(01) = −2 modulo quadratic terms. The nonzero Γ_(d,1q) are Γ_(0,10) = ½φ′ and
Γ_(1,11) = ½a′, so at linear order Γ⁰_(11) = −a′ and Γ¹_(10) = −φ′, and Σ Γ^a_(1b)Γ^b_(1a) = 2a′φ′ at bilinear order.
Further Γ¹_(11) = ½g^(11)a′ = −2φa′ and τ′ = g^(00)φ′ + g^(11)a′ = −4(aφ)′ at bilinear order, and
Γ^a_(ab)Γ^b_(11) is of order four. So R₁₁ = −2(φa′)′ + 2(aφ)″ − 2a′φ′ = 2aφ″. And Υ₁ = g^(11)a′ − ½τ′ = 2aφ′ − 2φa′,
so (δ^*Υ)₁₁ = 2aφ″ − 2φa″. Hence the bilinear part of P₁₁ is 2φa″.

*The values.* With the frame components A = εr^(−k)χT̂, B = s r^(−k)fT̂, φ = s r^(−k)f and a = εr^(−k)ζ, and
Σ T̂_(ab)T̂_(ab) = 2, the bilinear parts are 2r^(−2k)(χ′f′ + χ″f)T̂, −r^(−2k)χ′f′ and 2r^(−2k)fζ″; multiplied by
2r^(k+1) they are the three values stated. At n = 3, k = 1, they are 4(χ′f′ + χ″f)T̂, −2χ′f′ and 4ζ″f, independent of
r; at n = 4 they carry r^(1−k) = r^(−1/2).

(8) −f dt² + f⁻¹dr² = −f(dt² − dr*²) = −(f/2)(dx⁰ ⊗ dx¹ + dx¹ ⊗ dx⁰), so g_m⁻¹(dx⁰, dx¹) = −2/f and
g_m⁻¹(dx⁰, dx⁰) = g_m⁻¹(dx¹, dx¹) = 0. As r* − t = −x¹, ρ₀ = −1/x¹ and dρ₀ = ρ₀²dx¹, which is null. With
ρ_I = −x¹/r and dr = f dr* = (f/2)(dx⁰ − dx¹), r dρ_I = −dx¹ + (x¹/r)dr = (x¹f/(2r))dx⁰ − (1 + x¹f/(2r))dx¹, so
g_m⁻¹(r dρ_I, r dρ_I) = 2(x¹f/(2r))(−(1 + x¹f/(2r)))(−2/f) = (2x¹/r)(1 + x¹f/(2r)). Since r = (ρ₀ρ_I)⁻¹ = ρ₀⁻¹x_I⁻²,
on {ρ₀ < 2, x_I < x̄_I} we have r > ½x̄_I⁻² ≥ ½(2m^(1/4))² = 2√m, so r* is defined and f = 1 − m/r² > 1 − ¼ = ¾. And
x¹/r = −ρ_I = −x_I² < 0, |x¹f/(2r)| = ½x_I²f < ½x̄_I² ≤ 3/8, so 1 + x¹f/(2r) > 5/8 > 0 and [[eq:s17-hin23a-38]] is
negative. ∎
