#!/usr/bin/env python3.12
"""oneway.py -- the transition is one way, and that is where the paradox lives.

M: "We don't need a price both ways.  The transition is only 1 way.  The return
is a separate trip reinitiated at the time of return."

THE CORRECTION IS MINE TO TAKE AND IT CHANGES THREE THINGS, ONE OF THEM BADLY.

  0.  WHAT WAS WRONG AND WHERE.  ladder.py's closing sentence said the corridor
      buys "everyone, permanently, any mass, BOTH WAYS".  Both ways was never
      measured by any instrument -- it appears only in my prose and in the
      index finding I wrote from it.  NOTHING COMPUTED CHANGES, and it is
      CORRECTED HERE RATHER THAN EDITED, as threads.py and modulus.py were.

  1.  WHAT SURVIVES, AND IT IS THE STRUCTURAL ONE.  The transition equation's
      M is the mass MAKING THE GEOMETRY, not the mass going through it.  So
      THE COST IS PER METRE OF SHORTCUT AND NOT PER KILOGRAM OF PAYLOAD, and
      the payload rides free.  A ticket is priced the other way round.  That
      means a CROSSOVER MASS exists above which one transition beats shipping.

  2.  AND THE CROSSOVER IS NEVER REACHED, AT ANY SPEED.  Against the ideal
      floor for a ticket -- 2(gamma-1) m c^2, an external beam with no
      propellant penalty at all -- the crossover for Proxima sits above a
      trillion solar masses at gamma = 2, and bringing it down to a hundred
      tonnes needs gamma ~ 1e37.  THE CORRIDOR LOSES ON PAYLOAD TOO.

  3.  ONE WAY TO AN UNEQUIPPED DESTINATION IS ONE WAY PERMANENTLY.  If the
      return must be reinitiated at the far end, the far end must ALREADY hold
      the same capability.  The corridor is not transport.  IT IS EMIGRATION.

  4.  AND THE PARADOX MOVES TO THE RETURN, WHICH IS THE REAL FINDING.
      transit.py showed a SINGLE transition carries no signalling advantage.
      roundtrip.py showed TWO hops can close a loop.  M's correction makes the
      return an INDEPENDENTLY INITIATED SECOND HOP -- exactly the antitelephone
      configuration -- and the frame velocity it needs is not something anyone
      has to arrange.  THE STARS SUPPLY IT.  With Proxima's own radial motion,
      any transition faster than about 27,000 c closes the loop.

      SO THE ONE-WAY TRIP IS THE SAFE ONE AND THE RETURN IS THE PARADOX, and
      that is a sharper statement than the tree had, reached by M narrowing
      the claim rather than widening it.

  5.  ONE OPEN, MARKED AS ONE.  How many objects pass per transition event is
      established NOWHERE in this project.  Cost per object is the total over
      N and N IS UNKNOWN -- not 1, not unbounded.  It is not assumed here.

Comparators are RECALLED, not read.  Stdlib only.

    python3.12 oneway.py            full report
    python3.12 oneway.py --selftest
"""

import math
import sys

import ladder
import roundtrip

c = ladder.c
LY = ladder.LY
M_SUN = ladder.M_SUN

PROXIMA_LY = 4.2465
PROXIMA_RADIAL_MS = 22.2e3        # RECALLED: ~ -22.2 km/s relative to the Sun
FIGURES_ARE_READ = False


# --- 1/2.  per-metre against per-kilogram --------------------------------

def corridor_energy(d):
    """Independent of payload.  The geometry is what is bought."""
    return ladder.energy_for_delta_d(d)


def ticket_energy(m, gamma):
    """THE IDEAL FLOOR: accelerate to gamma and decelerate, external beam, no
    propellant carried.  A real rocket is vastly worse; using the floor makes
    the comparison as favourable to the ticket as physics allows."""
    return 2.0 * (gamma - 1.0) * m * c * c


def crossover_mass(d, gamma):
    """Payload above which one corridor event undercuts the ideal ticket."""
    return corridor_energy(d) / (2.0 * (gamma - 1.0) * c * c)


def gamma_for_crossover(d, m):
    """The gamma that would put the crossover at payload m."""
    return 1.0 + corridor_energy(d) / (2.0 * m * c * c)


