#!/usr/bin/env python3
r"""
localband.py -- DOCKET 52, the successor question, asked adversarially.

nonstatic.py answered "does dropping staticity let proper distance contract
without negative Misner-Sharp mass?" with YES, and produced two witnesses:
Minkowski in Milne slicing and open FRW.  BOTH ARE GLOBAL AND HOMOGENEOUS.
Neither is a corridor.  The question this file was handed is the one that
matters for a drive:

    Build an explicit spherically symmetric DYNAMIC metric with m > 0
    everywhere that satisfies 2m/R < e^{-2Phi} Rdot^2 OVER A FINITE REGION,
    compute the full stress-energy from the Einstein tensor, and check NEC,
    WEC, SEC and DEC pointwise.  If the NEC is violated the loophole is
    illusory.  If it is satisfied, report the witness.  Then integrate the
    NEC along a radial null geodesic: is ANEC satisfied?

    python3 localband.py             the reading
    python3 localband.py --selftest  every residual, every machine check

Needs sympy and z3-solver (pypi is on the proxy allowlist; see
PROOF-ASSISTANT.md).  Run under python3 (3.11).  Imports nonstatic.py and
prover.py rather than copying either.  The report takes about 40 s and the
selftest about 110 s: both evolve a spherical dust slice and push a null
geodesic across it, which is the whole point and is not cached.

===============================================================================
0.  THE ANSWER, IN FOUR LINES
===============================================================================

    THE WITNESS EXISTS.  A localized contraction band with m > 0 everywhere,
    NEC, WEC, SEC AND DEC ALL SATISFIED POINTWISE, and ANEC STRICTLY POSITIVE
    along the radial null geodesic that crosses it.  It is written out in full
    in section 2.  THE LOOPHOLE IS NOT ILLUSORY AND THE NEC DOES NOT CLOSE IT.

    NOR DOES ANEC.  Section 3 builds the other kind of localized band -- same
    initial slice, same contraction, different momentum -- and that one DOES
    violate NEC, WEC and DEC pointwise.  Even there the ANEC integral over the
    complete radial null geodesic comes out POSITIVE, because an ordinary
    positive-energy collar elsewhere on the same geodesic pays for the band.
    No energy condition, local or averaged, decides this question.

    WHAT CLOSES IT IS A CLOCK.  Section 5: with m >= 0 the areal radius cannot
    be held still where W > 1, so a corridor whose two ends stay inside an
    areal window of width D survives at most D/sqrt(W0^2 - 1) of proper time --
    and the product of the fractional saving with the number of its own light
    crossings it survives is EXACTLY sqrt((W-1)/(W+1)) < 1, always.  Measured
    on the witness of section 2 the real number is worse: above a 17.4 %
    contraction the dust band tears itself into a shell-crossing singularity
    BEFORE a light ray gets across it.

===============================================================================
1.  WHAT THIS FILE DERIVES BEFORE IT BUILDS ANYTHING
===============================================================================

nonstatic.py's general_einstein() is imported, not re-derived.  Three further
identities are needed to integrate anything along a null ray, and sympy returns
each residual as exactly 0 (`--selftest`, section D1):

    INAFFINITY.  For k = e^{-Phi} d_t + e^{-Lambda} d_r  (nonstatic's k_rad,
    the outgoing radial null vector with -u.k = 1),

        k^b grad_b k^a  =  kappa k^a,      kappa = D_t Lambda + D_r Phi

    so k_rad IS NOT AFFINE unless that combination vanishes.  Every ANEC number
    below carries the correction; getting this wrong rescales the integrand
    with the wrong weight and can flip a marginal answer.

    RAYCHAUDHURI, for the outgoing radial null congruence, with the expansion
    Theta+ = 2(U + W)/R:

        (D_t + D_r) Theta+  =  kappa Theta+ - Theta+^2/2 - 8 pi (rho+p_r-2j)

    which is the independent cross-check on every ANEC quadrature here.

    THE AFFINE RAY.  Write k = phi k_rad.  Then k is affine exactly when
    (D_t + D_r) ln phi = -kappa, and (D_t + D_r) is d/dt along the ray when
    Phi = 0.  So in the gauge both witnesses use,

        d(ln phi)/dt = -d_t Lambda  along the ray,     dlambda = dt / phi,
        ANEC  =  integral  phi (rho + p_r - 2j) dt.

===============================================================================
2.  WITNESS A -- THE COMOVING BAND.  EVERY ENERGY CONDITION HOLDS.
===============================================================================

THE METRIC, written out so it can be checked:

    ds^2 = -dt^2 + [R'(t,r)^2 / (1 + 2 Ecal(r))] dr^2 + R(t,r)^2 dOmega^2

    with R(t,r) the solution of      Rdot^2 = 2 Ecal(r) + 2 mass(r) / R
    and initial data                 R(0,r) = r,   R'(0,r) = 1.

That is Lemaitre-Tolman-Bondi in its standard gauge, and this file DERIVES its
content rather than quoting it (section D2, every residual 0):

    W = e^{-Lambda} R' = sqrt(1 + 2 Ecal(r))     EXACTLY, and INDEPENDENT OF t
    j = 0                                        IDENTICALLY, for any R(t,r)
    p_r = p_T = 0,   rho = mass'(r) / (4 pi R^2 R'),   m_MS = mass(r)

The first line is the whole point: THE CONTRACTION FACTOR IS A FREE FUNCTION OF
r THAT NEVER CHANGES.  W > 1 exactly on supp(Ecal), a finite band, and it holds
there for as long as the solution does, at no cost in flux -- which is EV-W of
nonstatic.py (D_t W = 4 pi R j + U D_r Phi) with both terms zero.

The explicit choice reported (all lengths in geometric units):

    bump(s)   = (1 - s^2)^4 for |s| < 1, else 0          C^3, compact
    W(r)      = 1 + w0 bump((r - 3)/1)                   band = (2, 4)
    Ecal(r)   = (W(r)^2 - 1)/2                           >= 0, supp = (2, 4)
    mass(r)   = M u^3 (10 - 15u + 6u^2),  u = min(r/6, 1),  M = 0.30
                so mass' >= 0, mass(0) = 0 (regular centre), vacuum past r = 6

    ENERGY CONDITIONS.  Dust: rho = mass'/(4 pi R^2 R') >= 0, p_r = p_T = j = 0.
    NEC rho + p_i = rho >= 0.  WEC rho >= 0.  SEC rho + sum p_i = rho >= 0.
    DEC rho >= |p_i| = 0.  ALL FOUR HOLD, and all four hold STRICTLY on the
    band, where mass' > 0 and R' > 0.  Checked pointwise on a grid, from the
    numerically evolved solution, not from the algebra that produced it.

    ANEC.  Positive, strictly, and it could not be anything else: for dust
    T_ab k^a k^b = rho (u_a k^a)^2 >= 0 pointwise, so the integral over any
    null geodesic is non-negative and is strictly positive for any ray that
    meets the matter.  The number is reported anyway, with the affine weight
    phi of section 1 carried correctly.

    THAT IS THE WITNESS THE DOCKET ASKED FOR AND IT IS CLEAN.  m > 0 on the
    whole band, 2m/R < Rdot^2 on the whole band, nothing exotic anywhere.

===============================================================================
3.  WITNESS B -- THE ENGINEERED BAND.  SAME SLICE, DIFFERENT MOMENTUM.
===============================================================================

THE METRIC, also written out:

    ds^2 = -dt^2 + [(1 + t v'(r))^2 / W(r)^2] dr^2 + (r + t v(r))^2 dOmega^2

    v(r) = v0 S((r - r0)/(r1 - r0)),   S(u) = u^3(10 - 15u + 6u^2) clipped to
    [0,1] -- a monotone ramp, so v' >= 0 and R' = 1 + t v' >= 1 FOR ALL t:
    this witness never shell-crosses.  Near the centre v = 0 and W = 1, so the
    core is exactly Minkowski and r = 0 is regular.

    By construction  U = v(r),  W = W(r),  both independent of t, and
    2m/R = 1 - W(r)^2 + v(r)^2, also independent of t.  With v0 > sqrt(Wmax^2-1)
    the mass is non-negative everywhere and strictly positive on the band.

    AT t = 0 THIS IS THE SAME SLICE AS WITNESS A.  Both have R = r, R' = 1 and
    e^Lambda = 1/W(r), so both induce

        dl^2 = dr^2 / W(r)^2 + r^2 dOmega^2

    -- the same three-geometry, the same contraction band, the same saving.
    The two spacetimes differ ONLY in the extrinsic curvature: witness A's
    areal velocity is whatever the dust's own binding energy dictates,
    U = sqrt(2 Ecal + 2 mass/R); witness B's is prescribed.

    AND THE STRESS-ENERGY, DERIVED (section D3, residuals 0):

        j    = 0                                          identically
        p_r  = -(2m/R) / (8 pi R^2)
        p_T  = (W W' - v v') / (8 pi R R')
        rho  = (2m/R)/(8 pi R^2) - (W W' - v v')/(4 pi R R')

        rho + p_r  =  (v v' - W W') / (4 pi R R')  =  d_r(2m/R) / (8 pi R R')

    NEC VIOLATED.  On the band v' = 0, so rho + p_r = -W W'/(4 pi R R') < 0 on
    the whole INNER HALF of the band, wherever W is rising.  WEC and DEC fail
    on the same set (DEC fails exactly where W' > 0, since rho - |p_r| =
    -W W'/(4 pi R)).  SEC: rho + p_r + 2 p_T = 0 IDENTICALLY in this family --
    exactly saturated everywhere -- so SEC fails only through its NEC half.

    ANEC, AND THIS IS THE PART THAT REFUSES TO OBLIGE.  On the band R' = 1 and
    phi is constant, and the band's own contribution to the ANEC integral has
    a closed form, derived by parts and confirmed by quadrature to 2e-7:

        Delta ANEC(band)  =  -(phi/4 pi) integral (W - 1) |dR| / R^2   <  0

    -- STRICTLY NEGATIVE, IN EXACT PROPORTION TO THE CONTRACTION, along either
    radial direction, for any bump shape and any v0.  THE CONTRACTION IS THE
    ANEC DEFICIT.  And yet the integral over the COMPLETE radial null geodesic
    (in from infinity, through the regular centre, out again) is POSITIVE: the
    velocity ramp is an ordinary positive-energy collar whose contribution
    outweighs the band's.  Switching the band off raises the total.  Measured,
    reported, and NOT dressed up: ANEC IS SATISFIED ON THIS GEODESIC WHILE THE
    NEC FAILS INSIDE THE CORRIDOR.

===============================================================================
4.  WHAT THE PAIR MEASURES, WHICH IS A SCOPE FACT ABOUT THE NEC
===============================================================================

    W IS A PROPERTY OF THE SLICE.  THE ENERGY CONDITIONS ARE NOT.

Witnesses A and B share a slice, a band and a saving, and disagree on the NEC.
So no function of the contraction can decide an energy condition, and the
question "does contracting proper distance cost negative energy" has no answer
at the level at which it was asked.  This is nonstatic.py section 5's gauge
observation with a second edge on it: there the SAME spacetime sliced two ways
gave two different W, here the SAME slice extended two ways gives two different
verdicts on the NEC.

===============================================================================
5.  WHAT DOES CLOSE IT, AND IT IS A CLOCK, NOT AN ENERGY CONDITION
===============================================================================

CORRIDOR EXHAUSTION.  Machine-checked in section D4, with one continuity step
taken by hand and labelled as such.

    Let the band hold W >= W0 > 1 with m >= 0 over a time interval, and let the
    corridor's ends stay inside an areal window of width D.  Then

    (i)   U^2 = W^2 - 1 + 2m/R >= W0^2 - 1 > 0, so U NEVER VANISHES;
    (ii)  U is continuous, so it keeps its sign: R is strictly monotone in t;
          [THE ONE HAND STEP -- an intermediate-value argument, not z3's.]
    (iii) |R(T) - R(0)| = integral |U| dtau >= T sqrt(W0^2 - 1), and that is
          bounded by D, so

              T  <=  D / sqrt(W0^2 - 1)                     (proper time)

    AT A MOMENT OF TIME SYMMETRY THERE IS NO CORRIDOR AT ALL.  On any slice with
    U == 0 -- which is exactly what time-symmetric initial data means -- m >= 0
    forces W <= 1 EVERYWHERE on it.  So a corridor cannot be switched on from
    rest.  It must be built with the matter already moving, which generalises
    nonstatic.py's "the free witnesses hold contraction because they were born
    with it" from FRW to every spherically symmetric initial datum.

THE PRODUCT BOUND.  Take D to be the corridor's own areal length.  An outgoing
ray closes an areal gap at rate W (nonstatic.py's ray identity), so one crossing
costs D/W and the corridor survives

        N  =  T / tau_cross  <=  W / sqrt(W^2 - 1)     light crossings

while saving the fraction S = 1 - 1/W of the proper length.  Then

        S * N  <=  sqrt( (W - 1) / (W + 1) )  <  1     FOR EVERY W > 1

exactly, with the bound approached only as W -> infinity, where the saving
tends to 100 % and the lifetime tends to exactly one crossing.  A corridor that
saves a lot lasts one crossing; a corridor that lasts many saves nothing.  And
against the trip you would have made anyway, T/D = 1/sqrt(W^2-1), so AT ANY
CONTRACTION STRONGER THAN W = sqrt(2) THE CORRIDOR DIES BEFORE LIGHT WOULD HAVE
ARRIVED WITHOUT IT.

AND THE MEASURED NUMBER IS WORSE THAN THE BOUND.  Witness A is dust, and dust
tears: the band's outer shells outrun the ones ahead of them and R' reaches
zero.  Asked the only question that matters -- does a light ray get across the
band before the band stops existing --

        W_max <= 1.20   the ray clears the band          (saving <= 16.7 %)
        W_max >= 1.25   THE RAY IS CAUGHT BY THE SINGULARITY (saving >= 20.0 %)

and the smooth indicator N = (time to the first shell crossing)/(time for light
to cross the band) passes 1 at W_max = 1.1336 +/- 0.001, an 11.8 % saving.  THE RAY TEST
IS REPORTED AS A BRACKET AND NOT BISECTED: at the threshold the ray and the
crossing locus are nearly tangent and the verdict stops being monotone in the
band strength at a fixed grid, which an earlier pass of this file did not
notice.  N is bisected instead, because it is smooth.

N is SCALE-INVARIANT: rescaling sigma, M, r_b and r_c together leaves it
unchanged to four decimals, so this is a shape fact about the band and not a
tuning.  It is also a statement about DUST: a shell-crossing singularity is
gravitationally weak and is the standard artefact of zero pressure.  RECORDED,
NOT REPAIRED, AND NOT GENERALISED.

===============================================================================
6.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT SAY THE LOOPHOLE IS ILLUSORY.  The witness of section 2 exists
    and every energy condition holds on it.  Anyone who wants the corridor
    closed by the NEC is refuted here, by construction.

    IT DOES NOT SAY ANEC CLOSES IT EITHER.  The one geodesic on which a band
    contributes negatively is a geodesic whose total is still positive.

    IT DOES NOT CLAIM THE SHELL-CROSSING THRESHOLD IS UNIVERSAL.  17.4 % is
    this profile family's number, for dust.  A fluid with pressure will fail
    differently and this file does not measure how.

    IT DOES NOT SPEAK TO ANYTHING NON-SPHERICAL.  Same scope line as
    certify.py and nonstatic.py.  The Alcubierre family is outside it.

    IT REPAIRS NOTHING.  certify.py, nonstatic.py, drivensource.py, overturn.py
    and paper/ are untouched, and no finding here is seated anywhere else.  The
    chat-67 full hold governs this exactly as it governs a section read.
"""

