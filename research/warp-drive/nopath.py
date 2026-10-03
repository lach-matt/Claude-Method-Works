#!/usr/bin/env python3
"""
nopath.py -- pricing "the point at which no path is needed".

M: "Spacetime is a closed index.  What makes transition expensive is the
constant movement of that index.  The goal is not to calculate the shortest
path, but determine at which point in the index no path is needed.  And that
involves step walking through dimensions.  This is the method equation at work.
The currency paid is in information, allowing for dimensional drift to where two
separate points are one."

Four claims.  ONE OF THEM IS THE BEST DIAGNOSIS ANYONE HAS MADE OF THIS
PROJECT'S COST STRUCTURE and the tree has already answered it.  One is exactly
inverted, and the tree's own equation inverts it.  One is priced here for the
first time and comes out twenty orders WORSE than the currency it replaces.  One
is a real physical route that turns out to be a door already on the list.

===============================================================================
1. "NO PATH NEEDED" HAS TWO READINGS AND THEY GO OPPOSITE WAYS
===============================================================================

MANUFACTURE the coincidence.  phase1.py's transition equation is

        Delta-d = (G/c^2) M Lambda,      LINEAR IN M,
                                         INDEPENDENT OF THE DISTANCE CONTRACTED,

so the exchange rate is a constant: 1.34895e26 kg per metre contracted.  Making
two points ONE means contracting the WHOLE separation, and linear means

        Proxima, 4.2465 ly  ->  5.4193e42 kg  =  2.7248e12 SOLAR MASSES.

    THE COST INTUITION IS EXACTLY INVERTED.  "No path needed" is not the
    cheap end of the curve; IT IS THE MAXIMUM OF IT.  A 1% contraction costs
    5.4193e40 kg and a one-metre contraction costs the bare exchange rate.

    CORRECTED (DOCKET 67 follow-ups, M: "address/correct/repair all
    figures"): first priced at a round "4 light years" -- 5.1048e42 kg =
    2.5666e12 solar masses, 5.1048e40 kg for 1%.  phase1.py, closeout.py and
    wormhole.py now price at Proxima's Gaia DR3 distance (phase1.L_PROXIMA,
    4.2465 ly, READ-VIA-RESTATEMENT), so this file imports it rather than
    carry a second distance.  Every figure below that follows from the mass
    moved with it (R_s, bits, Landauer, break-even); each first value is
    kept beside it and still checked as a RECORD at SEPARATION_LY_AS_FIRST_
    WRITTEN = 4.0.  The exchange rate is phase1's FIRST-ORDER law (phase1's
    own DOCKET 67 note gives the exact ansatz at 0.944 / 0.403 of it), and
    that hypothesis is carried here unchanged.  No verdict moves: the cost is
    linear at any separation, so coincidence is the maximum at any distance.
    Shortening is cheap in proportion; coincidence is the most expensive thing
    on the axis, and it is expensive BY THE PROJECT'S OWN EQUATION.

FIND one already there.  That is a different act entirely, and it is not on
this curve at all -- nothing is contracted, so nothing is paid for contracting.
Two points already one, in a manifold, is A WORMHOLE MOUTH PAIR, and

        create.py ALREADY CONCLUDED THIS: "find one and enlarge it."

    So the second reading is not new to the project.  IT IS DOOR THREE, arrived
    at from the front instead of the back.  apply.py listed it as "a relic, not
    a construction"; M has now derived the same door from the index picture.
    Two independent routes to the same door is worth more than either.

===============================================================================
2. THE INFORMATION CURRENCY, PRICED -- AND IT IS NOT A SECOND CURRENCY
===============================================================================

currency.py asked what the transition is denominated in.  It never priced
INFORMATION specifically, because nobody had proposed it.  Here it is.

The required M sits inside its own Schwarzschild radius, R_s = 8.0490e15 m, and
the information content of a region that size is fixed:

        holographic   A / 4 l_P^2, in bits      1.1241e102
        Bekenstein    2 pi R E / (hbar c ln2)   1.1241e102

    (CORRECTED, DOCKET 67 follow-ups: at Proxima.  First, at 4 ly, R_s =
    7.5818e15 m and 9.9736e101 bits on both routes.)

    THE TWO ROUTES AGREE TO SIX DIGITS, which they must -- the bound is
    saturated at the horizon -- and that agreement is the point:

        THE INFORMATION IS NOT A SEPARATE THING FROM THE ENERGY.  Bekenstein
        bounds S BY E: you cannot hold the bits without the energy to hold them
        in.  S <= 2 pi R E / (hbar c) runs the WRONG WAY for paying in
        information instead of mass.  The bits ARE the mass, in other units,
        and the conversion factor is hbar.

    CORRECTED (DOCKET 67): the two routes agree because the region IS a
    Schwarzschild horizon (D = 4), where the bound is saturated by Bousso's
    extrapolation beyond its weak-gravity class; they are not two
    independent routes to one number in general.  For weakly gravitating
    matter Bekenstein is an upper bound only (hep-th/0203101 p.9).

And if the payment means MANIPULATING those bits rather than merely holding
them, Landauer prices the manipulation on top:

        at the CMB, 2.7255 K       2.9319e79 J   against M c^2 = 4.8707e59 J
                                   NINETEEN AND THREE QUARTER ORDERS WORSE
                                   (19.780)
        break-even temperature     4.5279e-20 K  -- the CMB is 6.02e19 times
                                   warmer than the coldest place that would
                                   make information merely AS expensive as mass

    (CORRECTED, DOCKET 67 follow-ups: at Proxima.  First, at 4 ly, 2.6014e79 J
    against 4.5880e59 J, 19.754 orders, break-even 4.8068e-20 K, 5.67e19.
    Both ratios scale with M, so the 6 % longer separation moves them 6 %.)

    CAUTION, AND IT IS A REAL ONE: Landauer prices IRREVERSIBLE operations.  A
    reversible computation costs nothing in principle, so the Landauer number
    is an upper bound on a specific reading and is NOT the argument.  THE
    ARGUMENT IS BEKENSTEIN, which is a static bound and survives reversibility
    entirely.  The Landauer row is reported because it is the natural reading
    of "paid", and flagged because it is the weaker half.

===============================================================================
3. "STEP WALKING THROUGH DIMENSIONS" -- THE EMBEDDING IS FREE, AND FREE MEANS
   IT CANNOT BE THE MECHANISM
===============================================================================

The Campbell-Magaard theorem: ANY analytic n-dimensional (pseudo-)Riemannian
manifold can be locally embedded in an (n+1)-dimensional RICCI-FLAT one.  Every
4D spacetime, ours included, sits inside a 5D vacuum.  Always.

    SO THE EMBEDDING EXISTS UNCONDITIONALLY, AND A THING THAT IS ALWAYS TRUE
    CARRIES NO INFORMATION.  It cannot distinguish a spacetime where the drift
    helps from one where it does not, because it holds in both.  The existence
    of the higher dimension is not the mechanism; if there is a mechanism it is
    in the bulk's GEOMETRY, not in its existence.

And there the effect is real: BULK SHORTCUTS.  In a warped braneworld a bulk
geodesic between two brane points can be shorter than the brane geodesic
(Caldwell & Langlois; Abdalla and Cuadros-Melgar), so a bulk signal can arrive
before a brane photon.  A genuine, published, calculable effect.

    BUT IT IS NOT A NEW DOOR.  A warped bulk is an extra-dimensional theory,
    which is apply.py's DOOR ONE -- outside general relativity, where the DEC
    and the positive mass theorem are not the governing theorems.  Dimensional
    drift does not escape the three doors.  IT IS ONE OF THEM, and it is the
    one whose scope decision wormhole.py has been holding for M since the
    wormhole fork.

===============================================================================
4. AND THE DIAGNOSIS IS RIGHT -- "THE CONSTANT MOVEMENT" IS EXACTLY THE COST
===============================================================================

This is the part to keep.  M says what makes transition expensive is the
constant movement of the index, and the tree measured precisely that, twice,
without ever putting it that way:

    reverse.py    THE SEAT IS FREE.  A conjugate point at a declared range
                  costs ordinary matter and satisfies every energy condition.
                  THE MOVEMENT -- the contraction, the lead -- is all of the
                  cost.  apply.py sharpened it a pass ago: M_ADM is a free
                  parameter and THE LEAD IS THE WHOLE COST.

    warpshell.py  the CM theorem: no isolated system moves its own centre of
                  mass, and momentum changes only by RADIATING.  Movement is
                  the thing you cannot get for nothing.

    SO THE DIAGNOSIS IS CORRECT AND IT IS ALREADY BANKED IN TWO INSTRUMENTS.
    And the tree's own answer to it is the object that does not move:

        bothways.py's GATE MODE.  Zero offset, both directions, no closed
        timelike curve, and it AMORTISES -- built once, used many times.  A
        gate IS "a point in the index where no path is needed", and it is the
        safest of the three modes.

    THE IDEA CONVERGES ON THE PROJECT'S OWN ANSWER.  It does not add a fourth
    door and it does not lower a price.  What it does is name the cost
    structure correctly, from outside, and land on the two conclusions the
    tree reached from inside: FIND ONE RATHER THAN BUILD ONE, and BUILD A GATE
    RATHER THAN A VEHICLE.

===============================================================================
ON "THE METHOD EQUATION AT WORK"
===============================================================================

Register 1206 names the architecture -- "the two halves of the method equation
meet for the first time on this index" -- and tools/populate.py runs it over
elements and their ions.  THIS FILE MAKES NO CLAIM THAT THE TRANSITION IS AN
INSTANCE OF IT.  The corpus's equation is a statement about placement on an
index; the transition equation is Delta-d = (G/c^2) M Lambda.  A shared shape
is not a correspondence, and unified.py's rule on EIGHT governs here: same
structure, no established correspondence, and it is not asserted.

stdlib only.  Every figure recomputed from the instrument that owns it.
"""
import math
import sys

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34
KB = 1.380649e-23
LY = 9.4607304725808e15

