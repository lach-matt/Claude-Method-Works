#!/usr/bin/env python3
"""
candidates.py -- the three proposed leads, run against the full spec.  All three
fail, they fail at DIFFERENT PLACES, and the way they fail is more informative
than the verdict.

M, after teardown.py named the new requirement: "I honestly cannot remember.  I
read it in passing.  We'll have to run all three candidates."

    So: negative effective mass, the Casimir effect, and squeezed vacuum, each
    against the three things the lead must now do.  Nothing is taken on the
    reputation of the idea; each is failed at a specific gate with a number.

===============================================================================
0. THE SPEC, WHICH NOW HAS THREE HALVES RATHER THAN ONE
===============================================================================

    KIND       supplies rho < 0.  Not "negative mass" in some effective sense --
               a genuinely negative energy density, because that is what
               PMT rigidity DERIVED and what lattice.py's theorem forbids to
               every classical EM field.

    DEADLINE   switches off in ~R/c.  teardown.py: the corridor's lifetime is
               max(tau_seat, tau_lead), so a lead that cannot be switched makes
               the corridor un-closable whatever the seat does, and closure.py
               says what an un-closable corridor costs.

    MAGNITUDE  enough of it.  The lead is the whole cost, so it must carry
               E_transition in a region of size R:

                   |rho_needed|  ~  c^4 / (G Lambda R^2)

    THE THIRD GATE IS NEW HERE.  Previous passes asked for the sign and, since
    teardown.py, the deadline.  Neither asked the quantum sources how much they
    can actually supply, and that is what decides all three.

===============================================================================
1. CANDIDATE A -- NEGATIVE EFFECTIVE MASS.  FAILS AT THE FIRST GATE.
===============================================================================

Negative-mass exciton polaritons are real, measured, and switchable: dissipative
light-matter coupling in an atomically thin semiconductor inverts the lower
polariton branch, and the propagation direction is opposite to the momentum
(arXiv:2204.04041, and Nature Communications).  Negative-mass effects are also
seen in spin-orbit-coupled BECs (arXiv:1801.04779).

    AND IT IS THE WRONG QUANTITY, WHICH NO AMOUNT OF ENGINEERING FIXES.

        effective mass    m* = hbar^2 / (d^2 E / dk^2)

    is a property of the DISPERSION RELATION -- the curvature of a band.  It is
    not T_00.  A quasiparticle with m* < 0 still carries POSITIVE energy; what
    is inverted is how its group velocity responds to momentum.

    SO IT VIOLATES NO ENERGY CONDITION AT ALL.  lattice.py's theorem does not
    even engage with it, because there is nothing there to engage: the
    gravitational source is the full stress-energy of the cavity, the excitons
    and the field, and that is positive.

        A NEGATIVE-MASS POLARITON WOULD NOT BEND SPACETIME THE WRONG WAY.  It
        is a band-structure effect in a medium, and the medium weighs what it
        weighs.

    FAILS: KIND.  Passes the deadline trivially, and the magnitude gate is never
    reached because there is no rho < 0 to measure.  Recorded because it is the
    candidate most likely to be mistaken for a lead -- "negative mass" is the
    same phrase for two different things, and only one of them is exotic.

===============================================================================
2. CANDIDATE B -- THE CASIMIR EFFECT.  PASSES KIND, FAILS THE OTHER TWO.
===============================================================================

Genuine negative energy density between ideal plates, and measured in the
laboratory:

        rho_Casimir  =  - pi^2 hbar c / (720 d^4)

    KIND: PASSES.  This is a real rho < 0, not an effective one.

    DEADLINE: FAILS.  Switching it off means MOVING THE PLATES, which is
    mechanical and therefore slower than c -- by a lot.  There is no
    configuration of matter that clears itself at c, which is teardown.py's
    whole point.  The negative region is also anchored to the plates, whose own
    mass-energy is hugely positive and does not go anywhere.

    MAGNITUDE: FAILS, AND BY THE SAME MARGIN AS THE OTHERS.  Section 4.

===============================================================================
3. CANDIDATE C -- SQUEEZED VACUUM.  PASSES BOTH QUALITATIVE GATES.
===============================================================================

This is the one the tree had already singled out.  lightbuild.py's OPEN row says
lattice.py's theorem is about the CLASSICAL Maxwell stress tensor, and squeezed
vacuum is precisely the exception: a state in which the energy density at a
spacetime point is genuinely negative.

    KIND: PASSES.  A real rho < 0, and the standard one.

    DEADLINE: PASSES.  Kill the pump and it is gone at c.  Nothing to remove.

        SO TWO INDEPENDENT ROUTES SELECT THE SAME CANDIDATE.  The classical
        theorem says the only gap is non-classical; the teardown deadline says
        the lead must clear at c.  They converge on squeezed vacuum, and that
        convergence is why this file exists rather than stopping at candidate A.

    AND THEN IT FAILS ON MAGNITUDE, which is gate three.

===============================================================================
4. THE GATE THAT DECIDES ALL OF THEM, AND IT IS STRUCTURAL
===============================================================================

Quantum field theory does not let you have negative energy for free.  The
FORD-ROMAN quantum inequality (massless scalar, four dimensions) bounds the
sampled energy density available over a sampling length L = c tau:

        |rho|  <=  3 hbar c / (32 pi^2 L^4)

and the Casimir law has the same shape, pi^2 hbar c / (720 d^4).

    NOW PUT THAT AGAINST THE REQUIREMENT, AND NOTICE THE EXPONENTS:

        what is ALLOWED   goes as  L^-4
        what is NEEDED    goes as  R^-2        (c^4 / (G Lambda R^2))

    SO THE SHORTFALL GOES AS R^2, AND SHRINKING ALWAYS HELPS.  M's "small and
    contained" is quantitatively the right direction, and it is the only
    direction that helps at all:

        R (m)        need J/m^3    Ford-Roman     shortfall     Casimir shortfall
        1e-09        1.2124e+61    3.0031e+08     4.037e+52     2.798e+52
        1e-06        1.2124e+55    3.0031e-04     4.037e+58     2.798e+58
        1e-03        1.2124e+49    3.0031e-16     4.037e+64     2.798e+64
        1e+00        1.2124e+43    3.0031e-28     4.037e+70     2.798e+70

    52.6 ORDERS SHORT AT A NANOMETRE AND 70.6 AT A METRE -- the same order of
    shortfall lightbuild.py found for the kugelblitz block, arrived at from a
    completely different direction.

AND THE CROSSOVER HAS A CLOSED FORM, WHICH IS THE RESULT.  Setting
c^4/(G Lambda R^2) = 3 hbar c/(32 pi^2 R^4):

        R  =  l_P sqrt( 3 Lambda / (32 pi^2) )  =  0.307933 l_P

and for Casimir, R = l_P pi sqrt(Lambda / 720) = 0.369917 l_P.

    THE BOUND MEETS THE REQUIREMENT ONLY BELOW THE PLANCK LENGTH -- a third of
    one, and a third of one again.  THE FRAMEWORK FAILS BEFORE THE BOUND DOES.
    This is not "very hard".  It is outside the domain of the theory being used
    to state it, and Lambda -- M's own constant -- is sitting in both crossover
    formulas.

===============================================================================
5. ONE THING THAT DID NOT FIGHT, AND IT IS WORTH RECORDING
===============================================================================

The quantum inequality and the teardown deadline LOOK like they should compound,
and they do not.  The inequality says a deeper negative energy must be BRIEFER:
|rho| <= 3 hbar c/(32 pi^2 (c tau)^4) grows without limit as tau falls.  The
deadline says the lead must be brief.

        SO THE DEADLINE IS EXACTLY THE REGIME THE INEQUALITY IS MOST GENEROUS
        IN.  The two constraints point the SAME WAY.

    teardown.py's new requirement therefore costs NOTHING against the quantum
    inequality -- it is free, and it is the direction the inequality already
    wanted.  That does not rescue anything, because the failure is on magnitude
    and the magnitude fails by fifty-two orders in the best case.  But a
    requirement that turns out to be free is worth knowing, and if anything ever
    does supply the magnitude, the switchability will not be what stops it.

===============================================================================
WHAT THIS PASS ESTABLISHES
===============================================================================

    A   negative effective mass   FAILS on KIND.  m* is band curvature, not
                                  T_00.  No energy condition is violated.

    B   Casimir                   PASSES kind.  FAILS deadline (mechanical, and
                                  anchored to positive-mass plates) and
                                  magnitude (2.798e52 short at a nanometre).

    C   squeezed vacuum           PASSES kind AND deadline -- the only candidate
                                  that does, and selected independently by two
                                  routes.  FAILS magnitude by 4.037e52 at a
                                  nanometre, 4.037e70 at a metre.

    STRUCTURAL   both quantum bounds go as L^-4 and the requirement as R^-2, so
                 the shortfall goes as R^2 and SMALLER IS ALWAYS BETTER -- but
                 the crossover is 0.3079 l_P (Ford-Roman) and 0.3699 l_P
                 (Casimir), BELOW THE PLANCK LENGTH, with Lambda in both closed
                 forms.

    FREE         the teardown deadline costs nothing against the quantum
                 inequality; the two point the same way.

    NOT CLAIMED  that the list is exhaustive.  Three candidates were named and
                 three were run.  A fourth may exist and this file does not
                 speak to it.
"""

