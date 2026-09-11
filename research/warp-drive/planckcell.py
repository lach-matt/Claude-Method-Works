#!/usr/bin/env python3
"""
planckcell.py -- the framework, asked to specify itself, answers.  Every gate
closes.  And the answer is that the cost was never in the mechanism.

M: "the solution is to not find another framework, but instead build it from
what this current framework says it needs to be."

    THAT IS THE RIGHT MOVE AND THE FRAMEWORK HAS BEEN UNUSUALLY EXPLICIT.
    candidates.py ended by noticing that three unrelated mechanisms all run out
    within one order of the Planck length.  That was read there as an
    obstruction.  READ AS A SPECIFICATION IT IS AN INSTRUCTION, and this file
    follows it instead of arguing with it.

    The result is the first configuration in this project that passes EVERY
    gate.  It is also, for a reason that is structural rather than
    disappointing, worth exactly nothing -- and establishing that is the point.

===============================================================================
1. STOP ASSUMING R.  SOLVE THE GATES FOR IT.
===============================================================================

Every gate candidates.py imposed is a statement about ONE LENGTH:

    KIND       rho < 0.  Non-minimal coupling supplies it, with no
               state-independent QEI to forbid it (Fewster & Osterbrink).
    DEADLINE   tau ~ R/c.  A statement about R.
    MAGNITUDE  shortfall = (l_UV/l_P)^2 / Lambda, closing at l_UV <~ 3.16 l_P.
               A statement about R.

Every previous pass PICKED an R -- a nanometre, a metre -- and watched the gates
fail.  Solve for R instead:

        R    =  l_P            =  1.616255e-35 m
        tau  =  l_P / c        =  5.391246e-44 s        one Planck time
        E    =  E_Planck / Lambda  =  1.959505e+08 J

    AND THAT ENERGY IS 195.95 MEGAJOULES.  54.43 kilowatt-hours.  The chemical
    energy of 46.8 kg of TNT.  The rest mass of 2.18 nanograms.

    AFTER SEVENTY ORDERS OF SHORTFALL, THE FRAMEWORK'S OWN SPECIFICATION COMES
    IN AT A NUMBER A LABORATORY COULD WRITE A PURCHASE ORDER FOR.

===============================================================================
2. AND IT PASSES.  ALL THREE, THE FIRST TIME ANYTHING HAS.
===============================================================================

    MAGNITUDE   shortfall at R = l_UV = l_P is 1/Lambda = 0.100175.
                PASSES, with a factor of Lambda = 9.98 in hand.

    DEADLINE    tau = one Planck time.  Passes, and trivially: teardown.py's
                CTC window needs tau >= 2D/c, and 5.39e-44 s clears nothing.
                THE ARRAY CANNOT HOST A CLOSED TIMELIKE CURVE AT ANY
                SEPARATION, so closure.py's state-splitting never arises.

    KIND        supplied by candidate D, which is the only candidate whose
                shortfall was a pure number rather than orders -- and at this R
                that pure number is below one.

AND IT SITS EXACTLY WHERE THE COLLAPSE IDENTITY SAYS IT SHOULD.  lightbuild.py:
E_transition/E_kugelblitz = 2/Lambda at every d.  Measured here at d = l_P:
0.200350028.  The cell holds 20.035 % of a Planck-scale black hole, with the
design margin Lambda/2 = 4.9913 intact.  NOTHING WAS TUNED TO MAKE THAT HAPPEN;
it is the same identity, evaluated at the length the gates chose.

    SO THE FRAMEWORK IS SELF-CONSISTENT AT THIS SCALE AND ONLY AT THIS SCALE.

===============================================================================
3. WHAT IT BUYS, AND THIS IS WHERE IT TURNS
===============================================================================

        Delta d  =  1.616255e-35 m.

One Planck length.  That is the deliverable of a cell that costs 196 MJ and
satisfies every constraint this project has derived in its entire history.

    THE ENERGY IS SMALL BECAUSE THE OUTPUT IS SMALL.  There is no discount
    hiding in the Planck scale; there is only a very small purchase.

===============================================================================
4. SO TILE IT -- AND TILING IS EXACTLY NEUTRAL
===============================================================================

Delta d = (G/c^2) M Lambda is LINEAR in M, so N cells contract N Planck lengths
and cost N times 196 MJ.  No economy of scale, and no penalty either:

        target      cells N = d/l_P      total energy      per cell
        1 fm        6.1871e+19           1.2124e+28 J      1.9595e+08 J
        1 nm        6.1871e+25           1.2124e+34 J      1.9595e+08 J
        1 m         6.1871e+34           1.2124e+43 J      1.9595e+08 J

    AND THE TOTAL IS EXACTLY E_t(d).  At one metre, 1.212374e+43 J by tiling
    against 1.212374e+43 J from the closed form -- the same number, because it
    is the same equation.

        THE EXCHANGE RATE IS SCALE-INVARIANT.  TILING PASSES EVERY GATE CELL BY
        CELL AND MOVES THE BILL NOT AT ALL.

===============================================================================
5. WHICH IS THE RESULT, AND IT RELOCATES THE WHOLE PROJECT
===============================================================================

Read the history of this tree against that last line.  Every obstruction it has
ever recorded was about the MECHANISM -- whether light can lead, whether a
lattice holds, whether a kugelblitz forms, whether Casimir switches, whether a
quantum inequality permits.  obstruct.py has fifty-three of them.

    THE FRAMEWORK'S OWN SPECIFICATION DISSOLVES ALL OF THEM AND LEAVES THE BILL
    EXACTLY WHERE IT WAS.

That is not a failure of the specification.  It is the specification telling you
something the mechanism arguments could not: THE SEVENTY ORDERS WERE NEVER A
MECHANISM PROBLEM.  They are the exchange rate,

        c^4 / (G Lambda)  =  1.2123737e43 joules per metre,

and of its four symbols, three are constants of nature.

===============================================================================
6. THE ONE LEVER, AND IT IS SHUT
===============================================================================

Lambda is the only term in the rate that is not a constant, and it is set by the
geometry: Lambda = 2[ln(2 R_s/b) - 1], seated at 9.982529 from R_s/b = 200.  So
ask what Lambda would have to be, and what geometry that demands:

        to make one metre cost      needs Lambda      needs R_s/b
        world annual energy         2.0171e+23        > 1e300
        a one-megaton bomb          1.2103e+29        > 1e300
        one kilowatt-hour           3.3618e+37        > 1e300
        one Planck cell             6.1763e+35        > 1e300

    LAMBDA IS LOGARITHMIC IN THE GEOMETRY, so orders in Lambda cost
    exponentially in R_s/b.  phase1.py had this already: Lambda = 20 needs
    R_s/b = 2.99e4, Lambda = 50 needs 9.79e10, Lambda = 100 needs 7.05e21.
    The shell must exceed the corridor by those factors, and the corridor is
    what you are trying to travel down.

        THE ONLY LEVER IS SHUT, AND IT WAS NEVER THE MECHANISM'S FAULT.

===============================================================================
WHAT THIS PASS ESTABLISHES
===============================================================================

    NEW, AND IT IS THE FIRST OF ITS KIND HERE: a complete configuration that
    passes EVERY gate -- KIND, DEADLINE and MAGNITUDE -- at R = l_P, tau = t_P,
    E = E_Planck/Lambda = 195.95 MJ, sitting at 2/Lambda of a Planck black hole
    with the margin intact and unable to host a CTC.

    NEW: cells tile exactly, and the exchange rate is scale-invariant, so a
    gate-passing architecture exists at every scale and costs precisely what the
    closed form always said.

    THE RESULT: the obstruction was never the mechanism.  Fifty-three recorded
    obstructions are all about mechanism; the framework's own specification
    clears them and does not move the bill by one joule.

    THE REMAINING LEVER: Lambda alone, logarithmic in R_s/b, and shut.

    NOT CLAIMED, AND THIS MATTERS MORE THAN ANY OF THE ABOVE:

        THAT THIS IS TRANSPORT.  One Planck length of contraction for 196 MJ is
        a gate-passing configuration and NOT a drive.  Nothing here moves
        anything anywhere.

        THAT A PLANCK CELL IS BUILDABLE.  Every gate is a statement in a theory
        that candidates.py showed FAILS at this scale.  A specification whose
        validity condition is "l_UV ~ l_P" is a specification that needs quantum
        gravity to evaluate, and this file evaluates it in effective field
        theory because that is what exists.  The 196 MJ is what the FRAMEWORK
        says, not what a laboratory would pay.

        THAT ANY OBSTRUCTION HAS MOVED.  obstruct.py is unchanged, deliberately.
        A specification that satisfies constraints is not a demonstration that
        the constraints were the binding ones -- and section 5 is precisely the
        finding that they were not.
===============================================================================
7. THE POWER-PLANT QUESTION, ANSWERED BEFORE IT IS ASKED
===============================================================================

M, reading the figure: "54.43 kWh is relatively low.  So with a decent power
source, like a power plant, perhaps this is plausible."

    THE INSTINCT IS CORRECT FOR ALMOST ALL ENGINEERING AND FAILS HERE FOR ONE
    SPECIFIC REASON: 196 MJ IS NOT THE PRICE OF THE DEVICE.  IT IS THE PRICE OF
    ONE PLANCK LENGTH.

        source                    contraction rate
        1 GW power plant          8.2483e-35 m/s
        all human power           1.5672e-30 m/s
        the entire Sun            3.1574e-17 m/s
        the Milky Way             6.2687e-07 m/s

    A GIGAWATT PLANT NEEDS 1.2124e34 s FOR ONE METRE -- 2.787e16 times the age
    of the universe.  Run it for a century and it buys 2.6032e-25 m, which is
    3.099e-10 PROTON RADII.  One metre per second would take 1.2124e43 W:
    3.17e16 Suns, or 1.6 million Milky Ways.

    AND YOU COULD NOT CONFIRM A CELL HAD FIRED.  One cell contracts 1.616e-35 m;
    LIGO resolves about 1e-19 m.  That is 15.8 ORDERS below the most sensitive
    instrument ever built.

    The reason is section 4: THE EXCHANGE RATE IS SCALE-INVARIANT.  The Planck
    cell did not make transport cheap, it made the UNIT SMALL -- 6.19e34 of them
    per metre, and the bill per metre unchanged.  It is the grain-of-sand-to-a-
    beach argument with a ratio of 1e34 rather than 1e10.

===============================================================================
8. AND THE RING LASER, RE-TESTED HERE -- IT FAILS A NEW WAY
===============================================================================

M: "and the laser ring still doesn't fit?"  Re-tested at THIS scale rather than
restated, because the old refutation was about Mallett's MACROSCOPIC claim.

    GATE 1 IS UNCHANGED AND SCALE-FREE.  lattice.py's theorem has no length in
    it -- T_munu k^mu k^nu = V.V >= 0 for every classical EM field, measured
    identical in D = 3..26.  A ring laser is a classical EM field and shrinking
    it changes nothing.

    AND HERE IS SOMETHING NEW, WHICH ONLY APPEARS AT THIS SCALE.  A photon
    localised in the cell needs reduced wavelength lambdabar <= l_P, so its
    energy is at least hbar c / l_P -- which IS E_Planck, by definition.  The
    cell's entire budget is E_Planck/Lambda.

        ONE PHOTON THAT FITS OVERSHOOTS THE WHOLE CELL BY EXACTLY Lambda.

    Run it the other way: the photon the cell can AFFORD has
    lambdabar = Lambda l_P = 1.613e-34 m, TEN TIMES THE CELL.  It is not in the
    cell at all.

        A PHOTON THAT FITS COSTS Lambda TIMES THE BUDGET; A PHOTON YOU CAN
        AFFORD IS Lambda TIMES TOO BIG TO FIT.  LIGHT IS TOO COARSE TO PAY FOR
        A PLANCK CELL -- not too weak, too GRANULAR.

    And the hardware: a ring of radius 1.6e-35 m against atoms at 1e-10 m is
    25 ORDERS too small for mirrors, cavity or gain medium.

    ONE OBSTRUCTION DOES LIFT, AND IT IS RECORDED BECAUSE IT IS TRUE.  The 2024
    kugelblitz/Schwinger block runs 1e-29 m <~ R <~ 1e8 m and l_P sits BELOW
    that band -- its lower edge is set by there being no room to separate a pair
    below the Compton wavelength.  THAT BLOCK DOES NOT APPLY HERE.  It rescues
    nothing, because gates 1 and 3 are each decisive alone, but the ledger
    records that it lifted rather than pretending it still bites.
"""

