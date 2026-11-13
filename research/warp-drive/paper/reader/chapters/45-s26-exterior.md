# Part. The stability theory, V: the exterior, the nonlinear theorem, gluing and linear stability {#part:stability-nonlinear}

## The exterior region: estimates at null and spatial infinity, the exterior solution, partial polyhomogeneity and boosts {#ch:s26}

This chapter solves the gauge-fixed Einstein equation near spatial infinity I₀ and future null infinity ℐ⁺, for small
data on the part of the initial surface Σ_IVP outside a large ball, and describes the solution there. It is [Hin26,
Sections 5.4–5.7] (Lemma 5.16, Theorem 5.17 with (5.52)–(5.53), Remarks 5.18 and 5.20, Theorem 5.21 with Remark 5.22,
Theorem 5.23 with the cut-off gauge (5.75)–(5.76), Remark 5.24, Proposition 5.25, Section 5.7.1, Remark 5.26 and
Example 5.27; pp. 99–113) in dimension 4 + 1, together with [Hin23a, Section 3] (pp. 9–32), on whose energy estimates
[Hin26, Theorem 5.17] rests, written out in dimension 4 + 1 for the gauge-fixed operator of [[sec:iii-c-4]].

[[sec:iii-c1-1]] fixes the exterior domain Ω_(ext,r₀) and shows that its boundary hypersurfaces are spacelike for every
small perturbation of g_(b₀). [[sec:iv-0]]–[[sec:iv-4]] are [Hin23a, Sections 3.1–3.2]: the edge-b structure at ℐ⁺,
the conjugated scalar wave operator, the basic energy estimate near ℐ⁺ ([[prop:iv-3-1]]) and the b-energy estimate near
the interior of I₀ ([[prop:iv-4-1]]). [[sec:iv1-0]]–[[sec:iv1-2]] are [Hin23a, Sections 3.4–3.5] for the tensor
operator: its edge-b form ([[prop:iv1-1-2]]) and the energy estimate for the system with its tame form
([[prop:iv1-2-2]]). [[sec:iv2-0]]–[[sec:iv2-3]] are [Hin23a, Section 3.6]: the Cauchy problem near I₀ in both
directions, the linear exterior estimate with the sharp weight at ℐ⁺ ([[thm:iv2-2-4]]) and the nonlinear exterior
solution ([[thm:iv2-3-1]]). [[sec:iii-c1-2]] states the result as [Hin26, Theorem 5.17] in dimension 4 + 1
([[thm:iii-c1-2-1]]) and proves the propagation of the gauge condition and of the vacuum equation
([[prop:np-10-57-d]]). [[sec:iii-c2-2]] and [[sec:iv2-4]] introduce the cut-off gauge of [Hin26, (5.76)] and show that
the estimates hold in it. [[sec:iii-c1-3]] proves partial polyhomogeneity of the exterior solution ([[thm:iii-c1-3-1]]),
and [[sec:iii-c2-1]]–[[sec:iii-c2-4]] treat boosted backgrounds and data ([[thm:iii-c2-3-1]]) and gauged Cauchy data
([[prop:iii-c2-4-1]]).

