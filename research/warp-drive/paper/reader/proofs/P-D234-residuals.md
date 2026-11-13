### The residuals of two explicit approximants {#sec:tl5-residuals}

This section proves the residual bounds of [[ch:ten-l5]] for two explicit metrics of the class on the region of the
first seed where the solution is resolved. The metrics are polynomials in a chart whose coefficients are printed in
[[sec:tab-d-coefficients]]; the bounds are proved from those coefficients by Taylor's theorem and explicit
enclosures, and the resulting numbers are listed in [[sec:tab-d-points]] and [[sec:tab-d-boxes]]. No theorem of this
paper uses these bounds, and no bound for the residual over the whole region Π of [[eq:tl5-region]] is stated: no
argument of the paper uses one.

#### The chart and the approximants {#sec:tl5-objects}

**Definition {#def:tl5-chart}** (The chart.) Put a := 1/500, ξ_a := −arsinh 1500, ξ_b := −arsinh 50 and
h_ξ := (ξ_b − ξ_a)/2. For u ∈ [−4, −11/10] and v ∈ [11/20, 8/5] put

    ξ := arsinh((u + 1)/a),      t := (ξ − ξ_a)/h_ξ − 1,      σ := (40v − 43)/21.                    {#eq:tl5-chart}

The map (u, v) ↦ (t, σ) is a diffeomorphism onto [−1, 1]², and x ∈ (−1, 1) is the angular coordinate of the class.
The region of this section is

    Π := [−1, 1] × [−1, 1] × [−x₁, x₁],      x₁ := cos(π/32),                                        {#eq:tl5-region}

in the coordinates (t, σ, x). Since u + 1 = a sinh ξ, we have dξ/du = 1/(a cosh ξ), hence

    ∂_u = φ₁ ∂_t,   ∂_u² = φ₁² ∂_t² + φ₂ ∂_t,   ∂_v = (40/21) ∂_σ,
    φ₁ := 1/(a h_ξ cosh ξ),   φ₂ := −φ₁² h_ξ tanh ξ.                                                  {#eq:tl5-chain}

Here φ₁ = dt/du and φ₂ = d²t/du², since dφ₁/du = −sinh ξ/(a² h_ξ cosh³ ξ) = −φ₁² h_ξ tanh ξ.

**Definition {#def:tl5-approximants}** (The approximants.) Let T_k be the Chebyshev polynomial of degree k,
T_k(cos θ) = cos kθ. Each of the two tables of [[sec:tab-d-coefficients]] gives, for every F ∈ {R, m, n, W, s},
integers z^F_ijk (0 ≤ i ≤ 24, 0 ≤ j ≤ 30, 0 ≤ k ≤ 15); put C̃^F_ijk := z^F_ijk × 10⁻¹⁸ and ε₀ := 5 × 10⁻¹⁹. An
approximant of the first (second) kind is the metric

    g := −4 e^(2W) du dv + R² e^(−2(P+Q)) (dx − (1 − x²) s du)² / (4(1 − x²))
         + (1/2) R² (1 + x) e^(2P) dφ1² + (1/2) R² (1 − x) e^(2Q) dφ2²,                               {#eq:tl5-metric}

with P := (2(1 + x)m − (1 − x)n)/3 and Q := (2(1 − x)n − (1 + x)m)/3, whose fields are

    F(t, σ, x) := Σ_i Σ_j Σ_k C^F_ijk T_i(t) T_j(σ) T_k(x)                                             {#eq:tl5-fields}

for real numbers C^F_ijk with |C^F_ijk − C̃^F_ijk| ≤ ε₀ for all F, i, j, k, the C̃ taken from the first (second)
table. The printed approximants, C = C̃, are of these kinds. So are the two fitted approximants. Let U be the
discrete solution of the characteristic problem of [[ch:ten-l5]] on one null grid, and U₂ the discrete solution on
the grid of twice its null step, whose nodes are every second node of the first. The first fitted approximant is a
least-squares fit of U; the second is a fit of the Richardson combination (4U − U₂)/3, taken at the nodes of the
coarser grid, which removes the leading error of a scheme of second order in the null step. Each printed C̃ is the
corresponding fitted coefficient rounded to the nearest multiple of 10⁻¹⁸. Every result below holds for every
approximant of the kind named; f^(1)_ab and f^(2)_ab denote the residuals of approximants of the first and second
kind. At every point and on every box used below, R is positive ([[lem:tl5-positive]]), and there [[eq:tl5-metric]]
is a Lorentzian metric of the class [[eq:class-metric]].

**Definition {#def:tl5-residual}** (The residual.) Let Ω² := e^(2W), b := (1 − x²) s and

    l := ∂_v,   n̂ := (∂_u + b ∂_x)/(2Ω²),   e_x := e^(−ζ) ∂_x,   e_1 := e^(−A) ∂_φ1,   e_2 := e^(−B) ∂_φ2,

with ζ, A, B of [[eq:tl5-radii]] below; then g(l, n̂) = −1, g(e_x, e_x) = g(e_1, e_1) = g(e_2, e_2) = 1 and all other
products of these vectors vanish. The residual of g is the family of eight functions on Π

    f_ab := ρ Ric[g](e_a, e_b),   ρ := R⁴/√72,   ab ∈ {ll, ln, nn, lx, nx, xx, 11, 22}.               {#eq:tl5-residual}

The other components of Ric[g] in this frame vanish identically, by [[lem:warped-ricci]]. The factor ρ is 1/√𝒦₀,
where 𝒦₀ = 72/R⁸ is the Kretschmann scalar of the five-dimensional Tangherlini metric of unit mass at areal radius
R; we say that f_ab is measured in units of the curvature scale.

#### The residual in closed form {#sec:tl5-formula}

Write [[eq:tl5-metric]] as g = g3 + e^(2A) dφ1² + e^(2B) dφ2² with

    g3 := −4 e^(2W) du dv + e^(2ζ) (dx − b du)²,
    ζ := log R − (P + Q) − (1/2) log(4(1 − x²)),
    A := log R + P + (1/2) log((1 + x)/2),      B := log R + Q + (1/2) log((1 − x)/2).                 {#eq:tl5-radii}

Let L := ∂_v, Y := ∂_u + b ∂_x and E := e^(−ζ) ∂_x, so that g3(L, Y) = −2Ω², g3(E, E) = 1 and the other products
vanish. Define the six functions

    ω := L(W),   ω̲ := Y(W),   k := L(ζ),   k̲ := Y(ζ) + ∂_x b,   η := E(W),
    τ := e^(ζ − 2W) ∂_v b / 4.                                                                         {#eq:tl5-scalars}

**Lemma {#lem:tl5-connection}** (The connection of g3.) The Levi-Civita connection ∇ of g3 is given by

    ∇_L L = 2ω L,             ∇_L Y = 2Ω²(η + τ) E,     ∇_L E = (η + τ) L,
    ∇_Y L = 2Ω²(η − τ) E,     ∇_Y Y = 2ω̲ Y,             ∇_Y E = (η − τ) Y,
    ∇_E L = (η + τ) L + k E,  ∇_E Y = (η − τ) Y + k̲ E,  ∇_E E = (k̲ L + k Y)/(2Ω²).    {#eq:tl5-connection}

*Proof.* The brackets of the frame are [L, Y] = (∂_v b) ∂_x = 4Ω²τ E, [L, E] = ∂_v(e^(−ζ)) ∂_x = −k E and
[Y, E] = Y(e^(−ζ)) ∂_x − e^(−ζ)(∂_x b) ∂_x = −k̲ E. The table is torsion free: ∇_L Y − ∇_Y L = 4Ω²τ E,
∇_L E − ∇_E L = −k E and ∇_Y E − ∇_E Y = −k̲ E. It is metric: the only non-constant product is g3(L, Y) = −2Ω², and
X g3(L, Y) = g3(∇_X L, Y) + g3(L, ∇_X Y) reads −4Ω²ω = 2ω(−2Ω²) for X = L, −4Ω²ω̲ = 2ω̲(−2Ω²) for X = Y, and
−4Ω²η = −2Ω²(η + τ) − 2Ω²(η − τ) for X = E. The constant products are preserved: no ∇_X L has a Y-component, no
∇_X Y an L-component and no ∇_X E an E-component; and g3(∇_X L, E) + g3(L, ∇_X E) vanishes for X = L, Y, E (the sums
are 0 + 0, 2Ω²(η − τ) − 2Ω²(η − τ) and k − k), as does g3(∇_X Y, E) + g3(Y, ∇_X E) (2Ω²(η + τ) − 2Ω²(η + τ), 0 + 0
and k̲ − k̲). A torsion-free metric connection is the Levi-Civita connection. ∎

**Lemma {#lem:tl5-ricci3}** (The Ricci tensor of g3.) In the frame (L, Y, E),

    Ric[g3](L, L) = −L(k) + 2ωk − k²,
    Ric[g3](Y, Y) = −Y(k̲) + 2ω̲k̲ − k̲²,
    Ric[g3](L, E) = −L(η) + L(τ) + 2kτ,
    Ric[g3](Y, E) = −Y(η) − Y(τ) − 2k̲τ,
    Ric[g3](L, Y) = −L(k̲) − 2L(ω̲) − kk̲ + Ω²(2E(η) + 2E(τ) + 4η² + 8ητ − 4τ²),
    Ric[g3](E, E) = −2E(η) − 2η² − 2τ² + (L(k̲) + Y(k) + 2kk̲)/(2Ω²).                                  {#eq:tl5-ricci3}

*Proof.* With R(X, Z)V := ∇_X ∇_Z V − ∇_Z ∇_X V − ∇_[X,Z] V and the dual frame, Ric(Z, V) = −(g3(R(L, Z)V, Y) +
g3(R(Y, Z)V, L))/(2Ω²) + g3(R(E, Z)V, E). Since g3(R(X, Z)V, V′) is antisymmetric in (V, V′) and R(X, X) = 0,

    Ric(L, L) = ⟨R(E, L)L, E⟩,   Ric(Y, Y) = ⟨R(E, Y)Y, E⟩,   Ric(L, E) = −⟨R(Y, L)E, L⟩/(2Ω²),
    Ric(Y, E) = −⟨R(L, Y)E, Y⟩/(2Ω²),   Ric(L, Y) = −⟨R(Y, L)Y, L⟩/(2Ω²) + ⟨R(E, L)Y, E⟩,
    Ric(E, E) = −(⟨R(L, E)E, Y⟩ + ⟨R(Y, E)E, L⟩)/(2Ω²),

with ⟨·, ·⟩ := g3. Each curvature term is expanded with [[eq:tl5-connection]], the Leibniz rule
∇_X(φV) = X(φ)V + φ∇_X V and [X, Z] = ∇_X Z − ∇_Z X. For the first, [E, L] = kE and

    ∇_E ∇_L L = 2E(ω) L + 2ω((η + τ) L + k E),
    ∇_L ∇_E L = L(η + τ) L + 2ω(η + τ) L + L(k) E + k(η + τ) L,      ∇_[E,L] L = k(η + τ) L + k² E,

so R(E, L)L = (2E(ω) − L(η + τ) − 2k(η + τ)) L + (2ωk − L(k) − k²) E and ⟨R(E, L)L, E⟩ = −L(k) + 2ωk − k². The
same expansion gives

    ⟨R(E, Y)Y, E⟩ = −Y(k̲) − k̲² + 2ω̲k̲,          ⟨R(Y, L)E, L⟩ = 2Ω²(L(η) − L(τ) − 2kτ),
    ⟨R(L, Y)E, Y⟩ = 2Ω²(Y(η) + Y(τ) + 2k̲τ),     ⟨R(Y, L)Y, L⟩ = 4Ω² L(ω̲) − 4Ω⁴(η² + 2ητ − 3τ²),
    ⟨R(E, L)Y, E⟩ = −L(k̲) − kk̲ + 2Ω²(E(η) + E(τ) + η² + 2ητ + τ²),
    ⟨R(L, E)E, Y⟩ = 2Ω²(E(η) + E(τ) + (η + τ)²) − L(k̲) − kk̲,
    ⟨R(Y, E)E, L⟩ = 2Ω²(E(η) − E(τ) + (η − τ)²) − Y(k) − kk̲,

and substituting these into the six traces gives [[eq:tl5-ricci3]]. ∎

**Proposition {#prop:tl5-components}** (The eight components.) For ψ ∈ {A, B} put ψ_L := L(ψ), ψ_Y := Y(ψ),
ψ_E := E(ψ), and

    h_ψ(L, Y) := L(ψ_Y) − 2Ω²(η + τ) ψ_E,      h_ψ(E, E) := E(ψ_E) − (k̲ψ_L + kψ_Y)/(2Ω²),
    □ψ := −h_ψ(L, Y)/Ω² + h_ψ(E, E),           ⟨dψ, dχ⟩ := −(ψ_L χ_Y + ψ_Y χ_L)/(2Ω²) + ψ_E χ_E,
    M_ψ(L, L) := L(ψ_L) − 2ωψ_L + ψ_L ψ_L,     M_ψ(Y, Y) := Y(ψ_Y) − 2ω̲ψ_Y + ψ_Y ψ_Y,
    M_ψ(L, Y) := h_ψ(L, Y) + ψ_L ψ_Y,          M_ψ(E, E) := h_ψ(E, E) + ψ_E ψ_E,
    M_ψ(L, E) := L(ψ_E) − (η + τ)ψ_L + ψ_L ψ_E,  M_ψ(Y, E) := Y(ψ_E) − (η − τ)ψ_Y + ψ_Y ψ_E,

and N(X, Z) := Ric[g3](X, Z) − M_A(X, Z) − M_B(X, Z). Then

    f_ll = N(L, L) ρ,              f_ln = N(L, Y)/(2Ω²) · ρ,      f_nn = N(Y, Y)/(4Ω⁴) · ρ,
    f_lx = N(L, E) ρ,              f_nx = N(Y, E)/(2Ω²) · ρ,      f_xx = N(E, E) ρ,
    f_11 = −(□A + ⟨dA, dA⟩ + ⟨dA, dB⟩) ρ,      f_22 = −(□B + ⟨dB, dB⟩ + ⟨dA, dB⟩) ρ.    {#eq:tl5-components}

*Proof.* By [[lem:warped-ricci]], Ric[g](X, Z) = Ric[g3](X, Z) − Σ_ψ (∇∇ψ(X, Z) + X(ψ) Z(ψ)) for X, Z tangent to
the orbit space, and Ric[g](e_1, e_1) = e^(−2A) R11 = −(□A + |dA|² + ⟨dA, dB⟩), likewise for e_2. The Hessian is
∇∇ψ(X, Z) = X(Z(ψ)) − (∇_X Z)(ψ); by [[eq:tl5-connection]] it equals L(ψ_L) − 2ωψ_L on (L, L), Y(ψ_Y) − 2ω̲ψ_Y on
(Y, Y), h_ψ(L, Y) on (L, Y), L(ψ_E) − (η + τ)ψ_L on (L, E), Y(ψ_E) − (η − τ)ψ_Y on (Y, E) and h_ψ(E, E) on (E, E).
The inverse of g3 is −(L ⊗ Y + Y ⊗ L)/(2Ω²) + E ⊗ E, which gives □ψ and ⟨dψ, dχ⟩. Finally l = L, n̂ = Y/(2Ω²) and
e_x = E. ∎

*The derivatives.* Every quantity in [[eq:tl5-components]] is an explicit expression in x and in the values of the
five fields and their first and second derivatives in u, v and x. With ℓ_a := R_a/R and ℓ_ab := R_ab/R − ℓ_a ℓ_b for
a, b ∈ {u, v, x} (the derivatives of log R), S := P + Q = ((1 + x)m + (1 − x)n)/3 and w := (1 + x)(1 − x):

    S_a = ((1 + x)m_a + (1 − x)n_a)/3,   P_a = (2(1 + x)m_a − (1 − x)n_a)/3,   Q_a = (2(1 − x)n_a − (1 + x)m_a)/3
        for a ∈ {u, v, uu, uv, vv};
    S_x = (m − n + (1 + x)m_x + (1 − x)n_x)/3,           S_xx = (2m_x − 2n_x + (1 + x)m_xx + (1 − x)n_xx)/3,
    P_x = (2m + n + 2(1 + x)m_x − (1 − x)n_x)/3,         P_xx = (4m_x + 2n_x + 2(1 + x)m_xx − (1 − x)n_xx)/3,
    Q_x = (−2n − m + 2(1 − x)n_x − (1 + x)m_x)/3,        Q_xx = (−4n_x − 2m_x + 2(1 − x)n_xx − (1 + x)m_xx)/3,
    S_ax, P_ax, Q_ax (a ∈ {u, v}): S_x, P_x, Q_x with (m, n, m_x, n_x) replaced by (m_a, n_a, m_ax, n_ax);
    ζ_a = ℓ_a − S_a,  A_a = ℓ_a + P_a,  B_a = ℓ_a + Q_a   for a ∈ {u, v, uu, uv, vv, ux, vx};
    ζ_x = ℓ_x − S_x + x/w,   A_x = ℓ_x + P_x + 1/(2(1 + x)),   B_x = ℓ_x + Q_x − 1/(2(1 − x)),
    ζ_xx = ℓ_xx − S_xx + (1 + x²)/w²,   A_xx = ℓ_xx + P_xx − 1/(2(1 + x)²),   B_xx = ℓ_xx + Q_xx − 1/(2(1 − x)²);
    b_a = w s_a (a ∈ {u, v, uv, vv}),  b_x = w s_x − 2xs,  b_ax = w s_ax − 2x s_a (a ∈ {u, v}),
    b_xx = w s_xx − 4x s_x − 2s;     e^(−ζ) = 2√w e^S/R.                                 {#eq:tl5-derivatives}

Write μ := e^(−ζ), ϑ := e^(ζ − 2W)/4 (so τ = ϑ b_v) and Y(ζ) = ζ_u + bζ_x. Then ω = W_v, ω̲ = W_u + bW_x, k = ζ_v,
k̲ = ζ_u + bζ_x + b_x, η = μW_x, and

    L(k) = ζ_vv,   Y(k) = ζ_uv + bζ_vx,   L(k̲) = ζ_uv + b_v ζ_x + bζ_vx + b_vx,   L(ω̲) = W_uv + b_v W_x + bW_vx,
    Y(k̲) = ζ_uu + b_u ζ_x + bζ_ux + b_ux + b(ζ_ux + b_x ζ_x + bζ_xx + b_xx),
    L(η) = μ(W_vx − ζ_v W_x),   Y(η) = μ(W_ux + bW_xx − Y(ζ) W_x),   E(η) = μμ(W_xx − ζ_x W_x),
    L(τ) = τ(ζ_v − 2ω) + ϑ b_vv,   Y(τ) = τ(Y(ζ) − 2ω̲) + ϑ(b_uv + b b_vx),
    E(τ) = μ(τ(ζ_x − 2W_x) + ϑ b_vx),                                                    {#eq:tl5-frame-derivatives}

and for ψ ∈ {A, B}: ψ_L = ψ_v, ψ_Y = ψ_u + bψ_x, ψ_E = μψ_x, L(ψ_L) = ψ_vv, L(ψ_Y) = ψ_uv + b_v ψ_x + bψ_vx,
Y(ψ_Y) = ψ_uu + b_u ψ_x + bψ_ux + b(ψ_ux + b_x ψ_x + bψ_xx), L(ψ_E) = μ(ψ_vx − ζ_v ψ_x),
Y(ψ_E) = μ(ψ_ux + bψ_xx − Y(ζ) ψ_x), E(ψ_E) = μμ(ψ_xx − ζ_x ψ_x). The u- and v-derivatives of a field are those in
(t, σ) through [[eq:tl5-chain]]: F_u = φ₁F_t, F_uu = φ₁φ₁F_tt + φ₂F_t, F_uv = (40/21)φ₁F_tσ, F_ux = φ₁F_tx,
F_v = (40/21)F_σ, F_vv = (40/21)²F_σσ, F_vx = (40/21)F_σx. Each line follows from the definitions by the product and
chain rules; for instance ∂_x(−(1/2) log(1 − x²)) = x/w and ∂_x(x/w) = (1 + x²)/w².

*The order of evaluation.* [[eq:tl5-chain]], [[eq:tl5-components]], [[eq:tl5-derivatives]] and
[[eq:tl5-frame-derivatives]] are the formula used below. The enclosures of [[lem:tl5-jet-enclosure]] evaluate it one
operation at a time, and the following conventions fix every operation. Each quantity is formed from the expression
displayed for it, a product of several factors from left to right. A quotient p/q is the product p · (1/q), and a
square is a product: ℓ_a := R_a · (1/R), ℓ_ab := R_ab · (1/R) − ℓ_a ℓ_b, x/w := x · (1/w), η² := ηη, k² := kk,
k̲² := k̲k̲ and τ² := ττ. The remaining quantities are formed as

    cosh ξ := (e^ξ + e^(−ξ))/2,   sinh ξ := (e^ξ − e^(−ξ))/2,   tanh ξ := sinh ξ · (1/cosh ξ),
    φ₁ := 1/(cosh ξ · h_ξ a),   φ₂ := −(φ₁φ₁) tanh ξ · h_ξ,   w := (1 + x)(1 − x),   b := ws,
    S := ((1 + x)m + (1 − x)n)/3,   μ := 2√w · e^S · (1/R),   Ω² := e^(2W),   ϑ := (1/μ)(1/Ω²)/4,
    ρ := (RR)(RR)/√72,
    1/(2(1 ± x)) := (1/(1 ± x))/2,   1/(2(1 ± x)²) := (1/(1 ± x))(1/(1 ± x))/2,   (1 + x²)/w² := (1 + xx)(1/w)(1/w),
    X/Ω² := X · (1/Ω²),   X/(2Ω²) := X · (1/Ω²)/2,   X/(4Ω⁴) := X · (1/Ω²)(1/Ω²)/4,

where e^q, √q and 1/q are the exponential, the square root and the reciprocal of [[def:tl5-jets]] applied to the jet
q, and X is the numerator displayed. A factor that is a rational number or one of the numbers a, h_ξ, 40/21 and 1/√72
scales each interval exactly, so its place in a product does not change the result.

#### Bounds at points and on boxes {#sec:tl5-enclosures}

For a multi-index α = (α₁, α₂, α₃), a function f on Π and p ∈ Π write ∂^α := ∂_t^α₁ ∂_σ^α₂ ∂_x^α₃,
f_α(p) := ∂^α f(p)/α! (α! := α₁!α₂!α₃!) and |α| := α₁ + α₂ + α₃. A box is a set
𝔟 = {p : |p_d − c_d| ≤ h_d, d = 1, 2, 3} ⊂ Π with centre c and half-widths h; h^α := h₁^α₁ h₂^α₂ h₃^α₃.

**Lemma {#lem:tl5-taylor}** (One box.) For f ∈ C³(𝔟),

    sup_𝔟 |f| ≤ Σ_(|α|≤2) |f_α(c)| h^α + Σ_(|α|=3) sup_(p∈𝔟) |f_α(p)| h^α.                               {#eq:tl5-taylor}

*Proof.* By Taylor's formula with the Lagrange remainder, for p = c + y ∈ 𝔟 there is θ ∈ (0, 1) with
f(p) = Σ_(|α|≤2) f_α(c) y^α + Σ_(|α|=3) f_α(c + θy) y^α, and |y^α| ≤ h^α. ∎

**Lemma {#lem:tl5-chebyshev}** (Derivatives of the fields.) For F of [[eq:tl5-fields]] and every multi-index γ,
∂^γ F = Σ C^(F,γ)_ijk T_i(t) T_j(σ) T_k(x), where C^(F,γ) arises from C^F by applying γ₁ times in the first index,
γ₂ times in the second and γ₃ times in the third the map (c_i) ↦ (c′_i),

    c′_i := (2/(1 + δ_i0)) Σ_(i′ > i, i′ − i odd) i′ c_i′.                          {#eq:tl5-cheb-derivative}

Consequently |F_γ| ≤ Σ_ijk |C^(F,γ)_ijk|/γ! on [−1, 1]³.

*Proof.* The identity T′_k = 2k(T_(k−1) + T_(k−3) + …), with the last term T_0 halved when k is odd, follows from
T′_k(cos θ) = k sin kθ/sin θ and the identity 2 sin θ (cos (k−1)θ + cos (k−3)θ + …) = sin kθ, in which the last
term, cos 0 = 1, is again halved when k is odd. The latter telescopes by 2 sin θ cos mθ = sin (m + 1)θ − sin (m − 1)θ;
for k odd the halved term contributes sin θ. Summing over k gives [[eq:tl5-cheb-derivative]], and the bound follows
from |T_k| ≤ 1 on [−1, 1]. ∎

**Lemma {#lem:tl5-rounding}** (The rounding.) For n, a ≥ 0 one has T_n^(a)(1) = Π_(r<a) (n² − r²)/(2r + 1), and on
[−1, 1] one has |T_n^(a)| ≤ T_n^(a)(1). Hence, if two fields F and F̃ of the form [[eq:tl5-fields]] have
coefficients that differ by at most ε₀, then for every multi-index γ

    sup_([−1,1]³) |∂^γ F − ∂^γ F̃| ≤ ε₀ Θ_γ,      Θ_γ := Θ₂₄^(γ₁) Θ₃₀^(γ₂) Θ₁₅^(γ₃),   Θ_n^(a) := Σ_(i=0..n) T_i^(a)(1).
                                                                                       {#eq:tl5-rounding}

In particular Θ₂₄^(a) = 25, 4,900, 586,040, Θ₃₀^(a) = 31, 9,455, 1,754,848 and Θ₁₅^(a) = 16, 1,240, 59,024 for
a = 0, 1, 2, so that the values of the fields move by at most ε₀Θ_(0,0,0) = 6.2 × 10⁻¹⁵, their first derivatives in
t, σ and x by at most 1.3 × 10⁻¹², 1.9 × 10⁻¹² and 4.9 × 10⁻¹³, and their second derivatives in tt, tσ, tx, σσ, σx
and xx by at most 1.5 × 10⁻¹⁰, 3.8 × 10⁻¹⁰, 9.5 × 10⁻¹¹, 3.6 × 10⁻¹⁰, 1.5 × 10⁻¹⁰ and 2.3 × 10⁻¹¹.

*Proof.* T_n solves (1 − x²)y″ − xy′ + n²y = 0. Differentiating a times gives
(1 − x²)y^(a+2) − (2a + 1)x y^(a+1) + (n² − a²)y^(a) = 0, and at x = 1 this reads
(2a + 1) T_n^(a+1)(1) = (n² − a²) T_n^(a)(1); with T_n(1) = 1 the product formula follows. The map
[[eq:tl5-cheb-derivative]] has nonnegative entries, so T_n^(a) = Σ_l β_l T_l with β_l ≥ 0, and therefore one has
the bound |T_n^(a)(x)| ≤ Σ_l β_l = T_n^(a)(1), because |T_l| ≤ 1 = T_l(1). Then the difference of the fields
satisfies |∂^γ(F − F̃)| ≤ Σ_ijk |C_ijk − C̃_ijk| |T_i^(γ₁)| |T_j^(γ₂)| |T_k^(γ₃)| ≤ ε₀ Θ_γ. Finally
Θ_n^(1) = Σ i² and Θ_n^(2) = Σ i²(i² − 1)/3, whose values are the stated ones. ∎

*Enclosures of the fields.* For an approximant of either kind the coefficients are known only to lie within ε₀ of
the printed ones. For n, a ≥ 0 let 𝟙^(a)_n ∈ ℝ^(n+1) be the vector obtained from (1, 1, …, 1) by applying a times
the map [[eq:tl5-cheb-derivative]]; it is the coefficient vector of Σ_(i ≤ n) T_i^(a), its entries are nonnegative
integers, and their sum is Θ_n^(a). For a point c = (c₁, c₂, c₃) of [−1, 1]³, a field F and a multi-index γ put

    J^F_γ(c) := [F̃_γ(c) − r_γ(c), F̃_γ(c) + r_γ(c)],
    r_γ(c) := (ε₀/γ!) Π_(d=1,2,3) Σ_(l=0..n_d) (𝟙^(γ_d)_(n_d))_l |T_l(c_d)|,      (n₁, n₂, n₃) := (24, 30, 15),

with F̃ the printed field; the radius r_γ(c) depends neither on the field nor on the kind. Let Λ^F_γ be the number
(Σ_ijk |C̃^(F,γ)_ijk| + ε₀Θ_γ)/γ! rounded upward to four significant digits, where C̃^(F,γ) arises from the printed
coefficients as in [[lem:tl5-chebyshev]]; these numbers are printed in [[sec:tab-d-constants]].

**Lemma {#lem:tl5-centre}** (Enclosures of the fields.) For every approximant of either kind, every point
c ∈ [−1, 1]³, every field F and every multi-index γ, F_γ(c) ∈ J^F_γ(c), and |F_γ| ≤ Λ^F_γ on [−1, 1]³.

*Proof.* By [[lem:tl5-chebyshev]], ∂^γ(F − F̃) = Σ_ijk D_ijk T_i(t) T_j(σ) T_k(x), where D arises from the array
C^F − C̃^F by applying the map [[eq:tl5-cheb-derivative]] γ₁ times in the first index, γ₂ times in the second and γ₃
times in the third. The map has nonnegative entries and the entries of C^F − C̃^F lie in [−ε₀, ε₀], so, index by
index, the entries of D satisfy |D_ijk| ≤ ε₀ (𝟙^(γ₁)_24)_i (𝟙^(γ₂)_30)_j (𝟙^(γ₃)_15)_k. Multiplying by the
numbers |T_i(c₁)| |T_j(c₂)| |T_k(c₃)|, summing and dividing by γ! gives |F_γ(c) − F̃_γ(c)| ≤ r_γ(c). For the second
claim, by [[lem:tl5-chebyshev]] and [[lem:tl5-rounding]], the field satisfies |F_γ| ≤ |F̃_γ| + |F_γ − F̃_γ| ≤
Σ_ijk |C̃^(F,γ)_ijk|/γ! + ε₀Θ_γ/γ!, and rounding upward only increases the bound. ∎

**Lemma {#lem:tl5-field-box}** (Taylor coefficients of a field on a box.) Let 𝔟 be a box with centre c and
half-widths h, F a field of an approximant and γ a multi-index. For every p ∈ 𝔟, F_γ(p) lies in J^F_γ(c) enlarged on
each side by

    Σ_d (γ_d + 1) max|J^F_(γ+e_d)(c)| h_d + (1/2) Σ_(d,d′) (γ_d + 1)(γ_d′ + δ_dd′ + 1) Λ^F_(γ+e_d+e_d′) h_d h_d′,

where e_d is the d-th unit multi-index.

*Proof.* ∂_d F_γ = (γ_d + 1) F_(γ+e_d) and ∂_d′ ∂_d F_γ = (γ_d + 1)(γ_d′ + δ_dd′ + 1) F_(γ+e_d+e_d′). Taylor's formula
for F_γ at c to first order gives the claim, with F_(γ+e_d)(c) ∈ J^F_(γ+e_d)(c) and with the Lagrange remainder
bounded by the inequalities |F_(γ+e_d+e_d′)| ≤ Λ^F_(γ+e_d+e_d′) of [[lem:tl5-centre]]. ∎

**Definition {#def:tl5-jets}** (Jets and enclosures.) The jet of f at p is J_p f := (f_α(p))_(|α|≤3), twenty
numbers. For jets a, a′ put (a + a′)_α := a_α + a′_α and (aa′)_α := Σ_(β+β′=α) a_β a′_β′; for a jet a write a₀ for
its coefficient at α = 0 and ν := a − a₀ (the jet a with a₀ replaced by 0), with ν^j := ν^(j−1)ν, and put

    1/a := Σ_(j=0..3) (−1)^j a₀^(−j−1) ν^j,     √a := Σ_(j=0..3) binom(1/2, j) a₀^(1/2−j) ν^j,
    e^a := e^(a₀) Σ_(j=0..3) ν^j/j!.

Then J_p(fg) = (J_p f)(J_p g), J_p(1/f) = 1/J_p f, J_p √f = √(J_p f) and J_p e^f = e^(J_p f), because the Taylor
coefficients of order at most 3 of a product or of a composition depend only on those of the factors, and
ν⁴ = 0 in this product. An enclosure of a jet on a set is a family of closed intervals (I_α)_(|α|≤3) containing the
jet at every point of the set and for every approximant of the kind considered. Intervals are added and multiplied by
the endpoint rules [p₁, p₂] + [q₁, q₂] = [p₁ + q₁, p₂ + q₂] and [p₁, p₂][q₁, q₂] = [min, max] of the four products
p_i q_j. For a jet whose constant term lies in an interval [p₁, p₂], the coefficient e^(a₀) is increasing in a₀ and
is enclosed by its values at p₁ and p₂; when p₁ > 0, so are the coefficients a₀^(−j−1) and a₀^(1/2−j), which are
monotone in a₀.

**Lemma {#lem:tl5-jet-enclosure}** (The components on a box and at a point.) Let 𝔟 be a box in Π with centre c.
Enclose, for every field and |γ| ≤ 5, the coefficient F_γ on 𝔟 by [[lem:tl5-field-box]]; enclose the jets of x and
of ξ = ξ_a + (t + 1)h_ξ on 𝔟 (constant terms ranging over 𝔟, the coefficient 1 at (0, 0, 1) for x and h_ξ at
(1, 0, 0) for ξ, the others 0); and evaluate [[eq:tl5-chain]], [[eq:tl5-derivatives]], [[eq:tl5-frame-derivatives]]
and [[eq:tl5-components]] with jets, by the rules of [[def:tl5-jets]] and in the order fixed in [[sec:tl5-formula]],
the jet of ∂^δF (|δ| ≤ 2) having the coefficients ((α + δ)!/α!) F_(α+δ). Wherever a reciprocal or a square root is
formed, suppose the enclosure of the constant term is a positive interval. Then the result encloses J_p f_ab on 𝔟
for each ab, for every approximant of the kind. The same evaluation with the intervals J^F_γ(c) at the single point
c gives enclosures J^ab_α(c) of (f_ab)_α(c); with jets of order 0 it gives an interval containing f_ab(c) for every
approximant of the kind.

*Proof.* The jets the evaluation starts from contain, at every p ∈ 𝔟 and for every approximant, the jets at p of
the functions they stand for: for the fields by [[lem:tl5-field-box]], since the coefficient at α of the jet of
∂^δF at p is ((α + δ)!/α!) F_(α+δ)(p), and for x and ξ because these are affine in (t, x). Each step is a sum, a
product, a reciprocal, a square root or an exponential of jets with this property; by [[def:tl5-jets]] the exact
results are the jets at p of the corresponding functions, and the endpoint rules return intervals containing every
value the operation takes on the given intervals. Induction over the steps gives the claim on 𝔟; at c the same
argument applies with [[lem:tl5-centre]] in place of [[lem:tl5-field-box]]. ∎

**Definition {#def:tl5-certificate}** (The number of a box.) For a box 𝔟 with centre c and half-widths h, let

    κ_ab(𝔟) := Σ_(|α|≤2) max|J^ab_α(c)| h^α + Σ_(|α|=3) max|I^ab_α| h^α,      κ(𝔟) := max_ab κ_ab(𝔟),
                                                                                       {#eq:tl5-certificate}

with J^ab_α(c) and I^ab_α the enclosures of [[lem:tl5-jet-enclosure]] at c and on 𝔟, formed in the order fixed in
[[sec:tl5-formula]]. By [[lem:tl5-taylor]], sup_𝔟 max_ab |f_ab| ≤ κ(𝔟) for every approximant of the kind.
[[sec:tab-d-boxes]] gives, for every box of the subdivisions below, an integer v with κ(𝔟) ≤ v × 10⁻⁶. Another order
of the same operations also gives enclosures, by the same induction, and the number it gives in place of κ(𝔟) also
bounds sup_𝔟 max_ab |f_ab|; it need not equal κ(𝔟), and the tables bound κ(𝔟) itself. At a point p of G,
[[sec:tab-d-points]] gives an integer v such that the eight intervals of [[lem:tl5-jet-enclosure]] (jets of order 0)
containing the values f_ab(p) lie in [−vu, vu], with the unit u stated there.

#### The bounds {#sec:tl5-bounds}

Let d_k := (1 − cos(π/32))(3/2)^k for 0 ≤ k ≤ 9 and d_10 := 1/4. The grid G consists of the 24 × 24 × 28 = 16,128
points (t_p, t_q, x_r) with t_p := (2p − 23)/24 (0 ≤ p, q ≤ 23) and x_r running over the midpoints of the twenty
intervals [−1 + d_k, −1 + d_(k+1)] and [1 − d_(k+1), 1 − d_k] (0 ≤ k ≤ 9) and the eight numbers
−3/4 + (2r + 1)·3/32 (0 ≤ r ≤ 7); [[sec:tab-d-points]] numbers them x_0 < x_1 < … < x_27.

**Lemma {#lem:tl5-positive}** (Positivity.) Let 𝔟 be one of the boxes of the subdivisions in the proofs of
[[prop:tl5-box-first]] and [[prop:tl5-boxes-second]], and c a point of G. For every approximant of either kind, the
enclosure of R on 𝔟 by [[lem:tl5-field-box]] (γ = 0) lies in [1.80, ∞) and J^R_0(c) lies in [1.17, ∞). In the
evaluations of [[lem:tl5-jet-enclosure]] on 𝔟, at its centre and at c, the constant term of every reciprocal and of
every square root formed is a positive interval.

*Proof.* The lower ends of J^R_0(c) and of the enclosure of R on 𝔟 are the first numbers that the entries of
[[sec:tab-d-points]] and [[sec:tab-d-boxes]] require, and those sections record that they exceed 1.172 at every
point of G, for either kind, and 1.807, 4.431 and 2.549 on the boxes of Π*, of Π₁, Π₂ and Π₃, and of Π₄ (the boxes of
[[prop:tl5-box-first]] and [[prop:tl5-boxes-second]]). The enclosure of R at the centre of 𝔟 is J^R_0 there, which
lies inside the enclosure on 𝔟. The other quantities that are inverted or square-rooted are cosh ξ, cosh ξ · h_ξ a,
1 + x, 1 − x, w = (1 + x)(1 − x), μ and Ω². The constant terms of e^ξ and e^(−ξ) are positive, hence so is that of
cosh ξ. The boxes and the points lie in Π, so the constant terms of 1 ± x lie in [1 − x₁, 1 + x₁], and that of w is a
product of positive intervals. The constant terms of e^S and of Ω² = e^(2W) are positive, and that of
μ = 2√w · e^S · (1/R) is a product of positive intervals. ∎

**Proposition {#prop:tl5-points}** (The residuals at the points of G.) At every point of G and for every ab, every
approximant of the first kind satisfies |f^(1)_ab| ≤ 2.42 × 10⁻³ and every approximant of the second kind satisfies
the bound |f^(2)_ab| ≤ 3.73 × 10⁻⁵. Two approximants of the same kind have residuals that differ by at most
1.3 × 10⁻⁷ at every point of G. The largest values are taken by f_ll at (−23/24, 23/24, −21/32), where |f^(1)_ll|
lies in [2.4141, 2.4143] × 10⁻³, and at (−23/24, 23/24, x₆), x₆ := −1 + (d₆ + d₇)/2, where |f^(2)_ll| lies in
[3.715, 3.728] × 10⁻⁵. In particular 2.41 × 10⁻³ is not an upper bound for |f^(1)_ll| on G; the bound to three
significant figures is 2.42 × 10⁻³.

*Proof.* By [[lem:tl5-positive]], [[lem:tl5-jet-enclosure]] applies with jets of order 0 at every point of G, with
the intervals J^F_γ of [[lem:tl5-centre]], and gives eight intervals containing the values f_ab there for every
approximant of the kind. [[sec:tab-d-points]] lists, for each kind and each point, an integer v with these intervals
in [−vu, vu], where u = 10⁻⁵ for the first kind and u = 10⁻⁷ for the second; the largest entries are 242 and 373,
which gives the first two bounds. The same section lists, for each (p, q), an integer w_pq such that, for either
kind, each of these intervals at the points (t_p, t_q, x_r) has width at most w_pq × 10⁻⁹. The largest is 128. The
residuals of two approximants of one kind lie in the same interval, so they differ by at most 1.28 × 10⁻⁷, which is
at most 1.3 × 10⁻⁷.

That section lists also the interval of f_ll at the two points named: [−2.41424, −2.41411] × 10⁻³ for the first kind
at (t_0, t_23, x_10) = (−23/24, 23/24, −21/32), and [−3.72733, −3.71597] × 10⁻⁵ for the second kind at
(t_0, t_23, x_6). So there the values satisfy |f^(1)_ll| ∈ [2.41411, 2.41424] × 10⁻³ ⊂ [2.4141, 2.4143] × 10⁻³
and |f^(2)_ll| ∈ [3.71597, 3.72733] × 10⁻⁵ ⊂ [3.715, 3.728] × 10⁻⁵. At these two points the other seven intervals
lie in [−2.15 × 10⁻⁴, 2.15 × 10⁻⁴] and [−1.39 × 10⁻⁶, 1.39 × 10⁻⁶], and at every other point of G the entry of the
table is at most 239 for the first kind and 364 for the second. Since 2.41411 × 10⁻³ > 2.39 × 10⁻³ and
3.71597 × 10⁻⁵ > 3.64 × 10⁻⁵, the largest values of max_ab |f_ab| over G are those of f_ll at the two points named.
Finally 2.41411 × 10⁻³ > 2.41 × 10⁻³. ∎

**Proposition {#prop:tl5-box-first}** (The first kind on one box.) On Π* := [−1/2, 0] × [−1/2, 0] × [0, 1/4], every
approximant of the first kind satisfies

    sup_(Π*) max_ab |f^(1)_ab| ≤ 3.01 × 10⁻⁴.

*Proof.* Divide Π* into the 32³ = 32,768 boxes of half-widths (1/128, 1/128, 1/256). By [[lem:tl5-positive]],
[[lem:tl5-jet-enclosure]] applies on each box 𝔟 and at its centre, and by [[def:tl5-certificate]] the supremum of
max_ab |f^(1)_ab| over 𝔟 is at most κ(𝔟) for every approximant of the first kind, since κ(𝔟) is formed with the
intervals J^F_γ and the constants Λ^F_γ of [[lem:tl5-centre]]. [[sec:tab-d-boxes]] gives an integer v with
κ(𝔟) ≤ v × 10⁻⁶ for each of the boxes; the largest is 299, and 2.99 × 10⁻⁴ ≤ 3.01 × 10⁻⁴. ∎

**Proposition {#prop:tl5-boxes-second}** (The second kind on four boxes.) Let Π₁ := I_t × I_σ × [−21/32, −41/64],
Π₂ := I_t × I_σ × X₉, Π₃ := I_t × I_σ × X₈ and Π₄ := [−1/2, −3/8] × [3/8, 1/2] × [5/8, 11/16], where
I_t := [−31/32, −15/16], I_σ := [15/16, 31/32] and X_k is the eighth of the sixteen equal subintervals of
[−1 + d_k, −1 + d_(k+1)] counted from the left. Every approximant of the second kind satisfies

    sup_(Πi) max_ab |f^(2)_ab| ≤ 5.0 × 10⁻⁴   (i = 1, 2, 3, 4);

the bounds proved are 6.1 × 10⁻⁵, 4.92 × 10⁻⁴, 4.89 × 10⁻⁴ and 1.74 × 10⁻⁴. Each Πi contains a point of G at which
every approximant of the first kind has |f^(1)_ll| ≥ 1.09 × 10⁻³: (−23/24, 23/24, −21/32), (−23/24, 23/24,
−1 + (d₉ + d_10)/2), (−23/24, 23/24, −1 + (d₈ + d₉)/2) and (−11/24, 11/24, 21/32), where it is at least
2.414, 2.387, 2.347 and 1.095 × 10⁻³.

*Proof.* Divide Π₁ into 8³ equal boxes, Π₂ and Π₃ into 4³ and Π₄ into 16³. As in the proof of
[[prop:tl5-box-first]], [[sec:tab-d-boxes]] gives an integer v with κ(𝔟) ≤ v × 10⁻⁶ for each of the 4,736 boxes, and
the largest for Π₁, Π₂, Π₃ and Π₄ are 61, 492, 489 and 174. The four points are (t_0, t_23, x_10), (t_0, t_23, x_9),
(t_0, t_23, x_8) and (t_6, t_17, x_17). Since t_0 = −23/24 ∈ I_t and t_23 = 23/24 ∈ I_σ, the first lies in Π₁
(x_10 = −21/32 is the left end of its third factor), the second and the third lie in Π₂ and Π₃ (x_9 and x_8 are the
right ends of X₉ and X₈), and the fourth lies in Π₄. [[sec:tab-d-points]] lists the intervals of f^(1)_ll at these
points: [−2.41424, −2.41411] × 10⁻³, [−2.38766, −2.38753] × 10⁻³, [−2.34786, −2.34773] × 10⁻³ and
[1.09560, 1.09563] × 10⁻³. Their ends nearest 0 give the four lower bounds. ∎

**Remark {#rem:tl5-how-checked}** (Checking a row.) Each entry of the tables is a finite calculation with the printed
coefficients, the number ε₀, the constants Λ^F_γ and the rules of [[def:tl5-jets]], in the order fixed in
[[sec:tl5-formula]]. [[sec:tab-d-worked]] carries one box of [[prop:tl5-box-first]] through it completely: its
intervals at the centre, the constants Λ^F_γ, the enclosures of [[lem:tl5-field-box]], the jets of the quantities of
[[eq:tl5-components]] for the component that attains κ(𝔟), the coefficients of all eight components and the sum
[[eq:tl5-certificate]]. A printed interval contains the one these rules give, and a printed number is at least the
one these rules give; [[sec:tab-d-tables]] says where they differ.