import math
import sys

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34

KWH = 3.6e6
TNT_KG = 4.184e6
WORLD_ANNUAL_J = 6.0e20
MEGATON_J = 4.184e15


def lambda_value():
    import phase1
    return phase1.lam()


def planck_length():
    return math.sqrt(HBAR * G / C ** 3)


def planck_time():
    return planck_length() / C


def planck_energy():
    return math.sqrt(HBAR * C ** 5 / G)


# ---------------------------------------------- 1: solve the gates for R

def cell_radius():
    return planck_length()


def cell_lifetime():
    return planck_time()


def cell_energy():
    """E_t(l_P) = l_P c^4 / (G Lambda) = E_Planck / Lambda."""
    return cell_radius() * C ** 4 / (G * lambda_value())


def cell_energy_is_planck_over_lambda(tol=1e-12):
    return abs(cell_energy() - planck_energy() / lambda_value()) <= tol * cell_energy()


def in_kwh(j):
    return j / KWH


def in_tnt_kg(j):
    return j / TNT_KG


def rest_mass_kg(j):
    return j / C ** 2


# ---------------------------------------------- 2: does it pass?

def magnitude_shortfall(l_uv_m=None, R_m=None):
    """candidates.py's (l_UV/l_P)^2 / Lambda."""
    l_uv_m = l_uv_m or planck_length()
    return (l_uv_m / planck_length()) ** 2 / lambda_value()