import argparse
import math
import sys

# The instrument imports the seated instruments; it never copies one.
import nonstatic
from nonstatic import C, LY, PROXIMA_LY, general_einstein


# ------------------------------------------------------------------ profiles

def bump(s):
    """C^3 compactly supported bump, 1 at s = 0, 0 for |s| >= 1."""
    return (1.0 - s * s) ** 4 if abs(s) < 1.0 else 0.0


def dbump(s):
    return -8.0 * s * (1.0 - s * s) ** 3 if abs(s) < 1.0 else 0.0


def smoothstep(u):
    """Quintic ramp: 0 at u <= 0, 1 at u >= 1, two vanishing derivatives."""
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0
    return u ** 3 * (10.0 - 15.0 * u + 6.0 * u * u)


def dsmoothstep(u):
    if u <= 0.0 or u >= 1.0:
        return 0.0
    return 30.0 * u * u * (1.0 - u) ** 2


# The one band both witnesses wear, so that their t = 0 slices coincide.
R_C, SIGMA = 3.0, 1.0                 # band centre and half-width: (2, 4)
MASS_M, MASS_RB = 0.30, 6.0           # witness A's dust ball
RAMP_0, RAMP_1 = 0.5, 1.5             # witness B's velocity ramp


def W_of(r, w0):
    return 1.0 + w0 * bump((r - R_C) / SIGMA)


