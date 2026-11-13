## The linearised gauge-fixed Einstein operator {#ch:s15}

This chapter studies the linearised gauge-fixed Einstein operator L_b of the Myers–Perry metrics g_b, b near the
Tangherlini parameter b_0, in dimension 4 + 1. It proves what [Hin26, Section 8] proves on Kerr (pp. 144–163): the
structure of L_b as a stationary wave-type operator ([[lem:iii-f-2-1]]), its Minkowski model and the spectrum of the
model's endomorphism S̄ ([[lem:iii-f-3-1]]), the bound at the trapped set ([[prop:iii-f-4-1]]), the indicial roots at
zero energy ([[lem:iii-f1-2-1]]–[[lem:iii-f1-2-5]]), tf-admissibility and the inverse of the transition face normal
operator on b-Sobolev spaces ([[prop:iii-f1-3-3]], [[cor:iii-f1-3-4]]), the threshold at the event horizon and mode
stability away from zero frequency ([[sec:iii-f2-1]]–[[sec:iii-f2-4]]), the kernel and cokernel of the zero energy
operator and the right inverse built from them ([[sec:iii-f3-1]]–[[sec:iii-f3-4]]), and the zero energy pairings and
the physical large zero energy states ([[sec:iii-f4-1]]–[[sec:iii-f4-5]]). These are [Hin26, Lemmas 8.1, 8.2, 8.4, 8.5,
8.12, 8.15, Propositions 8.3, 8.6, 8.8, 8.9, 8.11, 8.14 (1), Corollaries 8.7, 8.13 and Remark 8.10] in dimension 4 + 1.

The dimensional changes are these. The radial weight ρ∂_ρ − 1 becomes ρ∂_ρ − 3/2, and the mass enters g_b − ḡ at
|x|⁻², so every deviation from Minkowski space gains a power of ρ. The spectrum of S̄ is the union of those of the
gauge potential and constraint propagation operators with five zeros (two in dimension 3 + 1); this follows from a
factorisation of S̄ through 1-forms and needs no explicit matrix. At the trapped set the angular complement of the
null frame is a plane, rotated along the flow; a grading of the symmetric 2-tensors that the rotation preserves gives
the bound for every constraint damping 1-form. The indicial roots of L_b at zero energy are, type by type, the roots of
the gauge potential operator shifted by 1, those of the constraint propagation operator shifted by −1, and the two
gauge-invariant roots −l and l + 2 (−l and l + 1 in dimension 3 + 1), with the roots of the Killing forms removed; the
proof ([[lem:iii-f1-2-1]]) compares L_b with the flat wave operator through the two identities that relate the three
operators, and computes nothing beyond the degrees of the Cartesian components of each type. The gap at zero energy
contains (0, 1]. The input [Hin26] takes from [AHW24, Theorem 6.1] on Kerr, mode stability and the classification of
stationary solutions of the linearised Einstein equation, has no five-dimensional counterpart; at b_0 it is proved here
from the Kodama–Ishibashi decomposition ([[thm:iii-f2-2-2]], [[thm:iii-f3-3-1]]), and near b_0 the kernel is counted
by an augmented operator. The kernel and the cokernel of the zero energy operator are eleven-dimensional (seven in
dimension 3 + 1): the mass, the six rotations of 𝔰𝔬(4) and the four translations. The mass change needs no logarithm.
Among the physical large zero energy states at the root −2 there is a tensor type state, which 𝕊² does not carry.

One result of the main argument enters as an input and is proved here: [[prop:np-10-34-iv]], the equivariance of the
linearised rotations of Minkowski space under rotations and the bracket form of 𝔰𝔬(4). The bound on the number
ε_ind of [[eq:iii-f1-2-2]] at the fixed gauge parameters is [[prop:np-10-52]] of [[ch:s14]].

Every outside result used without proof is from [KI03]: the reduction of the vacuum Einstein equations for each
harmonic type to a master equation. It is stated where it is used ([[sec:iii-f2-2]]), with its numbers and pages.
Everything else is proved here from [[ch:s01]]–[[ch:s14]].

*The dynamical hypotheses* (Dyn) are those of [[ch:s13]]: the hypotheses of [[ch:s01]]–[[ch:s03]] that concern the
metric alone. For g_b, b near b_0, they hold by [[thm:vi-a-6-1]] and [[thm:vi-b1-5-1]], for every operator with
principal symbol G Id.

