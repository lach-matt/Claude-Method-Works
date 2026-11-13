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
gauge-invariant roots −l and l + 2 (−l and l + 1 in dimension 3 + 1), with these removed, after the shifts: the roots
of the Killing forms of the gauge potential operator (the translations at scalar types 0 and 1, the rotations at
vector type 1) and the roots 2 (scalar types 0 and 1) and 3 (vector type 1) of the constraint propagation operator.
The proof ([[lem:iii-f1-2-1]]) compares L_b with the flat wave operator through the two identities that relate the
three operators, and computes nothing beyond the degrees of the Cartesian components of each type. The gap at zero energy
contains (0, 1]. The input [Hin26] takes from [AHW24, Theorem 6.1] on Kerr, mode stability and the classification of
stationary solutions of the linearised Einstein equation, has no five-dimensional counterpart; at b_0 it is proved here
from the Kodama–Ishibashi decomposition ([[thm:iii-f2-2-2]], [[thm:iii-f3-3-1]]), and near b_0 the kernel is counted
by an augmented operator. The kernel and the cokernel of the zero energy operator are eleven-dimensional (seven in
dimension 3 + 1): the mass, the six rotations of 𝔰𝔬(4) and the four translations. The mass change needs no logarithm.
Among the physical large zero energy states at the root −2 there is a tensor type state, which 𝕊² does not carry.

One result of the main argument enters as an input and is proved here: [[prop:np-10-34-iv]], the equivariance of the
linearised rotations of Minkowski space under rotations and the bracket form of 𝔰𝔬(4). The bound on the number
ε_ind of [[eq:iii-f1-2-2]] at the fixed gauge parameters is [[prop:np-10-52]] of [[ch:s14]].

The outside results used without proof are the reduction of the vacuum Einstein equations for each harmonic type to
a master equation [KI03], stated where it is used ([[thm:s15-ki]]) with its numbers and pages, and the subprincipal
operator of a tensor wave operator [Hin17, Proposition 4.1].
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

with □_g ġ := −g^(αβ) ġ_(;αβ) and R_g the curvature term of [[eq:iii-b-6-7]]: expand
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
and ℓ := dt̄ + d|x| (with X = −∂_(t̄) − ∂_r, dt_*(X) = 0, ℓ(X) = −2, ḡ⁻¹(ℓ, dt_*) = −2), and, by
[[eq:iii-b-6-5]], ḠĒ^C ω = γ_C(2c̄_C ⊗_s ω − e_C ḡ⟨c̄_C, ω⟩) with c̄_C/ρ = ½(1 − v_C)ℓ + ½(1 + v_C)dt_*. Then

    γ_C⁻¹ S̄^C ω = (1 − v_C)ω − ω(X) c̄_C/ρ + e_C⟨c̄_C/ρ, ω⟩ dt_*,

which is (1 − v_C)ω on angular ω, (1 − e_C)(1 − v_C)dt_* on dt_*, and 2(1 − v_C)ℓ + (1 + v_C)(1 − e_C)dt_* on ℓ.
With Ē^Υ Ḡ h = −γ_Υ(2ι_Y h − e_Υ c̄_Υ tr h), Y := ḡ⁻¹dt̄, c̄_Υ = ρ dt̄ ([[eq:iii-b-6-5]]),

    γ_Υ⁻¹ S̄^Υ ω = ω − ω(Y) dt_* + e_Υ ω(X) dt̄,

which is ω on angular ω, 2dt_* on dt_* (dt_*(Y) = −1), and (1 − e_Υ)(ℓ + dt_*) on ℓ. Both are triangular in the bases
(angular, dt_*, ℓ), with the diagonals of [[eq:iii-f-3-1]]. ∎

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

### The setting of the indicial analysis {#sec:iii-f1-1}

This section and the next two carry [Hin26, Sections 8.2–8.3] (pp. 149–153): the indicial roots of the zero energy
operator of L_b ([Hin26, Lemma 8.4] with (8.13)), the indicial solutions at ι = 0 ([Hin26, Lemma 8.5]),
tf-admissibility ([Hin26, Proposition 8.6]) and the inversion of the transition face normal operator on b-Sobolev
spaces ([Hin26, Corollary 8.7]).

L_b = D_(g_b)Ric + δ*_(g_b,E_C) δ_(g_b,E_Υ) G_(g_b) ([[eq:iii-f-1-1]]), and on Minkowski space its model L̄, with
2L̄ = □̄ + 2Ē^C δ̄ Ḡ + 2δ̄*_(Ē_C) Ē^Υ Ḡ; □̄^Υ := 2δ̄_(Ē_Υ) Ḡ δ̄* and □̄^C := 2δ̄ Ḡ δ̄*_(Ē_C) are the models of
[[ch:s13]] and [[ch:s14]]. With the trace weight 2/3,
Ē^Υ h = −γ_Υ(2ι_(c̄_Υ^♯) h − (2/3)(1 − e_Υ)c̄_Υ tr h), c̄_Υ = r⁻¹dt̄, and
Ē^C ω = γ_C(2c̄_C ⊗_s ω − (2/3)(1 − e_C)ḡ⟨c̄_C, ω⟩), c̄_C = r⁻¹(dt̄ − v_C dr) ([[eq:iii-b-6-5]],
[[thm:iii-e-1-1]]); so Ē^Υ Ḡ h = −γ_Υ(2ι_(c̄_Υ^♯) h − e_Υ c̄_Υ tr h). By [[lem:iii-f-2-1]] (3) the indicial roots of
L_b^(0) are those of L̄^(0), which is dilation homogeneous and equal to ρ² times its normal operator; likewise for □^Υ_b
([[lem:iii-d-2-1]] (3)) and □^C_b ([[sec:iii-e-1]]). All three models commute with the rotations SO(4) of the spatial
factor.

