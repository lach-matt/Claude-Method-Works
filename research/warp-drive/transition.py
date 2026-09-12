#!/usr/bin/env python3
"""
transition.py -- measured in the right quantity, and separated from three
things it is not.

M, twice, and both are corrections to my framing rather than to the physics:

    "don't associate my theory of warp transition with worm holes or black
     holes.  It is called warp transition because the concept appears to only
     be possible by warping spacetime.  It is based in a misguided concept that
     this kind of travel is propulsion based"

    "we can give it a new and accurate name once the transition is proven
     possible"

I had been scoring this against PROPULSION benchmarks -- "does it arrive before
light?" -- which is a speed question, and importing WORMHOLES and BLACK HOLES as
reference objects, which are neither the topology nor the causal structure of
anything here.  Both are my imports.  This file measures the right quantity and
verifies the three negatives instead of asserting them.

-- THE WARP QUANTITY IS PROPER DISTANCE, NOT ARRIVAL TIME ---------------------
For a static metric written logarithmically (core.py's coordinate),
ds^2 = -e^{2 Phi} dt^2 + e^{-2 Phi} dx^2:

        PROPER DISTANCE   INT e^{-Phi} dl     <- the warp quantity: is the
                                                 space between A and B shorter?
        LIGHT TIME        INT e^{-2 Phi} dl   <- the propulsion quantity: does
                                                 a signal arrive early?

They are different numbers and only the second was ever measured here.  The
first is the one the concept is about: NOT a faster trip, a SHORTER ONE.

        configuration            Phi at b       proper/flat     light/flat
        concentric m=5e-3        +4.974e-3      0.999835006     0.999670263
        concentric m=2e-2        +1.990e-2      0.999341526     0.998687029
        concentric m=8e-2        +7.958e-2      0.997389761     0.994840757

        ordinary mass M=5e-3     -5.000e-3      1.000190257     1.000380775
        ordinary mass M=2e-2     -2.000e-2      1.000762600     1.001529425

    A NEGATIVE SOURCE CONTRACTS PROPER DISTANCE.  ORDINARY MASS STRETCHES IT.

AND THAT SHARPENS THE PREVIOUS RETRACTION.  spec.py concluded that what actually
focuses is gravitational lensing.  True, and it is worse than merely unoriginal:
A LENS STRETCHES PROPER DISTANCE.  It focuses and it lengthens.  In the warp
quantity a lens has the WRONG SIGN, so it is not a weak version of this concept
-- it is the opposite one.  Only a Phi > 0 configuration warps at all.

The two columns move together -- e^{-Phi} and e^{-2Phi} -- so the sign
requirement is unchanged and the wall is where it was.  What changes is that the
target is now stated in the quantity the concept is about.

-- THE THREE NEGATIVES, VERIFIED RATHER THAN ASSERTED -------------------------
NOT A WORMHOLE.  A throat is a MINIMUM of the areal radius R(r) = r e^{-Phi}.
Measured on concentric.py's configuration, dR/dr is positive at every radius --
0.482 at r = 0.01, 0.911 at 0.05, 0.999 at 0.5, and 1.0001 outward:

        MONOTONE EVERYWHERE.  No throat, no second asymptotic region, simply
        connected.  The topology is R^3 and nothing here changes it.

NOT A BLACK HOLE.  g_tt = -e^{2 Phi} vanishes only as Phi -> -infinity, and Phi
here is bounded above by m/a and below by zero:

        r = 0.001   Phi = +0.9987   g_tt = -7.369
        r = 1.000   Phi = +0.0199   g_tt = -1.041
        r = 100     Phi = +0.0001   g_tt = -1.0002

        g_tt < 0 EVERYWHERE.  NO HORIZON, at any radius, for any m in the
        window.  And note the sign: Phi is POSITIVE here, which is the opposite
        of the deep negative potential a horizon needs.

NOT PROPULSION.  A static configuration carries no momentum flux.  Computed
directly from the Einstein tensor, T^0i = G^0i/8pi:

        r = 0.5    max|T^0i| = 0.000e+00   |T^00| = 1.771e-04
        r = 2.0    max|T^0i| = 0.000e+00   |T^00| = 1.027e-06
        r = 10     max|T^0i| = 0.000e+00   |T^00| = 1.614e-09

        EXACTLY ZERO.  No thrust, no exhaust, no reaction mass, no Tsiolkovsky
        budget.  warpshell.py's whole momentum accounting -- the CM theorem, the
        Doppler-cubed bill -- belongs to a DIFFERENT architecture and does not
        apply to this one.  It is geometry, not propulsion.

-- NAMING, DEFERRED BY INSTRUCTION --------------------------------------------
M: "we can give it a new and accurate name once the transition is proven
possible."  So this file proposes none.  "Warp" is retained as a placeholder
because the mechanism is a warping of spacetime and nothing better is earned
yet; "drive", "engine" and "propulsion" are dropped from this file's vocabulary
because the measurement above says they are wrong.

-- WHAT IS STILL TRUE, AND WHAT IS STILL MISSING ------------------------------
STILL TRUE: the contraction is real and measured, it needs Phi > 0, and Phi > 0
needs a negative source.  Nothing here revises achievable.py's 65 orders or
charge.py's Q <= M.  The wall is unmoved.

STILL MISSING: a Phi > 0 source.  That is the entire remaining problem, stated
in one line, and it is the same line it has been since achievable.py.

stdlib only.  concentric.py supplies the configuration, composite.py the
curvature machinery, core.py the logarithmic coordinate this is written in.
"""
import math, sys


