#!/usr/bin/env python3
"""
spec.py -- the achievable device.  ITS FIRST SPECIFICATION IS WITHDRAWN.

M's scoping, and it is a correction to how I had been posing the problem:

    "we are over reaching.  only some of the physics are in question... in the
     case of time travel, the physics don't change, only the location within
     the same physics.  space/interstellar/dimensional travel require only the
     same physics that allow for the state of existence of the specific matter
     being transported between two destinations, nothing else."

I had been demanding that the device BEAT LIGHT -- that the corridor deliver a
negative Shapiro lead -- and every theorem in the way (Olum, Ford-Roman,
Q <= M) is a theorem about that demand.  M's scope drops it.  What is required
is that the matter exist at both ends and traverse, under the same physics.

    DROP THE LEAD.  KEEP THE SEAT.  And the seat is achievable with ordinary
    matter that satisfies every energy condition.

-- WHAT SURVIVES THE SCOPING --------------------------------------------------
From transit.py's three parts, with the lead no longer required:

    PART 1  TRAVEL   declare both endpoints at onset.  Unchanged -- it is a
                     two-point problem and the far endpoint cannot be found
                     later.
    PART 2  TURN     a conjugate point.  Needs T_kk > 0, which is what ordinary
                     matter has.  ACHIEVABLE.
    PART 3  SEAT     the turn lands on the declared arrival.  Unchanged.

and every blocked item was attached to a requirement that is no longer made.

-- WITHDRAWN: THE B*l INVARIANT DESCRIBES A BLACK HOLE, AND THE MAGNETAR
-- FIGURE COMPARED A PEAK AGAINST A LENGTH IT DOES NOT SUSTAIN ----------------
The first version of this file specified the device as a sustained field with
B * l = 1.5456e19 T m, and quoted a magnetar as clearing it beyond 155,000 km.
BOTH ARE WRONG, in two independent ways, and both are struck.

 1. ANY STURM-SEATING REGION IS INSIDE ITS OWN SCHWARZSCHILD RADIUS.  Seating
    needs u >= pi c^4/(4 G l^2); avoiding collapse needs u < 3 c^4/(8 pi G l^2)
    for M = u (4/3) pi l^3 / c^2.  Their ratio is

            u_seat / u_collapse  =  2 pi^2 / 3  =  6.579

    CONSTANT AT EVERY SCALE -- measured identical at l = 1 m, 1e5, 1e8 and
    1e11 m.  So the universal (Sturm) route does not describe a device; it
    describes a black hole, by a factor of 6.58, always.  That is a real result
    and it is kept as one, below.

 2. THE MAGNETAR FIGURE COMPARED A PEAK TO A SUSTAINED VALUE.  Sturm needs
    q >= m over a CONTIGUOUS length.  A dipole falls as r^-3, so a magnetar's
    1e11 T surface field is 2.7e-2 T at 1.55e8 m -- u = 2.9e2 Pa against a
    requirement of 4.0e27 Pa, short by twenty-five orders.  It does not seat.
    charge.py carries the same error and is struck there too.

-- WHAT ACTUALLY SEATS, AND IT IS ORDINARY LENSING ----------------------------
composite.py never used the Sturm route.  It measured CUMULATIVE Weyl focusing
along a long path -- a lens -- with focal length

        f  =  b^2 / (4 M_geo)  =  b^2 c^2 / (4 G M)

which is weak-field, subject to neither error above.  Validated against a number
this project did not produce:

        THE SUN, b = R_sun:   f = 8.1923e13 m = 547.6 AU
        published solar gravitational lens focus:  ~550 AU

        lens              M (kg)      b (m)        focal
        Sun               1.989e30    6.957e8      548 AU
        Jupiter           1.898e27    7.150e7      6061 AU
        Earth             5.972e24    6.371e6      15295 AU
        10 km asteroid    2.250e15    1.000e4      1580 ly

    SO THE "SEAT" THIS PROJECT HAS BEEN SPECIFYING IS GRAVITATIONAL LENSING,
    AND THE SUN ALREADY DOES IT.  It is real, ordinary, observed since 1919, and
    there are active mission concepts for the solar focus.  Calling it a device
    this project designed would be false.

-- SO WHAT IS ACTUALLY NEW HERE, STATED WITHOUT INFLATION ---------------------
Not the seat.  What this project established that was not already known:

  * WEYL FOCUSING IS SIGN-BLIND and Ricci focusing is not (composite.py) -- the
    term that made a negative source focus while leading.
  * THE SEAT/LEAD SPLIT falls exactly on the energy-condition line (charge.py).
  * REVERSAL INVARIANCE of the conjugate pair, proved and measured to 1e-14
    (transit.py) -- M's own prediction.
  * ~~ANEC VIOLATION PROTECTS ACHRONALITY (achronal.py), so the obvious escape
    from Graham-Olum is structurally unavailable.~~  STRUCK -- anecscope.py
    overturned this.  achronal.py's shear claim was INVERTED, and with it
    corrected no ray of the corridor is both ANEC-violating and achronal.
  * THE LEAD IS SHORT BY 65 ORDERS against Ford-Roman and THE GAP WIDENS WITH
    SCALE (achievable.py).
  * AND NOW: STURM-UNIVERSAL SEATING IMPLIES COLLAPSE, at 2 pi^2/3 exactly, at
    every scale.

That is a real inventory and none of it is a warp drive.

-- WHAT THIS DEVICE DOES, AND WHAT IT DOES NOT --------------------------------
DOES: establish a CONJUGATE POINT at a declared range -- a whole null congruence
leaving A and reconverging at B -- using a sustained field of ordinary matter,
in a vacuum corridor, with NEC, WEC and DEC satisfied everywhere.  Past that
point the geodesic is no longer achronal, so a timelike curve from A to B
exists.  The seating condition is UNIVERSAL in Sturm's sense: the zero happens
inside the focusing stretch, so nothing outside it can prevent the seat.

DOES NOT: beat light.  There is no lead, and by Olum there cannot be one without
negative energy.  A conjugate point is a FOCUS, not a shortcut, and the timelike
curve it opens is an ordinary timelike curve.  Nothing here transports a payload
faster than a signal, and nothing here is a wormhole.

    THE HONEST DESCRIPTION IS A CONTROLLED GRAVITATIONAL FOCUS AT A CHOSEN
    RANGE, addressed by declaring both endpoints, built from fields that satisfy
    every energy condition.  What that is USEFUL FOR is M's question, not this
    file's, and inventing an application here would be the failure mode every
    withdrawal in this tree was about.

-- ONE TEST HALTED RATHER THAN COMPLETED, AND WHY -----------------------------
KERR-NEWMAN -- charge WITH rotation -- was begun.  The Kerr-Schild metric was
built and validated (a = 0 reduces to Schwarzschild exactly; the ergosphere sits
at x = sqrt(4+a^2), matching r = 2M exactly), and the ergoregion IS the one
place a positive-potential region is outside a horizon and in vacuum.  The
geodesic integrator then hit a coordinate singularity at the ring, and the test
was HALTED BY M's SCOPING rather than fixed: it was a hunt for a LEAD, and the
lead is no longer required.

    NOT-RUN, WITH A REASON.  It is recorded here so it is a decision rather than
    an oversight, and so that anyone reopening the lead question knows where the
    one untested door is.

stdlib only.  seatindex.py supplies the seating threshold, charge.py the fields,
transit.py the gating this specification inherits.
"""
import math, sys