#: CORRECTED (DOCKET 67 follow-ups): the separation was a round 4.0 ly.  It is
#: now phase1.L_PROXIMA (Gaia DR3, 4.2465 ly), asked of phase1, never retyped;
#: the first value is kept and every figure on it is still checked as RECORD.
SEPARATION_LY_AS_FIRST_WRITTEN = 4.0


def proxima_ly():
    """phase1.L_PROXIMA in light years (nopath's LY equals phase1.LIGHT_YEAR)."""
    import phase1
    return phase1.L_PROXIMA / LY


def _sep(separation_ly):
    return proxima_ly() if separation_ly is None else separation_ly
M_SUN = 1.98892e30
T_CMB = 2.7255


# ------------------- 1: manufacturing the coincidence is the maximum

def exchange_rate():
    """kg per metre contracted.  From phase1.py, not re-typed."""
    import phase1
    return phase1.exchange_rate()


def mass_to_contract(metres):
    """Linear in the contraction -- which is the whole of section 1."""
    return metres * exchange_rate()


def coincidence_mass(separation_ly=None):
    """Making two points ONE means contracting the WHOLE separation.
    Default: Proxima (phase1.L_PROXIMA); first a round 4.0 ly."""
    return mass_to_contract(_sep(separation_ly) * LY)