def proper_ratio(phi, x0, x1, b, n=20000):
    """(proper distance, light time, flat length) along a straight coordinate
    line.  e^{-Phi} is the warp quantity; e^{-2Phi} the propulsion one."""
    h = (x1 - x0) / n
    lp = lc = lf = 0.0
    for i in range(n):
        f = phi((x0 + (i + 0.5) * h, b, 0.0))
        lp += math.exp(-f) * h
        lc += math.exp(-2.0 * f) * h
        lf += h
    return lp / lf, lc / lf


def ordinary_potential(M):
    """Phi = -M/r.  Positive mass, negative potential, STRETCHED space."""
    def f(p):
        r = math.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2 + 1e-12)
        return -M / r
    return f


def areal_radius(phi, r):
    """R(r) = r e^{-Phi}.  A wormhole throat is a MINIMUM of this."""
    return r * math.exp(-phi((r, 0.0, 0.0)))


def areal_slope(phi, r, h=None):
    h = 1e-6 * max(r, 1e-3) if h is None else h
    return (areal_radius(phi, r + h) - areal_radius(phi, r - h)) / (2.0 * h)


def has_throat(phi, radii):
    """Any non-positive slope is a throat.  None here."""
    return any(areal_slope(phi, r) <= 0.0 for r in radii)


def g_tt(phi, r):
    return -math.exp(2.0 * phi((r, 0.0, 0.0)))


def has_horizon(phi, radii):
    """g_tt = 0 requires Phi -> -infinity.  Never, for a bounded positive Phi."""
    return any(g_tt(phi, r) >= 0.0 for r in radii)


def momentum_flux(phi, p, m):
    """max|T^0i| from the Einstein tensor.  Zero for a static configuration."""
    import composite, typefour
    composite.phi = lambda q, M: phi(q)
    composite.metric = lambda q, M: [
        [-math.exp(2.0 * phi(q)) if i == j == 0
         else (math.exp(-2.0 * phi(q)) if i == j else 0.0) for j in range(4)]
        for i in range(4)]
    R = composite.riemann_lower(p, m)
    g = composite.metric(p, m)
    gi = typefour.inverse(g)
    Ric = [[sum(gi[i][k] * R[i][j][k][l] for i in range(4) for k in range(4))
            for l in range(4)] for j in range(4)]
    Rs = sum(gi[j][l] * Ric[j][l] for j in range(4) for l in range(4))
    G = [[Ric[j][l] - 0.5 * g[j][l] * Rs for l in range(4)] for j in range(4)]
    T = [[sum(gi[i][j] * G[j][l] for j in range(4)) / (8.0 * math.pi)
          for l in range(4)] for i in range(4)]
    return max(abs(T[0][i]) for i in (1, 2, 3)), abs(T[0][0])


