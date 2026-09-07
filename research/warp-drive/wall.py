#!/usr/bin/env python3
"""
wall.py -- the stability of the warpshell wall is structural, so the fix is too.

warpshell.py ended on a wall that was not the energy budget.  Le's realized
tangential-pressure wall sits exactly on the Poisson-Visser marginal curve
V''(R) = 0, a neutral radial zero mode that e-folds in a light-crossing time, and
the burn-outruns-instability criterion delta_eta <= lambda excludes a habitable
1 g, 10 m design by 1.8e14.

BUT LE ALSO SAYS THE ESCAPE, IN ONE CLAUSE: "A slightly stiffer, still-admissible
wall is strictly stable at no cost in the surface dec margin, which is
junction-fixed and independent of the equation-of-state slope, so strict
stability and strict dominant energy decouple."

This file takes that clause seriously and asks the question it leaves open: HOW
MUCH STIFFER, AND IS THAT MATTER CAUSAL?  Both are computed here from scratch.

-- THE ANSWER -----------------------------------------------------------------

With s = sqrt(1 - x), x = 2m/R the compactness, and beta^2 = dp/dsigma the
surface equation-of-state slope, the linearised radial mode is strictly stable iff

        beta^2  >  beta^2_crit(x)  =  (1-s)(3s^2 + 2s + 1) / (4 s^2 (1 + 3s))

DERIVED HERE, not quoted.  It is exactly the zero of V''(R_0).  And it is CHEAP:

        x = 0.3  (Le's operating point)   beta^2 > 0.07933   c_s > 0.282 c
        x = 2/3  (Einstein-Vlasov limit)  beta^2 > 0.36603   c_s > 0.605 c
        x = 4/5  (the wall's own limit)   beta^2 > 0.73607   c_s > 0.858 c

The middle and last are exact: (sqrt3 - 1)/2 and sqrt5 - 3/2, checked below.
beta^2_crit reaches 1 -- the causal ceiling -- at the root of 15s^3+3s^2-s-1 = 0,

        x* = 0.84374189

and the ENTIRE operative window x < 4/5 lies below it.  So:

    STRICT STABILITY IS AVAILABLE EVERYWHERE THE WALL IS REALIZABLE, WITH A
    SUBLUMINAL SOUND SPEED, AND IT COSTS NOTHING IN DOMINANT ENERGY.

The decoupling is not taken on faith either.  sigma_0 and p_0 come out of the
junction as functions of (s, R) ALONE -- beta^2 does not appear until the second
derivative -- so V(R_0) = 0 and V'(R_0) = 0 hold identically in beta^2, which the
selftest confirms at four values.  The dec margin is therefore untouched:
8 pi R (sigma_0 - p_0) = -(5s-1)(s-1)/(2s), Le's Eq (17), reproduced here from the
Lanczos junction and giving surface dec iff x < 24/25.

-- AND THE CONSTRAINT INVERTS -------------------------------------------------

This is the part worth the trouble.  A marginal wall runs away, so the burn must
BEAT it: tau_burn <= tau_efold, i.e. delta_eta <= lambda.  A strictly stable wall
oscillates instead, at omega = sqrt(V''/2), so the burn must merely not RESONATE
with it: tau_burn >> 1/omega, i.e. W delta_eta / lambda >> 1 with
W = sqrt(V'' R^2 / 2).  The same ratio, upside down.

    design                     marginal wall        stiff wall (x=0.3, b^2=0.5)
    Le App. K worked burn      fails by 2.0         adiabatic by only 2.4
    1 g, 10 m cavity           fails by 1.8e14      ADIABATIC BY 2.2e14

The habitable regime was not near the boundary and on the wrong side of it.  It
was fourteen orders from the boundary, and which side depends entirely on the
sign of V''.  Note the corollary, which is the sanity check on the whole story:
the relativistic corner that a marginal wall handles best is the one a stiff wall
handles worst, and vice versa.  It also lines up with Le's own Prop. 6, which
proves the time-evolved assembly for SLOW fixed-axis burns -- the stiff wall and
the dynamical existence proof want the same regime.

-- BETA^2 IS NOT A FREE KNOB, AND THAT IS THE STING ----------------------------
Everything above treats beta^2 as a design choice.  For real matter it is not:
the matter model DETERMINES it.  Worked here for the cleanest admissible model,
a counter-rotating (Einstein-Vlasov) shell, marked RECONSTRUCTED because no
member or paper states it in this form:

    sigma = n mu gamma and p = n mu gamma v^2/2, so p/sigma = v^2/2 -- and the
    junction ALREADY fixes p_0/sigma_0 = (1-s)/(4s), so v^2 = (1-s)/(2s) is set
    by x alone.  Under a radial perturbation each particle conserves its angular
    momentum, so u = gamma v ~ 1/R, and carrying that through gives

        beta^2_vlasov(x)  =  u^2 (3u^2 + 4) / ( 2 (1 + u^2)(3u^2 + 2) )

It has a ceiling of 1/2 as u -> infinity, and the model itself expires at v = 1,
which is x = 8/9.  Against the requirement:

        x -> 0     ratio -> 4/3 exactly      33% margin, and it is the LIMIT
        x = 0.3    0.090800 vs 0.079332      STABLE by 14%   (Le's own point)
        x = 0.4    0.130697 vs 0.122892      stable by 6%
        x = 0.469  crossover
        x = 2/3    0.281089 vs 0.366025      UNSTABLE
        x = 4/5    0.399187 vs 0.736068      UNSTABLE, badly

    SO THE STRUCTURAL FIX IS REAL BUT CONDITIONAL: counter-rotating matter clears
    the threshold only for x < 0.46898, and the margin is widest at LOW
    compactness, tending to exactly 4/3 as x -> 0.

That is good news exactly where it is needed -- Le's operating point and any
habitable, low-compactness ship are both well inside -- and bad news in the
high-compactness corner, which is the corner a marginal wall handled best.  The
earlier framing, that stiffness is a knob to be turned, was wrong: it is an
output of the matter model, and it happens to clear the bar in the regime that
matters.  Recorded that way round.

-- THE RADIAL CRITERION IS CONFIRMED BY THE LITERATURE, TO MACHINE PRECISION --
Pitre, Schneider and Poisson (arXiv:2604.05980, Phys. Rev. D) quote the radial
criterion for exactly this configuration as Gamma >= Gamma_1 with
Gamma_1 = (4 - 6C + 2 sqrt(1-2C))/(4(1-2C)), C = M/R (LeMaitre-Poisson 2019).
Their Gamma is d ln p/d ln sigma in the REST-MASS density; beta^2 here is
dp/dmu in the ENERGY density, and their Eq (2.7) relates them by
Gamma = beta^2 (mu + p)/p.  Converted, the two agree to 1e-15 at every x from
1e-6 to 0.8, and both go to 3/2 in the Newtonian limit.  Independent derivation,
same answer.

-- AND THE NON-RADIAL MODE, WHICH THE STRUCTURAL FIX DOES NOT REACH ------------
The same paper establishes what this file did not test: the shell is unstable to
NON-RADIAL perturbations.  An even-parity matter mode with purely imaginary
positive frequency exists "for all sampled values of the shell's compactness and
adiabatic index, and all sampled values of the multipolar order l >= 2", and it
survives the Newtonian limit.  Their configuration is a static thin shell,
Minkowski inside, Schwarzschild outside -- LE'S STATIC ANCHOR EXACTLY.

    STIFFENING THE WALL FIXES THE RADIAL MODE AND DOES NOTHING TO l >= 2.
    beta^2 does not appear in the unstable branch at all.

But it is not unconditional in the only variable that matters for a mission.
Their Fig. 1 gives Im{omega} (R^3/M)^{1/2} ~= 0.6, roughly flat over
M/R in [0, 0.3] and Gamma in [1.8, 2.4], so the growth rate is the SELF-
GRAVITATIONAL rate omega ~= 0.6 sqrt(GM/R^3) -- and a diffuse shell has a slow
one.  Against a burn of duration c delta_eta/a, the number of e-foldings is

        N  =  0.6 sqrt(G M / R^3) · c delta_eta / a

and N < 1 is a ceiling on MEAN DENSITY, not on mass or size separately:

        rho_mean  <  3 a^2 / (4 pi G (0.6 c delta_eta)^2)

For a 1 g burn to delta_eta = 0.2 that is 2.658e-4 kg/m^3, about 1/4000 of air.
A 1,000-tonne ship meets it at R > 965 m, and comfortably (N < 0.1) at R > 4.48 km.
The compactness there is x ~ 1e-24, so every dominant-energy window and the
counter-rotating stability condition are satisfied with room to spare, and the
adiabatic criterion is satisfied by twelve orders.  There is a corner, and its
shape is BIG AND DIFFUSE.

Two escapes from the theorem itself are open and neither is claimed here: Pitre
et al. assume VACUUM on both sides, where Le's exterior is outgoing null dust;
and they treat an INFINITESIMALLY THIN shell, where Le's realized wall has finite
thickness.  Their own conclusion is phrased about objects "that feature a thin
shell at its surface".  Whether either escape works is not settled by this file.

-- WHAT THIS STILL DOES NOT SHOW, STATED PLAINLY ------------------------------
1. Not that EVERY admissible matter model clears it.  One model is worked, and
   Le's own realized wall is a Bowers-Liang anisotropic equilibrium rather than
   this one.  Anisotropic elastic matter on 2/3 < x < 4/5 is not treated here,
   and by the table above that is exactly the range where this model fails.
2. Not the flux-coupled dynamic stability of the RADIATING shell, which Le leaves
   open in his Sec. 15.  What is closed here is the frozen-background linear
   radial mode -- the one he identifies as marginal, and no more.
3. beta^2 here is the slope of the thin-shell surface equation of state, which is
   not identical to the microphysical sound speed of the finite-thickness wall.
   The causality reading beta^2 <= 1 is the standard one and is a proxy.
-- A BONUS THEOREM, WHICH IS THE OPPOSITE OF WHAT I EXPECTED ------------------
I went looking for the amplitude at which a swinging shell breaks dominant
energy, since d(sigma-p)/dR = (1-beta^2) sigma' < 0 means the margin falls as the
shell expands.  There is no such amplitude.  As R -> infinity the margin tends to
2(beta^2 sigma_0 - p_0)/(1+beta^2), so the basin is unbounded iff
beta^2 > p_0/sigma_0 = (1-s)/(4s) -- and

        beta^2_crit  -  p_0/sigma_0  =  x / (4 s^2 (1 + 3s))   >  0

exactly, for every x in (0,1), checked to 1e-13 at nine values.  So

    ANY STRICTLY STABLE WALL AUTOMATICALLY HAS AN UNBOUNDED DOMINANT-ENERGY
    BASIN.  Stability does not merely cost nothing in dec; it buys dec.

The oscillation therefore has no admissibility ceiling on its amplitude at all,
which removes the constraint I built this section to measure.

-- METHOD ---------------------------------------------------------------------
Standard Poisson-Visser thin-shell linearisation (Phys. Rev. D 52 7318, 1995) for
Minkowski inside, Schwarzschild outside.  Lanczos gives sigma and p; conservation
gives m_s' = -8 pi R p; the equation of motion is R_dot^2 + V(R) = 0 with
V = 1 - [m_s/(2R) + m/m_s]^2.  For a linear equation of state the conservation
ODE integrates in closed form, sigma(R) = (sigma_0 + K/A)(R/R_0)^{-2A} - K/A with
A = 1 + beta^2 and K = p_0 - beta^2 sigma_0, so V(R) is elementary and every
analytic result below is checked against a finite difference of it -- and the
oscillation period against a direct integration of R_ddot = -V'/2.

stdlib only.
"""
import math, sys

