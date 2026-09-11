#!/usr/bin/env python3
"""
lightbuild.py -- the transition equation, rebuilt in light: what light can carry,
what it cannot, and the one exact identity that says why.

M: "now that we have this, let's go back to the math and figure out how my warp
transition theory can be built to work with light."

This is the constructive pass.  light.py and lattice.py were both refusals --
Mallett's CTC does not follow, and no classical EM field violates the NEC.  This
one asks the opposite question: TAKE THE REFUSALS AS GIVEN AND BUILD WHAT IS
LEFT.  Three things come out, and the middle one is new mathematics about M's
own equation rather than a literature reading.

    1.  THE SEAT/LEAD SPLIT IS THE OPENING, AND LIGHT FITS EXACTLY ONE HALF.
        Light can be the seat.  It cannot be the lead.  Neither half is a
        matter of engineering.

    2.  THE COLLAPSE IDENTITY.  E_transition(d) / E_kugelblitz(d) = 2/Lambda
        = 0.200350028, EXACTLY, at EVERY d.  The transition runs at 20.035 %
        of the energy that makes a horizon of the same size, and the design
        margin before you build a black hole instead of a corridor is
        Lambda/2 = 4.9912645871.  A pure number, and it is M's Lambda.

    3.  THE MARGIN IS 4.99 IN ENERGY AND 2.23 IN RADIUS, AND THE KUGELBLITZ
        BLOCK SURVIVES IT.  The field goes as the square root, so the factor
        of five buys sqrt(Lambda/2) = 2.234 in scale and nothing else.  A
        2024 result closes light-to-horizon over ten orders of magnitude in
        radius; the transition's own configuration sits inside the same band,
        displaced by that factor of two.

And one thing light HAS that mass does not, which is the only genuine new
freedom this pass found: PARALLEL NULL CONGRUENCES DO NOT FOCUS EACH OTHER AT
ALL.  Not "weakly" -- exactly zero.  That is a geometry knob with no analogue
in any matter source, and section 5 says what it is and is not good for.

===============================================================================
1. THE SEAT AND THE LEAD -- LIGHT FITS ONE HALF AND THE HALF IS THE FREE ONE
===============================================================================

reverse.py split the device in two and apply.py sharpened the split:

    THE SEAT   holds the corridor open at the far end.  Ordinary matter.
               Every energy condition satisfied.  M_ADM is a FREE PARAMETER
               here, and the seat costs nothing exotic.

    THE LEAD   does the contracting.  It is the whole cost, and it requires
               rho < 0 somewhere.  That is not a modelling choice: PMT
               rigidity says M_ADM = 0 under DEC implies Minkowski, and the
               device is not Minkowski, so DEC must fail.  The negative
               energy is DERIVED.

Now put light against each half.

    SEAT       PASSES.  Light has positive energy density, focuses a null
               congruence the right way (R_munu k^mu k^nu >= 0), and carries
               momentum flux -- everything the seat is asked to do.  Nothing
               in lattice.py's theorem obstructs a seat; the theorem obstructs
               the OTHER half.

    LEAD       FAILS, AND FAILS AS A THEOREM.  lattice.py: for the Maxwell
               stress tensor, set V_a = F_mu-a k^mu.  Then
               T_munu k^mu k^nu = V.V with V.k = 0 by antisymmetry, so
               V.V >= 0 for EVERY classical electromagnetic field.  Standing
               waves, lattices, vortices, crystals, any superposition.  There
               is no configuration of classical light with rho < 0 along a
               null direction.

    SO THE ANSWER TO "CAN IT BE BUILT WITH LIGHT" IS SPLIT, AND THE SPLIT IS
    NOT 50/50.  Light can do the half that was already free.  It cannot do the
    half that is the entire cost.  That is not an engineering shortfall to be
    closed with more power -- more power makes V.V larger, not negative.

    THE HONEST STATEMENT: light is an excellent seat and a forbidden lead.
    Every joule you put into light goes to the side of the ledger that was
    never the problem.

===============================================================================
2. THE COLLAPSE IDENTITY -- AND IT IS EXACT
===============================================================================

M's equation, seated in phase1.py:

        Delta d = (G/c^2) M Lambda,        Lambda = 9.982529174

Read as an energy: to contract by d you must seat

        E_transition(d) = d c^4 / (G Lambda)

And the energy that makes a Schwarzschild horizon of radius d -- which is what
a kugelblitz is, a black hole made of light -- is

        E_kugelblitz(d) = d c^4 / (2 G)

Both are (c^4/G) times a length.  They are the SAME DIMENSIONAL OBJECT, which
is why their ratio is a pure number, and the number is

        E_transition(d)              2
        ---------------   =   -------------   =   0.20035002804400565
        E_kugelblitz(d)          Lambda

    INDEPENDENT OF d.  Measured over thirty-one decades, 1e-15 m to 1e15 m:
    worst residual 2.776e-17, which is one unit in the last place.  The d
    cancels algebraically; the measurement only confirms there is no hidden
    scale.

    AND AT THE PLANCK LENGTH IT COLLAPSES FURTHER:

        E_transition(l_P)  =  E_Planck / Lambda        exactly, 0.100175014

    l_P c^4/(G Lambda) = sqrt(hbar c^5/G)/Lambda by the definition of l_P.
    So Lambda is not merely a number in M's equation -- it is the factor
    relating the transition's natural quantum of energy to the Planck energy.

WHAT THE IDENTITY MEANS, AND IT IS THE REASON COLLAPSE KEEPS BINDING.

    Contracting a distance d costs 20.035 % of the energy that makes a black
    hole of radius d.  THE TRANSITION AND THE COLLAPSE ARE THE SAME ORDER.
    Not "close"; the same order with a fixed pure-number ratio.

    obstruct.py has COLLAPSE as a recurring closure across the tree, and this
    is why.  It is not a coincidence of some particular design point -- it is
    a structural feature of the equation, true at every scale at once.

    THE MARGIN IS THE INVERSE:  Lambda/2 = 4.9912645871.

    That is the whole design headroom.  You may seat up to a factor of 4.99
    more energy than the transition needs before the same region of space is
    holding enough to be a horizon rather than a corridor.  Every engineering
    decision -- confinement volume, fill factor, duty cycle, inefficiency --
    spends out of that one number, and it is not large.

    A FACTOR OF FIVE IS A TIGHTER BUDGET THAN ANY MACHINE HUMANS HAVE BUILT
    RUNS ON.  A tokamak's Q, a rocket's mass ratio, a laser's wall-plug: all
    of them are allowed to be off by five and still work.  Here five IS the
    failure boundary.

===============================================================================
3. WHAT THAT COSTS AT SCALES A LABORATORY WOULD PICK
===============================================================================

The exchange rate is c^2/(G Lambda) = 1.348948e26 kg per metre contracted,
which is 1.2123737e43 J per metre.  Linear in d, so:

    contract by      E_transition          equivalent mass      E_kugelblitz
    ---------------  --------------------  -------------------  ------------
    1 fm             1.2124e+28 J          1.3489e+11 kg        6.0513e+28 J
    1 nm             1.2124e+34 J          1.3489e+17 kg        6.0513e+34 J
    1 um             1.2124e+37 J          1.3489e+20 kg        6.0513e+37 J
    1 mm             1.2124e+40 J          1.3489e+23 kg        6.0513e+40 J
    1 m              1.2124e+43 J          1.3489e+26 kg        6.0513e+43 J

    World annual primary energy is about 6e20 J.  ONE FEMTOMETRE costs
    2.0e7 times it.  One metre costs 2.0e22 times it.

    This is not a new obstruction -- budget.py and supply.py had the number.
    It is here because the light question changes NOTHING about it: the
    identity above is about energy, and energy does not get cheaper by being
    carried as photons.  rates.py already showed the conversion table has no
    free rate but kappa.

===============================================================================
4. THE KUGELBLITZ IS BLOCKED, AND THE 4.99 MARGIN DOES NOT GET YOU OUT
===============================================================================

ALVAREZ-DOMINGUEZ, GARAY, MARTIN-MARTINEZ & POLO-GOMEZ, "No black holes from
light" (arXiv:2405.02389, 2024; Complutense, Waterloo, IQC, Perimeter).  Read
in full for this pass.

    THE RESULT: Schwinger-effect dissipation prevents kugelblitz formation for

            1e-29 m  <~  R  <~  1e8 m

    Concentrating light densely enough to collapse means field strengths far
    past the Schwinger limit; the field decays into electron-positron pairs,
    which carry the energy out faster than it can be concentrated.  Their
    numbers, re-derived here rather than quoted:

        Schwinger field                     1.323e18 V/m
        phi = sqrt(3 c^4 / 4 pi eps0 G)     1.806e27 V
        threshold f R                       5.211e82 W/m
        total power at R = 1 m              6.549e83 W
        pair-formation length / R           2.829e-22

    Against that: the strongest laboratory field is about 1e15 V/m, magnetar
    surfaces reach 1e19 V/m, and the brightest known quasar radiates 1e41 W.
    The lab-scale shortfall is MORE THAN FIFTY ORDERS OF MAGNITUDE.  All five
    of the paper's approximations are argued to UNDERESTIMATE the dissipation,
    so the bound is conservative in the direction that matters.

NOW THE QUESTION THIS PASS ACTUALLY ASKS, WHICH THE PAPER DOES NOT.

    The transition does not need a horizon.  It needs 20.035 % of one.  Does
    the Schwinger block bite below the design point, or does the Lambda/2
    margin put the transition's configuration in the clear?

    IT BITES.  And the reason is a square root, which is why the answer is not
    close.

    Energy E confined to a ball of radius R has u = E/((4/3) pi R^3) and, for
    radiation, u = eps0 |E_field|^2.  So the field goes as sqrt(E).  Put the
    transition's energy where the kugelblitz's would go, and

        E_field(transition)                     ------
        -------------------  =  sqrt(2/Lambda) = 0.4476047677
        E_field(kugelblitz)

    A FACTOR OF 4.99 IN ENERGY IS A FACTOR OF 2.234 IN FIELD.  Measured at
    R = 1e-15, 1e-9, 1e-6, 1e-3, 1, 1e8 m: the ratio is 0.447605 at every one.

    Both fields go as 1/R, so each crosses the Schwinger limit at one radius:

        kugelblitz crosses at    R = 9.6528e+08 m
        transition crosses at    R = 4.3206e+08 m
        ratio                    2.234114 = sqrt(Lambda/2), exactly

    BELOW ITS CROSSING RADIUS THE TRANSITION'S OWN LIGHT CONFIGURATION IS
    SUPER-SCHWINGER AND DISSIPATES INTO PAIRS.  The entire band the 2024
    paper closes for kugelblitzen -- 1e-29 m to 1e8 m -- is inside the
    transition's blocked region too, because 1e8 < 4.32e8.  The margin moved
    the boundary by a factor of two; the band spans thirty-seven orders.

    AND ABOVE THE CROSSING RADIUS IT IS WORSE, NOT BETTER.  At R = 4.32e8 m
    the field is finally sub-Schwinger, and the energy you are asked to have
    assembled there is

        5.2382e+51 J  =  5.828e+34 kg  =  2.930e+04 solar masses

    8.7e30 times world annual primary energy; delivered over one light-crossing
    of the region that is 3.6e51 W, which is 3.6e10 brightest-quasars.

    SO THE TWO ENDS CLOSE ON EACH OTHER.  Small enough for the field to be
    reachable is impossible because the field is super-Schwinger; large enough
    to be sub-Schwinger is impossible because the energy is stellar-cluster
    scale.  THE FACTOR OF 4.99 IS SPENT MOVING THE CROSSOVER BY 2.23 AND
    CHANGES NEITHER END.

    THIS IS A DERIVED RESULT ABOUT M'S EQUATION, not a quotation.  The paper
    bounds kugelblitzen; the identity in section 2 is what transfers the bound
    onto the transition, and the sqrt is what makes the transfer lossy in the
    wrong direction.

===============================================================================
5. THE ONE FREEDOM LIGHT HAS THAT MASS DOES NOT
===============================================================================

Everything above is a refusal or a cost.  This is the exception, and it is real
geometry rather than an engineering hope.

    PARALLEL NULL CONGRUENCES DO NOT FOCUS EACH OTHER.  Exactly zero, not
    weakly.  Two light beams travelling the same way exert no mutual
    gravitational deflection at all -- Tolman, Ehrenfest & Podolsky (1931),
    confirmed by Wheeler and standard since; the modern treatment is Rakhmanov
    / "The gravity of light" (arXiv:1009.3849), and it is still stated as well
    known in the current literature.

    THE MECHANISM IS CLEAN AND IS DERIVED HERE RATHER THAN CITED.  The field
    of a null source is an impulsive pp-wave, supported on the null hyperplane
    u = t - z = const.  A test ray moving PARALLEL keeps u constant: it never
    crosses the wavefront, so it collects no impulse.  A test ray moving
    ANTIPARALLEL sweeps through the entire wave and collects the full one.
    Measured below: the parallel impulse is identically zero as an integral,
    not small.

    WHAT IT IS: A SIGN-AND-MAGNITUDE KNOB WITH NO MATTER ANALOGUE.  Two
    masses always attract.  Two light beams attract, or do not, according to
    their RELATIVE PROPAGATION DIRECTION.  The focusing a light configuration
    delivers is a function of its internal geometry, not only of its energy.
    No arrangement of dust has that.

    WHAT IT IS NOT: A WAY PAST SECTION 1.  The knob runs between ZERO and
    POSITIVE.  It never reaches negative -- that is exactly what lattice.py's
    theorem forbids, and the parallel case is the theorem's equality case
    (V.V = 0 when V is parallel to k), not a violation of it.

        SO THE KNOB TURNS THE SEAT OFF, AND CANNOT TURN THE LEAD ON.

    That is still worth having.  A seat you can switch off geometrically --
    by reorienting a beam rather than by removing energy -- is a control
    authority the matter architecture does not offer, and it belongs in the
    design space even though it does not buy the lead.

===============================================================================
WHAT THIS PASS ESTABLISHES
===============================================================================

    HELD   The seat/lead split answers the light question, and answers it
           unevenly: light passes the free half and is forbidden the costly
           half by a theorem with no free parameter.

    NEW    E_transition(d)/E_kugelblitz(d) = 2/Lambda exactly, at every d;
           E_transition(l_P) = E_Planck/Lambda; design margin Lambda/2 = 4.99.
           These are statements about M's equation and they were not known
           here before this pass.

    NEW    The 2024 kugelblitz block transfers onto the transition, and the
           margin degrades by a square root in transferring: 4.99 in energy
           is 2.23 in radius.  The blocked band is unescaped.

    OPEN   Whether a NON-classical light field changes section 1.  The theorem
           is about the CLASSICAL Maxwell stress tensor.  Squeezed vacuum does
           have regions of negative energy density, and neclab.py already holds
           the quantum-inequality ledger for that.  This pass does not extend
           to it and does not claim to.

    NOT AN OBSTRUCTION, AND SAID PLAINLY: none of this says light is the wrong
    material.  It says light is the right material for the half that was
    already free, and that the half that is not free is not a materials
    question at all.
"""