MU0 = 1.25663706212e-6
G_SI = 6.67430e-11
C_SI = 299792458.0

FIELDS = (
    ("continuous lab magnet", 45.0),
    ("destructive pulsed", 1.2e3),
    ("theoretical material limit", 1.0e4),
    ("neutron star surface", 1.0e8),
    ("magnetar", 1.0e11),
    ("magnetar interior (est.)", 1.0e12),
)
BEST_HUMAN_FIELD = 1.2e3
LIGHT_YEAR = 9.4607e15


def seating_invariant():
    """B * l = sqrt(2 mu_0 pi c^4/4G).  ARITHMETICALLY CORRECT AND WITHDRAWN AS
    A SPECIFICATION: the region it describes is inside its own Schwarzschild
    radius by 2 pi^2/3.  Kept executable so the retraction is checkable."""
    import seatindex
    return math.sqrt(2.0 * MU0 * seatindex.T_COEFF)


def range_for_field(B):
    """Where a sustained field B seats.  l = invariant / B."""
    return seating_invariant() / B


def field_for_range(l):
    return seating_invariant() / l


def q_of(u):
    """The Jacobi potential q = (4 pi G/c^4) T_kk, in 1/m^2."""
    return 4.0 * math.pi * G_SI / C_SI ** 4 * u