*Parameters.* e_Υ > 0 and γ_Υ > 0 are small, with z = 4e_Υγ_Υ² ∈ (0, ½], the parameter of [[lem:iii-d-4-1]]; v_C, e_C,
c_C and γ_C are those of [[thm:iii-e-1-1]], with C_0 = 100 ([[sec:iii-f-1]]). The constraint damping parameters are
fixed first ([[sec:iv4-0]]); γ_Υ is then taken small, as in [Hin26] ("keeping the other parameters and all 1-forms
fixed").

*The constraint propagation operator.* The facts about □^C_b used below are the clauses of [[thm:iii-e-1-1]] (3):

(C1) Every indicial root of □^C_b has real part ≥ 2 or < −C_0; the only one with real part 2 is ι = 2, a simple root
of scalar types 0 and 1. At scalar type 0 two roots lie on each side, written ι^C_(s0,≪,1), ι^C_(s0,≪,2) (real parts
< −C_0) and 2, ι^C_(s0,+); at scalar type 1 three, ι^C_(s1,≪,j) (j = 1, 2, 3) and 2, ι^C_(s1,+,1), ι^C_(s1,+,2); at
scalar type l ≥ 2 three, ι^C_(sl,≪,j) and ι^C_(sl,+,j); at vector type l ≥ 1 one, ι^C_(vl,≪) and ι^C_(vl,+).

(C2) The indicial roots of □^C_b are simple.

(C3) At scalar type l no indicial root of □^C_b lies in {1 − l, 3 − l, l + 3, l + 5} ∖ {2}; at vector type l ≥ 2 none
lies in {1 − l, 2 − l, l + 3, l + 4}.

(C4) Every indicial root of □^C_b whose real part is an integer in [3, 51] is real.

*Types and representations.* Write H_d for the space of harmonic polynomials of degree d on ℝ⁴, restricted to 𝕊³.
Under SO(4) ≅ (SU(2) × SU(2))/{±1}, H_d is the irreducible representation of highest weights (d/2, d/2); the
spatial covectors ℝ⁴ are (½, ½), and the symmetric 2-tensors on ℝ⁴ are (0, 0) ⊕ (1, 1), the trace and the trace-free
part. The scalar, vector and tensor harmonics of degree l are the representations of highest weights (l/2, l/2),
((l ± 1)/2, (l ∓ 1)/2) and ((l ± 2)/2, (l ∓ 2)/2) (as recalled in the proof of [[prop:iii-d2-3-1]]), whose two
weights are equal, differ by one and differ by two, and whose sum is l. So each irreducible representation π occurs
in exactly one type and degree. For a bundle W of Cartesian components (functions, 1-forms or symmetric 2-tensors of
ℝ^(1+4) in the frame dt̄, dx^i), let W_π be the π-isotypic subspace of C^∞(𝕊³; W). It is finite-dimensional and equal
to ℂ^k ⊗ π for the type and degree of π, with k the size of that type's indicial matrices ([[eq:iii-a1-2-9]]–
[[eq:iii-a1-2-10]]); an operator on 𝕊³ commuting with the action of SO(4) on the base and the components acts on W_π as
N ⊗ Id_π with N a k × k matrix (Schur's lemma).

### The indicial roots {#sec:iii-f1-2}

For a type and degree let N_L(ι), N_Υ(ι) and N_C(ι) be the type's indicial matrices of ρ⁻²(2L̄)^(0), ρ⁻²(□̄^Υ)^(0) and
ρ⁻²(□̄^C)^(0), in the bases of [[eq:iii-a1-2-9]]–[[eq:iii-a1-2-10]]: of sizes k = 4, 6, 7, 2, 3, 1 for N_L at s0, s1,
sl (l ≥ 2), v1, vl (l ≥ 2), tl (l ≥ 2), and m = 2, 3, 3, 1, 1 for N_Υ and N_C at s0, s1, sl, v1, vl. Each is −ι² Id
plus lower powers of ι, so its determinant has degree 2k, resp. 2m, and leading coefficient (−1)^k, resp. (−1)^m.

**Lemma {#lem:iii-f1-2-1}** (The factorisation.) For each type and degree,

    det N_L(ι) = (−1)^k (ι + l)(ι − l − 2) det N_Υ(ι − 1) det N_C(ι + 1) / D(ι),
    D(ι) = (ι − 1)² at s0 and s1,     D(ι) = ι(ι − 2) at v1,     D(ι) = 1 at sl and vl, l ≥ 2,           {#eq:iii-f1-2-1}

and at tensor type l ≥ 2, det N_L(ι) = −(ι + l)(ι − l − 2). This holds for all values of the parameters γ_Υ, e_Υ,
γ_C, e_C and v_C.

*Proof.* *Homogeneous sections.* A stationary section of W on ℝ^(1+4) ∖ {r = 0} is *homogeneous of degree −ι* if its
Cartesian components are r^(−ι) times functions on 𝕊³. On stationary sections a Cartesian derivative is a spatial
derivative ∂_(x^i), and c̄_Υ, c̄_C are homogeneous of degree −1. So each first-order operator below, δ̄*, δ̄*_(Ē_C),
δ̄Ḡ and δ̄_(Ē_Υ)Ḡ, maps sections homogeneous of degree −ι to sections homogeneous of degree −ι − 1, and each
second-order operator, 2D Ric (the linearisation at ḡ), 2L̄, □̄^Υ and □̄^C, to degree −ι − 2. Restricted to the type
of π these act by matrices, defined by T(r^(−ι)a) = r^(−ι−1)T(ι)a for a first-order T and P(r^(−ι)a) = r^(−ι−2)P(ι)a
for a second-order P; for P = 2L̄, □̄^Υ, □̄^C these are N_L, N_Υ, N_C, and a composition has
(T_1T_2)(ι) = T_1(ι + 1)T_2(ι). Write R(ι), B(ι), B′(ι), Ψ(ι), Φ(ι) for 2D Ric, δ̄*, δ̄*_(Ē_C), δ̄Ḡ, δ̄_(Ē_Υ)Ḡ: R is
k × k, B and B′ are k × m, Ψ and Φ are m × k.

*Five identities.* On Minkowski space, D Ric ∘ δ̄* = 0, since 2δ̄*X^♭ = ℒ_X ḡ and D Ric(ℒ_X ḡ) = ℒ_X Ric(ḡ) = 0; and
δ̄Ḡ ∘ D Ric = 0, the linearised second Bianchi identity at the Ricci-flat ḡ. With the definitions,

    N_L(ι) = R(ι) + 2B′(ι + 1)Φ(ι),     N_Υ(ι) = 2Φ(ι + 1)B(ι),     N_C(ι) = 2Ψ(ι + 1)B′(ι),
    R(ι + 1)B(ι) = 0,     Ψ(ι + 2)R(ι) = 0.

*A determinant identity.* Let C be a constant k × (k − m) matrix and C̃ a constant (k − m) × k matrix, and put
M_1(ι) := (B(ι − 1) | C) and M_2(ι) := (Ψ(ι + 2); C̃) (columns, resp. rows, juxtaposed). By the identities,
Ψ(ι + 2)N_L(ι)B(ι − 1) = 2Ψ(ι + 2)B′(ι + 1)Φ(ι)B(ι − 1) = ½N_C(ι + 1)N_Υ(ι − 1),
Ψ(ι + 2)N_L(ι)C = N_C(ι + 1)Φ(ι)C and C̃N_L(ι)B(ι − 1) = C̃B′(ι + 1)N_Υ(ι − 1), so

    M_2 N_L M_1 = ⎛ N_C  0 ⎞ ⎛ ½I     ΦC              ⎞ ⎛ N_Υ  0 ⎞
                  ⎝ 0    I ⎠ ⎝ C̃B′   C̃RC + 2C̃B′ΦC    ⎠ ⎝ 0    I ⎠

with the arguments ι + 1 of N_C and B′, ι − 1 of N_Υ, and ι of R and Φ. The middle factor has determinant
det(½I) det(C̃RC + 2C̃B′ΦC − C̃B′(½I)⁻¹ΦC) = 2^(−m) det(C̃RC). Hence, for every ι,

    det M_2(ι) · det N_L(ι) · det M_1(ι) = 2^(−m) det N_C(ι + 1) det N_Υ(ι − 1) det(C̃R(ι)C).

*The flat wave operator.* On Minkowski space 2δ̄Ḡδ̄* = □̄ on 1-forms (in general 2δGδ*ω = □ω − Ric(ω)), and on
stationary sections □̄ acts in the Cartesian frame as −Δ on each component, Δ the Laplacian of ℝ⁴. For Y ∈ H_d,
Δ(r^a Y) = r^(a−2)(a(a + 2) − d(d + 2))Y on ℝ⁴; with a = −ι,

    −Δ(r^(−ι) Y) = −r^(−ι−2)(ι + d)(ι − d − 2) Y.

−Δ preserves each H_d ⊗ W, so on the type of π its matrix is diagonal in a basis adapted to the degrees, with the entry
−(ι + d)(ι − d − 2) repeated n_d(π, W) times, n_d(π, W) the multiplicity of π in H_d ⊗ W. In particular 2Ψ(ι + 1)B(ι),
the matrix of □̄ on 1-forms, is invertible for ι ∉ ℤ, so B(ι) is injective and Ψ(ι + 1) is surjective for ι ∉ ℤ.

*The ratio does not depend on the parameters.* Fix ι_* ∉ ℤ, choose C whose columns complete those of B(ι_* − 1) to a
basis, and C̃ whose rows complete those of Ψ(ι_* + 2) to a basis. Then det M_1 and det M_2 are polynomials in ι, nonzero
at ι_*. R, B and Ψ, hence M_1, M_2 and det(C̃RC), do not involve γ_Υ, e_Υ, γ_C, e_C or v_C. det N_Υ(ι − 1) and
det N_C(ι + 1) have leading coefficient ±1, so they are not the zero polynomial. So the rational function

    det N_L(ι) / (det N_Υ(ι − 1) det N_C(ι + 1)) = 2^(−m) det(C̃R(ι)C) / (det M_1(ι) det M_2(ι))

is the same for all values of the parameters, and it suffices to compute it at γ_Υ = γ_C = 0.

*The flat case.* At γ_Υ = γ_C = 0, Ē^Υ = 0 and Ē^C = 0, so 2L̄ = 2D Ric + 2δ̄*δ̄Ḡ = □̄ on symmetric 2-tensors (as
2D Ric = □ − 2δ*δG + 2R with R = 0 at ḡ), and □̄^Υ = □̄^C = □̄ on 1-forms. The components are: for a symmetric
2-tensor, h_(t̄t̄) (a function, (0, 0)), h_(t̄i) (a spatial 1-form, (½, ½)) and h_(ij) ((0, 0) ⊕ (1, 1)); for a
1-form, ω_(t̄) ((0, 0)) and ω_i ((½, ½)). By the Clebsch–Gordan rule for SU(2) × SU(2), (d/2, d/2) ⊗ (j_1, j_2) is the
sum of the (a, b) with a ∈ {|d/2 − j_1|, …, d/2 + j_1} and b ∈ {|d/2 − j_2|, …, d/2 + j_2}. Reading off the degrees d
with n_d ≠ 0 (each then equal to 1, per summand):

- scalar type l, π = (l/2, l/2): from (0, 0), d = l; from (½, ½), d = l ± 1 (d ≥ 0); from (1, 1), d = l − 2, l, l + 2,
  except that d = l is absent at l = 0 and d = l − 2 needs l ≥ 2. So the 2-tensor degrees are l; l − 1, l + 1;
  l, l − 2, l, l + 2 at sl, l ≥ 2 (k = 7); 1; 0, 2; 1, 1, 3 at s1 (k = 6); 0; 1; 0, 2 at s0 (k = 4); and the 1-form
  degrees are l; l − 1, l + 1 at sl (m = 3), 1; 0, 2 at s1 (m = 3) and 0; 1 at s0 (m = 2);
- vector type l, π = ((l + 1)/2, (l − 1)/2) or its mirror: from (½, ½), d = l; from (1, 1), d = l − 1 (needs l ≥ 2)
  and d = l + 1. So the 2-tensor degrees are l; l − 1, l + 1 at vl, l ≥ 2 (k = 3), and 1; 2 at v1 (k = 2), and the
  1-form degree is l (m = 1);
- tensor type l, π = ((l + 2)/2, (l − 2)/2) or its mirror: only from (1, 1), d = l (k = 1, m = 0).

These sizes are those of [[eq:iii-a1-2-9]]–[[eq:iii-a1-2-10]]. Write a_j := ι + j and b_j := ι − j − 2, so that
(ι + d)(ι − d − 2) = a_d b_d, while the same expression at ι + 1 is a_(d+1) b_(d−1) and at ι − 1 is a_(d−1) b_(d+1).
At the flat point det N_L = (−1)^k Π a_d b_d over the 2-tensor degrees, and det N_Υ(ι − 1) det N_C(ι + 1)
= Π a_(d−1) b_(d+1) a_(d+1) b_(d−1) over the 1-form degrees (the signs (−1)^m of the two factors cancel). At sl the
numerator is −a_(l−2) a_(l−1) a_l³ a_(l+1) a_(l+2) b_(l−2) b_(l−1) b_l³ b_(l+1) b_(l+2) and the denominator is
a_(l−2) a_(l−1) a_l² a_(l+1) a_(l+2) b_(l−2) b_(l−1) b_l² b_(l+1) b_(l+2); the quotient is −a_l b_l. At s1 the
numerator is a_0 a_1³ a_2 a_3 b_0 b_1³ b_2 b_3 and the denominator a_(−1) a_0 a_1² a_2 a_3 b_(−1) b_0 b_1² b_2 b_3,
quotient a_1 b_1/(a_(−1) b_(−1)) = (ι + 1)(ι − 3)/(ι − 1)². At s0 the numerator is a_0² a_1 a_2 b_0² b_1 b_2 and the
denominator a_(−1) a_0 a_1 a_2 b_(−1) b_0 b_1 b_2, quotient ι(ι − 2)/(ι − 1)². At vl the quotient is
−a_(l−1) a_l a_(l+1) b_(l−1) b_l b_(l+1)/(a_(l−1) a_(l+1) b_(l−1) b_(l+1)) = −a_l b_l; at v1 it is
a_1 a_2 b_1 b_2/(a_0 a_2 b_0 b_2) = (ι + 1)(ι − 3)/(ι(ι − 2)); at tl, det N_L = −a_l b_l. In every case the quotient is
(−1)^k(ι + l)(ι − l − 2)/D(ι), which is [[eq:iii-f1-2-1]] at the flat point, and so for all parameters. ∎

The factors have this meaning. On Minkowski space L̄δ̄* = ½δ̄*_(Ē_C) □̄^Υ, so the symmetric gradient of an indicial
solution of □̄^Υ at ι − 1 is one of L̄ at ι, unless it vanishes, which happens exactly for the stationary homogeneous
Killing 1-forms: the translations (at ι − 1 = 0, scalar types 0 and 1) and the rotations (at ι − 1 = −1, vector type
1). The identity δ̄Ḡ(2L̄) = □̄^C δ̄_(Ē_Υ) Ḡ is the dual relation, which shifts the roots of □̄^C by −1. The factor
(ι + l)(ι − l − 2) carries the gauge-invariant roots −l and l + N − 2, N = 4, the degrees of the homogeneous harmonic
functions r^l Y and r^(−l−2) Y on ℝ⁴; and D removes the roots that the two relations give twice: the Killing root of
□̄^Υ and the root 2 of □̄^C at s0 and s1, and at v1 the rotations (ι − 1 = −1) and the root 3 of □̄^C (ι + 1 = 3,
[[lem:iii-f1-2-2]]).

**Lemma {#lem:iii-f1-2-2}** (Vector type 1 of □^C.) At vector type 1, N_C(ι) = −(ι − 3)(ι + 1 + 2γ_C v_C). So the roots
are 3 and −1 − 2γ_C v_C, for every value of the parameters.

*Proof.* A vector type 1 1-form of degree 0 is ρV, V = (Wx) · dx with W ∈ 𝔰𝔬(4): a Killing 1-form (δ̄*V = 0),
tangential and divergence free, with V(∂_r) = 0. For f = r^(−ι−1), ⟨c̄_C, V⟩ = 0 and tr(k ⊗_s V) = ⟨k, V⟩ = 0 for
k ∈ span(dt̄, dr), so δ̄*_(Ē_C)(fV) = (df + 2γ_C f c̄_C) ⊗_s V = (F_r dr + F_t dt̄) ⊗_s V, with
F_r = f′ − 2γ_C v_C f/r = −(ι + 1 + 2γ_C v_C) r^(−ι−2), and Ḡ is the identity on it. For a function F(r) one computes
in Cartesian coordinates δ̄(F dt̄ ⊗_s V) = 0 and δ̄(F dr ⊗_s V) = −½(F′ + 5F/r)V, from ∂_i(F x_i/r) = F′ + 3F/r,
(x_i/r)∂_i V_j = V_j/r, x · V = 0 and div V = tr W = 0. So □̄^C(fV) = −(F_r′ + 5F_r/r)V
= −(ι + 1 + 2γ_C v_C)(ι − 3) r^(−2) f V. ∎

**Proposition {#prop:iii-f1-2-3}** (The indicial roots; [Hin26, Lemma 8.4] in dimension 4 + 1.) Assume z ∈ (0, ½] and
(C1). The indicial roots of L_b^(0), in the notation of [[lem:iii-d-4-1]] and (C1), are:

s0: ι^C_(s0,≪,1) − 1, ι^C_(s0,≪,2) − 1, 2 − ι^Υ_(s0,2), 0; 2, 1 + ι^Υ_(s0,2), ι^C_(s0,+) − 1, 4;

s1: ι^C_(s1,≪,j) − 1 (j = 1, 2, 3), 2 − ι^Υ_(s1,3), 2 − ι^Υ_(s1,2), −1; 3, 1 + ι^Υ_(s1,2), 1 + ι^Υ_(s1,3), 5,
ι^C_(s1,+,1) − 1, ι^C_(s1,+,2) − 1;

sl, l ≥ 2: ι^C_(sl,≪,j) − 1 (j = 1, 2, 3), −l, 2 − ι^Υ_(sl,l+2), 2 − ι^Υ_(sl,l+1), 2 − l; l + 2,
1 + ι^Υ_(sl,l+1), 1 + ι^Υ_(sl,l+2), l + 4, ι^C_(sl,+,j) − 1 (j = 1, 2, 3);

v1: −2 − 2γ_C v_C, −1; 3, 4;

vl, l ≥ 2: ι^C_(vl,≪) − 1, −l, 1 − l; l + 2, l + 3, ι^C_(vl,+) − 1;

tl, l ≥ 2: −l; l + 2.

(a) No root has real part in (0, 1]. (b) At each type and degree, k roots (with multiplicity) have real part ≤ 0 and k
have real part > 1: those before and after the semicolon. (c) 0 is a root only at scalar types 0 and 2, simple there,
with the indicial solutions of [[lem:iii-f1-2-5]]. (d) The roots with real part ≤ 0 that come from □^C, written with
superscript C, have real part < −C_0 − 1 = −101. (e) If (C2)–(C3) hold, there is a countable set Z_exc ⊂ (0, ½],
determined by the roots of □^C_b, such that for z ∉ Z_exc every root is simple. (f) If (C4) holds, then for every
R > 0 only finitely many roots have |ι| ≤ R, and no non-integer root with |ι| ≤ 50 has integer real part; so there is
ε_ind ∈ (0, 1] with

    d(Re ι, ℤ) ≥ ε_ind     for every non-integer root ι with |ι| ≤ 50,                                   {#eq:iii-f1-2-2}

which is [Hin26, (8.13)], and (0, ε_ind] ⊂ (0, 1] lies in the indicial gap. The number ε_ind is small: at the gauge
parameters (e_Υ, γ_Υ) = (1/100, 1/100) the roots 2 − ι^Υ_(sl,l+1), which approach the integers 1 − l as l grows,
force ε_ind ≤ δ_50, where 2 − ι^Υ_(s50,51) = −49 − δ_50 is a root of modulus below 50 at distance δ_50 from ℤ
([[prop:np-10-52]] (i), (iii)). The number δ_50 is a constant of [[ch:s14]], fixed by the gauge parameters alone
([[rem:s14-delta50]]), and its value is given by [[cor:s14-eps-ind-point]]. The gap (0, 1] of (a) is exact, and
ε_ind enters only through [[eq:iii-f1-2-2]], never as a number of order one.

*Proof.* *The list.* By [[lem:iii-f1-2-1]] the roots of each type are, with multiplicity, −l and l + 2, the roots of
□^Υ plus 1 and the roots of □^C minus 1, less the roots of D. [[lem:iii-d-4-1]] gives those of □^Υ: s0:
1 − ι^Υ_(s0,2), 0, ι^Υ_(s0,2), 3; sl (l ≥ 1): 1 − ι^Υ_(sl,l+2), 1 − ι^Υ_(sl,l+1), 1 − l, ι^Υ_(sl,l+1), ι^Υ_(sl,l+2),
l + 3; vl: −l, l + 2. (C1) and [[lem:iii-f1-2-2]] give those of □^C. At s0 and s1, (ι − 1)² divides the numerator of
[[eq:iii-f1-2-1]] exactly: ι = 1 is the simple root 0 of □^Υ plus 1 (at s0 the entry 0 of the list, at s1 the entry
1 − l), simple by [[lem:iii-d-4-1]], and the simple root 2 of □^C minus 1 (C1), and no other factor vanishes at 1
((ι + l)(ι − l − 2) does not, nor do the roots of either operator other than these two, by the bounds below). At v1,
ι(ι − 2) divides it exactly: 0 is the root −1 of □^Υ plus 1, and 2 is the root 3 of □^C minus 1
([[lem:iii-f1-2-2]]), each simple; and (ι + 1)(ι − 3), the other root 3 of □^Υ plus 1 and the other root
−1 − 2γ_C v_C of □^C minus 1 avoid 0 and 2. What remains is the list.

*Bounds.* By [[eq:iii-d-4-2]], for 0 < z ≤ ½: ι^Υ_(s0,2) ∈ (2, 2 + z/3] and ι^Υ_(sl,l+j) ∈ (l + j, l + j + ¼); so
2 − ι^Υ_(s0,2) ∈ [−z/3, 0), 2 − ι^Υ_(sl,l+j) ∈ (2 − l − j − ¼, 2 − l − j), 1 + ι^Υ_(s0,2) ∈ (3, 3 + z/3] and
1 + ι^Υ_(sl,l+j) ∈ (l + j + 1, l + j + 5/4). By (C1) the roots ι^C_(·,≪) − 1 have real part < −C_0 − 1 and the roots
ι^C_(·,+) − 1 real part > 1. *(a), (b), (d)* are read off: before the semicolon every real part is ≤ 0, after it every
real part is > 1 (the integers there are ≥ 2), and the counts are 4, 6, 7, 2, 3, 1. *(c)* Before the semicolon, 0
occurs only as the root 0 at s0 and as 2 − l at l = 2; every other entry there is < 0 (as z > 0,
2 − ι^Υ_(s0,2) < 0 and 2 − ι^Υ_(s1,2) < 0). So 0 is a simple root at s0 and at s2, and at no other type.

*(e) Simplicity.* Within the roots that do not come from □^C the entries of each type are distinct by the bounds: they
lie in pairwise disjoint intervals, for instance at sl,
−l − ¼ < 2 − ι^Υ_(sl,l+2) < −l < 1 − l − ¼ < 2 − ι^Υ_(sl,l+1) < 1 − l < 2 − l, and on the other side
l + 2 < 1 + ι^Υ_(sl,l+1) < l + 9/4 < l + 3 < 1 + ι^Υ_(sl,l+2) < l + 13/4 < l + 4 (at z = 0 the first and third pairs
would meet, which is why z > 0 is assumed). The roots from □^C are distinct among themselves by (C2), and at v1 the
four are distinct as γ_C v_C > 0. A root from □^C equals an integer entry of its type exactly when □^C has a root at
that integer plus 1: at scalar type l the integer entries are −l, 2 − l, l + 2, l + 4 (with 0, 2, 4 at s0 and −1, 3, 5
at s1), so these coincidences are the points of (C3) (the root 2 of □^C at s0 and s1 being the one D removes); at
vector type l ≥ 2 they are −l, 1 − l, l + 2, l + 3, and (C3) excludes them likewise. The remaining coincidences are
between a real root μ of □^C and ι^Υ + 2 or 3 − ι^Υ, for a root ι^Υ = ι^Υ_(s0,2) or ι^Υ_(sl,l+j) of the same type and
degree. Each ι^Υ is a strictly increasing function of z: ι^Υ_(s0,2) = ½ + (9/4 + z)^(1/2), and
ι^Υ_(sl,l+j) = ½ + (¼ + s_(l,j))^(1/2) with s_(l,1) < s_(l,2) the roots of
Q_l(s) = s² − (2 + 2κ + z)s + κ(κ + 1) + zκ ([[lem:iii-d-4-1]]), where Q_l(κ) = −κ < 0 puts κ strictly between the
two roots, so that ∂_z s_(l,j) = (s_(l,j) − κ)/∂_s Q_l(s_(l,j)) > 0 for both (numerator and denominator have the same
sign). The roots of □^C_b do not depend on z (its parameters are fixed first), and there are countably many of them, by
type and degree; so each coincidence happens at at most one z, and Z_exc, the set of those z, is countable.

*(f)* By [[lem:iii-f1-2-4]] below, with the strip |Re ι| ≤ R, only finitely many isotypic components carry roots with
|ι| ≤ R, each finitely many. The non-integer roots with |ι| ≤ 50 are those from □^Υ, which are real and lie in the
open intervals of the bounds above, so their real parts are not integers, and those ι^C_(·,+) − 1 that are not
integers (by (d) the roots ι^C_(·,≪) − 1 have |ι| > 101); a non-integer one with integer real part n, 2 ≤ n ≤ 50,
would make ι^C_(·,+) non-real with real part n + 1 ∈ [3, 51], against (C4). The minimum of d(Re ι, ℤ) over this finite
set is positive, and ε_ind is any number in (0, 1] not exceeding it. ∎

**Lemma {#lem:iii-f1-2-4}** (Roots in a strip, uniformly.) Let 𝒯 be a compact parameter space and
I_τ(ι) = −ι² + a_τ ι + Δ_(𝕊³) + V_τ + b_τ, τ ∈ 𝒯, indicial families of the form of [[lem:i-c-2-4]] on ℂ^N-valued
functions on 𝕊³ (the Cartesian frame of T* or S²T* of ℝ^(1+4)), with coefficients continuous in τ and commuting with
the action of SO(4) that rotates both the base and the Cartesian components. For an irreducible representation π let
W_π be the π-isotypic subspace, finite-dimensional, and d(π) the least d with W_π ∩ (H_d ⊗ ℂ^N) ≠ 0. Then for every
X > 0 there is d_0 such that for all τ ∈ 𝒯, all π with d(π) ≥ d_0 and all ι with |Re ι| ≤ X, I_τ(ι) is invertible on
W_π. On each W_π, det(I_τ(ι)|_(W_π)) is a polynomial of degree 2 dim W_π with leading coefficient (−1)^(dim W_π), so its
roots, with multiplicity, depend continuously on τ.

*Proof.* H_d ⊗ ℂ^N is invariant under the action (the rotation of components is by constant matrices), and
Δ = κ_d := d(d + 2) on it. The representation on ℂ^N has irreducible constituents of highest weights (a, b) with
a + b ≤ 2 (for S²(ℝ ⊕ ℝ⁴), ℝ⁴ = (½, ½)), and H_d = (d/2, d/2); by the Clebsch–Gordan rule for SU(2) × SU(2),
π = (j_1, j_2) occurs in H_d ⊗ ℂ^N only if |j_1 + j_2 − d| ≤ 2, so W_π ⊂ ⊕_(|d−d(π)|≤4) H_d ⊗ ℂ^N, a
finite-dimensional space preserved by I_τ(ι), on which κ_(d(π)) ≤ Δ ≤ κ_(d(π)+4). By [[lem:i-c-2-4]] (a), whose
constants depend on finitely many seminorms of the coefficients and so are uniform in τ, there is μ_0 with I_τ(ι)
invertible on all of H² for |Re ι| ≤ X, |Im ι| ≥ μ_0. For |ι| ≤ X + μ_0 and u ∈ W_π write I_τ(ι) = (1 + Δ) + R,
R := −1 − ι² + a_τ ι + V_τ + b_τ; then ‖Ru‖ ≤ C(‖u‖ + ‖u‖_(H¹)) ≤ C(1 + κ_(d(π)+4))^(1/2)‖u‖ and
‖(1 + Δ)u‖ ≥ (1 + κ_(d(π)))‖u‖, with C uniform in τ; as (1 + κ_(d+4))^(1/2)/(1 + κ_d) → 0, I_τ(ι)u ≠ 0 for u ≠ 0 once
d(π) ≥ d_0. The last statement: on W_π, I_τ(ι) = −ι² Id + ιA_τ + B_τ with matrices continuous in τ. ∎

By *Types and representations* in [[sec:iii-f1-1]], W_π is ℂ^k ⊗ π for the type and degree of π,
I(ι)|_(W_π) = N(ι) ⊗ Id_π, and det(I(ι)|_(W_π)) = det N(ι)^(dim π): the roots on W_π are those of the type, each with
multiplicity multiplied by dim π, and [[prop:iii-f1-2-3]] (b) holds on every W_π, with k dim π = dim W_π.

**Lemma {#lem:iii-f1-2-5}** (The indicial solutions at 0; [Hin26, Lemma 8.5] in dimension 4 + 1.)
ker N(L̄^(0), 0) ⊂ ker N(ρ⁻¹(δ̄_(Ē_Υ))^(0) Ḡ, 0). More precisely, at scalar type 0 the kernel is spanned by the
constant tensor

    h̄_s0 := −dt̄² + B_Υ dx²,     B_Υ := (2 − e_Υ)/(4e_Υ),                                               {#eq:iii-f1-2-3}

and at scalar type 2, for each S ∈ 𝒮_2, by h̄_s2(S) := δ̄*(ρ⁻¹w_S), w_S spanning ker N_s2((□̄^Υ)^(0), −1); both
satisfy δ̄_(Ē_Υ) Ḡ h̄ = 0 and L̄h̄ = 0 exactly.

*Proof.* By [[prop:iii-f1-2-3]] (c) the kernel is that of scalar types 0 and 2, one-dimensional for each S; so it
suffices that the stated tensors are nonzero, stationary, homogeneous of degree 0 and of the stated types, and satisfy
the two equations: for a stationary homogeneous h̄ of degree 0, L̄^(0) h̄ = ρ² N(·, 0) h̄, and likewise for the gauge
operator, both models being dilation homogeneous.

*Scalar type 0.* h̄_s0 = δ̄*Ω with Ω := d(−½t̄² + ½B_Υ r²), as δ̄*d is the Hessian. It is constant (so stationary and
homogeneous of degree 0), SO(4)-invariant, and nonzero. D Ric(δ̄*Ω) = 0 on Minkowski space. For the gauge condition,
δ̄Ḡh̄_s0 = 0 (constant coefficients), and with c̄_Υ^♯ = −r⁻¹∂_(t̄), ι_(c̄_Υ^♯) h̄_s0 = r⁻¹dt̄ and
tr h̄_s0 = 1 + 4B_Υ, so Ē^Υ Ḡ h̄_s0 = −γ_Υ r⁻¹dt̄ (2 − e_Υ(1 + 4B_Υ)), which is 0 exactly when 1 + 4B_Υ = 2/e_Υ, that
is [[eq:iii-f1-2-3]]. Then L̄h̄_s0 = D Ric h̄_s0 + δ̄*_(Ē_C)(δ̄_(Ē_Υ) Ḡ h̄_s0) = 0. (In the terms of [Hin26],
Ω = t̄ ω̄^(0)_s0 + W̄ with ω̄^(0)_s0 = −dt̄ Killing and W̄ = B_Υ r dr solving □̄^Υ W̄ = −[□̄^Υ, t̄] ω̄^(0)_s0; that −1
is not an s0 root of □^Υ for z > 0, [[lem:iii-d-4-1]], is what makes W̄ unique, and B_Υ → ∞ as e_Υ → 0, where
1 − ι^Υ_(s0,2) → −1.)

*Scalar type 2.* 1 − l = −1 is a simple root of □^Υ at scalar type 2 ([[lem:iii-d-4-1]]), so w_S exists and is unique
up to scaling, and Ω_S := ρ⁻¹w_S is stationary, homogeneous of degree 1 and annihilated by □̄^Υ. So
h̄_s2(S) = δ̄*Ω_S is stationary, homogeneous of degree 0, of scalar type 2, satisfies
δ̄_(Ē_Υ) Ḡ h̄_s2 = ½□̄^Υ Ω_S = 0 and L̄h̄_s2 = D Ric(δ̄*Ω_S) + δ̄*_(Ē_C)(0) = 0. It is nonzero: otherwise Ω_S would be a
stationary Killing 1-form homogeneous of degree 1, and those are the spatial rotations, of vector type 1. ∎

### tf-admissibility {#sec:iii-f1-3}

For an operator P̂ satisfying (H1)–(H2), [[eq:i-c-4-1]] defines N_tf(P̂, σ̂) from its data at ρ = 0 only: S_0, N(P⁽⁰⁾)
and H_0 ([[sec:i-c-4-1]]); and [[thm:i-c-4-3]] and [[def:i-c-5-1]] use only these data. For P̂ = (2L_b)^(·), S_0 = S̄ and
N(P⁽⁰⁾) is (2L̄)^(0) ([[lem:iii-f-2-1]] (2)–(3)); since 2L̄ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S̄) + (2L̄)^(0) exactly, with no
∂²_(t_*) term (dt_* is null), N_tf((2L_b)^(·), σ̂) is the spectral family (2L̄)^(σ̂) written in x̂ ([[eq:i-c-4-1]]–
[[eq:i-c-4-2]] with ς = 1). The same holds for □^C_b with its model □̄^C: the ∂_(t_*)-coefficient of □̄^C is
−2ρ(ρ∂_ρ − 3/2 − S̄^C) exactly (□̄ gives −2ρ(ρ∂_ρ − 3/2), and 2δ̄ḠĒ^C gives ρS̄^C as in [[lem:iii-f-3-1]]), and the
rest is stationary and dilation homogeneous. And it holds for the operators of [[lem:iii-f-2-1]] with the parameters
(γ_C, γ_Υ) replaced by (τγ_C, τγ_Υ), τ ∈ [0, 1], or by (0, γ_Υ), which satisfy (H1)–(H2) by the proof of
[[lem:iii-f-2-1]], which does not use the values of the parameters; at τ = 0 the model is □̄ on S²T*, componentwise in
the Cartesian frame. For all of them spec S̄ ⊂ [0, ∞) ([[eq:iii-f-3-1]], the γ's being ≥ 0), and spec S̄^C ⊂ (0, ∞)
([[sec:iii-e-1]]). Here P^(·) denotes the family σ ↦ P^(σ).

*Weights.* In [[thm:i-c-4-3]] the b-weight of 𝒳_(tf,θ) at ztf is q − 2, and the tf-admissible weight is β := 2 − q; for
brevity 𝒳(β), 𝒴(β) and ind(β) denote the spaces and the index of N_tf(e^(iθ)) : 𝒳_(tf,θ) → 𝒴_(tf,θ) at q = 2 − β (θ,
s, α_+ and the orders fixed, in the settings of [[thm:i-c-4-3]] (1)–(2)), defined when β is not the real part of an
indicial root. Near ztf, N_tf = r̂⁻²L, with L as at the end of [[sec:i-c-2-5]] at the end at 0 (ϱ = r̂), and Mellin
symbol J(ι) = I(−ι) ([[sec:i-c-4-1]] (c)); so a root μ of J is −μ_b, μ_b ∈ spec_b, and 𝒳(β) is H^s_(b,−β) there.

**Lemma {#lem:iii-f1-3-1}** (Relative index.) Let β_1 < β_2 < β_1 + 1, neither the real part of a point of spec_b,
and s ∈ ℤ. Then ind(β_2) − ind(β_1) = dim F, where F := ⊕_μ F_μ over the roots μ of J with −β_2 < Re μ < −β_1 and

    F_μ := {Res_(ι=μ)(ϱ^ι J(ι)⁻¹ g(ι)) : g holomorphic near μ, C^∞(𝕊³; ℂ^N)-valued}.                     {#eq:iii-f1-3-1}

dim F_μ is the sum over the finitely many W_π on which μ is a root of ord_μ det(J|_(W_π)), the algebraic
multiplicity; when J is an indicial family as in [[lem:iii-f1-2-4]], it is the multiplicity of −μ as a root of I on
those components.

*Proof.* Put c_i := −β_i, so c_2 < c_1 < c_2 + 1, 𝒳(β_1) ⊂ 𝒳(β_2) and 𝒴(β_1) ⊂ 𝒴(β_2), and write 𝒳_i, 𝒴_i,
N := N_tf(e^(iθ)), N_i := N|_(𝒳_i). Every Φ ∈ F_μ is a finite sum ϱ^μ Σ_j (log ϱ)^j a_j, a_j smooth, and
N(L)Φ = Res(ϱ^ι J(ι)J(ι)⁻¹g(ι)) = 0, as N(L)ϱ^ι a = ϱ^ι J(ι)a. Let χ ∈ C_c^∞([0, 1)) be a function of r̂ equal to 1 near
0.

*Step 1: the expansion.* Let 𝒵 := {w ∈ 𝒳_2 : Nw ∈ 𝒴_1} and w ∈ 𝒵. By [[lem:i-c-2-5]], v := χw ∈ H^s_(b,c_2), and
f := N(L)v = χr̂²Nw + [L, χ]w − (L − N(L))χw lies in H^(s−2)_(b,c_1): the first term as Nw ∈ 𝒴_1, whose weight at ztf is
c_1 − 2; the second has compact support in tf°; the third as L − N(L) ∈ ϱDiff²_b maps H^s_(b,c_2) to
H^(s−2)_(b,c_2+1) ⊂ H^(s−2)_(b,c_1). So ℳf is holomorphic on {Re ι < c_1} with the line bounds [[eq:i-c-2-1]] up to
Re ι = c_1, and Jℳv = ℳf on {Re ι < c_2}. Hence J⁻¹ℳf continues ℳv meromorphically to {Re ι < c_1}, with poles only at
roots μ with c_2 < Re μ < c_1 (none on Re ι = c_2, by hypothesis), finitely many by [[lem:i-c-2-4]] (b). Let
Φ := −Σ_μ Res_(ι=μ)(ϱ^ι J(ι)⁻¹ℳf(ι)) ∈ F. As ℳ(χϱ^μ(log ϱ)^j a) continues meromorphically with a single pole, at μ, of
principal part −j!(ι − μ)^(−j−1)a (differentiate ∫_0^(ϱ_0) ϱ^(μ−ι−1)dϱ = ϱ_0^(μ−ι)/(μ − ι) j times in μ), and
Res_(ι=μ)(ϱ^ι(ι − μ)^(−j−1)a) = ϱ^μ(log ϱ)^j a/j!, the transform of χ Res(ϱ^ι q) has principal part −q at μ for every
principal part q; so ℳ(v − χΦ) = J⁻¹ℳf − ℳ(χΦ) is holomorphic on {Re ι < c_1}. Its L² norms on the lines Re ι = x,
c_2 − ϵ ≤ x < c_1, are bounded uniformly: for |Im ι| ≥ μ_0 by [[lem:i-c-2-4]] (a) and [[eq:i-c-2-1]], with ℳ(χΦ) minus
its principal parts rapidly decreasing there; on the remaining compact set by holomorphy. [[lem:i-c-2-3]] gives
v − χΦ ∈ H⁰_(b,c_1); and L(v − χΦ) ∈ H^(s−2)_(b,c_1) near ztf, because L(χΦ) = [N(L), χ]Φ + (L − N(L))χΦ with
Re μ + 1 > c_2 + 1 > c_1; so [[lem:i-c-2-5]] at the weight c_1 gives w − χΦ ∈ H^s_(b,c_1) near ztf. Away from ztf,
w − χΦ and w agree near sctf and are smooth in between, and N(χΦ) ∈ 𝒴_1 by the same argument; so w − χΦ ∈ 𝒳_1. If
χΦ ∈ 𝒳_1 for some Φ ∈ F, then ℳ(χΦ) is holomorphic on {Re ι < c_1}, so its principal parts vanish and Φ = 0 (the
functions ϱ^μ(log ϱ)^j a with distinct (μ, j) are independent). So 𝒵 = 𝒳_1 ⊕ χF, with χF ⊂ 𝒵 by the same
argument.

*Step 2: the target.* 𝒴_2 = 𝒴_1 + N(𝒳_2). Let y ∈ 𝒴_2, χ′ a cut-off with χ′χ = χ, and f := χ′r̂²y ∈ H^(s−2)_(b,c_2).
Define u on all of (0, ∞) × 𝕊³ by ℳu := J⁻¹ℳf on the line Re ι = c_2; by Plancherel in t = −log ϱ (as in
[[eq:i-c-2-2]], s being an integer) and [[lem:i-c-2-4]] (c), e^(c_2 t)u ∈ H^s and N(L)u = f, so χu ∈ H^s_(b,c_2). Then
y − N(χu) = (1 − χ)y − r̂⁻²[N(L), χ]u − r̂⁻²(L − N(L))χu: the first term vanishes near ztf, where alone 𝒴_1 and 𝒴_2
differ; the second has compact support in tf°; the third lies in r̂⁻²H^(s−2)_(b,c_2+1) ⊂ H^(s−2)_(b,c_1−2) near ztf. So
y − N(χu) ∈ 𝒴_1, and χu ∈ 𝒳_2.

*Step 3: the indices.* N_2 and N_1 are Fredholm ([[thm:i-c-4-3]] (3)). ker N_2 = ker(N|_𝒵), as kernel elements lie in
𝒵. The map 𝒴_1/N(𝒵) → 𝒴_2/N(𝒳_2) is injective (if y = Nw with w ∈ 𝒳_2 and y ∈ 𝒴_1, then w ∈ 𝒵) and surjective by
Step 2. So N|_𝒵 : 𝒵 → 𝒴_1, with 𝒵 normed as 𝒳_1 ⊕ χF, is Fredholm with the index of N_2; and it is N_1 extended by the
finite-dimensional space χF, so its index is ind N_1 + dim F. *Multiplicity.* By [[lem:iii-f1-2-4]] and the
discreteness of [[lem:i-c-2-4]] (b), μ is a root on finitely many W_π, and J⁻¹g splits accordingly. On a
finite-dimensional block, the ring of germs of holomorphic functions at μ being a principal ideal domain,
J = E diag((ι − μ)^(k_i)) F′ with E, F′ holomorphic and invertible near μ (Smith form) and Σ_i k_i = ord_μ det J. As g
ranges over holomorphic germs so does E⁻¹g; the principal parts of diag((ι − μ)^(−k_i))h form a space of dimension
Σ k_i; multiplication by F′⁻¹ is a bijection of principal-part spaces (with inverse multiplication by F′); and
q ↦ Res(ϱ^ι q) is injective on principal parts, as Res(ϱ^ι(ι − μ)^(−j−1)a) = ϱ^μ(log ϱ)^j a/j!. So dim F_μ = Σ k_i. ∎

**Lemma {#lem:iii-f1-3-2}** (Common orders.) Let P̂_1, …, P̂_k satisfy (H1)–(H2) with principal symbols positive
multiples of one another, and let α_+ ∈ ℝ. There are orders 𝗋_± admissible with weight α_+ for every σ_0 ∈ J_±, in the
sense of [[sec:i-c-4-3]], for all of them at once; for a family continuous in a parameter in a compact set, the same
holds uniformly.

*Proof.* The characteristic set at the boundary face, the radial sets and the direction of the flow depend only on the
principal symbol, up to positive multiples ([[sec:i-a-4]]). Take 𝗋_in above the largest of the incoming thresholds
½(−1 + ϑ^(i)_in) − α_+ (bounded over a compact parameter set, as they depend continuously on the coefficients) and
𝗋_out below the smallest of −½ + S̄^(i) − α_+, with 𝗋_in ≥ 𝗋_out; [[lem:i-a-7-1]] gives an order pair with these values,
which satisfies (O1)–(O3) of [[sec:i-a-1]] for each operator. On compact subsets of (0, π) the constant order 𝗋_out is
allowed for each ([[thm:i-c-4-3]] (2)). ∎

**Proposition {#prop:iii-f1-3-3}** (tf-admissibility; [Hin26, Proposition 8.6] in dimension 4 + 1.) Assume e_Υ > 0
and (C1), and fix all parameters but γ_Υ. There is γ_1 > 0 such that for γ_Υ ∈ (0, γ_1) (so that
z = 4e_Υγ_Υ² ∈ (0, ½]) and every b near b_0, L_b^(·) is tf-admissible ([[def:i-c-5-1]]) with every weight β ∈ (0, 1].

*Proof.* (i) of [[def:i-c-5-1]]: (0, 1] lies in an indicial gap, by [[prop:iii-f1-2-3]] (a), and the gap contains
(0, β_+) with β_+ > 1. As N_tf depends only on the model, b plays no role. Fix α_+, s ∈ ℤ large, and by
[[lem:iii-f1-3-2]] orders admissible at once for (2L_b)^(·), (□^C_b)^(·), the operator P̂′ with parameters (0, γ_Υ), and
the operators P̂_τ with parameters (τγ_C, τγ_Υ), uniformly for γ_Υ ∈ [0, 1] and τ ∈ [0, 1]; by [[thm:i-c-4-3]] (3)
kernels, annihilators and indices do not depend on these choices or on q with 2 − q in the gap.

*(ii) The kernel.* Let θ ∈ [0, π], σ̂ := e^(iθ), β ∈ (0, ½) (by [[thm:i-c-4-3]] (3) this covers every weight in the
gap), and u_0 ∈ 𝒳(β) with N_tf((2L_b)^(·), σ̂)u_0 = 0.

*Step 1.* By [[thm:i-c-4-3]] (5), with the gap (0, β_+), u_0 ∈ ρ_ztf^(−β′)C^∞_b near ztf for every β′ > 0; and
(2L̄)^(σ̂)u_0 = 0 on ℝ⁴ ∖ 0 (the description above).

*Step 2: the gauge 1-form.* The linearised second Bianchi identity on Minkowski space, δ̄Ḡ D Ric = 0, gives
δ̄Ḡ(2L̄) = 2δ̄Ḡδ̄*_(Ē_C)δ̄_(Ē_Υ)Ḡ = □̄^C δ̄_(Ē_Υ)Ḡ; the operators are stationary, so their spectral families compose,
and η_0 := (δ̄_(Ē_Υ)Ḡ)^(σ̂)u_0 satisfies (□̄^C)^(σ̂)η_0 = (δ̄Ḡ)^(σ̂)(2L̄)^(σ̂)u_0 = 0, that is,
N_tf((□^C_b)^(·), σ̂)η_0 = 0.

*Step 3: η_0 ∈ 𝒳_(□^C)(β_C), β_C := 1 + 2β ∈ (1, 2).* (δ̄_(Ē_Υ)Ḡ)^(σ̂) = ρ̂A_1 + σ̂A_0 with
A_1 := ρ⁻¹(δ̄_(Ē_Υ))^(0)Ḡ ∈ Diff¹_b and A_0 a bundle map, both homogeneous of degree 0. Near ztf, ρ̂ = r̂⁻¹, so
η_0 ∈ ρ_ztf^(−1−β′)C^∞_b for every β′ > 0, hence η_0 ∈ H^∞_(b,−1−2β) there ([[lem:i-c-2-2]] (f)), which is the ztf part
of 𝒳(β_C). Near sctf, ρ̂A_1 ∈ Diff¹_sc and A_0 has order (0, 0), so η_0 ∈ H_sc^(s−1,𝗋+α_+) there, with the common
orders; in between η_0 is smooth. With N_tf η_0 = 0, η_0 ∈ 𝒳_(tf,θ) for (□^C_b)^(·) at the regularity s − 1 and the
weight β_C, which lies in the gap (−C_0, 2) of □^C_b (C1).

*Step 4.* By [[thm:iii-e-1-1]] (4), (□^C_b)^(·) is tf-admissible with the weight β_C ∈ [−C_0, 2), so η_0 = 0.

*Step 5: the unmodified gauge.* With η_0 = 0, (2L̄)^(σ̂)u_0 = 2(D Ric)^(σ̂)u_0 = (2L̄′)^(σ̂)u_0,
L̄′ := D Ric + δ̄*δ̄_(Ē_Υ)Ḡ, the model of P̂′ (parameters (0, γ_Υ)). So N_tf(P̂′, σ̂)u_0 = 0.
2L̄′ = □̄ + 2δ̄*Ē^ΥḠ does not involve γ_C.

*Step 6: small γ_Υ.* u_0 ∈ 𝒳_(P̂′)(1): near ztf u_0 ∈ H^s_(b,−1), as u_0 = O(r̂^(−β′)) with b-regularity and β′ < 1;
near sctf it is as before. At γ_Υ = 0, P̂′ = □^(·) on S²T*, componentwise in the Cartesian frame, tf-admissible with
every weight in (0, 2) ([[prop:i-c-5-3]]), so by [[cor:i-c-5-2]] (b) at the weight 1, uniformly in θ over the three
sectors, ‖w‖ ≤ C‖N⁰_tf w‖. The difference N_tf(P̂′, e^(iθ)) − N⁰_tf(e^(iθ)) = −2ie^(iθ)ρ̂S̄′ + ρ̂²M′, with S̄′ and
M′ ∈ Diff¹_b homogeneous and O(γ_Υ), is bounded from the space of 𝒳 into that of 𝒴 with norm C′γ_Υ, uniformly in θ,
exactly as in [[lem:iii-d-7-1]]; so ‖u_0‖ ≤ C‖N_tf(P̂′, e^(iθ))u_0‖ + CC′γ_Υ‖u_0‖, and u_0 = 0 once CC′γ_Υ ≤ ½. This
fixes γ_1; it depends on the orders, hence on γ_C, which is fixed first. The weight 1 lies in the indicial gap of
P̂′(0) for small γ_Υ: its roots are within O(γ_Υ) of the integer roots of □̄ on S²T* ([[lem:iii-a1-2-3]]), none in
(0, 2), on the finitely many components that meet the strip |Re ι − 1| ≤ ½ ([[lem:iii-f1-2-4]]), and on no other.

*(iii) The adjoint.* By [[thm:i-c-4-3]] (3) the annihilator of the range of
N_tf((2L_b)^(·), 1) : 𝒳(β) → 𝒴(β) is ker_(𝒳*) N_tf(1)^(*h); by (ii) the operator is injective, so it suffices that its
index is 0. Consider the family P̂_τ, τ ∈ [0, 1], at θ = 0 with the common orders. P̂_1 = (2L_b)^(·) and P̂_0 = □^(·) on
S²T*. 𝒳 does not depend on τ, and τ ↦ N_tf(P̂_τ, 1) is continuous in the norm of bounded maps 𝒳 → 𝒴 (the differences are
as in Step 6). Let I_τ be the indicial family of P̂_τ(0), apply [[lem:iii-f1-2-4]] with X := 2 and 𝒯 = [0, 1], and for β″
not the real part of a root of I_τ, |β″ − β| < 1, put

    G(τ) := ind_τ(β″) − Σ_π (n_π(τ, β″) − dim W_π),

n_π(τ, β″) the number of roots of I_τ on W_π with real part < β″, with multiplicity. The sum is finite: for d(π) ≥ d_0
no root on W_π has |Re ι| ≤ 2 for any τ, so by continuity n_π(τ, β″) is its value at τ = 0, where the roots on W_π are
those of □̄, dim W_π of them ≤ 0 and dim W_π of them ≥ 2 ([[lem:iii-a1-2-3]]: −d and d + 2), so the term is 0. G does
not depend on β″: by [[lem:iii-f1-3-1]] (through intermediate weights, finitely many roots lying between),
ind_τ(β_2) − ind_τ(β_1) is the number of roots with real part in (β_1, β_2), which is the change of the sum. G is
locally constant: near τ_0 choose β″ that no root of the finitely many components meeting the strip has as real part
for τ near τ_0 (the roots move continuously); then ind_τ(β″) is locally constant (a norm-continuous family of Fredholm
operators on fixed spaces) and so is the sum. So G(1) = G(0). At τ = 0 and β″ = β, ind = 0 (□^(0) is invertible,
[[prop:i-c-5-3]] and [[cor:i-c-5-2]] (a)) and the sum is 0 (the roots of □̄ split evenly about (0, 2)). At τ = 1 and
β″ = β the sum is 0 by [[prop:iii-f1-2-3]] (b) on every W_π (no root has real part in (0, 1], so n_π(1, β) counts the
roots with real part ≤ 0, dim W_π of them). Hence ind_1(β) = 0. ∎

As in [Hin26], the quantitative estimates of [[cor:i-c-5-2]] now hold for N_tf(L_b^(·), σ̂). On b-Sobolev spaces they
read:

**Corollary {#cor:iii-f1-3-4}** (The inverse of the transition face normal operator; [Hin26, Corollary 8.7] in
dimension 4 + 1.) On tf use the b-density |dr̂/r̂ dg̸| and H^(k,a,c)_b(tf) := ρ_sctf^a ρ_ztf^c H^k_b(tf). Fix

    β_sctf < 3/2 = 3/2 + min Re spec S̄,     β_ztf ∈ [−1, 0).                                            {#eq:iii-f1-3-2}

Then there is ℓ ∈ ℕ_0 such that for all k ∈ ℕ_0 and ϵ > 0

    N_tf(L_b^(·), ±1)⁻¹ : H_b^(k+ℓ, β_sctf+1, β_ztf−2)(tf) → H_b^(k, β_sctf−ϵ, β_ztf)(tf) is bounded.    {#eq:iii-f1-3-3}

*Proof.* *The threshold at R_out.* [[sec:i-a-1]] asks 𝗋 + α_+ < −½ + S̄_L there,
S̄_L := ½ inf_(∂X) λ_min(S̄ + S̄^(*h)) for a fibre inner product h of our choice ([[prop:i-a-4-9]]). For every δ > 0 some
smooth h gives S̄_L ≥ −δ, as min Re spec S̄ = 0 ([[eq:iii-f-3-1]]): at each ω, a Jordan basis of S̄(ω) rescaled so that
the off-diagonal entries are at most δ/2 defines h_ω with Re h_ω((S̄ + δ)u, u) ≥ (δ/2)h_ω(u, u), a strict inequality,
which persists for S̄(ω′), ω′ near ω; the condition is convex in h, so a partition of unity on 𝕊³ glues these. *The
orders.* Take β := −β_ztf ∈ (0, 1], q := 2 − β, α_+ := 0, δ := ¼(3/2 − β_sctf), ϵ < δ (it suffices to prove
[[eq:iii-f1-3-3]] for small ϵ), 𝗋_out := β_sctf − 2 − ϵ/2 < −½ − δ, and the orders 𝗋_± of [[lem:i-a-7-1]] at
σ_* = ±1 with that outgoing value, constant near R_out. By [[prop:iii-f1-3-3]] and [[cor:i-c-5-2]] (a)–(b), with
[[thm:i-c-4-3]] (4) for k further b-derivatives, N_tf(±1)⁻¹ is bounded from H^((s−2;k),(𝗋+1,q−2))_(sc,b;b) to
H^((s;k),(𝗋,q))_(sc,b;b). Near ztf these are H^(s−2+k)_(b,β_ztf−2) and H^(s+k)_(b,β_ztf) for the b-density
([[def:i-c-4-1]]). Near sctf, on the end of ℝ⁴_(x̂), [[lem:ii-g1-4-1]] ((4.1a)–(4.1b) there, on ℝ⁴ without the
artificial boundary) gives H_b^(k+ℓ,β_sctf+1) ↪ H^((s−1;k),𝗋+1) and H^((s;k),𝗋) ↪ H_b^(k−ℓ̃,β_sctf−ϵ) with the losses
ℓ, ℓ̃ of that lemma (𝗋_out + 3 + ϵ/2 = β_sctf + 1 and 𝗋_out + 2 − ϵ/2 = β_sctf − ϵ). Replacing k by k + ℓ̃ and enlarging
ℓ gives [[eq:iii-f1-3-3]], with ℓ independent of ϵ as in [[cor:ii-g1-4-2]]. ∎

### The horizon threshold and the hypotheses of the spectral theory {#sec:iii-f2-1}

This section and the next four carry [Hin26, Proposition 8.8] (p. 153), mode stability of L_b at the nonzero
frequencies of the closed upper half plane: at b_0 for every such frequency, and for b near b_0 for the frequencies
bounded away from zero. [Hin26] takes its input from [AHW24, Theorem 6.1 (1)], mode stability of the linearised Einstein
equation on Kerr, which has no five-dimensional counterpart; at b_0 it is proved here from the Kodama–Ishibashi
decomposition, with the gauge 1-form built by an ordinary differential equation in the radial direction and continued
inside the horizon as a solution. We write P′ := D_(g_b)Ric + δ*_(g_b) δ_(g_b,E_Υ) G_(g_b) for the operator without
the constraint damping modification. First we supply the threshold of L_b at the event horizon, by which the theory of
[[ch:s01]]–[[ch:s02]] applies to L_b.

**Lemma {#lem:iii-f2-1-1}** (The horizon threshold; [Hin26, footnote 78] in dimension 4 + 1.) On Tangherlini, in the
ingoing chart (v, r, ω), let c_C = a_v dv + a_r dr and c_(Υ,H) = c_v dv + c_r dr at r_h, and put x := a_v γ_C r_h,
y := c_v γ_(Υ,H) r_h. At N*ℋ, ζ = ξ dr, the subprincipal symbol of 2L_(b_0) on half-densities by |dg| is iξf′(r_h)K with

    det(ν − K) = ν⁵ (ν − 1 + x)³ (ν − 2 + 2x)(ν + (1 − e_C)x) (ν − y)(ν + 1 − y)³(ν + 2 − 2y).           {#eq:iii-f2-1-1}

So the threshold quantity ϑ_ℋ of [[sec:i-a-1]], in a suitable fibre inner product, is any number above
ϑ_L := max{0, 1 − x, 2 − 2x, −(1 − e_C)x, y, y − 1, 2y − 2}, and the regularity condition is s > ½ + ϑ_L. With the
choice c_(Υ,H) = −½χ dr of [[sec:iii-d1-1]] (y = 0), x = a_v γ_C r_h > 0, and e_C ∈ (0, 1) makes −(1 − e_C)x < 0; so
ϑ_L = max(0, 2 − 2x): it is 0 when a_v γ_C r_h ≥ 1, and below 2 always; 2, the threshold s > 5/2 of [Hin26, footnote
78], is its value without the damping (γ_C = 0). For every δ > 0 there is a neighbourhood of b_0 (and of the
modification parameters, in a compact set) on which ϑ_ℋ < ϑ_L + δ in a fixed fibre inner product.

*Proof.* *The terms.* Only the first-order part of 2L_(b_0) = □ + 2E^C δG + 2δ*_(E_C) E^Υ G + 2R ([[eq:iii-f-1-2]])
enters a subprincipal symbol beyond the principal part: 2E^C δG and 2δ*E^Υ G; the terms 2E^C E^Υ G and 2R are of order
zero. Near the horizon E^Υ is its horizon part, with E^Υ_H G h = 2γ_(Υ,H) ι_(g⁻¹c_(Υ,H)) h ([[eq:iii-b-6-5]]), and only
the values of c_C and c_(Υ,H) at r_h enter, as they multiply first derivatives. In the ingoing chart
g_(b_0) = −f dv² + 2dv dr + r²γ, g⁻¹ has g^vv = 0, g^vr = 1, g^rr = f, so at r_h, g⁻¹dr = ∂_v and g⁻¹dv = ∂_r, and
f′(r_h) = 2/r_h.

*The wave operator.* S_sub(□) = −i∇^(π*S²T*)_(H_G) on half-densities by |dg| ([[eq:iii-f-4-1]]), and at N*ℋ,
H_G = 2ξ∂_v plus a fibre term, which acts trivially on fibre-constant sections. At r_h the Christoffel symbols with a
lower index v are Γ^v_vv = f′/2, Γ^r_vr = −f′/2 and zero otherwise (Γ^r_vv = ff′/2 vanishes there), so
∇_(∂_v) dv = −(f′/2)dv, ∇_(∂_v) dr = (f′/2)dr and ∇_(∂_v) e = 0 for the angular covectors e = r ê, ê of unit length for
γ. So on 1-forms −i∇_(H_G) = iξf′(r_h)K_0 with K_0 = 1 on dv, −1 on dr and 0 on the angular covectors (the matrix of
[[lem:iii-d-5-1]] at γ_(Υ,H) = 0), and on symmetric 2-tensors K_0 is its Leibniz extension.

*The modifications.* With σ_1(δ)(ζ)h = −iι_(g⁻¹ζ)h and σ_1(δ*)(ζ)ω = iζ ⊗_s ω, the principal symbol at ζ = ξ dr of
2E^C δG + 2δ*E^Υ G is iξ(−2E^C ι_(∂_v) G + 2dr ⊗_s E^Υ G). So K = K_0 + K_C + K_Υ with

    K_C h = −r_h γ_C (2c_C ⊗_s ι_(∂_v)Gh − (2/3)(1 − e_C) g ⟨c_C, ι_(∂_v)Gh⟩),
    K_Υ h = 2r_h γ_(Υ,H) dr ⊗_s ι_(c_v∂_r + c_r∂_v) h.

*A grading.* Give dv, dr and the angular covectors the weights 1, −1, 0, and a symmetric product of two the sum. K_0
multiplies a monomial by its weight. ι_(∂_v) removes a factor dv, lowering the weight by 1, and ι_(∂_r) removes a factor
dr, raising it by 1; at r_h, g = 2dv dr + T with T := Σ_a e_a² (e_1, e_2, e_3 an orthonormal angular coframe) has weight
0, tr picks the pairs (dv, dr) and (e_a, e_a), so G preserves the weight; ⟨dv, ·⟩ picks the dr-component and ⟨dr, ·⟩ the
dv-component. Hence the a_v-part of K_C and the c_v-part of K_Υ preserve the weight, and the a_r-part of K_C and the
c_r-part of K_Υ lower it by 2. So K is block triangular for the grading, and det(ν − K) is the product of the
characteristic polynomials of the weight-preserving part D_0 on the five weight spaces. With x = a_v γ_C r_h and
y = c_v γ_(Υ,H) r_h:

- weight 2, dv²: Gdv² = dv² (tr dv² = g^vv = 0), ι_(∂_v)dv² = dv and ⟨dv, dv⟩ = 0, so D_0 dv² = (2 − 2x)dv²;
- weight 1, dv e_a: G is the identity there, ι_(∂_v)(dv e_a) = ½e_a, ⟨dv, e_a⟩ = 0 and ι_(∂_r)(dv e_a) = 0, so
  D_0 = 1 − x, three times;
- weight 0, spanned by dv dr, T and the five trace-free angular monomials: K_0 = 0 there. G(dv dr) = dv dr − ½g = −½T
  and ι_(∂_v)T = 0, so K_C(dv dr) = 0; GT = T − (3/2)g = −½T − 3dv dr, ι_(∂_v)GT = −(3/2)dr and ⟨dv, dr⟩ = 1, so
  K_C T = −x(−3dv dr + (1 − e_C)g) = x(1 + 2e_C)dv dr − x(1 − e_C)T; K_C vanishes on the trace-free angular part; and
  ι_(∂_r)(dv dr) = ½dv, ι_(∂_r)T = 0, so K_Υ(dv dr) = y dv dr and K_Υ vanishes on T and on the trace-free angular part.
  So D_0 is triangular there, with eigenvalues y, −(1 − e_C)x and 0 five times;
- weight −1, dr e_a: K_C vanishes (ι_(∂_v)(dr e_a) = 0), and ι_(∂_r)(dr e_a) = ½e_a, so D_0 = −1 + y, three times;
- weight −2, dr²: K_C vanishes, and ι_(∂_r)dr² = dr, so D_0 dr² = (−2 + 2y)dr².

The product is [[eq:iii-f2-1-1]]; at γ_C = γ_(Υ,H) = 0 it is (ν − 2)(ν + 2)(ν − 1)³(ν + 1)³ν⁷, the sums of two of the
1-form values 1, −1, 0, 0, 0.

*The threshold.* The normalisation of [[sec:i-a-1]] is that of the proof of [[lem:iii-d-5-1]], β_0⁻¹p_(1,±) being K up
to the orientation sign. For a matrix K and δ > 0, a Jordan basis rescaled so that the off-diagonal entries are at most
δ defines an inner product in which the self-adjoint part of K has its eigenvalues below max Re spec K + δ; K is
constant on N*ℋ up to the rotations, which act by isometries of such a choice made at one point and transported. The
sign of a_v: at r_h, g⁻¹(c_C, c_C) = 2a_v a_r < 0 and g⁻¹c_C = a_v∂_r + a_r∂_v, and a past-directed timelike vector
has positive inner product with the future-directed null ∂_v, which is c_C(∂_v) = a_v. The continuity in b and the
parameters is as in [[lem:iii-d-5-1]]. ∎

The constraint damping thus helps at the horizon as it does at infinity ([[eq:iii-f-3-1]]): its five eigenvalues are
the background's 2, 1, 1, 1, 0 lowered by x · (2, 1, 1, 1, 1 − e_C), and the gauge modification's five are the
background's −2, −1, −1, −1, 0 raised by y · (2, 1, 1, 1, 1); the other five are 0. The value of x is fixed with c_C in
[[sec:iv4-0]]; the regularity s is chosen accordingly, once.

**Corollary {#cor:iii-f2-1-2}** (The hypotheses of the spectral theory.) For b near b_0 and the parameters of
[[sec:iii-f1-1]], L_b^(·) satisfies, with (Dyn), the hypotheses (H1)–(H5) of [[sec:i-a-1]], with ϑ_ℋ < ϑ_L + δ, and
(H6)–(H7) of [[ch:s02]]: (H1), (H2) and the operator part of (H6) by [[lem:iii-f-2-1]], the threshold at infinity by
[[eq:iii-f-3-1]] (min spec S̄ = 0), (H7) by [[prop:iii-f-4-1]], and the horizon by [[lem:iii-f2-1-1]], the remaining
items concerning the metric alone and holding as for □^Υ_b ([[sec:iii-d-2]]–[[sec:iii-d-5]]). Hence, for
s > ½ + ϑ_L and admissible orders: L_b^(σ) : 𝒳_σ → 𝒴_σ is Fredholm of index 0 for σ ≠ 0, Im σ ≥ 0 ([[thm:i-a-7-2]] (3),
[[thm:i-b-1-3]] (3)); there is C_hf with L_b^(σ) invertible for |σ| ≥ C_hf, Im σ ≥ 0 ([[thm:i-b-1-3]], as
[[prop:iii-d-6-1]] for □^Υ_b); and the constants and the openness of invertibility are uniform in b ([[thm:i-a-8-1]]).
The same holds for P′, whose horizon matrix is [[eq:iii-f2-1-1]] at x = 0.

**Lemma {#lem:iii-f2-1-3}** (Conormal states.) Let P̂ satisfy (H1)–(H4), σ ≠ 0 with Im σ ≥ 0, and u ∈ 𝒜^a(X̄; E) for some
a ∈ ℝ (smooth up to ∂_♯X, conormal at ∂X) with P̂(σ)u = 0. Then u ∈ 𝒳_σ for admissible orders, so
u ∈ 𝒜^(3/2+S̄−ϵ) for every ϵ > 0 ([[thm:i-a-7-2]] (5)), and u = 0 if P̂(σ) is invertible.

*Proof.* Admissibility ((O1)–(O3) of [[sec:i-a-1]]) bounds 𝗋 + α_+ at R_out, the zero section of the boundary face,
only from above; so [[lem:i-a-7-1]] gives admissible orders with 𝗋_out + α_+ < min(a − 2, −½ + S̄) when Re σ ≠ 0, and
the constant order 𝗋_out is allowed when Re σ = 0 ([[thm:i-a-7-2]] (2)). By [[lem:i-a-7-4]] (a),
u ∈ H̄^(s,𝗋+α_+) for every s (the order exceeds a − 2 only away from the zero section, where it is unrestricted), and
P̂(σ)u = 0 ∈ 𝒴_σ. The kernel does not depend on the admissible orders ([[thm:i-a-7-2]] (3)). ∎

### The linearised Einstein equation on Tangherlini {#sec:iii-f2-2}

On {r > r_h} use the static chart (t, r, z), g_(b_0) = −f dt² + f⁻¹dr² + r²γ, r_* := r + (r_h/2) log((r − r_h)/(r +
r_h)), and the time t_* of [[eq:iii-b-3-6]], which is v + F_H(r) near r_h (v = t + r_*, F_H smooth in the ingoing chart)
and t − r_* + c_0 + O(r⁻¹), with all derivatives, at infinity (proof of [[prop:iii-d-6-2]], *The class*). A *mode* is
h = e^(−iσt_*)u with u smooth on {r > r_0} (in the ingoing chart near r_h) and conormal at infinity, u ∈ 𝒜^a for some
a; equivalently, on {r > r_h}, h = e^(−iσt)e^(−iσr_*) × (smooth across r_h) near r_h and
e^(−iσt)e^(iσr_*) × (conormal) near infinity. The operators D Ric, δ*, □^Υ_(b_0) and P′ at b_0 commute with the
rotations (E^Υ at b_0 is built from dt̄, dr ([[eq:iii-b-6-5]]) and c_(Υ,H) = −½χ dr), and the projections onto a type
and degree ([[lem:iii-a1-1-6]]) preserve modes. We use the radial uniqueness stated in the proof of
[[prop:iii-d-6-2]]: a solution of −Φ_** + VΦ = σ²Φ on (r_h, ∞), ∂_* := f∂_r, V real, positive, O(r⁻²) with all
derivatives at infinity and O(f) at r_h, of the form e^(−iσr_*) × (smooth at r_h) and e^(iσr_*) × (conormal,
polynomially bounded) at infinity, vanishes.

*The Kodama–Ishibashi reduction.* Write g_(b_0) = g_ab dy^a dy^b + r²γ with the orbit metric
g_ab dy^a dy^b = −f dt² + f⁻¹dr², D_a its covariant derivative, □_2 := D^aD_a its wave operator and ε_ab its volume
form. The vacuum equation D Ric(h) = 0 is equivalent to the vanishing of the linearised Einstein tensor, as
δG = G_(g_(b_0)) ∘ D Ric at the Ricci-flat g_(b_0) and G_(g_(b_0)) is invertible ([[lem:iii-b-6-2]]). We use the
following results of [KI03], which hold in every dimension n + 2; we state them at n = 3, K = 1, Λ = 0 and 2M = m_0,
where the metric function of [KI03, (2.15)] is f. Page numbers refer to the arXiv version of [KI03].

**Theorem {#thm:s15-ki}** ([KI03, Sections 2–5].) Let h be a symmetric 2-tensor on {r > r_h} of one type and degree l,
decomposed by [KI03, (2.4), p. 4, (5.1), p. 13, (5.7)–(5.9), p. 14], with D Ric(h) = 0.

(T) ([KI03, (5.3)–(5.6), p. 13].) Tensor type, l ≥ 2: h = 2r²H_T T_ij dz^i dz^j with T trace-free, divergence-free and
(Δ̂ + k_T²)T = 0, k_T² = κ − 2. H_T is gauge invariant, it satisfies □_2H_T + (3/r)Dr · DH_T − ((k_T² + 2)/r²)H_T = 0,
and Φ := r^(3/2)H_T satisfies □_2Φ − (V_T/f)Φ = 0 with V_T = (f/r²)(k_T² + 2 + 3/4 + 9m_0/(4r²)).

(V) ([KI03, (5.10)–(5.15), p. 14].) Vector type, l ≥ 2: h = 2rf_a V_i dy^a dz^i + 2r²H_T V_ij dz^i dz^j with V co-closed,
(Δ̂ + k_V²)V = 0, k_V² = κ − 1 and V_ij = −(D̂_iV_j + D̂_jV_i)/(2k_V). F_a := f_a + (r/k_V)D_aH_T is gauge invariant, and
r²F^a = ε^(ab)D_bΩ for a function Ω on the orbit space satisfying □_2Ω − (3/r)Dr · DΩ − ((k_V² − 2)/r²)Ω = 0; and
Φ := r^(−3/2)Ω satisfies □_2Φ − (V_V/f)Φ = 0 with V_V = (f/r²)(k_V² + 1 + 3/4 − 27m_0/(4r²)).

(V1) ([KI03, (5.16)–(5.17), p. 15].) Vector type, l = 1 (V a Killing 1-form of 𝕊³, V_ij = 0, h = 2rf_a V_i dy^a dz^i):
F^(1)_ab := rD_a(f_b/r) − rD_b(f_a/r) is gauge invariant and equals Lε_ab/r⁴ with L a constant.

(S) ([KI03, (2.7)–(2.8), p. 5, (2.11), p. 5, (2.20)–(2.24), p. 7, (3.1)–(3.10), pp. 8–9].) Scalar type, l ≥ 2:
h = f_ab S dy^a dy^b + 2rf_a S_i dy^a dz^i + 2r²(H_L γ_ij S + H_T S_ij)dz^i dz^j with (Δ̂ + k²)S = 0, k² = κ,
S_i = −D̂_iS/k and S_ij = D̂_iD̂_jS/k² + γ_ij S/3. The quantities F := H_L + H_T/3 + r⁻¹(D^a r)X_a and
F_ab := f_ab + D_aX_b + D_bX_a, X_a := (r/k)(f_a + (r/k)D_aH_T), are gauge invariant. With X := r(F^t_t − 2F),
Y := r(F^r_r − 2F) and Z := rF^r_t, one has F^a_a = −2F, and F^t_t = (2X − Y)/(3r), F^r_r = (2Y − X)/(3r),
F^r_t = Z/r, F = −(X + Y)/(6r). If h = e^(−iσt)k with σ ≠ 0, then with Z̃ defined from Z by [KI03, (2.23)] and
ς := m_0/r², p := κ − 3, H := p + 6ς, the function Φ := (3Z̃ − r(X + Y))/(r^(1/2)H) satisfies
−f(fΦ′)′ + V_SΦ = σ²Φ with V_S = fQ/(16r²H²) and

    Q = 1296ς³ + (624p − 144)ς² + 36p(p − 12)ς + 16p³ + 60p²,                                           {#eq:s15-ki-q}

and X, Y and Z are linear combinations of Φ and Φ′ with coefficients depending on r and σ ([KI03, (3.9)]).

(S0) ([KI03, (4.1)–(4.3), p. 11, (3.12), p. 9].) Scalar type, l ≥ 2, h independent of t: then Z = 0, X and Y satisfy
the first-order system [KI03, (4.2)], the function Φ := (Q_Y X − Q_X Y)/(2k²r^(1/2)f′H) with
Q_X := 48ς² + (16p − 24)ς − 12p and Q_Y := 24ς² − 4(p + 12)ς satisfies f(fΦ′)′ = V_SΦ, and X and Y are linear
combinations of Φ and Φ′ ([KI03, (3.12a)–(3.12b)] with ∂_tΦ = 0).

In (T), (V), (S) a function Φ = e^(−iσt)Φ_0(r) satisfies □_2Φ − (V/f)Φ = 0 exactly when −Φ_0,** + VΦ_0 = σ²Φ_0, as
□_2 = −f⁻¹∂_t² + ∂_r f ∂_r.

*Positivity of the potentials.* For l ≥ 2 and r > r_h (so 0 < ς < 1 and f > 0): V_T > 0; V_V ≥ (f/r²)(k_V² − 5)
= (f/r²)(κ − 6) > 0, as κ ≥ 8; and Q > 0, so V_S > 0. Indeed p = κ − 3 ≥ 5, and with a := 624p − 144 > 0,
b := 36p(p − 12) and c := 16p³ + 60p² > 0,

    4ac − b² = 16p²((624p − 144)(4p + 15) − 81(p − 12)²) = 48p²(23p − 24)(35p + 192) > 0,

so aς² + bς + c > 0 for all real ς, and Q ≥ aς² + bς + c > 0 for ς ≥ 0. Each potential is O(r⁻²) with all derivatives
at infinity (a function of ς times f/r²) and O(f) at r_h (H ≥ p > 0).

*The low sectors.* For the types l ≤ 1 not covered by [KI03]'s master equations we use the linearised Ricci tensor
directly. The Christoffel symbols of g_(b_0) in the static chart are Γ^t_tr = f′/(2f), Γ^r_tt = ff′/2,
Γ^r_rr = −f′/(2f), Γ^r_ij = −rfγ_ij, Γ^i_rj = δ^i_j/r and those of γ; with them,
D Ric(h)_μν = ½(∇^α∇_μ h_να + ∇^α∇_ν h_μα − ∇^α∇_α h_μν − ∇_μ∇_ν tr h) is written out on each type.

**Lemma {#lem:s15-low}** (The low sectors.) Let σ ∈ ℂ, and let a, b, c be functions of r on an interval in (r_h, ∞).

(a) For h = e^(−iσt)(2a dt dr + b dr²) (scalar type 0 with f_tt = H_L = 0),

    D Ric(h)_tr = −(3iσf/(2r)) b e^(−iσt),
    D Ric(h)_ij = (iσra + (f/(2r²))(2(m_0 + 2r²)b + r³fb′)) e^(−iσt) γ_ij.

(b) For h = e^(−iσt)((2a dt dr + b dr²)S + 2rcS_i dr dz^i), S ∈ 𝒮_1 (scalar type 1 with f_tt = f_t = H_L = 0; here
D̂_iD̂_jS = −γ_ij S, k = 3^(1/2) and S_ij = 0), all components multiplied by e^(−iσt),

    D Ric(h)_tr = (S/(2r³))(3ra − iσ(3r²b + 3^(1/2)r²c − 3m_0b)),
    D Ric(h)_ri = −(S_i/(2·3^(1/2) r³(r² − m_0)))(3iσr⁵a + 3(r² − m_0)(2r² − m_0)b + 3^(1/2)r²(4(r² − m_0) + σ²r⁴)c),
    D Ric(h)_ti = −(S_i/(2·3^(1/2) r³))(3(m_0 + r²)a + r(r² − m_0)(3a′ + iσ(3b + 3^(1/2)(4c + rc′)))),
    D Ric(h)_rr = (S/(2r⁴(r² − m_0)))(2iσm_0r⁵a/(r² − m_0) + 2iσr⁶a′ + (3r⁴ + 3m_0r² − 4m_0² − σ²r⁶)b
                  + r(3r² − 2m_0)(r² − m_0)b′ + 2·3^(1/2)r⁴c + 2·3^(1/2)r³(r² − m_0)c′),
    D Ric(h)_ij = (Sγ_ij/(6r⁴))(6iσr⁵a + 3(r² − m_0)(2m_0 + 5r²)b + 2·3^(1/2)r²(5r² − 3m_0)c
                  + 3r(r² − m_0)²b′ + 2·3^(1/2)r³(r² − m_0)c′).

(c) For a static metric −A dt² + B dr² + r²γ the Einstein tensor has G^t_t = −(3/(2r³))(r²(1 − B⁻¹))′ and
G^r_r − G^t_t = (3/(2rB))(log AB)′. Hence for h = a dt² + b dr² (scalar type 0, static, with H_L = f_tr = 0), the
linearised Einstein tensor at g_(b_0) has δG^t_t = −(3/(2r³))(r²f²b)′ and δG^r_r − δG^t_t = (3f/(2r))(fb − a/f)′.

*Proof.* (a) and (b) are D Ric written out with the Christoffel symbols above, ∂_t acting as −iσ, and, in (b), the
identities D̂^iS_i = kS (from S_i = −D̂_iS/k and D̂^iD̂_iS = −k²S) and D̂_iS_j = (k/3)γ_ij S (from
D̂_iD̂_jS = −γ_ijS and k² = 3). (c) The two formulas are the tt-component and the difference of the rr- and
tt-components of the Einstein tensor of a warped product with fibre 𝕊³ of radius r; at A = f, B = f⁻¹ one has
r²(1 − B⁻¹) = m_0 and AB = 1, and the variations of A and B are −a and b, which gives δ(r²(1 − B⁻¹)) = r²f²b and
δ log AB = −a/f + fb. ∎

**Corollary {#cor:s15-low}** (Vanishing in the low sectors.) (a) In [[lem:s15-low]] (a), if σ ≠ 0 and
D Ric(h) = 0, then a = b = 0. (b) In [[lem:s15-low]] (b), if D Ric(h) = 0 on an interval on which
σ²r⁴ ≠ m_0, then a = b = c = 0. (c) In [[lem:s15-low]] (c), if D Ric(h) = 0, then (a, b) = c_1(f, 0) +
ṁ(r⁻², r⁻²f⁻²) for constants c_1, ṁ.

*Proof.* (a) The tr-component gives b = 0 (f > 0), and then the angular one gives σra = 0. (b) The tr- and
ri-components are two linear equations for (a, c) given b, with determinant 3r · 3^(1/2)r²(4(r² − m_0) + σ²r⁴)
− (−3^(1/2)iσr²)(3iσr⁵) = 12 · 3^(1/2) r³(r² − m_0) ≠ 0; they give

    a = (iσ/(4r))(2r² − 3m_0 + σ²r⁴)b,     c = (3^(1/2)/(4r²))(m_0 − 2r² + σ²r⁴)b.

Substituting, the angular component becomes −(Sγ_ij/(4r⁴))(Q_1b − Pb′) and the ti-component
−(3^(1/2)iσS_i/(4r⁴))(Q_2b + Pb′), with P := r(r² − m_0)(σ²r⁴ − m_0),
Q_1 := 5m_0² − 3m_0r² + 2m_0σ²r⁴ − 5σ²r⁶ + σ⁴r⁸ and Q_2 := −4m_0² + 3m_0r² − 4m_0σ²r⁴ + 5σ²r⁶. If σ ≠ 0 the two
equations give (Q_1 + Q_2)b = (σ²r⁴ − m_0)²b = 0, so b = 0. If σ = 0 the ti-component vanishes identically, and the
rr-component becomes (m_0 S/(4r⁴(r² − m_0)))((3r² − 2m_0)b − r(r² − m_0)b′), while the angular one is
(m_0 Sγ_ij/(4r⁴))((3r² − 5m_0)b − r(r² − m_0)b′); their difference gives 3m_0 b = 0. In both cases b = 0, and then
a = c = 0. (c) δG = 0 gives r²f²b = ṁ and fb − a/f = −c_1 with constants ṁ, c_1, that is b = ṁ/(r²f²) and
a = f(fb + c_1) = ṁ/r² + c_1 f. ∎

**Lemma {#lem:iii-f2-2-1}** (The radial equations.) Fix a type and degree, σ ∈ ℂ, and a chart (τ, r, z) in which τ is a
time function with ∂_τ the Killing field (τ = t on {r > r_h}, or τ = t_* on {r > r_0}). For a symmetric 2-tensor
h = e^(−iστ)k of that type and degree, the r-row of δ*ω = h, (δ*ω)_rμ = h_rμ for ω = e^(−iστ)w of the same type and
degree, is a linear system ∂_rW = A(r)W + H(r) for the coefficients W of w, with A smooth where the chart is:
∂_r w_r = h_rr + Γ^α_rr w_α, ∂_r w_τ = 2h_rτ + iσw_r + 2Γ^α_rτ w_α, ∂_r w_A = 2h_rA − ∂_A w_r + 2Γ^α_rA w_α, the angular
derivative acting on the harmonic algebraically. Hence: (a) every 1-form of that type with δ*ω = h on an interval is
the solution of the system determined by its value at one point; (b) in the chart (t_*, r, z) on {r > r_0}, if h is a
mode, so are the solutions; (c) in the static chart the coefficients are real-analytic in r on (r_h, ∞).

*Proof.* The formulas are the definition of δ* with ∂_τ ↦ −iσ. (a) is uniqueness for the system. (b) A is smooth on
(r_0, ∞), as the chart is. Near infinity, in the time t_* (t − r_* + c_0 + O(r⁻¹) there), g_(t_*t_*) + 1, g_(t_*r) + 1
and g_rr are O(r⁻²) with b-derivatives, and g is t_*-independent and block-diagonal against the sphere. So
Γ^α_rr and Γ^α_(rt_*) (α ∈ {t_*, r}) are O(r⁻³), Γ^(t_*)_rA = Γ^r_rA = Γ^A_rr = Γ^A_(rt_*) = 0 and
Γ^B_rA = r⁻¹δ^B_A: the one entry of A that does not decay is iσ, coupling w_r into the w_(t_*) row. In
W̃ := (w_r, r⁻¹w_(t_*), r⁻¹w_A) the system is r∂_rW̃ = ÃW̃ + H̃ with Ã bounded with all b-derivatives (the entry iσ in
the second row; in the angular row r∂_rW̃_A = W̃_A − ∂_AW̃_r + 2h_rA, from Γ^B_rA = r⁻¹δ^B_A and the scaling, a diagonal
+1 and an O(1) coupling −∂_A to W̃_r, bounded on each type and degree; O(r⁻¹) and O(r⁻²) entries elsewhere) and H̃
conormal with a polynomial bound; for this b-system variation of constants gives polynomial bounds and propagates
b-regularity. (c) The static Tangherlini metric is analytic in r > r_h. ∎

**Theorem {#thm:iii-f2-2-2}** (Mode stability of the linearised Einstein operator on Tangherlini; [AHW24, Theorem 6.1
(1)] in dimension 4 + 1.) Let σ ≠ 0, Im σ ≥ 0, and let h be a mode of one type and degree with D_(g_(b_0))Ric(h) = 0
on {r > r_h}. Then there is a mode 1-form ω on {r > r_0}, of the same type and degree, with h = δ*ω on {r > r_h}.

*Proof.* We work on {r > r_h} in the static chart, with the splitting into (t, r)- and 𝕊³-parts of
[[thm:s15-ki]]. In each sector we find a 1-form ζ, smooth on {r > r_h} off at most one radius, with h = δ*ζ there;
Step 5 removes the exceptional radius, and Step 6 makes ζ a mode on {r > r_0}. Each master field below is a function
of the components of h, and of finitely many of their r-derivatives, which in the ingoing chart (v, r, z) has no factor
1/f; so it is e^(−iσt)e^(−iσr_*) × (smooth at r_h). At infinity the static components are combinations of those in
(t_*, r, z) with bounded conormal coefficients, so it is e^(−iσt)e^(iσr_*) × (conormal, polynomially bounded).

*The gauge shifts.* For ζ = e^(−iσt)(A_a S dy^a + r²BS_i dz^i) (scalar type) the definition of δ* with
Γ^j_ai = (∂_a r/r)δ^j_i and Γ^a_ij = −r(D^a r)γ_ij gives that δ*ζ shifts f_ab by ½(D_aA_b + D_bA_a), f_a by
(r²D_aB − kA_a)/(2r), H_L by kB/6 + (D^a r)A_a/(2r) and H_T by −kB/2 (using D̂_iS_j = −kS_ij + (k/3)γ_ij S); for
ζ = e^(−iσt)r²BV_i dz^i (vector type) it shifts f_a by (r/2)D_aB and H_T by −k_V B/2 (using D̂_(iV_j) = −k_V V_ij).

*Step 1: tensor type, l ≥ 2.* h = 2r²H T_ij dz^i dz^j. By [[thm:s15-ki]] (T), Φ := r^(3/2)H solves
−Φ_** + V_TΦ = σ²Φ, V_T > 0. H is an angular component, the same in both charts; the radial uniqueness gives Φ = 0,
so h = 0 = δ*0.

*Step 2: vector type, l ≥ 2.* h = 2rf_a V_i dy^a dz^i + 2r²H_T V_ij dz^i dz^j. With ζ_0 := r²BV_i dz^i,
B := 2H_T/k_V, the vector gauge shifts give H_T − (k_V/2)B = 0 and f_a + (r/2)D_aB = f_a + (r/k_V)D_aH_T; so
h′ := h + δ*ζ_0 has H_T = 0 and f_a = F_a := f_a + (r/k_V)D_aH_T, the gauge invariant of [[thm:s15-ki]] (V).
D Ric(h′) = D Ric(h) = 0, so r²F^a = ε^(ab)D_bΩ with Ω as in (V). The r-component, r²F^r = ε^(rt)∂_tΩ, determines
Ω = e^(−iσt)Ω_0(r) up to a function of r alone, which (V)'s equation for Ω and the t-component force to vanish, as
k_V² − 2 > 0; so r²F^r = −iσε^(rt)Ω and Ω = ε^(tr)r²F^r/(iσ), as ε^(tr) = −ε^(rt) = ±1 (the orbit metric has
determinant −1). In the ingoing
chart F_a dy^a = F_v dv + F′_r dr, so F^r = fF_r = fF′_r + F_v has no factor 1/f. Φ := r^(−3/2)Ω solves the master
equation with V_V > 0, so Φ = 0; then F = 0, h′ = 0 and h = δ*(−ζ_0).

*Step 3: scalar type, l ≥ 2.* h = f_ab S dy^a dy^b + 2rf_a S_i dy^a dz^i + 2r²(H_L γ_ij S + H_T S_ij)dz^i dz^j. With
ζ_1 := 2X_a S dy^a + (2r²/k)H_T S_i dz^i, X_a as in [[thm:s15-ki]] (S), the gauge shifts give
H_T + (−k/2)(2H_T/k) = 0 and f_a + (r/k)D_aH_T − (k/r)X_a = 0, so h′ := h + δ*ζ_1 has f_a = H_T = 0, and its remaining
components are the invariants F_ab and F (f_ab + D_aX_b + D_bX_a = F_ab and H_L + H_T/3 + r⁻¹(D^a r)X_a = F, by the
same shifts; X_a vanishes for h′). D Ric(h′) = 0, so by [[thm:s15-ki]] (S) the function
Φ solves −Φ_** + V_SΦ = σ²Φ, V_S > 0. In the ingoing chart, with F_ab dy^a dy^b = F_vv dv² + 2F_vr dv dr + F′_rr dr²,
one has F^t_t = −F_vv/f, F^r_r = F_vv/f + 2F_vr + fF′_rr and F^r_t = F_vv + fF_vr, so X + Y = r(2F_vr + fF′_rr − 4F)
and Z = r(F_vv + fF_vr) have no factor 1/f, and neither has Φ (H ≥ p > 0). The radial uniqueness gives Φ = 0, so
X = Y = Z = 0 ([KI03, (3.9)]), F_ab = F = 0 by the relations of (S), h′ = 0 and h = δ*(−ζ_1).

*Step 4: the exceptional sectors.* *Scalar type 0* (S = 1). δ*(e^(−iσt)(A_t dt + A_r dr)) shifts f_tt by
−iσA_t − (ff′/2)A_r and H_L by fA_r/(2r), so f_tt = H_L = 0 is reached with A_r = −2rH_L/f and then A_t,
algebraically on {r > r_h}; the result h′ has the form of [[lem:s15-low]] (a) and solves D Ric(h′) = 0, so
f_tr = f_rr = 0 by [[cor:s15-low]] (a). So h is pure gauge; there is no change of mass, σ being nonzero. *Vector type 1*
(V a Killing field of 𝕊³, V_ij = 0). By [[thm:s15-ki]] (V1), F^(1)_tr = Lε_tr/r⁴ with L constant; as h is
proportional to e^(−iσt) with σ ≠ 0, L = 0, so r∂_t(f_r/r) = r∂_r(f_t/r). With B := 2if_t/(σr), (r/2)∂_tB = f_t and
(r/2)∂_rB = (ir/σ)∂_r(f_t/r) = f_r, so h = δ*(r²BV_i dz^i) by the vector gauge shift. *Scalar type 1*
(D̂_iD̂_jS = −γ_ij S, S_ij = 0, k = 3^(1/2)). The shifts of f_tt, f_t and H_L under
δ*(e^(−iσt)(A_aS dy^a + r²BS_i dz^i)) are −iσA_t − (ff′/2)A_r, −(kA_t + iσr²B)/(2r) and kB/6 + fA_r/(2r), free of
derivatives, with determinant (rows f_tt, f_t, H_L; columns A_t, A_r, B)

    det ⎛ −iσ         −ff′/2     0        ⎞ = σ²f/4 − ff′k²/(24r) = (r² − m_0)(σ²r⁴ − m_0)/(4r⁶).
        ⎜ −k/(2r)     0          −iσr/2   ⎟
        ⎝ 0           f/(2r)     k/6      ⎠

So off the radius r_σ with σ²r_σ⁴ = m_0 (which lies in (r_h, ∞) only for real σ with σ² < 1/m_0) the gauge reaching
f_tt = f_t = H_L = 0 is algebraic; the result has the form of [[lem:s15-low]] (b), and [[cor:s15-low]] (b) gives
f_tr = f_rr = f_r = 0: h = δ*ζ_± on the intervals (r_h, r_σ) and (r_σ, ∞).

*Step 5: the radius r_σ.* Let ω be the solution, on (r_h, ∞), of the static radial system of [[lem:iii-f2-2-1]] equal
to ζ_− at a point of (r_h, r_σ). By [[lem:iii-f2-2-1]] (a), ω = ζ_− on (r_h, r_σ), so κ_h := h − δ*ω, smooth on
(r_h, ∞), vanishes there. On (r_σ, ∞), ζ_+ − ω solves the homogeneous radial system, so it is Z(r)c for a fundamental
matrix Z, analytic on (r_h, ∞) ([[lem:iii-f2-2-1]] (c)), and κ_h = δ*(Zc) there. δ*(Zc) is analytic on (r_h, ∞), and
at r_σ all its derivatives from the right are those of the smooth κ_h, which vanish (from the left); so
δ*(Zc) ≡ 0 and κ_h = 0 on (r_σ, ∞) too: h = δ*ω on (r_h, ∞).

*Step 6: the mode.* In each sector h = δ*ζ on (r_h, ∞) with ζ smooth there. Let ω be the solution on (r_0, ∞) of the
radial system in the chart (t_*, r, z) equal to ζ at a point r_1 > r_h; by [[lem:iii-f2-2-1]] (a) in that chart, ω = ζ
on (r_h, ∞), so h = δ*ω there, and by [[lem:iii-f2-2-1]] (b) ω is a mode. ∎

The sectors exhaust the types and degrees of [[lem:iii-a1-1-6]] for symmetric 2-tensors on 𝕊³: tensor l ≥ 2, vector
l ≥ 1, scalar l ≥ 0.

**Lemma {#lem:iii-f2-2-3}** (Continuing a solution inside the horizon.) Let Q be a stationary operator on
{r > r_0 − δ_0} whose principal part is a positive multiple of □_(g_(b_0)), commuting with the rotations, σ ∈ ℂ with
Im σ ≥ 0, and w of one type and degree, smooth on {r ≥ r_h} (up to the horizon), with Q^(σ)w = 0 on {r > r_h}. Then
there is w̃ of that type and degree, smooth on {r > r_0 − δ_0} (so up to {r = r_0}), with Q^(σ)w̃ = 0 on
{r > r_0 − δ_0} and w̃ = w on {r ≥ r_h}.

*Proof.* As in part (d) of the proof of [[prop:iii-d-6-2]], in the ingoing chart the equation on the coefficients U(r) of
the type and degree is −fU″ + AU′ + BU = 0 with A, B smooth on (r_0 − δ_0, ∞), and with Y := (U, (r − r_h)U′) it is
(r − r_h)Y′ = MY, M smooth. Y is smooth on [r_h, ∞) and solves the equation on (r_h, ∞), so its Taylor series at r_h
solves it formally. Let Y_B be smooth on (r_h − ϵ, r_h] with that Taylor series (Borel), so R := (r − r_h)Y_B′ − MY_B
vanishes to infinite order at r_h. Let Ψ be a fundamental matrix of (r − r_h)Ψ′ = MΨ on (r_h − ϵ, r_h); Gronwall gives
|Ψ(r)| + |Ψ(r)⁻¹| ≤ C|r − r_h|^(−m_1), m_1 := max ‖M‖. Then Z(r) := −Ψ(r)∫_(r_h)^r Ψ(s)⁻¹R(s)(s − r_h)⁻¹ ds converges,
vanishes to infinite order at r_h (the integrand does, and the equation Z′ = (MZ − R)/(r − r_h) carries this to every
derivative), and solves (r − r_h)Z′ = MZ − R. So Y_B + Z solves the equation on (r_h − ϵ, r_h) with the Taylor series of
Y at r_h; glued to Y it is smooth on (r_h − ϵ, ∞), and on (r_0 − δ_0, r_h − ϵ], where f < 0, the equation is a regular
second-order system and the solution continues. Its first entry, times the harmonic and e^(−iσt_*), is w̃ (the first
row of M being (0, 1), the second entry stays (r − r_h)U′). ∎

### Mode stability at the Tangherlini parameter {#sec:iii-f2-3}

**Proposition {#prop:iii-f2-3-1}** (Mode stability at b_0; [Hin26, Proposition 8.8] at b_0 in dimension 4 + 1.) Let the
modification parameters be those of [[prop:iii-d1-4-1]] and [[sec:iii-f1-1]], and s > ½ + ϑ_L. For every σ ≠ 0 with
Im σ ≥ 0, L_(b_0)^(σ) : 𝒳_σ → 𝒴_σ is invertible, and L_(b_0)^(σ) has trivial kernel on 𝒜^α(X̄; S²T*X) for every
α ∈ ℝ.

*Proof.* By [[cor:iii-f2-1-2]] the operator is Fredholm of index 0, so injectivity suffices; and by [[lem:iii-f2-1-3]] a
kernel element in 𝒜^α lies in 𝒳_σ. Let u ∈ 𝒳_σ, L_(b_0)^(σ)u = 0. By [[thm:i-a-7-2]] (5), u ∈ 𝒜^(3/2−ϵ), smooth up to
{r = r_0}, conormal at infinity. Let h := e^(−iσt_*)u, a mode, with L_(b_0)h = 0.

*The gauge 1-form.* η := (δ_(E_Υ))^(σ)Gu is conormal and smooth up to {r = r_0}, and the linearised second Bianchi
identity δG D Ric = 0 gives δG(2L_(b_0)) = □^C δ_(E_Υ)G, so (□^C_(b_0))^(σ)η = 0. By [[lem:iii-f2-1-3]] for □^C_(b_0),
which satisfies (H1)–(H4) ([[thm:iii-e-1-1]] (2)), and [[thm:iii-e-1-1]] (1), η = 0. So D Ric(h) = 0 and
δ_(E_Υ)Gh = 0 on {r > r_0}, and P′h = 0 there.

*The exterior.* Let h_π be the component of h of one type and degree, again a mode with both equations. By
[[thm:iii-f2-2-2]] there is a mode 1-form ω_π = e^(−iσt_*)w_π with h_π = δ*ω_π on {r > r_h}; then
□^Υω_π = 2δ_(E_Υ)Gδ*ω_π = 2δ_(E_Υ)Gh_π = 0 there. [[lem:iii-f2-2-3]], with Q = □^Υ_(b_0), gives w̃_π, smooth on X̄
(that is, up to {r = r_0}), conormal at infinity (it is w_π on {r ≥ r_h}), with (□^Υ_(b_0))^(σ)w̃_π = 0 on all of X̄.
By [[lem:iii-f2-1-3]] and [[prop:iii-d1-4-1]] (invertibility for every σ of the closed upper half plane), w̃_π = 0; so
h_π = 0 on {r > r_h}.

*The interior.* h_π vanishes on {r > r_h} and solves P′h_π = 0 on {r > r_0}, 2P′ = □ + 2δ*E^ΥG having the principal
part of □; part (d) of the proof of [[prop:iii-d-6-2]] (the system (r − r_h)Y′ = MY and Gronwall) gives h_π = 0 on
{r > r_0}. As this holds for every type and degree, u = 0. ∎

### Near the Tangherlini parameter {#sec:iii-f2-4}

**Proposition {#prop:iii-f2-4-1}** ([Hin26, Proposition 8.8] for |σ| ≥ c_0, in dimension 4 + 1.) Fix the modification
parameters as in [[prop:iii-f2-3-1]]. For every c_0 > 0 there is a neighbourhood ℬ(c_0) of b_0 such that for
b ∈ ℬ(c_0) and every σ with Im σ ≥ 0, |σ| ≥ c_0, L_b^(σ) : 𝒳_σ → 𝒴_σ is invertible and has trivial kernel on every
𝒜^α.

*Proof.* As [[prop:iii-d-6-3]]. For |σ| ≥ C_hf, [[cor:iii-f2-1-2]]. On the compact set
K := {c_0 ≤ |σ| ≤ C_hf, Im σ ≥ 0}, L_(b_0)^(σ) is invertible ([[prop:iii-f2-3-1]]); by [[thm:i-a-8-1]] every σ ∈ K
has a neighbourhood U_σ and a neighbourhood of b_0 on which invertibility holds; finitely many U_σ cover K. The kernel
on 𝒜^α by [[lem:iii-f2-1-3]]. ∎

### Small frequencies near the Tangherlini parameter {#sec:iii-f2-5}

For b ≠ b_0 and 0 < |σ| < c_0 the perturbation argument of [[prop:iii-f2-4-1]] degenerates, the neighbourhood ℬ(c_0)
shrinking as c_0 → 0. [Hin26] covers this range by [AHW24, Theorem 6.1 (1)], proved on Kerr from the Teukolsky
equation, which has no counterpart for the five-dimensional Myers–Perry family; it is needed where [Hin26] uses
Proposition 8.8 (the contour deformation before [Hin26, (10.3)], through [Hin26c, Theorem 9.5], p. 168). Here it is
supplied by the low energy analysis of L_b^(σ) near the zero energy operator, whose kernel and cokernel are found in
[[sec:iii-f3-4]]: mode stability for b near b_0 at small nonzero frequencies is [[cor:iii-h-4-3]] and
[[cor:iii-h-4-4]].

### The zero energy setting {#sec:iii-f3-1}

This section and the next three carry [Hin26, Section 8.4] from Proposition 8.9 to Corollary 8.13 (pp. 154–158): the
linearised Myers–Perry metrics brought into the gauge, the spin changes that are pure gauge, the kernel and cokernel
of the zero energy operator L_b^(0), eleven-dimensional against the seven of [Hin26], and the linear right inverse
built from them. [Hin26] takes the kernel bound from [AHW24, Theorem 6.1 (2)], the classification of the stationary
decaying solutions of the linearised Einstein equation on Kerr; at b_0 it is proved here harmonic by harmonic at zero
frequency ([[thm:iii-f3-3-1]]), and near b_0 the count follows from the invertibility at b_0 of an augmented operator
and the perturbation theory of [[thm:i-c-7-1]], so no rigidity statement for spinning Myers–Perry metrics is needed.
The pairings of [Hin26, Lemma 8.12] are not used here; they are part of [[sec:iii-f4-3]].

The parameters are those of [[sec:iii-f1-1]] and [[sec:iii-f2-1]]: (Dyn), z = 4e_Υγ_Υ² ∈ (0, ½], (C1), γ_Υ as in
[[prop:iii-f1-3-3]], the horizon modification and b ∈ ℬ(γ_(Υ,H)) as in [[prop:iii-d1-4-1]] and [[sec:iii-d2-1]], and
s > ½ + ϑ_L ([[lem:iii-f2-1-1]]). *All b-spaces use an unweighted b-density μ_b = |dx|/|x|⁴ near ∂X*, so that
H̄_b^(s,α) here is H̄_b^(s,α−2) of [[ch:s03]], and H_b^(∞,a) ⊂ 𝒜^a near ∂X. ε_Υ and ℰ_ind are as in
[[sec:iii-d2-1]]: ε_Υ ∈ (0, ½), fixed by the indicial roots of (□^Υ_b)^(0) alone, is less than d(Re ι, ℤ) for every
indicial root ι of (□^Υ_b)^(0) with non-integer real part of modulus at most 10 (it is the gauge potential operator's
number, not the number ε_ind of [[eq:iii-f1-2-2]], which concerns the roots of L_b^(0)), and ℰ_ind denotes an index set
with min Re ℰ_ind ≥ ε_Υ, independent of b, which may change from line to line. Write
β^L_+ := min{Re ι : ι an indicial root of L_b^(0), Re ι > 0}; by [[prop:iii-f1-2-3]], β^L_+ > 1, so every
α ∈ (0, 1] lies in the indicial gap (0, β^L_+).

*Densities and adjoints.* In the Kerr–Schild coordinates (t, x) of [[def:iii-b-3-2]], g_b = η + Hk ⊗ k with k null for
η ([[lem:iii-b-3-3]] (a)), so det g_b = det η = −1; and t_* − t = −ψ(|x|) is a function on X ([[eq:iii-b-3-6]]), so the
change (t, x) ↦ (t_*, x) has Jacobian 1 and |dg_b| = |dt_*| |dx| for every b. Adjoints on X are taken with respect to
|dx| and the fibre inner product induced by g_b (indefinite); for a stationary operator P on M with formal adjoint P*
with respect to |dg_b| and g_b, P^(0)* = (P*)^(0) (pair φ(t_*)u with φ(t_*)v, φ ∈ C_c^∞(ℝ), u, v ∈ C_c^∞(X°)
stationary, and integrate in t_*). The spatial density |dg_b|_X| of [Hin26] is |dx| here.

*The linearised family at b_0.* t denotes the Kerr–Schild time, v := t + |x|, and on {r > r_h} the static chart
(t_s, r, z) of [[sec:iii-f2-2]] has v = t_s + r_*, so dt + d|x| = dt_s + f⁻¹dr. For Ȧ ∈ 𝔰𝔬(4) put
V(Ȧ) := (Ȧx) · dx; it is r² times a Killing 1-form V_i dz^i of the unit 𝕊³, of vector type 1, and Ȧ ↦ V(Ȧ) is an
isomorphism of 𝔰𝔬(4) onto 𝒱_1 ([[eq:iii-d2-1-2]]).

**Lemma {#lem:iii-f3-1-1}** (The linearised family at b_0.) ġ_(b_0)(1, 0) = |x|⁻²(dt + d|x|)² and
ġ_(b_0)(0, Ȧ) = 2m_0|x|⁻⁴(dt + d|x|) ⊗_s V(Ȧ). So ġ_(b_0)(1, 0) is O(4)-invariant (scalar type 0) and equals
r⁻²(dt_s + f⁻¹dr)²; and ġ_(b_0)(0, Ȧ) is of vector type 1, with coefficients (h = 2rf_a V_i dy^a dz^i)
f_t = m_0 r⁻³ and f_r = m_0 r⁻³ f⁻¹ in the static chart, on the Killing form r⁻²V(Ȧ).

*Proof.* At A = 0 the metric is η + m|x|⁻²(dt + d|x|)² ([[prop:iii-b-3-4]]), which gives the first formula. For the
second, s = −½ tr(A²), p² and |Ax|² are of order |A|², so r_A = |x| + O(|A|²), P = r_A⁴ + O(|A|²), F_A = 1 + O(|A|²)
and H_(m,A) = m|x|⁻² + O(|A|²) ([[eq:iii-b-3-1]], [[lem:iii-b-3-1]] (b)); and 𝖬/P = (r²I − A²)⁻¹ = r⁻²I + O(|A|²)
([[lem:iii-b-3-1]] (a)), so ℓ_A = |x|⁻¹x · dx + |x|⁻²(Ax) · dx + O(|A|²). Differentiating H_(m,A)k_A ⊗ k_A at A = 0 in
the direction Ȧ gives 2m|x|⁻²(dt + d|x|) ⊗_s |x|⁻²(Ȧx) · dx. With a ⊗_s b = ½(a ⊗ b + b ⊗ a), the component of
ġ_(b_0)(0, Ȧ) on (∂_(t_s), ∂_(z^i)) is m_0r⁻⁴ · r²V_i, so rf_t = m_0r⁻², and the dr part gives f_r = m_0r⁻³f⁻¹. ∎

### Gauged linearised Myers–Perry metrics {#sec:iii-f3-2}

**Lemma {#lem:iii-f3-2-1}** (Inverse images.) Let k ∈ {1, 2} and let f be a stationary section, smooth on X̄, with
f ∈ ρ^(2+k)C^∞ near ∂X. Then u := (□^Υ_b)^(0)⁻¹f ∈ 𝒜^((k,0)∪(k+ℰ_ind))(X̄; E), with ℰ_ind independent of b; its ρ^k
coefficient u_k solves I(k)u_k = f_(2+k), where f = ρ^(2+k)f_(2+k) + O(ρ^(3+k)) and I is the indicial family of
A := ρ⁻²(□^Υ_b)^(0) near ∂X ([[eq:i-c-1-3]]).

*Proof.* f ∈ 𝒜^(2+(k,0)), so [[lem:iii-d1-5-1]] (2) applies with ℰ = (k, 0) and α ∈ (0, k), and its proof gives
u ∈ 𝒜^(ℰ′) with ℰ′ the index set of [[lem:iii-a-1-4]] built from E(α) (the boundary spectrum with real part > α),
F = (k, 0) and their shifts by ℕ_0: E_0 = E(α) ∪̄ F, E_(j+1) = E(α) ∪̄ (F ∪̄ (E_j + 1)). By [[lem:iii-d-4-1]] and
[[eq:iii-d-4-2]], every indicial root with positive real part is at least ι^Υ_(s1,2) ∈ (2, 3); so E(α) has
min Re ≥ ι^Υ_(s1,2), and ι^Υ_(s1,2) − 2 > ε_Υ by the choice of ε_Υ. The exponent k occurs in each E_j only through
F, with logarithmic order 0: k ∉ E(α), and E_j + 1 has minimal real part at least k + 1. Every other element of
ℰ′ = ⋃_j E_j has real part ≥ k + 1 or ≥ ι^Υ_(s1,2), hence ≥ k + ε_Υ. So ℰ′ ⊂ (k, 0) ∪ (k + ℰ_ind); the roots do not
depend on b ([[lem:iii-d-4-1]]), nor does this index set. Inserting u = ρ^k u_k + O(ρ^(k+ε_Υ)) into Au = ρ⁻²f and
comparing the ρ^k terms gives I(k)u_k = f_(2+k); I(k) is invertible since neither 1 nor 2 is an indicial root
([[sec:iii-d2-1]]). (At the types that occur below, scalar type 0 at k = 1 and vector type 1 at k = 2, the
determinants are det N_s0(1) = 1 · (−2) · (1 − 1 − 2 − z) = 2(2 + z) and N_v1(2) = (2 + 1)(3 − 2) = 3, by
[[eq:s13-dets]].) ∎

**Proposition {#prop:iii-f3-2-2}** (Gauged linearised metrics; [Hin26, Proposition 8.9] in dimension 4 + 1.) For b near
b_0 and ḃ = (ṁ, Ȧ) ∈ ℝ × 𝔰𝔬(4) let η_b(ḃ) := 2δ_(g_b,E_Υ)G_(g_b)ġ_b(ḃ) and

    ω̇_b(ḃ) := −(□^Υ_b)^(0)⁻¹ η_b(ḃ),     ġ^Υ_b(ḃ) := ġ_b(ḃ) + δ*_(g_b) ω̇_b(ḃ).                         {#eq:iii-f3-2-1}

(1) ω̇_b(1, 0) ∈ 𝒜^((1,0)∪(1+ℰ_ind)) and ω̇_b(0, Ȧ) ∈ 𝒜^((2,0)∪(2+ℰ_ind)); in particular neither has a logarithmic
term (the term c_b(log ρ)ω̄^(0)_s0 of [Hin26] is absent).

(2) ġ^Υ_b(ḃ) lies in ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b), hence in ker L_b^(0), and

    ġ^Υ_b(1, 0) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),     ġ^Υ_b(0, Ȧ) ∈ 𝒜^((3,0)∪(3+ℰ_ind)).                            {#eq:iii-f3-2-2}

(3) ω̇_b(ḃ) and ġ^Υ_b(ḃ) are linear in ḃ and of class C^k in b for every k, with values in H̄_b^(s,α′), resp.
H̄_b^(s−1,α′+1), for every s and every α′ ∈ (0, 1) (for ḃ = (1, 0)) or α′ ∈ (0, 2) (for ḃ = (0, Ȧ)).

(4) At b_0, ω̇_(b_0)(1, 0) and ġ^Υ_(b_0)(1, 0) are of scalar type 0, and ω̇_(b_0)(0, Ȧ), ġ^Υ_(b_0)(0, Ȧ) of vector type
1; and the coefficient f_t of ġ^Υ_(b_0)(0, Ȧ) is that of ġ_(b_0)(0, Ȧ).

*Proof.* (1) By [[eq:iii-b-3-7]], ġ_b(1, 0) ∈ ρ²C^∞ and ġ_b(0, Ȧ) ∈ ρ³C^∞ near ∂X, smooth on X̄ and stationary. As in
the proof of [[lem:iii-d2-2-1]], δ_(g_b) ∈ ρDiff¹_b, E^Υ_(g_b) ∈ ρDiff⁰_b and G_(g_b) ∈ Diff⁰_b near ∂X, with
coefficients smooth on X̄; so η_b(1, 0) ∈ ρ³C^∞ and η_b(0, Ȧ) ∈ ρ⁴C^∞, and [[lem:iii-f3-2-1]] with k = 1, resp. k = 2,
gives (1).

(2) g_b is Ricci-flat for every b ([[prop:iii-b-3-4]]), so D_(g_b)Ric(ġ_b(ḃ)) = 0; and D_(g_b)Ric ∘ δ*_(g_b) = 0, since
2δ*_(g_b)X^♭ = ℒ_X g_b and D_(g_b)Ric(ℒ_X g_b) = ℒ_X Ric(g_b) = 0. With □^Υ_b = 2δ_(g_b,E_Υ)G_(g_b)δ*_(g_b)
([[eq:iii-d-1-1]]), 2δ_(g_b,E_Υ)G_(g_b)ġ^Υ_b = η_b + □^Υ_b ω̇_b = 0; and then
L_b^(0)ġ^Υ_b = D_(g_b)Ric(ġ^Υ_b) + δ*_(g_b,E_C)δ_(g_b,E_Υ)G_(g_b)ġ^Υ_b = 0 ([[eq:iii-f-1-1]]). Since
δ*_(g_b) ∈ ρDiff¹_b ([[eq:iii-d2-2-1]]) maps 𝒜^ℱ to 𝒜^(1+ℱ), (1) gives [[eq:iii-f3-2-2]].

(3) Linearity is clear. b ↦ ġ_b(ḃ) is smooth into C^∞ ([[eq:iii-b-3-7]] holds smoothly in b), so b ↦ η_b(ḃ) is smooth
into H̄_b^(s−1,α′+2) for every s and α′ < k; [[lem:iii-d2-2-2]] gives ω̇_b, and δ*_(g_b) is smooth in b.

(4) At b_0 the operators δ_(g_(b_0),E_Υ), G_(g_(b_0)) and □^Υ_(b_0) commute with the rotations of x (c_Υ and c_(Υ,H)
are rotation-invariant, [[sec:iii-d2-1]]), and so does (□^Υ_(b_0))^(0)⁻¹, being the inverse of an invertible operator
that commutes with them. The projections onto a type and degree ([[lem:iii-a1-1-6]]) are averages over SO(4) and
commute with all of these; so ω̇_(b_0)(ḃ) and ġ^Υ_(b_0)(ḃ) have the type of ġ_(b_0)(ḃ), which [[lem:iii-f3-1-1]]
gives. A stationary 1-form of vector type 1 is r²B(r)V_i dz^i, and (δ*(r²BV_j dz^j))_(t_s i) =
½∂_(t_s)(r²BV_i) − Γ^j_(t_s i)r²BV_j = 0, the static metric having Γ^j_(t_s i) = 0; so δ* of it leaves f_t
unchanged. ∎

**Remark {#rem:iii-f3-2-3}** (Pure gauge spin changes; [Hin26, Remark 8.10] in dimension 4 + 1.) Let A_V ∈ 𝔰𝔬(4),
V := V(A_V), V_b := g_b(R_(A_V), ·) and W := [A(b), A_V]. Then

    ġ^Υ_b(0, [A(b), A_V]) = 2h_(b,v1)(V),     h_(b,v1)(V) = δ*_(g_b) ω^(−1)_(b,v1)(V)  ([[eq:iii-d2-3-4]]).
                                                                                                         {#eq:iii-f3-2-3}

*Proof.* By [[lem:iii-e1-2-2]], ġ_b(0, W) = D_Ag_b(W) = 2δ*_(g_b)V_b. Let
D := 2V_b + ω̇_b(0, W) − 2ω^(−1)_(b,v1)(V), a stationary 1-form smooth on X̄. Near ∂X, V_b − V = (g_b − ḡ)(R_(A_V), ·)
∈ ρC^∞ (g_b − ḡ ∈ ρ²C^∞, [[eq:iii-d2-2-3]], and R_(A_V) has Cartesian components in ρ⁻¹C^∞),
ω̇_b(0, W) ∈ 𝒜^((2,0)∪(2+ℰ_ind)) and ω^(−1)_(b,v1)(V) − V ∈ 𝒜^((2,0)∪(2+ℰ_ind)) ([[eq:iii-d2-3-2]]); so D ∈ 𝒜^ϵ for
every ϵ < 1. And (□^Υ_b)^(0)D = 2δ_(g_b,E_Υ)G_(g_b)(ġ_b(0, W) + δ*_(g_b)ω̇_b(0, W)) = 2δ_(g_b,E_Υ)G_(g_b)ġ^Υ_b(0, W)
= 0 by [[prop:iii-f3-2-2]] (2) and [[eq:iii-d2-3-3]]. By [[prop:iii-d1-4-1]], D = 0, and
ġ^Υ_b(0, W) = δ*_(g_b)(2V_b + ω̇_b(0, W)) = 2h_(b,v1)(V). ∎

So the spin changes in the image of ad_(A(b)), of dimension 6 − dim ker ad_(A(b)) ∈ {0, 2, 4} ([[lem:iii-e1-2-3]]), are
pure gauge. But for fixed Ȧ = [A, A_V] ≠ 0 and A → 0, ‖A_V‖ ≥ ‖Ȧ‖/(2‖A‖) → ∞, so the gauge potential
2ω^(−1)_(b,v1)(V), whose leading term is 2V, is unbounded as b approaches the Tangherlini parameters. As in [Hin26], the
final angular momentum must therefore be encoded as an element of 𝔰𝔬(4), all six components, and not modulo the pure
gauge changes.

### Stationary solutions on five-dimensional Tangherlini {#sec:iii-f3-3}

On {r > r_h} use the static chart (t_s, r, z) of [[sec:iii-f2-2]] and the time t_*. A stationary symmetric 2-tensor or
1-form on {r > r_0} is *in 𝒜^β near infinity* if its components in the frame (dt_*, dx) are; the frames
(dt_*, dr, r dz) and (dt_s, dr, r dz) differ near infinity by matrices with bounded conormal entries
(t_* = t_s − r_* + c_0 + O(r⁻¹) with all derivatives), so then the coefficients f_ab, f_a, H_L, H_T of each harmonic
([[thm:s15-ki]]), as functions of r, are conormal and O(r^(−β)), and a 1-form ζ = A_aS dy^a + r²BS_i dz^i (or
r²BV_i dz^i) is in 𝒜^(β−1) if A_a and rB are conormal and O(r^(1−β)). The ordinary differential equations below have
regular singular points at r = ∞ (analytic in 1/r) with the stated exponents p_+ > p_− in r. The solution behaving like
r^(p_−) carries no logarithm (in 1/r it belongs to the larger exponent −p_−; Frobenius), and every solution not
proportional to it grows like r^(p_+), possibly with a logarithmic factor; so a solution that is O(r^(−β)) with
−β < p_+ is a multiple of the decaying one.

**Theorem {#thm:iii-f3-3-1}** (Stationary solutions; [AHW24, Theorem 6.1 (2)] on five-dimensional Tangherlini.) Let
β ∈ (0, 1), and let h be a stationary symmetric 2-tensor on {r > r_0}, smooth there, in 𝒜^β near infinity, of one type
and degree, with D_(g_(b_0))Ric(h) = 0 on {r > r_h}. Then there are ḃ = (ṁ, Ȧ), with ṁ = 0 unless the type is scalar
type 0 and Ȧ = 0 unless it is vector type 1, and a stationary 1-form ω on {r > r_0}, smooth, of the same type and
degree, in 𝒜^(β−1) near infinity, with h = ġ_(b_0)(ḃ) + δ*_(g_(b_0))ω on {r > r_h}.

*Proof.* Steps 1–6 find, for each type, a 1-form ω smooth on {r > r_h}, in 𝒜^(β−1) near infinity, with
h = ġ_(b_0)(ḃ) + δ*ω on {r > r_h}; Step 7 makes it smooth on {r > r_0}. A gauge 1-form ζ in 𝒜^(β−1) that is smooth on
{r > r_0} leaves h′ := h + δ*ζ smooth on {r > r_0}, in 𝒜^β and in the kernel of D Ric. The gauge shifts are those of
the proof of [[thm:iii-f2-2-2]] at σ = 0.

*Step 1: tensor type, l ≥ 2.* h = 2r²H T_ij dz^i dz^j. By [[thm:s15-ki]] (T) at σ = 0 (□_2 = ∂_r f ∂_r on functions of
r, D r · D = f∂_r, k_T² + 2 = κ), r⁻³(r³fH′)′ − l(l + 2)r⁻²H = 0, and Φ := r^(3/2)H solves f(fΦ′)′ = V_TΦ,
V_T = (f/r²)(l(l + 2) + 3/4 + 9m_0/(4r²)), with V_T/f positive and bounded on [r_h, ∞); the exponents of H at infinity
are the roots p of p(p + 2) = l(l + 2), l and −(l + 2). H is an angular component, the same in all charts, so smooth on
{r > r_0}; at infinity H = O(r^(−β)) excludes the exponent l, so H = O(r^(−l−2)) and H′ = O(r^(−l−3)). On solutions,
f and V_T being real, (fΦ̄Φ′)′ = f|Φ′|² + V_T|Φ|²/f; the boundary terms vanish at r_h (f = 0, Φ and Φ′ bounded) and at
infinity (O(r^(−2l−2))), so ∫_(r_h)^∞ (f|Φ′|² + V_T|Φ|²/f) dr = 0, Φ = 0, and h = 0.

*Step 2: vector type, l ≥ 2.* h = 2rf_a V_i dy^a dz^i + 2r²H_T V_ij dz^i dz^j. With ζ_0 := r²BV_i dz^i,
B := 2H_T/k_V (smooth on {r > r_0}, rB = O(r^(1−β))), h′ := h + δ*ζ_0 has H′_T = 0 and f′_a = F_a, the invariants
f_a + (r/k_V)D_aH_T. By [[thm:s15-ki]] (V), r²F^a = ε^(ab)D_bΩ. As F is static,
∂_tΩ = r²F^r/ε^(rt) is a function of r, so Ω = αt + Ω_0(r), and ε^(tr)∂_rΩ = r²F^t static forces α to be constant;
the equation for Ω of (V) then gives (k_V² − 2)αt/r² = 0 (□_2 t = 0 and Dr · Dt = 0), so α = 0, F^r = 0 and F_r = 0.
With F_t = ry, r²F^t = −r³y/f = ε^(tr)Ω_0′, and the equation for Ω_0, (fΩ_0′)′ − (3/r)fΩ_0′ − ((k_V² − 2)/r²)Ω_0 = 0,
becomes ∓r³y′ = ((k_V² − 2)/r²)Ω_0; differentiating and using Ω_0′ = ∓r³y/f,

    f(r⁵y′)′ = (k_V² − 2)r³y,     k_V² − 2 = l(l + 2) − 3 ≥ 5;

the exponents of f_t = ry at infinity are l and −(l + 2) (y ∼ r^p with p(p + 4) = (l + 3)(l − 1)). In the ingoing chart
(v, r, z), as f_t dt + f_r dr = f_t dv + (f_r − f_t/f)dr, h_vi = rf_t V_i and h_ri = r(f_r − f_t/f)V_i. So, with
F_r = 0, h′_ri = −rf′_t V_i/f is smooth at r_h: y = f′_t/r is f times a smooth function near r_h, so y → 0 and y′ is
bounded there. At infinity f′_t = O(r^(−β)), so y = O(r^(−l−3)), y′ = O(r^(−l−4)). On solutions
(r⁵ȳy′)′ = r⁵|y′|² + (k_V² − 2)r³|y|²/f, with |y|²/f integrable at r_h and the boundary terms zero at both ends; so
y = 0, h′ = 0 and h = δ*(−ζ_0).

*Step 3: scalar type, l ≥ 2.* h = f_ab S dy^a dy^b + 2rf_a S_i dy^a dz^i + 2r²(H_L γ_ij S + H_T S_ij)dz^i dz^j. With
the gauge 1-form ζ_1 := 2X_a S dy^a + (2r²/k)H_T S_i dz^i, X_a := (r/k)(f_a + (r/k)D_aH_T) ([KI03, (2.8)]; built
covariantly on the orbit space from h, so smooth on {r > r_0}, and O(r^(1−β))), h′ := h + δ*ζ_1 has
f′_a = H′_T = 0, its remaining components being the invariants F_ab, F of [[thm:s15-ki]] (S). By
[[thm:s15-ki]] (S0), Z = 0, that is F_tr = 0; and with X := r(−F_tt/f − 2F), Y := r(fF_rr − 2F) (the X, Y of (S) in the
static chart), [KI03, (4.2)] at n = 3, K = 1, Λ = 0 and f = 1 − m_0/r² (f − 1 = −m_0/r², f′ = 2m_0/r³,
f″ = −6m_0/r⁴) is the flow

    Y′ = m_0(X − Y)/(r(r² − m_0)),
    X′ = (m_0(m_0 − 2r²)X + (k²r²(r² − m_0) + 4m_0r² − 3r⁴)Y)/(m_0 r(r² − m_0)),                         {#eq:iii-f3-3-1}

on which all the equations hold. Define Z̃ := (fr²/k²)(X′ − X/r − (f′/f − 2/r)Y) (the form that [KI03, (2.24a)], derived
there for ω ≠ 0, takes at ω = 0) and H := k² − 3 + 6m_0/r², and put Φ := (3Z̃ − r(X + Y))/(r^(1/2)H). Inserting
[[eq:iii-f3-3-1]] into Z̃ gives, on the flow,

    3Z̃ − r(X + Y) = (−m_0(k²r² + 9r² − 6m_0)X + (3(k² − 3)r⁴ − 2(2k² − 9)m_0r² − 12m_0²)Y)/(k²m_0r),    {#eq:iii-f3-3-2}

and comparing coefficients, Φ = (Q_Y X − Q_X Y)/(2k²r^(1/2)f′H) with Q_X, Q_Y as in [[thm:s15-ki]] (S0) (as f′ = 2m_0/r³,
the right side is r^(5/2)(Q_Y X − Q_X Y)/(4k²m_0H), and r⁴(Q_Y X − Q_X Y)/4 is the numerator of
[[eq:iii-f3-3-2]]). So by (S0), f(fΦ′)′ = V_SΦ with V_S = fQ/(16r²H²), and X and Y are
linear combinations of Φ and Φ′. At infinity V_S = (l(l + 2) + 3/4)r⁻² + O(r⁻⁴) (Q → 16p³ + 60p² = 4p²(4p + 15),
H → p = κ − 3), so the exponents of Φ there are l + 3/2 and −l − 1/2. At r_h: where F_tr = 0, in ingoing components
F_vv = −fF_vr, X = r(F_vr − 2F) and Y = r(fF′_rr + F_vr − 2F) (from F_tt = F_vv, F_tr = F_vv/f + F_vr and
F_rr = F_vv/f² + 2F_vr/f + F′_rr), smooth since h′ is; so by [[eq:iii-f3-3-2]], whose coefficients are polynomials in
r divided by k²m_0r, and H ≥ k² − 3 > 0, Φ is smooth on [r_h, ∞). At infinity X, Y = O(r^(1−β)), so
Φ = O(r^(7/2−β)) by [[eq:iii-f3-3-2]], which excludes the exponent l + 3/2 ≥ 7/2: Φ = O(r^(−l−1/2)),
Φ′ = O(r^(−l−3/2)). As Q > 0 on {r > r_h} for l ≥ 2 ([[sec:iii-f2-2]], *Positivity of the potentials*), V_S > 0 and
V_S/f is bounded; the identity (fΦ̄Φ′)′ = f|Φ′|² + V_S|Φ|²/f gives Φ = 0 as in Step 1; then X = Y = 0, and the
relations of (S) give F^t_t = F^r_r = F = 0, so F_tt = F_rr = F = 0, h′ = 0 and h = δ*(−ζ_1).

*Step 4: scalar type 0.* h = f_ab dy^a dy^b + 2r²H_L γ. δ*(A_t dt_s + A_r dr) shifts H_L by fA_r/(2r) (from
Γ^r_ij = −rfγ_ij) and f_tr by ½A_t′ − Γ^(t)_(tr)A_t = (f/2)(A_t/f)′. Put A_r := −2rH_L/f and
A_t := −f∫_(r_1)^r 2f_tr f⁻¹ dr′, smooth on (r_h, ∞) and O(r^(1−β)) (β < 1); h′ := h + δ*ζ, ζ := A_t dt_s + A_r dr, has
H′_L = f′_tr = 0, is O(r^(−β)) and solves the stationary equations, so by [[cor:s15-low]] (c),
(f′_tt, f′_rr) = c_1(f, 0) + ṁ(r⁻², r⁻²f⁻²). The first is c_1 f dt_s², not O(r^(−β)) unless c_1 = 0. By
[[lem:iii-f3-1-1]], ġ_(b_0)(1, 0) = r⁻²dt_s² + 2r⁻²f⁻¹dt_s dr + r⁻²f⁻²dr², and 2r⁻²f⁻¹dt_s dr = δ*(A^m dt_s) with
A^m := −f∫_r^∞ 2s⁻²f(s)⁻² ds = O(r⁻¹) (δ*(A dt_s) has only the tr component (f/2)(A/f)′). So
h = ṁ ġ_(b_0)(1, 0) + δ*(−ζ − ṁA^m dt_s) on {r > r_h}.

*Step 5: vector type 1.* h = 2rf_a V_i dy^a dz^i, V_ij = 0. By [[thm:s15-ki]] (V1), F^(1)_tr = −r(f_t/r)′ = Lε_tr/r⁴
with L constant, so f_t = ar + b′r⁻³ with constants a, b′, and f_r is unconstrained. δ*(r²BV_i dz^i) shifts f_r by
(r/2)B′ and f_t by 0. Put B := 2∫_∞^r f_r(s)s⁻¹ ds, convergent and O(r^(−β)); then h′ := h − δ*(r²BV_i dz^i) has
f′_r = 0, f′_t = f_t, and is O(r^(−β)), so a = 0. Let Ȧ with V(Ȧ) = (b′/m_0)r²V_i dz^i; by [[lem:iii-f3-1-1]],
k_1 := h − ġ_(b_0)(0, Ȧ) has f_t = 0 and f_r = O(r^(−β)), and with B̃ := 2∫_∞^r f^(k_1)_r(s)s⁻¹ ds,
k_1 − δ*(r²B̃V_i dz^i) has f_t = f_r = 0, so vanishes. Hence h = ġ_(b_0)(0, Ȧ) + δ*(r²B̃V_i dz^i), with
rB̃ = O(r^(1−β)).

*Step 6: scalar type 1.* h = f_ab S dy^a dy^b + 2rf_a S_i dy^a dz^i + 2r²H_L γ_ij S dz^i dz^j, D̂_iD̂_jS = −γ_ij S,
k = 3^(1/2). For stationary ζ = A_tS dt_s + A_rS dr + r²BS_i dz^i, δ*ζ shifts f_tt, f_t, H_L by −(ff′/2)A_r,
−(k/(2r))A_t, (k/6)B + (f/(2r))A_r, free of derivatives, with determinant −m_0(r² − m_0)/(4r⁶) ≠ 0 on (r_h, ∞) (rows
f_tt, f_t, H_L; columns A_t, A_r, B; the determinant of the proof of [[thm:iii-f2-2-2]] at σ = 0), and f_rr, f_r by
A_r′ + m_0A_r/(r(r² − m_0)) and (r²B′ − kA_r)/(2r). Let ζ solve the algebraic system making h + δ*ζ have
f_tt = f_t = H_L = 0; then h + δ*ζ has the form of [[lem:s15-low]] (b) at σ = 0 and solves the stationary equations, so
it vanishes by [[cor:s15-low]] (b), and ω := −ζ has h = δ*ω. Its coefficients satisfy, from the f_t, f_rr and H_L
components of h = δ*ω: A^ω_t = −2rf_t/k = O(r^(1−β)); (f^(1/2)A^ω_r)′ = f^(1/2)f_rr, so
A^ω_r = f^(−1/2)(c + ∫_(r_1)^r f^(1/2)f_rr) = O(r^(1−β)); and B^ω = (6/k)(H_L − (f/(2r))A^ω_r) = O(r^(−β)). So
ω ∈ 𝒜^(β−1) near infinity.

*Step 7: across the horizon.* By [[lem:iii-a1-1-6]] the sectors of Steps 1–6 are all the types and degrees of
symmetric 2-tensors on 𝕊³. In each, h = ġ_(b_0)(ḃ) + δ*ω on {r > r_h} with ω smooth there and in 𝒜^(β−1).
Let ω̃ be the solution on (r_0, ∞), in the
chart (t_*, r, z), of the r-row system of [[lem:iii-f2-2-1]] at σ = 0 for δ*ω̃ = h − ġ_(b_0)(ḃ), whose coefficients
and right side are smooth on (r_0, ∞), with ω̃ = ω at one point r_1 > r_h. By [[lem:iii-f2-2-1]] (a) there, ω̃ = ω on
(r_h, ∞); so ω̃ is smooth on (r_0, ∞) and in 𝒜^(β−1) near infinity. ∎

**Corollary {#cor:iii-f3-3-2}** (Stationary gauge invariants at b_0.) On {r > r_h}, for stationary 1-forms ω: (a) if
ṁ ġ_(b_0)(1, 0) = δ*ω, then ṁ = 0; (b) if ġ_(b_0)(0, Ȧ) = δ*ω, then Ȧ = 0; (c) if ω is of scalar type 1 and δ*ω = 0,
then ω = 0.

*Proof.* At b_0, δ* commutes with the projections onto types and degrees, so in (a) and (b) ω may be replaced by its
scalar type 0, resp. vector type 1, part. (a) For ω = A_t dt_s + A_r dr, the H_L component fA_r/(2r) of δ*ω must
vanish, so A_r = 0, and then the tt component −(ff′/2)A_r vanishes, while that of ġ_(b_0)(1, 0) is r⁻²
([[lem:iii-f3-1-1]]). (b) δ*(r²BV_i dz^i) has f_t = 0 ([[prop:iii-f3-2-2]] (4)), while ġ_(b_0)(0, Ȧ) has
f_t = m_0r⁻³ on r⁻²V(Ȧ) ([[lem:iii-f3-1-1]]). (c) Componentwise in a basis of 𝒮_1, the shifts of f_tt, f_t, H_L
vanish, and their determinant is nonzero (Step 6 of [[thm:iii-f3-3-1]]), so A_t = A_r = B = 0. ∎

### The zero energy kernel and cokernel {#sec:iii-f3-4}

For α ∈ (0, 1] consider

    L_b^(0) : 𝒳_b := {u ∈ H̄_b^(s,α)(X̄; S²T*X) : L_b^(0)u ∈ H̄_b^(s−1,α+2)} → H̄_b^(s−1,α+2)(X̄; S²T*X).
                                                                                                         {#eq:iii-f3-4-1}

Under the pairing ⟨u, v⟩ := ∫_X ⟨u, v⟩_(g_b) |dx|, and |dx| = ρ⁻⁴μ_b, the dual of H̄_b^(s−1,α+2) is Ḣ_b^(1−s,2−α)
([Hin26, footnote 79] in dimension 4 + 1).

**Proposition {#prop:iii-f3-4-1}** (Kernel and cokernel at zero energy; [Hin26, Proposition 8.11] in dimension 4 + 1.)
For b near b_0 and every α ∈ (0, 1], [[eq:iii-f3-4-1]] is Fredholm of index 0, and:

(1) (*Kernel.*) Its nullspace is eleven-dimensional, spanned by

    ġ^Υ_b(1, 0) ∈ 𝒜^((2,0)∪(2+ℰ_ind)),   ġ^Υ_b(0, Ȧ) ∈ 𝒜^((3,0)∪(3+ℰ_ind)) (Ȧ ∈ 𝔰𝔬(4)),
    h_(b,s1)(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)) (S ∈ 𝒮_1),                                                         {#eq:iii-f3-4-2}

of [[prop:iii-f3-2-2]] and [[eq:iii-d2-3-4]]; all lie in ker δ_(g_b,E_Υ)G_(g_b).

(2) (*Cokernel.*) The annihilator of its range in Ḣ_b^(1−s,2−α) is the kernel there of L_b^(0)*, and is
eleven-dimensional, spanned by the dual states of [[prop:iii-e-3-1]] (2),

    h*_(b,s0),     h*_(b,s1)(S) (S ∈ 𝒮_1),     h*_(b,v1)(V) (V ∈ 𝒱_1).                                   {#eq:iii-f3-4-3}

*Proof.* *Step 0: the index.* L_b^(·) satisfies (H1)–(H5) with index 0 at σ ≠ 0 ([[cor:iii-f2-1-2]]), (G) with the
weight α − 2 of [[ch:s03]], since α ∈ (0, β^L_+) ([[sec:iii-f3-1]]), and (TF) with the weight α ([[prop:iii-f1-3-3]]);
so [[eq:iii-f3-4-1]] has index 0 by [[cor:i-c-6-6]]. By [[thm:i-c-3-1]] (1)–(2) it is Fredholm, the annihilator of its
range is the kernel of the adjoint on the dual domain, and every element of its nullspace is smooth up to ∂_♯X and lies
in 𝒜^β near ∂X for every β < β^L_+ (the upper end of the gap containing α). The pairing with |dx| and g_b in place of
that of [[ch:s03]] identifies the adjoints' kernels by an invertible bundle map, smooth on X̄.

*Step 1: the states and the dual states.* By [[prop:iii-f3-2-2]] (2) and [[prop:iii-d2-3-1]] (2), the tensors
[[eq:iii-f3-4-2]] lie in ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b) ⊂ ker L_b^(0), and, being smooth on X̄ and O(ρ²), in
H̄_b^(s,α) for α < 2. For the adjoint: G := G_(g_b) = Id − ½g_b tr_(g_b) is self-adjoint and invertible,
G⁻¹ = Id − ⅓g_b tr_(g_b) in five dimensions ([[lem:iii-b-6-2]]), and G ∘ D_(g_b)Ric is formally self-adjoint. Indeed,
for symmetric 2-tensors h, k compactly supported in the interior of M and small s, t, put g_(s,t) := g_b + sh + tk and
F(s, t) := ∫_M R(g_(s,t)) |dg_(s,t)|; the integrand vanishes outside supp h ∪ supp k, where g_(s,t) = g_b and
R(g_b) = 0, so F is finite and smooth. The first variation formula, whose divergence term integrates to 0, gives
∂_tF(s, 0) = −∫_M ⟨G_(g_(s,0))Ric(g_(s,0)), k⟩_(g_(s,0)) |dg_(s,0)|; differentiating in s at s = 0, every term in which
the derivative falls elsewhere than on Ric contains Ric(g_b) = 0, so ∂_s∂_tF(0, 0) = −∫_M ⟨G D_(g_b)Ric(h), k⟩ |dg_b|.
This is symmetric in h and k, as ∂_s∂_tF = ∂_t∂_sF. So (D_(g_b)Ric)* = G D_(g_b)Ric G⁻¹ and

    L_b* = G D_(g_b)Ric G⁻¹ + G(δ_(g_b,E_Υ))*(δ*_(g_b,E_C))*.                                            {#eq:iii-f3-4-4}

For h* = Gδ*_(g_b)ω* with ω* ∈ ker(□^C_b)*, using D_(g_b)Ric ∘ δ*_(g_b) = 0 and
(□^C_b)* = 2(δ*_(g_b,E_C))*Gδ*_(g_b) (from □^C_b = 2δ_(g_b)Gδ*_(g_b,E_C), [[eq:iii-e-1-2]]),
L_b*h* = G(δ_(g_b,E_Υ))* ½(□^C_b)*ω* = 0. The dual states [[eq:iii-f3-4-3]] are of this form ([[prop:iii-e-3-1]]),
stationary, so in the kernel of L_b^(0)* = (L_b*)^(0) ([[sec:iii-f3-1]]), and they lie in
Ḣ_b^(0,((3,0),C_0+3)) ⊂ Ḣ_b^(1−s,2−α) (2 − α < 3, s ≥ 1; they vanish on {r_0 < |x| < r_h}). By Step 0 they annihilate
the range.

*Step 2: the dual states are independent, for every b.* Let
a h*_(b,s0) + h*_(b,s1)(S) + h*_(b,v1)(V) = 0, and ω := aω*^(0)_(b,s0) + ω*^(0)_(b,s1)(S) + ω*^(−1)_(b,v1)(V). Then
δ*_(g_b)ω = 0: ω is a Killing 1-form of g_b on X°, which vanishes on {r_0 < |x| < r_h} ([[prop:iii-e-3-1]] (2)),
hence everywhere (∇∇ω is a linear expression in ω through the curvature, so ω is determined by (ω, ∇ω) at one point of
the connected X°). By [[eq:iii-e-3-1]] and [[eq:iii-d2-3-2]], near ∂X, ω = χ(−a dt̄ + ξ_S · dx + V) + ω_2 with
|x|S = ξ_S · x and ω_2 partially polyhomogeneous with index set (2, 0); V has Cartesian components homogeneous of degree
1, and dt̄ = dt_* + d|x| and the dx^i are independent on ∂X. So ω = 0 forces V = 0, then a = 0 and ξ_S = 0.

*Step 3: the kernel at b_0.* Let u be in the nullspace of [[eq:iii-f3-4-1]] at b_0, and fix β ∈ (0, 1), so that
u ∈ 𝒜^β near ∂X, smooth up to ∂_♯X (Step 0).

(i) *The gauge 1-form.* η := δ_(g,E_Υ)Gu ∈ 𝒜^(1+β), smooth up to ∂_♯X. The linearised second Bianchi identity
δ_g G_g D_g Ric = 0 gives δ_g G_g L_(b_0) = ½□^C δ_(g,E_Υ)G_g, so (□^C)^(0)η = 0. As η ∈ H̄_b^(s′,1) for every s′,
which is the Euclidean weight −1, and −1 + 2 ∈ [−C_0, 2), [[thm:iii-e-1-1]] (2) gives η = 0. So D_(g_(b_0))Ric(u) = 0
and δ_(g_(b_0),E_Υ)G_(g_(b_0))u = 0.

(ii) *Harmonics.* Both operators commute with the rotations at b_0 (proof of [[prop:iii-f3-2-2]] (4)), so each
component u_π of a type and degree π ([[lem:iii-a1-1-6]]) lies in both kernels, is smooth on {r > r_0} and in 𝒜^β. By
[[thm:iii-f3-3-1]], u_π = ġ_(b_0)(ḃ_π) + δ*ω_π on {r > r_h}, with ω_π of type π, smooth on {r > r_0}, in 𝒜^(β−1). Let
ω′_π := ω_π − ω̇_(b_0)(ḃ_π), of type π ([[prop:iii-f3-2-2]] (4)) and in 𝒜^(β−1) ([[prop:iii-f3-2-2]] (1)). Then
u_π = ġ^Υ_(b_0)(ḃ_π) + δ*ω′_π on {r > r_h}, and applying 2δ_(E_Υ)G, □^Υ_(b_0)ω′_π = 0 there.

(iii) *Inside the horizon.* [[lem:iii-f2-2-3]] at σ = 0, with Q = □^Υ_(b_0), gives ω̃_π, smooth on
{r > r_0 − δ_0}, so up to {r = r_0}, equal to ω′_π on {r ≥ r_h}, with (□^Υ_(b_0))^(0)ω̃_π = 0 on all of X̄.

(iv) *The expansion at infinity.* Near ∂X, (□^Υ_(b_0))^(0) = ρ²A with A elliptic, and ω̃_π ∈ H_b^(∞,a) for every
a < β − 1; take a ∈ (−1, β − 1). [[lem:iii-a-1-4]], applied as in the proof of [[lem:iii-d1-5-1]] (2), with F = ∅ (as
Aω̃_π = 0 there) and a weight ϵ ∈ (0, ι^Υ_(s1,2)), gives ω̃_π ∈ H_b^(∞,(E,ϵ)) with E built from the roots of real part
> a. By [[lem:iii-d-4-1]] the only root with real part in (a, ϵ) ⊂ (−1, ι^Υ_(s1,2)) is 0, at scalar types 0 and 1 only,
and it is simple; so ω̃_π = χw_0 + w_ϵ with w_ϵ ∈ H_b^(∞,ϵ) ⊂ 𝒜^ϵ and w_0 an indicial solution for the root 0 of
type π: by [[lem:iii-d-4-1]], w_0 = c dt̄ at scalar type 0, w_0 = d(|x|S′) (S′ ∈ 𝒮_1) at scalar type 1, and w_0 = 0
otherwise.

(v) *Mode stability.* Let D_π := ω̃_π + c ω^(0)_(b_0,s0), resp. ω̃_π − ω^(0)_(b_0,s1)(S′), resp. ω̃_π (recall
ω̄^(0)_s0 = −dt̄). By [[eq:iii-d2-3-2]]–[[eq:iii-d2-3-3]], D_π ∈ 𝒜^(ϵ′) for some ϵ′ > 0, smooth on X̄, and
(□^Υ_(b_0))^(0)D_π = 0; [[prop:iii-d1-4-1]] gives D_π = 0. As δ*ω^(0)_(b_0,s0) = 0 and
δ*ω^(0)_(b_0,s1)(S′) = h_(b_0,s1)(S′), on {r ≥ r_h}

    u_π = ġ^Υ_(b_0)(ḃ_π) + h_(b_0,s1)(S′_π),                                                             {#eq:iii-f3-4-5}

with ḃ_π = 0 except at scalar type 0 and vector type 1, and S′_π = 0 except at scalar type 1.

(vi) *The interior.* k_π := u_π − ġ^Υ_(b_0)(ḃ_π) − h_(b_0,s1)(S′_π) lies in ker D Ric ∩ ker δ_(E_Υ)G, so P′k_π = 0
with 2P′ = □ + 2δ*E^ΥG of principal part □, and k_π = 0 on {r > r_h}; by part (d) of the proof of [[prop:iii-d-6-2]],
as in the proof of [[prop:iii-f2-3-1]] (*The interior*), k_π = 0 on {r > r_0}.

So u_π = 0 except at scalar types 0 and 1 and vector type 1, and u, the convergent sum of its components
([[lem:iii-a1-1-6]]), lies in the span of [[eq:iii-f3-4-2]] at b_0.

*Step 4: independence at b_0.* Suppose ġ^Υ_(b_0)(ṁ, Ȧ) + h_(b_0,s1)(S) = 0. First, ω^(0)_(b_0,s1)(S) is of scalar type
1: with Π the projection onto scalar type 1, Πω^(0)_(b_0,s1)(S) lies in ker (□^Υ_(b_0))^(0) and differs from d(|x|S) by
an element of 𝒜^ϵ, as ω^(0)_(b_0,s1)(S) does, so the two differ by an element of 𝒜^ϵ ∩ ker (□^Υ_(b_0))^(0) = 0. So by
[[prop:iii-f3-2-2]] (4) the three summands are of scalar type 0, vector type 1 and scalar type 1, and each vanishes.
ġ^Υ_(b_0)(ṁ, 0) = 0 means ṁ ġ_(b_0)(1, 0) = δ*(−ω̇_(b_0)(ṁ, 0)), so ṁ = 0 ([[cor:iii-f3-3-2]] (a)); likewise Ȧ = 0
([[cor:iii-f3-3-2]] (b)); and δ*ω^(0)_(b_0,s1)(S) = 0 gives ω^(0)_(b_0,s1)(S) = 0 on {r > r_h}
([[cor:iii-f3-3-2]] (c)), so its leading term d(|x|S) vanishes and S = 0. With Step 3, the nullspace at b_0 is
eleven-dimensional and spanned by [[eq:iii-f3-4-2]]. By Step 0 the annihilator of the range has dimension 11, and by
Steps 1–2 it is spanned by [[eq:iii-f3-4-3]].

*Step 5: near b_0.* Fix f*_j, f♯_j as in [[cor:iii-f3-4-2]]. At b_0, L̃_(b_0) of [[cor:iii-f3-4-2]] is invertible: if
L_(b_0)^(0)u + Σ_j c_j f♯_j = 0 and ⟨u, f*_j⟩ = 0 for all j, pairing with the annihilator of the range (Step 4) gives
c = 0, so u is in the nullspace and u = 0; and L̃_(b_0) has index 0, being a finite rank perturbation of
L_(b_0)^(0) ⊕ 0_(ℂ¹¹→ℂ¹¹). This is (Z_𝒫) of [[ch:s03]] for L_(b_0)^(·), with m_1 = m_2 = 11 and the compactly
supported f♯_j, f*_j; by [[thm:i-c-7-1]] (1) it holds for b near b_0, so L̃_b is invertible. Then
u ↦ (⟨u, f*_j⟩)_j is injective on the nullspace of [[eq:iii-f3-4-1]] at b (L̃_b(u, 0) = 0 otherwise), so its dimension
is at most 11. The eleven states [[eq:iii-f3-4-2]] depend continuously on b in H̄_b^(s−1,α) ([[prop:iii-f3-2-2]] (3);
[[prop:iii-d2-3-1]], smooth in b), so the matrix (⟨u_i(b), f*_j⟩)_(ij), invertible at b_0 by Step 4 and the choice of
f*_j, stays invertible near b_0: the states are independent, hence a basis. By index 0 the annihilator of the range has
dimension 11, and by Steps 1–2 it is spanned by [[eq:iii-f3-4-3]]. ∎

**Corollary {#cor:iii-f3-4-2}** (The right inverse at zero energy; [Hin26, Corollary 8.13] in dimension 4 + 1.) Fix
f*_j, f♯_j ∈ C_c^∞(X°; S²T*X), j = 1, …, 11, real, such that u ↦ (⟨u, f*_j⟩)_j and u* ↦ (⟨f♯_j, u*⟩)_j restrict to
isomorphisms of the nullspace of [[eq:iii-f3-4-1]] at b_0, resp. of the annihilator of its range, onto ℂ¹¹. Define

    L̃_b(u, c) := (L_b^(0)u + Σ_(j=1)^11 c_j f♯_j, (⟨u, f*_j⟩)_(j=1,…,11)).                              {#eq:iii-f3-4-6}

(1) (*Invertibility.*) For b near b_0, L̃_b : 𝒳_b ⊕ ℂ¹¹ → H̄_b^(s−1,α+2) ⊕ ℂ¹¹ is invertible, with ‖L̃_b⁻¹‖ bounded near
b_0; and if b ↦ (f_b, c_b) is of class C^k into 𝒜^(α+2)(X̄; S²T*X) ⊕ ℂ¹¹, then b ↦ L̃_b⁻¹(f_b, c_b) is of class C^k
into 𝒜^(α−ϵ) ⊕ ℂ¹¹ for every ϵ ∈ (0, α).

(2) (*Inversion of L_b^(0).*) If f ∈ 𝒜^(α+2) is orthogonal to the dual states [[eq:iii-f3-4-3]] and
(u, c) = L̃_b⁻¹(f, 0), then c = 0 and L_b^(0)u = f; if f depends smoothly on b and the orthogonality holds for all b,
then u depends smoothly on b.

*Proof.* The f*_j, f♯_j exist: the nullspace and the annihilator are finite-dimensional spaces of distributions on X°
(smooth tensors, by Step 0 of the proof of [[prop:iii-f3-4-1]]), and the restriction of C_c^∞(X°) → W* to a
finite-dimensional W ⊂ 𝒟′(X°) is onto, since otherwise a nonzero element of W would annihilate every test section; real
ones suffice, the spaces being spanned by real tensors.

(1) Invertibility near b_0 is Step 5 of the proof of [[prop:iii-f3-4-1]]. *Uniform bound.* Otherwise there are
b_j → b_0 and (u_j, c_j) with ‖u_j‖_(H̄_b^(s,α)) + |c_j| = 1 and L̃_(b_j)(u_j, c_j) → 0. By [[thm:i-c-7-1]] (2) the
estimate [[eq:i-c-3-2]] of [[thm:i-c-3-1]] holds uniformly near b_0:
‖u_j‖_(H̄_b^(s,α)) ≤ C(‖L_(b_j)^(0)u_j‖_(H̄_b^(s−1,α+2)) + ‖u_j‖_(H̄_b^(−N,−N))). Passing to a subsequence,
u_j → u weakly in H̄_b^(s,α) and strongly in H̄_b^(−N,−N) (compact inclusion), and c_j → c; since
L_(b_j)^(0) − L_(b_0)^(0) → 0 as maps H̄_b^(s,α) → H̄_b^(s−2,α+2), L̃_(b_0)(u, c) = 0, so (u, c) = 0; then
‖L_(b_j)^(0)u_j‖ ≤ |c_j| max_k ‖f♯_k‖ + o(1) → 0 and the estimate give ‖u_j‖_(H̄_b^(s,α)) → 0, contradicting the
normalisation. *Smoothness.* As in the proof of [[lem:iii-d2-2-2]]: the coefficients of L̃_b depend smoothly on b, so
b ↦ L̃_b⁻¹w is continuous for fixed w in ⋂_s H̄_b^(s−1,α′+2) ⊕ ℂ¹¹ (α′ := α − ϵ ∈ (0, 1], for which all of the above
holds), uniformly on bounded sets, and the difference quotients converge to L̃_b⁻¹(ẇ − L̃̇ L̃_b⁻¹w); induction gives
C^k. Finally 𝒜^(α+2) ⊂ ⋂_s H̄_b^(s−1,α′+2) near ∂X (with smoothness up to ∂_♯X) and ⋂_s H̄_b^(s,α′) ⊂ 𝒜^(α′).

(2) Pairing L_b^(0)u + Σ_j c_j f♯_j = f with each dual state h*_i(b) of [[eq:iii-f3-4-3]], which annihilate the range
([[prop:iii-f3-4-1]] (2)), gives Σ_j c_j ⟨f♯_j, h*_i(b)⟩ = ⟨f, h*_i(b)⟩ = 0. The matrix (⟨f♯_j, h*_i(b)⟩) is
invertible at b_0 by the choice of f♯_j, and depends continuously on b ([[prop:iii-e-3-1]] and [[prop:iii-e1-3-1]]:
the dual states are continuous in b in Ḣ_b^(0,C_0+3), resp. Ḣ_b^(0,((3,0),C_0+3))), so it is invertible near b_0 and
c = 0. Smoothness follows from (1). ∎

### The setting of the pairings {#sec:iii-f4-1}

This section and the next four carry the pairings of [Hin26, Lemma 8.12] (p. 157) and [Hin26, Lemma 8.15]
(pp. 158–159) and the physical large zero energy states of [Hin26, Proposition 8.14] (pp. 158–163) that the expansion
at low energies needs. [Hin26] proves Lemma 8.12 by reducing each pairing to a pairing at infinity of leading terms,
through [Hin24b, Lemma 3.17] and [Hin23b, Theorem 9.6]; here the reduction is written out ([[lem:iii-f4-2-2]]) and the
pairings at infinity are computed ([[lem:iii-f4-3-1]]). The vector type pairing of Lemma 8.15 is obtained on all of
𝔰𝔬(4) from [[rem:iii-f3-2-3]] and the spin independence of its leading terms. [Hin26, Proposition 8.14] is proved at
the root −2 for scalar, vector and tensor type 2, the last absent in dimension 3 + 1; its Step 2 is modified, because
in dimension 4 + 1 the vanishing of the centre-of-mass pairings against the rotations' dual states, which [Hin26]'s Step
2 uses, is not available away from b_0.

The parameters, the unweighted b-density μ_b, ε_Υ, ℰ_ind, |dg_b| = |dt_*| |dx| and the pairing
⟨u, v⟩ := ∫_X ⟨u, v⟩_(g_b) |dx| (real, bilinear) are those of [[sec:iii-f3-1]]; adjoints and transposes on X are taken
with respect to it. χ_R(x) := χ_1(|x|/R) with χ_1 ∈ C_c^∞([0, 2)) equal to 1 on [0, 1]; it is 1 near the black hole and
0 near infinity, and |dχ_R| ≤ CR⁻¹ is supported in {R ≤ |x| ≤ 2R}.

*Spins.* For A ∈ 𝔰𝔬(4) let V(A) := (Ax) · dx, the Euclidean dual of the rotation field R_A = (Ax) · ∂_x, and for
V ∈ 𝒱_1 let A_V be the element with V(A_V) = V ([[sec:iii-f3-1]]). ⟨A, B⟩_F := ½tr(AᵀB), so that the
E_ij := e_ie_jᵀ − e_je_iᵀ, i < j, are orthonormal; ad_A is skew for it, ⟨[A, X], Y⟩_F = −⟨X, [A, Y]⟩_F
([[prop:np-10-34-iv]] (b)). For S ∈ 𝒮_1, ξ_S ∈ ℝ⁴ is given by |x|S = ξ_S · x. The dual states are
h*_(b,•) = G_(g_b)δ*_(g_b)ω*_(b,•) ([[prop:iii-e-3-1]]), with leading terms ω̄_s0 = −dt̄, ω̄_s1(S) = ξ_S · dx and V;
and h*_(b,v1)(V) = h♯_(b,v1)([A(b), A_V]) + h♭_(b,v1)(V) ([[prop:iii-e1-3-1]]).

*Weights.* Each 1-form and tensor below is stationary, smooth on X (or, for the dual states, in Ḣ¹_b, resp. Ḣ⁰_b, and
zero on {r_0 < |x| < r_h}), and conormal near ∂X; its *weight* is the largest a with the object in 𝒜^a up to the
leading terms named. The weights used are: ġ^Υ_b(1, 0) 2, ġ^Υ_b(0, Ȧ) 3, h_(b,s1)(S) and h_(b,v1)(V) 3,
h̆¹_(b,s1)(S) 2, h̆¹_(b,v1)(V) and h̆²_(b,s1)(S) −1 ([[eq:iii-f3-4-2]], [[eq:iii-d2-3-4]], [[prop:iii-d3-3-1]]);
ω*_(b,s0), ω*_(b,s1)(S) 0 and ω*_(b,v1)(V) −1; h*_(b,s1), h*_(b,v1) and h♯_(b,v1) 3, and h*_(b,s0), h♭_(b,v1) in
Ḣ_b^(0,C_0+3) ([[eq:iii-e-3-2]], [[eq:iii-e1-3-3]]).

### The pairings at infinity {#sec:iii-f4-2}

A stationary operator on M is P = P_0 + P_1∂_(t_*) + P_2∂²_(t_*) with P_j operators on X; on stationary sections
P^(0) = P_0, [P, t_*] = P_1 and ½[[P, t_*], t_*] = P_2, and
P(½t_*²v + t_*v̆) = ½t_*²P_0v + t_*(P_1v + P_0v̆) + (P_2v + P_1v̆) for stationary v, v̆.

**Lemma {#lem:iii-f4-2-1}** Let P := D_(g_b)Ric, G := G_(g_b), and k(ω) := dt_* ⊗_s ω.

(1) GP_0 and GP_2 are symmetric and GP_1 is antisymmetric on X (as differential operators).

(2) For every stationary 1-form ω: P_0δ*ω = 0, P_1δ*ω = −P_0k(ω) and P_2δ*ω = −P_1k(ω).

*Proof.* (1) G ∘ P is formally self-adjoint on M ([[eq:iii-f3-4-4]]), and |dg_b| = |dt_*| |dx|, so
GP = Σ_j GP_j ∂^j_(t_*) has adjoint Σ_j (−∂_(t_*))^j (GP_j)ᵀ; comparing coefficients, (GP_j)ᵀ = (−1)^j GP_j. (2)
P ∘ δ* = 0 ([[prop:iii-f3-2-2]] (2)), and δ*(fω) = fδ*ω + df ⊗_s ω. Apply P to δ*(t_*ω) = t_*δ*ω + k(ω) and to
δ*(½t_*²ω) = ½t_*²δ*ω + t_*k(ω), expand by the formula above, and read off the coefficients of t_*⁰. ∎

**Lemma {#lem:iii-f4-2-2}** (Reduction to infinity.) Let L := L_b, L_j its coefficients as above, ω* one of the dual
1-forms of [[sec:iii-f4-1]], of weight c, and h* := Gδ*ω*, of weight c* ≥ 3. Write k := k(ω*).

(1) (*First order.*) If u ∈ ker (D_(g_b)Ric)^(0) ∩ ker δ_(g_b,E_Υ)G has weight a ≥ 2, then

    ⟨L_1u, h*⟩ = lim_(R→∞) ⟨[P_0, χ_R]u, Gk⟩.                                                            {#eq:iii-f4-2-1}

(2) (*Second order.*) If h, h̆ have weights a ≥ 3, ă ≥ 2, and h, t_*h + h̆ lie in ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G,
then L_2h + L_1h̆ = L(½t_*²h + t_*h̆) is stationary and

    ⟨L_2h + L_1h̆, h*⟩ = lim_(R→∞) ⟨[P_1, χ_R]h + [P_0, χ_R]h̆, Gk⟩.                                     {#eq:iii-f4-2-2}

(3) (*What the limits see.*) Let R_1(u), R_2(h, h̆) denote the right sides of [[eq:iii-f4-2-1]], [[eq:iii-f4-2-2]],
for u with P_0u = 0 of weight a ≥ 2, resp. pairs with P_0h = 0 = P_1h + P_0h̆ of weights a ≥ 3, ă ≥ 2, and put
e_1 := a + c − 2, e_2 := min(a − 3, ă − 2) + c. The limits exist and equal ⟨P_1u, h*⟩, resp. ⟨P_2h + P_1h̆, h*⟩. If
e_i > 0 they vanish; if e_i = 0 they are the same integrals computed with the leading terms of the arguments, of ω*, of
P_j, G and t_* alone, which do not depend on R; if e_i < 0 the leading terms do not determine them. R_1 vanishes on δ*ζ
and R_2 on (δ*ζ, δ*ζ̆ + k(ζ)), for stationary ζ ∈ 𝒜^(a−1), ζ̆ ∈ 𝒜^(ă−1) smooth on X; and R_1(u), R_2(h, h̆) do not change
when t_* is replaced by t_* + φ, φ smooth on X and in |x|C^∞(X̄) near ∂X, the pair being rewritten as (h, h̆ − φh).

*Proof.* In every pairing below one factor is smooth and supported in {|x| ≤ 2R} and the other vanishes on
{r_0 < |x| < r_h}, so integrations by parts on X produce no boundary terms; the dual states have finite regularity, and
the pairings are distributional. Near ∂X, χ_R is a function of ρR, so [P_0, χ_R] ∈ ρ²Diff¹_b, [P_1, χ_R] ∈ ρDiff⁰_b and
[P_0ᵀ, χ_R] ∈ ρ²Diff¹_b, with coefficients bounded uniformly in R and supported in {R ≤ |x| ≤ 2R}
(P_1 ∈ ρDiff¹_b, [[lem:iii-f-2-1]]); and |dx| = ρ⁻⁴μ_b. So a pairing over that annulus of [P_0, χ_R] or [P_0ᵀ, χ_R]
applied to weight w against weight w′ is O(R^(2−w−w′)), and of [P_1, χ_R] is O(R^(3−w−w′)). Also
P_0ᵀh* = GP_0G⁻¹h* = GP_0δ*ω* = 0 and (δ*_(E_C))*h* = ½(□^C_b)*ω* = 0 (Step 1 of the proof of [[prop:iii-f3-4-1]]).

(1) L = P + δ*_(E_C)δ_(E_Υ)G, and [δ*_(E_C)δ_(E_Υ)G, t_*]u = δ*_(E_C)ϑ with ϑ := [δ_(E_Υ)G, t_*]u of weight a, since
δ_(E_Υ)Gu = 0; and ⟨δ*_(E_C)ϑ, h*⟩ = lim_R ⟨ϑ, [(δ*_(E_C))*, χ_R]h*⟩ = O(R^(3−a−c*)) → 0. The pairing ⟨P_1u, h*⟩
converges absolutely and equals lim_R ⟨P_1(χ_Ru), h*⟩ (the commutator term is O(R^(3−a−c*))), and by
[[lem:iii-f4-2-1]],

    ⟨P_1(χ_Ru), Gδ*ω*⟩ = −⟨χ_Ru, GP_1δ*ω*⟩ = ⟨χ_Ru, GP_0k⟩ = ⟨GP_0(χ_Ru), k⟩ = ⟨[P_0, χ_R]u, Gk⟩,

the last as P_0u = 0.

(2) The expansion formula and Lh = 0, L(t_*h + h̆) = 0 give L(½t_*²h + t_*h̆) = L_2h + L_1h̆. As δ_(E_Υ)G is of first
order, δ_(E_Υ)G(½t_*²h + t_*h̆) = t_*δ_(E_Υ)G(t_*h + h̆) + [δ_(E_Υ)G, t_*]h̆ = [δ_(E_Υ)G, t_*]h̆ =: ϑ, of weight ă; so
L(½t_*²h + t_*h̆) = P_2h + P_1h̆ + δ*_(E_C)ϑ, and the last term pairs to O(R^(3−ă−c*)) → 0 with h* as in (1). By
[[lem:iii-f4-2-1]], with commutator terms O(R^(3−ă−c*)),

    ⟨P_2(χ_Rh) + P_1(χ_Rh̆), Gδ*ω*⟩ = ⟨χ_Rh, GP_2δ*ω*⟩ − ⟨χ_Rh̆, GP_1δ*ω*⟩ = −⟨χ_Rh, GP_1k⟩ + ⟨χ_Rh̆, GP_0k⟩
        = ⟨G(P_1(χ_Rh) + P_0(χ_Rh̆)), k⟩ = ⟨[P_1, χ_R]h + [P_0, χ_R]h̆, Gk⟩,

using P_1h + P_0h̆ = 0, the t_*⁰ coefficient of P(t_*h + h̆) = 0.

(3) The identity chains of (1)–(2) used only P_0u = 0, resp. P_0h = 0 = P_1h + P_0h̆, so R_1(u) = ⟨P_1u, h*⟩ and
R_2(h, h̆) = ⟨P_2h + P_1h̆, h*⟩, absolutely convergent. The leading terms: by the counting above the terms of R_1 are
O(R^(−e_1)) and those of R_2 are O(R^(−(a+c−3))) and O(R^(−(ă+c−2))); every correction to a leading term (of the
arguments, of ω*, of P_j and G by ρ²; dt_* is exact) raises a weight, and the model operators are homogeneous under
dilations, so at e_i = 0 the leading integral does not depend on R. *Gauge.* P_1δ*ζ = −P_0k(ζ) ([[lem:iii-f4-2-1]]),
and ⟨P_0k(ζ), h*⟩ = lim_R ⟨k(ζ), [P_0ᵀ, χ_R]h*⟩ = O(R^(3−a−c*)) → 0. For the pair,
P_2δ*ζ + P_1(δ*ζ̆ + k(ζ)) = −P_1k(ζ) − P_0k(ζ̆) + P_1k(ζ) = −P_0k(ζ̆), which pairs to O(R^(3−ă−c*)) → 0. *Time
function.* |dg_b| = |d(t_* + φ)| |dx| and [[lem:iii-f4-2-1]] holds for t_* + φ. With t̃ := t_* + φ, t̃u = t_*u + φu, so
the first-order coefficient changes by [P_0, φ]u = P_0(φu), and ⟨P_0(φu), h*⟩ = lim_R ⟨φu, [P_0ᵀ, χ_R]h*⟩
= O(R^(3−a−c*)) → 0. And ½t̃²h + t̃(h̆ − φh) = ½t_*²h + t_*h̆ + (φh̆ − ½φ²h), so the second-order quantity changes by
P_0(φh̆ − ½φ²h), of weight ≥ min(ă − 1, a − 2) ≥ 1 before P_0, which pairs to O(R^(1−c*)) → 0. ∎

*The leading-term integrals as fluxes.* At excess 0 we compute R_1 and R_2 with the time function t̄ = t_* + |x| of
Minkowski space (allowed by [[lem:iii-f4-2-2]] (3)), in which stationary means independent of t̄ at fixed x, and with
leading terms that solve the Minkowski equations on ℝ⁴ ∖ 0. On Minkowski space,
D Ric(W)_μν = ½(∂^ρ∂_μW_νρ + ∂^ρ∂_νW_μρ − ∂^ρ∂_ρW_μν − ∂_μ∂_ν tr W). For a stationary w (indices i, j, k spatial,
Cartesian, summed; tr w = −w_t̄t̄ + w_kk), P_0w = D Ric(w) and P_1w = D Ric(t̄w) − t̄ D Ric(w), where one derivative
falls on t̄; so

    (P_0w)_t̄t̄ = −½Δw_t̄t̄,   (P_0w)_t̄i = ½(∂_i∂_jw_t̄j − Δw_t̄i),   tr P_0w = ∂_i∂_jw_ij − Δ tr w,
    (P_1w)_t̄t̄ = ∂_jw_t̄j,   (P_1w)_t̄i = ½(∂_jw_ij − ∂_iw_kk),   tr P_1w = −2∂_jw_t̄j.                   {#eq:s15-p0p1}

For leading terms with P_0u = 0 on ℝ⁴ ∖ 0, [P_0, χ_R]u = P_0(χ_Ru), supported in {R ≤ |x| ≤ 2R}; likewise
[P_1, χ_R]h + [P_0, χ_R]h̆ = P_1(χ_Rh) + P_0(χ_Rh̆) when P_1h + P_0h̆ = 0. If the integrand is a divergence ∂_jY^j(·)
of an expression Y linear in its argument and first derivatives, then, as χ_R = 1 near {|x| ≤ R} and vanishes near
{|x| = 2R}, the integral over the annulus is −∮_(|x|=R) Y(u) · n dS, n = x/|x|. Three cases occur.

(a) ω* = −dt̄ (the s0 dual state). k = −dt̄², tr k = 1, Gk = −dt̄² − ½ḡ is constant, and ⟨T, Gk⟩ = −T_t̄t̄ − ½tr T. By
[[eq:s15-p0p1]], ⟨P_0w, Gk⟩ = ½∂_i(∂_iw_kk − ∂_jw_ij) and ⟨P_1w, Gk⟩ = 0. So

    R_1(u) = −½∮(∂_iu_kk − ∂_ju_ij)n_i dS,     R_2(h, h̆) = −½∮(∂_ih̆_kk − ∂_jh̆_ij)n_i dS.

(b) ω* = q · dx, q ∈ ℝ⁴ (the s1 dual states). k = dt̄ ⊗_s q · dx, tr k = 0, Gk = k is constant, ⟨T, k⟩ = −q_iT_t̄i,
⟨P_0w, k⟩ = −½q_i∂_j(∂_iw_t̄j − ∂_jw_t̄i) and ⟨P_1w, k⟩ = −½q_i∂_j(w_ij − δ_ijw_kk). So

    R_1(u) = ½∮q_i(∂_iu_t̄j − ∂_ju_t̄i)n_j dS,     R_2(h, h̆) = ½∮q_i(h_ij − δ_ijh_kk + ∂_ih̆_t̄j − ∂_jh̆_t̄i)n_j dS.

(c) ω* = V(A′) = (A′x) · dx (the v1 dual states). k = dt̄ ⊗_s V, tr k = 0, Gk = k, ⟨T, k⟩ = −V_iT_t̄i. With
F_ij := ∂_iw_t̄j − ∂_jw_t̄i and ∂_jV_i = A′_ij, A′ antisymmetric, V_i∂_jF_ij = ∂_j(V_iF_ij) − 2∂_i(A′_ijw_t̄j), so
⟨P_0w, k⟩ = ∂_j(−½V_iF_ij + A′_jlw_t̄l) and

    R_1(u) = ∮(½V_iF_ij(u) − A′_jlu_t̄l)n_j dS.

In the evaluations we use ∮_(|x|=R) dS = 2π²R³ and ∮_(|x|=R) x_ix_j dS = (π²/2)R⁵δ_ij.

### [Hin26, Lemma 8.12] in dimension 4 + 1 {#sec:iii-f4-3}

**Lemma {#lem:iii-f4-3-1}** (The zero energy pairings; [Hin26, Lemma 8.12] in dimension 4 + 1.) For b = (m, A) near
b_0, ṁ ∈ ℝ, Ȧ, A′ ∈ 𝔰𝔬(4), S, S′ ∈ 𝒮_1:

(1) (*Mass.*) ⟨L_1ġ^Υ_b(ṁ, 0), h*_(b,s0)⟩ = 3π²ṁ and ⟨L_1ġ^Υ_b(ṁ, 0), h*_(b,s1)(S′)⟩ = 0.

(2) (*Angular momenta.*) ⟨L_1ġ^Υ_b(0, Ȧ), h*_(b,s0)⟩ = ⟨L_1ġ^Υ_b(0, Ȧ), h*_(b,s1)(S′)⟩ = 0 and
⟨L_1ġ^Υ_b(0, Ȧ), h*_(b,v1)(V(A′))⟩ = 2π²m⟨Ȧ, A′⟩_F.

(3) (*Centres of mass.*) With h := h_(b,s1)(S), h̆ := h̆¹_(b,s1)(S): ⟨L_2h + L_1h̆, h*_(b,s0)⟩ = 0 and
⟨L_2h + L_1h̆, h*_(b,s1)(S′)⟩ = (3π²/2)m ξ_S · ξ_(S′).

(4) (*The rest.*) The pairings of L_1ġ^Υ_b(ṁ, 0) and of L_2h + L_1h̆ with h*_(b,v1)(V′) are not determined by the
leading terms; they are linear in their arguments and continuous in b. With them as unknowns, the 11 × 11 matrix of
(1)–(4) (rows ṁ, S, Ȧ; columns h*_s0, h*_s1, h*_v1) is block upper triangular with determinant
3π²((3π²/2)m)⁴(2π²m)⁶ ≠ 0.

*Proof.* [[lem:iii-f4-2-2]] applies: the states lie in ker D Ric ∩ ker δ_(E_Υ)G ([[prop:iii-f3-2-2]] (2),
[[prop:iii-d2-3-1]] (2)), with the weights of [[sec:iii-f4-1]], and c* ≥ 3 throughout. The excesses
(e_1 = a + c − 2, e_2 = min(a − 3, ă − 2) + c): mass (a = 2) against s0 and s1 (c = 0), 0; against v1 (c = −1), −1;
angular momenta (a = 3) against s0 and s1, 1; against v1, 0; centres of mass (a = 3, ă = 2) against s0 and s1, 0;
against v1, −1. The entries of excess > 0 vanish, those of excess < 0 are (4)'s, and the continuity there is that of
the states and dual states in b ([[prop:iii-f3-2-2]] (3), [[prop:iii-d2-3-1]], [[prop:iii-e-3-1]],
[[prop:iii-e1-3-1]]) with the absolute convergence of the pairings on the left of [[eq:iii-f4-2-1]]–[[eq:iii-f4-2-2]],
uniformly near b_0. The entries of excess 0 are, by [[lem:iii-f4-2-2]] (3), leading-term integrals on Minkowski space,
which may be computed with any representatives with P_0u = 0 (resp. P_0h = 0 = P_1h + P_0h̆) differing by decaying
gauge terms, and with the time t̄; we use the fluxes (a)–(c) of [[sec:iii-f4-2]].

*The representatives.* ġ^Υ_b(ṁ, 0) is ṁ|x|⁻²(dt̄ + d|x|)² + δ*ω̇_b with ω̇_b ∈ 𝒜^((1,0)∪(1+ℰ_ind))
([[lem:iii-f3-1-1]], [[prop:iii-f3-2-2]]), and on Minkowski space |x|⁻²(dt̄ + d|x|)² − |x|⁻²(dt̄² + d|x|²)
= δ̄*(−2|x|⁻¹dt̄), with −2|x|⁻¹dt̄ ∈ ρC^∞; so u := ṁ r⁻²(dt̄² + dr²) represents it. ġ^Υ_b(0, Ȧ) is
2m|x|⁻⁴(dt̄ + d|x|) ⊗_s V(Ȧ) plus gauge ([[eq:iii-e1-2-2]]: this leading term does not depend on A), whose
t̄i-components are u_t̄i = m r⁻⁴(Ȧx)_i. For the centres of mass, h_(b,s1)(S) and the stationary part of the boost
differ from the pair below by δ* of 1-forms in 𝒜², resp. 𝒜¹ ([[eq:iii-d2-3-2]]) up to a multiple of h_(b,s1)(S) (the
choice of the time origin), which changes (3) by a first-order pairing of h_(b,s1), of excess ≥ 1 against s0 and s1.
The pair: with g_b − ḡ = m|x|⁻²(dt̄² + d|x|²) + (gauge) + O(|x|⁻³) at first order in m and the boost field
X := t̄ c · ∂_x + (c · x)∂_(t̄), c := ξ_S, a Killing field of ḡ, ½ℒ_X(g_b − ḡ) = t̄h + h̆ with h = ½c · ∇(m r⁻²(dt̄² +
dr²)) and h̆ its t̄-independent part, h̆_t̄i = ½(m_jic_j + m_t̄t̄c_i), h̆_ij = ½(m_t̄jc_i + m_t̄ic_j) = 0, where m_t̄t̄
= m r⁻², m_t̄i = 0, m_ij = m x_ix_j r⁻⁴ are the components of m r⁻²(dt̄² + dr²). ℒ_X commutes with D Ric of ḡ, so the
pair solves the Minkowski equations, and the Kerr–Schild and static forms differ by δ̄*ζ with ζ = −2m|x|⁻¹dt̄, whose
image ℒ_Xδ̄*ζ = δ̄*ℒ_Xζ is a pair of the form (δ̄*ζ_1, δ̄*ζ_2 + k(ζ_1)) on which R_2 vanishes. The dual states' leading
terms are −dt̄, ξ_(S′) · dx and V(A′), with the remainders of higher weight.

*(1)* With u = ṁr⁻²(dt̄² + dr²): u_kk = ṁr⁻², u_ij = ṁx_ix_jr⁻⁴, ∂_iu_kk = −2ṁx_ir⁻⁴ and
∂_ju_ij = ṁ(5x_i − 4x_i)r⁻⁴ = ṁx_ir⁻⁴, so by (a), R_1 = −½∮(−3ṁx_ir⁻⁴)(x_i/r) dS = (3/2)ṁR⁻³ · 2π²R³ = 3π²ṁ. Against
s1, u_t̄i = 0, so (b) gives 0.

*(2)* The entries against s0 and s1 have excess 1. Against V(A′), by (c) with u_t̄j = m r⁻⁴(Ȧx)_j:
F_ij = 2m r⁻⁴Ȧ_ji − 4m r⁻⁶(x_i(Ȧx)_j − x_j(Ȧx)_i), and since x · Ȧx = 0, F_ijx_j = 2m r⁻⁴(Ȧx)_i; so on |x| = R,
½V_iF_ijn_j = m R⁻⁵(A′x) · (Ȧx) and −A′_jlu_t̄ln_j = −m R⁻⁵ x · A′Ȧx = m R⁻⁵(A′x) · (Ȧx). Hence
R_1 = 2m R⁻⁵ ∮(A′x) · (Ȧx) dS = 2m R⁻⁵ A′_ikȦ_il (π²/2)R⁵δ_kl = π²m tr(A′ᵀȦ) = 2π²m⟨Ȧ, A′⟩_F.

*(3)* Against s0, by (a), R_2 involves h̆_ij only, which vanishes. Against q · dx, q := ξ_(S′), by (b): from
h_ij = (m/2)(c_ix_j + x_ic_j)r⁻⁴ − 2m(c · x)x_ix_jr⁻⁶, h_ijx_j = (m/2)c_ir⁻² − (3m/2)(c · x)x_ir⁻⁴ and
h_kk = −m(c · x)r⁻⁴; and from h̆_t̄j = (m/2)(x_j(c · x)r⁻⁴ + c_jr⁻²), ∂_ih̆_t̄j − ∂_jh̆_t̄i = (3m/2)(c_ix_j − c_jx_i)r⁻⁴.
So on |x| = R the integrand q_i(h_ij − δ_ijh_kk + ∂_ih̆_t̄j − ∂_jh̆_t̄i)n_j is R⁻¹(2m(q · c)R⁻² − 2m(c · x)(q · x)R⁻⁴),
whose integral is 2m(q · c)R⁻³ · 2π²R³ − 2mR⁻⁵(π²/2)R⁵(q · c) = 3π²m(q · c); R_2 = (3π²/2)m ξ_S · ξ_(S′).

*(4)* The matrix with rows (ṁ, S, Ȧ) and columns (s0, s1, v1) has the blocks 3π² and 0 (row ṁ), 0 and
(3π²/2)m ξ_S · ξ_(S′) (row S), 0, 0 and 2π²m⟨Ȧ, A′⟩_F (row Ȧ), and the unknowns only in the column v1 of the rows ṁ
and S: it is block upper triangular, with the diagonal blocks 3π², (3π²/2)m Id (in a basis of 𝒮_1 for which the ξ_S are
orthonormal) and 2π²m Id_(𝔰𝔬(4)) (the E_ij being orthonormal). ∎

The values of [Hin26] ([Hin24b]'s normalisation 2L, and dt for the s0 dual state) are −16πṁ_K, −16πm_K(q · ȧ) and
8πm_K(q · c), m_K the Kerr mass; in each dimension the three are ∓8π times the mass and angular momentum and 4π times the
mass times the centre of mass, in the normalisations used.

### [Hin26, Lemma 8.15] in dimension 4 + 1 {#sec:iii-f4-4}

For a stationary v of weight ≥ −2, smooth on X, with L_b^(0)v of weight > 1, and W ∈ 𝔰𝔬(4), put

    ℓ♯_v(W) := ⟨L_b^(0)v, h♯_(b,v1)(W)⟩ − ⟨v, L_b^(0)*h♯_(b,v1)(W)⟩.                                     {#eq:iii-f4-4-1}

Both pairings converge absolutely: h♯ has weight 3, and L_b^(0)*h♯_(b,v1)(W) ∈ ρ^(⌊C_0⌋+6)C^∞ + C_c^∞ by
[[eq:iii-e1-3-4]] and [[eq:iii-f3-4-4]]. If moreover L_b^(0)v pairs absolutely with h*_(b,v1)(V′), then

    ⟨L_b^(0)v, h*_(b,v1)(V′)⟩ = ℓ♯_v([A(b), A_(V′)]),                                                    {#eq:iii-f4-4-2}

since ⟨L_b^(0)v, h♭⟩ = ⟨v, L_b^(0)*h♭⟩ (h♭ ∈ Ḣ_b^(0,C_0+3), C_0 > 1, so the boundary terms vanish) and
L_b^(0)*h♭ = −L_b^(0)*h♯, the dual state lying in ker L_b^(0)*. ℓ♯_v is defined on all of 𝔰𝔬(4), while the right side
of [[eq:iii-f4-4-2]] sees only im ad_(A(b)), which is 0 at b_0; this is the device [Hin26, (8.33)] for smoothness in b.

The algebra of 𝔰𝔬(4) used here and in [[sec:iii-f4-5]] is the following.

**Proposition {#prop:np-10-34-iv}** (Rotations and the bracket form of 𝔰𝔬(4).) On ℝ^(1+4) with coordinates (t, x), for
A ∈ 𝔰𝔬(4) let w_A := x · A dx = Σ_(i,j) x_iA_ij dx^j and h_A := m|x|⁻⁴(dt ⊗ w_A + w_A ⊗ dt).

(a) For B ∈ 𝔰𝔬(4) and the rotation field R := (Bx) · ∂_x, ℒ_R h_A = h_([A,B]).

(b) ⟨[X, Y], Z⟩_F = −⟨Y, [X, Z]⟩_F for X, Y, Z ∈ 𝔰𝔬(4).

(c) For A_b ∈ 𝔰𝔬(4) the form 𝔅(V, V′) := ⟨[A_V, A_b], A_(V′)⟩_F on 𝒱_1 is antisymmetric, with kernel
{V : [A_V, A_b] = 0}. At A_b = E_12 it has rank 4 and kernel spanned by V(E_12) and V(E_34), and
im ad_(E_12) = span{E_13, E_14, E_23, E_24}, while im ad_(E_13) contains E_12 and E_34.

(d) In three dimensions, with the isomorphism a ↦ â of ℝ³ onto 𝔰𝔬(3), âv := a × v, one has ⟨â, b̂⟩_F = a · b and
⟨[â_V, â_b], â_(V′)⟩_F = (a_V × a_b) · a_(V′), the triple product.

*Proof.* (a) The flow of R is φ_s(t, x) = (t, e^(sB)x), with e^(sB) orthogonal. So φ_s*dt = dt, φ_s*|x| = |x| and
φ_s*w_A = (e^(sB)x) · A e^(sB)dx = x · (e^(−sB)Ae^(sB))dx = w_(e^(−sB)Ae^(sB)); differentiating at s = 0,
ℒ_R w_A = w_(AB−BA) = w_([A,B]), and ℒ_R h_A = h_([A,B]). (b) For antisymmetric X, Y, Z, [X, Y] is antisymmetric, so
⟨[X, Y], Z⟩_F = −½tr([X, Y]Z) = −½tr(XYZ − YXZ), and ⟨Y, [X, Z]⟩_F = −½tr(Y(XZ − ZX)) = −½tr(YXZ − XYZ), using
tr(YZX) = tr(XYZ). The two sum to 0. (c) By (b), 𝔅(V′, V) = −⟨[A_b, A_(V′)], A_V⟩_F = ⟨A_(V′), [A_b, A_V]⟩_F
= −𝔅(V, V′). As ⟨·, ·⟩_F is nondegenerate, V lies in the kernel exactly when [A_V, A_b] = 0. With
[E_ij, E_jk] = E_ik for distinct i, j, k and [E_ij, E_kl] = 0 for disjoint pairs, ad_(E_12) maps E_13, E_14, E_23, E_24
to −E_23, −E_24, E_13, E_14 and annihilates E_12 and E_34; so its kernel is span{E_12, E_34} and its image
span{E_13, E_14, E_23, E_24}, of dimension 4. Likewise ad_(E_13)E_23 = −E_12 and ad_(E_13)E_14 = −E_34, so im ad_(E_13)
contains E_12 and E_34. (d) â_ij = −ε_ijk a_k, so
⟨â, b̂⟩_F = ½ε_ijkε_ijl a_k b_l = a · b; and [â, b̂] = (a × b)^ by the Jacobi identity for the cross product. ∎

**Lemma {#lem:iii-f4-4-1}** (The pairings of the generalised states; [Hin26, Lemma 8.15] in dimension 4 + 1.) For
b = (m, A) near b_0:

(1) (*Scalar type 1.*) L_b^(0)h̆²_(b,s1)(S) = −L_2h_(b,s1)(S) − L_1h̆¹_(b,s1)(S); so
⟨L_b^(0)h̆²_(b,s1)(S), h*_(b,s0)⟩ = 0, and S ↦ ⟨L_b^(0)h̆²_(b,s1)(S), h*_(b,s1)(·)⟩ = −(3π²/2)m ξ_S · ξ_((·)) is an
isomorphism 𝒮_1 → 𝒮_1*, smooth in b.

(2) (*Vector type 1.*) L_b^(0)h̆¹_(b,v1)(V) = −L_1h_(b,v1)(V), which pairs to 0 with h*_(b,s0) and h*_(b,s1)(S′), and

    ⟨L_b^(0)h̆¹_(b,v1)(V), h*_(b,v1)(V′)⟩ = π²m⟨A_V, [A(b), A_(V′)]⟩_F,
    ℓ♯_(h̆¹_(b,v1)(V))(W) = π²m⟨A_V, W⟩_F  for all W ∈ 𝔰𝔬(4).                                           {#eq:iii-f4-4-3}

*Proof.* (1) h^(≤2)_(b,s1)(S) = t_*²h + 2t_*h̆¹ + 2h̆², h := h_(b,s1)(S), lies in ker L_b ([[prop:iii-d3-3-1]] (2), with
its normalisation: the constant coefficient of h^(≤k) is k! h̆^k); expanding as in [[sec:iii-f4-2]] with Lh = 0 and
L(t_*h + h̆¹) = 0 gives 2(L_2h + L_1h̆¹) + 2L_b^(0)h̆² = 0. [[lem:iii-f4-3-1]] (3) gives the pairings.

(2) t_*h_(b,v1)(V) + h̆¹_(b,v1)(V) ∈ ker L_b ([[prop:iii-d3-3-1]] (3)), so L_b^(0)h̆¹ = −L_1h_(b,v1)(V), and by
[[rem:iii-f3-2-3]], h_(b,v1)(V) = ½ġ^Υ_b(0, [A, A_V]). [[lem:iii-f4-3-1]] (2) then gives 0 against h*_s0, h*_s1, and
−½ · 2π²m⟨[A, A_V], A_(V′)⟩_F = π²m⟨A_V, [A, A_(V′)]⟩_F against h*_v1(V′), by [[prop:np-10-34-iv]] (b). By
[[eq:iii-f4-4-2]], ℓ♯_(h̆¹_(b,v1)(V))(W) = π²m⟨A_V, W⟩_F for W ∈ im ad_(A(b)). Now
ℓ♯_(h̆¹_(b,v1)(V))(W) = −lim_R ⟨[L_b^(0), χ_R]h̆¹_(b,v1)(V), h♯_(b,v1)(W)⟩ (insert χ_R into [[eq:iii-f4-4-1]]:
L_b^(0)* of the compactly supported side is exact, and the limit of
⟨χ_RL_b^(0)v, h♯⟩ − ⟨χ_Rv, L_b^(0)*h♯⟩ is [[eq:iii-f4-4-1]]). Its weights are −1 and 3 with
[L_b^(0), χ_R] ∈ ρ²Diff¹_b, excess 0, so as in [[lem:iii-f4-2-2]] (3) it is the integral of the leading terms:
h̄¹_v1(V) of [[eq:iii-d3-3-3]], independent of b; h̄♯(W) = mρ³(dt_* + κ_C d|x|) ⊗_s ρV(W) of [[eq:iii-e1-3-3]], which
depends on b only through m; and the model operator. So ℓ♯_(h̆¹_(b,v1)(V))(W) = m c(V, W) with c a bilinear form
independent of b. For b = (m, A) in the parameter neighbourhood, c(V, W) = π²⟨A_V, W⟩_F on im ad_A ([[lem:iii-f4-3-1]]
(2) holds at every such b, spinning or not, with the same value, as the leading term
2mρ³(dt_* + 2d|x|) ⊗_s ρV(Ȧ) of ġ^Υ_b(0, Ȧ), [[eq:iii-e1-2-2]], does not depend on A); and these images, for A small,
span 𝔰𝔬(4) (im ad_(ϵE_12) = span{E_13, E_14, E_23, E_24} and im ad_(ϵE_13) ∋ E_12, E_34, [[prop:np-10-34-iv]] (c)). So
c(V, ·) = π²⟨A_V, ·⟩_F on 𝔰𝔬(4). ∎

### The physical large zero energy states {#sec:iii-f4-5}

Let τ be one of the types s2, v2, t2, and Y a harmonic of that type and degree 2 (S ∈ 𝒮_2, V ∈ 𝒱_2, or a trace-free
divergence-free tensor harmonic of degree 2). By [[prop:iii-f1-2-3]], −2 is a simple indicial root of L_b^(0) at τ (the
root −l at l = 2), so ker N_τ(L̄^(0), −2) is one-dimensional for each Y; let h̄_τ(Y) = ρ⁻²ū_τ(Y) span it, linearly in Y.
Since L̄ is homogeneous under dilations, L̄^(0)h̄_τ(Y) = 0 near ∂X.

**Proposition {#prop:iii-f4-5-1}** (The physical states at −2; [Hin26, Proposition 8.14 (1)] in dimension 4 + 1.) There
is an index set ℰ_ind such that for all b near b_0 there are

    h^(−2)_(b,τ)(Y) ∈ 𝒜^((−2,0)∪(−2+ℰ_ind))(X̄; S²T*X),     τ ∈ {s2, v2, t2},                            {#eq:iii-f4-5-1}

linear in Y and smooth in b, with ρ⁻² leading term h̄_τ(Y), in ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b), hence in
ker L_b^(0). Their leading terms span ker N_τ(L̄^(0), −2) for each τ.

*Proof.* It suffices to treat Y in a basis; we suppress Y and τ.

*Step 1: formal solution.* f_b := L_b^(0)(χh̄) ∈ ρ²C^∞ + C_c^∞, since L_b^(0) − L̄^(0) ∈ ρ⁴Diff²_b
([[lem:iii-f-2-1]]). Near ∂X, L_b^(0) = ρ²A with A an elliptic b-operator whose normal operator does not depend on b
([[eq:i-c-1-1]]–[[eq:i-c-1-3]]; [[lem:iii-f-2-1]]). [[lem:iii-a-1-5]] gives h′_(b,1) ∈ 𝒜^ℱ, ℱ built from (0, 0) and
the roots (with logarithms at the integer roots ≥ 0), smooth in b, with L_b^(0)h^≈_b ∈ 𝒜^N for a fixed large N,
h^≈_b := χh̄ + h′_(b,1); ℱ ⊂ −2 + ℰ_ind as min Re ℱ ≥ 0.

*Step 2: the obstructions.* By [[prop:iii-f3-4-1]] (2) and [[cor:iii-f3-4-2]] (2), L_b^(0)h = f is solvable, smoothly
in b, for f ∈ 𝒜^(α+2) orthogonal to the eleven dual states. (a)
⟨L_b^(0)h^≈_b, h*_(b,s0)⟩ = ⟨h^≈_b, L_b^(0)*h*_(b,s0)⟩ = 0: h*_(b,s0) ∈ Ḣ_b^(0,C_0+3), C_0 > 1, so the boundary terms,
O(R^(1−C_0)), vanish. (b) ℓ_s1(S′) := ⟨L_b^(0)h^≈_b, h*_(b,s1)(S′)⟩, a linear form on 𝒮_1, smooth in b. (c) By
[[eq:iii-f4-4-2]], ⟨L_b^(0)h^≈_b, h*_(b,v1)(V′)⟩ = ℓ♯_(h^≈_b)([A(b), A_(V′)]), with ℓ♯_(h^≈_b) a linear form on
𝔰𝔬(4), smooth in b. Let S_1 ∈ 𝒮_1 solve ℓ_s1(·) − (3π²/2)m ξ_(S_1) · ξ_((·)) = 0 ([[lem:iii-f4-4-1]] (1)), and
V_1 ∈ 𝒱_1 solve

    ℓ♯_(h^≈_b) + ℓ♯_(h̆²_(b,s1)(S_1)) + π²m⟨A_(V_1), ·⟩_F = 0     on 𝔰𝔬(4)                               {#eq:iii-f4-5-2}

([[lem:iii-f4-4-1]] (2); ℓ♯_(h̆²_(b,s1)(S_1)) is defined since h̆²_(b,s1) has weight −1 and L_b^(0)h̆²_(b,s1), by
[[lem:iii-f4-4-1]] (1), weight ≥ 2). Both are smooth in b. Put h^(≈,2)_b := h^≈_b + h̆²_(b,s1)(S_1) + h̆¹_(b,v1)(V_1).
Then L_b^(0)h^(≈,2)_b pairs to 0 with all eleven dual states: with h*_s0 by (a) and [[lem:iii-f4-4-1]]; with h*_s1 by
the choice of S_1 and [[lem:iii-f4-4-1]] (2) (h̆¹_v1 pairs to 0); with h*_v1(V′) by [[eq:iii-f4-4-2]] for each summand
and [[eq:iii-f4-5-2]] at W = [A(b), A_(V′)].

*Step 3: the state.* L_b^(0) maps h̆²_(b,s1)(S_1) and h̆¹_(b,v1)(V_1), of weight −1 with leading terms annihilated by
N(L̄^(0), −1) ([[prop:iii-d3-3-1]] (2)–(3)), into 𝒜^((2,0)∪(2+ℰ_ind)), so
L_b^(0)h^(≈,2)_b ∈ 𝒜^((2,0)∪(2+ℰ_ind)), smoothly in b. [[lem:iii-a-1-5]], applied to its ρ² terms, gives
h_(b,(0)) ∈ 𝒜^((0,k)) for some k, smooth in b, with f_b := −L_b^(0)(h^(≈,2)_b + h_(b,(0))) ∈ 𝒜^(2+ε_Υ); and
⟨L_b^(0)h_(b,(0)), h*⟩ = ⟨h_(b,(0)), L_b^(0)*h*⟩ = 0 for the dual states (weight ≥ 3: boundary terms O(R⁻¹ log^k R)), so
f_b is orthogonal to all of them. [[cor:iii-f3-4-2]] (2) with α ∈ (0, ε_Υ) gives u_b ∈ 𝒜^(α−ϵ), smooth in b, with
L_b^(0)u_b = f_b. Every term of f_b is polyhomogeneous: h^≈_b by its construction ([[lem:iii-a-1-5]]),
h̆²_(b,s1)(S_1) and h̆¹_(b,v1)(V_1) in 𝒜^((−1,0)∪(−1+ℰ_ind)) by [[prop:iii-d3-3-1]] (2)–(3), and h_(b,(0)); and L_b^(0)
has smooth coefficients. So u_b, which solves ρ²Au_b = f_b near ∂X with A b-elliptic, is polyhomogeneous by
[[lem:iii-a-1-4]], as in [[lem:iii-d1-5-1]] (2), with an index set built from the indicial roots of L_b^(0) with real
part > α − ϵ and from that of f_b, both independent of b (the roots are the model's, [[lem:iii-f1-2-1]]). This index
set contains the roots ι^C_(·,+) − 1, whose real parts exceed 1 ([[prop:iii-f1-2-3]] (b)). Then

    h^(−2)_b := h^(≈,2)_b + h_(b,(0)) + u_b ∈ ker L_b^(0),                                               {#eq:iii-f4-5-3}

with leading term h̄ and h^(−2)_b − χh̄ ∈ 𝒜^((−1,0)∪(−1+ℰ_ind)) + 𝒜^ℱ + 𝒜^((0,k)) + 𝒜^(ℰ′) ⊂ 𝒜^(−2+ℰ_ind), ℰ′ the index
set of u_b just found; its index set is that of [[eq:iii-f4-5-1]], independent of b.

*Step 4: the gauge.* η := δ_(g_b,E_Υ)G_(g_b)h^(−2)_b has weight −1, and the second Bianchi identity gives
(□^C_b)^(0)η = 2δ_(g_b)G_(g_b)L_b^(0)h^(−2)_b = 0. In the Euclidean weight of [[thm:iii-e-1-1]],
η ∈ H̄_b^(s,α_C) for every s and every α_C < −3; taking α_C + 2 ∈ [−C_0, −1) (possible as C_0 > 1),
[[thm:iii-e-1-1]] (2) gives η = 0; then D_(g_b)Ric(h^(−2)_b) = L_b^(0)h^(−2)_b = 0. ∎

**Remark {#rem:s15-window}** (Which states are needed.) In the expansion at future timelike infinity of [[ch:s16]]–
[[ch:s19]], a term t_*^(−α) at ι⁺ whose coefficient meets an indicial root μ of L_b^(0) contributes a term of order
α − μ at the Kerr face, and its generalised companions terms of orders α − μ + j, j ≥ 1 ([Hin26, (1.23), p. 17]); a
state must be accounted for while that order is at most 4, the forward problem needing u = O(t_*^(−2−ϵ)) and sources
O(t_*^(−4−ϵ)) ([Hin26, p. 273]). For the physical roots μ = −l, l ≥ 2, the order is α + l, which is at most 4 exactly
when l ≤ 4 − α; for α ∈ (1, 2] this is l = 2, with ⌊4 − α − 2⌋ = ⌊2 − α⌋ = 0 companions. So the physical states
needed for orders in (1, 2] are those of [[prop:iii-f4-5-1]], at −2 and without companions, and the roots with real
part ≤ 0 that enter lie in [α − 4, 0], that is in [−2, 0] at α = 2 and in [−5/2, 0] at α = 3/2. The construction of
companions in [Hin26, Step 4 of the proof of Proposition 8.14] would need −3 not to be a root at s2, v2 and t2; by
[[prop:iii-f1-2-3]] it is not (the roots there with real part ≤ 0 are −2, 2 − ι^Υ_(s2,4) ∈ (−9/4, −2),
2 − ι^Υ_(s2,3) ∈ (−5/4, −1), 0 and roots below −101 at s2; −2, −1 and a root below −101 at v2; and −2 at t2).

*Remarks on [Hin26].* (a) [Hin26, (8.25)], L* = G ∘ D Ric ∘ G − …, uses G² = Id, which holds in dimension 3 + 1 only;
in dimension 4 + 1 it is [[eq:iii-f3-4-4]], with G⁻¹ = Id − ⅓g tr, and the inclusion G δ* ker(□^C)* ⊂ ker L* holds as
there. (b) The threshold s > 5/2 of [Hin26, footnote 78] is that of the operator without constraint damping;
[[lem:iii-f2-1-1]] gives the threshold with it. (c) In the proof of [Hin26, Proposition 8.14], the printed
"−8πm a(V_1) = v_b" has the sign reversed against [Hin26, (8.33)], and [Hin26, (8.35)] prints the scalar type 1
functional where the vector type 1 functional is meant.