*What dimension 4 + 1 changes.* (1) *Weights.* Radiation fields decay like |x|^(−3/2) ([[rem:s17-dimension]] (a)), so
every weight at ℐ⁺ is shifted by ½: the condition 1 < ℓ^♭_I < min(ℓ^♭₀, 1 + (1 − e_Υ)γ_Υ, 3/2) of [Hin26, (5.49)]
becomes [[eq:iii-c1-1-1]]. (2) *No subtraction.* [Hin26, Theorem 5.21, Step 2] measures h from g_(b₀) + h₀, h₀ carrying
the radiation fields of π̸₀h and π₁₁h, because in dimension 3 + 1 these enter the leading part of the operator at ℐ⁺.
In dimension 4 + 1 the leading part is the constant matrix Ā and all of the perturbation lies in the error
([[prop:iii-c-4-4]]); so the equation is integrated directly ([[rem:iii-c1-3-2]]). (3) *Half steps.* The error gains ½
at ℐ⁺ in place of min(α_I − 1, (1 − e_Υ)γ_Υ), so each step of the proof of [[thm:iii-c1-3-1]] raises the weight at ℐ⁺
by any ν < ½. (4) *The index condition at I₀* is min Re ℰ₀ > 3/2 + 2γ_Υ, so that ℰ₀ ⊂ ℰ_I^C is compatible with
[[def:iii-c-3-1]] (2). (5) *The energy estimates.* The conjugation that removes the first-order term of the scalar wave
operator is by ρ^(3/2), the density is ρ₀⁵ρ_I⁴|dg|, and the conjugated operator carries ¾ with the spherical
Laplacian, which only increases the positive angular term of the energy identity. In the Minkowski null coordinates of
[[sec:iii-c-1]] the mass enters only through the error class, the first-order matrix of the conjugated tensor operator
at ℐ⁺ is the constant Ā, free of the perturbation, and its diagonal is nonnegative; so the sharp weights
α_I < min(α₀, 0) need no separate argument, the decay at ℐ⁺ is recovered in two integrations, and only the slot π̸₀
carries a radiation field. The estimate near the interior of I₀, for which [Hin23a] cites [HV20, Proposition 4.3], is
proved in [[prop:iv-4-1]]. (6) *Boosts.* The past slab of Ω_(ext,r₀) has the slope 1/12, so that the cut-off boosts of
[[sec:iii-b-5]] are genuine boosts on all of it ([[lem:iii-c2-1-1]]); the time function differs from Boyer–Lindquist
time by a function smooth in |x|⁻¹, so the Cauchy data acquire no logarithms ([[prop:iii-c2-4-2]]); part (1) of
[[thm:iii-c2-3-1]] needs the constraints, as the operator δ*_(g₀,E_C) is not natural under boosts; and the size of the
boost is made independent of r₀ by r₁ := 2r₀.

*Notation and the inner radius.* n = 4, D = 5. The notation is that of [[ch:s11]] and [[ch:s17]]: the family g_b,
b = (m, A) ∈ ℬ, with b₀ = (m₀, 0) and R₁ = m₀^(1/2); the time functions t_* and t_IVP of [[sec:iii-b-3]], with
t_IVP = t − C″ on {|x| ≥ R₃} ([[lem:iii-b-3-7]] (b)); the gauge-fixed operator P(g, g₀) of [[eq:iii-b-6-4]] and its
linearisation L^(g,g₀) of [[eq:iii-c-4-1]], with the gauge parameters of [[sec:iii-f-1]] and [[eq:iii-c-1-1]], so
0 < γ_Υ < ¼, 0 < e_Υ < 1, 0 < e_C, v_C < 1 and (1 − e_C)(1 − v_C)γ_C > 100; the coordinates [[eq:iii-c-1-2]], the
corner coordinates (ρ₀, ρ_I, ω) on U ([[eq:iii-c-1-3]], [[lem:iii-c-1-1]]), X₀ := ρ₀∂_(ρ₀), X_I := ρ_I∂_(ρ_I),
ρ := ρ₀ρ_I = |x|⁻¹, and r := |x|; the splitting [[eq:iii-c-1-6]] with its slots 1–7 ([[def:iii-c-1-2]]), the matrix Ā
of [[lem:iii-c-4-2]] with diagonal [[eq:iii-c-4-3]], the set σ_Υ = {0, (1 − e_Υ)γ_Υ, γ_Υ, 2γ_Υ}, the background class 𝒢
([[def:iii-c-3-4]]), and the partially polyhomogeneous spaces and classes of [[sec:iii-c-2]], [[sec:iii-c-3]] and
[[sec:iii-c-5]]. Index sets and their operations are those of [[def:s11-b-analysis]]. Unless stated otherwise the
weights at ℐ⁺ are powers of ρ_I, and the b-spaces are taken with the b-density, so that by b-Sobolev embedding (order
k > 5/2) a weight is the pointwise order. A vector field on 𝕊³ is written Θ. In this chapter r₀ is the exterior radius
of [Hin26, Lemma 5.16], not the radius of the artificial boundary of [[sec:i-a-1-1]]. The inner radius r_♭ ∈ (0, ½R₁]
of the spacetime ([[sec:iii-b-2]]) enters this chapter only through the constants C′ of t_* and C″ of t_IVP near
infinity: the exterior domain lies in {|x| ≥ r₀} with r₀ large, and no step reaches the inner boundary. So every result
of the chapter holds for each r_♭ ∈ (0, ½R₁], with r₀ and the constants chosen after r_♭.

### The exterior domain {#sec:iii-c1-1}

