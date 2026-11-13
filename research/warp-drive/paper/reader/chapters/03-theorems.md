## The theorems {#ch:theorems}

This chapter states the four theorems and the three propositions that complete the first, shows how the first follows
from the approximant, the data and the uniform existence theorem, and lists the further results with the chapters
that prove them. The notation is that of [[ch:setting]]. The order of the approximant is K, and the
Kretschmann scalar is 𝒦.

### The construction on the domain {#sec:main-statement}

**Theorem {#thm:main}** (the five-dimensional counterpart). Let l5 > 0, μ0 ≥ √72 l5², A > 0 and
env ∈ C_c^∞([v_start, v_end]), and let g0 be the Vaidya metric [[eq:background]] with
μ(v) = μ0 + (2/9) A² ∫_(−∞)^v env². Fix T > 0, τ0 with v_start − τ0 > √μ0 + 1, and K ≥ 6. There are λ0 > 0 and
C, depending on (l5, μ0, A, env, T, τ0, K) and the inner radius a of Ω, and not on λ, such that for every
λ ∈ (0, λ0] there is a smooth Lorentzian metric g_λ on Ω ⊃ D_T ∩ {τ ≥ τ0} with:

1. *Vacuum and symmetry.* Ric(g_λ) = 0 on Ω, and g_λ is invariant under the T² action and both reflections.
2. *Data.* On Σ_τ0, the Cauchy data of g_λ satisfy the vacuum constraints exactly, equal the data of the seed
   (five-dimensional Schwarzschild–Tangherlini of mass μ0) on r < v_start − τ0, and differ from those of an
   approximate solution g_app ([[thm:approximant]]) by O(λ^K) in the λ-scaled data norm: with w := g_λ − g_app
   and k = 6,

       Data(w) := ‖w‖ + Σ_(1≤j≤k+1) λ^(j−1) ‖∂_x^j w‖ + Σ_(j≤k) λ^j ‖∂_x^j ∂_τ w‖ ≤ C λ^K   on Σ_τ0;

   the leading oscillation of g_app is the waves of [[sec:waves]].
3. *The remainder.* g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω, where
   g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j], N = K + 3, with smooth profiles g_j(X, θ), 2π-periodic in θ, evaluated
   at θ = v/λ.
