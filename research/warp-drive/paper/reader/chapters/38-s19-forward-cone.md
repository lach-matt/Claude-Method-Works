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

    g_0 − g_(b₀) ∈ H^(∞,(⟨(3,0)⟩_0,∞),((2,0),∞),(0,0))_b(Ω_*),        g_0 = g_b near K⁺,                     {#eq:iii-i-3-5}

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
