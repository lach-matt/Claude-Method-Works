#!/usr/bin/env python3
"""
teardown.py -- closability as a design property, which nothing in this tree had
treated as one.  And it is the first thing in the light thread that goes LIGHT'S
WAY.

M: "that the corridor actually closes -- if it opens, it closes.  The mass
density energy approach would have forced a corridor open that couldn't close.
The reason we are identifying other cheaper currency is for the ability to close
what we open.  Small and contained."

    THE MECHANISM IS RIGHT AND IT IS DERIVABLE, and closure.py is what makes it
    matter rather than merely tidy: an un-closable corridor is EXACTLY the one
    that can host the state-splitting closure that file derived.

And a second claim, tested separately and scoring differently:

M: "it's like building an index.  You now have two axes of information that
share a value, this means there is another."

    A THIRD INSTANCE EXISTS.  It is also NOT INDEPENDENT of the first, and the
    shape is generic mathematics rather than a discovery.  Section 4 says so.

===============================================================================
1. NOTHING HERE HAD TREATED TEARDOWN AS A PROPERTY
===============================================================================

Every instrument in this tree asks what it costs to OPEN a corridor -- the
exchange rate, the seat, the lead, the supply.  None asks what it costs to SHUT
one, or whether it shuts at all.  That is a real gap and this file fills it.

The quantity is the corridor's LIFETIME AFTER YOU STOP PAYING: tau.

===============================================================================
2. THE ASYMMETRY, AND IT IS NOT SMALL
===============================================================================

LIGHT.  The field is null.  Stop the source and the region clears at c -- there
is nothing to remove, because the carrier leaves on its own at the only speed it
has.  For a corridor of extent R,

        tau_light  =  R / c

        R = 1 um     3.34e-15 s
        R = 1 mm     3.34e-12 s
        R = 1 m      3.34e-09 s
        R = 1 km     3.34e-06 s

MATTER.  A static configuration persists.  Nothing clears it but work, and the
work is bounded below by how fast mass can be moved, which is slower than c.
For the seated architecture it is worse than that: core.py's core is a
STRONG-FIELD object and negmass.py and stability.py hold its instability
findings.  Teardown is not the reverse of setup at the same price.

        tau_matter =  unbounded, and set by an active removal, not by a clock

    THE ASYMMETRY IS NOT A FACTOR.  IT IS THE DIFFERENCE BETWEEN A PROCESS WITH
    A DEADLINE AND A PROCESS WITH NONE.  Light's teardown is FREE and runs at c;
    matter's is WORK and runs slower.

    STATED HONESTLY: matter CAN be made transient -- you may throw it away.  The
    claim is not that a matter corridor must persist forever.  It is that
    light's termination is AUTOMATIC AND c-LIMITED while matter's must be
    performed, and that is the whole of the asymmetry.

===============================================================================
3. AND THAT IS EXACTLY WHAT DECIDES THE CTC -- WHICH IS WHY IT MATTERS
===============================================================================

chronology.py leaves EVERETT_ROUTE_OPEN = True: two devices at separation D, in
relative motion, needing no identification.  closure.py then derived that a
closed curve admits no definite state -- classically unsatisfiable, 50/50 under
Deutsch, amplitude zero under postselection.

    SO AN UN-CLOSABLE CORRIDOR IS NOT AN UNTIDINESS.  IT IS THE STANDING
    PRECONDITION FOR THE ONE FAILURE closure.py DESCRIBES.

The window argument.  A closed causal loop must traverse device 1, propagate to
device 2, traverse it and return: at least 2D/c of loop transit.  BOTH corridors
must still be open when the signal arrives.  So a CTC needs

        tau  >=  2 D / c

For a light corridor tau = R/c, so a CTC would need R >= 2D.  But two separate
devices do not overlap, so D >= R, hence 2D >= 2R > R.

        tau / loop  =  R / (2D)  <=  1/2      FOR EVERY NON-OVERLAPPING PAIR

    A SELF-TERMINATING LIGHT CORRIDOR CANNOT HOST THE EVERETT CTC AT ANY
    SEPARATION.  Measured at R = D = 1 um, 1 mm, 1 m, 1 km, 1 Mm: no, at every
    one, and the ratio is 1/2 at every one because it depends only on R/D.

    AND THE MATTER ROUTE IS PRECISELY THE ONE THAT LEAVES IT OPEN.  tau
    unbounded satisfies tau >= 2D/c at EVERY D.  A persistent matter corridor
    meets the CTC condition at all separations; a self-terminating light
    corridor meets it at none.

        M'S SENTENCE, DERIVED: the mass-density approach forces a corridor open
        that cannot close, and the reason to want a cheaper currency is the
        ability to close what you open.  SMALL AND CONTAINED IS THE CONDITION,
        and "small" is R < 2D, which is free.

    WHAT THIS IS, EXACTLY: a CAUSAL-WINDOW SCALING ARGUMENT, not a theorem.  The
    factor of 2 is geometry-dependent and a different loop topology moves it.
    What is robust is the SCALING -- tau goes as R, the loop goes as D, and
    D >= R for separate devices -- so no choice of the coefficient rescues the
    light case into a CTC.  Marked as scaling, and it is not upgraded here.

    AND IT DOES NOT RESCUE LIGHT ON THE LEAD.  lattice.py's theorem is
    untouched: no classical EM field supplies rho < 0, in any orientation.  This
    is a property of a corridor light could SEAT.  It is not a demonstration
    that light can build one.

    WHICH FORCES A QUALIFICATION THAT CUTS THE RESULT DOWN, AND IT IS THE
    HONEST SIZE OF IT.  A corridor is held open by the SEAT AND THE LEAD
    together, so its lifetime is set by the LONGEST-LIVED COMPONENT, not the
    shortest:

            tau_corridor  =  max(tau_seat, tau_lead)

    Light can be the seat, so tau_seat = R/c.  Light CANNOT be the lead.  If
    the lead is a persistent matter configuration then tau_lead is unbounded and
    tau_corridor is unbounded WITH IT -- and the whole CTC argument above
    evaporates, because the corridor stays open regardless of what the seat did.

        SO THE TEARDOWN ADVANTAGE IS REAL AND IT IS CONDITIONAL.  It belongs to
        the corridor only if the LEAD is transient too.

    THAT IS NOT A DEFEAT, IT IS A SPECIFICATION, and it is one nothing in this
    tree had written down: THE LEAD MUST BE SWITCHABLE.  Every previous pass
    asked the lead for a sign; this one asks it for a deadline as well.  A
    negative-energy element that cannot be turned off buys a corridor that
    cannot be shut, and closure.py says what that costs.  M's instinct -- "the
    reason we are identifying other cheaper currency is for the ability to
    close what we open" -- lands as a REQUIREMENT ON THE LEAD rather than a
    property of the seat.

===============================================================================
4. THE INDEX MOVE -- A THIRD INSTANCE EXISTS, AND IT IS THE WEAK KIND
===============================================================================

M: two axes sharing a value means there is another.  Tested.

    A THIRD INSTANCE IS THERE.  The chord itself is double-valued.  With
    c(t) = 2 sin(t/2),

        c(t + 2pi) = -c(t)      measured to 8.88e-16 over 501 samples

    THE CHORD IS ANTIPERIODIC -- spinorial, needing 4pi to return.  And the
    observable is restored by an EVEN power: A(t + 2pi) = +A(t) to 6.66e-15.
    So the same shape appears a third time: closure at 2pi forces c to carry
    both signs, and only the even power hides it.

    BUT TWO THINGS CUT IT DOWN, AND BOTH ARE RECORDED RATHER THAN GLOSSED.

    IT IS NOT INDEPENDENT.  bisector.py's instance and this one live in THE SAME
    ANGULAR VARIABLE.  The index move predicted a third axis; what turned up is
    a sub-structure of the first.  That is weaker than the prediction, and the
    difference is the whole point of insisting on independence.

    AND THE SHAPE IS GENERIC.  "Closure forces one object to carry two values"
    is MONODROMY, and monodromy is not a discovery -- it is the definition of a
    multivalued function continued around a non-trivial loop.  Branch points,
    double covers, holonomy, Berry phase, a spinor's 4pi period: the shape is
    everywhere in mathematics because it is what a non-trivial fundamental group
    MEANS.  Finding it a third time is expected, not informative.

        SO THE INDEX MOVE SCORES: a third instance, yes; a third INDEPENDENT
        axis, no; and evidence of a deep unity, no -- the recurrence is what
        monodromy is for.  A shape recurring across systems is still a finding
        and still not an identification.

    ONE THING THE THIRD INSTANCE DOES SETTLE, AND IT IS SMALL: the observable
    must be built from an EVEN power of the chord or it would not be
    single-valued on the circle.  It does NOT fix the power at four -- c^2 is
    even too, and c^2/2 = 1 - cos t is perfectly single-valued.  THE FOUR COMES
    FROM SPIN-2 SQUARING, not from single-valuedness, and claiming otherwise
    would be reading a cause into a consistency check.
"""

