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

The class subspace V_p at a point p is the eight-dimensional space of symmetric 2-tensors h with h(X, ∂_φi) = 0 for X
in span(∂_u, ∂_v, ∂_x) and h(∂_φ1, ∂_φ2) = 0, at points off the axes, and its closure at the axes; by
[[thm:tl5-wg]] (F4_W), g − ĝ lies in it for every solution g.

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