import math
import sys

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34

KIND = "supplies rho < 0"
DEADLINE = "switches off in ~R/c"
MAGNITUDE = "enough of it"
GATES = (KIND, DEADLINE, MAGNITUDE)


def lambda_value():
    import phase1
    return phase1.lam()


def planck_length():
    return math.sqrt(HBAR * G / C ** 3)


# ---------------------------------------------- the requirement

def rho_needed(R_m):
    """E_transition(R) spread over R^3  =  c^4 / (G Lambda R^2)."""
    return C ** 4 / (G * lambda_value() * R_m ** 2)


REQUIREMENT_SCALES_AS = -2


# ---------------------------------------------- the bounds

def ford_roman(L_m):
    """|rho| <= 3 hbar c / (32 pi^2 L^4).  Massless scalar, 4D."""
    return 3.0 * HBAR * C / (32.0 * math.pi ** 2 * L_m ** 4)


def casimir(d_m):
    """|rho| = pi^2 hbar c / (720 d^4).  Ideal plates."""
    return math.pi ** 2 * HBAR * C / (720.0 * d_m ** 4)


BOUNDS_SCALE_AS = -4


def bounds_fall_faster_than_the_requirement():
    return BOUNDS_SCALE_AS < REQUIREMENT_SCALES_AS