*The inner radius.* The radii 0 < r_0 − 2δ_0 < r_0 < r_2 < r_h are those of [[sec:i-a-1-1]]. The steps below the
horizon are [[lem:iii-f2-2-3]], on (r_0 − δ_0, r_h), whose radial equation is regular wherever f < 0, and the interior
uniqueness of [[prop:iii-d-6-2]] (d), which holds on (r_0, r_h) for every r_0 > 0; the pairings of [[sec:iii-f4-2]]
use only that one factor vanishes on {r_0 < |x| < r_h}, and the independence of the dual states only that
{|x| > r_0} is connected. Every other step reaches the inner boundary through the theorems of [[ch:s01]]–[[ch:s03]],
which hold with r_0 as a parameter. So every result of this chapter holds with the inner radius r_0 as a parameter.

*Small frequencies near b_0.* For b ≠ b_0 and 0 < |σ| < c_0, invertibility of the spectral family of L_b is not
proved in this chapter: the perturbation argument of [[prop:iii-f2-4-1]] degenerates as c_0 → 0. This range is
supplied by the analysis of the low energy resolvent, in [[cor:iii-h-4-3]] and [[cor:iii-h-4-4]] of [[ch:s18]].

*Notation.* b = (m, A) are the parameters of [[sec:iii-b-3]], b_0 = (m_0, 0), and on g_(b_0) we write
f := 1 − m_0/r², r_h := m_0^(1/2), r := |x|, ρ := r⁻¹ near infinity. On 𝕊³, γ is the round metric and D̂ its
covariant derivative; 𝒮_l, 𝒱_l are the scalar and vector harmonics of degree l ([[def:iii-a1-1-3]]),
κ := l(l + 2) is the eigenvalue of the Laplacian on 𝒮_l, and k := κ^(1/2), k_V := (κ − 1)^(1/2),
k_T := (κ − 2)^(1/2) are the numbers of [KI03] for the scalar, vector and tensor types. The types and degrees, the
bases of the indicial matrices and the indicial roots by type are those of [[eq:iii-a1-2-9]]–[[eq:iii-a1-2-10]] and
[[def:iii-a1-2-2]]; s0, s1, sl, v1, vl, tl abbreviate scalar type 0, 1, l, vector type 1, l and tensor type l. The
variable of indicial families is ι ∈ ℂ, an indicial root is a value of ι, and spec_b is the set of all indicial roots
of the operator considered. The variable of a characteristic polynomial is ν. z := 4e_Υγ_Υ² as in
[[lem:iii-d-4-1]]. For a stationary operator P, P^(σ) := e^(iσt_*) P e^(−iσt_*) is its spectral family, acting on
stationary sections; a stationary section is one whose components in the frame dt_*, dx¹, …, dx⁴ do not depend on
t_*. The symmetric product is a ⊗_s b := ½(a ⊗ b + b ⊗ a), the product ab of the notation of quadratic forms
(so a² = a ⊗ a, and a monomial in covectors denotes their symmetric product).

### The operator {#sec:iii-f-1}

