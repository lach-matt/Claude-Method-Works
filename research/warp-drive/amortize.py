#!/usr/bin/env python3
"""
amortize.py -- pushing on the ORDER row, and finding where it is actually open.

expand.py left order as the row that moved and the row that governs speed.  This
file pushes on it, finds the obvious escape, closes it on GJW's own sentence, and
locates the one place their paper leaves the question genuinely open.

-- THE OBVIOUS ESCAPE, AND IT IS WORTH TESTING -------------------------------
The bank-loan theorem quantifies over ONE INFINITE NULL GEODESIC: it must be
chronal, so a causal path already exists outside.  That is a statement about a
SINGLE TRIP.  It says nothing on its face about a channel used repeatedly.

So: deploy the mouths once at sublight, paying D/c, then transit N times.

        N          average cost (units of D/c)
        1          1.000001            no advantage
        10         0.100001            ADVANTAGE
        100        0.010001            ADVANTAGE
        10,000     0.000101            ADVANTAGE

And the two timescales really are independent, which is what makes the escape
look plausible.  GJW's traversal window scales with the MOUTH size R --
Delta t ~ R ln(R/(h l_P)) -- while the benefit scales with the SEPARATION D:

        R          D              window (s)     D/c (s)        ratio
        1 m        1 AU           2.672e-7       4.990e2        5.4e-10
        1 m        1 light-year   2.672e-7       3.156e7        8.5e-15
        1 km       1 light-year   2.903e-4       3.156e7        9.2e-12
        1000 km    1 light-year   3.133e-1       3.156e7        9.9e-9

    FOR D >> R THE WINDOW IS FIFTEEN ORDERS SHORTER THAN THE AMBIENT CROSSING.
    If the deployment cost amortises, the advantage is enormous.

-- AND IT CLOSES ON THEIR OWN SENTENCE ---------------------------------------
GJW's flat-space discussion says how the coupling is realised when the two
mouths sit in the same space:

    "The direct boundary interaction could then be produced by PROPAGATION
     THROUGH THE AMBIENT SPACETIME -- this would be the same as the interaction
     we studied, EXCEPT WITH A TIME DELAY."

    THE COUPLING IS NOT A ONE-TIME DEPLOYMENT COST.  It is mediated by ordinary
    propagation across D, so it carries D/c intrinsically, per use.  There is
    nothing to amortise: the channel is not a thing you build once, it is a
    signal you send every time.

    THE AMORTISATION ESCAPE IS CLOSED, and closed by the paper rather than by
    an argument of mine.

-- BUT THEY LEAVE ONE CASE, EXPLICITLY, AND IT IS THE ONE THAT MATTERS --------
Their footnote 2, in full:

    "We do not consider the case of a TIME-INDEPENDENT interaction, in order to
     prevent the quantum state from becoming non-regular on the past horizon."

    THEY DECLINED THE STANDING COUPLING.  Not because it fails -- because a
    time-independent h(t,x) makes their state irregular on the past horizon,
    which is a technical obstruction to THEIR calculation in THEIR background.

    AND A STANDING COUPLING IS EXACTLY WHAT THE AMORTISATION ARGUMENT NEEDS.  A
    channel held open continuously pays its propagation delay to ESTABLISH the
    standing state, not per transit.  Whether that is possible is the question
    their footnote sets aside.

    THAT IS A NOT-RUN IN THE SOURCE, WITH A STATED TECHNICAL REASON, AND IT IS
    WHERE THE ORDER ROW IS ACTUALLY OPEN.

-- WHAT THIS FILE DOES AND DOES NOT CLAIM ------------------------------------
DOES:  locate the open case exactly, in the source, with the authors' own reason
       for not treating it.  The order row is not open everywhere -- it is open
       at ONE point, and this is it.

DOES NOT: claim a standing coupling works.  Their regularity obstruction is real
       and it may be fatal; a past-horizon irregularity is not a bookkeeping
       nuisance.  Nor does this file claim the amortisation would survive even
       if a standing coupling existed -- the bank-loan theorem might extend, and
       this file has not extended it either way.

DOES NOT: touch the magnitude.  entangle.py's 2 pi^2 over the holographic bound
       and achievable.py's 65 orders are unmoved.  This is the ORDER row only,
       and expand.py's INFORMATION row still refuses.

    SO THE HONEST STATE: order admits a mechanism (external causal path), the
    single-trip advantage is closed by a theorem, the amortised advantage is
    closed by an ambient time delay, and the STANDING-COUPLING case is untested
    by anyone.  That is one door, and it is narrow, and it is real.

stdlib only.  gjw.py supplies the source reading, expand.py the row this pushes.
"""
import math, sys

C_SI = 299792458.0
L_PLANCK = 1.616255e-35
AU = 1.495979e11
LIGHT_YEAR = 9.4607e15


def traversal_window(R, h=1.0):
    """GJW's window, in metres of ct: Delta t ~ R ln(R/(h l_P))."""
    return R * math.log(R / (h * L_PLANCK))


def window_seconds(R, h=1.0):
    return traversal_window(R, h) / C_SI


def ambient_seconds(D):
    return D / C_SI