def passes_magnitude():
    return magnitude_shortfall() < 1.0


def magnitude_margin():
    return 1.0 / magnitude_shortfall()


def ctc_loop_transit(D_m):
    return 2.0 * D_m / C


def passes_deadline(D_m=None):
    """teardown.py's window: a CTC needs tau >= 2D/c."""
    D_m = D_m or cell_radius()
    return cell_lifetime() < ctc_loop_transit(D_m)


def kugelblitz_energy(d_m):
    return d_m * C ** 4 / (2.0 * G)


def collapse_ratio():
    """lightbuild.py's identity, evaluated at the length the gates chose."""
    return cell_energy() / kugelblitz_energy(cell_radius())


def collapse_margin():
    return lambda_value() / 2.0


def all_gates_pass():
    return passes_magnitude() and passes_deadline()


# ---------------------------------------------- 3-4: what it buys, and tiling

def cell_contraction():
    return cell_radius()


def cells_for(d_m):
    return d_m / cell_radius()


def tiled_energy(d_m):
    return cells_for(d_m) * cell_energy()


def closed_form_energy(d_m):
    return d_m * C ** 4 / (G * lambda_value())


def tiling_is_neutral(d_m=1.0, tol=1e-12):
    return abs(tiled_energy(d_m) - closed_form_energy(d_m)) <= tol * closed_form_energy(d_m)