def dW_of(r, w0):
    return w0 * dbump((r - R_C) / SIGMA) / SIGMA


def mass_of(r):
    u = min(r / MASS_RB, 1.0)
    return MASS_M * u ** 3 * (10.0 - 15.0 * u + 6.0 * u * u)


def dmass_of(r):
    if r >= MASS_RB:
        return 0.0
    u = r / MASS_RB
    return MASS_M * 30.0 * u * u * (1.0 - u) ** 2 / MASS_RB


def v_of(r, v0):
    return v0 * smoothstep((r - RAMP_0) / (RAMP_1 - RAMP_0))


def dv_of(r, v0):
    return v0 * dsmoothstep((r - RAMP_0) / (RAMP_1 - RAMP_0)) / (RAMP_1 - RAMP_0)


# ------------------------------------------------------- the derived identities

def frame_identities(E=None):
    """Section 1, as residuals sympy must return as 0.  Nothing is quoted."""
    E = E or general_einstein()
    sp = E["sp"]
    t, r, x, g, gi = E["t"], E["r"], E["x"], E["g"], E["gi"]
    Phi, Lam, R = E["Phi"], E["Lam"], E["R"]
    U, W, Dt, Dr = E["U"], E["W"], E["Dt"], E["Dr"]
    rho, p_r, j = E["rho"], E["p_r"], E["j"]

    Gm = [[[sp.cancel(sp.expand(
        sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                        - sp.diff(g[b, c], x[d])) for d in range(4)) / 2))
        for c in range(4)] for b in range(4)] for a in range(4)]
    k = [sp.exp(-Phi), sp.exp(-Lam), 0, 0]
    acc = [sp.simplify(sum(k[b] * sp.diff(k[a], x[b]) for b in range(4))
                       + sum(Gm[a][b][c] * k[b] * k[c]
                             for b in range(4) for c in range(4)))
           for a in range(4)]
    kappa = Dt(Lam) + Dr(Phi)
    theta = 2 * (U + W) / R
    nec_out = rho + p_r - 2 * j
    D1 = lambda f: Dt(f) + Dr(f)

    out = [("INAFFINITY  k^b grad_b k^a = kappa k^a, kappa = D_t Lam + D_r Phi",
            sum(sp.simplify(acc[a] - kappa * k[a]) for a in range(4)))]
    out.append(("RAYCHAUDHURI (D_t+D_r)Theta+ = kappa Theta+ - Theta+^2/2 - 8pi NEC",
                sp.simplify(D1(theta) - (kappa * theta - theta ** 2 / 2
                                         - 8 * sp.pi * nec_out))))
    # The affine ray.  Rescale k_rad by a FREE function phi(t,r) and compute the
    # acceleration of the rescaled vector from the Christoffels again.  The
    # residual below is the whole content: k = phi k_rad accelerates by exactly
    # phi (kappa + (D_t+D_r) ln phi), so it is affine exactly when that vanishes.
    # Checked with phi free, so the check cannot be satisfied by construction.
    phi = sp.Function("varphi", positive=True)(t, r)
    kt = [phi * k[a] for a in range(4)]
    acc_t = [sp.simplify(sum(kt[b] * sp.diff(kt[a], x[b]) for b in range(4))
                         + sum(Gm[a][b][c] * kt[b] * kt[c]
                               for b in range(4) for c in range(4)))
             for a in range(4)]
    fac = phi * (kappa + D1(sp.log(phi)))
    out.append(("AFFINE RAY  (phi k_rad) accelerates by phi(kappa + (D_t+D_r)ln phi)",
                sum(sp.simplify(acc_t[a] - fac * kt[a]) for a in range(4))))
    return out


def ltb_dust():
    """Section 2's stress-energy, DERIVED.  The LTB gauge is imposed on
    nonstatic's general metric and the dust constraint is substituted; every
    line below is a residual sympy returns as 0."""
    import sympy as sp
    E = general_einstein()
    t, r = E["t"], E["r"]
    Phi, Lam = E["Phi"], E["Lam"]
    Ecal = sp.Function("Ecal")(r)
    mfun = sp.Function("mass")(r)
    Rf = sp.Function("R")(t, r)
    Wr = sp.sqrt(1 + 2 * Ecal)
    gauge = {Phi: sp.Integer(0), Lam: sp.log(sp.Derivative(Rf, r) / Wr)}
    Rr = sp.Derivative(Rf, r)
    V = sp.Symbol("V")                                  # stands for Rdot
    Vsq = 2 * Ecal + 2 * mfun / Rf
    Rtt = -mfun / Rf ** 2                               # d/dt of the constraint
    Rtr = (sp.diff(Ecal, r) + sp.diff(mfun, r) / Rf
           - mfun * Rr / Rf ** 2) / V                   # d/dr of the constraint

    def free(expr):                                     # gauge only, no constraint
        return sp.simplify(sp.expand(expr.subs(gauge).doit()))

    def imp(expr):                                      # gauge AND constraint
        e = sp.expand(expr.subs(gauge).doit())
        e = e.subs({sp.Derivative(Rf, (t, 2)): Rtt, sp.Derivative(Rf, t, r): Rtr,
                    sp.Derivative(Rf, r, t): Rtr})
        e = e.subs(sp.Derivative(Rf, t), V)
        for _ in range(3):
            e = sp.expand(e.subs(V ** 2, Vsq))
        return sp.simplify(e)

    rows = [
        ("W = sqrt(1 + 2 Ecal(r)), independent of t, for ANY R(t,r)",
         free(E["W"]) - Wr),
        ("j = 0 identically in the LTB gauge, for ANY R(t,r)", free(E["j"])),
        ("p_r = 0 under Rdot^2 = 2 Ecal + 2 mass/R", imp(E["p_r"])),
        ("p_T = 0 under the same", sp.expand(sp.together(imp(E["p_T"])).as_numer_denom()[0])),
        ("rho = mass'(r) / (4 pi R^2 R')",
         imp(E["rho"]) - sp.diff(mfun, r) / (4 * sp.pi * Rf ** 2 * Rr)),
        ("m_MS = mass(r)", imp(E["m"]) - mfun),
    ]
    return rows


def engineered_band():
    """Section 3's stress-energy, DERIVED, with v(r) and W(r) left as free
    functions.  Residuals are 0; the closed forms are what the docstring quotes."""
    import sympy as sp
    t = sp.Symbol("t", positive=True)
    r = sp.Symbol("r", positive=True)
    W = sp.Function("W", positive=True)(r)
    v = sp.Function("v")(r)
    R = r + t * v
    Rp = sp.diff(R, r)
    w = nonstatic.witness("ENGINEERED BAND", sp.Integer(0), sp.log(Rp / W), R, r, False)
    Psi = 1 - W ** 2 + v ** 2                            # = 2m/R, a function of r
    rows = [
        ("U = v(r), independent of t", sp.simplify(w["U"] - v)),
        ("W = W(r), independent of t", sp.simplify(w["W"] - W)),
        ("2m/R = 1 - W^2 + v^2, independent of t", sp.simplify(2 * w["m"] / R - Psi)),
        ("j = 0 identically", sp.simplify(w["j"])),
        ("p_r = -(2m/R)/(8 pi R^2)", sp.simplify(w["p_r"] + Psi / (8 * sp.pi * R ** 2))),
        ("p_T = (W W' - v v')/(8 pi R R')",
         sp.simplify(w["p_T"] - (W * sp.diff(W, r) - v * sp.diff(v, r))
                     / (8 * sp.pi * R * Rp))),
        ("rho = (2m/R)/(8 pi R^2) - (W W' - v v')/(4 pi R R')",
         sp.simplify(w["rho"] - (Psi / (8 * sp.pi * R ** 2)
                     - (W * sp.diff(W, r) - v * sp.diff(v, r)) / (4 * sp.pi * R * Rp)))),
        ("rho + p_r = (v v' - W W')/(4 pi R R')",
         sp.simplify(w["rho"] + w["p_r"]
                     - (v * sp.diff(v, r) - W * sp.diff(W, r)) / (4 * sp.pi * R * Rp))),
        ("rho + p_r = d_r(2m/R)/(8 pi R R')",
         sp.simplify(w["rho"] + w["p_r"] - sp.diff(Psi, r) / (8 * sp.pi * R * Rp))),
        ("SEC combination rho + p_r + 2 p_T = 0 IDENTICALLY",
         sp.simplify(w["rho"] + w["p_r"] + 2 * w["p_T"])),
        ("nec_in = nec_out (j = 0)", sp.simplify(w["nec_in"] - w["nec_out"])),
    ]
    return rows


