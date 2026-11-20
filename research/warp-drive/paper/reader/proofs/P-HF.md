### The a priori estimate in the wave gauge {#sec:tl5-hf}

This section proves an a priori estimate for solutions of the reduced problem of [[sec:tl5-wg]] close to an explicit
background ĝ, in a norm Y built from characteristic energies with an exponential weight, and with it the hypotheses
(H1)–(H3) of [[lem:tl5-continuation]] in the wave gauge, every constant being an explicit function of the jets of ĝ.
The estimate has three parts. The first is a weighted energy identity for the linearised operator, the
five-dimensional tensor wave operator of ĝ with its curvature term, on the regions bounded by two hypersurfaces of the
tilted foliations of [[def:tl5-wg-domains]] ([[lem:tl5-hf-identity]]); the whole linear bulk is absorbed pointwise
by two rates, one for each family of hypersurfaces ([[def:tl5-hf-rates]]), and no Grönwall inequality is used
([[prop:tl5-hf-linear]]). The second is commutation with the static Killing field and the six rotations of the
seed, whose deformation tensors measure only the departure of ĝ from the seed ([[lem:tl5-hf-commutator]]),
together with the recovery of all second derivatives from them and from the equation ([[lem:tl5-hf-recovery]]). The
third is the bound of the quadratic terms ([[lem:tl5-hf-quadratic]]) by a Sobolev inequality on the future boundaries
([[lem:tl5-hf-sobolev]]). [[thm:tl5-hf]] collects them.

We use the notation of [[sec:tl5-wg]]: the background ĝ of [[def:tl5-wg-background]], with Ω̂, ê₃, ê₄, D̂ and R̂,
the region D̄ = [−10, u*] × [1/2, v*] × S³, N₀, N₁ and N = N₀ ∪ N₁, the tilted domains D^κ_s of
[[eq:tl5-wg-tilted]] with τ₁ = u + κ′(v − 1/2), τ₂ = v + κ(u + 10) and κ_m = min(κ, κ′), the norm |·|_k̂ of k̂
([[eq:tl5-wg-khat]]), and the operators of [[lem:tl5-wg-linear]]. Throughout, u* < −1. The background is G-invariant
and in double-null form, so by [[pending:lem-tl5-cip-form]] (b) it is a metric of the class in the gauge,

    ĝ = −4Ω̂² du dv + e^(2ζ) (dx − b̂ du)² + e^(2A) dφ1² + e^(2B) dφ2²,      Ω̂² = e^(2W),

with ζ, A and B as in [[eq:tl5-radii]] for its fields R, P, Q and with b̂ = (1 − x²) s; then ê₃ = ∂_u + b̂ ∂_x,
ê₄ = ∂_v, and e^(ζ + A + B) = R³/4. The round metric of S³ is γ₀ = dx²/(4(1 − x²)) + ((1 + x)/2) dφ1² +
((1 − x)/2) dφ2², and dω := dx dφ1 dφ2/4 is its measure.

#### The multiplier, the frame and the operators {#sec:tl5-hf-setting}