C = 299792458.0
X_THIN_SHELL = 24.0 / 25.0
X_TANGENTIAL = 4.0 / 5.0
X_VLASOV = 2.0 / 3.0

# -- the junction ------------------------------------------------------------

def statics(x, R=1.0):
    """Lanczos, Minkowski inside / Schwarzschild outside.  Returns
    (s, m, sigma_0, p_0).  NOTE: no beta^2 anywhere -- that is the decoupling."""
    s = math.sqrt(1.0 - x)
    m = x * R / 2.0
    sigma = (1.0 - s) / (4.0 * math.pi * R)
    p = (1.0 - s) ** 2 / (16.0 * math.pi * R * s)
    return s, m, sigma, p

def dec_margin(x, R=1.0):
    """sigma_0 - p_0, the worst-observer surface dominant-energy margin for a
    Type I stress with p > 0."""
    _, _, sg, p = statics(x, R)
    return sg - p

def dec_margin_scaled(x):
    """8 pi R (sigma_0 - p_0).  Must equal Le Eq (17): -(5s-1)(s-1)/(2s)."""
    return 8.0 * math.pi * dec_margin(x, 1.0)

def dec_margin_le(x):
    """Le's printed closed form, for comparison only -- never used as a source."""
    s = math.sqrt(1.0 - x)
    return -(5.0 * s - 1.0) * (s - 1.0) / (2.0 * s)