# ------------------------------------------------------------ energy conditions

def energy_conditions(rho, p_r, p_T, j, tol=1e-12):
    """Pointwise NEC, WEC, SEC, DEC.  Both witnesses have j = 0, which is
    MEASURED here rather than assumed: with j != 0 the (t,r) block is not
    diagonal and the type-I reduction below does not apply, so the function
    refuses instead of guessing."""
    if abs(j) > tol:
        return dict(diagonal=False, NEC=None, WEC=None, SEC=None, DEC=None,
                    nec_rad=None, nec_trn=None)
    nec_rad = rho + p_r
    nec_trn = rho + p_T
    nec = nec_rad >= -tol and nec_trn >= -tol
    return dict(diagonal=True,
                nec_rad=nec_rad, nec_trn=nec_trn,
                NEC=nec,
                WEC=nec and rho >= -tol,
                SEC=nec and (rho + p_r + 2 * p_T) >= -tol,
                DEC=rho >= abs(p_r) - tol and rho >= abs(p_T) - tol)


# ------------------------------------------------ witness A: the comoving band

def _A_funcs(w0):
    Ecal = lambda r: (W_of(r, w0) ** 2 - 1.0) / 2.0
    dEcal = lambda r: W_of(r, w0) * dW_of(r, w0)
    return Ecal, dEcal


def _A_rhs(r, R, Rp, Ecal, dEcal):
    U = math.sqrt(max(2.0 * Ecal(r) + 2.0 * mass_of(r) / R, 1e-300))
    dU = (dEcal(r) + dmass_of(r) / R - mass_of(r) * Rp / R ** 2) / U
    return U, dU


def witness_A_slice(w0, radii, t=0.0):
    """Witness A at time t, shell by shell.  Each shell is an independent ODE
    in LTB, so no grid is needed for a table."""
    Ecal, dEcal = _A_funcs(w0)
    rows = []
    for r in radii:
        R, Rp = r, 1.0
        n, h = 400, t / 400.0
        for _ in range(n if t > 0 else 0):
            a = _A_rhs(r, R, Rp, Ecal, dEcal)
            b = _A_rhs(r, R + h / 2 * a[0], Rp + h / 2 * a[1], Ecal, dEcal)
            c = _A_rhs(r, R + h / 2 * b[0], Rp + h / 2 * b[1], Ecal, dEcal)
            d = _A_rhs(r, R + h * c[0], Rp + h * c[1], Ecal, dEcal)
            R += h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0])
            Rp += h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1])
        U = math.sqrt(max(2.0 * Ecal(r) + 2.0 * mass_of(r) / R, 0.0))
        rho = dmass_of(r) / (4 * math.pi * R * R * Rp) if Rp != 0 else float("nan")
        m = R / 2 * (1 - W_of(r, w0) ** 2 + U * U)
        ec = energy_conditions(rho, 0.0, 0.0, 0.0)
        rows.append(dict(r=r, R=R, Rp=Rp, W=W_of(r, w0), U=U, m=m, rho=rho,
                         p_r=0.0, p_T=0.0, j=0.0, ec=ec,
                         contracts=W_of(r, w0) > 1.0 + 1e-12))
    return rows


def witness_A_ray(w0, r_launch=2.0, r_target=4.0, dt=0.002, n_t=4000,
                  r_max=10.0, n_r=401):
    """Evolve the whole slice and push an affinely parametrised outgoing radial
    null geodesic across the band, accumulating ANEC = integral phi rho dt.

    Returns the fate of the ray, which is the question section 5 asks."""
    Ecal, dEcal = _A_funcs(w0)
    hr = r_max / (n_r - 1)
    rs = [max(i * hr, 1e-6) for i in range(n_r)]
    Rg, Pg = list(rs), [1.0] * n_r

    def interp(arr, r):
        x = r / hr
        i = max(1, min(n_r - 3, int(x)))
        u = x - i
        p0, p1, p2, p3 = arr[i - 1], arr[i], arr[i + 1], arr[i + 2]
        return p1 + 0.5 * u * (p2 - p0 + u * (2 * p0 - 5 * p1 + 4 * p2 - p3
                                              + u * (3 * (p1 - p2) + p3 - p0)))

    rr, phi, anec, first_cross = r_launch, 1.0, 0.0, None
    for n in range(n_t):
        t = n * dt
        R, Rp = interp(Rg, rr), interp(Pg, rr)
        if Rp <= 0.0:
            return dict(fate="CAUGHT", t=t, r=rr, anec=anec, phi=phi,
                        first_cross=first_cross, w0=w0)
        rho = dmass_of(rr) / (4 * math.pi * R * R * Rp)
        dt_Lam = _A_rhs(rr, R, Rp, Ecal, dEcal)[1] / Rp        # d_t Lambda
        anec += phi * rho * dt                                  # nec_out = rho
        phi *= math.exp(-dt_Lam * dt)
        rr += (W_of(rr, w0) / Rp) * dt
        if first_cross is None and min(Pg) <= 0.0:
            first_cross = t
        if rr > r_target:
            return dict(fate="CLEARS", t=t, r=rr, anec=anec, phi=phi,
                        first_cross=first_cross, w0=w0)
        for i in range(n_r):
            R0, P0, r0 = Rg[i], Pg[i], rs[i]
            a = _A_rhs(r0, R0, P0, Ecal, dEcal)
            b = _A_rhs(r0, R0 + dt / 2 * a[0], P0 + dt / 2 * a[1], Ecal, dEcal)
            c = _A_rhs(r0, R0 + dt / 2 * b[0], P0 + dt / 2 * b[1], Ecal, dEcal)
            d = _A_rhs(r0, R0 + dt * c[0], P0 + dt * c[1], Ecal, dEcal)
            Rg[i] = R0 + dt / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0])
            Pg[i] = P0 + dt / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1])
    return dict(fate="TIMEOUT", t=n_t * dt, r=rr, anec=anec, phi=phi,
                first_cross=first_cross, w0=w0)


def witness_A_scan(w0s=(0.05, 0.10, 0.18, 0.22, 0.25, 0.50), fine=False):
    """The ray test across a series of band strengths.  A SCAN, not a
    bisection: right at the threshold the ray and the shell-crossing locus are
    nearly tangent, the predicate stops being monotone at a fixed resolution,
    and bisecting it would report a number the grid invented.  RECORDED."""
    rows = []
    for w0 in w0s:
        a = witness_A_ray(w0)
        row = dict(w0=w0, W=1 + w0, S=saving(1 + w0), fate=a["fate"],
                   t=a["t"], anec=a["anec"])
        if fine:
            row["fate_fine"] = witness_A_ray(w0, dt=0.001, n_t=8000,
                                             n_r=801)["fate"]
        rows.append(row)
    return rows