Fix, as [Hin26, Section 8] does, the gauge modification E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)) of [[sec:iii-d-1]],
with 0 < e_Υ ≪ 1 and 0 < γ_Υ ≪ 1 as [[prop:iii-d1-4-1]] allows, so that the gauge potential operator □^Υ_b is mode
stable with the indicial roots of [[lem:iii-d-4-1]]; and the constraint damping data v_C, e_C, c_C, γ_C and C_0 = 100
fixed in [[sec:iv4-0]], for which (1 − e_C)(1 − v_C)γ_C > 100 and the constraint propagation operator □^C_b of
[[eq:iii-e-1-1]] has the properties of [[thm:iii-e-1-1]]. The *linearised gauge-fixed Einstein operator* is

    L_b := D_(g_b)Ric + δ*_(g_b,E_C) δ_(g_b,E_Υ) G_(g_b),                                                 {#eq:iii-f-1-1}

the operator L_(g_b) of [[eq:iii-b-6-8]], acting on symmetric 2-tensors, with δ_(g,E_Υ) := δ_g + E^Υ_g and
δ*_(g,E_C) := δ*_g + E^C_g. By [[eq:iii-b-6-7]]–[[eq:iii-b-6-8]],

    2L_b = □_(g_b) + 2E^C_(g_b) δ_(g_b) G_(g_b) + 2δ*_(g_b,E_C) E^Υ_(g_b) G_(g_b) + 2R_(g_b),             {#eq:iii-f-1-2}

with □_g ġ := −g^(κλ) ġ_(;κλ) and R_g the curvature term of [[eq:iii-b-6-7]]: expand
2(δ* + E^C)(δ + E^Υ)G and use 2D Ric = □ − 2δ*δG + 2R. The spectral family L_b^(σ) acts on stationary sections of
S²T*X, trivialised by the products of dt_*, dx¹, …, dx⁴: the bundle E of [[sec:i-a-1]] with N_E = 15.

### Structure {#sec:iii-f-2}

The Minkowski model is ḡ = −(dt_* + d|x|)² + Σ_i (dx^i)² of [[sec:iii-d-2]], with t̄ := t_* + |x|. With the gauge
modification Ē^Υ of [[sec:iii-d-2]], put c̄_C := |x|⁻¹(dt̄ − v_C d|x|),
Ē^C ω := γ_C(2c̄_C ⊗_s ω − (2/3)(1 − e_C) ḡ ι_(ḡ⁻¹c̄_C) ω) on 1-forms ω, and

    2L̄ := □̄ + 2Ē^C δ̄ Ḡ + 2(δ̄* + Ē^C) Ē^Υ Ḡ.                                                         {#eq:iii-f-2-1}

**Lemma {#lem:iii-f-2-1}** (Structure; [Hin26, Lemma 8.1] in dimension 4 + 1.) (1) 2L_b is stationary with principal
symbol g_b⁻¹(ζ, ζ) Id, and (2L_b)^(σ) = P̂(0) + σT + σ²P_2 satisfies (H1) and the operator part of (H6) of
[[sec:i-a-1]] and [[ch:s02]] with g = g_b, t = t_*: P_2 = g_b^00 Id and σ_1(T) = −2g_b⁻¹(dt_*, ·) Id.

(2) On {|x| > 0}, exactly,

    2L̄ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄) + (2L̄)^(0),
    ρS̄ = −Ē^C ι_X Ḡ + (dt_* ⊗_s ·) Ē^Υ Ḡ,     X := ḡ⁻¹dt_*,                                              {#eq:iii-f-2-2}

with S̄ a bundle endomorphism homogeneous of degree 0, (2L̄)^(0) ∈ ρ² Diff_b², and no ∂_(t_*)² term.

(3) On {|x| > 3R_1},

    2L_b = 2L̄ − g_b^00 ∂²_(t_*) + Q_b ∂_(t_*) + R_b,     g_b^00 ∈ ρ²C^∞(X̄),  Q_b ∈ ρ³ Diff_b¹,
    R_b ∈ ρ⁴ Diff_b²,                                                                                    {#eq:iii-f-2-3}

stationary and smooth in b. Hence (H2) holds with S := S̄ near infinity, and (2L_b)^(0) − (2L̄)^(0) ∈ ρ⁴ Diff_b²;
[Hin26, (8.2)–(8.4)] hold with ρ∂_ρ − 1 replaced by ρ∂_ρ − 3/2, S − S̄ = 0 near infinity, and ρ³ replaced by ρ⁴.

*Proof.* (1) As in [[lem:iii-d-2-1]] (1): the terms of [[eq:iii-f-1-2]] other than □_(g_b) have order at most 1, and
□_(g_b) has principal part −g_b^(μν) ∂_μ ∂_ν Id in the frame; conjugation by e^(−iσt_*) gives the rest, and g_b^00 < 0
on X° by [[lem:iii-b-3-7]] (a).

(2) In Cartesian coordinates □̄ acts componentwise as the scalar wave operator, so by [[lem:iii-a1-2-1]] (1),
□̄ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2) + ᵇ□̄(0), without a ∂²_(t_*) term (ḡ⁻¹ has none, [[eq:iii-a1-2-3]]). The other terms of
[[eq:iii-f-2-1]] have order at most 1. In (t_*, x) a Cartesian derivative ∂_μ has ∂_(t_*)-coefficient (dt_*)_μ
(∂_(t̄) = ∂_(t_*) and ∂_(x^i) = ∂_(x^i)|_(t_*) − (x^i/|x|)∂_(t_*)), so the ∂_(t_*)-coefficient of
δ̄*ω = sym ∂ω is dt_* ⊗_s ω, and that of δ̄h = −ḡ^(μν) ∂_μ h_(ν·) is −ι_X h. Hence the ∂_(t_*)-coefficient of
2L̄ − □̄ is 2(−Ē^C ι_X Ḡ + (dt_* ⊗_s ·)Ē^Υ Ḡ), which is [[eq:iii-f-2-2]]; Ē^C and Ē^Υ carry the factor ρ through c̄_C
and c̄_Υ, so S̄ is homogeneous of degree 0. The stationary remainder is (2L̄)^(0); it lies in ρ² Diff_b², as each
Cartesian derivative lies in ρ𝒱_b on stationary sections and the zeroth-order terms are O(ρ²).

(3) As in [[lem:iii-d-2-1]] (3), with the same inputs: k := g_b − ḡ ∈ ρ²C^∞, g_b⁻¹ − ḡ⁻¹ ∈ ρ²C^∞, ḡ^00 = 0,
Γ(ḡ) ∈ ρC^∞, Γ(g_b) − Γ(ḡ) ∈ ρ³C^∞, Riem(g_b) ∈ ρ⁴C^∞ (two derivatives of k; Riem(ḡ) = 0),
c_C − c̄_C ∈ ρ³C^∞ ([[sec:iii-e-1]]) and E^Υ_(g_b) − Ē^Υ ∈ ρ³C^∞ ([[lem:iii-d-2-1]] (3)). Then □_(g_b) − □̄ has
second-order coefficients in ρ²C^∞ (in the ∂²_(t_*) slot only g_b^00), first-order ones in ρ³C^∞ and zeroth-order ones
in ρ⁴C^∞; E^C_(g_b) − Ē^C ∈ ρ³C^∞, G_(g_b) − Ḡ ∈ ρ²C^∞, δ_(g_b) − δ̄ has first-order coefficients in ρ² and
zeroth-order ones in ρ³, and δ*_(g_b) − δ̄* ∈ ρ³C^∞; so 2E^C δ G − 2Ē^C δ̄ Ḡ and
2δ*_(E_C) E^Υ G − 2(δ̄* + Ē^C)Ē^Υ Ḡ are of first order with ρ³ coefficients and zeroth-order ρ⁴ terms; and
2R_(g_b) ∈ ρ⁴C^∞. Sorting as there: the ρ²∂²_(t_*) terms form −g_b^00 ∂²_(t_*); the ρ²∂_(t_*)∂_(x^i) and ρ³∂_(t_*)
terms form Q_b ∂_(t_*); the ρ²∂_(x^i)∂_(x^j), ρ³∂_(x^i) and ρ⁴ terms form R_b. (H2) follows from (2) as in
[[lem:iii-d-2-1]]. ∎

### The model's endomorphism {#sec:iii-f-3}

**Lemma {#lem:iii-f-3-1}** (The spectrum of S̄; [Hin26, Lemma 8.2 and (8.7)] in dimension 4 + 1.) The characteristic
polynomial of S̄ on S²T* (of dimension 15) is ν⁵ times those of S̄^C and S̄^Υ on T*, the endomorphisms of the
constraint propagation and gauge potential operators ([[sec:iii-e-1]], [[eq:iii-d-2-1]]):

    spec S̄ = {0 (5 times)} ∪ γ_C{2(1 − v_C), (1 − e_C)(1 − v_C), 1 − v_C (3 times)}
             ∪ γ_Υ{2, 1 − e_Υ, 1 (3 times)},                                                             {#eq:iii-f-3-1}

with algebraic multiplicities. In particular every eigenvalue is ≥ 0, and min spec S̄ = 0, which is [Hin26, (8.7)].

*Proof.* Write [[eq:iii-f-2-2]] as ρS̄ = U_1V_1 + U_2V_2 with U_1 := −Ē^C and U_2 := dt_* ⊗_s · from T* to S²T*,
and V_1 := ι_X Ḡ, V_2 := Ē^Υ Ḡ from S²T* to T*. With U := (U_1 U_2) : T* ⊕ T* → S²T* and V := (V_1; V_2),
ρS̄ = UV. For linear maps U of size p × q and V of size q × p, det(ν − UV) = ν^(p−q) det(ν − VU); so
det(ν − UV) = ν^(15−10) det(ν − VU), and

    VU = ⎛ V_1U_1   V_1U_2 ⎞ ,     V_1U_2 ω = ι_X Ḡ(dt_* ⊗_s ω) = 0:
         ⎝ V_2U_1   V_2U_2 ⎠

indeed ι_X(dt_* ⊗_s ω) = ½(dt_*(X)ω + ω(X)dt_*) = ½ω(X)dt_*, as dt_* is null; tr(dt_* ⊗_s ω) = ω(X) and
ι_X ḡ = dt_*, so ι_X Ḡ(dt_* ⊗_s ω) = ½ω(X)dt_* − ½ω(X)dt_* = 0. So det(ν − VU) = det(ν − V_1U_1) det(ν − V_2U_2).
Reading off the ∂_(t_*)-coefficients in the same way for □̄^C = 2δ̄Ḡδ̄* + 2δ̄ḠĒ^C and □̄^Υ = 2δ̄Ḡδ̄* + 2Ē^ΥḠδ̄*
gives ρS̄^C = −ι_X Ḡ Ē^C = V_1U_1 and ρS̄^Υ = Ē^Υ Ḡ(dt_* ⊗_s ·) = V_2U_2. Their spectra: use the null covectors dt_*
and k := dt̄ + d|x| (with X = −∂_(t̄) − ∂_r, dt_*(X) = 0, k(X) = −2, ḡ⁻¹(k, dt_*) = −2), and, by
[[eq:iii-b-6-5]], ḠĒ^C ω = γ_C(2c̄_C ⊗_s ω − e_C ḡ⟨c̄_C, ω⟩) with c̄_C/ρ = ½(1 − v_C)k + ½(1 + v_C)dt_*. Then

    γ_C⁻¹ S̄^C ω = (1 − v_C)ω − ω(X) c̄_C/ρ + e_C⟨c̄_C/ρ, ω⟩ dt_*,

which is (1 − v_C)ω on angular ω, (1 − e_C)(1 − v_C)dt_* on dt_*, and 2(1 − v_C)k + (1 + v_C)(1 − e_C)dt_* on k.
With Ē^Υ Ḡ h = −γ_Υ(2ι_Y h − e_Υ c̄_Υ tr h), Y := ḡ⁻¹dt̄, c̄_Υ = ρ dt̄ ([[eq:iii-b-6-5]]),

    γ_Υ⁻¹ S̄^Υ ω = ω − ω(Y) dt_* + e_Υ ω(X) dt̄,

which is ω on angular ω, 2dt_* on dt_* (dt_*(Y) = −1), and (1 − e_Υ)(k + dt_*) on k. Both are triangular in the bases
(angular, dt_*, k), with the diagonals of [[eq:iii-f-3-1]]. ∎

The explicit form of (2L̄)^(0), [Hin26, (8.6)], is not needed: the indicial roots are found in [[sec:iii-f1-2]]
without it. The triangular structure of S̄ in the splitting of [Hin26, (5.27)], [Hin26, (8.8)], enters only through
[[eq:iii-f-3-1]], in the condition β_sctf < 3/2 + min Re spec S̄ = 3/2 of [[cor:iii-f1-3-4]] (1 in [Hin26]).

### The trapped set {#sec:iii-f-4}

As in [[sec:iii-d-5-2]], [[ch:s02]] uses at the trapped set the bound (Γ.4) with γ_− < 0, that is
sup_Γ λ_max(p_1^Γ) < ½ν_min, with losses governed by δ_Γ, and the inner product may depend on the covector
([[lem:i-b-6-0]]). The operator has real coefficients, so complex conjugation exchanges z_0 = 1 and z_0 = −1, and
[[eq:i-b-1-4]], with its factors z_0, is the same for both; we take z_0 = 1, σ = 1 on Γ.

**Proposition {#prop:iii-f-4-1}** (The trapped set; [Hin26, Proposition 8.3] in dimension 4 + 1, in the form
[[ch:s02]] uses.) Assume (Dyn). For every ϵ > 0 there are a stationary fibre inner product h_Γ on π*S²T* over a
neighbourhood of Γ_(b_0) in phase space, homogeneous of degree 0, and a neighbourhood ℬ_ϵ of b_0, such that for
b ∈ ℬ_ϵ, sup_(Γ_b) λ_max(p_1^Γ) < ϵ for 2L_b, p_1^Γ being [[eq:i-b-6-0]] of [[lem:i-b-6-0]]. In particular (Γ.4)
holds with γ_− < 0, and δ_Γ(0) is as small as wished. At b_0, 2L_(b_0) is strongly trapping admissible
([Hin26c, Definition 5.8]): this holds there for every ϵ with one b.

*Proof.* *The subprincipal operator.* Near Γ_(b_0), E^Υ = 0 ([[sec:iii-d-1]]: the supports of c_Υ and c_(Υ,H) avoid
U_Γ), and R_(g_b) is of order 0. So by [[eq:iii-f-1-2]], on half-densities by |dg|,

    iS_sub(2L_b) = iS_sub(□_(g_b)) + 2E^C_(g_b) σ_1(iδ_(g_b)) G_(g_b),     iS_sub(□_(g_b)) = ∇^(π*S²T*)_(H_G),
                                                                                                          {#eq:iii-f-4-1}

the second identity being [Hin26, (6.13)] for the tensor wave operator, which holds in every dimension
([Hin17, Proposition 4.1]; [[sec:iii-d-5-2]] (a) on 1-forms), with ∇^(π*S²T*) the Leibniz extension of ∇^(π*T*), and
σ_1(iδ_g)(ζ)h = ι_(g⁻¹ζ) h.

*The frame.* At b_0, near Γ_(b_0) (where C > 0), [[sec:iii-d-5-2]] (c) gives e_0 = ζ, e_1, e_2 with Gram matrix CJ and
∇_(H_G) e_0 = 0, ∇_(H_G) e_1 = −2σe_0, ∇_(H_G) e_2 = −2σe_1, and the plane V_⊥ of angular covectors orthogonal to them,
g-positive, ∇_(H_G)-invariant and g-skew there (proof of [[lem:iii-d-5-2]]). Normalise e_0, e_1, e_2 by C^(1/2)
(stationary and homogeneous of degree 0; H_G C = 0 keeps the connection matrix) and let e_3, e_4 be a local
g-orthonormal frame of V_⊥, so that ∇_(H_G) e_a = σϰR(e_a), a = 3, 4, with R the rotation e_3 ↦ e_4 ↦ −e_3 and ϰ a
function homogeneous of degree 0. Write c_C = Σ_μ c_μ e_μ. As c_C is past timelike ([[thm:iii-e-1-1]]) and e_0 is future
null on the future characteristic set, c_2 = −g⁻¹(c_C, e_0) < 0; and γ := C^(1/2)γ_C/σ > 0 (σ > 0 on Γ_(b_0), which lies
in the future characteristic set over {|x| > r_h}). With g⁻¹e_0 = −E_2 (E_μ the dual frame),
σ_1(iδ)(ζ) = −C^(1/2) ι_(E_2), and [[eq:iii-f-4-1]] reads, on components in the frame,

    iS_sub(2L_(b_0)) = H_G + σ(A + ϰR),                                                                   {#eq:iii-f-4-2}

where A = 2N + 2γ E^C_(c)(−ι_(E_2))G, N is the Leibniz extension of e_1 ↦ −e_0, e_2 ↦ −e_1, e_0, e_3, e_4 ↦ 0,
E^C_(c) is the map of [[eq:iii-b-6-2]] with c_C in place, divided by γ_C, and R acts as a derivation.

*The grading.* Give e_0, e_1, e_2, e_3, e_4 the weights 0, 1, 2, 1, 1, and a product of two the sum, wt. Then
g⁻¹(e_μ, e_ν) ≠ 0 only if the weights add to 2, and g = −2e_0e_2 + e_1² + e_3² + e_4² has weight 2. N lowers wt by 1;
R preserves it; ι_(E_2) removes a factor e_2, lowering it by 2; G = I − ½g tr preserves it; and
E^C_(c)ω = 2c ⊗_s ω − (2/3)(1 − e_C)g⟨c, ω⟩ raises it by the weight of the component c_μ e_μ used, at most 2, with
equality only for c_2. So A + ϰR does not raise wt, and its wt-preserving part is D := 2γc_2 Φ + ϰR with

    Φh := 2e_2 ⊗_s ιh − (2/3)(1 − e_C)g⟨e_2, ιh⟩,     ιh := −ι_(E_2)Gh = −ι_(E_2)h − ½(tr h)e_0,

as ι_(E_2) g = −e_0, and ⟨e_2, ω⟩ = −ω_0, the e_0-coefficient of ω. On the monomials: Φ = 0 on weight 0 (e_0²) and
weight 1 (e_0e_1, e_0e_a), for there ιh = 0. On weight 2: Φ(e_0e_2) = 0, as ι(e_0e_2) = −½e_0 + ½e_0 = 0; Φ = 0 on
the five spatial trace-free monomials, as these have no factor e_2 and trace 0 or are differences of monomials of equal
image; and with T := e_1² + e_3² + e_4², ι(e_a²) = −½e_0 for a = 1, 3, 4 (no e_2-factor, trace 1), so ιT = −(3/2)e_0,
⟨e_2, ιT⟩ = 3/2, and

    Φ(T) = 2e_2 ⊗_s (−(3/2)e_0) − (1 − e_C)g = −(1 + 2e_C)e_0e_2 − (1 − e_C)T

(as g = −2e_0e_2 + T and 2e_2 ⊗_s e_0 = 2e_0e_2). On weight 3: ι(e_1e_2) = −½e_1 and ι(e_2e_a) = −½e_a, which have
no e_0-component, so Φ(e_1e_2) = −e_1e_2 and Φ(e_2e_a) = −e_2e_a. On weight 4: ι(e_2²) = −e_2, so Φ(e_2²) = −2e_2².
Refine wt to W := 2wt + s with s = 1 on T and on the spatial trace-free part and s = 0 elsewhere: the only
wt-preserving map changing s is T ↦ e_0e_2, which lowers W. R preserves each of the pieces e_0²;
{e_0e_1, e_0e_3, e_0e_4}; e_0e_2; T; the trace-free spatial part; {e_1e_2, e_2e_3, e_2e_4}; e_2² (T and g are
R-invariant, and R fixes e_0, e_1, e_2). So A + ϰR = D_0 + D_− with D_− lowering W and D_0 preserving each piece, equal
there to a scalar plus ϰR. The scalars are 0, 0, 0, −2(1 − e_C)γc_2, 0, −2γc_2, −4γc_2 in the order above, all ≥ 0
as c_2 < 0 and e_C < 1.

*The inner product.* Let ⟨·, ·⟩_0 be the inner product on π*S²T* induced by the one making e_0, …, e_4 orthonormal; it
does not depend on the choice of e_3, e_4 in V_⊥, so it is defined near Γ_(b_0), stationary and homogeneous of degree
0, and the seven pieces are orthogonal for it. R is skew for it. For η ∈ (0, 1] let
h_Γ := Σ_P η^(−2W(P)) ⟨·_P, ·_P⟩_0, the sum over the pieces P. In an h_Γ-orthonormal basis a map lowering W by j ≥ 1
has its entries multiplied by η^j, so D_− is O(η), while D_0 is unchanged; h_Γ is constant in the frame, so H_G, which
acts componentwise and preserves the symplectic volume, is skew. By [[eq:iii-f-4-2]] and [[eq:i-b-6-0]] (the inner
product is constant in the frame, as in [[lem:iii-d-5-2]]), p_1^Γ = −½((A + ϰR) + (A + ϰR)*) = −½(D_0 + D_0*) + O(η),
and −½(D_0 + D_0*) ≤ 0, the scalars being ≥ 0 and ϰR skew. So λ_max(p_1^Γ) ≤ Cη on Γ_(b_0), with C independent of η
(γ, c_μ and ϰ are bounded near the compact Γ_(b_0)); take η with Cη < ϵ/2. As in [Hin26], this is for fixed
modification parameters. The density: [[eq:iii-f-4-1]] is on half-densities by |dg|, and the adjoints of [[ch:s01]] are
for |dx| and dt_*; they agree at b_0, and near b_0 the change adds a scalar O(|b − b_0|) to p_1 ([[lem:iii-d-5-2]]).

*Near b_0.* Extend h_Γ to a stationary inner product near Γ_(b_0). p_1^Γ for 2L_b is built from the subprincipal
symbol of 2L_b and h_Γ, continuous in b uniformly near Γ_(b_0), and Γ_b → Γ_(b_0) by (Dyn); so
sup_(Γ_b) λ_max(p_1^Γ) < ϵ for b near b_0. ν_min and β_0 are continuous in b by (Dyn) and positive at b_0. ∎
