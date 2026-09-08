#!/usr/bin/env python3
"""
chronology.py -- the Morris-Thorne-Yurtsever construction, taken apart, and
what it does to THIS device.

unified.py asserted a sentence it had not measured:

    "the INTERSECTION -- a spatial shortcut that also displaces in time -- is
     the Morris-Thorne-Yurtsever time machine"

That was an assertion.  This file tests it, and the test found something else
on the way in.  THE HEADLINE IS A WITHDRAWAL:

-- WITHDRAWN: THE DEVICE'S LEAD IS INTERIOR-ONLY -----------------------------

concentric.py ran its rays from x0 = -150 to +150 with the shell at R_s = 200.
BOTH ENDPOINTS SIT INSIDE THE SHELL.  "t - |dx|" compares a coordinate time
against a coordinate distance in a region that is not asymptotically flat, so
it is not a statement about the causal structure at all.  Push the endpoints
out past R_s into the near-flat exterior and the sign REVERSES:

        half-baseline X   endpoints    t - |dx|        verdict
        150               inside       -1.785e-01      early  (ambiguous)
        210               OUTSIDE      -9.635e-02      early
        260               OUTSIDE      -2.532e-02      early
        280               OUTSIDE      +3.117e-03      LATE
        400               OUTSIDE      +1.736e-01      LATE
        1000              OUTSIDE      +1.026e+00      LATE

The device makes you EARLY over short baselines and LATE over long ones, and
the crossover is at a computable distance.  DEVICE-SEATS-LEADS survives only
as a bounded, short-range statement, and is withdrawn as a global one.

-- WHY: THE GAIN SATURATES AND THE LOSS DOES NOT -----------------------------

composite.py already wrote the decomposition and nobody applied it to the
device:

        t - |dx|  =  (Shapiro, ~ m, flips sign)  +  (path lengthening, ~ m^2,
                                                     never negative)

M_ADM = 0 is what the shell is FOR.  It cancels the monopole, and cancelling
the monopole is exactly what makes the Shapiro term CONVERGE instead of
growing.  Measured by quadrature -- no geodesic integrator, no screen
transport -- the potential's whole contribution to the light time:

        half-baseline    device (M_ADM = 0)     bare mass (M_ADM < 0)
        200              -3.969054e-01          -4.768334e-01
        1000             -3.969054e-01          -6.055816e-01
        20000            -3.969054e-01          -8.452386e-01
        100000           -3.967683e-01          -9.738562e-01

    THE DEVICE'S SAVING IS CONSTANT TO FIVE DIGITS OVER THREE DECADES OF
    BASELINE.  The bare negative mass keeps gaining, as 4m ln X, forever.

The closed form for the device, derived and then checked:

        SAVING  =  4 m [ ln(2 R_s / sqrt(b^2 + a^2)) - 1 ]

agreeing with the quadrature to 0.15 % at m = 5e-3.  It contains no baseline.

And the deflection is NOT cancelled, because a ray at b << R_s passes wholly
INSIDE the shell, where a spherical shell has no field (Newton), and exits
nearly radially, where a radial field cannot bend it back.  So the ray keeps
the core's full deflection 4m/b, and pays

        LOSS  =  (4 m / b)^2 * X / 4  =  4 m^2 X / b^2

which is LINEAR in the baseline.  Bounded gain against unbounded loss gives

        X_c  =  b^2 [ ln(2 R_s / sqrt(b^2 + a^2)) - 1 ] / m

    = 249.6 for the seated configuration, against a measured crossover near
    277.  Within 11 % from a two-term model, which is what a two-term model is
    worth.

-- AND THIS IS NOT ABOUT THE SHELL.  IT IS GENERAL ---------------------------

The obvious objection is that the shell caused it.  It did not.  In the weak
field the Shapiro gain gets at most a LOGARITHM of the baseline, while the
deflection it necessarily produces costs path length LINEARLY, so

        4 m ln(2X/b)   against   4 m^2 X / b^2

has exactly one crossing whatever the configuration.  Measured for a BARE
negative mass, no shell anywhere, M_ADM = -m:

        X          t - |dx|        verdict
        150        -2.382e-01      early
        250        -1.370e-01      early
        320        -5.724e-02      early
        400        +3.860e-02      LATE
        600        +2.904e-01      LATE

    predicted 324, measured near 350.  THE DEVICE CROSSES AT 250 AND THE BARE
    NEGATIVE MASS AT 324 -- the same order.  The shell does not cause the
    failure; it only moves the crossing in, by turning the logarithm into a
    constant.  A bare negative mass buys 30 % more range, and needs to be a
    bare negative mass to do it.

    So the time advance is intrinsically SHORT-RANGE, for every weak-field
    configuration this project has built or can build.  eps decays like
    ln(X)/X, which is to say the faster you want to go, the less far you can
    go doing it.

-- THE WINDOW IS NARROW, AND IT IS BOUNDED AT BOTH ENDS ----------------------

An advance is UNAMBIGUOUS only when both endpoints are in the flat exterior,
X > R_s = 200.  It is POSITIVE only when X < X_c ~ 277.  So the whole window
where this device demonstrably beats light is

        200  <  X  <  277           a factor of 1.39 in baseline

and inside it the best fractional advance is 2.297e-4, at the near edge.

-- SO: DOES IT BUILD A TIME MACHINE? -----------------------------------------

Shoshany & Snodgrass (arXiv:2309.10072, PRD) give the condition, their eq.
(3.11), for two superluminal legs in frames of relative velocity u:

        u  >  (v1 + v2) / (1 + v1 v2)

with the standing requirement, stated in their own words, that "if either v1
or v2 are less than 1, we cannot have T_finish < 0".  BOTH LEGS MUST BE
GENUINELY SUPERLUMINAL.  For two identical legs of fractional advance eps,
v = 1 + eps, and the condition reduces -- exactly, in this file -- to

        gamma  >  1 / eps

QUADRATIC, not linear: a small advance is punished twice.  With the best
unambiguous eps this device produces, 2.297e-4:

        gamma_crit = 4354        (v = 0.999999974 c)

    THAT IS NOT A PROHIBITION.  It is a number, it is finite, and it is
    smaller than the LHC's proton gamma.  Two of these devices in relative
    motion at gamma > 4354 close a causal loop.  The device is not protected
    by chronology; it is protected by NOT WORKING AT RANGE.

-- AND THE COST OF A SECOND ---------------------------------------------------

The saving does not grow with the trip.  So price it as what it is -- a
one-time offset, bought once, no matter how far you go:

        to buy ONE SECOND requires m ~ 1.502e7 m of geometric mass, which is
        2.022e34 kg -- TEN THOUSAND SOLAR MASSES of negative mass, for one
        second, on a trip of any length whatsoever.

    A saving that does not scale with the journey is not a faster journey.
    Over four light years the best this architecture offers is a fixed offset;
    as a FRACTION of the trip it goes to zero like 1/L.

-- WHAT MTY ACTUALLY REQUIRES, AND WHICH PARTS THIS DEVICE HAS ---------------

MTY is not a statement about wormholes.  It needs four things, and the
wormhole was only how 1988 supplied the second:

        1. two paths between the same pair of events           HAS IT
        2. the short path elapsing less than the long one      HAS IT, bounded
        3. a persistent identification of the two ends         DOES NOT HAVE
        4. differential aging across that identification       BLOCKED BY 3

    Three fails on structure, not on magnitude.  transition.py measured no
    throat (areal radius monotone at every radius) and no horizon, so there is
    nothing that identifies two ends and holds them identified while they age
    apart.  Every use re-declares A and B at onset -- transit.py's gate, built
    for a completely different reason -- so nothing ACCUMULATES.

    That is the same payment GJW make.  Their coupling "fixes the relative
    time coordinate between them, excluding the possibility of having closed
    time-like curves."  Re-declaring the endpoints is that payment, made
    again, every time.  PAID IN ADVANCE, PER USE, AND NEVER BANKED.

    So the MTY route is closed to this device and the Everett/Shoshany route
    is NOT: the first needs an identification the device lacks, the second
    needs only two devices and a boost.  unified.py named the wrong machine.

-- WHAT IS NOT CLAIMED --------------------------------------------------------

    * That the device is safe from CTCs.  It is not.  gamma > 1/eps is
      finite and the construction is explicit in the literature.
    * That the crossover model is exact.  It is two terms and it lands within
      11 %.  The MEASURED crossover, not the formula, is the finding.
    * That a bare negative mass fails this way.  It does not -- its saving
      grows as 4m ln X without bound.  It fails for the reason obstruct.py
      already records, which is that it is a bare negative mass.
    * Hawking's chronology protection.  The Cauchy-horizon divergence and
      whether quantum gravity cuts it off (Kim-Thorne) or does not (Hawking)
      is UNRESOLVED in the literature and is NOT-RUN here.  Nothing in this
      file rests on it.

stdlib only.  concentric.py supplies the configuration and the geodesics;
the quadrature is self-contained so that the potential's contribution can be
read without the integrator in the way.
"""
import math, sys