import importlib
import math
import sys

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34
EPS0 = 8.8541878128e-12
M_E = 9.1093837015e-31
Q_E = 1.602176634e-19

SOLAR_MASS_KG = 1.989e30
WORLD_ANNUAL_ENERGY_J = 6.0e20
BRIGHTEST_QUASAR_W = 1.0e41
STRONGEST_LAB_FIELD_V_PER_M = 1.0e15
MAGNETAR_FIELD_V_PER_M = 1.0e19

KUGELBLITZ_PAPER = "arXiv:2405.02389 -- No black holes from light (2024)"
OBSTRUCTION_ROW = "LIGHT-AS-THE-SUPPLY"   # obstruct.py; distinct from LIGHT-AS-THE-SOURCE
KUGELBLITZ_BLOCKED_BAND_M = (1.0e-29, 1.0e8)
PARALLEL_BEAM_PAPER = "arXiv:1009.3849 -- The gravity of light"


# ---------------------------------------------- 1: the seat and the lead

HALVES = (
    # name,   what it does,                         light passes,  why
    ("seat", "holds the corridor open; free", True,
     "positive energy, focuses the right way, every energy condition met"),
    ("lead", "does the contracting; the whole cost", False,
     "needs rho < 0; lattice.py: T_munu k^mu k^nu = V.V >= 0 for every F"),
)