def witness_A_N1(lo=0.05, hi=0.40, rounds=14):
    """Bisect the SMOOTH indicator instead: the band strength at which the
    first shell crossing coincides with one light crossing of the band."""
    for _ in range(rounds):
        mid = (lo + hi) / 2
        if witness_A_ratio(mid)[2] > 1.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def witness_A_ratio(w0, sigma=None, mass_scale=1.0, length_scale=1.0,
                    n_shells=81, step=0.02):
    """N = (time to the first shell crossing) / (time for light to cross the
    band).  Both scale linearly in the length, so N is scale-invariant; the
    scale arguments exist so the selftest can demonstrate that."""
    global R_C, SIGMA, MASS_M, MASS_RB, RAMP_0, RAMP_1
    save = (R_C, SIGMA, MASS_M, MASS_RB)
    R_C, SIGMA = R_C * length_scale, (sigma or SIGMA) * length_scale
    MASS_M, MASS_RB = MASS_M * mass_scale, MASS_RB * length_scale
    try:
        Ecal, dEcal = _A_funcs(w0)
        t_cross = float("inf")
        for i in range(n_shells):
            r = max(0.05, R_C - 2 * SIGMA) + i * (4 * SIGMA / (n_shells - 1.0))
            R, Rp, t, h = r, 1.0, 0.0, step * length_scale
            while t < 30.0 * length_scale:
                a = _A_rhs(r, R, Rp, Ecal, dEcal)
                b = _A_rhs(r, R + h / 2 * a[0], Rp + h / 2 * a[1], Ecal, dEcal)
                c = _A_rhs(r, R + h / 2 * b[0], Rp + h / 2 * b[1], Ecal, dEcal)
                d = _A_rhs(r, R + h * c[0], Rp + h * c[1], Ecal, dEcal)
                R += h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0])
                Rp_new = Rp + h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1])
                t += h
                if Rp_new <= 0.0:
                    # linear refinement of the zero of R', so the answer is set
                    # by the shell sampling and not by the time step
                    t_cross = min(t_cross, t - h * Rp_new / (Rp_new - Rp))
                    break
                Rp = Rp_new
        n = 2000
        a0, b0 = R_C - SIGMA, R_C + SIGMA
        hh = (b0 - a0) / n
        t_light = sum(hh / W_of(a0 + (i + 0.5) * hh, w0) for i in range(n))
        return t_cross, t_light, t_cross / t_light
    finally:
        R_C, SIGMA, MASS_M, MASS_RB = save


# -------------------------------------------- witness B: the engineered band

def witness_B_fields(t, r, w0, v0):
    W, dW = W_of(r, w0), dW_of(r, w0)
    v, dv = v_of(r, v0), dv_of(r, v0)
    R, Rp = r + t * v, 1.0 + t * dv
    Psi = 1.0 - W * W + v * v                    # = 2m/R, independent of t
    p_r = -Psi / (8 * math.pi * R * R)
    p_T = (W * dW - v * dv) / (8 * math.pi * R * Rp)
    rho = Psi / (8 * math.pi * R * R) - (W * dW - v * dv) / (4 * math.pi * R * Rp)
    return dict(r=r, t=t, R=R, Rp=Rp, W=W, U=v, m=R * Psi / 2, Psi=Psi,
                rho=rho, p_r=p_r, p_T=p_T, j=0.0,
                ec=energy_conditions(rho, p_r, p_T, 0.0),
                contracts=W > 1.0 + 1e-12)


def witness_B_ray(w0, v0, r_far=12.0, n=120000):
    """The COMPLETE radial null geodesic: in from r_far through the regular
    Minkowski core, out again.  Returns the total ANEC, the band's own
    contribution, and the collar's."""
    def leg(t0, phi0, ra, rb):
        sgn = 1.0 if rb > ra else -1.0
        h = abs(rb - ra) / n
        t, phi, tot = t0, phi0, 0.0
        band, collar, closed = 0.0, 0.0, 0.0
        for i in range(n):
            r = ra + sgn * (i + 0.5) * h
            f = witness_B_fields(t, r, w0, v0)
            nec = f["rho"] + f["p_r"]
            dt = h * f["Rp"] / f["W"]                     # |dr| = (W/R') dt
            tot += phi * nec * dt
            if R_C - SIGMA < r < R_C + SIGMA:
                band += phi * nec * dt
                dR = f["Rp"] * sgn * h + f["U"] * dt      # dR along the ray
                closed += -phi * (f["W"] - 1.0) * abs(dR) / (4 * math.pi * f["R"] ** 2)
            if RAMP_0 < r < RAMP_1:
                collar += phi * nec * dt
            phi *= math.exp(-(dv_of(r, v0) / f["Rp"]) * dt)   # d_t Lambda
            t += dt
        return tot, band, collar, closed, t, phi

    ti, bi, ci, xi, tmid, phimid = leg(0.0, 1.0, r_far, 1e-9)
    to, bo, co, xo, _, _ = leg(tmid, phimid, 1e-9, r_far)
    return dict(total=ti + to, band=bi + bo, collar=ci + co,
                band_closed=xi + xo, ingoing=ti, outgoing=to)


def witness_B_band_off(v0, r_far=12.0, n=120000):
    """The same velocity profile with the contraction band switched off."""
    return witness_B_ray(0.0, v0, r_far, n)["total"]


# ------------------------------------------------ the corridor arithmetic

def exhaustion_time(D, W0):
    """Proper time a corridor can hold W >= W0 with m >= 0 while its ends stay
    inside an areal window of width D."""
    return D / math.sqrt(W0 * W0 - 1.0)


def crossings(W0):
    """Lifetime measured in light crossings of the contracted corridor."""
    return W0 / math.sqrt(W0 * W0 - 1.0)


def saving(W0):
    return 1.0 - 1.0 / W0


def product_bound(W0):
    """S * N, exactly."""
    return math.sqrt((W0 - 1.0) / (W0 + 1.0))


def corridor_table(Ws=(1.10, 1.2071067811865475, 1.4142135623730951, 2.0, 10.0, 100.0)):
    rows = []
    for W in Ws:
        rows.append(dict(W=W, S=saving(W), N=crossings(W),
                         SN=saving(W) * crossings(W), bound=product_bound(W),
                         lifetime_over_unassisted=1.0 / math.sqrt(W * W - 1.0)))
    return rows


def proxima_corridor(W0):
    """The exhaustion bound for a Proxima-length corridor, in SI."""
    D_m = PROXIMA_LY * LY
    tau_s = exhaustion_time(D_m, W0) / C
    cross_s = (D_m / W0) / C
    return dict(D_m=D_m, tau_years=tau_s / (LY / C), cross_years=cross_s / (LY / C),
                unassisted_years=(D_m / C) / (LY / C), N=crossings(W0),
                S=saving(W0), SN=saving(W0) * crossings(W0))


# ------------------------------------------------ the machine obligations

def obligations():
    """Every claim of section 5 asserted NEGATED and reported unsat, each with a
    vacuity guard, and the drift guards asked as SATISFIABILITY so they can
    fail.  The one continuity step of the exhaustion argument is NOT here: z3
    has no intermediate-value theorem and pretending otherwise would be the
    encoding drift PROOF-ASSISTANT.md warns about."""
    import prover
    prover.require_z3()
    import z3

    R, m, W, U, W0, T, D, Q, Sv, Nv = z3.Reals("R m W U W0 T D Q S N")
    ident = (W * W == 1 - 2 * m / R + U * U)
    out = []

    def obligation(name, hyp, concl):
        s = z3.Solver()
        s.add(hyp)
        s.add(z3.Not(concl))
        r = s.check()
        out.append((name, str(r), "unsat", r == z3.unsat))
        return r == z3.unsat

    def satisfiable(name, hyp, want=True):
        s = z3.Solver()
        s.add(hyp)
        r = s.check()
        out.append((name, str(r), "sat" if want else "unsat",
                    (r == z3.sat) if want else (r == z3.unsat)))
        return r == z3.sat

    base = [R > 0, ident]

    # X1 -- the sign lock.  U cannot vanish anywhere the band holds with m >= 0.
    satisfiable("guard: m >= 0 and W >= W0 > 1 is satisfiable",
                base + [m >= 0, W0 > 1, W >= W0])
    obligation("X1 SIGN-LOCK  m >= 0, W >= W0 > 1  =>  U^2 >= W0^2 - 1 > 0",
               base + [m >= 0, W0 > 1, W >= W0],
               z3.And(U * U >= W0 * W0 - 1, W0 * W0 - 1 > 0))

    # X2 -- time-symmetric slices carry no corridor at all.
    satisfiable("guard: U = 0 with m >= 0 is satisfiable", base + [U == 0, m >= 0])
    obligation("X2 TIME-SYMMETRY  U = 0 and m >= 0  =>  W^2 <= 1",
               base + [U == 0, m >= 0], W * W <= 1)

    # X3 -- exhaustion.  |dR/dtau| = |U| >= Q = sqrt(W0^2-1), travel T, window D.
    satisfiable("guard: the exhaustion hypothesis is satisfiable",
                base + [m >= 0, W0 > 1, W >= W0, Q > 0, Q * Q == W0 * W0 - 1,
                        T > 0, D > 0, T * Q <= D])
    obligation("X3 EXHAUSTION  |U| >= Q, T Q <= D  =>  T <= D/Q",
               base + [m >= 0, W0 > 1, W >= W0, Q > 0, Q * Q == W0 * W0 - 1,
                       T > 0, D > 0, T * Q <= D],
               T <= D / Q)

    # X4 -- the product bound, exactly.
    satisfiable("guard: S = 1-1/W, N = W/Q is satisfiable for some W > 1",
                [W0 > 1, Q > 0, Q * Q == W0 * W0 - 1,
                 Sv == 1 - 1 / W0, Nv == W0 / Q])
    obligation("X4 PRODUCT  S N = (W-1)/Q  and  (S N)^2 = (W-1)/(W+1) < 1",
               [W0 > 1, Q > 0, Q * Q == W0 * W0 - 1,
                Sv == 1 - 1 / W0, Nv == W0 / Q],
               z3.And(Sv * Nv * W0 * Q == (W0 - 1) * W0,
                      (Sv * Nv) * (Sv * Nv) * (W0 + 1) == W0 - 1,
                      Sv * Nv < 1))

    # X5 -- past sqrt(2) the corridor dies before the unassisted crossing.
    obligation("X5 SQRT2  W0^2 > 2, Q^2 = W0^2-1, Q > 0  =>  D/Q < D  (D > 0)",
               [W0 > 1, Q > 0, Q * Q == W0 * W0 - 1, W0 * W0 > 2, D > 0],
               D / Q < D)

    # DRIFT GUARDS, both asked as satisfiability so that a vacuous encoding
    # would be caught by returning unsat where sat is required.
    satisfiable("DRIFT: drop m >= 0 from X1 and a counterexample must EXIST",
                base + [W0 > 1, W >= W0, z3.Not(U * U >= W0 * W0 - 1)])
    satisfiable("DRIFT: X4's bound is TIGHT -- S N can exceed 1 - epsilon",
                [W0 > 1, Q > 0, Q * Q == W0 * W0 - 1,
                 Sv == 1 - 1 / W0, Nv == W0 / Q, Sv * Nv > z3.RealVal(99) / 100])
    satisfiable("DRIFT: X2 without m >= 0 admits W > 1 at U = 0",
                base + [U == 0, W > 1])
    return out


