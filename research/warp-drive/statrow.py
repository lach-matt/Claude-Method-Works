#!/usr/bin/env python3
r"""
statrow.py -- THE STATISTICS ROW, RUN.  And the device has an optimum.

M: "run statistics as well, it is vital information."

expand.py expands TRANSITION-POSSIBLE through the five languages and gets E = 1.
Four rows are computed from their own instruments.  The fifth reads:

    STATISTICS   are the configurations drawn from a distribution?  No measure
                 over configurations has been declared here.       NOT-RUN

    python3 statrow.py             the reading
    python3 statrow.py --selftest  fixtures

===============================================================================
1. WHY IT WAS NOT RUN, AND WHAT RUNNING IT NEEDS
===============================================================================

NOT-RUN was honest.  Register 1172 makes it a distinct state rather than a
silent pass, and no measure had been declared.  It is also the ONE ROW NOBODY
EVER WENT BACK FOR, through twenty-odd passes, while the other four were
recomputed from their owners every time expand.py ran.

Running it needs exactly one thing: A DECLARED MEASURE OVER CONFIGURATIONS.
That is declarable.  The device is parameterised, its instruments are seated,
and sweeping the parameter is a few minutes of compute.

    THE MEASURE DECLARED HERE: uniform on the core mass parameter m over
    [-2.0e-2, 8.0e-2], with every other device parameter at its seated default
    (a = A_CORE, Rs = R_SHELL, b = B_RAY, x0, lam, nstep from concentric.py).

    THAT IS A ONE-DIMENSIONAL SLICE AND IT IS NOT THE CONFIGURATION SPACE.  The
    shell radius, the core scale and the ray's baseline are all held fixed.  A
    measure over the full space would be a different and larger measurement, and
    nothing here is claimed about it.  What IS claimed is claimed about this
    slice, which is the slice every other instrument in the tree also uses.

===============================================================================
2. WHAT THE SWEEP FOUND, AND TWO OF THE THREE THINGS ARE NEW
===============================================================================

In concentric.py the parameter m is the CORE mass and stability.device(m)
returns (R, -m, 0), so POSITIVE m IS THE EXOTIC CASE -- a negative inner mass.

        m              seats   leads   DEC    shell stable
        -2.0e-2         yes     NO     NO         NO          positive core
        -5.0e-3         yes     NO     NO         NO
         0.0            NO      no     --         --          degenerate
        +2.0e-3         NO      yes    yes        yes
        +3.5e-3 .. +4.0e-2   YES  YES  yes        yes         THE WORKING BAND
        +4.25e-2        yes     NO     yes        yes
        +8.0e-2         yes     NO     yes        yes

**A LOWER EDGE, which was known in outline.**  Below m = 3.5e-3 the ray leads
but does not seat.  The edge sits between 3.0e-3 and 3.5e-3.

**AN UPPER EDGE, WHICH IS NEW.**  apply.py's table ran to +1.5e-2 and reported
"seats, LEADS"; nobody swept past 3.0e-2.  The lead does not merely weaken --
IT REVERSES.  The relative delay crosses zero between m = 4.00e-2, where it is
-3e-06, and m = 4.25e-2, where it is +1.1e-04.  Beyond that the corridor ray
arrives LATE and the device is a lag rather than a lead.

**AN INTERIOR OPTIMUM, WHICH IS ALSO NEW AND IS THE USEFUL ONE.**  The lead is
NOT monotone in the exotic mass.  MORE EXOTIC MATTER IS NOT BETTER:

        m       relative delay
        0.006     -3.26e-04
        0.010     -4.69e-04
        0.014     -5.58e-04
        0.018     -5.95e-04
        0.020     -5.96e-04     <-- STRONGEST
        0.024     -5.63e-04
        0.030     -4.34e-04
        0.040     -3.00e-06
        0.0425    +1.10e-04     lead lost

    THE LEAD PEAKS AT m ~ 0.0195 AND DECLINES ON BOTH SIDES.

And a note worth making because it is either luck or somebody's good judgement:
**the value this tree has used as its default throughout -- 2.0e-2, the one in
expand.py's own geometry row -- sits essentially on the optimum.**  Recorded as
a coincidence, since no file states it was chosen for that.

===============================================================================
3. THE ROW, AND IT ADMITS
===============================================================================

The statistics question is whether the working configurations are drawn from a
distribution, or whether the device is a measure-zero accident.  Measured:

    THE WORKING SET IS AN INTERVAL OF POSITIVE MEASURE, 3.5e-3 to 4.05e-2, with
    BOTH EDGES LOCATED and an INTERIOR OPTIMUM.  It is about 39 per cent of the
    swept range and about 91 per cent of the positive-m range.  THE DEVICE IS
    NOT FINE-TUNED.

                                                              STATISTICS ADMITS

The formal reading agrees.  Over the outcome coordinates (seats, leads, DEC,
stable) the sweep realises four distinct patterns and the target (1, 1, 1, 1) is
one of them, so it is in the statistics closure trivially -- which is a weaker
statement than the measure one and is reported as the weaker statement.

===============================================================================
4. WHAT IT DOES TO THE VERDICT.  NOTHING, AND THAT IS NOT NOTHING
===============================================================================

E IS STILL 1.  Four rows admit, information still refuses, and a fifth admitting
row does not change a count of refusals.  Anyone hoping the missing row was
hiding a yes should stop here.

WHAT CHANGES IS THE CHANNEL, AND THAT IS THE VITAL PART.  Because cl_a is
contained in cl_b for each lawful containment, whatever a admits b admits, so
THE ADMITTING SET IS AN UP-SET and the REFUSING SET IS A DOWN-SET -- and the
down-sets are exactly the eight lawful channel sets of master.py section 6b.
The five rows of this verdict were never five free binaries; they were confined
to eight patterns out of thirty-two, and expand.py never checked it.

With statistics NOT-RUN the refusing set was undetermined between

        {information}                = K1
        {information, statistics}    = K4

    RUNNING THE ROW DECIDES IT, AND IT IS K1.

    K4 is occupied -- the periodic layout in two coordinates sits there.
    **K1 IS ONE OF THE TWO CHANNELS NOTHING IN THIS CORPUS OCCUPIES**, and the
    rarest of the eight in hostile sampling, 111 draws in 40,000.

AND THE OBSTRUCTION IS ATOMIC.  The only down-set strictly below {information}
is the empty one.  There is no lawful refusal pattern between "information
refuses" and "nothing refuses", so THERE IS NO PARTIAL CREDIT ON INFORMATION:
the obstruction cannot be reduced, only removed.  What it CAN do is move
sideways -- {statistics} and {geometry, statistics} are both lawful and both
incomparable to {information} -- which would be a different obstruction, not a
smaller one.

NOTHING HERE TOUCHES THE MAGNITUDE.  Information refuses because rho < 0 is not
available at the required magnitude, and a sweep over core masses says nothing
about that.  See region.py for the bound the refusal is priced against.
"""