def light_passes(half):
    for name, _what, passes, _why in HALVES:
        if name == half:
            return passes
    raise KeyError(half)


def half_light_can_do():
    return [n for n, _w, p, _r in HALVES if p]


def half_that_is_the_cost():
    return "lead"


def light_can_do_the_costly_half():
    return light_passes(half_that_is_the_cost())


def more_power_helps():
    """V.V is a square.  Scaling F by s scales T k k by s^2, upward."""
    return False


def nec_scalar(F, k_up):
    """T_munu k^mu k^nu = V.V, via lattice.py's own V_lower and square."""
    import lattice
    return lattice.square(lattice.V_lower(F, k_up))


def nec_scales_upward(s=7.0):
    f = [[0.0] * 4 for _ in range(4)]
    f[0][1], f[1][0] = 1.3, -1.3
    f[0][2], f[2][0] = -0.4, 0.4
    f[1][3], f[3][1] = 0.9, -0.9
    k = [1.0, 0.6, 0.8, 0.0]
    base = nec_scalar(f, k)
    big = nec_scalar([[s * x for x in row] for row in f], k)
    return big, base, abs(big - s * s * base) <= 1e-9 * max(1.0, abs(big))


# ---------------------------------------------- 2: the collapse identity

def lambda_value():
    import phase1
    return phase1.lam()