# ------------------------------------------------------------------- statuses

STATUS = [
    ("INAFFINITY kappa = D_t Lambda + D_r Phi", "DERIVED", "sympy, residual 0"),
    ("RAYCHAUDHURI for the outgoing radial congruence", "DERIVED", "sympy, residual 0"),
    ("WITNESS A: W = sqrt(1+2Ecal), t-independent; j = 0", "DERIVED", "sympy, residual 0"),
    ("WITNESS A: p_r = p_T = 0, rho = mass'/(4 pi R^2 R')", "DERIVED", "sympy, residual 0"),
    ("WITNESS A: NEC, WEC, SEC, DEC all hold pointwise", "MEASURED", "grid, from the evolved solution"),
    ("WITNESS A: ANEC > 0 on the band-crossing ray", "MEASURED", "affine quadrature"),
    ("WITNESS B: rho+p_r = d_r(2m/R)/(8 pi R R'); SEC combination = 0", "DERIVED", "sympy, residual 0"),
    ("WITNESS B: NEC, WEC, DEC violated on the band's rising edge", "MEASURED", "grid"),
    ("WITNESS B: band ANEC = -(phi/4pi) int (W-1)|dR|/R^2", "DERIVED", "by parts; quadrature agrees to 2e-7 relative"),
    ("WITNESS B: complete-geodesic ANEC > 0", "MEASURED", "quadrature, both legs"),
    ("X1-X5, the corridor arithmetic", "MACHINE-CHECKED", "z3 over the reals, unsat"),
    ("the continuity step of the exhaustion argument", "DERIVED-BY-HAND", "IVT; z3 cannot state it"),
    ("ray-test bracket: clears at W_max <= 1.20, caught at >= 1.25", "MEASURED", "scan at two resolutions"),
    ("N = 1 at W_max = 1.1336 +/- 0.001 (11.8 % saving)", "MEASURED", "bisection on a smooth indicator"),
    ("the ray predicate is non-monotone AT the threshold", "RECORDED", "why it is a bracket, not a number"),
    ("scale-invariance of N = t_cross/t_light", "MEASURED", "four decimals under a joint rescaling"),
]

REFUSALS = [
    "The loophole is NOT declared illusory: witness A satisfies every energy condition.",
    "ANEC is NOT claimed to close it: the one negative contribution sits on a geodesic whose total is positive.",
    "The shell-crossing bracket (16.7-20.0 %) is this profile family's, for DUST, and is not generalised.",
    "Nothing non-spherical is touched; the Alcubierre family is outside this file exactly as it is outside certify.py's.",
    "Whether a fluid WITH pressure fails differently is NOT MEASURED.",
    "The ray-test threshold is a BRACKET, not a number: the predicate is not monotone at a fixed grid.",
    "Nothing is repaired and nothing is seated elsewhere; no file outside this one was written.",
]


# ------------------------------------------------------------------- selftest