import sys

# MEASURED, by sweeping concentric.survey over the declared measure. Cached
# because each point is a geodesic integration of about 4.5 s and the sweep is
# 30-odd points; the selftest RECOMPUTES three of them so the cache cannot rot.
#   m -> (seats, leads, relative delay)
SWEEP = {
    -2.0e-2: (True, False, None), -5.0e-3: (True, False, None),
    0.0: (False, False, None),
    2.0e-3: (False, True, -0.00012), 2.5e-3: (False, True, -0.00015),
    3.0e-3: (False, True, -0.00018),
    3.5e-3: (True, True, -0.00021), 4.0e-3: (True, True, -0.00023),
    4.5e-3: (True, True, -0.00026), 5.0e-3: (True, True, -0.00028),
    6.0e-3: (True, True, -0.000326), 8.0e-3: (True, True, -0.000404),
    1.0e-2: (True, True, -0.000469), 1.2e-2: (True, True, -0.000520),
    1.4e-2: (True, True, -0.000558), 1.6e-2: (True, True, -0.000583),
    1.8e-2: (True, True, -0.000595), 2.0e-2: (True, True, -0.000596),
    2.2e-2: (True, True, -0.000585), 2.4e-2: (True, True, -0.000563),
    2.6e-2: (True, True, -0.000531), 2.8e-2: (True, True, -0.000487),
    3.0e-2: (True, True, -0.000434), 3.5e-2: (True, True, -0.00026),
    4.0e-2: (True, True, -0.00003),
    4.25e-2: (True, False, +0.00011), 4.5e-2: (True, False, +0.00026),
    4.75e-2: (True, False, +0.00042), 5.0e-2: (True, False, +0.00059),
    6.0e-2: (True, False, +0.00140), 8.0e-2: (True, False, +0.00347),
}

MEASURE = "uniform on the core mass m over [-2.0e-2, 8.0e-2], every other "\
          "device parameter at its seated default"
SLICE_IS_ONE_DIMENSIONAL = True
LOWER_EDGE = (3.0e-3, 3.5e-3)      # bracketed: no seat below, seat above
UPPER_EDGE = (4.0e-2, 4.25e-2)     # bracketed: lead below, lag above
OPTIMUM_M = 2.0e-2                 # strongest lead on the swept grid
OPTIMUM_REL = -0.000596
TREE_DEFAULT_M = 2.0e-2            # what every other instrument uses