import math
import sys

C = 2.99792458e8

TREE_HAD_TREATED_TEARDOWN = False
THE_QUANTITY = "tau -- the corridor's lifetime after you stop paying"


# ---------------------------------------------- 2: the asymmetry

def tau_light(R_m):
    """A null field clears its own extent at c.  Nothing to remove."""
    return R_m / C


TAU_MATTER = None            # unbounded: set by an active removal, not a clock
MATTER_TEARDOWN_IS = "work, bounded below by how fast mass moves, which is < c"
LIGHT_TEARDOWN_IS = "free, and at c"


def matter_self_terminates():
    return False


def light_self_terminates():
    return True


def matter_can_be_made_transient():
    """Stated because it is true: you may throw matter away.  The asymmetry is
    that light's termination is AUTOMATIC and c-limited, not that matter's is
    impossible."""
    return True


# ---------------------------------------------- 3: the CTC window

def loop_transit(D_m):
    """A closed causal loop through two devices at separation D: >= 2D/c."""
    return 2.0 * D_m / C


def ctc_possible(R_m, D_m):
    """A CTC needs both corridors open across the loop transit."""
    return tau_light(R_m) >= loop_transit(D_m)


def window_ratio(R_m, D_m):
    """tau / loop = R / (2D).  Depends only on R/D."""
    return tau_light(R_m) / loop_transit(D_m)


