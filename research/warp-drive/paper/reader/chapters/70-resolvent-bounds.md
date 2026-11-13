# Part. Explicit constants {#part:constants}

## Explicit resolvent bounds on five-dimensional Tangherlini {#ch:resolvent-bounds}

The stability theory obtains its inverse bounds for the spectral families by Fredholm, compactness and contradiction
arguments, which give no number. This chapter makes the first of them explicit for one operator: the scalar wave
operator □ = δd on functions on five-dimensional Schwarzschild–Tangherlini, whose spectral family is invertible for
Im σ ≥ 0, σ ≠ 0 ([[lem:rb-scalar]]), and whose mode equation, the one solved in step (a) of the proof of
[[prop:iii-d-6-2]], is an ordinary differential equation harmonic by harmonic. For each harmonic the resolvent,
cut off to an interval about the photon sphere, is bounded with explicit constants: off the real axis by self-adjointness
([[lem:rb-off-axis]]); on the real axis first with a constant exponential in the harmonic's degree
([[prop:resolvent-outgoing]]), then uniformly in the degree where the potential barrier covers the interval
([[prop:rb-coercive]], [[cor:rb-closed-form]]) and where the frequency lies above the barrier
([[prop:resolvent-above-barrier]]); and then for every harmonic and every real frequency by multiplier identities of
Morawetz type ([[lem:morawetz-identity]]), with multipliers polynomial or rational in r⁻² whose weights are positive by
exact polynomial inequalities ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]],
[[prop:morawetz-polynomial]], [[prop:morawetz-harmonics]]). The same identities give one derivative
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
u(x) = e^(iσx) − ∫_x^∞ σ⁻¹ sin(σ(x − x′))V_l(x′)u(x′) dx′ have unique solutions by iteration, as in the fact stated
in the proof of [[prop:iii-d-6-2]]. They define the solutions u_h and u_∞ of −u″ + (V_l − σ²)u = 0 with

    u_h e^(iσr_*) → 1,  u_h′ + iσu_h → 0 as r_* → −∞;     u_∞ e^(−iσr_*) → 1,  u_∞′ − iσu_∞ → 0 as r_* → ∞,

the second limit in each case from the differentiated Volterra equation, whose remainder is bounded by the tail of
∫|V_l|. For real σ the same Volterra equations with e^(iσx) at −∞ and e^(−iσx) at +∞ give a second solution at each
end; so at each end every solution is Ae^(−iσr_*) + Be^(iσr_*) + o(1), with derivative
−iσAe^(−iσr_*) + iσBe^(iσr_*) + o(1). A solution with u′ + iσu → 0 at −∞ is a multiple of u_h, and one with
u′ − iσu → 0 at ∞ a multiple of u_∞. For real σ this holds because u′ + iσu = 2iσBe^(iσr_*) + o(1) at −∞, so that
B = 0, and likewise at +∞. For Im σ > 0, let u′ + iσu → 0 at −∞. Then (e^(iσx)u)′ = e^(iσx)(u′ + iσu) and the
modulus e^(−x Im σ) of e^(iσx) give |u(x)| ≤ C(e^(x Im σ) + 1/Im σ) near −∞, so u is bounded there; as u_h → 0 and
u_h′ + iσu_h → 0 at −∞, the constant Wronskian u_hu′ − u_h′u = u_h(u′ + iσu) − u(u_h′ + iσu_h) tends to 0, hence
vanishes, and u is a multiple of u_h. The same argument with e^(−iσx) applies at +∞. In the spacetime,
e^(−iσt)u_h = e^(−iσ(t + r_*))(1 + o(1)) is the behaviour of a field smooth across the future horizon, and
e^(−iσt)u_∞ = e^(−iσ(t − r_*))(1 + o(1)) that of an outgoing one: these are the classes of *The class* in the proof of
[[prop:iii-d-6-2]].

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

This bound is uniform in l and degenerates as Im σ → 0, where the content of [[lem:rb-scalar]] lies.

### The flux and the outgoing resolvent {#sec:rb-flux}

From here on σ is real and nonzero.

