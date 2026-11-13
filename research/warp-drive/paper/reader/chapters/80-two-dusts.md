# Part. Further results {#part:further}

## Two crossing null dusts {#ch:two-dusts}

This chapter carries [[thm:main]] over to two families of waves, one ingoing and one outgoing, whose high-frequency
limit is a solution of the Einstein equations with two crossing radial null dusts. Three things change. The background
is no longer explicit: it is the solution of a characteristic problem with explicit Vaidya data on two null cones, and it
is a Vaidya metric everywhere except on a compact diamond where the two dusts cross ([[prop:two-dust-background]]). The
approximant carries two phases, and the harmonics that mix them are removed at every order by division by a symbol that
is bounded away from zero, so that there are no small divisors ([[lem:two-dust-nonresonance]]). The uniform estimate
needs one phase shift per family; the two phase shifts are coupled through bounded coefficients, and the coupling
enters at the top order of their second derivatives, which are therefore estimated together
([[thm:two-dust-uniform]]). The data, the spheres' horizon and the mean mass then follow as for one family.

Where an argument of [[ch:approximant]], [[ch:uniform-existence]], [[ch:data]] or [[ch:horizon-mass]] carries over word
for word we say so, and we write out what changes.

### The data and the theorem {#sec:two-dust-statement}

