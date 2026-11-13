# Part. Explicit constants {#part:constants}

## Explicit resolvent bounds on five-dimensional Tangherlini {#ch:resolvent-bounds}

The stability theory obtains its inverse bounds for the spectral families by Fredholm, compactness and contradiction
arguments, which give no number. This chapter makes the first of them explicit for one operator: the scalar wave
operator □ = δd on five-dimensional Schwarzschild–Tangherlini, the operator of [[prop:iii-d-6-2]], whose invertibility
for Im σ ≥ 0, σ ≠ 0 rests harmonic by harmonic on an ordinary differential equation. For each harmonic the resolvent,
cut off to an interval about the photon sphere, is bounded with explicit constants: off the real axis by self-adjointness
([[lem:rb-off-axis]]); on the real axis first with a constant exponential in the harmonic's degree
([[prop:resolvent-outgoing]]), then uniformly in the degree where the potential barrier covers the interval
([[prop:rb-coercive]], [[cor:rb-closed-form]]) and where the frequency lies above the barrier
([[prop:resolvent-above-barrier]]); and then for every harmonic and every real frequency by multiplier identities of
Morawetz type ([[lem:morawetz-identity]]), with algebraic multipliers whose weights are positive by exact polynomial
inequalities ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]]). The same identities give one derivative
([[cor:morawetz-one-derivative]]), extend off the real axis ([[lem:morawetz-complex]]), apply to every master operator of
the 1-form wave operator and of the linearised Einstein operator ([[prop:morawetz-master-potentials]]), and, with
multipliers adapted to the frequency, give a bound uniform in the degree on the band 3 ≤ |σ| ≤ 384 ([[thm:band]],
[[cor:band-one-derivative]]).

The chapter then states the elementary operator facts by which bounds of this kind enter an inverse bound in the
function spaces of the stability theory: a parametrix gives a Fredholm estimate with an explicit constant
([[lem:rb-parametrix]]), absorption and interpolation are explicit ([[lem:rb-absorption]], [[lem:rb-interpolation]]),
the rotation group splits the inverse into blocks ([[lem:rb-schur]]), and a complex absorbing potential reduces the
global inverse to a cut-off one ([[lem:rb-gluing]], [[lem:rb-absorbed]]). It ends with the scalar-type blocks of the
linearised gauge-fixed Einstein operator at zero energy, and with an obstruction to a good constant for them that comes
from the weight ([[lem:rb-quasimode]]).

### The radial problem {#sec:rb-radial}

