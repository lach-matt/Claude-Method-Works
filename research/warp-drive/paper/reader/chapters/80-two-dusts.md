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