*Notation.* The background g0 of this chapter is a round double-null metric

    g0 = −2 e^(2σ) du dv + R² dΩ₃²,                                                                {#eq:two-dust-metric}

with σ and R > 0 functions of (u, v) and dΩ₃² the round metric of S³, written in the angles (ϑ, φ1, φ2) of
[[sec:background]]. Since g0 is invariant under O(4) acting on S³, the point x := R x̂ ∈ R⁴, x̂ ∈ S³, is well defined, and
with a time function τ (fixed in [[sec:two-dust-background]]) the pair X = (τ, x) is a chart in which tensors are arrays
of Cartesian components, as in [[sec:background]]. Two-phase profiles are smooth functions or tensors f(X, θ1, θ2) on
Ω₂ × T², 2π-periodic in each phase variable; we write [f](X) := f(X, v(X)/λ, u(X)/λ), ⟨f⟩ for the mean over T², F_K :=
∂_(θ_K) for K ∈ {in, out}, θ_in := θ1, θ_out := θ2, ϕ_in := v, ϕ_out := u, and ℓ_K := g0⁻¹ dϕ_K. A harmonic e^(i(n1 θ1 +
n2 θ2)) with n ≠ 0 is *pure* if n1 n2 = 0 and *mixed* if n1 n2 ≠ 0. The chain rule reads

    ∂_a [f] = λ⁻¹ (∂_a v) [F1 f] + λ⁻¹ (∂_a u) [F2 f] + [∂_a f],                                     {#eq:two-dust-chain}

so that, as in [[sec:profiles]], |[f]|_j ≤ C_j sup_(i≤j) |∂^i_(X,θ) f|_(L^∞) in the scaled norms [[eq:scaled-norm]] and
‖∂^i [f]‖_(L^∞) ≤ C λ^(−i). The conformal factor is σ; the letter s is kept for the contractions s_K(h) := h(ℓ_K, ℓ_K)
of [[sec:two-dust-uniform]].

**Definition {#def:two-dust-data}** (The two-dust data.) Let l5, μ0 ≥ √72 l5², A > 0, env ∈ C_c^∞([v_start, v_end]),
T > 0 and τ0 with v_start − τ0 > √μ0 + 1 be as in [[thm:main]], and let q0, δ0 and a = q0 − δ0 be as in
[[sec:domain]]. An outgoing family is given by A₂ > 0 and env₂ ∈ C_c^∞((u1, u2)). Put

    𝒜(v) := (1/3) A² env(v)²,      ℬ(u) := (1/3) A₂² env₂(u)²,      E₂ := (2/9) A₂² ∫ env₂².          {#eq:two-dust-fluxes}

The characteristic data of the background are explicit Vaidya data on two null cones, both in the past of Σ_τ0:

- on the ingoing cone 𝒞_in := {v = v0}, v0 < τ0 + a, before the shell: Tangherlini of mass μ0 (the seed) for u ≥ u2;
  across the packet [u1, u2] the outgoing Vaidya metric g = −(1 − m(u)/r²) du² − 2 du dr + r² dΩ₃², u its retarded
  time, with dm/du = −(2/9) A₂² env₂(u)², the mass law [[eq:mu-rate]] for the outgoing wave; and Tangherlini of mass
  μ0 + E₂ for u ≤ u1. The packet lies where 𝒞_in is untrapped, r² > m;
- on the outgoing cone 𝒞_out := {u = u0}, u0 < u1, outside the packet: the ingoing Vaidya metric [[eq:vr-form]], v its
  advanced time, with dμ/dv = (2/9) A² env(v)² and μ = μ0 + E₂ before the shell.

On 𝒞_in the parameter u is the retarded time on {u ≤ u2}, continued smoothly and increasing inward, and affine on
{u ≥ u2 + 1}; on 𝒞_out the parameter v is the advanced time. These fix the double-null coordinates (u, v) of the
background, each constant on the null cones of the other family. The *ingoing waves* are the wave W_TT of [[eq:waves]]
with the phase variable θ1 in place of θ; the *outgoing waves* are the same tensor with A₂, env₂(u) and θ2 in place of
A, env(v) and θ. Both are written in the chart X, where |x| = R.

The outgoing waves are posed on Σ_τ0, not at past null infinity: traced to the past, their rays run inward, toward the
seed's past horizon.

The background, its domain Ω₂, the region D_T, the slice Σ_τ0 and the number ε1 are those of
[[sec:two-dust-background]] ([[prop:two-dust-background]], [[lem:two-dust-domain]]). The trace of the packet on Σ_τ0 is
the shell of the points of Σ_τ0 with u1 ≤ u ≤ u2; it is {r1 ≤ R ≤ r2} for numbers r1 < r2 ([[prop:two-dust-background]]
(a)).

**Theorem {#thm:two-dusts}** (Two crossing dusts.) Let the data be those of [[def:two-dust-data]], with the packet's
trace on Σ_τ0 placed between the seed's horizon and the shell, √μ0 < r1 < r2 < v_start − τ0, and the outer cone 𝒞_out
chosen as in [[lem:two-dust-domain]], so that it meets {τ ≥ τ0} only where R > b(τ). Let g0 be the two-dust background
on the domain Ω₂ ([[sec:two-dust-background]]). Fix K ≥ 6. There are λ0 > 0 and C, depending on the data, T, τ0, K and
a, and not on λ, such that for every λ ∈ (0, λ0] there is a smooth Lorentzian metric g_λ on Ω₂ ⊃ D_T ∩ {τ ≥ τ0},
invariant under the T² action and both reflections, with:

1. *Vacuum.* Ric(g_λ) = 0 on Ω₂.
2. *Data.* On Σ_τ0 the Cauchy data of g_λ satisfy the vacuum constraints exactly, equal the seed's on R < r1, and
   differ from those of the two-phase approximant g_app of [[thm:two-dust-approximant]], with N = K + 3 stages, by
   O(λ^K) in the norm Data of item 2 of [[thm:main]].
3. *The remainder.* g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω₂.
4. *Convergence.* |g_λ − g0| ≤ C λ, |∂g_λ| ≤ C, and ∂g_λ − ∂g0 = dv ⊗ [F1 g1] + du ⊗ [F2 g1] + O(λ), so ∂g_λ → ∂g0
   weakly in L²(Ω₂), and not strongly wherever env or env₂ is nonzero. The limit is the two-null-dust background:

       Ric(g0) = K_in dv ⊗ dv + K_out du ⊗ du,      K_in R³ = 𝒜(v),      K_out R³ = ℬ(u),                {#eq:two-dust-limit}

   the two families' Isaacson fluxes [[eq:two-dust-fluxes]].
5. *Gauge and uniqueness.* D(g_λ) = 0 on Ω₂ (the gauge of [[sec:gauge]], relative to the two-dust g0), and g_λ is the
   only C² solution g of Ric^H(g) = 0 on Ω₂ with the data of g_λ on Σ_τ0 and |g − g0| ≤ ε1 on Ω₂.
6. *The spheres' horizon.* For a column (v and x̂ fixed, R varying, within D_T ∩ {τ ≥ τ0}) let R_H(v) be the zero on
   the column of the outgoing expansion of the round spheres of g0, the radius at which R² = μ. There are λ_H ∈ (0, λ0]
   and C, δ1, δ2 > 0 such that for λ ≤ λ_H: on every column the outgoing expansion of the spheres S_(v,R) for g_λ has
   at most one zero, positive above it and negative below it; if μ0 > √72 l5², on every column with R_H(v) ≤ v − τ0 −
   δ1 it has exactly one, within C λ of R_H(v), the spheres with R ≤ R_H(v) − C λ being trapped and those with
   R ≥ R_H(v) + C λ untrapped; if μ0 = √72 l5², the same holds on the columns with R_H(v)² ≥ μ0 + δ2 and R_H(v) ≤ v −
   τ0 − δ1 ([[prop:two-dust-one-zero]]). No condition on where the outgoing packet lies is needed beyond those above.
7. *Mean mass.* For every sphere S_(v,R) in D_T ∩ {τ ≥ τ0} at which neither family oscillates (v ∉ (v_start, v_end)
   and u ∉ (u1, u2)), its Hawking mass [[eq:hawking-mass]] satisfies |M[S](g_λ) − μ(S)| ≤ C λ², μ(S) the background's
   mass function there; elsewhere |M[S](g_λ) − μ(S)| ≤ C λ ([[prop:two-dust-mean-mass]]).

The theorem is the conjunction of the background on the whole domain ([[prop:two-dust-background]], [[lem:two-dust-domain]]), the
approximant ([[thm:two-dust-approximant]]), the uniform estimate ([[thm:two-dust-uniform]]), the data
([[thm:two-dust-data]]), and [[prop:two-dust-one-zero]] and [[prop:two-dust-mean-mass]]; it is assembled in
[[sec:two-dust-proof]].

**Remark {#rem:two-dust-scope}** (Other placements of the packet.) The theorem does not treat data whose packet lies
outside the shell on Σ_τ0, for then the two families do not cross in the future of Σ_τ0, nor data whose packet lies
inside the seed's horizon: there the packet is trapped on 𝒞_in and the mass function increases inward across it, so
that the argument for the lower bound μ ≥ μ0 of [[prop:two-dust-background]] (b), on which the inner boundary of the
domain rests, does not apply; that case is not examined here.

### The two-dust background {#sec:two-dust-background}

In this section g0 is a round double-null metric [[eq:two-dust-metric]] on a region of the (u, v)-plane, and 𝒜(v),
ℬ(u) ≥ 0. The *two-null-dust equations* are [[eq:two-dust-limit]], Ric(g0) = (𝒜/R³) dv ⊗ dv + (ℬ/R³) du ⊗ du: the right
side is the stress of two radial null dusts, one along ℓ_in = g0⁻¹ dv and one along ℓ_out = g0⁻¹ du, each trace-free
because dv and du are null. We time-orient g0 so that u and v increase to the future; the causal past of a point p in
a rectangle of the (u, v)-plane is J⁻(p) := {u ≤ u(p), v ≤ v(p)} there.

**Lemma {#lem:two-dust-equations}** (The equations.) For a round double-null metric, with γ̂ the round metric of S³ and
A, B angular indices, the nonzero components of the Ricci tensor are

    Ric_uu = −(3/R)(R_uu − 2σ_u R_u),      Ric_vv = −(3/R)(R_vv − 2σ_v R_v),      Ric_uv = −2σ_uv − 3 R_uv/R,
    Ric_AB = 2 e^(−2σ) (R R_uv + e^(2σ) + 2 R_u R_v) γ̂_AB.

Hence g0 solves the two-null-dust equations exactly when the evolution equations

    R R_uv = −(e^(2σ) + 2 R_u R_v),      σ_uv = 3 (e^(2σ) + 2 R_u R_v)/(2R²)                           {#eq:two-dust-evolution}

and the two constraints

    C_u := R_uu − 2σ_u R_u + ℬ/(3R²) = 0,      C_v := R_vv − 2σ_v R_v + 𝒜/(3R²) = 0                     {#eq:two-dust-constraints}

hold. Modulo [[eq:two-dust-evolution]], ∂_v(R² C_u) = (1/3) ∂_v ℬ = 0 and ∂_u(R² C_v) = (1/3) ∂_u 𝒜 = 0. So data with
C_v = 0 on a cone {u = u0} and C_u = 0 on a cone {v = v0}, evolved by [[eq:two-dust-evolution]], give a solution of the
two-null-dust equations.

*Proof.* Write g0 = h + R² γ̂ with h := −2e^(2σ) du dv, so that h^(uv) = −e^(−2σ). The nonzero Christoffel symbols of
h are Γ^u_uu = 2σ_u and Γ^v_vv = 2σ_v; those of g0 are these, Γ^a_AB = −R ∇^a R γ̂_AB for a ∈ {u, v} (∇ the connection
of h), Γ^A_aB = (∂_a R/R) δ^A_B, and those of γ̂. With R_bd = ∂_cΓ^c_bd − ∂_dΓ^c_bc + Γ^c_ceΓ^e_bd − Γ^c_deΓ^e_bc, as
in the proof of [[lem:warped-ricci]], the trace Γ^A_bA = 3 ∂_b R/R contributes −∂_a(3 ∂_b R/R) + 3 Γ^c_ab ∂_c R/R −
Σ_(A,B) Γ^A_aB Γ^B_bA = −(3/R) ∇_a∇_b R to Ric_ab; the components Ric_aA vanish, the reflections of S³ that fix a
point being isometries; and the angular components are Ric_AB = (2 − R □_h R − 2 |dR|²_h) γ̂_AB, the 2 being the Ricci
curvature of the unit three-sphere. For h, ∇_u∇_u R = R_uu − 2σ_u R_u, ∇_v∇_v R = R_vv − 2σ_v R_v, ∇_u∇_v R = R_uv,
Ric[h]_uu = Ric[h]_vv = 0, Ric[h]_uv = −∂_v Γ^u_uu = −2σ_uv, □_h R = −2e^(−2σ) R_uv and |dR|²_h = −2e^(−2σ) R_u R_v.
This gives the four components. The angular equation is the first of [[eq:two-dust-evolution]]; with it, Ric_uv = 0 is
σ_uv = −3 R_uv/(2R), the second; Ric_uu = ℬ/R³ is C_u = 0, and Ric_vv = 𝒜/R³ is C_v = 0.

For the propagation, put Y := R² (R_uu − 2σ_u R_u), so that R² C_u = Y + ℬ/3. Differentiating the first equation of
[[eq:two-dust-evolution]] in u gives R R_uuv = −2σ_u e^(2σ) − 2 R_uu R_v − 3 R_u R_uv, and σ_uv = −3 R_uv/(2R). Hence

    ∂_v Y = 2R R_v (R_uu − 2σ_u R_u) + R (R R_uuv) − 2R² σ_uv R_u − 2R² σ_u R_uv
          = −2R σ_u (e^(2σ) + 2 R_u R_v + R R_uv) = 0,

and ∂_v(R² C_u) = ∂_v ℬ/3 = 0, since ℬ depends on u alone. The identity for C_v is the same with u and v exchanged.
So R² C_u is constant along each line of constant u and vanishes where that line meets {v = v0}; likewise C_v. ∎

**Lemma {#lem:two-dust-identities}** (Identities.) Let g0 solve the two-null-dust equations and put

    μ := R² (1 + 2 e^(−2σ) R_u R_v),      f := 1 − μ/R² = −2 e^(−2σ) R_u R_v = g0⁻¹(dR, dR),               {#eq:two-dust-mass}

the mass function. Then:

(i) μ_u = −(2/3) ℬ e^(−2σ) R_v and μ_v = −(2/3) 𝒜 e^(−2σ) R_u;
(ii) R_uv = −e^(2σ) μ/R³, σ_uv = (3/2) e^(2σ) μ/R⁴ and (R³)_uv = −3 R e^(2σ);
(iii) μ_uv = (2/9) 𝒜ℬ e^(−2σ)/R²;
(iv) (e^(−2σ) R_u)_u = −e^(−2σ) ℬ/(3R²) and (e^(−2σ) R_v)_v = −e^(−2σ) 𝒜/(3R²);
(v) where R_u < 0, (v̂, R) are coordinates for every increasing function v̂ of v, and with e^ψ := −e^(2σ)/(R_u v̂′),

        g0 = −e^(2ψ) f dv̂² + 2 e^ψ dv̂ dR + R² dΩ₃²,   g0^(v̂v̂) = 0,  g0^(v̂R) = e^(−ψ),  g0^(RR) = f,  ψ_u = ℬ/(3R² R_u);
                                                                                                     {#eq:two-dust-chart}
    where R_v > 0, for every increasing function ũ of u, with e^ψ̃ := e^(2σ)/(R_v ũ′), g0 = −e^(2ψ̃) f dũ² − 2 e^ψ̃ dũ dR
    + R² dΩ₃² and ψ̃_v = 𝒜/(3R² R_v);
(vi) the Kretschmann scalar is

        𝒦 = 72 μ²/R⁸ + (8/3) e^(−4σ) 𝒜ℬ/R⁶.                                                         {#eq:two-dust-kretschmann}

*Proof.* (i) Differentiating, μ_u = 2R R_u + 2e^(−2σ)(2R R_u² R_v − 2R² σ_u R_u R_v + R² R_uu R_v + R² R_u R_uv). By the
first equation of [[eq:two-dust-evolution]], R² R_u R_uv = −R R_u (e^(2σ) + 2 R_u R_v), so μ_u = 2e^(−2σ) R² R_v (R_uu −
2σ_u R_u), which is −(2/3) ℬ e^(−2σ) R_v by C_u = 0. The second identity is the same with u and v exchanged.
(ii) By [[eq:two-dust-mass]], e^(2σ) + 2 R_u R_v = e^(2σ) μ/R², which turns [[eq:two-dust-evolution]] into the first two
identities; and (R³)_uv = 3R (R R_uv + 2 R_u R_v) = −3R e^(2σ).
(iv) is e^(−2σ) C_u = 0 and e^(−2σ) C_v = 0. (iii) Differentiate μ_v = −(2/3) 𝒜 e^(−2σ) R_u in u and use (iv).
(v) With dv = dv̂/v̂′ and du = (dR − R_v dv)/R_u,

    −2 e^(2σ) du dv = −(2 e^(2σ)/(R_u v̂′)) dR dv̂ + (2 e^(2σ) R_v/(R_u v̂′²)) dv̂² = 2 e^ψ dv̂ dR − e^(2ψ) f dv̂²,

because e^(2ψ) f = (e^(4σ)/(R_u² v̂′²))(−2e^(−2σ) R_u R_v). The (v̂, R) block [[−e^(2ψ) f, e^ψ], [e^ψ, 0]] has the
inverse [[0, e^(−ψ)], [e^(−ψ), f]]. Since v̂′ depends on v alone, ψ_u = 2σ_u − R_uu/R_u = −(R_uu − 2σ_u R_u)/R_u =
ℬ/(3R² R_u) by C_u = 0. The second form follows in the same way from du = dũ/ũ′ and dv = (dR − R_u du)/R_v, and
ψ̃_v = 2σ_v − R_vv/R_v = 𝒜/(3R² R_v) by C_v = 0.
(vi) For the warped product g0 = h + R² γ̂ the nonzero components of the Riemann tensor are, up to its symmetries,
R_abcd = K_h (h_ac h_bd − h_ad h_bc), R_aAbB = −R ∇_a∇_b R γ̂_AB and R_ABCD = R² (1 − |dR|²_h)(γ̂_AC γ̂_BD − γ̂_AD
γ̂_BC), with K_h the Gauss curvature of h; they follow from the Christoffel symbols of the proof of
[[lem:two-dust-equations]] as in the proof of [[lem:vr-curvature]]. Hence, counting the four orderings of the mixed
components and using γ̂^(AB) γ̂_AB = 3,

    𝒦 = 4 K_h² + 12 |∇∇R|²_h/R² + 12 (1 − |dR|²_h)²/R⁴.

Here Ric[h]_uv = K_h h_uv gives K_h = 2e^(−2σ) σ_uv = 3μ/R⁴ by (ii), 1 − |dR|²_h = μ/R², and, with ∇_u∇_u R = −ℬ/(3R²),
∇_v∇_v R = −𝒜/(3R²) and ∇_u∇_v R = −e^(2σ) μ/R³,

    |∇∇R|²_h = 2 (h^(uv))² ((∇_u∇_v R)² + ∇_u∇_u R ∇_v∇_v R) = 2 e^(−4σ) (e^(4σ) μ²/R⁶ + 𝒜ℬ/(9R⁴)).

So 𝒦 = 36 μ²/R⁸ + 24 μ²/R⁸ + (8/3) e^(−4σ) 𝒜ℬ/R⁶ + 12 μ²/R⁸. ∎

At ℬ = 0 these are the identities of [[prop:vaidya]]: with v̂ = v and ψ = 0 the mass law μ_v = (2/3) 𝒜, and the
Kretschmann scalar 72 μ²/R⁸. One null dust has Ric_ab Ric^ab = 0; two crossing ones do not, and their term in 𝒦 is
nonnegative because 𝒜ℬ ≥ 0.

**Proposition {#prop:two-dust-background}** (The background on the whole domain.) Let the data be those of
[[def:two-dust-data]], fix V1 > 2(v_end + T) + 1 − τ0, and let Q := [u0, ∞) × [v0, V1] in the double-null coordinates
of [[def:two-dust-data]]. There is a past set 𝒟 ⊂ Q, the development of the data, on which the characteristic problem
has exactly one smooth solution g0 of the two-null-dust equations, and:

(a) *Structure.* Where ℬ = 0 the background is an ingoing Vaidya metric, after reparametrising v, and where 𝒜 = 0 and
R_v ≠ 0 an outgoing Vaidya metric: the only region where it is not a Vaidya metric is the compact crossing diamond
Q× := [u1, u2] × [v_start, v_end]. Off Q× it is explicit from the data only in {u ≤ u1}, where it is the ingoing
Vaidya metric of the data on 𝒞_out with v its advanced time, and in {v ≤ v_start}, where it is the outgoing Vaidya
metric of the data on 𝒞_in; in {u ≥ u2} and in {v ≥ v_end} it is a Vaidya metric with the mass functions μ(u2, ·) and
μ(·, v_end), read from the solution on the edges of the diamond. On the slice Σ_τ0 of [[lem:two-dust-domain]] the
Cauchy data are the seed's for R < r1, outgoing Vaidya on the packet r1 ≤ R ≤ r2, Tangherlini of mass μ0 + E₂ between
the packet and the shell, and those of the shell of [[thm:main]] outside.

(b) *The mass bound.* μ ≥ μ0 on 𝒟.

(c) *The inner sphere.* R_u < 0 on 𝒟. On {R = a}, μ > a², so {R = a} is trapped (R_u, R_v < 0) and spacelike,
g0⁻¹(dR, dR) = 1 − μ/a² < 0, and R decreases along future causal curves crossing it. If R(p) ≥ a, then R ≥ min(R(p),
√μ0) ≥ a on J⁻(p).

(d) *Existence.* The set G := {p ∈ 𝒟 : R ≥ a on J⁻(p)} is closed in Q and its boundary in Q lies in {R = a}; the
background is smooth on G.

*Proof.* (c), first part. The corner (u0, v0) lies on the part of 𝒞_in where the data are Tangherlini of mass μ0 + E₂
and the cone is untrapped, and u increases inward along 𝒞_in, so R_u(u0, v0) < 0. Along 𝒞_out, μ ≥ μ0 + E₂ > 0 (the
data's mass function is nondecreasing), so ∂_v R_u = R_uv = −e^(2σ) μ/R³ < 0 there by [[lem:two-dust-identities]] (ii),
and R_u(u0, ·) < 0. By [[lem:two-dust-identities]] (iv), ∂_u(e^(−2σ) R_u) ≤ 0, so e^(−2σ) R_u ≤ e^(−2σ(u0, v)) R_u(u0,
v) < 0 wherever the solution exists.

(b) By [[lem:two-dust-identities]] (iii), μ_uv ≥ 0, so μ(u, v) ≥ μ(u, v0) + μ(u0, v) − μ(u0, v0). The difference
μ(u0, v) − μ(u0, v0) = ∫ μ_v(u0, ·) is nonnegative, because μ_v = −(2/3) 𝒜 e^(−2σ) R_u ≥ 0 by (i) and R_u < 0. On 𝒞_in,
μ(·, v0) = m decreases from μ0 + E₂ to μ0 across the untrapped packet and equals μ0 inward of it. Hence μ ≥ μ0.

(c), the rest. Since a < q0 ≤ √μ0 ([[sec:domain]], μ0 ≥ √72 l5²), μ ≥ μ0 > a² on {R = a}, so f < 0 there, and as
f = −2e^(−2σ) R_u R_v with R_u < 0, also R_v < 0: both null expansions of the round spheres are negative, and dR is
timelike. Future causal vectors are combinations of ∂_u, ∂_v with nonnegative coefficients plus vectors tangent to the
spheres, so dR is negative on them. For the last claim let q = (u_q, v_q) ∈ J⁻(p). Since R_u < 0, R(q) ≥ R(u_p, v_q),
so it suffices to bound R(u_p, ·) on [v0, v_p]. Suppose R(u_p, v′) < min(R(p), √μ0) for some v′ < v_p. There R² < μ0 ≤
μ, so R_v < 0 as above. Let v″ be the supremum of the v ∈ [v′, v_p] such that R(u_p, ·) < min(R(p), √μ0) on [v′, v];
on [v′, v″] R(u_p, ·) decreases, so R(u_p, v″) ≤ R(u_p, v′) < min(R(p), √μ0), and continuity forces v″ = v_p, so that
R(p) < min(R(p), √μ0), a contradiction.

(a) By [[lem:two-dust-identities]] (i) and (v), μ_u = 0 and ψ_u = 0 where ℬ = 0, so there μ and ψ are functions of v
alone on each segment of constant v, and with dṽ := e^ψ dv̂ the form [[eq:two-dust-chart]] becomes −f dṽ² + 2 dṽ dR +
R² dΩ₃², f = 1 − μ(ṽ)/R²: an ingoing Vaidya metric. On 𝒞_out the data are those of the ingoing Vaidya metric in its
advanced time v, for which e^ψ = 1 when v̂ = v, by comparison of [[eq:two-dust-chart]] with [[eq:vr-form]]; so ψ = 0 on
𝒞_out with v̂ = v, and on {u ≤ u1} the background is that ingoing Vaidya metric, with the mass function of the data. On
{u ≥ u2} it is ingoing Vaidya with ψ(u2, ·) and μ(u2, ·). The statements where 𝒜 = 0 follow in the same way from the
second form of (v), with ψ̃ = 0 on 𝒞_in ∩ {u ≤ u2} in the retarded time of the data. Where 𝒜 = ℬ = 0 the background is
Tangherlini. Both 𝒜 and ℬ are nonzero only on Q×, which is compact.

On Σ_τ0, u is strictly decreasing outward: in the chart of [[lem:two-dust-domain]], where v̂ = v and e^ψ = −e^(2σ)/R_u,
R_v = e^ψ f/2 ≤ 1/2, since e^ψ ≤ 1 and f ≤ 1, so du(∂_R|_τ) = (1 − R_v)/R_u < 0. Hence the points of Σ_τ0 with u ∈
[u1, u2] form a shell r1 ≤ R ≤ r2, with u > u2 inside it and u < u1 outside. The points of Σ_τ0 with R < v_start − τ0
have v = τ0 + R < v_start, where the background is the outgoing Vaidya metric of the data on 𝒞_in: Tangherlini of mass
μ0 for u > u2, outgoing Vaidya on the packet, Tangherlini of mass μ0 + E₂ for u < u1. Since r2 < v_start − τ0, the
points with R ≥ v_start − τ0 have u < u1, where the background is the ingoing Vaidya metric of the data on 𝒞_out, the
shell of [[thm:main]] on a Tangherlini metric of mass μ0 + E₂.

(d) *The integral equations.* Put U := (R, σ, P, Q̄), F(U) := −(e^(2σ) + 2 P Q̄)/R, H(U) := 3 (e^(2σ) + 2 P Q̄)/(2R²),
and for a function z on Q, D[z](u, v) := z(u0, v) + z(u, v0) − z(u0, v0). Consider

    P(u, v) = P(u, v0) + ∫_(v0)^v F(U)(u, v′) dv′,        Q̄(u, v) = Q̄(u0, v) + ∫_(u0)^u F(U)(u′, v) du′,
    R(u, v) = R(u0, v) + ∫_(u0)^u P(u′, v) du′,          σ(u, v) = D[σ](u, v) + ∫_(u0)^u ∫_(v0)^v H(U),        {#eq:two-dust-volterra}

with the data P(·, v0) = ∂_u R(·, v0), Q̄(u0, ·) = ∂_v R(u0, ·), R(u0, ·) and σ on both cones, which satisfy C_u = 0 on
𝒞_in and C_v = 0 on 𝒞_out. A continuous solution solves [[eq:two-dust-evolution]]: R_u = P by the third equation;
differentiating it in v, R_v(u, v) = ∂_v R(u0, v) + ∫ ∂_v P du′ = Q̄(u0, v) + ∫ F du′ = Q̄(u, v); so R_uv = P_v = F, and
σ_uv = H. The constraints [[eq:two-dust-constraints]] then hold by [[lem:two-dust-equations]], propagated from the cones.

*A priori bounds.* Let S ⊂ Q be a past set on which a solution exists with R ≥ a′ > 0. With R_max := max_v R(u0, v)
and the identities of [[lem:two-dust-identities]], at every point of S: (i) R³ = D[R³] − 3 ∫∫ R e^(2σ), and D[R³] ≤
R(u0, v)³ because R decreases along 𝒞_in, so R ≤ R_max and 3 ∫∫ R e^(2σ) ≤ R_max³ over every rectangle J⁻(p);
(ii) μ ≥ μ0 by (b); (iii) σ_uv ≥ 0, so σ ≥ D[σ] ≥ −S0, S0 := −min D[σ]; and on the part of S where u ≤ U, for a
number U: (iv) μ_uv ≤ (2/9) max(𝒜ℬ) e^(2S0)/a′², so μ ≤ M⁺ := max D[μ] + (2/9) max(𝒜ℬ) e^(2S0) (U − u0)(V1 − v0)/a′²;
(v) σ_uv = (3/2) e^(2σ) μ/R⁴ ≤ (3/2)(M⁺/a′⁵) R e^(2σ), so σ ≤ max D[σ] + (M⁺/(2a′⁵)) R_max³; (vi) |R_uv| = e^(2σ) μ/R³
is then bounded, and so are P and Q̄, by integrating R_uv from the cones. So |U| ≤ K_0 there, with K_0 depending on the
data, a′ and U only; each bound comes from the data, a′ and the bounds before it.

*Boundedness of the domain.* On 𝒞_in ∩ {u ≥ u2 + 1}, ℬ = 0 and u is affine, so σ_u = 0 there and C_u = 0 gives R_uu =
0: R_u(·, v0) is constant there, and R_u(·, v0) < 0 on the compact [u2, u2 + 1]; so R_u(·, v0) ≤ c0 < 0 on {u ≥ u2}.
R_uv = −e^(2σ) μ/R³ < 0 gives R_u ≤ c0 on {u ≥ u2} wherever the solution exists, so R ≤ R_max + c0 (u − u2) there, and
the set where R ≥ a′ lies in {u ≤ U(a′)}, U(a′) := u2 + (R_max − a′)/|c0|, for every a′ > 0.

*Existence.* Fix a′ ∈ (0, a), let K_0 be the bound above for this a′ and U = U(a′), K > K_0, and let F_K, H_K be smooth,
globally Lipschitz in U, and equal to F, H on {|U| ≤ K, R ≥ a′}. The map defined by the right sides of
[[eq:two-dust-volterra]] with F_K, H_K is a contraction in the norm sup_Q e^(−γ (u − u0 + v − v0)) |U| for γ large: each
single integral divides the Lipschitz constant by γ and the double one by γ², on the unbounded u-interval as well. So
it has one continuous fixed point Ũ on Q. Let Q_(a′) := {p ∈ Q : R̃ > a′ on J⁻(p)}, R̃ the first component of Ũ.
(1) Ũ solves the true equations on Q_(a′). For p ∈ Q_(a′), suppose |Ũ| ≥ K somewhere on the compact J⁻(p), and let q be
such a point with u + v least. On J⁻(q) ∖ {q}, |Ũ| < K and R̃ > a′, so Ũ solves the true equations there, the a priori
bounds give |Ũ| ≤ K_0 there and, by continuity, at q: a contradiction. (2) Q_(a′) is a past set, open in Q, the least of
R̃ over J⁻(p) being continuous in p; the development 𝒟 := ∪_(a″>0) Q_(a″) is a past set carrying one smooth solution,
since two truncations agree where both solve the true equations, by the contraction. (3) For p ∈ 𝒟 with R(p) ≥ a, (c)
applies on J⁻(p) ⊂ 𝒟 and gives R ≥ min(R(p), √μ0) ≥ a > a′ there, so p ∈ Q_(a′). (4) So G ⊂ Q_(a′), and G is closed in
Q, as G ⊂ Q_(a′) and R̃ is continuous there. At p ∈ ∂G the least of R over J⁻(p) is a, since otherwise a neighbourhood
of p would lie in G; so (c) at p gives min(R(p), √μ0) ≤ a < √μ0, that is R(p) = a: ∂G ⊂ {R = a}.

*Regularity.* Let U be the continuous solution on a past set. From [[eq:two-dust-volterra]], R_u = P and R_v = Q̄, P_v =
F(U), Q̄_u = F(U), and σ_u, σ_v are continuous. For ∂_u P, the difference quotients δ_h P solve δ_h P(u, v) = δ_h P(u,
v0) + ∫_(v0)^v (a_h · δ_h(R, σ, Q̄) + b_h δ_h P) dv′, where a_h, b_h are the mean values of ∇F on the segments, continuous
and converging uniformly, and δ_h(R, σ, Q̄) → (P, σ_u, F) uniformly; Gronwall's lemma in v makes δ_h P uniformly Cauchy,
so ∂_u P exists and is continuous, and likewise ∂_v Q̄. So U ∈ C¹. The k-th derivatives solve linear Volterra equations
of the same form, with coefficients built from lower derivatives, so U ∈ C^∞ by induction, the data being smooth. ∎

**Lemma {#lem:two-dust-domain}** (The domain.) Use the double-null coordinates of [[def:two-dust-data]], so that v̂ = v
in [[eq:two-dust-chart]] and e^ψ = −e^(2σ)/R_u, and on G the chart X = (τ, x), τ := v − R, x := R x̂. Let r_q(m) :=
(√72 m l5²)^(1/4), V := v_end + T, and

    D_T := {p ∈ G : v ≤ V, R ≥ r_q(μ)},      r_q^♭(v) := min {r_q(μ(p)) : p ∈ D_T, v(p) = v},
    τ_end := max_(v ≤ V) (v − r_q^♭(v)),      b(τ) := V + 1 − τ + (τ_end − τ),
    Ω₂ := {p ∈ G : τ0 ≤ τ ≤ τ_end, v + (τ − τ_end) ≤ V + 1},      Σ_τ := Ω₂ ∩ {τ},                     {#eq:two-dust-omega}

the forms of [[eq:dt]] and [[eq:omega]] with the mass function at the point. The outer cone can be chosen so that
𝒞_out ∩ {τ ≥ τ0} ⊂ {R > b(τ)}, and we choose it so. Then Σ_τ = A(τ) := {a ≤ |x| ≤ b(τ)}, and:

(a) g0⁻¹(dτ, dτ) = 1 − μ/R² − 2e^(−ψ) ≤ −1 − μ/R²: each Σ_τ is spacelike;
(b) on {R = a}, g0⁻¹(dR, dR) = 1 − μ/a² < 0 and g0⁻¹(dR, dτ) = e^(−ψ) − 1 + μ/a² > 0;
(c) g0⁻¹(d(v + τ), d(v + τ)) = 1 − μ/R² − 4e^(−ψ) ≤ −3 − μ/R², and g0⁻¹(dv, dτ) = −e^(−ψ) < 0;
(d) the ingoing generators are the lines {v, x̂ = const}, integral curves of ℓ_in = −e^(−ψ) L0, L0 := ∂_τ − x̂·∂_x;
followed to the past they stay in Ω₂ and meet Σ_τ0; every past causal curve from a point of Ω₂ meets Σ_τ0 inside Ω₂,
and both generators ℓ_in and ℓ_out are transverse to every Σ_τ;
(e) there is ε1 with 0 < ε1 < s0, s0 the least over Ω₂ of the least absolute eigenvalue of g0, such that every
Lorentzian g with |g − g0| ≤ ε1 on Ω₂ is time-oriented by dτ, J⁻(p; g) ∩ {τ ≥ τ0} ⊂ Ω₂ for every p ∈ Ω₂, and Σ_τ and
the two lateral boundaries stay spacelike for g; and every symmetric g̃ with |g̃ − g0| ≤ ε1 on Ω₂ is Lorentzian with
|g̃⁻¹| ≤ (s0 − ε1)⁻¹;
(f) b(τ) − a ≥ 1 + δ0, b ≤ b(τ0), D_T ∩ {τ ≥ τ0} ⊂ Ω₂, and D_T contains {p ∈ G : v ≤ V, 𝒦 ≤ l5⁻⁴}.

From here on ε1 is one fixed number as in (e).

*Proof.* The choice of the cone. In {u ≤ u1} the background is the ingoing Vaidya metric of the data on 𝒞_out
([[prop:two-dust-background]] (a)), so replacing u0 by a smaller value, with the data of the same Vaidya metric on the
new cone and of Tangherlini of mass μ0 + E₂ on the added part of 𝒞_in, changes the background nowhere in {u ≥ u0}, by
the uniqueness in [[prop:two-dust-background]]. Along an outgoing null ray of that Vaidya metric on which R² > μ_end :=
μ0 + E₂ + (2/9) A² ∫ env², the radius increases with τ (its radial speed f/(2 − f) is positive, [[sec:two-dust-phases]])
while b decreases. So the condition holds once the cone meets Σ_τ0 at a radius above max(b(τ0), √μ_end).

The slices. By [[prop:two-dust-background]] (c), R_u < 0 on G, so (v, R) are coordinates there. ψ = 0 on 𝒞_out
([[prop:two-dust-background]] (a)) and ψ_u = ℬ/(3R² R_u) ≤ 0, so ψ ≤ 0 on G. Along each ingoing ray {v = const}, R
decreases strictly inward from 𝒞_out, the point of the ray on 𝒞_out lies in G, and G is closed with boundary in {R = a};
so the ray lies in G until R = a, and G = {a ≤ R ≤ R(u0, v)} in the coordinates (v, R). Along 𝒞_out, which lies where
R² > μ_end, dR/dv = R_v = f/2 < 1, so R(u0, τ + R) − R is strictly decreasing in R, and {τ = const} ∩ G is an interval
a ≤ R ≤ R_out(τ), R_out(τ) the radius at which the slice meets 𝒞_out. By the choice of the cone, R_out(τ) > b(τ) for τ ≥
τ0, and the third condition of [[eq:two-dust-omega]] is R ≤ b(τ); the choice of V1 in [[prop:two-dust-background]]
makes Q contain the values v = τ + R ≤ τ_end + b(τ0). So Σ_τ = A(τ).

(a)–(c) are the contractions of the inverse in [[eq:two-dust-chart]] with dτ = dv − dR and d(v + τ) = 2dv − dR, with
e^(−ψ) ≥ 1 and f = 1 − μ/R². As in the proof of [[lem:domain]], dτ is timelike and positive on future causal vectors; at
R = a, dR and dτ are timelike with positive product, so dR is negative on future causal vectors; and dv(Y) = g0(ℓ_in, Y)
≥ 0 for future causal Y, ℓ_in = −e^(−ψ) L0 being past directed, so v + τ increases to the future.

(d) In the chart, ∂_R at fixed v is −∂_τ + x̂·∂_x = −L0, so ℓ_in = g0^(vR) ∂_R = −e^(−ψ) L0. Along −L0, τ decreases, R
increases and v is fixed, so R ≥ a and v + τ − τ_end ≤ V + 1 are kept; the curve reaches τ = τ0 at R = v − τ0, and for p
∈ Ω₂, v(p) − τ0 ≤ V + 1 + τ_end − τ(p) − τ0 ≤ b(τ0). A past causal curve cannot cross {R = a} or {v + τ = const}
outward, by (b) and (c), nor Σ_τ_end; parametrised by τ, it is Lipschitz on the compact Ω₂ (as in the proof of
[[lem:linear-wave]]), so it reaches Σ_τ0 inside Ω₂. A null vector is never tangent to a spacelike hypersurface.

(e) The strict inequalities in (a)–(c), and the nondegeneracy of g0, are open conditions in g on the compact set Ω₂;
the proof of [[lem:domain]] (e) applies, and that of [[lem:lorentz-margin]] for the bound on g̃⁻¹.

(f) By [[prop:two-dust-background]] (b), μ ≥ μ0, so r_q(μ) ≥ r_q(μ0) = q0 > a. A point of D_T has v ≤ V, R ≥ q0 and
τ = v − R ≤ v − r_q^♭(v) ≤ τ_end, hence v + (τ − τ_end) ≤ v < V + 1: it lies in Ω₂ if τ ≥ τ0. Further τ_end ≤ V − q0,
so b(τ) − a ≥ b(τ_end) − a = V + 1 − τ_end − a ≥ 1 + q0 − a = 1 + δ0, and b decreases. By [[eq:two-dust-kretschmann]]
and 𝒜ℬ ≥ 0, 𝒦 ≥ 72 μ²/R⁸, so 𝒦 ≤ l5⁻⁴ gives R⁸ ≥ 72 μ² l5⁴, that is R ≥ r_q(μ). ∎

So every part of the boundary of Ω₂ other than Σ_τ0 is spacelike with Ω₂ to its past, and Ω₂ is a domain of
dependence of Σ_τ0, for g0 and for every Lorentzian metric within ε1 of g0. Its slices are the annuli A(τ) of
[[sec:domain]], with the outer radius b(τ), b′ = −2, and the same bounds. Hence [[lem:sobolev]], the mollifier 𝒫 of
[[eq:mollifier]] with its properties (M1)–(M6) ([[lem:mollifier]]), and the energy inequality [[lem:energy]] hold on Ω₂
verbatim; the last uses only that Σ_τ, {R = a} and the outer boundary are spacelike with Ω₂ to their past, and (e).

**Remark {#rem:two-dust-example}** (Numerical observation.) The characteristic problem of [[prop:two-dust-background]]
was discretised for one choice of data, in the gauge e^(2σ) = 1/2 on both cones: corner mass 1.5 at R = 5, packet ℬ =
1.7 b(u; 5.7, 7.2) on 𝒞_in, shell 𝒜 = 3.6 b(v; 3, 4.5) on 𝒞_out with b a smooth bump, seed mass μ0 = 0.82211 and mass
3.6058 after the shell, on a rectangle that stops at v = 5. At 40, 80 and 160 steps per unit the discrete solutions
showed the structure of (a), the departures from a Vaidya metric off the diamond being 1.8 × 10⁻⁵, 5.2 × 10⁻³, 5.2 ×
10⁻³ and 2.2 × 10⁻⁴ in the four regions at 160 steps, each falling with the resolution; the mass bound (b) up to a
discretisation deficit falling at second order, −4.0 × 10⁻², −9.9 × 10⁻³ and −2.3 × 10⁻³ (with ℬ replaced by −ℬ the
deficit was −0.648 at both resolutions tried); the inner sphere trapped with μ − a² ≥ 0.332; and the diamond at R ≥
2.59, untrapped. On Σ_τ0, τ0 = −a + 0.02, the packet lay at R ∈ [1.861, 3.431], between the seed's horizon 0.907 and
the shell's inner edge 3.825. The outgoing ray of {u ≤ u1} from R = 7.505 at v = 0 kept R − b ≥ 0.9951 on [τ0, τ_end],
the least value at τ0, while the cone through R = 5 at v = 0 met Σ_τ0 at R − b = −4.09. Along the inner edge of the
packet, R(u2, v) − √μ(u2, v) ≥ 0.6127 at the three resolutions; with the amplitude of the shell raised to 16 the edge
was trapped, the gap −0.617. A discretisation for one other choice of the outgoing family's characteristic data
converged on a rectangle reaching Σ_τ0. No proof uses these observations.

### The phases and the transports {#sec:two-dust-phases}

From here on the background is that of [[prop:two-dust-background]] on Ω₂, in the double-null coordinates of
[[def:two-dust-data]] and the chart X = (τ, x) of [[lem:two-dust-domain]]. The ingoing phase is v, the advanced time
of the data on 𝒞_out (on Σ_τ0, v = τ0 + R), and the outgoing phase is u. Both are exact eikonals of g0, being
double-null coordinates: g0⁻¹(dv, dv) = g0⁻¹(du, du) = 0, while g0⁻¹(dv, du) = −e^(−2σ). The normalisation of u is any
λ-independent one; that of [[def:two-dust-data]] is fixed for definiteness. The generators are

    ℓ_in := g0⁻¹ dv = −e^(−2σ) ∂_u = −e^(−ψ) L0,      ℓ_out := g0⁻¹ du = −e^(−2σ) ∂_v,                     {#eq:two-dust-generators}

the first form in the coordinates (u, v, ϑ, φ1, φ2) and the second in the chart X ([[lem:two-dust-domain]] (d)): the
ingoing generator is the operator L0 of [[sec:background]] up to the smooth bounded factor e^(−ψ).

The outgoing generator has a variable radial speed. In the coordinates (v, R) of [[eq:two-dust-chart]] the second null
direction of the round spheres is ∂_v + y ∂_R, y := e^ψ f/2, since −e^(2ψ) f + 2 e^ψ y = 0. With ∂_v|_R = ∂_τ and
∂_R|_v = −∂_τ + x̂·∂_x it is (1 − y)(∂_τ + c_out x̂·∂_x), so

    ℓ_out = ℓ_out(τ) Z_out,      Z_out := ∂_τ + c_out x̂·∂_x,      c_out := y/(1 − y),      y = e^ψ f/2 ∈ (−∞, 1/2],
                                                                                                     {#eq:two-dust-speed}
with ℓ_out(τ) := dτ(ℓ_out). Here y ≤ 1/2 because e^ψ ≤ 1 and f ≤ 1, so c_out ∈ (−1, 1], and c_out < 0 exactly where f
< 0, that is where the spheres are trapped. In particular c_out(a) < 0 on {R = a} ([[prop:two-dust-background]] (c)).
Since a null vector is never tangent to a spacelike slice, ℓ_out(τ) ≠ 0, and on the compact Ω₂, |ℓ_out(τ)| ≥ c > 0.

**Lemma {#lem:two-dust-transport}** (Transport along both generators.) Let c be a smooth function on Ω₂ and Z := ∂_τ +
c x̂·∂_x. For φ on A(τ), with the flat measures on A(τ) and on its boundary spheres,

    ∂_τ ‖φ‖² = 2 ⟨φ, Zφ⟩ + ∫_(A(τ)) div(c x̂) φ² + (b′ − c(b)) ∫_(|x|=b) φ² + c(a) ∫_(|x|=a) φ².                {#eq:two-dust-transport}

For c = −1, Z = L0 and this is the identity of the proof of [[lem:transport]]. For c = c_out, b′ − c_out(b) < −2 + 1 =
−1 and c_out(a) < 0, so both boundary terms are nonpositive, as for L0, and if Z_out φ − c′ φ = f, with c′ a bounded
function or matrix, then

    ‖φ(τ)‖ ≤ e^(C (τ − τ0)) (‖φ(τ0)‖ + ∫_(τ0)^τ ‖f(s)‖ ds),      C := max(0, sup_(Ω₂) (c′ + ½ div(c_out x̂))),

c′ read as the largest eigenvalue of its symmetric part when it is a matrix.

*Proof.* ∂_τ ‖φ‖² = 2⟨φ, ∂_τ φ⟩ + b′ ∫_(|x|=b) φ², and ∂_τ φ = Zφ − c x̂·∂_x φ. By the divergence theorem on A(τ), with
outer normal x̂ on {|x| = b} and −x̂ on {|x| = a}, −2 ∫ c φ x̂·∂_x φ = −∫ c x̂·∂_x(φ²) = −∫_(|x|=b) c φ² + ∫_(|x|=a) c φ² +
∫ div(c x̂) φ². This is [[eq:two-dust-transport]]. With Zφ = c′ φ + f it gives ∂_τ ‖φ‖² ≤ 2 ‖φ‖ ‖f‖ + 2C ‖φ‖², hence
∂_τ ‖φ‖ ≤ ‖f‖ + C ‖φ‖, and Gronwall's lemma concludes. For c = −1, div(−x̂) = −3/r in R⁴. ∎

If the inner sphere were untrapped, c_out(a) would be positive and the boundary term at R = a would have the wrong sign:
the trapped inner sphere of [[prop:two-dust-background]] (c) is what both transports need.

**Lemma {#lem:two-dust-commutator}** (The commutator with a generator.) Let g0 be a round double-null metric
[[eq:two-dust-metric]] and L_in := ℓ_in·∂ = −e^(−2σ) ∂_u. For every function f,

    [□_(g0), L_in] f = a_in □_(g0) f + M_in(L_in f) + N_in f,      a_in := 2 L_in(R)/R,
    M_in F := 4 e^(−4σ) σ_v ∂_u(e^(2σ) F) + 4 e^(−4σ) (R_u/R) ∂_v(e^(2σ) F),                                 {#eq:two-dust-commutator}

with N_in a first-order operator with smooth coefficients; the mirror identity holds for L_out := ℓ_out·∂ = −e^(−2σ) ∂_v
with u and v exchanged. The same holds for □̃ := g0^(ab) ∂_a∂_b in the chart X, with another first-order N_in.

*Proof.* In the coordinates (u, v) and the angles,

    □_(g0) f = −e^(−2σ) (2 f_uv + 3 R⁻¹ (R_u f_v + R_v f_u)) + R⁻² Δ_(S³) f.

Put ρ := −e^(−2σ), so L_in = ρ ∂_u, and compute □(ρ f_u) − ρ ∂_u □f. The third derivatives cancel, as in any
commutator of a second-order with a first-order operator. Of the second derivatives, the terms in f_uv are
−2e^(−2σ) ρ_u f_uv − 2ρ ρ_u f_uv = 0, since ρ = −e^(−2σ); the terms 3R⁻¹(R_u f_uv + R_v f_uu) cancel between the two
sides; −2e^(−2σ) ρ_v f_uu = −4e^(−4σ) σ_v f_uu remains; and the angular part gives −ρ ∂_u(R⁻²) Δf = (2ρR_u/R) R⁻² Δf =
a_in R⁻² Δf, because the angular inverse metric R⁻² γ̂⁻¹ changes along ∂_u by a multiple of itself: the generator is
shear-free. Writing R⁻² Δf = □f + e^(−2σ)(2 f_uv + first order) gives a_in □f − 4e^(−4σ)(R_u/R) f_uv + first order. The
two remaining second derivatives, −4e^(−4σ) σ_v f_uu − 4e^(−4σ)(R_u/R) f_uv, carry the generator's index u; as f_u =
−e^(2σ) L_in f, they are M_in(L_in f). Finally □̃f = □_(g0) f + H0·∂f with H0^ρ := g0^(ab) Γ[g0]^ρ_ab smooth, and the
commutator of L_in with the first-order operator H0·∂ is of first order. ∎

So if ℓ_K·dφ = F along a generator, then Ψ := □̃φ satisfies the transport

    L_K Ψ + a_K Ψ = □̃F − M_K(F) − N_K φ,      K ∈ {in, out},                                              {#eq:two-dust-psi}

the form of [[eq:ue-psi]]: on Vaidya, ℓ_in = −L0, R = r and a_in = 2/r. Every second derivative of φ is a combination,
with smooth λ-independent coefficients, of L_K F, ∂_x F, dφ and the spatial Hessian ∂_x² φ, since L_K is transverse to
the slices; and ∂_x² φ satisfies L_K(∂_x² φ) = ∂_x² F + [L_K, ∂_x²] φ, the commutator having the smooth λ-independent
coefficients ∂_x ℓ_K.

### The approximant {#sec:two-dust-approximant}

The two-scale operator with two phases is Ric^H with every ∂_a replaced by ∂_a + λ⁻¹ (∂_a v) F1 + λ⁻¹ (∂_a u) F2, as in
[[def:two-scale]]; we write R[G] for it. It contains no explicit θ1, θ2, so

    R[G(·, · + c1, · + c2)](X, θ1, θ2) = R[G](X, θ1 + c1, θ2 + c2)                                        {#eq:two-dust-shift}

for all constants c1, c2, and the form (b) of [[lem:phase-shift-symmetry]], with phases u_K = ϕ_K + λ Φ_K, holds with
the same proof. For a profile G = g0 + λ g1 + Σ_(j≥2) λ^j g_j we write R[G] = λ⁻¹ R^(−1) + R^(0) + λ R^(1) + ….

The waves are

    W_in := W_TT^in + χ_in dv ⊗ dv,      W_out := W_TT^out + χ_out du ⊗ du,                                {#eq:two-dust-waves}

with W_TT^in, W_TT^out the ingoing and outgoing waves of [[def:two-dust-data]], and χ_in(X, θ1), χ_out(X, θ2) second
harmonics fixed below. Their Cartesian components are smooth on Ω₂ × T², the axes included ([[lem:waves]] (a)).

**Definition {#def:two-dust-approximant}** (Two-phase approximant.) Let N ≥ 1, K and k be integers. A two-phase
approximant with N stages is a metric g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j], with two-phase profiles g_j bounded with
all their (X, θ1, θ2)-derivatives independently of λ. It is of order K at regularity k if:

- (E1₂) g1 = ⟨g1⟩ + g1^in + g1^out, with g1^in a profile in (X, θ1) alone and g1^out in (X, θ2) alone, each of zero
  mean, and g1^in(ℓ_in, ·) = 0, g1^out(ℓ_out, ·) = 0;
- (E2₂) the coefficient R^(0) of λ⁰ in the two-scale expansion of Ric^H(g_app) vanishes identically in (X, θ1, θ2);
- (E3) |Ric^H(g_app)|_k (τ) ≤ C_R λ^K for every τ ∈ [τ0, τ_end], with C_R independent of λ.

**Lemma {#lem:two-dust-stage-zero}** (Stage 0 with two phases.) Let q be a two-phase profile and χ_in, χ_out smooth of
zero mean. In the two-scale expansion of R[g0 + λ (W_in + W_out) + λ² q]:

(a) R^(−1) = 0;
(b) R^(0) = R^(0)_in + R^(0)_out − Ric(g0) + R^(0)_× + e^(−2σ) F1F2 q, where R^(0)_K is the coefficient of λ⁰ of
R[g0 + λ W_K], given by [[eq:leading-coefficient]] with v replaced by ϕ_K, and R^(0)_× is bilinear in (W_in, W_out)
and has only mixed harmonics;
(c) the mean of R^(0) is Ric(g0) − (𝒜/R³) dv ⊗ dv − (ℬ/R³) du ⊗ du, so it vanishes exactly when g0 solves the
two-null-dust equations with the fluxes [[eq:two-dust-fluxes]];
(d) the pure harmonics (n, 0) of R^(0) vanish except in the component dv ⊗ dv at n = ±2, where the coefficient is
−(ℓ_in + ½ □_(g0) v) F1χ_in − ¼ (|F1 W_TT^in|²_(g0) − ⟨|F1 W_TT^in|²_(g0)⟩), and likewise for (0, n) with du ⊗ du;
(e) on a mixed harmonic e^(i(n1 θ1 + n2 θ2)), q enters R^(0) as multiplication by −e^(−2σ) n1 n2, which does not vanish;
(f) the gauge field has D = O(λ), the coefficient of λ⁰ being Σ_K g0⁻¹(F_K W_K(ℓ_K, ·) − ½ dϕ_K tr_(g0) F_K W_K) = 0.

Hence, with χ_in the solution of zero mean of

    (ℓ_in + ½ □_(g0) v) F1χ_in = −¼ (|F1 W_TT^in|²_(g0) − ⟨|F1 W_TT^in|²_(g0)⟩),      χ_in = 0 on Σ_τ0,   {#eq:two-dust-chi}

χ_out the solution of the same transport along ℓ_out, with u, θ2 and W_TT^out, and q the profile of zero mean whose
mixed harmonics are the quotients of those of −R^(0)_× by −e^(−2σ) n1 n2, R^(0) ≡ 0. The transports are along the
generators, which reach Σ_τ0 inside Ω₂ ([[lem:two-dust-domain]] (d)), and χ_in, χ_out are smooth on Ω₂ × S¹, the axes
included, as in [[sec:stage-zero]].

*Proof.* (a) Second derivatives of g enter Ric^H only through −½ g^(ab) ∂_a∂_b g ([[sec:gauge]]), and the other terms
contain at most first derivatives, which are O(1). The λ⁻¹ part of −½ g^(ab) ∂_a∂_b (λ (W_in + W_out)) is
−½ λ⁻¹ Σ_(J,K) g0⁻¹(dϕ_J, dϕ_K) F_J F_K (W_in + W_out) = 0: g0⁻¹(dϕ_K, dϕ_K) = 0, and F1F2 (W_in + W_out) = 0.

(b) A term of order λ⁰ is linear in one W_K with at most one phase derivative, quadratic in the waves with two phase
derivatives, or linear in λ² q with two phase derivatives, the last only from the principal part, where it is
−½ g0^(ab) (2 ∂_a v ∂_b u) F1F2 q = e^(−2σ) F1F2 q, the terms with two derivatives in one phase vanishing as in (a). The
terms in which only W_K occurs are those of the expansion of R[g0 + λ W_K]. The proof of [[lem:leading-coefficient]]
uses of g0 only that dϕ_K is null and of the wave only W_K(ℓ_K, ·) = 0 and tr_(g0) W_K = 0; both hold here, W_TT^K
having only angular components and being traceless on the spheres ([[lem:waves]] (b)) and dϕ_K ⊗ dϕ_K being null and
transverse to ℓ_K. So R^(0)_K is given by [[eq:leading-coefficient]] with v replaced by ϕ_K. The remaining terms are
products of a function of θ1 of zero mean with a function of θ2 of zero mean, which have only mixed harmonics.

(c) By (b), the mean of R^(0) is Ric(g0) − ¼ ⟨|F1 W_in|²⟩ dv ⊗ dv − ¼ ⟨|F2 W_out|²⟩ du ⊗ du, the other terms of
[[eq:leading-coefficient]] being phase derivatives. As in the proof of [[prop:limit]], χ_K does not contribute, and the
computation there, which uses only that g0 is R² times the round metric on the spheres, gives ⟨|F1 W_TT^in|²_(g0)⟩ =
(4/3) A² env² R⁻³ and ⟨|F2 W_TT^out|²_(g0)⟩ = (4/3) A₂² env₂² R⁻³ ([[eq:wave-energy]]).

(d) The pure harmonics (n, 0) come from R^(0)_in alone. In the coordinates (u, v), ℓ_in = −e^(−2σ) ∂_u and □_(g0) v =
−3 e^(−2σ) R_u/R. The angular components of F1 W_TT^in are R^(1/2) times functions of (v, the angles, θ1), and Γ^C_uA
= (R_u/R) δ^C_A, while Γ^C_ua = 0 for a ∈ {u, v}; so ∇_(ℓ_in) F1 W_TT^in = −e^(−2σ)(½ − 2)(R_u/R) F1 W_TT^in and

    ∇_(ℓ_in) F1 W_TT^in + ½ (□_(g0) v) F1 W_TT^in = 0.

Since ∇_(ℓ_in) dv = 0, the χ_in term of [[eq:leading-coefficient]] is −(ℓ_in + ½ □_(g0) v)(F1χ_in) dv ⊗ dv, and the
quadratic term is a second harmonic in θ1, as in [[lem:stage-zero]] (d).

(e) e^(−2σ) F1F2 multiplies the harmonic (n1, n2) by e^(−2σ)(i n1)(i n2).

(f) D is computed as in the proof of [[lem:mean-leading]]: its coefficient of λ⁰ is g0^(ab) C⁽⁰⁾ρ_ab, with C⁽⁰⁾ now the
sum over K of the terms with F_K W_K and dϕ_K; it vanishes because W_K(ℓ_K, ·) = 0 and tr_(g0) W_K = 0. ∎

With χ_in = χ_out = 0 the mixed harmonics of R^(0) do not vanish: the two families interact at stage 0, and the
interaction is removed by q with no transport.

**Lemma {#lem:two-dust-nonresonance}** (No small divisors.) Let ḡ be a mean metric with ḡ − g0 = O(λ), and u_in, u_out
phases with u_in − v = O(λ), u_out − u = O(λ), ḡ⁻¹(du_K, du_K) = O(λ). A term λ^j q(X) e^(i(n1 u_in + n2 u_out)/λ) E of
the metric, E a constant symmetric array, first meets Ric^H at order j − 2, through −½ g^(ab) ∂_a∂_b only, as
multiplication by the symbol

    ½ ḡ⁻¹(n1 du_in + n2 du_out, n1 du_in + n2 du_out) = −e^(−2σ) n1 n2 + λ 𝔮(n1, n2),                      {#eq:two-dust-symbol}

𝔮 a quadratic form in (n1, n2) with smooth bounded coefficients. The leading part vanishes exactly on the pure
harmonics, and on every mixed harmonic |e^(−2σ) n1 n2| ≥ e^(−2σ) ≥ min_(Ω₂) e^(−2σ) > 0. So the mixed harmonics are
solved by division with no small divisors, and the division loses no derivative; the part λ 𝔮 is of the next order. For
any two radial phases f(v) and h(u) in place of v and u the leading symbol is −e^(−2σ) f′ h′ n1 n2.

*Proof.* With Φ := (n1 u_in + n2 u_out)/λ, ∂_a∂_b e^(iΦ) = (−∂_aΦ ∂_bΦ + i ∂_a∂_bΦ) e^(iΦ), so the term of order λ^(j−2)
of −½ g^(ab) ∂_a∂_b (λ^j q e^(iΦ) E) is ½ λ^(j−2) ḡ⁻¹(n1 du_in + n2 du_out, n1 du_in + n2 du_out) q e^(iΦ) E; every
other term of Ric^H has at most one derivative on the factor e^(iΦ) and is O(λ^(j−1)). Expanding, the symbol is
½ n1² ḡ⁻¹(du_in, du_in) + n1 n2 ḡ⁻¹(du_in, du_out) + ½ n2² ḡ⁻¹(du_out, du_out), and ḡ⁻¹(du_in, du_out) = g0^(uv) + O(λ)
= −e^(−2σ) + O(λ). For radial phases f(v), h(u), g0^(ab) ∂_a f ∂_b h = −e^(−2σ) f′ h′. ∎

In the (u, v)-plane the null cone of g0 is the pair of lines du = 0 and dv = 0, so every combination n1 dv + n2 du with
n1 n2 ≠ 0 is timelike or spacelike, with g0⁻¹-length bounded below. This is Touati's strong coherence condition
[Tou24, (1.18), p. 9], min |g0⁻¹(dz, dz)| ≥ c over the combinations z of the phases that occur, for all mixed
combinations at once. Two ingoing phases would be resonant: their combinations are all null, and the symbol vanishes on
every harmonic.

**Remark {#rem:two-dust-symbol}** (The constant of the division.) The constant of [[lem:two-dust-nonresonance]] is
min_(Ω₂) e^(−2σ), which is positive on the compact Ω₂ but degenerates with the time spent inside the hole. With
e^(2σ) = −e^ψ R_u ([[lem:two-dust-domain]]), along a line of constant u, d(ln e^(−2σ))/dv = −ψ_v − R_uv/R_u = −ψ_v −
e^ψ μ/R³. In {u ≥ u2}, where ψ depends on v alone ([[prop:two-dust-background]] (a)), this gives on R ≥ a

    d(ln e^(−2σ))/dv ≥ −ψ′(v) − μ_max/a³,      μ_max := max_(Ω₂) μ,

an exponential lower bound for the constant in terms of the time spent in Ω₂ ∩ {u ≥ u2}. The constants of
[[thm:two-dusts]] depend on it, which is harmless for a fixed T.

**Remark {#rem:two-dust-symbol-values}** (Numerical observation.) On the discrete background of [[rem:two-dust-example]],
|g0⁻¹(dv, du)| = e^(−2σ), with v the advanced time on 𝒞_out and u normalised as there, had least value 0.181, 0.138 and
0.148 off the trapped region (R² ≥ 1.5 μ) at 40, 80 and 160 steps per unit, stable to ten per cent and not monotone in
the resolution. Its least value over every cell, 0.131, 0.071 and 0.042, did not converge: each finer grid reached
further into the strip near R = a at late v, where the double-null grid thins. Integrated along the outgoing rays of
{u ≥ u2}, where ψ and μ depend on v alone, its values on R = a were 0.892, 0.446, 0.240, 0.134, 0.0758, 0.0434,
0.0266, 0.0212, 0.0183 and 0.0156 at v = 0.5, 1, 1.5, …, 4.5 and 4.9, agreeing with the grids at v = 0.5, 1, 1.5 to one
per cent (the coefficients at 80 and 160 steps to two per cent), decreasing at a rate per unit v of 1.4, falling to 1.1 by v = 3 and to 0.3–0.5 once the shell had raised the
mass; the analytic rate of [[rem:two-dust-symbol]] is μ_max/a³ ≈ 10.5 there. No proof uses these observations.

**Lemma {#lem:two-dust-stages}** (The stages with two phases.) Let the unknowns be the means m_j (j ≥ 1), the phases
φ_j^in, φ_j^out (j ≥ 1) and the profiles ĝ_j(X, θ1, θ2) of zero mean (j ≥ 2). Put ḡ := g0 + Σ_(j=1)^N λ^j m_j,
u_in := v + Σ_(j=1)^N λ^j φ_j^in, u_out := u + Σ_(j=1)^N λ^j φ_j^out, W := W_in + W_out,

    G := ḡ + λ W + Σ_(j=2)^(N+1) λ^j ĝ_j(X, θ1, θ2),      g_app := G(X, u_in/λ, u_out/λ),                     {#eq:two-dust-ansatz}

and expand R_u[G] = Σ_m λ^m ℛ^(m), R_u the two-scale operator with the phases u_in, u_out. Then

    ḡ⁻¹(du_K, du_K) = Σ_(j≥1) λ^j e_j^K,      e_j^K = 2 ℓ_K·dφ_j^K − m_j(ℓ_K, ℓ_K) − q_j^K,

with q_j^K a polynomial in (m_i, dφ_i^K), i < j, as in [[eq:eikonal-coefficients]], once per phase; and
ḡ⁻¹(du_in, du_out) = g0^(uv) + λ c_1 + O(λ²), c_1 := ℓ_in·dφ_1^out + ℓ_out·dφ_1^in − m1(ℓ_in, ℓ_out), does not vanish.

(a) ℛ^(−1) = 0, and ℛ^(0) is the coefficient of λ⁰ of R[g0 + λ W + λ² ĝ_2] minus ½ Σ_K e_1^K F_K² W_K.
(b) For m ≥ 1,

    ℛ^(m) = T̂ ĝ_(m+1) + e^(−2σ) F1F2 ĝ_(m+2) − ½ Σ_K e_(m+1)^K F_K² W_K + 𝒲(m_m, φ_m^in, φ_m^out) + 𝒦_m,      {#eq:two-dust-stage-m}

where T̂ is linear, and on profiles Y of the harmonics of θ_K alone Π_K T̂ Y = −(ℓ_K·∂_X) F_K Y + Π_K ℳ Y, Π_K the
projection onto those harmonics and ℳ algebraic in X and of first order in (θ1, θ2), with smooth bounded coefficients
built from g0, ϕ_in, ϕ_out and W; 𝒲 is as in [[lem:first-entry]], linear in m_m to second order, with mean part −½ □̃ m_m
plus terms of first order, and linear in φ_m^K through dφ_m^K and □̃φ_m^K, the latter only as −½ (□̃φ_m^K) F_K W_K; and
𝒦_m depends only on the earlier stages and on the mixed harmonics of ĝ_(m+1). Only the mixed harmonics of ĝ_(m+2) enter
ℛ^(m).
(c) Each stage m ≥ 1 is the system

    (a′) −½ □̃ m_m + B̄·∂m_m + C̄ m_m = 𝒮_m − ⟨𝒲_φ⟩ − ⟨T̂ ĝ_(m+1)⟩,
    (b′) ℓ_K·dφ_m^K = ½ m_m(ℓ_K, ℓ_K) + ½ q_m^K,      K ∈ {in, out},
    (c′) Π_K T̂ ĝ_(m+1) = −Π_K (𝒲 + 𝒦_m),      K ∈ {in, out},
    (d′) e^(−2σ) F1F2 ĝ_(m+2) = −Π_mix (𝒲 + 𝒦_m + T̂ ĝ_(m+1)),                                             {#eq:two-dust-stage-system}

with 𝒮_m := −⟨𝒦_m⟩, 𝒲_φ := 𝒲(0, φ_m^in, φ_m^out) and Π_mix the projection onto the mixed harmonics: a wave equation
for the mean, a transport along its own generator for each phase, a transport along its own generator for the pure
harmonics of each family, and a division for the mixed harmonics. Given everything of the earlier stages, smooth, it has
a unique smooth solution on Ω₂ with data (m_m, ∂_τ m_m), φ_m^in, φ_m^out and the pure harmonics of ĝ_(m+1) on Σ_τ0;
the mixed harmonics take no data.

*Proof.* The expansions of ḡ⁻¹(du_K, du_K) are those of [[eq:eikonal-coefficients]] for each phase. For the cross
contraction, ḡ⁻¹ = g0⁻¹ − λ m1^♯ + O(λ²) and du_K = dϕ_K + λ dφ_1^K + O(λ²) give g0^(uv) + λ (ℓ_in·dφ_1^out +
ℓ_out·dφ_1^in − m1(ℓ_in, ℓ_out)) + O(λ²).

(a) and (b) follow from the weight count of the proof of [[lem:first-entry]], in which each phase derivative λ⁻¹ (∂ϕ_K)
F_K has weight −1. A factor of stage m + 1 reaches order m in the ways listed there: the pure harmonics of ĝ_(m+1) hit by
one phase derivative of their own phase, which gives T̂ (a phase derivative of the other phase annihilates them); and
m_(m+1), dφ_(m+1)^K in the phase contractions, which give −½ e_(m+1)^K F_K² W_K. In addition, ĝ_(m+2) hit by two phase
derivatives reaches order m, through the principal part only, as −½ Σ_(J,K) g0⁻¹(dϕ_J, dϕ_K) F_J F_K ĝ_(m+2) =
e^(−2σ) F1F2 ĝ_(m+2) ([[lem:two-dust-nonresonance]]); this vanishes on the pure harmonics. The mixed harmonics of
ĝ_(m+1) hit by one phase derivative reach order m too; they were fixed at stage m − 1 by (d′) and belong to 𝒦_m. The
cross contraction ḡ⁻¹(du_in, du_out) = g0^(uv) + Σ_(j≥1) λ^j c_j contributes at order m the terms −c_j F1F2 ĝ_(m+2−j),
which have mixed harmonics only: for j = 1 they are part of T̂, defined at G1 = g0 + λ (m1 + W) with the phases v + λ
φ_1^in and u + λ φ_1^out as in [[def:first-stage-operator]]; for j = m ≥ 2 they are linear in m_m and dφ_m^K and part
of 𝒲; the others are part of 𝒦_m. The form of T̂ on pure harmonics of θ_K is that of [[lem:first-stage-operator]], with ℓ_K and ϕ_K: the
principal term gives −(ℓ_K·∂_X) F_K Y − ½ (□̃ϕ_K) F_K Y − ½ e_1^K F_K² Y, and e_1^K = 0. The products of such Y with the
other family's wave, for instance ½ Y(ℓ_J, ℓ_J) F_J² W_J with J ≠ K, have mixed harmonics; they are the mixed part of
T̂ ĝ_(m+1), which (d′) carries.

(c) (b′) is e_m^K = 0. The mean of [[eq:two-dust-stage-m]] is (a′), its pure harmonics of θ_K are (c′), and its mixed
harmonics are (d′), which, by [[lem:two-dust-nonresonance]], is solved pointwise in X by division by −e^(−2σ) n1 n2.
⟨T̂ ĝ⟩ contains no X-derivative of ĝ and ⟨𝒲_φ⟩ only dφ_m^K. For Z_K := F_K Π_K ĝ_(m+1), (c′) is the transport −(ℓ_K·∂_X)
Z_K + ℳ′_K Z_K = (source) along ℓ_K, with ℳ′_K a bounded operator on profiles of zero mean. Its source contains
□̃φ_m^K, and Ψ_m^K := □̃φ_m^K satisfies the transport [[eq:two-dust-psi]] along ℓ_K with F = ½ (m_m(ℓ_K, ℓ_K) + q_m^K),
whose □̃F contains □̃ m_m from (a′). The system for (m_m, φ_m^in, φ_m^out, Ψ_m^in, Ψ_m^out, Z_in, Z_out) is linear with
smooth coefficients and closes without loss, m_m and φ_m^K in H^(s+1), Ψ_m^K and Z_K in H^s, by the Picard iteration of
the proof of [[lem:stage-system]]: the mean by [[lem:linear-wave]] on Ω₂, the transports along ℓ_in by [[lem:transport]]
(ℓ_in = −e^(−ψ) L0) and along ℓ_out by [[lem:two-dust-transport]], both generators reaching Σ_τ0 inside Ω₂
([[lem:two-dust-domain]] (d)). Then (d′) gives the mixed harmonics of ĝ_(m+2), which involve one X-derivative of the
mixed harmonics of ĝ_(m+1) through T̂: one derivative per stage, harmless for smooth data and finitely many stages.
[[lem:linear-wave]] holds on Ω₂ with the same proof, which uses of Ω only [[lem:domain]] (e) and its shape. ∎

**Theorem {#thm:two-dust-approximant}** (The approximant to every order, two phases.) For every N ≥ 1 and every smooth
choice of stage data there are two-phase profiles g1, …, g_N, independent of λ, such that g_app = g0 + λ [g1] +
Σ_(j=2)^N λ^j [g_j] is a two-phase approximant with N stages of order K = N − 1 at every regularity k
([[def:two-dust-approximant]]), with

    g1 = m1 + W_in(X, θ1 + φ_1^in(X)) + W_out(X, θ2 + φ_1^out(X)),

W_in and W_out as in [[eq:two-dust-waves]] with χ_in, χ_out of [[eq:two-dust-chi]], and the background g0 of
[[prop:two-dust-background]]. The stage data are those of [[lem:two-dust-stages]] (c) on Σ_τ0, for m = 1, …, N.

*Proof.* Solve stage 0 by [[lem:two-dust-stage-zero]], with ĝ_2's mixed harmonics the profile q there, and the stages m
= 1, …, N by [[lem:two-dust-stages]] (c), keeping in [[eq:two-dust-ansatz]] the pure harmonics of ĝ_(N+1) and the mixed
harmonics of ĝ_j for j ≤ N + 1. By [[lem:two-dust-stages]] (a)–(b), ℛ^(m) = 0 for m ≤ N − 1, so R_u[G] is λ^N times a
profile bounded uniformly in λ. Rewriting with the fixed phases v and u, the Taylor expansion in λΦ_K, Φ_K := Σ_(j≥2)
λ^(j−2) φ_j^K, about θ_K + φ_1^K, as in the proof of [[thm:approximant]], gives profiles g_j(X, θ1, θ2) with the stated
g1 and a remainder that changes Ric^H by O(λ^(N−1)) in |·|_k. (E1₂) holds because W_K(ℓ_K, ·) = 0 and ⟨g1⟩ = m1. (E2₂)
holds by the form (b) of [[eq:two-dust-shift]] with Φ_K = φ_1^K + λΦ_K: the coefficient of λ⁰ of R[G(·, · + Φ)] is
R^(0) of g_app, and it equals ℛ^(0)(X, θ1 + φ_1^in, θ2 + φ_1^out) = 0, since ℛ^(−1) = 0. (E3) holds with K = N − 1. ∎

[[thm:approximant]] is the case W_out = 0.