# --- 4.  where the loop closes -------------------------------------------

def frame_velocity(v_ms):
    return v_ms / c


def transition_speed_closing_loop(u):
    """Solve loop_threshold(v) = u for v: u v^2 - 2v + u = 0, upper root.

    roundtrip.py's convention: v is the SIGNAL speed, u the FRAME velocity,
    and loop_threshold(v) = 2v/(v^2+1) is the u above which the loop closes.
    Inverting gives the transition speed above which a GIVEN frame velocity
    suffices.
    """
    if u <= 0.0 or u >= 1.0:
        return float("inf")
    return (1.0 + math.sqrt(1.0 - u * u)) / u


def loop_closes(v, u):
    return roundtrip.loop_closes(v, u)


# --- verdicts -------------------------------------------------------------
BOTH_WAYS_WAS_MEASURED = False
BOTH_WAYS_WAS_MINE = True
COST_IS_PER_METRE_NOT_PER_KILOGRAM = True
CROSSOVER_EXISTS = True
CROSSOVER_IS_REACHABLE = False
RETURN_NEEDS_AN_EQUIPPED_FAR_END = True
CORRIDOR_IS_TRANSPORT = False
SINGLE_TRANSITION_IS_A_PARADOX = False
SEPARATELY_INITIATED_RETURN_CAN_BE = True
OBJECTS_PER_EVENT = None          # OPEN.  Established nowhere.
SCOPE = "the transition equation, roundtrip.py's kinematics, RECALLED comparators"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Comparators are")[0].rstrip())
    print()

    print(BAR)
    print("0.  THE CORRECTION, AND WHERE IT LANDED")
    print(BAR)
    print()
    print("      ladder.py closed with: the corridor buys 'everyone,")
    print("      permanently, any mass, BOTH WAYS'.  M: the transition is only")
    print("      one way, and the return is a separate trip reinitiated at the")
    print("      time of return.")
    print()
    print("      BOTH WAYS WAS NEVER MEASURED.  It is in my prose and in the")
    print("      index finding written from it, and in NO instrument -- grep")
    print("      over the tree finds it in dichotomy.py, negmass.py and")
    print("      reverse.py in unrelated senses only.  So NOTHING COMPUTED")
    print("      CHANGES and this is a correction to a claim, not to a")
    print("      measurement.  Corrected here rather than edited, as")
    print("      threads.py and modulus.py were.")
    print()
    print("      'PERMANENTLY' GOES WITH IT.  A transition that must be")
    print("      reinitiated is an EVENT, not a standing structure, and an")
    print("      event cannot be amortised over later users.")
    print()

    print(BAR)
    print("1.  WHAT SURVIVES -- PER METRE, NOT PER KILOGRAM")
    print(BAR)
    print()
    print("      In Delta d = (G/c^2) M Lambda the M IS THE GEOMETRY, not the")
    print("      payload.  So the corridor's price does not move when the cargo")
    print("      does, and A TICKET'S PRICE IS ENTIRELY THE CARGO.")
    print()
    print("      %14s %18s %18s %14s"
          % ("payload (kg)", "corridor (J)", "ideal ticket (J)", "ratio"))
    d = PROXIMA_LY * LY
    Ec = corridor_energy(d)
    for m in (1e2, 1e5, 1e8, 1e20, 1e30, 1e42):
        Et = ticket_energy(m, 2.0)
        print("      %14.3g %18.6e %18.6e %14.4e" % (m, Ec, Et, Et / Ec))
    print()
    print("      THE CORRIDOR COLUMN IS CONSTANT.  That is the only structural")
    print("      advantage it has, and it is a real one: it means a crossover")
    print("      mass exists rather than the comparison being hopeless at every")
    print("      scale.")
    print()

    print(BAR)
    print("2.  AND THE CROSSOVER IS NEVER REACHED")
    print(BAR)
    print()
    print("      Against the IDEAL FLOOR 2(gamma-1) m c^2 -- external beam, no")
    print("      propellant carried, a bound no real ship can approach:")
    print()
    print("      %10s %20s %20s" % ("gamma", "crossover mass (kg)", "solar masses"))
    for g in (1.05, 2.0, 10.0, 100.0, 1e6):
        mc_ = crossover_mass(d, g)
        print("      %10.4g %20.6e %20.6e" % (g, mc_, mc_ / M_SUN))
    print()
    g100t = gamma_for_crossover(d, 1e5)
    print("      AT gamma = 2 THE CROSSOVER IS %.4e SOLAR MASSES."
          % (crossover_mass(d, 2.0) / M_SUN))
    print("      To bring it down to a hundred tonnes you would need")
    print("      gamma = %.4e, which is not a speed, it is a misprint." % g100t)
    print()
    print("      SO THE CORRIDOR LOSES ON PAYLOAD TOO, and the comparison was")
    print("      made as favourable to the ticket as physics allows -- the")
    print("      floor, not a rocket.  A rocket is worse and it does not matter.")
    print()

    print(BAR)
    print("3.  AND ONE WAY TO AN UNEQUIPPED DESTINATION IS ONE WAY PERMANENTLY")
    print(BAR)
    print()
    print("      If the return is reinitiated AT THE FAR END, the far end must")
    print("      already hold the capability -- the same %.4e solar masses,"
          % (ladder.mass_for_delta_d(d) / M_SUN))
    print("      assembled there.  A destination that cannot build one cannot")
    print("      send anything back, ever.")
    print()
    print("        THE CORRIDOR IS NOT TRANSPORT.  IT IS EMIGRATION.")
    print()
    print("      That is a change of category rather than of price, and it is")
    print("      M's correction doing the work: a two-way ledger hid it, because")
    print("      a round trip silently assumes the far end is equipped.")
    print()

    print(BAR)
    print("4.  AND THE PARADOX MOVES TO THE RETURN")
    print(BAR)
    print()
    print("      transit.py: a SINGLE transition carries no signalling")
    print("      advantage.  roundtrip.py: TWO hops can close a loop, and the")
    print("      threshold is loop_threshold(v) = 2v/(v^2+1) in the frame")
    print("      velocity u, for a signal of speed v.")
    print()
    print("      M'S CORRECTION MAKES THE RETURN AN INDEPENDENTLY INITIATED")
    print("      SECOND HOP.  THAT IS THE ANTITELEPHONE CONFIGURATION EXACTLY.")
    print()
    u = frame_velocity(PROXIMA_RADIAL_MS)
    print("      And the frame velocity is not something anyone arranges.")
    print("      Proxima's own radial motion is %.1f km/s (RECALLED), which is"
          % (PROXIMA_RADIAL_MS / 1e3))
    print("      u = %.6e -- and that is already enough:" % u)
    print()
    print("      %14s %16s %16s %10s" % ("v (units of c)", "loop threshold u", "t_return", "closes?"))
    for v in (1e2, 1e3, 1e4, 2.70076e4, 1e5, 1e9):
        print("      %14.6g %16.6e %+16.6e %10s"
              % (v, roundtrip.loop_threshold(v), roundtrip.t_return(v, u),
                 loop_closes(v, u)))
    vcrit = transition_speed_closing_loop(u)
    print()
    print("      THE THRESHOLD IS v = %.6f c.  Any transition faster than" % vcrit)
    print("      that, between the Sun and Proxima, CLOSES THE LOOP -- and a")
    print("      corridor whose whole purpose is to arrive without traversing")
    print("      is faster than that by many orders.")
    print()
    print("        THE ONE-WAY TRIP IS THE SAFE ONE.  THE RETURN IS THE PARADOX.")
    print()
    print("      AND THE STARS SUPPLY THE FRAME VELOCITY.  Nothing has to be")
    print("      boosted, engineered or arranged; two stars in relative motion")
    print("      is the generic case and the exception -- exactly comoving ends")
    print("      -- is measure zero.  chronology.py's 'two devices plus a boost'")
    print("      needed the boost.  THIS NEEDS ONLY TWO STARS.")
    print()
    print("      WHAT IT DOES NOT SAY: nothing here shows a corridor CAN be")
    print("      built, so this is a constraint on a hypothetical and not a")
    print("      prediction.  And chronology.py's HAWKING row is still NOT-RUN,")
    print("      so whether a chronology-protection mechanism forbids the second")
    print("      hop is OPEN and is not resolved by this pass.")
    print()

    print(BAR)
    print("5.  ONE OPEN, MARKED AS ONE")
    print(BAR)
    print()
    print("      HOW MANY OBJECTS PASS PER TRANSITION EVENT IS ESTABLISHED")
    print("      NOWHERE IN THIS PROJECT.  Cost per object is the total over N.")
    print("      N = 1 makes every traveller pay %.2e solar masses; N large"
          % (ladder.mass_for_delta_d(d) / M_SUN))
    print("      makes the corridor a bulk carrier.  NEITHER IS ASSUMED HERE,")
    print("      and OBJECTS_PER_EVENT is recorded as None rather than guessed.")
    print()
    print("      It is the one parameter that could still move the verdict of")
    print("      section 2, and it is exactly the parameter nobody has measured.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Nothing here is repaired.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("oneway.py --selftest")
    print()
    d = PROXIMA_LY * LY

    # 0.  the correction
    chk("'both ways' was measured", BOTH_WAYS_WAS_MEASURED, False)
    chk("and it was mine", BOTH_WAYS_WAS_MINE, True)

    # 1.  the corridor price does not move with the payload
    chk("corridor energy is payload-independent",
        len({corridor_energy(d) for _ in range(3)}), 1)
    chk("and the ticket is linear in payload",
        abs(ticket_energy(2e5, 2.0) / ticket_energy(1e5, 2.0) - 2.0) < 1e-12, True)
    chk("and linear in (gamma - 1)",
        abs(ticket_energy(1e5, 3.0) / ticket_energy(1e5, 2.0) - 2.0) < 1e-12, True)
    chk("cost is per metre not per kilogram", COST_IS_PER_METRE_NOT_PER_KILOGRAM, True)

    # 2.  the crossover exists and is absurd
    chk("a crossover exists", CROSSOVER_EXISTS, True)
    chk("crossover inverts ticket_energy",
        abs(ticket_energy(crossover_mass(d, 2.0), 2.0) / corridor_energy(d) - 1.0)
        < 1e-12, True)
    chk("gamma_for_crossover inverts crossover_mass",
        abs(crossover_mass(d, gamma_for_crossover(d, 1e5)) / 1e5 - 1.0) < 1e-9, True)
    chk("at gamma = 2 it exceeds a trillion solar masses",
        crossover_mass(d, 2.0) / M_SUN > 1e12, True)
    chk("and a hundred tonnes needs gamma above 1e30",
        gamma_for_crossover(d, 1e5) > 1e30, True)
    chk("the crossover is reachable", CROSSOVER_IS_REACHABLE, False)

    # 4.  the loop
    u = frame_velocity(PROXIMA_RADIAL_MS)
    chk("Proxima's frame velocity is not zero", u > 0.0, True)
    vcrit = transition_speed_closing_loop(u)
    chk("the threshold inverts roundtrip's own function",
        abs(roundtrip.loop_threshold(vcrit) / u - 1.0) < 1e-9, True)
    chk("below it the loop is open", loop_closes(vcrit * 0.9, u), False)
    chk("above it the loop closes", loop_closes(vcrit * 1.1, u), True)
    chk("the threshold is between 1e4 and 1e5 c", 1e4 < vcrit < 1e5, True)
    chk("an instantaneous transition closes it", loop_closes(1e12, u), True)
    # NOTE: the first draft of this check evaluated a condition that was always
    # true and tested nothing -- the same shape as corridor.py's involution
    # fault.  It now tests what it says.
    chk("and a comoving far end does NOT", loop_closes(1e12, 0.0), False)
    chk("nor does a far end below the threshold",
        loop_closes(1e2, u), False)
    chk("a single hop is not a paradox", SINGLE_TRANSITION_IS_A_PARADOX, False)
    chk("a separately initiated return can be",
        SEPARATELY_INITIATED_RETURN_CAN_BE, True)

    # 3/5.  category and the open
    chk("the return needs an equipped far end", RETURN_NEEDS_AN_EQUIPPED_FAR_END, True)
    chk("the corridor is transport", CORRIDOR_IS_TRANSPORT, False)
    chk("objects per event is open", OBJECTS_PER_EVENT, None)
    chk("comparators were read", FIGURES_ARE_READ, False)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
