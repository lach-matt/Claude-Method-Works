#### The conditions (X) and (T) at the first stage {#sec:tl5-xt}

This subsection shows that the conditions (X) and (T) of [[thm:tl5-wg-data]] hold at the first stage of the problem at
10 l5 when u* < −1, for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and that for every
other background with the seed's values and first derivatives on N₀⁺ they follow from explicit inequalities on its
departure from the data along N₁ ([[thm:tl5-xt]]). Three facts make this possible. (X) follows from (T)
([[lem:tl5-xt-implies]]). On N₀⁺ the development has the seed's partial derivatives of order at most 3
([[lem:tl5-xt-seed-jets]]), so (X) and (T) hold there for every background with the seed's values and first derivatives
on N₀⁺ ([[lem:tl5-xt-order]]). On N₁, for a background equal to the data at the points of N₁, the gauge vector of the
development is ∂_v times 3e^(−2W)/(2R) times the difference of the transverse derivatives of R ([[lem:tl5-xt-gauge]]),
and that derivative of the development is one quadrature of the data ([[lem:tl5-xt-rho]]).

Throughout, a seed is fixed, u* < u⁺ < u₀ with u₀ as in [[lem:tl5-seed]] (a), v* ∈ (1/2, 7/2], κ and κ′ are as in
[[def:tl5-wg-domains]], g_N is the data of the first stage of [[cor:tl5-wg-data-first-stage]], and δ, g′, Ψ, ξ, ξ′, Y₀,
Y₁, K₁, ξ₀ and ξ₁ are those of [[thm:tl5-wg-data]]. The partial derivatives of g′ at the points of N⁺ are those of the
development of [[lem:tl5-wg-lchart]], taken on 𝒩_δ, since g′ equals that development on 𝒩_δ ∩ 𝒰 and every point of N⁺ is
a limit of interior points of 𝒩_δ ∩ 𝒰. On N₁ the data's fields R, P, Q, W and β are functions of (v, x): r is the
parameter of [[eq:cone-v]], R that of [[prop:cone-exact]], W = (1/2) ln(f(r)/(2f(10))) depends on v alone, b = β ∂_x, and
ζ is the 1-form of [[lem:tl5-cip-frame]], with ζ_x = e^(−2W) G_x ∂_vβ/4 and ζ_(φ1) = ζ_(φ2) = 0. As r increases with v
and f with r, e^W increases along N₁, and we put

    e₋ := e^W at v = 1/2,   e₊ := e^W at v = 7/2,   so e₋² = f(r_s)/(2f(10)),   e₊² = f(r_e)/(2f(10)).  {#eq:tl5-xt-ew}

Norms are those of k̂ ([[eq:tl5-wg-khat]]). For a background ĝ we write R̂, Ŵ, b̂, γ̂ and Ω̂ = e^Ŵ for its fields, and ζ̂
for its 1-form of [[lem:tl5-cip-frame]].

**Lemma {#lem:tl5-xt-implies}** ((T) gives (X).) Let ĝ be a background with N⁺ ⊂ 𝒪̂. If (T) of [[thm:tl5-wg-data]]
holds, then (X) holds.

*Proof.* Let p ∈ N₁. By (T), |g_N⁻¹ − ĝ⁻¹| < κ_m ≤ 1/4 at p, so |g_N − ĝ| ≤ 1/3 at p by [[lem:tl5-wg-norms]] (b). By
[[eq:tl5-wg-khat]], k̂(ê₃, ê₃) = k̂(ê₄, ê₄) = 2Ω̂², and ĝ(ê₃, ê₄) = −2Ω̂²; as g_N is in double-null form at p,
g_N(ê₃, ê₄) = g_N(∂_u, ∂_v) + b̂^A g_N(∂_A, ∂_v) = −2e^(2W). Hence 2|e^(2W) − Ω̂²| = |(g_N − ĝ)(ê₃, ê₄)| ≤ (1/3) 2Ω̂²,
so e^(2W) ≤ (4/3) Ω̂². Since e₄ = ê₄ = ∂_v, |e₄| = √2 Ω̂, and (T) gives e^(−2W) √2 Ω̂ ξ₁ < 1/4, that is

    ξ₁ < e^(2W)/(4√2 Ω̂) ≤ Ω̂/(3√2) < √2 Ω̂   at p.

Taking p where Ω̂ attains its minimum on the compact set N₁ gives the second inequality of (X). On N₀⁺ the same argument
applies with e₃ = ∂_u + b^A ∂_A in place of e₄: g_N(ê₃, ê₄) = −2e^(2W) as before, and |e₃| ≥ |du(e₃)|/|du| = √2 Ω̂ by
[[eq:tl5-wg-khat]], so (T) gives ξ₀ < e^(2W)/(4√2 Ω̂) ≤ Ω̂/(3√2) at every point of N₀⁺. ∎

**Lemma {#lem:tl5-xt-seed-jets}** (The development on N₀⁺.) (a) At every point of N₀⁺ the components of g′ and of the
seed in the coordinates (u, v, y) have the same partial derivatives of order at most 3, the derivatives in v being taken
in v ≥ 1/2 for g′ and in v ≤ 1/2 for the seed.

(b) Put c₀ := cos(1/(2λ)) and s₀ := sin(1/(2λ)), λ the wavelength of the seed ([[def:tl5-seeds]]). At every point of
N₀⁺ with −1 < x < 1 and (2c₀ − s₀) + (2c₀ + s₀) x ≠ 0, the fourth derivatives in v of the leaf metrics of g′ and of
the seed differ. The excluded set is at most one of the tori {x = c}.

*Proof.* (a) The seed is a smooth vacuum metric in double-null form on [−10, u⁺] × [0, 1/2] × S³, which lies in D_seed
× S³ as u⁺ < u₀ ([[lem:tl5-seed]] (a), as in the proof of [[cor:tl5-cip-staged]] (a)), and g′ is one on D′₀ = [−10, u⁺]
× [1/2, 1/2 + δ] × S³ ([[lem:tl5-wg-lchart]]). They agree at every point of H := N₀⁺ = [−10, u⁺] × {1/2} × S³, where
g′ = g_N is the seed. On Z := S the derivatives ∂_v^k of W, b and γ of g′ are those of g_N along N₁, taken in v ≥ 1/2,
and those of the seed are those of the seed along {u = −10, v ≤ 1/2}, which are the data of [[def:tl5-problem]] there
([[lem:tl5-seed]] (d)). The field of [[sec:tl5-cip-staged]] that carries these data on all of N is C³ in v, so the two
agree on Z for k ≤ 3. [[lem:tl5-cip-jets]] (a) with u₁ = u⁺, s₀ = 1/2, I₁ = [0, 1/2], I₂ = [1/2, 1/2 + δ] and m = 3
gives ∂_v^k W, ∂_v^k b and ∂_v^k γ equal on H for k ≤ 3; so are their derivatives along H, which are all the partial
derivatives of order at most 3 of W, b and γ, and with them those of the components.

(b) On N₀⁺ the seed has b = 0, so e₃ = ∂_u there for both metrics, and the integral curves of e₃ are the curves
u ↦ (u, 1/2, y). By (a), the derivatives with at most three derivatives in v agree on N₀⁺. The proof of
[[lem:tl5-cip-jets]] (a), step (i) with k = 4, shows that δ∂_v⁴b, the difference of the fourth derivatives in v of b,
solves a linear homogeneous system of ordinary differential equations along these curves; it vanishes on S, since b is
C⁴ in v on N (the paragraph after [[lem:tl5-cip-shift]]) and vanishes for v ≤ 1/2; so δ∂_v⁴b = 0 on N₀⁺. Step (ii) with
k = 4 then shows that δ∂_v⁴γ solves a linear homogeneous system along the same curves. So δ∂_v⁴γ does not vanish at any
point of a curve if it does not vanish at the curve's point on S, which has the same y. At S, in the chart
(x, φ1, φ2), the seed has
γ_(φ1φ1) = r² (1 + x)/2 below v = 1/2 and the data have γ_(φ1φ1) = R² ((1 + x)/2) e^(2P) above, where R − r has
vanishing one-sided derivatives in v of order at most 7 at v = 1/2 and P of order at most 3 (the paragraph after
[[lem:tl5-cip-shift]]). With m and n of [[eq:cone-data]] written as functions of v, m = h (λ/2) r^(−3/2) env(v)
cos(v/λ) and n = h (λ/2) r^(−3/2) env(v) sin(v/λ), and env(v) = sin⁴(π(v − 1/2)/3) has the one-sided derivatives 0 of
order at most 3 and 4! (π/3)⁴ of order 4 at v = 1/2. The Leibniz rule gives at the point of S above (x, φ1, φ2)

    δ∂_v⁴γ_(φ1φ1) = r_s² (1 + x) ∂_v⁴P = (4λπ⁴/81) r_s^(1/2) (1 + x) h(x) (2(1 + x) c₀ − (1 − x) s₀),

which is not zero for −1 < x < 1 unless (2c₀ − s₀) + (2c₀ + s₀) x = 0. If 2c₀ + s₀ = 0, then 2c₀ − s₀ = 4c₀ ≠ 0, as c₀
and s₀ do not both vanish; so this equation has at most one root. ∎

**Lemma {#lem:tl5-xt-order}** (Agreement to order m on N₀⁺.) Let ĝ be a background with N⁺ ⊂ 𝒪̂ and m ≥ 1 an integer,
and suppose that the components of ĝ − g′ and their partial derivatives of order at most m vanish at every point of N₀⁺.
Then:

(a) the components of Υ(g′) and their partial derivatives of order at most m − 1 vanish at every point of N₀⁺; so
Y₀ = 0 and ξ₀ = 0;

(b) the components of Ψ − id and their partial derivatives of order at most m vanish at every point of N₀⁺; in
particular ξ = 0;

(c) if (X) holds, the components of G^♯ − ĝ and their partial derivatives of order at most m − 1 vanish at every point
of N₀⁺, and G^♯ = g_N there;

(d) (X) and (T) hold on N₀⁺, for every κ_m.

For m ≤ 3 the hypothesis says, by [[lem:tl5-xt-seed-jets]] (a), that the components of ĝ have at the points of N₀⁺ the
seed's partial derivatives of order at most m.

*Proof.* (a) Put h′ := g′ − ĝ. With D̂ the connection of ĝ, C = Γ(g′) − Γ̂ has the components C^μ_αβ = (1/2) g′^(μλ)
(D̂_α h′_βλ + D̂_β h′_αλ − D̂_λ h′_αβ), as D̂ĝ = 0. In the coordinates, D̂h′ is ∂h′ plus products of Γ̂ with h′, so its
components and their partial derivatives of order at most m − 1 vanish on N₀⁺; by the Leibniz rule so do those of C and
of Υ(g′) = g′^(αβ) C_αβ. Then Y₀ = 0, and ξ₀ = Y₀ (u⁺ + 10) e^(K₀(u⁺ + 10)) = 0, K₀ being that of [[thm:tl5-wg-data]].

(b) Use the transport of step (i) of the proof of [[lem:tl5-wg-wavemap]] on N₀⁺, in a chart (u, v, y) used in the domain
and in the target. For a smooth map Φ near a point of N₀⁺ with Φ = id on N₀⁺, the components of ∂_v^(k−1)τ(Φ) on N₀⁺
depend only on the ∂_v^j Φ, j ≤ k, on N₀⁺ and their derivatives along N₀⁺, since ∂_v^(k+1)Φ occurs only with the
coefficient g′^(vv) = 0; they are affine in ∂_v^k Φ, with coefficients that depend on the ∂_v^j Φ with j < k. The jets
J⁰_k := ∂_v^k Ψ on N₀⁺ are the unique solutions of the linear equations ∂_v^(k−1)τ(Ψ) = 0 along the integral curves of
e₃, with the derivatives in v of the identity along N₁ as initial values on S. For the identity map,
[[lem:tl5-wg-tension]] (a) with G = g′ gives τ(id) = −Υ(g′), so ∂_v^(k−1)τ(id) = 0 on N₀⁺ for 1 ≤ k ≤ m by (a). Suppose
that J⁰_j = ∂_v^j id for j < k ≤ m. Then the equation for J⁰_k is the equation that ∂_v^k id satisfies, both having the
same lower jets, and the initial values on S agree; so J⁰_k = ∂_v^k id. Hence ∂_v^k (Ψ − id) = 0 on N₀⁺ for k ≤ m, and so
are its derivatives along N₀⁺; these are all the partial derivatives of order at most m. For k = 1 this is ξ = 0.

(c) G^♯ = Φ*g′ with Φ := Ψ⁻¹ on 𝒰^♯, and Φ = id on N⁺. At p ∈ N₀⁺, Ψ(p) = p, and the partial derivatives of Φ of order
at most m at p are polynomials in those of Ψ of order at most m at p and in dΨ(p)⁻¹, the same polynomials as for Ψ = Φ =
id; by (b) they are those of the identity. The components (Φ*g′)_μν = (g′_αβ ∘ Φ) ∂_μΦ^α ∂_νΦ^β have at p partial
derivatives of order at most m − 1 built from those of Φ of order at most m and of g′ of order at most m − 1; so they
are those of g′. Hence G^♯ − g′, and with the hypothesis G^♯ − ĝ, vanishes with its partial derivatives of order at most
m − 1 on N₀⁺. At order zero, G^♯ = g′ = g_N at the points of N₀⁺.

(d) By (a), ξ₀ = 0 < √2 min_(N₀⁺) Ω̂. By the hypothesis at order zero, ĝ = g′ = g_N at the points of N₀⁺, so the
norm |g_N⁻¹ − ĝ⁻¹| vanishes there, and the left side of (T) on N₀⁺ is 0 < κ_m. ∎

**Lemma {#lem:tl5-xt-gauge}** (The gauge vector and the constant K₁ on N₁.) Let ĝ be a background with N⁺ ⊂ 𝒪̂.

(a) At every point of 𝒪̂, with â := dŴ + ζ̂,

    |∇̂_(∂_v) k̂| = 2√2 ((∂_vŴ)² + Ω̂² |â|²_γ̂)^(1/2),
    K₁ = max_(N₁) (√2 ((∂_vŴ)² + Ω̂² |â|²_γ̂)^(1/2) + (3/2) ∂_vR/R),

R the data's R.

(b) If ĝ = g_N at every point of N₁, let R′ be the R of g′; then R′ = R̂ = R on N₁, and on N₁

    Υ(g′) = (3e^(−2W)/(2R)) ∂_u(R′ − R̂) ∂_v,      e^(2W) |Υ(g′)| = (3e^W/(√2 R)) |∂_u(R′ − R̂)|.  {#eq:tl5-xt-upsilon}

Moreover Ŵ = W, â = ζ and Ω̂ = e^W on N₁, so K₁ = max_(N₁) (√2 ((∂_vW)² + e^(2W) |ζ|²_γ)^(1/2) + (3/2) ∂_vR/R).

(c) In general let ε₀ := max_(N₁) |g_N − ĝ| and ε₁ := max_(N₁) |D̂(g′ − ĝ)|, and suppose ε₀ ≤ 1/4. Then on N₁

    |g_N⁻¹ − ĝ⁻¹| ≤ 2ε₀,   (1 − ε₀) Ω̂² ≤ e^(2W) ≤ (1 + ε₀) Ω̂²,   Y₁ ≤ (3/2) (1 + 2ε₀) (√5 + 2ε₀) e₊² ε₁.

*Proof.* (a) Put e₁ := (ê₄ − ê₃)/(2Ω̂). By [[eq:tl5-cip-connection]] for ĝ, ∇̂_(ê₄) ê₄ = 2∂_vŴ ê₄ and
∇̂_(ê₄) ê₃ = 2Ω̂² â^A ∂_A, so, with ê₄ = ∂_v and e₀ = (ê₃ + ê₄)/(2Ω̂),

    w := ∇̂_(∂_v) e₀ = −(∂_vŴ/(2Ω̂)) (ê₃ + ê₄) + (1/(2Ω̂)) (2Ω̂² â^A ∂_A + 2∂_vŴ ê₄) = ∂_vŴ e₁ + Ω̂ â^A ∂_A.

As ∇̂ĝ = 0, ∇̂_(∂_v) k̂ = 2 (w♭ ⊗ e₀♭ + e₀♭ ⊗ w♭) with w♭ := ĝ(w, ·) and e₀♭ := ĝ(e₀, ·). In the frame
(e₀, e₁, f₁, f₂, f₃) of [[sec:tl5-wg-equations]], e₀♭ has the components (−1, 0, 0, 0, 0), and w♭ has e₀-component 0, as
ĝ(w, e₀) = (1/2) ∂_v ĝ(e₀, e₀) = 0; so |∇̂_(∂_v) k̂|² = 8 |w|², and |w|² = (∂_vŴ)² + Ω̂² |â|²_γ̂. In K₁, e₄ = ∂_v and
trχ = 3∂_vR/R, χ being that of g′, whose leaf metric on N₁ is the data's ([[lem:tl5-leaf-expansion]]); and ∂_vR =
(f/2) ∂_rR > 0 on N₁ by [[prop:cone-exact]] (a), so (1/2) |trχ| = (3/2) ∂_vR/R.

(b) For a metric g in double-null form, by [[lem:tl5-cip-form]] (a) g^(uu) = g^(uA) = 0 and g^(uv) = −e^(−2W)/2, and in
the coordinates (u, v, y) the determinant is −4e^(4W) det γ, as in the proof of [[lem:cone-raychaudhuri]]; so the
functions |det g|^(1/2) g^(uμ) are −(det γ)^(1/2) δ^μ_v. By the identity g^(αβ) Γ(g)^μ_αβ = −|det g|^(−1/2) ∂_α(|det
g|^(1/2) g^(αμ)),

    Υ(g)^μ = −|det g|^(−1/2) ∂_α(|det g|^(1/2) g^(αμ)) − g^(αβ) Γ̂^μ_αβ.

At p ∈ N₁ the components of g′ and ĝ agree, so the last terms agree, the terms with α ≠ u are derivatives along N₁ of
functions that agree on N₁, and Υ(ĝ) = 0. The term with α = u gives Υ(g′)^μ = |det g′|^(−1/2) ∂_u((det γ′)^(1/2) − (det
γ̂)^(1/2)) δ^μ_v. In the chart (x, φ1, φ2), (det γ)^(1/2) = R³/4 and |det g|^(1/2) = e^(2W) R³/2, which gives the first
formula of [[eq:tl5-xt-upsilon]] for |x| < 1, and at the axes by continuity. By [[eq:tl5-wg-khat]], the norm of ∂_v is √2
Ω̂ = √2 e^W, which gives the second. The fields of ĝ restricted to N₁ are those of g_N, so their derivatives along N₁ are
the data's; W depends on v alone, so dŴ = 0 there, and (a) gives K₁.

(c) In a k̂-orthonormal frame in which ĝ has the matrix η = diag(−1, 1, 1, 1, 1), let G be the matrix of g′⁻¹. At points
of N₁, g′ = g_N, so by [[lem:tl5-wg-norms]] (a) the Frobenius norm of G − η is at most 2ε₀; so |G| ≤ √5 + 2ε₀ and the
operator norm of G is at most 1 + 2ε₀. With h′ := g′ − ĝ, the formula for C in the proof of [[lem:tl5-xt-order]] gives
Υ(g′)^μ = G^(μλ) ν_λ, ν_λ := G^(αβ) D̂_α h′_βλ − (1/2) G^(αβ) D̂_λ h′_αβ, and by the Cauchy–Schwarz inequality in (α, β)
for each λ, |ν| ≤ (3/2) |G| |D̂h′|. So |Υ(g′)| ≤ (3/2)(1 + 2ε₀)(√5 + 2ε₀) ε₁ on N₁, and e^(2W) ≤ e₊² there. For the
second inequality, (g_N − ĝ)(ê₃, ê₄) = −2e^(2W) + 2Ω̂², as in the proof of [[lem:tl5-xt-implies]], and its absolute value
is at most ε₀ |ê₃| |ê₄| = 2ε₀ Ω̂². ∎

**Lemma {#lem:tl5-xt-rho}** (The transverse derivative of R.) (a) Let g be a vacuum metric in double-null form, and R
the positive function with R⁶ det γ₀ = det γ in every chart of S³, γ₀ the round metric. Then at every point

    ∂_v(R² ∂_uR) = (R³/3) e^(2W) (2Δ̸W + 2|dW|² + 2|ζ|²_γ − R̸)
                   − (R³/6) (∂_v div_γ b + 3 b(∂_vR/R) + 6 (∂_vR/R) div_γ b),

where R̸ is the scalar curvature of the leaf metric γ and div_γ b := (det γ)^(−1/2) ∂_A((det γ)^(1/2) b^A).

(b) On N₁, the R′ of g′ satisfies ∂_v(R² ∂_uR′) = 𝒢, where, with the data's fields,

    𝒢 := (R³/3) e^(2W) (2|ζ|²_γ − R̸) − (R³/6) (∂_v div_γ b + 3β ∂_x(∂_vR/R) + 6 (∂_vR/R) div_γ b),
    div_γ b = ∂_xβ + 3β ∂_xR/R,
    R̸ = −2e^(−2ϰ₁) (∂_x²ϰ₂ + ∂_x²ϰ₃ + (∂_xϰ₂)² + (∂_xϰ₃)² + ∂_xϰ₂ ∂_xϰ₃ − ∂_xϰ₁ (∂_xϰ₂ + ∂_xϰ₃)),

with ϰ₁ := (ln G_x)/2, ϰ₂ := ln R + P + (1/2) ln((1 + x)/2) and ϰ₃ := ln R + Q + (1/2) ln((1 − x)/2) for |x| < 1, and
∂_uR′ = −f(r_s)/f(10) on S. So ∂_uR′ = ρ on N₁, where

    ρ(v, x) := R(v, x)⁻² (−r_s² f(r_s)/f(10) + ∫_(1/2)^v 𝒢(v′, x) dv′).  {#eq:tl5-xt-rho}

*Proof.* (a) Contract the fifth line of [[eq:tl5-cip-ricci]] with γ^(AB). Since ∂_vγ^(AB) = −2χ^(AB),
γ^(AB) ∂_vχ̲_AB = ∂_v trχ̲ + 2⟨χ, χ̲⟩. Since e₃γ_CD = 2χ̲_CD − γ_ED ∂_Cb^E − γ_CE ∂_Db^E, γ^(AB) e₃(χ_AB) = e₃(trχ) +
2⟨χ, χ̲⟩ − 2χ^C_E ∂_Cb^E, and the two terms of ℒ₃χ with ∂b add 2χ^C_E ∂_Cb^E; so γ^(AB) (ℒ₃χ)_AB = e₃(trχ) + 2⟨χ, χ̲⟩.
The products contribute 2 trχ trχ̲ − 4⟨χ, χ̲⟩. Hence

    0 = γ^(AB) Ric(∂_A, ∂_B) = (e^(−2W)/2) (∂_v trχ̲ + e₃(trχ) + 2 trχ trχ̲) − 2Δ̸W − 2|dW|² − 2|ζ|²_γ + R̸.

As ln det γ = 6 ln R + ln det γ₀ with det γ₀ independent of u and v, trχ = (1/2) γ^(AB) ∂_vγ_AB = 3∂_vR/R, and trχ̲ =
(1/2) e₃(ln det γ) + ∂_Ab^A = 3∂_uR/R + div_γ b. Then e₃(trχ) = 3∂_u(∂_vR/R) + 3b(∂_vR/R), and

    ∂_v trχ̲ + e₃(trχ) + 2 trχ trχ̲ = (6/R³) ∂_v(R² ∂_uR) + ∂_v div_γ b + 3b(∂_vR/R) + 6 (∂_vR/R) div_γ b,

since 3∂_v(∂_uR/R) + 3∂_u(∂_vR/R) + 18 ∂_vR ∂_uR/R² = 6 ∂_u∂_vR/R + 12 ∂_uR ∂_vR/R². Solving for ∂_v(R² ∂_uR) gives (a).

(b) g′ is a vacuum metric in double-null form on D′₁ ∋ N₁ ([[lem:tl5-wg-lchart]]), so (a) holds at the points of N₁, with
the derivative in u taken in u ≥ −10. All other terms are derivatives along N₁ of the fields of g′ on N₁, which are the
data's. On N₁, W depends on v alone, so Δ̸W = |dW|² = 0. In the chart (x, φ1, φ2), (det γ)^(1/2) = R³/4 and b = β ∂_x,
which gives div_γ b. The leaf metric is e^(2ϰ₁) dx² + e^(2ϰ₂) dφ1² + e^(2ϰ₃) dφ2²; with the arc length t, dt = e^(ϰ₁) dx,
the scalar curvature of dt² + a² dφ1² + c² dφ2² is −2(a_tt/a + c_tt/c + a_t c_t/(a c)), and a = e^(ϰ₂), c = e^(ϰ₃) give
the formula for R̸. On N₀⁺, g′ = g_N is the seed, so at S, ∂_uR′ is the seed's ∂_uR, which is −2e^(2W) by the proof of
[[lem:tl5-seed]] (c), and e^(2W) = f(r_s)/(2f(10)) at S by [[lem:tl5-seed]] (b). Integrating ∂_v(R² ∂_uR′) = 𝒢 from v =
1/2, where R = r_s, gives [[eq:tl5-xt-rho]]; it holds at x = ±1 by continuity. ∎

For the seed itself (a) gives ∂_v(R² ∂_uR) = −2e^(2W) R, as there b = 0, ζ = 0, W does not depend on the angles and
R̸ = 6/R²; along u = −10 this is ∂_v(−r² f(r)/f(10)) with ∂_vr = f(r)/2.

**Lemma {#lem:tl5-xt-rx}** (Derivatives in x of the exact radius.) Let W̄ be as in [[lem:cone-w]] and ℓ = (r_e − r_s)/2.
On [r_s, r_e] × [−1, 1] the function R of [[prop:cone-exact]] satisfies

    |∂_xR| ≤ X̄ := 2ℓ² W̄ r_e/(1 − 2ℓ² W̄),      |∂_x∂_rR| ≤ X̄′ := 2ℓ W̄ (r_e + X̄),

with X̄ ≤ 0.025895 and X̄′ ≤ 0.034817 at the first seed, and X̄ ≤ 0.011112 and X̄′ ≤ 0.014940 at the second.

*Proof.* With p(x) := (x² − 1)/(1 + x²) and q(x) := 2x/(1 + x²), [[eq:cone-w]] reads w = (4/9)(A² + B² + AB p +
(A² − B²) q), A and B not depending on x. Since p′ = 4x/(1 + x²)² and q′ = 2(1 − x²)/(1 + x²)², p′² + q′² = 4/(1 + x²)²,
and by the Cauchy–Schwarz inequality and A²B² + (A² − B²)² ≤ (A² + B²)²,

    |∂_xw| = (4/9) |AB p′ + (A² − B²) q′| ≤ (8/9)(A² + B²)/(1 + x²) ≤ W̄.

By the proof of [[prop:cone-exact]], R(r, x) = r − ∫_(r_s)^r (r − q) w(q, x) R(q, x) dq on [r_s, r_e], with 0 < R ≤ q
in the integrand, and R has continuous derivatives in x. So ∂_xR(r, x) = −∫_(r_s)^r (r − q)(∂_xw R + w ∂_xR) dq. Let X be
the maximum of |∂_xR| on [r_s, r_e] × [−1, 1]. Then |∂_xR| ≤ W̄ (r_e + X)(r − r_s)²/2 ≤ 2ℓ² W̄ (r_e + X), so
X (1 − 2ℓ² W̄) ≤ 2ℓ² W̄ r_e, which is X ≤ X̄. Likewise ∂_x∂_rR = −∫_(r_s)^r (∂_xw R + w ∂_xR) dq, with absolute value at
most 2ℓ W̄ (r_e + X̄). With 2ℓ² ≤ 1.1064, 2ℓ ≤ 1.4876 (the proof of [[cor:cone-compare]]) and r_e ≤ 11.7351
([[eq:cone-v]]), at the first seed 2ℓ² W̄ ≤ 2.20174 × 10⁻³, X̄ ≤ 0.0258377/0.997798 ≤ 0.025895 and X̄′ ≤ 2.96033 ×
10⁻³ × 11.76100 ≤ 0.034817; at the second 2ℓ² W̄ ≤ 9.4598 × 10⁻⁴, X̄ ≤ 0.0111012/0.999054 ≤ 0.011112 and
X̄′ ≤ 1.271898 × 10⁻³ × 11.746212 ≤ 0.014940. ∎

**Lemma {#lem:tl5-xt-k1}** (The constant K₁.) Let ĝ be a background with N⁺ ⊂ 𝒪̂ and ĝ = g_N at every point of N₁.
Then for every v* ∈ (1/2, 7/2]

    K₁ ≤ 𝔎,   𝔎 := 0.1038 at the first seed,   𝔎 := 0.09194 at the second.  {#eq:tl5-xt-k1}

*Proof.* We bound the three quantities of the formula for K₁ in [[lem:tl5-xt-gauge]] (b) on N₁, where r ∈ [r_s, r_e]
as v* ≤ 7/2. The constants used are r_s ∈ (10.24756039, 10.24756040) and r_e ∈ (11.73508635, 11.73508636), from
v(10.24756039) < 1/2 < v(10.24756040) and v(11.73508635) < 7/2 < v(11.73508636) in [[eq:cone-v]]; then f(r_s) ≥
0.9904773 and f(r_e) ≤ 0.992739, so by [[eq:tl5-xt-ew]] e₋² ≥ 0.500241, e₊² ≤ 0.501384, e₋ ≥ 0.707277 and
e₊/e₋ ≤ 1.001142.

*The first two.* By the proof of [[lem:cone-generator]], ∂_vW = 1/(2r³) ≤ 1/(2r_s³) ≤ 4.6464 × 10⁻⁴. By
[[prop:cone-exact]] (a), 0 < ∂_rR ≤ 1 and R ≥ r_s on [r_s, r_e], so (3/2) ∂_vR/R = (3f/4) ∂_rR/R ≤ 3f(r_e)/(4r_s) ≤
0.072657.

*The 1-form.* By the proof of [[lem:tl5-cip-shift]], ∂_v(R³ ζ_x) = R³ 𝔣 with ζ_x = 0 at v = 1/2, and on N₁, where
∂_xW = 0, [[eq:tl5-cip-shift]] with 2P + Q = (1 + x) m and P + 2Q = (1 − x) n reads

    𝔣 = 2∂_x(∂_vR/R) + ∂_x(∂_vP + ∂_vQ) + (∂_vm − ∂_vn)/2 + (∂_xR/R + ∂_xP)(1 + x) ∂_vm + (∂_xR/R + ∂_xQ)(1 − x) ∂_vn.

With Θ := (A² + B²)^(1/2), A and B as in [[lem:cone-generator]], ∂_vm = (f/2) h A and ∂_vn = (f/2) h B. We use h ≤ √2,
the bound |h′| = √2 |x| (1 + x²)^(−3/2) ≤ (2/3)^(3/2), Θ² ≤ (9/8) W̄ ([[lem:cone-w]]), and φ ≤ φ̄ := (λ/2) r_s^(−3/2) on
[r_s, r_e]. Then: 2∂_x(∂_vR/R) = f (∂_x∂_rR/R − ∂_rR ∂_xR/R²), at most f (X̄′/r_s + X̄/r_s²) by [[lem:tl5-xt-rx]]; the
bound |∂_vm − ∂_vn| ≤ (f/2) h √2 Θ ≤ fΘ holds; ∂_x(∂_vP + ∂_vQ) = (1/3)(∂_vm − ∂_vn + (f/2) h′ ((1 + x) A + (1 − x) B)),
and the factor |h′| ((1 + x)² + (1 − x)²)^(1/2) = 2|x|/(1 + x²) is at most 1, so it is at most fΘ/2; (1 + x)|∂_vm| + (1 −
x)|∂_vn| ≤ (f/2) h ((1 + x)² + (1 − x)²)^(1/2) Θ = fΘ; and from P_x = (2m + n + 2(1 + x) m_x − (1 − x) n_x)/3
with |m|, |n| ≤ hφ and |m_x|, |n_x| ≤ |h′| φ, |∂_xP| ≤ (h + 2|h′|) φ ≤ 𝔭̄ := (√2 + 2(2/3)^(3/2)) φ̄, and |∂_xQ| ≤ 𝔭̄
likewise. Hence

    |𝔣| ≤ 𝔣̄ := f(r_e) (X̄′/r_s + X̄/r_s² + Θ̄ (1 + X̄/r_s + 𝔭̄)),   Θ̄ := ((9/8) W̄)^(1/2).

As R increases along each generator, |ζ_x(v)| ≤ R(v)⁻³ ∫_(1/2)^v R³ |𝔣| dv′ ≤ (v − 1/2) 𝔣̄. With
G_x = R² e^(−2(P+Q))/(4(1 − x²)) and |P + Q| = |(1 + x) m + (1 − x) n|/3 ≤ 2φ/3, by the Cauchy–Schwarz inequality
and h ((1 + x)² + (1 − x)²)^(1/2) = 2,

    |ζ|_γ = |ζ_x|/G_x^(1/2) = 2 (1 − x²)^(1/2) e^(P+Q) |ζ_x|/R ≤ ζ̄ := 2 e^(2φ̄/3) · 3 𝔣̄/r_s   on N₁,

for |x| < 1 and at the axes by continuity.

*The numbers.* r_s^(−3/2) ≤ 0.0304839, √2 + 2(2/3)^(3/2) ≤ 2.502876, and 1/(2√10) ≤ 0.1581139. At the first seed
(λ = 1, W̄ = 1.99 × 10⁻³): φ̄ ≤ 0.0152420, 𝔭̄ ≤ 0.0381489, Θ̄ ≤ 0.0473155, X̄′/r_s ≤ 0.0033976, X̄/r_s² ≤ 0.00024659,
X̄/r_s ≤ 0.0025270, Θ̄ (1 + X̄/r_s + 𝔭̄) ≤ 0.0492402, 𝔣̄ ≤ 0.992739 × 0.0528844 ≤ 0.05251, e^(2φ̄/3) ≤ 1.010214 and ζ̄ ≤
0.03106. At the second seed (λ = 10^(−1/2), W̄ = 8.55 × 10⁻⁴): φ̄ ≤ 0.00481993, 𝔭̄ ≤ 0.0120637, Θ̄ ≤ 0.0310142,
X̄′/r_s ≤ 0.0014580, X̄/r_s² ≤ 0.00010582, X̄/r_s ≤ 0.0010844, Θ̄ (1 + X̄/r_s + 𝔭̄) ≤ 0.0314220,
𝔣̄ ≤ 0.992739 × 0.0329859 ≤ 0.03275, e^(2φ̄/3) ≤ 1.003219 and ζ̄ ≤ 0.01924. So √2 ((∂_vW)² + e^(2W) |ζ|²_γ)^(1/2) ≤ √2
((4.6464 × 10⁻⁴)² + 0.501384 ζ̄²)^(1/2), which is at most 0.03111 at the first seed and 0.01928 at the second, and K₁ ≤
0.072657 + 0.03111 ≤ 0.1038, respectively K₁ ≤ 0.072657 + 0.01928 ≤ 0.09194. ∎

**Theorem {#thm:tl5-xt}** (The conditions (X) and (T) at the first stage.) Let ĝ be a background with N⁺ ⊂ 𝒪̂ whose
components have at every point of N₀⁺ the seed's values and first partial derivatives.

(a) Y₀ = 0, ξ₀ = 0 and ξ = 0, and (X) and (T) hold on N₀⁺ for every κ_m; when (X) holds on N₁ as well, G^♯ = g_N at the
points of N₀⁺.

(b) Suppose ĝ = g_N at every point of N₁, and put ε_R := max_(N₁) |∂_uR̂ − ρ|, ρ as in [[eq:tl5-xt-rho]]. Then
Y₁ ≤ 3e₊ ε_R/(√2 r_s) and K₁ ≤ 𝔎, and (X) and (T) hold, so that G^♯ is data in the wave gauge for g_N, if

    3 (e₊/e₋) (v* − 1/2) e^(𝔎(v* − 1/2)) ε_R < r_s κ_m.  {#eq:tl5-xt-condition}

For v* = 7/2 this holds if ε_R ≤ 0.8329 κ_m at the first seed and if ε_R ≤ 0.8630 κ_m at the second, and for smaller v*
under the same bounds. If ε_R = 0, it holds for every κ_m, Y₁ = ξ₁ = 0, ξ′ = 0 and G^♯ = g_N at every point of N⁺.

(c) In general, let ε₀ and ε₁ be as in [[lem:tl5-xt-gauge]] (c) and K̄₁ ≥ K₁, for instance K₁ itself, given by the
formula of [[lem:tl5-xt-gauge]] (a). Then (X) and (T) hold, and G^♯ is data in the wave gauge for g_N, if

    2ε₀ + 4.996 (v* − 1/2) e^(K̄₁(v* − 1/2)) ε₁ < κ_m.  {#eq:tl5-xt-condition-general}

For v* = 7/2 and K̄₁ ≤ 0.11 this holds if 2ε₀ + 20.9 ε₁ < κ_m.

*Proof.* (a) By [[lem:tl5-xt-seed-jets]] (a), ĝ − g′ vanishes with its first partial derivatives at the points of N₀⁺;
[[lem:tl5-xt-order]] with m = 1 gives the claims.

(b) By [[lem:tl5-xt-rho]] (b), ∂_uR′ = ρ on N₁, so by [[eq:tl5-xt-upsilon]] and R ≥ r_s, e^(2W) |Υ(g′)| ≤ 3e₊ ε_R/(√2
r_s) on N₁, which bounds Y₁; [[lem:tl5-xt-k1]] bounds K₁, so ξ₁ ≤ (3e₊ ε_R/(√2 r_s)) (v* − 1/2) e^(𝔎(v* − 1/2)). On
N₁, |g_N⁻¹ − ĝ⁻¹| = 0 and |e₄| = |∂_v| = √2 Ω̂ = √2 e^W, so the left side of (T) on N₁ is √2 e^(−W) ξ₁ ≤ √2 ξ₁/e₋, which
is less than κ_m under [[eq:tl5-xt-condition]]. (T) on N₀⁺ is (a), and (X) follows by [[lem:tl5-xt-implies]];
[[thm:tl5-wg-data]] gives the data in the wave gauge. For v* = 7/2 the left side of [[eq:tl5-xt-condition]] divided by
r_s is c_R ε_R with c_R := 9 (e₊/e₋) e^(3𝔎)/r_s; with e^(0.3114) ≤ 1.3654 and e^(0.27582) ≤ 1.3177, c_R ≤ 9 × 1.001142 ×
1.3654/10.24756039 ≤ 1.2006 at the first seed and c_R ≤ 9 × 1.001142 × 1.3177/10.24756039 ≤ 1.1587 at the second, and
0.8329 × 1.2006 < 1 and 0.8630 × 1.1587 < 1. The left side increases with v*. If ε_R = 0, then Y₁ = 0, ξ₁ = 0, |ξ′| ≤
ξ₁ = 0, and the formula of [[thm:tl5-wg-data]] gives G^♯⁻¹ = g_N⁻¹ on N₁; on N₀⁺, G^♯ = g_N by (a).

(c) Under [[eq:tl5-xt-condition-general]], 2ε₀ < κ_m ≤ 1/4, so ε₀ ≤ 1/8 and [[lem:tl5-xt-gauge]] (c) applies. On N₁ the
norm of e₄ is √2 Ω̂ ≤ √2 e^W (1 − ε₀)^(−1/2), so the left side of (T) on N₁ is at most 2ε₀ + √2 (1 − ε₀)^(−1/2) ξ₁/e₋,
with ξ₁ ≤ (3/2)(1 + 2ε₀)(√5 + 2ε₀) e₊² ε₁ (v* − 1/2) e^(K̄₁(v* − 1/2)). With ε₀ ≤ 1/8, √2 (8/7)^(1/2)
(3/2)(5/4)(√5 + 1/4) e₊²/e₋ ≤ 1.511858 × 1.875 × 2.486068 × 0.501384/0.707277 ≤ 4.996. (T) on N₀⁺ and the rest follow as
in (b). For v* = 7/2 and K̄₁ ≤ 0.11, 3 × 4.996 × e^(0.33) ≤ 14.988 × 1.39097 ≤ 20.9. ∎

The constant κ_m enters [[eq:tl5-xt-condition]] and [[eq:tl5-xt-condition-general]] linearly: halving it halves the
departure of ĝ from the data along N₁ that they admit, and nothing else. Neither condition involves N₀⁺, beyond the
agreement of ĝ with the seed to first order there.

**Definition {#def:tl5-xt-natural}** (A background from the seed and the data.) Suppose u* < −1. The proof of
[[lem:tl5-seed]] uses −10 ≤ u only through u < 0, so the seed's R_s and W_s are defined, real-analytic, and give a
vacuum metric of the class in the gauge, also for −11 < u < −10 and v ≥ 0; its leaf metric is γ_s = R_s² γ₀. Let E be
the extension in v of smooth tensor fields on [1/2, v*] × S³ to (−1/2, v* + 1) × S³ by Seeley's operator, acting
component by component, as in the proof of [[lem:tl5-cip-extend]] (a); it is linear, acts on v alone and commutes with G
and with changes of chart. Let χ₀ ∈ C^∞(ℝ) with 0 ≤ χ₀ ≤ 1, χ₀ = 1 on [−1/2, 1/2] and support in (−1, 1), and for
η₁ ∈ (0, 1) put χ(u) := χ₀((u + 10)/η₁). On N₁ put γ_s¹(v) := γ_s(−10, v), ρ_s(v) := ∂_uR_s(−10, v),

    D := γ_N − γ_s¹,      λ := 2ρ/R − (2ρ_s/(3r)) tr_(γ_N) γ_s¹,

with γ_N, b_N the leaf metric and the shift of the data and ρ of [[eq:tl5-xt-rho]]. The background ĝ_♮ is the metric
[[eq:tl5-cip-form]] with

    Ŵ := W_s,      b̂ := χ(u) E b_N,      γ̂ := γ_s + χ(u) (E D + (u + 10) E(λ γ_N)).  {#eq:tl5-xt-natural}

**Lemma {#lem:tl5-xt-natural}** (The background ĝ_♮.) Fix u′ ∈ (u*, −1). For η₁ and η ∈ (0, 1/4] small enough, ĝ_♮ is a
background ([[def:tl5-wg-background]]) on

    𝒪̂ := ((−10 − η, u′) × (1/2 − η, v* + η) ∪ (−10 − η, u⁺ + η) × (1/2 − η, 1/2 + η)) × S³,

which contains D̄ and N⁺, and:

(a) ĝ_♮ is the seed where |u + 10| ≥ η₁;

(b) at every point of N₀⁺ the components of ĝ_♮ have the seed's partial derivatives of order at most 3;

(c) ĝ_♮ = g_N at every point of N₁, and ∂_uR̂ = ρ on N₁.

*Proof.* The seed is defined on 𝒪̂ for η small: for u < −1 for every v ≥ 0, and for −1 ≤ u < u⁺ + η where
v < 1/2 + η < 2u + ln((1 − u)/(1 + u)), as this bound exceeds 1/2 for u < u₀ ([[lem:tl5-seed]] (a)). The data on N₁ are
smooth ([[cor:tl5-cip-staged]] (a)), and so are ρ, by [[lem:tl5-xt-rho]] (b), and λ; E gives smooth G-invariant
extensions, and χ is smooth; so Ŵ, b̂ and γ̂ are smooth and G-invariant. At u = −10 and v ∈ [1/2, v*], γ_s + E D = γ_N is
positive definite; by compactness and continuity, γ_s(u, v) + E D(v) is positive definite for v ∈ [1/2 − η, v* + η]
and −η₁ ≤ u + 10 ≤ η₁, for η and then η₁ small; there γ̂ = (1 − χ) γ_s + χ (γ_s + E D) + χ (u + 10) E(λγ_N) is a convex
combination of two positive definite fields, with a uniform lower bound, plus a field of size at most η₁ times a
constant, so it is positive definite for η₁ small; where |u + 10| ≥ η₁ it is γ_s. By [[lem:tl5-cip-form]] (a), ĝ_♮ is a
smooth G-invariant metric in double-null form on 𝒪̂, that is, a background.

(a) χ = 0 there. (b) The corrections in [[eq:tl5-xt-natural]] are sums of products of functions of u with E D, E(λγ_N)
and E b_N, whose one-sided derivatives in v at v = 1/2 are those of D, λγ_N and b_N. These vanish up to order 3 at
v = 1/2: the field of [[sec:tl5-cip-staged]] on N is C³ in v and equals the seed's for v ≤ 1/2, so D and b_N vanish to
order 3 (b_N even to order 4). For λ, the seed along u = −10 satisfies ∂_v(r² ρ_s) = 𝒢_s by [[lem:tl5-xt-rho]] (a), 𝒢_s
being 𝒢 computed from the seed's fields, since R_s(−10, v) = r (the proof of [[lem:tl5-seed]] (d)); and 𝒢 contains
derivatives of W, b and γ with at most one derivative in v, so 𝒢 − 𝒢_s vanishes to order 2 at v = 1/2. As
r_s² ρ_s(1/2) = −r_s² f(r_s)/f(10),
R²ρ − r²ρ_s = ∫_(1/2)^v (𝒢 − 𝒢_s) vanishes to order 3, and so does R − r, hence ρ − ρ_s. Since

    λ = 2(ρ − ρ_s)/R + 2ρ_s (1/R − 1/r) + (2ρ_s/(3r)) (3 − tr_(γ_N) γ_s¹)

and tr_(γ_N) γ_s¹ − 3 vanishes to order 3, λ vanishes to order 3. So every partial derivative of order at most 3 of the
corrections vanishes at the points of N₀⁺, and (b) follows.

(c) At u = −10, χ = 1 and ∂_uχ = 0, so γ̂ = γ_s¹ + D = γ_N, b̂ = b_N and Ŵ = W_s = W, since W_s(−10, v) is the data's W
(the proof of [[lem:tl5-seed]] (d)); and ∂_uγ̂ = ∂_uγ_s + λγ_N. As γ_s = R_s² γ₀, ∂_uγ_s = (2ρ_s/r) γ_s¹ on N₁, so
tr_(γ_N) ∂_uγ̂ = (2ρ_s/r) tr_(γ_N) γ_s¹ + 3λ = 6ρ/R. Since R̂⁶ det γ₀ = det γ̂, 6∂_uR̂/R̂ = tr_(γ̂) ∂_uγ̂, and on N₁
this is 6ρ/R with R̂ = R. ∎

**Corollary {#cor:tl5-xt-data}** (Data in the wave gauge for the first stage.) At both seeds, for every u* ∈ (−10, −1),
u⁺ ∈ (u*, u₀), v* ∈ (1/2, 7/2] and κ, κ′ as in [[def:tl5-wg-domains]], the background ĝ_♮ of
[[lem:tl5-xt-natural]] satisfies (X) and (T) of [[thm:tl5-wg-data]], with Y₀ = Y₁ = ξ₀ = ξ₁ = 0. So G^♯ is data in the
wave gauge for g_N, G^♯ = g_N at every point of N⁺, G^♯ − ĝ_♮ vanishes with its partial derivatives of order at most 2
at the points of N₀⁺, and [[thm:tl5-wg]] applies.

*Proof.* By [[lem:tl5-xt-natural]] (b) and (c), [[thm:tl5-xt]] (a) and (b) apply with ε_R = 0. By
[[lem:tl5-xt-natural]] (b) and [[lem:tl5-xt-seed-jets]] (a), ĝ_♮ − g′ vanishes to order 3 on N₀⁺, and
[[lem:tl5-xt-order]] (c) with m = 3 gives the order 2. As g_N is smooth data in the gauge on N⁺ satisfying the
constraints ([[cor:tl5-wg-data-first-stage]]) and ĝ_♮ is a background, [[thm:tl5-wg]] applies. ∎

**Proposition {#prop:tl5-xt-seed}** (The seed as background.) Suppose u* < −1, and let ĝ be the seed, a background on
the set 𝒪̂ of [[lem:tl5-xt-natural]]. Its values and first derivatives on N₀⁺ are the seed's, so [[thm:tl5-xt]] (a)
applies. But on N₁, at the point with v = 9/4 and x = 1 at the first seed (if v* ≥ 9/4), and with v = 2 and x = 1 at the
second (if v* ≥ 2),

    |g_N⁻¹ − ĝ⁻¹| ≥ 0.01967   (first seed),      |g_N⁻¹ − ĝ⁻¹| ≥ 0.01100   (second seed);

so (T) fails on N₁ whenever κ_m ≤ 0.01967, respectively κ_m ≤ 0.01100.

*Proof.* For |x| < 1, the covector θ := dφ1/|dφ1| has norm 1, and as dφ1(ê₃) = dφ1(ê₄) = dφ1(e₃) = dφ1(e₄) = 0, the
inverses in [[lem:tl5-cip-form]] (a) and [[eq:tl5-wg-khat]] give |dφ1|² = γ_s^(φ1φ1) = 2/(r²(1 + x)) and

    (g_N⁻¹ − ĝ⁻¹)(θ, θ) = γ_N^(φ1φ1)/γ_s^(φ1φ1) − 1 = r² e^(−2P)/R² − 1,

so |g_N⁻¹ − ĝ⁻¹| ≥ |r² e^(−2P)/R² − 1|, and the same holds at x = 1 by continuity, with P(v, 1) = (4/3) m(v, 1) =
(4/3) φ cos(v/λ), as h(1) = 1. At the first seed take v = 9/4: v(11.1148) < 9/4 < v(11.1149) in [[eq:cone-v]], so r ∈
(11.1148, 11.1149) and r^(−3/2) ≥ 0.0269861; env(9/4) = sin⁴(7π/12) = (7 + 4√3)/16 ≥ 0.870512 and cos(9/4) ≤ −0.628173.
So P < 0 and, as R ≤ r, r² e^(−2P)/R² − 1 ≥ e^(−2P) − 1 ≥ −2P, and −2P equals (4/3) r^(−3/2) env(9/4) |cos(9/4)| ≥
(4/3) × 0.0269861 × 0.870512 × 0.628173 ≥ 0.01967. At the second seed take v = 2: r ∈ (10.9909, 10.9910), env(2) = 1,
cos(2√10) ≥ 0.999144 and φ = (1/(2√10)) r^(−3/2) ≥ 0.0043392, so P ≥ (4/3) × 0.0043392 × 0.999144 ≥ 0.00578 and
e^(−2P) ≤ e^(−0.01156) ≤ 0.988507. By [[prop:cone-exact]] (a), r − R ≤ W̄ r (r − r_s)²/2 ≤
8.55 × 10⁻⁴ × 10.991 × 0.74344²/2 ≤ 0.0025970, so r/R ≤ 10.9910/10.988303 ≤ 1.000246 and r²/R² ≤ 1.000493; hence
r² e^(−2P)/R² − 1 ≤ 0.988507 × 1.000493 − 1 ≤ −0.01100. The left side of (T) is at least |g_N⁻¹ − ĝ⁻¹|. ∎

**Remark {#rem:tl5-xt-background}** (The background of the estimate.) ĝ_♮ serves [[thm:tl5-wg]]: it gives data in the
wave gauge and the local existence, uniqueness and continuation of the reduced problem for the first stage. It is the
seed outside the strip |u + 10| < η₁, and across the strip it passes from the data to the seed; nothing here bounds its
Ricci tensor there. A background for an a priori estimate is to have a small Ricci tensor on all of D̄; by
[[prop:tl5-xt-seed]] the seed itself does not satisfy (T) for κ_m ≤ 0.01967 at the first seed when v* ≥ 9/4, nor for
κ_m ≤ 0.01100 at the second when v* ≥ 2. For a background whose values and first derivatives on N₀⁺ are the seed's,
(X) and (T) follow from [[eq:tl5-xt-condition]] or [[eq:tl5-xt-condition-general]], conditions on N₁ alone. For
G^♯ − ĝ to vanish with its partial derivatives of order at most k on N₀⁺ by [[lem:tl5-xt-order]], ĝ − g′ is to vanish to
order k + 1 there; for k ≥ 3, by [[lem:tl5-xt-seed-jets]] (b), this asks that the derivatives in v of ĝ of the orders 4
to k + 1 at the points of N₀⁺ be those of the development, which at order 4 are not the seed's.

### Placement

This part and the crosswalk rows below are instructions for merging; they are not chapter text. Line numbers are those
of chapters/87-ten-l5.md at the time of writing (HEAD dbf04838; lines 1–2760 are those of edafc288) and serve only to
find the place; each old text is quoted exactly, and each new text replaces it as a whole, with the line breaks shown.

*1. Where the subsection goes.* The subsection above, from its heading "#### The conditions (X) and (T) at the first
stage {#sec:tl5-xt}" through [[rem:tl5-xt-background]], is inserted in [[ch:ten-l5]] immediately after the proof of
[[cor:tl5-wg-data-first-stage]], whose last line is "[[thm:tl5-wg-data]] the rest. ∎" (line 2757), and before the heading
"### Double-null coordinates for a metric close to the background {#sec:tl5-dn}" (line 2759), with one blank line before
and one after. It is the last subsection of [[sec:tl5-wg]]. It defines the 21 labels listed in the crosswalk rows below,
none of which is defined elsewhere.

*2. The sentence on existence after [[def:tl5-wg-data]] (lines 2151–2153).* Old:

    the coordinates are wave coordinates relative to ĝ along N⁺, to infinite order. Data in the wave gauge exist for smooth
    data g_N on N⁺ satisfying the constraints, in particular for the data of the first stage of the problem at 10 l5,
    whenever two explicit conditions on N⁺ hold ([[thm:tl5-wg-data]], [[cor:tl5-wg-data-first-stage]]). By

New:

    the coordinates are wave coordinates relative to ĝ along N⁺, to infinite order. Data in the wave gauge exist for smooth
    data g_N on N⁺ satisfying the constraints, in particular for the data of the first stage of the problem at 10 l5,
    whenever two explicit conditions on N⁺ hold ([[thm:tl5-wg-data]], [[cor:tl5-wg-data-first-stage]]); at the first
    stage with u* < −1 they hold for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and
    for a background with the seed's values and first derivatives on N₀⁺ they follow from explicit inequalities on its
    departure from the data along N₁ ([[thm:tl5-xt]]). By

*3. The end of the first paragraph of [[sec:tl5-wg-first-stage]] (line 2500).* Old:

    explicit conditions of [[thm:tl5-wg-data]] for the invertibility of the map and for (W4).

New:

    explicit conditions of [[thm:tl5-wg-data]] for the invertibility of the map and for (W4). [[sec:tl5-xt]] shows that
    they hold at the first stage when u* < −1, for an explicit background.

*4. Other texts.* No other text of the chapters changes because of this file. The opening paragraph of [[ch:ten-l5]] and
[[rem:tl5-beyond]] describe the continuation lemma and are unaffected. No number already printed changes.

*5. References.* [[sec:tl5-xt]] cites, as they stand: [[thm:tl5-wg-data]], [[cor:tl5-wg-data-first-stage]],
[[lem:tl5-wg-lchart]], [[lem:tl5-wg-tension]] (a), step (i) of the proof of [[lem:tl5-wg-wavemap]], [[lem:tl5-wg-norms]]
(a) and (b), [[eq:tl5-wg-khat]], [[def:tl5-wg-background]], [[def:tl5-wg-domains]], [[thm:tl5-wg]] and the frame of
[[sec:tl5-wg-equations]]; from [[sec:tl5-cip]], [[lem:tl5-cip-jets]] (a) with m = 3 and steps (i) and (ii) of its proof
with k = 4, [[lem:tl5-cip-frame]] ([[eq:tl5-cip-ricci]], [[eq:tl5-cip-connection]]), [[lem:tl5-cip-form]] (a),
[[lem:tl5-cip-shift]] and the paragraph after it (regularity of R, P, Q and b in v at v = 1/2), the proof of
[[lem:tl5-cip-extend]] (a) (Seeley's operator in one variable), [[cor:tl5-cip-staged]] (a) and the paragraph before it
(the field on N is C³ in v); [[lem:tl5-seed]] (a), (b), (d) and the formula ∂_uR = −2e^(2W) of the proof of (c),
[[def:tl5-problem]], [[def:tl5-seeds]], [[eq:cone-v]], [[eq:cone-data]], [[eq:cone-w]], [[lem:cone-generator]] and its
proof (∂_vW = 1/(2r³), ∂_vm = (f/2)hA), [[lem:cone-w]] ((8/9)(A² + B²) ≤ W̄), [[prop:cone-exact]] (a) and its proof (the
integral equation), [[cor:cone-compare]] (2ℓ² ≤ 1.1064, 2ℓ ≤ 1.4876), [[lem:cone-raychaudhuri]] (the determinant) and
[[lem:tl5-leaf-expansion]]. No result of the literature is used beyond those these cite; Appendix A is unchanged.

*6. Remarks for the writers of the a priori estimate and of the background.* These are not chapter text.
(i) [[lem:tl5-xt-order]] (c) gives the order of agreement of G^♯ with ĝ on N₀⁺ from that of ĝ with the development:
order k for G^♯ − ĝ needs order k + 1 for ĝ − g′. A hypothesis that G^♯ − ĝ vanish to order N + 1 on N₀ therefore asks
ĝ − g′ to vanish to order N + 2 on N₀⁺. What [[lem:tl5-xt-seed-jets]] (b) shows is that the fourth derivatives in v
of the leaf metric of the development on N₀⁺ are not the seed's (off at most one torus {x = c}). So a background with
the seed's derivatives of order at most 4 on N₀⁺, for instance "seed plus (v − 1/2)⁵ times a smooth field", has ĝ − g′
vanishing to order 3 and not to order 4, and [[lem:tl5-xt-order]] gives G^♯ − ĝ to order 2 for it; no higher order is
shown. For "seed plus (v − 1/2)⁴ times a smooth field G" the fourth v-derivative on N₀⁺ is the seed's plus 4! times the
value of G at v = 1/2, and ĝ − g′ vanishes to order 4 exactly when that value is the difference of the development's
and the seed's fourth derivatives divided by 4!. In either form, order N + 2 asks that ĝ carry the development's v-jets
of orders 4 to N + 2 on N₀⁺, which solve the linear transport equations of the proof of [[lem:tl5-cip-jets]] (a) along
N₀⁺, with the seed's coefficients and with initial values the data's one-sided v-derivatives at S; the alternative is a
data term on N₀ in the estimate, as on N₁. This is a sufficient route; that it is necessary is not shown.
(ii) For a background with the seed's 1-jet on N₀⁺ that equals the data at the points of N₁, (X) and (T) hold if ∂_uR̂
matches ρ of [[eq:tl5-xt-rho]] to 0.8329 κ_m (first seed) or 0.8630 κ_m (second seed) in the maximum over N₁ (v* = 7/2);
the other transverse derivatives do not enter. For one that only approximates the data on N₁, they hold if
2ε₀ + 4.996 · 3 e^(3K̄₁) ε₁ < κ_m, with ε₀ and ε₁ maxima over N₁ in the norm of k̂; in the norm built from E₀ of the
multiplier frame, whose ratio to that of k̂ on N₁ is bounded by c(−10)^(−r/2) = (f(10)/2)^(−r/2) for tensors of rank r,
these are ε₀ ≤ ε₀′/0.495 and ε₁ ≤ ε₁′/0.3482.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns (label, source, source name, note), separated by tabs, in
chapter order. The source is "paper/reader/proofs/P-XT.md@PENDING:N", N the line of the label in this file and PENDING
to be replaced by the commit at which this file is merged.

    sec:tl5-xt	paper/reader/proofs/P-XT.md@PENDING:1	P-XT, subsection	new: (X), (T) of thm:tl5-wg-data at the first stage for u* < -1 (data item L1 of the plan); after cor:tl5-wg-data-first-stage, before sec:tl5-dn
    eq:tl5-xt-ew	paper/reader/proofs/P-XT.md@PENDING:22	P-XT, display	e^W at v = 1/2 and 7/2 on N1
    lem:tl5-xt-implies	paper/reader/proofs/P-XT.md@PENDING:27	P-XT, Lemma	(T) implies (X) for every background (kappa_m <= 1/4, lem:tl5-wg-norms (b))
    lem:tl5-xt-seed-jets	paper/reader/proofs/P-XT.md@PENDING:41	P-XT, Lemma	development = seed to order 3 on N0+ (lem:tl5-cip-jets (a), m = 3); differs at order 4 off one torus (env C3 not C4)
    lem:tl5-xt-order	paper/reader/proofs/P-XT.md@PENDING:78	P-XT, Lemma	ghat - g' to order m on N0+ gives Upsilon to m-1, Psi - id to m, G^sharp - ghat to m-1; (X), (T) on N0+
    lem:tl5-xt-gauge	paper/reader/proofs/P-XT.md@PENDING:122	P-XT, Lemma	|nabla_v khat| in closed form; Upsilon(g') = (3e^-2W/2R) d_u(R' - Rhat) d_v when ghat = data on N1; general bound by eps0, eps1
    eq:tl5-xt-upsilon	paper/reader/proofs/P-XT.md@PENDING:133	P-XT, display	the gauge vector on N1
    lem:tl5-xt-rho	paper/reader/proofs/P-XT.md@PENDING:174	P-XT, Lemma	traced angular vacuum equation: d_v(R^2 d_u R) explicit; transverse derivative of R on N1 by one quadrature of the data
    eq:tl5-xt-rho	paper/reader/proofs/P-XT.md@PENDING:191	P-XT, display	rho
    lem:tl5-xt-rx	paper/reader/proofs/P-XT.md@PENDING:219	P-XT, Lemma	|d_x R| and |d_x d_r R| on the data cone, both seeds (|d_x w| <= Wbar)
    lem:tl5-xt-k1	paper/reader/proofs/P-XT.md@PENDING:241	P-XT, Lemma	K1 <= 0.1038 (seed 1), 0.09194 (seed 2), every v* <= 7/2; shift 1-form bounded through the shift constraint
    eq:tl5-xt-k1	paper/reader/proofs/P-XT.md@PENDING:244	P-XT, display	the bound frak K
    thm:tl5-xt	paper/reader/proofs/P-XT.md@PENDING:289	P-XT, Theorem	(X), (T) on N0+ free; on N1: eps_R <= 0.8329 kappa_m (seed 1), <= 0.8630 kappa_m (seed 2) at v* = 7/2 (sufficient); general 2eps0 + 4.996 (v*-1/2) e^(K1(v*-1/2)) eps1 < kappa_m
    eq:tl5-xt-condition	paper/reader/proofs/P-XT.md@PENDING:298	P-XT, display	condition for backgrounds equal to the data on N1
    eq:tl5-xt-condition-general	paper/reader/proofs/P-XT.md@PENDING:306	P-XT, display	condition in general
    def:tl5-xt-natural	paper/reader/proofs/P-XT.md@PENDING:333	P-XT, Definition	ghat_natural: seed + data on N1 + transverse R from rho, cut off to a strip at u = -10
    eq:tl5-xt-natural	paper/reader/proofs/P-XT.md@PENDING:346	P-XT, display	the fields of ghat_natural
    lem:tl5-xt-natural	paper/reader/proofs/P-XT.md@PENDING:348	P-XT, Lemma	a background on a set containing Dbar and N+; seed 3-jet on N0+; = data on N1 with d_u Rhat = rho
    cor:tl5-xt-data	paper/reader/proofs/P-XT.md@PENDING:390	P-XT, Corollary	data in the wave gauge for the first stage, both seeds, every u* < -1, every v* <= 7/2, every kappa
    prop:tl5-xt-seed	paper/reader/proofs/P-XT.md@PENDING:401	P-XT, Proposition	the seed as background fails (T) on N1 for kappa_m <= 0.01967 (seed 1), 0.01100 (seed 2)
    rem:tl5-xt-background	paper/reader/proofs/P-XT.md@PENDING:425	P-XT, Remark	ghat_natural serves the local theory, not the estimate; order N+2 on N0+ needs the development's jets