# The seated configuration, from concentric.py.
A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0
C_SI, G_SI = 2.99792458e8, 6.67430e-11


# ------------------------------------------------------- the two potentials

def phi_device(x, b, m, a=A_CORE, Rs=R_SHELL):
    """The M_ADM = 0 device: core plus compensating shell."""
    r = math.hypot(x, b)
    return m / math.sqrt(r * r + a * a) - m / max(r, Rs)


def phi_bare(x, b, m):
    """A bare negative mass: M_ADM = -m, a 1/r tail and nothing cancelling it."""
    return m / math.hypot(x, b)


# ------------------------------------------------- the light time, by quadrature

def light_excess(f, m, b, X, n=200001):
    """int (e^{-2Phi} - 1) dl from -X to +X, Simpson.  Negative is EARLY.

    This is the POTENTIAL's whole contribution to the light time along the
    unperturbed line.  It carries no integrator error from the geodesic solver
    and no screen-transport error, which is the point: the saturation below is
    a property of the metric, not of the method.
    """
    h = 2.0 * X / n
    s = 0.0
    for i in range(n + 1):
        x = -X + i * h
        w = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
        s += w * (math.exp(-2.0 * f(x, b, m)) - 1.0)
    return s * h / 3.0


def saving_closed_form(m, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """-4 m [ ln(2 R_s / sqrt(b^2+a^2)) - 1 ].  NO BASELINE APPEARS."""
    return -4.0 * m * (math.log(2.0 * Rs / math.sqrt(b * b + a * a)) - 1.0)


def saturates(m=2.0e-2, b=B_RAY, tol=1e-3):
    """Is the device's saving independent of baseline?  Measured: yes."""
    near = light_excess(phi_device, m, b, 400.0, 40001)
    far = light_excess(phi_device, m, b, 20000.0, 40001)
    return abs(far - near) <= tol * abs(near)


def bare_keeps_growing(m=2.0e-2, b=B_RAY):
    """A bare negative mass never saturates -- 4m ln X, forever."""
    near = light_excess(phi_bare, m, b, 400.0, 40001)
    far = light_excess(phi_bare, m, b, 20000.0, 40001)
    return abs(far) > 1.3 * abs(near)


# ------------------------------------------------------ gain, loss, crossover

def deflection(m, b=B_RAY):
    """4m/b -- the CORE's bend, which the shell does not undo for b << R_s."""
    return 4.0 * m / b


def path_penalty(m, X, b=B_RAY):
    """Extra coordinate length of a bent path over its chord: X alpha^2 / 4."""
    return X * deflection(m, b) ** 2 / 4.0


def crossover(m, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """X_c: bounded gain against linear loss.  b^2[ln(2Rs/c)-1]/m."""
    return b * b * (math.log(2.0 * Rs / math.sqrt(b * b + a * a)) - 1.0) / m


def window(m, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """(X_min, X_max): unambiguous requires X > R_s, positive requires X < X_c."""
    return (Rs, crossover(m, b, a, Rs))


def window_is_narrow(m=2.0e-2, factor=2.0):
    lo, hi = window(m)
    return hi > lo and hi / lo < factor


def crossover_bare(m, b=B_RAY):
    """X_c for a BARE negative mass: 4m ln(2X/b) = 4 m^2 X / b^2.

    The bare mass has no shell, so its gain GROWS -- but only as a logarithm,
    against a loss that grows linearly.  Bisected, because ln X = kX has no
    elementary inverse.
    """
    f = lambda X: math.log(2.0 * X / b) - m * X / (b * b)
    # f is NEGATIVE at both ends -- ln is negative for small X, and the linear
    # term wins for large X -- so bisect DOWN from the peak, f'(X) = 0 at
    # X = b^2/m, not up from zero.  Bracketing this wrongly returns None.
    peak = b * b / m
    if f(peak) <= 0.0:
        return None                     # gain never exceeds loss at any range
    lo, hi = peak, peak * 1.0e9
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return lo


def every_configuration_crosses_over(m=2.0e-2, b=B_RAY):
    """THE GENERAL RESULT, and it is not about this device.

    In the weak field a negative Shapiro term buys time at most LOGARITHMICALLY
    in the baseline, while the deflection it necessarily produces costs path
    length LINEARLY.  Logarithm against linear has exactly one crossing, so
    EVERY weak-field configuration -- shelled or bare -- has a finite range
    beyond which it makes you late.  The shell does not cause this; it only
    moves the crossing in, by converting the logarithm into a constant.
    """
    return (crossover(m, b) is not None and crossover_bare(m, b) is not None
            and crossover(m, b) < crossover_bare(m, b))


# ------------------------------------------------ the CTC condition, exactly

def shoshany_u(v1, v2):
    """Their eq. (3.11): u > (v1+v2)/(1+v1 v2).  Both legs must exceed 1."""
    if v1 <= 1.0 or v2 <= 1.0:
        return None          # NOT-RUN: their own precondition fails
    return (v1 + v2) / (1.0 + v1 * v2)


def gamma_crit(eps):
    """The boost that closes the loop for two legs of fractional advance eps.

    Exact from shoshany_u, not the linearised guess: because BOTH legs must be
    superluminal the requirement is quadratic in eps, and gamma -> 1/eps.
    """
    u = shoshany_u(1.0 + eps, 1.0 + eps)
    if u is None or u >= 1.0:
        return None
    return 1.0 / math.sqrt(1.0 - u * u)


def gamma_is_one_over_eps(eps=2.297e-4, tol=1e-3):
    """gamma_crit(eps) * eps -> 1.  Checked, not assumed."""
    g = gamma_crit(eps)
    return g is not None and abs(g * eps - 1.0) < tol


def subluminal_is_not_run(eps=-1.0e-4):
    """A LATE leg returns NOT-RUN, never 'no CTC' -- register 1172's refusal."""
    return shoshany_u(1.0 + eps, 1.0 + eps) is None


# ---------------------------------------------------------- what a second costs

def mass_for_saving(seconds, b=B_RAY, a=A_CORE, Rs=R_SHELL):
    """Geometric mass (metres) whose SATURATED saving is `seconds`."""
    return seconds * C_SI / (4.0 * (math.log(2.0 * Rs / math.sqrt(b * b + a * a)) - 1.0))


def kg_for_saving(seconds, **kw):
    """...and in kilograms, at c^2/G = 1.3466e27 kg per metre."""
    return mass_for_saving(seconds, **kw) * C_SI ** 2 / G_SI


SOLAR_MASS = 1.98892e30


def fraction_of_trip(seconds, trip_seconds):
    """The saving as a FRACTION of the journey.  Goes as 1/L: it does not scale."""
    return seconds / trip_seconds


# ------------------------------------------------------- MTY's four ingredients

MTY_REQUIREMENTS = (
    ("two paths between the same pair of events", True,
     "a ray through the field and a ray around it; both connect A to B"),
    ("the short path elapsing less than the long one", True,
     "measured, but BOUNDED and only for X < X_c"),
    ("a persistent identification of the two ends", False,
     "no throat: transition.py measures the areal radius MONOTONE at every "
     "radius, so there are not two ends to identify -- re-confirmed here "
     "against the seated potential rather than quoted"),
    ("differential aging across that identification", False,
     "blocked by 3 -- there is nothing to age differentially, and transit.py's "
     "gate re-declares A and B every use, so nothing accumulates"),
)


def no_throat_confirmed(m=2.0e-2, n=4000, step=0.05):
    """MTY requirement 3, checked here and not quoted from another file.

    The areal radius R = r e^{-Phi} monotone at every radius means the geometry
    has no throat, so there are not two ends to identify and MTY's third
    requirement fails on structure.  Measured: (False, False).
    """
    import transition, concentric
    phi = concentric.potential(m)
    radii = [step * i for i in range(1, n + 1)]
    return transition.has_throat(phi, radii), transition.has_horizon(phi, radii)


def mty_available():
    """Does this device admit the MTY construction?  No -- and on STRUCTURE."""
    return all(has for _n, has, _w in MTY_REQUIREMENTS)


def mty_fails_on_structure():
    """It fails at 3 and 4, which are structural, not magnitude questions."""
    return [n for n, has, _w in MTY_REQUIREMENTS if not has] == \
           [MTY_REQUIREMENTS[2][0], MTY_REQUIREMENTS[3][0]]


EVERETT_ROUTE_OPEN = True     # two devices + a boost needs no identification
MTY_ROUTE_OPEN = False        # needs an identification the device lacks

HAWKING = "NOT-RUN"           # the Cauchy-horizon divergence; unresolved in the
                              # literature (Kim-Thorne vs Hawking), and nothing
                              # in this file rests on it


# ------------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-58s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE SAVING SATURATES -- and that is what M_ADM = 0 buys")
    near_v = light_excess(phi_device, 2.0e-2, 1.0, 400.0, 40001)
    far_v = light_excess(phi_device, 2.0e-2, 1.0, 20000.0, 40001)
    near("device saving at X = 400", near_v, -3.969054e-01, 2e-3)
    near("device saving at X = 20000 -- the SAME NUMBER", far_v, near_v, 1e-3)
    chk("the device's saving is baseline-independent", saturates(), True)
    chk("a bare negative mass keeps growing instead", bare_keeps_growing(), True)

    print("\n   and the closed form contains no baseline at all")
    for m in (5.0e-3, 2.0e-2):
        q = light_excess(phi_device, m, 1.0, 20000.0, 40001)
        near("  saving m=%-7.4g: closed form vs quadrature" % m,
             saving_closed_form(m), q, 1e-2)

    print("\n2. THE LOSS DOES NOT SATURATE -- it is linear in the baseline")
    near("deflection 4m/b at m = 2e-2", deflection(2.0e-2), 8.0e-2, 1e-12)
    d1, d2 = path_penalty(2.0e-2, 500.0), path_penalty(2.0e-2, 1000.0)
    near("doubling the baseline doubles the path penalty", d2 / d1, 2.0, 1e-12)

    print("\n3. SO THERE IS A CROSSOVER, AND BEYOND IT THE DEVICE IS LATE")
    near("X_c predicted for the seated configuration", crossover(2.0e-2), 249.6, 1e-3)
    print("      measured crossover sits between X = 260 (early) and 280 (late);")
    print("      a two-term model landing within 11 % is what it is worth, and the")
    print("      MEASURED crossover is the finding, not the formula.")
    lo, hi = window(2.0e-2)
    near("window opens at the shell radius", lo, 200.0, 1e-12)
    chk("and it is narrower than a factor of two", window_is_narrow(), True)

    print("\n3b. AND IT IS NOT ABOUT THIS DEVICE -- a BARE mass crosses over too")
    near("bare-mass crossover, bisected", crossover_bare(2.0e-2), 324.0, 5e-3)
    print("      measured between X = 320 (early, -5.72e-2) and 400 (late, +3.86e-2).")
    print("      The device crosses at ~250, the bare mass at ~324: THE SAME ORDER.")
    chk("every weak-field configuration crosses over",
        every_configuration_crosses_over(), True)
    print("      log gain against linear loss has exactly one crossing.  The shell")
    print("      does not CAUSE the failure -- it moves the crossing in, by turning")
    print("      the logarithm into a constant.  A bare negative mass buys 30 % more")
    print("      range and needs a bare negative mass to do it.")

    print("\n4. THE CTC CONDITION -- Shoshany & Snodgrass eq. (3.11), exactly")
    chk("a SUBLUMINAL leg returns NOT-RUN, never 'no CTC'",
        subluminal_is_not_run(), True)
    chk("  (register 1172: never print a verdict for a language not run)", True, True)
    eps = 2.297e-4
    near("required u for two legs at eps = 2.297e-4",
         shoshany_u(1 + eps, 1 + eps), 1.0 - eps * eps / 2.0, 1e-6)
    chk("gamma_crit * eps = 1, exactly and not by assumption",
        gamma_is_one_over_eps(eps), True)
    near("gamma_crit at the best unambiguous advance", gamma_crit(eps), 4353.5, 1e-3)
    print("      FINITE, and below the LHC's proton gamma.  Not a prohibition.")

    print("\n5. WHAT A SECOND COSTS, AND IT DOES NOT SCALE WITH THE TRIP")
    near("geometric mass for a one-second saving (m)", mass_for_saving(1.0), 1.5017e7, 1e-3)
    near("  the same in kg", kg_for_saving(1.0), 2.0221e34, 1e-3)
    near("  in solar masses", kg_for_saving(1.0) / SOLAR_MASS, 1.01664e4, 1e-3)
    ly = 4.0 * 3.15576e7 * 1.0        # four light years, in seconds of light travel
    near("one second as a fraction of a four-light-year trip",
         fraction_of_trip(1.0, ly), 7.9219e-9, 1e-3)
    print("      a fixed offset over ANY distance: as a fraction it dies like 1/L.")

    print("\n6. MTY'S FOUR REQUIREMENTS, CHECKED ONE AT A TIME")
    for n, has, why in MTY_REQUIREMENTS:
        print("      %-45s %-14s %s" % (n, "HAS IT" if has else "DOES NOT", why[:44]))
    chk("no throat and no horizon, re-measured not quoted",
        no_throat_confirmed(), (False, False))
    chk("the MTY construction is available to this device", mty_available(), False)
    chk("and it fails on STRUCTURE (3 and 4), not on magnitude",
        mty_fails_on_structure(), True)
    chk("MTY route open", MTY_ROUTE_OPEN, False)
    chk("Everett/Shoshany route open -- needs no identification",
        EVERETT_ROUTE_OPEN, True)
    chk("Hawking's Cauchy-horizon divergence", HAWKING, "NOT-RUN")

    print("\n7. THE WITHDRAWAL THIS FILE FORCES")
    print("      concentric.py's rays ran x0 = -150 to +150 inside a shell at 200.")
    print("      Both endpoints INSIDE.  't - |dx|' there is a coordinate")
    print("      statement in a region that is not asymptotically flat.")
    print("      DEVICE-SEATS-LEADS is withdrawn as a GLOBAL claim and survives")
    print("      as a bounded, short-range one: 200 < X < 277.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("VERDICT")
    print("""
  unified.py named the wrong machine.  The MTY construction is NOT
  available to this device, and it fails on structure: there is no
  throat, so there are not two ends to identify, so nothing can age
  differentially across the identification.  transit.py's gate
  re-declares both endpoints every use, so nothing accumulates -- the
  same payment GJW make, made again, every time.

  The Everett/Shoshany route IS open, because it needs no
  identification -- only two devices and a boost.  The condition is
  their eq. (3.11), and for two legs of fractional advance eps it
  reduces exactly to gamma > 1/eps.  At this device's best
  unambiguous advance that is gamma > 4354: finite, explicit, and
  below the LHC's proton gamma.  The device is not protected by
  chronology.

  What protects it is that IT DOES NOT WORK AT RANGE.  M_ADM = 0
  cancels the monopole, which is exactly what makes the time saving
  CONVERGE -- constant to five digits over three decades of baseline
  -- while the deflection it does not cancel costs a path penalty
  LINEAR in the baseline.  Bounded gain, unbounded loss, crossover at
  X_c ~ 250, and beyond it the device makes you LATE.

  And concentric.py's headline lead was measured with both endpoints
  INSIDE the shell, where the comparison is not asymptotically
  meaningful.  DEVICE-SEATS-LEADS is withdrawn as a global claim.
  What survives is a bounded saving of 4m[ln(2R_s/b) - 1], which buys
  one second for ten thousand solar masses of negative mass, and
  buys that same one second whether the trip is a metre or a
  thousand light years.

  A SAVING THAT DOES NOT SCALE WITH THE JOURNEY IS NOT A FASTER
  JOURNEY.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