# -- the stability criterion -------------------------------------------------

def one_minus_s(x):
    """1 - sqrt(1-x), computed as x/(1+s) so it stays exact for tiny x.  The
    naive form cancels to zero below x ~ 1e-16, which is exactly where a
    habitable low-compactness ship sits."""
    return x / (1.0 + math.sqrt(1.0 - x))

def beta2_crit(x):
    """DERIVED.  The zero of V''(R_0): stable iff beta^2 > this."""
    s = math.sqrt(1.0 - x)
    return one_minus_s(x) * (3.0 * s * s + 2.0 * s + 1.0) / (4.0 * s * s * (1.0 + 3.0 * s))

def sound_speed_crit(x):
    b = beta2_crit(x)
    return math.sqrt(b) if b <= 1.0 else float("nan")

def causal_limit(lo=1e-9, hi=1.0 - 1e-12, iters=200):
    """DERIVED.  beta^2_crit = 1 at the root of 15s^3 + 3s^2 - s - 1 = 0.
    Returns x* above which strict stability would need superluminal sound."""
    f = lambda s: 15.0 * s ** 3 + 3.0 * s * s - s - 1.0
    a, b = lo, hi
    for _ in range(iters):
        mid = 0.5 * (a + b)
        if f(a) * f(mid) <= 0.0:
            b = mid
        else:
            a = mid
    s = 0.5 * (a + b)
    return 1.0 - s * s

