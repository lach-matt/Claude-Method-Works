#!/usr/bin/env python3
"""
stability.py -- does concentric.py's device hold together?

The exotic core is M's identification phase and is deferred.  What is NOT
deferred is whether the thing is a device at all, and wall.py's history in this
project is the warning: the warpshell was radially stable, structurally fixable,
and then died to a non-radial mode nobody had posed.  So the shell gets asked
first, and it gets asked the way that killed the last one.

    THE SHELL IS ORDINARY MATTER AND IT IS RADIALLY STABLE WITH NO PRESSURE
    RESPONSE AT ALL -- and the reason is the same sign flip that made the core
    seat and lead.

-- THE SETUP IS UNUSUALLY CLEAN -----------------------------------------------
concentric.py's device has M_ADM = 0, so the Israel junction is between

        INTERIOR   Schwarzschild with M_in = -m   (the negative core)
        EXTERIOR   M_out = 0, i.e. FLAT MINKOWSKI

That is the mirror of the textbook shell (flat inside, mass outside), and every
result below is the textbook one with its sign reversed.

-- THE SHELL IS ORDINARY MATTER -----------------------------------------------
        sigma = -(1/4 pi R)[ sqrt(f_out) - sqrt(f_in) ] = (1/4 pi R)[sqrt(1+2m/R) - 1]

which is POSITIVE for every m > 0.  The pressure is a small tension, O((m/R)^2):

        m/R      sigma          p              sigma+p        sigma-|p|   DEC
        0.01     +7.918e-4      -1.950e-6      +7.899e-4      +7.899e-4   yes
        0.10     +7.595e-3      -1.654e-4      +7.430e-3      +7.430e-3   yes
        0.50     +3.296e-2      -2.414e-3      +3.055e-2      +3.055e-2   yes
        2.00     +9.836e-2      -1.359e-2      +8.477e-2      +8.477e-2   yes

    THE SHELL SATISFIES THE DOMINANT ENERGY CONDITION at every compactness
    tested.  All the exoticism in this device is in the core, and the core is
    the identification phase.  The structure holding it is ordinary.

-- AND IT IS RADIALLY STABLE FOR FREE -----------------------------------------
Poisson-Visser: Rdot^2 = -V(R) with V(R) = 1 - 2M_out/R - [dM/m_s - m_s/2R]^2,
dM = M_out - M_in, and m_s evolved by the conservation law m_s' = -8 pi R p.
A static shell sits at V = V' = 0 and is stable iff V'' > 0.

VALIDATION FIRST, because the sign is the whole claim.  The ORDINARY shell --
flat inside, mass M outside, no pressure response:

        M/R      V''(beta^2 = 0)
        0.01     -3.036e-2        UNSTABLE, as a dust shell must be
        0.10     -3.424e-1
        0.20     -8.169e-1

and OUR device, negative inside, flat outside, same machinery, same beta^2 = 0:

        m/R      V''(beta^2 = 0)
        0.01     +2.965e-2        STABLE
        0.10     +2.700e-1
        0.50     +1.018e+0

    NEARLY MIRROR IMAGES.  -3.036e-2 against +2.965e-2 at m/R = 0.01.  Flipping
    the sign of the interior mass flips the curvature of the effective
    potential, and the shell that needed stiffness to survive no longer does:

        beta^2_crit is NEGATIVE at every compactness measured (-0.0037 at
        m/R = 0.01 down to -0.132 at m/R = 1), so ANY non-negative beta^2 --
        dust included -- clears it.

    THAT IS THE THIRD APPEARANCE OF ONE SIGN STRUCTURE.  The negative source
    focuses through Weyl without needing positive energy (composite.py), leads
    instead of lagging because the Shapiro term is linear (composite.py), and
    now stabilises the shell because it reverses the potential's curvature.
    One sign, three consequences, none of them arranged.

-- THE CORE'S POSITION IS NEUTRAL, EXACTLY ------------------------------------
Newton's shell theorem: the field inside a spherical shell vanishes at EVERY
interior point, not only the centre.  So the core feels no force wherever it
sits inside, and its position is neutrally stable -- not stable, not unstable,
and worth stating as neither.

-- WHAT IS NOT RUN, AND THE FIRST ONE IS THE DANGEROUS ONE --------------------
 1. NON-RADIAL MODES, l >= 2.  THIS IS WHAT KILLED THE WARPSHELL.  Pitre-
    Schneider-Poisson find an unstable even-parity mode for all l >= 2, all
    compactness, all Gamma, on self-gravitating thin shells -- and obstruct.py
    still carries that as CONDITIONAL.  Their configuration has M_in >= 0 and
    M_out > 0; ours has M_in < 0 and M_out = 0, and the radial mode already
    flipped sign under exactly that exchange.  SO THERE IS A REASON TO EXPECT
    THE NON-RADIAL ONE MIGHT FLIP TOO, AND THAT IS PRECISELY WHY IT MUST BE
    COMPUTED RATHER THAN ASSUMED.  It is the top remaining risk to the device.
 2. l = 1, the core displaced.  Its position is neutral, but a displaced core
    presents an asymmetric field TO the shell, which is a dipole deformation
    nobody has posed here.
 3. THE CORE'S OWN STABILITY.  Deferred with the identification phase, by M's
    instruction, and named here so it is deferred rather than forgotten.
 4. The linearised-field caution from concentric.py stands unchanged.

stdlib only.  wall.py supplies the Poisson-Visser machinery this file
generalises to a negative interior; concentric.py supplies the device.


    *** A MODE THIS FILE NEVER NAMED, ADDED BY negmass.py ***

    What is measured below is the RADIAL breathing mode, and l >= 2 is flagged
    as the top NOT-RUN risk.  l = 1 -- THE TRANSLATION MODE -- is not mentioned
    anywhere, and Trivedi & Loeb (arXiv:2605.10976) analyse exactly our M = 0
    configuration and call it a RUNAWAY.

    It is not one: their case is a BINARY (a dipole) and ours is CONCENTRIC, so
    Newton's shell theorem gives zero force on the core at any displacement and
    the Bondi runaway has no dipole to work with.  BUT ZERO FORCE IS NEUTRAL,
    NOT RESTORING.  The failure mode is DRIFT TO CONTACT rather than
    exponential runaway -- slower than the literature's, and still a failure.
    The GR version, with the junction conditions rather than Newton, is
    NOT-RUN.  See negmass.py.

    AND CLOSED IN NEWTONIAN GRAVITY BY chain.py.  Earnshaw's theorem: the
    potential of any point sources is harmonic away from them whatever their
    signs -- the Hessian of 1/r is traceless -- so a harmonic function has no
    strict minimum and NO static configuration is stably in equilibrium, for
    any signs, any code, any placement.  The one escape Earnshaw permits is the
    DEGENERATE case, constant potential, and Newton's shell theorem hands the
    device exactly that.  So neutral is not an oversight here, it is the
    Newtonian CEILING, and drift to contact is not a defect to engineer out.
    A restoring force must come from outside Newtonian statics: GR, time
    dependence, or a non-gravitational channel.  The GR version stays NOT-RUN.
"""
import math, sys