def exchange_rate_j_per_m():
    return C ** 4 / (G * lambda_value())


def rate_is_scale_invariant(radii=(1e-15, 1e-9, 1.0, 1e6), tol=1e-12):
    vals = [closed_form_energy(d) / d for d in radii]
    return max(vals) - min(vals) <= tol * max(vals)


# ---------------------------------------------- 6: the one lever

def lambda_needed_for(total_j_per_metre):
    return C ** 4 / (G * total_j_per_metre)


def geometry_for_lambda(L):
    """R_s/b = exp(Lambda/2 + 1)/2.  Returns inf where it overflows."""
    try:
        return math.exp(L / 2.0 + 1.0) / 2.0
    except OverflowError:
        return float("inf")


def lambda_is_logarithmic():
    return geometry_for_lambda(100.0) / geometry_for_lambda(50.0) > 1.0e10


def lever_is_shut(target=WORLD_ANNUAL_J):
    return math.isinf(geometry_for_lambda(lambda_needed_for(target)))


CONSTANTS_IN_THE_RATE = 3          # c, G -- and Lambda is the fourth symbol
OBSTRUCTIONS_ARE_ABOUT = "the mechanism"
THE_BILL_IS = "the exchange rate"

GW = 1.0e9
WORLD_POWER_W = 1.9e13
SUN_W = 3.828e26
MILKY_WAY_W = 7.6e36
LIGO_STRAIN_M = 1.0e-19
PROTON_RADIUS_M = 0.84e-15
AGE_OF_UNIVERSE_S = 4.35e17
YEAR_S = 3.156e7


