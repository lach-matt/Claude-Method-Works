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

Two propositions close the first and second steps and are used in [[ch:s26]]. [[prop:np-10-38]] collects the operator
at null infinity in dimension 4 + 1, entry by entry, and what it gives for the order at which a radiative term at null
infinity reaches future timelike infinity. [[prop:np-10-64]] gives the quantities through which the spatial dimension
enters [Hin23a, Section 3], the energy estimates near null and spatial infinity that [[ch:s26]] carries to dimension
4 + 1.

The notation is that of [[ch:s11]]–[[ch:s16]]. In particular n = 4, D = 5; the family g_b, b = (μ, A) ∈ ℬ, of
[[sec:iii-b-3]], with μ₀, R₁ = μ₀^(1/2), the compactification M and its faces I₀, ℐ⁺, ι⁺, K⁺ ([[def:iii-b-2-1]]); the
gauge-fixed operator of [[sec:iii-b-6]]; the linearised operator L_b and its Minkowski model L̄ of [[ch:s15]], with the
endomorphism S̄ of [[lem:iii-f-2-1]] and its spectrum [[eq:iii-f-3-1]]; and the index sets and partially polyhomogeneous
spaces of [[sec:iii-a-1]]. No result of this chapter involves the inner radius r₀ of the spaces of [[ch:s01]]: the
exterior region below is a neighbourhood of I₀ ∪ ℐ⁺ of radius at least 4R₁, and the results at ι⁺ and at the transition
face concern faces at infinity. So every result holds for each choice of the radii at which the hypotheses of
[[ch:s05]] hold.

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