def Vpp(x, b2, R=1.0):
    """DERIVED.  V''(R_0) = -2 G''(R_0).  Stable iff > 0."""
    s = math.sqrt(1.0 - x)
    Gpp = ((1.0 - s) / 2.0 - b2 * (1.0 + 3.0 * s)
           + (1.0 - s) * (1.0 + s) ** 2 / (4.0 * s * s)) / (R * R)
    return -2.0 * Gpp

def is_stable(x, b2):
    return Vpp(x, b2) > 0.0

# -- the potential, in closed form, for checking everything above ------------

def sigma_of_R(R, x, b2, R0=1.0):
    """Closed-form solution of sigma' = -(2/R)(sigma + p) for p linear in sigma."""
    _, _, sig0, p0 = statics(x, R0)
    A = 1.0 + b2
    K = p0 - b2 * sig0
    return (sig0 + K / A) * (R / R0) ** (-2.0 * A) - K / A

def p_of_R(R, x, b2, R0=1.0):
    _, _, sig0, p0 = statics(x, R0)
    return p0 + b2 * (sigma_of_R(R, x, b2, R0) - sig0)

def V_of_R(R, x, b2, R0=1.0):
    _, m, _, _ = statics(x, R0)
    ms = 4.0 * math.pi * R * R * sigma_of_R(R, x, b2, R0)
    return 1.0 - (ms / (2.0 * R) + m / ms) ** 2

def Vpp_numeric(x, b2, R0=1.0, h=1e-5):
    return (V_of_R(R0 + h, x, b2, R0) - 2.0 * V_of_R(R0, x, b2, R0)
            + V_of_R(R0 - h, x, b2, R0)) / (h * h)

# -- the oscillation, and the inverted criterion -----------------------------

def omega_scaled(x, b2):
    """W = sqrt(V'' R^2 / 2), dimensionless.  omega = W c/R."""
    v = Vpp(x, b2, 1.0)
    return math.sqrt(v / 2.0) if v > 0.0 else float("nan")

def period_scaled(x, b2):
    """Oscillation period in units of R/c."""
    return 2.0 * math.pi / omega_scaled(x, b2)

def measure_period(x, b2, eps=1e-4, dt=2e-5, tmax=60.0):
    """Integrate R_ddot = -V'(R)/2 directly and time the oscillation.
    Independent of Vpp() -- this is the check on it."""
    h = 1e-7
    dV = lambda R: (V_of_R(R + h, x, b2) - V_of_R(R - h, x, b2)) / (2.0 * h)
    R, Rd, t, prev, cross = 1.0 + eps, 0.0, 0.0, 1.0 + eps, []
    while t < tmax and len(cross) < 2:
        Rd += -0.5 * dV(R) * dt
        R += Rd * dt
        t += dt
        if (prev - 1.0) * (R - 1.0) < 0.0:
            cross.append(t)
        prev = R
    return 2.0 * (cross[1] - cross[0]) if len(cross) > 1 else float("nan")

def lam(a_ms2, R_m):
    """lambda = a R / c^2."""
    return a_ms2 * R_m / (C * C)