def shortfall(R_m, bound=ford_roman):
    return rho_needed(R_m) / bound(R_m)


def smaller_is_better(a=1.0, b=1e-9):
    return shortfall(b) < shortfall(a)


def shortfall_scales_as_R_squared(R1=1e-9, R2=1e-6, tol=1e-9):
    ratio = shortfall(R2) / shortfall(R1)
    return abs(ratio - (R2 / R1) ** 2) <= tol * ratio


# ---------------------------------------------- the crossovers

def crossover_ford_roman():
    """c^4/(G Lambda R^2) = 3 hbar c/(32 pi^2 R^4)."""
    return math.sqrt(3.0 * G * lambda_value() * HBAR / (32.0 * math.pi ** 2 * C ** 3))


def crossover_ford_roman_closed():
    """R / l_P = sqrt(3 Lambda / (32 pi^2))."""
    return math.sqrt(3.0 * lambda_value() / (32.0 * math.pi ** 2))


def crossover_casimir():
    return math.sqrt(math.pi ** 2 * HBAR * C * G * lambda_value() / (720.0 * C ** 4))


def crossover_casimir_closed():
    """R / l_P = pi sqrt(Lambda / 720)."""
    return math.pi * math.sqrt(lambda_value() / 720.0)


def crossover_is_sub_planckian():
    return (crossover_ford_roman() < planck_length()
            and crossover_casimir() < planck_length())


# ---------------------------------------------- the candidates

