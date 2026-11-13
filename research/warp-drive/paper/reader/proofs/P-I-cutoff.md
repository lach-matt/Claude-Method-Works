<!-- Replaces, in chapter 63 (ch:own-data): the paragraph "The truncated problems" (lines 648-653) by
def:cutoff-truncation; item (iii) of lem:own-truncation (lines 660-663) and its proof (lines 682-686) by
prop:cutoff-cap, and "g_b0 + Σ" in item (iv) and its proof (lines 686-688) by "g_b0 + Σ + Σ′_J"; the bound of e(T)
in the proof of lem:own-exterior (lines 709-710) by the pointwise bounds of prop:cutoff-cap; in the proof of
thm:own-continuation, "the first term O(λ r⁻⁶) or 0" of Step 1 (line 738), the cap sentence of Step 3 with its
marker (lines 784-786), the cap of Step 4 (lines 800-801) and the cap of Step 5 (lines 807-809), as stated in
prop:cutoff-continuation; and the values of D_T on Σ̃_T in the proof of prop:own-vacuum (ii) (lines 852-857) by
lem:cutoff-gauge. Placement: sec:cutoff-expansion after lem:own-n-data (end of sec:own-sigma); def:cutoff-truncation
in place of the paragraph "The truncated problems"; sec:cutoff-cap in place of item (iii) of lem:own-truncation,
directly after that lemma; prop:cutoff-continuation, lem:cutoff-independence and lem:cutoff-gauge at the end of
sec:own-continuation. -->

### The expansion after the shell to every order {#sec:cutoff-expansion}

The truncated problems of Section [[sec:own-continuation]] interpolate, on a band of bounded width in v, between the
data of g_λ and data that continue them to spatial infinity. The commuted energies of the remainder at the initial
slice are small, uniformly in the truncation, only if the two data agree on the band to high order in r⁻¹: the
commutator Z is transverse to the initial slice at the band with a coefficient of size |T|, and each Z turns a time
derivative of a mismatch into a factor |T| ([[rem:cutoff-growth]]). This section supplies continuation data that
agree with those of g_λ to every prescribed order and are homogeneous, hence harmless for Z. It uses only the
expansion of [[prop:bondi-hierarchy]] at fixed λ; no smallness in λ is needed of the new terms, because they enter
only the data of the truncated problems, whose effect is removed by letting T → −∞ at fixed λ.

