# Part. The stability theory, V: exterior, nonlinear theorem, gluing, linear stability {#part:stability-nonlinear}

## The exterior region: estimates at infinity, the exterior solution, polyhomogeneity and boosts {#ch:s26}

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

### Notation and the inner radius {#sec:iii-c1-0}

n = 4, D = 5. The notation is that of [[ch:s11]] and [[ch:s17]]: the family g_b,
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
infinity. Every result posed on the exterior domain or near infinity lives in {|x| ≥ r₀} with r₀ large and does not
reach the inner boundary. [[prop:iii-c2-4-1]], [[rem:iii-c2-3-2]] and [[rem:iii-c2-4-3]] concern all of Σ_IVP, which
does reach it; but the proof of [[prop:iii-c2-4-1]] is pointwise on Σ_IVP and uses only that g_(b₀) is smooth and dt_IVP
is timelike for g_(b₀) on {|x| ≥ r_♭} ([[lem:iii-b-3-7]] (b)). So every result of the chapter holds for each
r_♭ ∈ (0, ½R₁], with r₀ and the constants chosen after r_♭.

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

*The radius R₀.* Enlarging R₀ keeps [[lem:iii-c1-1-1]] true. We fix R₀ once, so that in addition R₀ ≥ 4|C″| + 4, the
function F₀ of [[lem:s26-development]] is increasing on [R₀, ∞), and every statement of this chapter made for r₀ large
(in [[lem:s26-development]], [[rem:iv-4-2]], [[lem:iv2-1-1]] (a), [[lem:iv2-2-2]], [[lem:iv2-2-3]] and [[cor:iv2-4-1]])
holds for every r₀ ≥ R₀. Each of these asks r₀ above a bound depending only on b₀, the gauge parameters, ℓ^♭₀, ℓ^♭_I
and the constant c of [[lem:iv2-2-1]], whose choice does not involve r₀ (it is the smallness of x_I in [[prop:iv-3-1]]
and [[prop:iv1-2-2]]). From here on R₀ is this radius.

The causal structure of Ω_(ext,r₀) is that of a domain of dependence of Σ_(IVP,r₀). We record it in the form used for
uniqueness.