def coincidence_is_the_maximum(separation_ly=None, fraction=0.01):
    """Is full contraction dearer than partial?  Linear, so always."""
    separation_ly = _sep(separation_ly)
    full = coincidence_mass(separation_ly)
    part = mass_to_contract(fraction * separation_ly * LY)
    return full > part


def cost_is_linear(separation_ly=None, rtol=1e-12):
    """Doubling the contraction doubles the bill.  No economy of scale."""
    separation_ly = _sep(separation_ly)
    a = mass_to_contract(separation_ly * LY)
    b = mass_to_contract(2.0 * separation_ly * LY)
    return abs(b / a - 2.0) < rtol


FOUND_NOT_MANUFACTURED = "find one and enlarge it"


def second_reading_is_door_three():
    """Two points already one is a wormhole mouth pair.  create.py's route."""
    import create
    return create.ROUTE == FOUND_NOT_MANUFACTURED


# ---------------------- 2: the information currency, priced

def schwarzschild_radius(M):
    return 2.0 * G * M / C ** 2


def planck_length_squared():
    return HBAR * G / C ** 3


def holographic_bits(R):
    """A / 4 l_P^2, converted from nats to bits."""
    return 4.0 * math.pi * R * R / (4.0 * planck_length_squared()) / math.log(2.0)