def f_metric(R, M):
    return 1.0 - 2.0 * M / R


def sigma(R, M_in, M_out):
    """Israel surface density.  Positive for our device at every m."""
    return -(1.0 / (4.0 * math.pi * R)) * (math.sqrt(f_metric(R, M_out))
                                           - math.sqrt(f_metric(R, M_in)))


def pressure(R, M_in, M_out):
    """Israel surface pressure.  Negative here: a small tension."""
    a, b = math.sqrt(f_metric(R, M_in)), math.sqrt(f_metric(R, M_out))
    return (1.0 / (8.0 * math.pi * R)) * ((1.0 - M_out / R) / b
                                          - (1.0 - M_in / R) / a)


def dec_holds(R, M_in, M_out):
    s, p = sigma(R, M_in, M_out), pressure(R, M_in, M_out)
    return s >= 0.0 and s >= abs(p)


def nec_holds(R, M_in, M_out):
    return sigma(R, M_in, M_out) + pressure(R, M_in, M_out) >= 0.0


def ms_static(R, M_in, M_out):
    return R * (math.sqrt(f_metric(R, M_in)) - math.sqrt(f_metric(R, M_out)))


def potential(R, M_in, M_out, ms):
    dM = M_out - M_in
    return 1.0 - 2.0 * M_out / R - (dM / ms - ms / (2.0 * R)) ** 2


