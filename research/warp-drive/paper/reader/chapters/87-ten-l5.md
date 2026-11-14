## At the prescribed wavelength 10 l5 {#ch:ten-l5}

[[thm:main]] is a statement for small λ. This chapter treats the problem at the prescribed wavelength λ = 10 l5, at
two seeds, with the envelope sin⁴(π(v − 1/2)/3) on [1/2, 7/2]. That envelope is C³ and not C⁴, so [[thm:main]] does
not apply to it at any λ ([[rem:envelope-regularity]]); for the smooth envelope of [[def:lambda0-point]], whose
parameters are those of the first seed below, the threshold λ0 that the proof of [[thm:main]] delivers lies below
0.0024433 in the operator norm ([[prop:lambda0]]), and 10 l5 exceeds it by a factor above 409. At 10 l5 the wavelength
is not small against the curvature length ([[prop:tl5-scales]]), and the problem is posed as a characteristic initial
value problem in double-null gauge: the seed on an ingoing cone, the incoming wave on an outgoing one.

The chapter proves the following. The problem has a solution where the solution is the seed ([[thm:ten-l5]]). Wherever
a vacuum solution exists in the gauge with the seed's transverse derivative of R on the seed's cone, its leaves inside
the seed's horizon generator are outer trapped, and its T²-invariant marginally outer trapped sections lie at or outside
that generator and, under a condition on the generators through them, in an explicit band ([[prop:tl5-leaves]],
[[cor:tl5-mots]]). On the data cone the outgoing constraint has exact solutions, and an explicit approximant satisfies
it up to an explicit residual ([[sec:cone-approximant]]). Two explicit metrics of the class on a region beyond the seed
have explicit residual bounds ([[sec:tl5-residuals]]). A continuation lemma states what existence beyond the seed would
need ([[lem:tl5-continuation]]). No existence is proved beyond the seed, and [[rem:tl5-beyond]] says why. Numerical
observations, which no proof uses, are kept as remarks.

### The seeds and the scales {#sec:tl5-scales}