4. *Convergence.* |g_λ − g0| ≤ C λ and |∂g_λ| ≤ C on Ω; ∂g_λ − ∂g0 = dv ⊗ [∂_θ g1] + O(λ), so ∂g_λ → ∂g0 weakly
   in L²(Ω), and not strongly wherever env ≠ 0: the phase mean of ∂_θ g1 is 0 and that of its g0-norm squared is
   (4/3) A² env² r⁻³. The limit g0 satisfies Ric(g0) = (3 μ'/(2 r³)) dv ⊗ dv with [[eq:mu-rate]]: it is not vacuum
   but Einstein–null dust with one family.
5. *Gauge and uniqueness.* D(g_λ) = 0 on Ω, and g_λ is the only C² solution g of Ric^H(g) = 0 on Ω with the data
   of g_λ on Σ_τ0 and |g − g0| ≤ ε1 on Ω, ε1 the number fixed in [[sec:profiles]].
6. *The spheres' horizon.* If μ0 > √72 l5² and λ ≤ λ_H ([[prop:one-zero]]), the outgoing expansion of the spheres
   {v, r = const} has at most one zero on each column (v and the angles fixed), exactly one within C λ of √μ(v) on the
   columns that reach across it, the spheres with r ≤ √μ(v) − C λ being trapped and those with r ≥ √μ(v) + C λ
   untrapped: no inner zero, and the zero converges to √μ at O(λ) ([[prop:one-zero]]).
7. *Mean mass.* For every sphere S_(v,r) in D_T ∩ {τ ≥ τ0}, its Hawking mass satisfies |M[S](g_λ) − μ(v)| ≤ C λ²
   before and after the shell (v ≤ v_start or v ≥ v_end), and ≤ C λ within it ([[prop:mean-mass]]).

The construction fixes some constants explicitly: the order of the energy is k = 6, the approximant used has N = K + 3
stages, λ ≤ λ_Ω := min(1, δ0)/10 with δ0 = q0 − a as in [[sec:domain]] (a condition the construction imposes, not a
bound below which the theorem holds: that is λ0), and the data are solved in H^s(S³) with s > 3/2 + 4 ([[ch:data]]). λ0
and C are not evaluated; [[prop:lambda0]] bounds λ0 above at a numerical point. Every constant of the approximant's own
estimates is independent of λ, because its profiles are ([[thm:approximant]]). The waves are high-frequency on all of
D_T once λ < l5/10: on D_T, x_K = l5² √𝒦 ≤ 1, so the curvature length 𝒦^(−1/4) is at least l5, and λ 𝒦^(1/4) ≤
λ/l5 < 1/10.

**Proposition {#prop:boundary-spacelike}** (the boundary). On x_K = 1, with Φ := r − r_q(v),

    g0⁻¹(dΦ, dΦ) = 1 − √(μ/(√72 l5²)) − r_q μ'/(2 μ),                                             {#eq:boundary-margin}

so, μ being at least μ0 ≥ √72 l5² throughout, the boundary is spacelike for g0 wherever μ > √72 l5² or μ' > 0, and
every future causal curve that meets it leaves D_T there and does not return. If μ0 > √72 l5² the margin is uniform,
g0⁻¹(dΦ, dΦ) ≤ −δ_b with δ_b := √(μ0/(√72 l5²)) − 1 > 0, and for g_λ the margin is −δ_b + C λ ≤ −δ_b/2 once
C λ ≤ δ_b/2. If
μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the shell
starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ ([[ch:equality-layer]]), and inside that
layer, for λ small, every column has points where it is timelike for g_λ, so the no-return property stated above for
μ0 > √72 l5² fails at equality ([[thm:layer]], [[cor:layer]], [[thm:very-edge]]).

The proof is in [[ch:horizon-mass]].

**Proposition {#prop:one-zero}** (one zero per column of the spheres' outgoing expansion). Let μ0 ≥ √72 l5²,
K ≥ 6, and let θ⁺_λ(v, r, x̂) be the outgoing null expansion, for g_λ, of the sphere
S_(v,r) := {τ = v − r, |x| = r} at its point x̂ ∈ S³. There are λ_H ∈ (0, λ0] and C, δ1, δ2 > 0 such that for
λ ≤ λ_H: on every column (v and x̂ fixed, r varying, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero, positive
above it and negative below; if μ0 > √72 l5², on the columns with √μ(v) ≤ v − τ0 − δ1 it has exactly one,
R_λ(v, x̂), with |R_λ − √μ(v)| ≤ C λ, and the spheres with r ≤ √μ(v) − C λ are trapped, those with
r ≥ √μ(v) + C λ untrapped (C twice the constant that places the zero, so that the spheres at distance C λ are
strictly trapped); if μ0 = √72 l5², the same holds on the columns with μ(v) ≥ μ0 + δ2 and √μ(v) ≤ v − τ0 − δ1.

The proof is in [[ch:horizon-mass]]. The statement concerns the round family {v, r = const}: the per-column zero set
is not itself a marginally trapped surface.

For a 3-sphere S with future null normals n⁺, n⁻ and expansions θ⁺, θ⁻, let

    M[S](g) := R² (1 + (R²/9) ⟨Θ⟩),   R := (Area(S)/(2π²))^(1/3),   Θ := 2 θ⁺ θ⁻ / (−g(n⁺, n⁻)),     {#eq:hawking-mass}

with ⟨·⟩ the mean over S: the five-dimensional Hawking mass. Θ does not depend on the normalisation of n⁺ and n⁻.
For g0 and S = S_(v,r), Area = 2π² r³, so R = r; with n⁺ = ∂_v + (f/2) ∂_r and n⁻ = −∂_r in the form
[[eq:vr-form]], θ⁺ = 3f/(2r), θ⁻ = −3/r and g0(n⁺, n⁻) = −1 ([[prop:vaidya]] (b)), so Θ = −9f/r² and
M[S_(v,r)](g0) = r² (1 − f) = μ(v).

**Proposition {#prop:mean-mass}** (the mean mass). For K ≥ 6 and λ ≤ λ0, |M[S_(v,r)](g_λ) − μ(v)| ≤ C λ²
wherever v ≤ v_start or v ≥ v_end, and ≤ C λ for v_start < v < v_end.

The proof is in [[ch:horizon-mass]]; it rests on a quarter-turn symmetry of the two polarizations, under which the first
mean correction of the approximant is odd while the mass is invariant, so that the mass does not see it. The mean of the
mass aspect at past null infinity is a different quantity from the Hawking mass of the spheres of the domain;
[[thm:bondi-law]] treats it.

### How the first theorem follows {#sec:main-proof}

[[thm:main]] is the conjunction of three theorems: the approximant to every order ([[thm:approximant]], proved in
[[ch:approximant]]), exact data within O(λ^K) of it ([[thm:data]], proved in [[ch:data]]), and existence on Ω
with remainder estimates uniform in λ ([[thm:uniform-existence]], proved in [[ch:uniform-existence]]), together with
[[prop:one-zero]] and [[prop:mean-mass]].

**Lemma {#lem:gauge-propagation}** (the gauge propagates). Let g be a C³ Lorentzian metric on Ω, within ε1 of g0,
with Ric^H(g) = 0, and suppose D(g) = 0 on Σ_τ0 and the Cauchy data of g on Σ_τ0 satisfy the vacuum constraints.
Then D(g) = 0 on Ω, and g is vacuum.

*Proof.* Write C := Γ[g] − Γ[g0], ∇ for the connection of g, and D_m := g_mρ D^ρ. Since ∇̂_n D^ρ = ∇_n D^ρ −
C^ρ_nσ D^σ, the equation Ric^H(g) = 0 reads

    Ric(g)_mn = (1/2)(∇_m D_n + ∇_n D_m) + L_mn,      L_mn := −(1/2)(g_mρ C^ρ_nσ + g_nρ C^ρ_mσ) D^σ,

with L linear in D and free of its derivatives. The contracted Bianchi identity ∇^m(Ric_mn − (1/2) g_mn R) = 0, with
R = ∇_m D^m + tr L, gives

    (1/2) □_g D_n + (1/2)(∇^m ∇_n D_m − ∇_n ∇^m D_m) + ∇^m (L_mn − (1/2) g_mn tr L) = 0,

and ∇^m ∇_n D_m − ∇_n ∇^m D_m = Ric(g)_nσ D^σ. Substituting the expression for Ric(g) once more, D solves a linear
homogeneous system −(1/2) g^(ab) ∂_a ∂_b D = f, with f linear in (D, ∂D) and coefficients bounded on Ω.

On Σ_τ0, D = 0, so its derivatives tangent to Σ_τ0 vanish there, and ∇̂_b D^ρ = n_b ∂_τ D^ρ with n := dτ. Hence
Ric(g)_ab = (1/2)(n_a Y_b + n_b Y_a) there, Y_a := g_aρ ∂_τ D^ρ. With N := g⁻¹ n, the scalar curvature is
R = Y(N), and the Einstein tensor contracted with N is

    G(N, ·) = (1/2)(n(N) Y + Y(N) n) − (1/2) Y(N) n = (1/2) g⁻¹(n, n) Y.

The vacuum constraints are G(N, ·) = 0 on Σ_τ0, and g⁻¹(n, n) < 0 by [[lem:domain]] (e), so Y = 0: D and ∂_τ D vanish
on Σ_τ0. The energy inequality of [[ch:inequalities]], applied to this system on Ω, with Gronwall's lemma, gives D = 0
on Ω; then Ric(g) = 0. ∎

*Proof of [[thm:main]].* Let g_app be the approximant of [[thm:approximant]] with N = K + 3 stages and the stage data of
[[lem:stage-data]], which make its Cauchy data satisfy the constraints and D = 0 to order N − 2, and let the data on
Σ_τ0 be those of [[thm:data]], which satisfy the constraints exactly, carry D = 0, equal the seed's data on r <
v_start − τ0 and are within C λ^K of g_app's in the norm of item 2. [[thm:uniform-existence]] gives, for λ ≤ λ0, the
solution g_λ of Ric^H(g) = 0 on Ω with these data, unique among C² solutions with these data and |g − g0| ≤ ε1 on Ω,
together with the bounds of items 3 and 4 on w = g_λ − g_app and |g_λ − g0| ≤ C λ, |∂g_λ| ≤ C. Taking λ0 so small that C
λ0 ≤ ε1, [[lem:gauge-propagation]] gives D(g_λ) = 0 and Ric(g_λ) = 0. By [[lem:domain]] (f), D_T ∩ {τ ≥ τ0} lies in Ω.

Symmetry. Let ι be an element of G = O(2) × O(2), acting on x by an orthogonal matrix and fixing τ. It preserves r,
v, η and dv, hence g0, Ω and Σ_τ0. Ric^H and D are built from g and g0 alone, so ι*g_λ solves Ric^H(ι*g_λ) = 0; its
data are ι* of the data of [[thm:data]], which are invariant under G ([[ch:data]]); and ι acts on Cartesian arrays by
an orthogonal matrix, which preserves the Euclidean operator norm, so |ι*g_λ − g0| = |g_λ − g0| ≤ ε1. By the
uniqueness of item 5, ι*g_λ = g_λ. This is item 1.

Weak convergence. For a profile f and a test function u ∈ C_c^∞ in the interior of Ω, write f = Σ_n f_n(X) e^(inθ); the
coefficients decay faster than any power of n, uniformly with their X-derivatives. Since ∂_τ v = 1, for n ≠ 0,

    ∫ u f_n e^(inv/λ) = (λ/(in)) ∫ u f_n ∂_τ e^(inv/λ) = −(λ/(in)) ∫ ∂_τ(u f_n) e^(inv/λ) = O(λ/|n|),

so ∫ u [f] → ∫ u ⟨f⟩, and, [f] being bounded, [f] → ⟨f⟩ weakly in L²(Ω). By [[thm:approximant]] the oscillating part of
g1 is W_TT at a shifted phase plus a term χ dv ⊗ dv, so [[prop:limit]] gives ⟨∂_θ g1⟩ = 0 and ⟨|∂_θ g1|²_(g0)⟩ = (4/3)
A² env² r⁻³. Hence dv ⊗ [∂_θ g1] → 0 weakly, which with item 3 is the weak convergence of item 4. Applying the same
limit to the profile |dv ⊗ ∂_θ g1|², the Euclidean square of the array, shows that ‖dv ⊗ [∂_θ g1]‖²_(L²(U)) tends to ∫_U
⟨|dv ⊗ ∂_θ g1|²⟩ for every open U ⊂ Ω, which is positive where env ≠ 0, because ∂_θ g1 is not zero there: the mean of
its g0-norm squared is positive. So the convergence is not strong wherever env ≠ 0. The formula for Ric(g0) is
[[prop:vaidya]] (a).

Items 2, 3 and 5 are those of [[thm:data]] and [[thm:uniform-existence]]; items 6 and 7 are [[prop:one-zero]] and
[[prop:mean-mass]]. ∎

### The construction from past null infinity {#sec:past-statement}

**Theorem {#thm:past-construction}** (the construction from past null infinity). Let the waves at past null infinity
be the free data [F], [G] of [[sec:waves]], on the background of [[thm:main]]. For every K ≥ 6 there is λ_P > 0
such that for 0 < λ ≤ λ_P there is a smooth vacuum metric g_λ, in the wave-map gauge relative to g0, on Ω together
with a past domain P: the region τ ≤ τ0, r ≥ a, below the outer boundary v + (1/2)(1 + τ0 − τ)^(−1/4) = V_P, where
V_P := V + 1 + (τ_end − τ0) + 1/2; this boundary is spacelike and meets Σ_τ0 where the outer boundary of Ω does, so
that P and Ω share the slice Σ_τ0 ([[ch:past-construction]]). It satisfies:

1. g_λ = g0 for v ≤ v_start: before the shell, the black hole exactly;
2. its radiation field at past null infinity is the prescribed one: at every fixed v < V_P and x̂,
   r^(3/2)(g_λ − g0 − λ[W_TT]) → 0 as r → ∞, at every λ;
3. on P, |g_λ − g_app| ≤ C λ^(K−3) t^(−2), with t = 1 + τ0 − τ and g_app the approximant built from past null
   infinity ([[thm:past-approximant]]);
4. on Ω, the conclusions of [[thm:uniform-existence]] hold (items 1 and 3–5 of [[thm:main]]), with the data on Σ_τ0
   now the trace of g_λ itself; and items 6–7 of [[thm:main]] hold for these solutions too ([[prop:past-items]]);
5. g_λ is T² × Z2 × Z2-invariant, and unique among solutions of Ric^H(g) = 0 on P with item 1 whose difference from
   g_app is, with its first derivatives, at most ε_U t^(−3/2) for a small ε_U > 0 (within the margin of the past
   domain fixed in [[ch:past-construction]]), and whose energy on the slices tends to zero at past null infinity.

So the counterpart holds with the waves' own free data at past null infinity, and the constraints need not be solved
on this route ([[thm:data]] is the other route).

The proof is in [[ch:past-construction]]; it runs as follows. Before the shell the solution is the black hole: the
region v ≤ v_start is a past set for the black hole's cones, and the data there are the black hole's. Near past null
infinity every stage of the approximant is solved with nothing coming in. Each stage has an explicit leading term in r
and a remainder half a power of r better, and no forcing term of the stages falls off like r^(−5/2), the rate that would
produce a logarithm. So the residual decays like r^(−3), and the remainder can be estimated with the rotations as
commutators, which gain t^(−3/2) in Sobolev's inequality. The past is split at t = λ^(−2). Before the split, the one
large coefficient of the linearised problem ([[ch:uniform-existence]]) integrates in time to a constant, and no
decomposition is needed. After it, the decomposition of [[ch:uniform-existence]] runs over an interval of length
λ^(−2). There the transport of its auxiliary field loses a logarithm per unit of log t, which weights (T/t)^β0 absorb
at a cost λ^(−2β0); β0 does not depend on the order of the approximant, so a higher order pays it. The mollifier's
commutator with the wave operator is, apart from decaying terms, an exact derivative along the generators, and is
absorbed into the auxiliary field. The limit is vacuum because the gauge field of the approximant decays at past null
infinity, so its energy tends to zero there and the gauge field vanishes.

### The Bondi mass law at past null infinity {#sec:bondi-statement}

**Theorem {#thm:bondi-law}** (the Bondi mass at past null infinity). Let g_λ be the metric of
[[thm:past-construction]], 0 < λ ≤ λ_P. Near past null infinity it admits Bondi coordinates
(v_B, r_B, ϑ_B, φ1, φ2) — v_B null with v_B − v → 0 at past null infinity, ϑ_B constant along the generators, r_B the
areal radius — in which

    g_λ = −e^(2β) W dv_B² + 2 e^(2β) dv_B dr_B + r_B² [e^(−2(P1+P2)) (dϑ_B − U dv_B)² + cos²ϑ_B e^(2P1) dφ1²
          + sin²ϑ_B e^(2P2) dφ2²],                                                                  {#eq:bondi-form}

with P1, P2, β, U, W − 1 expanded in r_B^(−1/2) to order r_B^(−3) with o(r_B^(−3)) remainders, coefficients smooth in
(v_B, ϑ_B) and, for v_B ≤ v_start, those of g0: all zero except W − 1 = −μ0 r_B^(−2). In it:

1. P_i = r_B^(−3/2) p_i + O(r_B^(−5/2)), with p1 = (2c² G − s² F)/3 and p2 = (2s² F − c² G)/3 as in [[eq:waves]],
   c = cos ϑ_B, s = sin ϑ_B and the free data F, G of [[sec:waves]] at phase v_B/λ (the radiation field of
   [[thm:past-construction]], item 2); the r_B^(−2) coefficients vanish;
2. W = 1 + r_B^(−3/2) V1 − r_B^(−2) M + O(r_B^(−5/2)), with V1 a divergence on S³ and the mass aspect M obeying,
   pointwise, the five-dimensional Bondi law of [TTS09] (28), time-reversed,

       ∂_v M = (4/3)((∂_v p1)² + ∂_v p1 ∂_v p2 + (∂_v p2)²),                                            {#eq:bondi-law}

   with M = μ0 for v_B ≤ v_start;
3. the Bondi mass μ_B(v) := ⟨M(v, ·)⟩, the mean over S³, therefore obeys, exactly,

       μ_B' = (2/9) A² [env² + λ² env'² + (1 − π/2)(−(1/2)(env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ))],
                                                                                                    {#eq:flux-mean}

   the sphere mean of the flux of the radiation field: μ_B is μ(v) + O(λ) while the shell passes, and
   μ(v_end) + (2/9) λ² A² ∫ env'² + O(λ³) after it;
4. the Hawking mass M[S] ([[eq:hawking-mass]]) of the Bondi spheres S = {v_B, r_B = const} tends to μ_B(v_B) as
   r_B → ∞.

This is the mean mass at past null infinity, the sphere mean of the Bondi mass aspect.

The proof is in [[ch:bondi]]; it runs as follows. At fixed λ the far region of [[thm:past-construction]] is a
neighbourhood of past null infinity, and there the remainder g_λ − g_app solves a wave equation whose forcing decays
like r^(−3): subtracting its leading term, which is explicit, and estimating the rest with the energy of that far region
gains half a power of r at each step, so g_λ − g0 has an asymptotic expansion in r^(−1/2) to any order, with the
radiation field as its leading term ([[lem:every-order-fixed]], [[prop:bondi-hierarchy]]). The derivatives along the
ingoing generators of the remainders gain a full order, because the wave equation is a transport along the outgoing
generators for them, and those generators reach the seed region, where everything vanishes, after a bounded parameter
length. The Bondi coordinates are then built from the null geodesics of g_λ asymptotic to the ingoing generators of the
background, in the manner of the eikonal function of [HL21] at future null infinity: v_B is constant on the null
hypersurfaces they sweep, and its eikonal equation, a transport along those generators with a forcing term that decays
like r^(−2) because the first-order wave is transverse to them, gives its expansion; the angular coordinates are the
generators' asymptotic angles, and the areal radius is algebraic. In the Bondi form the vacuum equations are a hierarchy
in r_B^(−1/2), the one of [TTS09] in five dimensions, solved in the class with every coefficient from the first order
general: the radial equations kill every coefficient below the waves' and fix β, U and V1, the traceless angular
equation at order r^(−1) makes the r_B^(−2) coefficients of P constant in v, which the seed sets to zero, and R_vv at
order r^(−3) is [[eq:bondi-law]] plus a divergence that vanishes with them. The mass law integrates from the seed; its
sphere mean is [[eq:flux-mean]].

### Settling to Schwarzschild–Tangherlini {#sec:settling-statement}

The domain of [[thm:main]] ends at the time T after the shell. Settling for all later times concerns the exterior of
the black hole, the nonlinear stability theory of five-dimensional Schwarzschild–Tangherlini set up in
[[part:stability]] to [[part:stability-nonlinear]]: Hintz's initial surface, his data class, the time function t*,
the exterior and its spatially compact subsets, the slowly rotating Myers–Perry black holes [MP86], and the parameters
named below are defined there.

**Theorem {#thm:settling}** (settling). Fix ℓ0 ∈ (3, 4); let ε_K be the decay parameter of the stability theory, with
0 < ε_K < ε_+ < min(δ♯, ε_ind, ℓ_I − 3, 1/4) for some ℓ_I ∈ (3, ℓ0), δ♯ = (1 − e_Υ) γ_Υ and ε_ind the index distance
([[eq:iii-i9-1-1]], [[eq:iii-f1-2-2]]), such that no parameter exponent z at timelike infinity (a discrete set fixed
before these constants) has real part in (3, 3 + ε_+] (the condition (G⁺), [[def:iii-j-g-plus]]), and none has real part
in (2, 2 + ε_K] ∪ (3, 3 + ε_K], nor z + d_c0, z + d_c1 in (2, 2 + ε_K], d_c0, d_c1 ∈ (0, 1) being the offsets of the two
class roots ([[def:iii-i9-gap]]) (the gap (G), [[def:iii-i10-1-3]]; [[ch:s27]] collects these conditions with the other
choices of parameters); and fix ε < ε_K. Let g_λ be the solutions of [[thm:main]], with A and the envelope fixed, with K
large enough and on a domain enlarged as in [[ch:after-shell]]. For every ε_m > 0 there are λ1 > 0 and δ > 0, depending
on ε_m and ε, such that for λ ≤ λ1:

(i) (in the class) the data of g_λ on Hintz's initial surface, continued G-equivariantly to exact Tangherlini data
beyond a ball ([[ch:after-shell]]), have a G-invariant vacuum development, with the same data as g_λ on that ball,
which settles to five-dimensional Tangherlini of a mass m′ with |m′ − μ_end| < ε_m: its difference from that metric
is O(t*^(−2−ε)) in spatially compact subsets of the exterior;

(ii) (without symmetry) every smooth vacuum data set on the same surface whose difference from the data of (i) lies
in Hintz's data class — polyhomogeneous at spatial infinity, with terms of orders r^(−2) and r^(−3) in the metric and
r^(−3) and r^(−4) in the second fundamental form, and conormal remainders in r^(−ℓ0) H_b^∞ and r^(−ℓ0−1) H_b^∞ — and has
norm less than δ in that class has a vacuum development that, its initial slice boosted by a Lorentz boost below ε_m,
settles at the same rate to a Myers–Perry black hole of mass m′ with |m′ − μ_end| < ε_m and spin below ε_m.

[[thm:settling]] is proved in [[ch:settling-proof]], from the stability theory of [[part:stability]] to
[[part:stability-nonlinear]], which is Hintz's proof of the nonlinear stability of Kerr [Hin26] carried into spacetime
dimension n + 1 = 5 and written out in full. Gluing a perturbation far out to a boosted Myers–Perry metric replaces its
data near infinity, on which the solution near the hole at late times depends; so (ii) is stated for perturbations in
Hintz's own data class, where his theorem applies without gluing, and [[ch:after-shell]] determines which decaying
perturbations it reaches, directly or through gluing. The rate holds for every ε < ε_K.

The linear statement is proved with it, as the nonlinear theorem's linearisation at the Tangherlini data
([[thm:viii-2-2]], [[cor:viii-2-3]]). Every solution of the linearised constraint equations in Hintz's data class has
a linearised vacuum development in his generalised wave gauge. Up to a linearised boost it takes those data, and where
the late-time cut-off is 1 it differs from a linearised Myers–Perry metric by O(t*^(−2−ε)) in spatially compact
subsets of the exterior, for each ε < ε_K. In the class the boost vanishes and the Myers–Perry change is a change of
mass alone. A linearised vacuum solution given in another gauge, with the same data up to those of a linearised
diffeomorphism and given on the whole future of the initial surface outside r = r_0, smooth up to that surface,
differs from this one there by a linearised diffeomorphism L_X g, X unique up to Killing fields ([[thm:ix-2-2]],
[[cor:ix-2-3]]).

### Further results {#sec:further-results}

The remaining chapters prove the following; each is stated in full where it is proved.

- *After the shell.* On {v > v_end} every oscillating profile of the approximant vanishes, the estimate of
  [[thm:uniform-existence]] holds at every order of derivatives, and the data near the hole are small in every norm
  [[thm:settling]] uses; equivariant gluing matches the mass alone. The perturbations to which [[thm:settling]] (ii)
  applies, directly or through gluing uniformly in the gluing radius, are exactly those small in Hintz's class
  ([[ch:after-shell]]).
- *Beyond the boundary.* The development of [[thm:settling]] (i) also reaches inside the black hole after the shell,
  up to the curvature boundary, and on the common domain of dependence it and g_λ are one spacetime
  ([[prop:interior]]). The development of g_λ's own data settles, with no gluing, in a data class wider than (ii)'s by
  half-integer orders, for every λ below a threshold and with no exceptional set ([[thm:own-data]]).
- *The linear solution in two gauges.* In a Regge–Wheeler-type gauge the gauge vector is explicit, and the
  perturbation settles to the change of mass on each region r ≤ R, the horizon included, at the linear rate with two
  derivatives lost ([[thm:rw-settling]]). In the harmonic gauge a representative exists on the whole domain, induces
  the given data and settles on each region r ≤ R to μ̇K* + c π_(W*), the gauge-fixed change of mass plus a multiple of
  the pure-gauge solution of an explicit stationary one-form W*, at the rate τ^(−min(p,3/2)+ε), where p > 1/2 + 2γ_Υ
  is the order of decay of its spherically symmetric gauge data at spatial infinity and γ_Υ a parameter of the gauge
  of the stability theory ([[thm:harmonic-rate]]).
- *The constants of [[thm:settling]].* The loss d of the tame estimates and the regularity N_NM = 21d + 6 of the
  Nash–Moser step, with explicit upper bounds at a parameter point that lies outside the proved set ([[thm:loss-d]]),
  explicit resolvent bounds on five-dimensional Tangherlini ([[ch:resolvent-bounds]]), and where explicit evaluation
  of λ1 and δ stops ([[ch:explicit-constants]]).
- *More families.* Two crossing radial null dusts, one ingoing and one outgoing, with the background, the
  approximant, the uniform estimate and the data ([[thm:two-dusts]]); Cauchy stability of the class
  Einstein–null-dust system, without smallness, on compact domains of the type of Ω, for caustic-free dusts, the axes
  included where the lateral boundaries meeting them are adapted to the dust ([[thm:class-stability]]); restricted
  massless Vlasov limits, for fields that are caustic-free families of dusts meeting the hypotheses stated there, as
  weak limits of class vacuum metrics along odd numbers of dusts ([[thm:vlasov]]); and exactly localised vacuum data
  near the data of [[thm:main]], of the form background + εδ + O(ε²) with δ not a gauge perturbation and ε small: on
  every band of the initial slice that meets the inside of the apparent horizon such data exist, while on bands outside
  it the sign of their second-order charge excludes them when δ is invariant ([[thm:charge-sign]]).
- *The boundary at equality.* If μ0 = √72 l5², the curvature boundary is spacelike for g_λ away from a layer at the
  start of the shell, where timelike curves of g_λ cross it ([[thm:layer]], [[cor:layer]]), and at the very edge of
  the layer the character of the boundary is decided column by column ([[thm:very-edge]]).
- *Physical wavelengths.* An upper bound for λ0 at a numerical point, and an approximate value, which is not proved, of
  the first stage's mean correction there ([[prop:lambda0]]); at the prescribed wavelength 10 l5 there is no separation
  of scales, and existence holds where the solution is the seed ([[thm:ten-l5]]).

[[ch:scope]] collects what is claimed and what is not.