This section is [Hin26, Lemma 5.16] in dimension 4 + 1. Fix weights

    ℓ^♭₀ > 3/2,     3/2 < ℓ^♭_I < min(ℓ^♭₀, 3/2 + (1 − e_Υ)γ_Υ, 2).                                      {#eq:iii-c1-1-1}

So ℓ^♭_I < min Re ℰ_I^C for every ℰ_I^C of [[def:iii-c-3-1]], and H^(k,ℓ^♭₀,(−,ℓ^♭_I))_b ([[def:iii-c-3-1]]) consists
of the h with every slot in H^(k,ℓ^♭₀,ℓ^♭_I)_b except π̸₀h ∈ H^(k,ℓ^♭₀,((3/2,0),ℓ^♭_I))_b, which carries a radiation
field: the exponents 3/2 + s, s ∈ σ_Υ ∖ {0}, of the slots 4, 5 and 7 exceed ℓ^♭_I by [[eq:iii-c1-1-1]] and
(1 − e_Υ)γ_Υ ≤ γ_Υ ≤ 2γ_Υ.

**Lemma {#lem:iii-c1-1-1}** (The spacetime domain; [Hin26, Lemma 5.16] in dimension 4 + 1.) For r₀ large let, with
r = |x|,

    Ω_(ext,r₀) := {−(r − r₀)/12 ≤ t_IVP ≤ 0} ∪ {0 ≤ t_IVP ≤ r + 2r^(1−ℓ^♭_I) − (r₀ + 2r₀^(1−ℓ^♭_I))},

with boundary hypersurfaces Σ_(past,r₀), Σ_(fut,r₀) (the first and the last level set) and
Σ_(IVP,r₀) := Ω_(ext,r₀) ∩ {t_IVP = 0}. There is R₀ > max(3R₁, R₃) such that for r₀ ≥ R₀ and every
h ∈ H^(3,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀)) with norm below 1 (the spaces [[eq:iii-c-3-3]], defined for k ≥ 5, extend
verbatim to k = 3), the three hypersurfaces are spacelike for g_(b₀) + h.

*Proof.* For r ≥ R₃, t_IVP = t − C″ ([[lem:iii-b-3-7]] (b)), and r^(1−ℓ^♭_I) → 0 as ℓ^♭_I > 1; so
Ω_(ext,r₀) ⊂ U ∩ {|x| ≥ r₀} ([[eq:iii-c-1-3]]) for r₀ large, and on it ρ₀ ≤ C/r₀: on Σ_(fut,r₀),
x¹ = t − r = −r₀ + 2r^(1−ℓ^♭_I) − 2r₀^(1−ℓ^♭_I) + O(1), and x¹ is smaller below it, so ρ₀ = (2 − x¹)⁻¹ ≤ C/r₀. By
Sobolev embedding (3 > 5/2) every slot of h is bounded by Cρ₀^(ℓ^♭₀)ρ_I^(ℓ^♭_I), except π̸₀h, which is bounded by
Cρ₀^(ℓ^♭₀)ρ_I^(3/2); and g_(b₀) − η ∈ ρ₀²ρ_I²C^∞ with its π_C, π₀₁, π_(1/), π̸₀ parts in ρ₀²ρ_I³C^∞
([[lem:iii-c-3-5]] (1), [[def:iii-c-3-4]]). Write δ := g_(b₀) + h − η, so that
|δ| ≤ C(ρ₀²ρ_I² + ρ₀^(ℓ^♭₀)ρ_I^(3/2)) in the frame of [[eq:iii-c-1-6]], which is small for r₀ large.

*Σ_(IVP,r₀) and Σ_(past,r₀).* dt is timelike for η, and so for η + δ when |δ| is small. In the coordinates (u, r) of
Minkowski space, u := t − r, η⁻¹ = −2∂_u∂_r + ∂_r² on du, dr, so ζ := d(t_IVP + (r − r₀)/12) = du + (13/12)dr has
η⁻¹(ζ, ζ) = −2 · 13/12 + (13/12)² = −143/144. (The calculation does not involve the dimension; any slope c ∈ (0, 1) in
place of 1/12 gives −2(1 + c) + (1 + c)² = (c + 1)(c − 1) < 0.) So ζ is timelike for η + δ too.

*Σ_(fut,r₀).* With x⁰ = t + r, x¹ = t − r, η = −dx⁰dx¹ (symmetric product), so η^(01) = −2,
η^(00) = η^(11) = 0, and dr = ½(dx⁰ − dx¹). For ℓ := ℓ^♭_I,

    ζ := d(t_IVP − r − 2r^(1−ℓ)) = (ℓ − 1)r^(−ℓ)dx⁰ + (1 − (ℓ − 1)r^(−ℓ))dx¹,

so η⁻¹(ζ, ζ) = −4(ℓ − 1)r^(−ℓ)(1 − (ℓ − 1)r^(−ℓ)), with r^(−ℓ) = ρ₀^ℓρ_I^ℓ. As ζ has no angular part,
(η + δ)⁻¹(ζ, ζ) − η⁻¹(ζ, ζ) = −η^(ia)η^(jb)δ_(ab)ζ_iζ_j + O(|δ|²), i, j, a, b ∈ {0, 1}. The coefficient of ζ₁² is
−4δ₀₀, of π_C-type, bounded by C(ρ₀²ρ_I³ + ρ₀^(ℓ^♭₀)ρ_I^(ℓ^♭_I)); that of ζ₀ζ₁ involves δ₀₁, bounded likewise; that of
ζ₀² involves δ₁₁, bounded by C(ρ₀²ρ_I² + ρ₀^(ℓ^♭₀)ρ_I^(ℓ^♭_I)) and multiplied by ζ₀² = O(ρ₀^(2ℓ)ρ_I^(2ℓ)); and
O(|δ|²) ≤ C(ρ₀⁴ρ_I⁴ + ρ₀^(2ℓ^♭₀)ρ_I³). Relative to ρ₀^ℓρ_I^ℓ these are at most
C(ρ₀^(2−ℓ)ρ_I^(3−ℓ) + ρ₀^(ℓ^♭₀−ℓ) + ρ₀^(2ℓ^♭₀−ℓ)ρ_I^(3−ℓ)), which tends to 0 as ρ₀ → 0, as ℓ < 2, ℓ < ℓ^♭₀ and ℓ < 3
([[eq:iii-c1-1-1]]). As ρ₀ ≤ C/r₀ on Ω_(ext,r₀), for r₀ large (η + δ)⁻¹(ζ, ζ) ≤ −2(ℓ − 1)r^(−ℓ) < 0. ∎

The past slab of [Hin26, Lemma 5.16] has the slope ¼; the slope 1/12 keeps Ω_(ext,r₀) inside {t_IVP > −|x|/10}, where
χ_IVP = 1 ([[sec:iii-b-5]]), so that the boosts of [[sec:iii-c2-1]] are genuine boosts on all of it. [Hin26] uses its
Lemma 5.6 for the pointwise bounds; here the slots of h and of g_(b₀) − η give them directly, the mass entering at
ρ₀²ρ_I² in the slot π₁₁ only ([[lem:iii-c-3-5]]).

The causal structure of Ω_(ext,r₀) is that of a domain of dependence of Σ_(IVP,r₀). We record it in the form used for
uniqueness.

**Lemma {#lem:s26-development}** (Ω_(ext,r₀) is a Cauchy development.) Let r₀ ≥ R₀, with R₀ enlarged if necessary,
let g₀ = g_(b₀), or g₀ ∈ 𝒢 with g₀ − g_(b₀) satisfying the pointwise bounds of the proof of [[lem:iii-c1-1-1]], and let
g := g₀ + h with h as in [[lem:iii-c1-1-1]] and smooth in the interior of Ω_(ext,r₀). Time-orient g by ∂_t. Then the
interior Ω° of Ω_(ext,r₀) is globally hyperbolic for g, and Σ° := Ω° ∩ {t_IVP = 0} is a smooth spacelike Cauchy
hypersurface of Ω°.

*Proof.* Write g = η + δ as in the proof of [[lem:iii-c1-1-1]]; |δ| is small on Ω_(ext,r₀) for r₀ large. For
c ∈ [−½, ½] the covector dt + c d|x| is timelike for η with η⁻¹-norm −(1 − c²) ≤ −¾ (the calculation of that proof, in
which the sign of c does not enter), hence timelike for g; ∂_t is timelike for g, and (dt + c d|x|)(∂_t) = 1 > 0. A
covector that is timelike for g and positive on one future timelike vector is positive on every future causal vector, the
future causal cone being connected. So t + c|x| is strictly increasing along future directed causal curves for every
such c; in particular t_IVP = t − C″ is, and |V|x|| < 2Vt for every future causal V. The same holds, by the proof of
[[lem:iii-c1-1-1]], for φ₊ := t_IVP − F₀(|x|), F₀(r) := r + 2r^(1−ℓ^♭_I) − (r₀ + 2r₀^(1−ℓ^♭_I)), and for
φ₋ := t_IVP + (|x| − r₀)/12, whose differentials are the timelike covectors ζ there, each positive on ∂_t. As t_IVP is
strictly increasing along causal curves, Σ° is acausal in Ω°; it is spacelike by [[lem:iii-c1-1-1]].

Let p ∈ Ω° with t_IVP(p) > 0 and γ a past inextendible causal curve in Ω° from p. If γ did not meet Σ°, then
t_IVP > 0 along γ (t_IVP is continuous along γ, and Ω° ∩ {t_IVP = 0} = Σ°); φ₊ ≤ φ₊(p) < 0 along γ; and
|x| ≤ |x(p)| + 2t_IVP(p) along γ. So γ would lie in the compact set
K := {0 ≤ t_IVP ≤ t_IVP(p), φ₊ ≤ φ₊(p), |x| ≤ |x(p)| + 2t_IVP(p)}, which lies in Ω°: at its points F₀(|x|) > t_IVP ≥ 0,
so |x| > r₀ and −(|x| − r₀)/12 < 0 ≤ t_IVP < F₀(|x|). As in the proof of [[lem:ii-f-1-3]], t_IVP is strictly monotone
along γ and serves as a parameter in which the tangent lies in the compact set of causal vectors V over K with
dt_IVP(V) = 1; so γ extends continuously to its past end point in K ⊂ Ω°, against its inextendibility. Hence γ meets
Σ°. For p with t_IVP(p) < 0 the same argument, with future inextendible curves, φ₋ ≥ φ₋(p) > 0 in place of φ₊ and
the compact set {t_IVP(p) ≤ t_IVP ≤ 0, φ₋ ≥ φ₋(p), |x| ≤ |x(p)| + 2|t_IVP(p)|}, shows that every future inextendible
causal curve from p meets Σ°. Every inextendible causal curve through p contains a past (resp. future) inextendible
one from p. So Ω° is the Cauchy development of Σ° in Ω°, and [[thm:std-bgp-development]] gives the claim. ∎

### The edge-b structure at null infinity {#sec:iv-0}

[[sec:iv-0]]–[[sec:iv-4]] are [Hin23a, Sections 3.1–3.2] (pp. 9–17) in dimension 4 + 1, for the operator of
[[sec:iii-c-4]] on the exterior region of [[sec:iii-c-1]]: the edge-b structure at ℐ⁺ ([Hin23a, Definitions 3.1–3.3,
Lemmas 3.6, 3.12–3.16, Corollary 3.14]), the basic energy estimate ([Hin23a, Proposition 3.17]), and the estimate near
the interior of I₀ for which [Hin23a] cites [HV20, Proposition 4.3]. The dimension enters through the quantities of
[[prop:np-10-64]]; here each is written into the proof.

*The region.* U, (ρ₀, ρ_I, ω), X₀ = ρ₀∂_(ρ₀), X_I = ρ_I∂_(ρ_I), the null coordinates x⁰ = t + |x|, x¹ = t − |x| and
ρ = ρ₀ρ_I = |x|⁻¹ are those of [[sec:iii-c-1]] ([[lem:iii-c-1-1]], [[eq:iii-c-1-2]]–[[eq:iii-c-1-5]]), with ω ∈ 𝕊³. Put
x_I := ρ_I^(1/2) and let M_♯ be U with the smooth structure in which (ρ₀, x_I, ω) are coordinates near ℐ⁺ ([Hin23a,
(3.6)], there with ρ₀ and x_I of the null coordinates of Schwarzschild space). The faces of M_♯ at infinity are
I₀ = {ρ₀ = 0} and ℐ⁺ = {x_I = 0}, and ℐ⁺ is fibred by (ρ₀, ω) ↦ ω over 𝕊³, with fibres the ρ₀-lines ([Hin23a,
Definition 3.7]).

*Edge-b objects* ([Hin23a, Definitions 3.1–3.4], stated on any manifold with two boundary hypersurfaces and a
fibration of one of them; no dimension enters). 𝒱_b(M_♯) is spanned over C^∞(M_♯) by X₀, X_I = ½x_I∂_(x_I) and the
vector fields on 𝕊³. 𝒱_(e,b)(M_♯) ⊂ 𝒱_b(M_♯), the vector fields whose restriction to ℐ⁺ is tangent to its fibres, is
spanned by X₀, X_I and x_IΘ, Θ ∈ 𝒱(𝕊³) ([Hin23a, (3.9)]). Diff^k_(e,b)(M_♯) consists of the sums of compositions of at
most k elements of 𝒱_(e,b)(M_♯) with C^∞ coefficients, and Diff^(m;k)_(e,b;b)(M_♯) := Diff^m_(e,b)(M_♯) · Diff^k_b(M_♯)
of the sums of compositions PQ with P ∈ Diff^m_(e,b), Q ∈ Diff^k_b; on sections of a bundle the coefficients are
smooth endomorphisms, and for a space ℱ of functions, ℱDiff^k_(e,b) denotes the operators with coefficients in ℱ. With
the b-density, H^k_(e,b)(M_♯) is the space of u ∈ L² with Pu ∈ L² for all P ∈ Diff^k_(e,b), and H^((m;k))_(e,b;b)(M_♯)
that of u with PQu ∈ L² for all P ∈ Diff^m_(e,b), Q ∈ Diff^k_b; the weighted spaces are
H^(k,(α₀,α₁))_(e,b) := ρ₀^(α₀)x_I^(α₁)H^k_(e,b) and H^((m;k),(α₀,α₁))_(e,b;b) := ρ₀^(α₀)x_I^(α₁)H^((m;k))_(e,b;b). The
b-spaces are those of [[sec:iii-c-2]]: 𝒱_b and the b-density are the same in the coordinates ρ_I and x_I
(|dρ_I/ρ_I| = 2|dx_I/x_I|), and x_I^(2α) = ρ_I^α, so H^(k,(α₀,2α_I))_b in (ρ₀, x_I) is H^(k,α₀,α_I)_b of
[[sec:iii-c-2]] in (ρ₀, ρ_I). As dim M_♯ = 5,

    H^(s,(α₀,α₁))_b(M_♯) ↪ ρ₀^(α₀)x_I^(α₁)L^∞,     s > 5/2,                                              {#eq:iv-0-1}

by the change of variables z₀ = log ρ₀, z₁ = log x_I, in which b-Sobolev spaces are uniformly local Sobolev spaces on
ℝ² × 𝕊³, and Sobolev embedding there; the order s = 3 serves in dimensions 3 + 1 and 4 + 1 ([[prop:np-10-64]] (6)).

*The metric.* g_(b₀) is the Tangherlini metric, b₀ = (m₀, 0) ([[sec:iii-b-3]]), in the coordinates of [[ch:s11]], and
η = −dx⁰dx¹ + |x|²g̸ is the Minkowski metric. On U the components of g_(b₀) − η in the rescaled null frame of
[[eq:iii-c-1-6]] lie in ρ²C^∞(U) ([[lem:iii-c-3-5]] (1), [[lem:iii-c-1-3]]).

### The frame as edge-b covectors {#sec:iv-1}

This section is [Hin23a, Lemmas 3.12–3.13, Corollary 3.14 and Remark 3.15] in dimension 4 + 1.

**Lemma {#lem:iv-1-1}** ([Hin23a, Lemma 3.13] in dimension 4 + 1.) For ω̸ ∈ C^∞(𝕊³; T*𝕊³),

    dx⁰ ∈ ρ₀⁻¹x_I⁻²C^∞(M_♯; ᵉᵇT*M_♯),     dx¹ ∈ ρ₀⁻¹C^∞(M_♯; ᵉᵇT*M_♯),     |x|ω̸ ∈ ρ₀⁻¹x_I⁻¹C^∞(M_♯; ᵉᵇT*M_♯),

where ᵉᵇTM_♯ is the bundle whose smooth sections are the elements of 𝒱_(e,b)(M_♯) and ᵉᵇT*M_♯ its dual; and the
products of the frame [[eq:iii-c-1-6]] have the orders of [Hin23a, (3.13)]: (dx⁰)² ∈ ρ₀⁻²x_I⁻⁴C^∞; dx⁰dx¹ and |x|²h̸,
for h̸ ∈ C^∞(𝕊³; S²T*𝕊³), in ρ₀⁻²x_I⁻²C^∞; dx⁰ ⊗_s |x|ω̸ ∈ ρ₀⁻²x_I⁻³C^∞; (dx¹)² ∈ ρ₀⁻²C^∞;
dx¹ ⊗_s |x|ω̸ ∈ ρ₀⁻²x_I⁻¹C^∞, as sections of S²ᵉᵇT*M_♯.

*Proof.* By [[eq:iii-c-1-5]], ∂₀ = −½ρ₀ρ_I X_I and ∂₁ = ρ₀(X₀ − X_I + ½ρ_I X_I), and |x|⁻¹e_a = ρ₀x_I · x_Ie_a for an
orthonormal frame e_a of 𝕊³. So (∂₀, ∂₁, |x|⁻¹e_a) = ρ₀DB(X₀, X_I, x_Ie_a) with D = diag(x_I², 1, x_I Id₃) and

    B = ( 0     −½            0   )
        ( 1     −1 + ½x_I²    0   )
        ( 0      0            Id₃ ),     det B = ½.

B is smooth and invertible up to x_I = 0, and (X₀, X_I, x_Ie_a) is a frame of ᵉᵇTM_♯. The dual coframe of
(∂₀, ∂₁, |x|⁻¹e_a) is (dx⁰, dx¹, |x|e^a). So (dx⁰, dx¹, |x|e^a) is ρ₀⁻¹D⁻¹(B⁻¹)ᵀ applied to the dual eb-coframe, which
gives the three memberships, and the products follow. ∎

**Corollary {#cor:iv-1-2}** ([Hin23a, Lemma 3.12 and Corollary 3.14] in dimension 4 + 1.)
g_(b₀) ∈ ρ₀⁻²x_I⁻²C^∞(M_♯; S²ᵉᵇT*M_♯) is nondegenerate of Lorentzian signature up to I₀ ∪ ℐ⁺, and

    ρ₀²x_I²g_(b₀) ≡ 2(dρ₀/ρ₀)² + 2(dρ₀/ρ₀) ⊗_s (dρ_I/ρ_I) + x_I⁻²g̸,
    ρ₀⁻²x_I⁻²g_(b₀)⁻¹ ≡ 2X_I ⊗_s (X₀ − X_I) + x_I²g̸⁻¹,

modulo x_IC^∞(M_♯; S²ᵉᵇT*M_♯), resp. x_IC^∞(M_♯; S²ᵉᵇTM_♯).

*Proof.* For η: dx¹ = ρ₀⁻¹dρ₀/ρ₀ and d|x| = −|x|(dρ₀/ρ₀ + dρ_I/ρ_I), from x¹ = 2 − ρ₀⁻¹ and |x| = (ρ₀ρ_I)⁻¹; with
dx⁰ = dx¹ + 2d|x|,

    ρ₀²ρ_Iη = 2(dρ₀/ρ₀)² + 2(dρ₀/ρ₀) ⊗_s (dρ_I/ρ_I) − ρ_I(dρ₀/ρ₀)² + ρ_I⁻¹g̸

exactly, and ρ_I⁻¹g̸ = x_I⁻²g̸ is a smooth eb-tensor (dω/x_I being an eb-covector). The dual statement for
η⁻¹ = −4∂₀ ⊗_s ∂₁ + |x|⁻²g̸⁻¹ follows from [[eq:iii-c-1-5]] in the same way, with the remainder x_I²X_I ⊗ X_I. By
[[sec:iv-0]], the components of g_(b₀) − η in the null frame are O(ρ²); by [[lem:iv-1-1]] the worst frame product,
(dx⁰)², lies in ρ₀⁻²x_I⁻⁴C^∞, and ρ² = ρ₀²x_I⁴. So g_(b₀) − η ∈ C^∞ = ρ₀⁻²x_I⁻² · ρ₀²x_I²C^∞, which lies in the
error class. Nondegeneracy and the signature follow from the leading form, which is that of η. ∎

**Remark {#rem:iv-1-3}** ([Hin23a, Remark 3.15].) As 𝒱_(e,b) is a Lie algebra and differentiation along it preserves
ρ₀^(ℓ₀)x_I^(ℓ_I)C^∞, the Koszul formula gives ∇^(g_(b₀)) ∈ Diff¹_(e,b) on eb-tensor bundles, and

    □_(g_(b₀)) ∈ ρ₀²x_I²Diff²_(e,b)(M_♯; ᵉᵇT^(p,q)M_♯)                                                   {#eq:iv-1-1}

([Hin23a, (3.14)]). Nothing here depends on the dimension.