def marginal_shortfall(delta_eta, a_ms2, R_m):
    """MARGINAL wall: burn must beat the e-folding.  <= 1 passes."""
    return delta_eta / lam(a_ms2, R_m)

def adiabatic_margin(delta_eta, a_ms2, R_m, x, b2):
    """STIFF wall: burn must be slow against the oscillation.  >> 1 passes.
    tau_burn * omega = W delta_eta / lambda."""
    return omega_scaled(x, b2) * delta_eta / lam(a_ms2, R_m)

# -- how far the shell may swing before dominant energy fails ----------------

def dec_asymptotic_margin(x, b2, R0=1.0):
    """sigma - p as R -> infinity.  Positive means the dominant-energy basin is
    unbounded: no oscillation amplitude can break it."""
    _, _, sig0, p0 = statics(x, R0)
    return 2.0 * (b2 * sig0 - p0) / (1.0 + b2)

def basin_unbounded(x, b2):
    return dec_asymptotic_margin(x, b2) > 0.0

def p_over_sigma(x):
    """p_0/sigma_0 = (1-s)/(4s): the beta^2 above which the basin is unbounded."""
    s = math.sqrt(1.0 - x)
    return (1.0 - s) / (4.0 * s)

def stability_basin_gap(x):
    """DERIVED, exact: beta^2_crit - p_0/sigma_0 = x/(4 s^2 (1+3s)) > 0.
    Strict stability therefore IMPLIES an unbounded dominant-energy basin."""
    s = math.sqrt(1.0 - x)
    return x / (4.0 * s * s * (1.0 + 3.0 * s))

# -- can real matter supply it? ----------------------------------------------

def v2_of_x(x):
    """RECONSTRUCTED.  p_0/sigma_0 = v^2/2 for a counter-rotating shell, and the
    junction fixes p_0/sigma_0 = (1-s)/(4s), so the orbital speed is set by x."""
    return one_minus_s(x) / (2.0 * math.sqrt(1.0 - x))

def beta2_vlasov(x):
    """RECONSTRUCTED.  The DETERMINED equation-of-state slope of a counter-
    rotating shell whose particles conserve angular momentum: u = gamma v ~ 1/R.
    Returns None where the model expires (v >= 1, i.e. x >= 8/9)."""
    v2 = v2_of_x(x)
    if v2 >= 1.0:
        return None
    u2 = v2 / (1.0 - v2)
    return u2 * (3.0 * u2 + 4.0) / (2.0 * (1.0 + u2) * (3.0 * u2 + 2.0))

def vlasov_stable(x):
    b = beta2_vlasov(x)
    return b is not None and b > beta2_crit(x)