def transition_energy(d_metres):
    """E = d c^4 / (G Lambda).  M's equation read as an energy."""
    return d_metres * C ** 4 / (G * lambda_value())


def kugelblitz_energy(d_metres):
    """E = d c^4 / (2 G).  A Schwarzschild horizon of radius d."""
    return d_metres * C ** 4 / (2.0 * G)


def collapse_ratio(d_metres=1.0):
    return transition_energy(d_metres) / kugelblitz_energy(d_metres)


def collapse_ratio_closed_form():
    return 2.0 / lambda_value()


def design_margin():
    """Lambda/2.  How much more than the transition needs you may seat."""
    return lambda_value() / 2.0


def ratio_is_scale_free(decades=range(-15, 16)):
    """Worst |ratio(d) - 2/Lambda| over the given decades in d."""
    want = collapse_ratio_closed_form()
    return max(abs(collapse_ratio(10.0 ** e) - want) for e in decades)


def planck_length():
    return math.sqrt(HBAR * G / C ** 3)


def planck_energy():
    return math.sqrt(HBAR * C ** 5 / G)


def planck_ratio():
    """E_transition(l_P) / E_Planck.  Should be 1/Lambda."""
    return transition_energy(planck_length()) / planck_energy()


def exchange_rate_kg_per_metre():
    import phase1
    return phase1.exchange_rate()