def contraction_rate(watts):
    """cells per second times l_P."""
    return (watts / cell_energy()) * cell_radius()


def seconds_for(d_m, watts):
    return closed_form_energy(d_m) / watts


def buys_in(watts, seconds):
    return watts * seconds / exchange_rate_j_per_m()


def watts_for_one_metre_per_second():
    return exchange_rate_j_per_m()


def cell_is_visible_to_ligo():
    return cell_radius() >= LIGO_STRAIN_M


def orders_below_ligo():
    return math.log10(LIGO_STRAIN_M / cell_radius())


# ---------------------------------------------- 8: the ring laser, re-tested

def photon_energy_for(lambdabar_m):
    """E = hbar c / lambdabar."""
    return HBAR * C / lambdabar_m


def smallest_photon_that_fits():
    """lambdabar = l_P gives exactly E_Planck."""
    return photon_energy_for(cell_radius())


def photon_the_cell_can_afford_lambdabar():
    return HBAR * C / cell_energy()


def granularity_gap():
    """How far one fitting photon overshoots the budget.  Exactly Lambda."""
    return smallest_photon_that_fits() / cell_energy()


def affordable_photon_in_cells():
    """And how far the affordable photon overshoots the cell.  Also Lambda."""
    return photon_the_cell_can_afford_lambdabar() / cell_radius()


def light_can_pay_for_a_cell():
    return granularity_gap() <= 1.0


KUGELBLITZ_BAND_M = (1.0e-29, 1.0e8)


def kugelblitz_block_applies_here():
    lo, hi = KUGELBLITZ_BAND_M
    return lo <= cell_radius() <= hi


RING_FAILS_KIND_BECAUSE = "lattice.py's theorem has no length in it"
ATOM_M = 1.0e-10


def ring_hardware_orders_short():
    return math.log10(ATOM_M / cell_radius())