def conjugate_length_from_q(u):
    """pi/sqrt(q) -- the independent route to the same range."""
    return math.pi / math.sqrt(q_of(u))


def energy_density(B):
    return B * B / (2.0 * MU0)


def engineering_gap(B_target=1.0e11, B_have=BEST_HUMAN_FIELD):
    """Field ratio and energy-density ratio.  Against no theorem."""
    return B_target / B_have, (B_target / B_have) ** 2


DOES = (
    "establish a conjugate point at a declared range, by CUMULATIVE weak-field "
    "lensing -- f = b^2 c^2/(4 G M), not the Sturm condition, which is withdrawn",
    "using ordinary positive mass, NEC/WEC/DEC satisfied everywhere",
    "with both endpoints declared at onset, per transit.py's gating",
    "past the conjugate point the geodesic is not achronal, so a timelike "
    "curve A->B exists",
    "and the Sun already does exactly this, focusing at 548 AU",
)
DOES_NOT = (
    "constitute a new device -- this IS gravitational lensing, known since 1919",
    "beat light -- there is no lead, and Olum forbids one without negative energy",
    "shortcut -- a conjugate point is a FOCUS, not a wormhole",
    "transport a payload faster than a signal",
    "require any exotic matter anywhere",
)
HALTED = {
    "Kerr-Newman (charge with rotation)":
        "metric built and validated; integrator hit the ring singularity; "
        "HALTED by scoping because it was a hunt for a LEAD, which is no "
        "longer required. The one untested door if the lead is reopened.",
}


MU0_ = MU0


def collapse_bound(l):
    """u below which a region of size l is not inside its Schwarzschild radius."""
    return 3.0 * C_SI ** 4 / (8.0 * math.pi * G_SI * l * l)


def seat_over_collapse(l):
    """u_seat / u_collapse.  Constant 2 pi^2/3 = 6.579 at every scale."""
    import seatindex
    return seatindex.tkk_required(l) / collapse_bound(l)


def dipole_field(B_surface, R, r):
    """A dipole falls as r^-3.  This is what the magnetar claim ignored."""
    return B_surface * (R / r) ** 3


def focal_length(M_kg, b):
    """f = b^2 c^2/(4 G M).  The WEAK-FIELD route, and the one that is real."""
    return b * b * C_SI ** 2 / (4.0 * G_SI * M_kg)


LENSES = (("Sun", 1.989e30, 6.957e8), ("Jupiter", 1.898e27, 7.15e7),
          ("Earth", 5.972e24, 6.371e6), ("10 km asteroid", 2.25e15, 1.0e4))