*Setting.* We use the notation of [[ch:own-data]] and of Section [[sec:far-homogeneity]]: P(h) = Ric^H(g_b0 + h; g_b0),
g_b0 = η + μ m with m := r⁻² dv ⊗ dv, μ = μ_end, the coordinates (v, r, x̂) with ℓ = ∂_r at fixed (v, x̂) and ∂_v
the derivative at fixed (r, x̂), which is ∂_t at fixed x. The Cartesian derivatives are

    ∂_t = ∂_v,     ∂_i = x̂_i (∂_v + ℓ) + r⁻¹ Y_i,     Y_i := r (∂_i − x̂_i x̂·∂_x),               {#eq:cutoff-cartesian}

where Y_i is a vector field on the sphere {v, r fixed}, acting on x̂ only, with coefficients smooth in x̂. Put
I_1 := [v_end + 1, V′_P − 1], which contains v1 (v1 ≥ v_end + 2 and v1 ≤ V′_P − κ_P − 1 − m_Ω,
[[lem:interior-far-part]] (ii)), and 𝒰_1 := {(v, r, x̂) : v ∈ I_1, r ≥ r_1}, with r_1 so large that 𝒰_1 lies in the far
region of P′ (there t_P is comparable with r, and v + h_P(τ) ≤ V′_P − 1 + κ_P < V′_P). On 𝒰_1, v > v_end, so g0 = g_b0,
G_3 = 0 ([[eq:own-g3]], env = 0) and, by [[prop:bondi-hierarchy]], for every J ≥ 4

    g_λ − g_b0 = H_J + u_J,     H_J := Σ_(k=4)^J r^(−k/2) G_k.                                            {#eq:cutoff-hj}

A family of smooth tensors F on 𝒰_1, or on a subset of it, is *of strip order q* if |∂_v^i Ω^β ℓ^j F| ≤ C r^(−q−j) for
all i, β, j up to a fixed order, the constant independent of the members of the family. By [[eq:bondi-expansion]],
u_J is of strip order (J + 1)/2, and H_J of strip order 2, the G_k being bounded with all their derivatives. A
*monomial* is r^(−k/2) (v − v1)^n a(x̂) with integers k, n ≥ 0 and a smooth; its *weight* is n − k/2. Since
r^(−k/2) (v − v1)^n = r^(n−k/2) s^n with s = (v − v1)/r, a monomial is homogeneous, of degree equal to its weight,
under the dilation D_ς of Section [[sec:far-homogeneity]].

**Lemma {#lem:cutoff-expansion}** (the operator at fixed v). Let K ≥ 4, let c_4, …, c_K be smooth symmetric tensors on
I_1 × S³ (Cartesian components), bounded with all derivatives, and put H := Σ_(k=4)^K r^(−k/2) c_k and c_k := 0 for
k ∉ [4, K]. There is r_2 ≥ r_1 and, for every q ∈ ½ℕ, a smooth π_q(v, x̂) such that for every Q ≥ 0 the difference
P(H) − Σ_(q≤Q) r^(−q) π_q is of strip order Q + ½ on {v ∈ I_1, r ≥ r_2}; π_q = 0 for q < 3; and

    π_q = ((2q − 5)/2) ∂_v c_(2q−2) − ½ (Δ̊ + (q − 2)(q − 4)) c_(2q−4) + R_q,                             {#eq:cutoff-pi}

where R_q is a finite sum of terms

    a(x̂) μ^j Π_(i=1)^n ∂_v^(d_i) Y^(β_i) c_(k_i),     n ≥ 1,  n + j ≥ 2,  Σ_i d_i ≤ 2,
    Σ_i k_i/2 + 2j + 2 − Σ_i d_i = q,                                                                  {#eq:cutoff-terms}

Y^(β_i) a product of fields Y_l and a smooth. In particular every c_(k_i) in R_q has k_i ≤ 2q − 4.

*Proof.* By [[lem:far-scaling]] (a), with g = g_b0 + H = η + μ m + H, P(H) is a finite sum of products of components
of g and g⁻¹ with ∂∂g, ∂g ∂g, Γ̂ ∂g, ∂Γ̂ or Γ̂ Γ̂, Γ̂ := Γ[g_b0]. Here ∂g = μ ∂m + ∂H and ∂∂g = μ ∂∂m + ∂∂H, and Γ̂ is
½ g_b0⁻¹ applied to first derivatives of μ m, with g_b0⁻¹ = η⁻¹ − μ r⁻² L0 ⊗ L0 ([[eq:background]]), the Cartesian
components of L0 and of dv being functions of x̂. For r ≥ r_2, |g_b0⁻¹ H| ≤ ½ on {v ∈ I_1}, and
g⁻¹ = Σ_(ν≥0) (−g_b0⁻¹ H)^ν g_b0⁻¹. So every term of P(H) is a product of constant tensors, of factors μ r⁻² b(x̂)
(from μ m and from g_b0⁻¹ − η⁻¹), of factors r^(−k/2) c_k, and of exactly two derivatives, Γ̂ counting as one derivative
of a factor μ r⁻² b and ∂Γ̂ as two. By [[eq:cutoff-cartesian]], ∂_v maps r^(−k/2) c to r^(−k/2) ∂_v c and annihilates
r⁻² b(x̂) and every function of x̂; ℓ and r⁻¹ Y_i map r^(−k/2) c to r^(−k/2−1) times −(k/2) c and Y_i c, and r⁻² b to
r⁻³ times a function of x̂. Hence a product with n factors c_(k_i), j factors μ r⁻² b, and d_i derivatives ∂_v on the
i-th factor c_(k_i) is a sum of terms r^(−q) times a term of the form [[eq:cutoff-terms]], with
q = Σ_i k_i/2 + 2j + 2 − Σ_i d_i: every derivative other than a ∂_v on a factor c_(k_i) raises the power of r⁻¹ by
one or gives zero. Truncating the Neumann series after ν_0 terms leaves a remainder of strip order 2ν_0, and the terms
with q > Q have q ≥ Q + ½; this gives the expansion, with π_q the sum of the terms of order q.

The terms with n = 0 are the expansion of P(0) = Ric^H(g_b0; g_b0) = Ric(g_b0) = 0 (with reference g_b0 itself the
vector field D vanishes, and g_b0 is the Tangherlini metric), so they sum to zero at every order. The terms with n = 1
and j = 0 come from −½ η^(ab) ∂_a ∂_b H only: every other term of [[lem:far-scaling]] (a) that is linear in H contains
Γ̂, ∂Γ̂, μ ∂m, μ ∂∂m or a factor μ r⁻² L0 ⊗ L0. By [[eq:own-box-p]] at μ = 0, applied to each Cartesian component,
−½ □_η (r^(−k/2) c_k) = ((k − 3)/2) r^(−k/2−1) ∂_v c_k − ½ r^(−k/2−2) (Δ̊ + k²/4 − k) c_k, which at q = k/2 + 1 and
q = k/2 + 2 gives the first two terms of [[eq:cutoff-pi]] ((k/2)² − k = (q − 2)(q − 4) for k = 2q − 4). The terms with
n + j ≥ 2 form R_q. The flat terms have d ≤ 1, since □_η has no term ∂_v² in (v, r, x̂) ([[eq:wave-operator-vr]] at
μ = 0); so they start at q = 3, and the terms of R_q at q ≥ 4. In a term of R_q each factor contributes at least 2 to
q, so k_i/2 ≤ q − 2. ∎

**Lemma {#lem:cutoff-polynomial}** (the coefficients after the shell). For every k ≥ 4 the restriction of G_k to
I_1 × S³ is a polynomial in v − v1 of degree at most k/2 − 2,

    G_k = Σ_(0≤n≤k/2−2) (v − v1)^n G_(k,n)(x̂),                                                        {#eq:cutoff-gkn}

with G_(k,n) smooth and G-invariant; so every monomial r^(−k/2)(v − v1)^n G_(k,n) has weight at most −2. For p ∈ Π let
F_(p,n) := (1/n!) ∂_s^n F_p(0, ·) be the Taylor coefficients at s = 0 of the F_p of [[def:own-sigma]], and put
F_(p,n) := 0 for p ∉ Π. Then G_(k,n) = F_(k/2−n, n) whenever the weight n − k/2 exceeds −4.

*Proof.* *The recursion.* Fix J ≥ 4. On 𝒰_1, P(H_J + u_J) = Ric^H(g_λ; g0) = 0, g_λ being vacuum and in the wave-map
gauge relative to g0 ([[thm:past-construction]]). Write P(H) = −½ g(H)^(ab) ∂_a ∂_b H + N(X, H, ∂H), N collecting the
first-order terms of [[lem:far-scaling]] (a) and −½ g^(ab) ∂_a ∂_b g_b0. Then P(H_J + u_J) − P(H_J) is the sum of
−½ g_λ^(ab) ∂_a ∂_b u_J, of −½ (g_λ^(ab) − g_J^(ab)) ∂_a ∂_b (g_b0 + H_J) with g_J := g_b0 + H_J, and of
N(X, H_J + u_J, ∂H_J + ∂u_J) − N(X, H_J, ∂H_J). By [[eq:cutoff-cartesian]] the Cartesian Hessian of a function φ is
(∂_a v)(∂_b v) ∂_v² φ plus terms each containing ℓ or r⁻¹ Y, or a first derivative with a coefficient O(r⁻¹) from the
derivatives of x̂; and g_λ⁻¹(dv, dv) = (g_λ⁻¹ − g_b0⁻¹)(dv, dv) = O(r⁻²), since dv(L0) = 0 makes dv null for g_b0. So
the first term is of strip order (J + 3)/2. The second and third contain u_J or ∂u_J times factors of strip order at
least 2, and are of strip order (J + 5)/2. Hence P(H_J) is of strip order (J + 3)/2, and by [[lem:cutoff-expansion]]
with c_k = G_k, multiplying by r^q and letting r → ∞ at fixed (v, x̂), π_q = 0 for q ≤ (J + 2)/2. As J is arbitrary,
for every q ≥ 3

    (2q − 5) ∂_v G_(2q−2) = (Δ̊ + (q − 2)(q − 4)) G_(2q−4) − 2 R_q,                                {#eq:cutoff-recursion}

R_q being formed from the G_k, k ≤ 2q − 4, by [[eq:cutoff-terms]] (G_2 := G_3 := 0).

*The degree.* By induction on k. For k = 4 (q = 3), R_3 = 0 and G_2 = 0, so ∂_v G_4 = 0. Let k ≥ 5, q := (k + 2)/2,
and suppose the claim for 4 ≤ k′ < k. G_(k−2) has degree at most q − 4, and a term [[eq:cutoff-terms]] of R_q has
degree at most Σ_i (k_i/2 − 2) − Σ_i d_i = q − 2 − 2j − 2n ≤ q − 6. So ∂_v G_k, by [[eq:cutoff-recursion]] with
2q − 5 = k − 3 > 0, is a polynomial of degree at most q − 4 = k/2 − 3 (zero if that is negative), and
G_k(v) = G_k(v1) + ∫_(v1)^v ∂_v G_k has degree at most k/2 − 2. The coefficients are smooth, and G-invariant because G_k
is ([[prop:bondi-hierarchy]]) and G fixes v.

*The weights above −4.* Take in [[eq:cutoff-recursion]] the coefficient of (v − v1)^n, with k := 2q − 2:
(k − 3)(n + 1) G_(k,n+1) = (Δ̊ + (q − 2)(q − 4)) G_(k−2,n) − 2 [R_q]_n, where [R_q]_n = 0 for n > q − 6. The monomials
(k, n + 1) and (k − 2, n) have the same weight n + 1 − k/2 =: −p. If p < 4 then n > q − 6, and with k = 2(p + n + 1),

    (n + 1)(2p + 2n − 1) G_(2(p+n+1), n+1) = (Δ̊ + (p + n)(p + n − 2)) G_(2(p+n), n).       {#eq:cutoff-weight-recursion}

The weights are at most −2 and lie in ½ℤ, so p < 4 means p ∈ {2, 5/2, 3, 7/2} ⊂ Π. For p ∈ Π, the calculation in the
proof of [[lem:own-self-similar]], made for a smooth F(s, x̂) with Δ̊ acting on each Cartesian component, gives

    □_η (r^(−p) F) = −2 r^(−p−2) [ (s − s²/2) ∂_s² F + (p − ½)(1 − s) ∂_s F − ½ (p² − 2p + Δ̊) F ].      {#eq:cutoff-ode}

Since □_η Σ_p = 0, the bracket vanishes for F = F_p on [0, 3/2] × S³, and its coefficient of s^n at s = 0 is
½ [(n + 1)(2p + 2n − 1) F_(p,n+1) − (Δ̊ + (p + n)(p + n − 2)) F_(p,n)], as n(n − 1) + (2p − 1) n + p² − 2p =
(p + n)(p + n − 2). So the F_(p,n) satisfy [[eq:cutoff-weight-recursion]] too. At n = 0, G_(2p,0) = G_(2p)(v1) = F_p(0) =
F_(p,0) ([[def:own-sigma]]), and 2p + 2n − 1 > 0; by induction on n, G_(2(p+n),n) = F_(p,n). ∎

**Definition {#def:cutoff-extension}** (the continuation of the expansion). For an integer J ≥ 8 put

    Σ′_J := Σ_(8≤k≤J) Σ_(0≤n≤k/2−4) r^(−k/2) (v − v1)^n (G_(k,n) − F_(k/2−n, n))
          = Σ_(8≤k≤J) Σ_(0≤n≤k/2−4) r^(−(k/2−n)) s^n (G_(k,n) − F_(k/2−n, n)),                     {#eq:cutoff-extension}

a finite sum, defined on {r > 0} by its second form, and m_J := g_λ − g_b0 − Σ − Σ′_J on 𝒰_1.

**Lemma {#lem:cutoff-extension}** (the continued expansion). Let J ≥ 8.
(a) Σ′_J is a finite sum of smooth homogeneous tensors of degrees at most −4, and it is G-invariant. On
W ∩ {r ≥ 1}, |∂^j Γ^α Σ′_J| ≤ C r^(−4−j) for all j and α, with C depending on λ, J, j and α.
(b) m_J is of strip order (J + 1)/2 on 𝒰_1, with constants depending on λ and J.

*Proof.* (a) Each term is r^(−p) s^n a(x̂) with p = k/2 − n ≥ 4, a polynomial in s with smooth coefficients, so smooth
and homogeneous of degree −p on 𝒞_1 = {r ≥ 1, 0 ≤ s ≤ 3/2} ⊃ W. The bounds follow as [[eq:far-sigma-bounds]], from the
dilation (Section [[sec:far-homogeneity]]). G-invariance: G_(k,n) and F_(p,n) are Taylor coefficients at v = v1 of the
G-invariant G_k ([[lem:cutoff-polynomial]]) and Σ_p ([[lem:own-sigma-data]] (c)).

(b) For p ∈ Π let M_p := ⌊J/2 − p⌋ ≥ 0 and split

    Σ_p = Σ_(n≤M_p) r^(−p−n) (v − v1)^n F_(p,n) + r^(−p) s^(M_p+1) ρ_p(s, x̂),

with ρ_p smooth on [0, 3/2] × S³ (Taylor's formula with integral remainder; F_p is smooth there by
[[lem:own-self-similar]]). The polynomial part of Σ consists of the monomials r^(−k/2)(v − v1)^n F_(k/2−n, n) with
k ≤ J. By [[lem:cutoff-polynomial]], H_J is the sum of the monomials r^(−k/2)(v − v1)^n G_(k,n), k ≤ J, and
G_(k,n) = F_(k/2−n, n) at the weights above −4; at the weights −4 and below, the coefficient of Σ plus that of Σ′_J is
F_(k/2−n,n) + (G_(k,n) − F_(k/2−n,n)) = G_(k,n). Hence, by [[eq:cutoff-hj]],

    m_J = u_J − Σ_(p∈Π) r^(−p) s^(M_p+1) ρ_p(s, x̂).

u_J is of strip order (J + 1)/2. On 𝒰_1, v − v1 ≤ V′_P − v1 =: d_V, so s ≤ d_V/r. With ∂_v = r⁻¹ ∂_s and
ℓ(r^(−p) φ(s, x̂)) = −r^(−p−1) (p φ + s ∂_s φ), every ∂_v^i Ω^β ℓ^j of r^(−p) s^(M+1) ρ is r^(−p−j) times a sum of terms
r^(−i′) ∂_s^(i′)(s^(M+1) ρ′) with ρ′ smooth, each at most C r^(−(M+1)) d_V^(M+1); and p + M_p + 1 ≥ (J + 1)/2, as
J/2 − p ∈ ½ℤ. ∎

**Remark {#rem:cutoff-weights}** (what is new in Σ′_J). The weight −4 terms of Σ′_J are r⁻⁴ s^n (G_(8+2n,n) − F_(4,n)),
n ≥ 1. They are nonzero in general: at weight −4 the terms R_q of [[eq:cutoff-recursion]] are the products of two
factors of weight −2, or of μ with one, the terms of which Q_6 of [[prop:far-residual]] is made, whereas Σ_4 solves
□_η Σ_4 = 0; the two agree at s = 0. The terms of weight −9/2 and below are the higher homogeneous components of
g_λ − g_b0, truncated as polynomials in s. Their sizes in λ are not controlled here and are not needed.

### The truncated problems and the initial slice {#sec:cutoff-cap}

**Definition {#def:cutoff-truncation}** (the truncated problems). Fix an integer J ≥ 2k1 + 7. Extend f from [4R, ∞) to
a smooth function F̂ on [a′, ∞) with |F̂′| ≤ ¼ and |F̂| ≤ C_f. For T ≤ −1 put 𝒮_T := {τ = T + F̂(|x|), |x| ≥ a′}, which
is {t̃ = T} on r ≥ 4R, δ_0 := V′_P − κ_P − v1 (≥ 4 by [[lem:interior-far-part]] (ii)),
V_T := V′_P − δ_0/2 − h_P(T − C_f), and let χ_T(v) be smooth, 0 for v ≤ V_T and 1 for v ≥ V_T + δ_0/4, with derivatives
bounded independently of T. Put

    D_T := (1 − χ_T) g_λ + χ_T (g_b0 + Σ + Σ′_J),                                                      {#eq:cutoff-data}

defined where g_λ is defined or χ_T = 1. The *truncated problem* is the Cauchy problem for Ric^H(g) = 0 relative to g0
with data (g, ∂_τ g) on 𝒮_T equal to those of D_T. (Σ and Σ′_J are defined on {v ≥ v1}, which contains the support of
χ_T, as V_T ≥ v1 + δ_0/2.)

[[lem:own-truncation]] (i), (ii) and (iv) hold for these problems, for T ≤ T_0 with T_0 depending on λ and J, with
their proofs, g_b0 + Σ + Σ′_J in place of g_b0 + Σ: (i) and (ii) involve the data only where χ_T < 1, and on
𝒮_T ∩ {v ≥ V_T}, which lies in {r ≥ |T| − C}, |Σ′_J| ≤ C(λ, J) r⁻⁴ is as small as needed for T ≤ T_0; in (iv) the data
g_b0 + Σ + Σ′_J are smooth with every derivative bounded ([[lem:cutoff-extension]] (a)) and G-invariant. Item (iii) is
replaced by [[prop:cutoff-cap]]. We take T_0 so large in modulus that, besides, every point of Σ̃_T has r ≥ r_2 of
[[lem:cutoff-expansion]].

Write 𝒮^♭_T := Σ̃_T ∩ {v ≤ V_T + δ_0/4} for the part of the initial slice from N to the outer edge of the band; it is
{r_T ≤ r ≤ r_T + d_V} along the rays of Σ̃_T (v increases along them with dv/dr ≥ 1, [[lem:own-wedge]] (b)), and
r_T ≥ c_W (1 + |T|). Near Σ̃_T put

    H_0 := Σ + Σ′_J,     M := (1 − χ_T) m_J  (M := 0 where χ_T = 1),     H_D := D_T − g_b0 = H_0 + M,     {#eq:cutoff-hd}

the identity on the strip being D_T − g_b0 = Σ + Σ′_J + (1 − χ_T)(g_λ − g_b0 − Σ − Σ′_J). Let δ := g_T − D_T, defined on
W_T ∩ {t̃ ≤ T + δ_T} near Σ̃_T. Then h_R = g_T − g_b0 − Σ = Σ′_J + M + δ there.

**Definition {#def:cutoff-classes}** (two classes on the initial slice). Let N_0 be an integer and q ∈ ℝ. A family of
functions F, each defined on a neighbourhood of Σ̃_T in {t̃ ≥ T} and depending on T ≤ T_0, belongs to
- 𝒯^q if |∂^β F| ≤ C r^(−q−|β|) on Σ̃_T for |β| ≤ N_0;
- ℬ^q if |∂^β F| ≤ C r^(−q) on Σ̃_T for |β| ≤ N_0, and ∂^β F = 0 on Σ̃_T ∖ 𝒮^♭_T;
where ∂^β are Cartesian derivatives in (t, x) and C does not depend on T. ℰ is the class of F with |∂^β F| ≤ C on Σ̃_T
for |β| ≤ N_0.

**Lemma {#lem:cutoff-classes}** (the calculus of the classes). (a) 𝒯^q ⊂ 𝒯^(q′) and ℬ^q ⊂ ℬ^(q′) for q ≥ q′;
𝒯^(q1) 𝒯^(q2) ⊂ 𝒯^(q1+q2), 𝒯^(q1) ℬ^(q2) ⊂ ℬ^(q1+q2) and ℬ^(q1) ℬ^(q2) ⊂ ℬ^(q1+q2); ℰ ℬ^q ⊂ ℬ^q; and 𝒯^q, ℬ^q ⊂ ℰ for
q ≥ 0. (b) ∂ maps 𝒯^q into 𝒯^(q+1) and ℬ^q into ℬ^q, with N_0 lowered by one. (c) A tame field of order q on W, that
is a field with |∂^j Γ^α F| ≤ C r^(−q−j) on W ∩ {r ≥ r_2} for j + |α| ≤ N_0, restricts to 𝒯^q. A family of strip order q
on 𝒰_1 whose members vanish where v ≥ V_T + δ_0/4 belongs to ℬ^q. (d) Let Φ(X, w) be smooth in w ∈ ℝ^m, with
|∂_X^β ∂_w^γ Φ| ≤ C r^(−|β|) for X near Σ̃_T and w in a compact set, and let A_i ∈ 𝒯^0 and B_i ∈ ℬ^q (q ≥ 0) with A + θB
in that compact set for θ ∈ [0, 1]. Then Φ(X, A) ∈ 𝒯^0 and Φ(X, A + B) − Φ(X, A) ∈ ℬ^q.

*Proof.* (a) and (b) are Leibniz's rule, r ≥ 1 and the definitions. (c) For tame fields take α = 0. For the strip
class, the Cartesian derivatives are combinations of ∂_v, ℓ and r⁻¹ Y_i with coefficients bounded with all their
derivatives ([[eq:cutoff-cartesian]]), and ∂_v does not lower the order while ℓ and r⁻¹ Y_i raise it. (d) By the chain
rule ∂^β Φ(X, A) is a sum of products of a derivative of Φ with derivatives of the A_i whose orders add up, with the
X-derivatives of Φ, to |β|; each derivative gains r⁻¹. And Φ(X, A + B) − Φ(X, A) = Σ_i B_i ∫_0^1 ∂_(w_i) Φ(X, A + θB) dθ,
whose integrand is in ℰ by the chain rule, and ℰ ℬ^q ⊂ ℬ^q. ∎

**Lemma {#lem:cutoff-jets}** (the time derivatives at the initial slice). Let T ≤ T_0. Then δ = ∂δ = 0 on Σ̃_T, and for
2 ≤ |β| ≤ N_0

    |∂^β δ| ≤ C (r^(−4−|β|) + 1_(𝒮^♭_T) r^(−(J+3)/2))   on Σ̃_T,                                       {#eq:cutoff-jets}

with C depending on λ, J and N_0 but not on T. In the notation of [[def:cutoff-classes]], δ ∈ 𝒯^4 + ℬ^((J+3)/2) for
the derivatives of order at least 2.

*Proof.* *The forcing at the slice.* Put ℱ := P(H_D). We show ℱ ∈ 𝒯^6 + ℬ^((J+3)/2). First, P(H_0) is tame of order 6.
P(Σ) is: by the proof of [[prop:far-residual]] (with □_η Σ_4 = 0), P(Σ) is a finite sum of homogeneous terms of degrees
at most −6 and of Rem′, and ∂ lowers the degree of a homogeneous term by one, while ∂_a Rem′ = ς⁻¹ (∂_X Rem)′; so |∂^j
Γ^α P(Σ)| ≤ C λ r^(−6−j). And P(H_0) − P(Σ) = ∫_0^1 DP(Σ + θ Σ′_J)[Σ′_J] dθ, with DP(H)[k] = −½ g^(ab) ∂_a ∂_b k +
B(H)·∂k + C(H) k ([[prop:far-coefficients]]); g^(ab), B and C are polynomials in g^(±1), ∂g, ∂∂g, Γ̂ and ∂Γ̂, so by
Leibniz's rule, [[eq:far-sigma-bounds]] and [[lem:cutoff-extension]] (a) they are tame of orders 0, 3 and 4 for H = Σ +
θ Σ′_J, while Σ′_J is tame of order 4; each of the three terms is tame of order 6. Second, ℱ − P(H_0) = P(H_0 + M) −
P(H_0) vanishes where χ_T = 1, and on the strip it equals −½ g_M^(ab) ∂_a ∂_b M − ½ (g_M^(ab) − g_0^(ab)) ∂_a ∂_b H_0 +
N(X, H_0 + M, ∂H_0 + ∂M) − N(X, H_0, ∂H_0), with g_M := g_b0 + H_D and g_0 := g_b0 + H_0. M is of strip order (J + 1)/2,
uniformly in T, by [[lem:cutoff-extension]] (b) and the bounds on χ_T(v). As in the proof of [[lem:cutoff-polynomial]],
g_M⁻¹(dv, dv) = O(r⁻²) and every other second derivative in the first term contains ℓ, r⁻¹ Y or an O(r⁻¹) coefficient,
so the first term is of strip order (J + 3)/2; the other two contain M or ∂M times factors of strip order at least 2. By
[[lem:cutoff-classes]] (c), ℱ − P(H_0) ∈ ℬ^((J+3)/2).

*Coordinates at the slice.* Use (y, x), y := t̃ − T, on r ≥ 4R: ∂_y = ∂_t, and ∂̃_i := ∂_i + f′ x̂_i ∂_t is tangent to
the slices, so ∂_i = ∂̃_i − f′ x̂_i ∂_y with f′ x̂_i tame of order 2 (f′ ∈ |x|⁻² C^∞). The classes may therefore be
defined with ∂_y and ∂̃_i in place of ∂_t and ∂_i. Put δ_ν := ∂_y^ν δ|_(y=0), functions on Σ̃_T. The Cauchy data of g_T
and D_T agree, so δ_0 = δ_1 = 0 and every ∂̃^γ δ_0, ∂̃^γ δ_1 vanishes. We show by induction on ν ≥ 2 that

    |∂̃^γ δ_ν| ≤ C (r^(−4−ν−|γ|) + 1_(𝒮^♭_T) r^(−(J+3)/2))   for ν + |γ| ≤ N_0,                    {#eq:cutoff-induction}

which gives [[eq:cutoff-jets]], a Cartesian ∂^β at y = 0 being a combination of the ∂̃^γ δ_ν, ν + |γ| ≤ |β|, with
coefficients in ℰ that gain r⁻¹ for each order they lack.

*The equation.* P(H_D + δ) = 0, and P(H_D + δ) − P(H_D) = −½ g_δ^(ab) ∂_a ∂_b δ + e_0 δ + e_1·∂δ, with g_δ := g_b0 + H_D
+ δ = g_T, e_0 = ∫_0^1 [∂_H(−½ g^(ab)(H_D + θδ)) ∂_a ∂_b H_D + ∂_H N(X, H_D + θδ, ∂H_D + θ∂δ)] dθ and e_1 = ∫_0^1 ∂_(∂H)
N(X, H_D + θδ, ∂H_D + θ∂δ) dθ. In (y, x), g^(ab) ∂_a ∂_b = g⁻¹(dt̃, dt̃) ∂_y² + 2 g⁻¹(dt̃, dx^i) ∂_y ∂̃_i + g^(ij) ∂̃_i
∂̃_j + b^y ∂_y + b^i ∂̃_i, with b^y, b^i built from g⁻¹ and second derivatives of f(r), tame of order 3. Apply ∂_y^ν, ν
≥ 0, and restrict to y = 0, where δ = ∂δ = 0 and g_δ = g_D := g_b0 + H_D:

    −½ g_D⁻¹(dt̃, dt̃) δ_(ν+2) = −∂_y^ν ℱ|_(y=0) − ℛ_ν.                                         {#eq:cutoff-jet-equation}

By Leibniz's rule ℛ_ν is a finite sum of products, each with at least one factor ∂̃^γ δ_μ, μ ≤ ν + 1, and the other
factors further such factors or y- and tangential derivatives, at y = 0, of g⁻¹(H_D), e_0, e_1, b^y, b^i at δ = 0 and of
their derivatives in δ, ∂δ. The term δ_(ν+2) occurs only on the left: the only way to place ν + 2 derivatives ∂_y on δ
is ∂_y^ν on ∂_y² δ with the undifferentiated coefficient. At δ = 0, by [[lem:cutoff-classes]] (d) applied with A = (H_0,
∂H_0, ∂∂H_0) ∈ 𝒯^2 × 𝒯^3 × 𝒯^4 ⊂ ℰ and B = (M, ∂M, ∂∂M) ∈ ℬ^((J+1)/2), the coefficients are: g⁻¹(H_D) and b in 𝒯^0 +
ℬ^((J+1)/2), e_1 in 𝒯^3 + ℬ^((J+1)/2) (∂_(∂H) N is linear in ∂g = μ ∂m + ∂H and in Γ̂, tame of order 3), e_0 in 𝒯^4 +
ℬ^((J+1)/2) (it is linear in ∂∂g, quadratic in ∂g, Γ̂, or contains ∂Γ̂, tame of order 4). Each y- or tangential
derivative of a coefficient lowers its 𝒯-part by one more order and keeps its ℬ-part.

*The count.* Suppose [[eq:cutoff-induction]] for 2 ≤ μ ≤ ν + 1. In ∂_y^ν of g_δ^(ab) ∂_a ∂_b δ the derivatives on δ and
on the coefficients number ν + 2 in total; in ∂_y^ν (e_1·∂δ) they number ν + 1 and e_1 brings the order 3; in
∂_y^ν (e_0 δ) they number ν and e_0 brings 4; a factor ∂̃^γ δ_μ counts μ + |γ| and has 𝒯-order 4 + μ + |γ|. So the
𝒯-part of each product of ℛ_ν is at most C r^(−4−(ν+2)), every further factor δ only lowering it. A product with a
ℬ-factor has either a factor ∂̃^γ δ_μ in ℬ^((J+3)/2) and the others in ℰ, or a coefficient in ℬ^((J+1)/2) and a factor
∂̃^γ δ_μ with μ ≥ 2 in 𝒯^6 + ℬ^((J+3)/2); in both cases it is at most C r^(−(J+3)/2) and vanishes off 𝒮^♭_T. Also
∂_y^ν ℱ|_(y=0) ∈ 𝒯^(6+ν) + ℬ^((J+3)/2). Finally g_D⁻¹(dt̃, dt̃) ≤ −0.64 by [[lem:own-margins]] (b), since
|g_D⁻¹ − g_b0⁻¹| ≤ C(λ r⁻² + C(λ, J) r⁻⁴) ≤ 0.0232 on Σ̃_T for T ≤ T_0, and 1/g_D⁻¹(dt̃, dt̃) ∈ 𝒯^0 + ℬ^((J+1)/2) by
[[lem:cutoff-classes]] (d). So [[eq:cutoff-jet-equation]] gives [[eq:cutoff-induction]] for δ_(ν+2) at γ = 0; applying
∂̃^γ to [[eq:cutoff-jet-equation]], which holds on Σ̃_T, and counting in the same way gives it for every γ. ∎

**Proposition {#prop:cutoff-cap}** (the initial slice). Let T ≤ T_0 and k ≥ 0. On Σ̃_T, for |α| ≤ k,

    |Γ^α h_R| ≤ C (r⁻⁴ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),     |∂Γ^α h_R| ≤ C (r⁻⁵ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),
                                                                            {#eq:cutoff-cap-general}

with C depending on λ, J and k but not on T. If J ≥ 2k + 7, then |Γ^α h_R| ≤ C r⁻⁴ and |∂Γ^α h_R| ≤ C r⁻⁵ on all of
Σ̃_T, and for 0 < a < 3

    E_T[Γ^α h_R] ≤ C |T|^(2a−6)  (|α| ≤ k),     𝔈_k(T) ≤ C |T|^(2a−6).                                   {#eq:cutoff-cap}

On Σ̃_T ∩ {v ≤ V_T}, h_R = g_λ − g_b0 − Σ; on Σ̃_T ∩ {v ≥ V_T + δ_0/4}, h_R = Σ′_J and ∂_t h_R = ∂_t Σ′_J there, and
there |∂^β (h_R − Σ′_J)| ≤ C r^(−4−|β|) for |β| ≥ 2.

*Proof.* By [[eq:cutoff-hd]], h_R = Σ′_J + M + δ near Σ̃_T. Each Γ is ∂_t, x_i ∂_j − x_j ∂_i or (t − v1) ∂_t + x^i ∂_i
(on Cartesian components, L_Ω differs from Ω by a constant matrix), so by induction Γ^α = Σ_(|β|≤|α|) c_(α,β) ∂^β with
c_(α,β) a polynomial in (t − v1, x) of degree at most |β|: Γ(c ∂^β) = (Γc) ∂^β + c Γ∂^β, and Γ does not raise the
degree of c and raises the order and the degree by one together. On W, |t − v1| ≤ r ([[lem:own-wedge]] (b)) and
|x| = r, so |c_(α,β)| ≤ C r^(|β|) and |∂c_(α,β)| ≤ C r^(|β|−1). By [[lem:cutoff-extension]] (a), |Γ^α Σ′_J| ≤ C r⁻⁴ and
|∂Γ^α Σ′_J| ≤ C r⁻⁵. In (v, r, x̂), ∂_t = ∂_v and Z = (v − v1) ∂_v + r ℓ, with v − v1 ≤ d_V on the strip; so Γ^α M is of
strip order (J + 1)/2 and |Γ^α M| + |∂Γ^α M| ≤ C r^(−(J+1)/2) ≤ C r⁻⁵, as J ≥ 9; and M vanishes off 𝒮^♭_T. By
[[lem:cutoff-jets]], since δ and ∂δ vanish on Σ̃_T,

    |Γ^α δ| ≤ C Σ_(2≤|β|≤|α|) r^(|β|) (r^(−4−|β|) + 1_(𝒮^♭_T) r^(−(J+3)/2)) ≤ C (r⁻⁴ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),

and ∂Γ^α δ = Σ_β ((∂c_(α,β)) ∂^β δ + c_(α,β) ∂∂^β δ) gives the bound with r⁻⁵. This is [[eq:cutoff-cap-general]]. If
J ≥ 2k + 7, then r^(|α|−(J+3)/2) ≤ r⁻⁵ for |α| ≤ k. On Σ̃_T, |H| = |Σ + Σ′_J + M| ≤ 1/50 for T ≤ T_0, so by
[[lem:own-margins]] (d) and w ≤ C r^(2a), E_T[φ] ≤ C ∫_(Σ̃_T) r^(2a) |∂φ|² d⁴x; with d⁴x = r³ dr dω along the rays,
E_T[Γ^α h_R] ≤ C ∫_(r_T)^∞ r^(2a−10+3) dr = C r_T^(2a−6)/(6 − 2a) ≤ C |T|^(2a−6), as r_T ≥ c_W (1 + |T|). The last
statement: χ_T = 0 on {v ≤ V_T}, where D_T = g_λ and δ = 0 near Σ̃_T ([[lem:own-truncation]] (ii)); χ_T = 1 and M = 0
on {v ≥ V_T + δ_0/4}, where δ, ∂δ vanish and [[eq:cutoff-jets]] holds without the strip term. ∎

**Remark {#rem:cutoff-growth}** (the order of the matching). The condition J ≥ 2k + 7 is what the commuted fields need.
If the data beyond the band were those of g_b0 + Σ, that is with Σ′_J replaced by 0, the mismatch on the band would be
(1 − χ_T) h_λ, h_λ := g_λ − g_b0 − Σ, of strip order 9/2 only: by [[lem:cutoff-polynomial]] the coefficient of r^(−9/2)
of h_λ is G_(9,0), of weight −9/2 and constant in v, and the rest is of strip order 5. Since P(Σ + h_λ) = 0, the forcing
at the slice is ℱ = P(Σ + h_λ − χ_T h_λ) = χ_T′(v)(ℓ + 3/(2r)) h_λ + O(r⁻⁶) = −3 χ_T′(v) r^(−11/2) G_(9,0) + O(r⁻⁶) on
the band, and by [[eq:cutoff-jet-equation]] δ_2 = 2ℱ/g_D⁻¹(dt̃, dt̃) and δ_3 = −6 χ_T″(v) r^(−11/2) G_(9,0)/g_D⁻¹(dt̃,
dt̃) + O(r⁻⁶): a derivative ∂_y falls on χ_T without gain. In (y, r, x̂), Z = (y + T + β_f) ∂_y + r ∂_r with ∂_r at
fixed (y, x̂) and β_f := f − v1 − r f′ bounded, and ∂_r v = 1 + f′ there. So at y = 0, ∂_y Z² δ = ((T + β_f)² + 2 (T +
β_f) r (1 + f′)) δ_3 + O(|T| r^(−11/2) + T² r⁻⁶), and the bracket is −T² + O(|T|) on the band, where r = |T| + O(1).
Hence |∂_y Z² h_R| ≥ c T² r^(−11/2) where |χ_T″| and |G_(9,0)| are bounded below, and E_T[Z² h_R] ≥ c |T|^(2a−4) when
G_(9,0) ≢ 0, which is unbounded as T → −∞ for every a > 2; with k factors Z the order is |T|^(2a+2k−8). In general a
mismatch of strip order q gives E_T[Γ^α h_R] up to C |T|^(2a+2|α|−2q+1), and [[prop:cutoff-cap]] uses q = (J + 1)/2.

### The continuation with the matched truncation {#sec:cutoff-continuation}

**Lemma {#lem:cutoff-gauge}** (the gauge field on the initial slice). For T ≤ T_0, the field D_T := D(g_T) of the proof
of [[prop:own-vacuum]] satisfies on Σ̃_T: D_T = 0 on {v ≤ V_T}; |D_T| + |∂D_T| ≤ C r⁻⁵ on 𝒮^♭_T ∩ {v ≥ V_T};
|D_T| ≤ C λ r⁻³ + C r⁻⁵ and |∂D_T| ≤ C λ r⁻⁴ + C r⁻⁶ on {v ≥ V_T + δ_0/4}, the constants C depending on λ and J. Its
energy of weight 1 on Σ̃_T is at most C λ² |T|⁻² + C |T|⁻⁴.

*Proof.* D(g) is linear in ∂(g − g_b0) with coefficients in g⁻¹, plus terms (g⁻¹ − g_b0⁻¹)Γ̂, so
|D(g_b0 + H)| ≤ C(|∂H| + r⁻³ |H|), and ∂D(g) involves ∂²g linearly. On Σ̃_T, g_T and ∂g_T are those of D_T, and
∂²g_T = ∂² D_T + ∂²δ. On {v ≤ V_T}, D_T = D(g_λ) = 0 near Σ̃_T ([[thm:past-construction]]). On the strip,
H_D = (g_λ − g_b0) − χ_T m_J, so D(g_b0 + H_D) = D(g_λ) + O(r^(−(J+1)/2)) = O(r^(−(J+1)/2)), its derivative likewise,
and |∂²δ| ≤ C r^(−(J+3)/2) + C r⁻⁶ by [[lem:cutoff-jets]]; as J ≥ 9 this is O(r⁻⁵). Beyond the band H_D = Σ + Σ′_J;
D(g_b0 + Σ) = O(λ r⁻³) with ∂D(g_b0 + Σ) = O(λ r⁻⁴) (homogeneity, as in the proof of [[prop:own-vacuum]]), the terms of
Σ′_J add O(r⁻⁵) and O(r⁻⁶), and |∂²δ| ≤ C r⁻⁶. With w = (u* − u)² ≤ C r² and d⁴x = r³ dr dω, the energy is at most
C ∫_(r_T)^∞ r² (λ² r⁻⁸ + r⁻¹⁰) r³ dr + C r_T^(2+3) r_T^(−10) d_V ≤ C λ² |T|⁻² + C |T|⁻⁴. ∎

**Lemma {#lem:cutoff-independence}** (the limit does not depend on J). Suppose the conclusions of
[[thm:own-continuation]] hold for the truncated problems of [[def:cutoff-truncation]] with two values J, J′ ≥ 2k1 + 7,
with limits g^(J) and g^(J′). Then g^(J) = g^(J′).

*Proof.* g′ := g^(J′) satisfies the hypotheses of [[prop:own-uniqueness]] relative to g := g^(J): Ric^H(g′; g_b0) = 0,
g′ = g_λ on N with its first derivatives (it joins g_λ smoothly across N), |g′ − g_b0| ≤ 1/50 (Step 1 of the proof of
[[thm:own-continuation]]), and for a_0 ∈ (0, ½) its energies of weight a_0 of Γ^α h′, |α| ≤ 3, are bounded uniformly in
σ and tend to 0 as σ → −∞: those of h_R are dominated by those of weight a, as u* − u ≥ 1 on W, and those of Σ are
at most C λ² r_σ^(2a_0−2), as in the proof of [[prop:own-uniqueness]]. The proof of [[prop:own-uniqueness]] uses of g
only [[eq:own-pointwise]] and its energies, which g^(J) has. So g^(J′) = g^(J). ∎

**Proposition {#prop:cutoff-continuation}** (the continuation). With the truncated problems of [[def:cutoff-truncation]],
[[thm:own-continuation]] holds as stated, with T_1 depending on λ and J; λ_2, ε_2 and ε_B do not depend on J, and the
limit g does not depend on J. The proof of [[thm:own-continuation]] applies with the following changes, all of which
concern the initial slice Σ̃_T.
(1) In Step 1, beyond the band Γ^β h_R(T, x) = O(r⁻⁴) for |β| ≤ k1 − 3 ([[prop:cutoff-cap]]), which tends to 0 along
Σ̃_σ as before.
(2) In Step 3, by [[prop:cutoff-cap]] with k = k1 and J ≥ 2k1 + 7, 𝔈_(k1)(T) ≤ C(λ, J) |T|^(2a−6), which is at most λ²
for T ≤ T_1(λ, J), as a < 3. Put ε_B² := C_* (C(λ² + ν(λ)) + 2λ²). Then 𝔈_(k1) ≤ ε_B² on [T, σ*], the rest of Step 3
being unchanged.
(3) In Step 4, at order k > k1 the cap 𝔈_k(T) ≤ C(λ, J) |T|^(2a−6) is uniform in T when J ≥ 2k + 7. For every k take
J ≥ 2k + 7; by [[lem:cutoff-independence]] the limit is the same g, which therefore has 𝔈_k ≤ C_k(λ) for every k.
(4) In Step 5, the cap of the problem at T′ is at most C(λ, J) |T′|^(2a−6) and ϑ(T) → 0 as before.
(5) In the proof of [[lem:own-exterior]], the data on Σ̃_T ∩ {r ≥ ϱ_0}, which lies beyond the band, satisfy
|Γ^α h_R| ≤ C r⁻⁴ and |∂Γ^α h_R| ≤ C r⁻⁵ for |α| ≤ k when J ≥ 2k + 7, and are finite at every order for every J by
[[eq:cutoff-cap-general]], the strip having bounded width.
(6) In the proof of [[prop:own-vacuum]] (ii), the values of D_T on Σ̃_T are those of [[lem:cutoff-gauge]], and
E_σ[D_T] ≤ C(λ² |T|⁻² + C(λ, J) |T|⁻⁴) for σ ∈ [T, 0], which tends to 0 as T → −∞.
With these, [[prop:own-vacuum]], [[prop:own-uniqueness]], [[prop:own-transfer]] and [[thm:own-data]] hold as stated.

*Proof.* (1)–(6) are [[prop:cutoff-cap]], [[lem:cutoff-gauge]] and [[lem:cutoff-independence]] inserted at the places
named. The choice of ε_B in (2) does not involve the cap, so neither ε_B nor the thresholds λ_2, ε_2 of Step 3 depend on
J; only T_1 does. The equation of h_R, its forcing Π_i (Γ_i + c_i) P(Σ), the fluxes through N and the kernels are those
of [[thm:own-continuation]]: Σ′_J enters the data on Σ̃_T only. ∎