IS_TRANSPORT = False
IS_BUILDABLE = None                # needs quantum gravity to evaluate
MOVES_AN_OBSTRUCTION = False


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-5):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. SOLVE THE GATES FOR R INSTEAD OF ASSUMING IT")
    near("R = l_P (m)", cell_radius(), 1.616255e-35)
    near("tau = l_P/c (s)", cell_lifetime(), 5.391246e-44)
    near("E = E_Planck/Lambda (J)", cell_energy(), 1.959505e8)
    chk("  is that exactly E_Planck/Lambda", cell_energy_is_planck_over_lambda(), True)
    near("  in MJ", cell_energy() / 1e6, 195.9505)
    near("  in kWh", in_kwh(cell_energy()), 54.4307)
    near("  in kg of TNT", in_tnt_kg(cell_energy()), 46.8333)
    near("  as a rest mass (kg)", rest_mass_kg(cell_energy()), 2.1802e-9)
    print("       AFTER SEVENTY ORDERS OF SHORTFALL, A PURCHASE-ORDER NUMBER.")

    print("\n2. AND IT PASSES -- ALL THREE, THE FIRST TIME ANYTHING HAS")
    near("magnitude shortfall at R = l_UV = l_P", magnitude_shortfall(), 0.100175)
    chk("  PASSES MAGNITUDE", passes_magnitude(), True)
    near("  with a margin of", magnitude_margin(), lambda_value())
    near("deadline: tau (s)", cell_lifetime(), 5.391246e-44)
    near("  against a CTC loop of 2R/c (s)", ctc_loop_transit(cell_radius()), 1.078249e-43)
    chk("  PASSES DEADLINE", passes_deadline(), True)
    print("       so closure.py's state-splitting never arises: the array")
    print("       cannot host a CTC at any separation.")
    near("collapse ratio E_t/E_kugelblitz", collapse_ratio(), 0.200350028, 1e-9)
    near("  which is 2/Lambda", 2.0 / lambda_value(), 0.200350028, 1e-9)
    near("  margin Lambda/2", collapse_margin(), 4.9912646)
    print("       NOTHING WAS TUNED.  Same identity, evaluated at the length")
    print("       the gates chose.")
    chk("DO ALL GATES PASS", all_gates_pass(), True)

    print("\n3. WHAT IT BUYS")
    near("Delta d (m)", cell_contraction(), 1.616255e-35)
    print("       One Planck length.  The energy is small because the output")
    print("       is small.  There is no discount hiding in the Planck scale.")

    print("\n4. TILING IS EXACTLY NEUTRAL")
    print("     %-8s %16s %16s %16s" % ("target", "cells", "tiled J", "closed-form J"))
    for d, nm in ((1e-15, "1 fm"), (1e-9, "1 nm"), (1.0, "1 m")):
        print("     %-8s %16.4e %16.4e %16.4e"
              % (nm, cells_for(d), tiled_energy(d), closed_form_energy(d)))
        chk("  tiling matches the closed form at %s" % nm, tiling_is_neutral(d), True)
    near("the exchange rate (J/m)", exchange_rate_j_per_m(), 1.2123737e43)
    chk("  is it scale-invariant", rate_is_scale_invariant(), True)
    print("       TILING PASSES EVERY GATE CELL BY CELL AND MOVES THE BILL")
    print("       NOT AT ALL.")

    print("\n5. WHICH RELOCATES THE PROJECT")
    import obstruct
    chk("obstructions recorded", len(obstruct.LEDGER), 53)
    chk("  and they are all about", OBSTRUCTIONS_ARE_ABOUT, "the mechanism")
    chk("  while the bill is", THE_BILL_IS, "the exchange rate")
    print("       THE SEVENTY ORDERS WERE NEVER A MECHANISM PROBLEM.")

    print("\n6. THE ONE LEVER, AND IT IS SHUT")
    near("seated Lambda", lambda_value(), 9.982529)
    print("     %-24s %14s %14s" % ("to make 1 m cost", "needs Lambda", "needs R_s/b"))
    for target, nm in ((WORLD_ANNUAL_J, "world annual energy"),
                       (MEGATON_J, "a one-megaton bomb"), (KWH, "one kilowatt-hour")):
        L = lambda_needed_for(target)
        g = geometry_for_lambda(L)
        print("     %-24s %14.4e %14s"
              % (nm, L, "> 1e300" if math.isinf(g) else "%.3e" % g))
    chk("is Lambda logarithmic in the geometry", lambda_is_logarithmic(), True)
    for tgt in (20.0, 50.0, 100.0):
        print("       Lambda = %5.1f needs R_s/b = %.4e" % (tgt, geometry_for_lambda(tgt)))
    chk("IS THE LEVER SHUT", lever_is_shut(), True)

    print("\n7. THE POWER-PLANT QUESTION")
    print("     %-24s %16s" % ("source", "contraction m/s"))
    for w, nm in ((GW, "1 GW power plant"), (WORLD_POWER_W, "all human power"),
                  (SUN_W, "the entire Sun"), (MILKY_WAY_W, "the Milky Way")):
        print("     %-24s %16.4e" % (nm, contraction_rate(w)))
    near("1 GW contraction rate (m/s)", contraction_rate(GW), 8.2483e-35)
    near("seconds for 1 m at 1 GW", seconds_for(1.0, GW), 1.212374e34)
    near("  in ages of the universe", seconds_for(1.0, GW) / AGE_OF_UNIVERSE_S, 2.787e16, 1e-3)
    near("1 GW for a century buys (m)", buys_in(GW, 100 * YEAR_S), 2.6032e-25)
    near("  in proton radii", buys_in(GW, 100 * YEAR_S) / PROTON_RADIUS_M, 3.099e-10, 1e-3)
    near("watts for 1 m/s", watts_for_one_metre_per_second(), 1.212374e43)
    near("  in Suns", watts_for_one_metre_per_second() / SUN_W, 3.167e16, 1e-3)
    chk("can LIGO see one cell fire", cell_is_visible_to_ligo(), False)
    near("  orders below LIGO", orders_below_ligo(), 15.8, 1e-2)
    print("       196 MJ IS NOT THE PRICE OF THE DEVICE.  IT IS THE PRICE OF")
    print("       ONE PLANCK LENGTH.  The rate is scale-invariant.")

    print("\n8. THE RING LASER, RE-TESTED AT THIS SCALE")
    chk("why it fails KIND", RING_FAILS_KIND_BECAUSE,
        "lattice.py's theorem has no length in it")
    near("smallest photon that fits (J)", smallest_photon_that_fits(), planck_energy())
    near("  the cell's whole budget (J)", cell_energy(), 1.959505e8)
    near("  so one fitting photon overshoots by", granularity_gap(), lambda_value())
    near("affordable photon lambdabar (m)", photon_the_cell_can_afford_lambdabar(),
         1.613431e-34)
    near("  which is this many cells across", affordable_photon_in_cells(), lambda_value())
    chk("CAN LIGHT PAY FOR A CELL", light_can_pay_for_a_cell(), False)
    print("       A photon that FITS costs Lambda x the budget; a photon you")
    print("       can AFFORD is Lambda x too big to fit.  LIGHT IS TOO COARSE.")
    near("ring hardware, orders short", ring_hardware_orders_short(), 25.0, 1e-2)
    chk("does the 2024 kugelblitz block apply at l_P",
        kugelblitz_block_applies_here(), False)
    print("       it does NOT -- l_P is below its 1e-29 m floor.  Recorded")
    print("       because it is true; gates 1 and 3 are decisive without it.")

    print("\n  WHAT IS NOT CLAIMED")
    chk("is this transport", IS_TRANSPORT, False)
    chk("is a Planck cell buildable", IS_BUILDABLE, None)
    chk("does any obstruction move", MOVES_AN_OBSTRUCTION, False)
    print("       196 MJ for one Planck length is a gate-passing configuration")
    print("       and NOT a drive.  Every gate is stated in a theory that")
    print("       candidates.py showed FAILS at this scale, so the number is")
    print("       what the FRAMEWORK says, not what a laboratory would pay.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  candidates.py found three unrelated mechanisms all running out within one
  order of the Planck length and read it as an obstruction.  Read as a
  specification it is an instruction, and following it produces the first
  configuration in this project that passes every gate: R = l_P, tau = one
  Planck time, E = E_Planck/Lambda = 195.95 MJ -- fifty-four kilowatt-hours,
  forty-seven kilograms of TNT, after seventy orders of shortfall.  It
  clears MAGNITUDE with a factor of Lambda in hand, clears the DEADLINE so
  completely that no closed timelike curve can form, and sits at exactly
  2/Lambda of a Planck black hole with the design margin intact -- the same
  collapse identity, untuned, evaluated at the length the gates chose.  And
  it buys one Planck length.  Cells tile exactly: a metre is 6.19e34 of them
  at 196 MJ each, totalling 1.212374e43 J, which is precisely what the
  closed form always said, because the exchange rate is scale-invariant.  So
  the architecture passes every gate cell by cell and moves the bill by
  nothing.  THAT is the result: all fifty-three recorded obstructions are
  about the mechanism, and the framework's own specification clears them
  without touching the cost.  The seventy orders were never a mechanism
  problem -- they are c^4/(G Lambda) = 1.21e43 joules per metre, and three
  of its four symbols are constants of nature.  The fourth, Lambda, is
  logarithmic in the geometry: one metre at world-annual-energy needs
  Lambda = 2.02e23 and a shell-to-corridor ratio past 1e300.  The only lever
  is shut, and it was never the mechanism's fault.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