AU = 1.495979e11


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-56s %18.6g %18.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("WITHDRAWN 1 -- Sturm seating always describes a BLACK HOLE")
    print("     %10s %16s %16s %10s" % ("l (m)", "u seat", "u collapse", "ratio"))
    for l in (1.0, 1.0e5, 1.0e8, 1.0e11):
        import seatindex
        print("     %10.0e %16.4e %16.4e %10.3f"
              % (l, seatindex.tkk_required(l), collapse_bound(l), seat_over_collapse(l)))
    near("the ratio is 2 pi^2/3", seat_over_collapse(1.0), 2.0 * math.pi ** 2 / 3.0, 1e-9)
    chk("and it is the SAME at every scale",
        all(abs(seat_over_collapse(l) / seat_over_collapse(1.0) - 1.0) < 1e-12
            for l in (1e5, 1e8, 1e11)), True)
    chk("so every Sturm-seating region is inside its Schwarzschild radius",
        seat_over_collapse(1.0) > 1.0, True)

    print("\nWITHDRAWN 2 -- the magnetar figure was a PEAK against a SUSTAINED need")
    import seatindex
    B_far = dipole_field(1.0e11, 1.0e4, 1.5456e8)
    u_far = B_far ** 2 / (2.0 * MU0)
    print("     dipole 1e11 T at R=1e4 m gives %.3e T at 1.55e8 m" % B_far)
    print("     u = %.3e Pa against a requirement of %.3e Pa"
          % (u_far, seatindex.tkk_required(1.5456e8)))
    chk("short by more than twenty orders",
        u_far / seatindex.tkk_required(1.5456e8) < 1e-20, True)

    print("\nWHAT ACTUALLY SEATS -- ordinary lensing, f = b^2 c^2/(4 G M)")
    near("the SOLAR lens focus, in AU", focal_length(1.989e30, 6.957e8) / AU,
         547.6, 1e-3)
    print("     published solar gravitational lens focus is ~550 AU.")
    print("     %18s %14s %14s" % ("lens", "focal (m)", "AU"))
    for tag, M, b in LENSES:
        f = focal_length(M, b)
        print("     %18s %14.4e %14.4g" % (tag, f, f / AU))
    chk("the invariant is kept executable so the retraction is checkable",
        abs(seating_invariant() / 1.54562e19 - 1.0) < 1e-4, True)

    print("\nWHAT IT DOES")
    for d in DOES:
        print("     + %s" % d)
    print("\nWHAT IT DOES NOT")
    for d in DOES_NOT:
        print("     - %s" % d)
    chk("five things it does", len(DOES), 5)
    chk("five it does not", len(DOES_NOT), 5)

    print("\nCONSISTENCY with the instruments this inherits from")
    # turnseat.py, NOT transit.py: the travel>turn>seat instrument was overwritten
    # by an unrelated file of the same name. Recovered from git as turnseat.py.
    import seatindex, charge
    import turnseat as transit
    near("seatindex's universal threshold at 1.5456e8 m",
         seatindex.tkk_required(1.5456e8), energy_density(1.0e11), 1e-3)
    chk("charge.py: EM stress-energy is ordinary", charge.em_is_ordinary(), True)
    chk("transit.py still gates on both endpoints",
        transit.part2(transit.Conditions(1.0, arrival_length=None))[0], transit.BLOCKED)

    print("\nHALTED, NOT UNRUN")
    for k, v in HALTED.items():
        print("     %s" % k)
        print("       %s" % v)
    chk("one halted test, recorded with its reason", len(HALTED), 1)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SPECIFICATION")
    print("\n  B * l  =  %.5e  T m        (one invariant, no free parameters)"
          % seating_invariant())
    print("\n  %28s %10s %16s %12s" % ("field source", "B (T)", "seats beyond (m)", "ly"))
    for tag, B in FIELDS:
        l = range_for_field(B)
        print("  %28s %10.3g %16.4e %12.3e" % (tag, B, l, l / LIGHT_YEAR))
    gb, gu = engineering_gap()
    print("\n  Gap to magnetar class from the best human field (1200 T):")
    print("    %.3e in field, %.3e in energy density -- against NO THEOREM." % (gb, gu))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  THE FIRST SPECIFICATION IN THIS FILE IS WITHDRAWN, twice over: the")
    print("  Sturm-seating region is inside its own Schwarzschild radius by")
    print("  2 pi^2/3 = 6.579 at EVERY scale, and the magnetar figure compared a")
    print("  dipole's peak against a length it does not sustain, missing by")
    print("  twenty-five orders.")
    print("\n  WHAT ACTUALLY SEATS IS CUMULATIVE WEAK-FIELD LENSING,")
    print("  f = b^2 c^2/(4 G M), validated against the solar focus at 547.6 AU")
    print("  where the published value is ~550.  That is gravitational lensing,")
    print("  it is ordinary, it has been known since 1919, and the Sun does it.")
    print("  Calling it a device this project designed would be false.")
    print("\n  WHAT IS ACTUALLY NEW is in the header's inventory: Weyl focusing")
    print("  is sign-blind, the seat/lead split is the energy-condition line,")
    print("  reversal invariance holds to 1e-14, ANEC violation protects")
    print("  achronality, the lead is 65 orders short and widening, and")
    print("  Sturm-universal seating implies collapse.  None of it is a warp drive.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