Throughout this part: n = 4, D = 5; the family g_b, b = (μ, A) ∈ ℬ, of [[sec:iii-b-3]], with μ₀, R₁ = μ₀^(1/2), the
compactification M and its faces I₀, ℐ⁺, ι⁺, K⁺ ([[def:iii-b-2-1]]); the time functions t_* = t − ψ(|x|) and t_IVP
([[eq:iii-b-3-6]], [[lem:iii-b-3-7]]), with t_* = t − |x| + C′ − 8μ₀|x|⁻¹ on {|x| ≥ 3R₁}; and the gauge parameters of
[[sec:iii-f-1]], with, in addition,

    0 < γ_Υ < 1/4,     0 < e_Υ < 1.                                                                     {#eq:iii-c-1-1}

(The conditions [Hin26, (5.42)], v_C < 1, 0 < e_C < 1, γ_C > 0, 0 < e_Υ < 1, γ_Υ > 0, hold under the choices of
[[sec:iii-f-1]].) Let η := −dt² + dx² in the coordinates of [[sec:iii-b-2]], and

    x⁰ := t + |x|,     x¹ := t − |x|,     ρ₀ := 1/(2 − x¹),     ρ_I := (2 − x¹)/|x|,                       {#eq:iii-c-1-2}

the last two being the coordinates [[eq:iii-b-2-2]] near I₀ ∩ ℐ⁺. (Here x⁰ is that of Minkowski space; the x⁰ of
[[eq:iii-b-4-1]] for g_μ is t + |x| − T_μ(|x|), and the two null frames differ by I + ρ²C^∞, [[lem:iii-c-1-3]].) Fix
T₀ := C′ + 1 − 2R₁ and set

    Ω_ext := cl_M{t_* ≤ T₀},     U := Ω_ext ∩ {|x| ≥ 4R₁}.                                               {#eq:iii-c-1-3}

([Hin26, (5.1)] fixes T and shifts it to 1; the choice of T₀ only makes [[eq:iii-c-1-2]] global on U.) On U,
x¹ = t_* − C′ + 8μ₀|x|⁻¹ ≤ T₀ − C′ + 2R₁ = 1, since μ₀ = R₁².

**Lemma {#lem:iii-c-1-1}** (The corner coordinates.) (1) (ρ₀, ρ_I, ω), ω = x/|x|, are coordinates on all of U, smooth
up to I₀ and ℐ⁺: ρ₀ ∈ [0, 1], ρ₀ = 0 exactly at I₀, ρ_I = 0 exactly at ℐ⁺, and ρ₀ρ_I = |x|⁻¹. (2) With
X₀ := ρ₀∂_(ρ₀), X_I := ρ_I∂_(ρ_I) (at fixed ω and the other coordinate), exactly on U,

    ∂_(t_*)|_(ρ,ω) = ρ₀(X₀ − X_I),     ρ∂_ρ|_(t_*,ω) = X_I + 8μ₀ρ₀²ρ_I(X₀ − X_I),     ρ := |x|⁻¹,         {#eq:iii-c-1-4}

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
t_* = 2 − ρ₀⁻¹ + C′ − 8μ₀ρ₀ρ_I and ρ = ρ₀ρ_I: X₀t_* = ρ₀⁻¹ − 8μ₀ρ, X_I t_* = −8μ₀ρ, X₀ρ = X_Iρ = ρ. So ρ₀(X₀ − X_I) maps
t_* ↦ 1, ρ ↦ 0; and X_I + α(X₀ − X_I) with α := 8μ₀ρ₀²ρ_I maps ρ ↦ ρ and t_* ↦ −8μ₀ρ + αρ₀⁻¹ = 0. For
[[eq:iii-c-1-5]]: ∂₀|x| = ½, ∂₁|x| = −½, ∂₀x¹ = 0, ∂₁x¹ = 1; so ∂₀ρ₀ = 0, ∂₀ρ_I = −½ρ₀ρ_I², ∂₁ρ₀ = ρ₀²,
∂₁ρ_I = −ρ₀ρ_I + ½ρ₀ρ_I², which is [[eq:iii-c-1-5]]. The memberships: ∂_t = ∂₀ + ∂₁, ∂_(|x|) = ∂₀ − ∂₁,
∂_(x^i) = ω^i∂_(|x|) + |x|⁻¹(…)∂_ω, and |x|⁻¹∂_ω = ρ₀ρ_I∂_ω with ∂_ω (at fixed ρ₀, ρ_I) a b-vector field. ∎

For the null coordinates of the Tangherlini metric of mass μ ([[eq:iii-b-4-1]]–[[eq:iii-b-4-2]]), with ρ₀, ρ_I defined by
[[eq:iii-c-1-2]] from their x¹ and |x|, the same calculation with ∂₀|x| = f/2, ∂₁|x| = −f/2, f := 1 − μ|x|⁻², gives
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

    (h₀₀, h_(0ā), ⅓tr̸h, h₀₁, h_(1ā), π̸₀h, h₁₁),     tr̸h := g̸^(ab)h_(āb̄),                                 {#eq:iii-c-1-7}

the third being the coefficient of |x|²g̸. Each of these is the coefficient of the basis element of the corresponding
summand: for instance the element 2dx⁰dx¹ of the fourth summand has h₀₁ = 1, as dx⁰(∂₀) = dx¹(∂₁) = 1 and
dx⁰(∂₁) = dx¹(∂₀) = 0.

**Definition {#def:iii-c-1-2}** ([Hin26, Definition 5.2] in dimension 4 + 1.) π_C h := (h₀₀, h_(0ā), tr̸h),
π₀₁h := h₀₁, π_(1/)h := h_(1ā), π̸₀h := h_(āb̄) − ⅓(tr̸h)g̸_(ab), π₁₁h := h₁₁. (The factor ⅓ replaces the ½ of [Hin26]:
π̸₀h is the trace-free part on 𝕊³.)

**Lemma {#lem:iii-c-1-3}** (Frames.) Three smooth frames of S²T* on U are used: the products of the Cartesian dt, dx^i;
those of dt_*, dx^i ([[ch:s15]]); and the rescaled null frame of [[eq:iii-c-1-6]]. Each is related to the next by a
smooth bundle map with smooth inverse, of the form F₀(ω)(I + ρ²C^∞(U)) with F₀ depending on ω alone.

*Proof.* dt_* = dt − ψ′(|x|)d|x| with ψ′ = 1 − 8μ₀|x|⁻² on U, so dt_* = dx¹ + 8μ₀|x|⁻²d|x|. Further d|x| = ω_i dx^i,
and |x|e^a is the orthonormal tangential projection of dx; both depend on ω alone. Finally dx⁰ = dt + d|x| and
dx¹ = dt − d|x|. ∎

So the spaces below, which are defined slot by slot in [[eq:iii-c-1-6]], do not depend on which of the null frames of
η, of g_μ ([[eq:iii-b-4-2]]) or of ḡ ([[ch:s15]]) is used: these differ by I + ρ²C^∞, and ρ² = ρ₀²ρ_I² moves the index
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