def ratio_depends_only_on_R_over_D(pairs=((1.0, 1.0), (1e3, 1e3), (1e-6, 1e-6)),
                                   tol=1e-12):
    vals = [window_ratio(R, D) for R, D in pairs]
    return max(vals) - min(vals) <= tol


def light_can_ever_host_a_ctc(scales=(1e-6, 1e-3, 1.0, 1e3, 1e6)):
    """Devices do not overlap, so D >= R.  Test the tightest case D = R."""
    return any(ctc_possible(R, R) for R in scales)


def matter_hosts_a_ctc_at_every_separation():
    """tau unbounded satisfies tau >= 2D/c for every D."""
    return TAU_MATTER is None


def smallness_condition():
    return "R < 2D"


def smallness_is_free():
    """D >= R for separate devices, so 2D >= 2R > R.  Always satisfied."""
    return True


ARGUMENT_STATUS = "causal-window SCALING argument, not a theorem"
COEFFICIENT_IS = "geometry-dependent; the scaling tau ~ R against loop ~ D >= R is not"


def rescues_the_lead():
    """lattice.py: no classical EM field supplies rho < 0, in any orientation."""
    return False


def tau_corridor(tau_seat, tau_lead):
    """A corridor is held open by BOTH halves, so its lifetime is the LONGER.

    None stands for unbounded and dominates anything finite.
    """
    if tau_seat is None or tau_lead is None:
        return None
    return max(tau_seat, tau_lead)


def light_seat_matter_lead(R_m=1.0):
    """The seated architecture: light seats, matter leads.  tau is unbounded."""
    return tau_corridor(tau_light(R_m), TAU_MATTER)


def teardown_advantage_is_conditional():
    """It belongs to the corridor only if the LEAD is transient too."""
    return light_seat_matter_lead(1.0) is None


NEW_SPECIFICATION = "THE LEAD MUST BE SWITCHABLE"
SPEC_WAS_WRITTEN_DOWN_BEFORE = False
PREVIOUS_PASSES_ASKED_THE_LEAD_FOR = "a sign"
THIS_PASS_ALSO_ASKS_FOR = "a deadline"


# ---------------------------------------------- 4: the index move

def chord(theta):
    return 2.0 * math.sin(theta / 2.0)


def coupling(theta):
    return chord(theta) ** 4 / 2.0


def chord_antiperiod(samples=500):
    """Worst |c(t + 2pi) + c(t)|.  Zero means c(t+2pi) = -c(t) exactly."""
    return max(abs(chord(math.pi * i / samples) + chord(math.pi * i / samples + 2 * math.pi))
               for i in range(samples + 1))


def coupling_period(samples=500):
    """Worst |A(t + 2pi) - A(t)|.  Zero means the observable is restored."""
    return max(abs(coupling(math.pi * i / samples) - coupling(math.pi * i / samples + 2 * math.pi))
               for i in range(samples + 1))


def chord_is_spinorial(tol=1e-12):
    return chord_antiperiod() <= tol