Let m > 0, f := 1 − m/r² and r_h := m^(1/2). The tortoise coordinate r_* of [[prop:np-10-16]] (v) has dr_*/dr = 1/f,
r_* → −∞ as r → r_h and r_* = r + O(r⁻¹) as r → ∞; we write u′ := du/dr_*. For S ∈ 𝒮_l, κ := l(l + 2) (so that
−Δ_(𝕊³)S = κS), and a function u of r_*, [[prop:np-10-16]] (ii) gives, with □ = δd on functions,

    −fr^(3/2)e^(iσt)S⁻¹ □(r^(−3/2)u S e^(−iσt)) = u″ + σ²u − V_l u,
    V_l := f((κ + 3/4)/r² + 9m/(4r⁴)),                                                                {#eq:rb-potential}

since f(fu_r)_r = u″. So □(r^(−3/2)uSe^(−iσt)) = gSe^(−iσt), with g a function of r, is the equation

    −u″ + V_l u − σ²u = F,     F := fr^(3/2)g.                                                         {#eq:rb-radial}

V_l > 0 on r > r_h. As r_* → −∞, f and V_l decay like e^(2r_*/r_h), since f′(r_h)/2 = 1/r_h; as r_* → ∞,
V_l = (κ + 3/4)r_*⁻² + O(r_*⁻³). The integral of V_l in r_* is explicit:

    I_l := ∫_ℝ V_l dr_* = ∫_(r_h)^∞ ((κ + 3/4)/r² + 9m/(4r⁴)) dr = (κ + 3/2)/r_h.      {#eq:rb-barrier-integral}

*Solutions at the ends.* Let σ ∈ ℂ ∖ {0} with Im σ ≥ 0. V_l is integrable in r_* at both ends, so the Volterra
equations u(x) = e^(−iσx) + ∫_(−∞)^x σ⁻¹ sin(σ(x − x′))V_l(x′)u(x′) dx′ and
u(x) = e^(iσx) − ∫_x^∞ σ⁻¹ sin(σ(x − x′))V_l(x′)u(x′) dx′ have unique solutions by iteration, as in the proof of
[[prop:iii-d-6-2]]. They define the solutions u_h and u_∞ of −u″ + (V_l − σ²)u = 0 with

    u_h e^(iσr_*) → 1,  u_h′ + iσu_h → 0 as r_* → −∞;     u_∞ e^(−iσr_*) → 1,  u_∞′ − iσu_∞ → 0 as r_* → ∞,

the second limit in each case from the differentiated Volterra equation, whose remainder is bounded by the tail of
∫|V_l|. A solution with u′ + iσu → 0 at −∞ is a multiple of u_h, and one with u′ − iσu → 0 at ∞ a multiple of u_∞: the
other solution at each end behaves like e^(±iσr_*), for which this quantity is 2iσe^(±iσr_*)(1 + o(1)) and does not
tend to 0. In the spacetime, e^(−iσt)u_h = e^(−iσ(t + r_*))(1 + o(1)) is the behaviour of a field smooth across
the future horizon, and e^(−iσt)u_∞ = e^(−iσ(t − r_*))(1 + o(1)) that of an outgoing one: these are the classes of the
proof of [[prop:iii-d-6-2]].

*The resolvent.* H_l := −∂²_(r_*) + V_l, with domain H²(ℝ), is self-adjoint and nonnegative on L²(ℝ, dr_*), V_l being
bounded and nonnegative. For Im σ > 0, R_l(σ) := (H_l − σ²)⁻¹; then σ² ∉ [0, ∞). For real σ ≠ 0, R_l(σ) is the
outgoing resolvent of [[prop:resolvent-outgoing]]. Throughout, ‖·‖ is the norm of L²(ℝ, dr_*), I ⊂ ℝ an r_*-interval,
‖·‖_I the norm of L²(I, dr_*) and χ_I multiplication by the indicator function of I; for m = 1 we fix
I := {6/5 ≤ r ≤ 4}, whose length in r_* is Λ < 3.7436 ([[sec:morawetz-identity]]).

### Off the real axis {#sec:rb-off-axis}

**Lemma {#lem:rb-off-axis}** (Off the real axis.) For Im σ > 0 and every l,

    ‖R_l(σ)‖_(L²→L²) ≤ 1/dist(σ², [0, ∞)),

which is 1/(2|Re σ| Im σ) when |Re σ| ≥ Im σ and 1/|σ|² when |Re σ| < Im σ.

*Proof.* H_l ≥ 0 is self-adjoint, so spec H_l ⊂ [0, ∞) and ‖(H_l − σ²)⁻¹‖ = 1/dist(σ², spec H_l) ≤
1/dist(σ², [0, ∞)). With σ² = (Re σ)² − (Im σ)² + 2i Re σ Im σ, the distance is |Im σ²| = 2|Re σ| Im σ if
Re σ² ≥ 0, that is |Re σ| ≥ Im σ, and |σ²| otherwise. ∎

This bound is uniform in l and degenerates as Im σ → 0, where the content of [[prop:iii-d-6-2]] lies.

### The flux and the outgoing resolvent {#sec:rb-flux}

From here on σ is real and nonzero.

**Lemma {#lem:rb-flux}** (The flux.) Write u_h = A e^(−iσr_*) + B e^(iσr_*) + o(1) as r_* → ∞. Then
|A|² = 1 + |B|², and the Wronskian 𝒲 := u_h u_∞′ − u_h′ u_∞ equals 2iσA. In particular |𝒲| ≥ 2|σ|.

*Proof.* V_l is real, so Im(ūu′) is constant for every solution u. For u_h it is −σ at −∞, and −σ|A|² + σ|B|² at +∞,
the cross terms being real; so |A|² = 1 + |B|². 𝒲 is constant; at +∞, with u_∞ = e^(iσr_*)(1 + o(1)) and
u_∞′ = iσu_∞ + o(1),
𝒲 = (Ae^(−iσr_*) + Be^(iσr_*))iσe^(iσr_*) − (−iσAe^(−iσr_*) + iσBe^(iσr_*))e^(iσr_*) + o(1) = 2iσA. ∎

**Lemma {#lem:rb-growth}** (Growth through the barrier.) For a solution u of −u″ + (V_l − σ²)u = 0 put
E := |u′|² + σ²|u|². Then |E′| ≤ (V_l/|σ|)E. Hence

    |u_∞(x)|² ≤ 2 exp(|σ|⁻¹ ∫_x^∞ V_l dr_*),     |u_h(x)|² ≤ 2 exp(|σ|⁻¹ ∫_(−∞)^x V_l dr_*).

*Proof.* E′ = 2Re(ū′u″) + 2σ²Re(ūu′) = 2(V_l − σ²)Re(ū′u) + 2σ²Re(ūu′) = 2V_l Re(ū′u), and
2|ū′u| ≤ |u′|²/|σ| + |σ||u|² = E/|σ|. E tends to 2σ² at the end where u is normalised (u_∞ at +∞, u_h at −∞), so
Gronwall's inequality from that end gives E ≤ 2σ² exp(|σ|⁻¹∫V_l) over the interval between the end and x, and
σ²|u|² ≤ E. ∎

**Proposition {#prop:resolvent-outgoing}** (The outgoing resolvent.) Let σ be real and nonzero, and F ∈ L²(ℝ) vanish
outside a bounded set.

(a) There is exactly one solution u, with u and u′ locally absolutely continuous, of −u″ + (V_l − σ²)u = F almost
everywhere, that is a multiple of u_h near −∞ and of u_∞ near +∞. We write u =: R_l(σ)F. It satisfies
u − c_±e^(±iσr_*) → 0 and u′ ∓ iσu → 0 as r_* → ±∞, for constants c_±, and

    u(x) = ∫ k_l(x, x′) F(x′) dx′,     k_l(x, x′) := −u_h(min(x, x′)) u_∞(max(x, x′))/𝒲.                {#eq:rb-kernel}

(b) |k_l(x, x′)| ≤ |σ|⁻¹ exp(I_l/(2|σ|)), with I_l of [[eq:rb-barrier-integral]]. So for an r_*-interval J of length
Λ_J, ‖χ_J R_l(σ) χ_J‖ ≤ (Λ_J/|σ|) exp(I_l/(2|σ|)).

*Proof.* (a) 𝒲 ≠ 0 by [[lem:rb-flux]]. Define u by [[eq:rb-kernel]], that is
u(x) = −𝒲⁻¹(u_∞(x)∫_(−∞)^x u_h F + u_h(x)∫_x^∞ u_∞ F). The integrals are finite, F having bounded support, and u is
locally absolutely continuous with u′ = −𝒲⁻¹(u_∞′(x)∫_(−∞)^x u_h F + u_h′(x)∫_x^∞ u_∞ F), the two terms from the
variable limits cancelling; u′ is locally absolutely continuous, and almost everywhere
u″ = (V_l − σ²)u − 𝒲⁻¹(u_∞′u_h − u_h′u_∞)F = (V_l − σ²)u − F. Left of the support of F, u is the multiple
−𝒲⁻¹(∫u_∞F)u_h of u_h, and right of it the multiple −𝒲⁻¹(∫u_hF)u_∞ of u_∞; this gives the limits, with
c_− and c_+ these coefficients. If two such solutions exist, their difference solves the homogeneous equation and is a
multiple of u_h and of u_∞, so it vanishes since 𝒲 ≠ 0.

(b) For x ≤ x′, [[lem:rb-growth]] gives
|u_h(x)||u_∞(x′)| ≤ 2 exp((2|σ|)⁻¹(∫_(−∞)^x V_l + ∫_(x′)^∞ V_l)) ≤ 2 exp(I_l/(2|σ|)), as V_l ≥ 0, and |𝒲| ≥ 2|σ|. A
kernel bounded by K on J × J defines an operator on L²(J) of norm at most its Hilbert–Schmidt norm, KΛ_J. ∎

This is the injectivity of [[prop:iii-d-6-2]] at real σ, harmonic by harmonic, with a constant obtained by inequalities
alone. The constant grows like exp(κ/(2|σ|r_h)): the bound |𝒲| ≥ 2|σ| ignores that 𝒲 = 2iσA carries the same
tunnelling factor through the barrier as the solutions.

### Uniformly in the harmonic where the barrier covers the interval {#sec:rb-uniform}

Let σ > 0 (σ < 0 follows by complex conjugation, as V_l is real: R_l(−σ)F = conj(R_l(σ) conj F)), let I = [α, β] be an
r_*-interval, and for a solution u of the homogeneous equation write V_σ := V_l − σ² and n := |u|², so that
½n′ = Re(ūu′) and ½n″ = |u′|² + V_σ n.

**Lemma {#lem:rb-energy}** (An energy monotone on each side of the barrier.) Put ℰ := |u′|² + (σ² − V_l)n. Then
ℰ′ = −V_l′n. So ℰ(u_h) ≤ 2σ² on every interval (−∞, x] on which V_l is nondecreasing, and ℰ(u_∞) ≤ 2σ² on every [x, ∞)
on which V_l is nonincreasing.

*Proof.* ℰ′ = 2Re(ū′u″) − V_l′n + (σ² − V_l)n′, and 2Re(ū′u″) = 2V_σ Re(ū′u) = −(σ² − V_l)n′. At the end where each is
normalised, u_h ~ e^(−iσr_*) and u_∞ ~ e^(iσr_*) together with their derivatives, and V_l → 0, so ℰ → 2σ² there; and ℰ
does not increase toward the barrier on the stated intervals. ∎

For m = 1 put g_l := (κ + 3/4)/r² + 9/(4r⁴), so that V_l = fg_l. Then −4g_l/r ≤ dg_l/dr ≤ −2g_l/r, and with
df/dr = 2/r³ and f = 1 − 1/r², dV_l/dr = g_l df/dr + f dg_l/dr satisfies

    (g_l/r³)(6 − 4r²) ≤ dV_l/dr ≤ (g_l/r³)(4 − 2r²):                                                  {#eq:rb-monotone}

V_l increases in r for r² < 3/2 and decreases for r² > 2, for every l.

**Lemma {#lem:rb-end-signs}** (The signs at the ends of I.) Let x_1 < α and x_2 > β be points with
V_σ(x_1) = V_σ(x_2) = 0 and V_σ ≥ 0 on [x_1, x_2], with V_l nondecreasing on (−∞, x_1] and nonincreasing on [x_2, ∞).
Put A_− := ∫_(x_1)^α V_σ^(1/2) dr_*, A_+ := ∫_β^(x_2) V_σ^(1/2) dr_*, and for x < x_1 and x′ > x_2 with V_l(x) < σ² and
V_l(x′) < σ²,

    D_−(x) := (2σ²/(σ² − V_l(x)))^(1/2) + √2σ(x_1 − x),     D_+(x′) := (2σ²/(σ² − V_l(x′)))^(1/2) + √2σ(x′ − x_2).

Then ½n′(α) ≥ 2σA_− − √2σD_−(x) for u = u_h, and ½n′(β) ≤ √2σD_+(x′) − 2σA_+ for u = u_∞.

*Proof.* We treat u_h; u_∞ is the mirror image, with flux Im(ū_∞u_∞′) = +σ. n > 0 everywhere, since the flux
Im(ūu′) = −σ is not zero. On (−∞, x_1], σ² − V_l ≥ 0, and ℰ ≤ 2σ² ([[lem:rb-energy]]) gives |u′|² ≤ 2σ² and
(σ² − V_l)n ≤ 2σ²; so n(x)^(1/2) ≤ (2σ²/(σ² − V_l(x)))^(1/2), and |(n^(1/2))′| = |Re(ūu′)|/n^(1/2) ≤ |u′| ≤ √2σ, so
n(x_1)^(1/2) ≤ D_−(x). As V_l(x_1) = σ², |u′(x_1)|² = ℰ(x_1) ≤ 2σ², and |½n′(x_1)| ≤ n^(1/2)|u′| ≤ √2σD_−(x). On
[x_1, α], |u′| ≥ |Im(ūu′)|/|u| = σn^(−1/2), so ½n″ ≥ σ²/n + V_σ n ≥ 2σV_σ^(1/2). Integrating from x_1 to α gives the
claim. ∎

**Proposition {#prop:rb-coercive}** (Where the barrier covers the interval.) Suppose c_I := min_I V_σ > 0,
½n′(u_h)(α) ≥ 0 and ½n′(u_∞)(β) ≤ 0; by [[lem:rb-end-signs]] the last two hold when A_− ≥ D_−(x)/√2 and
A_+ ≥ D_+(x′)/√2 for some x, x′. Then ‖χ_I R_l(σ) χ_I‖ ≤ 1/c_I.

*Proof.* For F ∈ L² vanishing off I, u := R_l(σ)F equals c_h u_h on (−∞, α] and c_∞u_∞ on [β, ∞)
([[prop:resolvent-outgoing]]). Pairing −u″ + V_σ u = F with ū over I and taking real parts,

    ∫_I(|u′|² + V_σ|u|²) = Re∫_I Fū + |c_∞|² ½n′(u_∞)(β) − |c_h|² ½n′(u_h)(α) ≤ ‖F‖‖u‖_I,

and the left side is at least c_I‖u‖_I². ∎

**Corollary {#cor:rb-closed-form}** (Closed form; m = 1, I = {6/5 ≤ r ≤ 4}.) Let a := κ + 3/4 and c := (15/16)a. If

(i) (15/256)a > σ² and (0.21/1.4641)a > σ²,

(ii) 0.32727(0.120523a − σ²)^(1/2) > (2 + 1.1248σ)/√2, and

(iii) c^(1/2) > 8σ and (√3/2)c^(1/2) log(c^(1/2)/(8σ)) > (2 + 0.79217(κ + 1)^(1/2))/√2,

then the hypotheses of [[prop:rb-coercive]] hold, and

    ‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)a − σ²) = (256/15)/(κ + 3/4 − (256/15)σ²).                {#eq:rb-closed-form}

Each of (i)–(iii), once true, stays true as l grows; so with l_0(σ) the least l at which they hold, the bound holds for
every l ≥ l_0(σ). It is asymptotically (256/15)/κ ≈ 17.07/κ.

*Proof.* (i) On I, y := 1/r² ∈ [1/16, 25/36] and f/r² = y(1 − y), whose least value there is at y = 1/16, namely 15/256.
As V_l ≥ af/r², min_I V_σ ≥ (15/256)a − σ² > 0. Also V_l(r = 1.1) ≥ af(1.1)/1.21 = (0.21/1.4641)a > σ², and V_l
increases on {r ≤ 1.1} by [[eq:rb-monotone]]; so the point x_1 of [[lem:rb-end-signs]], where V_l first reaches σ², lies
at r < 1.1. V_l has a single maximum ([[prop:resolvent-above-barrier]]), so V_l ≥ min(V_l(1.1), V_l(4)) > σ² on
[1.1, 4], and the point x_2 beyond the maximum where V_l = σ² lies at r > 4, where V_l decreases. (ii) On [1.1, 1.2],
1/f ≥ 1/f(1.2) = 3.2727 and V_l ≥ af(1.1)/1.44 = 0.120523a, so A_− ≥ 0.32727(0.120523a − σ²)^(1/2). Take x where
V_l = σ²/2. On {r ≤ 1.1}, d log V_l/dr_* = f d log V_l/dr ≥ (6 − 4r²)/r³ ≥ 1.16/1.331 = 0.87152 by [[eq:rb-monotone]], so
x_1 − x ≤ log 2/0.87152 < 0.79534 and D_−(x) ≤ 2 + 1.1248σ. (iii) For r ≥ 4, 1/f ≥ 1 and V_l ≥ af/r² ≥ c/r²; on [4, ρ],
ρ := c^(1/2)/(2σ) > 4, σ² = c/(4ρ²) ≤ c/(4r²), so V_σ ≥ (3/4)c/r², and A_+ ≥ (√3/2)c^(1/2)∫_4^ρ dr/r =
(√3/2)c^(1/2) log(ρ/4). Take x′ where V_l = σ²/2. For r ≥ 4, |d log V_l/dr_*| ≥ (2/r)(1 − 2/r²) ≥ 1.75/r by
[[eq:rb-monotone]], and V_l ≤ (κ + 3/4)/r² + 9/(64r²) ≤ (κ + 1)/r², so r(x′) ≤ (2(κ + 1))^(1/2)/σ,
x′ − x_2 ≤ (log 2/1.75)r(x′) and D_+(x′) ≤ 2 + (2 log 2/1.75)(κ + 1)^(1/2) ≤ 2 + 0.79217(κ + 1)^(1/2). So (ii) and (iii)
give A_− ≥ D_−(x)/√2 and A_+ ≥ D_+(x′)/√2, and [[prop:rb-coercive]] applies with c_I ≥ (15/256)a − σ².

Monotonicity: the left sides of (i) and (ii) increase with a and their right sides do not depend on l. In (iii) the
first condition improves with a; dividing the second by a^(1/2), its left side becomes
(√3/2)(15/16)^(1/2) log(c^(1/2)/(8σ)), which increases with l, and its right side
(2a^(−1/2) + 0.79217((κ + 1)/a)^(1/2))/√2, which decreases. ∎

At σ = 3, (i)–(iii) hold at l = 50 (the proof of [[cor:morawetz-one-derivative]] (d) evaluates them), so
[[eq:rb-closed-form]] holds for every l ≥ 50 at σ = 3, and, every condition being monotone in σ, for every
0 < |σ| ≤ 3.

**Remark {#rem:rb-closed-form-observed}** (Numerical observation.) The least degrees at which (i)–(iii) of
[[cor:rb-closed-form]] hold are l_0 = 14, 19 and 50 at σ = 0.3, 1 and 3. Evaluating the hypotheses of
[[prop:rb-coercive]] directly by quadrature, with the points x, x′ optimised over samples, gives them already from
l = 3, 7 and 18. Against the cut-off norms of the resolvent computed from numerical solutions of the radial equation
(on I, with a discretised kernel of 161 points), the bound 1/c_I lies within a factor 2 of the computed norm (ratios 1.3
to 1.9): at σ = 0.3 and l = 8, 16, 32 the computed norms are 0.121, 0.0399, 0.0120 against 0.215, 0.0594, 0.0157; at
σ = 1, 0.139, 0.0415, 0.0122 against 0.267, 0.0628, 0.0159; at σ = 3 and l = 32, 0.0135 against 0.0182. A quarter of
the bound falls below the computed norm somewhere. No proof uses these values.

### Above the barrier {#sec:rb-above}

**Proposition {#prop:resolvent-above-barrier}** (Above the barrier.) Let m = 1. For every l, V_l, as a function of
r_*, has exactly one critical point, a maximum; write V_max := max V_l. If σ is real and σ² > V_max, then
|u_h|² ≤ 2σ²/(σ² − V_max) and |u_∞|² ≤ 2σ²/(σ² − V_max) everywhere. Hence, for every r_*-interval J of length Λ_J,

    ‖χ_J R_l(σ) χ_J‖ ≤ Λ_J|σ|/(σ² − V_max);

in particular ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − V_max).

*Proof.* With a := κ + 3/4, b := 9/4 and y := 1/r², V_l = (1 − y)(ay + by²) and r³ dV_l/dr = −2a + 4(a − b)y + 6by².
This convex quadratic in y is −2a < 0 at y = 0 and 2a + 2b > 0 at y = 1, so it changes sign exactly once on (0, 1):
V_l rises, then falls. Let σ > 0; σ < 0 follows by conjugation.

- Where V_l rises, ℰ(u_h) ≤ 2σ² by [[lem:rb-energy]], and (σ² − V_l)n ≤ ℰ, so n ≤ 2σ²/(σ² − V_max) there.
- Where V_l falls, 𝒢 := ℰ/(σ² − V_l) satisfies 𝒢′ = V_l′|u′|²/(σ² − V_l)² ≤ 0, because ℰ′ = −V_l′n and
  ℰ − (σ² − V_l)n = |u′|². So 𝒢 does not exceed its value at the maximum, which is at most 2σ²/(σ² − V_max), and
  n ≤ 𝒢.
- The mirror argument, from +∞, gives the same bound for u_∞: where V_l rises, 𝒢 is nondecreasing in r_*.
- So |k_l| ≤ |u_h||u_∞|/|𝒲| ≤ (2σ²/(σ² − V_max))/(2σ) = σ/(σ² − V_max), by [[lem:rb-flux]], and the
  Hilbert–Schmidt bound on J × J gives the estimate. ∎

Above the barrier the constant is polynomial; the exponential constant of [[prop:resolvent-outgoing]] is needed, before
the multiplier bounds below, only for the harmonics with V_max ≥ σ² below l_0(σ). At σ = 3 these are 5 ≤ l < 50: for
12 ≤ l < 50, min_I V_σ > 0 and only the end signs of [[lem:rb-end-signs]] are missing; for 5 ≤ l < 12 the barrier top
lies above σ² without covering I.

**Remark {#rem:rb-band-observed}** (Numerical observation.) On I (Λ = 3.74), the cut-off norm computed from numerical
solutions of the radial equation (a discretised kernel of 161 points) lies below the bound of
[[prop:resolvent-above-barrier]]: 1.89 ≤ 7.57 at σ = 1, l = 0, and 0.41, 0.42, 0.45, 0.51, 0.67 ≤ 1.32, 1.45, 1.72,
2.35, 4.44 at σ = 3, l = 0, …, 4; a tenth of the bound falls below the computed norm. Between the two bounds, at σ = 3,
the computed norm is 0.672, 1.132, 0.983, 0.725, 0.287, 0.193, 0.0551 and 0.0225 at l = 4, 5, 6, 8, 11, 12, 17 and 25
(max V_l = 6.47, 9.22, 12.47, 20.47, 36.22, 42.47, 81.22, 169.22). It peaks at l = 5, the harmonic whose barrier top
lies nearest σ² = 9, is at most 1.132 for l ≤ 25, and falls like about 1/(l(l + 2)) beyond; where min_I V_σ > 0
(l ≥ 12) it lies below 1/min_I V_σ (1.116, 0.1002, 0.0327 at l = 12, 17, 25), also where the end-sign conditions of
[[lem:rb-end-signs]] fail. For 5 ≤ l ≤ 11, max_I|u_h|² grows to 9.18 · 10¹³ while |𝒲|/(2σ) grows in step to
4.72 · 10⁶, and the kernel stays of order 1. At further frequencies the computed norms for l = 0, 1, 2, 4, 8, 16, 32 are
4.75, 1.66, 0.79, 0.33, 0.12, 0.040, 0.012 at σ = 0.3 and 1.89, 3.00, 1.96, 0.55, 0.14, 0.042, 0.012 at σ = 1, while
the constant of [[prop:resolvent-outgoing]] (b) is about 10⁶⁰ at (σ, l) = (0.3, 8). No proof uses these values.

### The multiplier identity {#sec:morawetz-identity}

From here on m = 1, so that f = 1 − 1/r², r_h = 1 and the photon sphere is r = √2. The bounds of the previous
sections fail exactly where the barrier top of a harmonic lies near σ² and the barrier does not cover I. A
multiplier identity of Morawetz type covers every harmonic and every real σ ≠ 0. The multipliers below are
algebraic in r, every weight is (1 − r⁻²)r⁻³ times a rational function of r⁻², and every constant follows from
exact rational inequalities.

Throughout, y := 1/r² ∈ (0, 1), z := 1 − 2y ∈ (−1, 1) and η(y) := (1 − y)y^(3/2) = (r² − 1)/r⁵. The tortoise coordinate
r_* has dr_*/dr = 1/f, and g′ := dg/dr_*. Since dy/dr = −2y^(3/2),

    d/dr_* = −2η(y) d/dy.                                                                            {#eq:pb-tortoise}

As r_* → −∞, y → 1 and 1 − y decays like e^(2r_*); as r_* → ∞, r_* = r + O(log r). The interval I := {6/5 ≤ r ≤ 4} is
{1/16 ≤ y ≤ 25/36} = {−7/18 ≤ z ≤ 7/8}. With r_* = r + ½ log((r − 1)/(r + 1)), its length is
Λ := 14/5 + ½ log(33/5) < 3.7436. We write ‖·‖ for the norm of L²(ℝ, dr_*) and ‖·‖_I for that of L²(I, dr_*).

Since η_y = y^(1/2)(3/2 − 5y/2), η increases on [0, 3/5] and decreases on [3/5, 1]; so on an interval of y its least
value is attained at an end. We use η(1/16) = 15/1024, η(1/2) = 2^(−5/2), η(25/36) = 1375/7776 > 2^(−5/2) (as
32 · 1375² > 7776²) and max η = η(3/5) = 6√15/125. At a rational r, η = (r² − 1)/r⁵ is rational.

The potentials. Put U := f/r² = (1 − y)y, Q := f/r⁴ = (1 − y)y² and V_(a,b) := aU + bQ = (1 − y)(ay + by²). With
κ := l(l + 2), the potentials V_0, V_1, V_2 of [[prop:np-10-16]] at degree l, which we write V^□, V^v and V^s (those of
the scalar wave, of the vector-type and of the scalar-type 1-forms), are V_(κ+3/4,b) with b = 9/4, 5/4 and −7/4; so
V^□ = V_l. Those of [[thm:s15-ki]] are V_T = V^□ and
V_V = V_(κ+3/4,−27/4), and V_S = (1 − y)yQ_S/(16H²), with Q_S the polynomial [[eq:s15-ki-q]] at ς = y, p := κ − 3 and
H := p + 6y.

**Lemma {#lem:morawetz-identity}** (The multiplier identity.) Let V be a real smooth function on ℝ with V, V′ integrable
and V, V′ → 0 at ±∞. Let φ and q be real smooth functions on ℝ with |φ| ≤ 1, φ → ±1 at ±∞, and φ′, φ″, φ‴, q, q′, q″
integrable and tending to 0 at ±∞. Let σ ≠ 0 be real, F ∈ L²(ℝ) vanish outside I, and let u be a solution, with u and u′
locally absolutely continuous, of −u″ + (V − σ²)u = F almost everywhere, with u − c_±e^(±iσr_*) → 0 and
u′ ∓ iσu → 0 as r_* → ±∞. Then, with integrals over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2σ²∫q|u|² = Re∫F(2φū′ + (φ′ − 2q)ū) + 2σ²(|c_+|² + |c_−|²),
    W := −φV′ − ½φ‴ + q″ − 2qV,                                                                      {#eq:pb-identity}

and σ(|c_+|² + |c_−|²) = −Im∫Fū. Suppose moreover that φ′ − q ≥ 0, q ≥ 0 and W ≥ 0 on ℝ, and put
m′ := min_I (φ′ − q) > 0, M′ := max_I |φ′ − 2q| and w_I := min_I W > 0. Then X := ‖u′‖_I and Y := ‖u‖_I satisfy

    Y ≤ B‖F‖,     B := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2);                                       {#eq:pb-bound}

for every B̃ with Y ≤ B̃‖F‖, X ≤ X(B̃)‖F‖ with X(B̃) := (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′); and for every
decomposition W = W_0 + W_1 with W_0, W_1 ≥ 0 on ℝ, ∫_I W_1|u|² ≤ (2X(B̃) + (M′ + 2|σ|)B̃)‖F‖².

*Proof.* The hypotheses make u and u′ bounded, and every integral in [[eq:pb-identity]] absolutely convergent. With
Re(u″ū) = ½(|u|²)″ − |u′|² and Re(u′ū) = ½(|u|²)′, one checks term by term:

    Re(−u″ · 2φū′) = −(φ|u′|²)′ + φ′|u′|²,
    Re(−u″ · φ′ū) = −(φ′Re(u′ū))′ + φ′|u′|² + (½φ″|u|²)′ − ½φ‴|u|²,
    Re((V − σ²)u · 2φū′) = ((V − σ²)φ|u|²)′ − (φV′ + (V − σ²)φ′)|u|²,
    Re((V − σ²)u · φ′ū) = (V − σ²)φ′|u|²,
    Re((−u″ + (V − σ²)u) · (−2qū)) = (q(|u|²)′ − q′|u|²)′ + q″|u|² − 2q|u′|² − 2qV|u|² + 2σ²q|u|².

Adding, almost everywhere, Re(F(2φū′ + (φ′ − 2q)ū)) = 2(φ′ − q)|u′|² + W|u|² + 2σ²q|u|² + E′, where E := −φ|u′|² −
φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² + q(|u|²)′ − q′|u|², which is locally absolutely continuous, as u and u′ are. At ±∞,
|u′|² → σ²|c_±|², |u|² → |c_±|² and φ′, φ″, q, q′, V → 0, so E → −2σ²φ(±∞)|c_±|² = ∓2σ²|c_±|². Integrating over [−R, R],
where ∫E′ = E(R) − E(−R), and letting R → ∞ gives [[eq:pb-identity]]. Next, almost everywhere, Im(Fū) = −Im(u″ū) =
−(Im(u′ū))′, and Im(u′ū) → ±σ|c_±|² at ±∞; integrating gives the flux identity.

Under the sign conditions every integrand on the left of [[eq:pb-identity]] is nonnegative. Dropping the term with q and
restricting the other two to I, the left side is at least 2m′X² + w_IY². On the right, F vanishes off I and |φ| ≤ 1, so
the integral is at most ‖F‖(2X + M′Y), and 2σ²(|c_+|² + |c_−|²) = −2σIm∫Fū ≤ 2|σ|‖F‖Y. Hence

    2m′X² + w_IY² ≤ ‖F‖(2X + (M′ + 2|σ|)Y).                                                          {#eq:pb-energy}

By the Cauchy–Schwarz inequality, 2X + (M′ + 2|σ|)Y ≤ (2/m′ + (M′ + 2|σ|)²/w_I)^(1/2)(2m′X² + w_IY²)^(1/2), so
(2m′X² + w_IY²)^(1/2) ≤ (2/m′ + (M′ + 2|σ|)²/w_I)^(1/2)‖F‖ and w_I^(1/2)Y ≤ (2m′X² + w_IY²)^(1/2), which is
[[eq:pb-bound]]. Dropping w_IY² in [[eq:pb-energy]] and using Y ≤ B̃‖F‖ gives 2m′X² − 2‖F‖X − (M′ + 2|σ|)B̃‖F‖² ≤ 0, so
X is at most the positive root, X(B̃)‖F‖. Finally the left side of [[eq:pb-identity]] is at least ∫_I W_1|u|², and the
right side is at most ‖F‖(2X + (M′ + 2|σ|)Y) ≤ (2X(B̃) + (M′ + 2|σ|)B̃)‖F‖². ∎

For V = V_l and real σ ≠ 0, the outgoing solution u := R_l(σ)F satisfies the hypotheses on u for every F ∈ L²(ℝ)
vanishing off I, by [[prop:resolvent-outgoing]] (a); this is how the lemma is applied below.

For a multiplier φ = Θ(y) and a Lagrangian term q = ηg(y), [[eq:pb-tortoise]] gives φ′ = −2ηΘ_y,
−½φ‴ = 4η(η(ηΘ_y)_y)_y, −φV′ = 2ηΘV_y and, with h := (3/2 − 5y/2)g + y(1 − y)g_y, q′ = −2(1 − y)y²h and
q″ = 4ηy((2 − 3y)h + y(1 − y)h_y). So W = ηG with

    G = 2ΘV_y + 4(η(ηΘ_y)_y)_y + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV.                              {#eq:pb-weight-general}

Every φ and q below is a rational function of y (with g a polynomial), so φ′, φ″, φ‴, q, q′, q″ are η or (1 − y)y²
times bounded functions; they are O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

### The weight of the multiplier 1 − 2/r² {#sec:morawetz-algebraic-weight}

**Proposition {#prop:morawetz-weight}** (The Morawetz weight of φ = 1 − 2/r².) Let φ := z = 1 − 2/r². Then φ is
increasing, φ → ±1 at ±∞, φ′ = 4η, and for q = 0 and V = V_(a,b) the weight of [[lem:morawetz-identity]] is
W = ηP_(a,b)(z) with

    P_(a,b)(z) := 2 + (b/2 − 6)z + (2a + b − 6)z² + (10 − 3b/2)z³.                                     {#eq:pb-weight}

P_(a,b) is affine in b and nondecreasing in a, with ∂_aP_(a,b) = 2z², and ψ := −φU′ = 2ηz² ≥ 0. For the scalar wave at
harmonic l (a = κ + 3/4, b = 9/4) the weight is w_l := ηP_l with

    P_l(z) = P_0(z) + c_l z²,     P_0(z) := 2 − (39/8)z + (53/8)z³,     c_l := 2κ − 9/4,          {#eq:pb-weight-scalar}

so that w_l = w_1 + (κ − 3)ψ. In the variable y, P_1 = ½p with

    p(y) := 15 − 90y + 189y² − 106y³ = 15(1 − y)(1 − 3y)² + y(29y² − 36y + 15).                   {#eq:pb-p-certificate}

Hence w_l ≥ w_1 > 0 on ℝ for every l ≥ 1, and φ satisfies the hypotheses of [[lem:morawetz-identity]] with q = 0
for every V_(κ+3/4,9/4), l ≥ 1.

*Proof.* With Θ = 1 − 2y, Θ_y = −2 and ηΘ_y = −2η, so 4(η(ηΘ_y)_y)_y = −8(η_y² + ηη_yy). From η_y = (y^(1/2)/2)(3 − 5y)
and η_yy = (3/4)y^(−1/2)(1 − 5y), η_y² + ηη_yy = (y/4)((3 − 5y)² + 3(1 − y)(1 − 5y)) = y(10y² − 12y + 3). So by
[[eq:pb-weight-general]], G = 2zV_y − 8y(10y² − 12y + 3). For V = V_(a,b), V_y = a(1 − 2y) + by(2 − 3y), and with
y = (1 − z)/2 one has y(2 − 3y) = (1 − z)(1 + 3z)/4 and 10y² − 12y + 3 = −½ + z + (5/2)z². Hence
2zV_y = 2az² + (b/2)(z + 2z² − 3z³) and −8y(10y² − 12y + 3) = −4(1 − z)(−½ + z + (5/2)z²) = 2 − 6z − 6z² + 10z³; the sum
is [[eq:pb-weight]]. U = V_(1,0) gives U_y = z, U′ = −2ηz and −φU′ = 2ηz². At a = κ + 3/4, b = 9/4 the coefficients
are 2, −39/8, 2κ − 9/4 and 53/8, which is [[eq:pb-weight-scalar]]; and c_l − c_1 = 2(κ − 3) gives w_l − w_1 = (κ − 3)ψ.
Substituting z = 1 − 2y in P_1 gives ½p, and expanding the right side of [[eq:pb-p-certificate]] gives p. Its first term
is nonnegative on [0, 1] and its second is positive on (0, 1], since 29y² − 36y + 15 has discriminant 1296 − 1740 < 0;
at y = 0, p = 15. So p > 0 on [0, 1], w_1 > 0 on ℝ, and w_l ≥ w_1 because κ ≥ 3 and ψ ≥ 0. φ is increasing as φ′ = 4η
> 0, and |φ| < 1. ∎

**Lemma {#lem:morawetz-weight-interval}** (The weight on I.) Let l ≥ 1 and c := c_l. On I:

(i) for 6/5 ≤ r ≤ √2, w_l ≥ 2^(−3/2) = √2/4;

(ii) for √2 ≤ r ≤ 8/5, with e_0 := 1677/2048 and
d := e_0c − 9/16, w_l ≥ 2^(−5/2)(2 − (47/8)z + dz²); hence w_l is at least
2^(−5/2)(2 − 2209/(256d)) when d ≥ 94/7, and at least 2^(−5/2)(2 − 329/256 + 49d/1024) otherwise;

(iii) for 2 ≤ r ≤ 3, w_l ≥ 25/1944 + (392/19683)c; for 17/10 ≤ r ≤ 2, w_l ≥ 0.03658 + 0.012624c; and for
8/5 ≤ r ≤ 17/10, w_l ≥ 0.09213 + 0.0071190c;

(iv) for 3 ≤ r ≤ 4, w_l ≥ w_l(4) = (15/1024)(8899/4096 + (49/64)c).

Consequently min_I w_l ≥ ω_l, where ω_1 := 0.07388, ω_2 := 0.1860, ω_3 := 0.2847, ω_4 := 0.3122, ω_5 := 0.3257,
ω_l := 0.3335 for 6 ≤ l ≤ 19 and ω_l := 0.3514 for l ≥ 20.

*Proof.* Write A := ηP_0 and K := ηz², so that w_l = A + cK by [[eq:pb-weight-scalar]], with c ≥ 15/4. P_0′(z) =
−39/8 + (159/8)z² vanishes on [0, 1] only at z_0 := (39/159)^(1/2) < 0.4953, and P_0(z_0) = 2 − (13/4)z_0 > 0.3902;
P_0 decreases on [0, z_0] and increases on [z_0, 1]. In the variable z, η = (1 + z)(1 − z)^(3/2)2^(−5/2) decreases on
[0, 7/8] (that is y ∈ [1/16, 1/2] ⊂ [0, 3/5]), and K is unimodal on [0, 1], since
d log K/dz = 1/(1 + z) − 3/(2(1 − z)) + 2/z is decreasing.

(i) Here z ∈ [−7/18, 0], so −(39/8)z = (39/8)|z|, cz² ≥ 0 and (53/8)z³ ≥ −(53/8)(49/324)|z| > −1.002|z|; thus P_l ≥ 2.
Also y ∈ [1/2, 25/36], where η ≥ min(η(1/2), η(25/36)) = 2^(−5/2). So w_l ≥ 2^(−3/2).

(ii) Here z ∈ [0, 7/32]. First, P_l ≥ Q_c := 2 − (39/8)z + cz², as (53/8)z³ ≥ 0, and Q_c > 0 because its
discriminant (39/8)² − 8c is negative for c ≥ 15/4. Second, (1 − z)^(1/2) ≥ (1 − z)(1 + z/2) on [0, 1]: with
t := (1 − z)^(1/2) ∈ [0, 1] this is 2 ≥ t(3 − t²), that is (t − 1)²(t + 2) ≥ 0. Hence
η ≥ 2^(−5/2)(1 + z)(1 − z)²(1 + z/2) ≥ 2^(−5/2)(1 − z/2 − 3z²/2) ≥ 0, the middle step dropping (z³ + z⁴)/2 ≥ 0.
Multiplying,

    w_l ≥ 2^(−5/2)(1 − z/2 − 3z²/2)Q_c = 2^(−5/2)(2 − (47/8)z + (c − 9/16)z² + (117/16)z³ − c(z/2 + 3z²/2)z²),

and z/2 + 3z²/2 ≤ 7/64 + 147/2048 = 1 − e_0 on [0, 7/32]. Dropping (117/16)z³ ≥ 0 gives the bound. Its minimum over
z ∈ [0, 7/32] is at z = 47/(16d) when that lies in [0, 7/32], that is d ≥ 94/7, and at z = 7/32 otherwise.

(iii) On 2 ≤ r ≤ 3, y ∈ [1/9, 1/4] and z ∈ [1/2, 7/9] ⊂ [z_0, 1]: η ≥ η(1/9) = 8/243 and P_0 ≥ P_0(1/2) = 25/64, so
A ≥ 25/1944; and K ≥ min(K at r = 3, K at r = 2) = min(392/19683, 3/128). On 17/10 ≤ r ≤ 2, y ∈ [1/4, 100/289]:
η ≥ η(1/4) = 3/32 and P_0 ≥ P_0(z_0) > 0.3902, so A ≥ 0.03658; K ≥ K(17/10) = (189000/1419857)(89/289)² > 0.012624, as
K(2) = 3/128 is larger. On 8/5 ≤ r ≤ 17/10, z ∈ [7/32, 89/289] ⊂ [0, z_0]: η ≥ η(17/10) = 189000/1419857 and
P_0 ≥ P_0(89/289) = 66831535/96550276, so A > 0.09213; K ≥ K(8/5) = (4875/32768)(49/1024) = 238875/33554432.

(iv) We show that A and K increase with y on [1/16, 1/9], so that w_l, an increasing combination, does too. There
z ∈ [7/9, 7/8] ⊂ [z_0, 1], so P_0 decreases with y, and |dP_0/dy| = 2P_0′(z) = (159/4)z² − 39/4. Now
d log K/dy = 3/(2y) − 1/(1 − y) − 4/(1 − 2y) ≥ 27/2 − 9/8 − 36/7 > 0, and
d log A/dy = 3/(2y) − 1/(1 − y) + (dP_0/dy)/P_0.
On y ∈ [1/16, 1/12] the last expression is at least 18 − 12/11 − (5295/256)/(3061/1728) > 5.2, using P_0(5/6) = 3061/1728
and (159/4)(7/8)² − 39/4 = 5295/256; on [1/12, 1/10] it is at least 15 − 10/9 − (857/48)/(373/250) > 1.9, using
P_0(4/5) = 373/250; on [1/10, 1/9] it is at least 27/2 − 9/8 − 15.69/P_0(7/9) > 0.53, using P_0(7/9) > 1.3254. Finally
η(1/16) = 15/1024, P_0(7/8) = 8899/4096 and (7/8)² = 49/64.

Evaluating (i)–(iv): at l = 1 and l = 2, (iv) gives 309885/4194304 > 0.07388 and 780285/4194304 > 0.1860, (ii) more
than 0.147 and 0.216, the three bounds of (iii) more than 0.0839 and 0.190, and (i) more than 0.3535. For
l = 3, 4, 5, 6 and 20, d ≥ 94/7, and the vertex value in (ii) exceeds 0.2847, 0.3122, 0.3257, 0.3335 and 0.3514; the
bounds of (iii) are at least 0.2896, 0.4178, 0.5744, 0.7595 and 6.33, and those of (iv) at least 0.3430, 0.5449, 0.7916,
1.083 and 9.87. As w_l is nondecreasing in l ([[prop:morawetz-weight]]), the bounds at l = 6 and l = 20 hold for every
larger l. ∎

**Proposition {#prop:morawetz-resolvent-l-ge-1}** (Morawetz bounds for every harmonic l ≥ 1.) For every l ≥ 1 and every
real σ ≠ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ B_l(σ) := ((512/15 + (M′ + 2|σ|)²/ω_l)/ω_l)^(1/2),     M′ := 0.74362,

with ω_l of [[lem:morawetz-weight-interval]]. At σ → 0, 1, 3 and 10 these are at most:

| l | B_l(0+) | B_l(1) | B_l(3) | B_l(10) |
|---|---|---|---|---|
| 1 | 23.74 | 42.91 | 93.78 | 281.60 |
| 2 | 14.13 | 20.03 | 38.71 | 112.35 |
| 3 | 11.26 | 14.59 | 26.10 | 73.68 |
| 4 | 10.73 | 13.66 | 24.00 | 67.27 |
| 5 | 10.49 | 13.26 | 23.10 | 64.51 |
| every l ≥ 6 | 10.36 | 13.04 | 22.62 | 63.02 |
| every l ≥ 20 | 10.09 | 12.58 | 21.58 | 59.85 |

Each B_l is even in σ, increasing in |σ| and bounded as σ → 0.

*Proof.* [[prop:morawetz-weight]] gives the hypotheses of [[lem:morawetz-identity]] with φ = z, q = 0. On I, φ′ = 4η
has least value 4 min(η(1/16), η(25/36)) = 15/256, so 2/m′ = 512/15, and greatest value 4η(3/5) = 24√15/125 < 0.74362,
since 3.873² > 15. So w_I ≥ ω_l by [[lem:morawetz-weight-interval]], and [[eq:pb-bound]] gives the bound; it decreases in
w_I and increases in M′. The table evaluates the formula, rounding up. ∎

### The harmonic l = 0 {#sec:morawetz-l-zero}

**Proposition {#prop:morawetz-l-zero}** (The harmonic l = 0.) Let φ := 1 − 2/r² and q := ½η(1 + 3y/2). Then
0 ≤ q ≤ (5/16)φ′, and for the scalar wave at l = 0, V = V_(3/4,9/4), the weight of [[lem:morawetz-identity]] is

    W = (3/8)ηQ_4,     Q_4(y) := 149y⁴ − 280y³ + 177y² − 42y + 4
                               = (2 − (21/2)y + 11y²)² + y²(28(y − 7/8)² + 21/16) > 0.          {#eq:pb-lzero-weight}

On I, m′ = min_I(φ′ − q) = 3315/65536, M′ = max_I|φ′ − 2q| < 0.3999 and w_I = W(4) = 5899185/536870912 > 0.010988. So
for every real σ ≠ 0, ‖χ_I R_0(σ) χ_I‖ ≤ B_0(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2), which is at most 70.17,
226.50, 585.53 and 1857.54 at σ → 0, σ = 1, 3 and 10. In [[lem:morawetz-complex]],
max q = 2√6/27 < 0.18145, attained at y = 2/3.

*Proof.* q = ηg with g = (2 + 3y)/4 ≥ 0, and φ′ = 4η, so q/φ′ = (2 + 3y)/16 ≤ 5/16. In [[eq:pb-weight-general]], h = (6
+ 5y − 21y²)/8 and (2 − 3y)h + y(1 − y)h_y = (12 − 3y − 104y² + 105y³)/8, so the q″-term is ½y(12 − 3y − 104y² + 105y³).
By [[prop:morawetz-weight]] the φ-terms give P_(3/4,9/4) = 3/2 − 21y + (141/2)y² − 53y³ in the variable y, and
−2gV_(3/4,9/4) = −(3/8)y(1 − y)(2 + 3y)(1 + 3y) = −(3/4)y − (21/8)y² + (27/8)y⁴. The sum is (3/8)Q_4, and the second
form of Q_4 is checked by expansion. In it, 28y² − 49y + 22.75 = 28(y − 7/8)² + 21/16 > 0, and the two terms do not
vanish together, since the second vanishes only at y = 0, where the first is 4.

The constants. φ′ − q = η(14 − 3y)/4. On [1/16, 1/4], d log(η(14 − 3y))/dy = 3/(2y) − 1/(1 − y) − 3/(14 − 3y) ≥
6 − 4/3 − 3/13 > 0, so the least value there is at y = 1/16: (15/1024)(221/64) = 3315/65536; on [1/4, 25/36],
φ′ − q ≥ (3/32)(14 − 25/12)/4 > 0.27. Next φ′ − 2q = (3/2)η(2 − y) ≥ 0, whose derivative in y is
(3/2)y^(1/2)(3 − (15/2)y + (7/2)y²); its only zero in (0, 1) is y_* = (15 − √57)/14 ∈ (0.5321, 0.5322), and
(3/2)η(y_*)(2 − y_*) < 0.3999.

For w_I, Q_4 has the Taylor expansion at 1/5, with s := y − 1/5,

    Q_4 = 424/625 − (4/125)s + s²(149s² − (804/5)s + 1119/25),

and the last bracket is positive, its discriminant (804/5)² − 4 · 149 · 1119/25 being negative. So Q_4 ≥ 0.6784 −
0.032s, which is at least 0.6768 on [3/20, 1/4] and 0.6625 on [1/4, 25/36]. Also Q_4″ = 1788y² − 1680y + 354 > 0 on
[0, 1/5] (it decreases there to 89.52), so Q_4′ increases there to Q_4′(1/5) = −0.032, and Q_4 decreases on [0, 1/5].
Then:

- on [1/16, 5/64], d log W/dy = 3/(2y) − 1/(1 − y) + Q_4′/Q_4 ≥ 19.2 − 64/59 − |Q_4′(1/16)|/Q_4(5/64) ≥
  19.2 − 1.085 − 23.011/1.6711 > 0, and on [5/64, 3/32] it is at least 16 − 32/29 − 19.187/1.3989 > 0, so W ≥ W(4) on
  [1/16, 3/32];
- on [3/32, 7/64], [7/64, 1/8] and [1/8, 3/20], W ≥ (3/8)η(left end)Q_4(right end), that is at least
  (3/8)(0.026013)(1.1786), (3/8)(0.032216)(1.0051) and (3/8)(0.038669)(0.81293), all above 0.0114;
- on [3/20, 1/4], W ≥ (3/8)(0.049380)(0.6768) > 0.0125, and on [1/4, 25/36], W ≥ (3/8)(3/32)(0.6625) > 0.023.

Here Q_4(1/16) = 131093/65536, so W(4) = (3/8)(15/1024)(131093/65536). [[lem:morawetz-identity]] applies, and the bounds
follow from [[eq:pb-bound]]. For max q: d/dy(η(2 + 3y)) = y^(1/2)(3 + (5/2)y − (21/2)y²), which vanishes on (0, 1) only
at y = 2/3, where q = (1/3)(2/3)^(3/2) = 2√6/27. ∎

### Off the real axis with a multiplier {#sec:morawetz-complex}

**Lemma {#lem:morawetz-complex}** (Off the real axis.) Let V ≥ 0 be real and bounded, with V and V′ integrable and
tending to 0 at ±∞, and let φ and q satisfy the hypotheses of [[lem:morawetz-identity]], its sign conditions
included, with constants m′, M′ and w_I. Let Im σ > 0, F ∈ L²(ℝ) vanish outside I, and let u := (−∂²_(r_*) + V − σ²)⁻¹F
be the solution in L²(ℝ). Then

    ‖u‖_I ≤ B⁺(σ)‖F‖,     B⁺(σ) := ((2/m′ + (M′ + 4|σ| + 2 max q)²/w_I)/w_I)^(1/2),

and the bounds of [[lem:morawetz-identity]] for ‖u′‖_I and for ∫_I W_1|u|² hold with 2|σ| replaced by
4|σ| + 2 max q. When q = 0, or when Re σ² ≥ 0, the term 2 max q may be dropped.

*Proof.* Write σ² = a_σ + ib_σ. The operator −∂² + V is self-adjoint and nonnegative, so u ∈ H²(ℝ); off I, u solves
the homogeneous equation and lies in L², so near ±∞ it is a multiple of the solution that behaves like e^(±iσr_*),
which decays exponentially with its derivative. So every boundary term below vanishes and no flux term arises. Pair
−u″ + (V − a_σ)u − ib_σu = F with 2φū′ + (φ′ − 2q)ū and take real parts. The terms with V − a_σ give, by the
calculation in the proof of [[lem:morawetz-identity]] with σ² replaced by a_σ, the integrand
2(φ′ − q)|u′|² + W|u|² + 2a_σq|u|² plus an exact derivative; the new term gives
Re(−ib_σu(2φū′ + (φ′ − 2q)ū)) = 2b_σφ Im(uū′). Integrating over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2a_σ∫q|u|² = Re∫F(2φū′ + (φ′ − 2q)ū) − 2b_σ∫φ Im(uū′).

Integration by parts gives the energy identity ∫Fū = ‖u′‖² + ∫V|u|² − σ²‖u‖², norms over ℝ. Its imaginary part gives
|b_σ|‖u‖² ≤ ‖F‖‖u‖_I, and its real part, with V ≥ 0, ‖u′‖² ≤ ‖F‖‖u‖_I + a_+‖u‖², a_+ := max(a_σ, 0). As |φ| ≤ 1,

    |2b_σ∫φ Im(uū′)| ≤ 2|b_σ|‖u‖‖u′‖ ≤ 2|b_σ|‖u‖(‖F‖‖u‖_I)^(1/2) + 2|b_σ|a_+^(1/2)‖u‖²
                      ≤ 2(|b_σ|^(1/2) + a_+^(1/2))‖F‖‖u‖_I ≤ 4|σ|‖F‖‖u‖_I,

since |b_σ| = 2|Re σ| Im σ ≤ |σ|² and a_+^(1/2) ≤ |Re σ| ≤ |σ|. If a_σ ≥ 0 the term 2a_σ∫q|u|² is nonnegative and is
dropped; if a_σ < 0, the real part of the energy identity gives |a_σ|‖u‖² ≤ ‖F‖‖u‖_I, so
−2a_σ∫q|u|² ≤ 2 max q ‖F‖‖u‖_I, and this term is moved to the right. Then the left side is at least 2m′X² + w_IY²,
X := ‖u′‖_I, Y := ‖u‖_I, and the right side is at most ‖F‖(2X + (M′ + 4|σ| + 2 max q)Y); the rest is the algebra of the
proof of [[lem:morawetz-identity]], with M′ + 4|σ| + 2 max q in place of M′ + 2|σ|. ∎

So the real-axis bounds are stable under Im σ > 0: B⁺ is continuous in σ and bounded on compact subsets of
{Im σ ≥ 0, σ ≠ 0}, and the degeneration of [[lem:rb-off-axis]] as Im σ → 0 is not met. As Im σ → 0, B⁺ tends to the
constant with 4|σ|, not to the real-axis one: the factor 2 is the price of bounding the b_σ-term by norms over ℝ. For
every l ≥ 1 the multiplier of [[prop:morawetz-resolvent-l-ge-1]] has q = 0; for l = 0, max q = 2√6/27
([[prop:morawetz-l-zero]]).

### One derivative {#sec:morawetz-one-derivative}

**Corollary {#cor:morawetz-one-derivative}** (The H¹ constants.) Let σ ≠ 0 be real, F ∈ L²(I), and u = R_l(σ)F, with
ψ = 2ηz² the weight of [[prop:morawetz-weight]], which vanishes on ℝ only at the photon sphere r = √2, to second order.

(a) For l ≥ 1, with m′ = 15/256, M′ = 0.74362 and B_l = B_l(σ) of [[prop:morawetz-resolvent-l-ge-1]],
‖u′‖_I ≤ X_l‖F‖ and (κ − 3)∫_I ψ|u|² ≤ K_l‖F‖², where X_l := (1 + (1 + 2m′(M′ + 2|σ|)B_l)^(1/2))/(2m′) and
K_l := 2X_l + (M′ + 2|σ|)B_l. With A_l := κK_l/(κ − 3) for l ≥ 2, A_1 := 3B_1² and C_l² := X_l² + A_l, at σ = 3:

| l | 1 | 2 | 3 | 4 | 5 | ≥ 6 |
|---|---|---|---|---|---|---|
| B_l(3) | 93.78 | 38.71 | 26.10 | 24.00 | 23.10 | 22.62 |
| X_l | 82.49 | 56.50 | 48.22 | 46.67 | 45.98 | 45.61 |
| A_l | 26,381.1 | 598.4 | 340.6 | 291.7 | 271.0 | 260.0 |
| C_l | 182.17 | 61.57 | 51.63 | 49.69 | 48.84 | 48.37 |

(b) For l = 0, with the constants of [[prop:morawetz-l-zero]], ‖u′‖_I ≤ X_0‖F‖ with
X_0 := (1 + (1 + 2m′(M′ + 2|σ|)B_0)^(1/2))/(2m′); X_0(3) < 202.6.

(c) Summed over the harmonics, which are orthogonal on 𝕊³: for every real 0 < |σ| ≤ 3,

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖F‖²,     C ≤ 182.17 over l ≥ 1 and C ≤ 202.6 over l ≥ 0,

the angular part at l = 1 taken unweighted. At |σ| = 1/2, 1, 2 and 3, C_1 is at most 63.86, 85.06, 132.46, 182.17 and
X_0 at most 55.13, 83.85, 142.96, 202.6.

(d) Without the weight: for every real 0 < |σ| ≤ 3, ‖∂_(r_*)u‖_I² + Σ_l κ‖u_l‖_I² ≤ C_u²‖F‖² with C_u < 1079.4.

*Proof.* (a) and (b) are [[lem:morawetz-identity]] with B̃ = B_l. In (a), W_1 := (κ − 3)ψ and W_0 := w_1 are
nonnegative ([[prop:morawetz-weight]]); so (κ − 3)∫_Iψ|u|² ≤ K_l‖F‖², and κ∫_Iψ|u|² ≤ A_l‖F‖² for l ≥ 2. At l = 1,
3‖u‖_I² ≤ 3B_1²‖F‖². For l ≥ 6, B_l ≤ B_6, X_l ≤ X_6, K_l ≤ K_6, and κ/(κ − 3) decreases, so C_l ≤ C_6. The table
evaluates the formulas at σ = 3, rounding up.

(c) Every quantity in (a) and (b) is an explicit function increasing in |σ|, so the values at |σ| = 3 bound the band.
The harmonics are orthogonal, so the sum is at most max_l C_l² (and X_0² at l = 0) times ‖F‖², and C_l ≤ C_1 for every
l ≥ 1 by the table. The values at |σ| = 1/2, 1, 2 evaluate the same formulas.

(d) The left side is at most max_l (X_l² + κB_l²)‖F‖², with any valid B_l. For l ≥ 50 we use the closed-form bound of
[[cor:rb-closed-form]], ‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)(κ + 3/4) − σ²), valid when its three conditions hold. At
l = 50 (κ + 3/4 = 2600.75) and σ = 3 they read 152.38 > 9 and 373.0 > 9; 0.32727(313.45 − 9)^(1/2) > 5.71 >
(2 + 3.3744)/√2; and, with c := (15/16)(2600.75) > 2438.2, c^(1/2) > 49.37 > 24 and
(√3/2)(49.37)log(49.37/24) > 30.8 > 29.99 > (2 + 0.79217 · 51)/√2. Each condition becomes easier as l grows or |σ|
decreases, so the bound holds for l ≥ 50 and 0 < |σ| ≤ 3; there B_l ≤ 0.006975, X_l² + κB_l² < 17.1², and both terms
decrease in κ. For 1 ≤ l ≤ 49 we use B_l(3) of [[prop:morawetz-resolvent-l-ge-1]]: (X_l² + κB_l²)^(1/2) is at most
182.2, 123.2, 112.0, 126.5, 144.2 for l = 1, …, 5, at most 454.0 for 6 ≤ l ≤ 19 (using ω_6 and κ ≤ 399) and at most
1079.4 for 20 ≤ l ≤ 49 (using ω_20 and κ ≤ 2499). At l = 0 the term is X_0² < 202.6². ∎

**Remark {#rem:rb-multiplier-observed}** (Numerical observation.) Multipliers tanh((r_* − x_p)/s) centred at the peak
x_p of V_l, checked to give a nonnegative weight on a grid, give w ≥ 0 for 1 ≤ l ≤ 30 at s = 0.98 and for no s in
[0.2, 0.98] at l = 0; at σ = 3 their bounds are about 253, 53.3, 35.5, 26.6, 21.35, 19.5, 19.3, 19.2 and 19.2 at l = 1,
2, 3, 4, 5, 6, 10, 17 and 25, against cut-off norms computed from numerical solutions of 0.423, 0.451, 0.508, 0.672,
1.132, 0.983, 0.421, 0.0551 and 0.0225. Off the axis, at l = 1 and σ = 3 + iη, the cut-off norm computed by finite
differences is 0.297, 0.224, 0.145 and 0.081 at η = 0.25, 0.5, 1 and 2, below 1/|Im σ²|; at l = 0 it is 0.183, 0.594
and 0.224 at σ = 1 + 2i, 0.5 + i and 2 + i. Multipliers whose width grows from 49/50 toward the horizon to 2 outside,
optimised on a grid, give at σ = 3 the values B_1(3) ≈ 95.6 and X_0(3) ≈ 117.3. No proof uses these values.

### From the radial problem to the spacetime operators {#sec:rb-transfer}

**Lemma {#lem:rb-schur}** (Blocks.) Let P̂(σ) be the spectral family at b_0 of □ on functions, of □ on 1-forms or of
2L_(b_0), and let 𝔏 := L²(I × 𝕊³, r³dr dω) with the pointwise norm of the static frame (dt, dr, r dω) (for m_0 = 1,
I = {6/5 ≤ r ≤ 4}). The rotations SO(4) act unitarily on 𝔏 and commute with P̂(σ) and χ_I. Let C_π bound
‖χ_I P̂(σ)⁻¹ χ_I F‖_𝔏/‖F‖_𝔏 over the smooth F supported in I × 𝕊³ that lie in the isotypic component π. Then
C_D(σ) := ‖χ_I P̂(σ)⁻¹ χ_I‖_(𝔏→𝔏) ≤ sup_π C_π, with equality when each C_π is the least such bound. For functions the
components are the degrees l; for 1-forms and symmetric 2-tensors each component consists of fields of one type
([[def:iii-a1-1-3]]) and one degree.

*Proof.* SO(4) acts by isometries of g_(b_0), on sections of the tensor bundles; it preserves the density and the
static frame up to rotation of its angular part, so it acts unitarily on 𝔏. P̂(σ) is built from g_(b_0) and from
1-forms that are combinations of dt and dr with coefficients depending on r alone, so it commutes with SO(4), and so do
P̂(σ)⁻¹ and χ_I. The isotypic decomposition of a unitary representation of a compact group is orthogonal, and an
operator commuting with the group maps each component into itself; so for F = Σ_π F_π,
‖χ_IP̂(σ)⁻¹χ_IF‖² = Σ_π ‖χ_IP̂(σ)⁻¹χ_IF_π‖² ≤ sup_π C_π² Σ_π‖F_π‖², and the smooth fields supported in I × 𝕊³ are
dense. Scalar harmonics of degree l carry the representation (l/2, l/2) of SO(4) = (SU(2) × SU(2))/{±1}, vector-type
fields of degree l the sum of ((l + 1)/2, (l − 1)/2) and ((l − 1)/2, (l + 1)/2), and tensor-type fields the sum of
((l + 2)/2, (l − 2)/2) and ((l − 2)/2, (l + 2)/2). These are distinct for distinct pairs (type, degree), so each
isotypic component lies within one type and one degree. ∎

The function spaces 𝒳_σ, 𝒴_σ of the stability theory are invariant under SO(4) only up to equivalence: averaging over
SO(4) gives invariant norms, equivalent to the given ones with constant sup_g ‖g‖_(𝒳_σ→𝒳_σ) ‖g‖_(𝒴_σ→𝒴_σ), a
constant of the calculus.

**Lemma {#lem:rb-transfer}** (The exact transfers.) Let m_0 = 1 and σ real and nonzero. Let B(σ) bound the cut-off
outgoing resolvent ‖χ_I R(σ) χ_I‖ on L²(ℝ, dr_*) of the master operator −∂²_(r_*) + V − σ² named below, for the degree
l in question. Then, on fields of the block named,

    ‖χ_I P̂(σ)⁻¹ χ_I‖_(𝔏→𝔏) ≤ (15/16) B(σ)

in each of the following cases: P̂ = □ on functions of degree l, V = V_l; P̂ = □ on 1-forms of vector type l, V = V^v
(the potential V_1 of [[prop:np-10-16]] (iii)); P̂ = 2L_(b_0) on symmetric 2-tensors of tensor type l ≥ 2, V = V_T of
[[thm:s15-ki]] (T).

*Proof.* P̂(σ) is invertible on the spaces of the stability theory ([[prop:iii-d-6-2]] for □, [[prop:iii-f2-3-1]] for
2L_(b_0)). Let F be smooth, supported in I × 𝕊³ and in the block; then ω := P̂(σ)⁻¹F lies in the block
([[lem:rb-schur]]) and is smooth across the future horizon and outgoing at infinity. Write c := ‖Y‖²_(L²(𝕊³)) for the
angular field Y of the block, and recall dr = f dr_*.

- *Functions.* ω = r^(−3/2)uS and F = gS. By [[eq:rb-radial]], −u″ + (V_l − σ²)u = G with G := fr^(3/2)g. Then
  |ω|²r³dr = f|u|²|S|²dr_* and |G|² dr_* = fr³|g|² dr, so ‖ω‖²_𝔏 ≤ c(max_I f)‖u‖²_I and
  ‖G‖² ≤ (max_I f)‖F‖²_𝔏/c.
- *Vector type.* ω = r^(−1/2)uY with Y ∈ 𝒱_l, δω = 0 and □ω = δdω. By [[prop:np-10-16]] (iii) the t- and r-components
  of δdω vanish and its angular part is gY with −fr^(1/2)g = u″ + σ²u − V^vu, so −u″ + (V^v − σ²)u = G := fr^(1/2)g. In
  the static frame |ω|² = r⁻³|u|²|Y|² and |F|² = r⁻²|g|²|Y|², so |ω|²r³dr = f|u|²|Y|²dr_*, while the integral of
  |F|²r³dr over 𝕊³ is cr|g|²dr and |G|²dr_* = fr|g|²dr; the two inequalities of the first case follow verbatim.
- *Tensor type.* ω = 2r²HT with T ∈ 𝒯_l. Then tr ω = 0, δω = 0, and ι_(g⁻¹c)ω = 0 for every c in the span of dt and
  dr, so the gauge terms of L_(b_0) vanish on ω and L_(b_0)ω = D Ric(ω) = −r²ℬ[H]T, where
  ℬ[H] := □_2H + (3/r)Dr · DH − ((k_T² + 2)/r²)H and all other components vanish ([KI03, (5.3), p. 13], in the
  notation of [[thm:s15-ki]]). With u := r^(3/2)H, fr^(3/2)ℬ[r^(−3/2)u] = u″ + σ²u − V_Tu, so F = 2L_(b_0)ω = −2r²ℬT
  and −u″ + (V_T − σ²)u = G := −fr^(3/2)ℬ. In the static frame |ω|² = 4|H|²|T|² and |F|² = 4|ℬ|²|T|², so
  |ω|²r³dr = 4f|u|²|T|²dr_* and |F|²r³dr = 4fr³|ℬ|²|T|²dr_*, while |G|² = f²r³|ℬ|²; so ‖ω‖²_𝔏 ≤ 4c(max_I f)‖u‖²_I and
  ‖G‖² ≤ (max_I f)‖F‖²_𝔏/(4c).

In each case u is outgoing and regular at the horizon, so u = R(σ)G by [[prop:resolvent-outgoing]] (a), and G vanishes
off I. Hence ‖ω‖_𝔏 ≤ (c′ max_I f)^(1/2)‖u‖_I ≤ (c′ max_I f)^(1/2)B(σ)‖G‖ ≤ (max_I f)B(σ)‖F‖_𝔏, with c′ = c, resp. 4c.
f increases, so max_I f = f(4) = 15/16. ∎

By [[lem:rb-schur]], the bounds of [[lem:rb-transfer]], taken uniformly in l, bound the cut-off inverse on all fields of
the type.

### The master operators {#sec:morawetz-master}

**Lemma {#lem:bernstein-lower-bound}** (Bernstein lower bound.) Let p be a polynomial of degree at most n and α < β.
Write p(α + (β − α)t) = Σ_(j≤n) c_j t^j and b_k := Σ_(j≤k) (C(k, j)/C(n, j))c_j for 0 ≤ k ≤ n. Then
min_([α,β]) p ≥ min_k b_k.

*Proof.* Expanding t^j = t^j(t + (1 − t))^(n−j) by the binomial theorem gives
t^j = Σ_(k≥j) (C(k, j)/C(n, j))C(n, k)t^k(1 − t)^(n−k), as C(n − j, k − j)/C(n, k) = C(k, j)/C(n, j). So
p(α + (β − α)t) = Σ_k b_k C(n, k)t^k(1 − t)^(n−k), a combination of the b_k with nonnegative weights of sum 1 on
t ∈ [0, 1]. ∎

In the proposition below a weight is W = ηN/D with N a polynomial and D a product of powers of positive increasing linear
functions of y. A lower bound on a piece r ∈ [r_2, r_1] (y ∈ [1/r_1², 1/r_2²]) is the product of η at the end where it is
least and of the least Bernstein coefficient of N on the piece divided by the value of D at its right end in y. Each
piece below is written "r_1–r_2: e · g ≥ v" with e and g such lower bounds. Positivity on (0, 1) is shown by the
Bernstein coefficients of N on the listed subintervals of [0, 1], whose least values are given.

**Proposition {#prop:morawetz-master-potentials}** (Every master operator at every harmonic.) Let m′, M′ and w_I be as
listed, and B(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2). For the operator −∂²_(r_*) + V − σ² of each of the following
rows, every real σ ≠ 0 and every harmonic of the row, ‖χ_I R(σ) χ_I‖ ≤ B(σ), with the values at σ → 0, σ = 1, 3, 10:

| row | operators and harmonics | multiplier | w_I ≥ | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|---|
| A | V^□, V^v, every l ≥ 1 | z | 0.064 | 25.86 | 48.70 | 107.88 | 324.95 |
| B | V^□, V^v, V^s, V_T, every l ≥ 2 | z | 0.1393 | 16.54 | 25.16 | 50.88 | 149.74 |
| C | V_V, every l ≥ 3 | z | 0.1413 | 16.41 | 24.88 | 50.20 | 147.63 |
| S4 | V_S, every l ≥ 4 | z | 0.1874 | 14.07 | 19.92 | 38.44 | 111.52 |
| S3 | V_S, l = 3 | z | 0.106 | 19.27 | 31.50 | 66.11 | 196.52 |
| T1 | V^s, l = 1 | z, q = (5/3)ηy | 0.0455 | 29.22 | 59.91 | 143.71 | 449.56 |
| T2 | V_V, l = 2 | z, q = 2ηy² | 0.0687 | 23.62 | 43.09 | 97.67 | 299.71 |
| T3 | V_S, l = 2 | (1 − 4y)/(1 + 2y), q = ½ηy(1 + y) | 0.0413 | 23.15 | 64.82 | 160.01 | 498.25 |

with m′ = 15/256, M′ = 0.74362 in rows A–S3, and (m′, M′) = (2805/49152, 0.4157), (7665/131072, 0.5324) and
(0.1384, 0.563) in rows T1, T2, T3. The largest values over all rows are 29.22, 64.82, 160.01 and 498.25. Multiplied by
15/16, the transfer of [[lem:rb-transfer]], rows A and B bound the vector-type 1-form blocks at l = 1 (24.24, 45.66,
101.13, 304.64) and at l ≥ 2 (15.51, 23.59, 47.70, 140.38), and row B the tensor-type blocks, every l ≥ 2 (the same).

*Proof.* In each row we give G = N/D of [[eq:pb-weight-general]], its positivity on (0, 1), which with the conditions on
φ′ − q, q and |φ| gives the hypotheses of [[lem:morawetz-identity]], and the lower bound for w_I. Then [[eq:pb-bound]]
gives the bound; the table evaluates it, rounding up.

Families. By [[prop:morawetz-weight]], for φ = z and q = 0 the weight of V_(a,b) is ηP_(a,b), affine in b and
nondecreasing in a; so for a ≥ a_0 and b_− ≤ b ≤ b_+ it is at least the smaller of the weights at (a_0, b_−) and
(a_0, b_+), on ℝ and on I. Row A is the family a ≥ 15/4, 5/4 ≤ b ≤ 9/4; row B the family a ≥ 35/4, −7/4 ≤ b ≤ 9/4; row C
the family a ≥ 63/4, b = −27/4. The corners (15/4, 9/4) and (35/4, 9/4) are the scalar wave at l = 1 and l = 2, with
w_I ≥ 0.07388 and 0.1860 by [[lem:morawetz-weight-interval]]. For the others, in the variable y, G = N with:

- (15/4, 5/4): N = 15/2 − 49y + (217/2)y² − 65y³; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 1]: at least 1.01, 0.437, 2.
  Pieces: 4–37/10: 0.01464 · 4.474 ≥ 0.0654; 37/10–31/10: 0.0183 · 3.502 ≥ 0.064; 31/10–5/2: 0.03007 · 2.171 ≥ 0.0652;
  5/2–21/10: 0.05376 · 1.209 ≥ 0.0649; 21/10–9/5: 0.08349 · 0.8011 ≥ 0.0668; 9/5–6/5: 0.1185 · 0.7239 ≥ 0.0857.
- (35/4, −7/4): N = 35/2 − 101y + (381/2)y² − 101y³; Bernstein: at least 2.57, 0.52, 2 on the same subintervals.
  Pieces: 4–33/10: 0.01464 · 9.753 ≥ 0.1427; 33/10–5/2: 0.02527 · 5.803 ≥ 0.1466; 5/2–21/10: 0.05376 · 3.215 ≥ 0.1728;
  21/10–19/10: 0.08349 · 1.993 ≥ 0.1663; 19/10–9/5: 0.1054 · 1.504 ≥ 0.1585; 9/5–17/10: 0.1185 · 1.176 ≥ 0.1393;
  17/10–8/5: 0.1331 · 1.071 ≥ 0.1425; 8/5–6/5: 0.1487 · 1.094 ≥ 0.1626.
- (63/4, −27/4): N = 63/2 − 177y + (633/2)y² − 161y³; Bernstein: at least 4.51, 0.437, 2. Pieces: 4–49/20:
  0.01464 · 10.05 ≥ 0.1471; 49/20–37/20: 0.05667 · 2.787 ≥ 0.1579; 37/20–17/10: 0.1117 · 1.478 ≥ 0.165; 17/10–33/20:
  0.1331 · 1.208 ≥ 0.1607; 33/20–31/20: 0.1408 · 1.004 ≥ 0.1413; 31/20–6/5: 0.1567 · 1.05 ≥ 0.1645.

Row S4. Here κ ≥ 24, p = κ − 3 = 21 + t with t ≥ 0, a = κ + 3/4 and H = H_0 + t, H_0 := 21 + 6y. With
G = 2zV_(S,y) − 8y(10y² − 12y + 3), expanding gives 16H³G = Σ_(j≤4) c_j(y)t^j with

    c_0 = −216(848y⁶ + 7008y⁵ + 16392y⁴ + 18376y³ − 205275y² + 159348y − 33957),
    c_1 = −72(1144y⁵ + 5868y⁴ + 10226y³ − 103203y² + 84042y − 18669),
    c_2 = −24(508y⁴ + 1828y³ − 19269y² + 16608y − 3843),
    c_3 = −8(106y³ − 1581y² + 1458y − 351),     c_4 = 32(2y − 1)².

The Bernstein coefficients of c_0 on [0, 1/2], [1/2, 1] are at least 53568 and 442368; those of c_1, c_2, c_3 on
[0, 1/4], [1/4, 1/2], [1/2, 1] at least 282590, 25776, 55296; 20754, 750, 2304; and 669, 3, 32. So c_0, …, c_3 > 0 and
c_4 ≥ 0 on [0, 1], and G > 0 on (0, 1) for every l ≥ 4. Moreover (H_0 + t)³ = Σ_(j≤3) C(3, j)H_0^(3−j)t^j, so
G ≥ k_S(y) := min_(j≤3) c_j/(16C(3, j)H_0^(3−j)) for every t ≥ 0, uniformly in l. On pieces, with k_S bounded below by
the least Bernstein coefficients of the c_j and the largest H_0: 4–23/10: 0.014648 · 13.722 ≥ 0.2009; 23/10–9/5:
0.066652 · 4.0959 ≥ 0.2729; 9/5–8/5: 0.11854 · 1.5817 ≥ 0.1874; 8/5–3/2: 0.14877 · 1.2656 ≥ 0.1882; 3/2–7/5:
0.1646 · 1.2626 ≥ 0.2078; 7/5–6/5: 0.17682 · 1.9338 ≥ 0.3419.

Row S3. At l = 3, p = 12 and H = 6(2 + y): N = 504 − 2652y + 3786y² − 161y³ − 420y⁴ − 447y⁵ − 106y⁶, D = 2(2 + y)³;
Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 1]: at least 73, 12.1, 62.5. Pieces: 4–12/5: 0.01464 · 7.614 ≥ 0.1114;
12/5–37/20: 0.05977 · 1.837 ≥ 0.1097; 37/20–17/10: 0.1117 · 0.9511 ≥ 0.1062; 17/10–33/20: 0.1331 · 0.8221 ≥ 0.1094;
33/20–31/20: 0.1408 · 0.7532 ≥ 0.106; 31/20–5/4: 0.1567 · 0.6989 ≥ 0.1095; 5/4–6/5: 0.1768 · 4.844 ≥ 0.8564.

Row T1 (a = 15/4, b = −7/4; here a + b < 4, and q is needed at the horizon). g = (5/3)y gives
N = 15/2 − 61y + 188y² − (728/3)y³ + (665/6)y⁴; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 1]: at least 0.641,
0.292, 0.193, 0.101. Pieces: 4–16/5: 0.01464 · 3.119 ≥ 0.0456; 16/5–13/5: 0.02753 · 1.857 ≥ 0.0511; 13/5–11/5:
0.04847 · 0.9837 ≥ 0.0476; 11/5–2: 0.07451 · 0.6412 ≥ 0.0477; 2–19/10: 0.09375 · 0.5229 ≥ 0.049; 19/10–17/10:
0.1054 · 0.432 ≥ 0.0455; 17/10–13/10: 0.1331 · 0.4373 ≥ 0.0582; 13/10–6/5: 0.1768 · 0.3101 ≥ 0.0548. Also
φ′ − q = η(12 − 5y)/3 > 0; d log(η(12 − 5y))/dy ≥ 3 − 2 − 5/9.5 > 0 on [1/16, 1/2] and η(12 − 5y)/3 > 0.5 on
[1/2, 25/36], so m′ = (15/1024)(187/48) = 2805/49152; φ′ − 2q = (2/3)η(6 − 5y) has its maximum on (0, 1) at the root
y = (55 − √505)/70 of 35y² − 55y + 18, where it is less than 0.4157.

Row T2 (a = 35/4, b = −27/4). g = 2y² gives N = 35/2 − 121y + (521/2)y² − 84y³ − 258y⁴ + 189y⁵; Bernstein on the same
four subintervals: at least 1.39, 0.316, 1.06, 0.0906. Pieces: 4–13/5: 0.01464 · 4.919 ≥ 0.072; 13/5–21/10:
0.04847 · 1.908 ≥ 0.0924; 21/10–19/10: 0.08349 · 0.9747 ≥ 0.0813; 19/10–9/5: 0.1054 · 0.6879 ≥ 0.0725; 9/5–17/10:
0.1185 · 0.5801 ≥ 0.0687; 17/10–6/5: 0.1331 · 0.5729 ≥ 0.0762. Also φ′ − q = 2η(2 − y²) > 0, increasing in y on
[1/16, 1/2] (log-derivative at least 3 − 2 − 2/3.5) and above 0.5 on [1/2, 25/36], so m′ = (15/1024)(511/128) =
7665/131072; φ′ − 2q = 4η(1 − y²) has its maximum on (0, 1) at y = (2√7 − 1)/9, the root of 9y² + 2y − 3 there,
where it is less than 0.5324.

Row T3 (V_S at l = 2, p = 5, H = 5 + 6y). Here Θ = (1 − 4y)/(1 + 2y) decreases from 1 to −1 on [0, 1], so |φ| ≤ 1,
φ → ±1 at ±∞, and φ′ = 12η/(1 + 2y)² > 0. With g = ½y(1 + y), [[eq:pb-weight-general]] gives G = N/D with
D = 4(1 + 2y)⁴(5 + 6y)³ and

    N = 8750 − 52800y − 52305y² + 661453y³ + 1153253y⁴ − 668761y⁵ − 2258994y⁶ − 1768052y⁷ − 1623176y⁸
        + 831312y⁹ + 3571104y¹⁰ + 2896704y¹¹ + 777600y¹²;

Bernstein on [0, 1/2], [1/2, 3/4], [3/4, 1]: at least 228, 27800, 34900. Pieces: 4–33/10: 0.01464 · 3.014 ≥ 0.0441;
33/10–29/10: 0.02527 · 1.742 ≥ 0.044; 29/10–27/10: 0.03612 · 1.243 ≥ 0.0448; 27/10–13/5: 0.04383 · 1.048 ≥ 0.0459;
13/5–5/2: 0.04847 · 0.9003 ≥ 0.0436; 5/2–12/5: 0.05376 · 0.793 ≥ 0.0426; 12/5–23/10: 0.05977 · 0.7024 ≥ 0.0419;
23/10–11/5: 0.06665 · 0.6601 ≥ 0.0439; 11/5–2: 0.07451 · 0.5544 ≥ 0.0413; 2–17/10: 0.09375 · 0.4985 ≥ 0.0467;
17/10–13/10: 0.1331 · 0.3475 ≥ 0.0462; 13/10–6/5: 0.1768 · 0.3621 ≥ 0.064. Also
φ′ − q = η(24 − y − 5y² − 8y³ − 4y⁴)/(2(1 + 2y)²) > 0; its logarithmic derivative is positive on [1/16, 1/4] (at least
6 − 4/3 − 0.23 − 3.56) and it exceeds 0.14 on [1/4, 25/36], so m′ is its value at y = 1/16, more than 0.1384. And
0 < φ′ − 2q = η(12 − y − 5y² − 8y³ − 4y⁴)/(1 + 2y)² ≤ 12η/(1 + 2y)², whose maximum on (0, 1) is at the root
y = (√73 − 7)/4 of 2y² + 7y − 3, where it is less than 0.563.

In every row q ≥ 0, and φ′ − q > 0 on ℝ. ∎

### Large frequencies with a fixed multiplier {#sec:morawetz-large-frequency}

**Proposition {#prop:morawetz-large-frequency}** (Every harmonic at a given frequency.) Let B_l be as in
[[prop:morawetz-resolvent-l-ge-1]]. For every real σ with |σ| ≥ 3 and every l ≥ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 6.521), B_5(σ)),

and for |σ| ≥ 6 also ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 9.271), B_6(σ)). In particular, for every l ≥ 0, the norm is at
most 23.10, 39.53, 74.89, 146.51, 290.27 and 578.04 at σ = 3, 6, 12, 24, 48 and 96.

*Proof.* max V_(a,b) ≤ a max U + b max Q = a/4 + 4b/27 for a, b ≥ 0, since U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27.
With b = 9/4 this is a/4 + 1/3: at most 6.521 for l ≤ 4 and 9.271 for l ≤ 5. When σ² exceeds max V_l, the bound above
the barrier ([[prop:resolvent-above-barrier]]) gives ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_l). So for |σ| ≥ 3 the harmonics
l ≤ 4 are bounded by Λ|σ|/(σ² − 6.521), and for |σ| ≥ 6 the harmonics l ≤ 5 by Λ|σ|/(σ² − 9.271); the others are
bounded by B_5(σ), respectively B_6(σ), as ω_l ≥ ω_5 for l ≥ 5 and ω_l ≥ ω_6 for l ≥ 6. At σ = 3 the first term is
at most 3.7436 · 3/2.479 < 4.54 and B_5(3) < 23.10; for σ ≥ 6 the first term is at most 3.7436 · 6/26.729 < 0.85, as
Λσ/(σ² − c) decreases for σ² > c, and the values given are B_6(σ), rounded up. ∎

### The resolvent bound on the band 3 ≤ |σ| ≤ 384 {#sec:band}

This section proves that the cut-off resolvent of the scalar wave operator on five-dimensional Schwarzschild–Tangherlini
with m = 1 is bounded by 11.477 for every harmonic and every real 3 ≤ |σ| ≤ 384, and derives from it the one-derivative
constants on that band. The notation is that of [[sec:morawetz-identity]]: y = 1/r², z = 1 − 2y, η = (1 − y)y^(3/2),
d/dr_* = −2η d/dy, I = {6/5 ≤ r ≤ 4} = {−7/18 ≤ z ≤ 7/8}, Λ < 3.7436 its length in r_*, U = (1 − y)y, Q = (1 − y)y²,
V_(a,b) = aU + bQ, κ = l(l + 2), and V_l = V_(κ+3/4,9/4) is the potential of the harmonic l. We also write v := 1/r, so
that y = v², η = (1 − v²)v³ and I = {1/4 ≤ v ≤ 5/6}.

Two results of [[sec:rb-radial]]–[[sec:rb-above]] are used: by [[prop:resolvent-outgoing]] (a), for real
σ ≠ 0 and F ∈ L²(ℝ) vanishing off I, u := R_l(σ)F satisfies the hypotheses of [[lem:morawetz-identity]]; and
the bound above the barrier, [[prop:resolvent-above-barrier]]: if σ² > max V_l, then
‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_l).

The route is the multiplier method of [[lem:morawetz-identity]], with two changes. The final inequality is solved exactly
and the flux term is combined with the pairing, which gives the constant B♯ of [[lem:band-sharp]]. And the multiplier is
allowed to depend on the frequency range: three multipliers polynomial in z serve 3 ≤ |σ| ≤ 14, and three members of
the algebraic family Φ(νz), Φ(x) = x(1 + x²)^(−1/2), serve 14 ≤ |σ| ≤ 384. A multiplier that is admissible for one
harmonic l_1 is admissible for every l ≥ l_1, and the harmonics below l_1 lie above their barrier, so one multiplier
covers a whole range of frequencies.

#### The multiplier bound in sharp form {#sec:band-sharp}

**Lemma {#lem:band-sharp}** (The multiplier bound in sharp form.) Let V be as in [[lem:morawetz-identity]], σ ≠ 0 real,
F ∈ L²(ℝ) vanishing off I, and u a solution, with u and u′ locally absolutely continuous, of −u″ + (V − σ²)u = F
almost everywhere, with the asymptotics stated there. Let φ be a real smooth nondecreasing function on ℝ with limits
φ(±∞), with φ′, φ″, φ‴ integrable and tending to 0 at ±∞, and suppose that w := −φV′ − ½φ‴ ≥ 0 on ℝ. Put

    m′ := min_I φ′ > 0,   M′ := max_I φ′,   w_I := min_I w > 0,   p_I := max_I |φ|,   p_∞ := max(|φ(∞)|, |φ(−∞)|).

Then ‖u‖_I ≤ B♯‖F‖, where

    B♯ := (c + (c² + 2p_I²w_I/m′)^(1/2))/(2w_I),     c := (M′² + 4σ²p_∞²)^(1/2).                    {#eq:band-sharp}

B♯ increases with |σ|, M′, p_I and p_∞, and decreases as m′ or w_I increases.

*Proof.* In the proof of [[lem:morawetz-identity]] take the Lagrangian term q = 0. The pointwise identity there,
Re(F(2φū′ + φ′ū)) = 2φ′|u′|² + w|u|² + E′, holds almost everywhere and does not use the values of φ at ±∞. Its
boundary term E = −φ|u′|² − φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² is locally absolutely continuous, since u and u′ are,
and it tends to −2σ²φ(±∞)|c_±|² at ±∞, since |u′|² → σ²|c_±|², |u|² → |c_±|² and φ′, φ″, V → 0. Integrating over
[−R, R], where ∫E′ = E(R) − E(−R), and letting R → ∞ (the integrand on the left is nonnegative, F vanishes off I),

    ∫(2φ′|u′|² + w|u|²) = Re∫F(2φū′ + φ′ū) + 2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²).                    {#eq:band-identity}

The last term is at most 2σ²p_∞(|c_+|² + |c_−|²), and by the flux identity σ(|c_+|² + |c_−|²) = −Im∫Fū of
[[lem:morawetz-identity]] this equals −2σp_∞Im∫Fū = Re∫F · conj(−2iσp_∞u). So, with X := ‖u′‖_I and Y := ‖u‖_I, since
both integrands on the left are nonnegative and F vanishes off I,

    2m′X² + w_IY² ≤ Re∫_I F · conj(2φu′ + (φ′ − 2iσp_∞)u) ≤ ‖F‖(2p_IX + cY),

because |φ| ≤ p_I on I and |φ′ − 2iσp_∞| = (φ′² + 4σ²p_∞²)^(1/2) ≤ c there. For every real X,
2m′X² − 2p_I‖F‖X ≥ −p_I²‖F‖²/(2m′); hence w_IY² − c‖F‖Y − p_I²‖F‖²/(2m′) ≤ 0, and Y is at most the positive root of
this quadratic, which is B♯‖F‖. Finally B♯ = c/(2w_I) + (c²/(4w_I²) + p_I²/(2m′w_I))^(1/2), which gives the
monotonicity. ∎

Since every hypothesis and the constant depend on σ only through |σ|, every bound below is even in σ.

**Lemma {#lem:band-barrier}** (Harmonics above the barrier.) For every l ≥ 0, max V_l ≤ κ/4 + 25/48. Consequently, if
σ² > κ/4 + 25/48, then ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − κ/4 − 25/48), which decreases as |σ| increases; and if
σ² − κ/4 − 25/48 ≥ |σ|/2, then ‖χ_I R_l(σ) χ_I‖ ≤ 2Λ < 7.4872.

*Proof.* U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27 on [0, 1], so V_l ≤ (κ + 3/4)/4 + (9/4)(4/27) = κ/4 + 25/48. The
bound above the barrier ([[prop:resolvent-above-barrier]]) then gives the first estimate, and t ↦ Λt/(t² − C)
decreases for t² > C, its derivative being −Λ(t² + C)/(t² − C)². The last statement is the first with
σ² − κ/4 − 25/48 ≥ |σ|/2. ∎

#### The weight of a multiplier in the variable z {#sec:band-weights}

**Lemma {#lem:band-weight-z}** (The weight in the variable z.) Let Θ be a smooth function of z ∈ [−1, 1] and
φ := Θ(z(r_*)). Then φ′ = 4ηΘ_z, and for V = V_(a,b) the weight w := −φV′ − ½φ‴ is w = ηG with

    G = 2ΘV_y − ½Ξ_zzΘ_z − (3/2)Ξ_zΘ_zz − ΞΘ_zzz,     Ξ := (1 + z)²(1 − z)³,
    V_y = az + (b/4)(1 − z)(1 + 3z),
    Ξ_z = −(1 + z)(1 − z)²(1 + 5z),     Ξ_zz = 4(1 − z)(5z² + 2z − 1).                              {#eq:band-weight-z}

If Θ has the sign of z, then for a ≥ a′ the weights of V_(a,b) and V_(a′,b) satisfy G_(a,b) − G_(a′,b) = 2(a − a′)zΘ ≥ 0.

*Proof.* [[eq:pb-weight-general]] with g = 0 gives φ′ = −2ηΘ_y and G = 2ΘV_y + 4(η(ηΘ_y)_y)_y. Since
η(ηΘ_y)_y = ½(η²)_yΘ_y + η²Θ_yy, the second term is 2(η²)_yyΘ_y + 6(η²)_yΘ_yy + 4η²Θ_yyy. As y = (1 − z)/2 and
1 − y = (1 + z)/2, η² = (1 − y)²y³ = Ξ/32; and d/dy = −2 d/dz, so (η²)_y = −Ξ_z/16, (η²)_yy = Ξ_zz/8, Θ_y = −2Θ_z,
Θ_yy = 4Θ_zz and Θ_yyy = −8Θ_zzz. Substituting gives [[eq:band-weight-z]] and φ′ = 4ηΘ_z. The formulas for Ξ_z and
Ξ_zz follow by differentiating Ξ, and V_y = a(1 − 2y) + by(2 − 3y) with y(2 − 3y) = (1 − z)(1 + 3z)/4 (as in the proof
of [[prop:morawetz-weight]]). G is affine in a, and the coefficient of a is 2zΘ. ∎

#### Polynomial multipliers for 3 ≤ |σ| ≤ 14 {#sec:band-polynomial}

**Proposition {#prop:band-polynomial}** (Three polynomial multipliers.) Let (l_1, Ψ, w_*, m_*, m^*) be one of the rows
Ψ_5, Ψ_7, Ψ_11 of [[sec:tb2-polynomial-multipliers]], put Θ := zΨ(z), and let p_I and p_∞ be the values listed there.
Then for every l ≥ l_1 the multiplier φ := Θ(z(r_*)) satisfies the hypotheses of [[lem:band-sharp]] with V = V_l, and
min_I w ≥ w_*, m′ ≥ m_*, M′ ≤ m^*. Hence, for every real σ ≠ 0 and every l ≥ l_1,

    ‖χ_I R_l(σ) χ_I‖ ≤ B♯(σ),   B♯ the constant [[eq:band-sharp]] with w_I = w_*, m′ = m_*, M′ = m^* and p_I, p_∞.

*Proof.* Every claim below is the positivity of one of the six polynomials (items 1–6) of [[sec:tb2-bernstein]] on an
interval, which that section cuts into pieces. Each polynomial is given there exactly, and on each piece the section
prints every Bernstein coefficient b_0, …, b_n of [[lem:bernstein-lower-bound]] (n the degree of the polynomial),
rounded down. Every printed value is positive and at most the coefficient it stands for, so every b_k is positive, and
by [[lem:bernstein-lower-bound]] the polynomial is at least min_k b_k > 0 on the piece. The pieces of each item cover
its interval.

The sign and the monotonicity. Ψ > 0 on [−1, 1] (item 1), so Θ has the sign of z. Θ_z ≥ 0 on [−1, 1] (item 2), so
φ′ = 4ηΘ_z ≥ 0 and φ is nondecreasing, with φ(∞) = Θ(1) = Ψ(1) and φ(−∞) = Θ(−1) = −Ψ(−1). As Θ is a polynomial in y,
φ′, φ″ and φ‴ are η times polynomials in y and y^(1/2); they are O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence
integrable and vanishing at ±∞.

Positivity of the weight. By [[lem:band-weight-z]], w_l = ηG_l with G_l the weight polynomial for a = κ + 3/4, and at
l = l_1 this is the polynomial G_(l_1) listed in [[sec:tb2-polynomial-multipliers]] (expanding [[eq:band-weight-z]] with
Θ = zΨ gives its coefficients). G_(l_1) ≥ 0 on [−1, 1] (item 3), and since Θ has the sign of z,
G_l ≥ G_(l_1) for l ≥ l_1 by [[lem:band-weight-z]]. So w_l ≥ w_(l_1) ≥ 0 on ℝ.

The constants on I. On I, v ∈ [1/4, 5/6], η = (1 − v²)v³ and z = 1 − 2v², so w_(l_1) − w_* and φ′ − m_*, m^* − φ′ are
the polynomials in v of items 4, 5 and 6. Their positivity gives min_I w_l ≥ min_I w_(l_1) ≥ w_* and
m_* ≤ φ′ ≤ m^* on I. Since Θ increases with z, on I it takes values in [Θ(−7/18), Θ(7/8)], so max_I |φ| = p_I; and
max(|φ(∞)|, |φ(−∞)|) = max(Ψ(1), Ψ(−1)) = p_∞. [[lem:band-sharp]] gives the bound. ∎

#### The algebraic multipliers for 14 ≤ |σ| ≤ 384 {#sec:band-algebraic}

Let Φ(x) := x(1 + x²)^(−1/2), so that Φ′ = (1 + x²)^(−3/2), Φ″ = −3x(1 + x²)^(−5/2) and Φ‴ = (12x² − 3)(1 + x²)^(−7/2).
For ν > 0 put Θ_ν(z) := Φ(νz), x := νz and s := 1 + x². Φ is odd and increasing with |Φ| < 1.

**Lemma {#lem:band-algebraic-weight}** (The weight of Θ_ν.) For V = V_(a,9/4) the weight of Θ_ν is w = ηG with

    G = 2s^(−7/2)((a/ν)x²s³ + R_ν(x)),
    R_ν(x) := (9/16)(1 − z)(1 + 3z)xs³ + ν(1 − z)(1 − 2z − 5z²)s² − (9/4)ν²(1 + z)(1 − z)²(1 + 5z)xs
              + (ν³/2)(3 − 12x²)(1 + z)²(1 − z)³,     z = x/ν.                                       {#eq:band-r}

Expanding in powers of x,

    R_ν(x) = ν³(3/2 − 6x²) + (15/4)ν²(x³ − x) + ν(4x⁴ − 10x² + 1) + (1/16)(9x⁷ + 3x⁵ + 195x³ − 39x)
             + (1/(8ν))(9x⁸ + 27x⁶ + 63x⁴ − 15x²)
             − (1/(16ν²))(27x⁹ + 85x⁷ + 125x⁵ − 53x³).                                           {#eq:band-r-expanded}

*Proof.* Θ_z = νΦ′(x) = νs^(−3/2), Θ_zz = ν²Φ″(x) = −3ν²xs^(−5/2) and Θ_zzz = ν³(12x² − 3)s^(−7/2). Substituting
these, Θ = xs^(−1/2) and V_y = (a/ν)x + (9/16)(1 − z)(1 + 3z) into [[eq:band-weight-z]] and multiplying by s^(7/2),

    Gs^(7/2) = 2xs³V_y − ½νΞ_zz s² + (9/2)ν²xΞ_z s − ν³(12x² − 3)Ξ.

With the formulas for Ξ, Ξ_z and Ξ_zz of [[eq:band-weight-z]], the term 2xs³ · (a/ν)x is 2(a/ν)x²s³ and the remaining
terms are 2R_ν(x). Substituting z = x/ν into [[eq:band-r]] and collecting powers of x gives [[eq:band-r-expanded]]. ∎

**Lemma {#lem:band-positivity}** (Positivity of the core polynomial.) Let 2 ≤ ν ≤ 12 and A_ν := 6ν⁴ + (17/2)ν³. Then

    R_ν(x) + (A_ν/ν)x²(1 + x²)³ ≥ ν³     for every real x with |x| ≤ ν.                    {#eq:band-positivity}

*Proof.* Put μ := 1/ν ∈ [1/12, 1/2] and 𝒬 := ν⁻³(R_ν(x) + (A_ν/ν)x²(1 + x²)³) − 1. Since A_ν/ν = (6 + 17μ/2)ν³,
[[eq:band-r-expanded]] gives 𝒬 = e_0 + μe_1 + μ²e_2 + μ³e_3 + μ⁴e_4 + μ⁵e_5 with

    e_0 = 1/2 + 18x⁴ + 18x⁶ + 6x⁸,            e_1 = −(15/4)x + (17/2)x² + (15/4)x³ + (51/2)(x⁴ + x⁶) + (17/2)x⁸,
    e_2 = 1 − 10x² + 4x⁴,                      e_3 = (1/16)(−39x + 195x³ + 3x⁵ + 9x⁷),
    e_4 = (1/8)(−15x² + 63x⁴ + 27x⁶ + 9x⁸),    e_5 = (1/16)(53x³ − 125x⁵ − 85x⁷ − 27x⁹);

here e_0 = 3/2 − 6x² + 6x²(1 + x²)³ − 1 and e_1 = (15/4)(x³ − x) + (17/2)x²(1 + x²)³.

Case 0 ≤ x ≤ 1. Dropping nonnegative terms, e_0 ≥ 1/2 + 18x⁴, e_1 ≥ −(15/4)x + (17/2)x², e_2 ≥ 1 − 10x²,
e_3 ≥ −(39/16)x and e_4 ≥ −(15/8)x². As x ≤ 1, 125x⁵ + 85x⁷ + 27x⁹ − 53x³ ≤ 184x³ ≤ 184x², so e_5 ≥ −(23/2)x². Hence

    𝒬 ≥ 1/2 + μ² − β_1x + β_2x² + 18x⁴,
    β_1 := (15/4)μ + (39/16)μ³,     β_2 := (17/2)μ − 10μ² − (15/8)μ⁴ − (23/2)μ⁵.

β_1 increases with μ, so β_1 ≤ β_1(1/2) = 279/128. β_2 is concave in μ ≥ 0, so on [1/12, 1/2] it is at least
min(β_2(1/12), β_2(1/2)) = min(0.63875…, 1.2734…) > 0.6387. And 18x⁴ ≥ (9/4)x² − 9/128, since 18(x² − 1/16)² ≥ 0. So
𝒬 ≥ γ_0 − (279/128)x + γ_2x² with γ_0 := 1/2 + 1/144 − 9/128 > 0.4366 and γ_2 := 0.6387 + 9/4 = 2.8887. This quadratic
has positive leading coefficient and discriminant (279/128)² − 4γ_0γ_2 < 4.7512 − 5.0448 < 0, so 𝒬 > 0.

Case −1 ≤ x < 0. Put ξ := −x ∈ (0, 1]. Then e_0 ≥ 1/2, e_1 = (15/4)ξ(1 − ξ²) + (17/2)ξ² + (51/2)(ξ⁴ + ξ⁶) +
(17/2)ξ⁸ ≥ (17/2)ξ², e_2 ≥ 1 − 10ξ², e_3 = (ξ/16)(39 − 195ξ² − 3ξ⁴ − 9ξ⁶) ≥ −(207/16)ξ³ ≥ −(207/16)ξ²,
e_4 ≥ −(15/8)ξ² and e_5 = (ξ³/16)(−53 + 125ξ² + 85ξ⁴ + 27ξ⁶) ≥ −(53/16)ξ². Hence 𝒬 ≥ 1/2 + μ² − β_3ξ², with
β_3 := 10μ² + (207/16)μ³ + (15/8)μ⁴ + (53/16)μ⁵ − (17/2)μ. β_3 is convex in μ ≥ 0, so on [1/12, 1/2] it is at most
max(β_3(1/12), β_3(1/2)) = β_3(1/2) = 45/512, as β_3(1/12) < 0. As μ² ≥ 0 and ξ² ≤ 1,
𝒬 ≥ 1/2 − max(β_3, 0)ξ² ≥ 1/2 − 45/512 > 0.

Case 1 ≤ |x| ≤ ν. Here x² ≥ 1, μ ≤ 1/2 and μ|x| ≤ 1. First e_1 ≥ 0: for x ≥ 1, (15/4)(x³ − x) ≥ 0 and the other terms
are nonnegative; for x ≤ −1, with ξ = −x, e_1 ≥ (17/2)ξ² + (51/2)ξ⁴ − (15/4)ξ³ ≥ 0, as ξ³ ≤ (ξ² + ξ⁴)/2. Next, using
μ|x| ≤ 1 to trade a power of μ for a power of |x|, and μ ≤ 1/2,

    μ²e_2 ≥ −10μ²x² ≥ −(5/2)x²,                        μ⁴e_4 ≥ −(15/8)μ⁴x² ≥ −(15/128)x²,
    μ³|e_3| ≤ (μ²/16)(39 + 195x² + 3x⁴ + 9x⁶) ≤ (1/64)(39 + 195x² + 3x⁴ + 9x⁶),
    μ⁵|e_5| ≤ (μ⁴/16)(53x² + 125x⁴ + 85x⁶ + 27x⁸) ≤ (1/256)(53x² + 125x⁴ + 85x⁶ + 27x⁸).

Adding these to e_0,

    𝒬 ≥ 1/2 − 39/64 − (1503/256)x² + (18 − 137/256)x⁴ + (18 − 121/256)x⁶ + (6 − 27/256)x⁸ ≥ −7/64 − 6x² + 17x⁴,

and −7/64 − 6x² + 17x⁴ ≥ −7/64 + 11x² > 0 since x⁴ ≥ x². In every case 𝒬 > 0, which is [[eq:band-positivity]]. ∎

**Lemma {#lem:band-algebraic-constants}** (The algebraic multiplier on I.) Let 2 ≤ ν ≤ 12, let a ≥ A_ν + (7/2)ν⁴ and
put α := (a − A_ν)/ν ≥ (7/2)ν³. Then φ := Θ_ν(z(r_*)) satisfies the hypotheses of [[lem:band-sharp]] for
V = V_(a,9/4), with

    m′ = (15ν/256)(1 + 49ν²/64)^(−3/2),   M′ ≤ 0.74362ν,   p_I = Φ(7ν/8),   p_∞ = Φ(ν),

and, for every τ ∈ (0, 7/8), with h_ν(z) := ηz²(1 + ν²z²)^(−1/2) and η = 2^(−5/2)(1 + z)(1 − z)^(3/2),

    w_I ≥ min{2ν³ min(η(τ), 1375/7776), 2αν² min(h_ν(τ), h_ν(7/8))},   h_ν(7/8) = (735/65536)(1 + 49ν²/64)^(−1/2).
                                                                                                  {#eq:band-wi}

*Proof.* The hypotheses. φ′ = 4ηΘ_z = 4νηΦ′(νz) > 0 ([[lem:band-weight-z]]), so φ increases, from −Φ(ν) at −∞ to
Φ(ν) at ∞. Θ_ν is a smooth function of y on [0, 1], so φ′, φ″ and φ‴ are η times bounded functions of y; they are
O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

The weight. Since a/ν = A_ν/ν + α, [[lem:band-algebraic-weight]] and [[lem:band-positivity]] give, on ℝ,

    w = 2ηs^(−7/2)(αx²s³ + (A_ν/ν)x²s³ + R_ν(x)) ≥ 2ηk(x²),   k(u) := αu(1 + u)^(−1/2) + ν³(1 + u)^(−7/2),

as |x| = ν|z| ≤ ν. So w > 0 on ℝ. Moreover k′(u) = (1 + u)^(−9/2)(α(1 + u)³(1 + u/2) − (7/2)ν³) ≥ 0 because
α ≥ (7/2)ν³, so k ≥ k(0) = ν³; and k ≥ αu(1 + u)^(−1/2). Hence w ≥ 2η max(ν³, αν²z²(1 + ν²z²)^(−1/2)).

The weight on I. As a function of z, η increases on [−1, −1/5] and decreases on [−1/5, 1], since η increases with y
on [0, 3/5] and decreases on [3/5, 1] ([[sec:morawetz-identity]]). So on [−7/18, τ], η ≥ min(η(−7/18), η(τ)), and
η(−7/18) = η(y = 25/36) = 1375/7776; there w ≥ 2ν³ min(η(τ), 1375/7776). On [τ, 7/8], w ≥ 2αν²h_ν(z), and h_ν is
log-concave on (0, 1):

    (log h_ν)″ = −1/(1 + z)² − 3/(2(1 − z)²) − 2/z² + ν²(ζ − 1)/(1 + ζ)²,     ζ := ν²z²,

and ν²(ζ − 1)/(1 + ζ)² = z⁻²ζ(ζ − 1)/(1 + ζ)² < z⁻², so (log h_ν)″ < −z⁻² < 0. So on [τ, 7/8], h_ν ≥ min(h_ν(τ),
h_ν(7/8)). At z = 7/8, η = η(y = 1/16) = 15/1024 and z² = 49/64, which gives h_ν(7/8). This is [[eq:band-wi]].

The constants. φ′ = 4νη(1 + ν²z²)^(−3/2). On y ∈ [1/16, 1/2] (z ∈ [0, 7/8]),
d(log φ′)/dy = 3/(2y) − 1/(1 − y) + 6ν²z/(1 + ν²z²) ≥ 3 − 2 > 0, so there
φ′ ≥ φ′(y = 1/16) = 4ν(15/1024)(1 + 49ν²/64)^(−3/2).
On y ∈ [1/2, 25/36], η ≥ 2^(−5/2) ([[sec:morawetz-identity]]) and |z| ≤ 7/18, so φ′ ≥ 4ν2^(−5/2)(1 + 49ν²/324)^(−3/2),
which is larger, as 4 · 2^(−5/2) > 15/256 and 49/324 < 49/64. This gives m′. Next φ′ ≤ 4ν max η = 4ν · 6√15/125 <
0.74362ν (as in [[prop:morawetz-resolvent-l-ge-1]]). Since Φ is odd and increasing, max_I |φ| = max(Φ(7ν/8), Φ(7ν/18))
= Φ(7ν/8), and |φ(±∞)| = Φ(ν). ∎

#### The band {#sec:band-theorem}

**Theorem {#thm:band}** (The resolvent on the band.) For every harmonic l ≥ 0 and every real σ with 3 ≤ |σ| ≤ 384,

    ‖χ_I R_l(σ) χ_I‖ ≤ 11.477.

*Proof.* All bounds used are even in σ, so let 3 ≤ σ ≤ 384. We cover [3, 384] by six ranges. In each, one multiplier
serves every harmonic from some l_1 on, and [[lem:band-barrier]] serves the harmonics below l_1. B♯ increases with σ
([[lem:band-sharp]]) and the barrier bound decreases, so on a range [σ_a, σ_b] it suffices to evaluate B♯ at σ_b and
the barrier bound at σ_a.

(a) 3 ≤ σ ≤ 15/4, the multiplier zΨ_5 of [[prop:band-polynomial]], l_1 = 5. With the constants of
[[sec:tb2-polynomial-multipliers]] (w_* = 0.87, m_* = 0.0455, m^* = 0.75, p_I < 0.99673, p_∞ = 43/40), B♯(15/4) < 10.51.
For l ≤ 4, κ ≤ 24 and the barrier bound at σ = 3 is 3.7436 · 3/(9 − 313/48) < 4.531.

(b) 15/4 ≤ σ ≤ 6, the multiplier zΨ_7, l_1 = 7. B♯(6) < 9.261 (w_* = 1.30, m_* = 0.031, m^* = 0.74, p_I < 0.83442,
p_∞ = 9/10). For l ≤ 6, κ ≤ 48 and the barrier bound at σ = 15/4 is 3.7436 · (15/4)/(225/16 − 601/48) < 9.107.

(c) 6 ≤ σ ≤ 14, the multiplier zΨ_11, l_1 = 11. B♯(14) < 9.544 (w_* = 1.80, m_* = 0.0210, m^* = 0.72, p_I < 0.50776,
p_∞ = 59/100). For l ≤ 10, κ ≤ 120 and the barrier bound at σ = 6 is 3.7436 · 6/(36 − 1465/48) < 4.100.

(d)–(f) 14 ≤ σ ≤ 384, the algebraic multipliers Θ_ν of [[lem:band-algebraic-constants]] with ν = 11/4 on [14, 28],
ν = 4 on [28, 108] and ν = 6 on [108, 384]. For σ in a range [σ_a, σ_b], let l_1(σ) be the least l with
κ/4 + 25/48 > σ² − σ/2. For l < l_1(σ), [[lem:band-barrier]] gives the bound 2Λ < 7.4872. For l ≥ l_1(σ),
κ > 4σ² − 2σ − 25/12, so a = κ + 3/4 > 4σ² − 2σ − 4/3 ≥ a_* := 4σ_a² − 2σ_a − 4/3, as 4σ² − 2σ increases for σ ≥ 1/4.
The rows of [[sec:tb2-algebraic-rows]] show a_* ≥ A_ν + (7/2)ν⁴ in each range, so [[lem:band-algebraic-constants]]
applies to every such l, with α ≥ (a_* − A_ν)/ν (the lower bound [[eq:band-wi]] increases with α). With the τ and the
constants listed there, B♯(σ_b) is less than 10.297, 10.579 and 10.381 in the three ranges.

So for every l ≥ 0 and 3 ≤ |σ| ≤ 384 the norm is at most
max(10.51, 9.261, 9.544, 10.297, 10.579, 10.381, 4.531, 9.107, 4.100, 7.4872) = 10.579 < 11.477. ∎

The six ranges, with the bound for the harmonics served by each multiplier and for those below it:

| range of σ | multiplier | harmonics it serves | multiplier bound ≤ | harmonics below: bound ≤ |
|---|---|---|---|---|
| [3, 15/4] | zΨ_5 | l ≥ 5 | 10.51 | 4.531 |
| [15/4, 6] | zΨ_7 | l ≥ 7 | 9.261 | 9.107 |
| [6, 14] | zΨ_11 | l ≥ 11 | 9.544 | 4.100 |
| [14, 28] | Θ_(11/4) | l ≥ l_1(σ) | 10.297 | 7.4872 |
| [28, 108] | Θ_4 | l ≥ l_1(σ) | 10.579 | 7.4872 |
| [108, 384] | Θ_6 | l ≥ l_1(σ) | 10.381 | 7.4872 |

Together with [[prop:morawetz-resolvent-l-ge-1]] and [[prop:morawetz-l-zero]], which bound every harmonic for
0 < |σ| ≤ 3, this bounds ‖χ_I R_l(σ) χ_I‖ uniformly in l for every real 0 < |σ| ≤ 384.

**Proposition {#prop:band-points}** (Sampled frequencies.) For every harmonic l ≥ 0, ‖χ_I R_l(σ) χ_I‖ is at most
8.878, 4.683, 5.990, 4.097, 3.022 and 2.252 at |σ| = 3, 6, 12, 24, 48 and 96; at most 2.024, 1.869 and 1.743 at
|σ| = 128, 160 and 192; and at most 1.677, 1.815 and 1.963 for every |σ| in [s − 1/20, s] with s = 256, 320 and 384.

*Proof.* At |σ| = 3, [[prop:band-polynomial]] with zΨ_5 gives B♯(3) < 8.878 for l ≥ 5, and [[lem:band-barrier]] gives
4.531 for l ≤ 4. At |σ| = 6, zΨ_11 gives B♯(6) < 4.683 for l ≥ 11 and [[lem:band-barrier]] gives 4.100 for l ≤ 10. At
the other frequencies, take the row of [[sec:tb2-points]]: the multiplier Θ_ν of [[lem:band-algebraic-constants]] with
the listed ν and τ, applied with a at l = l_1 (a larger a only increases α), serves every l ≥ l_1, and gives the listed
B♯ at the right end σ_+; [[lem:band-barrier]] at the left end σ_- gives the listed bound for every l < l_1. ∎

**Remark {#rem:band-observed}** (Numerical observation.) A numerical optimisation over multipliers that are narrow at
the photon sphere and wide in the flanks, one multiplier for each l_1 = 5, …, 768, with the bound evaluated in interval
arithmetic on the 7,620 subintervals of width 1/20 of [3, 384], gives for every l ≥ 0 the bounds 3.7719, 2.3724,
1.5222 and 0.99697 at |σ| = 12, 24, 48 and 96, and 0.83951, 0.73083, 0.66429, 0.56257, 0.49119 and 0.47635 on the
subintervals ending at |σ| = 128, 160, 192, 256, 320 and 384 (0.43792 at 384 when more multipliers are admitted); its
largest value on [3, 384] is 11.477, on [3.2, 3.25]. These values times |σ|^(1/2) are 9.77, 9.20 and 8.58 at
|σ| = 96, 192 and 384 (the last with 0.43792), so between |σ| = 96 and 384 they decay roughly like |σ|^(−0.6); the
scaling of the best multiplier at the trapped harmonic (the l with max V_l nearest σ²) suggests |σ|^(−1/2) for larger
|σ|. These values are not proved here ([[prop:band-points]] proves weaker ones from |σ| = 12 on), and no proof uses
them.

#### One derivative on the band {#sec:band-one-derivative}

**Corollary {#cor:band-one-derivative}** (The one-derivative constants on the band.) Let 3 ≤ |σ| ≤ 384. For F ∈ L²(ℝ)
vanishing off I and u = R_l(σ)F,

    ‖u′‖_I ≤ 283.06‖F‖ for every l ≥ 1,        ‖u′‖_I ≤ 305.31‖F‖ for l = 0;

in particular ‖u′‖_I ≤ 963.4‖F‖ for l ≥ 1 and ≤ 1516‖F‖ for l = 0. For F ∈ L²(I × 𝕊³), extended by zero to
ℝ × 𝕊³, with harmonic components F_l (the components of F in the eigenspaces of the Laplacian of 𝕊³ with eigenvalue
−κ, which are orthogonal), put u_l := R_l(σ)F_l, acting in r_*, and u := Σ_l u_l; by [[thm:band]] and the first bound
the series and its r_*-derivative converge in L² on I × 𝕊³. Then, with the norms taken on I × 𝕊³, ψ = 2ηz² the weight
of [[prop:morawetz-weight]] and the angular term at l = 1 taken unweighted,

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖F‖²,     C ≤ 308.46.

*Proof.* By [[thm:band]], B̃ := 11.477 bounds ‖u‖_I/‖F‖ for every l. [[lem:morawetz-identity]] then gives ‖u′‖_I ≤
X(B̃)‖F‖ with X(B̃) = (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′), where (m′, M′) = (15/256, 0.74362) for l ≥ 1, the
constants of φ = 1 − 2/r² and q = 0 ([[prop:morawetz-resolvent-l-ge-1]]), and (m′, M′) = (3315/65536, 0.3999) at
l = 0, those of φ = 1 − 2/r² and q = ½η(1 + 3y/2) ([[prop:morawetz-l-zero]]). X(B̃) increases with |σ|, so its value
at |σ| = 384 bounds the band: for l ≥ 1,
2m′(M′ + 768)B̃ = (15/128)(768.74362)(11.477) < 1033.94, whose increment by 1 has square root less than 32.171, so
X < (1 + 32.171)/(15/128) < 283.06; at l = 0, 2m′(M′ + 768)B̃ = (3315/32768)(768.3999)(11.477) < 892.18, whose
increment by 1 has square root less than 29.8862, so X_0 < (1 + 29.8862)(32768/3315) < 305.31.

For the sum, [[cor:morawetz-one-derivative]] (a) with B_l replaced by B̃ gives, for l ≥ 2,
κ∫_I ψ|u_l|² ≤ (κ/(κ − 3))J‖F_l‖², J := 2X(B̃) + (M′ + 2|σ|)B̃ < 566.12 + 8822.88 < 9389.0, and κ/(κ − 3) ≤ 8/5 as
κ ≥ 8. So for l ≥ 2 the harmonic contributes at most (283.06² + (8/5)(9389.0))‖F_l‖² < 308.46²‖F_l‖²; for l = 1 at
most (283.06² + 3B̃²)‖F_1‖² < 283.76²‖F_1‖²; and for l = 0 at most 305.31²‖F_0‖². Summing over l, with
‖∂_(r_*)u‖_I² = Σ_l‖u_l′‖_I² and ‖F‖² = Σ_l‖F_l‖² by the orthogonality of the harmonics, gives C ≤ 308.46. ∎

**Remark {#rem:rb-large-frequency-observed}** (Numerical observation.) The cut-off norm ‖χ_I R_l(σ) χ_I‖, computed from
numerical solutions of the radial equation (with at least 40 grid points per wavelength) and maximised over l, is
1.132, 0.618, 0.336, 0.181, 0.0972 and 0.0519 at σ = 3, 6, 12, 24, 48 and 96, attained at l = 5, 11, 23, 47, 95 and
191: in every case the first harmonic with max V_l > σ², the one trapped at the photon sphere. At these σ, σ times the
maximum is 2.887 + 0.459 log σ to within 0.004; between them the maximum oscillates in σ with a period of about 1/2,
the spacing of the barrier tops, and near σ = 12 it lies up to about 1.7 % above that fit. At σ = 128 and 160 it is
0.0399913 and 0.0326365 (l = 255 and 319). So the bounds of [[prop:band-points]] lie between 7.5 and 58 times above
these values at the sampled frequencies, the ratio growing with σ. With one multiplier of fixed width for every
frequency, the bound of [[lem:morawetz-identity]] grows instead like |σ|: maximised over l, with the best of forty tanh
widths at each σ, it is 253, 429, 800, 1554, 3068 and 6099 at σ = 3, 6, 12, 24, 48 and 96, set by l = 1. No proof uses
these values.

### Tables for the resolvent bound on the band {#sec:tb2}

These tables carry the numbers used by [[prop:band-polynomial]], [[thm:band]], [[prop:band-points]] and
[[cor:band-one-derivative]]. The notation is that of [[sec:band]]: y = 1/r², z = 1 − 2y, v := 1/r = y^(1/2),
η = (1 − y)y^(3/2) = (1 − v²)v³, I = {1/4 ≤ v ≤ 5/6} = {−7/18 ≤ z ≤ 7/8}, κ = l(l + 2) and a = κ + 3/4. The Bernstein
coefficients of a polynomial p on a piece are the numbers b_0, …, b_n of [[lem:bernstein-lower-bound]], with that piece
as the interval there and n the degree of p.

#### The polynomial multipliers {#sec:tb2-polynomial-multipliers}

Each multiplier is Θ(z) := zΨ(z), with Ψ a polynomial with rational coefficients, and is used for every harmonic
l ≥ l_1; the three rows are named Ψ_5, Ψ_7 and Ψ_11 after their l_1. G_(l_1) is the weight polynomial of
[[lem:band-weight-z]] for V = V_(a,9/4) at a = κ + 3/4, l = l_1; it is listed by its coefficients of z⁰, z¹, … .
w_*, m_* and m^* are the bounds asserted for min_I w, min_I φ′ and max_I φ′.

| name | l_1 | Ψ(z) | w_* | m_* | m^* |
|---|---|---|---|---|---|
| Ψ_5 | 5 | 1 + (11/20)z − (1/4)z² − (9/40)z³ | 0.87 | 0.0455 | 0.75 |
| Ψ_7 | 7 | 1 + (29/50)z − (33/50)z² − (11/25)z³ + (21/50)z⁴ | 1.30 | 0.031 | 0.74 |
| Ψ_11 | 11 | 1 + (8/25)z − (137/100)z² − (31/100)z³ + (19/20)z⁴ | 1.80 | 0.0210 | 0.72 |

| name | G_(l_1)(z): coefficients of z⁰, z¹, …, z⁷ |
|---|---|
| Ψ_5 | 103/20, 223/40, 4627/160, 829/32, 3469/64, −9, −2169/64 (degree 6) |
| Ψ_7 | 77/10, 1013/200, 11073/400, 8331/80, 12481/80, −3873/20, −4999/50, 43113/400 |
| Ψ_11 | 559/50, −2573/200, 13051/100, 200819/800, −9349/800, −2357/5, 4651/160, 39007/160 |

Values of Θ at the ends of ℝ (z = ±1) and of I (z = 7/8, −7/18), and the resulting p_∞ = max(Θ(1), −Θ(−1)) and
p_I = max(Θ(7/8), −Θ(−7/18)):

| name | Θ(1) | −Θ(−1) | Θ(7/8) | −Θ(−7/18) | p_∞ | p_I |
|---|---|---|---|---|---|---|
| Ψ_5 | 43/40 | 17/40 | 163303/163840 | 138173/466560 | 43/40 | 163303/163840 < 0.99673 |
| Ψ_7 | 9/10 | 31/50 | 1367107/1638400 | 1739381/6298560 | 9/10 | 1367107/1638400 < 0.83442 |
| Ψ_11 | 59/100 | 57/100 | 1663809/3276800 | 52049963/188956800 | 59/100 | 1663809/3276800 < 0.50776 |

#### Bernstein data for the polynomial multipliers {#sec:tb2-bernstein}

For each multiplier, the six polynomials below are positive on every listed piece. The first three are in the variable
z on [−1, 1]; the last three are in the variable v on [1/4, 5/6], obtained by substituting z = 1 − 2v².

1. Ψ(z), degree 3 (Ψ_5) or 4 (Ψ_7, Ψ_11).
2. Θ_z(z) = Ψ(z) + zΨ_z(z), of the same degree as Ψ.
3. G_(l_1)(z), degree 6 (Ψ_5) or 7 (Ψ_7, Ψ_11).
4. w_(l_1) − w_*, where w_(l_1) := (1 − v²)v³G_(l_1)(1 − 2v²) is the weight on I at l = l_1; degree 17 (Ψ_5) or 19
   (Ψ_7, Ψ_11).
5. φ′ − m_*, where φ′ = 4(1 − v²)v³Θ_z(1 − 2v²) on I; degree 11 (Ψ_5) or 13 (Ψ_7, Ψ_11).
6. m^* − φ′, of the same degree as item 5.

Items 1–3 are given exactly by the tables above. The polynomials w_(l_1) and φ′ of items 4–6 contain only odd powers of
v, from v³ on; each is the listed factor times the polynomial with the listed coefficients of v³, v⁵, v⁷, … .

| name | polynomial | factor | coefficients of v³, v⁵, v⁷, … |
|---|---|---|---|
| Ψ_5 | w_5 | 1/80 | 6149, −23685, −35745, 389341, −974980, 1182520, −717120, 173520 |
| Ψ_5 | φ′ | 1/5 | 9, 115, −400, 420, −144 |
| Ψ_7 | w_7 | 1/100 | 11475, −48123, 78009, −492941, 2788300, −7040408, 8892472, −5568400, 1379616 |
| Ψ_7 | φ′ | 1/25 | 52, −116, 2200, −7448, 8672, −3360 |
| Ψ_11 | w_11 | 1/200 | 33925, −225305, 1515511, −8691227, 28487500, −51985564, 53081160, −28457120, 6241120 |
| Ψ_11 | φ′ | 1/25 | 104, −1644, 9808, −22476, 21808, −7600 |

On each piece the table below prints every Bernstein coefficient b_0, b_1, …, b_n of the item, in order of k. Each is
rounded down to three significant digits, trailing zeros dropped, so each printed value is at most the coefficient and
equals it when the coefficient has at most three significant digits. Every printed value is positive. A list too long
for one row is split over two, each marked with its range of k.

| name | item | piece | Bernstein coefficients b_0, b_1, …, b_n |
|---|---|---|---|
| Ψ_5 | 1 | [−1, 1] | 0.425, 0.675, 1.49, 1.07 |
| Ψ_5 | 2 | [−1, 0] | 0.05, 0.0166, 0.633, 1 |
| Ψ_5 | 2 | [0, 1] | 1, 1.36, 1.48, 0.45 |
| Ψ_5 | 3 | [−1, 0] | 31.9, 26.3, 11.4, 6.85, 5.21, 4.22, 5.15 |
| Ψ_5 | 3 | [0, 1] | 5.15, 6.07, 8.93, 15, 29.2, 58.5, 76.8 |
| Ψ_5 | 4 | [1/4, 4/9], b_0–b_8 | 0.0304, 0.126, 0.225, 0.327, 0.428, 0.53, 0.629, 0.725, 0.816 |
| Ψ_5 | 4 | [1/4, 4/9], b_9–b_17 | 0.901, 0.978, 1.04, 1.1, 1.15, 1.18, 1.21, 1.22, 1.22 |
| Ψ_5 | 4 | [4/9, 23/36], b_0–b_8 | 1.22, 1.22, 1.21, 1.18, 1.15, 1.1, 1.05, 0.987, 0.918 |
| Ψ_5 | 4 | [4/9, 23/36], b_9–b_17 | 0.843, 0.765, 0.686, 0.607, 0.531, 0.457, 0.388, 0.324, 0.267 |
| Ψ_5 | 4 | [23/36, 5/6], b_0–b_8 | 0.267, 0.209, 0.158, 0.113, 0.0764, 0.0468, 0.0249, 0.0106, 0.00399 |
| Ψ_5 | 4 | [23/36, 5/6], b_9–b_17 | 0.00504, 0.014, 0.0315, 0.0584, 0.096, 0.145, 0.208, 0.284, 0.373 |
| Ψ_5 | 5 | [1/4, 5/6] | 0.000516, 0.0355, 0.0921, 0.178, 0.301, 0.458, 0.629, 0.768, 0.807, 0.702, 0.511, 0.316 |
| Ψ_5 | 6 | [1/4, 4/9] | 0.703, 0.692, 0.678, 0.661, 0.641, 0.618, 0.592, 0.562, 0.529, 0.493, 0.454, 0.414 |
| Ψ_5 | 6 | [4/9, 23/36] | 0.414, 0.373, 0.331, 0.287, 0.243, 0.2, 0.158, 0.12, 0.0868, 0.0592, 0.0389, 0.027 |
| Ψ_5 | 6 | [23/36, 5/6] | 0.027, 0.015, 0.0113, 0.017, 0.0328, 0.0592, 0.0959, 0.142, 0.197, 0.258, 0.323, 0.388 |
| Ψ_7 | 1 | [−1, 1] | 0.62, 0.07, 1.64, 1.09, 0.9 |
| Ψ_7 | 2 | [−1, −1/3] | 1.72, 0.293, 0.0444, 0.22, 0.484 |
| Ψ_7 | 2 | [−1/3, 1/3] | 0.484, 0.748, 1.09, 1.2, 1.12 |
| Ψ_7 | 2 | [1/3, 1] | 1.12, 1.05, 0.808, 0.466, 0.52 |
| Ψ_7 | 3 | [−1, 0] | 68, 71.5, 19, 5.27, 6.5, 7.57, 6.97, 7.7 |
| Ψ_7 | 3 | [0, 1] | 7.7, 8.42, 10.4, 16.8, 34.8, 67.3, 88.5, 114 |
| Ψ_7 | 4 | [1/4, 13/24], b_0–b_9 | 0.0575, 0.257, 0.467, 0.684, 0.904, 1.12, 1.33, 1.53, 1.71, 1.86 |
| Ψ_7 | 4 | [1/4, 13/24], b_10–b_19 | 1.99, 2.07, 2.12, 2.12, 2.08, 2, 1.88, 1.73, 1.55, 1.37 |
| Ψ_7 | 4 | [13/24, 5/6], b_0–b_9 | 1.37, 1.18, 0.99, 0.789, 0.595, 0.419, 0.269, 0.154, 0.0771, 0.037 |
| Ψ_7 | 4 | [13/24, 5/6], b_10–b_19 | 0.0283, 0.0405, 0.0599, 0.0725, 0.0689, 0.0489, 0.0255, 0.025, 0.0804, 0.219 |
| Ψ_7 | 5 | [1/4, 5/6], b_0–b_6 | 0.00128, 0.0197, 0.0472, 0.0878, 0.147, 0.234, 0.357 |
| Ψ_7 | 5 | [1/4, 5/6], b_7–b_13 | 0.516, 0.691, 0.828, 0.836, 0.66, 0.425, 0.252 |
| Ψ_7 | 6 | [1/4, 4/9] | 0.707, 0.701, 0.694, 0.686, 0.676, 0.665, 0.652, 0.637, 0.62, 0.6, 0.578, 0.553, 0.525, 0.495 |
| Ψ_7 | 6 | [4/9, 23/36], b_0–b_6 | 0.495, 0.464, 0.431, 0.395, 0.357, 0.317, 0.276 |
| Ψ_7 | 6 | [4/9, 23/36], b_7–b_13 | 0.234, 0.193, 0.153, 0.116, 0.0836, 0.057, 0.0376 |
| Ψ_7 | 6 | [23/36, 5/6], b_0–b_6 | 0.0376, 0.0182, 0.00604, 0.00245, 0.00866, 0.0256, 0.0539 |
| Ψ_7 | 6 | [23/36, 5/6], b_7–b_13 | 0.0935, 0.143, 0.202, 0.267, 0.334, 0.398, 0.456 |
| Ψ_11 | 1 | [−1, 0] | 0.57, 0.152, 0.611, 0.92, 1 |
| Ψ_11 | 1 | [0, 1] | 1, 1.08, 0.931, 0.477, 0.59 |
| Ψ_11 | 2 | [−1, −3/5] | 2.24, 0.854, 0.217, 0.00696, 0.0198 |
| Ψ_11 | 2 | [−3/5, −1/5] | 0.0198, 0.0327, 0.269, 0.526, 0.725 |
| Ψ_11 | 2 | [−1/5, 1/5] | 0.725, 0.923, 1.06, 1.06, 0.961 |
| Ψ_11 | 2 | [1/5, 3/5] | 0.961, 0.861, 0.662, 0.404, 0.252 |
| Ψ_11 | 2 | [3/5, 1] | 0.252, 0.0994, 0.0512, 0.27, 1.04 |
| Ψ_11 | 3 | [−1, 0] | 148, 105, 31.5, 26.7, 28.1, 21, 13, 11.1 |
| Ψ_11 | 3 | [0, 1] | 11.1, 9.34, 13.7, 31.4, 69.4, 111, 101, 169 |
| Ψ_11 | 4 | [1/4, 19/48], b_0–b_9 | 0.0773, 0.216, 0.359, 0.507, 0.658, 0.813, 0.971, 1.13, 1.29, 1.45 |
| Ψ_11 | 4 | [1/4, 19/48], b_10–b_19 | 1.62, 1.78, 1.95, 2.11, 2.26, 2.42, 2.57, 2.71, 2.84, 2.96 |
| Ψ_11 | 4 | [19/48, 13/24], b_0–b_9 | 2.96, 3.09, 3.2, 3.31, 3.4, 3.48, 3.54, 3.59, 3.62, 3.63 |
| Ψ_11 | 4 | [19/48, 13/24], b_10–b_19 | 3.63, 3.6, 3.56, 3.49, 3.41, 3.31, 3.19, 3.05, 2.9, 2.74 |
| Ψ_11 | 4 | [13/24, 11/16], b_0–b_9 | 2.74, 2.58, 2.4, 2.22, 2.02, 1.82, 1.62, 1.41, 1.21, 1.02 |
| Ψ_11 | 4 | [13/24, 11/16], b_10–b_19 | 0.837, 0.667, 0.512, 0.377, 0.264, 0.174, 0.109, 0.0703, 0.057, 0.0691 |
| Ψ_11 | 4 | [11/16, 5/6], b_0–b_9 | 0.0691, 0.0811, 0.118, 0.18, 0.266, 0.374, 0.502, 0.646, 0.804, 0.971 |
| Ψ_11 | 4 | [11/16, 5/6], b_10–b_19 | 1.14, 1.31, 1.49, 1.66, 1.83, 1.99, 2.14, 2.29, 2.44, 2.59 |
| Ψ_11 | 5 | [1/4, 19/48], b_0–b_6 | 0.0005, 0.00107, 0.0014, 0.00149, 0.00136, 0.00108, 0.000734 |
| Ψ_11 | 5 | [1/4, 19/48], b_7–b_13 | 0.000446, 0.000388, 0.000762, 0.0018, 0.00378, 0.00697, 0.0116 |
| Ψ_11 | 5 | [19/48, 13/24], b_0–b_6 | 0.0116, 0.0163, 0.0225, 0.0305, 0.0405, 0.0529, 0.0679 |
| Ψ_11 | 5 | [19/48, 13/24], b_7–b_13 | 0.0858, 0.106, 0.13, 0.157, 0.187, 0.219, 0.254 |
| Ψ_11 | 5 | [13/24, 11/16], b_0–b_6 | 0.254, 0.289, 0.326, 0.365, 0.405, 0.446, 0.487 |
| Ψ_11 | 5 | [13/24, 11/16], b_7–b_13 | 0.526, 0.564, 0.598, 0.628, 0.652, 0.669, 0.679 |
| Ψ_11 | 5 | [11/16, 5/6], b_0–b_6 | 0.679, 0.689, 0.692, 0.686, 0.671, 0.646, 0.612 |
| Ψ_11 | 5 | [11/16, 5/6], b_7–b_13 | 0.568, 0.516, 0.457, 0.392, 0.326, 0.26, 0.199 |
| Ψ_11 | 6 | [1/4, 19/48], b_0–b_6 | 0.698, 0.697, 0.697, 0.697, 0.697, 0.697, 0.698 |
| Ψ_11 | 6 | [1/4, 19/48], b_7–b_13 | 0.698, 0.698, 0.698, 0.697, 0.695, 0.692, 0.687 |
| Ψ_11 | 6 | [19/48, 13/24], b_0–b_6 | 0.687, 0.682, 0.676, 0.668, 0.658, 0.646, 0.631 |
| Ψ_11 | 6 | [19/48, 13/24], b_7–b_13 | 0.613, 0.592, 0.568, 0.541, 0.511, 0.479, 0.444 |
| Ψ_11 | 6 | [13/24, 11/16], b_0–b_6 | 0.444, 0.409, 0.372, 0.333, 0.293, 0.252, 0.211 |
| Ψ_11 | 6 | [13/24, 11/16], b_7–b_13 | 0.172, 0.134, 0.1, 0.0706, 0.0465, 0.029, 0.0191 |
| Ψ_11 | 6 | [11/16, 5/6], b_0–b_6 | 0.0191, 0.00915, 0.00673, 0.0127, 0.0278, 0.0524, 0.0868 |
| Ψ_11 | 6 | [11/16, 5/6], b_7–b_13 | 0.13, 0.182, 0.241, 0.306, 0.372, 0.438, 0.499 |

#### The algebraic multipliers on the band {#sec:tb2-algebraic-rows}

For [[thm:band]], ranges (d)–(f). Each row uses Θ_ν = Φ(νz) of [[lem:band-algebraic-constants]] on σ ∈ [σ_a, σ_b],
for every l ≥ l_1(σ), with a_* := 4σ_a² − 2σ_a − 4/3 the lower bound for a, A_ν := 6ν⁴ + (17/2)ν³ and α := (a_* − A_ν)/ν.
"Core" is 2ν³ min(η(τ), 1375/7776) and "flank" is 2αν² min(h_ν(τ), h_ν(7/8)); w_I is at least the smaller. Lower bounds
are rounded down and upper bounds up; B♯ is the bound of [[lem:band-sharp]] at σ = σ_b with these constants.

| row | ν | [σ_a, σ_b] | a_* | A_ν | α ≥ | (7/2)ν³ | τ | core ≥ | flank ≥ |
|---|---|---|---|---|---|---|---|---|---|
| (d) | 11/4 | [14, 28] | 2264/3 | 33275/64 | 85.361 | 72.79 | 9/50 | 6.4425 | 5.5568 |
| (e) | 4 | [28, 108] | 9236/3 | 2080 | 249.66 | 224 | 27/200 | 20.661 | 20.68 |
| (f) | 6 | [108, 384] | 139316/3 | 9612 | 6137.7 | 756 | 7/200 | 74.927 | 91.889 |

| row | w_I ≥ | m′ ≥ | M′ ≤ | p_I ≤ | p_∞ ≤ | B♯(σ_b) ≤ |
|---|---|---|---|---|---|---|
| (d) | 5.5568 | 0.009107 | 2.045 | 0.92344 | 0.9398 | 10.297 |
| (e) | 20.661 | 0.0048594 | 2.9745 | 0.96153 | 0.97015 | 10.579 |
| (f) | 74.927 | 0.002303 | 4.4618 | 0.98234 | 0.9864 | 10.381 |

#### Data for the sampled frequencies {#sec:tb2-points}

For [[prop:band-points]]. At each row the algebraic multiplier Θ_ν serves every l ≥ l_1 (a = κ + 3/4 at l = l_1 is
used exactly), and the harmonics l < l_1 are bounded by [[lem:band-barrier]] at the left end σ_- of the range; B♯ is
taken at its right end σ_+. Constants are rounded as in [[sec:tb2-algebraic-rows]].

| [σ_-, σ_+] | l_1 | ν | τ | α ≥ | w_I ≥ | m′ ≥ | M′ ≤ | p_I ≤ | p_∞ ≤ | barrier ≤ | B♯ ≤ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [12, 12] | 23 | 5/2 | 73/400 | 83.424 | 4.8284 | 0.010527 | 1.8591 | 0.90948 | 0.92848 | 3.914 | 5.990 |
| [24, 24] | 47 | 37/10 | 29/200 | 202.35 | 16.211 | 0.0055726 | 2.7514 | 0.95546 | 0.96537 | 3.827 | 4.097 |
| [48, 48] | 94 | 53/10 | 21/200 | 570.75 | 49.246 | 0.0029084 | 3.9412 | 0.97754 | 0.98267 | 1.897 | 3.022 |
| [96, 96] | 190 | 153/20 | 3/40 | 1585.1 | 151.37 | 0.0014458 | 5.6887 | 0.98903 | 0.99157 | 1.885 | 2.252 |
| [128, 128] | 253 | 177/20 | 13/200 | 2465.2 | 235.96 | 0.0010893 | 6.5811 | 0.99177 | 0.99368 | 1.257 | 2.024 |
| [160, 160] | 316 | 99/10 | 23/400 | 3495.4 | 331.94 | 0.00087484 | 7.3619 | 0.99341 | 0.99494 | 0.9422 | 1.869 |
| [192, 192] | 381 | 109/10 | 21/400 | 4607.4 | 444.45 | 0.00072418 | 8.1055 | 0.99455 | 0.99582 | 1.254 | 1.743 |
| [5119/20, 256] | 503 | 12 | 3/80 | 9575.9 | 598.53 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4244 | 1.677 |
| [6399/20, 320] | 631 | 12 | 1/40 | 21693 | 602.87 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4237 | 1.815 |
| [7679/20, 384] | 759 | 12 | 1/50 | 36541 | 604.55 | 0.00059921 | 8.9235 | 0.9955 | 0.99655 | 0.4232 | 1.963 |

### Effective forms of the inverse bounds {#sec:rb-effective}

The stability theory turns estimates into inverse bounds by four kinds of step: a Fredholm estimate with a weak
remainder, "Fredholm and injective, hence invertible", absorption of small terms, and interpolation in the spectral
parameter. Each has a form in which the constant is explicit in its inputs.

**Lemma {#lem:rb-parametrix}** (A parametrix gives the weak-remainder estimate.) Let X, Y, Z be Banach spaces with
X ⊂ Z continuously, T : X → Y and Q′ : Y → X bounded, and suppose that R′ := I − Q′T extends to a bounded map Z → X.
Then for x ∈ X, ‖x‖_X ≤ ‖Q′‖_(Y→X)‖Tx‖_Y + ‖R′‖_(Z→X)‖x‖_Z.

*Proof.* x = Q′Tx + R′x. ∎

**Remark {#rem:rb-parametrix-model}** (The model at ℐ⁺.) In [[lem:ii-f-5-5]] the estimates [[eq:ii-f-5-5]] are
obtained from [[lem:ii-f-5-2]], whose constant involves a projection onto the kernel built from Hahn–Banach functionals
and an open mapping constant. The parametrices of the proof of [[lem:ii-f-5-5]] (a) give them directly, with explicit
constants. There Q′P̂ = I − R′ with R′ fully residual, of indices (α_1, ∞), α_1 > 2γ_I, and Q′ bounded
x^(2γ_I)H^(m−2)_0 → x^(2γ_I)H^m_0. By the kernel bound (i) of that proof (with a = α_1 > 2γ_I and b = ∞) and the
conormality of the kernel under 0-vector fields on either factor, R′ is bounded from x^βH^(−M′)_0 into x^(2γ_I)H^m_0 for
every β. So [[lem:rb-parametrix]], with X = x^(2γ_I)H^m_0, Y = x^(2γ_I)H^(m−2)_0 and Z = x^βH^(−M′)_0, gives the first
estimate of [[eq:ii-f-5-5]] with C = max(‖Q′‖, ‖R′‖_(Z→X)). For the second, P̂Q = I − R with R fully residual of
indices (∞, 3 − α_0), α_0 < 2γ_I; for w in the dual Y* = x^(−2γ_I)H^(2−m)_0, Q*P̂*w = w − R*w, and with
W := x^(β′)H^(−M′)_0, |⟨R*w, y⟩| = |⟨w, Ry⟩| ≤ ‖w‖_W‖R‖_(Y→W*)‖y‖_Y, R being bounded from Y into W* = x^(−β′)H^(M′)_0
by (i) (left index ∞, right index 3 − α_0 > 3 − 2γ_I). So the second estimate holds with
C = max(‖Q‖_(Y→X), ‖R‖_(Y→W*)). No projection and no open mapping constant enter.

**Lemma {#lem:rb-injectivity}** (An a priori estimate and a quantitative injectivity give the inverse.) If
‖x‖_X ≤ C_A(‖Tx‖_Y + ‖Kx‖_V) and ‖Kx‖_V ≤ C_B‖Tx‖_Y for all x, then ‖x‖_X ≤ C_A(1 + C_B)‖Tx‖_Y.

*Proof.* Substitute the second inequality into the first. ∎

This is the effective form of every step "Fredholm and injective, hence invertible" whose inverse bound is wanted: the
content is C_B, a quantitative form of the injectivity.

**Lemma {#lem:rb-absorption}** (Absorption, with the thresholds.)

(a) Let h_a > 0, C_a ≥ ½ and M ∈ ℕ, and suppose that for h < h_a, ‖u‖ ≤ C_a h⁻²‖P′u‖ + C_a h^M‖u‖_(−M𝟏) and
‖u‖_(−M𝟏) ≤ ‖u‖. Then ‖u‖ ≤ 2C_a h⁻²‖P′u‖ for h < min(h_a, (2C_a)^(−1/M)).

(b) Let h_c > 0, C ≥ ¼, C_K > 0 and M ∈ ℕ, and suppose that for h < h_c,
‖u‖_𝐨 ≤ C(h^(−1−δ)‖Pu‖_(𝐨′) + h^M‖u‖_𝐨 + ‖u‖_(−M𝟏)) and ‖u‖_(−M𝟏) ≤ C_K h‖u‖_𝐨. Then ‖u‖_𝐨 ≤ 2Ch^(−1−δ)‖Pu‖_(𝐨′)
for h < h_1 := min(h_c, (4C)^(−1/M), (4CC_K)⁻¹).

(c) In the proof of [[thm:i-b-1-3]] (3) ([[sec:i-b-8-4]]), let C be the larger of the constants of the displays before
absorption in the proof of [[prop:i-b-8-1]] (a)–(c), h_c the least of their thresholds, C_K the constant of its
absorption step, h_1 as in (b), and C_0 := h_1⁻¹(1 − ν′²)^(−1/2). Then for Im σ ≥ 0 and |σ| ≥ C_0, with h = h(σ) and
z = hσ as in [[sec:i-b-8-4]], ‖·‖_𝐨 and ‖·‖_(𝐨′) the semiclassical norms at that h, and δ ∈ [0, 1] the loss of
[[eq:i-b-8-1]] at z,

    ‖u‖_𝐨 ≤ 2C(1 − ν′²)^(−(1−δ)/2) |σ|^(−1+δ) ‖P̂(σ)u‖_(𝐨′).                                 {#eq:rb-high-energy}

*Proof.* (a) For h < min(h_a, (2C_a)^(−1/M)), C_a h^M ≤ ½, so the last term is at most ‖u‖/2 and moves to the left.
(b) For h < h_1, Ch^M ≤ ¼ and CC_K h ≤ ¼, so the last two terms are at most ‖u‖_𝐨/2. (c) h_1 ≤ (4C)^(−1/M) ≤ 1, so
C_0 ≥ (1 − ν′²)^(−1/2) ≥ 1. If Im σ < ν′|σ|, then h = |Re σ|⁻¹ and |Re σ|² = |σ|² − (Im σ)² > |σ|²(1 − ν′²), so
h < (1 − ν′²)^(−1/2)|σ|⁻¹ ≤ h_1; (b) and P_(h,z) = h²P̂(σ) give ‖u‖_𝐨 ≤ 2Ch^(1−δ)‖P̂(σ)u‖_(𝐨′), and
h^(1−δ) ≤ (1 − ν′²)^(−(1−δ)/2)|σ|^(−(1−δ)). Otherwise h = |σ|⁻¹ ≤ C_0⁻¹ < h_1 and δ = 0, so
‖u‖_𝐨 ≤ 2C|σ|⁻¹‖P̂(σ)u‖_(𝐨′), and |σ|⁻¹ ≤ |σ|^(−1+δ) ≤ (1 − ν′²)^(−(1−δ)/2)|σ|^(−1+δ) as |σ| ≥ 1. ∎

The assumptions C_a ≥ ½ and C ≥ ¼ cost nothing, as enlarging a constant keeps an estimate true. The thresholds h_a and
h_c are those of the chains of estimates in [[prop:i-b-6-7]] (a) and [[prop:i-b-8-1]], which contain the threshold of
[[eq:i-b-6-6]]. The bound [[eq:rb-high-energy]] is uniform in σ in the semiclassical norms at h = h(σ); at each fixed h
these are equivalent to the norms of 𝒳_σ and 𝒴_σ ([[sec:i-b-8-4]]), with constants that depend on h.

**Lemma {#lem:rb-interpolation}** (The constant of the interpolation.) In [[prop:i-b-6-7]], let C′_a be such that, after
the absorption of its part (a), ‖P̂′(σ)⁻¹‖ ≤ C′_a for Re σ ≥ h_0⁻¹ and Im σ ∈ [β, β′], and ‖P̂′(σ)⁻¹‖ ≤ C′_a|σ|⁻¹ on
Im σ = β′. Put κ_Γ := β′ − β and

    F_Γ := sup_(σ_0 ≥ h_0⁻¹) exp(3 log σ_0 · e^(−πσ_0/(2κ_Γ))).

Then [[eq:i-b-6-11]] holds with the constant 4F_ΓC′_a: for h ≤ h_0/2 and z ∈ z_0 + i[hβ, hβ′],
‖(P′_(h,z))⁻¹‖ ≤ 4F_ΓC′_a h^(−1−(β′−Im(z/h))/κ_Γ). If κ_Γ = 2^(−3/2) and h_0 ≤ 1, then F_Γ ≤ 1.002659.

*Proof.* In part (c) of the proof of [[prop:i-b-6-7]], [[lem:i-b-6-6]] is applied on a rectangle with L = 2σ_0/κ_Γ,
A = A_0 = C′_a‖w‖, A_1 = C′_aσ_0⁻¹‖w‖ and Λ = log σ_0, w ∈ L². It gives
‖P̂′(σ)⁻¹w‖ ≤ C′_a σ_0^(−θ) exp(3 log σ_0 e^(−πσ_0/(2κ_Γ)))‖w‖ ≤ F_Γ C′_a σ_0^(−θ)‖w‖, θ := (Im σ − β)/κ_Γ ∈ [0, 1],
for Re σ ∈ [2σ_0, 4σ_0]. There h = 1/Re σ ∈ [1/(4σ_0), 1/(2σ_0)], so σ_0^(−θ) ≤ (4h)^θ ≤ 4h^θ, and
(P′_(h,z))⁻¹ = h⁻²P̂′(z/h)⁻¹; as 2 − θ = 1 + (β′ − Im(z/h))/κ_Γ, this is the bound. For the value: with
c := π/(2κ_Γ) = √2π > 4.44288 and s := σ_0 ≥ 1, the function g(s) := log s · e^(−cs) has g′(s) = e^(−cs)(1/s − c log s),
and 1/s − c log s decreases, so g attains its maximum on [1, ∞) at the point s_* where s_* log s_* = 1/c, with
g(s_*) = e^(−cs_*)/(cs_*). As s log s increases on [1, ∞) and 1.205 log 1.205 < 0.22471 < 0.22507 < 1/c, s_* > 1.205;
and t ↦ e^(−t)/t decreases, so g(s_*) < e^(−5.3536)/5.3536 < 8.837 · 10⁻⁴. Hence F_Γ ≤ exp(0.0026511) < 1.002659. ∎

At b_0 with m_0 = 1, q^Γ = 4 on Γ and ν_min = 2^(3/2) ([[thm:vi-a-6-1]]), so the function of η in (Γ.4) is
sup_Γ λ_max(p_1^Γ) − 4η exactly, whatever the fibre inner product, and γ_+ − γ_− = ν_min/8 = 2^(−3/2). For the
choice β = γ_− + ϵ, β′ = γ_+ + ϵ of [[prop:i-b-6-7]], κ_Γ = 2^(−3/2), and [[eq:i-b-6-11]] holds with the constant
4.01064 C′_a for every operator with principal symbol G Id at b_0, once h_0 ≤ 1.

**Lemma {#lem:rb-gluing}** (Gluing through complex absorption.) Let 𝒳, 𝒴, 𝒵 be Banach spaces, P̂ : 𝒳 → 𝒴 bounded,
j : 𝒳 → 𝒵, k : 𝒵 → 𝒴 and W : 𝒵 → 𝒵 bounded, Q := kWj and P_1 := P̂ − iQ, and suppose that P̂ and P_1 are invertible.
With C_ext := ‖P_1⁻¹‖_(𝒴→𝒳) and C_D := ‖jP̂⁻¹k‖_(𝒵→𝒵),

    ‖P̂⁻¹‖_(𝒴→𝒳) ≤ C_ext + C_ext²‖j‖‖k‖‖W‖(1 + ‖W‖C_D).

*Proof.* P_1⁻¹ − P̂⁻¹ = P_1⁻¹(P̂ − P_1)P̂⁻¹ = iP_1⁻¹QP̂⁻¹, and likewise P_1⁻¹ − P̂⁻¹ = iP̂⁻¹QP_1⁻¹. Inserting the second
into the first, P̂⁻¹ = P_1⁻¹ − iP_1⁻¹QP_1⁻¹ − P_1⁻¹(QP̂⁻¹Q)P_1⁻¹, and QP̂⁻¹Q = kW(jP̂⁻¹k)Wj has norm at most
‖k‖‖W‖²C_D‖j‖. ∎

In the stability theory, 𝒳 = 𝒳_σ, 𝒴 = 𝒴_σ, 𝒵 = L²(I) (or L²(I × 𝕊³)), j and k multiplication by a cut-off χ supported
in I with 0 ≤ χ ≤ 1, and W smoothing where 𝒴_σ has positive order on I; then C_D ≤ ‖χ_IP̂(σ)⁻¹χ_I‖, the cut-off bound of
the preceding sections. So, once the cut-off bound is known, an inverse bound in the spaces of the stability theory
needs only C_ext(σ), the inverse of the absorbed problem. Its estimate is the chain of Fredholm estimates at the fixed σ
with the absorbing term, and involves no trapping estimate and no mode stability; its invertibility is a hypothesis of
[[lem:rb-gluing]], which the next lemma supplies for the scalar wave.

**Lemma {#lem:rb-absorbed}** (The absorbed scalar problem is invertible.) At b_0, let q ≥ 0 be a smooth radial function
(q = q(r)) with compact support in {r > r_h}, Q multiplication by q, σ real and nonzero and ϵ_σ := sgn σ. Then
□̂(σ) − iϵ_σQ : 𝒳_σ → 𝒴_σ is invertible.

*Proof.* Q maps 𝒳_σ into functions of class H^s (s > ½ + ϑ_ℋ the order of 𝒳_σ) supported in a fixed compact subset of
{r > r_h}, which embed compactly into 𝒴_σ, whose order there is s − 1 (Rellich's theorem). So □̂(σ) − iϵ_σQ is a compact
perturbation of □̂(σ), which is Fredholm of index 0 by [[thm:i-a-7-2]] (3) and [[thm:i-b-1-3]] (3), as in the proof of
[[prop:iii-d-6-2]]; it suffices to show that its kernel is trivial. Let ω be in the kernel. As in the proof of
[[prop:iii-d-6-2]], ω is smooth across the future horizon and outgoing at infinity, and Q, being radial, preserves the
harmonics; so on {r > r_h}, each component r^(−3/2)u(r_*)Se^(−iσt) of e^(−iσt_*)ω, S ∈ 𝒮_l, has u solving
−u″ + (V_l − σ² − iϵ_σfq)u = 0, with u a multiple of u_h near −∞ and of u_∞ near +∞, where q = 0. As V_l is real,
Im(ū(−u″ + (V_l − σ² − iϵ_σfq)u)) = −(Im(ūu′))′ − ϵ_σfq|u|², and Im(ūu′) tends to σ|c_+|² at +∞ and to −σ|c_−|² at −∞,
where u − c_±e^(±iσr_*) → 0. Integrating over ℝ, 0 = −σ(|c_+|² + |c_−|²) − ϵ_σ∫fq|u|²dr_*. Both terms have the sign of
−σ, so c_+ = 0; u is then the zero multiple of u_∞ near +∞, and u = 0. So ω = 0 on {r > r_h}, and inside the horizon
ω = 0 follows as in part (d) of the proof of [[prop:iii-d-6-2]]. ∎

In the notation of [[lem:rb-gluing]], W = sgn(σ)q, and [[lem:rb-gluing]] uses no sign of W. With ϵ_σ replaced by −sgn σ
the two terms in the proof can cancel.

### The scalar-type blocks at zero energy {#sec:rb-scalar-blocks}

The inverse bound of [[thm:i-c-3-1]] (4) for the linearised operator at zero energy is, by [[lem:rb-schur]], the
supremum of the inverse bounds of its blocks of one type and degree. For the tensor-type blocks the gauge terms vanish
(the proof of [[lem:rb-transfer]]). The scalar-type blocks carry them, and this section records what can be said about
these blocks.

*The operator.* Let m_0 = 1 and L := L_(b_0) of [[def:iii-b-6-1]], with 2L = □ + 2E^C δG + 2δ*_(E_C)E^Υ G + 2R
([[eq:iii-f-1-2]]), acting on stationary symmetric 2-tensors in the Kerr–Schild chart of [[prop:iii-b-3-4]], in which

    g_(b_0) = −f dt² + 2(1 − f) dt dr + (2 − f) dr² + r²g̸,     f = 1 − 1/r²,

regular across the horizon; with v := t + r it is −f dv² + 2dv dr + r²g̸. Its 1-forms are c_C of [[sec:iv4-0]] (that of
[[prop:np-10-14]] at r_0 = 100, with v_C = 1/2, e_C = 1/102400 and γ_C = h⁻¹), c_Υ = ζ(r)r⁻¹dt with ζ = 1 for large r,
and c_(Υ,H) = −½χ(r)dr with χ ∈ C_c^∞ equal to 1 near r_h ([[sec:iii-d1-1]]); γ_(Υ,H) ∈ (0, ϵ_0] and e_Υ, γ_Υ below the
thresholds of [[prop:iii-d1-4-1]]. The tensor-type blocks do not depend on ζ, χ, the smoothing of c_C or the
parameters; the scalar-type blocks do, and every statement below is made for all admissible choices at once unless a
choice is named. Where numbers are given at (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100), they are numbers of the operator with
those parameters; these values are not shown to lie below the thresholds just cited, which are proved to exist without
a value.

*Scalar type.* For l ≥ 0 and S ∈ 𝒮_l real, a stationary symmetric 2-tensor of scalar type l is

    h = H_0S dt² + 2H_1S dt dr + H_2S dr² + 2H_3 dt ⊗_s dS + 2H_4 dr ⊗_s dS + r²(H_5Sg̸ + H_6 δ̸*₀dS),
                                                                                                  {#eq:rb-scalar-type}

with H_3 = H_4 = H_6 = 0 at l = 0 and H_6 = 0 at l = 1 ([[eq:iii-a1-1-3]]), and H_j functions of r. With
‖S‖_(L²(𝕊³)) = 1, its orthonormal components in the frame (dt, dr, r dω) are u_0 = H_0, u_1 = √2H_1, u_2 = H_2,
u_3 = (2κ)^(1/2)H_3/r, u_4 = (2κ)^(1/2)H_4/r, u_5 = √3H_5 and u_6 = ((2/3)κ(κ − 3))^(1/2)H_6, so that the integral
over 𝕊³ of the pointwise norm of h is Σ_j|u_j|², by [[eq:iii-a1-1-2]].

**Lemma {#lem:rb-block-structure}** (The scalar-type block.) L maps the tensors [[eq:rb-scalar-type]] built on S to
tensors of the same form built on S, with radial coefficients (F_0, …, F_6) = L_l(H_0, …, H_6), where L_l is a 7 × 7
(at l = 1, 6 × 6; at l = 0, 4 × 4) matrix of ordinary differential operators of order at most 2 in r, with real
coefficients that are polynomials in κ and do not depend on S ∈ 𝒮_l. Its second-order part is −(f/2)∂_r² times the
identity, so that L_l = ½A_l · Id + (an operator of first order), A_l := −r⁻³∂_r(r³f∂_r) + κr⁻².

*Proof.* L commutes with the rotations, which preserve its 1-forms, and with ∂_t. The space of stationary symmetric
2-tensors of scalar type l is the (l/2, l/2)-isotypic component of the stationary symmetric 2-tensors under SO(4)
([[lem:rb-schur]]), and the equivariant linear maps from 𝒮_l into it are the maps S ↦ [[eq:rb-scalar-type]] with fixed
coefficients H_j: at a point the fibre is the sum of four copies of the trivial representation of the stabiliser SO(3)
(dt², dt dr, dr², g̸), two copies of the vector representation (dt and dr times angular covectors) and one of the
trace-free angular tensors; (l/2, l/2) restricted to SO(3) contains each of the spins 0, 1, 2 once when l ≥ 2, so the
multiplicity is 7 (6 at l = 1, 4 at l = 0), and the seven maps of [[eq:rb-scalar-type]] are independent. So L maps the
tensors built on S to tensors built on S, by a matrix independent of S. Its coefficients are obtained by applying the
identities [[eq:iii-a1-1-2]], whose coefficients are polynomials in κ, and L has real coefficients. Finally the
second-order part of 2L is that of □ = ∇*∇, which is −g^(μν)∂_μ∂_ν on each component; on stationary fields the
angular second derivatives give terms of order zero in r, and g^(rr) = f in this chart, so the r-second-order part of
L is −(f/2)∂_r² on each component. A_l differs from −f∂_r² + κr⁻² by first-order terms. ∎

**Lemma {#lem:rb-block-identities}** (Three identities.) (a) For every stationary 1-form w,
L δ*w = δ*_(E_C)(½□^Υw), with □^Υ := 2δ_(E_Υ)Gδ* of [[eq:iii-b-6-4]]. (b) For every stationary symmetric 2-tensor h,
2δG(Lh) = □^C Υ(h), with Υ(h) := δ_(E_Υ)Gh and □^C := 2δGδ*_(E_C) of [[eq:iii-e-1-1]]. (c) h_m := r⁻²(dt + dr)², the
derivative in m of the Kerr–Schild metrics η + mr⁻²(dt + dr)², satisfies D Ric(h_m) = 0.

*Proof.* L = D Ric + δ*_(E_C)δ_(E_Υ)G at the Ricci-flat g_(b_0). (a) δ*w = ½ℒ_(w♯)g_(b_0), and D Ric(ℒ_Xg) = ℒ_X Ric(g)
= 0 at a Ricci-flat g, so Lδ*w = δ*_(E_C)δ_(E_Υ)Gδ*w = δ*_(E_C)(½□^Υw). (b) The contracted Bianchi identity δ_gG_g
Ric(g) = 0 holds for every metric; differentiating at the Ricci-flat g_(b_0), where Ric = 0, gives δG(D Ric(h)) = 0. So
2δG(Lh) = 2δGδ*_(E_C)(δ_(E_Υ)Gh) = □^C Υ(h). (c) The Kerr–Schild metrics are Ricci-flat for every m
([[prop:iii-b-3-4]]); differentiate at m = 1. ∎

So on the scalar-type block, L factors through the constraint propagation operator □^C and the gauge potential
operator □^Υ, as it does on all of the bundle.

*The indicial family at infinity.* For r beyond the supports of the free data (where ζ = 1, χ = 0 and c_C is in its
outer form), the coefficients of L_l in the orthonormal components u_j are those of a dilation-invariant model, up to
relative errors O(r⁻²) with all derivatives: g_(b_0) − η = r⁻²(dt + dr)², c_C − r⁻¹(dt − v_C dr) = O(r⁻³)dr
([[sec:iv4-0]]), c_Υ = r⁻¹dt and c_(Υ,H) = 0 there. The model is ½ times the operator 2L̄ of [[sec:iii-f1-2]] on
stationary sections of scalar type l, and the frame (dt, dr, r dω) differs from the Cartesian frame (dt̄, dx^i) used
there by an orthogonal change that is homogeneous of degree 0. So in the components u_j the model is
r⁻²N^n_l(−r∂_r) for a matrix polynomial N^n_l(ι) of degree 2, the indicial family of the block in orthonormal
components, with model(r^(−ι)w) = r^(−ι−2)N^n_l(ι)w for w ∈ ℂ^(n_l), and N^n_l(ι) is conjugate to ½N_L(ι) of
[[sec:iii-f1-2]] at scalar type l. By [[lem:iii-f1-2-1]],

    det N^n_l(ι) = 2^(−n_l)(−1)^(n_l)(ι + l)(ι − l − 2) det N_Υ(ι − 1) det N_C(ι + 1)/D(ι).

So the roots of det N^n_l are −l, l + 2, the indicial roots of □^Υ plus 1 and those of □^C less 1, with D removing a
double root 1 at l = 0.

**Lemma {#lem:rb-roots-point}** (The roots nearest the weight line.) Let (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100), and let
C and P_l be the polynomials of [[prop:np-10-12]] (iii) at (v, e, h) = (1/2, 1/102400, 10⁻⁶), h = γ_C⁻¹. At l = 0, 2
and 4, the root of det N^n_l with real part greater than 1 nearest to 1 is ι_l − 1, where ι_0 is the root of C greater
than 2 and, at l = 2, 4, ι_l is the least of the roots of P_l with real part greater than 2. It is real, no other root
of det N^n_l has real part in (1, ι_l − 1], and

    1.00007474375 < ι_0 − 1 < 1.00007474385,     1.00000293235 < ι_2 − 1 < 1.00000293245,
    1.00001692235 < ι_4 − 1 < 1.00001692245.                                                       {#eq:rb-roots-point}

To ten decimal places these roots are 1.0000747438, 1.0000029324 and 1.0000169224; each is an indicial root of □^C at
scalar type l less 1.

*Proof.* *The factors other than □^C.* In the basis of [[prop:np-10-12]] (ii) the scalar type l indicial family of □^C
is the matrix N_l(ι) there, with det(hN_l) = P_l at l ≥ 1 and det(hN_0) = P_0 = −(ι − 2)C; that basis differs from the
one of [[eq:iii-a1-2-9]] by a change that does not depend on ι, so det N_C is a nonzero constant times P_l. By
[[lem:iii-d-4-1]] and [[eq:iii-d-4-2]] the roots of det N_Υ are real: 1 − ι^Υ_(s0,2) < −1, 0, ι^Υ_(s0,2) > 2 and 3 at
l = 0; the negative numbers 1 − ι^Υ_(sl,l+2), 1 − ι^Υ_(sl,l+1) and 1 − l, and ι^Υ_(sl,l+1) > l + 1,
ι^Υ_(sl,l+2) > l + 2 and l + 3, at l ≥ 2. So the roots of det N_Υ(ι − 1) greater than 1 exceed 3 at l = 0 and l + 2 at
l ≥ 2, and the root l + 2 is at least 2. At l = 0 the root 1 of det N_Υ(ι − 1) and the root 1 of
P_0(ι + 1) = −(ι − 1)C(ι + 1) form the double root that D removes. Hence a root of det N^n_l with real part greater
than 1 is at least 2 unless it is μ − 1 for a root μ of C (at l = 0) or of P_l (at l = 2, 4).

*The roots of C and of P_l.* By [[prop:np-10-54]] and its proof, C has exactly one root greater than 2, its other two
roots having real part below −100; and at l = 2, 4, P_l has exactly three roots, counted with multiplicity, with real
part greater than 2, the other three having real part below −100. Expanding [[eq:s14-c0]] and the determinant of
[[eq:s14-nl]] about ι = 2 gives C(2 + ε) = Σ_(k≤3) c_kε^k and P_l(2 + ε) = Σ_(k≤6) c_kε^k, with the exact coefficients

    C:    c_0 = 1.4948443959375·10⁻⁴,  c_1 = −1.999957171827171875,  c_2 = −2.999994234375·10⁻⁶,  c_3 = −10⁻¹²;
    P_2:  c_0 = 1.131875750625·10⁻⁹,  c_1 = −3.9186117873477253125·10⁻⁴,  c_2 = 2.000144656033436956015625,
          c_3 = −1.999958171536796769234375;
    P_4:  c_0 = 1.4261642521875·10⁻⁸,  c_1 = −8.7661649198425078125·10⁻⁴,  c_2 = 2.000224654883184362015625,
          c_3 = −1.999958171408796889734375;

and, for P_2 and P_4, |c_4| < 5·10⁻⁶, |c_5| < 4·10⁻¹² and c_6 = −10⁻¹⁸, so that |c_4ε⁴ + c_5ε⁵ + c_6ε⁶| < 10⁻²⁴ for
0 ≤ ε ≤ 2·10⁻⁵. Let (ε_−, ε_+) be (7.474375·10⁻⁵, 7.474385·10⁻⁵) for C, (2.93235·10⁻⁶, 2.93245·10⁻⁶) for P_2 and
(1.692235·10⁻⁵, 1.692245·10⁻⁵) for P_4. The sums c_0 + c_1ε + c_2ε² + c_3ε³ at ε = ε_− and ε = ε_+ are
1.4071…·10⁻¹⁰ and −5.9280…·10⁻¹¹ for C, 1.6962…·10⁻¹⁶ and −3.7843…·10⁻¹⁴ for P_2, and 1.7929…·10⁻¹⁴ and
−6.2962…·10⁻¹⁴ for P_4; so C and P_l are positive at 2 + ε_− and negative at 2 + ε_+. From [[eq:s14-nl]],
moreover, P_2(5/2) = 0.2498…, P_2(3) = −2.1037…·10⁻⁴, P_4(5/2) = 0.2496… and P_4(3) = −6.1511…·10⁻⁴. Hence C has a
root in (2 + ε_−, 2 + ε_+), which is its only root greater than 2; and P_l has a root in each of (2 + ε_−, 2 + ε_+),
(2 + ε_+, 5/2) and (5/2, 3), which are therefore its three roots with real part greater than 2, each simple, the least
being ι_l. So ι_l − 1 ∈ (1 + ε_−, 1 + ε_+), which is [[eq:rb-roots-point]]; every other root of det N^n_l coming from C
or P_l has real part below −101 or, at l = 2, 4, greater than 1 + ε_+; with the first part the lemma follows. ∎

*The horizon.* Write x := a_vγ_C r_h, with a_v the dv-component of c_C at r_h.

**Lemma {#lem:rb-horizon-exponents}** (The horizon exponents do not depend on l.) r = r_h is a regular singular point of
the block L_l, and its exponents are 0, with multiplicity equal to the size n_l of the block (7, 6 or 4), and the
eigenvalues of the restriction to the block of the fibre endomorphism K of [[lem:iii-f2-1-1]]. If c_Υ vanishes near
r_h these are, for l ≥ 2,

    2 − 2x,   1 − x,   −(1 − e_C)x,   0,   0,   −1,   −2,

at l = 1 the same without one of the two zeros, and at l = 0 the values 2 − 2x, −(1 − e_C)x, 0 and −2. If instead
c_Υ = ζr⁻¹dt with ζ(r_h) = ζ_h near r_h, the values 0, −1 and −2 are replaced by −ζ_hγ_Υ(1 − e_Υ), −1 − ζ_hγ_Υ and
−2 − 2ζ_hγ_Υ, the others being unchanged. None of these depends on l.

*Proof.* Work in the ingoing chart (v, r), in which stationary fields are those independent of v, and use the frame (dv,
dr, r dω), which differs from (dt, dr, r dω) by the constant change dt = dv − dr; this changes neither the order of the
singularity nor the exponents. In this chart g^(vv) = 0, g^(vr) = 1 and g^(rr) = f, with f = f′(r_h)(r − r_h) (1 + O(r −
r_h)). By [[lem:rb-block-structure]], the block of 2L, which has the exponents of L_l, has the form −fU″ + A_1(r)U′ +
A_0(r)U on the vector U of radial coefficients, with A_1, A_0 smooth across r_h; for Y := (U, (r − r_h)U′),

    (r − r_h)Y′ = 𝔐(r)Y,     𝔐(r_h) = ⎛ 0    1                    ⎞ ,
                                       ⎝ 0    1 + A_1(r_h)/f′(r_h) ⎠

as (r − r_h)A_0/f is smooth; so the exponents are 0 (n_l times) and the eigenvalues of 1 + A_1(r_h)/f′(r_h). We compute
A_1(r_h), the coefficient of ∂_r at r_h of the stationary operator 2L. In □ = ∇*∇ the first-order terms in ∂_r
are −(1/√|g|)∂_μ(√|g|g^(μr))∂_r = −r⁻³(r³f)′∂_r, which is −f′(r_h)∂_r at r_h, and −2g^(μr)𝔄_μ∂_r = −2𝔄_v∂_r at r_h,
where ∇_(∂_v) acts on the frame by the matrix 𝔄_v; the proof of [[lem:iii-f2-1-1]] gives 𝔄_v = −(f′(r_h)/2)K_0. The
first-order operators 2E^CδG and 2δ*E^ΥG have, at r_h, ∂_r-coefficients equal to their principal symbols at ζ = ξdr
divided by iξ, which are f′(r_h)K_C and f′(r_h)K_Υ in the notation of that proof (where E^Υ is its horizon part); all
other terms are of order zero in r on stationary fields of one degree. So the coefficient of ∂_r of 2L at r_h is
−f′(r_h)(1 − K), K = K_0 + K_C + K_Υ, and 1 + A_1(r_h)/f′(r_h) = K on the block.

K is a fibre endomorphism commuting with the rotations that fix the point. It therefore maps the span of dv², dv dr,
dr², T := Σ_a e_a² (four copies of the trivial representation of the stabiliser) into itself, the span of dv ⊗_s e and
dr ⊗_s e with e angular into itself, and acts as a scalar on the trace-free angular tensors; on the block it acts on
the coefficients of S, of dS and of δ̸*₀dS by these three restrictions. The proof of [[lem:iii-f2-1-1]] computes them
at y = 0 (c_(Υ,H) has no dv-component): on the first, eigenvalues 2 − 2x (dv²), 0 (dv dr), −(1 − e_C)x (T) and −2 (dr²);
on the second, 1 − x and −1; on the third, 0. This is the list. If c_Υ = ζr⁻¹dt near r_h, then at r_h,
c_Υ = ζ_h(dv − dr) and g⁻¹c_Υ = ζ_h(∂_r − ∂_v), and the principal symbol of 2δ*E^Υ_∞G at ξdr adds to K the term
K_∞h = −ζ_hγ_Υ r_h dr ⊗_s (2ι_(∂_r−∂_v)h − e_Υ(dv − dr) tr h) ([[eq:iii-b-6-5]]). For the grading of the proof of
[[lem:iii-f2-1-1]] (weights 1, −1, 0 for dv, dr and the angular covectors), its part with ι_(∂_r) and its part with
e_Υ dr ⊗_s dv preserve the weight and the others lower it by 2, so K stays block triangular. The weight-preserving
part adds −ζ_hγ_Υ on dr ⊗_s e (ι_(∂_r)(dr ⊗_s e) = ½e) and −2ζ_hγ_Υ on dr², nothing on dv² and dv ⊗_s e, and on the
weight-zero span of dv dr and T it adds −ζ_hγ_Υ(1 − e_Υ) on dv dr (ι_(∂_r)(dv dr) = ½dv and tr(dv dr) = 1) and maps T
to 3ζ_hγ_Υe_Υ dv dr, which keeps that block triangular. Adding these to the diagonal entries above gives the second
list. ∎

At (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100), with a_v = 1/200 (the inner form of c_C) and r_h = 1, x = 5000, and the
exponents other than the zeros are −9998, −4999, −2559975/512, 0, −1, −2 when c_Υ vanishes near the horizon, and
−9998, −4999, −2559975/512, −0.0099, −1.01, −2.02 when ζ = 1 there. Whatever makes the scalar-type blocks invertible near
and inside the horizon is the same at every degree, and it carries exponents of size γ_Ca_vr_h.

*The weight.* Let α + 2 =: β lie in the indicial gap at infinity of the block, and use on stationary fields of scalar
type l, near infinity, the norms

    ‖h‖_X² := Σ_j ∫ r^(2α+3)(|u_j|² + r²|∂_ru_j|² + κ|u_j|²) dr,     ‖F‖_Y² := Σ_j ∫ r^(2α+7)|F_j|² dr
                                                                                                  {#eq:rb-block-norms}

in the orthonormal components (F_j those of a tensor F of the form [[eq:rb-scalar-type]]): these are norms of
H̄_b^(1,α) and H̄_b^(0,α+2) of [[sec:i-c-1-2]] near infinity, with the b-vector field r∂_r and the rotation fields as
generators (the squares of the rotation fields sum to κ on scalar type l). In x := log r, u = r^(−β)φ(x) gives
r^(2α+3)(|u|² + r²|∂_ru|²)dr = (|φ|² + |φ′ − βφ|²)dx, and F = r^(−β−2)φ(x) gives r^(2α+7)|F|²dr = |φ|²dx.

**Lemma {#lem:rb-quasimode}** (An upper bound for the least singular value.) For every nonzero v ∈ ℂ^(n_l) and every
admissible choice of the free gauge data,

    inf_(H≠0) ‖L_lH‖_Y/‖H‖_X ≤ |N^n_l(β)v|/((1 + β² + κ)^(1/2)|v|),

the infimum over H supported in r ≥ R for any R; at l = 0 also over H orthogonal in X to any given finite-dimensional
subspace of X.

*Proof.* Take φ ∈ C_c^∞((0, 1)) with ‖φ‖_(L²) = 1, x_0 ≥ log R, W ≥ 1, φ_W(x) := W^(−1/2)φ((x − x_0)/W), and H_W with
orthonormal components u = r^(−β)φ_W(log r)v. Then ‖H_W‖_X² = |v|²∫(|φ_W|² + |φ_W′ − βφ_W|² + κ|φ_W|²)dx =
(1 + β² + κ)|v|² + |v|²‖φ_W′‖², the cross term ∫φ_Wφ_W′ vanishing, and ‖φ_W′‖ = W⁻¹‖φ′‖. For x_0 large, H_W is
supported where the coefficients are those of the model up to O(r⁻²); since the model is r⁻²N^n_l(−r∂_r) and
−r∂_r(r^(−β)ψ(log r)) = r^(−β)(β − ∂_x)ψ,

    L_lH_W = r^(−β−2)(N^n_l(β − ∂_x)(φ_Wv) + e),     N^n_l(β − ∂_x) = N^n_l(β) − N^n_l′(β)∂_x + ½N^n_l″(β)∂_x²,

with |e| ≤ Ce^(−2x_0)(|φ_W| + |φ_W′| + |φ_W″|)|v|. Hence ‖L_lH_W‖_Y ≤ |N^n_l(β)v| + CW⁻¹ + Ce^(−2x_0), and letting
W → ∞ and then x_0 → ∞ gives the bound. At l = 0, H_W → 0 weakly in X as x_0 → ∞, since its support leaves every
compact set at bounded norm; so its component along a fixed finite-dimensional subspace tends to 0, and the quotient
on the orthogonal complement has the same limit. ∎

This is the elementary half of the b-calculus fact that the norm of an inverse on a weighted space is at least that of
the inverse of the indicial family on the weight line. For the scalar model ½A_l, whose indicial family is
½(ι(2 − ι) + κ), it gives at β = 1 an upper bound (κ + 1)/(2(κ + 2)^(1/2)) for its least singular value in these norms.

At α = −1 (β = 1) the indicial family of the degree-2 block has the root 1.0000029324, less than 2.94 · 10⁻⁶ from the
weight line ([[lem:rb-roots-point]]), and [[lem:rb-quasimode]] gives a correspondingly small upper bound. To evaluate it
we write the indicial family out.

*The indicial family, explicitly.* Put y_j := u_j/ν_j, with (ν_0, …, ν_6) := (1, √2, 1, (2κ)^(1/2), (2κ)^(1/2), √3,
((2/3)κ(κ − 3))^(1/2)), so that (y_0, …, y_6) = (H_0, H_1, H_2, H_3/r, H_4/r, H_5, H_6) and

    h = S(y_0dt² + 2y_1dt dr + y_2dr²) + 2r(y_3dt + y_4dr) ⊗_s dS + r²(y_5Sg̸ + y_6δ̸*₀dS);

write a stationary 1-form of scalar type l as (ω_0dt + ω_1dr)S + ω_2r dS. Let N^y_l(ι) be the indicial family in the
coordinates y, so that N^n_l(ι) has the entries ν_iN^y_l(ι)_(ij)/ν_j; at l = 1 the coordinate y_6, and at l = 0 the
coordinates y_3, y_4, y_6 and ω_2, are absent, and the corresponding rows and columns are dropped. With
|w|_ν² := Σ_j ν_j²|w_j|², the vector v with v_j = ν_jw_j has |v| = |w|_ν and |N^n_l(β)v| = |N^y_l(β)w|_ν.

**Lemma {#lem:rb-indicial-explicit}** (The indicial family of the block.) Put ϖ := κ + 2ι − ι². Then

    N^y_l(ι) = ½𝔚(ι) + 𝔈_C𝔇(ι)𝔊 + (𝔖(ι + 1) + 𝔈_C)𝔈_Υ,                                         {#eq:rb-indicial-explicit}

where, for y ∈ ℂ⁷ and ω ∈ ℂ³,

    𝔚(ι)y = (ϖy_0, (ϖ + 3)y_1 − 2κy_3, (ϖ + 6)y_2 − 4κy_4 − 6y_5, −2y_1 + (ϖ − 1)y_3,
             −2y_2 + (ϖ + 4)y_4 + 2y_5 − (4/3)(κ − 3)y_6, −2y_2 + (4/3)κy_4 + (ϖ + 2)y_5, −4y_4 + (ϖ − 4)y_6),
    𝔊y = (½(y_0 + y_2) + (3/2)y_5, y_1, ½(y_0 + y_2) − (3/2)y_5, y_3, y_4, ½(y_0 − y_2 − y_5), y_6),
    𝔇(ι)y = ((ι − 3)y_1 + κy_3, (ι − 3)y_2 + κy_4 + 3y_5, (ι − 4)y_4 − y_5 + (2/3)(κ − 3)y_6),
    𝔖(ι)ω = (0, −½ιω_0, −ιω_1, ½ω_0, ½(ω_1 − (ι + 1)ω_2), ω_1 − (κ/3)ω_2, ω_2),
    𝔈_Cω = γ_C((2/3)((2 + e_C)ω_0 − (1 − e_C)v_Cω_1), ω_1 − v_Cω_0, (2/3)((1 − e_C)ω_0 − (2 + e_C)v_Cω_1),
               ω_2, −v_Cω_2, (2/3)(1 − e_C)(ω_0 + v_Cω_1), 0),
    𝔈_Υy = γ_Υ((2 − e_Υ)y_0 + e_Υ(y_2 + 3y_5), 2y_1, 2y_3).

*Proof.* The model is ½ times 2L̄ = □̄ + 2Ē^Cδ̄Ḡ + 2(δ̄* + Ē^C)Ē^ΥḠ ([[eq:iii-f-2-1]]) on stationary sections of
scalar type l, in the frame (dt, dr, r dω) of ḡ = −dt² + dr² + r²g̸. On the coordinates of a section r^(−ι)ŷ (or
r^(−ι)ω̂), □̄ acts by 𝔚(ι) and the result carries r^(−ι−2); δ̄ acts by 𝔇(ι), δ̄* by 𝔖(ι), Ē^C by 𝔈_C and Ē^ΥḠ by
𝔈_Υ, the result carrying r^(−ι−1); and Ḡ acts by 𝔊. So the composition rule of the proof of [[lem:iii-f1-2-1]] gives
[[eq:rb-indicial-explicit]], and it remains to derive the six matrices. Below, dS, g̸ and δ̸*₀dS are the objects on
𝕊³, and the 1-form r dS and the tensor r²q, q on 𝕊³, are identified with tangential fields homogeneous of degree 0, as
in [[sec:iii-a1-2]].

*𝔚.* On stationary sections the formulas for □̄h in the proof of [[lem:iii-a1-2-1]], at ν = 3, apply with 𝖠 = y_0S,
𝖷 = y_1S, 𝖡 = y_2S, 𝖶 = y_3dS, 𝖴 = y_4dS and q = y_5Sg̸ + y_6δ̸*₀dS, and □_c(r^(−ι)X) = r^(−ι−2)(Δ̸ + 2ι − ι²)X.
The identities [[eq:iii-a1-1-2]] at ν = 3 (δ̸dS = κS, Δ̸dS = (κ − 2)dS, δ̸*dS = δ̸*₀dS − (κ/3)g̸S, Δ̸(g̸S) = κg̸S,
δ̸(g̸S) = −dS, tr(g̸S) = 3S, δ̸(δ̸*₀dS) = (2/3)(κ − 3)dS, Δ̸(δ̸*₀dS) = (κ − 6)δ̸*₀dS) turn □_c𝖠, T_X, T_B, T_W and
T_U into the components 0 to 4 of 𝔚(ι)y, and T_Q into the components 5 and 6; for instance
T_U = r^(−ι−2)((ϖ + 4)y_4 − 2y_2 + 2y_5 − (4/3)(κ − 3)y_6)dS.

*𝔊.* tr_ḡ h = (y_2 − y_0 + 3y_5)S, and Ḡh = h − ½ḡ tr_ḡ h.

*𝔇.* In Cartesian coordinates, on stationary sections, (δ̄k)_t = −∂_ik_(it) and (δ̄k)_j = −∂_ik_(ij). For a function
f(r), a 1-form V and a symmetric 2-tensor Q on 𝕊³, regarded as tangential fields homogeneous of degree 0, the relation
∂_ix̂_j = r⁻¹(δ_ij − x̂_ix̂_j) and the Gauss formula of the proof of [[lem:iii-a1-1-2]] give

    ∂_i(fx̂_i) = f′ + 3f/r,     ∂_i(fV_i) = −r⁻¹fδ̸V,     ∂_i(fx̂_ix̂_j) = (f′ + 3f/r)x̂_j,
    ∂_i(f(x̂_iV_j + V_ix̂_j)) = (f′ + 4f/r)V_j − r⁻¹f(δ̸V)x̂_j,     ∂_i(fQ_ij) = −r⁻¹f((δ̸Q)_j + (tr Q)x̂_j).

For k with the coordinates y, k_(ti) = y_1Sx̂_i + y_3(dS)_i and k_(ij) = y_2Sx̂_ix̂_j + y_4(x̂_i(dS)_j + (dS)_ix̂_j) +
(y_5Sg̸ + y_6δ̸*₀dS)_ij; with y_j = r^(−ι)ŷ_j these give the three components of 𝔇(ι)ŷ.

*𝔖.* The Christoffel symbols of ḡ in t, r and coordinates on 𝕊³ (indices a, b, c) vanish except Γ^r_(ab) = −rg̸_ab,
Γ^a_(rb) = Γ^a_(br) = r⁻¹δ^a_b and Γ^c_(ab) = Γ̸^c_(ab). For ω = (ω_0dt + ω_1dr)S + ω_2r dS with ω_j functions of r,
the components of δ̄*ω = ½(∇_μω_ν + ∇_νω_μ) are therefore 0 (tt), ½ω_0′S (tr), ½ω_0∂_aS (ta), ω_1′S (rr),
½(rω_2′ + ω_1 − ω_2)∂_aS (ra) and r(ω_1Sg̸ + ω_2∇̸²S)_ab (ab), where ∇̸²S = δ̸*₀dS − (κ/3)g̸S; with ω_j = r^(−ι)ω̂_j
these are the components of the tensor whose coordinates are r^(−ι−1)𝔖(ι)ω̂.

*𝔈_C and 𝔈_Υ.* With c̄_C = r⁻¹(dt − v_Cdr), ⟨c̄_C, ω⟩ = −r⁻¹(ω_0 + v_Cω_1)S, and the coordinates of
Ē^Cω = γ_C(2c̄_C ⊗_s ω − (2/3)(1 − e_C)ḡ⟨c̄_C, ω⟩) are r⁻¹𝔈_Cω. By the calculation in the proof of [[lem:iii-b-6-2]],
Ē^ΥḠh = −γ_Υ(2ι_(ḡ⁻¹c̄)h − e_Υc̄ tr_ḡ h) with c̄ = r⁻¹dt; as ḡ⁻¹c̄ = −r⁻¹∂_t and
h(∂_t, ·) = (y_0dt + y_1dr)S + y_3r dS, the coordinates of Ē^ΥḠh are r⁻¹𝔈_Υy. ∎

**Proposition {#prop:rb-quasimode-point}** (Upper bounds at the computational point.) Let (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100,
1/100). The least singular value of L_l from H̄_b^(1,α) to H̄_b^(0,α+2), in the norms [[eq:rb-block-norms]] (at l = 0
on the complement of the zero-energy state), is at most

    3.1413 · 10⁻⁶, 2.6181 · 10⁻⁷ and 1.4956 · 10⁻⁶ at α = −1,     0.0204, 0.0149 and 0.0121 at α + 2 = 1/2,

at l = 0, 2 and 4 respectively. Hence the inverse bound of the scalar-type blocks at (s, α) = (1, −1) is at least
1/(2.6181 · 10⁻⁷) > 3.81 · 10⁶.

*Proof.* Let β := α + 2. By [[lem:rb-quasimode]] with v_j = ν_jw_j, the least singular value is at most
|N^y_l(β)w|_ν/((1 + β² + κ)^(1/2)|w|_ν) for every nonzero w. Take for w the integer vectors below, in the coordinates
(y_0, y_1, y_2, y_5) at l = 0 and (y_0, …, y_6) at l = 2, 4, and evaluate N^y_l(β)w by [[eq:rb-indicial-explicit]]
with v_C = 1/2 and e_C = 1/102400 ([[sec:iv4-0]]), in exact rational arithmetic. The two norms satisfy

    l = 0, β = 1:    w = (100000000000000, 1007162254783, 57142808753792, 61891238140479),
                     |N^y_0(1)w|_ν < 6.99009 · 10⁸,  |w|_ν > 1.57349 · 10¹⁴;
    l = 2, β = 1:    w = (782915609357549, −995884630547290, 1000000000000000, −250929960117404,
                          273234393610333, −38274812163262, 220595097238448),
                     |N^y_2(1)w|_ν < 2.20608 · 10⁹,  |w|_ν > 2.66468 · 10¹⁵;
    l = 4, β = 1:    w = (−886797550484807, 1000000000000000, −870236443529540, 84073284652201,
                          −69161735576493, −61546428884644, −13333857961543),
                     |N^y_4(1)w|_ν < 1.55977 · 10¹⁰,  |w|_ν > 2.04541 · 10¹⁵;
    l = 0, β = 1/2:  w = (10000000000, 80667681, 6427240362, 6743687111),
                     |N^y_0(1/2)w|_ν < 3.80090 · 10⁸,  |w|_ν > 1.66659 · 10¹⁰;
    l = 2, β = 1/2:  w = (10000000000, −6663265206, 8414267379, −2107384764, 1619495356, 3474019763, 1429871770),
                     |N^y_2(1/2)w|_ν < 9.71275 · 10⁸,  |w|_ν > 2.15254 · 10¹⁰;
    l = 4, β = 1/2:  w = (10000000000, −6522392505, 6893152374, −687784430, 356595656, 3568156727, 73656247),
                     |N^y_4(1/2)w|_ν < 1.05160 · 10⁹,  |w|_ν > 1.73616 · 10¹⁰.

With (1 + β² + κ)^(1/2) = √2, √10 and √26 at β = 1 (κ = 0, 8, 24), larger than 1.41421, 3.16227 and 5.09901, and
(5/4)^(1/2), (37/4)^(1/2) and (105/4)^(1/2) at β = 1/2, larger than 1.11803, 3.04138 and 5.02493, the quotients are
less than 3.14128 · 10⁻⁶, 2.61805 · 10⁻⁷, 1.49554 · 10⁻⁶, 0.0203988, 0.0148362 and 0.0120540, which gives the bounds;
and 1/(2.6181 · 10⁻⁷) > 3.8195 · 10⁶. ∎

An explicit constant for these blocks is therefore to be sought at a weight in the middle of the gap; α + 2 ∈ (0, 1) is
what [[sec:iii-d1-1]] uses.

**Remark {#rem:rb-quasimode-observed}** (Numerical observation.) On the full degree-2 block at the parameters above,
the quasi-mode of the proof of [[lem:rb-quasimode]] with x_0 = log 400 and widths W = 100, 1000 and 10000, evaluated in
floating point, gives the quotient ‖L_lH‖_Y/‖H‖_X = 1.3900 · 10⁴, 1.3901 · 10³ and 1.3901 · 10², and the
dilation-invariant model gives the same to 10⁻³. At these widths the term N^n_l′(1)vφ_W′, of the size of γ_C, dominates,
so the quotient falls like 1/W and reaches the bound of [[lem:rb-quasimode]] only for W of order 5 · 10¹². No proof uses
these values.

*The perturbative route at large degree.* Write L_l = ½A_l · Id + ℛ_l in the orthonormal components, ℛ_l of first order.
A lower bound σ_min(L_l) ≥ σ_min(½A_l) − ‖ℛ_l‖_(X→Y) needs ‖ℛ_l‖ below σ_min(½A_l) ≤ (κ + 1)/(2(κ + 2)^(1/2)). At the
inner gauge data (c_C = (1/200)dt + (1/800)dr, c_(Υ,H) = −½dr, γ_C = 10⁶), the coefficient of u_3′ in the u_3 component
of ℛ_l is M_33(r) = −(5000r − 1)/r³, free of κ: this is the following lemma with γ_Ca = 10⁶/200 = 5000.

**Lemma {#lem:rb-m33}** (A first-order entry of ℛ_l.) Where c_C = a dt + b dr, with a and b functions of r, the
coefficient of u_3′ in the u_3 component of ℛ_l is

    M_33(r) = −(γ_C a(r) r − 1)/r³;                                                              {#eq:rb-m33}

it depends neither on κ nor on b, e_C, c_Υ, γ_Υ, e_Υ, c_(Υ,H) and γ_(Υ,H).

*Proof.* By [[eq:iii-f-1-2]], 2L = □ + 2E^CδG + 2δ*_(E_C)E^ΥG + 2R. Here R, E^ΥG and E^CE^ΥG are of order zero, and
for a stationary 1-form w the component (δ*w)_(tA) = ½∂_Aw_t − Γ^μ_(tA)w_μ (A an angular index) contains no
r-derivative of w. So in the component (Lh)_(tA) = F_3∂_AS, F_3 the coefficient of 2dt ⊗_s dS in Lh, the derivatives
of H_3 come from □h and 2E^CδGh only, and h_(tA) = H_3∂_AS.

In the chart above, g^(tt) = f − 2, g^(tr) = 1 − f = r⁻², g^(rr) = f and |det g|^(1/2) = r³|det g̸|^(1/2) (the
determinant of the (t, r) block of g is −1), and Γ^t_(tt) = −½g^(tr)∂_rg_(tt) = ½(1 − f)f′,
Γ^t_(rt) = ½g^(tt)∂_rg_(tt) = ½(2 − f)f′, Γ^B_(rA) = r⁻¹δ^B_A and Γ^B_(tA) = 0. For a symmetric 2-tensor,

    (□h)_(μν) = −g^(αβ)∂_α∂_βh_(μν) + g^(αβ)Γ^λ_(αβ)∂_λh_(μν) + 2g^(αβ)Γ^λ_(αμ)∂_βh_(λν) + 2g^(αβ)Γ^λ_(αν)∂_βh_(μλ)

up to terms without derivatives of h. At (μ, ν) = (t, A), with h stationary, H_3″ enters only through −g^(rr)∂_r²,
and H_3′ only through λ = r in the second term, λ = t and β = r in the third, and λ angular and β = r in the fourth.
With g^(αβ)Γ^r_(αβ) = −|det g|^(−1/2)∂_α(|det g|^(1/2)g^(αr)) = −r⁻³(r³f)′ and
2(g^(tr)Γ^t_(tt) + g^(rr)Γ^t_(rt)) = f′((1 − f)² + f(2 − f)) = f′, this gives

    (□h)_(tA) = (−fH_3″ + (−(3r² − 1)/r³ + f′ + 2f/r)H_3′)∂_AS + … = (−fH_3″ + (−1/r + 1/r³)H_3′)∂_AS + …,

by f = 1 − r⁻², where … stands for terms without H_3′ and H_3″. Next, (E^Cω)_(tA) = γ_C(c_(C,t)ω_A + c_(C,A)ω_t) =
γ_Caω_A, as g_(tA) = 0 and c_C has no angular component; and in (δGh)_A = −g^(αβ)∇_α(Gh)_(βA) the only term with H_3′
is −g^(rt)∂_r(Gh)_(tA) = −r⁻²H_3′∂_AS, as (Gh)_(tA) = h_(tA). Hence

    F_3 = −(f/2)H_3″ + (−1/(2r) + 1/(2r³) − γ_Ca r⁻²)H_3′ + … .

In the orthonormal components u_3 = (2κ)^(1/2)H_3/r and (L_lH)_3 = (2κ)^(1/2)F_3/r. Substituting H_3 = r(2κ)^(−1/2)u_3,
so that H_3′ = (2κ)^(−1/2)(u_3 + ru_3′) and H_3″ = (2κ)^(−1/2)(2u_3′ + ru_3″), the coefficient of u_3′ in (L_lH)_3 is
−f/r − 1/(2r) + 1/(2r³) − γ_Ca r⁻² = −3/(2r) + 3/(2r³) − γ_Ca r⁻². In ½A_lu_3 = −(f/2)u_3″ − ((3r² − 1)/(2r³))u_3′ +
κu_3/(2r²) the coefficient of u_3′ is −3/(2r) + 1/(2r³). The difference is [[eq:rb-m33]], and no constant other than
γ_C and a entered. ∎

Fields H with only u_3 nonzero, of high frequency in r and concentrated near r_0, have lim inf ‖ℛ_lH‖_Y/‖H‖_X ≥
r_0|M_33(r_0)| by [[eq:rb-block-norms]] (at α = −1 the weights are r and r⁵, and the derivative term dominates both
norms); on the domain {r ≥ r_h/2} of the zero-energy problem this gives ‖ℛ_l‖ ≥ ½|M_33(½)| = 9996 for every l. And
(κ + 1)/(2(κ + 2)^(1/2)) < 9996 exactly when (κ + 1)² < 4 · 9996²(κ + 2), which holds for every l ≤ 19,991, in
particular at l = 19,990 (κ = 399,640,080: (κ + 1)² < 1.59713 · 10¹⁷ < 1.59728 · 10¹⁷ < 4 · 9996²(κ + 2)) and fails
from l = 19,992 on. So this route gives no lower bound at any degree l ≤ 19,991; if a perturbative regime exists at
all, it begins above that degree, and the horizon part of the block does not become perturbative at any degree
([[lem:rb-horizon-exponents]]).