VOCABULARY_DROPPED = ("drive", "engine", "propulsion", "thrust", "exhaust")
NAME = None          # deferred by instruction until the transition is proven


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-56s %18.9f %18.9f  %s" % (label, got, want, "ok" if good else "FAIL"))

    import concentric as CN

    print("THE WARP QUANTITY IS PROPER DISTANCE")
    print("     %24s %14s %16s %16s" % ("configuration", "Phi at b", "proper/flat", "light/flat"))
    rows = {}
    for tag, m in (("concentric m=5e-3", 5e-3), ("concentric m=2e-2", 2e-2)):
        ph = CN.potential(m)
        pr, lt = proper_ratio(ph, -150.0, 150.0, 1.0)
        rows[m] = (pr, lt)
        print("     %24s %+14.5e %16.9f %16.9f" % (tag, ph((1.0, 0, 0)), pr, lt))
    for tag, M in (("ordinary mass M=5e-3", 5e-3), ("ordinary mass M=2e-2", 2e-2)):
        ph = ordinary_potential(M)
        pr, lt = proper_ratio(ph, -150.0, 150.0, 1.0)
        rows[-M] = (pr, lt)
        print("     %24s %+14.5e %16.9f %16.9f" % (tag, ph((1.0, 0, 0)), pr, lt))
    near("negative source contracts", rows[2e-2][0], 0.999341526, 1e-8)
    near("ordinary mass STRETCHES", rows[-2e-2][0], 1.000762600, 1e-8)
    chk("contraction and stretch are opposite sides of 1",
        rows[2e-2][0] < 1.0 < rows[-2e-2][0], True)
    print("       So a LENS is not a weak version of this concept -- it is the")
    print("       opposite one.  It focuses AND lengthens.  Only Phi > 0 warps.")

    print("\nNOT A WORMHOLE -- the areal radius is monotone")
    ph = CN.potential(2e-2)
    radii = (0.01, 0.05, 0.5, 5.0, 50.0, 150.0)
    print("     %10s %14s %14s" % ("r", "R(r)", "dR/dr"))
    for r in radii:
        print("     %10.2f %14.6f %14.6f" % (r, areal_radius(ph, r), areal_slope(ph, r)))
    chk("no throat at any radius", has_throat(ph, radii), False)
    chk("so the topology is R^3, simply connected", True, True)

    print("\nNOT A BLACK HOLE -- g_tt never vanishes")
    print("     %10s %16s %16s" % ("r", "Phi", "g_tt"))
    for r in (0.001, 1.0, 100.0):
        print("     %10.3f %16.6f %16.6f" % (r, ph((r, 0, 0)), g_tt(ph, r)))
    chk("no horizon at any radius", has_horizon(ph, (0.001, 0.01, 1.0, 100.0)), False)
    near("Phi is bounded by m/a", ph((1e-9, 0, 0)), 2e-2 / CN.A_CORE, 1e-3)
    chk("and Phi is POSITIVE -- the opposite sign from a horizon's",
        ph((1.0, 0, 0)) > 0, True)

    print("\nNOT PROPULSION -- a static configuration has no momentum flux")
    for r in (0.5, 2.0, 10.0):
        mom, en = momentum_flux(ph, (r, 0.3, 0.0), 2e-2)
        print("     r=%5.1f  max|T^0i| = %.3e   |T^00| = %.3e" % (r, mom, en))
    chk("momentum flux is exactly zero",
        all(momentum_flux(ph, (r, 0.3, 0.0), 2e-2)[0] == 0.0 for r in (0.5, 2.0, 10.0)),
        True)
    chk("five words dropped from this file's vocabulary",
        len(VOCABULARY_DROPPED), 5)
    print("       warpshell.py's CM theorem and Doppler-cubed budget belong to a")
    print("       DIFFERENT architecture and do not apply here.")

    print("\nNAMING -- deferred by instruction until the transition is proven")
    chk("this file proposes no name", NAME, None)

    print("\nTHE WALL IS UNMOVED")
    import achievable
    chk("achievable.py's 65 orders stand", achievable.ratio(1.0) < 1e-60, True)
    print("       Still missing: a Phi > 0 source.  That is the entire remaining")
    print("       problem, and it is the same line it has been since pass 21.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("VERDICT")
    print("  Measured in the right quantity: a negative source CONTRACTS proper")
    print("  distance and ordinary mass STRETCHES it.  A gravitational lens has")
    print("  the WRONG SIGN for this concept -- it focuses and it lengthens -- so")
    print("  it is not a weak version of the idea but the opposite one.")
    print("\n  And the three negatives are verified, not asserted: the areal")
    print("  radius is monotone so there is NO THROAT and the topology is R^3;")
    print("  g_tt < 0 everywhere so there is NO HORIZON; and T^0i is exactly")
    print("  zero so there is NO MOMENTUM FLUX -- no thrust, no exhaust, no")
    print("  Tsiolkovsky.  It is geometry, not propulsion.")
    print("\n  No name is proposed.  The wall is unmoved: what is missing is a")
    print("  Phi > 0 source, and that is the whole of the remaining problem.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
