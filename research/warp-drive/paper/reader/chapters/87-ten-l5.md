## At the prescribed wavelength 10 l5 {#ch:ten-l5}

[[thm:main]] is a statement for small λ. This chapter treats the problem at the prescribed wavelength λ = 10 l5, at
two seeds, with the envelope sin⁴(π(v − 1/2)/3) on [1/2, 7/2]. That envelope is C³ and not C⁴, so [[thm:main]] does
not apply to it at any λ ([[rem:envelope-regularity]]); for the smooth envelope of [[def:lambda0-point]], whose
parameters are those of the first seed below, the threshold λ0 that the proof of [[thm:main]] delivers lies below
0.0024433 in the operator norm ([[prop:lambda0]]), and 10 l5 exceeds it by a factor above 409. At 10 l5 the wavelength
is not small against the curvature length ([[prop:tl5-scales]]), and the problem is posed as a characteristic initial
value problem in double-null gauge: the seed on an ingoing cone, the incoming wave on an outgoing one.

The chapter proves the following. The problem has a solution where the solution is the seed and, for u* < u₀ (u* and u₀
as in [[def:tl5-problem]] and [[lem:tl5-seed]] (a)), also on a strip 1/2 ≤ v ≤ s beyond it, whose width is not
estimated; that solution is smooth beyond the seed and of class C³ ([[thm:ten-l5]]). Wherever a vacuum solution exists
in the gauge with the seed's transverse derivative of R on the seed's cone, its leaves inside the seed's horizon
generator are outer trapped, and its T²-invariant marginally outer trapped sections lie at or outside that generator
and, under a condition on the generators through them, in an explicit band ([[prop:tl5-leaves]], [[cor:tl5-mots]]). On
the data cone the outgoing constraint has exact solutions, and an explicit approximant satisfies it up to an explicit
residual ([[sec:cone-approximant]]). Two explicit metrics of the class on a region beyond the seed have explicit
residual bounds ([[sec:tl5-residuals]]). For smooth data the characteristic problem in the gauge has local existence,
uniqueness and continuation ([[thm:tl5-cip]]); the data at 10 l5 are smooth on two stages, to each of which it applies
([[cor:tl5-cip-staged]]), and a continuation lemma states what existence on a given region beyond the seed would further
need ([[lem:tl5-continuation]]). No existence is proved beyond the strip, and [[rem:tl5-beyond]] says why. Numerical
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
values of each seed, one at an end node and one where G₁ and F are largest, are printed as checkpoints with the tables
of [[sec:cone-table-n1]] and [[sec:cone-table-n2]]. ∎

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
[[eq:cone-ricvv]]. The constraint Ric_vx determines the shift on the cone; [[lem:tl5-cip-shift]] solves it.

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
C₀ := {v = 0, −10 ≤ u ≤ u*} and N := {u = −10, v ≥ 0}. The data on C₀ are those of the seed: R = −u, P = Q = β = 0 and
e^(2W) = 1/2. The data on N are W, P and Q of [[eq:cone-data]], with r the parameter of [[eq:cone-v]], and the R of
[[prop:cone-exact]]; on N ∩ {v ≤ 1/2} the shift is β = 0, and beyond it is the solution of the constraint Ric_vx = 0
with β = ∂_vβ = 0 at v = 1/2, which exists, is unique, is smooth in x and of class C⁴ in v, and is smooth on
N ∩ {1/2 ≤ v ≤ 7/2} and on N ∩ {v ≥ 7/2} ([[lem:tl5-cip-shift]] and the paragraph after it). A solution on a set
D ⊂ {−10 ≤ u ≤ u*, v ≥ 0} × S³ is a T²-invariant vacuum metric of the class in the gauge on D, whose R, P, Q, W and β
are C² functions of (u, v, x) on D and whose values on D ∩ C₀ and D ∩ N are the data.

On N ∩ {v ≤ 1/2}, r ≤ r_s, so the R of [[prop:cone-exact]] is r and the data there are the seed's ([[lem:tl5-seed]]
(d)).

**Theorem {#thm:ten-l5}** (The prescribed wavelength 10 l5.) At either seed of [[def:tl5-seeds]]:

(a) there is no separation of scales: on x_K = 1 the wavelength λ = 10 l5 is 10 times the curvature length, and at the
horizon it is more than 2.91 times it at the first seed and more than 0.92 times it at the second;

(b) the characteristic problem of [[def:tl5-problem]] has a solution where the solution is the seed: on
D⁰ := ({−10 ≤ u ≤ u*, 0 ≤ v ≤ 1/2} ∩ D_seed) × S³, which is all of {−10 ≤ u ≤ u*, 0 ≤ v ≤ 1/2} × S³ when u* < u₀
([[lem:tl5-seed]] (a)), the seed of [[lem:tl5-seed]] is a smooth vacuum metric of the class in the gauge that induces
the data on D⁰ ∩ C₀ and on D⁰ ∩ N; and when u* < u₀ the problem also has a solution beyond the seed: for some
s ∈ (1/2, 7/2] there is a solution on {−10 ≤ u ≤ u*, 0 ≤ v ≤ s} × S³ that is the seed for v ≤ 1/2 and smooth for
v ≥ 1/2, of class C³, and no other solution there has smooth restrictions to {v ≤ 1/2} and to {v ≥ 1/2};

(c) for every solution on a set D as in [[prop:tl5-leaves]] whose transverse derivative ∂_vR on C₀ is the seed's,
every leaf with −1 < u < 0 is outer trapped where it meets D; every T²-invariant marginally outer trapped section of an
ingoing cone contained in the interior of D has its innermost point at u ≤ −1; and every such section for which D
contains the two generator segments named in [[cor:tl5-mots]] (c) lies in the band of [[cor:tl5-mots]] (c), between
the infimum and the supremum of u over the zeros of the leaves' expansion on that cone in D.

Existence beyond v = 1/2 is asserted only on the strip of (b), whose width s − 1/2 is not estimated:
[[lem:tl5-continuation]] states what existence on a given region would need, and [[rem:tl5-beyond]] why the bounds
proved in this chapter do not provide it.

*Proof.* (a) is [[prop:tl5-scales]]. (b) D⁰ ⊂ D_seed × S³, so by [[lem:tl5-seed]] (b) and (c) the seed is a smooth
vacuum metric of the class in the gauge on D⁰, and by [[lem:tl5-seed]] (d) and the sentence after [[def:tl5-problem]] it
induces the data on D⁰ ∩ C₀ and D⁰ ∩ N. When u* < u₀, [[cor:tl5-cip-staged]] (a) and (F1) of [[thm:tl5-cip]] give
s ∈ (1/2, 7/2] and a solution of the first stage on [−10, u*] × [1/2, s] × S³, and by [[cor:tl5-cip-staged]] (c) it
continues the seed to a solution of class C³ on {−10 ≤ u ≤ u*, 0 ≤ v ≤ s} × S³, the only one there with smooth
restrictions to {v ≤ 1/2} and to {v ≥ 1/2}. (c) is [[prop:tl5-leaves]] and [[cor:tl5-mots]] (b) and (c), since θ_S = 0
on a marginally outer trapped section. ∎

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
[3.715, 3.728] × 10⁻⁵. In particular 2.41 × 10⁻³, the value of |f^(1)_ll| at (−23/24, 23/24, −21/32) rounded to
three significant figures, is not an upper bound for |f^(1)_ll| on G; the least number with three significant
figures that is an upper bound is 2.42 × 10⁻³.

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

### The characteristic problem in the gauge {#sec:tl5-cip}

This section proves the local existence, uniqueness and continuation of the characteristic problem in the gauge for
smooth data ([[thm:tl5-cip]]); these are the properties (F1)–(F3) that [[lem:tl5-continuation]] uses. Uniqueness is
proved for vacuum metrics in double-null form, without any symmetry ([[prop:tl5-cip-unique]]): two of them that agree
along the two data hypersurfaces have the same derivatives of all orders there ([[lem:tl5-cip-jets]]), so one smooth
extension across the hypersurfaces serves both, and local harmonic coordinates reduce the comparison to the uniqueness
of the Cauchy problem for linear wave equations. Existence comes from [[thm:std-ctg-neighbourhood]], through double-null
coordinates on its development ([[lem:tl5-cip-chart]]); the symmetry of the solution, and with it the form of the class,
follows from the uniqueness. Everything is done on the five-manifold, in charts of S³, so the axes play no special role
([[rem:tl5-cip-axes]]). The data of [[def:tl5-problem]] are not smooth, but they are smooth on the stages 1/2 ≤ v ≤ 7/2
and v ≥ 7/2 of the outgoing cone; the theorem applies to each stage, and the solutions glue to the seed and to each
other in class C³ ([[cor:tl5-cip-staged]]).

#### Metrics in double-null form {#sec:tl5-cip-form}

Write 𝒬 := ℝ² × S³, with coordinates (u, v) on ℝ² and S³ ⊂ ℂ² the unit sphere, and on S³ the function
x := |z₁|² − |z₂|² and the angles φ_i := arg z_i, which with x form a chart of {|x| < 1}. The group G = O(2) × O(2) of
[[sec:class]] acts on S³ ⊂ ℂ² = ℝ² × ℝ², hence on 𝒬, trivially on (u, v); in the chart (x, φ1, φ2) the rotations are
φ_i ↦ φ_i + c_i and the reflections φ_i ↦ −φ_i. A box is a set I × J × S³ with I, J compact intervals; a function, a
tensor field or a map on a box is smooth if all its partial derivatives, taken in charts at interior points, extend
continuously to the box. We use coordinates (u, v, y^A), y a chart of S³, with indices A, B, C, D, E running over 1, 2,
3; the spheres {u, v constant} are the leaves.

**Definition {#def:tl5-cip-null}** (Double-null form.) A smooth metric g on a box, or on an open subset of 𝒬, is in
double-null form if g(∂_v, ∂_v) = 0, g(∂_v, X) = 0 for every X tangent to the leaves, g⁻¹(dv, dv) = 0,
g(∂_u, ∂_v) < 0, and the metric γ that g induces on the leaves is positive definite.

**Lemma {#lem:tl5-cip-form}** (The form.) (a) A smooth metric g is in double-null form if and only if, in every chart
y of S³,

    g = −2e^(2W) (du ⊗ dv + dv ⊗ du) + γ_AB (dy^A − b^A du) ⊗ (dy^B − b^B du)                  {#eq:tl5-cip-form}

with W, b^A and γ_AB smooth and γ positive definite; then g is Lorentzian, and with e₃ := ∂_u + b^A∂_A and e₄ := ∂_v,

    g⁻¹ = −(e^(−2W)/2) (e₃ ⊗ e₄ + e₄ ⊗ e₃) + γ^(AB) ∂_A ⊗ ∂_B.

(b) If g is in double-null form and G-invariant, then on {|x| < 1} it is a metric of the class in the gauge of
[[sec:cone-constraint]], with β := b^x and with R > 0, P and Q given by R⁶ := 16 det γ, e^(2P) := 2γ_(φ1φ1)/(R²(1 + x))
and e^(2Q) := 2γ_(φ2φ2)/(R²(1 − x)), where γ and det γ are taken in the chart (x, φ1, φ2). Conversely, a smooth metric
of the class in the gauge is G-invariant and in double-null form.

*Proof.* (a) Put θ^A := dy^A − b^A du; the frame (e₃, e₄, ∂_A) is dual to (du, dv, θ^A). If g has the form
[[eq:tl5-cip-form]], then g(∂_v, ∂_v) = 0, g(∂_v, ∂_A) = 0 and g(∂_u, ∂_v) = −2e^(2W) < 0; in this frame g is block
diagonal, with the block ((0, −2e^(2W)), (−2e^(2W), 0)) on (e₃, e₄) and γ on the leaves, so g is Lorentzian, its inverse
is the one stated, and g⁻¹(dv, dv) = 0 since dv(e₃) = dv(∂_A) = 0. Conversely, let g be in double-null form, and define
W and b by g(∂_u, ∂_v) = −2e^(2W) and b^A := −γ^(AB) g(∂_u, ∂_B). Then g minus the right side of [[eq:tl5-cip-form]] is
c du ⊗ du with c := g(∂_u, ∂_u) − γ_AB b^A b^B, so in the frame above the (e₃, e₄) block of g is
((c, −2e^(2W)), (−2e^(2W), 0)); its inverse has the entry −c e^(−4W)/4 in the place of (dv, dv), and g⁻¹(dv, dv) = 0
gives c = 0.

(b) The rotations act by translations of φ1 and φ2, so the components of g in the chart (u, v, x, φ1, φ2) do not depend
on φ1, φ2. The reflection φ1 ↦ −φ1 maps ∂_(φ1) to −∂_(φ1) and fixes ∂_u, ∂_v, ∂_x and ∂_(φ2), so its invariance gives
g(∂_(φ1), Y) = 0 for these Y; likewise for φ2. Hence γ is diagonal and b^(φi) = −γ^(φiφi) g(∂_u, ∂_(φi)) = 0. With R,
P, Q as stated, γ_(φ1φ1) = R² ((1 + x)/2) e^(2P), γ_(φ2φ2) = R² ((1 − x)/2) e^(2Q), and
γ_xx = det γ/(γ_(φ1φ1)γ_(φ2φ2)) = R² e^(−2(P + Q))/(4(1 − x²)) = G_x; so [[eq:tl5-cip-form]] is the metric of
[[sec:cone-constraint]], in which −4e^(2W) du dv stands for −2e^(2W) (du ⊗ dv + dv ⊗ du). Conversely, that metric has
the form [[eq:tl5-cip-form]] on {|x| < 1}, with components independent of φ1, φ2 and with no term that contains exactly
one dφ_i, so it is invariant under G there, and on the whole box by continuity; it is in double-null form on {|x| < 1}
by (a), and at the axes by continuity, γ being positive semi-definite there and nondegenerate, as a vector X tangent to
a leaf with γ(X, ·) = 0 has g(X, ·) = 0. ∎

**Lemma {#lem:tl5-cip-axis}** (Regularity at the axes.) (a) Let g be a smooth G-invariant metric in double-null form on
a box I × J × S³. Then the functions R, P, Q, W and β of [[lem:tl5-cip-form]] (b) are the restrictions to
I × J × (−1, 1) of smooth functions of (u, v, x) on I × J × [−1, 1].

(b) Let J be an interval, k a nonnegative integer or ∞, and R > 0, P, Q functions on J × [−1, 1] whose partial
derivatives ∂_v^j∂_x^l with j ≤ k exist and are continuous, with P + 2Q = 0 at x = 1 and 2P + Q = 0 at x = −1. Then the
metrics

    R² e^(−2(P + Q)) dx²/(4(1 − x²)) + R² ((1 + x)/2) e^(2P) dφ1² + R² ((1 − x)/2) e^(2Q) dφ2²

on {|x| < 1} ⊂ S³, one for each v ∈ J, extend to Riemannian metrics on S³ whose components in every chart y of S³ have
continuous partial derivatives ∂_v^j∂_y^α for j ≤ k.

*Proof.* (a) G acts transitively on each set {x = c} ⊂ S³, a torus or, for c = ±1, a circle, so a G-invariant function f
on the box is f = F(u, v, x) for a function F on I × J × [−1, 1]. Let ω(ϑ) := (cos ϑ, sin ϑ) ∈ S³ ⊂ ℂ², so that
x(ω(ϑ)) = cos 2ϑ, and E(u, v, ϑ) := f(u, v, ω(ϑ)), a smooth function on I × J × ℝ. The rotations (z₁, z₂) ↦ (−z₁, z₂)
and (z₁, z₂) ↦ (z₁, −z₂) map ω(ϑ) to ω(π − ϑ) and to ω(−ϑ), so E is even about ϑ = 0 and about ϑ = π/2, and ∂_ϑE is odd
about both. Hence ∂_ϑE(u, v, ϑ) = ϑ ∫₀¹ ∂_ϑ²E(u, v, tϑ) dt and sin 2ϑ = ϑ ∫₀¹ 2 cos(2tϑ) dt, the last integral being
positive for |ϑ| < π/4, and likewise about π/2; so Ẽ := −∂_ϑE/(2 sin 2ϑ) extends from 0 < ϑ < π/2 to a smooth function
on I × J × (−π/4, 3π/4), again even about 0 and about π/2. For 0 < ϑ < π/2, x = cos 2ϑ gives
∂_xF(u, v, cos 2ϑ) = Ẽ(u, v, ϑ). By induction, ∂_x^l F(u, v, cos 2ϑ) = E_l(u, v, ϑ) with E_l smooth and even about 0 and
π/2, so every partial derivative ∂_u^i∂_v^j∂_x^l F, as a function of (u, v, ϑ) with 0 < ϑ < π/2, extends continuously to
0 ≤ ϑ ≤ π/2; by the mean value theorem, F extended by continuity to x = ±1 is smooth on I × J × [−1, 1].

W = (ln(−g(∂_u, ∂_v)/2))/2 and β = dx(b), with b^A = −γ^(AB) g(∂_u, ∂_B), are smooth and G-invariant, since G acts on S³
alone and preserves ∂_u, ∂_v and the leaves. With the round metric
γ₀ := dx²/(4(1 − x²)) + ((1 + x)/2) dφ1² + ((1 − x)/2) dφ2² of S³, whose determinant in the chart (x, φ1, φ2) is 1/16,
R³ = (det γ/det γ₀)^(1/2) in every chart, a smooth positive G-invariant function. The field ∂_(φ1), which generates the
rotations of z₁, is smooth on S³ and vanishes exactly on {x = −1}; so γ(∂_(φ1), ∂_(φ1)) is smooth and G-invariant, equal
to K₁(u, v, x) with K₁ smooth on I × J × [−1, 1] and zero at x = −1, and K₁ = (1 + x) K with
K := ∫₀¹ ∂_xK₁(u, v, −1 + t(1 + x)) dt smooth. By compactness γ ≥ c γ₀ for some c > 0, so K ≥ c
γ₀(∂_(φ1), ∂_(φ1))/(1 + x) = c/2, and e^(2P) = 2K/R² shows that P is smooth. Likewise for Q, with ∂_(φ2) and x = 1.

(b) On {|x| < 1}, x and the angles form charts, in which the components are R² e^(−2(P + Q))/(4(1 − x²)),
R² ((1 + x)/2) e^(2P) and R² ((1 − x)/2) e^(2Q). Near {x = 1}, where z₁ ≠ 0, take the chart (φ1, ξ¹, ξ²) with
z₂ = ξ¹ + iξ², and put ρ² := |z₂|², so that 1 − x = 2ρ². With A := R² e^(−2(P + Q))/(1 − ρ²), B := R² e^(2Q) and
C := R² (1 − ρ²) e^(2P), taken at x = 1 − 2ρ², the metric is A dρ² + B ρ² dφ2² + C dφ1², that is

    B ((dξ¹)² + (dξ²)²) + ((A − B)/(4ρ²)) (d(ρ²))² + C dφ1²,

since dρ² + ρ² dφ2² = (dξ¹)² + (dξ²)² and 4ρ² dρ² = (d(ρ²))². As functions of (v, ρ²), A, B and C have continuous
derivatives ∂_v^j∂_(ρ²)^l for j ≤ k, and A = B at ρ = 0, since P + 2Q = 0 at x = 1; so
(A − B)/ρ² = ∫₀¹ ∂₂(A − B)(v, tρ²) dt, ∂₂ denoting the derivative in the second variable, has such derivatives as well.
With ρ² = (ξ¹)² + (ξ²)², the components in this chart have continuous derivatives ∂_v^j∂_ξ^α for j ≤ k, and the metric
is positive definite, equal to B ((dξ¹)² + (dξ²)²) + C dφ1² at ρ = 0. Near {x = −1} the same holds with z₁ and z₂
exchanged and 2P + Q = 0. Other charts differ from these by diffeomorphisms of S³. ∎

**Lemma {#lem:tl5-cip-causal}** (Causal structure.) Let g be in double-null form on an open set 𝒪 ⊂ 𝒬, time-oriented
so that e₃ and e₄ are future directed.

(a) For every future directed causal vector X ≠ 0, du(X) ≥ 0, dv(X) ≥ 0, du(X) + dv(X) > 0 and
γ(X′, X′) ≤ 4e^(2W) du(X) dv(X), where X′ := X − du(X) e₃ − dv(X) e₄ is tangent to the leaves.

(b) Let ψ₁, ψ₂ be smooth functions of one variable with ψ₁′, ψ₂′ ≥ 0, and τ := u + v + ψ₁(u) + ψ₂(v). Then τ is
strictly increasing along future directed causal curves and g⁻¹(dτ, dτ) < 0, so every level set of τ is a smooth
spacelike hypersurface, acausal in 𝒪. Each of the sets {u < a}, {v < b} and {τ < c}, and every union of such sets, is a
past set: a past directed causal curve that starts in it stays in it.

(c) e₄ = −2e^(2W) ∇u and e₃ = −2e^(2W) ∇v, and ∇_(∇w)∇w = 0 for w = u, v; so the integral curves of e₄ and of e₃ are
null pregeodesics.

*Proof.* (a) Write X = λe₃ + μe₄ + X′ with λ = du(X), μ = dv(X). Then g(X, X) = −4e^(2W)λμ + γ(X′, X′) ≤ 0, so
λμ ≥ γ(X′, X′)/(4e^(2W)) ≥ 0. As e₃ + e₄ is future directed and timelike, g(X, e₃ + e₄) = −2e^(2W)(λ + μ) < 0, so
λ + μ > 0, and with λμ ≥ 0 both are non-negative. (b) dτ(X) = (1 + ψ₁′)du(X) + (1 + ψ₂′)dv(X) > 0 by (a), and by the
inverse in [[lem:tl5-cip-form]] (a), g⁻¹(du, du) = g⁻¹(dv, dv) = 0 and g⁻¹(du, dv) = −e^(−2W)/2, so
g⁻¹(dτ, dτ) = −(1 + ψ₁′)(1 + ψ₂′) e^(−2W) < 0. A causal curve meets a level set of τ at most once, and along a past
directed causal curve u, v and τ do not increase. (c) By the inverse in [[lem:tl5-cip-form]] (a), ∇u = −(e^(−2W)/2) e₄
and ∇v = −(e^(−2W)/2) e₃. For w = u, v, g(∇w, ∇w) = 0 everywhere, and as ∇∇w is symmetric,
g(∇_(∇w)∇w, Y) = ∇∇w(Y, ∇w) = Y(g(∇w, ∇w))/2 = 0 for every Y. ∎

**Lemma {#lem:tl5-cip-frame}** (The vacuum equations in double-null form.) Let g be in double-null form, with
[[eq:tl5-cip-form]] in a chart y, e₃ := ∂_u + b^A∂_A and e₄ := ∂_v, and put

    χ_AB := ∂_vγ_AB/2,    χ̲_AB := (e₃γ_AB + γ_CB ∂_Ab^C + γ_AC ∂_Bb^C)/2,    ζ_A := e^(−2W) γ_AB ∂_vb^B/4,

with indices raised by γ, trχ := χ_A^A, |χ|² := χ_A^B χ_B^A, ⟨χ, χ̲⟩ := χ_A^B χ̲_B^A, likewise for χ̲, and |dW|² :=
γ^(AB) ∂_AW ∂_BW, ⟨ζ, dW⟩ := γ^(AB) ζ_A ∂_BW, |ζ|² := γ^(AB) ζ_A ζ_B. Let ∇̸, Γ̸, Ric̸ and Δ̸ be the Levi-Civita
connection, its Christoffel symbols, the Ricci tensor and the Laplacian of γ on the leaves, and put (div̸ χ)_A :=
γ^(BC) ∇̸_B χ_CA, div̸ ζ := γ^(AB) ∇̸_A ζ_B, (ℒ₃ζ)_A := e₃(ζ_A) + ∂_Ab^B ζ_B and (ℒ₃χ)_AB := e₃(χ_AB) + ∂_Ab^C χ_CB +
∂_Bb^C χ_AC. Then

    Ric(e₄, e₄) = −∂_v trχ + 2∂_vW trχ − |χ|²,
    Ric(e₃, e₃) = −e₃(trχ̲) + 2e₃(W) trχ̲ − |χ̲|²,
    Ric(e₄, ∂_A) = ∂_vζ_A + trχ ζ_A − ∂_A∂_vW + trχ ∂_AW + (div̸ χ)_A − ∂_A trχ,
    Ric(e₃, ∂_A) = −(ℒ₃ζ)_A − trχ̲ ζ_A − ∂_A(e₃W) + trχ̲ ∂_AW + (div̸ χ̲)_A − ∂_A trχ̲,
    Ric(∂_A, ∂_B) = (e^(−2W)/2) (∂_vχ̲_AB + (ℒ₃χ)_AB + trχ χ̲_AB + trχ̲ χ_AB − 2χ_A^C χ̲_CB − 2χ̲_A^C χ_CB)
                    − 2∇̸_A∇̸_BW − 2∂_AW ∂_BW − 2ζ_A ζ_B + Ric̸_AB,
    Ric(e₃, e₄) = −2e₃(∂_vW) − e₃(trχ) − ⟨χ, χ̲⟩ + 2e^(2W) (Δ̸W − div̸ ζ + 2|dW|² − 4⟨ζ, dW⟩ − 2|ζ|²).
                                                                                                {#eq:tl5-cip-ricci}

*Proof.* The commutators of the frame are [e₄, e₃] = ∂_vb^A ∂_A, [∂_A, e₃] = ∂_Ab^B ∂_B and [∂_A, e₄] = [∂_A, ∂_B] = 0;
the products are g(e₃, e₄) = −2e^(2W) and g(∂_A, ∂_B) = γ_AB, all others vanishing. Put a_A := ∂_AW + ζ_A and
a̲_A := ∂_AW − ζ_A, and write ∇_3 := ∇_(e₃), ∇_4 := ∇_(e₄), ∇_A := ∇_(∂_A). The Koszul formula
2g(∇_XY, Z) = Xg(Y, Z) + Yg(X, Z) − Zg(X, Y) + g([X, Y], Z) − g([X, Z], Y) − g([Y, Z], X), evaluated on the frame, gives

    ∇_4e₄ = 2∂_vW e₄,    ∇_3e₃ = 2e₃(W) e₃,    ∇_4e₃ = 2e^(2W) a^A ∂_A,    ∇_3e₄ = 2e^(2W) a̲^A ∂_A,
    ∇_Ae₄ = ∇_4∂_A = χ_A^B ∂_B + a_A e₄,    ∇_Ae₃ = χ̲_A^B ∂_B + a̲_A e₃,    ∇_3∂_A = ∇_Ae₃ − ∂_Ab^B ∂_B,
    ∇_A∂_B = Γ̸^C_AB ∂_C + (e^(−2W)/2) (χ̲_AB e₄ + χ_AB e₃).                                    {#eq:tl5-cip-connection}

For instance 2g(∇_Ae₄, e₃) = ∂_A g(e₄, e₃) − g([∂_A, e₃], e₄) − g([e₄, e₃], ∂_A) = −2∂_A e^(2W) − γ_AB ∂_vb^B, which is
−4e^(2W) a_A, and 2g(∇_Ae₄, ∂_B) = ∂_vγ_AB; the other entries follow in the same way, and
∇_4e₃ − ∇_3e₄ = [e₄, e₃] checks the third and fourth. With R(Z, X)Y := ∇_Z∇_XY − ∇_X∇_ZY − ∇_([Z, X])Y,

    Ric(X, Y) = θ³(R(e₃, X)Y) + θ⁴(R(e₄, X)Y) + γ^(CD) g(R(∂_C, X)Y, ∂_D),

where θ³(V) := −e^(−2W) g(V, e₄)/2 and θ⁴(V) := −e^(−2W) g(V, e₃)/2 are the components of V along e₃ and e₄.

For Ric(e₄, e₄) the first two terms vanish, R being antisymmetric in its last two slots after lowering. The ∂_D
component of R(∂_C, e₄)e₄ = ∇_C(2∂_vW e₄) − ∇_4(χ_C^B ∂_B + a_C e₄), paired by g, is
2∂_vW χ_CD − γ_BD ∂_vχ_C^B − χ_C^B χ_BD, and the contraction with γ^(CD) is the first line. For Ric(e₃, e₃) the same
steps with e₃, χ̲, a̲ give the second line: the term −∇_([∂_C, e₃])e₃ = −∂_Cb^B ∇_Be₃ and the term −∂_Bb^E ∂_E of ∇_3∂_B
contribute −∂_Cb^B χ̲_B^C and +χ̲_E^B ∂_Bb^E to the contraction, which cancel.

For Ric(e₄, ∂_A): θ³(R(e₃, ∂_A)e₄) = 0; the e₄ component of R(e₄, ∂_A)e₄ = ∇_4(χ_A^B ∂_B + a_A e₄) − ∇_A(2∂_vW e₄) is
χ_A^B a_B + ∂_va_A − 2∂_A∂_vW; and since g(∇_C∇_Ae₄, ∂_D) = γ_BD ∂_Cχ_A^B + γ_ED Γ̸^E_CB χ_A^B + a_A χ_CD, the
contraction of R(∂_C, ∂_A)e₄ is (div̸ χ)_A − ∂_A trχ + a_A trχ − χ_A^B a_B. The sum, with a = dW + ζ, is the third
line. For Ric(e₃, ∂_A) the same steps, with the extra term −∇_([e₃, ∂_A])e₃ = ∂_Ab^B ∇_Be₃, give
θ³(R(e₃, ∂_A)e₃) = χ̲_A^B a̲_B + e₃(a̲_A) + ∂_Ab^B a̲_B − 2∂_A(e₃W) and the contraction
(div̸ χ̲)_A − ∂_A trχ̲ + a̲_A trχ̲ − χ̲_A^B a̲_B; as e₃(∂_AW) + ∂_Ab^B ∂_BW = ∂_A(e₃W), the sum is the fourth line.

For Ric(∂_A, ∂_B): from g(∇_A∂_B, e₃) = −χ̲_AB, g(∇_4∂_B, e₃) = −2e^(2W) a_B and [[eq:tl5-cip-connection]],

    θ⁴(R(e₄, ∂_A)∂_B) = (e^(−2W)/2) (∂_vχ̲_AB − χ_B^C χ̲_AC) − ∇̸_Aa_B − 2∂_AW a_B + a_B a̲_A,

and in the same way, the terms of [e₃, ∂_A] and of ∇_3∂_B combining into ℒ₃χ,

    θ³(R(e₃, ∂_A)∂_B) = (e^(−2W)/2) ((ℒ₃χ)_AB − χ̲_B^C χ_AC) − ∇̸_Aa̲_B − 2∂_AW a̲_B + a̲_B a_A;

the contraction of R(∂_C, ∂_A)∂_B is, by the last line of [[eq:tl5-cip-connection]],
Ric̸_AB + (e^(−2W)/2)(trχ χ̲_AB + trχ̲ χ_AB − χ_A^C χ̲_CB − χ̲_A^C χ_CB). Since χ_B^C χ̲_AC = χ̲_A^C χ_CB,
a + a̲ = 2dW and a_B a̲_A + a̲_B a_A = 2∂_AW ∂_BW − 2ζ_A ζ_B, the sum is the fifth line.

For Ric(e₃, e₄): θ³(R(e₃, e₃)e₄) = 0, and R(e₄, e₃)e₄ = ∇_4(2e^(2W) a̲^B ∂_B) − ∇_3(2∂_vW e₄) − ∂_vb^B ∇_Be₄ has, as
g(∇_3e₄, e₃) = 0 and ∂_vb^B = 4e^(2W) ζ^B, the e₄ component 2e^(2W) a̲^B a_B − 2e₃(∂_vW) − 4e^(2W) ζ^B a_B; the
contraction of R(∂_C, e₃)e₄ = ∇_C(2e^(2W) a̲^B ∂_B) − ∇_3(χ_C^B ∂_B + a_C e₄) − ∂_Cb^B ∇_Be₄ is
2e^(2W)(div̸ a̲ + 2⟨dW, a̲⟩) − e₃(trχ) − ⟨χ, χ̲⟩ − 2e^(2W) ⟨a, a̲⟩, the two terms in ∂b cancelling as before. With
div̸ a̲ = Δ̸W − div̸ ζ, the sum is the sixth line. ∎

#### Data, constraints and the shift {#sec:tl5-cip-data}

**Definition {#def:tl5-cip-data}** (Data in the gauge.) Let u* ∈ (−10, 0) and v* > 1/2, and put
N₀ := [−10, u*] × {1/2} × S³, N₁ := {−10} × [1/2, v*] × S³, N := N₀ ∪ N₁ and S := N₀ ∩ N₁. Characteristic data in
the gauge on N are a field g_N that assigns to every p ∈ N a symmetric bilinear form on T_p𝒬, whose components in the
coordinates (u, v, y) are smooth functions on N₀ and on N₁, which is G-invariant and which satisfies at every point the
conditions of [[def:tl5-cip-null]]. By [[lem:tl5-cip-form]], g_N amounts to functions W, b^A, γ_AB on N in every
chart, and on {|x| < 1} to functions R > 0, P, Q, W and β of (u, x) on N₀ and of (v, x) on N₁. A metric g on a set that
contains a part N′ of N induces the data on N′ if g = g_N at every point of N′. The data satisfy the characteristic
constraints if

    Ric(e₄, e₄) = 0  and  Ric(e₄, ∂_A) = 0  on N₁,      Ric(e₃, e₃) = 0  on N₀.               {#eq:tl5-cip-constraints}

By [[eq:tl5-cip-ricci]] the left sides contain only derivatives of W, b, γ along N₁, respectively along N₀
(e₃ is tangent to N₀, and χ̲ contains e₃γ and ∂_Ab), so they are defined by g_N. For s ∈ (1/2, v*] we put
D_s := [−10, u*] × [1/2, s] × S³.

In the variables of [[sec:cone-constraint]], Ric(e₄, e₄) on N₁ is the right side of [[eq:cone-raychaudhuri]], the
components Ric(e₄, ∂_(φi)) vanish identically ([[lem:warped-ricci]]), and Ric(e₄, ∂_x) = 0 is the constraint on the
shift that the next lemma solves.

**Lemma {#lem:tl5-cip-shift}** (The shift constraint.) Let a G-invariant metric γ on the leaves of N₁ and a G-invariant
function W on N₁ be given, smooth in y and of class C^m in v for some m ≥ 1 (all derivatives ∂_y^α∂_v^jγ, ∂_y^α∂_v^jW
with j ≤ m continuous), and on S a G-invariant vector field b_S tangent to the leaves and a G-invariant 1-form ζ_S.
There is exactly one field b along N₁, tangent to the leaves, with Ric(e₄, ∂_A) = 0 on N₁, b = b_S and ζ = ζ_S on S; it
is G-invariant, smooth in y and of class C^(m+1) in v, and smooth if γ and W are. In the variables of
[[sec:cone-constraint]], b = β ∂_x and

    Ric(∂_v, ∂_x) = (1/(4R³)) ∂_v(R³ e^(−2W) G_x ∂_vβ) − 𝔣,
    𝔣 := ∂_x∂_vW − 3 (∂_vR/R) ∂_xW + 2∂_x∂_v ln R + ∂_x∂_v(P + Q)
         + (∂_xR/R + ∂_xP + 1/(2(1 + x))) ∂_v(2P + Q) + (∂_xR/R + ∂_xQ − 1/(2(1 − x))) ∂_v(P + 2Q),
                                                                                                {#eq:tl5-cip-shift}

so that on {|x| < 1} the constraint reads ∂_v(R³ e^(−2W) G_x ∂_vβ) = 4R³ 𝔣. With x = cos 2ϑ, Ω = e^W,
γ_ϑ = R² e^(−2(P + Q)), A_c = ln(R cos ϑ) + P, A_s = ln(R sin ϑ) + Q and b = −β/(2 sin 2ϑ) in [[eq:loc-double-null]],
Ric(∂_v, ∂_x) = −Ric(∂_v, ∂_ϑ)/(2 sin 2ϑ), so the constraint is the vanishing of the second line of [[eq:loc-cone]].

*Proof.* By the third line of [[eq:tl5-cip-ricci]], Ric(e₄, ∂_A) = 0 reads

    ∂_vζ_A + trχ ζ_A = F_A,      F_A := ∂_A∂_vW − trχ ∂_AW − (div̸ χ)_A + ∂_A trχ,

where trχ, χ and F are determined by γ and W. In every chart this is, along each generator v ↦ (−10, v, y), a linear
system of ordinary differential equations for the components ζ_A, whose coefficients and right sides are continuous in v
and, together with all their derivatives in y, continuous in (v, y). It has exactly one solution with ζ = ζ_S at
v = 1/2, smooth in y by the differentiable dependence of solutions of linear equations on parameters; solutions in
overlapping charts agree, by uniqueness, as the equation is tensorial on the leaves. Since ζ′ = −trχ ζ + F, with trχ and
F of class C^(m−1) in v, ζ is of class C^m in v. Then ∂_vb^A = 4e^(2W) γ^(AB) ζ_B determines b with b = b_S on S,
uniquely, and of class C^(m+1) in v, as ζ and γ are C^m. For σ ∈ G the field σ*b solves the same problem, the equation
and the data being invariant, so σ*b = b.

In the chart (x, φ1, φ2), G-invariance makes γ diagonal and b = β ∂_x ([[lem:tl5-cip-form]] (b)), so
ζ_x = e^(−2W) G_x ∂_vβ/4 and ζ_(φi) = 0. As det γ = R⁶/16, trχ = 3∂_vR/R and ∂_vζ_x + trχ ζ_x =
R⁻³ ∂_v(R³ ζ_x). With ϰ_1 := (ln G_x)/2, ϰ_2 := (ln γ_(φ1φ1))/2, ϰ_3 := (ln γ_(φ2φ2))/2, the Christoffel symbols of the
diagonal metric γ that depends on x alone give Γ̸^C_(Cx) = ∂_xϰ_C, and (div̸ χ)_x = ∂_xχ_x^x + Σ_C Γ̸^C_(Cx) χ_x^x −
Σ_C Γ̸^C_(Cx) χ_C^C = ∂_x∂_vϰ_1 + (∂_xϰ_2 + ∂_xϰ_3) ∂_vϰ_1 − ∂_xϰ_2 ∂_vϰ_2 − ∂_xϰ_3 ∂_vϰ_3. Hence
−(div̸ χ)_x + ∂_x trχ = Σ_(i=2,3) (∂_x∂_vϰ_i + ∂_xϰ_i (∂_vϰ_i − ∂_vϰ_1)), and with ϰ_2 = ln R + (ln((1 + x)/2))/2 + P,
ϰ_3 = ln R + (ln((1 − x)/2))/2 + Q and ϰ_1 = ln R − P − Q − (ln(4(1 − x²)))/2 this is 𝔣 − ∂_x∂_vW + 3(∂_vR/R)∂_xW,
which gives [[eq:tl5-cip-shift]]. The components Ric(∂_v, ∂_(φi)) vanish by [[lem:warped-ricci]]. Finally, with
x = cos 2ϑ we have dx = −2 sin 2ϑ dϑ and G_x (dx − β du)² = 4(1 − x²) G_x (dϑ + β du/(2 sin 2ϑ))², which is the term
γ_ϑ (dϑ − b du)² of [[eq:loc-double-null]] with the stated γ_ϑ and b; the other terms match as stated, and ∂_x and
∂_ϑ differ by the factor dϑ/dx = −1/(2 sin 2ϑ). ∎

The lemma applies to the data on N of [[def:tl5-problem]]. There W is a smooth function of v, and P and Q are smooth in
x, with 2P + Q = (1 + x) m and P + 2Q = (1 − x) n by [[eq:cone-data]], so that 2P + Q = 0 at x = −1 and P + 2Q = 0 at
x = 1. In v, env is smooth on each of the intervals [0, 1/2], [1/2, 7/2] and [7/2, ∞), being there the restriction of 0,
of the entire function sin⁴(π(v − 1/2)/3) and of 0, and it is C³ on [0, ∞), its derivatives of order at most 3 vanishing
at 1/2 and 7/2; so P and Q, with all their derivatives in x, are smooth on each interval and C³ in v. R > 0
([[prop:cone-exact]] (c)) is smooth on each interval: on [r_s, r_e] it solves ∂_r²R = −w R with w smooth on
[r_s, r_e] × [−1, 1] and initial values at r_s that do not depend on x, and for r ≥ r_e it is affine in r with
coefficients smooth in x. It is C⁷ in v across v = 1/2 and v = 7/2: by the formulas in the proof of [[lem:cone-w]], A
and B are σ³ times smooth functions on [r_s, r_e], so w is σ⁶ times a smooth function, σ has simple zeros at r_s and
r_e, and ∂_r^(k+2)∂_x^l R = −∂_r^k∂_x^l(w R) vanishes there for k ≤ 5, as do the derivatives of order at least 2 in r of
r and of R(r_e, x) + ∂_rR(r_e, x)(r − r_e), while the values and first derivatives in r, with all their derivatives in
x, agree by construction. By [[lem:tl5-cip-axis]] (b), the leaf metrics on N are smooth on each interval and C³ in v on
N. At the corner, where the data are the seed's, b_S = 0 and ζ_S = 0; for v ≤ 1/2, 𝔣 = 0, as P = Q = 0 and W, R depend
on v alone there, so β = 0 for v ≤ 1/2. The solution of the lemma continues it. It is smooth on each of the intervals
[1/2, 7/2] and [7/2, ∞), by the lemma applied there, after a translation in v, with the values of b and ζ at the left
end, and C⁴ in v on N, by the lemma with m = 3 applied on all of N after a translation in v.

#### Uniqueness {#sec:tl5-cip-uniqueness}

**Lemma {#lem:tl5-cip-extend}** (Extension and gluing.) (a) Every smooth function on a box [a, b] × [c, d] × S³ is the
restriction of a smooth function on (a − 1, b + 1) × (c − 1, d + 1) × S³, given by an extension operator that is linear
and acts on the variables u, v alone; so it commutes with multiplication by functions of y and with changes of chart
of S³, and extends tensor fields component by component.

(b) Let O be an open set, a box or a product of compact intervals, w a coordinate function of a chart (w, w′) on O, and
f a continuous function on O that is smooth on O ∩ {w ≥ c} and on O ∩ {w ≤ c}, the partial derivatives of the two pieces
agreeing on {w = c}. Then f is smooth on O. If instead, for some m ≥ 1, the partial derivatives of order at most m of
the two pieces exist, extend continuously to the closed pieces and agree on {w = c}, then f is of class C^m on O.

(c) Let 𝒪 := (−10 − ε, u*) × (1/2 − ε, s) × S³ with ε > 0, and h a function on 𝒪 that vanishes on 𝒪 ∖ D_s and is
smooth on 𝒪 ∩ D_s, with every partial derivative zero on N ∩ 𝒪. Then h is smooth on 𝒪.

(d) Let O be an open subset of ℝⁿ, for instance the image of a chart, F ⊂ O a relatively closed set with interior F°,
and h a function on O that vanishes on O ∖ F°, is smooth on F°, and whose partial derivatives on F°, h included, all
extend continuously to F, with the value 0 on F ∖ F°. Then h is smooth on O, and its derivatives vanish on O ∖ F°.

*Proof.* (a) For a function f on the box and u < a put, with Seeley's sequences a_k, b_k and cut-off φ
([[thm:std-seeley]]) and ℓ := (b − a)/2, (Ef)(u, v, y) := Σ_k a_k φ(b_k (u − a)/ℓ) f(a + b_k (u − a), v, y). Each
point a + b_k(u − a) with φ(b_k(u − a)/ℓ) ≠ 0 lies in [a, b], the sum is finite for each u, and Seeley's argument, which
treats each line {(v, y)} × ℝ separately and uses only bounds of the derivatives of f on compact sets, shows that Ef,
equal to f for u ≥ a, has derivatives of all orders continuous on [a − 1, b] × [c, d] × S³; derivatives in v and y
commute with E. The same at u = b, with u replaced by −u, and then in v at c and at d, gives the extension.

(b) For each multi-index α the partial derivatives ∂^α of the two pieces define one continuous function f_α on O. At
a point of {w = c}, the difference quotients of f_α in the direction of w have one-sided limits from both sides, both
equal to f_(α + e_w); in the directions of w′ the line stays in {w = c}, where both pieces have the derivative
f_(α + e). So every f_α has continuous partial derivatives f_(α + e), and f is smooth. For the second statement the same
argument applies to the f_α with |α| < m.

(c) In the charts (u, v, y), 𝒪 ∩ D_s is relatively closed in 𝒪, the points of it that are not interior are those of
N ∩ 𝒪, and the partial derivatives of h on 𝒪 ∩ D_s are continuous and vanish on N ∩ 𝒪; so (c) is a case of (d).

(d) For a multi-index α let f_α be ∂^α h on F° and 0 on O ∖ F°; it is continuous on O by the hypothesis. Let z ∈ O and e
a coordinate direction. If z ∈ F°, or z ∉ F, then f_α = ∂^α h, respectively f_α = 0, near z, and f_α has the partial
derivative f_(α + e) at z. Let z ∈ F ∖ F°, so that f_α(z) = 0 = f_(α + e)(z), and let t ≠ 0 be small. If
f_α(z + te) ≠ 0, then z + te lies in an interval I of the segment from z to z + te that is contained in F° and has an
end point z′ not in F°, the one nearer to z, where f_α(z′) = 0; on I, f_α is differentiable along e with derivative
f_(α + e), so by the mean value theorem |f_α(z + te)| ≤ |t| sup |f_(α + e)|, the supremum over the segment. This is
o(|t|) as f_(α + e) is continuous and vanishes at z; so f_α has the partial derivative 0 = f_(α + e)(z). Hence every f_α
has the continuous partial derivatives f_(α + e), and h = f_0 is smooth. ∎

**Lemma {#lem:tl5-cip-wave}** (One-sided uniqueness for linear waves.) Let (X, h) be a time-oriented Lorentzian
manifold, Σ ⊂ X a connected smooth spacelike hypersurface that is acausal, and 𝔓 a linear differential operator on
ℝ^k-valued functions on X with smooth coefficients and principal part −h^(ij) ∂_i∂_j times the identity. Let V ⊂ X be
an open set containing D⁺(Σ), the set of points p such that every past inextendible causal curve through p meets Σ. If
w is a smooth function on V with 𝔓w = 0, and w and its derivative along a vector field transverse to Σ vanish on Σ,
then w = 0 on D⁺(Σ). The same holds with D⁻(Σ).

*Proof.* In a chart near a point of Σ in which Σ = {ξ⁰ = 0}, h^(00) ≠ 0 as Σ is spacelike, so 𝔓w = 0 gives ∂_0²w in
terms of derivatives with at most one ∂_0; by induction all derivatives of w vanish on Σ. By [[thm:std-bgp-development]]
the Cauchy development D(Σ) is an open, globally hyperbolic and causally compatible subset of X with Cauchy
hypersurface Σ, and by [[thm:std-bgp-causal]] (3) it has a Cauchy time-function t with Σ = t⁻¹(0), whose gradient is
timelike. Then D(Σ) ∩ {t ≥ 0} = D⁺(Σ) ⊂ V, and the function w̃ equal to w on {t ≥ 0} and to 0 on {t < 0} is smooth on
D(Σ) by [[lem:tl5-cip-extend]] (b), with t as a coordinate near Σ, and solves 𝔓w̃ = 0. Its support lies in J⁺(Σ), and
J⁺(Σ) ∩ J⁻(q) is compact for every q ∈ D(Σ) by [[thm:std-bgp-causal]] (4); so w̃ has past compact support. 𝔓 is
normally hyperbolic in the sense of [[def:std-normally-hyperbolic]], and [[thm:std-bgp-cauchy]] (2) gives w̃ = 0. ∎

**Lemma {#lem:tl5-cip-jets}** (Transverse derivatives on null hypersurfaces.) Let g₁ and g₂ be smooth vacuum metrics
in double-null form, with W_i, b_i, γ_i in [[eq:tl5-cip-form]] in a chart y; write ∂_v^k g_i, ∂_u^k g_i for the
derivatives of order k of (W_i, b_i, γ_i) in v, in u.

(a) Let H := [−10, u₁] × {s₀} × S³ and Z := {−10} × {s₀} × S³, and let g_i be defined on [−10, u₁] × I_i × S³, with I₁,
I₂ intervals that have s₀ as an endpoint, on the same side of s₀ or on opposite sides. If g₁ = g₂ at every point of H
and ∂_v^k g₁ = ∂_v^k g₂ on Z for every k, then ∂_v^k g₁ = ∂_v^k g₂ on H for every k, the derivatives in v at s₀ being
one-sided. The same holds for every m ≥ 0 with "for every k" replaced by "for every k ≤ m", in the hypothesis on Z
and in the conclusion.

(b) Let H′ := {−10} × [s₀, s₁] × S³ and Z := {−10} × {s₀} × S³, and let g₁, g₂ be defined on
[−10, −10 + η] × [s₀, s₁] × S³. If g₁ = g₂ at every point of H′, and ∂_u^k g₁ = ∂_u^k g₂ and ∂_u^k∂_vb₁ = ∂_u^k∂_vb₂
on Z for every k, then ∂_u^k g₁ = ∂_u^k g₂ on H′ for every k.

(c) If g₁ and g₂ are defined on D_s and g₁ = g₂ at every point of N ∩ D_s, then every partial derivative of g₁ − g₂ in
the coordinates (u, v, y) vanishes on N ∩ D_s.

*Proof.* We write δ for the difference of a quantity computed from g₁ and from g₂. Since Ric(g_i) = 0, every
derivative of every line of [[eq:tl5-cip-ricci]] vanishes.

(a) By induction on k; the case k = 0 is the hypothesis. Let k ≥ 1 and suppose ∂_v^j g₁ = ∂_v^j g₂ on H for j < k.
Then all derivatives of W, b, γ with at most k − 1 derivatives in v agree on H, being derivatives along H of functions
that agree there; we call a quantity known if it is built from these. On H, e₃ = ∂_u + b^A∂_A is the same for both
metrics, and its integral curves in H start on Z and fill H, as b is tangent to the spheres.

(i) In the fourth line of [[eq:tl5-cip-ricci]], derivatives in v occur only in ζ = e^(−2W) γ ∂_vb/4, through
−(ℒ₃ζ)_A − trχ̲ ζ_A; the other terms contain derivatives in u and y alone. Applying ∂_v^(k−1), with
[∂_v, e₃] = ∂_vb^C ∂_C, gives on H

    0 = −e^(−2W) γ_AB e₃(∂_v^k b^B)/4 + m_AB ∂_v^k b^B + n_A,

with m and n known. So δ∂_v^k b satisfies a linear homogeneous system of ordinary differential equations along the
integral curves of e₃, and vanishes on Z; hence it vanishes on H. (In each chart the system is of this form, and as it
is tensorial on the leaves, vanishing passes from chart to chart along a curve.)

(ii) In the fifth line, ∂_vχ̲ = (ℒ₃(∂_vγ) + ℒ_(∂_vb)γ)/2, where (ℒ_(∂_vb)γ)_AB := ∂_vb^C ∂_Cγ_AB + γ_CB ∂_A∂_vb^C +
γ_AC ∂_B∂_vb^C and ℒ₃ acts on 2-tensors as on χ, and (ℒ₃χ)_AB = (ℒ₃(∂_vγ))_AB/2; the other derivatives in v are those
of γ in χ and trχ, and those of b in ζ. Applying ∂_v^(k−1) gives on H

    0 = (e^(−2W)/2) (ℒ₃(∂_v^k γ))_AB + (terms linear in ∂_v^k γ, with known coefficients)
        + (terms in ∂_v^k b and ∂_C∂_v^k b, with known coefficients) + (known),

so by (i) δ∂_v^k γ satisfies a linear homogeneous system along the integral curves of e₃ and vanishes on Z, hence on
H. In the sixth line the terms with k derivatives in v after applying ∂_v^(k−1) are −2e₃(∂_v^k W),
−γ^(AB) e₃(∂_v^k γ_AB)/2, terms linear in ∂_v^k γ, and terms in ∂_v^k b and ∂_C∂_v^k b from div̸ ζ and ζ; so
e₃(δ∂_v^k W) = 0 on H, and δ∂_v^k W = 0. The step to k uses the hypothesis on Z for this k only, so the induction
stopped at m gives the second statement.

(b) By induction on k, as in (a), with "known" now meaning built from derivatives with at most k − 1 derivatives in u.
The fifth line contains no derivative in u of W or of b: derivatives in u occur only in e₃γ (in χ̲) and in e₃χ (in
ℒ₃χ). So ∂_u^(k−1) of it is, on H′, (e^(−2W)/2) ∂_v(∂_u^k γ_AB) + (terms linear in ∂_u^k γ) + (known), and δ∂_u^k γ
satisfies a linear homogeneous system along the generators v ↦ (−10, v, y) of H′ and vanishes on Z; so it vanishes.
In the sixth line ∂_u^(k−1) gives −2∂_v(∂_u^k W) plus terms in ∂_u^k γ, ∂_v∂_u^k γ and known ones, so ∂_v(δ∂_u^k W) = 0
and δ∂_u^k W = 0. The third line contains b only through ζ and no derivative in u; ∂_u^k of it is
∂_vY_A + trχ Y_A plus terms now known, with Y_A := e^(−2W) γ_AB ∂_v∂_u^k b^B/4. So δY satisfies ∂_v δY + trχ δY = 0,
δY = 0 on Z by hypothesis, hence δY = 0, ∂_v δ∂_u^k b = 0, and δ∂_u^k b = 0 as it vanishes on Z.

(c) Apply (a) with H = N₀, s₀ = 1/2 and I₁ = I₂ = [1/2, s]: on S the derivatives in v are derivatives along N₁, where
g₁ = g₂. Then apply (b) with H′ = N₁ ∩ D_s: on S the derivatives in u are derivatives along N₀, and ∂_u^k∂_vb₁ =
∂_u^k∂_vb₂ on S because ∂_vb₁ = ∂_vb₂ on N₀ by (a). Every partial derivative ∂_u^i ∂_v^j ∂_y^α of g₁ − g₂ at a point of
N₁ is a derivative along N₁ of ∂_u^i(g₁ − g₂), which vanishes there, and likewise on N₀. ∎

**Proposition {#prop:tl5-cip-unique}** (Uniqueness in double-null form.) Let s ∈ (1/2, v*] and let g₁, g₂ be smooth
vacuum metrics on D_s in double-null form with g₁ = g₂ at every point of N ∩ D_s. Then g₁ = g₂.

*Proof.* Step 1 (a common extension). By [[lem:tl5-cip-extend]] (a), applied to W₁, b₁ and γ₁ of g₁ in charts of S³,
these extend to smooth W, b, γ on (−11, u* + 1) × (−1/2, s + 1) × S³, and [[eq:tl5-cip-form]] with them defines a
smooth metric in double-null form wherever γ is positive definite, which holds on 𝒪 := (−10 − ε, u*) × (1/2 − ε, s) × S³
for some ε > 0, by compactness. Call it ĝ₁; it equals g₁ on 𝒪 ∩ D_s. Let ĝ₂ equal g₂ on 𝒪 ∩ D_s and ĝ₁ on 𝒪 ∖ D_s. By
[[lem:tl5-cip-jets]] (c) every partial derivative of g₂ − g₁ vanishes on N ∩ D_s, so ĝ₂ − ĝ₁ is smooth on 𝒪 by
[[lem:tl5-cip-extend]] (c). So ĝ₁ and ĝ₂ are smooth metrics on 𝒪 in double-null form, vacuum on 𝒪 ∩ D_s, and equal on
𝒫 := 𝒪 ∖ D_s = 𝒪 ∩ ({u < −10} ∪ {v < 1/2}). We time-orient both as in [[lem:tl5-cip-causal]] and put
τ := u + v + 1/(u* − u) + 1/(s − v) on 𝒪, which is of the form of [[lem:tl5-cip-causal]] (b) for both metrics; for
every c the set {τ ≤ c} ∩ D_s ∩ 𝒪 is compact.

Step 2 (a first point of disagreement). Let 𝔅 be the set of q ∈ 𝒪 such that ĝ₁ ≠ ĝ₂ somewhere in every neighbourhood of
q. It is closed in 𝒪 and contained in D_s, as 𝒫 is open. Suppose 𝔅 is not empty. Then τ attains its minimum T on 𝔅,
at a point p, since 𝔅 ∩ {τ ≤ c} is compact for every c; and ĝ₁ = ĝ₂ on the open set 𝒜 := 𝒫 ∪ {q ∈ 𝒪 : τ(q) < T}, hence,
with all derivatives, on its closure 𝒜̄ in 𝒪, which contains Σ := {τ = T}. We show that ĝ₁ = ĝ₂ near p, which
contradicts p ∈ 𝔅; so 𝔅 is empty, ĝ₁ = ĝ₂ on 𝒪, g₁ = g₂ on 𝒪 ∩ D_s, and by continuity on D_s.

Step 3 (harmonic coordinates). Σ is a smooth spacelike hypersurface, acausal for ĝ₁ and for ĝ₂
([[lem:tl5-cip-causal]] (b)), and both metrics induce the same Cauchy data on it. Fix a chart ξ = (ξ⁰, …, ξ⁴) of 𝒪 at p,
a connected open neighbourhood Σ₀ of p in Σ inside the domain of ξ, and χ ∈ C_c^∞(Σ₀) equal to 1 near p. For i = 1, 2,
D_i := D(Σ₀) in (𝒪, ĝ_i) is open and globally hyperbolic with Cauchy hypersurface Σ₀ ([[thm:std-bgp-development]]), and
by [[thm:std-bgp-cauchy]] (5) there are z_i^μ ∈ C^∞(D_i) with □_(ĝ_i) z_i^μ = 0, z_i^μ = χξ^μ and n(z_i^μ) = χ n(ξ^μ) on
Σ₀, n the future unit normal of Σ, the same for both metrics. Near p, z_i and ξ agree to first order on Σ₀, so
dz_i(p) = dξ(p), and z_i := (z_i^μ) is a chart on a neighbourhood U_i ⊂ D_i of p.

Step 4 (the coordinates agree on 𝒜̄ near p). (i) The past side. Membership of a point q with τ(q) ≤ T in D(Σ₀) depends
only on the causal curves from q up to their first point on Σ, which lie in {τ ≤ T}, where the two metrics agree; so
D_1 ∩ {τ ≤ T} = D_2 ∩ {τ ≤ T}. Let Z equal z₁ on D_2 ∩ {τ ≤ T} and z₂ on D_2 ∩ {τ ≥ T}. As z₁ and z₂ have the same
Cauchy data on Σ₀ and solve wave equations whose coefficients agree with all derivatives on Σ₀, the induction of
[[lem:tl5-cip-wave]] shows that their derivatives of all orders agree on Σ₀; so Z is smooth by [[lem:tl5-cip-extend]]
(b), and □_(ĝ₂) Z = 0 on D_2, as ĝ₁ = ĝ₂ on {τ ≤ T}. By [[lem:tl5-cip-wave]] with V = D_2, Z − z₂ = 0 on D⁻(Σ₀), so
z₁ = z₂ on D_2 ∩ {τ ≤ T}. (ii) The outer side. Suppose p ∈ N, so that 𝒫 meets every neighbourhood of p. The sets
𝒫⁰ := 𝒪 ∩ {v < 1/2} and 𝒫¹ := 𝒪 ∩ {u < −10}, whose union is 𝒫, are past sets for both metrics
([[lem:tl5-cip-causal]] (b)), and ĝ₁ = ĝ₂ on them. Near p, Σ is a graph v = v_Σ(u, y) over a box of the variables (u, y)
with v_Σ decreasing in u, so for Σ₀ small each Σʲ := Σ₀ ∩ 𝒫ʲ, j = 0, 1, is connected or empty. Every past inextendible
causal curve in 𝒪 from a point of D⁺(Σʲ), the development taken in (𝒫ʲ, ĝ₁), stays in 𝒫ʲ and meets Σʲ; so
D⁺(Σʲ) ⊂ D_1 ∩ D_2, and on it z₁ and z₂ solve □_(ĝ₁) z = 0 with the same Cauchy data on Σʲ. [[lem:tl5-cip-wave]] in
(𝒫ʲ, ĝ₁), with V = 𝒫ʲ ∩ D_1 ∩ D_2, gives z₁ = z₂ on D⁺(Σʲ). By [[lem:tl5-cip-causal]] (a), along a causal curve near p
the coordinates y change by at most a constant times the change of u + v, and from a point q near p with τ(q) ≥ T the
function u + v decreases by at most τ(q) − T before τ reaches T; a past inextendible causal curve from q, which cannot
stay in a compact subset of a chart without an end point, therefore meets Σ near p, inside Σ₀; a point of 𝒫 near p with
τ ≥ T lies in exactly one of 𝒫⁰, 𝒫¹, as τ < T on 𝒫⁰ ∩ 𝒫¹ near p, and such curves from it stay in that set. So for a
neighbourhood V_p of p every point of 𝒜̄ ∩ V_p lies in D_2 ∩ {τ ≤ T}, in D⁺(Σ⁰) or D⁺(Σ¹), or in their closure; hence
z₁ = z₂ on 𝒜̄ ∩ V_p, with all derivatives, as 𝒜̄ is the closure of its interior.

Step 5 (the transition map). Let Ψ := z₂⁻¹ ∘ z₁, a diffeomorphism between neighbourhoods of p with Ψ(p) = p; by Step 4,
Ψ = id on 𝒜̄ near p. If q ∉ 𝒜̄ is near p and Ψ(q) ∈ 𝒜̄, then Ψ(Ψ(q)) = Ψ(q), so Ψ(q) = q ∈ 𝒜̄ by injectivity, which is
absurd; hence Ψ maps points near p outside 𝒜̄, which lie in D_s, to points outside 𝒜̄, again in D_s. Put
G_i := (z_i⁻¹)*ĝ_i on z_i(U_i) ⊂ ℝ⁵. The coordinate functions are harmonic for G_i, so H^λ := G_i^(αβ) Γ^λ_(αβ) = 0, and
[[thm:std-cbcm-reduced]] with the flat background gives

    Ric(G_i)_(αβ) = −(1/2) G_i^(λμ) ∂_λ∂_μ (G_i)_(αβ) + f̂[G_i, ∂G_i]_(αβ),

f̂ being, by the coordinate formula for the Ricci tensor, a polynomial in ∂G with coefficients rational in G. Moreover
Ric(G₁) = Ric(G₂) =: 𝒯 near z₁(p) = z₂(p): at w = z₁(q), if q ∈ 𝒜̄ then z₂⁻¹(w) = q, and Ric(ĝ₁), Ric(ĝ₂) and the
differentials of z₁, z₂ agree at q; if q ∉ 𝒜̄, then q and Ψ(q) lie in D_s, where both Ricci tensors vanish.

Step 6 (the metrics agree near p). δ := G₂ − G₁ satisfies

    0 = −(1/2) G₂^(λμ) ∂_λ∂_μ δ + (1/2) G₂^(λρ) δ_(ρσ) G₁^(σμ) ∂_λ∂_μ G₁ + f̂[G₂, ∂G₂] − f̂[G₁, ∂G₁],

and f̂[G₂, ∂G₂] − f̂[G₁, ∂G₁] = 𝒜₀δ + 𝒜₁∂δ, with 𝒜₀, 𝒜₁ smooth, by the fundamental theorem of calculus along G₁ + θδ. So
𝔓δ = 0 for an operator 𝔓 with principal part −(1/2) G₂^(λμ) ∂_λ∂_μ, and 2𝔓 is as in [[lem:tl5-cip-wave]] for
(z₁(U₁) ∩ z₂(U₂), G₂). δ vanishes with all derivatives on z₁(𝒜̄ ∩ V_p), which contains z₁(Σ′) = z₂(Σ′) for a connected
open neighbourhood Σ′ of p in Σ, the image under the isometry z₂ of a hypersurface acausal and spacelike for ĝ₂. By
[[lem:tl5-cip-wave]], δ = 0 on D⁺(z₁(Σ′)), and δ = 0 on D⁻(z₁(Σ′)) ⊂ z₁(𝒜̄); so δ = 0 on D(z₁(Σ′)), an open
neighbourhood of z₁(p) ([[thm:std-bgp-development]]). Hence Ψ*ĝ₂ = z₁*G₂ = z₁*G₁ = ĝ₁ near p: Ψ is an isometry of ĝ₁
onto ĝ₂ there.

Step 7 (the gauge fixes Ψ). Let q be near p with q ∉ 𝒜̄, and write q = (u_q, v_q, y_q) in the coordinates (u, v, y) of
𝒪. The curve c: v′ ↦ (u_q, v′, y_q) is a null pregeodesic of ĝ₁ and of ĝ₂ ([[lem:tl5-cip-causal]] (c)); followed
from q in the direction of decreasing v′ it enters the interior of 𝒜̄ after a short arc, along which τ decreases. Let
c̃ be its reparametrization by an affine parameter of ĝ₁ starting at a point c₀ of that interior and ending at q. Then
Ψ ∘ c̃ is a geodesic of ĝ₂ with the initial point c₀ and the initial velocity c̃′(0), since Ψ = id near c₀; the maximal
geodesic of ĝ₂ with these initial data is a reparametrization of the integral curve of ∂_v through c₀, because c is a
pregeodesic of ĝ₂. So Ψ(q) lies on that integral curve: u(Ψ(q)) = u_q and y(Ψ(q)) = y_q. Likewise let d be the integral
curve through q of e₃ = ∂_u + b₁^A∂_A, a null pregeodesic of ĝ₁ in {v = v_q}, followed in the direction of decreasing u
into the interior of 𝒜̄, to a point d₀. There ĝ₁ = ĝ₂, so b₁ = b₂ and the direction of d at d₀ is that of the field
e₃ of ĝ₂; the geodesic Ψ ∘ d̃ of ĝ₂ has the initial data of d̃ at d₀, so it lies on the integral curve of the e₃ of ĝ₂
through d₀, which is a pregeodesic of ĝ₂ in {v = v_q}. So v(Ψ(q)) = v_q, and Ψ(q) = q. The arcs used are short for q
near p and lie where Ψ is defined and isometric. Hence Ψ = id near p, and ĝ₁ = Ψ*ĝ₂ = ĝ₂ near p. ∎

#### Existence and the continuation {#sec:tl5-cip-existence}

**Definition {#def:tl5-cip-development}** (Development.) Let g_N be data in the gauge on N satisfying
[[eq:tl5-cip-constraints]], with W, b, γ as in [[def:tl5-cip-data]], e₃ = ∂_u + b^A∂_A on N₀ and e₄ = ∂_v on N₁. A
development of the data consists of a time-oriented smooth Lorentzian manifold (M̃, g̃) of dimension five, a closed set
M ⊂ M̃ with Ric(g̃) = 0 on M, and an injective map ι: N → M with smooth restrictions to N₀ and N₁ that are immersions,
such that, with ∇̃ the connection of g̃:

(a) g̃(dι X, dι Y) = g_N(X, Y) for X, Y tangent to N₀ at a point of N₀, and for X, Y tangent to N₁ at a point of N₁;

(b) along N₁, ∇̃_V V = 2∂_vW V for V := dι(e₄), and along N₀, ∇̃_(V̲) V̲ = 2e₃(W) V̲ for V̲ := dι(e₃), these fields
being future directed;

(c) at every point of S, g̃(dι ∂_u, dι ∂_v) = g_N(∂_u, ∂_v), and g̃(∇̃_(dιX) V, dι e₃) = −X(e^(2W)) − γ(X, ∂_vb)/2 for
X tangent to S;

(d) there is an open set U ⊂ M̃ that contains ι(N) and satisfies U ∩ J⁺(ι(N)) ⊂ M, J⁺ taken in (U, g̃).

By (a), ι(N₀) and ι(N₁) are null hypersurfaces, with generators the images of the integral curves of e₃ in N₀ and of
∂_v in N₁, whose spacelike leaves ι({u = c} ∩ N₀) and ι({v = d} ∩ N₁) carry the metrics γ. The right sides of (b) and
(c) are the values that a metric in double-null form with the data's W, b, γ has, by [[eq:tl5-cip-connection]].

**Lemma {#lem:tl5-cip-data-extend}** (Extending the data.) Let g_N be data in the gauge on N satisfying
[[eq:tl5-cip-constraints]]. There are η > 0 with u* + η < 0 and data in the gauge on
N′ := ([−10, u* + η] × {1/2} × S³) ∪ ({−10} × [1/2, v* + η] × S³), in the sense of [[def:tl5-cip-data]] with u* + η and
v* + η in place of u* and v*, that satisfy [[eq:tl5-cip-constraints]] and whose restriction to N is g_N.

*Proof.* On N₁ put Ω := (det γ/det γ₀)^(1/6), with γ₀ the round metric of the proof of [[lem:tl5-cip-axis]], and
γ̂ := Ω⁻²γ, so that det γ̂ = det γ₀ in every chart. Then χ_A^B = (∂_vΩ/Ω) δ_A^B + χ̂_A^B, where χ̂_AB := ∂_vγ̂_AB/2 and
the index is raised with γ̂, and χ̂ has trace zero, as det γ̂ does not depend on v; so trχ = 3∂_vΩ/Ω
and |χ|² = 3(∂_vΩ/Ω)² + |χ̂|², |χ̂|² taken with γ̂, and the first line of [[eq:tl5-cip-ricci]] reads

    Ric(e₄, e₄) = −(3/Ω) (∂_v²Ω − 2∂_vW ∂_vΩ + |χ̂|² Ω/3).

Extend W and γ̂ beyond v = v* by the operator of [[lem:tl5-cip-extend]] (a), multiply the extended γ̂ by
(det γ₀/det γ̂)^(1/3), so that its determinant is again that of γ₀, and let Ω solve ∂_v²Ω − 2∂_vW ∂_vΩ + |χ̂|² Ω/3 = 0
along each generator, with its value and first derivative at v = 1/2. On [1/2, v*] it is the given Ω, by uniqueness for
this linear equation, as Ric(e₄, e₄) = 0 there; it is smooth in (v, y), and for η > 0 small it is positive and the
extended γ̂ is positive definite on [1/2, v* + η], by continuity, as both hold on the compact set
{−10} × [1/2, v*] × S³. Put γ := Ω²γ̂ there; then Ric(e₄, e₄) = 0 on {−10} × [1/2, v* + η] × S³. [[lem:tl5-cip-shift]],
with the given b and ζ on S, gives a smooth b on [1/2, v* + η] with Ric(e₄, ∂_A) = 0, by its uniqueness the given one on
[1/2, v*].

On N₀ let ψ_u be the flow of the field b(u, ·) on S³ from u = −10, so that the curves u ↦ (u, ψ_u(ỹ)) are the integral
curves of e₃ in N₀ and (u, ỹ) are coordinates on N₀ in which e₃ = ∂_u. As ∂_u(ψ_u*γ) = ψ_u*(∂_uγ + ℒ_bγ), ℒ_b the Lie
derivative on S³, the field γ̃ := ψ_u*γ has ∂_uγ̃ = 2ψ_u*χ̲, so in these coordinates the second line of
[[eq:tl5-cip-ricci]] is the first with u in place of v. Extend W and b beyond u = u* by the operator of
[[lem:tl5-cip-extend]] (a), so that ψ_u is defined for u ≤ u* + η; extend γ̃ as γ was extended on N₁, with u in place of
v, γ₀ taken in the coordinates ỹ and the conformal factor's value and first derivative at u = −10; and put
γ := (ψ_u⁻¹)*γ̃. Then Ric(e₃, e₃) = 0 on [−10, u* + η] × {1/2} × S³.

The operator of [[lem:tl5-cip-extend]] (a) acts on u and v alone and so commutes with G, γ₀ and the equations are
G-invariant, and ψ_u commutes with G as b is G-invariant; so the extended data are G-invariant. They are smooth on each
of the two hypersurfaces, agree on S, equal g_N on N, and are in double-null form at every point, γ being positive
definite. ∎

We use [[thm:std-ctg-neighbourhood]] in the following form: smooth data in the gauge satisfying
[[eq:tl5-cip-constraints]] have a development. The characteristic data of that theorem are those of the theorem of
Rendall that [CTG23, Section 1, p. 2] recalls, in the formulation of [CP12, Theorem 2.1, p. 5] ([[thm:std-cp-rendall]],
and the passages quoted with [[thm:std-ctg-neighbourhood]]): on each hypersurface a family of Riemannian metrics on the
sections, given up to a conformal factor, in coordinates in which the generators are affinely parametrized, and on the
intersection the conformal factor and its derivatives along the two hypersurfaces, g₁₂ and the torsion. The data g_N
determine these: the metrics γ, in the angular coordinates y on N₁ and, on N₀, in those that are constant along the
integral curves of e₃; the affine parameters, which by (b) are the functions with derivative a constant times e^(2W)
along ∂_v on N₁ and along e₃ on N₀; and on S the values in (c). The conformal factor that the theorem determines from
them by the Raychaudhuri equations, with the value 1 and the derivatives 0 on S, is the one of γ, as g_N satisfies
Ric(e₄, e₄) = 0 on N₁ and Ric(e₃, e₃) = 0 on N₀; so the metric of the theorem satisfies (a)–(c).

To obtain a development we apply the theorem to the data on N′ ⊃ N of [[lem:tl5-cip-data-extend]], on the two
hypersurfaces without their far ends {u = u* + η} and {v = v* + η}. By its proof (the passages quoted with
[[thm:std-ctg-neighbourhood]]), the solution g is defined in a double-null coordinate system (p, q, z), z ∈ S³, in which
the two hypersurfaces are {q = 0} and {p = 0}, each parametrised as [0, ∞) × S³, and g^(pp) = g^(qq) = 0: for all a₀,
a₀′ > 0 there are a₁, a₁′ > 0 such that the coordinates cover B := [0, a₀] × [0, a₁] × S³ and
B′ := [0, a₁′] × [0, a₀′] × S³, and g is smooth on B and on B′ up to their boundaries, as the metric of
[[thm:std-cp-rendall]] is on the closed region {x¹ ≥ 0, x² ≥ 0}. Let ι be the identification of N with its image, choose
a₀ and a₀′ with ι(N₀) ⊂ {p < a₀} and ι(N₁) ⊂ {q < a₀′}, and then a₁ ≤ a₀′ and a₁′ ≤ a₀, as we may, and put
M₀ := ([0, a₀] × [0, a₁/2] ∪ [0, a₁′/2] × [0, a₀′]) × S³. Extend the components of g⁻¹ from B and from B′ by
[[lem:tl5-cip-extend]] (a), and glue the two extensions with a smooth function of (p, q) that is 1 near the points of M₀
outside B′ and 0 on {q ≥ a₁}. The result is a smooth field equal to g⁻¹ on M₀, and its components (pp) and (qq) vanish,
as the extension operator is linear. Near ι(N) it is defined and nondegenerate and its component (pq) is negative, as
g⁻¹ has these properties on ι(N). Let M̃ be a connected open neighbourhood of ι(N) in
{p < a₀, q < a₀′} ∩ ({q < a₁/2} ∪ {p < a₁′/2}) on which they hold, g̃ its inverse there, Lorentzian as M̃ is connected
and g̃ = g on ι(N), and M := M₀ ∩ M̃, a closed subset of M̃ on which Ric(g̃) = Ric(g) = 0. On M̃, ∇p and ∇q are null and
nonzero, and g̃(∇p, ∇q) = g̃^(pq) < 0, so ∇p + ∇q is timelike; we time-orient M̃ so that ∇p + ∇q is past directed, which
on M is the time orientation of the development, in which p and q increase towards the future. As g̃(∇p, ∇p + ∇q) and
g̃(∇q, ∇p + ∇q) equal g̃^(pq) < 0, ∇p and ∇q are past directed. Then (a)–(c) hold, as g̃ = g on M, and (d) holds with
U := M̃: for a future directed causal vector X, dp(X) = g̃(∇p, X) ≥ 0 and dq(X) ≥ 0, so a future directed causal curve
in M̃ from ι(N) stays in {p ≥ 0, q ≥ 0} ∩ M̃, which is contained in M. The uniqueness of the development is not used.

**Lemma {#lem:tl5-cip-dn-form}** (Double-null form from null coordinate functions.) Let g_N be data in the gauge on N
satisfying [[eq:tl5-cip-constraints]], u₁ ∈ (−10, u*], v₁ ∈ (1/2, v*], D′ := [−10, u₁] × [1/2, v₁] × S³ and
N_D := N ∩ D′, and let g be a smooth time-oriented Lorentzian metric on D′, with ∇ its gradient in the coordinates
(u, v, y).

(a) If g⁻¹(du, du) = g⁻¹(dv, dv) = 0 and ∂_v = f∇u with f < 0, ∂_v being future directed, then g is in double-null form.

(b) If g is in double-null form and vacuum, and (a)–(c) of [[def:tl5-cip-development]] hold on N_D with (D′, g) in place
of (M̃, g̃) and the inclusion of N_D in place of ι, then g = g_N at every point of N_D.

*Proof.* (a) ∂_v = f∇u gives g(∂_v, ∂_v) = f² g⁻¹(du, du) = 0, g(∂_v, ∂_A) = f du(∂_A) = 0 and
g(∂_u, ∂_v) = f du(∂_u) = f < 0, and g⁻¹(dv, dv) = 0 is assumed. ∇u and ∇v are null and independent, so they span a
timelike plane, and the tangent space of a leaf, the common kernel of du and dv, is its orthogonal complement, hence
spacelike; so γ is positive definite.

(b) On N₀ ∩ D′, (a) of [[def:tl5-cip-development]] gives g = g_N on pairs of vectors tangent to N₀; by
[[eq:tl5-cip-form]] these values are γ_AB, −γ_AB b^B and γ_AB b^A b^B, so g and g_N have the same γ and b there, and
likewise the same γ on N₁ ∩ D′. So they have the same e₄ = ∂_v on N₁ and the same e₃ = ∂_u + b^A∂_A on N₀. For a metric
in double-null form ∇_(e₄)e₄ = 2∂_vW e₄ and ∇_(e₃)e₃ = 2e₃(W) e₃ ([[eq:tl5-cip-connection]]); with (b) of
[[def:tl5-cip-development]], the functions W of g and of g_N have the same derivative along the generators of N₁ and
along the integral curves of e₃ in N₀, which start on S, and at S they agree by the first part of (c). So W agrees on
N_D. By [[eq:tl5-cip-connection]], g(∇_X e₄, e₃) = −X(e^(2W)) − γ(X, ∂_vb)/2 for X tangent to S, so the second part of
(c) gives the same ζ on S. Finally g satisfies Ric(e₄, ∂_A) = 0 on N₁ ∩ D′, being vacuum, and g_N does by
[[eq:tl5-cip-constraints]]; by [[lem:tl5-cip-shift]], with v₁ in place of v*, the same γ and W on N₁ ∩ D′, the same b on
S and the same ζ on S, the two have the same b on N₁ ∩ D′. As W, b and γ determine all components, g = g_N on N_D. ∎

**Lemma {#lem:tl5-cip-chart}** (Double-null coordinates on a development.) Let (M̃, g̃, M, ι) be a development of data
g_N on N. There are s ∈ (1/2, v*] and a smooth map Φ: D_s → M̃, a diffeomorphism onto its image, with Φ(D_s) ⊂ M and
Φ = ι on N ∩ D_s, such that g := Φ*g̃ is a vacuum metric on D_s in double-null form with g = g_N at every point of
N ∩ D_s.

*Proof.* We use repeatedly that a smooth map on a box or a product of boxes that has invertible differential at the
points of a compact set K and is injective on K is a diffeomorphism of a neighbourhood of K in its domain onto its
image: near each point it extends smoothly ([[lem:tl5-cip-extend]] (a), in charts of M̃) to a local diffeomorphism, and
injectivity on a neighbourhood of K follows from that on K by compactness.

(1) The function v. For d ∈ [1/2, v*] let L_d := ι({−10} × {d} × S³), a spacelike leaf of ι(N₁), and K(d, y) the future
directed null normal of L_d at ι(−10, d, y) with g̃(K, dι ∂_v) = −2, transverse to ι(N₁). For d = 1/2 the geodesic
t ↦ exp(tK) is, up to parametrization, the generator of ι(N₀) through ι(−10, 1/2, y), the null normal of ι(S) transverse
to ι(N₁) being the direction of these generators. Let t_*(y) be its affine parameter at the point where u = u*, and
Ξ(d, t, y) := exp_(ι(−10, d, y))(t K(d, y)) for d ∈ [1/2, 1/2 + δ] and t ∈ [−δ, t_*(y) + δ]; for δ > 0 small these
geodesics exist in M̃, being close to the generators of ι(N₀) continued slightly beyond their ends, and with
t = (t_*(y) + 2δ)t′ − δ, Ξ is a smooth map of (d, t′, y) on the box [1/2, 1/2 + δ] × [0, 1] × S³. Along a geodesic with
d = 1/2 the field J := ∂_dΞ is a Jacobi field, and as all the curves t ↦ Ξ(d, t, y) are null geodesics,
∂_t g̃(J, ∂_tΞ) = g̃(∇̃_J ∂_tΞ, ∂_tΞ) = J(g̃(∂_tΞ, ∂_tΞ))/2 = 0, so g̃(J, ∂_tΞ) = g̃(dι ∂_v, K) = −2. Since ∂_tΞ spans
the null normal direction of ι(N₀), every vector tangent to ι(N₀) is orthogonal to it; so J is transverse to ι(N₀).
Ξ(1/2, ·, ·) is, for δ small, an injective immersion whose image contains ι(N₀), so dΞ is invertible on {d = 1/2}, and
for δ small Ξ is a diffeomorphism onto a closed set 𝒱. Put v := d on 𝒱. The tangent space of a level set H_d of v is
spanned by ∂_tΞ, which is null, and by the Jacobi fields ∂_(y^A)Ξ, with g̃(∂_(y^A)Ξ, ∂_tΞ) constant in t by the same
calculation and zero at t = 0, as K is normal to L_d. So H_d is a null hypersurface, and g̃⁻¹(dv, dv) = 0 on 𝒱.

(2) The function u and the angles. For c ∈ [−10, u*] let S_c := ι({c} × {1/2} × S³) and L(c, y) the future directed
null normal of S_c at ι(c, 1/2, y) transverse to ι(N₀), with g̃(L, V̲) = −2e^(2W). For c = −10 it is tangent to ι(N₁),
whose generator through ι(−10, 1/2, y) is the geodesic λ ↦ exp(λL) up to parametrization. Let
Θ(c, λ, y) := exp_(ι(c, 1/2, y))(λ L(c, y)) for λ ∈ [0, λ₀]. As in (1), for λ₀ small Θ is a diffeomorphism onto a
closed set 𝒰, and with u := c on 𝒰 the level sets C_c of u are null hypersurfaces, so g̃⁻¹(du, du) = 0, whose
generators λ ↦ Θ(c, λ, y) are the integral curves of ∇u. Let y also denote the third component of Θ⁻¹; it is constant
along these generators.

(3) The chart. At a point of ι(N₀) the linear form g̃(·, V̲) vanishes on the tangent space of ι(N₀) and is negative on
J and on L; so L = κJ + Y with κ > 0 and Y tangent to ι(N₀). Hence dv(L) = κ > 0, and the curves λ ↦ Θ(c, λ, y) leave
ι(N₀) to the side into which J points, where Ξ, extended near ι(N₀) to a local diffeomorphism, takes values with
d > 1/2. By compactness there are λ₀ > 0 and κ₀ > 0 with Θ([−10, u*] × [0, λ₀] × S³) ⊂ 𝒱 and ∂_λ v(Θ(c, λ, y)) ≥ κ₀
there. Let s ∈ (1/2, v*] with s ≤ 1/2 + κ₀λ₀. For (u, v, y) ∈ D_s there is exactly one λ ∈ [0, λ₀] with
v(Θ(u, λ, y)) = v; put Φ(u, v, y) := Θ(u, λ, y). Φ is smooth, with the smooth inverse (u, v, y) on its image. On N₀,
λ = 0 and Φ = ι. On N₁, Θ(−10, λ, y) runs along the generator ι({−10} × [1/2, v*] × {y}) of ι(N₁), on which
v(ι(−10, d, y)) = d, as ι(−10, d, y) = Ξ(d, 0, y); so Φ = ι there. Each point Θ(u, λ, y) is joined to ι(N₀) by the
future directed null geodesic Θ(u, ·, y) on [0, λ], so for λ₀ small it lies in U ∩ J⁺(ι(N)) ⊂ M.

(4) The double-null form. In the coordinates (u, v, y) the field ∂_v is tangent to the generators of the C_u, so it is a
multiple f∇u of ∇u, and g⁻¹(du, du) = 0 by (2) and g⁻¹(dv, dv) = 0 by (1). ∂_v = ∂_λΘ/∂_λv is future directed, and ∇u is
past directed, since g̃(∇u, V̲) = du(V̲) = du(e₃) = 1 > 0 with V̲ future directed; so f < 0. By [[lem:tl5-cip-dn-form]]
(a), g is in double-null form, and it is vacuum as Φ(D_s) ⊂ M.

(5) The data. Φ = ι on N ∩ D_s, so dΦ = dι on vectors tangent to N₀ and to N₁, and Φ is an isometry of (D_s, g) onto its
image; so (a)–(c) of [[def:tl5-cip-development]] hold on N ∩ D_s with (D_s, g) in place of (M̃, g̃) and the inclusion in
place of ι, and [[lem:tl5-cip-dn-form]] (b), with u₁ = u* and v₁ = s, gives g = g_N at every point of N ∩ D_s. ∎

**Theorem {#thm:tl5-cip}** (The characteristic problem in the gauge.) Let u* ∈ (−10, 0) and v* > 1/2, and let smooth
characteristic data in the gauge be given on N₀ and N₁ ([[def:tl5-cip-data]]), satisfying the characteristic constraints
[[eq:tl5-cip-constraints]]. With D_s as in [[def:tl5-cip-data]], call a solution on D_s a smooth T²-invariant vacuum
metric of the class on D_s, in the gauge, that induces the data on N ∩ D_s. Then:

(F1) there are s ∈ (1/2, v*] and a solution on D_s;

(F2) two solutions on the same D_s coincide;

(F3) a solution on D_s with s < v* is the restriction of a solution on D_(s′) for some s′ ∈ (s, v*].

Uniqueness holds more generally for vacuum metrics in double-null form on D_s, without symmetry
([[prop:tl5-cip-unique]]).

*Proof.* By [[lem:tl5-cip-form]] (b), a solution on D_s is a G-invariant vacuum metric on D_s in double-null form that
induces the data on N ∩ D_s.

(F2) is [[prop:tl5-cip-unique]].

(F1) By [[thm:std-ctg-neighbourhood]], in the form stated after [[def:tl5-cip-development]], the data have a
development, and [[lem:tl5-cip-chart]] gives s ∈ (1/2, v*] and a vacuum metric g on D_s in double-null form that induces
the data. For σ ∈ G, σ*g is vacuum and in double-null form, since σ acts on S³ alone and preserves ∂_v, dv and the
leaves, and σ*g = σ*g_N = g_N on N ∩ D_s, since the data and N are G-invariant. By [[prop:tl5-cip-unique]], σ*g = g. So
g is G-invariant, and a solution on D_s.

(F3) Let g be a solution on D_s with s < v*. Let g′ be the field on N′ := ([−10, u*] × {s} × S³) ∪ ({−10} × [s, v*] × S³)
equal to g on the first part and to g_N on the second; the two agree on {−10} × {s} × S³, as g induces the data on
N₁ ∩ D_s. g′ is smooth on each part, G-invariant and in double-null form at every point, so it is data in the gauge
for the problem with v = 1/2 replaced by v = s, and it satisfies the constraints: on the second part they are those of
g_N, and on the first Ric(e₃, e₃) is, by [[eq:tl5-cip-ricci]], computed from derivatives along {v = s}, so it is that of
g, which vanishes. By (F1), applied to this problem after the translation v ↦ v − s + 1/2, there are s′ ∈ (s, v*] and
a solution g″ on [−10, u*] × [s, s′] × S³ that induces g′. Let ḡ equal g on D_s and g″ there. By
[[lem:tl5-cip-jets]] (a), with H = [−10, u*] × {s} × S³, I₁ = [1/2, s] and I₂ = [s, s′], all one-sided derivatives in v
of g and g″ agree on H: on Z = {−10} × {s} × S³ they are the derivatives in v along N₁ of g_N, which is smooth on N₁.
With the derivatives along H, all partial derivatives of the two pieces agree on H, so ḡ is smooth on D_(s′) by
[[lem:tl5-cip-extend]] (b). It is G-invariant, vacuum and in double-null form, and induces the data on N ∩ D_(s′); so
it is a solution on D_(s′), and its restriction to D_s is g. ∎

**Remark {#rem:tl5-cip-axes}** (The axes.) The regions D_s contain the axes {x = ±1}, where the T² orbits degenerate.
The proofs above use the coordinates (x, φ1, φ2) only to express G-invariance ([[lem:tl5-cip-form]] (b)); the equations
[[eq:tl5-cip-ricci]], the transport along the generators in [[lem:tl5-cip-jets]] and [[lem:tl5-cip-shift]], the
extension and the harmonic coordinates are written in charts of S³ near any point, axes included, with smooth
coefficients. The reduction to the orbit space ([[prop:reduction]]), whose equations are singular at the axes, is not
used. In particular the shift β of [[lem:tl5-cip-shift]] is a smooth function that vanishes at the axes, as β = −2e^(2W)
g⁻¹(dv, dx) and dx = 0 there. By [[lem:tl5-cip-axis]] (a), the functions R, P, Q, W and β of a solution are smooth
functions of (u, v, x) up to the axes.

#### The problem at 10 l5 in two stages {#sec:tl5-cip-staged}

The data of [[def:tl5-problem]] are not smooth on N, but they are smooth on the parts of N on which env is the
restriction of an analytic function, and for u* < u₀, with u₀ as in [[lem:tl5-seed]] (a), the seed covers
[−10, u*] × [0, 1/2] × S³ and solves the problem there. So the problem splits into the seed and two characteristic
problems with smooth data, to which [[thm:tl5-cip]] applies. Below, g_N denotes the field on N, in the sense of
[[def:tl5-cip-data]], that has in the variables of [[lem:tl5-cip-form]] (b) the data's R, P, Q, W and β; it is
G-invariant and in double-null form, smooth on N ∩ {v ≤ 1/2}, on N ∩ {1/2 ≤ v ≤ 7/2} and on N ∩ {v ≥ 7/2}, and of class
C³ in v on N (the paragraph after [[lem:tl5-cip-shift]]).

**Corollary {#cor:tl5-cip-staged}** (The problem at 10 l5 in two stages.) Fix a seed and u* ∈ (−10, u₀), with u₀ as in
[[lem:tl5-seed]] (a), and let g_N be as above.

(a) For v* ∈ (1/2, 7/2], the field equal to the seed on N₀ = [−10, u*] × {1/2} × S³ and to g_N on
N₁ = {−10} × [1/2, v*] × S³ is smooth characteristic data in the gauge satisfying [[eq:tl5-cip-constraints]]. So
(F1)–(F3) of [[thm:tl5-cip]] hold for it; its solutions are called solutions of the first stage.

(b) Let g₁ be a solution of the first stage on D_(7/2), and v* > 7/2. The field equal to g₁ on [−10, u*] × {7/2} × S³
and to g_N on {−10} × [7/2, v*] × S³ is, after the translation v ↦ v − 3, smooth characteristic data in the gauge
satisfying [[eq:tl5-cip-constraints]]. So (F1)–(F3) hold for it; its solutions, translated back to regions
[−10, u*] × [7/2, s] × S³, are called solutions of the second stage.

(c) Let s ∈ (1/2, 7/2] and g₁ be a solution of the first stage on D_s. The metric equal to the seed on
[−10, u*] × [0, 1/2] × S³ and to g₁ on D_s is a solution of [[def:tl5-problem]] on [−10, u*] × [0, s] × S³; it is of
class C³, with Lipschitz derivatives of order 3, and smooth on each of the two pieces, and its R, P, Q, W and β are C³
functions of (u, v, x). If s = 7/2 and g₂ is a solution of the second stage on [−10, u*] × [7/2, s₂] × S³, the metric
equal to g₂ there and to the former one on [−10, u*] × [0, 7/2] × S³ is a solution on [−10, u*] × [0, s₂] × S³ with the
same properties. Conversely, let g′ be a solution of [[def:tl5-problem]] on [−10, u*] × [0, s′] × S³, s′ > 1/2, whose
restrictions to [−10, u*] × [0, 1/2] × S³, to [−10, u*] × [1/2, min(s′, 7/2)] × S³ and, if s′ > 7/2, to
[−10, u*] × [7/2, s′] × S³ are smooth. Then g′ is the seed on the first of these sets, a solution of the first stage on
the second and a solution of the second stage on the third; by (F2), there is at most one such g′ for each s′.

*Proof.* (a) By [[lem:tl5-seed]] (a), every (u, v) with −10 ≤ u ≤ u* and 0 ≤ v ≤ 1/2 lies in D_seed: for u ≤ −1 every
v ≥ 0 does, and for −1 < u ≤ u* those with v < 2u + ln((1 − u)/(1 + u)) do, a bound that exceeds 1/2 as u < u₀. So the
seed, real-analytic on D_seed × S³ ([[lem:tl5-seed]] (b), (c)), is a smooth vacuum metric of the class in the gauge on
[−10, u*] × [0, 1/2] × S³, G-invariant and in double-null form ([[lem:tl5-cip-form]] (b)), and the field is smooth on
N₀; on N₁ it is smooth, as stated above. The two agree on S: by [[lem:tl5-seed]] (d), the seed induces on
{u = −10, 0 ≤ v ≤ 1/2} the data's W, P and Q, with R = r, which is r_s = R(r_s, x) at v = 1/2, and β = 0, which is the
data's β at v = 1/2; so W, b and γ agree on S, and with them the fields ([[lem:tl5-cip-form]] (a)). On N₁,
Ric(e₄, e₄) = Ric_vv is on {|x| < 1} the right side of [[eq:cone-raychaudhuri]] ([[lem:cone-raychaudhuri]]), which
vanishes by [[prop:cone-exact]], and it vanishes at x = ±1 by continuity; Ric(e₄, ∂_A) = 0 on N₁ by the choice of β
([[lem:tl5-cip-shift]]); and on N₀, Ric(e₃, e₃) is determined by the field on N₀, which the seed induces, so it
vanishes, the seed being vacuum.

(b) g₁ is smooth on D_(7/2), G-invariant and in double-null form, so the field is smooth on [−10, u*] × {7/2} × S³; on
{−10} × [7/2, v*] × S³ it is smooth, as stated above. The two agree on {−10} × {7/2} × S³, as g₁ induces g_N on
N₁ ∩ D_(7/2). The constraints hold as in (a), with g₁, which is vacuum, in place of the seed. The translation v ↦ v − 3
preserves the class, the gauge and the vacuum equations, and maps these hypersurfaces to N₀ and N₁ of
[[def:tl5-cip-data]] with v* − 3 in place of v*.

(c) Write g for the glued metric, H := [−10, u*] × {1/2} × S³ and Z := {−10} × {1/2} × S³. The seed is smooth on
[−10, u*] × [0, 1/2] × S³ by (a), g₁ is smooth on D_s, and the two agree at every point of H, as g₁ induces the seed's
values on N₀. On Z the derivatives ∂_v^k of their W, b and γ are those of g_N along N, from below and from above
v = 1/2, since both induce g_N on their parts of N; as g_N is C³ in v on N, they agree for k ≤ 3. By
[[lem:tl5-cip-jets]] (a) with m = 3, I₁ = [0, 1/2] and I₂ = [1/2, s], the derivatives ∂_v^k of W, b and γ of the two
agree on H for k ≤ 3; so do the derivatives of these along H, and so all partial derivatives of order at most 3. By
[[lem:tl5-cip-extend]] (b), the components of g in charts of S³ are C³ on [−10, u*] × [0, s] × S³; their derivatives of
order 3 are Lipschitz on compact convex sets of a chart, being smooth on each piece, as a segment meets {v = 1/2} at
most once or lies in it. So g is a G-invariant metric of class C³ in double-null form, and Ric(g), which is continuous,
vanishes on both pieces and hence everywhere. The functions R, P, Q, W and β of g₁ are smooth on
[−10, u*] × [1/2, s] × [−1, 1] by [[lem:tl5-cip-axis]] (a), and those of the seed are smooth on
[−10, u*] × [0, 1/2] × [−1, 1], P, Q and β being 0 and R and W not depending on x. For |x| < 1 their partial derivatives
of order at most 3 from the two sides of v = 1/2 are the same expressions in those of the components of g in the chart
(x, φ1, φ2), so they agree, and at x = ±1 they agree by continuity; by [[lem:tl5-cip-extend]] (b) in the variables
(u, v, x), they are C³. Finally g induces the data on C₀ and on N ∩ {v ≤ 1/2} ([[lem:tl5-seed]] (d) and the sentence
after [[def:tl5-problem]]) and on N ∩ {1/2 ≤ v ≤ s}; so it is a solution of [[def:tl5-problem]]. The second gluing is
the same argument at v = 7/2, with g₁ and g₂ in place of the seed and g₁, I₁ = [1/2, 7/2] and I₂ = [7/2, s₂].

Conversely, the restrictions of g′ are G-invariant vacuum metrics in double-null form ([[lem:tl5-cip-form]] (b)). On
{v = 0} and on N ∩ {v ≤ 1/2}, g′ and the seed have the data's R, P, Q, W and β, which determine the metric on {|x| < 1}
and by continuity everywhere; so by [[prop:tl5-cip-unique]], after the translation v ↦ v + 1/2 and with s = v* = 1, g′
is the seed on [−10, u*] × [0, 1/2] × S³. Then its restriction to [−10, u*] × [1/2, min(s′, 7/2)] × S³ induces the data
of the first stage and so is a solution of the first stage; and if s′ > 7/2, its restriction to
[−10, u*] × [7/2, s′] × S³ is a solution of the second stage for the restriction of g′ to D_(7/2). By (F2) for each
stage, g′ is determined by s′. ∎

**Remark {#rem:tl5-cip-regularity}** (Regularity.) [[thm:tl5-cip]] is proved for smooth data, and smoothness enters at
three places: [[thm:std-ctg-neighbourhood]] is a theorem about smooth data; the common extension in the proof of
[[prop:tl5-cip-unique]] uses derivatives of all orders, and the linear theory of [[thm:std-bgp-cauchy]] is for smooth
coefficients; and the gluing in (F3) uses derivatives of all orders. The data of [[def:tl5-problem]] are C³ and not C⁴
in v at v = 1/2 and v = 7/2, as env is ([[rem:envelope-regularity]]), but they are smooth on each stage, and
[[cor:tl5-cip-staged]] applies the theorem stage by stage. Only the gluing across v = 1/2 and v = 7/2 is done in finite
regularity, by [[lem:tl5-cip-jets]] (a) with m = 3, and the solutions of [[cor:tl5-cip-staged]] (c) are of class C³ and
not C⁴, since the fourth derivatives in v of P and Q on N jump at v = 1/2 and v = 7/2. No theorem of finite regularity
is used, and the regularity of the data is no obstruction to existence on a given region: what [[lem:tl5-continuation]]
needs beyond [[thm:tl5-cip]] is (H1)–(H3) ([[rem:tl5-beyond]]). For an envelope that is smooth on ℝ and vanishes outside
[1/2, 7/2], the data on N would be smooth, and the theorem would apply in one stage, posed on {v = 0} and N after a
translation in v, as long as the R of the Raychaudhuri constraint stays positive.

### The reduced problem in the wave gauge {#sec:tl5-wg}

This section and the next treat the characteristic problem in a second gauge: the wave gauge relative to a fixed
background metric ĝ, in which the Einstein equations become a quasilinear wave system for the components of the metric.
We write the system and its linearisation, define its data on N₀ ∪ N₁ and the regions on which it is solved, and prove
its local theory: uniqueness ([[prop:tl5-wg-unique]]), propagation of the gauge and of the symmetry
([[prop:tl5-wg-vacuum]]), and local existence and continuation ([[prop:tl5-wg-local]]); [[thm:tl5-wg]] collects them.
In this gauge the coordinate hypersurfaces {v = s} are null for ĝ but in general not for a solution g, so the regions
are bounded to the future by hypersurfaces that are spacelike for every metric close to ĝ ([[def:tl5-wg-domains]]).
[[sec:tl5-dn]] then puts a solution close to ĝ into the double-null gauge of [[sec:cone-constraint]] on an explicit
region ([[thm:tl5-dn]]). We use the notation of [[sec:tl5-cip-form]]: 𝒬 = ℝ² × S³, the group G = O(2) × O(2)
acting on S³, charts y of S³ with indices A, B, C running over 1, 2, 3, the regions N₀, N₁, N = N₀ ∪ N₁ and
S = N₀ ∩ N₁ of [[def:tl5-cip-data]], and D̄:

    D̄ := [−10, u*] × [1/2, v*] × S³,   N₀ := [−10, u*] × {1/2} × S³,   N₁ := {−10} × [1/2, v*] × S³,

with u* ∈ (−10, 0) and v* > 1/2 fixed. A function on a closed subset of 𝒬 is smooth if, in charts, all its partial
derivatives at interior points extend continuously to the set; at points of the boundary the derivatives are these
limits.

#### The gauge and the reduced equations {#sec:tl5-wg-equations}

**Definition {#def:tl5-wg-background}** (The background.) A background is a smooth G-invariant metric ĝ in double-null
form ([[def:tl5-cip-null]]) on an open G-invariant set 𝒪̂ ⊂ 𝒬 that contains D̄. In a chart y of S³ we write,
as in [[lem:tl5-cip-form]],

    ĝ = −2Ω̂² (du ⊗ dv + dv ⊗ du) + γ̂_AB θ̂^A ⊗ θ̂^B,    θ̂^A := dy^A − b̂^A du,    ê₃ := ∂_u + b̂^A ∂_A,    ê₄ := ∂_v,

with Ω̂ > 0, and we time-orient ĝ so that ê₃ and ê₄ are future directed. Put e₀ := (ê₃ + ê₄)/(2Ω̂) and
k̂ := ĝ + 2 ĝ(e₀, ·) ⊗ ĝ(e₀, ·). For tensors of every type, |·| is the norm induced by k̂. D̂, Γ̂ and R̂ denote the
connection, the Christoffel symbols and the curvature of ĝ.

The vector field e₀ is unit timelike: ĝ(e₀, e₀) = ĝ(ê₃, ê₄)/(2Ω̂²) = −1. With e₁ := (ê₄ − ê₃)/(2Ω̂) and a γ̂-orthonormal
frame f₁, f₂, f₃ of the leaves, (e₀, e₁, f₁, f₂, f₃) is ĝ-orthonormal, and in it k̂ is the identity matrix. So k̂ is
Riemannian, |T| for a 2-tensor T is the Frobenius norm of its matrix in such a frame, and

    k̂⁻¹ = ĝ⁻¹ + 2 e₀ ⊗ e₀ = (1/(2Ω̂²)) (ê₃ ⊗ ê₃ + ê₄ ⊗ ê₄) + γ̂^(AB) ∂_A ⊗ ∂_B,  {#eq:tl5-wg-khat}

since e₀ ⊗ e₀ + e₁ ⊗ e₁ = (1/(2Ω̂²))(ê₃ ⊗ ê₃ + ê₄ ⊗ ê₄) and ĝ⁻¹ = −e₀ ⊗ e₀ + e₁ ⊗ e₁ + Σ f_i ⊗ f_i. In
particular |du|² = |dv|² = 1/(2Ω̂²) and k̂⁻¹(du, dv) = 0.

**Definition {#def:tl5-wg-gauge}** (The wave gauge.) For a smooth Lorentzian metric g on a subset of 𝒪̂ let
C := Γ(g) − Γ̂, a tensor field of type (1, 2), and

    Υ(g)^μ := g^(αβ) C^μ_αβ,      Ric^W(g)_αβ := Ric(g)_αβ − (1/2) (g_αλ D̂_β Υ^λ + g_βλ D̂_α Υ^λ).  {#eq:tl5-wg-def}

The metric g is in the wave gauge if Υ(g) = 0, and the reduced equation is

    Ric^W(g) = 0.  {#eq:tl5-wg-reduced}

Υ is the vector H of [[thm:std-cbcm-reduced]] for the background ĝ, since there W^λ = g^(αβ) Γ̂^λ_αβ, and Ric^W(g) is
the tensor R^(H) of that theorem. So, by [CBCM10, (2.9), p. 8],

    Ric^W(g)_αβ = −(1/2) g^(λμ) D̂_λ D̂_μ g_αβ + f̂[g, D̂g]_αβ,

with f̂ independent of the second derivatives of g. In coordinates (u, v, y), D̂_λD̂_μ g_αβ is ∂_λ∂_μ g_αβ plus terms
with at most one derivative of g and coefficients built from Γ̂ and ∂Γ̂, and the coordinate formulae for Ric(g) and
for the last term of [[eq:tl5-wg-def]] are polynomials in g_μν, g^μν, ∂g, ∂²g, Γ̂ and ∂Γ̂. Hence

    Ric^W(g)_αβ = −(1/2) g^(λμ) ∂_λ ∂_μ g_αβ + Φ_αβ(p, g(p), ∂g(p)),  {#eq:tl5-wg-form}

where Φ is a polynomial in g_μν, g^μν, ∂_λ g_μν and in the values at p of Γ̂ and ∂Γ̂; it is smooth on the set of
(p, g, ∂g) with p ∈ 𝒪̂ and g Lorentzian. The reduced equation is a quasilinear system of fifteen wave equations for the
components of g, with principal part −(1/2) g^(λμ) ∂_λ∂_μ times the identity. Write h := g − ĝ.

**Lemma {#lem:tl5-wg-linear}** (The linearisation.) (a) Υ(ĝ) = 0 and Ric^W(ĝ) = Ric(ĝ).

(b) For a smooth symmetric 2-tensor field h,

    𝓡̂ h := R̂iem·h − (1/2) (R̂ic ∘ h + h ∘ R̂ic),
    (d/dt) Ric^W(ĝ + t h)|_(t=0) = −(1/2) (□̂ h + 2 𝓡̂ h),                                            {#eq:tl5-wg-lin}

where □̂ h := ĝ^(λμ) D̂_λ D̂_μ h, (R̂iem·h)_αβ := R̂_αμβν h^(μν), (R̂ic ∘ h)_αβ := R̂ic_αρ h^ρ_β, (h ∘ R̂ic)_αβ :=
h_αρ R̂ic^ρ_β, indices are moved with ĝ, and the curvature convention is R̂^ρ_σμν V^σ = [D̂_μ, D̂_ν] V^ρ with
R̂ic_σν = R̂^ρ_σρν, R̂_ρσμν := ĝ_ρλ R̂^λ_σμν. Its principal part is −(1/2) ĝ^(λμ) ∂_λ∂_μ times the identity; on a vacuum
background, □̂ + 2𝓡̂ is the Lichnerowicz wave operator.

(c) At every smooth Lorentzian g, the linearisation h ↦ (d/dt) Ric^W(g + t h)|_(t=0) is a linear second-order
operator with principal part −(1/2) g^(λμ) ∂_λ∂_μ times the identity.

(d) If σ is a diffeomorphism of 𝒪̂ with σ*ĝ = ĝ, then Υ(σ*g) = σ*Υ(g) and Ric^W(σ*g) = σ*Ric^W(g).

*Proof.* (a) C = 0 for g = ĝ.

(b) Let g_t := ĝ + th and δΓ := (d/dt) Γ(g_t)|_(t=0), a tensor; differentiating the formula of the Christoffel
symbols gives δΓ^μ_αβ = (1/2) ĝ^(μλ) (D̂_α h_βλ + D̂_β h_αλ − D̂_λ h_αβ). At a point p, in coordinates in which
Γ̂(p) = 0, the derivative at t = 0 of Ric(g_t)_αβ = ∂_μ Γ^μ_αβ − ∂_β Γ^μ_μα + Γ^μ_μλ Γ^λ_αβ − Γ^μ_βλ Γ^λ_μα is
∂_μ δΓ^μ_αβ − ∂_β δΓ^μ_μα at p, so, both sides being tensors, δRic_αβ = D̂_μ δΓ^μ_αβ − D̂_β δΓ^μ_μα everywhere. With
δΓ^μ_μα = (1/2) D̂_α tr h, tr h := ĝ^(μν) h_μν,

    δRic_αβ = (1/2) (D̂_μ D̂_α h_β^μ + D̂_μ D̂_β h_α^μ − □̂ h_αβ − D̂_α D̂_β tr h).

By the convention, D̂_μ D̂_α h_β^μ − D̂_α D̂_μ h_β^μ = −R̂^ρ_βμα h_ρ^μ + R̂^μ_ρμα h_β^ρ, and R̂^ρ_βμα h_ρ^μ =
R̂_ρβμα h^(ρμ) = R̂_αμβρ h^(μρ) = (R̂iem·h)_αβ by the symmetries of R̂, while R̂^μ_ρμα h_β^ρ = (h ∘ R̂ic)_βα. Treating
the second term alike and writing (div h)_β := D̂_μ h_β^μ,

    δRic_αβ = −(1/2) □̂ h_αβ − (R̂iem·h)_αβ + (1/2) (R̂ic ∘ h + h ∘ R̂ic)_αβ
              + (1/2) (D̂_α ψ_β + D̂_β ψ_α),      ψ := div h − (1/2) d tr h.

On the other hand Υ(g_t)^μ = g_t^(αβ) (Γ(g_t) − Γ̂)^μ_αβ, so (d/dt) Υ(g_t)|_(t=0) = ĝ^(αβ) δΓ^μ_αβ = ψ^μ, and since
Υ(ĝ) = 0 the derivative of the last term of [[eq:tl5-wg-def]] at t = 0 is (1/2)(D̂_β ψ_α + D̂_α ψ_β). The difference is
[[eq:tl5-wg-lin]]. Its second-order part is −(1/2) ĝ^(λμ) ∂_λ ∂_μ h. When R̂ic = 0, □̂ h + 2𝓡̂ h = □̂ h + 2 R̂iem·h.

(c) By [[eq:tl5-wg-form]], (d/dt) Ric^W(g + th) = −(1/2) g^(λμ) ∂_λ ∂_μ h + (terms with at most one derivative of h).

(d) Γ(σ*g) − Γ(σ*ĝ) = σ*(Γ(g) − Γ(ĝ)) and σ*ĝ = ĝ, so C, Υ and D̂Υ transform as tensors, as does Ric. ∎

#### The tilted domains {#sec:tl5-wg-tilted}

**Definition {#def:tl5-wg-domains}** (The tilted domains.) Fix κ, κ′ ∈ (0, 1/4] with κ′(v* − 1/2) < u* + 10 and κ(u* +
10) < v* − 1/2, and put κ_m := min(κ, κ′),

    τ₁ := u + κ′ (v − 1/2),      τ₂ := v + κ (u + 10),
    D^κ := D̄ ∩ {τ₁ ≤ u*} ∩ {τ₂ ≤ v*},      D^κ_s := D^κ ∩ {τ₂ ≤ s}   (1/2 ≤ s ≤ v*).  {#eq:tl5-wg-tilted}

A smooth Lorentzian metric g on a set X ⊂ 𝒪̂ is tilted on X if |g⁻¹ − ĝ⁻¹| ≤ κ_m at every point of X. A tilted metric
is time-oriented so that dτ₂ is past directed.

D^κ_(1/2) = S, and D^κ_(v*) = D^κ. By the two conditions on κ and κ′, τ₁ < u* on N₁ and τ₂ < v* on N₀, so N ⊂ D^κ, N₁
does not meet {τ₁ = u*} and N₀ does not meet {τ₂ = v*}. The sets D^κ_s are the sublevel sets of τ₂ in D^κ, and their
boundaries consist of parts of N₀ and N₁ and of the future boundaries D^κ ∩ {τ₂ = s} and D^κ ∩ {τ₁ = u*}.

**Lemma {#lem:tl5-wg-norms}** (Inverse metrics.) At a point of 𝒪̂ let g be a symmetric 2-tensor and h := g − ĝ.

(a) If |h| ≤ 1/2, then g is Lorentzian and |g⁻¹ − ĝ⁻¹| ≤ 2|h|.

(b) If g is invertible and |g⁻¹ − ĝ⁻¹| ≤ 1/4, then |h| ≤ 1/3; and if g′ is another such tensor, every
g + θ(g′ − g), 0 ≤ θ ≤ 1, is Lorentzian.

*Proof.* In a frame as after [[def:tl5-wg-background]], ĝ has the matrix η := diag(−1, 1, 1, 1, 1), which is orthogonal,
and |·| is the Frobenius norm, which bounds the operator norm ‖·‖ and is unchanged by multiplication with η. (a) With H
the matrix of h, g = η(1 + ηH) and ‖ηH‖ ≤ 1/2, so g is invertible, g⁻¹ − η = −(1 + ηH)⁻¹ ηHη and |g⁻¹ − η| ≤ ‖(1 +
ηH)⁻¹‖ |H| ≤ 2|H|. Each η + tH, 0 ≤ t ≤ 1, is invertible, so its eigenvalues keep their signs and g has the signature
of η. (b) With K the matrix of g⁻¹ − ĝ⁻¹, g = (η + K)⁻¹ and g − η = −(1 + ηK)⁻¹ ηKη, so |h| ≤ |K|/(1 − ‖K‖) ≤ 1/3. Then
g + θ(g′ − g) − ĝ has norm at most 1/3, and (a) applies. ∎

**Lemma {#lem:tl5-wg-domains}** (Geometry of the tilted domains.) (a) ĝ⁻¹(dτ₁, dτ₁) = −κ′/Ω̂²,
ĝ⁻¹(dτ₂, dτ₂) = −κ/Ω̂² and ĝ⁻¹(dτ₁, dτ₂) = −(1 + κκ′)/(2Ω̂²).

(b) Let g be tilted at a point. Then g⁻¹(dτ₁, dτ₁) ≤ −15κ′/(32Ω̂²), g⁻¹(dτ₂, dτ₂) ≤ −15κ/(32Ω̂²) and
g⁻¹(dτ₁, dτ₂) < 0, so dτ₁ and dτ₂ are g-timelike and both past directed; so is every combination a dτ₁ + b dτ₂
with a, b ≥ 0, (a, b) ≠ 0. For ĝ, dτ₂ is past directed for the time orientation of [[def:tl5-wg-background]].

(c) Let g be tilted on a set X. Along every future directed g-causal curve in X, τ₁ and τ₂ are strictly increasing.
Let p ∈ X ∩ N₁, and suppose the tangent space of N₁ at p is degenerate for g, with ∂_v in its kernel. Then ∂_v is
future directed null at p, and du(V) ≥ 0 for every future directed g-causal vector V at p. Likewise, if p ∈ X lies on
{v = 1/2} and the tangent space of {v = 1/2} at p is degenerate for g with kernel spanned by a vector e with
du(e) = 1, then e is future directed null at p and dv(V) ≥ 0 for every future directed g-causal V at p.

(d) [−10, u* − κ′(v* − 1/2)] × [1/2, v* − κ(u* + 10)] × S³ ⊂ D^κ, and, for 1/2 ≤ s ≤ v*,
D^κ_s ⊂ [−10, −10 + (s − 1/2)/κ] × [1/2, s] × S³.

*Proof.* (a) By the inverse in [[lem:tl5-cip-form]] (a), ĝ⁻¹(du, du) = ĝ⁻¹(dv, dv) = 0 and
ĝ⁻¹(du, dv) = −1/(2Ω̂²), as du(ê₃) = dv(ê₄) = 1, du(ê₄) = dv(ê₃) = 0 and du, dv vanish on ∂_A.

(b) For covectors ω, ω′, |(g⁻¹ − ĝ⁻¹)(ω, ω′)| ≤ |g⁻¹ − ĝ⁻¹| |ω| |ω′|, and by [[eq:tl5-wg-khat]] |dτ₁|² = (1 + κ′²)/(2Ω̂²)
and |dτ₂|² = (1 + κ²)/(2Ω̂²). With κ_m ≤ κ ≤ 1/4, g⁻¹(dτ₂, dτ₂) ≤ (−κ + κ(1 + 1/16)/2)/Ω̂² = −15κ/(32Ω̂²), likewise for
τ₁, and g⁻¹(dτ₁, dτ₂) ≤ (−(1 + κκ′) + (1/4)(17/16))/(2Ω̂²) < 0. Two timelike covectors with negative product lie in the
same component of the timelike cone, and so does every positive combination; dτ₂ is past directed by definition. For ĝ,
dτ₂(ê₄) = 1 > 0 with ê₄ future directed null.

(c) A past directed timelike covector is positive on every nonzero future directed causal vector, so τ₁ and τ₂
increase strictly along future directed causal curves. At p ∈ N₁, dτ₂(∂_v) = 1 > 0 and ∂_v is null (it is in the
kernel of the degenerate tangent space, hence orthogonal to itself), so ∂_v is future directed. The vector g⁻¹(du) is
orthogonal to T_pN₁, as du vanishes there, so it lies in the kernel of the degenerate form on T_pN₁, which is
spanned by ∂_v: g⁻¹(du) = λ ∂_v with λ = dv(g⁻¹(du)) = g^(uv). Since |g^(uv) − ĝ^(uv)| ≤ κ_m |du| |dv| ≤
1/(8Ω̂²) and ĝ^(uv) = −1/(2Ω̂²), λ < 0. For future directed causal V, g(∂_v, V) ≤ 0, so du(V) = λ g(∂_v, V) ≥ 0. At
a point of {v = 1/2} the same argument with e, for which dτ₂(e) = κ > 0, with g⁻¹(dv) = g^(uv) e and dv(V) =
g^(uv) g(e, V), gives the second statement.

(d) On the first set τ₁ ≤ u* − κ′(v* − 1/2) + κ′(v − 1/2) ≤ u* and τ₂ ≤ v* − κ(u* + 10) + κ(u + 10) ≤ v*. On D^κ_s,
v − 1/2 ≥ 0 and u + 10 ≥ 0, and (v − 1/2) + κ(u + 10) = τ₂ − 1/2 ≤ s − 1/2. ∎

By (d), with v* − 1/2 = 3 and u* ≤ −1, D^κ contains [−10, u* − 3κ′] × [1/2, v* − 9κ] × S³, and for s close to 1/2 the
set D^κ_s is a small neighbourhood of S in D̄.

#### Data and solutions {#sec:tl5-wg-data-solutions}

Let g_N be smooth characteristic data in the gauge satisfying the characteristic constraints
([[def:tl5-cip-data]], [[eq:tl5-cip-constraints]]), with W, b and γ as there; on N₁ its shift is the
solution of the constraint Ric(e₄, ∂_A) = 0 ([[lem:tl5-cip-shift]]), and e₃ = ∂_u + b^A ∂_A on N₀. The
reduced equation needs all components of the metric on N, and the gauge condition on N involves their transverse
derivatives; the data of the reduced problem are therefore given through a metric defined near N. The data on N₀ are
taken on a slightly longer piece N₀⁺ of the cone {v = 1/2}, which the continuation uses near the corner
{u = u*, v = 1/2}.

**Definition {#def:tl5-wg-data}** (Data in the wave gauge.) Let u⁺ ∈ (u*, 0), let g_N be given, as data in the gauge
satisfying the constraints, on N⁺ := N₀⁺ ∪ N₁ with N₀⁺ := [−10, u⁺] × {1/2} × S³ ⊃ N₀. Data in the wave gauge for g_N
are a smooth G-invariant Lorentzian metric G^♯ on a G-invariant open set 𝒰^♯ ⊂ 𝒪̂ that contains N⁺, such that, with
N₀⁺ and N⁺ in place of N₀ and N:

(W1) G^♯(X, Y) = g_N(X, Y) for X, Y tangent to N₀ at a point of N₀, and for X, Y tangent to N₁ at a point of N₁;

(W2) every partial derivative, in the coordinates (u, v, y), of the components of Ric^W(G^♯) and of Υ(G^♯) vanishes
at every point of N;

(W3) the conditions (b) and (c) of [[def:tl5-cip-development]] hold for G^♯ with ι the inclusion: along N₁,
∇^♯_(∂_v) ∂_v = 2 ∂_vW ∂_v, and along N₀, ∇^♯_(e₃) e₃ = 2 e₃(W) e₃, ∇^♯ being the connection of G^♯; and at every
point of S, G^♯(∂_u, ∂_v) = g_N(∂_u, ∂_v) and G^♯(∇^♯_X ∂_v, e₃) = −X(e^(2W)) − γ(X, ∂_v b)/2 for X tangent to S;

(W4) G^♯ is tilted on N, with |G^♯⁻¹ − ĝ⁻¹| < κ_m at every point of N.

By (W1), N₀⁺ and N₁ are null for G^♯, with null directions e₃ and ∂_v. By (W2), Ric(G^♯) also vanishes to infinite
order on N⁺, as Ric(G^♯) − Ric^W(G^♯) is linear in Υ(G^♯) and its first derivatives; and (W2) says in addition that
the coordinates are wave coordinates relative to ĝ along N⁺, to infinite order. Data in the wave gauge exist for smooth
data g_N on N⁺ satisfying the constraints, in particular for the data of the first stage of the problem at 10 l5,
whenever two explicit conditions on N⁺ hold ([[thm:tl5-wg-data]], [[cor:tl5-wg-data-first-stage]]); at the first
stage with u* < −1 they hold for an explicit background built from the seed and the data ([[cor:tl5-xt-data]]), and
for a background with the seed's values and first derivatives on N₀⁺ they follow from explicit inequalities on its
departure from the data along N₁ ([[thm:tl5-xt]]). By
[[lem:tl5-wg-jets]] below, two choices of G^♯ that agree at the points of N have the same derivatives of all orders
there, so only the field G^♯|_N enters, and G^♯ is needed only near N.

**Definition {#def:tl5-wg-solution}** (Solutions of the reduced problem.) For s ∈ (1/2, v*], a solution of the reduced
problem on D^κ_s is a smooth Lorentzian metric g on D^κ_s that is tilted on D^κ_s, satisfies Ric^W(g) = 0 on D^κ_s and
equals G^♯ at every point of N ∩ D^κ_s.

**Lemma {#lem:tl5-wg-jets}** (Transverse derivatives on N.) Let s ∈ (1/2, v*], 𝒰 an open set containing N ∩ D^κ_s,
and g₁, g₂ smooth Lorentzian metrics on D^κ_s ∩ 𝒰 such that every partial derivative of Ric^W(g₁) and of Ric^W(g₂)
vanishes on N ∩ D^κ_s, g₁ = g₂ at every point of N ∩ D^κ_s, and N₀ and N₁ are null for g₁, with null directions e₃
and ∂_v. Then every partial derivative of g₁ − g₂ vanishes on N ∩ D^κ_s.

*Proof.* Write E(g) := Ric^W(g) in the form [[eq:tl5-wg-form]], and N₀ ∩ D^κ_s = [−10, u_s] × {1/2} × S³ with
u_s := min(u*, −10 + (s − 1/2)/κ), N₁ ∩ D^κ_s = {−10} × [1/2, s] × S³ ([[lem:tl5-wg-domains]] (d)).

On N₀, g₁^(vv) = g₂^(vv) = 0, and, as in the proof of [[lem:tl5-wg-domains]] (c), the vector field
V := g₁^(vμ) ∂_μ = g₂^(vμ) ∂_μ is g^(uv) e₃ with g^(uv) ≠ 0: it is tangent to N₀ and transverse to S. Its integral
curves, the reparametrised integral curves of e₃, start on S and fill N₀ ∩ D^κ_s, since b is tangent to the spheres.
We show by induction on k ≥ 1 that ∂_v^k g₁ = ∂_v^k g₂ on N₀ ∩ D^κ_s, the derivatives in v being one-sided. Let
δ_k := ∂_v^k (g₁ − g₂) there, and suppose δ_j = 0 for j < k; then all derivatives of g₁ − g₂ with fewer than k
derivatives in v vanish on N₀ ∩ D^κ_s, being derivatives along N₀ of functions that vanish there. Apply ∂_v^(k−1) to
E(g_i) and restrict to N₀. The term with ∂_v^(k+1) g_i has the coefficient −(1/2) g_i^(vv) = 0. The terms with
∂_v^k g_i are −V(∂_v^k g_i), from the pairs (λ, μ) with exactly one index v, −(1/2)(k − 1) ∂_v g_i^(vv) ∂_v^k g_i
(for k ≥ 2), and ∂Φ/∂(∂_v g)(p, g_i, ∂g_i) ∂_v^k g_i; all other terms contain derivatives of g_i with at most k − 1
derivatives in v. For k ≥ 2 the coefficients of ∂_v^k g_i and the remaining terms are the same for i = 1, 2, so
0 = −V(δ_k) + M δ_k on N₀ ∩ D^κ_s, with M continuous. For k = 1, Φ(p, g, ∂g₁) − Φ(p, g, ∂g₂) =
M′ (∂g₁ − ∂g₂), M′ := ∫₀¹ ∂Φ/∂(∂g)(p, g, ∂g₂ + θ(∂g₁ − ∂g₂)) dθ, and ∂g₁ − ∂g₂ has δ₁ as its only nonzero entries,
so again 0 = −V(δ₁) + M δ₁. In both cases δ_k solves a linear homogeneous system of ordinary differential equations
along the integral curves of V; at S, ∂_v is tangent to N₁, where g₁ = g₂, so δ_k = 0 on S, and δ_k = 0 on
N₀ ∩ D^κ_s. The same induction on N₁ ∩ D^κ_s, with ∂_u in place of ∂_v, g^(uμ) ∂_μ = g^(uv) ∂_v and initial values at S
that are derivatives along N₀, gives ∂_u^k g₁ = ∂_u^k g₂ there. Every partial derivative of g₁ − g₂ at a point of N₀
(of N₁) is a derivative along N₀ (along N₁) of some ∂_v^k (g₁ − g₂) (of some ∂_u^k (g₁ − g₂)), and so vanishes. ∎

**Lemma {#lem:tl5-wg-zero}** (Vanishing for linear wave systems.) Let s ∈ (1/2, v*], g a smooth Lorentzian metric
tilted on D^κ_s, and 𝔓 a linear differential operator of second order on ℝ^m-valued functions on D^κ_s with smooth
coefficients and principal part c g^(λμ) ∂_λ∂_μ times the identity, c a nonzero constant. If w is smooth on D^κ_s,
𝔓w = 0 on D^κ_s and every partial derivative of w vanishes on N ∩ D^κ_s, then w = 0.

*Proof.* Let X := D^κ_s ∩ {τ₁ < u*} ∩ {τ₂ < s} and τ := τ₂ + 1/(u* − τ₁) + 1/(s − τ₂) on X. Then
dτ = (1 + (s − τ₂)⁻²) dτ₂ + (u* − τ₁)⁻² dτ₁ is past directed timelike for g on X ([[lem:tl5-wg-domains]] (b)), and
X ∩ {τ ≤ c} is compact for every c. Let 𝔅 be the set of q ∈ X such that w ≠ 0 at some point of every neighbourhood of
q in D^κ_s; it is closed in X. Suppose 𝔅 ≠ ∅, and let p ∈ 𝔅 be a point where τ attains its minimum T on 𝔅. Then
w = 0 on X ∩ {τ < T} near p.

Near p we use a smooth extension. If p ∉ N, a neighbourhood of p in 𝒬 lies in D^κ_s; put w̃ := w and 𝔓̃ := 𝔓 there. If
p ∈ N, take a box B_p := [a₁, a₂] × [b₁, b₂] × S³ ⊂ D^κ_s with p in its relative interior in D̄ (it exists as
τ₁(p) < u* and τ₂(p) < s), extend the coefficients of 𝔓 and the components of g from B_p by
[[lem:tl5-cip-extend]] (a) to a neighbourhood U_p of p, and let w̃ be w on D^κ_s ∩ U_p and 0 on U_p ∖ D̄. The
function w̃ is smooth by [[lem:tl5-cip-extend]] (d), applied in the charts (u, v, y) with U_p ∩ D̄ as its set F,
whose points not interior to it lie in N for U_p small, since every partial derivative of w vanishes on N; for U_p
small the extended g is Lorentzian, dτ is timelike for it, and the extended operator 𝔓̃ satisfies
𝔓̃w̃ = 0 on U_p, by the equation on D^κ_s and since w̃ = 0 on the rest. In both cases w̃ and all its derivatives vanish
on Σ := {τ = T} near p, being limits from {τ < T} (on D^κ_s ∖ N) or zero (on N and beyond). Σ is a smooth spacelike
hypersurface near p, and every connected open piece Σ₀ ∋ p of it in a neighbourhood U of p small enough is acausal in
U, since τ increases strictly along causal curves. [[lem:tl5-cip-wave]], applied in (U, g) to the operator
−𝔓̃/c, whose principal part is −g^(λμ)∂_λ∂_μ times the identity, gives w̃ = 0 on D⁺(Σ₀); and w̃ = 0 on
D⁻(Σ₀) ⊂ {τ ≤ T}. D(Σ₀) is an open neighbourhood of p ([[thm:std-bgp-development]]), so w = 0 near p, against
p ∈ 𝔅. Hence 𝔅 = ∅, w = 0 on X, and by continuity on D^κ_s. ∎

**Proposition {#prop:tl5-wg-unique}** ((F2_W): uniqueness.) Let g₁ be a solution on D^κ_s and g₂ a solution on
D^κ_(s′). Then g₁ = g₂ on D^κ_(min(s, s′)).

*Proof.* Let s″ := min(s, s′); both restrictions are solutions on D^κ_(s″). By (W1) and [[lem:tl5-wg-jets]], every
partial derivative of δ := g₂ − g₁ vanishes on N ∩ D^κ_(s″). By [[eq:tl5-wg-form]],

    0 = E(g₂) − E(g₁) = −(1/2) g₂^(λμ) ∂_λ∂_μ δ + (1/2) (g₂⁻¹ δ g₁⁻¹)^(λμ) ∂_λ∂_μ g₁ + 𝒜₀ δ + 𝒜₁ ∂δ,

where g₁⁻¹ − g₂⁻¹ = g₂⁻¹ δ g₁⁻¹, and 𝒜₀, 𝒜₁ are the integrals over θ ∈ [0, 1] of the derivatives of Φ in g and in
∂g at (p, g₁ + θδ, ∂g₁ + θ∂δ). These are smooth: by [[lem:tl5-wg-norms]] (b) every g₁ + θδ is Lorentzian. So 𝔓δ = 0
for an operator 𝔓 with smooth coefficients and principal part −(1/2) g₂^(λμ) ∂_λ∂_μ, and [[lem:tl5-wg-zero]], with
g₂ in place of g, gives δ = 0. ∎

**Proposition {#prop:tl5-wg-vacuum}** ((F4_W): the gauge and the symmetry.) Let g be a solution on D^κ_s. Then:

(a) Υ(g) = 0 and Ric(g) = 0 on D^κ_s;

(b) g is G-invariant; so g(∂_(φi), ∂_a) = 0 for a ∈ {u, v, x} and g(∂_(φ1), ∂_(φ2)) = 0 on {|x| < 1}, and h = g − ĝ
lies there in the eight-dimensional space of symmetric 2-tensors with these properties;

(c) g and G^♯ have the same partial derivatives of all orders on N ∩ D^κ_s; in particular (W1) and (W3) hold with g in
place of G^♯ on N ∩ D^κ_s.

*Proof.* (c) is [[lem:tl5-wg-jets]] with 𝒰 := 𝒰^♯, since Ric^W(G^♯) vanishes to infinite order on N by (W2); (W1) and
(W3) involve only the values and the first derivatives of the metric on N.

(a) Let ∇ be the connection of g, Υ_β := g_βμ Υ(g)^μ and S := Ric(g) − Ric^W(g) = Ric(g) on D^κ_s. Since
D̂_β Υ^λ = ∇_β Υ^λ − C^λ_βμ Υ^μ,

    S_αβ = (1/2) (∇_α Υ_β + ∇_β Υ_α) − (1/2) (C_αβμ + C_βαμ) Υ^μ,      C_αβμ := g_αλ C^λ_βμ.

The contracted Bianchi identity ∇^α (Ric_αβ − (1/2) g_αβ g^(γδ) Ric_γδ) = 0 gives
∇^α S_αβ − (1/2) ∇_β (g^(γδ) S_γδ) = 0. Here ∇^α(∇_α Υ_β + ∇_β Υ_α)/2 − ∇_β ∇^α Υ_α/2 = (1/2) ∇^α∇_α Υ_β +
(1/2) g^(αγ) [∇_γ, ∇_β] Υ_α, and the commutator is linear in Υ with coefficients given by the curvature of g; the terms
with C contain at most one derivative of Υ. So Υ_β solves 𝔓Υ = 0 for a linear operator 𝔓 with smooth coefficients
and principal part (1/2) g^(λμ) ∂_λ∂_μ times the identity. Υ(g) is a polynomial in g_μν, g^μν, ∂g and Γ̂, so by (c)
its partial derivatives at points of N ∩ D^κ_s are those of Υ(G^♯), which vanish by (W2). [[lem:tl5-wg-zero]] gives
Υ = 0, and then Ric(g) = Ric^W(g) = 0.

(b) Let σ ∈ G. It acts on S³ alone, so it preserves u, v, τ₁, τ₂, D^κ_s and N, and σ*ĝ = ĝ. By
[[lem:tl5-wg-linear]] (d), Ric^W(σ*g) = σ*Ric^W(g) = 0; σ*g = σ*G^♯ = G^♯ at points of N ∩ D^κ_s, as G^♯ is
G-invariant; and σ*g is tilted, since σ preserves ê₃, ê₄ and Ω̂, hence e₀ and k̂. So σ*g is a solution on D^κ_s, and
σ*g = g by [[prop:tl5-wg-unique]]. The remaining statements follow from the invariance under the rotations and the
reflections φ_i ↦ −φ_i, as in the proof of [[lem:tl5-cip-form]] (b). ∎

#### Local existence and continuation {#sec:tl5-wg-existence}

Existence is reduced to the Cauchy problem, by Rendall's method ([Ren90, p. 221]): near the boundary of the
region already solved, a metric is built that equals the data to infinite order on N; its residual, cut off along N, is
a smooth forcing term for a Cauchy problem posed to the past; and uniqueness on the past side identifies the solution
of that problem with the built metric there, so that it takes the data.

**Lemma {#lem:tl5-wg-cauchy}** (The Cauchy problem near a point.) Let 𝒱 ⊂ 𝒪̂ be open, G a smooth Lorentzian metric on
𝒱, F a smooth symmetric 2-tensor field on 𝒱, t a smooth function on 𝒱 with dt timelike for G, and q ∈ 𝒱. There are
coordinates (τ, z) = (τ, z¹, …, z⁴) on a neighbourhood of q, with τ = t − t(q), z(q) = 0 and
G = G_ττ dτ² + G_ab dz^a dz^b, and numbers r₀ > 0 and C_c ≥ 1 with the following property: on
K₀ := [−r₀, r₀] × B̄_(r₀), B̄_r the closed Euclidean ball of radius r about 0, every vector V that is causal for some
symmetric 2-tensor g′ whose components in the coordinates (u, v, y) of 𝒬 differ from those of G by at most a number
η′ ∈ (0, 1], fixed in the proof, satisfies |V^z| ≤ C_c |V^τ|. For every η″ ∈ (0, η′] there is
ε₀ ∈ (0, r₀/(16 C_c)] such that for every ε ∈ (0, ε₀] there is a smooth Lorentzian metric g on
𝒲_ε := (−2ε, ε) × B_(r₀/2) with Ric^W(g) = F on 𝒲_ε, with g and its first partial derivatives equal to those of G on
𝒲_ε ∩ {τ = −ε}, and with the components of g − G in the coordinates (u, v, y) at most η″ on 𝒲_ε.

*Proof.* (i) *The chart.* Z := −G⁻¹(dt)/G⁻¹(dt, dt) satisfies dt(Z) = 1 and is G-orthogonal to the levels of t, which
are spacelike. Take a chart z of the level {t = t(q)} near q with z(q) = 0 and transport it along the flow of Z: in
the resulting coordinates (τ, z), ∂_τ = Z, so G(∂_τ, ∂_a) = 0, G_ττ = G(Z, Z) < 0 and (G_ab) is positive definite.
Choose r₀ > 0 so small that K₀ lies in the chart, and c₀ > 0 with −G^(ττ) ≥ 2c₀ and G^(ab) ξ_a ξ_b ≥ 2c₀ |ξ|² on
K₀. A vector with V^τ = 0 is G-spacelike; by continuity and compactness there is η′ ∈ (0, 1] such that it is spacelike
also for every g′ with |g′ − G| ≤ η′ in the components in (u, v, y) at points of K₀, and such that these g′ are
Lorentzian with −g′^(ττ) ≥ c₀ and g′^(ab) ξ_a ξ_b ≥ c₀ |ξ|². Then |V^z|/|V^τ| is bounded on the compact set of such
(p, g′, V) with V causal for g′ and |V^τ|² + |V^z|² = 1; let C_c ≥ 1 be a bound.

(ii) *The equation.* Let w be the array of the fifteen components of g − G in the coordinates (u, v, y) of 𝒬, as
functions of (τ, z). By [[eq:tl5-wg-form]], Ric^W(G + w) = F reads

    −(1/2) (G + w)^(λμ) ∂_λ∂_μ w + Ψ(p, w, ∂w) = 0,    Ψ := Φ(p, G + w, ∂G + ∂w) − (1/2) (G + w)^(λμ) ∂_λ∂_μ G − F,

and in the coordinates (τ, z) it takes the same form, −(1/2) (G + w)^(αβ) ∂_α∂_β w + Ψ̃(τ, z, w, ∂w) = 0, the
indices now referring to (τ, z) and Ψ̃ smooth where G + w is Lorentzian. Let ε₂ := η″.

(iii) *The modified system.* As in Step 8 (iii) of [[sec:ue-existence]], let ϒ: ℝ¹⁵ → ℝ¹⁵ be smooth with ϒ(w) = w for |w|
≤ ε₂/2 and |ϒ(w)| ≤ ε₂ (maximum of the components), and χ a smooth function of (τ, z) with compact support in the
interior of K₀, equal to 1 on [−r₀/2, r₀/2] × B̄_(r₀/2). Replace (G + w)^(αβ) by 𝔤^(αβ) := χ (G + ϒ(w))^(αβ) + (1 − χ)
m^(αβ), m := −dτ² + Σ (dz^a)², and Ψ̃ by χ Ψ̃(τ, z, ϒ(w), ∂w). The conditions 𝔤^(ττ) ≤ −min(c₀, 1) and 𝔤^(ab) ξ_a ξ_b ≥
min(c₀, 1) |ξ|² are convex in 𝔤⁻¹ and hold for both terms, so they hold for every value of w. Outside K₀ the system is
the wave equation of m, so it may be posed on ℝ × 𝕋⁴_L, 𝕋⁴_L a torus of period L > 2r₀ in z. In V := (w, ∂_τ w, ∂_z w)
it is the first-order system of Step 8 (iii) of [[sec:ue-existence]], with 𝔤 in place of g there and −χΨ̃ in place of F̃;
the calculation there of its symmetrizer and of its eigenvalues ζ_− < 0 < ζ_+ and 0 uses only that 𝔤^(ττ) < 0 and that
(𝔤^(ab)) is positive definite, so the system satisfies (A1)–(A4) of [DS23] on the whole state space, with bounds
uniform in τ, its coefficients being independent of τ outside [−r₀, r₀]. The relation between the last components of V
and ∂_z w propagates, as there.

(iv) *The initial time.* For σ ∈ [−r₀/2, r₀/2] consider W(τ′) := V(σ + τ′), which solves the system with coefficients
and forcing term at σ + τ′, and adjoin σ as an unknown with ∂_(τ′)σ = 0; this adds the eigenvalue 0, which the symbol has
already, so (A1)–(A4) still hold. [[thm:std-ds-existence]] at the datum (W, σ) = (0, 0), with r := 4, gives T₀ > 0
and a solution W₀ on [−T₀, T₀], and by [[thm:std-ds-stability]], applied to sequences σ_n → 0, there is σ₁ > 0 such
that for |σ| ≤ σ₁ the solution W_σ with datum (0, σ) exists on [−T₀, T₀] and sup_(|τ′|≤T₀) ‖W_σ(τ′) − W₀(τ′)‖_r ≤ ϑ,
for any given ϑ > 0. As H⁴(𝕋⁴_L) lies in the continuous functions, with a norm bound ([[thm:std-bh-manifold]]), and W₀
is continuous into H⁴ with
W₀(0) = 0, there are τ₁ ∈ (0, T₀] and σ₂ ∈ (0, σ₁] with |W_σ(τ′)| ≤ ε₂/2 for |τ′| ≤ τ₁ and |σ| ≤ σ₂. Put
ε₀ := min(σ₂, τ₁/3, r₀/(16 C_c), r₀/4). For ε ∈ (0, ε₀], V := W_(−ε)(· + ε) solves the modified system on
[−2ε, ε], V(−ε) = 0, and |V| ≤ ε₂/2 there, since τ + ε ∈ [−ε, 2ε] ⊂ [−τ₁, τ₁].

(v) *Conclusion.* By the first clause of [[thm:std-ds-continuation]] at every r ≥ 4, V lies in C(H^r) for every r, and
it is smooth, as in Step 8 (iv) of [[sec:ue-existence]]. On 𝒲_ε, χ = 1 and ϒ(w) = w, so w solves the equation of (ii),
g := G + w is Lorentzian with Ric^W(g) = F, |g − G| ≤ ε₂/2 ≤ η″, and at τ = −ε, w = 0, ∂_τ w = 0 and ∂_z w = 0. ∎

**Lemma {#lem:tl5-wg-nullfn}** (Null functions near N.) Let G be a smooth Lorentzian metric on an open set 𝒱 ⊂ 𝒪̂, and
q ∈ 𝒱 ∩ N₁ with v(q) < v*. Suppose that the tangent spaces of N₁ ∩ 𝒱 are degenerate for G with kernel spanned by ∂_v,
and that du(V) ≥ 0 for every future directed G-causal vector V at points of N₁ ∩ 𝒱. Then there are an open
neighbourhood U ⊂ 𝒱 of q that is a coordinate box (u(q) − a, u(q) + a) × (v(q) − a, v(q) + a) × U′, U′ open in S³, and
a smooth function ũ on U with G⁻¹(dũ, dũ) = 0, ∂_uũ > 0, ũ = −10 on U ∩ N₁ and dũ(V) ≥ 0 for every future directed
G-causal V on U; so ũ does not increase along past directed G-causal curves in U, {ũ < −10} is a past set in U, and on
U ∩ {v ≥ 1/2} the sign of ũ + 10 is that of u + 10. If v(q) > 1/2, U may be taken in {v > 1/2}, and then
{ũ < −10} = U ∩ {u < −10} and {ũ = −10} = U ∩ N₁. Likewise, let q ∈ 𝒱 ∩ N₀⁺ with u(q) < u⁺, let the tangent spaces of
N₀⁺ ∩ 𝒱 be degenerate for G with kernel spanned by a vector field e with du(e) = 1, and let dv(V) ≥ 0 for every future
directed G-causal V at points of N₀⁺ ∩ 𝒱. Then there are such a box U and a smooth function ṽ on U with
G⁻¹(dṽ, dṽ) = 0, ∂_vṽ > 0, ṽ = 1/2 on U ∩ N₀⁺ and dṽ(V) ≥ 0 for every future directed G-causal V on U; so
{ṽ < 1/2} is a past set in U, and on U ∩ {u ≥ −10} the sign of ṽ − 1/2 is that of v − 1/2. If u(q) > −10, U may be
taken in {u > −10}, and then {ṽ < 1/2} = U ∩ {v < 1/2} and {ṽ = 1/2} = U ∩ N₀⁺.

*Proof.* Let v_q := v(q) and, for c near −10, 𝒮_c := {u = c, v = v_q} near q. At q, G is positive semidefinite on
T_qN₁ with kernel ∂_v, so it is positive definite on the tangent space of the leaf; hence the 𝒮_c are spacelike near
q. At each of their points the G-orthogonal complement of T𝒮_c is a timelike 2-plane containing two null lines, which
depend smoothly on the point; let K(c, y) be the future directed null normal of 𝒮_c with dv(K) = 1 that equals ∂_v at
points of 𝒮_(−10) ⊂ N₁, where ∂_v is a null normal. Let Θ(c, λ, y) := exp_((c, v_q, y))(λ K(c, y)). At
(−10, 0, y(q)), dΘ maps ∂_c, ∂_λ and ∂_(y^A) to ∂_u, ∂_v and ∂_A, so Θ is a diffeomorphism of a neighbourhood of that
point onto a neighbourhood U of q; put ũ := c ∘ Θ⁻¹. For c = −10 the curves λ ↦ Θ(−10, λ, y) are null geodesics
tangent to ∂_v at their initial points, so their arcs in N₁ (λ ≥ 0, and all λ if v_q > 1/2) are reparametrised
generators of N₁ (the generators of a null hypersurface are null pregeodesics); for U small these arcs cover U ∩ N₁, so
ũ = −10 on U ∩ N₁, and {ũ = −10} = U ∩ N₁ if v_q > 1/2. The level sets of ũ are null: their tangent
spaces are spanned by J₀ := ∂_λΘ, null, and the Jacobi fields J := ∂_(y^A)Θ, and ∂_λ G(J, J₀) = G(∇_J J₀, J₀) =
J(G(J₀, J₀))/2 = 0 with G(J, J₀) = 0 at λ = 0, as K is normal to 𝒮_c; so G⁻¹(dũ, dũ) = 0. As dũ(∂_u) = 1 at q, for
U small ∂_uũ > 0 on U and dũ = ϱ du on U ∩ N₁ with ϱ > 0, which gives dũ(V) ≥ 0 on U ∩ N₁. Shrinking U to a box as
stated, ũ = −10 at the points (−10, v, y) of U with v ≥ 1/2 and ∂_uũ > 0 give the sign of ũ + 10 on U ∩ {v ≥ 1/2},
and, if v_q > 1/2 and a < v_q − 1/2, the description of {ũ < −10};
since dũ is a nowhere vanishing null covector field on U, taken connected, the sign of dũ on future directed causal
vectors is the same everywhere. A past directed causal curve in U along which ũ does not increase cannot leave
{ũ < −10}. The second statement is proved in the same way, with 𝒮_c := {v = c, u = u(q)} and the null normal tangent
to N₀⁺ at c = 1/2. ∎

Below, Q₊ := {u ≥ −10} ∩ {v ≥ 1/2} ⊂ 𝒬, and K_s := D^κ ∩ {τ₂ = s} is the front of D^κ_s; K_(1/2) = S.

**Proposition {#prop:tl5-wg-local}** ((F1_W) and (F3_W): existence and continuation.) Let G^♯ be data in the wave
gauge for g_N.

(a) There are s₁ ∈ (1/2, v*] and a solution of the reduced problem on D^κ_(s₁).

(b) Let s ∈ (1/2, v*) and g a solution on D^κ_s with |g⁻¹ − ĝ⁻¹| < κ_m at every point of D^κ_s. Then there are
s′ ∈ (s, v*] and a solution g′ on D^κ_(s′) with g′ = g on D^κ_s.

*Proof.* We treat (a) as the case s = 1/2 of (b), with D^κ_(1/2) = S and g := G^♯ on S; the hypothesis of (b) is then
(W4). Fix q ∈ K_s.

*Step 1 (a metric near q).* Near q, D^κ_s coincides with a set {ε₁ w₁ ≥ ε₁ a₁} ∩ {τ₂ ≤ s}, where (w₁, ε₁, a₁) is
(u, 1, −10) if q ∈ N₁, (v, 1, 1/2) if q ∈ N₀, (τ₁, −1, u*) if τ₁(q) = u* and q ∉ N₀, and where the first condition is
absent otherwise: at a point of K_s ∩ N₀ ∩ {τ₁ = u*}, that is u = u*, v = 1/2, the conditions v ≥ 1/2 and τ₂ ≤ s
imply κ(u − u*) ≤ 1/2 − v ≤ 0 and then τ₁ − u* ≤ (u − u*)(1 − κκ′) ≤ 0; and N₀ ∩ N₁ = S, where τ₂ = 1/2 < s. In
the coordinates (w₁, τ₂, y), with w₁ := u where the first condition is absent, D^κ_s is a box near q if s > 1/2. If
s = 1/2, let G_q := G^♯. If s > 1/2, extend g from the box by [[lem:tl5-cip-extend]] (a), after the affine
change of variables (u, v) ↦ (w₁, τ₂), to a smooth metric g_E on an open neighbourhood of q, and put G_q := g_E if
q ∉ N.
If q ∈ N₁, in the coordinates (u, τ₂, y) let d_k(τ₂, y) := ∂_u^k (G^♯ − g_E)(−10, τ₂, y) for τ₂ ≥ s and d_k := 0 for
τ₂ < s. By [[prop:tl5-wg-vacuum]] (c), g and G^♯ have the same derivatives of all orders on N₁ ∩ D^κ_s, so d_k and all
its derivatives vanish at τ₂ = s, and d_k is smooth by [[lem:tl5-cip-extend]] (b). Fix χ₀ ∈ C_c^∞(ℝ) with
χ₀ = 1 near 0 and choose ε_k ∈ (0, 1] so small that the term c_k := χ₀((u + 10)/ε_k) (u + 10)^k d_k(τ₂, y)/k! has
all its derivatives of order less than k bounded by 2^(−k) on a fixed compact neighbourhood of q; this is possible as
each such derivative is a sum of terms bounded by a constant times ε_k. Then c := Σ_k c_k converges with all
derivatives, ∂_u^k c = d_k at u = −10 (near u = −10 the terms with index m < k are polynomials of degree m in u + 10,
and those with m > k vanish to order m there), and c = 0 for τ₂ ≤ s. Put G_q := g_E + c. If q ∈ N₀, do the same in
the coordinates (v, τ₂, y), with ∂_v and v = 1/2, and with G^♯ on N₀⁺. In all cases, on a small open neighbourhood
𝒱_q of q, G_q is smooth and |G_q⁻¹ − ĝ⁻¹| < κ_m, by continuity, since c = 0 at q; and:

(P1) G_q = g on D^κ_s ∩ 𝒱_q;

(P2) every partial derivative of G_q − G^♯ vanishes at the points of N⁺ ∩ 𝒱_q; on N⁺ ∩ D^κ_s by (P1) and
[[prop:tl5-wg-vacuum]] (c), elsewhere by the choice of c;

(P3) Ric^W(G_q) = 0 on D^κ_s ∩ 𝒱_q, by (P1), and every partial derivative of Ric^W(G_q) vanishes at the points of
N⁺ ∩ 𝒱_q, by (P2) and (W2).

Shrinking 𝒱_q, we may assume that 𝒱_q ∩ ∂Q₊ ⊂ N⁺: since s < v*, q ∈ N₁ has v(q) < v*, and q ∈ N₀ has u(q) ≤ u* < u⁺.

*Step 2 (the forcing term and the past region).* Let F_q := Ric^W(G_q) on 𝒱_q ∖ Q₊ and F_q := 0 on 𝒱_q ∩ Q₊. By (P3) and
[[lem:tl5-cip-extend]] (d), applied in the charts (u, v, y) with the closure of 𝒱_q ∖ Q₊ in 𝒱_q as its set F,
whose points not interior to it lie in 𝒱_q ∩ ∂Q₊ ⊂ N⁺, F_q is smooth. Let

    R_q := (𝒱_q ∖ Q₊) ∪ (𝒱_q ∩ {τ₁ < u*} ∩ {τ₂ < s}).

On 𝒱_q ∩ Q₊ ∩ {τ₁ < u*} ∩ {τ₂ < s} ⊂ D^κ_s, Ric^W(G_q) = 0 = F_q; so Ric^W(G_q) = F_q on R_q. By
[[lem:tl5-wg-domains]] (c) and (W1), [[lem:tl5-wg-nullfn]] applies to G_q at q if q ∈ N₁ or q ∈ N₀ (both if q ∈ S);
shrinking 𝒱_q to a coordinate box U_q about q on which the null functions ũ, ṽ of that lemma exist, R_q is the union
of the sets {ũ < −10} (if q ∈ N₁), {ṽ < 1/2} (if q ∈ N₀) and U_q ∩ {τ₁ < u*} ∩ {τ₂ < s}. If q ∉ S, this is the
description of {ũ < −10} or of {ṽ < 1/2} in that lemma. If q ∈ S, then s = 1/2 and R_q = U_q ∖ Q₊; by the signs of
ũ + 10 on U_q ∩ {v ≥ 1/2} and of ṽ − 1/2 on U_q ∩ {u ≥ −10}, the first two sets do not meet Q₊ and contain
U_q ∩ {u < −10} ∩ {v ≥ 1/2} and U_q ∩ {u ≥ −10} ∩ {v < 1/2} respectively, and U_q ∩ {u < −10} ∩ {v < 1/2} lies in
the third set, as τ₁ < −10 < u* and τ₂ < 1/2 there. Each of the three sets is a past set in U_q for G_q: along past
directed causal curves ũ, ṽ, τ₁ and τ₂ do not increase ([[lem:tl5-wg-domains]] (b)).

*Step 3 (the Cauchy problem).* Apply [[lem:tl5-wg-cauchy]] to (U_q, G_q, F_q, τ₂, q), with η″ ≤ η′ so small that every
metric within η″ of G_q in components at the points of K₀ is tilted with strict inequality; this is possible by
continuity, as G_q is so near q. Let ε ∈ (0, ε₀] be so small that 𝒲_ε ⊂ U_q, and let g_q be the metric on 𝒲_ε.

*Step 4 (the past side).* Let δ := g_q − G_q on 𝒲_ε. On R_q ∩ 𝒲_ε both metrics satisfy Ric^W(·) = F_q, so, as in the
proof of [[prop:tl5-wg-unique]] with the roles arranged so that the principal part comes from G_q, 𝔓δ = 0 there for a
linear operator 𝔓 with smooth coefficients on 𝒲_ε and principal part −(1/2) G_q^(λμ) ∂_λ∂_μ. Let

    𝒞 := {(τ, z) : −2ε < τ < ε, |z| < r₀/2 − C_c (τ + 2ε)},      X := 𝒞 ∩ R_q,

and w := δ on X ∩ {τ ≥ −ε}, w := 0 on X ∩ {τ < −ε}. As δ and its first derivatives vanish on {τ = −ε}, w is of class C¹
and smooth on both sides, so its second derivatives in the sense of distributions are the pointwise ones off {τ = −ε},
and 2𝔓w = 0 on X, with supp w ⊂ {τ > −3ε/2}. We apply [[lem:ii-f-1-3]] on (X, G_q) to the operator 2𝔓, whose
principal symbol is G_q⁻¹(ζ, ζ) times the identity, with the time function τ and c := −3ε/2. Let p ∈ X with τ(p) > c. A
past directed G_q-causal curve in X from p, parametrised by τ, satisfies |dz/dτ| ≤ C_c, so |z| ≤ |z(p)| + C_c(τ(p) − τ)
along it; and it stays in each of the past sets of Step 2 that contain p, on which, respectively, ũ ≤ ũ(p), ṽ ≤ ṽ(p),
or τ₁ ≤ τ₁(p) and τ₂ ≤ τ₂(p). So J⁻_X(p) ∩ {τ ≥ c} lies in the set L_p of the points with c ≤ τ ≤ τ(p), |z| ≤ |z(p)| +
C_c(τ(p) − τ) and these inequalities, which is compact and, since |z(p)| + C_c(τ(p) − τ) < r₀/2 − C_c(τ + 2ε) for p ∈
𝒞, lies in X. By [[lem:ii-f-1-3]], w = 0. So g_q = G_q on X ∩ {τ ≥ −ε}, which contains R_q ∩ 𝒲′ for 𝒲′ := (−ε, ε) ×
B_(r₀/8), since r₀/2 − 3C_c ε ≥ r₀/8.

*Step 5 (the local solution).* On Q₊ ∩ 𝒲′: g_q = G_q = g on D^κ_s ∩ 𝒲′, by Step 4 and (P1), first on the interior of
D^κ_s ∩ R_q and then by continuity, with all derivatives; at the points of N ∩ 𝒲′, which are limits of points of
𝒲′ ∖ Q₊ ⊂ R_q, g_q = G_q = G^♯ by (P2); Ric^W(g_q) = F_q = 0; and g_q is tilted on 𝒲′ by the choice of η″.

*Step 6 (agreement of two local solutions).* Let q, q′ ∈ K_s, with local solutions g_q on Q₊ ∩ 𝒲′_q and g_(q′) on
Q₊ ∩ 𝒲′_(q′) as in Step 5, 𝒲′_q and 𝒲′_(q′) being the sets 𝒲′ of Step 4 for q and q′, and let
p ∈ K_s ∩ 𝒲′_q ∩ 𝒲′_(q′). Then δ := g_q − g_(q′) is smooth near p
(both metrics are defined on open sets by [[lem:tl5-wg-cauchy]]), vanishes on D^κ_s near p by Step 5, and vanishes with
all its derivatives at the points of N, since by Step 4 and (P2) both metrics equal G^♯ to infinite order there. So
δ̃ := δ on Q₊ and δ̃ := 0 off Q₊ is smooth on {τ₁ < u*} near p ([[lem:tl5-cip-extend]] (d), with
Q₊ ∩ {τ₁ < u*} near p as its set F, whose points not interior to it lie in N), vanishes on {τ₁ < u*} ∩ {τ₂ ≤ s}, as
Q₊ ∩ {τ₁ < u*} ∩ {τ₂ ≤ s} ⊂ D^κ_s, and satisfies 2𝔓̃δ̃ = 0 for the operator 𝔓̃ of the proof of [[prop:tl5-wg-unique]]
built from g_q and g_(q′), with principal part −(1/2) g_q^(λμ) ∂_λ∂_μ: on Q₊ as both are solutions, and off Q₊ as
δ̃ = 0. In the chart of
[[lem:tl5-wg-cauchy]] for q, where τ(p) = 0, take ρ > 0 and ε′ ∈ (0, ρ/(4C_c)] with

    𝒞_p := {(τ, z) : −2ε′ < τ < ε′, |z − z(p)| < ρ − C_c (τ + 2ε′)} ⊂ 𝒲′_q ∩ 𝒲′_(q′).

C_c bounds |dz/dτ| along g_q-causal curves, as g_q is within η″ ≤ η′ of G_q. As in Step 4, with
X := 𝒞_p ∩ {τ₁ < u*}, the past set {τ₁ < u*}, on which τ₁ ≤ τ₁(p′) along past directed causal curves from p′, and
c := −ε′, [[lem:ii-f-1-3]] gives δ̃ = 0 on X; so g_q = g_(q′) on Q₊ ∩ {τ₁ ≤ u*} ∩ 𝒞_p, by continuity, and 𝒞_p is a
neighbourhood of p.

*Step 7 (gluing).* Choose q₁, …, q_n ∈ K_s and open sets 𝒲″_j with compact closures in the sets 𝒲′_j of Step 4 for q_j,
such that the 𝒲″_j cover the compact set K_s, and let g_j be the local solutions. For each i, j the compact set K_s ∩
𝒲̄″_i ∩ 𝒲̄″_j ⊂ 𝒲′_i ∩ 𝒲′_j is covered by finitely many of the neighbourhoods of Step 6, so g_i = g_j on
Q₊ ∩ {τ₁ ≤ u*} ∩ O_ij for an open set O_ij containing it. With Y_(s′) the closure of D^κ_(s′) ∖ D^κ_s, the compact sets
Y_(s′) ∩ 𝒲̄″_i ∩ 𝒲̄″_j and Y_(s′) ∖ ⋃_j 𝒲″_j decrease, as s′ decreases to s, to subsets of K_s ∩ 𝒲̄″_i ∩ 𝒲̄″_j and to
the empty set, so there is s′ ∈ (s, v*] with D^κ_(s′) ∖ D^κ_s ⊂ ⋃_j 𝒲″_j and (D^κ_(s′) ∖ D^κ_s) ∩ 𝒲″_i ∩ 𝒲″_j ⊂ O_ij
for all i, j. Let g′ := g on D^κ_s and g′ := g_j on (D^κ_(s′) ∖ D^κ_s) ∩ 𝒲″_j; this is well defined, as D^κ_(s′) ∖
D^κ_s ⊂ Q₊ ∩ {τ₁ ≤ u*}. Since g_j = g on D^κ_s ∩ 𝒲′_j (Step 5), g′ = g_j on D^κ_(s′) ∩ 𝒲″_j, so g′ is smooth on
D^κ_(s′); it is tilted, satisfies Ric^W(g′) = 0, and equals G^♯ at the points of N ∩ D^κ_(s′). So it is a solution on
D^κ_(s′) extending g. For s = 1/2 this is (a), with s₁ := s′. ∎

**Theorem {#thm:tl5-wg}** (The reduced problem.) Let ĝ be a background, κ and κ′ as in [[def:tl5-wg-domains]], g_N
smooth characteristic data in the gauge satisfying the constraints on N⁺, and G^♯ data in the wave gauge for g_N.

(F1_W) There are s₁ ∈ (1/2, v*] and a solution of the reduced problem on D^κ_(s₁).

(F2_W) Two solutions of the reduced problem, on D^κ_s and on D^κ_(s′), coincide on D^κ_(min(s, s′)).

(F3_W) A solution g on D^κ_s with s < v* and |g⁻¹ − ĝ⁻¹| < κ_m on D^κ_s is the restriction of a solution on
D^κ_(s′) for some s′ ∈ (s, v*].

(F4_W) Every solution g on D^κ_s is a G-invariant vacuum metric in the wave gauge, Υ(g) = 0, and has on N ∩ D^κ_s the
derivatives of all orders of G^♯; so it satisfies (a)–(c) of [[def:tl5-cip-development]] on N ∩ D^κ_s with
ι the inclusion, and g − ĝ lies in the eight-dimensional class subspace of [[prop:tl5-wg-vacuum]] (b).

*Proof.* (F1_W) and (F3_W) are [[prop:tl5-wg-local]], (F2_W) is [[prop:tl5-wg-unique]], and (F4_W) is
[[prop:tl5-wg-vacuum]], with (W1) and (W3). ∎

**Remark {#rem:tl5-wg-continuation}** (Use in the continuation argument.) The proof of [[lem:tl5-continuation]] uses of
the regions D_s only that they increase with s, that a solution on D_s restricts to solutions on D_σ, σ < s, that
D_(s̄) is the closure of ⋃_(s<s̄) D_s and a smooth function on that union whose derivatives of every order are bounded
extends smoothly to D_(s̄), that the conditions defining a solution pass to such limits, and (F1)–(F3). The regions
D^κ_s and the solutions of the reduced problem have these properties, the tilt |g⁻¹ − ĝ⁻¹| ≤ κ_m being a closed
condition, and [[thm:tl5-wg]] supplies (F1)–(F3), with the strict tilt in (F3_W) as an extra hypothesis that an a
priori bound y ≤ 2A must imply. By [[lem:tl5-wg-norms]] (a), |h| ≤ κ_m/2 at a point gives |g⁻¹ − ĝ⁻¹| ≤ κ_m, with
strict inequality if |h| < κ_m/2. A solution obtained on D^κ in this way is put into the double-null gauge by
[[thm:tl5-dn]].

#### Data in the wave gauge from a development {#sec:tl5-wg-first-stage}

We construct data in the wave gauge ([[def:tl5-wg-data]]) from a vacuum development of the data: a G-invariant vacuum
metric in double-null form on a one-sided neighbourhood of all of N⁺ ([[lem:tl5-wg-lchart]]), pushed forward by a map
that is the identity on N⁺ and, to infinite order on N⁺, a wave map to (𝒪̂, ĝ) ([[lem:tl5-wg-wavemap]]). Its first
transverse derivative on N⁺ solves an explicit linear transport equation ([[lem:tl5-wg-tension]]), which gives the
explicit conditions of [[thm:tl5-wg-data]] for the invertibility of the map and for (W4). [[sec:tl5-xt]] shows that
they hold at the first stage when u* < −1, for an explicit background.

**Lemma {#lem:tl5-wg-lchart}** (A double-null development near N⁺.) Let g_N be smooth data in the gauge on N⁺
satisfying the constraints. There are δ ∈ (0, v* − 1/2] with δ ≤ u⁺ + 10 and a G-invariant vacuum metric g′ in
double-null form on

    𝒩_δ := D′₀ ∪ D′₁,   D′₀ := [−10, u⁺] × [1/2, 1/2 + δ] × S³,   D′₁ := [−10, −10 + δ] × [1/2, v*] × S³,

with g′ = g_N at every point of N⁺.

*Proof.* *The development.* By [[lem:tl5-cip-data-extend]], with u⁺ in place of u*, there are η > 0 with u⁺ + η < 0 and
data in the gauge on N⁺_η := ([−10, u⁺ + η] × {1/2} × S³) ∪ ({−10} × [1/2, v* + η] × S³) that satisfy the constraints
and restrict to g_N on N⁺. By [[thm:std-ctg-neighbourhood]], in the form stated in [[sec:tl5-cip-existence]] (smooth
data in the gauge satisfying [[eq:tl5-cip-constraints]] have a development), these data have a development (M̃, g̃, M,
ι) ([[def:tl5-cip-development]], with N⁺_η, u⁺ + η and v* + η in place of N, u* and v*). We use that a smooth map from
a relatively open subset of [a, b] × ℝ × S³ to M̃ that has invertible differential at the points of a compact set 𝒦 and
is injective on 𝒦 is a diffeomorphism of a neighbourhood of 𝒦 in its domain onto its image: near each point it extends
smoothly ([[lem:tl5-cip-extend]] (a), in charts of M̃) to a local diffeomorphism, and injectivity on a neighbourhood of
𝒦 follows from that on 𝒦 by compactness. Let V̲ := dι(e₃) on ι(N₀⁺_η) and V := dι(∂_v) on ι(N₁_η), N₀⁺_η and N₁_η being
the two parts of N⁺_η; they are future directed by (b) of [[def:tl5-cip-development]], by (a) they span the kernels of
the degenerate tangent spaces of the null hypersurfaces ι(N₀⁺_η) and ι(N₁_η), whose generators are the images of the
integral curves of e₃ and of the curves {u = −10, y constant}, and by (c), g̃(V, V̲) = g_N(∂_v, ∂_u) = −2e^(2W) at the
points of ι(S).

(1) *The function v.* For d ∈ [1/2, v* + η] let L_d := ι({−10} × {d} × S³), a spacelike leaf of ι(N₁_η), and K(d, y)
the future directed null normal of L_d at ι(−10, d, y) with g̃(K, V) = −2, transverse to ι(N₁_η). At d = 1/2 the null
normal of ι(S) transverse to ι(N₁_η) is that of V̲, which is null, orthogonal to the tangent space of ι(N₀⁺_η) and not
orthogonal to V; so K(1/2, y) = e^(−2W) V̲, and t ↦ exp(tK(1/2, y)) is, up to parametrization, the generator of
ι(N₀⁺_η) through ι(−10, 1/2, y), the generators of a null hypersurface being null pregeodesics. Let t_*(y) be its
affine parameter at the point where u = u⁺. Ξ(d, t, y) := exp_(ι(−10, d, y))(t K(d, y)) is smooth on a relatively open
subset of [1/2, v* + η] × ℝ × S³ containing 𝒦₁ := {(1/2, t, y) : 0 ≤ t ≤ t_*(y)} ∪ ([1/2, v* + η/2] × {0} × S³). At the
points of 𝒦₁ with t = 0, ∂_dΞ = V and the ∂_(y^A)Ξ = dι ∂_A span the tangent space of ι(N₁_η), and ∂_tΞ = K is
transverse to it, as g̃(K, V) ≠ 0 while V is orthogonal to that tangent space. Along t ↦ Ξ(1/2, t, y), J := ∂_dΞ is a
Jacobi field, and as all the curves t ↦ Ξ(d, t, y) are null geodesics, ∂_t g̃(J, ∂_tΞ) = g̃(∇̃_J ∂_tΞ, ∂_tΞ) =
J(g̃(∂_tΞ, ∂_tΞ))/2 = 0, so g̃(J, ∂_tΞ) = g̃(V, K) = −2; since ∂_tΞ spans the null normal direction of ι(N₀⁺_η), J is
transverse to ι(N₀⁺_η), while (t, y) ↦ Ξ(1/2, t, y) is ι composed with a diffeomorphism onto N₀⁺, the affine parameter
increasing along each generator. So dΞ is invertible on 𝒦₁; and Ξ is injective on 𝒦₁, as ι is injective and the two
parts of 𝒦₁ are mapped onto ι(N₀⁺) and ι({−10} × [1/2, v* + η/2] × S³), whose intersection ι(S) is the image of the
common points (1/2, 0, y). Hence Ξ is a diffeomorphism of a neighbourhood 𝒜 of 𝒦₁ in its domain onto its image 𝒱; put
v := d ∘ Ξ⁻¹ on 𝒱. Then v = d on L_d, v = 1/2 on ι(N₀⁺), and 𝒱 is a neighbourhood in M̃ of every point of ι({−10} ×
(1/2, v* + η/2) × S³). The tangent space of a level set H_d := Ξ(𝒜 ∩ {d} × ℝ × S³) is spanned by ∂_tΞ, which is null,
and by the Jacobi fields ∂_(y^A)Ξ, with g̃(∂_(y^A)Ξ, ∂_tΞ) constant in t by the same calculation and zero at t = 0, as
K is normal to L_d; so H_d is a null hypersurface, and g̃⁻¹(dv, dv) = 0 on 𝒱.

(2) *The function u and the angles.* For c ∈ [−10, u⁺] let S_c := ι({c} × {1/2} × S³), a spacelike leaf of ι(N₀⁺_η),
and L(c, y) its future directed null normal at ι(c, 1/2, y) transverse to ι(N₀⁺_η) with g̃(L, V̲) = −2e^(2W). As in
(1), L(−10, y) = V, so λ ↦ exp(λ L(−10, y)) is the generator of ι(N₁_η) through ι(−10, 1/2, y), equal to ι(−10, ν(λ,
y), y) with ν(0, y) = 1/2 and ∂_λν > 0; let λ_*(y) be defined by ν(λ_*(y), y) = v* + η/4. Θ(c, λ, y) := exp_(ι(c, 1/2,
y))(λ L(c, y)) is smooth on a relatively open subset of [−10, u⁺] × ℝ × S³ containing 𝒦₀ := ([−10, u⁺] × {0} × S³) ∪
{(−10, λ, y) : 0 ≤ λ ≤ λ_*(y)}. At λ = 0, ∂_cΘ = dι ∂_u and the ∂_(y^A)Θ = dι ∂_A span the tangent space of ι(N₀⁺_η),
and ∂_λΘ = L is transverse to it; at c = −10, ∂_λΘ and the ∂_(y^A)Θ span the tangent space of ι(N₁_η), and J̲ := ∂_cΘ
is a Jacobi field with g̃(J̲, ∂_λΘ) constant in λ, as in (1), equal at λ = 0 to g̃(dι ∂_u, V) = −2e^(2W) ≠ 0, so that
J̲ is transverse to ι(N₁_η). So dΘ is invertible on 𝒦₀, Θ is injective on 𝒦₀ as Ξ is on 𝒦₁, and Θ is a diffeomorphism
of a neighbourhood ℬ of 𝒦₀ in its domain onto its image 𝒰. Put u := c ∘ Θ⁻¹, and let y also denote the third component
of Θ⁻¹. By the calculation of (1), with L normal to S_c, the level sets C_c of u are null hypersurfaces, so g̃⁻¹(du,
du) = 0 on 𝒰, and their generators, along which y is constant, are the curves λ ↦ Θ(c, λ, y), tangent to the null
vector ∇u, which is orthogonal to C_c.

(3) *The chart.* At a point of ι(N₀⁺) the linear form g̃(·, V̲) vanishes on the tangent space of ι(N₀⁺_η) and is
negative on L and on J, as ∂_tΞ is a positive multiple of V̲ and g̃(J, ∂_tΞ) = −2; so L = κJ + Y with κ > 0 and Y
tangent to ι(N₀⁺_η), and dv(L) = κ > 0. So the curves λ ↦ Θ(c, λ, y), λ ≥ 0, leave ι(N₀⁺) to the side into which J
points, where Ξ, extended near ι(N₀⁺) to a local diffeomorphism, takes values with d ≥ 1/2, that is, into 𝒱; and at c =
−10, Θ(−10, λ, y) = ι(−10, ν(λ, y), y) ∈ 𝒱 with v(Θ(−10, λ, y)) = ν(λ, y) for λ ≤ λ_*(y). Let U be the open set of (d)
of [[def:tl5-cip-development]], which contains ι(N⁺_η). By compactness there are λ₀ ∈ (0, min λ_*], κ₀ > 0 and δ ∈ (0,
v* − 1/2] with δ ≤ min(κ₀λ₀, u⁺ + 10) such that on 𝒦₂ := ([−10, u⁺] × [0, λ₀] × S³) ∪ {(c, λ, y) : −10 ≤ c ≤ −10 + δ,
0 ≤ λ ≤ λ_*(y)} ⊂ ℬ, Θ takes values in 𝒱 ∩ U and ∂_λ(v ∘ Θ) ≥ κ₀, and v(Θ(c, λ_*(y), y)) > v* for c ≤ −10 + δ, as
v(Θ(−10, λ_*(y), y)) = v* + η/4. As v(Θ(c, 0, y)) = 1/2, for every (u, v, y) ∈ 𝒩_δ there is exactly one λ with (u, λ,
y) ∈ 𝒦₂ and v(Θ(u, λ, y)) = v; put Φ(u, v, y) := Θ(u, λ, y). By the implicit function theorem Φ is smooth, and it has
the smooth inverse (u, v, y) on its image; so it is a diffeomorphism onto its image. At v = 1/2, λ = 0 and Φ = ι on
N₀⁺, and Φ(−10, v, y) = ι(−10, v, y); so Φ = ι on N⁺. Each point Φ(u, v, y) = Θ(u, λ, y) is joined to ι(u, 1/2, y) by
the future directed null geodesic Θ(u, ·, y) on [0, λ], which lies in U; so Φ(𝒩_δ) ⊂ U ∩ J⁺(ι(N⁺_η)) ⊂ M, J⁺ taken in
(U, g̃).

(4) *The double-null form and the data.* Let g′ := Φ*g̃, a time-oriented vacuum metric on 𝒩_δ, as Φ(𝒩_δ) ⊂ M. In the
coordinates (u, v, y), ∂_v is tangent to the generators of the C_u, so it is a multiple f∇u of the g′-gradient of u;
g′⁻¹(du, du) = 0 by (2) and g′⁻¹(dv, dv) = 0 by (1); ∂_v = ∂_λΘ/∂_λ(v ∘ Θ) is future directed; and ∇u is past directed,
being a nowhere vanishing null vector field on each of the two connected boxes of 𝒩_δ with g̃(∇u, V̲) = du(dι e₃) = 1 >
0 at their points on N₀⁺; so f < 0. [[lem:tl5-cip-dn-form]] (a), with u⁺ in place of u*, on the boxes D′₀ (u₁ = u⁺,
v₁ = 1/2 + δ) and D′₁ (u₁ = −10 + δ, v₁ = v*), shows that g′ is in double-null form on 𝒩_δ = D′₀ ∪ D′₁. As Φ = ι on N⁺,
dΦ = dι on vectors tangent to N₀⁺ and to N₁, and Φ is an isometry of (𝒩_δ, g′) onto its image, (a)–(c) of
[[def:tl5-cip-development]] hold on N⁺ ∩ D′ᵢ with (D′ᵢ, g′) in place of (M̃, g̃) and the inclusion in place of ι; so
[[lem:tl5-cip-dn-form]] (b) on each box gives g′ = g_N at every point of N⁺ ∩ D′ᵢ, i = 0, 1, that is, of N⁺.

(5) *Symmetry.* For σ ∈ G, σ*g′ is a vacuum metric in double-null form on 𝒩_δ, as σ acts on S³ alone and preserves 𝒩_δ,
∂_v, dv and the leaves, and σ*g′ = σ*g_N = g_N at the points of N⁺, the data and N⁺ being G-invariant.
[[prop:tl5-cip-unique]], applied on D′₀ (with u⁺ and 1/2 + δ in place of u* and s) and on D′₁ (with −10 + δ and v* in
place of u* and s), gives σ*g′ = g′ on both. ∎

**Lemma {#lem:tl5-wg-tension}** (The tension field and its transport.) Let g′ be a smooth metric in double-null form on
an open set 𝒰 ⊃ N⁺, with W, b, γ, χ and χ̲ as in [[lem:tl5-cip-frame]], and Ψ: 𝒰 → 𝒪̂ a smooth map with
Ψ = id on N⁺. Its tension field relative to g′ and ĝ is the vector field τ(Ψ) := tr_(g′) ∇dΨ along Ψ, where
(∇dΨ)(X, Y) := ∇̂_X(dΨ(Y)) − dΨ(∇′_X Y), ∇′ the connection of g′; in coordinates

    τ(Ψ)^μ = g′^(ab) (∂_a ∂_b Ψ^μ − Γ′^c_ab ∂_c Ψ^μ + Γ̂^μ_αβ(Ψ) ∂_a Ψ^α ∂_b Ψ^β).  {#eq:tl5-wg-tension}

(a) If Ψ is a diffeomorphism onto an open set and G := (Ψ⁻¹)*g′, then Υ(G) ∘ Ψ = −τ(Ψ).

(b) Let ξ := dΨ(∂_v) − ∂_v on N₀⁺ and ξ′ := dΨ(∂_u) − ∂_u on N₁, vectors at the same points, as Ψ = id there. Then
ξ = ξ′ = 0 on S, dΨ = id + ξ ⊗ dv on N₀⁺ and dΨ = id + ξ′ ⊗ du on N₁, and

    τ(Ψ) = −e^(−2W) (∇̂_(e₃) ξ + (1/2) trχ̲ ξ) − Υ(g′)   on N₀⁺,
    τ(Ψ) = −e^(−2W) (∇̂_(e₄) ξ′ + (1/2) trχ ξ′) − Υ(g′)   on N₁,  {#eq:tl5-wg-transport}

where ∇̂_(e₃) ξ is the ĝ-covariant derivative of ξ along the integral curves of e₃ in N₀⁺, likewise for ξ′.

*Proof.* (a) For a metric G and the identity map of (𝒰′, G) to (𝒰′, ĝ), [[eq:tl5-wg-tension]] gives
τ(id)^μ = G^(ab)(Γ̂^μ_ab − Γ(G)^μ_ab) = −Υ(G)^μ. Ψ is an isometry of (𝒰, g′) onto (Ψ(𝒰), G); in a chart x′ of Ψ(𝒰)
and the chart x′ ∘ Ψ of 𝒰 the components of g′ are those of G, and those of Ψ are those of the identity, so
[[eq:tl5-wg-tension]] for Ψ at p is that for the identity at Ψ(p); τ is a vector field along the map, independent of
the charts.

(b) At S, ∂_v is tangent to N₁ and ∂_u to N₀⁺, where Ψ = id, so ξ = ξ′ = 0 there; dΨ is the identity on the tangent
spaces of N₀⁺ and N₁, which gives the forms of dΨ. Let p ∈ N₀⁺. By [[lem:tl5-cip-form]] (a),
g′⁻¹ = −(e^(−2W)/2)(e₃ ⊗ e₄ + e₄ ⊗ e₃) + γ^(AB) ∂_A ⊗ ∂_B, e₄ = ∂_v, so τ(Ψ) = −e^(−2W)(∇dΨ)(e₃, e₄) +
γ^(AB)(∇dΨ)(∂_A, ∂_B), ∇dΨ being symmetric. For X tangent to N₀⁺, ∇̂_X(dΨ(Y)) is the ĝ-derivative along N₀⁺ of the
field dΨ(Y) = Y + dv(Y) ξ. By [[eq:tl5-cip-connection]], ∇′_(e₃) e₄ = 2e^(2W) a̲^A ∂_A is tangent to N₀⁺, and
∇′_A ∂_B = Γ̸^C_AB ∂_C + (e^(−2W)/2)(χ̲_AB e₄ + χ_AB e₃). So

    (∇dΨ)(e₃, e₄) = ∇̂_(e₃) ξ + (∇̂_(e₃) e₄ − ∇′_(e₃) e₄),
    (∇dΨ)(∂_A, ∂_B) = (∇̂_A ∂_B − ∇′_A ∂_B) − (e^(−2W)/2) χ̲_AB ξ.

The terms ∇̂_X Y − ∇′_X Y = −C(X, Y), with C = Γ(g′) − Γ̂, traced with g′⁻¹, give −Υ(g′); the rest gives the first
line of [[eq:tl5-wg-transport]]. On N₁ the same calculation with e₃ and e₄ exchanged, dΨ(e₃) = e₃ + ξ′ (b being tangent
to N₁), ∇′_(e₄) e₃ = 2e^(2W) a^A ∂_A tangent to N₁ and the e₃-component (e^(−2W)/2) χ_AB of ∇′_A ∂_B gives the second
line. ∎

**Lemma {#lem:tl5-wg-wavemap}** (A wave map to infinite order on N⁺.) Let g′ be a smooth G-invariant metric in
double-null form on a G-invariant open set 𝒰 ⊃ N⁺. There are a G-invariant open neighbourhood 𝒰₁ ⊂ 𝒰 of N⁺ and a smooth
map Ψ: 𝒰₁ → 𝒪̂ that commutes with G, equals the identity on N⁺, and is such that every partial derivative of the
components of τ(Ψ) vanishes at every point of N⁺.

*Proof.* (i) *Transport.* Let Ψ be smooth near a point of N₁ with Ψ = id on N₁, and use the same chart (u, v, y) in the
domain and in the target. Apply ∂_u^(k−1), k ≥ 1, to [[eq:tl5-wg-tension]] and restrict to N₁, where g′^(uu) = 0 and
g′^(ua) ∂_a = g′^(uv) ∂_v ([[lem:tl5-cip-form]] (a)). The derivative ∂_u^(k+1)Ψ occurs only with the coefficient
g′^(uu). The terms with ∂_u^kΨ are 2g′^(uv) ∂_v ∂_u^kΨ^μ, (k − 1) ∂_u g′^(uu) ∂_u^kΨ^μ, −g′^(ab) Γ′^u_ab ∂_u^kΨ^μ and
2g′^(au) Γ̂^μ_αβ(Ψ) ∂_aΨ^α ∂_u^kΨ^β over a ≠ u, the terms with a = b = u carrying the factor g′^(uu); all others
contain only the ∂_u^jΨ with j < k and their derivatives along N₁. So, with J_k := ∂_u^kΨ on N₁,

    ∂_u^(k−1) τ(Ψ) = 2g′^(uv) ∂_v J_k + M_k J_k + R_k   on N₁,

M_k and R_k depending only on the J_j with j < k, their derivatives along N₁, and g′, ĝ and their derivatives. The
equations ∂_u^(k−1) τ(Ψ) = 0 on N₁, k ≥ 1, are linear systems of ordinary differential equations for the J_k along the
generators of N₁, with continuous coefficients smooth in y and initial values at S equal to the derivatives of the
identity in u along N₀⁺; they have unique solutions on all of N₁, smooth in (v, y). The conditions do not depend on the
charts, τ(Ψ) being a vector field along Ψ, so the solutions in overlapping charts belong to the same jets. On N₀⁺ the
same holds with ∂_v, g′^(vv) = 0, g′^(va) ∂_a = g′^(uv) e₃ and the integral curves of e₃, which start on S and fill
N₀⁺, and with initial values at S the derivatives of the identity in v along N₁.

To sum these jets we use the inclusion S³ ⊂ ℂ² = ℝ⁴ and π(w) := w/|w| for w ∈ ℝ⁴ ∖ {0}: for a map Ψ into 𝒬 let Ψ̃ :=
(u ∘ Ψ, v ∘ Ψ, z ∘ Ψ), an ℝ⁶-valued function, z ∈ S³ ⊂ ℝ⁴ the S³-component, and for an ℝ⁶-valued Φ̃ with
positive |Φ̃_z| let π(Φ̃) := (Φ̃_u, Φ̃_v, π(Φ̃_z)), so that π(Ψ̃) = Ψ. By the chain rule, the u-jets of Ψ̃ on N₁ and
those of Ψ in charts determine each other; let 𝔍¹_k be the ℝ⁶-valued functions on N₁ corresponding to the solutions
J_k, and 𝔍⁰_k those on N₀⁺ (with ∂_v). Extend the 𝔍¹_k smoothly in v beyond [1/2, v*] by [[lem:tl5-cip-extend]]
(a) (applied to functions constant in u), and the 𝔍⁰_k in u beyond [−10, u⁺] likewise.

(ii) *Summation along N₁.* Let ι̃ := (u, v, z) and χ₀ ∈ C_c^∞(ℝ) with χ₀ = 1 on [−1, 1] and support in [−2, 2]. Choose
ε_k ∈ (0, 1] so small that c_k := χ₀((u + 10)/ε_k) (u + 10)^k (𝔍¹_k − ∂_u^k ι̃)(v, y)/k! has all its derivatives of
order less than k bounded by 2^(−k) on [−12, −8] × [−1/2, v* + 1] × S³, in a fixed finite atlas; each such derivative is
a sum of terms bounded by a constant times ε_k. Then Ψ̃₁ := ι̃ + Σ_(k≥1) c_k converges with all its derivatives,
Ψ̃₁ = ι̃ on N₁ and where |u + 10| ≥ 2, and ∂_u^k Ψ̃₁ = 𝔍¹_k on N₁ (near u = −10 the term c_m is a polynomial of degree
m in u + 10). Let Ψ₁ := π(Ψ̃₁) where |(Ψ̃₁)_z| ≥ 1/2, a neighbourhood of N⁺. In a chart near a point of N₁, the same
formula with the chart jets J_k gives a map Ψ_c with those jets; Ψ̃₁ − Ψ̃_c and hence Ψ₁ − Ψ_c = π(Ψ̃₁) − π(Ψ̃_c) vanish
with all derivatives on N₁. So the u-jets of Ψ₁ on N₁ are the J_k, and every partial derivative of τ(Ψ₁) vanishes at
the points of N₁: its derivatives ∂_u^(k−1) do, by (i), and so do their derivatives along N₁.

(iii) *The corner.* Let J¹_k := ∂_v^k Ψ₁ and J⁰_k the solutions of (i) on N₀⁺, in a chart near a point of S. We show by
induction on k that J¹_k − J⁰_k vanishes with all its derivatives along N₀⁺ at the points of S; for k = 0 both are the
identity. By (ii), E_k := ∂_v^(k−1) τ(Ψ₁) on N₀⁺ vanishes with all its derivatives along N₀⁺ at S. By (i),
E_k = 2g′^(uv) e₃(J¹_k) + M_k(J¹_<k) J¹_k + R_k(J¹_<k) and 0 = 2g′^(uv) e₃(J⁰_k) + M_k(J⁰_<k) J⁰_k + R_k(J⁰_<k), so
δ_k := J¹_k − J⁰_k satisfies 2g′^(uv) e₃(δ_k) + M_k(J⁰_<k) δ_k = E′_k, where E′_k is E_k minus the differences of
M_k J¹_k and of R_k between the arguments J¹_<k and J⁰_<k, which agree to infinite order at S; so E′_k vanishes with all
its derivatives along N₀⁺ at S. At S, J¹_k is the k-th derivative in v along N₁ of Ψ₁ = id, so δ_k = 0 on S. Solving the
equation for ∂_u δ_k = e₃(δ_k) − b^A ∂_A δ_k and differentiating it in u and in y shows that all derivatives of δ_k
along N₀⁺ vanish at S.

(iv) *Summation along N₀⁺.* Let D_k := 𝔍⁰_k − ∂_v^k Ψ̃₁ on N₀⁺, for k ≥ 1. By (iii) and the chain rule, D_k vanishes
with all its derivatives at u = −10; extended by 0 to u < −10 it is smooth ([[lem:tl5-cip-extend]] (b)). With
ε′_k chosen as in (ii), Ψ̃ := Ψ̃₁ + Σ_(k≥1) χ₀((v − 1/2)/ε′_k) (v − 1/2)^k D_k(u, y)/k! is smooth, ∂_v^k Ψ̃ = 𝔍⁰_k on
N₀⁺, and the correction vanishes on {u ≤ −10}, so the u-jets of Ψ̃ on N₁ are those of Ψ̃₁. Let 𝒰₁ be a G-invariant open
neighbourhood of N⁺ on which |Ψ̃_z| ≥ 1/2 and Ψ := π(Ψ̃) takes values in 𝒪̂. As in (ii), the jets of Ψ on N₀⁺ and on N₁
are the solutions of (i), so every partial derivative of τ(Ψ) vanishes at the points of N⁺, and Ψ = id on N⁺.

(v) *Symmetry.* For σ ∈ G, σ*g′ = g′ and σ*ĝ = ĝ, and σ preserves N₀⁺, N₁, S and the identity; so σ ∘ Ψ ∘ σ⁻¹ satisfies
the same transport equations with the same initial values, and by uniqueness the J_k are equivariant. G acts on
ℝ⁶ = ℝ² × ℂ² linearly, commuting with π, and the sums in (ii) and (iv) and the extensions act on u and v alone; so Ψ̃₁,
the D_k, Ψ̃ and Ψ commute with G. ∎

**Theorem {#thm:tl5-wg-data}** (Data in the wave gauge exist.) Let ĝ be a background with N⁺ ⊂ 𝒪̂, g_N smooth data in
the gauge on N⁺ satisfying the constraints, δ and g′ as in [[lem:tl5-wg-lchart]], and extend W, b and γ of g′ from the
boxes D′₀ and D′₁ of 𝒩_δ by [[lem:tl5-cip-extend]] (a), to E₀ and E₁ say, and glue them as ϖ E₁ + (1 − ϖ) E₀, with ϖ a
smooth function of (v − 1/2) − (u + 10) equal to 1 on [δ/3, ∞) and to 0 on (−∞, −δ/3]. At the points of 𝒩_δ where
min(u + 10, v − 1/2) < δ/3 the glued fields are W, b and γ, as there D′₀ ∖ D′₁ lies in {ϖ = 0} and D′₁ ∖ D′₀ in
{ϖ = 1}; so [[eq:tl5-cip-form]] defines a G-invariant metric in double-null form, again called g′, on a G-invariant
open neighbourhood 𝒰 of N⁺ in {min(u + 10, v − 1/2) < δ/3}, equal to g′ on 𝒩_δ ∩ 𝒰. Let Ψ be the map of
[[lem:tl5-wg-wavemap]], ξ and ξ′ as in [[lem:tl5-wg-tension]], and, with W, χ and χ̲ those of g′ at the points of N⁺
and the norms those of k̂,

    Y₀ := max_(N₀⁺) e^(2W) |Υ(g′)|,   K₀ := max_(N₀⁺) ((1/2) |∇̂_(e₃) k̂| + (1/2) |trχ̲|),
    Y₁ := max_(N₁) e^(2W) |Υ(g′)|,    K₁ := max_(N₁) ((1/2) |∇̂_(e₄) k̂| + (1/2) |trχ|),
    ξ₀ := Y₀ (u⁺ + 10) e^(K₀(u⁺ + 10)),   ξ₁ := Y₁ (v* − 1/2) e^(K₁(v* − 1/2)).

By [[lem:tl5-cip-jets]] (c), applied on D′₀ (with u⁺ and 1/2 + δ in place of u* and s) and on D′₁ (with −10 + δ and v*
in place of u* and s), the derivatives of all orders of g′ at the points of N⁺ do not depend on the choice of g′ in
[[lem:tl5-wg-lchart]]; so Y₀, K₀, Y₁ and K₁ depend only on g_N and ĝ. Then |ξ| ≤ ξ₀ on N₀⁺ and |ξ′| ≤ ξ₁ on N₁. Suppose

    (X)  ξ₀ < √2 min_(N₀⁺) Ω̂   and   ξ₁ < √2 min_(N₁) Ω̂.

Then there is a G-invariant open neighbourhood 𝒰^♯ ⊂ 𝒪̂ of N⁺ on which G^♯ := (Ψ⁻¹)*g′ is a smooth G-invariant Lorentzian
metric satisfying (W1), (W2) and (W3) of [[def:tl5-wg-data]]. At the points of N⁺,

    G^♯⁻¹ = g_N⁻¹ − (e^(−2W)/2)(ξ ⊗ e₃ + e₃ ⊗ ξ)  on N₀⁺,      G^♯⁻¹ = g_N⁻¹ − (e^(−2W)/2)(ξ′ ⊗ e₄ + e₄ ⊗ ξ′)  on N₁,

so G^♯ also satisfies (W4) if

    (T)  |g_N⁻¹ − ĝ⁻¹| + e^(−2W) |e₃| ξ₀ < κ_m  on N₀⁺   and   |g_N⁻¹ − ĝ⁻¹| + e^(−2W) |e₄| ξ₁ < κ_m  on N₁,

and is then data in the wave gauge for g_N. If g′ and ĝ have the same values and first derivatives at the points of
N₀⁺, then Y₀ = 0, ξ = 0 and G^♯ = g_N on N₀⁺.

*Proof.* *The bounds.* Along an integral curve of e₃ in N₀⁺, parametrised by u from S, (d/du) k̂(ξ, ξ) =
(∇̂_(e₃) k̂)(ξ, ξ) + 2k̂(∇̂_(e₃) ξ, ξ). As Ψ is the identity on N⁺ and every derivative of τ(Ψ) vanishes there,
τ(Ψ) = 0 on N⁺, so by [[eq:tl5-wg-transport]] ∇̂_(e₃) ξ = −(1/2) trχ̲ ξ − e^(2W) Υ(g′), and f := (|ξ|² + ϵ²)^(1/2),
ϵ > 0, satisfies f′ ≤ K₀ f + Y₀ with f(−10) = ϵ. So (e^(−K₀(u + 10)) f)′ ≤ Y₀ e^(−K₀(u + 10)) ≤ Y₀, and
f(u) ≤ (ϵ + Y₀(u + 10)) e^(K₀(u + 10)); let ϵ → 0. On N₁ the same with e₄, v and K₁, Y₁.

*The map.* By [[lem:tl5-wg-tension]] (b), dΨ = id + ξ ⊗ dv on N₀⁺, with determinant 1 + dv(ξ), and |dv(ξ)|
≤ |dv| |ξ| = |ξ|/(√2 Ω̂) < 1 by [[eq:tl5-wg-khat]] and (X); likewise on N₁ with du and ξ′. So dΨ is invertible at the
points of N⁺; Ψ is the identity, hence injective, on the compact set N⁺; so Ψ is a diffeomorphism of a G-invariant open
neighbourhood 𝒰₂ ⊂ 𝒰₁ of N⁺ onto an open set 𝒰^♯ := Ψ(𝒰₂) ⊂ 𝒪̂, which is G-invariant as Ψ commutes with G, and G^♯ is a
smooth G-invariant Lorentzian metric on 𝒰^♯.

*(W1)–(W3).* dΨ is the identity on vectors tangent to N⁺, so G^♯ and g′ agree on pairs of such vectors, and g′ = g_N at
the points of N⁺ ([[lem:tl5-wg-lchart]]); this is (W1). g′ is vacuum on 𝒩_δ ∩ 𝒰, of which every point of N⁺ is a limit
of interior points, so every partial derivative of Ric(g′) vanishes at the points of N⁺, and Ric(G^♯) = (Ψ⁻¹)*Ric(g′),
with Ψ = id on N⁺, vanishes with all its derivatives there. By [[lem:tl5-wg-tension]] (a), Υ(G^♯) = −τ(Ψ) ∘ Ψ⁻¹ vanishes
with all its derivatives at N⁺, and then so does Ric^W(G^♯), which differs from Ric(G^♯) by terms linear in Υ(G^♯) and
its first derivatives; this is (W2). Ψ is an isometry of g′ onto G^♯ that is the identity on N⁺, so it maps the field
∂_v along N₁ and the field e₃ along N₀⁺ to themselves, and ∇^♯_(∂_v) ∂_v = dΨ(∇′_(∂_v) ∂_v) = 2∂_vW ∂_v along N₁ and
∇^♯_(e₃) e₃ = 2e₃(W) e₃ along N₀⁺, by [[eq:tl5-cip-connection]] for g′, whose W is that of g_N; at S,
G^♯(∂_u, ∂_v) = g′(∂_u, ∂_v) = g_N(∂_u, ∂_v), and G^♯(∇^♯_X ∂_v, e₃) = g′(∇′_X ∂_v, e₃), which by
[[eq:tl5-cip-connection]] for g′ is the right side of (c) of [[def:tl5-cip-development]]; this is (W3).

*(W4).* At p ∈ N₀⁺, G^♯⁻¹(ω, ω′) = g′⁻¹(ω ∘ dΨ, ω′ ∘ dΨ) with ω ∘ dΨ = ω + ω(ξ) dv, and g′⁻¹(dv, dv) = 0 and
g′⁻¹(dv) = −(e^(−2W)/2) e₃ by [[lem:tl5-cip-form]] (a); this gives the formula on N₀⁺, and likewise on N₁ with
g′⁻¹(du) = −(e^(−2W)/2) e₄. As |ξ ⊗ e₃ + e₃ ⊗ ξ| ≤ 2|ξ| |e₃|, (T) gives |G^♯⁻¹ − ĝ⁻¹| < κ_m on N⁺.

If g′ and ĝ have the same 1-jet at the points of N₀⁺, then Υ(g′) = g′^(ab) C_ab = 0 there, so Y₀ = 0, ξ = 0 by the
bound, and G^♯⁻¹ = g_N⁻¹ on N₀⁺. ∎

**Corollary {#cor:tl5-wg-data-first-stage}** (The first stage.) Fix a seed, u* < u⁺ < u₀ with u₀ as in
[[lem:tl5-seed]] (a), and v* ∈ (1/2, 7/2], and let g_N be the data of the first stage of
[[cor:tl5-cip-staged]] (a), with u⁺ in place of u*: the seed on N₀⁺ and the data of [[def:tl5-problem]] on N₁.
They are smooth data in the gauge on N⁺ satisfying the constraints, so [[lem:tl5-wg-lchart]] applies to them. For every
background ĝ with N⁺ ⊂ 𝒪̂ for which (X) and (T) of [[thm:tl5-wg-data]] hold, G^♯ of that theorem is data in the wave
gauge for g_N, and [[thm:tl5-wg]] applies.

*Proof.* [[cor:tl5-cip-staged]] (a) with u⁺ ∈ (−10, u₀) in place of u* gives the first sentence, and
[[thm:tl5-wg-data]] the rest. ∎

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

### Double-null coordinates for a metric close to the background {#sec:tl5-dn}

Let g be a G-invariant metric close to ĝ on D^κ, for instance a solution of the reduced problem. The null hypersurfaces
of g through the leaves of N₀ and of N₁ define double-null coordinates, as in [[lem:tl5-cip-chart]]; here we
show that they have no caustics and cover an explicit region D′, the loss of D′ against D̄ being bounded by an
explicit multiple of the distance of g to ĝ. The construction reduces to three dimensions.

**Definition {#def:tl5-dn-slice}** (The slice.) Let M_σ ⊂ 𝒬 be the set of points (u, v, z) with z = (cos ϑ, sin ϑ) ∈ S³
⊂ ℂ² real, ϑ ∈ ℝ/2πℤ. On M_σ, (u, v, ϑ) are coordinates, x = cos 2ϑ, and the axes are ϑ ∈ (π/2)ℤ. For a metric g on
a G-invariant set X, g_σ denotes the metric that g induces on X ∩ M_σ.

**Lemma {#lem:tl5-dn-geodesic}** (The slice is totally geodesic.) Let g be a smooth G-invariant metric on an open
G-invariant set X ⊂ 𝒬. (a) X ∩ M_σ is the set of points of X fixed by the reflections ρ₁: (z₁, z₂) ↦ (z̄₁, z₂) and ρ₂:
(z₁, z₂) ↦ (z₁, z̄₂) of G. At p ∈ M_σ, every vector of T_p𝒬 is the sum of a vector tangent to M_σ and a vector on which
dρ₁ or dρ₂ is −1, and these summands are g-orthogonal. A g-geodesic whose initial point lies in M_σ and whose initial
velocity is tangent to M_σ stays in M_σ while it stays in X. (b) Every G-orbit in 𝒬 meets M_σ. (c) If g is in
double-null form, so is g_σ, in the coordinates (u, v, ϑ).

*Proof.* (a) ρ₁ and ρ₂ are the reflections φ₁ ↦ −φ₁ and φ₂ ↦ −φ₂, and their common fixed points are the points with z₁,
z₂ real. They are commuting involutions, so T_p𝒬 splits into the joint eigenspaces of dρ₁, dρ₂; the one for the
eigenvalues (1, 1) is T_pM_σ, the tangent space of the fixed point set. If dρ_i V = V and dρ_i W = −W, then g(V, W) =
g(dρ_i V, dρ_i W) = −g(V, W) = 0. If γ is the geodesic, ρ_i ∘ γ is a geodesic with the same initial point and velocity,
so ρ_i ∘ γ = γ. (b) A rotation of the angles of z₁ and z₂ maps any point of S³ to one with z₁, z₂ real and nonnegative.
(c) ∂_u, ∂_v and ∂_ϑ are tangent to M_σ at its points, so g(∂_v, ∂_v) = 0, g(∂_v, ∂_ϑ) = 0, g(∂_u, ∂_v) < 0 and the
positivity on the leaves restricts to g_σ. The covector dv vanishes on the vectors on which dρ₁ or dρ₂ is −1, which are
g-orthogonal to M_σ by (a); so g_σ⁻¹(dv, dv) = g⁻¹(dv, dv) = 0. ∎

#### One family of null hypersurfaces {#sec:tl5-dn-one}

We work in coordinates (t, r, z) on ℝ³, all functions being 2π-periodic in z. Let t₀ < t₁, r₀ < r₁, T := t₁ − t₀,
ρ ∈ (0, 1], B := [t₀, t₁] × [r₀, r₁] × ℝ and B_ρ := [t₀, t₁] × [r₀ − ρ, r₁ + ρ] × ℝ. For vectors |·| is the maximum
of the absolute values of the components, and ‖·‖ is the induced norm of linear and bilinear maps.

*The reference metric.* ĝ is a smooth Lorentzian metric on a neighbourhood of B_ρ, and β̂ a smooth function there, with
ĝ(ê, ê) = ĝ(ê, ∂_z) = 0 and ĝ(ê, ∂_r) < 0 for ê := ∂_t + β̂ ∂_z. So every surface {r = c} is null for ĝ with null
generator field ê, whose integral curves are therefore null pregeodesics (ĝ⁻¹(dr) is a multiple of ê, and the
integral curves of the gradient of a function whose gradient is everywhere null are pregeodesics, as in
[[lem:tl5-cip-causal]] (c)).

*The metric.* g is a smooth Lorentzian metric on an open neighbourhood of B, time-oriented, such that: (i) at every
point of {t = t₀} the form g on span(∂_r, ∂_z) is degenerate; (ii) the surface {r = r₀} is null for g, with null
generator field ê_g := ∂_t + β ∂_z for a smooth β, ê_g future directed; (iii) dr(V) ≥ 0 for every future directed
g-causal vector V at the points of {r = r₀}. Put

    ε := max over B of |∂^α (g − ĝ)_μν|,   μ, ν ∈ {t, r, z},   |α| ≤ 2.                                 {#eq:tl5-dn-eps}

*The vector fields.* For a 1-jet j¹ = (g_μν, ∂_λ g_μν) at a point (t, r, z), with (g_μν) invertible, and
Y = (r, z, p, q) ∈ ℝ⁴, let Ẋ := (1, p, q) and

    𝔉(t, Y; j¹) := (p, q, −Γ^r_αβ Ẋ^α Ẋ^β + p Γ^t_αβ Ẋ^α Ẋ^β, −Γ^z_αβ Ẋ^α Ẋ^β + q Γ^t_αβ Ẋ^α Ẋ^β),  {#eq:tl5-dn-field}

the Christoffel symbols being those that j¹ determines. Put F_g(t, Y) := 𝔉(t, Y; j¹g(t, r, z)) and F̂ := F_ĝ. A curve
t ↦ X(t) = (t, r(t), z(t)) satisfies Y′ = F_g(t, Y), Y := (r, z, r′, z′), if and only if ∇_(X′) X′ = κ X′ with
κ := Γ^t_αβ X′^α X′^β, the t-component of the geodesic equation holding trivially; that is, if and only if X is a
pregeodesic of g parametrised by t. Write 𝔊(t, Y; j²) := ∂_Y 𝔉 + ∂_(j¹) 𝔉 · ∂_(r,z) j¹ for the derivative in Y of
𝔉(t, Y; j¹g(t, r, z)), expressed through the 2-jet j² of the metric. For a 0-jet j⁰ = (g_μν) let

    𝔑(j⁰) := (p₀, q₀),   p₀ := −C/(2B̃),   q₀ := −(g_tz + p₀ g_rz)/g_zz,
    C := g_tt − g_tz²/g_zz,   B̃ := g_tr − g_rz g_tz/g_zz.  {#eq:tl5-dn-normal}

At a point of {t = t₀}, where g_rr − g_rz²/g_zz = 0 by (i), V := ∂_t + p₀∂_r + q₀∂_z is the unique vector with
dt(V) = 1, g(V, ∂_z) = 0 and g(V, V) = 0, provided g_zz > 0 and B̃ ≠ 0: the first condition gives q in terms of p, and
substituting gives g(V, V) = C + 2B̃p + (g_rr − g_rz²/g_zz)p². For ĝ, the same formula gives 𝔑(ĝ) = (0, β̂), as Ĉ = 0
and q̂₀ = −ĝ_tz/ĝ_zz = β̂, by the two conditions on ê.

*The reference generators.* For (c, z₀) ∈ [r₀ − ρ, r₁ + ρ] × ℝ let ẑ(t; c, z₀) solve ∂_t ẑ = β̂(t, c, ẑ),
ẑ(t₀) = z₀, and Ŷ(t; c, z₀) := (c, ẑ, 0, β̂(t, c, ẑ)). It solves Ŷ′ = F̂(t, Ŷ), as t ↦ (t, c, ẑ) is an integral curve of
ê. Let ψ̂_t(c, z₀) := (c, ẑ(t; c, z₀)) and Ẑ := ∂Ŷ/∂(c, z₀).

**Definition {#def:tl5-dn-constants}** (The constants of a family.) In this setting let 𝒯 be the set of (t, c, z₀, Y)
with t ∈ [t₀, t₁], c ∈ [r₀, r₁] and |Y − Ŷ(t; c, z₀)| ≤ ρ; it is compact modulo the periods. Let ε_* ∈ (0, 1] be such
that for every point of B_ρ and every k-jet within ε_* of that of ĝ (in the maximum of the components), k ≤ 2, the
matrix (g_μν) is Lorentzian, g_zz ≥ min ĝ_zz/2 and |B̃| ≥ min |ĝ(ê, ∂_r)|/2, the minima being over B_ρ; such an ε_*
exists by compactness. Let 𝒥_k denote the closed ε_*-neighbourhood of the k-jets of ĝ over the points involved. Put

    L := max_𝒯 ‖D_Y F̂(t, Y)‖,   L₂ := max_𝒯 ‖D_Y² F̂(t, Y)‖,
    Λ₀ := max ‖D𝔑(j⁰)‖,   Λ₀′ := max ‖D²𝔑(j⁰)‖   (j⁰ ∈ 𝒥₀ at points of {t₀} × [r₀, r₁] × ℝ),
    Λ₁ := max ‖∂_(j¹) 𝔉(t, Y; j¹)‖,   Λ₂ := max ‖∂_(j²) 𝔊(t, Y; j²)‖   ((t, ·, ·, Y) ∈ 𝒯, j¹ ∈ 𝒥₁, j² ∈ 𝒥₂),
    M₁ := max_({t₀} × [r₀, r₁] × ℝ) |∂_(r,z) ĝ_μν|,   Ĵ := max ‖Ẑ‖,   Ĵ⁻ := max ‖(Dψ̂_t)⁻¹‖,
    b_min := min ∂_(z₀) ẑ,   b_∞ := max |β̂|,

the last four over t ∈ [t₀, t₁], c ∈ [r₀ − ρ, r₁] and z₀ ∈ ℝ, and the jet norms being maxima over components. Here
Dψ̂_t = ((1, 0), (∂_c ẑ, ∂_(z₀) ẑ)) and ∂_(z₀) ẑ = exp ∫ ∂_z β̂ > 0. Finally let

    η₀ := (Λ₀ + Λ₁ T) ε e^(L T),
    η₁ := (2 (Λ₀′ M₁ + Λ₀) ε + T Ĵ (Λ₂ ε + L₂ η₀)) e^((L + Λ₂ ε) T),
    η₂ := η₀ + 2 (b_∞ + 1) η₁ / b_min.                                                                {#eq:tl5-dn-eta}

η₀, η₁ and η₂ are at most a constant times ε, the constants depending only on ĝ, β̂, ρ and the box. At Y = Ŷ the
entries of D_Y F̂ are built from the Christoffel symbols Γ̂^μ_αβ contracted with ê and their first derivatives; for
β̂ = 0 these are the Γ̂^μ_tα, the entry for the pair (z, q) is Γ̂^t_tt − 2Γ̂^z_tz, and 2Γ̂^z_tz = ∂_t ln ĝ_zz is twice
the null expansion of the circles {t, r constant} along ê; so the exponential rate L is a bound for the null expansions
and the related connection coefficients of ĝ along the reference generators, enlarged to the tube 𝒯.

**Lemma {#lem:tl5-dn-gronwall}** (Comparison of solutions.) Let F, F̂ be continuous on [a, b] × ℝ^m, F̂ of class C¹ in
Y, Ŷ a solution of Ŷ′ = F̂(t, Ŷ) on [a, b], and L > 0 with L ≥ ‖D_Y F̂‖ on 𝒯_ρ := {(t, Y) : |Y − Ŷ(t)| ≤ ρ}. Let Y be a
C¹ solution of Y′ = F(t, Y) on [a, b′), b′ ≤ b, with |F(t, Y(t)) − F̂(t, Y(t))| ≤ θ whenever (t, Y(t)) ∈ 𝒯_ρ,
and |Y(a) − Ŷ(a)| ≤ θ₀. If (θ₀ + θ(b − a)) e^(L(b − a)) < ρ, then (t, Y(t)) ∈ 𝒯_ρ and |Y(t) − Ŷ(t)| ≤ (θ₀ + θ(t − a))
e^(L(t − a)) for all t ∈ [a, b′).

*Proof.* Let t₂ be the supremum of the t′ ∈ [a, b′) with (t, Y(t)) ∈ 𝒯_ρ for t ∈ [a, t′]. On [a, t₂), φ := |Y − Ŷ|
satisfies φ(t) ≤ θ₀ + ∫_a^t (|F(Y) − F̂(Y)| + |F̂(Y) − F̂(Ŷ)|) ≤ α(t) + L ∫_a^t φ, α(t) := θ₀ + θ(t − a), by the
mean value inequality on the segment from Ŷ(s) to Y(s), which lies in the convex fibre of 𝒯_ρ. With
ψ(t) := ∫_a^t φ, (e^(−L(t−a)) ψ)′ ≤ α e^(−L(t−a)), so ψ(t) ≤ α(t)(e^(L(t−a)) − 1)/L and φ ≤ α + Lψ ≤
α e^(L(t − a)) < ρ. If t₂ < b′, continuity would give (t, Y(t)) ∈ 𝒯_ρ beyond t₂; so t₂ = b′. ∎

**Lemma {#lem:tl5-dn-family}** (One family.) In the setting above suppose ε ≤ ε_*, η₀ < ρ, η₀ < r₁ − r₀,
Ĵ⁻ η₁ ≤ 1/2 and η₁ (1 + 2(Ĵ + 1)/b_min) ≤ 1/2, and put P := [t₀, t₁] × [r₀, r₁ − η₀] × ℝ.

(a) For (c, z₀) ∈ [r₀, r₁ − η₀] × ℝ the solution Y(t; c, z₀) of Y′ = F_g(t, Y) with Y(t₀) = (c, z₀, 𝔑(j⁰g(t₀, c, z₀)))
exists on [t₀, t₁], the curve X(t; c, z₀) := (t, r, z) lies in B, r ≥ r₀, and |Y − Ŷ| ≤ η₀. X is a future directed null
pregeodesic of g, normal to the circle {t = t₀, r = c} at its initial point and transverse to {t = t₀}; for c = r₀ it
is the integral curve of ê_g through (t₀, r₀, z₀).

(b) Z := ∂Y/∂(c, z₀) satisfies |Z − Ẑ| ≤ η₁ on P.

(c) Φ(t, c, z₀) := X(t; c, z₀) is a diffeomorphism of P onto a subset Φ(P) of B that contains
[t₀, t₁] × [r₀, r₁ − 2η₀] × ℝ, and Φ(t, c, z₀ + 2π) = Φ(t, c, z₀) + (0, 0, 2π).

(d) On Φ(P), r̃ := c ∘ Φ⁻¹ and z̃ := z₀ ∘ Φ⁻¹ are smooth, g⁻¹(dr̃, dr̃) = 0, |r̃ − r| ≤ η₀; on {t = t₀}, r̃ = r and
z̃ = z; on {r = r₀}, r̃ = r₀ and z̃ is constant along the integral curves of ê_g; and
dr̃ = λ (dr + a_t dt + a_z dz) with λ > 0 and |a_t|, |a_z| ≤ η₂.

*Proof.* F_g is defined near B. At points of B, the jets of g lie within ε
of those of ĝ, so |F_g − F̂| ≤ Λ₁ ε along a solution in B and in 𝒯, by the mean value inequality in the jet variable,
and |Y(t₀) − Ŷ(t₀)| = |𝔑(j⁰g) − 𝔑(j⁰ĝ)| ≤ Λ₀ ε.

(a) Fix (c, z₀). The vector V of [[eq:tl5-dn-normal]] at (t₀, c, z₀) is the null normal of the circle with dt(V) = 1;
for c = r₀ it is ê_g, which by (ii) is null, orthogonal to ∂_z and has dt(ê_g) = 1. It depends continuously on (c, z₀)
and never vanishes, so it is future directed for all (c, z₀), as it is for c = r₀. Let [t₀, t₂) be the largest interval
on which the solution exists, lies in B and satisfies (t, c, z₀, Y(t)) ∈ 𝒯. On it, |Y − Ŷ| ≤ (Λ₀ + Λ₁(t − t₀)) ε
e^(L(t − t₀)) ≤ η₀ by [[lem:tl5-dn-gronwall]], so r ≤ c + η₀ ≤ r₁. The curve X is a pregeodesic with null initial
velocity, so g(X′, X′) = 0 throughout, since (d/dt) g(X′, X′) = 2κ g(X′, X′); and X′ stays future directed. If c = r₀, X
is the integral curve of ê_g, which is a null pregeodesic (a generator of {r = r₀}) parametrised by t and so solves the
same equation with the same initial data. If c > r₀ and r(t₃) = r₀ for a first t₃ < t₂, then dr(X′(t₃)) ≤ 0, and
dr(X′(t₃)) ≥ 0 by (iii); so X′(t₃) is a causal vector tangent to the null surface {r = r₀}, hence a multiple of ê_g, and
equal to ê_g as dt(X′) = 1. By uniqueness, X is then the integral curve of ê_g through X(t₃), on which r = r₀
throughout, against r(t₀) = c. So r > r₀ on [t₀, t₂). If ε = 0, then g = ĝ on B and X is the reference generator.
Otherwise the bound of [[lem:tl5-dn-gronwall]] is either identically 0, and then Y = Ŷ, a curve in B, or strictly
increasing in t, since L ≥ 1 (the first two components of F̂ are p and q); in the latter case, for t₂ < t₁ the solution
extends to t₂ with |Y − Ŷ| < η₀ < ρ and r₀ < r < c + η₀ ≤ r₁ at t₂ (r > r₀ at t₂ by the same argument), and then beyond
t₂ within B and 𝒯, against the choice of t₂. So t₂ = t₁, and the solution extends to [t₀, t₁] by continuity.

(b) Z solves Z′ = 𝔊(t, Y; j²g) Z, and Ẑ solves Ẑ′ = 𝔊(t, Ŷ; j²ĝ) Ẑ. So
(Z − Ẑ)′ = 𝔊(t, Y; j²g)(Z − Ẑ) + (𝔊(t, Y; j²g) − 𝔊(t, Y; j²ĝ) + D_Y F̂(t, Y) − D_Y F̂(t, Ŷ)) Ẑ, with
‖𝔊(t, Y; j²g)‖ ≤ L + Λ₂ ε and the bracket bounded by Λ₂ ε + L₂ η₀. At t₀ the first two rows of Z − Ẑ vanish, and the
last two are ∂_(c,z₀)(𝔑(j⁰g) − 𝔑(j⁰ĝ)) = (D𝔑(j⁰g) − D𝔑(j⁰ĝ)) ∂j⁰ĝ + D𝔑(j⁰g) ∂(j⁰g − j⁰ĝ), of norm at most
Λ₀′ ε · 2M₁ + Λ₀ · 2ε, the derivatives ∂ being in (r, z) along {t = t₀}. Grönwall's inequality for the linear
equation gives (b).

(c) Fix t, put ψ_t(c, z₀) := (r, z)(t; c, z₀) and Δ := ψ_t − ψ̂_t on A₀ := [r₀, r₁ − η₀] × ℝ. By (a) and (b), |Δ| ≤ η₀
and ‖DΔ‖ ≤ η₁, so Δ is η₁-Lipschitz on the convex set A₀; and Δ_r(r₀, z₀) = 0 by (a). The inverse of the diffeomorphism
ψ̂_t of [r₀ − ρ, r₁ + ρ] × ℝ is Ĵ⁻-Lipschitz on convex subsets of [r₀ − ρ, r₁] × ℝ.
If ψ_t(a) = ψ_t(a′), then |a − a′| ≤ Ĵ⁻ |ψ̂_t(a) −
ψ̂_t(a′)| = Ĵ⁻ |Δ(a) − Δ(a′)| ≤ |a − a′|/2, so a = a′. Periodicity, which holds as g and ĝ are periodic, makes ψ_t
injective modulo 2π in z as well. For surjectivity let w = (w_r, w_z) with r₀ ≤ w_r ≤ r₁ − 2η₀. Put Δ̃(a) := Δ(max(a_r,
r₀), a_z) on A := [r₀ − ρ, r₁ − η₀] × ℝ; it is η₁-Lipschitz, |Δ̃| ≤ η₀, and Δ̃_r(a) = 0 for a_r ≤ r₀. The map T_w(a) :=
ψ̂_t⁻¹(w − Δ̃(a)) is defined on A, since ψ̂_t⁻¹ preserves the first component and w_r − Δ̃_r(a) ∈ [r₀ − η₀, r₁ − η₀],
maps A into A, and is a contraction with constant Ĵ⁻ η₁ ≤ 1/2; let a* be its fixed point. Then ψ̂_t(a*) + Δ̃(a*) = w.
If a*_r < r₀, the first component reads a*_r = w_r ≥ r₀, a contradiction; so a* ∈ A₀ and ψ_t(a*) = w. Hence Φ is a
bijection of P onto Φ(P), which contains the stated set. Its differential is triangular, with blocks 1 and
Dψ_t = Dψ̂_t + DΔ, which is invertible as ‖(Dψ̂_t)⁻¹‖ ‖DΔ‖ ≤ 1/2; so Φ is a diffeomorphism onto its image.

(d) The level set {r̃ = c} = Φ({c} × ·) has the tangent vectors X′ = ∂_tΦ and J := ∂_(z₀)Φ, and [X′, J] = 0. As g(X′,
X′) = 0 for all (t, c, z₀), ∂_t g(J, X′) = g(∇_J X′, X′) + κ g(J, X′) = J(g(X′, X′))/2 + κ g(J, X′) = κ g(J, X′), and
g(J, X′) = g(∂_z, V) = 0 at t₀; so g(J, X′) = 0, the level set is null, and g⁻¹(dr̃, dr̃) = 0. The statements on {t =
t₀} and {r = r₀} follow from Φ(t₀, c, z₀) = (t₀, c, z₀) and (a), and |r̃ − r| ≤ η₀ from (a). With X′ = (1, p, q) and
J = (0, a, b), a covector vanishing on both is a multiple of (pb − qa, −b, a), that is of dr + a_t dt + a_z dz with a_t
:= −p + qa/b and a_z := −a/b. By (a) and (b), |p| ≤ η₀, |q| ≤ b_∞ + η₀, |a| ≤ η₁ and b ≥ b_min − η₁ ≥ b_min/2, so |a_z|
≤ 2η₁/b_min ≤ η₂ and |a_t| ≤ η₀ + 2(b_∞ + 1)η₁/b_min = η₂. Write dr̃ = λ(dr + a_t dt + a_z dz). Since r̃(Φ(t, c, z₀)) =
c, 1 = dr̃(∂_cΦ) = λ(∂_c r + a_z ∂_c z), with ∂_c r ≥ 1 − η₁ and |∂_c z| ≤ Ĵ + η₁, so the bracket is at least 1 − η₁ −
2η₁(Ĵ + 1)/b_min ≥ 1/2, and λ > 0. ∎

#### Double-null coordinates on an explicit region {#sec:tl5-dn-chart}

**Theorem {#thm:tl5-dn}** (Double-null coordinates for a metric close to the background.) Let ĝ be a background, κ, κ′
as in [[def:tl5-wg-domains]], u_m := u* − κ′(v* − 1/2), v_m := v* − κ(u* + 10), so that
B := [−10, u_m] × [1/2, v_m] × S³ ⊂ D^κ ([[lem:tl5-wg-domains]] (d)), and g_N data in the gauge on N satisfying the
constraints. Let g be a smooth G-invariant vacuum metric on B, tilted on B, such that (a)–(c) of
[[def:tl5-cip-development]] hold for g on N ∩ B with ι the inclusion. Let ε be the quantity
[[eq:tl5-dn-eps]] for g_σ and ĝ_σ on B ∩ M_σ in the coordinates (u, v, ϑ), the C²-distance (in the maximum of the
components) of the two metrics on the slice, and let the constants of [[def:tl5-dn-constants]] be formed, with one
ρ ∈ (0, 1] for which 𝒪̂ contains [−10 − ρ, u_m + ρ] × [1/2 − ρ, v_m + ρ] × S³, for

- the outgoing family: (t, r, z) := (v, u, ϑ), t₀ := 1/2, t₁ := v_m, r₀ := −10, r₁ := u_m, β̂ := 0, β := 0;
- the ingoing family: (t, r, z) := (u, v, ϑ), t₀ := −10, t₁ := u_m, r₀ := 1/2, r₁ := v_m, β̂ := dϑ(b̂), β := dϑ(b),

where b̂ and b, the shifts of ĝ and of g_N, are tangent to M_σ at its points. Denote by η₀^out, η₀^in, η₂^in the
quantities [[eq:tl5-dn-eta]] of the two families, suppose that the hypotheses of [[lem:tl5-dn-family]] hold for both
and that η₂^in η₀^out < 1/2, and put

    η := max(κ′(v* − 1/2) + η₀^out, κ(u* + 10) + 3η₀^in),   D′ := [−10, u* − η] × [1/2, v* − η] × S³  {#eq:tl5-dn-region}

If η < min(u* + 10, v* − 1/2), then there are a closed set D″ ⊂ B containing N ∩ D′, and smooth functions ũ, ṽ and a
smooth map ỹ: D″ → S³, such that:

(a) ũ is constant on the outgoing null hypersurfaces of g through the leaves of N₀ and equal to u on N₀ ∩ D″; ṽ is
constant on the ingoing null hypersurfaces of g through the leaves of N₁ and equal to v on N₁ ∩ D″; ỹ is constant
along the outgoing null generators and equal to the S³-component on N₀ ∩ D″; these hypersurfaces have no caustics
and do not cross on D″; and in the coordinates of S³, φ_i ∘ ỹ = φ_i;

(b) Ψ := (ũ, ṽ, ỹ) is a G-equivariant diffeomorphism of D″ onto D′, equal to the identity on N ∩ D″; on D″ ∩ M_σ, |ũ −
u| ≤ η₀^out and |ṽ − v| ≤ η₀^in;

(c) the metric g̃ := (Ψ⁻¹)*g on D′ is a smooth G-invariant vacuum metric in double-null form, so of the class in the
gauge of [[sec:cone-constraint]], with R, P, Q, W and β smooth functions of (u, v, x) up to the axes; and g̃ = g_N at
every point of N ∩ D′. In particular, for the data of [[def:tl5-problem]] at a stage with smooth data
([[cor:tl5-cip-staged]] (a)), g̃ is a solution on D′ in the sense of [[thm:tl5-cip]], with u* − η and
v* − η in place of u* and s.

*Proof.* *The slice.* Extend g from B by [[lem:tl5-cip-extend]] (a) to a smooth metric on a neighbourhood of
B, Lorentzian near B and G-invariant, as the operator acts on u and v alone; the quantities below depend only on its
values on B. By [[lem:tl5-dn-geodesic]] (c), ĝ_σ satisfies the hypotheses on the reference metric for both
families: ∂_v and ê₃ restricted to M_σ are null, orthogonal to ∂_ϑ, and ĝ(∂_v, ∂_u) = ĝ(ê₃, ∂_v) = −2Ω̂² < 0. The
metric g_σ satisfies (i)–(iii) for both families, by (a) of [[def:tl5-cip-development]], which makes the
restrictions of g and g_N to TN₀ and TN₁ equal, with kernels e₃ and ∂_v, and by [[lem:tl5-wg-domains]] (c).

*Five dimensions.* Let 𝔜^out(v; c, y₀), for (c, y₀) ∈ [−10, u_m − η₀^out] × S³, be the null pregeodesic of g (extended
as above), parametrised by v, with initial point (c, 1/2, y₀), normal to the leaf {u = c, v = 1/2} and transverse to
N₀; and 𝔜^in(u; d, y₀), for (d, y₀) ∈ [1/2, v_m − η₀^in] × S³, the one parametrised by u from (−10, d, y₀), normal to
the leaf {u = −10, v = d} and transverse to N₁. The null normals depend smoothly on the initial point, so Φ^out(v, c,
y₀) := 𝔜^out(v; c, y₀) and Φ^in(u, d, y₀) := 𝔜^in(u; d, y₀) are smooth where they are defined. Since g, the leaves and
the transversal directions are G-invariant, Φ^out(v, c, σy₀) = σ Φ^out(v, c, y₀) for σ ∈ G, likewise for Φ^in. If y₀
lies in M_σ, the null normal is tangent to M_σ by [[lem:tl5-dn-geodesic]] (a), being fixed by dρ₁ and dρ₂, and the
pregeodesic stays in M_σ; it is a null pregeodesic of g_σ normal to the circle {u = c, v = 1/2} of the slice, and so it
is the curve X of [[lem:tl5-dn-family]] (a) for the outgoing family, with z₀ = ϑ₀, and likewise for the ingoing family.
So, by (a) of that lemma and by equivariance, Φ^out and Φ^in exist on [1/2, v_m] × [−10, u_m − η₀^out] × S³ and [−10,
u_m] × [1/2, v_m − η₀^in] × S³, and their restrictions to the slice are the maps Φ of the two families. The reflection
ϑ ↦ −ϑ is the rotation by π of z₂ restricted to M_σ, and ϑ ↦ π − ϑ the rotation by π of z₁; both are isometries of g_σ
and ĝ_σ fixing the axes, so the generators from the axes stay on them, and the maps ψ_t of [[lem:tl5-dn-family]] (c),
which are injective, map each interval (kπ/2, (k + 1)π/2) of ϑ₀ onto a subset of itself. Likewise every reflection φ_i
↦ 2φ_i⁰ − φ_i fixing a point fixes the generator from it, so φ₁ and φ₂ are constant along the generators.

*Injectivity and immersion.* Let Φ^out(v, c, y₀) = Φ^out(v′, c′, y₀′). Then v = v′, and by (b) of [[lem:tl5-dn-geodesic]]
and equivariance we may take y₀ ∈ M_σ; as the orbit of y₀′ meets M_σ, the injectivity of the slice map modulo the
reflections gives c = c′ and y₀′ = σ y₀ for some σ ∈ G, so that σ fixes p := Φ^out(v, c, y₀). The isotropy group of
y₀ is contained in that of p, and both are isomorphic to ℤ₂ × ℤ₂ if 0 < ϑ₀ < π/2 modulo π/2, and to O(2) × ℤ₂ on the
axes, as the slice map preserves these classes; a closed subgroup of a compact Lie group isomorphic to it with the
same number of components and the same dimension is the whole group, so σ fixes y₀ and y₀′ = y₀. At a point with y₀
in M_σ off the axes, T𝒬 is the sum of TM_σ and the tangent space of the T²-orbit; dΦ^out maps the generators of the
T²-action to the generators at the image (equivariance), which span the orbit's tangent space there, and maps TM_σ
isomorphically onto TM_σ by [[lem:tl5-dn-family]] (c); so it is invertible. At a point on an axis, say z₂ = 0, the
rotations of z₂ fix the point and its image; dΦ^out commutes with them, so it maps the subspace they fix
(spanned by ∂_v, ∂_c and the orbit direction ∂_(φ₁)) to the one at the image and the plane of z₂ to the plane of z₂.
On the first it is invertible by the slice and by equivariance; on the plane of z₂ it commutes with all rotations and
with the reflection z₂ ↦ z̄₂, so it is multiplication by a real number, which is the derivative ∂_(ϑ₀)ϑ of the slice
map, at least 1 − η₁ > 0 by (b) (for Φ^in at least b_min − η₁ ≥ b_min/2). So Φ^out is an injective immersion, hence
a diffeomorphism onto its image; likewise Φ^in.

*The chart.* Let ũ := c ∘ (Φ^out)⁻¹, ỹ := y₀ ∘ (Φ^out)⁻¹ and ṽ := d ∘ (Φ^in)⁻¹; they are smooth, ũ and ṽ are
G-invariant, ỹ is G-equivariant, and their level sets are null (on the slice by [[lem:tl5-dn-family]] (d), and
everywhere by invariance). For (c, y₀) with c ∈ [−10, u_m − η₀^out], the outgoing generator lies in
{c − η₀^out ≤ u ≤ c + η₀^out} ∩ {u ≥ −10} ⊂ [−10, u_m] and, for v ≤ v_m − 2η₀^in, in the image of Φ^in, which by
[[lem:tl5-dn-family]] (c) contains [−10, u_m] × [1/2, v_m − 2η₀^in] × S³. Put V(v; c, y₀) := ṽ(Φ^out(v, c, y₀)). Then
V(1/2) = 1/2, as N₀ is the ingoing null hypersurface through the leaf {u = −10, v = 1/2}; V(v) ≥ v − η₀^in; and
∂_v V = dṽ(ℓ) with ℓ := ∂_vΦ^out. At a point of the slice, by [[lem:tl5-dn-family]] (a) and (d),
ℓ = ∂_v + p ∂_u + q ∂_ϑ with |p|, |q| ≤ η₀^out, and dṽ = λ(dv + a_u du + a_ϑ dϑ) with λ > 0 and |a_u|, |a_ϑ| ≤ η₂^in;
so ∂_v V ≥ λ(1 − 2η₂^in η₀^out) > 0, and by invariance everywhere. So, for each (c, y₀), V(·; c, y₀) is increasing and
maps [1/2, v_m − 2η₀^in] onto an interval containing [1/2, v_m − 3η₀^in]. Hence

    Ψ ∘ Φ^out (v, c, y₀) = (c, V(v; c, y₀), y₀)

is a diffeomorphism of {(v, c, y₀) : −10 ≤ c ≤ u* − η, 1/2 ≤ v, V(v; c, y₀) ≤ v* − η} onto D′, since
u* − η ≤ u_m − η₀^out and v* − η ≤ v_m − 3η₀^in by [[eq:tl5-dn-region]]; let D″ be the image of that set under Φ^out.
Then Ψ is a diffeomorphism of D″ onto D′. On N₀, ũ = u and ỹ = y as Φ^out(1/2, c, y₀) = (c, 1/2, y₀), and ṽ = 1/2;
on N₁, ṽ = v, ũ = −10 as N₁ is the outgoing null hypersurface through the leaf {u = −10, v = 1/2}, and ỹ = y as the
generators of N₁ are the curves {u = −10, y constant} (their tangent ∂_v spans the kernel of g on TN₁). So Ψ is the
identity on N ∩ D″, and (a) and (b) hold, the bounds on the slice being [[lem:tl5-dn-family]] (d).

*The metric.* As η < min(u* + 10, v* − 1/2), D′ is the box of [[lem:tl5-cip-dn-form]] with u₁ := u* − η and
v₁ := v* − η, and in the coordinates (ũ, ṽ, ỹ) on D′ the hypotheses of its part (a) hold for g̃: dũ and dṽ are null;
∂_ṽ is tangent to the outgoing generators, on which ũ and ỹ are constant and which are the integral curves of the
gradient ∇ũ of ũ, so ∂_ṽ = f∇ũ for a function f; ∂_ṽ = ℓ/∂_vV is future directed; and ∇ũ is past directed, being a
nowhere vanishing null vector field on the connected set D′ with dũ a positive multiple of du on N₁
([[lem:tl5-dn-family]] (d) for the outgoing family), where g(∇u, V) = du(V) ≥ 0 for every future directed causal V
([[lem:tl5-wg-domains]] (c)); so f < 0, and g̃ is in double-null form. Since Ψ is an isometry of g onto g̃ that is the
identity on N ∩ D″, with differential the identity on vectors tangent to N, (a)–(c) of
[[def:tl5-cip-development]] hold on N ∩ D′ with D′ and g̃ in place of the development and the inclusion in
place of ι, as they do for g. So part (b) of [[lem:tl5-cip-dn-form]], g̃ being vacuum as g is, gives g̃ = g_N
at every point of N ∩ D′. It is G-invariant by equivariance, hence of the class in the gauge with fields smooth up to
the axes ([[lem:tl5-cip-form]] (b), [[lem:tl5-cip-axis]] (a)). ∎

**Remark {#rem:tl5-dn-use}** (The size of the loss.) η is the tilt of [[def:tl5-wg-domains]] plus a multiple of ε:
by [[eq:tl5-dn-eta]], η₀^out and η₀^in are (Λ₀ + Λ₁T) ε e^(LT) for the two families, the exponential rates L being
bounds for the connection coefficients of ĝ along its own null generators (the null expansions among them,
[[def:tl5-dn-constants]]). In an application to a solution g of the reduced problem, ε is bounded through the a
priori estimate: a bound for h = g − ĝ in C² on D^κ, expressed in the coordinates (u, v, ϑ) of the slice, bounds
ε. The theorem uses neither uniqueness in the double-null gauge nor the existence theory of the characteristic problem
in that gauge: it is applied to a metric already known to exist.

### Continuation beyond the seed {#sec:tl5-beyond}

The following lemma reduces existence beyond the seed to an a priori estimate on the whole region and a closing
condition; the local existence, uniqueness and continuation of the reduced problem in the wave gauge that it uses are
[[thm:tl5-wg]]. [[thm:tl5-hf]] proves the estimate, with explicit constants, for solutions close to a background.

**Lemma {#lem:tl5-continuation}** (Existence by continuity.) Let ĝ be a background ([[def:tl5-wg-background]]), κ and κ′
as in [[def:tl5-wg-domains]], g_N smooth characteristic data in the gauge on N⁺ satisfying the characteristic constraints
[[eq:tl5-cip-constraints]], and G^♯ data in the wave gauge for g_N ([[def:tl5-wg-data]]). For s ∈ (1/2, v*] call a
solution on D^κ_s a solution of the reduced problem on the tilted domain D^κ_s of [[eq:tl5-wg-tilted]]
([[def:tl5-wg-solution]]). Suppose that to every solution g on a D^κ_s and every σ ∈ [1/2, s] a number y_σ(g) ≥ 0 is
assigned, depending only on the restriction of g to D^κ_σ and continuous in σ, and that there are A, B > 0 such that
every solution g on every D^κ_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s] satisfies:

(H1) y_s(g) ≤ A + B y_s(g)²;

(H2) for every k ≥ 0 there is C_k, independent of g and s, such that the components of g and their derivatives of order
at most k, and the components of g⁻¹, are bounded by C_k on D^κ_s, in a fixed finite atlas of [−10, u*] × [1/2, v*] × S³;

(H4) |g⁻¹ − ĝ⁻¹|_k̂ < κ_m at every point of D^κ_s;

and that

(H3) 4AB < 1, and y_(1/2)(g) ≤ A for every solution g.

Then there is a solution g on D^κ = D^κ_(v*), and y_σ(g) ≤ 2A for every σ ∈ [1/2, v*].

The proof uses three properties of the reduced problem, for the data of the lemma, which [[thm:tl5-wg]] provides: (F1_W)
there are s₁ ∈ (1/2, v*] and a solution on D^κ_(s₁); (F2_W) two solutions, on D^κ_s and on D^κ_(s′), coincide on
D^κ_(min(s, s′)); (F3_W) a solution on D^κ_s with s < v* and |g⁻¹ − ĝ⁻¹|_k̂ < κ_m on D^κ_s is the restriction of a
solution on D^κ_(s′) for some s′ ∈ (s, v*]. Of the regions D^κ_s it uses only the properties listed in
[[rem:tl5-wg-continuation]]; (H4) is the strict tilt that
(F3_W) requires, and (H1), (H2) and (H4) are used only for solutions with y_σ ≤ 2A for all σ. By [[thm:tl5-wg]] (F4_W)
the solution is a G-invariant vacuum metric in the wave gauge, and [[thm:tl5-dn]] puts it into the gauge of
[[sec:cone-constraint]] on a region D′ whose loss against D̄ is the tilt plus an explicit multiple of the
C²-distance of g to ĝ on the slice. For the problem of [[def:tl5-problem]] with u* < u₀ the data of the first stage
of [[cor:tl5-cip-staged]] (a), with v* ≤ 7/2, are such data g_N, and [[cor:tl5-wg-data-first-stage]] gives data in the
wave gauge for them under two explicit conditions on the background along N⁺.

*Proof.* First, if 4AB < 1 and y ≥ 0 satisfies y ≤ A + By², then y ∉ (2A, 1/(2B)), and if moreover y ≤ 2A then y ≤ A +
4A²B < 2A. Indeed q(y) := By² − y + A is convex with q(2A) = A(4AB − 1) < 0 and q(1/(2B)) = (4AB − 1)/(4B) < 0, so q < 0
on [2A, 1/(2B)], an interval since 2A < 1/(2B); and 4A²B < A.

Let I be the set of s ∈ (1/2, v*] for which there is a solution g on D^κ_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s]. If s ∈
I and 1/2 < s′ < s, then s′ ∈ I, by restriction.

I is not empty. By (F1_W) of [[thm:tl5-wg]] there is a solution g on some D^κ_(s₁); y_(1/2)(g) ≤ A < 2A by (H3), and
y_σ(g) is continuous in σ, so y_σ(g) ≤ 2A on [1/2, s₂] for some s₂ ∈ (1/2, s₁], and s₂ ∈ I.

I is open in (1/2, v*]. Let s ∈ I with s < v*, and g the solution on D^κ_s. For σ ∈ (1/2, s] the restriction of g to
D^κ_σ is a solution on D^κ_σ with y_σ′ ≤ 2A for σ′ ≤ σ, so (H1) and y_σ(g) ≤ 2A give y_σ(g) ≤ A + 4A²B < 2A; at σ = 1/2,
y_(1/2)(g) ≤ A by (H3). By (H4), |g⁻¹ − ĝ⁻¹|_k̂ < κ_m on D^κ_s, so by (F3_W) of [[thm:tl5-wg]], g is the restriction of a
solution g′ on some D^κ_(s′), s′ > s, and since y_σ(g′) is continuous in σ and y_s(g′) = y_s(g) < 2A, y_σ(g′) ≤ 2A on
[1/2, s″] for some s″ ∈ (s, s′]. So s″ ∈ I.

I is closed. Let s_n ∈ I increase to s̄ ≤ v*, with solutions g_n on D^κ_(s_n). By (F2_W) of [[thm:tl5-wg]], g_m
restricted to D^κ_(s_n) is g_n for m ≥ n, so the g_n define a smooth metric g on D^κ ∩ {τ₂ < s̄}, with y_σ(g) ≤ 2A for σ
< s̄. By (H2) the components of g and of g⁻¹ in the charts of the atlas are bounded on D^κ ∩ {τ₂ < s̄} together with all
their derivatives, so each component and each derivative is uniformly continuous there and extends continuously to
D^κ_(s̄), the closure of that set; the extended components are smooth, and the extended metric is nondegenerate, since
the components of g⁻¹ extend as well. The extension is tilted, the inequality |g⁻¹ − ĝ⁻¹|_k̂ ≤ κ_m being preserved under
limits, satisfies Ric^W = 0 and equals G^♯ at the points of N ∩ D^κ_(s̄), since each of these conditions is preserved
under limits of the components and their derivatives; it is Lorentzian, being tilted, by [[lem:tl5-wg-norms]] (b). So it
is a solution ḡ on D^κ_(s̄). For σ ≤ s_n, y_σ(ḡ) = y_σ(g_n) ≤ 2A, since y_σ depends only on the restriction to D^κ_σ; so
y_σ(ḡ) ≤ 2A for σ < s̄, and y_(s̄)(ḡ) ≤ 2A by the continuity of y_σ(ḡ) in σ. Hence s̄ ∈ I.

So I = (1/2, v*], and v* ∈ I is the claim. ∎

In [[thm:tl5-hf]], y_σ is the weighted norm Y_σ of [[def:tl5-hf-norm]]: a supremum of the energies of g − ĝ and of its
Lie derivatives along the static Killing field and the six rotations of the seed through the future faces of the tilted
regions, weighted by e^(−φ), with φ the integral of two rates that absorb the linear bulk of the energy identity
pointwise. There A = A_w is of the size of the data error on N and of the residual of ĝ, and B = B_w the constant of the
quadratic remainder, in which the amplification e^(φ/2) of the linear estimate enters once; the condition 4AB < 1 of (H3)
is the closing condition [[eq:tl5-hf-closing]], linear in that amplification.

**Remark {#rem:tl5-beyond}** (Why existence beyond the seed is claimed only on a strip.) [[lem:tl5-continuation]]
concerns smooth data, for which the local theory holds in the double-null gauge ([[thm:tl5-cip]]) and in the wave gauge
([[thm:tl5-wg]]). The data of [[def:tl5-problem]] are not smooth: env is C³ and not C⁴ at v = 1/2 and v = 7/2
([[rem:envelope-regularity]]), and so are the fields P and Q on N there. But for u* < u₀ the problem splits into the seed
and two stages with smooth data, whose solutions glue in class C³ ([[cor:tl5-cip-staged]]); so the regularity of the data
is no obstruction: (F1) of [[thm:tl5-cip]] gives the strip of [[thm:ten-l5]] (b), and the lemma applies stage by stage.
What is missing for a given region is the verification of the hypotheses of [[thm:tl5-hf]] for a background there: that
theorem gives (H1), (H2) and (H4) and reduces (H3) to inequalities between suprema and integrals of explicit functions of
the background, of its residual and of the data on N. The estimate (H1) is one on all of D^κ_s, axes included. An
estimate for the linearised problem on a truncated domain of dependence that avoids the axes would not give (H1): no such
domain contains a region of the form D^κ_s, since D^κ_s contains the axes. The residual bounds of [[sec:tl5-residuals]]
hold at points and on boxes of the region Π of [[eq:tl5-region]], which is not of the form D^κ_s, and are not bounds of
the quantities ε_w and ϱ of [[def:tl5-hf-constants]] over a region D^κ_s. So the hypotheses of [[thm:tl5-hf]] are
established in this paper for no background at 10 l5, and no existence is claimed beyond the strip of [[thm:ten-l5]] (b),
whose width is not estimated.

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
a closing condition of the form 4F²G ε_r < 1, with ε_r the size of the residual and G the constant of a quadratic
remainder, asks a residual ε_r of order 10⁻⁶⁸/G, against the bounds 3.73 × 10⁻⁵ at points and 5.0 × 10⁻⁴ on sub-boxes
of [[prop:tl5-points]] and [[prop:tl5-boxes-second]]. No proof uses these observations.

### The a priori estimate in the wave gauge {#sec:tl5-hf}

This section proves an a priori estimate for solutions of the reduced problem of [[sec:tl5-wg]] close to an explicit
background ĝ, in a norm Y built from characteristic energies with an exponential weight, and with it the hypotheses
(H1), (H2) and (H4) of [[lem:tl5-continuation]] in the wave gauge and (H3) under an explicit closing condition, every
constant being an explicit function of the jets of ĝ, of the data and of the weights. The
estimate has three parts. The first is a weighted energy identity for the linearised operator, the five-dimensional
tensor wave operator of ĝ with its curvature term, on the regions bounded by two hypersurfaces of the tilted foliations
of [[def:tl5-wg-domains]] ([[lem:tl5-hf-identity]]); the whole linear bulk is absorbed pointwise by two rates, one for
each family of hypersurfaces ([[def:tl5-hf-rates]]), and no Grönwall inequality is used ([[prop:tl5-hf-linear]]). The
second is commutation with the static Killing field and the six rotations of the seed, whose deformation tensors measure
only the departure of ĝ from the seed ([[lem:tl5-hf-commutator]]), together with the recovery of all second derivatives
from them and from the equation ([[lem:tl5-hf-recovery]]). The third is the bound of the quadratic terms
([[lem:tl5-hf-quadratic]]) by a Sobolev inequality on the future boundaries ([[lem:tl5-hf-sobolev]]). [[thm:tl5-hf]]
collects them.

We use the notation of [[sec:tl5-wg]]: the background ĝ of [[def:tl5-wg-background]], with Ω̂, ê₃, ê₄, D̂ and R̂, the
region D̄ = [−10, u*] × [1/2, v*] × S³, N₀, N₁ and N = N₀ ∪ N₁, the tilted domains D^κ_s of [[eq:tl5-wg-tilted]] with
τ₁ = u + κ′(v − 1/2), τ₂ = v + κ(u + 10) and κ_m = min(κ, κ′), the norm |·|_k̂ of k̂ ([[eq:tl5-wg-khat]]), and the
operators of [[lem:tl5-wg-linear]]. Throughout, u* < −1. The background is G-invariant and in double-null form, so by
[[lem:tl5-cip-form]] (b) it is a metric of the class in the gauge,

    ĝ = −4Ω̂² du dv + e^(2ζ) (dx − b̂ du)² + e^(2A) dφ1² + e^(2B) dφ2²,      Ω̂² = e^(2W),

with ζ, A and B as in [[eq:tl5-radii]] for its fields R, P, Q and with b̂ the shift β; then ê₃ = ∂_u + b̂ ∂_x, ê₄ = ∂_v,
and e^(ζ + A + B) = R³/4. The round metric of S³ is γ₀ = dx²/(4(1 − x²)) + ((1 + x)/2) dφ1² + ((1 − x)/2) dφ2², and dω :=
dx dφ1 dφ2/4 is its measure.

#### The multiplier, the frame and the operators {#sec:tl5-hf-setting}

**Definition {#def:tl5-hf-frame}** (The multiplier and the frame.) Let f(r) := 1 − r⁻² and c(u) := f(−u)/2, a smooth
function on [−10, u*] with 0 < c < 1/2, and put

    T := ê₄ + c ê₃,    |T| := 2 √c Ω̂,    E₀ := T/|T|,    E₁ := (ê₄ − c ê₃)/|T|.

At each point let f₁, f₂, f₃ be a ĝ-orthonormal frame of the leaf. Then (E₀, E₁, f₁, f₂, f₃) is ĝ-orthonormal, with ĝ(E₀,
E₀) = −1, and

    ê₄ = √c Ω̂ (E₀ + E₁),      ê₃ = (Ω̂/√c) (E₀ − E₁).                                             {#eq:tl5-hf-null-pair}

Put k := ĝ + 2 ĝ(E₀, ·) ⊗ ĝ(E₀, ·), a Riemannian metric in which the frame is orthonormal. For tensors of every type, ⟨·,
·⟩ and |·| denote the inner product and the norm induced by k; for a 2-tensor A, |A|² = Σ A(F_M, F_N)², the sum over the
frame F = (E₀, E₁, f₁, f₂, f₃). Frame components are written A_MN := A(F_M, F_N), with M, N ∈ {0, …, 4}, and indices j, l
∈ {2, 3, 4} refer to f₁, f₂, f₃. The operator norm of a linear map between spaces of tensors is taken in these norms.

For the seed of [[lem:tl5-seed]], b̂ = 0 and T = ∂_v + c ∂_u is a Killing field, the static one: T(R) = f(R)/2 −
f(−u) e^(2W) = 0 by ∂_vR = f(R)/2 and e^(2W) = f(R)/(2f(−u)) ([[lem:tl5-seed]] (b)) and ∂_uR = −2e^(2W) (its proof of
(c)); hence T(e^(2W)) = −c′ e^(2W), and ℒ_T(−4e^(2W) du dv + R² γ₀) = −4(T(e^(2W)) + c′ e^(2W)) du dv + T(R²) γ₀ = 0.
The norm k is the norm k̂ of [[eq:tl5-wg-khat]] with E₀ in place of the vector e₀ = (ê₃ + ê₄)/(2Ω̂) used there.

**Lemma {#lem:tl5-hf-khat}** (The two norms.) For every tensor A of rank r (covariant, contravariant or mixed) at a point
of D̄,

    c^(r/2) |A|_k̂ ≤ |A| ≤ c^(−r/2) |A|_k̂.

*Proof.* By [[eq:tl5-hf-null-pair]] and the definition of e₀ and e₁ := (ê₄ − ê₃)/(2Ω̂) in [[sec:tl5-wg]], E₀ = ch β e₀ +
sh β e₁ and E₁ = sh β e₀ + ch β e₁ with e^β := c^(−1/2), the leaf frame being common to both. So the frame F is the image
of the k̂-orthonormal frame (e₀, e₁, f₁, f₂, f₃) under a linear map whose matrix has singular values e^β, e^(−β), 1, 1,
1; its operator norm and that of its inverse are e^β = c^(−1/2), as c < 1. The components of A in one frame are those in
the other, transformed by this matrix or its inverse transpose in each of the r slots, and the Frobenius norm of the
result is at most e^(rβ) times the Frobenius norm of the components. ∎

**Definition {#def:tl5-hf-operators}** (The operators.) Let 𝓡̂, □̂ and the curvature convention be those of
[[lem:tl5-wg-linear]] (b), and for a symmetric 2-tensor field h put

    L̂ h := □̂ h + 2 𝓡̂ h,      𝒞_αβ h := [D̂_α, D̂_β] h,                                          {#eq:tl5-hf-operators}

so that L̂ h = −2 (d/dt) Ric^W(ĝ + t h)|_(t=0) by [[eq:tl5-wg-lin]], and (𝒞_αβ h)_μν = −R̂^ρ_μαβ h_ρν − R̂^ρ_ναβ h_μρ.
Write 𝒞_MN := 𝒞(F_M, F_N). Let ω_i(V) := ĝ(D̂_V E₀, F_i) for i = 1, …, 4, so that D̂_V E₀ = Σ_(i≥1) ω_i(V) F_i, and for
2-tensors A, B put

    D_i(A, B) := 4 Σ_N (A_iN B_0N + A_0N B_iN),      𝔇_V(A, B) := Σ_(i≥1) ω_i(V) D_i(A, B).      {#eq:tl5-hf-frame-terms}

Then for 2-tensor fields A, B and every vector V,

    V⟨A, B⟩ = ⟨D̂_V A, B⟩ + ⟨A, D̂_V B⟩ + 𝔇_V(A, B).                                                      {#eq:tl5-hf-dk}

For a solution g of the reduced problem, h := g − ĝ lies in the eight-dimensional class subspace of
[[prop:tl5-wg-vacuum]] (b); the estimates below do not use this, and hold for symmetric 2-tensor fields without symmetry.

*Proof of [[eq:tl5-hf-dk]].* In components, ⟨A, B⟩ = A_μν B_ρσ k^μρ k^νσ with k^μρ = ĝ^μρ + 2E₀^μ E₀^ρ, and D̂_V k^μρ =
2((D̂_V E₀)^μ E₀^ρ + E₀^μ (D̂_V E₀)^ρ) = 2 Σ_i ω_i(V) (F_i^μ E₀^ρ + E₀^μ F_i^ρ). The derivative of k in the first pair of
slots gives 2 Σ_i ω_i(V) Σ_N (A_iN B_0N + A_0N B_iN), and in the second pair, by the symmetry of A and B, the same; their
sum is 𝔇_V(A, B). ∎

The vector fields E₀, E₁ and the forms ω_i are smooth on D̄: E₀ and E₁ are built from ê₃, ê₄ and c, and ω_i(V) F_i is the
vector D̂_V E₀, which is orthogonal to E₀; 𝔇_V does not depend on the choice of the leaf frame.

**Definition {#def:tl5-hf-domains}** (Corner regions.) For a ∈ [−10, u*] and b ∈ [1/2, v*] put

    Q(a, b) := D̄ ∩ {τ₁ ≤ a} ∩ {τ₂ ≤ b},

so that D^κ_s = Q(u*, s). Its boundary consists of the parts {u = −10} of N₁ and {v = 1/2} of N₀ and of the future faces
Σ₁(a, b) := Q(a, b) ∩ {τ₁ = a} and Σ₂(a, b) := Q(a, b) ∩ {τ₂ = b}. The coordinates (τ₁, τ₂) are related to (u, v) by a
linear map of determinant 1 − κκ′ ∈ [15/16, 1), and on Q(a, b), u ≤ τ₁ ≤ a and v ≤ τ₂ ≤ b.

If p ∈ Q(a, b), then Q(τ₁(p), τ₂(p)) ⊂ Q(a, b); and Q(a′, b′) ⊂ Q(a, b) for a′ ≤ a, b′ ≤ b.

#### The energy identity {#sec:tl5-hf-identity}

**Definition {#def:tl5-hf-current}** (The current.) Let z and z̲ be smooth positive functions of (u, v) on [−10, u*] ×
[1/2, v*], and 𝒵 := z ê₄ + z̲ ê₃. For a C² symmetric 2-tensor field Ψ on a set Q ⊂ D̄ put

    𝕋[Ψ]_αβ := ⟨D̂_α Ψ, D̂_β Ψ⟩ − (1/2) ĝ_αβ ĝ^(γδ) ⟨D̂_γ Ψ, D̂_δ Ψ⟩,      J[Ψ] := −𝕋[Ψ](T, ·)^♯ + |Ψ|² 𝒵,

the index raised with ĝ, and the flux densities

    e_o[Ψ] := −ĝ(J[Ψ], ê₄) = 𝕋[Ψ](T, ê₄) + 2Ω̂² z̲ |Ψ|²,      e_i[Ψ] := −ĝ(J[Ψ], ê₃) = 𝕋[Ψ](T, ê₃) + 2Ω̂² z |Ψ|².

Write w_± := D̂_(E₀)Ψ ± D̂_(E₁)Ψ and |∇̸Ψ|² := Σ_j |D̂_(f_j)Ψ|².

**Lemma {#lem:tl5-hf-densities}** (The densities.) 𝕋[Ψ](T, ê₄) = c Ω̂² (|w₊|² + |∇̸Ψ|²) and 𝕋[Ψ](T, ê₃) = Ω̂²
(|w₋|² + |∇̸Ψ|²). In particular e_o and e_i are nonnegative, and

    |D̂_(ê₄)Ψ|² = c Ω̂² |w₊|² ≤ e_o,   |D̂_(ê₃)Ψ|² = (Ω̂²/c) |w₋|²,   |Ψ|² ≤ e_o/(2Ω̂² z̲),   |Ψ|² ≤ e_i/(2Ω̂² z),
    Σ_M |D̂_(F_M)Ψ|² = (|w₊|² + |w₋|²)/2 + |∇̸Ψ|² ≤ e_o/(2cΩ̂²) + e_i/(2Ω̂²).                       {#eq:tl5-hf-coercive}

*Proof.* By [[eq:tl5-hf-null-pair]], D̂_(ê₄)Ψ = √c Ω̂ w₊ and D̂_(ê₃)Ψ = (Ω̂/√c) w₋. The inverse metric is ĝ⁻¹ = −(ê₃ ⊗
ê₄ + ê₄ ⊗ ê₃)/(2Ω̂²) + Σ_j f_j ⊗ f_j, so ĝ^(γδ)⟨D̂_γΨ, D̂_δΨ⟩ = −Ω̂⁻² ⟨D̂_(ê₃)Ψ, D̂_(ê₄)Ψ⟩ + |∇̸Ψ|². With ĝ(ê₄, ê₄) =
ĝ(ê₃, ê₃) = 0 and ĝ(ê₃, ê₄) = −2Ω̂² this gives 𝕋(ê₄, ê₄) = |D̂_(ê₄)Ψ|², 𝕋(ê₃, ê₃) = |D̂_(ê₃)Ψ|² and 𝕋(ê₃, ê₄) =
Ω̂² |∇̸Ψ|², and with T = ê₄ + c ê₃ the two formulae follow. Further −ĝ(𝒵, ê₄) = 2Ω̂² z̲ and −ĝ(𝒵, ê₃) = 2Ω̂² z. The last
line uses D̂_(E₀)Ψ = (w₊ + w₋)/2, D̂_(E₁)Ψ = (w₊ − w₋)/2, and that the term |∇̸Ψ|² occurs in both densities, so
that |∇̸Ψ|² ≤ e_i/Ω̂²; then (|w₊|² + |∇̸Ψ|²)/2 ≤ e_o/(2cΩ̂²) and |w₋|²/2 + |∇̸Ψ|²/2 ≤ e_i/(2Ω̂²). ∎

**Lemma {#lem:tl5-hf-divergence}** (The divergence.) Let π := ℒ_T ĝ. For every C² symmetric 2-tensor field Ψ,

    div J[Ψ] = −⟨L̂Ψ, D̂_TΨ⟩ + ℬ[Ψ],
    ℬ[Ψ] := −(1/2) π^(αβ) 𝕋_αβ + 2⟨𝓡̂Ψ, D̂_TΨ⟩ − T^β ⟨D̂^αΨ, 𝒞_αβ Ψ⟩ − ĝ^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ)
            + (1/2) ĝ^(γδ) 𝔇_T(D̂_γΨ, D̂_δΨ) + 2⟨Ψ, D̂_𝒵 Ψ⟩ + 𝔇_𝒵(Ψ, Ψ) + |Ψ|² div 𝒵,                   {#eq:tl5-hf-bulk}

where D̂_αD̂_βΨ denotes the second covariant derivative and the divergence is that of ĝ.

*Proof.* By [[eq:tl5-hf-dk]], D̂^α⟨D̂_αΨ, D̂_βΨ⟩ = ⟨□̂Ψ, D̂_βΨ⟩ + ⟨D̂^αΨ, D̂_αD̂_βΨ⟩ + ĝ^(αγ) 𝔇_(∂_γ)(D̂_αΨ, D̂_βΨ) and
(1/2) D̂_β(ĝ^(γδ)⟨D̂_γΨ, D̂_δΨ⟩) = ĝ^(γδ)⟨D̂_βD̂_γΨ, D̂_δΨ⟩ + (1/2) ĝ^(γδ) 𝔇_(∂_β)(D̂_γΨ, D̂_δΨ). Since D̂_αD̂_βΨ −
D̂_βD̂_αΨ = 𝒞_αβ Ψ, the difference of the two second-derivative terms is ⟨D̂^αΨ, 𝒞_αβ Ψ⟩. Next, div(𝕋(T, ·)^♯) = T^β
D̂^α𝕋_αβ + 𝕋_αβ D̂^α T^β, and 𝕋_αβ D̂^α T^β = (1/2) π^(αβ) 𝕋_αβ since 𝕋 is symmetric and π_αβ = D̂_α T_β + D̂_β T_α.
Finally div(|Ψ|² 𝒵) = 𝒵(|Ψ|²) + |Ψ|² div 𝒵 with 𝒵(|Ψ|²) = 2⟨Ψ, D̂_𝒵 Ψ⟩ + 𝔇_𝒵(Ψ, Ψ), and □̂Ψ = L̂Ψ − 2𝓡̂Ψ. Collecting the
terms gives [[eq:tl5-hf-bulk]]. ∎

The term −T^β⟨D̂^αΨ, 𝒞_αβ Ψ⟩ is absent for scalar fields; for tensors it is zeroth order in Ψ times first order.

**Lemma {#lem:tl5-hf-identity}** (The weighted energy identity.) Let Φ_o ∈ C¹[−10, u*] and Φ_i ∈ C¹[1/2, v*], put a_o :=
Φ_o′, a_i := Φ_i′ and φ := Φ_o(τ₁) + Φ_i(τ₂) on D̄ ∩ {τ₁ ≤ u*, τ₂ ≤ v*}, and let Ψ be a C² symmetric 2-tensor field on Q
:= Q(a, b). With the face densities

    ε₁[Ψ] := (e_o[Ψ] + κ′ e_i[Ψ])/(1 − κκ′),      ε₂[Ψ] := (e_i[Ψ] + κ e_o[Ψ])/(1 − κκ′),              {#eq:tl5-hf-faces}

and dμ := R³ dω, the measure that ĝ induces on the leaves,

    ∫_(Σ₁(a,b)) e^(−φ) ε₁ dμ dτ₂ + ∫_(Σ₂(a,b)) e^(−φ) ε₂ dμ dτ₁
      = ∫_(N₁ ∩ Q) e^(−φ) e_o dμ dv + ∫_(N₀ ∩ Q) e^(−φ) e_i dμ du
        + ∫_Q e^(−φ) (2Ω̂² div J − (a_o + κ a_i) e_o − (a_i + κ′ a_o) e_i) dμ du dv,                {#eq:tl5-hf-identity}

with a_o and a_i evaluated at τ₁ and τ₂. There is no boundary term at the axes.

*Proof.* In the coordinates (u, v, x, φ1, φ2) the volume form of ĝ is 2Ω̂² e^(ζ + A + B) du dv dx dφ1 dφ2: the (u, v, x)
block of ĝ has determinant −4Ω̂⁴ e^(2ζ), as its expansion along the row of v, (−2Ω̂², 0, 0), shows. Since e^(ζ + A + B) =
R³/4 and dω = dx dφ1 dφ2/4, this is 2Ω̂² dμ du dv; the measure dμ = R³ dω is smooth on each leaf, the axes included. In
the coordinates (τ₁, τ₂, x, φ1, φ2), du dv = dτ₁ dτ₂/(1 − κκ′).

The region Q is P × S³ with P the convex polygon {u ≥ −10, v ≥ 1/2, τ₁ ≤ a, τ₂ ≤ b} in the (u, v)-plane, so its boundary
is ∂P × S³; S³ is closed, and the points of the axes are interior points of S³. For a C¹ vector field V on Q, Stokes'
theorem for the form ι_V vol on the manifold with corners Q gives ∫_Q div V vol as the sum over the edges of P of the
integrals over the edge times S³; on the edge {τ₁ = a} the pullback of ι_V vol is dτ₁(V) times 2Ω̂² dμ dτ₂/(1 − κκ′), on
{τ₂ = b} it is dτ₂(V) times 2Ω̂² dμ dτ₁/(1 − κκ′), and on {u = −10} and {v = 1/2}, traversed with the outward
orientation, it is −du(V) 2Ω̂² dμ dv and −dv(V) 2Ω̂² dμ du.

Take V := e^(−φ) J. Since ĝ(ê₄, ·) = −2Ω̂² du and ĝ(ê₃, ·) = −2Ω̂² dv, 2Ω̂² du(J) = e_o and 2Ω̂² dv(J) = e_i; hence 2Ω̂²
dτ₁(J) = e_o + κ′ e_i = (1 − κκ′) ε₁ and 2Ω̂² dτ₂(J) = e_i + κ e_o = (1 − κκ′) ε₂. Finally div(e^(−φ) J) = e^(−φ)(div J −
dφ(J)), and 2Ω̂² dφ(J) = a_o (e_o + κ′ e_i) + a_i (e_i + κ e_o). ∎

If Ψ = 0 on N₀, then e_i[Ψ] = 0 on N₀, since ê₃ and the leaves are tangent to N₀.

#### The pointwise bound and the rates {#sec:tl5-hf-rates}

At a point p of D̄ let 𝒮_p be the space of symmetric 2-tensors at p, a fifteen-dimensional Euclidean space with ⟨·, ·⟩.
The expression ℬ[Ψ](p) of [[eq:tl5-hf-bulk]] depends only on the jet

    ξ := (ξ₊, ξ₋, ξ_∥, ξ₀) := (w₊, w₋, (D̂_(f₁)Ψ, D̂_(f₂)Ψ, D̂_(f₃)Ψ), Ψ) ∈ 𝒮_p ⊕ 𝒮_p ⊕ 𝒮_p³ ⊕ 𝒮_p

at p, and is a quadratic form ℬ_p(ξ) in it, whose coefficients are built from the 2-jet of ĝ at p, the values of c and c′
and the 1-jets of z and z̲. Write it in blocks, ℬ_p(ξ) = Σ_ϰ ℬ_ϰϰ(ξ_ϰ, ξ_ϰ) + 2 Σ_(ϰ<λ) ℬ_ϰλ(ξ_ϰ, ξ_λ), the indices
ranging over (+, −, ∥, 0) in this order, with ℬ_ϰϰ symmetric.

**Definition {#def:tl5-hf-blocks}** (The bulk matrix.) At p let 𝔟_ϰϰ be the largest eigenvalue of the symmetric form ℬ_ϰϰ
on its space (a real number of either sign), 𝔟_ϰλ := sup {ℬ_ϰλ(ξ, ξ′) : |ξ| = |ξ′| = 1} ≥ 0 for ϰ ≠ λ, and 𝔅(p) := 2Ω̂²
(𝔟_ϰλ), a symmetric 4 × 4 matrix with nonnegative off-diagonal entries. Put

    E_o := diag(c Ω̂², 0, c Ω̂², 2Ω̂² z̲),      E_i := diag(0, Ω̂², Ω̂², 2Ω̂² z),

so that e_o = nᵀ E_o n and e_i = nᵀ E_i n for n := (|ξ₊|, |ξ₋|, |ξ_∥|, |ξ₀|), by [[lem:tl5-hf-densities]].

**Lemma {#lem:tl5-hf-pointwise}** (The pointwise bound.) For every C² symmetric 2-tensor field Ψ, at every point,

    2Ω̂² ℬ[Ψ] ≤ nᵀ 𝔅 n,      2Ω̂² |⟨L̂Ψ, D̂_TΨ⟩| ≤ 2Ω̂² |L̂Ψ| (√e_o + √c √e_i),

with n as in [[def:tl5-hf-blocks]].

*Proof.* By the definition of the largest eigenvalue, ℬ_ϰϰ(ξ_ϰ, ξ_ϰ) ≤ 𝔟_ϰϰ |ξ_ϰ|², and by that of 𝔟_ϰλ, ℬ_ϰλ(ξ_ϰ, ξ_λ) ≤
𝔟_ϰλ |ξ_ϰ| |ξ_λ|; summing gives the first inequality. For the second, D̂_TΨ = |T| D̂_(E₀)Ψ = |T| (w₊ + w₋)/2, and |T|/2 =
√c Ω̂; so |⟨L̂Ψ, D̂_TΨ⟩| ≤ |L̂Ψ| √c Ω̂ (|w₊| + |w₋|), and √c Ω̂ |w₊| ≤ √e_o and Ω̂ |w₋| ≤ √e_i by
[[lem:tl5-hf-densities]]. ∎

**Remark {#rem:tl5-hf-blocks}** (The blocks.) In the frame F, with π^MN the components of π raised with η := diag(−1, 1,
1, 1, 1), S^MN := −(1/2)(π^MN − (1/2)(tr_η π) η^MN), D̂_M := D̂_(F_M) and 𝔇_M := 𝔇_(F_M), the terms of [[eq:tl5-hf-bulk]]
are

    −(1/2) π^(αβ) 𝕋_αβ = Σ_(M,N) S^MN ⟨D̂_MΨ, D̂_NΨ⟩,
    2⟨𝓡̂Ψ, D̂_TΨ⟩ − T^β⟨D̂^αΨ, 𝒞_αβΨ⟩
        = |T| (⟨w₊, (𝓡̂ − (1/2) 𝒞_10) Ψ⟩ + ⟨w₋, (𝓡̂ + (1/2) 𝒞_10) Ψ⟩ − Σ_j ⟨D̂_(f_j)Ψ, 𝒞_(j0) Ψ⟩),
    −ĝ^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ) + (1/2) ĝ^(γδ) 𝔇_T(D̂_γΨ, D̂_δΨ)
        = |T| (−Σ_M η^MM 𝔇_M(D̂_MΨ, D̂_0Ψ) + (1/2) Σ_M η^MM 𝔇_0(D̂_MΨ, D̂_MΨ)),
    2⟨Ψ, D̂_𝒵Ψ⟩ = 2z √c Ω̂ ⟨Ψ, w₊⟩ + 2z̲ (Ω̂/√c) ⟨Ψ, w₋⟩,

with D̂_0 = (w₊ + w₋)/2 and D̂_1 = (w₊ − w₋)/2 substituted, and the remaining terms 𝔇_𝒵(Ψ, Ψ) + |Ψ|² div 𝒵 form ℬ₀₀,
where div 𝒵 = z ∂_v log(Ω̂²R³) + z̲ (∂_u log(Ω̂²R³) + ∂_x b̂ + b̂ ∂_x log(Ω̂²R³)) + ∂_v z + ∂_u z̲. The second line uses
𝒞_00 = 0 and T = |T| E₀; the third uses ĝ^(αβ) ∂_α ⊗ ∂_β = Σ_M η^MM F_M ⊗ F_M. So the first-order blocks (ϰ, λ ≠ 0) come
from the deformation π of T and from 𝔇, that is from the acceleration and the deformation of the congruence of E₀; the
blocks (±, 0) are the operators |T|(𝓡̂ ∓ 𝒞_10/2)/2 + z √c Ω̂ (resp. z̲ Ω̂/√c) times the identity, the block (∥, 0) is
−|T|(𝒞_(j0))_j/2, and ℬ₀₀ is zeroth order. In particular, if T is a Killing field of ĝ, as for the seed, the term
−(1/2) π^(αβ) 𝕋_αβ vanishes, and the first-order blocks come from 𝔇 alone. The formula for div 𝒵 follows from div(fV) =
f div V + V(f) and from the coordinate density Ω̂²R³/2 of the
volume form in the coordinates (u, v, x, φ1, φ2) (proof of [[lem:tl5-hf-identity]]): div ∂_v = ∂_v log(Ω̂²R³) and
div(∂_u + b̂ ∂_x) = ∂_u log(Ω̂²R³) + ∂_x b̂ + b̂ ∂_x log(Ω̂²R³).

**Definition {#def:tl5-hf-rates}** (Admissible rates.) Let 𝔐 be a function on D^κ with values in the symmetric m × m
matrices with nonnegative off-diagonal entries, and ℰ_o, ℰ_i functions with values in the nonnegative diagonal m × m
matrices. Continuous functions a_o ≥ 0 on [−10, u*] and a_i ≥ 0 on [1/2, v*] are admissible rates for (𝔐, ℰ_o, ℰ_i) if at
every p ∈ D^κ and for every n ∈ ℝ^m with nonnegative entries

    nᵀ ((a_o + κ a_i) ℰ_o + (a_i + κ′ a_o) ℰ_i − 𝔐) n ≥ 0,
    a_o = a_o(τ₁(p)), a_i = a_i(τ₂(p)).                                                           {#eq:tl5-hf-admissible}

For level zero, m = 4 and (𝔐, ℰ_o, ℰ_i) = (𝔅, E_o, E_i).

Since the off-diagonal entries of the matrix in [[eq:tl5-hf-admissible]] are nonpositive, the condition for all n ≥ 0 is
equivalent to positive semidefiniteness: for any n, nᵀMn ≥ |n|ᵀ M |n| when M has nonpositive off-diagonal entries, |n|
denoting the vector of absolute values. The condition is monotone in the tilt: for fixed values of a_o and a_i its left
side does not decrease when κ or κ′ increases, so nondecreasing rates that satisfy it with κ = κ′ = 0 at every point of
D̄ satisfy it for all κ, κ′ ≥ 0, as τ₁ ≥ u and τ₂ ≥ v on D̄.

**Lemma {#lem:tl5-hf-allocation}** (Explicit admissible rates.) In the setting of [[def:tl5-hf-rates]] suppose that for
each index ϰ at least one of the diagonal entries (ℰ_o)_ϰϰ, (ℰ_i)_ϰϰ is positive everywhere. Let θ_ϰ be measurable
functions on D^κ with values in [0, 1], equal to 1 where (ℰ_i)_ϰϰ = 0 and to 0 where (ℰ_o)_ϰϰ = 0, and t_ϰλ > 0
measurable functions for ϰ < λ, with t_λϰ := 1/t_ϰλ. Put

    d_ϰ := max(0, 𝔐_ϰϰ + Σ_(λ≠ϰ) 𝔐_ϰλ t_ϰλ),
    α_o := max over ϰ with θ_ϰ > 0 of θ_ϰ d_ϰ/(ℰ_o)_ϰϰ,
    α_i := max over ϰ with θ_ϰ < 1 of (1 − θ_ϰ) d_ϰ/(ℰ_i)_ϰϰ.                                          {#eq:tl5-hf-alpha}

If a_o(τ₁(p)) ≥ α_o(p) and a_i(τ₂(p)) ≥ α_i(p) at every p ∈ D^κ, then a_o and a_i are admissible. In particular, for the
bulk matrix of level zero, with the indices (+, −, ∥, 0),

    α_o = max(d₊/(cΩ̂²), θ_∥ d_∥/(cΩ̂²), θ₀ d₀/(2Ω̂² z̲)),
    α_i = max(d₋/Ω̂², (1 − θ_∥) d_∥/Ω̂², (1 − θ₀) d₀/(2Ω̂² z)),

and continuous functions a_o ≥ sup {α_o(p) : τ₁(p) = ·} and a_i ≥ sup {α_i(p) : τ₂(p) = ·} are admissible.

*Proof.* For n ≥ 0 and ϰ ≠ λ, 2 𝔐_ϰλ n_ϰ n_λ ≤ 𝔐_ϰλ (t_ϰλ n_ϰ² + t_λϰ n_λ²), so nᵀ𝔐n ≤ Σ_ϰ d_ϰ n_ϰ². On the other hand,
as κ, κ′ ≥ 0 and the diagonal matrices are nonnegative, nᵀ((a_o + κa_i)ℰ_o + (a_i + κ′a_o)ℰ_i)n ≥ Σ_ϰ (a_o (ℰ_o)_ϰϰ + a_i
(ℰ_i)_ϰϰ) n_ϰ² ≥ Σ_ϰ (θ_ϰ + (1 − θ_ϰ)) d_ϰ n_ϰ², by the choice of α_o and α_i. ∎

The functions θ_ϰ allocate the shared diagonal entries between the two families, point by point; they and the t_ϰλ are
free. Any choice gives admissible rates, and the rates enter the constants only through the integrals of
[[prop:tl5-hf-linear]]. The best rates for a given ĝ can be sought by optimising these choices over a partition of D^κ;
that search is not part of any proof.

**Proposition {#prop:tl5-hf-linear}** (The weighted linear estimate.) Let a ∈ [−10, u*], b ∈ [1/2, v*], let (Ψ_ι)_(ι∈ℐ)
be a finite family of C² symmetric 2-tensor fields on Q(a, b) and m_ι > 0 weights; write
e_o := Σ_ι m_ι e_o[Ψ_ι], e_i := Σ_ι m_ι e_i[Ψ_ι], and ε₁, ε₂ for the corresponding face densities [[eq:tl5-hf-faces]].
Let a_o ≥ 0 and a_i ≥ 0 be continuous on [−10, u*] and [1/2, v*], Φ_o(t) := ∫_(−10)^t a_o, Φ_i(t) := ∫_(1/2)^t a_i and φ
:= Φ_o(τ₁) + Φ_i(τ₂), and let s ≥ 0 be a bounded measurable function on Q(a, b) with

    Σ_ι m_ι 2Ω̂² div J[Ψ_ι] ≤ (a_o + κ a_i) e_o + (a_i + κ′ a_o) e_i + 2Ω̂² s (√e_o + √c √e_i)           {#eq:tl5-hf-hyp}

at every point of Q(a, b), a_o and a_i evaluated at τ₁ and τ₂. For a′ ≤ a and b′ ≤ b let ℰ(a′, b′) be the left side of
[[eq:tl5-hf-identity]] for Q(a′, b′), summed over ι with the weights m_ι, and put

    Y² := sup {ℰ(a′, b′) : −10 ≤ a′ ≤ a, 1/2 ≤ b′ ≤ b},
    Y_d² := ∫_(N₁ ∩ Q(a,b)) e^(−φ) e_o dμ dv + ∫_(N₀ ∩ Q(a,b)) e^(−φ) e_i dμ du,
    𝒮 := ∫_(−10)^a ‖2Ω̂² s‖_(1,t) dt + ∫_(1/2)^b ‖2√c Ω̂² s‖_(2,t) dt,                                {#eq:tl5-hf-source}

where ‖f‖²_(1,t) := ∫_(Σ₁(t,b)) e^(−φ) f² dμ dτ₂/(1 − κκ′) and ‖f‖²_(2,t) := ∫_(Σ₂(a,t)) e^(−φ) f² dμ dτ₁/(1 − κκ′). Then

    Y ≤ Y_d + 𝒮.                                                                                      {#eq:tl5-hf-linear}

Moreover, the unweighted energies ℰ⁰ (the same with φ replaced by 0) satisfy ℰ⁰(a′, b′) ≤ e^(Φ_o(a′) + Φ_i(b′)) Y². With
δ and 𝒮₀ the quantities Y_d and 𝒮 with φ replaced by 0, and y_sep² := sup_(a′ ≤ a) ∫_(Σ₁(a′,b)) ε₁ dμ dτ₂ + sup_(b′ ≤ b)
∫_(Σ₂(a,b′)) ε₂ dμ dτ₁, the sum of the two unweighted suprema taken separately,

    y_sep ≤ F (δ + 𝒮₀),      F² := 2 e^(Φ_o(a) + Φ_i(b)).                                                  {#eq:tl5-hf-f}

*Proof.* Fix a′ ≤ a and b′ ≤ b. [[lem:tl5-hf-identity]] for each Ψ_ι on Q(a′, b′), summed with the weights, has terms
on N₁ and on N₀ whose sum is at most Y_d², as e_o, e_i ≥ 0; the term on N₀ is zero if every Ψ_ι vanishes on N₀ ∩ Q(a,
b). By [[eq:tl5-hf-hyp]]
its bulk is at most ∫_(Q(a′,b′)) e^(−φ) 2Ω̂² s (√e_o + √c √e_i) dμ du dv. In the coordinates (τ₁, τ₂), du dv = dτ₁ dτ₂/(1
− κκ′), and the set Q(a′, b′) ∩ {τ₁ = t} is Σ₁(t, b′) ⊂ Σ₁(t, b). By the Cauchy–Schwarz inequality on it, with e_o/(1 −
κκ′) ≤ ε₁,

    ∫_(Σ₁(t,b′)) e^(−φ) 2Ω̂² s √e_o dμ dτ₂/(1 − κκ′) ≤ ‖2Ω̂² s‖_(1,t) (∫_(Σ₁(t,b′)) e^(−φ) ε₁ dμ dτ₂)^(1/2)
      ≤ ‖2Ω̂² s‖_(1,t) ℰ(t, b′)^(1/2) ≤ ‖2Ω̂² s‖_(1,t) Y,

since ε₂ ≥ 0 and Q(t, b′) is in the family of the supremum. Integrating over t ∈ [−10, a′] and treating the term with √c
√e_i alike on the sets Σ₂(a′, t) ⊂ Σ₂(a, t), with e_i/(1 − κκ′) ≤ ε₂, gives ℰ(a′, b′) ≤ Y_d² + Y𝒮. Taking the supremum,
Y² ≤ Y_d² + Y𝒮, so Y ≤ 𝒮/2 + (𝒮²/4 + Y_d²)^(1/2) ≤ Y_d + 𝒮.

Since a_o, a_i ≥ 0, φ is nondecreasing in τ₁ and τ₂, and on Q(a′, b′) it is at most Φ_o(a′) + Φ_i(b′); hence ℰ⁰(a′, b′) ≤
e^(Φ_o(a′) + Φ_i(b′)) ℰ(a′, b′). Each of the two suprema in y_sep² is at most a supremum of ℰ⁰ over the family, so y_sep²
≤ 2 e^(Φ_o(a) + Φ_i(b)) Y². Finally φ ≥ 0 gives Y_d ≤ δ and 𝒮 ≤ 𝒮₀. ∎

**Corollary {#cor:tl5-hf-level0}** (Level zero.) Let a_o, a_i be admissible rates for (𝔅, E_o, E_i), and Ψ a C² symmetric
2-tensor field on Q(a, b). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ) with weight 1 and s
:= |L̂Ψ|, and so [[eq:tl5-hf-linear]] and [[eq:tl5-hf-f]] hold.

*Proof.* By [[lem:tl5-hf-divergence]] and [[lem:tl5-hf-pointwise]], 2Ω̂² div J ≤ nᵀ𝔅n + 2Ω̂² |L̂Ψ| (√e_o + √c √e_i), and
by [[eq:tl5-hf-admissible]], nᵀ𝔅n ≤ (a_o + κa_i) e_o + (a_i + κ′a_o) e_i, as e_o = nᵀE_on and e_i = nᵀE_in. ∎

**Remark {#rem:tl5-hf-weight}** (The weight.) The weight e^(−φ) lets each density be paid by the rate of its own family
at each point, and the estimate [[eq:tl5-hf-linear]] has constant 1 in the weighted norm; the factor e^(φ/2) appears only
on passing to unweighted energies. The rates need not be functions of τ₁ and τ₂ separately: the proof uses only that
dφ(J) dominates the bulk, and any C¹ function φ = φ(τ₁, τ₂) ≥ 0 with ∂_(τ₁)φ ≥ 0, ∂_(τ₂)φ ≥ 0 and
[[eq:tl5-hf-admissible]] at every
point with (a_o, a_i) := (∂_(τ₁)φ, ∂_(τ₂)φ) gives [[eq:tl5-hf-linear]], with F² = 2 e^(φ(a, b)).

#### Commutation {#sec:tl5-hf-commutation}

**Definition {#def:tl5-hf-fields}** (The commutation fields.) Write S³ ⊂ ℂ² = ℝ⁴ with z₁ = X₁ + iX₂ and z₂ = X₃ + iX₄, so
that x = |z₁|² − |z₂|² and φ_i = arg z_i, and for 1 ≤ a < b ≤ 4 let K_ab := X_a ∂_(X_b) − X_b ∂_(X_a), the rotation
fields of S³, extended to D̄ independently of (u, v). Put

    Γ := {T, K₁₂, K₃₄, K₁₃, K₁₄, K₂₃, K₂₄},      π^Z := ℒ_Z ĝ   (Z ∈ Γ).

For a word I = (Z₁, …, Z_j) in Γ put |I| := j and ℒ^I := ℒ_(Z₁) ⋯ ℒ_(Z_j), ℒ^∅ := 1; for a symmetric 2-tensor field h,
Ψ_I := ℒ^I h.

**Lemma {#lem:tl5-hf-fields}** (The commutation fields.) (a) Each Z ∈ Γ is smooth on D̄; K₁₂ = ∂_φ1, K₃₄ = ∂_φ2, and
Σ_(a<b) K_ab ⊗ K_ab = γ₀⁻¹. Hence the symmetric 3 × 3 matrix M_jl := Σ_(a<b) ĝ(K_ab, f_j) ĝ(K_ab, f_l) is positive
definite, with smallest eigenvalue

    λ_M = R² min(e^(−2(P + Q)), e^(2P), e^(2Q)),                                                      {#eq:tl5-hf-lambda}

and the coefficients c^ab_j := Σ_l (M⁻¹)_jl ĝ(K_ab, f_l) satisfy Σ_(a<b) c^ab_j K_ab = f_j and Σ_j |Σ_(a<b) c^ab_j v_ab|²
≤ λ_M⁻¹ Σ_(a<b) |v_ab|² for vectors v_ab of any Euclidean space.

(b) π^(K₁₂) = π^(K₃₄) = 0 for every background, and for the seed π^Z = 0 for every Z ∈ Γ.

(c) For every background and every Z ∈ Γ, π^Z(ê₄, ê₄) = π^Z(ê₃, ê₃) = 0; and π^(K_ab)(ê₄, Y) = 0 for Y tangent to the
leaves.

*Proof.* (a) K_ab is the restriction to S³ of a linear vector field of ℝ⁴ tangent to S³, so it is smooth; with z₁ =
√((1 + x)/2) e^(iφ1) and z₂ = √((1 − x)/2) e^(iφ2), K₁₂ and K₃₄ generate the rotations of φ1 and φ2. For ω ∈ S³ and a
covector ζ of ℝ⁴, Σ_(a<b) (X_a ζ_b − X_b ζ_a)² = |X|²|ζ|² − (X·ζ)² = |ζ − (X·ζ)X|², which is γ₀⁻¹ applied to the
restriction of ζ to TS³; so Σ K_ab ⊗ K_ab = γ₀⁻¹. With γ̂ the metric of the leaf, M is the matrix of γ₀⁻¹ in the frame
γ̂(f_j, ·), so its eigenvalues are those of γ̂ relative to γ₀. In the chart (x, φ1, φ2), γ̂ and γ₀ are diagonal with
ratios e^(2ζ) · 4(1 − x²) = R² e^(−2(P + Q)), e^(2A) · 2/(1 + x) = R² e^(2P) and e^(2B) · 2/(1 − x) = R² e^(2Q), by
[[eq:tl5-radii]]; at the axes by continuity. Next Σ_ab c^ab_j K_ab = Σ_(l,m) (M⁻¹)_jl M_lm f_m = f_j, since K_ab is
tangent to the leaves. The matrix C := (c^ab_j) is M⁻¹G with G_(l,ab) := ĝ(K_ab, f_l) and GGᵀ = M, so CCᵀ = M⁻¹ and the
operator norm of C is λ_M^(−1/2).

(b) The components of ĝ in (u, v, x, φ1, φ2) do not depend on φ1 and φ2. The seed of [[lem:tl5-seed]] is of the class
with b̂ = 0 and P = Q = 0, so its leaves are round of radius R and the K_ab are Killing for it, and T is its static
Killing field (the remark after [[def:tl5-hf-frame]]).

(c) For a vector field Z and a vector field V, π^Z(V, V) = 2ĝ(D̂_V Z, V) = 2V(ĝ(Z, V)) − 2ĝ(Z, D̂_V V). The background is
a warped product over its orbit space, which is totally geodesic ([[lem:warped-ricci]], proof: no Christoffel symbol with
one index φ_i and two orbit indices), so D̂_(ê₄) ê₄ = 2ω ê₄ and D̂_(ê₃) ê₃ = 2ω̲ ê₃ with ω := ê₄(W), ω̲ := ê₃(W), by
[[lem:tl5-connection]]. For K = K_ab, ĝ(K, ê₄) = ĝ(K, ê₃) = 0, as K is tangent to the leaves and ĝ(∂_x, ê₃) = −e^(2ζ)
b̂ + b̂ e^(2ζ) = 0; so π^K(ê₄, ê₄) = −4ω ĝ(K, ê₄) = 0 and π^K(ê₃, ê₃) = 0. For T = ê₄ + c ê₃, with ê₄(c) = 0, π^T(ê₄,
ê₄) = 2c ĝ(D̂_(ê₄) ê₃, ê₄) = 2c (ê₄(ĝ(ê₃, ê₄)) − ĝ(ê₃, 2ω ê₄)) = 2c(−4ω Ω̂² + 4ω Ω̂²) = 0, and π^T(ê₃, ê₃) = 2ĝ(D̂_(ê₃)
ê₄, ê₃) + 2ê₃(c) ĝ(ê₃, ê₃) + 2c ĝ(D̂_(ê₃) ê₃, ê₃) = 2(−4ω̲ Ω̂² + 4ω̲ Ω̂²) = 0. Finally [ê₄, K] = 0, so for Y tangent to
the leaves π^K(ê₄, Y) = ĝ(D̂_K ê₄, Y) + ĝ(D̂_Y K, ê₄) = ĝ(D̂_K ê₄, Y) − ĝ(K, D̂_Y ê₄), which vanishes because (X, Y) ↦
ĝ(D̂_X ê₄, Y) is symmetric on vectors tangent to the leaves: its antisymmetric part is −ĝ(ê₄, [X, Y]) for leaf-tangent
extensions, and [X, Y] is tangent to the leaves. ∎

By (c), in π^(αβ) D̂_αD̂_βΨ the components D̂²Ψ(ê₃, ê₃) and D̂²Ψ(ê₄, ê₄) never occur, and for the rotations D̂²Ψ(ê₃, f_j)
does not occur either: the coefficient of D̂²Ψ(ê₃, f_j) is a multiple of π(ê₄, f_j).

**Lemma {#lem:tl5-hf-commutator}** (The commutator.) For a symmetric 2-tensor field δ let

    Γ′[δ]^ρ_αβ := (1/2) ĝ^(ρσ) (D̂_α δ_σβ + D̂_β δ_σα − D̂_σ δ_αβ),

and let 𝒦[δ] be the second-order operator

    (𝒦[δ]Ψ)_μν := −δ^(αβ) D̂_αD̂_βΨ_μν − ĝ^(αβ) Γ′^ρ_αβ D̂_ρΨ_μν − 2ĝ^(αβ) (Γ′^ρ_αμ D̂_βΨ_ρν + Γ′^ρ_αν D̂_βΨ_μρ)
                 − ĝ^(αβ) ((D̂_αΓ′)^ρ_βμ Ψ_ρν + (D̂_αΓ′)^ρ_βν Ψ_μρ) + 2 (D𝓡̂[δ]Ψ)_μν,                      {#eq:tl5-hf-k}

indices of δ raised with ĝ, Γ′ = Γ′[δ], and D𝓡̂[δ] := (d/dt) 𝓡̂_(ĝ + tδ)|_(t=0), the derivative of the operator 𝓡̂ of
[[lem:tl5-wg-linear]] for the metric ĝ + tδ: with δR̂^ρ_σμν = D̂_μ Γ′^ρ_νσ − D̂_ν Γ′^ρ_μσ and δR̂ic_σν = δR̂^ρ_σρν, it is
(D𝓡̂[δ]Ψ)_αβ = δ(R_αμβν g^(μa) g^(νb)) Ψ_ab − (1/2) δ(Ric_αρ g^(ρa)) Ψ_aβ − (1/2) Ψ_αa δ(g^(aρ) Ric_ρβ), each δ the
derivative at t = 0 along ĝ + tδ, with δg^(μa) = −δ^(μa) and δR_αμβν = ĝ_αλ δR̂^λ_μβν + δ_αλ R̂^λ_μβν. Then for every
vector field Z on D̄ and every C³ symmetric 2-tensor field Ψ,

    L̂ ℒ_Z Ψ = ℒ_Z L̂Ψ − 𝒦[π^Z] Ψ.                                                                      {#eq:tl5-hf-comm}

*Proof.* For a metric g let L_g := □_g + 2𝓡_g. For a diffeomorphism σ, σ*(L_g Ψ) = L_(σ*g)(σ*Ψ), as L_g is built from g
alone. Let σ_t be the local flow of Z near an interior point. Differentiating σ_t*(L̂Ψ) = L_(σ_t*ĝ)(σ_t*Ψ) at t = 0, with
(d/dt) σ_t*ĝ|_(t=0) = π^Z, gives ℒ_Z L̂Ψ = (d/dt) L_(ĝ + tπ^Z)Ψ|_(t=0) + L̂ ℒ_ZΨ, at interior points and by continuity on
D̄. It remains to compute the derivative of L_(ĝ+tδ)Ψ at t = 0. Along g_t := ĝ + tδ the connection changes by the tensor
Γ′ := (d/dt) Γ(g_t)|_(t=0) = Γ′[δ]. So (d/dt) (D_tΨ)_βμν = −Γ′^ρ_βμ Ψ_ρν − Γ′^ρ_βν Ψ_μρ, and differentiating D_t(D_tΨ)
gives

    (d/dt) (D_tD_tΨ)_αβμν = −D̂_α(Γ′^ρ_βμ Ψ_ρν + Γ′^ρ_βν Ψ_μρ) − Γ′^ρ_αβ D̂_ρΨ_μν − Γ′^ρ_αμ D̂_βΨ_ρν − Γ′^ρ_αν D̂_βΨ_μρ.

Contracting with ĝ^(αβ), using the symmetry of Γ′ in its lower indices and (d/dt) g_t^(αβ) = −δ^(αβ), gives the first
four terms of [[eq:tl5-hf-k]]; the last is the derivative of 2𝓡. The formula for δR̂ is the variation of the curvature
under a change Γ′ of the connection, and δRic is its contraction. ∎

Two more identities are used. For a tensor field A of type (0, r) and a vector field Z,

    ℒ_Z(D̂A) − D̂(ℒ_Z A) = −Γ′[π^Z] ⋆ A,      (Γ′ ⋆ A)_(αμ₁⋯μ_r) := Σ_i Γ′^ρ_(αμ_i) A_(μ₁⋯ρ⋯μ_r),      {#eq:tl5-hf-lie-d}

the index ρ in the i-th place; this is the derivative at t = 0 of σ_t*D̂ = D_(σ_t*ĝ), as in the proof above. And

    ℒ_ZΨ = D̂_ZΨ + Ψ(D̂Z ·, ·) + Ψ(·, D̂Z ·),      (Ψ(D̂Z ·, ·))(X, Y) := Ψ(D̂_X Z, Y),                  {#eq:tl5-hf-lie}

since D̂ is torsion free.

**Definition {#def:tl5-hf-triples}** (Second-order operators.) A second-order operator is a triple 𝔭 = (𝔭², 𝔭¹, 𝔭⁰) of
smooth tensor fields, acting by 𝔭Ψ := 𝔭² · D̂²Ψ + 𝔭¹ · D̂Ψ + 𝔭⁰ · Ψ, where · denotes a fixed contraction of all indices
of the derivative. By [[eq:tl5-hf-k]], 𝒦[π^Z] is such a triple, with 𝒦[π^Z]² the contraction with −(π^Z)^(αβ). For a
vector field W, define 𝔏_W 𝔭 by ℒ_W(𝔭Ψ) = 𝔭(ℒ_WΨ) + (𝔏_W 𝔭)Ψ; by [[eq:tl5-hf-lie-d]] applied to Ψ and to D̂Ψ,

    𝔏_W 𝔭 = (ℒ_W 𝔭², ℒ_W 𝔭¹ − 𝔭² · (Γ′ ⋆ ·) − 𝔭² · (Γ′ ⋆ ·)′, ℒ_W 𝔭⁰ − 𝔭² · (D̂Γ′ ⋆ ·) − 𝔭¹ · (Γ′ ⋆ ·)),
    Γ′ := Γ′[π^W],

where 𝔭² · (Γ′ ⋆ ·) is the first-order coefficient of Ψ ↦ 𝔭² · (Γ′ ⋆ D̂Ψ), and 𝔭² · (Γ′ ⋆ ·)′ and 𝔭² · (D̂Γ′ ⋆ ·) are the
first- and zeroth-order coefficients of Ψ ↦ 𝔭² · D̂(Γ′ ⋆ Ψ); so 𝔏_W 𝔭 is again a second-order operator, and its
coefficients are explicit in the jets of 𝔭, of W and of ĝ.

**Lemma {#lem:tl5-hf-system}** (The commuted equation.) Let h be a C^(N+2) symmetric 2-tensor field and I = (Z₁, …, Z_j)
a word, j ≤ N. Then

    L̂Ψ_I = ℒ^I L̂h − Σ_(k=1)^j Σ_(S ⊂ {1, …, k−1}) (𝔏_(Z_S) 𝒦[π^(Z_k)]) Ψ_(J(k,S)),                  {#eq:tl5-hf-system}

where, for S = {s₁ < ⋯ < s_m}, 𝔏_(Z_S) := 𝔏_(Z_(s₁)) ⋯ 𝔏_(Z_(s_m)), and J(k, S) is the word obtained from (Z₁, …,
Z_(k−1)) by deleting the letters with indices in S, followed by (Z_(k+1), …, Z_j); |J(k, S)| = j − 1 − |S|.

*Proof.* By [[eq:tl5-hf-comm]] and induction on j, L̂Ψ_I = ℒ^I L̂h − Σ_k ℒ_(Z₁) ⋯ ℒ_(Z_(k−1))
(𝒦[π^(Z_k)]Ψ_(Z_(k+1)⋯Z_j)). By the definition of 𝔏 and induction on m, ℒ_(W₁) ⋯ ℒ_(W_m)(𝔭Ψ) = Σ_(S ⊂ {1,…,m}) (𝔏_(W_S)
𝔭)(ℒ_(W_(S^c)) Ψ), the complement taken in its order: for m = 1 this is the definition, and applying ℒ_(W₁) to the
identity for (W₂, …, W_m) splits each term into the term with 1 ∉ S and the term with 1 ∈ S. ∎

For the seed every operator in the sum vanishes, since π^Z = 0 for all Z ∈ Γ.

**Lemma {#lem:tl5-hf-recovery}** (Recovery of second derivatives.) At a point p of D̄ let H be a symmetric tensor of type
(2, 0) with |H| ≤ 1/4, and Ψ a C² symmetric 2-tensor field near p. Put 𝔣 := L̂Ψ + H^(αβ) D̂_αD̂_βΨ at p,

    K_rec := max(|T|⁻¹, λ_M^(−1/2)),      𝔷_Z := 3 |D̂Z| |D̂Ψ| + 2 |D̂²Z| |Ψ|   (Z ∈ Γ),

with λ_M of [[eq:tl5-hf-lambda]], and let ‖𝓡̂‖ and ‖𝒞_(·1)‖ be the operator norms of Ψ ↦ 𝓡̂Ψ and of Ψ ↦
(𝒞_(M1)Ψ)_(M=0,…,4) on 𝒮_p. Then at p

    (1 − (4/3)|H|) |D̂²Ψ| ≤ (√3 + 8/3) K_rec ((Σ_(Z∈Γ) |D̂ ℒ_ZΨ|²)^(1/2) + (Σ_(Z∈Γ) 𝔷_Z²)^(1/2))
                          + (4/3) |𝔣| + ((8/3)‖𝓡̂‖ + √2 ‖𝒞_(·1)‖) |Ψ|.                              {#eq:tl5-hf-recovery}

For H = 0 the proof gives D̂²Ψ(p) as an explicit linear function ℛ_p of (D̂ℒ_ZΨ(p))_(Z∈Γ), D̂Ψ(p), Ψ(p) and L̂Ψ(p), with
coefficients built from the 2-jets of ĝ and of the fields Z at p.

*Proof.* Write D̂²Ψ(A, B) for the second covariant derivative in the frame directions F_A, F_B, and let X be the sum
of |D̂²Ψ(A, B)|² over all A and all B ≠ 1. By [[eq:tl5-hf-lie]], for Z ∈ Γ and every A,

    D̂_A(ℒ_ZΨ) = Z^B D̂²Ψ(A, B) + 𝔷_(Z,A),
    𝔷_(Z,A) := (D̂_A Z)^B D̂_BΨ + (D̂_AΨ)(D̂Z ·, ·) + (D̂_AΨ)(·, D̂Z ·) + Ψ(D̂_A D̂Z ·, ·) + Ψ(·, D̂_A D̂Z ·),

and (Σ_A |𝔷_(Z,A)|²)^(1/2) ≤ 𝔷_Z, each contraction being bounded by the product of the norms. Since T = |T| E₀, D̂²Ψ(A,
0) = |T|⁻¹ (D̂_A ℒ_TΨ − 𝔷_(T,A)); since f_j = Σ_ab c^ab_j K_ab ([[lem:tl5-hf-fields]] (a)), D̂²Ψ(A, j) = Σ_ab c^ab_j
(D̂_A ℒ_(K_ab)Ψ − 𝔷_(K_ab,A)). By [[lem:tl5-hf-fields]] (a) and Minkowski's inequality,

    X^(1/2) ≤ K_rec ((Σ_Z |D̂ℒ_ZΨ|²)^(1/2) + (Σ_Z 𝔷_Z²)^(1/2)).

For A ≠ 1, D̂²Ψ(A, 1) = D̂²Ψ(1, A) + 𝒞_(A1)Ψ, and D̂²Ψ(1, A) is a term of X; so Σ_(A≠1) |D̂²Ψ(A, 1)|² ≤ 2X +
2‖𝒞_(·1)‖² |Ψ|². For the entry (1, 1), ĝ^(αβ) D̂_αD̂_βΨ = −D̂²Ψ(0, 0) + D̂²Ψ(1, 1) + Σ_j D̂²Ψ(j, j) and H^(αβ)
D̂_αD̂_βΨ = Σ_(M,N) H^MN D̂²Ψ(M, N), with |H^MN| the frame components of H; so

    (1 + H^11) D̂²Ψ(1, 1) = 𝔣 − 2𝓡̂Ψ + D̂²Ψ(0, 0) − Σ_j D̂²Ψ(j, j) − Σ_((M,N)≠(1,1)) H^MN D̂²Ψ(M, N).

With |H^11| ≤ |H| ≤ 1/4 and |D̂²Ψ(0, 0)| + Σ_j |D̂²Ψ(j, j)| ≤ 2X^(1/2), four terms of X, |D̂²Ψ(1, 1)| ≤ (4/3)(|𝔣| +
2‖𝓡̂‖|Ψ| + 2X^(1/2) + |H| |D̂²Ψ|). Finally |D̂²Ψ| ≤ (3X + 2‖𝒞_(·1)‖²|Ψ|²)^(1/2) + |D̂²Ψ(1, 1)| ≤ √3 X^(1/2) + √2
‖𝒞_(·1)‖ |Ψ| + |D̂²Ψ(1, 1)|, and collecting gives [[eq:tl5-hf-recovery]]. For H = 0 every step is an identity between the
frame components, which defines ℛ_p. ∎

**Definition {#def:tl5-hf-coupling}** (The couplings at level N.) Fix N ≥ 1 and μ ∈ (0, 1]. For a C^(N+2) symmetric
2-tensor field h put 𝔤 := L̂h. At a point p, substitute in [[eq:tl5-hf-system]], for each word I with |I| ≤ N, every
second derivative D̂²Ψ_J (|J| < |I|) by ℛ_p of [[lem:tl5-hf-recovery]] with Ψ := Ψ_J, using D̂ℒ_ZΨ_J = D̂Ψ_(ZJ) and L̂Ψ_J
given again by [[eq:tl5-hf-system]]; after finitely many steps this writes

    L̂Ψ_I(p) = Σ_(|J|≤|I|) 𝔄_IJ (D̂Ψ_J(p), Ψ_J(p)) + Σ_(|J|≤|I|) 𝔔_IJ (ℒ^J 𝔤(p)),

with 𝔔_II the identity, 𝔄_IJ zero on Ψ_J when |J| = |I|, and every 𝔄_IJ, 𝔔_IJ a linear map built from the jets of ĝ and
of the fields Γ at p, of order at most N + 3, and independent of h. For levels j′ ≤ j ≤ N and ϰ ∈ {+, −, ∥, 0} let
ℭ_(jj′ϰ)(p) be the operator norm of the map (ξ_ϰ[Ψ_J])_(|J|=j′) ↦ (𝔄_IJ-part)_(|I|=j) from the ϰ-components of the jets
of level j′ (in the notation of [[def:tl5-hf-blocks]]) to the family (L̂Ψ_I)_(|I|=j), and 𝔮_(jj′)(p) that of
(ℒ^J𝔤)_(|J|=j′) ↦ (𝔔_IJ ℒ^J𝔤)_(|I|=j), in the Euclidean norms of the families; 𝔮_(jj) = 1. Let 𝔅_N be the symmetric
matrix of size 4(N + 1), indexed by (j, ϰ), with

    𝔅_N := diag(𝔅, …, 𝔅) + 𝔒 + 𝔒ᵀ,
    𝔒_((j,σ),(j′,ϰ)) := √c Ω̂³ μ^((j − j′)/2) ℭ_(jj′ϰ)   (σ ∈ {±}, j′ ≤ j),                               {#eq:tl5-hf-bn}

the other entries of 𝔒 being zero, and E_o^N, E_i^N the block diagonal matrices with N + 1 copies of E_o and E_i.

The maps 𝔄_IJ with |J| = |I| come only from the recovery of D̂²Ψ_(I′) with |I′| = |I| − 1: they are the same-level
couplings. All couplings vanish for the seed.

**Proposition {#prop:tl5-hf-linear-n}** (The linear estimate at level N.) Let h be a C^(N+2) symmetric 2-tensor field on
Q(a, b), 𝔤 := L̂h, and let a_o, a_i be admissible
rates for (𝔅_N, E_o^N, E_i^N). Then [[eq:tl5-hf-hyp]] holds for the family (Ψ_I)_(|I|≤N) with the weights μ^|I| and

    s_N[𝔤] := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) G_(j′))²)^(1/2),
    G_(j′) := (Σ_(|J|=j′) |ℒ^J 𝔤|²)^(1/2),                                                                {#eq:tl5-hf-sn}

and so [[eq:tl5-hf-linear]] and [[eq:tl5-hf-f]] hold for it.

*Proof.* At a point, let n^(j)_ϰ := (Σ_(|I|=j) |ξ_ϰ[Ψ_I]|²)^(1/2) and ñ^(j) := μ^(j/2) n^(j). Since 𝔅
has nonnegative off-diagonal entries, the Cauchy–Schwarz inequality over the words of level j gives Σ_(|I|=j) n[Ψ_I]ᵀ 𝔅
n[Ψ_I] ≤ n^(j)ᵀ 𝔅 n^(j), so by [[lem:tl5-hf-pointwise]] the terms ℬ contribute at most Σ_j ñ^(j)ᵀ 𝔅 ñ^(j). By
[[lem:tl5-hf-divergence]] the remaining terms are −2Ω̂² Σ_I μ^|I| ⟨L̂Ψ_I, D̂_TΨ_I⟩, and |⟨L̂Ψ_I, D̂_TΨ_I⟩| ≤ √c
Ω̂ |L̂Ψ_I| (|w₊[Ψ_I]| + |w₋[Ψ_I]|). By the Cauchy–Schwarz inequality over the words of level j and
[[def:tl5-hf-coupling]],

    Σ_(|I|=j) |L̂Ψ_I| (|w₊| + |w₋|) ≤ (n^(j)_+ + n^(j)_−) (Σ_(j′≤j) Σ_ϰ ℭ_(jj′ϰ) n^(j′)_ϰ + Σ_(j′≤j) 𝔮_(jj′) G_(j′)).

Multiplied by 2√c Ω̂³ μ^j, the first part is 2√c Ω̂³ Σ μ^((j−j′)/2) ℭ_(jj′ϰ) (ñ^(j)_+ + ñ^(j)_−) ñ^(j′)_ϰ = ñᵀ(𝔒 + 𝔒ᵀ)ñ;
so the bulk without the forcing terms is at most ñᵀ𝔅_N ñ, which by admissibility is at most (a_o + κa_i) e_o + (a_i +
κ′a_o) e_i, as e_o = Σ_j ñ^(j)ᵀ E_o ñ^(j) and e_i likewise. The forcing part is 2√c Ω̂³ Σ_j μ^(j/2) 𝔊_j (ñ^(j)_+ +
ñ^(j)_−) with 𝔊_j := Σ_(j′≤j) 𝔮_(jj′) G_(j′), and by the Cauchy–Schwarz inequality over j, with c Ω̂² Σ_j (ñ^(j)_+)² ≤
e_o and Ω̂² Σ_j (ñ^(j)_−)² ≤ e_i, it is at most 2Ω̂² s_N[𝔤] (√e_o + √c √e_i). ∎

#### Bounds at a point {#sec:tl5-hf-sobolev}

**Lemma {#lem:tl5-hf-sphere}** (Sobolev on S³.) For f ∈ C²(S³) and ω ∈ S³,

    |f(ω)|² ≤ 6 C_(S³)² ∫_(S³) (f² + Σ_(a<b) (K_ab f)² + Σ_(a<b) Σ_(c<d) (K_cd K_ab f)²) dω,
    C_(S³)² := Σ_(n≥0) (n + 1)²/(2π² (1 + n(n + 2))²) = 1/12.                                         {#eq:tl5-hf-sphere}

*Proof.* Let f = Σ_n f_n be the expansion in spherical harmonics, f_n of degree n, with −Δf_n = n(n + 2) f_n, where Δ is
the Laplacian of γ₀; the space of degree n has dimension (n + 1)², and its reproducing kernel at (ω, ω) is (n +
1)²/(2π²), the volume of S³ being 2π² = ∫ dω, so |f_n(ω)|² ≤ (n + 1)² ‖f_n‖²/(2π²) with ‖·‖ the norm of L²(S³, dω). By
the Cauchy–Schwarz inequality over n and Parseval's identity, |f(ω)| ≤ Σ_n (n + 1)(2π²)^(−1/2) ‖f_n‖ ≤ C_(S³) ‖(1 − Δ)f‖,
where, as 1 + n(n + 2) = (n + 1)², C_(S³)² = Σ_(m≥1) 1/(2π² m²) = 1/12,
the series converging as its terms are O(n⁻²). Since the K_ab are Killing fields of γ₀ with Σ K_ab ⊗ K_ab = γ₀⁻¹
([[lem:tl5-hf-fields]] (a)), |df|²_(γ₀) = Σ (K_ab f)² and Δf = Σ_(a<b) K_ab K_ab f; so ‖(1 − Δ)f‖² = ‖f‖² + 2‖df‖² +
‖Δf‖² ≤ ‖f‖² + 2 Σ‖K_ab f‖² + 6 Σ ‖K_ab K_ab f‖², which is at most six times the integral in [[eq:tl5-hf-sphere]]. ∎

**Definition {#def:tl5-hf-component}** (Components.) Let W_a := ∂_(X_a) − X_a Σ_b X_b ∂_(X_b) (a = 1, …, 4), the
projections of the coordinate fields of ℝ⁴ to TS³, and 𝒱 := (∂_u, ∂_v, W₁, …, W₄). For a tensor A of rank r at a point
let A_e be the array of its 6^r components on 𝒱 and |A|_e its Euclidean norm, and put

    𝔳² := Σ_(V∈𝒱) |V|²,      𝔴² := Σ_M (du(F_M)² + dv(F_M)² + |F_M − du(F_M) ∂_u − dv(F_M) ∂_v|²_(γ₀)).

Explicitly, |∂_v|² = 2cΩ̂², |∂_u| ≤ √(2/c) Ω̂ + |b̂| e^ζ, Σ_a |W_a|² = R² (e^(−2(P+Q)) + e^(2P) + e^(2Q)), and 𝔴² = 2(1 +
c²)/|T|² + 2c² |b̂ ∂_x|²_(γ₀)/|T|² + R⁻² (e^(2(P+Q)) + e^(−2P) + e^(−2Q)), all smooth on D̄, as b̂ ∂_x is the shift
vector field of ĝ, smooth on each leaf ([[lem:tl5-cip-form]] (a)).

**Lemma {#lem:tl5-hf-components}** (Components.) For a tensor A of rank r, |A|_e ≤ 𝔳^r |A| and |A| ≤ 𝔴^r |A|_e. For a
rotation K_ab, the components of ℒ_(K_ab) A and the derivative K_ab(A_e) differ by the action of an antisymmetric matrix
of norm at most 1 on each index in the place of a W, so |K_ab(A_e) − (ℒ_(K_ab) A)_e| ≤ r |A|_e; and ∂_u, ∂_v commute with
every field of 𝒱, so ∂(A_e) = (ℒ_∂ A)_e for ∂ = ∂_u, ∂_v.

*Proof.* |A(V₁, …, V_r)| ≤ |A| Π|V_i|, and summing the squares over 𝒱^r gives the first inequality. On the leaves Σ_a
dX_a(Y) W_a = Y for Y ∈ TS³, as W_a = P∂_(X_a) with P the projection; so every vector Y equals du(Y)∂_u + dv(Y)∂_v + Σ_a
dX_a(Y_∥) W_a, with Y_∥ := Y − du(Y)∂_u − dv(Y)∂_v, and Σ_a dX_a(Y_∥)² = |Y_∥|²_(γ₀). Expanding A(F_(M₁), …, F_(M_r)) in
this way and applying the Cauchy–Schwarz inequality gives the second. K_ab is the restriction of a linear field X ↦ BX
with B antisymmetric of norm 1, and [K_ab, W_c] = Σ_d B_cd W_d, as the flow of K_ab is a rotation commuting with the
projection; [K_ab, ∂_u] = [K_ab, ∂_v] = 0. Then K_ab(A(V₁, …)) = (ℒ_(K_ab)A)(V₁, …) + Σ_i A(…, [K_ab, V_i], …). The last
statement holds as W_a does not depend on (u, v). The formula for 𝔴 uses du(E₀) = c/|T|, dv(E₀) = 1/|T|, E₀ − (c ∂_u +
∂_v)/|T| = c b̂ ∂_x/|T|, |∂_x|²_(γ₀) = 1/(4(1 − x²)), the same for E₁ with −c, and Σ_j |f_j|²_(γ₀) = tr_(γ̂) γ₀; those
for 𝔳 use [[eq:tl5-hf-null-pair]], |∂_x| = e^ζ and Σ_a |W_a|² = tr_(γ₀) γ̂, with the ratios of the proof of
[[lem:tl5-hf-fields]] (a). ∎

**Lemma {#lem:tl5-hf-sobolev}** (A Sobolev inequality on the future faces.) Let p ∈ D^κ, a := τ₁(p), b := τ₂(p), and let
A be a C¹ symmetric 2-tensor field on Q(a, b), with ℒ_(K)A and ℒ_(K′)ℒ_K A of class C¹ for all rotations K, K′, and
let S_a := {a} × {1/2} × S³, the leaf of N₀ in which the face Σ₁(a, b) begins. Then, with ε₁ the face density
[[eq:tl5-hf-faces]] and the sums over words J of length at most two in the six rotations,

    |A(p)|² ≤ C_S(p)² Σ_(|J|≤2) ∫_(Σ₁(a,b)) ε₁[ℒ^J A] dμ dτ₂ + C_(S,0)(p)² Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω,
    C_S(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(Σ₁(a,b)) 𝔳⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),                 {#eq:tl5-hf-cs}
    C_(S,0)(p)² := 6 C_(S³)² 𝔭₂ 𝔴(p)⁴ sup_(S_a) 𝔳⁴;

the last term is zero if A = 0 on N₀ ∩ Q(a, b).

where 𝔭₂ := 2353, ∂_γ := ∂_v − κ′ ∂_u, |D̂∂_γ| is the norm of the (1, 1)-tensor D̂∂_γ, and 𝔨₁ := 3 max(1, κ′/c, κ′² b̂²
e^(2ζ)/((c + κ′) Ω̂²)).

*Proof.* For ω ∈ S³ let γ_ω(v) := (a − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_p; its (u, v)-image is the face Σ₁(a, b) in the
(u, v)-plane, from N₀ to p, since dτ₂/dv = 1 − κκ′ > 0 along it, and its velocity is ∂_γ. For a function f on Q(a, b) put
𝔈(f)(v) := ∫_(S³) (f² + Σ(K f)² + Σ(K′K f)²)(γ_ω(v)) dω. By [[lem:tl5-hf-components]] and [[lem:tl5-hf-sphere]], |A(p)|²
≤ 𝔴(p)⁴ |A(p)|²_e ≤ 6C_(S³)² 𝔴(p)⁴ Σ 𝔈(A_(VV′))(v_p), the sum over the 36 components. Here 𝔈(A_(VV′))(v_p) =
𝔈(A_(VV′))(1/2) + ∫ ∂_v 𝔈 dv ≤ 𝔈(A_(VV′))(1/2) + ∫_(1/2)^(v_p) (𝔈(A_(VV′)) + 𝔈(∂_γ A_(VV′))) dv, by 2|f ∂_γ f| ≤ f² +
(∂_γ f)²; here ∂_γ commutes with the K and with the index actions, so ∂_γ(K′K A_(VV′)) = K′K((ℒ_(∂_γ)A)_(VV′)).
By [[lem:tl5-hf-components]] with r = 2, |K(B_e)| ≤ |(ℒ_K B)_e| + 2|B_e| and |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K B)_e| + 2|(ℒ_K
B)_e| + 2|(ℒ_(K′)B)_e| + 4|B_e|; squaring with (x + y + z + w)² ≤ 4(x² + y² + z² + w²) and summing over the six K and the
36 pairs gives Σ_(VV′) 𝔈-integrand of B_(VV′) ≤ 𝔭₂ Σ_(|J|≤2) |ℒ^J B|²_e, with 𝔭₂ = 1 + 12·4 + 144·16. Apply this to B = A
and to B = ℒ_(∂_γ)A, using ℒ_(∂_γ) ℒ^J = ℒ^J ℒ_(∂_γ), |B|_e ≤ 𝔳² |B|, and ℒ_(∂_γ)B = D̂_(∂_γ)B + B(D̂∂_γ ·, ·) + B(·,
D̂∂_γ ·), so that |B|² + |ℒ_(∂_γ)B|² ≤ (1 + 8|D̂∂_γ|²)|B|² + 2|D̂_(∂_γ)B|². With ∂_γ = ê₄ − κ′ê₃ + κ′b̂ ∂_x, |D̂_(∂_γ)B|²
≤ 3(cΩ̂²|w₊|² + κ′²(Ω̂²/c)|w₋|² + κ′² b̂² e^(2ζ) |∇̸B|²) ≤ 𝔨₁ (e_o[B] + κ′ e_i[B]), and |B|² ≤ (e_o[B] + κ′ e_i[B])/(2Ω̂²
z̲), by [[lem:tl5-hf-densities]]. Finally dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face, and (e_o + κ′e_i)/(1 − κκ′) = ε₁.
The terms at v = 1/2 are integrals over S_a, and the bound for B = A gives Σ_(VV′) 𝔈(A_(VV′))(1/2) ≤ 𝔭₂ sup_(S_a) 𝔳⁴
Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω; they are zero if A = 0 on N₀ ∩ Q(a, b), as A and its derivatives along N₀ then vanish. ∎

The same proof, with r slots in place of two and 𝔭_r := 1 + 12r² + 144r⁴, gives for a tensor field A of rank r on
Q(a, b)

    |A(p)|² ≤ 6 C_(S³)² 𝔭_r 𝔴(p)^(2r) (Σ_(|J|≤2) ∫_(Σ₁(a,b)) 𝔳^(2r) R⁻³ ((1 + 2r²|D̂∂_γ|²) |ℒ^J A|²
              + 2|∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′)
              + sup_(S_a) 𝔳^(2r) Σ_(|J|≤2) ∫_(S_a) |ℒ^J A|² dω),                                       {#eq:tl5-hf-cs-r}

using |D̂_(∂_γ)B| ≤ |∂_γ| |D̂B| in place of the densities; the last term is zero if A = 0 on N₀ ∩ Q(a, b).

#### The reduced operator and its quadratic part {#sec:tl5-hf-quadratic}

**Lemma {#lem:tl5-hf-reduced}** (The reduced operator about ĝ.) Let g be a C² Lorentzian metric near a point, h := g − ĝ,
H := g⁻¹ − ĝ⁻¹, K_σμν := (1/2)(D̂_μ h_σν + D̂_ν h_σμ − D̂_σ h_μν) and C := g⁻¹K, the tensor C^λ_μν = g^(λσ) K_σμν. Then

    −2 Ric^W(g) = −2 R̂ic + L̂h + N(h),      N(h) := H^(λσ) D̂_λD̂_σ h − 2 𝔠(H) h − 2 𝔮,                   {#eq:tl5-hf-n}

where, with D̂g^(λσ) = −g^(λμ) g^(σν) D̂h_μν and Υ^λ = g^(λσ) g^(μν) K_σμν,

    (𝔠(H)h)_αβ := −(1/2) H^(λσ) (R̂^ρ_βλα h_ρσ + R̂^ρ_σλα h_βρ + R̂^ρ_αλβ h_ρσ + R̂^ρ_σλβ h_αρ + R̂^ρ_λαβ h_ρσ),
    𝔮_αβ := (D̂_λ g^(λσ)) K_σαβ − (1/2) (D̂_β g^(λσ)) D̂_α h_λσ + C^λ_λσ C^σ_αβ − C^λ_βσ C^σ_λα
            − (1/2) ((D̂_β g^(μν)) K_αμν + (D̂_α g^(μν)) K_βμν) + (1/2) (D̂_β h_αλ + D̂_α h_βλ) Υ^λ.

So g solves the reduced equation [[eq:tl5-wg-reduced]] if and only if L̂h = 2R̂ic − N(h). Each term of 2𝔮 is a
contraction of g⁻¹ ⊗ g⁻¹ ⊗ D̂h ⊗ D̂h, and the sum of the absolute values of its coefficients, counted over the monomials
obtained by expanding K, is 16; 2𝔠(H)h is a sum of five contractions of H ⊗ R̂ ⊗ h with coefficient 1.

*Proof.* Since D̂ĝ = 0, D̂g = D̂h, and the difference of the connections is C. The standard formula for the Ricci tensor
of a connection D̂ + C reads Ric(g)_αβ = R̂ic_αβ + D̂_λ C^λ_αβ − D̂_β C^λ_λα + C^λ_λσ C^σ_αβ − C^λ_βσ C^σ_λα, with
C^λ_λα = (1/2) g^(λσ) D̂_α h_λσ. In [[eq:tl5-wg-def]], g_αλ D̂_β Υ^λ = D̂_β 𝒱_α − (D̂_β h_αλ) Υ^λ with 𝒱_α := g_αλ Υ^λ =
g^(μν)(D̂_μ h_αν − (1/2) D̂_α h_μν). Expanding, the terms with two derivatives of h are

    (1/2) g^(λσ) ([D̂_λ, D̂_α] h_βσ + [D̂_λ, D̂_β] h_ασ) − (1/2) g^(λσ) D̂_λD̂_σ h_αβ + (1/4) g^(μν) [D̂_α, D̂_β] h_μν,

by pairing (1/2) g^(λσ) D̂_λD̂_α h_σβ from D̂_λC^λ_αβ with −(1/2) g^(μν) D̂_αD̂_μ h_βν from −(1/2)D̂_α𝒱_β, the same with
α and β exchanged, and −(1/2) g^(λσ) D̂_βD̂_α h_λσ from −D̂_βC^λ_λα with (1/4) g^(μν)(D̂_βD̂_α + D̂_αD̂_β) h_μν from the
gauge term. By the convention of [[lem:tl5-wg-linear]], [D̂_μ, D̂_ν] h_αβ = −R̂^ρ_αμν h_ρβ − R̂^ρ_βμν h_αρ, and the
commutator terms are 𝔠(g⁻¹)h, with g⁻¹ in place of H (the last term of 𝔠 uses the symmetry of g^(μν) and of h). The terms
with products of first derivatives are 𝔮. So Ric^W(g) = R̂ic − (1/2) g^(λσ) D̂_λD̂_σ h + 𝔠(g⁻¹)h + 𝔮. Applied to ĝ + th
and differentiated at t = 0, this gives (d/dt)Ric^W = −(1/2)□̂h + 𝔠(ĝ⁻¹)h, as 𝔮 is quadratic in h; by [[eq:tl5-wg-lin]],
𝔠(ĝ⁻¹)h = −𝓡̂h. Since 𝔠 is linear in its first argument, −2Ric^W(g) = −2R̂ic + □̂h + 2𝓡̂h + H^(λσ)D̂_λD̂_σh − 2𝔠(H)h −
2𝔮. The count: the six groups of 𝔮 contribute 3/2, 1/2, 3/4, 9/4, 3/2 and 3/2, since K is one half of a sum of three
index permutations of D̂h and 𝒱 a sum of two monomials with coefficients 1 and 1/2. ∎

**Definition {#def:tl5-hf-levels}** (Low and high quantities.) Fix N ≥ 5. For a C^(N+2) symmetric 2-tensor field h with
g = ĝ + h Lorentzian, put at each point

    𝔰 := max(|H|, |Ψ_B| (|B| ≤ N − 2), |D̂Ψ_B| (|B| ≤ N − 3), |D̂²Ψ_B| (|B| ≤ N − 4)),
    𝔧 := max(𝔰, |Ψ_B|, |D̂Ψ_B| (|B| ≤ N), |D̂²Ψ_B| (|B| ≤ N − 1)),

the maxima over words B in Γ. The tensors in the first line are the low quantities. Let Λ ≥ 1 be a bound at the point for
the norms of ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z], D̂ℒ^B Γ′[π^Z] and ℒ^B R̂ for all words B with |B| ≤ N and all Z ∈ Γ,
and put 𝔤₀ := √5 + 1/4 and, with the ordered Bell numbers F₀ = F₁ = 1, F₂ = 3, F₃ = 13, F₄ = 75, F₅ = 541, F_k = Σ_(r) r!
S(k, r) in general,

    β₁(k) := 1 + (2^(k+1) − 2) Λ,      β₂(k) := 1 + (7/3)(4^k − 1) Λ²,
    b_g(0) := 𝔤₀,   b_g(k) := F_k 𝔤₀^(k+1) (Λ + 1)^k,   b_H(0) := 1,   b_H(k) := (2k + 1) F_k 𝔤₀^(k+1) (Λ + 1)^k,
    𝔠_n := β₂(n) − 1 + Σ_(k=1)^n C(n, k) b_H(k) β₂(n − k) + 5Λ Σ_(k=0)^n C(n, k) 2^(n−k) b_H(k)
           + 16 Σ_(k₁+k₂+k₃+k₄=n) (n!/(k₁! k₂! k₃! k₄!)) b_g(k₁) b_g(k₂) β₁(k₃) β₁(k₄),                   {#eq:tl5-hf-cn}

C(n, k) the binomial coefficients and k ≥ 1 where not stated.

**Lemma {#lem:tl5-hf-quadratic}** (The quadratic terms.) Let N ≥ 5, h as in [[def:tl5-hf-levels]], and p a point with
𝔰(p) ≤ 1/8. Then for every word I with |I| ≤ N,

    |ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I| ≤ 𝔠_(|I|) 𝔰 𝔧   at p.                                                 {#eq:tl5-hf-g}

*Proof.* As |h| ≤ 𝔰 ≤ 1/8, |H| ≤ 1/4 by [[lem:tl5-wg-norms]] (a), whose proof applies to the norm |·| as it uses only a
ĝ-orthonormal frame; so |g⁻¹| ≤ |ĝ⁻¹| + |H| ≤ 𝔤₀. Lie derivatives commute with contractions and obey Leibniz's rule, so
ℒ^I of a contraction of m factors is the sum, over the assignments of the letters of I to the factors with the order
kept, of the contractions of the Lie derivatives of the factors; there are n!/(k₁! ⋯ k_m!) assignments with k_i letters
on the i-th factor, n := |I|. A full contraction of tensors is bounded by the product of their norms. Expand each Lie
derivative of a factor as follows; a monomial is a contraction of background factors and of solution factors, the latter
among H, Ψ_B, D̂Ψ_B and D̂²Ψ_B.

(i) ℒ^J h = Ψ_J and ℒ^J R̂, of norm at most Λ.

(ii) ℒ^J D̂h = D̂Ψ_J + R′_J, where by [[eq:tl5-hf-lie-d]] R′_(ZJ) = ℒ_Z R′_J − Γ′[π^Z] ⋆ Ψ_J: each monomial of R′_J has
one coefficient ℒ^B Γ′[π^Z] and one solution factor Ψ_B, |B| < |J|, and their number m′_k (k := |J|) satisfies m′_k ≤
2m′_(k−1) + 2, m′₀ = 0; so ℒ^J D̂h is a sum of monomials with background norms of total at most β₁(k).

(iii) ℒ^J D̂²h = D̂²Ψ_J + R_J with R_(ZJ) = ℒ_Z R_J + [ℒ_Z, D̂²]Ψ_J and [ℒ_Z, D̂²]Ψ = −Γ′ ⋆ D̂Ψ − (D̂Γ′) ⋆ Ψ − Γ′ ⋆̃ D̂Ψ,
seven monomials, ⋆̃ the contraction in which D̂ falls on Ψ inside D̂(Γ′ ⋆ Ψ); Lie differentiation of a monomial with
solution factor D̂Ψ_B gives at most four monomials, by ℒ_Z D̂Ψ_B = D̂Ψ_(ZB) − Γ′ ⋆ Ψ_B, and of one with Ψ_B at most
three (two if it has one background factor); so the
number m_k of monomials of R_J satisfies m_k ≤ 4m_(k−1) + 7, m_k ≤ (7/3)(4^k − 1), each with at most two background
factors and one solution factor D̂Ψ_B or Ψ_B with |B| < k.

(iv) ℒ^J g⁻¹ = Σ (−1)^r g⁻¹ (ℒ^(B₁) g) g⁻¹ ⋯ (ℒ^(B_r) g) g⁻¹, the sum over the ordered sequences of r ≥ 1 disjoint
nonempty subwords B_i of J, in the order of J, covering J; this follows by induction from ℒ_Z g⁻¹ = −g⁻¹(ℒ_Z g)g⁻¹, the
new letter either starting a block at one of the r + 1 factors g⁻¹ or joining a block, so that there are r! S(k, r) terms
with r blocks, F_k in all. Here ℒ^B g = ℒ^B ĝ + Ψ_B with ℒ^B ĝ = ℒ^(B′) π^(Z) for B = (B′, Z), of norm at most Λ. So ℒ^J
g⁻¹ is a sum of monomials of total background norm at most b_g(k). For ℒ^J H = ℒ^J g⁻¹ − ℒ^J ĝ⁻¹, write each difference
of products of 2r + 1 factors as a telescoping sum of 2r + 1 terms, each with one difference factor H or Ψ_(B_i) and the
other factors among g⁻¹, ĝ⁻¹, ℒ^B g and ℒ^B ĝ; every monomial of ℒ^J H then contains a solution factor, and the total
background norm is at most b_H(k), |ĝ⁻¹| = √5 ≤ 𝔤₀.

By [[lem:tl5-hf-reduced]], with these expansions, ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I is a sum of monomials whose total
background norm, with the coefficients, is at most 𝔠_n: the first two terms of [[eq:tl5-hf-cn]] come from
H^(λσ)D̂_λD̂_σh, the term D̂²Ψ_I with all letters on D̂²h being the one subtracted; the third from the five terms of
2𝔠(H)h, the letters distributed over H, R̂ and h; the fourth from 2𝔮.

Every monomial has at least two solution factors, since each term of N(h) has two (H and D̂²h, H and h, D̂h and D̂h) and
each expansion above keeps one in every monomial. Call a solution factor high if it is not a low quantity: Ψ_B with |B| ≥
N − 1, D̂Ψ_B with |B| ≥ N − 2, or D̂²Ψ_B with |B| ≥ N − 3. A monomial has at most one high factor. In the terms from 𝔮
the solution factors are of the forms Ψ_B and D̂Ψ_B, carried by disjoint sets of letters, and two high ones would need at
least 2N − 4 > N letters. In the terms from H^(λσ)D̂_λD̂_σh the factors of the expansion of H are of the form H or Ψ_B,
those of D̂²h of the form D̂²Ψ_B, D̂Ψ_B or Ψ_B, one of them, and two high factors would need at least (N − 1) + (N − 3) >
N letters. In the terms from 𝔠, both are of the form H or Ψ_B, and 2(N − 1) > N. So each monomial is bounded by its
background norm times 𝔰^(q−1) 𝔧, q ≥ 2 the number of its solution factors, the high one or any one of them bounded by 𝔧
and the others by 𝔰; and 𝔰^(q−1) ≤ 𝔰. ∎

**Lemma {#lem:tl5-hf-linfty}** (The low quantities at a point.) Let N ≥ 5, g a solution of the reduced problem on D^κ_s
and h := g − ĝ. For p ∈ D^κ_s put a := τ₁(p), b := τ₂(p), let ℰ⁰_N(p) := Σ_(|I|≤N) ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂, the
unweighted face energy of all words of length at most N, ϱ(p) := sup over Q(a, b) of max_(|J|≤N−1) |ℒ^J(2R̂ic)|, and
η₀(p) := sup over N₀ ∩ Q(a, b) of max(𝔰, |Ψ_C| (|C| ≤ N), |D̂Ψ_C| (|C| ≤ N − 1)), a bound for derivatives of h of order
at most N on N₀. At points of D^κ_s let

    𝒥₁ := (Σ_(|C|≤N) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),   M₂ := max_(|C|≤N−1) |D̂²Ψ_C|,   𝔯₀ := (8/3)‖𝓡̂‖ + √2 ‖𝒞_(·1)‖,
    α_𝔄 := √2 max_(|C|≤N−1) Σ_J ‖𝔄_CJ‖,   q₁ := max_(|C|≤N−1) Σ_J ‖𝔔_CJ‖,
    k₁ := (6/5) ((√3 + 8/3) K_rec (1 + √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + 𝔯₀ + (4/3) α_𝔄),   k₂ := (8/5) q₁,
    k₃ := (8/5) max_(|C|≤N−1) (𝔠_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠_(|J|) + 1)),

with the maps of [[def:tl5-hf-coupling]], their operator norms ‖·‖ taken with the norm (|D̂Ψ|² + |Ψ|²)^(1/2) on the jets,
and 𝔠_n of [[eq:tl5-hf-cn]], and 𝔨₂ := (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²). If 𝔰 ≤ 𝔰₀
:= min(1/8, 1/(2 sup_(Q(a,b)) k₃)) on Q(a, b), then

    𝔰(p) ≤ C_∞(p) ℰ⁰_N(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀(p),                              {#eq:tl5-hf-linfty}

with 𝔐 := Σ_(j≤N−3) 7^j the number of words of length at most N − 3, C_∞ := 2 max(2C_S, C₁, k₁(p) (2𝔐)^(1/2) max(C_S,
C₁)), C_(∞,ϱ) := 2 max(C_(1,ϱ), k₁(p) (2𝔐)^(1/2) C_(1,ϱ) + k₂(p)), C_(∞,0) := 2 max(2C_(0,0), C_(1,0), k₁(p) (2𝔐)^(1/2)
max(C_(0,0), C_(1,0))), C_S and C_(S,0) of [[eq:tl5-hf-cs]], S_a as in [[lem:tl5-hf-sobolev]], and

    C₁² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ)² + 4|∂_γ|² (72Λ² + 8(k₁ + 1)²)),
    C_(1,ϱ)² := 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 32 |∂_γ|² k₂²) · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),
    C_(0,0)² := 86π² C_(S,0)(p)²,      C_(1,0)² := 516π² C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ)².

*Proof.* By [[thm:tl5-wg]] (F4_W) g is vacuum, so by [[lem:tl5-hf-reduced]] L̂h = 2R̂ic − N(h); with 𝔤 := L̂h,
[[def:tl5-hf-coupling]] gives at every point, for |C| ≤ N − 1, L̂Ψ_C + H^(αβ)D̂_αD̂_βΨ_C = Σ_J 𝔄_CJ(D̂Ψ_J, Ψ_J) + Σ_J
𝔔_CJ ℒ^J(2R̂ic) − Σ_(J≠C) 𝔔_CJ ℒ^J N(h) − (ℒ^C N(h) − H^(αβ)D̂_αD̂_βΨ_C).

*Second derivatives.* At a point of Q(a, b) apply [[lem:tl5-hf-recovery]] to Ψ_C, |C| ≤ N − 1, with the tensor H of the
solution, |H| ≤ 𝔰₀ ≤ 1/8, so 1 − (4/3)|H| ≥ 5/6. There (Σ_Z |D̂ℒ_ZΨ_C|²)^(1/2) ≤ 𝒥₁ and (Σ_Z 𝔷_Z²)^(1/2) ≤ √7 (3
max|D̂Z| + 2 max|D̂²Z|) 𝒥₁, as Γ has seven fields; |D̂Ψ_J| + |Ψ_J| ≤ √2 𝒥₁; and by [[lem:tl5-hf-quadratic]] |ℒ^J N(h)|
≤ |H| |D̂²Ψ_J| + 𝔠_(|J|) 𝔰𝔧 ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ N − 1, with 𝔧 ≤ 2𝒥₁ + M₂, as |H| ≤ 2|h| by
[[lem:tl5-wg-norms]] (a). Hence M₂ ≤ k₁ 𝒥₁ + k₂ |ℒ^(≤N−1)(2R̂ic)| + k₃ 𝔰 (2𝒥₁ + M₂), and with k₃𝔰 ≤ 1/2,

    M₂ ≤ 2(k₁ + 1) 𝒥₁ + 2k₂ max_(|J|≤N−1) |ℒ^J(2R̂ic)|.

*Zeroth order.* [[lem:tl5-hf-sobolev]] for A := Ψ_B, |B| ≤ N − 2, gives |Ψ_B(p)| ≤ C_S(p) ℰ⁰_N(p)^(1/2) + C_(0,0)
η₀(p), since ℒ^J Ψ_B = Ψ_(JB), the words JB are distinct for distinct J, there are 43 words J and ∫_(S_a) dω = 2π²,
and the bound |H(p)| ≤ 2|h(p)| holds by [[lem:tl5-wg-norms]] (a).

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] with r = 3 to A := D̂Ψ_B. For a word J of rotations, |J| ≤ 2, ℒ^J
D̂Ψ_B = D̂Ψ_(JB) + R′, with at most six monomials in R′ by the proof of [[lem:tl5-hf-quadratic]] (ii), each a contraction
of one coefficient of norm at most Λ with a Ψ_C; so |ℒ^J A| ≤ (1 + 6Λ) 𝒥₁, and, with Λ bounding also the derivatives
D̂ℒ^B Γ′[π^Z], |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁, as |JB| ≤ N − 1. There are 43 words J. On the face, by [[eq:tl5-hf-coercive]]
and [[lem:tl5-hf-densities]], |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]), so ∫ 𝒥₁² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ⁰_N(p)
on Σ₁(a, b); inserting the bound for M₂, with (x + y)² ≤ 2x² + 2y², and bounding the term on S_a by |ℒ^J A| ≤ (1 + 6Λ)
η₀(p) there, gives |D̂Ψ_B(p)| ≤ C₁ ℰ⁰_N(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p).

*Second order at low levels.* For |B| ≤ N − 4 every solution factor of every monomial of ℒ^B N(h) is low, so the proof of
[[lem:tl5-hf-quadratic]] gives |ℒ^B N(h)| ≤ (𝔠_(|B|) + 1) 𝔰², and the argument above at p, with every term of 𝒥₁ replaced
by L := (Σ_(|C|≤N−3) (|Ψ_C|² + |D̂Ψ_C|²))^(1/2) ≤ (2𝔐)^(1/2) (max(C_S, C₁) ℰ⁰_N^(1/2) + C_(1,ϱ) ϱ + max(C_(0,0),
C_(1,0)) η₀), as all words involved
have length at most N − 3, gives |D̂²Ψ_B(p)| ≤ k₁ L + k₂ ϱ + k₃ 𝔰(p)²; as k₃ 𝔰(p) ≤ 1/2, the last term is at most 𝔰(p)/2.
Taking the maximum of the four bounds and absorbing 𝔰(p)/2 gives [[eq:tl5-hf-linfty]]. ∎

**Lemma {#lem:tl5-hf-quasilinear}** (The quasilinear term.) Let H be a C¹ symmetric tensor field of type (2, 0) and Ψ a
C² symmetric 2-tensor field on Q(a, b), and put

    𝔟[Ψ]^α := H^(αβ) ⟨D̂_βΨ, D̂_TΨ⟩ − (1/2) T^α H^(βγ) ⟨D̂_βΨ, D̂_γΨ⟩.

(a) div 𝔟 = H^(αβ) ⟨D̂_αD̂_βΨ, D̂_TΨ⟩ + 𝔮_H[Ψ], where, with |D̂Ψ|² := Σ_M |D̂_(F_M)Ψ|², 𝔡 := max {|𝔇_V(A, B)|
: |V| = |A| = |B| = 1} and ‖𝒞_(·0)‖ the norm of Ψ ↦ (𝒞(F_M, E₀)Ψ)_M,

    |𝔮_H[Ψ]| ≤ ϰ_H |D̂Ψ|² + |H| |T| ‖𝒞_(·0)‖ |Ψ| |D̂Ψ|,
    ϰ_H := (√5 + 1/2) |T| |D̂H| + |H| (|D̂T| + (1/2)|div T| + (√5 + 1/2) 𝔡 |T|).                          {#eq:tl5-hf-qh}

(b) 2Ω̂² |dτ₁(𝔟)| ≤ θ_H (e_o[Ψ] + κ′ e_i[Ψ]) and 2Ω̂² |dτ₂(𝔟)| ≤ θ_H (e_i[Ψ] + κ e_o[Ψ]), where

    θ_H := (√2 + 1/2) |H| max((c + κ′)/min(c, κ′), (1 + κc)/(κc)).                                     {#eq:tl5-hf-theta}

*Proof.* (a) By [[eq:tl5-hf-dk]], D̂_α(H^(αβ)⟨D̂_βΨ, D̂_TΨ⟩) = (D̂_αH^(αβ))⟨D̂_βΨ, D̂_TΨ⟩ + H^(αβ)⟨D̂_αD̂_βΨ, D̂_TΨ⟩ +
H^(αβ)⟨D̂_βΨ, (D̂_αT)^δ D̂_δΨ + T^δ D̂_αD̂_δΨ⟩ + H^(αβ) 𝔇_(∂_α)(D̂_βΨ, D̂_TΨ), and (1/2) D̂_α(T^α H^(βγ)⟨D̂_βΨ, D̂_γΨ⟩) =
(1/2)(div T) H^(βγ)⟨·,·⟩ + (1/2)(D̂_T H^(βγ))⟨D̂_βΨ, D̂_γΨ⟩ + H^(βγ)⟨T^δ D̂_δD̂_βΨ, D̂_γΨ⟩ + (1/2) H^(βγ) 𝔇_T(D̂_βΨ,
D̂_γΨ). The two terms with T^δ and two derivatives of Ψ differ by H^(αβ) T^δ ⟨D̂_βΨ, 𝒞_αδ Ψ⟩. So 𝔮_H is the sum of the
six remaining terms and of this one. Bounding each: a contraction of different tensors by the product of their norms,
the trace
D̂_αH^(αβ) by √5 |D̂H|, |D̂_TΨ| ≤ |T| |D̂Ψ|, and |Σ_(A,B) H^AB 𝔇_A(D̂_BΨ, X)| ≤ |H| √5 𝔡 |D̂Ψ| |X|, with T^δ 𝒞_αδ = |T|
𝒞(·, E₀), gives [[eq:tl5-hf-qh]].

(b) The covectors du and dv have the k-norms |du| = √2 c/|T| = √c/(√2 Ω̂) and |dv| = √2/|T| = 1/(√2 √c Ω̂), since
du(E₀) = −du(E₁) = c/|T|, dv(E₀) = dv(E₁) = 1/|T| and both vanish on the leaves; and dτ₁(T) = c + κ′, dτ₂(T) = 1 + κc.
Hence |dτ₁| |T| ≤ √2 (c + κ′), |dτ₂| |T| ≤ √2 (1 + κc), and

    |dτ₁(𝔟)| ≤ |H| (|dτ₁| |T| + (c + κ′)/2) |D̂Ψ|² ≤ (√2 + 1/2) (c + κ′) |H| |D̂Ψ|²,

and likewise |dτ₂(𝔟)| ≤ (√2 + 1/2)(1 + κc) |H| |D̂Ψ|². By [[lem:tl5-hf-densities]], e_o + κ′e_i ≥ cΩ̂²|w₊|² +
κ′Ω̂²|w₋|² + (c + κ′)Ω̂²|∇̸Ψ|² ≥ 2 min(c, κ′) Ω̂² |D̂Ψ|², and e_i + κe_o ≥ 2 min(1, κc) Ω̂² |D̂Ψ|² = 2κc Ω̂² |D̂Ψ|². ∎

**Lemma {#lem:tl5-hf-conversions}** (The norms of the local theory and of the double-null conversion.) Let c_* := c(u*) =
f(−u*)/2, the minimum of c on [−10, u*].

(a) At every point of D̄, |h|_k̂ ≤ |h|/c_* for every symmetric 2-tensor h. So |h| < c_* κ_m/2 at every point of a set X
gives |h|_k̂ < κ_m/2, hence |g⁻¹ − ĝ⁻¹|_k̂ < κ_m on X by [[lem:tl5-wg-norms]] (a): g is tilted on X with the strict
inequality that [[thm:tl5-wg]] (F3_W) requires.

(b) On the slice M_σ of [[def:tl5-dn-slice]], with the coordinates (u, v, ϑ), let ν := max_μ |∂_μ|, Γ̂_s :=
max_(λ,μ) |D̂_(∂_λ) ∂_μ| and Γ̂′_s := max_(κ,λ,μ) |D̂_(∂_κ) D̂_(∂_λ) ∂_μ|, the maxima over μ, λ, κ ∈ {u, v, ϑ}, all norms
those of k. Then for the quantity ε of [[eq:tl5-dn-eps]], for g_σ and ĝ_σ on a set B ∩ M_σ,

    ε ≤ ε_𝔰 · sup_(B ∩ M_σ) max(|h|, |D̂h|, |D̂²h|),
    ε_𝔰 := sup_(B ∩ M_σ) max(ν², ν³ + 2νΓ̂_s, ν⁴ + 5ν²Γ̂_s + 2νΓ̂′_s + 2Γ̂_s²),                          {#eq:tl5-hf-eps}

and |∂_u| ≤ √(2/c) Ω̂ + |b̂| e^ζ, |∂_v| = √(2c) Ω̂, |∂_ϑ| = R e^(−(P+Q)), the last since x = cos 2ϑ on M_σ.

*Proof.* (a) is [[lem:tl5-hf-khat]] with r = 2 and c ≥ c_*. (b) The components are h_μν = h(∂_μ, ∂_ν), and ∂_λ(h_μν) =
(D̂_(∂_λ)h)(∂_μ, ∂_ν) + h(D̂_(∂_λ)∂_μ, ∂_ν) + h(∂_μ, D̂_(∂_λ)∂_ν); differentiating once more gives ten terms, the second
derivative D̂²h(∂_κ, ∂_λ, ∂_μ, ∂_ν), five with one derivative of h and one D̂∂, two with D̂D̂∂ and two with two factors
D̂∂; each is bounded by the product of the norms. On M_σ, ∂_ϑ = −2 sin 2ϑ ∂_x and |∂_x| = e^ζ, with e^ζ = R
e^(−(P+Q))/(2(1 − x²)^(1/2)) by [[eq:tl5-radii]]. ∎

#### The weighted bootstrap {#sec:tl5-hf-bootstrap}

**Definition {#def:tl5-hf-norm}** (The weighted norm.) Fix N ≥ 5, μ ∈ (0, 1], weights z, z̲, admissible rates a_o, a_i
for (𝔅_N, E_o^N, E_i^N) and φ as in [[prop:tl5-hf-linear]]. For a solution g of the reduced problem on D^κ_s, with h := g
− ĝ, and σ ∈ [1/2, s] put

    Y_σ(g)² := sup {Σ_(|I|≤N) μ^|I| ℰ_I(a, b) : −10 ≤ a ≤ u*, 1/2 ≤ b ≤ σ},
    ℰ_I(a, b) := ∫_(Σ₁(a,b)) e^(−φ) ε₁[Ψ_I] dμ dτ₂ + ∫_(Σ₂(a,b)) e^(−φ) ε₂[Ψ_I] dμ dτ₁.

Since Q(a, b) ⊂ D^κ_σ for a ≤ u* and b ≤ σ, Y_σ(g) depends only on the restriction of g to D^κ_σ. It is continuous in σ:
(a, b) ↦ ℰ_I(a, b) is continuous, the faces depending continuously on (a, b) and the integrands being continuous, and the
supremum of a continuous function over [−10, u*] × [1/2, σ] is continuous in σ. And Y_(1/2)(g) = 0, as D^κ_(1/2) is the
sphere S and its faces have measure zero.

**Definition {#def:tl5-hf-constants}** (The constants of the bootstrap.) In the setting of [[def:tl5-hf-norm]], let G^♯
be data in the wave gauge, and on N = N₀ ∪ N₁ let Ψ_I := ℒ^I(G^♯ − ĝ) and H := (G^♯)⁻¹ − ĝ⁻¹, computed from the
derivatives of G^♯ on N. Put, with s_N of [[eq:tl5-hf-sn]], ϱ and η₀ the functions of [[lem:tl5-hf-linfty]] for p with
τ₁(p) = u*, τ₂(p) = v*, and the constants of [[lem:tl5-hf-linfty]] and [[lem:tl5-hf-quasilinear]],

    δ_w² := Σ_(|I|≤N) μ^|I| (∫_(N₁) e^(−φ) (e_o[Ψ_I] + 2Ω̂² |du(𝔟[Ψ_I])|) dμ dv
              + ∫_(N₀) e^(−φ) (e_i[Ψ_I] + 2Ω̂² |dv(𝔟[Ψ_I])|) dμ du),
    ε_w := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_N k₂ ϱ]   (the quantity [[eq:tl5-hf-source]] for a = u*, b = v*),
    𝔤_N := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠_(j′) + 1))²)^(1/2),
    ϰ₀ := (√5 + 1/2) |T| 𝔤₀² + |D̂T| + (1/2)|div T| + (√5 + 1/2) 𝔡 |T|,
    𝔞_o := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c) + 2Ω̂ 𝔤_N (2k₁ + 4) μ^(−N/2) (1 + 1/z̲ + 1/c)^(1/2),
    𝔞_i := ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖ + 2Ω̂ 𝔤_N (2k₁ + 4) μ^(−N/2) (1 + 1/z̲ + 1/c)^(1/2),
    S_F := μ^(−N/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_o C_∞ e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_i C_∞ e^(φ/2)) dt),
    𝔯_w := ∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_o (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_i (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt,
    A_w := √2 δ_w + 2ε_w,      B_w := 2 S_F,

where C_∞, C_(∞,ϱ), C_(∞,0), k₁, k₂ are evaluated at the point of the supremum, and, for a fixed ϑ ∈ (0, 1/4],

    𝔰₀ := min(1/8, 1/(2 sup_(D^κ) k₃)),   𝔰_θ := ϑ ((√2 + 1/2) sup_(D^κ) max((c + κ′)/min(c, κ′), (1 + κc)/(κc)))⁻¹,
    𝔰₁ := min(𝔰₀/2, c_* κ_m/2, 𝔰_θ),
    𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−N/2) e^(φ(p)/2) A_w + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).

**Proposition {#prop:tl5-hf-bootstrap}** (The a priori estimate.) In the setting of [[def:tl5-hf-constants]], suppose
that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N), and that

    𝔯_w ≤ 1/4,      η₀ < 𝔰₁,      𝔰_* < 𝔰₁.                                                       {#eq:tl5-hf-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_w for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_* on D^κ_s; in
particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_w + B_w Y_s(g)².                                                                           {#eq:tl5-hf-h1}

*Proof.* By [[thm:tl5-wg]] (F4_W), g is vacuum and has on N ∩ D^κ_s the derivatives of all orders of G^♯; so the
quantities of [[def:tl5-hf-constants]] on N are those of g. In particular 𝔰 ≤ η₀ < 𝔰₁ on N₀ ∩ D^κ_s.

*Step 1: the low quantities.* Let Σ_* be the set of σ ∈ [1/2, s] with 𝔰 ≤ 𝔰₀ on D^κ_σ. It contains 1/2, as D^κ_(1/2) = S
⊂ N₀, and it is closed, 𝔰 being continuous. If σ ∈ Σ_* and p ∈ D^κ_σ, then Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, and
[[lem:tl5-hf-linfty]] applies at p. On the face Σ₁(τ₁(p), τ₂(p)), φ ≤ φ(p), so ℰ⁰_N(p) ≤ μ^(−N) e^(φ(p)) Y_σ(g)² ≤
4μ^(−N) e^(φ(p)) A_w², and 𝔰(p) ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2. By the uniform continuity of 𝔰 on D^κ_s, 𝔰 < 𝔰₀ on a neighbourhood of
D^κ_σ in D^κ_s, which contains D^κ_(σ′) for some σ′ > σ (unless σ = s), as the compact sets D^κ_(σ′) decrease to D^κ_σ.
So Σ_* = [1/2, s], and 𝔰 ≤ 𝔰_* on D^κ_s. Then |h| ≤ 𝔰 < c_* κ_m/2 gives |h|_k̂ < κ_m/2 by [[lem:tl5-hf-conversions]] (a),
and |H| ≤ 𝔰 < 𝔰_θ gives θ_H ≤ ϑ.

*Step 2: the energy identity.* For |I| ≤ N apply [[lem:tl5-hf-identity]] to the current J̃ := J[Ψ_I] − 𝔟[Ψ_I], with H the
tensor of g; the identity holds for J̃, its proof using only that J̃ is a C¹ vector field. By (b) of
[[lem:tl5-hf-quasilinear]], its face densities are at least (1 − ϑ) ≥ 3/4 times ε₁[Ψ_I] and ε₂[Ψ_I]; on N₁ and on N₀
they are at most e_o[Ψ_I] + 2Ω̂²|du(𝔟)| and e_i[Ψ_I] + 2Ω̂²|dv(𝔟)|. By [[lem:tl5-hf-divergence]] and (a) of
[[lem:tl5-hf-quasilinear]], div J̃ = −⟨L̂Ψ_I + H^(αβ)D̂_αD̂_βΨ_I, D̂_TΨ_I⟩ + ℬ[Ψ_I] − 𝔮_H[Ψ_I]. By
[[def:tl5-hf-coupling]] with 𝔤 = 2R̂ic − N(h),

    L̂Ψ_I + H^(αβ)D̂_αD̂_βΨ_I = Σ_J 𝔄_IJ(D̂Ψ_J, Ψ_J) + Σ_J 𝔔_IJ ℒ^J(2R̂ic) − Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑_I,

with 𝔑_I := ℒ^I N(h) − H^(αβ)D̂_αD̂_βΨ_I. The first two sums are treated as in the proof of [[prop:tl5-hf-linear-n]],
with the weights μ^|I|: their bulk, with that of the terms ℬ, is at most ñᵀ𝔅_N ñ plus the forcing term 2Ω̂²
s_N[2R̂ic](√e_o + √c √e_i). The weight contributes −2Ω̂² dφ(J̃), and by (b) of [[lem:tl5-hf-quasilinear]], 2Ω̂² |dφ(𝔟)| ≤
ϑ((a_o + κa_i) e_o + (a_i + κ′a_o) e_i); so by the admissibility for (1 − ϑ)⁻¹𝔅_N, ñᵀ𝔅_N ñ − 2Ω̂² dφ(J̃) ≤ 0. By
[[lem:tl5-hf-quadratic]] and |H| ≤ 𝔰, |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ N − 1 and |𝔑_I| ≤ 𝔠_(|I|) 𝔰 𝔧; so the
third and fourth terms, summed as in [[eq:tl5-hf-sn]], contribute at most 2Ω̂² 𝔤_N 𝔰 𝔧 (√e_o + √c √e_i), the factor
7^(j′/2) counting the words of length j′. By the proof of [[lem:tl5-hf-linfty]] and |H| ≤ 2|h|, 𝔧 ≤ 2𝒥₁ + M₂ ≤ (2k₁ + 4)
𝒥₁ + 2k₂ ϱ, and by [[eq:tl5-hf-coercive]], with e_o and e_i the weighted sums, 𝒥₁² ≤ μ^(−N) ((1/z̲ + 1/c) e_o +
e_i)/(2Ω̂²); with √e_o + √c √e_i ≤ √2 (e_o + e_i)^(1/2), 2Ω̂² 𝒥₁ (√e_o + √c √e_i) ≤ 2Ω̂ μ^(−N/2) (1 + 1/z̲ + 1/c)^(1/2)
(e_o + e_i). Likewise, by (a) of [[lem:tl5-hf-quasilinear]] with |D̂H| = |g⁻¹(D̂h)g⁻¹| ≤ 𝔤₀² 𝔰 and |D̂Ψ|² ≤ (e_o/c +
e_i)/(2Ω̂²) for each field, the weighted sum of 2Ω̂²|𝔮_H| is at most 𝔰 times the first two terms of 𝔞_o e_o + 𝔞_i e_i.
Hence the bulk of the weighted sum over I is at most

    ∫ e^(−φ) (2Ω̂² (s_N[2R̂ic] + (1/4) 𝔤_N k₂ ϱ)(√e_o + √c √e_i) + 𝔰 (𝔞_o e_o + 𝔞_i e_i)) dμ du dv,

using 2𝔤_N k₂ 𝔰 ϱ ≤ (1/4)𝔤_N k₂ ϱ.

*Step 3: the inequality.* The first term is bounded as in [[prop:tl5-hf-linear]] by Y_s ε_w. For the second, foliate by
the faces Σ₁(t, b′) and Σ₂(a′, t): with e_o/(1 − κκ′) ≤ ε₁ and du dv = dτ₁ dτ₂/(1 − κκ′), ∫ e^(−φ) 𝔰 𝔞_o e_o ≤ ∫ dt
sup_(Σ₁(t,v*)) (𝔰 𝔞_o) Y_s², and likewise for the ingoing term. By Step 1 and [[lem:tl5-hf-linfty]], 𝔰 ≤ C_∞ μ^(−N/2)
e^(φ/2) Y_s + C_(∞,ϱ) ϱ + C_(∞,0) η₀ at every point. So for every a′ ≤ u*, b′ ≤ s,

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s ε_w + 𝔯_w Y_s² + S_F Y_s³,

and taking the supremum, with ϑ ≤ 1/4 and 𝔯_w ≤ 1/4, Y_s² ≤ 2δ_w² + 2Y_s ε_w + 2S_F Y_s³. If Y_s ≥ √2 δ_w this gives Y_s
≤ 2δ_w²/Y_s + 2ε_w + 2S_F Y_s² ≤ √2 δ_w + 2ε_w + 2S_F Y_s², and otherwise the same holds trivially. ∎

The factor F of the linear estimate enters A_w B_w only through e^(φ/2) in S_F, that is linearly: the nonlinear error
made at a point is amplified from there to the future boundary, and the weight e^(−φ) records that it is quadratic in the
solution at that point, whose size is e^(φ/2) Y there.

**Lemma {#lem:tl5-hf-persistence}** (Persistence of regularity.) Suppose the hypotheses of [[prop:tl5-hf-bootstrap]] hold
with N ≥ 6. For every k ≥ 0 there is C_k, depending only on k, ĝ, G^♯, κ, κ′, μ, the rates and A_w, such that every
solution g of the reduced problem on a D^κ_s with Y_σ(g) ≤ 2A_w for all σ ∈ [1/2, s] has its components and their partial
derivatives of order at most k, and the components of g⁻¹, bounded by C_k on D^κ_s, in the coordinates (u, v, y) of a
fixed finite atlas of S³.

*Proof.* By [[prop:tl5-hf-bootstrap]], 𝔰 ≤ 𝔰_* on D^κ_s; in particular |H| ≤ 1/8, which bounds g⁻¹ = ĝ⁻¹ + H, and θ_H ≤
ϑ. For m ≥ N let P(m) be the statement: the unweighted energies Σ_(|I|≤m) ℰ⁰_I(a, b) over the words of length at most m
are bounded on the corner regions in D^κ_s by a constant E_m, and the quantities |Ψ_B| (|B| ≤ m − 2), |D̂Ψ_B| (|B| ≤ m −
3) and |D̂²Ψ_B| (|B| ≤ m − 4) by a constant L_m, both depending only on the data listed. P(N) holds: ℰ⁰ ≤ μ^(−N)
e^(Φ_o(u*) + Φ_i(v*)) 4A_w² and 𝔰 ≤ 𝔰_*.

Let m ≥ N + 1 ≥ 7 and assume P(m − 1). In the expansion of ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, |I| ≤ m, of the proof of
[[lem:tl5-hf-quadratic]], call a solution factor known if it is one of the quantities bounded by L_(m−1). A monomial has
at most one factor that is not known: two such would need at least 2(m − 3) > m letters for two factors D̂Ψ_B, (m − 2) +
(m − 4) > m for Ψ_B and D̂²Ψ_B, and more in the other cases. So |ℒ^I N(h) − H^(αβ)D̂_αD̂_βΨ_I| is at most a constant
times the largest of |Ψ_B|, |D̂Ψ_B| (|B| ≤ m) and |D̂²Ψ_B| (|B| ≤ m − 1), and every second derivative D̂²Ψ_B, |B| ≤ m −
1, appears there only with |B| < |I| or as the subtracted term. Applying [[lem:tl5-hf-recovery]], with the tensor H of g,
to D̂²Ψ_B in order of increasing |B| bounds each of them by a constant times 𝒥₁^(m) + ϱ, with 𝒥₁^(m) := (Σ_(|C|≤m)
(|Ψ_C|² + |D̂Ψ_C|²))^(1/2): for |B| = j the nonlinear part of its equation contains second derivatives of words shorter
than j only, besides H^(αβ)D̂_αD̂_βΨ_B, which the lemma absorbs. Hence the nonlinear terms of the identities for J[Ψ_I] −
𝔟[Ψ_I], |I| ≤ m, weights 1, are bounded pointwise by a constant 𝔊 times e_o + e_i plus a constant times
ϱ (√e_o + √c √e_i), the 𝔟-terms as in the proof of [[prop:tl5-hf-bootstrap]]. Choose constant rates admissible for
((1 − ϑ)⁻¹ (𝔅_m + 𝔊 (E_o^m + E_i^m)), E_o^m, E_i^m): they exist by [[lem:tl5-hf-allocation]], all entries being bounded
on D^κ. Steps 2 and 3 of the proof of [[prop:tl5-hf-bootstrap]] with these rates, and the argument of
[[prop:tl5-hf-linear]], then bound the level-m energies by the fluxes through N₁ and N₀, which are fluxes of derivatives
of G^♯ of order at most m + 1 ([[thm:tl5-wg]] (F4_W)), and by the residual; so E_m exists. And the proof of
[[lem:tl5-hf-linfty]] at level m, which uses smallness only to absorb the nonlinear part, now bounded by known factors,
gives L_m, its terms on N₀ being bounded by derivatives of G^♯ on N₀. So P(m) holds for every m.

Finally, every covariant derivative D̂^k Ψ_B, for every k and every word B, is bounded, by induction on k and, for fixed
k, on |B|; for k ≤ 2 this is P(m) for m large. The proof of [[lem:tl5-hf-recovery]] applies verbatim to a tensor field A
of any rank in place of Ψ, with □̂ in place of L̂, 𝓡̂ replaced by 0 and 𝒞 acting on every slot: it bounds |D̂²A| at a
point by |D̂ℒ_Z A| (Z ∈ Γ), |D̂A|, |A| and |□̂A + H^(αβ) D̂_αD̂_β A|. Take A := D̂^(k−2)Ψ_B, k ≥ 3. By
[[eq:tl5-hf-lie-d]], ℒ_Z A is D̂^(k−2)Ψ_(ZB) plus contractions of derivatives of Γ′[π^Z] with D̂^j Ψ_B, j ≤ k − 3;
commuting D̂ with □̂ gives
□̂A = D̂^(k−2) □̂Ψ_B plus contractions of derivatives of R̂ with D̂^j Ψ_B, j ≤ k − 2; and □̂Ψ_B + H^(αβ) D̂_αD̂_β Ψ_B is
given by the equation in the proof of [[lem:tl5-hf-linfty]], whose k − 2 derivatives contain derivatives of order k only
of Ψ_(B′), |B′| < |B|, or in H^(αβ) D̂_αD̂_β A up to terms of lower order. So the induction bounds D̂^k Ψ_B by bounded
quantities. Since ĝ is smooth on the compact set D̄, the components of g = ĝ + h in the charts and their partial
derivatives of order at most k are polynomials in the components of D̂^j h, j ≤ k, with bounded coefficients. ∎

**Theorem {#thm:tl5-hf}** (Existence close to an explicit background.) Let ĝ be a background with u* < −1, κ and κ′ as in
[[def:tl5-wg-domains]], g_N smooth characteristic data in the gauge on N⁺ satisfying the constraints, G^♯ data in the
wave gauge for g_N, N ≥ 6, μ ∈ (0, 1], ϑ ∈ (0, 1/4], z, z̲ and rates a_o, a_i as in [[def:tl5-hf-norm]], and suppose:

(a) the quantity η₀ of [[def:tl5-hf-constants]], computed from the derivatives of G^♯ − ĝ of order at most N on N₀,
satisfies η₀ < 𝔰₁;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N);

(c) the constants of [[def:tl5-hf-constants]] satisfy 𝔯_w ≤ 1/4, 𝔰_* < 𝔰₁ and the closing condition

    4 A_w B_w = 8 (√2 δ_w + 2ε_w) S_F < 1.                                                           {#eq:tl5-hf-closing}

Then there is a solution g of the reduced problem on D^κ, and Y_σ(g) ≤ 2A_w for every σ ∈ [1/2, v*]. It is a G-invariant
vacuum metric in the wave gauge, with |g − ĝ|_k̂ < κ_m/2 and 𝔰 ≤ 𝔰_* on D^κ, and the quantity ε of [[eq:tl5-dn-eps]] for
g_σ and ĝ_σ on B ∩ M_σ, B as in [[thm:tl5-dn]], satisfies ε ≤ ε_𝔰 𝔰_*. If moreover the hypotheses of [[thm:tl5-dn]] hold
for this ε, then the metric g̃ that theorem gives on D′ is a smooth G-invariant vacuum metric of the class in the gauge
of [[sec:cone-constraint]], equal to g_N at every point of N ∩ D′.

*Proof.* If A_w = 0, then R̂ic = 0 on D^κ and G^♯ = ĝ at the points of N, so ĝ is the solution, with Y_σ(ĝ) = 0.
Otherwise apply [[lem:tl5-continuation]] with y_σ := Y_σ, A := A_w and B := B_w. By [[def:tl5-hf-norm]], Y_σ depends only
on the restriction of g to D^κ_σ, is continuous in σ, and Y_(1/2) = 0 ≤ A_w. For a solution g on a D^κ_s with Y_σ(g) ≤
2A_w for all σ, (H1) is [[eq:tl5-hf-h1]] and (H4), |g⁻¹ − ĝ⁻¹|_k̂ < κ_m, follows from |h|_k̂ < κ_m/2
([[prop:tl5-hf-bootstrap]], [[lem:tl5-wg-norms]] (a)); (H2) is [[lem:tl5-hf-persistence]]; and (H3) is
[[eq:tl5-hf-closing]]. So the lemma gives the solution on D^κ with Y_σ ≤ 2A_w, and [[prop:tl5-hf-bootstrap]] with s = v*
gives the bounds on h and 𝔰. By [[thm:tl5-wg]] (F4_W) it is a G-invariant vacuum metric in the wave gauge with the
derivatives of G^♯ on N, so (a)–(c) of [[def:tl5-cip-development]] hold on N ∩ D^κ with ι the inclusion. The bound for ε
is [[eq:tl5-hf-eps]], as |h|, |D̂h| and |D̂²h| are low quantities for N ≥ 4. The last statement is [[thm:tl5-dn]], the
set B of that theorem lying in D^κ by [[lem:tl5-wg-domains]] (d). ∎

The constants of [[thm:tl5-hf]] are explicit in the jets of ĝ of order at most N + 3, in c, z, z̲, κ, κ′, μ and ϑ, and in
the data G^♯ on N: the rates enter through the weight φ, the amplification from the data to each point being e^(φ/2) ≤
e^((Φ_o(u*) + Φ_i(v*))/2), and the closing condition is linear in it. No numerical value of them is used or stated in
this paper: for a given background they are suprema and integrals of explicit functions over D^κ, and establishing the
inequalities (a)–(c) for a background at 10 l5 requires enclosures of those functions, of the residual Ric(ĝ) and of
the data on N, which this paper does not provide. The hypotheses (X) and (T) of [[thm:tl5-wg-data]] that give G^♯, and
those of [[thm:tl5-dn]], are conditions on the background of the same kind. The derivatives of G^♯ − ĝ on N₀ transverse
to N₀ need not vanish, so η₀ and the terms on N₀ in δ_w are small only for a background whose transverse derivatives on
N₀ of order at most N are close to those of G^♯. [[thm:tl5-hfg]] gives the conclusions of [[thm:tl5-hf]] under
sharpened constants: graded background bounds, and μ^(−3/2) in place of the factor μ^(−N) of S_F ([[sec:tl5-hfg]]).

**Remark {#rem:tl5-hf-level}** (The level N.) In the proof of [[lem:tl5-hf-quadratic]] each monomial of ℒ^I N(h) has at
least two solution factors, and all but one of them are bounded at the point; the bounds at a point of
[[lem:tl5-hf-linfty]] reach Ψ_B for |B| ≤ N − 2, D̂Ψ_B for |B| ≤ N − 3 and D̂²Ψ_B for |B| ≤ N − 4: the Sobolev inequality
on S³ uses two rotations, and each further derivative transverse to the leaves is recovered from one more commutation.
A product D̂Ψ_B D̂Ψ_(B′) with |B| + |B′| = N then has a factor bounded at the point exactly when N ≥ 5, which is the
condition of [[lem:tl5-hf-quadratic]]; at level N + 1, with the bounds of level N only, the same count needs N + 1 ≥ 7,
that is N ≥ 6, which is the condition of [[lem:tl5-hf-persistence]]. These conditions belong to this way of bounding
the products, with one factor at a point and the others in the energies; the estimate (H1) itself needs N ≥ 5, and
N ≥ 6 enters only through the proof of (H2). One requirement does not depend on the method: the passage to the
double-null gauge needs |D̂²h| at every point, the quantity ε of [[eq:tl5-dn-eps]] being a C² distance, bounded through
[[lem:tl5-hf-conversions]] (b). The face energies of level 3 control D̂²h only in H² of the four-dimensional faces, and
H² of a four-dimensional manifold does not embed in L^∞; so they give no bound of |D̂²h| at a point. With another
bound of the products, [[sec:tl5-hf4]] proves the counterpart [[thm:tl5-hf4]] of [[thm:tl5-hf]] at level four, where two
kinds of products have no factor bounded at a point; it bounds them on the faces by a Hölder inequality in mixed norms.

### The a priori estimate at level four {#sec:tl5-hf4}

[[thm:tl5-hf]] is proved at a level N ≥ 6: the energies of h = g − ĝ are commuted with the seven fields of Γ up to
order N. This section proves its counterpart at level four, with N := 4 throughout. The results of [[sec:tl5-hf]]
up to [[lem:tl5-hf-reduced]], and [[lem:tl5-hf-quasilinear]], [[lem:tl5-hf-conversions]] and [[def:tl5-hf-norm]], do
not depend on the level, and are used here at N = 4 as they stand. [[def:tl5-hf-levels]], [[lem:tl5-hf-quadratic]] and
[[lem:tl5-hf-linfty]] are replaced by [[def:tl5-hf4-levels]], [[lem:tl5-hf4-quadratic]] and [[lem:tl5-hf4-linfty]], and
the proofs of [[prop:tl5-hf-bootstrap]] and [[thm:tl5-hf]] are used with these. What changes is the bound of the
quadratic terms. At level four two kinds of products have no factor bounded at a point ([[lem:tl5-hf4-quadratic]]); on
the future faces they are bounded by a Hölder inequality in mixed norms, the supremum over the leaves against the
supremum along the face ([[lem:tl5-hf4-face]], [[lem:tl5-hf4-mixed]]). The same inequality gives the persistence of
regularity at level four ([[lem:tl5-hf4-persistence]]), and [[thm:tl5-hf4]] collects the results.

#### The products at level four {#sec:tl5-hf4-products}

**Definition {#def:tl5-hf4-levels}** (Level four.) Let N := 4. For a C⁶ symmetric 2-tensor field h with g = ĝ + h
Lorentzian, let 𝔰, 𝔧, Λ and 𝔠_n (n ≤ 4) be given by the formulas of [[def:tl5-hf-levels]] with N = 4:

    𝔰 = max(|H|, |Ψ_B| (|B| ≤ 2), |D̂Ψ_B| (|B| ≤ 1), |D̂²h|),
    𝔧 = max(𝔰, |Ψ_B|, |D̂Ψ_B| (|B| ≤ 4), |D̂²Ψ_B| (|B| ≤ 3)),

Λ ≥ 1 being a bound at the point for the norms of ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z], D̂ℒ^B Γ′[π^Z] and ℒ^B R̂ for
all words B with |B| ≤ 4 and all Z ∈ Γ, and 𝔠_n being given by [[eq:tl5-hf-cn]]. The order of a solution factor H,
Ψ_B, D̂Ψ_B or D̂²Ψ_B is 0, |B|, |B| + 1 or |B| + 2. Put, at each point,

    𝔭_M² := Σ_(|B|=|B′|=2) |D̂Ψ_B|² |D̂Ψ_(B′)|² + Σ_(|B|=3) Σ_(Z∈Γ) |Ψ_B|² |D̂²Ψ_Z|²,                    {#eq:tl5-hf4-pm}

the sums over the words B, B′ in Γ of the lengths shown.

**Lemma {#lem:tl5-hf4-quadratic}** (The quadratic terms at level four.) Let h be a smooth symmetric 2-tensor field with
g = ĝ + h Lorentzian, p a point with |h(p)| ≤ 1/8, and I a word in Γ.

(a) In the expansion of ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I of the proof of [[lem:tl5-hf-quadratic]], every monomial has at
least two solution factors; these carry disjoint sets of the letters of I, and the numbers of derivatives D̂ on them add
up to at most two. So their orders add up to at most |I| + 2, and each of them has order at most |I| + 1.

(b) Let |I| ≤ 4 and 𝔰(p) ≤ 1/8. Then at p

    ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I = 𝔑^L_I + 𝔑^M_I,
    |𝔑^L_I| ≤ 𝔠_(|I|) 𝔰 𝔧,      |𝔑^M_I| ≤ 𝔠_(|I|) 𝔭_M,                                                    {#eq:tl5-hf4-g}

where 𝔑^M_I is the sum of the monomials with at least two high factors, in the sense of the proof below, and 𝔑^L_I the
sum of the others; and 𝔑^M_I = 0 if |I| ≤ 3.

*Proof.* (a) The expansion in the proof of [[lem:tl5-hf-quadratic]] distributes the letters of I over the factors of each
term of N(h), each letter going to one factor, and expands the Lie derivatives of the factors by (i)–(iv) there; it does
not use the level, nor does the statement there that every monomial has at least two solution factors. Each term of N(h)
carries at most two derivatives D̂ on its solution factors (H and D̂²h, H and h, D̂h and D̂h, the factors g⁻¹ carrying
none), and the expansions (i)–(iv) do not increase this number: in (ii) and (iii) the solution factors of the remainders
carry fewer derivatives than D̂h and D̂²h, and in (iv) the solution factors are H and Ψ_B. The order of a factor is the
number of its letters plus the number of its derivatives D̂, which gives the bound |I| + 2 for the sum. A factor of
order |I| + 2 carries all letters and two derivatives, so it is D̂²Ψ_I, which occurs only in H^(αβ) D̂_αD̂_βΨ_I and is
subtracted; so every factor has order at most |I| + 1.

(b) As |h(p)| ≤ 1/8, |H| ≤ 1/4 and |g⁻¹| ≤ 𝔤₀ at p, as in the proof of [[lem:tl5-hf-quadratic]], and the total
background norm of the monomials, with the coefficients, is at most 𝔠_(|I|) by that proof. Call a solution factor high
if it is not a low quantity of [[def:tl5-hf4-levels]]: Ψ_B with |B| ≥ 3, D̂Ψ_B with |B| ≥ 2, or D̂²Ψ_B with |B| ≥ 1. A
monomial with at most one high factor and q solution factors is bounded by its background norm times 𝔰^(q−1) 𝔧 ≤ 𝔰𝔧,
the high factor, or any one, being bounded by 𝔧 and the others by 𝔰 ≤ 1; this gives the bound for 𝔑^L_I. Consider a
monomial with two high factors. In the terms from 2𝔮 the solution factors are of the forms Ψ_B and D̂Ψ_B, and two high
ones carry at least four letters; with four, they are D̂Ψ_B and D̂Ψ_(B′) with |B| = |B′| = 2, as a high factor Ψ_B
carries three. In the terms from H^(λσ)D̂_λD̂_σh the solution factors from the expansion of H are of the forms H and
Ψ_B, high only for |B| ≥ 3, and the one factor from the expansion of D̂²h is of the form D̂²Ψ_B, D̂Ψ_B or Ψ_B, high only
for |B| ≥ 1, 2 or 3; two high factors carry at least four letters, and with four they are Ψ_B with |B| = 3 and D̂²Ψ_Z
with Z ∈ Γ. In the terms from 2𝔠(H)h the solution factors are of the forms H and Ψ_B, and two high ones carry at least
six letters. So 𝔑^M_I = 0 if |I| ≤ 3. If |I| = 4, the two high factors of a monomial of 𝔑^M_I form one of the two pairs
of [[eq:tl5-hf4-pm]] and carry all four letters; its other solution factors carry no letter and, by (a), no derivative,
so they are H or h, bounded by 𝔰 ≤ 1. The product of the two high factors is the square root of one term of 𝔭_M², so
the monomial is bounded by its background norm times 𝔭_M, and summing gives the bound for 𝔑^M_I. ∎

**Lemma {#lem:tl5-hf4-face}** (A Hölder inequality in mixed norms on a face.) Let t ∈ [−10, u*] and b ∈ [1/2, v*] be
such that Σ := Σ₁(t, b) is not empty, and let γ_ω(v) := (t − κ′(v − 1/2), v, ω), 1/2 ≤ v ≤ v_Σ, ω ∈ S³, with v_Σ the
largest value of v on Σ, be the curves of the proof of [[lem:tl5-hf-sobolev]] that fill Σ, with velocity
∂_γ := ∂_v − κ′∂_u, starting on the leaf S_t := {t} × {1/2} × S³ of N₀. Let φ be as in
[[prop:tl5-hf-linear]]. For a tensor field A on Q(t, b), with A_e as in [[def:tl5-hf-component]], put

    ‖A‖_Σ² := ∫_Σ e^(−φ) |A|² dμ dτ₂/(1 − κκ′),
    ⟦A⟧_(2,∞)² := ∫_(1/2)^(v_Σ) e^(−φ) sup_(ω∈S³) |A_e(γ_ω(v))|² dv,
    ⟦A⟧_(∞,2)² := sup_(1/2≤v≤v_Σ) e^(−φ) ∫_(S³) |A_e(γ_ω(v))|² dω,

φ being evaluated on the leaf through γ_ω(v), on which it is constant. For a function f on D^κ let [f]_t be its
supremum over Σ₁(t, v*), and put, with 𝔭_r := 1 + 12r² + 144r⁴ as in [[eq:tl5-hf-cs-r]],

    𝔵_r(t) := [𝔳^(2r) R⁻³]_t,      𝔪(t) := [max(1, 𝔴)⁶ R^(3/2)]_t,
    𝔱_r(t) := [𝔳^(2r) R⁻³ max(1 + 2r² |D̂∂_γ|², 2|∂_γ|²)]_t.

Then for every smooth covariant tensor field A of rank r with 1 ≤ r ≤ 4 on Q(t, b):

(a) ⟦A⟧_(∞,2)² ≤ [𝔳^(2r)]_t ∫_(S_t) |A|² dω + 𝔱_r(t) (‖A‖_Σ² + ‖D̂A‖_Σ²);

(b) ⟦A⟧_(2,∞)² ≤ (1/2) 𝔭_r 𝔵_r(t) Σ_(|J|≤2) ‖ℒ^J A‖_Σ², J ranging over the words in the six rotations;

(c) if X and Y are smooth covariant tensor fields on Q(t, b) of ranks r_X and r_Y with r_X + r_Y ≤ 6, and f is a
function on Σ with |f| ≤ |X| |Y| at every point, then, with φ(t, b) := Φ_o(t) + Φ_i(b),

    ‖f‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) ⟦X⟧_(2,∞) ⟦Y⟧_(∞,2).                                                   {#eq:tl5-hf4-holder}

*Proof.* Along γ_ω, τ₁ = t and dτ₂/dv = 1 − κκ′ > 0, so φ = Φ_o(t) + Φ_i(τ₂) is nondecreasing in v, as a_i ≥ 0, and at
most φ(t, b) on Σ; it depends only on (u, v), so it is constant on each leaf. On Σ, dμ dτ₂/(1 − κκ′) = R³ dω dv, as in
the proof of [[lem:tl5-hf-sobolev]].

(a) Fix ω. Since ∂_γ := ∂_v − κ′∂_u commutes with the fields of 𝒱 ([[lem:tl5-hf-components]]),
(d/dv)|A_e|²(γ_ω(v)) = 2⟨A_e, (ℒ_(∂_γ)A)_e⟩ ≤ |A_e|² + |(ℒ_(∂_γ)A)_e|². Integrate over S³ and from 1/2 to v, and use
e^(−φ(v)) ≤ e^(−φ(v′)) for v′ ≤ v and e^(−φ) ≤ 1:

    e^(−φ(v)) ∫ |A_e|²(γ_ω(v)) dω ≤ ∫_(S_t) |A_e|² dω + ∫_(1/2)^v e^(−φ) ∫ (|A_e|² + |(ℒ_(∂_γ)A)_e|²) dω dv′.

By [[lem:tl5-hf-components]], |B_e| ≤ 𝔳^r |B| for every tensor B of rank r. As D̂ is torsion free, ℒ_(∂_γ)A = D̂_(∂_γ)A +
Σ_(i=1)^r A(…, D̂∂_γ ·, …), the i-th slot receiving D̂∂_γ; so |ℒ_(∂_γ)A| ≤ |∂_γ| |D̂A| + r |D̂∂_γ| |A|,
and |A_e|² + |(ℒ_(∂_γ)A)_e|² ≤ 𝔳^(2r) ((1 + 2r²|D̂∂_γ|²)|A|² + 2|∂_γ|²|D̂A|²). With dω dv = R⁻³ dμ dτ₂/(1 − κκ′), this
gives (a).

(b) Fix v. By [[lem:tl5-hf-sphere]], with 6C_(S³)² = 1/2, applied to each component f of A_e on the leaf through
γ_ω(v), sup_ω |A_e|² is at most 1/2 times the integral over the leaf of the sum over the components of
f² + Σ (K f)² + Σ (K′K f)². By [[lem:tl5-hf-components]], with r slots, |K(B_e)| ≤ |(ℒ_K B)_e| + r|B_e|
and |K′K(B_e)| ≤ |(ℒ_(K′)ℒ_K B)_e| + r|(ℒ_K B)_e| + r|(ℒ_(K′)B)_e| + r²|B_e|, the index actions being constant. Squaring,
with (x + y)² ≤ 2(x² + y²) and (x + y + z + w)² ≤ 4(x² + y² + z² + w²), and summing over the six K and the 36 pairs
(K, K′), the sum is at most 𝔭_r Σ_(|J|≤2) |(ℒ^J A)_e|², the coefficients being 1 + 12r² + 144r⁴, 2 + 48r² and 4.
With |(ℒ^J A)_e| ≤ 𝔳^r |ℒ^J A|, multiply by e^(−φ), constant on the leaf, integrate over v and use
dω dv = R⁻³ dμ dτ₂/(1 − κκ′).

(c) By [[lem:tl5-hf-components]], |f| ≤ |X| |Y| ≤ 𝔴^(r_X + r_Y) |X_e| |Y_e| ≤ max(1, 𝔴)⁶ |X_e| |Y_e|, so ‖f‖_Σ² ≤
𝔪(t)² ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv. Writing e^(−φ) = e^φ e^(−φ) e^(−φ), with e^φ ≤ e^(φ(t,b)) on Σ,

    ∫∫ e^(−φ) |X_e|² |Y_e|² dω dv ≤ e^(φ(t,b)) ∫ (e^(−φ) sup_ω |X_e|²) (e^(−φ) ∫ |Y_e|² dω) dv
      ≤ e^(φ(t,b)) ⟦X⟧_(2,∞)² ⟦Y⟧_(∞,2)²,

which is (c). ∎

**Lemma {#lem:tl5-hf4-linfty}** (The low quantities at level four.) Let g be a solution of the reduced problem on
D^κ_s, h := g − ĝ, p ∈ D^κ_s, and let 𝔰₀ and the other quantities of [[lem:tl5-hf-linfty]] be formed with N = 4 and the
quantities of [[def:tl5-hf4-levels]]. If 𝔰 ≤ 𝔰₀ on Q(τ₁(p), τ₂(p)), then [[eq:tl5-hf-linfty]] holds at p, and at every
point of Q(τ₁(p), τ₂(p))

    M₂ ≤ 2(k₁ + 1) 𝒥₁ + 2k₂ ϱ(p),      M₂ = max_(|C|≤3) |D̂²Ψ_C|.                                      {#eq:tl5-hf4-m2}

*Proof.* The proof of [[lem:tl5-hf-linfty]] uses the level only through [[lem:tl5-hf-quadratic]], which it applies to
the words of length at most N − 1 = 3 and, in its last step, to the word of length N − 4 = 0, whose monomials have only
low solution factors. For these words [[lem:tl5-hf4-quadratic]] (b) gives the bounds used there, as 𝔑^M vanishes on
them. Every other step holds for N = 4 as written, and its step on second derivatives gives [[eq:tl5-hf4-m2]], ϱ(p)
bounding |ℒ^J(2R̂ic)|, |J| ≤ 3, on Q(τ₁(p), τ₂(p)). ∎

**Lemma {#lem:tl5-hf4-mixed}** (The products with no factor at a point.) Let g be a solution of the reduced problem on
D^κ_s, h := g − ĝ, t ∈ [−10, u*] and b ∈ [1/2, s] with Σ := Σ₁(t, b) not empty, and suppose that 𝔰 ≤ 𝔰₀ on Q(t, b), with
𝔰₀ as in [[lem:tl5-hf4-linfty]]. Let ϱ ≥ max_(|J|≤3) |ℒ^J(2R̂ic)| on Q(t, b), and η₀ ≥ max(𝔰, |Ψ_C| (|C| ≤ 4), |D̂Ψ_C|
(|C| ≤ 3)) on N₀ ∩ Q(t, b). With the notation of [[lem:tl5-hf4-face]], 𝒥₁, k₁ and k₂ as in [[lem:tl5-hf4-linfty]] and 𝔨₂
:= (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²), put 𝔍 := ‖𝒥₁‖_Σ and

    λ_t := 2([k₁]_t + 1),      ς_t := 2[k₂]_t (∫_(Σ₁(t,v*)) dμ dτ₂/(1 − κκ′))^(1/2),
    𝔛_t := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ]_t²),
               (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),
    𝔜_t := max(𝔱₃(t)^(1/2) (1 + 7λ_t), 7 𝔱₃(t)^(1/2) ς_t, 𝔱₂(t)^(1/2), π (98 [𝔳⁶]_t)^(1/2), π (686 [𝔳⁴]_t)^(1/2)).

Then

    ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔛_t 𝔜_t (𝔍 + ϱ) (𝔍 + ϱ + η₀),
    𝔍² ≤ [𝔨₂]_t Σ_(|I|≤4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                                  {#eq:tl5-hf4-mixed}

*Proof.* On Σ, |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) = 𝔨₂ (1 − κκ′) ε₁[Ψ_C] by [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], which gives the second inequality. By [[eq:tl5-hf4-m2]] at the points of Σ, with e^(−φ) ≤ 1
and Σ ⊂ Σ₁(t, v*), ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ.

The function 𝔭_M² is a sum of products |X|² |Y|² over the pairs (X, Y) := (D̂Ψ_B, D̂Ψ_(B′)), |B| = |B′| = 2, of ranks
3 and 3, and (X, Y) := (D̂²Ψ_Z, Ψ_B), |B| = 3, Z ∈ Γ, of ranks 4 and 2. So ‖𝔭_M‖_Σ² is the sum of ‖|X| |Y|‖_Σ² over
these pairs, and by [[eq:tl5-hf4-holder]] it is at most e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²), with

    X₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(2,∞)²,   Y₁² := Σ_(|B|=2) ⟦D̂Ψ_B⟧_(∞,2)²,
    X₂² := Σ_(Z∈Γ) ⟦D̂²Ψ_Z⟧_(2,∞)²,   Y₂² := Σ_(|B|=3) ⟦Ψ_B⟧_(∞,2)².

*X₁.* By (ii) of the proof of [[lem:tl5-hf-quadratic]], applied with Ψ_B in place of h, for a word J of rotations
with |J| ≤ 2, ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′ with R′ a sum of at most m′_(|J|) monomials, m′₀ = 0, m′₁ = 2, m′₂ = 6, each the
contraction of a coefficient of norm at most Λ with some Ψ_C, |C| ≤ 3; so |R′| ≤ m′_(|J|) Λ 𝒥₁. The words JB are distinct
and of length at most 4, there are 49 words B of length 2, and Σ_(|J|≤2) m′_(|J|)² = 6 · 4 + 36 · 36 = 1320; so Σ_B
Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥₁² + 2 · 49 · 1320 Λ² 𝒥₁² at every point, and by [[lem:tl5-hf4-face]] (b) with r = 3, X₁ ≤ (𝔭₃ 𝔵₃(t)
(1 + 64680 [Λ]_t²))^(1/2) 𝔍.

*X₂.* By (iii) of that proof, applied with Ψ_Z in place of h, ℒ^J D̂²Ψ_Z = D̂²Ψ_(JZ) + R with R a sum of at most m_(|J|)
monomials, m₁ = 7, m₂ = 35, each with at most two background factors of norm at most Λ and one solution factor D̂Ψ_C or
Ψ_C with |C| ≤ 2; so |R| ≤ m_(|J|) Λ² 𝒥₁, while |D̂²Ψ_(JZ)| ≤ M₂ as |JZ| ≤ 3. There are 7 fields Z and 43 words J, and
Σ_(|J|≤2) m_(|J|)² = 6 · 49 + 36 · 35² = 44394; so Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M₂² + 621516 Λ⁴ 𝒥₁², and by
[[lem:tl5-hf4-face]] (b) with r = 4 and √621516 < 789, X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 ‖M₂‖_Σ + 789 [Λ]_t² 𝔍).

*Y₁ and Y₂.* On S_t ⊂ N₀ ∩ Q(t, b), |D̂Ψ_B| ≤ η₀ for |B| ≤ 3 and |Ψ_B| ≤ η₀ for |B| ≤ 4, and ∫_(S_t) dω = 2π². By
[[lem:tl5-hf4-face]] (a) with r = 3 and r = 2, as Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M₂² and Σ_(|B|=2) |D̂Ψ_B|² ≤ 𝒥₁²,

    Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍² + 49 ‖M₂‖_Σ²),      Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍²,

there being 343 words of length 3.

With ‖M₂‖_Σ ≤ λ_t 𝔍 + ς_t ϱ these give X_i ≤ 𝔛_t (𝔍 + ϱ) and Y_i ≤ 𝔜_t (𝔍 + ϱ + η₀) for i = 1, 2, and (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ X₁ Y₁ + X₂ Y₂ gives the first inequality. ∎

#### The bootstrap at level four {#sec:tl5-hf4-bootstrap}

**Definition {#def:tl5-hf4-constants}** (The constants at level four.) Fix μ ∈ (0, 1], weights z, z̲, admissible rates
a_o, a_i for (𝔅₄, E_o⁴, E_i⁴) and φ as in [[prop:tl5-hf-linear]], and let Y_σ be the norm of [[def:tl5-hf-norm]], whose
definition and properties do not use N ≥ 5, with N = 4. Let G^♯ be data in the wave gauge, and let δ_w, ε_w, 𝔤₄, ϰ₀,
𝔞_o, 𝔞_i, S_F, 𝔯_w, 𝔰₀, 𝔰_θ and 𝔰₁ be given by the formulas of [[def:tl5-hf-constants]] with N = 4, the quantities of
[[def:tl5-hf4-levels]] and the constants of [[lem:tl5-hf4-linfty]], ϱ and η₀ being those of [[lem:tl5-hf4-linfty]] for a
point p with τ₁(p) = u*, τ₂(p) = v*. Put, with the notation of [[lem:tl5-hf4-face]] and [[lem:tl5-hf4-mixed]] and with
[𝔠₄]_t the number 𝔠₄ formed with [Λ]_t in place of Λ,

    m_t := 98 e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t [𝔠₄]_t 𝔪(t) 𝔛_t 𝔜_t,
    S_M := μ^(−2) ∫_(−10)^(u*) m_t [𝔨₂]_t dt,      𝔯_M := ∫_(−10)^(u*) m_t [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_M := μ² ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t dt,
    S_(F,4) := S_F + S_M,      𝔯_(w,4) := 𝔯_w + 𝔯_M,      ε_(w,4) := ε_w + ε_M,
    A_(w,4) := √2 δ_w + 2ε_(w,4),      B_(w,4) := 2 S_(F,4),                                      {#eq:tl5-hf4-constants}

and let 𝔰_* be given by the formula of [[def:tl5-hf-constants]] with N = 4 and A_(w,4) in place of A_w:

    𝔰_* := sup_(p∈D^κ) (2 C_∞(p) μ^(−2) e^(φ(p)/2) A_(w,4) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).

As in [[def:tl5-hf-constants]], δ_w contains the fluxes of the Ψ_I and of 𝔟[Ψ_I], |I| ≤ 4, through N₀ and through N₁,
and η₀ and these fluxes are computed from the derivatives of G^♯ − ĝ on N of order at most 4, and of order 5 in the
terms 𝔟, which vanish where H does.

**Proposition {#prop:tl5-hf4-bootstrap}** (The a priori estimate at level four.) In the setting of
[[def:tl5-hf4-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴) and that

    𝔯_(w,4) ≤ 1/4,      η₀ < 𝔰₁,      𝔰_* < 𝔰₁.                                                   {#eq:tl5-hf4-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_(w,4) for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_* on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_(w,4) + B_(w,4) Y_s(g)².                                                                {#eq:tl5-hf4-h1}

*Proof.* The first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]] hold as written with N = 4, A_(w,4)
in place of A_w and [[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]]: g is vacuum and has on N ∩ D^κ_s the
derivatives of G^♯, so that the quantities on N₀ bounded by η₀ are those of g; and 𝔰 ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, so
that |h|_k̂ < κ_m/2 and θ_H ≤ ϑ.

Step 2 of that proof holds with N = 4, [[lem:tl5-hf4-quadratic]] and [[lem:tl5-hf4-linfty]] in place of
[[lem:tl5-hf-quadratic]] and [[lem:tl5-hf-linfty]], except at one place: |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) 𝔰 𝔧 for |J| ≤ 3, as
there, but for |I| = 4 only |𝔑_I − 𝔑^M_I| ≤ 𝔠₄ 𝔰 𝔧. With 𝔑_I − 𝔑^M_I in place of 𝔑_I that step goes through, and the
terms 𝔑^M_I add to the bulk of the weighted sum over I, by the proof of the second inequality of
[[lem:tl5-hf-pointwise]], at most

    ∫_(Q(a′,b′)) e^(−φ) μ⁴ Σ_(|I|=4) 2Ω̂² |𝔑^M_I| (√e_o[Ψ_I] + √c √e_i[Ψ_I]) dμ du dv.

By the Cauchy–Schwarz inequality, √e_o + √c √e_i ≤ (1 + c/κ′)^(1/2) (e_o + κ′ e_i)^(1/2), and
e_o + κ′ e_i = (1 − κκ′) ε₁. Foliate Q(a′, b′) by the faces Σ₁(t, b′), −10 ≤ t ≤ a′, with du dv = dτ₁ dτ₂/(1 − κκ′),
and apply the Cauchy–Schwarz inequality on each nonempty face Σ := Σ₁(t, b′) and over I: the term is at most

    ∫_(−10)^(a′) [2Ω̂² (1 + c/κ′)^(1/2)]_t μ⁴ (Σ_(|I|=4) ‖𝔑^M_I‖_Σ²)^(1/2)
        × (Σ_(|I|=4) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂)^(1/2) dt.

By [[eq:tl5-hf4-g]], ‖𝔑^M_I‖_Σ ≤ [𝔠₄]_t ‖𝔭_M‖_Σ, and as there are 7⁴ = 49² words of length 4, the second factor is at
most 49 [𝔠₄]_t ‖𝔭_M‖_Σ. The last factor is at most μ^(−2) Y_s. By Step 1, 𝔰 ≤ 𝔰₀ on D^κ_s, so [[lem:tl5-hf4-mixed]]
applies, with the ϱ and η₀ of [[def:tl5-hf4-constants]], and with 𝔍² ≤ [𝔨₂]_t μ^(−4) Y_s², as Σ_(|I|≤4) ∫_Σ e^(−φ)
ε₁[Ψ_I] dμ dτ₂ ≤ μ^(−4) Y_s². With e^(φ(t,b′)) ≤ e^(φ(t,v*)), the term is at most

    ∫_(−10)^(u*) m_t μ² (𝔍 + ϱ)(𝔍 + ϱ + η₀) Y_s dt ≤ S_M Y_s³ + 𝔯_M Y_s² + ε_M Y_s,

by μ²(𝔍 + ϱ)(𝔍 + ϱ + η₀) ≤ [𝔨₂]_t μ^(−2) Y_s² + [𝔨₂]_t^(1/2) (2ϱ + η₀) Y_s + μ² ϱ (ϱ + η₀).

Step 3 of that proof, with this term added, gives for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s ε_(w,4) + 𝔯_(w,4) Y_s² + S_(F,4) Y_s³,

and, as there, with ϑ ≤ 1/4 and 𝔯_(w,4) ≤ 1/4, Y_s² ≤ 2δ_w² + 2Y_s ε_(w,4) + 2S_(F,4) Y_s³, whence
[[eq:tl5-hf4-h1]]. ∎

**Lemma {#lem:tl5-hf4-persistence}** (Persistence of regularity at level four.) Suppose the hypotheses of
[[prop:tl5-hf4-bootstrap]] hold. For every k ≥ 0 there is C_k, depending only on k, ĝ, G^♯, κ, κ′, μ, ϑ, z, z̲, the rates
and A_(w,4), such that every solution g of the reduced problem on a D^κ_s with Y_σ(g) ≤ 2A_(w,4) for all σ ∈ [1/2, s] has
its components and their partial derivatives of order at most k, and the components of g⁻¹, bounded by C_k on D^κ_s, in
the coordinates (u, v, y) of a fixed finite atlas of S³.

*Proof.* By [[prop:tl5-hf4-bootstrap]], 𝔰 ≤ 𝔰_* on D^κ_s; in particular |H| ≤ 1/8, which bounds g⁻¹ = ĝ⁻¹ + H, and
θ_H ≤ ϑ. A constant is a number depending only on the data listed, Λ here bounding the quantities of
[[def:tl5-hf4-levels]] for words of every length that occurs. A face is a nonempty Σ := Σ₁(t, b) with t ≤ u* and b ≤
s; for a weight φ as in [[prop:tl5-hf-linear]] we use the norms of [[lem:tl5-hf4-face]], and write ‖·‖_(Σ,0) and
⟦·⟧⁰ for those with φ replaced by 0, to which that lemma applies with zero rates. For m ≥ 4 let P(m) be the statement:
there is a constant E_m such that on every face

    Σ_(|I|≤m) ∫_Σ ε₁[Ψ_I] dμ dτ₂ + Σ_(|B|≤m−1) ‖D̂²Ψ_B‖²_(Σ,0) ≤ E_m,

and |Ψ_B| (|B| ≤ m − 2), |D̂Ψ_B| (|B| ≤ m − 3) and |D̂²Ψ_B| (|B| ≤ m − 4) are at most E_m on D^κ_s. P(4) holds: the
face energies are at most μ^(−4) e^(Φ_o(u*) + Φ_i(v*)) 4A_(w,4)²; by [[eq:tl5-hf4-m2]] each |D̂²Ψ_B|, |B| ≤ 3, is at
most 2(k₁ + 1)𝒥₁ + 2k₂ϱ at every point, and ∫_Σ 𝒥₁² dμ dτ₂/(1 − κκ′) is at most [𝔨₂]_t times the face energy, as in
the proof of [[lem:tl5-hf4-mixed]]; and 𝔰 ≤ 𝔰_*.

Let m ≥ 5 and assume P(m − 1). Then every solution factor of order at most m − 3 is bounded at every point by a
constant, and every solution factor of order at most m has its norm ‖·‖_(Σ,0) bounded by a constant on every face:
Ψ_B and D̂Ψ_B with |B| ≤ m − 1 by [[eq:tl5-hf-coercive]], Ψ_B with |B| = m by |ℒ_ZΨ| ≤ |Z| |D̂Ψ| + 2|D̂Z| |Ψ|
([[eq:tl5-hf-lie]]), and D̂²Ψ_B with |B| ≤ m − 2 by P(m − 1). For a face and a weight φ let U_φ(Σ) be the sum of the
norms ‖Φ‖_Σ of the solution factors Φ of order m + 1: D̂Ψ_C with |C| = m, Ψ_C with |C| = m + 1 and D̂²Ψ_C with |C| =
m − 1.

*(i) The monomials.* Let |I| = n ≤ m and take a monomial of ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, with its solution factors
ordered by their orders. By [[lem:tl5-hf4-quadratic]] (a) these orders add up to at most n + 2 and each is at most n + 1.
If at most one factor has order at least m − 2, the others are bounded at every point, and the norm ‖·‖_Σ of the monomial
is at most a constant times ‖Φ‖_Σ, Φ the factor of largest order; this is at most a constant if Φ has order at most m,
and otherwise at most a constant times U_φ(Σ). If two factors have orders o ≤ o′ with o ≥ m − 2, then 2(m − 2) ≤ o + o′ ≤
m + 2, so m ≤ 6 and o, o′ ≤ 4; a third factor of order at least m − 2 would need 3(m − 2) ≤ m + 2, which fails, so the
other factors are bounded at every point. At most one of the two is of the form D̂²Ψ_C, as there are at most two
derivatives D̂ in all. Let Y be one that is not, the one of larger order if neither is, and X the other; then o_X ≤ 4 and
o_Y ≤ 4, and 4 ≤ m − 1. By [[eq:tl5-hf4-holder]], with the weight on one of the two factors, the norm ‖·‖_Σ of the
monomial is at most a constant times ⟦X⟧_(2,∞) ⟦Y⟧⁰_(∞,2) and at most a constant times ⟦X⟧⁰_(2,∞) ⟦Y⟧_(∞,2); for this,
the proof of (c) of that lemma is used with e^(−φ) |X_e|² |Y_e|² bounded by (e^(−φ) sup_ω |X_e|²) ∫ |Y_e|² dω, or by
sup_ω |X_e|² (e^(−φ) ∫ |Y_e|² dω), after integration over the leaf. By [[lem:tl5-hf4-face]] (b), and (ii), (iii) of the
proof of [[lem:tl5-hf-quadratic]] for the words JX, |J| ≤ 2, ⟦X⟧_(2,∞) is at most a constant times the norms of factors
of order at most o_X + 2 ≤ m + 1; and by (a) of that lemma ⟦Y⟧_(∞,2) is at most a constant times the norms of factors of
order at most o_Y + 1 ≤ m + 1 plus the integral of |Y|² over S_t, a derivative of G^♯ − ĝ on N₀ of order at most m and so
a constant. Factors of order m + 1 occur on both sides only if o_X + 2 = o_Y + 1 = m + 1, that is if o_X + o_Y = 2m − 1,
which exceeds m + 2; so, taking the weight on the side where they occur, the norm ‖·‖_Σ of the monomial is at most a
constant times 1 + U_φ(Σ).

*(ii) Second derivatives.* For |B| = m − 1 apply [[lem:tl5-hf-recovery]] at every point of a face, with the tensor H of
g, as in the proof of [[lem:tl5-hf-linfty]]: |D̂²Ψ_B| is at most a constant times Σ_Z |D̂Ψ_(ZB)| + |D̂Ψ_B| + |Ψ_B|
plus |𝔣_B|, 𝔣_B := L̂Ψ_B + H^(αβ)D̂_αD̂_βΨ_B being given by [[def:tl5-hf-coupling]] with 𝔤 = 2R̂ic − N(h) as there. Its
nonlinear part consists of the monomials of (i) for the words of length n ≤ m − 1, and of the terms H^(αβ)D̂_αD̂_βΨ_J
with |J| ≤ m − 2. These have norms ‖·‖_(Σ,0) bounded by constants: in the first case of (i) the factor of largest order
has order at most n + 1 ≤ m, and in the second case 2(m − 2) ≤ o + o′ ≤ n + 2 ≤ m + 1 forces m = 5 and o = o′ = 3, so
that o_X + 2 = 5 = m and o_Y + 1 = 4. The linear part is bounded by constants times the jets of level at most m − 1 and
the residual. So, for every weight, ‖D̂²Ψ_B‖_Σ is at most a constant times 1 + (Σ_(|C|=m) ‖D̂Ψ_C‖_Σ²)^(1/2), and
U_φ(Σ) ≤ c_m (1 + 𝔈_φ(Σ)^(1/2)) with a constant c_m and 𝔈_φ(Σ) := Σ_(|I|≤m) ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂, by
[[eq:tl5-hf-coercive]] and [[eq:tl5-hf-lie]].

*(iii) The energies.* By [[lem:tl5-hf-allocation]] there are constant rates A, A′ admissible for
((1 − ϑ)⁻¹ 𝔅_m, E_o^m, E_i^m), all entries being bounded on D^κ; for a constant Ã ≥ 0 take a_o := A + Ã and a_i := A′,
which are admissible too, as [[eq:tl5-hf-admissible]] is monotone in the rates, and the weight
φ := (A + Ã)(τ₁ + 10) + A′(τ₂ − 1/2). For |I| ≤ m apply [[lem:tl5-hf-identity]] to J̃ := J[Ψ_I] − 𝔟[Ψ_I] on
Q(a′, b′) ⊂ D^κ_s, with weights 1 and with 𝔅_m formed with μ = 1, as in Step 2 of the proof of
[[prop:tl5-hf-bootstrap]] at level m, which uses [[def:tl5-hf-coupling]] and the argument of [[prop:tl5-hf-linear-n]]
at level m. The face densities are at least 1 − ϑ times ε₁ and ε₂; the terms on N₁ and N₀ are fluxes of derivatives
of G^♯ − ĝ of order at most m + 1 ([[thm:tl5-wg]] (F4_W)), and so constants; and the linear bulk, with the weight and
the terms 𝔟 in it, is at most −(1 − ϑ) Ã (e_o + κ′ e_i) plus the forcing term of the residual. Indeed, as there,
2Ω̂² dφ(J) = (a_o + κa_i) e_o + (a_i + κ′a_o) e_i and 2Ω̂² |dφ(𝔟)| is at most ϑ times this; and of (1 − ϑ) times
this, the part with the rates A, A′ dominates ñᵀ𝔅_m ñ by their admissibility, and the rest is
(1 − ϑ) Ã (e_o + κ′ e_i). The term 𝔮_H is at most a constant times e_o + e_i ≤ (1 + 1/κ′)(e_o + κ′e_i), as in Step 2
of that proof. The nonlinear terms of L̂Ψ_I + H^(αβ)D̂_αD̂_βΨ_I are the monomials of (i) and the terms 𝔔_IJ ℒ^J N(h)
with |J| < |I|, whose terms H^(αβ)D̂_αD̂_βΨ_J are bounded by (ii); foliating by the faces Σ₁(t, b′) as in the proof of
[[prop:tl5-hf4-bootstrap]], their contribution is at most ∫ dt c (1 + 𝔈_φ(Σ₁(t, b′))) with a constant c, by (i), (ii)
and 2x ≤ 1 + x². The term −(1 − ϑ) Ã (e_o + κ′ e_i) contributes −(1 − ϑ) Ã ∫ dt 𝔈_φ(Σ₁(t, b′)), since
∫_Q e^(−φ) (e_o + κ′ e_i) dμ du dv = ∫ dt ∫_(Σ₁(t,b′)) e^(−φ) ε₁ dμ dτ₂. With Ã so large that (1 − ϑ) Ã exceeds c and
the constant of 𝔮_H, and with the residual bounded as in [[prop:tl5-hf-linear]], the supremum Y_m² of the weighted
level-m energies over the corner regions in D^κ_s satisfies Y_m² ≤ c′ + 𝒮_m Y_m with constants c′ and 𝒮_m. So Y_m is
bounded by a constant, and so are the unweighted energies, which are at most e^((A+Ã)(u*+10) + A′(v*−1/2)) Y_m², and
by (ii) the norms ‖D̂²Ψ_B‖_(Σ,0), |B| = m − 1.

*(iv) Bounds at a point.* [[lem:tl5-hf-sobolev]] and [[eq:tl5-hf-cs-r]], whose terms on S_a are derivatives of G^♯ − ĝ on
N₀ of order at most m, bound |Ψ_B| (|B| ≤ m − 2) and |D̂Ψ_B| (|B| ≤ m − 3) at every point by the face energies of level m
and the face norms of D̂²Ψ_C, |C| ≤ m − 1. [[lem:tl5-hf-recovery]] at the point, in order of increasing |B| ≤ m − 4,
bounds |D̂²Ψ_B|: its nonlinear terms come from words of length at most m − 4, whose solution factors have orders at most
m − 3 by [[lem:tl5-hf4-quadratic]] (a) and are bounded at the point by the bounds just obtained, by P(m − 1) and by the
induction on |B|, besides H^(αβ)D̂_αD̂_βΨ_B, which the lemma absorbs. So P(m) holds for every m ≥ 4.

The last paragraph of the proof of [[lem:tl5-hf-persistence]] uses only the bounds at a point of the statements P(m),
for all m, and gives the claim. ∎

**Theorem {#thm:tl5-hf4}** (Existence close to an explicit background, at level four.) Let ĝ be a background with
u* < −1, κ and κ′ as in [[def:tl5-wg-domains]], g_N smooth characteristic data in the gauge on N⁺ satisfying the
constraints, G^♯ data in the wave gauge for g_N, μ ∈ (0, 1], ϑ ∈ (0, 1/4], z, z̲ and rates a_o, a_i as in
[[def:tl5-hf4-constants]], and suppose:

(a) the quantity η₀ of [[def:tl5-hf4-constants]], computed from the derivatives of G^♯ − ĝ of order at most 4 on N₀,
satisfies η₀ < 𝔰₁;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴);

(c) the constants of [[def:tl5-hf4-constants]] satisfy 𝔯_(w,4) ≤ 1/4, 𝔰_* < 𝔰₁ and the closing condition

    4 A_(w,4) B_(w,4) = 8 (√2 δ_w + 2ε_w + 2ε_M) (S_F + S_M) < 1.                                   {#eq:tl5-hf4-closing}

Then there is a solution g of the reduced problem on D^κ, and Y_σ(g) ≤ 2A_(w,4) for every σ ∈ [1/2, v*]. It is a
G-invariant vacuum metric in the wave gauge, with |g − ĝ|_k̂ < κ_m/2 and 𝔰 ≤ 𝔰_* on D^κ, and the quantity ε of
[[eq:tl5-dn-eps]] for g_σ and ĝ_σ on B ∩ M_σ, B as in [[thm:tl5-dn]], satisfies ε ≤ ε_𝔰 𝔰_*. If moreover the
hypotheses of [[thm:tl5-dn]] hold for this ε, then the metric g̃ that theorem gives on D′ is a smooth G-invariant vacuum
metric of the class in the gauge of [[sec:cone-constraint]], equal to g_N at every point of N ∩ D′.

*Proof.* The proof of [[thm:tl5-hf]] applies with A_(w,4), B_(w,4), [[prop:tl5-hf4-bootstrap]], [[eq:tl5-hf4-h1]],
[[lem:tl5-hf4-persistence]] and [[eq:tl5-hf4-closing]] in place of A_w, B_w, [[prop:tl5-hf-bootstrap]],
[[eq:tl5-hf-h1]], [[lem:tl5-hf-persistence]] and [[eq:tl5-hf-closing]]; if A_(w,4) = 0, then δ_w = ε_w = 0, and ĝ is
the solution as there. The bound for ε is [[eq:tl5-hf-eps]], as |h|, |D̂h| and |D̂²h| are at most 𝔰 at level four
([[def:tl5-hf4-levels]]). ∎

**Remark {#rem:tl5-hf4-level}** (Level four and level six.) The constants of [[thm:tl5-hf4]] are those of
[[thm:tl5-hf]] at N = 4, with the terms S_M, 𝔯_M and ε_M of the products of [[lem:tl5-hf4-mixed]] added. They are
explicit in the jets of ĝ of order at most N + 3 = 7, against 9 at N = 6; they involve the Σ_(j≤4) 7^j = 2801 words of
length at most 4, against 137,257 at N = 6, the derivatives of R̂ic along Γ of order at most 4, against 6, and the
factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2); with the constants of [[thm:tl5-hf4g]]
and the graded triple both carry μ^(−3/2) ([[rem:tl5-hfg-powers]]). On N₀ they involve the derivatives of
G^♯ − ĝ of order at most 4, through η₀ and the fluxes in δ_w, and of order 5 in the terms 𝔟 of δ_w, which carry the
factor H; all of these vanish when G^♯ − ĝ vanishes together with its partial derivatives of order at most 4 at the
points of N₀. At the first stage of the problem at 10 l5, by
[[lem:tl5-xt-order]] (c) with m = 5, this holds when (X) holds and the components of ĝ − g′ and their partial
derivatives of order at most 5 vanish at the points of N₀⁺, g′ being the metric of [[thm:tl5-wg-data]] as in
[[sec:tl5-xt]]. By [[lem:tl5-xt-seed-jets]], the partial derivatives of g′ of order at most 3 at those points are the
seed's, and the fourth derivatives in v of its leaf metric differ from the seed's at every point with −1 < x < 1 off
at most one torus {x = c}. So this condition asks the background to carry the derivatives in v of g′ of orders 4 and
5 on N₀⁺, and a background with the seed's jets there does not satisfy it. At level three the face energies give no
bound of |D̂²h| at a point ([[rem:tl5-hf-level]]), which the passage to the double-null gauge needs. As for
[[thm:tl5-hf]] ([[rem:tl5-beyond]]), the hypotheses of [[thm:tl5-hf4]] are established in this paper for no background
at 10 l5.

### The sharpened constants {#sec:tl5-hfg}

This section sharpens the constants of [[thm:tl5-hf]] and [[thm:tl5-hf4]] in three ways and proves both theorems with
the sharpened constants. First, each background factor of a quadratic term is bounded by a bound for the derivatives of
ĝ of its own order, instead of the uniform bound Λ, and the constant of the recovery of second derivatives is taken at
the level where it is used ([[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]]). Second, in Steps 2 and 3 of the proof
of [[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again, of which the weight of level j in 𝔤_N returns
μ^(j/2); here each factor is bounded by the energies of the lowest level that controls it, and in every term of level n
the two levels used add up to at most n + 3, so that the factor becomes μ^(−3/2) at every level N ≥ 4
([[lem:tl5-hfg-products]]). Third, the quadratic part of N(h) is
expanded with its own coefficients, the terms of higher order carrying a factor 𝔰 ([[lem:tl5-hfg-quadratic]]), and the
factor bounded at a point is never a second derivative of a word of length two or more ([[lem:tl5-hfg-products]]). The
closing conditions are [[eq:tl5-hfg-closing]] at level N ≥ 6 and [[eq:tl5-hf4g-closing]] at level four
([[thm:tl5-hfg]], [[thm:tl5-hf4g]]); those of [[thm:tl5-hf]] and [[thm:tl5-hf4]] remain valid, and either may be used.
Throughout, N ≥ 4 and μ ∈ (0, 1]; for N = 4 the quantities 𝔰, 𝔧 and 𝔭_M are those of [[def:tl5-hf4-levels]], and
[[lem:tl5-hf4-linfty]] takes the place of [[lem:tl5-hf-linfty]].

**Definition {#def:tl5-hfg-graded}** (Graded quantities.) Let h be a C^(N+2) symmetric 2-tensor field with g = ĝ + h
Lorentzian. At a point let Λ₀ := 0 ≤ Λ₁ ≤ ⋯ ≤ Λ_N be numbers such that, for k ≥ 1, Λ_k bounds the norms of ℒ^B π^Z, ℒ^B
Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] for |B| ≤ k − 1 and Z ∈ Γ; for 0 ≤ k ≤ N let Λ^R_k bound the norms of ℒ^B R̂ for
the words B with |B| = k, and for 1 ≤ k ≤ N let λ_k bound those of ℒ^K ĝ⁻¹ for the words K with |K| = k; and put Λ̄_k :=
max(Λ_k, Λ_k²), λ₀ := 1, λ̂₀ := √5 and λ̂_k := λ_k for k ≥ 1. A background factor ℒ^B R̂ carries the |B| letters of B,
and ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] carry the |B| + 1 letters of B and Z; so a factor of the last
four kinds that carries at most k letters has norm at most Λ_k. For m ≥ 1 and a function f on ℕ^m write

    Σ^m_n f := Σ_(k∈ℕ^m, k₁+⋯+k_m=n) (n!/(k₁! ⋯ k_m!)) f(k),

and put, with 𝔤₀ and the ordered Bell numbers F_k of [[def:tl5-hf-levels]],

    β₁^g(0) := β₂^g(0) := 1,   β₁^g(k) := 1 + (2^(k+1) − 2) Λ_k,   β₂^g(k) := 1 + (7/3)(4^k − 1) Λ̄_k,
    b_g^g(0) := 𝔤₀,   b_g^g(k) := F_k 𝔤₀^(k+1) (Λ_k + 1)^k,   b_H^g(0) := 1,   b_H^g(k) := (2k + 1) b_g^g(k),
    𝔠^g_n := Σ²_n b_H^g(k₁) β₂^g(k₂) − 1 + 5 Σ³_n b_H^g(k₁) Λ^R_(k₂) + 16 Σ⁴_n b_g^g(k₁) b_g^g(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^Q_n := Σ⁴_n λ_(k₁) λ_(k₃) β₂^g(k₄) − 1 + 5 Σ⁵_n λ_(k₁) λ_(k₃) Λ^R_(k₄) + 16 Σ⁴_n λ̂_(k₁) λ̂_(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^(3)_n := Σ⁶_n b_g^g(k₁) λ_(k₃) λ_(k₅) β₂^g(k₆) − 𝔤₀ + 5 Σ⁷_n b_g^g(k₁) λ_(k₃) λ_(k₅) Λ^R_(k₆)
               + 16 Σ⁶_n b_g^g(k₁) λ_(k₃) (b_g^g(k₄) + λ̂_(k₄)) β₁^g(k₅) β₁^g(k₆),                       {#eq:tl5-hfg-cn}

k ≥ 1 where not stated. Fix 𝔰_♭ ∈ (0, 1/8] and one of the two choices 𝔠^⋆_n := 𝔠^g_n, the first expansion, or 𝔠^⋆_n :=
𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n, the second expansion, for all n ≤ N; with the first choice 𝔰_♭ = 1/8 may be taken. Finally put

    𝒥_g := (Σ_(|C|≤N) μ^|C| (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),      M_g^(j) := max_(|C|≤j) μ^((|C|+1)/2) |D̂²Ψ_C|,
    𝔰_g^(m) := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2), μ^((|B|+3)/2) |D̂Ψ_B| (|B| ≤ N − 3),
               μ^((|B|+4)/2) |D̂²Ψ_B| (|B| ≤ m)),
    𝔷 := max_(Z∈Γ) (|Z|² + 4|D̂Z|²)^(1/2),      m_P := min(1, N − 4),

for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4, the maxima over words B and C in Γ, M_g := M_g^(N−1), and for p ∈ D^κ, with a :=
τ₁(p) and b := τ₂(p),

    ℰ_g(p) := Σ_(|I|≤N) μ^|I| ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂.

The order of a solution factor H, Ψ_B, D̂Ψ_B or D̂²Ψ_B is 0, |B|, |B| + 1 or |B| + 2, as in [[def:tl5-hf4-levels]]; a
low quantity of order o enters 𝔰_g^(m) with the weight μ^((o+2)/2), and o + 2 ≤ N, so 𝔰_g^(N−4) ≤ 𝔰 ≤ μ^(−N/2)
𝔰_g^(N−4). For μ = 1, 𝒥_g, M_g, 𝔰_g^(N−4) and ℰ_g(p) are 𝒥₁, M₂, 𝔰 and ℰ⁰_N(p) of [[lem:tl5-hf-linfty]].

Every Λ as in [[def:tl5-hf-levels]] or [[def:tl5-hf4-levels]] may be taken for every Λ_k, k ≥ 1, and every Λ^R_k, as
it bounds the five kinds of factors for words of length at most N; so 𝔠^g_n ≤ 𝔠_n, by Λ ≥ 1 and Σ_(j≤n−k) C(n − k, j)
Λ^R_j ≤ 2^(n−k) Λ, with the binomial coefficients C(·, ·). And λ_k := Σ_(r=1)^k r! S(k, r) 5^((r+1)/2) Λ_k^r may be
taken, S(k, r) the Stirling numbers of the second kind: by (iv) of the proof of [[lem:tl5-hf-quadratic]] with h = 0,
ℒ^K ĝ⁻¹ is a sum of r! S(k, r) products of r + 1 factors ĝ⁻¹, of norm √5, and r factors ℒ^(B′) π^Z, each carrying at
most k letters.

**Lemma {#lem:tl5-hfg-quadratic}** (The quadratic terms with graded background bounds.) Let h be as in
[[def:tl5-hfg-graded]], p a point with 𝔰(p) ≤ 𝔰_♭, and I a word with n := |I| ≤ N. Then ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I
is a sum of monomials, each a contraction of background factors and of q ≥ 2 solution factors of the forms and orders
of [[lem:tl5-hf4-quadratic]] (a), whose background norms ν, with the coefficients, satisfy

    Σ ν 𝔰(p)^(q−2) ≤ 𝔠^⋆_n,                                                                             {#eq:tl5-hfg-sum}

the sum over the monomials. Consequently [[eq:tl5-hf-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N ≥ 5, and
[[eq:tl5-hf4-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N = 4, 𝔑^L_I and 𝔑^M_I being formed from the chosen
expansion.

*Proof.* *The first expansion.* It is that of the proof of [[lem:tl5-hf-quadratic]]. In (i) there, ℒ^J R̂ has norm at
most Λ^R_(|J|). In (ii), with k := |J|, each monomial of R′_J has one coefficient
ℒ^B Γ′[π^Z] whose letters are among those of J, so its norm is at most Λ_k, and ℒ^J D̂h is a sum of monomials of total
background norm at most β₁^g(k). In (iii) each monomial of R_J has at most two background factors, carrying letters of
J, so their product is at most Λ̄_k, and the total is at most β₂^g(k). In (iv) each factor ℒ^B ĝ = ℒ^(B′) π^Z carries
the |B| ≤ k letters of B, so ℒ^J g⁻¹ has total background norm at most b_g^g(k) and ℒ^J H at most b_H^g(k), the
number of factors in the telescoping sums being 2r + 1 ≤ 2k + 1 as there. Summing as in that proof, over the
distributions of the letters of I over the factors of each term of N(h), gives the three sums of 𝔠^g_n: Σ²_n from
H^(λσ) D̂_λD̂_σ h, the letters going to H and to D̂²h, less 1 for the subtracted term H^(αβ) D̂_αD̂_βΨ_I; Σ³_n from the
five terms of 2𝔠(H)h, the letters going to H, R̂ and h; Σ⁴_n from the sixteen units of coefficient of 2𝔮. Every
monomial has q ≥ 2 solution factors and 𝔰(p) ≤ 1, which gives [[eq:tl5-hfg-sum]].

*The second expansion.* Let H₁ := −ĝ⁻¹ h ĝ⁻¹, that is H₁^(αβ) = −ĝ^(αμ) h_μν ĝ^(νβ), and H₂ := H − H₁. Since g⁻¹ −
ĝ⁻¹ = −g⁻¹ h ĝ⁻¹, applied twice, H₂ = g⁻¹ h ĝ⁻¹ h ĝ⁻¹. By [[lem:tl5-hf-reduced]], 2𝔮 = Σ_m c_m 𝒯_m(g⁻¹, g⁻¹, D̂h, D̂h)
with Σ_m |c_m| = 16, each 𝒯_m a contraction, linear in each argument; let 2𝔮̂ := Σ_m c_m 𝒯_m(ĝ⁻¹, ĝ⁻¹, D̂h, D̂h). Then
2𝔮 − 2𝔮̂ = Σ_m c_m (𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹, H, D̂h, D̂h)) with H = −g⁻¹ h ĝ⁻¹, and, 𝔠 being linear in its first
argument, N(h) = Q + R₃ with

    Q := H₁^(λσ) D̂_λD̂_σ h − 2𝔠(H₁)h − 2𝔮̂,      R₃ := H₂^(λσ) D̂_λD̂_σ h − 2𝔠(H₂)h − (2𝔮 − 2𝔮̂).

So ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I is the sum of ℒ^I Q − H₁^(αβ) D̂_αD̂_βΨ_I and ℒ^I R₃ − H₂^(αβ) D̂_αD̂_βΨ_I. Expand
ℒ^I of each term by Leibniz's rule over its factors, as in the proof of [[lem:tl5-hf-quadratic]]: ℒ^J h = Ψ_J;
ℒ^J D̂h, ℒ^J D̂²h and ℒ^J g⁻¹ by (ii), (iii) and (iv) there, with the bounds β₁^g, β₂^g and b_g^g of the first part;
ℒ^J R̂ with norm at most Λ^R_(|J|); and ℒ^K ĝ⁻¹, for K ≠ ∅, as one background factor of norm at most λ_(|K|). The factors
ĝ⁻¹ that carry no letter in H₁, in H₂ and in H = −g⁻¹ h ĝ⁻¹ join an index of h to an index of another factor; in the
frame F, where ĝ^MN = η^MN, such a contraction is bounded by the product of the norms of the two factors, by the
Cauchy–Schwarz inequality, so these factors count λ₀ = 1. A factor ĝ⁻¹ of 𝒯_m that carries no letter may join two
indices of one factor, and counts |ĝ⁻¹| = √5 = λ̂₀. A full contraction of the factors is bounded by the product of
their norms. Summing over the distributions of the letters gives, for the terms of Q, the three sums of 𝔠^Q_n: Σ⁴_n
over the factors ĝ⁻¹, h, ĝ⁻¹, D̂²h of H₁^(λσ) D̂_λD̂_σ h, less 1 for the subtracted term H₁^(αβ) D̂_αD̂_βΨ_I; Σ⁵_n over
ĝ⁻¹, h, ĝ⁻¹, R̂, h for the five terms of 2𝔠(H₁)h; and Σ⁴_n over ĝ⁻¹, ĝ⁻¹, D̂h, D̂h for 2𝔮̂. Likewise the terms of R₃
give the three sums of 𝔠^(3)_n: Σ⁶_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h, less b_g^g(0) = 𝔤₀ for H₂^(αβ) D̂_αD̂_βΨ_I;
Σ⁷_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, R̂, h; and Σ⁶_n over g⁻¹, h, ĝ⁻¹, X, D̂h, D̂h with X = g⁻¹ or X = ĝ⁻¹. In the terms of
Q each of the two factors among h, D̂h and D̂²h keeps exactly one solution factor in its expansion, and the factors ĝ⁻¹
and R̂ none, so q = 2; in the terms of R₃ three such factors keep one each, so q ≥ 3, and 𝔰(p)^(q−2) ≤ 𝔰_♭. This gives
[[eq:tl5-hfg-sum]].

*The forms and the consequences.* In both expansions every term of N(h) carries at most two derivatives D̂ on its
solution factors, the expansions (ii)–(iv) do not increase this number, and the letters of I are distributed over
distinct factors; so the argument of [[lem:tl5-hf4-quadratic]] (a) applies: the orders of the solution factors of a
monomial add up to at most n + 2, and each is at most n + 1, the factor D̂²Ψ_I occurring only in the subtracted terms.
A solution factor is high, in the sense of [[lem:tl5-hf-quadratic]] (N ≥ 5) or of [[lem:tl5-hf4-quadratic]] (N = 4),
exactly when its order is at least N − 1. If N ≥ 5, two high factors would have orders adding up to at least 2N − 2 >
N + 2; so each monomial has at most one, and is bounded by ν 𝔰^(q−1) 𝔧 at p, which by [[eq:tl5-hfg-sum]] gives
[[eq:tl5-hf-g]] with 𝔠^⋆_n. If N = 4, two high factors have orders 3 and 3 and n = 4; with at most two derivatives D̂
and at most four letters they are D̂Ψ_B and D̂Ψ_(B′) with |B| = |B′| = 2, or Ψ_B and D̂²Ψ_Z with |B| = 3 and Z ∈ Γ, and
the other solution factors carry no letter and no derivative, so they are H or h, of norm at most 𝔰(p). With 𝔑^M_I the
sum of these monomials, each is bounded by ν 𝔰^(q−2) times one of the products whose squares are the terms of 𝔭_M²,
and the others by ν 𝔰^(q−1) 𝔧; [[eq:tl5-hfg-sum]] gives [[eq:tl5-hf4-g]] with 𝔠^⋆_n, and 𝔑^M_I = 0 if n ≤ 3. ∎

**Lemma {#lem:tl5-hfg-linfty}** (The low quantities, graded.) Let g be a solution of the reduced problem on D^κ_s, h :=
g − ĝ and p ∈ D^κ_s, with ϱ(p), η₀(p), k₂, C_S, C_(S,0), C_(0,0), C_(1,ϱ), 𝔯₀ and 𝔐 as in [[lem:tl5-hf-linfty]]. Put,
for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4,

    α_𝔄^(j) := √2 max_(|C|≤j) Σ_J ‖𝔄_CJ‖,
    k₁^(j) := (6/5) ((√3 + 8/3) K_rec (1 + √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + 𝔯₀ + (4/3) α_𝔄^(j)),
    k₃^⋆ := (8/5) max_(|C|≤N−1) (𝔠^⋆_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠^⋆_(|J|) + 1)),      𝔐^(m) := Σ_(j≤m+1) 7^j,
    C_∞^(m) := 2 max(2C_S, C₁^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_S, C₁^g)),
    C_(∞,ϱ)^(m) := 2 max(C_(1,ϱ), k₁^(m) (2𝔐^(m))^(1/2) C_(1,ϱ) + k₂),
    C_(∞,0)^(m) := 2 max(2C_(0,0), C_(1,0)^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_(0,0), C_(1,0)^g)),          {#eq:tl5-hfg-cinf}

with the maps of [[def:tl5-hf-coupling]] and their norms as in [[lem:tl5-hf-linfty]], C₁^g and C_(1,0)^g the constants
C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂ in place of Λ, Λ₂ evaluated at the points of the suprema in C₁^g and
C_(1,0)^g; so k₁^(N−1) = k₁, 𝔐^(N−4) = 𝔐 and k₃^⋆ ≤ k₃ when 𝔠^⋆_n ≤ 𝔠_n. None of these constants depends on μ. If
𝔰 ≤ 𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^⋆)) on Q(a, b), a := τ₁(p), b := τ₂(p), then for every μ ∈ (0, 1], at every
point of Q(a, b)

    M_g^(j) ≤ 2(k₁^(j) + 1) 𝒥_g + 2k₂ ϱ(p)      (0 ≤ j ≤ N − 1),                                         {#eq:tl5-hfg-m2}

and at p, for 0 ≤ m ≤ N − 4,

    𝔰_g^(m)(p) ≤ C_∞^(m)(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(m)(p) ϱ(p) + C_(∞,0)^(m)(p) η₀(p),               {#eq:tl5-hfg-linfty}

*Proof.* We follow the proof of [[lem:tl5-hf-linfty]], multiplying each bound by the weight of the quantity it bounds;
for N = 4 that proof applies as in [[lem:tl5-hf4-linfty]]. The bounds of [[lem:tl5-hf-quadratic]] it uses, for words of
length at most N − 1, hold with 𝔠^⋆ by [[lem:tl5-hfg-quadratic]], as 𝔰 ≤ 𝔰_♭ and, for N = 4, 𝔑^M_J = 0 for |J| ≤ 3; so
its inequalities hold with k₃^⋆ in place of k₃, and k₃^⋆ 𝔰 ≤ 1/2. By [[lem:tl5-hfg-quadratic]] the solution factors of a
monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J are H, Ψ_C or D̂Ψ_C with |C| ≤ |J|, or D̂²Ψ_C with |C| ≤ |J| − 1.

*Second derivatives.* Let q ∈ Q(a, b), j ≤ N − 1 and |C| ≤ j, and multiply the bound of [[lem:tl5-hf-recovery]] for Ψ_C,
as used in that proof, by μ^((|C|+1)/2). The words ZC have length |C| + 1, so μ^((|C|+1)/2) (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤
𝒥_g. The terms with D̂Ψ_C and Ψ_C, and those of the maps 𝔄_CJ, |J| ≤ |C|, are bounded by the multiples of 𝒥_g that bound
them by 𝒥₁ there, as μ^((|C|+1)/2) ≤ μ^(|J|/2), with α_𝔄^(j) in place of α_𝔄 as |C| ≤ j; the residual terms by k₂ ϱ(p),
as μ ≤ 1. In the nonlinear terms, each monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, has at most one high factor,
the others being at most 𝔰, and the factor Φ bounded by 𝔧 there satisfies μ^((|C|+1)/2) |Φ| ≤ 2𝒥_g + M_g^(j): for Φ = H
as |H| ≤ 2|h|, for Ψ_(C′) and D̂Ψ_(C′), |C′| ≤ |J|, as μ^((|C|+1)/2) ≤ μ^(|C′|/2), and for D̂²Ψ_(C′), |C′| ≤ |J| − 1 ≤ j,
as μ^((|C|+1)/2) ≤ μ^((|C′|+1)/2). Likewise μ^((|C|+1)/2) |H| |D̂²Ψ_J| ≤ 𝔰 M_g^(j) for |J| < |C|. So
μ^((|C|+1)/2) |D̂²Ψ_C| ≤ k₁^(j) 𝒥_g + k₂ ϱ(p) + k₃^⋆ 𝔰 (2𝒥_g + M_g^(j)), and taking the maximum over C, with k₃^⋆ 𝔰 ≤
1/2, M_g^(j)/2 ≤ (k₁^(j) + 1) 𝒥_g + k₂ ϱ(p).

*Zeroth order.* For |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] with A := Ψ_B involves the words JB, |J| ≤ 2, of length at
most |B| + 2, so μ^(|B|+2) Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂ ≤ ℰ_g(p); with μ ≤ 1 in the term on S_a, μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S
ℰ_g(p)^(1/2) + C_(0,0) η₀(p). And μ |H(p)| ≤ 2μ |h(p)|.

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] to A := D̂Ψ_B, as in that proof. For a word J of rotations
with |J| ≤ 2 the coefficients of the remainder R′ in ℒ^J A = D̂Ψ_(JB) + R′ carry at most two letters, so their norms and
those of their derivatives D̂ are at most Λ₂. The words JB have length at most |B| + 2 ≤ N − 1, and the factors Ψ_(C′) of
the remainders have |C′| ≤ |B| + 1, so the bounds |ℒ^J A| ≤ (1 + 6Λ) 𝒥₁ and |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁ there become
μ^((|B|+3)/2) |ℒ^J A| ≤ (1 + 6Λ₂) 𝒥_g and μ^((|B|+3)/2) |D̂ℒ^J A| ≤ M_g + 6√2 Λ₂ 𝒥_g. By [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], ∫_(Σ₁(a,b)) 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g(p), 𝔨₂ as in [[lem:tl5-hf-linfty]], and
[[eq:tl5-hfg-m2]] with j = N − 1 replaces the bound for M₂; the term on S_a is as there, with μ ≤ 1 and Λ₂ in place of Λ.
The argument of that proof then gives μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^g ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^g η₀(p).

*Second order at low levels.* Let |B| ≤ m and multiply the bound at p of that proof by μ^((|B|+4)/2). Its first-order
terms involve Ψ_C and D̂Ψ_C with |C| ≤ |B| + 1 ≤ m + 1 ≤ N − 3, which by the two previous steps are bounded with the
weights μ^((|C|+2)/2) and μ^((|C|+3)/2); so L is replaced by L_g := (Σ_(|C|≤m+1) (μ^(|C|+2) |Ψ_C|² +
μ^(|C|+3) |D̂Ψ_C|²))^(1/2) ≤ (2𝔐^(m))^(1/2) (max(C_S, C₁^g) ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)^g) η₀(p)),
there being 𝔐^(m) words of length at most m + 1, and k₁ by k₁^(m), as |B| ≤ m. Its nonlinear terms come from the words J
with |J| ≤ |B|: in each monomial the factor of largest order o ≤ |B| + 1 is H, Ψ_C or D̂Ψ_C with |C| ≤ |B|, or D̂²Ψ_C
with |C| ≤ |B| − 1, and in H^(αβ) D̂_αD̂_βΨ_J, |J| < |B|, the factor D̂²Ψ_J; each enters 𝔰_g^(m) with a weight at least
μ^((|B|+4)/2), and bounding it by 𝔰_g^(m) and the others by 𝔰 gives at most k₃^⋆ 𝔰(p) 𝔰_g^(m)(p) ≤ 𝔰_g^(m)(p)/2. So
μ^((|B|+4)/2) |D̂²Ψ_B(p)| ≤ k₁^(m) L_g + k₂ ϱ(p) + 𝔰_g^(m)(p)/2.

Taking the largest of the four bounds and absorbing 𝔰_g^(m)(p)/2 gives [[eq:tl5-hfg-linfty]]. ∎

**Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] suppose that
𝔰 ≤ 𝔰₀^⋆ on Q(a, b), and let I be a word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I
if N ≥ 5, 𝔑^L_I as in [[lem:tl5-hfg-quadratic]] if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2) and 𝔰_P := 𝔰_g^(m_P). Then at
every point of Q(a, b)

    μ^(n/2) |𝔑^L_I| ≤ 𝔠^⋆_n (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p)),
    μ^(n/2) |ℒ^J N(h)| ≤ (𝔠^⋆_(|J|) + 1) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p))      for |J| < n.     {#eq:tl5-hfg-products}

*Proof.* For a low solution factor Φ of order o put ℓ_P(Φ) := o + 2. For any solution factor Φ let ℓ_E(Φ) be 0 for
H and h, |C| − 1 for Ψ_C with |C| ≥ 1, |C| for D̂Ψ_C and |C| + 1 for D̂²Ψ_C. For every factor Φ of a monomial of
ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ n, and for Φ = D̂²Ψ_J with |J| < n,

    μ^(ℓ_E(Φ)/2) |Φ| ≤ 𝔨_g 𝒥_g + 2k₂ ϱ(p).                                                               (∗)

Indeed |H| ≤ 2|h| ≤ 2𝒥_g and |h| ≤ 𝒥_g; for Ψ_C = ℒ_Z Ψ_(C′) with |C| ≥ 1, by [[eq:tl5-hf-lie]], |Ψ_C| ≤ |Z| |D̂Ψ_(C′)| +
2|D̂Z| |Ψ_(C′)| ≤ 𝔷 (|D̂Ψ_(C′)|² + |Ψ_(C′)|²)^(1/2), so μ^((|C|−1)/2) |Ψ_C| ≤ 𝔷 𝒥_g, as |C′| = |C| − 1 ≤ N;
μ^(|C|/2) |D̂Ψ_C| ≤ 𝒥_g; and D̂²Ψ_C has |C| ≤ N − 1 by [[lem:tl5-hfg-quadratic]], so μ^((|C|+1)/2) |D̂²Ψ_C| ≤ M_g,
which [[eq:tl5-hfg-m2]] with j = N − 1 bounds.

Take a monomial of 𝔑^L_I, with solution factors of orders o_i, q ≥ 2 of them; by [[lem:tl5-hfg-quadratic]] it has at
most one high factor, and at most one factor is a second derivative, as there are at most two derivatives D̂ on the
solution factors. Let Φ₂ be the high factor if there is one; otherwise a factor D̂²Ψ_C if there is one; and otherwise a
factor of largest order. Let Φ₁ be another factor, not a second derivative if there is such a choice. By
[[lem:tl5-hfg-quadratic]], o₁ + o₂ ≤ n + 2 and o₂ ≤ n + 1. If o₂ ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1; if o₂ = 0, Φ₂ is neither high
nor a second derivative, so all factors have order 0 and o₁ = 0. In both cases

    ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3,      ℓ_E(Φ₂) ≤ n.                                                      {#eq:tl5-hfg-count}

Φ₁ is low. If Φ₁ = D̂²Ψ_B, then Φ₂ is high and not a second derivative, and it is not D̂Ψ_C either, as the derivatives D̂
would then number three; so Φ₂ = Ψ_C with |C| ≥ N − 1, every other factor would offer another choice, so q = 2, and |B| +
2 + N − 1 ≤ o₁ + o₂ ≤ N + 2 gives |B| ≤ 1; with |B| ≤ N − 4, as Φ₁ is low, |B| ≤ m_P. So Φ₁ is one of the quantities of
𝔰_P, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P. With |Φ_i| ≤ 𝔰 ≤ 1 for the other factors, (∗) for Φ₂, and |Φ₁| bounded by
μ^(−ℓ_P(Φ₁)/2) 𝔰_P in the term with 𝒥_g and by 𝔰 in the term with ϱ(p), the monomial times μ^(n/2) is at most ν 𝔰^(q−2)
times

    μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔨_g 𝔰_P 𝒥_g + μ^((n − ℓ_E(Φ₂))/2) 2k₂ 𝔰 ϱ(p) ≤ μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p),

ν its background norm with the coefficient. By [[eq:tl5-hfg-sum]] this gives the first inequality. For |J| < n,
ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J, and 𝔑_J = 𝔑^L_J also for N = 4, as |J| ≤ 3; the first inequality for J, with
μ^(n/2) ≤ μ^(|J|/2), bounds μ^(n/2) |𝔑_J|. In the last term ℓ_P(H) = 2, H is a quantity of 𝔰_P, ℓ_E(D̂²Ψ_J) = |J| + 1
≤ n and 2 + |J| + 1 ≤ n + 2; the same splitting bounds μ^(n/2) |H| |D̂²Ψ_J| by μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p). ∎

**Lemma {#lem:tl5-hfg-mixed}** (The products of level four, graded.) Let N = 4, and let g, h, t, b, Σ, ϱ and η₀ be as
in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b). With the notation of that lemma, whose λ_t = 2([k₁]_t + 1) is not
one of the bounds λ_k, 𝔍_g := ‖𝒥_g‖_Σ and

    𝔛_t^g := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ̄₂]_t),
                 (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),

    μ^(7/2) ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔛_t^g 𝔜_t (𝔍_g + ϱ) (𝔍_g + ϱ + η₀),
    𝔍_g² ≤ [𝔨₂]_t Σ_(|I|≤4) μ^|I| ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                          {#eq:tl5-hfg-mixed}

*Proof.* The second inequality follows from [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], as in the proof of
[[lem:tl5-hf4-mixed]]. By [[eq:tl5-hfg-m2]] with j = 3 at the points of Σ, ‖M_g‖_Σ ≤ λ_t 𝔍_g + ς_t ϱ. In the proof of
[[lem:tl5-hf4-mixed]], ‖𝔭_M‖_Σ² ≤ e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²); we bound μ² X₁, μ² X₂, μ^(3/2) Y₁ and
μ^(3/2) Y₂. The coefficients of the remainders R′ and R there belong to words J of rotations with |J| ≤ 2, so they and
the products of two of them are at most [Λ₂]_t and [Λ̄₂]_t on Σ.

*μ² X₁.* The factors of Σ_B Σ_J |ℒ^J D̂Ψ_B|² there are D̂Ψ_(JB), |JB| ≤ 4, and Ψ_C, |C| ≤ 3, and μ⁴ ≤ μ^(|JB|), μ^(|C|);
so μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2 · 49 · 1320 [Λ₂]_t² 𝒥_g², and μ² X₁ ≤ (𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2) 𝔍_g.

*μ² X₂.* The factors of Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² there are D̂²Ψ_(JZ), |JZ| ≤ 3, with μ² ≤ μ^((|JZ|+1)/2), and D̂Ψ_C, Ψ_C
with |C| ≤ 2; so μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 621516 [Λ̄₂]_t² 𝒥_g², and μ² X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602
‖M_g‖_Σ + 789 [Λ̄₂]_t 𝔍_g).

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* In the bounds of Y₁² and Y₂² there, μ³ Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M_g², μ³ Σ_(|B|=2) |D̂Ψ_B|²
≤ 𝒥_g², μ³ Σ_(|B|=3) (|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², and μ³ ≤ 1 in the terms with η₀; so

    μ³ Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍_g² + 49 ‖M_g‖_Σ²),      μ³ Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍_g².

As there, μ² X_i ≤ 𝔛_t^g (𝔍_g + ϱ) and μ^(3/2) Y_i ≤ 𝔜_t (𝔍_g + ϱ + η₀) for i = 1, 2, and μ^(7/2) (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ μ² X₁ μ^(3/2) Y₁ + μ² X₂ μ^(3/2) Y₂ gives the first inequality. ∎

**Definition {#def:tl5-hfg-constants}** (The sharpened constants.) Let N ≥ 5 and the setting be that of
[[def:tl5-hf-constants]], or N = 4 and the setting that of [[def:tl5-hf4-constants]], with δ_w, ϰ₀, 𝔰_θ, ϱ and η₀ as
there and 𝒮 of [[eq:tl5-hf-source]] for a = u*, b = v*. With the constants of [[lem:tl5-hfg-linfty]] and
[[lem:tl5-hfg-products]], C_P := C_∞^(m_P), C_(P,ϱ) := C_(∞,ϱ)^(m_P) and C_(P,0) := C_(∞,0)^(m_P), put

    𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^⋆)),      𝔰₁^⋆ := min(𝔰₀^⋆/2, c_* κ_m/2, 𝔰_θ),
    𝔤_(N,g) := (Σ_(j≤N) (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^⋆_(j′) + 1))²)^(1/2),
    𝔞_(o,g) := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c) + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    𝔞_(i,g) := ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖ + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    S_(F,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) C_P e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) C_P e^(φ/2)) dt),
    𝔯_(w,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) (C_(P,ϱ) ϱ + C_(P,0) η₀)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) (C_(P,ϱ) ϱ + C_(P,0) η₀)) dt),
    ε_(w,g) := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ],

the functions of p being evaluated at the point of the supremum. For N = 4 put, with the notation of
[[lem:tl5-hf4-mixed]] and [[lem:tl5-hfg-mixed]] and with [𝔠^⋆₄]_t the number 𝔠^⋆₄ formed with the suprema over
Σ₁(t, v*) of the Λ_k, the Λ^R_k and the λ_k,

    m_t^g := 98 e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t [𝔠^⋆₄]_t 𝔪(t) 𝔛_t^g 𝔜_t,
    S_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t^g [𝔨₂]_t dt,
    𝔯_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t^g [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_(M,g) := μ^(−3/2) ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t^g dt,

the graded triple, or let S_(M,g), 𝔯_(M,g) and ε_(M,g) be S_M, 𝔯_M and ε_M of [[def:tl5-hf4-constants]] with m_t^g in
place of m_t, the ungraded triple, the same triple throughout; for N ≥ 5 let S_(M,g) = 𝔯_(M,g) = ε_(M,g) := 0. Finally

    A_g := √2 δ_w + 2ε_(w,g) + 2ε_(M,g),      B_g := 2 (S_(F,g) + S_(M,g)),      𝔯_g := 𝔯_(w,g) + 𝔯_(M,g),
    𝔰_(*,g) := sup_(p∈D^κ) (2 C_∞^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_g
               + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀).                                    {#eq:tl5-hfg-constants}

**Proposition {#prop:tl5-hfg-bootstrap}** (The a priori estimate with the sharpened constants.) In the setting of
[[def:tl5-hfg-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N) and that

    𝔯_g ≤ 1/4,      η₀ < 𝔰₁^⋆,      𝔰_(*,g) < 𝔰₁^⋆.                                               {#eq:tl5-hfg-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_g for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,g) on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_g + B_g Y_s(g)².                                                                          {#eq:tl5-hfg-h1}

*Proof.* *Step 1.* As in the first paragraph and Step 1 of the proof of [[prop:tl5-hf-bootstrap]], with 𝔰₀^⋆, 𝔰₁^⋆
and A_g in place of 𝔰₀, 𝔰₁ and A_w, and with [[eq:tl5-hfg-linfty]] for m = N − 4 and μ = 1 in place of
[[eq:tl5-hf-linfty]]: if 𝔰 ≤ 𝔰₀^⋆ on D^κ_σ and p ∈ D^κ_σ, then ℰ⁰_N(p) ≤ μ^(−N) e^(φ(p)) Y_σ(g)² ≤ 4μ^(−N) e^(φ(p)) A_g²,
so 𝔰(p) ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤
𝔰₀^⋆/2. That argument gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ on D^κ_s, |h|_k̂ < κ_m/2 by [[lem:tl5-hf-conversions]] (a), and
θ_H ≤ ϑ. So [[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]] and [[lem:tl5-hfg-products]] apply at every point of
D^κ_s, and their ϱ(p) and η₀(p) are at most the ϱ and η₀ of [[def:tl5-hfg-constants]].

*Step 2.* Step 2 of the proof of [[prop:tl5-hf-bootstrap]] (for N = 4, of the proof of [[prop:tl5-hf4-bootstrap]])
holds up to the bound of the nonlinear terms, which we replace as follows. The nonlinear terms of L̂Ψ_I +
H^(αβ) D̂_αD̂_βΨ_I other than 𝔑^M_I are −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I, and 𝔔_IJ ≠ 0 with J ≠ I only for |J| < |I|. By
[[eq:tl5-hfg-products]], by the definition of 𝔮_(jj′) and the Cauchy–Schwarz inequality over the 7^(j′) words of each
length j′ ≤ |I| ([[def:tl5-hf-coupling]]), the family of these terms over |I| = j has norm at most

    μ^(−j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^⋆_(j′) + 1) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ),

with 𝔮_(jj) = 1. As for the forcing terms in the proof of [[prop:tl5-hf-linear-n]], with the weights μ^|I| and the
Cauchy–Schwarz inequality over j, their contribution to the bulk is at most 2Ω̂² 𝔤_(N,g) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g +
2k₂ 𝔰 ϱ)(√e_o + √c √e_i), e_o and e_i being the weighted sums. By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ (1/z̲ + 1/c) e_o +
e_i, so, with √e_o + √c √e_i ≤ √2 (e_o + e_i)^(1/2), 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2) (e_o + e_i);
and 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ, as 𝔰 ≤ 1/8. By (a) of [[lem:tl5-hf-quasilinear]], with |D̂H| = |g⁻¹ (D̂h) g⁻¹| ≤ 𝔤₀² |D̂h| ≤
𝔤₀² μ^(−3/2) 𝔰_P, |H| ≤ μ^(−1) 𝔰_P ≤ μ^(−3/2) 𝔰_P and |D̂Ψ|² ≤ (e_o/c + e_i)/(2Ω̂²) for each field, the weighted sum of
2Ω̂² |𝔮_H| is at most μ^(−3/2) 𝔰_P times the first two terms of 𝔞_(o,g) e_o + 𝔞_(i,g) e_i. For N = 4 the terms 𝔑^M_I
are bounded as in the proof of [[prop:tl5-hf4-bootstrap]], with [[eq:tl5-hf4-g]] for 𝔠^⋆₄ and [[lem:tl5-hfg-mixed]] in
place of [[lem:tl5-hf4-mixed]]: the factors there become 49 [𝔠^⋆₄]_t ‖𝔭_M‖_Σ and at most μ^(−2) Y_s, and 𝔍_g ≤
[𝔨₂]_t^(1/2) Y_s, so the term is at most ∫_(−10)^(u*) m_t^g μ^(−3/2) (𝔍_g + ϱ)(𝔍_g + ϱ + η₀) Y_s dt ≤ S_(M,g) Y_s³ +
𝔯_(M,g) Y_s² + ε_(M,g) Y_s for the graded triple. For the ungraded triple, [[lem:tl5-hfg-mixed]] with μ = 1, where
𝔍_g = 𝔍, gives the first inequality of [[eq:tl5-hf4-mixed]] with 𝔛_t^g in place of 𝔛_t, and the argument of the
proof of [[prop:tl5-hf4-bootstrap]], with [𝔠^⋆₄]_t in place of [𝔠₄]_t, bounds the term by S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² +
ε_(M,g) Y_s. Hence the bulk of the weighted sum over I is at most

    ∫ e^(−φ) (2Ω̂² (s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ)(√e_o + √c √e_i) + μ^(−3/2) 𝔰_P (𝔞_(o,g) e_o + 𝔞_(i,g) e_i)) dμ du dv

plus, for N = 4, S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² + ε_(M,g) Y_s.

*Step 3.* Step 3 of that proof applies with μ^(−3/2) 𝔰_P in place of 𝔰: by [[eq:tl5-hfg-linfty]] for m = m_P, as
ℰ_g(p) ≤ e^(φ(p)) Y_s², φ being at most φ(p) on Σ₁(τ₁(p), τ₂(p)), 𝔰_P ≤ C_P e^(φ/2) Y_s + C_(P,ϱ) ϱ + C_(P,0) η₀ at
every point; so for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,g) + ε_(M,g)) + 𝔯_g Y_s² + (S_(F,g) + S_(M,g)) Y_s³,

and with ϑ ≤ 1/4 and 𝔯_g ≤ 1/4 the conclusion follows as there. ∎

**Theorem {#thm:tl5-hfg}** (Existence close to an explicit background, with the sharpened constants.) In the setting
of [[thm:tl5-hf]] (N ≥ 6) let the bounds Λ_k, Λ^R_k, λ_k, the number 𝔰_♭ and the choice of 𝔠^⋆ be as in
[[def:tl5-hfg-graded]], and suppose:

(a) the quantity η₀ of [[def:tl5-hf-constants]] satisfies η₀ < 𝔰₁^⋆;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N);

(c) the constants of [[def:tl5-hfg-constants]] satisfy 𝔯_(w,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁^⋆ and the closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g)) S_(F,g) < 1.                                                  {#eq:tl5-hfg-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_g and 𝔰_(*,g) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]], [[eq:tl5-hfg-h1]] and
[[eq:tl5-hfg-closing]] in place of A_w, B_w, [[prop:tl5-hf-bootstrap]], [[eq:tl5-hf-h1]] and [[eq:tl5-hf-closing]].
For (H2), the proof of [[lem:tl5-hf-persistence]] uses [[prop:tl5-hf-bootstrap]] only through its conclusion 𝔰 ≤ 𝔰_*
on D^κ_s, which gives |H| ≤ 1/8 and θ_H ≤ ϑ, and through the bound Y_σ ≤ 2A_w; [[prop:tl5-hfg-bootstrap]] gives
𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤ min(1/16, 𝔰_θ) under Y_σ ≤ 2A_g, so that proof gives (H2) with A_g in place of A_w. The bound
for ε is [[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_(*,g). ∎

**Theorem {#thm:tl5-hf4g}** (Level four, with the sharpened constants.) In the setting of [[thm:tl5-hf4]] let the
bounds Λ_k, Λ^R_k, λ_k, the number 𝔰_♭ and the choice of 𝔠^⋆ be as in [[def:tl5-hfg-graded]] with N = 4, and suppose:

(a) the quantity η₀ of [[def:tl5-hf4-constants]] satisfies η₀ < 𝔰₁^⋆;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴);

(c) the constants of [[def:tl5-hfg-constants]] with N = 4 satisfy 𝔯_(w,g) + 𝔯_(M,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁^⋆ and the
closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g) + 2ε_(M,g)) (S_(F,g) + S_(M,g)) < 1.                          {#eq:tl5-hf4g-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_g and 𝔰_(*,g) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]] for N = 4,
[[eq:tl5-hfg-h1]] and [[eq:tl5-hf4g-closing]] in place of A_(w,4), B_(w,4), [[prop:tl5-hf4-bootstrap]],
[[eq:tl5-hf4-h1]] and [[eq:tl5-hf4-closing]]. For (H2), the proof of [[lem:tl5-hf4-persistence]] uses
[[prop:tl5-hf4-bootstrap]] only through its conclusion 𝔰 ≤ 𝔰_* on D^κ_s, which gives |H| ≤ 1/8 and θ_H ≤ ϑ, through
the bound Y_σ ≤ 2A_(w,4) and through [[eq:tl5-hf4-m2]], which holds by [[eq:tl5-hfg-m2]] with μ = 1 and j = 3;
[[prop:tl5-hfg-bootstrap]] gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤ min(1/16, 𝔰_θ) under Y_σ ≤ 2A_g. The bound for ε is
[[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_(*,g). ∎

**Remark {#rem:tl5-hfg-powers}** (What the sharpened constants contain.) In S_(F,g) and 𝔯_(w,g), and with the graded
triple in S_(M,g), 𝔯_(M,g) and ε_(M,g), the only power of μ is μ^(−3/2), at every level N ≥ 4, against μ^(−N) in S_F
and μ^(−2) in S_M of [[thm:tl5-hf]] and [[thm:tl5-hf4]]: for given rates,
𝔤_(N,g), 𝔨_g, 𝔞_(o,g), 𝔞_(i,g), C_P, C_(P,ϱ), C_(P,0) and m_t^g do not depend on μ. If 𝔠^⋆_n = 𝔠_n, then 𝔤_(N,g) is the
value at μ = 1 of 𝔤_N of [[def:tl5-hf-constants]], and the weights μ^j of 𝔤_N give 𝔤_N ≤ 𝔤_(N,g) ≤ μ^(−N/2) 𝔤_N; so
ε_(w,g) ≥ ε_w, and in S_F and 𝔯_w these weights offset part of the powers μ^(−N) and μ^(−N/2). The power μ^(−3/2)
is that of the count
[[eq:tl5-hfg-count]], which gives exactly n + 3 for the term D̂Ψ_B · D̂Ψ_(B′) of 2𝔮 with |B| + |B′| = n and |B| ≤ N − 3:
D̂Ψ_B is bounded at a point through the energies of level |B| + 3, and D̂Ψ_(B′) through those of level |B′|. The
smallness 𝔰_(*,g) < 𝔰₁^⋆ keeps the factor μ^(−N/2): it bounds the unweighted 𝔰, which the absorption in the recovery of
second derivatives and the hypothesis of [[lem:tl5-hfg-quadratic]] require, and whose quantities of order N − 2 are
bounded through the energies of level N only.

The recovery constant of the highest level, k₁ = k₁^(N−1), enters S_(F,g) through 𝔨_g and through C₁^g in C_P; in C_P
it is otherwise replaced by k₁^(m_P), which involves the couplings 𝔄_CJ with |C| ≤ 1 only, and for N = 4 none, as
𝔄_∅J = 0 by [[def:tl5-hf-coupling]]; and 𝔐^(m_P) = 57 for N ≥ 5 and 8 for N = 4, against 𝔐 = Σ_(j≤N−3) 7^j. The
smallness constants C_∞^(N−4), C_(∞,ϱ)^(N−4) and C_(∞,0)^(N−4) contain k₁^(N−4) in place of the k₁ of the third entry
of C_∞. The background bounds enter graded: 𝔠^⋆_n through Λ_k, Λ^R_k and λ_k with k ≤ n, C₁^g, C_(1,0)^g and 𝔛_t^g
through Λ₂ only.
If π^Z = 0 for every Z ∈ Γ, as for the seed, then ℒ^K ĝ⁻¹ = 0 and ℒ^K R̂ = 0 for K ≠ ∅, the choices Λ_k = λ_k = 0 for
k ≥ 1, Λ^R_0 = |R̂| and Λ^R_k = 0 for k ≥ 1 are admissible, and

    𝔠^Q_n = (81 + 5|R̂|) 2^n − 1,

the number of distributions of n letters over the two solution factors of each quadratic term, 2^n, times the norms of
its coefficients, less 1 for the subtracted term. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
[[thm:tl5-hfg]] and [[thm:tl5-hf4g]] are established in this paper for no background at 10 l5. [[sec:tl5-hfs]]
sharpens these constants a second time ([[thm:tl5-hfs]], [[thm:tl5-hf4s]]).

### The constants sharpened a second time {#sec:tl5-hfs}

This section sharpens the constants of [[sec:tl5-hfg]] further and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with them.
Four changes are made, each a proved restatement. First, every background factor is bounded by a bound of its own order,
also inside the iterated Lie derivatives of ĝ⁻¹, of g⁻¹, of D̂h and of D̂²h, so that in every product of bounds the
orders add up to at most the number of letters of the term ([[def:tl5-hfs-bounds]], [[lem:tl5-hfs-quadratic]]). Second,
the letters that a quadratic term of level n places on
background factors cost no power of μ: a term whose background factors carry b letters is bounded with the factor
μ^((b−3)/2), and the forcing of level j′ in the equation of level j keeps the weight μ^((j−j′)/2)
([[lem:tl5-hfs-products]]). Third, the recovery of second derivatives keeps the weights of the levels it couples, so
its constant k₁ becomes k₁^(j,μ), and the top-level recovery constant enters each quadratic term once: a term whose
factor in the energies is a second derivative has no derivative on the factor at a point ([[lem:tl5-hfs-linfty]],
[[lem:tl5-hfs-products]]). Fourth, at level four the products with no factor at a point are summed over the words
before the Hölder inequality, which removes the word count and the coefficient 𝔠₄ from their terms of second order, the
terms of higher order keeping 49 𝔰_♭ 𝔠^(3♮)₄ ([[lem:tl5-hfs-quadratic]], [[lem:tl5-hfs-mixed]]).
The closing conditions are [[eq:tl5-hfs-closing]] and [[eq:tl5-hf4s-closing]]; those of [[thm:tl5-hf]],
[[thm:tl5-hf4]], [[thm:tl5-hfg]] and [[thm:tl5-hf4g]] remain valid, and any of them may be used. Throughout, N ≥ 4,
μ ∈ (0, 1], the notation is that of [[sec:tl5-hfg]] with the second expansion of [[def:tl5-hfg-graded]], and for N = 4
the quantities 𝔰, 𝔧 and 𝔭_M are those of [[def:tl5-hf4-levels]].

**Definition {#def:tl5-hfs-bounds}** (Bounds of their own order.) Let Λ_k, Λ^R_k (0 ≤ k ≤ N) and 𝔰_♭ ∈ (0, 1/8] be as
in [[def:tl5-hfg-graded]], and put 𝔤₁ := 1 + 2𝔰_♭. For 1 ≤ k ≤ N let A(k) be the set of the finite sequences a = (a₁,
…, a_r) of positive integers with a₁ + ⋯ + a_r = k, and put, with the binomial coefficients C(·, ·),

    λ^♮_k := Σ_(a∈A(k)) (k!/(a₁! ⋯ a_r!)) Λ_(a₁) ⋯ Λ_(a_r),
    b^♮_g(k) := Σ_(a∈A(k)) (k!/(a₁! ⋯ a_r!)) 𝔤₁^(r+1) (Λ_(a₁) + 1) ⋯ (Λ_(a_r) + 1),
    β₁^♮(k) := 1 + 2 Σ_(j=1)^k C(k, j) Λ_j,
    β₂^♮(k) := 1 + Σ_(l=1)^k Σ_(j=1)^l C(l − 1, j − 1) Λ_j (7 + 10 Σ_(i=1)^(l−j) C(l − j, i) Λ_i),

r being the length of a, and λ^♮₀ := 1, λ̂^♮₀ := √5, λ̂^♮_k := λ^♮_k (k ≥ 1), b^♮_g(0) := 𝔤₀, β₁^♮(0) := β₂^♮(0) := 1.
With Σ^m_n of [[def:tl5-hfg-graded]] put

    𝔠^(2♮)_n := Σ⁴_n λ^♮_(k₁) λ^♮_(k₃) β₂^♮(k₄) − 1 + 5 Σ⁵_n λ^♮_(k₁) λ^♮_(k₃) Λ^R_(k₄)
                + 16 Σ⁴_n λ̂^♮_(k₁) λ̂^♮_(k₂) β₁^♮(k₃) β₁^♮(k₄),
    𝔠^(3♮)_n := Σ⁶_n b^♮_g(k₁) λ^♮_(k₃) λ^♮_(k₅) β₂^♮(k₆) − 𝔤₀ + 5 Σ⁷_n b^♮_g(k₁) λ^♮_(k₃) λ^♮_(k₅) Λ^R_(k₆)
                + 16 Σ⁶_n b^♮_g(k₁) λ^♮_(k₃) (b^♮_g(k₄) + λ̂^♮_(k₄)) β₁^♮(k₅) β₁^♮(k₆),                  {#eq:tl5-hfs-cn}

and 𝔠^♮_n := 𝔠^(2♮)_n + 𝔰_♭ 𝔠^(3♮)_n. For ν ∈ (0, 1] let 𝔠^♮_n(ν) be 𝔠^♮_n formed with ν^(a/2) Λ_a and ν^(a/2) Λ^R_a in
place of Λ_a and Λ^R_a for every a, the other numbers being formed from these; so 𝔠^♮_n(1) = 𝔠^♮_n, and λ^♮_k is
replaced by ν^(k/2) λ^♮_k. For 0 ≤ j ≤ N − 1, with the notation of [[lem:tl5-hf-linfty]] and [[lem:tl5-hfg-linfty]],
put

    α_𝔄^(j,μ) := √2 max_(|C|≤j) Σ_J μ^((|C|+1−|J|)/2) ‖𝔄_CJ‖,
    k₁^(j,μ) := (6/5) ((√3 + 8/3) K_rec (1 + μ^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + μ^(1/2) 𝔯₀
                + (4/3) α_𝔄^(j,μ)),      k₁^μ := k₁^(N−1,μ),      Λ₂^μ := max(μ Λ₁, μ^(3/2) Λ₂),

the sum over the words J with |J| ≤ |C|, and

    𝔰_P⁰ := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2)).

So k₁^(j,1) = k₁^(j), and k₁^(j,μ) ≤ k₁^(j). The number λ^♮_k is the norm bound of ℒ^K ĝ⁻¹, |K| = k, that the
expansion of the proof of [[lem:tl5-hf-quadratic]] (iv) gives when each factor ℒ^B ĝ is bounded by Λ_(|B|) and each
factor ĝ⁻¹ by 1; λ_k := λ^♮_k is admissible in [[def:tl5-hfg-graded]], by [[lem:tl5-hfs-quadratic]] (a).

**Lemma {#lem:tl5-hfs-quadratic}** (The quadratic terms with bounds of their own order.) Let h be as in
[[def:tl5-hfg-graded]], p a point with 𝔰(p) ≤ 𝔰_♭, and I a word with n := |I| ≤ N.

(a) For words J, K with |J| = |K| = k at p: ℒ^J D̂h − D̂Ψ_J is a sum of monomials, each the contraction of one factor
ℒ^B Γ′[π^Z] with one Ψ_C, of which 2C(k, j) have a factor carrying j letters; ℒ^J D̂²h − D̂²Ψ_J is a sum of monomials
of total background norm at most β₂^♮(k) − 1; |ℒ^K ĝ⁻¹| ≤ λ^♮_k; and ℒ^K g⁻¹ is a sum of monomials of total background
norm at most b^♮_g(k). In each monomial the background factors carry disjoint letters, and the norm of the background
part is a product of the bounds Λ_a of its factors, a the number of letters each carries, and of numbers that carry no
letter (𝔤₀, 𝔤₁, the counts).

(b) In the second expansion of the proof of [[lem:tl5-hfg-quadratic]], ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I is a sum of
monomials with q ≥ 2 solution factors whose orders add up to at most n − b + 2, b the number of letters carried by the
background factors of the monomial, and whose background norms ν, with the coefficients, satisfy for every ν′ ∈ (0, 1]

    Σ ν ν′^(b/2) 𝔰(p)^(q−2) ≤ 𝔠^♮_n(ν′).                                                                {#eq:tl5-hfs-sum}

(c) For N = 4 and |I| = 4 let 𝔑^M_I be as in [[lem:tl5-hfg-quadratic]] for the second expansion, and put P₁² :=
Σ_(|B|=|B′|=2) |D̂Ψ_B|² |D̂Ψ_(B′)|² and P₂² := Σ_(|B|=3) Σ_(Z∈Γ) |Ψ_B|² |D̂²Ψ_Z|², so that 𝔭_M² = P₁² + P₂². Then at p

    𝔠^M₁ := 480 + 49 𝔰_♭ 𝔠^(3♮)₄,      𝔠^M₂ := 4 + 49 𝔰_♭ 𝔠^(3♮)₄,
    (Σ_(|I|=4) |𝔑^M_I|²)^(1/2) ≤ 𝔠^M₁ P₁ + 𝔠^M₂ P₂.                                                       {#eq:tl5-hfs-m}

*Proof.* (a) By [[eq:tl5-hf-lie-d]] and induction on k, ℒ^J D̂h = D̂Ψ_J − Σ_(l=1)^k Σ_S (ℒ^(Z_S) Γ′[π^(Z_l)]) ⋆
Ψ_(J(l,S)), the inner sum over S ⊂ {1, …, l − 1}, Z_S the subword with indices in S, J(l, S) the word J with the letters
of S and Z_l deleted, and ⋆ the contraction of [[eq:tl5-hf-lie-d]], which has two terms on a 2-tensor and commutes with
Lie derivatives, as it involves no metric. The factor ℒ^(Z_S) Γ′[π^(Z_l)] carries j = |S| + 1 letters, and Σ_l 2C(l − 1,
j − 1) = 2C(k, j). Next, ℒ_Z D̂²A = D̂² ℒ_Z A + [ℒ_Z, D̂²]A, so ℒ^J D̂²h = D̂²Ψ_J + Σ_(l=1)^k ℒ^(Z₁⋯Z_(l−1)) ([ℒ_(Z_l),
D̂²] Ψ_(Z_(l+1)⋯Z_k)), and [ℒ_Z, D̂²]Ψ consists, by (iii) of the proof of [[lem:tl5-hf-quadratic]], of five contractions
of Γ′[π^Z] with D̂Ψ and two of D̂Γ′[π^Z] with Ψ. By Leibniz's rule the coefficient receives j − 1 of the letters Z₁, …,
Z_(l−1), in C(l − 1, j − 1) ways, and carries j letters; the solution factor receives the other l − j, and ℒ^T Ψ_C =
Ψ_(TC), while ℒ^T D̂Ψ_C − D̂Ψ_(TC) has, as just shown, 2C(l − j, i) monomials whose coefficient carries i letters. So the
background norms add up to at most Σ_l Σ_j C(l − 1, j − 1) Λ_j (2 + 5(1 + 2 Σ_i C(l − j, i) Λ_i)) = β₂^♮(k) − 1. By (iv)
of that proof with h = 0, ℒ^K ĝ⁻¹ = Σ (−1)^r ĝ⁻¹ (ℒ^(B₁) ĝ) ĝ⁻¹ ⋯ (ℒ^(B_r) ĝ) ĝ⁻¹, the sum over the ordered sequences of
disjoint nonempty subwords B_i of K covering K; there are k!/(a₁! ⋯ a_r!) of them with |B_i| = a_i. Each ℒ^(B_i) ĝ =
ℒ^(B′) π^Z, B_i = (B′, Z), carries a_i letters, so its norm is at most Λ_(a_i); in the frame F, where ĝ^MN = η^MN, each
factor ĝ⁻¹ joins indices of two distinct factors or raises a free index, which by the Cauchy–Schwarz inequality costs the
factor 1. This gives |ℒ^K ĝ⁻¹| ≤ λ^♮_k. For g⁻¹ the same expansion holds with g⁻¹ and ℒ^(B_i) g = ℒ^(B_i) ĝ + Ψ_(B_i), of
norm sum at most Λ_(a_i) + 1, the second part a solution factor carrying the letters of B_i; and a factor g⁻¹ = ĝ⁻¹ + H
joining two factors or raising an index costs at most 1 + |H| ≤ 1 + 2𝔰 ≤ 𝔤₁, by [[lem:tl5-wg-norms]] (a). This gives
b^♮_g(k).

(b) The second expansion of the proof of [[lem:tl5-hfg-quadratic]] distributes the letters of I over the factors of the
terms of Q and R₃ by Leibniz's rule, and expands ℒ^J D̂h, ℒ^J D̂²h, ℒ^J g⁻¹ and ℒ^K ĝ⁻¹ as in (a). By (a), a monomial
whose background factors carry b letters has a background norm that is a product of bounds Λ_a and Λ^R_a with the a
adding up to b, times numbers carrying no letter; replacing each Λ_a and Λ^R_a by ν′^(a/2) Λ_a and ν′^(a/2) Λ^R_a
multiplies it by ν′^(b/2). The counts of that proof, with the bounds of (a) in place of β₁^g, β₂^g, b_g^g and λ_k, give
[[eq:tl5-hfs-sum]], the terms of Q having q = 2 and those of R₃ q ≥ 3. The order of a solution factor is the number of
its letters plus the number of its derivatives D̂; the solution factors of a monomial carry the n − b letters not on
background factors, disjointly, and at most two derivatives D̂, as in [[lem:tl5-hf4-quadratic]] (a).

(c) Of the monomials of 𝔑^M_I, two high factors carry all four letters, so b = 0. Those of Q are, by the argument of
[[lem:tl5-hfg-quadratic]], the monomials of H₁^(λσ) D̂_λD̂_σ h with three letters, in the positions S ⊂ {1, 2, 3, 4}, on
h and one on D̂²h, which are bounded by |Ψ_(I_S)| |D̂²Ψ_(I_(S^c))| with coefficient λ^♮₀² = 1, I_S the subword of I in
the positions S; and the monomials of 2𝔮̂ with two letters on each factor D̂h, bounded by 16
λ̂^♮₀² |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))| = 80 |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))|, |S| = 2. For fixed S the map I ↦ (I_S, I_(S^c)) is a
bijection from the words of length 4 onto the pairs of words of lengths |S| and 4 − |S|; so, by Minkowski's inequality
over the six sets S with |S| = 2 and the four with |S| = 3, these monomials contribute at most 6 · 80 P₁ + 4 P₂ to the
left side of [[eq:tl5-hfs-m]]. Each monomial of R₃ in 𝔑^M_I is bounded by ν 𝔰^(q−2) times one of the products whose
squares are the terms of 𝔭_M², with Σ ν 𝔰^(q−2) ≤ 𝔰_♭ 𝔠^(3♮)₄ over them by (b); as there are 7⁴ = 49² words of length 4,
they contribute at most 49 𝔰_♭ 𝔠^(3♮)₄ 𝔭_M ≤ 49 𝔰_♭ 𝔠^(3♮)₄ (P₁ + P₂). ∎

Since Λ_(a_i) ≤ Λ_k, 𝔤₁ ≤ 𝔤₀ and r ≤ k, and the number of the ordered sequences in (a) with r blocks is r! S(k, r),
λ^♮_k, b^♮_g(k), β₁^♮(k) and β₂^♮(k) are at most the numbers λ_k (with the admissible choice of
[[def:tl5-hfg-graded]]), b_g^g(k), β₁^g(k) and β₂^g(k); so 𝔠^♮_n ≤ 𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n.

**Lemma {#lem:tl5-hfs-linfty}** (The low quantities with the weights kept.) Let g, h, p, a, b, ϱ(p) and η₀(p) be as in
[[lem:tl5-hfg-linfty]], let k₃^♮ be k₃^⋆ of [[eq:tl5-hfg-cinf]] with 𝔠^♮_n in place of 𝔠^⋆_n, 𝔰₀^♮ := min(𝔰_♭, 1/(2
sup_(Q(a,b)) k₃^♮)), and C₁^♮ and C_(1,0)^♮ the constants C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂^μ in place of
Λ and k₁^μ in place of k₁, Λ₂^μ evaluated at the points of their suprema. Let C_(∞,μ)^(m), C_((∞,ϱ),μ)^(m) and
C_((∞,0),μ)^(m) be the constants C_∞^(m), C_(∞,ϱ)^(m) and C_(∞,0)^(m) of [[eq:tl5-hfg-cinf]] with k₁^(m,μ), C₁^♮ and
C_(1,0)^♮ in place of k₁^(m), C₁^g and C_(1,0)^g. If 𝔰 ≤ 𝔰₀^♮ on Q(a, b), then at every point of Q(a, b), for every
word C with |C| ≤ j ≤ N − 1,

    |D̂²Ψ_C| ≤ 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ϱ(p),                                            {#eq:tl5-hfs-m2}

so that M_g^(j) ≤ 2(k₁^(j,μ) + 1) 𝒥_g + 2k₂ ϱ(p); and at p, for 0 ≤ m ≤ N − 4,

    𝔰_P⁰(p) ≤ 2C_S ℰ_g(p)^(1/2) + 2C_(0,0) η₀(p),
    𝔰_g^(m)(p) ≤ C_(∞,μ)^(m) ℰ_g(p)^(1/2) + C_((∞,ϱ),μ)^(m) ϱ(p) + C_((∞,0),μ)^(m) η₀(p).            {#eq:tl5-hfs-linfty}

*Proof.* We follow the proof of [[lem:tl5-hfg-linfty]], whose bounds of [[lem:tl5-hf-quadratic]] hold with 𝔠^♮_n by
[[lem:tl5-hfs-quadratic]] (b) with ν′ = 1, as 𝔰 ≤ 𝔰_♭; so k₃^♮ takes the place of k₃^⋆, and k₃^♮ 𝔰 ≤ 1/2.

*Second derivatives.* Let q ∈ Q(a, b) and R_C := 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ϱ(p); we prove
[[eq:tl5-hfs-m2]] by induction on |C| ≤ j. In the bound of [[lem:tl5-hf-recovery]] for Ψ_C, as used in the proof of
[[lem:tl5-hf-linfty]], the words ZC have length |C| + 1, so (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤ μ^(−(|C|+1)/2) 𝒥_g; the terms
with D̂Ψ_C and Ψ_C, among them 𝔯₀ |Ψ_C|, are at most μ^(1/2) μ^(−(|C|+1)/2) 𝒥_g times their coefficients there, as
μ^(|C|/2) (|D̂Ψ_C|² + |Ψ_C|²)^(1/2) ≤ 𝒥_g; and the jets of level |J| ≤ |C| in the maps 𝔄_CJ are at most
μ^((|C|+1−|J|)/2) μ^(−(|C|+1)/2) 𝒥_g. With the residual terms, at most k₂ ϱ(p), this gives the linear part
k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p). In the nonlinear part, the factor of a monomial bounded by 𝔧 there is H, Ψ_(C′)
or D̂Ψ_(C′) with |C′| ≤ |C|, at most 2μ^(−(|C|+1)/2) 𝒥_g, or D̂²Ψ_(C′) with |C′| ≤ |C| − 1, at most R_C by the induction
hypothesis, as μ^(−(|C′|+1)/2) ≤ μ^(−(|C|+1)/2); and H^(αβ) D̂_αD̂_βΨ_J with |J| < |C| is at most 𝔰 R_C. So |D̂²Ψ_C| ≤
k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p) + k₃^♮ 𝔰 (2μ^(−(|C|+1)/2) 𝒥_g + R_C) ≤ R_C, by k₃^♮ 𝔰 ≤ 1/2. Multiplying by
μ^((|C|+1)/2) ≤ 1 gives the bound of M_g^(j).

*Zeroth order.* This is the step of that proof: μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p) for |B| ≤
N − 2, and μ |H(p)| ≤ 2μ |h(p)|; this gives the bound of 𝔰_P⁰(p).

*First order.* In the step of that proof for A := D̂Ψ_B, |B| ≤ N − 3, a coefficient of the remainder R′ in ℒ^J A, J a
word of rotations with |J| ≤ 2, carries a ≤ 2 letters and is contracted with Ψ_C or, after D̂, with D̂Ψ_C,
where |C| = |J| + |B| − a ≤ |B| + 2 − a; so μ^((|B|+3)/2) times its contribution is at most μ^((1+a)/2) Λ_a μ^(|C|/2)
(|Ψ_C| + |D̂Ψ_C|), and μ^((1+a)/2) Λ_a ≤ Λ₂^μ; on S_a it is at most μ^((1+a)/2) Λ_a η₀(p). By [[eq:tl5-hfs-m2]]
with |JB| + 1 ≤ |B| + 3, μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ 2(k₁^μ + 1) 𝒥_g + 2k₂ ϱ(p). The argument of that step then gives
μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^♮ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^♮ η₀(p).

*Second order at low levels.* In the step of that proof for |B| ≤ m, multiplied by μ^((|B|+4)/2), the terms with D̂Ψ_(ZB)
are bounded by L_g as there; those with D̂Ψ_B, Ψ_B and 𝔯₀ Ψ_B carry the factor μ^(1/2) more than their weights in L_g,
and the jets of level |J| ≤ |B| in 𝔄_BJ the factor μ^((|B|+1−|J|)/2), as μ^((|B|+4)/2) = μ^((|B|+1−|J|)/2) μ^((|J|+3)/2)
and μ^((|B|+4)/2) ≤ μ^((|B|+1−|J|)/2) μ^((|J|+2)/2). So k₁^(m) is replaced by k₁^(m,μ), and C₁^g and C_(1,0)^g by C₁^♮
and C_(1,0)^♮ through the first-order step. Taking the largest of the bounds and absorbing 𝔰_g^(m)/2 as there gives
[[eq:tl5-hfs-linfty]]. ∎

**Lemma {#lem:tl5-hfs-products}** (The quadratic terms with the letters on the background free.) In the setting of
[[lem:tl5-hfs-linfty]] suppose that 𝔰 ≤ 𝔰₀^♮ on Q(a, b), and let I be a word with n := |I| ≤ N, 𝔑_I and 𝔑^L_I as in
[[lem:tl5-hfg-products]], for N = 4 with the second expansion. Put 𝔨_A := 2k₁^μ + 2, 𝔨_B := max(𝔷, 2), 𝔰_P :=
𝔰_g^(m_P) and 𝔓 := max(𝔨_A 𝔰_P⁰, 𝔨_B 𝔰_P). Then at every point of Q(a, b), for every word J with |J| < n,

    μ^(n/2) |𝔑^L_I| ≤ μ^(−3/2) 𝔠^♮_n(μ) 𝔓 𝒥_g + μ^(n/2) 𝔠^♮_n 2k₂ 𝔰 ϱ(p),
    μ^(n/2) |ℒ^J N(h)| ≤ μ^((n−|J|−3)/2) (𝔠^♮_(|J|)(μ) + 1) 𝔓 𝒥_g
                         + μ^(n/2) (𝔠^♮_(|J|) + 1) 2k₂ 𝔰 ϱ(p).                                     {#eq:tl5-hfs-products}

*Proof.* Take a monomial of 𝔑^L_I with q solution factors, ν its background norm with the coefficient and b the number of
letters on its background factors, and choose Φ₁ and Φ₂ as in the proof of [[lem:tl5-hfg-products]], with ℓ_P and ℓ_E as
there. By [[lem:tl5-hfs-quadratic]] (b) the orders satisfy o₁ + o₂ ≤ n − b + 2, so the argument of that proof gives
ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n − b + 3. If Φ₂ = D̂²Ψ_C, then |Φ₂| ≤ 𝔨_A μ^(−ℓ_E(Φ₂)/2) 𝒥_g + 2k₂ ϱ(p) by [[eq:tl5-hfs-m2]], and Φ₁
carries no derivative D̂, as there are at most two in all, so it is H, h or Ψ_B with |B| ≤ N − 2 and |Φ₁| ≤
μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰. Otherwise μ^(ℓ_E(Φ₂)/2) |Φ₂| ≤ 𝔨_B 𝒥_g, by the proof of (∗) there, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P, by
that proof. With |Φ₁| ≤ 𝔰 in the term with ϱ(p) and |Φ_i| ≤ 𝔰 for the other factors, the monomial times μ^(n/2) is at
most ν 𝔰^(q−2) (μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔓 𝒥_g + μ^(n/2) 2k₂ 𝔰 ϱ(p)), and μ^((n − ℓ_P − ℓ_E)/2) ≤ μ^(−3/2) μ^(b/2).
By [[eq:tl5-hfs-sum]] with ν′ = μ and with ν′ = 1 this gives the first inequality. For |J| < n, 𝔑_J = 𝔑^L_J, also for
N = 4 as |J| ≤ 3, and μ^(n/2) |𝔑_J| = μ^((n−|J|)/2) μ^(|J|/2) |𝔑_J| is bounded by the first inequality for J; in
H^(αβ) D̂_αD̂_βΨ_J the factor D̂²Ψ_J is
the factor Φ₂ of the first kind, with Φ₁ = H, b = 0 and ℓ_P(H) + ℓ_E(D̂²Ψ_J) = |J| + 3. ∎

**Lemma {#lem:tl5-hfs-mixed}** (The products of level four, summed over the words.) Let N = 4, and let g, h, t, b, Σ,
ϱ, η₀, 𝔍_g, ς_t, X₁, X₂, Y₁ and Y₂ be as in [[lem:tl5-hfg-mixed]] and its proof, with 𝔰 ≤ 𝔰₀^♮ on Q(t, b). Put
λ_t^μ := 2([k₁^μ]_t + 1),

    ϖ₁ := 6 (2μ^(1/2) Λ₁)² + 36 (4μ^(1/2) Λ₁ + 2μ Λ₂)²,
    ϖ₂ := 6 (7μ^(1/2) Λ₁)² + 36 (14μ^(1/2) Λ₁ + 10μ Λ₁² + 7μ Λ₂)²,
    𝔛_(1,t) := (𝔭₃ 𝔵₃(t) (1 + 49 [ϖ₁]_t))^(1/2),
    𝔛_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (14 [ϖ₂]_t)^(1/2)),      𝔛′_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t,
    𝔜_(1,t) := 𝔱₃(t)^(1/2) (1 + 7λ_t^μ),   𝔜′_(1,t) := 7 𝔱₃(t)^(1/2) ς_t,   𝔜″_(1,t) := π (98 [𝔳⁶]_t)^(1/2),
    𝔜_(2,t) := 𝔱₂(t)^(1/2),   𝔜″_(2,t) := π (686 [𝔳⁴]_t)^(1/2).

Then, with P₁ and P₂ as in [[lem:tl5-hfs-quadratic]] (c),

    ‖P₁‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) X₁ Y₁,      ‖P₂‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) X₂ Y₂,
    μ² X₁ ≤ 𝔛_(1,t) 𝔍_g,   μ^(3/2) Y₁ ≤ 𝔜_(1,t) 𝔍_g + 𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀,
    μ² X₂ ≤ 𝔛_(2,t) 𝔍_g + 𝔛′_(2,t) ϱ,   μ^(3/2) Y₂ ≤ 𝔜_(2,t) 𝔍_g + 𝔜″_(2,t) η₀.                       {#eq:tl5-hfs-mixed}

*Proof.* ‖P₁‖_Σ² is the sum of ‖|D̂Ψ_B| |D̂Ψ_(B′)|‖_Σ² over the pairs (B, B′), and ‖P₂‖_Σ² that of ‖|Ψ_B| |D̂²Ψ_Z|‖_Σ²
over the pairs (B, Z); [[eq:tl5-hf4-holder]] for each pair, with X := D̂Ψ_B, Y := D̂Ψ_(B′) and X := D̂²Ψ_Z, Y := Ψ_B,
gives the first line. In the proof of [[lem:tl5-hfg-mixed]], replace the bounds of the remainders R′ and R as follows. By
[[lem:tl5-hfs-quadratic]] (a) with Ψ_B in place of h, R′ for a rotation word J has 2 monomials whose coefficient carries
one letter if |J| = 1, and 4 with one letter and 2 with two letters if |J| = 2; each is contracted with a Ψ_C, |C| = |JB|
− a for a coefficient with a letters, and μ² ≤ μ^(a/2) μ^(|C|/2) as |JB| ≤ 4. So μ² |R′| ≤ ρ′_(|J|) 𝒥_g with ρ′₁ :=
2μ^(1/2) Λ₁ and ρ′₂ := 4μ^(1/2) Λ₁ + 2μ Λ₂, and Σ_(|J|≤2) ρ′_(|J|)² = ϖ₁ over the 6 words of length one and 36 of length
two; with the 49 words B, μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 98 ϖ₁ 𝒥_g², which with [[lem:tl5-hf4-face]] (b) for r = 3
gives the bound of μ² X₁. Likewise R for ℒ^J D̂²Ψ_Z has background norm at most β₂^♮(|J|) − 1, that is 7Λ₁ for |J| = 1
and 14Λ₁ + 10Λ₁² + 7Λ₂ for |J| = 2, each monomial contracted with Ψ_C or D̂Ψ_C, |C| = |JZ| − a ≤ 3 − a, and μ² ≤ μ^(a/2)
μ^(|C|/2); with the 7 fields Z, μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 14 ϖ₂ 𝒥_g², and ‖M_g‖_Σ ≤ λ_t^μ 𝔍_g + ς_t ϱ by
[[eq:tl5-hfs-m2]] with j = 3, which with [[lem:tl5-hf4-face]] (b) for r = 4 gives the bound of μ² X₂. The bounds of μ³
Y₁² and μ³ Y₂² of that proof, with ‖M_g‖_Σ ≤ λ_t^μ 𝔍_g + ς_t ϱ and (x + y + z)^(1/2) ≤ x^(1/2) + y^(1/2) + z^(1/2), give
those of μ^(3/2) Y₁ and μ^(3/2) Y₂; the bound of Y₂ contains no second derivative. ∎

**Definition {#def:tl5-hfs-constants}** (The constants sharpened a second time.) Let N ≥ 5 and the setting be that of
[[def:tl5-hf-constants]], or N = 4 and the setting that of [[def:tl5-hf4-constants]], with δ_w, ϰ₀, 𝔰_θ, ϱ, η₀ and 𝒮
as there, and with the constants of [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]] put C_P^♮ := C_(∞,μ)^(m_P),
C_(P,ϱ)^♮ := C_((∞,ϱ),μ)^(m_P), C_(P,0)^♮ := C_((∞,0),μ)^(m_P), 𝔣₀ := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c), 𝔣₁ := ϰ₀ +
(1/2)|T| ‖𝒞_(·0)‖ and 𝔣₂ := 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2). Put

    𝔰₀^♮ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮)),      𝔰₁^♮ := min(𝔰₀^♮/2, c_* κ_m/2, 𝔰_θ),
    𝔤_(𝒥,s) := (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1))²)^(1/2),
    𝔤_(ϱ,s) := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′) + 1))²)^(1/2),
    𝔎 := max(2C_S 𝔨_A, C_P^♮ 𝔨_B),   𝔎_ϱ := C_(P,ϱ)^♮ 𝔨_B,   𝔎₀ := max(2C_(0,0) 𝔨_A, C_(P,0)^♮ 𝔨_B),
    𝔞_(o,s) := 𝔣₀ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎,      𝔞_(i,s) := 𝔣₁ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎,
    𝔟_(o,s) := 𝔣₀ (C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀) + 𝔣₂ 𝔤_(𝒥,s) (𝔎_ϱ ϱ + 𝔎₀ η₀),
    𝔟_(i,s) := 𝔣₁ (C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀) + 𝔣₂ 𝔤_(𝒥,s) (𝔎_ϱ ϱ + 𝔎₀ η₀),
    S_(F,s) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,s) e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,s) e^(φ/2)) dt),
    𝔯_(w,s) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) 𝔟_(o,s) dt + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) 𝔟_(i,s) dt),
    ε_(w,s) := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(ϱ,s) k₂ ϱ],

the functions of p being evaluated at the point of the supremum. For N = 4 put, with the notation of
[[lem:tl5-hfs-mixed]], [𝔠^M_i]_t the number 𝔠^M_i formed with the suprema over Σ₁(t, v*) of the Λ_k and the Λ^R_k, and
w_t := e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t 𝔪(t),

    S_(M,s) := μ^(−3/2) ∫_(−10)^(u*) w_t ([𝔠^M₁]_t 𝔛_(1,t) 𝔜_(1,t) + [𝔠^M₂]_t 𝔛_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_(M,s) := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) ([𝔠^M₁]_t 𝔛_(1,t) (𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀)
               + [𝔠^M₂]_t (𝔛_(2,t) 𝔜″_(2,t) η₀ + 𝔛′_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_(M,s) := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t [𝔠^M₂]_t 𝔛′_(2,t) 𝔜″_(2,t) dt,

and for N ≥ 5 let S_(M,s) = 𝔯_(M,s) = ε_(M,s) := 0. Finally, with the constants of [[eq:tl5-hfg-cinf]],

    A_s := √2 δ_w + 2ε_(w,s) + 2ε_(M,s),      B_s := 2 (S_(F,s) + S_(M,s)),      𝔯_s := 𝔯_(w,s) + 𝔯_(M,s),
    𝔰_(*,s) := sup_(p∈D^κ) (2 C_∞^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_s
               + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀).                                    {#eq:tl5-hfs-constants}

**Proposition {#prop:tl5-hfs-bootstrap}** (The a priori estimate with the constants sharpened a second time.) In the
setting of [[def:tl5-hfs-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N)
and that

    𝔯_s ≤ 1/4,      η₀ < 𝔰₁^♮,      𝔰_(*,s) < 𝔰₁^♮.                                               {#eq:tl5-hfs-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_s for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,s) on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_s + B_s Y_s(g)².                                                                          {#eq:tl5-hfs-h1}

*Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hfg-bootstrap]], with 𝔰₀^♮, 𝔰₁^♮ and A_s in place of 𝔰₀^⋆,
𝔰₁^⋆ and A_g, and [[eq:tl5-hfs-linfty]] for m = N − 4 and μ = 1, whose constants are then those of
[[eq:tl5-hfg-cinf]], in place of [[eq:tl5-hfg-linfty]]: this gives 𝔰 ≤ 𝔰_(*,s) < 𝔰₁^♮ on D^κ_s, |h|_k̂ < κ_m/2 and
θ_H ≤ ϑ, and [[lem:tl5-hfs-quadratic]], [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]] apply at every point of
D^κ_s, with ϱ(p) ≤ ϱ and η₀(p) ≤ η₀.

*Step 2.* Step 2 of the proof of [[prop:tl5-hfg-bootstrap]] holds up to the bounds of the nonlinear terms, which we
replace as follows. By [[eq:tl5-hfs-products]], the definition of 𝔮_(jj′) and the Cauchy–Schwarz inequality over the
7^(j′) words of each length j′ ≤ j, the family over |I| = j of the nonlinear terms other than 𝔑^M_I has norm at most
μ^(−j/2) (A_j + B_j), with A_j := Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1) μ^(−3/2) 𝔓 𝒥_g and B_j :=
μ^(j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′) + 1) 2k₂ 𝔰 ϱ. As for the forcing terms in the proof of
[[prop:tl5-hf-linear-n]], with the weights μ^|I| and Minkowski's and the Cauchy–Schwarz inequalities over j, their
contribution to the bulk is at most 2Ω̂² (𝔤_(𝒥,s) μ^(−3/2) 𝔓 𝒥_g + 𝔤_(ϱ,s) 2k₂ 𝔰 ϱ)(√e_o + √c √e_i); with 2Ω̂² 𝒥_g
(√e_o + √c √e_i) ≤ 𝔣₂ (e_o + e_i), as there, and 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ, it is at most 2Ω̂² (1/4) 𝔤_(ϱ,s) k₂ ϱ (√e_o +
√c √e_i) + μ^(−3/2) 𝔣₂ 𝔤_(𝒥,s) 𝔓 (e_o + e_i). The terms 2Ω̂² |𝔮_H| are bounded as there, with 𝔰_P ≥ 𝔰_P⁰: at most
μ^(−3/2) 𝔰_P (𝔣₀ e_o + 𝔣₁ e_i). For N = 4, the terms 𝔑^M_I contribute, by the proof of [[prop:tl5-hf4-bootstrap]], at
most ∫ [2Ω̂² (1 + c/κ′)^(1/2)]_t μ⁴ ‖(Σ_(|I|=4) |𝔑^M_I|²)^(1/2)‖_Σ μ^(−2) Y_s dt over the faces Σ := Σ₁(t, b′), the
Cauchy–Schwarz inequality over I being taken at each point; by [[eq:tl5-hfs-m]] and [[eq:tl5-hfs-mixed]], μ²
‖(Σ_I |𝔑^M_I|²)^(1/2)‖_Σ ≤ μ^(−3/2) e^(φ(t,v*)/2) 𝔪(t) ([𝔠^M₁]_t (μ² X₁)(μ^(3/2) Y₁) + [𝔠^M₂]_t (μ² X₂)(μ^(3/2) Y₂)),
and expanding with 𝔍_g ≤ [𝔨₂]_t^(1/2) Y_s bounds the term by S_(M,s) Y_s³ + 𝔯_(M,s) Y_s² + ε_(M,s) Y_s.

*Step 3.* By [[eq:tl5-hfs-linfty]] for m = m_P and ℰ_g(p) ≤ e^(φ(p)) Y_s², at every point 𝔰_P ≤ C_P^♮ e^(φ/2) Y_s +
C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀ and 𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0) η₀, so 𝔓 ≤ 𝔎 e^(φ/2) Y_s + 𝔎_ϱ ϱ + 𝔎₀ η₀. Foliating
as in Step 3 of the proof of [[prop:tl5-hf-bootstrap]], for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,s) + ε_(M,s)) + 𝔯_s Y_s² + (S_(F,s) + S_(M,s)) Y_s³,

and with ϑ ≤ 1/4 and 𝔯_s ≤ 1/4 the conclusion follows as there. ∎

**Theorem {#thm:tl5-hfs}** (Existence close to an explicit background, with the constants sharpened a second time.) In
the setting of [[thm:tl5-hf]] (N ≥ 6) let Λ_k, Λ^R_k and 𝔰_♭ be as in [[def:tl5-hfs-bounds]], and suppose: (a) η₀ <
𝔰₁^♮; (b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N); (c) the constants of
[[def:tl5-hfs-constants]] satisfy 𝔯_(w,s) ≤ 1/4, 𝔰_(*,s) < 𝔰₁^♮ and the closing condition

    4 A_s B_s = 8 (√2 δ_w + 2ε_(w,s)) S_(F,s) < 1.                                                  {#eq:tl5-hfs-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_s and 𝔰_(*,s) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hfg]] applies with A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]],
[[eq:tl5-hfs-h1]] and [[eq:tl5-hfs-closing]] in place of A_g, B_g, 𝔰_(*,g), 𝔰₁^⋆, [[prop:tl5-hfg-bootstrap]],
[[eq:tl5-hfg-h1]] and [[eq:tl5-hfg-closing]]; it uses only 𝔰 ≤ 𝔰_(*,s) < 𝔰₁^♮ ≤ min(1/16, 𝔰_θ) and the bound
Y_σ ≤ 2A_s. ∎

**Theorem {#thm:tl5-hf4s}** (Level four, with the constants sharpened a second time.) In the setting of
[[thm:tl5-hf4]] let Λ_k, Λ^R_k and 𝔰_♭ be as in [[def:tl5-hfs-bounds]] with N = 4, and suppose: (a) η₀ < 𝔰₁^♮; (b)
a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) the constants of [[def:tl5-hfs-constants]] with N = 4
satisfy 𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4, 𝔰_(*,s) < 𝔰₁^♮ and the closing condition

    4 A_s B_s = 8 (√2 δ_w + 2ε_(w,s) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1.                          {#eq:tl5-hf4s-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_s and 𝔰_(*,s) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4g]] applies with A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]] for N = 4,
[[eq:tl5-hfs-h1]] and [[eq:tl5-hf4s-closing]] in place of A_g, B_g, 𝔰_(*,g), 𝔰₁^⋆, [[prop:tl5-hfg-bootstrap]],
[[eq:tl5-hfg-h1]] and [[eq:tl5-hf4g-closing]]; [[eq:tl5-hf4-m2]] holds by [[eq:tl5-hfs-m2]] with μ = 1 and j = 3. ∎

**Remark {#rem:tl5-hfs-what}** (What the second sharpening changes.) A background factor that carries a letters enters
𝔤_(𝒥,s) as μ^(a/2) Λ_a or μ^(a/2) Λ^R_a, and the forcing of level j′ in the equation of level j as μ^((j−j′)/2) 𝔮_(jj′),
the weights of the coupling 𝔒 of [[eq:tl5-hf-bn]]; a product of bounds Λ_(a₁) ⋯ Λ_(a_r) occurs only with a₁ + ⋯ + a_r
at most the number of letters of the term, against the powers Λ_k^r of [[def:tl5-hfg-graded]]. The constant of the term
with ϱ in ε_(w,s), 𝔤_(ϱ,s), has the weights μ^j of 𝔤_N of [[def:tl5-hf-constants]]; in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s), ϱ
carries μ^(−3/2) as in [[sec:tl5-hfg]]. The recovery constant of the highest level enters 𝔎 through 𝔨_A
in the first entry and through C₁^♮ in the second, not as a product; it enters as k₁^μ, whose couplings 𝔄_CJ carry
the weights μ^((|C|+1−|J|)/2) ≤ μ^(1/2), as do its terms with 𝔯₀ and with D̂Z and D̂²Z. At level four,
S_(M,s) contains the coefficients 𝔠^M₁ = 480 + 49 𝔰_♭ 𝔠^(3♮)₄ and 𝔠^M₂ = 4 + 49 𝔰_♭ 𝔠^(3♮)₄ in place of 49 [𝔠^⋆₄]_t, and
k₁^μ once in each of the two products 𝔛_(1,t) 𝔜_(1,t) and 𝔛_(2,t) 𝔜_(2,t). The smallness 𝔰_(*,s) < 𝔰₁^♮ keeps the
constants of [[eq:tl5-hfg-cinf]] and the factor μ^(−N/2), for the reasons given in [[rem:tl5-hfg-powers]]. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfs]] and [[thm:tl5-hf4s]] are established in this
paper for no background at 10 l5. [[sec:tl5-hft]] sharpens the smallness condition and the Sobolev constants further
([[thm:tl5-hft]], [[thm:tl5-hf4t]]).

### The constants sharpened a third time {#sec:tl5-hft}

This section sharpens the constants of [[sec:tl5-hfs]] in two ways and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with
them. First, the smallness condition is weighted: the low quantities at a point are bounded by the weighted energies
with the weighted recovery constant, the terms with ϱ and η₀ being kept apart ([[lem:tl5-hft-small]] (a)), or the
absorption of the nonlinear terms in the recovery is weighted as well ([[lem:tl5-hft-small]] (b)). Second, the Sobolev
inequalities on the faces are proved intrinsically on the leaves, through the action of the rotations on the tensors
over S³, without passing to Euclidean components ([[lem:tl5-hft-leaf]], [[lem:tl5-hft-face]]). The closing conditions are
[[eq:tl5-hft-closing]] and [[eq:tl5-hf4t-closing]]; those of the earlier theorems remain valid, and any of them may be
used. Throughout, N ≥ 4, μ ∈ (0, 1] and the notation is that of [[sec:tl5-hfs]].

**Lemma {#lem:tl5-hft-leaf}** (An intrinsic Sobolev inequality on the leaves.) Let α, β, ρ > 0 be numbers, h₀ := α² du² +
β² dv² + ρ² γ₀, and |·|₀ the norm it induces on tensors at the points of a leaf S_(u,v) := {(u, v)} × S³. For r ≥ 0 and j
∈ ℕ let e_j(r) be the multiplicity of the irreducible representation [j] of spin j of SU(2) in (2[0] ⊕ [1])^(⊗r), and for
j₁, j₂ ∈ (1/2)ℕ with j₁ + j₂ ∈ ℕ put m_(j₁j₂)(r) := Σ_(j=|j₁−j₂|)^(j₁+j₂) e_j(r) and

    C_(E,r)² := (1/(2π²)) Σ_(j₁,j₂) (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r) / (1 + 2j₁(j₁ + 1) + 2j₂(j₂ + 1))².   {#eq:tl5-hft-ce}

The series converges, and C_(E,0)² = C_(S³)² = 1/12. For every C² covariant tensor field A of rank r on S_(u,v) and every
ω ∈ S³, with the sum over the words J of length at most two in the six rotations,

    |A(ω)|₀² ≤ 6 C_(E,r)² Σ_(|J|≤2) ∫_(S³) |ℒ^J A|₀² dω.                                               {#eq:tl5-hft-leaf}

*Proof.* Let E be the bundle over S³ of the covariant r-tensors at the points of S_(u,v), with the metric h₀. The group
SO(4) acts on S³ by rotations, and on E by pullback, as its elements fix ∂_u and ∂_v and preserve γ₀; the action
preserves h₀ and the measure dω, so it is unitary on L²(S³, E), which we complexify. The fields K_ab generate the
rotations in the planes of X_a, X_b, and ℒ_(K_ab) is the derivative of this action along K_ab; it is skew-adjoint on
L²(S³, E). The fiber at the point o = (1, 0, 0, 0) is E_o = (ℝ du ⊕ ℝ dv ⊕ T*_o S³)^(⊗r), on which the isotropy group
SO(3) acts trivially on du and dv and by its standard representation, of spin one, on T*_o S³; so E_o ≅ (2[0] ⊕ [1])^(⊗r)
as a representation of SO(3).

The irreducible representations of SO(4) are the π = (j₁, j₂) of SU(2) × SU(2) with j₁ + j₂ ∈ ℕ, of dimension (2j₁ +
1)(2j₂ + 1), and the isotropy group of o is the diagonal SU(2), on which (j₁, j₂) restricts, by the Clebsch–Gordan
rule, to [|j₁ − j₂|] ⊕ ⋯ ⊕ [j₁ + j₂]. By the Peter–Weyl theorem and Frobenius reciprocity, L²(S³, E) is the orthogonal
sum of the isotypic subspaces V_π, each finite-dimensional, made of smooth sections, of dimension dim π · dim
Hom_(SO(3))(π, E_o) = (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r). The operator Ω := −Σ_(a<b) ℒ_(K_ab)² is the Casimir operator of
the invariant form for which the K_ab are orthonormal; on V_π it is the number c_π := 2j₁(j₁ + 1) + 2j₂(j₂ + 1).
Indeed, with L₁ := K₂₃, L₂ := −K₁₃, L₃ := K₁₂ and M_i := K_(i4), the fields J_i^± := (L_i ± M_i)/2 satisfy
[J₁^±, J₂^±] = −J₃^± and the cyclic relations, and [J_i⁺, J_l⁻] = 0; so they span the two copies of su(2) in so(4),
of spins j₁ and j₂ on π, −Σ_i (J_i⁺)² and −Σ_i (J_i⁻)² are j₁(j₁ + 1) and j₂(j₂ + 1) on V_π, and Σ_(a<b) K_ab² =
Σ_i (L_i² + M_i²) = 2 Σ_i ((J_i⁺)² + (J_i⁻)²). (On the representation ℝ⁴ = (1/2, 1/2) both sides are −3, each K_ab²
being minus the projection onto its plane, and on the functions of degree n, (n/2, n/2), they are −n(n + 2), the
eigenvalue of the Laplacian of γ₀.)

For an orthonormal basis (s_k) of V_π the function Σ_k |s_k(ω)|₀² does not depend on the basis, so it is invariant under
SO(4), which acts transitively on S³; its integral is dim V_π, so it is dim V_π/(2π²). Hence for A_π ∈ V_π, by the
Cauchy–Schwarz inequality, |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖², ‖·‖ the norm of L²(S³, E). Writing A = Σ_π A_π and using
the Cauchy–Schwarz inequality over π,

    |A(ω)|₀ ≤ Σ_π (dim V_π/(2π²))^(1/2) (1 + c_π)⁻¹ ‖(1 + Ω) A_π‖ ≤ C_(E,r) ‖(1 + Ω) A‖,

the series C_(E,r)² converging because m_(j₁j₂)(r) ≤ 5^r and vanishes unless |j₁ − j₂| ≤ r, so that its terms with
j₁ ≥ 1 are at most 5^r (2j₁ + 2r + 1)² / (2j₁²)² for at most 2r + 1 values of j₂. As ℒ_(K_ab) is skew-adjoint, ‖(1 + Ω)
A‖² = ‖A‖² + 2 Σ ‖ℒ_(K_ab) A‖² + ‖Σ ℒ_(K_ab)² A‖² ≤ 6 Σ_(|J|≤2) ‖ℒ^J A‖², by the Cauchy–Schwarz inequality over the six
fields. For r = 0, m_(j₁j₂)(0) = 1 if j₁ = j₂ and 0 otherwise, and with n := 2j₁ the series is Σ_n 1/(2π²(n + 1)²) =
1/12. ∎

**Lemma {#lem:tl5-hft-face}** (The Sobolev inequalities on the faces, intrinsic.) Let h₀ be as in [[lem:tl5-hft-leaf]],
with numbers α, β, ρ fixed for each face Σ₁(a, b), in (c) the same for all the faces Σ₁(t, b) with one t, and at each
point let 𝔳₀ := sup |X|/|X|₀ and 𝔴₀ := sup |X|₀/|X| over the nonzero vectors X, |X| the norm of k. Then:

(a) [[eq:tl5-hf-cs-r]] holds with 6 C_(E,r)², 𝔳₀ and 𝔴₀ in place of 6 C_(S³)² 𝔭_r, 𝔳 and 𝔴;

(b) [[lem:tl5-hf-sobolev]] holds with C_S and C_(S,0) replaced by C_S^E and C_(S,0)^E, where

    C_S^E(p)² := 6 C_(E,2)² 𝔴₀(p)⁴ sup_(Σ₁(a,b)) 𝔳₀⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),
    C_(S,0)^E(p)² := 6 C_(E,2)² 𝔴₀(p)⁴ sup_(S_a) 𝔳₀⁴;                                                    {#eq:tl5-hft-cs}

(c) [[lem:tl5-hf4-face]] holds with |A|₀ in place of |A_e| in ⟦·⟧_(2,∞) and ⟦·⟧_(∞,2), with 6 C_(E,r)² in place of
𝔭_r/2 in (b), and with 𝔳₀ and 𝔴₀ in place of 𝔳 and 𝔴 in 𝔵_r(t), 𝔱_r(t), 𝔪(t) and in (a).

*Proof.* For a tensor A of rank r at a point, the components of A in a frame orthonormal for h₀ and in one orthonormal
for k differ by the action of a matrix in each slot, whose operator norm is 𝔴₀ in one direction and 𝔳₀ in the other;
so |A| ≤ 𝔴₀^r |A|₀ and |A|₀ ≤ 𝔳₀^r |A|, as in the proof of [[lem:tl5-hf-khat]]. The coefficients of h₀ are constant,
so ℒ_(∂_γ) h₀ = 0 and ℒ_K h₀ = 0 for the rotations K; and ∂_γ commutes with the rotations. So along the curves γ_ω of the
proof of [[lem:tl5-hf-sobolev]], (d/dv)|B|₀² = 2⟨B, ℒ_(∂_γ) B⟩₀ ≤ |B|₀² + |ℒ_(∂_γ) B|₀² for every tensor field B, and
ℒ_(∂_γ) commutes with ℒ^J. In the proofs of [[lem:tl5-hf-sobolev]], of [[eq:tl5-hf-cs-r]] and of [[lem:tl5-hf4-face]],
replace the components A_e, the inequality [[eq:tl5-hf-sphere]] for each component and the passage from K(A_e) to
(ℒ_K A)_e, which produce 6C_(S³)² 𝔭_r and the factors 𝔳 and 𝔴, by |A|₀, by [[eq:tl5-hft-leaf]] applied to A and to
ℒ_(∂_γ) A on the leaf through γ_ω(v), and by the two comparisons above; the rest of each proof holds as written. For
(c), |f| ≤ |X| |Y| ≤ 𝔴₀^(r_X + r_Y) |X|₀ |Y|₀ ≤ max(1, 𝔴₀)⁶ |X|₀ |Y|₀. ∎

In what follows, C_S, C_(S,0), C₁, C_(1,ϱ), C_(1,0), C_(0,0) and their variants of [[sec:tl5-hfg]] and [[sec:tl5-hfs]],
and at level four 𝔵_r(t), 𝔱_r(t), 𝔪(t) and [𝔳^(2r)]_t, denote either the merged constants or those formed by
[[lem:tl5-hft-face]], that is with 6 C_(E,r)² in place of 6 C_(S³)² 𝔭_r (so 258 C_(E,3)² in place of 258 C_(S³)² 𝔭₃ in
C₁, 516π² C_(E,3)² in place of 516π² C_(S³)² 𝔭₃ in C_(1,0), 6 C_(E,r)² in place of 𝔭_r/2 in the bounds of ⟦·⟧_(2,∞))
and with 𝔳₀, 𝔴₀ in place of 𝔳, 𝔴; the same choice throughout. Every statement below holds for either choice, as their
proofs use the Sobolev inequalities only through their forms.

**Lemma {#lem:tl5-hft-small}** (The low quantities for the smallness.) Let g, h, p, a, b, ϱ(p) and η₀(p) be as in
[[lem:tl5-hfs-linfty]].

(a) If 𝔰 ≤ 𝔰₀^♮ on Q(a, b), with 𝔰₀^♮ as there, then, with the constants of [[eq:tl5-hfg-cinf]] and
[[eq:tl5-hfs-linfty]],

    𝔰(p) ≤ μ^(−N/2) C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀(p).   {#eq:tl5-hft-small}

(b) Let k₃^♮(μ) := (8/5) max_(|C|≤N−1) (𝔠^♮_(|C|)(μ) + Σ_(J≠C) μ^((|C|−|J|)/2) ‖𝔔_CJ‖ (𝔠^♮_(|J|)(μ) + 1)) and 𝔰₀^μ :=
min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^♮(μ))). If 𝔰 ≤ 𝔰₀^μ on Q(a, b), then at every point of Q(a, b) and for 0 ≤ j ≤ N − 1,
M_g^(j) ≤ 2(k₁^(j,μ) + 1) 𝒥_g + 2k₂ ϱ(p), the second inequality of [[eq:tl5-hfs-linfty]] holds at p for 0 ≤ m ≤ N − 4,
and

    𝔰(p) ≤ μ^(−N/2) (C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2) + C_((∞,ϱ),μ)^(N−4)(p) ϱ(p)
                     + C_((∞,0),μ)^(N−4)(p) η₀(p)).                                                  {#eq:tl5-hft-smallb}

*Proof.* (a) Every low quantity Φ of order o, other than H, satisfies |Φ(p)| ≤ μ^(−(o+2)/2) E_Φ + R_Φ, with E_Φ, R_Φ as
follows. For Ψ_B, |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] gives |Ψ_B(p)| ≤ C_S (Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂)^(1/2) + C_(0,0)
η₀(p) ≤ μ^(−(|B|+2)/2) C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p), as μ^(|B|+2) ≤ μ^(|JB|); and |H(p)| ≤ 2|h(p)|. For D̂Ψ_B, |B| ≤
N − 3, apply the first-order step of the proof of [[lem:tl5-hfs-linfty]] without the weight: at the points of the face,
by [[eq:tl5-hfs-m2]] and the bounds of the remainders there, |ℒ^J D̂Ψ_B| ≤ μ^(−(|B|+3)/2) (1 + 6Λ₂^μ) 𝒥_g and |D̂ℒ^J
D̂Ψ_B| ≤ μ^(−(|B|+3)/2) (2(k₁^μ + 1) + 6√2 Λ₂^μ) 𝒥_g + 2k₂ ϱ(p), and on S_a, |ℒ^J D̂Ψ_B| ≤ (1 + 6Λ₂) η₀(p); with (x + y)²
≤ 2x² + 2y² as there this gives |D̂Ψ_B(p)| ≤ μ^(−(|B|+3)/2) C₁^♮ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^g η₀(p). For
D̂²Ψ_B, |B| ≤ N − 4, the bound at p of [[lem:tl5-hf-recovery]], as used in the proof of [[lem:tl5-hf-linfty]], is a
linear combination of jets Ψ_C, D̂Ψ_C with |C| ≤ |B| + 1, plus k₂ ϱ(p), plus the nonlinear terms, which are at most k₃^♮
𝔰(p)². Inserting the bounds just found for the jets, their parts with ℰ_g(p) give at most μ^(−(|B|+4)/2) k₁^(N−4,μ)
(2𝔐)^(1/2) max(C_S, C₁^♮) ℰ_g(p)^(1/2), with the weights counted as in the proof of [[lem:tl5-hfs-linfty]], and their
parts with ϱ(p) and η₀(p) at most k₁^(N−4) (2𝔐)^(1/2) (C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)^g) η₀(p)), the coefficients
being those of k₁^(N−4). As μ^(−(o+2)/2) ≤ μ^(−N/2) for every low quantity, the maximum over them gives 𝔰(p) ≤
(1/2)(μ^(−N/2) C_(∞,μ)^(N−4) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(N−4) ϱ(p) + C_(∞,0)^(N−4) η₀(p)) + k₃^♮ 𝔰(p)², and k₃^♮ 𝔰(p) ≤ 1/2
gives [[eq:tl5-hft-small]].

(b) In the proof of [[lem:tl5-hfs-linfty]], the nonlinear terms of the bound of μ^((|C|+1)/2) |D̂²Ψ_C| are sums over the
monomials of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, multiplied by 𝔔_CJ, and of H^(αβ) D̂_αD̂_βΨ_J, |J| < |C|. In a
monomial whose background factors carry b letters, the factor Φ bounded there by 𝔧 has order at most |J| − b + 2, and at
most |J| − b + 1 unless Φ = D̂²Ψ_(C′) with |C′| = |J| − b; so μ^((|C|+1)/2) |Φ| ≤ μ^(b/2) (2𝒥_g + M_g^(j)) for |C| ≤ j,
as |C| ≥ |J|, and μ^((|C|+1)/2) = μ^((|C|−|J|)/2) μ^((|J|+1)/2). By [[eq:tl5-hfs-sum]] with ν′ = μ these terms are at
most k₃^♮(μ) 𝔰 (2𝒥_g + M_g^(j)), and k₃^♮(μ) 𝔰 ≤ 1/2 gives the bound of M_g^(j) as there. In the step on second
derivatives at low levels the same count gives k₃^♮(μ) 𝔰(p) 𝔰_g^(m)(p) for the nonlinear terms; the other steps do not
use the smallness, and the first-order step uses M_g in place of [[eq:tl5-hfs-m2]], μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ M_g. So
the second inequality of [[eq:tl5-hfs-linfty]] holds, and [[eq:tl5-hft-smallb]] follows from 𝔰 ≤ μ^(−N/2) 𝔰_g^(N−4). ∎

**Lemma {#lem:tl5-hft-products}** (The quadratic terms under the weighted absorption.) In the setting of
[[lem:tl5-hft-small]] (b), with 𝔰 ≤ 𝔰₀^μ on Q(a, b), [[lem:tl5-hfs-products]] holds with μ^(−1/2) 𝔠^♮_n(μ) in place
of μ^(n/2) 𝔠^♮_n and μ^(−1/2) (𝔠^♮_(|J|)(μ) + 1) μ^((n−|J|)/2) in place of μ^(n/2) (𝔠^♮_(|J|) + 1) in the terms with
ϱ(p), and [[lem:tl5-hfs-mixed]] holds as stated.

*Proof.* In the proof of [[lem:tl5-hfs-products]], the bound of a factor Φ₂ = D̂²Ψ_C becomes |Φ₂| ≤ μ^(−ℓ_E(Φ₂)/2)
(𝔨_A 𝒥_g + 2k₂ ϱ(p)), by [[lem:tl5-hft-small]] (b); the other bounds hold as there, [[lem:tl5-hft-small]] (b) giving
those of 𝔰_P⁰ and 𝔰_P. The term with ϱ(p) of a monomial whose background factors carry b letters is then at most ν
𝔰^(q−1) μ^((n − ℓ_E(Φ₂))/2) 2k₂ ϱ(p). If b = 0, ℓ_E(Φ₂) ≤ n; if b ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1 ≤ n − b + 1; so μ^((n −
ℓ_E(Φ₂))/2) ≤ μ^(−1/2) μ^(b/2), and [[eq:tl5-hfs-sum]] with ν′ = μ gives the first inequality. For |J| < n the term
with ϱ(p) of μ^(n/2) |H| |D̂²Ψ_J| is at most μ^((n−|J|−1)/2) 𝔰 2k₂ ϱ(p). In the proof of [[lem:tl5-hfs-mixed]], ‖M_g‖_Σ
≤ λ_t^μ 𝔍_g + ς_t ϱ follows from the bound of M_g^(3) in [[lem:tl5-hft-small]] (b). ∎

**Definition {#def:tl5-hft-constants}** (The constants sharpened a third time.) In the setting of
[[def:tl5-hfs-constants]], with its constants formed with the choice of Sobolev constants made above, fix one of the
two options (a), (b) of [[lem:tl5-hft-small]], and put, with k₃^♮(μ) as there,

    option (a):  𝔰₁^t := 𝔰₁^♮,   ε_(w,t) := ε_(w,s),
                 𝔰_(*,t) := sup_(p∈D^κ) (2 C_(∞,μ)^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_t + C_(∞,ϱ)^(N−4)(p) ϱ(p)
                            + C_(∞,0)^(N−4)(p) η₀);
    option (b):  𝔰₀^μ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮(μ))),   𝔰₁^t := min(𝔰₀^μ/2, c_* κ_m/2, 𝔰_θ),
                 ε_(w,t) := 𝒮[s_N[2R̂ic] + (1/4) μ^(−1/2) 𝔤_(𝒥,s) k₂ ϱ],
                 𝔰_(*,t) := sup_(p∈D^κ) μ^(−N/2) (2 C_(∞,μ)^(N−4)(p) e^(φ(p)/2) A_t + C_((∞,ϱ),μ)^(N−4)(p) ϱ(p)
                            + C_((∞,0),μ)^(N−4)(p) η₀);
    A_t := √2 δ_w + 2ε_(w,t) + 2ε_(M,s),      B_t := B_s,      𝔯_t := 𝔯_s.                        {#eq:tl5-hft-constants}

**Proposition {#prop:tl5-hft-bootstrap}** (The a priori estimate with the constants sharpened a third time.) In the
setting of [[def:tl5-hft-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N)
and that 𝔯_t ≤ 1/4, η₀ < 𝔰₁^t and 𝔰_(*,t) < 𝔰₁^t. Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤
2A_t for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,t) on D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_t + B_t Y_s(g)².                                                                          {#eq:tl5-hft-h1}

*Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hfs-bootstrap]], with 𝔰₁^t, A_t and 𝔰_(*,t) in place of
𝔰₁^♮, A_s and 𝔰_(*,s), and with [[eq:tl5-hft-small]] (option (a)) or [[eq:tl5-hft-smallb]] (option (b)) in place of the
bound at μ = 1: for p ∈ D^κ_σ, ℰ_g(p) ≤ e^(φ(p)) Y_σ(g)² ≤ 4 e^(φ(p)) A_t², as φ is at most φ(p) on Σ₁(τ₁(p), τ₂(p)),
so 𝔰(p) ≤ 𝔰_(*,t) < 𝔰₁^t, which is at most half the threshold of [[lem:tl5-hft-small]] in either option. The argument
there gives 𝔰 ≤ 𝔰_(*,t) on D^κ_s, |h|_k̂ < κ_m/2 and θ_H ≤ ϑ.

*Steps 2 and 3.* Option (a): 𝔰 ≤ 𝔰₀^♮ on D^κ_s, so Steps 2 and 3 of the proof of [[prop:tl5-hfs-bootstrap]] apply as
written. Option (b): 𝔰 ≤ 𝔰₀^μ on D^κ_s, and those steps apply with [[lem:tl5-hft-small]] (b) and [[lem:tl5-hft-products]]
in place of [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]]: the terms with ϱ of the family of level j become
μ^(−j/2) μ^(−1/2) Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1) 2k₂ 𝔰 ϱ, which with the weights μ^|I|
contribute at most 2Ω̂² (1/4) μ^(−1/2) 𝔤_(𝒥,s) k₂ ϱ (√e_o + √c √e_i), and so give ε_(w,t) in place of ε_(w,s). In both
options this gives (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,t) + ε_(M,s)) + 𝔯_t Y_s² + (S_(F,s) + S_(M,s)) Y_s³,
and the conclusion follows as there. ∎

**Theorem {#thm:tl5-hft}** (Existence close to an explicit background, with the constants sharpened a third time.) In
the setting of [[thm:tl5-hfs]] (N ≥ 6), with the choices of [[def:tl5-hft-constants]], suppose: (a) η₀ < 𝔰₁^t; (b) the
rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N); (c) 𝔯_(w,s) ≤ 1/4, 𝔰_(*,t) < 𝔰₁^t and the closing
condition

    4 A_t B_t = 8 (√2 δ_w + 2ε_(w,t)) S_(F,s) < 1.                                                  {#eq:tl5-hft-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_t and 𝔰_(*,t) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hfs]] applies with A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]], [[eq:tl5-hft-h1]]
and [[eq:tl5-hft-closing]] in place of A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]], [[eq:tl5-hfs-h1]] and
[[eq:tl5-hfs-closing]]; it uses only 𝔰 ≤ 𝔰_(*,t) < 𝔰₁^t ≤ min(1/16, 𝔰_θ) and the bound Y_σ ≤ 2A_t. ∎

**Theorem {#thm:tl5-hf4t}** (Level four, with the constants sharpened a third time.) In the setting of
[[thm:tl5-hf4s]], with the choices of [[def:tl5-hft-constants]] for N = 4, suppose: (a) η₀ < 𝔰₁^t; (b) the rates a_o,
a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) 𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4, 𝔰_(*,t) < 𝔰₁^t and the closing condition

    4 A_t B_t = 8 (√2 δ_w + 2ε_(w,t) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1.                          {#eq:tl5-hf4t-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_t and 𝔰_(*,t) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4s]] applies with A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]] for N = 4,
[[eq:tl5-hft-h1]] and [[eq:tl5-hf4t-closing]] in place of A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]],
[[eq:tl5-hfs-h1]] and [[eq:tl5-hf4s-closing]]. In option (b), the bound [[eq:tl5-hf4-m2]] used in the proof of
[[lem:tl5-hf4-persistence]] is replaced by |D̂²Ψ_B| ≤ μ^(−2) (2(k₁^μ + 1) 𝒥₁ + 2k₂ ϱ), |B| ≤ 3, from the bound of
M_g^(3) in [[lem:tl5-hft-small]] (b), as 𝒥_g ≤ 𝒥₁; that proof needs only some such bound by a constant. ∎

**Remark {#rem:tl5-hft-what}** (What the third sharpening changes.) In option (a) the smallness 𝔰_(*,t) < 𝔰₁^t carries
the weighted constant C_(∞,μ)^(N−4), with k₁^(N−4,μ) and C₁^♮, in its term with A_t, and the constants of
[[eq:tl5-hfg-cinf]] only in its terms with ϱ and η₀; the factor μ^(−N/2) remains, as the low quantities of order N − 2
are bounded through the energies of level N. In option (b) the threshold 𝔰₁^t is formed with k₃^♮(μ), whose
nonlinear constants carry the weights μ^(b/2) of the background letters and μ^((|C|−|J|)/2) of the couplings 𝔔_CJ, at
the cost of the factor μ^(−N/2) on the terms with ϱ and η₀ of 𝔰_(*,t) and of μ^(−1/2) 𝔤_(𝒥,s) in place of 𝔤_(ϱ,s) in
ε_(w,t). With the Sobolev constants of [[lem:tl5-hft-face]], every constant formed from the Sobolev inequality on a
face, at level four also 𝔛, carries 6C_(E,r)² in place of 6C_(S³)² 𝔭_r, and these constants, 𝔜 and 𝔪 carry the operator
norms 𝔳₀, 𝔴₀ of the comparison of k with h₀ in place of the Euclidean component norms 𝔳, 𝔴; the numbers α, β, ρ of h₀
are free for each face, in (c) for each t. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hft]] and [[thm:tl5-hf4t]] are established in this
paper for no background at 10 l5. [[sec:tl5-hfq]] sharpens the constants at level four a fourth time
([[thm:tl5-hf4q]]).

### The constants at level four sharpened a fourth time {#sec:tl5-hfq}

This section sharpens the constants of [[sec:tl5-hft]] at level four and proves [[thm:tl5-hf4]] with them. Three changes
are made. First, the products of level four with no factor at a point are counted exactly, monomial by monomial, also in
the terms of higher order of N(h), which removes the constant 𝔠^(3♮)₄ and the count 49 from them ([[lem:tl5-hfq-m]]).
Second, the absorption of the nonlinear terms in the recovery of second derivatives is weighted separately for the parts
with the energies and for those with ϱ and η₀, by μ and by μ^θ for a number θ ∈ [0, 1]; for θ = 0 and θ = 1 this gives
the two options of [[lem:tl5-hft-small]], and between them a family of thresholds and of requirements on ϱ and η₀
([[lem:tl5-hfq-theta]]). Third, three constants of the products with no factor at a point lose a count of words or take
the recovery constant of the level where it is used ([[lem:tl5-hfq-mixed]]). The closing condition is
[[eq:tl5-hf4q-closing]]; those of the earlier theorems remain valid. Throughout, N = 4 unless stated otherwise, μ ∈ (0,
1], the notation is that of [[sec:tl5-hfs]] and [[sec:tl5-hft]], with either choice of Sobolev constants made in
[[sec:tl5-hft]], and the second expansion of [[def:tl5-hfg-graded]] is used.

**Lemma {#lem:tl5-hfq-m}** (The products with no factor at a point, counted exactly.) Let h be as in
[[def:tl5-hfg-graded]] with N = 4, p a point with 𝔰(p) ≤ 𝔰_♭, and P₁, P₂ as in [[lem:tl5-hfs-quadratic]] (c). Then at p

    (Σ_(|I|=4) |𝔑^M_I|²)^(1/2) ≤ 𝔠^Mq₁ P₁ + 𝔠^Mq₂ P₂,
    𝔠^Mq₁ := 480 + 96 𝔤₁ (𝔤₀ + √5) 𝔰_♭,      𝔠^Mq₂ := 4 + 4 𝔤₁ 𝔰_♭ (2 + 𝔤₁ 𝔰_♭).                          {#eq:tl5-hfq-m}

*Proof.* By the proof of [[lem:tl5-hfs-quadratic]] (c), the monomials of 𝔑^M_I have b = 0, two high factors carrying all
four letters, which are D̂Ψ_(I_S) and D̂Ψ_(I_(S^c)) with |S| = 2 or Ψ_(I_S) and D̂²Ψ_(I_(S^c)) with |S| = 3, and other
factors carrying no letter; those of Q contribute at most 480 P₁ + 4 P₂. In the terms of R₃ a factor carrying letters is,
in a monomial of 𝔑^M_I, one of the two high factors, since b = 0. So the factors ĝ⁻¹ carry no letter, and a factor g⁻¹
carrying letters contributes one block Ψ_B with r = 1, that is −g⁻¹ Ψ_B g⁻¹, B of length 3, the expansion of
[[lem:tl5-hfs-quadratic]] (a) giving no other monomial of this kind. A factor g⁻¹ = ĝ⁻¹ + H that joins two factors or
raises an index costs at most 𝔤₁, one that may close a trace at most 𝔤₀, and a factor ĝ⁻¹ that carries no letter costs 1
or, in 𝒯_m, √5; and |h| ≤ 𝔰 ≤ 𝔰_♭. In H₂^(λσ) D̂_λD̂_σ h, H₂ = g⁻¹ h ĝ⁻¹ h ĝ⁻¹, the factor D̂²Ψ_(I_(S^c)), |S^c| = 1,
comes from D̂²h, and Ψ_(I_S) from the first h, from the second, or from the factor g⁻¹ as the block −g⁻¹ Ψ_(I_S) g⁻¹; the
three monomials are at most 𝔤₁ 𝔰, 𝔤₁ 𝔰 and 𝔤₁² 𝔰² times |Ψ_(I_S)| |D̂²Ψ_(I_(S^c))|. The terms 2𝔠(H₂)h contain no
derivative D̂, and two high factors Ψ_B would need six letters. In 2𝔮 − 2𝔮̂ = Σ_m c_m (𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹,
H, D̂h, D̂h)), H = −g⁻¹ h ĝ⁻¹, the high pair is D̂Ψ_(I_S), D̂Ψ_(I_(S^c)) from the two factors D̂h, as a factor Ψ_B of
length 3 would be paired with D̂Ψ of length one, which is low; with |H| ≤ 𝔤₁ |h| and Σ |c_m| = 16 these monomials are at
most 16 𝔤₁ 𝔰 (𝔤₀ + √5) |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))|. For fixed S the map I ↦ (I_S, I_(S^c)) is a bijection from the words
of length 4 onto the pairs of words of lengths |S| and 4 − |S|; so Minkowski's inequality over the six sets S with |S| =
2 and the four with |S| = 3 gives [[eq:tl5-hfq-m]]. ∎

**Lemma {#lem:tl5-hfq-theta}** (The absorption weighted in two parts.) Let N ≥ 4, θ ∈ [0, 1] and ν := μ^θ, let g, h,
p, a, b, ϱ(p) and η₀(p) be as in [[lem:tl5-hfs-linfty]], k₃^♮(·) as in [[lem:tl5-hft-small]] (b), and suppose that 𝔰 ≤
𝔰₀^q := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^♮(ν))) on Q(a, b). Then at every point of Q(a, b), for every word C with |C| ≤ j ≤
N − 1,

    |D̂²Ψ_C| ≤ 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ν^(−(|C|+1)/2) ϱ(p);                             {#eq:tl5-hfq-m2}

at p, with the constants of [[eq:tl5-hfs-linfty]] for μ and for ν,

    𝔰(p) ≤ μ^(−N/2) C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2)
           + ν^(−N/2) (C_((∞,ϱ),ν)^(N−4)(p) ϱ(p) + C_((∞,0),ν)^(N−4)(p) η₀(p));                       {#eq:tl5-hfq-small}

the statements of [[lem:tl5-hft-small]] (b) and of [[lem:tl5-hft-products]] hold; and the terms with ϱ(p) of
[[eq:tl5-hfs-products]] hold with μ^((1−θ)n/2) ν^(−1/2) 𝔠^♮_n(ν) in place of μ^(n/2) 𝔠^♮_n and with μ^((n−|J|)/2)
μ^((1−θ)|J|/2) ν^(−1/2) (𝔠^♮_(|J|)(ν) + 1) in place of μ^(n/2) (𝔠^♮_(|J|) + 1).

*Proof.* As k₃^♮(·) is nondecreasing and μ ≤ ν, 𝔰 ≤ 1/(2 sup k₃^♮(μ)); so [[lem:tl5-hft-small]] (b) and
[[lem:tl5-hft-products]] apply. We prove [[eq:tl5-hfq-m2]] by induction on |C|, as [[eq:tl5-hfs-m2]] is proved in
[[lem:tl5-hfs-linfty]], with R_C := 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ν^(−(|C|+1)/2) ϱ(p). The linear part is at
most k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p), and k₂ ϱ(p) ≤ k₂ ν^(−(|C|+1)/2) ϱ(p). In a nonlinear monomial whose
background factors carry b letters, the factor Φ bounded there by 𝔧 is H, Ψ_(C′) or D̂Ψ_(C′) with |C′| ≤ |C| − b, at
most 2μ^(b/2) μ^(−(|C|+1)/2) 𝒥_g, or D̂²Ψ_(C′) with |C′| ≤ |C| − b and |C′| < |C|, at most μ^(b/2) times the part of
R_C with 𝒥_g plus ν^(b/2) times its part with ϱ(p), by the induction hypothesis; the terms H^(αβ) D̂_αD̂_βΨ_J, |J| < |C|,
are of the same kind with b = 0, and the couplings 𝔔_CJ carry μ^((|C|−|J|)/2) ≤ ν^((|C|−|J|)/2). By
[[eq:tl5-hfs-sum]] with ν′ = μ and ν′ = ν, the nonlinear part is at most 𝔰 k₃^♮(μ) (2μ^(−(|C|+1)/2) 𝒥_g + the part of
R_C with 𝒥_g) + 𝔰 k₃^♮(ν) (the part of R_C with ϱ(p)), and 𝔰 k₃^♮(ν) ≤ 1/2 closes the induction.

For [[eq:tl5-hfq-small]] let a_Φ := μ^(−(o+2)/2) and r_Φ := ν^(−(o+2)/2) for a low quantity Φ of order o (for H the
factor 2 of |H| ≤ 2|h| is taken up by 2C_S and 2C_(0,0) in the constants). The steps of the proof of
[[lem:tl5-hft-small]] (a), with [[eq:tl5-hfq-m2]] in place of
[[eq:tl5-hfs-m2]], give for each Φ a bound |Φ(p)| ≤ a_Φ 𝔈 + r_Φ ℜ + 𝔫_Φ, where 2𝔈 := μ^(N/2)·(the part of the right side
of [[eq:tl5-hfq-small]] with ℰ_g) and 2ℜ := ν^(N/2)·(its part with ϱ and η₀) are formed from the linear terms of those
steps: for D̂Ψ_B the part with ϱ of D̂²Ψ_(JB) on the face is at most 2k₂ ν^(−(|B|+3)/2) ϱ(p); for D̂²Ψ_B the jets of the
recovery carry the weights of [[lem:tl5-hfs-linfty]] with μ in their parts with ℰ_g and with ν in their parts with ϱ(p)
and η₀(p), which gives k₁^(N−4,μ) and k₁^(N−4,ν); the part with η₀(p) of Ψ_B is C_(0,0) η₀(p), with 1 ≤ r_Φ, and in that
of D̂Ψ_B, on S_a, a coefficient of the remainder of ℒ^J D̂Ψ_B carrying a ≤ 2 letters is at most Λ_a ≤ ν^(−(|B|+3)/2)
ν^((1+a)/2) Λ_a ≤ ν^(−(|B|+3)/2) Λ₂^ν, which gives r_Φ times the constant C_(1,0) formed with ν. Here 𝔫_Φ = 0 unless
Φ = D̂²Ψ_B, and then 𝔫_Φ is the nonlinear part, whose factor Φ′ of largest order is a low
quantity with a_(Φ′) ≤ μ^(b/2) a_Φ and r_(Φ′) ≤ ν^(b/2) r_Φ, b the letters on the background factors. With t :=
max_Φ |Φ(p)|/(a_Φ 𝔈 + r_Φ ℜ), [[eq:tl5-hfs-sum]] gives 𝔫_Φ ≤ t 𝔰 (k₃^♮(μ) a_Φ 𝔈 + k₃^♮(ν) r_Φ ℜ) ≤ (t/2)(a_Φ 𝔈 + r_Φ ℜ);
so t ≤ 1 + t/2, t ≤ 2, and max_Φ a_Φ ≤ μ^(−N/2), max_Φ r_Φ ≤ ν^(−N/2) give [[eq:tl5-hfq-small]].

In the proof of [[lem:tl5-hfs-products]] a factor Φ₂ = D̂²Ψ_C has, by [[eq:tl5-hfq-m2]], its part with ϱ(p) at most
2k₂ ν^(−ℓ_E(Φ₂)/2) ϱ(p); so the term with ϱ(p) of a monomial with b background letters is at most its background norm
times 𝔰^(q−1) μ^(n/2) ν^(−ℓ_E(Φ₂)/2) 2k₂ ϱ(p), and ℓ_E(Φ₂) ≤ n − b + 1 for b ≥ 1, ℓ_E(Φ₂) ≤ n for b = 0, give
μ^(n/2) ν^(−ℓ_E(Φ₂)/2) ≤
μ^((1−θ)n/2) ν^(−1/2) ν^(b/2); [[eq:tl5-hfs-sum]] with ν′ = ν gives the first replacement, and the term H^(αβ)
D̂_αD̂_βΨ_J, |J| < n, the second. ∎

**Lemma {#lem:tl5-hfq-mixed}** (Three constants of level four.) In the setting of [[lem:tl5-hfs-mixed]], with 𝔰 ≤
𝔰₀^q on Q(t, b), put λ_t^(μ,2) := 2([k₁^(2,μ)]_t + 1) and

    𝔛^q_(1,t) := (𝔭₃ 𝔵₃(t) (1 + [ϖ₁]_t))^(1/2),
    𝔛^q_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (2 [ϖ₂]_t)^(1/2)),      𝔜^q_(1,t) := 𝔱₃(t)^(1/2) (1 + 7λ_t^(μ,2)),

𝔭_r standing for 12 C_(E,r)² with the intrinsic Sobolev constants. Then [[eq:tl5-hfs-mixed]] holds with 𝔛^q_(1,t),
𝔛^q_(2,t) and 𝔜^q_(1,t) in place of 𝔛_(1,t), 𝔛_(2,t) and 𝔜_(1,t).

*Proof.* In the proof of [[lem:tl5-hfs-mixed]], for a rotation word J and a monomial of the remainder R′ of ℒ^J D̂Ψ_B,
the solution factor is Ψ_(σB), σ the subword of J left by the coefficient, and B ↦ σB is injective; so, by Minkowski's
inequality over the monomials and the weights as there, μ² (Σ_(|B|=2) |R′|²)^(1/2) ≤ ρ′_(|J|) 𝒥_g, and summing over J,
μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2ϖ₁ 𝒥_g², without the count 49 of the words B. Likewise Z ↦ σZ is injective in the
remainders R of ℒ^J D̂²Ψ_Z, whose solution factors are D̂Ψ_(σZ) or Ψ_(σZ), which removes the count 7 of the fields Z from
their part: μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 2ϖ₂ 𝒥_g². In the bound of Y₁ only D̂²Ψ_B with |B| = 2 occurs, and
μ^(3/2) |D̂²Ψ_B| ≤ M_g^(2) ≤ 2(k₁^(2,μ) + 1) 𝒥_g + 2k₂ ϱ by [[lem:tl5-hft-small]] (b); so ‖M_g^(2)‖_Σ ≤ λ_t^(μ,2) 𝔍_g +
ς_t ϱ takes the place of the bound of ‖M_g‖_Σ there. The rest of that proof holds as written, its bound of ‖M_g‖_Σ
holding by [[lem:tl5-hfq-theta]]. ∎

**Definition {#def:tl5-hfq-constants}** (The constants at level four sharpened a fourth time.) Let N = 4 and the
setting be that of [[def:tl5-hfs-constants]], with its constants formed with the chosen Sobolev constants; fix θ ∈
[0, 1] and put ν := μ^θ, 𝔰₀^q as in [[lem:tl5-hfq-theta]] with the supremum over D^κ, 𝔰₁^q := min(𝔰₀^q/2, c_* κ_m/2,
𝔰_θ), 𝔰_θ being that of [[def:tl5-hf-constants]], which does not depend on θ, and, with the notation of
[[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]],

    𝔤_(ϱ,q) := ν^(−1/2) (Σ_(j≤4) (Σ_(j′≤j) μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(ν) + 1))²)^(1/2),
    ε_(w,q) := 𝒮[s₄[2R̂ic] + (1/4) min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) k₂ ϱ],
    S_(M,q) := μ^(−3/2) ∫_(−10)^(u*) w_t (𝔠^Mq₁ 𝔛^q_(1,t) 𝔜^q_(1,t) + 𝔠^Mq₂ 𝔛^q_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_(M,q) := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) (𝔠^Mq₁ 𝔛^q_(1,t) (𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀)
               + 𝔠^Mq₂ (𝔛^q_(2,t) 𝔜″_(2,t) η₀ + 𝔛′_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_(M,q) := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t 𝔠^Mq₂ 𝔛′_(2,t) 𝔜″_(2,t) dt,
    A_q := √2 δ_w + 2ε_(w,q) + 2ε_(M,q),      B_q := 2 (S_(F,s) + S_(M,q)),      𝔯_q := 𝔯_(w,s) + 𝔯_(M,q),
    𝔰_(*,q) := sup_(p∈D^κ) (2 C_(∞,μ)^(0)(p) μ^(−2) e^(φ(p)/2) A_q
               + ν^(−2) (C_((∞,ϱ),ν)^(0)(p) ϱ(p) + C_((∞,0),ν)^(0)(p) η₀)).                       {#eq:tl5-hfq-constants}

**Proposition {#prop:tl5-hfq-bootstrap}** (The a priori estimate at level four, sharpened a fourth time.) In the
setting of [[def:tl5-hfq-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴) and
that 𝔯_q ≤ 1/4, η₀ < 𝔰₁^q and 𝔰_(*,q) < 𝔰₁^q. Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_q for
every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,q) on D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_q + B_q Y_s(g)².                                                                          {#eq:tl5-hfq-h1}

*Proof.* Step 1 is that of the proof of [[prop:tl5-hft-bootstrap]] with 𝔰₀^q, 𝔰₁^q, A_q, 𝔰_(*,q) and [[eq:tl5-hfq-small]]
in place of the quantities of option (b), as 𝔰₁^q ≤ 𝔰₀^q/2: it gives 𝔰 ≤ 𝔰_(*,q) < 𝔰₁^q on D^κ_s, |h|_k̂ < κ_m/2 and θ_H
≤ ϑ. Steps 2 and 3 are those of option (b) there, by [[lem:tl5-hfq-theta]], with two changes. The terms with ϱ of the
family of level j are bounded either as there or by [[lem:tl5-hfq-theta]], which gives μ^(−j/2) ν^(−1/2) Σ_(j′≤j)
μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(ν) + 1) 2k₂ 𝔰 ϱ and, with the weights μ^|I|, the contribution 2Ω̂² (1/4) 𝔤_(ϱ,q)
k₂ ϱ (√e_o + √c √e_i); either bound may be used, which gives ε_(w,q). The terms 𝔑^M_I are bounded as in the proof of
[[prop:tl5-hfs-bootstrap]] with [[eq:tl5-hfq-m]] and [[lem:tl5-hfq-mixed]] in place of [[eq:tl5-hfs-m]] and of the
constants 𝔛_(1,t), 𝔛_(2,t), 𝔜_(1,t) of [[lem:tl5-hfs-mixed]], which gives S_(M,q) Y_s³ + 𝔯_(M,q) Y_s² + ε_(M,q) Y_s. So
(1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,q) + ε_(M,q)) + 𝔯_q Y_s² + (S_(F,s) + S_(M,q)) Y_s³, and the conclusion
follows as there. ∎

**Theorem {#thm:tl5-hf4q}** (Level four, with the constants sharpened a fourth time.) In the setting of
[[thm:tl5-hf4t]], with θ and the choices of [[def:tl5-hfq-constants]], suppose: (a) η₀ < 𝔰₁^q; (b) the rates a_o, a_i
are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) 𝔯_(w,s) + 𝔯_(M,q) ≤ 1/4, 𝔰_(*,q) < 𝔰₁^q and the closing condition

    4 A_q B_q = 8 (√2 δ_w + 2ε_(w,q) + 2ε_(M,q)) (S_(F,s) + S_(M,q)) < 1.                          {#eq:tl5-hf4q-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_q and 𝔰_(*,q) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4t]] in option (b) applies with A_q, B_q, 𝔰_(*,q), 𝔰₁^q, [[prop:tl5-hfq-bootstrap]],
[[eq:tl5-hfq-h1]] and [[eq:tl5-hf4q-closing]] in place of A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]],
[[eq:tl5-hft-h1]] and [[eq:tl5-hf4t-closing]]: it uses 𝔰 ≤ 𝔰_(*,q) < 𝔰₁^q ≤ min(1/16, 𝔰_θ), the bound Y_σ ≤ 2A_q and the
bound of M_g^(3) of [[lem:tl5-hft-small]] (b), which holds as 𝔰 ≤ 1/(2 sup k₃^♮(μ)). ∎

**Remark {#rem:tl5-hfq-what}** (What the fourth sharpening changes.) The products of level four with no factor at a
point carry 𝔠^Mq₁ = 480 + 96 𝔤₁ (𝔤₀ + √5) 𝔰_♭ and 𝔠^Mq₂ = 4 + 4 𝔤₁ 𝔰_♭ (2 + 𝔤₁ 𝔰_♭), in place of 49 𝔰_♭ [𝔠^(3♮)₄]_t
added to 480 and 4. The number θ moves the threshold and the requirements on ϱ and η₀ together: 𝔰₁^q is formed with
k₃^♮(μ^θ), and the terms with ϱ and η₀ of 𝔰_(*,q) carry μ^(−2θ); θ = 0 gives the threshold of option (a) of
[[def:tl5-hft-constants]] with μ⁰ on these terms, and θ = 1 option (b). The factor μ^(−2) of the term with A_q
remains for the reason given in [[rem:tl5-hft-what]]. In 𝔜^q_(1,t) the recovery constant is that of level two, and
𝔛^q_(1,t), 𝔛^q_(2,t) carry no count of the words B and of the fields Z in their parts with ϖ₁ and ϖ₂. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hf4q]] are established in this paper for no
background at 10 l5. [[sec:tl5-hfv]] sharpens the constants a fifth time, at levels four and N ≥ 6
([[thm:tl5-hfv]]).

### The constants sharpened a fifth time {#sec:tl5-hfv}

This section sharpens the constants of [[sec:tl5-hft]] (level N ≥ 6) and of [[sec:tl5-hfq]] (level four) in four ways
and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with them. First, the number ϑ of the quasilinear term is replaced by two
numbers ϑ₁, ϑ₂ ∈ (0, 1), one for each family of faces, and the bootstrap is closed with η = 1 − max(ϑ₁, ϑ₂) − 𝔯^v in
place of the bounds ϑ ≤ 1/4 and 𝔯 ≤ 1/4; this frees the cap 𝔰_θ of the smallness condition and the factor 8√2 of the
closing condition ([[lem:tl5-hfv-close]]). Second, the conversion of the high factor into the densities is made
separately for the two families of faces ([[lem:tl5-hfv-conv]]). Third, |H| ≤ 𝔤₁ |h| replaces |H| ≤ 2|h| in the constant
𝔨_B. Fourth, at level four the recovery of D̂²h at a point is bounded term by term ([[lem:tl5-hfv-rec]]). The closing
conditions are [[eq:tl5-hfv-closing]]; the earlier ones remain valid. Throughout, the notation is that of
[[sec:tl5-hfs]], [[sec:tl5-hft]] and [[sec:tl5-hfq]].

**Lemma {#lem:tl5-hfv-close}** (Two numbers for the quasilinear term.) Let ϑ₁, ϑ₂ ∈ (0, 1), and put

    θ_H^(1) := (√2 + 1/2) |H| (c + κ′)/min(c, κ′),      θ_H^(2) := (√2 + 1/2) |H| (1 + κc)/(κc),
    𝔰_(θ,v) := min(ϑ₁ (√2 + 1/2)⁻¹ inf_(D^κ) min(c, κ′)/(c + κ′),
                   ϑ₂ (√2 + 1/2)⁻¹ inf_(D^κ) κc/(1 + κc)).                                              {#eq:tl5-hfv-cap}

If |H| ≤ 𝔰_(θ,v) at a point, then θ_H^(1) ≤ ϑ₁ and θ_H^(2) ≤ ϑ₂ there; the face densities of J̃ := J[Ψ] − 𝔟[Ψ] on the
faces Σ₁ and Σ₂ are at least (1 − ϑ₁) ε₁[Ψ] and (1 − ϑ₂) ε₂[Ψ]; and for rates a_o, a_i and φ as in
[[prop:tl5-hf-linear]],

    2Ω̂² |dφ(𝔟[Ψ])| ≤ ϑ₁ a_o (e_o + κ′ e_i) + ϑ₂ a_i (e_i + κ e_o).                                    {#eq:tl5-hfv-dphi}

So if the rates â_o := (1 − ϑ₁) a_o and â_i := (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N), then the linear
bulk ñᵀ 𝔅_N ñ − 2Ω̂² dφ(J̃) of the proof of [[prop:tl5-hf-bootstrap]] is at most 0. Finally, if Y ≥ 0 satisfies η Y² ≤
δ² + Y ε + S Y³ with η > 0 and δ, ε, S ≥ 0, then Y ≤ A + B Y² with A := η^(−1/2) δ + η⁻¹ ε and B := η⁻¹ S.

*Proof.* The proof of [[lem:tl5-hf-quasilinear]] (b) gives 2Ω̂² |dτ₁(𝔟)| ≤ θ_H^(1) (e_o + κ′ e_i) and 2Ω̂² |dτ₂(𝔟)| ≤
θ_H^(2) (e_i + κ e_o) separately, and the definition of 𝔰_(θ,v) gives the first claim. The face densities are those of
the proof of [[prop:tl5-hf-bootstrap]], Step 2, with θ_H^(1) and θ_H^(2) in place of θ_H. As dφ = a_o dτ₁ + a_i dτ₂,
[[eq:tl5-hfv-dphi]] follows; and 2Ω̂² dφ(J) = (a_o + κ a_i) e_o + (a_i + κ′ a_o) e_i, so 2Ω̂² dφ(J̃) ≥ (â_o + κ â_i)
e_o + (â_i + κ′ â_o) e_i, which dominates ñᵀ 𝔅_N ñ by the admissibility of â_o, â_i. For the last claim, if Y ≥ η^(−1/2)
δ, then Y ≤ η⁻¹ δ²/Y + η⁻¹ ε + η⁻¹ S Y² ≤ A + B Y², and otherwise Y < A. ∎

**Lemma {#lem:tl5-hfv-conv}** (The conversion into the densities, by families.) Let A := 1/z̲ + 1/c and 𝔣₂ be as in
[[def:tl5-hfs-constants]]; at the points where c/z̲² + 1/z̲ ≤ 2 put

    𝔣₂^o := √2 Ω̂ (A (1 + cA))^(1/2),      𝔣₂^i := √2 Ω̂ (1/A + c)^(1/2),

and at the other points 𝔣₂^o := 𝔣₂^i := 𝔣₂. Then 𝔣₂^o ≤ 𝔣₂ and 𝔣₂^i ≤ 𝔣₂ everywhere, and for every family of fields as
in [[prop:tl5-hf-linear-n]], with 𝒥_g and the weighted sums e_o, e_i of it, 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂^o e_o +
𝔣₂^i e_i.

*Proof.* By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ A e_o + e_i, and by the Cauchy–Schwarz inequality √e_o + √c √e_i ≤ (1/A +
c)^(1/2) (A e_o + e_i)^(1/2); so 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ √2 Ω̂ (1/A + c)^(1/2) (A e_o + e_i), which is the claim at
the points where c/z̲² + 1/z̲ ≤ 2. There A(1 + cA) − 2(1 + A) = A(cA − 1) − 2 = c/z̲² + 1/z̲ − 2 ≤ 0, as cA = 1 + c/z̲,
so 𝔣₂^o ≤ 𝔣₂; and 1/A + c ≤ 2c < 1, as 1/A < c < 1/2, so 𝔣₂^i < 𝔣₂. At the other points the claim is the bound
2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂ (e_o + e_i) of Step 2 of the proof of [[prop:tl5-hfg-bootstrap]]. ∎

**Lemma {#lem:tl5-hfv-rec}** (The recovery of D̂²h at a point, term by term.) Let N = 4 and put 𝔷₁ := 3 max_Z |D̂Z| and
𝔷₂ := 2 max_Z |D̂²Z|, and, with the constants of [[lem:tl5-hfs-linfty]] (C₁ := C₁^♮, C_(1,0) := C_(1,0)^♮),

    𝔨_rec := (6/5) ((√3 + 8/3) K_rec √7 (C₁ + 𝔷₁ μ^(1/2) C₁ + 𝔷₂ μ C_S) + μ 𝔯₀ C_S),
    𝔨_rec^ϱ := (6/5) (√3 + 8/3) K_rec √7 (1 + 𝔷₁ μ^(1/2)) C_(1,ϱ),
    𝔨_rec^0 := (6/5) ((√3 + 8/3) K_rec √7 ((1 + 𝔷₁ μ^(1/2)) C_(1,0) + 𝔷₂ μ C_(0,0)) + μ 𝔯₀ C_(0,0)),
    C_P^v := 2 max(2C_S, C₁, 𝔨_rec),   C_(P,ϱ)^v := 2 max(C_(1,ϱ), 𝔨_rec^ϱ + k₂),
    C_(P,0)^v := 2 max(2C_(0,0), C_(1,0), 𝔨_rec^0).

In the setting of [[lem:tl5-hfs-linfty]] or of [[lem:tl5-hft-small]] (b), the bound of 𝔰_P = 𝔰_g^(0) of
[[eq:tl5-hfs-linfty]] holds with C_P^v, C_(P,ϱ)^v and C_(P,0)^v in place of C_P^♮, C_(P,ϱ)^♮ and C_(P,0)^♮.

*Proof.* In the step on second derivatives at low levels of the proof of [[lem:tl5-hfs-linfty]] with B = ∅, the bound of
[[lem:tl5-hf-recovery]] for h, as used in the proof of [[lem:tl5-hf-linfty]], is (6/5) times (√3 + 8/3) K_rec
((Σ_Z |D̂Ψ_Z|²)^(1/2) + (Σ_Z 𝔷_Z²)^(1/2)) + (4/3)|𝔣| + 𝔯₀ |h|, with (Σ_Z 𝔷_Z²)^(1/2) ≤ √7 (𝔷₁ |D̂h| + 𝔷₂ |h|), and 𝔣 has
no part 𝔄 at level zero. Multiply by μ² and bound each jet by its weighted bound at p: μ² |D̂Ψ_Z| ≤ C₁ ℰ_g^(1/2) +
C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p) for the seven fields Z, μ² |D̂h| ≤ μ^(1/2) times that bound, and μ² |h| ≤ μ (C_S ℰ_g^(1/2) +
C_(0,0) η₀(p)), in place of the bound of L_g by (2𝔐^(0))^(1/2) times the largest of them; the residual and the nonlinear
terms are as there. Taking the largest of the four bounds and absorbing 𝔰_g^(0)/2 as there gives the claim. ∎

**Definition {#def:tl5-hfv-constants}** (The constants sharpened a fifth time.) Let N ≥ 6 and the constants be those of
[[def:tl5-hft-constants]] with either option, or N = 4 and those of [[def:tl5-hfq-constants]] for some θ ∈ [0, 1]. Fix
ϑ₁, ϑ₂ ∈ (0, 1). Form the same constants with the following replacements, and call them the constants with index v:
𝔰_θ by 𝔰_(θ,v) in 𝔰₁ (that is in 𝔰₁^t or 𝔰₁^q); in 𝔞_(o,s) and 𝔟_(o,s) the factor 𝔣₂ by 𝔣₂^o, and in 𝔞_(i,s) and
𝔟_(i,s) by 𝔣₂^i; 𝔨_B by max(𝔷, 𝔤₁) in 𝔎, 𝔎_ϱ and 𝔎₀; and, for N = 4, C_P^♮, C_(P,ϱ)^♮ and C_(P,0)^♮ by C_P^v,
C_(P,ϱ)^v and C_(P,0)^v of [[lem:tl5-hfv-rec]]. With the resulting S_F^v := S_(F,s), S_M^v := S_(M,q) (0 for N ≥ 6),
ε^v := ε_(w,t) or ε_(w,q), ε_M^v := ε_(M,q) (0 for N ≥ 6), 𝔯^v := 𝔯_t or 𝔯_q, 𝔰₁^v and 𝔰_*^v (with A_v in place of A_t or
A_q), put

    η := 1 − max(ϑ₁, ϑ₂) − 𝔯^v,      A_v := η^(−1/2) δ_w + η⁻¹ (ε^v + ε_M^v),
    B_v := η⁻¹ (S_F^v + S_M^v).                                                                   {#eq:tl5-hfv-constants}

**Theorem {#thm:tl5-hfv}** (Existence close to an explicit background, with the constants sharpened a fifth time.) In
the setting of [[thm:tl5-hft]] (N ≥ 6) or of [[thm:tl5-hf4q]] (N = 4), with ϑ₁, ϑ₂ ∈ (0, 1) in place of ϑ and the
constants with index v of [[def:tl5-hfv-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i
are admissible for (𝔅_N, E_o^N, E_i^N); (c) η > 0, 𝔰_*^v < 𝔰₁^v and the closing condition

    4 A_v B_v = 4 η^(−3/2) (δ_w + η^(−1/2) (ε^v + ε_M^v)) (S_F^v + S_M^v) < 1.                      {#eq:tl5-hfv-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_v and 𝔰_*^v in place of A_w (or
A_(w,4)) and 𝔰_*.

*Proof.* The proofs of [[prop:tl5-hft-bootstrap]] and [[prop:tl5-hfq-bootstrap]] apply with the following changes.
Step 1 uses only 𝔰_*^v < 𝔰₁^v, and gives |H| ≤ 𝔰 < 𝔰_(θ,v) on D^κ_s, so θ_H^(1) ≤ ϑ₁ and θ_H^(2) ≤ ϑ₂ by
[[lem:tl5-hfv-close]]. In Step 2 the face densities of J̃ are at least (1 − ϑ₁) ε₁ and (1 − ϑ₂) ε₂, and the linear bulk
with the weight is at most 0 by [[lem:tl5-hfv-close]] and (b); the conversion of the terms with 𝒥_g uses
[[lem:tl5-hfv-conv]], so 𝔣₂^o multiplies the densities e_o and 𝔣₂^i the densities e_i; in the bound of a factor H by the
energies, |H| ≤ 𝔤₁ |h|, as H = −g⁻¹ h ĝ⁻¹ and a factor g⁻¹ raising an index costs at most 1 + |H| ≤ 𝔤₁; and for N = 4,
[[lem:tl5-hfv-rec]] bounds 𝔰_P. Step 3 then gives (1 − max(ϑ₁, ϑ₂)) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε^v + ε_M^v) +
𝔯^v Y_s² + (S_F^v + S_M^v) Y_s³, and taking the supremum, η Y_s² ≤ δ_w² + Y_s (ε^v + ε_M^v) + (S_F^v + S_M^v) Y_s³; the
last claim of [[lem:tl5-hfv-close]] gives Y_s ≤ A_v + B_v Y_s². The rest is the proof of [[thm:tl5-hft]] or
[[thm:tl5-hf4q]] with A_v, B_v and [[eq:tl5-hfv-closing]]; the proofs of persistence use only |H| ≤ 1/8 and θ_H ≤ ϑ on
each family of faces, and their choice of rates holds with (1 − ϑ₁) a_o, (1 − ϑ₂) a_i in place of (1 − ϑ) a_o, (1 − ϑ)
a_i. ∎

**Remark {#rem:tl5-hfv-what}** (What the fifth sharpening changes.) With ϑ₁ = ϑ₂ = 1/4 and 𝔯^v = 1/4, η = 1/2 and
[[eq:tl5-hfv-closing]] is the form 8(√2 δ_w + 2(ε^v + ε_M^v))(S_F^v + S_M^v) < 1 of the earlier theorems; smaller ϑ₁,
ϑ₂ and 𝔯^v let η approach 1 and lower the factors 8√2 of δ_w and 16 of ε^v + ε_M^v towards 4, and larger ϑ₁, ϑ₂ raise
the cap 𝔰_(θ,v) at the cost of η and of larger rates a_o = â_o/(1 − ϑ₁), a_i = â_i/(1 − ϑ₂). The cap on the faces Σ₂
carries κc/(1 + κc), as the density e_i + κ e_o of these faces controls the derivative along ê₄ only through κ e_o; the
numbers κ, κ′ of [[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfv]] are established in this paper for no background at 10 l5. [[sec:tl5-hfw]] sharpens the
terms with ϱ ([[thm:tl5-hfw]]).

### The terms with ϱ, sharpened {#sec:tl5-hfw}

In the proofs of [[prop:tl5-hf-bootstrap]] and of all its sharpened forms, the part with ϱ of the nonlinear terms (at
level four, of those other than the terms 𝔑^M_I, whose parts with ϱ go into 𝔯_M and ε_M) is a product of the residual
with a solution factor bounded by 𝔰, and it is bounded there by (1/4) k₂ ϱ through 𝔰 ≤ 1/8. After Step 1 of the proof
of [[thm:tl5-hfw]], 𝔰 is at most 𝔰_*^w < 𝔰₁^v on D^κ_s; this section uses that bound instead, at level four and at level
N ≥ 6, which multiplies the coefficient of ϱ in the error ε by 8𝔰₁^v. The closing condition is [[eq:tl5-hfw-closing]];
the earlier ones remain valid. The notation is that of [[sec:tl5-hfv]].

**Definition {#def:tl5-hfw-constants}** (The constants with the terms with ϱ sharpened.) In the setting of
[[def:tl5-hfv-constants]], let 𝔤_ϱ^v be the factor that multiplies (1/4) k₂ ϱ in ε^v: 𝔤_(ϱ,s) for N ≥ 6 with option (a)
of [[def:tl5-hft-constants]], μ^(−1/2) 𝔤_(𝒥,s) with option (b), and min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) for N = 4. Put

    ε^w := 𝒮[s_N[2R̂ic] + 2𝔰₁^v 𝔤_ϱ^v k₂ ϱ],      A_w^v := η^(−1/2) δ_w + η⁻¹ (ε^w + ε_M^v),            {#eq:tl5-hfw-eps}

and let 𝔰_*^w be 𝔰_*^v with A_w^v in place of A_v.

**Theorem {#thm:tl5-hfw}** (Existence close to an explicit background, with the terms with ϱ sharpened.) In the
setting of [[thm:tl5-hfv]], suppose (a) and (b) of that theorem and (c) η > 0, 𝔰_*^w < 𝔰₁^v and the closing condition

    4 A_w^v B_v = 4 η^(−3/2) (δ_w + η^(−1/2) (ε^w + ε_M^v)) (S_F^v + S_M^v) < 1.                    {#eq:tl5-hfw-closing}

Then the conclusions of [[thm:tl5-hfv]] hold with A_w^v and 𝔰_*^w in place of A_v and 𝔰_*^v.

*Proof.* The proof of [[thm:tl5-hfv]] applies with ε^w, A_w^v and 𝔰_*^w in place of ε^v, A_v and 𝔰_*^v, with one change
in Step 2. Step 1 uses only 𝔰_*^w < 𝔰₁^v and gives 𝔰 ≤ 𝔰_*^w < 𝔰₁^v on D^κ_s. In Step 2, the nonlinear terms of level j
other than 𝔑^M_I contribute to the bulk a part with 𝒥_g, bounded as there, and a part 2Ω̂² 𝔤_ϱ^v 2k₂ 𝔰 ϱ (√e_o + √c
√e_i): in each monomial the factor bounded by its part with ϱ is multiplied by a factor Φ₁ with |Φ₁| ≤ 𝔰, or, in
H^(αβ) D̂_αD̂_βΨ_J, by H with |H| ≤ 𝔰, as in the proofs of [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and
[[lem:tl5-hfq-theta]]; the constant 𝔤_ϱ^v is the one of those proofs, and the terms 𝔑^M_I are bounded as there. There
the bound 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ was used; we use 2k₂ 𝔰 ϱ ≤ 2𝔰₁^v k₂ ϱ, by Step 1. As in the proof of
[[prop:tl5-hf-linear]], this part together with the forcing term 2Ω̂² s_N[2R̂ic] (√e_o + √c √e_i) is bounded by
Y_s ε^w, in place of Y_s ε^v. ∎

**Remark {#rem:tl5-hfw-what}** (The split of the error.) The residual enters the hypotheses of [[thm:tl5-hfw]] through
ε^w and ε_M^v, and through ϱ also in 𝔯^v, and so in η, and in 𝔰_*^w. As 𝒮 is subadditive and positively homogeneous,
ε^w ≤ 𝒮[s_N[2R̂ic]] + 2𝔰₁^v ϱ 𝒮[𝔤_ϱ^v k₂], and the hypotheses hold whenever they hold with ε^w replaced by this sum; so
any bounds of 𝒮[s_N[2R̂ic]] and of ϱ with which they hold are admissible, and the theorem does not fix their ratio. The
coefficient 2𝔰₁^v 𝒮[𝔤_ϱ^v k₂] of ϱ there is 8𝔰₁^v times the one for ε^v, where 𝔰₁^v ≤ 𝔰_♭/2 ≤ 1/16. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfw]] are established in this paper for no background
at 10 l5. [[sec:tl5-hfx]] counts the first-order constant over the words ([[thm:tl5-hfx]]).

### The first-order constant, counted over the words {#sec:tl5-hfx}

In the first-order step of the proof of [[lem:tl5-hf-linfty]], and in its weighted forms, each of the 43 words J of
rotations with |J| ≤ 2 is bounded by the whole of 𝒥₁, which gives the factor 258 = 6 · 43 of C₁. This section counts
the terms that are first derivatives over the words, as the words JB are distinct, and keeps the count 43 only for the
second derivatives, which are bounded through their maximum; it applies to the constant C₁^♮ of [[lem:tl5-hfs-linfty]]
with either choice of Sobolev constants, at every level N ≥ 4. The notation is that of [[sec:tl5-hfw]].

**Lemma {#lem:tl5-hfx-c1}** (The first-order constant.) Let ρ′₁ := 2μΛ₁, ρ′₂ := 4μΛ₁ + 2μ^(3/2)Λ₂ and ϖ′ := 6ρ′₁² +
36ρ′₂², and let C₁^x be the smaller of C₁^♮ and the number formed as C₁^♮ with (1 + ϖ′^(1/2))²/43 in place of
(1 + 6Λ₂^μ)² and with (2(43)^(1/2)(k₁^μ + 1) + (2ϖ′)^(1/2))²/43 in place of 72(Λ₂^μ)² + 8(k₁^μ + 1)²:

    C₁^x² = min(C₁^♮², 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))²
            + 4|∂_γ|² (2(43)^(1/2) (k₁^μ + 1) + (2ϖ′)^(1/2))²)),                                        {#eq:tl5-hfx-c1}

6C² 𝔴⁶ 𝔳⁶ standing for 6C_(S³)² 𝔭₃ 𝔴⁶ 𝔳⁶ or 6C_(E,3)² 𝔴₀⁶ 𝔳₀⁶. Then [[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] and
[[lem:tl5-hfq-theta]] hold with C₁^x in place of C₁^♮.

*Proof.* In the first-order step for A := D̂Ψ_B, |B| ≤ N − 3, write ℒ^J A = D̂Ψ_(JB) + R′_J and D̂ℒ^J A = D̂²Ψ_(JB) +
D̂R′_J. The words JB are distinct for distinct J, so Σ_J μ^(|B|+3) |D̂Ψ_(JB)|² ≤ 𝒥_g², as μ^(|B|+3) ≤ μ^(|JB|). By
[[lem:tl5-hfs-quadratic]] (a) with Ψ_B in place of h, R′_J has 2 monomials whose coefficient carries one letter if |J| =
1, and 4 with one letter and 2 with two letters if |J| = 2, each contracted with a Ψ_C, |C| = |JB| − a; with μ^(|B|+3)
≤ μ^(1+a) μ^(|C|), μ^((|B|+3)/2) |R′_J| ≤ ρ′_(|J|) 𝒥_g and μ^((|B|+3)/2) |D̂R′_J| ≤ √2 ρ′_(|J|) 𝒥_g, so that, by
Minkowski's inequality over the words, (Σ_J μ^(|B|+3) |ℒ^J A|²)^(1/2) ≤ (1 + ϖ′^(1/2)) 𝒥_g and (Σ_J μ^(|B|+3) |D̂ℒ^J
A|²)^(1/2) ≤ 43^(1/2) max_J μ^((|B|+3)/2) |D̂²Ψ_(JB)| + (2ϖ′)^(1/2) 𝒥_g. By [[eq:tl5-hfs-m2]] (or [[eq:tl5-hfq-m2]], or
the bound of M_g in [[lem:tl5-hft-small]] (b)), μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ 2(k₁^μ + 1) 𝒥_g + (its part with ϱ). In the
Sobolev inequality [[eq:tl5-hf-cs-r]] (or that of [[lem:tl5-hft-face]]) with r = 3, insert these bounds in place of
the bounds of the 43 words by 𝒥 used in the proof of [[lem:tl5-hf-linfty]], separate the parts with 𝒥_g from those with
ϱ by (x + y)² ≤ 2x² + 2y² as there, and use ∫ 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g; this gives the part with ℰ_g of the
bound with the second entry of [[eq:tl5-hfx-c1]], and parts with ϱ and η₀ at most those of that proof, the part with ϱ
being 2^(−1/2) times it. The bound with C₁^♮ holds as well, with the same parts with ϱ and η₀; so it holds with C₁^x. ∎

**Theorem {#thm:tl5-hfx}** (Existence with the first-order constant counted over the words.) The conclusions of
[[thm:tl5-hfw]] hold under its hypotheses with every constant formed with C₁^x in place of C₁^♮, in particular in C_P^v
(directly, and at level four also through 𝔨_rec), hence in 𝔎 and S_F^v, and in C_(∞,μ)^(N−4) of 𝔰_*^w.

*Proof.* The proofs of [[thm:tl5-hfw]] and of the results it rests on use C₁^♮ only through the bounds of
[[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] and [[lem:tl5-hfq-theta]], which hold with C₁^x by [[lem:tl5-hfx-c1]]. ∎

**Remark {#rem:tl5-hfx-what}** (What changes.) In the second entry of [[eq:tl5-hfx-c1]] the count 43 remains only with
the recovery constant k₁^μ, whose coefficient is 4 · 43 · 4 against 4 · 43 · 8 in C₁^♮; the terms without k₁^μ carry
(1 + ϖ′^(1/2))² and 4|∂_γ|² · 2ϖ′ against 43(1 + 6Λ₂^μ)² and 4|∂_γ|² · 43 · 72(Λ₂^μ)², and the cross term
4|∂_γ|² · 4 · 43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2) has no counterpart. As ϖ′ ≤ 1320(Λ₂^μ)², the second entry is the smaller if
8Λ₂^μ ≤ k₁^μ + 1 on Σ₁(a, b); otherwise the cross term can make it the larger, and the minimum keeps C₁^x ≤ C₁^♮. As
for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfx]] are established in this paper for no
background at 10 l5. [[sec:tl5-hfy]] absorbs the nonlinear terms with the bootstrap's smallness ([[thm:tl5-hfy]]).

### The absorption with the bootstrap's smallness {#sec:tl5-hfy}

In the recovery of second derivatives and in the bounds at a point of [[sec:tl5-hfs]], [[sec:tl5-hft]],
[[sec:tl5-hfq]], [[sec:tl5-hfv]] and [[sec:tl5-hfx]], the nonlinear terms are absorbed with k₃𝔰 ≤ 1/2, which gives the
factors 2 in 2(k₁ + 1), in 2k₂ and in front of the maxima of the constants C_∞. After Step 1 of the bootstrap, 𝔰 is at
most 𝔰₁^v; this section runs the bootstrap with that smallness as the hypothesis of the bounds at a point, so that the
absorption costs 1/(1 − 𝔵) with 𝔵 := 𝔰₁^v sup_(D^κ) k₃ ≤ 1/4 in place of 2, at every level N ≥ 4. The notation is that
of [[sec:tl5-hfx]].

**Lemma {#lem:tl5-hfy-abs}** (Absorption with the smallness of the bootstrap.) Let k₃ denote the constant of the
absorption in the chosen set (k₃^♮ for option (a) of [[def:tl5-hft-constants]], k₃^♮(μ) for option (b), k₃^♮(ν) at
level four), 𝔰₁^v as in [[def:tl5-hfv-constants]] and 𝔵 := 𝔰₁^v sup_(D^κ) k₃, so 𝔵 ≤ 1/4 as 𝔰₁^v ≤ 𝔰₀/2. If 𝔰 ≤ 𝔰₁^v on
Q(a, b), then the lemmas that the chosen set uses hold with the replacements below: [[lem:tl5-hfs-linfty]],
[[lem:tl5-hft-small]] (a) and [[lem:tl5-hfs-products]] for option (a); [[lem:tl5-hft-small]] (b) and
[[lem:tl5-hft-products]] for option (b); these, [[lem:tl5-hfq-theta]], [[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]]
at level four; and [[lem:tl5-hfv-rec]] and [[lem:tl5-hfx-c1]]. The replacements are 2(k₁^(j,·) + 1) by
(k₁^(j,·) + 2𝔵)/(1 − 𝔵) and 2k₂ by k₂/(1 − 𝔵) in [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] and the bounds of M_g^(j), and
hence wherever these bounds enter: in 𝔨_A, λ_t^μ and λ_t^(μ,2); in C₁^x, where 2(43)^(1/2)(k₁^μ + 1) becomes
(43)^(1/2)(k₁^μ + 2𝔵)/(1 − 𝔵); in ς_t, 2[k₂]_t by [k₂]_t/(1 − 𝔵); in C_(1,ϱ), 32k₂² by 8k₂²/(1 − 𝔵)²; and in the terms
with ϱ of the products, 2k₂ 𝔰 ϱ by k₂ 𝔰 ϱ/(1 − 𝔵); and the factor 2 in front of the maxima defining C_∞^(m),
C_(∞,ϱ)^(m), C_(∞,0)^(m), their weighted forms, C_P^v, C_(P,ϱ)^v and C_(P,0)^v by 1/(1 − 𝔵).

*Proof.* In each of these proofs the smallness is used through 𝔰 ≤ 𝔰_♭, |H| ≤ 1/8 and 𝔰 ≤ 1, which 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2
keeps, and through k₃ 𝔰 ≤ 1/2 in the absorptions, the constant there being k₃ of the chosen set or, at level four,
k₃^♮(μ) ≤ k₃^♮(ν); with 𝔰 ≤ 𝔰₁^v each of these products is at most 𝔵. In the bound of the second derivatives,
M ≤ k₁ 𝒥 + k₂ ϱ + 𝔵 (2𝒥 + M) gives M ≤ ((k₁ + 2𝔵) 𝒥 + k₂ ϱ)/(1 − 𝔵), and in the inductions of [[eq:tl5-hfs-m2]] and
[[eq:tl5-hfq-m2]] the same inequality for the parts with 𝒥_g and with ϱ closes with these coefficients; the bounds that
use them (of the products, of ‖M_g‖_Σ and of the first-order step) follow with the replaced coefficients. In the bounds
at a point, 𝔰_g ≤ m + 𝔵 𝔰_g, m the largest of the linear bounds, gives 𝔰_g ≤ m/(1 − 𝔵); in the argument with t of
[[lem:tl5-hfq-theta]], t ≤ 1 + 𝔵 t gives t ≤ 1/(1 − 𝔵). The rest of each proof holds as written. ∎

**Theorem {#thm:tl5-hfy}** (Existence with the absorption at the bootstrap's smallness.) The conclusions of
[[thm:tl5-hfx]] hold under its hypotheses with every constant formed with the replacements of [[lem:tl5-hfy-abs]], and
with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v in ε^w.

*Proof.* In Step 1 of the proof, let Σ_* be the set of σ with 𝔰 ≤ 𝔰₁^v on D^κ_σ. It contains 1/2, as 𝔰 ≤ η₀ < 𝔰₁^v on
N₀, and it is closed. For σ ∈ Σ_* and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so [[lem:tl5-hfy-abs]] applies at p and
gives 𝔰(p) ≤ 𝔰_* < 𝔰₁^v, 𝔰_* formed with the replaced constants; by the uniform continuity of 𝔰, Σ_* is open in
[1/2, s], so Σ_* = [1/2, s]. Steps 2 and 3 then use the bounds of [[lem:tl5-hfy-abs]] in place of those they replace; in
the terms with ϱ of Step 2, k₂ 𝔰 ϱ/(1 − 𝔵) ≤ 𝔰₁^v k₂ ϱ/(1 − 𝔵) gives ε^w with 𝔰₁^v/(1 − 𝔵) in place of 2𝔰₁^v. The
rest of the proof of [[thm:tl5-hfx]] holds as written. ∎

**Remark {#rem:tl5-hfy-what}** (What changes.) With 𝔵 small the recovery constant 2(k₁^μ + 1) becomes nearly k₁^μ, 2k₂
nearly k₂, and the maxima of the constants C_∞ and C_P lose their factor 2; at 𝔵 = 1/4 the replacements are
(4/3)(k₁^μ + 1/2), (4/3)k₂ and 4/3; for every 𝔵 each new factor is at least 2(1 − 𝔵) times smaller than the one it
replaces. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper
for no background at 10 l5. [[sec:tl5-hfz]] sharpens the recovery and counts it over the words ([[thm:tl5-hfz]]).

### The recovery sharpened and counted over the words {#sec:tl5-hfz}

In the recovery of second derivatives of [[lem:tl5-hf-recovery]] the coefficients (√3 + 8/3) K_rec, 4/3 and 𝔯₀ are
divided by 1 − (4/3)|H| ≥ 5/6, which gives the factor (6/5)(√3 + 8/3) of K_rec in every recovery constant, the factor
8/5 in k₂, in k₃ and in front of α_𝔄, and (6/5)𝔯₀. After Step 1 of the bootstrap |H| ≤ 𝔰 ≤ 𝔰₁^v; this section bounds the
second derivatives with that smallness and with the entry (1, 1) kept apart ([[lem:tl5-hfz-rec]]), which replaces these
factors by 𝔨_♯(𝔰₁^v) < 2.45, (1 − 𝔰₁^v)⁻¹ and (1 − 𝔰₁^v)⁻¹ 𝔯_♯. It then bounds the second derivatives of the words JB of
the first-order step in the Euclidean norm over the 43 words J ([[lem:tl5-hfz-words]]): the leading term of the recovery
counts once, the couplings 𝔄 count through the operator norm of their family over the words, and the count 43 remains
only with the nonlinear part and in the bounds of that norm. Finally the parts with 𝒥_g and with ϱ of the first-order
step are separated by the triangle inequality on the face, in place of (x + y)² ≤ 2x² + 2y² ([[lem:tl5-hfz-c1]]). The
closing condition is [[eq:tl5-hfz-closing]]; every new constant is at most the one it replaces, and the earlier closing
conditions remain valid. The notation is that of [[sec:tl5-hfy]].

**Lemma {#lem:tl5-hfz-rec}** (The recovery with the entry (1, 1) apart.) Let p, H, Ψ, 𝔣, K_rec, 𝔷_Z, ‖𝓡̂‖ and ‖𝒞_(·1)‖
be as in [[lem:tl5-hf-recovery]], except that |H| ≤ 𝔥 at p for a number 𝔥 ∈ [0, 1) in place of |H| ≤ 1/4, and put

    𝔨_♯(𝔥) := (1 + (2 + √2 𝔥)²/(1 − 𝔥)²)^(1/2),      𝔯_♯ := 2‖𝓡̂‖ + ‖𝒞_(·1)‖.

Then at p

    |D̂²Ψ| ≤ 𝔨_♯(𝔥) K_rec ((Σ_(Z∈Γ) |D̂ ℒ_ZΨ|²)^(1/2) + (Σ_(Z∈Γ) 𝔷_Z²)^(1/2))
             + (1 − 𝔥)⁻¹ (|𝔣| + 𝔯_♯ |Ψ|).                                                         {#eq:tl5-hfz-rec}

The function 𝔨_♯ is increasing, 𝔨_♯(0) = √5 and 𝔨_♯(1/4) < 3.3; for 𝔥 ≤ 1/4 each coefficient of [[eq:tl5-hfz-rec]] is at
most the corresponding one of [[eq:tl5-hf-recovery]] divided by 1 − (4/3)𝔥.

*Proof.* Let X be as in the proof of [[lem:tl5-hf-recovery]], X₀ the sum of its terms |D̂²Ψ(A, B)|² with A ≠ 1, and
X₁ := X − X₀, the sum of the |D̂²Ψ(1, B)|², B ≠ 1; that proof gives X^(1/2) ≤ K_rec ((Σ_Z |D̂ℒ_ZΨ|²)^(1/2) + (Σ_Z
𝔷_Z²)^(1/2)) without using H. Let R² := |D̂²Ψ|² − |D̂²Ψ(1, 1)|², the sum of X and of the |D̂²Ψ(A, 1)|², A ≠ 1. As
D̂²Ψ(A, 1) = D̂²Ψ(1, A) + 𝒞_(A1)Ψ, Minkowski's inequality gives (Σ_(A≠1) |D̂²Ψ(A, 1)|²)^(1/2) ≤ X₁^(1/2) + ‖𝒞_(·1)‖ |Ψ|,
and so R ≤ (X₀ + 2X₁)^(1/2) + ‖𝒞_(·1)‖ |Ψ|. In the identity for (1 + H^11) D̂²Ψ(1, 1) of that proof the squared norms of
the four diagonal terms D̂²Ψ(0, 0) and D̂²Ψ(j, j) are terms of X₀, so the sum of their norms is at most 2X₀^(1/2); by
the Cauchy–Schwarz inequality |Σ_((M,N)≠(1,1)) H^MN D̂²Ψ(M, N)| ≤ |H| R; and |H^11| ≤ |H| ≤ 𝔥. With R ≤ (2X)^(1/2) +
‖𝒞_(·1)‖ |Ψ| in the last term this gives

    (1 − 𝔥) |D̂²Ψ(1, 1)| ≤ 2X₀^(1/2) + √2 𝔥 X^(1/2) + |𝔣| + (2‖𝓡̂‖ + 𝔥 ‖𝒞_(·1)‖) |Ψ|.

Write X₀ = s² X with s ∈ [0, 1], so that X₀ + 2X₁ = (2 − s²) X. As |D̂²Ψ| = (R² + |D̂²Ψ(1, 1)|²)^(1/2), Minkowski's
inequality in the plane gives |D̂²Ψ| ≤ g(s)^(1/2) X^(1/2) + ‖𝒞_(·1)‖ |Ψ| + (1 − 𝔥)⁻¹ (|𝔣| + (2‖𝓡̂‖ + 𝔥 ‖𝒞_(·1)‖) |Ψ|),
with g(s) := 2 − s² + (2s + √2 𝔥)²/(1 − 𝔥)²; and ‖𝒞_(·1)‖ + 𝔥 ‖𝒞_(·1)‖/(1 − 𝔥) = ‖𝒞_(·1)‖/(1 − 𝔥). As 4/(1 − 𝔥)² > 1, g
is convex, so its largest value on [0, 1] is g(1) = 𝔨_♯(𝔥)² or g(0) = 2 + 2𝔥²/(1 − 𝔥)², and g(1) ≥ g(0) since
(2 + √2 𝔥)² − 2𝔥² − (1 − 𝔥)² = 3 + (4√2 + 2)𝔥 − 𝔥² > 0. With the bound of X this is [[eq:tl5-hfz-rec]]. For the last
claim, 𝔨_♯(𝔥) ≤ 𝔨_♯(1/4) < √3 + 8/3, (4/3)(1 − 𝔥) ≥ 1 − (4/3)𝔥, (8/3)(1 − 𝔥) ≥ 2(1 − (4/3)𝔥) and √2 (1 − 𝔥) ≥ 1 − (4/3)𝔥
for 𝔥 ≤ 1/4. ∎

**Definition {#def:tl5-hfz-constants}** (The constants with index z.) In the setting of [[lem:tl5-hfy-abs]], with k₃,
𝔰₁^v and 𝔵 as there, let 𝔨_♯ := 𝔨_♯(𝔰₁^v) and 𝔯_♯ be as in [[lem:tl5-hfz-rec]], q₁ as in [[lem:tl5-hf-linfty]], and
α_𝔄^(j,ν′) and k₁^(j,ν′) the numbers α_𝔄^(j,μ) and k₁^(j,μ) of [[def:tl5-hfs-bounds]] with ν′ in place of μ. For 0 ≤ j ≤
N − 1 and ν′ ∈ (0, 1] put

    k₁^(j,ν′,z) := 𝔨_♯ K_rec (1 + ν′^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|))
                   + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),
    k₁^z := k₁^(N−1,μ,z),   k₂^z := (1 − 𝔰₁^v)⁻¹ q₁,   k₃^z := (5/8)(1 − 𝔰₁^v)⁻¹ k₃,   𝔵^z := 𝔰₁^v sup_(D^κ) k₃^z,

and let 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z) be 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0 of [[lem:tl5-hfv-rec]] with 𝔨_♯ in place of
(6/5)(√3 + 8/3) and (1 − 𝔰₁^v)⁻¹ 𝔯_♯ in place of (6/5)𝔯₀. For a word B with |B| ≤ N − 3 let 𝔞_𝔄(B) be, at each point,
the operator norm of the map

    (ξ_K)_(|K|≤|B|+2) ↦ (Σ_K μ^((|B|+3−|K|)/2) 𝔄_(JB,K) ξ_K)_J,

J running over the 43 words of rotations with |J| ≤ 2 and 𝔄_(JB,K) := 0 for |K| > |JB|, from the families (ξ_K) of jets
at the point, with the Euclidean norm of the family formed with the norm (|D̂Ψ|² + |Ψ|²)^(1/2) on the jets, to the
families of tensors indexed by J, with their Euclidean norm. Let 𝔞_𝔄 be the largest of the 𝔞_𝔄(B), and put

    𝔩₀ := 𝔨_♯ K_rec (1 + μ^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + (1 − 𝔰₁^v)⁻¹ (μ^(1/2) 𝔯_♯ + 𝔞_𝔄),
    𝔩 := 𝔩₀ + 43^(1/2) 𝔵^z (k₁^z + 2)/(1 − 𝔵^z),
    C₁^z² := 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 2|∂_γ|² (𝔩 + (2ϖ′)^(1/2))²),
    C_(1,ϱ)^z² := 43 · 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 2|∂_γ|² (k₂^z)²/(1 − 𝔵^z)²)
                  · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),                                                  {#eq:tl5-hfz-c1}

with ϖ′ and 6C²𝔴⁶𝔳⁶ as in [[lem:tl5-hfx-c1]]; so C_(1,ϱ)^z is C_(1,ϱ) with 2(k₂^z)²/(1 − 𝔵^z)² in place of 32k₂². The
constants with index z are the constants of [[thm:tl5-hfy]] formed with k₁^(j,·,z), k₂^z, 𝔵^z, 𝔨_rec^z, 𝔨_rec^(ϱ,z),
𝔨_rec^(0,z), C₁^z and C_(1,ϱ)^z in place of k₁^(j,·), k₂, 𝔵, 𝔨_rec, 𝔨_rec^ϱ, 𝔨_rec^0, C₁^x and C_(1,ϱ); the thresholds
𝔰₀ and 𝔰₁^v keep k₃.

**Lemma {#lem:tl5-hfz-abs}** (The bounds with index z.) In the setting of [[lem:tl5-hfy-abs]], if 𝔰 ≤ 𝔰₁^v on Q(a, b),
then the lemmas named there hold with its replacements and with k₁^(j,·,z), k₂^z, 𝔵^z, 𝔨_rec^z, 𝔨_rec^(ϱ,z) and
𝔨_rec^(0,z) in place of k₁^(j,·), k₂, 𝔵, 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0. In particular the bounds [[eq:tl5-hfs-m2]],
[[eq:tl5-hfq-m2]] and those of M_g^(j), in the lemmas that state them, hold at every point of Q(a, b) with (k₁^(j,μ,z) +
2𝔵^z)/(1 − 𝔵^z) and k₂^z/(1 − 𝔵^z) in place of 2(k₁^(j,μ) + 1) and 2k₂. Moreover k₁^(j,ν′,z) ≤ k₁^(j,ν′), k₂^z ≤ k₂, 𝔵^z
≤ 2𝔵/3 ≤ 1/6, and 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z) are at most 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0 formed with the same
constants of first order.

*Proof.* In each of these lemmas the second derivatives are recovered only through [[eq:tl5-hf-recovery]], at points of
Q(a, b) (at p in [[lem:tl5-hfv-rec]]), for the tensor H of the solution, and divided by 1 − (4/3)|H| ≥ 5/6: this gives
the factor (6/5)(√3 + 8/3) of K_rec, the factor (6/5)𝔯₀ with its weight, and the factor 8/5 of |𝔣|, which stands in
front of the couplings 𝔄 in k₁^(j,·), of the residual in k₂ = (8/5)q₁ and of the nonlinear terms in every constant of
absorption. At these points |H| ≤ 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 ≤ 1/16, so [[lem:tl5-hfz-rec]] with 𝔥 := 𝔰₁^v gives the same bound
with 𝔨_♯, (1 − 𝔰₁^v)⁻¹ 𝔯_♯ and (1 − 𝔰₁^v)⁻¹ in place of these three factors. The constants named are formed from these
factors as before; so the linear parts of the bounds hold with k₁^(j,·,z), k₂^z and the 𝔨_rec^(·,z), and the nonlinear
parts with every constant of absorption multiplied by (5/8)(1 − 𝔰₁^v)⁻¹. With 𝔰 ≤ 𝔰₁^v each of these products with 𝔰 is
at most 𝔵^z on Q(a, b), at level four as k₃^♮(μ) ≤ k₃^♮(ν); so the proof of [[lem:tl5-hfy-abs]] holds with 𝔵^z in place
of 𝔵. Finally 𝔨_♯ ≤ 𝔨_♯(1/16) < 2.45 < (6/5)(√3 + 8/3), (1 − 𝔰₁^v)⁻¹ ≤ 16/15 < 8/5, 2(1 − 𝔰₁^v)⁻¹ ≤ (6/5)(8/3) and
(1 − 𝔰₁^v)⁻¹ ≤ (6/5)√2, which give the inequalities, with 𝔵^z = (5/8)(1 − 𝔰₁^v)⁻¹ 𝔵 ≤ (2/3)𝔵 and 𝔵 ≤ 1/4. ∎

**Lemma {#lem:tl5-hfz-words}** (The second derivatives counted over the words.) In the setting of [[lem:tl5-hfz-abs]],
with 𝔰 ≤ 𝔰₁^v on Q(a, b), let |B| ≤ N − 3.

(a) Let r_B and c_B be the largest of the sums of μ^((|B|+3−|K|)/2) ‖𝔄_(JB,K)‖ over K for fixed J and over J for fixed
K, at a point. Then 𝔞_𝔄(B) ≤ (r_B c_B)^(1/2) ≤ 43^(1/2) r_B ≤ (43/2)^(1/2) α_𝔄^(N−1,μ) there; so 𝔩₀ ≤ 43^(1/2) k₁^z and
𝔩 ≤ 43^(1/2) (k₁^z + 2𝔵^z)/(1 − 𝔵^z).

(b) By [[lem:tl5-hfz-abs]], the first-order step of the lemma in use bounds |D̂²Ψ_(JB)| at the points of Σ₁(a, b), for
every word J of rotations with |J| ≤ 2, by μ^(−(|B|+3)/2) 𝒥_g (k₁^z + 2𝔵^z)/(1 − 𝔵^z) + P_ϱ, where P_ϱ := w k₂^z
ϱ(p)/(1 − 𝔵^z) with w = 1 in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a), w = μ^(−(|B|+3)/2) in
[[lem:tl5-hft-small]] (b) and w = ν^(−(|B|+3)/2) in [[lem:tl5-hfq-theta]]. Then at those points, the sum being over the
43 words J,

    (Σ_J |D̂²Ψ_(JB)|²)^(1/2) ≤ μ^(−(|B|+3)/2) 𝔩 𝒥_g + 43^(1/2) P_ϱ.                                  {#eq:tl5-hfz-words}

*Proof.* (a) Write a_JK := μ^((|B|+3−|K|)/2) 𝔄_(JB,K). For a family (ξ_K), the Cauchy–Schwarz inequality gives |Σ_K a_JK
ξ_K|² ≤ (Σ_K ‖a_JK‖)(Σ_K ‖a_JK‖ |ξ_K|²) ≤ r_B Σ_K ‖a_JK‖ |ξ_K|², and summing over J gives Schur's bound (r_B c_B)^(1/2).
Each term of a sum over J is at most r_B, so c_B ≤ 43 r_B. As |B| + 3 ≥ |JB| + 1, the sum over K for fixed J is at most
Σ_K μ^((|JB|+1−|K|)/2) ‖𝔄_(JB,K)‖ ≤ 2^(−1/2) α_𝔄^(N−1,μ). Then 𝔩₀ = k₁^z + (1 − 𝔰₁^v)⁻¹ (𝔞_𝔄 − α_𝔄^(N−1,μ)) ≤ k₁^z +
(43^(1/2) − 1)(1 − 𝔰₁^v)⁻¹ α_𝔄^(N−1,μ) ≤ 43^(1/2) k₁^z, and 43^(1/2) (k₁^z + 2𝔵^z) − (1 − 𝔵^z) 𝔩 = (1 −
𝔵^z)(43^(1/2) k₁^z − 𝔩₀) ≥ 0.

(b) Let q be a point of Σ₁(a, b) and C := JB. As |H(q)| ≤ 𝔰(q) ≤ 𝔰₁^v, [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v applies to Ψ_C,
with 𝔣 = Σ_K 𝔄_CK(D̂Ψ_K, Ψ_K) + Σ_K 𝔔_CK ℒ^K(2R̂ic) − 𝔑′_C, where 𝔑′_C := Σ_(K≠C) 𝔔_CK ℒ^K N(h) + ℒ^C N(h) −
H^(αβ) D̂_αD̂_βΨ_C collects the nonlinear terms of the proof of [[lem:tl5-hf-linfty]]. Take the Euclidean norm over J
and apply Minkowski's inequality to each kind of term. The words
ZJB are distinct for distinct (Z, J) and have length at most |B| + 3 ≤ N, so (Σ_J Σ_Z |D̂Ψ_(ZJB)|²)^(1/2) ≤
μ^(−(|B|+3)/2) 𝒥_g. The words JB are distinct and have length at most |B| + 2, and (Σ_Z 𝔷_Z²)^(1/2) ≤ √7
(3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)(|D̂Ψ_C|² + |Ψ_C|²)^(1/2); so the terms with 𝔷_Z and with 𝔯_♯ |Ψ_C| contribute at most
μ^(1/2) μ^(−(|B|+3)/2) 𝒥_g times their coefficients. As Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², the definition of 𝔞_𝔄(B)
bounds the terms with 𝔄 by (1 − 𝔰₁^v)⁻¹ μ^(−(|B|+3)/2) 𝔞_𝔄(B) 𝒥_g. Together these contribute at most μ^(−(|B|+3)/2) 𝔩₀
𝒥_g. For each J, (1 − 𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) ≤ (1 − 𝔵^z) P_ϱ, as w ≥ 1; and, as in the proof of the
bound of |D̂²Ψ_C| that the step uses, (1 − 𝔰₁^v)⁻¹ |𝔑′_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐), 𝔐 that bound for the second
derivatives of the words of length at most |C|, whose weights are at most μ^(−(|B|+3)/2) and w as |C| + 1 ≤ |B| + 3; so
𝔐 ≤ μ^(−(|B|+3)/2) 𝒥_g (k₁^z + 2𝔵^z)/(1 − 𝔵^z) + P_ϱ. For each J these two terms are thus at most P_ϱ + μ^(−(|B|+3)/2)
𝒥_g 𝔵^z (k₁^z + 2)/(1 − 𝔵^z), which does not depend on J, so their Euclidean norm over the 43 words J is at most
43^(1/2) times it. Adding the parts gives [[eq:tl5-hfz-words]]. ∎

**Lemma {#lem:tl5-hfz-c1}** (The first-order constant with index z.) In the setting of [[lem:tl5-hfz-abs]], with 𝔰 ≤
𝔰₁^v on Q(a, b), the first-order step of the lemma in use, [[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] or
[[lem:tl5-hfq-theta]], gives its bound of D̂Ψ_B(p), |B| ≤ N − 3, with C₁^z and C_(1,ϱ)^z of [[eq:tl5-hfz-c1]] in place
of C₁^x and C_(1,ϱ), with the weights of that step and its part with η₀. Moreover C₁^z ≤ C₁^x and C_(1,ϱ)^z ≤ C_(1,ϱ),
these being formed as in [[thm:tl5-hfy]].

*Proof.* Let A := D̂Ψ_B. By Minkowski's inequality over the words and the bounds of R′_J and D̂R′_J in the proof of
[[lem:tl5-hfx-c1]], at the points of Σ₁(a, b), (Σ_J |ℒ^J A|²)^(1/2) ≤ μ^(−(|B|+3)/2) (1 + ϖ′^(1/2)) 𝒥_g and (Σ_J |D̂ℒ^J
A|²)^(1/2) ≤ (Σ_J |D̂²Ψ_(JB)|²)^(1/2) + μ^(−(|B|+3)/2) (2ϖ′)^(1/2) 𝒥_g; by [[eq:tl5-hfz-words]] the latter is at most
μ^(−(|B|+3)/2) (𝔩 + (2ϖ′)^(1/2)) 𝒥_g + 43^(1/2) P_ϱ. Let ∫ denote the integral over Σ₁(a, b) with dμ dτ₂/(1 − κκ′), and
put W := 2|∂_γ|² 𝔳⁶ R⁻³, F := ∫ 𝔳⁶ R⁻³ (1 + 18|D̂∂_γ|²) Σ_J |ℒ^J A|², P² := μ^(−(|B|+3)) ∫ W (𝔩 + (2ϖ′)^(1/2))² 𝒥_g² and
V² := 43 ∫ W P_ϱ². By Minkowski's inequality in L² of the face, ∫ W Σ_J |D̂ℒ^J A|² ≤ (P + V)²; so the right side of
[[eq:tl5-hf-cs-r]] with r = 3, or of its form in [[lem:tl5-hft-face]] (a), is at most 6C² 𝔴(p)⁶ (F + (P + V)² + S), S
its term on S_a, and

    (F + (P + V)² + S)^(1/2) ≤ (F + P²)^(1/2) + V + S^(1/2).

As in the proof of [[lem:tl5-hf-linfty]], |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) on the face, so ∫ f 𝒥_g² ≤
sup (f 𝔨₂) ℰ_g(p) for every function f ≥ 0, and 6C² 𝔴(p)⁶ (F + P²) ≤ μ^(−(|B|+3)) C₁^z² ℰ_g(p). Next 6C² 𝔴(p)⁶ V² ≤
w² C_(1,ϱ)^z² ϱ(p)², as P_ϱ = w k₂^z ϱ(p)/(1 − 𝔵^z) with w and ϱ(p) numbers; and S is bounded as in the proof of
[[lem:tl5-hfx-c1]]. This is the bound of the step with C₁^z and C_(1,ϱ)^z.

For the comparison let 𝔨 := (k₁^z + 2𝔵^z)/(1 − 𝔵^z) and Λ := Λ₂^μ, so that ϖ′ ≤ 1320 Λ² as in [[rem:tl5-hfx-what]], 𝔩 ≤
43^(1/2) 𝔨 by [[lem:tl5-hfz-words]] (a), and 𝔨 ≤ (k₁^μ + 2𝔵)/(1 − 𝔵) ≤ 2(k₁^μ + 1) by [[lem:tl5-hfz-abs]], as (k, x) ↦
(k + 2x)/(1 − x) is increasing in each argument and 𝔵 ≤ 1/4. At each point of the face 2(𝔩 + (2ϖ′)^(1/2))² ≤
4(43^(1/2) 𝔨 + (2ϖ′)^(1/2))², which compares C₁^z with the second entry of C₁^x. Also 2(𝔩 + (2ϖ′)^(1/2))² ≤ 4𝔩² + 8ϖ′ ≤
43 · 4 (72Λ² + 2𝔨²) and (1 + ϖ′^(1/2))² ≤ (1 + 37Λ)² ≤ 43 (1 + 6Λ)², which compare it with C₁^♮, whose term with k₁^μ is
4|∂_γ|² · 2(2(k₁^μ + 1))², or 4|∂_γ|² · 2((k₁^μ + 2𝔵)/(1 − 𝔵))² with the replacements of [[lem:tl5-hfy-abs]], both at
least 4|∂_γ|² · 2𝔨². Finally 2(k₂^z)²/(1 − 𝔵^z)² ≤ 8k₂²/(1 − 𝔵)². ∎

**Theorem {#thm:tl5-hfz}** (Existence with the recovery sharpened and counted over the words.) In the setting of
[[thm:tl5-hfy]] let S_F^z, S_M^z, ε_M^z and 𝔯^z be S_F^v, S_M^v, ε_M^v and 𝔯^v formed with the constants with index z of
[[def:tl5-hfz-constants]], and put

    ε^z := 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^v k₂^z ϱ],      η_z := 1 − max(ϑ₁, ϑ₂) − 𝔯^z,
    A_z := η_z^(−1/2) δ_w + η_z⁻¹ (ε^z + ε_M^z),      B_z := η_z⁻¹ (S_F^z + S_M^z),

and let 𝔰_*^z be 𝔰_*^w formed with the constants with index z and with A_z in place of A_w^v. Suppose: (a) η₀ < 𝔰₁^v;
(b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_z > 0, 𝔰_*^z < 𝔰₁^v and the
closing condition

    4 A_z B_z = 4 η_z^(−3/2) (δ_w + η_z^(−1/2) (ε^z + ε_M^z)) (S_F^z + S_M^z) < 1.                 {#eq:tl5-hfz-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_z and 𝔰_*^z in place of A_w (or
A_(w,4)) and 𝔰_*. Each constant with index z, and each of ε^z, A_z, B_z and 𝔰_*^z, is at most the one of [[thm:tl5-hfy]]
it replaces, and η_z is at least η; so the hypotheses of [[thm:tl5-hfy]] imply these.

*Proof.* The proof of [[thm:tl5-hfy]] applies with [[lem:tl5-hfz-abs]] and [[lem:tl5-hfz-c1]] in place of
[[lem:tl5-hfy-abs]] and [[lem:tl5-hfx-c1]]. In Step 1, Σ_* is the set of σ with 𝔰 ≤ 𝔰₁^v on D^κ_σ, as there; for σ ∈ Σ_*
and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so the two lemmas apply at p and give 𝔰(p) ≤ 𝔰_*^z < 𝔰₁^v, and Σ_* = [1/2, s] as
there. Steps 2 and 3 use their bounds in place of those they replace; in the terms with ϱ of Step 2, k₂^z 𝔰 ϱ/(1 − 𝔵^z)
≤ 𝔰₁^v k₂^z ϱ/(1 − 𝔵^z) gives ε^z. The rest is the proof of [[thm:tl5-hfv]] with A_z, B_z and [[eq:tl5-hfz-closing]].
For the last claim, k₁^(j,·,z), k₂^z, 𝔵^z, the 𝔨_rec^(·,z), C₁^z and C_(1,ϱ)^z are at most the numbers they replace, by
[[lem:tl5-hfz-abs]] and [[lem:tl5-hfz-c1]]; every constant of [[thm:tl5-hfy]], ε^w and 𝔯^v are nondecreasing in these
numbers, so η_z ≥ η, and A_w^v, B_v and 𝔰_*^w are nonincreasing in η and nondecreasing in the constants. ∎

**Remark {#rem:tl5-hfz-what}** (What changes.) The recovery constant loses the factor 6/5 of 1 − (4/3)|H| ≥ 5/6, and its
coefficient √3 + 8/3 of K_rec becomes 𝔨_♯, which lies between √5 and 𝔨_♯(1/16) < 2.45; so the factor (6/5)(√3 +
8/3) > 5.27 becomes about √5 < 2.24 when 𝔰₁^v is small, in k₁^(j,·), in 𝔨_rec, and through the bounds of the second
derivatives in 𝔨_A, λ_t^μ, λ_t^(μ,2) and C₁^z. The factor 8/5 in front of the residual and of the nonlinear terms
becomes (1 − 𝔰₁^v)⁻¹ ≤ 16/15, which lowers k₂ and k₃, and with k₃ the number 𝔵, by the factor (5/8)(1 − 𝔰₁^v)⁻¹ ≤ 2/3.
In the part of C₁^z with 𝒥_g the count 43 of the words remains in the nonlinear part 43^(1/2) 𝔵^z (k₁^z + 2)/(1 − 𝔵^z)
and in the bounds of 𝔞_𝔄 below, against 43^(1/2) (k₁^μ + 2𝔵)/(1 − 𝔵) in [[eq:tl5-hfx-c1]] with the replacements of
[[lem:tl5-hfy-abs]]: the nonlinear terms are bounded through the largest second derivative and are not absorbed over
the words, so no condition on 43^(1/2) 𝔵^z is needed. The couplings 𝔄 enter through the norm 𝔞_𝔄 of their family over
the words, which any bound of it may replace, Schur's (r_B c_B)^(1/2) among them, and which is at most (43/2)^(1/2)
α_𝔄^(N−1,μ). The triangle
inequality on the face halves the term with |∂_γ|² of the square of C₁^z against the split (x + y)² ≤ 2x² + 2y² of
[[eq:tl5-hfx-c1]], and quarters the square of C_(1,ϱ)^z against the two splits of C_(1,ϱ); it is at least as good as
(x + y)² ≤ (1 + δ)x² + (1 + 1/δ)y² for every δ > 0, which would move a factor between the two parts, so no such number
is needed. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfz]] are established in this paper
for no background at 10 l5. [[sec:tl5-hfp]] sharpens the Sobolev constants and the bound of D̂²h ([[thm:tl5-hfp]]).

### The leaf constant, the weights of the words and the seven fields {#sec:tl5-hfp}

This section sharpens the constants of [[sec:tl5-hfz]] in five ways, with the intrinsic Sobolev constants of
[[lem:tl5-hft-face]]. First, the sum over the 43 words in [[eq:tl5-hft-leaf]] is diagonal on the representations of
SO(4), so that inequality holds with its own constant C_(E,r)^♯ ≤ (2/9)^(1/2) (6C_(E,r)²)^(1/2), and also with weights
𝔶₀, 𝔶₁ on the words of lengths zero and one ([[lem:tl5-hfp-leaf]]). Second, in the bounds of Ψ_B(p) and of D̂Ψ_B(p) the
words J of length k ≤ 2 carry weights 𝔶_k ≤ μ^(k−2), which their energies allow, in place of the weight of the longest
words. Third, the first-order bound is proved for a family of words B of one length at once, which counts the seven
fields of the bound of D̂²h at level four together, and at the levels N ≥ 6 the words of each length in the second
derivatives at low levels ([[lem:tl5-hfp-words]], [[lem:tl5-hfp-c1]], [[lem:tl5-hfp-rec]], [[lem:tl5-hfp-low]]). Fourth,
the leading term of the recovery is bounded through the energy of the first derivatives alone, whose density carries 𝔨₂
without its part 1/(2Ω̂²z̲). Fifth, the fields enter the terms 𝔷_Z through (Σ_Z |D̂Z|²)^(1/2) and (Σ_Z |D̂²Z|²)^(1/2).
The closing condition is [[eq:tl5-hfp-closing]]; with 𝔶₀ = 𝔶₁ = 1 every new constant is at most the one it replaces, and
the earlier closing conditions remain valid. The notation is that of [[sec:tl5-hfz]].

**Lemma {#lem:tl5-hfp-leaf}** (The Sobolev inequality on the leaves, with its own constant and with weights.) In the
setting of [[lem:tl5-hft-leaf]] let 𝔶₀, 𝔶₁ > 0, put 𝔶₂ := 1, c_(j₁j₂) := 2j₁(j₁ + 1) + 2j₂(j₂ + 1) and

    C_(E,r)(𝔶)² := (1/(2π²)) Σ_(j₁,j₂) (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r) / (𝔶₀ + 𝔶₁ c_(j₁j₂) + c_(j₁j₂)²).

Then for every C² covariant tensor field A of rank r on S_(u,v) and every ω ∈ S³, with the sum over the words J of
length at most two in the six rotations,

    |A(ω)|₀² ≤ C_(E,r)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀² dω.                                     {#eq:tl5-hfp-leaf}

C_(E,r)(𝔶) is nonincreasing in 𝔶₀ and in 𝔶₁, and C_(E,r)^♯ := C_(E,r)(1, 1) satisfies C_(E,r)^♯² ≤ (4/3) C_(E,r)² =
(2/9) · 6C_(E,r)². For r = 0, [[eq:tl5-hf-sphere]] holds with C_(E,0)^♯² in place of 6C_(S³)² = 1/2.

*Proof.* In the proof of [[lem:tl5-hft-leaf]], the orthogonal projection of L²(S³, E) onto V_π commutes with the action
of SO(4), hence with each ℒ_(K_ab), and Ω = c_π on V_π. As ℒ_(K_ab) is skew-adjoint, Σ_(a<b) ‖ℒ_(K_ab) B‖² = ⟨ΩB, B⟩ for
B ∈ V_π; with B = A_π and with B = ℒ_(K_cd) A_π ∈ V_π this gives Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A_π‖² = (𝔶₀ + 𝔶₁ c_π + c_π²)
‖A_π‖², the 36 words of length two being the ordered pairs of rotations. Summed over π, as the V_π are orthogonal, the
left side is Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖². With |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖² as there, the Cauchy–Schwarz
inequality over π gives

    |A(ω)|₀ ≤ Σ_π |A_π(ω)|₀ ≤ C_(E,r)(𝔶) (Σ_π (𝔶₀ + 𝔶₁ c_π + c_π²) ‖A_π‖²)^(1/2),

which is [[eq:tl5-hfp-leaf]]. The series converges, as 𝔶₀ + 𝔶₁ c + c² ≥ min(𝔶₀, 𝔶₁, 1)(1 + c)²/2 bounds its terms by
2/min(𝔶₀, 𝔶₁, 1) times those of C_(E,r)²; and its terms do not increase with 𝔶₀ and 𝔶₁. Since (4/3)(1 + c + c²) − (1 +
c)² = (1 − c)²/3 ≥ 0, C_(E,r)^♯² ≤ (4/3) C_(E,r)². For r = 0, E is the trivial bundle, |·|₀ is the absolute value and
ℒ_K f = K f, so with 𝔶₀ = 𝔶₁ = 1 the right side of [[eq:tl5-hfp-leaf]] is C_(E,0)^♯² times the integral of
[[eq:tl5-hf-sphere]]. ∎

**Definition {#def:tl5-hfp-constants}** (The constants with index p.) In the setting of [[def:tl5-hfz-constants]], with
the intrinsic Sobolev constants, fix 𝔶₀ ∈ (0, μ⁻²] and 𝔶₁ ∈ (0, μ⁻¹], put 𝔶₂ := 1, let C_(E,r)(𝔶) and C_(E,r)^♯ be as in
[[lem:tl5-hfp-leaf]], and put, for 0 ≤ j ≤ N − 1 and ν′ ∈ (0, 1],

    𝔷₁′ := 3 (Σ_(Z∈Γ) |D̂Z|²)^(1/2),   𝔷₂′ := 2 (Σ_(Z∈Γ) |D̂²Z|²)^(1/2),   𝔷′ := (𝔷₁′² + 𝔷₂′²)^(1/2),
    k₁^(j,ν′,p) := 𝔨_♯ K_rec (1 + ν′^(1/2) 𝔷′) + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),   k₁^p := k₁^(N−1,μ,p),
    k₁^D := 𝔨_♯ K_rec,   𝔨₂′ := max(1/c, 1/κ′)/(2Ω̂²),   𝒟_g := (Σ_(|C|≤N) μ^|C| |D̂Ψ_C|²)^(1/2).

For a family 𝔚 of n distinct words of one length b ≤ N − 3 let 𝔞_𝔄(𝔚) be, at each point, the operator norm of the map

    (ξ_K)_(|K|≤b+2) ↦ (Σ_K (𝔶_(|J|) μ^(b+3−|K|))^(1/2) 𝔄_(JB,K) ξ_K)_((J,B)),

the pairs (J, B) running over the words J of rotations with |J| ≤ 2 and the B ∈ 𝔚, 𝔄_(JB,K) := 0 for |K| > |JB|, normed
as in [[def:tl5-hfz-constants]], and put

    𝔩_D(𝔚) := k₁^D (1 + (43n)^(1/2) 𝔵^z/(1 − 𝔵^z)),
    𝔩_J(𝔚) := μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔚) + (43n)^(1/2) 𝔵^z (k₁^p − k₁^D + 2)/(1 − 𝔵^z),
    C₁^U(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(μ^(1/2) + ϖ′^(1/2))²
                + 2|∂_γ|² (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^D(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂′ (μ (1 + 18|D̂∂_γ|²) + 2|∂_γ|² 𝔩_D(𝔚)²),
    C₁^J(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²) ϖ′ + 2|∂_γ|² (𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁(𝔚) := min(C₁^U(𝔚), C₁^D(𝔚) + C₁^J(𝔚)),                                                           {#eq:tl5-hfp-c1}

with ϖ′ as in [[lem:tl5-hfx-c1]]. Let C₁^p be the largest of the C₁({B}), |B| ≤ N − 3, and for N = 4 put C₁^Γ := C₁(Γ),
the seven fields being words of length one. Put 𝔗(𝔶)² := (𝔶₀ + 6𝔶₁ + 36)/43 for the steps of [[lem:tl5-hfs-linfty]] and
[[lem:tl5-hft-small]] (a), 𝔗(𝔶)² := (μ²𝔶₀ + 6μ𝔶₁ + 36)/43 for those of [[lem:tl5-hft-small]] (b) and 𝔗(𝔶)² := (ν²𝔶₀ +
6ν𝔶₁ + 36)/43 for those of [[lem:tl5-hfq-theta]]. Let C_S^p be C_S^E of [[eq:tl5-hft-cs]] with C_(E,2)(𝔶)² in place of
6C_(E,2)², and C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p the constants C_(1,ϱ)^z, C_(1,0) and C_(0,0) of the lemma in use
formed with C_(E,r)(𝔶)² 𝔗(𝔶)² in place of 6C_(E,r)² (r = 3, 3 and 2). For 0 ≤ m ≤ N − 4 put 𝔐_p^(m) := (Σ_(b≤m+1)
(C_S^p² + C₁(𝔚_b)²))^(1/2), 𝔚_b being the family of the 7^b words of length b, and for N = 4 put

    𝔨_rec^p := 𝔨_♯ K_rec (C₁^Γ + 𝔷₁′ μ^(1/2) C₁^p + 𝔷₂′ μ C_S^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^p,
    𝔨_rec^(ϱ,p) := 𝔨_♯ K_rec (√7 + 𝔷₁′ μ^(1/2)) C_(1,ϱ)^p,
    𝔨_rec^(0,p) := 𝔨_♯ K_rec ((√7 + 𝔷₁′ μ^(1/2)) C_(1,0)^p + 𝔷₂′ μ C_(0,0)^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_(0,0)^p.

The constants with index p are the constants with index z of [[thm:tl5-hfz]] formed with k₁^(j,·,p), C₁^p, C_S^p,
C_(1,ϱ)^p, C_(1,0)^p, C_(0,0)^p and the 𝔨_rec^(·,p) in place of k₁^(j,·,z), C₁^z, C_S^E, C_(1,ϱ)^z, C_(1,0), C_(0,0) and
the 𝔨_rec^(·,z), with 𝔐_p^(m) in place of (2𝔐^(m))^(1/2) max(C_S, C₁) in C_(∞,μ)^(m) and its forms, and with C_(E,r)^♯²
in place of 6C_(E,r)² in every other constant formed with a Sobolev inequality on a face.

**Lemma {#lem:tl5-hfp-abs}** (The bounds with index p.) (a) [[lem:tl5-hft-face]] holds with C_(E,r)^♯² in place of
6C_(E,r)², and its parts (a) and (b) hold also with every sum over the words J weighted by 𝔶_(|J|) and with C_(E,r)(𝔶)²
in place of 6C_(E,r)², for all 𝔶₀, 𝔶₁ > 0.

(b) In the setting of [[lem:tl5-hfz-abs]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), the lemmas named there hold with k₁^(j,·,p) in
place of k₁^(j,·,z); and the bounds [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] and those of M_g^(j), in the lemmas that state
them, hold with k₁^D 𝒟_g + (k₁^(j,μ,p) − k₁^D + 2𝔵^z) 𝒥_g in place of (k₁^(j,μ,z) + 2𝔵^z) 𝒥_g.

(c) In that setting, the zeroth-order step of the lemma in use gives its bound of Ψ_B(p), |B| ≤ N − 2, with C_S^p and
C_(0,0)^p in place of C_S^E and C_(0,0); and for a family 𝔚 of n distinct words of one length b ≤ N − 2 it gives the
same bound of (Σ_(B∈𝔚) |Ψ_B(p)|²)^(1/2), with n^(1/2) times its part with η₀.

Moreover k₁^(j,ν′,p) ≤ k₁^(j,ν′,z), and for 𝔶₀ = 𝔶₁ = 1, 𝔗(𝔶) ≤ 1, C_S^p ≤ C_S^E and C_(0,0)^p ≤ C_(0,0).

*Proof.* (a) The proof of [[lem:tl5-hft-face]] uses [[eq:tl5-hft-leaf]] only through its form, applied on the leaves
through γ_ω(v) to A and to ℒ_(∂_γ)A; [[lem:tl5-hfp-leaf]] gives that form with C_(E,r)^♯² in place of 6C_(E,r)², and
with the weights 𝔶_(|J|) and C_(E,r)(𝔶)². The weights pass through the proofs of (a) and (b) there, since (d/dv)|ℒ^J
A|₀² ≤ |ℒ^J A|₀² + |ℒ_(∂_γ) ℒ^J A|₀² holds for each J and is multiplied by 𝔶_(|J|) > 0 before the sum over J, and every
later step bounds the terms of each J separately.

(b) By Minkowski's inequality over Z and the Cauchy–Schwarz inequality, (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷₁′ |D̂Ψ| + 𝔷₂′ |Ψ| ≤ 𝔷′
(|D̂Ψ|² + |Ψ|²)^(1/2), and 𝔷′ ≤ 𝔷₁′ + 𝔷₂′ ≤ √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|); in the proofs of these lemmas the jets
of the terms 𝔷_Z are bounded through (|D̂Ψ_C|² + |Ψ_C|²)^(1/2), so k₁^(j,·,p) may replace k₁^(j,·,z). In the bound of
the second derivatives the leading term of [[eq:tl5-hfz-rec]] for Ψ_C is 𝔨_♯ K_rec (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤ k₁^D
μ^(−(|C|+1)/2) 𝒟_g, the words ZC having length |C| + 1. As 𝒟_g ≤ 𝒥_g, the inductions of the proofs of
[[lem:tl5-hfy-abs]] and [[lem:tl5-hfz-abs]] then close with the stated coefficients: with X_𝒟 ≤ X the weighted 𝒟_g and
𝒥_g of a word and ϱ′ its part with ϱ, R := (k₁^D X_𝒟 + (k₁ − k₁^D + 2𝔵^z) X + k₂^z ϱ′)/(1 − 𝔵^z) satisfies k₁^D X_𝒟 +
(k₁ − k₁^D) X + k₂^z ϱ′ + 𝔵^z (2X + R) = R.

(c) The step applies [[lem:tl5-hf-sobolev]], in the form of [[lem:tl5-hft-face]] (b), to A := Ψ_B; by (a) it holds with
the weights 𝔶_(|J|) and C_(E,2)(𝔶)². As ℒ^J Ψ_B = Ψ_(JB), the words JB are distinct and 𝔶_(|J|) μ^(|B|+2) ≤ μ^(|JB|),
the face term is at most μ^(−(|B|+2)) C_S^p² ℰ_g(p). On S_a, |Ψ_(JB)| ≤ η₀(p) for every J, and for |J| = k this bound,
divided by the weight of the step, is at most 𝔢_k times the one the step uses for every J, with 𝔢_k := 1 in
[[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a); 𝔢_k := μ^((2−k)/2) in [[lem:tl5-hft-small]] (b), where the step
multiplies by μ^((|B|+2)/2) and uses μ^((|B|+2)/2) η₀(p) ≤ η₀(p), while η₀(p) ≤ μ^((2−k)/2) μ^(−(|B|+2)/2) η₀(p); and
𝔢_k := ν^((2−k)/2) in [[lem:tl5-hfq-theta]], where the step uses r_Φ η₀(p) with r_Φ = ν^(−(|B|+2)/2), while η₀(p) ≤
ν^((2−k)/2) r_Φ η₀(p). As 𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36 = 43 𝔗(𝔶)², the sum over J of the squares, with the weights 𝔶_(|J|), is at
most 43 𝔗(𝔶)² times the square of that bound, which gives C_(0,0)^p. For a family, sum the inequality over B ∈ 𝔚: the
words JB are distinct for distinct pairs (J, B), as the B have one length, so the face terms still add up to at most
μ^(−(b+2)) C_S^p² ℰ_g(p), and the terms on S_a to n times those of one word.

Finally (b) gives k₁^(j,ν′,p) ≤ k₁^(j,ν′,z); for 𝔶₀ = 𝔶₁ = 1, 𝔗(𝔶)² ≤ 1 as μ, ν ≤ 1, C_(E,2)(𝔶) = C_(E,2)^♯ and
C_(E,2)^♯² ≤ 6C_(E,2)² by [[lem:tl5-hfp-leaf]]. ∎

**Lemma {#lem:tl5-hfp-words}** (The second derivatives over a family of words, with weights.) In the setting of
[[lem:tl5-hfz-abs]] and [[def:tl5-hfp-constants]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), let 𝔚 be a family of n distinct words of
one length b ≤ N − 3, and let P_ϱ be as in [[lem:tl5-hfz-words]] (b). Then at the points of Σ₁(a, b), the sum being over
the words J of rotations with |J| ≤ 2 and the B ∈ 𝔚,

    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂²Ψ_(JB)|²)^(1/2)
        ≤ 𝔩_D(𝔚) 𝒟_g + 𝔩_J(𝔚) 𝒥_g + (43n)^(1/2) 𝔗(𝔶) μ^((b+3)/2) P_ϱ.                                {#eq:tl5-hfp-words}

Moreover 𝔞_𝔄(𝔚) ≤ (43n/2)^(1/2) α_𝔄^(N−1,μ) and 𝔞_𝔄(𝔚) ≤ (Σ_(B∈𝔚) 𝔞_𝔄({B})²)^(1/2).

*Proof.* By [[lem:tl5-hfp-abs]] (b) and the proof of [[lem:tl5-hfz-words]] (b), the step bounds |D̂²Ψ_C| at the points
of the face, for every word C with |C| = b + k ≤ b + 2, by μ^(−(|C|+1)/2) (k₁^D 𝒟_g + (k₁^p − k₁^D + 2𝔵^z) 𝒥_g)/(1 −
𝔵^z) + P_C, with P_C := 𝔢_k P_ϱ ≥ k₂^z ϱ(p)/(1 − 𝔵^z), where 𝔢_k is as in the proof of [[lem:tl5-hfp-abs]] (c): the
bound of the part with ϱ is uniform in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a), and carries
μ^(−(|C|+1)/2) = μ^((2−k)/2) μ^(−(b+3)/2) in [[lem:tl5-hft-small]] (b) and ν^(−(|C|+1)/2) in [[lem:tl5-hfq-theta]]. So
𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36 = 43 𝔗(𝔶)², the numbers of the words J of lengths 0, 1 and 2 being 1, 6 and 36. Let q be a point of
Σ₁(a, b), (J, B) a pair and C := JB, and put 𝔬_J := (𝔶_(|J|) μ^(b+3))^(1/2), so that 𝔬_J ≤ μ^((|C|+1)/2), as 𝔶_k ≤
μ^(k−2). Apply [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v to Ψ_C at q, as there, with (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷′
(|D̂Ψ_C|² + |Ψ_C|²)^(1/2); multiply by 𝔬_J, take the Euclidean norm over the 43n pairs and apply Minkowski's inequality
to each kind of term. The words ZJB are distinct for distinct (Z, J, B), as the B have one length, and 𝔬_J² ≤ μ^(|ZJB|);
so the leading term contributes at most k₁^D 𝒟_g. The words JB are distinct and 𝔬_J² ≤ μ μ^(|JB|), so the terms with 𝔷_Z
and with 𝔯_♯ |Ψ_C| contribute at most μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) 𝒥_g, and the terms with 𝔄 at most (1 −
𝔰₁^v)⁻¹ 𝔞_𝔄(𝔚) 𝒥_g, by the definition of 𝔞_𝔄(𝔚) and Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g². For each pair, (1 −
𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) ≤ (1 − 𝔵^z) P_C, and, as in the proof of the bound of |D̂²Ψ_C|, (1 −
𝔰₁^v)⁻¹ |𝔑′_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐), where 𝔐 is the bound above for the words of length |C|, which bounds the
second derivatives of the words of length at most |C|. So 𝔬_J times these two terms is at most 𝔵^z (k₁^D 𝒟_g + (k₁^p −
k₁^D + 2) 𝒥_g)/(1 − 𝔵^z) + 𝔬_J P_C. The Euclidean norm over the pairs of the first part is (43n)^(1/2) times it, and
that of the second is (n (𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36) μ^(b+3))^(1/2) P_ϱ. Adding the parts gives [[eq:tl5-hfp-words]]. The row
of (J, B) of the map defining 𝔞_𝔄(𝔚) has the sum Σ_K (𝔶_(|J|) μ^(b+3−|K|))^(1/2) ‖𝔄_(JB,K)‖ ≤ Σ_K μ^((|JB|+1−|K|)/2)
‖𝔄_(JB,K)‖ ≤ 2^(−1/2) α_𝔄^(N−1,μ), and the argument of [[lem:tl5-hfz-words]] (a) with 43n rows gives the first bound;
the map is the family over B ∈ 𝔚 of the maps for {B}, which gives the second. ∎

**Lemma {#lem:tl5-hfp-c1}** (The first-order bound over a family of words.) In the setting of [[lem:tl5-hfp-words]], at
p

    (Σ_(B∈𝔚) |D̂Ψ_B(p)|²)^(1/2)
        ≤ μ^(−(b+3)/2) C₁(𝔚) ℰ_g(p)^(1/2) + n^(1/2) (w C_(1,ϱ)^p ϱ(p) + E₀),                        {#eq:tl5-hfp-family}

w being the weight of P_ϱ in [[lem:tl5-hfz-words]] (b) and E₀ the part with η₀ of the bound of |D̂Ψ_B(p)| that the
first-order step of the lemma in use gives, divided by its weight where the step bounds a weighted quantity, formed with
C_(E,3)(𝔶)² 𝔗(𝔶)² in place of 6C_(E,3)². In particular that step gives its bound of D̂Ψ_B(p), |B| ≤ N − 3, with C₁^p,
C_(1,ϱ)^p and C_(1,0)^p in place of C₁^z, C_(1,ϱ)^z and C_(1,0). Moreover C₁(𝔚) ≤ C₁^U(𝔚) ≤ n^(1/2) max_(B∈𝔚) C₁^U({B}),
and for 𝔶₀ = 𝔶₁ = 1, C₁^U({B}) ≤ C₁^z.

*Proof.* For B ∈ 𝔚 let A_B := D̂Ψ_B. By [[lem:tl5-hfp-abs]] (a), [[eq:tl5-hf-cs-r]] with r = 3, in its intrinsic form,
holds with the weights 𝔶_(|J|) and C_(E,3)(𝔶)². Sum it over B ∈ 𝔚 and multiply by μ^(b+3). Let ∫ denote the integral
over Σ₁(a, b) with dμ dτ₂/(1 − κκ′), f := 𝔳₀⁶ R⁻³ (1 + 18|D̂∂_γ|²) and W := 2|∂_γ|² 𝔳₀⁶ R⁻³. At the points of the face
ℒ^J A_B = D̂Ψ_(JB) + R′_(J,B), as in the proof of [[lem:tl5-hfx-c1]]. The words JB are distinct and 𝔶_(|J|) μ^(b+3) ≤ μ
μ^(|JB|), so (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂Ψ_(JB)|²)^(1/2) ≤ μ^(1/2) 𝒟_g. Each monomial of R′_(J,B) is a coefficient
carrying a ≥ 1 letters of J, of norm at most Λ_a, contracted with Ψ_(σB), σ the subword of J left; B ↦ σB is injective,
and 𝔶_(|J|) μ^(b+3) ≤ μ^(1+a) μ^(|σB|) for |J| ≥ 1; so Minkowski's inequality over the monomials and over the words
gives (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |R′_(J,B)|²)^(1/2) ≤ ϖ′^(1/2) 𝒥_g, as in the proof of [[lem:tl5-hfq-mixed]], and likewise
(2ϖ′)^(1/2) 𝒥_g for the D̂R′_(J,B). With [[eq:tl5-hfp-words]], at each point of the face

    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |ℒ^J A_B|²)^(1/2) ≤ μ^(1/2) 𝒟_g + ϖ′^(1/2) 𝒥_g,
    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂ℒ^J A_B|²)^(1/2) ≤ 𝔩_D(𝔚) 𝒟_g + (𝔩_J(𝔚) + (2ϖ′)^(1/2)) 𝒥_g + y,

with y := (43n)^(1/2) 𝔗(𝔶) μ^((b+3)/2) P_ϱ. Put F_D² := ∫ f μ 𝒟_g², F_J² := ∫ f ϖ′ 𝒥_g², P_D² := ∫ W 𝔩_D(𝔚)² 𝒟_g², P_J²
:= ∫ W (𝔩_J(𝔚) + (2ϖ′)^(1/2))² 𝒥_g², V² := ∫ W y² and S the sum over B of the terms on S_a, times μ^(b+3). By
Minkowski's inequality in L² of the face and then in ℝ³, the square root of the right side is at most

    C_(E,3)(𝔶) 𝔴₀(p)³ ((F_D² + P_D²)^(1/2) + (F_J² + P_J²)^(1/2) + V + S^(1/2)),

and, as 𝒟_g ≤ 𝒥_g, also at most C_(E,3)(𝔶) 𝔴₀(p)³ ((F² + P²)^(1/2) + V + S^(1/2)), where F² := ∫ f (μ^(1/2) + ϖ′^(1/2))²
𝒥_g² and P² := ∫ W (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))² 𝒥_g². By [[eq:tl5-hf-coercive]], on the face |D̂Ψ_C|² ≤ 𝔨₂′
(e_o[Ψ_C] + κ′ e_i[Ψ_C]), and |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) as in the proof of [[lem:tl5-hf-linfty]];
so ∫ g 𝒟_g² ≤ sup (g 𝔨₂′) ℰ_g(p) and ∫ g 𝒥_g² ≤ sup (g 𝔨₂) ℰ_g(p) for every function g ≥ 0, and C_(E,3)(𝔶)² 𝔴₀(p)⁶ times
F_D² + P_D², F_J² + P_J² and F² + P² is at most C₁^D(𝔚)², C₁^J(𝔚)² and C₁^U(𝔚)² times ℰ_g(p). As P_ϱ = w k₂^z ϱ(p)/(1 −
𝔵^z), C_(E,3)(𝔶)² 𝔴₀(p)⁶ V² ≤ n μ^(b+3) w² C_(1,ϱ)^p² ϱ(p)². On S_a, for |J| = k, the bound of ℒ^J A_B that the step
uses for every J, divided by its weight, may be replaced by 𝔢_k times it, 𝔢_k as in the proof of [[lem:tl5-hfp-abs]]
(c): in [[lem:tl5-hft-small]] (b) the weight is μ^((b+3)/2) = μ^((2−k)/2) μ^((|JB|+1)/2), and μ^((|JB|+1)/2) |D̂Ψ_(JB)|
≤ η₀(p) and μ^((|JB|+1)/2) Λ_a ≤ μ^((1+a)/2) Λ_a for the coefficients of R′_(J,B), as |JB| ≥ a; in [[lem:tl5-hfq-theta]]
likewise with ν and the factor ν^(−(b+3)/2) of the step. So the terms on S_a, with the weights 𝔶_(|J|), give n^(1/2)
μ^((b+3)/2) E₀, and dividing by μ^((b+3)/2) gives [[eq:tl5-hfp-family]]. For n = 1 the bound of the step follows, with
C₁({B}) ≤ C₁^p.

For the last claims, (43n)^(1/2) = n^(1/2) 43^(1/2) gives 𝔩_D(𝔚) ≤ n^(1/2) 𝔩_D({B}), and [[lem:tl5-hfp-words]] gives
𝔞_𝔄(𝔚) ≤ n^(1/2) max_B 𝔞_𝔄({B}), so 𝔩_J(𝔚) ≤ n^(1/2) max_B 𝔩_J({B}); as 𝔩_D({B}) does not depend on B, the integrand of
C₁^U(𝔚)² is at most n times the largest of those of the C₁^U({B})², and the supremum over the face of that largest one
is the largest of the suprema. For 𝔶₀ = 𝔶₁ = 1, C_(E,3)(𝔶) = C_(E,3)^♯ and C_(E,3)^♯² ≤ 6C_(E,3)², μ^(1/2) ≤ 1, and
𝔩_D({B}) + 𝔩_J({B}) is 𝔩 of [[eq:tl5-hfz-c1]] with 𝔷′, k₁^p and 𝔞_𝔄({B}) ≤ 𝔞_𝔄 in place of √7 (3 max_Z |D̂Z| + 2
max_Z |D̂²Z|), k₁^z and 𝔞_𝔄, each at most the one it replaces by [[lem:tl5-hfp-abs]] (b); so C₁^U({B}) ≤ C₁^z. ∎

**Lemma {#lem:tl5-hfp-rec}** (The recovery of D̂²h with the seven fields together.) Let N = 4 and, in the setting of
[[lem:tl5-hfz-abs]], 𝔰 ≤ 𝔰₁^v on Q(a, b). Then [[lem:tl5-hfv-rec]], with the constants with index z, holds with 𝔨_rec^p,
𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p) in place of 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z), and with C_S^p, C₁^p, C_(1,ϱ)^p, C_(1,0)^p
and C_(0,0)^p in place of C_S^E, C₁^z, C_(1,ϱ)^z, C_(1,0) and C_(0,0) in C_P^v, C_(P,ϱ)^v and C_(P,0)^v.

*Proof.* In the proof of [[lem:tl5-hfv-rec]], use [[lem:tl5-hfz-rec]] for h at p with 𝔥 = 𝔰₁^v, and bound (Σ_Z
𝔷_Z²)^(1/2) by 𝔷₁′ |D̂h| + 𝔷₂′ |h|, by Minkowski's inequality over Z. Bound μ² (Σ_Z |D̂Ψ_Z|²)^(1/2) by
[[eq:tl5-hfp-family]] with 𝔚 = Γ, b = 1 and n = 7, that is by C₁^Γ ℰ_g^(1/2) + √7 (C_(1,ϱ)^p ϱ(p) + C_(1,0)^p η₀(p))
with the weights of the step, in place of √7 times the bound of one field; bound μ^(3/2) |D̂h| by [[lem:tl5-hfp-c1]]
with B = ∅ and μ |h| by [[lem:tl5-hfp-abs]] (c). The rest is the proof of [[lem:tl5-hfv-rec]]. ∎

**Lemma {#lem:tl5-hfp-low}** (The second derivatives at low levels, with the words of each length together.) In the
setting of [[lem:tl5-hfp-abs]] (c), let 0 ≤ m ≤ N − 4. Then the step on second derivatives at low levels of the lemma in
use holds with 𝔐_p^(m) in place of (2𝔐^(m))^(1/2) max(C_S, C₁) in its part with ℰ_g, its parts with ϱ and η₀ being
formed with C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p; and for 𝔶₀ = 𝔶₁ = 1, 𝔐_p^(m) ≤ (2𝔐^(m))^(1/2) max(C_S^E, C₁^z).

*Proof.* In that step, L_g² is the sum over b ≤ m + 1 of Σ_(|C|=b) (μ^(b+2) |Ψ_C|² + μ^(b+3) |D̂Ψ_C|²), with the weights
of the step, and there are 7^b words of length b. By [[lem:tl5-hfp-abs]] (c) and [[eq:tl5-hfp-family]] with 𝔚 = 𝔚_b and
n = 7^b, the two sums over |C| = b are at most the squares of C_S^p ℰ_g(p)^(1/2) + 7^(b/2) e_b and of C₁(𝔚_b)
ℰ_g(p)^(1/2) + 7^(b/2) e′_b, where e_b and e′_b are the parts with ϱ and η₀ of the bounds of one word. Minkowski's
inequality in the Euclidean norm over b and the two kinds gives L_g ≤ 𝔐_p^(m) ℰ_g(p)^(1/2) + (Σ_b 7^b (e_b² +
e′_b²))^(1/2), and Σ_(b≤m+1) 2 · 7^b = 2𝔐^(m), so the second term is at most (2𝔐^(m))^(1/2) times the largest of these
parts, as there. For 𝔶₀ = 𝔶₁ = 1, C₁(𝔚_b) ≤ 7^(b/2) C₁^z by [[lem:tl5-hfp-c1]], and C_S^p ≤ C_S^E; so 𝔐_p^(m)² ≤ Σ_b 7^b
(C_S^E² + C₁^z²) ≤ 2𝔐^(m) max(C_S^E, C₁^z)². ∎

**Theorem {#thm:tl5-hfp}** (Existence with the leaf constant, the weights of the words and the seven fields.) In the
setting of [[thm:tl5-hfz]], with the intrinsic Sobolev constants of [[lem:tl5-hft-face]], let 𝔶₀ ∈ (0, μ⁻²] and 𝔶₁ ∈ (0,
μ⁻¹], let S_F^p, S_M^p, ε_M^p and 𝔯^p be S_F^z, S_M^z, ε_M^z and 𝔯^z formed with the constants with index p of
[[def:tl5-hfp-constants]], and put

    η_p := 1 − max(ϑ₁, ϑ₂) − 𝔯^p,      A_p := η_p^(−1/2) δ_w + η_p⁻¹ (ε^z + ε_M^p),      B_p := η_p⁻¹ (S_F^p + S_M^p),

and let 𝔰_*^p be 𝔰_*^z formed with the constants with index p and with A_p in place of A_z. Suppose: (a) η₀ < 𝔰₁^v; (b)
the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_p > 0, 𝔰_*^p < 𝔰₁^v and the closing
condition

    4 A_p B_p = 4 η_p^(−3/2) (δ_w + η_p^(−1/2) (ε^z + ε_M^p)) (S_F^p + S_M^p) < 1.                 {#eq:tl5-hfp-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_p and 𝔰_*^p in place of A_w (or
A_(w,4)) and 𝔰_*. For 𝔶₀ = 𝔶₁ = 1 each constant with index p, and each of A_p, B_p and 𝔰_*^p, is at most the one of
[[thm:tl5-hfz]] it replaces, and η_p ≥ η_z; so the hypotheses of [[thm:tl5-hfz]], with the intrinsic Sobolev constants,
imply these.

*Proof.* The proof of [[thm:tl5-hfz]] applies with [[lem:tl5-hfp-abs]], [[lem:tl5-hfp-c1]], [[lem:tl5-hfp-low]] and, for
N = 4, [[lem:tl5-hfp-rec]] in place of [[lem:tl5-hfz-abs]], [[lem:tl5-hfz-c1]], the step at low levels and
[[lem:tl5-hfv-rec]]. Step 1 is the same and gives 𝔰(p) ≤ 𝔰_*^p < 𝔰₁^v. The bounds at p and on the faces that Steps 2 and
3 use hold with the constants with index p, by these lemmas and, for the constants of the products of level four with no
factor at a point, by [[lem:tl5-hfp-abs]] (a); ε^z is unchanged, as its coefficient of ϱ contains no Sobolev constant.
The rest is the proof of [[thm:tl5-hfv]] with A_p, B_p and [[eq:tl5-hfp-closing]]. For 𝔶₀ = 𝔶₁ = 1, [[lem:tl5-hfp-leaf]]
gives C_(E,r)^♯² ≤ 6C_(E,r)², and [[lem:tl5-hfp-abs]] gives 𝔗(𝔶) ≤ 1, k₁^(j,·,p) ≤ k₁^(j,·,z) and C_S^p ≤ C_S^E; so
C_(1,ϱ)^p ≤ C_(1,ϱ)^z, C_(1,0)^p ≤ C_(1,0) and C_(0,0)^p ≤ C_(0,0). By [[lem:tl5-hfp-c1]], C₁^p ≤ C₁^z and, at level
four, C₁^Γ ≤ √7 max_Z C₁^U({Z}) ≤ √7 C₁^z; with 𝔷₁′ ≤ √7 𝔷₁, 𝔷₂′ ≤ √7 𝔷₂ and C_S^p ≤ C_S^E this gives 𝔨_rec^(·,p) ≤
𝔨_rec^(·,z), and [[lem:tl5-hfp-low]] gives 𝔐_p^(m) ≤ (2𝔐^(m))^(1/2) max(C_S^E, C₁^z). Every constant of [[thm:tl5-hfz]]
is nondecreasing in these numbers, which gives the last claim as there. ∎

**Remark {#rem:tl5-hfp-what}** (What changes.) The constant of [[eq:tl5-hft-leaf]] comes from ‖(1 + Ω)A‖² ≤ 6 Σ_(|J|≤2)
‖ℒ^J A‖², while on each V_π the sum over the 43 words is exactly (1 + c_π + c_π²) ‖A_π‖²; so C_(E,r)^♯ is at most
(2/9)^(1/2) < 0.48 times (6C_(E,r)²)^(1/2), in every constant formed with a Sobolev inequality on a face. In the bounds
at a point the words J of length k < 2 take the weights 𝔶_k ≤ μ^(k−2), which the energies of the words JB and ZJB allow,
against the weight 1 of the words of length two; the terms of C_(E,r)(𝔶)² are divided by 𝔶₀ + 𝔶₁ c_π + c_π² in place of
1 + c_π + c_π², so the representations with small c_π are bounded through the words of lengths zero and one. The parts
with ϱ and η₀ carry 𝔗(𝔶), which is at most 1 for all admissible weights in [[lem:tl5-hft-small]] (b) and equals ((ν²𝔶₀ +
6ν𝔶₁ + 36)/43)^(1/2) at level four; in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a) it grows with the weights,
which then trade the part with ℰ_g against those with ϱ and η₀. In 𝔨_rec the seven fields are counted together: where √7
C₁^z counts the leading term of the recovery √7 times, C₁^Γ counts it once over the 301 words JZ, the nonlinear part
keeping the count 301^(1/2) = (7 · 43)^(1/2) and the parts with ϱ and η₀ the factor √7; at the levels N ≥ 6, 𝔐_p^(m)
counts the words of each length in the same way, in place of (2𝔐^(m))^(1/2) times the bound of one word. The leading
term of the recovery is the one term bounded through 𝒟_g, whose density carries 𝔨₂′ = 𝔨₂ − 1/(2Ω̂²z̲); the minimum in
[[eq:tl5-hfp-c1]] keeps C₁(𝔚) ≤ C₁^U(𝔚). The number K_rec = max(|T|⁻¹, λ_M^(−1/2)) is the operator norm of the map
(v_Z)_Z ↦ (|T|⁻¹ v_T, (Σ_(a<b) c^ab_j v_(K_ab))_j) of the proof of [[lem:tl5-hf-recovery]], by [[lem:tl5-hf-fields]]
(a), so it is the best constant of that step for vectors v_Z of any size; a smaller one would need bounds that separate
the words beginning with T from those beginning with a rotation, which 𝒥_g and 𝒟_g do not give. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfp]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfu]] carries the weights and the families of words into S_M, 𝔯_M and ε_M ([[thm:tl5-hfu]]).

### The products with no factor at a point, with the weights and the families of words {#sec:tl5-hfu}

This section carries the leaf constant, the weights of the words and the counting over families of words of
[[sec:tl5-hfp]] into the products of level four with no factor at a point, that is into the numbers S_M, 𝔯_M and ε_M of
[[def:tl5-hfq-constants]]. Four changes are made. First, the Sobolev inequality on the leaves in [[lem:tl5-hf4-face]]
(b) takes the weights 𝔶 and the constant C_(E,r)(𝔶) of [[lem:tl5-hfp-leaf]], and the inequality along the curves γ_ω in
(a) keeps the coefficients of |A|² and of |D̂A|² apart ([[lem:tl5-hfu-face]]). Second, the second derivatives of a
family of words are bounded in the Euclidean norm over the family, the leading term of the recovery counting once
([[lem:tl5-hfu-fam]]); this replaces the count 7 of the 49 words of length two in 𝔜_(1,t) and the count √602 of the
second derivatives in 𝔛_(2,t). Third, the remainders are added to the leading terms by the triangle inequality over the
words in place of (x + y)² ≤ 2x² + 2y², and those of the second derivatives gain a factor μ^(1/2) from the weights of
the energies. Fourth, the terms with η₀ keep the factor μ^(3/2) of the step, and those with ϱ the weights of
[[lem:tl5-hfq-theta]] ([[lem:tl5-hfu-mixed]]). The closing condition is [[eq:tl5-hfu-closing]]; for 𝔶₀, 𝔶₁ ≥ 1 every new
constant is at most the one it replaces, and the earlier closing conditions remain valid. [[lem:tl5-hfu-fam]] holds for
every N ≥ 4; the rest of the section is at level four, with the intrinsic Sobolev constants of [[lem:tl5-hft-face]], and
the notation is that of [[sec:tl5-hfp]].

**Lemma {#lem:tl5-hfu-face}** (The inequalities on a face, with weights and with the coefficients apart.) Let t, b, Σ,
γ_ω, S_t and the norms be as in [[lem:tl5-hf4-face]], in the form of [[lem:tl5-hft-face]] (c), let 𝔶₀, 𝔶₁ > 0, 𝔶₂ := 1
and C_(E,r)(𝔶) be as in [[lem:tl5-hfp-leaf]], and put

    𝔱_(r,0)(t) := [𝔳₀^(2r) R⁻³ (1 + 2r² |D̂∂_γ|²)]_t,      𝔱_(r,1)(t) := [2 𝔳₀^(2r) R⁻³ |∂_γ|²]_t,

both at most 𝔱_r(t). Then for every smooth covariant tensor field A of rank r with 1 ≤ r ≤ 4 on Q(t, b), the sum being
over the words J of length at most two in the six rotations,

    ⟦A⟧_(2,∞)² ≤ C_(E,r)(𝔶)² 𝔵_r(t) Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖_Σ²,
    ⟦A⟧_(∞,2)² ≤ [𝔳₀^(2r)]_t ∫_(S_t) |A|² dω + 𝔱_(r,0)(t) ‖A‖_Σ² + 𝔱_(r,1)(t) ‖D̂A‖_Σ².               {#eq:tl5-hfu-face}

*Proof.* For the first inequality fix v, as in the proof of [[lem:tl5-hf4-face]] (b) in the form of [[lem:tl5-hft-face]]
(c). The points γ_ω(v), ω ∈ S³, fill one leaf, and [[eq:tl5-hfp-leaf]] applied to A on it gives sup_ω |A|₀²(γ_ω(v)) ≤
C_(E,r)(𝔶)² Σ_J 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀²(γ_ω(v)) dω. With |ℒ^J A|₀ ≤ 𝔳₀^r |ℒ^J A|, multiply by e^(−φ), which is constant
on the leaf, integrate over v and use dω dv = R⁻³ dμ dτ₂/(1 − κκ′); the supremum of 𝔳₀^(2r) R⁻³ over Σ ⊂ Σ₁(t, v*) is at
most 𝔵_r(t). For the second, the proof of [[lem:tl5-hf4-face]] (a) in that form bounds e^(−φ(v)) ∫_(S³) |A|₀²(γ_ω(v)) dω
by ∫_(S_t) |A|₀² dω plus the integral over the part of Σ with v′ ≤ v, with e^(−φ) dω dv′, of |A|₀² + |ℒ_(∂_γ)A|₀² ≤
𝔳₀^(2r) ((1 + 2r²|D̂∂_γ|²) |A|² + 2|∂_γ|² |D̂A|²). With dω dv′ = R⁻³ dμ dτ₂/(1 − κκ′), bounding the two coefficients
times 𝔳₀^(2r) R⁻³ by their own suprema, in place of their largest, and |A|₀² by 𝔳₀^(2r) |A|² on S_t gives the second
inequality. ∎

**Lemma {#lem:tl5-hfu-fam}** (The second derivatives over a weighted family of words.) In the setting of
[[lem:tl5-hfz-abs]] and [[def:tl5-hfp-constants]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), let 𝔙 be a family of n distinct words C
with |C| ≤ j ≤ N − 1, each with a number 𝔬_C > 0 such that 𝔬_C² ≤ μ^(|C|+1). Let 𝔞_𝔄(𝔙) be, at each point, the operator
norm of the map

    (ξ_K)_(|K|≤N) ↦ (Σ_K 𝔬_C μ^(−|K|/2) 𝔄_CK ξ_K)_(C∈𝔙),

𝔄_CK := 0 for |K| > |C|, normed as in [[def:tl5-hfz-constants]], and put

    𝔩(𝔙) := k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙) + n^(1/2) 𝔵^z (k₁^(j,μ,p) + 2)/(1 − 𝔵^z).

Let w_C be the weight of the part with ϱ(p) of the bound of |D̂²Ψ_C| in the lemma in use: 1 in [[lem:tl5-hfs-linfty]]
and [[lem:tl5-hft-small]] (a), μ^(−(|C|+1)/2) in [[lem:tl5-hft-small]] (b) and ν^(−(|C|+1)/2) in [[lem:tl5-hfq-theta]].
Then at every point of Q(a, b)

    (Σ_(C∈𝔙) 𝔬_C² |D̂²Ψ_C|²)^(1/2) ≤ 𝔩(𝔙) 𝒥_g + (Σ_(C∈𝔙) 𝔬_C² w_C²)^(1/2) k₂^z ϱ(p)/(1 − 𝔵^z).         {#eq:tl5-hfu-fam}

Moreover 𝔞_𝔄(𝔙) ≤ (n/2)^(1/2) α_𝔄^(j,μ) and 𝔩(𝔙) ≤ n^(1/2) (k₁^(j,μ,p) + 2𝔵^z)/(1 − 𝔵^z).

*Proof.* Let q be a point of Q(a, b) and C ∈ 𝔙. As |H(q)| ≤ 𝔰(q) ≤ 𝔰₁^v, [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v applies to
Ψ_C at q, with 𝔣 and 𝔑′_C as in the proof of [[lem:tl5-hfz-words]] (b), and (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷′
(|D̂Ψ_C|² + |Ψ_C|²)^(1/2) as in the proof of [[lem:tl5-hfp-abs]] (b). Multiply by 𝔬_C, take the Euclidean norm over 𝔙
and apply Minkowski's inequality to each kind of term. A word determines its first letter and the word of its other
letters, so the words ZC, Z ∈ Γ, C ∈ 𝔙, are distinct, and 𝔬_C² ≤ μ^(|ZC|); the leading term therefore contributes at
most k₁^D 𝒥_g. The words C are distinct and 𝔬_C² ≤ μ μ^(|C|), so the terms with 𝔷_Z and with 𝔯_♯ |Ψ_C| contribute at
most μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) 𝒥_g, and, as Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², the terms with 𝔄 at most
(1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙) 𝒥_g. For each C, (1 − 𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) and, as in the proof of
[[lem:tl5-hfz-words]] (b), (1 − 𝔰₁^v)⁻¹ |𝔑′_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐_C), where 𝔐_C is the bound of the second
derivatives of the words of length at most |C| that [[lem:tl5-hfp-abs]] (b) gives. The weights of that bound do not
decrease with the length and 𝒟_g ≤ 𝒥_g, so 𝔐_C ≤ μ^(−(|C|+1)/2) (k₁^(j,μ,p) + 2𝔵^z) 𝒥_g/(1 − 𝔵^z) + w_C k₂^z
ϱ(p)/(1 − 𝔵^z). As 𝔬_C μ^(−(|C|+1)/2) ≤ 1, w_C ≥ 1 and 2(1 − 𝔵^z) + k₁^(j,μ,p) + 2𝔵^z = k₁^(j,μ,p) + 2, 𝔬_C times these
two terms is at most 𝔵^z (k₁^(j,μ,p) + 2) 𝒥_g/(1 − 𝔵^z) + 𝔬_C w_C k₂^z ϱ(p)/(1 − 𝔵^z), and the Euclidean norm over 𝔙 of
the first part is n^(1/2) times it. Adding the parts gives [[eq:tl5-hfu-fam]]. For the last claims, the row of C of the
map defining 𝔞_𝔄(𝔙) has the sum Σ_K 𝔬_C μ^(−|K|/2) ‖𝔄_CK‖ ≤ Σ_K μ^((|C|+1−|K|)/2) ‖𝔄_CK‖ ≤ 2^(−1/2) α_𝔄^(j,μ), so each
of the n components of the image is at most 2^(−1/2) α_𝔄^(j,μ) times the norm of the family, which gives the first
bound. With it, and with k₁^(j,μ,p) = k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ α_𝔄^(j,μ), 𝔩(𝔙) ≤
n^(1/2) (k₁^(j,μ,p) + 𝔵^z (k₁^(j,μ,p) + 2)/(1 − 𝔵^z)) = n^(1/2) (k₁^(j,μ,p) + 2𝔵^z)/(1 − 𝔵^z). ∎

**Definition {#def:tl5-hfu-constants}** (The constants with index u.) Let N = 4 and the setting be that of
[[thm:tl5-hfp]], at level four with θ, ν = μ^θ and the weights 𝔶₀, 𝔶₁ of [[def:tl5-hfp-constants]], and let 𝔗(𝔶)² :=
(ν²𝔶₀ + 6ν𝔶₁ + 36)/43 be its number for [[lem:tl5-hfq-theta]]. Let 𝔙₂ be the family of the 49 words of length two, each
with the number μ^(3/2), and 𝔙_Γ the family of the 301 words JZ, J a word of rotations with |J| ≤ 2 and Z ∈ Γ, the word
JZ with the number (𝔶_(|J|) μ⁴)^(1/2); as 𝔶_k ≤ μ^(k−2), both satisfy the hypothesis of [[lem:tl5-hfu-fam]], with j = 2
and j = 3. With the notation of [[lem:tl5-hfs-mixed]], [[lem:tl5-hfq-mixed]] and [[lem:tl5-hfu-face]], 𝔵_r(t), 𝔱_r(t),
𝔪(t) and [𝔳₀^(2r)]_t formed as in [[lem:tl5-hft-face]] (c), and ς_t := [k₂^z]_t (1 − 𝔵^z)⁻¹ (∫_(Σ₁(t,v*)) dμ
dτ₂/(1 − κκ′))^(1/2), put

    𝔛^u_(1,t) := C_(E,3)(𝔶) 𝔵₃(t)^(1/2) (1 + [ϖ₁]_t^(1/2)),
    𝔛^u_(2,t) := C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ([𝔩(𝔙_Γ)]_t + μ^(1/2) [ϖ₂]_t^(1/2)),
    𝔛′^u_(2,t) := 301^(1/2) 𝔗(𝔶) (μ/ν)² C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ς_t,
    𝔜^u_(1,t) := (μ 𝔱_(3,0)(t) + 𝔱_(3,1)(t) [𝔩(𝔙₂)]_t²)^(1/2),      𝔜′^u_(1,t) := 7 (μ/ν)^(3/2) 𝔱_(3,1)(t)^(1/2) ς_t,
    𝔜″^u_(1,t) := μ^(3/2) π (98 [𝔳₀⁶]_t)^(1/2),      𝔜″^u_(2,t) := μ^(3/2) π (686 [𝔳₀⁴]_t)^(1/2),

and, with w_t as in [[def:tl5-hfs-constants]], 𝔠^Mq₁, 𝔠^Mq₂ as in [[eq:tl5-hfq-m]] and 𝔜_(2,t) = 𝔱₂(t)^(1/2),

    S_M^u := μ^(−3/2) ∫_(−10)^(u*) w_t (𝔠^Mq₁ 𝔛^u_(1,t) 𝔜^u_(1,t) + 𝔠^Mq₂ 𝔛^u_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_M^u := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) (𝔠^Mq₁ 𝔛^u_(1,t) (𝔜′^u_(1,t) ϱ + 𝔜″^u_(1,t) η₀)
             + 𝔠^Mq₂ (𝔛^u_(2,t) 𝔜″^u_(2,t) η₀ + 𝔛′^u_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_M^u := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t 𝔠^Mq₂ 𝔛′^u_(2,t) 𝔜″^u_(2,t) dt.                      {#eq:tl5-hfu-constants}

**Lemma {#lem:tl5-hfu-mixed}** (The products with no factor at a point, with index u.) In the setting of
[[lem:tl5-hfq-mixed]] and [[def:tl5-hfu-constants]], with 𝔰 ≤ 𝔰₁^v on Q(t, b) and the constants with index p,
[[eq:tl5-hfs-mixed]] holds with 𝔛^u_(1,t), 𝔛^u_(2,t), 𝔛′^u_(2,t), 𝔜^u_(1,t), 𝔜′^u_(1,t), 𝔜″^u_(1,t) and 𝔜″^u_(2,t) in
place of 𝔛^q_(1,t), 𝔛^q_(2,t), 𝔛′_(2,t), 𝔜^q_(1,t), 𝔜′_(1,t), 𝔜″_(1,t) and 𝔜″_(2,t). For 𝔶₀, 𝔶₁ ≥ 1 each of these is at
most the one it replaces, formed with the constants with index p.

*Proof.* The first line of [[eq:tl5-hfs-mixed]] is unchanged. In the steps below [[lem:tl5-hfu-fam]] is applied on
Q(t, b), with ϱ in place of ϱ(p) as in the proof of [[lem:tl5-hfg-mixed]], and the bound of the lemma in use is that of
[[lem:tl5-hfq-theta]], so w_C = ν^(−(|C|+1)/2).

*μ² X₁.* By [[eq:tl5-hfu-face]] with r = 3, μ⁴ X₁² ≤ C_(E,3)(𝔶)² 𝔵₃(t) ‖(Σ_(J,B) 𝔶_(|J|) μ⁴ |ℒ^J D̂Ψ_B|²)^(1/2)‖_Σ², the
sum being over the 43 words J and the 49 words B of length two. At each point ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′_(J,B), as in the
proof of [[lem:tl5-hfs-mixed]]. The words JB are distinct, as the B have one length, and 𝔶_(|J|) μ⁴ ≤ μ^(|JB|), so
(Σ_(J,B) 𝔶_(|J|) μ⁴ |D̂Ψ_(JB)|²)^(1/2) ≤ 𝒥_g. A monomial of R′_(J,B) whose coefficient carries a letters of J is at most
Λ_a |Ψ_(σB)|, σ the subword of J left and |σB| = |JB| − a, and 𝔶_(|J|)^(1/2) μ² ≤ μ^(|JB|/2) = μ^(a/2) μ^(|σB|/2); as B
↦ σB is injective, Minkowski's inequality over the monomials gives (Σ_B 𝔶_(|J|) μ⁴ |R′_(J,B)|²)^(1/2) ≤ ρ′_(|J|) 𝒥_g
with ρ′_(|J|) as in the proof of [[lem:tl5-hfs-mixed]], and Σ_J ρ′_(|J|)² = ϖ₁. By Minkowski's inequality over the pairs
(J, B), (Σ_(J,B) 𝔶_(|J|) μ⁴ |ℒ^J D̂Ψ_B|²)^(1/2) ≤ (1 + ϖ₁^(1/2)) 𝒥_g, and so μ² X₁ ≤ 𝔛^u_(1,t) 𝔍_g.

*μ² X₂.* By [[eq:tl5-hfu-face]] with r = 4, μ⁴ X₂² ≤ C_(E,4)(𝔶)² 𝔵₄(t) ‖(Σ_(J,Z) 𝔶_(|J|) μ⁴ |ℒ^J D̂²Ψ_Z|²)^(1/2)‖_Σ²,
the sum being over the 43 words J and the Z ∈ Γ. At each point ℒ^J D̂²Ψ_Z = D̂²Ψ_(JZ) + R_(J,Z), as in the proof of
[[lem:tl5-hfs-mixed]]. By [[eq:tl5-hfu-fam]] for 𝔙_Γ the part with the D̂²Ψ_(JZ) is at most 𝔩(𝔙_Γ) 𝒥_g + 301^(1/2) 𝔗(𝔶)
(μ/ν)² k₂^z ϱ/(1 − 𝔵^z), as Σ_(J,Z) 𝔶_(|J|) μ⁴ ν^(−(|J|+2)) = 7 (μ/ν)⁴ (ν²𝔶₀ + 6ν𝔶₁ + 36) = 301 (μ/ν)⁴ 𝔗(𝔶)². A monomial
of R_(J,Z) whose coefficient carries a letters is contracted with Ψ_(σZ) or D̂Ψ_(σZ), |σZ| = |JZ| − a, and 𝔶_(|J|)^(1/2)
μ² ≤ μ^((|JZ|+1)/2) = μ^(1/2) μ^(a/2) μ^(|σZ|/2); with the background norms of that proof and the injectivity of Z ↦ σZ,
(Σ_(J,Z) 𝔶_(|J|) μ⁴ |R_(J,Z)|²)^(1/2) ≤ μ^(1/2) ϖ₂^(1/2) 𝒥_g. Minkowski's inequality over the pairs and in L² of the
face, with e^(−φ) ≤ 1 and Σ ⊂ Σ₁(t, v*) in the part with ϱ, gives μ² X₂ ≤ 𝔛^u_(2,t) 𝔍_g + 𝔛′^u_(2,t) ϱ.

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* By [[eq:tl5-hfu-face]] with r = 3 for A := D̂Ψ_B, summed over the 49 words B of length two,
μ³ Y₁² is at most μ³ [𝔳₀⁶]_t Σ_B ∫_(S_t) |D̂Ψ_B|² dω + 𝔱_(3,0)(t) ‖(μ³ Σ_B |D̂Ψ_B|²)^(1/2)‖_Σ² + 𝔱_(3,1)(t)
‖(μ³ Σ_B |D̂²Ψ_B|²)^(1/2)‖_Σ². On S_t, |D̂Ψ_B| ≤ η₀ and ∫_(S_t) dω = 2π², so the first term is at most (𝔜″^u_(1,t) η₀)²;
as μ³ = μ μ^(|B|), the second norm is at most μ^(1/2) 𝔍_g; and by [[eq:tl5-hfu-fam]] for 𝔙₂, whose sum of the 𝔬_C² w_C²
is 49 (μ/ν)³, the third norm is at most [𝔩(𝔙₂)]_t 𝔍_g + 7 (μ/ν)^(3/2) ς_t ϱ. With (x + y + z)^(1/2) ≤ x^(1/2) +
(y + z)^(1/2) and Minkowski's inequality in the plane this gives μ^(3/2) Y₁ ≤ 𝔜^u_(1,t) 𝔍_g + 𝔜′^u_(1,t) ϱ + 𝔜″^u_(1,t)
η₀. Likewise for A := Ψ_B, summed over the 343 words B of length three, with r = 2, |Ψ_B| ≤ η₀ on S_t and μ³ Σ_B
(|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², as 𝔱_(2,0)(t) and 𝔱_(2,1)(t) are at most 𝔱₂(t): μ^(3/2) Y₂ ≤ 𝔜_(2,t) 𝔍_g + 𝔜″^u_(2,t) η₀.

*The comparison.* Let 𝔶₀, 𝔶₁ ≥ 1, so that C_(E,r)(𝔶) ≤ C_(E,r)^♯ by [[lem:tl5-hfp-leaf]]. With the constants with index
p, 𝔭_r/2 is C_(E,r)^♯² in [[lem:tl5-hfq-mixed]] and [[lem:tl5-hfs-mixed]], and λ_t^μ and λ_t^(μ,2) are ([k₁^(3,μ,p)]_t +
2𝔵^z)/(1 − 𝔵^z) and ([k₁^(2,μ,p)]_t + 2𝔵^z)/(1 − 𝔵^z), by [[lem:tl5-hfz-abs]] and [[lem:tl5-hfp-abs]] (b). Then
𝔛^u_(1,t) ≤ 𝔛^q_(1,t), as (1 + x)² ≤ 2(1 + x²). By [[lem:tl5-hfu-fam]], [𝔩(𝔙_Γ)]_t ≤ 301^(1/2) λ_t^μ and [𝔩(𝔙₂)]_t ≤ 7
λ_t^(μ,2); with μ^(1/2) ≤ 2^(1/2) this gives 𝔛^u_(2,t) ≤ 𝔛^q_(2,t), and 𝔜^u_(1,t) ≤ 𝔱₃(t)^(1/2) (μ + [𝔩(𝔙₂)]_t²)^(1/2) ≤
𝔱₃(t)^(1/2) (1 + 7 λ_t^(μ,2)) = 𝔜^q_(1,t). As μ ≤ ν ≤ 1, 𝔶₀ ≤ μ⁻² and 𝔶₁ ≤ μ⁻¹, (μ/ν)⁴ 𝔗(𝔶)² ≤ ((μ/ν)² + 6(μ/ν)³ +
36(μ/ν)⁴)/43 ≤ 1, so 𝔛′^u_(2,t) ≤ 𝔛′_(2,t); and (μ/ν)^(3/2) ≤ 1, 𝔱_(3,1)(t) ≤ 𝔱₃(t) and μ^(3/2) ≤ 1 give the other
three. ∎

**Theorem {#thm:tl5-hfu}** (Level four, with the weights and the families of words in the products with no factor at a
point.) In the setting of [[thm:tl5-hfp]] with N = 4, let S_M^p, 𝔯_M^p and ε_M^p be S_(M,q), 𝔯_(M,q) and ε_(M,q) of
[[eq:tl5-hfq-constants]] formed with the constants with index p, so that S_M^p and ε_M^p are those of [[thm:tl5-hfp]]
and 𝔯_M^p is the part of 𝔯^p with the products with no factor at a point, let S_M^u, 𝔯_M^u and ε_M^u be as in
[[def:tl5-hfu-constants]], 𝔯^u := 𝔯^p − 𝔯_M^p + 𝔯_M^u, and put

    η_u := 1 − max(ϑ₁, ϑ₂) − 𝔯^u,      A_u := η_u^(−1/2) δ_w + η_u⁻¹ (ε^z + ε_M^u),      B_u := η_u⁻¹ (S_F^p + S_M^u),

and let 𝔰_*^u be 𝔰_*^p with A_u in place of A_p. Suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are
admissible for (𝔅₄, E_o⁴, E_i⁴); (c) η_u > 0, 𝔰_*^u < 𝔰₁^v and the closing condition

    4 A_u B_u = 4 η_u^(−3/2) (δ_w + η_u^(−1/2) (ε^z + ε_M^u)) (S_F^p + S_M^u) < 1.                 {#eq:tl5-hfu-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_u and 𝔰_*^u in place of A_(w,4) and 𝔰_*. For 𝔶₀, 𝔶₁ ≥ 1, S_M^u ≤
S_M^p, 𝔯_M^u ≤ 𝔯_M^p and ε_M^u ≤ ε_M^p, so η_u ≥ η_p, A_u ≤ A_p, B_u ≤ B_p and 𝔰_*^u ≤ 𝔰_*^p, and the hypotheses of
[[thm:tl5-hfp]] with N = 4 imply these.

*Proof.* The proof of [[thm:tl5-hfp]] applies with N = 4 and with A_u, 𝔰_*^u, 𝔯^u and η_u in place of A_p, 𝔰_*^p, 𝔯^p
and η_p. Step 1 is unchanged and gives 𝔰 ≤ 𝔰_*^u < 𝔰₁^v on D^κ_s. In Step 2 the terms 𝔑^M_I are bounded, as in the proof
of [[prop:tl5-hfq-bootstrap]], by the argument of the proof of [[prop:tl5-hfs-bootstrap]] with [[eq:tl5-hfq-m]] and the
bounds of μ² X₁, μ^(3/2) Y₁, μ² X₂ and μ^(3/2) Y₂ on the faces Σ₁(t, b′). By [[lem:tl5-hfu-mixed]], which applies there
as 𝔰 ≤ 𝔰₁^v on D^κ_s, these bounds hold with the constants of [[def:tl5-hfu-constants]], and expanding with 𝔍_g ≤
[𝔨₂]_t^(1/2) Y_s as there gives S_M^u Y_s³ + 𝔯_M^u Y_s² + ε_M^u Y_s in place of S_M^p Y_s³ + 𝔯_M^p Y_s² + ε_M^p Y_s. No
other step uses S_M^p, 𝔯_M^p or ε_M^p, and the rest is the proof of [[thm:tl5-hfv]] with A_u, B_u and
[[eq:tl5-hfu-closing]]. For the last claim, each constant of [[def:tl5-hfu-constants]] is at most the one it replaces,
by [[lem:tl5-hfu-mixed]], and S_M, 𝔯_M and ε_M are nondecreasing in these constants; so 𝔯^u ≤ 𝔯^p and η_u ≥ η_p, and
A_u, B_u and 𝔰_*^u, which are nonincreasing in η_u and nondecreasing in ε_M^u and S_M^u, are at most A_p, B_p and 𝔰_*^p.
∎

**Remark {#rem:tl5-hfu-what}** (What changes.) The products with no factor at a point are bounded through the Hölder
inequality [[eq:tl5-hf4-holder]], one factor in ⟦·⟧_(2,∞), which the Sobolev inequality on the leaves bounds, and the
other in ⟦·⟧_(∞,2), which the inequality along the curves γ_ω bounds. The first now carries C_(E,r)(𝔶) of
[[sec:tl5-hfp]], at most (2/9)^(1/2) (6C_(E,r)²)^(1/2) for 𝔶₀, 𝔶₁ ≥ 1 and smaller for the weights 𝔶_k ≤ μ^(k−2), which
the energies of the words JB and JZ allow, and the triangle inequality over the words: the factor (2(1 + ϖ₁))^(1/2) of
𝔛_(1,t) becomes 1 + ϖ₁^(1/2). In 𝔛_(2,t) the second derivatives of the 301 words JZ are counted together, so that √602
λ_t^μ becomes 𝔩(𝔙_Γ), in which the leading term of the recovery counts once and 301^(1/2) remains with the nonlinear
part and in the bound of 𝔞_𝔄(𝔙_Γ); and the remainders of ℒ^J D̂²Ψ_Z, whose solution factors Ψ_C and D̂Ψ_C
have |C| = |JZ| − a while the weight (𝔶_(|J|) μ⁴)^(1/2) of the step is at most μ^((|JZ|+1)/2), gain the factor μ^(1/2)
in place of the factor 2 of their square. In 𝔜_(1,t) the second derivatives of the 49 words of length two are counted
together, so that 7 λ_t^(μ,2) becomes 𝔩(𝔙₂), whose leading term counts once and whose nonlinear part carries 7 𝔵^z; the
first derivatives D̂Ψ_B, |B| = 2, have the weight μ² of their own length against the weight μ³ of the step, which gives
μ in place of 1 beside 𝔩(𝔙₂)², and the two coefficients of [[lem:tl5-hf4-face]] (a) are kept apart. The terms with η₀
keep the factor μ^(3/2) of the step, and those with ϱ the weights of [[lem:tl5-hfq-theta]], which give (μ/ν)^(3/2) in
𝔜′^u_(1,t) and (μ/ν)² 𝔗(𝔶) ≤ 1 in 𝔛′^u_(2,t). The coefficients 𝔠^Mq₁ and 𝔠^Mq₂, the factors w_t and [𝔨₂]_t and the
factor 𝔜_(2,t) are unchanged: in 𝔜_(2,t) the words B of length three have the weight μ³ of the step, so neither a count
nor a power is gained there. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfu]] are
established in this paper for no background at 10 l5.
[[sec:tl5-hfd]] gives the leaves one Sobolev constant for every rank and sums products over the words ([[thm:tl5-hfd]]).

### One leaf constant for every rank, and the products over the words {#sec:tl5-hfd}

This section makes two changes. First, the Sobolev inequality on the leaves of [[lem:tl5-hft-leaf]] and
[[lem:tl5-hfp-leaf]] bounds |A(ω)|₀ through the functions Σ_k |s_k(ω)|₀² of the isotypic subspaces V_π, that is through
the traces of their kernels at ω. The trace counts every copy of every representation of the isotropy group in the fibre
at ω, whose dimension is 5^r. The kernel itself commutes with the isotropy group, so on each isotypic component of the
fibre it is a multiple of the identity; summed over π with the weights, these multiples give one number for each spin,
the largest being that of spin zero, the constant of the functions ([[lem:tl5-hfd-leaf]]). So the inequality holds for
tensors of every rank with the constant C_(E,0)(𝔶) of the functions, which is also the best constant for each rank, and
every constant formed with a Sobolev inequality on a face takes it. Second, in the products with a factor at a point,
the monomials of 2𝔮̂ whose two factors are first derivatives D̂Ψ are summed over the words of each length before they
are bounded: the factor in the energies is then counted by 𝒥_g once for all its words, and the factor at a point by the
square root of the number of its own words, in place of 7^(j′/2), that of all the words of the level, and these
monomials need no recovery constant ([[lem:tl5-hfd-words]]). Both changes enter the constants with index d
([[def:tl5-hfd-constants]], [[thm:tl5-hfd]]). The closing condition is [[eq:tl5-hfd-closing]]; every new constant is at
most the one it replaces, for all weights, and the earlier closing conditions remain valid. The notation is that of
[[sec:tl5-hfp]] and, for N = 4, of [[sec:tl5-hfu]].

**Lemma {#lem:tl5-hfd-leaf}** (One leaf constant for every rank.) In the setting of [[lem:tl5-hfp-leaf]] let 𝔶₀, 𝔶₁ > 0
and 𝔶₂ := 1, and for j ∈ ℕ put

    𝔖_j(𝔶) := (1/(2π²(2j + 1))) Σ_((j₁,j₂)) (2j₁ + 1)(2j₂ + 1)/(𝔶₀ + 𝔶₁ c_(j₁j₂) + c_(j₁j₂)²),

the sum over the j₁, j₂ ∈ (1/2)ℕ with j₁ + j₂ − j ∈ ℕ and |j₁ − j₂| ≤ j ≤ j₁ + j₂. Then 𝔖_j(𝔶) ≤ 𝔖_0(𝔶) = C_(E,0)(𝔶)²,
C_(E,r)(𝔶)² = Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶), and for every r ≥ 0, every C² covariant tensor field A of rank r on S_(u,v)
and every ω ∈ S³

    |A(ω)|₀² ≤ C_(E,0)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀² dω,                                     {#eq:tl5-hfd-leaf}

where C_(E,0)(𝔶)² = (1/(2π²)) Σ_(n≥0) (n + 1)²/(𝔶₀ + 𝔶₁ n(n + 2) + n²(n + 2)²). In particular C_(E,0)(𝔶) ≤ C_(E,r)(𝔶)
and C_(E,0)^♯ ≤ C_(E,r)^♯ for every r, and C_(E,r)(𝔶)² ≤ 5^r C_(E,0)(𝔶)².

*Proof.* Let E, the action of SO(4), the point o, the V_π and c_π be as in the proof of [[lem:tl5-hft-leaf]],
complexified, and put w_π := 𝔶₀ + 𝔶₁ c_π + c_π² and CG(π) := {|j₁ − j₂|, …, j₁ + j₂} for π = (j₁, j₂). Write the fibre
E_o as an orthogonal sum of subspaces U on which the isotropy group SO(3) acts irreducibly, of spin j_U, and let E^U be
the subbundle with fibre g·U at g·o, g ∈ SO(4). It is well defined, as U is invariant under the isotropy group; it is
invariant under SO(4); and the E^U are orthogonal, as SO(4) preserves h₀. So L²(S³, E) is the orthogonal sum of the
invariant subspaces L²(S³, E^U), and V_π the orthogonal sum of their π-isotypic parts V_π^U. By Frobenius reciprocity,
as in that proof, dim V_π^U = dim π · dim Hom_(SO(3))(π, U), which is dim π if j_U ∈ CG(π) and 0 otherwise, as (j₁, j₂)
restricted to the diagonal SU(2) contains each [j] at most once. For an orthonormal basis (s_k) of V_π^U the operator
K_π^U(ω) := Σ_k s_k(ω) ⟨·, s_k(ω)⟩₀ on the fibre at ω does not depend on the basis, so K_π^U(g·ω) = g K_π^U(ω) g⁻¹ for
g ∈ SO(4). At o it maps into U, vanishes on the orthogonal complement of U and commutes with the isotropy group, so by
Schur's lemma it is a multiple of the orthogonal projection P_U onto U; its trace is Σ_k |s_k(o)|₀² = dim V_π^U/(2π²),
as in that proof. Hence K_π^U(o) = dim π P_U/(2π²(2j_U + 1)) if j_U ∈ CG(π), and 0 otherwise.

Let A = Σ_π A_π as in that proof, and expand each A_π in an orthonormal basis of V_π made of bases of the V_π^U. For a
unit vector u in the fibre at ω, the Cauchy–Schwarz inequality over π and over these basis vectors gives |⟨A(ω), u⟩₀|² ≤
Σ_π w_π ‖A_π‖² · Σ_π w_π⁻¹ Σ_U ⟨K_π^U(ω) u, u⟩₀. By the invariance it suffices to bound the second factor at ω = o,
where Σ_π w_π⁻¹ Σ_U K_π^U(o) = Σ_U 𝔖_(j_U)(𝔶) P_U, an operator of norm at most the largest 𝔖_j(𝔶). In the proof of
[[lem:tl5-hfp-leaf]], Σ_π w_π ‖A_π‖² = Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖², and taking the supremum over u gives
[[eq:tl5-hfd-leaf]] with the largest 𝔖_j(𝔶) in place of C_(E,0)(𝔶)². It remains to compare the 𝔖_j(𝔶). The (j₁, j₂) of
the sum defining 𝔖_j(𝔶) have d := j₁ − j₂ ∈ {−j, −j + 1, …, j}, as j₁ + j₂ − j ∈ ℕ, and for fixed d the number κ :=
(j₁ + j₂)/2, with 2κ ∈ ℕ, determines (j₁, j₂). As (2j₁ + 1)(2j₂ + 1) ≤ (2κ + 1)², 2j₁(j₁ + 1) + 2j₂(j₂ + 1) ≥
4κ(κ + 1) = c_(κκ) because j₁² + j₂² ≥ 2κ², and 𝔶₀ + 𝔶₁ c + c² is increasing in c ≥ 0, the terms with a fixed d add up
to at most Σ_κ (2κ + 1)²/(𝔶₀ + 𝔶₁ c_(κκ) + c_(κκ)²) = 2π² 𝔖_0(𝔶); with the 2j + 1 values of d this gives 𝔖_j(𝔶) ≤
𝔖_0(𝔶). The representations with 0 ∈ CG(π) are the (κ, κ), with c_(κκ) = n(n + 2) for n := 2κ, so 𝔖_0(𝔶) = C_(E,0)(𝔶)²,
which is the value of the sum in [[eq:tl5-hfd-leaf]]. Finally m_(j₁j₂)(r) = Σ_(j∈CG(j₁,j₂)) e_j(r) gives C_(E,r)(𝔶)² =
Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶), which is at least 𝔖_0(𝔶) as e_0(r) ≥ 1 (the tensor du ⊗ ⋯ ⊗ du is invariant) and at most 5^r
𝔖_0(𝔶) as Σ_j e_j(r) (2j + 1) = dim E_o = 5^r. ∎

**Lemma {#lem:tl5-hfd-words}** (The products over the words of one length.) In the setting of [[lem:tl5-hfs-products]],
with the notation of [[def:tl5-hfs-bounds]], put λ̂^♮₀(ν′) := √5 and λ̂^♮_k(ν′) := ν′^(k/2) λ^♮_k for k ≥ 1, and for
0 ≤ n ≤ N and ν′ > 0

    𝔠^D_n(ν′) := 16 Σ⁴_n λ̂^♮_(k₁)(ν′) λ̂^♮_(k₂)(ν′),
    𝔠^(D,7)_n(ν′) := 16 Σ⁴_n λ̂^♮_(k₁)(7ν′) λ̂^♮_(k₂)(7ν′) 7^(min(k₃,k₄)/2) χ(k),

with χ(k) := 0 if N = 4 and k = (0, 0, 2, 2), and χ(k) := 1 otherwise. Let 𝔡_n be the part with ϱ(p) of the right side
of the first inequality of [[eq:tl5-hfs-products]] and 𝔡′_(j′) that of the second for |J| = j′, in the forms that the
lemma in use gives them. Then at every point of Q(a, b), the sums being over the words of the lengths shown,

    (Σ_(|I|=n) μ^n |𝔑^L_I|²)^(1/2) ≤ μ^(−3/2) (𝔠^(D,7)_n(μ) 𝔰_P + 7^(n/2) (𝔠^♮_n(μ) − 𝔠^D_n(μ)) 𝔓) 𝒥_g + 7^(n/2) 𝔡_n,
    (Σ_(|J|=j′) μ^n |ℒ^J N(h)|²)^(1/2) ≤ μ^((n−j′−3)/2) (𝔠^(D,7)_(j′)(μ) 𝔰_P
        + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔓) 𝒥_g + 7^(j′/2) 𝔡′_(j′)      (j′ < n).          {#eq:tl5-hfd-words}

Moreover 𝔠^D_n(ν′) ≤ 𝔠^(2♮)_n(ν′) and 𝔠^(D,7)_n(ν′) ≤ 7^(n/2) 𝔠^D_n(ν′).

*Proof.* Use the second expansion of the proof of [[lem:tl5-hfg-quadratic]]. Call a monomial of ℒ^I(2𝔮̂) one of type D
if both its factors D̂h give it the leading term D̂Ψ_K of their expansions ℒ^K D̂h = D̂Ψ_K + ⋯ of
[[lem:tl5-hfs-quadratic]] (a). For a term c_m 𝒯_m of 2𝔮̂ and a decomposition of the positions of the letters of I into
four sets, on ĝ⁻¹, ĝ⁻¹, D̂h, D̂h, carrying the subwords I₁, I₂, I₃, I₄ with k₁, …, k₄ letters, the monomial of type D is
c_m 𝒯_m(X₁, X₂, D̂Ψ_(I₃), D̂Ψ_(I₄)), X_i := ℒ^(I_i) ĝ⁻¹ (ĝ⁻¹ if I_i is empty), its background factors carry b := k₁ + k₂
letters, and |X_i| ≤ λ̂^♮_(k_i)(1) as counted there. In the count of [[lem:tl5-hfs-quadratic]] (b) the sum 16 Σ⁴_n λ̂^♮
λ̂^♮ β₁^♮ β₁^♮ of 𝔠^(2♮)_n is that of 2𝔮̂, the norms of the terms of the expansion of each ℒ^K D̂h adding up to at most
β₁^♮(|K|), whose term 1 is that of D̂Ψ_K. So the sum of ν ν′^(b/2) over the monomials of type D is at most 𝔠^D_n(ν′),
and that of ν ν′^(b/2) 𝔰^(q−2) over the other monomials is at most 𝔠^♮_n(ν′) − 𝔠^D_n(ν′); and 𝔠^D_n ≤ 𝔠^(2♮)_n, as
β₁^♮ ≥ 1 and the other sums of 𝔠^(2♮)_n are nonnegative. The other monomials are bounded word by word as in the proof of
[[lem:tl5-hfs-products]], with 𝔠^♮_n(μ) − 𝔠^D_n(μ) in place of 𝔠^♮_n(μ) in the part with 𝒥_g and as there in the part
with ϱ(p), and the Euclidean norm over the 7^n words I is at most 7^(n/2) times the largest; this gives the terms with 𝔓
and with 𝔡_n.

Let a monomial of type D belong to 𝔑^L_I. Its solution factors D̂Ψ_(I₃) and D̂Ψ_(I₄) have k₃ + k₄ = n − b letters; for
N = 4 the decomposition with k = (0, 0, 2, 2) gives two high factors and belongs to 𝔑^M_I, and two factors D̂Ψ_C of
order at least N − 1 would need 2N − 4 letters, more than N for N ≥ 5. So the one with fewer letters, Φ₁ := D̂Ψ_(I_P)
with k_P := min(k₃, k₄), is low, as the other would then be high as well; let Φ₂ := D̂Ψ_(I_E) be the other, with k_E :=
n − b − k_P letters. As in the proof of [[lem:tl5-hfs-products]], |Φ₁| ≤ μ^(−(k_P+3)/2) 𝔰_P and μ^(n/2) μ^(−(k_P+3)/2)
μ^(−k_E/2) = μ^(−3/2) μ^(b/2). Fix m and the four sets of positions. As I runs over the words of length n, the four
subwords run independently over all words of their lengths, so the Euclidean norm over I of the monomial, times μ^(n/2),
is at most |c_m| μ^(−3/2) μ^(b/2) times the product of (Σ_(I₁) |X₁|²)^(1/2) ≤ 7^(k₁/2) λ̂^♮_(k₁)(1), the same for X₂,
(Σ_(I_P) μ^(k_P+3) |Φ₁|²)^(1/2) ≤ 7^(k_P/2) 𝔰_P and (Σ_(I_E) μ^(k_E) |D̂Ψ_(I_E)|²)^(1/2) ≤ 𝒥_g, the words I_E being
distinct. As 7^(k/2) μ^(k/2) λ̂^♮_k(1) = λ̂^♮_k(7μ), Minkowski's inequality over m, with Σ_m |c_m| = 16, and over the
n!/(k₁! k₂! k₃! k₄!) decompositions for each k gives μ^(−3/2) 𝔠^(D,7)_n(μ) 𝔰_P 𝒥_g. These monomials carry no second
derivative, so they have no part with ϱ(p); and k₁ + k₂ + min(k₃, k₄) ≤ n gives 𝔠^(D,7)_n(ν′) ≤ 7^(n/2) 𝔠^D_n(ν′).
Minkowski's inequality over the two kinds of monomials gives the first inequality. For |J| = j′ < n, ℒ^J N(h) = 𝔑_J +
H^(αβ) D̂_αD̂_βΨ_J with 𝔑_J = 𝔑^L_J, also for N = 4, as j′ ≤ 3; the first inequality for the words of length j′, times
μ^((n−j′)/2), bounds the family of the 𝔑_J, and H^(αβ) D̂_αD̂_βΨ_J is bounded word by word as in the proof of
[[lem:tl5-hfs-products]], which gives the second inequality. ∎

**Definition {#def:tl5-hfd-constants}** (The constants with index d.) The constants with index d are the constants with
index p of [[def:tl5-hfp-constants]] and, for N = 4, those with index u of [[def:tl5-hfu-constants]], formed, first,
with C_(E,0)(𝔶) in place of C_(E,r)(𝔶) and with C_(E,0)^♯ in place of C_(E,r)^♯, for every rank r: in C_S^p (r = 2), in
C₁(𝔚) and C₁^p (r = 3), in C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p with their factors 𝔗(𝔶)², in 𝔛^u_(1,t), 𝔛^u_(2,t) and
𝔛′^u_(2,t) (r = 3 and 4), and in every other constant formed with a Sobolev inequality on a face, and in the constants
formed from these, 𝔨_rec^(·,p) and 𝔐_p^(m) among them. They are formed, second, with 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ in place of the
products 𝔤_(𝒥,s) 𝔎, 𝔤_(𝒥,s) 𝔎_ϱ and 𝔤_(𝒥,s) 𝔎₀ in 𝔞_(o,s), 𝔞_(i,s), 𝔟_(o,s) and 𝔟_(i,s) of [[def:tl5-hfs-constants]], in
their forms with index p, where, with 𝔠^D and 𝔠^(D,7) as in [[lem:tl5-hfd-words]],

    𝔎^D := (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) (𝔠^(D,7)_(j′)(μ) C_P
           + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔎))²)^(1/2),

and 𝔎^D_ϱ and 𝔎^D₀ are formed in the same way with C_(P,ϱ), 𝔎_ϱ and with C_(P,0), 𝔎₀ in place of C_P, 𝔎; here C_P,
C_(P,ϱ), C_(P,0), 𝔎, 𝔎_ϱ and 𝔎₀ are C_P^♮, C_(P,ϱ)^♮, C_(P,0)^♮ and the 𝔎 of [[def:tl5-hfs-constants]] in their forms
with index d (for N = 4, C_P^v, C_(P,ϱ)^v and C_(P,0)^v of [[lem:tl5-hfv-rec]]). The number 𝔤_(𝒥,s) in the minimum of
ε_(w,q) is kept. For N ≥ 6 let S_F^d and 𝔯^d be S_F^p and 𝔯^p of [[thm:tl5-hfp]] formed with the constants with index d,
and S_M^d := ε_M^d := 0; for N = 4 let S_F^d, S_M^d, ε_M^d and 𝔯^d be S_F^p, S_M^u, ε_M^u and 𝔯^u of [[thm:tl5-hfu]] so
formed. Put

    η_d := 1 − max(ϑ₁, ϑ₂) − 𝔯^d,      A_d := η_d^(−1/2) δ_w + η_d⁻¹ (ε^z + ε_M^d),      B_d := η_d⁻¹ (S_F^d + S_M^d),

and let 𝔰_*^d be 𝔰_*^p (N ≥ 6) or 𝔰_*^u (N = 4) formed with the constants with index d and with A_d in place of A_p or
A_u.

**Theorem {#thm:tl5-hfd}** (Existence with one leaf constant for every rank and the products over the words.) In the
setting of [[thm:tl5-hfp]] (N ≥ 6) or of [[thm:tl5-hfu]] (N = 4), suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1
− ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_d > 0, 𝔰_*^d < 𝔰₁^v and the closing condition

    4 A_d B_d = 4 η_d^(−3/2) (δ_w + η_d^(−1/2) (ε^z + ε_M^d)) (S_F^d + S_M^d) < 1.                 {#eq:tl5-hfd-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_d and 𝔰_*^d in place of A_w (or
A_(w,4)) and 𝔰_*. For all admissible weights each constant with index d is at most the one it replaces, η_d ≥ η_p (or
η_u), and A_d, B_d and 𝔰_*^d are at most A_p, B_p and 𝔰_*^p (or A_u, B_u and 𝔰_*^u); so the hypotheses of
[[thm:tl5-hfp]] (N ≥ 6) and of [[thm:tl5-hfu]] (N = 4) imply these, and for N = 4 and 𝔶₀, 𝔶₁ ≥ 1 so do those of
[[thm:tl5-hfp]].

*Proof.* By [[lem:tl5-hfd-leaf]], [[eq:tl5-hfp-leaf]] holds for every rank r and all weights with C_(E,0)(𝔶) in place of
C_(E,r)(𝔶), and so with C_(E,0)^♯ in place of C_(E,r)^♯ for 𝔶₀ = 𝔶₁ = 1. The proofs of [[lem:tl5-hft-face]],
[[lem:tl5-hfp-abs]] (a) and [[lem:tl5-hfu-face]] use [[eq:tl5-hfp-leaf]] only through its form, so these lemmas hold
with C_(E,0)(𝔶) and C_(E,0)^♯ in place of C_(E,r)(𝔶) and C_(E,r)^♯; the lemmas of [[sec:tl5-hfp]] and [[sec:tl5-hfu]]
use the Sobolev constants only through these, and so hold with the constants with index d. Then the proof of
[[thm:tl5-hfp]] (N ≥ 6) or of [[thm:tl5-hfu]] (N = 4) applies with the constants with index d, η_d, A_d, B_d, 𝔰_*^d and
[[eq:tl5-hfd-closing]], with one change in Step 2 of the proof of [[prop:tl5-hfs-bootstrap]], on which it rests. There
the family over |I| = j of the nonlinear terms other than 𝔑^M_I, which are −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I with |J| < |I|
in the sum, is bounded by [[eq:tl5-hfd-words]] and the definition of 𝔮_(jj′), in place of [[eq:tl5-hfs-products]] and
the Cauchy–Schwarz inequality over the 7^(j′) words: its norm is at most μ^(−j/2) Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′)
(𝔠^(D,7)_(j′)(μ) 𝔰_P + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔓) μ^(−3/2) 𝒥_g plus the part with ϱ that the proof
uses. The rest of Step 2 holds as written, and in Step 3, at each point, 𝔰_P ≤ C_P e^(φ/2) Y_s + C_(P,ϱ) ϱ + C_(P,0) η₀
and 𝔓 ≤ 𝔎 e^(φ/2) Y_s + 𝔎_ϱ ϱ + 𝔎₀ η₀; Minkowski's inequality in the Euclidean norm over j then gives the terms with
𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ in place of those with 𝔤_(𝒥,s) 𝔎, 𝔤_(𝒥,s) 𝔎_ϱ and 𝔤_(𝒥,s) 𝔎₀. For the last claim, C_(E,0)(𝔶) ≤
C_(E,r)(𝔶) and C_(E,0)^♯ ≤ C_(E,r)^♯ by [[lem:tl5-hfd-leaf]], and every constant of [[thm:tl5-hfp]] and [[thm:tl5-hfu]]
is nondecreasing in the Sobolev constants. By [[lem:tl5-hfd-words]], 𝔠^(D,7)_(j′)(μ) ≤ 7^(j′/2) 𝔠^D_(j′)(μ), and C_P ≤
𝔎, C_(P,ϱ) ≤ 𝔎_ϱ and C_(P,0) ≤ 𝔎₀, as the number 𝔨_B in 𝔎, 𝔎_ϱ and 𝔎₀ is at least 1; so each term of the inner sum of
𝔎^D is at most the corresponding term of 𝔤_(𝒥,s) 𝔎, and 𝔎^D ≤ 𝔤_(𝒥,s) 𝔎, 𝔎^D_ϱ ≤ 𝔤_(𝒥,s) 𝔎_ϱ and 𝔎^D₀ ≤ 𝔤_(𝒥,s) 𝔎₀. So
𝔯^d ≤ 𝔯^p (or 𝔯^u) and S_F^d ≤ S_F^p, and the rest follows as in the proof of [[thm:tl5-hfu]]. ∎

**Remark {#rem:tl5-hfd-what}** (What changes.) In [[lem:tl5-hft-leaf]] the bound |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖²
takes the trace of the kernel at ω, the sum of its eigenvalues over the 5^r dimensions of the fibre, where the pointwise
bound needs only the largest eigenvalue of the kernels summed over π with the weights, the Cauchy–Schwarz inequality
being taken over π and the basis together for one direction in the fibre; each kernel is a multiple of the identity on
each isotypic component of the fibre for the isotropy group, so that sum is 𝔖_j(𝔶) on the component of spin j, and
𝔖_j(𝔶) ≤ 𝔖_0(𝔶). So C_(E,r)(𝔶)² = Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶) becomes 𝔖_0(𝔶) = C_(E,0)(𝔶)², a factor between 1 and 5^r;
the rank enters the Sobolev constants on the faces only through the comparison factors 𝔳₀^r and 𝔴₀^r and the coefficient
1 + 2r²|D̂∂_γ|² of the step along the curves. No smaller constant holds for any rank with these weights: for A := f du ⊗
⋯ ⊗ du, whose Lie derivatives along the rotations are (Kf) du ⊗ ⋯ ⊗ du, [[eq:tl5-hfd-leaf]] is the inequality for the
function f, and for the functions f := Σ_(c_π≤M) (𝔶₀ + 𝔶₁ c_π + c_π²)⁻¹ K_π(·, o), K_π(·, o) the kernel at o of the
π-isotypic functions, the left side divided by the sum on the right tends to C_(E,0)(𝔶)² as M → ∞. The split of the
derivatives between the leaves and the curves is unchanged: the leaves need the words of length two in the six
rotations, and the curves one derivative. In S_F the products with a factor at a point were counted word by word, each
word I bounded through 𝒥_g, which already sums over all the words, and the family over the 7^(j′) words of a length then
counted 7^(j′/2) times; in [[eq:tl5-hfd-words]] the monomials of type D, which give the term 16 λ̂₀² 2^n = 80 · 2^n of
𝔠^♮_n at Λ = 0, are summed over the words first, so the factor in the energies is counted once, the factor at a point by
the 7^(k_P) words of its own length, and the background factors by theirs, which the argument 7ν′ of λ̂^♮ carries. At
Λ = 0 the coefficient 7^(n/2) 𝔠^D_n of these monomials, 7^(n/2) 80 · 2^n, becomes 80 Σ_(k₃+k₄=n) C(n, k₃)
7^(min(k₃,k₄)/2) χ, for n = 4 and N = 4 80 (2 + 8 · 7^(1/2)) in place of 49 · 1280, and they enter with C_P in place of
𝔎, as their factor in the energies is a first derivative, for which no recovery constant and no 𝔷 is needed. The other
monomials keep the count 7^(j′/2), and the parts with ϱ keep 𝔤_(ϱ,s). As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfd]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfe]] gives the transport along the curves a weight and the parts with ϱ their own count ([[thm:tl5-hfe]]).

### A weight in the transport along the curves, and the parts with ϱ over the second derivatives {#sec:tl5-hfe}

This section makes two changes. First, the Sobolev inequalities on the faces, and at level four the bound along the
curves in the products with no factor at a point, carry integrals over the leaves from the initial leaf along the curves
γ_ω; the derivative 2⟨B, ℒ_(∂_γ)B⟩₀ of |B|₀² along a curve is bounded there by |B|₀² + |ℒ_(∂_γ)B|₀². We bound it by
𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² with a positive function 𝔲, one for the steps of zeroth order, one for those of first order
and, at level four, one for the products with no factor at a point ([[lem:tl5-hfe-face]]). A bracket 𝔲X + 𝔲⁻¹Y with X,
Y > 0 has the least value 2(XY)^(1/2), at 𝔲 = (Y/X)^(1/2), against X + Y for 𝔲 = 1. In the bracket of the first-order
constant, X = (μ^(1/2) + ϖ′^(1/2))² comes from the first derivatives ℒ^J D̂Ψ_B, whose leading terms D̂Ψ_(JB) the weights
of the step bound with the factor μ^(1/2) over their energies, and Y from their Lie derivatives along the curves, that
is from their derivatives D̂ℒ^J D̂Ψ_B, which carry the recovery constant, and from the terms with D̂∂_γ. Second, in the
products with a factor at a point the part with ϱ comes only from the monomials whose factor in the energies is a second
derivative D̂²Ψ_C, through the residual of its recovery. These are among the monomials of H₁^(λσ) D̂_λD̂_σh and H₂^(λσ)
D̂_λD̂_σh in which the factor D̂²h gives its leading term, and a number 𝔠^ϱ_n counts the latter in place of 𝔠^♮_n
([[lem:tl5-hfe-rho]]); when all Λ_k and Λ^R_k vanish, 𝔠^ϱ_n + 1 = 2^n against 𝔠^♮_n + 1 = 81 · 2^n, up to terms with the
factor 𝔰_♭. Both changes enter the constants with index l ([[def:tl5-hfe-constants]], [[thm:tl5-hfe]]). The closing
condition is [[eq:tl5-hfe-closing]]; with the weights equal to 1 every new constant is at most the one it replaces, and
the earlier closing conditions remain valid. The notation is that of [[sec:tl5-hfd]] and, for N = 4, of [[sec:tl5-hfu]].

**Lemma {#lem:tl5-hfe-face}** (The transport along the curves with a weight.) Let 𝔲 be a positive continuous function on
D̄, p ∈ D^κ, a := τ₁(p), b := τ₂(p), S_a, the curves γ_ω, ∂_γ and 𝔨₁ as in [[lem:tl5-hf-sobolev]], h₀, 𝔳₀ and 𝔴₀ as in
[[lem:tl5-hft-face]], and 𝔶₀, 𝔶₁ > 0, 𝔶₂ := 1 and C_(E,0)(𝔶) as in [[lem:tl5-hfd-leaf]].

(a) For every tensor field A of rank r on Q(a, b) of the regularity of [[lem:tl5-hf-sobolev]], the sums being over the
words J of length at most two in the six rotations,

    |A(p)|² ≤ C_(E,0)(𝔶)² 𝔴₀(p)^(2r) (Σ_(|J|≤2) 𝔶_(|J|) ∫_(Σ₁(a,b)) 𝔳₀^(2r) R⁻³ ((𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²) |ℒ^J A|²
              + 2𝔲⁻¹ |∂_γ|² |D̂ ℒ^J A|²) dμ dτ₂/(1 − κκ′)
              + sup_(S_a) 𝔳₀^(2r) Σ_(|J|≤2) 𝔶_(|J|) ∫_(S_a) |ℒ^J A|² dω).                             {#eq:tl5-hfe-face}

(b) For every symmetric 2-tensor field A as in [[lem:tl5-hf-sobolev]], the inequality of that lemma, in the form of
[[lem:tl5-hft-face]] (b) with the weights 𝔶_(|J|) on its sums over J and with C_(E,0)(𝔶)² in place of 6C_(E,2)², holds
with (𝔲 + 8𝔲⁻¹ |D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔲⁻¹ 𝔨₁ in place of (1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁ in C_S^E, C_(S,0)^E being
formed with C_(E,0)(𝔶)² in place of 6C_(E,2)² as well.

(c) In the setting of [[lem:tl5-hfu-face]], with [·]_t the supremum over Σ₁(t, v*), the second inequality of
[[eq:tl5-hfu-face]] holds with 𝔱_(r,0)(t; 𝔲) := [𝔳₀^(2r) R⁻³ (𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²)]_t and 𝔱_(r,1)(t; 𝔲) := [2𝔲⁻¹
𝔳₀^(2r) R⁻³ |∂_γ|²]_t in place of 𝔱_(r,0)(t) and 𝔱_(r,1)(t).

For 𝔲 = 1 these are the forms of [[eq:tl5-hf-cs-r]], of [[lem:tl5-hf-sobolev]] and of [[eq:tl5-hfu-face]] that
[[lem:tl5-hfp-abs]] (a), [[lem:tl5-hfu-face]] and [[lem:tl5-hfd-leaf]] give.

*Proof.* (a) Let v_p be the value of v at p. The points γ_ω(v_p), ω ∈ S³, fill the leaf of p, and the points γ_ω(1/2)
fill S_a. For a word J put g_J(v) := ∫_(S³) |ℒ^J A|₀²(γ_ω(v)) dω. By [[eq:tl5-hfd-leaf]] on the leaf of p, with the
weights 𝔶_(|J|), and |A| ≤ 𝔴₀^r |A|₀ ([[lem:tl5-hft-face]]),

    |A(p)|² ≤ 𝔴₀(p)^(2r) C_(E,0)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) g_J(v_p).

As in the proof of [[lem:tl5-hft-face]], h₀ has constant coefficients, so ℒ_(∂_γ) h₀ = 0 and along each curve, with B :=
ℒ^J A, (d/dv) |B|₀² = 2⟨B, ℒ_(∂_γ)B⟩₀, which is at most 𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² at each point, by 2xy ≤ 𝔲x² + 𝔲⁻¹y²
for x, y ≥ 0. Integrating over ω ∈ S³ and over v from 1/2 to v_p, with dω dv = R⁻³ dμ dτ₂/(1 − κκ′) on the face, gives
g_J(v_p) ≤ g_J(1/2) + ∫_(Σ₁(a,b)) R⁻³ (𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀²) dμ dτ₂/(1 − κκ′), and g_J(1/2) ≤ sup_(S_a) 𝔳₀^(2r)
∫_(S_a) |ℒ^J A|² dω, as |·|₀ ≤ 𝔳₀^r |·|. As D̂ is torsion free, ℒ_(∂_γ)B = D̂_(∂_γ)B + Σ_(i=1)^r B(…, D̂∂_γ ·, …),
so |ℒ_(∂_γ)B| ≤ |∂_γ| |D̂B| + r |D̂∂_γ| |B| ([[lem:tl5-hf4-face]]), and with (x + y)² ≤ 2x² + 2y²

    𝔲 |B|₀² + 𝔲⁻¹ |ℒ_(∂_γ)B|₀² ≤ 𝔳₀^(2r) ((𝔲 + 2r² 𝔲⁻¹ |D̂∂_γ|²) |B|² + 2𝔲⁻¹ |∂_γ|² |D̂B|²).

Summing over J with the weights gives [[eq:tl5-hfe-face]]. (b) Let r = 2 and B := ℒ^J A. As in (a), the left side is at
most 𝔴₀(p)⁴ C_(E,0)(𝔶)² Σ_J 𝔶_(|J|) g_J(v_p), and g_J(v_p) is at most g_J(1/2) plus the integral of R⁻³ 𝔳₀⁴ ((𝔲 +
8𝔲⁻¹ |D̂∂_γ|²) |B|² + 2𝔲⁻¹ |D̂_(∂_γ)B|²) over the face with dμ dτ₂/(1 − κκ′), by |ℒ_(∂_γ)B| ≤ |D̂_(∂_γ)B| + 2|D̂∂_γ| |B|
in place of the bound through |D̂B|. In the proof of [[lem:tl5-hf-sobolev]], |D̂_(∂_γ)B|² ≤ 𝔨₁ (e_o[B] + κ′ e_i[B])
and |B|² ≤ (e_o[B] + κ′ e_i[B])/(2Ω̂² z̲) at the points of the face, and (e_o + κ′ e_i)/(1 − κκ′) = ε₁; bounding the
coefficient of ε₁[B] by its supremum over the face gives (b). (c) In the proof of [[lem:tl5-hfu-face]], the second
inequality comes from (d/dv)|A|₀² = 2⟨A, ℒ_(∂_γ)A⟩₀ ≤ |A|₀² + |ℒ_(∂_γ)A|₀² along the curves, integrated as in
[[lem:tl5-hf4-face]] (a) with the factors e^(−φ). With 𝔲 |A|₀² + 𝔲⁻¹ |ℒ_(∂_γ)A|₀² in its place, the pointwise bound of
the proof of (a) with B := A, and the suprema over Σ₁(t, v*) of the two coefficients times 𝔳₀^(2r) R⁻³, give 𝔱_(r,0)(t;
𝔲) and 𝔱_(r,1)(t; 𝔲); the rest of that proof holds as written. For 𝔲 = 1 every step is that of the proofs cited. ∎

**Lemma {#lem:tl5-hfe-rho}** (The parts with ϱ, counted over the second derivatives.) In the setting of
[[lem:tl5-hfs-quadratic]], for ν′ ∈ (0, 1] let λ^♮_k(ν′) and b^♮_g(k, ν′) be λ^♮_k and b^♮_g(k) of
[[def:tl5-hfs-bounds]] formed with ν′^(a/2) Λ_a in place of Λ_a for every a, so that λ^♮_k(ν′) = ν′^(k/2) λ^♮_k and
b^♮_g(0, ν′) = 𝔤₀, and put, for 0 ≤ n ≤ N, with Σ^m_n as in [[def:tl5-hfg-graded]],

    𝔠^ϱ_n(ν′) := Σ⁴_n λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1
                 + 𝔰_♭ (Σ⁶_n b^♮_g(k₁, ν′) λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀).                            {#eq:tl5-hfe-rho}

(a) In the second expansion of [[lem:tl5-hfg-quadratic]], with n := |I|, every monomial of ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I
with a solution factor D̂²Ψ_C is a monomial of ℒ^I (H₁^(λσ) D̂_λD̂_σh) or of ℒ^I (H₂^(λσ) D̂_λD̂_σh) in which the Lie
derivative ℒ^K D̂²h of the factor D̂²h gives its term D̂²Ψ_K; and the sum of ν ν′^(b/2) 𝔰(p)^(q−2) over these monomials,
with the notation of [[eq:tl5-hfs-sum]], is at most 𝔠^ϱ_n(ν′).

(b) In [[lem:tl5-hfs-products]], [[lem:tl5-hft-products]] and [[lem:tl5-hfq-theta]], and so in the parts 𝔡_n and 𝔡′_(j′)
of [[eq:tl5-hfd-words]], the terms with ϱ(p) hold with 𝔠^ϱ_n and 𝔠^ϱ_(|J|) in place of 𝔠^♮_n and 𝔠^♮_(|J|), at the same
argument: 1 in [[lem:tl5-hfs-products]], μ in [[lem:tl5-hft-products]] and ν in [[lem:tl5-hfq-theta]].

Moreover 0 ≤ 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′) − 𝔠^D_n(ν′), with 𝔠^D_n of [[lem:tl5-hfd-words]].

*Proof.* (a) The second expansion writes ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I as the sum of ℒ^I Q − H₁^(αβ) D̂_αD̂_βΨ_I and ℒ^I
R₃ − H₂^(αβ) D̂_αD̂_βΨ_I, and expands ℒ^I of each term of Q and R₃ by Leibniz's rule over its factors: ℒ^J h = Ψ_J; ℒ^J
D̂h, ℒ^J D̂²h and ℒ^J g⁻¹ by (ii), (iii) and (iv) of the proof of [[lem:tl5-hf-quadratic]]; ℒ^J R̂ and ℒ^K ĝ⁻¹ as
background factors. By (ii) the solution factors of the monomials of ℒ^J D̂h are D̂Ψ_J and factors Ψ_B; by (iv) and
[[lem:tl5-hfs-quadratic]] (a) the monomials of ℒ^J g⁻¹ have, besides factors g⁻¹ and background factors, solution
factors Ψ_B only; and by (iii), or [[lem:tl5-hfs-quadratic]] (a), ℒ^J D̂²h is D̂²Ψ_J, with the coefficient 1, plus
monomials whose solution factor is D̂Ψ_B or Ψ_B. So a solution factor D̂²Ψ_C comes only from a factor D̂²h, as its term
D̂²Ψ_K. The terms of Q and R₃ with a factor D̂²h are H₁^(λσ) D̂_λD̂_σh and H₂^(λσ) D̂_λD̂_σh; the others, 2𝔠(H₁)h,
2𝔠(H₂)h, 2𝔮̂ and 2𝔮 − 2𝔮̂, have the factors h, R̂, D̂h, g⁻¹, ĝ⁻¹ and H = −g⁻¹ h ĝ⁻¹. This is the first claim. In H₁^(λσ)
D̂_λD̂_σh, with the factors ĝ⁻¹, h, ĝ⁻¹, D̂²h carrying k₁, …, k₄ letters, the monomial with the term D̂²Ψ_(I₄) has q =
2, its factors ℒ^(I₁) ĝ⁻¹ and ℒ^(I₃) ĝ⁻¹ are background factors of norms at most λ^♮_(k₁) and λ^♮_(k₃), carrying k₁ and
k₃ letters, and the factors ĝ⁻¹ that carry no letter count λ^♮₀ = 1, as in the proof of [[lem:tl5-hfg-quadratic]]; so ν
ν′^(b/2) ≤ λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′), b = k₁ + k₃. Summing over the n!/(k₁! ⋯ k₄!) distributions of the letters for each
k, less the subtracted term H₁^(αβ) D̂_αD̂_βΨ_I, which is the one with k = (0, 0, 0, n) and the value 1, gives Σ⁴_n
λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1. In H₂^(λσ) D̂_λD̂_σh, with the factors g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h, the monomials of ℒ^(I₁)
g⁻¹ have, by [[lem:tl5-hfs-quadratic]] (a), background norms of total at most b^♮_g(k₁), a product of bounds Λ_a, each
for a factor carrying a letters, and of numbers that carry no letter, so at most b^♮_g(k₁, ν′) once each Λ_a is
multiplied by ν′^(a/2); the monomials have q ≥ 3, so 𝔰(p)^(q−2) ≤ 𝔰_♭; the factors ℒ^(I₃) ĝ⁻¹ and ℒ^(I₅) ĝ⁻¹ count
λ^♮_(k₃)(ν′) and λ^♮_(k₅)(ν′) as in H₁; and the subtracted term H₂^(αβ) D̂_αD̂_βΨ_I is the one with all letters on D̂²h,
of value b^♮_g(0) = 𝔤₀. This gives 𝔰_♭ (Σ⁶_n b^♮_g(k₁, ν′) λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀), and adding the two sums
gives the bound.

(b) In the proofs of these lemmas a monomial of 𝔑^L_I has a term with ϱ(p) only if its factor Φ₂ is a second derivative
D̂²Ψ_C, bounded by [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] or the bound of M_g^(j) of [[lem:tl5-hft-small]] (b); otherwise
Φ₂ is bounded by 𝔨_B 𝒥_g, as in the proof of [[lem:tl5-hfs-products]]. In each proof the term with ϱ(p) of such a
monomial is at most ν ν′^(b/2) 𝔰^(q−2) times a number that does not depend on the monomial, with ν′ = 1, μ or ν, namely
μ^(n/2) 2k₂ 𝔰 ϱ(p), μ^(−1/2) 2k₂ 𝔰 ϱ(p) or μ^((1−θ)n/2) ν^(−1/2) 2k₂ 𝔰 ϱ(p), and those proofs sum ν ν′^(b/2) 𝔰^(q−2)
over all the monomials by [[eq:tl5-hfs-sum]]. By (a) the sum over the monomials with a factor D̂²Ψ_C is at most
𝔠^ϱ_n(ν′), which gives the first inequality of each lemma with 𝔠^ϱ_n in its term with ϱ(p); the second follows from the
first for J and from the term H^(αβ) D̂_αD̂_βΨ_J, as there. The parts 𝔡_n and 𝔡′_(j′) of [[eq:tl5-hfd-words]] are those
of the lemma in use, so they take these forms.

For the last claim, the term with k = (0, 0, 0, n) of the first sum of [[eq:tl5-hfe-rho]] is 1 and that of the second
with all letters on the sixth factor is 𝔤₀, the other terms being nonnegative, so 𝔠^ϱ_n(ν′) ≥ 0. In 𝔠^♮_n(ν′) the
numbers β₁^♮ and β₂^♮ formed with the ν′^(a/2) Λ_a are at least 1 and the other sums of [[eq:tl5-hfs-cn]] are
nonnegative, so 𝔠^(2♮)_n(ν′) ≥ Σ⁴_n λ^♮_(k₁)(ν′) λ^♮_(k₃)(ν′) − 1 + 𝔠^D_n(ν′) and 𝔠^(3♮)_n(ν′) ≥ Σ⁶_n b^♮_g(k₁, ν′)
λ^♮_(k₃)(ν′) λ^♮_(k₅)(ν′) − 𝔤₀, which gives 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′) − 𝔠^D_n(ν′). ∎

**Definition {#def:tl5-hfe-constants}** (The constants with index l.) Let 𝔲₀, 𝔲₁ and, for N = 4, 𝔲_M be positive
continuous functions on D̄, and let the setting be that of [[def:tl5-hfd-constants]], with its constants with index d.
For p ∈ D^κ, a := τ₁(p) and b := τ₂(p), with the suprema over Σ₁(a, b), a family 𝔚 and the numbers 𝔩_D(𝔚), 𝔩_J(𝔚), ϖ′,
𝔨₂ and 𝔨₂′ as in [[def:tl5-hfp-constants]], 𝔗(𝔶) that of the lemma in use, and 𝔱_(3,0)(t; 𝔲) and 𝔱_(3,1)(t; 𝔲) as in
[[lem:tl5-hfe-face]] (c), put

    C_S^l(p)² := C_(E,0)(𝔶)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ ((𝔲₀ + 8𝔲₀⁻¹ |D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁),
    C₁^(U,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) (μ^(1/2) + ϖ′^(1/2))²
                    + 2𝔲₁⁻¹ |∂_γ|² (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^(D,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂′ (μ (𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) + 2𝔲₁⁻¹ |∂_γ|² 𝔩_D(𝔚)²),
    C₁^(J,l)(𝔚)² := C_(E,0)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) ϖ′
                    + 2𝔲₁⁻¹ |∂_γ|² (𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^l(𝔚) := min(C₁^(U,l)(𝔚), C₁^(D,l)(𝔚) + C₁^(J,l)(𝔚)),
    C_(1,ϱ)^l(p)² := 43 C_(E,0)(𝔶)² 𝔗(𝔶)² 𝔴₀(p)⁶ sup (𝔳₀⁶ R⁻³ 2𝔲₁⁻¹ |∂_γ|² (k₂^z)²/(1 − 𝔵^z)²)
                    · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),
    𝔜^l_(1,t) := (μ 𝔱_(3,0)(t; 𝔲_M) + 𝔱_(3,1)(t; 𝔲_M) [𝔩(𝔙₂)]_t²)^(1/2),
    𝔜′^l_(1,t) := 7 (μ/ν)^(3/2) 𝔱_(3,1)(t; 𝔲_M)^(1/2) ς_t,                                       {#eq:tl5-hfe-constants}

and let C₁^l be the largest of the C₁^l({B}), |B| ≤ N − 3, and, for N = 4, C₁^(Γ,l) := C₁^l(Γ). The constants with index
l are the constants with index d formed with C_S^l, C₁^l(𝔚), C₁^l, C₁^(Γ,l) and C_(1,ϱ)^l in place of C_S^p, C₁(𝔚),
C₁^p, C₁^Γ and C_(1,ϱ)^p in their forms with index d, wherever these enter, among them 𝔐_p^(m), 𝔨_rec^p, 𝔨_rec^(ϱ,p),
C_P^v, C_(P,ϱ)^v, C_(∞,μ)^(m) and C_((∞,ϱ),μ)^(m) with their forms, 𝔎, 𝔎_ϱ, 𝔎^D and 𝔎^D_ϱ; and, for N = 4, with
𝔜^l_(1,t) and 𝔜′^l_(1,t) in place of 𝔜^u_(1,t) and 𝔜′^u_(1,t) in S_M^u and 𝔯_M^u. With 𝔠^ϱ as in [[lem:tl5-hfe-rho]] put

    𝔤^l_(ϱ,s) := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(1) + 1))²)^(1/2),
    𝔤^l_(ϱ,t) := μ^(−1/2) (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(μ) + 1))²)^(1/2),
    𝔤^l_(ϱ,q) := ν^(−1/2) (Σ_(j≤4) (Σ_(j′≤j) μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^ϱ_(j′)(ν) + 1))²)^(1/2),

and let 𝔤_ϱ^l be 𝔤^l_(ϱ,s) for N ≥ 6 with option (a) of [[def:tl5-hft-constants]], 𝔤^l_(ϱ,t) with option (b), and
min(𝔤^l_(ϱ,q), 𝔤^l_(ϱ,t)) for N = 4, with θ and ν = μ^θ of [[def:tl5-hfq-constants]]. Let S_F^l, S_M^l, ε_M^l and 𝔯^l be
S_F^d, S_M^d, ε_M^d and 𝔯^d formed with the constants with index l (S_M^l = ε_M^l = 0 for N ≥ 6), and for N = 4 let
𝔯_M^l be 𝔯_M^u so formed, the part of 𝔯^l with the products with no factor at a point; put

    ε^l := 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^l k₂^z ϱ],      η_l := 1 − max(ϑ₁, ϑ₂) − 𝔯^l,
    A_l := η_l^(−1/2) δ_w + η_l⁻¹ (ε^l + ε_M^l),      B_l := η_l⁻¹ (S_F^l + S_M^l),

and let 𝔰_*^l be 𝔰_*^d formed with the constants with index l and with A_l in place of A_d.

**Theorem {#thm:tl5-hfe}** (Existence with a weight in the transport along the curves and the parts with ϱ over the
second derivatives.) In the setting of [[thm:tl5-hfd]], let 𝔲₀, 𝔲₁ and, for N = 4, 𝔲_M be positive continuous functions
on D̄, and the constants with index l be those of [[def:tl5-hfe-constants]]. Suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 −
ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_l > 0, 𝔰_*^l < 𝔰₁^v and the closing condition

    4 A_l B_l = 4 η_l^(−3/2) (δ_w + η_l^(−1/2) (ε^l + ε_M^l)) (S_F^l + S_M^l) < 1.                 {#eq:tl5-hfe-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_l and 𝔰_*^l in place of A_w (or
A_(w,4)) and 𝔰_*. For 𝔲₀ = 𝔲₁ = 𝔲_M = 1 each constant with index l is the one with index d it replaces, ε^l ≤ ε^z, η_l =
η_d, A_l ≤ A_d, B_l = B_d and 𝔰_*^l ≤ 𝔰_*^d; so the hypotheses of [[thm:tl5-hfd]] imply these with 𝔲₀ = 𝔲₁ = 𝔲_M = 1.

*Proof.* The proof of [[thm:tl5-hfd]] applies with the constants with index l, ε^l, η_l, A_l, B_l, 𝔰_*^l and
[[eq:tl5-hfe-closing]], with four changes.

*The steps of zeroth order.* In the proof of [[lem:tl5-hfp-abs]] (c), with the constants with index d, the step applies
[[lem:tl5-hf-sobolev]] in the form of [[lem:tl5-hft-face]] (b) with the weights 𝔶_(|J|) and C_(E,0)(𝔶); by
[[lem:tl5-hfe-face]] (b) with 𝔲 = 𝔲₀ this form holds with C_S^l(p) in place of C_S^p(p), the terms on S_a being the
same, so the step gives its bounds of Ψ_B(p) and of the families with C_S^l in place of C_S^p.

*The steps of first order.* In the proof of [[lem:tl5-hfp-c1]] use [[eq:tl5-hfe-face]] with r = 3 and 𝔲 = 𝔲₁ for each
A_B in place of [[eq:tl5-hf-cs-r]] in its intrinsic form with the weights. This replaces the functions f and W of that
proof by 𝔳₀⁶ R⁻³ (𝔲₁ + 18𝔲₁⁻¹ |D̂∂_γ|²) and 2𝔲₁⁻¹ |∂_γ|² 𝔳₀⁶ R⁻³, and leaves its terms on S_a unchanged. The rest of
that proof uses f and W only as nonnegative continuous functions on the face, through Minkowski's inequalities and the
bounds ∫ g 𝒟_g² ≤ sup (g 𝔨₂′) ℰ_g(p) and ∫ g 𝒥_g² ≤ sup (g 𝔨₂) ℰ_g(p) for functions g ≥ 0; so it gives
[[eq:tl5-hfp-family]] with C₁^l(𝔚) and C_(1,ϱ)^l in place of C₁(𝔚) and C_(1,ϱ)^p, with the same E₀, and the first-order
step of the lemma in use gives its bound of D̂Ψ_B(p) with C₁^l and C_(1,ϱ)^l. The bounds of [[lem:tl5-hfp-rec]],
[[lem:tl5-hfp-low]] and [[lem:tl5-hfv-rec]], and the bounds at a point that the proofs of [[thm:tl5-hfp]] and
[[thm:tl5-hfu]] take from the lemma in use, are formed from these two steps, the recovery and the absorption, in the
same way for all values of these constants; so they hold with the constants with index l.

*The products with no factor at a point.* For N = 4, the step for μ^(3/2) Y₁ in the proof of [[lem:tl5-hfu-mixed]] uses
[[eq:tl5-hfu-face]] with r = 3. By [[lem:tl5-hfe-face]] (c) with 𝔲 = 𝔲_M it holds with 𝔱_(3,0)(t; 𝔲_M) and 𝔱_(3,1)(t;
𝔲_M), and the rest of that step gives μ^(3/2) Y₁ ≤ 𝔜^l_(1,t) 𝔍_g + 𝔜′^l_(1,t) ϱ + 𝔜″^u_(1,t) η₀; the other bounds of
that proof are unchanged. So the expansion in the proof of [[thm:tl5-hfu]] gives S_M^l Y_s³ + 𝔯_M^l Y_s² + ε_M^l Y_s in
place of S_M^u Y_s³ + 𝔯_M^u Y_s² + ε_M^u Y_s.

*The terms with ϱ.* By [[lem:tl5-hfe-rho]] (b), the parts with ϱ(p) of [[eq:tl5-hfd-words]] hold with 𝔠^ϱ in place of
𝔠^♮. In Step 2 the terms with ϱ of the family of level j are then bounded as in Step 2 of the proofs of
[[prop:tl5-hfs-bootstrap]] (option (a)), [[prop:tl5-hft-bootstrap]] (option (b)) and [[prop:tl5-hfq-bootstrap]] (N = 4),
with 𝔠^ϱ_(j′)(·) + 1 in place of 𝔠^♮_(j′)(·) + 1, which gives 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t) and, for N = 4, either of 𝔤^l_(ϱ,q)
and 𝔤^l_(ϱ,t), in place of 𝔤_(ϱ,s), μ^(−1/2) 𝔤_(𝒥,s) and 𝔤_(ϱ,q). With the bound 𝔰 ≤ 𝔰₁^v of Step 1 and the absorption,
as in the proofs of [[thm:tl5-hfw]], [[thm:tl5-hfy]] and [[thm:tl5-hfz]], this part together with the forcing term is
bounded by Y_s ε^l in place of Y_s ε^z. The rest of the proof holds as written.

For the last claim, let 𝔲₀ = 𝔲₁ = 𝔲_M = 1. Then C_S^l, C₁^(U,l)(𝔚), C₁^(D,l)(𝔚), C₁^(J,l)(𝔚), C_(1,ϱ)^l, 𝔜^l_(1,t) and
𝔜′^l_(1,t) are C_S^p, C₁^U(𝔚), C₁^D(𝔚), C₁^J(𝔚) and C_(1,ϱ)^p with index d and 𝔜^u_(1,t) and 𝔜′^u_(1,t), so every
constant with index l other than ε^l is the one with index d, and S_F^l, S_M^l, ε_M^l, 𝔯^l, η_l and B_l are S_F^d,
S_M^d, ε_M^d, 𝔯^d, η_d and B_d. By [[lem:tl5-hfe-rho]], 𝔠^ϱ_n(ν′) ≤ 𝔠^♮_n(ν′), so each term of 𝔤^l_(ϱ,s), 𝔤^l_(ϱ,t) and
𝔤^l_(ϱ,q) is at most the corresponding one of 𝔤_(ϱ,s), μ^(−1/2) 𝔤_(𝒥,s) and 𝔤_(ϱ,q), and 𝔤_ϱ^l ≤ 𝔤_ϱ^v and ε^l ≤ ε^z. As
A_d and 𝔰_*^d are nondecreasing in ε^z, A_l ≤ A_d and 𝔰_*^l ≤ 𝔰_*^d. ∎

**Remark {#rem:tl5-hfe-what}** (What changes.) In [[lem:tl5-hft-face]], [[lem:tl5-hfp-abs]] (a) and [[lem:tl5-hfu-face]]
the derivative 2⟨B, ℒ_(∂_γ)B⟩₀ of |B|₀² along the curves is bounded by |B|₀² + |ℒ_(∂_γ)B|₀², which fixes the balance
between the two parts of each bracket; with 2xy ≤ 𝔲x² + 𝔲⁻¹y² it is free. A bracket 𝔲X + 𝔲⁻¹Y with X, Y > 0 has the
least value 2(XY)^(1/2) at 𝔲 = (Y/X)^(1/2), and 2(XY)^(1/2) ≤ X + Y, its value for 𝔲 = 1, with a large gain where X and
Y differ much. In the bracket of C₁^(U,l)(𝔚)², X = (μ^(1/2) + ϖ′^(1/2))²: its part μ comes from the leading terms
D̂Ψ_(JB) of the first derivatives ℒ^J D̂Ψ_B, whose words JB have length at most |B| + 2, so that the weights 𝔶_(|J|)
μ^(|B|+3) ≤ μ μ^(|JB|) of the step leave the factor μ over their energies, and its part ϖ′ from their remainders. And
Y = 18|D̂∂_γ|² X + 2|∂_γ|² 𝔩′², 𝔩′ := 𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2), carries the second derivatives, with the recovery
constant k₁^D = 𝔨_♯ K_rec ≥ √5 K_rec in 𝔩_D(𝔚). The least value at a point is at most 2^(3/2) |∂_γ| 𝔩′ X^(1/2) +
6√2 |D̂∂_γ| X, where the value for 𝔲₁ = 1 is at least 2|∂_γ|² 𝔩′²; the ratio of the leading parts is 2^(1/2)
X^(1/2)/(|∂_γ| 𝔩′), with X^(1/2) = μ^(1/2) + ϖ′^(1/2). The same holds in 𝔜^l_(1,t), whose first part carries μ against
𝔩(𝔙₂)² in its second. In C_S^l both parts are bounded through the densities of the same words, X = 1/(2Ω̂² z̲) and Y =
8|D̂∂_γ|²/(2Ω̂² z̲) + 2𝔨₁, and 𝔲₀ gains as far as these differ. Each weight is one function for all the faces and all
the families of words of its steps, and the parts of one step with ℰ_g, ϱ and η₀ share it; the part with ϱ of the
first-order step lies in Y and carries 𝔲₁⁻¹ in C_(1,ϱ)^l², and the parts with η₀ come from the leaf S_a and do not carry
the weight. In the products with a factor at a point the part with ϱ comes from the residual of the recovery of a second
derivative, and only the monomials of H₁^(λσ) D̂_λD̂_σh and H₂^(λσ) D̂_λD̂_σh with the term D̂²Ψ_K of ℒ^K D̂²h have one:
the monomials of 2𝔮̂ and 2𝔮 − 2𝔮̂ have first derivatives, those of 2𝔠(H₁)h and 2𝔠(H₂)h none, and the other monomials of
the Lie derivatives of D̂²h first derivatives or none. When all Λ_k and Λ^R_k vanish, the first sum of 𝔠^ϱ_n is 2^n, so
𝔠^ϱ_n + 1 = 2^n and 𝔠^♮_n + 1 = 81 · 2^n up to terms with the factor 𝔰_♭, and each term of 𝔤_ϱ^l is about 1/81 times the
corresponding one of 𝔤_ϱ^v; in general 𝔠^ϱ_n ≤ 𝔠^♮_n − 𝔠^D_n. The counts 𝔠^Mq₁ and 𝔠^Mq₂ of the products with no factor
at a point, the leaf constant C_(E,0)(𝔶), 𝔨₂, K_rec, 𝔨_♯, 𝔵^z and the thresholds are unchanged. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfe]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfc]] takes the threshold of the continuation at the smaller root and the factor 𝔤₁ for H ([[thm:tl5-hfc]]).

### The threshold of the continuation, and the factor of H at a point {#sec:tl5-hfc}

This section makes two changes. First, [[lem:tl5-continuation]] extends solutions under the a priori bound y_σ ≤ 2A, and
every smallness condition of this chapter is formed with that bound: Step 1 of the a priori estimate applies the bounds
at a point with ℰ_g(p) ≤ e^(φ(p)) Y_σ² ≤ 4e^(φ(p)) A², which gives the term with A of 𝔰_*. The argument needs only a
number 𝔜 at which q(y) := By² − y + A is negative, and every 𝔜 between the two roots Y₋ < Y₊ of q serves; the solution
then satisfies y_σ ≤ Y₋ = 2A/(1 + (1 − 4AB)^(1/2)), which lies between A and 2A and is close to A when 4AB is small
([[lem:tl5-hfc-cont]]). So 𝔰_* may be formed with Y₋ in place of 2A. Second, the bounds at a point carry the factor 2
of |H| ≤ 2|h| in the products 2C_S and 2C_(0,0). Under 𝔰 ≤ 𝔰_♭ the identity H = −g⁻¹ h ĝ⁻¹ gives |H| ≤ 𝔤₁ |h|, as it
does in the constant 𝔨_B, so these products become 𝔤₁ C_S and 𝔤₁ C_(0,0) ([[lem:tl5-hfc-h]]). Both changes enter the
constants with index c ([[def:tl5-hfc-constants]], [[thm:tl5-hfc]]). The closing condition is [[eq:tl5-hfc-closing]];
every new constant is at most the one it replaces, and the earlier closing conditions remain valid. The notation is that
of [[sec:tl5-hfe]].

**Lemma {#lem:tl5-hfc-cont}** (Existence by continuity with a threshold below 2A.) In the setting of
[[lem:tl5-continuation]] let A, B > 0 with 4AB < 1, and put

    Y₋ := 2A/(1 + (1 − 4AB)^(1/2)),      Y₊ := (1 + (1 − 4AB)^(1/2))/(2B),                               {#eq:tl5-hfc-y}

the roots of q(y) := By² − y + A, so that q < 0 on (Y₋, Y₊), q ≥ 0 on [0, Y₋], and A ≤ Y₋ < 2A < 1/(2B) ≤ Y₊. Let 𝔜 ∈
(Y₋, Y₊), and suppose that every solution g on every D^κ_s with y_σ(g) ≤ 𝔜 for all σ ∈ [1/2, s] satisfies (H1), (H2) and
(H4) of [[lem:tl5-continuation]], and that y_(1/2)(g) ≤ A for every solution g. Then there is a solution g on D^κ, and
y_σ(g) ≤ Y₋ for every σ ∈ [1/2, v*]. For 𝔜 = 2A the hypotheses are those of [[lem:tl5-continuation]].

*Proof.* With x := 4AB ∈ (0, 1), the roots of q are (1 ∓ (1 − x)^(1/2))/(2B), and (1 − (1 − x)^(1/2))/(2B) = x/(2B (1 +
(1 − x)^(1/2))) = Y₋. As 1 < 1 + (1 − x)^(1/2) ≤ 2, A ≤ Y₋ < 2A; 2A < 1/(2B) as x < 1; and 1/(2B) ≤ Y₊. As q has
positive leading coefficient and q(0) = A > 0, q < 0 exactly on (Y₋, Y₊), and q ≥ 0 on [0, Y₋]. So if y ≥ 0 satisfies y
≤ A + By² and y ≤ 𝔜, then q(y) ≥ 0 and y ≤ 𝔜 < Y₊ give y ≤ Y₋ < 𝔜; this takes the place of the first paragraph of the
proof of [[lem:tl5-continuation]], whose rest holds with 𝔜 in place of 2A. Let I be the set of s ∈ (1/2, v*] for which
there is a solution g on D^κ_s with y_σ(g) ≤ 𝔜 for all σ ∈ [1/2, s]. It is not empty, as y_(1/2)(g) ≤ A ≤ Y₋ < 𝔜 and y_σ
is continuous in σ. It is open: for s ∈ I, s < v*, and the solution g on D^κ_s, (H1) for the restrictions of g to the
D^κ_σ, σ ∈ (1/2, s], and y_σ(g) ≤ 𝔜 give y_σ(g) ≤ Y₋ < 𝔜, so y_s(g) < 𝔜; (H4) and (F3_W) of [[thm:tl5-wg]] extend g to a
solution g′ on some D^κ_(s′), s′ > s, and y_σ(g′) ≤ 𝔜 on [1/2, s″] for some s″ ∈ (s, s′] by continuity. It is closed, by
the argument of that proof with (H2), the bound y_σ ≤ 𝔜 passing to the limit as the bound y_σ ≤ 2A does there. So v* ∈
I. For the solution g on D^κ and σ ∈ (1/2, v*], the restriction of g to D^κ_σ is a solution with y_σ′ ≤ 𝔜 for σ′ ≤ σ, so
(H1) gives y_σ(g) ≤ Y₋, and y_(1/2)(g) ≤ A ≤ Y₋. For 𝔜 = 2A, which lies in (Y₋, Y₊), the hypotheses are (H1), (H2), (H4)
and (H3) of [[lem:tl5-continuation]]. ∎

**Lemma {#lem:tl5-hfc-h}** (The factor of H at a point.) Let h be as in [[def:tl5-hfg-graded]] and q a point with 𝔰(q) ≤
𝔰_♭. Then |H(q)| ≤ 𝔤₁ |h(q)|, with 𝔤₁ = 1 + 2𝔰_♭ of [[def:tl5-hfs-bounds]]. Consequently, under their hypotheses and in
the forms that the later lemmas of this chapter give them, [[lem:tl5-hfg-linfty]], [[lem:tl5-hfs-linfty]],
[[lem:tl5-hft-small]], [[lem:tl5-hfq-theta]] and [[lem:tl5-hfv-rec]] hold with 𝔤₁ C_S and 𝔤₁ C_(0,0) in place of 2C_S
and 2C_(0,0): in the first inequality of [[eq:tl5-hfs-linfty]], in C_∞^(m) and C_(∞,0)^(m) of [[eq:tl5-hfg-cinf]] and
their forms with μ and with ν, and in C_P^v and C_(P,0)^v of [[lem:tl5-hfv-rec]].

*Proof.* By [[lem:tl5-wg-norms]] (a), |H(q)| ≤ 2|h(q)| ≤ 2𝔰(q) ≤ 2𝔰_♭, as |h| ≤ 𝔰 and 𝔰_♭ ≤ 1/8. As g⁻¹ − ĝ⁻¹ = −g⁻¹ h
ĝ⁻¹, as in the proof of [[lem:tl5-hfg-quadratic]], H = −g⁻¹ h ĝ⁻¹. In the frame F, where ĝ^MN = η^MN, raising an index
with ĝ⁻¹ does not change the norm and a contraction with H multiplies it by at most |H|, so a factor g⁻¹ = ĝ⁻¹ + H that
raises an index costs at most 1 + |H| ≤ 1 + 2𝔰_♭ = 𝔤₁, as in the proofs of [[lem:tl5-hfs-quadratic]] (a) and
[[thm:tl5-hfv]]; this gives |H(q)| ≤ 𝔤₁ |h(q)|. In each lemma named, the hypothesis on Q(a, b), 𝔰 ≤ 𝔰₀^⋆, 𝔰₀^♮, 𝔰₀^μ or
𝔰₀^q, or 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 with the replacements of [[lem:tl5-hfy-abs]], each at most 𝔰_♭, gives 𝔰(p) ≤ 𝔰_♭ at the point p
of the bound. There the factors 2 of 2C_S and 2C_(0,0) are those of |H(p)| ≤ 2|h(p)| in the step of zeroth order, which
bounds μ |H(p)| by 2μ |h(p)| and μ |h(p)| by C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p), with the weights of the lemma in use (for
H in [[lem:tl5-hfq-theta]] the factor 2 is taken up by 2C_S and 2C_(0,0), as stated there, and in [[lem:tl5-hft-small]]
(a) the bound is that of |H(p)| by 2|h(p)|); each other quantity of 𝔰_P⁰, of 𝔰_g^(m) and of 𝔰 enters these maxima with
its own constant. With |H(p)| ≤ 𝔤₁ |h(p)| in place of |H(p)| ≤ 2|h(p)| the bound of μ |H(p)| has the factor 𝔤₁, and as
𝔤₁ ≥ 1 the entries 𝔤₁ C_S and 𝔤₁ C_(0,0) also bound the quantities Ψ_B that the entries 2C_S and 2C_(0,0) bounded; so
the maxima hold with 𝔤₁ C_S and 𝔤₁ C_(0,0). ∎

**Definition {#def:tl5-hfc-constants}** (The constants with index c.) In the setting of [[def:tl5-hfe-constants]], the
constants with index c are the constants with index l formed with 𝔤₁ C_S^l and 𝔤₁ C_(0,0) in place of 2C_S^l and
2C_(0,0), C_(0,0) in its form with index l: at the sites of [[lem:tl5-hfc-h]], in 𝔎 and 𝔎₀ of [[def:tl5-hfs-constants]],
which Step 3 of the proof of [[prop:tl5-hfs-bootstrap]] forms from the bound of 𝔰_P⁰, and in every constant formed from
these, among them 𝔎^D and 𝔎^D₀, C_P, C_(P,0), C_(∞,μ)^(m) and C_((∞,0),μ)^(m) with their forms with ν, S_F, 𝔯 and 𝔰_*.
Let S_F^c, S_M^c, ε_M^c and 𝔯^c be S_F^l, S_M^l, ε_M^l and 𝔯^l formed with them, ε^c := ε^l, and

    η_c := 1 − max(ϑ₁, ϑ₂) − 𝔯^c,      A_c := η_c^(−1/2) δ_w + η_c⁻¹ (ε^c + ε_M^c),      B_c := η_c⁻¹ (S_F^c + S_M^c).

For a number 𝔜 ≥ 0 let 𝔰_*^c[𝔜] be 𝔰_*^l formed with the constants with index c and with 𝔜/2 in place of A_l, so that
its term with A_l carries 𝔜 in place of 2A_l, and, when 4A_c B_c < 1, put

    Y_c := 2A_c/(1 + (1 − 4A_c B_c)^(1/2)),      𝔰_*^c := 𝔰_*^c[Y_c].                            {#eq:tl5-hfc-constants}

**Theorem {#thm:tl5-hfc}** (Existence with the threshold Y_c and the factor 𝔤₁.) In the setting of [[thm:tl5-hfe]], with
the constants with index c of [[def:tl5-hfc-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂)
a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_c > 0, the closing condition

    4 A_c B_c = 4 η_c^(−3/2) (δ_w + η_c^(−1/2) (ε^c + ε_M^c)) (S_F^c + S_M^c) < 1,                 {#eq:tl5-hfc-closing}

and 𝔰_*^c < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_c for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with 𝔰_*^c in place of 𝔰_*. Each
constant with index c is at most the one with index l it replaces, η_c ≥ η_l, A_c ≤ A_l, B_c ≤ B_l, Y_c ≤ 2A_c ≤ 2A_l
and 𝔰_*^c ≤ 𝔰_*^l; so the hypotheses of [[thm:tl5-hfe]] imply these.

*Proof.* If A_c = 0, the proof of [[thm:tl5-hf]] gives ĝ as the solution, with Y_σ(ĝ) = 0 = Y_c. Otherwise A_c > 0 and
B_c > 0, as S_F^c > 0, and Y_c < 2A_c by [[lem:tl5-hfc-cont]]. The term of 𝔰_*^c[𝔜] with A_l is a(p) 𝔜 with a(p) ≥ 0,
and its other terms do not depend on 𝔜 and are nonnegative, so 𝔰_*^c[𝔜] ≤ (𝔜/Y_c) 𝔰_*^c for 𝔜 ≥ Y_c; fix 𝔜 with Y_c < 𝔜
≤ 2A_c and 𝔜 𝔰_*^c < Y_c 𝔰₁^v, so that 𝔰_*^c[𝔜] < 𝔰₁^v.

*The factor of H.* By [[lem:tl5-hfc-h]], the bounds at a point that the proof of [[thm:tl5-hfe]] uses hold with the
constants with index c. The proofs on which it rests use the products 2C_S and 2C_(0,0) only through these bounds and
through 𝔎 and 𝔎₀, which Step 3 of the proof of [[prop:tl5-hfs-bootstrap]] forms from 𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0)
η₀, with 𝔤₁ in place of 2 by [[lem:tl5-hfc-h]]. So that proof applies with the constants with index c, and gives (H1)
with A_c and B_c, under the a priori bound it uses.

*The threshold.* In the proof of [[thm:tl5-hfe]] and in the proofs on which it rests, the a priori bound Y_σ ≤ 2A, A the
number of the theorem in use (A_w, A_(w,4), A_g, …, A_l), enters at three places, and we use Y_σ ≤ 𝔜 at each of them.
(i) In the a priori estimate, [[prop:tl5-hf-bootstrap]] and its forms, it enters only Step 1, through ℰ_g(p) ≤ e^(φ(p))
Y_σ(g)² ≤ 4e^(φ(p)) A² for p ∈ D^κ_σ, as φ ≤ φ(p) on Σ₁(τ₁(p), τ₂(p)). With ℰ_g(p) ≤ e^(φ(p)) 𝔜² in its place, the
bounds at p and the argument with Σ_* of the proof of [[thm:tl5-hfy]] give 𝔰 ≤ 𝔰_*^c[𝔜] < 𝔰₁^v on D^κ_s; Steps 2 and 3
use this smallness and Y_s itself, not the a priori bound, and so give Y_s ≤ A_c + B_c Y_s². (ii) In
[[lem:tl5-hf-persistence]] and [[lem:tl5-hf4-persistence]], as in the proofs of [[thm:tl5-hfg]] and [[thm:tl5-hf4g]],
the a priori estimate enters only through 𝔰 ≤ 𝔰_*, which gives |H| ≤ 1/8 and the bounds of θ_H, θ_H^(1) and θ_H^(2) (as
in the proof of [[thm:tl5-hfv]]) and, at level four, the bound of |D̂²Ψ_B|, |B| ≤ 3, by a constant (as in the proof of
[[thm:tl5-hf4t]]); and the a priori bound enters only P(N), through the bound μ^(−N) e^(Φ_o(u*) + Φ_i(v*)) 4A² of the
energies of level N. Under Y_σ ≤ 𝔜, (i) gives the first, with 𝔰_*^c[𝔜] < 𝔰₁^v, and P(N) holds with 𝔜² in place of 4A²;
so (H2) holds, and (H4) follows from |h|_k̂ < κ_m/2 as there. (iii) In the proof of [[thm:tl5-hf]] or of
[[thm:tl5-hf4]], [[lem:tl5-continuation]] is applied with y_σ := Y_σ; apply [[lem:tl5-hfc-cont]] with A := A_c, B := B_c
and 𝔜, which lies in (Y_c, Y₊) as 𝔜 ≤ 2A_c < Y₊. Its hypotheses are (H1), (H2) and (H4) for the solutions with Y_σ ≤ 𝔜,
given by the factor of H and by (i) and (ii), 4A_c B_c < 1 and Y_(1/2) = 0 ≤ A_c. It gives a solution g on D^κ with
Y_σ(g) ≤ Y_c for every σ ∈ [1/2, v*].

As Y_σ(g) ≤ Y_c and 𝔰_*^c[Y_c] = 𝔰_*^c < 𝔰₁^v, (i) with Y_c in place of 𝔜 and s = v* gives 𝔰 ≤ 𝔰_*^c on D^κ, |h|_k̂ <
κ_m/2 and the bounds of θ_H; the rest of the conclusions follows from these as in the proofs of [[thm:tl5-hf]] and
[[thm:tl5-hf4]], the bound for ε being [[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_*^c. For the last claim, 𝔤₁ ≤ 5/4 < 2 as 𝔰_♭ ≤ 1/8,
and every constant with index l is nondecreasing in the products it contains, so each constant with index c is at most
the one it replaces; then η_c ≥ η_l, A_c ≤ A_l, B_c ≤ B_l and 4A_c B_c ≤ 4A_l B_l, as in the proof of [[thm:tl5-hfe]].
Y_c ≤ 2A_c as 1 + (1 − 4A_c B_c)^(1/2) ≥ 1, and 𝔰_*^c[𝔜] is nondecreasing in 𝔜 and in the constants, so 𝔰_*^c ≤
𝔰_*^c[2A_c] ≤ 𝔰_*^l. ∎

**Remark {#rem:tl5-hfc-what}** (What changes.) The continuation needs, for the solutions it extends, a bound y_σ ≤ 𝔜
that (H1) makes strict, and q(𝔜) < 0 is what makes y ≤ A + By² and y ≤ 𝔜 give y ≤ Y₋ < 𝔜. The threshold 2A of
[[lem:tl5-continuation]] is one such number, with q(2A) = A(4AB − 1); every number between the roots serves, and the
bound of the solution is the smaller root Y₋ = 2A/(1 + (1 − 4AB)^(1/2)) = A + A²B + 2A³B² + ⋯, which tends to A as 4AB
tends to 0 and to 2A as 4AB tends to 1. The term of 𝔰_* with A carries the a priori bound, so it takes the factor 2/(1 +
(1 − 4A_c B_c)^(1/2)) in place of 2: when the closing condition holds with room this nearly halves that term, and when
the closing condition is close to binding the gain is small. As 𝔰_*^c < 𝔰₁^v is strict, a number 𝔜 slightly above Y_c
keeps 𝔰_*^c[𝔜] < 𝔰₁^v, and the solutions with Y_σ ≤ 𝔜 are those the continuation extends; Steps 2 and 3, the persistence
of regularity and the conclusions use the a priori bound only through the smallness it gives and through a bound of the
energies by a constant. The factor 2 of 2C_S and 2C_(0,0) is that of |H| ≤ 2|h|, which holds for |h| ≤ 1/2; at every
point where a bound at a point is formed, 𝔰 ≤ 𝔰_♭ holds, and there |H| ≤ 𝔤₁ |h|, the bound already used for 𝔨_B. So the
entry of C_P^v, of 𝔎 and of C_∞^(m) that bounds μ |H| loses its factor 2, the other entries keeping theirs; the factor 2
of 2𝒥_g in the nonlinear parts of the absorption, which comes from |H| ≤ 2|h| as well and enters only with 𝔵^z, is kept.
The counts, the recovery constants, the Sobolev constants, the weights 𝔲₀, 𝔲₁, 𝔲_M, the thresholds 𝔰₀ and 𝔰₁^v and the
rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfc]] are established in
this paper for no background at 10 l5.
[[sec:tl5-hff]] can put the parts with ϱ in 𝔯 and takes the zeroth order through the shorter words ([[thm:tl5-hff]]).

### The parts with ϱ through the bound at a point, and the zeroth order through the shorter words {#sec:tl5-hff}

This section makes two changes. First, in the products with a factor at a point the part with ϱ of a monomial is the
residual of the recovery of its factor D̂²Ψ_C times its factor Φ₁, which is H, h or a Ψ_B, and Step 2 of the bootstrap
bounds Φ₁ by 𝔰 ≤ 𝔰₁^v, which puts the part into ε. But Φ₁ is a quantity of 𝔰_P⁰, and at the levels N ≥ 6 with option (b)
of [[def:tl5-hft-constants]], where the part with ϱ of the bound of D̂²Ψ_C carries the weight μ^(−(|C|+1)/2), |Φ₁| ≤
μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰ leaves the factor μ^(−3/2) μ^(b/2) that the parts with 𝒥_g carry, so these parts hold with μ^(−1)
𝔰_P⁰ in place of 𝔰 ([[lem:tl5-hff-rho]]). Step 3 bounds 𝔰_P⁰ by C_P⁰ e^(φ/2) Y_s + C_(P,0)⁰ η₀, which has no part with
ϱ; the weight e^(−φ) of 𝒮 takes up the factor e^(φ/2), so the part with ϱ gives a term 𝔯_ϱ^f Y_s², which enters 𝔯, and a
part of ε with ϱ η₀. The two routes put the part in different places, and the theorem takes either. Second, the
zeroth-order step bounds the part |Ψ_(JB)|² of the density of each word JB through the energy of JB itself, whose weight
𝔶_(|J|) μ^(|B|+2) is at most μ^(|JB|), with equality at the largest weights. For JB = ZC, Z its first letter, the
bound |Ψ_(ZC)| ≤ 𝔷 (|D̂Ψ_C|² + |Ψ_C|²)^(1/2) in the proof of (∗) of [[lem:tl5-hfg-products]] passes it to the energy of
the shorter word C, whose weight leaves a factor μ; its coefficient 1/(2Ω̂² z̲) becomes 6μ 𝔷² 𝔨₂, six words ZC sharing
each C, or at most 7μ 𝔷² 𝔨₂ for the words that the first letters of a family share, and at each point of the face the
smaller of the two bounds is taken ([[lem:tl5-hff-zero]]). The word h has no shorter word; its step takes its own leaf
weight 𝔶₀^h, which multiplies its own part by 𝔶₀^h μ². Both changes enter the constants with index f
([[def:tl5-hff-constants]], [[thm:tl5-hff]]). The closing condition is [[eq:tl5-hff-closing]]; with 𝔶₀^h = 𝔶₀ and the
first route every new constant is at most the one it replaces, and the earlier closing conditions remain valid. The
notation is that of [[sec:tl5-hfc]].

**Lemma {#lem:tl5-hff-rho}** (The parts with ϱ through the bound of 𝔰_P⁰.) Let N ≥ 6, with option (b) of
[[def:tl5-hft-constants]], and let the setting be that of [[lem:tl5-hft-products]] with 𝔰 ≤ 𝔰₁^v on Q(a, b) and the
replacements of [[lem:tl5-hfy-abs]] and [[lem:tl5-hfz-abs]], so that the bounds of the second derivatives carry k₂^z
ϱ(p)/(1 − 𝔵^z) in place of 2k₂ ϱ(p). Then at every point of Q(a, b), for every word I with n := |I| ≤ N and every word J
with |J| < n, the two inequalities of [[lem:tl5-hft-products]], with 𝔠^ϱ in their terms with ϱ(p) as in
[[lem:tl5-hfe-rho]] (b), hold with

    μ^(−3/2) 𝔠^ϱ_n(μ) (1 − 𝔵^z)⁻¹ k₂^z 𝔰_P⁰ ϱ(p),
    μ^((n−|J|−3)/2) (𝔠^ϱ_(|J|)(μ) + 1) (1 − 𝔵^z)⁻¹ k₂^z 𝔰_P⁰ ϱ(p)                                      {#eq:tl5-hff-rho}

in place of their terms with ϱ(p), that is with μ^(−1) 𝔰_P⁰ in place of 𝔰 there; and the parts 𝔡_n and 𝔡′_(j′) of
[[eq:tl5-hfd-words]] take these forms.

*Proof.* By [[lem:tl5-hfe-rho]] (b) and the proofs of [[lem:tl5-hfs-products]] and [[lem:tl5-hft-products]], a monomial
of 𝔑^L_I has a term with ϱ(p) only if its factor Φ₂ is a second derivative D̂²Ψ_C, and then Φ₁ carries no derivative D̂,
as there are at most two in all, so it is H, h or Ψ_B with |B| ≤ N − 2, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰, with ℓ_P as in
the proof of [[lem:tl5-hfg-products]]. The part with ϱ(p) of the bound of Φ₂ is μ^(−ℓ_E(Φ₂)/2) k₂^z ϱ(p)/(1 − 𝔵^z), by
[[lem:tl5-hft-small]] (b) with the replacements. With |Φ_i| ≤ 𝔰 for the other factors, the term with ϱ(p) of the
monomial times μ^(n/2) is at most ν 𝔰^(q−2) μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔰_P⁰ k₂^z ϱ(p)/(1 − 𝔵^z), with ν its
background norm with the coefficient, q the number of its solution factors and b the number of letters on its background
factors; and ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n − b + 3, as in the proof of [[lem:tl5-hfs-products]], so μ^((n − ℓ_P(Φ₁) −
ℓ_E(Φ₂))/2) ≤ μ^(−3/2) μ^(b/2). The proof of [[lem:tl5-hft-products]] bounds the same term by ν 𝔰^(q−2) 𝔰 μ^(−1/2)
μ^(b/2) times the same factor k₂^z ϱ(p)/(1 − 𝔵^z), through |Φ₁| ≤ 𝔰; so the new bound is that one with μ^(−1) 𝔰_P⁰ in
place of 𝔰, and the sum over the monomials with a factor D̂²Ψ_C, by [[lem:tl5-hfe-rho]] (a) with ν′ = μ, gives the first
term of [[eq:tl5-hff-rho]]. For |J| < n, ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J. As there, μ^(n/2) |𝔑_J| = μ^((n−|J|)/2)
μ^(|J|/2) |𝔑_J|, and the first term for J bounds the part with ϱ(p) of μ^(|J|/2) |𝔑_J|. In H^(αβ) D̂_αD̂_βΨ_J the factor
Φ₁ is H, with ℓ_P(H) = 2 and |H| ≤ μ⁻¹ 𝔰_P⁰, and the part with ϱ(p) of the bound of D̂²Ψ_J is μ^(−(|J|+1)/2) k₂^z
ϱ(p)/(1 − 𝔵^z); so μ^(n/2) times their product is at most μ^((n−|J|−3)/2) 𝔰_P⁰ k₂^z ϱ(p)/(1 − 𝔵^z), where the proof of
[[lem:tl5-hft-products]] has μ^((n−|J|−1)/2) 𝔰. Adding the two gives the second term. The parts 𝔡_n and 𝔡′_(j′) are
those of the lemma in use, so they take these forms. ∎

**Lemma {#lem:tl5-hff-zero}** (The zeroth-order step through the shorter words.) In the setting of [[lem:tl5-hfp-abs]]
(c), with the weights 𝔶₀, 𝔶₁ and 𝔲₀ and the constants with index l of [[def:tl5-hfe-constants]], let 𝔶₀^h ∈ (0, μ⁻²] and
𝔶^h := (𝔶₀^h, 𝔶₁), let 𝔷 be as in [[def:tl5-hfg-graded]], 𝔨₁ as in [[lem:tl5-hf-sobolev]] and 𝔨₂ as in
[[lem:tl5-hf-linfty]], put 𝔲₀^♯ := 𝔲₀ + 8𝔲₀⁻¹ |D̂∂_γ|², and, with the suprema over Σ₁(a, b),

    C_S^f(p)² := C_(E,0)(𝔶)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ min(𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁,
                  max(6μ 𝔷² 𝔨₂ 𝔲₀^♯ + 2𝔲₀⁻¹ 𝔨₁, 7μ 𝔷² 𝔨₂ 𝔲₀^♯)),
    C_S^h(p)² := C_(E,0)(𝔶^h)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ min(𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁,
                  6μ 𝔷² 𝔨₂ 𝔲₀^♯ + max(2𝔲₀⁻¹ 𝔨₁, 𝔶₀^h μ² (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁))),                  {#eq:tl5-hff-cs}

and let C_(0,0)^h be the constant C_(0,0) of the lemma in use, in its form with index l, formed with 𝔶^h in place of
(𝔶₀, 𝔶₁). Then the zeroth-order step of the lemma in use gives its bound of Ψ_B(p) for 1 ≤ |B| ≤ N − 2, and its bound of
(Σ_(B∈𝔚) |Ψ_B(p)|²)^(1/2) for a family 𝔚 of n distinct such words of one length, with C_S^f in place of C_S^l and the
same parts with η₀; and it gives its bound of h(p) with C_S^h and C_(0,0)^h in place of C_S^l and C_(0,0). Moreover
C_S^f ≤ C_S^l, and for 𝔶₀^h = 𝔶₀, C_S^h ≤ C_S^l and C_(0,0)^h = C_(0,0).

*Proof.* In the proof of [[lem:tl5-hfp-abs]] (c), in the form that the proof of [[thm:tl5-hfe]] gives it with
[[lem:tl5-hfe-face]] (b) and 𝔲 = 𝔲₀, the step for a word B multiplies by μ^(|B|+2) the inequality of
[[lem:tl5-hfe-face]] (b) for A := Ψ_B, and for a family it adds these over B ∈ 𝔚. As ℒ^J Ψ_B = Ψ_(JB), the face term of
that inequality is, by its proof, Σ_(|J|≤2) 𝔶_(|J|) ∫_Σ 𝔳₀⁴ R⁻³ (𝔲₀^♯ |Ψ_(JB)|² + 2𝔲₀⁻¹ |D̂_(∂_γ)Ψ_(JB)|²) dμ dτ₂/(1 −
κκ′), Σ := Σ₁(a, b). There, at each point, |D̂_(∂_γ)Ψ_(JB)|² ≤ 𝔨₁ (e_o + κ′ e_i)[Ψ_(JB)] and |Ψ_(JB)|² ≤ (e_o + κ′
e_i)[Ψ_(JB)]/(2Ω̂² z̲), and (e_o + κ′ e_i)/(1 − κκ′) = ε₁; with 𝔶_(|J|) μ^(|B|+2) ≤ μ^(|JB|) every word JB, these words
being distinct, carries at most 𝔳₀⁴ R⁻³ (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁) times μ^(|JB|) ε₁[Ψ_(JB)] dμ dτ₂, which gives C_S^l,
as Σ_W μ^(|W|) ∫_Σ ε₁[Ψ_W] dμ dτ₂ ≤ ℰ_g(p) for distinct words W of length at most N. Call this the first way of bounding
the parts with |Ψ_(JB)|².

Let 1 ≤ |B| ≤ N − 2. Each word JB is ZC with Z its first letter: Z is the first letter of J and C = J′B if J = ZJ′, and
Z ∈ Γ and C = B′ if J = ∅ and B = ZB′. As in the proof of (∗) of [[lem:tl5-hfg-products]], [[eq:tl5-hf-lie]] and the
Cauchy–Schwarz inequality give |Ψ_(ZC)|² ≤ 𝔷² (|D̂Ψ_C|² + |Ψ_C|²), and |D̂Ψ_C|² + |Ψ_C|² ≤ 𝔨₂ (e_o + κ′ e_i)[Ψ_C], as in
the proof of [[lem:tl5-hf-linfty]]. As 𝔶_k ≤ μ^(k−2) and 𝔶₂ = 1, 𝔶_(|J|) μ^(|B|+2) ≤ μ μ^(|C|) in each case. Bound the
part with |Ψ_(JB)|² in this way for every pair (J, B), the second way, and the part with |D̂_(∂_γ)Ψ_(JB)|² as before.
Then the word JB with |J| = 2 carries 2𝔲₀⁻¹ 𝔨₁ at most; the word JB with |J| ≤ 1 carries at most 2𝔲₀⁻¹ 𝔨₁ + 6μ 𝔷² 𝔨₂
𝔲₀^♯, the words ZJB with Z a rotation being six; and the word B′ with |B′| = |B| − 1 carries at most 7μ 𝔷² 𝔨₂ 𝔲₀^♯, the
words ZB′ in 𝔚 being at most seven, as Z ∈ Γ, and one for a single word; each times 𝔳₀⁴ R⁻³ and μ^(|W|) ε₁[Ψ_W] dμ dτ₂
for the word W. These three classes have the lengths |B| + 2, |B| + 1 or |B|, and |B| − 1, so they are disjoint, and in
each the words are distinct, as the B ∈ 𝔚 have one length. At each point of the face use, for all the pairs at once, the
way for which the largest of the coefficients is the smaller; the set of the points where the first way is used is
closed, as all the functions are continuous. Every word then carries at most 𝔳₀⁴ R⁻³ times the minimum in C_S^f(p)², so
the face term, times μ^(|B|+2), is at most C_S^f(p)² ℰ_g(p) divided by C_(E,0)(𝔶)² 𝔴₀(p)⁴. The terms on S_a are those of
the proof of [[lem:tl5-hfp-abs]] (c), and the rest of the step gives its bounds with C_S^f in place of C_S^l.

For the word h, B = ∅, apply the step with the weights 𝔶^h: [[lem:tl5-hfe-face]] (b) holds with them and C_(E,0)(𝔶^h),
its proof using [[lem:tl5-hfd-leaf]], which holds for all weights, and the step holds with them, as 𝔶₀^h μ² ≤ 1. The
words of the step are the J with |J| ≤ 2. For J = ZJ′ put C := J′; then 𝔶_(|J|) μ² ≤ μ μ^(|J′|), as above. The word h
itself has no shorter word, and its part with |h|² is bounded as before, with the weight 𝔶₀^h μ². In the second way the
word J with |J| = 2 carries at most 2𝔲₀⁻¹ 𝔨₁, the word J with |J| = 1 at most 2𝔲₀⁻¹ 𝔨₁ + 6μ 𝔷² 𝔨₂ 𝔲₀^♯, and h at most
𝔶₀^h μ² (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁) + 6μ (𝔶₁ μ) 𝔷² 𝔨₂ 𝔲₀^♯, with 𝔶₁ μ ≤ 1; each of these is at most the second entry of
the minimum in C_S^h(p)². In the first way every word carries at most 𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁, as 𝔶₁ μ ≤ 1 and 𝔶₀^h μ²
≤ 1, each times 𝔳₀⁴ R⁻³. Choosing at each point as above gives C_S^h, and the terms on S_a, formed with 𝔶^h by the proof
of [[lem:tl5-hfp-abs]] (c), give C_(0,0)^h.

Finally, the first entry of the minimum in C_S^f(p)² is the function whose supremum gives C_S^l(p)², so C_S^f ≤ C_S^l.
For 𝔶₀^h = 𝔶₀, C_(E,0)(𝔶^h) = C_(E,0)(𝔶), so C_S^h ≤ C_S^l for the same reason, and C_(0,0)^h = C_(0,0). ∎

**Definition {#def:tl5-hff-constants}** (The constants with index f.) In the setting of [[def:tl5-hfc-constants]], let
𝔶₀^h ∈ (0, μ⁻²], let C_S^f, C_S^h and C_(0,0)^h be as in [[lem:tl5-hff-zero]], and put C_P⁰ := max(𝔤₁ C_S^h, C_S^f) and
C_(P,0)⁰ := max(𝔤₁ C_(0,0)^h, C_(0,0)). The constants with index f are the constants with index c formed with C_P⁰ and
C_(P,0)⁰ in place of 𝔤₁ C_S^l and 𝔤₁ C_(0,0) at the sites of [[lem:tl5-hfc-h]] and in 𝔎 and 𝔎₀, with C_S^h and C_(0,0)^h
in place of C_S^p and C_(0,0)^p in 𝔨_rec^p and 𝔨_rec^(0,p), with C_S^h for b = 0 and C_S^f for b ≥ 1 in place of C_S^p
in 𝔐_p^(m), and with max(C_(0,0)^h, C_(0,0)) in place of C_(0,0)^p in the parts with η₀ of the step of
[[lem:tl5-hfp-low]], each in its form with index l, and in every constant formed from these. Fix one of the two routes
below for the parts with ϱ, the second only for N ≥ 6 with option (b) of [[def:tl5-hft-constants]]:

    route (𝔰):  ε^f := ε^l,   𝔯_ϱ^f := 0;
    route (𝔯):  ε^f := 𝒮[s_N[2R̂ic] + μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_(P,0)⁰ η₀ ϱ],
                𝔯_ϱ^f := ϱ 𝒮[μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰ e^(φ/2)],                          {#eq:tl5-hff-routes}

with 𝒮 of [[eq:tl5-hf-source]] for a = u*, b = v* and the functions of the point evaluated at it. Let S_F^f, S_M^f and
ε_M^f be S_F^c, S_M^c and ε_M^c formed with the constants with index f, let 𝔯^f be 𝔯^c so formed plus 𝔯_ϱ^f, and put

    η_f := 1 − max(ϑ₁, ϑ₂) − 𝔯^f,      A_f := η_f^(−1/2) δ_w + η_f⁻¹ (ε^f + ε_M^f),      B_f := η_f⁻¹ (S_F^f + S_M^f).

For a number 𝔜 ≥ 0 let 𝔰_*^f[𝔜] be 𝔰_*^c[𝔜] formed with the constants with index f, and, when 4A_f B_f < 1, put

    Y_f := 2A_f/(1 + (1 − 4A_f B_f)^(1/2)),      𝔰_*^f := 𝔰_*^f[Y_f].                            {#eq:tl5-hff-constants}

**Theorem {#thm:tl5-hff}** (Existence with the parts with ϱ through the bound at a point and the zeroth order through
the shorter words.) In the setting of [[thm:tl5-hfc]], with 𝔶₀^h ∈ (0, μ⁻²], one of the routes of [[eq:tl5-hff-routes]]
and the constants with index f of [[def:tl5-hff-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 −
ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_f > 0, the closing condition

    4 A_f B_f = 4 η_f^(−3/2) (δ_w + η_f^(−1/2) (ε^f + ε_M^f)) (S_F^f + S_M^f) < 1,                 {#eq:tl5-hff-closing}

and 𝔰_*^f < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_f for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with 𝔰_*^f in place of 𝔰_*. For
𝔶₀^h = 𝔶₀ and route (𝔰) each constant with index f is at most the one with index c it replaces, ε^f = ε^c, η_f ≥ η_c,
A_f ≤ A_c, B_f ≤ B_c, Y_f ≤ Y_c and 𝔰_*^f ≤ 𝔰_*^c; so the hypotheses of [[thm:tl5-hfc]] imply these.

*Proof.* The proof of [[thm:tl5-hfc]] applies with the constants with index f, ε^f, 𝔯^f, η_f, A_f, B_f, Y_f, 𝔰_*^f[𝔜]
and [[eq:tl5-hff-closing]] in place of those with index c, with two changes.

*The zeroth order.* By [[lem:tl5-hff-zero]], the zeroth-order step of the lemma in use gives its bounds of h(p), of
Ψ_B(p) with 1 ≤ |B| ≤ N − 2 and of the families of words of one length with C_S^h and C_(0,0)^h for h and with C_S^f and
C_(0,0) for the others. With [[lem:tl5-hfc-h]], μ |H(p)| ≤ 𝔤₁ μ |h(p)|, so 𝔰_P⁰(p) ≤ C_P⁰(p) ℰ_g(p)^(1/2) + C_(P,0)⁰(p)
η₀(p). The bounds at a point that the proof of [[thm:tl5-hfc]] uses take the zeroth-order step only through these
bounds: through the quantities of 𝔰_P⁰, in the entries of [[lem:tl5-hfc-h]] and in 𝔎 and 𝔎₀, which Step 3 of the proof
of [[prop:tl5-hfs-bootstrap]] forms from the bound of 𝔰_P⁰; through μ |h(p)| in [[lem:tl5-hfp-rec]]; and through the
families of the words of each length in [[lem:tl5-hfp-low]]. Each is formed from the bounds of the step in the same way
for all values of their constants, so they hold with the constants with index f.

*The parts with ϱ.* With route (𝔰) the proof of [[thm:tl5-hfc]] bounds them as written, with ε^c = ε^f. With route (𝔯),
after Step 1, 𝔰 ≤ 𝔰₁^v on D^κ_s, so [[lem:tl5-hff-rho]] applies at every point of D^κ_s, with ϱ(p) ≤ ϱ. In Step 2 the
terms with ϱ of the family of level j are bounded as in the proof of [[thm:tl5-hfe]], through Step 2 of the proof of
[[prop:tl5-hft-bootstrap]] with 𝔠^ϱ and the replacements, now with μ⁻¹ 𝔰_P⁰ in place of 𝔰 by [[lem:tl5-hff-rho]]. With
the weights μ^|I| they contribute to the bulk at most 2Ω̂² μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z 𝔰_P⁰ ϱ (√e_o + √c √e_i) at
each point, where that proof has 𝔰₁^v in place of μ⁻¹ 𝔰_P⁰. As ℰ_g(p) ≤ e^(φ(p)) Y_s² at every point p of D^κ_s, the
bound of 𝔰_P⁰ gives 𝔰_P⁰ ≤ C_P⁰ e^(φ/2) Y_s + C_(P,0)⁰ η₀ there. So this part together with the forcing term is at most
2Ω̂² s^f (√e_o + √c √e_i), with s^f := s_N[2R̂ic] + s₀^f + Y_s s₁^f, s₀^f := μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_(P,0)⁰ η₀
ϱ and s₁^f := μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰ e^(φ/2) ϱ. As in the proof of [[prop:tl5-hf-linear]], its integral
with the weight e^(−φ) over Q(a′, b′) is at most Y_s 𝒮[s^f]; and 𝒮 is subadditive and positively homogeneous, so Y_s
𝒮[s^f] ≤ Y_s ε^f + 𝔯_ϱ^f Y_s². The inequality of Step 3 then holds with ε^f in place of ε^c and with 𝔯^f in place of
𝔯^c, and gives (H1) with A_f and B_f.

The rest of the proof of [[thm:tl5-hfc]], with A_f, B_f, Y_f and 𝔰_*^f[𝔜], holds as written. For the last claim, let
𝔶₀^h = 𝔶₀ and take route (𝔰). By [[lem:tl5-hff-zero]], C_S^h ≤ C_S^l, C_S^f ≤ C_S^l and C_(0,0)^h = C_(0,0), so C_P⁰ ≤
𝔤₁ C_S^l and C_(P,0)⁰ = 𝔤₁ C_(0,0), as 𝔤₁ ≥ 1; every constant with index c is nondecreasing in these numbers, so each
constant with index f is at most the one it replaces; and 𝔯_ϱ^f = 0 and ε^f = ε^c. Then η_f ≥ η_c, A_f ≤ A_c, B_f ≤ B_c
and 4A_f B_f ≤ 4A_c B_c. The smaller root 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, so Y_f ≤ Y_c, and
𝔰_*^f ≤ 𝔰_*^f[Y_c] ≤ 𝔰_*^c[Y_c] = 𝔰_*^c, as 𝔰_*^c[𝔜] is nondecreasing in 𝔜 and in the constants. ∎

**Remark {#rem:tl5-hff-what}** (What changes.) In the products with a factor at a point, the part with ϱ of a monomial
is the residual of the recovery of its factor D̂²Ψ_C times its factor Φ₁, which is H, h or a Ψ_B. The bound |Φ₁| ≤ 𝔰 ≤
𝔰₁^v makes it a forcing term with the factor 𝔰₁^v ϱ, which enters ε, and so A, the closing condition and the term of 𝔰_*
with A, which carries μ^(−N/2). In route (𝔯), Φ₁ is bounded as a quantity of 𝔰_P⁰, at the cost of a factor μ⁻¹, the
weights leaving μ^(−3/2) μ^(b/2) in place of μ^(−1/2) μ^(b/2), and 𝔰_P⁰ by its bound at the point, which comes from the
energies and from η₀ alone. The factor e^(φ/2) of that bound is taken up by the weight e^(−φ) of 𝒮, as e^(φ/2) is in
S_F, so the part gives the term 𝔯_ϱ^f Y_s², which enters 𝔯, and a part of ε with ϱ η₀: in the coefficient of ϱ in ε, μ⁻¹
C_(P,0)⁰ η₀ takes the place of 𝔰₁^v, and 𝔯_ϱ^f carries μ⁻¹ C_P⁰ where ε^l carries 𝔰₁^v. The two routes put the part in
different places, ε against 𝔯, so the theorem takes either; it takes route (𝔯) only for N ≥ 6 with option (b), where the
bounds of the second derivatives carry the weight μ^(−(|C|+1)/2) on their parts with ϱ. In the zeroth-order step, the
part |Ψ_(JB)|² of the density of a word JB is bounded through the energy of JB itself, with the weight 𝔶_(|J|)
μ^(|B|+2), which is μ^(|JB|) at the largest weights 𝔶_k = μ^(k−2), so its coefficient 1/(2Ω̂² z̲) has no factor μ.
Through the shorter word C with JB = ZC the weight leaves the factor μ, and the coefficient becomes 6μ 𝔷² 𝔨₂, or at most
7μ 𝔷² 𝔨₂ for the words B′ that the first letters of a family share; the part with |D̂_(∂_γ)Ψ_(JB)|² stays with its own
word. At each point the smaller bound is taken, so C_S^f ≤ C_S^l for all weights. The word h has no shorter word, and
its own part keeps the coefficient 1/(2Ω̂² z̲) with the factor 𝔶₀^h μ²; a weight 𝔶₀^h < 𝔶₀ lowers it, at the cost of
C_(E,0)(𝔶^h) ≥ C_(E,0)(𝔶), whose square has the term 1/(2π² 𝔶₀^h) with j₁ = j₂ = 0. The entry C_P⁰ that bounds μ |H| and
the Ψ_B is the larger of 𝔤₁ C_S^h and C_S^f, so it falls only if both do, which is why the step for h takes its own
weight. The counts, the recovery constants, the first-order constants, the weights 𝔲₀, 𝔲₁, 𝔲_M, the thresholds 𝔰₀ and
𝔰₁^v and the rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hff]] are
established in this paper for no background at 10 l5.