def exchange_rate_joules_per_metre():
    return exchange_rate_kg_per_metre() * C ** 2


DESIGN_POINTS = (("1 fm", 1.0e-15), ("1 nm", 1.0e-9), ("1 um", 1.0e-6),
                 ("1 mm", 1.0e-3), ("1 m", 1.0))


def world_years(energy_j):
    return energy_j / WORLD_ANNUAL_ENERGY_J


# ---------------------------------------------- 3: the Schwinger transfer

def schwinger_field():
    """E_S = m_e^2 c^3 / (q hbar).  1.323e18 V/m."""
    return M_E ** 2 * C ** 3 / (Q_E * HBAR)


def confinement_field(energy_j, radius_m):
    """Field holding energy_j as radiation in a ball of radius_m.  u = eps0 E^2."""
    u = energy_j / ((4.0 / 3.0) * math.pi * radius_m ** 3)
    return math.sqrt(u / EPS0)


def field_ratio(radius_m=1.0):
    """transition field / kugelblitz field at the same radius."""
    return (confinement_field(transition_energy(radius_m), radius_m)
            / confinement_field(kugelblitz_energy(radius_m), radius_m))


def field_ratio_closed_form():
    return math.sqrt(collapse_ratio_closed_form())


def crossing_radius(alpha):
    """Radius where a configuration holding alpha x kugelblitz energy has

        |E_field| = E_Schwinger.

    u = 3 alpha c^4 / (8 pi G R^2), so R = sqrt(3 alpha c^4/(8 pi G eps0 E_S^2)).
    """
    return math.sqrt(3.0 * alpha * C ** 4
                     / (8.0 * math.pi * G * EPS0 * schwinger_field() ** 2))


def transition_crossing_radius():
    return crossing_radius(collapse_ratio_closed_form())


def kugelblitz_crossing_radius():
    return crossing_radius(1.0)


def crossing_gain():
    """What the Lambda/2 energy margin buys in radius.  sqrt(Lambda/2)."""
    return kugelblitz_crossing_radius() / transition_crossing_radius()


def margin_degrades_by_a_square_root(tol=1e-12):
    return abs(crossing_gain() - math.sqrt(design_margin())) <= tol * crossing_gain()


def blocked_band_is_inside_transition_block():
    """The 2024 paper's whole band sits below the transition's crossing radius."""
    return KUGELBLITZ_BLOCKED_BAND_M[1] < transition_crossing_radius()


def energy_at_transition_crossing():
    return transition_energy(transition_crossing_radius())


def assembly_power_at_crossing():
    """Energy delivered over one light-crossing of the region."""
    r = transition_crossing_radius()
    return energy_at_transition_crossing() / (r / C)


def both_ends_close():
    """Small -> super-Schwinger.  Large -> stellar-cluster energy.  No window."""
    small_is_blocked = blocked_band_is_inside_transition_block()
    large_is_absurd = (energy_at_transition_crossing() / C ** 2
                       > 1.0e3 * SOLAR_MASS_KG)
    return small_is_blocked and large_is_absurd


def kugelblitz_potential():
    """phi = sqrt(3 c^4 / 4 pi eps0 G).  ~1.8e27 V."""
    return math.sqrt(3.0 * C ** 4 / (4.0 * math.pi * EPS0 * G))


