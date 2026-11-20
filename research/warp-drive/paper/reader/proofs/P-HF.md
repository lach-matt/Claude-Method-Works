### The a priori estimate in the wave gauge {#sec:tl5-hf}

This section proves an a priori estimate for solutions of the reduced problem of [[sec:tl5-wg]] close to an explicit
background ĝ, in a norm Y built from characteristic energies with an exponential weight, and with it the hypotheses
(H1)–(H3) of [[lem:tl5-continuation]] in the wave gauge, every constant being an explicit function of the jets of ĝ.
The estimate has three parts. The first is a weighted energy identity for the linearised operator, the
five-dimensional tensor wave operator of ĝ with its curvature term, on the regions bounded by two hypersurfaces of the
tilted foliations of [[def:tl5-wg-domains]] ([[lem:tl5-hf-identity]]); the whole linear bulk is absorbed pointwise
by two rates, one for each family of hypersurfaces ([[def:tl5-hf-rates]]), and no Grönwall inequality is used
([[prop:tl5-hf-linear]]). The second is commutation with the static Killing field and the six rotations of the
first seed, whose deformation tensors measure only the departure of ĝ from the seed ([[lem:tl5-hf-commutator]]),
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

For the first seed, T is the static Killing field ∂_v + (f(−u)/2) ∂_u of [[lem:tl5-seed]], since there b̂ = 0. The
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
(∥, 0) is −|T|(𝒞_(j0))_j/2, and ℬ₀₀ is zeroth order. In particular, if T is a Killing field of ĝ, as for the first
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

(b) π^(K₁₂) = π^(K₃₄) = 0 for every background, and for the first seed π^Z = 0 for every Z ∈ Γ.

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

(b) The components of ĝ in (u, v, x, φ1, φ2) do not depend on φ1 and φ2. The first seed is of the class with
b̂ = 0, P = Q = 0, so its leaves are round of radius R and the K_ab are Killing for it, and T is its static Killing
field ([[lem:tl5-seed]] and the remark after [[def:tl5-hf-frame]]).

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

For the first seed every operator in the sum vanishes, since π^Z = 0 for all Z ∈ Γ.