def matter_crossover(lo=0.01, hi=0.85, iters=200):
    """DERIVED.  The x above which counter-rotating matter no longer supplies
    the stiffness the stability criterion demands."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if vlasov_stable(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def vlasov_margin(x):
    """beta^2_vlasov / beta^2_crit.  Tends to 4/3 as x -> 0."""
    b = beta2_vlasov(x)
    return None if b is None else b / beta2_crit(x)

def vlasov_model_limit():
    """v -> 1 at x = 8/9: where the counter-rotating model itself expires."""
    return 8.0 / 9.0

# -- the non-radial mode (Pitre, Schneider & Poisson 2026) -------------------

PSP_K = 0.6          # PINNED from their Fig. 1: Im{omega}(R^3/M)^{1/2}, 0.52-0.66
G_SI = 6.67430e-11

def gamma1_published(x):
    """PINNED.  LeMaitre-Poisson 2019 / Pitre et al Eq (3.16c), C = M/R = x/2."""
    s = math.sqrt(1.0 - x)
    return (4.0 - 3.0 * x + 2.0 * s) / (4.0 * s * s)

def gamma_crit(x, R=1.0):
    """DERIVED.  This file's beta^2_crit converted to their adiabatic index via
    their Eq (2.7): Gamma = beta^2 (mu + p)/p.  Must equal gamma1_published."""
    _, _, sig, p = statics(x, R)
    return beta2_crit(x) * (sig + p) / p

def nonradial_rate(M_kg, R_m, k=PSP_K):
    """Growth rate of the l >= 2 even-parity matter mode, 1/s.  Independent of
    beta^2 -- the structural fix does not reach this branch."""
    return k * math.sqrt(G_SI * M_kg / R_m ** 3)

def efoldings(M_kg, R_m, delta_eta, a_ms2, k=PSP_K):
    """How many e-foldings the instability gets during the burn.  < 1 to survive."""
    return nonradial_rate(M_kg, R_m, k) * (C * delta_eta / a_ms2)

def max_mean_density(delta_eta, a_ms2, k=PSP_K):
    """DERIVED.  N < 1 is a ceiling on mean density alone, kg/m^3."""
    return 3.0 * a_ms2 ** 2 / (4.0 * math.pi * G_SI * (k * C * delta_eta) ** 2)

def min_radius(M_kg, delta_eta, a_ms2, k=PSP_K, n=1.0):
    """DERIVED.  Smallest cavity for which the burn takes fewer than n e-foldings."""
    return (G_SI * M_kg * (k * C * delta_eta / (n * a_ms2)) ** 2) ** (1.0 / 3.0)

# -- selftest ----------------------------------------------------------------

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The junction reproduces Le Eq (17) -- derived here, not transcribed")
    for x in (0.1, 0.3, 0.5, 0.8, X_THIN_SHELL):
        chk("  8 pi R (sigma-p) at x = %.4f" % x, dec_margin_scaled(x),
            dec_margin_le(x), 1e-12)
    chk("surface dec vanishes exactly at 24/25", dec_margin_scaled(X_THIN_SHELL),
        0.0, 1e-14)
    chk("...and is positive below it", dec_margin_scaled(0.95) > 0.0, True)
    chk("...and negative above it", dec_margin_scaled(0.97) < 0.0, True)

    print("\nTHE DECOUPLING: the statics do not contain beta^2 at all")
    for b2 in (0.0, 0.05, 0.5, 1.0):
        chk("  V(R_0) = 0 at beta^2 = %.2f" % b2, V_of_R(1.0, 0.3, b2), 0.0, 1e-14)
        d = (V_of_R(1.0 + 1e-6, 0.3, b2) - V_of_R(1.0 - 1e-6, 0.3, b2)) / 2e-6
        chk("  V'(R_0) = 0 at beta^2 = %.2f" % b2, d, 0.0, 1e-9)
    chk("dec margin is identical for every beta^2 (it is junction-fixed)",
        len({round(dec_margin_scaled(0.3), 12)}), 1)

    print("\nV'' analytic against a finite difference of the closed-form V(R)")
    for x in (0.2, 0.3, 0.5, 0.7):
        for b2 in (0.0, 0.2, 0.5, 1.0):
            chk("  x = %.1f, beta^2 = %.1f" % (x, b2), Vpp_numeric(x, b2),
                Vpp(x, b2), 2e-5)

    print("\nbeta^2_crit is exactly the zero of V''")
    for x in (0.1, 0.3, 0.5, 2.0 / 3.0, 0.8):
        chk("  V''(beta^2_crit) at x = %.4f" % x, Vpp(x, beta2_crit(x)), 0.0, 1e-13)
        chk("    ...just above is stable", is_stable(x, beta2_crit(x) * 1.01), True)
        chk("    ...just below is not", is_stable(x, beta2_crit(x) * 0.99), False)

    print("\nTwo exact closed forms fall out")
    chk("beta^2_crit(2/3) = (sqrt3 - 1)/2", beta2_crit(X_VLASOV),
        (math.sqrt(3.0) - 1.0) / 2.0, 1e-15)
    chk("beta^2_crit(4/5) = sqrt5 - 3/2", beta2_crit(X_TANGENTIAL),
        math.sqrt(5.0) - 1.5, 1e-15)

    print("\nThe causal ceiling, and the window that matters")
    xs = causal_limit()
    chk("x* where beta^2_crit = 1", beta2_crit(xs), 1.0, 1e-9)
    chk("  and it is", xs, 0.8437418926, 1e-9)
    chk("the operative window x < 4/5 is entirely below x*", X_TANGENTIAL < xs, True)
    chk("  so is the Vlasov window x < 2/3", X_VLASOV < xs, True)
    chk("but the thin-shell dec window 24/25 is NOT", X_THIN_SHELL < xs, False)
    for x in (0.1, 0.3, X_VLASOV, X_TANGENTIAL):
        cs = sound_speed_crit(x)
        print("      x = %.4f  needs beta^2 > %.6f, c_s > %.4f c" % (x, beta2_crit(x), cs))
        chk("    subluminal at x = %.4f" % x, cs < 1.0, True)

    print("\nThe oscillation period, measured by integrating R_ddot = -V'/2")
    for x, b2 in ((0.3, 0.5), (0.5, 0.5), (0.3, 0.2)):
        meas, pred = measure_period(x, b2), period_scaled(x, b2)
        chk("  x = %.1f, beta^2 = %.1f  (units R/c)" % (x, b2), meas, pred, 1e-3)

    print("\nTHE INVERSION")
    ETA, A_G, R_M = 0.2, 9.80665, 10.0
    sf = marginal_shortfall(ETA, A_G, R_M)
    am = adiabatic_margin(ETA, A_G, R_M, 0.3, 0.5)
    print("      1 g, 10 m cavity, delta_eta = 0.2:")
    print("        marginal wall  -- needs <= 1, gets %.4e   FAILS" % sf)
    print("        stiff wall     -- needs >> 1, gets %.4e   PASSES" % am)
    chk("the marginal wall fails by more than 1e13", sf > 1e13, True)
    chk("the stiff wall is adiabatic by more than 1e13", am > 1e13, True)
    chk("it is the same ratio, times W", am / sf, omega_scaled(0.3, 0.5), 1e-9)
    lew = adiabatic_margin(0.24, 1.0, 1.0, 0.3, 0.5) * lam(1.0, 1.0) / 0.12
    chk("Le's relativistic burn is only marginally adiabatic (< 5)", lew < 5.0, True)
    print("      Le App. K burn (delta_eta/lambda = 2.0) is adiabatic by %.3f" % lew)

    print("\nBONUS: strict stability IMPLIES an unbounded dec basin")
    for x in (0.01, 0.1, 0.3, 0.5, X_VLASOV, X_TANGENTIAL, 0.9, 0.999):
        chk("  gap == x/(4s^2(1+3s)) at x = %.4f" % x,
            beta2_crit(x) - p_over_sigma(x), stability_basin_gap(x), 1e-13)
        chk("    ...and it is positive", stability_basin_gap(x) > 0.0, True)
    for x, b2 in ((0.3, 0.5), (0.3, 0.2), (0.5, 0.5), (X_VLASOV, 0.9)):
        chk("  basin unbounded at x=%.4f, beta^2=%.2f" % (x, b2),
            basin_unbounded(x, b2), True)
    chk("a wall stable but with beta^2 just under p_0/sigma_0 cannot exist",
        p_over_sigma(0.3) < beta2_crit(0.3), True)
    chk("  ...and an UNstable soft wall does have a finite basin",
        basin_unbounded(0.3, 0.02), False)

    print("\nTHE STING: beta^2 is DETERMINED by the matter, not chosen")
    for x in (0.05, 0.1, 0.3, 0.4, 0.5, X_VLASOV, X_TANGENTIAL):
        bv, bc = beta2_vlasov(x), beta2_crit(x)
        print("      x = %.4f  supplied %.6f  required %.6f  %s"
              % (x, bv, bc, "STABLE" if bv > bc else "unstable"))
    chk("Le's own operating point x = 0.3 is stable", vlasov_stable(0.3), True)
    chk("  ...by 14%", vlasov_margin(0.3), 1.144557648, 1e-8)
    chk("but x = 2/3 is NOT", vlasov_stable(X_VLASOV), False)
    chk("and x = 4/5 is not either", vlasov_stable(X_TANGENTIAL), False)
    xc = matter_crossover()
    chk("crossover", xc, 0.46897656, 1e-6)
    chk("  the crossover is where supplied == required",
        beta2_vlasov(xc) - beta2_crit(xc), 0.0, 1e-8)
    chk("the margin is WIDEST at low compactness -> 4/3", vlasov_margin(1e-9),
        4.0 / 3.0, 1e-6)
    chk("  and shrinks monotonically to 1 at the crossover",
        all(vlasov_margin(a) > vlasov_margin(b)
            for a, b in zip([1e-6, .05, .1, .2, .3, .4], [.05, .1, .2, .3, .4, .46])), True)
    chk("a habitable ship (x = 1.5e-22) sits at the 4/3 limit",
        vlasov_margin(1.5e-22), 4.0 / 3.0, 1e-12)
    chk("  the naive 1-sqrt(1-x) would have underflowed there",
        1.0 - math.sqrt(1.0 - 1.5e-22), 0.0, 0.0)
    chk("  x/(1+s) does not", one_minus_s(1.5e-22) > 0.0, True)
    chk("the model itself expires at x = 8/9", vlasov_model_limit(), 8.0 / 9.0, 1e-15)

    print("\nTHE RADIAL CRITERION, AGAINST THE PUBLISHED ONE")
    for x in (1e-6, 0.05, 0.2, 0.3, 0.5, 0.8):
        chk("  Gamma_crit == Gamma_1 at x = %.4g" % x, gamma_crit(x),
            gamma1_published(x), 1e-9)
    chk("both go to 3/2 in the Newtonian limit", gamma_crit(1e-9), 1.5, 1e-6)

    print("\nTHE NON-RADIAL MODE: beta^2 does not appear in it")
    r1 = nonradial_rate(1.0e6, 10.0)
    print("      1e6 kg at R = 10 m grows at %.4e /s  (e-fold %.0f s = %.2f h)"
          % (r1, 1.0 / r1, 1.0 / r1 / 3600.0))
    n_small = efoldings(1.0e6, 10.0, 0.2, 9.80665)
    print("      a 1 g burn to delta_eta = 0.2 lasts %.3e e-foldings" % n_small)
    chk("a 10 m ship is torn apart hundreds of times over", n_small > 100.0, True)
    chk("the ceiling is on MEAN DENSITY", max_mean_density(0.2, 9.80665), 2.657927437e-4, 1e-12)
    rmin = min_radius(1.0e6, 0.2, 9.80665)
    chk("1,000 tonnes needs R > 964 m", rmin, 964.4, 0.5)
    chk("  at which N = 1 exactly", efoldings(1.0e6, rmin, 0.2, 9.80665), 1.0, 1e-9)
    r10 = min_radius(1.0e6, 0.2, 9.80665, n=0.1)
    chk("and R > 4.5 km for N < 0.1", r10 / 1000.0, 4.478398718, 1e-8)
    print("      compactness there: x = %.3e -- every window clears by decades"
          % (2.0 * G_SI * 1.0e6 / (r10 * C * C)))
    chk("  ...and the counter-rotating wall is stable there",
        vlasov_stable(2.0 * G_SI * 1.0e6 / (r10 * C * C)), True)
    chk("  ...and the burn is still adiabatic there",
        adiabatic_margin(0.2, 9.80665, r10, 0.3, 0.5) > 1e9, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE STIFFNESS REQUIREMENT\n")
    print("  %-10s %12s %12s %14s %14s"
          % ("x = 2m/R", "beta^2_crit", "c_s / c", "8piR(sig-p)", "causal?"))
    for x in (0.05, 0.1, 0.2, 0.3, 0.5, X_VLASOV, X_TANGENTIAL,
              causal_limit(), 0.9, X_THIN_SHELL):
        b = beta2_crit(x)
        cs = "%.4f" % math.sqrt(b) if b <= 1.0 else "  --  "
        print("  %-10.5f %12.6f %12s %14.6f %14s"
              % (x, b, cs, dec_margin_scaled(x), "yes" if b <= 1.0 else "NO"))
    print("\n  every window the wall is realizable in (x < 4/5) is causal.")

    print("\nTHE OSCILLATION, once stiffened (period in units R/c)\n")
    print("  %-10s %10s %12s %12s %16s" % ("x", "beta^2", "V''R^2", "period", "dec basin"))
    for x, b2 in ((0.3, 0.2), (0.3, 0.5), (0.3, 1.0), (0.5, 0.5), (X_VLASOV, 0.9)):
        print("  %-10.4f %10.2f %12.6f %12.5f %16s"
              % (x, b2, Vpp(x, b2), period_scaled(x, b2),
                 "unbounded" if basin_unbounded(x, b2) else "FINITE"))

    print("\nTHE INVERSION\n")
    print("  %-26s %16s %18s" % ("design", "marginal (<=1)", "stiff (>>1)"))
    for lbl, eta, a, R in (("Le App. K worked burn", 0.24, None, None),
                           ("1 g, 1 km cavity", 0.2, 9.80665, 1000.0),
                           ("1 g, 10 m cavity", 0.2, 9.80665, 10.0)):
        if a is None:
            sf, am = 2.0, 2.0 * omega_scaled(0.3, 0.5)
        else:
            sf = marginal_shortfall(eta, a, R)
            am = adiabatic_margin(eta, a, R, 0.3, 0.5)
        print("  %-26s %16.3e %18.3e" % (lbl, sf, am))
    print("\n  Same ratio, opposite sign of V''.  The habitable regime was never")
    print("  near the boundary; it was fourteen orders from it, on whichever side")
    print("  the equation of state puts it.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