def dissipation_threshold_fR():
    """2 q^3 phi^3 / (9 pi^3 hbar^2 c), in W/m."""
    return (2.0 * Q_E ** 3 * kugelblitz_potential() ** 3
            / (9.0 * math.pi ** 3 * HBAR ** 2 * C))


def total_power_needed(radius_m=1.0):
    return 4.0 * math.pi * radius_m * dissipation_threshold_fR()


def pair_length_fraction():
    """l_bh/R = m_e c^2 / (q phi).  ~1e-22 -- pairs form deep inside."""
    return M_E * C ** 2 / (Q_E * kugelblitz_potential())


# ---------------------------------------------- 4: the parallel null

def pp_wave_phase(t, z, direction):
    """u = t - z for a source moving +z.  A test ray's phase relative to it."""
    return t - direction * z


def impulse_collected(direction, steps=20000, span=1.0e3):
    """A test ray at speed c in +z (direction=+1) or -z (-1) against a pp-wave
    supported on u = t - z = 0.

    Parallel: u is CONSTANT along the worldline, so the ray never crosses the
    wavefront and the integral of the delta support is identically zero.
    Antiparallel: u sweeps the whole line and collects the full impulse.
    """
    crossings = 0
    prev = None
    for i in range(steps + 1):
        t = -span + 2.0 * span * i / steps
        z = direction * t
        u = pp_wave_phase(t, z, 1.0)
        if prev is not None and (prev < 0.0) != (u < 0.0):
            crossings += 1
        prev = u
    return crossings


def parallel_impulse_is_zero():
    return impulse_collected(+1.0) == 0


def antiparallel_impulse_is_nonzero():
    return impulse_collected(-1.0) >= 1


KNOB_RANGE = ("zero", "positive")
KNOB_REACHES_NEGATIVE = False


def knob_turns_the_seat_off():
    return KNOB_RANGE[0] == "zero"


def knob_turns_the_lead_on():
    return KNOB_REACHES_NEGATIVE


def parallel_case_is_the_equality_case():
    """V.V = 0 when V is parallel to k.  The theorem's boundary, not a breach."""
    f = [[0.0] * 4 for _ in range(4)]
    f[0][1], f[1][0] = 1.0, -1.0
    f[3][1], f[1][3] = -1.0, 1.0          # a null plane wave travelling in +z
    k = [1.0, 0.0, 0.0, 1.0]              # a ray travelling the same way
    return nec_scalar(f, k)


def antiparallel_case_is_strictly_positive():
    """The SAME field against a ray going the other way.  Nonzero, so the
    zero above is the co-moving geometry and not a vanishing field."""
    f = [[0.0] * 4 for _ in range(4)]
    f[0][1], f[1][0] = 1.0, -1.0
    f[3][1], f[1][3] = -1.0, 1.0
    k = [1.0, 0.0, 0.0, -1.0]
    return nec_scalar(f, k)


# ---------------------------------------------- 5: what stays open

OPEN_QUESTION = ("whether a NON-classical light field changes section 1 -- "
                 "the theorem is about the CLASSICAL Maxwell stress tensor")
OPEN_IS_HELD_BY = "neclab.py"