# (name, kind, deadline, magnitude, why it fails first)
CANDIDATES = (
    ("negative effective mass", False, True, None,
     "m* = hbar^2/(d2E/dk2) is band curvature, not T_00; no EC is violated"),
    ("Casimir", True, False, False,
     "switching means MOVING PLATES -- mechanical, slower than c, and anchored "
     "to positive-mass plates"),
    ("squeezed vacuum", True, True, False,
     "passes both qualitative gates and fails Ford-Roman by 52.6 orders at 1 nm"),
)


def first_gate_failed(name):
    for n, k, d, m, _why in CANDIDATES:
        if n != name:
            continue
        if not k:
            return KIND
        if not d:
            return DEADLINE
        if m is False:
            return MAGNITUDE
        return None
    raise KeyError(name)


def any_candidate_passes():
    return any(k and d and m for _n, k, d, m, _w in CANDIDATES)


def only_one_passes_both_qualitative_gates():
    return [n for n, k, d, _m, _w in CANDIDATES if k and d] == ["squeezed vacuum"]


EFFECTIVE_MASS_IS = "band curvature"
EFFECTIVE_MASS_IS_NOT = "T_00"


def effective_mass_violates_an_energy_condition():
    return False


# ---------------------------------------------- the alignment

def ford_roman_allows_more_when_briefer(tau_long=1e-9, tau_short=1e-15):
    """The inequality grows without limit as tau falls."""
    return ford_roman(C * tau_short) > ford_roman(C * tau_long)


def deadline_costs_anything_against_the_inequality():
    """The deadline wants brief; the inequality is most generous when brief."""
    return not ford_roman_allows_more_when_briefer()