**Lemma {#lem:s26-development}** (Ω_(ext,r₀) is a Cauchy development.) Let r₀ ≥ R₀, let g₀ = g_(b₀), or g₀ ∈ 𝒢
with g₀ − g_(b₀) satisfying the pointwise bounds of the proof of [[lem:iii-c1-1-1]], and let g := g₀ + h with h as in
[[lem:iii-c1-1-1]] and smooth in the interior of Ω_(ext,r₀). Time-orient g by ∂_t. Then the interior Ω° of Ω_(ext,r₀) is
globally hyperbolic for g, and Σ° := Ω° ∩ {t_IVP = 0} is a smooth spacelike Cauchy hypersurface of Ω°.

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
|x| ≤ |x(p)| + 2t_IVP(p) along γ; and |x| ≥ r₀ on Ω°. So γ would lie in the compact set
K := {0 ≤ t_IVP ≤ t_IVP(p), φ₊ ≤ φ₊(p), r₀ ≤ |x| ≤ |x(p)| + 2t_IVP(p)}, which lies in Ω°: at its points
F₀(|x|) > t_IVP ≥ 0, and F₀(r₀) = 0 with F₀ increasing on [r₀, ∞) (the choice of R₀), so |x| > r₀ and
−(|x| − r₀)/12 < 0 ≤ t_IVP < F₀(|x|). As in the proof of [[lem:ii-f-1-3]], t_IVP is strictly monotone
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

### The scalar wave operator {#sec:iv-2}

This section is [Hin23a, Lemma 3.16] and the density of [Hin23a, Proposition 3.17] in dimension 4 + 1. The
conjugation that removes the first-order term is by ρ^(3/2) = |x|^(−3/2), where in dimension 3 + 1 it is by ρ
([[prop:np-10-64]] (1)).

**Lemma {#lem:iv-2-1}** (The density.) μ_b := ρ₀⁵ρ_I⁴|dg_(b₀)| is a smooth positive b-density on M_♯. For η it is
exactly |(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|. The operator

    L := ρ_Iρ^(−7/2) □_(g_(b₀)) ρ^(3/2)                                                                 {#eq:iv-2-1}

is formally self-adjoint on L²(M_♯; μ_b). ([Hin23a] has ρ₀⁴ρ_I³ and ρ_Iρ⁻³□ρ in dimension 3 + 1; [[prop:np-10-64]]
(2).)

*Proof.* |dη| = |x|³|dt d|x| dg̸| with t = x¹ + |x|, and |dx¹ ∧ d|x|| = ρ₀⁻²|x||dρ₀ ∧ dρ_I/ρ_I|
= ρ₀⁻¹|x||(dρ₀/ρ₀) ∧ (dρ_I/ρ_I)|. So |dη| = |x|⁴ρ₀⁻¹|(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸| = ρ₀⁻⁵ρ_I⁻⁴|(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|.
|dg_(b₀)| = |dη|(1 + O(ρ²)) with a smooth factor, by [[sec:iv-0]]. For the self-adjointness,

    ⟨Lu, v⟩_(L²(μ_b)) = ∫(□ρ^(3/2)u) v ρ_Iρ^(−7/2)ρ₀⁵ρ_I⁴|dg| = ∫(□ρ^(3/2)u)(ρ^(3/2)v)|dg|,

as ρ_Iρ^(−7/2)ρ₀⁵ρ_I⁴ = ρ^(−7/2)ρ⁵ = ρ^(3/2), and □ is symmetric on L²(|dg|). ∎

**Lemma {#lem:iv-2-2}** (L as an eb-operator; commutators; [Hin23a, Lemma 3.16] in dimension 4 + 1.)
L ∈ Diff²_(e,b)(M_♯), and

    L = −2X_I(X₀ − X_I) + x_I²(Δ̸ + ¾) + L̃,     L̃ ∈ x_IDiff²_(e,b)(M_♯),                                {#eq:iv-2-2}

with Δ̸ = −tr̸∇̸² ≥ 0 the Laplacian of 𝕊³. For every vector field Θ on 𝕊³,

    [L, X₀],  [L, X_I],  [L, Θ] ∈ x_IDiff^(1;1)_(e,b;b)(M_♯).                                         {#eq:iv-2-3}

*Proof.* *Minkowski space.* With □ = −tr∇², □_η = 4∂₀∂₁ − (3/|x|)∂_(|x|) + |x|⁻²Δ̸ on functions, and conjugation by
|x|^(−3/2) removes the first-order term:

    |x|^(3/2)□_η|x|^(−3/2) = 4∂₀∂₁ + |x|⁻²(Δ̸ + ¾),

the constant being (n − 1)(n − 3)/4 = ¾ ([[prop:np-10-64]] (1); it is 0 in dimension 3 + 1). By [[eq:iii-c-1-5]] and
X_Iρ₀ = 0, X_Iρ_I = ρ_I,

    4∂₀∂₁ = −2ρ₀ρ_IX_I ρ₀(X₀ − X_I + ½ρ_IX_I) = −2ρ₀²ρ_IX_I(X₀ − X_I) − ρ₀²ρ_I²(X_I + 1)X_I.

Multiplying by ρ_Iρ⁻² = ρ₀⁻²ρ_I⁻¹ (with |x|⁻² = ρ₀²ρ_I²) gives

    L_η = −2X_I(X₀ − X_I) + x_I²(Δ̸ + ¾) − x_I²(X_I + 1)X_I,

and x_I²(X_I + 1)X_I ∈ x_I²Diff²_(e,b), X_I being an eb-vector field.

*The mass.* □_g modulo ρ₀²x_I³Diff²_(e,b) depends only on g modulo ρ₀⁻²x_I⁻¹C^∞(S²ᵉᵇT*), by [[eq:iv-1-1]] and the
Koszul formula. By the proof of [[cor:iv-1-2]], g_(b₀) − η ∈ ρ₀⁻²x_I⁻² · ρ₀²x_I²C^∞, which lies in that class.
Conjugation by ρ^(3/2) and multiplication by ρ_Iρ⁻² preserve the classes up to the factor ρ₀⁻²x_I⁻². So
L − L_η ∈ x_IDiff²_(e,b), which is [[eq:iv-2-2]].

*Commutators.* The argument of [Hin23a] uses only [[eq:iv-2-2]] and the structure of 𝒱_(e,b).

- [L, X₀] = [L̃, X₀] ∈ x_IDiff²_(e,b), as X₀ commutes with the leading part of [[eq:iv-2-2]] ([X₀, x_I²] = 0) and
  𝒱_(e,b) is a Lie algebra.
- [L, X_I] = −ρ_I(Δ̸ + ¾) + [L̃, X_I], as [x_I², X_I] = −x_I². Write Δ̸ = Σ_k Θ_(k,1)Θ_(k,2) + Θ_♭ + f, with the Θ's
  vector fields on 𝕊³ and f ∈ C^∞(𝕊³). As 𝒱(𝕊³) ⊂ x_I⁻¹𝒱_(e,b) ∩ 𝒱_b,

      ρ_I(Δ̸ + ¾) = x_I Σ_k (x_IΘ_(k,1))Θ_(k,2) + x_I(x_IΘ_♭) + x_I²(f + ¾) ∈ x_IDiff^(1;1)_(e,b;b)

  ([Hin23a, (3.18)]).
- [L, Θ] = ρ_I[Δ̸, Θ] + [L̃, Θ] ([Hin23a] prints the first commutator with the opposite sign, which does not matter
  here), and the first term lies in x_IDiff^(1;1)_(e,b;b) in the same way. For the second, lifts of vector fields on
  𝕊³ preserve the eb-classes: in coordinates, Θ = Σ_j Θ^j(y)∂_(y^j) and V = a⁰X₀ + a¹X_I + Σ_j a^j x_I∂_(y^j), and

      [Θ, V] = (Θa⁰)X₀ + (Θa¹)X_I + x_I Σ_j [Θ, a^j∂_(y^j)] ∈ 𝒱_(e,b)

  ([Hin23a, (3.19a)]). So [·, Θ] maps ρ₀^a x_I^b Diff²_(e,b) to itself for all weights a, b ([Hin23a, (3.19b)]),
  and [L̃, Θ] ∈ x_IDiff²_(e,b).

The term ¾x_I² commutes with X₀ and Θ, and [¾x_I², X_I] = −¾x_I² lies in x_IDiff⁰. ∎

### The basic energy estimate near ℐ⁺ {#sec:iv-3}

This section is [Hin23a, Proposition 3.17 and Remark 3.18] in dimension 4 + 1.

*Domains.* Let c_♯ > 0 be so small that, on {x_I < c_♯} ∩ {ρ₀ ≤ 1}:

- |x| = ρ₀⁻¹x_I⁻² > c_♯⁻² ≥ 4R₁, so that the part of the set in {t_* ≤ T₀} lies in U ([[eq:iii-c-1-3]]; x¹ ≤ 1 alone
  does not give t_* ≤ T₀, as t_* = x¹ + C′ − 8m₀|x|⁻¹ there);
- the level sets of x_I are spacelike for g_(b₀);
- the multiplier V below is future timelike for g_(b₀).

This is possible. For η, dρ_I = |x|⁻¹(−½ρ_I dx⁰ − (1 − ½ρ_I)dx¹), so

    η⁻¹(dρ_I, dρ_I) = −2|x|⁻²ρ_I(1 − ½ρ_I) < 0     (ρ_I < 2)                                          {#eq:iv-3-1}

([Hin23a, (3.8)], with η⁻¹(dx⁰, dx¹) = −2, η⁻¹(dx⁰, dx⁰) = η⁻¹(dx¹, dx¹) = 0). The correction from δ := g_(b₀) − η is
O(ρ²) relative to ρ_I|x|⁻²: η⁻¹dρ_I = |x|⁻¹((2 − ρ_I)∂₀ + ρ_I∂₁), and with δ_(ab) := δ(∂_a, ∂_b) as in the proof of
[[lem:iii-c1-1-1]], δ₀₀, δ₀₁ ∈ ρ₀²ρ_I³C^∞ and δ₁₁ ∈ ρ₀²ρ_I²C^∞ ([[def:iii-c-3-4]], [[lem:iii-c-3-5]] (1)), so

    δ(η⁻¹dρ_I, η⁻¹dρ_I) = |x|⁻²((2 − ρ_I)²δ₀₀ + 2ρ_I(2 − ρ_I)δ₀₁ + ρ_I²δ₁₁) ∈ ρ_I|x|⁻² · ρ²C^∞,

and the terms quadratic in δ are smaller. So [[eq:iv-3-1]] persists for ρ = ρ₀x_I² small; this is the role of the bound
x̄_I ≤ 1/√(8m) of [Hin23a]. Here c_♯ is fixed by the three conditions above in the Minkowski coordinates of
[[sec:iii-c-1]]; the bound of [Hin23a], stated in its tortoise coordinates ([[prop:np-10-64]] (8)), is not used.

Let Ω ⊂ {x_I < c} ∩ {ρ₀ < 1} ∩ {t_* ≤ T₀}, c < c_♯, be open. Its boundary in the interior consists of two
hypersurfaces, each smooth or piecewise smooth (there is no boundary term at a corner of Σ_in, where u vanishes):
Σ_in, spacelike for g_(b₀), and Σ_fin, spacelike or null for g_(b₀), with Ω to the future of Σ_in and to the past of
Σ_fin. Every integral curve of X_I in Ω (at fixed ρ₀ and ω, with ρ_I decreasing) begins on Σ_in. The set
{x_I < c, ρ₀ < 1} of [Hin23a], with Σ_in = x_I⁻¹(c) and Σ_fin = ρ₀⁻¹(1), is an example once 1 is replaced by
ρ̄₀ := (1 + 2R₁)⁻¹: ρ₀ < ρ̄₀ means x¹ < 1 − 2R₁, which gives t_* < T₀. So is Ω_(ext,r₀) ∩ {x_I < c} ∩ {t_IVP ≥ 0},
whose part of Σ_IVP and whose Σ_(fut,r₀) are spacelike ([[lem:iii-c1-1-1]]), together with the part of x_I⁻¹(c) in it
(a piecewise smooth Σ_in, with a corner where it meets Σ_IVP; Ω_(ext,r₀) ⊂ U by the proof of [[lem:iii-c1-1-1]]); an
outgoing ray at fixed x¹ enters it across Σ_IVP or x_I⁻¹(c).

**Proposition {#prop:iv-3-1}** (The energy estimate; [Hin23a, Proposition 3.17] in dimension 4 + 1.) Let Ω be as
above, k ∈ ℕ₀, and α₀, α_I ∈ ℝ with α_I < min(α₀, 0). Let f ∈ H^(k,(α₀,2α_I))_b(Ω) = ρ₀^(α₀)ρ_I^(α_I)H^k_b(Ω) vanish
near Σ_in. Then the forward solution u of Lu = f (vanishing Cauchy data on Σ_in) lies in
H^((1;k),(α₀,2α_I))_(e,b;b)(Ω), and

    ‖u‖_(H^((1;k),(α₀,2α_I))_(e,b;b)(Ω)) ≤ C‖f‖_(H^(k,(α₀,2α_I))_b(Ω)),                                {#eq:iv-3-2}

with C depending on k, α₀, α_I, c and the geometry of Σ_in, Σ_fin. Away from ℐ⁺ (on {x_I ≥ c/2}) the same holds with
H^(k+1)_b on the left.

*Proof.* *The multiplier* ([Hin23a, (3.22)]). Let

    W := w²V,     w := ρ₀^(−α₀)ρ_I^(−α_I),     V := X₀ − (1 + κ)X_I,     κ > 0.

V is future timelike: by [[eq:iii-c-1-4]]–[[eq:iii-c-1-5]], V = ρ₀⁻¹(∂_t + 2κρ_I⁻¹∂₀), a positive combination of the
future timelike ∂_t and the future null ∂₀ near ℐ⁺ for η, hence for g_(b₀) by [[cor:iv-1-2]]. By the leading form of
[[cor:iv-1-2]], g_(b₀)(V, V) ≡ ρ₀⁻²x_I⁻²(2 − 2(1 + κ)) = −2κρ₀⁻²x_I⁻² modulo ρ₀⁻²x_I⁻¹C^∞, so V is uniformly timelike in
the eb-sense.

*The identity* ([Hin23a, (3.23)]). For u smooth with support as in the statement,

    2 Re⟨wLu, wVu⟩_(L²(Ω,μ_b)) = ⟨Qu, u⟩ + ℬ_fin(u),     Q := L*W + W*L = [L, W] − (div_(μ_b)W)L.

It is the integral over Ω of the pointwise identity 2 Re(w²Lu · Vū) = div_(μ_b)J + q(u) of the vector field method. As L
is real and formally self-adjoint ([[lem:iv-2-1]]), L = −div_(μ_b)(G∇u) + V₀u with G its principal symbol and V₀ := L(1);
J is the energy current of W, including the potential term; and q(u), built from G, its derivative along W, ∇W,
div_(μ_b)W, V₀ and WV₀, is a quadratic form in u and its first derivatives with no products of u with its derivatives. We
write ⟨Qu, u⟩ for ∫_Ω q(u)μ_b, which is the pairing of Qu with u when u vanishes near Σ_fin, and ℬ_fin(u) for the flux of
J through Σ_fin. There is no boundary term at Σ_in, where u vanishes to second order, and none at I₀ ∪ ℐ⁺ in the
following approximation, which is needed as the forward solution is not known beforehand to lie in the weighted space.
Approximate f in H^(k,(α₀,2α_I))_b by f_j supported in {ρ₀ ≥ 1/j}. The forward solution u_j of Lu_j = f_j vanishes near
I₀, the causal future of supp f_j staying in {x¹ ≥ x¹_j} for some x¹_j, so away from spatial infinity. Apply the identity
to u_j on Ω_ε := Ω ∩ {x_I > ε}, whose added boundary {x_I = ε} is spacelike by [[eq:iv-3-1]], with Ω_ε to its past: it is
a further final boundary, with a boundary term of the same sign as ℬ_fin. The Poincaré inequality below does not depend
on where an X_I-curve ends. So the estimate holds for u_j on Ω_ε, uniformly in ε and j; let ε → 0, then j → ∞, the u_j
converging to u locally uniformly with their derivatives and the uniform bound passing to the limit. ℬ_fin(u) ≥ 0: it is
the flux through Σ_fin of the energy current of the future timelike W, and Σ_fin is spacelike or null with Ω to its past.
It also contains the potential term, a positive multiple of V₀|u|² with V₀ = L(1) = ¾x_I² + O(x_I³) > 0 (near I₀, ¾ρ_I),
of the same sign; so does the boundary term of the proof of [[prop:iv-4-1]].

*The bulk term.* Modulo ρ₀^(−2α₀)x_I^(−4α_I+1)Diff²_(e,b), L may be replaced by the leading part L₀ of [[eq:iv-2-2]], and
μ_b by μ̄_b := |(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸| ([[lem:iv-2-1]]). Accordingly q(u)μ_b differs from the bulk term q̄(u)μ̄_b of L₀
and μ̄_b by a quadratic form in u and V′u, V′ ∈ {X₀, X_I, x_IΘ}, with coefficients in w²x_IC^∞: the principal symbols of
L and L₀ differ by an element of x_IC^∞(M_♯; S²ᵉᵇTM_♯), V₀ − ¾x_I² ∈ x_I³C^∞, μ_b/μ̄_b ∈ 1 + ρ²C^∞, and
differentiation along eb-vector fields preserves these classes. For L₀ and μ̄_b, X₀ and X_I are skew-adjoint on
L²(μ̄_b), −div_(μ̄_b)W = −V(w²) = w²(2α₀ − 2(1 + κ)α_I), and, with c_A := 1 + 2(α₀ − α_I) + κ(1 − 2α_I) > 0,

    Q̄ := [L₀, W] − (div_(μ̄_b)W)L₀
       = 4|α_I|(X₀ − X_I)*w²(X₀ − X_I) + 4κ(α₀ − α_I)X_I*w²X_I + c_Ax_Iw(Δ̸ + ¾)wx_I                   {#eq:iv-3-3}

exactly. Indeed, put Y₀ := X₀ − X_I, so that L₀ = −2X_IY₀ + ρ_I(Δ̸ + ¾) and V = Y₀ − κX_I. The fields X_I, Y₀, V
commute with each other and with Δ̸, and X_Iw² = −2α_Iw², Y₀w² = −2(α₀ − α_I)w², Vρ_I = −(1 + κ)ρ_I. The angular part
of Q̄ is −w²(Vρ_I)(Δ̸ + ¾) + w²(2α₀ − 2(1 + κ)α_I)ρ_I(Δ̸ + ¾) = c_Aρ_Iw²(Δ̸ + ¾), which is the last term, as x_I and w
commute with Δ̸. The rest is

    [−2X_IY₀, w²V] − 2(2α₀ − 2(1 + κ)α_I)w²X_IY₀
        = −8α_I(α₀ − α_I)w²V + 4(α₀ − α_I)w²X_IV + 4α_Iw²Y₀V − 4(α₀ − (1 + κ)α_I)w²X_IY₀
        = w²(4α_IY₀² − 4κ(α₀ − α_I)X_I²) − 8α_I(α₀ − α_I)w²V,

the terms in X_IY₀ cancelling. On the other side, as X* = −X for X ∈ {X₀, X_I},
4|α_I|Y₀*w²Y₀ = 4α_IY₀w²Y₀ = 4α_Iw²Y₀² − 8α_I(α₀ − α_I)w²Y₀ and
4κ(α₀ − α_I)X_I*w²X_I = −4κ(α₀ − α_I)w²X_I² + 8κα_I(α₀ − α_I)w²X_I, whose first-order terms add up to
−8α_I(α₀ − α_I)w²V. Written with w² in front, as the identity is usually written, the right side of [[eq:iv-3-3]] would
be w²(4α_IY₀² − 4κ(α₀ − α_I)X_I² + c_Aρ_I(Δ̸ + ¾)); that form omits the first-order term −8α_I(α₀ − α_I)w²V, which
carries no factor x_I, so only the symmetric form is exact. Its principal symbol is that of [Hin23a, (3.25)] with
Δ̸ + ¾ in place of Δ̸, which is [[prop:np-10-64]] (3) with q₄ = ¾ and κ in place of c.

So q̄(u) and

    4|α_I|w²|(X₀ − X_I)u|² + 4κ(α₀ − α_I)w²|X_Iu|² + c_Aρ_Iw²(|∇̸u|² + ¾|u|²)

are quadratic forms in u and its first derivatives without products of u with its derivatives, with the same operator
Q̄; such a form is determined by its operator, so the two are equal. As α_I < 0, κ > 0 and α₀ − α_I > 0, all
coefficients are positive, and with ‖wX₀u‖ ≤ ‖w(X₀ − X_I)u‖ + ‖wX_Iu‖ and |Θ_ju| ≤ C|∇̸u|,

    ∫_Ω q̄(u) μ̄_b ≥ c₀ Σ_(V′) ‖wV′u‖²_(L²_b),

the sum over V′ ∈ {X₀, X_I, x_IΘ_j}, with the Θ_j spanning T𝕊³. The constant ¾ only adds the term ¾c_Aρ_Iw²|u|² ≥ 0.

*Poincaré.* Along each integral curve of X_I in Ω, which begins on Σ_in where u = 0, with s := −log ρ_I and ρ₀ fixed,

    ∫ e^(2α_Is)|u|² ds ≤ α_I⁻² ∫ e^(2α_Is)|∂_s u|² ds     (α_I < 0),

by u(s) = ∫_(s₀)^s ∂_s u and Young's inequality for the kernel e^(α_I(s−s′)), s′ < s, of L¹-norm |α_I|⁻¹. The constant
does not depend on where the curve ends, so integrating in ρ₀ and ω gives ‖wu‖_(L²_b) ≤ C‖wX_Iu‖_(L²_b).

*Conclusion for k = 0.* On Ω ⊂ {x_I < c}, |∫_Ω(q(u)μ_b − q̄(u)μ̄_b)| ≤ Cc(Σ_(V′)‖wV′u‖²_(L²_b) + ‖wu‖²_(L²_b)), its
coefficients carrying the factor x_I < c. Cauchy–Schwarz on the left of the identity, ℬ_fin ≥ 0, the Poincaré
inequality and absorption for c small give ‖wu‖_(H¹_(e,b)) ≤ C‖wf‖_(L²_b), which is [[eq:iv-3-2]] for k = 0. Existence
of the forward solution, smooth in Ω, is standard for the wave equation with smooth coefficients on Ω.

*Higher b-regularity* (the induction of [Hin23a]). Let X₀, X₁ := X_I, X₂, …, X₇ be the six rotation fields of 𝕊³
(spanning T𝕊³ pointwise), and X₈ := 1. These span Diff¹_b over C^∞. By [[eq:iv-2-3]], [L, X_j] = Σ_l x_IP_(jl)X_l with
P_(jl) ∈ Diff¹_(e,b). Assume [[eq:iv-3-2]] at k. Applying it to L(X_ju) = X_jf + [L, X_j]u (the support condition is
preserved, the X_j being tangent to the faces and commuting with restriction to Σ_in up to terms vanishing there)
gives, with the weights,

    ‖X_ju‖_(H^((1;k))_(e,b;b)) ≤ C(‖X_jf‖_(H^k_b) + Σ_l ‖x_IX_lu‖_(H^((1;k))_(e,b;b))).

Summing over j, the last sum is absorbed for c small. This gives [[eq:iv-3-2]] at k + 1. The statement on
{x_I ≥ c/2} holds as 𝒱_(e,b) = 𝒱_b there, so [[eq:iv-3-2]] gives one b-derivative more. ∎

**Remark {#rem:iv-3-2}** ([Hin23a, Remark 3.18].) In the coordinates (t, |x|), modulo lower-order terms,
W = |x|^(2α_I)(2 − x¹)^(2(α₀−α_I))((2 − x¹)∂_t + κ|x|(∂_t + ∂_(|x|))).

### The estimate near the interior of I₀ {#sec:iv-4}

Near the interior of I₀, away from ℐ⁺, the coordinates of [[sec:iii-b-2]] are (τ, ρ) = (t/|x|, |x|⁻¹), with
τ ∈ [−½, 1 − δ] (the proof of [[lem:iii-c-1-1]]), and ρ_I = 1 − τ + 2ρ ≥ δ. The following estimate takes the place of
[HV20, Proposition 4.3], which [Hin23a] cites.

**Proposition {#prop:iv-4-1}** (The b-energy estimate near I₀.) Let δ > 0 and
Ω₀ ⊂ {ρ ≤ ρ₁} ∩ {τ₀ ≤ τ ≤ 1 − δ} be open, with interior boundary consisting of {τ = τ₀} (initial) and a hypersurface
Σ_fin that is spacelike or null for g_(b₀) (final). Let k ∈ ℕ₀, α₀ ∈ ℝ, and let f ∈ ρ^(α₀)H^k_b(Ω₀) vanish near
{τ = τ₀}. Then for ρ₁ small the forward solution of Lu = f satisfies
‖u‖_(ρ^(α₀)H^(k+1)_b(Ω₀)) ≤ C‖f‖_(ρ^(α₀)H^k_b(Ω₀)).

*Proof.* In (τ, ρ, ω), ∂_t = ρ∂_τ and ∂_(|x|) = −ρ(τ∂_τ + ρ∂_ρ), so the coordinate fields of η are ρ times b-vector
fields. η⁻¹ is ρ² times a smooth nondegenerate Lorentzian b-metric G_b on {ρ ≤ ρ₁}:

    G_b = −∂_τ² + (τ∂_τ + ρ∂_ρ)² + g̸⁻¹.

G_b(dτ, dτ) = −(1 − τ²) < 0 for |τ| < 1, so τ is a b-time function there. g_(b₀)⁻¹ − η⁻¹ is O(ρ²) relative
([[sec:iv-0]]). So L = ρ_Iρ^(−7/2)□ρ^(3/2) lies in Diff²_b, with principal symbol ρ_IG_b up to O(ρ) and ρ_I ≥ δ.

Use the multiplier W₀ := w₀²V₀, with w₀ := ρ^(−α₀)e^(−Λτ) and V₀ := −G_b(dτ, ·), a future timelike b-vector field. In
the identity 2 Re⟨w₀Lu, w₀V₀u⟩ = ⟨Q₀u, u⟩ + ℬ_fin, the boundary term at Σ_fin is ≥ 0, as in the proof of
[[prop:iv-3-1]], and Q₀ = [L, W₀] − (div W₀)L. There is no boundary term at I₀ in the following approximation.
Approximate f in ρ^(α₀)H^k_b by f_j supported in {ρ ≥ 1/j}. As g_(b₀) − η is O(ρ²) relative, d|x| ≤ (1 + δ/4)dt along
future causal curves in Ω₀ for ρ₁ small; with t ≤ (1 − δ)|x| on Ω₀ and (1 + δ/4)(1 − δ) < 1, the bound
|x| ≤ |x₀| + (1 + δ/4)(t − t₀) along such a curve from (t₀, x₀) ∈ supp f_j keeps |x| bounded. So the forward solution
u_j of Lu_j = f_j vanishes near I₀, the identity holds for it, and the estimate passes to the limit j → ∞ as in the
proof of [[prop:iv-3-1]].

The term of Q₀ from differentiating e^(−2Λτ) is 2Λw₀² times the energy-momentum quadratic form of V₀ and dτ in ρ_IG_b.
It is positive definite in the b-gradient, as V₀ and −∇τ are future timelike (the dominant energy condition for the
scalar wave equation). The other terms are bounded by C(1 + |α₀|)w₀²|ᵇ∇u|² + Cw₀²|u|² with C independent of Λ. The
|u|² term is controlled by integrating ∂_τ from {τ = τ₀}, where u = 0, over the compact τ-interval. For Λ large this
gives the estimate for k = 0, with e^(±Λτ) bounded on [τ₀, 1 − δ].

Higher b-regularity follows by commuting ρ∂_ρ and the rotation fields: their commutators with L lie in Diff²_b and are
of first order in the commuted derivatives, since L is a b-operator. The induction closes on the compact τ-interval
with the same Λ-argument, the commutator terms entering as sources: the estimate for k = 0 has the form
‖w₀∇u‖ ≤ CΛ⁻¹‖w₀f‖, so these sources, of first order in the commuted derivatives, are absorbed for Λ large, and the
∂_τ²-terms of [L, ρ∂_ρ] are recovered from the equation. Commuting ∂_τ is not needed: a b-derivative transversal to the
level sets of τ is recovered from the equation, L being strictly hyperbolic with respect to τ. ∎

**Remark {#rem:iv-4-2}** (Gluing the estimates.) [[prop:iv-3-1]] near ℐ⁺ ∪ (I₀ ∩ ℐ⁺), [[prop:iv-4-1]] near the
interior of I₀, and the standard energy estimate on compact sets cover Ω_(ext,r₀) near infinity. The forward problem
is solved successively: on a region whose past boundary is Σ_IVP, then on the next region with the previous solution as
data. The data enter as sources after an extension of the Cauchy data, cut off near the initial surface, is
subtracted. The regions are ordered by domain of dependence ([[lem:ii-f-1-3]]), as in [Hin23a, p. 16] ("cut and paste
energy estimates using domain of dependence properties"). Where two estimates apply the solutions agree, and the norms
are equivalent on the overlaps, each overlap lying away from the face that distinguishes the two calculi. Ω_(ext,r₀)
also contains the past slab {−(r − r₀)/12 ≤ t_IVP ≤ 0} ([[lem:iii-c1-1-1]]). There the solution is the backward one
from Σ_IVP, near the interior of I₀ (τ ∈ [−1/12 − ε, ε] for r₀ large), and the proof of [[prop:iv-4-1]], run backward
in time, gives it: it uses only the b-structure of L and that dτ is timelike on the τ-range, and Σ_(past,r₀) is
spacelike ([[lem:iii-c1-1-1]]). The backward problem is argued directly because t ↦ −t is not an isometry of the
gauge-fixed operator, whose E_C-term is odd in time. [[lem:iv2-2-2]] writes this backward problem with the data, and
[[prop:iv1-2-2]] and [[thm:iv2-2-4]] give the estimate for the tensor operator, with weights at both faces.

### The tensor operator: setting {#sec:iv1-0}

[[sec:iv1-0]]–[[sec:iv1-2]] carry [Hin23a, Sections 3.4–3.5] (Proposition 3.29, Lemmas 3.33–3.34, Proposition 3.32;
pp. 18–30) to the gauge-fixed operator of [[sec:iii-c-4]] in dimension 4 + 1, on the exterior region of
[[sec:iii-c-1]]. [[sec:iv1-1]] puts the conjugated operator in edge-b form; in dimension 4 + 1 its first-order matrix
is the constant Ā of [[lem:iii-c-4-2]], free of the perturbation h ([[prop:iii-c-4-4]], [[rem:iii-c-4-5]]).
[[sec:iv1-2]] proves the energy estimate for the system, with its tame form and the sharp weights. [Hin23a,
Section 3.3] (metric perturbations, Lemmas 3.23–3.28) is [[sec:iii-c-2]]–[[sec:iii-c-5]] in dimension 4 + 1, which we
use as they stand.

U, M_♯, x_I = ρ_I^(1/2), X₀, X_I, 𝒱_(e,b) and the spaces are those of [[sec:iv-0]], and the splitting
[[eq:iii-c-1-6]], its slots and Ā are those of [[lem:iii-c-4-2]]. Let g₁, g₀ ∈ 𝒢 ([[def:iii-c-3-4]]), k ≥ 5, and
h ∈ H^(k,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b(U; S²T*) as in [[prop:iii-c-4-4]]. That is: ℰ₀ as in [[def:iii-c-3-1]] (1),
min Re ℱ > 0, 2ℱ ⊂ ℱ, ℓ₀, ℓ_I > 0, and h small in H^(k,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b, the polyhomogeneous norm. (The coefficients
ã below are ρ_I⁻¹ times terms in h, whose size near ℐ⁺ the conormal norm H^(k,a₀,a_I)_b does not control when
a_I < 1.) Assume moreover

    min Re ℱ > 1,     ℓ_I > 1,                                                                          {#eq:iv1-0-1}

which holds for ℱ = ℰ_I^tot (min Re ℰ_I^tot = 3/2, [[eq:iii-c-3-1]]) and every ℓ_I > 3/2, and for ℱ = (2, 0). Put
g := g₁ + h and

    L_g := 2ρ_Iρ^(−7/2) L^(g,g₀) ρ^(3/2),                                                               {#eq:iv1-0-2}

with L^(g,g₀) the linearised gauge-fixed operator [[eq:iii-c-4-1]], whose principal part is ½□_g ⊗ Id. For the scalar
operator this is the L of [[eq:iv-2-1]] up to the factor 2: 2L^(g,g₀) has principal part □_g.

### The operator in edge-b form {#sec:iv1-1}

This section is [Hin23a, Proposition 3.29] for the operator of [[sec:iii-c-4]] in dimension 4 + 1 ([Hin26, (5.26b)]).

**Lemma {#lem:iv1-1-1}** (Cartesian derivatives are ρ₀ times eb-vector fields.) On U, ∂_t, ∂_(x^i), ∂₀, ∂₁ lie in
ρ₀𝒱_(e,b)(M_♯), and |x|⁻¹∂_ω ∈ ρ₀x_I𝒱_(e,b)(M_♯).

*Proof.* By [[eq:iii-c-1-5]], ∂₀ = −½ρ₀ρ_IX_I and ∂₁ = ρ₀(X₀ − X_I + ½ρ_IX_I), with X₀, X_I ∈ 𝒱_(e,b). And
|x|⁻¹∂_ω = ρ₀x_I · x_I∂_ω, with x_I∂_ω ∈ 𝒱_(e,b). Finally ∂_t = ∂₀ + ∂₁ and
∂_(x^i) = ω^i(∂₀ − ∂₁) + |x|⁻¹(…)∂_ω, the dots smooth functions of ω. ∎

This refines [[lem:iii-c-1-1]], which places the same fields in ρ₀𝒱_b. The refinement is what the edge-b form needs:
angular second derivatives come with |x|⁻², hence with ρ₀²x_I² times eb-derivatives.

**Proposition {#prop:iv1-1-2}** (The edge-b form.) Under the hypotheses of [[sec:iv1-0]], on U, in the splitting
[[eq:iii-c-1-6]],

    L_g = −2(X_I − Ā)(X₀ − X_I) + x_I²Δ̸ + L̃_g,
    L̃_g ∈ (x_IC^∞(M_♯) + H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b) Diff²_(e,b)(M_♯; S²T*),                      {#eq:iv1-1-1}

where Δ̸ = −g̸^(ab)∂_a∂_b acts on each slot, in local coordinates ω^a of 𝕊³. By [[eq:iv1-0-1]] the coefficients of the
second class decay at ℐ⁺ at least like ρ_I^(γ−ε) for every ε > 0, γ := min(min Re ℱ − 1, ℓ_I − 1) > 0, and are small
in L^∞ near ℐ⁺ for h small. So L̃_g is small relative to the leading part near ℐ⁺, as [Hin23a, (3.29b)] is.

*Proof.* *The conjugation.* By [[prop:iii-c-4-4]],

    L^(g,g₀) = −ρ₀²ρ_I(X_I − 3/2 − Ā)(X₀ − X_I) + R,     R ∈ (ρ₀²ρ_I²C^∞ + H^(k−2,(ℰ₀+2,ℓ₀+2),(ℱ,ℓ_I))_b)Diff²_b.

As (X₀ − X_I)ρ = 0 and X_Iρ^(3/2) = (3/2)ρ^(3/2), ρ^(−3/2)(X_I − 3/2 − Ā)(X₀ − X_I)ρ^(3/2) = (X_I − Ā)(X₀ − X_I); and
2ρ_Iρ^(−7/2) · ρ₀²ρ_I · ρ^(3/2) = 2. So the leading part of [[eq:iv1-1-1]] is the image of that of [[eq:iii-c-4-4]],
and L_g + 2(X_I − Ā)(X₀ − X_I) = 2ρ₀⁻²ρ_I⁻¹ρ^(−3/2)Rρ^(3/2). Conjugation by ρ^(3/2) preserves Diff_b and Diff_(e,b), as
ρ^(−3/2)Vρ^(3/2) = V + (3/2)V(log ρ) with V log ρ smooth for V ∈ 𝒱_b.

*The b-form remainder does not suffice.* ρ₀⁻²ρ_I⁻¹R lies in (ρ_IC^∞ + H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b)Diff²_b. But
Diff²_b ⊂ x_I⁻²Diff²_(e,b) only, ∂_ω being x_I⁻¹ times an eb-vector field. So we redo the count of the proof of
[[prop:iii-c-4-4]] with [[lem:iv1-1-1]] in place of [[lem:iii-c-1-1]].

*The background part.* L^(g₁,g₀) differs from L_(b₀) := L^(g_(b₀),g_(b₀)) by terms with a factor g₁ − g_(b₀) or
g₀ − g_(b₀) in ρ₀²ρ_I²C^∞ ([[def:iii-c-3-4]], [[lem:iii-c-3-5]]). By [[lem:iii-c-4-3]] and [[lem:iv1-1-1]], these lie
in ρ₀² · ρ₀²ρ_I²C^∞Diff²_(e,b). After the prefactor 2ρ₀⁻²ρ_I⁻¹ this is ρ₀²ρ_IC^∞Diff²_(e,b) ⊂ x_I²Diff²_(e,b). For
L_(b₀) itself:

- its second-order part is ½□_(g_(b₀)) on each component in the frame, the principal symbol being scalar;
- its first-order part consists of the connection terms of the frame and the terms of E_C, E_Υ. These are Cartesian
  derivatives (in ρ₀𝒱_(e,b), [[lem:iv1-1-1]]) times coefficients in ρC^∞ = ρ₀ρ_IC^∞ (c_C, c_Υ and the Christoffel
  symbols of η in the frame are O(|x|⁻¹), [[def:iii-b-6-1]], [[lem:iii-c-1-3]]), so they lie in
  ρ₀²ρ_IC^∞Diff¹_(e,b);
- its zeroth-order part lies in ρ²C^∞.

The calculation of [[lem:iii-c-4-1]] identifies the part of the first-order terms that is not O(x_I) relative: it is
ρ₀²ρ_IĀ(X₀ − X_I) (with the −3/2 of the scalar conjugation). So, after conjugation and the prefactor,

    L_(b₀,conj) = (2ρ_Iρ^(−7/2) ½□_(g_(b₀)) ρ^(3/2)) ⊗ Id + 2Ā(X₀ − X_I) + x_IC^∞Diff¹_(e,b) + x_I²C^∞.

The scalar term is the L of [[lem:iv-2-2]]: −2X_I(X₀ − X_I) + x_I²(Δ̸ + ¾) modulo x_IDiff²_(e,b). Its first-order part
in [[lem:iv-2-2]] is that of the scalar wave operator, and it differs from that of the frame by the connection terms
just counted. ¾x_I² and x_IC^∞Diff¹_(e,b) (the angular connection terms) lie in x_IDiff¹_(e,b). So the background
part of [[eq:iv1-1-1]] holds with L̃ in x_IC^∞Diff²_(e,b).

*The perturbation.* For (g₁ + h, g₀) against (g₁, g₀) the factor is δ = h. By [[lem:iii-c-4-3]] and [[lem:iv1-1-1]],
each term is ρ₀² times a product of h or of 𝒱_b-derivatives of h of order at most 2 with smooth bounded functions,
applied through Diff²_(e,b) ([[lem:iv1-1-1]] replaces ρ₀𝒱_b by ρ₀𝒱_(e,b) for the derivatives acting on u). By the
proof of [[prop:iii-c-4-4]] (the Neumann series, and [[lem:iii-c-2-1]] there), the coefficients lie in
ρ₀²H^(k−2,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b = H^(k−2,(ℰ₀+2,ℓ₀+2),(ℱ,ℓ_I))_b. After the prefactor they lie in
H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b, multiplying Diff²_(e,b). The frame change of [[lem:iii-c-1-3]] preserves the classes, as
in the proof of [[prop:iii-c-4-4]].

*Smallness.* By [[eq:iv1-0-1]] and the embedding [[eq:iv-0-1]] (k − 2 ≥ 3), elements of
H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b are bounded by Cρ₀^(min(min Re ℰ₀,ℓ₀))ρ_I^(γ−ε) times their norm, with γ as above, and
their norm is O(‖h‖_(H^k)). ∎

**Remark {#rem:iv1-1-3}** (The terms A_g and B_g of [Hin23a].) In [Hin23a, (3.29a)] the h-dependent entries of A_g
and the term B_g are of the size of the leading part at ℐ⁺; in dimension 3 + 1 they are bounded there. In dimension
4 + 1 they carry an extra factor ρ_I^(1/2) ([[prop:np-10-64]] (7), [[rem:iii-c-4-5]]) and lie in L̃_g. So the
first-order matrix of [[eq:iv1-1-1]] is Ā, constant and lower triangular, with diagonal [[eq:iii-c-4-3]], all of whose
entries are ≥ 0:

    2(1 − v_C)γ_C,  (1 − v_C)γ_C,  (1 − e_C)(1 − v_C)γ_C,  (1 − e_Υ)γ_Υ,  γ_Υ,  0,  2γ_Υ.

The term A⁰_h of [Hin23a], for which its proof of Proposition 3.32 uses [Hin23a, Lemma 3.33], does not arise
([[prop:iii-c-4-4]], [[rem:iii-c-4-5]]): all of the h-dependent first-order part is treated like the contribution of
L̃_g.

### The energy estimate for the system {#sec:iv1-2}

This section is [Hin23a, Proposition 3.32 and Lemmas 3.33–3.34] in dimension 4 + 1.

**Lemma {#lem:iv1-2-1}** (A fibre inner product.) For every ε > 0 there is a constant positive definite inner product
⟨·, ·⟩_ε on the fibres of S²T*, in the frame [[eq:iii-c-1-6]], such that

    Ā = D + N_ε,     D = diag(d₁, …, d₇) ⊗ Id_slot,     |N_ε|_ε ≤ ε,

with the diagonal [[eq:iii-c-4-3]], d_j ≥ 0, and D self-adjoint for ⟨·, ·⟩_ε.

*Proof.* Take the slots of [[eq:iii-c-1-6]] orthogonal, each with its standard inner product multiplied by ε^(2j) on
slot j. Ā maps each slot to slots of the same type by scalars and is lower triangular ([[lem:iii-c-4-2]]). An entry
Ā_(ji), i < j, which maps slot i to slot j, then has norm ε^(j−i)|Ā_(ji)| in the scaled norms. For ε ≤ 1 this is at
most ε max|Ā_(ji)|; rename ε. D is diagonal in an orthogonal splitting, so self-adjoint. ∎

**Proposition {#prop:iv1-2-2}** (The energy estimate and its tame form; [Hin23a, Proposition 3.32] in dimension
4 + 1.) Let Ω, Σ_in, Σ_fin be as in [[sec:iv-3]], and α₀, α_I ∈ ℝ with α_I < min(α₀, 0). Let k ≥ 8 and 3 ≤ m ≤ k − 3,
and let h be as in [[sec:iv1-0]], small in H^(8,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b. For f ∈ H^(m,(α₀,2α_I))_b(Ω; S²T*) vanishing near
Σ_in, the forward solution u of L_gu = f lies in H^((1;m),(α₀,2α_I))_(e,b;b)(Ω; S²T*), and

    ‖u‖_(H^((1;m),(α₀,2α_I))_(e,b;b)) ≤ C(‖f‖_(H^(m,(α₀,2α_I))_b)
                                           + ‖h‖_(H^(m+3,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b)‖f‖_(H^(3,(α₀,2α_I))_b)),     {#eq:iv1-2-1}

with C depending on m, k, α₀, α_I and the classes, not on f or h.

*Proof.* *The basic estimate.* Use the multiplier W = w²V of the proof of [[prop:iv-3-1]], V = X₀ − (1 + κ)X_I, with
κ > 0 to be fixed, the density μ̄_b, and the fibre inner product of [[lem:iv1-2-1]]. Then

    2 Re⟨wL_gu, wVu⟩ = ⟨Qu, u⟩ + ℬ_fin(u),     Q = [L_g, W] − (div W)L_g + (L_g* − L_g)W,

with ℬ_fin ≥ 0, as in [[prop:iv-3-1]]. Write

    Y := w(X₀ − X_I)u,     Z := wX_Iu,     Vu = w⁻¹(Y − κZ).

The scalar part −2X_I(X₀ − X_I) + x_I²Δ̸ acts on each slot, and the fibre inner product is constant; so it gives the Q̄
of [[eq:iv-3-3]] with Δ̸ in place of Δ̸ + ¾, whose bulk term is, by the proof of [[prop:iv-3-1]],
4|α_I||Y|² + 4κ(α₀ − α_I)|Z|² + c_Aρ_Iw²|∇̸u|² (the ¾ of [[eq:iv-3-3]] only added a nonnegative term).

The first-order term 2Ā(X₀ − X_I) of [[eq:iv1-1-1]] contributes, up to terms of order 0 in u and terms with a factor
x_I,

    4 Re⟨ĀY, Y − κZ⟩ = 4⟨DY, Y⟩ − 4κ Re⟨DY, Z⟩ + O(ε)(|Y|² + |Z|²).

On each slot, the quadratic form in (Y_j, Z_j) from the scalar part and this term is

    4(d_j − α_I)|Y_j|² − 4κd_j Re(Y_jZ̄_j) + 4κ(α₀ − α_I)|Z_j|².

It is positive definite if 4(d_j − α_I)(α₀ − α_I) > κd_j². As d_j ≥ 0, α_I < 0 and α₀ > α_I, this holds for κ > 0
small. Fix such κ, then ε small. The angular term c_Aρ_Iw²|∇̸u|² is nonnegative and bounds Σ_j|x_IwΘ_ju|²/C, so
⟨Qu, u⟩ controls ‖wu‖²_(H¹_(e,b)) modulo two terms: ‖wu‖²_(L²_b), which the Poincaré inequality of the proof of
[[prop:iv-3-1]] removes; and the contribution of L̃_g, whose coefficients are O(c^(γ′)) on {x_I < c} for every
γ′ < min(2 min Re ℱ − 2, 2ℓ_I − 2) by the smallness in [[prop:iv1-1-2]], and which is absorbed for c small, as in
[[prop:iv-3-1]].

The term (L_g* − L_g)W is that of the first-order part, already counted, plus that of L̃_g. This gives

    ‖u‖_(H^(1,(α₀,2α_I))_(e,b)) ≤ C₀‖L_gu‖_(H^(0,(α₀,2α_I))_b),                                         {#eq:iv1-2-2}

with C₀ uniform for h small in H^(5,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b ([Hin23a, (3.53)]; the skew part needs ã ∈ W^(1,∞), so h ∈ H⁶,
which the hypothesis on H⁸ gives). Away from ℐ⁺, the argument of the proof of [[prop:iv-4-1]] applies to the system:
the principal part is scalar, and the first-order terms are bounded b-operators, absorbed by the exponential weight.
[[rem:iv-4-2]] glues the pieces.

*Commuting.* With X₀, X₁ := X_I, the rotation fields X₂, …, X₇ of 𝕊³ (acting on the slots in the frame
[[eq:iii-c-1-6]], which they preserve, by the equivariance of [[lem:iii-c-4-2]]) and X₈ := 1, apply [[eq:iv1-2-2]] to
X_(j₁)⋯X_(j_l)u, l ≤ m. [[lem:iv1-2-4]] gives ([Hin23a, (3.55)], with the weights (α₀, 2α_I) throughout)

    ‖u‖_(H^((1;m))_(e,b;b))
        ≤ C₀(‖L_gu‖_(H^m_b) + Σ_(1≤q≤l≤m) Σ ‖(ad_(X_(i₁))⋯ad_(X_(i_q))L_g) X_(j₁)⋯X_(j_(l−q))u‖_(H⁰_b)),   {#eq:iv1-2-3}

the inner sum over the indices. The commutators of the X_j with the leading part of [[eq:iv1-1-1]] lie in
x_IDiff^(1;1)_(e,b;b): for the scalar part by [[lem:iv-2-2]]; and Ā is constant and commutes with the X_j (X₀, X_I act
on the slot coordinates, and the rotations commute with Ā by the equivariance of [[lem:iii-c-4-2]]). These terms are
absorbed for x_I small. For L̃_g = Σ_i(x_Ia_i + ã_i)P_i, with a_i ∈ C^∞, ã_i ∈ H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b and P_i
spanning Diff²_(e,b), the x_Ia_i-terms are absorbed. By Leibniz's rule the ã_i-terms are sums of products
(V₁⋯V_qã)(W′V′₁⋯V′_ru), q + r ≤ m + 1, with V_l, V′_l among the X_j and W′ an eb-vector field, up to smooth bounded
factors (the commutators of the X_j with P_i stay in Diff²_(e,b), as said below, and expanding smooth coefficients
produces only terms of this kind). For q = 0 such a product is bounded by
‖ã‖_(L^∞)‖u‖_(H^((1;m))) ≤ C‖ã‖_(H³)‖u‖_(H^((1;m))). For q ≥ 1, move W′ to the right of the V′_l: as [X_j, W′] is an
eb-vector field for each X_j, this costs only products of the same form with fewer V′_l. Put f := V_qã and g := W′u,
so that the remaining q − 1 derivatives fall on f and r ≤ m − q + 1 on g. We reduce to the estimate for products of
derivatives, [[thm:std-gn-moser]] (2) with s := m, through the charts of the proof of [[lem:iv1-2-3]]. Divide out the
weights, and extend f and g from Ω to M_♯ by the operator of that proof, which is bounded on H^m_b and on L^∞. Let φ_i
be the partition of unity and ψ_i the cut-offs of that proof, ψ_i = 1 near supp φ_i. The product
Π := (V₁⋯V_qã)(V′₁⋯V′_rW′u) is Σ_i φ_iΠ, and on supp φ_i it equals (V₁⋯V_(q−1)(ψ_if))(V′₁⋯V′_r(ψ_ig)). In the chart of
index i each V_l and each V′_l is a combination of the fields of 𝒱 (the two coordinate fields of ℝ² and the rotation
fields of 𝕊³) with coefficients bounded with all their derivatives; expanding the compositions by Leibniz's rule, φ_iΠ is
a finite sum of terms c(Q′(ψ_if))(Q″(ψ_ig)) with c bounded and Q′, Q″ compositions of at most q − 1 and at most r fields
of 𝒱, so of at most m fields in all. In the chart, [[thm:std-gn-moser]] (2) bounds each term in L² by
C(‖ψ_if‖_(L^∞)‖ψ_ig‖_(H^m) + ‖ψ_if‖_(H^m)‖ψ_ig‖_(L^∞)), and the chart comparison and the boundedness of multiplication by
ψ_i in the proof of [[lem:iv1-2-3]] bound these norms by those of f and g. Summing over i gives

    ‖(V₁⋯V_qã)(V′₁⋯V′_rW′u)‖ ≤ C(‖V_qã‖_(L^∞)‖W′u‖_(H^m_b) + ‖V_qã‖_(H^m_b)‖W′u‖_(L^∞))
                              ≤ C(‖ã‖_(H⁴)‖u‖_(H^((1;m))) + ‖ã‖_(H^(m+1))‖u‖_(H^((1;3)))),

by [[eq:iv-0-1]] (H³_b ⊂ L^∞) and ‖W′u‖_(H^j_b) ≤ C‖u‖_(H^((1;j))), which holds by moving W′ to the left in the same way.
The first term is absorbed near ℐ⁺, the coefficients decaying at ℐ⁺; the second is bounded by ‖h‖_(H^(m+3)) times
the bound of [[eq:iv1-2-1]] at m = 3 for ‖u‖_(H^((1;3))), by ‖ã_i‖_(H^(m+1)) ≤ C‖h‖_(H^(m+3)) (the coefficients are
rational in at most two b-derivatives of h). Commutators of the X_j preserve Diff^k_(e,b): for X₀, X_I as eb-vector
fields, and for the rotations by the argument for [[eq:iv-2-3]] ([Hin23a, (3.19a)–(3.19b)]). This proves
[[eq:iv1-2-1]]. At m = 3 the constant depends on ‖h‖_(H⁸) ([Hin23a, (3.54)]). ∎

**Lemma {#lem:iv1-2-3}** (Moser estimates on M_♯.) Let s ≥ 0 be an integer, and let Ω be M_♯ or a domain in it whose
boundary hypersurfaces in the interior are, in the charts of the proof, graphs over coordinate hyperplanes of functions
bounded with all their derivatives; the domains of this chapter on which the lemma is used are of this kind (Ω_c, Ω_N,
Ω⁺₁, Ω_(ext,r₀) and the parts cut from them by level sets of ρ_I, τ′ and t_IVP). For a, b on Ω with finite right side,

    ‖ab‖_(H^(s,(β₀+γ₀,β₁+γ₁))_b(Ω)) ≤ C(‖a‖_(ρ₀^(β₀)x_I^(β₁)L^∞)‖b‖_(H^(s,(γ₀,γ₁))_b(Ω))
                                        + ‖a‖_(H^(s,(β₀,β₁))_b(Ω))‖b‖_(ρ₀^(γ₀)x_I^(γ₁)L^∞)),

and for s ≥ 3 > 5/2 = ½ dim M_♯, H^s_b embeds in L^∞ ([[eq:iv-0-1]]). Every Sobolev order in this chapter is an integer.

*Proof.* Multiplication by ρ₀^(β₀)x_I^(β₁) maps H^s_b and L^∞ onto the weighted spaces, so we may take all weights 0.
For s = 0 the bound is ‖ab‖_(L²) ≤ ‖a‖_(L^∞)‖b‖_(L²); let s ≥ 1.

*On M_♯.* Cover M_♯ by finitely many charts: near I₀ ∩ ℐ⁺ the coordinates (z₀, z₁, ω), z₀ := log ρ₀, z₁ := log x_I;
near the interior of I₀, (log ρ, τ, ω); near the interior of ℐ⁺, (log ρ₀, log x_I, ω) with ρ₀ in a compact interval;
and a relatively compact part. In each chart the b-vector fields are combinations, with coefficients bounded with all
their derivatives, of the two coordinate fields of ℝ² and the rotation fields of 𝕊³, and conversely, and the b-density
is bounded above and below by the product measure. So for functions supported in a chart, extended by 0, the norm of
H^s_b is equivalent to that of H^s(ℝ² × 𝕊³) of [[cor:std-moser-product]] (2), with k = 2, N = 𝕊³ and 𝒱 those fields.
Let φ_i be a partition of unity on M_♯ subordinate to the charts and ψ_i ∈ C^∞(M_♯) supported in them with ψ_i = 1
near supp φ_i; multiplication by these is bounded on H^s_b. Then ab = Σ_i(ψ_ia)(φ_ib), and [[cor:std-moser-product]]
(2) applied to each product gives the bound.

*On a domain Ω.* After a partition of unity in ω, a diffeomorphism that flattens the boundary hypersurfaces of Ω, with
its derivatives and those of its inverse bounded (composition with it is bounded on every W^(j,2) and on L^∞, by the
chain rule), makes Ω locally a half-space or, near an edge where two of them meet, a quadrant. The extension operator of
[[thm:std-ly-extension]] acts in the normal variable alone, the others being parameters, so its bounds hold fibrewise; it
is one operator bounded on every W^(j,2) and on L^∞. Applied in the normal variable of each hypersurface in turn, it
gives extensions Ea, Eb of a, b to M_♯ with ‖Ea‖_(H^s_b) ≤ C‖a‖_(H^s_b(Ω)), ‖Ea‖_(L^∞) ≤ C‖a‖_(L^∞(Ω)), and likewise for
b. As ab = (Ea)(Eb) on Ω, the bound on M_♯ gives the bound on Ω. ∎

**Lemma {#lem:iv1-2-4}** ([Hin23a, Lemma 3.34], the commutator identity.) In any associative algebra, for
L, Z₁, …, Z_l, with ad_Z := [·, Z],

    [L, Z₁⋯Z_l] = Σ_(q=1)^l (−1)^(q−1) Σ_(i₁<⋯<i_q) (ad_(Z_(i₁))⋯ad_(Z_(i_q))L) Π_(j∉{i₁,…,i_q}) Z_j,

the products taken in increasing order of j.

*Proof.* Induction on l: [L, Z₁⋯Z_(l+1)] = [L, Z₁⋯Z_l]Z_(l+1) + [L, Z_(l+1)]Z₁⋯Z_l − [ad_(Z_(l+1))L, Z₁⋯Z_l], since
Z₁⋯Z_l[L, Z_(l+1)] = [L, Z_(l+1)]Z₁⋯Z_l − [ad_(Z_(l+1))L, Z₁⋯Z_l]; the induction hypothesis applied to the first and the
last term gives the formula for l + 1. ∎

**Remark {#rem:iv1-2-5}** ([Hin23a, Lemma 3.33].) The tame product estimate of [Hin23a, Lemma 3.33], with the
Sobolev index d_(dim M−1), is used in [Hin23a] only for the term A⁰_h, which does not arise in dimension 4 + 1
([[rem:iv1-1-3]]). In dimension 4 + 1 its index is d₄ = 3 ([[prop:np-10-64]] (6)).

### Sharp decay: the setting {#sec:iv2-0}

[[sec:iv2-0]]–[[sec:iv2-4]] carry [Hin23a, Section 3.6] (Theorem 3.35, Corollary 3.36; pp. 30–32) to the gauge-fixed
operator of [[sec:iii-c-4]] in dimension 4 + 1 on the exterior domain Ω_(ext,r₀) of [[lem:iii-c1-1-1]]. They give the
linear estimate with its tame form ([[thm:iv2-2-4]]), the nonlinear solution ([[thm:iv2-3-1]]) and the backward
solution on the past slab ([[lem:iv2-2-2]]), and both in the cut-off gauge of [[sec:iii-c2-2]] and for the
backgrounds of [[rem:iii-c1-2-2]] (2) ([[cor:iv2-4-1]]). [[sec:iv2-1]] integrates the leading part along its two
families of curves; [[sec:iv2-2]] proves the linear theorem in three steps: the Cauchy problem near the interior of I₀,
the energy estimate of [[prop:iv1-2-2]] near ℐ⁺, and the recovery of the sharp weight at ℐ⁺; [[sec:iv2-3]] applies
[[thm:ii-g-2-1]]. In dimension 4 + 1 the recovery needs two integrations and no leading terms depending on h
([[rem:iv1-1-3]]), and only slot 6 carries a radiation field. [[lem:iv2-1-1]], [[lem:iv2-1-2]] and
[[lem:iv2-2-1]] are stated so that the continuation of the solution near ℐ⁺ on a slab beyond Σ_(fut,r₀), which the
nonlinear theorem of [[ch:s27]] poses, can use them.

U, M_♯, x_I = ρ_I^(1/2), X₀, X_I, the edge-b and b-spaces and the weights are those of [[sec:iv-0]]; the splitting
[[eq:iii-c-1-6]], its slots 1–7 and Ā are those of [[lem:iii-c-4-2]]; L_g is [[eq:iv1-0-2]]. As in [[sec:iv-0]],
H^(k,(a₀,2a_I))_b = ρ₀^(a₀)ρ_I^(a_I)H^k_b, the weight at ℐ⁺ in this notation being written in powers of x_I; all other
weights at ℐ⁺ below are powers of ρ_I.

*Parameters.* ℓ^♭₀, ℓ^♭_I are as in [[eq:iii-c1-1-1]], and

    β := ℓ^♭_I − 3/2 ∈ (0, ½),     β < d_* := min_(j≠6) Ā_(jj) = (1 − e_Υ)γ_Υ.                           {#eq:iv2-0-1}

The diagonal [[eq:iii-c-4-3]] is 2(1 − v_C)γ_C, (1 − v_C)γ_C, (1 − e_C)(1 − v_C)γ_C, (1 − e_Υ)γ_Υ, γ_Υ, 0, 2γ_Υ; the
first three exceed 100 ([[sec:iii-f-1]]: (1 − e_C)(1 − v_C)γ_C > 100, 0 < e_C, v_C < 1), and
(1 − e_Υ)γ_Υ ≤ γ_Υ ≤ 2γ_Υ; so d_* = (1 − e_Υ)γ_Υ, and β < d_* is the condition ℓ^♭_I < 3/2 + (1 − e_Υ)γ_Υ of
[[eq:iii-c1-1-1]]. By [[lem:iii-c-4-2]] the off-diagonal entries of Ā are at (3, 1), (4, 1), (4, 3), (5, 2), (7, 3) and
(7, 4): no row couples to slot 6, and row 6 has no off-diagonal entry.

*Conjugation.* For a symmetric 2-tensor ġ on U put u := ρ^(−3/2)ġ. Then

    L^(g,g₀)ġ = f   ⟺   L_gu = f_♭ := 2ρ_Iρ^(−7/2)f.                                                  {#eq:iv2-0-2}

Multiplication by ρ^(±3/2) = ρ₀^(±3/2)ρ_I^(±3/2) and by ρ_I maps weighted b-Sobolev spaces isomorphically onto each
other with the weights shifted (b-derivatives of these functions are constant multiples of them). So
ġ ∈ H^(k,α₀,α_I)_b if and only if u ∈ H^(k,(α₀−3/2,2(α_I−3/2)))_b, and f ∈ H^(k,α₀+2,α_I+1)_b if and only if
f_♭ ∈ H^(k,(α₀−3/2,2(α_I−3/2)))_b. Put a₀ := α₀ − 3/2.

*The classes of [[thm:iii-c1-2-1]] in these terms.* The forcing class H^(k,α₀+2,(−′,ℓ^♭_I+1))_b ([[def:iii-c-5-1]]
(2)) has every slot in H^(k,α₀+2,ℓ^♭_I+1)_b near ℐ⁺: its index sets ℰ_I^C + 1 and ℱ_(I,11) have real parts above
ℓ^♭_I + 1 (by [[eq:iii-c1-1-1]], and min Re ℱ_(I,11) ≥ 5/2 + (1 − e_Υ)γ_Υ by [[eq:iii-c-5-1]]). So
f_♭ ∈ H^(k,(a₀,2β))_b in every slot. The solution class H^(k,α₀,(−,ℓ^♭_I))_b ([[sec:iii-c1-1]]) has every slot in
H^(k,α₀,ℓ^♭_I)_b except π̸₀ġ ∈ H^(k,α₀,((3/2,0),ℓ^♭_I))_b. In terms of u it is

    𝒴^k_(a₀)(Ω) := {u : u_j ∈ H^(k,(a₀,2β))_b (j ≠ 6),  u₆ = χ_Iu^((0)) + ũ₆,
                         u^((0)) ∈ H^(k,a₀)_b(ℐ⁺_c),  ũ₆ ∈ H^(k,(a₀,2β))_b},                             {#eq:iv2-0-3}

with χ_I := χ̂(ρ_I), χ̂ ∈ C_c^∞([0, c/2)) equal to 1 on [0, c/4], c the constant of [[lem:iv2-2-1]] (so u^((0)) is used
only over Ω_c := Ω⁺ ∩ {ρ_I < c}, Ω⁺ as below; another such χ̂ gives an equivalent norm), and u^((0)) a function of
(ρ₀, ω) extended to be constant in ρ_I. Here ℐ⁺_c is the image of Ω_c under (ρ₀, ρ_I, ω) ↦ (ρ₀, ω), a domain in ℐ⁺
containing ℐ⁺ ∩ Ω̄_c and in general larger: an integral curve of X_I near Σ_(fut,r₀) leaves Ω⁺ through Σ_(fut,r₀) before
it reaches ℐ⁺. So the splitting u₆ = χ_Iu^((0)) + ũ₆ is determined by u over ℐ⁺ ∩ Ω̄_c, where ρ₀^(3/2)u^((0)) is the
radiation field of π̸₀ġ (the coefficient of ρ_I^(3/2)), and not elsewhere; the norm of 𝒴^k_(a₀) is therefore the
infimum over the splittings ([[lem:s26-decompositions]]). Away from U the classes impose only H^k.

*The operator.* Let g₀ ∈ 𝒢 ([[def:iii-c-3-4]]) with Ric(g₀) = 0 and g₀ − g_(b₀) small in the sense of the pointwise
bounds of the proof of [[lem:iii-c1-1-1]], or g₀ = g_(b₀); let h ∈ H^(∞,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀); S²T*) and
g := g₀ + h. In the terms of [[sec:iv1-0]], h ∈ H^(k,(ℰ₀,ℓ₀),(ℱ,ℓ_I))_b for every k, with ℰ₀ := ∅, ℓ₀ := ℓ^♭₀,
ℱ := ⋃_(j≥1)(3j/2, 0) and ℓ_I := ℓ^♭_I: ℱ + ℱ ⊂ ℱ, and [[eq:iv1-0-1]] holds, as min Re ℱ = 3/2 and ℓ^♭_I > 3/2. So
[[prop:iv1-1-2]] applies to L_g on U: in its coefficient class H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b the exponents at ℐ⁺ are at
least ½ and the weight is ℓ^♭_I − 1 > ½, so

    L̃_g = x_I Σ_i (a_i + ã_i)P_i,     a_i ∈ C^∞(M_♯),     ã_i ∈ x_I⁻¹H^(k−2,(ℰ₀,ℓ₀),(ℱ−1,ℓ_I−1))_b,
    P_i ∈ Diff²_(e,b),                                                                                   {#eq:iv2-0-4}

with ã_i bounded (its expansion at ℐ⁺ starts at ρ_I⁰) and ‖ã_i‖_(H^j) ≤ C‖h‖_(H^(j+2)) in these classes (the proof of
[[prop:iv1-1-2]]: the coefficients are rational in h and in two b-derivatives of it). L denotes L^(g,g₀), or
L^(χ₀)_(g,g₀) in [[sec:iv2-4]].

*Domains.* Ω⁺ := Ω_(ext,r₀) ∩ {t_IVP ≥ 0} and the past slab Ω⁻ := Ω_(ext,r₀) ∩ {t_IVP ≤ 0}. For |x| ≥ R₃,
t_IVP = t − C″ ([[lem:iii-b-3-7]] (b)), and

    Ω⁺ = {0 ≤ t_IVP ≤ F₀(|x|)},     F₀(r) := r + 2r^(1−ℓ^♭_I) − (r₀ + 2r₀^(1−ℓ^♭_I)),                    {#eq:iv2-0-5}

which is empty where r < r₀; Ω_(ext,r₀) ⊂ U ∩ {|x| ≥ r₀} (the proof of [[lem:iii-c1-1-1]]). Near the interior of I₀,
τ := t/|x| and ρ = |x|⁻¹ are the coordinates of [[sec:iii-b-2]], ρ_I = 1 − τ + 2ρ ([[sec:iv-4]]), and
τ′ := t_IVP/|x| = τ − C″ρ.

### The two families of curves {#sec:iv2-1}

This section gives the integrations of [Hin23a, Theorem 3.35] along the integral curves of X_I and of X₀ − X_I.

**Lemma {#lem:iv2-1-1}** (The curves.) Let c ∈ (0, ½] and r₀ ≥ R₀ (so r₀ ≥ 4|C″| + 4).

(a) {ρ_I = c} ∩ U = {t = (1 − c)|x| + 2} is spacelike for g_(b₀) near infinity, and {ρ_I < c} lies to its future.
Ω⁻ ⊂ {ρ_I ≥ ½}.

(b) Let p ∈ Ω⁺ with ρ_I(p) < c. The integral curve of X_I through p (at fixed ρ₀ and ω: the outgoing ray of η at fixed
x¹) and that of X₀ − X_I (at fixed |x| and ω), followed in the direction of increasing ρ_I, stay in Ω⁺ until they reach
{ρ_I = c}, which they do.

*Proof.* (a) ρ_I = (2 − x¹)/|x| = c if and only if t = (1 − c)|x| + 2. For η, ζ := dt − (1 − c)d|x| has
η⁻¹(ζ, ζ) = −1 + (1 − c)² < 0; the correction from g_(b₀) − η, O(|x|⁻²) in the frame ([[lem:iii-c-1-3]]), does not
change the sign for |x| large. Along ∂_t, ρ_I decreases. On Ω⁻, t ≤ C″, so ρ_I ≥ (2 − C″ + |x|)/|x| ≥ ½ for |x| ≥ r₀.

(b) *The X_I-curve.* Along it x¹ = x¹_p is fixed and |x| decreases from |x|_p to r_c := (2 − x¹_p)/c, where ρ_I = c.
The upper condition of [[eq:iv2-0-5]] is x¹ ≤ C″ − r₀ − 2r₀^(1−ℓ^♭_I) + 2|x|^(1−ℓ^♭_I), whose right side decreases in
|x| (ℓ^♭_I > 1); it holds at p, so at every smaller |x|. It gives x¹_p ≤ C″ − r₀ < 0. The lower condition is
x¹_p + |x| ≥ C″, and x¹_p + |x| decreases along the curve; at r_c, x¹_p + r_c = x¹_p(1 − c⁻¹) + 2c⁻¹ ≥ |x¹_p|
≥ r₀ − C″ > C″, as c⁻¹ − 1 ≥ 1. And r_c ≥ (2 + r₀ − C″)/c ≥ r₀. *The (X₀ − X_I)-curve.* Along it |x| = |x|_p and t
decreases to t_c := (1 − c)|x|_p + 2. The upper condition is monotone in t; the lower one holds at t_c, as
t_c − C″ ≥ ½|x|_p + 2 − C″ > 0. In both cases ρ_I increases to c along the curve. ∎

Both curves are integral curves of commuting b-vector fields: in the coordinates (ρ₀, ρ, ω), X_I = ρ∂_ρ at fixed ρ₀ and
X₀ − X_I = ρ₀∂_(ρ₀) at fixed ρ; X₀, X_I and the rotation fields of 𝕊³ commute with both.

**Lemma {#lem:iv2-1-2}** (Integration.) Let c, r₀ be as in [[lem:iv2-1-1]], Ω_c := Ω⁺ ∩ {ρ_I < c}, m ∈ ℕ₀, a₀, γ ∈ ℝ,
and let w ∈ H^(m,(a₀,2γ))_b(Ω_c) vanish on {ρ_I > c/2}. Let v on Ω_c vanish on {ρ_I > c/2}.

(a) If (X_I − d)v = w with d > γ, then ‖v‖_(H^(m,(a₀,2γ))_b) ≤ (d − γ)⁻¹‖w‖_(H^(m,(a₀,2γ))_b).

(b) If X_Iv = w and γ > 0, then v = v^((0)) + ṽ on Ω_c, with v^((0)) a function of (ρ₀, ω) on ℐ⁺_c, the image of Ω_c
under (ρ₀, ρ_I, ω) ↦ (ρ₀, ω) (as after [[eq:iv2-0-3]]), v^((0)) and ṽ depending linearly on w, and

    ‖v^((0))‖_(H^(m,a₀)_b(ℐ⁺_c)) ≤ C(2γ)^(−1/2)c^γ‖w‖_(H^(m,(a₀,2γ))_b),
    ‖ṽ‖_(H^(m,(a₀,2γ))_b) ≤ Cγ⁻¹‖w‖_(H^(m,(a₀,2γ))_b),

with C depending only on m and Ω_c. Over a point of ℐ⁺_c whose X_I-curve lies in Ω_c for all ρ_I < c, v^((0)) is the
limit of v along that curve as ρ_I → 0.

(c) If (X₀ − X_I)v = w and a₀ > γ, then ‖v‖_(H^(m,(a₀,2γ))_b) ≤ (a₀ − γ)⁻¹‖w‖_(H^(m,(a₀,2γ))_b).

The norms are those of the b-density |(dρ₀/ρ₀)(dρ_I/ρ_I)dg̸|, equivalent to that of μ_b on Ω_c ([[lem:iv-2-1]]).

*Proof.* (a), (b): in the coordinates (s, ρ₀, ω), s := log ρ_I, X_I = ∂_s, X₀ = ρ₀∂_(ρ₀) at fixed s, and the density
is ds (dρ₀/ρ₀) dg̸. By [[lem:iv2-1-1]] (b), for p ∈ Ω_c the segment of its X_I-curve from p to s_c := log c lies in Ω_c,
and v = 0 near s_c. So v(s) = −∫_s^(s_c) e^(d(s−s′))w(s′) ds′. Hence

    e^(−γs)|v(s)| ≤ ∫_s^(s_c) e^(−(d−γ)(s′−s)) e^(−γs′)|w(s′)| ds′,

a convolution with a kernel of L¹-norm (d − γ)⁻¹; Young's inequality in s, then integration in (ρ₀, ω) with the weight
ρ₀^(−2a₀), gives (a) for m = 0.

For (b), d = 0, and the X_I-curve over a point of ℐ⁺_c may leave Ω_c through Σ_(fut,r₀) before it reaches ℐ⁺ (after
[[eq:iv2-0-3]]), at a value of s that varies with the point; so we first extend w. Let Ω^♯_c be the set of the points
with (ρ₀, ω) ∈ ℐ⁺_c and ρ_I < c. It lies in M_♯ for r₀ large: over a point of ℐ⁺_c, x¹ ≤ C″ − r₀ + 2 by the upper
condition of [[eq:iv2-0-5]] at a point of Ω_c (see the proof of [[lem:iv2-1-1]]), and |x| = (2 − x¹)/ρ_I ≥ 2(r₀ − C″)
for ρ_I < c ≤ ½. It contains the whole X_I-curve over each point of ℐ⁺_c. Let E be the extension operator of the proof
of [[lem:iv1-2-3]] for Ω = Ω_c, one linear operator bounded on every H^j_b, and put
w_♯ := ρ₀^(a₀)ρ_I^γE(ρ₀^(−a₀)ρ_I^(−γ)w) on Ω^♯_c. Then w_♯ = w on Ω_c and
‖w_♯‖_(H^(m,(a₀,2γ))_b(Ω^♯_c)) ≤ C‖w‖_(H^(m,(a₀,2γ))_b(Ω_c)), with C depending only on m and Ω_c. Put

    v^((0)) := −∫_(−∞)^(s_c) w_♯ ds′,     ṽ(s) := ∫_(−∞)^s w_♯ ds′     on Ω^♯_c.

At a point of Ω_c, v^((0)) + ṽ(s) = −∫_s^(s_c) w_♯ ds′ = −∫_s^(s_c) w ds′ = v(s), as the segment from s to s_c lies in
Ω_c. By Cauchy–Schwarz,
|v^((0))|² ≤ ∫_(−∞)^(s_c) e^(2γs′) ds′ · ∫ e^(−2γs′)|w_♯|² ds′ = (2γ)⁻¹c^(2γ)∫ e^(−2γs′)|w_♯|² ds′, and e^(−γs)|ṽ(s)| ≤ ∫_(−∞)^s e^(−γ(s−s′))e^(−γs′)|w_♯(s′)| ds′, a kernel of L¹-norm γ⁻¹; integration in (ρ₀, ω) with
the weight ρ₀^(−2a₀) gives (b) for m = 0. Over a point of ℐ⁺_c whose curve lies in Ω_c for all ρ_I < c, w_♯ = w along
it, and for almost every such point ∫ e^(−2γs′)|w|² ds′ is finite; then |ṽ(s)|² ≤ (2γ)⁻¹e^(2γs)∫ e^(−2γs′)|w|² ds′ by
Cauchy–Schwarz on (−∞, s], so v(s) = v^((0)) + ṽ(s) → v^((0)) as s → −∞. (c): in the coordinates (z, y, ω),
z := log ρ₀, y := log ρ, X₀ − X_I = ∂_z and log ρ_I = y − z, so the density is dz dy dg̸ and {ρ_I = c} is
{z = z_c(y) := y − log c}. By [[lem:iv2-1-1]] (b), v(z, y) = ∫_(z_c(y))^z w(z′, y) dz′. The weight is
ρ₀^(−a₀)ρ_I^(−γ) = e^(−γy)e^(−(a₀−γ)z), and

    e^(−(a₀−γ)z)|v(z)| ≤ ∫_(z_c)^z e^(−(a₀−γ)(z−z′)) e^(−(a₀−γ)z′)|w(z′)| dz′,

a kernel of L¹-norm (a₀ − γ)⁻¹; Young's inequality in z gives (c) for m = 0.

*Derivatives.* Let V be one of X₀, X_I and the rotation fields. V commutes with X_I and with X₀ − X_I, and Vv vanishes
where v does; so in (a) and (c) Vv solves the same equation with Vw, and the bounds for m = 0 apply to it. (In (c),
differentiating the integral in y produces the boundary term w(z_c(y), y)∂_yz_c, which vanishes as w = 0 near
{ρ_I = c}.) Induction on m gives (a) and (c) for m ≥ 1, with the same constants. In (b) the limits of the integrals
defining v^((0)) and ṽ do not depend on (ρ₀, ω), so X₀ and the rotations, which act at fixed s, commute with them:
Vv^((0)) = −∫_(−∞)^(s_c) Vw_♯ ds′ and Vṽ(s) = ∫_(−∞)^s Vw_♯ ds′; and X_Iv^((0)) = 0, X_Iṽ = w_♯. The fields tangent to
ℐ⁺ are X₀ and the rotations, so the bounds for m = 0, applied to the derivatives of w_♯, give (b) for every m, with the
bound for w_♯ above. Without the extension, the lower limit would be the value of s at which the curve leaves Ω_c,
which depends on (ρ₀, ω), and its derivatives would enter those of v^((0)) and ṽ. ∎

**Lemma {#lem:s26-decompositions}** (Decompositions.) For u ∈ 𝒴^k_(a₀)(Ω), Ω ⊃ Ω_c, call a pair (u^((0)), ũ) with
u^((0)) ∈ H^(k,a₀)_b(ℐ⁺_c), ũ_j ∈ H^(k,(a₀,2β))_b in every slot j, ũ₆ = u₆ − χ_Iu^((0)) and ũ_j = u_j for j ≠ 6, a
*decomposition* of u, and ‖u^((0))‖_(H^(k,a₀)_b(ℐ⁺_c)) + Σ_j‖ũ_j‖_(H^(k,(a₀,2β))_b) its norm of order k; the norm of u in
𝒴^k_(a₀)(Ω) is the infimum of the norms of order k of its decompositions. Let y_* := C″ − r₀ − 2r₀^(1−ℓ^♭_I). Then
ℐ⁺ ∩ Ω̄_c is the part of ℐ⁺ where x¹ ≤ y_*, and:

(a) two decompositions of u have the same u^((0)) almost everywhere on ℐ⁺ ∩ Ω̄_c;

(b) if (u^((0)), ũ) is a decomposition of u and z is smooth with compact support in ℐ⁺_c ∩ {x¹ > y_*}, then
(u^((0)) + z, ũ′) is a decomposition of u, where ũ′₆ := ũ₆ − χ_Iz and ũ′_j := ũ_j for j ≠ 6.

*Proof.* On U, ρ_I = (2 − x¹)/|x| ([[eq:iii-c-1-2]]), and the upper condition of [[eq:iv2-0-5]] reads
x¹ ≤ y_* + 2|x|^(1−ℓ^♭_I) (the proof of [[lem:iv2-1-1]]). Over a point of ℐ⁺ with x¹ ≤ y_* it holds at every |x|, and
the lower condition holds for ρ_I ≤ c, as in the proof of [[lem:iv2-1-1]] (b); so the whole X_I-curve {0 < ρ_I < c}
over the point lies in Ω_c, and the point lies in Ω̄_c. Over a point with x¹ > y_*, it gives
|x| ≤ ((x¹ − y_*)/2)^(−1/(ℓ^♭_I−1)) on Ω_c, so ρ_I is bounded below on Ω_c over a neighbourhood of the point, which
therefore is not in Ω̄_c. This proves the description of ℐ⁺ ∩ Ω̄_c.

(b) By the same bound, ρ_I ≥ c_z > 0 on Ω_c over the compact set supp z, and ρ₀ = 1/(2 − x¹) is bounded above and
below there. So χ_Iz, whose b-derivatives are bounded, is supported in a region of finite b-volume on which the weights
are bounded, and lies in H^(∞,(a₀,2β))_b(Ω_c); and u₆ = χ_I(u^((0)) + z) + ũ′₆.

(a) If (u^((0)), ũ) and (u′^((0)), ũ′) are decompositions of u, then z := u^((0)) − u′^((0)) satisfies
χ_Iz = ũ′₆ − ũ₆ ∈ H^(0,(a₀,2β))_b(Ω_c). In the coordinates (s, ρ₀, ω), s := log ρ_I, of the proof of [[lem:iv2-1-2]],
the square of this norm is comparable to ∫(∫ e^(−2βs)|χ_Iz|² ds) ρ₀^(−2a₀)(dρ₀/ρ₀)dg̸, which is therefore finite. Over a
point with x¹ ≤ y_* the
inner integral runs over (−∞, log c), on which χ_I = 1 for s ≤ log(c/4), and ∫_(−∞)^(log(c/4)) e^(−2βs) ds = ∞ as
β > 0. So z = 0 at almost every such point. ∎

The estimates below bound the norm of a decomposition that they construct, linearly in the data, and so bound the norm
of u. Where a choice linear in u is needed, in the smoothing of the proof of [[thm:iv2-3-1]], the decomposition is
carried with u.

### The linear theorem {#sec:iv2-2}

This section is [Hin23a, Theorem 3.35] with data, for the operator of [[sec:iii-c-4]], in dimension 4 + 1.

**Lemma {#lem:iv2-2-1}** (The region of the radiation field.) Fix c ∈ (0, ½] so small that [[prop:iv1-2-2]] holds on
Ω_c with Σ_in := {ρ_I = c} ∩ Ω⁺ and Σ_fin := Σ_(fut,r₀) ∩ {ρ_I < c}. These are admissible in [[sec:iv-3]].

*Proof.* Ω_c ⊂ Ω_(ext,r₀) ⊂ U and Ω_c ⊂ {x_I < c^(1/2)}; Σ_in is spacelike with Ω_c to its future ([[lem:iv2-1-1]]
(a)); Σ_fin is spacelike for g ([[lem:iii-c1-1-1]]); and every X_I-curve in Ω_c begins on Σ_in ([[lem:iv2-1-1]] (b)). ∎

**Lemma {#lem:iv2-2-2}** (The Cauchy problem near the interior of I₀, in both directions.) Let
Ω_N := Ω_(ext,r₀) ∩ {τ′ ≤ ¼}, which contains Ω⁻, and α ∈ ℝ, s ∈ ℕ₀. For h small in H⁵ with h ∈ H^(s+2),
f ∈ H^(s,α+2)_b(Ω_N) and data ġ_j ∈ H^(s+1−j,α)_b(Σ_(IVP,r₀)), j = 0, 1, there is a unique ġ ∈ H^(s+1,α)_b(Ω_N) with
Lġ = f, ġ = ġ₀ and rℒ_(∂_(t_IVP))ġ = ġ₁ on Σ_(IVP,r₀), and

    ‖ġ‖_(H^(s+1,α)_b(Ω_N)) ≤ C(‖f‖_(H^(s,α+2)_b) + ‖ġ₀‖_(H^(s+1,α)_b) + ‖ġ₁‖_(H^(s,α)_b))
        + C‖h‖_(H^(s+2))(‖f‖_(H^(4,α+2)_b) + ‖ġ₀‖_(H^(5,α)_b) + ‖ġ₁‖_(H^(4,α)_b)).                         {#eq:iv2-2-1}

Here the weight at I₀ is a power of ρ; on Ω_N, ρ_I ≥ ½, so it is one of ρ₀. If moreover s ≤ 3 and h is bounded in
H⁸, then [[eq:iv2-2-1]] holds without its last term, with C depending on that bound.

*Proof.* On Ω_N, τ′ ∈ [−1/12, ¼] ([[lem:iii-c1-1-1]]: t_IVP ≥ −(|x| − r₀)/12), so τ ∈ [−1/12 − ε, ¼ + ε] for r₀
large, inside the range of [[prop:iv-4-1]] with δ = ½. That proposition, for the system as in the proof of
[[prop:iv1-2-2]] (the principal part is scalar, and the first-order terms are bounded b-operators, absorbed by the
exponential weight), and with τ replaced by τ′, applies here: τ′ is a smooth function near the interior of I₀ with
G_b(dτ′, dτ′) = G_b(dτ, dτ) + O(ρ) = τ² − 1 + O(ρ) < 0, and its proof uses only that dτ is uniformly timelike in the
b-sense on the τ-range and that L ∈ ρ²Diff²_b is a wave operator; for h ∈ H^(s₀) the change L − L_(b₀) lies in
ρ²(ρC^∞ + H^(s₀−2))Diff²_b (the coefficients of the perturbation are rational in h and two of its b-derivatives),
small for h small in H⁵ and g₀ − g_(b₀) small ([[prop:iii-c-4-4]], near the interior of I₀; [[lem:iii-c2-2-1]] for
L^(χ₀)). Two changes are needed.

*Data.* [[prop:iv-4-1]] has vanishing data and f vanishing near the initial surface. With the data above, the energy
identity of its proof, on {0 ≤ τ′ ≤ τ′₁}, has in addition the flux through Σ_(IVP,r₀) = {τ′ = 0} of the energy current
of its multiplier, bounded by C(‖ġ₀‖²_(H^(1,α)_b) + ‖ġ₁‖²_(H^(0,α)_b)), as r∂_(t_IVP) = ∂_(τ′) modulo b-vector fields
tangent to {τ′ = 0} (with ρ∂_ρ at fixed τ′). The term on the left of the identity coming from f does not need f to
vanish there. This gives the case s = 0. For s ≥ 1, commute the b-vector fields tangent to {τ′ = 0}, ρ∂_ρ at fixed τ′
and the rotations: their commutators with L lie in ρ²Diff²_b (with coefficients in H^(s₀−3) for the perturbation), of
first order in the commuted fields, and their data are tangential derivatives of ġ₀, ġ₁ together with one normal
derivative, given at {τ′ = 0} by the data and the equation; the commutator terms enter as sources and are absorbed as
in the proof of [[prop:iv-4-1]]. The normal derivatives ∂²_(τ′) are recovered from the equation, which is
non-characteristic at the level sets of τ′. The tame term comes from the Moser estimate ([[lem:iv1-2-3]]) for the
coefficients of the perturbation, which are rational in h and two of its b-derivatives.

*Low orders.* Let s ≤ 3 and h be bounded in H⁸; we use Leibniz's rule in place of the Moser estimate. A commutator
term of order s is a sum of products of a b-derivative of order at most s of a coefficient of L with a b-derivative of
order at most s + 1 of ġ. A b-derivative of order at most s of a coefficient of the perturbation is a polynomial in the
b-derivatives of h of order at most s + 2 ≤ 5, with smooth bounded factors (h is small, so the denominators are bounded
below). Each of these b-derivatives of h lies in H³_b, with norm at most ‖h‖_(H⁸), so in L^∞ by the embedding of
[[lem:iv1-2-3]]. Hence each commutator term is bounded by a constant depending only on the bound on h in H⁸ times
‖ġ‖_(H^(s+1,α)_b), and it is absorbed for Λ large as in the proof of [[prop:iv-4-1]], Λ now depending on that bound.
The normal derivatives that the equation gives at {τ′ = 0} are bounded by the data in the same way. So no norm of f or
of the data above those of the first term of [[eq:iv2-2-1]] enters.

*Both directions.* On Ω⁺ ∩ Ω_N the solution is the forward one; on Ω⁻ it is the backward one, given by the same argument
run backward in time, which uses only the b-structure of L, that dτ′ is timelike, and that Σ_(past,r₀) is spacelike
([[lem:iii-c1-1-1]]); the backward problem is argued directly as t ↦ −t is not an isometry of the gauge-fixed operator,
whose E_C-term is odd in time. Uniqueness: the estimate applied to the difference of two solutions, which has vanishing
data and forcing term. ∎

**Lemma {#lem:iv2-2-3}** (The forward problem with growth at ℐ⁺; [[rem:iv-4-2]] for the system.) Let
Ω⁺₁ := Ω⁺ ∩ {τ′ ≥ 1/16}, a₀ ∈ ℝ, α_I < min(a₀, 0), 3 ≤ m ≤ k_h − 3, k_h ≥ 8, with h ∈ H^(k_h) small in H⁸, and let
f_♭ ∈ H^(m,(a₀,2α_I))_b(Ω⁺₁) vanish on {τ′ < ⅛}. The forward solution u of L_gu = f_♭ on Ω⁺₁, vanishing on
{τ′ < ⅛}, satisfies

    ‖u‖_(H^(m+1,a₀)_b(Ω⁺₁∩{ρ_I>c/2})) + ‖u‖_(H^((1;m),(a₀,2α_I))_(e,b;b)(Ω_c))
        ≤ C(‖f_♭‖_(H^(m,(a₀,2α_I))_b) + ‖h‖_(H^(m+3))‖f_♭‖_(H^(4,(a₀,2α_I))_b)).                       {#eq:iv2-2-2}

For m = 3, [[eq:iv2-2-2]] holds without its last term, with C depending on the bound on h in H⁸.

*Proof.* *Away from ℐ⁺.* Ω′ := Ω⁺₁ ∩ {ρ_I > c/4} lies in {1/16 ≤ τ′ ≤ 1 − c/8} for r₀ large (ρ_I = 1 − τ + 2ρ). Its
interior boundary consists of {τ′ = 1/16}, initial, and the piecewise smooth ({ρ_I = c/4} ∪ Σ_(fut,r₀)) ∩ Ω̄′,
spacelike ([[lem:iv2-1-1]] (a), [[lem:iii-c1-1-1]]) with Ω′ to its past. [[prop:iv-4-1]], for the system and with
τ′, as in the proof of [[lem:iv2-2-2]], gives u₁ on Ω′ with ‖u₁‖_(H^(m+1,a₀)_b) ≤ C(‖f_♭‖_(H^(m,a₀)_b) plus the tame
term), and for m = 3 without the tame term, by the part *Low orders* of that proof; on Ω′, ρ_I > c/4, so the weight at
ℐ⁺ does not matter. As the boundary to its future is spacelike, Ω′ is closed under the past within Ω⁺₁, and u₁ = u on
Ω′ ([[lem:ii-f-1-3]]).

*Near ℐ⁺.* Let χ_c := χ̂_c(ρ_I) with χ̂_c = 1 on [c/2, ∞) and 0 on [0, c/4], and u₂ := u − χ_cu₁ on Ω_c. Then
u₂ = 0 on {ρ_I > c/2}, and

    L_gu₂ = f₃ := (1 − χ_c)f_♭ − [L_g, χ_c]u₁,

which vanishes on {ρ_I > c/2}, hence near Σ_in = {ρ_I = c}. The commutator is a first-order b-operator supported in
{c/4 ≤ ρ_I ≤ c/2}: [L_g, χ_c] = Σ_l c_lV_l + c₀, with V_l b-vector fields, c_l products of b-derivatives of χ_c with the
second-order coefficients of L_g, which are smooth functions of h, and c₀ involving also the first-order coefficients,
smooth functions of h and of its first b-derivatives. Each coefficient is its value at h = 0, smooth and bounded with
all its b-derivatives, plus a part c̃ that vanishes at h = 0, with ‖c̃_l‖_(H^j_b) ≤ C‖h‖_(H^j) and
‖c̃₀‖_(H^j_b) ≤ C‖h‖_(H^(j+1)) for every j, as for the coefficients ã_i ([[eq:iv2-0-4]]), and with
‖c̃‖_(L^∞) ≤ C‖h‖_(H⁵) by the embedding of [[lem:iv1-2-3]]. On {ρ_I ≥ c/4} the weight at ℐ⁺ is immaterial, and
‖V_lu₁‖_(L^∞) + ‖u₁‖_(L^∞) ≤ C‖u₁‖_(H^(4,a₀)_b(Ω′)) with the weight a₀ divided out, by the same embedding. So
[[lem:iv1-2-3]] with s := m, applied to each product c̃V_lu₁ and c̃₀u₁, gives

    ‖[L_g, χ_c]u₁‖_(H^(m,(a₀,2α_I))_b)
        ≤ C(‖u₁‖_(H^(m+1,a₀)_b(Ω′)) + ‖h‖_(H^(m+1))‖u₁‖_(H^(4,a₀)_b(Ω′))).                 {#eq:s26-commutator}

u₂ is the forward solution on Ω_c from Σ_in (uniqueness by [[lem:ii-f-1-3]]), and [[prop:iv1-2-2]] on Ω_c
([[lem:iv2-2-1]]) gives ‖u₂‖_(H^((1;m),(a₀,2α_I))_(e,b;b)) ≤ C(‖f₃‖_m + ‖h‖_(H^(m+3))‖f₃‖_3), where here and below
‖·‖_j is the norm of H^(j,(a₀,2α_I))_b, and that of H^(j,a₀)_b(Ω′) for u₁. The bound for u₁ above, at the order m and
at the order 3 (the latter without tame term, by the part *Low orders* of the proof of [[lem:iv2-2-2]]), gives
‖u₁‖_(m+1) ≤ C(‖f_♭‖_m + ‖h‖_(H^(m+2))‖f_♭‖_4) and ‖u₁‖_4 ≤ C‖f_♭‖_3. With [[eq:s26-commutator]] this gives

    ‖f₃‖_m ≤ C(‖f_♭‖_m + ‖u₁‖_(m+1) + ‖h‖_(H^(m+1))‖u₁‖_4) ≤ C(‖f_♭‖_m + ‖h‖_(H^(m+2))‖f_♭‖_4),
    ‖f₃‖_3 ≤ C(‖f_♭‖_3 + ‖u₁‖_4) ≤ C‖f_♭‖_3,

h being bounded in H⁸. Hence ‖u₂‖_(H^((1;m),(a₀,2α_I))_(e,b;b)) ≤ C(‖f_♭‖_m + ‖h‖_(H^(m+3))‖f_♭‖_4), the second term of
[[eq:iv2-2-2]]; no product of two norms of h arises. For m = 3, the last term of [[eq:iv1-2-1]] is
‖h‖_(H⁶)‖f₃‖_3 ≤ C‖f₃‖_3 ≤ C‖f_♭‖_3, and u₁ is bounded without tame term, so no tame term arises. ∎

**Lemma {#lem:s26-interpolation}** (Interpolation.) For j ∈ ℕ₀ let (B^j, |·|_j) be Banach spaces with continuous
inclusions B^j ↪ B^i for j ≥ i along which the norms do not increase, B^∞ := ⋂_j B^j, and for θ > 1 let
S_θ : B^∞ → B^∞ be linear maps satisfying [[eq:ii-g-2-1]] for every v ∈ B^∞. For integers 0 ≤ s₀ ≤ s ≤ s₁ there is C
such that for every v ∈ B^∞

    |v|_s ≤ C|v|_(s₀)^(1−λ)|v|_(s₁)^λ,     λ := (s − s₀)/(s₁ − s₀) (λ := 0 if s₁ = s₀),    {#eq:s26-interpolation}

and for integers 0 ≤ s₀ ≤ q ≤ p there is C such that for every v ∈ B^∞

    |v|_p|v|_q ≤ C|v|_(s₀)|v|_(p+q−s₀),                                               {#eq:s26-interpolation-product}

C depending only on these integers and the constants C_(s,t) of [[eq:ii-g-2-1]]. This applies to the spaces B^j of the
proof of [[thm:iv2-3-1]], whose elements are the decompositions of [[lem:s26-decompositions]] (after conjugation), with
their norms made monotone in j as in [[rem:ii-g-2-2]], and to the smoothing operators of part (i) of that proof, which
act on each of the two components of a decomposition by the operator S̃_θ of Step 4 of the proof of [[prop:ii-g-3-1]];
their construction uses nothing of this section.

*Proof.* Let s₀ < s < s₁, the other cases being trivial, and v ≠ 0, so that |v|_(s₀) > 0. Put
R := |v|_(s₁)/|v|_(s₀), which is at least 1 as the norms are monotone. If R ≤ 2^(s₁−s₀), then

    |v|_s ≤ |v|_(s₁) = |v|_(s₁)^(1−λ)|v|_(s₁)^λ ≤ 2^(s₁−s₀)|v|_(s₀)^(1−λ)|v|_(s₁)^λ.

Otherwise θ := R^(1/(s₁−s₀)) > 2, and [[eq:ii-g-2-1]], with (s, t) := (s, s₀) for S_θv and (s, t) := (s, s₁) for
v − S_θv, gives

    |v|_s ≤ |S_θv|_s + |v − S_θv|_s ≤ C_(s,s₀)θ^(s−s₀)|v|_(s₀) + C_(s,s₁)θ^(s−s₁)|v|_(s₁)
        = (C_(s,s₀) + C_(s,s₁))|v|_(s₀)^(1−λ)|v|_(s₁)^λ,

as θ^(s−s₀) = R^λ and θ^(s−s₁) = R^(λ−1). For the product put n := p + q − s₀, so n ≥ p. If n = s₀, then p = q = s₀
and the claim is an identity. Otherwise [[eq:s26-interpolation]] with s₁ := n, at s = p and at s = q, has the exponents
λ_p := (p − s₀)/(n − s₀) and λ_q := (q − s₀)/(n − s₀), and λ_p + λ_q = 1 as (p − s₀) + (q − s₀) = n − s₀. The product
of the two bounds is |v|_p|v|_q ≤ C|v|_(s₀)^(2−λ_p−λ_q)|v|_n^(λ_p+λ_q) = C|v|_(s₀)|v|_n. ∎

**Theorem {#thm:iv2-2-4}** (The linear exterior estimate; [Hin23a, Theorem 3.35] in dimension 4 + 1, with [Hin26,
(5.52)–(5.53)].) Let α₀ > ℓ^♭_I, a₀ := α₀ − 3/2, k ∈ ℕ₀, d := 4, and let h be small in H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b. For
f ∈ H^(k+d,α₀+2,(−′,ℓ^♭_I+1))_b(Ω_(ext,r₀)) and ġ₀, ġ₁ ∈ H^(k+d,α₀)_b(Σ_(IVP,r₀)) there is a
ġ ∈ H^(k,α₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀)), unique in H^(max(k,1),α₀,(−,ℓ^♭_I))_b (the energy estimate needs H¹), with
Lġ = f, ġ|_(Σ_(IVP,r₀)) = ġ₀ and rℒ_(∂_(t_IVP))ġ|_(Σ_(IVP,r₀)) = ġ₁; and with
N(f, ġ₀, ġ₁; j) := ‖f‖_(H^(j,α₀+2,(−′,ℓ^♭_I+1))_b) + ‖ġ₀‖_(H^(j,α₀)_b) + ‖ġ₁‖_(H^(j,α₀)_b),

    ‖ġ‖_(H^(k,α₀,(−,ℓ^♭_I))_b)
        ≤ C(N(f, ġ₀, ġ₁; k + d) + ‖h‖_(H^(k+d+3,ℓ^♭₀,(−,ℓ^♭_I))_b)N(f, ġ₀, ġ₁; 8)),                        {#eq:iv2-2-3}

with C depending on k, α₀, ℓ^♭_I, the parameters and the bound on h in H⁸, and not on h otherwise. Here the norms of h
are those of one decomposition of ρ^(−3/2)h ([[lem:s26-decompositions]], a₀ = ℓ^♭₀ − 3/2), small at order 8, the same
at every order; and the left side of [[eq:iv2-2-3]] may be replaced by the norm of the decomposition of ġ that the proof
constructs, which depends linearly on (f, ġ₀, ġ₁). At α₀ = ℓ^♭₀ this is the tame form [Hin26, (5.52)] of
[[eq:iii-c1-2-2]]; [[eq:iii-c1-2-2]] itself follows, with C depending on h.

*Proof.* *Step 1 (near Σ_IVP).* [[lem:iv2-2-2]] with s := k + 3 and α := α₀ gives ġ_N on Ω_N, including the past
slab, bounded in H^(k+4,α₀)_b by [[eq:iv2-2-1]].

*Step 2 (the forcing for the rest).* Let χ := χ̂_N(τ′), χ̂_N = 1 on (−∞, ⅛] and 0 on [¼, ∞). On Ω⁺, w := ġ − χġ_N must
satisfy

    Lw = f₂ := (1 − χ)f − [L, χ]ġ_N,     w = 0 on {τ′ < ⅛},

as ġ = ġ_N on Ω_N (uniqueness in [[lem:iv2-2-2]]). f₂ vanishes on {τ′ < ⅛}, and [L, χ] ∈ ρ²Diff¹_b is supported in
{⅛ ≤ τ′ ≤ ¼}, where ρ_I ≥ ½. The argument for [[eq:s26-commutator]], with χ in place of χ_c, L in place of L_g and the
factor ρ² of [L, χ] giving the weight α₀ + 2, gives

    ‖[L, χ]ġ_N‖_(H^(k+3,α₀+2,(−′,ℓ^♭_I+1))_b) ≤ C(‖ġ_N‖_(H^(k+4,α₀)_b) + ‖h‖_(H^(k+4))‖ġ_N‖_(H^(4,α₀)_b)).

Put u := ρ^(−3/2)w; then L_gu = f_(2,♭) := 2ρ_Iρ^(−7/2)f₂ ∈ H^(k+3,(a₀,2β))_b in every slot ([[sec:iv2-0]]).

*Step 3 (growth).* Fix ε := ¼(½ − β) > 0 and γ₀ := β − 1 + 2ε < 0; then γ₀ < min(a₀, 0), as a₀ > β > γ₀.
[[lem:iv2-2-3]] with m := k + 3 and α_I := γ₀ gives u on Ω⁺₁, with [[eq:iv2-2-2]], and u = 0 on {τ′ < ⅛}, so u is the
solution on Ω⁺. On Ω⁺ ∩ {ρ_I > c/2} this already bounds u in H^(k+4,a₀)_b, which is the claim there.

*Step 4 (the equation near ℐ⁺).* On Ω_c, with u₂ of the proof of [[lem:iv2-2-3]], u₂ = 0 on {ρ_I > c/2} and, by
[[eq:iv1-1-1]],

    (X_I − Ā)(X₀ − X_I)u₂ = F := −½(f₃ − x_I²Δ̸u₂ − L̃_gu₂).                                              {#eq:iv2-2-4}

*The gain.* Let j ≥ 2 and u₂ ∈ H^(j,(a₀,2γ))_b. Then x_I²Δ̸u₂ and L̃_gu₂ lie in H^(j−2,(a₀,2γ+1−2ε))_b. Indeed x_I²Δ̸
and x_Ia_iP_i carry the factor x_I and are of second order. For x_Iã_iP_iu₂ put b_i := P_iu₂, so that
‖b_i‖_(H^(j−2,(a₀,2γ))_b) ≤ C‖u₂‖_(H^(j,(a₀,2γ))_b). By [[eq:iv2-0-4]], for every j′ ∈ ℕ₀,
ã_i ∈ H^(j′,(ℓ^♭₀,−2ε))_b ⊂ H^(j′,(0,−2ε))_b with norm at most C‖h‖_(H^(j′+2)) (its expansion at ℐ⁺ starts at ρ_I⁰,
which lies in every x_I^(−2ε)L²_b near ℐ⁺ but not in L²_b; and ρ₀ ≤ 1 on Ω_c). By the embedding of [[lem:iv1-2-3]] (order
3, on Ω_c), ã_i ∈ x_I^(−2ε)L^∞ with norm at most C‖h‖_(H⁵). There are two cases.

(1) j ≥ 5. Then b_i ∈ H^(3,(a₀,2γ))_b, so b_i ∈ ρ₀^(a₀)x_I^(2γ)L^∞ with norm at most C‖u₂‖_(H^(5,(a₀,2γ))_b), by the same
embedding. [[lem:iv1-2-3]] with s := j − 2, a := ã_i with the weights (0, −2ε) and b := b_i with the weights (a₀, 2γ),
followed by multiplication by x_I, gives

    ‖x_Iã_iP_iu₂‖_(H^(j−2,(a₀,2γ+1−2ε))_b)
        ≤ C(‖u₂‖_(H^(j,(a₀,2γ))_b) + ‖h‖_(H^j)‖u₂‖_(H^(5,(a₀,2γ))_b)),                                    {#eq:iv2-2-5}

the first term from ‖ã_i‖_(x_I^(−2ε)L^∞)‖b_i‖_(H^(j−2,(a₀,2γ))_b) and the second from
‖ã_i‖_(H^(j−2,(0,−2ε))_b)‖b_i‖_(ρ₀^(a₀)x_I^(2γ)L^∞).

(2) 2 ≤ j ≤ 4. Now b_i need not be bounded (j − 2 < 3), and we use Leibniz's rule, which puts at most j − 2 ≤ 2
derivatives on ã_i. Divide out the weights: ã_i = x_I^(−2ε)a′ and b_i = ρ₀^(a₀)x_I^(2γ)b′, so that the left side of
[[eq:iv2-2-5]] is ‖a′b′‖_(H^(j−2)_b). Measure H^p_b by the L²_b-norms of the compositions of at most p of the fields
X₀, …, X₈ of the proof of [[prop:iv1-2-2]], which span Diff¹_b over C^∞. For l ≤ 7, X_l obeys Leibniz's rule for the
product of a coefficient with a section, and X₈ = 1; so a composition Q of q of these fields maps a′b′ to a sum of at
most 2^q products (Q′a′)(Q″b′), with Q′ and Q″ compositions of q′ and q″ of the fields, q′ + q″ ≤ q. Hence

    ‖a′b′‖_(H^(j−2)_b) ≤ C max_(Q′) ‖Q′a′‖_(L^∞) ‖b′‖_(H^(j−2)_b),

the maximum over the compositions Q′ of at most j − 2 of the fields. For such Q′, as j − 2 ≤ 2, Q′a′ ∈ H³_b with norm
at most ‖a′‖_(H⁵_b) = ‖ã_i‖_(H^(5,(0,−2ε))_b) ≤ C‖h‖_(H⁷), so ‖Q′a′‖_(L^∞) ≤ C‖h‖_(H⁷) by the same embedding. Therefore

    ‖x_Iã_iP_iu₂‖_(H^(j−2,(a₀,2γ+1−2ε))_b) ≤ C‖h‖_(H⁷)‖u₂‖_(H^(j,(a₀,2γ))_b) ≤ C‖u₂‖_(H^(j,(a₀,2γ))_b),
                                                                                                    {#eq:iv2-2-5-low}

with C depending on the bound on h in H⁸, as [[eq:iv2-2-3]] allows: at these orders there is no tame term.

With u₂ ∈ H^((1;m),(a₀,2γ))_(e,b;b) in place of H^(j,(a₀,2γ))_b the loss is one b-derivative instead of two, as
P_i ∈ Diff¹_(e,b)Diff¹_b and x_I²Δ̸ ∈ x_IDiff¹_(e,b)Diff¹_b: then b_i ∈ H^(m−1,(a₀,2γ))_b with norm at most
C‖u₂‖_(H^((1;m),(a₀,2γ))_(e,b;b)), and the two cases are m − 1 ≥ 3 and m − 1 ≤ 2. For m ≥ 4 the argument of (1)
gives [[eq:iv2-2-5]] with j − 2, ‖u₂‖_(H^(j,(a₀,2γ))_b), ‖h‖_(H^j) and ‖u₂‖_(H^(5,(a₀,2γ))_b) replaced by m − 1,
‖u₂‖_(H^((1;m),(a₀,2γ))_(e,b;b)), ‖h‖_(H^(m+1)) and ‖u₂‖_(H^((1;4),(a₀,2γ))_(e,b;b)); for m ≤ 3 the argument of (2)
gives [[eq:iv2-2-5-low]] with the same replacements. And f₃ ∈ H^(k+3,(a₀,2β))_b: f_(2,♭) is, and [L_g, χ_c]u₁ is
supported in {ρ_I ≥ c/4}.

*Step 5 (the integration, slot by slot).* Write [[eq:iv2-2-4]] by slots. As Ā is lower triangular with the entries of
[[sec:iv2-0]], for j ≠ 6

    (X_I − Ā_(jj))Y_j = F_j + Σ_(i<j, i≠6) Ā_(ji)Y_i,     Y_j := (X₀ − X_I)u_(2,j),                    {#eq:iv2-2-6}

and, X_I and X₀ − X_I commuting, for slot 6

    (X₀ − X_I)Z₆ = F₆,     Z₆ := X_Iu_(2,6).                                                           {#eq:iv2-2-7}

All of Y_j, Z₆, u₂, F vanish on {ρ_I > c/2}, so [[lem:iv2-1-2]] applies; the solution of each equation vanishing there
is unique (it is an ordinary differential equation along curves that reach {ρ_I = c}, [[lem:iv2-1-1]] (b)).

*First integration.* u₂ ∈ H^((1;k+3),(a₀,2γ₀))_(e,b;b) (Step 3), so by Step 4, F ∈ H^(k+2,(a₀,2γ₁))_b with
γ₁ := min(β, γ₀ + ½ − ε) = β − ½ + ε < 0. For j ≠ 6, in the order 1, 2, 3, 4, 5, 7, [[lem:iv2-1-2]] (a) with
d = Ā_(jj) ≥ d_* > γ₁ gives Y_j ∈ H^(k+2,(a₀,2γ₁))_b, the right side of [[eq:iv2-2-6]] lying there by induction; then
[[lem:iv2-1-2]] (c), a₀ > γ₁, gives u_(2,j) ∈ H^(k+2,(a₀,2γ₁))_b. For slot 6, [[lem:iv2-1-2]] (c) gives Z₆, and
[[lem:iv2-1-2]] (a) with d = 0 > γ₁ gives u_(2,6) ∈ H^(k+2,(a₀,2γ₁))_b.

*Second integration.* Now u₂ ∈ H^(k+2,(a₀,2γ₁))_b, so by Step 4 (with two derivatives lost), F ∈ H^(k,(a₀,2γ₂))_b,
γ₂ := min(β, γ₁ + ½ − ε) = β. As in the first integration, with d_* > β ([[eq:iv2-0-1]]) and a₀ > β,
u_(2,j) ∈ H^(k,(a₀,2β))_b for j ≠ 6. For slot 6, Z₆ ∈ H^(k,(a₀,2β))_b by [[lem:iv2-1-2]] (c), and [[lem:iv2-1-2]] (b),
β > 0, gives u_(2,6) = u^((0)) + ũ₆ with u^((0)) ∈ H^(k,a₀)_b(ℐ⁺_c) and ũ₆ ∈ H^(k,(a₀,2β))_b.

*Step 6 (assembly).* On Ω_c, u = u₂ + χ_cu₁, with χ_cu₁ supported in {ρ_I ≥ c/4}; on Ω⁺ ∩ {ρ_I > c/2}, Step 3; on Ω_N,
Step 1. As χ_I = χ̂(ρ_I) vanishes for ρ_I ≥ c/2, u₆ − χ_Iu^((0)) = ũ₆ + (1 − χ_I)u^((0)) + χ_cu_(1,6) on Ω_c, and
(1 − χ_I)u^((0)) is supported in {ρ_I ≥ c/4} within Ω_c, where every weight at ℐ⁺ is equivalent. So u ∈ 𝒴^k_(a₀)(Ω⁺),
with the decomposition ([[lem:s26-decompositions]]) whose first component is u^((0)), linear in (f, ġ₀, ġ₁) as every
step is; that is, ġ = ρ^(3/2)u + χġ_N ∈ H^(k,α₀,(−,ℓ^♭_I))_b on Ω⁺ ([[sec:iv2-0]]), and on Ω⁻ by Step 1.

*The estimate.* Write |h|_j for the norm of order j of the decomposition of h fixed in the statement, made monotone in
j as in [[rem:ii-g-2-2]], and N_j := N(f, ġ₀, ġ₁; j); let C depend only on k, α₀, ℓ^♭_I, the parameters and the bound
on h in H⁸, so that |h|_j ≤ C for j ≤ 8. For the other quantities ‖·‖_j is the norm of order j of the space in which
the step bounds them (H^(j,α₀)_b for ġ_N, H^(j,(a₀,2β))_b for f_(2,♭) and f₃, H^(j,a₀)_b(Ω′) for u₁), and
‖u₂‖_((1;m)) is the norm of u₂ in H^((1;m),(a₀,2γ₀))_(e,b;b). Each step is bounded by the previous ones. Each lower
norm is bounded by the same steps at a low order, where the tame factors are |h|_j with j ≤ 7, except
‖u₂‖_(H^(5,(a₀,2γ₁))_b), whose bound carries |h|_9 and is treated in the second integration.

- Step 1, by [[eq:iv2-2-1]] at s = k + 3 (for k = 0, its clause for s ≤ 3):
  ‖ġ_N‖_(H^(k+4,α₀)_b) ≤ C(N_(k+4) + |h|_(k+5)N_5); at s = 3, ‖ġ_N‖_(H^(4,α₀)_b) ≤ CN_4.
- Step 2, by the bound for [L, χ]ġ_N: ‖f_(2,♭)‖_(H^(k+3,(a₀,2β))_b) ≤ C(N_(k+4) + ‖ġ_N‖_(k+4) + |h|_(k+4)‖ġ_N‖_4)
  ≤ C(N_(k+4) + |h|_(k+5)N_5); at k = 1, ‖f_(2,♭)‖_(H^(4,(a₀,2β))_b) ≤ CN_5.
- Step 3, by [[eq:iv2-2-2]] at m = k + 3 (for k = 0, its clause for m = 3): ‖u₂‖_(H^((1;k+3),(a₀,2γ₀))_(e,b;b)), the
  norm of u in H^(k+4,a₀)_b(Ω⁺ ∩ {ρ_I > c/2}), and, by the proof of [[lem:iv2-2-3]], those of u₁ in H^(k+4,a₀)_b(Ω′)
  and of f₃ in H^(k+3,(a₀,2β))_b are at most C(‖f_(2,♭)‖_(k+3) + |h|_(k+6)‖f_(2,♭)‖_4) ≤ C(N_(k+4) + |h|_(k+6)N_5); at
  k = 1, ‖u₂‖_(H^((1;4),(a₀,2γ₀))_(e,b;b)) ≤ CN_5.
- The first integration, by [[eq:iv2-2-5]] in H^((1;m)) with m = k + 3 (for k = 0, [[eq:iv2-2-5-low]]) and the
  constants of [[lem:iv2-1-2]]: ‖u₂‖_(H^(k+2,(a₀,2γ₁))_b) ≤ C(‖f₃‖_(k+2) + ‖u₂‖_((1;k+3)) + |h|_(k+4)‖u₂‖_((1;4)))
  ≤ C(N_(k+4) + |h|_(k+6)N_5). At k = 3 this is ‖u₂‖_(H^(5,(a₀,2γ₁))_b) ≤ C(N_7 + |h|_9N_5).
- The second integration, by [[eq:iv2-2-5]] at j = k + 2 (for k ≤ 2, [[eq:iv2-2-5-low]]) and [[lem:iv2-1-2]]: the
  norms of u_(2,j) (j ≠ 6), u^((0)) and ũ₆ in 𝒴^k_(a₀) are at most C(‖f₃‖_k + ‖u₂‖_(H^(k+2,(a₀,2γ₁))_b) + T), with
  T := 0 for k ≤ 2 and T := |h|_(k+2)‖u₂‖_(H^(5,(a₀,2γ₁))_b) ≤ C|h|_(k+2)(N_7 + |h|_9N_5) for k ≥ 3. For 3 ≤ k ≤ 6,
  |h|_(k+2) ≤ C, so T ≤ C(N_7 + |h|_9N_5) ≤ C(N_(k+4) + |h|_(k+7)N_5). For k ≥ 7, |h|_(k+2)N_7 ≤ |h|_(k+7)N_8, and
  [[eq:s26-interpolation-product]] ([[lem:s26-interpolation]] for the decompositions) with s₀ := 8, q := 9 and
  p := k + 2 ≥ 9 gives |h|_(k+2)|h|_9 ≤ C|h|_8|h|_(k+3) ≤ C|h|_(k+3); so T ≤ C(N_(k+4) + |h|_(k+7)N_8).

By Step 6, the norm of the decomposition of ġ constructed there, and so ‖ġ‖_(H^(k,α₀,(−,ℓ^♭_I))_b), is at most C times
the sum of these bounds, which is at most C(N_(k+4) + |h|_(k+7)N_8): this is [[eq:iv2-2-3]].

*The estimate with C depending on h.* Let k ≥ 1. The lower norms in the tame terms are of orders 4, 5 and 4 for f, ġ₀
and ġ₁ in [[eq:iv2-2-1]] at s = k + 3, of order 4 for ġ_N and for u₁ in the bounds for [L, χ]ġ_N and
[[eq:s26-commutator]], of order 4 for f_(2,♭) in [[eq:iv2-2-2]] at m = k + 3, and of orders (1;4) and 5 for u₂ in
[[eq:iv2-2-5]], which is used only at m ≥ 4 and j ≥ 5. Each is at most the order to which the same quantity is bounded
in the main term of its step: k + 4 for f, ġ₀, ġ₁, ġ_N and u₁, k + 3 for f_(2,♭), (1;m) and j for u₂. So every tame
term is at most C‖h‖_(H^(k+7,ℓ^♭₀,(−,ℓ^♭_I))_b) times the main terms, and the steps give [[eq:iii-c1-2-2]] with C
depending on h. Let k = 0. Step 1 uses [[lem:iv2-2-2]] at s = 3, Step 3 uses [[lem:iv2-2-3]] at m = 3, and both
integrations of Step 5 use [[eq:iv2-2-5-low]] (at m = 3 and j = 2); none of these has a tame term, h being bounded in
H⁸. So [[eq:iii-c1-2-2]] holds at k = 0 too, with C depending on the bound on h in H⁸.

*Uniqueness.* Two solutions differ by one with vanishing data and forcing term; it vanishes on Ω_N by [[lem:iv2-2-2]],
and on Ω⁺ as the forward solution with vanishing forcing term ([[lem:ii-f-1-3]]). ∎

[Hin23a, Theorem 3.35] integrates π_(CΥ)u, then π̸₀u, then π₁₁u, and repeats, because in dimension 3 + 1 the radiation
field of π̸₀u enters the equation of π₁₁u through the h-dependent entry A̸₁₁ of [Hin23a] and through the second-order
error acting on π̸₀u, and π₁₁u has the size of the leading part. In dimension 4 + 1 both are in L̃_g, gaining
x_I^(1−2ε), and Ā₇₆ = 0: so all slots improve together, two integrations from the growth weight γ₀ suffice, with a loss
of d = 4 derivatives, and π₁₁ġ has no radiation field ([[rem:s17-no-radiation]]).

### The nonlinear exterior solution {#sec:iv2-3}

This section is [Hin23a, Corollary 3.36] in dimension 4 + 1, the nonlinear part of [Hin26, Theorem 5.17].

**Theorem {#thm:iv2-3-1}** (The nonlinear exterior solution.) Let g₀ be as in [[sec:iv2-0]], d := 7 and
N_NM := 21d + 6 = 153, the order of [[thm:ii-g-2-1]]. There are ε₀ > 0 and, for every k and ε > 0, an ε₁ ∈ (0, ε₀] such
that for h₀, h₁ ∈ H^(∞,ℓ^♭₀)_b(Σ_(IVP,r₀); S²T*) with ‖h_j‖_(H^(N_NM,ℓ^♭₀)_b) < ε₀ the problem

    P(g₀ + h, g₀) = 0 in Ω_(ext,r₀),     h = h₀,  rℒ_(∂_(t_IVP))h = h₁ on Σ_(IVP,r₀),                     {#eq:iv2-3-1}

has a solution h ∈ H^(∞,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀)) small in H^(3d) of this class, unique among the solutions small
in H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b, and ‖h_j‖_(H^(N_NM+k,ℓ^♭₀)_b) < ε₁ gives ‖h‖_(H^(3d+k,ℓ^♭₀,(−,ℓ^♭_I))_b) < ε.

*Proof.* Apply [[thm:ii-g-2-1]] with d = 7 and:

- B^k := H^(k,a₀)_b(ℐ⁺_c) × H^(k,ℓ^♭₀,ℓ^♭_I)_b(Ω_(ext,r₀); S²T*), a₀ := ℓ^♭₀ − 3/2, with the sum of the two norms. An
  element x = (v, h̃) is, after conjugation, a decomposition ([[lem:s26-decompositions]]) of the tensor h_x that equals
  h̃ + ρ^(3/2)χ_Iv in slot 6 and h̃ in the other slots: h_x ∈ H^(k,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀); S²T*), with norm in
  that class at most C|x|_k ([[sec:iv2-0]]). The map x ↦ h_x is linear. F^k := H^(k,ℓ^♭₀+2,(−′,ℓ^♭_I+1))_b(Ω_(ext,r₀))
  × H^(k,ℓ^♭₀)_b(Σ_(IVP,r₀))². The norms are made monotone in k by [[rem:ii-g-2-2]];
- trivial support classes: the subspaces B^k_η and F^∞_η of [[thm:ii-g-2-1]] all equal to B^k and F^∞, and η₀ := 1;
- Φ(x) := (P(g₀ + h_x, g₀), h_x|_(Σ_(IVP,r₀)) − h₀, rℒ_(∂_(t_IVP))h_x|_(Σ_(IVP,r₀)) − h₁) on the set {|x|_(3d) < δ}.

The unknown is the decomposition, not the tensor: a decomposition is not determined by h_x
([[lem:s26-decompositions]] (b)), and the smoothing operators must be linear.

*(i) Smoothing.* Componentwise: on v the operator S̃_θ of Step 4 of the proof of [[prop:ii-g-3-1]], which acts on
weighted b-Sobolev spaces without support conditions, built on ℐ⁺_c, and on h̃ the same operator built on Ω_(ext,r₀).
S_θ is linear and the norm of B^k is the sum of the two norms, so [[eq:ii-g-2-1]] holds; the support conditions are
vacuous.

*(ii) The map.* Write h := h_x. By [[cor:iii-c-5-3]] (with ℰ₀ = ∅, ℓ₀ = ℓ^♭₀, and ⟨ℰ_I^C⟩ at the weight ℓ^♭_I, which by
[[def:iii-c-3-1]] is the class (−, ℓ^♭_I) of h), P(g₀ + h, g₀) ∈ H^(k−2,ℓ^♭₀+2,(−′,ℓ^♭_I+1))_b for x ∈ B^k small in
B⁵, and by [[eq:iii-c-5-5]] and [[prop:iii-c-5-2]] it is C² in x, with
Φ′(x)ẋ = (L^(g₀+h,g₀)h_ẋ, h_ẋ|_Σ, rℒ_(∂_(t_IVP))h_ẋ|_Σ) and Φ″ bilinear in two b-derivatives, with coefficients
rational in h and its first two b-derivatives. [[eq:ii-g-2-2]] and [[eq:ii-g-2-3]] follow from the Moser estimates
([[lem:iv1-2-3]], [[lem:iii-c-2-1]]) applied to the components of x, the loss being 2 and the low norms of order at
most 5 ≤ d. The trace on Σ_(IVP,r₀) is bounded B^(k+1) → H^(k,ℓ^♭₀)_b(Σ_(IVP,r₀)) (χ_I = 0 near Σ_(IVP,r₀)), which lies
within the loss d. The data enter the constants C_k of [[eq:ii-g-2-3]]:
‖Φ(x)‖_k ≤ C^P_k(1 + |x|_(k+d)) + ‖h₀‖_(H^(k,ℓ^♭₀)_b) + ‖h₁‖_(H^(k,ℓ^♭₀)_b), with C^P_k depending only on g₀, k and δ.
For k ≤ N_NM and ‖h_j‖_(H^(N_NM,ℓ^♭₀)_b) ≤ 1 this is at most (C^P_k + 2)(1 + |x|_(k+d));
so we take C_k := C^P_k + 2 for k ≤ N_NM, which does not depend on the data. For k > N_NM,
C_k := C^P_k + ‖h₀‖_(H^k) + ‖h₁‖_(H^k) is finite, as h_j ∈ H^∞, and does not enter the threshold of [[thm:ii-g-2-1]].
(Smallness in H^(2d) alone is not enough for this argument: the threshold of [[thm:ii-g-2-1]] depends on the C_k with
k ≤ N_NM.)

*(iii) Right inverses.* For x in the set above, Ψ(x)(f, ġ₀, ġ₁) is the decomposition of ġ that the proof of
[[thm:iv2-2-4]] constructs, with α₀ := ℓ^♭₀ > ℓ^♭_I, for h := h_x with its decomposition x; it is linear in
(f, ġ₀, ġ₁), and h_(Ψ(x)F) = ġ. Then Φ′(x)Ψ(x) = id on F^∞, and [[eq:iv2-2-3]], for these decompositions, gives
[[eq:ii-g-2-4]]: |Ψ(x)F|_k ≤ C(‖F‖_(k+4) + |x|_(k+7)‖F‖₈) ≤ C(‖F‖_(k+d) + |x|_(k+d)‖F‖_(2d)) for k ≥ d, and 3d ≥ 8
gives the smallness that [[thm:iv2-2-4]] asks. The support statement of (iii) is vacuous.

Φ(0) = (0, −h₀, −h₁), as P(g₀, g₀) = 0 (the proof of [[cor:iii-c-5-3]]). Let ε_NM be the threshold of
[[thm:ii-g-2-1]] for d, δ, η₀ and the constants above, and ε₀ := min(1, ε_NM/2). If ‖h_j‖_(H^(N_NM,ℓ^♭₀)_b) < ε₀, then
‖Φ(0)‖_(2d) ≤ ‖h₀‖_(H^(2d,ℓ^♭₀)_b) + ‖h₁‖_(H^(2d,ℓ^♭₀)_b) < ε_NM, and [[thm:ii-g-2-1]] gives x with |x|_(3d) < δ and
Φ(x) = 0; h := h_x solves [[eq:iv2-3-1]], with norm below Cδ in H^(3d) of its class. *Higher norms.* For k ≥ 0 the
shifted scales |v|′_i := |v|_(i+k), ‖f‖′_i := ‖f‖_(i+k) satisfy (i)–(iii) with the same d: [[eq:ii-g-2-1]] and
[[eq:ii-g-2-4]] are invariant under the shift, and [[eq:ii-g-2-3]] holds on {|x|′_(3d) < δ′} ⊂ {|x|_(3d) < δ}, δ′ ≤ δ,
with constants depending on k; as above, those of order i ≤ N_NM do not depend on the data once
‖h_j‖_(H^(N_NM+k,ℓ^♭₀)_b) ≤ 1. So [[thm:ii-g-2-1]] for the shifted scales, with δ′ := min(δ, ε/C), gives ε₁ ∈ (0, ε₀]
such that data with ‖h_j‖_(H^(N_NM+k,ℓ^♭₀)_b) < ε₁ have a solution h_x with |x|_(3d+k) < ε/C, so with norm below ε in
H^(3d+k) of its class; it is small in H⁸ of its class, so by uniqueness it is the h above.
*Uniqueness.* If h and h′ solve [[eq:iv2-3-1]] and are small in H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b, then L̄(h − h′) = 0 with
vanishing data, where
L̄ := ∫₀¹ L^(g₀+h′+s(h−h′),g₀) ds. Each L^(g₀+h_s,g₀) has the form [[eq:iv1-1-1]] with the same leading part, which does
not depend on h, and a remainder in the class [[eq:iv2-0-4]], uniformly in s; so L̄ has this form too, and its principal
part, an average of ½□_(g_s) with g_s close to g_(b₀), is a wave operator with the same causal structure. [[lem:iv2-2-2]]
and [[lem:iv2-2-3]] hold for L̄ (their proofs use only these properties), and the difference vanishes. ∎

**Remark {#rem:iv2-3-2}** (Constraints.) If the data of [[thm:iv2-3-1]] satisfy the vacuum constraint equations and
the gauge condition on Σ_(IVP,r₀), the solution is Ricci flat and satisfies the gauge condition on Ω_(ext,r₀):
[[rem:iii-c1-2-2]] (1) applies to it as stated there.

### The exterior solution {#sec:iii-c1-2}

This section states [Hin26, (5.52)–(5.53) and Theorem 5.17] in dimension 4 + 1, and proves the propagation of the
gauge condition and of the vacuum equation that [Hin26, Remark 5.18] uses.

**Theorem {#thm:iii-c1-2-1}** ([Hin26, Theorem 5.17] in dimension 4 + 1.) There is k₀ ∈ ℕ such that the following
holds. Let ℓ^♭₀, ℓ^♭_I be as in [[eq:iii-c1-1-1]] and r₀ ≥ R₀, with R₀ as fixed after [[lem:iii-c1-1-1]]. There is
ε₀ > 0 such that for
h₀, h₁ ∈ H^(∞,ℓ^♭₀)_b(Σ_(IVP,r₀); S²T*) with ‖h_j‖_(H^(k₀,ℓ^♭₀)_b) < ε₀, the problem

    P(g_(b₀) + h, g_(b₀)) = 0 in Ω_(ext,r₀),     h = h₀,  rℒ_(∂_(t_IVP))h = h₁ on Σ_(IVP,r₀),           {#eq:iii-c1-2-1}

has a solution h ∈ H^(∞,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀)), unique among the solutions of this class that are small in
H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b; and for every ε > 0 and k there are k₁ ≥ k₀ and ε₁ ∈ (0, ε₀] such that
‖h_j‖_(H^(k₁,ℓ^♭₀)_b) < ε₁ gives ‖h‖_(H^(k,ℓ^♭₀,(−,ℓ^♭_I))_b) < ε. Moreover, for h ∈ H^(∞,ℓ^♭₀,(−,ℓ^♭_I))_b small in
H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b and every α₀ > ℓ^♭_I, d := 4, the solution of

    L^(g_(b₀)+h,g_(b₀))ġ = f ∈ H^(k+d,α₀+2,(−′,ℓ^♭_I+1))_b,     ġ|_(Σ_(IVP,r₀)) = ġ₀,
    rℒ_(∂_(t_IVP))ġ|_(Σ_(IVP,r₀)) = ġ₁,     ġ₀, ġ₁ ∈ H^(k+d,α₀)_b,

satisfies

    ‖ġ‖_(H^(k,α₀,(−,ℓ^♭_I))_b) ≤ C(‖f‖_(H^(k+d,α₀+2,(−′,ℓ^♭_I+1))_b) + ‖ġ₀‖_(H^(k+d,α₀)_b) + ‖ġ₁‖_(H^(k+d,α₀)_b)),
                                                                                                         {#eq:iii-c1-2-2}

with C depending on k, α₀, ℓ^♭_I and h; and the tame form of [[eq:iii-c1-2-2]] at α₀ = ℓ^♭₀, [Hin26, (5.52)], is
[[eq:iv2-2-3]].

Here (−′, ℓ^♭_I + 1) is the class of [[def:iii-c-5-1]] (2) with the index sets left out, as in [Hin26].

*Proof.* [[thm:iv2-3-1]] with g₀ = g_(b₀) gives the solution, its uniqueness and the smallness, with k₀ := N_NM = 153
and k₁ := N_NM + k, as ‖h‖_(H^(k,ℓ^♭₀,(−,ℓ^♭_I))_b) ≤ ‖h‖_(H^(21+k,ℓ^♭₀,(−,ℓ^♭_I))_b) (21 = 3d for the d = 7 of
[[thm:iv2-3-1]]). [[thm:iv2-2-4]] gives [[eq:iii-c1-2-2]] and its tame form [[eq:iv2-2-3]]. ∎

[Hin26] derives its Theorem 5.17 from [Hin23a, Theorem 3.35 and Corollary 3.36] by a change of notation: the tame
estimate (5.52), a Nash–Moser scheme (by [SR89] there; here [[thm:ii-g-2-1]], which is [Hin26c, Theorem 12.4]), and the
radiation fields of π₁₁ġ and π̸₀ġ recovered by integrating the leading part. In dimension 4 + 1 the leading part is that
of [[eq:iii-c-4-4]], and only π̸₀ carries a radiation field ([[rem:s17-no-radiation]]). [Hin23a, Section 3] is written
out in dimension 4 + 1 in [[sec:iv-0]]–[[sec:iv2-3]], and [[prop:np-10-64]] collects the places where the dimension
enters it.

The data and the gauge condition propagate by the second Bianchi identity. We first record the uniqueness statement for
linear wave equations that this uses.

**Lemma {#lem:s26-uniqueness}** (Uniqueness for the Cauchy problem.) Let X be a globally hyperbolic Lorentzian manifold
with metric g and a smooth spacelike Cauchy hypersurface S, and let P be a second-order operator with smooth
coefficients on a vector bundle over X, with principal symbol g⁻¹(ζ, ζ)Id. If v ∈ C²(X) solves Pv = 0 and v and all its
first derivatives vanish along S, then v = 0.

*Proof.* By [[thm:std-bgp-causal]] (3) there is a Cauchy time function τ on X with S = τ⁻¹(0); its level sets are
spacelike Cauchy hypersurfaces ([[thm:std-bgp-causal]] (2)). Let H be the Heaviside function and w := H(τ)v. In local
coordinates and a trivialisation, P = −g^(ij)∂_i∂_j + A^j∂_j + B; as v = 0 on S, ∂_j(H(τ)v) = H(τ)∂_jv, and as
∂_jv = 0 on S, ∂_i(H(τ)∂_jv) = H(τ)∂_i∂_jv, in the sense of distributions. So Pw = H(τ)Pv = 0 in 𝒟′(X), and
supp w ⊂ {τ ≥ 0}. For p ∈ X with τ(p) > −1, the set L_p := J⁻_X(p) ∩ J⁺_X(τ⁻¹(−1)) is compact
([[thm:std-bgp-causal]] (4) with K = {p}), and it contains J⁻_X(p) ∩ {τ ≥ −1}: through a point q with τ(q) ≥ −1 the
maximal integral curve of the gradient of τ, which is timelike, is an inextendible causal curve, so it meets the Cauchy
hypersurface τ⁻¹(−1), at a point where τ ≤ τ(q), that is, to the past of q. [[lem:ii-f-1-3]] with c = −1 gives w = 0,
so v = 0 on {τ ≥ 0}. With the time orientation of X reversed, X is globally hyperbolic with the same Cauchy
hypersurfaces, −τ is a Cauchy time function, and P is unchanged; the same argument applied to H(−τ)v gives v = 0 on
{τ ≤ 0}. ∎

**Proposition {#prop:np-10-57-d}** (Propagation of the gauge condition and of the vacuum equation.) Let X be a globally
hyperbolic Lorentzian manifold with metric g and a smooth spacelike Cauchy hypersurface S, with future unit normal n.
Let g₀ be a smooth Lorentzian metric on X, δ*_(g₀,E_C) = δ*_(g₀) + E^C_(g₀) the operator of [[eq:iii-b-6-2]] (with any
smooth 1-form c_C), and Υ a smooth 1-form on X with

    Ric(g) = δ*_(g₀,E_C)Υ     on X.                                                                    {#eq:s26-gauge-eq}

If Υ = 0 along S and the first and second fundamental forms of S satisfy the vacuum constraint equations, then Υ = 0
and Ric(g) = 0 on X. The dimension does not enter. In particular [[eq:s26-gauge-eq]] holds with
Υ = Υ^(E_Υ)(g, g₀) when P(g, g₀) = 0 ([[eq:iii-b-6-4]]), and with Υ = Υ^(χ₀E_Υ)(g, g₀) when P^(χ₀)(g, g₀) = 0
([[eq:iii-c2-2-1]]).

*Proof.* *The equation for Υ.* The contracted second Bianchi identity δ_gG_gRic(g) = 0 holds in every dimension.
Applying 2δ_gG_g to [[eq:s26-gauge-eq]] gives QΥ = 0, with Q := 2δ_gG_gδ*_(g₀,E_C). For a 1-form ω, with
(δ_gu)_μ = −∇^κu_(κμ) and G_g = I − ½g tr_g,

    (2δ_gG_gδ*_gω)_μ = −∇^κ∇_κω_μ − ∇^κ∇_μω_κ + ∇_μ∇^κω_κ,

and by the Ricci identity ∇^κ∇_μω_κ − ∇_μ∇^κω_κ is of order zero in ω, linear in the curvature of g. The operator
δ*_(g₀,E_C) − δ*_g = (δ*_(g₀) − δ*_g) + E^C_(g₀) is of order zero. So Q = □_g + Q₁ with Q₁ of first order, and Q has
principal symbol g⁻¹(ζ, ζ)Id.

*The data of Υ.* Along S, Υ = 0, so its derivatives along S vanish, and there ∇Υ = −n♭ ⊗ Z with Z := ∇_nΥ,
n♭ := g(n, ·), g(n, n) = −1, where (∇Υ)(V, W) := (∇_VΥ)(W). The terms of order zero in δ*_(g₀,E_C)Υ vanish along S,
so there, with a ⊗_s b := ½(a ⊗ b + b ⊗ a),

    Ric(g) = δ*_gΥ = −n♭ ⊗_s Z,     G_gRic(g) = −n♭ ⊗_s Z + ½Z(n)g,

as tr_g(n♭ ⊗_s Z) = Z(n). For every vector Y, (G_gRic(g))(n, Y) = −½(n♭(n)Z(Y) + Z(n)g(n, Y)) + ½Z(n)g(n, Y) = ½Z(Y).
By the Gauss and Codazzi equations, the vacuum constraint equations for the first and second fundamental forms of S are
the equations (G_gRic(g))(n, ·) = 0 along S. So Z = 0, and all first derivatives of Υ vanish along S.

*Conclusion.* [[lem:s26-uniqueness]] with P = Q and v = Υ gives Υ = 0 on X, and then Ric(g) = 0 by
[[eq:s26-gauge-eq]]. ∎

**Remark {#rem:iii-c1-2-2}** ([Hin26, Remarks 5.18 and 5.20] in dimension 4 + 1.) (1) Let h be the solution of
[[thm:iii-c1-2-1]], and ĝ := g_(b₀) + h₀ + t_IVP r⁻¹h₁, with h₀, h₁ extended to be independent of t_IVP near
Σ_(IVP,r₀). If the first and second fundamental forms of Σ_(IVP,r₀) for ĝ satisfy the vacuum constraint equations and
Υ^(E_Υ)(ĝ, g_(b₀)) = 0 on Σ_(IVP,r₀), then Υ^(E_Υ)(g_(b₀) + h, g_(b₀)) = 0 and Ric(g_(b₀) + h) = 0 on Ω_(ext,r₀).
Indeed g_(b₀) + h and ĝ agree on Σ_(IVP,r₀) with their first derivatives (h = h₀ and rℒ_(∂_(t_IVP))h = h₁ there), so
they have the same fundamental forms and the same Υ^(E_Υ) there; h is smooth in the interior Ω° of Ω_(ext,r₀); and Ω°
is globally hyperbolic with the spacelike Cauchy hypersurface Σ° ([[lem:s26-development]]). [[prop:np-10-57-d]] on Ω°
gives the claim there, and by continuity on Ω_(ext,r₀). The same argument applies in the cut-off gauge of
[[sec:iii-c2-2]] and to the gauged data of [[sec:iii-c2-4]] ([[thm:iii-c2-3-1]]). ([Hin26, Remark 5.18] prints
t_IVP r h₁; with h₁ = rℒ_(∂_(t_IVP))h as in [[eq:iii-c1-2-1]] the factor is r⁻¹, as in [Hin26, Proposition 5.25 and
Section 5.7.1].)

(2) The structure [[eq:iii-c-4-4]] holds for every g₀ ∈ 𝒢 ([[def:iii-c-3-4]]), and [[cor:iii-c-5-3]] needs only
Ric(g₀) = 0; so [[thm:iii-c1-2-1]] holds for P(g₀ + h, g₀) = 0 with g₀ ∈ 𝒢 Ricci flat and g₀ − g_(b₀) small in the
sense of the pointwise bounds of the proof of [[lem:iii-c1-1-1]]: this is [[thm:iv2-3-1]] and [[thm:iv2-2-4]] for such
g₀. In particular it holds for g₀ = φ_S*g_(b₀) where [[lem:iii-c-3-5]] (2) applies; the cut-off region near I₀ is
treated in [[sec:iii-c2-1]].

### The cut-off gauge {#sec:iii-c2-2}

This section is [Hin26, (5.75)–(5.76)] in dimension 4 + 1. Fix χ̌₀ ∈ C_c^∞((−¼, ¼)) equal to 1 on [−⅛, ⅛] ([Hin26]
prints [−⅛, −⅛]), and χ₀ := 1 − χ̌₀(t_IVP/r), extended by 1 where r is small relative to t_IVP. Near I₀ and ℐ⁺,
t_IVP/r is a smooth function on M (τ = t/|x| near the interior of I₀, [[lem:iii-c-1-1]]), so χ₀ ∈ C^∞(M). It equals 0
on {|t_IVP| ≤ r/8} ⊃ Ω_(ext,r₀) ∩ {t_IVP ≤ 0} and near Σ_IVP, and 1 on {t_IVP ≥ r/4}, a neighbourhood of
ℐ⁺ ∩ Ω_(ext,r₀) (there t_IVP/r → 1). Let

    Υ^(χ₀E_Υ)(g, g₀) := Υ⁰(g, g₀) − χ₀E^Υ_(g₀)G_(g₀)(g − g₀),
    P^(χ₀)(g, g₀) := Ric(g) − δ*_(g₀,E_C)Υ^(χ₀E_Υ)(g, g₀),                                               {#eq:iii-c2-2-1}

and L^(χ₀)_(g,g₀) the linearisation of P^(χ₀) in g. Υ⁰ is natural: for a diffeomorphism φ,

    φ*Υ⁰(g, g₀) = Υ⁰(φ*g, φ*g₀),                                                                       {#eq:iii-c2-2-2}

[Hin26, (5.75)], in any dimension, since ∇^(φ*g) = φ*∇^g and the trace is natural. The term E^Υ_(g₀)G_(g₀)(g − g₀)
is not natural in this sense when E^Υ is stationary relative to g_(b₀); this is why the cut-off is introduced.

**Lemma {#lem:iii-c2-2-1}** (The structure in the cut-off gauge.) For g₀ ∈ 𝒢, [[prop:iii-c-4-4]], [[prop:iii-c-5-2]]
and [[cor:iii-c-5-3]] hold for L^(χ₀) and P^(χ₀) in place of L and P.

*Proof.* L^(χ₀)_(g,g₀) − L_(g,g₀) = −δ*_(g₀,E_C)((1 − χ₀)E^Υ_(g₀)G_(g₀)(·)), as E^Υ_(g₀)G_(g₀)(g − g₀) is linear in
g − g₀. Its coefficients are those of the E^Υ-term of [[eq:iii-c-4-1]], which lie in ρ₀²C^∞Diff¹_b near I₀
([[def:iii-b-6-1]]: E^Υ_(g₀) is homogeneous of degree −1, and δ* is of degree −1 in |x|), times 1 − χ₀, which is
supported in {|t_IVP| < r/4}, a set on which ρ_I is bounded below. So the difference lies in
ρ₀²ρ_I²C^∞Diff¹_b, the error class of [[eq:iii-c-4-4]], and the leading part at ℐ⁺ is unchanged (χ₀ = 1 there). The
proofs of [[prop:iii-c-5-2]] and [[cor:iii-c-5-3]] use only [[eq:iii-c-4-4]] and P^(χ₀)(g₀, g₀) = 0, which holds as
Ric(g₀) = 0 and G_(g₀)(g₀ − g₀) = 0. ∎

### The exterior estimates in the cut-off gauge {#sec:iv2-4}

**Corollary {#cor:iv2-4-1}** (The cut-off gauge.) [[thm:iv2-2-4]], [[thm:iv2-3-1]], [[lem:iv2-2-2]] and
[[lem:iv2-2-3]] hold with L^(χ₀)_(g,g₀) and P^(χ₀) of [[eq:iii-c2-2-1]] in place of L^(g,g₀) and P, for every g₀ of
[[sec:iv2-0]].

*Proof.* χ₀ = 1 − χ̌₀(t_IVP/r) equals 1 on {t_IVP ≥ r/4} ([[sec:iii-c2-2]]). On Ω_c, ρ_I < c ≤ ½ gives
t > (1 − c)|x| + 2, so t_IVP ≥ ¼|x| for |x| ≥ r₀ large, which suffices; so L^(χ₀) = L on Ω_c, and the edge-b
structure ([[prop:iv1-1-2]]), [[prop:iv1-2-2]] and the integration of [[sec:iv2-2]], which are used only on Ω_c, are
unchanged. Elsewhere only the b-structure enters ([[prop:iv-4-1]] in [[lem:iv2-2-2]] and [[lem:iv2-2-3]]), and
L^(χ₀) − L ∈ ρ₀²ρ_I²C^∞Diff¹_b (the proof of [[lem:iii-c2-2-1]]), a first-order term of the class those proofs absorb.
In [[thm:iv2-3-1]], [[prop:iii-c-5-2]] and [[cor:iii-c-5-3]] hold for L^(χ₀), P^(χ₀) by [[lem:iii-c2-2-1]], and
P^(χ₀)(g₀, g₀) = 0 there. For g₀ ≠ g_(b₀): [[sec:iv1-0]] is stated for g₁, g₀ ∈ 𝒢; the hypersurfaces Σ_(IVP,r₀),
Σ_(fut,r₀), Σ_(past,r₀) are spacelike for g₀ + h when g₀ − g_(b₀) is small as in [[lem:iii-c1-1-1]] (its proof uses
only the size of g₀ + h − η in the frame); and [[lem:iv2-1-1]] (a) persists likewise. ∎

So the change of gauge lies where only robust estimates are used, and the structure at ℐ⁺ is that of the original
gauge; this is the content of [Hin26]'s remark that the stationarity of E^Υ and the choice of c_Υ away from ℐ⁺ play
no role in its Theorems 5.17 and 5.21.

### Partial polyhomogeneity {#sec:iii-c1-3}

This section is [Hin26, Theorem 5.21 and Remark 5.22] (pp. 102–108) in dimension 4 + 1.

**Theorem {#thm:iii-c1-3-1}** ([Hin26, Theorem 5.21] in dimension 4 + 1.) Let ℰ₀ be an index set with
min Re ℰ₀ > 3/2 + 2γ_Υ and jℰ₀ ⊂ ℰ₀ for j ∈ ℕ. Let ℓ₀, ℓ_I > 3/2 with ℓ₀ ∉ Re π₁ℰ₀, ℓ_I < ℓ₀,
ℓ_I < 3/2 + (1 − e_C)(1 − v_C)γ_C and ℓ_I ∉ 3/2 + σ_Υ. Let ℓ^♭₀ := 3/2 + ½(1 − e_Υ)γ_Υ and
ℓ^♭_I := 3/2 + ¼(1 − e_Υ)γ_Υ, which satisfy [[eq:iii-c1-1-1]]. There is an index set ℰ_I^C satisfying
[[def:iii-c-3-1]], with ℰ₀ ⊂ ℰ_I^C, such that: if h₀, h₁ ∈ H^(∞,(ℰ₀,ℓ₀))_b(Σ_(IVP,r₀); S²T*) satisfy the smallness of
[[thm:iii-c1-2-1]], the solution h of [[eq:iii-c1-2-1]] satisfies

    h ∈ H^(∞,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_(ext,r₀)),                                                       {#eq:iii-c1-3-1}

and for every k and ε > 0 there are k₀ and ε₀ with

    ‖h_j‖_(H^(k₀,(ℰ₀,ℓ₀))_b) < ε₀ (j = 0, 1)   ⟹   ‖h‖_(H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b) < ε.             {#eq:iii-c1-3-2}

As in [Hin26, Remark 5.22], smallness of ‖h_j‖_(H^(k₀,ℓ^♭₀)_b) does not make the coefficients of the expansions small,
which is why [[eq:iii-c1-3-2]] is stated separately.

*Proof.* *Step 1 (the expansion at I₀).* Suppose h ∈ H^(∞,(ℰ₀,α₀),(−,ℓ^♭_I))_b for some α₀ ∈ [ℓ^♭₀, ℓ₀); for
α₀ = ℓ^♭₀ this is [[thm:iii-c1-2-1]] (ℓ^♭₀ < min Re ℰ₀). As P(g_(b₀) + h, g_(b₀)) = 0 and P(g_(b₀), g_(b₀)) = 0,

    L_(g_(b₀))h = −∫₀¹ (L_(g_(b₀)+sh,g_(b₀)) − L_(g_(b₀),g_(b₀)))h ds.                                   {#eq:iii-c1-3-3}

By [[prop:iii-c-4-4]], applied with g₁ = g₀ = g_(b₀) to h and to 0, the two operators have the same leading part and
the same C^∞ error (the part *The perturbation* of its proof), and their difference lies in
H^(∞,(ℰ₀+2,α₀+2),(ℰ_I^tot,ℓ^♭_I))_b Diff²_b on U (the perturbation part of [[eq:iii-c-4-4]], whose coefficients are
polynomial in sh and its first two derivatives, each term with a factor of h; [[lem:iii-c-4-3]]), uniformly in s.
Acting on h, whose slots lie in H^(∞,(ℰ₀,α₀),(ℰ_I^tot,ℓ^♭_I))_b, it gives by [[lem:iii-c-2-1]] an element of
H^(∞,(ℰ₀+2,α₀+3),(2ℰ_I^tot,ℓ^♭_I+1))_b: at I₀ the index set is 2ℰ₀ + 2 ⊂ ℰ₀ + 2 and the weight
α₀ + 2 + min Re ℰ₀ > α₀ + 3 (as min Re ℰ₀ > 1); at ℐ⁺, 2ℰ_I^tot ⊂ ℰ_I^C + 1 ([[lem:iii-c-3-2]] (b)), at the weight
ℓ^♭_I + 3/2 > ℓ^♭_I + 1. Away from U the spaces impose only regularity. So h solves

    L_(g_(b₀))h ∈ H^(∞,(ℰ₀+2,α₀+3),(−′,ℓ^♭_I+1))_b,
    h|_(Σ_(IVP,r₀)) = h₀,     rℒ_(∂_t)h|_(Σ_(IVP,r₀)) = h₁ ∈ H^(∞,(ℰ₀,ℓ₀))_b.                            {#eq:iii-c1-3-4}

This is one order better at I₀ than [[prop:iii-c-5-2]] alone gives. ([Hin26] writes ℰ₀ + 3; the index set is ℰ₀ + 2,
the gain being in the weight, which is what the argument uses.) Lower α₀ slightly if needed so that
α₁ := min(α₀ + 1, ℓ₀) ∉ Re π₁ℰ₀. Let ℰ_(0,≤) := {(z, k) ∈ ℰ₀ : Re z ≤ α₁}, a finite set, p := |ℰ_(0,≤)|, and
R := Π_((z,k)∈ℰ_(0,≤))(X₀ − z) ∈ Diff^p_b. Then Rh ∈ H^(∞,α₀,(−,ℓ^♭_I))_b (the converse part of [[lem:iii-a-1-3]]),
and

    L_(g_(b₀))(Rh) = ρ₀²R(ρ₀⁻²L_(g_(b₀))h) + ρ₀²[ρ₀⁻²L_(g_(b₀)), R]h.

Index sets are closed under + ℕ₀, so ℰ₀ + j ⊂ ℰ₀. The first term: ρ₀⁻²L_(g_(b₀))h ∈ H^(∞,(ℰ₀,α₀+1),(−′,ℓ^♭_I+1))_b by
[[eq:iii-c1-3-4]], and R removes its expansion at I₀ up to α₁ ≤ α₀ + 1 (the converse part of [[lem:iii-a-1-3]]), so the
first term lies in H^(∞,α₁+2,(−′,ℓ^♭_I+1))_b. For the second, by [[lem:iii-c-4-1]] and [[eq:iii-c1-3-5]] below, A :=
ρ₀⁻²L_(g_(b₀)) = −ρ_I(X_I − 3/2 − Ā)(X₀ − X_I) + ρ₀⁻²R̃_b with ρ₀⁻²R̃_b ∈ ρ_I²C^∞Diff²_b, the leading part having
coefficients independent of ρ₀. X₀ commutes with X₀, X_I, ∂_ω, ρ_I and the constant Ā, and maps a ∈ C^∞ to X₀a ∈ ρ₀C^∞;
so R commutes with the leading part, and [A, R] = [ρ₀⁻²R̃_b, R] ∈ ρ₀ρ_I²Diff^(p+1)_b. (The cruder [A, R] ∈
ρ₀ρ_IDiff^(p+1)_b would not do: on the radiation field ρ_I^(3/2) of slot 6 it gives ρ_I^(5/2), below the weight ℓ^♭_I + 1
∈ (5/2, 3) of the target.) Split h = h_e + h_r, with h_e the terms of its expansion at I₀ with real part at most α₀
(those known) and h_r ∈ H^(∞,α₀) at I₀. Then Rh_e = 0, so [A, R]h_e = −RAh_e. At I₀, Ah_e has its expansion in ℰ₀ (smooth
coefficients only add ℕ₀), and R removes its terms up to α₁, leaving order > α₁. At ℐ⁺, Ah_e lies in (−′, ℓ^♭_I + 1): the
leading part sends the slots other than 6 from the weight ℓ^♭_I to ℓ^♭_I + 1 and annihilates the radiation field
ρ_I^(3/2)a of slot 6 (column 6 of Ā vanishes: Ā_(j6) = 0 for j < 6, Ā being lower triangular, and Ā₆₆ = Ā₇₆ = 0; so on it
X_I − 3/2 − Ā acts as X_I − 3/2, which commutes past X₀ − X_I), and ρ₀⁻²R̃_b gains ρ_I². And [A, R]h_r ∈ H^(∞,α₀+1) at
I₀, with α₀ + 1 ≥ α₁, and it has the weight at least 3/2 + 2 > ℓ^♭_I + 1 at ℐ⁺. So ρ₀²[A, R]h ∈
H^(∞,α₁+2,(−′,ℓ^♭_I+1))_b. The data of Rh lie in H^(∞,α₁)_b(Σ_(IVP,r₀)). Near I₀, X₀ = ρ∂_ρ + 2ρ∂_τ in the coordinates
(τ, ρ), so X₀τ′ = (2 − C″)ρ for τ′ = τ − C″ρ: X₀ is tangent to Σ_IVP = {τ′ = 0} only when C″ = 2, and in general these
data involve the normal derivatives ∂^j_(τ′)h on Σ_IVP. These are determined by h₀, h₁ and the equation, which is
non-characteristic on Σ_IVP, with coefficients in C^∞ + H^(∞,(ℰ₀,ℓ₀))_b (jℰ₀ ⊂ ℰ₀ for the nonlinear terms); so the jet of
h on Σ_IVP has its expansion at ∂Σ_IVP in ℰ₀ up to ℓ₀ ≥ α₁, and R removes its terms with real part at most α₁ (the
converse part of [[lem:iii-a-1-3]]). [[eq:iii-c1-2-2]] with h = 0 and α₀ replaced by α₁ > ℓ^♭_I gives Rh ∈
H^(∞,α₁,(−,ℓ^♭_I))_b, and [[lem:iii-a-1-3]] gives h ∈ H^(∞,(ℰ₀,α₁),(−,ℓ^♭_I))_b. After finitely many steps, h ∈
H^(∞,(ℰ₀,ℓ₀),(−,ℓ^♭_I))_b.

*Step 2 (the expansion at ℐ⁺).* Suppose h ∈ H^(∞,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,α_I)_b for some α_I ∈ [ℓ^♭_I, ℓ_I) and some ℰ_I^C of
[[def:iii-c-3-1]] with ℰ₀ ⊂ ℰ_I^C; Step 1 gives this for α_I = ℓ^♭_I, with any such ℰ_I^C (one exists:
[[lem:iii-c-3-2]] (e) applied to ℰ₀). By [[eq:iii-c1-3-3]] and [[prop:iii-c-4-4]] on U,

    (X_I − 3/2 − Ā)(X₀ − X_I)h = f̃
        := ρ₀⁻²ρ_I⁻¹(R̃_bh + ∫₀¹ (L_(g_(b₀)+sh,g_(b₀)) − L_(g_(b₀)))h ds),                               {#eq:iii-c1-3-5}

with R̃_b ∈ ρ₀²ρ_I²C^∞Diff²_b ([[eq:iii-c-4-4]] at h = 0). The first term maps the slots of h, in (ℰ_I^tot, α_I) at ℐ⁺,
to (ℰ_I^tot + 1, α_I + 1) ⊂ (ℰ_I^C, α_I + 1) ([[lem:iii-c-3-2]] (a)). The second is ρ_I⁻¹ times a Diff²_b-operator
with coefficients in H^(∞,(ℰ₀,ℓ₀),(ℰ_I^tot,α_I))_b acting on h; by [[lem:iii-c-2-1]] it lies in
(ℰ_I^tot + ℰ_I^tot − 1, α_I + ν) ⊂ (ℰ_I^C, α_I + ν) for every ν < ½ ([[def:iii-c-3-1]] (3); the weight is
α_I + 3/2 − 1, with the strict inequality of [[lem:iii-c-2-1]]). At I₀ both lie in (ℰ₀, ℓ₀). Fix ν ∈ (¼, ½) and put
α′ := min(α_I + ν, ℓ_I), as in [Hin26, Theorem 5.21, Step 2.6]; lower ν slightly if needed so that
α′ ∉ 3/2 + σ_Υ and α′ ∉ Re π₁ℰ₀ (which is not needed if α′ = ℓ_I, by the hypotheses). So

    f̃ ∈ H^(∞,(ℰ₀,ℓ₀),(ℰ_I^C,α′))_b(U).                                                                {#eq:iii-c1-3-6}

Write w := (X₀ − X_I)h; its slots have the index sets of those of h ((F1) of [[sec:iii-a-1]]). By [[lem:iii-c-4-2]], Ā
is lower triangular with the diagonal [[eq:iii-c-4-3]], off-diagonal entries at (3, 1), (4, 1), (4, 3), (5, 2),
(7, 3), (7, 4), and Ā₇₆ = 0. We integrate slot by slot, in the order 1, 2, 3, 4, 5, 6, 7, putting the off-diagonal
terms on the right.

(i) *Slots 1–3 (π_Ch).* (X_I − 3/2 − Ā_(jj))w_j = f̃_j + Σ_(i<j) Ā_(ji)w_i, with
3/2 + Ā_(jj) ≥ 3/2 + (1 − e_C)(1 − v_C)γ_C > ℓ_I ≥ α′ (1 − e_C < 1). By induction the right side lies in (ℰ_I^C, α′)
at ℐ⁺, and [[lem:iii-a-1-2]] (with α′ ≠ 3/2 + Ā_(jj); the new exponent 3/2 + Ā_(jj) lies above α′, so only the
conormal statement is affected) gives w_j ∈ H^(∞,(ℰ₀,ℓ₀),(ℰ_I^C,α′))_b. Then (X₀ − X_I)h_j = w_j, and
[[lem:iii-a-3-2]] with z = 0 (ℓ₀ > α′, α′ ∉ Re π₁ℰ₀; away from ℐ⁺ there is nothing to show) gives
h_j ∈ H^(∞,(ℰ₀,ℓ₀),(ℰ₀∪̄ℰ_I^C,α′))_b.

(ii) *Slots 4–5 (π₀₁h, π_(1/)h).* The couplings (4, 1), (4, 3), (5, 2) bring w₁, w₂, w₃ ∈ (ℰ_I^C, α′).
[[lem:iii-a-1-2]] with z = 3/2 + Ā_(jj), Ā₄₄ = (1 − e_Υ)γ_Υ, Ā₅₅ = γ_Υ, gives w_j the index set
ℰ_I^C ∪ (3/2 + Ā_(jj), 0), which is ℰ_(I,01), resp. ℰ_(I,1/) ([[eq:iii-c-3-2]]), at the weight α′; [[lem:iii-a-3-2]]
then gives h_j the extended union with ℰ₀.

(iii) *Slot 6 (π̸₀h).* There is no coupling (Ā_(6i) = 0 for i < 6). [[lem:iii-a-1-2]] with z = 3/2 gives
ℰ̸_(I,0) = ℰ_I^C ∪ (3/2, 0): the radiation field.

(iv) *Slot 7 (π₁₁h).* The couplings (7, 3) (from ℰ_I^C) and (7, 4) (from ℰ_(I,01)), and no (7, 6); [[lem:iii-a-1-2]]
with z = 3/2 + 2γ_Υ gives ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0) ∪ (3/2 + 2γ_Υ, 0) = ℰ_(I,11). (If Ā₇₇ = 2γ_Υ equalled Ā₄₄,
the two exponents would coincide and [[lem:iii-a-1-2]] would give a logarithm, so that [[eq:iii-c-3-2]] would need
(3/2 + 2γ_Υ, 1); this happens only for e_Υ = −1, which 0 < e_Υ < 1 excludes.) No radiation field of π̸₀h reaches slot
7 ([[rem:s17-no-radiation]]).

[[lem:iii-a-3-2]] gives the extended union ℰ₀ ∪̄ (·) at ℐ⁺: where an exponent of the expansion at I₀ meets one at ℐ⁺,
the corner produces a logarithm. So, with ℰ′ the smallest index set containing ℰ₀ ∪̄ ℰ_I^C and satisfying
[[def:iii-c-3-1]] (it exists by [[lem:iii-c-3-2]] (e), as min Re(ℰ₀ ∪̄ ℰ_I^C) > 3/2 + 2γ_Υ; it contains ℰ₀), the slots
of h lie in the classes of [[eq:iii-c-3-3]] for ℰ′, at the weight α′ (for the slots 4, 5 and 7,
ℰ₀ ∪̄ ℰ_(I,j) ⊂ ℰ′_(I,j) by [[lem:iii-c-3-2]] (d), as min Re ℰ₀ > 3/2 + 2γ_Υ): h ∈ H^(∞,(ℰ₀,ℓ₀),⟨ℰ′⟩,α′)_b on U, and
off U trivially. This is [Hin26, Theorem 5.21, Step 2.6], with its ℰ_I^(C,new). Repeating with (α_I, ℰ_I^C) replaced
by (α′, ℰ′), ν > ¼, reaches ℓ_I after J ≤ 4(ℓ_I − ℓ^♭_I) + 1 repetitions, with index sets
ℰ^((0)) ⊂ ℰ^((1)) ⊂ ⋯ ⊂ ℰ^((J)); take ℰ_I^C := ℰ^((J)), with ℰ^((0)) the smallest index set of [[def:iii-c-3-1]]
containing ℰ₀. As the number of repetitions and every step depend only on ℰ₀, ℓ₀, ℓ_I and the parameters, so does
ℰ_I^C. This is [[eq:iii-c1-3-1]].

*Smallness, [[eq:iii-c1-3-2]].* Each step is linear in the data of the previous one: the coefficients of the expansion
at I₀ are obtained from Rh, which [[eq:iii-c1-2-2]] bounds by the data and the right side of [[eq:iii-c1-3-4]]; that
right side is quadratic in h, bounded in H^(k,α₀+3) by the norms of the previous step times the small
‖h‖_(H^(k+2,ℓ^♭₀,(−,ℓ^♭_I))); and [[lem:iii-a-1-2]], [[lem:iii-a-1-3]] and [[lem:iii-a-3-2]] are bounded at every order.
At ℐ⁺ the coefficients are obtained by the integrations (i)–(iv), bounded likewise. Finitely many steps compose to
[[eq:iii-c1-3-2]], with k₀ the sum of the losses plus that of [[thm:iii-c1-2-1]]. ∎

**Remark {#rem:iii-c1-3-2}** (No subtraction of radiation fields.) In dimension 3 + 1 the entries A^h − A₀ and B^h of
[Hin26, (5.28)] are of the order of A₀ at ℐ⁺, so the radiation fields of π₁₁h and π̸₀h enter the leading part of the
operator; [Hin26, Theorem 5.21, Step 2] removes them by measuring h from g₀ = g_(b₀) + h₀, at the cost of the forcing
term P(g₀, g_(b₀)) ([Hin26, (5.64)], with the class ⟨(2, 0)⟩₀). In dimension 4 + 1 they are half an order lower
([[rem:s17-dimension]] (c)) and sit in the error of [[eq:iii-c1-3-5]], whose index set ℰ_I^tot + ℰ_I^tot − 1 lies in
ℰ_I^C by [[def:iii-c-3-1]] (3). So the subtraction is not needed, and no class with (3/2, 0) in slot 6 is used as a
background.

### The boosted background {#sec:iii-c2-1}

[[sec:iii-c2-1]]–[[sec:iii-c2-4]] are [Hin26, Sections 5.6–5.7] (Theorem 5.23 with the cut-off gauge (5.76), Remark
5.24, Proposition 5.25, Section 5.7.1, Remark 5.26 and Example 5.27; pp. 108–113) in dimension 4 + 1. The cut-off
boosts φ_S, S = S_w ∈ 𝒮₁, and the cut-offs χ_IVP, χ_K are those of [[sec:iii-b-5]], and |S| := |w|. The gauge 1-form
Υ⁰(g, g₀) and E^Υ_(g₀) are those of [[sec:iii-b-6]] ([[eq:iii-b-6-1]], [[eq:iii-b-6-3]]).

**Lemma {#lem:iii-c2-1-1}** (The boosted Tangherlini metric on the exterior domain; [Hin26, Section 5.6, first
paragraph] in dimension 4 + 1.) There is ε_φ > 0 such that for S ∈ 𝒮₁ with |S| < ε_φ and r₁ ≥ R₀ + 1: φ_S*g_(b₀)
agrees on Ω_(ext,r₁) with an element of 𝒢 ([[def:iii-c-3-4]]), it is Ricci flat, and φ_S*g_(b₀) − g_(b₀) satisfies
the pointwise bounds of the proof of [[lem:iii-c1-1-1]]. Hence [[thm:iii-c1-2-1]] and [[thm:iii-c1-3-1]] hold with
g_(b₀) replaced by g₀ = φ_S*g_(b₀) ([[rem:iii-c1-2-2]] (2); for [[thm:iii-c1-3-1]], the same proof, with
[[prop:iii-c-4-4]] applied with g₁ = g₀ ∈ 𝒢).

*Proof.* On Ω_(ext,r₁), t_IVP ≥ −(r − r₁)/12 > −|x|/10, so χ_IVP = 1 there ([[sec:iii-b-5]]); and
t_IVP ≤ r + 2r^(1−ℓ^♭_I) there, so t ≤ |x| + C, and χ_K = 0, as supp χ_K ⊂ {|x| < t/2} (χ^♯_K = 1 near supp χ_K). So
Ω_(ext,r₁) ⊂ {χ_IVP(1 − χ_K) = 1}, and [[lem:iii-c-3-5]] (2) with [[eq:iii-b-5-3]] gives
φ_S*g_(b₀) − g_(b₀) = |x|⁻²h_S(ω)(dx¹)² + ρ₀²ρ_I³C^∞ there for |S| small, with h_S smooth and O(|S|)
([[eq:iii-b-5-2]]). The first term has only the slot π₁₁ and lies in ρ₀²ρ_I²C^∞, and g_(b₀) ∈ 𝒢 ([[lem:iii-c-3-5]]
(1)); so φ_S*g_(b₀) satisfies [[eq:iii-c-3-4]] on Ω_(ext,r₁). Ric(φ_S*g_(b₀)) = φ_S*Ric(g_(b₀)) = 0. And
δ := φ_S*g_(b₀) + h − η obeys the pointwise bounds of the proof of [[lem:iii-c1-1-1]] (the slots of φ_S*g_(b₀) − η are
those of g_(b₀) − η plus the term above in the slot π₁₁, [[def:iii-c-3-4]]), so the hypersurfaces of Ω_(ext,r₁) stay
spacelike for |S| small. ∎

So the boost need only be genuine where the exterior problem is posed, and the slope 1/12 of [[lem:iii-c1-1-1]]
arranges it. The region where χ_IVP < 1 lies below Σ_(past,r₁) and plays no part.

### Stability with boosted background and data {#sec:iii-c2-3}

For h on Ω_(ext,r₀) and r₁ := 2r₀, put

    h_(S,0) := (φ_S*h)|_(Σ_(IVP,r₁)),     h_(S,1) := rℒ_(∂_(t_IVP))(φ_S*h)|_(Σ_(IVP,r₁)),                {#eq:iii-c2-3-1}

defined for |S| < ε′_φ, with ε′_φ independent of r₀, as φ_S maps a neighbourhood of Σ_(IVP,r₁) into
{|t_IVP| < r/8} ∩ Ω_(ext,r₀): φ_S is the time-1 flow of a b-vector field, and near |x| = r it moves t_IVP by at most
C|S|r ([[lem:iii-b-5-1]], [[lem:iii-b-5-2]]), while for r ≥ r₁ = 2r₀ the past slab of Ω_(ext,r₀) reaches down to
−(r − r₀)/12 ≤ −r/24; so C|S| < 1/24 suffices, for every r₀. ([Hin26] takes r₁ = r₀ + 1; then the slab reaches only to
−1/12 near |x| = r₁, while a boost moves t_IVP by about |S|r₁, so |S| would have to be below about 1/(12Cr₁), against
the bound depending only on b₀ and ℓ^♭ that [Hin26, Theorem 5.23] states.)

**Theorem {#thm:iii-c2-3-1}** ([Hin26, Theorem 5.23] in dimension 4 + 1.) There are k₂ ∈ ℕ and ε₂ > 0 such that the
following holds. Let h₀, h₁ be data as in [[thm:iii-c1-3-1]] with ‖h_j‖_(H^(k₂,ℓ^♭₀)_b) < ε₂ (j = 0, 1), and let h be
the solution of

    P^(χ₀)(g_(b₀) + h, g_(b₀)) = 0,     h|_(Σ_(IVP,r₀)) = h₀,     rℒ_(∂_(t_IVP))h|_(Σ_(IVP,r₀)) = h₁     {#eq:iii-c2-3-2}

that [[thm:iii-c1-2-1]] gives in the cut-off gauge ([[cor:iv2-4-1]]), which by its proof is small in H^(3d) of its
class for the d = 7 of [[thm:iv2-3-1]]. It lies in H^(∞,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_(ext,r₀)) by [[thm:iii-c1-3-1]], whose
proof holds for L^(χ₀) by [[lem:iii-c2-2-1]], which leaves the leading part at ℐ⁺ unchanged and adds to the error of
[[eq:iii-c-4-4]] a term of that class. For S ∈ 𝒮₁ small, depending only on b₀, ℓ^♭₀ and ℓ^♭_I, the
problem

    P^(χ₀)(φ_S*g_(b₀) + h_S, φ_S*g_(b₀)) = 0 in Ω_(ext,r₁),     h_S = h_(S,0),  rℒ_(∂_(t_IVP))h_S = h_(S,1) on Σ_(IVP,r₁)
                                                                                                         {#eq:iii-c2-3-3}

([[lem:iii-c2-1-1]]) has a solution h_S ∈ H^(∞,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_(ext,r₁)), unique among the solutions in
H^(∞,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₁)) that are small in H^(8,ℓ^♭₀,(−,ℓ^♭_I))_b. By the proof, k₂ = 2N_NM + 2 = 308, with
N_NM = 153 the order of [[thm:iv2-3-1]]. Then:

(1) h_S at S = 0 is h on Ω_(ext,r₁); and under the hypotheses of (3), h_S = φ_S*h on a neighbourhood in Ω_(ext,r₁) of
Σ°_(IVP,r₁) := Σ_(IVP,r₁) ∩ {|x| > r₁};

(2) h_S depends smoothly on S, in the sense of [Hin26, footnote 59]: it is C^l in S with values in
H^(k,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b for data of regularity depending on k and l;

(3) if h₀, h₁ induce data satisfying the vacuum constraint equations and Υ⁰(g_(b₀) + h, g_(b₀)) = 0 at
Σ_(IVP,r₀), then Ric(φ_S*g_(b₀) + h_S) = 0 and Υ^(χ₀E_Υ)(φ_S*g_(b₀) + h_S, φ_S*g_(b₀)) = 0.

*Proof.* *The solution h_S.* For |S| < ε_φ, [[lem:iii-c2-1-1]], [[rem:iii-c1-2-2]] (2) and [[cor:iv2-4-1]] give
[[thm:iii-c1-2-1]] on Ω_(ext,r₁) in the cut-off gauge with φ_S*g_(b₀) in place of g_(b₀). Its threshold ε₀ can be taken
equal to one ε_* > 0 for all |S| ≤ ½ε_φ. Indeed, the constants of [[thm:iv2-2-4]] and [[thm:iv2-3-1]] depend on the
background g₀ only through the pointwise bounds of the proof of [[lem:iii-c1-1-1]] and through finitely many of the
seminorms that define 𝒢 ([[def:iii-c-3-4]]), the C^∞-seminorms on Ω_(ext,r₁) of ρ₀⁻²ρ_I⁻²(g₀ − η) and of
ρ₀⁻²ρ_I⁻³π(g₀ − η): the coefficients of P^(χ₀) and of L^(χ₀) are smooth functions of g₀ and of its b-derivatives of
order at most two, and the leading part at ℐ⁺ does not depend on g₀ ([[rem:iii-c1-2-2]] (2)). For g₀ = φ_S*g_(b₀) these
seminorms depend continuously on S (the expansion of the proof of [[lem:iii-c2-1-1]] is smooth in S, as used in the
proof of (2) below), so they are bounded for |S| ≤ ½ε_φ, and so are the constants C_k, C_(s,t) and δ of
[[thm:ii-g-2-1]] that fix ε₀.

Let |S| < ε′_φ, and let 𝒰 be a neighbourhood of Σ_(IVP,r₁) that φ_S maps into {|t_IVP| < r/8} ∩ Ω_(ext,r₀) (after
[[eq:iii-c2-3-1]]). There ρ_I is bounded below, so the class of h there is H^(∞,ℓ^♭₀)_b. Pullback by φ_S is bounded from
H^(k,ℓ^♭₀)_b(φ_S(𝒰)) to H^(k,ℓ^♭₀)_b(𝒰), uniformly in S: φ_S is the time-1 flow of a b-vector field linear in S and
tangent to every boundary hypersurface ([[lem:iii-b-5-1]]), so the b-derivatives of φ_S and of its inverse are bounded
uniformly, and ρ ∘ φ_S/ρ is bounded above and below. Near I₀, r∂_(t_IVP) = ∂_τ is a b-vector field, and the frame of
[[eq:iii-c-1-6]] does not depend on t; so rℒ_(∂_(t_IVP)) is a first-order b-differential operator near Σ_(IVP,r₁). The
restriction to Σ_(IVP,r₁) is bounded from H^(k+1,ℓ^♭₀)_b to H^(k,ℓ^♭₀)_b(Σ_(IVP,r₁)), as in the proof of [[thm:iv2-3-1]]
(ii). Hence, with C_* independent of S,

    ‖h_(S,j)‖_(H^(N_NM,ℓ^♭₀)_b(Σ_(IVP,r₁))) ≤ C_*‖h‖_(H^(N_NM+2,ℓ^♭₀,(−,ℓ^♭_I))_b(Ω_(ext,r₀))),     j = 0, 1.

Let k₂ and ε₂ be the k₁ and ε₁ that the clause of [[thm:iii-c1-2-1]] on higher norms, in the cut-off gauge, gives for
k := N_NM + 2 and ε := ε_*/C_*; by its proof, k₂ = N_NM + k = 2N_NM + 2. As k₂ is at least, and ε₂ at most, the k₀ and
ε₀ of [[thm:iii-c1-2-1]] for g_(b₀) on Ω_(ext,r₀), data with ‖h_j‖_(H^(k₂,ℓ^♭₀)_b) < ε₂ have the smallness that theorem
asks, so h exists, and the clause on higher norms applies to it. If ‖h_j‖_(H^(k₂,ℓ^♭₀)_b) < ε₂, then
‖h‖_(H^(N_NM+2,ℓ^♭₀,(−,ℓ^♭_I))_b) < ε_*/C_*, so the data [[eq:iii-c2-3-1]] have H^(N_NM,ℓ^♭₀)_b-norm below ε_*, and
[[thm:iii-c1-2-1]] for the background φ_S*g_(b₀) gives h_S and its uniqueness, for |S| < min(½ε_φ, ε′_φ), a bound
depending only on b₀, ℓ^♭₀ and ℓ^♭_I. The data [[eq:iii-c2-3-1]] lie in H^(∞,(ℰ₀,ℓ₀))_b(Σ_(IVP,r₁)): h is of that class
near Σ_(IVP,r₁) away from ℐ⁺, and pullback by φ_S preserves weighted, partially polyhomogeneous b-Sobolev spaces near
compact subsets of the interior of I₀ (φ_S is the flow of a b-vector field; [Hin26, after (5.77b)]). So
[[thm:iii-c1-3-1]] for this background ([[lem:iii-c2-1-1]]) places h_S in H^(∞,(ℰ₀,ℓ₀),⟨ℰ_I^C⟩,ℓ_I)_b(Ω_(ext,r₁)).

(1) For S = 0, φ_0 = id and [[eq:iii-c2-3-3]] is [[eq:iii-c2-3-2]] on Ω_(ext,r₁) ⊂ Ω_(ext,r₀). The restriction of h to
Ω_(ext,r₁) solves it and, like h_0, is small in H^(3d) of its class for the d = 7 of [[thm:iv2-3-1]], hence in H⁸; so
h_0 = h there by the uniqueness. Now assume the hypotheses of (3), and let 𝒰 be as above, so that φ_S maps 𝒰 into
{|t_IVP| < r/8} ∩ Ω_(ext,r₀), where χ₀ = 0. [[rem:iii-c1-2-2]] (1) applies to h in the cut-off gauge ([[prop:np-10-57-d]]
with Υ = Υ^(χ₀E_Υ), whatever the term of order zero in the gauge; and Υ^(χ₀E_Υ) = Υ⁰ near Σ_(IVP,r₀), where χ₀ = 0):
Ric(g_(b₀) + h) = 0 and Υ^(χ₀E_Υ)(g_(b₀) + h, g_(b₀)) = 0 on Ω_(ext,r₀), and on φ_S(𝒰), where χ₀ = 0,
Υ⁰(g_(b₀) + h, g_(b₀)) = 0. Pulling back by φ_S, Ric(φ_S*g_(b₀) + φ_S*h) = φ_S*Ric(g_(b₀) + h) = 0 and, by
[[eq:iii-c2-2-2]], Υ⁰(φ_S*g_(b₀) + φ_S*h, φ_S*g_(b₀)) = 0 on 𝒰, where χ₀ = 0 as well; so both terms of
P^(χ₀)(φ_S*g_(b₀) + φ_S*h, φ_S*g_(b₀)) vanish on 𝒰, and φ_S*h solves [[eq:iii-c2-3-3]] there with the data
[[eq:iii-c2-3-1]]. The whole operator is not pulled back: δ*_(g₀,E_C) is not natural, E_C being built from the fixed
stationary 1-form c_C of [[def:iii-b-6-1]], which a boost does not preserve (φ_S*c_C ≠ c_C); so φ_S*h solves the
equation with φ_S*c_C, while [[eq:iii-c2-3-3]] has c_C, and the two agree where Υ⁰ vanishes. Without the constraints
statement (1) is not proved here; [Hin26, Theorem 5.23 (1)] states it without them, but its proof pulls back the whole
operator. So v := h_S − φ_S*h satisfies L̄v = 0 on 𝒰 ∩ Ω_(ext,r₁) with vanishing Cauchy data on Σ_(IVP,r₁), where, with
g₀ := φ_S*g_(b₀) and g_s := g₀ + φ_S*h + sv, L̄ := ∫₀¹ L^(χ₀)_(g_s,g₀) ds. Each g_s is a convex combination of
φ_S*(g_(b₀) + h) and φ_S*g_(b₀) + h_S, so it is close to g_(b₀) in the frame of [[eq:iii-c-1-6]] for |S| and the data
small ([[lem:iii-c2-1-1]]); hence 2L̄ has principal symbol ḡ⁻¹(ζ, ζ)Id with ḡ⁻¹ := ∫₀¹ g_s⁻¹ ds, the inverse of a
Lorentzian metric ḡ for which dt_IVP is timelike. Let M := 𝒰 ∩ Ω°_(ext,r₁), the interior, time-oriented by ∂_t.
t_IVP increases along future ḡ-causal curves in M, so Σ°_(IVP,r₁) ⊂ M is acausal, and its Cauchy development D in M
is open, globally hyperbolic and has Σ°_(IVP,r₁) as a Cauchy hypersurface ([[thm:std-bgp-development]]). On D the
coefficients of L̄ are smooth and v and its first derivatives vanish on Σ°_(IVP,r₁), so [[lem:s26-uniqueness]] with
P = 2L̄ gives v = 0 on D, a neighbourhood of Σ°_(IVP,r₁) in Ω_(ext,r₁).

(2) The data [[eq:iii-c2-3-1]] depend smoothly on S (differentiate [[eq:iii-c2-3-1]]). Formally
ḣ := (d/ds)h_(S(s))|_(s=0), with S(0) = S₀ and Ṡ = S′(0), solves

    L^(χ₀)_(φ_(S₀)*g_(b₀)+h_(S₀), φ_(S₀)*g_(b₀))ḣ = −(d/ds)P^(χ₀)(φ_(S(s))*g_(b₀) + h_(S₀), φ_(S(s))*g_(b₀))|_(s=0),

with the differentiated data. Let D₁, D₂ denote the derivatives in the first and the second argument. As
P^(χ₀)(g₀, g₀) = 0 for every Ricci-flat g₀ (the proof of [[lem:iii-c2-2-1]]), in particular along φ_(S(s))*g_(b₀)
([[lem:iii-c2-1-1]]), with g₀ := φ_(S₀)*g_(b₀) and ġ₀ := (d/ds)φ_(S(s))*g_(b₀)|_(s=0) the right side is

    −[(D₁ + D₂)P^(χ₀)(g₀ + h_(S₀), g₀) − (D₁ + D₂)P^(χ₀)(g₀, g₀)]ġ₀,

which carries a factor of h_(S₀) ([[lem:iii-c-4-3]]); without this cancellation the index set at I₀ would be (4, 0),
which need not lie in ℰ₀ + 2 (for instance ℰ₀ = ∅, [[rem:iii-c2-4-3]]). So it is a linear differential expression in
ġ₀, which lies in ρ₀²ρ_I²C^∞ with the slots of [[eq:iii-c-3-4]] on Ω_(ext,r₁) (differentiate the expansion of the proof
of [[lem:iii-c2-1-1]] in S), applied with coefficients in the classes of [[prop:iii-c-4-4]]; so it lies in the target
space of [[eq:iii-c-5-2]]. The linear estimate [[eq:iii-c1-2-2]], which holds for L^(χ₀) by [[lem:iii-c2-2-1]] and
[[cor:iv2-4-1]], and the proof of [[thm:iii-c1-3-1]] give ḣ in the class of h_S; difference quotients converge to ḣ by
the same estimate applied to their difference with ḣ, and higher derivatives follow likewise, with the losses of
[Hin26, footnote 59].

(3) The metrics φ_S*g_(b₀) + h_S and φ_S*(g_(b₀) + h) have the same Cauchy data on Σ_(IVP,r₁) ([[eq:iii-c2-3-1]],
[[eq:iii-c2-3-3]]), hence the same first and second fundamental forms and the same Υ⁰ there, Υ⁰ involving the metric
and its first derivatives only; so (3) does not depend on (1). By the proof of (1), the Ricci tensor and Υ⁰ of
φ_S*(g_(b₀) + h) vanish on 𝒰 ⊃ Σ_(IVP,r₁). So the data of φ_S*g_(b₀) + h_S at Σ_(IVP,r₁) satisfy the constraints,
and Υ^(χ₀E_Υ) = Υ⁰ = 0 there (χ₀ = 0 near Σ_(IVP,r₁)). [[rem:iii-c1-2-2]] (1), with [[rem:iii-c1-2-2]] (2) for the
background φ_S*g_(b₀) and with [[prop:np-10-57-d]] for the cut-off gauge, applied to [[eq:iii-c2-3-3]], gives the
conclusions on Ω_(ext,r₁). ∎

**Remark {#rem:iii-c2-3-2}** ([Hin26, Remark 5.24] in dimension 4 + 1.) If h₀ = h₁ = 0, then h_S = 0 by uniqueness,
and the metric is φ_S*g_(b₀). On all of Σ_IVP such data are compactly supported perturbations of the Myers–Perry data,
as gluing produces them ([CD03]; [[ch:s28]]).

### Gauged Cauchy data {#sec:iii-c2-4}

**Proposition {#prop:iii-c2-4-1}** ([Hin26, Proposition 5.25] in dimension 4 + 1.) Let ℰ₀ be an index set with
min Re ℰ₀ > 0 and jℰ₀ ⊂ ℰ₀ for j ∈ ℕ, and ℓ₀ > 0. The second fundamental form of Σ_IVP for a metric g is taken as in
[[lem:iii-b-3-9]]: k(X, Y) := g(∇^g_Xν, Y) for X, Y tangent to Σ_IVP, with ν the future unit normal. Let
γ = γ_(b₀) + γ̃ and k = k_(b₀) + k̃ be symmetric 2-tensors on Σ_IVP, γ_(b₀) and k_(b₀) the first and second fundamental
forms of Σ_IVP for g_(b₀), with γ̃ ∈ H^(∞,(ℰ₀,ℓ₀))_b(Σ_IVP; S²T*Σ_IVP), k̃ ∈ H^(∞,(ℰ₀+1,ℓ₀+1))_b(Σ_IVP; S²T*Σ_IVP), and
γ̃ small in H³_b. There are h₀, h₁ ∈ H^(∞,(ℰ₀,ℓ₀))_b(Σ_IVP; S²T*), depending continuously on (γ̃, k̃) and 0 at (0, 0),
such that for every spacetime metric g with (g − g_(b₀))|_(Σ_IVP) = h₀ and (rℒ_(∂_(t_IVP))(g − g_(b₀)))|_(Σ_IVP) = h₁:
(1) the first and second fundamental forms of Σ_IVP for g are γ and k; (2) Υ⁰(g, g_(b₀)) = 0 at Σ_IVP.

*Proof.* We follow [Hin26], which follows [HV18b, Proposition 3.10] and [HV24, Theorem 4.2]; the dimension enters only
through the size of the frame. Near Σ_IVP write g_(b₀) = a dt_IVP² + 2dt_IVP ⊗_s b + γ_(b₀) and set h₀ := γ̃, extended
to S²T* by h₀(ν_(b₀), ·) := 0, so that g₀ := g_(b₀) + h₀ induces γ. Let ν_(b₀) and ν₀ = ν_(b₀) + ν̃ be the future unit
normals; ν̃ ∈ H^(∞,(ℰ₀,ℓ₀))_b. We seek h₁ = rh̃₁ such that g := g₀ + t_IVP h̃₁ (still with unit normal ν₀ at Σ_IVP)
has second fundamental form k and Υ⁰(g, g_(b₀)) = 0 there. For X, Y tangent to Σ_IVP, g(ν, Y) = 0 along Σ_IVP, so
X(g(ν, Y)) = 0 gives k_g(X, Y) = −g(ν, ∇^g_XY) for the second fundamental form k_g of g with unit normal ν. As g = g₀
on Σ_IVP, with the same unit normal ν₀, k_g(X, Y) = −g₀(∇^g_XY, ν₀). Writing g₀ = g_(b₀) + h₀ and ν₀ = ν_(b₀) + ν̃,

    g₀(∇^(g₀)_XY, ν₀) = −k_(b₀)(X, Y) + h₀(∇^(g_(b₀))_XY, ν_(b₀)) + g₀(∇^(g_(b₀))_XY, ν̃)
                          + g₀((∇^(g₀)_X − ∇^(g_(b₀))_X)Y, ν₀),

as g_(b₀)(∇^(g_(b₀))_XY, ν_(b₀)) = −k_(b₀)(X, Y). Subtracting this from g₀(∇^g_XY, ν₀) = −k_(b₀)(X, Y) − k̃(X, Y),
which is k_g = k, gives the first of the two conditions; the second is Υ⁰(g, g_(b₀)) = 0 at Σ_IVP. They are the
conditions of [Hin26, (5.80) and (5.81)], written in the convention of [[lem:iii-b-3-9]]:

    g₀((∇^g_X − ∇^(g₀)_X)Y, ν₀) = −k̃(X, Y) − h₀(∇^(g_(b₀))_XY, ν_(b₀)) − g₀(∇^(g_(b₀))_XY, ν̃)
                                    − g₀((∇^(g₀)_X − ∇^(g_(b₀))_X)Y, ν₀),
    tr_(g₀)(∇^g − ∇^(g₀)) = −tr_(g₀)(∇^(g₀) − ∇^(g_(b₀))).

Each x-derivative of h₀ gains a factor r⁻¹ (b-regularity), the Christoffel symbols of g_(b₀) are O(r⁻³) with all
b-derivatives in dimension 4 + 1 ([[prop:iii-b-3-6]]: the mass enters at |x|⁻²), and ℰ₀ is closed under sums; so both
right sides lie in H^(∞,(ℰ₀+1,ℓ₀+1))_b. In a frame e₀ = ν₀, e₁, …, e₄, g₀-orthonormal and tangent to Σ_IVP for
i ≥ 1, at t_IVP = 0,

    2(Γ(g)_(λμν) − Γ(g₀)_(λμν)) = (t_IVP)_(;μ)(h̃₁)_(νλ) + (t_IVP)_(;ν)(h̃₁)_(μλ) − (t_IVP)_(;λ)(h̃₁)_(μν),

with e_it_IVP = 0 (i ≥ 1) and e₀t_IVP in C^∞ + H^(∞,(ℰ₀,ℓ₀))_b and bounded away from 0. The first equation at
(e_i, e_j), i, j = 1, …, 4, reads −½(e₀t_IVP)(h̃₁)_(ij) = ⋯ and determines (h̃₁)_(ij); the e^j-component of the second
determines (h̃₁)_(0j); and its e⁰-component, −½(e₀t_IVP)(h̃₁)₀₀ = f₀ + ½(e₀t_IVP)(g₀)^(ij)(h̃₁)_(ij), with f₀ the
e⁰-component of its right side, determines (h̃₁)₀₀; all lie in H^(∞,(ℰ₀+1,ℓ₀+1))_b, linearly and continuously in the
data. So h₁ = rh̃₁ ∈ H^(∞,(ℰ₀,ℓ₀))_b. ∎

These data enter [[thm:iii-c1-3-1]] when min Re ℰ₀ > 3/2 + 2γ_Υ, ℓ₀ > 3/2 and ‖h_j‖_(H^(k₀,ℓ^♭₀)_b) < ε₀ as in
[[thm:iii-c1-2-1]] (k₀ = N_NM = 153), and they enter [[thm:iii-c2-3-1]] when moreover ‖h_j‖_(H^(k₂,ℓ^♭₀)_b) < ε₂
(k₂ = 2N_NM + 2 = 308). Both smallness conditions hold for (γ̃, k̃) small in a suitable norm, by the continuity in
[[prop:iii-c2-4-1]]. If (γ, k) satisfy the constraints, the solutions are vacuum ([[rem:iii-c1-2-2]] (1),
[[thm:iii-c2-3-1]] (3)).

**Proposition {#prop:iii-c2-4-2}** (Data at Boyer–Lindquist time 0; [Hin26, Section 5.7.1 and Remark 5.26] in
dimension 4 + 1.) Let t_BL be the Boyer–Lindquist time of g_(b₀), Σ^BL := t_BL⁻¹(0) near spatial infinity, and
γ^BL_(b₀), k^BL_(b₀) the first and second fundamental forms of Σ^BL for g_(b₀), k as in [[prop:iii-c2-4-1]]. Let ℰ₀, ℓ₀
and ℓ^♭₀ be as in [[thm:iii-c1-3-1]], δ ∈ (0, ¼] small, and let γ^BL = γ^BL_(b₀) + γ̃^BL and k^BL = k^BL_(b₀) + k̃^BL be
symmetric 2-tensors on Σ^BL ∩ {r > δ⁻¹} satisfying the vacuum constraint equations, with γ̃^BL ∈ H^(∞,(ℰ₀,ℓ₀))_b and
k̃^BL ∈ H^(∞,(ℰ₀+1,ℓ₀+1))_b. Let h^BL_0, h^BL_1 be the gauged Cauchy data on Σ^BL that the proof of [[prop:iii-c2-4-1]]
gives with t_BL in place of t_IVP, and assume them small in H^(N_NM,ℓ^♭₀)_b, N_NM = 153 as in
[[thm:iv2-3-1]] (by the continuity in [[prop:iii-c2-4-1]], this holds for (γ̃^BL, k̃^BL) small in a suitable norm).
Then the solution h of the gauge-fixed equation with Υ⁰,
Ric(g_(b₀) + h) − δ*_(g_(b₀),E_C)Υ⁰(g_(b₀) + h, g_(b₀)) = 0, with these data, on the domain of dependence D_δ of
Σ^BL ∩ {r > δ⁻¹} within the conic neighbourhood U_δ := {|t/r| < δ, r > δ⁻¹} of spatial infinity, induces on
Σ_IVP ∩ {r > r₀}, for r₀ large, data (h₀, h₁) in H^(∞,(ℰ₀,ℓ₀))_b: the index set is unchanged, and no index set
ℰ_log arises.

*Proof.* *The time functions.* On {|x| ≥ R₃}, t_IVP = t − C″ ([[lem:iii-b-3-7]] (b)), with t = t_KS + T_m the time of
[[eq:iii-b-3-3]] and T_m = 2m r⁻¹ + O(r⁻³) ([[lem:iii-b-3-5]] (a)). For the Tangherlini metric of mass m,
f = 1 − m r⁻², t_KS − t_BL = ∫ m r⁻²(1 − m r⁻²)⁻¹ dr = −m r⁻¹ − m²/(3r³) − ⋯, an odd series in r⁻¹; so
t − t_BL = m r⁻¹ + O(r⁻³), a smooth function of ρ = r⁻¹ near ρ = 0 (in dimension 3 + 1 the integral is 2m log r). So
τ_IVP := t_IVP/r = τ_BL + ρc(ρ) and τ_BL := t_BL/r = τ − ρc̃(ρ), with c and c̃ smooth.

*The solution.* As dτ_BL = dτ + O(ρ) in the b-sense, G_b(dτ_BL, dτ_BL) = τ² − 1 + O(ρ) < 0 on U_δ, and |τ| < ¼ there,
inside the range of [[prop:iv-4-1]]. So [[lem:iv2-2-2]] holds with τ′ replaced by τ_BL and Σ_(IVP,r₀) by
Σ^BL ∩ {r > δ⁻¹}, on D_δ: its proof uses only that the initial surface is a level set of a b-time function and the
b-structure of the operator, and U_δ itself has the timelike side {r = δ⁻¹}, so the problem is posed on D_δ. The
operator with Υ⁰ differs from L by a first-order term of the class absorbed there (the proof of [[lem:iii-c2-2-1]] with
χ₀ = 0, ρ_I being bounded below on U_δ). With these estimates for the right inverses, [[thm:ii-g-2-1]] gives h on D_δ as
in the proof of [[thm:iv2-3-1]] (d = 7, trivial support classes); this is the boost problem of [COM81], as in [Hin26].
Its partial polyhomogeneity h ∈ H^(∞,(ℰ₀,ℓ₀))_b(D_δ) follows as in Step 1 of the proof of [[thm:iii-c1-3-1]], with
[[lem:iv2-2-2]] in place of [[eq:iii-c1-2-2]]. On Σ_IVP, t is bounded, so Σ_IVP ∩ {r > r₀} ⊂ D_δ for r₀ large.

*The data.* Taylor expansion of a(τ_BL)ρ^z(log ρ)^k = a(τ_IVP − ρc(ρ))ρ^z(log ρ)^k in ρ gives the terms
ρ^(z+j)(log ρ)^k, j ∈ ℕ₀: the index set (z, k) + ℕ₀ ⊂ ℰ₀, with no new logarithm. ∎

So [Hin26, Remark 5.26] (logarithms from (2, 0) + ℰ_log) has no counterpart in dimension 4 + 1 from this mechanism;
logarithmic index sets enter the later chapters for other reasons (the analysis at ι⁺ and K⁺).

**Remark {#rem:iii-c2-4-3}** ([Hin26, Example 5.27] in dimension 4 + 1.) (1) Data equal to the data of g_(b₀) outside a
compact set satisfy [[prop:iii-c2-4-1]] with ℰ₀ = ∅ and every ℓ₀; gluing produces data equal outside a compact set to
those of a member of the family ([CD03] in dimension 4 + 1; [[ch:s28]]). (2) The constructions by the conformal
method in [Hin26, Example 5.27 (2)–(3)] are stated in dimension 3 + 1; their counterparts in dimension 4 + 1 are not
used here.