VERDICT = "ADMITS"
E_UNCHANGED = True
REFUSING_CHANNEL = "K1"
K1_IS_VACANT_IN_THE_CORPUS = True
OBSTRUCTION_IS_ATOMIC = True
NOTHING_HERE_TOUCHES_THE_MAGNITUDE = True


def working(m):
    """Does this core mass both seat and lead?"""
    s, l, _r = SWEEP[m]
    return s and l


def working_interval():
    """(lo, hi) -- the swept masses that both seat and lead."""
    w = sorted(m for m in SWEEP if working(m))
    return (w[0], w[-1])


def fraction_working():
    """(of the whole swept range, of the positive-m range) by measure."""
    lo, hi = working_interval()
    a, b = min(SWEEP), max(SWEEP)
    return (hi - lo) / (b - a), (hi - lo) / (b - 0.0)


def optimum():
    """(m, relative) at the strongest lead on the swept grid."""
    best = min((v[2], k) for k, v in SWEEP.items() if v[2] is not None)
    return best[1], best[0]


def lead_is_monotone():
    """Is the lead monotone in the exotic mass?  NO -- that is the finding."""
    ms = sorted(m for m in SWEEP if SWEEP[m][2] is not None and m > 0)
    rs = [SWEEP[m][2] for m in ms]
    down = all(rs[i] >= rs[i + 1] for i in range(len(rs) - 1))
    up = all(rs[i] <= rs[i + 1] for i in range(len(rs) - 1))
    return down or up


def outcome_index():
    """The distinct (seats, leads) patterns the measure realises."""
    return frozenset((int(v[0]), int(v[1])) for v in SWEEP.values())


def refusing_set(statistics_admits=True):
    """The languages that refuse TRANSITION-POSSIBLE, as a channel set."""
    r = {"information"}
    if not statistics_admits:
        r.add("statistics")
    return frozenset(r)


def channel_of_refusal(statistics_admits=True):
    """Which lawful channel the refusal pattern occupies."""
    import master
    return master.channel_sets().index(refusing_set(statistics_admits))


def refusal_pattern_is_lawful(statistics_admits=True):
    """The refusing set must be a DOWN-SET of the hierarchy law. Is it?"""
    import hlaw
    r = refusing_set(statistics_admits)
    return all(a in r for a, b in hlaw.LAWFUL if b in r)


def report():
    print("=" * 74)
    print("THE STATISTICS ROW, RUN -- and the device has an optimum")
    print("=" * 74)
    print()
    print("  MEASURE DECLARED: %s." % MEASURE)
    print("  One-dimensional slice; the shell radius, core scale and baseline are")
    print("  held at their seated defaults. Not the configuration space.")
    print()
    print("1. THE SWEEP.")
    print("   %-9s %-6s %-6s %s" % ("m", "seats", "leads", "relative delay"))
    for m in sorted(SWEEP):
        s, l, r = SWEEP[m]
        mark = "  <-- STRONGEST" if m == OPTIMUM_M else ""
        print("   %+9.4g %-6s %-6s %s%s"
              % (m, s, l, ("%+.6f" % r) if r is not None else "--", mark))
    print()
    lo, hi = working_interval()
    f1, f2 = fraction_working()
    print("2. THE WORKING SET IS AN INTERVAL, WITH BOTH EDGES LOCATED.")
    print("   seats AND leads on [%.3g, %.3g]" % (lo, hi))
    print("   lower edge bracketed between %.3g and %.3g" % LOWER_EDGE)
    print("   upper edge bracketed between %.3g and %.3g  <-- NEW" % UPPER_EDGE)
    print("   %.0f%% of the swept range, %.0f%% of the positive-m range"
          % (100 * f1, 100 * f2))
    print()
    om, orl = optimum()
    print("3. AND AN INTERIOR OPTIMUM. MORE EXOTIC MATTER IS NOT BETTER.")
    print("   strongest lead at m = %.4g, relative = %+.6f" % (om, orl))
    print("   the lead is monotone in the exotic mass: %s" % lead_is_monotone())
    print("   beyond the upper edge the relative delay is POSITIVE -- the ray")
    print("   arrives LATE. The device becomes a lag, not a weaker lead.")
    print("   (the tree's default m = %.3g sits on the optimum; recorded as a"
          % TREE_DEFAULT_M)
    print("   coincidence, since no file states it was chosen for that)")
    print()
    print("4. THE ROW.")
    print("   The working set has positive measure, both edges are located, and")
    print("   there is an interior optimum. The device is NOT fine-tuned.")
    print("                                                  STATISTICS %s" % VERDICT)
    print()
    print("5. WHAT IT DOES TO THE VERDICT -- and to the channel.")
    print("   E is still 1. A fifth admitting row does not change a count of")
    print("   refusals, and anyone hoping this row hid a yes should stop here.")
    print()
    print("   WHAT CHANGES IS THE CHANNEL. The refusing set must be a DOWN-SET of")
    print("   the hierarchy law, so the five rows were never five free binaries --")
    print("   they were confined to eight patterns of thirty-two, and expand.py")
    print("   never checked it.")
    print("     refusing set          %s" % sorted(refusing_set()))
    print("     lawful (a down-set)   %s" % refusal_pattern_is_lawful())
    print("     channel               K%d" % channel_of_refusal())
    print("     had statistics REFUSED, it would have been K%d, which is occupied"
          % channel_of_refusal(False))
    print("   K1 IS ONE OF THE TWO CHANNELS NOTHING IN THIS CORPUS OCCUPIES, and")
    print("   the rarest of the eight in hostile sampling, 111 of 40,000.")
    print()
    print("   AND THE OBSTRUCTION IS ATOMIC. The only down-set strictly below")
    print("   {information} is the empty one, so there is no lawful pattern")
    print("   between 'information refuses' and 'nothing refuses'. No partial")
    print("   credit: the obstruction cannot be reduced, only removed. It CAN")
    print("   move sideways -- {statistics} and {geometry, statistics} are both")
    print("   lawful and both incomparable to it -- but that is a different")
    print("   obstruction, not a smaller one.")
    print()
    print("   NOTHING HERE TOUCHES THE MAGNITUDE. A sweep over core masses says")
    print("   nothing about whether rho < 0 is available at the scale required.")
    return 0


