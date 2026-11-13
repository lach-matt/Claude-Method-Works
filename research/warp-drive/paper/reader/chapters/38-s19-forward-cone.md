# Part. The stability theory, IV: forward solutions and their asymptotics {#part:stability-forward}

## Forward solutions in the cone, uniformly near b₀; null infinity; almost linear bounds {#ch:s19}

This chapter solves the linearised gauge-fixed Einstein equation forward in time around the backgrounds of the
nonlinear iteration: a patched Myers–Perry metric g_(b₀,b,−S), equal to g_b near K⁺ and to a boosted g_(b₀) near
null infinity, plus a perturbation h that decays at 𝓘⁺, ι⁺ and K⁺. It writes out [Hin26, Section 11 (opening) and
Sections 11.1–11.3] in dimension 4 + 1, together with the uniformity in the black hole parameter that [Hin26] uses
there.

[[sec:iii-i-1]]–[[sec:iii-i-5]] define the classes of metric perturbations and of their sources, show that the
perturbations are e3b-perturbations of g_b, give the structure of L^(g,g_0) in the forward cone and its mapping
properties, prove that 2L^(g,g_0) is admissible relative to 2L_b in the sense of [[def:ii-c-3-3]], and obtain forward
solutions at b₀ ([[thm:iii-i-5-3]]). [[sec:iii-h2-0]]–[[sec:iii-h2-5]] prove the two inputs that the case b ≠ b₀
needs, on one fixed neighbourhood of b₀ and with constants uniform in b: strong trapping admissibility of 2L_b at every
b, which gives 2-admissibility for every order k of b-regularity ([[prop:iii-h2-1-1]], [[thm:iii-h2-2-1]]), and the
forward solution theory of [[ch:s09]] uniformly over the stationary models 2L_b ([[thm:iii-h2-3-1]],
[[thm:iii-h2-4-1]]). Forward solutions near b₀, continuous in b, follow ([[cor:iii-h2-5-1]]). [[sec:iii-i1-1]]–
[[sec:iii-i1-3]] give the partial polyhomogeneity of solutions at 𝓘⁺ and formal solutions there, and
[[sec:iii-i2-1]]–[[sec:iii-i2-5]] improve the forward solutions at ι⁺ and K⁺ for sources with more decay
([[prop:iii-i2-5-1]]).

*What changes in dimension 4 + 1.* (1) The contributions of the perturbation h to the operator at null infinity are
half an order lower than the constant matrix Ā of [[lem:iii-c-4-2]] ([[prop:iii-c-4-4]], [[rem:iii-c-4-5]]). So the
leading part of L^(g,g_0) at 𝓘⁺ is that of L_b, 2L^(g,g_0) is admissible relative to 2L_b with p_0 = p̃_1 = 0, and the
restriction ℓ_I < 2γ_Υ of [Hin26, Lemma 11.5] disappears ([[lem:iii-i-2-2]]). (2) At ι⁺ the differences of the
backgrounds (mass, rotation, cut-off boost) are of order 2, where [Hin26] has 1, and the curvature of the patched
background is of order 4, where [Hin26] has 3 ([[lem:iii-i-3-6]], [[lem:iii-i-4-3]]). (3) The forward solutions have
sf-loss 0 and their weights at 𝓘⁺ reach 3/2, the order of a radiation field ([[thm:iii-i-5-3]]). (4) The trapping
bound holds at every b near b₀ with a frame built from the null geometry alone, and the ι⁺-normal operator of 2L_b
does not depend on b ([[prop:iii-h2-1-1]], [[lem:iii-h2-3-2]]). (5) At 𝓘⁺ the first exponent of a solution is 3/2, in
the slot π̸₀ only; π₁₁ u has no term at 3/2; and formal solutions remove one exceptional term,
5/2 + (1 − e_Υ)γ_Υ in the 11-component, where [Hin26] removes two ([[lem:iii-i1-2-2]], [[prop:iii-i1-3-1]]). (6) The
Fourier transforms of the cut-off zero energy states decay rapidly at scf and lie one order deeper at tf
([[lem:iii-i2-4-3]]). So the singular part of the low-frequency resolvent does not limit the decay at ι⁺: forward
solutions keep the ι⁺-weight min(α_+, 3/2, min Re ℰ_+) − ε at every K⁺-weight α_K − 2, α_K ∈ [1/2, 1), where [Hin26]
has α_K − ε ([[prop:iii-i2-5-1]]). The cap 3/2 is the transport of the radiation field's order from 𝓘⁺; in dimension
3 + 1 it is 1.

*Notation and the inner radius.* The notation is that of [[ch:s04]]–[[ch:s10]] and of [[ch:s11]], [[ch:s13]]–
[[ch:s18]]. The black hole parameters are b = (m, A), b₀ = (m₀, 0) and R₁ = m₀^(1/2); g_m := g_((m,0)). L_b is the
linearised gauge-fixed Einstein operator of [[ch:s15]], with the gauge modification E_Υ of [[sec:iii-d-1]] and the
constraint damping (c_C, e_C, γ_C) of [[sec:iii-f-1]] fixed there, and for metrics g, g_0, L^(g,g_0) is the
linearisation [[eq:iii-c-4-1]] of the gauge-fixed Einstein operator P(g, g_0) of [[eq:iii-b-6-4]] in g, so that
L^(g_b,g_b) = L_b. The radii r_0 − 2δ_0 < r_0 < r_2 of the artificial boundary are those of [[def:s12-radii]], with
r_0 = r_♭ ∈ (0, ½R₁], the inner radius of the spacetime of [[ch:s11]]; then the artificial boundary of the spaces of
[[ch:s04]]–[[ch:s10]] is the inner boundary of that spacetime. Every result of the chapter holds for each such r_♭, with
constants and neighbourhoods of b₀ that may depend on it. The slots of a symmetric 2-tensor near 𝓘⁺ are those of
[[def:iii-c-1-2]], in the splitting [[eq:iii-c-1-6]]: slots 1–3 form π_C, and slots 4, 5, 6, 7 are π₀₁, π_(1/), π̸₀
and π₁₁. We write

    σ_Υ := {0, (1 − e_Υ)γ_Υ, γ_Υ, 2γ_Υ},

the eigenvalues of Ā on the slots 6, 4, 5, 7, and λ_C ∈ γ_C{2(1 − v_C), 1 − v_C, (1 − e_C)(1 − v_C)} those on the slots
1–3 ([[eq:iii-c-4-3]]). The gauge parameters satisfy 0 < γ_Υ < 1/4, 0 < e_Υ < 1 ([[eq:iii-c-1-1]]) and
(1 − e_C)(1 − v_C)γ_C > 100 ([[sec:iii-f-1]]). For an index set E, (E, ℓ) denotes the expansion in E up to the
weight ℓ, and E ∪̄ {(z, 0)} is the extended union of [[lem:iii-a-1-2]]: E ∪ {(z, 0)} if z ∉ π_1E, and E with the
logarithmic order at z raised by one otherwise; ∪̄^m is that union taken m times.

### The setting {#sec:iii-i-1}

This section is [Hin26, (11.1)–(11.11)] in dimension 4 + 1.