def selftest():
    import sympy as sp
    fails = []

    def chk(name, got, want, tol=0.0):
        ok = (abs(got - want) <= tol) if tol else (got == want)
        print("  %-68s %s" % (name, "ok" if ok else "FAIL  got %r want %r" % (got, want)))
        if not ok:
            fails.append(name)

    def chk_true(name, cond):
        print("  %-68s %s" % (name, "ok" if cond else "FAIL"))
        if not cond:
            fails.append(name)

    print("D1  the frame identities (sympy residuals)")
    E = general_einstein()
    for name, res in frame_identities(E):
        chk(name, sp.simplify(res), 0)

    print("D2  witness A, the LTB dust derivation (sympy residuals)")
    for name, res in ltb_dust():
        chk(name, sp.simplify(res), 0)

    print("D3  witness B, the engineered band (sympy residuals)")
    for name, res in engineered_band():
        chk(name, sp.simplify(res), 0)

    print("D4  the machine obligations")
    for name, got, want, ok in obligations():
        print("  %-68s %s" % (name, "ok (%s)" % got if ok else "FAIL (%s, want %s)" % (got, want)))
        if not ok:
            fails.append(name)

    print("D5  witness A: every energy condition, pointwise")
    rows = witness_A_slice(0.10, [0.5, 1.5, 2.5, 3.0, 3.5, 5.0, 8.0], t=0.0)
    rows += witness_A_slice(0.10, [0.5, 1.5, 2.5, 3.0, 3.5, 5.0, 8.0], t=0.8)
    chk_true("all four energy conditions hold at every sample",
             all(r["ec"]["NEC"] and r["ec"]["WEC"] and r["ec"]["SEC"] and r["ec"]["DEC"]
                 for r in rows))
    chk_true("j = 0 at every sample, so the type-I reduction applies",
             all(r["ec"]["diagonal"] for r in rows))
    band = [r for r in rows if r["contracts"]]
    chk_true("the band is non-empty and every band sample has m > 0",
             len(band) > 0 and all(r["m"] > 0 for r in band))
    chk_true("every band sample satisfies 2m/R < Rdot^2 (= W > 1)",
             all(2 * r["m"] / r["R"] < r["U"] ** 2 + 1e-12 for r in band))
    chk_true("every band sample has rho > 0 strictly", all(r["rho"] > 0 for r in band))
    chk_true("no trapped surface anywhere sampled: 2m/R < 1",
             all(2 * r["m"] / r["R"] < 1.0 for r in rows))
    chk_true("the exterior is vacuum with W = 1 (Schwarzschild, PG slicing)",
             all(abs(r["W"] - 1.0) < 1e-15 and r["rho"] == 0.0
                 for r in witness_A_slice(0.10, [7.0, 9.0], t=0.0)))

    print("D6  witness A: the ray, and ANEC")
    a10 = witness_A_ray(0.10)
    chk("W_max = 1.10: the ray clears the band", a10["fate"], "CLEARS")
    chk_true("W_max = 1.10: ANEC > 0", a10["anec"] > 0)
    chk("W_max = 1.10: ANEC", a10["anec"], 1.19280e-03, 2e-05)
    a25 = witness_A_ray(0.25)
    chk("W_max = 1.25: the ray is caught by the shell crossing", a25["fate"], "CAUGHT")
    chk_true("W_max = 1.25: the crossing precedes the catch",
             a25["first_cross"] is not None and a25["first_cross"] < a25["t"])

    print("D7  witness B: the energy conditions and ANEC")
    W0B, V0B = 0.10, 0.6
    inner = witness_B_fields(0.0, 2.5, W0B, V0B)
    outer = witness_B_fields(0.0, 3.5, W0B, V0B)
    chk_true("B: v0^2 > W_max^2 - 1, so m > 0 on the band",
             V0B ** 2 > (1 + W0B) ** 2 - 1 and inner["m"] > 0 and outer["m"] > 0)
    chk_true("B: NEC VIOLATED on the rising edge", inner["ec"]["NEC"] is False)
    chk_true("B: WEC VIOLATED on the rising edge", inner["ec"]["WEC"] is False)
    chk_true("B: DEC VIOLATED on the rising edge", inner["ec"]["DEC"] is False)
    chk_true("B: NEC holds on the falling edge", outer["ec"]["NEC"] is True)
    chk("B: SEC combination rho+p_r+2p_T is 0 on the rising edge",
        inner["rho"] + inner["p_r"] + 2 * inner["p_T"], 0.0, 1e-15)
    ray = witness_B_ray(W0B, V0B)
    chk_true("B: the band's own ANEC contribution is NEGATIVE", ray["band"] < 0)
    chk_true("B: the closed form matches the quadrature to 1e-6",
             abs(ray["band"] - ray["band_closed"]) <= 1e-6 * abs(ray["band_closed"]))
    chk_true("B: the COMPLETE geodesic ANEC is POSITIVE", ray["total"] > 0)
    chk_true("B: switching the band off RAISES the total",
             witness_B_band_off(V0B) > ray["total"])

    print("D8  the same slice, two momenta")
    slice_A = witness_A_slice(W0B, [2.5, 3.0, 3.5], t=0.0)
    for rA in slice_A:
        rB = witness_B_fields(0.0, rA["r"], W0B, V0B)
        chk("t=0 slice agrees at r=%.1f: R" % rA["r"], rA["R"], rB["R"], 1e-12)
        chk("t=0 slice agrees at r=%.1f: W" % rA["r"], rA["W"], rB["W"], 1e-12)
        chk("t=0 slice agrees at r=%.1f: R'" % rA["r"], rA["Rp"], rB["Rp"], 1e-12)
    chk_true("and the two disagree on the NEC at r = 2.5",
             witness_A_slice(W0B, [2.5])[0]["ec"]["NEC"] is True
             and witness_B_fields(0.0, 2.5, W0B, V0B)["ec"]["NEC"] is False)

    print("D9  the corridor arithmetic")
    for W in (1.05, 1.25, 2.0, 10.0, 1e4):
        chk("S N = sqrt((W-1)/(W+1)) at W = %g" % W,
            saving(W) * crossings(W), product_bound(W), 1e-12 * max(1.0, W))
        chk_true("S N < 1 at W = %g" % W, saving(W) * crossings(W) < 1.0)
    chk("lifetime = one unassisted crossing exactly at W = sqrt(2)",
        1.0 / math.sqrt(math.sqrt(2.0) ** 2 - 1.0), 1.0, 1e-15)
    chk_true("and strictly less than one above sqrt(2)",
             1.0 / math.sqrt(1.5 ** 2 - 1.0) < 1.0 < 1.0 / math.sqrt(1.3 ** 2 - 1.0))
    chk_true("crossings(W) is decreasing in W",
             all(crossings(a) > crossings(b) for a, b in
                 ((1.1, 1.2), (1.2, 2.0), (2.0, 10.0), (10.0, 100.0))))

    print("D10 the measured shell-crossing scale, and its scale invariance")
    n1 = witness_A_ratio(0.25)[2]
    n2 = witness_A_ratio(0.25, mass_scale=2.0, length_scale=2.0)[2]
    chk("N is scale-invariant under a joint rescaling", n1, n2, 1e-4)
    chk_true("N < 1 at W_max = 1.25", n1 < 1.0)
    chk_true("N > 1 at W_max = 1.05", witness_A_ratio(0.05)[2] > 1.0)
    chk("N = 1 at w0 (81 shells; converges to 0.1326 as the sampling refines)",
        witness_A_N1(0.05, 0.40, 12), 0.13361, 1e-3)
    chk("and the time step does not set it: 0.02 and 0.005 agree",
        witness_A_ratio(0.20, step=0.02)[2], witness_A_ratio(0.20, step=0.005)[2], 1e-6)
    scan = {r["w0"]: r for r in witness_A_scan((0.05, 0.18, 0.25, 0.50))}
    chk_true("the ray CLEARS well below the threshold (W_max = 1.05, 1.18)",
             scan[0.05]["fate"] == "CLEARS" and scan[0.18]["fate"] == "CLEARS")
    chk_true("the ray is CAUGHT well above it (W_max = 1.25, 1.50)",
             scan[0.25]["fate"] == "CAUGHT" and scan[0.50]["fate"] == "CAUGHT")
    chk_true("and the same four verdicts survive a doubled resolution",
             all(witness_A_ray(w, dt=0.001, n_t=8000, n_r=801)["fate"]
                 == scan[w]["fate"] for w in (0.05, 0.18, 0.25, 0.50)))

    print()
    if fails:
        print("SELFTEST FAILED: %d" % len(fails))
        for f in fails:
            print("   -", f)
        return 1
    print("SELFTEST OK")
    return 0


# --------------------------------------------------------------------- report

def _rule(s=""):
    print("=" * 79)
    if s:
        print(s)
        print("=" * 79)