**Definition {#def:tl5-seeds}** (The two seeds.) Fix l5 > 0 and the wavelength λ := 10 l5. The first seed is the
five-dimensional Schwarzschild–Tangherlini metric of mass μ0 = 100 l5², the second that of mass μ0 = 1000 l5². Lengths
are measured in units of the horizon radius r_h := √μ0, so that μ0 = 1 and f(r) := 1 − r⁻²; then l5 = 1/10 and λ = 1
at the first seed, and l5 = 1000^(−1/2) and λ = 10^(−1/2) at the second. The envelope is env(v) := sin⁴(π(v − 1/2)/3)
for 1/2 < v < 7/2 and env(v) := 0 otherwise, with amplitude A = 1. The first seed has the μ0 and l5 of
[[def:lambda0-point]].

**Proposition {#prop:tl5-scales}** (No separation of scales.) Let 𝒦 = 72 μ0²/r⁸ be the Kretschmann scalar of the seed
([[prop:vaidya]] (b)) and L := 𝒦^(−1/4) its curvature length. At both seeds λ/L = 10 on x_K = 1, that is at
r = r_q := (√72 μ0 l5²)^(1/4). At the horizon r = √μ0,

    λ/L = 72^(1/4) ∈ (2.912, 2.913)  (first seed),      λ/L = (72/100)^(1/4) ∈ (0.9211, 0.9212)  (second seed).

Against the areal radius, λ/r = 1 and λ/r = 10^(−1/2) ∈ (0.3162, 0.3163) at the horizon, and on x_K = 1

    λ/r_q = 10^(1/2) 72^(−1/8) ∈ (1.852, 1.853)  (first seed),
    λ/r_q = 10 · 72^(−1/8) 1000^(−1/4) ∈ (1.041, 1.042)  (second seed).

*Proof.* On x_K = 1, l5² √𝒦 = 1 by the definition of x_K ([[ch:setting]]), so L = l5 and λ/L = 10. At r = √μ0,
𝒦 = 72/μ0² and L = √μ0 · 72^(−1/4), so λ/L = 10 l5 · 72^(1/4)/√μ0; this is 72^(1/4) when √μ0 = 10 l5 and
72^(1/4)/√10 = (72/100)^(1/4) when √μ0 = √1000 l5. Likewise λ/√μ0 = 10 l5/√μ0 is 1 and 10^(−1/2). On x_K = 1,
r_q⁸ = 72 μ0² l5⁴, so (λ/r_q)⁸ = 10⁸ l5⁴/(72 μ0²), which is 10⁴/72 at the first seed and 10²/72 at the second. The
bounds follow from 2.912⁴ < 72 < 2.913⁴, 0.9211⁴ < 0.72 < 0.9212⁴, 0.3162² < 0.1 < 0.3163², 1.852⁸ < 10⁴/72 < 1.853⁸
and 1.041⁸ < 10²/72 < 1.042⁸. ∎

So the expansion parameter of a high-frequency theorem, the wavelength over the curvature length, is 10 on x_K = 1 and
of order one at the horizon. The statement of [[sec:main-statement]] that the waves are high-frequency on D_T once
λ < l5/10 concerns the approximant, not the threshold λ0. Against the scale r on which the curvature varies the ratio
is of order one as well; that is the parameter a construction from waves exact on a locally linear background, in the
manner of [AB26, Section 3.1], would see, and there the wavelengths are chosen, while here λ is prescribed.

**Remark {#rem:tl5-bondi-scheme}** (Numerical observation.) A numerical scheme in the Bondi chart, which evolves
ingoing null slices from a timelike excision boundary inside x_K = 1 and whose premise is that the outgoing expansion of
the round spheres has one zero on each column and that the boundary is outflow, was run at λ = 10 l5 at both seeds. The
premise fails before the peak of the shell: a second zero holds over 0.04 in v from v = 1.50 at the first seed (1.496
on a finer grid) and from v = 1.583 at the second (three grids agreeing to 0.0005), and the boundary ceases to be
outflow within 0.1 after; deeper excisions, at r = 0.39 and 0.25 at the first seed and at r = 0.21 at the second, fail
earlier. Up to the failure the growth factor of the radiation field, the exponential of the integral in v of the largest
v-derivative of its two polarizations, is 1.9 and 2.1, and a finite-difference amplification of the data along one
direction, a lower bound for the norm of the propagator, is 1.28 and 1.00; at λ = l5 at the first seed, where the scheme
completes, they are 6.9 and 1.71, while the sup-norm Grönwall factor is 17, 2 × 10⁵ and 6 × 10³ in the three cases.
These breakdown times were measured at one angular resolution; at its own time step the scheme is unstable in angle at
the two finer angular resolutions tried, on the seed itself, before the wave arrives. No approximant on D_T comes from
that scheme at 10 l5, and no proof uses these observations.

### The data cone: an explicit approximant and exact data {#sec:cone-approximant}

This section concerns the characteristic data on the outgoing cone u = −10 at the two seeds of [[def:tl5-seeds]], whose
wavelength parameters are λ = 1 (the first seed) and λ = 1/√10 (the second seed). On this cone the Raychaudhuri
constraint determines the areal radius R from the other data. We prove two things. First, an explicit approximant
R_app, a tensor Chebyshev series with the coefficients of [[sec:cone-tables]], satisfies the constraint
up to an explicit residual ([[prop:cone-residual]]). Second, the constraint has an exact solution on every generator,
positive and within an explicit distance of the Tangherlini radius ([[prop:cone-exact]]); the approximant equals it
for v ≤ 1/2, lies within 10⁻⁶ of it for 1/2 ≤ v ≤ 7/2, and departs from it at most linearly in r beyond
([[cor:cone-compare]]).

### The constraint on the data cone {#sec:cone-constraint}

The metrics of the class are written in double-null gauge as

    g = −4 e^(2W) du dv + G_x (dx − β du)² + R² ((1 + x)/2) e^(2P) dφ1² + R² ((1 − x)/2) e^(2Q) dφ2²,
    G_x = R² e^(−2(P + Q))/(4(1 − x²)),

with R > 0, P, Q, W and β functions of (u, v, x), and x ∈ [−1, 1]. The choice of G_x is the gauge: the leaves
u = const, v = const carry the volume element (R³/4) dx dφ1 dφ2.

**Lemma {#lem:cone-raychaudhuri}** (The outgoing constraint.) For every metric of the class, at every point
with |x| < 1,

    Ric_vv = −(3/R) (∂_v²R − 2 ∂_vW ∂_vR) − ((∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)²).          {#eq:cone-raychaudhuri}

*Proof.* Write (y¹, y², y³) := (x, φ1, φ2), let γ be the diagonal matrix with entries γ₁₁ := G_x,
γ₂₂ := R² ((1 + x)/2) e^(2P) and γ₃₃ := R² ((1 − x)/2) e^(2Q), and put β¹ := β and β² = β³ := 0, so that
g = −4 e^(2W) du dv + γ_AB (dy^A − β^A du)(dy^B − β^B du), indices A, B, C running over 1, 2, 3. Then
g_vv = g_vA = 0 and g_uv = −2 e^(2W). The inverse metric has g^(uu) = g^(uA) = 0, g^(uv) = −e^(−2W)/2 and
g^(AB) = γ^(AB), and det g = −4 e^(4W) det γ, since in the coframe (du, dv, dy^A − β^A du), whose determinant
against (du, dv, dy^A) is 1, the metric is block diagonal. For the Christoffel symbols of g, with indices μ, ν
running over u, v, y¹, y², y³, this gives

    Γ^μ_vv = g^(μu) ∂_v g_uv,  so  Γ^v_vv = 2 ∂_vW  and  Γ^u_vv = Γ^A_vv = 0;
    Γ^u_vν = (1/2) g^(uv) ∂_ν g_vv = 0;      Γ^A_vB = (1/2) γ^(AC) ∂_vγ_CB =: χ^A_B;
    Γ^μ_μv = ∂_v ln |det g|^(1/2) = 2 ∂_vW + (1/2) ∂_v ln det γ,

where every other term of Γ^A_vB contains g^(Au) = 0 or a derivative of g_vv or of g_vC, which vanish. In
Ric_vv = ∂_μΓ^μ_vv − ∂_vΓ^μ_vμ + Γ^μ_μν Γ^ν_vv − Γ^μ_vν Γ^ν_vμ, the last sum has no term with μ = u or ν = u, and
Γ^A_vv = 0 reduces it to (Γ^v_vv)² + χ^A_B χ^B_A. So

    Ric_vv = ∂_v(2∂_vW) − ∂_v(2∂_vW + (1/2) ∂_v ln det γ) + 2∂_vW (2∂_vW + (1/2) ∂_v ln det γ) − 4 (∂_vW)²
             − χ^A_B χ^B_A
           = −(1/2) ∂_v² ln det γ + ∂_vW ∂_v ln det γ − χ^A_B χ^B_A.

In the gauge, det γ = R⁶/16, so ∂_v ln det γ = 6 ∂_vR/R and ∂_v² ln det γ = 6 ∂_v²R/R − 6 (∂_vR/R)². The matrix χ
is diagonal with entries (1/2) ∂_v ln γ_AA, namely ρ − ∂_vP − ∂_vQ, ρ + ∂_vP and ρ + ∂_vQ, where ρ := ∂_vR/R; so
χ^A_B χ^B_A = 3ρ² + (∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)². Substituting gives [[eq:cone-raychaudhuri]]. ∎

The right side of [[eq:cone-raychaudhuri]] contains no shift and no derivative in x, and so is determined by the data
(R, P, Q, W) on an outgoing cone u = const. For such data, given for x ∈ [−1, 1], Ric_vv[R] denotes the right side
of [[eq:cone-raychaudhuri]], also at x = ±1.

Put f(r) := 1 − r^(−2). Along the cone u = −10 the Tangherlini areal radius r ∈ [10, ∞) is a parameter on each
generator, related to v by

    v(r) = 2(r − 10) + ln(11(r − 1)/(9(r + 1))),        v′(r) = 2 + 2/(r² − 1) = 2/f(r),                {#eq:cone-v}

so v(10) = 0 and dr/dv = f/2. Let r_s < r_e be the solutions of v(r_s) = 1/2 and v(r_e) = 7/2 (v is increasing);
r_s = 10.2475603901…, r_e = 11.7350863591…. The data on the cone are W = (1/2) ln(f(r)/(2 f(10))) and

    m = h(x) φ(r) cos θ(r),     n = h(x) φ(r) sin θ(r),     h(x) = (2/(1 + x²))^(1/2),
    φ(r) = (λ/2) r^(−3/2) env(v(r)),     θ(r) = v(r)/λ,
    P = (2(1 + x) m − (1 − x) n)/3,     Q = (2(1 − x) n − (1 + x) m)/3,                               {#eq:cone-data}

where env(v) = sin⁴(π(v − 1/2)/3) for 1/2 < v < 7/2 and env(v) = 0 otherwise. The function env is C³, so φ is C³ in
r, and φ = φ′ = 0 for r ∉ (r_s, r_e): there the data are those of Tangherlini. R is the unknown.

This envelope, the one of the two seeds of [[def:tl5-seeds]], is C³ and not C⁴ at v = 1/2 and v = 7/2, so it is not an
envelope of [[thm:main]], and nothing in this section uses [[thm:main]]. The constraint on a generator needs only
φ ∈ C¹ with φ = φ′ = 0 outside (r_s, r_e). [[lem:cone-ellipse]] uses that on [r_s, r_e] env is the restriction of
an entire function; the smooth envelope of [[lem:envelope-constant]] is not, since it has essential singularities at
v = 1/2 and v = 7/2.

**Lemma {#lem:cone-generator}** (The constraint on a generator.) Let A := (φ cos θ)′ and B := (φ sin θ)′, the prime
denoting d/dr, and

    w(r, x) := (4/(9(1 + x²))) H(r, x),      H := (1 + x)² A² − (1 − x²) A B + (1 − x)² B².                {#eq:cone-w}

Then s := (∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)² = (3f²/4) w, w vanishes for r ∉ (r_s, r_e), and for R(·, x) of class C²
in r and nonzero,

    Ric_vv[R] = −(3f²/(4R)) (∂_r²R + w R).                                                               {#eq:cone-ricvv}

*Proof.* Since dr/dv = f/2 and f′ = 2r^(−3), ∂_vR = (f/2) ∂_rR and ∂_v²R = (f/2)² ∂_r²R + (f/(2r³)) ∂_rR, while
∂_vW = (f/2) f′/(2f) = 1/(2r³). Hence ∂_v²R − 2 ∂_vW ∂_vR = (f/2)² ∂_r²R. Next, ∂_r m = h A and ∂_r n = h B. With
a := (1 + x) A and b := (1 − x) B,

    ∂_vP = (f h/6)(2a − b),     ∂_vQ = (f h/6)(2b − a),     ∂_vP + ∂_vQ = (f h/6)(a + b),

and (2a − b)² + (2b − a)² + (a + b)² = 6(a² − ab + b²). So s = (f² h²/6)(a² − ab + b²) = (f²/(3(1 + x²))) H =
(3f²/4) w. Substituting both in [[eq:cone-raychaudhuri]] gives [[eq:cone-ricvv]]. Outside (r_s, r_e), φ = φ′ = 0, so
A = B = 0 and w = 0. ∎

So on each generator the constraint Ric_vv = 0 is the linear equation ∂_r²R = −w R, that is
∂_r²R = −(4/(3f²)) R s.

**Lemma {#lem:cone-w}** (The size of w.) On [r_s, r_e] × [−1, 1], A² + B² = φ′² + φ² θ′² and

    0 ≤ w ≤ (8/9)(A² + B²) ≤ W̄,      s ≤ s̄,

with W̄ = 1.99 × 10⁻³ and s̄ = 1.46 × 10⁻³ at the first seed, and W̄ = 8.55 × 10⁻⁴ and s̄ = 6.3 × 10⁻⁴ at the second.

*Proof.* Expanding,

    H = (1 + x²)(A² + B²) + A B (x² − 1) + 2(A² − B²) x.

By the Cauchy–Schwarz inequality, |A B (x² − 1) + 2(A² − B²) x| ≤ (A²B² + (A² − B²)²)^(1/2) ((x² − 1)² + 4x²)^(1/2),
and A²B² + (A² − B²)² ≤ 4A²B² + (A² − B²)² = (A² + B²)², (x² − 1)² + 4x² = (1 + x²)². Hence
0 ≤ H ≤ 2(1 + x²)(A² + B²), which is the first claim. Next, A + iB = (φ e^(iθ))′ = (φ′ + iφθ′) e^(iθ), so
A² + B² = φ′² + φ²θ′². Write σ := sin(π(v − 1/2)/3) and κ := cos(π(v − 1/2)/3), so env = σ⁴ and
d env/dv = (4π/3) σ³ κ. With v′ = 2/f,

    φ θ′ = r^(−3/2) σ⁴/f,      φ′ = λ r^(−3/2) σ³ ((4π/3) κ/f − 3σ/(4r)),
    A² + B² = r^(−3) f^(−2) σ⁶ (σ² + λ² ((4π/3) κ − 3fσ/(4r))²).

On [r_s, r_e] we have 0 ≤ σ ≤ 1, |κ| = (1 − σ²)^(1/2), 3f/(4r) ≤ 3/(4r_s) ≤ β := 0.0732, and r^(−3) f^(−2) =
r/(r² − 1)² is decreasing, so r^(−3) f^(−2) ≤ r_s/(r_s² − 1)² ≤ 9.473 × 10⁻⁴. With y := σ² ∈ [0, 1] and a := 4π/3
(a² = 16π²/9 = 17.5460…),

    σ⁶ (σ² + λ² (aκ − 3fσ/(4r))²) ≤ g(y) := y⁴ + λ² y³ (a (1 − y)^(1/2) + β)².

The function y³ (1 − y)^(1/2) has its maximum on [0, 1] at y = 6/7, equal to 216/(343 √7) ≤ 0.23803. At the first
seed, g(y) = α y³ − γ y⁴ + 2aβ y³ (1 − y)^(1/2) with α := a² + β² and γ := a² − 1; the polynomial α y³ − γ y⁴ has
its maximum on [0, ∞) at y = 3α/(4γ), equal to 27α⁴/(256γ³) ≤ 2.2097. So g ≤ 2.2097 + 2aβ (0.23803) ≤ 2.3557 and
w ≤ (8/9)(9.473 × 10⁻⁴)(2.3557) ≤ 1.99 × 10⁻³. At the second seed, λ² = 1/10 and the polynomial part of g is
(1 − a²/10) y⁴ + ((a² + β²)/10) y³, whose derivative y² (4(1 − a²/10) y + 3(a² + β²)/10) is positive on (0, 1]
because 1 − a²/10 < 0 and 4(1 − a²/10) + 3(a² + β²)/10 ≥ 4 − a²/10 > 0. So the polynomial part is at most its value
1 + β²/10 at y = 1, g ≤ 1 + β²/10 + (2aβ/10)(0.23803) ≤ 1.0152, and w ≤ (8/9)(9.473 × 10⁻⁴)(1.0152) ≤ 8.55 × 10⁻⁴.
Finally s = (3f²/4) w ≤ (2f²/3)(A² + B²) = (2/3) r^(−3) σ⁶ (σ² + λ² (aκ − 3fσ/(4r))²) ≤ (2/3) r_s^(−3) g, with
r_s^(−3) ≤ 9.294 × 10⁻⁴; this gives s̄. ∎

### The approximant {#sec:cone-approximant-def}

T_k denotes the Chebyshev polynomial of degree k, T_k(cos ψ) = cos(kψ).

**Definition {#def:cone-approximant}** (The approximant.) Let N_r := 40 at the first seed and N_r := 64 at the
second, c := (r_s + r_e)/2, ℓ := (r_e − r_s)/2 and t := (r − c)/ℓ, so that t ∈ [−1, 1] for r ∈ [r_s, r_e]. Let
C_(ij), 0 ≤ i ≤ N_r, 0 ≤ j ≤ 28, be the decimal numbers of [[sec:cone-table-c1]] (first seed) and
[[sec:cone-table-c2]] (second seed), and

    S(r, x) := Σ_(i=0)^(N_r) Σ_(j=0)^(28) C_(ij) T_i(t) T_j(x),    a(x) := r_s − S(r_s, x),    b(x) := 1 − ∂_rS(r_s, x).

The approximant is

               ⎧ r                                                  for 10 ≤ r ≤ r_s,
    R_app :=   ⎨ S(r, x) + a(x) + b(x)(r − r_s)                     for r_s ≤ r ≤ r_e,
               ⎩ R_app(r_e, x) + (∂_rS(r_e, x) + b(x))(r − r_e)     for r ≥ r_e,             {#eq:cone-approximant}

and g_app denotes the data (R_app, P, Q, W) on the cone.

Since T_i(−1) = (−1)^i and T_i′(−1) = (−1)^(i−1) i², the corrections are a(x) = Σ_j a_j T_j(x) and
b(x) = Σ_j b_j T_j(x) with

    a_j = r_s δ_(j0) − Σ_i (−1)^i C_(ij),      b_j = δ_(j0) − ℓ^(−1) Σ_i (−1)^(i−1) i² C_(ij),

δ_(j0) the Kronecker symbol. By construction R_app is C¹ in r: both formulas at r_s give the value r_s and the slope
1, and the last line continues the middle one to first order at r_e. Moreover ∂_r²R_app = 0 for r ∉ [r_s, r_e] and
∂_r²R_app = ∂_r²S = ℓ^(−2) ∂_t²S on (r_s, r_e). The approximant has 41 × 29 = 1,189 coefficients at the first seed and
65 × 29 = 1,885 at the second.

**Proposition {#prop:cone-residual}** (The residual of the approximant.) At each seed:

(a) Ric_vv[g_app] = 0 on the cone outside 1/2 ≤ v ≤ 7/2.

(b) For 1/2 ≤ v ≤ 7/2 and x ∈ [−1, 1] (one-sided at v = 1/2 and
v = 7/2), |Ric_vv[g_app]| ≤ 4.97 × 10⁻⁵ at the first seed and |Ric_vv[g_app]| ≤ 2.28 × 10⁻⁵ at the second.

(c) The jumps of ∂_r²R_app across v = 1/2 and across v = 7/2 are at most 3.6 × 10⁻⁸ at the first seed and at most
8.5 × 10⁻⁸ at the second.

The proof occupies the next section. It bounds the residual of the linear equation by its values at the nodes of a
Chebyshev grid: in x it uses that the residual, multiplied by 1 + x², is a polynomial of degree 30; in r it uses that
the polynomial part is reproduced exactly by interpolation and that the rest is holomorphic on an explicit ellipse.

### Proof of the residual bound {#sec:cone-residual-proof}

On [r_s, r_e] × [−1, 1] put

    ℰ := ∂_r²R_app + w R_app,      G := (1 + x²) ℰ = (1 + x²) ℓ^(−2) ∂_t²S + F,      F := (4/9) H R_app,   {#eq:cone-g}

with H as in [[eq:cone-w]]. By [[lem:cone-generator]], Ric_vv[g_app] = −(3f²/(4R_app)) ℰ wherever R_app ≠ 0.

**Lemma {#lem:cone-structure}** (Structure of G.) (a) For each r ∈ [r_s, r_e], G(r, ·) is a polynomial of degree at
most 30. (b) For each x ∈ [−1, 1], (1 + x²) ℓ^(−2) ∂_t²S is a polynomial in t of degree at most N_r − 2, and H and
F are the restrictions to t ∈ [−1, 1] of functions holomorphic in t on the set {t : Re(c + ℓt) > 1}.

*Proof.* (a) S is a polynomial of degree 28 in x, hence so are ∂_t²S, a, b and R_app(r, ·); H is a polynomial of
degree 2 in x. (b) The first statement is clear. For the second, r ↦ v(r) extends holomorphically to Re r > 1 as
2(r − 10) + ln(11/9) + Log(r − 1) − Log(r + 1), Log the principal branch; r^(−3/2) extends as the principal branch on
Re r > 0; on [r_s, r_e], env is the restriction of the entire function sin⁴(π(v − 1/2)/3), cos θ and sin θ are
entire functions of v, and S, a, b are polynomials. ∎

**Lemma {#lem:cone-ellipse}** (F on a Bernstein ellipse.) For ϱ > 1 let E_ϱ be the closed region bounded by the
ellipse with foci ±1 and semi-axes (ϱ + ϱ^(−1))/2 and (ϱ − ϱ^(−1))/2. Take ϱ = 2 at the first seed and ϱ = 3/2 at the
second. Then for t ∈ E_ϱ and x ∈ [−1, 1], with r = c + ℓt, the holomorphic extension of F satisfies |F| ≤ M, where
M = 192.3 at the first seed and M = 7.878 at the second.

*Proof.* Let t ∈ E_ϱ and z := c + ℓt = p + iq. Then |q| ≤ η := ℓ(ϱ − ϱ^(−1))/2, |z − c| ≤ ℓ(ϱ + ϱ^(−1))/2 and
p ≥ r_− := c − ℓ(ϱ + ϱ^(−1))/2. At the first seed η ≤ 0.5579, ℓ(ϱ + ϱ^(−1))/2 ≤ 0.9298 and r_− ≥ 10.061; at the second
η ≤ 0.3100, ℓ(ϱ + ϱ^(−1))/2 ≤ 0.8058 and r_− ≥ 10.185. Put V := 2 + 2/(r_−² − 1) ≤ 2.021 (both seeds).

(i) The phase. Im v(z) = 2q + arctan(q/(p − 1)) − arctan(q/(p + 1)), and since arctan has derivative at most
1, |arctan(q/(p − 1)) − arctan(q/(p + 1))| ≤ |q| (1/(p − 1) − 1/(p + 1)) = 2|q|/(p² − 1). So |Im v(z)| ≤ η V =: η_v,
with η_v ≤ 1.128 (first seed) and η_v ≤ 0.6266 (second). Also v′(z) = 2 + 2/(z² − 1) and |z² − 1| ≥ |z|² − 1 ≥
r_−² − 1, so |v′(z)| ≤ V.

(ii) The trigonometric factors. For complex ξ, |sin ξ| and |cos ξ| are at most cosh(Im ξ). With env and d env/dv
extended as the entire functions sin⁴(π(v − 1/2)/3) and (4π/3) sin³(π(v − 1/2)/3) cos(π(v − 1/2)/3), this
gives |env(v(z))| ≤ c₄ and |d env/dv (v(z))| ≤ (4π/3) c₄, where c₄ := cosh⁴(π η_v/3) ≤ 10.1 (first seed), ≤ 2.24
(second); and |cos θ|, |sin θ| ≤ cosh(η_v/λ) ≤ 1.707 (first seed), ≤ 3.696 (second).

(iii) A and B. Here φ = (λ/2) z^(−3/2) env(v(z)), φ′ = (λ/2)(−(3/2) z^(−5/2) env + z^(−3/2) (d env/dv) v′) and
θ′ = v′/λ, with |z| ≥ p ≥ r_−. Since A = φ′ cos θ − φ θ′ sin θ and B = φ′ sin θ + φ θ′ cos θ, |A| and |B| are at
most (|φ′| + |φ| |θ′|) cosh(η_v/λ) ≤ Ā, where

    Ā := r_−^(−3/2) c₄ cosh(η_v/λ) ((λ/2)(3/(2r_−) + (4π/3) V) + V/2).

At the first seed r_−^(−3/2) ≤ 0.03134, the last factor is at most 5.318 and Ā ≤ 2.874; at the second
r_−^(−3/2) ≤ 0.03077, the last factor is at most 2.373 and Ā ≤ 0.6046.

(iv) R_app. Each t ∈ E_ϱ is t = (ω + ω^(−1))/2 with 1 ≤ |ω| ≤ ϱ, and T_i(t) = (ω^i + ω^(−i))/2, so |T_i(t)| ≤ ϱ^i.
Also |T_j(x)| ≤ 1 and |z − r_s| ≤ |z − c| + ℓ. So

    |R_app| ≤ Σ_(i,j) |C_(ij)| ϱ^i + Σ_j |a_j| + Σ_j |b_j| (ℓ(ϱ + ϱ^(−1))/2 + ℓ) ≤ R̄,

with R̄ = 13.089 at the first seed and R̄ = 12.122 at the second, by the sums of [[sec:cone-table-constants]].

(v) Since (1 + x)² + (1 − x²) + (1 − x)² = 3 + x² ≤ 4, |H| ≤ 4Ā², and |F| ≤ (16/9) Ā² R̄. This is at most
(16/9)(2.874)²(13.089) ≤ 192.3 at the first seed and (16/9)(0.6046)²(12.122) ≤ 7.878 at the second. ∎

The nodes of the grid are

    t_k := cos(kπ/n),  r_k := c + ℓ t_k  (0 ≤ k ≤ n),      x_l := cos(lπ/30)  (0 ≤ l ≤ 30),

with n := 40 at the first seed and n := 64 at the second.

**Lemma {#lem:cone-nodes}** (Values at the nodes.) For 0 ≤ k ≤ n and 0 ≤ l ≤ 30, |G(r_k, x_l)| ≤ ε_*, with
ε_* = 1.5 × 10⁻⁸ at the first seed and ε_* = 7.4 × 10⁻⁸ at the second. More finely, |G(r_k, x_l)| ≤ ε_k for each k,
where ε_k is the entry of row k of [[sec:cone-table-n1]] (first seed) or [[sec:cone-table-n2]] (second seed).

*Proof.* Write G = G₁ + F with G₁ := (1 + x²) ℓ^(−2) ∂_t²S, as in [[eq:cone-g]]. At a node, T_i(t_k) = cos(ikπ/n)
and T_j(x_l) = cos(jlπ/30); with ψ := kπ/n,

    T_i″(cos ψ) = (i cos ψ sin(iψ) − i² sin ψ cos(iψ))/sin³ψ   (0 < k < n),      T_i″(±1) = (±1)^i i²(i² − 1)/3.

By the definitions of a and b, R_app(r, x) = r + S(r, x) − S(r_s, x) − (r − r_s) ∂_rS(r_s, x) on [r_s, r_e], and
r_k − r_s = ℓ(1 + t_k), ∂_rS = ℓ^(−1) ∂_tS, T_i′(−1) = (−1)^(i−1) i². So at the node (r_k, x_l)

    G₁ = (1 + x_l²) ℓ^(−2) Σ_(i,j) C_(ij) T_i″(t_k) T_j(x_l),        F = (4/9) H(r_k, x_l) (r_k + D_k(x_l)),
    D_k(x) := Σ_(i,j) C_(ij) (cos(ikπ/n) − (−1)^i + (−1)^i i² (1 + t_k)) T_j(x),

where H(r_k, x_l) is given by [[eq:cone-data]] and [[eq:cone-w]] through values of sin, cos, ln and square roots at
r_k. Each node value is thus a finite sum of products of the tabulated coefficients with cosines of rational
multiples of π, together with one value of H. Arranged as Σ_j T_j(x_l) Σ_i (…), all node values take about
2 × 10⁵ multiplications at the first seed and 4 × 10⁵ at the second. At the nodes, |G₁| and |F| are at most
3.1 × 10⁻² at the first seed and 1.5 × 10⁻² at the second, and they cancel. At the end nodes k = 0 and k = n, that
is r_k = r_e and r_k = r_s, φ = φ′ = 0, so H = F = 0 and G = G₁.

*The data fix the node values to within 10⁻¹⁶.* The coefficients C_(ij) are exact decimals: they define S. Besides
them and the angles, G₁ depends only on ℓ, and F only on r_k = c + ℓ t_k. The twenty-decimal values of c and ℓ in
[[sec:cone-tables]] give ℓ to within 5 × 10⁻²¹, which changes G₁ by less than 10⁻²¹ (as |G₁| ≤ 3.1 × 10⁻² and
ℓ > 0.74), and r_k to within 10⁻²⁰. For F, put Φ(r) := (4/9) H(r, x_l)(r + D_k(x_l)), so that F = Φ(r_k). By
[[lem:cone-structure]] (b) and [[lem:cone-ellipse]] (iii) and (v), t ↦ H(c + ℓt, x_l) is holomorphic on a
neighbourhood of E_ϱ and bounded on E_ϱ by 4Ā². Put δ_ϱ := (ϱ + ϱ^(−1))/2 − 1, which is 1/4 at the first seed and
1/12 at the second. For real t within δ_ϱ/2 of [−1, 1], every point of the disc of radius δ_ϱ/2 about t lies within
δ_ϱ of a point of [−1, 1], so the sum of its distances to ±1 is at most 2 + 2δ_ϱ = ϱ + ϱ^(−1); the disc therefore
lies in E_ϱ, and Cauchy's estimate gives |∂_tH| ≤ 8Ā²/δ_ϱ. Since r_k + D_k(x_l) = R_app(r_k, x_l) has modulus at
most R̄ ([[lem:cone-ellipse]] (iv)), |r + D_k(x_l)| ≤ R̄ + 1 for real r within ℓδ_ϱ/2 of r_k, and there

    |Φ′(r)| ≤ (4/9)(ℓ^(−1) (8Ā²/δ_ϱ)(R̄ + 1) + 4Ā²) = (16/9) Ā² (2(R̄ + 1)/(ℓ δ_ϱ) + 1) ≤ 2.3 × 10³

at both seeds, so the error in r_k changes F by less than 3 × 10⁻¹⁷.

*The precision each bound needs.* If G₁ and F are known to within e at a node, G is known to within 2e, and |G|
≤ ε follows as soon as the approximate value has modulus at most ε − 2e; this is the case whenever |G| + 4e ≤ ε.
The largest |G| at the nodes is attained at the end nodes: it is below 1.4439 × 10⁻⁸ at the first seed (k = 0)
and below 7.3612 × 10⁻⁸ at the second (k = 64), so its margins to ε_* exceed 5.6 × 10⁻¹⁰ and 3.8 × 10⁻¹⁰. At the
interior nodes |G| ≤ 4.3 × 10⁻⁹ (first seed) and |G| ≤ 2.7 × 10⁻⁸ (second). So ε_* is confirmed at every node
with e = 5 × 10⁻¹¹, and at the interior nodes already with e = 10⁻⁹. The entries ε_k are the row maxima of |G|
rounded up to two significant digits. The smallest margin ε_k − max_l |G(r_k, x_l)| exceeds 1.3 × 10⁻¹⁴ at the
first seed (k = 19) and 1.6 × 10⁻¹⁴ at the second (k = 32), so every ε_k is confirmed with e = 3 × 10⁻¹⁵, that
is, with G₁ and F to about fourteen significant digits. The data allow this, by the previous paragraph. Two node
values of each seed, one at an end node and one where G₁ and F are largest, are printed with the tables as
checkpoints. ∎

We use two results on polynomial interpolation in the Chebyshev points ξ_k := cos(kπ/n), 0 ≤ k ≤ n. For a
continuous g on [−1, 1], I_n g denotes the polynomial of degree at most n that equals g at these n + 1 points;
I_n g = g when g is a polynomial of degree at most n, and I_n is linear. In Lagrange form I_n g = Σ_k g(ξ_k) L_k,
where L_k is the polynomial of degree n with L_k(ξ_k) = 1 and L_k(ξ_m) = 0 for m ≠ k, and the Lebesgue constant of
the points is Λ_n := max_(x∈[−1, 1]) Σ_k |L_k(x)| [Tre19, (15.2)–(15.4), p. 108].
So |I_n g| ≤ Λ_n max_k |g(ξ_k)| on [−1, 1].

- (I1) [Tre19, Theorem 15.2, (15.8a), p. 109]: Λ_n ≤ (2/π) ln(n + 1) + 1.
- (I2) [Tre19, Theorem 8.2, (8.3), p. 57]: if g is analytic in [−1, 1] and analytically continuable to the open
  region bounded by the ellipse of [[lem:cone-ellipse]] with parameter ϱ > 1, where |g| ≤ M,
  then |g − I_n g| ≤ 4M ϱ^(−n)/(ϱ − 1) on [−1, 1], for every n ≥ 0.

In particular Λ_30 ≤ 3.19, Λ_40 ≤ 3.37 and Λ_64 ≤ 3.66.

**Lemma {#lem:cone-residual-bound}** (The residual of the linear equation.) On [r_s, r_e] × [−1, 1],

    |ℰ| ≤ |G| ≤ ℰ̄ := Λ_30 (Λ_n ε_* + 4M ϱ^(−n)/(ϱ − 1)),

and ℰ̄ ≤ 1.7 × 10⁻⁷ at the first seed and ℰ̄ ≤ 8.7 × 10⁻⁷ at the second.

*Proof.* The first inequality holds because 1 + x² ≥ 1. Fix r ∈ [r_s, r_e]. By [[lem:cone-structure]] (a), G(r, ·)
is a polynomial of degree at most 30, so it equals its interpolant in the points x_l, and by the Lagrange form with
n = 30, |G(r, x)| ≤ Λ_30 max_l |G(r, x_l)|. Now fix l and put g_l(t) := G(c + ℓt, x_l) for t ∈ [−1, 1]. By [[eq:cone-g]],
g_l = P_l + F_l, where P_l := (1 + x_l²) ℓ^(−2) ∂_t²S(·, x_l) is a polynomial of degree at most N_r − 2 ≤ n and
F_l(t) := F(c + ℓt, x_l). So I_n P_l = P_l and g_l − I_n g_l = F_l − I_n F_l. By [[lem:cone-structure]] (b) and
[[lem:cone-ellipse]], F_l is holomorphic on a neighbourhood of E_ϱ (whose points have Re(c + ℓt) ≥ r_− > 1) and
bounded on E_ϱ by M, so (I2) gives |F_l − I_n F_l| ≤ 4M ϱ^(−n)/(ϱ − 1). By the Lagrange form and
[[lem:cone-nodes]], |I_n g_l| ≤ Λ_n max_k |g_l(t_k)| ≤ Λ_n ε_*. Hence |g_l| ≤ Λ_n ε_* + 4M ϱ^(−n)/(ϱ − 1) on
[−1, 1], for every l, and the bound on G follows. At the first seed 4M ϱ^(−n)/(ϱ − 1) = 4(192.3) 2^(−40) ≤
7.0 × 10⁻¹⁰ and ℰ̄ ≤ 3.19 (3.37 × 1.5 × 10⁻⁸ + 7.0 × 10⁻¹⁰) ≤ 1.7 × 10⁻⁷. At the second,
8(7.878)(2/3)^64 ≤ 3.4 × 10⁻¹⁰ and ℰ̄ ≤ 3.19 (3.66 × 7.4 × 10⁻⁸ + 3.4 × 10⁻¹⁰) ≤ 8.7 × 10⁻⁷. ∎

*Proof of [[prop:cone-residual]].* Let W̄ be as in [[lem:cone-w]] and R̄ as in [[lem:cone-ellipse]] (iv), which
bounds R_app also for real t ∈ [−1, 1] ⊂ E_ϱ. On [r_s, r_e] × [−1, 1], ∂_r²R_app = ℰ − w R_app, so by
[[lem:cone-residual-bound]] and [[lem:cone-w]]

    |∂_r²R_app| ≤ K := ℰ̄ + W̄ R̄,      K ≤ 0.0261 (first seed),  K ≤ 0.0104 (second seed).

Since R_app(r_s, x) = r_s and ∂_rR_app(r_s, x) = 1,

    R_app(r, x) − r = ∫_(r_s)^r (r − q) ∂_r²R_app(q, x) dq ≥ −K (r − r_s)²/2,

so R_app(r, x) ≥ r_s + (r − r_s)(1 − Kℓ) ≥ r_s on [r_s, r_e], as Kℓ ≤ 0.02. Also
∂_rR_app(r_e, x) ≥ 1 − 2ℓK ≥ 0.96.

(a) For 10 ≤ r < r_s, R_app = r, so ∂_r²R_app = 0, and w = 0 by [[lem:cone-generator]]. For r > r_e, ∂_r²R_app = 0
and w = 0, and R_app ≥ R_app(r_e, x) ≥ r_s > 0 since R_app increases there. In both cases [[eq:cone-ricvv]] gives
Ric_vv[g_app] = 0.

(b) On [r_s, r_e], f² ≤ (1 − r_e^(−2))² and R_app ≥ r_s, so by [[eq:cone-ricvv]] and [[lem:cone-residual-bound]]

    |Ric_vv[g_app]| ≤ (3 (1 − r_e^(−2))²/(4 r_s)) ℰ̄ ≤ 0.0722 ℰ̄.

This is at most 0.0722 × 1.7 × 10⁻⁷ ≤ 1.3 × 10⁻⁸ ≤ 4.97 × 10⁻⁵ at the first seed, and at most
0.0722 × 8.7 × 10⁻⁷ ≤ 6.3 × 10⁻⁸ ≤ 2.28 × 10⁻⁵ at the second.

(c) For r < r_s and for r > r_e, ∂_r²R_app = 0. Since T_i″(±1) = (±1)^i i²(i² − 1)/3, the one-sided values at the
ends are

    ∂_r²R_app(r_s+, x) = Σ_j δ^s_j T_j(x),      ∂_r²R_app(r_e−, x) = Σ_j δ^e_j T_j(x),
    δ^s_j := ℓ^(−2) Σ_i (−1)^i (i²(i² − 1)/3) C_(ij),      δ^e_j := ℓ^(−2) Σ_i (i²(i² − 1)/3) C_(ij).

As |T_j| ≤ 1 on [−1, 1], the jumps are at most Σ_j |δ^s_j| and Σ_j |δ^e_j|. By [[sec:cone-table-jumps]] these are at
most 2.56 × 10⁻⁸ and 2.72 × 10⁻⁸ at the first seed, and 6.85 × 10⁻⁸ and 7.29 × 10⁻⁸ at the second. ∎

The proof gives more than the proposition states: |Ric_vv[g_app]| ≤ 1.3 × 10⁻⁸ at the first seed and
≤ 6.3 × 10⁻⁸ at the second. The two terms on the right of [[eq:cone-raychaudhuri]] cancel in Ric_vv, and the second
of them is −s. At x = −1, [[eq:cone-w]] gives H = 4B², w = (8/9) B² and s = (2/3) f² B². At the first seed and
r = 10.73, [[eq:cone-v]] and [[eq:cone-data]] give v = 1.47373… and B = 3.9165 × 10⁻², so s = 1.0049 × 10⁻³; at the
second seed and r = 10.98, v = 1.97801… and B = 2.7668 × 10⁻², so s = 5.019 × 10⁻⁴. With [[lem:cone-w]], sup s lies
between 1.00 × 10⁻³ and 1.46 × 10⁻³ at the first seed and between 5.0 × 10⁻⁴ and 6.3 × 10⁻⁴ at the second. So the
residual is below 1.3 × 10⁻⁵ (first seed) and 1.3 × 10⁻⁴ (second) times the largest size of the terms that cancel
in it.

### Exact data on the cone {#sec:cone-exact}

**Proposition {#prop:cone-exact}** (Exact data.) Fix a seed and x ∈ [−1, 1]. There is exactly one function
R(·, x) ∈ C²([10, ∞)) with R(r, x) = r for 10 ≤ r ≤ r_s and

    ∂_r²R = −(4/(3f²)) R s      on [10, ∞).                                                                {#eq:cone-ode}

With W̄ as in [[lem:cone-w]] it satisfies:

(a) for r_s ≤ r ≤ r_e, 0 ≤ r − R(r, x) ≤ W̄ r (r − r_s)²/2 and 1 − W̄ (r² − r_s²)/2 ≤ ∂_rR(r, x) ≤ 1; so
r − R ≤ 0.0259 and ∂_rR ≥ 0.967 at the first seed, and r − R ≤ 0.0112 and ∂_rR ≥ 0.986 at the second;

(b) for r ≥ r_e, R(r, x) = R(r_e, x) + ∂_rR(r_e, x)(r − r_e), so 0 ≤ r − R(r, x) ≤ 0.0259 + 0.0326 (r − r_e) at the
first seed and 0 ≤ r − R(r, x) ≤ 0.0112 + 0.0140 (r − r_e) at the second;

(c) R > 0 on [10, ∞) × [−1, 1]; R and ∂_rR are continuous there, and R is C^∞ in x.

The data (R, P, Q, W) therefore satisfy the Raychaudhuri constraint exactly: Ric_vv[R] = 0 on the whole cone, by
[[eq:cone-ricvv]]. The constraint Ric_vx, which determines the shift on the cone, is not treated here.

*Proof.* By [[lem:cone-generator]], [[eq:cone-ode]] is ∂_r²R = −w R, with w continuous on [10, ∞) × [−1, 1] and zero
outside (r_s, r_e). On [10, r_s] the function R = r solves it. On [r_s, ∞) the linear equation ∂_r²R = −w R with
R(r_s) = r_s and ∂_rR(r_s) = 1 has exactly one C² solution, and the two pieces join to a C² function because
w(r_s, x) = 0. Any solution equal to r on [10, r_s] has these values at r_s, which gives uniqueness.

For the bounds we compare with the solution r of ∂_r²R = 0. Let r₁ be the supremum of the r₁′ ∈ (r_s, r_e] with
R > 0 on [r_s, r₁′]. On [r_s, r₁), ∂_r²R = −w R ≤ 0, so ∂_rR ≤ 1 and R ≤ r; hence 0 ≤ w R ≤ W̄ q at every
q ∈ [r_s, r₁), and

    ∂_rR(r) = 1 − ∫_(r_s)^r w R dq ≥ 1 − W̄ (r² − r_s²)/2,
    r − R(r) = ∫_(r_s)^r (r − q) w R dq ∈ [0, W̄ r (r − r_s)²/2].

So R(r) ≥ r (1 − W̄ (r − r_s)²/2) ≥ r (1 − 2ℓ² W̄) on [r_s, r₁), and 2ℓ² W̄ ≤ 0.0023. If r₁ < r_e, continuity would
give R(r₁) > 0 and R > 0 beyond r₁, against the definition of r₁; so r₁ = r_e and the bounds hold on [r_s, r_e]. With
r ≤ r_e, (r − r_s)²/2 ≤ 2ℓ² ≤ 1.1064 and (r_e² − r_s²)/2 ≤ 16.35, they give the numbers in (a). For r ≥ r_e, w = 0,
so R is affine in r with slope ∂_rR(r_e, x), and by (a) 1 − ∂_rR(r_e, x) ≤ W̄ (r_e² − r_s²)/2, which is at most
1.99 × 10⁻³ × 16.35 ≤ 0.0326 at the first seed and 8.55 × 10⁻⁴ × 16.35 ≤ 0.0140 at the second, while
∂_rR(r_e, x) ≤ 1. Since r − R(r) = (r_e − R(r_e)) + (1 − ∂_rR(r_e))(r − r_e), this gives (b), and R > 0 there; on
[10, r_s], R = r > 0.

For the regularity, R(r, x) = r − ∫_(r_s)^r (r − q) w(q, x) R(q, x) dq on [r_s, r_e]. By [[eq:cone-w]], w is
continuous on [r_s, r_e] × [−1, 1] and smooth in x, with every x-derivative continuous (it is a polynomial in x
divided by 1 + x²). The Picard iterates of this integral equation and all their x-derivatives converge uniformly on
[r_s, r_e] × [−1, 1]. Fix m; by induction on k, for all orders up to m at once, the x-derivatives of order at most m
of the k-th increment are bounded by C_m D_m^k (r − r_s)^(2k)/(2k)! for constants C_m and D_m, because by the Leibniz
rule the x-derivative of order j ≤ m of the next increment involves only the x-derivatives of w of order at most j
and those of the k-th increment of order at most j. So R and ∂_rR are continuous and R is C^∞ in x on
[r_s, r_e] × [−1, 1], and then on [10, ∞) × [−1, 1] by the explicit formulas on the other two intervals. ∎

**Corollary {#cor:cone-compare}** (The approximant and the exact data.) With R as in [[prop:cone-exact]] and ℰ̄ as in
[[lem:cone-residual-bound]], put Δ := 2ℓ² ℰ̄/(1 − 2ℓ² W̄). On [r_s, r_e] × [−1, 1]

    |R_app − R| ≤ Δ,      |∂_r(R_app − R)| ≤ 2ℓ (ℰ̄ + W̄ Δ),

that is, |R_app − R| ≤ 1.9 × 10⁻⁷ and |∂_r(R_app − R)| ≤ 2.6 × 10⁻⁷ at the first seed, and |R_app − R| ≤ 9.7 × 10⁻⁷
and |∂_r(R_app − R)| ≤ 1.3 × 10⁻⁶ at the second. For r ≤ r_s, R_app = R; for r ≥ r_e both are affine in r,
so |R_app − R| grows at most linearly, with these values and slopes at r_e.

*Proof.* D := R_app − R satisfies D(r_s, x) = ∂_rD(r_s, x) = 0 and, on [r_s, r_e], ∂_r²D = (ℰ − w R_app) + w R =
ℰ − w D. Let Δ₀ := max |D| over [r_s, r_e] × [−1, 1]. Then |D(r, x)| ≤ ∫_(r_s)^r (r − q)(ℰ̄ + W̄ Δ₀) dq ≤
2ℓ²(ℰ̄ + W̄ Δ₀), so Δ₀ (1 − 2ℓ² W̄) ≤ 2ℓ² ℰ̄, that is Δ₀ ≤ Δ; and |∂_rD| ≤ ∫_(r_s)^r (ℰ̄ + W̄ Δ₀) dq ≤
2ℓ(ℰ̄ + W̄ Δ). The numbers follow from [[lem:cone-w]], [[lem:cone-residual-bound]], 2ℓ² ≤ 1.1064 and 2ℓ ≤ 1.4876. ∎

### The characteristic problem and the seed {#sec:tl5-problem}

We call the form of the metrics of [[sec:cone-constraint]], in the coordinates (u, v, x, φ1, φ2), the gauge. The leaves
are the three-dimensional orbits S_(u,v) := {u, v fixed}, which are spheres with the metric γ, the restriction of g,
and ∂_v is null and orthogonal to them. The outgoing generators are the integral curves of ∂_v, and the outgoing
expansion of S_(u,v) is θ_leaf := Σ_A g(∇_(e_A) ∂_v, e_A), the sum over a γ-orthonormal frame of the leaf.

**Lemma {#lem:tl5-leaf-expansion}** (The expansion of a leaf.) For every metric of the class in the gauge,
θ_leaf = 3 ∂_vR/R.

*Proof.* For vector fields X, Y tangent to the leaves that commute with ∂_v, such as ∂_x, ∂_φ1 and ∂_φ2,
g(∇_X ∂_v, Y) = g(∇_(∂_v) X, Y), and the compatibility of ∇ with g gives
g(∇_(∂_v) X, Y) + g(∇_(∂_v) Y, X) = ∂_v g(X, Y). So θ_leaf = (1/2) γ^(AB) ∂_v γ_AB = ∂_v ln (det γ)^(1/2) in the
coordinates (x, φ1, φ2), and det γ = R⁶/16 in the gauge, as in the proof of [[lem:cone-raychaudhuri]]; at x = ±1 the
identity follows by continuity. ∎

**Lemma {#lem:tl5-seed}** (The seed in the gauge.) Let F(R) := e^(2R) (R − 1)/(R + 1) for R > 0. For −10 ≤ u < 0 and
v ≥ 0 let R(u, v) > 0 solve

    F(R) = e^(v − 2u) (u + 1)/(u − 1)                                                       {#eq:tl5-seed-radius}

where a solution exists, call that set of (u, v) D_seed, and put

    e^(2W) := (R + 1)² u² e^(v − 2u − 2R)/(2 R² (u − 1)²),      P = Q := 0,      β := 0.             {#eq:tl5-seed-lapse}

(a) F is an increasing bijection of (0, ∞) onto (−1, ∞), so R(u, v) is unique where it exists. For u ≤ −1 it exists
for every v ≥ 0; for −1 < u < 0 it exists exactly when v < 2u + ln((1 − u)/(1 + u)). At v = 1/2 it exists exactly for
u < u₀, where −0.7698 < u₀ < −0.7697. The set D_seed is connected.

(b) R and W are real-analytic on D_seed, ∂_vR = f(R)/2 there, and e^(2W) = f(R)/(2 f(−u)) where u ≠ −1.

(c) With these R, P, Q, W and β, the metric of the class in the gauge on D_seed × S³ is a vacuum metric: it is the seed,
the five-dimensional Schwarzschild–Tangherlini metric of mass 1.

(d) It induces on {v = 0} the values R = −u, P = Q = β = 0 and e^(2W) = 1/2, and on {u = −10, 0 ≤ v ≤ 1/2} the values
of [[eq:cone-data]] with R = r, r the parameter of [[eq:cone-v]].

*Proof.* (a) F′(R) = 2R² e^(2R)/(R + 1)² > 0, F(R) → −1 as R → 0 and F(R) → ∞ as R → ∞. For u ≤ −1 the right side
of [[eq:tl5-seed-radius]] is nonnegative. For −1 < u < 0 it is −e^(v − 2u)(1 + u)/(1 − u), which exceeds −1 exactly
when v < h(u) := 2u + ln((1 − u)/(1 + u)). On (−1, 0), h′(u) = 2 − 2/(1 − u²) < 0, h → ∞ as u → −1 and h(0) = 0, so
h(u) > 1/2 exactly for u < u₀ with h(u₀) = 1/2; and h(−0.7698) > 0.50005 > 1/2 > 0.49980 > h(−0.7697). For each u the
admissible v form an interval containing 0, since at v = 0 the right side equals F(−u) > −1; so D_seed is connected.

(b) R is real-analytic by the analytic implicit function theorem, since F′ > 0, and then so is W, as u ≠ 1 and R > 0.
Differentiating [[eq:tl5-seed-radius]] in v gives F′(R) ∂_vR = F(R), so ∂_vR = F(R)/F′(R) = (R² − 1)/(2R²) = f(R)/2.
Where u ≠ −1, [[eq:tl5-seed-radius]] gives e^(v − 2u) = F(R)(u − 1)/(u + 1); substituting in [[eq:tl5-seed-lapse]],
e^(2W) = (R + 1)(R − 1) u²/(2R² (u − 1)(u + 1)) = f(R)/(2 f(−u)).

(c) Let r*(ρ) := ρ + (1/2) ln((ρ − 1)/(ρ + 1)) for ρ > 1, so that dr*/dρ = 1/f(ρ). Where u < −1, the right side of
[[eq:tl5-seed-radius]] is positive, so R > 1, and taking logarithms the equation reads 2 r*(R) = v + 2 r*(−u). Put
t := v/2 − r*(−u). Then dt = dv/2 + du/f(−u) and d(r*(R)) = dv/2 − du/f(−u), so by (b)

    −f(R) dt² + dR²/f(R) = −f(R) (dt − d(r*(R)))(dt + d(r*(R))) = −2 f(R) du dv/f(−u) = −4 e^(2W) du dv.

With P = Q = β = 0 the remaining part of the metric is R² (dx²/(4(1 − x²)) + ((1 + x)/2) dφ1² + ((1 − x)/2) dφ2²),
which is R² times the round metric of S³ (with x = cos 2ϑ it is R² (dϑ² + cos²ϑ dφ1² + sin²ϑ dφ2²)). So on {u < −1}
the metric is −f dt² + f⁻¹ dr² + r² γ_(S³) with r = R, which is [[eq:vr-form]] with μ = 1 in the coordinate
t + r*(r), since −f (dt + dr/f)² + 2 (dt + dr/f) dr = −f dt² + dr²/f. By [[prop:vaidya]] (a) with μ′ = 0 it is
vacuum there. The components of the metric in the coordinates (u, v, ϑ, φ1, φ2), 0 < ϑ < π/2, are real-analytic by (b),
hence so are those of its Ricci tensor; they vanish on the open set {u < −1} of the connected set D_seed × (0, π/2), so
they vanish identically, and the metric is vacuum on D_seed × S³ by continuity at the axes, where it is R² times the
round metric in the angular directions and smooth. It is the seed on all of D_seed × S³, the horizon u = −1 and the
region u > −1 included: differentiating [[eq:tl5-seed-radius]] in u gives F′(R) ∂_uR = −2u² e^(v − 2u)/(u − 1)², so
∂_uR = −2e^(2W) by the formula for F′ in (a) and [[eq:tl5-seed-lapse]], and with ∂_vR = f(R)/2 from (b) this gives
2 dv dR − f(R) dv² = −4e^(2W) du dv. For each v the admissible u form an interval: by (a) they are the u ∈ [−10, −1]
and the u ∈ (−1, 0) with h(u) > v, and h is decreasing. As ∂_uR < 0, the map (u, v) ↦ (v, R) is therefore injective
on D_seed, with Jacobian determinant −∂_uR > 0, so (v, R, ϑ, φ1, φ2) are coordinates on D_seed × S³ away from the
axes, and in them the metric is [[eq:vr-form]] with μ = 1 and r = R. By continuity, (u, v, ω) ↦ (v, R(u, v), ω),
ω ∈ S³, is then an isometry of D_seed × S³, the axes included, onto a region of the seed.

(d) At v = 0, R = −u solves [[eq:tl5-seed-radius]], since F(−u) = e^(−2u)(u + 1)/(u − 1), and then
[[eq:tl5-seed-lapse]] gives e^(2W) = (1 − u)² u²/(2u² (u − 1)²) = 1/2. At u = −10 the equation reads
2R + ln((R − 1)/(R + 1)) = v + 20 + ln(9/11), that is v = v(R) with v(·) of [[eq:cone-v]], and (b) gives
e^(2W) = f(R)/(2 f(10)), the W of [[eq:cone-data]]. For v ≤ 1/2, env(v) = 0, so the P and Q of [[eq:cone-data]]
vanish, as for the seed. ∎

**Definition {#def:tl5-problem}** (The characteristic problem at 10 l5.) Fix a seed and u* ∈ (−10, 0), and let
C₀ := {v = 0, −10 ≤ u ≤ u*} and N := {u = −10, v ≥ 0}. The data on C₀ are those of the seed: R = −u, P = Q = β = 0
and e^(2W) = 1/2. The data on N are W, P and Q of [[eq:cone-data]], with r the parameter of [[eq:cone-v]], and the R
of [[prop:cone-exact]]; on N ∩ {v ≤ 1/2} the shift is β = 0, and beyond it is subject to the constraint Ric_vx = 0,
which this paper does not treat. A solution on a set D ⊂ {−10 ≤ u ≤ u*, v ≥ 0} × S³ is a T²-invariant vacuum metric of
the class in the gauge on D, whose R, P, Q, W and β are C² functions of (u, v, x) on D and whose values on D ∩ C₀ and
D ∩ N are the data.

On N ∩ {v ≤ 1/2}, r ≤ r_s, so the R of [[prop:cone-exact]] is r and the data there are the seed's ([[lem:tl5-seed]]
(d)).

**Theorem {#thm:ten-l5}** (The prescribed wavelength 10 l5.) At either seed of [[def:tl5-seeds]]:

(a) there is no separation of scales: on x_K = 1 the wavelength λ = 10 l5 is 10 times the curvature length, and at the
horizon it is more than 2.91 times it at the first seed and more than 0.92 times it at the second;

(b) the characteristic problem of [[def:tl5-problem]] has a solution where the solution is the seed: on
D⁰ := ({−10 ≤ u ≤ u*, 0 ≤ v ≤ 1/2} ∩ D_seed) × S³, which is all of {−10 ≤ u ≤ u*, 0 ≤ v ≤ 1/2} × S³ when u* < u₀
([[lem:tl5-seed]] (a)), the seed of [[lem:tl5-seed]] is a smooth vacuum metric of the class in the gauge that induces
the data on D⁰ ∩ C₀ and on D⁰ ∩ N;

(c) for every solution on a set D as in [[prop:tl5-leaves]] whose transverse derivative ∂_vR on C₀ is the seed's,
every leaf with −1 < u < 0 is outer trapped where it meets D; every T²-invariant marginally outer trapped section of an
ingoing cone contained in the interior of D has its innermost point at u ≤ −1; and every such section for which D
contains the two generator segments named in [[cor:tl5-mots]] (c) lies in the band of [[cor:tl5-mots]] (c), between
the infimum and the supremum of u over the zeros of the leaves' expansion on that cone in D.

No existence is asserted for v > 1/2: [[lem:tl5-continuation]] states what a continuation would need, and
[[rem:tl5-beyond]] why the bounds proved in this chapter do not provide it.

*Proof.* (a) is [[prop:tl5-scales]]. (b) D⁰ ⊂ D_seed × S³, so by [[lem:tl5-seed]] (b) and (c) the seed is a smooth
vacuum metric of the class in the gauge on D⁰, and by [[lem:tl5-seed]] (d) and the sentence after
[[def:tl5-problem]] it induces the data on D⁰ ∩ C₀ and D⁰ ∩ N. (c) is [[prop:tl5-leaves]] and [[cor:tl5-mots]] (b)
and (c), since θ_S = 0 on a marginally outer trapped section. ∎

**Remark {#rem:tl5-runs}** (Numerical observation.) The characteristic problem was solved numerically in the gauge,
with an expansion in the polar angle, at both seeds. At the second seed, with the angular and null grids refined
together, the two coarser angular resolutions agree up to v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at
every angle; on a finer null grid the resolutions with 32 and 40 angular modes agree to 0.09 𝒦₀ up to v = 3.5 and to
0.53 𝒦₀ up to v = 4.5, where 𝒦₀ = 72/R⁸, away from the cells that the run with 48 modes masks, and that run departs
from v ≈ 3.25 as on the coarser grid: beyond v ≈ 3.25 the second seed's solution is not resolved in angle. At the first
seed, a scheme that imposes the outgoing constraint along every generator, with its singular coupling at the axes
regularised, converges at second order in the null step to v ≈ 1.8 at areal radius at least 0.9 and to v ≈ 2.0 at
areal radius at least 1.2 (observed orders 2.00–2.03), and is resolved in angle there (the runs with 40 and 48 modes
change the metric by at most 3.0 × 10⁻⁹ and 3.3 × 10⁻⁹); the scheme that does not impose it is consistent with
second-order convergence to v ≈ 1.8 at areal radius at least 1. Beyond, with 32 modes the metric still converges in
the null step while the unimposed constraint does not fall, so that limit is not vacuum; from v ≈ 1.9 at areal radius
0.9–1.0 and from v ≈ 2.0 at 1.0–1.2 the violation grows with the angular resolution, and at 1.0–1.2 on [1.8, 2.0) the
comparison in angular resolution does not decide. The linear scattering of the shell off the seed at 10 l5 was also
solved numerically; no conclusion is drawn from it. No proof uses these observations.

### The second zero {#sec:tl5-second-zero}

The second zero of [[rem:tl5-bondi-scheme]] is a zero of the outgoing expansion of the round spheres of the Bondi
chart. The results of this section concern the exact solution in the gauge wherever it exists; they are not existence
results.

**Proposition {#prop:tl5-leaves}** (The leaves inside the horizon generator.) Let g be a solution on a set D such that
with each point (u, v, x) the set D contains the segment {(u, v′, x) : 0 ≤ v′ ≤ v}, and suppose ∂_vR = f(R)/2 on
D ∩ C₀, as for the seed ([[lem:tl5-seed]] (b)). Then on D

    e^(−2W) ∂_vR ≤ 1 − u⁻²,                                                                           {#eq:tl5-leaves}

and every leaf S_(u,v) with −1 < u < 0 that meets D has θ_leaf < 0 at each of its points in D: it is outer trapped.

*Proof.* At points with |x| < 1, [[eq:cone-raychaudhuri]] with Ric_vv = 0 gives
∂_v²R − 2 ∂_vW ∂_vR = −(R/3) s with s := (∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)² ≥ 0, so

    ∂_v(e^(−2W) ∂_vR) = e^(−2W) (∂_v²R − 2 ∂_vW ∂_vR) = −(R/3) e^(−2W) s ≤ 0,

since R > 0; by continuity this holds also at x = ±1. So e^(−2W) ∂_vR does not increase along the outgoing generators.
On C₀, R = −u, e^(2W) = 1/2 and ∂_vR = f(−u)/2, so e^(−2W) ∂_vR = f(−u) = 1 − u⁻² there, and [[eq:tl5-leaves]]
follows. For −1 < u < 0, 1 − u⁻² < 0, so ∂_vR < 0, and θ_leaf = 3 ∂_vR/R < 0 by [[lem:tl5-leaf-expansion]]. ∎

Let C_v be an ingoing cone {v = const}. The vector field L̲ := ∂_u + β ∂_x is tangent to C_v, null, and orthogonal to
every vector tangent to C_v: g(L̲, L̲) = G_x β² − 2G_x β² + G_x β² = 0, g(L̲, ∂_x) = −G_x β + G_x β = 0,
g(L̲, ∂_φi) = 0 and g(L̲, ∂_v) = −2e^(2W). Its integral curves are the ingoing generators of C_v. A T²-invariant
section of C_v is a compact T²-invariant C² submanifold S ⊂ C_v of dimension three that meets every generator of C_v
exactly once, and transversally; then S = {u = Ũ} for a C² function Ũ on C_v, constant along the generators and
T²-invariant, and U := u|_S. The leaf through a point of C_v is its intersection with {u = const}, and γ denotes its
metric. With θ_S its outgoing expansion along the null normal l_S of [[lem:tl5-section]], S is marginally outer trapped
if θ_S = 0 on S. Its innermost point is a point where U is largest, its outermost point one where U is smallest.

**Lemma {#lem:tl5-section}** (The expansion of a section.) Let g be a C² metric of the class in the gauge on a
neighbourhood of a T²-invariant section S of C_v, and on C_v put Z := 2 e^(2W) grad_γ Ũ, the gradient of Ũ along the
leaf through each point, a := e^(2W) |dŨ|²_γ and l_S := ∂_v + a L̲ + Z.

(i) l_S is null, orthogonal to S, and g(l_S, L̲) = −2e^(2W).

(ii) At every critical point p of U, including points on the axes,

    θ_S(p) = θ_leaf(p) + 2 e^(2W(p)) Δ_S U(p),                                                       {#eq:tl5-section}

where θ_S := Σ_A g(∇_(e_A) l_S, e_A) over an orthonormal frame of S and Δ_S is the Laplacian of the induced metric
of S.

(iii) At a point of S with |x| < 1 at which U is critical, if S is described near it as u = U(ξ), x = X(ξ) with X′ ≠ 0,
then [[eq:tl5-section]] reads θ_S = 3 ∂_vR/R + 2 e^(2W) U″/(X′² G_x).

*Proof.* (i) A vector at a point of S is V = Ŷ + c L̲ with Ŷ tangent to the leaf, and V is tangent to S if and only if
du(V) = dŨ(V); since du(Ŷ) = 0, du(L̲) = 1 and L̲Ũ = 0, this reads c = Ŷ(Ũ). For such V, using g(∂_v, Ŷ) = 0,
g(∂_v, L̲) = −2e^(2W), g(L̲, Ŷ) = g(L̲, L̲) = 0 and g(Z, L̲) = 0,

    g(l_S, V) = −2e^(2W) Ŷ(Ũ) + 2e^(2W) γ(grad_γ Ũ, Ŷ) = 0,      g(l_S, l_S) = −4a e^(2W) + |Z|²_γ = 0.

(ii) Let p be a critical point of U. Then Ŷ(Ũ) = 0 for every Ŷ tangent to the leaf at p, so T_pS is the tangent space
of the leaf at p, Z(p) = 0, a(p) = 0, and da(p) = 0 because a is quadratic in the derivatives of Ũ along the leaf. Let
e_A be an orthonormal frame of S near p. In g(∇_(e_A) l_S, e_A) = g(∇_(e_A) ∂_v, e_A) + e_A(a) g(L̲, e_A) +
a g(∇_(e_A) L̲, e_A) + g(∇_(e_A) Z, e_A) the middle two terms vanish at p. The first, summed, depends only on the
e_A(p), an orthonormal basis of the leaf's tangent space, and gives θ_leaf(p). In the last, ∇_(e_A(p)) Z depends only
on e_A(p); for X tangent to a leaf and Z tangent to the leaves, the component of ∇_X Z tangent to the leaf is ∇^γ_X Z,
∇^γ the Levi-Civita connection of γ, so the sum is the divergence of Z in γ at p:
2 e^(2W) Δ_γ Ũ(p) + 2 γ(grad_γ e^(2W), grad_γ Ũ)(p) = 2 e^(2W) Δ_γ Ũ(p). Finally, label the points of S and of the
leaf through p by the generators through them. In these coordinates U and Ũ are the same function, the two induced
metrics coincide at p, and both functions are critical at p, so Δ_S U(p) and Δ_γ Ũ(p) are both the trace of the
matrix of second derivatives at p in the common metric at p. Nothing here uses the coordinate x, so the argument holds
at the axes as well, where θ_leaf = 3 ∂_vR/R by continuity.

(iii) At such a point T_pS is spanned by ∂_x, ∂_φ1 and ∂_φ2, the leaf metric there is G_x dx² + …, and the tangent
vector of the curve is X′ ∂_x, so Δ_S U = U″/(X′² G_x) at a critical point. ∎

**Corollary {#cor:tl5-mots}** (Sections of an ingoing cone.) Let g be a solution on D as in [[prop:tl5-leaves]], and S
a T²-invariant section of C_v contained in the interior of D, so that [[lem:tl5-section]] applies, with innermost point
p and outermost point q.

(a) θ_S(p) ≤ θ_leaf(p) and θ_S(q) ≥ θ_leaf(q).

(b) If θ_S(p) ≥ 0, then u(p) ≤ −1.

(c) Suppose S is marginally outer trapped, D contains the segment of the generator of C_v through q from N to q, and
the segment of the generator through p from p to a point with u > −1. Then θ_leaf has a zero on the first segment and a
zero on the second; so S lies in the band between the infimum and the supremum of u over the zeros of θ_leaf on
C_v ∩ D.

*Proof.* (a) U attains its maximum at p, so p is a critical point and the Hessian of U at p is negative semidefinite,
whence Δ_S U(p) ≤ 0; [[eq:tl5-section]] gives the first inequality, and the minimum at q the second. (b) If
−1 < u(p) < 0 then θ_leaf(p) < 0 by [[prop:tl5-leaves]], so θ_S(p) < 0 by (a). (c) Here θ_S = 0, so by (a)
θ_leaf(p) ≥ 0 and θ_leaf(q) ≤ 0. On the second segment θ_leaf is continuous, nonnegative at p and negative at its end
with u > −1 ([[prop:tl5-leaves]]), so it vanishes at some point with u ≥ u(p). At the end of the first segment on N,
θ_leaf = 3 ∂_vR/R = (3f/(2R)) ∂_rR > 0 by [[eq:cone-v]] and [[prop:cone-exact]] (a)–(c), which give ∂_rR ≥ 0.967 and
R > 0 on N; so θ_leaf vanishes at some point of the first segment with u ≤ u(q). Hence u(q) is at least that infimum
and u(p) at most that supremum, and every point of S has u between them. ∎

**Remark {#rem:tl5-second-zero-runs}** (Numerical observation.) On the computed solutions of [[rem:tl5-runs]] the
leaves' expansion has one zero per angular node along every ingoing cone of the converged region: at the first seed at
u ∈ [−1.0070, −1.0035], areal radius 1.013–1.024, at v = 1.5, and at u ∈ [−1.0121, −1.0056] at v = 1.75; at the second
seed at u ∈ [−1.0029, −1.0014] at v = 1.5 and at u ∈ [−1.0080, −1.0036] at v = 1.9. By [[cor:tl5-mots]] a T²-invariant
marginally outer trapped section of these cones would lie in that band, near areal radius 1.01–1.05. Every further zero
of ∂_vR found up to v = 1.8 lies at u > −1 next to the inner cut-off of the computation, where [[prop:tl5-leaves]]
excludes it for the exact solution. The round spheres of the Bondi chart, rebuilt on the double-null solution at the
first seed, are tilted against the leaves, and their outgoing expansion reproduces the Bondi scheme's: on the sphere of
least areal radius reached (0.64–0.78), the band of columns along which the rebuilt spheres are untrapped has each edge
within one column spacing of the Bondi scheme's up to v = 1.525, at two radii of the data cone and two null resolutions,
and at v = 1.55 the Bondi scheme's band reaches the axis while the rebuilt one stops about four spacings short; from 800
to 1600 rows of the null grid the rebuilt outer zero changes by at most 0.007 up to v = 1.375, against its difference
from the Bondi scheme's from v = 1.3, 0.026–0.046 at the larger radius of the data cone and 0.053–0.106 at the smaller,
which is consistent with the truncation of the data, halving as the radius of the data cone doubles, at two radii; the
leaves' own expansion leaves no column untrapped. At the second seed the rebuild reaches no sphere below areal radius
about 0.5, so the Bondi scheme's second zero there, at 0.21–0.30, is neither reproduced nor contradicted. No proof uses
these observations.

### The residuals of two explicit approximants {#sec:tl5-residuals}

This section proves residual bounds for two explicit metrics of the class on the region of the
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
discrete solution of the characteristic problem of [[def:tl5-problem]] on one null grid, and U₂ the discrete solution on
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

**Lemma {#lem:tl5-rounding}** (The rounding.) For n, a ≥ 0 one has T_n^(a)(1) = ∏_(r<a) (n² − r²)/(2r + 1), and on
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
    r_γ(c) := (ε₀/γ!) ∏_(d=1,2,3) Σ_(l=0..n_d) (𝟙^(γ_d)_(n_d))_l |T_l(c_d)|,      (n₁, n₂, n₃) := (24, 30, 15),

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

**Lemma {#lem:tl5-positive}** (Positivity.) Let 𝔟 be one of the boxes of the subdivision in the proof of
[[prop:tl5-box-first]], taken with the first kind, or of the subdivisions in the proof of [[prop:tl5-boxes-second]],
taken with the second kind, and let c be a point of G. For that kind the enclosure of R on 𝔟 by [[lem:tl5-field-box]]
(γ = 0) lies in [1.80, ∞), and for either kind J^R_0(c) lies in [1.17, ∞). In the evaluations of
[[lem:tl5-jet-enclosure]] on 𝔟 and at its centre, for that kind, and at c, for either kind, the constant term of
every reciprocal and of every square root formed is a positive interval.

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

### Continuation beyond the seed {#sec:tl5-beyond}

The following lemma reduces existence beyond the seed to an a priori estimate on the whole region and a closing
condition, assuming the local existence, uniqueness and continuation of the characteristic problem in the gauge.

**Lemma {#lem:tl5-continuation}** (Existence by continuity.) Let u* ∈ (−10, 0) and v* > 1/2, and let smooth
T²-invariant characteristic data for the vacuum equations of the class in the gauge be given on
N₀ := {v = 1/2, −10 ≤ u ≤ u*} and N₁ := {u = −10, 1/2 ≤ v ≤ v*}, satisfying the characteristic constraints. Put
D := {−10 ≤ u ≤ u*, 1/2 ≤ v ≤ v*} × S³ and D_s := D ∩ {v ≤ s}, and call a solution on D_s a smooth T²-invariant
vacuum metric of the class on D_s, in the gauge, that induces the data. Suppose that to every solution g on a D_s and
every σ ∈ [1/2, s] a number y_σ(g) ≥ 0 is assigned, depending only on the restriction of g to D_σ and continuous in σ,
and that there are A, B > 0 such that:

(H1) y_s(g) ≤ A + B y_s(g)² for every solution g on every D_s;

(H2) for every k ≥ 0 there is C_k such that every solution g on a D_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s] has its
components and their derivatives of order at most k, and the components of g⁻¹, bounded by C_k on D_s, in a fixed
finite atlas of [−10, u*] × [1/2, v*] × S³;

(H3) 4AB < 1, and y_(1/2)(g) ≤ A for every solution g.

Suppose moreover that the characteristic initial value problem in the gauge has, for these data, the following three
properties.

(F1) There are s ∈ (1/2, v*] and a solution on D_s.

(F2) Two solutions on the same D_s coincide.

(F3) A solution on D_s with s < v* is the restriction of a solution on D_(s′) for some s′ ∈ (s, v*].

Then there is a solution g on D, and y_σ(g) ≤ 2A for every σ ∈ [1/2, v*].

(F1)–(F3) are the local existence, uniqueness and continuation of the characteristic problem in the gauge. For smooth
data, [[thm:std-ctg-neighbourhood]] gives a vacuum development containing a future neighbourhood of N₀ ∪ N₁ (its
proof, [CTG23, Section 4, p. 10], runs the argument of [CCTW16, Theorem 5.3] in any maximal domain of existence and
does not show that this domain is unique), and likewise for the data that a solution on D_s induces on {v = s} ∩ D
and on N₁ ∩ {v ≥ s}, which meet transversally at the sphere {u = −10, v = s}. Three further facts would give (F1)–(F3)
from it: that the T² action of the data and the reflections φ1 ↦ −φ1 and φ2 ↦ −φ2 extend to isometries of the
development, which puts the metric in the form of the class; that double-null coordinates on that neighbourhood, with u
constant on the outgoing null hypersurfaces through the leaves of N₀, v constant on the ingoing ones through the leaves
of N₁, and x, φ1 and φ2 constant along the outgoing generators and equal on N₀ to those of the data, cover a region
D_(s′) with s′ > s; and that a solution in the gauge is determined by its data. The first and the third rest on the
uniqueness, up to isometry, of the vacuum development of characteristic data on a neighbourhood of the whole of the two
hypersurfaces, which no result quoted in [[app:standard-results]] provides. [CP12, Section 4.3, p. 16] writes of the
characteristic problem that "Here uniqueness is understood locally, though again it is clear that unique maximal
globally hyperbolic developments should exist in the current context", and the proof of [CCTW16, Theorem 5.3, p. 55]
notes that "the question, whether a unique such maximal domain exists is irrelevant for our purposes". So (F1)–(F3) are
hypotheses of the lemma. No proof in this paper uses the lemma.

*Proof.* First, if 4AB < 1 and y ≥ 0 satisfies y ≤ A + By², then y ∉ (2A, 1/(2B)), and if moreover y ≤ 2A then
y ≤ A + 4A²B < 2A. Indeed q(y) := By² − y + A is convex with q(2A) = A(4AB − 1) < 0 and q(1/(2B)) =
(4AB − 1)/(4B) < 0, so q < 0 on [2A, 1/(2B)], an interval since 2A < 1/(2B); and 4A²B < A.

Let I be the set of s ∈ (1/2, v*] for which there is a solution g on D_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s]. If
s ∈ I and 1/2 < s′ < s, then s′ ∈ I, by restriction.

I is not empty. By (F1) there is a solution g on some D_(s₁); y_(1/2)(g) ≤ A < 2A by (H3), and y_σ(g) is continuous in
σ, so y_σ(g) ≤ 2A on [1/2, s₂] for some s₂ ∈ (1/2, s₁], and s₂ ∈ I.

I is open in (1/2, v*]. Let s ∈ I with s < v*, and g the solution on D_s. For σ ∈ (1/2, s] the restriction of g to D_σ
is a solution on D_σ, so (H1) and y_σ(g) ≤ 2A give y_σ(g) ≤ A + 4A²B < 2A; at σ = 1/2, y_(1/2)(g) ≤ A by (H3). By
(F3), g is the restriction of a solution g′ on some D_(s′), s′ > s, and since y_σ(g′) is continuous in σ and
y_s(g′) = y_s(g) < 2A, y_σ(g′) ≤ 2A on [1/2, s″] for some s″ ∈ (s, s′]. So s″ ∈ I.

I is closed. Let s_n ∈ I increase to s̄ ≤ v*, with solutions g_n on D_(s_n). By (F2), g_m restricted to D_(s_n)
is g_n for m ≥ n, so the g_n define a smooth metric g on D ∩ {v < s̄}, with y_σ(g) ≤ 2A for σ < s̄. By (H2) the
components of g and of g⁻¹ in the charts of the atlas are bounded on D ∩ {v < s̄} together with all their derivatives,
so each component and each derivative is uniformly continuous there and extends continuously to D_(s̄); the extended
components are smooth, and the extended metric is nondegenerate, since the components of g⁻¹ extend as well. The
extension is T²-invariant, of the form of the class in the gauge, vacuum and induces the data on D_(s̄), since each of
these conditions is preserved under limits of the components and their derivatives. So it is a solution ḡ on D_(s̄).
For σ ≤ s_n, y_σ(ḡ) = y_σ(g_n) ≤ 2A, since y_σ depends only on the restriction to D_σ; so y_σ(ḡ) ≤ 2A for σ < s̄,
and y_(s̄)(ḡ) ≤ 2A by the continuity of y_σ(ḡ) in σ. Hence s̄ ∈ I.

So I = (1/2, v*], and v* ∈ I is the claim. ∎

In an application y_σ(g) is a norm of g − ĝ on D_σ, ĝ an explicit approximant on D, and (H1) is an a priori estimate
with A = F ε_r and B = F G: ε_r is the size of the residual of ĝ, F the constant of a linear estimate for the problem
linearised about ĝ, and G the constant of its quadratic remainder. The condition 4AB < 1 of (H3) is then the closing
condition 4F²G ε_r < 1.

**Remark {#rem:tl5-beyond}** (Why no existence is claimed beyond the seed.) [[lem:tl5-continuation]] concerns smooth
data and assumes (F1)–(F3), which this paper does not establish. The data of [[def:tl5-problem]] are not smooth: env is
C³ and not C⁴ at v = 1/2 and v = 7/2 ([[rem:envelope-regularity]]), and so are the fields P and Q on N there.
[[thm:std-ctg-neighbourhood]] is stated in the smooth category, its authors adding that it remains true in suitable
Sobolev spaces; a version of [[lem:tl5-continuation]] for data of finite regularity is not stated in this paper.
Whatever the data, (H1) is an estimate on all of D, axes included. An estimate for the linearised problem on a
truncated domain of dependence that avoids the axes would not give (H1): no such domain contains a region of the form
D_s, since D_s contains the axes. The residual bounds of [[sec:tl5-residuals]] hold at points and on boxes of the
region Π of [[eq:tl5-region]], which is not of the form D_s, and are not bounds of a norm over a region D_s. So
(H1)–(H3) are established in this paper for no region D with v* > 1/2, and no existence beyond v = 1/2 is claimed.

**Remark {#rem:tl5-constants}** (Numerical observation.) Write the vacuum equations of the class as three-dimensional
gravity for the rescaled orbit metric of [[prop:reduction]] coupled to its two waves, in a null frame of that metric,
and linearise them about a metric of the class. A Grönwall argument for the energies of the linear system on a domain
of dependence truncated to avoid the axes would bound them by F² times the energies of their data and sources, with
F² = exp(2∫a_o du + 2∫a_i dv), where a_o(u) and a_i(v) are the largest, over the unknowns measured on outgoing and on
ingoing cones, of the sums of the absolute values of the coefficients with which each unknown enters. On a computed
solution at the first seed, over |x| ≤ 1/2 on the (u, v)-rectangle of [[def:tl5-chart]], where no such truncated
domain exists, so that no such bound applies, this number evaluates to F² ≈ 10^138, and to about 10^66.9 with weights
in the energy norms; toward the axes the coefficients grow like the inverse distance to the axis, and with the band
widened to |x| ≤ 0.95 the figure is about 10^1916. The couplings of the coefficients across a cut in the angular
Chebyshev degree do not depend on the cut beyond the degree of the coefficient, since
T_j T_k = (T_(j+k) + T_(|j−k|))/2, and on the computed coefficients they are of the coefficients' own size, so a Schur
complement estimate on the high angular modes does not lower the constant at any angular resolution. At F² = 10^66.9
the closing condition 4F²G ε_r < 1 asks a residual ε_r of order 10⁻⁶⁸/G, against the bounds 3.73 × 10⁻⁵ at points and
5.0 × 10⁻⁴ on sub-boxes of [[prop:tl5-points]] and [[prop:tl5-boxes-second]]. No proof uses these observations.