LIST_IS_EXHAUSTIVE = False


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("0. THE SPEC -- THREE GATES, AND THE THIRD IS NEW HERE")
    for g in GATES:
        print("     %s" % g)
    chk("how many gates", len(GATES), 3)

    print("\n1. CANDIDATE A -- NEGATIVE EFFECTIVE MASS")
    chk("what m* is", EFFECTIVE_MASS_IS, "band curvature")
    chk("what it is not", EFFECTIVE_MASS_IS_NOT, "T_00")
    chk("does it violate an energy condition",
        effective_mass_violates_an_energy_condition(), False)
    chk("FIRST GATE FAILED", first_gate_failed("negative effective mass"), KIND)
    print("       real, measured and switchable -- and the WRONG QUANTITY.")
    print("       'negative mass' is one phrase for two things and only one")
    print("       of them is exotic.")

    print("\n2. CANDIDATE B -- CASIMIR")
    near("rho at d = 10 nm (J/m^3)", casimir(1e-8), 4.33375e4, 1e-4)
    near("  and at d = 1 nm, four orders up", casimir(1e-9), 4.33375e8, 1e-4)
    chk("FIRST GATE FAILED", first_gate_failed("Casimir"), DEADLINE)
    print("       switching means MOVING PLATES: mechanical, slower than c,")
    print("       and the negative region is anchored to positive-mass plates.")

    print("\n3. CANDIDATE C -- SQUEEZED VACUUM")
    chk("passes KIND and DEADLINE", only_one_passes_both_qualitative_gates(), True)
    chk("FIRST GATE FAILED", first_gate_failed("squeezed vacuum"), MAGNITUDE)
    print("       the only one that passes both qualitative gates, and it is")
    print("       the same candidate lightbuild.py left OPEN -- two independent")
    print("       routes selecting one thing.")

    print("\n4. THE GATE THAT DECIDES ALL THREE")
    chk("bounds scale as L^n, n =", BOUNDS_SCALE_AS, -4)
    chk("the requirement scales as R^n, n =", REQUIREMENT_SCALES_AS, -2)
    chk("  so do the bounds fall faster", bounds_fall_faster_than_the_requirement(), True)
    chk("  and is smaller better", smaller_is_better(), True)
    chk("  does the shortfall go as R^2", shortfall_scales_as_R_squared(), True)
    print("     %-10s %14s %14s %13s %13s"
          % ("R (m)", "need J/m^3", "Ford-Roman", "FR short", "Cas short"))
    for R in (1e-9, 1e-6, 1e-3, 1.0):
        print("     %-10.0e %14.4e %14.4e %13.3e %13.3e"
              % (R, rho_needed(R), ford_roman(R), shortfall(R),
                 shortfall(R, casimir)))
    near("shortfall at 1 nm", shortfall(1e-9), 4.037e52, 1e-3)
    near("  in orders", math.log10(shortfall(1e-9)), 52.606, 1e-3)
    near("shortfall at 1 m", shortfall(1.0), 4.037e70, 1e-3)
    near("  in orders", math.log10(shortfall(1.0)), 70.606, 1e-3)
    print("     THE CROSSOVER, AND IT HAS A CLOSED FORM:")
    near("Ford-Roman crossover (m)", crossover_ford_roman(), 4.976981e-36, 1e-5)
    near("  in Planck lengths", crossover_ford_roman() / planck_length(), 0.307933, 1e-5)
    near("  closed form sqrt(3 Lambda/(32 pi^2))", crossover_ford_roman_closed(),
         0.307933, 1e-5)
    near("Casimir crossover (m)", crossover_casimir(), 5.978797e-36, 1e-5)
    near("  in Planck lengths", crossover_casimir() / planck_length(), 0.369917, 1e-5)
    near("  closed form pi sqrt(Lambda/720)", crossover_casimir_closed(), 0.369917, 1e-5)
    chk("IS THE CROSSOVER SUB-PLANCKIAN", crossover_is_sub_planckian(), True)
    print("       THE FRAMEWORK FAILS BEFORE THE BOUND DOES.  Not 'very hard' --")
    print("       outside the domain of the theory stating it.  And Lambda is")
    print("       sitting in both closed forms.")

    print("\n5. THE ONE THING THAT DID NOT FIGHT")
    chk("does the inequality allow more when briefer",
        ford_roman_allows_more_when_briefer(), True)
    chk("  so does the deadline cost anything against it",
        deadline_costs_anything_against_the_inequality(), False)
    print("       the deadline is exactly the regime the inequality is most")
    print("       generous in.  teardown.py's requirement is FREE.")

    print("\n  THE VERDICT")
    print("     %-26s %7s %9s %10s" % ("candidate", "kind", "deadline", "magnitude"))
    for n, k, d, m, _w in CANDIDATES:
        print("     %-26s %7s %9s %10s"
              % (n, k, d, "n/a" if m is None else m))
    chk("DOES ANY CANDIDATE PASS", any_candidate_passes(), False)
    chk("is the list exhaustive", LIST_IS_EXHAUSTIVE, False)
    print("       three were named and three were run.  A fourth may exist and")
    print("       this file does not speak to it.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  Three candidates, three gates, and each fails at a different one.
  Negative effective mass fails at the FIRST: m* is the curvature of a
  band, not T_00, so a negative-mass polariton violates no energy
  condition and would not bend spacetime the wrong way -- "negative mass"
  is one phrase for two things and only one is exotic.  Casimir supplies a
  genuine rho < 0 and fails the DEADLINE, because switching it off means
  moving plates, which is mechanical and anchored to positive mass.
  Squeezed vacuum passes both qualitative gates -- the only one that does,
  and the same candidate lightbuild.py had already left open, so two
  independent routes select it -- and then fails on MAGNITUDE.  That third
  gate is new here and it is structural: the Ford-Roman and Casimir bounds
  both go as L^-4 while the requirement goes as R^-2, so the shortfall goes
  as R^2 and shrinking always helps, which makes "small and contained"
  quantitatively the right instinct and the only one that helps.  It is
  still 52.6 orders short at a nanometre and 70.6 at a metre, and the
  crossover where the bound would finally meet the requirement is
  0.307933 l_P for Ford-Roman and 0.369917 l_P for Casimir -- BELOW the
  Planck length, with Lambda sitting in both closed forms.  The framework
  fails before the bound does.  One consolation, recorded because it is
  real: the quantum inequality is most generous exactly where the teardown
  deadline wants to live, so switchability is free and will not be what
  stops a lead that ever does supply the magnitude.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
