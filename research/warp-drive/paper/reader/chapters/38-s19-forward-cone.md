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
the slot π̸_0 only; π_11 u has no term at 3/2; and formal solutions remove one exceptional term,
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
[[def:iii-c-1-2]], in the splitting [[eq:iii-c-1-6]]: slots 1–3 form π_C, and slots 4, 5, 6, 7 are π_01, π_1/, π̸_0
and π_11. We write

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

and let ℰ^C_I satisfy [[def:iii-c-3-1]] (2)–(3), with ℰ^tot_I, ℰ_(I,01), ℰ_(I,1/), ℰ̸_(I,0), ℰ_(I,11) and ℱ_(I,11)
as there ([[eq:iii-c-3-1]]–[[eq:iii-c-3-2]], [[eq:iii-c-5-1]]). Let ℓ_I, ℓ_+, ℓ_K ∈ ℝ.

(1) For k ≥ 5, H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b(Ω_*) is the space of real symmetric 2-tensors h whose slot
components near 𝓘⁺ lie in H^(k,(ℰ,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b with ℰ = ℰ^C_I for π_C, ℰ_(I,01) for π_01, ℰ_(I,1/) for π_1/,
ℰ̸_(I,0) for π̸_0 and ℰ_(I,11) for π_11 ([[eq:iii-c-3-3]] with ι⁺ in place of I⁰).

(2) For k ≥ 3, H^(k,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2),ℓ_K)_b(Ω_*) is the space of f with π_C f, π_01 f, π_1/ f,
π̸_0 f in (ℰ^C_I + 1, ℓ_I + 1) and π_11 f in (ℱ_(I,11), ℓ_I + 1) at 𝓘⁺, all in (ℰ_+ + 2, ℓ_+ + 2) at ι⁺, and of
weight ℓ_K at K⁺ ([[def:iii-c-5-1]]).

(3) H^(k,(⟨(3,0)⟩_0,ℓ_I),(ℰ_+,ℓ_+),ℰ_K)_b(Ω_*) is the class of [[def:iii-c-3-3]] at 𝓘⁺ ((3, 0) for every slot but
π_11, (2, 0) for π_11), with (ℰ_+, ℓ_+) at ι⁺ and the index set ℰ_K at K⁺.

[Hin26] has (1, 0) ∈ ℰ_+ and min Re ℰ_+ ≥ 1: (1, 0) is the ι⁺-order of its background differences, which in dimension
4 + 1 is 2 ([[lem:iii-i-3-6]]). The condition min Re ℰ_+ > 1 is what [[lem:iii-i-2-2]] and [[prop:iii-i-4-1]] use.
Later chapters may raise min Re ℰ_+; the exponent 3/2 + (1 − e_Υ)γ_Υ that formal solutions at 𝓘⁺ produce
([[prop:iii-i1-3-1]]) lies above it.

*The class of perturbations.* With parameters a_I > 3/2, a_+ > 1, a_K > 2, put

    𝒳^k := H^(k,(⟨ℰ^C_I⟩,a_I),(ℰ_+,a_+),a_K)_b(Ω_*; S²T*).                                              {#eq:iii-i-1-4}

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
≥ 3 + 2γ_Υ; π̸_0 h of order 3 ([[def:iii-i-1-1]] (1), [[eq:iii-c-3-2]]). The coefficients of h in the frame
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
U⁺ ∩ {ρ_I ≤ 1}, g_0 − η ∈ ρ_+²ρ_I²C^∞ and π(g_0 − η) ∈ ρ_+²ρ_I³C^∞ for π ≠ π_11 ([[def:iii-c-3-4]] with ρ_+ for ρ_0).

**Proposition {#prop:iii-i-3-3}** (The leading part at 𝓘⁺; [Hin26, Proposition 11.6 (1)] in dimension 4 + 1.) Let
g_1, g_0 ∈ 𝒢⁺, k ≥ 5, and h ∈ 𝒳^k with small H^(3,(1,0,0))_b-norm. Then g := g_1 + h satisfies, on U⁺ ∩ {ρ_I ≤ 1}, in
the splitting [[eq:iii-c-1-6]],

    L^(g,g_0) ≡ ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − Ā)
        mod (ρ_+²ρ_I²C^∞ + H^(k−2,(ℰ^tot_I,a_I),(ℰ_++2,a_++2))_b) Diff²_b.                              {#eq:iii-i-3-4}

For h ∈ H^(k,(⟨(3,0)⟩_0,a_I),(ℰ_+,a_+),·)_b the same holds with (2, 0) in place of ℰ^tot_I.

*Proof.* This is the proof of [[prop:iii-c-4-4]] on U⁺, with [[lem:iii-i-3-1]]–[[lem:iii-i-3-2]] in place of
[[lem:iii-c-1-1]] and [[lem:iii-c-4-1]], and with the expansion of g⁻¹ after [[prop:iii-i-3-4]] in place of the Neumann
series used there (whose convergence needs smallness in H^k). The change of frame ([[lem:iii-c-1-3]], with
ρ² = ρ_+²ρ_I²) turns S̄ into Ā ([[lem:iii-c-4-2]]). The backgrounds (g_1, g_0) differ from (g_b, g_b) by
ρ_+²ρ_I²C^∞, which with the two factors ρ_+ from the derivatives gives ρ_+⁴ρ_I²C^∞ Diff²_b. The perturbation, counted
as in [[lem:iii-c-4-3]] with Cartesian derivatives in ρ_+𝒱_b ([[lem:iii-i-3-1]]) and c_C, c_Υ ∈ ρ_+ρ_I C^∞, gives
ρ_+² times H^(k−2)-functions of the index sets of h: ℰ^tot_I at 𝓘⁺ ([[lem:iii-c-3-2]] (b)–(c)), and ℰ_+ at ι⁺
(jℰ_+ ⊂ ℰ_+ for the Taylor terms of g⁻¹, [[lem:iii-c-2-1]] with the weights (a_I, a_+)). ∎

So, as at I⁰ ∩ 𝓘⁺, the leading part has the constant lower-triangular Ā and no h-dependent term. The terms A^h − A_0
and B^h of [Hin26] are part of the error, of 𝓘⁺-order 3/2 against the leading order 1 ([[prop:iii-c-4-4]],
[[rem:iii-c-4-5]]). The edge-b form [Hin26, (11.17b)] is not needed: [[cor:iii-i-5-2]] uses [[eq:iii-i-3-7]] instead.

**Proposition {#prop:iii-i-3-4}** (The difference from L_b; [Hin26, Proposition 11.6 (2)] in dimension 4 + 1.) Let
g_0 = g_(b₀,b,−S), or more generally g_0 ∈ 𝒢⁺ with ([Hin26, (11.15a)–(11.15b)])

    g_0 − g_(b₀) ∈ H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),(0,0))_b(Ω_*),      g_0 = g_b near K⁺,          {#eq:iii-i-3-5}

let h ∈ 𝒳^k, k ≥ 5, with small H^(3,(1,0,0))_b-norm, and g := g_(b₀,b,−S) + h ([Hin26, (11.16)]). Then on Ω_*

    L^(g,g_0) − L_b ∈ H^(k−2,(ℰ^tot_I,a_I),(ℰ_++2,a_++2),a_K)_b Diff²_b(Ω_*; S²T*),                      {#eq:iii-i-3-6}

    2L^(g,g_0) − 2L_b ∈ x_I²ρ_+² H^(k−2,(2ℓ_I,ℓ_+,ℓ_K))_b Diff²_(e3b)(Ω_*; S²T*),                       {#eq:iii-i-3-7}

for ℓ_I, ℓ_+, ℓ_K as in [[eq:iii-i-2-2]], the latter with norm bounded by C(|b − b₀| + |S| + ‖h‖_(𝒳^k)), C depending
on k and on an upper bound for ‖h‖_(𝒳^k).

[Hin26, (11.18a)–(11.18b)] carry in addition the term χ_Iρ_Iρ_+²((A^h − A_0)(ρ_I∂_(ρ_I) − ρ_+∂_(ρ_+)) + ρ_+⁻¹B^h),
which contains a term of leading order at 𝓘⁺; in dimension 4 + 1 it is part of the error.

*Proof.* Write g − g_b = (g_(b₀,b,−S) − g_b) + h, and g_0 − g_b. By [[lem:iii-i-3-6]] below, g_(b₀,b,−S) − g_b is
supported where χ_K < 1, so away from K⁺, and lies in H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),∞)_b ⊂ 𝒳^∞ ([[def:iii-c-3-3]] and
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
g_(b₀,b,−S) − g_(b₀,b,0) = (1 − χ_K)(φ_(−S)^* g_(b₀) − g_(b₀)) ∈ H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),∞)_b
([[lem:iii-i-3-6]]). This is where the condition (2, 0) ∈ ℰ_+ of [[eq:iii-i-1-3]] is used.

**Lemma {#lem:iii-i-3-6}** (The background differences.) For |b − b₀| and |S| small, g_(b₀,b,−S) satisfies
[[eq:iii-i-3-5]] and lies in 𝒢⁺; g_(b₀,b,−S) − g_b is supported in {χ_K < 1} and lies in
H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),∞)_b(Ω_*), with seminorms O(|b − b₀| + |S|).

*Proof.* We have g_(b₀,b,−S) − g_b = (1 − χ_K)(φ_(−S)^* g_(b₀) − g_(b₀)) + (1 − χ_K)(g_(b₀) − g_b). On
supp(1 − χ_K) ∩ Ω_*, χ_IVP = 1 and the flow of V(S) is the boost: this is the first alternative of [[lem:iii-b-5-2]],
with supp χ^♭_K ⊂ χ_K⁻¹(1); on its second alternative, {|x| < 6R₁}, the difference is smooth and supported in a
compact set away from the faces at infinity, as that alternative of [[lem:iii-b-5-2]] states, hence in the class. So
by [[eq:iii-b-5-3]], φ_(−S)^* g_(b₀) − g_(b₀) = |x|⁻²h_(−S)(ω)(dx¹)² + ρ_0²ρ_I³ρ_+² C^∞ with h_(−S) = O(|S|); and by
[[prop:iii-b-3-6]], g_(b₀) − g_b = (m₀ − m)|x|⁻²(dx¹)² + O(|b − b₀|)|x|⁻³C^∞ on {|x| ≥ 3R₁}. Near 𝓘⁺,
|x|⁻²(dx¹)² is the slot π_11 at ρ_I-order 2 and ι⁺-order 2, and |x|⁻³ is of orders 3; in the interior of ι⁺,
|x|⁻² ∈ ρ_+²C^∞. This is the class stated, as 1 − χ_K is smooth on M. For [[eq:iii-i-3-5]]: g_(b₀,b,−S) − g_(b₀) =
(g_(b₀,b,−S) − g_b) + (g_b − g_(b₀)), the last term being independent of χ_K, smooth at K⁺ and of the same classes; and
g_(b₀,b,−S) = g_b on χ_K⁻¹(1), a neighbourhood of K⁺. 𝒢⁺: near 𝓘⁺ ∩ ι⁺, g_(b₀,b,−S) = φ_(−S)^* g_(b₀), and
g_(b₀) − η = m₀|x|⁻²(dx¹)² has the slot π_11 only. ∎

### Forward mapping {#sec:iii-i-4}

This section is [Hin26, Proposition 11.8 and Corollary 11.9] in dimension 4 + 1.

**Proposition {#prop:iii-i-4-1}** (Forward mapping; [Hin26, Proposition 11.8] in dimension 4 + 1.) Let g_0 ∈ 𝒢⁺
satisfy [[eq:iii-i-3-5]], let h and g be as in [[prop:iii-i-3-4]], and let 3/2 < ℓ_I < a_I + ½,
0 < ℓ_+ < a_+ + min Re ℰ_+, ℓ_K ∈ ℝ and k ≥ 5. Then

    L^(g,g_0) : H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b(Ω_*) → H^(k−2,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(ℰ_++2,ℓ_++2),ℓ_K)_b(Ω_*),
                                                                                                  {#eq:iii-i-4-1}

and, if moreover ℓ_+ ≤ max(a_+, min Re ℰ_+), then for every ε > 0

    L^(g,g_0) − L_b : H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,ℓ_+),ℓ_K)_b
                          → H^(k−2,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(2ℰ_++2,ℓ_++2+m_+−ε),ℓ_K+a_K)_b,
    m_+ := min(a_+, min Re ℰ_+).                                                                   {#eq:iii-i-4-2}

[Hin26, (11.19)] has ℓ_+ + 3 − ε (m_+ = 1) and ℓ_K + 2 + ε_K (a_K = 2 + ε_K). The upper bounds on ℓ_I and ℓ_+ are
those of the products ([[lem:iii-c-2-1]]): a coefficient of the error with no expansion beyond its 𝓘⁺-weight a_I,
acting on the radiation term ρ_I^(3/2) of π̸_0 u, gives ρ_I^(a_I+3/2) times a function with no expansion, and likewise
at ι⁺. [Hin26, Proposition 11.8] is stated for all weights, but its products need the same restrictions (in dimension
3 + 1, ℓ_I < a_I and ℓ_+ < a_+ + min Re ℰ_+, and ℓ_+ ≤ max(a_+, min Re ℰ_+) for [Hin26, (11.19)]).
[[cor:iii-i-4-2]] (ℓ = a) lies inside this range, and the later chapters keep their weights in it.

*Proof.* [[eq:iii-i-4-1]]. Near 𝓘⁺ (on U⁺ ∩ {ρ_I ≤ 1}) this is the proof of [[prop:iii-c-5-2]], with
[[prop:iii-i-3-3]] in place of [[prop:iii-c-4-4]], ι⁺ in place of I⁰ and ℰ_+ in place of ℰ_0. The leading part
ρ_+²ρ_I(X_+ − X_I)(X_I − 3/2 − Ā) has the slot-by-slot effect computed there: X_+ − X_I preserves index sets,
X_I − 3/2 − Ā_jj annihilates the exceptional terms, and the couplings of Ā act as there; the factor ρ_+²ρ_I shifts the
data by 2 at ι⁺ and by 1 at 𝓘⁺. The C^∞ error gives ℰ^tot_I + 2 ⊂ ℰ^C_I + 1 and ℰ_+ + 2. The perturbation error gives,
by [[lem:iii-c-2-1]], 2ℰ^tot_I ⊂ ℰ^C_I + 1 at the weight ℓ_I + 1 and 2ℰ_+ + 2 ⊂ ℰ_+ + 2 at the weight ℓ_+ + 2. The
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
                 ∈ H^(∞,(⟨ℰ^C_I+1⟩′,a_I+1),(ℰ_++2,a_++2),a_K)_b(Ω_*).                                   {#eq:iii-i-4-3}

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