def _ms_at(R, R0, M_in, M_out, beta2, n=200):
    """Evolve m_s by the conservation law m_s' = -8 pi R p, EOS p' = beta2 sigma'."""
    ms0 = ms_static(R0, M_in, M_out)
    s0 = ms0 / (4.0 * math.pi * R0 * R0)
    p0 = pressure(R0, M_in, M_out)
    ms, h = ms0, (R - R0) / n
    for i in range(n):
        r = R0 + (i + 0.5) * h
        s = ms / (4.0 * math.pi * r * r)
        ms += -8.0 * math.pi * r * (p0 + beta2 * (s - s0)) * h
    return ms


def V_second(R0, M_in, M_out, beta2, h=1e-5):
    """V''(R0).  Positive is STABLE."""
    ms0 = ms_static(R0, M_in, M_out)
    return (potential(R0 + h, M_in, M_out, _ms_at(R0 + h, R0, M_in, M_out, beta2))
            - 2.0 * potential(R0, M_in, M_out, ms0)
            + potential(R0 - h, M_in, M_out, _ms_at(R0 - h, R0, M_in, M_out, beta2))
            ) / (h * h)


def beta2_crit(R0, M_in, M_out, lo=-3.0, hi=10.0, iters=60):
    """The stiffness the matter must supply.  Negative means none is needed."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if V_second(R0, M_in, M_out, mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def device(m, R=1.0):
    """concentric.py's configuration: negative core inside, flat outside."""
    return (R, -m, 0.0)