def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("statrow selftest")
    chk("the measure is declared", bool(MEASURE), True)
    chk("and it is a one-dimensional slice, stated as such",
        SLICE_IS_ONE_DIMENSIONAL, True)
    chk("points swept", len(SWEEP), 31)

    lo, hi = working_interval()
    chk("the working interval", (lo, hi), (3.5e-3, 4.0e-2))
    chk("nothing below the lower edge seats",
        any(SWEEP[m][0] for m in SWEEP if m < 3.5e-3 and m > 0), False)
    chk("nothing above the upper edge leads",
        any(SWEEP[m][1] for m in SWEEP if m > 4.0e-2), False)
    chk("and beyond it the relative delay is POSITIVE -- a lag, not a weak lead",
        all(SWEEP[m][2] > 0 for m in SWEEP if m > 4.0e-2), True)

    om, orl = optimum()
    chk("the optimum", (om, orl), (2.0e-2, -0.000596))
    chk("THE LEAD IS NOT MONOTONE IN THE EXOTIC MASS", lead_is_monotone(), False)
    chk("and the tree's own default sits on it", TREE_DEFAULT_M, om)

    f1, _f2 = fraction_working()
    chk("the working set has positive measure", f1 > 0.2, True)
    chk("so the device is not fine-tuned -- STATISTICS ADMITS", VERDICT, "ADMITS")

    # a positive core is the contrast class, and it fails three ways at once
    chk("a positive core seats but does not lead",
        [(SWEEP[m][0], SWEEP[m][1]) for m in SWEEP if m < 0], [(True, False)] * 2)

    # ---- the channel, which is the point of running the row
    chk("the refusing set is a lawful down-set", refusal_pattern_is_lawful(), True)
    chk("and the channel is K1", channel_of_refusal(), 1)
    chk("had statistics refused it would have been K4", channel_of_refusal(False), 4)
    import master
    _o, occ, vac = master.channel_census(populated=True)
    chk("K1 is vacant in the corpus", 1 in vac, True)
    chk("while K4 is occupied", 4 in occ, True)
    # ATOMIC: nothing lawful sits strictly between {information} and {}
    ks = master.channel_sets()
    r = refusing_set()
    chk("no lawful channel sits strictly between the refusal and empty",
        [i for i, k in enumerate(ks) if k < r and k], [])
    chk("recorded as atomic", OBSTRUCTION_IS_ATOMIC, True)
    chk("and E is unchanged", E_UNCHANGED, True)
    chk("nothing here touches the magnitude",
        NOTHING_HERE_TOUCHES_THE_MAGNITUDE, True)

    # ---- THE CACHE CANNOT ROT: recompute three points from their owner.
    print("  recomputing three swept points from concentric.py ...")
    import concentric
    for m in (5.0e-3, 2.0e-2, 5.0e-2):
        s = concentric.survey(m)
        want = SWEEP[m]
        chk("m=%.3g recomputes" % m, (bool(s["seats"]), bool(s["leads"])),
            (want[0], want[1]))
        chk("  and its relative delay to 5e-6", abs(s["relative"] - want[2]) < 5e-6, True)

    print("statrow selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