*Background.* For b near b₀ and S ∈ 𝒮_1 small, with the cut-offs χ_K and the boosts φ_S of [[sec:iii-b-5]], put

    g_(b₀,b,−S) := (1 − χ_K) φ_(−S)^* g_(b₀) + χ_K g_b                                                  {#eq:iii-i-1-1}

([Hin26, (11.1)]). The cut-offs are moreover taken with ([Hin26, (11.5)])

    supp χ^♭_K ⊂ χ_K⁻¹(1) ⊂ supp χ_K ⊂ (χ^♯_K)⁻¹(1) ⊂ supp χ^♯_K ⊂ {t^♭_* ≥ 10},                        {#eq:iii-i-1-2}

a further condition of the same kind as those of [[sec:iii-b-5]] (supports in {t > T} with T large), and compatible
with them.

*Time function and domain.* t^♭_* is the function of [[lem:ii-c-3-2]] with ℓ = ℓ_I = ½, built for g_(b₀)
([Hin26, (11.3)]), and Ω_* := cl_M{t^♭_* ≥ 1} ⊂ Ω = cl_M{t_* ≥ 1} ([Hin26, (11.4)]). L²-based spaces on Ω_* use the
unweighted b-density μ_b = |dt_* dx|/(t_*⟨x⟩⁴) of [[cor:ii-f1-1-2]] ([Hin26] has t_*⁻¹⟨x⟩⁻³|dt_* dx|), and weights
are listed at (𝓘⁺, ι⁺, K⁺), with the defining functions ρ_I, ρ_+, ρ_K of [[eq:iii-b-2-2]].

**Definition {#def:iii-i-1-1}** (Metric perturbations and their sources; [Hin26, Definition 11.3] in dimension 4 + 1.)
Let ℰ_+ ⊂ ℂ × ℕ₀ be an index set with

    (2, 0) ∈ ℰ_+,      min Re ℰ_+ > 1,      jℰ_+ ⊂ ℰ_+  (j ∈ ℕ),                                         {#eq:iii-i-1-3}

and let ℰ_I^C satisfy [[def:iii-c-3-1]] (2)–(3), with ℰ_I^tot, ℰ_(I,01), ℰ_(I,1/), ℰ̸_(I,0), ℰ_(I,11) and ℱ_(I,11)
as there ([[eq:iii-c-3-1]]–[[eq:iii-c-3-2]], [[eq:iii-c-5-1]]). Let ℓ_I, ℓ_+, ℓ_K ∈ ℝ.

(1) For k ≥ 5, H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b(Ω_*) is the space of real symmetric 2-tensors h whose slot
components near 𝓘⁺ lie in H^(k,(ℰ,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b with ℰ = ℰ_I^C for π_C, ℰ_(I,01) for π₀₁, ℰ_(I,1/) for π_(1/),
ℰ̸_(I,0) for π̸₀ and ℰ_(I,11) for π₁₁ ([[eq:iii-c-3-3]] with ι⁺ in place of I⁰).

(2) For k ≥ 3, H^(k,(⟨ℰ_I^C+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2),ℓ_K)_b(Ω_*) is the space of f with π_C f, π₀₁ f, π_(1/) f,
π̸₀ f in (ℰ_I^C + 1, ℓ_I + 1) and π₁₁ f in (ℱ_(I,11), ℓ_I + 1) at 𝓘⁺, all in (ℰ_+ + 2, ℓ_+ + 2) at ι⁺, and of
weight ℓ_K at K⁺ ([[def:iii-c-5-1]]).

(3) H^(k,(⟨(3,0)⟩₀,ℓ_I),(ℰ_+,ℓ_+),ℰ_K)_b(Ω_*) is the class of [[def:iii-c-3-3]] at 𝓘⁺ ((3, 0) for every slot but
π₁₁, (2, 0) for π₁₁), with (ℰ_+, ℓ_+) at ι⁺ and the index set ℰ_K at K⁺.

[Hin26] has (1, 0) ∈ ℰ_+ and min Re ℰ_+ ≥ 1: (1, 0) is the ι⁺-order of its background differences, which in dimension
4 + 1 is 2 ([[lem:iii-i-3-6]]). The condition min Re ℰ_+ > 1 is what [[lem:iii-i-2-2]] and [[prop:iii-i-4-1]] use.
Later chapters may raise min Re ℰ_+; the exponent 3/2 + (1 − e_Υ)γ_Υ that formal solutions at 𝓘⁺ produce
([[prop:iii-i1-3-1]]) lies above it.

*The class of perturbations.* With parameters a_I > 3/2, a_+ > 1, a_K > 2, put

    𝒳^k := H^(k,(⟨ℰ_I^C⟩,a_I),(ℰ_+,a_+),a_K)_b(Ω_*; S²T*).                                              {#eq:iii-i-1-4}

[Hin26, (11.9)–(11.10)] fixes (a_I, a_+, a_K) = (3 + ε_I, 3 + ε_+, 2 + ε_K), with
0 < ε_K < ε_+ < min(ε_ind, ε_I) < 1, for the iteration of [Hin26, Sections 11.2–11.8]. This chapter uses only the
inequalities a_I > 3/2, a_+ > 1, a_K > 2, and, where a statement says so, upper bounds of the weights in terms of a_I
and a_+; the values are chosen where the iteration needs them, from [[ch:s20]] on.

### The edge-3b class {#sec:iii-i-2}

This section is [Hin26, Lemma 11.5 and (11.12)–(11.14)] in dimension 4 + 1. On M_(1/2) ([[def:iii-b-2-1]]) put
x_I := ρ_I^(1/2). Near 𝓘⁺, with the null coordinates x⁰ = t + |x|, x¹ = t − |x| and r dω the rescaled angular
coframe, the tensors

    x_I²(dx⁰)²,  dx⁰ ⊗_s dx¹,  x_I dx⁰ ⊗_s r dω,  x_I⁻²(dx¹)²,  x_I⁻¹ dx¹ ⊗_s r dω,  r dω ⊗_s r dω       {#eq:iii-i-2-1}

span x_I⁻²ρ_+⁻² C^∞(Ω_(*,1/2); S² ᵉ³ᵇT*M_(1/2)), and [[eq:iii-i-2-1]] with the factors of x_I dropped is a global
frame away from 𝓘⁺ ([Hin26, (11.13)]).

**Lemma {#lem:iii-i-2-1}** (The frame.) [[eq:iii-i-2-1]] is a frame of x_I⁻²ρ_+⁻² C^∞(S² ᵉ³ᵇT*) over Ω_(*,1/2).

*Proof.* By [[lem:ii-a-2-5]], as used in the proof of [[lem:ii-c-3-2]], near 𝓘⁺ the covectors e_1 := x_I⁻¹ dt_*,
e_2 := x_I dr and r dω span ρ_+⁻¹x_I⁻¹ C^∞(ᵉ³ᵇT*). With dt_* = dx¹ + O(|x|⁻²) d|x| ([[lem:iii-c-1-3]] and its proof)
and dr = d|x|, we have x_I⁻¹dx¹ = e_1 + O(ρ²x_I⁻²)e_2 and x_I dx⁰ = x_I²e_1 + 2e_2 + O(ρ²)e_2, an invertible smooth
change of frame (ρ = |x|⁻¹, and ρ²x_I⁻² = ρ_+²ρ_I ≤ 1). Symmetric products give [[eq:iii-i-2-1]]. Away from 𝓘⁺, x_I is
bounded below and the same products of dt, dx^i span; near K⁺ they span x_I⁻²ρ_+⁻² S² ᵉ³ᵇT* themselves, with no
rescaling by ⟨x⟩ ([[sec:ii-c-5-1]]). ∎

**Lemma {#lem:iii-i-2-2}** (Perturbations are e3b-perturbations; [Hin26, Lemma 11.5] in dimension 4 + 1.) Let h ∈ 𝒳^k,
k ≥ 3. Then h ∈ 𝒢̃^(k−3,(2ℓ_I,ℓ_+,ℓ_K))_b ([[def:ii-c-3-1]]) for every

    ℓ_I ∈ (0, ½],      ℓ_+ ∈ (0, 1],      ℓ_K ∈ (0, a_K],                                               {#eq:iii-i-2-2}

with ‖h‖_(𝒢̃^(k−3,(2ℓ_I,ℓ_+,ℓ_K))_b) ≤ C‖h‖_(𝒳^k). [Hin26] needs ℓ_I < min(2γ_Υ, ½) and ℓ_+ < 1.

*Proof.* b-Sobolev embedding for μ_b (dim M = 5, three derivatives) gives, slot by slot, sup bounds with k − 3
b-derivatives: at 𝓘⁺ by the least real part of the slot's index set (the expansion terms) or by a_I, whichever is
smaller; at ι⁺ by min(a_+, min Re ℰ_+) − ε > 1 ≥ ℓ_+ for ε small; at K⁺ by a_K ≥ ℓ_K. In powers of x_I the slot
components are: h_00, h_0ā, tr̸ h of order > 3 + 4γ_Υ; h_01 and h_11 of order ≥ 3 + 2(1 − e_Υ)γ_Υ; h_1ā of order
≥ 3 + 2γ_Υ; π̸₀ h of order 3 ([[def:iii-i-1-1]] (1), [[eq:iii-c-3-2]]). The coefficients of h in the frame
[[eq:iii-i-2-1]] are x_I⁻²h_00, h_01, x_I⁻¹h_0ā, x_I²h_11, x_I h_1ā and h_āb̄, of x_I-orders at least 1 + 4γ_Υ, 3,
2 + 4γ_Υ, 5, 4 and 3, all ≥ 1 ≥ 2ℓ_I. These are the orders of the index sets; where a_I is smaller, a slot has
x_I-order 2a_I (less ε for logarithms), and the least coefficient order is then 2a_I − 2 − ε > 1, so the conclusion
stands. Away from 𝓘⁺ the coefficients are the Cartesian components times bounded factors. So the coefficients lie in
C^(k−3,(2ℓ_I,ℓ_+,ℓ_K))_b, which is the claim. ∎

In dimension 3 + 1 the coefficient x_I⁻²h_00 has order 4γ_Υ, which is the restriction ℓ_I < 2γ_Υ of [Hin26]; in
dimension 4 + 1 the extra power of x_I in the radiation order 3/2 removes it. As in [Hin26, footnote 103], ℓ_I is an
e3b-weight in [[lem:iii-i-2-2]], [[cor:iii-i-5-2]] and the proof of [[thm:iii-i-5-3]], and a b-weight at 𝓘⁺ in
[[def:iii-i-1-1]] and [[prop:iii-i-4-1]]; the two are not compared.

*Consequences.* By [[lem:iii-i-2-2]] with ℓ_I = ½ and [[lem:ii-c-3-2]], dt^♭_* is past timelike for
g = g_(b₀,b,−S) + h when |b − b₀|, |S| and ‖h‖_(𝒳⁴) are small: g − g_(b₀) = (g_(b₀,b,−S) − g_(b₀)) + h, and
g_(b₀,b,−S) − g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b) ([[lem:iii-i-3-6]] with the argument of [[lem:iii-i-2-2]]; it
vanishes at b = b₀, S = 0 and depends continuously on (b, S)). Such g lie in 𝒢^((0;k−3),(2ℓ_I,ℓ_+,ℓ_K))_(e3b;b)
relative to g_b, that is, they are asymptotically Kerr in the sense of [Hin26c, Definition 5.15]. Smallness of h in
H^(3,(1,0,0))_b makes x_I²ρ_+²g non-degenerate and Lorentzian ([[rem:s05-metric-class]] (b)): by the
coefficients in the proof of [[lem:iii-i-2-2]], the weight 1 at 𝓘⁺ suffices ([Hin26, footnote 104]).

### The structure in the forward cone {#sec:iii-i-3}

This section is [Hin26, Proposition 11.6 and Remark 11.7] in dimension 4 + 1.

*Coordinates.* On U⁺ := Ω_* ∩ {|x| ≥ 4R₁} put

    ρ_+ := 1/(t_* + 1),   ρ_I := (t_* + 1)/|x|,   ρ := |x|⁻¹ = ρ_+ρ_I,   X_+ := ρ_+∂_(ρ_+),   X_I := ρ_I∂_(ρ_I).
                                                                                                  {#eq:iii-i-3-1}

With ω these are smooth coordinates near 𝓘⁺ ∩ ι⁺, and there they are smooth positive multiples of the functions ρ_+,
ρ_I of [[eq:iii-b-2-2]] (by [[eq:iii-b-2-2]] and t_* = t − |x| + C′ − 8m₀|x|⁻¹ on {|x| ≥ 3R₁}); so they define the
same faces and the same b-structure.

**Lemma {#lem:iii-i-3-1}** (The vector fields.) On U⁺_C := U⁺ ∩ {ρ_I ≤ C}, C ≥ 1 fixed, exactly

    ∂_(t_*)|_(ρ,ω) = −ρ_+(X_+ − X_I),        ρ∂_ρ|_(t_*,ω) = X_I.                                        {#eq:iii-i-3-2}

The Cartesian derivatives ∂_t, ∂_(x^i) lie in ρ_+𝒱_b(U⁺_C), and |x|⁻¹∂_ω ∈ ρ_+ρ_I𝒱_b(U⁺_C). Near K⁺ (ρ_I → ∞) the
functions [[eq:iii-i-3-1]] are not coordinates, and the weights there are those of [[eq:iii-b-2-2]]; [[lem:iii-i-3-2]]
and [[prop:iii-i-3-3]]–[[prop:iii-i-3-4]] use this lemma near 𝓘⁺ ∪ (ι⁺)° only, and the proof of [[prop:iii-i-3-4]]
treats K⁺ separately.

*Proof.* At fixed ρ, ∂_(t_*)ρ_+ = −ρ_+² and ∂_(t_*)ρ_I = ρ = ρ_+ρ_I; at fixed t_*, ρ_+ is constant and ρ_I is a constant
multiple of ρ. This gives [[eq:iii-i-3-2]]. Then ∂_t|_x = ∂_(t_*)|_x, and ∂_|x||_t = ∂_|x||_(t_*) − ψ′(|x|)∂_(t_*) with
∂_|x||_(t_*) = −ρ · ρ∂_ρ = −ρ_+ρ_I X_I and ψ′ bounded; finally ∂_(x^i) = ω^i∂_|x| + |x|⁻¹(·)∂_ω, and
|x|⁻¹∂_ω = ρ_+ρ_I∂_ω. ∎

**Lemma {#lem:iii-i-3-2}** (The background in the cone.) On U⁺ ∩ {ρ_I ≤ 1}, in the frame of products of dt_*, dx^i,

    L_b = ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − S̄) + R̃_b,        R̃_b ∈ ρ_+²ρ_I² Diff²_b(U⁺; S²T*),            {#eq:iii-i-3-3}

with S̄ of [[lem:iii-f-2-1]] (2) and R̃_b with coefficients smooth on U⁺.

*Proof.* This is the proof of [[lem:iii-c-4-1]] with [[eq:iii-i-3-2]] in place of [[eq:iii-c-1-4]]. By
[[eq:iii-f-2-2]]–[[eq:iii-f-2-3]],

    2L_b = −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S̄) + (2L̄)^∧(0) − g_b^00 ∂²_(t_*) + Q_b∂_(t_*) + R_b,

where (2L̄)^∧(0) ∈ ρ²Diff²_b is the stationary part of the model 2L̄. The last four terms lie in ρ²Diff²_b with
ρ = ρ_+ρ_I, since ρ∂_ρ|_(t_*) and ∂_ω are b-vector fields on U⁺ and ∂_(t_*) ∈ ρ_+𝒱_b. The first is

    2ρ_+(X_+ − X_I)ρ_+ρ_I(X_I − 3/2 − S̄) = 2ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − S̄),

as (X_+ − X_I)(ρ_+ρ_I) = 0 and S̄ depends on ω only. Halving gives [[eq:iii-i-3-3]]. ∎

This is [[eq:iii-c-4-2]] with ρ_+ for ρ_0 and −(X_+ − X_I) for X_0 − X_I; [Hin26, (11.17a)] has 1 for 3/2 and the
h-dependent A^h, B^h.

*The background class in the cone.* 𝒢⁺ is the set of Lorentzian metrics g_0 on Ω_*, smooth on M, with, on
U⁺ ∩ {ρ_I ≤ 1}, g_0 − η ∈ ρ_+²ρ_I²C^∞ and π(g_0 − η) ∈ ρ_+²ρ_I³C^∞ for π ≠ π₁₁ ([[def:iii-c-3-4]] with ρ_+ for ρ_0).

**Proposition {#prop:iii-i-3-3}** (The leading part at 𝓘⁺; [Hin26, Proposition 11.6 (1)] in dimension 4 + 1.) Let
g_1, g_0 ∈ 𝒢⁺, k ≥ 5, and h ∈ 𝒳^k with small H^(3,(1,0,0))_b-norm. Then g := g_1 + h satisfies, on U⁺ ∩ {ρ_I ≤ 1}, in
the splitting [[eq:iii-c-1-6]],

    L^(g,g_0) ≡ ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − Ā)
        mod (ρ_+²ρ_I²C^∞ + H^(k−2,(ℰ_I^tot,a_I),(ℰ_++2,a_++2))_b) Diff²_b.                              {#eq:iii-i-3-4}

For h ∈ H^(k,(⟨(3,0)⟩₀,a_I),(ℰ_+,a_+),·)_b the same holds with (2, 0) in place of ℰ_I^tot.

*Proof.* This is the proof of [[prop:iii-c-4-4]] on U⁺, with [[lem:iii-i-3-1]]–[[lem:iii-i-3-2]] in place of
[[lem:iii-c-1-1]] and [[lem:iii-c-4-1]], and with the expansion of g⁻¹ after [[prop:iii-i-3-4]] in place of the Neumann
series used there (whose convergence needs smallness in H^k). The change of frame ([[lem:iii-c-1-3]], with
ρ² = ρ_+²ρ_I²) turns S̄ into Ā ([[lem:iii-c-4-2]]). The backgrounds (g_1, g_0) differ from (g_b, g_b) by
ρ_+²ρ_I²C^∞, which with the two factors ρ_+ from the derivatives gives ρ_+⁴ρ_I²C^∞ Diff²_b. The perturbation, counted
as in [[lem:iii-c-4-3]] with Cartesian derivatives in ρ_+𝒱_b ([[lem:iii-i-3-1]]) and c_C, c_Υ ∈ ρ_+ρ_I C^∞, gives
ρ_+² times H^(k−2)-functions of the index sets of h: ℰ_I^tot at 𝓘⁺ ([[lem:iii-c-3-2]] (b)–(c)), and ℰ_+ at ι⁺
(jℰ_+ ⊂ ℰ_+ for the Taylor terms of g⁻¹, [[lem:iii-c-2-1]] with the weights (a_I, a_+)). ∎

So, as at I⁰ ∩ 𝓘⁺, the leading part has the constant lower-triangular Ā and no h-dependent term. The terms A^h − A_0
and B^h of [Hin26] are part of the error, of 𝓘⁺-order 3/2 against the leading order 1 ([[prop:iii-c-4-4]],
[[rem:iii-c-4-5]]). The edge-b form [Hin26, (11.17b)] is not needed: [[cor:iii-i-5-2]] uses [[eq:iii-i-3-7]] instead.

**Proposition {#prop:iii-i-3-4}** (The difference from L_b; [Hin26, Proposition 11.6 (2)] in dimension 4 + 1.) Let
g_0 = g_(b₀,b,−S), or more generally g_0 ∈ 𝒢⁺ with ([Hin26, (11.15a)–(11.15b)])

    g_0 − g_(b₀) ∈ H^(∞,(⟨(3,0)⟩₀,∞),((2,0),∞),(0,0))_b(Ω_*),      g_0 = g_b near K⁺,          {#eq:iii-i-3-5}

let h ∈ 𝒳^k, k ≥ 5, with small H^(3,(1,0,0))_b-norm, and g := g_(b₀,b,−S) + h ([Hin26, (11.16)]). Then on Ω_*

    L^(g,g_0) − L_b ∈ H^(k−2,(ℰ_I^tot,a_I),(ℰ_++2,a_++2),a_K)_b Diff²_b(Ω_*; S²T*),                      {#eq:iii-i-3-6}

    2L^(g,g_0) − 2L_b ∈ x_I²ρ_+² H^(k−2,(2ℓ_I,ℓ_+,ℓ_K))_b Diff²_(e3b)(Ω_*; S²T*),                       {#eq:iii-i-3-7}

for ℓ_I, ℓ_+, ℓ_K as in [[eq:iii-i-2-2]], the latter with norm bounded by C(|b − b₀| + |S| + ‖h‖_(𝒳^k)), C depending
on k and on an upper bound for ‖h‖_(𝒳^k).

[Hin26, (11.18a)–(11.18b)] carry in addition the term χ_Iρ_Iρ_+²((A^h − A_0)(ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+)) + ρ_+⁻¹B^h),
which contains a term of leading order at 𝓘⁺; in dimension 4 + 1 it is part of the error.

*Proof.* Write g − g_b = (g_(b₀,b,−S) − g_b) + h, and g_0 − g_b. By [[lem:iii-i-3-6]] below, g_(b₀,b,−S) − g_b is
supported where χ_K < 1, so away from K⁺, and lies in H^(∞,(⟨(3,0)⟩₀,∞),((2,0),∞),∞)_b ⊂ 𝒳^∞ ([[def:iii-c-3-3]] and
[[lem:iii-c-3-2]] (a); (2, 0) ∈ ℰ_+); the same holds for g_0 − g_b under [[eq:iii-i-3-5]]. So both differences are of
the class of h, and [[lem:iii-c-4-3]] applies to L^(g,g_0) − L^(g_b,g_b) with δ in 𝒳^k. Cartesian derivatives lie in
ρ_+𝒱_b near 𝓘⁺ ∪ ι⁺ ([[lem:iii-i-3-1]], and in the interior of ι⁺ by homogeneity) and in ρ_+𝒱_(3b) ⊂ ρ_+𝒱_b near K⁺
(as in [Hin26]); the counting gives ρ_+² times H^(k−2)-functions of the class of 𝒳^k, which is [[eq:iii-i-3-6]]
(ρ_+² shifts the data at ι⁺ by 2; at K⁺, ρ_+² is bounded and the weight is a_K).

For [[eq:iii-i-3-7]]: near 𝓘⁺, ∂_0 ∈ x_I²ρ_+𝒱_(e3b), ∂_1 ∈ ρ_+𝒱_(e3b) and |x|⁻¹∂_ω ∈ x_Iρ_+𝒱_(e3b) ([Hin26, (11.12)],
which does not depend on the dimension), so all Cartesian derivatives lie in ρ_+𝒱_(e3b). A coefficient c of the
counting carries a factor δ of x_I-order at least 3 (the least slot order, 3/2 in ρ_I), so c ∂∂ ∈ x_I²ρ_+² ·
x_I · (⋯) Diff²_(e3b), and x_I ≤ x_I^(2ℓ_I); at ι⁺ the factor has order > 1 ≥ ℓ_+, and at K⁺ order a_K ≥ ℓ_K. The
b-regularity of the coefficients is k − 2, and the e3b-vector fields are b-vector fields on M_(1/2). The norm bound is
linear in the factors δ, whose norms add up to at most C(|b − b₀| + |S|) + ‖h‖; the other factors are bounded in terms
of an upper bound for ‖h‖_(𝒳^k). ∎

*The inverse metric.* Smallness enters only through g⁻¹ = (g_b + δ)⁻¹, δ := g − g_b. Write

    (g_b + δ)⁻¹ = Σ_(j≤N) (−g_b⁻¹δ)^j g_b⁻¹ + R_N,        R_N := (−g_b⁻¹δ)^(N+1)(g_b + δ)⁻¹.

(g_b + δ)⁻¹ is a smooth function of δ for δ pointwise small, which the H^(3,(1,0,0))_b-smallness gives by Sobolev
embedding; so by Moser's composition estimate (the tame estimates of [[sec:ii-a-9]]), (g_b + δ)⁻¹ − g_b⁻¹ is bounded in
H^k_b with weights 0, by a constant depending on an upper bound for ‖δ‖_(H^k). The factor (−g_b⁻¹δ)^(N+1) has N + 1
times the least orders of δ, which are positive at each face; so for N large, R_N lies in H^k_b with weights beyond
every weight in [[eq:iii-i-3-4]], [[eq:iii-i-3-6]] and [[eq:iii-i-3-7]], and adds no expansion term. The Taylor terms
are products, handled by [[lem:iii-c-2-1]]. This replaces the Neumann series of [[prop:iii-c-4-4]], whose convergence
needs smallness in H^k.

**Remark {#rem:iii-i-3-5}** ([Hin26, Remark 11.7] in dimension 4 + 1.) g_(b₀) + h and g_(b₀,b,0) + h differ near
(ι⁺)° by χ_K(g_b − g_(b₀)) ∈ ρ_+²C^∞, which is absorbed into h as (2, 0) ∈ ℰ_+. The same holds for the boost:
g_(b₀,b,−S) − g_(b₀,b,0) = (1 − χ_K)(φ_(−S)^* g_(b₀) − g_(b₀)) ∈ H^(∞,(⟨(3,0)⟩₀,∞),((2,0),∞),∞)_b
([[lem:iii-i-3-6]]). This is where the condition (2, 0) ∈ ℰ_+ of [[eq:iii-i-1-3]] is used.

**Lemma {#lem:iii-i-3-6}** (The background differences.) For |b − b₀| and |S| small, g_(b₀,b,−S) satisfies
[[eq:iii-i-3-5]] and lies in 𝒢⁺; g_(b₀,b,−S) − g_b is supported in {χ_K < 1} and lies in
H^(∞,(⟨(3,0)⟩₀,∞),((2,0),∞),∞)_b(Ω_*), with seminorms O(|b − b₀| + |S|).

*Proof.* We have g_(b₀,b,−S) − g_b = (1 − χ_K)(φ_(−S)^* g_(b₀) − g_(b₀)) + (1 − χ_K)(g_(b₀) − g_b). On
supp(1 − χ_K) ∩ Ω_*, χ_IVP = 1 and the flow of V(S) is the boost: this is the first alternative of [[lem:iii-b-5-2]],
with supp χ^♭_K ⊂ χ_K⁻¹(1); on its second alternative, {|x| < 6R₁}, the difference is smooth and supported in a
compact set away from the faces at infinity, as that alternative of [[lem:iii-b-5-2]] states, hence in the class. So
by [[eq:iii-b-5-3]], φ_(−S)^* g_(b₀) − g_(b₀) = |x|⁻²h_(−S)(ω)(dx¹)² + ρ_0²ρ_I³ρ_+² C^∞ with h_(−S) = O(|S|); and by
[[prop:iii-b-3-6]], g_(b₀) − g_b = (m₀ − m)|x|⁻²(dx¹)² + O(|b − b₀|)|x|⁻³C^∞ on {|x| ≥ 3R₁}. Near 𝓘⁺,
|x|⁻²(dx¹)² is the slot π₁₁ at ρ_I-order 2 and ι⁺-order 2, and |x|⁻³ is of orders 3; in the interior of ι⁺,
|x|⁻² ∈ ρ_+²C^∞. This is the class stated, as 1 − χ_K is smooth on M. For [[eq:iii-i-3-5]]: g_(b₀,b,−S) − g_(b₀) =
(g_(b₀,b,−S) − g_b) + (g_b − g_(b₀)), the last term being independent of χ_K, smooth at K⁺ and of the same classes; and
g_(b₀,b,−S) = g_b on χ_K⁻¹(1), a neighbourhood of K⁺. 𝒢⁺: near 𝓘⁺ ∩ ι⁺, g_(b₀,b,−S) = φ_(−S)^* g_(b₀), and
g_(b₀) − η = m₀|x|⁻²(dx¹)² has the slot π₁₁ only. ∎

### Forward mapping {#sec:iii-i-4}

This section is [Hin26, Proposition 11.8 and Corollary 11.9] in dimension 4 + 1.

**Proposition {#prop:iii-i-4-1}** (Forward mapping; [Hin26, Proposition 11.8] in dimension 4 + 1.) Let g_0 ∈ 𝒢⁺
satisfy [[eq:iii-i-3-5]], let h and g be as in [[prop:iii-i-3-4]], and let 3/2 < ℓ_I < a_I + ½,
0 < ℓ_+ < a_+ + min Re ℰ_+, ℓ_K ∈ ℝ and k ≥ 5. Then

    L^(g,g_0) : H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b(Ω_*) → H^(k−2,(⟨ℰ_I^C+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2),ℓ_K)_b(Ω_*),
                                                                                                  {#eq:iii-i-4-1}

and, if moreover ℓ_+ ≤ max(a_+, min Re ℰ_+), then for every ε > 0

    L^(g,g_0) − L_b : H^(k,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b
                          → H^(k−2,(⟨ℰ_I^C+1⟩′,ℓ_I+1),(2ℰ_++2,ℓ_++2+m_+−ε),ℓ_K+a_K)_b,
    m_+ := min(a_+, min Re ℰ_+).                                                                   {#eq:iii-i-4-2}

[Hin26, (11.19)] has ℓ_+ + 3 − ε (m_+ = 1) and ℓ_K + 2 + ε_K (a_K = 2 + ε_K). The upper bounds on ℓ_I and ℓ_+ are
those of the products ([[lem:iii-c-2-1]]): a coefficient of the error with no expansion beyond its 𝓘⁺-weight a_I,
acting on the radiation term ρ_I^(3/2) of π̸₀ u, gives ρ_I^(a_I+3/2) times a function with no expansion, and likewise
at ι⁺. [Hin26, Proposition 11.8] is stated for all weights, but its products need the same restrictions (in dimension
3 + 1, ℓ_I < a_I and ℓ_+ < a_+ + min Re ℰ_+, and ℓ_+ ≤ max(a_+, min Re ℰ_+) for [Hin26, (11.19)]).
[[cor:iii-i-4-2]] (ℓ = a) lies inside this range, and the later chapters keep their weights in it.

*Proof.* [[eq:iii-i-4-1]]. Near 𝓘⁺ (on U⁺ ∩ {ρ_I ≤ 1}) this is the proof of [[prop:iii-c-5-2]], with
[[prop:iii-i-3-3]] in place of [[prop:iii-c-4-4]], ι⁺ in place of I⁰ and ℰ_+ in place of ℰ_0. The leading part
ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − Ā) has the slot-by-slot effect computed there: X_+ − X_I preserves index sets,
X_I − 3/2 − Ā_jj annihilates the exceptional terms, and the couplings of Ā act as there; the factor ρ_+²ρ_I shifts the
data by 2 at ι⁺ and by 1 at 𝓘⁺. The C^∞ error gives ℰ_I^tot + 2 ⊂ ℰ_I^C + 1 and ℰ_+ + 2. The perturbation error gives,
by [[lem:iii-c-2-1]], 2ℰ_I^tot ⊂ ℰ_I^C + 1 at the weight ℓ_I + 1 and 2ℰ_+ + 2 ⊂ ℰ_+ + 2 at the weight ℓ_+ + 2. The
inequalities [[lem:iii-c-2-1]] asks are ℓ_I + 1 < ℓ_I + 3/2, ℓ_I + 1 < a_I + 3/2 (by the hypothesis ℓ_I < a_I + ½) and
ℓ_I + 1 ≤ a_I + ℓ_I; and ℓ_+ + 2 < ℓ_+ + 2 + min Re ℰ_+, ℓ_+ + 2 < a_+ + 2 + min Re ℰ_+ (by the hypothesis on ℓ_+) and
ℓ_+ + 2 ≤ a_+ + 2 + ℓ_+. Away from 𝓘⁺, near ι⁺ ∪ K⁺: L_b ∈ ρ_+²Diff²_b near (ι⁺)° (Cartesian derivatives lie in
ρ_+𝒱_b) and L_b ∈ Diff²_b near K⁺, which gives [[eq:iii-i-4-1]] there, and L^(g,g_0) − L_b is handled by
[[eq:iii-i-3-6]] and [[lem:iii-c-2-1]].

[[eq:iii-i-4-2]]. Only ι⁺ and K⁺ need an argument, as at 𝓘⁺ [[eq:iii-i-4-2]] is [[eq:iii-i-4-1]]. By
[[eq:iii-i-3-6]], the coefficients of L^(g,g_0) − L_b have the data (ℰ_+ + 2, a_+ + 2) at ι⁺ and the weight a_K at K⁺.
[[lem:iii-c-2-1]] gives the product index set 2ℰ_+ + 2 at the weight ℓ_+ + 2 + m_+ − ε, which is below each of
ℓ_+ + 2 + min Re ℰ_+, ℓ_+ + 2 + a_+ and a_+ + 2 + min Re ℰ_+ (the last because ℓ_+ + m_+ ≤ a_+ + min Re ℰ_+ when
ℓ_+ ≤ max(a_+, min Re ℰ_+)), and the weight ℓ_K + a_K at K⁺. ∎

**Lemma {#lem:iii-i-4-3}** (The curvature of the patched background.) For |b − b₀| and |S| small, Ric(g_(b₀,b,−S)) is
supported in supp χ_K ∩ supp(1 − χ_K) and lies in ρ_+⁴C^∞ near (ι⁺)°, with seminorms O(|b − b₀| + |S|).

*Proof.* g_1 := φ_(−S)^* g_(b₀) and g_2 := g_b are Ricci flat, so Ric(g_(b₀,b,−S)) vanishes on the interior of
χ_K⁻¹({0, 1}). So it is supported in supp χ_K ∩ supp(1 − χ_K), whose closure meets ∂M only in a compact subset of
(ι⁺)°: χ_K = 1 near K⁺ and χ_K = 0 near 𝓘⁺, since χ^♭_K = 1 on {|x| < t/10, t > 60R₁} and supp χ^♯_K ⊂ {|x| < t/2}
([[sec:iii-b-5]]). Near (ι⁺)°, g_i − ḡ = k_i ∈ ρ_+²C^∞ ([[lem:iii-i-3-6]], and [[lem:iii-b-5-1]] for the pullback),
and Cartesian derivatives lie in ρ_+𝒱_b. With k := (1 − χ_K)k_1 + χ_K k_2, Ric(ḡ + k) = DRic(k) + Q(k), Q at least
quadratic, and Q(k) ∈ ρ_+⁶C^∞ (two factors k, two derivatives). Further DRic(k) = (1 − χ_K)DRic(k_1) +
χ_K DRic(k_2) + E, with DRic(k_i) = −Q(k_i) ∈ ρ_+⁶C^∞ and E the terms with a derivative on χ_K: ∂χ_K ∈ ρ_+C^∞ and
∂²χ_K ∈ ρ_+²C^∞ (χ_K is smooth on M), times ∂k_i ∈ ρ_+³C^∞ and k_i ∈ ρ_+²C^∞ respectively; so E ∈ ρ_+⁴C^∞. Where χ_K
is locally constant, E = 0 and the count gives ρ_+⁶. The size is linear in k_1 − k_2 (for k_1 = k_2 the patched metric
is Ricci flat), and k_1 − k_2 = O(|b − b₀| + |S|) by [[lem:iii-i-3-6]]. ∎

In dimension 3 + 1 the same count gives ρ_+³, the order P(g_0, g_0) ∈ ρ_+³C^∞ of [Hin26].

**Corollary {#cor:iii-i-4-2}** (The gauge-fixed Einstein operator; [Hin26, Corollary 11.9] in dimension 4 + 1.) Let
g_0 = g_(b₀,b,−S) with |b − b₀| and |S| small, and g = g_0 + h with h ∈ 𝒳^∞ of small H^(3,(1,0,0))_b-norm. Then

    P_0(h, S, b) := P(g, g_0) = Ric(g) − δ^*_(g_0,E_C) Υ^(E_Υ)(g, g_0)
                 ∈ H^(∞,(⟨ℰ_I^C+1⟩′,a_I+1),(ℰ_++2,a_++2),a_K)_b(Ω_*).                                   {#eq:iii-i-4-3}

*Proof.* P(g_0, g_0) = Ric(g_0), as Υ^(E_Υ)(g_0, g_0) = 0 (the proof of [[cor:iii-c-5-3]]). By [[lem:iii-i-4-3]] it
lies in ρ_+⁴C^∞, with support whose closure meets ∂M in a compact subset of (ι⁺)°, and (4, 0) ∈ ℰ_+ + 2 as
(2, 0) ∈ ℰ_+. And P(g, g_0) − P(g_0, g_0) = ∫_0^1 L^(g_0+sh,g_0)h ds, which lies in the space by [[prop:iii-i-4-1]]
(with g_1 = g_0, uniformly in s), as in [[cor:iii-c-5-3]]. ∎

### Admissibility and forward solutions {#sec:iii-i-5}

This section is [Hin26, Corollary 11.10 and Theorem 11.12] in dimension 4 + 1.

#### The orders {#sec:iii-i-5-1}

[[thm:iii-h1-1-3]] holds for orders in its class 𝒪_c, the orders of [[def:ii-c-2-4]] with the conditions (C1)–(C3) of
[[def:iii-h1-1-1]]. The orders used by the forward solution theory of [[ch:s09]] are built by the construction of
[[prop:ii-c-5-1]] ([[sec:ii-c-5-2]]: 𝗌 = s_in − (s_in − s_out)χ) and shifted by constants ([[lem:ii-f1-2-3]] and
[[rem:ii-f1-7-1]]). The next lemma shows that they lie in 𝒪_c, so that [[thm:iii-h1-1-3]] supplies the
2-admissibility those results assume.

**Lemma {#lem:iii-i-5-1}** (The orders lie in 𝒪_c.) The order 𝗌 of [[prop:ii-c-5-1]], read over K⁺ as a
t_*-translation-invariant function ([[prop:ii-c-5-1]] (1)), satisfies (C1)–(C3) of [[def:iii-h1-1-1]] with s_c = s_in;
and so does 𝗌 + c for every constant c.

*Proof.* Over K⁺, ψ_0(x_I) = 0 (x_I ≥ ϵ_I there), so 𝗌 = s_in − (s_in − s_out)χ_ι with

    χ_ι = φ(f_W/δ) ψ̃(ϵ_ιδ f_T) ψ(|η̂_(3b)|²/(2δ)) Ψ(σ_(3b)²/|ν|²_(3b))

on Ω_ι and χ_ι = 0 elsewhere ([[eq:ii-c-5-3]]; the factor ψ̃ vanishes where ϵ_ιδ f_T ≤ 4, which holds near the inner
boundary of Ω_ι).

(C1): Ψ = 0 on (−∞, 0.04], so χ_ι = 0 on {σ_(3b)² ≤ 0.04|ν|²_(3b)} ⊃ {σ = 0}, and 𝗌 = s_in there.

(C2): on supp φ(f_W/δ), |ξ̂_(3b)| < δ/2, so f_T = r(1 − ξ̂_(3b)) < 2r, and ψ̃(ϵ_ιδ f_T) = 0 for r ≤ 2/(ϵ_ιδ); so
𝗌 = s_in over {r ≤ 2/(ϵ_ιδ)} ⊃ {r ≤ r_Γ}, the construction having chosen 1/(ϵ_ιδ) > r_Γ. (C2) is in any case implied
by [[def:ii-c-2-4]] (3), as noted after [[def:iii-h1-1-1]].

(C3): −𝖧𝗌 = (s_in − s_out)𝖧χ_ι for the stationary G_0 (𝖧 = 𝖧^(3b) on Σ⁺, a positive multiple of 𝖧_(G_0)). On Σ⁺ over Ω_ι
the factors ψ and Ψ equal 1 ([[lem:ii-c-5-3]] and [[lem:ii-c-5-5]] (b): σ_(3b)² ≥ 0.09|ν|² and |η̂_(3b)|² ≤ 3δ < 4δ),
and 𝖧 applied to the other two factors is ≥ 0 ([[lem:ii-c-5-5]] (a), (c), with ψ̃′ ≥ 0, and φ′(f_W/δ) ≥ 0 where f_W ∈
[−δ/2, −δ/4], φ being even with φ′ ≤ 0 on [0, ∞); by [[lem:ii-c-5-5]] (b) the other branch ξ̂_(3b) < −δ/8 does not meet
Σ). Each of these holds with a margin off Σ. The proof of [[lem:ii-c-5-3]] shows |G_(3b)| > 0.0125|ν|²_(3b) where
σ_(3b)² < 0.09|ν|²_(3b), so Ψ = 1 on W_1 := {|G_(3b)| < 0.0125|ν|²_(3b)}. On W_2 := {|σ_(3b)⁻²G_(3b)| < δ/16} the
argument of [[lem:ii-c-5-5]] (b), with the error δ/16 + δ/16, still gives ξ̂_(3b) ≥ −δ/8 and |η̂_(3b)|² ≤ (3/2)δ + δ/8 <
4δ, so ψ = 1 there. [[lem:ii-c-5-5]] (a) and (c) are proved from [[eq:ii-b-3-4]] and [[eq:ii-c-5-2]] without using Σ
(𝖧̄f_T = 2ϱ⁻¹ and 𝖧̄f_W = 2(2 − ξ̂_(3b))ξ̂_(3b) wherever σ_(3b) ≠ 0), so they hold on W_1 ∩ Ω_ι ∩ {|ξ̂_(3b)| ≤ δ/2}. Any
other positive rescaling of the Hamilton field, or any other defining symbol of Σ (such as 𝖧^♮ of [[sec:i-b-1-4]]),
differs from 𝖧^(3b) by a positive factor and by terms vanishing on Σ, of size O(|σ_(3b)⁻²G_(3b)|) relative to the
margins δ/8 and ϱ⁻¹ of (a) and (c). So on a thinner neighbourhood W ⊂ W_1 ∩ W_2 of Σ the monotonicity 𝖧𝗌 ≤ 0 holds for
it too. On Σ⁻ the same holds by the evenness of the construction of [[sec:ii-c-5-2]] under the antipodal map. Outside
Ω_ι the order is constant. Constants added to 𝗌 change none of this. ∎

#### Admissibility {#sec:iii-i-5-2}

**Corollary {#cor:iii-i-5-2}** (Admissibility relative to 2L_b; [Hin26, Corollary 11.10] in dimension 4 + 1.) Let
g_0 = g_(b₀,b,−S) (or g_0 with [[eq:iii-i-3-5]]) and g := g_0 + h, h ∈ 𝒳^k, k ≥ 5, with small 𝒳⁵-norm. Then
P := 2L^(g,g_0) is admissible relative to P_0 := 2L_b of class ((0;k−5),(2ℓ_I,ℓ_+,ℓ_K)) ([[def:ii-c-3-3]]) for every
ℓ_I ∈ (0, ½], ℓ_+ ∈ (0, 1] and ℓ_K ∈ (2, a_K], with p_0 = p̃_1 = 0, whenever P_0 is 2-admissible with sf-loss 0 and
margin 1 for the orders of 𝒪_c ([[def:iii-h1-1-1]]). By [[thm:iii-h1-1-3]] this holds at b = b₀, and by
[[thm:iii-h2-2-1]] at every b of the neighbourhood B̄_1 of [[sec:iii-h2-0]], for every k.

*Proof.* (1) σ_2(P) = G_g, with g − g_b = (g_0 − g_b) + h ∈ 𝒢̃^((0;k−3),(2ℓ_I,ℓ_+,ℓ_K)) by [[lem:iii-i-2-2]] and
[[lem:iii-i-3-6]]. (2) With p_0 = p̃_1 = 0, P̃ = P − P_0, which by [[eq:iii-i-3-7]] and Sobolev embedding
(H^(k−2)_b ⊂ C^(k−5)_b, three derivatives for dim M = 5) lies in x_I²ρ_+² C^(k−5,(2ℓ_I,ℓ_+,ℓ_K))_b Diff²_(e3b).
(3) p_1 = S|_(∂X), which in the splitting [[eq:iii-c-1-6]] is Ā, lower triangular with real diagonal
([[lem:iii-c-4-2]]), and p_0 = 0 is strictly lower triangular. The conditions ℓ_+ > δ = 0 and ℓ_K > ℵ = 2 of
[[def:ii-c-3-3]] hold. ∎

[Hin26] has p̃_1 = (A^h − A_0)|_(𝓘⁺) and p_0 = 4ρ_+⁻¹B^h|_(𝓘⁺), of class ρ_+^(ℓ_+)C^(k−4)_b, and needs ℓ_+ ∈ (δ, 1)
and ℓ_I < min(2γ_Υ, ½).

#### Forward solutions at b₀ {#sec:iii-i-5-3}

**Theorem {#thm:iii-i-5-3}** (Forward solutions at b₀; [Hin26, Theorem 11.12] in dimension 4 + 1, at b₀.) Let
β_+ ∈ (½, 3/2) and β_I ∈ (β_+, 3/2). There are ε_0 > 0 and d ∈ ℕ such that for every k ∈ ℕ₀, every S ∈ 𝒮_1 with
|S| < ε_0, every h ∈ 𝒳^(k+d) with ‖h‖_(𝒳^d) < ε_0, and every

    f ∈ H^(k+d,(β_I+1,β_++2,1/2))_b(Ω_*; S²T*)^(•,−),                                                   {#eq:iii-i-5-1}

the forward solution u of L^(g,g_0)u = f, g_0 := g_(b₀,b₀,−S), g := g_0 + h, satisfies

    u ∈ H^(k,(β_I,β_+,−3/2))_b(Ω_*; S²T*)^(•,−),
    ‖u‖_(H^(k,(β_I,β_+,−3/2))_b)
        ≤ C_k (‖f‖_(H^(k+d,(β_I+1,β_++2,1/2))_b) + ‖h‖_(𝒳^(k+d)) ‖f‖_(H^(d,(β_I+1,β_++2,1/2))_b)).       {#eq:iii-i-5-2}

For k ≥ 1, u depends continuously on (S, h) in H^(k−1,(β_I−ς,β_+−ς,−3/2−ς))_b for every ς > 0. The densities are μ_b.

[Hin26] has β_+ ∈ (½, ½ + ε_ind), β_I ∈ (β_+, 1), an sf-loss δ > β_+ − ½ (so that u has the weight β_+ − δ), and b
near b₀. Here δ = 0, the window of β_+ is (½, 3/2), and β_I reaches 3/2, the order of the radiation field. [Hin26,
(11.23)] writes the K⁺-weights −2 for u and 0 for f where [Hin26, (11.22) and (11.21)] have −3/2 and ½; with μ_b
throughout, [[eq:iii-i-5-2]] uses the latter. [[cor:iii-h2-5-1]] extends the theorem to every b near b₀, with
constants independent of b and continuity in b.

*Proof.* Apply [[thm:ii-f1-1-1]] in the form of [[cor:ii-f1-1-2]], with P_0 := 2L_(b₀), ℵ = 2, the sf-weight
α_+ := β_+ − 5/2 and α_I := β_I − 2, and with [[rem:ii-f1-7-1]] for the relaxed admissibility with margin d_ℵ = 1
(d raised by 1). Its hypotheses hold.

(i) P_0 is 2-admissible with sf-weight α_+, sf-loss 0 and margin 1, by [[thm:iii-h1-1-3]] at b₀ for every k, as
α_+ + 2 = β_+ − ½ ∈ (0, 1), for the orders of [[ch:s09]], which lie in 𝒪_c by [[lem:iii-i-5-1]]. [[eq:ii-f-8-6]], where
the admissibility enters ([[rem:ii-f-8-2]]), uses these orders over K⁺ with the weights α_+, −2 and margin 1, as
[[def:iii-h1-1-1]] asks.

(ii) [[eq:ii-f1-1-3]]: α_I < −½ + S̄ = −½ (S̄ = 0, the least eigenvalue of Ā, [[eq:iii-c-4-3]]) is β_I < 3/2, and
α_+ < α_I − ½ is β_+ < β_I.

(iii) P = 2L^(g,g_0) is admissible relative to P_0 of class ((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)) for fixed ℓ_I ∈ (0, ½],
ℓ_+ ∈ (0, 1] and ℓ_K ∈ (2, a_K], by [[cor:iii-i-5-2]] with h ∈ 𝒳^(k+d+5) (d raised by 5), and
‖P − P_0‖_((0;d)) ≤ C(|S| + ‖h‖_(𝒳^(d+5))) < ε′_0 for ε_0 small ([[prop:iii-i-3-4]], [[eq:iii-i-3-7]]).

The tame form: ‖P − P_0‖_((0;k+d)) ≤ C_k(|S| + ‖h‖_(𝒳^(k+d+5))) by [[eq:iii-i-3-7]], whose coefficients are polynomial
in h, g⁻¹ and their derivatives, with tame (Moser) bounds in the b-regularity for ‖h‖_(𝒳^(d+5)) small (the tame
product estimates of [[sec:ii-a-9]]). With [[eq:ii-f1-1-5]] and C_k|S| ‖f‖_(H^d) ≤ C_k‖f‖_(H^(k+d)), this is
[[eq:iii-i-5-2]]. The weights: [[cor:ii-f1-1-2]] with b_I = α_I + 2 = β_I, b_+ = α_+ + 5/2 = β_+, sf-loss 0, and the
K⁺-weights ½ for f and −ℵ + ½ = −3/2 for u. Continuity: the last statement of [[thm:ii-f1-1-1]], P depending
continuously on (S, h) in the norm of [[eq:iii-i-3-7]]. ∎

**Remark {#rem:iii-i-5-5}** ([Hin26, Remark 11.13] in dimension 4 + 1.) As in [Hin26], rewriting
L_b u = f − (L^(g,g_0) − L_b)u and using [[eq:iii-i-4-2]], the tameness of [[eq:iii-i-5-2]] propagates through a fixed
finite number of such rewritings, with a total loss of b-regularity independent of k. This is used in the later
chapters, whose statements are written with k = ∞. Each rewriting uses [[eq:iii-i-4-2]], so the weights must lie in
the range of [[prop:iii-i-4-1]].

### Uniformity near b₀: the setting {#sec:iii-h2-0}

This section and [[sec:iii-h2-1]]–[[sec:iii-h2-5]] prove, on one fixed neighbourhood of b₀ and with constants uniform
in b, the two inputs that [[thm:iii-i-5-3]] needs at b ≠ b₀: the 2-admissibility of 2L_b for every order k of
b-regularity, which is [Hin26, Proposition 8.3 and Theorem 10.1] near b₀, and the forward solution theory of
[[thm:ii-f-8-1]] and [[thm:ii-f1-1-1]] uniformly over the stationary models 2L_b, which is [Hin26c, Theorems 10.1 and
11.1] for this family. Three facts make this possible. (1) [[prop:iii-f-4-1]] proves strong trapping admissibility at
b₀ from a frame built with the symmetry of Schwarzschild–Tangherlini; near b₀ it gives a bound ε only on a
neighbourhood that shrinks with ε. [Hin26, pp. 147–149] proves the bound at every Kerr parameter in Marck's tetrad.
Here the frame comes from the null geometry alone: along every null bicharacteristic e_0 := ζ/σ is parallel and the
filtration span e_0 ⊂ e_0^⊥ ⊂ T* is invariant, so in an adapted frame the connection is a rotation of the screen plus
a part that lowers a grading. The grading argument holds in such a frame at every b, with bounds uniform near b₀
([[prop:iii-h2-1-1]]). (2) The model at ι⁺ does not see b ([[lem:iii-h2-3-2]]), so [[sec:ii-f-1]]–[[sec:ii-f-6]],
which concern that operator alone, hold for every b with the same constants. (3) The rest is continuity and
compactness, as in [[sec:i-a-8]], [[sec:i-b-9]] and [[rem:iii-h-2-6]].

*The parameters.* They are those of [[sec:iii-h-1]]: the gauge modification E_Υ of [[sec:iii-d-1]] and the constraint
damping (c_C, e_C, γ_C) of [[sec:iii-f-1]], with e_C ∈ (0, 1) and γ_C > 0, and the dynamical hypotheses (Dyn) of
[[ch:s12]]. ℬ is the neighbourhood of b₀ of [[cor:iii-h-4-4]], on which [[cor:iii-h-4-2]]–[[cor:iii-h-4-3]] hold
uniformly. U_Γ is the fixed neighbourhood of the projections of the trapped sets of [[sec:iii-d-1]], over which
E^Υ = 0 for every b ∈ ℬ. As in [[sec:iii-f-4]] we take z_0 = 1 (the operator has real coefficients, and z_0 = −1 is
the conjugate case); then σ = 1 on Γ_b in the normalisation of [[ch:s02]], and Γ_b lies in the future characteristic
set over {|x| > r_h}.

The neighbourhoods are chosen in two steps. First fix an open B_1 ∋ b₀ whose closure B̄_1 is a compact subset of ℬ
such that for b ∈ B̄_1:

(B1) Γ_b lies over a fixed compact subset of U_Γ and in a fixed conic neighbourhood O of Γ_(b₀) in T*M ∖ o, on which
σ > 0 and which meets the characteristic set Σ_b of g_b only in its future component; O lies over U_Γ and is so small
that on it ζ and dt_* are independent and g_b⁻¹(dt_*, ζ) ≠ 0 (both hold on Σ_b, where a nonzero null covector is
independent of, and not orthogonal to, the timelike dt_* of (B2), hence near Γ_(b₀) for b near b₀); and (Γ.1)–(Γ.3)
of (H7) ([[sec:i-b-1-5]]) hold, with ν_min, β_0 and sup_Γ q^Γ continuous in b and positive ((Dyn)).

(B2) dt_* is g_b-timelike over U_Γ (g_b^00 < 0 on X°, [[lem:iii-b-3-7]] (a)), and g_b − g_(b₀) is below the ϵ_G of
[[lem:ii-c-3-2]] (2), so that the time function t^♭ := t^♭_* built from g_(b₀) serves every g_b and
Ω_* = cl_M{t^♭ ≥ 1} does not depend on b. Moreover g_b⁻¹(dr, dr) ≤ −c < 0 and g_b⁻¹(dt_*, dr) > 0 on
{½r_♭ ≤ r ≤ 15R₁/16}, with c independent of b. Then dr is future timelike for g_b there: dt_* is past timelike
([[lem:vi-a-1-1]]), and two timelike covectors lie in the same cone exactly when their g_b⁻¹-pairing is negative. At b₀
this holds by [[eq:vi-a-0-1]]. On {r ≤ 2R₁} the change of time Φ_(m₀) is a translation ([[lem:iii-b-3-5]] (c)) and
ψ′ = 1 ([[def:s12-radii]]), so dt_* = dt − dr = dv − 2dr with v = t_KS + r; and g_(b₀)⁻¹(dv, dv) = 0,
g_(b₀)⁻¹(dv, dr) = 1, g_(b₀)⁻¹(dr, dr) = f = 1 − m₀r⁻². So

    g_(b₀)⁻¹(dr, dr) = 1 − m₀r⁻² < 0,      g_(b₀)⁻¹(dt_*, dr) = 1 − 2f = 2m₀r⁻² − 1 > 0      (r < R₁).

The metrics g_b are stationary and depend smoothly on b on {|x| ≥ ½r_♭} ([[lem:s12-ks-domain]]), and
{½r_♭ ≤ r ≤ 15R₁/16} is compact in X, so both strict inequalities persist for b near b₀.

(B3) c_C is past timelike for g_b over U_Γ ([[thm:iii-e-1-1]] at b₀, and continuity over the closure of U_Γ, which is
compact modulo t_*-translations, all quantities being stationary).

(B4) The order 𝗌 of [[prop:ii-c-5-1]], built for 2L_(b₀), is admissible for 2L_b with the same weights and margin
([[prop:ii-c-5-1]] (4)), and satisfies (C1)–(C3) of [[def:iii-h1-1-1]] for 2L_b. At b₀ this is [[lem:iii-i-5-1]]. At b,
(C1) and (C2) do not involve the metric. For (C3): [[lem:ii-c-5-3]] and [[lem:ii-c-5-5]] hold for every g of
[[prop:ii-c-5-1]] (2), whose item (4) includes the models 2L_b at nearby b, so the proof of [[lem:iii-i-5-1]] runs
verbatim with G_b, its margins (𝖧f_T ≥ ϱ⁻¹ against 2ϱ⁻¹, 𝖧f_W ≥ δ/8, and the gap ξ̂_(3b) < −δ/8 off Σ) being relative.

[[sec:iii-h2-1]]–[[sec:iii-h2-4]] are stated and proved on B̄_1, with constants uniform there; their proofs use only
(B1)–(B4). Then fix an open B_* ∋ b₀ with B̄_* ⊂ B_1 and

(B5) |b − b₀| so small, for b ∈ B̄_*, that ‖P − 2L_b‖_((0;d)) < ε_0 of [[thm:iii-h2-4-1]] in [[cor:iii-h2-5-1]] for |S|
and ‖h‖ small ([[prop:iii-i-3-4]], [[eq:iii-i-3-7]]).

This is the only condition on B_* in this chapter; [[ch:s25]] shrinks B_* further. [[thm:iii-h2-3-1]] and
[[thm:iii-h2-4-1]] apply the slab estimates of [[ch:s07]] relative to 2L_b itself, so no condition on slabs enters
(B5). The choices are made in this order: B_1 by (B1)–(B4); the constants of [[sec:iii-h2-1]]–[[sec:iii-h2-4]],
uniform on B̄_1; then B_* by (B5), which involves only the ε_0 of [[thm:iii-h2-4-1]]. So nothing is circular, and every
statement of [[sec:iii-h2-1]]–[[sec:iii-h2-4]] holds a fortiori on B̄_*.

Put f_b := |dg_b|/(|dt_*| |dx|), a smooth positive stationary function, smooth in b.

### Strong trapping admissibility near b₀ {#sec:iii-h2-1}

This section is [Hin26, Proposition 8.3] on B̄_1, in dimension 4 + 1 and with a different frame. We use the following
identity of [Hin17, Proposition 4.1], valid in every dimension and for every metric: for the tensor wave operator
□_g = −g^(κλ)∇_κ∇_λ on a bundle with the connection ∇ induced by the Levi-Civita connection, the subprincipal operator
on half-densities by |dg| is iS_sub(□_g) = ∇^(π*E)_(H_G), the derivative along the Hamilton vector field H_G of
G(ζ) = g⁻¹(ζ, ζ) for the pullback connection ∇^(π*E) on π*E over T*M ∖ o.

**Proposition {#prop:iii-h2-1-1}** (Strong trapping admissibility near b₀.) For η ∈ (0, 1] and b ∈ B̄_1 there is a
stationary fibre inner product h_(η,b) on π*S²T* over O, homogeneous of degree 0 and smooth in b, such that, with p_1^Γ
of (Γ.4) ([[sec:i-b-1-5]]) for 2L_b, the inner product h_(η,b) and the adjoints of [[ch:s01]] (for |dx| and dt_*),

    sup_(Γ_b) λ_max(p_1^Γ) ≤ Cη,                                                                    {#eq:iii-h2-1-1}

with C independent of η and b. In particular 2L_b is strongly trapping admissible ([Hin26c, Definition 5.8]) at every
b ∈ B̄_1.

*Proof.* *Step 1: the subprincipal operator.* Over U_Γ, E^Υ = 0 and R_(g_b) has order 0, so [[eq:iii-f-4-1]] holds at
every b ∈ B̄_1, on half-densities by |dg_b|:

    iS_sub(2L_b) = ∇^(π*S²T*)_(H_G) + 2E^C_(g_b) σ_1(iδ_(g_b)) G_(g_b),

by the identity of [Hin17, Proposition 4.1] recalled above, with σ_1(iδ_g)(ζ)h = ι_(g⁻¹ζ)h.

*Step 2: the frame.* On O put σ := −ζ(∂_(t_*)) and e_0 := ζ/σ: stationary, homogeneous of degree 0, null on Σ := Σ_b
and future directed there. As ∂_(t_*) is Killing, H_Gσ = 0; and ∇^(π*T*)_(H_G)ζ = 0, which is the geodesic equation
(the identity of [[sec:iii-d-5-2]] (c), which uses no property of the metric). So ∇_(H_G)e_0 = 0 on Σ ∩ O. Let
τ := dt_*, timelike by (B2). A timelike covector and a nonzero null covector are never g⁻¹-orthogonal, so with

    e_2 := aτ + ce_0,        a := −1/g⁻¹(τ, e_0),        c := −a g⁻¹(τ, τ)/(2g⁻¹(τ, e_0)),

expansion with g⁻¹(e_0, e_0) = 0 gives g⁻¹(e_0, e_2) = −1 and g⁻¹(e_2, e_2) = a²g⁻¹(τ, τ) + 2ac g⁻¹(τ, e_0) = 0 on
Σ ∩ O; e_2 is stationary and homogeneous of degree 0. Let V := {e_0, e_2}^⊥, a bundle of rank 3 on which g⁻¹ is
positive definite (the orthogonal complement of a Lorentzian plane). Every covector is ω = ω_0e_0 + ω_V + ω_2e_2 with
ω_V ∈ V, ω_2 = −g⁻¹(ω, e_0) and ω_0 = −g⁻¹(ω, e_2). As ∇ is metric and ∇_(H_G)e_0 = 0,

    (∇_(H_G)e_2)_2 = −H_G g⁻¹(e_2, e_0) = 0,        (∇_(H_G)e_2)_0 = −½H_G g⁻¹(e_2, e_2) = 0,

so w := ∇_(H_G)e_2 ∈ V; and for a section v of V, (∇_(H_G)v)_2 = −H_G g⁻¹(v, e_0) = 0, (∇_(H_G)v)_0 = g⁻¹(v, w), and
the V-part ∇^V v is g-skew. In a local frame (e_0, v_1, v_2, v_3, e_2) with (v_i) g⁻¹-orthonormal in V, therefore,

    ∇_(H_G) = H_G + σ(N_1 + Ω)  componentwise,    N_1e_0 = 0,  N_1v = σ⁻¹g⁻¹(v, w)e_0,  N_1e_2 = σ⁻¹w,   {#eq:iii-h2-1-2}

with Ω, the matrix of σ⁻¹∇^V in (v_i), skew; σ⁻¹w and Ω are homogeneous of degree 0, as H_G is of degree 1 and the
frame of degree 0. (At b₀ the frame of [[sec:iii-d-5-2]] (c), whose e_2 is not built from dt_*, has the same
structure; the comparison is not used.)

*Step 3: the grading.* Give e_0, V, e_2 the weights 0, 1, 2, and S²T* the induced weight wt, the weight of a symmetric
product being the sum of the weights of its factors. The dual frame vector E_2 satisfies g⁻¹e_0 = −E_2 (the pairings of
e_0 with e_0, V, e_2 are 0, 0, −1), so σ_1(iδ)(ζ) = ι_(g⁻¹ζ) = −σι_(E_2), and Step 1 reads, on components,

    iS_sub(2L_b) = H_G + σ(A + Ω),        A := N_1 + 2γ_C E^C_(c)(−ι_(E_2))G,                            {#eq:iii-h2-1-3}

N_1 and Ω acting as derivations, and E^C_(c)ω := 2c_C ⊗_s ω − (2/3)(1 − e_C) g ⟨c_C, ω⟩ the map E^C_(g_b) of
[[eq:iii-b-6-2]] divided by γ_C, with ⟨·, ·⟩ := g⁻¹. We determine the part of A + Ω that preserves wt. Write
c_C = c_0e_0 + Σ_i c_i v_i + c_2e_2, so that c_2 = −g⁻¹(c_C, e_0), and e_ae_b := e_a ⊗_s e_b. The metric itself is

    g = −2e_0e_2 + T,        T := v_1² + v_2² + v_3²,

as the Gram matrix of g⁻¹ in (e_0, v_1, v_2, v_3, e_2) is its own inverse; in particular ι_(E_2)g = g(E_2, ·) = −e_0.

(a) N_1 maps e_0 to 0, V into span e_0 and e_2 into V; so as a derivation it lowers wt by exactly 1. Ω acts on V
alone, by skew maps, and preserves wt.

(b) As G = I − ½g tr, for h ∈ S²T*

    ιh := −ι_(E_2)Gh = −ι_(E_2)h − ½(tr h)e_0,

tr h being the g⁻¹-trace. ι_(E_2) removes a factor e_2 and so lowers wt by 2, and tr h vanishes on the parts of h of
weight ≠ 2, since g⁻¹ pairs e_0 only with e_2 and V only with V. So ι maps the part of weight w of S²T* to the part of
weight w − 2 of T*.

(c) In E^C_(c), the component c_μe_μ of c_C raises wt by wt(e_μ) in the first term; in the second, ⟨e_μ, ω⟩ ≠ 0 only
for the part of ω of weight 2 − wt(e_μ), and g has weight 2, so it raises wt by wt(e_μ) as well. Hence
2γ_C E^C_(c) ∘ ι changes wt by wt(e_μ) − 2 ≤ 0, with equality only for μ = 2.

So A + Ω does not raise wt, and its wt-preserving part is

    D := 2γ_C c_2 Φ + Ω,        Φh := 2e_2 ⊗_s ιh − (2/3)(1 − e_C) g ⟨e_2, ιh⟩,

where ⟨e_2, ω⟩ = −ω_0 is minus the e_0-coefficient of ω. On the monomials (v ∈ V, i ≠ j):

- e_0² and e_0v: ι_(E_2) vanishes on them and so does tr, so ι = 0 and Φ = 0.
- e_0e_2: ι_(E_2)(e_0e_2) = ½e_0 and tr(e_0e_2) = g⁻¹(e_0, e_2) = −1, so ι(e_0e_2) = −½e_0 + ½e_0 = 0 and Φ = 0.
- v_iv_j: ι_(E_2) and tr vanish, so Φ(v_iv_j) = 0.
- v_i²: ι_(E_2)v_i² = 0 and tr v_i² = 1, so ι(v_i²) = −½e_0 and ⟨e_2, −½e_0⟩ = ½. Hence

      Φ(v_i²) = −e_0e_2 − (1/3)(1 − e_C)g = −(1/3)(1 + 2e_C)e_0e_2 − (1/3)(1 − e_C)T,

  by g = −2e_0e_2 + T. So Φ(T) = −(1 + 2e_C)e_0e_2 − (1 − e_C)T, and Φ(v_i² − v_j²) = 0.
- e_2v: ι_(E_2)(e_2v) = ½v and tr(e_2v) = 0, so ι(e_2v) = −½v; ⟨e_2, v⟩ = 0, and Φ(e_2v) = −e_2v.
- e_2²: ι_(E_2)e_2² = e_2 and tr e_2² = 0, so ι(e_2²) = −e_2; ⟨e_2, e_2⟩ = 0, and Φ(e_2²) = −2e_2².

Moreover Ω T = 2Σ_i v_i ⊗_s Ωv_i = 2Σ_(i,j) Ω_(ji) v_iv_j = 0, Ω being skew, and Ω maps the trace-free part S²_0V of
S²V into itself, the trace on S²V being invariant under the infinitesimal rotation Ω.

Refine wt to W := 2wt + s, with s = 1 on T and on S²_0V and s = 0 elsewhere. The seven pieces

    e_0²;   e_0 ⊗_s V;   e_0e_2;   ℝT;   S²_0V;   e_2 ⊗_s V;   e_2²

have W = 0, 2, 4, 5, 5, 6, 8; they are mutually orthogonal for the inner product of Step 4 below, and Ω maps each into
itself. By the list above, D maps each piece into itself except for the component of D(T) along e_0e_2, which goes from
W = 5 to W = 4. Every other part of A + Ω lowers wt by at least 1, by (a) and (c), and hence lowers W by at least
2 − 1 = 1. So

    A + Ω = D_0 + D_−,

where D_− lowers W and D_0 preserves each piece, and on the seven pieces, in the order above, D_0 is Ω plus the scalars

    0,   0,   0,   −2(1 − e_C)γ_C c_2,   0,   −2γ_C c_2,   −4γ_C c_2.

This is the structure of [[prop:iii-f-4-1]], with N_1 in place of 2N, γ_C in place of γ and Ω in place of κR. The
grading argument uses the frame only through four facts: g = −2e_0e_2 + Σ_i v_i²; the weights; that the part of the
connection that does not preserve wt lowers it; and that the wt-preserving part acts on V by skew maps. All four hold
here, as does g⁻¹e_0 = −E_2 with e_0 proportional to ζ. Finally c_2 = −g⁻¹(c_C, e_0) < 0: c_C is past timelike (B3)
and e_0 is future null, and a past and a future causal covector, not both null, have positive g⁻¹-pairing. As e_C < 1,
the scalars are ≥ 0.

*Step 4: the inner product.* Let ⟨·, ·⟩_0 be the inner product on π*S²T* induced by declaring e_0, v_1, v_2, v_3, e_2
orthonormal. It does not depend on the choice of (v_i), as O(V) acts unitarily, so it is defined on O, stationary,
homogeneous of degree 0 and smooth in b (the frame is built from g_b, ζ and dt_*); the seven pieces are orthogonal for
it, and Ω is skew for it. Put h⁰_(η,b) := Σ_P η^(−2W(P)) ⟨·_P, ·_P⟩_0 on Σ ∩ O, the sum over the pieces, and extend it
to O by the same formulas: e_0, e_2 (by the formulas for a and c), V, the frame and the pieces are defined near Σ_b,
where span{e_0, e_2} = span{τ, e_0} stays Lorentzian and e_0, τ stay independent (on O, by (B1)–(B2)). This gives a
stationary inner product on O, homogeneous of degree 0 and smooth in b; p_1^Γ involves the inner product only on Γ_b
and through its derivative along H_G, which is tangent to Σ, so the extension does not enter. In an
h⁰_(η,b)-orthonormal frame a map lowering W by j ≥ 1 has its entries multiplied by η^j, so D_− is O(η), while D_0 is
unchanged; h⁰_(η,b) is constant in the frame, so H_G is skew. By [[eq:iii-h2-1-3]] and [[eq:i-b-6-0]], on Γ_b,

    p_1^Γ = −½(D_0 + D_0^*) + O(η),        −½(D_0 + D_0^*) ≤ 0,

for half-densities by |dg_b|. The O(η) term is bounded by η times a polynomial in |σ⁻¹w|, γ_C and the components c_μ,
which are continuous on O and in b; as Γ_b ∩ {σ = 1} lies in a fixed compact subset of O modulo time translations (B1),
the bound is uniform on B̄_1.

*Step 5: the density.* The adjoints of [[ch:s01]] are for |dt_*| |dx|, and [[eq:iii-h2-1-3]] is on half-densities by
|dg_b| = f_b |dt_*| |dx|. Put h_(η,b) := f_b h⁰_(η,b). Then ∫ h_(η,b)(u, v) |dt_*| |dx| = ∫ h⁰_(η,b)(u, v) |dg_b|, so the
two pairings agree, and with them the adjoints and p_1^Γ (p_1^Γ is an endomorphism, and a scalar factor in the inner
product changes neither its self-adjointness nor its eigenvalues). This replaces the scalar O(|b − b₀|) that
[[lem:iii-d-5-2]] and [[prop:iii-f-4-1]] carry for a fixed inner product. With Cη < ε, [[eq:iii-h2-1-1]] gives strong
trapping admissibility. ∎

**Corollary {#cor:iii-h2-1-2}** (δ_Γ uniformly small.) For every k ∈ ℕ₀ there are η_k ∈ (0, 1] and ε_k > 0 such that,
with h_Γ := h_(η_k,b) in (Γ.4), δ_Γ(0) < 1/(2(k + 1)) and δ_Γ(−ε) ≤ 1/(k + 1) for ε ∈ (0, ε_k] and every b ∈ B̄_1. So
the condition δ_Γ(0) < 1/(2(k + 1)), under which [[thm:iii-h1-1-3]] is proved at the order k ([[sec:iii-h1-1]]), holds
at every b ∈ B̄_1, for every k.

*Proof.* With f(η′) := sup_Γ λ_max(p_1^Γ − η′q^Γ) of [[eq:i-b-1-4]], q^Γ ≥ 2β_0 and [[eq:iii-h2-1-1]] give
f(η′) ≤ Cη − 2β_0η′ for η′ ≥ 0, so γ_+ ≤ Cη/(2β_0). f is Lipschitz with constant Q := sup_Γ q^Γ, and
f(γ_−) − f(γ_+) = ½ν_min, so γ_+ − γ_− ≥ ν_min/(2Q). Hence, by [[eq:i-b-1-4]],

    δ_Γ(−ε) ≤ (γ_+ + ε)/(γ_+ − γ_−) ≤ (2Q/ν_min)(Cη/(2β_0) + ε),

and likewise δ_Γ(0) ≤ (2Q/ν_min)Cη/(2β_0). β_0, Q and ν_min are continuous and positive on the compact B̄_1 (B1).
Choose η_k and ε_k accordingly. ∎

For each k the inner product h_(η_k,b) is a different one. [[thm:i-b-1-3]] is applied at each k separately (in the proof
of [[lem:iii-h1-3-1]]), so this is what it needs.

### 2-admissibility near b₀ for every order {#sec:iii-h2-2}

This section is [Hin26, Theorem 10.1] near b₀, for every k.

**Theorem {#thm:iii-h2-2-1}** (2-admissibility on B̄_1 for every k.) For every k ∈ ℕ₀, the order 𝗌 of (B4) and every
b ∈ B̄_1, the forward solution u of L_b u = f satisfies the estimate [[eq:iii-h1-1-2]] of [[thm:iii-h1-1-3]] with a
constant C_k independent of b. So 2L_b is 2-admissible with sf-weight α_sf, sf-loss 0 and margin 1
([[def:ii-c-2-7]], relaxed, for these orders) at every b ∈ B̄_1, with constants uniform in b; in particular
[[thm:iii-h1-1-3]] holds at every b ∈ B̄_1, for every k.

*Proof.* Run the proof of [[thm:iii-h1-1-3]] ([[sec:iii-h1-2]]–[[sec:iii-h1-7]]) at b ∈ B̄_1. Each constant is uniform,
as follows.

(i) [[sec:iii-h1-2]]: c is at most the c_(j,k′) of [[thm:iii-h-4-1]] (3) for j + k′ ≤ k, uniform near b₀ by
[[cor:iii-h-4-2]] (and [[lem:iii-h-5-2]] (b)). [[lem:iii-h1-2-1]] has no constant; its high-energy input,
[[thm:i-b-1-3]] (3), is uniform in b by [[sec:i-b-9]].

(ii) [[lem:iii-h1-3-1]] for |σ| ≥ C_0: [[thm:i-b-1-3]] (5) at the orders of [[lem:iii-h1-1-2]] (b), with
h_Γ := h_(η_k,b) of [[cor:iii-h2-1-2]]. By [[sec:i-b-9]] its constants are uniform in b, given (H5)–(H8) continuously
in b ((Dyn)) and the inner product continuous in b; then the thresholds γ_± of [[sec:i-b-6]] and c_Γ are continuous in
b. The condition (k + 1)δ ≤ 1 of that proof holds on B̄_1 by [[cor:iii-h2-1-2]], for ε ≤ ε_k.

(iii) [[lem:iii-h1-3-1]] for c/2 ≤ |σ| ≤ C_0: the argument by contradiction there, run with sequences
(σ_n, b_n) → (σ_*, b_*), b_* ∈ B̄_1. The estimates [[eq:i-a-7-1]] and [[eq:i-a-7-3]] of [[thm:i-a-7-2]] hold uniformly
in b for these fixed orders ([[thm:i-a-8-1]]); the coefficients of L̂_(b_n)(σ_n) converge in C^∞ to those of
L̂_(b_*)(σ_*); and the limit is a nonzero element of the kernel of L̂_(b_*)(σ_*) on a space of admissible order. This
contradicts [[cor:iii-h-4-4]], as b_* ∈ ℬ. The inverse is then bounded uniformly and continuous in (σ, b)
([[thm:i-a-8-1]]), which gives the σ∂_σ-derivatives as there.

(iv) [[sec:iii-h1-4]] ([[lem:iii-h1-4-1]]–[[lem:iii-h1-4-2]]): [[cor:iii-h-4-2]]–[[cor:iii-h-4-3]] and the bound
[[eq:iii-h-4-5]], uniform near b₀ ([[rem:iii-h-2-6]] and the uniformity paragraph of the proof of [[cor:iii-h-4-2]]).

(v) [[sec:iii-h1-5]] ([[lem:iii-h1-5-1]]): uniform near b₀, by the last paragraph of [[sec:iii-h1-5]]
([[rem:iii-h-2-6]]).

(vi) [[sec:iii-h1-6]] ([[lem:iii-h1-6-1]]–[[lem:iii-h1-6-2]]): statements about t_*-translation-invariant elliptic
operators and integration in t_*, which do not involve b.

(vii) [[sec:iii-h1-7]]: the assembly, linear in the bounds above.

*Uniformity for every k on B̄_1.* The uniformity near b₀ that (i), (iv) and (v) cite ([[cor:iii-h-4-2]],
[[rem:iii-h-2-6]], [[lem:iii-h-5-2]]) comes from [[thm:i-c-7-1]] (2), together with two arguments of the uniformity
paragraph of the proof of [[cor:iii-h-4-2]]: the uniform inverse of [[prop:iii-h-3-2]] (by contradiction) and the
column bounds of [[rem:iii-h-2-6]], both local in b. [[thm:i-c-7-1]] gives constants uniform on a neighbourhood of a
parameter at which its hypotheses hold, and the neighbourhood may depend on k. Its hypotheses, (G), (Z_𝒫) and (TF) of
[[ch:s03]], and the invertibility in [[prop:iii-h-3-2]] and [[cor:iii-h-4-4]], are qualitative and hold at every
b ∈ B̄_1: (G) and (TF) by [[sec:iii-h-1]], the rest because ℬ is taken inside the neighbourhoods of [[prop:iii-h-3-2]]
and [[cor:iii-h-4-4]]. So for each k, [[thm:i-c-7-1]] (2), with [[prop:iii-h-3-2]] and [[rem:iii-h-2-6]] rerun at b_*,
gives uniform constants near each b_* ∈ B̄_1, and by compactness c_k and C_k are uniform on B̄_1.

For [[def:ii-c-2-7]]: (1) is [[prop:iii-h2-1-1]]; (2), tf-admissibility with weight α_sf + 2, is [[prop:iii-f1-3-3]],
which holds for every b near b₀ as the tf-normal operator does not depend on b; (3) is [[eq:iii-h1-1-2]] at the orders of
(B4), which lie in 𝒪_c. ∎

### Forward solutions of the stationary models, uniformly near b₀ {#sec:iii-h2-3}

This section is [Hin26c, Theorem 10.1] for the stationary models 2L_b, b ∈ B̄_1.

**Lemma {#lem:iii-h2-3-2}** (The ι⁺-normal operator does not depend on b.) For b ∈ ℬ, in the normal form
[[eq:ii-f-1-4]] of P_0 = 2L_b on {|x| > 3R₁}: S = S̄, Q = Q_b, g_00 = g_b^00, and ρ²P⁽⁰⁾ = (2L̄)^∧(0) + R_b, so that
P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω) is that of 2L̄. Hence N_(ι⁺)(2L_b) = N_(ι⁺)(2L̄), and N⁰(σ) ([[eq:ii-f-1-6]]) does not depend
on b.

*Proof.* By [[lem:iii-f-2-1]] (2)–(3), on {|x| > 3R₁}, 2L_b = 2L̄ − g_b^00∂²_(t_*) + Q_b∂_(t_*) + R_b, with
g_b^00 ∈ ρ²C^∞(X̄), Q_b ∈ ρ³Diff¹_b and R_b ∈ ρ⁴Diff²_b; and 2L̄ = −2∂_(t_*)ρ(ρ∂_ρ − 3/2 − S̄) + (2L̄)^∧(0) with
(2L̄)^∧(0) ∈ ρ²Diff²_b. Comparing with [[eq:ii-f-1-4]] (c = 3/2) gives the identifications. As ρ⁻²R_b ∈ ρ²Diff²_b
vanishes at ρ = 0, the frozen operator P⁽⁰⁾(0, ·) is (ρ⁻²(2L̄)^∧(0))|_(ρ=0). [[def:ii-f-1-1]] uses only S_0 = S|_(∂X)
and P⁽⁰⁾(0, ·). ∎

In dimension 3 + 1 the mass enters R_b at ρ³, and ρ⁻²R_b is of order ρ; in dimension 4 + 1 it is of order ρ². Either
way it vanishes at ρ = 0; what matters is that the remainder carries all the dependence on b.

**Theorem {#thm:iii-h2-3-1}** ([[thm:ii-f-8-1]] uniformly near b₀.) [[thm:ii-f-8-1]], with [[rem:ii-f-8-2]] (margin
1), holds for P_0 = 2L_b, b ∈ B̄_1, ℵ = 2, sf-loss 0, the order 𝗌 of (B4), and a constant C_k independent of b.

*Proof.* (a) *[[sec:ii-f-1]]–[[sec:ii-f-6]].* They concern N_(ι⁺)(P_0): its Mellin family N⁰(σ) and the semiclassical
rescaling ([[sec:ii-f-1-2]]–[[sec:ii-f-1-3]]), the estimates of [[prop:ii-f-3-1]] and [[prop:ii-f-5-1]] and their
lemmas, and the forward problem for N_(ι⁺)(P_0) ([[prop:ii-f-6-2]]). By [[lem:iii-h2-3-2]] their statements do not
depend on b. The proof in [[sec:ii-f-6-3]] also uses P_0: it builds P_λ := P_0 + ψψ̃(N − P_0), applies
[[prop:ii-e-3-4]] to it with λ chosen by smallness relative to P_0, and the orders of [[sec:ii-f-6-1]] are admissible
for P_0. So [[sec:ii-f-6]] is run with P_0 := 2L_(b₀) for every b, which is allowed as the statement of
[[prop:ii-f-6-2]] involves only N_(ι⁺)(P_0) = N_(ι⁺)(2L_(b₀)). The statement also involves the order of
[[sec:ii-f-6-1]], admissible for P_0; with P_0 := 2L_(b₀) this is the order 𝗌 of (B4), which [[sec:ii-f-7-2]] uses at
2L_b, so the substitution is consistent. The compactness and contradiction arguments of [[sec:ii-f-3-5]],
[[sec:ii-f-4-2]] and [[sec:ii-f-5-4]] concern N⁰ and N_tf, which do not depend on b. The uniqueness of
[[sec:ii-f-1-4]] ([[lem:ii-f-1-3]]–[[lem:ii-f-1-4]]) is qualitative and holds for every g_b, with t_* a time function
([[lem:ii-b-1-1]]).

(b) *[[sec:ii-f-7]].* P_+ = χN_(ι⁺)(P_0) + (1 − χ)P_0 ([[def:ii-f-7-1]]), and P_+ − N_(ι⁺)(P_0) =
(1 − χ)(P_0 − N_(ι⁺)(P_0)) lies in x_I²τ³ρ_cf⁻² Diff²_ebe ([[lem:ii-f-7-2]] (b)), with seminorms continuous in b
([[lem:iii-f-2-1]] (3): the coefficients are smooth in b). The τ_1 of [[lem:ii-f-7-2]] (c) is uniform, the normalised
difference there being O(ρ_+²) with constants continuous in b. By the remark after [[prop:ii-f-7-4]], τ_0 and the
constants depend on P_0 only through [[sec:ii-f-7-6]]. Its estimates are the radial estimates at cf ([[lem:ii-f-7-6]],
whose quantities at the radial sets are those of N_(ι⁺)(P_0), independent of b by (a)), the radial estimates at 𝓘⁺
([[prop:ii-d-3-5]]–[[prop:ii-d-3-6]]), propagation estimates and the slab estimates of [[ch:s07]]; and
τ_0 < ½C′τ_1 involves the C′ of [[lem:ii-c-3-2]]. Their constants depend on finitely many seminorms of
P_+ − N_(ι⁺)(P_0) and of the orders, and on margins, all continuous in b. The one limit argument there (u^ε ⇀ u)
extracts a solution from an estimate that is already uniform. Strong uniqueness ([[sec:ii-f-7-4]]) is qualitative.
Finite-time solvability ([[sec:ii-f-7-5]]) applies [[prop:ii-e-3-4]] and [[prop:ii-e-4-3]] on slabs to operators weakly
admissible relative to P_0 = 2L_b itself, with ε_P ≤ C t_(*,0)^(−(1−ℓ_+)) ([[lem:ii-f-7-5]]; C is a seminorm of
N_(ι⁺)(P_0) − P_0 in the class of [[lem:ii-f-1-2]], continuous in b by [[lem:iii-f-2-1]] (3)). The constants of
[[ch:s07]] depend on P_0 through finitely many coefficient norms and the structural margins (the timelike conditions,
the threshold, the dynamics), and are uniform for ε_P small (the last paragraph of the proof of [[prop:ii-e-3-4]], and
the proof of [[prop:ii-e-4-3]], which applies it). For P_0 = 2L_b these norms, which [[sec:ii-f-7-5]] bounds over all
its slabs at a fixed b, are seminorms of stationary coefficients smooth in b ([[lem:iii-f-2-1]] (3)), and the margins
are continuous and positive in b; so they are bounded, respectively bounded below, on the compact B̄_1, as no
perturbation of 2L_(b₀) is taken. What is uniform in b is the constant of each slab (those of [[lem:ii-f-7-5]] depend
on the step), and only finitely many steps enter [[eq:ii-f-7-4]] at T = 2δ⁻¹, so the bound is uniform. So
[[prop:ii-f-7-4]] holds with τ_0 and C uniform on B̄_1.

(c) *[[sec:ii-f-8]].* Step 0 of the proof in [[sec:ii-f-8-2]] uses [[prop:ii-e-4-3]] on a slab, uniform as in (b).
Steps 1 and 3 use [[prop:ii-f-7-4]], uniform by (b). Step 2 uses the 2-admissibility estimate [[eq:ii-f-8-6]], uniform
by [[thm:iii-h2-2-1]], and [[lem:ii-f-1-3]]–[[lem:ii-f-1-4]], which are qualitative. Step 4 sums the bounds. So
[[eq:ii-f-8-2]] holds with C_k independent of b. ∎

### Forward solutions of admissible operators, uniformly near b₀ {#sec:iii-h2-4}

This section is [Hin26c, Theorem 11.1] uniformly over the family 2L_b.

**Theorem {#thm:iii-h2-4-1}** ([[thm:ii-f1-1-1]] uniformly near b₀.) Let α_I, α_+, ℓ_I, ℓ_+, ℓ_K be as in
[[thm:ii-f1-1-1]], with ℵ = 2, δ = 0 and the order 𝗌 of (B4). There are ε_0 > 0 and d ∈ ℕ such that for every
b ∈ B̄_1 the conclusions of [[thm:ii-f1-1-1]] and [[cor:ii-f1-1-2]] hold with P_0 := 2L_b (with [[rem:ii-f1-7-1]] for
margin 1), with ε_0, d and C_k independent of b. Moreover, for k ≥ 1: let b_j → b in B̄_1; let P_j be admissible
relative to 2L_(b_j) of class ((0;k+d),(2ℓ_I,ℓ_+,ℓ_K)), with ‖P_j − 2L_(b_j)‖_((0;d)) < ε_0 and
‖P_j − 2L_(b_j)‖_((0;k+d)) bounded, and with coefficients converging in C² on compact subsets of M° ∩ {r > r_0} to those
of P, admissible relative to 2L_b with ‖P − 2L_b‖_((0;d)) < ε_0; and let f_j → f in [[eq:ii-f1-1-4]]. Then the forward
solutions converge in H^(k−1,(α_I−ς,α_+−ς,−2−ς))_b(Ω_*; E)^(•,−) for every ς > 0.

*Proof.* The proof of [[thm:ii-f1-1-1]] depends on P_0 only through the following inputs.

(i) [[thm:ii-e-6-1]] and [[prop:ii-e-3-4]], [[prop:ii-e-4-3]] and [[prop:ii-e-4-4]] ([[sec:ii-f1-3-1]]).
[[thm:ii-e-6-1]] is uniform over the stationary models of nearby parameters (its last sentence). The slab propositions
are applied relative to P_0 = 2L_b ([[prop:ii-f1-3-1]] (iv) on Ω_(1,T_η), [[lem:ii-f1-2-9]] on Ω_(1,4/ε), and
[[prop:ii-e-4-4]], which rests on [[prop:ii-e-4-3]]), and are uniform on every slab as in the proof of
[[thm:iii-h2-3-1]] (b).

(ii) The thresholds of [[lem:ii-f1-2-1]] and of [[lem:ii-c-3-2]] and [[lem:ii-c-3-7]], which are continuous in the
coefficients.

(iii) The orders ([[sec:ii-f1-2-3]]), fixed by (B4).

(iv) [[thm:ii-f-8-1]] with [[rem:ii-f-8-2]], uniform by [[thm:iii-h2-3-1]].

(v) The 2-admissibility estimate [[eq:ii-c-2-2]], uniform by [[thm:iii-h2-2-1]].

Every other constant depends on P only through ε_0 (the last sentence of [[sec:ii-f1-3-1]]). So ε_0, d and C_k can be
chosen independent of b ∈ B̄_1. *Continuity.* Run the proof of [[sec:ii-f1-6]] with P^(j) := P_j relative to 2L_(b_j).
By the first part the u_j are bounded in H^(k,(α_I,α_+,−2))_b uniformly in j. A weak limit point ũ satisfies Pũ = f,
by the C² convergence of the coefficients on compact sets; the uniqueness of [[lem:ii-f1-2-2]], which is qualitative,
gives ũ = u, and [[lem:ii-f1-6-1]] gives convergence in norm. ∎

[Hin26c, Theorem 11.1] also allows P_0 near an admissible P_1 among all small stationary perturbations. That wider
statement is not proved here and is not used: the later chapters use only the family 2L_b, b ∈ B̄_*.

### Forward solutions in the cone near b₀ {#sec:iii-h2-5}

**Corollary {#cor:iii-h2-5-1}** (Forward solutions near b₀; [Hin26, Theorem 11.12] in dimension 4 + 1.)
[[thm:iii-i-5-3]] holds for every b ∈ B_* in place of b₀. With g_0 := g_(b₀,b,−S), g := g_0 + h and the forward
solution u of L^(g,g_0)u = f, [[eq:iii-i-5-1]]–[[eq:iii-i-5-2]] hold with ε_0, d and C_k independent of b. For k ≥ 1,
u depends continuously on (b, S, h) in H^(k−1,(β_I−ς,β_+−ς,−3/2−ς))_b(Ω_*; S²T*)^(•,−), for every ς > 0.

*Proof.* The proof of [[thm:iii-i-5-3]], with P_0 := 2L_b and [[thm:iii-h2-4-1]] in place of [[thm:ii-f1-1-1]]. Its
hypothesis (i) is [[thm:iii-h2-2-1]]. (ii) is unchanged, as S̄ and Ā do not depend on b. (iii) is [[cor:iii-i-5-2]],
which is stated for g_0 = g_(b₀,b,−S) and P_0 = 2L_b and whose hypothesis is now [[thm:iii-h2-2-1]], with
‖P − 2L_b‖_((0;d)) ≤ C(|b − b₀| + |S| + ‖h‖_(𝒳^(d+5))) by [[prop:iii-i-3-4]], [[eq:iii-i-3-7]], small by (B5).
*Continuity.* [[thm:iii-h2-4-1]], as 2L^(g,g_0) depends smoothly on (b, S) and continuously on h in the norm of
[[eq:iii-i-3-7]] ([[lem:iii-i-3-6]]). ∎

[Hin26, Theorem 11.12] states continuity in (b₀, b, S, h); here b₀ is fixed.

### Null infinity: the setting and the structure {#sec:iii-i1-1}

This section and the next two are [Hin26, Section 11.2] in dimension 4 + 1: the partial polyhomogeneity at 𝓘⁺ of
solutions of L^(g,g_0)u = f without loss at ι⁺ ([Hin26, Proposition 11.14 and Lemma 11.15]), and formal solutions of
L_b u = f at 𝓘⁺ ([Hin26, Proposition 11.16]). The leading part of the operator at 𝓘⁺ is (X_+ − X_I)(X_I − 3/2 − Ā),
with the constant lower-triangular Ā, for the dynamical operator as for L_b ([[prop:iii-i-3-3]]); the terms A^h, B^h
of [Hin26] and its h-dependent coupling (A^h)_(7,6) of the radiation field into the 11-component are half an order
lower and enter only through the error.

On the region U_I := [0, c_I]_(ρ_I) × [0, 1]_(ρ_+) × 𝕊³, with the coordinates [[eq:iii-i-3-1]] (so that
{ρ_+ = 1} = {t_* = 0}) and c_I ∈ (0, 1] small, weights are listed at (𝓘⁺, ι⁺) and none at K⁺, as in [Hin26].
L := L^(g,g_0) with g_0 := g_(b₀,b,−S), g := g_0 + h and h ∈ 𝒳^∞ small ([[eq:iii-i-1-4]], [[prop:iii-i-3-4]]). All
functions below vanish for t_* ≤ 1, so the region {0 ≤ t_* ≤ 1}, where h is extended arbitrarily, plays no role.
Components are taken in the splitting [[eq:iii-c-1-6]], slots 1, …, 7. [[sec:iii-f-1]] takes
(1 − e_C)(1 − v_C)γ_C > 100. Put

    ℓ_I^max := 3/2 + (1 − e_C)(1 − v_C)γ_C   (> 100),                                                 {#eq:iii-i1-1-1}

the least indicial root of the π_C-slots. The weights at 𝓘⁺ below reach min(a_I + ½, ℓ_I^max): a_I + ½ is the bound of
the products with the coefficients of the error, whose remainder has the weight a_I − 1, against the least exponent 3/2
of u ([Hin26] has ℓ_I ≤ 3 + ε_I, the same bound in dimension 3 + 1 with the least exponent 1); and ℓ_I^max keeps ℓ_I
below the roots of the π_C-slots, which [Hin26] states as 3 + ε_I < 1 + (1 − e_C)(1 − v_C)γ_C.

**Lemma {#lem:iii-i1-1-1}** (The structure; [Hin26, (11.26) and (11.34)] in dimension 4 + 1.) On U_I,

    ρ_I⁻¹ρ_+⁻²L = L_0 + L̃,        L_0 := (X_+ − X_I)(X_I − 3/2 − Ā),
    L̃ ∈ (ρ_I C^∞ + H^(∞,(ℰ_I^tot−1,a_I−1),(ℰ_+,a_+))_b) Diff²_b,                                       {#eq:iii-i1-1-2}

and for L_b the same holds with L̃ ∈ ρ_I Diff²_b (smooth coefficients). X_+ − X_I and X_I − 3/2 − Ā commute.

*Proof.* Divide [[eq:iii-i-3-4]] by ρ_Iρ_+², and for L_b use [[lem:iii-i-3-2]] with the change of frame of
[[lem:iii-c-1-3]]. Ā is constant, and X_+, X_I commute. ∎

[Hin26] has L_0 = −(ρ_I∂_(ρ_I) − (I + A^h))(ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+)) + ρ_+⁻¹B^h, with
L̃ ∈ (ρ_I C^∞ + H^(k−2,(ℰ_I^C−1,2+ε_I),(ℰ_+,3+ε_+))_b) Diff²_b, which gains min Re(ℰ_I^C − 1) > 2γ_Υ; here L̃ gains ½
(as min Re ℰ_I^tot = 3/2), and L_0 has constant coefficients.

*Integration tools.* We use [[lem:iii-a-1-2]] ([Hin26, Lemma 2.12]: the equation (x∂_x − z)u = f adds (z, 0) to the
index set when Re z ≤ α, for a weight α ≠ Re z), [[lem:iii-a-3-1]] ([Hin26, Lemma 2.22]) and [[lem:iii-a-3-2]]
([Hin26, Lemma 2.23]: the equation (x∂_x − y∂_y + z)u = f, with α + Re z > β and an a priori bound near y = 1). Here
(x, y) = (ρ_I, ρ_+) when integrating forward from {ρ_+ = 1}, where u = 0, and (x, y) = (ρ_+, ρ_I) when integrating
backward from {ρ_I = c_I}. Slot j of L_0u is

    (L_0u)_j = (X_+ − X_I)((X_I − 3/2 − Ā_jj)u_j − Σ_(i<j) Ā_ji u_i),                                    {#eq:iii-i1-1-3}

the couplings being at (3, 1), (4, 1), (4, 3), (5, 2), (7, 3) and (7, 4) ([[lem:iii-c-4-2]]).

### Partial polyhomogeneity at null infinity {#sec:iii-i1-2}

This section is [Hin26, Proposition 11.14 and Lemma 11.15] in dimension 4 + 1.

**Proposition {#prop:iii-i1-2-1}** (Partial polyhomogeneity at 𝓘⁺; [Hin26, Proposition 11.14] in dimension 4 + 1.)
Let ℰ_I^C and ℰ_+ be as in [[def:iii-i-1-1]]. Let 3/2 < ℓ_I < min(a_I + ½, ℓ_I^max),
ℓ_+ < min(ℓ_I, a_+ + min Re ℰ_+), ℓ_+ ∉ Re π_1ℰ_+ ∪ Re π_1ℰ_I^tot and ℓ_I ∉ 3/2 + σ_Υ. Suppose that u and f vanish for
t_* ≤ 1, and

    Lu = f ∈ H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2))_b,      u ∈ H^(∞,α_I,(ℰ_+,ℓ_+))_b          {#eq:iii-i1-2-1}

for some α_I ∈ ℝ. Then u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_+,ℓ_+))_b.

[Hin26] asks ℓ_+ < ℓ_I ≤ 3 + ε_I, its 3 + ε_I being the product bound in dimension 3 + 1. Its exceptional roots
1 + σ_Υ (at most 1 + 2γ_Υ) can equal a small ℓ_I, which its statement does not exclude, and its roots 1 + λ_C of the
π_C-slots lie far above. The exclusions ℓ_I ∉ 3/2 + σ_Υ and ℓ_+ ∉ Re π_1ℰ_I^tot come from the conditions α ≠ Re z of
[[lem:iii-a-1-2]] and of [[lem:iii-a-3-2]].

**Lemma {#lem:iii-i1-2-2}** (The expansion at 𝓘⁺ away from ι⁺; [Hin26, Lemma 11.15] in dimension 4 + 1.) Under the
assumptions of [[prop:iii-i1-2-1]], u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),α_+)_b for every
α_+ < min(α_I, 3/2, ℓ_+, min Re ℰ_+).

*Proof.* Reducing α_I if necessary, we may assume α_I < 3/2 and

    u ∈ H^(∞,α_I,α_+)_b.                                                                             {#eq:iii-i1-2-2}

*Step 1: the weight below 3/2.* Fix η ∈ (0, ½) with α_I + η < 3/2. By [[eq:iii-i1-1-2]] and [[lem:iii-c-2-1]] (the
𝓘⁺-index set of the coefficient has min Re = ½ > η; at ι⁺, min Re ℰ_+ > 0), L̃u ∈ H^(∞,α_I+η,α_+)_b; and
ρ_I⁻¹ρ_+⁻²f ∈ H^(∞,α_I+η,α_+)_b, as its 𝓘⁺-index sets ℰ_I^C and ℱ_(I,11) − 1 have min Re > 3/2 and its data at ι⁺
are (ℰ_+, ℓ_+) with α_+ < min(ℓ_+, min Re ℰ_+). So L_0u ∈ H^(∞,α_I+η,α_+)_b. In slot 1, by [[eq:iii-i1-1-3]],
(X_I − 3/2 − λ)w = (L_0u)_1 for w := (X_+ − X_I)u_1 and the eigenvalue λ of the slot. [[lem:iii-a-1-2]] in ρ_I (with
Re(3/2 + λ) > α_I + η, so that no term is added; the a priori hypothesis, on ρ_I near c_I, away from 𝓘⁺, holds by
[[eq:iii-i1-2-2]]) gives w ∈ H^(∞,α_I+η,α_+)_b. Then (X_I − X_+)u_1 = −w with u_1 = 0 near {ρ_+ = 1}, and
[[lem:iii-a-3-2]] with (x, y) = (ρ_I, ρ_+), z = 0, E = F = ∅ and α = α_I + η > β = α_+ gives
u_1 ∈ H^(∞,α_I+η,α_+)_b. In slot j > 1 the couplings (X_+ − X_I)Ā_ji u_i, i < j, already improved, go to the right,
and the same two steps apply, as every eigenvalue satisfies 3/2 + λ ≥ 3/2 > α_I + η. So [[eq:iii-i1-2-2]] holds with
α_I + η in place of α_I, and iterating,

    u ∈ ⋂_(α_I<3/2) H^(∞,α_I,α_+)_b.                                                                {#eq:iii-i1-2-3}

*Step 2: the first expansion term.* Let 0 < η < min((1 − e_Υ)γ_Υ, ½), the least nonzero element of σ_Υ being
(1 − e_Υ)γ_Υ (as 0 < e_Υ < 1). By [[eq:iii-i1-2-3]] and [[eq:iii-i1-1-2]], L̃u and ρ_I⁻¹ρ_+⁻²f lie in
H^(∞,3/2+η,α_+)_b. In the slots 1–5 and 7, whose eigenvalues exceed η, the two steps of Step 1 give membership at
3/2 + η (slot 7 by the couplings (7, 3) and (7, 4) from slots already improved; Ā_76 = 0). In slot 6 (π̸₀, eigenvalue
0), [[lem:iii-a-1-2]] adds (3/2, 0): (X_+ − X_I)π̸₀u ∈ H^(∞,((3/2,0),3/2+η),α_+)_b, and [[lem:iii-a-3-2]]
(E = {(3/2, 0)}, α = 3/2 + η > α_+, 3/2 ≠ α_+) gives π̸₀u ∈ H^(∞,((3/2,0),3/2+η),α_+)_b, the terms it adds at ι⁺
lying above the weight α_+ < 3/2. So

    u ∈ H^(∞,(⟨ℰ_I^C⟩,α_I),α_+)_b        for every α_I < 3/2 + (1 − e_Υ)γ_Υ,                             {#eq:iii-i1-2-4}

with π̸₀u carrying (3/2, 0) and no other slot carrying an expansion term below the weight. In dimension 3 + 1, u_11
acquires (1, 0) here, from (A^h)_(7,6) acting on π̸₀u ([Hin26, (11.29)]); in dimension 4 + 1 that coupling is part of
L̃, and acting on (3/2, 0) it gives 𝓘⁺-order ≥ 2 > 3/2 + η.

*Step 3: the full expansion.* Suppose [[eq:iii-i1-2-4]] holds for some α_I, and let 0 < η < ½. Every slot of u has its
𝓘⁺-index set in ℰ_I^tot ([[lem:iii-c-3-2]] (c)), so by [[eq:iii-i1-1-2]] and [[lem:iii-c-2-1]], with
(ℰ_I^tot − 1) + ℰ_I^tot ⊂ ℰ_I^C ([[def:iii-c-3-1]] (3)) and ℰ_I^tot + 1 ⊂ ℰ_I^C ([[lem:iii-c-3-2]] (a)),
L̃u ∈ H^(∞,(ℰ_I^C,α′),α_+)_b with α′ := min(ℓ_I, α_I + η). The three inequalities of [[lem:iii-c-2-1]] hold:
α′ < α_I + ½; α′ ≤ α_I + a_I − 1, as a_I > 3/2; and α′ < (a_I − 1) + 3/2 = a_I + ½, the remainder of the coefficient at
the weight a_I − 1, which has no expansion, against the least exponent 3/2 of u. This last is where the hypothesis
ℓ_I < a_I + ½ enters. The term ρ_I⁻¹ρ_+⁻²f has the 𝓘⁺-index sets ℰ_I^C (slots 1–6) and
ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0) (slot 7) at the weight ℓ_I. Here α′ is chosen off 3/2 + σ_Υ, by decreasing η (ℓ_I is
off it by hypothesis).

Slots 1–3: the eigenvalues satisfy 3/2 + λ_C ≥ ℓ_I^max > ℓ_I ≥ α′, so [[lem:iii-a-1-2]] adds nothing, and
(X_+ − X_I)u_j ∈ H^(∞,(ℰ_I^C,α′),α_+)_b; [[lem:iii-a-3-2]] (E = ℰ_I^C, α′ > α_+, and α_+ ∉ Re π_1ℰ_I^C as α_+ < 3/2)
gives u_j ∈ H^(∞,(ℰ_I^C,α′),α_+)_b, the index set it adds at ι⁺ lying above the weight α_+.

Slots 4, 5, 6: with the couplings (4, 1), (4, 3), (5, 2) from the slots 1–3 on the right, the eigenvalue
s ∈ {(1 − e_Υ)γ_Υ, γ_Υ, 0} adds (3/2 + s, 0), so u_01, π_(1/)u and π̸₀u lie in the classes of ℰ_(I,01), ℰ_(I,1/) and
ℰ̸_(I,0) at the weight α′.

Slot 7: the couplings (7, 3) (index set ℰ_I^C) and (7, 4) (index set ℰ_(I,01)), the term (3/2 + (1 − e_Υ)γ_Υ, 0) of
f, and, through L̃, the h-dependent couplings, which land in ℰ_I^C (above); with the eigenvalue 2γ_Υ,
[[lem:iii-a-1-2]] gives ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0) ∪ (3/2 + 2γ_Υ, 0) = ℰ_(I,11), as (1 − e_Υ)γ_Υ ≠ 2γ_Υ.

So [[eq:iii-i1-2-4]] holds with α′ in place of α_I, in the class of [[def:iii-i-1-1]] (1), and finitely many steps
reach ℓ_I. ∎

*Proof of [[prop:iii-i1-2-1]].* *Step 1: the data at ι⁺, at a weaker 𝓘⁺-weight.* Suppose that
u ∈ H^(∞,(⟨ℰ_I^C⟩,α_I),(ℰ_+,ℓ_+))_b for some α_I < ℓ_+ (or u ∈ H^(∞,α_I,(ℰ_+,ℓ_+))_b when α_I < 3/2; this holds for
the given α_I). By [[eq:iii-i1-1-2]], L̃u has the 𝓘⁺-weight α_I + η for η < ½, with some index set, and the data
(ℰ_+, ℓ_+) at ι⁺ (ℰ_+ + ℰ_+ ⊂ ℰ_+; the remainder of the product needs ℓ_+ < a_+ + min Re ℰ_+, the remainder of the
coefficient at the weight a_+ against the least exponent of u). Integrate L_0u = ρ_I⁻¹ρ_+⁻²f − L̃u slot by slot as in
[[lem:iii-i1-2-2]], except that the hyperbolic field is integrated backward from {ρ_I = c_I}: [[lem:iii-a-3-2]] with
(x, y) = (ρ_+, ρ_I), the a priori bound near {ρ_I = c_I} being the hypothesis u ∈ H^(∞,·,(ℰ_+,ℓ_+)) there (away from
𝓘⁺), needs ℓ_+ > α_I + η (α + Re z > β) and α_I + η ∉ Re π_1ℰ_+; and in the slot-by-slot step [[lem:iii-a-1-2]] in
ρ_I needs α_I + η off 3/2 + spec Ā. Decrease η to ensure all three. This gives the data (ℰ_+, ℓ_+) at ι⁺, and 𝓘⁺-index
sets that are extended unions with ℰ_+; but by [[lem:iii-i1-2-2]] the 𝓘⁺-expansion of u, which is determined by u away
from ι⁺, has exponents only in ⟨ℰ_I^C⟩ up to the weight ℓ_I, so the coefficients of all other terms vanish. Hence the
hypothesis holds with α_I + η, and finitely many steps give it for every α_I < ℓ_+.

*Step 2: both.* Now integrate forward as in [[lem:iii-i1-2-2]], from α_I < ℓ_+ close to ℓ_+ up to ℓ_I, keeping the data
(ℰ_+, ℓ_+) at ι⁺. In [[lem:iii-a-3-2]] with (x, y) = (ρ_I, ρ_+), the 𝓘⁺-weight α_I + η of the right side exceeds ℓ_+
(α + Re z > β with β = ℓ_+), and ℓ_+ ∉ Re π_1 of the 𝓘⁺-index sets, which lie in ℰ_I^tot (a hypothesis; these sets do
not depend on the weight); also ℓ_+ < ℓ_I and ℓ_+ ∉ Re π_1ℰ_+. The index sets at ι⁺ that it produces are extended
unions of ℰ_+ with 𝓘⁺-index sets of components of u, but u has the index set ℰ_+ at ι⁺ by Step 1, so no other
exponent occurs. After finitely many steps, u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),(ℰ_+,ℓ_+))_b. ∎

### Formal solutions at null infinity {#sec:iii-i1-3}

This section is [Hin26, Proposition 11.16] in dimension 4 + 1.

**Proposition {#prop:iii-i1-3-1}** (Formal solutions at 𝓘⁺; [Hin26, Proposition 11.16] in dimension 4 + 1.) Let ℰ_I^C
be as in [[def:iii-i-1-1]] and Ĕ_+ ⊂ ℂ × ℕ₀ an index set. Let ℓ̆_+ < ℓ_I < ℓ_I^max with ℓ_I > 3/2,
ℓ̆_+, ℓ_I ∉ Re π_1ℰ_I^C and ℓ̆_+, ℓ_I ≠ 3/2 + (1 − e_Υ)γ_Υ. Let
f ∈ H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),(Ĕ_++2,ℓ̆_++2))_b vanish for t_* < 1. Then there are an index set ℰ^♯_+, depending only
on ℰ_I^C and Ĕ_+, and u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),(ℰ^♯_+,ℓ̆_+))_b vanishing on {t_* < 1} ∪ {ρ_I > ½c_I}, with

    f − L_b u ∈ H^(∞,ℓ_I+1,(ℰ^♯_++2,ℓ̆_++2))_b(Ω_*; S²T*).                                              {#eq:iii-i1-3-1}

One can take ℰ^♯_+ = ⋃_(j≥1) ℰ^(♯,(j))_+, with

    ℰ^(♯,(1))_+ := Ĕ_+ ∪̄ {(3/2 + (1 − e_Υ)γ_Υ, 0)},
    ℰ^(♯,(j+1))_+ := ℰ^(♯,(j))_+ ∪̄^(k(ℰ_I^C,z)+1) {(z, 0)}
                     for each z ∈ π_1ℰ_I^C with m_j ≤ Re z < m_j + 1,                              {#eq:iii-i1-3-2}

m_j := min Re ℰ_I^C + j − 1 (only Re z ≤ ℓ_I matters), where k(ℰ_I^C, z) is the largest logarithmic order of ℰ_I^C
at z, and E ∪̄^m {(z, 0)} is the extended union of [[lem:iii-a-1-2]] taken m times: E ∪ {(z, m − 1)} if z ∉ π_1E, and
E with its logarithmic order at z raised by m otherwise. (The rounds of the proof take the windows [μ_j, μ_j + 1), with
μ_j ≥ m_j the least real part left; the union ℰ^♯_+ is the same.) If all the terms ρ_I^(z+1)(log ρ_I)^k of the
𝓘⁺-expansion of f vanish for Re z ≤ C_0, these z may be omitted from [[eq:iii-i1-3-2]].

[Hin26, (11.33a)] has ℰ^(♯,(1))_+ = Ĕ_+ ∪ {(1, 0)} ∪ {(1 + (1 − e_Υ)γ_Υ, 0)} and windows j < Re z ≤ j + 1. The (1, 0)
comes from the radiation coupling of its Step 1, which dimension 4 + 1 does not have. Its windows rely on
min Re ℰ_I^C ∈ (1, 2) in dimension 3 + 1; [[eq:iii-i1-3-2]] takes them from min Re ℰ_I^C upward in steps of 1, which is
what the induction uses. And [Hin26, (11.33a)–(11.33b)] write ∪ where [[lem:iii-a-1-2]] returns the extended union
E ∪̄ {(z, 0)}; the plain union understates the logarithmic orders at ι⁺ when Ĕ_+ meets z_1 or π_1ℰ_I^C, and the
existence of ℰ^♯_+ is not affected.

*Proof.* By [[lem:iii-i1-1-1]], ρ_I⁻¹ρ_+⁻²L_b = L_0 + L̃ with L̃ ∈ ρ_I Diff²_b. Let χ = χ(ρ_I) ∈ C^∞_c([0, ½c_I))
equal 1 near 0. By [[def:iii-i-1-1]] (2) ([[eq:iii-c-5-1]]), write

    f = χρ_I^(5/2+(1−e_Υ)γ_Υ) f^♭_11 (dx¹)² + f̃,      f^♭_11 ∈ H^(∞,(Ĕ_++2,ℓ̆_++2))_b(Ω_* ∩ 𝓘⁺),
                                                     f̃ ∈ H^(∞,(ℰ_I^C+1,ℓ_I+1),(Ĕ_++2,ℓ̆_++2))_b,

the exceptional term of the 11-component: ℱ_(I,11) = 1 + (ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0)), and
z_1 := 3/2 + (1 − e_Υ)γ_Υ < 3/2 + 2γ_Υ < min Re ℰ_I^C by [[def:iii-c-3-1]] (2), so the splitting is clean.

*Step 1: the exceptional term.* Try v := χρ_I^(z_1)u^♭(dx¹)² with u^♭ = u^♭(ρ_+, ω). On slot 7, the last,
X_I − 3/2 − Ā acts by z_1 − 3/2 − 2γ_Υ = −(1 + e_Υ)γ_Υ ≠ 0 (there is no slot below it), and
(X_+ − X_I)ρ_I^(z_1) = ρ_I^(z_1)(X_+ − z_1). So, where χ = 1,
L_0v = −(1 + e_Υ)γ_Υ ρ_I^(z_1)((X_+ − z_1)u^♭)(dx¹)², and the corresponding term of ρ_I⁻¹ρ_+⁻²f is
ρ_I^(z_1)ρ_+⁻²f^♭_11(dx¹)². Solve, on 𝓘⁺,

    (X_+ − z_1)u^♭ = −((1 + e_Υ)γ_Υ)⁻¹ρ_+⁻²f^♭_11,        u^♭ = 0 near {ρ_+ = 1}.

[[lem:iii-a-1-2]] in ρ_+ (ℓ̆_+ ≠ z_1; the right side vanishes for t_* < 1, so the solution vanishing at ρ_+ = 1 does
too) gives u^♭ ∈ H^(∞,(Ĕ_+∪̄{(z_1,0)},ℓ̆_+))_b(Ω_* ∩ 𝓘⁺). Then f − L_b v has no term ρ_I^(z_1+1) in slot 7: the
remainder from L̃ is ρ_I^(z_1+2) times H^∞-functions with the index set ℰ^(♯,(1))_+ + 2 at ι⁺, and
z_1 + 2 ∈ ℰ_I^tot + 2 ⊂ ℰ_I^C + 1 ([[lem:iii-c-3-2]] (c)); the derivatives of χ are supported away from 𝓘⁺. So f is
reduced to

    f ∈ H^(∞,(F_I+1,ℓ_I+1),(F_++2,ℓ̆_++2))_b,      F_I = ℰ_I^C,      F_+ = ℰ^(♯,(1))_+.        {#eq:iii-i1-3-3}

*Step 2: the remaining terms.* Given [[eq:iii-i1-3-3]], let z ∈ π_1F_I with Re z < min Re F_I + 1 and Re z ≤ ℓ_I, let
k := k(F_I, z), and let χρ_I^(z+1)(log ρ_I)^k f^((z+1,k)) be the corresponding term of f, with
f^((z+1,k)) ∈ H^(∞,(F_++2,ℓ̆_++2))_b(Ω_* ∩ 𝓘⁺; S²T*). As Re z > 3/2 + 2γ_Υ ([[def:iii-c-3-1]] (2)) and
Re z ≤ ℓ_I < ℓ_I^max, z ∉ 3/2 + spec Ā, so z − 3/2 − Ā is invertible. Let u^((z,k)) solve

    (z − 3/2 − Ā)(X_+ − z)u^((z,k)) = ρ_+⁻²f^((z+1,k)),        u^((z,k)) = 0 for t_* ≤ 1;

by [[lem:iii-a-1-2]] (ℓ̆_+ ≠ Re z), u^((z,k)) ∈ H^(∞,(F_+∪̄{(z,0)},ℓ̆_+))_b(Ω_* ∩ 𝓘⁺). By [[eq:iii-a-1-1]] in ρ_I,

    L_0(ρ_I^z(log ρ_I)^k u^((z,k)))
        = ρ_I^z(log ρ_I)^k ρ_+⁻²f^((z+1,k)) + ρ_I^z Σ_(k′<k) (log ρ_I)^(k′) ρ_+⁻²f′^((z+1,k′)),

with explicit f′^((z+1,k′)) ∈ H^(∞,((F_+∪̄{(z,0)})+2,ℓ̆_++2))_b; and L̃ applied to it gives terms
ρ_I^(z+1+j)(log ρ_I)^(k″), j ≥ 1, k″ ≤ k, which lie in F_I + 1 at 𝓘⁺ beyond the current window (z + j ∈ ℰ_I^C, as
ℰ_I^C + 1 ⊂ ℰ_I^C by [[lem:iii-c-3-2]] (a); L̃ has smooth coefficients, so the shifts are integers). Replacing f by
f − L_b(χρ_I^z(log ρ_I)^k u^((z,k))) replaces (F_I, F_+) by (F_I ∖ {(z, k)}, F_+ ∪̄ {(z, 0)}); repeating for
(z, k − 1), …, (z, 0) gives (F_I ∖ {(z, j)}_(j≤k), F_+ ∪̄^(k+1) {(z, 0)}), the logarithmic order at z rising by one at
each repetition through the extended union. Doing this for every such z (finitely many, by the construction of
[[lem:iii-c-3-2]] (e)) replaces F_I by {(z, k) ∈ F_I : Re z ≥ min Re F_I + 1} and F_+ by the next set of
[[eq:iii-i1-3-2]]. Finitely many rounds exhaust the terms with Re z ≤ ℓ_I, and the remainder has the 𝓘⁺-weight ℓ_I + 1
with no expansion, which is [[eq:iii-i1-3-1]]. The terms of u vanish on {ρ_I > ½c_I} by the cut-off and on {t_* < 1}
by construction, and lie in the class of [[def:iii-i-1-1]] (1): their 𝓘⁺-exponents are those of ℰ_I^C, and z_1 in
slot 7, with (z_1, 0) ∈ ℰ_(I,11). If the terms of f vanish for Re z ≤ C_0, the corresponding u^((z,k)) are 0. ∎

By [[eq:iii-i1-3-2]], min Re ℰ^♯_+ = min(min Re Ĕ_+, 3/2 + (1 − e_Υ)γ_Υ), since min Re ℰ_I^C > 3/2 + 2γ_Υ: when Ĕ_+
does not go lower, the index set at ι⁺ of the formal solution starts at 3/2 + (1 − e_Υ)γ_Υ.

### Almost linear bounds: the setting {#sec:iii-i2-1}

This section and [[sec:iii-i2-2]]–[[sec:iii-i2-5]] are [Hin26, Section 11.3] in dimension 4 + 1: the improvement of the
forward solutions of L^(g,g_0)u = f at ι⁺ and K⁺ for right sides with more decay there ([Hin26, Proposition 11.17]),
with the two integration lemmas it rests on ([Hin26, Lemmas 11.18 and 11.19]). The scheme is that of [Hin26]. The
forward solution of [[thm:iii-i-5-3]] is improved by rewriting L_b u = f − (L^(g,g_0) − L_b)u, solving away the terms
at null infinity ([[prop:iii-i1-3-1]]), splitting L_b⁻¹ by the Fourier transform in t_* into high, regular low and
singular low frequencies, integrating the singular part twice in t_*, and recovering the expansion at null infinity
([[prop:iii-i1-2-1]]). The bookkeeping window of the iteration is (0, 1), the window of [[eq:iii-h-1-1]] inside the
indicial gap of L̂_b(0) ([[prop:iii-f1-2-3]] (a)), where [Hin26] has (0, ε_ind). As in [[thm:iii-i-5-3]], everything in
these sections is at b = b₀; base points b near b₀ are treated in [[ch:s25]].

*The manifold.* X = {r ≥ r_0} as in [[sec:iii-h-1]], and M′ := [ℝ̄_(t_*) × X̄; {±∞} × ∂X̄], the manifold M of
[[sec:ii-g1-3-1]] over X̄ ([[rem:ii-g1-3-7]]; [[sec:iii-a-4]] in dimension 4 + 1). Its faces are I (the lift of
ℝ̄ × ∂X̄; its part in t_* > 0 is 𝓘⁺), ι = ι⁺ ∪ ι⁻ (the front faces) and K = K⁺ ∪ K⁻ (the lifts of {±∞} × X̄), and it
has the artificial boundary {r = r_0}, at which all spaces are extendible. H^(k,β_I,β_ι,β_K)_b(M′), with index sets
where written, are the spaces of [[sec:iii-a-4]] for the b-density |dt_*/⟨t_*⟩| μ_b, μ_b = |dx|/⟨x⟩⁴; on Ω_* they are
the spaces of [[sec:iii-i-1]] (the last paragraph of [[cor:ii-g1-4-5]]). Put Ω_− := cl_(M′){t_* ≤ 1} and, for C > 0,
Ω_< := cl_(M′){t_* ≤ −Cr}, with H̄ for restrictions. X^±_(sc-b) and its spaces, with the faces scf, tf, zf and the
weights listed in that order, are those of [[sec:ii-g1-3-1]] ([[eq:ii-g1-3-2]]).

*Coordinates.* With r = |x|:

(a) near I ∩ ι⁺, on {t_* > 0}: ρ_I := t_*/r and ρ_+ := 1/t_* ([Hin26, (3.4e)]), and
t_*∂_(t_*) = ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+);

(b) near ι⁺ ∩ K⁺: ρ_+ := 1/r and ρ_K := r/t_* ([Hin26, (3.4g)]), and near all of K⁺, ρ_K := ⟨x⟩/t_* with x ∈ X̄; in
both, t_*∂_(t_*) = −ρ_K∂_(ρ_K) at fixed x;

(c) near I ∩ ι⁻, on {t_* < 2}: ρ_0 := (2 − t_*)⁻¹ and ρ_I := (2 − t_*)/r, and
(2 − t_*)∂_(t_*) = ρ_0∂_(ρ_0) − ρ_I∂_(ρ_I).

Indeed, in (a), t_*∂_(t_*)ρ_I = ρ_I and t_*∂_(t_*)ρ_+ = −ρ_+; in (c), ∂_(t_*)ρ_0 = ρ_0² and ∂_(t_*)ρ_I = −1/r. The
chart [Hin26, (3.4c)] uses t_* + 2, whose field −(t_* + 2)∂_(t_*) vanishes at t_* = −2; (c) covers {t_* < 2} in one
chart. In all three, ∂_(t_*) ∈ ρ_ιρ_K 𝒱_b(M′) (ρ_ι, ρ_K defining functions of ι, K), so ∂_(t_*) raises the ι- and
K-weights by 1 and keeps the I-weight.

*The operator.* L_b := L_(b₀); g_0 := g_(b₀,b₀,−S), g := g_0 + h and L := L^(g,g_0), with |S| < ε_0, h ∈ 𝒳^∞
([[eq:iii-i-1-4]]) and ‖h‖_(𝒳^d) < ε_0, where ε_0 and d are those of [[thm:iii-i-5-3]]. L̂_b(σ) is invertible for real
σ ≠ 0 ([[cor:iii-h-4-4]]), and so is the augmented operator L̃_b(σ) of [[def:iii-h-3-1]] for 0 < |σ| ≤ c_k
([[cor:iii-h-4-2]]). ℓ_I^max is [[eq:iii-i1-1-1]], and σ_Υ is as at the start of the chapter.

*The gap.* By [[prop:iii-f1-2-3]] (a) no indicial root of L̂_b(0) has real part in (0, 1], so (0, 1) lies in its
indicial gap for μ_b; [[eq:iii-h-1-1]] takes its weight α with α + 2 ∈ (0, 1), and so do these sections.

### Integration of ∂_(t_*) {#sec:iii-i2-2}

**Lemma {#lem:iii-i2-2-1}** (Integration of ∂_(t_*); [Hin26, Lemma 11.18] in dimension 4 + 1.) Let k ∈ ℕ₀,
β_I, β_ι, β_K ∈ ℝ with β_K ≠ 0, ℰ_K an index set, and C > 0.

(1) (*From t_* = 1.*) If u|_(Ω_−) ∈ H̄^(k,β_I,β_ι,(ℰ_K,β_K))_b(Ω_−) and
∂_(t_*)u ∈ H^(k,β_I,β_ι+1,(ℰ_K+1,β_K+1))_b(M′), then for every ε > 0

    u ∈ H^(k,β_I,min(β_ι,β_I−ε),(ℰ_K∪̄{(0,0)},β_K))_b(M′).                                               {#eq:iii-i2-2-1}

(2) (*From t_* = −Cr.*) If u|_(Ω_<) ∈ H̄^(k,∞,β_ι,β_K)_b(Ω_<) and
(∂_(t_*)u)|_(Ω_−) ∈ H̄^(k,β_I,β_ι+1,β_K+1)_b(Ω_−), then for every ε > 0

    u|_(Ω_−) ∈ H̄^(k,min(β_I,β_ι−ε),β_ι,β_K)_b(Ω_−),                                                    {#eq:iii-i2-2-2}

and likewise with (ℰ_K, β_K) and (ℰ_K + 1, β_K + 1) in place of β_K and β_K + 1.

As Ω_< ∩ I = ∅, the first weight on Ω_< is immaterial; the K⁻-weight in [[eq:iii-i2-2-2]] is the a priori one, and the
content of [[eq:iii-i2-2-2]] is the I-weight.

*Proof.* (1) *Near I ∩ ι⁺.* In the chart (a), with x := ρ_I/C′ and y := ρ_+/2 for a large C′, so that
{y ≥ ½} = {t_* ≤ 1} and {x < 2} covers {t_* < 2C′r}, the hypotheses read (x∂_x − y∂_y)u = t_*∂_(t_*)u ∈
H^(k,β_I,β_ι)_b (as t_* = ρ_+⁻¹ is a defining function of ι⁺ to the power −1 there) and u ∈ H^(k,β_I)_b on
{y ≥ ½}. [[lem:iii-a-3-2]] with z = 0, E = F = ∅, α := β_I and the target weight β := β′_ι := min(β_ι, β_I − ε) (so
that α > β and the right side lies in H^(k,α,β)_b) gives u ∈ H^(k,β_I,β′_ι)_b there. (The flow of x∂_x − y∂_y
preserves xy and increases x as y decreases, so the value at a point depends on the data at smaller x only; the end
x = 2 plays no role. Where the square [0, 2)² of the chart meets {r < r_0}, u is first extended across {r = r_0} by
the Seeley extension of [[rem:ii-g1-3-7]], which acts in the spatial variable and commutes with ∂_(t_*); the
characteristics being the sets {r = const}, nothing propagates across {r = r_0}.) This holds on every set
{t_* ≤ C′r}, that is, off any neighbourhood of K⁺.

*Near K⁺.* In the chart (b) with ρ_K = ⟨x⟩/t_* and x ∈ X̄, ρ_K∂_(ρ_K)u = −t_*∂_(t_*)u ∈ H^(k,(ℰ_K,β_K),β_ι)_b
(t_* = ⟨x⟩ρ_K⁻¹), and on {ρ_K ≥ ½}, a set of the previous kind, u has the ι⁺-weight β′_ι ≤ β_ι. [[lem:iii-a-1-2]] with
z = 0 (β_K ≠ 0) and H := X̄ (the ι⁺-face ∂X̄ carrying the weight β′_ι; its solution operators act in ρ_K alone and
commute with the extension at {r = r_0}) gives u ∈ H^(k,(ℰ_K∪̄{(0,0)},β_K),β′_ι)_b near K⁺. Away from I ∪ ι⁺ ∪ K⁺ in
t_* ≥ 1 the set is compact, and u(t_*) = u(1) + ∫_1^(t_*) ∂_(t_*)u gives H^k there. With the hypothesis on Ω_− this is
[[eq:iii-i2-2-1]].

(2) Ω_− ∖ Ω_< is covered by the chart (c) on {r ≥ R}, where ρ_I ≤ C + 2/R, and by the compact set
{r ≤ R, −CR ≤ t_* ≤ 1}, on which u(t_*) = u(−CR) + ∫_(−CR)^(t_*) ∂_(t_*)u gives the claim. In the chart (c), with
x := ρ_0 and y := ρ_I/C″, C″ > 2C, we have {y ≥ ½} ∩ {r ≥ R} ⊂ Ω_< for R large, and
(x∂_x − y∂_y)u = (2 − t_*)∂_(t_*)u ∈ H^(k,β_ι,β_I)_b (2 − t_* = ρ_0⁻¹ is a defining function of ι⁻ to the power −1).
[[lem:iii-a-3-2]] with z = 0, E = F = ∅, α := β_ι and the target weight min(β_I, β_ι − ε) < α at y = 0 gives
[[eq:iii-i2-2-2]] near I. It is applied to ψ(r)u, ψ = 1 on [R, ∞) and ψ = 0 on [0, R/2], so that the square of the
chart meets only {r ≥ R/2}; ψ(r) commutes with ∂_(t_*) and changes nothing on {r ≥ R}. The K⁻-weight: near K⁻, Ω_−
lies in Ω_< for every constant. Index sets at K pass through unchanged. ∎

### Integration with a moment condition {#sec:iii-i2-3}

**Lemma {#lem:iii-i2-3-1}** (Integration with a moment condition; [Hin26, Lemma 11.19] in dimension 4 + 1.) Let
Ω_< := cl_(M′){t_* < −r} and β_I, β_ι, β_K ∈ ℝ with β_ι > β_I, β_K ≤ β_ι − β_I and β_K ∈ (−1, 1) ∖ {0}. Suppose
u|_(Ω_<) ∈ H̄^(k,∞,β_ι,β_K)_b(Ω_<), ℱu is supported in [−c_0, c_0] × X for some c_0 < ½, and

    ℱ(∂_(t_*)u)|_(±(0,1]) ∈ H^(k+ℓ,(β_I,β_ι,((0,0),β_K)))_b(X^±_(sc-b)),                                 {#eq:iii-i2-3-1}

with ℓ a k-independent integer depending on the weights, the restrictions to zf of the two signs agreeing when β_K > 0.
Then u ∈ H^(k,β_I,β_ι−ε,((0,0),β_K))_b(M′) for every ε > 0.

[Hin26] states β_K < 1, β_K ≠ 0. The condition β_K > −1 is needed for the application of [[prop:ii-g1-3-5]] (1) below,
whose K-weight β_K + 1 must lie in (0, ∞) ∖ ℕ; it is implicit in [Hin26]. By [[prop:ii-g1-3-5]] (1) alone,
[[eq:iii-i2-3-1]] gives ∂_(t_*)u the I-weight β_I − ε, and [[lem:iii-i2-2-1]] would then give u the ι-weight β_I − 2ε
only; the moment condition [[eq:iii-i2-3-4]] below is what gives β_ι − ε. [Hin26] asks ℱu to be supported in
[−1, 1] × X. Its proof treats f_2 by [[prop:ii-g1-3-5]] (1), whose cut-off is 1 only near [−½, ½], and f_1 by
[[def:ii-g1-2-7]], which asks regularity across σ = ±1, where ℱf may jump. Support in [−c_0, c_0], c_0 < ½, meets
both, and the application in [[sec:iii-i2-5]] has it.

*Proof.* Let χ = χ(t_*/r) equal 0 on (−∞, −3] and 1 on [−2, ∞), and f := ∂_(t_*)u. As ∂_(t_*)χ = r⁻¹χ′(t_*/r) is
supported in {−3r ≤ t_* ≤ −2r} ⊂ Ω_<, away from I and K,

    ∂_(t_*)(χu) = f′ + χf,        f′ := (∂_(t_*)χ)u ∈ H^(k,∞,β_ι+1,∞)_b(M′).                             {#eq:iii-i2-3-2}

Let χ_scf ∈ C^∞_c([0, 2)) equal 1 on [0, 1], regarded as χ_scf(ρ/|σ|) on X^±_(sc-b), ρ = ⟨x⟩⁻¹ (1 near scf, 0 near
zf), and f_1 := ℱ⁻¹(χ_scf ℱf), f_2 := ℱ⁻¹((1 − χ_scf)ℱf). Since (1 − χ_scf)ℱf ∈
H^(k+ℓ,(∞,β_ι,((0,0),β_K)))_b (it vanishes near scf), [[prop:ii-g1-3-5]] (1) (with the K-weight
β_K + 1 ∈ (0, 2) ∖ {1}; for ℓ large) gives

    f_2,  χf_2 ∈ H^(k,β_ι+1−ε,β_ι+1,β_K+1)_b(M′),                                                       {#eq:iii-i2-3-3}

χ being bounded and conormal on M′. As χu = 0 for t_* ≤ −3r, χu = F′ + F_1 + F_2 with F′ := ∫_(−∞)^(t_*) f′ and
F_j := ∫_(−∞)^(t_*) χf_j.

*F′ and F_2.* F′ vanishes for t_* ≤ −3r. By [[lem:iii-i2-2-1]] (2) with C = 3 and [[eq:iii-i2-3-2]],
F′|_(Ω_−) ∈ H̄^(k,β_ι−ε,β_ι,∞)_b, and [[lem:iii-i2-2-1]] (1) (with a large nonzero K-weight) gives
F′ ∈ H^(k,β_ι−ε,β_ι−2ε,(0,0))_b(M′). Likewise, by [[eq:iii-i2-3-3]], F_2|_(Ω_−) ∈ H̄^(k,β_ι−ε,β_ι,∞)_b and
F_2 ∈ H^(k,β_ι−ε,β_ι−2ε,((0,0),β_K))_b(M′) (β_K ≠ 0).

*F_1.* As χ_scf vanishes near zf, ℱf_1 = χ_scf ℱf ∈ H^(k+ℓ,(β_I,β_ι,∞))_b. On its support, near tf ∩ scf,
ρ_scf = ρ/|σ| and ρ_tf = |σ| (the proof of [[lem:iii-a-4-1]]), and near scf° ρ_scf ∼ ρ. Let γ := β_ι − β_I if this is
not an integer, and γ := β_ι − β_I − ε′ with 0 < ε′ < min(ε, 1 − β_K) if it is (then it is at least 1); so γ ∉ ℕ,
γ ≥ β_ι − β_I − ε and γ ≥ β_K. Then

    ℱf_1 = ρ^(β_I)|σ|^γ w,        w ∈ H^(k+ℓ)_b(±[0, 1]_σ × X̄; |dσ/σ| μ_b).

So the pair (ℱf_1|_((−∞,0)), ℱf_1|_((0,∞))) lies in the space X^(k′,γ) of [[def:ii-g1-2-7]], with vanishing polynomial
part and with values in ρ^(β_I)H^(k″)_b(X̄, μ_b); and [[prop:ii-g1-2-8]] (2) with β = γ + 1 ∉ ℕ, applied to V^αℱf_1 for
the b-vector fields V on X̄ (ℱ commutes with them), gives f_1 ∈ ρ^(β_I)⟨t_*⟩^(−γ−1)H^k_b(ℝ̄_(t_*) × X̄), in the
convention H^(k,β)_b(ℝ) = ⟨t_*⟩^(−β)H^k_b(ℝ, |dt_*/⟨t_*⟩|) of [[def:ii-g1-2-1]]; so does χf_1. As γ > 0, f_1(·, x) is
integrable in t_* (by Cauchy–Schwarz with ⟨t_*⟩^(−2γ−1)), and |ℱf_1(σ)| ≤ C|σ|^γ (by Sobolev embedding in log|σ|,
ℓ ≥ 1), so

    ∫_ℝ f_1(t_*, x) dt_* = ℱf_1(0, x) = 0.                                                             {#eq:iii-i2-3-4}

*For t_* ≤ 1:* integrating χf_1 from −∞ ([[lem:iii-a-1-2]] in τ = |t_*|⁻¹, where t_*∂_(t_*) = −τ∂_τ, with the weight
γ > 0 and the solution vanishing at τ = 0) gives
F_1|_({t_*≤1}) ∈ ρ^(β_I)⟨t_*⟩^(−γ)H̄^k_b([−∞, 1] × X̄) = H̄^(k,β_I,β_I+γ,γ)_b(Ω_−): near I, ρ ∼ ρ_I; near ι⁻, ρ and
⟨t_*⟩⁻¹ are both ∼ ρ_ι; near K⁻, ⟨t_*⟩⁻¹ ∼ ρ_K; and the b-vector fields of ℝ̄ × X̄ lift to span those of M′.

*For t_* ≥ −1:* by [[eq:iii-i2-3-4]],

    F_1(t_*) = −∫_(t_*)^∞ f_1(s) ds + F_3(t_*),        F_3(t_*) := ∫_(−∞)^(t_*) ((χ − 1)f_1)(s) ds.

The first term lies in ρ^(β_I)⟨t_*⟩^(−γ)H̄^k_b([−1, ∞] × X̄), which has the weights (β_I, β_I + γ, γ) at (I, ι⁺, K⁺), by
the same integration from +∞. (χ − 1)f_1 is supported in {t_* ≤ −2r}, so F_3|_(Ω_<) ∈ H̄^(k,∞,β_I+γ,γ)_b as above, and
∂_(t_*)F_3 = (χ − 1)f_1 ∈ H^(k,∞,β_I+γ+1,γ+1)_b(M′). [[lem:iii-i2-2-1]] (2) (with C = 1) gives
F_3|_(Ω_−) ∈ H̄^(k,β_I+γ−ε,β_I+γ,γ)_b, and [[lem:iii-i2-2-1]] (1) (γ ≠ 0) gives
F_3 ∈ H^(k,β_I+γ−ε,β_I+γ−2ε,((0,0),γ))_b(M′). Altogether, as β_I + γ − ε ≥ β_I for ε small and β_I + γ ≥ β_ι − ε,
F_1 ∈ H^(k,β_I,β_ι−3ε,((0,0),γ))_b(M′).

*Conclusion.* χu = F′ + F_1 + F_2 ∈ H^(k,β_I,β_ι−3ε,((0,0),β_K))_b, as γ ≥ β_K. (1 − χ)u is supported in
{t_* ≤ −2r} ⊂ Ω_<, with the weights (∞, β_ι, β_K). Renaming ε gives the claim. ∎

### The three frequency ranges {#sec:iii-i2-4}

Fix k. Let c ∈ (0, ½] be at most ς_1 of [[lem:ii-g1-4-6]], the c_(k′) of [[cor:iii-h-4-2]] and the c_(j,k′) of
[[thm:iii-h-4-1]] (3) for j + k′ ≤ k + ℓ_0, ℓ_0 being the losses below, and let χ ∈ C^∞_c([0, c)) equal 1 on
[0, c/2], as in [[sec:iii-h1-2]]. So c depends on k, and, through the weight α of [[eq:iii-h-1-1]] ([[lem:iii-i2-4-2]]),
on the step of [[sec:iii-i2-5]] in which it is used. The memberships [[eq:iii-i2-5-5]]–[[eq:iii-i2-5-9]] below hold at
the order k for that c, the losses ℓ_0 being independent of k; u, u_I and u^♭ do not depend on c, so their memberships
hold at every order. H^∞ in [[eq:iii-i2-5-5]]–[[eq:iii-i2-5-9]] is to be read in this sense.

For f ∈ C^∞_c(Ω_*°), [[lem:iii-h1-2-1]], [[eq:iii-h1-4-1]]–[[eq:iii-h1-4-2]] and [[eq:iii-h1-5-1]]–[[eq:iii-h1-5-2]] give
the forward solution of L_b u = f as u = u_hi + u_reg + u_sing, with ℱu_hi = (1 − χ(|σ|))L̂_b(σ)⁻¹f̂(σ) on ℝ,
ℱu_reg = χ(|σ|)û_(reg,1)(σ) on ℝ (the proof of [[lem:iii-h1-4-1]]),
(û_(reg,1), b̂_1, Ŝ_1) := L̃_b(σ)⁻¹(f̂(σ), 0, 0), and u_sing = v_ġ + v_h of [[eq:iii-h1-5-1]]–[[eq:iii-h1-5-2]], with (the proof of
[[lem:iii-h1-5-1]])

    ℱ(∂_(t_*)v_ġ) = χ(|σ|)G_1(σ)(b̂_1(σ)),        ℱ(∂²_(t_*)v_h) = χ(|σ|)G_2(σ)(Ŝ_1(σ)),
    G_1(σ)(ḃ) := Ψ(σ, ·)ġ(ḃ),        G_2(σ)(S) := (Ψ − σ∂_σΨ)h(S) − iσΨh̆(S),                            {#eq:iii-i2-4-1}

with Ψ of [[lem:iii-h-2-5]]. The bounds below are linear in f, and the forward solution map is continuous
([[thm:iii-i-5-3]] with h = 0, S = 0), so the decomposition and the bounds extend by density to the spaces stated. These
spaces are extendible at {r = r_0}, where C^∞_c(Ω_*°) is not dense: one approximates an extension of f across
{r = r_0}, vanishing for t_* < 1, by smooth compactly supported functions, for which the decomposition holds, and
restricts. The forward solution on {r ≥ r_0} depends on f there only, since {r = r_0} is spacelike with dr future
timelike ([[lem:ii-c-3-2]] (1)), so that r decreases along future causal curves. [[ch:s18]] uses the same convention.

**Lemma {#lem:iii-i2-4-1}** (High and bounded frequencies; [Hin26, (11.44)] in dimension 4 + 1.) Let
f ∈ H^(∞,(β^f_I+1,β_ι+2,β_K))_b(Ω_*)^(•,−) with β_K ∈ (0, ∞) ∖ ℕ, β^f_I ≥ 3/2 and
β^f_I + 1 ≥ β_ι + 2 − min(β_K, 1 − ε_1) for some ε_1 ∈ (0, 1). Then u_hi ∈ H^(∞,(3/2−ε,N,N))_b(M′) for every N and
every ε > 0.

*Proof.* Let χ_(C_0) be the cut-off of [[cor:ii-g1-4-5]] (1 on [−C_0, C_0], supported in [−C′_0, C′_0]). The piece
ℱ⁻¹((1 − χ_(C_0))L̂_b⁻¹f̂) lies in H^(∞,(β′_I,N,N))_b(M′) for every β′_I < min(β^f_I, 3/2 + S̄) = 3/2, by
[[cor:ii-g1-4-5]] (with the hypotheses of [[ch:s02]] for 2L_(b₀), as in [[sec:iii-h1-3]]; S̄ = 0, as in the proof of
[[thm:iii-i-5-3]]). The rest is w := (χ_(C_0) − χ(|σ|))L̂_b⁻¹f̂, supported in J := {c/2 ≤ |σ| ≤ C′_0}. By
[[prop:ii-g1-3-3]] (1) and (2), whose hypotheses on the weights are those of the lemma, f̂ lies on ±(0, 1] in
H^(∞,(min(β^f_I+1,β_ι+2)−ε,β_ι+1,·))_b(X^±_(sc-b)), and on ±[½, ∞) in the high-frequency space with the scf-weight
β^f_I + 1. On functions supported in the compact set J, away from tf and zf, both norms are equivalent to that of
H̄^(∞,β)_b(J × X̄) of [[cor:ii-g1-4-2]] (2), with β the scf-weight. So f̂|_J ∈ H̄^(∞,5/2−ε)_b(J × X̄), as β_ι + 2 ≥ 5/2
and β^f_I + 1 ≥ 5/2 (if β_ι < ½, use the weaker weight β_ι + 2 − ε in place of 5/2 − ε throughout; in the
applications β_ι > ½). [[cor:ii-g1-4-2]] (2) with β_scf := 3/2 − ε < 3/2 + S̄ (L̂_b(σ) is invertible on J̄,
[[cor:iii-h-4-4]]) gives w ∈ H̄^(∞,3/2−2ε)_b(J × X̄). With χ′ the cut-off of [[prop:ii-g1-3-5]], χ′w is supported away
from tf and zf and lies in H^(∞,(3/2−2ε,N,N))_b(X^±_(sc-b)) for every N (and has no Taylor coefficients at 0), so
[[prop:ii-g1-3-5]] (1) gives ℱ⁻¹(χ′w) ∈ H^(∞,(3/2−3ε,N,N))_b(M′); and (1 − χ′)w, supported in ±[½, C′_0], lies in the
high-frequency space with every σ-weight, so [[prop:ii-g1-3-5]] (2) gives ℱ⁻¹((1 − χ′)w) ∈ H^(∞,(3/2−2ε,N,N))_b(M′).
Each step loses finitely many derivatives, depending on N; the space is H^∞. ∎

**Lemma {#lem:iii-i2-4-2}** (Low frequencies; [Hin26c, Proposition 13.18] for L̃_b, [Hin26, (11.45)].) Let α be as in
[[eq:iii-h-1-1]], β_scf < 3/2, ε ∈ (0, 1), and β_tf, β_zf with β_tf − β_zf = α + 2. There is ℓ such that for
f̂ ∈ H^(k+ℓ,(β_scf+1,β_tf+2,β_zf))_b(X^±_(sc-b)) (over ±[0, c]) and (û, b̂, Ŝ)(σ) := L̃_b(σ)⁻¹(f̂(σ), 0, 0),

    û ∈ H^(k,(β_scf−ε,β_tf,β_zf))_b(X^±_(sc-b)),        b̂, Ŝ ∈ H^(k,β_zf)_b(±(0, c], |dσ/σ|),           {#eq:iii-i2-4-2}

with norms bounded by that of f̂.

*Proof.* This is the proof of [[prop:ii-g1-4-7]], with [[cor:iii-h-4-2]] and [[thm:iii-h-4-1]] (3) for L̃_b in place of
[[thm:i-c-6-4]] (4)–(5). Division by the scalar |σ|^(β_zf), which commutes with L̃_b(σ)⁻¹ (componentwise, L̃_b⁻¹ being
linear) and satisfies σ∂_σ|σ|^(β_zf) = β_zf|σ|^(β_zf), reduces to β_zf = 0, β_tf = α + 2. Take α_+ := 0,
𝗋_out := β_scf − 2 − ε/2, below the outgoing threshold −½ + S̄ = −½, and the orders of [[sec:i-c-6]] built from it,
equal to 𝗋_out near the zero section over sctf (as the proof of [[cor:iii-h-4-2]] uses them). For 0 < |σ| ≤ c and
j ≤ k, [[thm:iii-h-4-1]] (3) (its estimate [[eq:iii-h-4-2]], as [[lem:iii-h1-4-1]]–[[lem:iii-h1-4-2]] use it) bounds
‖(σ∂_σ)^j L̃_b⁻¹g‖ in ‖·‖_((s+j;m),(𝗋,α,0),ς), plus the moduli of the last two components, by
C‖g‖_((s−1;m+j),(𝗋+1,α+2,0),ς), ς = |σ|. [[eq:ii-g1-4-5b]] and [[eq:ii-g1-4-5a]] with l = α and ε/2 convert the left
side to H^(m−ℓ̃,(β_scf−ε,α+2,0))_(b,ς) and the right side to H^(m+j+ℓ_a,(β_scf+1,α+4,0))_(b,ς), as
𝗋_out + 2 − ε/2 = β_scf − ε and 𝗋_out + 3 + ε/2 = β_scf + 1. Leibniz' rule and integration in |dσ/σ| (the description of
the norm in [[sec:ii-g1-4-3]]) give [[eq:iii-i2-4-2]], with ℓ := ℓ_a + ℓ̃; for the moduli,
∫ Σ_(j≤k) |(σ∂_σ)^j b̂|² |dσ/σ| is bounded the same way. ∎

**Lemma {#lem:iii-i2-4-3}** (The cut-off states; [Hin26, (11.47)–(11.48)] in dimension 4 + 1.) Let a ∈ ℝ,
b̂ ∈ H^(∞,a)_b(±(0, c], |dσ/σ|; 𝔟_ℂ) and Ŝ ∈ H^(∞,a)_b(±(0, c], |dσ/σ|; 𝒮_(1,ℂ)). Then for every N and ε > 0,

    χ(|σ|)G_1(σ)(b̂(σ)) ∈ H^(∞,(N,a+2−ε,a))_b(X^±_(sc-b)),
    χ(|σ|)G_2(σ)(Ŝ(σ)) ∈ H^(∞,(N,a+3−ε,a))_b(X^±_(sc-b)).                                            {#eq:iii-i2-4-3}

[Hin26, (11.47)] has the orders (1 − ε, 1 − ε, ·) and (1 − ε, 2 − ε, ·) for the states before the cut-off, so that
[Hin26, (11.48)] has (1 − ε, a + 1 − ε, a) and (1 − ε, a + 2 − ε, a).

*Proof.* *Pointwise bounds.* By [[sec:iii-h-1]] the states ġ(ḃ) lie in 𝒜^q with q = 2 (for ṁ) or q = 3 (for Ȧ), and
h(S) ∈ 𝒜³, h̆(S) ∈ 𝒜². For r ≥ 1, Ψ = Φ(σr), Φ entire with |∂^j_ζΦ| ≤ C_(j,M)⟨ζ⟩^(−M) ([[lem:iii-h-2-5]] (b)),
σ∂_σΨ = ζΦ′(ζ) and r∂_rΨ = ζΦ′(ζ), ζ = σr. So G_1(ḃ) = Φ(ζ)ġ and
G_2(S) = (Φ − ζΦ′)(ζ)h − iζΦ(ζ) r⁻¹h̆, with r⁻¹h̆ ∈ 𝒜³. For r ≤ 1, Ψ and its σ- and x-derivatives are bounded for
|σ| ≤ 1 ([[lem:iii-h-2-5]] (d) and its proof). Hence, with q_1 := 2, q_2 := 3 and V any product of σ∂_σ and b-vector
fields on X̄, |VG_i| ≤ C_(V,M)⟨|σ|⟨x⟩⟩^(−M)⟨x⟩^(−q_i) on basis elements.

*Weights.* By [[sec:ii-g1-4-3]] the norm of H^(K,β)_b(X^±_(sc-b)) is equivalent to

    (Σ_(K′≤K) ∫ ‖(σ∂_σ)^(K′)v(σ)‖²_(H^(K−K′,β)_(b,|σ|)) |dσ/σ|)^(1/2),

with ‖v‖_(H^(m,β)_(b,ς)) = ‖w_β(ς)⁻¹v‖_(H̄^m_b(X̄,μ_b)) and (the proof of [[lem:ii-g1-4-6]])
w_β(ς) ∼ ς^(β_tf)W_β(ρ̂), ρ̂ := ⟨x⟩⁻¹/ς, W_β(ρ̂) = (ρ̂/(1 + ρ̂))^(β_scf)(1 + ρ̂)^(β_tf−β_zf), with bounded logarithmic
derivatives. Take β = (N, a + q_i − ε, a), so that β_tf − β_zf = q_i − ε. Where ς⟨x⟩ ≥ 1 (ρ̂ ≤ 1),
W_β⁻¹ ≤ C(ς⟨x⟩)^N, and with M = N + q_i, |W_β⁻¹VG_i| ≤ Cς^(q_i)(ς⟨x⟩)^(−2q_i), whose square is μ_b-integrable there
with integral ≤ Cς^(2q_i). Where ς⟨x⟩ ≤ 1, W_β⁻¹ ≤ C(ς⟨x⟩)^(q_i−ε), so |W_β⁻¹VG_i| ≤ Cς^(q_i−ε)⟨x⟩^(−ε), and
∫ ⟨x⟩^(−2ε) μ_b < ∞. So ‖W_β⁻¹VG_i(σ)‖_(L²(μ_b)) ≤ C|σ|^(q_i−ε), and by Leibniz' rule

    ‖χG_1(b̂)‖²_(H^(K,β)) ≤ C Σ_(K′≤K) ∫ |σ|^(−2(a+q_1−ε)) |σ|^(2(q_1−ε)) |(σ∂_σ)^(K′)b̂|² |dσ/σ| = C‖b̂‖²_(H^(K,a)_b),

and likewise for G_2. ∎

### Almost linear bounds {#sec:iii-i2-5}

**Proposition {#prop:iii-i2-5-1}** (Almost linear bounds; [Hin26, Proposition 11.17] in dimension 4 + 1, at b₀.) Let
ℰ_I^C and ℰ_+ be as in [[def:iii-i-1-1]], L as in [[sec:iii-i2-1]], and

    2 ≤ ℓ_I < min(a_I + ½, ℓ_I^max),        ℓ_I ∉ Re π_1ℰ_I^C,        ℓ_I ∉ 3/2 + σ_Υ.                  {#eq:iii-i2-5-1}

Let α_K ∈ [½, 1), α_+ > α_K and β_+ < min(α_+, 3/2, min Re ℰ_+). For
f ∈ H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),α_++2,α_K)_b(Ω_*; S²T*)^(•,−), the forward solution u of Lu = f satisfies

    u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),β_+,α_K−2)_b(Ω_*; S²T*)^(•,−).                                                {#eq:iii-i2-5-2}

Moreover u depends continuously on (S, h) in the space [[eq:iii-i2-5-2]] with every weight lowered by ς, for every
ς > 0.

[Hin26] has the ι⁺-weight α_K − ε and the 𝓘⁺-weight 3 + ε_I. Its proof notes that the decay would be α_+ but for the
singular terms at σ = 0. In dimension 4 + 1 they do not limit it, and the cap is 3/2: the scf-weight of
[[lem:iii-i2-4-1]] and [[lem:iii-i2-4-2]], that is, the transport of the order of the radiation field from 𝓘⁺; the
corresponding cap in [Hin26, pp. 232 and 238] is 1. The condition ℓ_I ≥ 2 serves [[prop:ii-g1-3-3]] (1) in
[[lem:iii-i2-4-1]] and in Step 2b, which needs ℓ_I + 1 ≥ γ_+ + 2 − α̃_K, that is ℓ_I ≥ 2 for ι⁺-weights up to 3/2;
the 3 + ε_I of [Hin26] meets it. The bound ℓ_I < a_I + ½ is the range of [[prop:iii-i-4-1]].

*Proof.* *Step 0: the start.* By [[def:iii-c-3-1]] (2), min Re ℰ_I^C > 3/2 + 2γ_Υ, so the 𝓘⁺-exponents of f
(ℰ_I^C + 1, and ℱ_(I,11) ⊂ 1 + (ℰ_I^C ∪ (3/2 + (1 − e_Υ)γ_Υ, 0)) for π₁₁) have real parts > 5/2, and
f ∈ H^(∞,(5/2−ε,α_++2,α_K))_b. Fix β^(0)_+ ∈ (½, min(α_+, 3/2, min Re ℰ_+)) and β^(0)_I ∈ (β^(0)_+, 3/2).
[[thm:iii-i-5-3]] (α_K ≥ ½) gives u ∈ H^(∞,(β^(0)_I,β^(0)_+,−3/2))_b. [[prop:iii-i1-2-1]] with ℓ_+ := β^(0)_+ (which
is below min Re ℰ_+, so that (ℰ_+, ℓ_+) is the weight ℓ_+, and ℓ_+ < a_+ + min Re ℰ_+, a_+ > 0; ℓ_+ lies neither in
Re π_1ℰ_+ nor in Re π_1ℰ_I^tot, whose least real part is 3/2; and ℓ_+ < 3/2 < ℓ_I), f having the ι⁺-weight
α_+ + 2 ≥ ℓ_+ + 2, gives the expansion at 𝓘⁺ near 𝓘⁺; away from 𝓘⁺ nothing changes. So

    u ∈ H^(∞,(⟨ℰ_I^C⟩,ℓ_I),β′_+,α′_K−2)_b                                                             {#eq:iii-i2-5-3}

holds with (α′_K, β′_+) = (½, β^(0)_+).

*The iteration.* Suppose [[eq:iii-i2-5-3]] holds with α′_K ∈ [½, α_K] and β′_+ ∈ (½, min(α_+, 3/2, min Re ℰ_+)). Put
α̃_K := min(α′_K + a_K − 2, α_K) and fix

    γ_+ ∈ (α_K, min(α_+, 3/2, min Re ℰ_+)),     ε > 0 with γ_+ < 3/2 − 5ε,  γ_+ − 4ε > max(½, α_K).      {#eq:iii-i2-5-4}

Then γ_+ − α̃_K ∈ (0, 1) (as α̃_K ≤ α_K < γ_+ < 3/2 ≤ α̃_K + 1) and γ_+ < α̃_K + 1 − ε.

*Step 1: the rewriting ([Hin26, (11.41)]).* By [[eq:iii-i-4-2]] of [[prop:iii-i-4-1]], whose hypotheses hold
(3/2 < ℓ_I < a_I + ½; 0 < β′_+ < min Re ℰ_+ ≤ max(a_+, min Re ℰ_+)), (L − L_b)u has the 𝓘⁺-data
(⟨ℰ_I^C+1⟩′, ℓ_I + 1), the ι⁺-weight β′_+ + 2 + m_+ − ε (with no expansion term, as β′_+ + m_+ < 2 min Re ℰ_+) and the
K⁺-weight α′_K − 2 + a_K. As β′_+ + m_+ − ε > ½ + 1 − ε > γ_+,

    L_b u = f′ := f − (L − L_b)u ∈ H^(∞,(⟨ℰ_I^C+1⟩′,ℓ_I+1),γ_++2,α̃_K)_b(Ω_*)^(•,−).

*Step 2a: null infinity ([Hin26, (11.42)]).* [[prop:iii-i1-3-1]] with Ĕ_+ := ∅ and ℓ̆_+ := γ_+ (γ_+ < 3/2 <
min Re ℰ_I^C and γ_+ ≠ 3/2 + (1 − e_Υ)γ_Υ; ℓ_I by [[eq:iii-i2-5-1]]) gives u_I, vanishing on
{t_* < 1} ∪ {ρ_I > ½c_I}, with the 𝓘⁺-data (⟨ℰ_I^C⟩, ℓ_I) and the ι⁺-data (ℰ^♯_+, γ_+), which is the weight γ_+ as
min Re ℰ^♯_+ ≥ min(3/2 + (1 − e_Υ)γ_Υ, min Re ℰ_I^C) > 3/2 ([[eq:iii-i1-3-2]]); and
f^♭ := f′ − L_b u_I ∈ H^(∞,ℓ_I+1,γ_++2,α̃_K)_b(Ω_*)^(•,−), the K⁺-weight being unchanged as u_I is supported near 𝓘⁺.
u^♭ := u − u_I vanishes for t_* < 1 and solves L_b u^♭ = f^♭, so it is the forward solution ([[prop:ii-e-3-4]]).

*Step 2b: the Fourier transform ([Hin26, (11.43)–(11.52)]).* Decompose u^♭ = u_hi + u_reg + u_sing as in
[[sec:iii-i2-4]], with f^♭ in place of f. [[prop:ii-g1-3-3]] (1), with (β_I, β_ι, β_K) = (ℓ_I + 1, γ_+ + 2, α̃_K)
(α̃_K ∈ (0, 1), and ℓ_I + 1 ≥ γ_+ + 2 − min(α̃_K, 1 − ε_1) for ε_1 < 1 − α̃_K, as ℓ_I ≥ 2 > γ_+ + 1 − α̃_K), gives

    f̂^♭|_(±(0,1]) ∈ H^(∞,(min(ℓ_I+1,γ_++2)−ε,γ_++1,α̃_K−1))_b(X^±_(sc-b)),

the zf index set (0, 0) dropping as α̃_K − 1 < 0.

*High frequencies.* [[lem:iii-i2-4-1]] (β^f_I = ℓ_I, β_ι = γ_+, β_K = α̃_K; its weight condition is the one just
checked) gives u_hi ∈ H^(∞,(3/2−ε,N,N))_b(M′).

*The regular part.* [[lem:iii-i2-4-2]] with β_scf := 3/2 − ε, β_tf := γ_+ − 1, β_zf := α̃_K − 1
(α + 2 := γ_+ − α̃_K ∈ (0, 1); the space of the right side contains f̂^♭, as 5/2 − ε ≤ min(ℓ_I + 1, γ_+ + 2) − ε)
gives

    û_(reg,1) ∈ H^(∞,(3/2−2ε,γ_+−1,α̃_K−1))_b,        b̂_1, Ŝ_1 ∈ H^(∞,α̃_K−1)_b(±(0, c], |dσ/σ|).       {#eq:iii-i2-5-5}

χ(|σ|)û_(reg,1) is supported where the cut-off of [[prop:ii-g1-3-5]] is 1 (c ≤ ½), and its Taylor condition is void
(K-weight α̃_K, α̃_K − 1 < 0); [[prop:ii-g1-3-5]] (1) gives

    u_reg ∈ H^(∞,(γ_+−ε,γ_+,α̃_K))_b(M′).                                                              {#eq:iii-i2-5-6}

*The singular part.* By [[eq:iii-i2-4-1]], [[lem:iii-i2-4-3]] with a = α̃_K − 1 and [[eq:iii-i2-5-5]], and
ℱ(∂_(t_*)v) = −iσℱv, which raises the tf- and zf-weights by 1,

    ℱ(∂²_(t_*)u_sing) = −iσχG_1(b̂_1) + χG_2(Ŝ_1) ∈ H^(∞,(N,α̃_K+2−ε,α̃_K−1))_b(X^±_(sc-b)).             {#eq:iii-i2-5-7}

([Hin26, (11.49)] has (1 − ε, α̃_K + 1 − ε, α̃_K); the zf-weight that [Hin26, (11.48)] gives, and with which [Hin26,
Lemma 11.19] is then applied, is α̃_K − 1.) As u^♭ = 0 for t_* < 1, u_sing = −(u_hi + u_reg) there, so by
[[eq:iii-i2-5-6]] and the bound for u_hi, with γ_+ < 3/2 − ε,

    u_sing|_(Ω_−) ∈ H̄^(∞,γ_+−ε,γ_+,α̃_K)_b,        ∂_(t_*)u_sing|_(Ω_−) ∈ H̄^(∞,γ_+−ε,γ_++1,α̃_K+1)_b.  {#eq:iii-i2-5-8}

*First integration.* [[lem:iii-i2-3-1]] applies to v := ∂_(t_*)u_sing with β_I := 3/2, β_ι := γ_+ + 1 and
β_K := α̃_K − 1. Indeed β_ι > β_I (γ_+ > ½); β_K < 0 < β_ι − β_I; β_K ∈ [−½, 0); v|_(Ω_<) has the weights
(·, γ_+ + 1, α̃_K + 1), at least (∞, β_ι, β_K), by [[eq:iii-i2-5-8]]; ℱv is χ(|σ|) times the boundary value from
Im σ > 0 of a function holomorphic inside 𝒞_0 with at most a pole at 0 ([[sec:iii-h1-5]]), a distribution supported in
a compact subset of (−c, c), c ≤ ½, as [[lem:iii-i2-3-1]] asks; and ℱ(∂_(t_*)v) is [[eq:iii-i2-5-7]], whose tf-weight
α̃_K + 2 − ε is at least β_ι = γ_+ + 1 (as γ_+ < α̃_K + 1 − ε) and whose zf-weight is β_K, with no zf index term as
β_K < 0. So

    ∂_(t_*)u_sing ∈ H^(∞,3/2,γ_++1−ε,α̃_K−1)_b(M′).

([Hin26] takes β_ι = α̃_K + 1 − ε, from [Hin26, (11.49)] and the minimum min(α̃_+ + 1, α̃_K + 1 − ε) in [Hin26,
(11.50)]; here the tf-weight of [[eq:iii-i2-5-7]] exceeds the a priori bound [[eq:iii-i2-5-8]], which sets β_ι.)

*Second integration.* [[lem:iii-i2-2-1]] (1) for u_sing with (β_I, β_ι, β_K) := (γ_+ − ε, γ_+ − ε, α̃_K − 2) and
ℰ_K = ∅ (α̃_K − 2 ≠ 0): the hypotheses are [[eq:iii-i2-5-8]] and the last display (3/2 ≥ γ_+ − ε). So

    u_sing ∈ H^(∞,γ_+−ε,γ_+−2ε,α̃_K−2)_b(M′),                                                          {#eq:iii-i2-5-9}

the term (0, 0) at K lying above the weight α̃_K − 2 < 0. With [[eq:iii-i2-5-6]] and the bound for u_hi,
u^♭ ∈ H^(∞,γ_+−ε,γ_+−2ε,α̃_K−2)_b(Ω_*)^(•,−), and u = u^♭ + u_I has the same ι⁺- and K⁺-weights.

*Step 3: the expansion at 𝓘⁺.* [[prop:iii-i1-2-1]] with ℓ_+ := γ_+ − 2ε (below min Re ℰ_+ and a_+ + min Re ℰ_+, below
ℓ_I, and below min Re ℰ_I^tot = 3/2; f has the ι⁺-weight α_+ + 2 > ℓ_+ + 2; the a priori 𝓘⁺-weight is γ_+ − ε) gives
[[eq:iii-i2-5-3]] with (α̃_K, γ_+ − 2ε) in place of (α′_K, β′_+), again in the range of the iteration by
[[eq:iii-i2-5-4]].

*Conclusion.* Each step raises α′_K by min(a_K − 2, α_K − α′_K), a_K > 2, so finitely many steps reach α′_K = α_K,
with the ι⁺-weight γ_+ − 2ε; given β_+ as in the proposition, choose γ_+ > β_+ + 2ε in [[eq:iii-i2-5-4]]. This is
[[eq:iii-i2-5-2]]. Each step loses finitely many b-derivatives, and the spaces are H^∞ in the sense of
[[sec:iii-i2-4]]: at each order k, with the c of that order.

*Continuity.* The maps of the scheme are linear in f and u; u_I, u_hi, u_reg and u_sing depend on f′ only, through maps
bounded between the spaces above (the construction of [[prop:iii-i1-3-1]] by [[lem:iii-a-1-2]], and
[[lem:iii-i2-2-1]], [[lem:iii-i2-3-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]] with [[prop:ii-g1-3-3]] (1) and
[[prop:ii-g1-3-5]] (1), each with bounds). (S, h) enters in three ways. Through L − L_b, whose coefficients in
[[eq:iii-i-3-6]] depend continuously on (S, h) ([[prop:iii-i-3-4]] and the expansion of g⁻¹ after it), with the bound of
[[eq:iii-i-4-2]] uniform for (S, h) small. Through the start, which [[thm:iii-i-5-3]] gives continuously in (S, h) at
weights lowered by ς. And through [[prop:iii-i1-2-1]] in Steps 0 and 3, whose proof is constructive ([[lem:iii-a-1-2]]
and [[lem:iii-a-3-2]] with their bounds, the products by [[lem:iii-c-2-1]] with the coefficient norms of the operator),
so that its bound depends on L only through coefficient norms, which [[prop:iii-i-3-4]] bounds locally uniformly in
(S, h). (A closed graph argument would give a bound for each fixed L only.) So every constant of the scheme, and the
bound of u in [[eq:iii-i2-5-2]] by f, is locally uniform in (S, h). For two parameters, L(u − u′) = (L′ − L)u′, with u′
bounded in [[eq:iii-i2-5-2]] uniformly and (L′ − L)u′ small in the space of the right side of Step 1 at the lowered
weights; the bounds of the scheme for the difference give the claim, for ς below the room in [[eq:iii-i2-5-4]]. ∎

In dimension 4 + 1 the window needs no relaxation. [Hin26] relaxes the ι⁺-weight to α̃_+ ∈ (α̃_K, α̃_K + ε_ind) to stay
in the indicial gap at zero energy. Here the gap of L̂_b(0) contains (0, 1] ([[prop:iii-f1-2-3]] (a)), the window (0, 1)
of [[eq:iii-h-1-1]] lies inside it, and γ_+ − α̃_K ∈ (0, 1) throughout [[eq:iii-i2-5-4]].