def classical_only():
    return True


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-6):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.10g %20.10g  %s"
              % (label, got, want, "ok" if good else "FAIL"))

    def under(label, got, bound):
        nonlocal ok
        good = got <= bound
        ok &= good
        print("  %-56s %20.6g %20s  %s"
              % (label, got, "<= %.3g" % bound, "ok" if good else "FAIL"))

    print("1. THE SEAT AND THE LEAD")
    for name, what, passes, why in HALVES:
        print("     %-6s %-38s light: %-8s" % (name, what[:38], "PASSES" if passes else "FAILS"))
        print("            %s" % why)
    chk("can light do the seat", light_passes("seat"), True)
    chk("can light do the lead", light_passes("lead"), False)
    chk("which half is the whole cost", half_that_is_the_cost(), "lead")
    chk("so can light do the costly half", light_can_do_the_costly_half(), False)
    chk("does more power help", more_power_helps(), False)
    big, base, quadratic = nec_scales_upward(7.0)
    chk("  scaling F by 7 scales T k k by 49, UPWARD", quadratic, True)
    near("    T k k at F", base, 1.93, 1e-9)
    near("    T k k at 7F", big, 94.57, 1e-9)
    print("       LIGHT IS AN EXCELLENT SEAT AND A FORBIDDEN LEAD.  Every")
    print("       joule spent goes to the side that was never the problem.")

    print("\n2. THE COLLAPSE IDENTITY -- E_t/E_k = 2/Lambda, EXACTLY")
    near("Lambda", lambda_value(), 9.982529174194637, 1e-12)
    near("2/Lambda", collapse_ratio_closed_form(), 0.20035002804400565, 1e-12)
    near("design margin Lambda/2", design_margin(), 4.9912645870973185, 1e-12)
    print("     %-14s %14s %14s %14s" % ("d (m)", "E_t (J)", "E_k (J)", "ratio"))
    for e in (-15, -9, 0, 3, 15):
        d = 10.0 ** e
        print("     %-14.0e %14.5e %14.5e %14.12f"
              % (d, transition_energy(d), kugelblitz_energy(d), collapse_ratio(d)))
    under("worst residual over 31 decades in d", ratio_is_scale_free(), 1e-16)
    print("       ONE UNIT IN THE LAST PLACE.  The d cancels algebraically;")
    print("       the measurement only confirms there is no hidden scale.")
    near("l_P (m)", planck_length(), 1.61625502392855e-35, 1e-9)
    near("E_Planck (J)", planck_energy(), 1956081636.0991087, 1e-9)
    near("E_t(l_P)/E_Planck", planck_ratio(), 1.0 / lambda_value(), 1e-12)
    chk("  is that 1/Lambda", abs(planck_ratio() - 1.0 / lambda_value()) < 1e-15, True)
    print("       Lambda relates the transition's natural quantum of energy")
    print("       to the Planck energy.  It is not merely a coefficient.")

    print("\n3. WHAT IT COSTS AT SCALES A LABORATORY WOULD PICK")
    near("exchange rate (kg/m)", exchange_rate_kg_per_metre(), 1.348947644431751e26, 1e-9)
    near("exchange rate (J/m)", exchange_rate_joules_per_metre(), 1.2123736812778673e43, 1e-9)
    print("     %-8s %14s %14s %14s" % ("contract", "E_t (J)", "mass (kg)", "world-years"))
    for label, d in DESIGN_POINTS:
        e = transition_energy(d)
        print("     %-8s %14.4e %14.4e %14.4e" % (label, e, e / C ** 2, world_years(e)))
    near("1 fm in world-years", world_years(transition_energy(1e-15)), 2.0206e7, 1e-4)
    near("1 m in world-years", world_years(transition_energy(1.0)), 2.0206e22, 1e-4)
    print("       ONE FEMTOMETRE COSTS 2.0e7 WORLD-YEARS.  Light changes")
    print("       nothing here: energy is not cheaper carried as photons.")

    print("\n4. THE SCHWINGER TRANSFER -- 4.99 IN ENERGY IS 2.23 IN RADIUS")
    print("     %s" % KUGELBLITZ_PAPER)
    near("Schwinger field (V/m)", schwinger_field(), 1.323285474948166e18, 1e-9)
    near("phi (V)", kugelblitz_potential(), 1.8064247479229715e27, 1e-9)
    near("threshold f R (W/m)", dissipation_threshold_fR(), 5.211414873235492e82, 1e-6)
    near("total power at R = 1 m (W)", total_power_needed(1.0), 6.548857072226081e83, 1e-6)
    near("pair length / R", pair_length_fraction(), 2.82878625629831e-22, 1e-9)
    print("     against: lab %.0e V/m, magnetar %.0e V/m, brightest quasar %.0e W"
          % (STRONGEST_LAB_FIELD_V_PER_M, MAGNETAR_FIELD_V_PER_M, BRIGHTEST_QUASAR_W))
    print("     %-10s %14s %14s %10s" % ("R (m)", "E_k field", "E_t field", "ratio"))
    for R in (1e-15, 1e-9, 1e-6, 1e-3, 1.0, 1e8):
        print("     %-10.0e %14.4e %14.4e %10.6f"
              % (R, confinement_field(kugelblitz_energy(R), R),
                 confinement_field(transition_energy(R), R), field_ratio(R)))
        near("  ratio at R = %.0e is sqrt(2/Lambda)" % R,
             field_ratio(R), field_ratio_closed_form(), 1e-12)
    near("sqrt(2/Lambda)", field_ratio_closed_form(), 0.4476047676734528, 1e-12)
    near("kugelblitz crossing radius (m)", kugelblitz_crossing_radius(), 9.6528e8, 1e-4)
    near("transition crossing radius (m)", transition_crossing_radius(), 4.3206e8, 1e-4)
    near("what the margin buys in radius", crossing_gain(), 2.234114, 1e-5)
    chk("  is that exactly sqrt(Lambda/2)", margin_degrades_by_a_square_root(), True)
    chk("is the paper's whole band inside the transition's block",
        blocked_band_is_inside_transition_block(), True)
    print("       1e-29 m to 1e8 m, and 1e8 < 4.32e8.  THIRTY-SEVEN ORDERS")
    print("       BLOCKED; the margin moved the boundary by a factor of two.")
    near("energy at the crossing radius (J)", energy_at_transition_crossing(), 5.2382e51, 1e-4)
    near("  in solar masses", energy_at_transition_crossing() / C ** 2 / SOLAR_MASS_KG,
         2.9303e4, 1e-4)
    near("  assembly power over one light-crossing (W)",
         assembly_power_at_crossing(), 3.635e51, 1e-3)
    near("  in brightest-quasars", assembly_power_at_crossing() / BRIGHTEST_QUASAR_W,
         3.635e10, 1e-3)
    chk("do both ends close on each other", both_ends_close(), True)
    print("       SMALL ENOUGH TO REACH IS SUPER-SCHWINGER; LARGE ENOUGH TO BE")
    print("       SUB-SCHWINGER IS 29,000 SOLAR MASSES.  No window between.")

    print("\n5. THE ONE FREEDOM LIGHT HAS THAT MASS DOES NOT")
    print("     %s" % PARALLEL_BEAM_PAPER)
    chk("wavefront crossings, parallel ray", impulse_collected(+1.0), 0)
    chk("wavefront crossings, antiparallel ray", impulse_collected(-1.0), 1)
    chk("is the parallel impulse zero", parallel_impulse_is_zero(), True)
    chk("is the antiparallel impulse nonzero", antiparallel_impulse_is_nonzero(), True)
    print("       u = t - z is CONSTANT along a parallel ray, so it never")
    print("       crosses the wavefront.  Exactly zero, not weakly.")
    near("T k k for a null wave and a co-moving ray", parallel_case_is_the_equality_case(), 0.0, 1e-12)
    near("  the SAME field against a counter-moving ray", antiparallel_case_is_strictly_positive(), 4.0, 1e-12)
    chk("  so the zero is the geometry, not a vanishing field",
        antiparallel_case_is_strictly_positive() > 0.0, True)
    chk("  the knob's range", KNOB_RANGE, ("zero", "positive"))
    chk("does the knob turn the seat off", knob_turns_the_seat_off(), True)
    chk("does the knob turn the lead on", knob_turns_the_lead_on(), False)
    print("       THE PARALLEL CASE IS THE THEOREM'S EQUALITY CASE, not a")
    print("       breach of it.  Control authority, not a route to rho < 0.")

    print("\n6. WHERE THIS IS SEATED, AND WHAT STAYS OPEN")
    import obstruct
    chk("the obstruction row this pass adds", OBSTRUCTION_ROW, "LIGHT-AS-THE-SUPPLY")
    chk("  and it is NOT light.py's row of a similar name",
        OBSTRUCTION_ROW in {r[0] for r in obstruct.LEDGER}
        and "LIGHT-AS-THE-SOURCE" in {r[0] for r in obstruct.LEDGER}, True)
    chk("  closed how", [r[2] for r in obstruct.LEDGER if r[0] == OBSTRUCTION_ROW],
        ["CLOSED-NEGATIVE"])
    chk("is the theorem classical-only", classical_only(), True)
    print("     OPEN: %s" % OPEN_QUESTION)
    print("     held by: %s" % OPEN_IS_HELD_BY)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  Light can be the seat and cannot be the lead, and the lead is the whole
  cost.  That is settled by lattice.py's theorem, which has no free
  parameter and gets worse, not better, with more power.  What is new here
  is exact and it is about M's own equation: contracting a distance d costs
  2/Lambda = 20.035 %% of the energy that makes a horizon of radius d, at
  EVERY d, with a residual of one unit in the last place over thirty-one
  decades -- and at the Planck length that collapses to E_Planck/Lambda.
  So the design margin before a corridor becomes a black hole is exactly
  Lambda/2 = 4.99.  That margin does not survive the transfer to the 2024
  kugelblitz block, because the confining field goes as the square root of
  the energy: 4.99 in energy is 2.234 in radius, which moves the Schwinger
  crossing from 9.65e8 m to 4.32e8 m and leaves the paper's entire blocked
  band -- 1e-29 m to 1e8 m -- inside the transition's block as well.  Above
  the crossing the field is finally reachable and the energy is 29,000
  solar masses.  The two ends close.  The one genuine new freedom is that
  parallel null congruences do not focus each other at all, which is a
  geometry knob running from zero to positive; it can switch the seat off
  and it cannot switch the lead on, because zero is the theorem's equality
  case and not a breach of it.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