**Lemma {#lem:rb-flux}** (The flux.) Write u_h = A e^(−iσr_*) + B e^(iσr_*) + o(1) as r_* → ∞, with
u_h′ = −iσAe^(−iσr_*) + iσBe^(iσr_*) + o(1) (*Solutions at the ends* in [[sec:rb-radial]]). Then |A|² = 1 + |B|²,
and the Wronskian 𝒲 := u_h u_∞′ − u_h′ u_∞ equals 2iσA. In particular |𝒲| ≥ 2|σ|.

*Proof.* V_l is real, so Im(ūu′) is constant for every solution u. For u_h it is −σ at −∞, and −σ|A|² + σ|B|² at +∞,
the cross terms being real; so |A|² = 1 + |B|². 𝒲 is constant; at +∞, with u_∞ = e^(iσr_*)(1 + o(1)) and
u_∞′ = iσu_∞ + o(1),
𝒲 = (Ae^(−iσr_*) + Be^(iσr_*))iσe^(iσr_*) − (−iσAe^(−iσr_*) + iσBe^(iσr_*))e^(iσr_*) + o(1) = 2iσA. ∎

**Lemma {#lem:rb-growth}** (Growth through the barrier.) For a solution u of −u″ + (V_l − σ²)u = 0 put
E_σ := |u′|² + σ²|u|². Then |E_σ′| ≤ (V_l/|σ|)E_σ. Hence

    |u_∞(x)|² ≤ 2 exp(|σ|⁻¹ ∫_x^∞ V_l dr_*),     |u_h(x)|² ≤ 2 exp(|σ|⁻¹ ∫_(−∞)^x V_l dr_*).

*Proof.* E_σ′ = 2Re(ū′u″) + 2σ²Re(ūu′) = 2(V_l − σ²)Re(ū′u) + 2σ²Re(ūu′) = 2V_l Re(ū′u), and
2|ū′u| ≤ |u′|²/|σ| + |σ||u|² = E_σ/|σ|. E_σ tends to 2σ² at the end where u is normalised (u_∞ at +∞, u_h at −∞), so
Gronwall's inequality from that end gives E_σ ≤ 2σ² exp(|σ|⁻¹∫V_l) over the interval between the end and x, and
σ²|u|² ≤ E_σ. ∎

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

(b) For x ≤ x′, [[lem:rb-growth]] gives |u_h(x)||u_∞(x′)| ≤ 2 exp((2|σ|)⁻¹(∫_(−∞)^x V_l + ∫_(x′)^∞ V_l)) ≤
2 exp(I_l/(2|σ|)), as V_l ≥ 0, and |𝒲| ≥ 2|σ|. A kernel bounded by K on J × J defines an operator on L²(J) of norm at
most its Hilbert–Schmidt norm, KΛ_J. ∎

This is the injectivity of the scalar spectral family ([[lem:rb-scalar]]) at real σ on {r > r_h}, harmonic by
harmonic, which step (a) of the proof of [[prop:iii-d-6-2]] proves, here with a constant obtained by inequalities
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
½n′(u_h)(α) ≥ 0 and ½n′(u_∞)(β) ≤ 0; for x_1, x_2 as in [[lem:rb-end-signs]], the last two hold when
A_− ≥ D_−(x)/√2 and A_+ ≥ D_+(x′)/√2 for some x, x′ as there. Then ‖χ_I R_l(σ) χ_I‖ ≤ 1/c_I.

*Proof.* For F ∈ L² vanishing off I, u := R_l(σ)F equals c_h u_h on (−∞, α] and c_∞u_∞ on [β, ∞)
([[prop:resolvent-outgoing]]). Pairing −u″ + V_σ u = F with ū over I and taking real parts,

    ∫_I(|u′|² + V_σ|u|²) = Re∫_I Fū + |c_∞|² ½n′(u_∞)(β) − |c_h|² ½n′(u_h)(α) ≤ ‖F‖‖u‖_I,

and the left side is at least c_I‖u‖_I². ∎

**Corollary {#cor:rb-closed-form}** (Closed form; m = 1, I = {6/5 ≤ r ≤ 4}.) Let a := κ + 3/4 and c := (15/16)a. If

(i) (15/256)a > σ² and (0.21/1.4641)a > σ² (the second follows from the first, as 0.21/1.4641 > 0.1434 > 15/256),

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
σ = 1, 0.139, 0.0415, 0.0122 against 0.267, 0.0628, 0.0159; at σ = 3 and l = 32, 0.0135 against 0.0182. No proof uses
these values.

### Above the barrier {#sec:rb-above}

**Proposition {#prop:resolvent-above-barrier}** (Above the barrier.) Let m = 1. For every l, V_l, as a function of
r_*, has exactly one critical point, a maximum; write V_max := max V_l. If σ is real and σ² > V_max,
then |u_h|² ≤ 2σ²/(σ² − V_max) and |u_∞|² ≤ 2σ²/(σ² − V_max) everywhere. Hence, for every r_*-interval J of length Λ_J,

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
2.35, 4.44 at σ = 3, l = 0, …, 4. Between the two bounds, at σ = 3,
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
sections are not uniform in the harmonic exactly where the barrier top of a harmonic lies near σ² and the barrier does
not cover I. A multiplier identity of Morawetz type covers every harmonic and every real σ ≠ 0. Every multiplier of
[[sec:morawetz-identity]]–[[sec:morawetz-large-frequency]] is a polynomial or a rational function of r⁻², every
weight there is (1 − r⁻²)r⁻³ times a rational function of r⁻², and every constant is obtained from exact rational
inequalities; the band ([[sec:band]]) also uses the algebraic multipliers Φ(νz). The coefficient lists that the
Bernstein bounds below use are in [[sec:tb-morawetz]].

Throughout, y := 1/r² ∈ (0, 1), z := 1 − 2y ∈ (−1, 1) and η(y) := (1 − y)y^(3/2) = (r² − 1)/r⁵. The tortoise coordinate
r_* has dr_*/dr = 1/f, and g′ := dg/dr_*. Since dy/dr = −2y^(3/2),

    d/dr_* = −2η(y) d/dy.                                                                            {#eq:pb-tortoise}

As r_* → −∞, y → 1 and 1 − y decays like e^(2r_*); as r_* → ∞, r_* = r + O(r⁻¹). The interval I := {6/5 ≤ r ≤ 4} is
{1/16 ≤ y ≤ 25/36} = {−7/18 ≤ z ≤ 7/8}. With r_* = r + ½ log((r − 1)/(r + 1)), its length is
Λ := 14/5 + ½ log(33/5) < 3.7436. We write ‖·‖ for the norm of L²(ℝ, dr_*) and ‖·‖_I for that of L²(I, dr_*).

For a potential V as below, a real σ ≠ 0 and F ∈ L²(ℝ) vanishing outside I, R(σ)F is the outgoing solution of
−u″ + (V − σ²)u = F. Its construction in [[sec:rb-radial]] and [[prop:resolvent-outgoing]] (a) uses of V_l only that it
is real, smooth and integrable in r_*: the solutions u_h and u_∞ come from the Volterra equations, and their Wronskian
is not zero by [[lem:rb-flux]], whose proof uses only that V_l is real. So the construction applies verbatim to each V
below, and the proof of [[lem:morawetz-identity]] recalls it. R_l(σ) is R(σ) for V = V_l, and ‖χ_I R(σ) χ_I‖ is the
norm of F ↦ χ_I R(σ)F on L²(I).

Since η_y = y^(1/2)(3/2 − 5y/2), η increases on [0, 3/5] and decreases on [3/5, 1]; so on an interval of y its least
value is attained at an end. We use η(1/16) = 15/1024, η(1/2) = 2^(−5/2), η(25/36) = 1375/7776 > 2^(−5/2) (as
32 · 1375² > 7776²) and max η = η(3/5) = 6√15/125 < 0.18591. At a rational r, η = (r² − 1)/r⁵ is rational.

The potentials. Put U := f/r² = (1 − y)y, Q := f/r⁴ = (1 − y)y² and V_(a,b) := aU + bQ = (1 − y)(ay + by²). With
κ := l(l + 2), the potentials V_0, V_1, V_2 of [[prop:np-10-16]] at degree l, which we write V^□, V^v and V^s (those of
the scalar wave, of the vector-type and of the scalar-type 1-forms), are V_(κ+3/4,b) with b = 9/4, 5/4 and −7/4; so
V^□ = V_l. Those of [[thm:s15-ki]] are V_T = V^□ and V_V = V_(κ+3/4,−27/4), and V_S = (1 − y)yQ_S/(16H²), with Q_S the
polynomial [[eq:s15-ki-q]] at ς = y, p := κ − 3 and H := p + 6y, for l ≥ 2. Each of them is (1 − y)y times a rational
function of y bounded on [0, 1] (for V_S, H ≥ p > 0), so V and V′ = −2ηV_y are O(r⁻²) and O(r⁻³) as r_* → ∞ and
O(e^(2r_*)) as r_* → −∞: they are integrable and tend to 0 at ±∞.

**Lemma {#lem:morawetz-identity}** (The multiplier identity.) Let V be a real smooth function on ℝ with V, V′ integrable
and V, V′ → 0 at ±∞. Let φ and q be real smooth functions on ℝ, φ bounded with limits φ(±∞) at ±∞, and φ′, φ″, φ‴, q,
q′, q″ integrable and tending to 0 at ±∞. Let σ ≠ 0 be real, F ∈ L²(ℝ) vanish outside I, and let u be a solution, with
u and u′ locally absolutely continuous, of −u″ + (V − σ²)u = F (almost everywhere), such that u − c_±e^(±iσr_*) → 0 and
u′ ∓ iσu → 0 as r_* → ±∞. Then, with integrals over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2σ²∫q|u|² = Re∫F(2φū′ + (φ′ − 2q)ū) + 2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²),
    W := −φV′ − ½φ‴ + q″ − 2qV,                                                                      {#eq:pb-identity}

and σ(|c_+|² + |c_−|²) = −Im∫Fū. The outgoing solution R(σ)F is a solution of this kind.

Suppose moreover that φ′ − q ≥ 0, q ≥ 0 and W ≥ 0 on ℝ, and let m′ > 0, M′, w_I > 0, p_I and p_∞ satisfy
m′ ≤ φ′ − q, |φ′ − 2q| ≤ M′, w_I ≤ W and |φ| ≤ p_I on I, and p_∞ ≥ max(φ(∞), −φ(−∞), 0). Then X := ‖u′‖_I and
Y := ‖u‖_I satisfy

    Y ≤ B‖F‖,     B := ((2p_I²/m′ + (M′ + 2p_∞|σ|)²/w_I)/w_I)^(1/2);                               {#eq:pb-bound}

for every B̃ with Y ≤ B̃‖F‖, X ≤ X(B̃)‖F‖ with X(B̃) := (p_I + (p_I² + 2m′(M′ + 2p_∞|σ|)B̃)^(1/2))/(2m′); and for every
decomposition W = W_0 + W_1 with W_0, W_1 ≥ 0 on ℝ, ∫_I W_1|u|² ≤ (2p_IX(B̃) + (M′ + 2p_∞|σ|)B̃)‖F‖². When |φ| ≤ 1 on
ℝ one may take p_I = p_∞ = 1; then B = ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2) and
X(B̃) = (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′).

*Proof.* First, R(σ)F is a solution of this kind. Let u_h and u_∞ be the solutions of the homogeneous equation with
u_h − e^(−iσr_*) → 0 and u_h′ + iσu_h → 0 as r_* → −∞, and u_∞ − e^(iσr_*) → 0 and u_∞′ − iσu_∞ → 0 as r_* → ∞,
given by the Volterra equations of [[sec:rb-radial]] with V in place of V_l, and let 𝒲 := u_hu_∞′ − u_h′u_∞ be their
Wronskian, a nonzero constant by [[lem:rb-flux]], whose proof uses only that V is real. Then

    R(σ)F(x) = −𝒲⁻¹(u_∞(x)∫_(−∞)^x u_hF + u_h(x)∫_x^∞ u_∞F).

As F ∈ L² vanishes outside the bounded interval I and u_h, u_∞ are continuous, u_hF and u_∞F are integrable, and both
integrals are absolutely continuous in x. Differentiating, the two terms ±𝒲⁻¹u_∞u_hF cancel, so
u′ = −𝒲⁻¹(u_∞′∫_(−∞)^x u_hF + u_h′∫_x^∞ u_∞F), which is again absolutely continuous; differentiating once more,
u″ = (V − σ²)u − 𝒲⁻¹(u_hu_∞′ − u_h′u_∞)F = (V − σ²)u − F almost everywhere. To the right of I, u is a multiple of u_∞,
and to its left a multiple of u_h, which gives the stated behaviour at ±∞.

Now let u be any solution as in the statement. Since u and u′ are locally absolutely continuous and φ, q, V are smooth,
all the products below are locally absolutely continuous and the product rule holds for them almost everywhere. With
Re(u″ū) = ½(|u|²)″ − |u′|² and Re(u′ū) = ½(|u|²)′, one checks term by term, almost everywhere:

    Re(−u″ · 2φū′) = −(φ|u′|²)′ + φ′|u′|²,
    Re(−u″ · φ′ū) = −(φ′Re(u′ū))′ + φ′|u′|² + (½φ″|u|²)′ − ½φ‴|u|²,
    Re((V − σ²)u · 2φū′) = ((V − σ²)φ|u|²)′ − (φV′ + (V − σ²)φ′)|u|²,
    Re((V − σ²)u · φ′ū) = (V − σ²)φ′|u|²,
    Re((−u″ + (V − σ²)u) · (−2qū)) = (q(|u|²)′ − q′|u|²)′ + q″|u|² − 2q|u′|² − 2qV|u|² + 2σ²q|u|².

Adding, Re(F(2φū′ + (φ′ − 2q)ū)) = 2(φ′ − q)|u′|² + W|u|² + 2σ²q|u|² + E′ almost everywhere, where the locally
absolutely continuous function E is −φ|u′|² − φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² + q(|u|²)′ − q′|u|². The function u
is continuous with limits of modulus |c_±| at ±∞, and u′ continuous with limits of modulus |σc_±|; so both are bounded,
and every integral in [[eq:pb-identity]] converges absolutely, as F vanishes outside I and φ′, φ‴, q, q″, V′ and qV are
integrable. Integrate over [−R, R] and let R → ∞: at ±∞, |u′|² → σ²|c_±|², |u|² → |c_±|², Re(u′ū) → 0, φ → φ(±∞) and
φ′, φ″, q, q′, V → 0, so E → −2σ²φ(±∞)|c_±|², and [[eq:pb-identity]] follows. Next, almost everywhere,
Im(Fū) = −Im(u″ū) = −(Im(u′ū))′, and Im(u′ū) → ±σ|c_±|² at ±∞; integrating gives the flux identity.

Under the sign conditions every integrand on the left of [[eq:pb-identity]] is nonnegative. Dropping the term with q and
restricting the other two to I, the left side is at least 2m′X² + w_IY². On the right, F vanishes outside I
and |φ| ≤ p_I on I, so the integral is at most ‖F‖(2p_IX + M′Y); and
2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²) ≤ 2σ²p_∞(|c_+|² + |c_−|²) = −2σp_∞Im∫Fū ≤ 2|σ|p_∞‖F‖Y. Hence, with
M_σ := M′ + 2p_∞|σ|,

    2m′X² + w_IY² ≤ ‖F‖(2p_IX + M_σY).                                                                {#eq:pb-energy}

By the Cauchy–Schwarz inequality, 2p_IX + M_σY ≤ (2p_I²/m′ + M_σ²/w_I)^(1/2)(2m′X² + w_IY²)^(1/2), so
(2m′X² + w_IY²)^(1/2) ≤ (2p_I²/m′ + M_σ²/w_I)^(1/2)‖F‖ and w_I^(1/2)Y ≤ (2m′X² + w_IY²)^(1/2), which is [[eq:pb-bound]].
Dropping w_IY² in [[eq:pb-energy]] and using Y ≤ B̃‖F‖ gives 2m′X² − 2p_I‖F‖X − M_σB̃‖F‖² ≤ 0, so X is at most the
positive root, X(B̃)‖F‖. Finally the left side of [[eq:pb-identity]] is at least ∫_I W_1|u|², and the right side is at
most ‖F‖(2p_IX + M_σY) ≤ (2p_IX(B̃) + M_σB̃)‖F‖². When |φ| ≤ 1 on ℝ, also |φ(±∞)| ≤ 1, so p_I = p_∞ = 1 serve. ∎

For a multiplier φ = Θ(y) and a Lagrangian term q = ηg(y), [[eq:pb-tortoise]] gives φ′ = −2ηΘ_y,
−½φ‴ = 4η(η(ηΘ_y)_y)_y, −φV′ = 2ηΘV_y and, with h := (3/2 − 5y/2)g + y(1 − y)g_y, q′ = −2(1 − y)y²h and
q″ = 4ηy((2 − 3y)h + y(1 − y)h_y). So W = ηG with

    G = 2ΘV_y + 4(η(ηΘ_y)_y)_y + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV.                              {#eq:pb-weight-general}

Every φ below is a polynomial or a rational function of y with no pole on [0, 1], and every q is η times a polynomial g.
Since ηη_y = (1 − y)y²(3 − 5y)/2 and η² = (1 − y)²y³ are polynomials, φ′, φ″, φ‴, q, q′, q″ are η or (1 − y)y² times
bounded functions; they are O(r⁻³) as r_* → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

### The weight of the multiplier 1 − 2/r² {#sec:morawetz-algebraic-weight}

**Proposition {#prop:morawetz-weight}** (The Morawetz weight of φ = 1 − 2/r².) Let φ := z = 1 − 2/r². Then φ is
increasing, φ → ±1 at ±∞, φ′ = 4η, and for q = 0 and V = V_(a,b) the weight of [[lem:morawetz-identity]] is
W = ηP_(a,b)(z) with

    P_(a,b)(z) := 2 + (b/2 − 6)z + (2a + b − 6)z² + (10 − 3b/2)z³.                                     {#eq:pb-weight}

P_(a,b) is affine in b and nondecreasing in a, with ∂_aP_(a,b) = 2z², and ψ := −φU′ = 2ηz² ≥ 0. For the scalar wave at
harmonic l (a = κ + 3/4, b = 9/4) the weight is w_l := ηP_l with

    P_l(z) = P̄(z) + c_l z²,     P̄(z) := 2 − (39/8)z + (53/8)z³,     c_l := 2κ − 9/4,             {#eq:pb-weight-scalar}

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
at y = 0, p = 15. So p > 0 on [0, 1], w_1 > 0 on ℝ, and w_l ≥ w_1 because κ ≥ 3 and ψ ≥ 0. φ is increasing as φ′ =
4η > 0, and |φ| < 1. ∎

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

*Proof.* Write A := ηP̄ and Z := ηz², so that w_l = A + cZ by [[eq:pb-weight-scalar]], with c ≥ 15/4. P̄′(z) =
−39/8 + (159/8)z² vanishes on [0, 1] only at z_0 := (39/159)^(1/2) < 0.4953, and P̄(z_0) = 2 − (13/4)z_0 > 0.3902;
P̄ decreases on [0, z_0] and increases on [z_0, 1]. In the variable z, η = (1 + z)(1 − z)^(3/2)2^(−5/2) decreases on
[0, 7/8] (that is y ∈ [1/16, 1/2] ⊂ [0, 3/5]), and Z is unimodal on [0, 1], since
d log Z/dz = 1/(1 + z) − 3/(2(1 − z)) + 2/z is decreasing.

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

(iii) On 2 ≤ r ≤ 3, y ∈ [1/9, 1/4] and z ∈ [1/2, 7/9] ⊂ [z_0, 1]: η ≥ η(1/9) = 8/243 and P̄ ≥ P̄(1/2) = 25/64, so
A ≥ 25/1944; and Z ≥ min(Z at r = 3, Z at r = 2) = min(392/19683, 3/128). On 17/10 ≤ r ≤ 2, y ∈ [1/4, 100/289]:
η ≥ η(1/4) = 3/32 and P̄ ≥ P̄(z_0) > 0.3902, so A ≥ 0.03658; Z ≥ Z(17/10) = (189000/1419857)(89/289)² > 0.012624, as
Z(2) = 3/128 is larger. On 8/5 ≤ r ≤ 17/10, z ∈ [7/32, 89/289] ⊂ [0, z_0]: η ≥ η(17/10) = 189000/1419857 and
P̄ ≥ P̄(89/289) = 66831535/96550276, so A > 0.09213; Z ≥ Z(8/5) = (4875/32768)(49/1024) = 238875/33554432.

(iv) We show that A and Z increase with y on [1/16, 1/9], so that w_l, an increasing combination, does too. There
z ∈ [7/9, 7/8] ⊂ [z_0, 1], so P̄ decreases with y, and |dP̄/dy| = 2P̄′(z) = (159/4)z² − 39/4. Now
d log Z/dy = 3/(2y) − 1/(1 − y) − 4/(1 − 2y) ≥ 27/2 − 9/8 − 36/7 > 0, and
d log A/dy = 3/(2y) − 1/(1 − y) + (dP̄/dy)/P̄.
On y ∈ [1/16, 1/12] the last expression is at least 18 − 12/11 − (5295/256)/(3061/1728) > 5.2, using P̄(5/6) = 3061/1728
and (159/4)(7/8)² − 39/4 = 5295/256; on [1/12, 1/10] it is at least 15 − 10/9 − (857/48)/(373/250) > 1.9, using
P̄(4/5) = 373/250; on [1/10, 1/9] it is at least 27/2 − 9/8 − 15.69/P̄(7/9) > 0.53, using P̄(7/9) > 1.3254. Finally
η(1/16) = 15/1024, P̄(7/8) = 8899/4096 and (7/8)² = 49/64.

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

Each B_l is even in σ, increasing in |σ| and bounded as σ → 0. [[prop:morawetz-harmonics]] improves these values for
l ≥ 1 with the multipliers of [[sec:morawetz-polynomial]].

*Proof.* [[prop:morawetz-weight]] gives the hypotheses of [[lem:morawetz-identity]] with φ = z, q = 0, and |φ| ≤ 1, so
p_I = p_∞ = 1. On I, φ′ = 4η has least value 4 min(η(1/16), η(25/36)) = 15/256, so m′ = 15/256 and 2/m′ = 512/15, and
greatest value 4η(3/5) = 24√15/125 < 0.74362, since 3.873² > 15. So w_I ≥ ω_l by [[lem:morawetz-weight-interval]], and
[[eq:pb-bound]] gives the bound; it decreases in w_I and increases in M′. The table evaluates the formula, rounding up. ∎

### The harmonic l = 0 {#sec:morawetz-l-zero}

**Proposition {#prop:morawetz-l-zero}** (The harmonic l = 0.) Let φ := 1 − 2/r² and q := ½η(1 + 3y/2). Then
0 ≤ q ≤ (5/16)φ′, and for the scalar wave at l = 0, V = V_(3/4,9/4), the weight of [[lem:morawetz-identity]] is

    W = (3/8)ηQ_4,     Q_4(y) := 149y⁴ − 280y³ + 177y² − 42y + 4
                               = (2 − (21/2)y + 11y²)² + y²(28(y − 7/8)² + 21/16) > 0.          {#eq:pb-lzero-weight}

On I, m′ = min_I(φ′ − q) = 3315/65536, M′ = max_I|φ′ − 2q| < 0.3999 and w_I = W(4) = 5899185/536870912 > 0.010988. So
for every real σ ≠ 0, ‖χ_I R_0(σ) χ_I‖ ≤ B_0(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2), which is at most 70.17,
226.50, 585.53 and 1857.54 at σ → 0, σ = 1, 3 and 10. For the bound off the real axis of [[lem:morawetz-complex]],
which replaces 2|σ| by 4|σ| + 2 max q, max q = 2√6/27 < 0.18145, attained at y = 2/3.

*Proof.* q = ηg with g = (2 + 3y)/4 ≥ 0, and φ′ = 4η, so q/φ′ = (2 + 3y)/16 ≤ 5/16. In [[eq:pb-weight-general]],
h = (6 + 5y − 21y²)/8 and (2 − 3y)h + y(1 − y)h_y = (12 − 3y − 104y² + 105y³)/8, so the q″-term is
½y(12 − 3y − 104y² + 105y³). By [[prop:morawetz-weight]] the φ-terms give P_(3/4,9/4) = 3/2 − 21y + (141/2)y² − 53y³ in
the variable y, and −2gV_(3/4,9/4) = −(3/8)y(1 − y)(2 + 3y)(1 + 3y) = −(3/4)y − (21/8)y² + (27/8)y⁴. The sum is
(3/8)Q_4, and the second form of Q_4 is checked by expansion. In it, 28y² − 49y + 22.75 = 28(y − 7/8)² + 21/16 > 0, and
the two terms do not vanish together, since the second vanishes only at y = 0, where the first is 4.

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

Here Q_4(1/16) = 131093/65536, so W(4) = (3/8)(15/1024)(131093/65536). [[lem:morawetz-identity]] applies with
p_I = p_∞ = 1, as |φ| ≤ 1, and the bounds follow from [[eq:pb-bound]]. For max q: d/dy(η(2 + 3y)) =
y^(1/2)(3 + (5/2)y − (21/2)y²), which vanishes on (0, 1) only at y = 2/3, where q = (1/3)(2/3)^(3/2) = 2√6/27. ∎

### Off the real axis with a multiplier {#sec:morawetz-complex}

**Lemma {#lem:morawetz-complex}** (Off the real axis.) Let V ≥ 0 be real, smooth and bounded, with V and V′ integrable
and tending to 0 at ±∞, and let φ and q satisfy the hypotheses of [[lem:morawetz-identity]] on φ and q, its sign
conditions φ′ − q ≥ 0, q ≥ 0 and W ≥ 0 on ℝ included, and |φ| ≤ 1 on ℝ; put max q := sup_ℝ q, and let m′, M′ and w_I
be constants as there. Let Im σ > 0,
F ∈ L²(ℝ) vanish outside I, and let u := (−∂²_(r_*) + V − σ²)⁻¹F be the solution in L²(ℝ). Then

    ‖u‖_I ≤ B⁺(σ)‖F‖,     B⁺(σ) := ((2/m′ + (M′ + 4|σ| + 2 max q)²/w_I)/w_I)^(1/2),

and the bounds of [[lem:morawetz-identity]] for ‖u′‖_I and for ∫_I W_1|u|², with p_I = p_∞ = 1, hold with 2|σ|
replaced by 4|σ| + 2 max q. When q = 0, or when Re σ² ≥ 0, the term 2 max q may be dropped.
If instead |φ| ≤ p_φ on ℝ for a constant p_φ > 0, and the other hypotheses hold, then
‖u‖_I ≤ ((2p_φ²/m′ + (M′ + 4p_φ|σ| + 2 max q)²/w_I)/w_I)^(1/2)‖F‖.

*Proof.* Write σ² = a_σ + ib_σ. The operator −∂² + V is self-adjoint and nonnegative, so u ∈ H²(ℝ); off I, u solves
the homogeneous equation and lies in L², so near ±∞ it is a multiple of the solution that behaves like e^(±iσr_*),
which decays exponentially with its derivative. So every boundary term below vanishes and no flux term arises. Pair
−u″ + (V − a_σ)u − ib_σu = F with 2φū′ + (φ′ − 2q)ū and take real parts. The terms with V − a_σ give, by the
calculation in the proof of [[lem:morawetz-identity]] with σ² replaced by a_σ, the integrand
2(φ′ − q)|u′|² + W|u|² + 2a_σq|u|² plus an exact derivative; the new term gives
Re(−ib_σu(2φū′ + (φ′ − 2q)ū)) = 2b_σφ Im(uū′). Integrating over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2a_σ∫q|u|² = Re∫F(2φū′ + (φ′ − 2q)ū) − 2b_σ∫φ Im(uū′).

Integration by parts gives the energy identity ∫Fū = ‖u′‖² + ∫V|u|² − σ²‖u‖², norms over ℝ. Its imaginary part
gives |b_σ|‖u‖² ≤ ‖F‖‖u‖_I, and its real part, with V ≥ 0, ‖u′‖² ≤ ‖F‖‖u‖_I + a_+‖u‖², a_+ := max(a_σ, 0). As |φ| ≤ 1,

    |2b_σ∫φ Im(uū′)| ≤ 2|b_σ|‖u‖‖u′‖ ≤ 2|b_σ|‖u‖(‖F‖‖u‖_I)^(1/2) + 2|b_σ|a_+^(1/2)‖u‖²
                      ≤ 2(|b_σ|^(1/2) + a_+^(1/2))‖F‖‖u‖_I ≤ 4|σ|‖F‖‖u‖_I,

since |b_σ| = 2|Re σ| Im σ ≤ |σ|² and a_+^(1/2) ≤ |Re σ| ≤ |σ|. If a_σ ≥ 0 the term 2a_σ∫q|u|² is nonnegative and is
dropped; if a_σ < 0, the real part of the energy identity gives |a_σ|‖u‖² ≤ ‖F‖‖u‖_I, so
−2a_σ∫q|u|² ≤ 2 max q ‖F‖‖u‖_I, and this term is moved to the right. Then the left side is at least 2m′X² + w_IY²,
X := ‖u′‖_I, Y := ‖u‖_I, and, as |φ| ≤ 1 on I, the right side is at most ‖F‖(2X + (M′ + 4|σ| + 2 max q)Y); the rest is
the algebra of the proof of [[lem:morawetz-identity]] with p_I = p_∞ = 1, with M′ + 4|σ| + 2 max q in place of
M′ + 2|σ|. For the last statement, φ/p_φ and q/p_φ satisfy the hypotheses with |φ/p_φ| ≤ 1; since W, φ′ − q and
φ′ − 2q are linear in (φ, q), their constants are m′/p_φ, M′/p_φ, w_I/p_φ and max q/p_φ, and the bound just proved for
them is the one stated. ∎

So the real-axis bounds are stable under Im σ > 0: B⁺ is continuous in σ and bounded on compact subsets of
{Im σ ≥ 0, σ ≠ 0}, and the degeneration of [[lem:rb-off-axis]] as Im σ → 0 is not met. As Im σ → 0, B⁺ tends to the
constant with 4|σ|, not to the real-axis one: the factor 2 is the price of bounding the b_σ-term by norms over ℝ. The
lemma applies directly to the multiplier φ = z, which has |z| < 1, with q = 0 for l ≥ 1
([[prop:morawetz-resolvent-l-ge-1]]) and max q = 2√6/27 for l = 0 ([[prop:morawetz-l-zero]]), and in the scaled form,
with p_φ := sup_ℝ|φ|, to the multipliers of [[prop:morawetz-master-potentials]], as stated there.

### Polynomial multipliers {#sec:morawetz-polynomial}

**Lemma {#lem:bernstein-lower-bound}** (Bernstein lower bound.) Let p be a polynomial of degree at most n and α < β.
Write p(α + (β − α)t) = Σ_(j≤n) c_j t^j and b_k := Σ_(j≤k) (C(k, j)/C(n, j))c_j for 0 ≤ k ≤ n. Then
min_k b_k ≤ p ≤ max_k b_k on [α, β]; in particular |p| ≤ max_k |b_k| there.

*Proof.* Expanding t^j = t^j(t + (1 − t))^(n−j) by the binomial theorem gives
t^j = Σ_(k≥j) (C(k, j)/C(n, j))C(n, k)t^k(1 − t)^(n−k), as C(n − j, k − j)/C(n, k) = C(k, j)/C(n, j). So
p(α + (β − α)t) = Σ_k b_k C(n, k)t^k(1 − t)^(n−k), a combination of the b_k with nonnegative weights of sum 1 on
t ∈ [0, 1]. ∎

**Lemma {#lem:morawetz-polynomial-weight}** (The weight of a polynomial multiplier.) Let Θ be a real polynomial in z
and g a real polynomial in y, with g ≥ 0 and 4Θ_z(1 − 2y) − g(y) ≥ 0 for 0 ≤ y ≤ 1, and put φ := Θ(z) and q := ηg. Then
φ and q satisfy the hypotheses of [[lem:morawetz-identity]] on φ and q, with φ(±∞) = Θ(±1); and q ≥ 0, φ′ = 4ηΘ_z,
φ′ − q = η(4Θ_z − g) ≥ 0 and φ′ − 2q = η(4Θ_z − 2g) on ℝ, the derivatives of Θ taken at z = 1 − 2y. For V = V_(a,b) or
V = V_S the weight of [[lem:morawetz-identity]] is W = ηG with

    G = 2ΘV_y − 8y(10y² − 12y + 3)Θ_z + 24(1 − y)y²(3 − 5y)Θ_zz − 32(1 − y)²y³Θ_zzz
        + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV,                                                        {#eq:pb-weight-poly}

with h as in [[eq:pb-weight-general]]. If g = 0 and Θ(0) = 0, then zΘ ≥ 0 on [−1, 1], and for V = V_(a,b) the polynomial
G is affine in b and nondecreasing in a, with ∂_aG = 2zΘ; the a-part of W is a(−φU′), with −φU′ = 2ηzΘ ≥ 0.

*Proof.* φ is smooth and bounded, and z → ±1 as r_* → ±∞, so φ(±∞) = Θ(±1). By the remark after
[[eq:pb-weight-general]], φ′, φ″, φ‴, q, q′, q″ are integrable and tend to 0 at ±∞. With Θ_y = −2Θ_z,
[[eq:pb-tortoise]] gives φ′ = 4ηΘ_z, and the identities for φ′ − q and φ′ − 2q follow. Next,
4(η(ηΘ_y)_y)_y = 4(η_y² + ηη_yy)Θ_y + 12ηη_yΘ_yy + 4η²Θ_yyy, since (η²)_y = 2ηη_y; substituting Θ_y = −2Θ_z,
Θ_yy = 4Θ_zz, Θ_yyy = −8Θ_zzz, η_y² + ηη_yy = y(10y² − 12y + 3) (proof of [[prop:morawetz-weight]]),
ηη_y = (1 − y)y²(3 − 5y)/2 and η² = (1 − y)²y³ gives the Θ-terms of [[eq:pb-weight-poly]]; the others are those of
[[eq:pb-weight-general]]. If Θ(0) = 0 and Θ_z ≥ 0 on [−1, 1] (which holds when g = 0), Θ(z) has the sign of z. With
g = 0, G is linear in (a, b) up to an a- and b-free term, and the coefficient of a is 2ΘU_y = 2zΘ, since U_y = z;
−φU′ = 2ηΘU_y = 2ηzΘ. ∎

**Proposition {#prop:morawetz-polynomial}** (Five polynomial multipliers.) Let

    Θ_A := z + (3/16)z² − (7/40)z³,               Θ_B := z + (9/20)z² − (17/120)z³ − (1/12)z⁴,
    Θ_E := z − z³/3,                               Θ_C := z + (11/24)z² − (9/40)z³ − (17/60)z⁴,
    Θ_T := z + (7/20)z² − (3/40)z⁴,

with g = 0 for Θ_A, Θ_B, Θ_E and Θ_C, and g = y/2 for Θ_T, so that q = 0, respectively q = ηy/2. Each pair (Θ, g)
satisfies the hypotheses of [[lem:morawetz-polynomial-weight]], and the constants of [[lem:morawetz-identity]] may be
taken as follows:

| multiplier | m′ | M′ | p_I | p_∞ | max q |
|---|---|---|---|---|---|
| Θ_A | 0.0537 | 0.72 | 18459/20480 | 81/80 | 0 |
| Θ_B | 0.0718 | 0.735 | 264383/245760 | 49/40 | 0 |
| Θ_E | 0.0135 | 0.735 | 1001/1536 | 2/3 | 0 |
| Θ_C | 0.0305 | 0.735 | 74473/81920 | 19/20 | 0 |
| Θ_T | 0.0814 | 0.65 | 180061/163840 | 51/40 | (1/7)(5/7)^(5/2) < 0.06161 |

For the operators of each row below, W > 0 on ℝ, w_I is at least the value listed, and so, for every real σ ≠ 0 and
every harmonic of the row, ‖χ_I R(σ) χ_I‖ ≤ B(σ) := ((2p_I²/m′ + (M′ + 2p_∞|σ|)²/w_I)/w_I)^(1/2) with the constants of
the row's multiplier; B is even in σ and increasing in |σ|, and its values at σ → 0, σ = 1, 3 and 10 are at most:

| row | operators | multiplier | w_I ≥ | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|---|
| A | V_(a,b), a ≥ 15/4, 5/4 ≤ b ≤ 9/4 | Θ_A | 0.0728 | 22.66 | 42.87 | 95.54 | 288.77 |
| A′ | V_(a,9/4), a ≥ 15/4 | Θ_A | 0.0756 | 22.16 | 41.46 | 92.09 | 278.11 |
| B | V_(a,b), a ≥ 35/4, −7/4 ≤ b ≤ 9/4 | Θ_B | 0.211 | 12.85 | 19.51 | 40.27 | 120.24 |
| B′ | V_(a,9/4), a ≥ 35/4 | Θ_B | 0.224 | 12.44 | 18.61 | 38.04 | 113.30 |
| E | V_(a,9/4), a ≥ 35/4 | Θ_E | 0.139 | 21.93 | 25.97 | 40.17 | 103.43 |
| C | V_(a,b), a ≥ 63/4, −27/4 ≤ b ≤ 9/4 | Θ_C | 0.325 | 13.11 | 15.25 | 23.64 | 62.09 |
| C3 | V_(a,9/4), a ≥ 63/4 | Θ_C | 0.352 | 12.59 | 14.50 | 22.10 | 57.43 |
| C4 | V_(a,9/4), a ≥ 99/4 | Θ_C | 0.559 | 9.94 | 10.92 | 15.15 | 36.66 |
| C5 | V_(a,9/4), a ≥ 143/4 | Θ_C | 0.80 | 8.29 | 8.87 | 11.51 | 26.01 |
| C6 | V_(a,9/4), a ≥ 195/4 | Θ_C | 0.815 | 8.21 | 8.78 | 11.36 | 25.56 |
| S3 | V_S, l = 3 | Θ_C | 0.302 | 13.62 | 15.99 | 25.17 | 66.71 |
| S4 | V_S, every l ≥ 4 | Θ_C | 0.515 | 10.36 | 11.47 | 16.17 | 39.67 |
| T2 | V_V, l = 2 | Θ_T | 0.19 | 12.96 | 20.98 | 45.44 | 138.20 |

At the harmonic l the scalar wave is V_(a,9/4) with a = κ + 3/4, which is 15/4, 35/4, 63/4, 99/4, 143/4 and 195/4 at
l = 1, …, 6; so rows A′, B′ and E, C3, C4, C5 and C6 serve every l ≥ 1, 2, 3, 4, 5 and 6 respectively.

*Proof.* The hypotheses. Θ_E has Θ_z = 1 − z² ≥ 0. For Θ_A, Θ_B, Θ_C and Θ_T the Bernstein coefficients of Θ_z on [−1, 1]
(on [−1, 0] and [0, 1] for Θ_C) are positive ([[sec:tb-morawetz-monotone]]), so Θ_z > 0 on [−1, 1] by
[[lem:bernstein-lower-bound]]. For Θ_T, g = y/2 ≥ 0, and the Bernstein coefficients of 4Θ_z(1 − 2y) − y/2 on [0, 1] are
positive. So [[lem:morawetz-polynomial-weight]] applies to each pair. Each Θ is increasing on [−1, 1], so on
I, |Θ| ≤ max(|Θ(7/8)|, |Θ(−7/18)|) = Θ(7/8), and φ(±∞) = Θ(±1); these values are listed in [[sec:tb-morawetz-monotone]]
and give p_I and p_∞. For Θ_T, q = ½(1 − y)y^(5/2), whose derivative ¼y^(3/2)(5 − 7y) vanishes on (0, 1) only at y = 5/7.

The weights. By [[lem:morawetz-polynomial-weight]], W = ηG with G of [[eq:pb-weight-poly]], a polynomial in y for
V = V_(a,b). [[sec:tb-morawetz-weights]] lists G at the corners A1 = (15/4, 5/4), A2 = (15/4, 9/4), B1 = (35/4, −7/4),
B2 = (35/4, 9/4), C1 = (63/4, −27/4), C3 = (63/4, 9/4), C4 = (99/4, 9/4), C5 = (143/4, 9/4) and C6 = (195/4, 9/4) of
their multipliers, G for Θ_E at (35/4, 9/4) (E2), G for Θ_T and V_V at l = 2, that is (35/4, −27/4) (T2), and, for V_S
at l = 3, where p = 12 and H = 6(2 + y), the polynomial Π := 120(2 + y)³G (S3). Their Bernstein coefficients on the
subintervals of [0, 1] listed in [[sec:tb-morawetz-positivity]] are positive, so each is positive on [0, 1] by
[[lem:bernstein-lower-bound]], and W > 0 on ℝ. For Θ_A, Θ_B, Θ_E and Θ_C, g = 0 and Θ(0) = 0, so G is nondecreasing in a
and affine in b: in row A, for a ≥ 15/4 and 5/4 ≤ b ≤ 9/4, G is at least the smaller of its values at A1 and A2, on ℝ
and on I; in the same way rows B and C reduce to the corners B1, B2 and C1, C3, and rows A′, B′, E, C3, C4, C5 and C6
to the single corners A2, B2, E2, C3, C4, C5 and C6.

Row S4. Here κ ≥ 24, p = κ − 3 = 21 + t with t := κ − 24 ≥ 0, and H = H_0 + t with H_0 := 21 + 6y. Expanding,
16H³G = Σ_(j≤4) c_j(y)t^j with the polynomials c_0, …, c_4 of [[sec:tb-morawetz-weights]]; c_4 = 32zΘ_C(z) ≥ 0 by
[[lem:morawetz-polynomial-weight]], and c_0, …, c_3 have positive Bernstein coefficients on [0, 1/2] and [1/2, 1]
([[sec:tb-morawetz-positivity]]), so they are positive on [0, 1]. Since (H_0 + t)³ = Σ_(j≤3) C(3, j)H_0^(3−j)t^j,

    G ≥ k_S(y) := min_(j≤3) c_j/(16C(3, j)H_0^(3−j)) > 0     for every t ≥ 0,

uniformly in l ≥ 4.

The lower bounds for w_I. In each row the pieces of [[sec:tb-morawetz-pieces]] cover I, and on a piece
w = ηG ≥ (least value of η)(least Bernstein coefficient of G) by [[lem:bernstein-lower-bound]], since that coefficient
is positive on every piece listed, the least value of η being attained at an end of the piece
([[sec:morawetz-identity]]); in rows with two corners this is done for each corner.
For S3 the least coefficient of Π is divided by 120(2 + y)³ at the right end of the piece, its largest value there; for
S4, k_S is bounded below by the least Bernstein coefficients of c_0, …, c_3 with H_0 at the right end of the piece. Every
product listed is at least the w_I of its row.

The constants m′ and M′. On the pieces of [[sec:tb-morawetz-constants]], η(4Θ_z − g) is bounded below by the least
value of η times the least Bernstein coefficient of 4Θ_z − g, and |η(4Θ_z − 2g)| above by the largest value of η times
the largest modulus of a Bernstein coefficient of 4Θ_z − 2g. Every product is at least m′, respectively at most M′.

Finally [[eq:pb-bound]] gives the bound for each operator of a row and every harmonic of it, and the table evaluates it
with the constants above, rounding up. ∎

### Every harmonic of the scalar wave {#sec:morawetz-harmonics}

**Proposition {#prop:morawetz-harmonics}** (The scalar wave at every harmonic.) (i) For l ≥ 1 let B*_l(σ) be the least of
B_l(σ) of [[prop:morawetz-resolvent-l-ge-1]] and the bounds B(σ) of the rows A′ (l ≥ 1), B′ and E (l ≥ 2), C3 (l ≥ 3),
C4 (l ≥ 4), C5 (l ≥ 5) and C6 (l ≥ 6) of [[prop:morawetz-polynomial]], each taken when l is in its range. Then for every
real σ ≠ 0, ‖χ_I R_l(σ) χ_I‖ ≤ B*_l(σ); B*_l is even in σ, increasing in |σ| and bounded as σ → 0; and for l ≥ 6,
B*_l is at most the least of B_6 and the bound of row C6, which the line "every l ≥ 6" below evaluates.

(ii) For l = 0 put B*_0(σ) := B_0(σ) of [[prop:morawetz-l-zero]] for 0 < |σ| < 1, and
B*_0(σ) := min(B_0(σ), Λ|σ|/(σ² − 25/48)) for |σ| ≥ 1. Then ‖χ_I R_0(σ) χ_I‖ ≤ B*_0(σ), and B*_0(σ) < 7.8128
for |σ| ≥ 1.

At σ → 0 and |σ| = 1/2, 1, 2, 3 and 10, B*_l is at most:

| l | σ → 0 | 1/2 | 1 | 2 | 3 | 10 |
|---|---|---|---|---|---|---|
| 0 | 70.17 | 140.82 | 7.82 | 2.16 | 1.33 | 0.38 |
| 1 | 22.16 | 30.43 | 41.46 | 66.20 | 92.09 | 278.11 |
| 2 | 12.44 | 14.85 | 18.61 | 27.88 | 38.04 | 103.43 |
| 3 | 11.26 | 12.55 | 14.50 | 17.89 | 22.10 | 57.43 |
| 4 | 9.94 | 10.30 | 10.92 | 12.76 | 15.15 | 36.66 |
| 5 | 8.29 | 8.50 | 8.87 | 10.00 | 11.51 | 26.01 |
| every l ≥ 6 | 8.21 | 8.42 | 8.78 | 9.88 | 11.36 | 25.56 |

*Proof.* (i) By the last sentence of [[prop:morawetz-polynomial]], each listed row contains V_(κ+3/4,9/4) for the l in
its range, and each bound is even in σ and increasing in |σ|, hence so is their least. For l ≥ 6, rows C6 and
[[prop:morawetz-resolvent-l-ge-1]] give bounds independent of l. The entries come from row A′ at l = 1; from row B′ at
l = 2, except at σ = 10, from row E; from [[prop:morawetz-resolvent-l-ge-1]] at l = 3 for σ → 0 and |σ| = 1/2, and from
row C3 otherwise; and from rows C4, C5 and C6 at l = 4, 5 and every l ≥ 6. At |σ| = 1/2 and 2 they evaluate
[[eq:pb-bound]] with the constants of those rows, rounding up.

(ii) max V_(a,b) ≤ a max U + b max Q = a/4 + 4b/27 for a, b ≥ 0, since U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27; at
l = 0 this is 3/16 + 1/3 = 25/48 < 1. For σ² > max V_0 the bound above the barrier, [[prop:resolvent-above-barrier]],
gives ‖χ_I R_0(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_0) ≤ Λ|σ|/(σ² − 25/48). As Λt/(t² − 25/48) decreases for t² > 25/48, its value
for |σ| ≥ 1 is at most Λ/(23/48) < 3.7436 · 48/23 < 7.8128. The entries at l = 0 are B_0(0+) and B_0(1/2) of
[[prop:morawetz-l-zero]] and 3.7436|σ|/(σ² − 25/48) at |σ| = 1, 2, 3, 10, rounded up. ∎

At |σ| ≥ 3 the bound above the barrier also improves the entries for 1 ≤ l ≤ 4 ([[prop:morawetz-large-frequency]]); the
estimates below use B*_l for l ≥ 1 because it is increasing in |σ|.

### One derivative {#sec:morawetz-one-derivative}

**Corollary {#cor:morawetz-one-derivative}** (The H¹ constants.) Let σ ≠ 0 be real, F ∈ L²(ℝ) vanish outside I, and
u = R_l(σ)F, with ψ = 2ηz² the weight of [[prop:morawetz-weight]], which vanishes on ℝ only at the photon sphere
r = √2, to second order. Let B*_l be as in [[prop:morawetz-harmonics]].

(a) For l ≥ 1, with m′ = 15/256 and M′ = 0.74362, ‖u′‖_I ≤ X_l‖F‖ and (κ − 3)∫_Iψ|u|² ≤ J_l‖F‖², where
X_l := (1 + (1 + 2m′(M′ + 2|σ|)B*_l)^(1/2))/(2m′) and J_l := 2X_l + (M′ + 2|σ|)B*_l. Put A_l := κJ_l/(κ − 3) for
l ≥ 2, A_1 := 3(B*_1)² and C_l := (X_l² + A_l)^(1/2). At σ = 3, each line bounding its quantity from the lines above it:

| l | 1 | 2 | 3 | 4 | 5 | ≥ 6 |
|---|---|---|---|---|---|---|
| B*_l(3) ≤ | 92.081 | 38.036 | 22.095 | 15.149 | 11.509 | 11.351 |
| X_l ≤ | 81.826 | 56.090 | 45.198 | 39.268 | 35.647 | 35.479 |
| J_l ≤ | — | 368.69 | 239.40 | 180.70 | 148.91 | 147.51 |
| A_l ≤ | 25,436.8 | 590.0 | 299.3 | 206.6 | 162.9 | 157.4 |
| C_l ≤ | 179.26 | 61.13 | 48.40 | 41.82 | 37.87 | 37.64 |

(b) For l = 0, with m′_0 := 3315/65536 and M′_0 := 0.3999 of [[prop:morawetz-l-zero]], ‖u′‖_I ≤ X_0‖F‖ with
X_0 := (1 + (1 + 2m′_0(M′_0 + 2|σ|)B*_0)^(1/2))/(2m′_0). X_0 ≤ 83.85 for every real 0 < |σ| ≤ 3, and X_0(3) < 23.36.

(c) Summed over the harmonics. Let F ∈ L²(I × 𝕊³), extended by zero to ℝ × 𝕊³, where here and in (d) every norm on
I × 𝕊³ or ℝ × 𝕊³ is taken with the measure dr_* dω, dω the round measure of 𝕊³. Let F_l(r_*, ·) be the orthogonal
projection of F(r_*, ·) onto 𝒮_l ⊗ ℂ, the eigenspace of −Δ_(𝕊³) with eigenvalue κ = l(l + 2), let
u_l := R_l(σ)F_l, R_l(σ) acting in r_*, and u := Σ_l u_l. For every real 0 < |σ| ≤ 3 the series Σ_l u_l and
Σ_l ∂_(r_*)u_l converge in L²(I × 𝕊³), the second to the weak derivative ∂_(r_*)u on the interior of I × 𝕊³, and

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖F‖²,     C ≤ 179.26,

over every l ≥ 0, where the term at l = 1 is taken unweighted, as 3‖u_1‖_I². At |σ| = 1/2, 1, 2 and 3 one may take
C = C_1, that is 61.37, 82.61, 129.87 and 179.26: there max_(l≥2) C_l = C_2 is at most 27.98, 33.88, 47.07 and 61.13,
and X_0 at most 55.13, 26.71, 23.72 and 23.36.

(d) Without the weight: for F as in (c) and every real 0 < |σ| ≤ 3, ‖∂_(r_*)u‖_I² + Σ_l κ‖u_l‖_I² ≤ C_u²‖F‖² with
C_u < 568.55.

*Proof.* (a) and (b) are [[lem:morawetz-identity]] with B̃ = B*_l, applied to φ = z with q = 0 for l ≥ 1 and to the
multiplier of [[prop:morawetz-l-zero]] for l = 0, both with p_I = p_∞ = 1. In (a), W_1 := (κ − 3)ψ and W_0 := w_1 are
nonnegative ([[prop:morawetz-weight]]); so (κ − 3)∫_Iψ|u|² ≤ J_l‖F‖², and κ∫_Iψ|u|² ≤ A_l‖F‖² for l ≥ 2. At l = 1,
3‖u‖_I² ≤ 3(B*_1)²‖F‖². For l ≥ 6, B*_l is at most the line "every l ≥ 6" of [[prop:morawetz-harmonics]], X_l and J_l
increase with B*_l, and κ/(κ − 3) decreases, so C_l ≤ C_6. In the table each entry is evaluated from the rounded entries
above it and rounded up. In (b), for 0 < |σ| ≤ 1, X_0 increases with |σ| and with B*_0 ≤ B_0 ≤ B_0(1) < 226.50, so
X_0 ≤ (1 + (1 + (3315/32768)(2.3999)(226.50))^(1/2))(32768/3315) < 83.85; for 1 ≤ |σ| ≤ 3, B*_0 < 7.8128 and |σ| ≤ 3
give X_0 ≤ (1 + (1 + (3315/32768)(6.3999)(7.8128))^(1/2))(32768/3315) < 34.22. At |σ| = 3, B*_0 < 1.3246 gives
X_0 < 23.36.

(c) *The harmonic components.* Let (S_(l,k))_k be an orthonormal basis of 𝒮_l ⊗ ℂ in L²(𝕊³), finite for each l, and
F_(l,k)(r_*) := ∫_(𝕊³) F(r_*, ω) conj(S_(l,k)(ω)) dω. By the Cauchy–Schwarz inequality and Fubini's theorem F_(l,k) lies
in L²(ℝ) and vanishes outside I, and F_l = Σ_k F_(l,k)S_(l,k). The S_(l,k), over all l and k, form an orthonormal basis
of L²(𝕊³), so by Parseval's identity for almost every r_* and integration in r_* (monotone convergence),
‖F‖² = Σ_l ‖F_l‖² and ‖F_l‖² = Σ_k ‖F_(l,k)‖². By definition u_l = Σ_k (R_l(σ)F_(l,k))S_(l,k), each R_l(σ)F_(l,k) a
solution as in [[lem:morawetz-identity]], so u_l and ∂_(r_*)u_l = Σ_k (R_l(σ)F_(l,k))′S_(l,k) are defined on ℝ × 𝕊³,
and since the S_(l,k) are orthonormal for each fixed r_*,

    ‖u_l‖_I² = Σ_k ‖R_l(σ)F_(l,k)‖_I²,     ‖∂_(r_*)u_l‖_I² = Σ_k ‖(R_l(σ)F_(l,k))′‖_I²,
    ∫_I ψ|u_l|² = Σ_k ∫_I ψ|R_l(σ)F_(l,k)|².

*The bound for each harmonic.* Applying [[prop:morawetz-harmonics]], (a) and (b) to each F_(l,k) and summing over k,
‖u_l‖_I ≤ B*_l‖F_l‖ and ‖∂_(r_*)u_l‖_I ≤ X_l‖F_l‖ for every l ≥ 0; for l ≥ 2, ‖∂_(r_*)u_l‖_I² + κ∫_Iψ|u_l|² ≤
(X_l² + A_l)‖F_l‖² = C_l²‖F_l‖²; at l = 1, ‖∂_(r_*)u_1‖_I² + 3‖u_1‖_I² ≤ (X_1² + 3(B*_1)²)‖F_1‖² = C_1²‖F_1‖²; and at
l = 0, where κ = 0, ‖∂_(r_*)u_0‖_I² ≤ X_0²‖F_0‖².

*The constants are uniform in l.* B*_l is increasing in |σ| ([[prop:morawetz-harmonics]]), and X_l, J_l, A_l and C_l
increase with |σ| and with B*_l; so for 0 < |σ| ≤ 3 each is at most its value at |σ| = 3, and C_l(σ) ≤ C_l(3) ≤ 179.26
for every l ≥ 1, by the table (for l ≥ 6, C_l ≤ C_6). Also X_0 ≤ 83.85 by (b). Moreover B*_l ≤ B_l(σ) ≤ B_1(σ) for
l ≥ 1, as ω_l ≥ ω_1 in [[prop:morawetz-resolvent-l-ge-1]], so b := max(B*_0(σ), B_1(σ)) and
x := max(X_0, X(B_1(σ))), with X(B̃) := (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′), the bound of
[[lem:morawetz-identity]] with the constants of (a), bound B*_l and X_l for every l ≥ 0.

*Convergence.* For l ≠ l′ and almost every r_*, u_l(r_*, ·) ∈ 𝒮_l ⊗ ℂ and u_(l′)(r_*, ·) ∈ 𝒮_(l′) ⊗ ℂ are orthogonal
in L²(𝕊³), and so are ∂_(r_*)u_l(r_*, ·) and ∂_(r_*)u_(l′)(r_*, ·); integrating over I, the u_l are mutually orthogonal
in L²(I × 𝕊³), and so are the ∂_(r_*)u_l. Hence for every finite set L of harmonics
‖Σ_(l∈L) u_l‖_I² = Σ_(l∈L) ‖u_l‖_I² ≤ b² Σ_(l∈L) ‖F_l‖² and ‖Σ_(l∈L) ∂_(r_*)u_l‖_I² ≤ x² Σ_(l∈L) ‖F_l‖². As
Σ_l ‖F_l‖² = ‖F‖² < ∞, the partial sums of both series are Cauchy sequences in L²(I × 𝕊³), so both series converge
there; let v be the sum of the second. For a smooth function χ with compact support in the interior of I × 𝕊³, each
R_l(σ)F_(l,k) is absolutely continuous in r_*, so ∫u_l ∂_(r_*)χ = −∫(∂_(r_*)u_l)χ; summing over l and passing to the
limit in L² gives ∫u ∂_(r_*)χ = −∫vχ, that is ∂_(r_*)u = v weakly. By orthogonality and the continuity of the norm,
‖∂_(r_*)u‖_I² = Σ_l ‖∂_(r_*)u_l‖_I².

*The sum.* Adding the bounds for each harmonic,
‖∂_(r_*)u‖_I² + Σ_l κ∫_Iψ|u_l|² ≤ Σ_(l≥1) C_l²‖F_l‖² + X_0²‖F_0‖² ≤ max(sup_(l≥1) C_l, X_0)²‖F‖², and the maximum is at
most 179.26. At |σ| = 1/2, 1 and 2, B*_l ≤ B*_2 for l ≥ 2 (every bound that serves l = 2 in
[[prop:morawetz-harmonics]] serves every l ≥ 2, and B_l ≤ B_2), so X_l ≤ X_2, J_l ≤ J_2 and, as κ/(κ − 3) decreases,
C_l ≤ C_2 for l ≥ 2. The same evaluation of (a) and (b) with the bounds of [[prop:morawetz-harmonics]] at that σ gives
the values listed; they are evaluated from B*_1(1/2) < 30.4202, B*_1(1) < 41.46, B*_1(2) < 66.1908, B*_2(1/2) < 14.85,
B*_2(1) < 18.61, B*_2(2) < 27.88, B*_0(1/2) < 140.82, B*_0(1) < 7.8128 and B*_0(2) < 2.1521, the values of
[[prop:morawetz-harmonics]] computed from the rows' constants; its table rounds them up to two decimals, which is too
coarse to reproduce C_1 at |σ| = 1/2 and 2 and X_0 at |σ| = 1 and 2.

(d) As in (c), for each l ≥ 1 and every B̃_l with ‖χ_I R_l(σ) χ_I‖ ≤ B̃_l,
‖∂_(r_*)u_l‖_I² + κ‖u_l‖_I² ≤ (X(B̃_l)² + κB̃_l²)‖F_l‖², with X(B̃) as in (c); and
‖∂_(r_*)u_0‖_I² ≤ X_0²‖F_0‖² ≤ 83.85²‖F_0‖². By the orthogonality of (c), the left side is at most the largest of these
factors times ‖F‖². X(B̃) increases with |σ| and with B̃.

For l ≥ 50 we use the closed-form bound for large harmonics, [[cor:rb-closed-form]]: with c := (15/16)(κ + 3/4),
‖χ_I R_l(σ) χ_I‖ ≤ B̃_l := 1/((15/256)(κ + 3/4) − σ²) whenever (15/256)(κ + 3/4) > σ² and
(0.21/1.4641)(κ + 3/4) > σ²; 0.32727(0.120523(κ + 3/4) − σ²)^(1/2) > (2 + 1.1248|σ|)/√2; and c^(1/2) > 8|σ| and
(√3/2)c^(1/2) log(c^(1/2)/(8|σ|)) > (2 + 0.79217(κ + 1)^(1/2))/√2. At l = 50 (κ + 3/4 = 2600.75) and |σ| = 3 these
read 152.38 > 9 and 373.0 > 9; 0.32727(313.45 − 9)^(1/2) > 5.71 > (2 + 3.3744)/√2; and c > 2438.2,
c^(1/2) > 49.37 > 24 and (√3/2)(49.37) log(49.37/24) > 30.8 > 29.99 > (2 + 0.79217 · 51)/√2. Each condition becomes
easier as l grows or |σ| decreases, so the bound holds for l ≥ 50 and 0 < |σ| ≤ 3, and there
B̃_l ≤ 1/((15/256)(κ + 3/4) − 9) ≤ 0.006975. At l = 50 and |σ| = 3, X(B̃_l)² < 292.1 and κB̃_l² < 0.127, so
X(B̃_l)² + κB̃_l² < 17.1²; both terms decrease as κ increases beyond 2600 and as |σ| decreases (for κB̃_l², the
derivative of κ/(aκ + b)² in κ is (b − aκ)/(aκ + b)³ < 0, with a = 15/256, b = (15/256)(3/4) − σ² < aκ and
aκ + b > 0).

For 1 ≤ l ≤ 49 we take B̃_l = B*_l, which increases with |σ|, so that the values at |σ| = 3 bound 0 < |σ| ≤ 3:
(X_l² + κ(B*_l)²)^(1/2) is at most 179.26, 121.33, 96.78, 83.97 and 76.86 for l = 1, …, 5 (with the table's entries),
and for 6 ≤ l ≤ 49, with B*_l ≤ 11.351, X_l ≤ 35.479 and κ ≤ 2499, at most (35.479² + 2499 · 11.351²)^(1/2) < 568.55. ∎

**Remark {#rem:rb-multiplier-observed}** (Numerical observation.) Multipliers tanh((r_* − x_p)/s) centred at the peak
x_p of V_l, checked to give a nonnegative weight on a grid, give w ≥ 0 for 1 ≤ l ≤ 30 at s = 0.98 and for no s in
[0.2, 0.98] at l = 0; at σ = 3 the bounds they give are about 253, 53.3, 35.5, 26.6, 21.35, 19.5, 19.3, 19.2 and 19.2
at l = 1, 2, 3, 4, 5, 6, 10, 17 and 25, each above the bound B*_l(3) proved in [[prop:morawetz-harmonics]] (92.09,
38.04, 22.10, 15.15, 11.51, and 11.36 for every l ≥ 6), while the cut-off norms computed from numerical solutions of the
radial equation are 0.423, 0.451, 0.508, 0.672, 1.132, 0.983, 0.421, 0.0551 and 0.0225. Off the axis, at l = 1,
Re σ = 3 and Im σ = 0.25, 0.5, 1 and 2, the cut-off norm computed by finite differences is 0.297, 0.224, 0.145 and
0.081, below 1/|Im σ²|; at l = 0 it is 0.183, 0.594 and 0.224 at σ = 1 + 2i, 0.5 + i and 2 + i. Multipliers whose width
grows from 49/50 toward the horizon to 2 outside, optimised on a grid, give at σ = 3 about 95.6 for the cut-off
resolvent at l = 1 and about 117.3 for the constant of ‖u′‖_I at l = 0, above the bounds 92.09 and 23.36 that
[[prop:morawetz-harmonics]] and [[cor:morawetz-one-derivative]] (b) prove. No proof uses these values.

### From the radial problem to the spacetime operators {#sec:rb-transfer}

At b_0 we take the 1-forms c_Υ, c_(Υ,H) and c_C that enter L_(b_0) to be combinations of dt and dr with coefficients
depending on r alone. This is a choice: [[def:iii-b-6-1]] fixes c_Υ and c_C only for large r, as r⁻¹dt and
r⁻¹(dt − v_C dr), and c_(Υ,H) only through its support; the choices c_(Υ,H) = −½χ(r)dr of [[sec:iii-d1-1]] and c_C of
[[sec:iv4-0]], built from [[eq:s14-cform]], are of this form.

**Lemma {#lem:rb-scalar}** (The scalar spectral family.) Let □ = δd = −∇^μ∇_μ act on functions on g_(b_0) (the
operator □_0 of [[ch:s13]]), and let □̂(σ) := e^(iσt_*)□e^(−iσt_*) be its spectral family, acting on stationary
functions, sections of the trivial bundle of rank one. For σ ≠ 0 with Im σ ≥ 0, □̂(σ) : 𝒳_σ → 𝒴_σ is invertible, with
𝒳_σ and 𝒴_σ the spaces of [[thm:i-a-7-2]] with the orders of [[thm:i-b-1-3]] (3).

*Proof.* *The hypotheses.* □ is t_*-translation invariant with principal symbol G := g_(b_0)⁻¹(ζ, ζ). By
[[lem:ii-c-1-3]] at (p, q) = (0, 0), whose proof uses of the metric only (K1), □ is a stationary wave-type operator with
S = 0; so by [[lem:ii-c-1-2]] its spectral family satisfies (H1), (H2) with S = 0, hence S̄ = 0, and the operator part
of (H6). By [[thm:vi-a-6-1]], (K1), the metric part of (H6), the dynamical parts of (H3), all of (H4), (Γ.1)–(Γ.3) with
ν_min = 4(2m_0)^(−1/2), the values q^Γ = 4 and β_0 = 2 on Γ, and (H8) hold, for every operator with principal symbol
G Id; (H5) is void for a single operator. The remaining conditions concern Im □̂, taken for the density |dx| of
[[sec:i-a-1-1]] and the standard inner product of ℂ. In coordinates □u = −|g|^(−1/2)∂_μ(|g|^(1/2)g^(μν)∂_νu) has
real coefficients, and two integrations by parts give ∫(□u)v̄|dg| = ∫g^(μν)∂_νu ∂_μv̄|dg| = ∫u conj(□v)|dg| for
smooth compactly supported u, v. Moreover |dg| = |dt_*||dx| on X̃°. The Kerr–Schild chart of [[prop:iii-b-3-4]] covers
X̃° ([[lem:s11-ks-domain]]; r_0 − 2δ_0 ≥ ½r_♭ by [[sec:s12-radii]]). Let t_KS be its time, so that g_(b_0) is
g^KS_(m_0,0) in the coordinates (t_KS, x) ([[eq:iii-b-3-3]]), r = |x|, and z = (z¹, z², z³) coordinates on 𝕊³.
Expanding η + m_0r⁻²(dt_KS + dr)² with η = −dt_KS² + dr² + r²g̸ gives
g_(b_0) = −f dt_KS² + 2(1 − f) dt_KS dr + (2 − f) dr² + r²g̸ with f = 1 − m_0r⁻², the form used in the proof of
[[lem:rb-m33]]. Its (t_KS, r) block has determinant −f(2 − f) − (1 − f)² = −1, and no term couples dt_KS or dr to dz;
so in the coordinates (t_KS, r, z), |det g| = r⁶ det g̸ and |dg| = r³(det g̸)^(1/2)|dt_KS dr dz|. The Euclidean metric
is dr² + r²g̸ in (r, z), so |dx| = r³(det g̸)^(1/2)|dr dz| = r³dr dω. Finally t_* − t_KS is a function of r
([[eq:iii-b-3-3]], [[eq:iii-b-3-6]]), so the change of coordinates (t_KS, r, z) ↦ (t_*, r, z) has a triangular Jacobian
matrix with determinant 1, and |dg| = r³(det g̸)^(1/2)|dt_* dr dz| = |dt_*||dx|. Writing
□ = A_0 + A_1∂_(t_*) + A_2∂²_(t_*) with stationary A_k, the symmetry gives A_k* = (−1)^kA_k for |dx|, so
□̂(σ) = A_0 − iσA_1 − σ²A_2 satisfies □̂(σ)* = □̂(σ̄). Hence
Im □̂(0) = 0 and Im T = 0 for T = −iA_1; the threshold quantities of [[eq:i-a-1-5]] are ϑ_ℋ = 0 and ϑ_in = 0, as S = 0;
and the endomorphism p_1 of (Γ.4) vanishes ([[lem:i-b-1-1]] (b), with the standard inner product as h_Γ), so that the
function of (Γ.4) is −q^Γ times its argument, which decreases at the rate q^Γ = 2β_0, with γ_+ = 0 and
γ_− = −ν_min/(2q^Γ) < 0.

*Fredholm of index 0.* So [[thm:i-a-7-2]] (3) and [[thm:i-b-1-3]] (3) apply: □̂(σ) : 𝒳_σ → 𝒴_σ is Fredholm with an index
that does not depend on σ ∈ {σ ≠ 0, Im σ ≥ 0}, and it is invertible for |σ| ≥ C_0; so the index is 0.

*Injectivity.* Let u ∈ 𝒳_σ with □̂(σ)u = 0. By [[thm:i-a-7-2]] (5) with S̄ = 0, u ∈ 𝒜^(3/2−ε)(X̄) for every ε > 0.
Put ω := e^(iσt_*)d(e^(−iσt_*)u) = du − iσu dt_*, a stationary 1-form. In the frame dt_*, dx¹, …, dx⁴ its components
are −iσu and ∂_(x^i)u, and ∂_(x^i) ∈ ρ𝒱_b maps 𝒜^q into 𝒜^(q+1); so ω ∈ ⋂_(ε>0)𝒜^(3/2−ε), which lies in the space
𝒳_σ of the 1-form operator □ of [[prop:iii-d-6-2]] by [[thm:i-a-7-2]] (5), its S̄ being 0 ([[lem:ii-c-1-3]] at
(p, q) = (0, 1), as □ = ∇*∇ there). On 1-forms □ = dδ + δd ([[prop:np-10-16]] (i)), so □d = dδd = d□ on functions,
and □(e^(−iσt_*)ω) = □d(e^(−iσt_*)u) = d□(e^(−iσt_*)u) = d(e^(−iσt_*)□̂(σ)u) = 0. So ω is in the kernel of the
spectral family of [[prop:iii-d-6-2]], and ω = 0. Its dt_*-component −iσu vanishes, and u = 0 as σ ≠ 0. ∎

**Lemma {#lem:rb-schur}** (Blocks.) Let ℌ_1 and ℌ_2 be Hilbert spaces on which SO(4) acts unitarily, let 𝒟 ⊂ ℌ_1 be a
dense subspace that SO(4) and the isotypic projections E_π of ℌ_1 (π running over the irreducible representations of
SO(4)) map into itself, and let A : 𝒟 → ℌ_2 be linear with A(gF) = gAF and AE_πF = E_πAF for g ∈ SO(4) and F ∈ 𝒟. If
C_π bounds ‖AF‖/‖F‖ over the nonzero F ∈ 𝒟 in the component π, then ‖AF‖ ≤ (sup_π C_π)‖F‖ for every F ∈ 𝒟, and the
least bound is sup_π C_π when each C_π is the least such bound. This applies:

(a) to A := χ_I P̂(σ)⁻¹ χ_I on ℌ_1 = ℌ_2 = 𝔏 := L²(I × 𝕊³, r³dr dω), with the pointwise norm of the static frame
(dt, dr, r dω) (for m_0 = 1, I = {6/5 ≤ r ≤ 4}), and 𝒟 the smooth fields supported in I × 𝕊³, where P̂(σ), σ ≠ 0 and
Im σ ≥ 0, is the spectral family at b_0 of □ on functions, of □ on 1-forms or of 2L_(b_0); so
C_D(σ) := ‖χ_I P̂(σ)⁻¹ χ_I‖_(𝔏→𝔏) ≤ sup_π C_π, with C_π the bound over the smooth F supported in I × 𝕊³ in the
component π;

(b) to the inverse of any of these operators, at σ ≠ 0 or at zero energy, between any two Hilbert norms invariant under
SO(4) in which it is bounded, with 𝒟 = ℌ_1.

For functions the components are the degrees l; for 1-forms and symmetric 2-tensors each component consists of fields of
one type ([[def:iii-a1-1-3]]) and one degree.

*Proof.* By the Peter–Weyl theorem, in ℌ_1 and in ℌ_2 the operators E_π := d_π∫_(SO(4)) conj(χ_π(g)) g dg, with d_π
the dimension and χ_π the character of π and dg the Haar probability measure, are mutually orthogonal orthogonal
projections with Σ_π E_π = I strongly. For F ∈ 𝒟, E_πF ∈ 𝒟 lies in the component π, so
‖AF‖² = Σ_π ‖E_πAF‖² = Σ_π ‖AE_πF‖² ≤ sup_π C_π² Σ_π ‖E_πF‖² = sup_π C_π² ‖F‖². If each C_π is least, the norm of A
on 𝒟 is at least every C_π. (a) SO(4) acts by isometries of g_(b_0), on sections of the tensor bundles; it preserves
the density and the static frame up to rotation of its angular part, so it acts unitarily on 𝔏, and it maps 𝒟 into
itself. P̂(σ) is built from g_(b_0) and, for 2L_(b_0), from the 1-forms fixed above, which SO(4) preserves; so it
commutes with SO(4), and so do P̂(σ)⁻¹ and χ_I. For F ∈ 𝒟, g ↦ gF is continuous into the smooth fields supported in
I × 𝕊³, so the integral defining E_πF converges there, E_πF ∈ 𝒟, and the integral converges in 𝒴_σ, into which these
fields embed continuously; χ_IP̂(σ)⁻¹ is continuous from 𝒴_σ into 𝔏 (𝒳_σ has positive regularity), so
AE_πF = d_π∫conj(χ_π(g)) A(gF) dg = d_π∫conj(χ_π(g)) gAF dg = E_πAF. (b) There A is bounded on ℌ_1 and commutes with
SO(4), hence with every E_π. Scalar harmonics of degree l carry the representation (l/2, l/2) of
SO(4) = (SU(2) × SU(2))/{±1}, vector-type fields of degree l the sum of ((l + 1)/2, (l − 1)/2) and
((l − 1)/2, (l + 1)/2), and tensor-type fields the sum of ((l + 2)/2, (l − 2)/2) and ((l − 2)/2, (l + 2)/2). These are
distinct for distinct pairs (type, degree), so each isotypic component lies within one type and one degree. ∎

The function spaces 𝒳_σ, 𝒴_σ of the stability theory are invariant under SO(4) only up to equivalence: averaging over
SO(4) gives invariant norms, equivalent to the given ones with constant sup_g ‖g‖_(𝒳_σ→𝒳_σ) ‖g‖_(𝒴_σ→𝒴_σ), a
constant of the calculus. [[lem:rb-schur]] (b) applies in these averaged norms.

**Lemma {#lem:rb-tensor-ricci}** (The linearised Ricci tensor on tensor type.) On {r > r_h} write
g_(b_0) = g_ab dx^a dx^b + r²γ with x^a = (t, r), the orbit metric g_ab dx^a dx^b = −f dt² + f⁻¹dr² and D, □_2 as in
[[thm:s15-ki]], and let z^i be coordinates on 𝕊³. Let T = T_ij dz^i dz^j ∈ 𝒯_l, l ≥ 2, be trace-free and
divergence-free with (Δ̂ + k_T²)T = 0, k_T² = κ − 2, as in [[thm:s15-ki]] (T), and let H be a smooth function of
(t, r). Then h := 2r²H T_ij dz^i dz^j has tr h = 0 and δh = 0, its components D Ric(h)_ab and D Ric(h)_ai vanish, and

    D Ric(h)_ij = −r²ℬ[H]T_ij,     ℬ[H] := □_2H + (3/r)Dr · DH − ((k_T² + 2)/r²)H.                {#eq:rb-tensor-ricci}

For H = e^(−iσt)H_0(r), ℬ[H] = e^(−iσt)(σ²H_0/f + r⁻³(r³fH_0′)′ − κr⁻²H_0), and with H_0 = r^(−3/2)u,
fr^(3/2)e^(iσt)ℬ[H] = u″ + σ²u − V_lu, u″ := d²u/dr_*²; in particular V_T of [[thm:s15-ki]] (T) equals V_l.

*Proof.* Write r_a := D_ar, r^a := g^(ab)r_b and K := 2H, so h_ij = r²KT_ij and h_ab = h_ai = 0; indices of T are
raised by γ, and D̂ is the covariant derivative of γ. The Christoffel symbols of g_(b_0) are those of the orbit metric,
Γ^a_ij = −rr^aγ_ij, Γ^i_aj = (r_a/r)δ^i_j and the Γ̂^i_jk of γ, all others vanishing (the list before [[lem:s15-low]]).

*Trace and divergence.* tr h = r⁻²γ^(ij)h_ij = 2H T^i_i = 0. In (δh)_a = −g^(μν)∇_μh_νa only the term
g^(ij)Γ^k_(ia)h_jk = (r_a/r) tr h = 0 survives, and (δh)_i = −g^(jk)∇_jh_ki = −r⁻²γ^(jk)D̂_j(r²KT_ki) = −KD̂^kT_ki = 0,
as ∇_ah_bi = −Γ^k_ai h_bk = 0 and the terms of ∇_jh_ki with an orbit index on Γ multiply h_ai = 0.

*The variation of the connection.* For every metric, D Ric(h)_μν = ∇_αδΓ^α_μν − ∇_νδΓ^α_αμ, with
δΓ^α_μν := ½g^(αβ)(∂_μh_νβ + ∂_νh_μβ − ∂_βh_μν) − h^α_λΓ^λ_μν the first variation of Γ^α_μν (as δg^(αβ) = −h^(αβ))
and δΓ^α_αμ = ½∂_μ tr h: in normal coordinates at a point, where Γ = 0, these are the variations of
Ric_μν = ∂_αΓ^α_μν − ∂_νΓ^α_αμ + (terms quadratic in Γ) and of Γ^α_αμ = ½∂_μ log|det g|, and δΓ is a tensor. Here
δΓ^α_αμ = 0, and with C^k_ij := γ^(kl)(D̂_iT_jl + D̂_jT_il − D̂_lT_ij) the components of Q := δΓ that do not vanish are

    Q^a_ij = −½D^a(r²K)T_ij,     Q^k_ai = Q^k_ia = ½(D_aK)T^k_i,     Q^k_ij = ½KC^k_ij;

for instance Q^k_ai = ½r⁻²D_a(r²K)T^k_i − KT^k_l(r_a/r)δ^l_i = ½(D_aK)T^k_i, and Q^k_ij is ½K times the first
variation of Γ̂ in the direction T, which is tensorial on 𝕊³. Also C^k_ki = D̂_iT^k_k = 0.

*The divergence.* D Ric(h)_μν = ∂_αQ^α_μν + Γ^α_αβQ^β_μν − Γ^β_αμQ^α_βν − Γ^β_ανQ^α_μβ, with
Γ^α_αb = Γ^c_cb + 3r_b/r and Γ^α_αj = Γ̂^k_kj. At (b, c) every term vanishes: Q^α_bc = 0, and the only products are
Γ^i_kbQ^k_ic = (r_b/r)Q^k_kc = ½(r_b/r)(D_cK)T^k_k = 0. At (b, i) the terms give
½(D_bK)(∂_kT^k_i + Γ̂^l_lkT^k_i − Γ̂^j_kiT^k_j) − Γ^j_kbQ^k_ji = ½(D_bK)D̂_kT^k_i − ½(r_b/r)KC^k_ki = 0. At (i, j):
∂_aQ^a_ij + Γ^α_αaQ^a_ij = −½(□_2(r²K) + (3/r)r^aD_a(r²K))T_ij; the two terms −Γ^k_aiQ^a_kj and −Γ^k_ajQ^a_ik give
(1/r)r^aD_a(r²K)T_ij; the two terms −Γ^c_kiQ^k_cj and −Γ^c_kjQ^k_ic give rr^cD_cK T_ij; and the terms with angular
indices only give ½KD̂_kC^k_ij. With □_2(r²K) = r²□_2K + 4rr^aD_aK + 2K(r□_2r + r^ar_a) and
r^aD_a(r²K) = r²r^aD_aK + 2rr^ar_aK,

    D Ric(h)_ij = −½r²(□_2K + (3/r)r^aD_aK)T_ij − K(r□_2r + 2r^ar_a)T_ij + ½KD̂_kC^k_ij.

On the unit 𝕊³ (sectional curvature 1, Ricci tensor 2γ) the Ricci identity gives D̂^lD̂_iT_jl = D̂_iD̂^lT_jl + 3T_ij =
3T_ij, T being trace-free and divergence-free; so D̂_kC^k_ij = 6T_ij − Δ̂T_ij = (6 + k_T²)T_ij. On the orbit metric,
whose determinant is −1, r^ar_a = f and □_2r = f′ = 2m_0/r³, so r□_2r + 2r^ar_a = 2. Hence
D Ric(h)_ij = −½r²(□_2K + (3/r)Dr · DK − ((k_T² + 2)/r²)K)T_ij, which at K = 2H is [[eq:rb-tensor-ricci]].

*The radial form.* For H = e^(−iσt)H_0, □_2 = −f⁻¹∂_t² + ∂_rf∂_r and Dr · DH = f∂_rH give the formula for ℬ[H], and
k_T² + 2 = κ. In the proof of [[prop:np-10-16]] (ii), e^(iσt)δd(H_0Se^(−iσt))/S = −σ²f⁻¹H_0 − r⁻³(r³fH_0′)′ + κr⁻²H_0,
which is −e^(iσt)ℬ[H]; so [[prop:np-10-16]] (ii) ([[eq:rb-potential]]) gives fr^(3/2)e^(iσt)ℬ[H] = u″ + σ²u − V_lu.
Finally V_T = (f/r²)(k_T² + 2 + 3/4 + 9m_0/(4r²)) = V_l. ∎

**Lemma {#lem:rb-transfer}** (The exact transfers.) Let m_0 = 1 and σ real and nonzero. Let B(σ) bound the cut-off
outgoing resolvent ‖χ_I R(σ) χ_I‖ on L²(ℝ, dr_*) of the master operator −∂²_(r_*) + V − σ² named below, for the degree
l in question. Then, on fields of the block named,

    ‖χ_I P̂(σ)⁻¹ χ_I‖_(𝔏→𝔏) ≤ (15/16) B(σ)

in each of the following cases: P̂ = □ on functions of degree l, V = V_l; P̂ = □ on 1-forms of vector type l, V = V^v
(the potential V_1 of [[prop:np-10-16]] (iii)); P̂ = 2L_(b_0) on symmetric 2-tensors of tensor type l ≥ 2, V = V_T of
[[thm:s15-ki]] (T), which equals V_l ([[lem:rb-tensor-ricci]]).

*Proof.* P̂(σ) is invertible on the spaces of the stability theory ([[lem:rb-scalar]] for □ on functions,
[[prop:iii-d-6-2]] for □ on 1-forms, [[prop:iii-f2-3-1]] for 2L_(b_0)). Let F be smooth, supported in I × 𝕊³ and in
the block, and ω := P̂(σ)⁻¹F. Then ω lies in the block, as P̂(σ)⁻¹ commutes with the isotypic projections (proof of
[[lem:rb-schur]]). The kernel of P̂(σ) and the annihilator of its range do not depend on the admissible orders
([[thm:i-a-7-2]] (3)), so P̂(σ) is invertible at every admissible order (a Fredholm operator with trivial kernel and
trivial annihilator of its closed range is invertible), and the inverse at a larger regularity is the restriction of the
inverse at a smaller one: the spaces at the larger orders lie in those at the smaller, and the solution is unique in the
latter. F lies in 𝒴_σ at every order, so ω lies in 𝒳_σ for orders of every regularity, and is smooth on X°; and it is
conormal at infinity, with polynomial bounds, by [[thm:i-a-7-2]] (4). Since t_* − t is a function of r
([[eq:iii-b-3-6]]) and σ is real, e^(−iσt_*)ω = e^(−iσt)ω̃ and e^(−iσt_*)F = e^(−iσt)F̃ with ω̃ := e^(−iσ(t_*−t))ω and
F̃ := e^(−iσ(t_*−t))F, which have the pointwise norms of ω and F; in the static chart on {r > r_h} the equation is
P(e^(−iσt)ω̃) = e^(−iσt)F̃, P the stationary operator. Let (Y_k) be an orthonormal basis in L²(𝕊³) of the angular
fields of the block (of 𝒮_l, 𝒱_l or 𝒯_l), and ω_k, F_k the components of ω̃, F̃ along Y_k; for each r these
components are orthogonal on 𝕊³, so by Parseval's identity ‖χ_Iω‖²_𝔏 = Σ_k‖χ_Iω_k‖²_𝔏 and
‖F‖²_𝔏 = Σ_k‖F_k‖²_𝔏, as in [[cor:morawetz-one-derivative]] (c). Each ω_k solves the equation with right side F_k, and
we bound it. Recall dr = f dr_*.

- *Functions.* ω_k = r^(−3/2)uS and F_k = gS, S = Y_k. By [[eq:rb-radial]], −u″ + (V_l − σ²)u = G with G := fr^(3/2)g.
  Then |ω_k|²r³dr = f|u|²|S|²dr_* and |G|² dr_* = fr³|g|² dr, so ‖χ_Iω_k‖²_𝔏 ≤ (max_I f)‖u‖²_I and
  ‖G‖² ≤ (max_I f)‖F_k‖²_𝔏.
- *Vector type.* ω_k = r^(−1/2)uY with Y = Y_k ∈ 𝒱_l, δω_k = 0 and □ω_k = δdω_k. By [[prop:np-10-16]] (iii) the t- and
  r-components of δdω_k vanish and its angular part is gY with −fr^(1/2)g = u″ + σ²u − V^vu, so
  −u″ + (V^v − σ²)u = G := fr^(1/2)g. In the static frame |ω_k|² = r⁻³|u|²|Y|² and |F_k|² = r⁻²|g|²|Y|², so
  |ω_k|²r³dr = f|u|²|Y|²dr_*, while the integral of |F_k|²r³dr over 𝕊³ is r|g|²dr and |G|²dr_* = fr|g|²dr; the two
  inequalities of the first case follow verbatim.
- *Tensor type.* ω_k = 2r²HT with T = Y_k ∈ 𝒯_l. By [[lem:rb-tensor-ricci]], tr ω_k = 0 and δω_k = 0, and
  ι_(g⁻¹c)ω_k = 0 for every c in the span of dt and dr; so the gauge terms of L_(b_0) vanish on ω_k, and
  L_(b_0)ω_k = D Ric(ω_k) = −r²ℬ[H]T with all other components zero, by [[eq:rb-tensor-ricci]]. With u := r^(3/2)H, on
  the factor e^(−iσt), fr^(3/2)ℬ = u″ + σ²u − V_Tu with V_T = V_l, so F_k = 2L_(b_0)ω_k = −2r²ℬT and
  −u″ + (V_T − σ²)u = G := −fr^(3/2)ℬ. In the static frame |ω_k|² = 4|H|²|T|² and |F_k|² = 4|ℬ|²|T|², so
  |ω_k|²r³dr = 4f|u|²|T|²dr_* and |F_k|²r³dr = 4fr³|ℬ|²|T|²dr_*, while |G|² = f²r³|ℬ|²; so
  ‖χ_Iω_k‖²_𝔏 ≤ 4(max_I f)‖u‖²_I and ‖G‖² ≤ (max_I f)‖F_k‖²_𝔏/4.

In each case G vanishes off I, and u = R(σ)G. Indeed, by *The class* in the proof of [[prop:iii-d-6-2]], which uses of
ω only that it is smooth across the future horizon and conormal at infinity, u = e^(−iσr_*)a near r_* = −∞ with a
smooth across r_h, and u = e^(iσr_*)b near r_* = ∞ with b conormal and polynomially bounded. Near −∞,
u′ + iσu = e^(−iσr_*)f ∂_ra → 0, so u is a multiple of u_h left of I (*Solutions at the ends* in [[sec:rb-radial]]).
Near +∞, as in the fact stated in the proof of [[prop:iii-d-6-2]], the second solution e^(−iσr_*)(1 + o(1)) is not of
the form e^(iσr_*)b with b conormal, e^(−2iσr_*) not being conormal, so u is a multiple of u_∞ right of I. So
u = R(σ)G by the uniqueness in [[prop:resolvent-outgoing]] (a), which holds verbatim for V (the paragraph before
[[lem:morawetz-identity]]). Hence ‖χ_Iω_k‖_𝔏 ≤ (c′ max_I f)^(1/2)‖u‖_I ≤ (c′ max_I f)^(1/2)B(σ)‖G‖ ≤
(max_I f)B(σ)‖F_k‖_𝔏, with c′ = 1, resp. 4. Summing over k gives the bound for ω. f increases, so
max_I f = f(4) = 15/16. ∎

By [[lem:rb-schur]], the bounds of [[lem:rb-transfer]], taken uniformly in l, bound the cut-off inverse on all fields of
the type.

### The master operators {#sec:morawetz-master}

For rows T1 and T3 below the weight is W = ηΠ/D with Π a polynomial and D = 1 (T1) or D = 4(1 + 2y)⁴(5 + 6y)³ (T3),
positive and increasing in y. A lower bound on a piece r ∈ [r_2, r_1] (y ∈ [1/r_1², 1/r_2²]) is the product of η at
the end where it is least and of the least Bernstein coefficient of Π on the piece divided by the value of D at its
right end in y; this is a lower bound because that least coefficient is positive on every piece below. Each piece is
written "r_1–r_2: e · g ≥ v" with e and g such lower bounds; the Bernstein coefficients are listed in
[[sec:tb-morawetz-t1t3]].

**Proposition {#prop:morawetz-master-potentials}** (Every master operator at every harmonic.) For the operator
−∂²_(r_*) + V − σ² of each of the following rows, every real σ ≠ 0 and every harmonic of the row,
‖χ_I R(σ) χ_I‖ ≤ B(σ), the bound [[eq:pb-bound]] with the row's constants, whose values at σ → 0, σ = 1, 3 and 10 are:

| row | operators and harmonics | multiplier | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|
| A | V^□, V^v, every l ≥ 1 | Θ_A | 22.66 | 42.87 | 95.54 | 288.77 |
| B | V^□, V^v, V^s, V_T, every l ≥ 2 | Θ_B | 12.85 | 19.51 | 40.27 | 120.24 |
| C | V^□, V^v, V^s, V_T, V_V, every l ≥ 3 | Θ_C | 13.11 | 15.25 | 23.64 | 62.09 |
| S4 | V_S, every l ≥ 4 | Θ_C | 10.36 | 11.47 | 16.17 | 39.67 |
| S3 | V_S, l = 3 | Θ_C | 13.62 | 15.99 | 25.17 | 66.71 |
| T1 | V^s, l = 1 | z, q = (5/3)ηy | 29.22 | 59.91 | 143.71 | 449.56 |
| T2 | V_V, l = 2 | Θ_T, q = ηy/2 | 12.96 | 20.98 | 45.44 | 138.20 |
| T3 | V_S, l = 2 | (1 − 4y)/(1 + 2y), q = ½ηy(1 + y) | 23.15 | 64.82 | 160.01 | 498.25 |

Rows A, B, C, S4, S3 and T2 are those of [[prop:morawetz-polynomial]]. In rows T1 and T3, p_I = p_∞ = 1, w_I ≥ 0.0455
and 0.0413, and (m′, M′) = (935/16384, 0.4157) and (0.1384, 0.563). The largest values over all rows are 29.22, 64.82,
160.01 and 498.25. With V^□ at l = 0 ([[prop:morawetz-harmonics]] (ii)), the largest values over every master operator
and every harmonic are 70.17, 64.82, 160.01 and 498.25. Multiplied by 15/16, the transfer of [[lem:rb-transfer]],
rows A and B bound the vector-type 1-form blocks at l = 1 (21.25, 40.20, 89.57, 270.73) and at l ≥ 2 (12.05, 18.30,
37.76, 112.73), and row B the tensor-type blocks, every l ≥ 2 (the same). Every potential of the rows is real, bounded
and nonnegative, so off the real axis [[lem:morawetz-complex]] applies in its scaled form, with p_φ := sup_ℝ|φ|:
p_φ = 1 in rows T1 and T3, and p_φ = p_∞ in the others, whose multipliers increase from Θ(−1) to Θ(1). There max q is 0
in rows A to S3 and less than 0.20534, 0.06161 and 0.10659 in rows T1, T2 and T3.

*Proof.* Rows A, B, C, S4, S3 and T2: V^□ = V_(κ+3/4,9/4) and V^v = V_(κ+3/4,5/4), and at l ≥ 1, κ + 3/4 ≥ 15/4, which
is row A of [[prop:morawetz-polynomial]]. At l ≥ 2, κ + 3/4 ≥ 35/4 and V^s = V_(κ+3/4,−7/4), V_T = V^□ lie in its row B.
At l ≥ 3, κ + 3/4 ≥ 63/4 and b ∈ {9/4, 5/4, −7/4, −27/4} ⊂ [−27/4, 9/4], so V^□, V^v, V^s, V_T and V_V lie in its
row C. V_S at l = 3 and at l ≥ 4 are its rows S3 and S4, and V_V at l = 2 its row T2. The values are those of
[[prop:morawetz-polynomial]].

Row T1 (a = 15/4, b = −7/4). Here a + b = 2 < 4, so P_(a,b)(−1) = 2(a + b − 4) < 0: with q = 0 the weight of
[[prop:morawetz-weight]] is negative near the horizon, and the term q is needed there. g = (5/3)y gives
Π = 15/2 − 61y + 188y² − (728/3)y³ + (665/6)y⁴; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 1]: at least 0.641,
0.292, 0.193, 0.101. Pieces: 4–16/5: 0.01464 · 3.119 ≥ 0.0456; 16/5–13/5: 0.02753 · 1.857 ≥ 0.0511; 13/5–11/5:
0.04847 · 0.9837 ≥ 0.0476; 11/5–2: 0.07451 · 0.6412 ≥ 0.0477; 2–19/10: 0.09375 · 0.5229 ≥ 0.049; 19/10–17/10:
0.1054 · 0.432 ≥ 0.0455; 17/10–13/10: 0.1331 · 0.4373 ≥ 0.0582; 13/10–6/5: 0.1768 · 0.3101 ≥ 0.0548. Also
φ′ − q = η(12 − 5y)/3 > 0; d log(η(12 − 5y))/dy ≥ 3 − 2 − 5/9.5 > 0 on [1/16, 1/2] and η(12 − 5y)/3 > 0.5 on
[1/2, 25/36], so m′ = (15/1024)(187/48) = 935/16384; φ′ − 2q = (2/3)η(6 − 5y) has its maximum on (0, 1) at the root
y = (55 − √505)/70 of 35y² − 55y + 18, where it is less than 0.4157. q = (5/3)(1 − y)y^(5/2) has its maximum at y = 5/7,
(10/21)(5/7)^(5/2) < 0.20534.

Row T3 (V_S at l = 2, p = 5, H = 5 + 6y). Here Θ = (1 − 4y)/(1 + 2y) decreases from 1 to −1 on [0, 1], so |φ| ≤ 1,
φ → ±1 at ±∞, and φ′ = 12η/(1 + 2y)² > 0. With g = ½y(1 + y), [[eq:pb-weight-general]] gives G = Π/D with
D = 4(1 + 2y)⁴(5 + 6y)³ and

    Π = 8750 − 52800y − 52305y² + 661453y³ + 1153253y⁴ − 668761y⁵ − 2258994y⁶ − 1768052y⁷ − 1623176y⁸
        + 831312y⁹ + 3571104y¹⁰ + 2896704y¹¹ + 777600y¹²;

Bernstein on [0, 1/2], [1/2, 3/4], [3/4, 1]: at least 228, 27800, 34900. Pieces: 4–33/10: 0.01464 · 3.014 ≥ 0.0441;
33/10–29/10: 0.02527 · 1.742 ≥ 0.044; 29/10–27/10: 0.03612 · 1.243 ≥ 0.0448; 27/10–13/5: 0.04383 · 1.048 ≥ 0.0459;
13/5–5/2: 0.04847 · 0.9003 ≥ 0.0436; 5/2–12/5: 0.05376 · 0.793 ≥ 0.0426; 12/5–23/10: 0.05977 · 0.7024 ≥ 0.0419;
23/10–11/5: 0.06665 · 0.6601 ≥ 0.0439; 11/5–2: 0.07451 · 0.5544 ≥ 0.0413; 2–17/10: 0.09375 · 0.4985 ≥ 0.0467;
17/10–13/10: 0.1331 · 0.3475 ≥ 0.0462; 13/10–6/5: 0.1768 · 0.3621 ≥ 0.064. Also
φ′ − q = η(24 − y − 5y² − 8y³ − 4y⁴)/(2(1 + 2y)²) > 0; its logarithmic derivative is positive on [1/16, 1/4] (at least
6 − 4/3 − 0.23 − 3.56) and it exceeds 0.14 on [1/4, 25/36], so m′ is its value at y = 1/16, more than 0.1384. On I,
0 < φ′ − 2q = η(12 − y − 5y² − 8y³ − 4y⁴)/(1 + 2y)² ≤ 12η/(1 + 2y)²: the quartic decreases on [0, 1] and is more than
5.28 at y = 25/36. The maximum of 12η/(1 + 2y)² on (0, 1) is at the root y = (√73 − 7)/4 of 2y² + 7y − 3, where it is
less than 0.563. q = ½(1 − y²)y^(5/2) has its maximum at y = √5/3, (2/9)(5/9)^(5/4) < 0.10659.

In rows T1 and T3, q ≥ 0 and φ′ − q > 0 on ℝ, and [[eq:pb-bound]] with p_I = p_∞ = 1 gives the values listed. The
transfers are 15/16 times the values of rows A and B, rounded up.

Off the real axis. Every V_(a,b) of the rows has a > 0 and a + b ≥ 2, so V_(a,b) = (1 − y)y(a + by) with
a + by ≥ min(a, a + b) > 0 on [0, 1]. V_S = (1 − y)yQ_S/(16H²) with
Q_S = 1296y³ + (624p − 144)y² + 36p(p − 12)y + 16p³ + 60p², whose coefficients are nonnegative for p ≥ 12 (l ≥ 3), and
which is 1296y³ + 2976y² − 1260y + 3500 ≥ 3500 − 1260y > 0 on [0, 1] for p = 5 (l = 2). So every potential of the rows is
nonnegative, and it is bounded, with V and V′ integrable and tending to 0 at ±∞ ([[sec:morawetz-identity]]). The
multipliers of rows A, B, C, S4, S3 and T2 increase, so sup_ℝ|φ| = max(Θ(1), −Θ(−1)) = p_∞
([[sec:tb-morawetz-monotone]]); in rows T1 and T3, |φ| ≤ 1. Since the sign conditions of [[lem:morawetz-identity]]
hold on ℝ in every row, [[lem:morawetz-complex]] applies, in its scaled form with p_φ := sup_ℝ|φ|. The values of max q:
in rows A to S3, q = 0; in row T2 it is that of Θ_T in [[prop:morawetz-polynomial]]; in rows T1 and T3 they are computed
above. ∎

### Large frequencies with a fixed multiplier {#sec:morawetz-large-frequency}

**Proposition {#prop:morawetz-large-frequency}** (Every harmonic at a given frequency.) Let B_(C5) and B_(C6) be the
bounds of rows C5 and C6 of [[prop:morawetz-polynomial]]. For every real σ with |σ| ≥ 3 and every l ≥ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 6.521), B_(C5)(σ)),

and for |σ| ≥ 6 also ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 9.271), B_(C6)(σ)). In particular, for every l ≥ 0, the norm is
at most 11.51, 16.98, 30.01, 57.44, 113.10 and 224.86 at |σ| = 3, 6, 12, 24, 48 and 96.

*Proof.* As in the proof of [[prop:morawetz-harmonics]] (ii), max V_(κ+3/4,9/4) ≤ (κ + 3/4)/4 + 1/3: at most 6.521 for
l ≤ 4 and 9.271 for l ≤ 5. When σ² exceeds it, the bound above the barrier, [[prop:resolvent-above-barrier]], gives
‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V). So for |σ| ≥ 3 the harmonics l ≤ 4 are bounded by Λ|σ|/(σ² − 6.521), and
for |σ| ≥ 6 the harmonics l ≤ 5 by Λ|σ|/(σ² − 9.271); the others are bounded by B_(C5)(σ), respectively B_(C6)(σ), as
row C5 serves every l ≥ 5 and row C6 every l ≥ 6. At |σ| = 3 the first term is at most 3.7436 · 3/2.479 < 4.54 and
B_(C5)(3) < 11.51; for |σ| ≥ 6 the first term is at most 3.7436 · 6/26.729 < 0.85, as Λt/(t² − c) decreases for
t² > c, and the values given are B_(C6)(σ), rounded up. ∎

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

    B♯ := (ϱ + (ϱ² + 2p_I²w_I/m′)^(1/2))/(2w_I),     ϱ := (M′² + 4σ²p_∞²)^(1/2).                    {#eq:band-sharp}

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

    2m′X² + w_IY² ≤ Re∫_I F · conj(2φu′ + (φ′ − 2iσp_∞)u) ≤ ‖F‖(2p_IX + ϱY),

because |φ| ≤ p_I on I and |φ′ − 2iσp_∞| = (φ′² + 4σ²p_∞²)^(1/2) ≤ ϱ there. For every real X,
2m′X² − 2p_I‖F‖X ≥ −p_I²‖F‖²/(2m′); hence w_IY² − ϱ‖F‖Y − p_I²‖F‖²/(2m′) ≤ 0, and Y is at most the positive root of
this quadratic, which is B♯‖F‖. Finally B♯ = ϱ/(2w_I) + (ϱ²/(4w_I²) + p_I²/(2m′w_I))^(1/2), which gives the
monotonicity. ∎

Since every hypothesis and the constant depend on σ only through |σ|, every bound below is even in σ.

**Lemma {#lem:band-barrier}** (Harmonics above the barrier.) For every l ≥ 0, max V_l ≤ κ/4 + 25/48. Consequently, if
σ² > κ/4 + 25/48, then ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − κ/4 − 25/48), which decreases as |σ| increases; and if
σ² − κ/4 − 25/48 ≥ |σ|/2, then ‖χ_I R_l(σ) χ_I‖ ≤ 2Λ < 7.4872.

*Proof.* U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27 on [0, 1], so V_l ≤ (κ + 3/4)/4 + (9/4)(4/27) = κ/4 + 25/48. The
bound above the barrier ([[prop:resolvent-above-barrier]]) then gives the first estimate, and
t ↦ Λt/(t² − κ/4 − 25/48) decreases for t² > κ/4 + 25/48, its derivative being
−Λ(t² + κ/4 + 25/48)/(t² − κ/4 − 25/48)². The last statement is the first with
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
[[eq:band-r-expanded]] gives 𝒬 = 𝔢_0 + μ𝔢_1 + μ²𝔢_2 + μ³𝔢_3 + μ⁴𝔢_4 + μ⁵𝔢_5 with

    𝔢_0 = 1/2 + 18x⁴ + 18x⁶ + 6x⁸,            𝔢_1 = −(15/4)x + (17/2)x² + (15/4)x³ + (51/2)(x⁴ + x⁶) + (17/2)x⁸,
    𝔢_2 = 1 − 10x² + 4x⁴,                      𝔢_3 = (1/16)(−39x + 195x³ + 3x⁵ + 9x⁷),
    𝔢_4 = (1/8)(−15x² + 63x⁴ + 27x⁶ + 9x⁸),    𝔢_5 = (1/16)(53x³ − 125x⁵ − 85x⁷ − 27x⁹);

here 𝔢_0 = 3/2 − 6x² + 6x²(1 + x²)³ − 1 and 𝔢_1 = (15/4)(x³ − x) + (17/2)x²(1 + x²)³.

Case 0 ≤ x ≤ 1. Dropping nonnegative terms, 𝔢_0 ≥ 1/2 + 18x⁴, 𝔢_1 ≥ −(15/4)x + (17/2)x², 𝔢_2 ≥ 1 − 10x²,
𝔢_3 ≥ −(39/16)x and 𝔢_4 ≥ −(15/8)x². As x ≤ 1, 125x⁵ + 85x⁷ + 27x⁹ − 53x³ ≤ 184x³ ≤ 184x², so 𝔢_5 ≥ −(23/2)x². Hence

    𝒬 ≥ 1/2 + μ² − β_1x + β_2x² + 18x⁴,
    β_1 := (15/4)μ + (39/16)μ³,     β_2 := (17/2)μ − 10μ² − (15/8)μ⁴ − (23/2)μ⁵.

β_1 increases with μ, so β_1 ≤ β_1(1/2) = 279/128. β_2 is concave in μ ≥ 0, so on [1/12, 1/2] it is at least
min(β_2(1/12), β_2(1/2)) = min(0.63875…, 1.2734…) > 0.6387. And 18x⁴ ≥ (9/4)x² − 9/128, since 18(x² − 1/16)² ≥ 0. So
𝒬 ≥ γ_0 − (279/128)x + γ_2x² with γ_0 := 1/2 + 1/144 − 9/128 > 0.4366 and γ_2 := 0.6387 + 9/4 = 2.8887. This quadratic
has positive leading coefficient and discriminant (279/128)² − 4γ_0γ_2 < 4.7512 − 5.0448 < 0, so 𝒬 > 0.

Case −1 ≤ x < 0. Put ξ := −x ∈ (0, 1]. Then 𝔢_0 ≥ 1/2, 𝔢_1 = (15/4)ξ(1 − ξ²) + (17/2)ξ² + (51/2)(ξ⁴ + ξ⁶) +
(17/2)ξ⁸ ≥ (17/2)ξ², 𝔢_2 ≥ 1 − 10ξ², 𝔢_3 = (ξ/16)(39 − 195ξ² − 3ξ⁴ − 9ξ⁶) ≥ −(207/16)ξ³ ≥ −(207/16)ξ²,
𝔢_4 ≥ −(15/8)ξ² and 𝔢_5 = (ξ³/16)(−53 + 125ξ² + 85ξ⁴ + 27ξ⁶) ≥ −(53/16)ξ². Hence 𝒬 ≥ 1/2 + μ² − β_3ξ², with
β_3 := 10μ² + (207/16)μ³ + (15/8)μ⁴ + (53/16)μ⁵ − (17/2)μ. β_3 is convex in μ ≥ 0, so on [1/12, 1/2] it is at most
max(β_3(1/12), β_3(1/2)) = β_3(1/2) = 45/512, as β_3(1/12) < 0. As μ² ≥ 0 and ξ² ≤ 1,
𝒬 ≥ 1/2 − max(β_3, 0)ξ² ≥ 1/2 − 45/512 > 0.

Case 1 ≤ |x| ≤ ν. Here x² ≥ 1, μ ≤ 1/2 and μ|x| ≤ 1. First 𝔢_1 ≥ 0: for x ≥ 1, (15/4)(x³ − x) ≥ 0 and the other terms
are nonnegative; for x ≤ −1, with ξ = −x, 𝔢_1 ≥ (17/2)ξ² + (51/2)ξ⁴ − (15/4)ξ³ ≥ 0, as ξ³ ≤ (ξ² + ξ⁴)/2. Next, using
μ|x| ≤ 1 to trade a power of μ for a power of |x|, and μ ≤ 1/2,

    μ²𝔢_2 ≥ −10μ²x² ≥ −(5/2)x²,                        μ⁴𝔢_4 ≥ −(15/8)μ⁴x² ≥ −(15/128)x²,
    μ³|𝔢_3| ≤ (μ²/16)(39 + 195x² + 3x⁴ + 9x⁶) ≤ (1/64)(39 + 195x² + 3x⁴ + 9x⁶),
    μ⁵|𝔢_5| ≤ (μ⁴/16)(53x² + 125x⁴ + 85x⁶ + 27x⁸) ≤ (1/256)(53x² + 125x⁴ + 85x⁶ + 27x⁸).

Adding these to 𝔢_0,

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
0.74362ν (as in [[prop:morawetz-resolvent-l-ge-1]]). Since Φ is odd and increasing,
max_I |φ| = max(Φ(7ν/8), Φ(7ν/18)) = Φ(7ν/8), and |φ(±∞)| = Φ(ν). ∎

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
8.878, 4.683, 5.990, 4.097, 3.022 and 2.252 at |σ| = 3, 6, 12, 24, 48 and 96; at most 2.024, 1.869 and 1.743
at |σ| = 128, 160 and 192; and at most 1.677, 1.815 and 1.963 for every |σ| in [σ_+ − 1/20, σ_+] with σ_+ = 256, 320
and 384.

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
largest value on [3, 384] is 11.477, on [3.2, 3.25]. These values times |σ|^(1/2) are 9.77, 9.20 and 8.58
at |σ| = 96, 192 and 384 (the last with 0.43792), so between |σ| = 96 and 384 they decay roughly like |σ|^(−0.6); the
scaling of the best multiplier at the trapped harmonic (the l with max V_l nearest σ²) suggests |σ|^(−1/2) for
larger |σ|. The values from |σ| = 12 on and the decay are not proved here ([[prop:band-points]] proves weaker ones),
and no proof uses them; the largest value, 11.477, is the constant of [[thm:band]].

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

For the sum, [[cor:morawetz-one-derivative]] (a) with B*_l replaced by B̃ gives, for l ≥ 2,
κ∫_I ψ|u_l|² ≤ (κ/(κ − 3))J♯‖F_l‖², J♯ := 2X(B̃) + (M′ + 2|σ|)B̃ < 566.12 + 8822.88 < 9389.0, and κ/(κ − 3) ≤ 8/5 as
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
these values at the sampled frequencies, the ratio growing with σ from σ = 6 on. With one multiplier of fixed width
for every frequency, the bound of [[lem:morawetz-identity]] grows instead like |σ|: maximised over l, with the best of
forty tanh widths at each σ, it is 253, 429, 800, 1554, 3068 and 6099 at σ = 3, 6, 12, 24, 48 and 96, set by l = 1. No
proof uses these values.

### Tables for the Morawetz multipliers {#sec:tb-morawetz}

These tables carry the numbers used by [[prop:morawetz-polynomial]] and [[prop:morawetz-master-potentials]]. The
notation is that of [[sec:morawetz-identity]]: y = 1/r², z = 1 − 2y, η = (1 − y)y^(3/2) = (r² − 1)/r⁵ and
I = {6/5 ≤ r ≤ 4}. For a polynomial p of degree n and an interval [α, β], b_0, …, b_n are the Bernstein coefficients of
p on [α, β] in the notation of [[lem:bernstein-lower-bound]], so that min_k b_k ≤ p ≤ max_k b_k on [α, β]. A list gives
b_0, …, b_n in order, each rounded to five significant digits, or to the nearest integer when it exceeds 10⁵; a
least coefficient in a column of its own is rounded down and a greatest one rounded up. A piece "r_1–r_2" of I is the
interval r_2 ≤ r ≤ r_1, that is 1/r_1² ≤ y ≤ 1/r_2². Since η increases on [0, 3/5] and decreases on [3/5, 1] in y, its
least value on a piece is at an end, and "η ≥" is that value rounded down; "η ≤" is its greatest value on the piece,
rounded up (6√15/125 < 0.18591 on a piece that contains y = 3/5). An entry of a column headed "product ≥" (respectively
"product ≤") is the product of the exact factors, rounded down (respectively up), and not the product of the
printed factors, from which it may differ in the last digit; on a piece containing y = 3/5 the factor η is taken as
0.18591 in a "product ≤" entry. The product of the printed factors satisfies the same bound against the constant of
its table.

#### The weight polynomials {#sec:tb-morawetz-weights}

Each weight G of [[prop:morawetz-polynomial]] is listed by its coefficients of y⁰, y¹, …; for S3 the polynomial
listed is Π := 120(2 + y)³G.

- A1 (Θ_A, V_(15/4,5/4)): 243/32, −1731/40, −19/160, 9263/20, −6919/8, 4431/10.
- A2 (Θ_A, V_(15/4,9/4)): 243/32, −1569/40, −2079/160, 9359/20, −34047/40, 4347/10.
- B1 (Θ_B, V_(35/4,−7/4)): 343/16, −14257/120, 5689/80, 124103/120, −166373/60, 26071/10, −2506/3.
- B2 (Θ_B, V_(35/4,9/4)): 343/16, −2381/24, 1243/240, 127031/120, −159989/60, 74837/30, −2410/3.
- E2 (Θ_E, V_(35/4,9/4)): 35/3, −52/3, −319, 4100/3, −5566/3, 828.
- C1 (Θ_C, V_(63/4,−27/4)): 1197/40, −3797/40, −5065/8, 103499/24, −280579/30, 87209/10, −44642/15.
- C3 (Θ_C, V_(63/4,9/4)): 1197/40, −2429/40, −27689/40, 485779/120, −256423/30, 79709/10, −8194/3.
- C4 (Θ_C, V_(99/4,9/4)): 1881/40, −3953/40, −32897/40, 542371/120, −270607/30, 81341/10, −8194/3.
- C5 (Θ_C, V_(143/4,9/4)): 2717/40, −17447/120, −117787/120, 611539/120, −95981/10, 250007/30, −8194/3.
- C6 (Θ_C, V_(195/4,9/4)): 741/8, −8017/40, −9357/8, 693283/120, −308431/30, 85693/10, −8194/3.
- S3 (Θ_C, V_S, l = 3): 28728, −80868, −633378, 3396065, −4298021, −860697, 3158651, 673100, −1036164, −327760.
- T2 (Θ_T, V_(35/4,−27/4)): 357/16, −3233/20, 26791/80, 2889/10, −7191/4, 10506/5, −3939/5.

For V_S at l ≥ 4 and Θ_C, with t := κ − 24 ≥ 0, 16H³G = c_0 + c_1t + c_2t² + c_3t³ + c_4t⁴, where

- c_0: 34839882/5, −86791446/5, −594687366/5, 3160192878/5, −4938188076/5, 1873269504/5, 1451374272/5, −467276832/5,
  −360656064/5, −9439488.
- c_1: 6384798/5, −15290982/5, −96274278/5, 502403094/5, −828060072/5, 454017456/5, 20523552, −97773984/5, −23494272/5.
- c_2: 438102/5, −1015218/5, −5634066/5, 28203066/5, −47313268/5, 32390216/5, −2867408/5, −3898304/5.
- c_3: 13338/5, −30154/5, −138498/5, 379822/3, −2990456/15, 746472/5, −131104/3.
- c_4: 152/5, −1016/15, −3472/15, 4192/5, −12608/15, 4352/15.

#### Positivity on [0, 1] {#sec:tb-morawetz-positivity}

Bernstein coefficients of each weight polynomial on the listed subintervals of [0, 1] in y; every one is positive.

| polynomial | subinterval | Bernstein coefficients |
|---|---|---|
| A1 | [0, 1/4] | 7.5938, 5.4300, 3.2655, 1.8239, 1.1533, 1.0586 |
| A1 | [1/4, 1/2] | 1.0586, 0.96389, 1.4451, 2.3073, 3.1125, 3.6125 |
| A1 | [1/2, 3/4] | 3.6125, 4.1125, 4.3073, 3.9487, 2.9783, 1.9600 |
| A1 | [3/4, 7/8] | 1.9600, 1.4508, 0.92970, 0.46712, 0.17249, 0.20763 |
| A1 | [7/8, 1] | 0.20763, 0.24276, 0.60768, 1.4642, 3.0266, 5.5750 |
| A2 | [0, 1/4] | 7.5938, 5.6325, 3.5900, 2.1975, 1.5212, 1.3867 |
| A2 | [1/4, 1/2] | 1.3867, 1.2522, 1.6596, 2.4346, 3.1625, 3.6125 |
| A2 | [1/2, 3/4] | 3.6125, 4.0625, 4.2346, 3.8982, 3.0066, 2.1217 |
| A2 | [3/4, 1] | 2.1217, 1.2367, 0.35848, 0.048789, 1.4781, 6.8500 |
| B1 | [0, 1/2] | 21.438, 11.537, 2.8213, 1.7547, 3.2471, 4.2333, 4.2000 |
| B1 | [1/2, 3/4] | 4.2000, 4.1833, 3.9118, 3.3211, 2.5067, 1.7397, 1.2797 |
| B1 | [3/4, 1] | 1.2797, 0.81972, 0.66682, 1.0806, 2.3093, 4.4017, 6.8167 |
| B2 | [0, 1/2] | 21.438, 13.170, 4.9891, 3.5106, 4.2404, 4.5667, 4.2000 |
| B2 | [1/2, 3/4] | 4.2000, 4.0167, 3.6601, 3.0941, 2.4278, 1.9290, 1.8422 |
| B2 | [3/4, 1] | 1.8422, 1.7554, 2.0806, 3.0624, 4.9218, 7.6740, 10.750 |
| E2 | [0, 1/4] | 11.667, 10.800, 7.9396, 5.2208, 3.3297, 2.3112 |
| E2 | [1/4, 1/2] | 2.3112, 1.2927, 1.1469, 1.9188, 3.0125, 4.0000 |
| E2 | [1/2, 3/4] | 4.0000, 4.9875, 5.8688, 6.2156, 5.7677, 5.2409 |
| E2 | [3/4, 1] | 5.2409, 4.7141, 4.1083, 4.1396, 6.5000, 14.667 |
| C1 | [0, 1/2] | 29.925, 22.015, 3.5521, 1.4904, 3.8130, 4.9556, 4.7250 |
| C1 | [1/2, 3/4] | 4.7250, 4.6097, 4.1512, 3.3252, 2.4434, 2.1192, 2.5078 |
| C1 | [3/4, 1] | 2.5078, 2.8964, 3.9977, 5.9669, 8.5005, 10.076, 6.4667 |
| C3 | [0, 1/2] | 29.925, 24.865, 8.2671, 5.4335, 6.0505, 5.7056, 4.7250 |
| C3 | [1/2, 1] | 4.7250, 3.7444, 2.1283, 0.20276, 3.0331, 19.261, 17.267 |
| C4 | [0, 1/2] | 47.025, 38.790, 16.847, 9.4460, 7.2505, 5.7056, 4.7250 |
| C4 | [1/2, 1] | 4.7250, 3.7444, 3.3283, 3.3903, 8.3131, 26.636, 28.067 |
| C5 | [0, 1/2] | 67.925, 55.809, 27.334, 14.350, 8.7172, 5.7056, 4.7250 |
| C5 | [1/2, 1] | 4.7250, 3.7444, 4.7949, 7.2861, 14.766, 35.650, 41.267 |
| C6 | [0, 1/2] | 92.625, 75.923, 39.727, 20.146, 10.450, 5.7056, 4.7250 |
| C6 | [1/2, 1] | 4.7250, 3.7444, 6.5283, 11.890, 22.393, 46.303, 56.867 |
| S3 | [0, 1/2] | 28728, 24235, 15344, 7108.3, 2449.3, 1943.5, 4195.9, 6947.8, 8614.4, 8859.4 |
| S3 | [1/2, 3/4] | 8859.4, 8981.8, 8748.9, 8118.4, 7126.4, 5904.7, 4684.0, 3770.9, 3483.4, 4025.5 |
| S3 | [3/4, 1] | 4025.5, 4567.6, 5939.3, 8344.3, 11872, 16373, 21268, 25281, 26060, 19656 |
| T2 | [0, 1/2] | 22.312, 8.8417, 0.95229, 0.45000, 1.6498, 2.3198, 2.3156 |
| T2 | [1/2, 3/4] | 2.3156, 2.3135, 2.1429, 1.7857, 1.3543, 1.0490, 0.92271 |
| T2 | [3/4, 1] | 0.92271, 0.79642, 0.84918, 1.1340, 1.5566, 1.6406, 0.10000 |
| c_0 | [0, 1/2] | 6967976, 6003627, 4213323, 2537598, 1427086, 935441, 866253, 953675, 1025178, 1045094 |
| c_0 | [1/2, 1] | 1045094, 1065011, 1033342, 914422, 809450, 1000035, 1872542, 3621891, 5583751, 4975862 |
| c_1 | [0, 1/2] | 1276960, 1085822, 722767, 412080, 230181, 156293, 134567, 128563, 130637 |
| c_1 | [1/2, 1] | 130637, 132710, 142861, 153445, 185610, 298690, 554484, 899014, 905904 |
| c_2 | [0, 1/2] | 87620, 73117, 45200, 24013, 12804, 7562.8, 5381.7, 5443.2 |
| c_2 | [1/2, 1] | 5443.2, 5504.7, 7809.0, 11539, 17968, 31450, 53034, 60624 |
| c_3 | [0, 1/2] | 2667.6, 2165.0, 1200.8, 566.22, 221.87, 75.289, 75.600 |
| c_3 | [1/2, 1] | 75.600, 75.911, 223.12, 466.36, 796.42, 1340.4, 1773.9 |

#### The weight on I {#sec:tb-morawetz-pieces}

For each row of [[prop:morawetz-polynomial]] the pieces below cover I. A line gives the least value of η on the
piece, the Bernstein coefficients of the weight polynomial on the piece, their least value, and the product, a lower
bound for w = ηG on the piece (for S3, the least coefficient is divided by 120(2 + y)³ at the right end of the piece,
its largest value there).
Every product is at least the w_I of [[prop:morawetz-polynomial]].

Row A (weights A1, A2), w_I ≥ 0.0728:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–319/80 | A1 | 0.014648 | 4.9889, 4.9859, 4.9828, 4.9798, 4.9768, 4.9737 | 4.9737 | 0.072857 |
| 4–319/80 | A2 | 0.014648 | 5.1931, 5.1903, 5.1874, 5.1846, 5.1818, 5.1789 | 5.1789 | 0.075863 |
| 319/80–159/40 | A1 | 0.014780 | 4.9737, 4.9707, 4.9676, 4.9646, 4.9615, 4.9584 | 4.9584 | 0.073287 |
| 319/80–159/40 | A2 | 0.014780 | 5.1789, 5.1761, 5.1732, 5.1703, 5.1675, 5.1646 | 5.1646 | 0.076335 |
| 159/40–79/20 | A1 | 0.014914 | 4.9584, 4.9522, 4.9460, 4.9399, 4.9337, 4.9275 | 4.9274 | 0.073488 |
| 159/40–79/20 | A2 | 0.014914 | 5.1646, 5.1588, 5.1530, 5.1472, 5.1414, 5.1357 | 5.1356 | 0.076593 |
| 79/20–39/10 | A1 | 0.015185 | 4.9275, 4.9148, 4.9021, 4.8894, 4.8767, 4.8641 | 4.8640 | 0.073865 |
| 79/20–39/10 | A2 | 0.015185 | 5.1357, 5.1238, 5.1119, 5.1000, 5.0881, 5.0763 | 5.0763 | 0.077088 |
| 39/10–19/5 | A1 | 0.015749 | 4.8641, 4.8373, 4.8106, 4.7839, 4.7574, 4.7309 | 4.7309 | 0.074510 |
| 39/10–19/5 | A2 | 0.015749 | 5.0763, 5.0512, 5.0262, 5.0012, 4.9764, 4.9516 | 4.9515 | 0.077985 |
| 19/5–73/20 | A1 | 0.016962 | 4.7309, 4.6871, 4.6435, 4.6002, 4.5571, 4.5143 | 4.5142 | 0.076572 |
| 19/5–73/20 | A2 | 0.016962 | 4.9516, 4.9105, 4.8696, 4.8289, 4.7884, 4.7482 | 4.7481 | 0.080539 |
| 73/20–33/10 | A1 | 0.019021 | 4.5143, 4.3907, 4.2693, 4.1501, 4.0333, 3.9189 | 3.9189 | 0.074542 |
| 73/20–33/10 | A2 | 0.019021 | 4.7482, 4.6320, 4.5177, 4.4054, 4.2951, 4.1869 | 4.1869 | 0.079639 |
| 33/10–59/20 | A1 | 0.025271 | 3.9189, 3.7615, 3.6087, 3.4608, 3.3179, 3.1803 | 3.1802 | 0.080369 |
| 33/10–59/20 | A2 | 0.025271 | 4.1869, 4.0380, 3.8932, 3.7526, 3.6166, 3.4852 | 3.4851 | 0.088074 |
| 59/20–13/5 | A1 | 0.034476 | 3.1803, 2.9834, 2.7971, 2.6220, 2.4582, 2.3060 | 2.3060 | 0.079503 |
| 59/20–13/5 | A2 | 0.034476 | 3.4852, 3.2972, 3.1188, 2.9504, 2.7924, 2.6449 | 2.6449 | 0.091186 |
| 13/5–12/5 | A1 | 0.048479 | 2.3060, 2.1877, 2.0763, 1.9721, 1.8749, 1.7849 | 1.7848 | 0.086529 |
| 13/5–12/5 | A2 | 0.048479 | 2.6449, 2.5302, 2.4219, 2.3201, 2.2249, 2.1362 | 2.1361 | 0.10356 |
| 12/5–9/4 | A1 | 0.059779 | 1.7849, 1.7010, 1.6234, 1.5519, 1.4865, 1.4272 | 1.4271 | 0.085314 |
| 12/5–9/4 | A2 | 0.059779 | 2.1362, 2.0536, 1.9767, 1.9055, 1.8400, 1.7801 | 1.7801 | 0.10641 |
| 9/4–21/10 | A1 | 0.070449 | 1.4272, 1.3547, 1.2913, 1.2368, 1.1911, 1.1539 | 1.1538 | 0.081290 |
| 9/4–21/10 | A2 | 0.070449 | 1.7801, 1.7070, 1.6422, 1.5858, 1.5376, 1.4974 | 1.4973 | 0.10548 |
| 21/10–19/10 | A1 | 0.083494 | 1.1539, 1.0899, 1.0512, 1.0364, 1.0440, 1.0720 | 1.0364 | 0.086534 |
| 21/10–19/10 | A2 | 0.083494 | 1.4974, 1.4282, 1.3826, 1.3596, 1.3576, 1.3750 | 1.3576 | 0.11335 |
| 19/10–6/5 | A1 | 0.10540 | 1.0720, 1.3047, 2.9448, 4.8636, 4.4073, 3.0132 | 1.0720 | 0.11300 |
| 19/10–6/5 | A2 | 0.10540 | 1.3750, 1.5191, 2.9946, 4.7712, 4.3062, 3.0538 | 1.3749 | 0.14493 |

Row A′ (weight A2), w_I ≥ 0.0756:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–159/40 | A2 | 0.014648 | 5.1931, 5.1874, 5.1817, 5.1760, 5.1703, 5.1646 | 5.1646 | 0.075653 |
| 159/40–79/20 | A2 | 0.014914 | 5.1646, 5.1588, 5.1530, 5.1472, 5.1414, 5.1357 | 5.1356 | 0.076593 |
| 79/20–39/10 | A2 | 0.015185 | 5.1357, 5.1238, 5.1119, 5.1000, 5.0881, 5.0763 | 5.0763 | 0.077088 |
| 39/10–19/5 | A2 | 0.015749 | 5.0763, 5.0512, 5.0262, 5.0012, 4.9764, 4.9516 | 4.9515 | 0.077985 |
| 19/5–73/20 | A2 | 0.016962 | 4.9516, 4.9105, 4.8696, 4.8289, 4.7884, 4.7482 | 4.7481 | 0.080539 |
| 73/20–33/10 | A2 | 0.019021 | 4.7482, 4.6320, 4.5177, 4.4054, 4.2951, 4.1869 | 4.1869 | 0.079639 |
| 33/10–59/20 | A2 | 0.025271 | 4.1869, 4.0380, 3.8932, 3.7526, 3.6166, 3.4852 | 3.4851 | 0.088074 |
| 59/20–13/5 | A2 | 0.034476 | 3.4852, 3.2972, 3.1188, 2.9504, 2.7924, 2.6449 | 2.6449 | 0.091186 |
| 13/5–9/4 | A2 | 0.048479 | 2.6449, 2.4234, 2.2257, 2.0527, 1.9043, 1.7801 | 1.7801 | 0.086299 |
| 9/4–19/10 | A2 | 0.070449 | 1.7801, 1.5812, 1.4445, 1.3683, 1.3475, 1.3750 | 1.3475 | 0.094933 |
| 19/10–6/5 | A2 | 0.10540 | 1.3750, 1.5191, 2.9946, 4.7712, 4.3062, 3.0538 | 1.3749 | 0.14493 |

Row B (weights B1, B2), w_I ≥ 0.211:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–159/40 | B1 | 0.014648 | 14.502, 14.489, 14.476, 14.463, 14.450, 14.437, 14.423 | 14.423 | 0.21128 |
| 4–159/40 | B2 | 0.014648 | 15.477, 15.466, 15.454, 15.442, 15.431, 15.419, 15.408 | 15.407 | 0.22569 |
| 159/40–79/20 | B1 | 0.014914 | 14.423, 14.410, 14.397, 14.383, 14.370, 14.357, 14.343 | 14.343 | 0.21391 |
| 159/40–79/20 | B2 | 0.014914 | 15.408, 15.396, 15.384, 15.372, 15.360, 15.348, 15.337 | 15.336 | 0.22873 |
| 79/20–39/10 | B1 | 0.015185 | 14.343, 14.316, 14.288, 14.261, 14.234, 14.206, 14.179 | 14.178 | 0.21532 |
| 79/20–39/10 | B2 | 0.015185 | 15.337, 15.312, 15.288, 15.264, 15.240, 15.215, 15.191 | 15.191 | 0.23069 |
| 39/10–19/5 | B1 | 0.015749 | 14.179, 14.121, 14.063, 14.006, 13.949, 13.892, 13.835 | 13.834 | 0.21788 |
| 39/10–19/5 | B2 | 0.015749 | 15.191, 15.140, 15.089, 15.038, 14.987, 14.937, 14.886 | 14.886 | 0.23445 |
| 19/5–73/20 | B1 | 0.016962 | 13.835, 13.740, 13.646, 13.553, 13.460, 13.368, 13.276 | 13.275 | 0.22518 |
| 19/5–73/20 | B2 | 0.016962 | 14.886, 14.802, 14.719, 14.636, 14.553, 14.471, 14.389 | 14.388 | 0.24406 |
| 73/20–33/10 | B1 | 0.019021 | 13.276, 13.010, 12.749, 12.492, 12.240, 11.991, 11.747 | 11.747 | 0.22344 |
| 73/20–33/10 | B2 | 0.019021 | 14.389, 14.152, 13.919, 13.688, 13.461, 13.237, 13.017 | 13.017 | 0.24759 |
| 33/10–59/20 | B1 | 0.025271 | 11.747, 11.412, 11.084, 10.765, 10.455, 10.153, 9.8603 | 9.8602 | 0.24918 |
| 33/10–59/20 | B2 | 0.025271 | 13.017, 12.714, 12.417, 12.126, 11.842, 11.565, 11.295 | 11.295 | 0.28544 |
| 59/20–13/5 | B1 | 0.034476 | 9.8603, 9.4412, 9.0399, 8.6566, 8.2913, 7.9440, 7.6144 | 7.6143 | 0.26251 |
| 59/20–13/5 | B2 | 0.034476 | 11.295, 10.909, 10.537, 10.179, 9.8360, 9.5074, 9.1932 | 9.1932 | 0.31694 |
| 13/5–9/4 | B1 | 0.048479 | 7.6144, 7.1192, 6.6642, 6.2487, 5.8717, 5.5319, 5.2276 | 5.2276 | 0.25343 |
| 13/5–9/4 | B2 | 0.048479 | 9.1932, 8.7214, 8.2823, 7.8759, 7.5015, 7.1582, 6.8447 | 6.8447 | 0.33182 |
| 9/4–19/10 | B1 | 0.070449 | 5.2276, 4.7401, 4.3438, 4.0320, 3.7962, 3.6268, 3.5139 | 3.5139 | 0.24755 |
| 9/4–19/10 | B2 | 0.070449 | 6.8447, 6.3425, 5.9170, 5.5632, 5.2743, 5.0426, 4.8600 | 4.8600 | 0.34239 |
| 19/10–6/5 | B1 | 0.10540 | 3.5139, 2.9212, 3.8885, 4.9871, 4.5385, 3.1887, 2.0636 | 2.0636 | 0.21751 |
| 19/10–6/5 | B2 | 0.10540 | 4.8600, 3.9010, 4.2957, 4.8683, 4.1676, 2.9161, 2.2092 | 2.2091 | 0.23286 |

Row B′ (weight B2), w_I ≥ 0.224:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–79/20 | B2 | 0.014648 | 15.477, 15.454, 15.430, 15.407, 15.383, 15.360, 15.337 | 15.336 | 0.22465 |
| 79/20–39/10 | B2 | 0.015185 | 15.337, 15.312, 15.288, 15.264, 15.240, 15.215, 15.191 | 15.191 | 0.23069 |
| 39/10–19/5 | B2 | 0.015749 | 15.191, 15.140, 15.089, 15.038, 14.987, 14.937, 14.886 | 14.886 | 0.23445 |
| 19/5–73/20 | B2 | 0.016962 | 14.886, 14.802, 14.719, 14.636, 14.553, 14.471, 14.389 | 14.388 | 0.24406 |
| 73/20–33/10 | B2 | 0.019021 | 14.389, 14.152, 13.919, 13.688, 13.461, 13.237, 13.017 | 13.017 | 0.24759 |
| 33/10–13/5 | B2 | 0.025271 | 13.017, 12.279, 11.580, 10.920, 10.303, 9.7269, 9.1932 | 9.1932 | 0.23232 |
| 13/5–19/10 | B2 | 0.048479 | 9.1932, 7.9654, 6.9594, 6.1728, 5.5826, 5.1566, 4.8600 | 4.8600 | 0.23561 |
| 19/10–6/5 | B2 | 0.10540 | 4.8600, 3.9010, 4.2957, 4.8683, 4.1676, 2.9161, 2.2092 | 2.2091 | 0.23286 |

Row E (weight E2), w_I ≥ 0.139:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–39/10 | E2 | 0.014648 | 9.6434, 9.6155, 9.5875, 9.5594, 9.5312, 9.5029 | 9.5029 | 0.13920 |
| 39/10–19/5 | E2 | 0.015749 | 9.5029, 9.4724, 9.4417, 9.4109, 9.3800, 9.3490 | 9.3489 | 0.14724 |
| 19/5–73/20 | E2 | 0.016962 | 9.3490, 9.2976, 9.2459, 9.1940, 9.1418, 9.0894 | 9.0893 | 0.15417 |
| 73/20–33/10 | E2 | 0.019021 | 9.0894, 8.9380, 8.7847, 8.6298, 8.4737, 8.3168 | 8.3168 | 0.15819 |
| 33/10–13/5 | E2 | 0.025271 | 8.3168, 7.7917, 7.2572, 6.7266, 6.2102, 5.7162 | 5.7161 | 0.14445 |
| 13/5–9/4 | E2 | 0.048479 | 5.7162, 5.2793, 4.8599, 4.4634, 4.0937, 3.7537 | 3.7536 | 0.18197 |
| 9/4–21/10 | E2 | 0.070449 | 3.7537, 3.5533, 3.3632, 3.1840, 3.0160, 2.8595 | 2.8594 | 0.20144 |
| 21/10–19/10 | E2 | 0.083494 | 2.8595, 2.5904, 2.3554, 2.1558, 1.9920, 1.8630 | 1.8630 | 0.15555 |
| 19/10–31/20 | E2 | 0.10540 | 1.8630, 1.5059, 1.4172, 1.5826, 1.9343, 2.3945 | 1.4172 | 0.14938 |
| 31/20–6/5 | E2 | 0.15676 | 2.3945, 3.3143, 4.6676, 5.8349, 6.0378, 5.7202 | 2.3945 | 0.37537 |

Row C (weights C1, C3), w_I ≥ 0.325:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–79/20 | C1 | 0.014648 | 22.437, 22.402, 22.367, 22.332, 22.297, 22.262, 22.227 | 22.227 | 0.32559 |
| 4–79/20 | C3 | 0.014648 | 24.291, 24.262, 24.234, 24.205, 24.177, 24.148, 24.119 | 24.119 | 0.35331 |
| 79/20–39/10 | C1 | 0.015185 | 22.227, 22.191, 22.154, 22.118, 22.081, 22.045, 22.009 | 22.008 | 0.33422 |
| 79/20–39/10 | C3 | 0.015185 | 24.119, 24.090, 24.060, 24.030, 24.000, 23.971, 23.941 | 23.940 | 0.36356 |
| 39/10–19/5 | C1 | 0.015749 | 22.009, 21.931, 21.854, 21.777, 21.700, 21.623, 21.546 | 21.545 | 0.33933 |
| 39/10–19/5 | C3 | 0.015749 | 23.941, 23.877, 23.814, 23.751, 23.687, 23.624, 23.560 | 23.560 | 0.37106 |
| 19/5–73/20 | C1 | 0.016962 | 21.546, 21.418, 21.290, 21.162, 21.035, 20.907, 20.780 | 20.779 | 0.35247 |
| 19/5–73/20 | C3 | 0.016962 | 23.560, 23.455, 23.349, 23.244, 23.138, 23.032, 22.926 | 22.925 | 0.38887 |
| 73/20–33/10 | C1 | 0.019021 | 20.780, 20.412, 20.046, 19.681, 19.318, 18.957, 18.599 | 18.598 | 0.35377 |
| 73/20–33/10 | C3 | 0.019021 | 22.926, 22.620, 22.314, 22.007, 21.700, 21.394, 21.089 | 21.088 | 0.40113 |
| 33/10–59/20 | C1 | 0.025271 | 18.599, 18.106, 17.619, 17.137, 16.663, 16.196, 15.738 | 15.737 | 0.39771 |
| 33/10–59/20 | C3 | 0.025271 | 21.089, 20.669, 20.251, 19.835, 19.423, 19.015, 18.612 | 18.612 | 0.47035 |
| 59/20–13/5 | C1 | 0.034476 | 15.738, 15.082, 14.444, 13.825, 13.226, 12.650, 12.096 | 12.096 | 0.41702 |
| 59/20–13/5 | C3 | 0.034476 | 18.612, 18.036, 17.470, 16.916, 16.376, 15.851, 15.341 | 15.341 | 0.52891 |
| 13/5–9/4 | C1 | 0.048479 | 12.096, 11.264, 10.484, 9.7580, 9.0880, 8.4741, 7.9155 | 7.9154 | 0.38373 |
| 13/5–9/4 | C3 | 0.048479 | 15.341, 14.577, 13.848, 13.159, 12.511, 11.906, 11.343 | 11.342 | 0.54989 |
| 9/4–21/10 | C1 | 0.070449 | 7.9155, 7.5863, 7.2763, 6.9854, 6.7132, 6.4594, 6.2234 | 6.2234 | 0.43843 |
| 9/4–21/10 | C3 | 0.070449 | 11.343, 11.011, 10.694, 10.392, 10.104, 9.8301, 9.5705 | 9.5705 | 0.67424 |
| 21/10–19/10 | C1 | 0.083494 | 6.2234, 5.8177, 5.4648, 5.1624, 4.9072, 4.6956, 4.5237 | 4.5237 | 0.37770 |
| 21/10–19/10 | C3 | 0.083494 | 9.5705, 9.1242, 8.7192, 8.3540, 8.0264, 7.7337, 7.4729 | 7.4728 | 0.62394 |
| 19/10–31/20 | C1 | 0.10540 | 4.5237, 4.0474, 3.8754, 3.9236, 4.0902, 4.2889, 4.4601 | 3.8753 | 0.40849 |
| 19/10–31/20 | C3 | 0.10540 | 7.4729, 6.7504, 6.2731, 5.9778, 5.7851, 5.6294, 5.4683 | 5.4683 | 0.57640 |
| 31/20–6/5 | C1 | 0.15676 | 4.4601, 4.8022, 5.0342, 4.6798, 3.6872, 2.7868, 2.4692 | 2.4692 | 0.38708 |
| 31/20–6/5 | C3 | 0.15676 | 5.4683, 5.1466, 4.8037, 4.1034, 3.0861, 2.4882, 2.7951 | 2.4881 | 0.39005 |

Row C3 (weight C3), w_I ≥ 0.352:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–79/20 | C3 | 0.014648 | 24.291, 24.262, 24.234, 24.205, 24.177, 24.148, 24.119 | 24.119 | 0.35331 |
| 79/20–39/10 | C3 | 0.015185 | 24.119, 24.090, 24.060, 24.030, 24.000, 23.971, 23.941 | 23.940 | 0.36356 |
| 39/10–19/5 | C3 | 0.015749 | 23.941, 23.877, 23.814, 23.751, 23.687, 23.624, 23.560 | 23.560 | 0.37106 |
| 19/5–73/20 | C3 | 0.016962 | 23.560, 23.455, 23.349, 23.244, 23.138, 23.032, 22.926 | 22.925 | 0.38887 |
| 73/20–33/10 | C3 | 0.019021 | 22.926, 22.620, 22.314, 22.007, 21.700, 21.394, 21.089 | 21.088 | 0.40113 |
| 33/10–13/5 | C3 | 0.025271 | 21.089, 20.068, 19.057, 18.071, 17.118, 16.207, 15.341 | 15.341 | 0.38769 |
| 13/5–19/10 | C3 | 0.048479 | 15.341, 13.351, 11.605, 10.165, 9.0233, 8.1427, 7.4729 | 7.4728 | 0.36228 |
| 19/10–31/20 | C3 | 0.10540 | 7.4729, 6.7504, 6.2731, 5.9778, 5.7851, 5.6294, 5.4683 | 5.4683 | 0.57640 |
| 31/20–6/5 | C3 | 0.15676 | 5.4683, 5.1466, 4.8037, 4.1034, 3.0861, 2.4882, 2.7951 | 2.4881 | 0.39005 |

Row C4 (weight C4), w_I ≥ 0.559:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–79/20 | C4 | 0.014648 | 38.609, 38.568, 38.526, 38.484, 38.443, 38.401, 38.359 | 38.359 | 0.56190 |
| 79/20–39/10 | C4 | 0.015185 | 38.359, 38.316, 38.272, 38.229, 38.185, 38.142, 38.098 | 38.098 | 0.57855 |
| 39/10–19/5 | C4 | 0.015749 | 38.098, 38.006, 37.914, 37.821, 37.729, 37.636, 37.543 | 37.543 | 0.59129 |
| 19/5–73/20 | C4 | 0.016962 | 37.543, 37.390, 37.236, 37.081, 36.927, 36.772, 36.617 | 36.617 | 0.62111 |
| 73/20–33/10 | C4 | 0.019021 | 36.617, 36.171, 35.722, 35.273, 34.824, 34.374, 33.925 | 33.925 | 0.64529 |
| 33/10–13/5 | C4 | 0.025271 | 33.925, 32.423, 30.926, 29.451, 28.010, 26.614, 25.268 | 25.267 | 0.63855 |
| 13/5–19/10 | C4 | 0.048479 | 25.268, 22.172, 19.346, 16.873, 14.767, 13.002, 11.535 | 11.534 | 0.55919 |
| 19/10–31/20 | C4 | 0.10540 | 11.535, 9.9522, 8.7165, 7.7745, 7.0503, 6.4772, 6.0085 | 6.0084 | 0.63334 |
| 31/20–6/5 | C4 | 0.15676 | 6.0085, 5.0719, 4.5523, 4.0781, 3.6009, 3.7610, 4.9848 | 3.6009 | 0.56449 |

Row C5 (weight C5), w_I ≥ 0.8:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–19/5 | C5 | 0.014648 | 56.109, 55.865, 55.620, 55.374, 55.128, 54.881, 54.634 | 54.633 | 0.80029 |
| 19/5–73/20 | C5 | 0.016962 | 54.634, 54.421, 54.208, 53.994, 53.780, 53.566, 53.351 | 53.351 | 0.90495 |
| 73/20–33/10 | C5 | 0.019021 | 53.351, 52.732, 52.111, 51.488, 50.863, 50.239, 49.614 | 49.613 | 0.94370 |
| 33/10–13/5 | C5 | 0.025271 | 49.614, 47.523, 45.432, 43.360, 41.323, 39.333, 37.400 | 37.400 | 0.94515 |
| 13/5–9/4 | C5 | 0.048479 | 37.400, 35.691, 34.027, 32.413, 30.854, 29.355, 27.916 | 27.916 | 1.3533 |
| 9/4–19/10 | C5 | 0.070449 | 27.916, 25.611, 23.462, 21.478, 19.660, 18.003, 16.499 | 16.499 | 1.1623 |
| 19/10–17/10 | C5 | 0.10540 | 16.499, 15.194, 14.004, 12.925, 11.950, 11.071, 10.281 | 10.280 | 1.0836 |
| 17/10–31/20 | C5 | 0.13311 | 10.281, 9.4769, 8.7644, 8.1353, 7.5813, 7.0947, 6.6687 | 6.6686 | 0.88767 |
| 31/20–3/2 | C5 | 0.15676 | 6.6687, 6.4975, 6.3361, 6.1841, 6.0410, 5.9066, 5.7803 | 5.7803 | 0.90614 |
| 3/2–29/20 | C5 | 0.16460 | 5.7803, 5.6408, 5.5114, 5.3915, 5.2809, 5.1791, 5.0859 | 5.0859 | 0.83719 |
| 29/20–57/40 | C5 | 0.17200 | 5.0859, 5.0356, 4.9878, 4.9424, 4.8995, 4.8589, 4.8207 | 4.8207 | 0.82918 |
| 57/40–7/5 | C5 | 0.17539 | 4.8207, 4.7804, 4.7427, 4.7076, 4.6751, 4.6451, 4.6175 | 4.6175 | 0.80990 |
| 7/5–11/8 | C5 | 0.17849 | 4.6175, 4.5885, 4.5623, 4.5388, 4.5181, 4.5002, 4.4850 | 4.4850 | 0.80056 |
| 11/8–27/20 | C5 | 0.18120 | 4.4850, 4.4690, 4.4561, 4.4463, 4.4396, 4.4360, 4.4357 | 4.4356 | 0.80378 |
| 27/20–13/10 | C5 | 0.18342 | 4.4357, 4.4349, 4.4491, 4.4788, 4.5246, 4.5872, 4.6676 | 4.4348 | 0.81348 |
| 13/10–6/5 | C5 | 0.17682 | 4.6676, 4.8595, 5.1529, 5.5608, 6.1013, 6.7955, 7.6612 | 4.6675 | 0.82535 |

Row C6 (weight C6), w_I ≥ 0.815:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–33/10 | C6 | 0.014648 | 76.791, 75.382, 73.955, 72.515, 71.066, 69.611, 68.155 | 68.154 | 0.99835 |
| 33/10–13/5 | C6 | 0.025271 | 68.155, 65.368, 62.575, 59.798, 57.056, 54.366, 51.739 | 51.738 | 1.3075 |
| 13/5–19/10 | C6 | 0.048479 | 51.739, 45.694, 39.986, 34.762, 30.085, 25.960, 22.366 | 22.366 | 1.0843 |
| 19/10–17/10 | C6 | 0.10540 | 22.366, 20.445, 18.676, 17.055, 15.577, 14.235, 13.022 | 13.021 | 1.3725 |
| 17/10–31/20 | C6 | 0.13311 | 13.022, 11.787, 10.686, 9.7097, 8.8501, 8.0990, 7.4489 | 7.4488 | 0.99153 |
| 31/20–3/2 | C6 | 0.15676 | 7.4489, 7.1877, 6.9427, 6.7136, 6.4999, 6.3010, 6.1166 | 6.1166 | 0.95886 |
| 3/2–29/20 | C6 | 0.16460 | 6.1166, 5.9129, 5.7268, 5.5579, 5.4056, 5.2695, 5.1491 | 5.1490 | 0.84758 |
| 29/20–57/40 | C6 | 0.17200 | 5.1491, 5.0841, 5.0237, 4.9678, 4.9163, 4.8693, 4.8267 | 4.8266 | 0.83020 |
| 57/40–113/80 | C6 | 0.17539 | 4.8267, 4.8045, 4.7835, 4.7636, 4.7449, 4.7274, 4.7110 | 4.7110 | 0.82631 |
| 113/80–7/5 | C6 | 0.17699 | 4.7110, 4.6942, 4.6786, 4.6643, 4.6511, 4.6391, 4.6283 | 4.6282 | 0.81915 |
| 7/5–11/8 | C6 | 0.17849 | 4.6283, 4.6058, 4.5884, 4.5762, 4.5690, 4.5668, 4.5697 | 4.5668 | 0.81516 |
| 11/8–27/20 | C6 | 0.18120 | 4.5697, 4.5727, 4.5812, 4.5954, 4.6150, 4.6402, 4.6708 | 4.5696 | 0.82806 |
| 27/20–13/10 | C6 | 0.18342 | 4.6708, 4.7375, 4.8303, 4.9490, 5.0939, 5.2653, 5.4638 | 4.6708 | 0.85676 |
| 13/10–6/5 | C6 | 0.17682 | 5.4638, 5.9376, 6.5656, 7.3547, 8.3174, 9.4694, 10.824 | 5.4637 | 0.96613 |

Row S3 (weight S3), w_I ≥ 0.302:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–79/20 | S3 | 0.014648 | 21963, 21940, 21918, 21896, 21874, 21852, 21830, 21808, 21786, |  |  |
|  |  |  | 21764 | 21764 / 1055.3 | 0.30210 |
| 79/20–39/10 | S3 | 0.015185 | 21764, 21741, 21718, 21695, 21672, 21649, 21626, 21603, |  |  |
|  |  |  | 21580, 21557 | 21557 / 1057.9 | 0.30947 |
| 39/10–19/5 | S3 | 0.015749 | 21557, 21509, 21460, 21411, 21362, 21314, 21265, 21216, |  |  |
|  |  |  | 21167, 21118 | 21118 / 1063.3 | 0.31282 |
| 19/5–73/20 | S3 | 0.016962 | 21118, 21037, 20956, 20875, 20794, 20713, 20631, 20550, |  |  |
|  |  |  | 20469, 20388 | 20387 / 1072.2 | 0.32253 |
| 73/20–33/10 | S3 | 0.019021 | 20388, 20153, 19918, 19684, 19449, 19215, 18981, 18747, |  |  |
|  |  |  | 18514, 18282 | 18281 / 1098.4 | 0.31658 |
| 33/10–59/20 | S3 | 0.025271 | 18282, 17962, 17643, 17325, 17010, 16696, 16385, 16076, |  |  |
|  |  |  | 15769, 15466 | 15465 / 1135.2 | 0.34430 |
| 59/20–13/5 | S3 | 0.034476 | 15466, 15032, 14603, 14181, 13766, 13359, 12959, 12568, |  |  |
|  |  |  | 12186, 11813 | 11813 / 1189.2 | 0.34249 |
| 13/5–12/5 | S3 | 0.048479 | 11813, 11523, 11239, 10960, 10687, 10421, 10160, 9906.0, |  |  |
|  |  |  | 9658.3, 9417.2 | 9417.1 / 1232.4 | 0.37046 |
| 12/5–9/4 | S3 | 0.059779 | 9417.2, 9192.6, 8973.7, 8760.5, 8553.2, 8351.8, 8156.3, |  |  |
|  |  |  | 7966.8, 7783.4, 7606.0 | 7605.9 / 1273.5 | 0.35704 |
| 9/4–21/10 | S3 | 0.070449 | 7606.0, 7389.2, 7181.5, 6982.9, 6793.4, 6613.0, 6441.8, |  |  |
|  |  |  | 6279.7, 6126.7, 5982.6 | 5982.6 / 1325.0 | 0.31810 |
| 21/10–2 | S3 | 0.083494 | 5982.6, 5868.1, 5759.2, 5656.1, 5558.6, 5466.6, 5380.2, 5299.4, |  |  |
|  |  |  | 5223.9, 5153.9 | 5153.8 / 1366.9 | 0.31482 |
| 2–19/10 | S3 | 0.093750 | 5153.9, 5072.5, 4998.4, 4931.4, 4871.5, 4818.5, 4772.3, 4732.8, |  |  |
|  |  |  | 4699.9, 4673.3 | 4673.2 / 1416.7 | 0.30925 |
| 19/10–17/10 | S3 | 0.10540 | 4673.3, 4605.3, 4578.9, 4591.6, 4640.5, 4722.4, 4833.8, |  |  |
|  |  |  | 4971.4, 5131.2, 5309.6 | 4578.9 / 1549.5 | 0.31150 |
| 17/10–31/20 | S3 | 0.13311 | 5309.6, 5491.1, 5691.8, 5907.7, 6134.8, 6369.1, 6606.5, |  |  |
|  |  |  | 6843.1, 7075.2, 7299.2 | 5309.5 / 1692.8 | 0.41752 |
| 31/20–7/5 | S3 | 0.15676 | 7299.2, 7599.0, 7884.3, 8146.8, 8378.6, 8573.0, 8724.1, |  |  |
|  |  |  | 8827.7, 8881.0, 8882.8 | 7299.1 / 1898.1 | 0.60284 |
| 7/5–6/5 | S3 | 0.17682 | 8882.8, 8886.3, 8691.8, 8290.1, 7696.4, 6952.9, 6130.1, 5323.2, |  |  |
|  |  |  | 4643.4, 4201.0 | 4201.0 / 2347.5 | 0.31645 |

Row T2 (weight T2), w_I ≥ 0.19:

| piece | weight | η ≥ | Bernstein coefficients | least | product ≥ |
|---|---|---|---|---|---|
| 4–39/10 | T2 | 0.014648 | 13.563, 13.499, 13.435, 13.372, 13.309, 13.246, 13.183 | 13.183 | 0.19311 |
| 39/10–19/5 | T2 | 0.015749 | 13.183, 13.116, 13.048, 12.981, 12.914, 12.848, 12.782 | 12.781 | 0.20130 |
| 19/5–73/20 | T2 | 0.016962 | 12.782, 12.672, 12.563, 12.455, 12.348, 12.241, 12.136 | 12.135 | 0.20584 |
| 73/20–33/10 | T2 | 0.019021 | 12.136, 11.830, 11.532, 11.240, 10.954, 10.675, 10.402 | 10.401 | 0.19784 |
| 33/10–59/20 | T2 | 0.025271 | 10.402, 10.026, 9.6620, 9.3101, 8.9700, 8.6415, 8.3245 | 8.3244 | 0.21037 |
| 59/20–13/5 | T2 | 0.034476 | 8.3245, 7.8709, 7.4408, 7.0335, 6.6485, 6.2853, 5.9430 | 5.9430 | 0.20489 |
| 13/5–12/5 | T2 | 0.048479 | 5.9430, 5.6769, 5.4234, 5.1824, 4.9534, 4.7362, 4.5304 | 4.5304 | 0.21963 |
| 12/5–9/4 | T2 | 0.059779 | 4.5304, 4.3388, 4.1570, 3.9848, 3.8220, 3.6682, 3.5232 | 3.5232 | 0.21061 |
| 9/4–11/5 | T2 | 0.070449 | 3.5232, 3.4681, 3.4143, 3.3618, 3.3105, 3.2603, 3.2114 | 3.2114 | 0.22624 |
| 11/5–21/10 | T2 | 0.074510 | 3.2114, 3.1029, 3.0002, 2.9032, 2.8118, 2.7257, 2.6447 | 2.6447 | 0.19706 |
| 21/10–41/20 | T2 | 0.083494 | 2.6447, 2.5997, 2.5563, 2.5145, 2.4742, 2.4354, 2.3980 | 2.3980 | 0.20022 |
| 41/20–2 | T2 | 0.088454 | 2.3980, 2.3579, 2.3194, 2.2826, 2.2474, 2.2138, 2.1817 | 2.1816 | 0.19298 |
| 2–79/40 | T2 | 0.093750 | 2.1817, 2.1647, 2.1482, 2.1321, 2.1164, 2.1012, 2.0863 | 2.0863 | 0.19559 |
| 79/40–39/20 | T2 | 0.096528 | 2.0863, 2.0709, 2.0559, 2.0413, 2.0272, 2.0135, 2.0002 | 2.0002 | 0.19307 |
| 39/20–77/40 | T2 | 0.099396 | 2.0002, 1.9864, 1.9730, 1.9601, 1.9476, 1.9356, 1.9239 | 1.9239 | 0.19123 |
| 77/40–19/10 | T2 | 0.10235 | 1.9239, 1.9118, 1.9002, 1.8890, 1.8782, 1.8679, 1.8580 | 1.8580 | 0.19017 |
| 19/10–15/8 | T2 | 0.10540 | 1.8580, 1.8477, 1.8379, 1.8285, 1.8195, 1.8110, 1.8029 | 1.8028 | 0.19003 |
| 15/8–37/20 | T2 | 0.10855 | 1.8029, 1.7945, 1.7865, 1.7790, 1.7719, 1.7653, 1.7590 | 1.7590 | 0.19094 |
| 37/20–9/5 | T2 | 0.11179 | 1.7590, 1.7458, 1.7344, 1.7249, 1.7171, 1.7109, 1.7062 | 1.7062 | 0.19074 |
| 9/5–17/10 | T2 | 0.11854 | 1.7062, 1.6957, 1.6931, 1.6974, 1.7077, 1.7230, 1.7424 | 1.6930 | 0.20070 |
| 17/10–31/20 | T2 | 0.13311 | 1.7424, 1.7789, 1.8301, 1.8899, 1.9535, 2.0163, 2.0750 | 1.7424 | 0.23193 |
| 31/20–7/5 | T2 | 0.15676 | 2.0750, 2.1536, 2.2248, 2.2802, 2.3144, 2.3247, 2.3109 | 2.0750 | 0.32528 |
| 7/5–6/5 | T2 | 0.17682 | 2.3109, 2.2838, 2.1644, 1.9515, 1.6818, 1.4180, 1.2074 | 1.2074 | 0.21350 |

Row S4 (c_0, …, c_3 of [[sec:tb-morawetz-weights]]), w_I ≥ 0.515. On each piece, k_S ≥ the least over
j ≤ 3 of (least Bernstein coefficient of c_j)/(16 C(3, j)H_0^(3−j)), with H_0 = 21 + 6y at the right end of the piece.

| piece | c_j | Bernstein coefficients | least |
|---|---|---|---|
| 4–79/20 | c_0 | 5558094, 5553538, 5548980, 5544421, 5539860, 5535297, 5530733, 5526168, 5521601, 5517032 | 5517032 |
|  | c_1 | 1032700, 1031816, 1030931, 1030047, 1029161, 1028276, 1027390, 1026503, 1025617 | 1025616 |
|  | c_2 | 71767, 71702, 71637, 71572, 71506, 71441, 71376, 71310 | 71310 |
|  | c_3 | 2210.5, 2208.3, 2206.1, 2204.0, 2201.8, 2199.6, 2197.4 | 2197.4 |
| 79/20–39/10 | c_0 | 5517032, 5512287, 5507540, 5502792, 5498042, 5493290, 5488537, 5483783, 5479027, |  |
|  |  | 5474270 | 5474269 |
|  | c_1 | 1025617, 1024696, 1023774, 1022853, 1021931, 1021008, 1020085, 1019162, 1018239 | 1018238 |
|  | c_2 | 71310, 71243, 71175, 71107, 71039, 70971, 70903, 70834 | 70834 |
|  | c_3 | 2197.4, 2195.1, 2192.9, 2190.6, 2188.3, 2186.1, 2183.8 | 2183.8 |
| 39/10–19/5 | c_0 | 5474270, 5464185, 5454095, 5443998, 5433896, 5423787, 5413673, 5403553, 5393429, 5383299 | 5383298 |
|  | c_1 | 1018239, 1016281, 1014322, 1012362, 1010400, 1008437, 1006472, 1004506, 1002539 | 1002539 |
|  | c_2 | 70834, 70690, 70546, 70401, 70256, 70111, 69966, 69821 | 69821 |
|  | c_3 | 2183.8, 2179.0, 2174.2, 2169.3, 2164.5, 2159.7, 2154.8 | 2154.8 |
| 19/5–73/20 | c_0 | 5383299, 5366515, 5349717, 5332906, 5316083, 5299249, 5282405, 5265551, 5248689, 5231819 | 5231818 |
|  | c_1 | 1002539, 999280, 996017, 992751, 989482, 986210, 982936, 979659, 976380 | 976379 |
|  | c_2 | 69821, 69581, 69340, 69099, 68857, 68616, 68374, 68131 | 68131 |
|  | c_3 | 2154.8, 2146.8, 2138.7, 2130.7, 2122.6, 2114.5, 2106.4 | 2106.4 |
| 73/20–33/10 | c_0 | 5231819, 5183126, 5134369, 5085567, 5036740, 4987908, 4939088, 4890299, 4841559, |  |
|  |  | 4792884 | 4792884 |
|  | c_1 | 976380, 966916, 957433, 947936, 938431, 928920, 919410, 909903, 900403 | 900403 |
|  | c_2 | 68131, 67432, 66731, 66029, 65325, 64620, 63916, 63211 | 63210 |
|  | c_3 | 2106.4, 2083.1, 2059.6, 2036.0, 2012.4, 1988.7, 1965.0 | 1965.0 |
| 33/10–59/20 | c_0 | 4792884, 4725874, 4658989, 4592272, 4525768, 4459516, 4393558, 4327929, 4262667, |  |
|  |  | 4197807 | 4197806 |
|  | c_1 | 900403, 887326, 874263, 861225, 848222, 835264, 822359, 809516, 796743 | 796743 |
|  | c_2 | 63211, 62240, 61269, 60300, 59332, 58367, 57405, 56447 | 56446 |
|  | c_3 | 1965.0, 1932.4, 1899.7, 1867.0, 1834.3, 1801.7, 1769.1 | 1769.0 |
| 59/20–13/5 | c_0 | 4197807, 4105022, 4013058, 3922016, 3831989, 3743066, 3655328, 3568849, 3483699, 3399939 | 3399939 |
|  | c_1 | 796743, 778472, 760344, 742383, 724611, 707048, 689713, 672621, 655789 | 655788 |
|  | c_2 | 56447, 55077, 53716, 52365, 51027, 49703, 48396, 47106 | 47106 |
|  | c_3 | 1769.1, 1722.5, 1676.1, 1629.9, 1584.1, 1538.7, 1493.8 | 1493.8 |
| 13/5–9/4 | c_0 | 3399939, 3274116, 3151432, 3032099, 2916301, 2804192, 2695898, 2591520, 2491133, 2394790 | 2394790 |
|  | c_1 | 655789, 630503, 605801, 581734, 558345, 535670, 513735, 492562, 472168 | 472167 |
|  | c_2 | 47106, 45168, 43271, 41417, 39612, 37860, 36161, 34519 | 34519 |
|  | c_3 | 1493.8, 1426.4, 1360.1, 1295.1, 1231.7, 1170.0, 1110.1 | 1110.1 |
| 9/4–19/10 | c_0 | 2394790, 2240420, 2096433, 1963048, 1840328, 1728202, 1626477, 1534854, 1452943, 1380280 | 1380280 |
|  | c_1 | 472168, 439490, 408809, 380189, 353654, 329193, 306768, 286316, 267755 | 267755 |
|  | c_2 | 34519, 31888, 29402, 27069, 24893, 22875, 21012, 19300 | 19299 |
|  | c_3 | 1110.1, 1014.2, 922.95, 836.94, 756.45, 681.65, 612.57 | 612.57 |
| 19/10–17/10 | c_0 | 1380280, 1317185, 1261064, 1211612, 1168484, 1131298, 1099646, 1073101, 1051220, |  |
|  |  | 1033559 | 1033558 |
|  | c_1 | 267755, 251638, 236947, 223629, 211619, 200846, 191233, 182696, 175155 | 175154 |
|  | c_2 | 19300, 17814, 16442, 15181, 14029, 12980, 12029, 11171 | 11170 |
|  | c_3 | 612.57, 552.59, 496.93, 445.61, 398.61, 355.83, 317.17 | 317.16 |
| 17/10–31/20 | c_0 | 1033559, 1015590, 1001987, 992282, 985995, 982654, 981791, 982956, 985720, 989681 | 981791 |
|  | c_1 | 175155, 167482, 160838, 155137, 150289, 146206, 142801, 139994, 137710 | 137710 |
|  | c_2 | 11171, 10298, 9521.3, 8835.4, 8234.2, 7711.8, 7262.6, 6881.2 | 6881.2 |
|  | c_3 | 317.17, 277.83, 242.75, 211.82, 184.88, 161.77, 142.32 | 142.31 |
| 31/20–7/5 | c_0 | 989681, 994982, 1002428, 1011058, 1019999, 1028493, 1035919, 1041808, 1045862, 1047957 | 989680 |
|  | c_1 | 137710, 134653, 132532, 131167, 130396, 130086, 130134, 130471, 131066 | 130086 |
|  | c_2 | 6881.2, 6370.7, 5981.7, 5701.5, 5518.5, 5423.4, 5409.1, 5471.4 | 5409.0 |
|  | c_3 | 142.32, 116.29, 96.813, 83.495, 75.920, 73.711, 76.547 | 73.710 |
| 7/5–6/5 | c_0 | 1047957, 1052063, 1048638, 1036747, 1018054, 997045, 980942, 979214, 1002550, 1061195 | 979213 |
|  | c_1 | 131066, 132234, 134396, 137319, 141311, 147270, 156607, 171027, 192110 | 131066 |
|  | c_2 | 5471.4, 5593.5, 6010.0, 6688.7, 7636.7, 8905.6, 10577, 12723 | 5471.3 |
|  | c_3 | 76.547, 82.109, 107.07, 149.01, 206.36, 278.92, 366.72 | 76.547 |

| piece | η ≥ | k_S ≥ | product ≥ |
|---|---|---|---|
| 4–79/20 | 0.014648 | 35.260 | 0.51650 |
| 79/20–39/10 | 0.015185 | 34.938 | 0.53057 |
| 39/10–19/5 | 0.015749 | 34.256 | 0.53952 |
| 19/5–73/20 | 0.016962 | 33.130 | 0.56196 |
| 73/20–33/10 | 0.019021 | 29.927 | 0.56926 |
| 33/10–59/20 | 0.025271 | 25.713 | 0.64980 |
| 59/20–13/5 | 0.034476 | 20.265 | 0.69868 |
| 13/5–9/4 | 0.048479 | 13.707 | 0.66452 |
| 9/4–19/10 | 0.070449 | 7.4122 | 0.52219 |
| 19/10–17/10 | 0.10540 | 5.2568 | 0.55411 |
| 17/10–31/20 | 0.13311 | 4.7297 | 0.62958 |
| 31/20–7/5 | 0.15676 | 4.4403 | 0.69609 |
| 7/5–6/5 | 0.17682 | 3.8395 | 0.67893 |

#### The constants m′ and M′ {#sec:tb-morawetz-constants}

For each multiplier, φ′ − q = η(4Θ_z − g) and φ′ − 2q = η(4Θ_z − 2g), with Θ_z at z = 1 − 2y. The first table
bounds η(4Θ_z − g) below on the pieces of I, the second bounds |η(4Θ_z − 2g)| above.

| multiplier | 4Θ_z − g in y: coefficients of y⁰, y¹, … | m′ ≥ | 4Θ_z − 2g | M′ ≤ |
|---|---|---|---|---|
| Θ_A | 17/5, 27/5, −42/5 | 0.0537 | 17/5, 27/5, −42/5 | 0.72 |
| Θ_B | 137/30, 38/5, −114/5, 32/3 | 0.0718 | 137/30, 38/5, −114/5, 32/3 | 0.735 |
| Θ_E | 0, 16, −16 | 0.0135 | 0, 16, −16 | 0.735 |
| Θ_C | 13/30, 92/3, −326/5, 544/15 | 0.0305 | 13/30, 92/3, −326/5, 544/15 | 0.735 |
| Θ_T | 28/5, 11/10, −72/5, 48/5 | 0.0814 | 28/5, 3/5, −72/5, 48/5 | 0.65 |

| multiplier | piece | η ≥ | Bernstein coefficients of 4Θ_z − g | least | product ≥ |
|---|---|---|---|---|---|
| Θ_A | 4–13/5 | 0.014648 | 3.7047, 3.8905, 4.0150 | 3.7046 | 0.054267 |
| Θ_A | 13/5–6/5 | 0.048479 | 4.0150, 4.8115, 3.0991 | 3.0990 | 0.15024 |
| Θ_B | 4–13/5 | 0.014648 | 4.9552, 5.0940, 5.1823, 5.2265 | 4.9552 | 0.072586 |
| Θ_B | 13/5–6/5 | 0.048479 | 5.2265, 5.5097, 3.9943, 2.4213 | 2.4213 | 0.11738 |
| Θ_E | 4–6/5 | 0.014648 | 0.93750, 5.3611, 3.3951 | 0.93750 | 0.013732 |
| Θ_C | 4–6/5 | 0.014648 | 2.1042, 6.9368, 3.9953, 2.4324 | 2.1041 | 0.030822 |
| Θ_T | 4–33/10 | 0.014648 | 5.6148, 5.6091, 5.5997, 5.5870 | 5.5870 | 0.081841 |
| Θ_T | 33/10–13/5 | 0.025271 | 5.5870, 5.5627, 5.5260, 5.4787 | 5.4786 | 0.13845 |
| Θ_T | 13/5–6/5 | 0.048479 | 5.4787, 5.0178, 3.5473, 2.6345 | 2.6344 | 0.12771 |

| multiplier | piece | η ≤ | Bernstein coefficients of 4Θ_z − 2g | greatest modulus | product ≤ |
|---|---|---|---|---|---|
| Θ_A | 4–13/5 | 0.048480 | 3.7047, 3.8905, 4.0150 | 4.0150 | 0.19465 |
| Θ_A | 13/5–19/10 | 0.10541 | 4.0150, 4.2031, 4.2513 | 4.2513 | 0.44812 |
| Θ_A | 19/10–31/20 | 0.15677 | 4.2513, 4.3032, 4.1924 | 4.3033 | 0.67459 |
| Θ_A | 31/20–3/2 | 0.16461 | 4.1924, 4.1699, 4.1407 | 4.1924 | 0.69011 |
| Θ_A | 3/2–29/20 | 0.17201 | 4.1407, 4.1085, 4.0681 | 4.1408 | 0.71223 |
| Θ_A | 29/20–57/40 | 0.17540 | 4.0681, 4.0463, 4.0221 | 4.0682 | 0.71355 |
| Θ_A | 57/40–7/5 | 0.17850 | 4.0221, 3.9967, 3.9685 | 4.0222 | 0.71795 |
| Θ_A | 7/5–11/8 | 0.18121 | 3.9685, 3.9388, 3.9062 | 3.9686 | 0.71914 |
| Θ_A | 11/8–27/20 | 0.18343 | 3.9062, 3.8717, 3.8340 | 3.9062 | 0.71651 |
| Θ_A | 27/20–13/10 | 0.18584 | 3.8340, 3.7519, 3.6542 | 3.8340 | 0.71250 |
| Θ_A | 13/10–6/5 | 0.18591 | 3.6542, 3.4210, 3.0991 | 3.6542 | 0.67936 |
| Θ_B | 4–13/5 | 0.048480 | 4.9552, 5.0940, 5.1823, 5.2265 | 5.2266 | 0.25338 |
| Θ_B | 13/5–19/10 | 0.10541 | 5.2265, 5.2934, 5.2600, 5.1491 | 5.2935 | 0.55797 |
| Θ_B | 19/10–17/10 | 0.13312 | 5.1491, 5.0899, 5.0085, 4.9085 | 5.1492 | 0.68542 |
| Θ_B | 17/10–8/5 | 0.14878 | 4.9085, 4.8438, 4.7714, 4.6922 | 4.9085 | 0.73026 |
| Θ_B | 8/5–63/40 | 0.15278 | 4.6922, 4.6700, 4.6472, 4.6240 | 4.6922 | 0.71684 |
| Θ_B | 63/40–31/20 | 0.15677 | 4.6240, 4.5996, 4.5746, 4.5491 | 4.6240 | 0.72488 |
| Θ_B | 31/20–61/40 | 0.16073 | 4.5491, 4.5224, 4.4950, 4.4671 | 4.5492 | 0.73114 |
| Θ_B | 61/40–121/80 | 0.16268 | 4.4671, 4.4526, 4.4379, 4.4231 | 4.4671 | 0.72669 |
| Θ_B | 121/80–3/2 | 0.16461 | 4.4231, 4.4080, 4.3927, 4.3772 | 4.4232 | 0.72809 |
| Θ_B | 3/2–119/80 | 0.16652 | 4.3772, 4.3613, 4.3453, 4.3291 | 4.3772 | 0.72887 |
| Θ_B | 119/80–59/40 | 0.16839 | 4.3291, 4.3125, 4.2957, 4.2788 | 4.3292 | 0.72897 |
| Θ_B | 59/40–117/80 | 0.17022 | 4.2788, 4.2615, 4.2439, 4.2263 | 4.2789 | 0.72834 |
| Θ_B | 117/80–29/20 | 0.17201 | 4.2263, 4.2081, 4.1898, 4.1713 | 4.2263 | 0.72694 |
| Θ_B | 29/20–57/40 | 0.17540 | 4.1713, 4.1329, 4.0937, 4.0539 | 4.1714 | 0.73165 |
| Θ_B | 57/40–7/5 | 0.17850 | 4.0539, 4.0119, 3.9692, 3.9258 | 4.0540 | 0.72361 |
| Θ_B | 7/5–6/5 | 0.18591 | 3.9258, 3.4753, 2.9516, 2.4213 | 3.9259 | 0.72986 |
| Θ_E | 4–13/5 | 0.048480 | 0.93750, 1.5355, 2.0167 | 2.0168 | 0.097770 |
| Θ_E | 13/5–19/10 | 0.10541 | 2.0167, 2.7439, 3.2044 | 3.2044 | 0.33777 |
| Θ_E | 19/10–31/20 | 0.15677 | 3.2044, 3.7011, 3.8877 | 3.8878 | 0.60946 |
| Θ_E | 31/20–7/5 | 0.17850 | 3.8877, 4.0137, 3.9983 | 4.0137 | 0.71643 |
| Θ_E | 7/5–27/20 | 0.18343 | 3.9983, 3.9920, 3.9621 | 3.9984 | 0.73341 |
| Θ_E | 27/20–53/40 | 0.18503 | 3.9621, 3.9458, 3.9225 | 3.9621 | 0.73308 |
| Θ_E | 53/40–13/10 | 0.18584 | 3.9225, 3.8979, 3.8654 | 3.9225 | 0.72895 |
| Θ_E | 13/10–6/5 | 0.18591 | 3.8654, 3.7147, 3.3951 | 3.8655 | 0.71862 |
| Θ_C | 4–13/5 | 0.048480 | 2.1042, 2.7575, 3.2687, 3.6605 | 3.6605 | 0.17746 |
| Θ_C | 13/5–19/10 | 0.10541 | 3.6605, 4.2524, 4.5716, 4.6961 | 4.6962 | 0.49501 |
| Θ_C | 19/10–17/10 | 0.13312 | 4.6961, 4.7627, 4.7736, 4.7407 | 4.7736 | 0.63542 |
| Θ_C | 17/10–8/5 | 0.14878 | 4.7407, 4.7195, 4.6800, 4.6254 | 4.7408 | 0.70530 |
| Θ_C | 8/5–31/20 | 0.15677 | 4.6254, 4.5941, 4.5578, 4.5172 | 4.6255 | 0.72510 |
| Θ_C | 31/20–61/40 | 0.16073 | 4.5172, 4.4954, 4.4723, 4.4480 | 4.5172 | 0.72601 |
| Θ_C | 61/40–3/2 | 0.16461 | 4.4480, 4.4225, 4.3958, 4.3679 | 4.4481 | 0.73219 |
| Θ_C | 3/2–119/80 | 0.16652 | 4.3679, 4.3534, 4.3385, 4.3234 | 4.3679 | 0.72732 |
| Θ_C | 119/80–59/40 | 0.16839 | 4.3234, 4.3079, 4.2921, 4.2760 | 4.3235 | 0.72802 |
| Θ_C | 59/40–117/80 | 0.17022 | 4.2760, 4.2595, 4.2426, 4.2255 | 4.2761 | 0.72786 |
| Θ_C | 117/80–29/20 | 0.17201 | 4.2255, 4.2079, 4.1900, 4.1718 | 4.2255 | 0.72681 |
| Θ_C | 29/20–57/40 | 0.17540 | 4.1718, 4.1340, 4.0949, 4.0547 | 4.1719 | 0.73174 |
| Θ_C | 57/40–7/5 | 0.17850 | 4.0547, 4.0123, 3.9687, 3.9241 | 4.0547 | 0.72375 |
| Θ_C | 7/5–6/5 | 0.18591 | 3.9241, 3.4609, 2.8880, 2.4324 | 3.9241 | 0.72953 |
| Θ_T | 4–13/5 | 0.048480 | 5.5836, 5.5526, 5.4910, 5.4047 | 5.5836 | 0.27069 |
| Θ_T | 13/5–19/10 | 0.10541 | 5.4047, 5.2743, 5.0877, 4.8653 | 5.4048 | 0.56970 |
| Θ_T | 19/10–17/10 | 0.13312 | 4.8653, 4.7464, 4.6173, 4.4812 | 4.8653 | 0.64763 |
| Θ_T | 17/10–33/20 | 0.14085 | 4.4812, 4.4392, 4.3966, 4.3533 | 4.4813 | 0.63116 |
| Θ_T | 33/20–8/5 | 0.14878 | 4.3533, 4.3060, 4.2579, 4.2093 | 4.3534 | 0.64766 |
| Θ_T | 8/5–63/40 | 0.15278 | 4.2093, 4.1833, 4.1570, 4.1307 | 4.2094 | 0.64307 |
| Θ_T | 63/40–31/20 | 0.15677 | 4.1307, 4.1030, 4.0752, 4.0472 | 4.1307 | 0.64754 |
| Θ_T | 31/20–123/80 | 0.15875 | 4.0472, 4.0327, 4.0182, 4.0036 | 4.0473 | 0.64249 |
| Θ_T | 123/80–61/40 | 0.16073 | 4.0036, 3.9887, 3.9738, 3.9588 | 4.0037 | 0.64347 |
| Θ_T | 61/40–121/80 | 0.16268 | 3.9588, 3.9434, 3.9280, 3.9126 | 3.9588 | 0.64400 |
| Θ_T | 121/80–3/2 | 0.16461 | 3.9126, 3.8967, 3.8809, 3.8650 | 3.9126 | 0.64405 |
| Θ_T | 3/2–119/80 | 0.16652 | 3.8650, 3.8487, 3.8324, 3.8161 | 3.8651 | 0.64359 |
| Θ_T | 119/80–59/40 | 0.16839 | 3.8161, 3.7993, 3.7826, 3.7658 | 3.8161 | 0.64259 |
| Θ_T | 59/40–29/20 | 0.17201 | 3.7658, 3.7308, 3.6958, 3.6607 | 3.7658 | 0.64773 |
| Θ_T | 29/20–57/40 | 0.17540 | 3.6607, 3.6238, 3.5868, 3.5498 | 3.6608 | 0.64209 |
| Θ_T | 57/40–7/5 | 0.17850 | 3.5498, 3.5107, 3.4717, 3.4327 | 3.5498 | 0.63363 |
| Θ_T | 7/5–6/5 | 0.18591 | 3.4327, 3.0275, 2.6257, 2.2872 | 3.4327 | 0.63817 |

#### Monotonicity of the multipliers {#sec:tb-morawetz-monotone}

Bernstein coefficients of Θ_z on subintervals of [−1, 1] in z, and, for Θ_T, of 4Θ_z(1 − 2y) − g(y) on [0, 1] in
y; every one is positive. The end values of the multipliers follow.

| polynomial | subinterval | Bernstein coefficients |
|---|---|---|
| Θ_z of Θ_A | [−1, 1] | 0.10000, 1.5250, 0.85000 |
| Θ_z of Θ_B | [−1, 1] | 0.0083333, 0.50833, 1.7750, 1.1417 |
| Θ_z of Θ_C | [−1, 0] | 0.54167, 0.16389, 0.69444, 1.0000 |
| Θ_z of Θ_C | [0, 1] | 1.0000, 1.3056, 1.3861, 0.10833 |
| Θ_z of Θ_T | [−1, 1] | 0.60000, 0.46667, 1.5333, 1.4000 |
| 4Θ_z − g of Θ_T | [0, 1] | 5.6000, 5.9667, 1.5333, 1.9000 |


| multiplier | Θ(1) | Θ(−1) | Θ(7/8) | Θ(−7/18) |
|---|---|---|---|---|
| Θ_A | 81/80 | −51/80 | 18459/20480 | −10213/29160 |
| Θ_B | 49/40 | −59/120 | 264383/245760 | −990157/3149280 |
| Θ_E | 2/3 | −2/3 | 1001/1536 | −6461/17496 |
| Θ_C | 19/20 | −3/5 | 74473/81920 | −985159/3149280 |
| Θ_T | 51/40 | −29/40 | 180061/163840 | −472633/1399680 |

#### Rows T1 and T3 {#sec:tb-morawetz-t1t3}

The numerators Π of rows T1 and T3 of [[prop:morawetz-master-potentials]]: Bernstein coefficients on the subintervals
of [0, 1] used there, and on the pieces of I, with the least coefficient divided, for T3, by D = 4(1 + 2y)⁴(5 + 6y)³
at the right end of the piece.

| row | interval | Bernstein coefficients | least |
|---|---|---|---|
| T1 | [0, 1/4] | 7.5000, 3.6875, 1.8333, 0.98958, 0.64128 | 0.64127 |
| T1 | [1/4, 1/2] | 0.64128, 0.29297, 0.44010, 0.56771, 0.59375 | 0.29296 |
| T1 | [1/2, 3/4] | 0.59375, 0.61979, 0.54427, 0.28516, 0.19336 | 0.19335 |
| T1 | [3/4, 1] | 0.19336, 0.10156, 0.17708, 0.77083, 2.6667 | 0.10156 |
| T3 | [0, 1/2] | 8750.0, 6550.0, 4151.9, 1931.5, 410.17, 228.68, 2082.3, 6600.7, 14142, 24465, 36298, 47113, |  |
|  |  | 54400 | 228.68 |
| T3 | [1/2, 3/4] | 54400, 58043, 60804, 62370, 62426, 60701, 57028, 51440, 44316, 36592, 30068, 27839, 34910 | 27838 |
| T3 | [3/4, 1] | 34910, 41981, 58352, 89029, 140926, 223481, 349445, 535900, 805571, 1188495, 1724163, |  |
|  |  | 2464250, 3476088 | 34909 |

| row | piece | η ≥ | Bernstein coefficients | least (over D) | product ≥ |
|---|---|---|---|---|---|
| T1 | 4–16/5 | 0.014648 | 4.3643, 4.0107, 3.6869, 3.3908, 3.1200 | 3.1199 | 0.045702 |
| T1 | 16/5–13/5 | 0.027537 | 3.1200, 2.7327, 2.3974, 2.1076, 1.8579 | 1.8578 | 0.051160 |
| T1 | 13/5–11/5 | 0.048479 | 1.8579, 1.5663, 1.3292, 1.1375, 0.98378 | 0.98377 | 0.047692 |
| T1 | 11/5–2 | 0.074510 | 0.98378, 0.87009, 0.77710, 0.70173, 0.64128 | 0.64127 | 0.047781 |
| T1 | 2–19/10 | 0.093750 | 0.64128, 0.60365, 0.57180, 0.54509, 0.52292 | 0.52291 | 0.049023 |
| T1 | 19/10–17/10 | 0.10540 | 0.52292, 0.46627, 0.43928, 0.43210, 0.43739 | 0.43209 | 0.045546 |
| T1 | 17/10–13/10 | 0.13311 | 0.43739, 0.45625, 0.63325, 0.63739, 0.54159 | 0.43739 | 0.058222 |
| T1 | 13/10–6/5 | 0.17682 | 0.54159, 0.50153, 0.44400, 0.37433, 0.31018 | 0.31018 | 0.054848 |
| T3 | 4–33/10 | 0.014648 | 5424.0, 5300.5, 5178.3, 5057.4, 4938.0, 4820.2, 4704.1, |  |  |
|  |  |  | 4589.7, 4477.3, 4366.9, 4258.6, 4152.5, 4048.8 | 4048.8 / 1343.0 | 0.044162 |
| T3 | 33/10–29/10 | 0.025271 | 4048.8, 3953.1, 3859.3, 3767.6, 3678.2, 3591.0, 3506.1, |  |  |
|  |  |  | 3423.7, 3343.9, 3266.7, 3192.2, 3120.6, 3051.9 | 3051.8 / 1751.4 | 0.044037 |
| T3 | 29/10–27/10 | 0.036126 | 3051.9, 3005.5, 2960.5, 2916.8, 2874.5, 2833.6, 2794.1, |  |  |
|  |  |  | 2756.2, 2719.7, 2684.7, 2651.3, 2619.5, 2589.3 | 2589.3 / 2082.9 | 0.044910 |
| T3 | 27/10–13/5 | 0.043836 | 2589.3, 2571.5, 2554.3, 2537.7, 2521.6, 2506.1, 2491.1, |  |  |
|  |  |  | 2476.8, 2463.1, 2449.9, 2437.4, 2425.4, 2414.1 | 2414.1 / 2302.0 | 0.045971 |
| T3 | 13/5–5/2 | 0.048479 | 2414.1, 2401.4, 2389.5, 2378.3, 2368.0, 2358.5, 2349.7, |  |  |
|  |  |  | 2341.8, 2334.7, 2328.4, 2323.0, 2318.4, 2314.7 | 2314.7 / 2571.0 | 0.043647 |
| T3 | 5/2–12/5 | 0.053760 | 2314.7, 2310.5, 2307.4, 2305.5, 2304.6, 2304.8, 2306.2, |  |  |
|  |  |  | 2308.7, 2312.4, 2317.2, 2323.3, 2330.5, 2338.9 | 2304.5 / 2906.0 | 0.042634 |
| T3 | 12/5–23/10 | 0.059779 | 2338.9, 2348.4, 2359.5, 2372.2, 2386.4, 2402.2, 2419.6, |  |  |
|  |  |  | 2438.7, 2459.3, 2481.7, 2505.7, 2531.4, 2558.7 | 2338.8 / 3329.9 | 0.041989 |
| T3 | 23/10–11/5 | 0.066652 | 2558.7, 2589.9, 2623.4, 2659.0, 2696.9, 2737.0, 2779.5, |  |  |
|  |  |  | 2824.2, 2871.3, 2920.8, 2972.6, 3026.8, 3083.5 | 2558.7 / 3876.1 | 0.044000 |
| T3 | 11/5–2 | 0.074510 | 3083.5, 3223.3, 3377.8, 3547.3, 3732.2, 3932.6, 4148.8, 4381.1, |  |  |
|  |  |  | 4629.7, 4894.8, 5176.7, 5475.3, 5791.1 | 3083.4 / 5561.2 | 0.041313 |
| T3 | 2–17/10 | 0.093750 | 5791.1, 6489.8, 7271.9, 8139.0, 9092.4, 10133, 11260, 12473, |  |  |
|  |  |  | 13771, 15151, 16610, 18145, 19749 | 5791.0 / 11617 | 0.046734 |
| T3 | 17/10–13/10 | 0.13311 | 19749, 23855, 28419, 33356, 38537, 43787, 48878, 53529, |  |  |
|  |  |  | 57423, 60218, 61600, 61349, 59473 | 19749 / 56828 | 0.046259 |
| T3 | 13/10–6/5 | 0.17682 | 59473, 58689, 57620, 56268, 54640, 52751, 50627, 48307, 45845, |  |  |
|  |  |  | 43312, 40800, 38428, 36343 | 36342 / 100341 | 0.064044 |


### Tables for the resolvent bound on the band {#sec:tb2}

These tables carry the numbers used by [[prop:band-polynomial]], [[thm:band]] and [[prop:band-points]]. The notation
is that of [[sec:band]]: y = 1/r², z = 1 − 2y, v := 1/r = y^(1/2), η = (1 − y)y^(3/2) = (1 − v²)v³,
I = {1/4 ≤ v ≤ 5/6} = {−7/18 ≤ z ≤ 7/8}, κ = l(l + 2) and a = κ + 3/4. The Bernstein coefficients of a polynomial p
on a piece are the numbers b_0, …, b_n of [[lem:bernstein-lower-bound]], with that piece as the interval there and n
the degree of p.

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

(c) In the proof of [[thm:i-b-1-3]] (3) ([[sec:i-b-8-4]]), let C be the largest of the constants of the display
[[eq:i-b-8-chain]] before absorption in the proof of [[prop:i-b-8-1]], in its parts (a)–(c) (with δ = 0 in (b) and
(c)), h_c the least of their thresholds, C_K the constant of the absorption step [[eq:i-b-8-absorb]] there, h_1 as in
(b), and C_0 := h_1⁻¹(1 − ν′²)^(−1/2), where ν′ ∈ (0, 1) is the constant of [[thm:i-b-1-3]] (2) used in
[[sec:i-b-8-4]]. Then for Im σ ≥ 0 and |σ| ≥ C_0, with h = h(σ) and z = hσ as in [[sec:i-b-8-4]], ‖·‖_𝐨 and ‖·‖_(𝐨′)
the semiclassical norms at that h, and δ ∈ [0, 1] the loss of [[eq:i-b-8-1]] at z,

    ‖u‖_𝐨 ≤ 2C(1 − ν′²)^(−(1−δ)/2) |σ|^(−1+δ) ‖P̂(σ)u‖_(𝐨′).                                 {#eq:rb-high-energy}

*Proof.* (a) For h < min(h_a, (2C_a)^(−1/M)), C_a h^M ≤ ½, so the last term is at most ‖u‖/2 and moves to the left.
(b) For h < h_1, Ch^M ≤ ¼ and CC_K h ≤ ¼, so the last two terms are at most ‖u‖_𝐨/2. (c) h_1 ≤ (4C)^(−1/M) ≤ 1, so
C_0 ≥ (1 − ν′²)^(−1/2) ≥ 1. If Im σ < ν′|σ|, then h = |Re σ|⁻¹ and |Re σ|² = |σ|² − (Im σ)² > |σ|²(1 − ν′²), so
h < (1 − ν′²)^(−1/2)|σ|⁻¹ ≤ h_1; (b) and P_(h,z) = h²P̂(σ) give ‖u‖_𝐨 ≤ 2Ch^(1−δ)‖P̂(σ)u‖_(𝐨′), and
h^(1−δ) ≤ (1 − ν′²)^(−(1−δ)/2)|σ|^(−(1−δ)). Otherwise h = |σ|⁻¹ ≤ C_0⁻¹ < h_1 (as ν′ > 0) and δ = 0, so
‖u‖_𝐨 ≤ 2C|σ|⁻¹‖P̂(σ)u‖_(𝐨′), and |σ|⁻¹ ≤ |σ|^(−1+δ) ≤ (1 − ν′²)^(−(1−δ)/2)|σ|^(−1+δ) as |σ| ≥ 1. ∎

The assumptions C_a ≥ ½ and C ≥ ¼ cost nothing, as enlarging a constant keeps an estimate true. The thresholds h_a and
h_c are those of the chains of estimates [[eq:i-b-6-apriori]] and [[eq:i-b-8-chain]] in the proofs of [[prop:i-b-6-7]]
(a) and [[prop:i-b-8-1]], which contain the threshold of [[eq:i-b-6-6]]. The bound [[eq:rb-high-energy]] is uniform
in σ in the semiclassical norms at h = h(σ); at each fixed h these are equivalent to the norms of 𝒳_σ and 𝒴_σ
([[sec:i-b-8-4]]), with constants that depend on h.

**Lemma {#lem:rb-interpolation}** (The constant of the interpolation.) In [[prop:i-b-6-7]], let h_0 ≤ 1, put
κ_Γ := β′ − β, and let C′_a be such that ‖P̂′(σ)⁻¹‖_(L²→L²) ≤ C′_a for Re σ ≥ h_0⁻¹ (Re σ ≤ −h_0⁻¹ when z_0 = −1)
and Im σ ∈ [β, β′], and ‖P̂′(σ)⁻¹‖ ≤ C′_a|σ|⁻¹ there on Im σ = β′. Such a C′_a is given by the a priori estimate
[[eq:i-b-6-apriori]] in the proof of [[prop:i-b-6-7]] once its last term is absorbed, read at h = |Re σ|⁻¹ (part (c)
of that proof). Put

    F_Γ := sup_(σ_0 ≥ h_0⁻¹) exp(3 log σ_0 · e^(−πσ_0/(2κ_Γ))).

Then [[eq:i-b-6-11]] holds with the constant 4F_ΓC′_a: for h ≤ h_0/2 and z ∈ z_0 + i[hβ, hβ′],
‖(P′_(h,z))⁻¹‖ ≤ 4F_ΓC′_a h^(−1−(β′−Im(z/h))/κ_Γ). If κ_Γ = 2^(−3/2), then F_Γ ≤ 1.002659.

*Proof.* Let z_0 = 1; for z_0 = −1 the same argument runs with Re σ ≤ −h_0⁻¹ and the rectangle reflected in the
imaginary axis. Let σ_0 ≥ h_0⁻¹, so σ_0 ≥ 1, and w ∈ L². Apply [[lem:i-b-6-6]] to F(ζ) := P̂′(3σ_0 + iβ + κ_Γζ)⁻¹w on
the rectangle [−L, L] + i[0, 1], L := 2σ_0/κ_Γ, where Re σ ∈ [σ_0, 5σ_0] and Im σ ∈ [β, β′]. F is holomorphic near the
rectangle. Indeed, P̂′(σ) is entire in σ (the sentence after [[eq:i-b-6-10]]) as a family of bounded operators from
H^(2,0) into L², where H^(2,0) is the scattering Sobolev space of [[sec:i-a-2-2]], which is the space H_h^((2,0,0)) of
[[prop:i-b-6-7]] at each fixed h, with an equivalent norm ([[sec:i-b-2-3]]). On the compact set 𝒦 of the σ above, where the bound C′_a holds, P̂′(σ) is invertible from H^(2,0) onto L², with inverse
bounded from L² into H^(2,0) by the open mapping theorem. For σ_1 ∈ 𝒦 put 𝔗(σ) := P̂′(σ_1)⁻¹(P̂′(σ_1) − P̂′(σ)), a
holomorphic family of bounded operators on H^(2,0); its norm is at most ‖P̂′(σ_1)⁻¹‖‖P̂′(σ_1) − P̂′(σ)‖, less than ½
for σ near σ_1, P̂′ being continuous in norm. For such σ, P̂′(σ) = P̂′(σ_1)(I − 𝔗(σ)) is invertible and
P̂′(σ)⁻¹ = Σ_(n≥0) 𝔗(σ)ⁿP̂′(σ_1)⁻¹, a series of holomorphic functions that converges uniformly (its n-th term has norm
at most 2⁻ⁿ‖P̂′(σ_1)⁻¹‖), and a uniform limit of holomorphic functions is holomorphic. So σ ↦ P̂′(σ)⁻¹w is holomorphic
on a neighbourhood of 𝒦, and F near the rectangle.
There ‖F‖ ≤ A := C′_a‖w‖, and ‖F‖ ≤ A_0 := C′_a‖w‖ on Im ζ = 0 and ‖F‖ ≤ A_1 := C′_aσ_0⁻¹‖w‖ on Im ζ = 1, since
the modulus of σ is at least σ_0 there; A_1 ≤ A since σ_0 ≥ 1, and the Λ of [[lem:i-b-6-6]] is
Λ_0 := log(A/A_1) = log σ_0. With t := Im ζ = (Im σ − β)/κ_Γ ∈ [0, 1] and πL/4 = πσ_0/(2κ_Γ), the lemma gives, for
Re σ ∈ [2σ_0, 4σ_0],
‖P̂′(σ)⁻¹w‖ ≤ C′_a σ_0^(−t) exp(3Λ_0 e^(−πσ_0/(2κ_Γ)))‖w‖ ≤ F_Γ C′_a σ_0^(−t)‖w‖. There h = 1/Re σ ∈ [1/(4σ_0),
1/(2σ_0)], so σ_0^(−t) ≤ (4h)^t ≤ 4h^t, and (P′_(h,z))⁻¹ = h⁻²P̂′(z/h)⁻¹; as 2 − t = 1 + (β′ − Im(z/h))/κ_Γ, this is
the bound, and every h ≤ h_0/2 is 1/Re σ for some such σ_0. For the value: with c := π/(2κ_Γ) = √2π > 4.44288 and
s := σ_0 ≥ 1, the function g(s) := log s · e^(−cs) has g′(s) = e^(−cs)(1/s − c log s), and 1/s − c log s decreases,
so g attains its maximum on [1, ∞) at the point s_* where s_* log s_* = 1/c, with g(s_*) = e^(−cs_*)/(cs_*). As
s log s increases on [1, ∞) and 1.205 log 1.205 < 0.22471 < 0.22507 < 1/c, s_* > 1.205; so
cs_* > 4.44288 · 1.205 > 5.35367, and x ↦ e^(−x)/x decreases, so g(s_*) < e^(−5.35367)/5.35367 < 8.8365 · 10⁻⁴.
Hence F_Γ ≤ exp(3g(s_*)) ≤ exp(0.0026510) < 1.002659. ∎

At b_0 with m_0 = 1, q^Γ = 4 on Γ and ν_min = 2^(3/2) ([[thm:vi-a-6-1]]), so the function of (Γ.4) decreases at
exactly the rate 4 from its value sup_Γ λ_max(p_1^Γ) at 0, whatever the fibre inner product, and
γ_+ − γ_− = ν_min/8 = 2^(−3/2). For the choice β = γ_− + ϵ, β′ = γ_+ + ϵ of [[prop:i-b-6-7]], κ_Γ = 2^(−3/2), and
[[eq:i-b-6-11]] holds with the constant 4.01064 C′_a for every operator with principal symbol G Id at b_0, once h_0 ≤ 1
(4 · 1.002659 = 4.010636).

**Lemma {#lem:rb-gluing}** (Gluing through complex absorption.) Let 𝒳, 𝒴, 𝒵 be Banach spaces, P̂ : 𝒳 → 𝒴 bounded,
W : 𝒵 → 𝒵 and j : 𝒳 → 𝒵 linear, and k linear from W(𝒵) into 𝒴, such that Wj : 𝒳 → 𝒵 and kW : 𝒵 → 𝒴 are bounded.
Put Q := kWj and P_1 := P̂ − iQ, and suppose that P̂ and P_1 are invertible. With C_ext := ‖P_1⁻¹‖_(𝒴→𝒳) and C_D the
norm of jP̂⁻¹k on the subspace W(𝒵) of 𝒵 on which it is defined,

    ‖P̂⁻¹‖_(𝒴→𝒳) ≤ C_ext + C_ext²‖kWj‖ + C_ext²‖kW‖ C_D ‖Wj‖.

*Proof.* P_1⁻¹ − P̂⁻¹ = P_1⁻¹(P̂ − P_1)P̂⁻¹ = iP_1⁻¹QP̂⁻¹, and likewise P_1⁻¹ − P̂⁻¹ = iP̂⁻¹QP_1⁻¹. Inserting the second
into the first, P̂⁻¹ = P_1⁻¹ − iP_1⁻¹QP_1⁻¹ − P_1⁻¹(QP̂⁻¹Q)P_1⁻¹. For x ∈ 𝒳, v := Wjx lies in W(𝒵) and
QP̂⁻¹Qx = kW(jP̂⁻¹kv), so ‖QP̂⁻¹Qx‖ ≤ ‖kW‖C_D‖Wj‖‖x‖; and ‖Q‖ = ‖kWj‖. ∎

In the stability theory, at real σ ≠ 0, 𝒳 = 𝒳_σ, 𝒴 = 𝒴_σ, 𝒵 = 𝔏 of [[lem:rb-schur]], and j and k are multiplication
by a smooth cut-off χ supported in I × 𝕊³ with 0 ≤ χ ≤ 1; j is bounded from 𝒳_σ into 𝔏, as 𝒳_σ has positive
regularity. Let s be the regularity order of 𝒳_σ, so that 𝒴_σ has regularity order s − 1; on fields supported in the
compact set I × 𝕊³ ⊂ X°, the norm of 𝒴_σ is, up to constants, that of H^(s−1), and the norm of 𝔏 that of L².

When s − 1 ≤ 0, ‖·‖_(H^(s−1)) ≤ ‖·‖_(L²), so k is bounded from 𝔏 into 𝒴_σ, and W is a bounded operator on 𝔏, such as
multiplication by sgn(σ)q with q as in [[lem:rb-absorbed]], supported in the interior of I × 𝕊³, and χ = 1 on the
support of q. Then kWj is multiplication by sgn(σ)χ²q = ϵ_σq, so for P̂ = □̂(σ) the operator P_1 of [[lem:rb-gluing]] is
the operator □̂(σ) − iϵ_σQ of [[lem:rb-absorbed]]. Otherwise W is a smoothing operator on 𝔏 with values in fields smooth
on I × 𝕊³, for which kW is bounded.

For v ∈ W(𝒵), as χ = χ_Iχ, jP̂⁻¹kv = χ(χ_IP̂(σ)⁻¹χ_I)(χv), with χv supported in I × 𝕊³ and ‖χv‖_𝔏 ≤ ‖v‖_𝔏. The
cut-off bound of the preceding sections is C_D(σ) of [[lem:rb-schur]], the norm of χ_IP̂(σ)⁻¹χ_I on the dense subspace
𝒟 of smooth fields supported in I × 𝕊³. In the second case χv lies in 𝒟. In the first, χ_I is bounded from 𝔏 into 𝒴_σ
like k and from 𝒳_σ into 𝔏 like j, so χ_IP̂(σ)⁻¹χ_I is bounded on 𝔏, and its norm on 𝔏 equals its norm on the dense
subspace 𝒟. In both cases, as 0 ≤ χ ≤ 1, ‖jP̂⁻¹kv‖_𝔏 ≤ C_D(σ)‖χv‖_𝔏 ≤ C_D(σ)‖v‖_𝔏, so C_D ≤ C_D(σ). So, once the
cut-off bound is known, an inverse bound in the spaces of the stability theory needs only C_ext(σ), the inverse of the
absorbed problem, besides the norms of the fixed operators kWj, kW and Wj. Its estimate is the chain of Fredholm
estimates at the fixed σ with the absorbing term, and involves no trapping estimate and no mode stability; its
invertibility is a hypothesis of [[lem:rb-gluing]]. For the scalar wave the next lemma supplies it, with W
multiplication by sgn(σ)q. There every constant s ∈ (½, 1] is an admissible regularity order, as ϑ_ℋ = 0
([[lem:rb-scalar]]) and [[def:i-a-admissible]] and [[thm:i-b-1-3]] ask of the regularity order only that it be a
constant s > ½ + ϑ_ℋ; at such an order 𝒴_σ has regularity order s − 1 ≤ 0, and P̂ = □̂(σ) and P_1 are invertible by
[[lem:rb-scalar]] and [[lem:rb-absorbed]].

**Lemma {#lem:rb-absorbed}** (The absorbed scalar problem is invertible.) At b_0, let q ≥ 0 be a smooth radial function
(q = q(r)) with compact support in {r > r_h}, Q multiplication by q, σ real and nonzero and ϵ_σ := sgn σ. Then
□̂(σ) − iϵ_σQ : 𝒳_σ → 𝒴_σ is invertible.

*Proof.* Q maps 𝒳_σ into functions of class H^s (s > ½ + ϑ_ℋ the order of 𝒳_σ) supported in a fixed compact subset of
{r > r_h}, which embed compactly into 𝒴_σ, whose order there is s − 1 (Rellich's theorem). So □̂(σ) − iϵ_σQ is a compact
perturbation of □̂(σ), the spectral family of □ on functions, which is Fredholm of index 0 ([[lem:rb-scalar]], by
[[thm:i-a-7-2]] (3) and [[thm:i-b-1-3]] (3)); it suffices to show that its kernel is trivial. Let ω be in the kernel.
The perturbation −iϵ_σQ is of order zero with compact support in X°, so it changes neither the principal symbols nor
the structure at infinity nor the thresholds verified in the proof of [[lem:rb-scalar]], and [[thm:i-a-7-2]] (5)
applies to □̂(σ) − iϵ_σQ: ω ∈ 𝒜^(3/2−ε)(X̄) for every ε > 0. So, as in *The class* in the proof of
[[prop:iii-d-6-2]], ω is smooth across the future horizon and outgoing at infinity; and Q, being radial, preserves the
harmonics; so on {r > r_h}, each component r^(−3/2)u(r_*)Se^(−iσt) of e^(−iσt_*)ω, S ∈ 𝒮_l, has u solving
−u″ + (V_l − σ² − iϵ_σfq)u = 0, with u a multiple of u_h near −∞ and of u_∞ near +∞, where q = 0, as in the proof of
[[lem:rb-transfer]]. As V_l is real,
Im(ū(−u″ + (V_l − σ² − iϵ_σfq)u)) = −(Im(ūu′))′ − ϵ_σfq|u|², and Im(ūu′) tends to σ|c_+|² at +∞ and to −σ|c_−|² at −∞,
where u − c_±e^(±iσr_*) → 0. Integrating over ℝ, 0 = −σ(|c_+|² + |c_−|²) − ϵ_σ∫fq|u|²dr_*. Both terms have the sign of
−σ, so c_+ = 0; u is then the zero multiple of u_∞ near +∞, and u = 0. So ω = 0 on {r > r_h}, and inside the horizon
ω = 0 follows as in part (d) of the proof of [[prop:iii-d-6-2]]. ∎

In the notation of [[lem:rb-gluing]], W is multiplication by sgn(σ)q and kWj = ϵ_σQ, and [[lem:rb-gluing]] uses no sign
of W. With ϵ_σ replaced by −sgn σ the two terms in the proof can cancel.

### The scalar-type blocks at zero energy {#sec:rb-scalar-blocks}

The inverse bound of [[thm:i-c-3-1]] (4) for the linearised operator at zero energy is, in SO(4)-averaged norms and by
[[lem:rb-schur]] (b), the supremum of the inverse bounds of its blocks of one type and degree. For the tensor-type
blocks the gauge terms vanish (the proof of [[lem:rb-transfer]]). The scalar-type blocks carry them, and this section
records what can be said about these blocks.

*The operator.* Let m_0 = 1 and L := L_(b_0) of [[def:iii-b-6-1]], with 2L = □ + 2E^C δG + 2δ*_(E_C)E^Υ G + 2R
([[eq:iii-f-1-2]]), acting on stationary symmetric 2-tensors in the Kerr–Schild chart of [[prop:iii-b-3-4]], in which

    g_(b_0) = −f dt² + 2(1 − f) dt dr + (2 − f) dr² + r²g̸,     f = 1 − 1/r²,

regular across the horizon; with v := t + r it is −f dv² + 2dv dr + r²g̸. Its 1-forms are c_C of [[sec:iv4-0]] (that of
[[prop:np-10-14]] at r_0 = 100, with v_C = 1/2, e_C = 1/102400 and γ_C = h⁻¹), c_Υ = ζ(r)r⁻¹dt with ζ = 1 for large r
(our choice, as at the start of [[sec:rb-transfer]]; [[def:iii-b-6-1]] fixes c_Υ only for large r), and
c_(Υ,H) = −½χ(r)dr with χ ∈ C_c^∞ equal to 1 near r_h ([[sec:iii-d1-1]]); γ_(Υ,H) ∈ (0, ϵ_0] and e_Υ, γ_Υ below the
thresholds of [[prop:iii-d1-4-1]]. The tensor-type blocks do not depend on ζ, χ, the smoothing of c_C or the
parameters; the scalar-type blocks do, and every statement below is made for all admissible choices at once unless a
choice is named. Where numbers are given at (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100), they are numbers of the operator with
those parameters. This point lies outside the set on which the theorems are proved: γ_C = 10⁶ is not of the form h⁻¹
with h as in [[eq:iv4-0-1]], where h < 10⁻⁶, and (γ_Υ, e_Υ) = (1/100, 1/100) are not shown to lie below the thresholds
of [[prop:iii-d1-4-1]], which are proved to exist without a value.

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

*Proof.* L = D Ric + δ*_(E_C)δ_(E_Υ)G at the Ricci-flat g_(b_0). (a) δ*w = ½ℒ_(w♯)g_(b_0), and
D Ric(ℒ_Xg) = ℒ_X Ric(g) = 0 at a Ricci-flat g, so Lδ*w = δ*_(E_C)δ_(E_Υ)Gδ*w = δ*_(E_C)(½□^Υw). (b) The
contracted Bianchi identity δ_gG_g Ric(g) = 0 holds for every metric; differentiating at the Ricci-flat g_(b_0), where
Ric = 0, gives δG(D Ric(h)) = 0. So 2δG(Lh) = 2δGδ*_(E_C)(δ_(E_Υ)Gh) = □^C Υ(h). (c) The Kerr–Schild metrics are
Ricci-flat for every m ([[prop:iii-b-3-4]]); differentiate at m = 1. ∎

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
double root 1 at l = 0 and at l = 1 (D = (ι − 1)² at s0 and s1, [[eq:iii-f1-2-1]]).

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

*The roots of C and of P_l.* C is a cubic with leading coefficient −h², and P_l a sextic with leading coefficient −h³
([[prop:np-10-12]] (iii)). Expanding [[eq:s14-c0]] and the determinant of [[eq:s14-nl]] about ι = 2 gives
C(2 + ε) = Σ_(k≤3) c_kε^k and P_l(2 + ε) = Σ_(k≤6) c_kε^k, with the exact coefficients

    C:    c_0 = 1.4948443959375·10⁻⁴,  c_1 = −1.999957171827171875,  c_2 = −2.999994234375·10⁻⁶,  c_3 = −10⁻¹²;
    P_2:  c_0 = 1.131875750625·10⁻⁹,  c_1 = −3.9186117873477253125·10⁻⁴,  c_2 = 2.000144656033436956015625,
          c_3 = −1.999958171536796769234375;
    P_4:  c_0 = 1.4261642521875·10⁻⁸,  c_1 = −8.7661649198425078125·10⁻⁴,  c_2 = 2.000224654883184362015625,
          c_3 = −1.999958171408796889734375;

and, for P_2 and P_4, |c_4| < 5·10⁻⁶, |c_5| < 4·10⁻¹² and c_6 = −10⁻¹⁸, so that |c_4ε⁴ + c_5ε⁵ + c_6ε⁶| < 10⁻²⁴ for
0 ≤ ε ≤ 2·10⁻⁵. Let (ε_−, ε_+) be (7.474375·10⁻⁵, 7.474385·10⁻⁵) for C, (2.93235·10⁻⁶, 2.93245·10⁻⁶) for P_2 and
(1.692235·10⁻⁵, 1.692245·10⁻⁵) for P_4. The sums c_0 + c_1ε + c_2ε² + c_3ε³ at ε = ε_− and ε = ε_+ are
1.4071…·10⁻¹⁰ and −5.9280…·10⁻¹¹ for C, 1.6962…·10⁻¹⁶ and −3.7843…·10⁻¹⁴ for P_2, and 1.7929…·10⁻¹⁴ and
−6.2962…·10⁻¹⁴ for P_4; so C and P_l are positive at 2 + ε_− and negative at 2 + ε_+, and C(2) = c_0 > 0 and
P_l(2) = c_0 > 0. From [[eq:s14-c0]] and [[eq:s14-nl]], moreover,

    C(−1.5·10⁶) = −3.7505…·10⁵,
    P_2(−1.5·10⁶) = 4.2193…·10¹⁷,  P_2(−999980) = −4.0028…·10⁸,  P_2(5/2) = 0.2498…,  P_2(3) = −2.1037…·10⁻⁴,
    P_4(−1.5·10⁶) = 4.2193…·10¹⁷,  P_4(−999980) = −4.0028…·10⁸,  P_4(5/2) = 0.2496…,  P_4(3) = −6.1511…·10⁻⁴.

C tends to +∞ as ι → −∞, so it has a root in each of (−∞, −1.5·10⁶), (−1.5·10⁶, 2) and (2 + ε_−, 2 + ε_+); these are
its three roots, real and simple, and ι_0 is the third. P_l tends to −∞ as ι → −∞, so it has a root in each of
(−∞, −1.5·10⁶), (−1.5·10⁶, −999980), (−999980, 2), (2 + ε_−, 2 + ε_+), (2 + ε_+, 5/2) and (5/2, 3); these are its six
roots, real and simple, and ι_l is the fourth. So ι_l − 1 ∈ (1 + ε_−, 1 + ε_+), which is [[eq:rb-roots-point]]; every
other root of det N^n_l coming from C or P_l is real and lies below 1 or, at l = 2, 4, above 1 + ε_+; with the first
part the lemma follows. ∎

*The horizon.* Write x := a_vγ_C r_h, with a_v the dv-component of c_C at r_h.

**Lemma {#lem:rb-horizon-exponents}** (The horizon exponents do not depend on l.) r = r_h is a regular singular point of
the block L_l, and its exponents are 0, with multiplicity equal to the size n_l of the block (7, 6 or 4), and the
eigenvalues of the restriction to the block of the fibre endomorphism K of [[lem:iii-f2-1-1]]. If c_Υ vanishes near
r_h these are, for l ≥ 2,

    2 − 2x,   1 − x,   −(1 − e_C)x,   0,   0,   −1,   −2,

the two zeros belonging to dv dr and to the trace-free angular tensors; at l = 1 the same without the second zero, and
at l = 0 the values 2 − 2x, −(1 − e_C)x, 0 (on dv dr) and −2. If instead c_Υ = ζr⁻¹dt with ζ(r_h) = ζ_h near r_h, the
value 0 on dv dr and the values −1 and −2 are replaced by −ζ_hγ_Υ(1 − e_Υ), −1 − ζ_hγ_Υ and −2 − 2ζ_hγ_Υ, the others,
the zero on the trace-free angular tensors included, being unchanged. None of these depends on l.

*Proof.* Work in the ingoing chart (v, r), in which stationary fields are those independent of v, and use the frame (dv,
dr, r dω), which differs from (dt, dr, r dω) by the constant change dt = dv − dr; this changes neither the order of the
singularity nor the exponents. In this chart g^(vv) = 0, g^(vr) = 1 and g^(rr) = f, with f = f′(r_h)(r − r_h) (1 + O(r −
r_h)). By [[lem:rb-block-structure]], the block of 2L, which has the exponents of L_l, has the form −fU″ + A_1(r)U′ +
A_0(r)U on the vector U of radial coefficients, with A_1, A_0 smooth across r_h; for Y := (U, (r − r_h)U′),

    (r − r_h)Y′ = 𝔐(r)Y,     𝔐(r_h) = ⎛ 0    1                    ⎞ ,
                                       ⎝ 0    1 + A_1(r_h)/f′(r_h) ⎠

as (r − r_h)A_0/f is smooth; so the exponents are 0 (n_l times) and the eigenvalues of 1 + A_1(r_h)/f′(r_h).

*The coefficient of ∂_r at r_h.* At r_h the Christoffel symbols with a lower index v are Γ^v_vv = f′/2 and
Γ^r_vr = −f′/2, all others vanishing ([[eq:s13-chris]] and the formula after it; Γ^r_vv = ff′/2 vanishes at r_h). So at
r_h, ∇_(∂_v)dv = −(f′/2)dv, ∇_(∂_v)dr = (f′/2)dr and ∇_(∂_v)e = 0 for e = r ê, ê an angular covector of unit length
for γ (∂_vr = 0): ∇_(∂_v) acts on the frame by 𝔄_v = −(f′(r_h)/2)K_0, where K_0 is 1 on dv, −1 on dr and 0 on the
angular covectors, extended to symmetric 2-tensors by the Leibniz rule. In □ = ∇*∇ = −g^(μν)∇_μ∇_ν the first-order
terms in ∂_r are −(1/√|g|)∂_μ(√|g|g^(μr))∂_r = −r⁻³(r³f)′∂_r, which is −f′(r_h)∂_r at r_h, and −2g^(μr)𝔄_μ∂_r =
−2𝔄_v∂_r at r_h; together −f′(r_h)(1 − K_0)∂_r. The first-order operators 2E^CδG and 2δ*E^ΥG have, at r_h,
∂_r-coefficients equal to their principal symbols at the covector ξdr divided by iξ. With σ_1(δ)(ζ)h = −iι_(g⁻¹ζ)h,
σ_1(δ*)(ζ)w = iζ ⊗_s w, g⁻¹dr = ∂_v at r_h, f′(r_h) = 2/r_h and E^Υ equal to its horizon part near r_h, these
coefficients are f′(r_h)K_C and f′(r_h)K_Υ, where by [[eq:iii-b-6-2]] and [[eq:iii-b-6-5]]

    K_Ch := −r_hγ_C(2c_C ⊗_s ι_(∂_v)Gh − (2/3)(1 − e_C)g⟨c_C, ι_(∂_v)Gh⟩),   K_Υh := 2r_hγ_(Υ,H) dr ⊗_s ι_(g⁻¹c_(Υ,H))h,

⟨·, ·⟩ the pairing by g⁻¹. All other terms are of order zero in r on stationary fields of one degree. So the
coefficient of ∂_r of 2L at r_h is −f′(r_h)(1 − K) with K := K_0 + K_C + K_Υ, and 1 + A_1(r_h)/f′(r_h) = K on the
block. This K is the endomorphism of [[lem:iii-f2-1-1]]: on half-densities by |dg| = 𝔪|dv dr dz|, with
z = (z¹, z², z³) coordinates on 𝕊³ and 𝔪 := r³|det γ|^(1/2) (the (v, r) block of g has determinant −1), an operator
−g^(μν)∂_μ∂_ν + b^μ∂_μ + c has subprincipal symbol iξ(b^r + 𝔪⁻¹∂_μ(𝔪g^(μr))) at the covector ξdr, and
𝔪⁻¹∂_μ(𝔪g^(μr)) = r⁻³(r³f)′ = f′(r_h) at r_h, so the subprincipal symbol of 2L there is iξf′(r_h)K.

*The values.* Give dv, dr and the angular covectors the weights 1, −1 and 0, and a symmetric product the sum of the
weights of its factors. At r_h, g = 2dv dr + T with T := Σ_a e_a² (e_1, e_2, e_3 an orthonormal angular coframe),
g⁻¹dv = ∂_r and g⁻¹dr = ∂_v; ι_(∂_v) removes a factor dv and ι_(∂_r) a factor dr, and G and tr preserve the weight. So
K_0 multiplies a monomial by its weight; with c_C = a_vdv + a_rdr, the a_v-part of K_C preserves the weight and its
a_r-part lowers it by 2; and as c_(Υ,H) = −½χdr has no dv-component, g⁻¹c_(Υ,H) = −½∂_v there and K_Υ lowers the
weight by 2. So K is block triangular for the grading, and its eigenvalues are those of its weight-preserving part D_0
on the weight spaces. On dv² (tr dv² = 0, ι_(∂_v)dv² = dv, ⟨dv, dv⟩ = 0), D_0 = 2 − 2x. On dv ⊗_s e_a (trace-free,
ι_(∂_v) = ½e_a, ⟨dv, e_a⟩ = 0), D_0 = 1 − x. On the weight-zero span of dv dr, T and the trace-free angular tensors,
K_0 = 0; G(dv dr) = −½T and ι_(∂_v)T = 0, so D_0(dv dr) = 0; GT = −½T − 3dv dr, ι_(∂_v)GT = −(3/2)dr and
⟨dv, dr⟩ = 1, so D_0T = −x(−3dv dr + (1 − e_C)g) = x(1 + 2e_C)dv dr − x(1 − e_C)T; and D_0 vanishes on the trace-free
angular tensors. On dr ⊗_s e_a and on dr², ι_(∂_v) gives 0, so D_0 = −1 and −2.

K commutes with the rotations that fix the point. So it maps the span of dv², dv dr, dr², T (four copies of the trivial
representation of the stabiliser) into itself, the span of dv ⊗_s e and dr ⊗_s e with e angular into itself, and acts
as a scalar on the trace-free angular tensors; on the block it acts on the coefficients of S, of dS and of δ̸*₀dS by
these three restrictions, which by the above are triangular with diagonal entries 2 − 2x (dv²), 0 (dv dr),
−(1 − e_C)x (T) and −2 (dr²); 1 − x and −1; and 0. This is the list. If c_Υ = ζr⁻¹dt near r_h, then at r_h,
c_Υ = ζ_h(dv − dr) and g⁻¹c_Υ = ζ_h(∂_r − ∂_v), and the principal symbol of 2δ*E^Υ_∞G at ξdr adds to K the term
K_∞h = −ζ_hγ_Υ r_h dr ⊗_s (2ι_(∂_r−∂_v)h − e_Υ(dv − dr) tr h) ([[eq:iii-b-6-5]]). For the grading above, its part
with ι_(∂_r) and its part with e_Υ dr ⊗_s dv preserve the weight and the others lower it by 2, so K stays block
triangular. The weight-preserving
part adds −ζ_hγ_Υ on dr ⊗_s e (ι_(∂_r)(dr ⊗_s e) = ½e) and −2ζ_hγ_Υ on dr², nothing on dv² and dv ⊗_s e, and on the
weight-zero span of dv dr and T it adds −ζ_hγ_Υ(1 − e_Υ) on dv dr (ι_(∂_r)(dv dr) = ½dv and tr(dv dr) = 1) and maps T
to 3ζ_hγ_Υe_Υ dv dr, which keeps that block triangular. Adding these to the diagonal entries above gives the second
list. ∎

At (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100), with a_v = 1/200 (the inner form of c_C) and r_h = 1, x = 5000, and at
l ≥ 2 the exponents other than the n_l zeros are −9998, −4999, −2559975/512, 0, 0, −1, −2 when c_Υ vanishes near the
horizon, and −9998, −4999, −2559975/512, −0.0099, 0, −1.01, −2.02 when ζ = 1 there. At the horizon the exponents are
the same at every degree, and three of them, 2 − 2x, 1 − x and −(1 − e_C)x, are of size γ_Ca_vr_h. The zeroth-order
coefficients of the block at r_h depend on κ: on h = H_0S dt² the only term of 2L that differentiates S twice is the
angular part of □, which contributes κr⁻²H_0S dt²; a term that differentiates S once gives no multiple of S dt², and a
term that does not differentiate S has a coefficient independent of κ; so the coefficient of H_0 in F_0 is κ/(2r_h²)
plus a number that does not depend on κ.

*The weight.* Let α + 2 =: β lie in the indicial gap at infinity of the block. The zero-energy problem is posed on
X̄ = {r ≥ r_0}, with r_0 = r_♭ ≤ r_h/2 ([[def:s12-radii]]), so that its domain contains r = r_h/2. On stationary
fields of scalar type l we use the norms

    ‖h‖_X² := Σ_j ∫ r^(2α+3)(|u_j|² + r²|∂_ru_j|² + κ|u_j|²) dr,     ‖F‖_Y² := Σ_j ∫ r^(2α+7)|F_j|² dr,
                                                                                                  {#eq:rb-block-norms}

with the integrals over the whole domain, in the orthonormal components (F_j those of a tensor F of the form
[[eq:rb-scalar-type]]): near infinity these are norms of H̄_b^(1,α) and H̄_b^(0,α+2) of [[sec:i-c-1-2]], with the
b-vector field r∂_r and the rotation fields as generators (the squares of the rotation fields sum to κ on scalar type
l), and on a bounded range of r they are equivalent to those of H¹ and L². In x := log r, u = r^(−β)φ(x) gives
r^(2α+3)(|u|² + r²|∂_ru|²)dr = (|φ|² + |φ′ − βφ|²)dx, and F = r^(−β−2)φ(x) gives r^(2α+7)|F|²dr = |φ|²dx.

**Lemma {#lem:rb-quasimode}** (An upper bound for the least singular value.) For every nonzero v ∈ ℂ^(n_l) and every
admissible choice of the free gauge data,

    inf_(H≠0) ‖L_lH‖_Y/‖H‖_X ≤ |N^n_l(β)v|/((1 + β² + κ)^(1/2)|v|),

the infimum over the smooth H with compact support in {r ≥ R}, for any R; at l = 0 also over the H = H_c + w with H_c
smooth with compact support in {r ≥ R} and w ∈ V that are orthogonal in X to V, for any finite-dimensional subspace V
of X with L_l(V) ⊂ Y.

*Proof.* Take φ ∈ C_c^∞((0, 1)) with ‖φ‖_(L²) = 1, x_0 ≥ log R, W ≥ 1, φ_W(x) := W^(−1/2)φ((x − x_0)/W), and H_W with
orthonormal components u = r^(−β)φ_W(log r)v. Then ‖H_W‖_X² = |v|²∫(|φ_W|² + |φ_W′ − βφ_W|² + κ|φ_W|²)dx =
(1 + β² + κ)|v|² + |v|²‖φ_W′‖², the cross term ∫φ_Wφ_W′ vanishing, and ‖φ_W′‖ = W⁻¹‖φ′‖. For x_0 large, H_W is
supported where the coefficients are those of the model up to O(r⁻²); since the model is r⁻²N^n_l(−r∂_r) and
−r∂_r(r^(−β)ψ(log r)) = r^(−β)(β − ∂_x)ψ,

    L_lH_W = r^(−β−2)(N^n_l(β − ∂_x)(φ_Wv) + e),     N^n_l(β − ∂_x) = N^n_l(β) − N^n_l′(β)∂_x + ½N^n_l″(β)∂_x²,

with |e| ≤ Ce^(−2x_0)(|φ_W| + |φ_W′| + |φ_W″|)|v|. Hence ‖L_lH_W‖_Y ≤ |N^n_l(β)v| + CW⁻¹ + Ce^(−2x_0), and letting
W → ∞ and then x_0 → ∞ gives the bound. At l = 0, let P be the orthogonal projection of X onto V; then H_W − PH_W
is of the stated form. For fixed W, H_W → 0 weakly in X as x_0 → ∞, since it is bounded and its support leaves every
compact set, while fields with compact support are dense in X; so ‖PH_W‖_X → 0, V being finite-dimensional. As L_l is
linear from the finite-dimensional V into Y, ‖L_lPH_W‖_Y ≤ C_V‖PH_W‖_X → 0, and
‖L_l(H_W − PH_W)‖_Y/‖H_W − PH_W‖_X has the same limit as ‖L_lH_W‖_Y/‖H_W‖_X, as ‖H_W‖_X ≥ (1 + β² + κ)^(1/2)|v|. ∎

This is the elementary half of the b-calculus fact that the norm of an inverse on a weighted space is at least that of
the inverse of the indicial family on the weight line. For the scalar model ½A_l, whose indicial family is
½(ι(2 − ι) + κ), it gives at β = 1 an upper bound (κ + 1)/(2(κ + 2)^(1/2)) for its least singular value in these norms.

At α = −1 (β = 1) the indicial family of the degree-2 block has the root 1.0000029324, less than 2.94 · 10⁻⁶ from the
weight line ([[lem:rb-roots-point]]), and [[lem:rb-quasimode]] then gives small upper bounds. To evaluate them we write
the indicial family out.

*The indicial family, explicitly.* Put y_j := u_j/ν_j, with (ν_0, …, ν_6) := (1, √2, 1, (2κ)^(1/2), (2κ)^(1/2), √3,
((2/3)κ(κ − 3))^(1/2)), so that (y_0, …, y_6) = (H_0, H_1, H_2, H_3/r, H_4/r, H_5, H_6) and

    h = S(y_0dt² + 2y_1dt dr + y_2dr²) + 2r(y_3dt + y_4dr) ⊗_s dS + r²(y_5Sg̸ + y_6δ̸*₀dS);

write a stationary 1-form of scalar type l as (ω_0dt + ω_1dr)S + ω_2r dS. Let N^y_l(ι) be the indicial family in the
coordinates y, so that N^n_l(ι) has the entries ν_iN^y_l(ι)_(ij)/ν_j; at l = 1 the coordinate y_6, and at l = 0 the
coordinates y_3, y_4, y_6 and ω_2, are absent, and the corresponding rows and columns are dropped.
With |w|_ν² := Σ_j ν_j²|w_j|², the vector v with v_j = ν_jw_j has |v| = |w|_ν and |N^n_l(β)v| = |N^y_l(β)w|_ν.

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
scalar type l, in the frame (dt̄, dr, r dω), where ḡ = −dt̄² + dr² + r²g̸; we write t for t̄, so that
c̄_C = r⁻¹(dt − v_Cdr) and c̄ = r⁻¹dt in [[eq:iii-f-2-1]]. On the coordinates of a section r^(−ι)ŷ (or
r^(−ι)ω̂), □̄ acts by 𝔚(ι) and the result carries r^(−ι−2); δ̄ acts by 𝔇(ι), δ̄* by 𝔖(ι), Ē^C by 𝔈_C and Ē^ΥḠ by
𝔈_Υ, the result carrying r^(−ι−1); and Ḡ acts by 𝔊. If operators T and T′ map r^(−ι)a to r^(−ι−d)T(ι)a and
r^(−ι)b to r^(−ι−d′)T′(ι)b for every ι, then T′T maps r^(−ι)a to r^(−ι−d−d′)T′(ι + d)T(ι)a. Hence 2Ē^Cδ̄Ḡ acts by
2𝔈_C𝔇(ι)𝔊 and 2(δ̄* + Ē^C)Ē^ΥḠ by 2(𝔖(ι + 1) + 𝔈_C)𝔈_Υ, each result carrying r^(−ι−2), and half the sum with
𝔚(ι) is [[eq:rb-indicial-explicit]]. It remains to derive the six matrices. Below, dS, g̸ and δ̸*₀dS are the objects on
𝕊³, and the 1-form r dS and the tensor r²q, q on 𝕊³, are identified with tangential fields homogeneous of degree 0, as
in [[sec:iii-a1-2]].

*𝔚.* Write h = 𝖠dt² + 2𝖷dt dr + 𝖡dr² + 2dt ⊗_s 𝖶 + 2dr ⊗_s 𝖴 + q, with 𝖶, 𝖴 tangential 1-forms and q a tangential
symmetric 2-tensor, so that h_tt = 𝖠, (h_ti) = 𝖷x̂ + 𝖶 and (h_ij) = 𝖡x̂ ⊗ x̂ + x̂ ⊙ 𝖴 + q. On stationary sections the
formula [[eq:s11-box-tensors]] in the proof of [[lem:iii-a1-2-1]], at ν = 3, gives □̄h, with T_X, T_W, T_B, T_U and T_Q
as there and □_c := −∂_r² − (3/r)∂_r + r⁻²Δ̸ acting on each of 𝖠, …, q, Δ̸ the rough Laplacian of 𝕊³
([[sec:iii-a1-1]]). Take 𝖠 = y_0S, 𝖷 = y_1S, 𝖡 = y_2S, 𝖶 = y_3dS, 𝖴 = y_4dS and q = y_5Sg̸ + y_6δ̸*₀dS; then
□_c(r^(−ι)X) = r^(−ι−2)(Δ̸ + 2ι − ι²)X for X on 𝕊³, as (−∂_r² − (3/r)∂_r)r^(−ι) = (2ι − ι²)r^(−ι−2). The identities
[[eq:iii-a1-1-2]] at ν = 3 (δ̸dS = κS, Δ̸dS = (κ − 2)dS, δ̸*dS = δ̸*₀dS − (κ/3)g̸S, Δ̸(g̸S) = κg̸S, δ̸(g̸S) = −dS,
tr(g̸S) = 3S, δ̸(δ̸*₀dS) = (2/3)(κ − 3)dS, Δ̸(δ̸*₀dS) = (κ − 6)δ̸*₀dS) turn □_c𝖠, T_X, T_B, T_W and T_U into the
components 0 to 4 of 𝔚(ι)y, and T_Q into the components 5 and 6; for instance
T_U = r^(−ι−2)((ϖ + 4)y_4 − 2y_2 + 2y_5 − (4/3)(κ − 3)y_6)dS.

*𝔊.* tr_ḡ h = (y_2 − y_0 + 3y_5)S, and Ḡh = h − ½ḡ tr_ḡ h.

*𝔇.* In Cartesian coordinates, on stationary sections, (δ̄k)_t = −∂_ik_(it) and (δ̄k)_j = −∂_ik_(ij). Let V be a
tangential vector field and Q a tangential symmetric 2-tensor field on ℝ⁴ ∖ {0}, both homogeneous of degree 0, and
D the Euclidean derivative. At a point of radius r and for X tangent to the sphere there, the Gauss formula of the
unit sphere gives D_XV = r⁻¹(∇̸_XV − ⟨X, V⟩x̂) and D_XQ = r⁻¹(∇̸_XQ − x̂ ⊙ Q(X)), Q(X) := Q(X, ·): the tangential part
of D_XV is r⁻¹∇̸_XV, the factor r⁻¹ coming from the radius, and its normal part is
⟨D_XV, x̂⟩x̂ = −⟨V, D_Xx̂⟩x̂ = −r⁻¹⟨X, V⟩x̂, as ⟨V, x̂⟩ = 0 and D_Xx̂ = r⁻¹X; the formula for Q follows by writing
Q = Σ q_bce_b ⊗ e_c in a tangential frame. Also D_(x̂)V = 0 and D_(x̂)Q = 0. Taking the trace over an orthonormal
frame (x̂, e_1, e_2, e_3), with (x̂ ⊙ Q(e_a))(e_a, ·) = Q(e_a, e_a)x̂, gives ∂_iV_i = −r⁻¹δ̸V and
∂_iQ_ij = −r⁻¹((δ̸Q)_j + (tr Q)x̂_j). With ∂_ix̂_j = r⁻¹(δ_ij − x̂_ix̂_j), x̂_i∂_iS = 0 and x̂_i∂_iV_j = 0, for a
function f(r) and a function S on 𝕊³ this gives

    ∂_i(fSx̂_i) = (f′ + 3f/r)S,     ∂_i(fV_i) = −r⁻¹fδ̸V,     ∂_i(fSx̂_ix̂_j) = (f′ + 3f/r)Sx̂_j,
    ∂_i(f(x̂_iV_j + V_ix̂_j)) = (f′ + 4f/r)V_j − r⁻¹f(δ̸V)x̂_j,     ∂_i(fQ_ij) = −r⁻¹f((δ̸Q)_j + (tr Q)x̂_j).

For k with the coordinates y, k_(ti) = y_1Sx̂_i + y_3(dS)_i and k_(ij) = y_2Sx̂_ix̂_j + y_4(x̂_i(dS)_j + (dS)_ix̂_j) +
(y_5Sg̸ + y_6δ̸*₀dS)_ij; with y_j = r^(−ι)ŷ_j these give the three components of 𝔇(ι)ŷ.

*𝔖.* The Christoffel symbols of ḡ in t, r and coordinates on 𝕊³ (indices a, b, c) vanish except Γ^r_(ab) = −rg̸_ab,
Γ^a_(rb) = Γ^a_(br) = r⁻¹δ^a_b and Γ^c_(ab) = Γ̸^c_(ab). For ω = (ω_0dt + ω_1dr)S + ω_2r dS with ω_j functions of r,
the components of δ̄*ω = ½(∇_μω_ν + ∇_νω_μ) are therefore 0 (tt), ½ω_0′S (tr), ½ω_0∂_aS (ta), ω_1′S (rr),
½(rω_2′ + ω_1 − ω_2)∂_aS (ra) and r(ω_1Sg̸ + ω_2∇̸²S)_ab (ab), where ∇̸²S = δ̸*₀dS − (κ/3)g̸S; with ω_j = r^(−ι)ω̂_j
these are the components of the tensor whose coordinates are r^(−ι−1)𝔖(ι)ω̂.

*𝔈_C and 𝔈_Υ.* With c̄_C = r⁻¹(dt − v_Cdr), ⟨c̄_C, ω⟩ = −r⁻¹(ω_0 + v_Cω_1)S, and the coordinates of
Ē^Cω = γ_C(2c̄_C ⊗_s ω − (2/3)(1 − e_C)ḡ⟨c̄_C, ω⟩) ([[sec:iii-f-2]]) are r⁻¹𝔈_Cω. The modification Ē^Υ of
[[sec:iii-d-2]] is E^Υ_(g₀,∞) of [[eq:iii-b-6-1]] at g₀ = ḡ and c_Υ = c̄, so the first identity of [[eq:iii-b-6-5]]
gives Ē^ΥḠh = −γ_Υ(2ι_(ḡ⁻¹c̄)h − e_Υc̄ tr_ḡ h); as ḡ⁻¹c̄ = −r⁻¹∂_t and h(∂_t, ·) = (y_0dt + y_1dr)S + y_3r dS, the
coordinates of Ē^ΥḠh are r⁻¹𝔈_Υy. ∎

**Proposition {#prop:rb-quasimode-point}** (Upper bounds at γ_C = 10⁶.) Let (γ_C, γ_Υ, e_Υ) = (10⁶, 1/100, 1/100). The
least singular value of L_l from H̄_b^(1,α) to H̄_b^(0,α+2), in the norms [[eq:rb-block-norms]] (at l = 0
on the complement of the zero-energy state), is at most

    3.1413 · 10⁻⁶, 2.6181 · 10⁻⁷ and 1.4956 · 10⁻⁶ at α = −1,     0.0204, 0.0149 and 0.0121 at α + 2 = 1/2,

at l = 0, 2 and 4 respectively. Hence the inverse bound of the scalar-type blocks at (s, α) = (1, −1) is at least
1/(2.6181 · 10⁻⁷) > 3.81 · 10⁶.

*Proof.* Let β := α + 2. By [[lem:rb-quasimode]] with v_j = ν_jw_j, the least singular value is at
most |N^y_l(β)w|_ν/((1 + β² + κ)^(1/2)|w|_ν) for every nonzero w. Take for w the integer vectors below, in the
coordinates (y_0, y_1, y_2, y_5) at l = 0 and (y_0, …, y_6) at l = 2, 4, and evaluate N^y_l(β)w by
[[eq:rb-indicial-explicit]] with v_C = 1/2 and e_C = 1/102400 ([[sec:iv4-0]]), in exact rational arithmetic. The two
norms satisfy

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

An explicit constant for these blocks is therefore to be sought at a weight in the middle of the gap. The linearised
operator is used at the weights of [[eq:iii-h-1-1]], α + 2 ∈ (0, 1), an open interval, so the weight α = −1 of
[[prop:rb-quasimode-point]] lies at its upper end point, outside it.

**Remark {#rem:rb-quasimode-observed}** (Numerical observation.) On the full degree-2 block at the parameters above,
the quasi-mode of the proof of [[lem:rb-quasimode]] with x_0 = log 400 and widths W = 100, 1000 and 10000, evaluated in
floating point, gives the quotient ‖L_lH‖_Y/‖H‖_X = 1.3900 · 10⁴, 1.3901 · 10³ and 1.3901 · 10², and the
dilation-invariant model gives the same to 10⁻³. At these widths the term N^n_l′(1)vφ_W′, of the size of γ_C, dominates,
so the quotient falls like 1/W and reaches the bound of [[lem:rb-quasimode]] only for W of order 5 · 10¹². No proof uses
these values.

*The perturbative route at large degree.* Write L_l = ½A_l · Id + ℛ_l in the orthonormal components, ℛ_l of first order,
and s_min for the least singular value in the norms [[eq:rb-block-norms]] at α = −1. A lower bound
s_min(L_l) ≥ s_min(½A_l) − ‖ℛ_l‖_(X→Y) needs ‖ℛ_l‖ below s_min(½A_l) ≤ (κ + 1)/(2(κ + 2)^(1/2)). At the
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

In the Kerr–Schild chart of the operator above, where g = −f dt² + 2(1 − f) dt dr + (2 − f) dr² + r²g̸, one has
g^(tt) = f − 2, g^(tr) = 1 − f = r⁻², g^(rr) = f and |det g|^(1/2) = r³|det g̸|^(1/2) (the determinant of the (t, r)
block of g is −1), and Γ^t_(tt) = −½g^(tr)∂_rg_(tt) = ½(1 − f)f′,
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

Fields H with only u_3 nonzero, of high frequency in r and concentrated near a radius r_1 of the domain, have
lim inf ‖ℛ_lH‖_Y/‖H‖_X ≥ r_1|M_33(r_1)| by [[eq:rb-block-norms]] (at α = −1 the weights are r and r⁵, and the
derivative term dominates both norms). The domain of the zero-energy problem contains r = r_h/2 = ½ (*The weight*
above), so ‖ℛ_l‖ ≥ ½|M_33(½)| = 9996 for every l ≥ 1; at l = 0 the component u_3 does not exist. And
(κ + 1)/(2(κ + 2)^(1/2)) < 9996 exactly when (κ + 1)² < 4 · 9996²(κ + 2), which holds for every l ≤ 19,991, in
particular at l = 19,990 (κ = 399,640,080: (κ + 1)² < 1.59713 · 10¹⁷ < 1.59728 · 10¹⁷ < 4 · 9996²(κ + 2)) and fails
from l = 19,992 on. So this route gives no lower bound at any degree l ≤ 19,991; if a perturbative regime exists at
all, it begins above that degree, and the horizon part of the block does not become perturbative at any degree
([[lem:rb-horizon-exponents]]).