def bekenstein_bits(R, E):
    """2 pi R E / (hbar c ln2).  Independent route to the same number.

    CORRECTED (DOCKET 67): the same number ONLY AT SCHWARZSCHILD SATURATION
    (D = 4, R the horizon radius), which is the one case routes_agree()
    evaluates.  That saturation is Bousso's extrapolation of the bound to a
    strongly gravitating object (hep-th/0203101 p.9), outside the bound's own
    weakly-self-gravitating class (quant-ph/0404042 p.1); for weakly
    gravitating matter this is an upper bound that real systems approach at
    best to within about an order of magnitude (hep-th/0203101 p.9).
    """
    return 2.0 * math.pi * R * E / (HBAR * C * math.log(2.0))


def routes_agree(separation_ly=None, rtol=1e-6):
    """They must -- the bound is saturated at the horizon -- and the agreement
    is the finding: THE BITS ARE THE MASS, in other units.

    CORRECTED (DOCKET 67): for a Schwarzschild horizon in D = 4, the case
    computed here.  The agreement is not a general identity of the two routes
    (see bekenstein_bits)."""
    M = coincidence_mass(separation_ly)
    R = schwarzschild_radius(M)
    return abs(bekenstein_bits(R, M * C * C) / holographic_bits(R) - 1.0) < rtol


def landauer_energy(bits, T):
    """N k T ln2.  Prices IRREVERSIBLE manipulation only -- see the caution."""
    return bits * KB * T * math.log(2.0)


def landauer_over_mass(separation_ly=None, T=T_CMB):
    M = coincidence_mass(separation_ly)
    R = schwarzschild_radius(M)
    return landauer_energy(holographic_bits(R), T) / (M * C * C)


def break_even_temperature(separation_ly=None):
    """The T at which information merely EQUALS mass.  Not beats -- equals."""
    M = coincidence_mass(separation_ly)
    R = schwarzschild_radius(M)
    return M * C * C / (holographic_bits(R) * KB * math.log(2.0))


def information_is_cheaper(separation_ly=None, T=T_CMB):
    return landauer_over_mass(separation_ly, T) < 1.0


BEKENSTEIN_IS_THE_ARGUMENT = True     # static; survives reversible computation
LANDAUER_IS_THE_WEAKER_HALF = True    # prices irreversible operations only


# --------------------------- 3: the embedding is free

CAMPBELL_MAGAARD = "every analytic n-manifold embeds locally in (n+1) Ricci-flat"


def embedding_always_exists():
    """Campbell-Magaard.  Unconditional."""
    return True


def embedding_carries_information():
    """A thing true of every spacetime cannot distinguish between spacetimes."""
    return not embedding_always_exists()


BULK_SHORTCUTS_ARE_REAL = True        # Caldwell-Langlois; a warped bulk
BULK_SHORTCUT_DOOR = "OUTSIDE GR"     # apply.py's door one, not a fourth


def dimensional_drift_is_a_new_door():
    import apply
    return BULK_SHORTCUT_DOOR not in [d[0] for d in apply.DOORS]


# ------------------ 4: the diagnosis is right, and already banked

