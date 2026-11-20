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
