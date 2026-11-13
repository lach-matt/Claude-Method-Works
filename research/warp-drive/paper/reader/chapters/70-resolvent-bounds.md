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

    I_l := ∫_ℝ V_l dr_* = ∫_(r_h)^∞ ((κ + 3/4)/r² + 9m/(4r⁴)) dr = (κ + 3/2)/r_h.                     {#eq:rb-barrier-integral}

*Solutions at the ends.* Let σ ∈ ℂ ∖ {0} with Im σ ≥ 0. V_l is integrable in r_* at both ends, so the Volterra
equations u(x) = e^(−iσx) + ∫_(−∞)^x σ⁻¹ sin(σ(x − x′))V_l(x′)u(x′) dx′ and
u(x) = e^(iσx) − ∫_x^∞ σ⁻¹ sin(σ(x − x′))V_l(x′)u(x′) dx′ have unique solutions by iteration, as in the proof of
[[prop:iii-d-6-2]]. They define the solutions u_h and u_∞ of −u″ + (V_l − σ²)u = 0 with

    u_h e^(iσr_*) → 1,  u_h′ + iσu_h → 0 as r_* → −∞;     u_∞ e^(−iσr_*) → 1,  u_∞′ − iσu_∞ → 0 as r_* → ∞,

the second limit in each case from the differentiated Volterra equation, whose remainder is bounded by the tail of
∫|V_l|. A solution with u′ + iσu → 0 at −∞ is a multiple of u_h, and one with u′ − iσu → 0 at ∞ a multiple of u_∞: the
other solution at each end behaves like e^(±iσr_*), for which this quantity tends to a nonzero multiple of e^(±iσr_*)
when σ is real. In the spacetime, e^(−iσt)u_h = e^(−iσ(t + r_*))(1 + o(1)) is the behaviour of a field smooth across
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

    ‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)a − σ²) = (256/15)/(κ + 3/4 − (256/15)σ²).                          {#eq:rb-closed-form}

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