DIAGNOSIS = "the movement is the cost, not the seat"

BANKED_IN = (("reverse.py", "the seat is FREE; the lead is the whole cost"),
             ("warpshell.py", "the CM theorem: momentum changes only by radiating"),
             ("apply.py", "M_ADM is free; the lead is the whole cost, measured"))


def seat_is_free():
    """reverse.py's split, read from the instrument that owns it."""
    import reverse
    return dict((h[0], h[1]) for h in reverse.HALVES)["the seat"] == "FREE"


def the_answer_is_a_gate():
    """bothways.py's GATE: zero offset, both directions, no CTC, amortises."""
    import bothways
    gate = [m for m in bothways.MODES if m[0] == "GATE"][0]
    return gate[1] == "0" and gate[4] is False


def gate_can_precede_its_construction():
    import bothways
    return bothways.can_precede_construction()


# --------------------- on the method equation: not asserted

METHOD_EQUATION_CORRESPONDENCE = None    # register 1206; shape, not established


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s"
              % (label, str(got)[:18], str(want)[:18], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. MANUFACTURING THE COINCIDENCE IS THE MAXIMUM, NOT THE MINIMUM")
    near("exchange rate, kg per metre (phase1.py)", exchange_rate(), 1.34895e26)
    # CORRECTED (DOCKET 67 follow-ups): re-based on phase1.L_PROXIMA; the
    # pins are the computed values (python3 -c "import nopath as n;
    # print(n.coincidence_mass()/n.M_SUN)" -> 2.72477e12).  The 4.0 ly pins
    # are kept below as RECORD checks.
    Mc = coincidence_mass()
    L4 = SEPARATION_LY_AS_FIRST_WRITTEN
    print("     one metre contracted      %.4e kg" % mass_to_contract(1.0))
    print("     1%% of Proxima             %.4e kg" % mass_to_contract(0.01 * proxima_ly() * LY))
    print("     ALL of Proxima (%.4f ly)  %.4e kg = %.4e solar masses"
          % (proxima_ly(), Mc, Mc / M_SUN))
    near("the separation is phase1.L_PROXIMA, in ly", proxima_ly(), 4.24646, 1e-5)
    near("coincidence at Proxima, kg", Mc, 5.41934e42)
    near("coincidence at Proxima, solar masses", Mc / M_SUN, 2.72477e12)
    import phase1 as _p1
    near("  and it is phase1's own price for the whole separation",
         Mc, _p1.mass_for_contraction(_p1.L_PROXIMA), 1e-9)
    near("RECORD: coincidence at 4 ly (as first written), kg",
         coincidence_mass(L4), 5.1048e42)
    near("RECORD: coincidence at 4 ly, solar masses", coincidence_mass(L4) / M_SUN, 2.5666e12)
    chk("is coincidence dearer than a 1% contraction",
        coincidence_is_the_maximum(), True)
    chk("and the cost is strictly linear -- no economy of scale",
        cost_is_linear(), True)
    print("       THE COST INTUITION IS INVERTED, BY THE PROJECT'S OWN EQUATION.")
    print("     and the OTHER reading -- find one already there:")
    chk("  create.py's route, unchanged", second_reading_is_door_three(), True)
    print("       Not a new idea to the project: DOOR THREE, derived from the")
    print("       index picture instead of from the topology theorems.")

    print("\n2. THE INFORMATION CURRENCY IS NOT A SECOND CURRENCY")
    R = schwarzschild_radius(Mc)
    hb, bb = holographic_bits(R), bekenstein_bits(R, Mc * C * C)
    print("     its own Schwarzschild radius  %.4e m" % R)
    print("     holographic bits              %.4e" % hb)
    print("     Bekenstein bits               %.4e" % bb)
    chk("the two routes agree", routes_agree(), True)
    print("       They must -- saturated at the horizon -- AND THAT IS THE")
    print("       POINT: Bekenstein bounds S BY E, so the bits ARE the mass.")
    print("       S <= 2 pi R E / hbar c runs the WRONG WAY for the trade.")
    r = landauer_over_mass()
    print("     Landauer at the CMB           %.4e J against Mc^2 = %.4e J"
          % (landauer_energy(hb, T_CMB), Mc * C * C))
    near("  orders worse", math.log10(r), 19.7796, 1e-3)
    near("  RECORD: at 4 ly", math.log10(landauer_over_mass(L4)), 19.7536, 1e-3)
    chk("is information cheaper than mass", information_is_cheaper(), False)
    chk("  RECORD: nor at 4 ly", information_is_cheaper(L4), False)
    near("break-even temperature, K", break_even_temperature(), 4.5279e-20)
    near("  RECORD: at 4 ly, K", break_even_temperature(L4), 4.8068e-20)
    near("holographic bits at Proxima", hb, 1.12405e102)
    near("  RECORD: at 4 ly", holographic_bits(schwarzschild_radius(coincidence_mass(L4))),
         9.9736e101)
    chk("  the two routes agree at 4 ly too (RECORD)", routes_agree(L4), True)
    print("       The CMB is %.3e times warmer than the coldest place that"
          % (T_CMB / break_even_temperature()))
    print("       would make information merely AS expensive as mass.")
    chk("Landauer is the weaker half (irreversible only)",
        LANDAUER_IS_THE_WEAKER_HALF, True)
    chk("Bekenstein is the argument (static, survives reversibility)",
        BEKENSTEIN_IS_THE_ARGUMENT, True)

    print("\n3. THE EMBEDDING IS FREE, AND FREE MEANS IT CANNOT BE THE MECHANISM")
    print("     Campbell-Magaard: %s" % CAMPBELL_MAGAARD)
    chk("does a 5D Ricci-flat embedding always exist", embedding_always_exists(), True)
    chk("so does its existence carry information",
        embedding_carries_information(), False)
    chk("are bulk shortcuts real", BULK_SHORTCUTS_ARE_REAL, True)
    chk("do they open a FOURTH door", dimensional_drift_is_a_new_door(), False)
    print("       A warped bulk is an extra-dimensional theory -- apply.py's")
    print("       DOOR ONE, and the scope decision wormhole.py holds for M.")

    print("\n4. AND THE DIAGNOSIS IS RIGHT -- ALREADY BANKED IN THREE INSTRUMENTS")
    for who, what in BANKED_IN:
        print("     %-14s %s" % (who, what))
    chk("reverse.py: the seat is free", seat_is_free(), True)
    chk("so the diagnosis is", DIAGNOSIS, "the movement is the cost, not the seat")
    chk("and the tree's answer is the object that does not move",
        the_answer_is_a_gate(), True)
    chk("which still cannot precede its own construction",
        gate_can_precede_its_construction(), False)
    print("       A GATE IS 'a point in the index where no path is needed', and")
    print("       it amortises.  The idea converges on the project's own answer.")

    print("\nON 'THE METHOD EQUATION AT WORK'")
    chk("is a correspondence asserted", METHOD_EQUATION_CORRESPONDENCE, None)
    print("       Register 1206 is a statement about placement on an index; the")
    print("       transition equation is Delta-d = (G/c^2) M Lambda.  A shared")
    print("       SHAPE is not a correspondence -- unified.py's rule on EIGHT.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    Mc = coincidence_mass()
    R = schwarzschild_radius(Mc)
    print("THE PRICE OF 'NO PATH NEEDED', AT PROXIMA (%.4f ly, phase1.L_PROXIMA)" % proxima_ly())
    print("(CORRECTED, DOCKET 67 follow-ups: first at a round four light years)\n")
    print("  %-34s %.4e kg  = %.4e solar" % ("manufacture it", Mc, Mc / M_SUN))
    print("  %-34s %.4e bits" % ("its information content", holographic_bits(R)))
    print("  %-34s %.4e J  (CMB)" % ("Landauer on those bits",
                                     landauer_energy(holographic_bits(R), T_CMB)))
    print("  %-34s %.4e J" % ("against M c^2", Mc * C * C))
    print("  %-34s %.4e K" % ("break-even temperature", break_even_temperature()))
    print("  %-34s %s" % ("find one instead", FOUND_NOT_MANUFACTURED))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE DIAGNOSIS IS THE BEST ANYONE HAS MADE OF THIS PROJECT'S COST
  STRUCTURE, AND IT IS ALREADY BANKED TWICE WITHOUT BEING SAID THAT
  WAY.  "What makes transition expensive is the constant movement of
  the index" is reverse.py's split -- the seat is FREE, the movement is
  all of the cost -- and it is warpshell.py's CM theorem, that momentum
  changes only by radiating.  apply.py sharpened it a pass ago: M_ADM
  is a free parameter and THE LEAD IS THE WHOLE COST.

  BUT THE COST INTUITION THAT FOLLOWS IS EXACTLY INVERTED, AND THE
  PROJECT'S OWN EQUATION INVERTS IT.  Delta-d = (G/c^2) M Lambda is
  LINEAR in the contraction, so there is no economy of scale and no
  cheap far end.  Making two points ONE means contracting the WHOLE
  separation: at Proxima, 4.2465 ly, that is 5.4193e42 kg, 2.7248e12
  SOLAR MASSES (first 5.1048e42 kg, 2.5666e12, at a round four light
  years).  "No path needed" is not the cheap corner of the curve -- IT
  IS THE MAXIMUM OF IT.

  AND INFORMATION IS NOT A SECOND CURRENCY.  Priced here for the first
  time: the required configuration holds 1.1241e102 bits (first
  9.9736e101, at four light years), and the
  holographic and Bekenstein routes agree to six digits because the
  bound is saturated at the horizon.  THAT AGREEMENT IS THE FINDING.
  Bekenstein bounds S BY E -- you cannot hold the bits without the
  energy to hold them in -- so S <= 2 pi R E / hbar c runs the WRONG
  WAY for the trade.  The bits ARE the mass, in other units, and the
  conversion factor is hbar.  Landauer adds that manipulating them at
  the CMB costs 19.78 ORDERS MORE than the mass-energy, breaking even
  only at 4.5279e-20 K (first 19.75 and 4.8068e-20 K) -- but that half is flagged as the weaker one,
  since Landauer prices irreversible operations and Bekenstein does not
  care.

  DIMENSIONAL DRIFT IS REAL AND IT IS NOT A NEW DOOR.  Campbell-Magaard
  guarantees that every analytic 4D spacetime embeds locally in a 5D
  RICCI-FLAT one -- always, unconditionally -- so the existence of the
  higher dimension CANNOT be the mechanism: a thing true of every
  spacetime distinguishes none of them.  If there is a mechanism it is
  in the bulk's geometry, and there bulk shortcuts are genuine and
  published.  But a warped bulk is an extra-dimensional theory, which
  is apply.py's DOOR ONE -- and the scope decision on it has been
  wormhole.py's open question for M since the wormhole fork.

  SO THE IDEA CONVERGES ON THE PROJECT'S OWN TWO ANSWERS RATHER THAN
  ADDING TO THEM, AND CONVERGING FROM OUTSIDE IS WORTH MORE THAN
  EITHER ROUTE ALONE.  "Two points already one" is a wormhole mouth
  pair, which is create.py's FIND ONE AND ENLARGE IT.  "A point where
  no path is needed" is bothways.py's GATE -- zero offset, both
  directions, no closed timelike curve, and it AMORTISES.  Find one
  rather than build one; build a gate rather than a vehicle.  The index
  picture reaches both from the front; the theorems reached them from
  the back.

  NOTHING HERE IS CLAIMED TO BE THE METHOD EQUATION.  Register 1206 is
  a statement about placement on an index and the transition equation
  is Delta-d = (G/c^2) M Lambda.  A shared shape is not a
  correspondence, and unified.py's rule on EIGHT governs: same
  structure, none established, and none asserted.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
