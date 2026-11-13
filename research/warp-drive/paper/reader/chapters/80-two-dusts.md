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

### The uniform estimate {#sec:two-dust-uniform}

Let g_app be a two-phase approximant ([[def:two-dust-approximant]]), F := −Ric^H(g_app), and

    ℓ_app^K := g_app⁻¹ dϕ_K,   s_K(w) := w(ℓ_K, ℓ_K),   G1^K := [F_K g1],   G2^K := [F_K² g1],   Y_K := [F_K g1 + λ F_K g2],
    c_in := G1^out(ℓ_in, ℓ_in),   c_out := G1^in(ℓ_out, ℓ_out),   □̃_app := g_app^(ab) ∂_a∂_b,   □̃ := g0^(ab) ∂_a∂_b,

for K ∈ {in, out}, with g1, g2 the first two profiles of g_app. The remainder w is decomposed as

    w = h + φ_in Y_in + φ_out Y_out,                                                                    {#eq:two-dust-decomposition}

with φ_in(X), φ_out(X) fields fixed in [[lem:two-dust-phases]], Ψ_K := □̃φ_K, and the energy is

    𝒩₂(τ) := Σ_(j≤k) λ^j (‖∂^j ∂h‖ + Σ_K (‖∂^j Ψ_K‖ + ‖∂^j ∂φ_K‖ + λ ‖∂^j ∂_x² φ_K‖)) + ‖h‖ + Σ_K ‖φ_K‖,       {#eq:two-dust-energy}

the norms those of [[ch:inequalities]] on the slices Σ_τ = A(τ) of Ω₂.

**Theorem {#thm:two-dust-uniform}** (Uniform existence with two phases.) Fix k = 6 and K ≥ 6. Let g_app be a two-phase
approximant with N stages of order K at regularity k, with the constant C_R in (E3), and let g be a Cauchy datum on Σ_τ0
for Ric^H(g) = 0 with w := g − g_app satisfying (E4) of [[thm:uniform-existence]], Data(w) ≤ C_D λ^K. There are λ0 > 0
and M, depending on Ω₂, k, K, C_R, C_D and the bounds on the profiles but not on λ, such that for 0 < λ ≤ λ0 the
solution g of Ric^H(g) = 0 with these data exists on Ω₂, is unique there among C² solutions with |g − g0| ≤ ε1 on Ω₂,
is smooth if the data are, and

    w = h + Σ_K φ_K Y_K,      𝒩₂(τ) ≤ M λ^K   on [τ0, τ_end].                                              {#eq:two-dust-remainder}

In particular |w| ≤ M λ^(K−3) and |∂w| ≤ M λ^(K−4) on Ω₂, |g − g0| ≤ C λ and |∂g| ≤ C.

With W_out = 0 this is [[thm:uniform-existence]], with φ_out = 0. The proof is that of [[thm:uniform-existence]] with
two phase shifts. We collect the structure of the linearisation, define the phase shifts, write the equation for h and
its ℓ_in ⊗ ℓ_in component, and then go through the eight steps.

**Lemma {#lem:two-dust-facts}** (The linearisation with two phases.) Let P(w) := (d/ds) Ric^H(g_app + s w) at s = 0, and
for g := g_app + w let P_g be P with its principal part −½ g_app^(ab) ∂_a∂_b replaced by −½ g^(ab) ∂_a∂_b, so that
Ric^H(g_app + w) = 0 reads P_g(w) = F + 𝒬(w), 𝒬(w) the terms of second and higher order in (w, ∂w) other than the
principal part. Then:

(F1) P(w) = −½ g_app^(ab) ∂_a∂_b w + ½ λ⁻¹ Σ_K s_K(w) G2^K + B·∂w + C·w, with B and C two-phase profiles: there is no
term of order λ⁻², and one of order λ⁻¹ for each family.

(F2) For φ(X),

    P_g(φ Y_K) = φ [T1^K] − λ⁻¹ (ℓ_app^K·dφ) G2^K − ½ (□̃_app φ) G1^K − ½ λ (□̃_app φ) [F_K g2] + B1^K·dφ + C1^K φ
                 + 𝒬_φ^K,

with T1^K, B1^K, C1^K bounded two-phase profiles and |𝒬_φ^K| ≤ C |w| (λ⁻² |φ| + λ⁻¹ |dφ| + |d²φ|), likewise for
derivatives in the scaled norms, the second derivatives of φ in 𝒬_φ^K multiplying Y_K. The term of order λ⁻¹ contains
no derivative of φ along the other family's generator.

(F3) P(Y_K) = [T1^K], a bounded profile.

(F4) G1^in(ℓ_in, ·) = G2^in(ℓ_in, ·) = 0 and G1^out(ℓ_out, ·) = G2^out(ℓ_out, ·) = 0; c_in and G2^out(ℓ_in, ℓ_in) are
bounded profiles in θ2 alone, c_out and G2^in(ℓ_out, ℓ_out) in θ1 alone; and |ℓ_app^K − ℓ_K| ≤ C λ. For the
approximant of [[thm:two-dust-approximant]], c_in = e^(−4σ) [F2 χ_out] and G2^out(ℓ_in, ℓ_in) = e^(−4σ) [F2² χ_out], at
the phase θ2 + φ_1^out, and the oscillating part of ℓ_app^in − ℓ_in at order λ is λ e^(−2σ) [χ_out] ℓ_out; the mirror
statements hold with in and out exchanged.

(F5) With q := g0^(ττ)/g^(ττ) and c^(ab) := g0^(ab) − q g^(ab), c^(ττ) = 0 and

    c^(ab) = (g0^(ab) (g^(ττ) − g0^(ττ)) − g0^(ττ) (g^(ab) − g0^(ab)))/g^(ττ),

so |c| ≤ C |g⁻¹ − g0⁻¹| ≤ C (λ + |w|); g0^(ττ) ≤ −1 on Ω₂, so g^(ττ) ≤ −½ for |g − g0| small. For every h,
□̃ s_K(h) = (□̃h)(ℓ_K, ℓ_K) + 2 g0^(ab) ∂_a(ℓ_K ⊗ ℓ_K)·∂_b h + h·□̃(ℓ_K ⊗ ℓ_K).

(F6) If ℓ_K·dφ_K = ½ 𝒫 s_K(h), then Ψ_K satisfies L_K Ψ_K + a_K Ψ_K = ½ □̃ 𝒫 s_K(h) − ½ M_K(𝒫 s_K(h)) − N_K φ_K
([[eq:two-dust-psi]]); every second derivative of φ_K is a bounded combination of L_K 𝒫 s_K(h), ∂_x 𝒫 s_K(h), dφ_K and
∂_x² φ_K, and L_K(∂_x² φ_K) = ½ ∂_x² 𝒫 s_K(h) + (bounded) ∂_x² φ_K + (bounded) ∂_x φ_K.

(F7) ℓ_in = −e^(−ψ) L0 and ℓ_out = ℓ_out(τ) Z_out ([[eq:two-dust-generators]], [[eq:two-dust-speed]]), |ℓ_out(τ)| ≥
c > 0 on Ω₂, and the transport estimates [[lem:transport]] and [[lem:two-dust-transport]] hold for both, the boundary
terms having the sign they have for L0.

*Proof.* (F1) Second derivatives of g_app enter P only through ½ w^(ab) ∂_a∂_b g_app, w^(ab) := g_app^(ac) g_app^(bd)
w_cd, because second derivatives of g enter Ric^H(g) only through −½ g^(ab) ∂_a∂_b g. By [[eq:two-dust-chain]],
∂_a∂_b [λ g1] = λ⁻¹ Σ_(J,K) ∂_aϕ_J ∂_bϕ_K [F_J F_K g1] + O(1) = λ⁻¹ Σ_K ∂_aϕ_K ∂_bϕ_K [F_K² g1] + O(1), because F1F2 g1 =
0 by (E1₂); and ∂_a∂_b [λ^j g_j] = O(1) for j ≥ 2. Further w^(ab) ∂_aϕ_K ∂_bϕ_K = w(ℓ_app^K, ℓ_app^K) = s_K(w) +
O(λ) |w|, and that difference times λ⁻¹ goes into C. Every other term is linear in w or ∂w with coefficients built from
g_app and ∂g_app, which are bounded. This is the derivation of [[eq:ue-linearisation]], once per phase.

(F2) In −½ g^(ab) ∂_a∂_b(φ Y_K) = −½ φ g^(ab) ∂_a∂_b Y_K − g^(ab) ∂_aφ ∂_b Y_K − ½ (g^(ab) ∂_a∂_b φ) Y_K the first term
belongs to φ P_g(Y_K). By [[eq:two-dust-chain]], ∂_b Y_K = λ⁻¹ ∂_bϕ_K [F_K² g1] + Σ_J ∂_bϕ_J [F_J F_K g2] + [∂_b(F_K g1 +
λ F_K g2)], the λ⁻¹ term with the other phase vanishing because F_J F_K g1 = 0 for J ≠ K; so the second term is
−λ⁻¹ (g^(ab) ∂_aφ ∂_bϕ_K) G2^K + B·dφ, and g^(ab) ∂_bϕ_K = (ℓ_app^K)^a + O(|w|). In the third term g^(ab) = g_app^(ab) +
O(|w|), and Y_K = G1^K + λ [F_K g2]. The first-order terms of P_g give φ times their action on Y_K and terms in dφ. The
terms with a factor w form 𝒬_φ^K, and the bounds follow, each derivative of Y_K costing λ⁻¹. Finally φ P_g(Y_K) =
φ P(Y_K) + O(|w| λ⁻² |φ|), and P(Y_K) = [T1^K] by (F3).

(F3) Let G be the profile of g_app. Differentiating [[eq:two-dust-shift]] in c_K at c = 0, the linearisation of R at G
in the direction F_K G equals F_K R[G]. On a profile Z, P([Z]) = [λ⁻² P_(−2) Z + λ⁻¹ T Z + P_0 Z], where P_(−2) Z =
−g0⁻¹(dv, du) F1F2 Z = e^(−2σ) F1F2 Z, the terms −½ λ⁻² g_app⁻¹(dϕ_K, dϕ_K) F_K² Z being of order λ⁻¹ and kept in T.
Since F_K G = λ F_K g1 + λ² F_K g2 + O(λ³) and P_(−2) F_K g1 = 0 by (E1₂), the left side is T F_K g1 + P_(−2) F_K g2 +
O(λ). The right side is F_K(λ⁻¹ R^(−1) + R^(0)) + O(λ) = O(λ), since R^(−1) = −½ Σ_(J,K) g0⁻¹(dϕ_J, dϕ_K) F_J F_K g1 =
0 and R^(0) = 0 by (E2₂). So T F_K g1 + P_(−2) F_K g2 = O(λ), and P(Y_K) = [λ⁻¹ (T F_K g1 + P_(−2) F_K g2) + P_0 F_K g1 +
T F_K g2 + λ P_0 F_K g2] is bounded. Without the term λ F_K g2 in Y_K, the term λ⁻¹ P_(−2) F_K g2, which does not vanish
on the mixed harmonics of g2, would remain.

(F4) By (E1₂), G1^in = [F1 g1^in] and G2^in = [F1² g1^in] with g1^in(ℓ_in, ·) = 0, and they depend on θ1 alone; likewise
for out. For the approximant of [[thm:two-dust-approximant]], g1^out = W_out(X, θ2 + φ_1^out); W_TT^out has only
angular components, and (du ⊗ du)(ℓ_in, ℓ_in) = g0⁻¹(du, dv)² = e^(−4σ). Next, ℓ_app^in − ℓ_in = (g_app⁻¹ − g0⁻¹) dv =
−λ g0⁻¹(g1(ℓ_in, ·)) + O(λ²), and g1(ℓ_in, ·) = m1(ℓ_in, ·) + [χ_out] du(ℓ_in) du = m1(ℓ_in, ·) − e^(−2σ) [χ_out] du.

(F5) c^(ττ) = g0^(ττ) − (g0^(ττ)/g^(ττ)) g^(ττ) = 0, and the formula for c^(ab) is algebra. g0^(ττ) ≤ −1 − μ/R² by
[[lem:two-dust-domain]] (a). The last identity is the product rule.

(F6) is [[eq:two-dust-psi]] with F = ½ 𝒫 s_K(h), and the remarks after it. (F7) is [[sec:two-dust-phases]]. ∎

**Lemma {#lem:two-dust-phases}** (The phase shifts.) Let w be smooth on Ω₂ ∩ {τ ≤ τ*}. The system

    ℓ_K·dφ_K = ½ 𝒫 s_K(h),      h := w − Σ_J φ_J Y_J,      φ_K = 0 on Σ_τ0,      K ∈ {in, out},             {#eq:two-dust-phases}

has a unique solution (φ_in, φ_out) on Ω₂ ∩ {τ ≤ τ*}, and it is smooth.

*Proof.* Since s_K(h) = s_K(w) − Σ_J φ_J [Y_J(ℓ_K, ℓ_K)], with Y_out(ℓ_in, ℓ_in) = c_in + O(λ) and Y_in(ℓ_in, ℓ_in) =
O(λ) by (F4), and likewise for out, [[eq:two-dust-phases]] is a linear system of two transports along transversal null
generators, L0 φ_in = −½ e^ψ 𝒫 s_in(h) and Z_out φ_out = ½ 𝒫 s_out(h)/ℓ_out(τ) by (F7), coupled through the maps φ ↦
½ 𝒫([Y_J(ℓ_K, ℓ_K)] φ), which are bounded on L²(A(τ)) by (M1). By [[lem:transport]] and [[lem:two-dust-transport]], the
solution map of the two transports with zero data on a slab [τ1, τ1 + δ] is bounded from L¹ in τ to C in τ with values
in L²(A(τ)), so the map that takes (φ_in, φ_out) to the solutions with the sources computed from h is a contraction in
C([τ1, τ1 + δ]; L²(A(τ)))² for δ small independently of the data. Picard iteration on successive slabs gives a unique
solution on [τ0, τ*]. It is smooth, 𝒫 smoothing in x at fixed λ and (M6) giving the τ-derivatives. ∎

The estimates below use [[eq:two-dust-phases]] through s_K(h), which 𝒩₂ controls, the coupling being inside h. If the
phases were defined through s_K(w) instead, their sources would contain 𝒫([Y_J(ℓ_K, ℓ_K)] φ_J), with a coefficient that
oscillates at the mollifier's own scale, and λ^j ‖∂^j ∂ 𝒫(c φ_J)‖ with every derivative on c costs λ⁻¹ ‖φ_J‖ by (M2):
a power of λ would be lost.

**Lemma {#lem:two-dust-h}** (The equation for h.) With φ_K from [[eq:two-dust-phases]] and h := w − Σ_K φ_K Y_K, the
equation Ric^H(g_app + w) = 0 is

    −½ g^(ab) ∂_a∂_b h + B·dh + C·h = F + 𝒬(w) − Σ_K 𝒬_φ^K − ½ λ⁻¹ Σ_K ((1 − 𝒫) s_K(h)) G2^K
          + λ⁻¹ Σ_K ((ℓ_app^K − ℓ_K)·dφ_K) G2^K − Σ_K φ_K [T1^K] + ½ Σ_K (□̃_app φ_K) G1^K
          + ½ λ Σ_K (□̃_app φ_K) [F_K g2] − Σ_K (B1^K·dφ_K + C1^K φ_K).                                     {#eq:two-dust-h}

Every coefficient on the right is a bounded profile, except the one of order λ⁻¹ of each family, which multiplies
(1 − 𝒫) s_K(h) = O(λ ∂s_K(h)) by (M3); and |ℓ_app^K − ℓ_K| ≤ C λ.

*Proof.* Insert w = h + Σ_K φ_K Y_K in P_g(w) = F + 𝒬(w) and use (F1) for P_g(h) and (F2) for P_g(φ_K Y_K). The terms of
order λ⁻¹ are ½ λ⁻¹ Σ_K s_K(h) G2^K − λ⁻¹ Σ_K (ℓ_app^K·dφ_K) G2^K, and by [[eq:two-dust-phases]], ℓ_K·dφ_K = ½ 𝒫 s_K(h),
so they are ½ λ⁻¹ Σ_K ((1 − 𝒫) s_K(h)) G2^K − λ⁻¹ Σ_K ((ℓ_app^K − ℓ_K)·dφ_K) G2^K. Move them and the terms of (F2) to
the right side. ∎

**Lemma {#lem:two-dust-ell-ell}** (The ℓ_in ⊗ ℓ_in component.) With s := s_in(h),

    □̃ s = c1·dh + c0·h + Σ_K (c2^K·dφ_K + c3^K φ_K) − q c_in Ψ_out + q λ⁻¹ ((1 − 𝒫) s_out(h)) G2^out(ℓ_in, ℓ_in)
          + Σ_K c4^(K,ab) ∂_a∂_b φ_K − 2q F(ℓ_in, ℓ_in) − 2q 𝒬(w)(ℓ_in, ℓ_in) + 2q Σ_K 𝒬_φ^K(ℓ_in, ℓ_in)
          + Σ_(a,i) c^(ai) (∂_a∂_i h)(ℓ_in, ℓ_in),                                                         {#eq:two-dust-ell-ell}

with c0, c1, c2^K, c3^K bounded coefficients (profiles, and profiles times the function q of (F5)), c_in and
G2^out(ℓ_in, ℓ_in) bounded profiles oscillating in θ2, |c4^K| ≤ C λ, |c^(ai)| ≤ C (λ + |w|) and |∂c^(ai)| ≤ C (1 +
|∂w|), i spatial. 𝒬_φ^in(ℓ_in, ℓ_in) contains second derivatives of φ_in only with a factor λ |w|, and 𝒬_φ^out(ℓ_in,
ℓ_in) contains |w| |∂² φ_out|. The only coefficient of order λ⁻¹ multiplies (1 − 𝒫) s_out(h), which is O(λ ∂s_out(h))
by (M3). The mirror statement holds for s_out(h), with ℓ_out ⊗ ℓ_out, c_out and Ψ_in.

*Proof.* By (F5), □̃ s = (□̃h)(ℓ_in, ℓ_in) + c1·dh + c0·h, ℓ_in being smooth and λ-independent, and (□̃h)(ℓ_in, ℓ_in) =
q (g^(ab) ∂_a∂_b h)(ℓ_in, ℓ_in) + Σ c^(ai) (∂_a∂_i h)(ℓ_in, ℓ_in) + (first order), each term of c^(ab) ∂_a∂_b having a
spatial index because c^(ττ) = 0. By [[eq:two-dust-h]], (g^(ab) ∂_a∂_b h)(ℓ_in, ℓ_in) is −2 times the contraction of its
right side minus B·dh − C·h. Contract with ℓ_in ⊗ ℓ_in using (F4). Family in: G1^in(ℓ_in, ·) = G2^in(ℓ_in, ·) = 0
removes its term of order λ⁻¹, its (ℓ_app^in − ℓ_in) term and ½ (□̃_app φ_in) G1^in exactly, and ½ λ (□̃_app φ_in) [F1
g2](ℓ_in, ℓ_in) is O(λ |∂² φ_in|). Family out: −½ λ⁻¹ ((1 − 𝒫) s_out(h)) G2^out(ℓ_in, ℓ_in) survives, and gives the term
with q λ⁻¹; λ⁻¹ ((ℓ_app^out − ℓ_out)·dφ_out) G2^out(ℓ_in, ℓ_in) is O(|dφ_out|), since |ℓ_app^out − ℓ_out| ≤ C λ;
½ (□̃_app φ_out) c_in = ½ c_in Ψ_out + O(λ |∂² φ_out|), because □̃_app − □̃ = c′^(ab) ∂_a∂_b with |c′| ≤ C λ; and
½ λ (□̃_app φ_out) [F2 g2](ℓ_in, ℓ_in) is O(λ |∂² φ_out|). The rest is of first order or part of 𝒬_φ^K. In 𝒬_φ^K the
second derivatives of φ_K multiply Y_K, and Y_in(ℓ_in, ℓ_in) = λ [F1 g2](ℓ_in, ℓ_in), Y_out(ℓ_in, ℓ_in) = c_in + O(λ).
So φ_in drops out at the top order, φ_out enters only through Ψ_out with the bounded coefficient −q c_in, and no
coefficient of order λ⁻¹ remains other than the one stated. ∎

So s_in's equation has no large coefficient, and at the top order it is coupled to Ψ_out through a bounded profile
oscillating in θ2; the equation for s_out is the mirror image. This replaces [[lem:ell-ell]].

*Proof of [[thm:two-dust-uniform]].* The proof follows the eight steps of the proof of [[thm:uniform-existence]], on Ω₂,
with 𝒩₂ for 𝒩, [[eq:two-dust-h]] for [[eq:ue-h]], [[eq:two-dust-ell-ell]] for [[lem:ell-ell]], and (F6) for
[[lem:commutator-transport]]. Every constant depends on Ω₂, k, K and the profiles, never on λ.

**Step 1** (what 𝒩₂ controls). λ^j ∂^j(φ_K Y_K) is a sum of λ^i ∂^i φ_K times bounded profiles, and λ^i ‖∂^i φ_K‖ ≤ λ 𝒩₂
for 1 ≤ i ≤ k + 1, ‖φ_K‖ ≤ 𝒩₂. So, as in Step 1 there, |w|_(k+1) ≤ C 𝒩₂, ‖∂^i w‖_∞ ≤ C λ^(−3−i) 𝒩₂ for i ≤ 4, and
|∂w|_k ≤ C λ⁻¹ 𝒩₂.

**Step 2** (data). φ_K = 0 on Σ_τ0, so h = w there, and the derivatives of φ_K tangent to Σ_τ0 vanish; so ∂_τ φ_K =
½ 𝒫 s_K(h)/ℓ_K(τ) there by [[eq:two-dust-phases]], with no factor λ⁻¹, ℓ_in(τ) = −e^(−ψ) and |ℓ_out(τ)| ≥ c. The higher
τ-derivatives of h, φ_K and Ψ_K on Σ_τ0 follow from [[eq:two-dust-phases]], [[eq:two-dust-h]] and the equation for w, as
there, and 𝒩₂(τ0) ≤ C (C_D + C_R) λ^K.

**Step 3** (the bootstrap). Suppose 𝒩₂ ≤ 2M λ^K on [τ0, τ*]. Then |w| ≤ C M λ^(K−3) and |∂w| ≤ C M λ^(K−4), so for
λ ≤ λ0(M), |g − g0| ≤ ε1: the conclusions of [[lem:two-dust-domain]] (e) hold for g (Σ_τ and the lateral boundaries
spacelike, both generators transverse to Σ_τ), and |∂g| ≤ Λ with Λ independent of M.

**Step 4** (h). Apply ∂^α, |α| = j ≤ k, to [[eq:two-dust-h]], apply [[lem:energy]] to each component, and multiply by
λ^j. Term by term, with the exponent of λ each attains:

- (a) the commutator [∂^α, g^(ab)] ∂_a∂_b h: ‖∂^i g_app‖_∞ ≤ C λ^(1−i), so at most C 𝒩₂, and the w part at most
  C M λ^(K−4) 𝒩₂, with ∂^i w in L^∞ for i ≤ 4 and in L² for i ≥ 5, as in Step 4 there;
- (b) F: at most C_R λ^K, by (E3);
- (c) B·dh and C·h: at most C 𝒩₂, a derivative on a profile costing λ⁻¹ and the weight paying for it;
- (d) ½ λ⁻¹ ((1 − 𝒫) s_K(h)) G2^K: Σ_i λ^(i−1) ‖∂^i (1 − 𝒫) s_K‖ ≤ C Σ_i λ^i ‖∂^i ∂s_K‖ ≤ C 𝒩₂, by (M3), (M4), (M6);
- (e) λ⁻¹ ((ℓ_app^K − ℓ_K)·dφ_K) G2^K: ℓ_app^K − ℓ_K is λ times a profile, by (F4), so at most C 𝒩₂;
- (f) φ_K [T1^K], B1^K·dφ_K and C1^K φ_K: at most C 𝒩₂;
- (g) ½ (□̃_app φ_K) G1^K = ½ Ψ_K G1^K + ½ (c′^(ab) ∂_a∂_b φ_K) G1^K with |c′| ≤ C λ: the first at most C 𝒩₂, both Ψ_K
  being in 𝒩₂ at every level; the second by (F6), λ^(j+1) ‖∂^j ∂² φ_K‖ ≤ C 𝒩₂, since λ^(j+1) ‖∂^j L_K 𝒫 s_K‖ ≤ C λ^(j+1)
  ‖∂^j ∂s_K‖ by (M4), (M6) (no Bernstein inequality is needed here);
- (h) ½ λ (□̃_app φ_K) [F_K g2] = λ (Ψ_K + O(λ) ∂² φ_K) times a profile: at most C λ 𝒩₂;
- (i) 𝒬_φ^K: at most C M λ^(K−5) 𝒩₂ ≤ C M λ 𝒩₂, as K ≥ 6, its part |w| |∂² φ_K| at most C M λ^(K−4) 𝒩₂;
- (j) 𝒬(w): at most C λ⁻⁵ 𝒩₂² ≤ C M² λ^(2K−5) ≤ C M² λ^(K+1), as K ≥ 6, the worst term being quadratic in ∂w,
  |∂w ∂w|_k ≤ C λ⁻³ |∂w|_k², by the product bound of [[lem:sobolev]] at the top derivatives of w.

The g0 part of [∂^α, g^(ab)] and the commutator [∂_x², L_K] of Step 5 have smooth λ-independent coefficients and are at
most C 𝒩₂. So

    Σ_(j≤k) λ^j ‖∂^j ∂h(τ)‖ + ‖h(τ)‖ ≤ C (𝒩₂(τ0) + ∫_(τ0)^τ (𝒩₂ + C_R λ^K + C M² λ^(K+1))).

No term in (a)–(j) has a coefficient of order λ⁻¹ beyond (d), which (M3) pays for, and the two families enter (d)–(i)
once each.

**Step 5** (φ_in, φ_out). Each φ_K obeys its own transport [[eq:two-dust-phases]] with source ½ 𝒫 s_K(h): L0 φ_in =
−½ e^ψ 𝒫 s_in(h), the transport [[eq:ue-transport]] with the smooth bounded factor e^ψ, and Z_out φ_out =
½ 𝒫 s_out(h)/ℓ_out(τ). Apply ∂^α, |α| = j ≤ k: [Z_K, ∂^α] has smooth λ-independent coefficients and involves derivatives
of φ_K of order at most j, and λ^j ‖∂^α ∂ 𝒫 s_K‖ ≤ C λ^j ‖∂^(j+1) s_K(h)‖ ≤ C 𝒩₂ by (M1), (M4), (M6), s_K(h) =
h(ℓ_K, ℓ_K) with ℓ_K smooth. For λ ∂_x² φ_K use the transport of (F6), with source ½ ∂_x² 𝒫 s_K, and the Bernstein bound
(M2) on one spatial derivative: λ^(j+1) ‖∂^j ∂_x² 𝒫 s_K‖ ≤ C λ^j ‖∂^j ∂_x s_K‖ ≤ C 𝒩₂. [[lem:transport]] for φ_in and
[[lem:two-dust-transport]] for φ_out bound the φ-part of 𝒩₂(τ) by C (𝒩₂(τ0) + ∫_(τ0)^τ 𝒩₂). Without (M2) the transport of
∂_x² φ_K would need k + 2 derivatives of s_K.

**Step 6** (Ψ_in, Ψ_out). Apply ∂^α to the transport of (F6) for Ψ_in, along L_in = −e^(−ψ) L0 with the bounded
coefficient a_in, and [[lem:transport]]. In ½ □̃ 𝒫 s_in = ½ 𝒫 □̃ s_in + ½ [□̃, 𝒫] s_in insert [[eq:two-dust-ell-ell]].

- (a) 𝒫 of the terms of [[eq:two-dust-ell-ell]]: c1·dh, c0·h, c2^K·dφ_K and c3^K φ_K give at most C 𝒩₂. The coupling:
  ‖𝒫(q c_in Ψ_out)‖ ≤ C ‖Ψ_out‖ by (M1), and λ^j ‖∂^j 𝒫(q c_in Ψ_out)‖ ≤ C Σ_(i≤j) λ^i ‖∂^i Ψ_out‖ ≤ C 𝒩₂, each derivative
  on the profile q c_in costing λ⁻¹ and the weight paying for it. q λ⁻¹ ((1 − 𝒫) s_out) G2^out(ℓ_in, ℓ_in) is at most
  C 𝒩₂ by (M3); c4^K ∂² φ_K at most C 𝒩₂ by (F6); F, 𝒬(w) and 𝒬_φ^K give C_R λ^K, C M² λ^(K+1) and C M λ^(K−5) 𝒩₂; and
  Σ c^(ai) ∂_a∂_i h, written 𝒫 ∂_i(c ∂_a h) − 𝒫((∂_i c) ∂_a h) with the Bernstein bound on the ∂_i, is at most C λ⁻¹
  ‖c ∂h‖ + C ‖∂h‖ ≤ C 𝒩₂, as |c| ≤ C (λ + |w|); at level j only k + 1 derivatives of h occur, where taking the second
  derivatives directly would need k + 2.
- (b) [□̃, 𝒫] s_in: the terms with a spatial index are at most C ‖∂s_in‖ by the first form of (M5). The ττ term is
  rewritten through ∂_τ² s_in = (□̃ s_in − 2 g0^(τi) ∂_τ∂_i s_in − g0^(ij) ∂_i∂_j s_in)/g0^(ττ), g0^(ττ) ≤ −1, after
  which the second form of (M5) gains λ on every term of [[eq:two-dust-ell-ell]], the coupling included (at most C λ 𝒩₂),
  except Σ c^(ai) ∂_a∂_i h, which is written ∂_i(c ∂_a h) − (∂_i c) ∂_a h and bounded by the first form (the second
  form on them would cost a derivative at j = k, as in Step 6 there); and g0^(ab) (∂_a∂_b 𝒫 − 𝒫 ∂_a∂_b) s_in is at
  most C ‖∂s_in‖ by (M4), (M6).
- (c) −½ M_in(𝒫 s_in) and −N_in φ_in are of first order, at most C 𝒩₂.

So the Ψ_in-part of 𝒩₂(τ) is at most C (𝒩₂(τ0) + ∫ (𝒩₂ + C_R λ^K + C M² λ^(K+1))). The same holds for Ψ_out, along
Z_out with [[lem:two-dust-transport]], whose source contains 𝒫(q′ c_out Ψ_in). The coupling enters through ∫ 𝒩₂: Ψ_in
and Ψ_out are estimated together, which is why both are in 𝒩₂. Treated as a generic second derivative of φ_out, the
coupling term would lose a power of λ.

**Step 7** (closing). Steps 4–6 give 𝒩₂(τ) ≤ C2 (𝒩₂(τ0) + ∫_(τ0)^τ 𝒩₂ + (τ_end − τ0)(C_R λ^K + C M² λ^(K+1))), C2
independent of M and λ. Gronwall's lemma and Step 2 give 𝒩₂(τ) ≤ C3 ((C_D + 1 + C_R) λ^K + C M² λ^(K+1)). With M :=
C3 (C_D + 1 + C_R) + 1 and λ0 such that C3 C M² λ0 ≤ 1 and Step 3 holds, 𝒩₂ ≤ M λ^K < 2M λ^K, which improves the
bootstrap assumption. K ≥ 6 enters only in (i) and (j) of Step 4, through 2K − 5 ≥ K + 1 and K − 5 ≥ 1. 𝒩₂ is
continuous in τ for a smooth solution, so the set of τ* for which the assumption holds is open and closed in the
interval of existence.

**Step 8** (existence, continuation and uniqueness). This is Step 8 of the proof of [[thm:uniform-existence]] with Ω₂ in
place of Ω. Its part (i) uses of the background only that the extended approximant has spacelike slices {τ = const},
with lapse, shift and spatial metric bounded above and below, on a neighbourhood of the domain; here the profiles of
g_app, g0 among them, are extended from Ω₂ by Stein's operator ([[thm:std-sy-extension]]), and by continuity and the
compactness of Ω₂ ([[lem:two-dust-domain]] (a), (e)) this holds on a neighbourhood U of Ω₂ for λ small, with bounds
independent of λ; outside U the lapse, shift and spatial metric are interpolated convexly to (1, 0, δ) as there. Parts
(ii)–(iv) are unchanged, the slices being the annuli A(τ) of Ω. Uniqueness among C² solutions with |g − g0| ≤ ε1 is
the energy argument there, and with Step 7 the bootstrap continues, so the solution exists on all of Ω₂ with
[[eq:two-dust-remainder]]. The bounds after [[eq:two-dust-remainder]] follow from Step 1 as there: |w| ≤ C λ⁻³ 𝒩₂,
|∂w| ≤ C λ⁻⁴ 𝒩₂, and |g − g0| ≤ |λ [g1] + Σ_(j≥2) λ^j [g_j]| + |w| ≤ C λ, |∂g| ≤ C, since ∂[λ g1] = dv ⊗ [F1 g1] + du ⊗
[F2 g1] + λ [∂_X g1] is bounded. ∎

### The data {#sec:two-dust-data}

**Theorem {#thm:two-dust-data}** (Exact data with two families.) Let K ≥ 6 and N := K + 3, and let g_app be the
approximant of [[thm:two-dust-approximant]] with N stages and the stage data of [[lem:two-dust-stage-data]], in its
fixed-phase form. For λ small there is a vacuum Cauchy datum on Σ_τ0, with the gauge condition D = 0 imposed through
∂_τ g, whose w := g − g_app satisfies (E4) of [[thm:uniform-existence]]; it equals the seed's datum on Σ_τ0 ∩ {R < r1},
and it is smooth and invariant under the T² action and both reflections.

The proof is that of [[thm:data]] on the two-dust slice, with the changes of the next two lemmas.

**Lemma {#lem:two-dust-slice}** (The constraints on a round slice.) Let γ = G(R) dR² + R² γ̂ on [a, b1] × S³, G > 0,
and let κ be any symmetric 2-tensor invariant under O(4). With U = (α, ϖ, q) and (γ_U, κ_U) as in [[eq:data-u]], the
linearisation at U = 0 of the constraint map of (γ_U, κ_U) has the principal part

    ρ ≅ (3/(R G²)) ∂_R α − (1/(G R²)) Δ_(S³) α,      J_R ≅ 6 ∂_R ϖ − (2/R²) γ̂^(AB) ∂_A q_B,      J_A ≅ −(2/G) ∂_R q_A + 4 ∂_A ϖ,

with no ∂_R² α and no ∂_R∂_A α in ρ, and independent of κ. The coefficient of ∂_R α is (γ^(RR))^(3/2) H, H = 3/(R √G) >
0 the mean curvature of the spheres; the symmetrizer 𝒮 = diag(1, −½ Π⁻¹), Π = R² γ̂, gives 𝒮A0 = diag(6, G⁻¹ Π⁻¹) > 0
and 𝒮A^B symmetric for every angle B; and in the class of fields of (R, ϑ) invariant under T² and both reflections the
characteristic speeds satisfy c² = 2G/(3R²) > 0. At G = 1 + μ/R² these are the formulas of [[lem:constraints-evolution]]
(a). The slice Σ_τ0 of the two-dust background is such a slice, with G = e^ψ (2 − e^ψ f) ≥ e^ψ > 0.

*Proof.* The proof of [[lem:constraints-evolution]] (a) is written for γ = ν² dr² + Π_AB (dω^A + σ^A dr)(dω^B + σ^B dr)
in general. Here ν² = G, σ^A = 0 and Π = R² γ̂, so the second fundamental form of the spheres is 𝒜 = (1/(2ν)) ∂_R Π =
(R/√G) γ̂ and H = tr_Π 𝒜 = 3/(R √G). The coefficient of ∂_R α is (γ^(RR))^(3/2) H = G^(−3/2) · 3/(R √G) = 3/(R G²), and
the angular second derivatives of α are −γ^(RR) Π^(AB) ∂_A∂_B α = −(G R²)⁻¹ Δ_(S³) α; κ enters ρ only through −|κ_U|² +
(tr κ_U)², algebraically. The principal part of J there, at γ^(RA) = 0 and α = 0, is J_R ≅ 6 ∂_R ϖ − 2 Π^(AB) ∂_A q_B and
J_A ≅ 4 ∂_A ϖ − 2 γ^(RR) ∂_R q_A, and [[eq:data-symmetrizer]] at γ^(RA) = 0 is 𝒮 = diag(1, −½ Π⁻¹), with 𝒮A0 = diag(6,
γ^(RR) Π^(AB)). In the class, A0 = diag(6, −2/G) and A^ϑ = [[0, −2/R²], [4, 0]] in (ϖ, q_ϑ), and det(A^ϑ − c A0) =
−12 c²/G + 8/R² vanishes at c² = 2G/(3R²). On Σ_τ0, dτ = 0 gives dv = dR, so by [[eq:two-dust-chart]] the induced metric
is (2e^ψ − e^(2ψ) f) dR² + R² dΩ₃²; and 2 − e^ψ f ≥ 1, as e^ψ ≤ 1 and f ≤ 1. ∎

So the slice need not be a Vaidya slice: H > 0 holds on every round slice on which R is a coordinate.

**Lemma {#lem:two-dust-stage-data}** (The gauge hierarchy and the stage data, two families.) (a) [[lem:gauge-hierarchy]]
holds for the approximant of [[lem:two-dust-stages]], with D^(m)(X, θ1, θ2) two-phase profiles and (F1)–(F2) there for
all (θ1, θ2).

(b) For every N there are stage data for [[thm:two-dust-approximant]] satisfying (F1) and (F2) of
[[lem:gauge-hierarchy]], all vanishing on Σ_τ0 ∩ {R < r1}; "the stage data of [[lem:two-dust-stage-data]]" means those
constructed in the proof. The mixed harmonics of every profile vanish off the diamond Q×, and in particular on a
neighbourhood of Σ_τ0.

*Proof.* (a) In two-scale form the principal part ½ g^(ab) ∂_a∂_b of B_g ([[eq:data-bianchi]]) acts on λ^m [Y] at order
λ^(m−2) through ½ Σ_(J,K) g⁻¹(du_J, du_K) F_J F_K Y; with g⁻¹(du_K, du_K) = O(λ²) and g⁻¹(du_in, du_out) = g0^(uv) +
O(λ), it multiplies the mixed harmonic (n1, n2) of Y by e^(−2σ) n1 n2 + O(λ), which does not vanish, and its pure
harmonics by O(λ²). At order λ^(m−1) it acts on the pure harmonics of θ_K as the transport (ℓ_K·∂_X + ½ □_(g0) ϕ_K) F_K
plus a bounded multiplication M, as in the proof of [[lem:gauge-hierarchy]]. Induct on m with the hypothesis: D^(j) = 0
for j < m, D^(m) does not depend on (θ1, θ2), and the mixed harmonics of D^(m+1) vanish; it holds at m = 0, by
[[lem:two-dust-stage-zero]] (f) and the order −1 of [[eq:data-bianchi]], whose only term is the mixed one in D^(1). At
order m, the mean of [[eq:data-bianchi]] is the linear wave equation for ⟨D^(m)⟩ of the proof of
[[lem:gauge-hierarchy]], its pure harmonics of θ_K are the transport along ℓ_K for Z_K := F_K Π_K D^(m+1), and its mixed
harmonics are algebraic and give the mixed harmonics of D^(m+2) in terms of ⟨D^(m)⟩ and the Z_K; every other term
vanishes by the hypothesis or contains ℛ^(i), i ≤ m + 1 ≤ N − 1. The data of ⟨D^(m)⟩, ∂_τ⟨D^(m)⟩ and the Z_K are zero
by (F1)–(F2), so the system, which closes as the stage equations do ([[lem:two-dust-stages]], both generators reaching
Σ_τ0 inside Ω₂), gives ⟨D^(m)⟩ = 0 and Z_K = 0, and then the mixed harmonics of D^(m+2) vanish: the hypothesis at m + 1.
The rest is the proof of [[lem:gauge-hierarchy]].

(b) Supports. The harmonics with n1 ≠ 0 of W_in, and those with n2 ≠ 0 of W_out, vanish where v ∉ (v_start, v_end),
respectively u ∉ (u1, u2). For every later profile the same holds by induction over the stages: a harmonic with n1 ≠ 0
of a forcing term contains a factor with such a harmonic, the pure harmonics of θ1 are transported along ℓ_in at fixed
v, the divisions are pointwise, and the data below are fixed pointwise on Σ_τ0 from such terms; likewise for n2 and u.
So every mixed harmonic vanishes off Q× = [u1, u2] × [v_start, v_end], which lies in the future of Σ_τ0, and the mixed
harmonics take no data.

The construction is that of the proof of [[lem:stage-data]]. Stage 0: χ_in = χ_out = 0 on Σ_τ0 ([[eq:two-dust-chi]]).
Stage m = 1, …, N: φ_m^in = φ_m^out = 0 and (m_m)_(τ ·) = 0 on Σ_τ0. (i) On Σ_τ0 the pure harmonics of θ_K of the
oscillating part of D^(m) are Pol_K(F_K Π_K ĝ_(m+1)) + Λ_m^K(γ_m) + (known), with Pol_K(Y) := Y(ℓ_K, ·) − ½ dϕ_K tr_(g0)
Y; Pol_K is onto at every point, by the construction of the proof of [[lem:stage-data]] with the null covector dϕ_K in
place of dv, and its right inverse Pol_K⁺ = Pol_K^T (Pol_K Pol_K^T)⁻¹ commutes with the symmetries; so each family's
pure harmonics of ĝ_(m+1) are fixed as there, each on its own support. The mixed harmonics of D^(m) vanish on Σ_τ0 by
the supports. (ii) As there. (iii) As there, with [[lem:two-dust-slice]] in place of [[lem:constraints-evolution]] (a):
the order-m mean of the constraints is a linear radial problem on the two-dust slice, solved by [[lem:linear-evolution]]
outward from R = a with zero data, through the packet and then the shell; its forcing terms vanish where the earlier
stages' data and both families' waves do, so on R < r1. ∎

*Proof of [[thm:two-dust-data]].* The proof in [[sec:data-proof]] applies, with [[lem:two-dust-stage-data]] for
[[lem:gauge-hierarchy]] and [[lem:stage-data]], and with [[lem:constraints-evolution]] (a) at the data of g0 replaced by
[[lem:two-dust-slice]]. Its parts (b) and (c) hold as stated, with the same proofs: they use of the approximant's data
only that on Σ_τ0 every phase is a function of R, so that phase derivatives are radial (here v = τ0 + R and u is a
function of R on the slice, [[prop:two-dust-background]] (a)); that the parts W_TT^K of the waves have only angular
components and are traceless on the spheres, and the other parts are multiples of dϕ_K ⊗ dϕ_K, which on Σ_τ0 is a
multiple of dR ⊗ dR; that φ_j^K = 0 and (m_j)_(τ ·) = 0 there and γ_RA = O(λ²); that g0^(Aτ) = 0, g0 being round; and
that the mixed harmonics vanish on Σ_τ0. In particular, at the approximant's data the constraint map of (γ_U, κ_U) has
no coefficient of order λ⁻¹: the second derivatives of γ of order λ⁻¹ are λ⁻¹ Σ_K (∂_R ϕ_K)² [F_K² W_K] in ∂_R² γ, and
enter the coefficients of U only through the traces of the W_TT^K on the spheres, which vanish, and through κ̃_RA, the
order-one oscillating part of κ, which vanishes, while the ∂_R κ_RR terms of div κ and d tr κ cancel. This holds for any
phases that are functions of R on the slice, null or not; and the constraint map depends only on g and ∂_τ g on Σ_τ0,
not on ∂_τ² of the phases, so the eikonal equation of the outgoing phase is not used by the data. The principal
coefficients at the approximant's data have the background's values at order zero in every harmonic, H's oscillating
part (1/(2ν)) Π0^(AB) Σ_K ∂_R ϕ_K [F_K W_K,AB] vanishing. [[prop:exact-correction]] then holds on [a, b(τ0)] × S³ with
its proof, U = 0 on R < r1, where 𝒞(γ, κ) and the forcing vanish. ∎

### The spheres' horizon and the mean mass {#sec:two-dust-items}

**Proposition {#prop:two-dust-one-zero}** (One zero per column, two families.) Let μ0 ≥ √72 l5² and K ≥ 6, and for a
column let θ⁺_λ(R) be the outgoing null expansion, for g_λ, of the sphere S_(v,R) = {τ = v − R, |x| = R} at its point
R x̂, and R_H(v) the radius on the column at which R² = μ. There are λ_H ∈ (0, λ0] and C, δ1, δ2 > 0, independent of λ,
such that for λ ≤ λ_H: (a) on every column θ⁺_λ has at most one zero, and θ⁺_λ > 0 above it, < 0 below it; and, if
μ0 > √72 l5², (b) on every column with R_H(v) ≤ v − τ0 − δ1 it has exactly one zero R_λ(v, x̂), and |R_λ − R_H(v)| ≤
C λ; (c) the spheres with R ≤ R_H(v) − C λ (within the domain) are trapped, both future null expansions being negative
at every point, and those with R ≥ R_H(v) + C λ are untrapped. If μ0 = √72 l5², (b)–(c) hold on the columns with
R_H(v)² ≥ μ0 + δ2. In particular there is no inner apparent horizon.

*Proof.* (i) The background. The spheres S_(v,R) are the spheres {u, v = const}. The expansion of a round sphere along a
normal N is 3 N(R)/R. The future null normals ∂_v and ∂_u, normalised by n(τ) = 1, are ∂_v/(1 − R_v) and ∂_u/(−R_u),
since dτ(∂_v) = 1 − R_v ≥ ½ and dτ(∂_u) = −R_u > 0; so

    θ⁺(g0) = 3 R_v/(R (1 − R_v)) = 3 e^ψ f/(R (2 − e^ψ f)),      θ⁻(g0) = −3/R,

using R_v = e^ψ f/2 ([[sec:two-dust-phases]]). On a column R decreases in u, and ∂_u R_v = R_uv = −e^(2σ) μ/R³ < 0
([[lem:two-dust-identities]] (ii)), so along the column ∂_R R_v = R_uv/R_u = e^ψ μ/R³ > 0: θ⁺(g0) has at most one zero
on each column, at R_v = 0, that is at f = 0, R = R_H(v), and there ∂_R θ⁺(g0) = 3 e^ψ μ/R⁴ = 3 e^ψ/μ ≥ 3 e^(min ψ)/μ_max,
min ψ and μ_max := max μ taken over Ω₂. The ingoing expansion is negative everywhere.

(ii) The approximant. The proof of [[lem:sphere-two-scale]] applies with two phases: the conormal plane of the spheres is
spanned by dτ and dR, which also span du and dv, so Π_g^(ab) ∂_a ϕ_K = 0, and the fast part of θ^±(g) is ½ λ⁻¹ Σ_K
k^±(g⁻¹ dϕ_K) Π_g^(ab) [F_K ĝ_ab]. Its λ⁰ coefficient is ½ Σ_K k^±_0(ℓ_K) F_K tr_S g1 = 0, because tr_S W_K = 0 on
every sphere ([[eq:wave-traceless]] for W_TT^K, and dϕ_K ⊗ dϕ_K vanishes on vectors tangent to the spheres). So
θ^±(g_app) = θ^±(g0) + λ [Th1^±] + λ² E^±, with Th1^± a two-phase profile and E^± = e^±(X, v/λ, u/λ, λ), e^± smooth and
bounded with all its derivatives. Along a column v is constant, but u is not: by [[eq:two-dust-chain]] the derivative
along a column of λ [Th1⁺] is λ [∂_R Th1⁺] + (∂_R u) [F2 Th1⁺], which is O(1) unless Th1⁺ does not depend on θ2. It does
not ((iii) below). Then ∂_R(λ [Th1⁺]) = O(λ) and ∂_R(λ² E⁺) = λ² [∂_R e⁺] + λ (∂_R u) [F2 e⁺] = O(λ), so along every
column

    |θ⁺(g_app) − θ⁺(g0)| + |∂_R (θ⁺(g_app) − θ⁺(g0))| ≤ C λ,

and |θ⁻(g_app) + 3/R| ≤ C λ.

(iii) The coefficient Th1⁺ does not depend on θ2. Work in the coordinates (u, v, y), y = (ϑ, φ1, φ2), off the axes (the
identities below extend to the axes by continuity), where the spheres are {u, v = const} with induced metric γ_AB :=
g_AB, A, B angular, and put α := (det γ_AB)^(1/2). For a normal covector k = k_u du + k_v dv and n := g⁻¹ k,

    θ_k = −γ^(AB) Γ[g]^c_AB k_c = (n^u ∂_u + n^v ∂_v) ln α + ½ γ^(AB) n^C ∂_C g_AB − γ^(AB) n^d ∂_A g_dB,      {#eq:two-dust-theta}

since γ^(AB) ∂_d g_AB = 2 ∂_d ln α for d ∈ {u, v}. The outgoing covector is k⁺ = c(g)(du + β dv), with β fixed by
g⁻¹(k⁺, k⁺) = 0 and c(g) > 0 by n(τ) = 1; for g0, β = 0 and n0 = c0 g0⁻¹ du has n0^u = 0 and no angular component. The
last two terms of [[eq:two-dust-theta]] contain only angular derivatives of g, which carry no phase derivative since
∂_A ϕ_K = 0. At order λ they are products of first-order quantities with g0-quantities; as g0_dB = 0 for d ∈ {u, v},
n0^C = 0, the oscillating parts of g1 have no components g1_dB with d ∈ {u, v} (W_TT^K is angular and χ_K dϕ_K ⊗ dϕ_K
lies in the (u, v)-block), and the oscillating part of the λ-coefficient n1 of n has no angular component, their
coefficient of λ does not depend on (θ1, θ2). In the first term write ln α = ln α0 + λ a1 + λ² a2 + O(λ³), with

    a1 = ½ tr_(γ0) G1 = ½ tr_S m1,      a2 = ½ tr_(γ0) G2 − ¼ |G1|²_(γ0),      G_j := (g_j)_AB,

tr_S W_K = 0 making a1 independent of (θ1, θ2). By [[eq:two-dust-chain]], ∂_v [λ^j a_j] = λ^j [∂_v a_j] + λ^(j−1) [F1 a_j]
and ∂_u [λ^j a_j] = λ^j [∂_u a_j] + λ^(j−1) [F2 a_j], so, with n = n0 + λ n1 + O(λ²) and n0^u = 0, the coefficient of λ
of the first term is n0^v [F1 a2] + n0^v [∂_v a1] + n1^v [∂_v ln α0] + n1^u [∂_u ln α0]. The λ-coefficient n1 depends on
(θ1, θ2) only through g1(ℓ_out, ·) = m1(ℓ_out, ·) + [χ_in] dv(ℓ_out) dv, which enters β, c(g) and g⁻¹ at order λ, and so
only through θ1. Hence Th1⁺ depends on θ2 only through n0^v [F1 a2], that is through the mixed harmonics of a2 (F1 kills
those of θ2 alone).

The mixed harmonics of a2 vanish. In the fixed-phase form, the mixed harmonics of G2 are those of ĝ_2 at the phases
θ1 + φ_1^in, θ2 + φ_1^out (the other parts of g2 are m2 and phase-shift terms φ_2^K F_K W_K, which have no mixed
harmonics), and those of |G1|² are those of 2 ⟨W_TT^in, W_TT^out⟩_(γ0); so the mixed part of a2 is that of ã2 :=
½ tr_S ĝ_2 − ¼ |W_TT^in + W_TT^out|²_(γ0) at the shifted phases. We show that, for the stage-0 metric g0 + λ (W_in +
W_out) + λ² ĝ_2 of [[lem:two-dust-stage-zero]],

    γ0^(AB) R^(0)_AB = −2 g0^(uv) F1F2 ã2      on the mixed harmonics;                                        {#eq:two-dust-trace-mixed}

as R^(0) ≡ 0 and F1F2 multiplies the harmonic (n1, n2) by −n1 n2 ≠ 0, the mixed harmonics of ã2 then vanish. First,
Ric^H = Ric − S with S_AB = ½ (g_Aρ ∇̂_B D^ρ + g_Bρ ∇̂_A D^ρ), and D = O(λ) by [[lem:two-dust-stage-zero]] (f); the
derivatives in S_AB are angular, so they bring no factor λ⁻¹, and S_AB = O(λ). Ric has no term of order λ⁻¹ either, so
γ^(AB) Ric_AB has the λ⁰ coefficient γ0^(AB) R^(0)_AB. Second, a mixed harmonic of order λ⁰ comes only from terms with two
phase derivatives, one of each phase: bilinear in (W_in, W_out), or linear in λ² ĝ_2. The latter come from the principal
part alone and give e^(−2σ) F1F2 tr_S ĝ_2 = −2 g0^(uv) F1F2 (½ tr_S ĝ_2). The former are terms of Ric_AB with two
phase derivatives of g̃ := g0 + λ (W_in + W_out), and contain no angular derivative; Ric being at most quadratic in
first derivatives, they are those of the metric with the same components and the same derivatives in (u, v) at the
point and no dependence on y. The metric g̃ is block diagonal for the splitting into the (u, v)-block and the angular
block. For a metric h_ab(x) dx^a dx^b + γ_AB(x) dy^A dy^B, x = (u, v), whose components do not depend on y, the
Christoffel symbols are those of h, Γ^a_AB = −½ h^(ab) ∂_b γ_AB and Γ^A_aB = ½ γ^(AC) ∂_a γ_CB, so that

    Ric_AB = −½ □_h γ_AB − ¼ h^(ab) ∂_a ln det γ ∂_b γ_AB + ½ h^(ab) γ^(CD) ∂_a γ_AC ∂_b γ_BD,
    γ^(AB) Ric_AB = −α⁻¹ □_h α,      α = (det γ)^(1/2),                                                     {#eq:two-dust-cpw}

the trace following from γ^(AB) □_h γ_AB = □_h ln det γ + h^(ab) tr(γ⁻¹ ∂_a γ γ⁻¹ ∂_b γ); this is the trace identity of
colliding plane waves. For g̃, ln α = ln α0 + λ ½ tr_S W − ¼ λ² |W|²_(γ0) + O(λ³), and tr_S W = 0. In −α⁻¹ □_h α = −□_h
ln α − |d ln α|²_h, the terms of order λ⁰ with two phase derivatives come from −h0^(ab) ∂_a∂_b(−¼ λ² |W|²_(γ0)) alone
(d ln α = O(λ), and h − h0 = O(λ)), and their mixed part is −2 g0^(uv) F1F2(−¼ |W_TT^in + W_TT^out|²_(γ0)), the terms
with two derivatives in one phase being multiplied by g0^(uu) = g0^(vv) = 0. This gives [[eq:two-dust-trace-mixed]].

(iv) The remainder. θ⁺(g) is a smooth function of (X, g) plus a smooth function of (X, g) times ∂g ([[lem:sphere-two-scale]]).
So |θ⁺(g_λ) − θ⁺(g_app)| ≤ C (|w| + |∂w|), and its derivative along a column is at most C (λ⁻¹ |w| + |∂w| + |∂²w|), the
derivatives along a column of g_app and ∂g_app being at most C and C λ⁻¹. By [[eq:remainder-pointwise]], which holds here
by Step 1 of the proof of [[thm:two-dust-uniform]], both are at most C M λ^(K−5) ≤ C λ, as K ≥ 6. With (ii), along every
column |θ⁺_λ − θ⁺(g0)| + |∂_R(θ⁺_λ − θ⁺(g0))| ≤ C3 λ and |θ⁻(g_λ) + 3/R| ≤ C3 λ.

(v) The zero. This is (v) of the proof of [[prop:one-zero]], with R_H(v) in place of √μ(v), the lower bound 3 e^(min ψ)/
μ_max for ∂_R θ⁺(g0) at the zero in place of 3/μ_max, and the margin of the zero from the curvature boundary as follows.
At R = R_H, μ = R_H², so R_H⁴ − r_q(μ)⁴ = μ² − √72 μ l5² ≥ μ0 (μ0 − √72 l5²), which is positive when μ0 > √72 l5²; μ
being uniformly continuous on the compact Ω₂, there is δ > 0 such that the points of a column with |R − R_H| ≤ δ and
R ≤ v − τ0 lie in D_T. If μ0 = √72 l5², the same holds on the columns with R_H² ≥ μ0 + δ2. ∎

The statement concerns the round family {S_(v,R)}: its zero set on the columns is not itself a marginally trapped
surface. Although ∂g_λ converges only weakly, the expansions of these spheres do not see the oscillation at order λ⁰,
the waves being traceless on them; and at order λ the outgoing wave, which oscillates along the columns, does not enter
the outgoing expansion, because stage 0's division has removed the mixed harmonics of the angular trace.

**Lemma {#lem:two-dust-quarter-turn}** (The quarter turn with two phases.) Let J be the map of [[sec:quarter-turn]], and
let S act on families of two-phase profiles by (S g)_j(X, θ1, θ2) := (−1)^j (J* g_j)(X, 3π/2 − θ1, 3π/2 − θ2).

(a) J is an isometry of every round double-null metric, fixing u, v and every sphere, with J_* ℓ_K = ℓ_K; and
[[lem:quarter-turn]] (a) holds for two phases: the two-scale residual of g̃ := g0 + Σ_j λ^j (S g)_j is
R[g̃](X, θ1, θ2; λ) = J* R[g](X, 3π/2 − θ1, 3π/2 − θ2; −λ).
(b) W_in and W_out are S-invariant at weight 1, and the coefficient of λ in the expansion of R[g0 + λ W_K] is S-odd.
(c) The mixed harmonics of ĝ_2 fixed in [[lem:two-dust-stage-zero]] are S-invariant at weight 2.
(d) The profiles of the approximant of [[thm:two-dust-approximant]], with the stage data of [[lem:two-dust-stage-data]],
satisfy S g = g. In particular J* m1 = −m1.

*Proof.* (a) J is linear in x and lies in O(4), so it preserves R = |x|, τ, the round metric and hence g0, and every
function of (τ, R), u and v among them. The proof of [[lem:quarter-turn]] (a) applies with D^λ_a := ∂_a + λ⁻¹ (∂_a v) F1
+ λ⁻¹ (∂_a u) F2 and ρ(θ1, θ2) := (3π/2 − θ1, 3π/2 − θ2): D^λ_a(f ∘ ρ) = (D^(−λ)_a f) ∘ ρ, and J* commutes with D^λ.
(b) The outgoing wave has the algebraic form of the ingoing one, with F₂ := λ A₂ env₂(u) h(ζ) sin θ2 and G₂ :=
λ A₂ env₂(u) h(ζ) cos θ2, and J fixes u; so the computation of [[lem:quarter-turn]] (b) gives (J* W_TT^K)(X, 3π/2 −
θ_K) = −W_TT^K(X, θ_K) for both families. χ_in and χ_out are S-invariant by the uniqueness of the transports
[[eq:two-dust-chi]], which commute with J and whose forcing terms are S-even by (a) at order 0, as in [[lem:quarter-turn]]
(b). The last claim is (a) at order 1 for the S-invariant family g0 + λ W_K.
(c) By (a), applied to the S-invariant family g0 + λ (W_in + W_out), J* R^(0)(X, 3π/2 − θ1, 3π/2 − θ2) = R^(0)(X, θ1,
θ2). The division by e^(−2σ) F1F2 commutes with J*, σ being O(4)-invariant, and with ρ, since F1F2 is invariant under ρ.
So the mixed harmonics of ĝ_2, the quotients of those of −R^(0) at ĝ_2 = 0, satisfy (J* ĝ_2)(X, 3π/2 − θ1, 3π/2 − θ2) =
ĝ_2(X, θ1, θ2).
(d) Every later stage of [[lem:two-dust-stages]] (c) and every choice of [[lem:two-dust-stage-data]] (the right inverses
Pol_K⁺, which are O(4)-equivariant and act pointwise in (θ1, θ2), the division, and the data of the means and phases as
in [[lem:stage-data]]) is the unique solution of a problem that S maps to itself, and the rewriting with the fixed phases
commutes with S. So the proof of [[lem:quarter-turn]] (c) applies and gives S g = g; taking the mean over T², J* m1 =
−m1. ∎

The base of the induction is (b) for both families and (c) for the interaction: with one quadrature alone in either
family, (b) fails for that family.

**Proposition {#prop:two-dust-mean-mass}** (The mean mass, two families.) For K ≥ 6 and λ ≤ λ0, and every sphere
S = S_(v,R) in D_T ∩ {τ ≥ τ0}: if v ∉ (v_start, v_end) and u ∉ (u1, u2) on S, then |M[S](g_λ) − μ(S)| ≤ C λ², μ(S) the
mass function [[eq:two-dust-mass]] on S; otherwise |M[S](g_λ) − μ(S)| ≤ C λ. Moreover M[S](g0) = μ(S) for every round
double-null metric.

*Proof.* For g0, with the future null normals n⁺ := e^(−2σ) ∂_v and n⁻ := e^(−2σ) ∂_u (Θ in [[eq:hawking-mass]] does not
depend on their normalisation), θ^± = 3 e^(−2σ) R_v/R and 3 e^(−2σ) R_u/R, and g0(n⁺, n⁻) = −e^(−2σ); so Θ = 18 e^(−2σ)
R_u R_v/R², the area is 2π² R³, and M[S](g0) = R² (1 + 2e^(−2σ) R_u R_v) = μ(S).

If v ∉ (v_start, v_end) and u ∉ (u1, u2) on S, every oscillating profile of g_app vanishes on S: the harmonics with
n1 ≠ 0 vanish where v ∉ (v_start, v_end) and those with n2 ≠ 0 where u ∉ (u1, u2) ([[lem:two-dust-stage-data]] (b)),
and so do the phase-shift terms of the fixed-phase form, which carry the waves. So g_app = g0 + λ m1 + λ² E on S, and
M[S](g_λ) = μ(S) + λ DM[m1] + O(λ²) + O(|w| + |∂w|). By naturality DM[J* m] = DM[m], J fixing g0 and S, as in the
proof of [[prop:mean-mass]]; so DM[m1] = −DM[m1] = 0 by [[lem:two-dust-quarter-turn]] (d), and the remainder is at most
C λ^(K−4) ≤ C λ². Elsewhere θ^± have no oscillation at order λ⁰ ((ii) of the proof of [[prop:two-dust-one-zero]]) and
the area none, tr_S W_K being zero, so M[S](g_app) − μ(S) = O(λ), and the remainder is at most C λ^(K−4). For λ beyond
the λ* of [[lem:sphere-two-scale]] the bounds hold with a larger C, as in the proof of [[prop:mean-mass]]. ∎

### Proof of the theorem {#sec:two-dust-proof}

*Proof of [[thm:two-dusts]].* The background exists on Ω₂ ⊃ D_T ∩ {τ ≥ τ0} with the properties of
[[prop:two-dust-background]] and [[lem:two-dust-domain]]. Let g_app be the approximant of [[thm:two-dust-approximant]]
with N = K + 3 stages and the stage data of [[lem:two-dust-stage-data]], and let the data on Σ_τ0 be those of
[[thm:two-dust-data]], which satisfy the constraints exactly, carry D = 0, equal the seed's on R < r1, and are within
C λ^K of those of g_app. [[thm:two-dust-uniform]] gives, for λ ≤ λ0, the solution g_λ of Ric^H(g) = 0 on Ω₂ with these
data, unique among C² solutions with these data and |g − g0| ≤ ε1, smooth, with w = g_λ − g_app as in items 3 and 4.
Taking λ0 so small that C λ0 ≤ ε1, g_λ is Lorentzian by [[lem:two-dust-domain]] (e). [[lem:gauge-propagation]] holds on
Ω₂ with its proof, which uses of the domain only [[lem:domain]] (e) and the energy inequality, both of which hold on Ω₂
([[lem:two-dust-domain]]); it gives D(g_λ) = 0 and Ric(g_λ) = 0. This is items 1, 2, 3 and 5.

Symmetry. Every element of G = O(2) × O(2), acting on x and fixing τ, lies in O(4), so it preserves R, u and v, hence
g0, Ω₂ and Σ_τ0, and the argument of [[sec:main-proof]] applies: by the uniqueness of item 5 and the invariance of the
data ([[thm:two-dust-data]]), g_λ is invariant.

Convergence. For a two-phase profile f = Σ_n f_n(X) e^(i(n1 θ1 + n2 θ2)) and a test function ζ ∈ C_c^∞ in the interior of
Ω₂, let n ≠ 0 and Φ_n := n1 v + n2 u. If n1 ≠ 0, put Z := ℓ_out, so that Z(Φ_n) = n1 g0^(uv) = −n1 e^(−2σ); if n1 = 0,
put Z := ℓ_in, with Z(Φ_n) = −n2 e^(−2σ). Then e^(iΦ_n/λ) = (λ/(i Z(Φ_n))) Z(e^(iΦ_n/λ)), and integrating by parts,
∫ ζ f_n e^(iΦ_n/λ) = O(λ/|n1|) or O(λ/|n2|), with constants given by derivatives of ζ f_n, which decay faster than any
power of |n|. So ∫ ζ [f] → ∫ ζ ⟨f⟩, and [f] → ⟨f⟩ weakly in L²(Ω₂). Now ∂[λ g1] = dv ⊗ [F1 g1] + du ⊗ [F2 g1] + λ [∂_X
g1], ∂[λ^j g_j] = O(λ^(j−1)) for j ≥ 2, and |∂w| ≤ C λ^(K−4), which gives the formula of item 4; ⟨F_K g1⟩ = 0, so ∂g_λ →
∂g0 weakly. Applying the same limit to |dv ⊗ F1 g1 + du ⊗ F2 g1|², whose mean over T² is the sum of the means of the two
families' terms, the cross term having mean zero, shows that ‖dv ⊗ [F1 g1] + du ⊗ [F2 g1]‖²_(L²(U)) tends to a positive
limit on every open U on which env or env₂ is not identically zero: there the mean of |F_K W_TT^K|²_(g0) is (4/3) A² env²
R⁻³, respectively (4/3) A₂² env₂² R⁻³ ([[lem:two-dust-stage-zero]] (c)). So the convergence is not strong there.
[[eq:two-dust-limit]] is [[lem:two-dust-stage-zero]] (c) with [[prop:two-dust-background]]; [[lem:two-dust-identities]]
(vi) gives the background's Kretschmann scalar.

Items 6 and 7 are [[prop:two-dust-one-zero]] and [[prop:two-dust-mean-mass]]. ∎