**Definition {#def:tl5-hf-frame}** (The multiplier and the frame.) Let f(r) := 1 − r⁻² and c(u) := f(−u)/2, a smooth
function on [−10, u*] with 0 < c < 1/2, and put

    T := ê₄ + c ê₃,    |T| := 2 √c Ω̂,    E₀ := T/|T|,    E₁ := (ê₄ − c ê₃)/|T|.

At each point let f₁, f₂, f₃ be a ĝ-orthonormal frame of the leaf. Then (E₀, E₁, f₁, f₂, f₃) is ĝ-orthonormal, with
ĝ(E₀, E₀) = −1, and

    ê₄ = √c Ω̂ (E₀ + E₁),      ê₃ = (Ω̂/√c) (E₀ − E₁).                                                {#eq:tl5-hf-null-pair}

Put k := ĝ + 2 ĝ(E₀, ·) ⊗ ĝ(E₀, ·), a Riemannian metric in which the frame is orthonormal. For tensors of every type,
⟨·, ·⟩ and |·| denote the inner product and the norm induced by k; for a 2-tensor A, |A|² = Σ A(F_M, F_N)², the sum
over the frame F = (E₀, E₁, f₁, f₂, f₃). Frame components are written A_MN := A(F_M, F_N), with M, N ∈ {0, …, 4},
and indices j, l ∈ {2, 3, 4} refer to f₁, f₂, f₃. The operator norm of a linear map between spaces of tensors is
taken in these norms.

For the seed of [[lem:tl5-seed]], T is the static Killing field ∂_v + (f(−u)/2) ∂_u of [[lem:tl5-seed]], since there b̂ = 0. The
norm k is the norm k̂ of [[eq:tl5-wg-khat]] with E₀ in place of the vector e₀ = (ê₃ + ê₄)/(2Ω̂) used there.

**Lemma {#lem:tl5-hf-khat}** (The two norms.) For every tensor A of rank r (covariant, contravariant or mixed) at a
point of D̄,

    c^(r/2) |A|_k̂ ≤ |A| ≤ c^(−r/2) |A|_k̂.

*Proof.* By [[eq:tl5-hf-null-pair]] and the definition of e₀ and e₁ := (ê₄ − ê₃)/(2Ω̂) in [[sec:tl5-wg]],
E₀ = ch β e₀ + sh β e₁ and E₁ = sh β e₀ + ch β e₁ with e^β := c^(−1/2), the leaf frame being common to both. So the
frame F is the image of the k̂-orthonormal frame (e₀, e₁, f₁, f₂, f₃) under a linear map whose matrix has singular
values e^β, e^(−β), 1, 1, 1; its operator norm and that of its inverse are e^β = c^(−1/2), as c < 1. The components of
A in one frame are those in the other, transformed by this matrix or its inverse transpose in each of the r slots, and
the Frobenius norm of the result is at most e^(rβ) times the Frobenius norm of the components. ∎

**Definition {#def:tl5-hf-operators}** (The operators.) Let 𝓡̂, □̂ and the curvature convention be those of
[[lem:tl5-wg-linear]] (b), and for a symmetric 2-tensor field h put

    L̂ h := □̂ h + 2 𝓡̂ h,      𝒞_αβ h := [D̂_α, D̂_β] h,                                                 {#eq:tl5-hf-operators}

so that L̂ h = −2 (d/dt) Ric^W(ĝ + t h)|_(t=0) by [[eq:tl5-wg-lin]], and (𝒞_αβ h)_μν = −R̂^ρ_μαβ h_ρν − R̂^ρ_ναβ h_μρ.
Write 𝒞_MN := 𝒞(F_M, F_N). Let ω_i(V) := ĝ(D̂_V E₀, F_i) for i = 1, …, 4, so that D̂_V E₀ = Σ_(i≥1) ω_i(V) F_i, and
for 2-tensors A, B put

    D_i(A, B) := 4 Σ_N (A_iN B_0N + A_0N B_iN),      𝔇_V(A, B) := Σ_(i≥1) ω_i(V) D_i(A, B).                {#eq:tl5-hf-frame-terms}

Then for 2-tensor fields A, B and every vector V,

    V⟨A, B⟩ = ⟨D̂_V A, B⟩ + ⟨A, D̂_V B⟩ + 𝔇_V(A, B).                                                 {#eq:tl5-hf-dk}

For a solution g of the reduced problem, h := g − ĝ lies in the eight-dimensional class subspace of
[[prop:tl5-wg-vacuum]] (b); the estimates below do not use this, and hold for symmetric 2-tensor fields without
symmetry.

*Proof of [[eq:tl5-hf-dk]].* In components, ⟨A, B⟩ = A_μν B_ρσ k^μρ k^νσ with k^μρ = ĝ^μρ + 2E₀^μ E₀^ρ, and
D̂_V k^μρ = 2((D̂_V E₀)^μ E₀^ρ + E₀^μ (D̂_V E₀)^ρ) = 2 Σ_i ω_i(V) (F_i^μ E₀^ρ + E₀^μ F_i^ρ). The derivative of k in the
first pair of slots gives 2 Σ_i ω_i(V) Σ_N (A_iN B_0N + A_0N B_iN), and in the second pair, by the symmetry of A and
B, the same; their sum is 𝔇_V(A, B). ∎

The vector fields E₀, E₁ and the forms ω_i are smooth on D̄: E₀ and E₁ are built from ê₃, ê₄ and c, and ω_i(V) F_i
is the vector D̂_V E₀, which is orthogonal to E₀; 𝔇_V does not depend on the choice of the leaf frame.

**Definition {#def:tl5-hf-domains}** (Corner regions.) For a ∈ [−10, u*] and b ∈ [1/2, v*] put

    Q(a, b) := D̄ ∩ {τ₁ ≤ a} ∩ {τ₂ ≤ b},

so that D^κ_s = Q(u*, s). Its boundary consists of the parts {u = −10} of N₁ and {v = 1/2} of N₀ and of the future
faces Σ₁(a, b) := Q(a, b) ∩ {τ₁ = a} and Σ₂(a, b) := Q(a, b) ∩ {τ₂ = b}. The coordinates (τ₁, τ₂) are
related to (u, v) by a linear map of determinant 1 − κκ′ ∈ [15/16, 1), and on Q(a, b), u ≤ τ₁ ≤ a and v ≤ τ₂ ≤ b.

If p ∈ Q(a, b), then Q(τ₁(p), τ₂(p)) ⊂ Q(a, b); and Q(a′, b′) ⊂ Q(a, b) for a′ ≤ a, b′ ≤ b.

#### The energy identity {#sec:tl5-hf-identity}

**Definition {#def:tl5-hf-current}** (The current.) Let z and z̲ be smooth positive functions of (u, v) on
[−10, u*] × [1/2, v*], and 𝒵 := z ê₄ + z̲ ê₃. For a C² symmetric 2-tensor field Ψ on a set Q ⊂ D̄ put

    𝕋[Ψ]_αβ := ⟨D̂_α Ψ, D̂_β Ψ⟩ − (1/2) ĝ_αβ ĝ^(γδ) ⟨D̂_γ Ψ, D̂_δ Ψ⟩,      J[Ψ] := −𝕋[Ψ](T, ·)^♯ + |Ψ|² 𝒵,

the index raised with ĝ, and the flux densities

    e_o[Ψ] := −ĝ(J[Ψ], ê₄) = 𝕋[Ψ](T, ê₄) + 2Ω̂² z̲ |Ψ|²,      e_i[Ψ] := −ĝ(J[Ψ], ê₃) = 𝕋[Ψ](T, ê₃) + 2Ω̂² z |Ψ|².

Write w_± := D̂_(E₀)Ψ ± D̂_(E₁)Ψ and |∇̸Ψ|² := Σ_j |D̂_(f_j)Ψ|².

**Lemma {#lem:tl5-hf-densities}** (The densities.) 𝕋[Ψ](T, ê₄) = c Ω̂² (|w₊|² + |∇̸Ψ|²) and
𝕋[Ψ](T, ê₃) = Ω̂² (|w₋|² + |∇̸Ψ|²). In particular e_o and e_i are nonnegative, and

    |D̂_(ê₄)Ψ|² = c Ω̂² |w₊|² ≤ e_o,   |D̂_(ê₃)Ψ|² = (Ω̂²/c) |w₋|²,   |Ψ|² ≤ e_o/(2Ω̂² z̲),   |Ψ|² ≤ e_i/(2Ω̂² z),
    Σ_M |D̂_(F_M)Ψ|² = (|w₊|² + |w₋|²)/2 + |∇̸Ψ|² ≤ e_o/(2cΩ̂²) + e_i/(2Ω̂²).                             {#eq:tl5-hf-coercive}

*Proof.* By [[eq:tl5-hf-null-pair]], D̂_(ê₄)Ψ = √c Ω̂ w₊ and D̂_(ê₃)Ψ = (Ω̂/√c) w₋. The inverse metric is
ĝ⁻¹ = −(ê₃ ⊗ ê₄ + ê₄ ⊗ ê₃)/(2Ω̂²) + Σ_j f_j ⊗ f_j, so ĝ^(γδ)⟨D̂_γΨ, D̂_δΨ⟩ = −Ω̂⁻² ⟨D̂_(ê₃)Ψ, D̂_(ê₄)Ψ⟩ + |∇̸Ψ|².
With ĝ(ê₄, ê₄) = ĝ(ê₃, ê₃) = 0 and ĝ(ê₃, ê₄) = −2Ω̂² this gives 𝕋(ê₄, ê₄) = |D̂_(ê₄)Ψ|², 𝕋(ê₃, ê₃) = |D̂_(ê₃)Ψ|² and
𝕋(ê₃, ê₄) = Ω̂² |∇̸Ψ|², and with T = ê₄ + c ê₃ the two formulae follow. Further −ĝ(𝒵, ê₄) = 2Ω̂² z̲ and
−ĝ(𝒵, ê₃) = 2Ω̂² z. The last line uses D̂_(E₀)Ψ = (w₊ + w₋)/2, D̂_(E₁)Ψ = (w₊ − w₋)/2, and that the term |∇̸Ψ|² occurs
in both densities, so that |∇̸Ψ|² ≤ e_i/Ω̂²; then (|w₊|² + |∇̸Ψ|²)/2 ≤ e_o/(2cΩ̂²) and |w₋|²/2 + |∇̸Ψ|²/2 ≤ e_i/(2Ω̂²). ∎

**Lemma {#lem:tl5-hf-divergence}** (The divergence.) Let π := ℒ_T ĝ. For every C² symmetric 2-tensor field Ψ,

    div J[Ψ] = −⟨L̂Ψ, D̂_TΨ⟩ + ℬ[Ψ],
    ℬ[Ψ] := −(1/2) π^(αβ) 𝕋_αβ + 2⟨𝓡̂Ψ, D̂_TΨ⟩ − T^β ⟨D̂^αΨ, 𝒞_αβ Ψ⟩ − ĝ^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ)
            + (1/2) ĝ^(γδ) 𝔇_T(D̂_γΨ, D̂_δΨ) + 2⟨Ψ, D̂_𝒵 Ψ⟩ + 𝔇_𝒵(Ψ, Ψ) + |Ψ|² div 𝒵,                    {#eq:tl5-hf-bulk}

where D̂_αD̂_βΨ denotes the second covariant derivative and the divergence is that of ĝ.

*Proof.* By [[eq:tl5-hf-dk]], D̂^α⟨D̂_αΨ, D̂_βΨ⟩ = ⟨□̂Ψ, D̂_βΨ⟩ + ⟨D̂^αΨ, D̂_αD̂_βΨ⟩ + ĝ^(αγ) 𝔇_(∂_γ)(D̂_αΨ, D̂_βΨ)
and (1/2) D̂_β(ĝ^(γδ)⟨D̂_γΨ, D̂_δΨ⟩) = ĝ^(γδ)⟨D̂_βD̂_γΨ, D̂_δΨ⟩ + (1/2) ĝ^(γδ) 𝔇_(∂_β)(D̂_γΨ, D̂_δΨ). Since
D̂_αD̂_βΨ − D̂_βD̂_αΨ = 𝒞_αβ Ψ, the difference of the two second-derivative terms is ⟨D̂^αΨ, 𝒞_αβ Ψ⟩. Next,
div(𝕋(T, ·)^♯) = T^β D̂^α𝕋_αβ + 𝕋_αβ D̂^α T^β, and 𝕋_αβ D̂^α T^β = (1/2) π^(αβ) 𝕋_αβ since 𝕋 is symmetric and
π_αβ = D̂_α T_β + D̂_β T_α. Finally div(|Ψ|² 𝒵) = 𝒵(|Ψ|²) + |Ψ|² div 𝒵 with 𝒵(|Ψ|²) = 2⟨Ψ, D̂_𝒵 Ψ⟩ + 𝔇_𝒵(Ψ, Ψ),
and □̂Ψ = L̂Ψ − 2𝓡̂Ψ. Collecting the terms gives [[eq:tl5-hf-bulk]]. ∎

The term −T^β⟨D̂^αΨ, 𝒞_αβ Ψ⟩ is absent for scalar fields; for tensors it is zeroth order in Ψ times first order.

**Lemma {#lem:tl5-hf-identity}** (The weighted energy identity.) Let Φ_o ∈ C¹[−10, u*] and Φ_i ∈ C¹[1/2, v*], put
a_o := Φ_o′, a_i := Φ_i′ and φ := Φ_o(τ₁) + Φ_i(τ₂) on D̄ ∩ {τ₁ ≤ u*, τ₂ ≤ v*}, and let Ψ be a C² symmetric 2-tensor
field on Q := Q(a, b). With the face densities

    ε₁[Ψ] := (e_o[Ψ] + κ′ e_i[Ψ])/(1 − κκ′),      ε₂[Ψ] := (e_i[Ψ] + κ e_o[Ψ])/(1 − κκ′),               {#eq:tl5-hf-faces}

and dμ := R³ dω, the measure that ĝ induces on the leaves,

    ∫_(Σ₁(a,b)) e^(−φ) ε₁ dμ dτ₂ + ∫_(Σ₂(a,b)) e^(−φ) ε₂ dμ dτ₁
      = ∫_(N₁ ∩ Q) e^(−φ) e_o dμ dv + ∫_(N₀ ∩ Q) e^(−φ) e_i dμ du
        + ∫_Q e^(−φ) (2Ω̂² div J − (a_o + κ a_i) e_o − (a_i + κ′ a_o) e_i) dμ du dv,                    {#eq:tl5-hf-identity}

with a_o and a_i evaluated at τ₁ and τ₂. There is no boundary term at the axes.

*Proof.* In the coordinates (u, v, x, φ1, φ2) the volume form of ĝ is 2Ω̂² e^(ζ + A + B) du dv dx dφ1 dφ2: the
(u, v, x) block of ĝ has determinant −4Ω̂⁴ e^(2ζ), as its expansion along the row of v, (−2Ω̂², 0, 0), shows. Since
e^(ζ + A + B) = R³/4 and dω = dx dφ1 dφ2/4, this is 2Ω̂² dμ du dv; the measure dμ = R³ dω is smooth on each leaf, the
axes included. In the coordinates (τ₁, τ₂, x, φ1, φ2), du dv = dτ₁ dτ₂/(1 − κκ′).

The region Q is P × S³ with P the convex polygon {u ≥ −10, v ≥ 1/2, τ₁ ≤ a, τ₂ ≤ b} in the (u, v)-plane, so its
boundary is ∂P × S³; S³ is closed, and the points of the axes are interior points of S³. For a C¹ vector field V on
Q, Stokes' theorem for the form ι_V vol on the manifold with corners Q gives ∫_Q div V vol as the sum over the edges
of P of the integrals over the edge times S³; on the edge {τ₁ = a} the pullback of ι_V vol is dτ₁(V) times
2Ω̂² dμ dτ₂/(1 − κκ′), on {τ₂ = b} it is dτ₂(V) times 2Ω̂² dμ dτ₁/(1 − κκ′), and on {u = −10} and {v = 1/2},
traversed with the outward orientation, it is −du(V) 2Ω̂² dμ dv and −dv(V) 2Ω̂² dμ du.

Take V := e^(−φ) J. Since ĝ(ê₄, ·) = −2Ω̂² du and ĝ(ê₃, ·) = −2Ω̂² dv, 2Ω̂² du(J) = e_o and 2Ω̂² dv(J) = e_i; hence
2Ω̂² dτ₁(J) = e_o + κ′ e_i = (1 − κκ′) ε₁ and 2Ω̂² dτ₂(J) = e_i + κ e_o = (1 − κκ′) ε₂. Finally
div(e^(−φ) J) = e^(−φ)(div J − dφ(J)), and 2Ω̂² dφ(J) = a_o (e_o + κ′ e_i) + a_i (e_i + κ e_o). ∎

If Ψ = 0 on N₀, then e_i[Ψ] = 0 on N₀, since ê₃ and the leaves are tangent to N₀.

#### The pointwise bound and the rates {#sec:tl5-hf-rates}

At a point p of D̄ let 𝒮_p be the space of symmetric 2-tensors at p, a fifteen-dimensional Euclidean space with
⟨·, ·⟩. The expression ℬ[Ψ](p) of [[eq:tl5-hf-bulk]] depends only on the jet

    ξ := (ξ₊, ξ₋, ξ_∥, ξ₀) := (w₊, w₋, (D̂_(f₁)Ψ, D̂_(f₂)Ψ, D̂_(f₃)Ψ), Ψ) ∈ 𝒮_p ⊕ 𝒮_p ⊕ 𝒮_p³ ⊕ 𝒮_p

at p, and is a quadratic form ℬ_p(ξ) in it, whose coefficients are built from the 2-jet of ĝ at p, the values of c
and c′ and the 1-jets of z and z̲. Write it in blocks, ℬ_p(ξ) = Σ_ϰ ℬ_ϰϰ(ξ_ϰ, ξ_ϰ) + 2 Σ_(ϰ<λ) ℬ_ϰλ(ξ_ϰ, ξ_λ), the
indices ranging over (+, −, ∥, 0) in this order, with ℬ_ϰϰ symmetric.

**Definition {#def:tl5-hf-blocks}** (The bulk matrix.) At p let 𝔟_ϰϰ be the largest eigenvalue of the symmetric form
ℬ_ϰϰ on its space (a real number of either sign), 𝔟_ϰλ := sup {ℬ_ϰλ(ξ, ξ′) : |ξ| = |ξ′| = 1} ≥ 0 for ϰ ≠ λ, and
𝔅(p) := 2Ω̂² (𝔟_ϰλ), a symmetric 4 × 4 matrix with nonnegative off-diagonal entries. Put

    E_o := diag(c Ω̂², 0, c Ω̂², 2Ω̂² z̲),      E_i := diag(0, Ω̂², Ω̂², 2Ω̂² z),

so that e_o = nᵀ E_o n and e_i = nᵀ E_i n for n := (|ξ₊|, |ξ₋|, |ξ_∥|, |ξ₀|), by [[lem:tl5-hf-densities]].

**Lemma {#lem:tl5-hf-pointwise}** (The pointwise bound.) For every C² symmetric 2-tensor field Ψ, at every point,

    2Ω̂² ℬ[Ψ] ≤ nᵀ 𝔅 n,      2Ω̂² |⟨L̂Ψ, D̂_TΨ⟩| ≤ 2Ω̂² |L̂Ψ| (√e_o + √c √e_i),

with n as in [[def:tl5-hf-blocks]].

*Proof.* By the definition of the largest eigenvalue, ℬ_ϰϰ(ξ_ϰ, ξ_ϰ) ≤ 𝔟_ϰϰ |ξ_ϰ|², and by that of 𝔟_ϰλ,
ℬ_ϰλ(ξ_ϰ, ξ_λ) ≤ 𝔟_ϰλ |ξ_ϰ| |ξ_λ|; summing gives the first inequality. For the second, D̂_TΨ = |T| D̂_(E₀)Ψ =
|T| (w₊ + w₋)/2, and |T|/2 = √c Ω̂; so |⟨L̂Ψ, D̂_TΨ⟩| ≤ |L̂Ψ| √c Ω̂ (|w₊| + |w₋|), and √c Ω̂ |w₊| ≤ √e_o and
Ω̂ |w₋| ≤ √e_i by [[lem:tl5-hf-densities]]. ∎

**Remark {#rem:tl5-hf-blocks}** (The blocks.) In the frame F, with π^MN the components of π raised with
η := diag(−1, 1, 1, 1, 1), S^MN := −(1/2)(π^MN − (1/2)(tr_η π) η^MN), D̂_M := D̂_(F_M) and 𝔇_M := 𝔇_(F_M), the terms
of [[eq:tl5-hf-bulk]] are

    −(1/2) π^(αβ) 𝕋_αβ = Σ_(M,N) S^MN ⟨D̂_MΨ, D̂_NΨ⟩,
    2⟨𝓡̂Ψ, D̂_TΨ⟩ − T^β⟨D̂^αΨ, 𝒞_αβΨ⟩
        = |T| (⟨w₊, (𝓡̂ − (1/2) 𝒞_10) Ψ⟩ + ⟨w₋, (𝓡̂ + (1/2) 𝒞_10) Ψ⟩ − Σ_j ⟨D̂_(f_j)Ψ, 𝒞_(j0) Ψ⟩),
    −ĝ^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ) + (1/2) ĝ^(γδ) 𝔇_T(D̂_γΨ, D̂_δΨ)
        = |T| (−Σ_M η^MM 𝔇_M(D̂_MΨ, D̂_0Ψ) + (1/2) Σ_M η^MM 𝔇_0(D̂_MΨ, D̂_MΨ)),
    2⟨Ψ, D̂_𝒵Ψ⟩ = 2z √c Ω̂ ⟨Ψ, w₊⟩ + 2z̲ (Ω̂/√c) ⟨Ψ, w₋⟩,

with D̂_0 = (w₊ + w₋)/2 and D̂_1 = (w₊ − w₋)/2 substituted, and the remaining terms 𝔇_𝒵(Ψ, Ψ) + |Ψ|² div 𝒵 form ℬ₀₀,
where div 𝒵 = z ∂_v log(Ω̂²R³) + z̲ (∂_u log(Ω̂²R³) + ∂_x b̂ + b̂ ∂_x log(Ω̂²R³)) + ∂_v z + ∂_u z̲. The second line uses
𝒞_00 = 0 and T = |T| E₀; the third uses ĝ^(αβ) ∂_α ⊗ ∂_β = Σ_M η^MM F_M ⊗ F_M. So the first-order blocks (ϰ, λ ≠ 0)
come from the deformation π of T and from 𝔇, that is from the acceleration and the deformation of the congruence of
E₀; the blocks (±, 0) are the operators |T|(𝓡̂ ∓ 𝒞_10/2)/2 + z √c Ω̂ (resp. z̲ Ω̂/√c) times the identity, the block
(∥, 0) is −|T|(𝒞_(j0))_j/2, and ℬ₀₀ is zeroth order. In particular, if T is a Killing field of ĝ, as for the
seed, the principal term vanishes. The formula for div 𝒵 follows from div(fV) = f div V + V(f) and from the
coordinate density Ω̂²R³/2 of the volume form in the coordinates (u, v, x, φ1, φ2) (proof of
[[lem:tl5-hf-identity]]): div ∂_v = ∂_v log(Ω̂²R³) and div(∂_u + b̂ ∂_x) = ∂_u log(Ω̂²R³) + ∂_x b̂ + b̂ ∂_x log(Ω̂²R³).

**Definition {#def:tl5-hf-rates}** (Admissible rates.) Let 𝔐 be a function on D^κ with values in the symmetric
m × m matrices with nonnegative off-diagonal entries, and ℰ_o, ℰ_i functions with values in the nonnegative diagonal
m × m matrices. Continuous functions a_o ≥ 0 on [−10, u*] and a_i ≥ 0 on [1/2, v*] are admissible rates for
(𝔐, ℰ_o, ℰ_i) if at every p ∈ D^κ and for every n ∈ ℝ^m with nonnegative entries

    nᵀ ((a_o + κ a_i) ℰ_o + (a_i + κ′ a_o) ℰ_i − 𝔐) n ≥ 0,      a_o = a_o(τ₁(p)), a_i = a_i(τ₂(p)).       {#eq:tl5-hf-admissible}

For level zero, m = 4 and (𝔐, ℰ_o, ℰ_i) = (𝔅, E_o, E_i).

Since the off-diagonal entries of the matrix in [[eq:tl5-hf-admissible]] are nonpositive, the condition for all n ≥ 0
is equivalent to positive semidefiniteness: for any n, nᵀMn ≥ |n|ᵀ M |n| when M has nonpositive off-diagonal entries,
|n| denoting the vector of absolute values. The condition is monotone in the tilt: rates that satisfy
[[eq:tl5-hf-admissible]] with κ = κ′ = 0 satisfy it for all κ, κ′ ≥ 0.

**Lemma {#lem:tl5-hf-allocation}** (Explicit admissible rates.) In the setting of [[def:tl5-hf-rates]] suppose that
for each index ϰ at least one of the diagonal entries (ℰ_o)_ϰϰ, (ℰ_i)_ϰϰ is positive everywhere. Let θ_ϰ be
measurable functions on D^κ with values in [0, 1], equal to 1 where (ℰ_i)_ϰϰ = 0 and to 0 where (ℰ_o)_ϰϰ = 0, and
t_ϰλ > 0 measurable functions for ϰ < λ, with t_λϰ := 1/t_ϰλ. Put

    d_ϰ := max(0, 𝔐_ϰϰ + Σ_(λ≠ϰ) 𝔐_ϰλ t_ϰλ),
    α_o := max over ϰ with θ_ϰ > 0 of θ_ϰ d_ϰ/(ℰ_o)_ϰϰ,   α_i := max over ϰ with θ_ϰ < 1 of (1 − θ_ϰ) d_ϰ/(ℰ_i)_ϰϰ.  {#eq:tl5-hf-alpha}

If a_o(τ₁(p)) ≥ α_o(p) and a_i(τ₂(p)) ≥ α_i(p) at every p ∈ D^κ, then a_o and a_i are admissible. In particular, for
the bulk matrix of level zero, with the indices (+, −, ∥, 0),

    α_o = max(d₊/(cΩ̂²), θ_∥ d_∥/(cΩ̂²), θ₀ d₀/(2Ω̂² z̲)),      α_i = max(d₋/Ω̂², (1 − θ_∥) d_∥/Ω̂², (1 − θ₀) d₀/(2Ω̂² z)),

and continuous functions a_o ≥ sup {α_o(p) : τ₁(p) = ·} and a_i ≥ sup {α_i(p) : τ₂(p) = ·} are admissible.

*Proof.* For n ≥ 0 and ϰ ≠ λ, 2 𝔐_ϰλ n_ϰ n_λ ≤ 𝔐_ϰλ (t_ϰλ n_ϰ² + t_λϰ n_λ²), so nᵀ𝔐n ≤ Σ_ϰ d_ϰ n_ϰ². On the other
hand, as κ, κ′ ≥ 0 and the diagonal matrices are nonnegative, nᵀ((a_o + κa_i)ℰ_o + (a_i + κ′a_o)ℰ_i)n ≥
Σ_ϰ (a_o (ℰ_o)_ϰϰ + a_i (ℰ_i)_ϰϰ) n_ϰ² ≥ Σ_ϰ (θ_ϰ + (1 − θ_ϰ)) d_ϰ n_ϰ², by the choice of α_o and α_i. ∎

The functions θ_ϰ allocate the shared diagonal entries between the two families, point by point; they and the t_ϰλ are
free. Any choice gives admissible rates, and the rates enter the constants only through the integrals of
[[prop:tl5-hf-linear]]. The best rates for a given ĝ can be sought by optimising these choices over a partition of
D^κ; that search is not part of any proof.

**Proposition {#prop:tl5-hf-linear}** (The weighted linear estimate.) Let a ∈ [−10, u*], b ∈ [1/2, v*], let
(Ψ_ι)_(ι∈ℐ) be a finite family of C² symmetric 2-tensor fields on Q(a, b), each vanishing on N₀ ∩ Q(a, b), and m_ι > 0
weights; write e_o := Σ_ι m_ι e_o[Ψ_ι], e_i := Σ_ι m_ι e_i[Ψ_ι], and ε₁, ε₂ for the corresponding face densities
[[eq:tl5-hf-faces]]. Let a_o ≥ 0 and a_i ≥ 0 be continuous on [−10, u*] and [1/2, v*], Φ_o(t) := ∫_(−10)^t a_o,
Φ_i(t) := ∫_(1/2)^t a_i and φ := Φ_o(τ₁) + Φ_i(τ₂), and let s ≥ 0 be a bounded measurable function on Q(a, b) with

    Σ_ι m_ι 2Ω̂² div J[Ψ_ι] ≤ (a_o + κ a_i) e_o + (a_i + κ′ a_o) e_i + 2Ω̂² s (√e_o + √c √e_i)                 {#eq:tl5-hf-hyp}

at every point of Q(a, b), a_o and a_i evaluated at τ₁ and τ₂. For a′ ≤ a and b′ ≤ b let ℰ(a′, b′) be the left side of
[[eq:tl5-hf-identity]] for Q(a′, b′), summed over ι with the weights m_ι, and put

    Y² := sup {ℰ(a′, b′) : −10 ≤ a′ ≤ a, 1/2 ≤ b′ ≤ b},      Y_d² := ∫_(N₁ ∩ Q(a,b)) e^(−φ) e_o dμ dv,
    𝒮 := ∫_(−10)^a ‖2Ω̂² s‖_(1,t) dt + ∫_(1/2)^b ‖2√c Ω̂² s‖_(2,t) dt,                                    {#eq:tl5-hf-source}

where ‖f‖²_(1,t) := ∫_(Σ₁(t,b)) e^(−φ) f² dμ dτ₂/(1 − κκ′) and ‖f‖²_(2,t) := ∫_(Σ₂(a,t)) e^(−φ) f² dμ dτ₁/(1 − κκ′).
Then

    Y ≤ Y_d + 2𝒮.                                                                                   {#eq:tl5-hf-linear}

Moreover, the unweighted energies ℰ⁰ (the same with φ replaced by 0) satisfy ℰ⁰(a′, b′) ≤ e^(Φ_o(a′) + Φ_i(b′)) Y².
With δ and 𝒮₀ the quantities Y_d and 𝒮 with φ replaced by 0, and
y_sep² := sup_(a′ ≤ a) ∫_(Σ₁(a′,b)) ε₁ dμ dτ₂ + sup_(b′ ≤ b) ∫_(Σ₂(a,b′)) ε₂ dμ dτ₁, the sum of the two unweighted
suprema taken separately,

    y_sep ≤ F (δ + 2𝒮₀),      F² := 2 e^(Φ_o(a) + Φ_i(b)).                                                {#eq:tl5-hf-f}

*Proof.* Fix a′ ≤ a and b′ ≤ b. [[lem:tl5-hf-identity]] for each Ψ_ι on Q(a′, b′), summed with the weights, has no
contribution from N₀, since each Ψ_ι vanishes there, and its N₁-term is at most Y_d², as e_o ≥ 0. By
[[eq:tl5-hf-hyp]] its bulk is at most ∫_(Q(a′,b′)) e^(−φ) 2Ω̂² s (√e_o + √c √e_i) dμ du dv. In the coordinates
(τ₁, τ₂), du dv = dτ₁ dτ₂/(1 − κκ′), and the set Q(a′, b′) ∩ {τ₁ = t} is Σ₁(t, b′) ⊂ Σ₁(t, b). By the Cauchy–Schwarz
inequality on it, with e_o/(1 − κκ′) ≤ ε₁,

    ∫_(Σ₁(t,b′)) e^(−φ) 2Ω̂² s √e_o dμ dτ₂/(1 − κκ′) ≤ ‖2Ω̂² s‖_(1,t) (∫_(Σ₁(t,b′)) e^(−φ) ε₁ dμ dτ₂)^(1/2)
      ≤ ‖2Ω̂² s‖_(1,t) ℰ(t, b′)^(1/2) ≤ ‖2Ω̂² s‖_(1,t) Y,

since ε₂ ≥ 0 and Q(t, b′) is in the family of the supremum. Integrating over t ∈ [−10, a′] and treating the term with
√c √e_i alike on the sets Σ₂(a′, t) ⊂ Σ₂(a, t), with e_i/(1 − κκ′) ≤ ε₂, gives ℰ(a′, b′) ≤ Y_d² + 2Y𝒮. Taking the
supremum, Y² ≤ Y_d² + 2Y𝒮, so Y ≤ 𝒮 + (𝒮² + Y_d²)^(1/2) ≤ Y_d + 2𝒮.

Since a_o, a_i ≥ 0, φ is nondecreasing in τ₁ and τ₂, and on Q(a′, b′) it is at most Φ_o(a′) + Φ_i(b′); hence
ℰ⁰(a′, b′) ≤ e^(Φ_o(a′) + Φ_i(b′)) ℰ(a′, b′). Each of the two suprema in y_sep² is at most a supremum of ℰ⁰ over the
family, so y_sep² ≤ 2 e^(Φ_o(a) + Φ_i(b)) Y². Finally φ ≥ 0 gives Y_d ≤ δ and 𝒮 ≤ 𝒮₀. ∎

**Corollary {#cor:tl5-hf-level0}** (Level zero.) Let a_o, a_i be admissible rates for (𝔅, E_o, E_i), and Ψ a C²
symmetric 2-tensor field on Q(a, b) vanishing on N₀ ∩ Q(a, b). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ) with
weight 1 and s := |L̂Ψ|, and so [[eq:tl5-hf-linear]] and [[eq:tl5-hf-f]] hold.

*Proof.* By [[lem:tl5-hf-divergence]] and [[lem:tl5-hf-pointwise]], 2Ω̂² div J ≤ nᵀ𝔅n + 2Ω̂² |L̂Ψ| (√e_o + √c √e_i),
and by [[eq:tl5-hf-admissible]], nᵀ𝔅n ≤ (a_o + κa_i) e_o + (a_i + κ′a_o) e_i, as e_o = nᵀE_on and e_i = nᵀE_in. ∎

**Remark {#rem:tl5-hf-weight}** (The weight.) The weight e^(−φ) lets each density be paid by the rate of its own family
at each point, and the estimate [[eq:tl5-hf-linear]] has constant 1 in the weighted norm; the factor e^(φ/2) appears
only on passing to unweighted energies. The rates need not be functions of τ₁ and τ₂ separately: the proof uses
only that dφ(J) dominates the bulk, and any C¹ function φ ≥ 0 with ∂_(τ₁)φ ≥ 0, ∂_(τ₂)φ ≥ 0 and
[[eq:tl5-hf-admissible]] at every point with (a_o, a_i) := (∂_(τ₁)φ, ∂_(τ₂)φ) gives [[eq:tl5-hf-linear]], with
F² = 2 e^(φ(a, b)).

#### Commutation {#sec:tl5-hf-commutation}

**Definition {#def:tl5-hf-fields}** (The commutation fields.) Write S³ ⊂ ℂ² = ℝ⁴ with z₁ = X₁ + iX₂ and
z₂ = X₃ + iX₄, so that x = |z₁|² − |z₂|² and φ_i = arg z_i, and for 1 ≤ a < b ≤ 4 let K_ab := X_a ∂_(X_b) − X_b ∂_(X_a),
the rotation fields of S³, extended to D̄ independently of (u, v). Put

    Γ := {T, K₁₂, K₃₄, K₁₃, K₁₄, K₂₃, K₂₄},      π^Z := ℒ_Z ĝ   (Z ∈ Γ).

For a word I = (Z₁, …, Z_j) in Γ put |I| := j and ℒ^I := ℒ_(Z₁) ⋯ ℒ_(Z_j), ℒ^∅ := 1; for a symmetric 2-tensor field
h, Ψ_I := ℒ^I h.

**Lemma {#lem:tl5-hf-fields}** (The commutation fields.) (a) Each Z ∈ Γ is smooth on D̄; K₁₂ = ∂_φ1, K₃₄ = ∂_φ2, and
Σ_(a<b) K_ab ⊗ K_ab = γ₀⁻¹. Hence the symmetric 3 × 3 matrix M_jl := Σ_(a<b) ĝ(K_ab, f_j) ĝ(K_ab, f_l) is positive
definite, with smallest eigenvalue

    λ_M = R² min(e^(−2(P + Q)), e^(2P), e^(2Q)),                                                          {#eq:tl5-hf-lambda}

and the coefficients c^ab_j := Σ_l (M⁻¹)_jl ĝ(K_ab, f_l) satisfy Σ_(a<b) c^ab_j K_ab = f_j and
Σ_j |Σ_(a<b) c^ab_j v_ab|² ≤ λ_M⁻¹ Σ_(a<b) |v_ab|² for vectors v_ab of any Euclidean space.

(b) π^(K₁₂) = π^(K₃₄) = 0 for every background, and for the seed π^Z = 0 for every Z ∈ Γ.

(c) For every background and every Z ∈ Γ, π^Z(ê₄, ê₄) = π^Z(ê₃, ê₃) = 0; and π^(K_ab)(ê₄, Y) = 0 for Y tangent to the
leaves.

*Proof.* (a) K_ab is the restriction to S³ of a linear vector field of ℝ⁴ tangent to S³, so it is smooth; with
z₁ = √((1 + x)/2) e^(iφ1) and z₂ = √((1 − x)/2) e^(iφ2), K₁₂ and K₃₄ generate the rotations of φ1 and φ2. For
ω ∈ S³ and a covector ζ of ℝ⁴, Σ_(a<b) (X_a ζ_b − X_b ζ_a)² = |X|²|ζ|² − (X·ζ)² = |ζ − (X·ζ)X|², which is γ₀⁻¹ applied
to the restriction of ζ to TS³; so Σ K_ab ⊗ K_ab = γ₀⁻¹. With γ̂ the metric of the leaf, M is the matrix of γ₀⁻¹ in the
frame γ̂(f_j, ·), so its eigenvalues are those of γ̂ relative to γ₀. In the chart (x, φ1, φ2), γ̂ and γ₀ are diagonal
with ratios e^(2ζ) · 4(1 − x²) = R² e^(−2(P + Q)), e^(2A) · 2/(1 + x) = R² e^(2P) and e^(2B) · 2/(1 − x) = R² e^(2Q),
by [[eq:tl5-radii]]; at the axes by continuity. Next Σ_ab c^ab_j K_ab = Σ_(l,m) (M⁻¹)_jl M_lm f_m = f_j, since K_ab is
tangent to the leaves. The matrix C := (c^ab_j) is M⁻¹G with G_(l,ab) := ĝ(K_ab, f_l) and GGᵀ = M, so CCᵀ = M⁻¹ and
the operator norm of C is λ_M^(−1/2).

(b) The components of ĝ in (u, v, x, φ1, φ2) do not depend on φ1 and φ2. The seed of [[lem:tl5-seed]] is of the
class with b̂ = 0 and P = Q = 0, so its leaves are round of radius R and the K_ab are Killing for it, and T is its
static Killing field (the remark after [[def:tl5-hf-frame]]).

(c) For a vector field Z and a vector field V, π^Z(V, V) = 2ĝ(D̂_V Z, V) = 2V(ĝ(Z, V)) − 2ĝ(Z, D̂_V V). The background is
a warped product over its orbit space, which is totally geodesic ([[lem:warped-ricci]], proof: no Christoffel symbol
with one index φ_i and two orbit indices), so D̂_(ê₄) ê₄ = 2ω ê₄ and D̂_(ê₃) ê₃ = 2ω̲ ê₃ with ω := ê₄(W),
ω̲ := ê₃(W), by [[lem:tl5-connection]]. For K = K_ab, ĝ(K, ê₄) = ĝ(K, ê₃) = 0, as K is tangent to the leaves and
ĝ(∂_x, ê₃) = −e^(2ζ) b̂ + b̂ e^(2ζ) = 0; so π^K(ê₄, ê₄) = −4ω ĝ(K, ê₄) = 0 and π^K(ê₃, ê₃) = 0. For T = ê₄ + c ê₃,
with ê₄(c) = 0, π^T(ê₄, ê₄) = 2c ĝ(D̂_(ê₄) ê₃, ê₄) = 2c (ê₄(ĝ(ê₃, ê₄)) − ĝ(ê₃, 2ω ê₄)) = 2c(−4ω Ω̂² + 4ω Ω̂²) = 0,
and π^T(ê₃, ê₃) = 2ĝ(D̂_(ê₃) ê₄, ê₃) + 2ê₃(c) ĝ(ê₃, ê₃) + 2c ĝ(D̂_(ê₃) ê₃, ê₃) = 2(−4ω̲ Ω̂² + 4ω̲ Ω̂²) = 0. Finally
[ê₄, K] = 0, so for Y tangent to the leaves π^K(ê₄, Y) = ĝ(D̂_K ê₄, Y) + ĝ(D̂_Y K, ê₄) = ĝ(D̂_K ê₄, Y) − ĝ(K, D̂_Y ê₄),
which vanishes because (X, Y) ↦ ĝ(D̂_X ê₄, Y) is symmetric on vectors tangent to the leaves: its antisymmetric part is
−ĝ(ê₄, [X, Y]) for leaf-tangent extensions, and [X, Y] is tangent to the leaves. ∎

By (c), in π^(αβ) D̂_αD̂_βΨ the components D̂²Ψ(ê₃, ê₃) and D̂²Ψ(ê₄, ê₄) never occur, and for the rotations
D̂²Ψ(ê₃, f_j) does not occur either: the coefficient of D̂²Ψ(ê₃, f_j) is a multiple of π(ê₄, f_j).

**Lemma {#lem:tl5-hf-commutator}** (The commutator.) For a symmetric 2-tensor field δ let

    Γ′[δ]^ρ_αβ := (1/2) ĝ^(ρσ) (D̂_α δ_σβ + D̂_β δ_σα − D̂_σ δ_αβ),

and let 𝒦[δ] be the second-order operator

    (𝒦[δ]Ψ)_μν := −δ^(αβ) D̂_αD̂_βΨ_μν − ĝ^(αβ) Γ′^ρ_αβ D̂_ρΨ_μν − 2ĝ^(αβ) (Γ′^ρ_αμ D̂_βΨ_ρν + Γ′^ρ_αν D̂_βΨ_μρ)
                 − ĝ^(αβ) ((D̂_αΓ′)^ρ_βμ Ψ_ρν + (D̂_αΓ′)^ρ_βν Ψ_μρ) + 2 (D𝓡̂[δ]Ψ)_μν,                             {#eq:tl5-hf-k}

indices of δ raised with ĝ, Γ′ = Γ′[δ], and D𝓡̂[δ] := (d/dt) 𝓡̂_(ĝ + tδ)|_(t=0), the derivative of the operator 𝓡̂
of [[lem:tl5-wg-linear]] for the metric ĝ + tδ: with δR̂^ρ_σμν = D̂_μ Γ′^ρ_νσ − D̂_ν Γ′^ρ_μσ and δR̂ic_σν = δR̂^ρ_σρν, it
is (D𝓡̂[δ]Ψ)_αβ = δ(R_αμβν g^(μa) g^(νb)) Ψ_ab − (1/2) δ(Ric_αρ g^(ρa)) Ψ_aβ − (1/2) Ψ_αa δ(g^(aρ) Ric_ρβ), each δ the
derivative at t = 0 along ĝ + tδ, with δg^(μa) = −δ^(μa) and δR_αμβν = ĝ_αλ δR̂^λ_μβν + δ_αλ R̂^λ_μβν. Then for every
vector field Z on D̄ and every C³ symmetric 2-tensor field Ψ,

    L̂ ℒ_Z Ψ = ℒ_Z L̂Ψ − 𝒦[π^Z] Ψ.                                                                          {#eq:tl5-hf-comm}

*Proof.* For a metric g let L_g := □_g + 2𝓡_g. For a diffeomorphism σ, σ*(L_g Ψ) = L_(σ*g)(σ*Ψ), as L_g is built from
g alone. Let σ_t be the local flow of Z near an interior point. Differentiating σ_t*(L̂Ψ) = L_(σ_t*ĝ)(σ_t*Ψ) at t = 0,
with (d/dt) σ_t*ĝ|_(t=0) = π^Z, gives ℒ_Z L̂Ψ = (d/dt) L_(ĝ + tπ^Z)Ψ|_(t=0) + L̂ ℒ_ZΨ, at interior points and by
continuity on D̄. It remains to compute the derivative of L_(ĝ+tδ)Ψ at t = 0. Along g_t := ĝ + tδ the connection
changes by the tensor Γ′ := (d/dt) Γ(g_t)|_(t=0) = Γ′[δ]. So (d/dt) (D_tΨ)_βμν = −Γ′^ρ_βμ Ψ_ρν − Γ′^ρ_βν Ψ_μρ,
and differentiating D_t(D_tΨ) gives

    (d/dt) (D_tD_tΨ)_αβμν = −D̂_α(Γ′^ρ_βμ Ψ_ρν + Γ′^ρ_βν Ψ_μρ) − Γ′^ρ_αβ D̂_ρΨ_μν − Γ′^ρ_αμ D̂_βΨ_ρν − Γ′^ρ_αν D̂_βΨ_μρ.

Contracting with ĝ^(αβ), using the symmetry of Γ′ in its lower indices and (d/dt) g_t^(αβ) = −δ^(αβ), gives the first
four terms of [[eq:tl5-hf-k]]; the last is the derivative of 2𝓡. The formula for δR̂ is the variation of the curvature
under a change Γ′ of the connection, and δRic is its contraction. ∎

Two more identities are used. For a tensor field A of type (0, r) and a vector field Z,

    ℒ_Z(D̂A) − D̂(ℒ_Z A) = −Γ′[π^Z] ⋆ A,      (Γ′ ⋆ A)_(αμ₁⋯μ_r) := Σ_i Γ′^ρ_(αμ_i) A_(μ₁⋯ρ⋯μ_r),        {#eq:tl5-hf-lie-d}

the index ρ in the i-th place; this is the derivative at t = 0 of σ_t*D̂ = D_(σ_t*ĝ), as in the proof above. And

    ℒ_ZΨ = D̂_ZΨ + Ψ(D̂Z ·, ·) + Ψ(·, D̂Z ·),      (Ψ(D̂Z ·, ·))(X, Y) := Ψ(D̂_X Z, Y),                     {#eq:tl5-hf-lie}

since D̂ is torsion free.

**Definition {#def:tl5-hf-triples}** (Second-order operators.) A second-order operator is a triple 𝔭 = (𝔭², 𝔭¹, 𝔭⁰)
of smooth tensor fields, acting by 𝔭Ψ := 𝔭² · D̂²Ψ + 𝔭¹ · D̂Ψ + 𝔭⁰ · Ψ, where · denotes a fixed contraction of all
indices of the derivative. By [[eq:tl5-hf-k]], 𝒦[π^Z] is such a triple, with 𝒦[π^Z]² the contraction with −(π^Z)^(αβ).
For a vector field W, define 𝔏_W 𝔭 by ℒ_W(𝔭Ψ) = 𝔭(ℒ_WΨ) + (𝔏_W 𝔭)Ψ; by [[eq:tl5-hf-lie-d]] applied to Ψ and to D̂Ψ,

    𝔏_W 𝔭 = (ℒ_W 𝔭², ℒ_W 𝔭¹ − 𝔭² · (Γ′ ⋆ ·) − 𝔭² · (Γ′ ⋆ ·)′, ℒ_W 𝔭⁰ − 𝔭² · (D̂Γ′ ⋆ ·) − 𝔭¹ · (Γ′ ⋆ ·)),
    Γ′ := Γ′[π^W],

where 𝔭² · (Γ′ ⋆ ·) is the first-order coefficient of Ψ ↦ 𝔭² · (Γ′ ⋆ D̂Ψ), and 𝔭² · (Γ′ ⋆ ·)′ and 𝔭² · (D̂Γ′ ⋆ ·)
are the first- and zeroth-order coefficients of Ψ ↦ 𝔭² · D̂(Γ′ ⋆ Ψ); so 𝔏_W 𝔭 is again a second-order operator, and
its coefficients are explicit in the jets of 𝔭, of W and of ĝ.

**Lemma {#lem:tl5-hf-system}** (The commuted equation.) Let h be a C^(N+2) symmetric 2-tensor field and
I = (Z₁, …, Z_j) a word, j ≤ N. Then

    L̂Ψ_I = ℒ^I L̂h − Σ_(k=1)^j Σ_(S ⊂ {1, …, k−1}) (𝔏_(Z_S) 𝒦[π^(Z_k)]) Ψ_(J(k,S)),                            {#eq:tl5-hf-system}

where, for S = {s₁ < ⋯ < s_m}, 𝔏_(Z_S) := 𝔏_(Z_(s₁)) ⋯ 𝔏_(Z_(s_m)), and J(k, S) is the word obtained from
(Z₁, …, Z_(k−1)) by deleting the letters with indices in S, followed by (Z_(k+1), …, Z_j); |J(k, S)| = j − 1 − |S|.

*Proof.* By [[eq:tl5-hf-comm]] and induction on j, L̂Ψ_I = ℒ^I L̂h − Σ_k ℒ_(Z₁) ⋯ ℒ_(Z_(k−1)) (𝒦[π^(Z_k)]Ψ_(Z_(k+1)⋯Z_j)).
By the definition of 𝔏 and induction on m, ℒ_(W₁) ⋯ ℒ_(W_m)(𝔭Ψ) = Σ_(S ⊂ {1,…,m}) (𝔏_(W_S) 𝔭)(ℒ_(W_(S^c)) Ψ), the
complement taken in its order: for m = 1 this is the definition, and applying ℒ_(W₁) to the identity for (W₂, …, W_m)
splits each term into the term with 1 ∉ S and the term with 1 ∈ S. ∎

For the seed every operator in the sum vanishes, since π^Z = 0 for all Z ∈ Γ.

**Lemma {#lem:tl5-hf-recovery}** (Recovery of second derivatives.) At a point p of D̄ let H be a symmetric tensor of
type (2, 0) with |H| ≤ 1/4, and Ψ a C² symmetric 2-tensor field near p. Put 𝔣 := L̂Ψ + H^(αβ) D̂_αD̂_βΨ at p,

    K_rec := max(|T|⁻¹, λ_M^(−1/2)),      𝔷_Z := 3 |D̂Z| |D̂Ψ| + 2 |D̂²Z| |Ψ|   (Z ∈ Γ),

with λ_M of [[eq:tl5-hf-lambda]], and let ‖𝓡̂‖ and ‖𝒞_(·1)‖ be the operator norms of Ψ ↦ 𝓡̂Ψ and of
Ψ ↦ (𝒞_(M1)Ψ)_(M=0,…,4) on 𝒮_p. Then at p

    (1 − (4/3)|H|) |D̂²Ψ| ≤ (√3 + 8/3) K_rec ((Σ_(Z∈Γ) |D̂ ℒ_ZΨ|²)^(1/2) + (Σ_(Z∈Γ) 𝔷_Z²)^(1/2))
                          + (4/3) |𝔣| + ((8/3)‖𝓡̂‖ + √2 ‖𝒞_(·1)‖) |Ψ|.                                       {#eq:tl5-hf-recovery}

For H = 0 the proof gives D̂²Ψ(p) as an explicit linear function ℛ_p of (D̂ℒ_ZΨ(p))_(Z∈Γ), D̂Ψ(p), Ψ(p) and L̂Ψ(p),
with coefficients built from the 2-jets of ĝ and of the fields Z at p.

*Proof.* Write D̂²Ψ(A, B) for the second covariant derivative in the frame directions F_A, F_B, and let X be the sum of
|D̂²Ψ(A, B)|² over all A and all B ≠ 1. By [[eq:tl5-hf-lie]], for Z ∈ Γ and every A,

    D̂_A(ℒ_ZΨ) = Z^B D̂²Ψ(A, B) + 𝔷_(Z,A),
    𝔷_(Z,A) := (D̂_A Z)^B D̂_BΨ + (D̂_AΨ)(D̂Z ·, ·) + (D̂_AΨ)(·, D̂Z ·) + Ψ(D̂_A D̂Z ·, ·) + Ψ(·, D̂_A D̂Z ·),

and (Σ_A |𝔷_(Z,A)|²)^(1/2) ≤ 𝔷_Z, each contraction being bounded by the product of the norms. Since T = |T| E₀,
D̂²Ψ(A, 0) = |T|⁻¹ (D̂_A ℒ_TΨ − 𝔷_(T,A)); since f_j = Σ_ab c^ab_j K_ab ([[lem:tl5-hf-fields]] (a)),
D̂²Ψ(A, j) = Σ_ab c^ab_j (D̂_A ℒ_(K_ab)Ψ − 𝔷_(K_ab,A)). By [[lem:tl5-hf-fields]] (a) and Minkowski's inequality,

    X^(1/2) ≤ K_rec ((Σ_Z |D̂ℒ_ZΨ|²)^(1/2) + (Σ_Z 𝔷_Z²)^(1/2)).

For A ≠ 1, D̂²Ψ(A, 1) = D̂²Ψ(1, A) + 𝒞_(A1)Ψ, and D̂²Ψ(1, A) is a term of X; so
Σ_(A≠1) |D̂²Ψ(A, 1)|² ≤ 2X + 2‖𝒞_(·1)‖² |Ψ|². For the entry (1, 1), ĝ^(αβ) D̂_αD̂_βΨ = −D̂²Ψ(0, 0) + D̂²Ψ(1, 1) +
Σ_j D̂²Ψ(j, j) and H^(αβ) D̂_αD̂_βΨ = Σ_(M,N) H^MN D̂²Ψ(M, N), with |H^MN| the frame components of H; so

    (1 + H^11) D̂²Ψ(1, 1) = 𝔣 − 2𝓡̂Ψ + D̂²Ψ(0, 0) − Σ_j D̂²Ψ(j, j) − Σ_((M,N)≠(1,1)) H^MN D̂²Ψ(M, N).

With |H^11| ≤ |H| ≤ 1/4 and |D̂²Ψ(0, 0)| + Σ_j |D̂²Ψ(j, j)| ≤ 2X^(1/2), four terms of X,
|D̂²Ψ(1, 1)| ≤ (4/3)(|𝔣| + 2‖𝓡̂‖|Ψ| + 2X^(1/2) + |H| |D̂²Ψ|). Finally |D̂²Ψ| ≤ (3X + 2‖𝒞_(·1)‖²|Ψ|²)^(1/2) +
|D̂²Ψ(1, 1)| ≤ √3 X^(1/2) + √2 ‖𝒞_(·1)‖ |Ψ| + |D̂²Ψ(1, 1)|, and collecting gives [[eq:tl5-hf-recovery]]. For H = 0
every step is an identity between the frame components, which defines ℛ_p. ∎

**Definition {#def:tl5-hf-coupling}** (The couplings at level N.) Fix N ≥ 1 and μ ∈ (0, 1]. For a C^(N+2) symmetric
2-tensor field h put 𝔤 := L̂h. At a point p, substitute in [[eq:tl5-hf-system]], for each word I with |I| ≤ N, every
second derivative D̂²Ψ_J (|J| < |I|) by ℛ_p of [[lem:tl5-hf-recovery]] with Ψ := Ψ_J, using D̂ℒ_ZΨ_J = D̂Ψ_(ZJ) and
L̂Ψ_J given again by [[eq:tl5-hf-system]]; after finitely many steps this writes

    L̂Ψ_I(p) = Σ_(|J|≤|I|) 𝔄_IJ (D̂Ψ_J(p), Ψ_J(p)) + Σ_(|J|≤|I|) 𝔔_IJ (ℒ^J 𝔤(p)),

with 𝔔_II the identity, 𝔄_IJ zero on Ψ_J when |J| = |I|, and every 𝔄_IJ, 𝔔_IJ a linear map built from the jets of ĝ
and of the fields Γ at p, of order at most N + 3, and independent of h. For levels j′ ≤ j ≤ N and ϰ ∈ {+, −, ∥, 0}
let ℭ_(jj′ϰ)(p) be the operator norm of the map (ξ_ϰ[Ψ_J])_(|J|=j′) ↦ (𝔄_IJ-part)_(|I|=j) from the ϰ-components of
the jets of level j′ (in the notation of [[def:tl5-hf-blocks]]) to the family (L̂Ψ_I)_(|I|=j), and 𝔮_(jj′)(p) that of
(ℒ^J𝔤)_(|J|=j′) ↦ (𝔔_IJ ℒ^J𝔤)_(|I|=j), in the Euclidean norms of the families; 𝔮_(jj) = 1. Let 𝔅_N be the symmetric
matrix of size 4(N + 1), indexed by (j, ϰ), with

    𝔅_N := diag(𝔅, …, 𝔅) + 𝔒 + 𝔒ᵀ,      𝔒_((j,σ),(j′,ϰ)) := √c Ω̂³ μ^((j − j′)/2) ℭ_(jj′ϰ)   (σ ∈ {±}, j′ ≤ j),  {#eq:tl5-hf-bn}

the other entries of 𝔒 being zero, and E_o^N, E_i^N the block diagonal matrices with N + 1 copies of E_o and E_i.

The maps 𝔄_IJ with |J| = |I| come only from the recovery of D̂²Ψ_(I′) with |I′| = |I| − 1: they are the
same-level couplings. All couplings vanish for the seed.

**Proposition {#prop:tl5-hf-linear-n}** (The linear estimate at level N.) Let h be a C^(N+2) symmetric 2-tensor field
on Q(a, b) whose partial derivatives of order at most N vanish on N₀ ∩ Q(a, b), 𝔤 := L̂h, and let a_o, a_i be
admissible rates for (𝔅_N, E_o^N, E_i^N). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ_I)_(|I|≤N) with the weights
μ^|I| and

    s_N[𝔤] := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) G_(j′))²)^(1/2),      G_(j′) := (Σ_(|J|=j′) |ℒ^J 𝔤|²)^(1/2),     {#eq:tl5-hf-sn}

and so [[eq:tl5-hf-linear]] and [[eq:tl5-hf-f]] hold for it.

*Proof.* Each Ψ_I is a combination of partial derivatives of h of order at most |I| with smooth coefficients, so it
vanishes on N₀ ∩ Q(a, b). At a point, let n^(j)_ϰ := (Σ_(|I|=j) |ξ_ϰ[Ψ_I]|²)^(1/2) and ñ^(j) := μ^(j/2) n^(j). Since
𝔅 has nonnegative off-diagonal entries, the Cauchy–Schwarz inequality over the words of level j gives
Σ_(|I|=j) n[Ψ_I]ᵀ 𝔅 n[Ψ_I] ≤ n^(j)ᵀ 𝔅 n^(j), so by [[lem:tl5-hf-pointwise]] the terms ℬ contribute at most
Σ_j ñ^(j)ᵀ 𝔅 ñ^(j). By [[lem:tl5-hf-divergence]] the remaining terms are −2Ω̂² Σ_I μ^|I| ⟨L̂Ψ_I, D̂_TΨ_I⟩, and
|⟨L̂Ψ_I, D̂_TΨ_I⟩| ≤ √c Ω̂ |L̂Ψ_I| (|w₊[Ψ_I]| + |w₋[Ψ_I]|). By the Cauchy–Schwarz inequality over the words of level
j and [[def:tl5-hf-coupling]],

    Σ_(|I|=j) |L̂Ψ_I| (|w₊| + |w₋|) ≤ (n^(j)_+ + n^(j)_−) (Σ_(j′≤j) Σ_ϰ ℭ_(jj′ϰ) n^(j′)_ϰ + Σ_(j′≤j) 𝔮_(jj′) G_(j′)).

Multiplied by 2√c Ω̂³ μ^j, the first part is 2√c Ω̂³ Σ μ^((j−j′)/2) ℭ_(jj′ϰ) (ñ^(j)_+ + ñ^(j)_−) ñ^(j′)_ϰ =
ñᵀ(𝔒 + 𝔒ᵀ)ñ; so the bulk without the source is at most ñᵀ𝔅_N ñ, which by admissibility is at most
(a_o + κa_i) e_o + (a_i + κ′a_o) e_i, as e_o = Σ_j ñ^(j)ᵀ E_o ñ^(j) and e_i likewise. The source part is
2√c Ω̂³ Σ_j μ^(j/2) 𝔊_j (ñ^(j)_+ + ñ^(j)_−) with 𝔊_j := Σ_(j′≤j) 𝔮_(jj′) G_(j′), and by the Cauchy–Schwarz inequality
over j, with c Ω̂² Σ_j (ñ^(j)_+)² ≤ e_o and Ω̂² Σ_j (ñ^(j)_−)² ≤ e_i, it is at most 2Ω̂² s_N[𝔤] (√e_o + √c √e_i). ∎

#### Bounds at a point {#sec:tl5-hf-sobolev}

**Lemma {#lem:tl5-hf-sphere}** (Sobolev on S³.) For f ∈ C²(S³) and ω ∈ S³,

    |f(ω)|² ≤ 6 C_(S³)² ∫_(S³) (f² + Σ_(a<b) (K_ab f)² + Σ_(a<b) Σ_(c<d) (K_cd K_ab f)²) dω,
    C_(S³)² := Σ_(n≥0) (n + 1)²/(2π² (1 + n(n + 2))²).                                                   {#eq:tl5-hf-sphere}

*Proof.* Let f = Σ_n f_n be the expansion in spherical harmonics, f_n of degree n, with −Δf_n = n(n + 2) f_n, where
Δ is the Laplacian of γ₀; the space of degree n has dimension (n + 1)², and its reproducing kernel at (ω, ω) is
(n + 1)²/(2π²), the volume of S³ being 2π² = ∫ dω, so |f_n(ω)|² ≤ (n + 1)² ‖f_n‖²/(2π²) with ‖·‖ the norm of
L²(S³, dω). By the Cauchy–Schwarz inequality over n and Parseval's identity, |f(ω)| ≤ Σ_n (n + 1)(2π²)^(−1/2)
‖f_n‖ ≤ C_(S³) ‖(1 − Δ)f‖, the series converging as its terms are O(n⁻²). Since the K_ab are Killing fields of γ₀
with Σ K_ab ⊗ K_ab = γ₀⁻¹ ([[lem:tl5-hf-fields]] (a)), |df|²_(γ₀) = Σ (K_ab f)² and Δf = Σ_(a<b) K_ab K_ab f; so
‖(1 − Δ)f‖² = ‖f‖² + 2‖df‖² + ‖Δf‖² ≤ ‖f‖² + 2 Σ‖K_ab f‖² + 6 Σ ‖K_ab K_ab f‖², which is at most six times the
integral in [[eq:tl5-hf-sphere]]. ∎

**Definition {#def:tl5-hf-component}** (Components.) Let W_a := ∂_(X_a) − X_a Σ_b X_b ∂_(X_b) (a = 1, …, 4), the
projections of the coordinate fields of ℝ⁴ to TS³, and 𝒱 := (∂_u, ∂_v, W₁, …, W₄). For a tensor A of rank r at a
point let A_e be the array of its 6^r components on 𝒱 and |A|_e its Euclidean norm, and put

    𝔳² := Σ_(V∈𝒱) |V|²,      𝔴² := Σ_M (du(F_M)² + dv(F_M)² + |F_M − du(F_M) ∂_u − dv(F_M) ∂_v|²_(γ₀)).

Explicitly, |∂_v|² = 2cΩ̂², |∂_u| ≤ √(2/c) Ω̂ + |b̂| e^ζ, Σ_a |W_a|² = R² (e^(−2(P+Q)) + e^(2P) + e^(2Q)), and
𝔴² = 2(1 + c²)/|T|² + c² (1 − x²) s²/(2|T|²) + R⁻² (e^(2(P+Q)) + e^(−2P) + e^(−2Q)), all smooth on D̄.

**Lemma {#lem:tl5-hf-components}** (Components.) For a tensor A of rank r, |A|_e ≤ 𝔳^r |A| and |A| ≤ 𝔴^r |A|_e. For
a rotation K_ab, the components of ℒ_(K_ab) A and the derivative K_ab(A_e) differ by the action of an
antisymmetric matrix of norm at most 1 on each index in the place of a W, so |K_ab(A_e) − (ℒ_(K_ab) A)_e| ≤ r |A|_e;
and ∂_u, ∂_v commute with every field of 𝒱, so ∂(A_e) = (ℒ_∂ A)_e for ∂ = ∂_u, ∂_v.

*Proof.* |A(V₁, …, V_r)| ≤ |A| Π|V_i|, and summing the squares over 𝒱^r gives the first inequality. On the leaves
Σ_a dX_a(Y) W_a = Y for Y ∈ TS³, as W_a = P∂_(X_a) with P the projection; so every vector Y equals
du(Y)∂_u + dv(Y)∂_v + Σ_a dX_a(Y_∥) W_a, with Y_∥ := Y − du(Y)∂_u − dv(Y)∂_v, and Σ_a dX_a(Y_∥)² = |Y_∥|²_(γ₀).
Expanding A(F_(M₁), …, F_(M_r)) in this way and applying the Cauchy–Schwarz inequality gives the second. K_ab is the
restriction of a linear field X ↦ BX with B antisymmetric of norm 1, and [K_ab, W_c] = Σ_d B_cd W_d, as the flow of
K_ab is a rotation commuting with the projection; [K_ab, ∂_u] = [K_ab, ∂_v] = 0. Then K_ab(A(V₁, …)) =
(ℒ_(K_ab)A)(V₁, …) + Σ_i A(…, [K_ab, V_i], …). The last statement holds as W_a does not depend on (u, v). The formula
for 𝔴 uses du(E₀) = c/|T|, dv(E₀) = 1/|T|, E₀ − (c ∂_u + ∂_v)/|T| = c b̂ ∂_x/|T|, |∂_x|²_(γ₀) = 1/(4(1 − x²)), the
same for E₁ with −c, and Σ_j |f_j|²_(γ₀) = tr_(γ̂) γ₀; those for 𝔳 use [[eq:tl5-hf-null-pair]],
|∂_x| = e^ζ and Σ_a |W_a|² = tr_(γ₀) γ̂, with the ratios of the proof of [[lem:tl5-hf-fields]] (a). ∎

**Lemma {#lem:tl5-hf-sobolev}** (A Sobolev inequality on the future faces.) Let p ∈ D^κ, a := τ₁(p), b := τ₂(p), and
let A be a symmetric 2-tensor field on Q(a, b), with ℒ_(K)A and ℒ_(K′)ℒ_K A of class C¹ for all rotations K, K′, and
A = 0 on N₀ ∩ Q(a, b). Then, with ε₁ the face density [[eq:tl5-hf-faces]] and the sums over words J of length at
most two in the six rotations,

    |A(p)|² ≤ C_S(p)² Σ_(|J|≤2) ∫_(Σ₁(a,b)) ε₁[ℒ^J A] dμ dτ₂,
    C_S(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(Σ₁(a,b)) 𝔳⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),                    {#eq:tl5-hf-cs}

where 𝔭₂ := 2353, ∂_γ := ∂_v − κ′ ∂_u, |D̂∂_γ| is the norm of the (1, 1)-tensor D̂∂_γ, and
𝔨₁ := 3 max(1, κ′/c, κ′² b̂² e^(2ζ)/((c + κ′) Ω̂²)).

*Proof.* For ω ∈ S³ let γ_ω(v) := (a − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_p; its (u, v)-image is the face Σ₁(a, b) in
the (u, v)-plane, from N₀ to p, since dτ₂/dv = 1 − κκ′ > 0 along it, and its velocity is ∂_γ. For a function f on
Q(a, b) put 𝔈(f)(v) := ∫_(S³) (f² + Σ(K f)² + Σ(K′K f)²)(γ_ω(v)) dω. By [[lem:tl5-hf-components]] and
[[lem:tl5-hf-sphere]], |A(p)|² ≤ 𝔴(p)⁴ |A(p)|²_e ≤ 6C_(S³)² 𝔴(p)⁴ Σ 𝔈(A_(VV′))(v_p), the sum over the 36 components.
These vanish at v = 1/2, as A and its derivatives along N₀ do, so 𝔈(A_(VV′))(v_p) = ∫ ∂_v 𝔈 dv ≤
∫_(1/2)^(v_p) (𝔈(A_(VV′)) + 𝔈(∂_γ A_(VV′))) dv, by 2|f ∂_γ f| ≤ f² + (∂_γ f)²; here ∂_γ commutes with the K and with
the index actions, so ∂_γ(K′K A_(VV′)) = K′K((ℒ_(∂_γ)A)_(VV′)). By [[lem:tl5-hf-components]] with r = 2,
|K(B_e)| ≤ |(ℒ_K B)_e| + 2|B_e| and |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K B)_e| + 2|(ℒ_K B)_e| + 2|(ℒ_(K′)B)_e| + 4|B_e|; squaring
with (x + y + z + w)² ≤ 4(x² + y² + z² + w²) and summing over the six K and the 36 pairs gives
Σ_(VV′) 𝔈-integrand of B_(VV′) ≤ 𝔭₂ Σ_(|J|≤2) |ℒ^J B|²_e, with 𝔭₂ = 1 + 12·4 + 144·16. Apply this to B = A and to
B = ℒ_(∂_γ)A, using ℒ_(∂_γ) ℒ^J = ℒ^J ℒ_(∂_γ), |B|_e ≤ 𝔳² |B|, and ℒ_(∂_γ)B = D̂_(∂_γ)B + B(D̂∂_γ ·, ·) + B(·, D̂∂_γ ·),
so that |B|² + |ℒ_(∂_γ)B|² ≤ (1 + 8|D̂∂_γ|²)|B|² + 2|D̂_(∂_γ)B|². With ∂_γ = ê₄ − κ′ê₃ + κ′b̂ ∂_x,
|D̂_(∂_γ)B|² ≤ 3(cΩ̂²|w₊|² + κ′²(Ω̂²/c)|w₋|² + κ′² b̂² e^(2ζ) |∇̸B|²) ≤ 𝔨₁ (e_o[B] + κ′ e_i[B]), and
|B|² ≤ (e_o[B] + κ′ e_i[B])/(2Ω̂² z̲), by [[lem:tl5-hf-densities]]. Finally dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face,
and (e_o + κ′e_i)/(1 − κκ′) = ε₁. ∎

The same proof, with r slots in place of two, gives for a tensor field A of rank r on Q(a, b) vanishing on
N₀ ∩ Q(a, b), with 𝔭_r := 1 + 12r² + 144r⁴,

    |A(p)|² ≤ 6 C_(S³)² 𝔭_r 𝔴(p)^(2r) Σ_(|J|≤2) ∫_(Σ₁(a,b)) 𝔳^(2r) R⁻³ ((1 + 2r²|D̂∂_γ|²) |ℒ^J A|²
              + 2|∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′),                                                {#eq:tl5-hf-cs-r}

using |D̂_(∂_γ)B| ≤ |∂_γ| |D̂B| in place of the densities.

#### The reduced operator and its quadratic part {#sec:tl5-hf-quadratic}

**Lemma {#lem:tl5-hf-reduced}** (The reduced operator about ĝ.) Let g be a C² Lorentzian metric near a point,
h := g − ĝ, H := g⁻¹ − ĝ⁻¹, K_σμν := (1/2)(D̂_μ h_σν + D̂_ν h_σμ − D̂_σ h_μν) and C := g⁻¹K, the tensor
C^λ_μν = g^(λσ) K_σμν. Then

    −2 Ric^W(g) = −2 R̂ic + L̂h + N(h),      N(h) := H^(λσ) D̂_λD̂_σ h − 2 𝔠(H) h − 2 𝔮,                     {#eq:tl5-hf-n}

where, with D̂g^(λσ) = −g^(λμ) g^(σν) D̂h_μν and Υ^λ = g^(λσ) g^(μν) K_σμν,

    (𝔠(H)h)_αβ := −(1/2) H^(λσ) (R̂^ρ_βλα h_ρσ + R̂^ρ_σλα h_βρ + R̂^ρ_αλβ h_ρσ + R̂^ρ_σλβ h_αρ + R̂^ρ_λαβ h_ρσ),
    𝔮_αβ := (D̂_λ g^(λσ)) K_σαβ − (1/2) (D̂_β g^(λσ)) D̂_α h_λσ + C^λ_λσ C^σ_αβ − C^λ_βσ C^σ_λα
            − (1/2) ((D̂_β g^(μν)) K_αμν + (D̂_α g^(μν)) K_βμν) + (1/2) (D̂_β h_αλ + D̂_α h_βλ) Υ^λ.

So g solves the reduced equation [[eq:tl5-wg-reduced]] if and only if L̂h = 2R̂ic − N(h). Each term of 2𝔮 is a
contraction of g⁻¹ ⊗ g⁻¹ ⊗ D̂h ⊗ D̂h, and the sum of the absolute values of its coefficients, counted over the
monomials obtained by expanding K, is 16; 2𝔠(H)h is a sum of five contractions of H ⊗ R̂ ⊗ h with coefficient 1.

*Proof.* Since D̂ĝ = 0, D̂g = D̂h, and the difference of the connections is C. The standard formula for the Ricci
tensor of a connection D̂ + C reads Ric(g)_αβ = R̂ic_αβ + D̂_λ C^λ_αβ − D̂_β C^λ_λα + C^λ_λσ C^σ_αβ − C^λ_βσ C^σ_λα,
with C^λ_λα = (1/2) g^(λσ) D̂_α h_λσ. In [[eq:tl5-wg-def]], g_αλ D̂_β Υ^λ = D̂_β 𝒱_α − (D̂_β h_αλ) Υ^λ with
𝒱_α := g_αλ Υ^λ = g^(μν)(D̂_μ h_αν − (1/2) D̂_α h_μν). Expanding, the terms with two derivatives of h are

    (1/2) g^(λσ) ([D̂_λ, D̂_α] h_βσ + [D̂_λ, D̂_β] h_ασ) − (1/2) g^(λσ) D̂_λD̂_σ h_αβ + (1/4) g^(μν) [D̂_α, D̂_β] h_μν,

by pairing (1/2) g^(λσ) D̂_λD̂_α h_σβ from D̂_λC^λ_αβ with −(1/2) g^(μν) D̂_αD̂_μ h_βν from −(1/2)D̂_α𝒱_β, the same with α
and β exchanged, and −(1/2) g^(λσ) D̂_βD̂_α h_λσ from −D̂_βC^λ_λα with (1/4) g^(μν)(D̂_βD̂_α + D̂_αD̂_β) h_μν from the
gauge term. By the convention of [[lem:tl5-wg-linear]], [D̂_μ, D̂_ν] h_αβ = −R̂^ρ_αμν h_ρβ − R̂^ρ_βμν h_αρ, and the
commutator terms are 𝔠(g⁻¹)h, with g⁻¹ in place of H (the last term of 𝔠 uses the symmetry of g^(μν) and of h). The
terms with products of first derivatives are 𝔮. So Ric^W(g) = R̂ic − (1/2) g^(λσ) D̂_λD̂_σ h + 𝔠(g⁻¹)h + 𝔮. Applied to
ĝ + th and differentiated at t = 0, this gives (d/dt)Ric^W = −(1/2)□̂h + 𝔠(ĝ⁻¹)h, as 𝔮 is quadratic in h; by
[[eq:tl5-wg-lin]], 𝔠(ĝ⁻¹)h = −𝓡̂h. Since 𝔠 is linear in its first argument, −2Ric^W(g) = −2R̂ic + □̂h + 2𝓡̂h +
H^(λσ)D̂_λD̂_σh − 2𝔠(H)h − 2𝔮. The count: the six groups of 𝔮 contribute 3/2, 1/2, 3/4, 9/4, 3/2 and 3/2, since K is
one half of a sum of three index permutations of D̂h and 𝒱 a sum of two monomials with coefficients 1 and 1/2. ∎

**Definition {#def:tl5-hf-levels}** (Low and high quantities.) Fix N ≥ 5. For a C^(N+2) symmetric 2-tensor field h
with g = ĝ + h Lorentzian, put at each point

    𝔰 := max(|H|, |Ψ_B| (|B| ≤ N − 2), |D̂Ψ_B| (|B| ≤ N − 3), |D̂²Ψ_B| (|B| ≤ N − 4)),
    𝔧 := max(𝔰, |Ψ_B|, |D̂Ψ_B| (|B| ≤ N), |D̂²Ψ_B| (|B| ≤ N − 1)),

the maxima over words B in Γ. The tensors in the first line are the low quantities. Let Λ ≥ 1 be a bound at the point
for the norms of ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z], D̂ℒ^B Γ′[π^Z] and ℒ^B R̂ for all words B with |B| ≤ N and all
Z ∈ Γ, and put
𝔤₀ := √5 + 1/4 and, with the ordered Bell numbers F₀ = F₁ = 1, F₂ = 3, F₃ = 13, F₄ = 75, F₅ = 541,
F_k = Σ_(r) r! S(k, r) in general,

    β₁(k) := 1 + (2^(k+1) − 2) Λ,      β₂(k) := 1 + (7/3)(4^k − 1) Λ²,
    b_g(0) := 𝔤₀,   b_g(k) := F_k 𝔤₀^(k+1) (Λ + 1)^k,   b_H(0) := 1,   b_H(k) := (2k + 1) F_k 𝔤₀^(k+1) (Λ + 1)^k,
    𝔠_n := β₂(n) − 1 + Σ_(k=1)^n C(n, k) b_H(k) β₂(n − k) + 5Λ Σ_(k=0)^n C(n, k) 2^(n−k) b_H(k)
           + 16 Σ_(k₁+k₂+k₃+k₄=n) (n!/(k₁! k₂! k₃! k₄!)) b_g(k₁) b_g(k₂) β₁(k₃) β₁(k₄),                       {#eq:tl5-hf-cn}

C(n, k) the binomial coefficients and k ≥ 1 where not stated.

**Lemma {#lem:tl5-hf-quadratic}** (The quadratic terms.) Let N ≥ 5, h as in [[def:tl5-hf-levels]], and p a point with
𝔰(p) ≤ 1/8. Then for every word I with |I| ≤ N,

    |ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I| ≤ 𝔠_(|I|) 𝔰 𝔧   at p.                                                {#eq:tl5-hf-g}

*Proof.* As |h| ≤ 𝔰 ≤ 1/8, |H| ≤ 1/4 by [[lem:tl5-wg-norms]] (a), whose proof applies to the norm |·| as it uses only
a ĝ-orthonormal frame; so |g⁻¹| ≤ |ĝ⁻¹| + |H| ≤ 𝔤₀. Lie derivatives commute with contractions and obey Leibniz's
rule, so ℒ^I of a contraction of m factors is the sum, over the assignments of the letters of I to the factors with
the order kept, of the contractions of the Lie derivatives of the factors; there are n!/(k₁! ⋯ k_m!) assignments with
k_i letters on the i-th factor, n := |I|. A full contraction of tensors is bounded by the product of their norms.
Expand each Lie derivative of a factor as follows; a monomial is a contraction of background factors and of solution
factors, the latter among H, Ψ_B, D̂Ψ_B and D̂²Ψ_B.

(i) ℒ^J h = Ψ_J and ℒ^J R̂, of norm at most Λ.

(ii) ℒ^J D̂h = D̂Ψ_J + R′_J, where by [[eq:tl5-hf-lie-d]] R′_(ZJ) = ℒ_Z R′_J − Γ′[π^Z] ⋆ Ψ_J: each monomial of R′_J has one
coefficient ℒ^B Γ′[π^Z] and one solution factor Ψ_B, |B| < |J|, and their number m′_k (k := |J|) satisfies
m′_k ≤ 2m′_(k−1) + 2, m′₀ = 0; so ℒ^J D̂h is a sum of monomials with background norms of total at most β₁(k).

(iii) ℒ^J D̂²h = D̂²Ψ_J + R_J with R_(ZJ) = ℒ_Z R_J + [ℒ_Z, D̂²]Ψ_J and [ℒ_Z, D̂²]Ψ = −Γ′ ⋆ D̂Ψ − (D̂Γ′) ⋆ Ψ − Γ′ ⋆̃ D̂Ψ,
seven monomials, ⋆̃ the contraction in which D̂ falls on Ψ inside D̂(Γ′ ⋆ Ψ); Lie differentiation of a monomial with
solution factor D̂Ψ_B gives at most four monomials, by ℒ_Z D̂Ψ_B = D̂Ψ_(ZB) − Γ′ ⋆ Ψ_B, and of one with Ψ_B two; so the
number m_k of monomials of R_J satisfies m_k ≤ 4m_(k−1) + 7, m_k ≤ (7/3)(4^k − 1), each with at most two background
factors and one solution factor D̂Ψ_B or Ψ_B with |B| < k.

(iv) ℒ^J g⁻¹ = Σ (−1)^r g⁻¹ (ℒ^(B₁) g) g⁻¹ ⋯ (ℒ^(B_r) g) g⁻¹, the sum over the ordered sequences of r ≥ 1 disjoint
nonempty subwords B_i of J, in the order of J, covering J; this follows by induction from ℒ_Z g⁻¹ = −g⁻¹(ℒ_Z g)g⁻¹,
the new letter either starting a block at one of the r + 1 factors g⁻¹ or joining a block, so that there are
r! S(k, r) terms with r blocks, F_k in all. Here ℒ^B g = ℒ^B ĝ + Ψ_B with ℒ^B ĝ = ℒ^(B′) π^(Z) for B = (Z, B′), of norm
at most Λ. So ℒ^J g⁻¹ is a sum of monomials of total background norm at most b_g(k). For ℒ^J H = ℒ^J g⁻¹ − ℒ^J ĝ⁻¹,
write each difference of products of 2r + 1 factors as a telescoping sum of 2r + 1 terms, each with one difference
factor H or Ψ_(B_i) and the other factors among g⁻¹, ĝ⁻¹, ℒ^B g and ℒ^B ĝ; every monomial of ℒ^J H then contains a
solution factor, and the total background norm is at most b_H(k), |ĝ⁻¹| = √5 ≤ 𝔤₀.

By [[lem:tl5-hf-reduced]], with these expansions, ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I is a sum of monomials whose total
background norm, with the coefficients, is at most 𝔠_n: the first two terms of [[eq:tl5-hf-cn]] come from
H^(λσ)D̂_λD̂_σh, the term D̂²Ψ_I with all letters on D̂²h being the one subtracted; the third from the five terms of
2𝔠(H)h, the letters distributed over H, R̂ and h; the fourth from 2𝔮.

Every monomial has at least two solution factors, since each term of N(h) has two (H and D̂²h, H and h, D̂h and D̂h)
and each expansion above keeps one in every monomial. Call a solution factor high if it is not a low quantity: Ψ_B
with |B| ≥ N − 1, D̂Ψ_B with |B| ≥ N − 2, or D̂²Ψ_B with |B| ≥ N − 3. A monomial has at most one high factor. In the
terms from 𝔮 the solution factors are of the forms Ψ_B and D̂Ψ_B, carried by disjoint sets of letters, and two high
ones would need at least 2N − 4 > N letters. In the terms from H^(λσ)D̂_λD̂_σh the factors of the expansion of H are
of the form H or Ψ_B, those of D̂²h of the form D̂²Ψ_B, D̂Ψ_B or Ψ_B, one of them, and two high factors would need at
least (N − 1) + (N − 3) > N letters. In the terms from 𝔠, both are of the form H or Ψ_B, and 2(N − 1) > N. So each
monomial is bounded by its background norm times 𝔰^(q−1) 𝔧, q ≥ 2 the number of its solution factors, the high one or
any one of them bounded by 𝔧 and the others by 𝔰; and 𝔰^(q−1) ≤ 𝔰. ∎

**Lemma {#lem:tl5-hf-linfty}** (The low quantities at a point.) Let N ≥ 5, g a solution of the reduced problem on
D^κ_s, h := g − ĝ, and suppose that all partial derivatives of h of order at most N + 1 vanish on N₀ ∩ D^κ_s. For
p ∈ D^κ_s put a := τ₁(p), b := τ₂(p), let ℰ⁰_N(p) := Σ_(|I|≤N) ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂, the unweighted face energy
of all words of length at most N, and ϱ(p) := sup over Q(a, b) of max_(|J|≤N−1) |ℒ^J(2R̂ic)|. At points of D^κ_s let

    𝒥₁ := (Σ_(|C|≤N) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),   M₂ := max_(|C|≤N−1) |D̂²Ψ_C|,   𝔯₀ := (8/3)‖𝓡̂‖ + √2 ‖𝒞_(·1)‖,
    α_𝔄 := √2 max_(|C|≤N−1) Σ_J ‖𝔄_CJ‖,   q₁ := max_(|C|≤N−1) Σ_J ‖𝔔_CJ‖,
    k₁ := (6/5) ((√3 + 8/3) K_rec (1 + √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + 𝔯₀ + (4/3) α_𝔄),   k₂ := (8/5) q₁,
    k₃ := (8/5) max_(|C|≤N−1) (𝔠_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠_(|J|) + 1)),

with the maps of [[def:tl5-hf-coupling]] and 𝔠_n of [[eq:tl5-hf-cn]], and 𝔨₂ := (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²). If
𝔰 ≤ 𝔰₀ := min(1/8, 1/(2 sup_(Q(a,b)) k₃)) on Q(a, b), then

    𝔰(p) ≤ C_∞(p) ℰ⁰_N(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p),                                                    {#eq:tl5-hf-linfty}

with 𝔐 := Σ_(j≤N−3) 7^j the number of words of length at most N − 3, C_∞ := 2 max(2C_S, C₁, k₁(p) (2𝔐)^(1/2)
max(C_S, C₁)), C_(∞,ϱ) := 2 max(C_(1,ϱ), k₁(p) (2𝔐)^(1/2) C_(1,ϱ) + k₂(p)), C_S of [[eq:tl5-hf-cs]] and

    C₁² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ)² + 4|∂_γ|² (72Λ² + 8(k₁ + 1)²)),
    C_(1,ϱ)² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 32 |∂_γ|² k₂²) · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′).

*Proof.* By [[thm:tl5-wg]] (F4_W) g is vacuum, so by [[lem:tl5-hf-reduced]] L̂h = 2R̂ic − N(h); with 𝔤 := L̂h,
[[def:tl5-hf-coupling]] gives at every point, for |C| ≤ N − 1, L̂Ψ_C + H^(αβ)D̂_αD̂_βΨ_C = Σ_J 𝔄_CJ(D̂Ψ_J, Ψ_J) +
Σ_J 𝔔_CJ ℒ^J(2R̂ic) − Σ_(J≠C) 𝔔_CJ ℒ^J N(h) − (ℒ^C N(h) − H^(αβ)D̂_αD̂_βΨ_C). Each Ψ_I, |I| ≤ N, and each low
quantity vanishes on N₀, being built from derivatives of h of order at most N + 1.

*Second derivatives.* At a point of Q(a, b) apply [[lem:tl5-hf-recovery]] to Ψ_C, |C| ≤ N − 1, with the tensor H of
the solution, |H| ≤ 𝔰₀ ≤ 1/8, so 1 − (4/3)|H| ≥ 5/6. There (Σ_Z |D̂ℒ_ZΨ_C|²)^(1/2) ≤ 𝒥₁ and
(Σ_Z 𝔷_Z²)^(1/2) ≤ √7 (3 max|D̂Z| + 2 max|D̂²Z|) 𝒥₁, as Γ has seven fields; |D̂Ψ_J| + |Ψ_J| ≤ √2 𝒥₁; and by
[[lem:tl5-hf-quadratic]] |ℒ^J N(h)| ≤ |H| |D̂²Ψ_J| + 𝔠_(|J|) 𝔰𝔧 ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ N − 1, with
𝔧 ≤ max(𝒥₁, M₂). Hence M₂ ≤ k₁ 𝒥₁ + k₂ |ℒ^(≤N−1)(2R̂ic)| + k₃ 𝔰 max(𝒥₁, M₂), and with k₃𝔰 ≤ 1/2,

    M₂ ≤ 2(k₁ + 1) 𝒥₁ + 2k₂ max_(|J|≤N−1) |ℒ^J(2R̂ic)|.

*Zeroth order.* [[lem:tl5-hf-sobolev]] for A := Ψ_B, |B| ≤ N − 2, gives |Ψ_B(p)| ≤ C_S(p) ℰ⁰_N(p)^(1/2), since
ℒ^J Ψ_B = Ψ_(JB) and the words JB are distinct for distinct J; and |H(p)| ≤ 2|h(p)| by [[lem:tl5-wg-norms]] (a).

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] with r = 3 to A := D̂Ψ_B. For a word J of rotations,
|J| ≤ 2, ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′, with at most six monomials in R′ by the proof of [[lem:tl5-hf-quadratic]] (ii), each
a contraction of one coefficient of norm at most Λ with a Ψ_C; so |ℒ^J A| ≤ (1 + 6Λ) 𝒥₁, and, with Λ bounding also
the derivatives D̂ℒ^B Γ′[π^Z], |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁, as |JB| ≤ N − 1. There are 43 words J. On the face,
by [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]), so
∫ 𝒥₁² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ⁰_N(p) on Σ₁(a, b); inserting the bound for M₂, with (x + y)² ≤ 2x² + 2y², gives
|D̂Ψ_B(p)| ≤ C₁ ℰ⁰_N(p)^(1/2) + C_(1,ϱ) ϱ(p).

*Second order at low levels.* For |B| ≤ N − 4 every solution factor of every monomial of ℒ^B N(h) is low, so the proof
of [[lem:tl5-hf-quadratic]] gives |ℒ^B N(h)| ≤ (𝔠_(|B|) + 1) 𝔰², and the computation above at p, with every term of
𝒥₁ replaced by L := (Σ_(|C|≤N−3) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2) ≤ (2𝔐)^(1/2) (max(C_S, C₁) ℰ⁰_N^(1/2) + C_(1,ϱ) ϱ), as
all words involved have length at most N − 3, gives |D̂²Ψ_B(p)| ≤ k₁ L + k₂ ϱ + k₃ 𝔰(p)²; as k₃ 𝔰(p) ≤ 1/2, the
last term is at most 𝔰(p)/2. Taking the maximum of the four bounds and absorbing
𝔰(p)/2 gives [[eq:tl5-hf-linfty]]. ∎

**Lemma {#lem:tl5-hf-quasilinear}** (The quasilinear term.) Let H be a C¹ symmetric tensor field of type (2, 0) and Ψ a
C² symmetric 2-tensor field on Q(a, b), and put

    𝔟[Ψ]^α := H^(αβ) ⟨D̂_βΨ, D̂_TΨ⟩ − (1/2) T^α H^(βγ) ⟨D̂_βΨ, D̂_γΨ⟩.

(a) div 𝔟 = H^(αβ) ⟨D̂_αD̂_βΨ, D̂_TΨ⟩ + 𝔮_H[Ψ], where, with |D̂Ψ|² := Σ_M |D̂_(F_M)Ψ|²,
𝔡 := max {|𝔇_V(A, B)| : |V| = |A| = |B| = 1} and ‖𝒞_(·0)‖ the norm of Ψ ↦ (𝒞(F_M, E₀)Ψ)_M,

    |𝔮_H[Ψ]| ≤ ϰ_H |D̂Ψ|² + |H| |T| ‖𝒞_(·0)‖ |Ψ| |D̂Ψ|,
    ϰ_H := (√5 + 1/2) |T| |D̂H| + |H| (|D̂T| + (1/2)|div T| + (√5 + 1/2) 𝔡 |T|).                          {#eq:tl5-hf-qh}

(b) 2Ω̂² |dτ₁(𝔟)| ≤ θ_H (e_o[Ψ] + κ′ e_i[Ψ]) and 2Ω̂² |dτ₂(𝔟)| ≤ θ_H (e_i[Ψ] + κ e_o[Ψ]), where

    θ_H := (√2 + 1/2) |H| max((c + κ′)/min(c, κ′), (1 + κc)/(κc)).                                     {#eq:tl5-hf-theta}

*Proof.* (a) By [[eq:tl5-hf-dk]], D̂_α(H^(αβ)⟨D̂_βΨ, D̂_TΨ⟩) = (D̂_αH^(αβ))⟨D̂_βΨ, D̂_TΨ⟩ + H^(αβ)⟨D̂_αD̂_βΨ, D̂_TΨ⟩ +
H^(αβ)⟨D̂_βΨ, (D̂_αT)^δ D̂_δΨ + T^δ D̂_αD̂_δΨ⟩ + H^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ), and
(1/2) D̂_α(T^α H^(βγ)⟨D̂_βΨ, D̂_γΨ⟩) = (1/2)(div T) H^(βγ)⟨·,·⟩ + (1/2)(D̂_T H^(βγ))⟨D̂_βΨ, D̂_γΨ⟩ +
H^(βγ)⟨T^δ D̂_δD̂_βΨ, D̂_γΨ⟩ + (1/2) H^(βγ) 𝔇_T(D̂_βΨ, D̂_γΨ). The two terms with T^δ and two derivatives of Ψ differ
by H^(αβ) T^δ ⟨D̂_βΨ, 𝒞_αδ Ψ⟩. So 𝔮_H is the sum of the six remaining terms. Bounding each: a contraction of different
tensors by the product of their norms, the trace D̂_αH^(αβ) by √5 |D̂H|, |D̂_TΨ| ≤ |T| |D̂Ψ|, and
|Σ_(A,B) H^AB 𝔇_A(D̂_BΨ, X)| ≤ |H| √5 𝔡 |D̂Ψ| |X|, with T^δ 𝒞_αδ = |T| 𝒞(·, E₀), gives [[eq:tl5-hf-qh]].

(b) The covectors du and dv have the k-norms |du| = √2 c/|T| = √c/(√2 Ω̂) and |dv| = √2/|T| = 1/(√2 √c Ω̂), since
du(E₀) = −du(E₁) = c/|T|, dv(E₀) = dv(E₁) = 1/|T| and both vanish on the leaves; and dτ₁(T) = c + κ′,
dτ₂(T) = 1 + κc. Hence |dτ₁| |T| ≤ √2 (c + κ′), |dτ₂| |T| ≤ √2 (1 + κc), and

    |dτ₁(𝔟)| ≤ |H| (|dτ₁| |T| + (c + κ′)/2) |D̂Ψ|² ≤ (√2 + 1/2) (c + κ′) |H| |D̂Ψ|²,

and likewise |dτ₂(𝔟)| ≤ (√2 + 1/2)(1 + κc) |H| |D̂Ψ|². By [[lem:tl5-hf-densities]], e_o + κ′e_i ≥ cΩ̂²|w₊|² +
κ′Ω̂²|w₋|² + (c + κ′)Ω̂²|∇̸Ψ|² ≥ 2 min(c, κ′) Ω̂² |D̂Ψ|², and e_i + κe_o ≥ 2 min(1, κc) Ω̂² |D̂Ψ|² = 2κc Ω̂² |D̂Ψ|². ∎

**Lemma {#lem:tl5-hf-conversions}** (The norms of the local theory and of the double-null conversion.) Let
c_* := c(u*) = f(−u*)/2, the minimum of c on [−10, u*].

(a) At every point of D̄, |h|_k̂ ≤ |h|/c_* for every symmetric 2-tensor h. So |h| < c_* κ_m/2 at every point of a set X
gives |h|_k̂ < κ_m/2, hence |g⁻¹ − ĝ⁻¹|_k̂ < κ_m on X by [[lem:tl5-wg-norms]] (a): g is tilted on X with the strict
inequality that [[thm:tl5-wg]] (F3_W) requires.

(b) On the slice M_σ of [[def:tl5-dn-slice]], with the coordinates (u, v, ϑ), let ν := max_μ |∂_μ|, Γ̂_s :=
max_(λ,μ) |D̂_(∂_λ) ∂_μ| and Γ̂′_s := max_(κ,λ,μ) |D̂_(∂_κ) D̂_(∂_λ) ∂_μ|, the maxima over μ, λ, κ ∈ {u, v, ϑ}, all
norms those of k. Then for the quantity ε of [[eq:tl5-dn-eps]], for g_σ and ĝ_σ on a set B ∩ M_σ,

    ε ≤ ε_𝔰 · sup_(B ∩ M_σ) max(|h|, |D̂h|, |D̂²h|),
    ε_𝔰 := sup_(B ∩ M_σ) max(ν², ν³ + 2νΓ̂_s, ν⁴ + 5ν²Γ̂_s + 2νΓ̂′_s + 2Γ̂_s²),                         {#eq:tl5-hf-eps}

and |∂_u| ≤ √(2/c) Ω̂ + |b̂| e^ζ, |∂_v| = √(2c) Ω̂, |∂_ϑ| = R e^(−(P+Q)), the last since x = cos 2ϑ on M_σ.

*Proof.* (a) is [[lem:tl5-hf-khat]] with r = 2 and c ≤ 1. (b) The components are h_μν = h(∂_μ, ∂_ν), and
∂_λ(h_μν) = (D̂_(∂_λ)h)(∂_μ, ∂_ν) + h(D̂_(∂_λ)∂_μ, ∂_ν) + h(∂_μ, D̂_(∂_λ)∂_ν); differentiating once more gives ten terms,
the second derivative D̂²h(∂_κ, ∂_λ, ∂_μ, ∂_ν), five with one derivative of h and one D̂∂, two with D̂D̂∂ and two with
two factors D̂∂; each is bounded by the product of the norms. On M_σ, ∂_ϑ = −2 sin 2ϑ ∂_x and |∂_x| = e^ζ, with
e^ζ = R e^(−(P+Q))/(2(1 − x²)^(1/2)) by [[eq:tl5-radii]]. ∎