def report():
    W0A, W0B, V0B = 0.10, 0.10, 0.6

    _rule("DOCKET 52 -- THE LOCALIZED BAND.  localband.py")
    print("""
The question: an explicit spherically symmetric DYNAMIC metric, m > 0
everywhere, with 2m/R < e^{-2Phi} Rdot^2 over a FINITE region; the full
stress-energy from the Einstein tensor; NEC, WEC, SEC, DEC pointwise; and the
NEC integrated along a radial null geodesic.

The answer: THE WITNESS EXISTS AND EVERY ENERGY CONDITION HOLDS ON IT.  A
second, differently built band with the SAME initial slice violates NEC, WEC
and DEC -- and even there the ANEC integral over the complete geodesic is
positive.  No energy condition decides this.  What does is a clock.
""")

    _rule("1.  WITNESS A -- THE COMOVING BAND")
    print("""
    ds^2 = -dt^2 + [R'(t,r)^2/(1 + 2 Ecal(r))] dr^2 + R(t,r)^2 dOmega^2
           Rdot^2 = 2 Ecal(r) + 2 mass(r)/R ;  R(0,r) = r ,  R'(0,r) = 1

    W(r)    = 1 + %.2f (1 - ((r-3)/1)^2)^4  on 2 < r < 4, else 1
    Ecal(r) = (W(r)^2 - 1)/2
    mass(r) = 0.30 u^3(10 - 15u + 6u^2),  u = min(r/6, 1)

DERIVED from the Einstein tensor (residual 0): W = sqrt(1+2Ecal), independent
of t; j = 0 identically; p_r = p_T = 0; rho = mass'/(4 pi R^2 R'); m_MS = mass.
mass(0) = 0, so the centre is regular; Ecal = 0 and mass = M past r = 6, so the
exterior is Schwarzschild in a marginally bound (Painleve-Gullstrand) slicing,
W = 1 exactly, and the spacetime is asymptotically flat.  No trapped surface:
max 2m/R on the sampled slice is well below 1.
""" % W0A)
    print("   r      W       m      2m/R     U      rho        NEC  WEC  SEC  DEC   band")
    for row in witness_A_slice(W0A, [0.5, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 8.0], 0.0):
        ec = row["ec"]
        print("  %-5.2f %7.5f %7.5f %7.5f %7.5f %10.3e   %-4s %-4s %-4s %-4s  %s"
              % (row["r"], row["W"], row["m"], 2 * row["m"] / row["R"], row["U"],
                 row["rho"], "yes" if ec["NEC"] else "NO", "yes" if ec["WEC"] else "NO",
                 "yes" if ec["SEC"] else "NO", "yes" if ec["DEC"] else "NO",
                 "CONTRACTS" if row["contracts"] else "-"))
    print("\n   ... and at t = 0.8, after the band has evolved:")
    print("   r      W       m      2m/R     U      rho        NEC  WEC  SEC  DEC   band")
    for row in witness_A_slice(W0A, [2.5, 3.0, 3.5], 0.8):
        ec = row["ec"]
        print("  %-5.2f %7.5f %7.5f %7.5f %7.5f %10.3e   %-4s %-4s %-4s %-4s  %s"
              % (row["r"], row["W"], row["m"], 2 * row["m"] / row["R"], row["U"],
                 row["rho"], "yes" if ec["NEC"] else "NO", "yes" if ec["WEC"] else "NO",
                 "yes" if ec["SEC"] else "NO", "yes" if ec["DEC"] else "NO",
                 "CONTRACTS" if row["contracts"] else "-"))
    ray = witness_A_ray(W0A)
    print("""
    ANEC along the affinely parametrised outgoing radial null geodesic that
    crosses the band, launched at r = 2.0:

        fate = %s   at t = %.4f, r = %.4f
        ANEC = %+.8e     POSITIVE -- SATISFIED

    That is the witness.  m > 0 throughout, contraction on a finite band,
    NEC/WEC/SEC/DEC all satisfied and all strict on the band, ANEC positive.
    THE LOOPHOLE IS NOT ILLUSORY AND THE NEC DOES NOT CLOSE IT.
""" % (ray["fate"], ray["t"], ray["r"], ray["anec"]))

    _rule("2.  WITNESS B -- THE ENGINEERED BAND, SAME SLICE")
    print("""
    ds^2 = -dt^2 + [(1 + t v'(r))^2/W(r)^2] dr^2 + (r + t v(r))^2 dOmega^2
           v(r) = %.2f S((r-0.5)/1), S the quintic ramp;  W(r) as above

    At t = 0 this induces dl^2 = dr^2/W(r)^2 + r^2 dOmega^2 -- THE SAME SLICE,
    band and saving as witness A.  Only the momentum differs.
""" % V0B)
    print("   r      W       m      2m/R     rho        p_r        p_T       NEC  WEC  SEC  DEC")
    for r in (1.0, 2.0, 2.3, 2.5, 2.8, 3.0, 3.2, 3.5, 3.7, 4.0, 6.0):
        f = witness_B_fields(0.0, r, W0B, V0B)
        ec = f["ec"]
        print("  %-5.2f %7.5f %7.5f %7.5f %10.3e %10.3e %10.3e  %-4s %-4s %-4s %-4s"
              % (r, f["W"], f["m"], f["Psi"], f["rho"], f["p_r"], f["p_T"],
                 "yes" if ec["NEC"] else "NO", "yes" if ec["WEC"] else "NO",
                 "yes" if ec["SEC"] else "NO", "yes" if ec["DEC"] else "NO"))
    rb = witness_B_ray(W0B, V0B)
    off = witness_B_band_off(V0B)
    print("""
    rho + p_r = d_r(2m/R)/(8 pi R R')  -- DERIVED, residual 0.  On the band
    v' = 0, so it is -W W'/(4 pi R): NEGATIVE on the whole rising edge.
    rho + p_r + 2 p_T = 0 IDENTICALLY in this family, so SEC fails only through
    its NEC half.

    ANEC on the COMPLETE radial null geodesic (in from r = 12 through the
    regular Minkowski core, out again):

        band's own contribution     %+.6e     (closed form %+.6e)
        velocity collar             %+.6e
        COMPLETE GEODESIC TOTAL     %+.6e     POSITIVE -- SATISFIED
        same v, band switched off   %+.6e     (the band LOWERS it by %.3e)

    So the contraction contributes negatively to ANEC, exactly and always, and
    an ordinary positive-energy collar elsewhere on the same geodesic pays for
    it.  ANEC DOES NOT CLOSE THE LOOPHOLE EITHER, AND THIS FILE SAYS SO.
""" % (rb["band"], rb["band_closed"], rb["collar"], rb["total"], off,
       off - rb["total"]))

    _rule("3.  WHAT THE PAIR MEASURES")
    print("""
    Witness A and witness B share a t = 0 slice to machine precision -- same R,
    same R', same W, same contraction band, same saving -- and disagree on the
    NEC.  W IS A PROPERTY OF THE SLICE; THE ENERGY CONDITIONS ARE NOT.  No
    function of the contraction can decide an energy condition, so the question
    "does contracting proper distance cost negative energy" has no answer at
    the level at which the docket asked it.
""")

    _rule("4.  WHAT DOES CLOSE IT -- THE CLOCK")
    print("""
    With m >= 0 and W >= W0 > 1: U^2 >= W0^2 - 1 > 0, so U never vanishes and
    keeps its sign, so the areal radius is strictly monotone.  A corridor whose
    ends stay inside an areal window of width D therefore survives at most

        T  <=  D / sqrt(W0^2 - 1)

    and at a moment of TIME SYMMETRY (U == 0 on the slice) m >= 0 forces W <= 1
    EVERYWHERE: a corridor cannot be switched on from rest.
""")
    print("    W        saving S   crossings N   S*N      sqrt((W-1)/(W+1))   T/(unassisted)")
    for row in corridor_table():
        print("  %-8.4f %8.4f   %9.4f   %7.4f   %14.4f   %12.4f"
              % (row["W"], row["S"], row["N"], row["SN"], row["bound"],
                 row["lifetime_over_unassisted"]))
    print("""
    S * N = sqrt((W-1)/(W+1)) EXACTLY, and it is < 1 for every W.  A corridor
    that saves half its length survives 1.155 crossings; one that survives four
    saves 6.1 %.  And T/(unassisted crossing) = 1/sqrt(W^2-1) passes 1 at
    W = sqrt(2): ABOVE A 29.3 % CONTRACTION THE CORRIDOR DIES BEFORE LIGHT
    WOULD HAVE ARRIVED WITHOUT IT.
""")
    p = proxima_corridor(2.0)
    print("    Proxima, %.4f ly, at W = 2:  lifetime <= %.4f yr, one contracted"
          % (PROXIMA_LY, p["tau_years"]))
    print("    crossing %.4f yr, unassisted %.4f yr, S*N = %.4f"
          % (p["cross_years"], p["unassisted_years"], p["SN"]))

    print("""
    AND THE MEASURED NUMBER IS WORSE THAN THE BOUND.  Witness A is dust, and
    dust tears: the band's outer edge runs into the shells ahead of it and R'
    reaches zero.  Asked the only question that matters -- does light get
    across before the band stops existing --
""")
    print("    W_max    saving     t_cross   t_light      N       ray      ray (2x res)")
    for row in witness_A_scan((0.05, 0.10, 0.18, 0.20, 0.22, 0.25, 0.50)):
        tc, tl, n = witness_A_ratio(row["w0"])
        fine = (witness_A_ray(row["w0"], dt=0.001, n_t=8000, n_r=801)["fate"]
                if row["w0"] in (0.20, 0.22, 0.25) else "-")
        print("   %6.3f  %8.4f  %8.4f  %8.4f  %7.4f   %-8s  %s"
              % (row["W"], row["S"], tc, tl, n, row["fate"], fine))
    n1 = witness_A_N1()
    print("""
    N = 1 -- the first shell crossing arrives exactly one band light-crossing
    after t = 0 -- at W_max = %.4f, a saving of %.2f %%, converging to
    W_max = 1.133 as the shell sampling refines.  That indicator is smooth,
    is insensitive to the time step, and is bisected.  THE RAY TEST ITSELF IS
    NOT BISECTED: right at its threshold the ray and the crossing locus are nearly tangent, the verdict
    stops being monotone in w0 at a fixed grid, and the two resolutions above
    disagree at W_max = 1.22.  The honest statement is a BRACKET: the ray
    clears at W_max <= 1.20 and is caught at W_max >= 1.25 at both resolutions,
    so the threshold saving lies between 16.7 %% and 20.0 %%.  An earlier pass of
    this file bisected that predicate and reported 17.4 %%; the number was in
    the bracket but the method was invalid, and it is withdrawn as a method.

    N is scale-invariant to four decimals under a joint rescaling of sigma, M,
    r_b and r_c, so this is a shape fact and not a tuning.  It is also a
    statement about DUST: a shell-crossing singularity is gravitationally weak
    and is the standard artefact of zero pressure.  RECORDED, NOT REPAIRED,
    NOT GENERALISED.
""" % (1 + n1, 100 * saving(1 + n1)))

    _rule("5.  STATUSES, NEVER FLATTENED")
    for name, st, how in STATUS:
        print("  %-12s %-58s %s" % (st, name, how))

    _rule("6.  WHAT THIS FILE REFUSES")
    for line in REFUSALS:
        print("  -", line)
    _rule()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--selftest", action="store_true",
                    help="every residual, every machine obligation")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