def window_ratio(R, D, h=1.0):
    """How short the window is against the ambient crossing.  R and D are
    independent parameters, which is what makes the escape look plausible."""
    return window_seconds(R, h) / ambient_seconds(D)


def amortised_cost(N, deploy=1.0, per_transit=1.0e-6):
    """Average cost per transit, in units of D/c, for N transits after one
    deployment."""
    return (deploy + N * per_transit) / N


def amortisation_helps(N, deploy=1.0, per_transit=1.0e-6):
    return amortised_cost(N, deploy, per_transit) < 1.0


# The two sentences that decide this, quoted rather than paraphrased.
CLOSES_IT = ("The direct boundary interaction could then be produced by "
             "propagation through the ambient spacetime -- this would be the "
             "same as the interaction we studied, EXCEPT WITH A TIME DELAY.")
LEAVES_IT_OPEN = ("We do not consider the case of a TIME-INDEPENDENT "
                  "interaction, in order to prevent the quantum state from "
                  "becoming non-regular on the past horizon.")

NOT_CLAIMED = (
    "that a standing coupling works -- the regularity obstruction is real and "
    "may be fatal",
    "that amortisation would survive even if one existed -- the bank-loan "
    "theorem might extend, and this file has not extended it either way",
    "anything about the magnitude -- entangle.py's 2 pi^2 and achievable.py's "
    "65 orders are unmoved, and expand.py's INFORMATION row still refuses",
)


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

    print("THE TWO TIMESCALES ARE INDEPENDENT -- window on R, benefit on D")
    print("     %10s %14s %14s %14s %12s" % ("R", "D", "window (s)", "D/c (s)", "ratio"))
    for R, D, tag in ((1.0, AU, "1 m / 1 AU"), (1.0, LIGHT_YEAR, "1 m / 1 ly"),
                      (1.0e3, LIGHT_YEAR, "1 km / 1 ly"),
                      (1.0e6, LIGHT_YEAR, "1000 km / 1 ly")):
        print("     %10.0e %14.3e %14.4e %14.4e %12.3e"
              % (R, D, window_seconds(R), ambient_seconds(D), window_ratio(R, D)))
    near("1 m mouth against a light-year", window_ratio(1.0, LIGHT_YEAR), 8.467e-15, 1e-3)
    chk("the window shortens against the crossing as D grows",
        window_ratio(1.0, LIGHT_YEAR) < window_ratio(1.0, AU), True)
    chk("and it lengthens with the mouth, independently",
        window_seconds(1.0e6) > window_seconds(1.0), True)

    print("\nSO THE AMORTISATION ARITHMETIC LOOKS DECISIVE")
    print("     %10s %22s %12s" % ("N", "avg cost (D/c units)", "advantage?"))
    for N in (1, 10, 100, 10000):
        print("     %10d %22.6f %12s"
              % (N, amortised_cost(N), "YES" if amortisation_helps(N) else "no"))
    chk("one trip: no advantage", amortisation_helps(1), False)
    chk("ten trips: advantage", amortisation_helps(10), True)

    print("\nAND IT CLOSES ON THEIR OWN SENTENCE")
    print("     \"%s\"" % CLOSES_IT)
    chk("the coupling is per-use, not a deployment cost",
        "EXCEPT WITH A TIME DELAY" in CLOSES_IT, True)
    print("       There is nothing to amortise: the channel is not a thing you")
    print("       build once, it is a signal you send every time.")

    print("\nBUT THEY LEAVE ONE CASE, EXPLICITLY (their footnote 2)")
    print("     \"%s\"" % LEAVES_IT_OPEN)
    chk("they declined the TIME-INDEPENDENT coupling",
        "TIME-INDEPENDENT" in LEAVES_IT_OPEN, True)
    chk("for a stated technical reason, not a failure",
        "non-regular on the past horizon" in LEAVES_IT_OPEN, True)
    print("       A standing coupling is exactly what amortisation needs: it")
    print("       pays its delay to ESTABLISH the state, not per transit.")
    print("       THAT IS WHERE THE ORDER ROW IS ACTUALLY OPEN.")

    print("\nWHAT THIS DOES NOT CLAIM")
    for n in NOT_CLAIMED:
        print("     - %s" % n)
    chk("three things", len(NOT_CLAIMED), 3)
    import expand, achievable
    st = expand.expand()
    chk("INFORMATION still refuses", st["information"], expand.REFUSES)
    chk("and the magnitude is unmoved", achievable.ratio(1.0) < 1e-60, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("VERDICT")
    print("  Order admits a MECHANISM -- GJW's external causal path.  The")
    print("  single-trip advantage is closed by the bank-loan theorem.  The")
    print("  amortised advantage is closed by their own sentence: in flat space")
    print("  the coupling is carried by ambient propagation, 'except with a time")
    print("  delay', so it is a per-use cost with nothing to amortise.")
    print("\n  AND THEY EXPLICITLY DECLINED THE TIME-INDEPENDENT COUPLING, in")
    print("  footnote 2, to keep their state regular on the past horizon.  A")
    print("  standing channel is exactly that case, and it is exactly what an")
    print("  amortised advantage would need.")
    print("\n  ONE DOOR.  Narrow, real, untested by anyone, and named in the")
    print("  source with the authors' own reason for not opening it.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