def ordinary(M, R=1.0):
    """The textbook shell: flat inside, mass outside."""
    return (R, 0.0, M)


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-58s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The junction is consistent: a static shell sits at V = 0")
    for m in (0.01, 0.1, 0.5):
        R, Mi, Mo = device(m)
        near("m/R=%.2f  V(R0)" % m, potential(R, Mi, Mo, ms_static(R, Mi, Mo)), 0.0, 1e-12)

    print("\nTHE SHELL IS ORDINARY MATTER")
    print("     %8s %14s %14s %10s %10s" % ("m/R", "sigma", "p", "NEC", "DEC"))
    for m in (0.01, 0.1, 0.5, 2.0):
        R, Mi, Mo = device(m)
        print("     %8.2f %+14.5e %+14.5e %10s %10s"
              % (m, sigma(R, Mi, Mo), pressure(R, Mi, Mo),
                 "yes" if nec_holds(R, Mi, Mo) else "NO",
                 "yes" if dec_holds(R, Mi, Mo) else "NO"))
    chk("sigma > 0 at every compactness",
        all(sigma(*device(m)) > 0 for m in (0.01, 0.1, 0.5, 2.0)), True)
    chk("the pressure is a TENSION, not a pressure",
        all(pressure(*device(m)) < 0 for m in (0.01, 0.1, 0.5, 2.0)), True)
    chk("DOMINANT energy condition holds throughout",
        all(dec_holds(*device(m)) for m in (0.01, 0.1, 0.5, 2.0)), True)

    print("\nVALIDATION -- the ORDINARY shell must come out UNSTABLE at beta^2 = 0")
    print("     %8s %18s" % ("M/R", "V''(0)"))
    for M in (0.01, 0.1, 0.2):
        v = V_second(*ordinary(M), beta2=0.0)
        print("     %8.2f %+18.6e" % (M, v))
    chk("a dust shell with mass outside is unstable, as it must be",
        all(V_second(*ordinary(M), beta2=0.0) < 0 for M in (0.01, 0.1, 0.2)), True)

    print("\nAND OUR DEVICE COMES OUT STABLE, ON THE SAME MACHINERY")
    print("     %8s %18s %14s" % ("m/R", "V''(0)", "beta2_crit"))
    for m in (0.01, 0.1, 0.5):
        R, Mi, Mo = device(m)
        print("     %8.2f %+18.6e %+14.6f"
              % (m, V_second(R, Mi, Mo, 0.0), beta2_crit(R, Mi, Mo)))
    chk("V'' > 0 with NO pressure response at all",
        all(V_second(*device(m), beta2=0.0) > 0 for m in (0.01, 0.1, 0.5)), True)
    chk("beta2_crit is NEGATIVE, so any ordinary matter clears it",
        all(beta2_crit(*device(m)) < 0 for m in (0.01, 0.1, 0.5)), True)

    print("\nThe two are near mirror images -- it is the interior sign, nothing else")
    a = V_second(*ordinary(0.01), beta2=0.0)
    b = V_second(*device(0.01), beta2=0.0)
    near("V''(ordinary) + V''(device) at 0.01, relative to |V''|",
         (a + b) / abs(a), 0.0, 0.03)
    print("       %+.6e and %+.6e.  Same magnitude, opposite sign." % (a, b))
    print("       THIRD appearance of one sign structure: Weyl focusing without")
    print("       positive energy, a lead instead of a lag, and now stability.")

    print("\nThe core's position is NEUTRAL, exactly")
    print("     Newton's shell theorem: the field vanishes at EVERY interior point,")
    print("     so the core feels no force wherever it sits.  Neither stable nor")
    print("     unstable, and recorded as neither.")

    print("\nNOT RUN -- and the first is the top remaining risk")
    for i, s in enumerate((
            "l >= 2 non-radial modes.  THIS KILLED THE WARPSHELL.",
            "l = 1, the core displaced: a dipole deformation of the shell.",
            "the core's own stability -- deferred with the identification phase.",
            "the linearised-field caution from concentric.py, unchanged."), 1):
        print("     %d. %s" % (i, s))
    print("     PSP's shells have M_in >= 0 and M_out > 0; ours has M_in < 0 and")
    print("     M_out = 0, and the RADIAL mode already flipped under exactly that")
    print("     exchange.  A reason to expect, never a reason to assume.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SHELL")
    print("  %8s %14s %14s %8s %8s %16s %12s"
          % ("m/R", "sigma", "p", "NEC", "DEC", "V''(beta2=0)", "beta2_crit"))
    for m in (0.01, 0.05, 0.1, 0.25, 0.5, 1.0):
        R, Mi, Mo = device(m)
        print("  %8.2f %+14.5e %+14.5e %8s %8s %+16.6e %+12.5f"
              % (m, sigma(R, Mi, Mo), pressure(R, Mi, Mo),
                 "yes" if nec_holds(R, Mi, Mo) else "NO",
                 "yes" if dec_holds(R, Mi, Mo) else "NO",
                 V_second(R, Mi, Mo, 0.0), beta2_crit(R, Mi, Mo)))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The shell is ORDINARY MATTER -- positive surface density, a small")
    print("  tension, dominant energy condition satisfied at every compactness")
    print("  measured.  And it is RADIALLY STABLE WITH NO PRESSURE RESPONSE AT")
    print("  ALL: beta^2_crit is negative everywhere, where the textbook shell")
    print("  with the same machinery comes out unstable.  Flipping the sign of")
    print("  the interior mass flips the curvature of the effective potential.")
    print("\n  NOT RUN, and it is what killed the last architecture: the l >= 2")
    print("  non-radial modes.  Top remaining risk to the device.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
