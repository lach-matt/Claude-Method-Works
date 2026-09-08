#!/usr/bin/env python3
"""
spec.py -- the device that is actually achievable, specified.

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

-- THE DESIGN EQUATION, AND IT IS ONE INVARIANT -------------------------------
seatindex.py's universal seating condition is q l^2 >= pi^2 with q = 4 pi T_kk,
so in SI a sustained field of energy density u seats at

        l = sqrt( pi c^4 / (4 G u) )

and for a magnetic field, u = B^2/2 mu_0, the two collapse into one number:

        B * l  =  sqrt( 2 mu_0 * pi c^4 / (4 G) )  =  1.5456e19  T m

    THAT IS THE SPECIFICATION.  One invariant, real units, no free parameters.
    Field strength and range trade exactly inversely, and the product is fixed
    by c, G and mu_0 alone.

Cross-checked two ways that do not share a formula: q = (4 pi G/c^4) T_kk gives
pi/sqrt(q) = 1.5456e8 m at B = 1e11 T, and seatindex.py's threshold gives
1.5456e8 m.  Same number, different route.

        field source                 B (T)      seats beyond
        continuous lab magnet        45         3.435e17 m   (36 ly)
        destructive pulsed           1.2e3      1.288e16 m   (1.4 ly)
        theoretical material limit   1e4        1.546e15 m   (0.16 ly)
        neutron star surface         1e8        1.546e11 m
        MAGNETAR                     1e11       1.546e08 m   (155,000 km)
        magnetar interior (est.)     1e12       1.546e07 m   (15,500 km)

-- WHAT THE GAP IS NOW, AND IT IS A DIFFERENT KIND OF THING -------------------
Against the strongest field humans have made -- 1200 T, destructively pulsed --
reaching magnetar class is 8.3e7 in field and 6.9e15 in energy density.

    THAT IS AN ENGINEERING GAP AGAINST NO THEOREM.  Nothing forbids it.  It is
    not comparable to achievable.py's 65 orders, which was a gap against
    Ford-Roman and widened with scale.  This one CLOSES with scale: a weaker
    field simply seats further out, on the B l = const line, and nature already
    operates at the strong end of it.

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
    """B * l = sqrt(2 mu_0 pi c^4 / 4G).  The whole specification, one number."""
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
    "establish a conjugate point at a declared range",
    "using a sustained field of ordinary matter",
    "in a vacuum corridor, NEC/WEC/DEC satisfied everywhere",
    "universal in Sturm's sense: nothing outside the stretch can prevent it",
    "past it the geodesic is not achronal, so a timelike curve A->B exists",
)
DOES_NOT = (
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

    print("THE DESIGN EQUATION -- one invariant, real units")
    inv = seating_invariant()
    near("B * l  (T m)", inv, 1.54562e19, 1e-5)
    print("       B l = sqrt(2 mu_0 pi c^4 / 4G).  Fixed by c, G and mu_0 alone.")

    print("\n   Cross-checked by a route that shares no formula")
    for B in (1.0e8, 1.0e11, 1.0e12):
        near("B=%.0e T: pi/sqrt(q) vs invariant/B" % B,
             conjugate_length_from_q(energy_density(B)), range_for_field(B), 1e-9)

    print("\nTHE TRADE CURVE -- field and range trade exactly inversely")
    print("     %28s %10s %16s %12s" % ("source", "B (T)", "seats beyond (m)", "ly"))
    for tag, B in FIELDS:
        l = range_for_field(B)
        print("     %28s %10.3g %16.4e %12.3e" % (tag, B, l, l / LIGHT_YEAR))
    chk("the product is constant across eleven orders in B",
        all(abs(B * range_for_field(B) / inv - 1.0) < 1e-12 for _t, B in FIELDS), True)
    near("a magnetar seats at 155,000 km", range_for_field(1.0e11), 1.5456e8, 1e-4)

    print("\nTHE GAP IS ENGINEERING, AGAINST NO THEOREM")
    gb, gu = engineering_gap()
    near("field ratio to magnetar class", gb, 8.333e7, 1e-3)
    near("energy-density ratio", gu, 6.944e15, 1e-3)
    import achievable
    chk("and it is NOT comparable to the lead's 65 orders",
        achievable.ratio(1.0) < 1e-60, True)
    chk("that one WIDENED with scale", achievable.gap_widens_with_size(), True)
    chk("this one CLOSES with scale -- weaker field, longer range",
        range_for_field(45.0) > range_for_field(1.0e11), True)
    print("       B l = const is a line you can walk in either direction.")

    print("\nWHAT IT DOES")
    for d in DOES:
        print("     + %s" % d)
    print("\nWHAT IT DOES NOT")
    for d in DOES_NOT:
        print("     - %s" % d)
    chk("five things it does", len(DOES), 5)
    chk("four it does not", len(DOES_NOT), 4)

    print("\nCONSISTENCY with the instruments this inherits from")
    import seatindex, charge, transit
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
    print("  Under M's scoping -- the matter must exist at both ends under the")
    print("  same physics, nothing more -- the lead is not required and the seat")
    print("  is achievable.  The whole specification is one invariant,")
    print("  B l = 1.5456e19 T m, fixed by c, G and mu_0 alone, and field")
    print("  strength trades exactly inversely against range.")
    print("\n  It establishes a controlled gravitational focus at a chosen range,")
    print("  from matter satisfying every energy condition, in a vacuum corridor.")
    print("  It does not beat light, does not shortcut, and needs nothing exotic.")
    print("\n  The remaining gap is 8.3e7 in field strength -- engineering against")
    print("  no theorem, on a line that closes as you walk out in range.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