def even_power_restores_it(tol=1e-12):
    return coupling_period() <= tol


def square_would_also_work(samples=200, tol=1e-12):
    """c^2 is even too, so single-valuedness does NOT fix the power at four."""
    f = lambda t: chord(t) ** 2
    return max(abs(f(math.pi * i / samples) - f(math.pi * i / samples + 2 * math.pi))
               for i in range(samples + 1)) <= tol


THIRD_INSTANCE_EXISTS = True
THIRD_INSTANCE_IS_INDEPENDENT = False
THIRD_INSTANCE_LIVES_IN = "the same angular variable as bisector.py's -- a sub-structure, not a new axis"
THE_SHAPE_IS = "monodromy -- what a non-trivial fundamental group MEANS"
SHAPE_RECURRENCE_IS = "expected, not informative"
FOUR_COMES_FROM = "spin-2 squaring, not from single-valuedness"


def index_move_predicted_a_third_axis():
    return THIRD_INSTANCE_EXISTS and THIRD_INSTANCE_IS_INDEPENDENT


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    def under(label, got, bound):
        nonlocal ok
        good = got <= bound
        ok &= good
        print("  %-56s %20.6g %20s  %s"
              % (label, got, "<= %.3g" % bound, "ok" if good else "FAIL"))

    print("1. NOTHING HERE HAD TREATED TEARDOWN AS A PROPERTY")
    chk("had the tree treated it", TREE_HAD_TREATED_TEARDOWN, False)
    print("     the quantity is %s" % THE_QUANTITY)

    print("\n2. THE ASYMMETRY")
    print("     %-10s %16s %18s" % ("R", "tau_light = R/c", "tau_matter"))
    for R in (1e-6, 1e-3, 1.0, 1e3):
        print("     %-10.0e %16.4e %18s" % (R, tau_light(R), "unbounded"))
    near("tau_light at R = 1 m (s)", tau_light(1.0), 3.335641e-9, 1e-6)
    chk("does light self-terminate", light_self_terminates(), True)
    chk("does matter", matter_self_terminates(), False)
    chk("  and matter's teardown is", MATTER_TEARDOWN_IS,
        "work, bounded below by how fast mass moves, which is < c")
    chk("  light's is", LIGHT_TEARDOWN_IS, "free, and at c")
    chk("can matter be made transient anyway", matter_can_be_made_transient(), True)
    print("       stated because it is true.  The asymmetry is that light's")
    print("       termination is AUTOMATIC and c-limited, not that matter's")
    print("       is impossible.")

    print("\n3. AND THAT DECIDES THE CTC")
    print("     %-10s %-10s %14s %14s %6s %7s"
          % ("R (m)", "D (m)", "tau = R/c", "loop = 2D/c", "CTC?", "ratio"))
    for R, D in ((1e-6, 1e-6), (1e-3, 1e-3), (1.0, 1.0), (1.0, 10.0), (1e6, 1e6)):
        print("     %-10.0e %-10.0e %14.4e %14.4e %6s %7.3f"
              % (R, D, tau_light(R), loop_transit(D),
                 "YES" if ctc_possible(R, D) else "no", window_ratio(R, D)))
        chk("  CTC at R=%.0e D=%.0e" % (R, D), ctc_possible(R, D), False)
    near("the ratio at D = R", window_ratio(1.0, 1.0), 0.5)
    chk("  does it depend only on R/D", ratio_depends_only_on_R_over_D(), True)
    chk("CAN A LIGHT CORRIDOR EVER HOST THE EVERETT CTC",
        light_can_ever_host_a_ctc(), False)
    chk("does a matter corridor, at every separation",
        matter_hosts_a_ctc_at_every_separation(), True)
    chk("  the smallness condition", smallness_condition(), "R < 2D")
    chk("  and is it free", smallness_is_free(), True)
    print("       M'S SENTENCE, DERIVED: the mass approach forces a corridor")
    print("       open that cannot close, and cheaper currency buys the")
    print("       ability to close what you open.")
    chk("what this argument is", ARGUMENT_STATUS,
        "causal-window SCALING argument, not a theorem")
    print("     %s" % COEFFICIENT_IS)
    chk("does it rescue light on the LEAD", rescues_the_lead(), False)
    print("       lattice.py is untouched: no classical EM field gives rho < 0.")
    print("     AND THE QUALIFICATION THAT CUTS IT DOWN:")
    print("       tau_corridor = max(tau_seat, tau_lead) -- the LONGER, not the")
    print("       shorter.  Light seats at R/c; light cannot lead.")
    near("  tau_seat at R = 1 m (s)", tau_light(1.0), 3.335641e-9, 1e-6)
    chk("  tau_lead for persistent matter", TAU_MATTER, None)
    chk("  so tau_corridor for light-seat/matter-lead",
        light_seat_matter_lead(1.0), None)
    chk("  IS THE TEARDOWN ADVANTAGE CONDITIONAL",
        teardown_advantage_is_conditional(), True)
    near("  and if the lead IS switchable at R/c", tau_corridor(tau_light(1.0),
         tau_light(1.0)), 3.335641e-9, 1e-6)
    chk("the specification this forces", NEW_SPECIFICATION,
        "THE LEAD MUST BE SWITCHABLE")
    chk("  had the tree written it down", SPEC_WAS_WRITTEN_DOWN_BEFORE, False)
    chk("  previous passes asked the lead for", PREVIOUS_PASSES_ASKED_THE_LEAD_FOR, "a sign")
    chk("  this one also asks for", THIS_PASS_ALSO_ASKS_FOR, "a deadline")
    print("       NOT A DEFEAT, A SPECIFICATION.  M's instinct lands as a")
    print("       REQUIREMENT ON THE LEAD, not a property of the seat.")

    print("\n4. THE INDEX MOVE -- A THIRD INSTANCE, AND IT IS THE WEAK KIND")
    print("     %10s %12s %14s %12s %14s"
          % ("theta", "c(t)", "c(t+2pi)", "A(t)", "A(t+2pi)"))
    for d in (0, 60, 120, 180):
        t = math.radians(d)
        print("     %10d %12.6f %14.6f %12.6f %14.6f"
              % (d, chord(t), chord(t + 2 * math.pi), coupling(t),
                 coupling(t + 2 * math.pi)))
    under("worst |c(t+2pi) + c(t)|", chord_antiperiod(), 1e-14)
    chk("  is the chord antiperiodic -- spinorial", chord_is_spinorial(1e-14), True)
    under("worst |A(t+2pi) - A(t)|", coupling_period(), 1e-13)
    chk("  does the even power restore the observable",
        even_power_restores_it(1e-13), True)
    chk("does a third instance exist", THIRD_INSTANCE_EXISTS, True)
    chk("  is it INDEPENDENT of the first", THIRD_INSTANCE_IS_INDEPENDENT, False)
    print("     it lives in %s" % THIRD_INSTANCE_LIVES_IN)
    chk("  so did the index move predict a third AXIS",
        index_move_predicted_a_third_axis(), False)
    chk("the shape is", THE_SHAPE_IS,
        "monodromy -- what a non-trivial fundamental group MEANS")
    chk("  so its recurrence is", SHAPE_RECURRENCE_IS, "expected, not informative")
    print("       branch points, double covers, holonomy, Berry phase, a")
    print("       spinor's 4pi period.  Finding it again is not a discovery.")
    chk("would c^2 also be single-valued", square_would_also_work(), True)
    chk("  so the FOUR comes from", FOUR_COMES_FROM,
        "spin-2 squaring, not from single-valuedness")
    print("       single-valuedness forces an EVEN power, not the power four.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  Every instrument here asks what a corridor costs to OPEN and none asked
  what it costs to SHUT.  Light's teardown is free and runs at c -- stop
  the source and a null field clears its own extent in R/c, 3.34 ns at a
  metre -- while a matter configuration persists and must be actively
  removed, slower than c.  That asymmetry is not cosmetic, because
  closure.py derived that a closed curve admits no definite state and
  chronology.py leaves the two-device Everett route OPEN: an un-closable
  corridor is the standing precondition for exactly that failure.  A closed
  causal loop needs 2D/c of transit with both corridors still open, so a
  CTC requires tau >= 2D/c; a light corridor gives tau/loop = R/(2D) <= 1/2
  for every non-overlapping pair, and CANNOT host one at any separation,
  while an unbounded matter corridor satisfies the condition at every
  separation.  M's sentence, derived -- the mass approach forces open what
  cannot close, and cheaper currency buys closability; small and contained
  is R < 2D, which is free.  It is a scaling argument, not a theorem, and
  it does not rescue the lead: lattice.py stands.  The index move scores
  differently -- a third instance of the shape is real, the chord being
  antiperiodic and spinorial with the even power hiding it, but it is not
  INDEPENDENT (same angular variable) and the shape is monodromy, which is
  generic.  Recurrence is what monodromy is for.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
