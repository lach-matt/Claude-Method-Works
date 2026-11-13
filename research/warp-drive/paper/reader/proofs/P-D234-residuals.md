### The residuals of two explicit approximants {#sec:tl5-residuals}

This section proves the residual bounds of [[ch:ten-l5]] for two explicit metrics of the class on the region of the
first seed where the solution is resolved. The metrics are polynomials in a chart whose coefficients are printed in
[[sec:tab-d-coefficients]]; the bounds are proved from those coefficients by Taylor's theorem and explicit
enclosures, and the resulting numbers are listed in [[sec:tab-d-points]] and [[sec:tab-d-boxes]]. No theorem of this
paper uses these bounds, and no bound for the residual over the whole region Π of [[eq:tl5-region]] is stated: no
argument of the paper uses one.

#### The chart and the approximants {#sec:tl5-objects}

**Definition {#def:tl5-chart}** (the chart). Put a := 1/500, ξ_a := −arsinh 1500, ξ_b := −arsinh 50 and
h_ξ := (ξ_b − ξ_a)/2. For u ∈ [−4, −11/10] and v ∈ [11/20, 8/5] put

    ξ := arsinh((u + 1)/a),      t := (ξ − ξ_a)/h_ξ − 1,      σ := (40v − 43)/21.                    {#eq:tl5-chart}

The map (u, v) ↦ (t, σ) is a diffeomorphism onto [−1, 1]², and x ∈ (−1, 1) is the angular coordinate of the class.
The region of this section is

    Π := [−1, 1] × [−1, 1] × [−x₁, x₁],      x₁ := cos(π/32),                                        {#eq:tl5-region}

in the coordinates (t, σ, x). Since u + 1 = a sinh ξ, we have dξ/du = 1/(a cosh ξ), hence

    ∂_u = φ₁ ∂_t,   ∂_u² = φ₁² ∂_t² + φ₂ ∂_t,   ∂_v = (40/21) ∂_σ,
    φ₁ := 1/(a h_ξ cosh ξ),   φ₂ := −φ₁² h_ξ tanh ξ.                                                  {#eq:tl5-chain}

Here φ₁ = dt/du and φ₂ = d²t/du², since dφ₁/du = −sinh ξ/(a² h_ξ cosh³ ξ) = −φ₁² h_ξ tanh ξ.

**Definition {#def:tl5-approximants}** (the approximants). Let T_k be the Chebyshev polynomial of degree k,
T_k(cos θ) = cos kθ. Each of the two tables of [[sec:tab-d-coefficients]] gives, for every F ∈ {R, m, n, W, s},
integers N^F_ijk (0 ≤ i ≤ 24, 0 ≤ j ≤ 30, 0 ≤ k ≤ 15); put C̃^F_ijk := N^F_ijk × 10⁻¹⁸ and ε₀ := 5 × 10⁻¹⁹. An
approximant of the first (second) kind is the metric

    g := −4 e^(2W) du dv + R² e^(−2(P+Q)) (dx − (1 − x²) s du)² / (4(1 − x²))
         + (1/2) R² (1 + x) e^(2P) dφ1² + (1/2) R² (1 − x) e^(2Q) dφ2²,                               {#eq:tl5-metric}

with P := (2(1 + x)m − (1 − x)n)/3 and Q := (2(1 − x)n − (1 + x)m)/3, whose fields are

    F(t, σ, x) := Σ_i Σ_j Σ_k C^F_ijk T_i(t) T_j(σ) T_k(x)                                             {#eq:tl5-fields}

for real numbers C^F_ijk with |C^F_ijk − C̃^F_ijk| ≤ ε₀ for all F, i, j, k, the C̃ taken from the first (second)
table. The printed approximants, C = C̃, are of these kinds. So are the two fitted approximants: the first is a
least-squares fit of the discrete solution of the characteristic problem of [[ch:ten-l5]] on one null grid, the
second a fit of the Richardson combination of the solutions on two nested grids, and each printed C̃ is the
corresponding fitted coefficient rounded to the nearest multiple of 10⁻¹⁸. Every result below holds for every
approximant of the kind named; f^(1)_ab and f^(2)_ab denote the residuals of approximants of the first and second
kind. At every point and on every box used below, R is positive (its enclosure, by [[lem:tl5-jet-enclosure]], is a
positive interval), and there [[eq:tl5-metric]] is a Lorentzian metric of the class [[eq:class-metric]].

**Definition {#def:tl5-residual}** (the residual). Let Ω² := e^(2W), b := (1 − x²) s and

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

**Lemma {#lem:tl5-connection}** (the connection of g3). The Levi-Civita connection ∇ of g3 is given by

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

**Lemma {#lem:tl5-ricci3}** (the Ricci tensor of g3). In the frame (L, Y, E),

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

**Proposition {#prop:tl5-components}** (the eight components). For ψ ∈ {A, B} put ψ_L := L(ψ), ψ_Y := Y(ψ),
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

**The derivatives.** Every quantity in [[eq:tl5-components]] is an explicit expression in x and in the values of the
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

Write ε := e^(−ζ), ϑ := e^(ζ − 2W)/4 (so τ = ϑ b_v) and Y(ζ) = ζ_u + bζ_x. Then ω = W_v, ω̲ = W_u + bW_x, k = ζ_v,
k̲ = ζ_u + bζ_x + b_x, η = εW_x, and

    L(k) = ζ_vv,   Y(k) = ζ_uv + bζ_vx,   L(k̲) = ζ_uv + b_v ζ_x + bζ_vx + b_vx,   L(ω̲) = W_uv + b_v W_x + bW_vx,
    Y(k̲) = ζ_uu + b_u ζ_x + bζ_ux + b_ux + b(ζ_ux + b_x ζ_x + bζ_xx + b_xx),
    L(η) = ε(W_vx − ζ_v W_x),   Y(η) = ε(W_ux + bW_xx − Y(ζ) W_x),   E(η) = εε(W_xx − ζ_x W_x),
    L(τ) = τ(ζ_v − 2ω) + ϑ b_vv,   Y(τ) = τ(Y(ζ) − 2ω̲) + ϑ(b_uv + b b_vx),
    E(τ) = ε(τ(ζ_x − 2W_x) + ϑ b_vx),                                                    {#eq:tl5-frame-derivatives}

and for ψ ∈ {A, B}: ψ_L = ψ_v, ψ_Y = ψ_u + bψ_x, ψ_E = εψ_x, L(ψ_L) = ψ_vv, L(ψ_Y) = ψ_uv + b_v ψ_x + bψ_vx,
Y(ψ_Y) = ψ_uu + b_u ψ_x + bψ_ux + b(ψ_ux + b_x ψ_x + bψ_xx), L(ψ_E) = ε(ψ_vx − ζ_v ψ_x),
Y(ψ_E) = ε(ψ_ux + bψ_xx − Y(ζ) ψ_x), E(ψ_E) = εε(ψ_xx − ζ_x ψ_x). The u- and v-derivatives of a field are those in
(t, σ) through [[eq:tl5-chain]]: F_u = φ₁F_t, F_uu = φ₁φ₁F_tt + φ₂F_t, F_uv = (40/21)φ₁F_tσ, F_ux = φ₁F_tx,
F_v = (40/21)F_σ, F_vv = (40/21)²F_σσ, F_vx = (40/21)F_σx. Each line follows from the definitions by the product and
chain rules; for instance ∂_x(−(1/2) log(1 − x²)) = x/w and ∂_x(x/w) = (1 + x²)/w².

[[eq:tl5-components]], [[eq:tl5-derivatives]] and [[eq:tl5-frame-derivatives]] are the formula used below. Its
operations are carried out in the order written, a product of several factors from left to right; this fixes the
enclosures of [[lem:tl5-jet-enclosure]].

#### Bounds at points and on boxes {#sec:tl5-enclosures}

For a multi-index α = (α₁, α₂, α₃), a function f on Π and p ∈ Π write ∂^α := ∂_t^α₁ ∂_σ^α₂ ∂_x^α₃,
f_α(p) := ∂^α f(p)/α! (α! := α₁!α₂!α₃!) and |α| := α₁ + α₂ + α₃. A box is b = {p : |p_d − c_d| ≤ h_d, d = 1, 2, 3}
⊂ Π with centre c and half-widths h; h^α := h₁^α₁ h₂^α₂ h₃^α₃.

**Lemma {#lem:tl5-taylor}** (one box). For f ∈ C³(b),

    sup_b |f| ≤ Σ_(|α|≤2) |f_α(c)| h^α + Σ_(|α|=3) sup_(p∈b) |f_α(p)| h^α.                               {#eq:tl5-taylor}

*Proof.* By Taylor's formula with the Lagrange remainder, for p = c + y ∈ b there is θ ∈ (0, 1) with
f(p) = Σ_(|α|≤2) f_α(c) y^α + Σ_(|α|=3) f_α(c + θy) y^α, and |y^α| ≤ h^α. ∎

**Lemma {#lem:tl5-chebyshev}** (derivatives of the fields). For F of [[eq:tl5-fields]] and every multi-index γ,
∂^γ F = Σ C^(F,γ)_ijk T_i(t) T_j(σ) T_k(x), where C^(F,γ) arises from C^F by applying γ₁ times in the first index,
γ₂ times in the second and γ₃ times in the third the map (c_i) ↦ (c′_i),

    c′_i := (2/(1 + δ_i0)) Σ_(i′ > i, i′ − i odd) i′ c_i′.                          {#eq:tl5-cheb-derivative}

Consequently |F_γ| ≤ Σ_ijk |C^(F,γ)_ijk|/γ! on [−1, 1]³.

*Proof.* The identity T′_k = 2k(T_(k−1) + T_(k−3) + …), with the last term T_0 halved when k is odd, follows from
T′_k(cos θ) = k sin kθ/sin θ and 2 sin θ (cos (k−1)θ + cos (k−3)θ + …) = sin kθ. Summing over k gives
[[eq:tl5-cheb-derivative]]; |T_k| ≤ 1 on [−1, 1] gives the bound. ∎

**Lemma {#lem:tl5-rounding}** (the rounding). For n, a ≥ 0, T_n^(a)(1) = Π_(r<a) (n² − r²)/(2r + 1) and
|T_n^(a)| ≤ T_n^(a)(1) on [−1, 1]. Hence, if two fields F and F̃ of the form [[eq:tl5-fields]] have coefficients
that differ by at most ε₀, then for every multi-index γ

    sup_([−1,1]³) |∂^γ F − ∂^γ F̃| ≤ ε₀ M_γ,      M_γ := S₂₄^(γ₁) S₃₀^(γ₂) S₁₅^(γ₃),   S_n^(a) := Σ_(i=0..n) T_i^(a)(1).
                                                                                       {#eq:tl5-rounding}

In particular S₂₄^(a) = 25, 4,900, 586,040, S₃₀^(a) = 31, 9,455, 1,754,848 and S₁₅^(a) = 16, 1,240, 59,024 for
a = 0, 1, 2, so that the values of the fields move by at most ε₀M₀ = 6.2 × 10⁻¹⁵, their first derivatives in t, σ and
x by at most 1.3 × 10⁻¹², 1.9 × 10⁻¹² and 4.9 × 10⁻¹³, and their second derivatives in tt, tσ, tx, σσ, σx and xx by
at most 1.5 × 10⁻¹⁰, 3.8 × 10⁻¹⁰, 9.5 × 10⁻¹¹, 3.6 × 10⁻¹⁰, 1.5 × 10⁻¹⁰ and 2.3 × 10⁻¹¹.

*Proof.* T_n solves (1 − x²)y″ − xy′ + n²y = 0. Differentiating a times gives (1 − x²)y^(a+2) − (2a + 1)x y^(a+1)
+ (n² − a²)y^(a) = 0, and at x = 1 this reads (2a + 1) T_n^(a+1)(1) = (n² − a²) T_n^(a)(1); with T_n(1) = 1 the
product formula follows. The map [[eq:tl5-cheb-derivative]] has nonnegative entries, so T_n^(a) = Σ_l β_l T_l with
β_l ≥ 0, and |T_n^(a)(x)| ≤ Σ_l β_l = T_n^(a)(1) because |T_l| ≤ 1 = T_l(1). Then
|∂^γ(F − F̃)| ≤ Σ_ijk |C_ijk − C̃_ijk| |T_i^(γ₁)| |T_j^(γ₂)| |T_k^(γ₃)| ≤ ε₀ M_γ. Finally S_n^(1) = Σ i² and
S_n^(2) = Σ i²(i² − 1)/3, whose values are the stated ones. ∎

**The enclosures at a point.** For an approximant of either kind, its coefficients are known only to lie within ε₀ of
the printed ones. At a point c we therefore use, for every field and multi-index γ, the interval

    J^F_γ(c) := [F̃_γ(c) − r^F_γ(c), F̃_γ(c) + r^F_γ(c)],      r^F_γ(c) := ε₀ Σ_ijk |∂^γ(T_i T_j T_k)(c)|/γ!,

with F̃ the printed field; F_γ(c) ∈ J^F_γ(c) for every approximant of the kind. Put also

    L^F_γ := Σ_ijk |C̃^(F,γ)_ijk|/γ! + ε₀ M_γ/γ!;

by [[lem:tl5-chebyshev]] and [[lem:tl5-rounding]], |F_γ| ≤ L^F_γ on [−1, 1]³ for every approximant of the kind.

**Lemma {#lem:tl5-field-box}** (Taylor coefficients of a field on a box). Let b be a box with centre c and
half-widths h, F a field of an approximant and γ a multi-index. For every p ∈ b, F_γ(p) lies in J^F_γ(c) enlarged on
each side by

    Σ_d (γ_d + 1) max|J^F_(γ+e_d)(c)| h_d + (1/2) Σ_(d,d′) (γ_d + 1)(γ_d′ + δ_dd′ + 1) L^F_(γ+e_d+e_d′) h_d h_d′,

where e_d is the d-th unit multi-index.

*Proof.* ∂_d F_γ = (γ_d + 1) F_(γ+e_d) and ∂_d′ ∂_d F_γ = (γ_d + 1)(γ_d′ + δ_dd′ + 1) F_(γ+e_d+e_d′). Taylor's formula
for F_γ at c to first order, with the Lagrange remainder bounded by |F_(γ+e_d+e_d′)| ≤ L^F_(γ+e_d+e_d′), gives the
claim. ∎

**Definition {#def:tl5-jets}** (jets and enclosures). The jet of f at p is J_p f := (f_α(p))_(|α|≤3), twenty numbers.
For jets a, a′ put (a + a′)_α := a_α + a′_α and (aa′)_α := Σ_(β+β′=α) a_β a′_β′; for a jet a write a₀ for its
coefficient at α = 0 and N := a − a₀ (the jet a with a₀ replaced by 0), and put

    1/a := Σ_(j=0..3) (−1)^j a₀^(−j−1) N^j,     √a := Σ_(j=0..3) binom(1/2, j) a₀^(1/2−j) N^j,
    e^a := e^(a₀) Σ_(j=0..3) N^j/j!.

Then J_p(fg) = (J_p f)(J_p g), J_p(1/f) = 1/J_p f, J_p √f = √(J_p f) and J_p e^f = e^(J_p f), because the Taylor
coefficients of order at most 3 of a product or of a composition depend only on those of the factors, and
N^4 = 0 in this product. An enclosure of a jet on a set is a family of closed intervals (I_α)_(|α|≤3) containing the
jet at every point of the set and for every approximant of the kind considered. Intervals are added and multiplied by
the endpoint rules [p₁, p₂] + [q₁, q₂] = [p₁ + q₁, p₂ + q₂] and [p₁, p₂][q₁, q₂] = [min, max] of the four products
p_i q_j; for a jet whose constant term lies in an interval [p₁, p₂] with p₁ > 0, the coefficients a₀^(−j−1),
a₀^(1/2−j) and e^(a₀) are monotone in a₀ and are enclosed by their values at p₁ and p₂.

**Lemma {#lem:tl5-jet-enclosure}** (the components on a box and at a point). Let b be a box in Π with centre c.
Enclose, for every field and |γ| ≤ 5, the coefficient F_γ on b by [[lem:tl5-field-box]]; enclose the jets of x and
of ξ = ξ_a + (t + 1)h_ξ on b (constant terms ranging over the box, first coefficients 1 and h_ξ); and evaluate
[[eq:tl5-chain]], [[eq:tl5-derivatives]], [[eq:tl5-frame-derivatives]] and [[eq:tl5-components]] in the order
written, with jets, by the rules of [[def:tl5-jets]], the jet of ∂_t F having coefficients (α₁ + 1)F_(α+e₁) and that
of ∂_t²F (α₁ + 1)(α₁ + 2)F_(α+2e₁) (similarly in σ and x). Wherever a reciprocal, a square root or a logarithmic
derivative is formed, suppose the enclosure of the constant term is a positive interval. Then the result encloses
J_p f_ab on b for each ab, for every approximant of the kind. The same evaluation with the intervals J^F_γ(c) at the
single point c gives enclosures J^ab_α(c) of (f_ab)_α(c); with jets of order 0, it gives an interval containing
f_ab(c) for every approximant of the kind.

*Proof.* Each step is a sum, a product, a reciprocal, a square root or an exponential of jets that, at every p ∈ b
and for every approximant, contain the jets at p of the functions the formula names; by [[def:tl5-jets]] the exact
results are the jets at p of the corresponding functions, and the endpoint rules return intervals containing every
value the operation takes on the given intervals. Induction over the steps gives the claim. ∎

**Definition {#def:tl5-certificate}** (the number of a box). For a box b with centre c and half-widths h, let

    κ_ab(b) := Σ_(|α|≤2) max|J^ab_α(c)| h^α + Σ_(|α|=3) max|I^ab_α| h^α,      κ(b) := max_ab κ_ab(b),
                                                                                       {#eq:tl5-certificate}

with J^ab_α(c) and I^ab_α the enclosures of [[lem:tl5-jet-enclosure]] at c and on b. By [[lem:tl5-taylor]],
sup_b max_ab |f_ab| ≤ κ(b) for every approximant of the kind. The tables give, for every box, a number at least κ(b),
rounded upward; since the endpoint rules are exact for each single operation, an evaluation by them never exceeds
the printed number. At a point p the tables give a number at least the largest of max|·| over the intervals of
[[lem:tl5-jet-enclosure]] containing f_ab(p), rounded upward.

#### The bounds {#sec:tl5-bounds}

Let d_k := (1 − cos(π/32))(3/2)^k for 0 ≤ k ≤ 9 and d_10 := 1/4. The grid G consists of the 24 × 24 × 28 = 16,128
points (t_p, t_q, x_r) with t_p := (2p − 23)/24 (0 ≤ p, q ≤ 23) and x_r running over the midpoints of the twenty
intervals [−1 + d_k, −1 + d_(k+1)] and [1 − d_(k+1), 1 − d_k] (0 ≤ k ≤ 9) and the eight numbers
−3/4 + (2r + 1)·3/32 (0 ≤ r ≤ 7).

**Proposition {#prop:tl5-points}** (the residuals at the points of G). At every point of G and for every ab, every
approximant of the first kind satisfies |f^(1)_ab| ≤ 2.42 × 10⁻³ and every approximant of the second kind
|f^(2)_ab| ≤ 3.73 × 10⁻⁵. Two approximants of the same kind have residuals that differ by at most 1.3 × 10⁻⁷ at
every point of G. The largest values are taken by f_ll at (−23/24, 23/24, −21/32), where |f^(1)_ll| lies in
[2.4141, 2.4143] × 10⁻³, and at (−23/24, 23/24, x₆), x₆ := −1 + (d₆ + d₇)/2, where |f^(2)_ll| lies in
[3.715, 3.728] × 10⁻⁵. In particular 2.41 × 10⁻³ is not an upper bound for |f^(1)_ll| on G; the bound to three
significant figures is 2.42 × 10⁻³.

*Proof.* [[sec:tab-d-points]] lists, for each kind and each point of G, an upper bound for max_ab |f_ab| at that
point over all approximants of the kind, obtained from the intervals of [[lem:tl5-jet-enclosure]] (jets of order 0,
coefficients in J^F_γ by [[lem:tl5-rounding]]); the largest entries are 242 × 10⁻⁵ and 373 × 10⁻⁷. The same
intervals have widths at most 1.3 × 10⁻⁷, which bounds the difference of the residuals of two approximants of one
kind, and at the two points named they are the stated ones. Every claimed bound therefore holds with this allowance
included: 2.4143 × 10⁻³ ≤ 2.42 × 10⁻³ and 3.728 × 10⁻⁵ ≤ 3.73 × 10⁻⁵. ∎

**Proposition {#prop:tl5-box-first}** (the first kind on one box). On B* := [−1/2, 0] × [−1/2, 0] × [0, 1/4], every
approximant of the first kind satisfies

    sup_(B*) max_ab |f^(1)_ab| ≤ 3.01 × 10⁻⁴.

*Proof.* Divide B* into the 32³ = 32,768 boxes of half-widths (1/128, 1/128, 1/256). [[sec:tab-d-boxes]] gives an
upper bound for κ(b) for each of them ([[def:tl5-certificate]]); the largest is 2.99 × 10⁻⁴ ≤ 3.01 × 10⁻⁴. Since
κ(b) is formed with the intervals of [[lem:tl5-rounding]], the allowance for the rounding is included. ∎

**Proposition {#prop:tl5-boxes-second}** (the second kind on four boxes). Let B1 := I × J × [−21/32, −41/64],
B2 := I × J × X₉, B3 := I × J × X₈ and B4 := [−1/2, −3/8] × [3/8, 1/2] × [5/8, 11/16], where I := [−31/32, −15/16],
J := [15/16, 31/32] and X_k is the eighth of the sixteen equal subintervals of [−1 + d_k, −1 + d_(k+1)] counted from
the left. Every approximant of the second kind satisfies

    sup_(Bi) max_ab |f^(2)_ab| ≤ 5.0 × 10⁻⁴   (i = 1, 2, 3, 4);

the bounds proved are 6.1 × 10⁻⁵, 4.92 × 10⁻⁴, 4.89 × 10⁻⁴ and 1.74 × 10⁻⁴. Each Bi contains a point of G at which every
approximant of the first kind has |f^(1)_ll| ≥ 1.09 × 10⁻³: (−23/24, 23/24, −21/32), (−23/24, 23/24,
−1 + (d₉ + d_10)/2), (−23/24, 23/24, −1 + (d₈ + d₉)/2) and (−11/24, 11/24, 21/32), where it is at least
2.414, 2.387, 2.347 and 1.095 × 10⁻³.

*Proof.* Divide B1 into 8³ equal boxes, B2 and B3 into 4³ and B4 into 16³. [[sec:tab-d-boxes]] gives an upper bound
for κ(b) for each of the 4,736 boxes, and the largest for each Bi are the four numbers stated; the allowance for the
rounding is included as in [[prop:tl5-box-first]]. The lower bounds at the points are the lower ends of the intervals
of [[prop:tl5-points]]. ∎

**Remark {#rem:tl5-how-checked}** (checking a row). Each entry of the tables is a finite calculation with the printed
coefficients, the number ε₀ and the rules of [[def:tl5-jets]]. [[sec:tab-d-worked]] carries one box of
[[prop:tl5-box-first]] through it completely: its intervals at the centre, the constants L^F_γ, the enclosures of
[[lem:tl5-field-box]], the jets of the quantities of [[eq:tl5-components]] for the component that attains κ(b), the
coefficients of all eight components and the sum [[eq:tl5-certificate]].
