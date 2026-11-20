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

### Continuation beyond the seed {#sec:tl5-beyond}

The following lemma reduces existence beyond the seed to an a priori estimate on the whole region and a closing
condition; the local existence, uniqueness and continuation of the characteristic problem in the gauge that it uses are
[[thm:tl5-cip]].

**Lemma {#lem:tl5-continuation}** (Existence by continuity.) Let u* ∈ (−10, 0) and v* > 1/2, and let smooth
characteristic data in the gauge ([[def:tl5-cip-data]]) be given on N₀ := {v = 1/2, −10 ≤ u ≤ u*} × S³ and
N₁ := {u = −10, 1/2 ≤ v ≤ v*} × S³, satisfying the characteristic constraints [[eq:tl5-cip-constraints]]. Put
D := {−10 ≤ u ≤ u*, 1/2 ≤ v ≤ v*} × S³ and D_s := D ∩ {v ≤ s}, and call a solution on D_s a smooth T²-invariant
vacuum metric of the class on D_s, in the gauge, that induces the data. Suppose that to every solution g on a D_s and
every σ ∈ [1/2, s] a number y_σ(g) ≥ 0 is assigned, depending only on the restriction of g to D_σ and continuous in σ,
and that there are A, B > 0 such that:

(H1) y_s(g) ≤ A + B y_s(g)² for every solution g on every D_s;

(H2) for every k ≥ 0 there is C_k such that every solution g on a D_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s] has its
components and their derivatives of order at most k, and the components of g⁻¹, bounded by C_k on D_s, in a fixed
finite atlas of [−10, u*] × [1/2, v*] × S³;

(H3) 4AB < 1, and y_(1/2)(g) ≤ A for every solution g.

Then there is a solution g on D, and y_σ(g) ≤ 2A for every σ ∈ [1/2, v*].

The proof uses three properties of the characteristic problem in the gauge, for the data of the lemma: (F1) there are
s ∈ (1/2, v*] and a solution on D_s; (F2) two solutions on the same D_s coincide; (F3) a solution on D_s with s < v* is
the restriction of a solution on D_(s′) for some s′ ∈ (s, v*]. For smooth data satisfying the constraints these are
[[thm:tl5-cip]]. Its proof does not use the uniqueness of a maximal development, which [CP12, Section 4.3, p. 16] and
the proof of [CCTW16, Theorem 5.3, p. 55] leave aside: [[thm:std-ctg-neighbourhood]] is used only for the existence of
one development, on which double-null coordinates cover a region D_s ([[lem:tl5-cip-chart]]), uniqueness is proved in
the gauge, for vacuum metrics in double-null form on the regions D_s, axes included ([[prop:tl5-cip-unique]]), and the
symmetry of the class follows from the uniqueness. For the problem of [[def:tl5-problem]] with u* < u₀ the lemma applies
stage by stage: to the data of the first stage of [[cor:tl5-cip-staged]] (a), with v* ≤ 7/2, and, given a solution on
the whole first stage, to the data of its second stage, translated by v ↦ v − 3 ([[cor:tl5-cip-staged]] (b)); with the
seed, the solutions it gives form a solution of [[def:tl5-problem]] of class C³ ([[cor:tl5-cip-staged]] (c)). No proof
in this paper uses the lemma.

*Proof.* First, if 4AB < 1 and y ≥ 0 satisfies y ≤ A + By², then y ∉ (2A, 1/(2B)), and if moreover y ≤ 2A then
y ≤ A + 4A²B < 2A. Indeed q(y) := By² − y + A is convex with q(2A) = A(4AB − 1) < 0 and q(1/(2B)) =
(4AB − 1)/(4B) < 0, so q < 0 on [2A, 1/(2B)], an interval since 2A < 1/(2B); and 4A²B < A.

Let I be the set of s ∈ (1/2, v*] for which there is a solution g on D_s with y_σ(g) ≤ 2A for all σ ∈ [1/2, s]. If
s ∈ I and 1/2 < s′ < s, then s′ ∈ I, by restriction.

I is not empty. By (F1) of [[thm:tl5-cip]] there is a solution g on some D_(s₁); y_(1/2)(g) ≤ A < 2A by (H3), and
y_σ(g) is continuous in σ, so y_σ(g) ≤ 2A on [1/2, s₂] for some s₂ ∈ (1/2, s₁], and s₂ ∈ I.

I is open in (1/2, v*]. Let s ∈ I with s < v*, and g the solution on D_s. For σ ∈ (1/2, s] the restriction of g to D_σ
is a solution on D_σ, so (H1) and y_σ(g) ≤ 2A give y_σ(g) ≤ A + 4A²B < 2A; at σ = 1/2, y_(1/2)(g) ≤ A by (H3). By
(F3) of [[thm:tl5-cip]], g is the restriction of a solution g′ on some D_(s′), s′ > s, and since y_σ(g′) is continuous
in σ and y_s(g′) = y_s(g) < 2A, y_σ(g′) ≤ 2A on [1/2, s″] for some s″ ∈ (s, s′]. So s″ ∈ I.

I is closed. Let s_n ∈ I increase to s̄ ≤ v*, with solutions g_n on D_(s_n). By (F2) of [[thm:tl5-cip]], g_m
restricted to D_(s_n) is g_n for m ≥ n, so the g_n define a smooth metric g on D ∩ {v < s̄}, with y_σ(g) ≤ 2A for
σ < s̄. By (H2) the
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

**Remark {#rem:tl5-beyond}** (Why existence beyond the seed is claimed only on a strip.) [[lem:tl5-continuation]]
concerns smooth data, for which (F1)–(F3) hold ([[thm:tl5-cip]]). The data of [[def:tl5-problem]] are not smooth: env is
C³ and not C⁴ at v = 1/2 and v = 7/2 ([[rem:envelope-regularity]]), and so are the fields P and Q on N there. But for
u* < u₀ the problem splits into the seed and two stages with smooth data, whose solutions glue in class C³
([[cor:tl5-cip-staged]]); so the regularity of the data is no obstruction: (F1) gives the strip of [[thm:ten-l5]] (b),
and the lemma applies stage by stage. What is missing for a given region D is (H1)–(H3). (H1) is an estimate on all of
D, axes included. An estimate for the linearised problem on a truncated domain of dependence that avoids the axes would
not give (H1): no such domain contains a region of the form D_s, since D_s contains the axes. The residual bounds of
[[sec:tl5-residuals]] hold at points and on boxes of the region Π of [[eq:tl5-region]], which is not of the form D_s,
and are not bounds of a norm over a region D_s. So (H1)–(H3) are established in this paper for no region D with
v* > 1/2, and no existence is claimed beyond the strip of [[thm:ten-l5]] (b), whose width is not estimated.

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
